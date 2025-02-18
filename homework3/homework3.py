#Question 1
def compute_power(x,y):
    P=1
    for i in range(1, y+1):
        P=P*x
    return P

x = 2
y = 3
print(compute_power(x, y))

#Question 2
def temperatureRange():
    readings= [15, 14, 17, 20, 23, 28, 20]
    return (min(readings), max(readings))

print(temperatureRange())

#Question 3
def isWeekend(day):
    Days = {'Weekdays': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'Weekends': ['Sunday', 'Saturday']}
    if day in Days['Weekdays']:
        return False
    elif day in Days['Weekends']:
        return True
    else:
        return None

print(isWeekend('Friday'))
print(isWeekend('Saturday'))

#Question 4
def fuel_efficiency(distance, fuel):
    E = distance / fuel  # efficiency
    return(E)

distance = 70  # miles
fuel = 21.5  # gallons
print(fuel_efficiency(distance, fuel))  #When I use the run and debug feature of vscode it gives me 3.25 as the answer but when I try individually running this line or any other line it tells me there is an indentation error even though there is clearly not. I have tried retyping it, using spaces instead of enter or tab, and even copy pasting from another document but nothing fixes it.

#Question 5
def decodeNumbers(n):
    last_digit = n % 10 #modulus by ten will always return last digit of a number
    rest_of_number = n // 10 #floor division by ten gives you number and removes last digit
    #calculate remaining digits in rest of number
    num_digits = 0 #define number of digits variable and start it at zero
    temp = rest_of_number #temporary variable to prevent modifying actual rest of number variable
    while temp > 0: #a while loop that will continue until temp = 0
        temp //= 10 #divides temp by 10 and gets rid of remainder. Since its 10, the remainder will simply be whatever is in the final digit of the number.
        num_digits += 1 # after each iteration, the num_digits variable will increase by 1. Since this continues until temp variable reaches zero, we are basically moving the number of digits from the temp variable to the num_digits variable. This tells us how many digits are in the rest_of_number variable.

    new_number = last_digit * (10 ** num_digits) + rest_of_number #This variable will be the last digit we found multiplied by ten to the number of digits in the rest of number variable. This basically turns a number (1-9) into a number times 10^x. (i.e. 5 * 10**4 = 50000). We then add the rest of number variable and that will give us our new number.
    return new_number

n=12345
print(decodeNumbers(n))

#Question 6
#6.1
def find_max_with_for_loops(nums):
    max_number = nums[0] #holding variable beginning with the first element of the list
    for num in nums:
        if num > max_number:
            max_number = num #update max_number with current number that is greater than previous number
    return max_number

nums = [2024, 98, 131, 2, 3, 72]
print(find_max_with_for_loops(nums))

def find_min_with_for_loops(nums):
    min_number = nums[0]
    for num in nums:
        if num < min_number:
            min_number = num
    return min_number

print(find_min_with_for_loops(nums))

#6.2
def find_max_with_while_loops(nums):
    greatest_num = nums[0]
    i = 1 #start with second element of list (non inclusive)
    while i < len(nums): #continue until reaching the end (length) of the list
        if nums[i] > greatest_num: #condition for an element i in the list being greater than the holding variable greatest num
            greatest_num = nums[i]  #update holding variable to new number
        i += 1 #move on to next element in list
    return greatest_num

print(find_max_with_while_loops(nums))

def find_min_with_while_loops(nums):
    least_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < least_num:
            least_num = nums[i]
        i += 1
    return least_num

print(find_min_with_while_loops(nums))

#Question 7
def vowel_and_consonant_count(text):
    vowels = {'A': True, 'E': True, 'I': True, 'O': True, 'U': True, 'a': True, 'e': True, 'i': True, 'o': True, 'u': True} #Dictionary to define what my vowels are, each vowel is labelled true
    vowel_count = 0
    consonant_count = 0 #Begin counts at 0
    for char in text:
        if char.isalpha(): #Check that character is letter
            if char in vowels: #check that character is in dictionary
                vowel_count += 1 #add to cowel counter
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))

#Question 8
def digital_root(int):
    sum_digits = 0 #define variable that will be the sum of all our digits and start it at zero
    while int > 0:
        sum_digits += int % 10 #takes last digit of integer and adds it to our sum variable
        int //= 10 #updates integer and removes the digit we just added to our sum
    return sum_digits

int = 2468
print(digital_root(int))



