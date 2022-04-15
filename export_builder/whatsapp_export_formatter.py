def process(message_object):
    output = "{date}, {time} - {name}: {message}"
    return output.format(date = message_object.date, time=message_object.time, name=message_object.sender_name, message=message_object.message)