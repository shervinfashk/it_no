import csv

with open("en_variant.csv","w", newline='') as fil_skriver:
    fieldnames = ["Handle","Title","Variant Inventory Qty","Variant Price","Image Src", "Width", "Length"]
    writer = csv.DictWriter(fil_skriver, fieldnames=fieldnames)
    writer.writeheader()
    with open('fil_for_prosjekt.csv', 'r') as lese_i_fra:
        r = csv.reader(lese_i_fra)
        headers = lese_i_fra.readline()

        for row in r:
            if len(row[1]) > 0:
                
                ord_i__tittel = row[1].split(" ")
                størrelse = ord_i__tittel[-1]
                
                if ( "solgt" in størrelse.lower()):
                    størrelse = ord_i__tittel[-2]
                
                # på dette punktet bør det være typ 321x193
                
                lengde_bredde = størrelse.lower().replace(" ", "").split("x")
                try:
                    lengde = lengde_bredde[0]
                    bredde = lengde_bredde[1]
                except IndexError:
                    continue
                
                
                writer.writerow({'Handle': row[0], 'Title': row[1], 'Variant Inventory Qty' : row[2], "Variant Price": row[3], "Image Src" : row[5], "Width" : bredde, "Length" : lengde,})
    
    

           


    
