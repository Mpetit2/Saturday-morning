vlan_rango_normal=range(1,1005)
vlan_rango_extendida=range(1006,4094)
numero_vlan=int(input("ingrese el numero de vlan: "))
if numero_vlan in vlan_rango_normal:
    print("numero de vlan",numero_vlan,"es de rango normal")
elif numero_vlan in vlan_rango_extendida:
    print("numero de vlan",numero_vlan,"es de rango extendida")
else:
    print("el numero",numero_vlan,"no corresponde a una vlan")