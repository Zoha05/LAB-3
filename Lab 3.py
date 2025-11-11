def calculate_energy_charges(units_consumed, customer_type):
    """Calculate energy charges based on units consumed and customer type."""
    
    # Tariff slabs for different customer types
    tariffs = {
        "domestic": [
            (0, 50, 1.95),      # 0-50 units @ 1.95/unit
            (51, 100, 3.00),    # 51-100 units @ 3.00/unit
            (101, 200, 4.50),   # 101-200 units @ 4.50/unit
            (201, float('inf'), 7.50)  # Above 200 units @ 7.50/unit
        ],
        "commercial": [
            (0, 100, 6.50),     # 0-100 units @ 6.50/unit
            (101, 200, 7.50),   # 101-200 units @ 7.50/unit
            (201, float('inf'), 8.50)  # Above 200 units @ 8.50/unit
        ]
    }
    
    if customer_type not in tariffs:
        raise ValueError("Invalid customer type")
        
    total_charge = 0
    remaining_units = units_consumed
    
    for start, end, rate in tariffs[customer_type]:
        if remaining_units <= 0:
            break
            
        slab_units = min(remaining_units, end - start + 1)
        total_charge += slab_units * rate
        remaining_units -= slab_units
        
    return round(total_charge, 2)

def calculate_fixed_charges(customer_type):
    """Calculate fixed charges based on customer type."""
    fixed_charges = {
        "domestic": 50,
        "commercial": 100
    }
    return fixed_charges.get(customer_type, 0)

def calculate_customer_charges(units_consumed):
    """Calculate customer charges based on units consumed."""
    if units_consumed <= 100:
        return 25
    elif units_consumed <= 200:
        return 35
    else:
        return 45

def calculate_electricity_duty(energy_charges):
    """Calculate electricity duty (6% of energy charges)."""
    return round(energy_charges * 0.06, 2)

def generate_bill():
    """Generate electricity bill based on user input."""
    print("\n=== TGNPDCL Electricity Bill Calculator ===\n")
    
    # Get customer details
    customer_name = input("Enter customer name: ")
    service_no = input("Enter service number: ")
    
    # Get customer type
    while True:
        customer_type = input("Enter customer type (domestic/commercial): ").lower()
        if customer_type in ["domestic", "commercial"]:
            break
        print("Invalid customer type! Please enter 'domestic' or 'commercial'")
    
    # Get meter readings
    try:
        previous_reading = float(input("Enter previous meter reading: "))
        current_reading = float(input("Enter current meter reading: "))
        
        if current_reading < previous_reading:
            raise ValueError("Current reading cannot be less than previous reading")
            
        units_consumed = current_reading - previous_reading
        
        # Calculate charges
        energy_charges = calculate_energy_charges(units_consumed, customer_type)
        fixed_charges = calculate_fixed_charges(customer_type)
        customer_charges = calculate_customer_charges(units_consumed)
        electricity_duty = calculate_electricity_duty(energy_charges)
        
        total_bill = energy_charges + fixed_charges + customer_charges + electricity_duty
        
        # Print the bill
        print("\n" + "=" * 40)
        print("TGNPDCL ELECTRICITY BILL")
        print("=" * 40)
        print(f"Customer Name: {customer_name}")
        print(f"Service No: {service_no}")
        print(f"Customer Type: {customer_type.title()}")
        print("-" * 40)
        print(f"Previous Reading: {previous_reading:.2f}")
        print(f"Current Reading: {current_reading:.2f}")
        print(f"Units Consumed: {units_consumed:.2f}")
        print("-" * 40)
        print("Charges Breakdown:")
        print(f"Energy Charges (EC): ₹{energy_charges:.2f}")
        print(f"Fixed Charges (FC): ₹{fixed_charges:.2f}")
        print(f"Customer Charges (CC): ₹{customer_charges:.2f}")
        print(f"Electricity Duty (ED): ₹{electricity_duty:.2f}")
        print("-" * 40)
        print(f"Total Bill Amount: ₹{total_bill:.2f}")
        print("=" * 40)
        
    except ValueError as e:
        print(f"\nError: {str(e)}")
        print("Please enter valid numeric values for meter readings.")

if __name__ == "__main__":
    while True:
        generate_bill()
        choice = input("\nGenerate another bill? (yes/no): ").lower()
        if choice != 'yes':
            print("\nThank you for using TGNPDCL Bill Calculator!")
            break