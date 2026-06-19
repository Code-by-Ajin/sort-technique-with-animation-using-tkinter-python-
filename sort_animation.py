import tkinter as tk
from tkinter import ttk, messagebox
import time
import colorsys

class AdvancedVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Technique Sorting Visualizer")
        self.root.geometry("900x650")
        self.root.config(bg="#1E1E24")

        self.data = []
        self.running = False

        self.setup_ui()

    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Sorting Algorithm & Animation Visualizer", font=("Helvetica", 16, "bold"), bg="#1E1E24", fg="#E2E8F0")
        title.pack(pady=10)

        # Control Panel
        control_frame = tk.Frame(self.root, bg="#2D3748", bd=1, relief=tk.SOLID)
        control_frame.pack(pady=5, fill=tk.X, padx=20)

        # Row 1: Inputs
        tk.Label(control_frame, text="Numbers (comma-separated):", bg="#2D3748", fg="#E2E8F0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.input_entry = tk.Entry(control_frame, width=45, font=("Helvetica", 10))
        self.input_entry.insert(0, "55, 22, 88, 44, 11, 99, 33, 77, 66, 50, 5, 80, 25, 70, 15")
        self.input_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="w")

        # Row 2: Selectors
        tk.Label(control_frame, text="Algorithm:", bg="#2D3748", fg="#E2E8F0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.algo_menu = ttk.Combobox(control_frame, values=["Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"], state="readonly", width=15)
        self.algo_menu.set("Bubble Sort")
        self.algo_menu.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(control_frame, text="Animation Style:", bg="#2D3748", fg="#E2E8F0").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.style_menu = ttk.Combobox(control_frame, values=["Bar Chart Height", "Scatter Plot / Dots", "Rainbow / Color Wheel"], state="readonly", width=22)
        self.style_menu.set("Bar Chart Height")
        self.style_menu.grid(row=1, column=3, padx=10, pady=10)

        # Delay Slider
        tk.Label(control_frame, text="Delay (s):", bg="#2D3748", fg="#E2E8F0").grid(row=0, column=4, padx=10, pady=10)
        self.speed_scale = tk.Scale(control_frame, from_=0.01, to=1.0, resolution=0.05, orient=tk.HORIZONTAL, length=120, bg="#2D3748", fg="#E2E8F0", highlightbackground="#2D3748")
        self.speed_scale.set(0.2)
        self.speed_scale.grid(row=0, column=5, padx=10, pady=0)

        # Action Button
        self.start_btn = tk.Button(control_frame, text="⚡ Run Animation", command=self.start_sorting, bg="#38A169", fg="white", font=("Helvetica", 10, "bold"), width=15)
        self.start_btn.grid(row=1, column=5, padx=10, pady=10)

        # Canvas Display
        self.canvas = tk.Canvas(self.root, width=860, height=400, bg="#0F172A", highlightthickness=0)
        self.canvas.pack(pady=15, padx=20)

    def get_color(self, val, max_val, index, total, state_color=None):
        """Generates color maps dynamically depending on the selected visualization style."""
        style = self.style_menu.get()
        
        if state_color:
            return state_color # Override default colors during operations (e.g. Red for swap)
            
        if style == "Rainbow / Color Wheel":
            # Map values to distinct HSV wheel angles
            hue = (val / max_val) * 0.7  # Limit to 0.7 so it doesn't loop completely back to red
            r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
            return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'
        
        elif style == "Scatter Plot / Dots":
            return "#38BDF8" # Bright Cyan sky color for dots
            
        return "#6366F1" # Default Indigo for normal bars

    def draw_frame(self, highlights=None):
        """Renders the frame based on the chosen animation style technique."""
        self.canvas.delete("all")
        if not self.data: return

        c_width = 860
        c_height = 400
        total_elements = len(self.data)
        max_val = max(self.data) if max(self.data) != 0 else 1
        
        spacing = 4
        item_width = (c_width - (total_elements + 1) * spacing) / total_elements
        style = self.style_menu.get()

        for i, val in enumerate(self.data):
            x0 = i * item_width + (i + 1) * spacing
            x1 = x0 + item_width
            
            # Determine custom action state color if targeted
            state_color = highlights.get(i) if highlights else None
            color = self.get_color(val, max_val, i, total_elements, state_color)

            # TECH 1 & 3: Bar Height / Rainbow Layout
            if style in ["Bar Chart Height", "Rainbow / Color Wheel"]:
                y0 = c_height - (val / max_val * (c_height - 60))
                y1 = c_height
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
                if total_elements <= 25: # Display numbers above bars if array size permits
                    self.canvas.create_text(x0 + item_width/2, y0 - 12, text=str(val), font=("Helvetica", 8, "bold"), fill="#94A3B8")

            # TECH 2: Scatter Plot / Dots Layout
            elif style == "Scatter Plot / Dots":
                y_center = c_height - (val / max_val * (c_height - 60))
                radius = max(4, item_width / 2) # Adapt dot size to array bounds
                # If active operational change, blow up dot size slightly for emphasis
                if state_color:
                    radius *= 1.5
                self.canvas.create_oval(x0, y_center - radius, x0 + (radius*2), y_center + radius, fill=color, outline="")
                if total_elements <= 25:
                    self.canvas.create_text(x0 + radius, y_center - (radius + 10), text=str(val), font=("Helvetica", 8), fill="#94A3B8")

        self.root.update()

    def start_sorting(self):
        if self.running: return
        try:
            self.data = [int(x.strip()) for x in self.input_entry.get().split(",") if x.strip() != ""]
            if not self.data: raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please provide a valid sequence of integers separated by commas.")
            return

        self.running = True
        self.start_btn.config(state=tk.DISABLED, bg="#4A5568")
        
        algo = self.algo_menu.get()
        delay = self.speed_scale.get()

        if algo == "Bubble Sort":
            self.bubble_sort(delay)
        elif algo == "Insertion Sort":
            self.insertion_sort(delay)
        elif algo == "Merge Sort":
            self.merge_sort(0, len(self.data) - 1, delay)
        elif algo == "Quick Sort":
            self.quick_sort(0, len(self.data) - 1, delay)

        # Completion animation state
        self.draw_frame({i: "#10B981" for i in range(len(self.data))})
        self.running = False
        self.start_btn.config(state=tk.NORMAL, bg="#38A169")

    # --- 1. BUBBLE SORT ---
    def bubble_sort(self, delay):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.draw_frame({j: "#EF4444", j+1: "#F59E0B"}) # Red / Yellow compare
                time.sleep(delay)
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    self.draw_frame({j: "#F59E0B", j+1: "#EF4444"})
                    time.sleep(delay)

    # --- 2. INSERTION SORT ---
    def insertion_sort(self, delay):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.draw_frame({j: "#EF4444", j+1: "#F59E0B"})
                time.sleep(delay)
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
            self.draw_frame({j+1: "#10B981"})
            time.sleep(delay)

    # --- 3. MERGE SORT ---
    def merge_sort(self, left, right, delay):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid, delay)
            self.merge_sort(mid + 1, right, delay)
            self.merge(left, mid, right, delay)

    def merge(self, left, mid, right, delay):
        left_part = self.data[left:mid + 1]
        right_part = self.data[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            self.draw_frame({k: "#EF4444", left+i: "#F59E0B", mid+1+j: "#3B82F6"})
            time.sleep(delay)
            if left_part[i] <= right_part[j]:
                self.data[k] = left_part[i]
                i += 1
            else:
                self.data[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            self.data[k] = left_part[i]
            i += 1; k += 1
        while j < len(right_part):
            self.data[k] = right_part[j]
            j += 1; k += 1
        self.draw_frame({m: "#10B981" for m in range(left, right+1)})
        time.sleep(delay)

    # --- 4. QUICK SORT ---
    def quick_sort(self, low, high, delay):
        if low < high:
            p_idx = self.partition(low, high, delay)
            self.quick_sort(low, p_idx - 1, delay)
            self.quick_sort(p_idx + 1, high, delay)

    def partition(self, low, high, delay):
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            self.draw_frame({j: "#F59E0B", high: "#8B5CF6", i: "#EF4444"}) # Yellow scanner, Purple pivot
            time.sleep(delay / 2)
            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.draw_frame({i: "#EF4444", j: "#EF4444"})
                time.sleep(delay / 2)
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.draw_frame({i + 1: "#10B981"})
        time.sleep(delay)
        return i + 1

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedVisualizer(root)
    root.mainloop()