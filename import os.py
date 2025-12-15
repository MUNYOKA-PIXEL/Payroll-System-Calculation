import os

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
def generate_and_save_records():
    """Generates records from the fixed sample list and saves to file."""
    filename = "payroll_report.txt"
    
    # Updated list with Names and Fixed Salaries
    sample_employees = [
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

    print(f"\nGenerating records for {len(sample_employees)} employees...")
    
    try:
        with open(filename, "w") as file:
            # Write the Header to the file
            header = f" | {'Name':<15} | {'Gross Salary':>12} | {'PAYE Tax':>10} | {'NHIF':>8} | {'NSSF':>8} | {'Housing':>10} | {'Net Salary':>12} |\n"
            divider = "-" * 97 + "\n"
            
            file.write("COMPANY PAYROLL REPORT\n")
            file.write(divider)
            file.write(header)
            file.write(divider)
            
            # Print header to console as well
            print("-" * 97)
            print(header.strip())
            print("-" * 97)
            
            # Loop through the specific list of tuples (name, salary)
            for name, salary in sample_employees:
                
                # Calculate breakdown using the fixed salary
                data = get_salary_breakdown(salary)
                
                # Format the line string
                line = (f" | {name:<15} | "
                        f"{data['gross']:>12,.2f} | "
                        f"{data['tax']:>10,.2f} | "
                        f"{data['nhif']:>8,.2f} | "
                        f"{data['nssf']:>8,.2f} | "
                        f"{data['housing']:>10,.2f} | "
                        f"{data['net']:>12,.2f} | \n")
                
                # Write to file
                file.write(line)
                
                # Print to console for immediate feedback
                print(line.strip())
                
            file.write(divider)
            print("-" * 97)
            print(f"\nSUCCESS: Records have been saved to '{filename}'.")
            
            # Display absolute path for clarity
            print(f"File location: {os.path.abspath(filename)}")
            
    except IOError as e:
        print(f"Error writing to file: {e}")

# --- MAIN PROGRAM MENU ---
def main():
    while True:
        print("\n--- PAYROLL SYSTEM MENU ---")
        print("1. Generate Employee Records from List (Save to File)")
        print("2. Calculate Single Salary (Manual Input)")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            generate_and_save_records()
        elif choice == '2':
            try:
                salary = float(input("\nEnter your Salary: "))
                if salary <= 0:
                    print("Salary must be a positive number.")
                else:
                    data = get_salary_breakdown(salary)
                    print(" \n Salary Breakdown")
                    print(f"Gross Salary: KSh {data['gross']:,.2f}")
                    print(f"PAYE Tax:     KSh {data['tax']:,.2f}")
                    print(f"NHIF Levy:    KSh {data['nhif']:,.2f}")
                    print(f"NSSF Levy:    KSh {data['nssf']:,.2f}")
                    print(f"Housing Levy: KSh {data['housing']:,.2f}")
                    print(f"Total Ded.:   KSh {data['total_deductions']:,.2f}")
                    print(f"Net Salary:   KSh {data['net']:,.2f}")
            except ValueError:
                print("Invalid input! Please enter a numeric salary.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()