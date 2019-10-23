#Cale (Leafy Vegetable), Daniel, Austin (meme king/ Cowboy), Logan
#9/11/2019
#Doing geometries with python
#Intro
def intro(name):
    print("""
    Welcome to """+name+"""
    please choose an option
    from the list below

    1: Square area and perimiter
    2: Triangle area
    3: Circle area
    4: Cube volume
    5: quit
""")

def menu():
    while True:
        intro("Geometry Calculator")
        choice = input("pick an option 1, 2, 3, 4, or 5")
        if choice == "1":
                Square()
        elif choice == "2":
                triangle()
        elif choice == "3":
                circle()
        elif choice == "4":
                cube()
        elif choice == "5":
            verify = option4()
            if verify:
                break
            else:
                continue
        else:
                print("Invalid Choice")

def option4():
    verify = input("Are you sure you want to quit")
    verify = verify.lower()
    if "y" in verify:
        return True
    else:
        return False

##Square
#To make sure that you cant just input a string and break the program, we put in the try command
def Square():
  while True:
    squ_side = input("Square Side Length → ")
    if "." in squ_side:
      squ_side = squ_side.replace(".", "")
    if squ_side.isdigit():
      squ_side=float(squ_side)
      break
    else:
      print("There was an error with the square side length, please make sure that you inputed ONLY numbers")
  
  #testing for negative numbers which may or may not be needed due to the "isdigit" above
  while True:
    if squ_side > 0:
      break
    else:
      print("There was an incorrect sidelength")
    
  #Calculations
  squ_area = float(squ_side) ** 2
  squ_peri = float(squ_side) * 4
  if squ_side <= 0:
    print("There was an incorrect sidelength")
    squ_side = 1
  #Picture formatting
  squr_pic = str.format(''' 
     _____     side = {2: 1.2f}
    |     |    p = {0: 1.2f}
    |     |    a = {1: 1.2f}
    |_____|''',squ_peri,squ_area,squ_side)

  print(squr_pic)

#Triangle
def triangle():

    #input for triangle base and verification of number
    while True:
            tri_base = input("Triangle Base Length → ")
            if tri_base.isdigit():
                tri_base=float(tri_base)
                break
            else:
                print("There was an error with the Triangle Base Length, please make sure that you inputed ONLY numbers")

    #input for triangle height and verification of number
    while True:
            tri_height = input("Triangle Height Lenght → ")
            if tri_height.isdigit():
                tri_height=float(tri_base)
                break
            else:
                print("There was an error with the Triangle Heigth, please make sure that you inputed ONLY numbers")

    #calculations
    area = float(tri_base) * float(tri_height) / 2
    tri_pic = str.format('''
               /\       
              / |\      
             /  | \    
            /   |  \    
           /    {0: 1.2f} \   
          /     |    \  
         /      |     \ 
        /_______{1: 1.2f}____\
        area = {2: 1.2f}
        ''',tri_height,tri_base,area)
    print(tri_pic)


#Circle
def circle():
  while True:
    circ_radius = input("Input your circle radius")
    if "." in circ_radius:
        circ_radius = circ_radius.replace(".", "9223372036854775807")
    if circ_radius.isdigit() and "9223372036854775807" in circ_radius:
      circ_radius =circ_radius.replace("9223372036854775807", ".")
      circ_radius=float(circ_radius)
      break
    elif circ_radius.isdigit():
      circ_radius = float(circ_radius)
      break
    else:
        print("Your input is bad, you cant letter in here")
  r= float(circ_radius)
  pi=3.14
  c=2*pi*r
  circ_pic =str.format('''
                     ooo OOO OOO ooo
                 oOO                 OOo
             oOO                         OOo
          oOO                               OOo
        oOO                                   OOo
      oOO                                       OOo
     oOO                                         OOo
    oOO                                           OOo
   oOO                                             OOo  Radius = {0: 1.2f}
   oOO                                             OOo  
   oOO                                             OOo
   oOO                                             OOo
   oOO                                             OOo  Circumfrence = {1: 1.2f}
    oOO                                            OOo
     oOO                                         OOo
      oOO                                       OOo
        oOO                                   OOo
          oO                                OOo
             oOO                         OOo
                 oOO                 OOo
                     ooo OOO OOO ooo
                     ''',r,c)
  print(circ_pic)
#Cube
def cube():
  try:
      cube_side = int(input("Cube Side Length → "))
  except:
    cube_side = 1
    print("err 404: Cube side is a string")
  volume = float(cube_side) ** 3
  pic_cube = str.format(''' 
   .___________,
   |`          :\\
   | `         : \\
   |  `        :  \\
   |   +-----------+
   |__ : ______:   :
   `   :        \\  :
    `  :         \\ : Side = {0: 1.2f}
     ` :          \\:
      `:___________>
      volume = {1: 1.2f}
  ''',cube_side,volume)
  print(pic_cube)

menu()
input("Enter to Close")
