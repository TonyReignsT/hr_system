with open("hr_system.txt") as employees:
    for employee in employees:
        data = employee.split()
        name = data[0]
        title = data[2]
        employee_id = data[1]
        salary = float(data[3])
        paycheck = salary / 24

        if title == "Engineer":
            paycheck += 1000
        print(f"{name} (ID: {employee_id}), {title} - ${paycheck:.2f}) ")