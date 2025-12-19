grades = []

print("Enter grades (type done to stop):")

while True:
    g = input("Grade: ")
    if g == "done":
        break
    grades.append(int(g))

a = b = c = d = f = 0

for g in grades:
    if g >= 90:
        a += 1
    elif g >= 80:
        b += 1
    elif g >= 70:
        c += 1
    elif g >= 60:
        d += 1
    else:
        f += 1

print("\nTotal Students:", len(grades))
print("Average Grade:", sum(grades) / len(grades))
print("Highest Grade:", max(grades))
print("Lowest Grade:", min(grades))

print("\nGrade Distribution:")
print("A:", a)
print("B:", b)
print("C:", c)
print("D:", d)
print("F:", f)