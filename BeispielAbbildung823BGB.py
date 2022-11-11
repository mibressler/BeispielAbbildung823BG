# Vorsatz oder Fahrlaessigkeit
a = False
b = True

# Rechtsgueter
c = False
d = True
e = False
f = False
g = False
h = False

# weitere Vorraussetzungen
i = True
j = True
k = True

# Schadensersatzpflicht
l = None

if (a or b) and (c or d or e or f or g or h) and i and j and k:
  l = True
else:
  l = False
  
  
if l == True:
  print("es gibt eine Verpflichtung zum Ersatz des daraus entstandenen Schadens!")
if l == False:
  print("es gibt keine Verpflichtung zum Ersatz des daraus entstandenen Schadens!")