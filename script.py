from _conn import banco_default

for i in range(100):
    nome = input(f"Digite o nome do participante {i+1}: ")
    banco_default(f"UPDATE `participante` SET `nome`='{nome}' WHERE numero={i+1}")
