import pages


#I didn't finish adding the choices for pages that don't have more than one path.
#I didn't fix the choices for the pages that had a path split in the middle of the page
#I don't know how to get it to print both the page and the choice for the path; right now it only prints the page and the path stops.
#I don't know if any of this is helpful; if I had more time, I would try to work it out.
#You guys don't have to use this if it isn't helpful at all.


def choice1():
   print(pages.page4)

def choice4():
   print(pages.page10)
   
def choice7():
   choice7=input("\nDo you want to head northeast or south? ").lower()
   if choice7=="northeast":
      print(pages.page20)
   elif choice7=="south":
      print(pages.page16_1)
   else:
      print("Invalid input")
      choice7()

def choice8():
   print(pages.page44)

##def choice9_1():
   
def choice10():
   print(pages.page11)

def choice11():
   print(pages.page14)

def choice12():
   choice12=input("\nDo you want to take your chances with the diving birds? ").lower()
   if choice12=="no":
      print(pages.page31)
   elif choice12=="yes":
      print(pages.page28)
   else:
      print("Invalid input")
      choice12()
 
def choice14():
   choice14=input("\nDo you want to head northeast or south? ").lower()
   if choice14=="northeast":
      print(pages.page20)
   elif choice14=="south":
      print(pages.page16)
   else:
      print("Invalid input")
      choice14()

def choice19():
   choice19=input("\nDo you want to take a chance? ").lower()
   if choice19=="yes":
      print(pages.page31)
   elif choice19=="no":
      print(pages.page24)
   else:
      print("Invalid input")
      choice19()
 
def choice20():
   choice20=input("\nDo you want to go right or straight? ").lower()
   if choice20=="right":
      print(pages.page9)
   elif choice20=="straight":
      print(pages.page26)
   else:
      print("Invalid input")
      choice20()
 
def choice25():
   choice25=input("\nDo you want to go southeast or south? ").lower()
   if choice25=="southeast":
      print(pages.page44)
   elif choice25=="south":
      print(pages.page86)
   else:
      print("Invalid input")
      choice25()

def choice26():
   choice26=input("\nDo you want to go to Agron? ").lower()
   if choice26=="no":
      print(pages.page37)
   elif choice26=="yes":
      print(pages.page33)
   else:
      print("Invalid input")
      choice26()

def choice27():
   choice27=input("\nDo you want to go northeast, or southeast? ").lower()
   if choice27=="northeast":
      print(pages.page68)
   elif choice27=="southeast":
      print(pages.page38)
   else:
      print("Invalid input")
      choice27()

def choice28():
   choice28=input("\nDo you want to go northeast or southeast? ").lower()
   if choice28=="northeast":
      print(pages.page92)
   elif choice28=="southeast":
      print(pages.page50)
   else:
      print("Invalid input")
      choice28()

def choice31():
   choice31=input("\nDo you want to go north, or south? ").lower()
   if choice31=="north":
      print(pages.page9)
   elif choice31=="south":
      print(pages.page44)
   else:
      print("Invalid input")
      choice31()

def choice34():
   choice34=input("\nDo you want to go west, south, or north? ").lower()
   if choice34=="west":
      print(pages.page92)
   elif choice34=="south":
      print(pages.page52)
   elif choice34=="north":
      print(pages.page82)
   else:
      print("Invalid input")
      choice34()

def choice37():
   choice37=input("\nDo you want to go to Agron? ").lower()
   if choice37=="yes":
      print(pages.page33)
   if choice37=="no":
      print(pages.page68)
   else:
      print("Invalid input")
      choice37()

def choice38():
   choice38=input("\nDo you to take the northern route, the southern route, or go back to Agron? ").lower()
   if choice38=="northern route":
      print(pages.page49)
   elif choice38=="southern route":
      print(pages.page28)
   elif choice38=="Agron":
      print(pages.page77)
   else:
      print("Invalid input")
      choice38()

def choice43():
   choice43=input("\nDo you want to go to Okur or Mount Karra? ").lower()
   if choice43=="okur":
      print(pages.page57)
   elif choice43=="mount karra":
      print(pages.page55)
   else:
      print("Invalid input")
      choice43()

def choice44():
   choice44=input("\nDo you want to swim across the Rapoor River or go to Kacita? ").lower()
   if choice44=="rapoor river":
      print(pages.page60)
   elif choice44=="kacita":
      print(pages.page24)
   else:
      print("Invalid input")
      choice44()

def choice45():
   choice45=input("\nDo you want to take the northeastern trail or the southeastern trail? ").lower()
   if choice45=="northeastern trail":
      print(pages.page49)
   elif choice45=="southeastern trail":
      print(pages.page28)
   else:
      print("Invalid input")

def choice46():
   choice46=input("\nDo you want to jump down or climb back down? ").lower()
   if choice46=="jump":
      print(pages.page111)
   elif choice=="climb":
      print(pages.page7)
   else:
      print("Invalid input")
      choice46()

def choice49():
   choice49=input("\nDo you want to go north or south? ").lower()
   if choice49=="north":
      print(pages.page82)
   elif choice49=="south":
      print(pages.page92)
   else:
      print("Invalid input")
      choice49()

def choice50():
   choice50=input("\nDo you want to go north or northeast? ").lower()
   if choice50=="north":
      print(pages.page92)
   elif choice50=="northeast":
      print(pages.page61)
   else:
      print("Invalid input")
      choice50()

def choice52():
   choice52=input("\nDo you want to go north or southwest? ").lower()
   if choice52=="north":
      print(pages.page75)
   elif choice52=="southwest":
      print(pages.page65)
   else:
      print("Invalid input")
      choice52()

def choice55():
   choice55=input("\nDo you want to follow the first, second, or third sign? ").lower()
   if choice55=="first":
      print(pages.page88)
   elif choice55=="second":
      print(pages.page62)
   elif choice55=="third":
      print(pages.page85)
   else:
      print("Invalid input")
      choice55()

def choice57():
   choice57=input("\nDo you want to go right at every corner or alternate your direction? ").lower()
   if choice57=="right":
      print(pages.page71)
   elif choice57=="alternate":
      print(pages.page83)
   else:
      print("Invalid input")
      choice57()

def choice62():
   choice62=input("\nDo you want to go north, east, or accepte a ride across the lake? ").lower()
   if choice62=="north":
      print(pages.page81)
   elif choice62=="east":
      print(pages.page84)
   elif choice62=="ride":
      print(pages.page88)
   else:
      print("Invalid input")
      choice62()

def choice65():
   choice65=input("\nDo you want to go left, right, or toward the lake? ").lower()
   if choice65=="left":
      print(pages.page52)
   elif choice65=="right":
      print(pages.page57)
   elif choice65=="lake":
      print(pages.page55)
   else:
      print("Invalid input")
      choice65()

def choice67():
   choice67=input("\nDo you want to ask the crogocides for help or try to cut throught the forest to avoid the spiders? ").lower()
   if choice67=="ask for help":
      print(pages.page7)
   elif choice67=="cut through forest":
      print(pages.page102)
   else:
      print("Invalid input")
      choice67()

def choice69():
   choice69=input("\nDo you want to board the boat, go toward the orange sun, or go away from the orange sun? ").lower()
   if choice69=="boat":
      print(pages.page86)
   elif choice69=="toward":
      print(pages.page33)
   elif choice69=="away":
      print(pages.page82)
   else:
      print("Invalid input")
      choice69()

def choice71():
   choice71=input("\nDo you want to head upstream or downstream? ").lower()
   if choice71=="upstream":
      print(pages.page58)
   elif choice71=="downstream":
      print(pages.page67)
   else:
      print("Invalid input")
      choice71()

def choice74():
   choice74=input("\nDo you want to head toward the sun or away? ").lower()
   if choice74=="toward":
      print(pages.page124)
   elif choice74=="away":
      print(pages.page86)
   else:
      print("Invalid input")
      choice74()

def choice75():
   choice75=input("\nDo you want to give up your computer or refuse? ").lower()
   if choice75=="give up":
      print(pages.page70)
   elif choice75=="refuse":
      print(pages.page116)
   else:
      print("Invalid input")
      choice75()

def choice77():
   choice77=input("\nDo you want to go northeast or southeast? ").lower()
   if choice77=="northeast":
      print(pages.page68)
   elif choice77=="southeast":
      print(pages.page38)
   else:
      print("Invalid input")
      choice77()

def choice78():
   choice78=input("\nDo you want to go northwest, east, or south? ").lower()
   if choice78=="northeast":
      print(pages.page120)
   elif choice78=="east":
      print(pages.page75)
   elif choice78=="south":
      print(pages.page105)
   else:
      print("Invalid input")
      choice78()

def choice82():
   choice82=input("\nDo you want to swim or hide in the bushes? ").lower()
   if choice82=="swim":
      print(pages.page76)
   elif choice82=="hide":
      print(pages.page75)
   else:
      print("Invalid input")
      choice82()

def choice84():
   choice84=input("\nDo you want to go north or south? ").lower()
   if choice84=="north":
      print(pages.page95)
   elif choice84=="south":
      print(pages.page91)
   else:
      print("Invalid input")
      choice84()

def choice86():
   choice86=input("\nDo you want to go northeast, southeast, or northwest? ").lower()
   if choice86=="northeast":
      print(pages.page44)
   elif choice86=="southeast":
      print(pages.page74)
   elif choice86=="northwest":
      print(pages.page24)
   else:
      print("Invalid input")
      choice86()

def choice89():
   choice89=input("\nDo you want to take the sailboat, go south, or go west? ").lower()
   if choice89=="sailboat":
      print(pages.page108)
   elif choice89=="south":
      print(pages.page94)
   elif choice89=="west":
      print(pages.page55)
   else:
      print("Invalid input")
      choice89()

def choice90():
   choice90=input("\nDo you want to go to Kacita, Pira, or Land of the Nekka? ").lower()
   if choice90=="kacita":
      print(pages.page24)
   elif choice90=="pira":
      print(pages.page74)
   elif choice90=="land of the nekka":
      print(pages.page44)
   else:
      print("Invalid input")
      choice90()

def choice91():
   choice91=input("\nDo you want to head east or go to Medea? ").lower()
   if choice91=="east":
      print(pages.page114)
   elif choice91=="medea":
      print(pages.page88)
   else:
      print("Invalid input")
      choice91()

def choice93():
   choice93=iput("\nDo you want to go to the krelium mine or the crystal mine? ").lower()
   if choice93=="krelium":
      print(pages.page7)
   elif choice93=="crystal":
      print(pages.page75)
   else:
      print("Invalid input")
      choice93()

def choice94():
   choice94=input("\nDo you want to go east, south, or north? ").lower()
   if choice94=="east":
      print(pages.page97)
   elif choice94=="south":
      print(pages.page102)
   elif choice94=="north":
      print(pages.page88)
   else:
      print("Invalid input")
      choice94()

def choice95():
   choice95=input("\nDo you want to go left or right? ").lower()
   if choice95=="left":
      print(pages.page99)
   elif choice95=="right":
      print(pages.page120)
   else:
      print("Invalid input")
      choice95()

def choice96():
   choice96=input("\nDo you want to take the trail marked by the rock pillars, solitary pine, or logs? ").lower()
   if choice96=="rock pillars":
      print(pages.page101)
   elif choice96=="solitary pine":
      print(pages.page120)
   elif choice96=="logs":
      print(pages.page78)
   else:
      print("Invalid input")
      choice96()

def choice97():
   choice97=input("\nDo you want to go north or south? ").lower()
   if choice97=="north":
      print(pages.page91)
   elif choice97=="south":
      print(pages.page102)
   else:
      print("Invalid input")
      choice97()

def choice101():
   choice101=input("\nDo you want to go west, east, or to Chawakelamptha? ").lower()
   if choice101=="west":
      print(pages.page82)
   elif choice101=="east":
      print(pages.page120)
   elif choice101=="chawakelamptha":
      print(pages.page99)
   else:
      print("Invalid input")
      choice101()

def choice102():
   choice102=input("\nDo you want to show yourself or retreat? ").lower()
   if choice102=="show yourself":
      print(pages.page36)
   elif choice102=="retreat":
      print(pages.page94)
   else:
      print("Invalid input")
      choice102()

def choice106():
   choice106=input("\nDo you want to east, west, or south?").lower()
   if choice106=="east":
      print(pages.page46)
   elif choice106=="west":
      print(pages.page118)
   elif choice106=="south":
      print(pages.page114)
   else:
      print("Invalid input")
      choice106()

def choice109():
   choice109=input("\nDo you want to go to Mount Calm, Verde, Porros, Chawakelamptha, or Dazzling Mountains? ").lower()
   if choice109=="mount calm":
      print(pages.page52)
   elif choice109=="verde":
      print(pages.page101)
   elif choice109=="porros":
      print(pages.page120)
   elif choice109=="chawakelamptha":
      print(pages.page99)
   elif choice109=="dazzling mountains":
      print(pages.page81)
   else:
      print("Invalid input")
      choice109()

def choice114():
   choice114=input("\nDo you want to go east or west? ").lower()
   if choice114=="east":
      print(pages.page46)
   elif choice114=="west":
      print(pages.page91)
   else:
      print("Invalid input")
      choice114()

def choice117():
   choice117=input("\nDo you want to go east, west, or south? ").lower()
   if choice117=="east":
      print(pages.page46)
   elif choice117=="west":
      print(pages.page118)
   elif choice=="south":
      print(pages.page114)
   else:
      print("Invalid input")
      choice117

def choice122():
   choice122=input("\nDo you want to go Okur or Mount Karra? ").lower()
   if choice122=="okur":
      print(pages.page57)
   elif choice122=="mount karra":
      print(pages.page55)
   else:
      print("Invalid input")
      choice122()

def choice125():
   choice125=input("\nDo you want to go to Medea, Issus, rain forest, or harbor? ").lower()
   if choice125=="medea":
      print(pages.page88)
   elif choice125=="issus":
      print(pages.page55)
   elif choice125=="rain forest":
      print(pages.page97)
   elif choice125=="harbor":
      print(pages.page102)
   else:
      print("Invalid input")
      choice125()

def choice128():
   choice128=input("\nDo you want to go to Riva, Land of Volcas, coast, or climb over the wall? ").lower()
   if choice128=="riva":
      print(pages.page75)
   elif choice128=="land of volcas":
      print(pages.page114)
   elif choice128=="coast":
      print(pages.page102)
   elif choice128=="climb":
      print(pages.page111)
   else:
      print("Invalid input")
      choice128()

def choice132():
   choice132=input("\nDo you want to take a boat or hike around the lake? ").lower()
   if choice132=="boat":
      print(pages.page88)
   elif choice132=="hike":
      print(pages.page62)
   else:
      print("Invalid input")
      choice132()

def choice133():
   choice133=input("\nDo you want to go left or straight? ").lower()
   if choice133=="left":
      print(pages.page85)
   elif choice133=="right":
      print(pages.page55)
   else:
      print("Invalid input")
      choice133()
