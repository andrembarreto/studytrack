import json

class Attendance:
    def __init__(self, workload_hours, minimum_attendance_percentage = 0.75):
        self.workload_hours = workload_hours
        self.current_attendance = 0
        self.minimum_attendance_percentage = minimum_attendance_percentage

    def __eq__(self, __value: object):
        return isinstance(__value, Attendance) and self.workload_hours == __value.workload_hours and self.current_attendance == __value.current_attendance


    def update_current_attendance(self, hours):
        updated_attendance = self.current_attendance + hours
        if updated_attendance < 0:
            raise ValueError('The final attendance value cannot be less than 0')
        self.current_attendance += hours

    def get_minimum_attendance(self):
        return round(self.workload_hours * self.minimum_attendance_percentage)

    def has_minimum_attendance(self):
        return self.current_attendance >= self.get_minimum_attendance()
    
    def print(self):
        print(f"Workload in hours: {self.workload_hours}")
        print(f"Current attendance in hours: {self.current_attendance}")
        print(f"Minimum attendance: {self.get_minimum_attendance()}")

    def to_json(self):
        attendance_dict = {"workload_hours" : self.workload_hours,
                        "current_attendance" : self.current_attendance,
                        "minimum_attendance_percentage" : self.minimum_attendance_percentage
        }
        return json.dumps(attendance_dict)
    
    @staticmethod
    def from_json(json_obj):
        json_obj = json.loads(json_obj)
        attendance = Attendance(workload_hours=json_obj.get('workload_hours'), 
                                minimum_attendance_percentage=json_obj.get('minimum_attendance_percentage'))
        attendance.current_attendance =json_obj.get('current_attendance')

        return attendance
    