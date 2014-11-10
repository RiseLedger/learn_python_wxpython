import wx
import pprint

# Single Toolbar

# class Example(wx.Frame):
#     def __init__(self, *args, **kwargs):
#         super(Example, self).__init__(*args, **kwargs)
#         self.InitUI()

#     def InitUI(self):
#         toolbar = self.CreateToolBar()
#         qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('images/exit.png'))
#         toolbar.Realize()
#         self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

#         self.SetSize((250, 200))
#         self.SetTitle('Simple toolbar')
#         self.Centre()
#         self.Show(True)

#     def OnQuit(self, e):
#         self.Close()

# def main():
#     ex = wx.App()
#     Example(None)
#     ex.MainLoop()

# if __name__ == '__main__':
#     main()

# Multiple Toolbars

# class Example(wx.Frame):

#     def __init__(self, *args, **kwargs):
#         super(Example, self).__init__(*args, **kwargs)

#         self.InitUI()

#     def InitUI(self):

#         vbox = wx.BoxSizer(wx.VERTICAL)

#         toolbar1 = wx.ToolBar(self)
#         toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('images/database_save.png'))
#         toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('images/folder_magnify.png'))
#         toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('images/drink_empty.png'))
#         toolbar1.Realize()

#         toolbar2 = wx.ToolBar(self)
#         qtool = toolbar2.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('images/cross.png'))
#         toolbar2.Realize()

#         vbox.Add(toolbar1, 0, wx.EXPAND)
#         vbox.Add(toolbar2, 0, wx.EXPAND)

#         self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

#         self.SetSizer(vbox)

#         self.SetSize((300, 250))
#         self.SetTitle('Toolbars')
#         self.Centre()
#         self.Show(True)

#     def OnQuit(self, e):
#         self.Close()

# def main():

#     ex = wx.App()
#     Example(None)
#     ex.MainLoop()


# if __name__ == '__main__':
#     main()

# Toolbar Separator

import wx

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        pprint.pprint(args)
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.count = 5

        self.toolbar = self.CreateToolBar()
        tundo = self.toolbar.AddLabelTool(wx.ID_UNDO, '', wx.Bitmap('images/arrow_undo.png'))
        tredo = self.toolbar.AddLabelTool(wx.ID_REDO, '', wx.Bitmap('images/arrow_redo.png'))
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()
        texit = self.toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('images/cross.png'))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, texit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, tundo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, tredo)

        self.SetSize((250, 200))
        self.SetTitle('Undo redo')
        self.Centre()
        self.Show(True)

    def OnUndo(self, e):
        if self.count > 1 and self.count <= 5:
            self.count = self.count - 1

        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)

        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, e):
        if self.count < 5 and self.count >= 1:
            self.count = self.count + 1

        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)

        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)

    def OnQuit(self, e):
        self.Close()



def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()