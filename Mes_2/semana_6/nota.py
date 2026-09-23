from urllib.parse import urlparse, parse_qs

ruta  = urlparse("https://mail.google.com/mail/u/0/#inbox/FMfcgzQhWLNsVPRtcFwkDMwdtPKzgsWL")

print(f"Protocolo: {ruta.scheme}")   
print(f"Ubicación de red o dominio: {ruta.netloc}")   
print(f"Ruta: {ruta.path}")     
print(f"Consulta: {ruta.query}")    
print(f"Fragmento / Ancla: {ruta.fragment}")

my_query = parse_qs(ruta.query)

for i in my_query:
    print()