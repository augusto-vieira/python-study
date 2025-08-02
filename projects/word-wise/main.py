import tkinter as tk
import re
from collections import Counter

class WordWise:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Wise")
        self.root.geometry("800x600")

        # Configura as colunas para expandirem igualmente
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Frame para entrada de texto
        self.text_frame = tk.Frame(root)
        self.text_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Frame para visualização e seleção de palavras
        self.selection_frame = tk.Frame(root)
        self.selection_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Label de instruções para a entrada de texto
        self.text_label = tk.Label(self.text_frame, text="Digite ou cole seu texto abaixo:")
        self.text_label.pack()
        # Pula um espaço
        self.text_label = tk.Label(self.text_frame, text="") 
        self.text_label.pack()

        # Caixa de entrada de texto (editável)
        self.text_entry = tk.Text(self.text_frame, wrap='word')
        self.text_entry.pack(fill=tk.BOTH, expand=True)

        # Botão para processar texto
        self.process_button = tk.Button(self.text_frame, text="Processar Texto", command=self.processar_texto)
        self.process_button.pack()

        # Label para mostrar a contagem de palavras
        self.contagem_label = tk.Label(self.text_frame, text="Total de palavras: 0")
        self.contagem_label.pack()

        # Frame para as opções de cor
        self.color_frame = tk.Frame(self.selection_frame)
        self.color_frame.pack(side=tk.TOP)

        # Label para seleção de palavras na segunda janela
        self.selection_label = tk.Label(self.selection_frame, text="Selecione as palavras conhecidas:")
        self.selection_label.pack()

        # Radiobuttons para as cores (na horizontal)
        self.color_var = tk.StringVar(value="yellow")  # Valor inicial padrão
        self.create_color_buttons()

        # Caixa de texto para seleção de palavras (não editável)
        self.selection_text = tk.Text(self.selection_frame, wrap='word', state=tk.DISABLED)
        self.selection_text.pack(fill=tk.BOTH, expand=True)

        # Caixa de seleção para "Palavras Repetidas"
        self.repetidas_var = tk.BooleanVar(value=True)  # Padrão marcado
        self.repetidas_checkbox = tk.Checkbutton(self.selection_frame, text="Marcar palavras repetidas", variable=self.repetidas_var)
        self.repetidas_checkbox.pack()

        # Botão para desmarcar todas as seleções
        self.clear_button = tk.Button(self.selection_frame, text="Desmarcar Seleções", command=self.desmarcar_selecoes)
        self.clear_button.pack(side=tk.RIGHT)

        # Label para mostrar a porcentagem de palavras conhecidas
        self.porcentagem_label = tk.Label(self.selection_frame, text="Porcentagem de palavras conhecidas: 0%")
        self.porcentagem_label.pack()

        # Variáveis para controle
        self.palavras = []
        self.palavras_conhecidas = set()  # Usando um conjunto para palavras conhecidas

        # Bind para selecionar palavras ao clicar
        self.selection_text.bind("<Button-1>", self.selecionar_palavra)

    def create_color_buttons(self):
        # Radiobuttons para as cores (dispostos horizontalmente)
        cores = [("Amarelo", "yellow"), ("Verde", "green"), ("Azul", "blue"), ("Vermelho", "red"), ("Roxo", "purple")]
        for texto, valor in cores:
            tk.Radiobutton(self.color_frame, text=texto, variable=self.color_var, value=valor).pack(side=tk.LEFT)

    def _extrair_palavras(self, texto):
        # Exclui caracteres especiais da contagem de palavras
        return re.findall(r'\b[a-zA-Z]+\b', texto.lower())

    def processar_texto(self):
        texto = self.text_entry.get("1.0", tk.END).strip()
        if not texto:
            return

        self.palavras = self._extrair_palavras(texto)
        self.palavras_unicas = set(self.palavras)

        # Limpa a área de seleção e popula com as palavras
        self.selection_text.config(state=tk.NORMAL)
        self.selection_text.delete("1.0", tk.END)  # Limpa o texto anterior
        self.selection_text.insert(tk.END, texto)  # Insere o texto na área de seleção
        self.selection_text.config(state=tk.DISABLED)  # Desabilita edição

        # Contagem de palavras
        self.contagem_palavras()
        self.atualizar_porcentagem()  # Atualiza a porcentagem após processar

    def contagem_palavras(self):
        total_palavras = len(self.palavras)
        total_unicas = len(self.palavras_unicas)
        contagem_repetidas = Counter(self.palavras)
        # Contabiliza o número total de repetições (não apenas as que aparecem mais de uma vez)
        repetidas = sum(count - 1 for count in contagem_repetidas.values() if count > 1)

        # Atualiza a label com contagem
        self.contagem_label.config(text=f"Total de palavras: {total_palavras}\nTotal de palavras únicas: {total_unicas}\nTotal de palavras repetidas: {repetidas}")

    def selecionar_palavra(self, event):
        # Pega a posição do clique
        index = self.selection_text.index("@%s,%s" % (event.x, event.y))
        palavra = self.selection_text.get(index + " wordstart", index + " wordend").strip()

        # Ignora se a palavra for um espaço em branco ou caracteres especiais
        if palavra == "" or not palavra.isalpha():
            return

        # Atualiza a cor da palavra conhecida com base na cor selecionada no Radiobutton
        cor_selecionada = self.color_var.get()

        # Aplica a cor à palavra
        self.marcar_palavra_unica(index, cor_selecionada)

        self.atualizar_porcentagem()  # Atualiza a porcentagem após marcar ou desmarcar

    def marcar_palavra_unica(self, index, cor):
        # Marca apenas a palavra na posição especificada
        self.selection_text.config(state=tk.NORMAL)  # Habilita a edição para aplicar cor

        # Calcula os limites da palavra
        start_index = self.selection_text.index(index + " wordstart")
        end_index = self.selection_text.index(index + " wordend")

        palavra = self.selection_text.get(start_index, end_index).strip()

        # Cria uma tag única para a cor (não usa a palavra)
        tag_name = f"colored_{start_index}"

        # Verifica se a palavra já tem a tag
        if self.selection_text.tag_ranges(tag_name):
            # Remove a tag se a palavra já estiver marcada
            self.selection_text.tag_remove(tag_name, start_index, end_index)
            self.palavras_conhecidas.discard(palavra.lower())  # Remove a palavra do conjunto

            # Se a caixa de "palavras repetidas" estiver marcada, desmarca todas as instâncias
            if self.repetidas_var.get():
                self.desmarcar_palavra_repetida(palavra)

        else:
            # Adiciona a tag se a palavra não estiver marcada
            self.selection_text.tag_add(tag_name, start_index, end_index)
            self.selection_text.tag_config(tag_name, background=cor)
            self.palavras_conhecidas.add(palavra.lower())  # Armazena a palavra em minúsculas

            # Marca palavras repetidas se a caixa estiver marcada
            if self.repetidas_var.get():
                self.marcar_palavra_repetida(palavra, cor)  # Passar a palavra e a cor

        self.selection_text.config(state=tk.DISABLED)  # Desabilita edição novamente

    def marcar_palavra_repetida(self, palavra, cor):
        # Marca todas as instâncias da palavra na área de seleção
        start = self.selection_text.search(palavra, "1.0", tk.END)
        while start:
            end = f"{start}+{len(palavra)}c"
            tag_name = f"colored_{start}"
            self.selection_text.tag_add(tag_name, start, end)
            self.selection_text.tag_config(tag_name, background=cor)
            self.palavras_conhecidas.add(palavra.lower())  # Armazena a palavra em minúsculas
            start = self.selection_text.search(palavra, start + "+1c", tk.END)  # Ajuste para o próximo índice

    def desmarcar_palavra_repetida(self, palavra):
        # Remove todas as instâncias da palavra na área de seleção
        start = self.selection_text.search(palavra, "1.0", tk.END)
        while start:
            end = f"{start}+{len(palavra)}c"
            tag_name = f"colored_{start}"
            self.selection_text.tag_remove(tag_name, start, end)
            start = self.selection_text.search(palavra, start + "+1c", tk.END)  # Ajuste para o próximo índice

    def desmarcar_selecoes(self):
        # Remove todas as tags de cor da área de seleção
        for tag in self.selection_text.tag_names():
            if tag.startswith("colored_"):
                self.selection_text.tag_remove(tag, "1.0", tk.END)

        # Limpa o conjunto de palavras conhecidas
        self.palavras_conhecidas.clear()

        # Atualiza a contagem e porcentagem após desmarcar
        self.contagem_palavras()
        self.atualizar_porcentagem()

    def atualizar_porcentagem(self):
        # Calcula a porcentagem de palavras conhecidas
        total_palavras = len(self.palavras)
        
        # Converte palavras conhecidas para minúsculas para comparação
        palavras_conhecidas_lower = {palavra.lower() for palavra in self.palavras_conhecidas}
        
        # Contabiliza palavras selecionadas em minúsculas
        total_selecionadas = sum(1 for palavra in self.palavras if palavra.lower() in palavras_conhecidas_lower)

        if total_palavras > 0:
            porcentagem = round((total_selecionadas / total_palavras) * 100, 2)
        else:
            porcentagem = 0

        # Atualiza o rótulo com a porcentagem
        self.porcentagem_label.config(text=f"Porcentagem de palavras conhecidas: {porcentagem}% ({len(self.palavras_conhecidas)}/{total_palavras})")

# Inicializa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = WordWise(root)
    root.mainloop()
