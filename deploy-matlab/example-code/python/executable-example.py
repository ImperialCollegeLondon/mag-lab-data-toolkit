import subprocess

result = subprocess.run(["./exampleFunction",  "input"], capture_output=True)

print(result.stdout.decode())

print("\n")

print(result.stderr.decode())

print(f"\n{result.returncode}")