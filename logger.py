import datetime

def log_action(action_name, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calc_history.log", "a") as f:
<<<<<<< HEAD
        f.write(f"[{timestamp}] ACTION={action_name}RESULT={result}\n")
=======
        f.write(f"[{timestamp}] {action_name}: 😍{result}\n")
>>>>>>> ddb4d7f (fix: logger and cal2)
