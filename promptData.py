from Task import Task
from Prompt import Prompt

#health, stress, smarts, happiness

prompts = {
    "schoolwork": [
        Prompt(["Math Test"], Task(["Study"], 0, -10, 10, -5), Task(["Cry"], 0, 10, -5, -5)),
        Prompt(["Science Test"], Task(["Study"], 0, -10, 15, -5), Task(["Cry"], 0, 15, -10, -5)),
        Prompt(["English", "Assignment"], Task(["Read"], 0, -15, 10, 5), Task(["Play"], 0, 10, -10, 5)),
        Prompt(["Geography Test"], Task(["Study"], 0, -5, 10, 0), Task(["Play"], 5, 10, -5, 5)),
        Prompt(["History", "Project"], Task(["Do it"], 0, -10, 10, 0), Task(["Cry"], 0, 10, -5, -5))
    ],
    
    "extra-time": [
        Prompt(["You have some", "downtime"], Task(["Study"], 0, -5, 10, 0), Task(["Watch Netflix"], -5, 10, -5, 5)),
        Prompt(["You finished", "your homework"], Task(["Read"], 5, 0, 10, 10), Task(["Play"], -5, 5, -10, 5)),
        Prompt(["You have some", "free time"], Task(["Study"], 0, -10, 10, -5), Task(["Watch", "YouTube"], 0, 10, -5, -5)),
        Prompt(["You need to go to", "your part-time job"], Task(["Go to work"], 0, 5, 5, -5), Task(["Call in sick"], 0, 5, -5, 5)),
        Prompt(["You have to eat", "dinner"], Task(["Cook"], 10, 0, 10, 5), Task(["Order", "Takeout"], -10, 0, -5, 5))
    ],

    "encounter": [
        Prompt(["Someone doesn't", "like your sweater"], Task(["Fight"], -10, 10, -5, -10), Task(["Ignore"], 0, 10, 5, -10)),
        Prompt(["Your friends", "want to hangout"], Task(["Hangout"], 5, 5, 0, 20), Task(["Read"], 5, -5, 10, 15)),
        Prompt(["A drink is spilled on", "your favourite sweater"], Task(["Yell at them"], -5, 10, 0, -10), Task(["Let it go"], 0, 5, 0, -10)),
        Prompt(["It's your", "friends birthday"], Task(["Say Happy", "Birthday"], 0, -10, 5, 5), Task(["Get them", "a gift"], 0, 10, 10, 10)),
        Prompt(["Your school", "is having a BBQ"], Task(["Go to the BBQ"], 5, -10, 0, 10), Task(["Stay at home"], 5, -10, 0, 5))

    ]
}