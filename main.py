start = int(input("pochatkove chislo: "))
end = int(input("kinceve chislo: "))
sum_of_range = 0
for num in range(start + 1, end):
    sum_of_range += num
print("suma chisel y diapazoni mezhdu", start, "i", end, "=", sum_of_range)