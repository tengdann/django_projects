import csv
from unesco.models import site, category, states, region, iso
fhand = open('unesco2/whc-sites-2018-small.csv')
reader = csv.reader(fhand)

site.objects.all().delete()
category.objects.all().delete()
states.objects.all().delete()
region.objects.all().delete()
iso.objects.all().delete()

i = 1

for row in reader:
    cat = category.objects.get_or_create(name = row[7])[0]
    sta = states.objects.get_or_create(name = row[8])[0]
    reg = region.objects.get_or_create(name = row[9])[0]
    iso = iso.objects.get_or_create(name = row[10])[0]
    
    try:
        yr = int(row[3])
    except:
        yr = None
    
    try:
        long = float(row[4])
    except:
        long = None
    
    try:
        lat = float(row[5])
    except:
        lat = None
    
    try:
        area = float(row[6])
    except:
        area = None
    
    m = site(name = row[0], description = row[1], justification = row[2],
            year = yr, longitude = long, latitude = lat, area_hectares = area,
            category = cat, states = sta, region = reg, iso = iso)
    m.save()
    print (f'Row {i} done')
    i += 1