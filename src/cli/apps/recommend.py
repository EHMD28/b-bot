import apps.utils.send_email as sendmail
from ssl import create_default_context
import json
import os
from random import randint


def recommend_dinner_list(reciever: str):
    if reciever is not None:
        pathjoin = os.path.join
        with open(pathjoin("apps", "data", "misc", "meals.json"), "r") as f:
            meals: list = json.load(f)

        meals_to_send: list = []
        for i in range(5):
            rand_index = randint(0, len(meals) - 1)
            meals_to_send.append(meals[rand_index])

        next_sunday: str = sendmail.find_next_sunday()
        body = f"""
            1. {meals_to_send[0]}
            2. {meals_to_send[1]}
            3. {meals_to_send[2]}
            4. {meals_to_send[3]}
            5. {meals_to_send[4]}
        """
        email = sendmail.make_EmailMessage(
            os.environ.get("LIST_RECIEVER"),
            os.environ.get("BBOT_EMAIL_ADDRESS"),
            f"Recommended Dinner List for Week of {next_sunday}",
            body=body,
        )

        sendmail.send_email(
            os.environ.get("BBOT_EMAIL_ADDRESS"),
            os.environ.get("BBOT_EMAIL_PASSWORD"),
            reciever,
            email,
            create_default_context(),
        )

