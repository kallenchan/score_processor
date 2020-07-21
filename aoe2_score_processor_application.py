import wx, sys
from threading import Thread
import time
import datetime
import numpy as np

#Import Screenshot Application
from screenshot import screenshot_process

class TestThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.dead = False
        self.start()

    def run(self):
        i=0
        application=screenshot_process()
        
        dt_started=datetime.datetime.utcnow()
        while not self.dead and i<20:
            dt_now=datetime.datetime.utcnow()
            time.sleep(2)
            application.capture_screenshot(bbox=(1400,-280,1800,-140))    
            # print(np.round((dt_now-dt_started).total_seconds(),0))
            # print("{} Screenshot NUmber:{}".format(now.strftime("%H:%M:%S"),i))
            i+=1
        print ("Aborted")

class mywxframe(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self,None)
        pnl = wx.Panel(self)
        szr = wx.BoxSizer(wx.VERTICAL)
        pnl.SetSizer(szr)
        szr2 = self.sizer2(pnl)
        szr.Add(szr2, 1, wx.ALL|wx.EXPAND, 10)
        log = wx.TextCtrl(pnl, -1, style= wx.TE_MULTILINE, size = (300, -1))
        szr.Add(log, 0, wx.ALL, 10)
        btn3 = wx.Button(pnl, -1, "Stop")
        btn3.Bind(wx.EVT_BUTTON, self.OnStop)
        szr.Add(btn3, 0, wx.ALL, 10)
        self.CreateStatusBar()

        redir = RedirectText(log)
        #sys.stdout=redir

        szr.Fit(self)
        self.Show()

    def sizer2(self, panel):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.tc2 = wx.TextCtrl(panel, -1, 'Set Range', size = (100, -1))
        btn2 = wx.Button(panel, -1, "OK",)
        self.Bind(wx.EVT_BUTTON, self.OnStart, btn2)
        sizer.Add(self.tc2, 0, wx.ALL, 10)
        sizer.Add(btn2, 0, wx.ALL, 10)
        return sizer


    def OnStart(self, event):
        self.our_thread = TestThread()

    def OnStop(self, event):
        self.our_thread.dead = True


class RedirectText(object):
    def __init__(self, aWxTextCtrl):
        self.out=aWxTextCtrl

    def write(self, string):
        wx.CallAfter(self.out.WriteText, string)

app = wx.App()
frm = mywxframe()
app.MainLoop()