from cryptography.fernet import Fernet

key = 'qNeAdq53wi9_eaVhUyHIQxtoAwfsz66I-M48ro-Ld9g='
f = Fernet(key)
texto = 'abc123'


print(f.encrypt(texto.encode('utf-8')))