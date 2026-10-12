# 🏋️ Personal Fitness Tracker Dashboard

## 📌 Project Overview

The **Personal Fitness Tracker Dashboard** is a Python-based project designed to help users record, manage, analyze, and visualize their daily fitness activities. It allows users to track exercises such as running, walking, yoga, and cycling, along with exercise duration and calories burned.

This project uses basic Python programming concepts and data analysis libraries to provide a simple and user-friendly fitness tracking system.

## ✨ Features

- 📝 **Activity Logging:** Record activities with exercise type, duration, and calories burned.
- ✅ **Input Validation:** Check user inputs to prevent invalid values.
- 📊 **Fitness Metrics:** Calculate total calories burned, average activity duration, and total exercise time.
- 🔍 **Activity Filtering:** Filter records by activity type or date range.
- 📄 **Fitness Report:** Generate a summary of fitness activities and statistics.
- 💾 **CSV Data Management:** Read and save fitness records in a CSV file.
- 🧮 **Data Analysis:** Use NumPy and Pandas to calculate and organize fitness data.
- 📈 **Data Visualization:** Display fitness progress through different charts.
- 🖼️ **Chart Saving:** Automatically save chart images in the `output` folder.
- 🖥️ **Menu-Driven Interface:** Navigate through the application using a simple menu.

## 🛠️ Technologies Used

- 🐍 Python
- 🔢 NumPy
- 🐼 Pandas
- 📊 Matplotlib
- 🎨 Seaborn
- 📁 CSV File Handling

## 📊 Data Visualizations

The project includes four types of charts to help users understand their fitness activities:

1. 📊 **Bar Chart:** Displays the total time spent on each activity type.
2. 📈 **Line Graph:** Shows calories burned over time.
3. 🥧 **Pie Chart:** Displays the percentage distribution of recorded activities.
4. 🌡️ **Heatmap:** Shows the correlation between exercise duration and calories burned.

Generated charts are automatically saved as image files in the `output` folder.

## 📂 Dataset Information

The project uses a CSV file named `fitness_activities.csv` to store fitness records.

The dataset contains the following columns:

- 📅 `Date`
- 🏃 `Activity Type`
- ⏱️ `Duration (Minutes)`
- 🔥 `Calories Burned`

Users can add new activities, and the updated records are saved in the CSV file.

## ⚙️ Installation and Setup

Follow these steps to run the project on your computer:

1. 🐍 Install Python 3.
2. 📥 Download or clone this repository.
3. 💻 Open the project folder in Visual Studio Code.
4. 📦 Install the required libraries:

   `pip install pandas numpy matplotlib seaborn`

5. 📁 Keep `fitness_activities.csv` in the same folder as `fitness_tracker.py`.
6. ▶️ Run the `fitness_tracker.py` file.
7. 🎯 Select options from the menu to record activities, view reports, analyze data, and generate charts.

## 🧠 Python Concepts Used

- Variables and Data Types
- Conditional Statements (`if-elif-else`)
- Loops
- Functions
- Input Validation
- Object-Oriented Programming (OOP)
- NumPy Numerical Calculations
- Pandas Data Handling
- Matplotlib and Seaborn Visualization
- CSV File Handling
- Exception Handling

## 🎯 Project Objective

The main objective of this project is to apply Python programming and data analysis concepts to a practical fitness tracking application. It helps users review their exercise habits, monitor activity statistics, and understand fitness trends through charts and reports.

## 🚀 Future Improvements

- 🖥️ Add a graphical user interface.
- 📅 Include weekly and monthly fitness summaries.
- 👤 Add user profiles and personalized fitness goals.
- 📄 Export fitness reports to PDF.
- 📊 Include additional fitness statistics.

## ✅ Conclusion

The **Personal Fitness Tracker Dashboard** demonstrates how Python can be used to build a basic data analysis application. By combining activity logging, numerical calculations, CSV data management, and visualization, the project provides a straightforward way to track fitness activities and understand exercise trends.

---

**⚠️ Note:** This project is intended for educational purposes. Calories burned are user-entered estimates and may not represent medically accurate measurements.

⭐ *If you find this project useful, consider giving the repository a star!*
