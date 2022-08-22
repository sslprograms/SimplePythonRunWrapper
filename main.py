from SimplePythonRun import loadModule

spr = loadModule()

script = "print('hello, world!');"

resp = spr.run(script)
print(resp)
