import time

t = input("Digite o tempo (em segundos): ")
if t.isdigit():
    t = int(t)
else:
    print("Dígito inválido!")
    quit()

while t:
    minutes, seconds = divmod(t, 60)
    timer = f"{minutes:02d}:{seconds:02d}"
    print(f"\r{timer}", end="", flush=True)
    time.sleep(1)
    t -= 1

print("\nTEMPO ESGOTADO")