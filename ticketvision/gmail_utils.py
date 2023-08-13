from datetime import datetime
import datetime
import google_workspace


def authenticate():
    """
    Returns authentication credentials to run the client.
    """
    service = google_workspace.service.GoogleService(
        api="gmail",
        session="my-gmail",
        client_secrets=r"C:\Users\diabl\PycharmProjects\Gmail_Second\ticketvision\credentials.json"
    )
    service.local_oauth()
    return service


def client():
    """
    Returns the client after using the credentials.
    """
    gmail_client = google_workspace.gmail.GmailClient(service=authenticate())
    return gmail_client


def from_():
    """
    Returns a str of who message(s) are from. Must follow gmail format (choose either): "NAME <username@domain.com>"
    """
    fr = input("From: ")
    if fr == "":
        return None
    return str(fr)


def to_address():
    """
    Returns a list of addresses.
    GET: Must follow gmail format (choose either): "NAME <username@domain.com>"
    SEND: Must follow gmail format: <username@domain.com>
    """
    addresses = []
    while True:
        address = input("Address(es) (type 'done' to finish): ")
        if address == "done":
            break
        elif address is []:
            return None
        try:
            add = str(address)
        except:
            print("Invalid input")
            continue
        addresses.append(add)
    return addresses


def subject():
    """
    Returns user input as a str to search by subject text. Full subject line not needed.
    """
    subj = input("Subject: ")
    if subj == "":
        return None
    return str(subj)


def create_body():
    """
    Returns a str from user input for the body text of an email. Use html commands to format the text.
    """
    body = input("Write your message body: ")
    return body


def filter_time():
    """
    Returns a tuple of dates to filter by a date range.
    """
    while True:
        try:
            start_month = input("Start Month: ")
            start_day = input("Start Day: ")
            start_year = input("Start Year: ")
            end_month = input("End Month: ")
            end_day = input("End Day: ")
            end_year = input("End Year: ")
            start_date = datetime.date(year=int(start_year), month=int(start_month), day=int(start_day))
            end_date = datetime.date(year=int(end_year), month=int(end_month), day=int(end_day))
            return start_date, end_date
        except Exception as e:
            print("Error: ", e)
            print("Provided an incorrect date, check that all numbers are whole numbers.")
            continue


def label_name():
    """
    Returns user input as a str to search by a label. Must type label in full.
    """
    lbl_name = input("Label Name: ")
    if lbl_name == "":
        return None
    return str(lbl_name)


def spam_trash():
    """
    Returns a bool response to determine whether to include spam & trash.
    """
    spam_and_trash = input("Include spam/trash (y/n)").lower()
    if spam_and_trash == "y":
        return True
    elif spam_and_trash == "n":
        return False
    else:
        print("That is not y/n, default n")
        return False
