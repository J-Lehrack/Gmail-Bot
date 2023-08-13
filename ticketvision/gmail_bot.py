from gmail_utils import *


class GmailBot:
    """
    Class that initializes the gmail client. Allows users to:
    Get their entire inbox (all messages labeled "Inbox")
    Get all of their mail (from All Mail in gmail)
    Filter search for their mail
    Send a message (format using html commands)
    """
    def __init__(self):
        self.gmail_bot = client()

    def get_inbox_all(self):
        """
        Call the Gmail API to fetch all mail labeled "Inbox"
        """
        for message in self.gmail_bot.get_messages(label_name="Inbox"):
            yield message

    def get_all_mail(self):
        """
        Call the Gmail API to fetch All Mail
        """
        for message in self.gmail_bot.get_messages(label_name="All Mail"):
            yield message

    def get_filter_mail(self):
        """
        Filters the fetch request based on user input.
        """
        filter_date = filter_time()
        for message in self.gmail_bot.get_messages(
                from_=from_(),
                subject=subject(),
                to=to_address(),
                after=filter_date[0],
                before=filter_date[1],
                label_name=label_name(),
                include_spam_and_trash=spam_trash()
        ):
            yield message

    def send_message(self):
        """
        Crafts am email based on user input. Use html commands during the
        creation of the body text to format the message.
        """
        message = self.gmail_bot.send_message(
            to=to_address(),
            subject=subject(),
            html=create_body(),
            cc=to_address(),
            bcc=to_address()
        )
        return message


if __name__ == "__main__":
    client = GmailBot()
