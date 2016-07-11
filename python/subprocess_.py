import subprocess

def run_script(script, stdin=None):
    proc = subprocess.Popen(['bash', '-c', script],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise ScriptException(proc.returncode,
                            stdout,
                            stderr,
                            script)
    return stdout, stderr

class ScriptException(Exception):
    def __init__(self, returncode, stdout, stderr, script):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        self.script = script
        super(ScriptException, self).__init__('Error in script')

stdout, stderr = run_script('ls /tmp')
print('stdout')
print(stdout)
print('stderr')
print(stderr)
