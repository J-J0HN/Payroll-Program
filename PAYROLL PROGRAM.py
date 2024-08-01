#Import math enables 2 decimal places for outputs
import math


#Title and Date
print()
print("=PAYROLL PROGRAM=") 
print() 
print("-This program is written by Joyal John at 12/12/19-")
print()

#The print() spaces and asterisks are used to space out and neaten up the payslip
print("******************************************************************************") 
print() 

#Basic Inputs 
name = input("Input Employee Name:")
print("Employee =",name)
employeehours = float(input("Input Hours Worked In A Week:"))
hourlyPay = float(input("Input Hourly Pay:"))
MobilityBenefitsMonthly = float(input("Input Monthly Mobility Benefits:"))
ChildBenefitMonthly = float(input("Input Monthly Child Benefits:"))

#The print()spaces and lines are used to space out and neaten up the payslip again
print() 
print("------------------------------------------------------------------------------") 
print()

#Gross Weekly Pay Calculation
GrossWeeklyPay = hourlyPay*employeehours


#Over Time calculation
if employeehours > 35:
    overtime = employeehours - 35
    print("           Overtime hours = ""%.2f"%overtime)  #Added spaces to all outputs to neatly align
    GrossWeeklyPay = (hourlyPay * 35) + (hourlyPay * overtime * 1.5)
else:
    GrossWeeklyPay = hourlyPay*employeehours

    
#Print for Gross Weekly Pay    
print("         Gross Weekly Pay = £""%.2f"%GrossWeeklyPay)


#Gross Annual Pay calculation and output
GrossAnnualPay = 52 * GrossWeeklyPay
print("         Gross Annual Pay = £""%.2f"%GrossAnnualPay)


#Tax Calculations
if GrossAnnualPay <= 12500: 
    tax = (GrossAnnualPay - 0) * 0
    print("               Annual Tax = £""%.2f"% tax)
    
elif GrossAnnualPay >= 12500 < 50000:
    tax = (GrossAnnualPay - 12500) * 0.2
    print("               Annual Tax = £""%.2f"% tax)

elif GrossAnnualPay >= 50001 < 150000:
    tax = (GrossAnnualPay - 50001) * 0.4
    print("               Annual Tax = £""%.2f"% tax)

elif GrossAnnualPay >= 150001:
    tax = (GrossAnnualPay - 150001) * 0.45
    print("               Annual Tax = £""%.2f"% tax)


#Annual Income With Tax deducted calculation
AnnualIncomeWithTax = GrossAnnualPay - tax
print("      Annual Pay with Tax = £""%.2f"%AnnualIncomeWithTax)


#Weekly Pay With Tax deducted calculation
WeeklyTax = tax/52
WeeklyPayWithTax = GrossWeeklyPay - WeeklyTax
print("      Weekly Pay with Tax = £""%.2f"%WeeklyPayWithTax)


#National Insurance Calculations
if GrossWeeklyPay < 166:
    NationalInsurance = 0
    print("Annual National Insurance = £""%.2f"%NationalInsurance)

elif GrossWeeklyPay >= 166 < 962:
    NationalInsurance = ((GrossWeeklyPay - 166) / 100) * 12
    print("Annual National Insurance = £""%.2f"%NationalInsurance)
 
else:
    x = (GrossWeeklyPay - 166) - 962
    y = (796 / 100) * 12    
    NationalInsurance = ((x / 100) * 2) + y
    print("Annual National Insurance = £""%.2f"%NationalInsurance)


#Weekly National Insurance
WeeklyNationalInsurance = NationalInsurance / 52
print("Weekly National Insurance = £""%.2f"%WeeklyNationalInsurance)


#Annual Mobility Benefits
AnnualMobilityBenefits = MobilityBenefitsMonthly * 12
print(" Annual Mobility Benefits = £""%.2f"%AnnualMobilityBenefits)


#Child Benefit Calc
AnnualChildBenefits = ChildBenefitMonthly * 12
print("    Annual Child Benefits = £""%.2f"%AnnualChildBenefits)


#Net Annual Pay Calculations
NetAnnualPay = AnnualIncomeWithTax - NationalInsurance - tax + AnnualMobilityBenefits + AnnualChildBenefits
print("           Net Annual Pay = £""%.2f"%NetAnnualPay)


#Net Weekly Pay Calculations
NetWeeklyPay = (GrossWeeklyPay - WeeklyNationalInsurance) - WeeklyTax + (MobilityBenefitsMonthly / 4) + (ChildBenefitMonthly / 4)
print("           Net Weekly Pay = £""%.2f"%NetWeeklyPay)


print()
print("******************************************************************************")
