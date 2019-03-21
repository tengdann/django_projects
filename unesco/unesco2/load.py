import csv

from unesco2.models import Category, State, Region, Iso, Site

fhand = open(r'unesco2/whc-sites-2018-small.csv')
reader = csv.reader(fhand)

Category.objects.all().delete()
State.objects.all().delete()
Region.objects.all().delete()
Iso.objects.all().delete()
Site.objects.all().delete()

# Format
# name, description, justification, year, longitude, latitude, area_hectares, category, states, region, iso

next(reader)

for row in reader:
    c = Category.objects.get_or_create(name = row[7])[0]
    s = State.objects.get_or_create(name = row[8])[0]
    r = Region.objects.get_or_create(name = row[9])[0]
    i = Iso.objects.get_or_create(name = row[10])[0]

    try:
        y = int(row[3])
    except:
        y = None

    try:
        lo = float(row[4])
    except:
        lo = None

    try:
        la = float(row[5])
    except:
        la = None

    try:
        ar = float(row[6])
    except:
        ar = None

    m = Site(name = row[0], description = row[1], justification = row[2],
             year = y, longitude = lo, latitude = la, area_hectares = ar,
             category = c, states = s, region = r, iso = i)
    m.save()