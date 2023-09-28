from deps.gmail_bot import GmailBot
import inquirer
from inquirer.themes import GreenPassion


def session():
    gmail_client = GmailBot()

    questions = [
        inquirer.List(
            "action",
            message="What action would like to take?",
            choices=[
                "Filter Mail",
                "All Inbox",
                "All Mail",
                "Send Mail",
                "Close"
            ],
        )
    ]
    answers = inquirer.prompt(questions, theme=GreenPassion())

    if answers["action"] == "Filter Mail":
        questions = [
            inquirer.Checkbox(
                "filters",
                message="Which filters do you want to use?",
                choices=[
                    "From",
                    "Subject",
                    "To",
                    "Date",
                    "Label Name",
                    "Spam & Trash"
                ]
            )
        ]
        answers = inquirer.prompt(questions, theme=GreenPassion())
        if answers["filters"] == "From":
            filter_msgs = gmail_client.gmail_bot.get_messages()
            for msg in filter_msgs:
                print(msg)

    if answers["action"] == "All Inbox":
        try:
            inbox_msgs = gmail_client.get_inbox_all()
            for msg in inbox_msgs:
                print(msg)
        except Exception as e:
            print("Error: ", e)
            print("Failed to pull inbox, see error.")

    elif answers["action"] == "All Mail":
        try:
            mail_msgs = gmail_client.get_all_mail()
            for msg in mail_msgs:
                print(msg)
        except Exception as e:
            print("Error: ", e)
            print("Failed to pull inbox, see error.")

    elif answers["action"] == "Send Mail":
        try:
            gmail_client.send_message()
            print("Message has been sent.")
        except Exception as e:
            print("Error: ", e)
            print("Your email has failed to send, see error.")

    elif answers["action"] == "Close":
        print("Closing Program")


if __name__ == "__main__":
    session()
