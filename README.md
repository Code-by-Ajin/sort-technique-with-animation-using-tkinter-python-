📊 Sorting Algorithm & Animation Visualizer

A dynamic, interactive Python application built with **Tkinter** that visualizes classic sorting algorithms in real time. It allows users to input custom datasets and choose between multiple rendering styles—including traditional bar charts, scatter plots, and a vibrant rainbow spectrum.

---

## ✨ Features

* **Multiple Sorting Algorithms:**
    * **Bubble Sort** (Ideal for understanding basic adjacent swapping)
    * **Insertion Sort** (Visualizes element-by-element array insertion)
    * **Merge Sort** (Demonstrates divide-and-conquer sub-array building)
    * **Quick Sort** (Shows pointer movement and pivot-locking mechanics)
* **Diverse Animation Techniques:**
    * 📐 **Bar Chart Height:** Standard bar visualization where height matches the value.
    * 🌌 **Scatter Plot / Dots:** Plots isolated coordinate points—great for observing global data noise reductions.
    * 🌈 **Rainbow / Color Wheel:** Columns transition through the HSV spectrum, rearranging chaotic blocks into a clean gradient.
* **Interactive Controls:** Custom comma-separated inputs and real-time animation delay/speed adjustments.

---

## 🛠️ Visualizing the Operations

The application uses intuitive color states to guide the user through each algorithm's workflow:
* **Blue/Indigo:** Standard unsorted elements.
* **Yellow/Red:** Active comparisons, scanning arrays, and direct element swaps.
* **Purple:** Current designated **Pivot** element (for Quick Sort).
* **Green:** Finalized, successfully sorted index confirmation.

---

## 🚀 Getting Started

### Prerequisites

You need **Python 3.x** installed on your system. Tkinter comes bundled with standard Python installations on Windows and macOS. 

If you are on **Linux** (Ubuntu/Debian), you may need to install it explicitly:
 bash
sudo apt-get install python3-tk
Installation & Execution
Clone this repository or download the source code:

Bash
git clone [https://github.com/YOUR_USERNAME/sorting-visualizer.git](https://github.com/YOUR_USERNAME/sorting-visualizer.git)
cd sorting-visualizer
Run the application:

Bash
python3 sort_animation.py
📖 How to Use
Enter a custom list of integers separated by commas in the input field (e.g., 40, 10, 30, 20).

Select your preferred Algorithm from the dropdown menu.

Choose an Animation Style (Bar Chart, Scatter Plot, or Rainbow).

Use the Delay (s) slider to speed up or slow down the execution.

Click ⚡ Run Animation to view the process step-by-step.
