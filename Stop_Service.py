import subprocess
import os

# stop running services
args = ['sc', 'stop', 'cplspcon']
result = subprocess.run(args)
args[2] = 'cphs'
result = subprocess.run(args)
args[2] = 'jhi_service'
result = subprocess.run(args)
args[2] = 'esifsvc'
result = subprocess.run(args)
args[2] = 'LMS'
result = subprocess.run(args)
args[2] = 'EvtEng'
result = subprocess.run(args)
args[2] = 'RegSrvc'
result = subprocess.run(args)
args[2] = 'ZeroConfigService'
result = subprocess.run(args)
args[2] = 'AESMService'
result = subprocess.run(args)
args[2] = 'MBAMainService'
result = subprocess.run(args)
args[2] = 'ClickToRunSvc'
result = subprocess.run(args)
args[2] = 'AGSService'
result = subprocess.run(args)
args[2] = 'AdobeUpdateService'
result = subprocess.run(args)

# terminate running processes
os.system("TASKKILL /f /PID 10688")  #CreativeCloud.exe
os.system("TASKKILL /f /PID 9276")  #AdobeCreativeCloud.exe
os.system("TASKKILL /f /PID 10508")  #AdobeCEFHelper.exe
os.system("TASKKILL /f /PID 6972")  #AdobeCEFHelper.exe
os.system("TASKKILL /f /PID 13800")  #AdobeIPCbroker.exe
os.system("TASKKILL /f /PID 10748")  #CCXProcess.exe
os.system("TASKKILL /f /PID 8148")  #MBAMessageCenter.exe