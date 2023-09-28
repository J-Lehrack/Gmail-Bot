import google_workspace

import inquirer
from inquirer.themes import GreenPassion
from pprint import pprint

import datetime


def authenticate():
    service = google_workspace.service.GoogleService(
        api="gmail",
        session="my-gmail",
        client_secrets=r"C:\Users\diabl\PycharmProjects\Gmail_Second\ticketvision\credentials.json"
        )
    service.local_oauth()
    return service


def client():
    gmail_client = google_workspace.gmail.GmailClient(service=authenticate())
    return gmail_client


def filter_time():
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


def from_():
    fr = input("From: ")
    if fr == "":
        return None
    return fr


def subject():
    subj = input("Subject: ")
    if subj == "":
        return None
    return subj


def to_address():
    addresses = []
    while True:
        address = input("To Address (type 'done' to finish): ")
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


def label_name():
    lbl_name = input("Label Name: ")
    if lbl_name == "":
        return None
    return lbl_name


def spam_trash():
    spam_and_trash = input("Include spam/trash (y/n): ").lower()
    if spam_and_trash == "y":
        return True
    elif spam_and_trash == "n":
        return False
    else:
        print("That is not y/n, defaulting to n")
        return False


def filter_emails():
    cl = client()
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
    fr = answers["filters"]["From"] = from_()
    sub = answers["filters"]["Subject"] = subject()
    to = answers["filters"]["To"] = to_address()
    date = answers["filters"]["Date"] = filter_time()
    lbl = answers["filters"]["Label Name"] = label_name()
    sptr = answers["filters"]["Spam & Trash"] = spam_trash()
    filter_date = date
    for message in cl.get_messages(
            from_=fr,
            subject=sub,
            to=to,
            after=filter_date[0],
            before=filter_date[1],
            label_name=lbl,
            include_spam_and_trash=sptr
    ):
        yield message


def main():
    cl = client()
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
    print("Here is the dict of filters selected:")
    pprint(answers)
    filters = answers["filters"]
    print("Here is a list of the filters: ", filters)
    new_vars = []
    for filters in answers["filters"]:
        if "From" in filters:
            var = from_()
            new_vars.append(var)

        elif "From" not in filters:
            var = None
            new_vars.append(var)

        elif "Subject" in filters:
            var = subject()
            new_vars.append(var)

        elif "Subject" not in filters:
            var = None
            new_vars.append(var)

        elif "To" in filters:
            var = to_address()
            new_vars.append(var)

        elif "To" not in filters:
            var = None
            new_vars.append(var)

        elif "Date" in filters:
            var = filter_time()
            new_vars.append(var)

        elif "Date" not in filters:
            var = None
            new_vars.append(var)

        elif "Label Name" in filters:
            var = label_name()
            new_vars.append(var)

        elif "Label Name" not in filters:
            var = None
            new_vars.append(var)

        elif "Spam & Trash" in filters:
            var = spam_trash()
            new_vars.append(var)

        elif "Spam & Trash" not in filters:
            var = False
            new_vars.append(var)

    print(new_vars)

  #  for message in cl.get_messages(
  #          from_=new_vars[0],
  #          subject=new_vars[1],
  #          to=new_vars[2],
  #          after=new_vars[3][0],
  #          before=new_vars[3][1],
  #          label_name=new_vars[4],
  #          include_spam_and_trash=new_vars[5]
  #  ):
  #      yield message


if __name__ == "__main__":
    main()
