
#def on_message_delete(self, message): pass
#def on_message_edit(self, before, after): pass
#def on_status(self, member): pass

list = [ 
    "on_message;message",
    "on_ready;",

    "on_message_delete;message",
    "on_message_edit;before;after",

    "on_status;member",

    "on_channel_delete;channel",
    "on_channel_create;channel",
    "on_channel_update;channel",

    "on_member_join;member",
    "on_member_remove;member",
    "on_member_update;member",

    "on_server_join;server",
    "on_server_remove;server",

    "on_server_role_create;server;role",
    "on_server_role_delete;server;role",
    "on_server_role_update;role",

    "on_server_available;server",
    "on_server_unavailable;server",

    "on_voice_state_update;member" 
]

def gen_plugin_defs():
    tem = "def %s(self, client%s): pass"
    for l in list:
        a = l.split(";")
        name = a[0]
        args = []
        if len(a) > 1:
            for p in a[1:]:
                if p != "":
                    args.append(p)
        b = ", ".join([x for x in args if x != ""])
        if b != "":
            b = ", " + b
        print(tem % (name, b))

def gen_plugins_binds():
    #tem = "[p.%s(self, %s) for p in Plugin.plugins if hasattr(p, \"%s\")]"
    tem = "for plugin in Plugin.plugins:\n\t\tif hasattr(plugin, \"%s\"):\n\t\t\tplugin.%s(self, %s)"
    fun = "def %s(self, %s):\n\t%s"
    
    for l in list:
        a = l.split(";")
        name = a[0]
        args = [] #["client"]
        if len(a) > 1:
            for p in a[1:]:
                if p != "":
                    args.append(p)
        b = ",".join(args)
        #plugin = (tem % (name, b, name))
        plugin = (tem % (name, name, b))
        
        func = (fun % (name, ", ".join([x for x in args if x != ""]), plugin))
        print(func+"\n")
        
gen_plugin_defs()
gen_plugin_bindings()