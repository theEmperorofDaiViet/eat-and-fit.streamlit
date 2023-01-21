class Cardio():
    def __init__(self, stage, body, sex, sessions, time):
        self.stage = stage
        self.body = body
        self.sex = sex
        self.sessions = sessions
        self.time = time

class Gym():
    def __init__(self, day, exercise, sets, reps):
        self.day = day
        self.exercise = exercise
        self.sets = sets
        self.reps = reps

class Exercise():
    def __init__(self, id, name, link, overview, introductions):
        self.id = id
        self.name = name
        self.link = link
        self.overview = overview
        self.introductions = introductions

    def get_overview_paragraph(self):
        return self.overview.split(';')

    def get_introductions_detail(self):
        return self.introductions.split(';')