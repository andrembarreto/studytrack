import json

class Attendance:
    def __init__(self, workload_hours):
        self.workload_hours = workload_hours
        self.current_attendance = 0

    def __eq__(self, __value: object):
        return isinstance(__value, Attendance) and self.workload_hours == __value.workload_hours and self.current_attendance == __value.current_attendance


    def update_current_attendance(self, hours):
        updated_attendance = self.current_attendance + hours
        if updated_attendance < 0:
            raise ValueError('The final attendance value cannot be less than 0')
        self.current_attendance += hours

    def get_minimun_attendance(self):
        return round(self.workload_hours * 0.75)

    def has_minimun_attendance(self):
        return self.current_attendance >= self.get_minimun_attendance()
    
    def to_json(self):
        attendance_dict = {"workload_hours" : self.workload_hours,
                        "current_attendance" : self.current_attendance
        }
        return json.dumps(attendance_dict)
    
    @staticmethod
    def from_json(json_obj):
        json_obj = json.loads(json_obj)
        attendance = Attendance(workload_hours=json_obj.get('workload_hours'))
        attendance.current_attendance =json_obj.get('current_attendance')

        return attendance
    