from main.models import Course
from django.utils.text import slugify

courses = [
    ("Robotics", "animations/robotics.png"),
    ("Meditation & Mindfulness", "animations/Dawn Meditation by the Lake_ Serenity in Pink and Purple.jpg"),
    ("Learn Guitar in 30 Days", "animations/guitar30days.jpg"),
    ("Motion Design in After Effects", "animations/motiondesign.png"),
    ("Time Management like a CEO", "animations/timemanagement.jpg"),
    ("Intro to AI", "animations/introtoai.png"),
    ("Sound Design Essentials", "animations/sounddesign.webp"),
    ("Creative Thinking for Designers", "animations/design-thinking.jpg"),
    ("Speak Like a Pro", "animations/speak.jpg"),
]

for title, image_path in courses:
    Course.objects.get_or_create(
        title=title,
        slug=slugify(title),
        description="This is a course about " + title,
        instructor="Instructor Team Uiren",
        duration=10,
        rating=4.8,
        image=image_path
    )
