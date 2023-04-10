first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')

if first_number > second_number:
    print(f"{first_number=} it's greater than {second_number=}")
elif first_number == second_number:
    print(f"{first_number=} is equal to the {second_number=}")    
else:
    print(f"{second_number=} it's greater than {first_number=}")
