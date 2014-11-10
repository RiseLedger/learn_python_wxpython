import wx

# app = wx.App()

# frame = wx.Frame(None, -1, 'Ads Manager')
# frame.Show()
# app.MainLoop()

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(450,350))
        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
