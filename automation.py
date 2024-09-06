import subprocess

def run_script(script_name):
    try:
        # Run the script
        result = subprocess.run(['python3', script_name], check=True)
        print(f"{script_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")

# Run the scripts in order
run_script('05-generate.py')
run_script('05-logs.py')