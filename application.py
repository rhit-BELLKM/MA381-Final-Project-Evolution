import tkinter as tk
from organism import Organism

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.organism = Organism()
        
        self.title_label = tk.Label(self, text="Organism Simulator", font=("TkDefaultFont", 16))
        self.master.geometry("600x600")
        self.title_label.pack(pady=20)

        self.reproduce_button = tk.Button(self, text="Reproduce", command=lambda: self.reproduce(1))
        self.reproduce_button.pack(pady=10)
        
        self.reproduce_10_button = tk.Button(self, text="Reproduce 10", command=lambda: self.reproduce(10))
        self.reproduce_10_button.pack(pady=10)

        self.reproduce_100_button = tk.Button(self, text="Reproduce 100", command=lambda: self.reproduce(100))
        self.reproduce_100_button.pack(pady=10)

        self.reproduce_1000_button = tk.Button(self, text="Reproduce 1000", command=lambda: self.reproduce(1000))
        self.reproduce_1000_button.pack(pady=10)

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(pady=10)

        self.fitness_label = tk.Label(self, text="Fitness: 0.0", font=("TkDefaultFont", 14))
        self.fitness_label.pack(pady=10)

        self.mutations_label = tk.Label(self, text="Mutations: 0.0", font=("TkDefaultFont", 14))
        self.mutations_label.pack(pady=10)
        
        self.mutation_rate_label = tk.Label(self, text="Mutation Rate: 0.0", font=("TkDefaultFont", 14))
        self.mutation_rate_label.pack(pady=10)

        self.mutation_rate_entry = tk.Entry(self)
        self.mutation_rate_entry.insert(0, "0.01")
        self.mutation_rate_entry.pack(pady=10)

        self.update_mutation_rate_button = tk.Button(self, text="Update Mutation Rate", command=self.update_mutation_rate)
        self.update_mutation_rate_button.pack(pady=10)

    def reproduce(self, times=1):
        self.organism = self.organism.reproduce(times=times)
        self.fitness_label["text"] = f"Fitness: {self.organism.fitness:.2f}"
        self.mutations_label["text"] = f"Mutations: {self.organism.mutations:.2f}"

    def update_mutation_rate(self):
        self.mutation_rate = float(self.mutation_rate_entry.get())
        self.organism.mutation_rate = self.mutation_rate
        self.mutation_rate_label["text"] = f"Mutation Rate: {self.organism.mutation_rate:.2f}"


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
