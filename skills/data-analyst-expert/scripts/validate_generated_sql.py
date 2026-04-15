#!/usr/bin/env python3

"""
Basic validation helper for generated BigQuery SQL.

This script is intentionally lightweight for v1.
It does not parse full SQL semantics.
It performs simple guardrail checks that can be expanded later.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


FORBIDDEN_PATTERNS = [
    r"\bDELETE\b",
    r"\bUPDATE\b",
    r"\bINSERT\b",
    r"\bMERGE\b",
    r"\bDROP\b",
    r"\bTRUNCATE\b",
    r"\bCREATE\s+OR\s+REPLACE\b",
]

RECOMMENDED_PATTERNS = [
    r"`[^`]+\.[^`]+\.[^`]+`",
]


@dataclass
class ValidationResult:
    is_valid: bool
    errors: list[str]
    warnings: list[str]


def read_sql_input() -> str:
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        return path.read_text(encoding="utf-8")

    data = sys.stdin.read()
    if not data.strip():
        raise ValueError("No SQL input provided. Pass a file path or pipe SQL via stdin.")
    return data


def validate_sql(sql: str) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    normalized_sql = sql.upper()

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, normalized_sql, flags=re.IGNORECASE):
            errors.append(f"Forbidden SQL pattern detected: {pattern}")

    if "SELECT *" in normalized_sql:
        warnings.append("Query contains SELECT *. Prefer explicit column selection.")

    if "LIMIT" not in normalized_sql and "GROUP BY" not in normalized_sql:
        warnings.append("No LIMIT detected in a non-obviously aggregated query.")

    has_fully_qualified_table = any(
        re.search(pattern, sql, flags=re.IGNORECASE) for pattern in RECOMMENDED_PATTERNS
    )
    if not has_fully_qualified_table:
        warnings.append("No fully qualified backticked table reference detected.")

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


def main() -> int:
    try:
        sql = read_sql_input()
        result = validate_sql(sql)

        print("SQL Validation Report")
        print("=====================")
        print(f"Valid: {result.is_valid}")

        if result.errors:
            print("\nErrors:")
            for error in result.errors:
                print(f"- {error}")

        if result.warnings:
            print("\nWarnings:")
            for warning in result.warnings:
                print(f"- {warning}")

        return 0 if result.is_valid else 1

    except Exception as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())