import language_tool_python

def ajustar_gramatica(texto):
    """
    Ajusta a gramática de um texto em português.

    Args:
        texto (str): O texto a ser corrigido.

    Returns:
        str: O texto corrigido.
    """
    # Inicializa a ferramenta para a língua portuguesa
    ferramenta = language_tool_python.LanguageTool('pt-BR')
    
    # Identifica os erros no texto
    erros = ferramenta.check(texto)
    
    # Aplica as correções no texto
    texto_corrigido = language_tool_python.utils.correct(texto, erros)
    
    return texto_corrigido

# Exemplo de uso
texto_original = "eu estou programando um codigo e ele esta sendo bem visto porem algumas pessoas nao gostaram "
texto_corrigido = ajustar_gramatica(texto_original)

print("Texto Original:")
print(texto_original)
print("\nTexto Corrigido:")
print(texto_corrigido)

