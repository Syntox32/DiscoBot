#def on_socket_closed(self): pass

#def on_message_delete(self, message): pass
#def on_message_edit(self, before, after): pass
#def on_status(self, member): pass

#def on_channel_delete(self, channel): pass
#def on_channel_create(self, channel): pass
#def on_channel_update(self, channel): pass

#def on_member_join(self, member): pass
#def on_member_remove(self, member): pass
#def on_member_update(self, member): pass

#def on_server_create(self, server): pass
#def on_server_delete(self, server): pass

#def on_server_role_create(self, server, role): pass
#def on_server_role_delete(self, server, role): pass
#def on_server_role_update(self, role): pass

#def on_voice_state_update(self, member): pass

list = [ 
    "on_message; message",
    "on_ready;",
    "on_message_delete; message",
    "on_message_edit; before; after",
    "on_status; member",
    "on_channel_delete; channel",
    "on_channel_create; channel",
    "on_channel_update; channel",
    "on_member_join; member",
    "on_member_remove; member",
    "on_member_update; member",
    "on_server_create; server",
    "on_server_delete; server",
    "on_server_role_create; server; role",
    "on_server_role_delete; server; role",
    "on_server_role_update; role",
    "on_voice_state_update; member" 
]

#tem = "[p.%s(self, %s) for p in Plugin.plugins if hasattr(p, \"%s\")]"
tem = "for plugin in Plugin.plugins:\n\t\tif hasattr(plugin, \"%s\"):\n\t\t\tplugin.%s(self, %s)"
fun = "def %s(self, %s):\n\t%s"

for l in list:
    a = l.split(";")
    name = a[0]
    args = ["client"]
    if len(a) > 1:
        for p in a[1:]:
            if p != "":
                args.append(p)
    b = ",".join(args)
    #plugin = (tem % (name, b, name))
    plugin = (tem % (name, name, b))
    
    func = (fun % (name, ",".join([x for x in args[1:] if x != ""]), plugin))
    print(func+"\n")