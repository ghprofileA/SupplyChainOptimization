import csv
import os

def add_edge_to_csv():
    csv_path = os.path.join("data", "user_edges.csv")
    with open(csv_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        while True:
            source = input("Enter source node (or type 'exit' to finish): ").strip()
            if source.lower() == "exit":
                break
            target = input("Enter target node: ").strip()
            weight = input("Enter weight (numeric): ").strip()
            
            if weight.isdigit():
                weight = int(weight)
                writer.writerow([source, target, weight])
                print(f"Edge added: {source} -> {target} with weight {weight}")
            else:
                print("Invalid weight. Please enter a numeric value.")
