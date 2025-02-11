import speech_recognition as sr
import pyttsx3

# Inicializar o reconhecedor de fala e o engine de conversão de texto para fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Método para converter texto em fala
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Função para capturar e transcrever a fala
def audicao():
    with sr.Microphone() as microfone:
        print("Fale algo...")
        try:
            # Capta a fala
            fala = recognizer.listen(microfone)
            # Transcreve a fala para texto
            texto = recognizer.recognize_google(fala, language="pt-BR") #A biblioteca usa uma API do Google
            #print(f"Você disse: {texto}")
            print(f"Você: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return None
        except sr.RequestError as e:
            print(f"Erro no serviço de reconhecimento de fala: {e}")
            return None

# Main
def main():
    while True:
        print("\nO que você quer que eu faça? Estou aqui pra servir :)\n")
        print("1: Falar algo para eu transcrever\n")
        print("2: Digitar algo para eu falar\n")
        print("3: Sair do programa :(\n")
        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == "1":
            audio = audicao()

        elif opcao == "2":
            texto_digitado = input("Digite algo para eu falar: ")
            falar(texto_digitado)

        elif opcao == "3":
            print("Encerrando o programa. Tchau ;)")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
