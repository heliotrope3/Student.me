from Task import Task
from Prompt import Prompt

prompts = {
    "tests": [
        Prompt("Math Test", Task("Study", -10), Task("Cry", 10))
    ],
    "downtime": [
        Prompt("You have some downtime", Task("Study", -10), Task("Watch Netflix", 10))
    ],
    "encounter": [
        Prompt("Someone doesn't like your sweater", Task("Fight", 10), Task("Flight", 10))
    ]
}