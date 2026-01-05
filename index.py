import os
import argparse
import logging

# --- CALCULATION FUNCTIONS ---
def calculate_tax(salary):
    if salary < 50000:
        tax = salary * 0.02
    elif salary <= 100000:
        tax = salary * 0.03
    elif salary <= 250000:
        tax = salary * 0.05
    elif salary <= 500000:
        tax = salary * 0.07
    else:
        tax = salary * 0.10
    return tax

def calculate_nhiflevy(salary):
    if salary < 20000:
        nhif = 300
    elif salary <= 80000:
        nhif = 500
    elif salary <= 120000:
        nhif = 1200
    elif salary <= 200000:
        nhif = 1800
    elif salary <= 250000:
        nhif = 2500
    elif salary <= 500000:
        nhif = 4500
    elif salary <= 1000000:
        nhif = 7500
    else:
        nhif = 9000
    return nhif

def calculate_nssflevy(salary):
    if salary < 100000:
        nssf = 1500
    elif salary <= 500000:
        nssf = 2500
    elif salary <= 1000000:
        nssf = 4500
    else:
        nssf = 8500
    return nssf

def calculate_housinglevy(salary):
    return salary * 0.025

def get_salary_breakdown(salary):
    """Calculates all deductions and returns a dictionary of results."""
    tax = calculate_tax(salary)
    nhif = calculate_nhiflevy(salary)
    nssf = calculate_nssflevy(salary)
    housing = calculate_housinglevy(salary)
    
    total_deductions = tax + nhif + nssf + housing
    net_salary = salary - total_deductions
    
    return {
        "gross": salary,
        "tax": tax,
        "nhif": nhif,
        "nssf": nssf,
        "housing": housing,
        "total_deductions": total_deductions,
        "net": net_salary
    }

# --- FILE WRITING AND GENERATION ---
SAMPLE_EMPLOYEES = [
    ("Peter Ilunga", 53400.00),
    ("Jane Kyakilika", 880000.00),
    ("Alice Kalekesha", 23500.00),
    ("Linguja LInguja", 1555000.00),
    ("Esther Liswan", 56800.00),
    ("Evans Ngosa", 56700.00),
    ("Frank Mumba", 67800.00),
    ("Ireen Mants", 555000.00),
    ("Henry Mwanza", 678090.00),
    ("Saidati Ebeni", 98400.00),
    ("Debora Mutenda", 422100.00),
    ("Niza Sikapizie", 78900.00),
]


def generate_and_save_records(filename="payroll_report.txt", employees=None):
    """Generates records from the sample list and saves to a CSV-like file.

    Returns the path to the generated file.
    """
    if employees is None:
        employees = SAMPLE_EMPLOYEES

    logging.info("Generating records for %d employees...", len(employees))

    try:
        with open(filename, "w", encoding="utf-8") as file:
            # Write the Header to the file (CSV style)
            header = "Name,Gross,Tax,NHIF,NSSF,Housing,Total Deductions,Net\n"
            file.write(header)

            for name, salary in employees:
                breakdown = get_salary_breakdown(salary)
                line = (
                    f'{name},{breakdown["gross"]:.2f},{breakdown["tax"]:.2f},'
                    f'{breakdown["nhif"]:.2f},{breakdown["nssf"]:.2f},'
                    f'{breakdown["housing"]:.2f},{breakdown["total_deductions"]:.2f},'
                    f'{breakdown["net"]:.2f}\n'
                )
                file.write(line)

        logging.info("Saved payroll report to %s", filename)
        return os.path.abspath(filename)

    except Exception as e:
        logging.exception("Failed to generate or save records: %s", e)
        raise


def main():
    parser = argparse.ArgumentParser(description="Generate payroll report")
    parser.add_argument("--output", "-o", default="payroll_report.txt", help="Output filename")
    parser.add_argument("--print", action="store_true", help="Print generated report to stdout")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    output_path = generate_and_save_records(filename=args.output)

    print(f"Report written to: {output_path}")

    if args.print:
        print("\n---- Report contents ----\n")
        with open(output_path, "r", encoding="utf-8") as f:
            print(f.read())


if __name__ == "__main__":
    main()
