#By: Sabria Fafach
#Date: April 4, 2025
#Title: Employee_program.py


import Employee_class

def main():
    emplist=[]
    for count in range(1,4):
        name=input(f"Enter the name of employee {count}:")
        IDnum=int(input(f"Enter the ID number of employee {count}:"))
        dpmt=input(f"Enter the department of employee {count}:")
        title=input(f"Enter the job title of employee {count}:")
        employee=Employee_class.Employee(name,IDnum,dpmt, title)
        emplist.append(employee)

    empnum = 0

    for employee in emplist:
        empnum+=1
        print(f"The name of employee {empnum} is {employee.get_name()}.")
        print(f"The ID number of employee {empnum} is {employee.get_IDnum()}.")
        print(f"The department of employee {empnum} is {employee.get_dpmt()}.")
        print(f"The job title of employee {empnum} is {employee.get_Title()}")

if __name__ == '__main__':
    main()



