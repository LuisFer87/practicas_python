monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
print(monto_interes)
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
print(importe_bonificacion)
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
print(monto_neto)
