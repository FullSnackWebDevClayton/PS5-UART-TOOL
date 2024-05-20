# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# This file is generated by wxPython's PI generator.  Do not edit by hand.
#
# The *.pyi files are used by PyCharm and other development tools to provide
# more information, such as PEP 484 type hints, than it is able to glean from
# introspection of extension types and methods.  They are not intended to be
# imported, executed or used for any other purpose other than providing info
# to the tools. If you don't use use a tool that makes use of .pyi files then
# you can safely ignore this file.
#
# See: https://www.python.org/dev/peps/pep-0484/
#      https://www.jetbrains.com/help/pycharm/2016.1/type-hinting-in-pycharm.html
#
# Copyright: (c) 2020 by Total Control Software
# License:   wxWindows License
#---------------------------------------------------------------------------


"""
The classes in this module enable loading widgets and layout from XML.
"""
#-- begin-_xrc --#
import wx.xml

import wx
ID_NONE = wx.ID_NONE  # Needed for some parameter defaults in this module
XRC_USE_LOCALE = 0
XRC_NO_SUBCLASSING = 0
XRC_NO_RELOADING = 0
XRC_USE_ENVVARS = 0

class XmlResource(Object):
    """
    XmlResource(filemask, flags=XRC_USE_LOCALE, domain=wx.EmptyString)
    XmlResource(flags=XRC_USE_LOCALE, domain=wx.EmptyString)
    
    This is the main class for interacting with the XML-based resource
    system.
    """

    def __init__(self, *args, **kw):
        """
        XmlResource(filemask, flags=XRC_USE_LOCALE, domain=wx.EmptyString)
        XmlResource(flags=XRC_USE_LOCALE, domain=wx.EmptyString)
        
        This is the main class for interacting with the XML-based resource
        system.
        """

    def LoadMenuBar(self, *args, **kw):
        """
        LoadMenuBar(parent, name) -> MenuBar
        LoadMenuBar(name) -> MenuBar
        
        Loads a menubar from resource.
        """

    def LoadObject(self, *args, **kw):
        """
        LoadObject(parent, name, classname) -> Object
        LoadObject(instance, parent, name, classname) -> bool
        
        Load an object from the resource specifying both the resource name and
        the class name.
        """

    def LoadObjectRecursively(self, *args, **kw):
        """
        LoadObjectRecursively(parent, name, classname) -> Object
        LoadObjectRecursively(instance, parent, name, classname) -> bool
        
        Load an object from anywhere in the resource tree.
        """

    def AddHandler(self, handler):
        """
        AddHandler(handler)
        
        Initializes only a specific handler (or custom handler).
        """

    def InsertHandler(self, handler):
        """
        InsertHandler(handler)
        
        Add a new handler at the beginning of the handler list.
        """

    def AttachUnknownControl(self, name, control, parent=None):
        """
        AttachUnknownControl(name, control, parent=None) -> bool
        
        Attaches an unknown control to the given panel/window/dialog.
        """

    def ClearHandlers(self):
        """
        ClearHandlers()
        
        Removes all handlers and deletes them (this means that any handlers
        added using AddHandler() must be allocated on the heap).
        """

    def CompareVersion(self, major, minor, release, revision):
        """
        CompareVersion(major, minor, release, revision) -> int
        
        Compares the XRC version to the argument.
        """

    def GetDomain(self):
        """
        GetDomain() -> String
        
        Returns the domain (message catalog) that will be used to load
        translatable strings in the XRC.
        """

    def GetFlags(self):
        """
        GetFlags() -> int
        
        Returns flags, which may be a bitlist of wxXmlResourceFlags
        enumeration values.
        """

    def GetResourceNode(self, name):
        """
        GetResourceNode(name) -> XmlNode
        
        Returns the wxXmlNode containing the definition of the object with the
        given name or NULL.
        """

    def GetVersion(self):
        """
        GetVersion() -> long
        
        Returns version information (a.b.c.d = d + 256*c + 2562*b + 2563*a).
        """

    def InitAllHandlers(self):
        """
        InitAllHandlers()
        
        Initializes handlers for all supported controls/windows.
        """

    def Load(self, filemask):
        """
        Load(filemask) -> bool
        
        Loads resources from XML files that match given filemask.
        """

    def LoadDocument(self, doc, name=""):
        """
        LoadDocument(doc, name="") -> bool
        
        Load resources from the XML document containing them.
        """

    def LoadFile(self, file):
        """
        LoadFile(file) -> bool
        
        Simpler form of Load() for loading a single XRC file.
        """

    def LoadAllFiles(self, dirname):
        """
        LoadAllFiles(dirname) -> bool
        
        Loads all .xrc files from directory dirname.
        """

    def LoadBitmap(self, name):
        """
        LoadBitmap(name) -> Bitmap
        
        Loads a bitmap resource from a file.
        """

    def LoadDialog(self, *args, **kw):
        """
        LoadDialog(parent, name) -> Dialog
        LoadDialog(dlg, parent, name) -> bool
        
        Loads a dialog.
        """

    def LoadFrame(self, *args, **kw):
        """
        LoadFrame(parent, name) -> Frame
        LoadFrame(frame, parent, name) -> bool
        
        Loads a frame from the resource.
        """

    def LoadIcon(self, name):
        """
        LoadIcon(name) -> Icon
        
        Loads an icon resource from a file.
        """

    def LoadMenu(self, name):
        """
        LoadMenu(name) -> Menu
        
        Loads menu from resource.
        """

    def LoadPanel(self, *args, **kw):
        """
        LoadPanel(parent, name) -> Panel
        LoadPanel(panel, parent, name) -> bool
        
        Loads a panel.
        """

    def LoadToolBar(self, parent, name):
        """
        LoadToolBar(parent, name) -> ToolBar
        
        Loads a toolbar.
        """

    def SetDomain(self, domain):
        """
        SetDomain(domain)
        
        Sets the domain (message catalog) that will be used to load
        translatable strings in the XRC.
        """

    def SetFlags(self, flags):
        """
        SetFlags(flags)
        
        Sets flags (bitlist of wxXmlResourceFlags enumeration values).
        """

    def Unload(self, filename):
        """
        Unload(filename) -> bool
        
        This function unloads a resource previously loaded by Load().
        """

    @staticmethod
    def AddSubclassFactory(factory):
        """
        AddSubclassFactory(factory)
        
        Registers subclasses factory for use in XRC.
        """

    @staticmethod
    def FindXRCIDById(numId):
        """
        FindXRCIDById(numId) -> String
        
        Returns a string ID corresponding to the given numeric ID.
        """

    @staticmethod
    def Get():
        """
        Get() -> XmlResource
        
        Gets the global resources object or creates one if none exists.
        """

    @staticmethod
    def GetXRCID(str_id, value_if_not_found=ID_NONE):
        """
        GetXRCID(str_id, value_if_not_found=ID_NONE) -> int
        
        Returns a numeric ID that is equivalent to the string ID used in an
        XML resource.
        """

    @staticmethod
    def Set(res):
        """
        Set(res) -> XmlResource
        
        Sets the global resources object and returns a pointer to the previous
        one (may be NULL).
        """

    def LoadFromBuffer(self, data):
        """
        LoadFromBuffer(data) -> bool
        
        Load the resource from a bytes string or other data buffer compatible
        object.
        """

    LoadFromString = wx.deprecated(LoadFromBuffer, 'Use LoadFromBuffer instead')
    Domain = property(None, None)
    Flags = property(None, None)
    Version = property(None, None)
# end of class XmlResource


class XmlResourceHandler(Object):
    """
    XmlResourceHandler()
    
    wxSizerXmlHandler is a class for resource handlers capable of creating
    a wxSizer object from an XML node.
    """

    def __init__(self):
        """
        XmlResourceHandler()
        
        wxSizerXmlHandler is a class for resource handlers capable of creating
        a wxSizer object from an XML node.
        """

    def CreateResource(self, node, parent, instance):
        """
        CreateResource(node, parent, instance) -> Object
        
        Creates an object (menu, dialog, control, ...) from an XML node.
        """

    def DoCreateResource(self):
        """
        DoCreateResource() -> Object
        
        Called from CreateResource after variables were filled.
        """

    def CanHandle(self, node):
        """
        CanHandle(node) -> bool
        
        Returns true if it understands this node and can create a resource
        from it, false otherwise.
        """

    def SetParentResource(self, res):
        """
        SetParentResource(res)
        
        Sets the parent resource.
        """
    Animation = property(None, None)
    Bitmap = property(None, None)
    BitmapBundle = property(None, None)
    Class = property(None, None)
    CurFileSystem = property(None, None)
    Font = property(None, None)
    ID = property(None, None)
    Icon = property(None, None)
    ImageList = property(None, None)
    Instance = property(None, None)
    Name = property(None, None)
    Node = property(None, None)
    Parent = property(None, None)
    ParentAsWindow = property(None, None)
    Position = property(None, None)
    Resource = property(None, None)
    Size = property(None, None)
    Style = property(None, None)

    def AddStyle(self, name, value):
        """
        AddStyle(name, value)
        
        Add a style flag (e.g.
        """

    def AddWindowStyles(self):
        """
        AddWindowStyles()
        
        Add styles common to all wxWindow-derived classes.
        """

    def CreateChildren(self, parent, this_hnd_only=False):
        """
        CreateChildren(parent, this_hnd_only=False)
        
        Creates children.
        """

    def CreateChildrenPrivately(self, parent, rootnode=None):
        """
        CreateChildrenPrivately(parent, rootnode=None)
        
        Helper function.
        """

    def CreateResFromNode(self, node, parent, instance=None):
        """
        CreateResFromNode(node, parent, instance=None) -> Object
        
        Creates a resource from a node.
        """

    def GetAnimation(self, param="animation", ctrl=None):
        """
        GetAnimation(param="animation", ctrl=None) -> Animation
        
        Creates an animation (see wxAnimation) from the filename specified in
        param.
        """

    def GetBitmap(self, *args, **kw):
        """
        GetBitmap(param="bitmap", defaultArtClient=ART_OTHER, size=DefaultSize) -> Bitmap
        GetBitmap(node, defaultArtClient=ART_OTHER, size=DefaultSize) -> Bitmap
        
        Gets a bitmap.
        """

    def GetBitmapBundle(self, *args, **kw):
        """
        GetBitmapBundle(param="bitmap", defaultArtClient=ART_OTHER, size=DefaultSize) -> BitmapBundle
        GetBitmapBundle(node, defaultArtClient=ART_OTHER, size=DefaultSize) -> BitmapBundle
        
        Gets a bitmap bundle.
        """

    def GetBool(self, param, defaultv=False):
        """
        GetBool(param, defaultv=False) -> bool
        
        Gets a bool flag (1, t, yes, on, true are true, everything else is
        false).
        """

    def GetColour(self, param, defaultColour=NullColour):
        """
        GetColour(param, defaultColour=NullColour) -> Colour
        
        Gets colour in HTML syntax (#RRGGBB).
        """

    def GetCurFileSystem(self):
        """
        GetCurFileSystem() -> FileSystem
        
        Returns the current file system.
        """

    def GetDimension(self, param, defaultv=0, windowToUse=0):
        """
        GetDimension(param, defaultv=0, windowToUse=0) -> Coord
        
        Gets a dimension (may be in dialog units).
        """

    def GetDirection(self, param, dirDefault=LEFT):
        """
        GetDirection(param, dirDefault=LEFT) -> Direction
        
        Gets a direction.
        """

    def GetFont(self, param="font"):
        """
        GetFont(param="font") -> Font
        
        Gets a font.
        """

    def GetID(self):
        """
        GetID() -> int
        
        Returns the XRCID.
        """

    def GetIcon(self, *args, **kw):
        """
        GetIcon(param="icon", defaultArtClient=ART_OTHER, size=DefaultSize) -> Icon
        GetIcon(node, defaultArtClient=ART_OTHER, size=DefaultSize) -> Icon
        
        Returns an icon.
        """

    def GetIconBundle(self, param, defaultArtClient=ART_OTHER):
        """
        GetIconBundle(param, defaultArtClient=ART_OTHER) -> IconBundle
        
        Returns an icon bundle.
        """

    def GetImageList(self, param="imagelist"):
        """
        GetImageList(param="imagelist") -> ImageList
        
        Creates an image list from the param markup data.
        """

    def GetLong(self, param, defaultv=0):
        """
        GetLong(param, defaultv=0) -> long
        
        Gets the integer value from the parameter.
        """

    def GetFloat(self, param, defaultv=0):
        """
        GetFloat(param, defaultv=0) -> float
        
        Gets a float value from the parameter.
        """

    def GetName(self):
        """
        GetName() -> String
        
        Returns the resource name.
        """

    def IsObjectNode(self, node):
        """
        IsObjectNode(node) -> bool
        
        Checks if the given node is an object node.
        """

    def GetNodeContent(self, node):
        """
        GetNodeContent(node) -> String
        
        Gets node content from wxXML_ENTITY_NODE.
        """

    def GetNodeParent(self, node):
        """
        GetNodeParent(node) -> XmlNode
        
        Gets the parent of the node given.
        """

    def GetNodeNext(self, node):
        """
        GetNodeNext(node) -> XmlNode
        
        Gets the next sibling node related to the given node, possibly NULL.
        """

    def GetNodeChildren(self, node):
        """
        GetNodeChildren(node) -> XmlNode
        
        Gets the first child of the given node or NULL.
        """

    def GetParamNode(self, param):
        """
        GetParamNode(param) -> XmlNode
        
        Finds the node or returns NULL.
        """

    def GetParamValue(self, *args, **kw):
        """
        GetParamValue(param) -> String
        GetParamValue(node) -> String
        
        Finds the parameter value or returns the empty string.
        """

    def GetPosition(self, param="pos"):
        """
        GetPosition(param="pos") -> Point
        
        Gets the position (may be in dialog units).
        """

    def GetSize(self, param="size", windowToUse=0):
        """
        GetSize(param="size", windowToUse=0) -> Size
        
        Gets the size (may be in dialog units).
        """

    def GetStyle(self, param="style", defaults=0):
        """
        GetStyle(param="style", defaults=0) -> int
        
        Gets style flags from text in form "flag | flag2| flag3 |..." Only
        understands flags added with AddStyle().
        """

    def GetText(self, param, translate=True):
        """
        GetText(param, translate=True) -> String
        
        Gets text from param and does some conversions:
        """

    def HasParam(self, param):
        """
        HasParam(param) -> bool
        
        Check to see if a parameter exists.
        """

    def IsOfClass(self, node, classname):
        """
        IsOfClass(node, classname) -> bool
        
        Convenience function.
        """

    def SetupWindow(self, wnd):
        """
        SetupWindow(wnd)
        
        Sets common window options.
        """

    def ReportError(self, *args, **kw):
        """
        ReportError(context, message)
        ReportError(message)
        
        Reports error in XRC resources to the user.
        """

    def ReportParamError(self, param, message):
        """
        ReportParamError(param, message)
        
        Like ReportError(wxXmlNode*, const wxString&), but uses the node of
        parameter param of the currently processed object as the context.
        """

    def GetResource(self):
        """
        GetResource() -> XmlResource
        
        After CreateResource has been called this will return the current
        wxXmlResource object.
        """

    def GetNode(self):
        """
        GetNode() -> XmlNode
        
        After CreateResource has been called this will return the XML node
        being processed.
        """

    def GetClass(self):
        """
        GetClass() -> String
        
        After CreateResource has been called this will return the class name
        of the XML resource node being processed.
        """

    def GetParent(self):
        """
        GetParent() -> Object
        
        After CreateResource has been called this will return the current
        item's parent, if any.
        """

    def GetInstance(self):
        """
        GetInstance() -> Object
        
        After CreateResource has been called this will return the instance
        that the XML resource content should be created upon, if it has
        already been created.
        """

    def GetParentAsWindow(self):
        """
        GetParentAsWindow() -> Window
        
        After CreateResource has been called this will return the item's
        parent as a wxWindow.
        """
# end of class XmlResourceHandler


@wx.deprecated
def EmptyXmlResource(flags=XRC_USE_LOCALE, domain=""):
    """
    A compatibility wrapper for the XmlResource(flags, domain) constructor
    """
    pass

def XRCID(str_id, value_if_not_found=wx.ID_NONE):
    """
    Returns a numeric ID that is equivalent to the string ID used in an XML resource.
    """
    pass

def XRCCTRL(window, str_id, *ignoreargs):
    """
    Returns the child window associated with the string ID in an XML resource.
    """
    pass

class XmlSubclassFactory(object):
    """
    XmlSubclassFactory()
    """

    def __init__(self):
        """
        XmlSubclassFactory()
        """

    def Create(self, className):
        """
        Create(className) -> Object
        """
# end of class XmlSubclassFactory


# Create a factory for handling the subclass property of XRC's
# object tag.  This factory will search for the specified
# package.module.class and will try to instantiate it for XRC's
# use.  The class must support instantiation with no parameters and
# delayed creation of the UI widget (aka 2-phase create).

def _my_import(name):
    try:
        mod = __import__(name)
    except ImportError:
        import traceback
        print(traceback.format_exc())
        raise
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

class XmlSubclassFactory_Python(XmlSubclassFactory):
    def __init__(self):
        XmlSubclassFactory.__init__(self)

    def Create(self, className):
        assert className.find('.') != -1, "Module name must be specified!"
        mname = className[:className.rfind('.')]
        cname = className[className.rfind('.')+1:]
        module = _my_import(mname)
        klass = getattr(module, cname)
        inst = klass()
        return inst

XmlResource.AddSubclassFactory(XmlSubclassFactory_Python())
#-- end-_xrc --#
