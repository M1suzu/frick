def get_script(module, offsets):
    js = 'var module = "' + module + '"'
    js += '''
        var base = 0x0;
        var sleep = false;
        var cContext = null;
        var cOff = 0x0;
        
        function sendContext() {
            var context = {};
            for (var reg in cContext) {
                var what = cContext[reg];
                context[reg] = {
                    'value': what
                };
                try {
                    var rr = Memory.readPointer(what);
                    context[reg]['sub'] = [rr]
                    while(true) {
                        rr = Memory.readPointer(rr);
                        context[reg]['sub'].push(rr);
                    }
                } catch(err) {
                    continue;
                }
            }
            send('2:::' + cOff + ':::' + JSON.stringify(context));
        }
        
        function att(off) {
            if (base == 0) {
                return;
            }
            var pt = base.add(off);
            send('1:::' + pt);
            Interceptor.attach(pt, function() {
                cContext = this.context;
                cOff = off;
                sendContext();
                sleep = true;
                while(sleep) {
                    Thread.sleep(1);
                }
            });
        }
        
        rpc.exports = {
            add: function(what) {
                att(what);
            },
            c: function() {
                sleep = false;
            },
            ivp: function(p) {
                try {
                    var ppt = ptr(p);
                    Memory.readPointer(ppt);
                    return true;
                } catch(err) {
                    return false;
                }
            },
            mr: function(p, l) {
                try {
                    p = ptr(p);
                    send('3:::' + p, Memory.readByteArray(p, l));
                } catch(err) {}
            },
            mrs: function(p, l) {
                try {
                    p = ptr(p);
                    return Memory.readByteArray(p, l);
                } catch(err) {
                    return null;
                }
            },
            mw: function(p, w) {
                try {
                    p = ptr(p);
                    Memory.writeByteArray(p, hexToBytes(w));
                    return p;
                } catch(err) {
                    console.log(err)
                    return null;
                }
            },
            rp: function(p) {
                try {
                    return Memory.readPointer(ptr(p));
                } catch(err) {
                    return null;
                }
            },
            rw: function(r, v) {
                try {
                    console.log(JSON.stringify(cContext));
                    cContext[r] = v;
                    return v;
                } catch(err) {
                    return null;
                }
            },
            sc: function() {
                sendContext();
            }
        };

        function hexToBytes(hex) {
            for (var bytes = [], c = 0; c < hex.length; c += 2)
            bytes.push(parseInt(hex.substr(c, 2), 16));
            return bytes;
        }
        
        setTimeout(function() {
            base = Process.findModuleByName(module).base;
            send('0:::' + base + ':::' + Process.arch);            
    '''
    for k, v in offsets.items():
        js += 'att(' + str(k) + ');'
    js += '}, 250);'
    return js