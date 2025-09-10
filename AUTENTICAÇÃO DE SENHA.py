def autenticar():
    senha_correta = "1234"  
    hash_correto = hashlib.sha256(senha_correta.encode()).hexdigest()
    
    senha_digitada = input("Digite sua senha: ")
    hash_digitada = hashlib.sha256(senha_digitada.encode()).hexdigest()
    
    if hash_digitada == hash_correto:
        print("✅ Acesso permitido.")
    else:
        print("❌ Senha incorreta.")