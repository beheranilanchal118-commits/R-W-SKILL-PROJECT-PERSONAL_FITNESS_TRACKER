
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os


class FitnessTracker:


    def __init__(self):
        folder = os.path.dirname(os.path.abspath(__file__))

        self.file_name = os.path.join(
            folder, "fitness_activities.csv"
        )

        self.output_folder = os.path.join(folder, "output")

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        try:
            self.data = pd.read_csv(self.file_name)

            print("CSV file loaded:", self.file_name)
            print("Rows found in CSV:", len(self.data))

            required_columns = [
                "Date",
                "Activity Type",
                "Duration (Minutes)",
                "Calories Burned"
            ]

            if not all(column in self.data.columns
                       for column in required_columns):
                print("Error: CSV column names do not match.")
                print("Required columns:", required_columns)
                print("Your columns:", list(self.data.columns))

                self.data = pd.DataFrame(columns=required_columns)
                return

            self.data["Date"] = pd.to_datetime(
                self.data["Date"], errors="coerce"
            )

            self.data["Duration (Minutes)"] = pd.to_numeric(
                self.data["Duration (Minutes)"], errors="coerce"
            )

            self.data["Calories Burned"] = pd.to_numeric(
                self.data["Calories Burned"], errors="coerce"
            )

            self.data["Activity Type"] = (
                self.data["Activity Type"].astype("string").str.strip()
            )

            self.data = self.data.dropna(
                subset=required_columns
            )

            self.data = self.data[
                (self.data["Activity Type"] != "") &
                (self.data["Duration (Minutes)"] > 0) &
                (self.data["Calories Burned"] > 0)
            ].reset_index(drop=True)

            print("Valid activities loaded:", len(self.data))

        except FileNotFoundError:
            print("ERROR: fitness_activities.csv was not found!")
            print("Place the CSV file in the same folder as this Python file.")

            self.data = pd.DataFrame(columns=[
                "Date",
                "Activity Type",
                "Duration (Minutes)",
                "Calories Burned"
            ])


    def save_data(self):
        self.data.to_csv(
            self.file_name,
            index=False,
            date_format="%Y-%m-%d"
        )

    def log_activity(self, activity_type, duration, calories):

        activity_type = activity_type.strip().title()

        if activity_type == "":
            print("Activity type cannot be empty.")
            return

        if duration <= 0 or calories <= 0:
            print("Duration and calories must be positive.")
            return

        new_activity = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Activity Type": activity_type,
            "Duration (Minutes)": duration,
            "Calories Burned": calories
        }

        self.data.loc[len(self.data)] = new_activity
        self.save_data()
        print("\n================================")
        print("\n  Activity added successfully.")
        print("\n================================")
    def calculate_metrics(self):

        if self.data.empty:
            print("No activity data available.")
            return

        total_calories = self.data["Calories Burned"].sum()

        average_duration = np.mean(
            self.data["Duration (Minutes)"]
        )

        total_minutes = self.data["Duration (Minutes)"].sum()
        print("\n================================")
        print("\n  ----- Fitness Summary -----")
        print("\n================================")
        print("Total activities:", len(self.data))
        print("Total calories burned:", round(total_calories, 2))
        print("Average duration:", round(average_duration, 2), "minutes")
        print("Total exercise time:", round(total_minutes, 2), "minutes")

        print("\nActivities by type:")
        print(self.data["Activity Type"].value_counts().to_string())

        calories_per_minute = (
            self.data["Calories Burned"] /
            self.data["Duration (Minutes)"]
        )

        print(
            "Average calories per minute:",
            round(calories_per_minute.mean(), 2)
        )

    def filter_activities(self, condition):

        if self.data.empty:
            print("No activity data available.")
            return

        if condition == "1":

            activity = input(
                "Enter activity type: "
            ).strip().title()

            result = self.data[
                self.data["Activity Type"] == activity
            ]

        elif condition == "2":

            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")

            try:
                start = pd.to_datetime(start_date)
                end = pd.to_datetime(end_date)

                if start > end:
                    print("Start date cannot be after end date.")
                    return

                result = self.data[
                    (self.data["Date"] >= start) &
                    (self.data["Date"] <= end)
                ]

            except (ValueError, TypeError):
                print("Invalid date format.")
                return

        else:
            print("Invalid filter choice.")
            return

        if result.empty:
            print("No matching activities found.")
        else:
            print(result.to_string(index=False))


    def generate_report(self):

        if self.data.empty:
            print("No activity data available for a report.")
            return

        
        self.data["Date"] = pd.to_datetime(
            self.data["Date"].astype(str),
            errors="coerce"
        )
        print("\n=============================")
        print("\n----- Fitness Report -----")
        print("\n=============================")
        
        valid_dates = self.data["Date"].dropna()

        if not valid_dates.empty:
            start_date = valid_dates.min().strftime("%Y-%m-%d")
            end_date = valid_dates.max().strftime("%Y-%m-%d")

            print("Date range:", start_date, "to", end_date)
        else:
            print("Date range: No valid dates available")

        print("Total activities:", len(self.data))

        total_minutes = self.data["Duration (Minutes)"].sum()
        total_calories = self.data["Calories Burned"].sum()

        print("Total minutes:", round(total_minutes, 2))
        print("Total calories:", round(total_calories, 2))
        print("\n=============================")
        print("\nSummary by activity:")
        print("\n=============================")
        summary = self.data.groupby("Activity Type").agg({
            "Duration (Minutes)": "sum",
            "Calories Burned": "sum"
        })

        if summary.empty:
            print("No valid activity records found.")
        else:
            print(summary.to_string())


    def save_chart(self, file_name):

        file_path = os.path.join(
            self.output_folder,
            file_name
        )

        plt.tight_layout()
        plt.savefig(file_path)

        print("Chart saved successfully:", file_path)

        plt.show()
        plt.close()

    def show_bar_chart(self):

        if self.data.empty:
            print("No data available for the chart.")
            return

        activity_time = self.data.groupby("Activity Type")[
            "Duration (Minutes)"
        ].sum()

        activity_time.plot(
            kind="bar",
            title="Time Spent on Each Activity"
        )

        plt.xlabel("Activity Type")
        plt.ylabel("Duration in Minutes")

        self.save_chart("bar_chart.png")


    def show_line_chart(self):

        if self.data.empty:
            print("No data available for the line chart.")
            return

        
        chart_data = self.data.copy()

        chart_data["Date"] = pd.to_datetime(
            chart_data["Date"].astype(str),
            errors="coerce"
        )

        chart_data["Calories Burned"] = pd.to_numeric(
            chart_data["Calories Burned"],
            errors="coerce"
        )

        
        chart_data = chart_data.dropna(
            subset=["Date", "Calories Burned"]
        )

        if chart_data.empty:
            print("No valid date or calorie data found.")
            return

        
        daily_calories = chart_data.groupby("Date")[
            "Calories Burned"
        ].sum()

        daily_calories = daily_calories.sort_index()

        
        daily_calories.plot(
            kind="line",
            marker="o",
            title="Calories Burned Over Time"
        )

        plt.xlabel("Date")
        plt.ylabel("Calories Burned")
        plt.xticks(rotation=45)

        self.save_chart("line_chart.png")


    def show_pie_chart(self):

        if self.data.empty:
            print("No data available for the chart.")
            return

        activity_count = self.data["Activity Type"].value_counts()

        activity_count.plot(
            kind="pie",
            autopct="%1.1f%%",
            title="Activity Distribution"
        )

        plt.ylabel("")

        self.save_chart("pie_chart.png")

    def show_heatmap(self):

        if len(self.data) < 2:
            print("At least two activities are needed.")
            return

        numbers = self.data[
            ["Duration (Minutes)", "Calories Burned"]
        ]

        correlation = numbers.corr()

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm",
            vmin=-1,
            vmax=1
        )

        plt.title("Duration and Calories Correlation")

        self.save_chart("heatmap.png")

    def show_charts(self):

        while True:
            print("\n=============================")
            print("\n  ----- Charts Menu -----")
            print("\n=============================")
            print("1. Bar Chart")
            print("2. Line Graph")
            print("3. Pie Chart")
            print("4. Heatmap")
            print("5. Generate All Charts")
            print("6. Back to Main Menu")

            choice = input("Choose a chart (1-6): ")

            if choice == "1":
                self.show_bar_chart()

            elif choice == "2":
                self.show_line_chart()

            elif choice == "3":
                self.show_pie_chart()

            elif choice == "4":
                self.show_heatmap()

            elif choice == "5":
                self.show_bar_chart()
                self.show_line_chart()
                self.show_pie_chart()
                self.show_heatmap()

            elif choice == "6":
                break

            else:
                print("Invalid choice. Select from 1 to 6.")

            if choice != "6":
                press_enter()


def get_positive_number(message):

    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid number.")


def press_enter():
    input("\nPress Enter to continue...")


def main():

    tracker = FitnessTracker()

    while True:
        print("\n====================================")
        print(" \n     PERSONAL FITNESS TRACKER ")
        print("\n====================================")
        print("1. Log a New Activity")
        print("2. View Fitness Metrics")
        print("3. Filter Activities")
        print("4. Generate Report")
        print("5. Show Charts")
        print("6. View All Activities")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":

            activity = input(
                "Activity type (Running, Yoga, Cycling, etc.): "
            )

            duration = get_positive_number(
                "Duration in minutes: "
            )

            calories = get_positive_number(
                "Calories burned: "
            )

            tracker.log_activity(
                activity,
                duration,
                calories
            )

            press_enter()

        elif choice == "2":

            tracker.calculate_metrics()
            press_enter()

        elif choice == "3":

            print("\n1. Filter by Activity Type")
            print("2. Filter by Date Range")

            filter_choice = input("Choose filter (1-2): ")

            tracker.filter_activities(filter_choice)
            press_enter()

        elif choice == "4":

            tracker.generate_report()
            press_enter()

        elif choice == "5":

            tracker.show_charts()

        elif choice == "6":

            if tracker.data.empty:
                print("No activities recorded yet.")

            else:
                print(tracker.data.to_string(index=False))

            press_enter()

        elif choice == "7":
            print("\n==================================================")
            print("\n  Thank you for using Personal Fitness Tracker!")
            print("\n==================================================")
            break

        else:

            print("Invalid choice. Please select from 1 to 7.")
            press_enter()


if __name__ == "__main__":
    main()
