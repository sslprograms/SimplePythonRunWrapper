import subprocess, random, string, os

class loadModule:

  def run(self, script):
    name = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=7))
    open(
      f'data//{name}.py',
      'w'
    ).write(script)

    file = f'data//{name}.py'
    text = subprocess.getoutput(f'python3 {file}')
    os.remove(file)

    return text
    
