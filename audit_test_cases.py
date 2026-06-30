# ============================================================
# QA Test Case Auditor
# Author: Ascol Parajuli
# Purpose: Reads a CSV of test cases and flags incomplete ones
# ============================================================

import csv

def audit_test_cases(filename):
    incomplete = []
    complete = []
    total = 0

    print("\n========================================")
    print("       QA TEST CASE AUDIT REPORT")
    print("========================================\n")

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            total += 1
            # Check if expected_result is missing or empty
            if not row['expected_result'].strip():
                incomplete.append(row)
            else:
                complete.append(row)

    # Print incomplete test cases
    print(f"❌ INCOMPLETE TEST CASES ({len(incomplete)} found):")
    print("-" * 40)
    if incomplete:
        for tc in incomplete:
            print(f"  ID: {tc['id']}")
            print(f"  Title: {tc['title']}")
            print(f"  Status: {tc['status']}")
            print(f"  Issue: Missing expected result")
            print()
    else:
        print("  None — all test cases are complete!\n")

    # Print summary
    print("========================================")
    print("              SUMMARY")
    print("========================================")
    print(f"  Total test cases:    {total}")
    print(f"  Complete:            {len(complete)}")
    print(f"  Incomplete:          {len(incomplete)}")
    print(f"  Completion rate:     {round(len(complete)/total*100)}%")
    print("========================================\n")

# Run the audit
audit_test_cases('test_cases.csv')