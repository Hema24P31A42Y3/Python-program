thickness=int(input("enetr the thickness : "))
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness)+c+(c*i).ljust(thickness))
