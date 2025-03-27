
# 1.Rabattberechnung für einen einzelnen Preis

price = float(input("Gib den Preis ein: "))

if price <= 20:
    rabatt = 0.20 # 20% rabatt 
elif 20 < price <=50:
    rabatt = 0.40 # 40% rabatt 
else:       
    rabatt = 0.60 # 60% rabatt  
    
new_price = price * (1 - rabatt) 
    
print(f"Der Rreis mit Rabatt beträgt: {new_price} €") 


##############################################################################
# 2. Berechnung rabattierter Preise für eine Liste von Preisen
prices = [40, 21, 29, 50, 101]
new_prices = []

# Rabattberechnung für jede Preis in der Liste
for price in prices:
    if price <= 20:
        rabatt = 0.20  
    elif 20 < price <= 50:
        rabatt = 0.40  
    else:
        rabatt = 0.60  
    
    new_price = price * (1 - rabatt)
    new_prices.append(new_price) # fügt den berechneten neuen Preis hinzu

print("Rabattierte Preise aus der Liste:", new_prices)

#################################################################
# 3. Bereinigung der chaos-Liste und Rabattberechnung der alten Preise

chaos = ["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

# Verarbeitung der chaos-Liste
for item in chaos:
    if "old price" in item:  # Nur die alten Preise auswählen
        old_price = float(item.split(":")[1].strip())  # Preis extrahieren und als float konvertieren
        if old_price <= 20:
            rabatt = 0.20
        elif 20 < old_price <= 50:
            rabatt = 0.40
        else:
            rabatt = 0.60
        
        new_price = old_price * (1 - rabatt)
        order.append(new_price)

# Ausgabe der bereinigten Liste mit neuen Preisen
print("Bereinigte Liste mit neuen Preisen:", order)  