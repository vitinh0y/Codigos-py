from PIL import Image
import os

def converter_imagem(caminho_entrada, formato_saida, caminho_saida=None):
    """
    Converte uma imagem para um formato especificado.

    Args:
        caminho_entrada (str): Caminho do arquivo de imagem original.
        formato_saida (str): Formato de saída (e.g., 'JPEG', 'PNG', 'BMP').
        caminho_saida (str, opcional): Caminho para salvar a imagem convertida. 
                                       Se None, salva no mesmo diretório com o formato alterado.
    """
    try:
        # Abre a imagem original
        imagem = Image.open(caminho_entrada)
        
        # Define o nome do arquivo de saída
        if caminho_saida is None:
            base, _ = os.path.splitext(caminho_entrada)
            caminho_saida = f"{base}.{formato_saida.lower()}"
        
        # Converte e salva a imagem no formato desejado
        imagem.save(caminho_saida, formato_saida.upper())
        print(f"Imagem convertida com sucesso: {caminho_saida}")
    
    except Exception as e:
        print(f"Erro ao converter a imagem: {e}")

# Exemplo de uso
caminho_entrada = "exemplo.png"  # Caminho da imagem original
formato_saida = "JPEG"          # Formato de saída desejado
caminho_saida = "convertida.jpeg"  # Caminho de saída (opcional)

converter_imagem(caminho_entrada, formato_saida, caminho_saida)
