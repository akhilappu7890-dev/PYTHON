attend = [18,20,19,15,21]
full = 0
total = 0
for student in attend:
    if student >=20:
        print('full')
        full = full + 1
    else:
        print('not full')
        total = total + student
        print('full :',full)
        print('total attendance',total)