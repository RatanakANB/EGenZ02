import datetime

def log_action(action_name, result):
    # TODO: {#{13}} Initial log format
    # This will be modified by multiple members to cause conflicts
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calc_history.log", "a") as f:
        f.write(f"[{timestamp}] {action_name}: 😍{result}\n")
