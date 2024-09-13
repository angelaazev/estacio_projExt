import tkinter as tk
from tkinter import messagebox

class GymTrainingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Treinos")
        self.trainings = {}

        # Seleção de dias
        self.day_label = tk.Label(root, text="Selecione o dia da semana:")
        self.day_label.grid(row=0, column=0)
        self.day_var = tk.StringVar(value="Segunda")
        self.day_menu = tk.OptionMenu(root, self.day_var, "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
        self.day_menu.grid(row=0, column=1)

        # Input dos exercícios
        self.exercise_label = tk.Label(root, text="Nome do Exercício:")
        self.exercise_label.grid(row=1, column=0)
        self.exercise_entry = tk.Entry(root)
        self.exercise_entry.grid(row=1, column=1)

        # Input das repetições
        self.reps_label = tk.Label(root, text="Repetições:")
        self.reps_label.grid(row=2, column=0)
        self.reps_entry = tk.Entry(root)
        self.reps_entry.grid(row=2, column=1)

        # Input das séries
        self.series_label = tk.Label(root, text="Séries:")
        self.series_label.grid(row=3, column=0)
        self.series_entry = tk.Entry(root)
        self.series_entry.grid(row=3, column=1)

        # Configuração dos botões
        self.add_button = tk.Button(root, text="Adicionar exercício", command=self.add_exercise)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="Visualizar treino do dia", command=self.view_training)
        self.view_button.grid(row=5, column=0, columnspan=2)
        
        self.view_all_button = tk.Button(root, text="Visualizar todos os treinos", command=self.view_all_trainings)
        self.view_all_button.grid(row=6, column=0, columnspan=2)


        self.display_box = tk.Text(root, height=10, width=40)
        self.display_box.grid(row=7, column=0, columnspan=2)

    def add_exercise(self):
        day = self.day_var.get()
        exercise = self.exercise_entry.get()
        reps = self.reps_entry.get()
        series = self.series_entry.get()

        if not exercise or not reps or not series:
            messagebox.showwarning("Erro de input", "Por favor, preencha todos os campos")
            return

        if day not in self.trainings:
            self.trainings[day] = []

        self.trainings[day].append(f"{exercise} - {reps} repetições x {series} séries")

        self.exercise_entry.delete(0, tk.END)
        self.reps_entry.delete(0, tk.END)
        self.series_entry.delete(0, tk.END)

        messagebox.showinfo("Sucesso", f"Exercício adicionado ao treino de {day}")

    def view_training(self):
        day = self.day_var.get()
        self.display_box.delete(1.0, tk.END)

        if day in self.trainings:
            self.display_box.insert(tk.END, f"Treino de {day}:\n")
            for exercise in self.trainings[day]:
                self.display_box.insert(tk.END, f"- {exercise}\n")
        else:
            self.display_box.insert(tk.END, f"Nenhum treino criado para {day}.")

    def view_all_trainings(self):
        self.display_box.delete(1.0, tk.END)

        if not self.trainings:
            self.display_box.insert(tk.END, "Nenhum treino agendado.")
            return

        for day, exercises in self.trainings.items():
            self.display_box.insert(tk.END, f"=Treino de {day}:\n")
            for exercise in exercises:
                self.display_box.insert(tk.END, f"- {exercise}\n")
            self.display_box.insert(tk.END, "\n") #quebra de linha após cada dia da semana

def main():
    root = tk.Tk()
    app = GymTrainingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
