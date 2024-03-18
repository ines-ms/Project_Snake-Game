class Activity:
    def __init__(self, activity_type, duration, distance, calories_burned):
        self.activity_type = activity_type
        self.duration = duration  # in minutes
        self.distance = distance  # in kilometers for applicable activities
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.activity_type}: {self.distance} km in {self.duration} minutes, {self.calories_burned} calories burned"


class User:
    def __init__(self, name):
        self.name = name
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def get_activities_summary(self):
        summary = {}
        for activity in self.activities:
            if activity.activity_type not in summary:
                summary[activity.activity_type] = {
                    'total_distance': 0,
                    'total_duration': 0,
                    'total_calories': 0,
                    'count': 0
                }
            summary_info = summary[activity.activity_type]
            summary_info['total_distance'] += activity.distance
            summary_info['total_duration'] += activity.duration
            summary_info['total_calories'] += activity.calories_burned
            summary_info['count'] += 1
        return summary

    def print_summary(self):
        summary = self.get_activities_summary()
        for activity_type, info in summary.items():
            print(f"{activity_type} - Total distance: {info['total_distance']} km, Total duration: {info['total_duration']} min, Total calories: {info['total_calories']}, Activities: {info['count']}")
# Create a user
user = User("Alex")

# Simulate adding activities
user.add_activity(Activity("Running", 30, 5, 300))
user.add_activity(Activity("Cycling", 60, 20, 600))
user.add_activity(Activity("Swimming", 45, 2, 400))

# Print summary of activities
user.print_summary()
