import datetime

timestamp = 1701159106519.3965 / 1000  # dividing by 1000 if the timestamp is in milliseconds
dt_object = datetime.datetime.utcfromtimestamp(timestamp)

print("The exact date and time is:", dt_object)