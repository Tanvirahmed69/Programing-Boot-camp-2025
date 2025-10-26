##Check leap year (div by 4 and not by 100) or (div by 400) -> (সংখ্যাটাকে ৪ দিয়ে ভাগ করলে ভাগশেষ ০ হতে হবে এবং ১০০ দিয়ে ভাগ করলে ভাগশেষ ১ হতে হবে) অথবা (সংখ্যাটাকে ৪০০ দিয়ে ভাগ করলে ভাগশেষ ০ হবে) 

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
