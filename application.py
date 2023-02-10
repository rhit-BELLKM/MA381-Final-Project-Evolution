import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from organism import Organism

matplotlib.use("TkAgg")

class Application(tk.Frame):
    def __init__(self, master=None, generation=0, orgs_fitness_history=[]):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.generation = generation
        self.orgs_fitness_history = orgs_fitness_history
        self.master.geometry("700x700")
        self.create_widgets()

    def create_widgets(self):
        self.organism = Organism(gui=self)
        
        self.title_label = tk.Label(self, text="Organism Simulator", font=("TkDefaultFont", 16))
        self.title_label.pack(pady=20)

        # Create a frame for the graph
        self.graph_frame = ttk.Frame(self)
        self.graph_frame.pack(side="top", fill="both", expand=True)

        # Create a figure for the graph
        self.figure = Figure(figsize=(1,1), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel("Fitness")
        self.ax.set_ylabel("Generation")
        self.ax.set_xlim(0,5)
        self.ax.set_ylim(0,100)

        # Create a canvas for the graph
        self.canvas = FigureCanvasTkAgg(self.figure, self.graph_frame)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Update the graph
        self.update_graph()

        self.reproduce_button = tk.Button(self, text="Reproduce", command=lambda: self.reproduce(1))
        self.calculate_button = tk.Button(self, text="Calculate Average Fitness", command=lambda: self.calculate_avg_fitness())

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        # self.quit.pack(pady=5)

        self.reset = tk.Button(self, text="RESET", fg="blue", command=lambda: self.reset_graph())

        self.reproduce_button.pack(side="left", padx=10)
        self.calculate_button.pack(side="left", padx=10)
        self.quit.pack(side="left", padx=10)
        self.reset.pack(side="left", padx=10)

        self.generation_label = tk.Label(self, text="Generation: " + str(self.generation), font=("TkDefaultFont", 12))
        self.generation_label.pack(pady=5)
        
        self.fitness_label = tk.Label(self, text="Fitness: 0.0", font=("TkDefaultFont", 12))
        self.fitness_label.pack(pady=5)

        self.mutations_label = tk.Label(self, text="Mutations: 0.0", font=("TkDefaultFont", 12))
        self.mutations_label.pack(pady=5)
        
        self.mutation_rate_label = tk.Label(self, text="Mutation Rate: " + str(self.organism.mutation_rate), font=("TkDefaultFont", 12))
        self.mutation_rate_label.pack(pady=5)

        self.mutation_rate_entry = tk.Entry(self)
        self.mutation_rate_entry.insert(0, "0.01")
        self.mutation_rate_entry.pack(pady=5)

        self.update_mutation_rate_button = tk.Button(self, text="Update Mutation Rate", command=self.update_mutation_rate)
        self.update_mutation_rate_button.pack(pady=5)

    def reproduce(self, times=1):
        self.organism = self.organism.reproduce(times=times)
        self.orgs_fitness_history.append(self.organism.fitness)
        # print("Organism fitness history: ", self.orgs_fitness_history)
        self.generation_label["text"] = f"Generation: {self.generation:.2f}"
        self.fitness_label["text"] = f"Fitness: {self.organism.fitness:.2f}"
        self.mutations_label["text"] = f"Mutations: {self.organism.mutations:.2f}"
        self.update_graph()

    def update_graph(self):
        self.generation = self.generation + 1
        self.ax.set_xlabel("Fitness")
        self.ax.set_ylabel("Generation")
        self.figure = Figure(figsize=(1,1), dpi=100)
        self.ax.plot(self.organism.fitness, self.generation, 'o')
        self.canvas.draw()

    def update_mutation_rate(self):
        self.mutation_rate = float(self.mutation_rate_entry.get())
        self.organism.mutation_rate = self.mutation_rate
        self.mutation_rate_label["text"] = f"Mutation Rate: {self.organism.mutation_rate:.2f}"

    def reset_graph(self):
        self.ax.cla()
        self.ax.set_xlabel("Fitness")
        self.ax.set_ylabel("Generation")
        self.ax.set_xlim(0,5)
        self.ax.set_ylim(0,100)
        self.canvas.draw()

    def calculate_avg_fitness(self):
        fitness_values = self.orgs_fitness_history
        total_fitness = sum(fitness_values)
        total_organisms = len(fitness_values)
        avg_fitness = sum(fitness_values) / len(fitness_values)
        messagebox.showinfo("Average Fitness", "The average fitness is: {:.2f}\nTotal Organisms: {}\nCombined Fitnesses: {:.2f}".format(avg_fitness, total_organisms, total_fitness))

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
