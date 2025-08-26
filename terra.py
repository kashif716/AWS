import subprocess

def terraform_run(command):
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(process.stdout.decode())
    print(process.stderr.decode())

directory = "/home/kashifali/Downloads/python-workshop-practice/terra-automate/Wanderlust-Mega-Project/terraform"
command = f"terraform -chdir={directory} plan"

terraform_run(command)



