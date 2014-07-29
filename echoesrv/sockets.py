from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace


@namespace('/echo')
class EchoNamespace(BaseNamespace):
    def on_msg(self, msg):
        pkt = dict(type='event',
                   name='msg',
                   args='Someone said: {0}'.format(msg),
                   endpoint=self.ns_name)

        for sessid, socket in self.socket.server.sockets.iteritems():
            socket.send_packet(pkt)
