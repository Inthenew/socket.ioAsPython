from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    def PyJs_LONG_648_(var=var):
        @Js
        def PyJs_anonymous_1_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'r', u'e', u't', u'n'])
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                if var.get(u't'):
                    @Js
                    def PyJs_anonymous_2_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        for PyJsTemp in var.get(u'r').get(u'prototype'):
                            var.put(u'e', PyJsTemp)
                            var.get(u't').put(var.get(u'e'), var.get(u'r').get(u'prototype').get(var.get(u'e')))
                        return var.get(u't')
                    PyJs_anonymous_2_._set_name(u'anonymous')
                    return PyJs_anonymous_2_(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            pass
            def PyJs_LONG_14_(var=var):
                @Js
                def PyJs_anonymous_3_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    PyJs_Object_4_ = Js({})
                    return PyJsComma(PyJsComma(var.get(u"this").put(u'_callbacks', (var.get(u"this").get(u'_callbacks') or PyJs_Object_4_)),var.get(u"this").get(u'_callbacks').put((Js(u'$')+var.get(u't')), (var.get(u"this").get(u'_callbacks').get((Js(u'$')+var.get(u't'))) or Js([]))).callprop(u'push', var.get(u'e'))),var.get(u"this"))
                PyJs_anonymous_3_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_5_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    @Js
                    def PyJsHoisted_n_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        PyJsComma(var.get(u"this").callprop(u'off', var.get(u't'), var.get(u'n')),var.get(u'e').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    PyJsHoisted_n_.func_name = u'n'
                    var.put(u'n', PyJsHoisted_n_)
                    pass
                    return PyJsComma(PyJsComma(var.get(u'n').put(u'fn', var.get(u'e')),var.get(u"this").callprop(u'on', var.get(u't'), var.get(u'n'))),var.get(u"this"))
                PyJs_anonymous_5_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_6_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'o', u'n'])
                    PyJs_Object_7_ = Js({})
                    if PyJsComma(var.get(u"this").put(u'_callbacks', (var.get(u"this").get(u'_callbacks') or PyJs_Object_7_)),(Js(0.0)==var.get(u'arguments').get(u'length'))):
                        PyJs_Object_8_ = Js({})
                        return PyJsComma(var.get(u"this").put(u'_callbacks', PyJs_Object_8_),var.get(u"this"))
                    var.put(u'r', var.get(u"this").get(u'_callbacks').get((Js(u'$')+var.get(u't'))))
                    if var.get(u'r').neg():
                        return var.get(u"this")
                    if (Js(1.0)==var.get(u'arguments').get(u'length')):
                        return PyJsComma(var.get(u"this").get(u'_callbacks').delete((Js(u'$')+var.get(u't'))),var.get(u"this"))
                    #for JS loop
                    var.put(u'o', Js(0.0))
                    while (var.get(u'o')<var.get(u'r').get(u'length')):
                        try:
                            if (PyJsStrictEq(var.put(u'n', var.get(u'r').get(var.get(u'o'))),var.get(u'e')) or PyJsStrictEq(var.get(u'n').get(u'fn'),var.get(u'e'))):
                                var.get(u'r').callprop(u'splice', var.get(u'o'), Js(1.0))
                                break
                        finally:
                                (var.put(u'o',Js(var.get(u'o').to_number())+Js(1))-Js(1))
                    return PyJsComma((PyJsStrictEq(Js(0.0),var.get(u'r').get(u'length')) and var.get(u"this").get(u'_callbacks').delete((Js(u'$')+var.get(u't')))),var.get(u"this"))
                PyJs_anonymous_6_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_9_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'o', u'n'])
                    PyJs_Object_10_ = Js({})
                    var.get(u"this").put(u'_callbacks', (var.get(u"this").get(u'_callbacks') or PyJs_Object_10_))
                    #for JS loop
                    var.put(u'e', var.get(u'Array').create((var.get(u'arguments').get(u'length')-Js(1.0))))
                    var.put(u'n', var.get(u"this").get(u'_callbacks').get((Js(u'$')+var.get(u't'))))
                    var.put(u'r', Js(1.0))
                    while (var.get(u'r')<var.get(u'arguments').get(u'length')):
                        try:
                            var.get(u'e').put((var.get(u'r')-Js(1.0)), var.get(u'arguments').get(var.get(u'r')))
                        finally:
                                (var.put(u'r',Js(var.get(u'r').to_number())+Js(1))-Js(1))
                    if var.get(u'n'):
                        var.put(u'r', Js(0.0))
                        #for JS loop
                        var.put(u'o', var.put(u'n', var.get(u'n').callprop(u'slice', Js(0.0))).get(u'length'))
                        while (var.get(u'r')<var.get(u'o')):
                            try:
                                var.get(u'n').get(var.get(u'r')).callprop(u'apply', var.get(u"this"), var.get(u'e'))
                            finally:
                                    var.put(u'r',Js(var.get(u'r').to_number())+Js(1))
                    return var.get(u"this")
                PyJs_anonymous_9_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_11_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    PyJs_Object_12_ = Js({})
                    return PyJsComma(var.get(u"this").put(u'_callbacks', (var.get(u"this").get(u'_callbacks') or PyJs_Object_12_)),(var.get(u"this").get(u'_callbacks').get((Js(u'$')+var.get(u't'))) or Js([])))
                PyJs_anonymous_11_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_13_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u"this").callprop(u'listeners', var.get(u't')).get(u'length').neg().neg()
                PyJs_anonymous_13_._set_name(u'anonymous')
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u't').put(u'exports', var.get(u'r')),var.get(u'r').get(u'prototype').put(u'on', var.get(u'r').get(u'prototype').put(u'addEventListener', PyJs_anonymous_3_))),var.get(u'r').get(u'prototype').put(u'once', PyJs_anonymous_5_)),var.get(u'r').get(u'prototype').put(u'off', var.get(u'r').get(u'prototype').put(u'removeListener', var.get(u'r').get(u'prototype').put(u'removeAllListeners', var.get(u'r').get(u'prototype').put(u'removeEventListener', PyJs_anonymous_6_))))),var.get(u'r').get(u'prototype').put(u'emit', PyJs_anonymous_9_)),var.get(u'r').get(u'prototype').put(u'listeners', PyJs_anonymous_11_)),var.get(u'r').get(u'prototype').put(u'hasListeners', PyJs_anonymous_13_))
            PyJs_LONG_14_()
        PyJs_anonymous_1_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_15_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'e', u'i', u'o', u'n', u'r', u't'])
            var.put(u'r', var.get(u'n')(Js(23.0)))
            var.put(u'o', var.get(u'n')(Js(24.0)))
            var.put(u'i', var.get(u'String').callprop(u'fromCharCode', Js(30.0)))
            @Js
            def PyJs_anonymous_17_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u's', u'e', u't', u'o', u'n'])
                var.put(u'n', var.get(u't').get(u'length'))
                var.put(u'o', var.get(u'Array').create(var.get(u'n')))
                var.put(u's', Js(0.0))
                @Js
                def PyJs_anonymous_18_(t, c, this, arguments, var=var):
                    var = Scope({u'this':this, u'c':c, u't':t, u'arguments':arguments}, var)
                    var.registers([u'c', u't'])
                    @Js
                    def PyJs_anonymous_19_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        PyJsComma(var.get(u'o').put(var.get(u'c'), var.get(u't')),(PyJsStrictEq(var.put(u's',Js(var.get(u's').to_number())+Js(1)),var.get(u'n')) and var.get(u'e')(var.get(u'o').callprop(u'join', var.get(u'i')))))
                    PyJs_anonymous_19_._set_name(u'anonymous')
                    var.get(u'r')(var.get(u't'), Js(1.0).neg(), PyJs_anonymous_19_)
                PyJs_anonymous_18_._set_name(u'anonymous')
                var.get(u't').callprop(u'forEach', PyJs_anonymous_18_)
            PyJs_anonymous_17_._set_name(u'anonymous')
            @Js
            def PyJs_anonymous_20_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'c', u'e', u'n', u's', u'r', u't'])
                #for JS loop
                var.put(u'n', var.get(u't').callprop(u'split', var.get(u'i')))
                var.put(u'r', Js([]))
                var.put(u's', Js(0.0))
                while (var.get(u's')<var.get(u'n').get(u'length')):
                    try:
                        var.put(u'c', var.get(u'o')(var.get(u'n').get(var.get(u's')), var.get(u'e')))
                        if PyJsComma(var.get(u'r').callprop(u'push', var.get(u'c')),PyJsStrictEq(Js(u'error'),var.get(u'c').get(u'type'))):
                            break
                    finally:
                            (var.put(u's',Js(var.get(u's').to_number())+Js(1))-Js(1))
                return var.get(u'r')
            PyJs_anonymous_20_._set_name(u'anonymous')
            PyJs_Object_16_ = Js({u'protocol':Js(4.0),u'encodePacket':var.get(u'r'),u'encodePayload':PyJs_anonymous_17_,u'decodePacket':var.get(u'o'),u'decodePayload':PyJs_anonymous_20_})
            var.get(u't').put(u'exports', PyJs_Object_16_)
        PyJs_anonymous_15_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_21_(t, e, this, arguments, var=var):
            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
            var.registers([u'e', u't'])
            var.get(u't').put(u'exports', (var.get(u'self') if (Js(u'undefined')!=var.get(u'self',throw=False).typeof()) else (var.get(u'window') if (Js(u'undefined')!=var.get(u'window',throw=False).typeof()) else var.get(u'Function')(Js(u'return this'))())))
        PyJs_anonymous_21_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_22_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'f', u'i', u'o', u'n', u's', u'r', u'u', u't'])
            @Js
            def PyJsHoisted_a_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_30_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_30_._set_name(u'anonymous')
                return var.put(u'a', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_30_))(var.get(u't'))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_29_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                        PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                        raise PyJsTempException
                    return var.get(u't')
                PyJs_anonymous_29_._set_name(u'anonymous')
                return (PyJs_anonymous_29_(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_i_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_25_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_25_._set_name(u'anonymous')
                return var.put(u'i', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_25_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_o_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_s_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_26_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_27_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_27_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_27_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_8957791 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_8957791 is not None:
                                var.own[u't'] = PyJsHolder_74_8957791
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_8957791
                PyJs_anonymous_26_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_26_())
                @Js
                def PyJs_anonymous_28_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'a')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'a')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'c')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_28_._set_name(u'anonymous')
                return PyJs_anonymous_28_
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_23_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_23_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_24_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_24_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_23_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_24_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            pass
            pass
            pass
            pass
            pass
            pass
            var.put(u'u', var.get(u'n')(Js(1.0)))
            @Js
            def PyJs_anonymous_31_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'c', u'e', u'n', u'r', u't'])
                @Js
                def PyJsHoisted_a_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    pass
                    @Js
                    def PyJs_anonymous_35_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        if var.get(u't').instanceof(var.get(u'e')).neg():
                            PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                            raise PyJsTempException
                    PyJs_anonymous_35_._set_name(u'anonymous')
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJs_anonymous_35_(var.get(u"this"), var.get(u'a')),var.put(u'e', var.get(u'c').callprop(u'call', var.get(u"this"))).put(u'opts', var.get(u't'))),var.get(u'e').put(u'query', var.get(u't').get(u'query'))),var.get(u'e').put(u'readyState', Js(u''))),var.get(u'e').put(u'socket', var.get(u't').get(u'socket'))),var.get(u'e'))
                PyJsHoisted_a_.func_name = u'a'
                var.put(u'a', PyJsHoisted_a_)
                @Js
                def PyJs_anonymous_32_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                        PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                        raise PyJsTempException
                    PyJs_Object_34_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                    PyJs_Object_33_ = Js({u'constructor':PyJs_Object_34_})
                    PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_33_)),(var.get(u'e') and var.get(u'i')(var.get(u't'), var.get(u'e'))))
                PyJs_anonymous_32_._set_name(u'anonymous')
                PyJs_anonymous_32_(var.get(u'a'), var.get(u't')).neg()
                var.put(u'c', var.get(u's')(var.get(u'a')))
                pass
                @Js
                def PyJs_anonymous_37_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    var.put(u'n', var.get(u'Error').create(var.get(u't')))
                    return PyJsComma(PyJsComma(PyJsComma(var.get(u'n').put(u'type', Js(u'TransportError')),var.get(u'n').put(u'description', var.get(u'e'))),var.get(u"this").callprop(u'emit', Js(u'error'), var.get(u'n'))),var.get(u"this"))
                PyJs_anonymous_37_._set_name(u'anonymous')
                PyJs_Object_36_ = Js({u'key':Js(u'onError'),u'value':PyJs_anonymous_37_})
                @Js
                def PyJs_anonymous_39_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return PyJsComma(((PyJsStrictNeq(Js(u'closed'),var.get(u"this").get(u'readyState')) and PyJsStrictNeq(Js(u''),var.get(u"this").get(u'readyState'))) or PyJsComma(var.get(u"this").put(u'readyState', Js(u'opening')),var.get(u"this").callprop(u'doOpen'))),var.get(u"this"))
                PyJs_anonymous_39_._set_name(u'anonymous')
                PyJs_Object_38_ = Js({u'key':Js(u'open'),u'value':PyJs_anonymous_39_})
                @Js
                def PyJs_anonymous_41_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return PyJsComma(((PyJsStrictNeq(Js(u'opening'),var.get(u"this").get(u'readyState')) and PyJsStrictNeq(Js(u'open'),var.get(u"this").get(u'readyState'))) or PyJsComma(var.get(u"this").callprop(u'doClose'),var.get(u"this").callprop(u'onClose'))),var.get(u"this"))
                PyJs_anonymous_41_._set_name(u'anonymous')
                PyJs_Object_40_ = Js({u'key':Js(u'close'),u'value':PyJs_anonymous_41_})
                @Js
                def PyJs_anonymous_43_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictNeq(Js(u'open'),var.get(u"this").get(u'readyState')):
                        PyJsTempException = JsToPyException(var.get(u'Error').create(Js(u'Transport not open')))
                        raise PyJsTempException
                    var.get(u"this").callprop(u'write', var.get(u't'))
                PyJs_anonymous_43_._set_name(u'anonymous')
                PyJs_Object_42_ = Js({u'key':Js(u'send'),u'value':PyJs_anonymous_43_})
                @Js
                def PyJs_anonymous_45_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    PyJsComma(PyJsComma(var.get(u"this").put(u'readyState', Js(u'open')),var.get(u"this").put(u'writable', Js(0.0).neg())),var.get(u"this").callprop(u'emit', Js(u'open')))
                PyJs_anonymous_45_._set_name(u'anonymous')
                PyJs_Object_44_ = Js({u'key':Js(u'onOpen'),u'value':PyJs_anonymous_45_})
                @Js
                def PyJs_anonymous_47_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    var.put(u'e', var.get(u'u').callprop(u'decodePacket', var.get(u't'), var.get(u"this").get(u'socket').get(u'binaryType')))
                    var.get(u"this").callprop(u'onPacket', var.get(u'e'))
                PyJs_anonymous_47_._set_name(u'anonymous')
                PyJs_Object_46_ = Js({u'key':Js(u'onData'),u'value':PyJs_anonymous_47_})
                @Js
                def PyJs_anonymous_49_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    var.get(u"this").callprop(u'emit', Js(u'packet'), var.get(u't'))
                PyJs_anonymous_49_._set_name(u'anonymous')
                PyJs_Object_48_ = Js({u'key':Js(u'onPacket'),u'value':PyJs_anonymous_49_})
                @Js
                def PyJs_anonymous_51_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    PyJsComma(var.get(u"this").put(u'readyState', Js(u'closed')),var.get(u"this").callprop(u'emit', Js(u'close')))
                PyJs_anonymous_51_._set_name(u'anonymous')
                PyJs_Object_50_ = Js({u'key':Js(u'onClose'),u'value':PyJs_anonymous_51_})
                return PyJsComma(PyJsComma(PyJsComma(var.put(u'e', var.get(u'a')),(var.put(u'n', Js([PyJs_Object_36_, PyJs_Object_38_, PyJs_Object_40_, PyJs_Object_42_, PyJs_Object_44_, PyJs_Object_46_, PyJs_Object_48_, PyJs_Object_50_])) and var.get(u'o')(var.get(u'e').get(u'prototype'), var.get(u'n')))),(var.get(u'r') and var.get(u'o')(var.get(u'e'), var.get(u'r')))),var.get(u'a'))
            PyJs_anonymous_31_._set_name(u'anonymous')
            var.put(u'f', PyJs_anonymous_31_(var.get(u'n')(Js(0.0))))
            var.get(u't').put(u'exports', var.get(u'f'))
        PyJs_anonymous_22_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_52_(t, e, this, arguments, var=var):
            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
            var.registers([u'e', u't'])
            @Js
            def PyJs_anonymous_53_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't', u'n'])
                var.put(u'e', Js(u''))
                for PyJsTemp in var.get(u't'):
                    var.put(u'n', PyJsTemp)
                    (var.get(u't').callprop(u'hasOwnProperty', var.get(u'n')) and PyJsComma((var.get(u'e').get(u'length') and var.put(u'e', Js(u'&'), u'+')),var.put(u'e', ((var.get(u'encodeURIComponent')(var.get(u'n'))+Js(u'='))+var.get(u'encodeURIComponent')(var.get(u't').get(var.get(u'n')))), u'+')))
                return var.get(u'e')
            PyJs_anonymous_53_._set_name(u'anonymous')
            @Js
            def PyJs_anonymous_54_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u'i', u'o', u'n', u'r', u't'])
                #for JS loop
                PyJs_Object_55_ = Js({})
                var.put(u'e', PyJs_Object_55_)
                var.put(u'n', var.get(u't').callprop(u'split', Js(u'&')))
                var.put(u'r', Js(0.0))
                var.put(u'o', var.get(u'n').get(u'length'))
                while (var.get(u'r')<var.get(u'o')):
                    try:
                        var.put(u'i', var.get(u'n').get(var.get(u'r')).callprop(u'split', Js(u'=')))
                        var.get(u'e').put(var.get(u'decodeURIComponent')(var.get(u'i').get(u'0')), var.get(u'decodeURIComponent')(var.get(u'i').get(u'1')))
                    finally:
                            (var.put(u'r',Js(var.get(u'r').to_number())+Js(1))-Js(1))
                return var.get(u'e')
            PyJs_anonymous_54_._set_name(u'anonymous')
            PyJsComma(var.get(u'e').put(u'encode', PyJs_anonymous_53_),var.get(u'e').put(u'decode', PyJs_anonymous_54_))
        PyJs_anonymous_52_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_56_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'b', u'e', u'd', u'f', u'i', u'h', u'm', u'l', u'o', u'n', u'p', u's', u'r', u'u', u't', u'v', u'y'])
            @Js
            def PyJsHoisted_a_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_66_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_66_._set_name(u'anonymous')
                return var.put(u'a', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_66_))(var.get(u't'))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_65_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                        PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                        raise PyJsTempException
                    return var.get(u't')
                PyJs_anonymous_65_._set_name(u'anonymous')
                return (PyJs_anonymous_65_(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_f_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_f_.func_name = u'f'
            var.put(u'f', PyJsHoisted_f_)
            @Js
            def PyJsHoisted_i_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_61_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_61_._set_name(u'anonymous')
                return var.put(u'i', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_61_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_o_(t, e, n, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                var.registers([u'e', u't', u'n'])
                @Js
                def PyJs_anonymous_59_(t, e, n, this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                    var.registers([u'r', u'e', u't', u'o', u'n'])
                    @Js
                    def PyJs_anonymous_60_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        #for JS loop
                        
                        while (var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u't'), var.get(u'e')).neg() and PyJsStrictNeq(var.get(u"null"),var.put(u't', var.get(u'a')(var.get(u't'))))):
                            pass
                        
                        return var.get(u't')
                    PyJs_anonymous_60_._set_name(u'anonymous')
                    var.put(u'r', PyJs_anonymous_60_(var.get(u't'), var.get(u'e')))
                    if var.get(u'r'):
                        var.put(u'o', var.get(u'Object').callprop(u'getOwnPropertyDescriptor', var.get(u'r'), var.get(u'e')))
                        return (var.get(u'o').get(u'get').callprop(u'call', var.get(u'n')) if var.get(u'o').get(u'get') else var.get(u'o').get(u'value'))
                PyJs_anonymous_59_._set_name(u'anonymous')
                return var.put(u'o', (var.get(u'Reflect').get(u'get') if ((Js(u'undefined')!=var.get(u'Reflect',throw=False).typeof()) and var.get(u'Reflect').get(u'get')) else PyJs_anonymous_59_))(var.get(u't'), var.get(u'e'), (var.get(u'n') or var.get(u't')))
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_p_(t, e, n, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                var.registers([u'e', u't', u'n'])
                return PyJsComma(PyJsComma((var.get(u'e') and var.get(u'f')(var.get(u't').get(u'prototype'), var.get(u'e'))),(var.get(u'n') and var.get(u'f')(var.get(u't'), var.get(u'n')))),var.get(u't'))
            PyJsHoisted_p_.func_name = u'p'
            var.put(u'p', PyJsHoisted_p_)
            @Js
            def PyJsHoisted_s_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_62_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_63_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_63_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_63_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_95543582 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_95543582 is not None:
                                var.own[u't'] = PyJsHolder_74_95543582
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_95543582
                PyJs_anonymous_62_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_62_())
                @Js
                def PyJs_anonymous_64_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'a')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'a')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'c')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_64_._set_name(u'anonymous')
                return PyJs_anonymous_64_
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_57_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_57_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_58_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_58_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_57_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_58_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            @Js
            def PyJsHoisted_u_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                if var.get(u't').instanceof(var.get(u'e')).neg():
                    PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                    raise PyJsTempException
            PyJsHoisted_u_.func_name = u'u'
            var.put(u'u', PyJsHoisted_u_)
            Js(u'use strict')
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            PyJs_Object_67_ = Js({u'value':Js(0.0).neg()})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'__esModule'), PyJs_Object_67_),var.get(u'e').put(u'Decoder', var.get(u'e').put(u'Encoder', var.get(u'e').put(u'PacketType', var.get(u'e').put(u'protocol', PyJsComma(Js(0.0), Js(None)))))))
            var.put(u'h', var.get(u'n')(Js(0.0)))
            var.put(u'y', var.get(u'n')(Js(29.0)))
            var.put(u'd', var.get(u'n')(Js(15.0)))
            PyJs_Object_68_ = Js({})
            @Js
            def PyJs_anonymous_69_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                def PyJs_LONG_70_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u't').put(var.get(u't').put(u'CONNECT', Js(0.0)), Js(u'CONNECT')),var.get(u't').put(var.get(u't').put(u'DISCONNECT', Js(1.0)), Js(u'DISCONNECT'))),var.get(u't').put(var.get(u't').put(u'EVENT', Js(2.0)), Js(u'EVENT'))),var.get(u't').put(var.get(u't').put(u'ACK', Js(3.0)), Js(u'ACK'))),var.get(u't').put(var.get(u't').put(u'CONNECT_ERROR', Js(4.0)), Js(u'CONNECT_ERROR'))),var.get(u't').put(var.get(u't').put(u'BINARY_EVENT', Js(5.0)), Js(u'BINARY_EVENT'))),var.get(u't').put(var.get(u't').put(u'BINARY_ACK', Js(6.0)), Js(u'BINARY_ACK')))
                PyJs_LONG_70_()
            PyJs_anonymous_69_._set_name(u'anonymous')
            PyJsComma(var.get(u'e').put(u'protocol', Js(5.0)),PyJs_anonymous_69_(var.put(u'l', (var.get(u'e').get(u'PacketType') or var.get(u'e').put(u'PacketType', PyJs_Object_68_)))))
            @Js
            def PyJs_anonymous_71_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJsHoisted_t_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    var.get(u'u')(var.get(u"this"), var.get(u't'))
                PyJsHoisted_t_.func_name = u't'
                var.put(u't', PyJsHoisted_t_)
                pass
                @Js
                def PyJs_anonymous_73_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    def PyJs_LONG_74_(var=var):
                        return (Js([var.get(u"this").callprop(u'encodeAsString', var.get(u't'))]) if ((PyJsStrictNeq(var.get(u't').get(u'type'),var.get(u'l').get(u'EVENT')) and PyJsStrictNeq(var.get(u't').get(u'type'),var.get(u'l').get(u'ACK'))) or var.get(u'd').callprop(u'hasBinary', var.get(u't')).neg()) else PyJsComma(var.get(u't').put(u'type', (var.get(u'l').get(u'BINARY_EVENT') if PyJsStrictEq(var.get(u't').get(u'type'),var.get(u'l').get(u'EVENT')) else var.get(u'l').get(u'BINARY_ACK'))),var.get(u"this").callprop(u'encodeAsBinary', var.get(u't'))))
                    return PyJs_LONG_74_()
                PyJs_anonymous_73_._set_name(u'anonymous')
                PyJs_Object_72_ = Js({u'key':Js(u'encode'),u'value':PyJs_anonymous_73_})
                @Js
                def PyJs_anonymous_76_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    var.put(u'e', (Js(u'')+var.get(u't').get(u'type')))
                    def PyJs_LONG_77_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(((PyJsStrictNeq(var.get(u't').get(u'type'),var.get(u'l').get(u'BINARY_EVENT')) and PyJsStrictNeq(var.get(u't').get(u'type'),var.get(u'l').get(u'BINARY_ACK'))) or var.put(u'e', (var.get(u't').get(u'attachments')+Js(u'-')), u'+')),((var.get(u't').get(u'nsp') and PyJsStrictNeq(Js(u'/'),var.get(u't').get(u'nsp'))) and var.put(u'e', (var.get(u't').get(u'nsp')+Js(u',')), u'+'))),((var.get(u"null")!=var.get(u't').get(u'id')) and var.put(u'e', var.get(u't').get(u'id'), u'+'))),((var.get(u"null")!=var.get(u't').get(u'data')) and var.put(u'e', var.get(u'JSON').callprop(u'stringify', var.get(u't').get(u'data')), u'+'))),var.get(u'e'))
                    return PyJs_LONG_77_()
                PyJs_anonymous_76_._set_name(u'anonymous')
                PyJs_Object_75_ = Js({u'key':Js(u'encodeAsString'),u'value':PyJs_anonymous_76_})
                @Js
                def PyJs_anonymous_79_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'n'])
                    var.put(u'e', var.get(u'y').callprop(u'deconstructPacket', var.get(u't')))
                    var.put(u'n', var.get(u"this").callprop(u'encodeAsString', var.get(u'e').get(u'packet')))
                    var.put(u'r', var.get(u'e').get(u'buffers'))
                    return PyJsComma(var.get(u'r').callprop(u'unshift', var.get(u'n')),var.get(u'r'))
                PyJs_anonymous_79_._set_name(u'anonymous')
                PyJs_Object_78_ = Js({u'key':Js(u'encodeAsBinary'),u'value':PyJs_anonymous_79_})
                return PyJsComma(var.get(u'p')(var.get(u't'), Js([PyJs_Object_72_, PyJs_Object_75_, PyJs_Object_78_])),var.get(u't'))
            PyJs_anonymous_71_._set_name(u'anonymous')
            var.put(u'v', PyJs_anonymous_71_())
            var.get(u'e').put(u'Encoder', var.get(u'v'))
            @Js
            def PyJs_anonymous_80_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't', u'n'])
                @Js
                def PyJsHoisted_n_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return PyJsComma(var.get(u'u')(var.get(u"this"), var.get(u'n')),var.get(u'e').callprop(u'call', var.get(u"this")))
                PyJsHoisted_n_.func_name = u'n'
                var.put(u'n', PyJsHoisted_n_)
                @Js
                def PyJs_anonymous_81_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                        PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                        raise PyJsTempException
                    PyJs_Object_83_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                    PyJs_Object_82_ = Js({u'constructor':PyJs_Object_83_})
                    PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_82_)),(var.get(u'e') and var.get(u'i')(var.get(u't'), var.get(u'e'))))
                PyJs_anonymous_81_._set_name(u'anonymous')
                PyJs_anonymous_81_(var.get(u'n'), var.get(u't')).neg()
                var.put(u'e', var.get(u's')(var.get(u'n')))
                pass
                @Js
                def PyJs_anonymous_85_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    pass
                    if (Js(u'string')==var.get(u't',throw=False).typeof()):
                        def PyJs_LONG_86_(var=var):
                            return (PyJsComma(var.get(u"this").put(u'reconstructor', var.get(u'm').create(var.get(u'e'))),(PyJsStrictEq(Js(0.0),var.get(u'e').get(u'attachments')) and var.get(u'o')(var.get(u'a')(var.get(u'n').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'decoded'), var.get(u'e')))) if (PyJsStrictEq(var.put(u'e', var.get(u"this").callprop(u'decodeString', var.get(u't'))).get(u'type'),var.get(u'l').get(u'BINARY_EVENT')) or PyJsStrictEq(var.get(u'e').get(u'type'),var.get(u'l').get(u'BINARY_ACK'))) else var.get(u'o')(var.get(u'a')(var.get(u'n').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'decoded'), var.get(u'e')))
                        PyJs_LONG_86_()
                    else:
                        if (var.get(u'd').callprop(u'isBinary', var.get(u't')).neg() and var.get(u't').get(u'base64').neg()):
                            PyJsTempException = JsToPyException(var.get(u'Error').create((Js(u'Unknown type: ')+var.get(u't'))))
                            raise PyJsTempException
                        if var.get(u"this").get(u'reconstructor').neg():
                            PyJsTempException = JsToPyException(var.get(u'Error').create(Js(u'got binary data when not reconstructing a packet')))
                            raise PyJsTempException
                        (var.put(u'e', var.get(u"this").get(u'reconstructor').callprop(u'takeBinaryData', var.get(u't'))) and PyJsComma(var.get(u"this").put(u'reconstructor', var.get(u"null")),var.get(u'o')(var.get(u'a')(var.get(u'n').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'decoded'), var.get(u'e'))))
                PyJs_anonymous_85_._set_name(u'anonymous')
                PyJs_Object_84_ = Js({u'key':Js(u'add'),u'value':PyJs_anonymous_85_})
                @Js
                def PyJs_anonymous_88_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'a', u'c', u'e', u'f', u'i', u'o', u's', u'r', u'u', u't'])
                    var.put(u'e', Js(0.0))
                    PyJs_Object_89_ = Js({u'type':var.get(u'Number')(var.get(u't').callprop(u'charAt', Js(0.0)))})
                    var.put(u'r', PyJs_Object_89_)
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u'l').get(var.get(u'r').get(u'type'))):
                        PyJsTempException = JsToPyException(var.get(u'Error').create((Js(u'unknown packet type ')+var.get(u'r').get(u'type'))))
                        raise PyJsTempException
                    if (PyJsStrictEq(var.get(u'r').get(u'type'),var.get(u'l').get(u'BINARY_EVENT')) or PyJsStrictEq(var.get(u'r').get(u'type'),var.get(u'l').get(u'BINARY_ACK'))):
                        #for JS loop
                        var.put(u'o', (var.get(u'e')+Js(1.0)))
                        while (PyJsStrictNeq(Js(u'-'),var.get(u't').callprop(u'charAt', var.put(u'e',Js(var.get(u'e').to_number())+Js(1)))) and (var.get(u'e')!=var.get(u't').get(u'length'))):
                            pass
                        
                        var.put(u'i', var.get(u't').callprop(u'substring', var.get(u'o'), var.get(u'e')))
                        if ((var.get(u'i')!=var.get(u'Number')(var.get(u'i'))) or PyJsStrictNeq(Js(u'-'),var.get(u't').callprop(u'charAt', var.get(u'e')))):
                            PyJsTempException = JsToPyException(var.get(u'Error').create(Js(u'Illegal attachments')))
                            raise PyJsTempException
                        var.get(u'r').put(u'attachments', var.get(u'Number')(var.get(u'i')))
                    if PyJsStrictEq(Js(u'/'),var.get(u't').callprop(u'charAt', (var.get(u'e')+Js(1.0)))):
                        #for JS loop
                        var.put(u's', (var.get(u'e')+Js(1.0)))
                        while var.put(u'e',Js(var.get(u'e').to_number())+Js(1)):
                            if PyJsStrictEq(Js(u','),var.get(u't').callprop(u'charAt', var.get(u'e'))):
                                break
                            if PyJsStrictEq(var.get(u'e'),var.get(u't').get(u'length')):
                                break
                        
                        var.get(u'r').put(u'nsp', var.get(u't').callprop(u'substring', var.get(u's'), var.get(u'e')))
                    else:
                        var.get(u'r').put(u'nsp', Js(u'/'))
                    var.put(u'c', var.get(u't').callprop(u'charAt', (var.get(u'e')+Js(1.0))))
                    if (PyJsStrictNeq(Js(u''),var.get(u'c')) and (var.get(u'Number')(var.get(u'c'))==var.get(u'c'))):
                        #for JS loop
                        var.put(u'a', (var.get(u'e')+Js(1.0)))
                        while var.put(u'e',Js(var.get(u'e').to_number())+Js(1)):
                            var.put(u'u', var.get(u't').callprop(u'charAt', var.get(u'e')))
                            if ((var.get(u"null")==var.get(u'u')) or (var.get(u'Number')(var.get(u'u'))!=var.get(u'u'))):
                                var.put(u'e',Js(var.get(u'e').to_number())-Js(1))
                                break
                            if PyJsStrictEq(var.get(u'e'),var.get(u't').get(u'length')):
                                break
                        
                        var.get(u'r').put(u'id', var.get(u'Number')(var.get(u't').callprop(u'substring', var.get(u'a'), (var.get(u'e')+Js(1.0)))))
                    if var.get(u't').callprop(u'charAt', var.put(u'e',Js(var.get(u'e').to_number())+Js(1))):
                        @Js
                        def PyJs_anonymous_90_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u't'])
                            try:
                                return var.get(u'JSON').callprop(u'parse', var.get(u't'))
                            except PyJsException as PyJsTempException:
                                PyJsHolder_74_91707326 = var.own.get(u't')
                                var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                                try:
                                    return Js(1.0).neg()
                                finally:
                                    if PyJsHolder_74_91707326 is not None:
                                        var.own[u't'] = PyJsHolder_74_91707326
                                    else:
                                        del var.own[u't']
                                    del PyJsHolder_74_91707326
                        PyJs_anonymous_90_._set_name(u'anonymous')
                        var.put(u'f', PyJs_anonymous_90_(var.get(u't').callprop(u'substr', var.get(u'e'))))
                        if var.get(u'n').callprop(u'isPayloadValid', var.get(u'r').get(u'type'), var.get(u'f')).neg():
                            PyJsTempException = JsToPyException(var.get(u'Error').create(Js(u'invalid payload')))
                            raise PyJsTempException
                        var.get(u'r').put(u'data', var.get(u'f'))
                    return var.get(u'r')
                PyJs_anonymous_88_._set_name(u'anonymous')
                PyJs_Object_87_ = Js({u'key':Js(u'decodeString'),u'value':PyJs_anonymous_88_})
                @Js
                def PyJs_anonymous_92_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    (var.get(u"this").get(u'reconstructor') and var.get(u"this").get(u'reconstructor').callprop(u'finishedReconstruction'))
                PyJs_anonymous_92_._set_name(u'anonymous')
                PyJs_Object_91_ = Js({u'key':Js(u'destroy'),u'value':PyJs_anonymous_92_})
                @Js
                def PyJs_anonymous_94_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get(u't'))
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'CONNECT')):
                            SWITCHED = True
                            return PyJsStrictEq(Js(u'object'),var.get(u'r')(var.get(u'e')))
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'DISCONNECT')):
                            SWITCHED = True
                            return PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u'e'))
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'CONNECT_ERROR')):
                            SWITCHED = True
                            return ((Js(u'string')==var.get(u'e',throw=False).typeof()) or PyJsStrictEq(Js(u'object'),var.get(u'r')(var.get(u'e'))))
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'EVENT')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'BINARY_EVENT')):
                            SWITCHED = True
                            return (var.get(u'Array').callprop(u'isArray', var.get(u'e')) and (var.get(u'e').get(u'length')>Js(0.0)))
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'ACK')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'BINARY_ACK')):
                            SWITCHED = True
                            return var.get(u'Array').callprop(u'isArray', var.get(u'e'))
                        SWITCHED = True
                        break
                PyJs_anonymous_94_._set_name(u'anonymous')
                PyJs_Object_93_ = Js({u'key':Js(u'isPayloadValid'),u'value':PyJs_anonymous_94_})
                return PyJsComma(var.get(u'p')(var.get(u'n'), Js([PyJs_Object_84_, PyJs_Object_87_, PyJs_Object_91_]), Js([PyJs_Object_93_])),var.get(u'n'))
            PyJs_anonymous_80_._set_name(u'anonymous')
            var.put(u'b', PyJs_anonymous_80_(var.get(u'h')))
            var.get(u'e').put(u'Decoder', var.get(u'b'))
            @Js
            def PyJs_anonymous_95_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJsHoisted_t_(e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                    var.registers([u'e'])
                    PyJsComma(PyJsComma(PyJsComma(var.get(u'u')(var.get(u"this"), var.get(u't')),var.get(u"this").put(u'packet', var.get(u'e'))),var.get(u"this").put(u'buffers', Js([]))),var.get(u"this").put(u'reconPack', var.get(u'e')))
                PyJsHoisted_t_.func_name = u't'
                var.put(u't', PyJsHoisted_t_)
                pass
                @Js
                def PyJs_anonymous_97_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if PyJsComma(var.get(u"this").get(u'buffers').callprop(u'push', var.get(u't')),PyJsStrictEq(var.get(u"this").get(u'buffers').get(u'length'),var.get(u"this").get(u'reconPack').get(u'attachments'))):
                        var.put(u'e', var.get(u'y').callprop(u'reconstructPacket', var.get(u"this").get(u'reconPack'), var.get(u"this").get(u'buffers')))
                        return PyJsComma(var.get(u"this").callprop(u'finishedReconstruction'),var.get(u'e'))
                    return var.get(u"null")
                PyJs_anonymous_97_._set_name(u'anonymous')
                PyJs_Object_96_ = Js({u'key':Js(u'takeBinaryData'),u'value':PyJs_anonymous_97_})
                @Js
                def PyJs_anonymous_99_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    PyJsComma(var.get(u"this").put(u'reconPack', var.get(u"null")),var.get(u"this").put(u'buffers', Js([])))
                PyJs_anonymous_99_._set_name(u'anonymous')
                PyJs_Object_98_ = Js({u'key':Js(u'finishedReconstruction'),u'value':PyJs_anonymous_99_})
                return PyJsComma(var.get(u'p')(var.get(u't'), Js([PyJs_Object_96_, PyJs_Object_98_])),var.get(u't'))
            PyJs_anonymous_95_._set_name(u'anonymous')
            var.put(u'm', PyJs_anonymous_95_())
        PyJs_anonymous_56_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_100_(t, e, this, arguments, var=var):
            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
            var.registers([u'r', u'e', u't', u'n'])
            var.put(u'n', JsRegExp(u'/^(?:(?![^:@]+:[^:@\\/]*@)(http|https|ws|wss):\\/\\/)?((?:(([^:@]*)(?::([^:@]*))?)?@)?((?:[a-f0-9]{0,4}:){2,7}[a-f0-9]{0,4}|[^:\\/?#]*)(?::(\\d*))?)(((\\/(?:[^?#](?![^?#\\/]*\\.[^?#\\/.]+(?:[?#]|$)))*\\/?)?([^?#\\/]*))(?:\\?([^#]*))?(?:#(.*))?)/'))
            var.put(u'r', Js([Js(u'source'), Js(u'protocol'), Js(u'authority'), Js(u'userInfo'), Js(u'user'), Js(u'password'), Js(u'host'), Js(u'port'), Js(u'relative'), Js(u'path'), Js(u'directory'), Js(u'file'), Js(u'query'), Js(u'anchor')]))
            @Js
            def PyJs_anonymous_101_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'c', u'e', u'f', u'i', u'o', u's', u'u', u't'])
                var.put(u'e', var.get(u't'))
                var.put(u'o', var.get(u't').callprop(u'indexOf', Js(u'[')))
                var.put(u'i', var.get(u't').callprop(u'indexOf', Js(u']')))
                ((((-Js(1.0))!=var.get(u'o')) and ((-Js(1.0))!=var.get(u'i'))) and var.put(u't', ((var.get(u't').callprop(u'substring', Js(0.0), var.get(u'o'))+var.get(u't').callprop(u'substring', var.get(u'o'), var.get(u'i')).callprop(u'replace', JsRegExp(u'/:/g'), Js(u';')))+var.get(u't').callprop(u'substring', var.get(u'i'), var.get(u't').get(u'length')))))
                #for JS loop
                var.put(u'a', var.get(u'n').callprop(u'exec', (var.get(u't') or Js(u''))))
                PyJs_Object_102_ = Js({})
                var.put(u'u', PyJs_Object_102_)
                var.put(u'f', Js(14.0))
                while (var.put(u'f',Js(var.get(u'f').to_number())-Js(1))+Js(1)):
                    var.get(u'u').put(var.get(u'r').get(var.get(u'f')), (var.get(u'a').get(var.get(u'f')) or Js(u'')))
                
                def PyJs_LONG_107_(var=var):
                    def PyJs_LONG_103_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(var.get(u'u').put(u'source', var.get(u'e')),var.get(u'u').put(u'host', var.get(u'u').get(u'host').callprop(u'substring', Js(1.0), (var.get(u'u').get(u'host').get(u'length')-Js(1.0))).callprop(u'replace', JsRegExp(u'/;/g'), Js(u':')))),var.get(u'u').put(u'authority', var.get(u'u').get(u'authority').callprop(u'replace', Js(u'['), Js(u'')).callprop(u'replace', Js(u']'), Js(u'')).callprop(u'replace', JsRegExp(u'/;/g'), Js(u':')))),var.get(u'u').put(u'ipv6uri', Js(0.0).neg()))
                    @Js
                    def PyJs_anonymous_104_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        var.put(u'n', var.get(u'e').callprop(u'replace', JsRegExp(u'/\\/{2,9}/g'), Js(u'/')).callprop(u'split', Js(u'/')))
                        (((Js(u'/')!=var.get(u'e').callprop(u'substr', Js(0.0), Js(1.0))) and PyJsStrictNeq(Js(0.0),var.get(u'e').get(u'length'))) or var.get(u'n').callprop(u'splice', Js(0.0), Js(1.0)))
                        ((Js(u'/')==var.get(u'e').callprop(u'substr', (var.get(u'e').get(u'length')-Js(1.0)), Js(1.0))) and var.get(u'n').callprop(u'splice', (var.get(u'n').get(u'length')-Js(1.0)), Js(1.0)))
                        return var.get(u'n')
                    PyJs_anonymous_104_._set_name(u'anonymous')
                    PyJs_Object_105_ = Js({})
                    @Js
                    def PyJs_anonymous_106_(t, e, n, this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                        var.registers([u'e', u't', u'n'])
                        (var.get(u'e') and var.get(u'c').put(var.get(u'e'), var.get(u'n')))
                    PyJs_anonymous_106_._set_name(u'anonymous')
                    return PyJsComma(PyJsComma(PyJsComma(((((-Js(1.0))!=var.get(u'o')) and ((-Js(1.0))!=var.get(u'i'))) and PyJs_LONG_103_()),var.get(u'u').put(u'pathNames', PyJs_anonymous_104_(Js(0.0), var.get(u'u').get(u'path')))),var.get(u'u').put(u'queryKey', PyJsComma(PyJsComma(PyJsComma(var.put(u's', var.get(u'u').get(u'query')),var.put(u'c', PyJs_Object_105_)),var.get(u's').callprop(u'replace', JsRegExp(u'/(?:^|&)([^&=]*)=?([^&]*)/g'), PyJs_anonymous_106_)),var.get(u'c')))),var.get(u'u'))
                return PyJs_LONG_107_()
            PyJs_anonymous_101_._set_name(u'anonymous')
            var.get(u't').put(u'exports', PyJs_anonymous_101_)
        PyJs_anonymous_100_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_108_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'd', u'f', u'i', u'h', u'l', u'o', u'n', u'p', u's', u'r', u'u', u't', u'v', u'y'])
            @Js
            def PyJsHoisted_a_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_117_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                        PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                        raise PyJsTempException
                    return var.get(u't')
                PyJs_anonymous_117_._set_name(u'anonymous')
                return (PyJs_anonymous_117_(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_114_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_115_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_115_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_115_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_11194988 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_11194988 is not None:
                                var.own[u't'] = PyJsHolder_74_11194988
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_11194988
                PyJs_anonymous_114_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_114_())
                @Js
                def PyJs_anonymous_116_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'u')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'u')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'a')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_116_._set_name(u'anonymous')
                return PyJs_anonymous_116_
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_i_(t, e, n, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                var.registers([u'e', u't', u'n'])
                @Js
                def PyJs_anonymous_111_(t, e, n, this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                    var.registers([u'r', u'e', u't', u'o', u'n'])
                    @Js
                    def PyJs_anonymous_112_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        #for JS loop
                        
                        while (var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u't'), var.get(u'e')).neg() and PyJsStrictNeq(var.get(u"null"),var.put(u't', var.get(u'u')(var.get(u't'))))):
                            pass
                        
                        return var.get(u't')
                    PyJs_anonymous_112_._set_name(u'anonymous')
                    var.put(u'r', PyJs_anonymous_112_(var.get(u't'), var.get(u'e')))
                    if var.get(u'r'):
                        var.put(u'o', var.get(u'Object').callprop(u'getOwnPropertyDescriptor', var.get(u'r'), var.get(u'e')))
                        return (var.get(u'o').get(u'get').callprop(u'call', var.get(u'n')) if var.get(u'o').get(u'get') else var.get(u'o').get(u'value'))
                PyJs_anonymous_111_._set_name(u'anonymous')
                return var.put(u'i', (var.get(u'Reflect').get(u'get') if ((Js(u'undefined')!=var.get(u'Reflect',throw=False).typeof()) and var.get(u'Reflect').get(u'get')) else PyJs_anonymous_111_))(var.get(u't'), var.get(u'e'), (var.get(u'n') or var.get(u't')))
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_o_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_s_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_113_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_113_._set_name(u'anonymous')
                return var.put(u's', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_113_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_109_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_109_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_110_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_110_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_109_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_110_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            @Js
            def PyJsHoisted_u_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_118_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_118_._set_name(u'anonymous')
                return var.put(u'u', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_118_))(var.get(u't'))
            PyJsHoisted_u_.func_name = u'u'
            var.put(u'u', PyJsHoisted_u_)
            Js(u'use strict')
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            PyJs_Object_119_ = Js({u'value':Js(0.0).neg()})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'__esModule'), PyJs_Object_119_),var.get(u'e').put(u'Manager', PyJsComma(Js(0.0), Js(None))))
            var.put(u'f', var.get(u'n')(Js(19.0)))
            var.put(u'p', var.get(u'n')(Js(14.0)))
            var.put(u'l', var.get(u'n')(Js(0.0)))
            var.put(u'h', var.get(u'n')(Js(5.0)))
            var.put(u'y', var.get(u'n')(Js(16.0)))
            var.put(u'd', var.get(u'n')(Js(30.0)))
            @Js
            def PyJs_anonymous_120_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'e', u'l', u'n', u't', u'v'])
                @Js
                def PyJsHoisted_v_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'o', u'n'])
                    pass
                    def PyJs_LONG_128_(var=var):
                        @Js
                        def PyJs_anonymous_124_(t, e, this, arguments, var=var):
                            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                            var.registers([u'e', u't'])
                            if var.get(u't').instanceof(var.get(u'e')).neg():
                                PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                                raise PyJsTempException
                        PyJs_anonymous_124_._set_name(u'anonymous')
                        PyJs_Object_125_ = Js({})
                        PyJs_Object_126_ = Js({})
                        PyJs_Object_127_ = Js({u'min':var.get(u'n').callprop(u'reconnectionDelay'),u'max':var.get(u'n').callprop(u'reconnectionDelayMax'),u'jitter':var.get(u'n').callprop(u'randomizationFactor')})
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJs_anonymous_124_(var.get(u"this"), var.get(u'v')).neg(),var.put(u'n', var.get(u'l').callprop(u'call', var.get(u"this"))).put(u'nsps', PyJs_Object_125_)),var.get(u'n').put(u'subs', Js([]))),((var.get(u't') and PyJsStrictEq(Js(u'object'),var.get(u'r')(var.get(u't')))) and PyJsComma(var.put(u'e', var.get(u't')),var.put(u't', PyJsComma(Js(0.0), Js(None)))))),var.put(u'e', (var.get(u'e') or PyJs_Object_126_)).put(u'path', (var.get(u'e').get(u'path') or Js(u'/socket.io')))),var.get(u'n').put(u'opts', var.get(u'e'))),var.get(u'n').callprop(u'reconnection', PyJsStrictNeq(Js(1.0).neg(),var.get(u'e').get(u'reconnection')))),var.get(u'n').callprop(u'reconnectionAttempts', (var.get(u'e').get(u'reconnectionAttempts') or (Js(1.0)/Js(0.0))))),var.get(u'n').callprop(u'reconnectionDelay', (var.get(u'e').get(u'reconnectionDelay') or Js(1000.0)))),var.get(u'n').callprop(u'reconnectionDelayMax', (var.get(u'e').get(u'reconnectionDelayMax') or Js(5000.0)))),var.get(u'n').callprop(u'randomizationFactor', (var.get(u'e').get(u'randomizationFactor') or Js(0.5)))),var.get(u'n').put(u'backoff', var.get(u'd').create(PyJs_Object_127_))),var.get(u'n').callprop(u'timeout', (Js(20000.0) if (var.get(u"null")==var.get(u'e').get(u'timeout')) else var.get(u'e').get(u'timeout')))),var.get(u'n').put(u'_readyState', Js(u'closed'))),var.get(u'n').put(u'uri', var.get(u't')))
                    PyJs_LONG_128_()
                    var.put(u'o', (var.get(u'e').get(u'parser') or var.get(u'h')))
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'n').put(u'encoder', var.get(u'o').get(u'Encoder').create()),var.get(u'n').put(u'decoder', var.get(u'o').get(u'Decoder').create())),var.get(u'n').put(u'_autoConnect', PyJsStrictNeq(Js(1.0).neg(),var.get(u'e').get(u'autoConnect')))),(var.get(u'n').get(u'_autoConnect') and var.get(u'n').callprop(u'open'))),var.get(u'n'))
                PyJsHoisted_v_.func_name = u'v'
                var.put(u'v', PyJsHoisted_v_)
                @Js
                def PyJs_anonymous_121_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                        PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                        raise PyJsTempException
                    PyJs_Object_123_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                    PyJs_Object_122_ = Js({u'constructor':PyJs_Object_123_})
                    PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_122_)),(var.get(u'e') and var.get(u's')(var.get(u't'), var.get(u'e'))))
                PyJs_anonymous_121_._set_name(u'anonymous')
                PyJs_anonymous_121_(var.get(u'v'), var.get(u't')).neg()
                var.put(u'l', var.get(u'c')(var.get(u'v')))
                pass
                def PyJs_LONG_189_(var=var):
                    @Js
                    def PyJs_anonymous_130_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        return (PyJsComma(var.get(u"this").put(u'_reconnection', var.get(u't').neg().neg()),var.get(u"this")) if var.get(u'arguments').get(u'length') else var.get(u"this").get(u'_reconnection'))
                    PyJs_anonymous_130_._set_name(u'anonymous')
                    PyJs_Object_129_ = Js({u'key':Js(u'reconnection'),u'value':PyJs_anonymous_130_})
                    @Js
                    def PyJs_anonymous_132_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        return (var.get(u"this").get(u'_reconnectionAttempts') if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')) else PyJsComma(var.get(u"this").put(u'_reconnectionAttempts', var.get(u't')),var.get(u"this")))
                    PyJs_anonymous_132_._set_name(u'anonymous')
                    PyJs_Object_131_ = Js({u'key':Js(u'reconnectionAttempts'),u'value':PyJs_anonymous_132_})
                    @Js
                    def PyJs_anonymous_134_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        pass
                        def PyJs_LONG_135_(var=var):
                            return (var.get(u"this").get(u'_reconnectionDelay') if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')) else PyJsComma(PyJsComma(var.get(u"this").put(u'_reconnectionDelay', var.get(u't')),((PyJsStrictEq(var.get(u"null"),var.put(u'e', var.get(u"this").get(u'backoff'))) or PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u'e'))) or var.get(u'e').callprop(u'setMin', var.get(u't')))),var.get(u"this")))
                        return PyJs_LONG_135_()
                    PyJs_anonymous_134_._set_name(u'anonymous')
                    PyJs_Object_133_ = Js({u'key':Js(u'reconnectionDelay'),u'value':PyJs_anonymous_134_})
                    @Js
                    def PyJs_anonymous_137_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        pass
                        def PyJs_LONG_138_(var=var):
                            return (var.get(u"this").get(u'_randomizationFactor') if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')) else PyJsComma(PyJsComma(var.get(u"this").put(u'_randomizationFactor', var.get(u't')),((PyJsStrictEq(var.get(u"null"),var.put(u'e', var.get(u"this").get(u'backoff'))) or PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u'e'))) or var.get(u'e').callprop(u'setJitter', var.get(u't')))),var.get(u"this")))
                        return PyJs_LONG_138_()
                    PyJs_anonymous_137_._set_name(u'anonymous')
                    PyJs_Object_136_ = Js({u'key':Js(u'randomizationFactor'),u'value':PyJs_anonymous_137_})
                    @Js
                    def PyJs_anonymous_140_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        pass
                        def PyJs_LONG_141_(var=var):
                            return (var.get(u"this").get(u'_reconnectionDelayMax') if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')) else PyJsComma(PyJsComma(var.get(u"this").put(u'_reconnectionDelayMax', var.get(u't')),((PyJsStrictEq(var.get(u"null"),var.put(u'e', var.get(u"this").get(u'backoff'))) or PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u'e'))) or var.get(u'e').callprop(u'setMax', var.get(u't')))),var.get(u"this")))
                        return PyJs_LONG_141_()
                    PyJs_anonymous_140_._set_name(u'anonymous')
                    PyJs_Object_139_ = Js({u'key':Js(u'reconnectionDelayMax'),u'value':PyJs_anonymous_140_})
                    @Js
                    def PyJs_anonymous_143_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        return (PyJsComma(var.get(u"this").put(u'_timeout', var.get(u't')),var.get(u"this")) if var.get(u'arguments').get(u'length') else var.get(u"this").get(u'_timeout'))
                    PyJs_anonymous_143_._set_name(u'anonymous')
                    PyJs_Object_142_ = Js({u'key':Js(u'timeout'),u'value':PyJs_anonymous_143_})
                    @Js
                    def PyJs_anonymous_145_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        (((var.get(u"this").get(u'_reconnecting').neg() and var.get(u"this").get(u'_reconnection')) and PyJsStrictEq(Js(0.0),var.get(u"this").get(u'backoff').get(u'attempts'))) and var.get(u"this").callprop(u'reconnect'))
                    PyJs_anonymous_145_._set_name(u'anonymous')
                    PyJs_Object_144_ = Js({u'key':Js(u'maybeReconnectOnOpen'),u'value':PyJs_anonymous_145_})
                    @Js
                    def PyJs_anonymous_147_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'a', u'c', u'e', u'o', u'n', u's', u'r', u't'])
                        var.put(u'e', var.get(u"this"))
                        if (~var.get(u"this").get(u'_readyState').callprop(u'indexOf', Js(u'open'))):
                            return var.get(u"this")
                        var.get(u"this").put(u'engine', var.get(u'f')(var.get(u"this").get(u'uri'), var.get(u"this").get(u'opts')))
                        var.put(u'n', var.get(u"this").get(u'engine'))
                        var.put(u'r', var.get(u"this"))
                        PyJsComma(var.get(u"this").put(u'_readyState', Js(u'opening')),var.get(u"this").put(u'skipReconnect', Js(1.0).neg()))
                        @Js
                        def PyJs_anonymous_148_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            PyJsComma(var.get(u'r').callprop(u'onopen'),(var.get(u't') and var.get(u't')()))
                        PyJs_anonymous_148_._set_name(u'anonymous')
                        var.put(u'o', var.get(u'y').callprop(u'on', var.get(u'n'), Js(u'open'), PyJs_anonymous_148_))
                        @Js
                        def PyJs_anonymous_149_(n, this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments, u'n':n}, var)
                            var.registers([u'n'])
                            PyJsComma(PyJsComma(PyJsComma(var.get(u'r').callprop(u'cleanup'),var.get(u'r').put(u'_readyState', Js(u'closed'))),var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u'e')).callprop(u'call', var.get(u'e'), Js(u'error'), var.get(u'n'))),(var.get(u't')(var.get(u'n')) if var.get(u't') else var.get(u'r').callprop(u'maybeReconnectOnOpen')))
                        PyJs_anonymous_149_._set_name(u'anonymous')
                        var.put(u's', var.get(u'y').callprop(u'on', var.get(u'n'), Js(u'error'), PyJs_anonymous_149_))
                        if PyJsStrictNeq(Js(1.0).neg(),var.get(u"this").get(u'_timeout')):
                            var.put(u'c', var.get(u"this").get(u'_timeout'))
                            (PyJsStrictEq(Js(0.0),var.get(u'c')) and var.get(u'o')())
                            @Js
                            def PyJs_anonymous_150_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                PyJsComma(PyJsComma(var.get(u'o')(),var.get(u'n').callprop(u'close')),var.get(u'n').callprop(u'emit', Js(u'error'), var.get(u'Error').create(Js(u'timeout'))))
                            PyJs_anonymous_150_._set_name(u'anonymous')
                            var.put(u'a', var.get(u'setTimeout')(PyJs_anonymous_150_, var.get(u'c')))
                            @Js
                            def PyJs_anonymous_151_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                var.get(u'clearTimeout')(var.get(u'a'))
                            PyJs_anonymous_151_._set_name(u'anonymous')
                            var.get(u"this").get(u'subs').callprop(u'push', PyJs_anonymous_151_)
                        return PyJsComma(PyJsComma(var.get(u"this").get(u'subs').callprop(u'push', var.get(u'o')),var.get(u"this").get(u'subs').callprop(u'push', var.get(u's'))),var.get(u"this"))
                    PyJs_anonymous_147_._set_name(u'anonymous')
                    PyJs_Object_146_ = Js({u'key':Js(u'open'),u'value':PyJs_anonymous_147_})
                    @Js
                    def PyJs_anonymous_153_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        return var.get(u"this").callprop(u'open', var.get(u't'))
                    PyJs_anonymous_153_._set_name(u'anonymous')
                    PyJs_Object_152_ = Js({u'key':Js(u'connect'),u'value':PyJs_anonymous_153_})
                    @Js
                    def PyJs_anonymous_155_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u't'])
                        PyJsComma(PyJsComma(var.get(u"this").callprop(u'cleanup'),var.get(u"this").put(u'_readyState', Js(u'open'))),var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'open')))
                        var.put(u't', var.get(u"this").get(u'engine'))
                        def PyJs_LONG_156_(var=var):
                            return var.get(u"this").get(u'subs').callprop(u'push', var.get(u'y').callprop(u'on', var.get(u't'), Js(u'ping'), var.get(u"this").get(u'onping').callprop(u'bind', var.get(u"this"))), var.get(u'y').callprop(u'on', var.get(u't'), Js(u'data'), var.get(u"this").get(u'ondata').callprop(u'bind', var.get(u"this"))), var.get(u'y').callprop(u'on', var.get(u't'), Js(u'error'), var.get(u"this").get(u'onerror').callprop(u'bind', var.get(u"this"))), var.get(u'y').callprop(u'on', var.get(u't'), Js(u'close'), var.get(u"this").get(u'onclose').callprop(u'bind', var.get(u"this"))), var.get(u'y').callprop(u'on', var.get(u"this").get(u'decoder'), Js(u'decoded'), var.get(u"this").get(u'ondecoded').callprop(u'bind', var.get(u"this"))))
                        PyJs_LONG_156_()
                    PyJs_anonymous_155_._set_name(u'anonymous')
                    PyJs_Object_154_ = Js({u'key':Js(u'onopen'),u'value':PyJs_anonymous_155_})
                    @Js
                    def PyJs_anonymous_158_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'ping'))
                    PyJs_anonymous_158_._set_name(u'anonymous')
                    PyJs_Object_157_ = Js({u'key':Js(u'onping'),u'value':PyJs_anonymous_158_})
                    @Js
                    def PyJs_anonymous_160_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.get(u"this").get(u'decoder').callprop(u'add', var.get(u't'))
                    PyJs_anonymous_160_._set_name(u'anonymous')
                    PyJs_Object_159_ = Js({u'key':Js(u'ondata'),u'value':PyJs_anonymous_160_})
                    @Js
                    def PyJs_anonymous_162_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'packet'), var.get(u't'))
                    PyJs_anonymous_162_._set_name(u'anonymous')
                    PyJs_Object_161_ = Js({u'key':Js(u'ondecoded'),u'value':PyJs_anonymous_162_})
                    @Js
                    def PyJs_anonymous_164_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'error'), var.get(u't'))
                    PyJs_anonymous_164_._set_name(u'anonymous')
                    PyJs_Object_163_ = Js({u'key':Js(u'onerror'),u'value':PyJs_anonymous_164_})
                    @Js
                    def PyJs_anonymous_166_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        var.put(u'n', var.get(u"this").get(u'nsps').get(var.get(u't')))
                        return PyJsComma((var.get(u'n') or PyJsComma(var.put(u'n', var.get(u'p').get(u'Socket').create(var.get(u"this"), var.get(u't'), var.get(u'e'))),var.get(u"this").get(u'nsps').put(var.get(u't'), var.get(u'n')))),var.get(u'n'))
                    PyJs_anonymous_166_._set_name(u'anonymous')
                    PyJs_Object_165_ = Js({u'key':Js(u'socket'),u'value':PyJs_anonymous_166_})
                    @Js
                    def PyJs_anonymous_168_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'r', u'e', u't', u'n'])
                        #for JS loop
                        var.put(u'e', Js(0.0))
                        var.put(u'n', var.get(u'Object').callprop(u'keys', var.get(u"this").get(u'nsps')))
                        while (var.get(u'e')<var.get(u'n').get(u'length')):
                            try:
                                var.put(u'r', var.get(u'n').get(var.get(u'e')))
                                if var.get(u"this").get(u'nsps').get(var.get(u'r')).get(u'active'):
                                    return var.get('undefined')
                            finally:
                                    (var.put(u'e',Js(var.get(u'e').to_number())+Js(1))-Js(1))
                        var.get(u"this").callprop(u'_close')
                    PyJs_anonymous_168_._set_name(u'anonymous')
                    PyJs_Object_167_ = Js({u'key':Js(u'_destroy'),u'value':PyJs_anonymous_168_})
                    @Js
                    def PyJs_anonymous_170_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        #for JS loop
                        var.put(u'e', var.get(u"this").get(u'encoder').callprop(u'encode', var.get(u't')))
                        var.put(u'n', Js(0.0))
                        while (var.get(u'n')<var.get(u'e').get(u'length')):
                            try:
                                var.get(u"this").get(u'engine').callprop(u'write', var.get(u'e').get(var.get(u'n')), var.get(u't').get(u'options'))
                            finally:
                                    (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
                    PyJs_anonymous_170_._set_name(u'anonymous')
                    PyJs_Object_169_ = Js({u'key':Js(u'_packet'),u'value':PyJs_anonymous_170_})
                    @Js
                    def PyJs_anonymous_172_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        @Js
                        def PyJs_anonymous_173_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u't'])
                            return var.get(u't')()
                        PyJs_anonymous_173_._set_name(u'anonymous')
                        PyJsComma(PyJsComma(var.get(u"this").get(u'subs').callprop(u'forEach', PyJs_anonymous_173_),var.get(u"this").get(u'subs').put(u'length', Js(0.0))),var.get(u"this").get(u'decoder').callprop(u'destroy'))
                    PyJs_anonymous_172_._set_name(u'anonymous')
                    PyJs_Object_171_ = Js({u'key':Js(u'cleanup'),u'value':PyJs_anonymous_172_})
                    @Js
                    def PyJs_anonymous_175_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        def PyJs_LONG_176_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put(u'skipReconnect', Js(0.0).neg()),var.get(u"this").put(u'_reconnecting', Js(1.0).neg())),(PyJsStrictEq(Js(u'opening'),var.get(u"this").get(u'_readyState')) and var.get(u"this").callprop(u'cleanup'))),var.get(u"this").get(u'backoff').callprop(u'reset')),var.get(u"this").put(u'_readyState', Js(u'closed'))),(var.get(u"this").get(u'engine') and var.get(u"this").get(u'engine').callprop(u'close')))
                        PyJs_LONG_176_()
                    PyJs_anonymous_175_._set_name(u'anonymous')
                    PyJs_Object_174_ = Js({u'key':Js(u'_close'),u'value':PyJs_anonymous_175_})
                    @Js
                    def PyJs_anonymous_178_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return var.get(u"this").callprop(u'_close')
                    PyJs_anonymous_178_._set_name(u'anonymous')
                    PyJs_Object_177_ = Js({u'key':Js(u'disconnect'),u'value':PyJs_anonymous_178_})
                    @Js
                    def PyJs_anonymous_180_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        def PyJs_LONG_181_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").callprop(u'cleanup'),var.get(u"this").get(u'backoff').callprop(u'reset')),var.get(u"this").put(u'_readyState', Js(u'closed'))),var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'close'), var.get(u't'))),((var.get(u"this").get(u'_reconnection') and var.get(u"this").get(u'skipReconnect').neg()) and var.get(u"this").callprop(u'reconnect')))
                        PyJs_LONG_181_()
                    PyJs_anonymous_180_._set_name(u'anonymous')
                    PyJs_Object_179_ = Js({u'key':Js(u'onclose'),u'value':PyJs_anonymous_180_})
                    @Js
                    def PyJs_anonymous_183_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u'r', u'e', u't', u'n'])
                        var.put(u't', var.get(u"this"))
                        if (var.get(u"this").get(u'_reconnecting') or var.get(u"this").get(u'skipReconnect')):
                            return var.get(u"this")
                        var.put(u'e', var.get(u"this"))
                        if (var.get(u"this").get(u'backoff').get(u'attempts')>=var.get(u"this").get(u'_reconnectionAttempts')):
                            PyJsComma(PyJsComma(var.get(u"this").get(u'backoff').callprop(u'reset'),var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'reconnect_failed'))),var.get(u"this").put(u'_reconnecting', Js(1.0).neg()))
                        else:
                            var.put(u'n', var.get(u"this").get(u'backoff').callprop(u'duration'))
                            var.get(u"this").put(u'_reconnecting', Js(0.0).neg())
                            @Js
                            def PyJs_anonymous_184_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                @Js
                                def PyJs_anonymous_185_(n, this, arguments, var=var):
                                    var = Scope({u'this':this, u'arguments':arguments, u'n':n}, var)
                                    var.registers([u'n'])
                                    (PyJsComma(PyJsComma(var.get(u'e').put(u'_reconnecting', Js(1.0).neg()),var.get(u'e').callprop(u'reconnect')),var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u't')).callprop(u'call', var.get(u't'), Js(u'reconnect_error'), var.get(u'n'))) if var.get(u'n') else var.get(u'e').callprop(u'onreconnect'))
                                PyJs_anonymous_185_._set_name(u'anonymous')
                                (var.get(u'e').get(u'skipReconnect') or PyJsComma(var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u't')).callprop(u'call', var.get(u't'), Js(u'reconnect_attempt'), var.get(u'e').get(u'backoff').get(u'attempts')),(var.get(u'e').get(u'skipReconnect') or var.get(u'e').callprop(u'open', PyJs_anonymous_185_))))
                            PyJs_anonymous_184_._set_name(u'anonymous')
                            var.put(u'r', var.get(u'setTimeout')(PyJs_anonymous_184_, var.get(u'n')))
                            @Js
                            def PyJs_anonymous_186_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                var.get(u'clearTimeout')(var.get(u'r'))
                            PyJs_anonymous_186_._set_name(u'anonymous')
                            var.get(u"this").get(u'subs').callprop(u'push', PyJs_anonymous_186_)
                    PyJs_anonymous_183_._set_name(u'anonymous')
                    PyJs_Object_182_ = Js({u'key':Js(u'reconnect'),u'value':PyJs_anonymous_183_})
                    @Js
                    def PyJs_anonymous_188_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.put(u't', var.get(u"this").get(u'backoff').get(u'attempts'))
                        PyJsComma(PyJsComma(var.get(u"this").put(u'_reconnecting', Js(1.0).neg()),var.get(u"this").get(u'backoff').callprop(u'reset')),var.get(u'i')(var.get(u'u')(var.get(u'v').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'reconnect'), var.get(u't')))
                    PyJs_anonymous_188_._set_name(u'anonymous')
                    PyJs_Object_187_ = Js({u'key':Js(u'onreconnect'),u'value':PyJs_anonymous_188_})
                    return var.put(u'n', Js([PyJs_Object_129_, PyJs_Object_131_, PyJs_Object_133_, PyJs_Object_136_, PyJs_Object_139_, PyJs_Object_142_, PyJs_Object_144_, PyJs_Object_146_, PyJs_Object_152_, PyJs_Object_154_, PyJs_Object_157_, PyJs_Object_159_, PyJs_Object_161_, PyJs_Object_163_, PyJs_Object_165_, PyJs_Object_167_, PyJs_Object_169_, PyJs_Object_171_, PyJs_Object_174_, PyJs_Object_177_, PyJs_Object_179_, PyJs_Object_182_, PyJs_Object_187_]))
                return PyJsComma(PyJsComma(PyJsComma(var.put(u'e', var.get(u'v')),(PyJs_LONG_189_() and var.get(u'o')(var.get(u'e').get(u'prototype'), var.get(u'n')))),(var.get(u'a') and var.get(u'o')(var.get(u'e'), var.get(u'a')))),var.get(u'v'))
            PyJs_anonymous_120_._set_name(u'anonymous')
            var.put(u'v', PyJs_anonymous_120_(var.get(u'l')))
            var.get(u'e').put(u'Manager', var.get(u'v'))
        PyJs_anonymous_108_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_190_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'e', u'i', u'o', u'n', u's', u'r', u't'])
            var.put(u'r', var.get(u'n')(Js(9.0)))
            var.put(u'o', var.get(u'n')(Js(22.0)))
            var.put(u'i', var.get(u'n')(Js(26.0)))
            var.put(u's', var.get(u'n')(Js(27.0)))
            @Js
            def PyJs_anonymous_191_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'c', u'e', u'n', u's', u't'])
                var.put(u'e', Js(1.0).neg())
                var.put(u'n', Js(1.0).neg())
                var.put(u's', PyJsStrictNeq(Js(1.0).neg(),var.get(u't').get(u'jsonp')))
                if (Js(u'undefined')!=var.get(u'location',throw=False).typeof()):
                    var.put(u'c', PyJsStrictEq(Js(u'https:'),var.get(u'location').get(u'protocol')))
                    var.put(u'a', var.get(u'location').get(u'port'))
                    PyJsComma(PyJsComma((var.get(u'a') or var.put(u'a', (Js(443.0) if var.get(u'c') else Js(80.0)))),var.put(u'e', (PyJsStrictNeq(var.get(u't').get(u'hostname'),var.get(u'location').get(u'hostname')) or PyJsStrictNeq(var.get(u'a'),var.get(u't').get(u'port'))))),var.put(u'n', PyJsStrictNeq(var.get(u't').get(u'secure'),var.get(u'c'))))
                if PyJsComma(PyJsComma(var.get(u't').put(u'xdomain', var.get(u'e')),var.get(u't').put(u'xscheme', var.get(u'n'))),(var.get(u'r').create(var.get(u't')).contains(Js(u'open')) and var.get(u't').get(u'forceJSONP').neg())):
                    return var.get(u'o').create(var.get(u't'))
                if var.get(u's').neg():
                    PyJsTempException = JsToPyException(var.get(u'Error').create(Js(u'JSONP disabled')))
                    raise PyJsTempException
                return var.get(u'i').create(var.get(u't'))
            PyJs_anonymous_191_._set_name(u'anonymous')
            PyJsComma(var.get(u'e').put(u'polling', PyJs_anonymous_191_),var.get(u'e').put(u'websocket', var.get(u's')))
        PyJs_anonymous_190_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_192_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'r', u'e', u't', u'o', u'n'])
            var.put(u'r', var.get(u'n')(Js(21.0)))
            var.put(u'o', var.get(u'n')(Js(2.0)))
            @Js
            def PyJs_anonymous_193_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'i', u'e', u't', u'n'])
                var.put(u'e', var.get(u't').get(u'xdomain'))
                var.put(u'n', var.get(u't').get(u'xscheme'))
                var.put(u'i', var.get(u't').get(u'enablesXDR'))
                try:
                    if ((Js(u'undefined')!=var.get(u'XMLHttpRequest',throw=False).typeof()) and (var.get(u'e').neg() or var.get(u'r'))):
                        return var.get(u'XMLHttpRequest').create()
                except PyJsException as PyJsTempException:
                    PyJsHolder_74_42088556 = var.own.get(u't')
                    var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                    try:
                        pass
                    finally:
                        if PyJsHolder_74_42088556 is not None:
                            var.own[u't'] = PyJsHolder_74_42088556
                        else:
                            del var.own[u't']
                        del PyJsHolder_74_42088556
                try:
                    if (((Js(u'undefined')!=var.get(u'XDomainRequest',throw=False).typeof()) and var.get(u'n').neg()) and var.get(u'i')):
                        return var.get(u'XDomainRequest').create()
                except PyJsException as PyJsTempException:
                    PyJsHolder_74_11967082 = var.own.get(u't')
                    var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                    try:
                        pass
                    finally:
                        if PyJsHolder_74_11967082 is not None:
                            var.own[u't'] = PyJsHolder_74_11967082
                        else:
                            del var.own[u't']
                        del PyJsHolder_74_11967082
                if var.get(u'e').neg():
                    try:
                        return var.get(u'o').get(Js([Js(u'Active')]).callprop(u'concat', Js(u'Object')).callprop(u'join', Js(u'X'))).create(Js(u'Microsoft.XMLHTTP'))
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_63207863 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            pass
                        finally:
                            if PyJsHolder_74_63207863 is not None:
                                var.own[u't'] = PyJsHolder_74_63207863
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_63207863
            PyJs_anonymous_193_._set_name(u'anonymous')
            var.get(u't').put(u'exports', PyJs_anonymous_193_)
        PyJs_anonymous_192_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_194_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'f', u'i', u'h', u'l', u'o', u'n', u'p', u's', u'r', u'u', u't', u'y'])
            @Js
            def PyJsHoisted_a_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_201_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                        PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                        raise PyJsTempException
                    return var.get(u't')
                PyJs_anonymous_201_._set_name(u'anonymous')
                return (PyJs_anonymous_201_(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_198_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_199_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_199_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_199_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_75020500 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_75020500 is not None:
                                var.own[u't'] = PyJsHolder_74_75020500
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_75020500
                PyJs_anonymous_198_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_198_())
                @Js
                def PyJs_anonymous_200_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'u')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'u')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'a')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_200_._set_name(u'anonymous')
                return PyJs_anonymous_200_
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_i_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_o_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                if var.get(u't').instanceof(var.get(u'e')).neg():
                    PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                    raise PyJsTempException
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_s_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_197_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_197_._set_name(u'anonymous')
                return var.put(u's', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_197_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_195_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_195_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_196_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_196_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_195_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_196_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            @Js
            def PyJsHoisted_u_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_202_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_202_._set_name(u'anonymous')
                return var.put(u'u', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_202_))(var.get(u't'))
            PyJsHoisted_u_.func_name = u'u'
            var.put(u'u', PyJsHoisted_u_)
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            var.put(u'f', var.get(u'n')(Js(3.0)))
            var.put(u'p', var.get(u'n')(Js(4.0)))
            var.put(u'l', var.get(u'n')(Js(1.0)))
            var.put(u'h', var.get(u'n')(Js(12.0)))
            @Js
            def PyJs_anonymous_203_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'e', u'n', u'r', u'u', u't'])
                @Js
                def PyJsHoisted_u_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return PyJsComma(var.get(u'o')(var.get(u"this"), var.get(u'u')),var.get(u'a').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                PyJsHoisted_u_.func_name = u'u'
                var.put(u'u', PyJsHoisted_u_)
                @Js
                def PyJs_anonymous_204_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                        PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                        raise PyJsTempException
                    PyJs_Object_206_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                    PyJs_Object_205_ = Js({u'constructor':PyJs_Object_206_})
                    PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_205_)),(var.get(u'e') and var.get(u's')(var.get(u't'), var.get(u'e'))))
                PyJs_anonymous_204_._set_name(u'anonymous')
                PyJs_anonymous_204_(var.get(u'u'), var.get(u't')).neg()
                var.put(u'a', var.get(u'c')(var.get(u'u')))
                pass
                @Js
                def PyJs_anonymous_208_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    var.get(u"this").callprop(u'poll')
                PyJs_anonymous_208_._set_name(u'anonymous')
                PyJs_Object_207_ = Js({u'key':Js(u'doOpen'),u'value':PyJs_anonymous_208_})
                @Js
                def PyJs_anonymous_210_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'n'])
                    @Js
                    def PyJsHoisted_n_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        PyJsComma(var.get(u'e').put(u'readyState', Js(u'paused')),var.get(u't')())
                    PyJsHoisted_n_.func_name = u'n'
                    var.put(u'n', PyJsHoisted_n_)
                    var.put(u'e', var.get(u"this"))
                    pass
                    if PyJsComma(var.get(u"this").put(u'readyState', Js(u'pausing')),(var.get(u"this").get(u'polling') or var.get(u"this").get(u'writable').neg())):
                        var.put(u'r', Js(0.0))
                        @Js
                        def PyJs_anonymous_211_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            (var.put(u'r',Js(var.get(u'r').to_number())-Js(1)) or var.get(u'n')())
                        PyJs_anonymous_211_._set_name(u'anonymous')
                        @Js
                        def PyJs_anonymous_212_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            (var.put(u'r',Js(var.get(u'r').to_number())-Js(1)) or var.get(u'n')())
                        PyJs_anonymous_212_._set_name(u'anonymous')
                        PyJsComma((var.get(u"this").get(u'polling') and PyJsComma((var.put(u'r',Js(var.get(u'r').to_number())+Js(1))-Js(1)),var.get(u"this").callprop(u'once', Js(u'pollComplete'), PyJs_anonymous_211_))),(var.get(u"this").get(u'writable') or PyJsComma((var.put(u'r',Js(var.get(u'r').to_number())+Js(1))-Js(1)),var.get(u"this").callprop(u'once', Js(u'drain'), PyJs_anonymous_212_))))
                    else:
                        var.get(u'n')()
                PyJs_anonymous_210_._set_name(u'anonymous')
                PyJs_Object_209_ = Js({u'key':Js(u'pause'),u'value':PyJs_anonymous_210_})
                @Js
                def PyJs_anonymous_214_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    PyJsComma(PyJsComma(var.get(u"this").put(u'polling', Js(0.0).neg()),var.get(u"this").callprop(u'doPoll')),var.get(u"this").callprop(u'emit', Js(u'poll')))
                PyJs_anonymous_214_._set_name(u'anonymous')
                PyJs_Object_213_ = Js({u'key':Js(u'poll'),u'value':PyJs_anonymous_214_})
                @Js
                def PyJs_anonymous_216_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    var.put(u'e', var.get(u"this"))
                    def PyJs_LONG_218_(var=var):
                        @Js
                        def PyJs_anonymous_217_(t, n, r, this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments, u'r':r, u't':t, u'n':n}, var)
                            var.registers([u'r', u't', u'n'])
                            if PyJsComma(((PyJsStrictEq(Js(u'opening'),var.get(u'e').get(u'readyState')) and PyJsStrictEq(Js(u'open'),var.get(u't').get(u'type'))) and var.get(u'e').callprop(u'onOpen')),PyJsStrictEq(Js(u'close'),var.get(u't').get(u'type'))):
                                return PyJsComma(var.get(u'e').callprop(u'onClose'),Js(1.0).neg())
                            var.get(u'e').callprop(u'onPacket', var.get(u't'))
                        PyJs_anonymous_217_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'l').callprop(u'decodePayload', var.get(u't'), var.get(u"this").get(u'socket').get(u'binaryType')).callprop(u'forEach', PyJs_anonymous_217_),(PyJsStrictNeq(Js(u'closed'),var.get(u"this").get(u'readyState')) and PyJsComma(PyJsComma(var.get(u"this").put(u'polling', Js(1.0).neg()),var.get(u"this").callprop(u'emit', Js(u'pollComplete'))),(PyJsStrictEq(Js(u'open'),var.get(u"this").get(u'readyState')) and var.get(u"this").callprop(u'poll')))))
                    PyJs_LONG_218_()
                PyJs_anonymous_216_._set_name(u'anonymous')
                PyJs_Object_215_ = Js({u'key':Js(u'onData'),u'value':PyJs_anonymous_216_})
                @Js
                def PyJs_anonymous_220_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    @Js
                    def PyJsHoisted_e_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        PyJs_Object_221_ = Js({u'type':Js(u'close')})
                        var.get(u't').callprop(u'write', Js([PyJs_Object_221_]))
                    PyJsHoisted_e_.func_name = u'e'
                    var.put(u'e', PyJsHoisted_e_)
                    var.put(u't', var.get(u"this"))
                    pass
                    (var.get(u'e')() if PyJsStrictEq(Js(u'open'),var.get(u"this").get(u'readyState')) else var.get(u"this").callprop(u'once', Js(u'open'), var.get(u'e')))
                PyJs_anonymous_220_._set_name(u'anonymous')
                PyJs_Object_219_ = Js({u'key':Js(u'doClose'),u'value':PyJs_anonymous_220_})
                @Js
                def PyJs_anonymous_223_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    var.put(u'e', var.get(u"this"))
                    @Js
                    def PyJs_anonymous_224_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        @Js
                        def PyJs_anonymous_225_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            PyJsComma(var.get(u'e').put(u'writable', Js(0.0).neg()),var.get(u'e').callprop(u'emit', Js(u'drain')))
                        PyJs_anonymous_225_._set_name(u'anonymous')
                        var.get(u'e').callprop(u'doWrite', var.get(u't'), PyJs_anonymous_225_)
                    PyJs_anonymous_224_._set_name(u'anonymous')
                    PyJsComma(var.get(u"this").put(u'writable', Js(1.0).neg()),var.get(u'l').callprop(u'encodePayload', var.get(u't'), PyJs_anonymous_224_))
                PyJs_anonymous_223_._set_name(u'anonymous')
                PyJs_Object_222_ = Js({u'key':Js(u'write'),u'value':PyJs_anonymous_223_})
                @Js
                def PyJs_anonymous_227_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    PyJs_Object_228_ = Js({})
                    var.put(u't', (var.get(u"this").get(u'query') or PyJs_Object_228_))
                    var.put(u'e', (Js(u'https') if var.get(u"this").get(u'opts').get(u'secure') else Js(u'http')))
                    var.put(u'n', Js(u''))
                    def PyJs_LONG_229_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma((PyJsStrictNeq(Js(1.0).neg(),var.get(u"this").get(u'opts').get(u'timestampRequests')) and var.get(u't').put(var.get(u"this").get(u'opts').get(u'timestampParam'), var.get(u'h')())),((var.get(u"this").get(u'supportsBinary') or var.get(u't').get(u'sid')) or var.get(u't').put(u'b64', Js(1.0)))),var.put(u't', var.get(u'p').callprop(u'encode', var.get(u't')))),((var.get(u"this").get(u'opts').get(u'port') and ((PyJsStrictEq(Js(u'https'),var.get(u'e')) and PyJsStrictNeq(Js(443.0),var.get(u'Number')(var.get(u"this").get(u'opts').get(u'port')))) or (PyJsStrictEq(Js(u'http'),var.get(u'e')) and PyJsStrictNeq(Js(80.0),var.get(u'Number')(var.get(u"this").get(u'opts').get(u'port')))))) and var.put(u'n', (Js(u':')+var.get(u"this").get(u'opts').get(u'port'))))),(var.get(u't').get(u'length') and var.put(u't', (Js(u'?')+var.get(u't'))))),(((((var.get(u'e')+Js(u'://'))+(((Js(u'[')+var.get(u"this").get(u'opts').get(u'hostname'))+Js(u']')) if PyJsStrictNeq((-Js(1.0)),var.get(u"this").get(u'opts').get(u'hostname').callprop(u'indexOf', Js(u':'))) else var.get(u"this").get(u'opts').get(u'hostname')))+var.get(u'n'))+var.get(u"this").get(u'opts').get(u'path'))+var.get(u't')))
                    return PyJs_LONG_229_()
                PyJs_anonymous_227_._set_name(u'anonymous')
                PyJs_Object_226_ = Js({u'key':Js(u'uri'),u'value':PyJs_anonymous_227_})
                @Js
                def PyJs_anonymous_231_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return Js(u'polling')
                PyJs_anonymous_231_._set_name(u'anonymous')
                PyJs_Object_230_ = Js({u'key':Js(u'name'),u'get':PyJs_anonymous_231_})
                return PyJsComma(PyJsComma(PyJsComma(var.put(u'e', var.get(u'u')),(var.put(u'n', Js([PyJs_Object_207_, PyJs_Object_209_, PyJs_Object_213_, PyJs_Object_215_, PyJs_Object_219_, PyJs_Object_222_, PyJs_Object_226_, PyJs_Object_230_])) and var.get(u'i')(var.get(u'e').get(u'prototype'), var.get(u'n')))),(var.get(u'r') and var.get(u'i')(var.get(u'e'), var.get(u'r')))),var.get(u'u'))
            PyJs_anonymous_203_._set_name(u'anonymous')
            var.put(u'y', PyJs_anonymous_203_(var.get(u'f')))
            var.get(u't').put(u'exports', var.get(u'y'))
        PyJs_anonymous_194_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_232_(t, e, this, arguments, var=var):
            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
            var.registers([u'r', u'e', u't', u'n'])
            var.put(u'n', var.get(u'Object').callprop(u'create', var.get(u"null")))
            PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'n').put(u'open', Js(u'0')),var.get(u'n').put(u'close', Js(u'1'))),var.get(u'n').put(u'ping', Js(u'2'))),var.get(u'n').put(u'pong', Js(u'3'))),var.get(u'n').put(u'message', Js(u'4'))),var.get(u'n').put(u'upgrade', Js(u'5'))),var.get(u'n').put(u'noop', Js(u'6')))
            var.put(u'r', var.get(u'Object').callprop(u'create', var.get(u"null")))
            @Js
            def PyJs_anonymous_233_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                var.get(u'r').put(var.get(u'n').get(var.get(u't')), var.get(u't'))
            PyJs_anonymous_233_._set_name(u'anonymous')
            var.get(u'Object').callprop(u'keys', var.get(u'n')).callprop(u'forEach', PyJs_anonymous_233_)
            PyJs_Object_235_ = Js({u'type':Js(u'error'),u'data':Js(u'parser error')})
            PyJs_Object_234_ = Js({u'PACKET_TYPES':var.get(u'n'),u'PACKET_TYPES_REVERSE':var.get(u'r'),u'ERROR_PACKET':PyJs_Object_235_})
            var.get(u't').put(u'exports', PyJs_Object_234_)
        PyJs_anonymous_232_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_236_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'i', u'o', u'n', u's', u'r', u'u', u't'])
            @Js
            def PyJsHoisted_a_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                var.put(u'e', Js(u''))
                while 1:
                    PyJsComma(var.put(u'e', (var.get(u'o').get((var.get(u't')%Js(64.0)))+var.get(u'e'))),var.put(u't', var.get(u'Math').callprop(u'floor', (var.get(u't')/Js(64.0)))))
                    if not (var.get(u't')>Js(0.0)):
                        break
                return var.get(u'e')
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_u_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u't'])
                var.put(u't', var.get(u'a')((+var.get(u'Date').create())))
                return (PyJsComma(var.put(u's', Js(0.0)),var.put(u'r', var.get(u't'))) if PyJsStrictNeq(var.get(u't'),var.get(u'r')) else ((var.get(u't')+Js(u'.'))+var.get(u'a')((var.put(u's',Js(var.get(u's').to_number())+Js(1))-Js(1)))))
            PyJsHoisted_u_.func_name = u'u'
            var.put(u'u', PyJsHoisted_u_)
            Js(u'use strict')
            var.put(u'o', Js(u'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_').callprop(u'split', Js(u'')))
            PyJs_Object_237_ = Js({})
            var.put(u'i', PyJs_Object_237_)
            var.put(u's', Js(0.0))
            var.put(u'c', Js(0.0))
            pass
            pass
            #for JS loop
            
            while (var.get(u'c')<Js(64.0)):
                try:
                    var.get(u'i').put(var.get(u'o').get(var.get(u'c')), var.get(u'c'))
                finally:
                        (var.put(u'c',Js(var.get(u'c').to_number())+Js(1))-Js(1))
            @Js
            def PyJs_anonymous_238_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                var.put(u'e', Js(0.0))
                #for JS loop
                var.put(u'c', Js(0.0))
                while (var.get(u'c')<var.get(u't').get(u'length')):
                    try:
                        var.put(u'e', ((Js(64.0)*var.get(u'e'))+var.get(u'i').get(var.get(u't').callprop(u'charAt', var.get(u'c')))))
                    finally:
                            (var.put(u'c',Js(var.get(u'c').to_number())+Js(1))-Js(1))
                return var.get(u'e')
            PyJs_anonymous_238_._set_name(u'anonymous')
            PyJsComma(PyJsComma(var.get(u'u').put(u'encode', var.get(u'a')),var.get(u'u').put(u'decode', PyJs_anonymous_238_)),var.get(u't').put(u'exports', var.get(u'u')))
        PyJs_anonymous_236_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_239_(t, e, this, arguments, var=var):
            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
            var.registers([u'e', u't'])
            @Js
            def PyJs_anonymous_240_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'e', var.get(u'arguments').get(u'length'))
                var.put(u'n', var.get(u'Array').create(((var.get(u'e')-Js(1.0)) if (var.get(u'e')>Js(1.0)) else Js(0.0))))
                var.put(u'r', Js(1.0))
                while (var.get(u'r')<var.get(u'e')):
                    try:
                        var.get(u'n').put((var.get(u'r')-Js(1.0)), var.get(u'arguments').get(var.get(u'r')))
                    finally:
                            (var.put(u'r',Js(var.get(u'r').to_number())+Js(1))-Js(1))
                @Js
                def PyJs_anonymous_241_(e, n, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u'arguments':arguments, u'n':n}, var)
                    var.registers([u'e', u'n'])
                    return PyJsComma((var.get(u't').callprop(u'hasOwnProperty', var.get(u'n')) and var.get(u'e').put(var.get(u'n'), var.get(u't').get(var.get(u'n')))),var.get(u'e'))
                PyJs_anonymous_241_._set_name(u'anonymous')
                PyJs_Object_242_ = Js({})
                return var.get(u'n').callprop(u'reduce', PyJs_anonymous_241_, PyJs_Object_242_)
            PyJs_anonymous_240_._set_name(u'anonymous')
            var.get(u't').get(u'exports').put(u'pick', PyJs_anonymous_240_)
        PyJs_anonymous_239_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_243_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'd', u'f', u'i', u'h', u'l', u'o', u'n', u'p', u's', u'r', u'u', u't', u'v', u'y'])
            @Js
            def PyJsHoisted_a_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_260_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_260_._set_name(u'anonymous')
                return var.put(u'a', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_260_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, e, n, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                var.registers([u'e', u't', u'n'])
                @Js
                def PyJs_anonymous_258_(t, e, n, this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                    var.registers([u'r', u'e', u't', u'o', u'n'])
                    @Js
                    def PyJs_anonymous_259_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        #for JS loop
                        
                        while (var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u't'), var.get(u'e')).neg() and PyJsStrictNeq(var.get(u"null"),var.put(u't', var.get(u'p')(var.get(u't'))))):
                            pass
                        
                        return var.get(u't')
                    PyJs_anonymous_259_._set_name(u'anonymous')
                    var.put(u'r', PyJs_anonymous_259_(var.get(u't'), var.get(u'e')))
                    if var.get(u'r'):
                        var.put(u'o', var.get(u'Object').callprop(u'getOwnPropertyDescriptor', var.get(u'r'), var.get(u'e')))
                        return (var.get(u'o').get(u'get').callprop(u'call', var.get(u'n')) if var.get(u'o').get(u'get') else var.get(u'o').get(u'value'))
                PyJs_anonymous_258_._set_name(u'anonymous')
                return var.put(u'c', (var.get(u'Reflect').get(u'get') if ((Js(u'undefined')!=var.get(u'Reflect',throw=False).typeof()) and var.get(u'Reflect').get(u'get')) else PyJs_anonymous_258_))(var.get(u't'), var.get(u'e'), (var.get(u'n') or var.get(u't')))
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_f_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_264_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                        PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                        raise PyJsTempException
                    return var.get(u't')
                PyJs_anonymous_264_._set_name(u'anonymous')
                return (PyJs_anonymous_264_(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_f_.func_name = u'f'
            var.put(u'f', PyJsHoisted_f_)
            @Js
            def PyJsHoisted_i_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                (((var.get(u"null")==var.get(u'e')) or (var.get(u'e')>var.get(u't').get(u'length'))) and var.put(u'e', var.get(u't').get(u'length')))
                #for JS loop
                var.put(u'n', Js(0.0))
                var.put(u'r', var.get(u'Array').create(var.get(u'e')))
                while (var.get(u'n')<var.get(u'e')):
                    try:
                        var.get(u'r').put(var.get(u'n'), var.get(u't').get(var.get(u'n')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
                return var.get(u'r')
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_o_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'c', u'e', u'o', u'n', u's', u'r', u't'])
                pass
                if ((Js(u'undefined')==var.get(u'Symbol',throw=False).typeof()) or (var.get(u"null")==var.get(u't').get(var.get(u'Symbol').get(u'iterator')))):
                    @Js
                    def PyJs_anonymous_246_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        if var.get(u't').neg():
                            return var.get('undefined')
                        if (Js(u'string')==var.get(u't',throw=False).typeof()):
                            return var.get(u'i')(var.get(u't'), var.get(u'e'))
                        var.put(u'n', var.get(u'Object').get(u'prototype').get(u'toString').callprop(u'call', var.get(u't')).callprop(u'slice', Js(8.0), (-Js(1.0))))
                        ((PyJsStrictEq(Js(u'Object'),var.get(u'n')) and var.get(u't').get(u'constructor')) and var.put(u'n', var.get(u't').get(u'constructor').get(u'name')))
                        if (PyJsStrictEq(Js(u'Map'),var.get(u'n')) or PyJsStrictEq(Js(u'Set'),var.get(u'n'))):
                            return var.get(u'Array').callprop(u'from', var.get(u't'))
                        if (PyJsStrictEq(Js(u'Arguments'),var.get(u'n')) or JsRegExp(u'/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/').callprop(u'test', var.get(u'n'))):
                            return var.get(u'i')(var.get(u't'), var.get(u'e'))
                    PyJs_anonymous_246_._set_name(u'anonymous')
                    if ((var.get(u'Array').callprop(u'isArray', var.get(u't')) or var.put(u'n', PyJs_anonymous_246_(var.get(u't')))) or ((var.get(u'e') and var.get(u't')) and (Js(u'number')==var.get(u't').get(u'length').typeof()))):
                        (var.get(u'n') and var.put(u't', var.get(u'n')))
                        var.put(u'r', Js(0.0))
                        @Js
                        def PyJs_anonymous_247_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_247_._set_name(u'anonymous')
                        var.put(u'o', PyJs_anonymous_247_)
                        @Js
                        def PyJs_anonymous_249_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            PyJs_Object_250_ = Js({u'done':Js(0.0).neg()})
                            PyJs_Object_251_ = Js({u'done':Js(1.0).neg(),u'value':var.get(u't').get((var.put(u'r',Js(var.get(u'r').to_number())+Js(1))-Js(1)))})
                            return (PyJs_Object_250_ if (var.get(u'r')>=var.get(u't').get(u'length')) else PyJs_Object_251_)
                        PyJs_anonymous_249_._set_name(u'anonymous')
                        @Js
                        def PyJs_anonymous_252_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u't'])
                            PyJsTempException = JsToPyException(var.get(u't'))
                            raise PyJsTempException
                        PyJs_anonymous_252_._set_name(u'anonymous')
                        PyJs_Object_248_ = Js({u's':var.get(u'o'),u'n':PyJs_anonymous_249_,u'e':PyJs_anonymous_252_,u'f':var.get(u'o')})
                        return PyJs_Object_248_
                    PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.')))
                    raise PyJsTempException
                var.put(u'c', Js(0.0).neg())
                var.put(u'a', Js(1.0).neg())
                @Js
                def PyJs_anonymous_254_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    var.put(u'n', var.get(u't').callprop(var.get(u'Symbol').get(u'iterator')))
                PyJs_anonymous_254_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_255_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u't'])
                    var.put(u't', var.get(u'n').callprop(u'next'))
                    return PyJsComma(var.put(u'c', var.get(u't').get(u'done')),var.get(u't'))
                PyJs_anonymous_255_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_256_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    PyJsComma(var.put(u'a', Js(0.0).neg()),var.put(u's', var.get(u't')))
                PyJs_anonymous_256_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_257_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    try:
                        ((var.get(u'c') or (var.get(u"null")==var.get(u'n').get(u'return'))) or var.get(u'n').callprop(u'return'))
                    finally:
                        if var.get(u'a'):
                            PyJsTempException = JsToPyException(var.get(u's'))
                            raise PyJsTempException
                PyJs_anonymous_257_._set_name(u'anonymous')
                PyJs_Object_253_ = Js({u's':PyJs_anonymous_254_,u'n':PyJs_anonymous_255_,u'e':PyJs_anonymous_256_,u'f':PyJs_anonymous_257_})
                return PyJs_Object_253_
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_p_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_265_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_265_._set_name(u'anonymous')
                return var.put(u'p', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_265_))(var.get(u't'))
            PyJsHoisted_p_.func_name = u'p'
            var.put(u'p', PyJsHoisted_p_)
            @Js
            def PyJsHoisted_s_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_244_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_244_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_245_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_245_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_244_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_245_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            @Js
            def PyJsHoisted_u_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_261_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_262_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_262_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_262_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_91676982 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_91676982 is not None:
                                var.own[u't'] = PyJsHolder_74_91676982
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_91676982
                PyJs_anonymous_261_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_261_())
                @Js
                def PyJs_anonymous_263_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'p')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'p')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'f')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_263_._set_name(u'anonymous')
                return PyJs_anonymous_263_
            PyJsHoisted_u_.func_name = u'u'
            var.put(u'u', PyJsHoisted_u_)
            Js(u'use strict')
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            PyJs_Object_266_ = Js({u'value':Js(0.0).neg()})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'__esModule'), PyJs_Object_266_),var.get(u'e').put(u'Socket', PyJsComma(Js(0.0), Js(None))))
            var.put(u'l', var.get(u'n')(Js(5.0)))
            var.put(u'h', var.get(u'n')(Js(0.0)))
            var.put(u'y', var.get(u'n')(Js(16.0)))
            PyJs_Object_267_ = Js({u'connect':Js(1.0),u'connect_error':Js(1.0),u'disconnect':Js(1.0),u'disconnecting':Js(1.0),u'newListener':Js(1.0),u'removeListener':Js(1.0)})
            var.put(u'd', var.get(u'Object').callprop(u'freeze', PyJs_Object_267_))
            @Js
            def PyJs_anonymous_268_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u'f', u'i', u'n', u'r', u't'])
                @Js
                def PyJsHoisted_f_(t, e, n, this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                    var.registers([u'r', u'e', u't', u'n'])
                    pass
                    def PyJs_LONG_277_(var=var):
                        @Js
                        def PyJs_anonymous_272_(t, e, this, arguments, var=var):
                            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                            var.registers([u'e', u't'])
                            if var.get(u't').instanceof(var.get(u'e')).neg():
                                PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                                raise PyJsTempException
                        PyJs_anonymous_272_._set_name(u'anonymous')
                        PyJs_Object_273_ = Js({})
                        PyJs_Object_274_ = Js({})
                        PyJs_Object_275_ = Js({})
                        PyJs_Object_276_ = Js({})
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJs_anonymous_272_(var.get(u"this"), var.get(u'f')),var.put(u'r', var.get(u'i').callprop(u'call', var.get(u"this"))).put(u'receiveBuffer', Js([]))),var.get(u'r').put(u'sendBuffer', Js([]))),var.get(u'r').put(u'ids', Js(0.0))),var.get(u'r').put(u'acks', PyJs_Object_273_)),var.get(u'r').put(u'flags', PyJs_Object_274_)),var.get(u'r').put(u'io', var.get(u't'))),var.get(u'r').put(u'nsp', var.get(u'e'))),var.get(u'r').put(u'ids', Js(0.0))),var.get(u'r').put(u'acks', PyJs_Object_275_)),var.get(u'r').put(u'receiveBuffer', Js([]))),var.get(u'r').put(u'sendBuffer', Js([]))),var.get(u'r').put(u'connected', Js(1.0).neg())),var.get(u'r').put(u'disconnected', Js(0.0).neg())),var.get(u'r').put(u'flags', PyJs_Object_276_)),((var.get(u'n') and var.get(u'n').get(u'auth')) and var.get(u'r').put(u'auth', var.get(u'n').get(u'auth')))),(var.get(u'r').get(u'io').get(u'_autoConnect') and var.get(u'r').callprop(u'open'))),var.get(u'r'))
                    return PyJs_LONG_277_()
                PyJsHoisted_f_.func_name = u'f'
                var.put(u'f', PyJsHoisted_f_)
                @Js
                def PyJs_anonymous_269_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                        PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                        raise PyJsTempException
                    PyJs_Object_271_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                    PyJs_Object_270_ = Js({u'constructor':PyJs_Object_271_})
                    PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_270_)),(var.get(u'e') and var.get(u'a')(var.get(u't'), var.get(u'e'))))
                PyJs_anonymous_269_._set_name(u'anonymous')
                PyJs_anonymous_269_(var.get(u'f'), var.get(u't')).neg()
                var.put(u'i', var.get(u'u')(var.get(u'f')))
                pass
                def PyJs_LONG_346_(var=var):
                    @Js
                    def PyJs_anonymous_279_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u't'])
                        if var.get(u"this").get(u'subs').neg():
                            var.put(u't', var.get(u"this").get(u'io'))
                            def PyJs_LONG_280_(var=var):
                                return var.get(u"this").put(u'subs', Js([var.get(u'y').callprop(u'on', var.get(u't'), Js(u'open'), var.get(u"this").get(u'onopen').callprop(u'bind', var.get(u"this"))), var.get(u'y').callprop(u'on', var.get(u't'), Js(u'packet'), var.get(u"this").get(u'onpacket').callprop(u'bind', var.get(u"this"))), var.get(u'y').callprop(u'on', var.get(u't'), Js(u'error'), var.get(u"this").get(u'onerror').callprop(u'bind', var.get(u"this"))), var.get(u'y').callprop(u'on', var.get(u't'), Js(u'close'), var.get(u"this").get(u'onclose').callprop(u'bind', var.get(u"this")))]))
                            PyJs_LONG_280_()
                    PyJs_anonymous_279_._set_name(u'anonymous')
                    PyJs_Object_278_ = Js({u'key':Js(u'subEvents'),u'value':PyJs_anonymous_279_})
                    @Js
                    def PyJs_anonymous_282_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return PyJsComma((var.get(u"this").get(u'connected') or PyJsComma(PyJsComma(var.get(u"this").callprop(u'subEvents'),(var.get(u"this").get(u'io').get(u'_reconnecting') or var.get(u"this").get(u'io').callprop(u'open'))),(PyJsStrictEq(Js(u'open'),var.get(u"this").get(u'io').get(u'_readyState')) and var.get(u"this").callprop(u'onopen')))),var.get(u"this"))
                    PyJs_anonymous_282_._set_name(u'anonymous')
                    PyJs_Object_281_ = Js({u'key':Js(u'connect'),u'value':PyJs_anonymous_282_})
                    @Js
                    def PyJs_anonymous_284_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return var.get(u"this").callprop(u'connect')
                    PyJs_anonymous_284_._set_name(u'anonymous')
                    PyJs_Object_283_ = Js({u'key':Js(u'open'),u'value':PyJs_anonymous_284_})
                    @Js
                    def PyJs_anonymous_286_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        #for JS loop
                        var.put(u't', var.get(u'arguments').get(u'length'))
                        var.put(u'e', var.get(u'Array').create(var.get(u't')))
                        var.put(u'n', Js(0.0))
                        while (var.get(u'n')<var.get(u't')):
                            try:
                                var.get(u'e').put(var.get(u'n'), var.get(u'arguments').get(var.get(u'n')))
                            finally:
                                    (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
                        return PyJsComma(PyJsComma(var.get(u'e').callprop(u'unshift', Js(u'message')),var.get(u"this").get(u'emit').callprop(u'apply', var.get(u"this"), var.get(u'e'))),var.get(u"this"))
                    PyJs_anonymous_286_._set_name(u'anonymous')
                    PyJs_Object_285_ = Js({u'key':Js(u'send'),u'value':PyJs_anonymous_286_})
                    @Js
                    def PyJs_anonymous_288_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u'i', u'o', u'n', u's', u'r', u't'])
                        if var.get(u'd').callprop(u'hasOwnProperty', var.get(u't')):
                            PyJsTempException = JsToPyException(var.get(u'Error').create(((Js(u'"')+var.get(u't'))+Js(u'" is a reserved event name'))))
                            raise PyJsTempException
                        #for JS loop
                        var.put(u'e', var.get(u'arguments').get(u'length'))
                        var.put(u'n', var.get(u'Array').create(((var.get(u'e')-Js(1.0)) if (var.get(u'e')>Js(1.0)) else Js(0.0))))
                        var.put(u'r', Js(1.0))
                        while (var.get(u'r')<var.get(u'e')):
                            try:
                                var.get(u'n').put((var.get(u'r')-Js(1.0)), var.get(u'arguments').get(var.get(u'r')))
                            finally:
                                    (var.put(u'r',Js(var.get(u'r').to_number())+Js(1))-Js(1))
                        var.get(u'n').callprop(u'unshift', var.get(u't'))
                        PyJs_Object_290_ = Js({})
                        PyJs_Object_289_ = Js({u'type':var.get(u'l').get(u'PacketType').get(u'EVENT'),u'data':var.get(u'n'),u'options':PyJs_Object_290_})
                        var.put(u'o', PyJs_Object_289_)
                        def PyJs_LONG_291_(var=var):
                            return PyJsComma(var.get(u'o').get(u'options').put(u'compress', PyJsStrictNeq(Js(1.0).neg(),var.get(u"this").get(u'flags').get(u'compress'))),((Js(u'function')==var.get(u'n').get((var.get(u'n').get(u'length')-Js(1.0))).typeof()) and PyJsComma(var.get(u"this").get(u'acks').put(var.get(u"this").get(u'ids'), var.get(u'n').callprop(u'pop')),var.get(u'o').put(u'id', (var.get(u"this").put(u'ids',Js(var.get(u"this").get(u'ids').to_number())+Js(1))-Js(1))))))
                        PyJs_LONG_291_()
                        var.put(u'i', ((var.get(u"this").get(u'io').get(u'engine') and var.get(u"this").get(u'io').get(u'engine').get(u'transport')) and var.get(u"this").get(u'io').get(u'engine').get(u'transport').get(u'writable')))
                        var.put(u's', (var.get(u"this").get(u'flags').get(u'volatile') and (var.get(u'i').neg() or var.get(u"this").get(u'connected').neg())))
                        PyJs_Object_292_ = Js({})
                        return PyJsComma(PyJsComma((var.get(u's') or (var.get(u"this").callprop(u'packet', var.get(u'o')) if var.get(u"this").get(u'connected') else var.get(u"this").get(u'sendBuffer').callprop(u'push', var.get(u'o')))),var.get(u"this").put(u'flags', PyJs_Object_292_)),var.get(u"this"))
                    PyJs_anonymous_288_._set_name(u'anonymous')
                    PyJs_Object_287_ = Js({u'key':Js(u'emit'),u'value':PyJs_anonymous_288_})
                    @Js
                    def PyJs_anonymous_294_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        PyJsComma(var.get(u't').put(u'nsp', var.get(u"this").get(u'nsp')),var.get(u"this").get(u'io').callprop(u'_packet', var.get(u't')))
                    PyJs_anonymous_294_._set_name(u'anonymous')
                    PyJs_Object_293_ = Js({u'key':Js(u'packet'),u'value':PyJs_anonymous_294_})
                    @Js
                    def PyJs_anonymous_296_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.put(u't', var.get(u"this"))
                        @Js
                        def PyJs_anonymous_297_(e, this, arguments, var=var):
                            var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                            var.registers([u'e'])
                            PyJs_Object_298_ = Js({u'type':var.get(u'l').get(u'PacketType').get(u'CONNECT'),u'data':var.get(u'e')})
                            var.get(u't').callprop(u'packet', PyJs_Object_298_)
                        PyJs_anonymous_297_._set_name(u'anonymous')
                        PyJs_Object_299_ = Js({u'type':var.get(u'l').get(u'PacketType').get(u'CONNECT'),u'data':var.get(u"this").get(u'auth')})
                        (var.get(u"this").callprop(u'auth', PyJs_anonymous_297_) if (Js(u'function')==var.get(u"this").get(u'auth').typeof()) else var.get(u"this").callprop(u'packet', PyJs_Object_299_))
                    PyJs_anonymous_296_._set_name(u'anonymous')
                    PyJs_Object_295_ = Js({u'key':Js(u'onopen'),u'value':PyJs_anonymous_296_})
                    @Js
                    def PyJs_anonymous_301_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        (var.get(u"this").get(u'connected') or var.get(u'c')(var.get(u'p')(var.get(u'f').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'connect_error'), var.get(u't')))
                    PyJs_anonymous_301_._set_name(u'anonymous')
                    PyJs_Object_300_ = Js({u'key':Js(u'onerror'),u'value':PyJs_anonymous_301_})
                    @Js
                    def PyJs_anonymous_303_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put(u'connected', Js(1.0).neg()),var.get(u"this").put(u'disconnected', Js(0.0).neg())),var.get(u"this").delete(u'id')),var.get(u'c')(var.get(u'p')(var.get(u'f').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'disconnect'), var.get(u't')))
                    PyJs_anonymous_303_._set_name(u'anonymous')
                    PyJs_Object_302_ = Js({u'key':Js(u'onclose'),u'value':PyJs_anonymous_303_})
                    @Js
                    def PyJs_anonymous_305_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        if PyJsStrictEq(var.get(u't').get(u'nsp'),var.get(u"this").get(u'nsp')):
                            while 1:
                                SWITCHED = False
                                CONDITION = (var.get(u't').get(u'type'))
                                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'PacketType').get(u'CONNECT')):
                                    SWITCHED = True
                                    if (var.get(u't').get(u'data') and var.get(u't').get(u'data').get(u'sid')):
                                        var.put(u'e', var.get(u't').get(u'data').get(u'sid'))
                                        var.get(u"this").callprop(u'onconnect', var.get(u'e'))
                                    else:
                                        var.get(u'c')(var.get(u'p')(var.get(u'f').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'connect_error'), var.get(u'Error').create(Js(u'It seems you are trying to reach a Socket.IO server in v2.x with a v3.x client, but they are not compatible (more information here: https://socket.io/docs/v3/migrating-from-2-x-to-3-0/)')))
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'PacketType').get(u'EVENT')):
                                    SWITCHED = True
                                    pass
                                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'PacketType').get(u'BINARY_EVENT')):
                                    SWITCHED = True
                                    var.get(u"this").callprop(u'onevent', var.get(u't'))
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'PacketType').get(u'ACK')):
                                    SWITCHED = True
                                    pass
                                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'PacketType').get(u'BINARY_ACK')):
                                    SWITCHED = True
                                    var.get(u"this").callprop(u'onack', var.get(u't'))
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'PacketType').get(u'DISCONNECT')):
                                    SWITCHED = True
                                    var.get(u"this").callprop(u'ondisconnect')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u'l').get(u'PacketType').get(u'CONNECT_ERROR')):
                                    SWITCHED = True
                                    var.put(u'n', var.get(u'Error').create(var.get(u't').get(u'data').get(u'message')))
                                    PyJsComma(var.get(u'n').put(u'data', var.get(u't').get(u'data').get(u'data')),var.get(u'c')(var.get(u'p')(var.get(u'f').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'connect_error'), var.get(u'n')))
                                SWITCHED = True
                                break
                    PyJs_anonymous_305_._set_name(u'anonymous')
                    PyJs_Object_304_ = Js({u'key':Js(u'onpacket'),u'value':PyJs_anonymous_305_})
                    @Js
                    def PyJs_anonymous_307_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        var.put(u'e', (var.get(u't').get(u'data') or Js([])))
                        PyJsComma(((var.get(u"null")!=var.get(u't').get(u'id')) and var.get(u'e').callprop(u'push', var.get(u"this").callprop(u'ack', var.get(u't').get(u'id')))),(var.get(u"this").callprop(u'emitEvent', var.get(u'e')) if var.get(u"this").get(u'connected') else var.get(u"this").get(u'receiveBuffer').callprop(u'push', var.get(u'Object').callprop(u'freeze', var.get(u'e')))))
                    PyJs_anonymous_307_._set_name(u'anonymous')
                    PyJs_Object_306_ = Js({u'key':Js(u'onevent'),u'value':PyJs_anonymous_307_})
                    @Js
                    def PyJs_anonymous_309_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        if (var.get(u"this").get(u'_anyListeners') and var.get(u"this").get(u'_anyListeners').get(u'length')):
                            var.put(u'n', var.get(u'o')(var.get(u"this").get(u'_anyListeners').callprop(u'slice')))
                            try:
                                #for JS loop
                                var.get(u'n').callprop(u's')
                                while var.put(u'e', var.get(u'n').callprop(u'n')).get(u'done').neg():
                                    var.get(u'e').get(u'value').callprop(u'apply', var.get(u"this"), var.get(u't'))
                                
                            except PyJsException as PyJsTempException:
                                PyJsHolder_74_98644242 = var.own.get(u't')
                                var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                                try:
                                    var.get(u'n').callprop(u'e', var.get(u't'))
                                finally:
                                    if PyJsHolder_74_98644242 is not None:
                                        var.own[u't'] = PyJsHolder_74_98644242
                                    else:
                                        del var.own[u't']
                                    del PyJsHolder_74_98644242
                            finally:
                                var.get(u'n').callprop(u'f')
                        var.get(u'c')(var.get(u'p')(var.get(u'f').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'apply', var.get(u"this"), var.get(u't'))
                    PyJs_anonymous_309_._set_name(u'anonymous')
                    PyJs_Object_308_ = Js({u'key':Js(u'emitEvent'),u'value':PyJs_anonymous_309_})
                    @Js
                    def PyJs_anonymous_311_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        var.put(u'e', var.get(u"this"))
                        var.put(u'n', Js(1.0).neg())
                        @Js
                        def PyJs_anonymous_312_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([u'i', u'r', u'o'])
                            if var.get(u'n').neg():
                                var.put(u'n', Js(0.0).neg())
                                #for JS loop
                                var.put(u'r', var.get(u'arguments').get(u'length'))
                                var.put(u'o', var.get(u'Array').create(var.get(u'r')))
                                var.put(u'i', Js(0.0))
                                while (var.get(u'i')<var.get(u'r')):
                                    try:
                                        var.get(u'o').put(var.get(u'i'), var.get(u'arguments').get(var.get(u'i')))
                                    finally:
                                            (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
                                PyJs_Object_313_ = Js({u'type':var.get(u'l').get(u'PacketType').get(u'ACK'),u'id':var.get(u't'),u'data':var.get(u'o')})
                                var.get(u'e').callprop(u'packet', PyJs_Object_313_)
                        PyJs_anonymous_312_._set_name(u'anonymous')
                        return PyJs_anonymous_312_
                    PyJs_anonymous_311_._set_name(u'anonymous')
                    PyJs_Object_310_ = Js({u'key':Js(u'ack'),u'value':PyJs_anonymous_311_})
                    @Js
                    def PyJs_anonymous_315_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        var.put(u'e', var.get(u"this").get(u'acks').get(var.get(u't').get(u'id')))
                        ((Js(u'function')==var.get(u'e',throw=False).typeof()) and PyJsComma(var.get(u'e').callprop(u'apply', var.get(u"this"), var.get(u't').get(u'data')),var.get(u"this").get(u'acks').delete(var.get(u't').get(u'id'))))
                    PyJs_anonymous_315_._set_name(u'anonymous')
                    PyJs_Object_314_ = Js({u'key':Js(u'onack'),u'value':PyJs_anonymous_315_})
                    @Js
                    def PyJs_anonymous_317_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put(u'id', var.get(u't')),var.get(u"this").put(u'connected', Js(0.0).neg())),var.get(u"this").put(u'disconnected', Js(1.0).neg())),var.get(u'c')(var.get(u'p')(var.get(u'f').get(u'prototype')), Js(u'emit'), var.get(u"this")).callprop(u'call', var.get(u"this"), Js(u'connect'))),var.get(u"this").callprop(u'emitBuffered'))
                    PyJs_anonymous_317_._set_name(u'anonymous')
                    PyJs_Object_316_ = Js({u'key':Js(u'onconnect'),u'value':PyJs_anonymous_317_})
                    @Js
                    def PyJs_anonymous_319_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.put(u't', var.get(u"this"))
                        @Js
                        def PyJs_anonymous_320_(e, this, arguments, var=var):
                            var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                            var.registers([u'e'])
                            return var.get(u't').callprop(u'emitEvent', var.get(u'e'))
                        PyJs_anonymous_320_._set_name(u'anonymous')
                        @Js
                        def PyJs_anonymous_321_(e, this, arguments, var=var):
                            var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                            var.registers([u'e'])
                            return var.get(u't').callprop(u'packet', var.get(u'e'))
                        PyJs_anonymous_321_._set_name(u'anonymous')
                        PyJsComma(PyJsComma(PyJsComma(var.get(u"this").get(u'receiveBuffer').callprop(u'forEach', PyJs_anonymous_320_),var.get(u"this").put(u'receiveBuffer', Js([]))),var.get(u"this").get(u'sendBuffer').callprop(u'forEach', PyJs_anonymous_321_)),var.get(u"this").put(u'sendBuffer', Js([])))
                    PyJs_anonymous_319_._set_name(u'anonymous')
                    PyJs_Object_318_ = Js({u'key':Js(u'emitBuffered'),u'value':PyJs_anonymous_319_})
                    @Js
                    def PyJs_anonymous_323_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        PyJsComma(var.get(u"this").callprop(u'destroy'),var.get(u"this").callprop(u'onclose', Js(u'io server disconnect')))
                    PyJs_anonymous_323_._set_name(u'anonymous')
                    PyJs_Object_322_ = Js({u'key':Js(u'ondisconnect'),u'value':PyJs_anonymous_323_})
                    @Js
                    def PyJs_anonymous_325_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        @Js
                        def PyJs_anonymous_326_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u't'])
                            return var.get(u't')()
                        PyJs_anonymous_326_._set_name(u'anonymous')
                        PyJsComma((var.get(u"this").get(u'subs') and PyJsComma(var.get(u"this").get(u'subs').callprop(u'forEach', PyJs_anonymous_326_),var.get(u"this").put(u'subs', PyJsComma(Js(0.0), Js(None))))),var.get(u"this").get(u'io').callprop(u'_destroy', var.get(u"this")))
                    PyJs_anonymous_325_._set_name(u'anonymous')
                    PyJs_Object_324_ = Js({u'key':Js(u'destroy'),u'value':PyJs_anonymous_325_})
                    @Js
                    def PyJs_anonymous_328_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        PyJs_Object_329_ = Js({u'type':var.get(u'l').get(u'PacketType').get(u'DISCONNECT')})
                        return PyJsComma(PyJsComma(PyJsComma((var.get(u"this").get(u'connected') and var.get(u"this").callprop(u'packet', PyJs_Object_329_)),var.get(u"this").callprop(u'destroy')),(var.get(u"this").get(u'connected') and var.get(u"this").callprop(u'onclose', Js(u'io client disconnect')))),var.get(u"this"))
                    PyJs_anonymous_328_._set_name(u'anonymous')
                    PyJs_Object_327_ = Js({u'key':Js(u'disconnect'),u'value':PyJs_anonymous_328_})
                    @Js
                    def PyJs_anonymous_331_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return var.get(u"this").callprop(u'disconnect')
                    PyJs_anonymous_331_._set_name(u'anonymous')
                    PyJs_Object_330_ = Js({u'key':Js(u'close'),u'value':PyJs_anonymous_331_})
                    @Js
                    def PyJs_anonymous_333_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        return PyJsComma(var.get(u"this").get(u'flags').put(u'compress', var.get(u't')),var.get(u"this"))
                    PyJs_anonymous_333_._set_name(u'anonymous')
                    PyJs_Object_332_ = Js({u'key':Js(u'compress'),u'value':PyJs_anonymous_333_})
                    @Js
                    def PyJs_anonymous_335_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        return PyJsComma(PyJsComma(var.get(u"this").put(u'_anyListeners', (var.get(u"this").get(u'_anyListeners') or Js([]))),var.get(u"this").get(u'_anyListeners').callprop(u'push', var.get(u't'))),var.get(u"this"))
                    PyJs_anonymous_335_._set_name(u'anonymous')
                    PyJs_Object_334_ = Js({u'key':Js(u'onAny'),u'value':PyJs_anonymous_335_})
                    @Js
                    def PyJs_anonymous_337_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        return PyJsComma(PyJsComma(var.get(u"this").put(u'_anyListeners', (var.get(u"this").get(u'_anyListeners') or Js([]))),var.get(u"this").get(u'_anyListeners').callprop(u'unshift', var.get(u't'))),var.get(u"this"))
                    PyJs_anonymous_337_._set_name(u'anonymous')
                    PyJs_Object_336_ = Js({u'key':Js(u'prependAny'),u'value':PyJs_anonymous_337_})
                    @Js
                    def PyJs_anonymous_339_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        if var.get(u"this").get(u'_anyListeners').neg():
                            return var.get(u"this")
                        if var.get(u't'):
                            #for JS loop
                            var.put(u'e', var.get(u"this").get(u'_anyListeners'))
                            var.put(u'n', Js(0.0))
                            while (var.get(u'n')<var.get(u'e').get(u'length')):
                                try:
                                    if PyJsStrictEq(var.get(u't'),var.get(u'e').get(var.get(u'n'))):
                                        return PyJsComma(var.get(u'e').callprop(u'splice', var.get(u'n'), Js(1.0)),var.get(u"this"))
                                finally:
                                        (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
                        else:
                            var.get(u"this").put(u'_anyListeners', Js([]))
                        return var.get(u"this")
                    PyJs_anonymous_339_._set_name(u'anonymous')
                    PyJs_Object_338_ = Js({u'key':Js(u'offAny'),u'value':PyJs_anonymous_339_})
                    @Js
                    def PyJs_anonymous_341_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return (var.get(u"this").get(u'_anyListeners') or Js([]))
                    PyJs_anonymous_341_._set_name(u'anonymous')
                    PyJs_Object_340_ = Js({u'key':Js(u'listenersAny'),u'value':PyJs_anonymous_341_})
                    @Js
                    def PyJs_anonymous_343_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return var.get(u"this").get(u'subs').neg().neg()
                    PyJs_anonymous_343_._set_name(u'anonymous')
                    PyJs_Object_342_ = Js({u'key':Js(u'active'),u'get':PyJs_anonymous_343_})
                    @Js
                    def PyJs_anonymous_345_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return PyJsComma(var.get(u"this").get(u'flags').put(u'volatile', Js(0.0).neg()),var.get(u"this"))
                    PyJs_anonymous_345_._set_name(u'anonymous')
                    PyJs_Object_344_ = Js({u'key':Js(u'volatile'),u'get':PyJs_anonymous_345_})
                    return var.put(u'n', Js([PyJs_Object_278_, PyJs_Object_281_, PyJs_Object_283_, PyJs_Object_285_, PyJs_Object_287_, PyJs_Object_293_, PyJs_Object_295_, PyJs_Object_300_, PyJs_Object_302_, PyJs_Object_304_, PyJs_Object_306_, PyJs_Object_308_, PyJs_Object_310_, PyJs_Object_314_, PyJs_Object_316_, PyJs_Object_318_, PyJs_Object_322_, PyJs_Object_324_, PyJs_Object_327_, PyJs_Object_330_, PyJs_Object_332_, PyJs_Object_334_, PyJs_Object_336_, PyJs_Object_338_, PyJs_Object_340_, PyJs_Object_342_, PyJs_Object_344_]))
                return PyJsComma(PyJsComma(PyJsComma(var.put(u'e', var.get(u'f')),(PyJs_LONG_346_() and var.get(u's')(var.get(u'e').get(u'prototype'), var.get(u'n')))),(var.get(u'r') and var.get(u's')(var.get(u'e'), var.get(u'r')))),var.get(u'f'))
            PyJs_anonymous_268_._set_name(u'anonymous')
            var.put(u'v', PyJs_anonymous_268_(var.get(u'h')))
            var.get(u'e').put(u'Socket', var.get(u'v'))
        PyJs_anonymous_243_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_347_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'i', u'o', u'n', u's', u'r', u't'])
            @Js
            def PyJsHoisted_a_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_351_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u'ArrayBuffer').callprop(u'isView', var.get(u't')) if (Js(u'function')==var.get(u'ArrayBuffer').get(u'isView').typeof()) else var.get(u't').get(u'buffer').instanceof(var.get(u'ArrayBuffer')))
                PyJs_anonymous_351_._set_name(u'anonymous')
                return (((var.get(u'o') and (var.get(u't').instanceof(var.get(u'ArrayBuffer')) or PyJs_anonymous_351_(var.get(u't')))) or (var.get(u's') and var.get(u't').instanceof(var.get(u'Blob')))) or (var.get(u'c') and var.get(u't').instanceof(var.get(u'File'))))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_348_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_348_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_349_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_349_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_348_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_349_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            Js(u'use strict')
            pass
            PyJs_Object_350_ = Js({u'value':Js(0.0).neg()})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'__esModule'), PyJs_Object_350_),var.get(u'e').put(u'hasBinary', var.get(u'e').put(u'isBinary', PyJsComma(Js(0.0), Js(None)))))
            var.put(u'o', (Js(u'function')==var.get(u'ArrayBuffer',throw=False).typeof()))
            var.put(u'i', var.get(u'Object').get(u'prototype').get(u'toString'))
            var.put(u's', ((Js(u'function')==var.get(u'Blob',throw=False).typeof()) or ((Js(u'undefined')!=var.get(u'Blob',throw=False).typeof()) and PyJsStrictEq(Js(u'[object BlobConstructor]'),var.get(u'i').callprop(u'call', var.get(u'Blob'))))))
            var.put(u'c', ((Js(u'function')==var.get(u'File',throw=False).typeof()) or ((Js(u'undefined')!=var.get(u'File',throw=False).typeof()) and PyJsStrictEq(Js(u'[object FileConstructor]'),var.get(u'i').callprop(u'call', var.get(u'File'))))))
            pass
            @Js
            def PyJs_t_352_(e, n, this, arguments, var=var):
                var = Scope({u'this':this, u't':PyJs_t_352_, u'e':e, u'arguments':arguments, u'n':n}, var)
                var.registers([u'i', u's', u'e', u'o', u'n'])
                if (var.get(u'e').neg() or PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e')))):
                    return Js(1.0).neg()
                if var.get(u'Array').callprop(u'isArray', var.get(u'e')):
                    #for JS loop
                    var.put(u'o', Js(0.0))
                    var.put(u'i', var.get(u'e').get(u'length'))
                    while (var.get(u'o')<var.get(u'i')):
                        try:
                            if var.get(u't')(var.get(u'e').get(var.get(u'o'))):
                                return Js(0.0).neg()
                        finally:
                                (var.put(u'o',Js(var.get(u'o').to_number())+Js(1))-Js(1))
                    return Js(1.0).neg()
                if var.get(u'a')(var.get(u'e')):
                    return Js(0.0).neg()
                if ((var.get(u'e').get(u'toJSON') and (Js(u'function')==var.get(u'e').get(u'toJSON').typeof())) and PyJsStrictEq(Js(1.0),var.get(u'arguments').get(u'length'))):
                    return var.get(u't')(var.get(u'e').callprop(u'toJSON'), Js(0.0).neg())
                for PyJsTemp in var.get(u'e'):
                    var.put(u's', PyJsTemp)
                    if (var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'e'), var.get(u's')) and var.get(u't')(var.get(u'e').get(var.get(u's')))):
                        return Js(0.0).neg()
                return Js(1.0).neg()
            PyJs_t_352_._set_name(u't')
            PyJsComma(var.get(u'e').put(u'isBinary', var.get(u'a')),var.get(u'e').put(u'hasBinary', PyJs_t_352_))
        PyJs_anonymous_347_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_353_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'e', u't', u'n'])
            Js(u'use strict')
            PyJs_Object_354_ = Js({u'value':Js(0.0).neg()})
            @Js
            def PyJs_anonymous_355_(t, e, n, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                var.registers([u'e', u't', u'n'])
                @Js
                def PyJs_anonymous_356_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    var.get(u't').callprop(u'off', var.get(u'e'), var.get(u'n'))
                PyJs_anonymous_356_._set_name(u'anonymous')
                return PyJsComma(var.get(u't').callprop(u'on', var.get(u'e'), var.get(u'n')),PyJs_anonymous_356_)
            PyJs_anonymous_355_._set_name(u'anonymous')
            PyJsComma(PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'__esModule'), PyJs_Object_354_),var.get(u'e').put(u'on', PyJsComma(Js(0.0), Js(None)))),var.get(u'e').put(u'on', PyJs_anonymous_355_))
        PyJs_anonymous_353_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_357_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'f', u'i', u'o', u'n', u's', u'r', u'u', u't'])
            @Js
            def PyJsHoisted_a_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'e', u'f', u'n', u'p', u's', u'u', u't'])
                PyJs_Object_364_ = Js({})
                PyJsComma((PyJsStrictEq(Js(u'object'),var.get(u'r')(var.get(u't'))) and PyJsComma(var.put(u'e', var.get(u't')),var.put(u't', PyJsComma(Js(0.0), Js(None))))),var.put(u'e', (var.get(u'e') or PyJs_Object_364_)))
                var.put(u's', var.get(u'o').callprop(u'url', var.get(u't'), var.get(u'e').get(u'path')))
                var.put(u'a', var.get(u's').get(u'source'))
                var.put(u'u', var.get(u's').get(u'id'))
                var.put(u'f', var.get(u's').get(u'path'))
                var.put(u'p', (var.get(u'c').get(var.get(u'u')) and var.get(u'c').get(var.get(u'u')).get(u'nsps').contains(var.get(u'f'))))
                def PyJs_LONG_365_(var=var):
                    return (var.put(u'n', var.get(u'i').get(u'Manager').create(var.get(u'a'), var.get(u'e'))) if (((var.get(u'e').get(u'forceNew') or var.get(u'e').get(u'force new connection')) or PyJsStrictEq(Js(1.0).neg(),var.get(u'e').get(u'multiplex'))) or var.get(u'p')) else PyJsComma((var.get(u'c').get(var.get(u'u')) or var.get(u'c').put(var.get(u'u'), var.get(u'i').get(u'Manager').create(var.get(u'a'), var.get(u'e')))),var.put(u'n', var.get(u'c').get(var.get(u'u')))))
                return PyJsComma(PyJsComma(PyJs_LONG_365_(),((var.get(u's').get(u'query') and var.get(u'e').get(u'query').neg()) and var.get(u'e').put(u'query', var.get(u's').get(u'queryKey')))),var.get(u'n').callprop(u'socket', var.get(u's').get(u'path'), var.get(u'e')))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_358_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_358_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_359_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_359_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_358_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_359_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            Js(u'use strict')
            pass
            PyJs_Object_360_ = Js({u'value':Js(0.0).neg()})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'__esModule'), PyJs_Object_360_),var.get(u'e').put(u'Socket', var.get(u'e').put(u'io', var.get(u'e').put(u'Manager', var.get(u'e').put(u'protocol', PyJsComma(Js(0.0), Js(None)))))))
            var.put(u'o', var.get(u'n')(Js(18.0)))
            var.put(u'i', var.get(u'n')(Js(7.0)))
            var.put(u's', var.get(u'n')(Js(14.0)))
            @Js
            def PyJs_anonymous_362_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                return var.get(u's').get(u'Socket')
            PyJs_anonymous_362_._set_name(u'anonymous')
            PyJs_Object_361_ = Js({u'enumerable':Js(0.0).neg(),u'get':PyJs_anonymous_362_})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'Socket'), PyJs_Object_361_),var.get(u't').put(u'exports', var.put(u'e', var.get(u'a'))))
            PyJs_Object_363_ = Js({})
            var.put(u'c', var.get(u'e').put(u'managers', PyJs_Object_363_))
            pass
            var.get(u'e').put(u'io', var.get(u'a'))
            var.put(u'u', var.get(u'n')(Js(5.0)))
            @Js
            def PyJs_anonymous_367_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                return var.get(u'u').get(u'protocol')
            PyJs_anonymous_367_._set_name(u'anonymous')
            PyJs_Object_366_ = Js({u'enumerable':Js(0.0).neg(),u'get':PyJs_anonymous_367_})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'protocol'), PyJs_Object_366_),var.get(u'e').put(u'connect', var.get(u'a')))
            var.put(u'f', var.get(u'n')(Js(7.0)))
            @Js
            def PyJs_anonymous_369_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                return var.get(u'f').get(u'Manager')
            PyJs_anonymous_369_._set_name(u'anonymous')
            PyJs_Object_368_ = Js({u'enumerable':Js(0.0).neg(),u'get':PyJs_anonymous_369_})
            var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'Manager'), PyJs_Object_368_)
        PyJs_anonymous_357_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_370_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'r', u'e', u't', u'n'])
            Js(u'use strict')
            PyJs_Object_371_ = Js({u'value':Js(0.0).neg()})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'__esModule'), PyJs_Object_371_),var.get(u'e').put(u'url', PyJsComma(Js(0.0), Js(None))))
            var.put(u'r', var.get(u'n')(Js(6.0)))
            @Js
            def PyJs_anonymous_372_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u'i', u'o', u'n', u's', u't'])
                var.put(u'e', (var.get(u'arguments').get(u'1') if ((var.get(u'arguments').get(u'length')>Js(1.0)) and PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u'arguments').get(u'1'))) else Js(u'')))
                var.put(u'n', (var.get(u'arguments').get(u'2') if (var.get(u'arguments').get(u'length')>Js(2.0)) else PyJsComma(Js(0.0), Js(None))))
                var.put(u'o', var.get(u't'))
                def PyJs_LONG_374_(var=var):
                    def PyJs_LONG_373_(var=var):
                        return PyJsComma(PyJsComma((PyJsStrictEq(Js(u'/'),var.get(u't').callprop(u'charAt', Js(0.0))) and var.put(u't', ((var.get(u'n').get(u'protocol')+var.get(u't')) if PyJsStrictEq(Js(u'/'),var.get(u't').callprop(u'charAt', Js(1.0))) else (var.get(u'n').get(u'host')+var.get(u't'))))),(JsRegExp(u'/^(https?|wss?):\\/\\//').callprop(u'test', var.get(u't')) or var.put(u't', (((var.get(u'n').get(u'protocol')+Js(u'//'))+var.get(u't')) if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u'n')) else (Js(u'https://')+var.get(u't')))))),var.put(u'o', var.get(u'r')(var.get(u't'))))
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put(u'n', (var.get(u'n') or ((Js(u'undefined')!=var.get(u'location',throw=False).typeof()) and var.get(u'location')))),((var.get(u"null")==var.get(u't')) and var.put(u't', ((var.get(u'n').get(u'protocol')+Js(u'//'))+var.get(u'n').get(u'host'))))),((Js(u'string')==var.get(u't',throw=False).typeof()) and PyJs_LONG_373_())),(var.get(u'o').get(u'port') or (var.get(u'o').put(u'port', Js(u'80')) if JsRegExp(u'/^(http|ws)$/').callprop(u'test', var.get(u'o').get(u'protocol')) else (JsRegExp(u'/^(http|ws)s$/').callprop(u'test', var.get(u'o').get(u'protocol')) and var.get(u'o').put(u'port', Js(u'443')))))),var.get(u'o').put(u'path', (var.get(u'o').get(u'path') or Js(u'/'))))
                PyJs_LONG_374_()
                var.put(u'i', PyJsStrictNeq((-Js(1.0)),var.get(u'o').get(u'host').callprop(u'indexOf', Js(u':'))))
                var.put(u's', (((Js(u'[')+var.get(u'o').get(u'host'))+Js(u']')) if var.get(u'i') else var.get(u'o').get(u'host')))
                def PyJs_LONG_375_(var=var):
                    return PyJsComma(PyJsComma(var.get(u'o').put(u'id', (((((var.get(u'o').get(u'protocol')+Js(u'://'))+var.get(u's'))+Js(u':'))+var.get(u'o').get(u'port'))+var.get(u'e'))),var.get(u'o').put(u'href', (((var.get(u'o').get(u'protocol')+Js(u'://'))+var.get(u's'))+(Js(u'') if (var.get(u'n') and PyJsStrictEq(var.get(u'n').get(u'port'),var.get(u'o').get(u'port'))) else (Js(u':')+var.get(u'o').get(u'port')))))),var.get(u'o'))
                return PyJs_LONG_375_()
            PyJs_anonymous_372_._set_name(u'anonymous')
            var.get(u'e').put(u'url', PyJs_anonymous_372_)
        PyJs_anonymous_370_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_376_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'r', u'e', u't', u'n'])
            var.put(u'r', var.get(u'n')(Js(20.0)))
            def PyJs_LONG_378_(var=var):
                @Js
                def PyJs_anonymous_377_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return var.get(u'r').create(var.get(u't'), var.get(u'e'))
                PyJs_anonymous_377_._set_name(u'anonymous')
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u't').put(u'exports', PyJs_anonymous_377_),var.get(u't').get(u'exports').put(u'Socket', var.get(u'r'))),var.get(u't').get(u'exports').put(u'protocol', var.get(u'r').get(u'protocol'))),var.get(u't').get(u'exports').put(u'Transport', var.get(u'n')(Js(3.0)))),var.get(u't').get(u'exports').put(u'transports', var.get(u'n')(Js(8.0)))),var.get(u't').get(u'exports').put(u'parser', var.get(u'n')(Js(1.0))))
            PyJs_LONG_378_()
        PyJs_anonymous_376_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_379_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'd', u'f', u'i', u'h', u'l', u'o', u'n', u'p', u's', u'r', u'u', u't', u'v', u'y'])
            @Js
            def PyJsHoisted_a_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_384_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_385_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_385_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_385_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_53200353 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_53200353 is not None:
                                var.own[u't'] = PyJsHolder_74_53200353
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_53200353
                PyJs_anonymous_384_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_384_())
                @Js
                def PyJs_anonymous_386_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'f')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'f')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'u')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_386_._set_name(u'anonymous')
                return PyJs_anonymous_386_
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_383_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_383_._set_name(u'anonymous')
                return var.put(u'c', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_383_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_f_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_388_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_388_._set_name(u'anonymous')
                return var.put(u'f', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_388_))(var.get(u't'))
            PyJsHoisted_f_.func_name = u'f'
            var.put(u'f', PyJsHoisted_f_)
            @Js
            def PyJsHoisted_i_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                if var.get(u't').instanceof(var.get(u'e')).neg():
                    PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                    raise PyJsTempException
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_o_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_381_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_381_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_382_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_382_._set_name(u'anonymous')
                return var.put(u'o', (PyJs_anonymous_381_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_382_))(var.get(u't'))
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_s_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                @Js
                def PyJs_anonymous_380_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'n'])
                    #for JS loop
                    var.put(u'e', Js(1.0))
                    while (var.get(u'e')<var.get(u'arguments').get(u'length')):
                        try:
                            var.put(u'n', var.get(u'arguments').get(var.get(u'e')))
                            for PyJsTemp in var.get(u'n'):
                                var.put(u'r', PyJsTemp)
                                (var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'n'), var.get(u'r')) and var.get(u't').put(var.get(u'r'), var.get(u'n').get(var.get(u'r'))))
                        finally:
                                (var.put(u'e',Js(var.get(u'e').to_number())+Js(1))-Js(1))
                    return var.get(u't')
                PyJs_anonymous_380_._set_name(u'anonymous')
                return var.put(u'r', (var.get(u'Object').get(u'assign') or PyJs_anonymous_380_)).callprop(u'apply', var.get(u"this"), var.get(u'arguments'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            @Js
            def PyJsHoisted_u_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_387_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                        PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                        raise PyJsTempException
                    return var.get(u't')
                PyJs_anonymous_387_._set_name(u'anonymous')
                return (PyJs_anonymous_387_(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'o')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_u_.func_name = u'u'
            var.put(u'u', PyJsHoisted_u_)
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            var.put(u'p', var.get(u'n')(Js(8.0)))
            var.put(u'l', var.get(u'n')(Js(0.0)))
            var.put(u'h', var.get(u'n')(Js(1.0)))
            var.put(u'y', var.get(u'n')(Js(6.0)))
            var.put(u'd', var.get(u'n')(Js(4.0)))
            @Js
            def PyJs_anonymous_389_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u'f', u'l', u'n', u'u', u't'])
                @Js
                def PyJsHoisted_l_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    PyJs_Object_393_ = Js({})
                    var.put(u'n', (var.get(u'arguments').get(u'1') if ((var.get(u'arguments').get(u'length')>Js(1.0)) and PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u'arguments').get(u'1'))) else PyJs_Object_393_))
                    def PyJs_LONG_399_(var=var):
                        def PyJs_LONG_394_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put(u't', var.get(u'y')(var.get(u't'))),var.get(u'n').put(u'hostname', var.get(u't').get(u'host'))),var.get(u'n').put(u'secure', (PyJsStrictEq(Js(u'https'),var.get(u't').get(u'protocol')) or PyJsStrictEq(Js(u'wss'),var.get(u't').get(u'protocol'))))),var.get(u'n').put(u'port', var.get(u't').get(u'port'))),(var.get(u't').get(u'query') and var.get(u'n').put(u'query', var.get(u't').get(u'query'))))
                        PyJs_Object_396_ = Js({u'threshold':Js(1024.0)})
                        PyJs_Object_397_ = Js({})
                        PyJs_Object_395_ = Js({u'path':Js(u'/engine.io'),u'agent':Js(1.0).neg(),u'withCredentials':Js(1.0).neg(),u'upgrade':Js(0.0).neg(),u'jsonp':Js(0.0).neg(),u'timestampParam':Js(u't'),u'rememberUpgrade':Js(1.0).neg(),u'rejectUnauthorized':Js(0.0).neg(),u'perMessageDeflate':PyJs_Object_396_,u'transportOptions':PyJs_Object_397_})
                        @Js
                        def PyJs_anonymous_398_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            (var.get(u'e').get(u'transport') and PyJsComma(var.get(u'e').get(u'transport').callprop(u'removeAllListeners'),var.get(u'e').get(u'transport').callprop(u'close')))
                        PyJs_anonymous_398_._set_name(u'anonymous')
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'i')(var.get(u"this"), var.get(u'l')),var.put(u'e', var.get(u'f').callprop(u'call', var.get(u"this")))),((var.get(u't') and PyJsStrictEq(Js(u'object'),var.get(u'o')(var.get(u't')))) and PyJsComma(var.put(u'n', var.get(u't')),var.put(u't', var.get(u"null"))))),(PyJs_LONG_394_() if var.get(u't') else (var.get(u'n').get(u'host') and var.get(u'n').put(u'hostname', var.get(u'y')(var.get(u'n').get(u'host')).get(u'host'))))),var.get(u'e').put(u'secure', (var.get(u'n').get(u'secure') if (var.get(u"null")!=var.get(u'n').get(u'secure')) else ((Js(u'undefined')!=var.get(u'location',throw=False).typeof()) and PyJsStrictEq(Js(u'https:'),var.get(u'location').get(u'protocol')))))),((var.get(u'n').get(u'hostname') and var.get(u'n').get(u'port').neg()) and var.get(u'n').put(u'port', (Js(u'443') if var.get(u'e').get(u'secure') else Js(u'80'))))),var.get(u'e').put(u'hostname', (var.get(u'n').get(u'hostname') or (var.get(u'location').get(u'hostname') if (Js(u'undefined')!=var.get(u'location',throw=False).typeof()) else Js(u'localhost'))))),var.get(u'e').put(u'port', (var.get(u'n').get(u'port') or (var.get(u'location').get(u'port') if ((Js(u'undefined')!=var.get(u'location',throw=False).typeof()) and var.get(u'location').get(u'port')) else (Js(443.0) if var.get(u'e').get(u'secure') else Js(80.0)))))),var.get(u'e').put(u'transports', (var.get(u'n').get(u'transports') or Js([Js(u'polling'), Js(u'websocket')])))),var.get(u'e').put(u'readyState', Js(u''))),var.get(u'e').put(u'writeBuffer', Js([]))),var.get(u'e').put(u'prevBufferLen', Js(0.0))),var.get(u'e').put(u'opts', var.get(u'r')(PyJs_Object_395_, var.get(u'n')))),var.get(u'e').get(u'opts').put(u'path', (var.get(u'e').get(u'opts').get(u'path').callprop(u'replace', JsRegExp(u'/\\/$/'), Js(u''))+Js(u'/')))),((Js(u'string')==var.get(u'e').get(u'opts').get(u'query').typeof()) and var.get(u'e').get(u'opts').put(u'query', var.get(u'd').callprop(u'decode', var.get(u'e').get(u'opts').get(u'query'))))),var.get(u'e').put(u'id', var.get(u"null"))),var.get(u'e').put(u'upgrades', var.get(u"null"))),var.get(u'e').put(u'pingInterval', var.get(u"null"))),var.get(u'e').put(u'pingTimeout', var.get(u"null"))),var.get(u'e').put(u'pingTimeoutTimer', var.get(u"null"))),((Js(u'function')==var.get(u'addEventListener',throw=False).typeof()) and var.get(u'addEventListener')(Js(u'beforeunload'), PyJs_anonymous_398_, Js(1.0).neg()))),var.get(u'e').callprop(u'open')),var.get(u'e'))
                    return PyJs_LONG_399_()
                PyJsHoisted_l_.func_name = u'l'
                var.put(u'l', PyJsHoisted_l_)
                @Js
                def PyJs_anonymous_390_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                        PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                        raise PyJsTempException
                    PyJs_Object_392_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                    PyJs_Object_391_ = Js({u'constructor':PyJs_Object_392_})
                    PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_391_)),(var.get(u'e') and var.get(u'c')(var.get(u't'), var.get(u'e'))))
                PyJs_anonymous_390_._set_name(u'anonymous')
                PyJs_anonymous_390_(var.get(u'l'), var.get(u't')).neg()
                var.put(u'f', var.get(u'a')(var.get(u'l')))
                pass
                def PyJs_LONG_461_(var=var):
                    @Js
                    def PyJs_anonymous_401_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't', u'n'])
                        @Js
                        def PyJs_anonymous_402_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u'e', u't', u'n'])
                            PyJs_Object_403_ = Js({})
                            var.put(u'e', PyJs_Object_403_)
                            for PyJsTemp in var.get(u't'):
                                var.put(u'n', PyJsTemp)
                                (var.get(u't').callprop(u'hasOwnProperty', var.get(u'n')) and var.get(u'e').put(var.get(u'n'), var.get(u't').get(var.get(u'n'))))
                            return var.get(u'e')
                        PyJs_anonymous_402_._set_name(u'anonymous')
                        var.put(u'e', PyJs_anonymous_402_(var.get(u"this").get(u'opts').get(u'query')))
                        PyJsComma(PyJsComma(var.get(u'e').put(u'EIO', var.get(u'h').get(u'protocol')),var.get(u'e').put(u'transport', var.get(u't'))),(var.get(u"this").get(u'id') and var.get(u'e').put(u'sid', var.get(u"this").get(u'id'))))
                        PyJs_Object_404_ = Js({})
                        PyJs_Object_405_ = Js({u'query':var.get(u'e'),u'socket':var.get(u"this"),u'hostname':var.get(u"this").get(u'hostname'),u'secure':var.get(u"this").get(u'secure'),u'port':var.get(u"this").get(u'port')})
                        var.put(u'n', var.get(u'r')(PyJs_Object_404_, var.get(u"this").get(u'opts').get(u'transportOptions').get(var.get(u't')), var.get(u"this").get(u'opts'), PyJs_Object_405_))
                        return var.get(u'p').get(var.get(u't')).create(var.get(u'n'))
                    PyJs_anonymous_401_._set_name(u'anonymous')
                    PyJs_Object_400_ = Js({u'key':Js(u'createTransport'),u'value':PyJs_anonymous_401_})
                    @Js
                    def PyJs_anonymous_407_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        pass
                        if ((var.get(u"this").get(u'opts').get(u'rememberUpgrade') and var.get(u'l').get(u'priorWebsocketSuccess')) and PyJsStrictNeq((-Js(1.0)),var.get(u"this").get(u'transports').callprop(u'indexOf', Js(u'websocket')))):
                            var.put(u't', Js(u'websocket'))
                        else:
                            if PyJsStrictEq(Js(0.0),var.get(u"this").get(u'transports').get(u'length')):
                                var.put(u'e', var.get(u"this"))
                                @Js
                                def PyJs_anonymous_408_(this, arguments, var=var):
                                    var = Scope({u'this':this, u'arguments':arguments}, var)
                                    var.registers([])
                                    var.get(u'e').callprop(u'emit', Js(u'error'), Js(u'No transports available'))
                                PyJs_anonymous_408_._set_name(u'anonymous')
                                return PyJsComma(var.get(u'setTimeout')(PyJs_anonymous_408_, Js(0.0)), Js(None))
                            var.put(u't', var.get(u"this").get(u'transports').get(u'0'))
                        var.get(u"this").put(u'readyState', Js(u'opening'))
                        try:
                            var.put(u't', var.get(u"this").callprop(u'createTransport', var.get(u't')))
                        except PyJsException as PyJsTempException:
                            PyJsHolder_74_43158802 = var.own.get(u't')
                            var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                            try:
                                return PyJsComma(var.get(u"this").get(u'transports').callprop(u'shift'),PyJsComma(var.get(u"this").callprop(u'open'), Js(None)))
                            finally:
                                if PyJsHolder_74_43158802 is not None:
                                    var.own[u't'] = PyJsHolder_74_43158802
                                else:
                                    del var.own[u't']
                                del PyJsHolder_74_43158802
                        PyJsComma(var.get(u't').callprop(u'open'),var.get(u"this").callprop(u'setTransport', var.get(u't')))
                    PyJs_anonymous_407_._set_name(u'anonymous')
                    PyJs_Object_406_ = Js({u'key':Js(u'open'),u'value':PyJs_anonymous_407_})
                    @Js
                    def PyJs_anonymous_410_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        var.put(u'e', var.get(u"this"))
                        @Js
                        def PyJs_anonymous_411_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            var.get(u'e').callprop(u'onClose', Js(u'transport close'))
                        PyJs_anonymous_411_._set_name(u'anonymous')
                        @Js
                        def PyJs_anonymous_412_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u't'])
                            var.get(u'e').callprop(u'onError', var.get(u't'))
                        PyJs_anonymous_412_._set_name(u'anonymous')
                        @Js
                        def PyJs_anonymous_413_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u't'])
                            var.get(u'e').callprop(u'onPacket', var.get(u't'))
                        PyJs_anonymous_413_._set_name(u'anonymous')
                        @Js
                        def PyJs_anonymous_414_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            var.get(u'e').callprop(u'onDrain')
                        PyJs_anonymous_414_._set_name(u'anonymous')
                        PyJsComma(PyJsComma((var.get(u"this").get(u'transport') and var.get(u"this").get(u'transport').callprop(u'removeAllListeners')),var.get(u"this").put(u'transport', var.get(u't'))),var.get(u't').callprop(u'on', Js(u'drain'), PyJs_anonymous_414_).callprop(u'on', Js(u'packet'), PyJs_anonymous_413_).callprop(u'on', Js(u'error'), PyJs_anonymous_412_).callprop(u'on', Js(u'close'), PyJs_anonymous_411_))
                    PyJs_anonymous_410_._set_name(u'anonymous')
                    PyJs_Object_409_ = Js({u'key':Js(u'setTransport'),u'value':PyJs_anonymous_410_})
                    @Js
                    def PyJs_anonymous_416_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'a', u'c', u'e', u'f', u'i', u'o', u'n', u's', u'r', u'u', u't'])
                        @Js
                        def PyJsHoisted_a_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            var.get(u's')(Js(u'socket closed'))
                        PyJsHoisted_a_.func_name = u'a'
                        var.put(u'a', PyJsHoisted_a_)
                        @Js
                        def PyJsHoisted_c_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            var.get(u's')(Js(u'transport closed'))
                        PyJsHoisted_c_.func_name = u'c'
                        var.put(u'c', PyJsHoisted_c_)
                        @Js
                        def PyJsHoisted_f_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            def PyJs_LONG_423_(var=var):
                                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'e').callprop(u'removeListener', Js(u'open'), var.get(u'o')),var.get(u'e').callprop(u'removeListener', Js(u'error'), var.get(u's'))),var.get(u'e').callprop(u'removeListener', Js(u'close'), var.get(u'c'))),var.get(u'r').callprop(u'removeListener', Js(u'close'), var.get(u'a'))),var.get(u'r').callprop(u'removeListener', Js(u'upgrading'), var.get(u'u')))
                            PyJs_LONG_423_()
                        PyJsHoisted_f_.func_name = u'f'
                        var.put(u'f', PyJsHoisted_f_)
                        @Js
                        def PyJsHoisted_i_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            (var.get(u'n') or PyJsComma(PyJsComma(PyJsComma(var.put(u'n', Js(0.0).neg()),var.get(u'f')()),var.get(u'e').callprop(u'close')),var.put(u'e', var.get(u"null"))))
                        PyJsHoisted_i_.func_name = u'i'
                        var.put(u'i', PyJsHoisted_i_)
                        @Js
                        def PyJsHoisted_o_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([u't'])
                            if var.get(u'r').get(u'onlyBinaryUpgrades'):
                                var.put(u't', (var.get(u"this").get(u'supportsBinary').neg() and var.get(u'r').get(u'transport').get(u'supportsBinary')))
                                var.put(u'n', (var.get(u'n') or var.get(u't')))
                            PyJs_Object_418_ = Js({u'type':Js(u'ping'),u'data':Js(u'probe')})
                            @Js
                            def PyJs_anonymous_419_(t, this, arguments, var=var):
                                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                                var.registers([u't', u'o'])
                                if var.get(u'n').neg():
                                    if (PyJsStrictEq(Js(u'pong'),var.get(u't').get(u'type')) and PyJsStrictEq(Js(u'probe'),var.get(u't').get(u'data'))):
                                        if PyJsComma(PyJsComma(var.get(u'r').put(u'upgrading', Js(0.0).neg()),var.get(u'r').callprop(u'emit', Js(u'upgrading'), var.get(u'e'))),var.get(u'e').neg()):
                                            return var.get('undefined')
                                        @Js
                                        def PyJs_anonymous_420_(this, arguments, var=var):
                                            var = Scope({u'this':this, u'arguments':arguments}, var)
                                            var.registers([])
                                            def PyJs_LONG_422_(var=var):
                                                PyJs_Object_421_ = Js({u'type':Js(u'upgrade')})
                                                return (PyJsStrictNeq(Js(u'closed'),var.get(u'r').get(u'readyState')) and PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'f')(),var.get(u'r').callprop(u'setTransport', var.get(u'e'))),var.get(u'e').callprop(u'send', Js([PyJs_Object_421_]))),var.get(u'r').callprop(u'emit', Js(u'upgrade'), var.get(u'e'))),var.put(u'e', var.get(u"null"))),var.get(u'r').put(u'upgrading', Js(1.0).neg())),var.get(u'r').callprop(u'flush')))
                                            (var.get(u'n') or PyJs_LONG_422_())
                                        PyJs_anonymous_420_._set_name(u'anonymous')
                                        PyJsComma(var.get(u'l').put(u'priorWebsocketSuccess', PyJsStrictEq(Js(u'websocket'),var.get(u'e').get(u'name'))),var.get(u'r').get(u'transport').callprop(u'pause', PyJs_anonymous_420_))
                                    else:
                                        var.put(u'o', var.get(u'Error').create(Js(u'probe error')))
                                        PyJsComma(var.get(u'o').put(u'transport', var.get(u'e').get(u'name')),var.get(u'r').callprop(u'emit', Js(u'upgradeError'), var.get(u'o')))
                            PyJs_anonymous_419_._set_name(u'anonymous')
                            (var.get(u'n') or PyJsComma(var.get(u'e').callprop(u'send', Js([PyJs_Object_418_])),var.get(u'e').callprop(u'once', Js(u'packet'), PyJs_anonymous_419_)))
                        PyJsHoisted_o_.func_name = u'o'
                        var.put(u'o', PyJsHoisted_o_)
                        @Js
                        def PyJsHoisted_s_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u't', u'n'])
                            var.put(u'n', var.get(u'Error').create((Js(u'probe error: ')+var.get(u't'))))
                            PyJsComma(PyJsComma(var.get(u'n').put(u'transport', var.get(u'e').get(u'name')),var.get(u'i')()),var.get(u'r').callprop(u'emit', Js(u'upgradeError'), var.get(u'n')))
                        PyJsHoisted_s_.func_name = u's'
                        var.put(u's', PyJsHoisted_s_)
                        @Js
                        def PyJsHoisted_u_(t, this, arguments, var=var):
                            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                            var.registers([u't'])
                            ((var.get(u'e') and PyJsStrictNeq(var.get(u't').get(u'name'),var.get(u'e').get(u'name'))) and var.get(u'i')())
                        PyJsHoisted_u_.func_name = u'u'
                        var.put(u'u', PyJsHoisted_u_)
                        PyJs_Object_417_ = Js({u'probe':Js(1.0)})
                        var.put(u'e', var.get(u"this").callprop(u'createTransport', var.get(u't'), PyJs_Object_417_))
                        var.put(u'n', Js(1.0).neg())
                        var.put(u'r', var.get(u"this"))
                        pass
                        pass
                        pass
                        pass
                        pass
                        pass
                        pass
                        def PyJs_LONG_424_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'l').put(u'priorWebsocketSuccess', Js(1.0).neg()),var.get(u'e').callprop(u'once', Js(u'open'), var.get(u'o'))),var.get(u'e').callprop(u'once', Js(u'error'), var.get(u's'))),var.get(u'e').callprop(u'once', Js(u'close'), var.get(u'c'))),var.get(u"this").callprop(u'once', Js(u'close'), var.get(u'a'))),var.get(u"this").callprop(u'once', Js(u'upgrading'), var.get(u'u'))),var.get(u'e').callprop(u'open'))
                        PyJs_LONG_424_()
                    PyJs_anonymous_416_._set_name(u'anonymous')
                    PyJs_Object_415_ = Js({u'key':Js(u'probe'),u'value':PyJs_anonymous_416_})
                    @Js
                    def PyJs_anonymous_426_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        def PyJs_LONG_427_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put(u'readyState', Js(u'open')),var.get(u'l').put(u'priorWebsocketSuccess', PyJsStrictEq(Js(u'websocket'),var.get(u"this").get(u'transport').get(u'name')))),var.get(u"this").callprop(u'emit', Js(u'open'))),var.get(u"this").callprop(u'flush')),((PyJsStrictEq(Js(u'open'),var.get(u"this").get(u'readyState')) and var.get(u"this").get(u'opts').get(u'upgrade')) and var.get(u"this").get(u'transport').get(u'pause')))
                        if PyJs_LONG_427_():
                            #for JS loop
                            var.put(u't', Js(0.0))
                            var.put(u'e', var.get(u"this").get(u'upgrades').get(u'length'))
                            while (var.get(u't')<var.get(u'e')):
                                try:
                                    var.get(u"this").callprop(u'probe', var.get(u"this").get(u'upgrades').get(var.get(u't')))
                                finally:
                                        (var.put(u't',Js(var.get(u't').to_number())+Js(1))-Js(1))
                    PyJs_anonymous_426_._set_name(u'anonymous')
                    PyJs_Object_425_ = Js({u'key':Js(u'onOpen'),u'value':PyJs_anonymous_426_})
                    @Js
                    def PyJs_anonymous_429_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        if ((PyJsStrictEq(Js(u'opening'),var.get(u"this").get(u'readyState')) or PyJsStrictEq(Js(u'open'),var.get(u"this").get(u'readyState'))) or PyJsStrictEq(Js(u'closing'),var.get(u"this").get(u'readyState'))):
                            while 1:
                                SWITCHED = False
                                CONDITION = (PyJsComma(PyJsComma(var.get(u"this").callprop(u'emit', Js(u'packet'), var.get(u't')),var.get(u"this").callprop(u'emit', Js(u'heartbeat'))),var.get(u't').get(u'type')))
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'open')):
                                    SWITCHED = True
                                    var.get(u"this").callprop(u'onHandshake', var.get(u'JSON').callprop(u'parse', var.get(u't').get(u'data')))
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'ping')):
                                    SWITCHED = True
                                    PyJsComma(PyJsComma(var.get(u"this").callprop(u'resetPingTimeout'),var.get(u"this").callprop(u'sendPacket', Js(u'pong'))),var.get(u"this").callprop(u'emit', Js(u'pong')))
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'error')):
                                    SWITCHED = True
                                    var.put(u'e', var.get(u'Error').create(Js(u'server error')))
                                    PyJsComma(var.get(u'e').put(u'code', var.get(u't').get(u'data')),var.get(u"this").callprop(u'onError', var.get(u'e')))
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js(u'message')):
                                    SWITCHED = True
                                    PyJsComma(var.get(u"this").callprop(u'emit', Js(u'data'), var.get(u't').get(u'data')),var.get(u"this").callprop(u'emit', Js(u'message'), var.get(u't').get(u'data')))
                                SWITCHED = True
                                break
                    PyJs_anonymous_429_._set_name(u'anonymous')
                    PyJs_Object_428_ = Js({u'key':Js(u'onPacket'),u'value':PyJs_anonymous_429_})
                    @Js
                    def PyJs_anonymous_431_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        def PyJs_LONG_432_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").callprop(u'emit', Js(u'handshake'), var.get(u't')),var.get(u"this").put(u'id', var.get(u't').get(u'sid'))),var.get(u"this").get(u'transport').get(u'query').put(u'sid', var.get(u't').get(u'sid'))),var.get(u"this").put(u'upgrades', var.get(u"this").callprop(u'filterUpgrades', var.get(u't').get(u'upgrades')))),var.get(u"this").put(u'pingInterval', var.get(u't').get(u'pingInterval'))),var.get(u"this").put(u'pingTimeout', var.get(u't').get(u'pingTimeout'))),var.get(u"this").callprop(u'onOpen')),(PyJsStrictNeq(Js(u'closed'),var.get(u"this").get(u'readyState')) and var.get(u"this").callprop(u'resetPingTimeout')))
                        PyJs_LONG_432_()
                    PyJs_anonymous_431_._set_name(u'anonymous')
                    PyJs_Object_430_ = Js({u'key':Js(u'onHandshake'),u'value':PyJs_anonymous_431_})
                    @Js
                    def PyJs_anonymous_434_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.put(u't', var.get(u"this"))
                        @Js
                        def PyJs_anonymous_435_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            var.get(u't').callprop(u'onClose', Js(u'ping timeout'))
                        PyJs_anonymous_435_._set_name(u'anonymous')
                        PyJsComma(var.get(u'clearTimeout')(var.get(u"this").get(u'pingTimeoutTimer')),var.get(u"this").put(u'pingTimeoutTimer', var.get(u'setTimeout')(PyJs_anonymous_435_, (var.get(u"this").get(u'pingInterval')+var.get(u"this").get(u'pingTimeout')))))
                    PyJs_anonymous_434_._set_name(u'anonymous')
                    PyJs_Object_433_ = Js({u'key':Js(u'resetPingTimeout'),u'value':PyJs_anonymous_434_})
                    @Js
                    def PyJs_anonymous_437_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        PyJsComma(PyJsComma(var.get(u"this").get(u'writeBuffer').callprop(u'splice', Js(0.0), var.get(u"this").get(u'prevBufferLen')),var.get(u"this").put(u'prevBufferLen', Js(0.0))),(var.get(u"this").callprop(u'emit', Js(u'drain')) if PyJsStrictEq(Js(0.0),var.get(u"this").get(u'writeBuffer').get(u'length')) else var.get(u"this").callprop(u'flush')))
                    PyJs_anonymous_437_._set_name(u'anonymous')
                    PyJs_Object_436_ = Js({u'key':Js(u'onDrain'),u'value':PyJs_anonymous_437_})
                    @Js
                    def PyJs_anonymous_439_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        def PyJs_LONG_440_(var=var):
                            return ((((PyJsStrictNeq(Js(u'closed'),var.get(u"this").get(u'readyState')) and var.get(u"this").get(u'transport').get(u'writable')) and var.get(u"this").get(u'upgrading').neg()) and var.get(u"this").get(u'writeBuffer').get(u'length')) and PyJsComma(PyJsComma(var.get(u"this").get(u'transport').callprop(u'send', var.get(u"this").get(u'writeBuffer')),var.get(u"this").put(u'prevBufferLen', var.get(u"this").get(u'writeBuffer').get(u'length'))),var.get(u"this").callprop(u'emit', Js(u'flush'))))
                        PyJs_LONG_440_()
                    PyJs_anonymous_439_._set_name(u'anonymous')
                    PyJs_Object_438_ = Js({u'key':Js(u'flush'),u'value':PyJs_anonymous_439_})
                    @Js
                    def PyJs_anonymous_442_(t, e, n, this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                        var.registers([u'e', u't', u'n'])
                        return PyJsComma(var.get(u"this").callprop(u'sendPacket', Js(u'message'), var.get(u't'), var.get(u'e'), var.get(u'n')),var.get(u"this"))
                    PyJs_anonymous_442_._set_name(u'anonymous')
                    PyJs_Object_441_ = Js({u'key':Js(u'write'),u'value':PyJs_anonymous_442_})
                    @Js
                    def PyJs_anonymous_444_(t, e, n, this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                        var.registers([u'e', u't', u'n'])
                        return PyJsComma(var.get(u"this").callprop(u'sendPacket', Js(u'message'), var.get(u't'), var.get(u'e'), var.get(u'n')),var.get(u"this"))
                    PyJs_anonymous_444_._set_name(u'anonymous')
                    PyJs_Object_443_ = Js({u'key':Js(u'send'),u'value':PyJs_anonymous_444_})
                    @Js
                    def PyJs_anonymous_446_(t, e, n, r, this, arguments, var=var):
                        var = Scope({u'r':r, u'e':e, u't':t, u'this':this, u'arguments':arguments, u'n':n}, var)
                        var.registers([u'r', u'e', u't', u'o', u'n'])
                        def PyJs_LONG_447_(var=var):
                            return PyJsComma(PyJsComma(((Js(u'function')==var.get(u'e',throw=False).typeof()) and PyJsComma(var.put(u'r', var.get(u'e')),var.put(u'e', PyJsComma(Js(0.0), Js(None))))),((Js(u'function')==var.get(u'n',throw=False).typeof()) and PyJsComma(var.put(u'r', var.get(u'n')),var.put(u'n', var.get(u"null"))))),(PyJsStrictNeq(Js(u'closing'),var.get(u"this").get(u'readyState')) and PyJsStrictNeq(Js(u'closed'),var.get(u"this").get(u'readyState'))))
                        if PyJs_LONG_447_():
                            PyJs_Object_448_ = Js({})
                            var.put(u'n', (var.get(u'n') or PyJs_Object_448_)).put(u'compress', PyJsStrictNeq(Js(1.0).neg(),var.get(u'n').get(u'compress')))
                            PyJs_Object_449_ = Js({u'type':var.get(u't'),u'data':var.get(u'e'),u'options':var.get(u'n')})
                            var.put(u'o', PyJs_Object_449_)
                            PyJsComma(PyJsComma(PyJsComma(var.get(u"this").callprop(u'emit', Js(u'packetCreate'), var.get(u'o')),var.get(u"this").get(u'writeBuffer').callprop(u'push', var.get(u'o'))),(var.get(u'r') and var.get(u"this").callprop(u'once', Js(u'flush'), var.get(u'r')))),var.get(u"this").callprop(u'flush'))
                    PyJs_anonymous_446_._set_name(u'anonymous')
                    PyJs_Object_445_ = Js({u'key':Js(u'sendPacket'),u'value':PyJs_anonymous_446_})
                    @Js
                    def PyJs_anonymous_451_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u'r', u'e', u't', u'n'])
                        @Js
                        def PyJsHoisted_r_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            PyJsComma(var.get(u't').callprop(u'once', Js(u'upgrade'), var.get(u'n')),var.get(u't').callprop(u'once', Js(u'upgradeError'), var.get(u'n')))
                        PyJsHoisted_r_.func_name = u'r'
                        var.put(u'r', PyJsHoisted_r_)
                        @Js
                        def PyJsHoisted_e_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            PyJsComma(var.get(u't').callprop(u'onClose', Js(u'forced close')),var.get(u't').get(u'transport').callprop(u'close'))
                        PyJsHoisted_e_.func_name = u'e'
                        var.put(u'e', PyJsHoisted_e_)
                        @Js
                        def PyJsHoisted_n_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            PyJsComma(PyJsComma(var.get(u't').callprop(u'removeListener', Js(u'upgrade'), var.get(u'n')),var.get(u't').callprop(u'removeListener', Js(u'upgradeError'), var.get(u'n'))),var.get(u'e')())
                        PyJsHoisted_n_.func_name = u'n'
                        var.put(u'n', PyJsHoisted_n_)
                        var.put(u't', var.get(u"this"))
                        pass
                        pass
                        pass
                        def PyJs_LONG_453_(var=var):
                            @Js
                            def PyJs_anonymous_452_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                (var.get(u'r')() if var.get(u"this").get(u'upgrading') else var.get(u'e')())
                            PyJs_anonymous_452_._set_name(u'anonymous')
                            return ((PyJsStrictNeq(Js(u'opening'),var.get(u"this").get(u'readyState')) and PyJsStrictNeq(Js(u'open'),var.get(u"this").get(u'readyState'))) or PyJsComma(var.get(u"this").put(u'readyState', Js(u'closing')),(var.get(u"this").callprop(u'once', Js(u'drain'), PyJs_anonymous_452_) if var.get(u"this").get(u'writeBuffer').get(u'length') else (var.get(u'r')() if var.get(u"this").get(u'upgrading') else var.get(u'e')()))))
                        return PyJsComma(PyJs_LONG_453_(),var.get(u"this"))
                    PyJs_anonymous_451_._set_name(u'anonymous')
                    PyJs_Object_450_ = Js({u'key':Js(u'close'),u'value':PyJs_anonymous_451_})
                    @Js
                    def PyJs_anonymous_455_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        PyJsComma(PyJsComma(var.get(u'l').put(u'priorWebsocketSuccess', Js(1.0).neg()),var.get(u"this").callprop(u'emit', Js(u'error'), var.get(u't'))),var.get(u"this").callprop(u'onClose', Js(u'transport error'), var.get(u't')))
                    PyJs_anonymous_455_._set_name(u'anonymous')
                    PyJs_Object_454_ = Js({u'key':Js(u'onError'),u'value':PyJs_anonymous_455_})
                    @Js
                    def PyJs_anonymous_457_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        def PyJs_LONG_458_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'clearTimeout')(var.get(u"this").get(u'pingIntervalTimer')),var.get(u'clearTimeout')(var.get(u"this").get(u'pingTimeoutTimer'))),var.get(u"this").get(u'transport').callprop(u'removeAllListeners', Js(u'close'))),var.get(u"this").get(u'transport').callprop(u'close')),var.get(u"this").get(u'transport').callprop(u'removeAllListeners')),var.get(u"this").put(u'readyState', Js(u'closed'))),var.get(u"this").put(u'id', var.get(u"null"))),var.get(u"this").callprop(u'emit', Js(u'close'), var.get(u't'), var.get(u'e'))),var.get(u"this").put(u'writeBuffer', Js([]))),var.get(u"this").put(u'prevBufferLen', Js(0.0)))
                        (((PyJsStrictNeq(Js(u'opening'),var.get(u"this").get(u'readyState')) and PyJsStrictNeq(Js(u'open'),var.get(u"this").get(u'readyState'))) and PyJsStrictNeq(Js(u'closing'),var.get(u"this").get(u'readyState'))) or PyJs_LONG_458_())
                    PyJs_anonymous_457_._set_name(u'anonymous')
                    PyJs_Object_456_ = Js({u'key':Js(u'onClose'),u'value':PyJs_anonymous_457_})
                    @Js
                    def PyJs_anonymous_460_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u'r', u'e', u't', u'n'])
                        #for JS loop
                        var.put(u'e', Js([]))
                        var.put(u'n', Js(0.0))
                        var.put(u'r', var.get(u't').get(u'length'))
                        while (var.get(u'n')<var.get(u'r')):
                            try:
                                ((~var.get(u"this").get(u'transports').callprop(u'indexOf', var.get(u't').get(var.get(u'n')))) and var.get(u'e').callprop(u'push', var.get(u't').get(var.get(u'n'))))
                            finally:
                                    (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
                        return var.get(u'e')
                    PyJs_anonymous_460_._set_name(u'anonymous')
                    PyJs_Object_459_ = Js({u'key':Js(u'filterUpgrades'),u'value':PyJs_anonymous_460_})
                    return PyJsComma(PyJsComma(PyJsComma(var.put(u'e', var.get(u'l')),(var.put(u'n', Js([PyJs_Object_400_, PyJs_Object_406_, PyJs_Object_409_, PyJs_Object_415_, PyJs_Object_425_, PyJs_Object_428_, PyJs_Object_430_, PyJs_Object_433_, PyJs_Object_436_, PyJs_Object_438_, PyJs_Object_441_, PyJs_Object_443_, PyJs_Object_445_, PyJs_Object_450_, PyJs_Object_454_, PyJs_Object_456_, PyJs_Object_459_])) and var.get(u's')(var.get(u'e').get(u'prototype'), var.get(u'n')))),(var.get(u'u') and var.get(u's')(var.get(u'e'), var.get(u'u')))),var.get(u'l'))
                return PyJs_LONG_461_()
            PyJs_anonymous_389_._set_name(u'anonymous')
            var.put(u'v', PyJs_anonymous_389_(var.get(u'l')))
            PyJsComma(PyJsComma(var.get(u'v').put(u'priorWebsocketSuccess', Js(1.0).neg()),var.get(u'v').put(u'protocol', var.get(u'h').get(u'protocol'))),var.get(u't').put(u'exports', var.get(u'v')))
        PyJs_anonymous_379_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_462_(t, e, this, arguments, var=var):
            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
            var.registers([u'e', u't'])
            try:
                var.get(u't').put(u'exports', ((Js(u'undefined')!=var.get(u'XMLHttpRequest',throw=False).typeof()) and var.get(u'XMLHttpRequest').create().contains(Js(u'withCredentials'))))
            except PyJsException as PyJsTempException:
                PyJsHolder_65_21674397 = var.own.get(u'e')
                var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
                try:
                    var.get(u't').put(u'exports', Js(1.0).neg())
                finally:
                    if PyJsHolder_65_21674397 is not None:
                        var.own[u'e'] = PyJsHolder_65_21674397
                    else:
                        del var.own[u'e']
                    del PyJsHolder_65_21674397
        PyJs_anonymous_462_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_463_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'_', u'a', u'c', u'b', u'e', u'd', u'g', u'f', u'i', u'h', u'k', u'm', u'l', u'o', u'n', u'p', u's', u'r', u'u', u't', u'w', u'v', u'y'])
            @Js
            def PyJsHoisted_a_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                    PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                    raise PyJsTempException
                PyJs_Object_468_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                PyJs_Object_467_ = Js({u'constructor':PyJs_Object_468_})
                PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_467_)),(var.get(u'e') and var.get(u'u')(var.get(u't'), var.get(u'e'))))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, e, n, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                var.registers([u'e', u't', u'n'])
                return PyJsComma(PyJsComma((var.get(u'e') and var.get(u's')(var.get(u't').get(u'prototype'), var.get(u'e'))),(var.get(u'n') and var.get(u's')(var.get(u't'), var.get(u'n')))),var.get(u't'))
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_f_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_470_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_471_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_471_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_471_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_46553472 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_46553472 is not None:
                                var.own[u't'] = PyJsHolder_74_46553472
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_46553472
                PyJs_anonymous_470_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_470_())
                @Js
                def PyJs_anonymous_472_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'l')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'l')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'p')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_472_._set_name(u'anonymous')
                return PyJs_anonymous_472_
            PyJsHoisted_f_.func_name = u'f'
            var.put(u'f', PyJsHoisted_f_)
            @Js
            def PyJsHoisted_i_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                if var.get(u't').instanceof(var.get(u'e')).neg():
                    PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                    raise PyJsTempException
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_m_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                pass
            PyJsHoisted_m_.func_name = u'm'
            var.put(u'm', PyJsHoisted_m_)
            @Js
            def PyJsHoisted_l_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_474_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_474_._set_name(u'anonymous')
                return var.put(u'l', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_474_))(var.get(u't'))
            PyJsHoisted_l_.func_name = u'l'
            var.put(u'l', PyJsHoisted_l_)
            @Js
            def PyJsHoisted_o_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                @Js
                def PyJs_anonymous_466_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'n'])
                    #for JS loop
                    var.put(u'e', Js(1.0))
                    while (var.get(u'e')<var.get(u'arguments').get(u'length')):
                        try:
                            var.put(u'n', var.get(u'arguments').get(var.get(u'e')))
                            for PyJsTemp in var.get(u'n'):
                                var.put(u'r', PyJsTemp)
                                (var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u'n'), var.get(u'r')) and var.get(u't').put(var.get(u'r'), var.get(u'n').get(var.get(u'r'))))
                        finally:
                                (var.put(u'e',Js(var.get(u'e').to_number())+Js(1))-Js(1))
                    return var.get(u't')
                PyJs_anonymous_466_._set_name(u'anonymous')
                return var.put(u'o', (var.get(u'Object').get(u'assign') or PyJs_anonymous_466_)).callprop(u'apply', var.get(u"this"), var.get(u'arguments'))
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_p_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_473_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                        PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                        raise PyJsTempException
                    return var.get(u't')
                PyJs_anonymous_473_._set_name(u'anonymous')
                return (PyJs_anonymous_473_(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_p_.func_name = u'p'
            var.put(u'p', PyJsHoisted_p_)
            @Js
            def PyJsHoisted_s_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_464_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_464_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_465_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_465_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_464_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_465_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            @Js
            def PyJsHoisted_u_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_469_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_469_._set_name(u'anonymous')
                return var.put(u'u', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_469_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_u_.func_name = u'u'
            var.put(u'u', PyJsHoisted_u_)
            @Js
            def PyJsHoisted___(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u't'])
                for PyJsTemp in var.get(u'w').get(u'requests'):
                    var.put(u't', PyJsTemp)
                    (var.get(u'w').get(u'requests').callprop(u'hasOwnProperty', var.get(u't')) and var.get(u'w').get(u'requests').get(var.get(u't')).callprop(u'abort'))
            PyJsHoisted___.func_name = u'_'
            var.put(u'_', PyJsHoisted___)
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            var.put(u'h', var.get(u'n')(Js(9.0)))
            var.put(u'y', var.get(u'n')(Js(10.0)))
            var.put(u'd', var.get(u'n')(Js(0.0)))
            var.put(u'v', var.get(u'n')(Js(13.0)).get(u'pick'))
            var.put(u'b', var.get(u'n')(Js(2.0)))
            pass
            PyJs_Object_475_ = Js({u'xdomain':Js(1.0).neg()})
            var.put(u'g', (var.get(u"null")!=var.get(u'h').create(PyJs_Object_475_).get(u'responseType')))
            @Js
            def PyJs_anonymous_476_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't', u'n'])
                @Js
                def PyJsHoisted_n_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u's', u'r', u'c', u'o', u't'])
                    pass
                    if PyJsComma(PyJsComma(var.get(u'i')(var.get(u"this"), var.get(u'n')),var.put(u'r', var.get(u'e').callprop(u'call', var.get(u"this"), var.get(u't')))),(Js(u'undefined')!=var.get(u'location',throw=False).typeof())):
                        var.put(u'o', PyJsStrictEq(Js(u'https:'),var.get(u'location').get(u'protocol')))
                        var.put(u's', var.get(u'location').get(u'port'))
                        def PyJs_LONG_477_(var=var):
                            return PyJsComma(PyJsComma((var.get(u's') or var.put(u's', (Js(443.0) if var.get(u'o') else Js(80.0)))),var.get(u'r').put(u'xd', (((Js(u'undefined')!=var.get(u'location',throw=False).typeof()) and PyJsStrictNeq(var.get(u't').get(u'hostname'),var.get(u'location').get(u'hostname'))) or PyJsStrictNeq(var.get(u's'),var.get(u't').get(u'port'))))),var.get(u'r').put(u'xs', PyJsStrictNeq(var.get(u't').get(u'secure'),var.get(u'o'))))
                        PyJs_LONG_477_()
                    var.put(u'c', (var.get(u't') and var.get(u't').get(u'forceBase64')))
                    return PyJsComma(var.get(u'r').put(u'supportsBinary', (var.get(u'g') and var.get(u'c').neg())),var.get(u'r'))
                PyJsHoisted_n_.func_name = u'n'
                var.put(u'n', PyJsHoisted_n_)
                var.get(u'a')(var.get(u'n'), var.get(u't'))
                var.put(u'e', var.get(u'f')(var.get(u'n')))
                pass
                @Js
                def PyJs_anonymous_479_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u't'])
                    PyJs_Object_480_ = Js({})
                    var.put(u't', (var.get(u'arguments').get(u'0') if ((var.get(u'arguments').get(u'length')>Js(0.0)) and PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u'arguments').get(u'0'))) else PyJs_Object_480_))
                    PyJs_Object_481_ = Js({u'xd':var.get(u"this").get(u'xd'),u'xs':var.get(u"this").get(u'xs')})
                    return PyJsComma(var.get(u'o')(var.get(u't'), PyJs_Object_481_, var.get(u"this").get(u'opts')),var.get(u'w').create(var.get(u"this").callprop(u'uri'), var.get(u't')))
                PyJs_anonymous_479_._set_name(u'anonymous')
                PyJs_Object_478_ = Js({u'key':Js(u'request'),u'value':PyJs_anonymous_479_})
                @Js
                def PyJs_anonymous_483_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'n'])
                    PyJs_Object_484_ = Js({u'method':Js(u'POST'),u'data':var.get(u't')})
                    var.put(u'n', var.get(u"this").callprop(u'request', PyJs_Object_484_))
                    var.put(u'r', var.get(u"this"))
                    @Js
                    def PyJs_anonymous_485_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.get(u'r').callprop(u'onError', Js(u'xhr post error'), var.get(u't'))
                    PyJs_anonymous_485_._set_name(u'anonymous')
                    PyJsComma(var.get(u'n').callprop(u'on', Js(u'success'), var.get(u'e')),var.get(u'n').callprop(u'on', Js(u'error'), PyJs_anonymous_485_))
                PyJs_anonymous_483_._set_name(u'anonymous')
                PyJs_Object_482_ = Js({u'key':Js(u'doWrite'),u'value':PyJs_anonymous_483_})
                @Js
                def PyJs_anonymous_487_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    var.put(u't', var.get(u"this").callprop(u'request'))
                    var.put(u'e', var.get(u"this"))
                    @Js
                    def PyJs_anonymous_488_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.get(u'e').callprop(u'onData', var.get(u't'))
                    PyJs_anonymous_488_._set_name(u'anonymous')
                    @Js
                    def PyJs_anonymous_489_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.get(u'e').callprop(u'onError', Js(u'xhr poll error'), var.get(u't'))
                    PyJs_anonymous_489_._set_name(u'anonymous')
                    PyJsComma(PyJsComma(var.get(u't').callprop(u'on', Js(u'data'), PyJs_anonymous_488_),var.get(u't').callprop(u'on', Js(u'error'), PyJs_anonymous_489_)),var.get(u"this").put(u'pollXhr', var.get(u't')))
                PyJs_anonymous_487_._set_name(u'anonymous')
                PyJs_Object_486_ = Js({u'key':Js(u'doPoll'),u'value':PyJs_anonymous_487_})
                return PyJsComma(var.get(u'c')(var.get(u'n'), Js([PyJs_Object_478_, PyJs_Object_482_, PyJs_Object_486_])),var.get(u'n'))
            PyJs_anonymous_476_._set_name(u'anonymous')
            var.put(u'k', PyJs_anonymous_476_(var.get(u'y')))
            @Js
            def PyJs_anonymous_490_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't', u'n'])
                @Js
                def PyJsHoisted_n_(t, r, this, arguments, var=var):
                    var = Scope({u'this':this, u'r':r, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u't', u'o'])
                    pass
                    def PyJs_LONG_491_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'i')(var.get(u"this"), var.get(u'n')),var.put(u'o', var.get(u'e').callprop(u'call', var.get(u"this"))).put(u'opts', var.get(u'r'))),var.get(u'o').put(u'method', (var.get(u'r').get(u'method') or Js(u'GET')))),var.get(u'o').put(u'uri', var.get(u't'))),var.get(u'o').put(u'async', PyJsStrictNeq(Js(1.0).neg(),var.get(u'r').get(u'async')))),var.get(u'o').put(u'data', (var.get(u'r').get(u'data') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u'r').get(u'data')) else var.get(u"null")))),var.get(u'o').callprop(u'create')),var.get(u'o'))
                    return PyJs_LONG_491_()
                PyJsHoisted_n_.func_name = u'n'
                var.put(u'n', PyJsHoisted_n_)
                var.get(u'a')(var.get(u'n'), var.get(u't'))
                var.put(u'e', var.get(u'f')(var.get(u'n')))
                pass
                @Js
                def PyJs_anonymous_493_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'o'])
                    var.put(u't', var.get(u'v')(var.get(u"this").get(u'opts'), Js(u'agent'), Js(u'enablesXDR'), Js(u'pfx'), Js(u'key'), Js(u'passphrase'), Js(u'cert'), Js(u'ca'), Js(u'ciphers'), Js(u'rejectUnauthorized')))
                    PyJsComma(var.get(u't').put(u'xdomain', var.get(u"this").get(u'opts').get(u'xd').neg().neg()),var.get(u't').put(u'xscheme', var.get(u"this").get(u'opts').get(u'xs').neg().neg()))
                    var.put(u'e', var.get(u"this").put(u'xhr', var.get(u'h').create(var.get(u't'))))
                    var.put(u'r', var.get(u"this"))
                    try:
                        var.get(u'e').callprop(u'open', var.get(u"this").get(u'method'), var.get(u"this").get(u'uri'), var.get(u"this").get(u'async'))
                        try:
                            if var.get(u"this").get(u'opts').get(u'extraHeaders'):
                                for PyJsTemp in PyJsComma((var.get(u'e').get(u'setDisableHeaderCheck') and var.get(u'e').callprop(u'setDisableHeaderCheck', Js(0.0).neg())),var.get(u"this").get(u'opts').get(u'extraHeaders')):
                                    var.put(u'o', PyJsTemp)
                                    (var.get(u"this").get(u'opts').get(u'extraHeaders').callprop(u'hasOwnProperty', var.get(u'o')) and var.get(u'e').callprop(u'setRequestHeader', var.get(u'o'), var.get(u"this").get(u'opts').get(u'extraHeaders').get(var.get(u'o'))))
                        except PyJsException as PyJsTempException:
                            PyJsHolder_74_91355254 = var.own.get(u't')
                            var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                            try:
                                pass
                            finally:
                                if PyJsHolder_74_91355254 is not None:
                                    var.own[u't'] = PyJsHolder_74_91355254
                                else:
                                    del var.own[u't']
                                del PyJsHolder_74_91355254
                        if PyJsStrictEq(Js(u'POST'),var.get(u"this").get(u'method')):
                            try:
                                var.get(u'e').callprop(u'setRequestHeader', Js(u'Content-type'), Js(u'text/plain;charset=UTF-8'))
                            except PyJsException as PyJsTempException:
                                PyJsHolder_74_4307988 = var.own.get(u't')
                                var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                                try:
                                    pass
                                finally:
                                    if PyJsHolder_74_4307988 is not None:
                                        var.own[u't'] = PyJsHolder_74_4307988
                                    else:
                                        del var.own[u't']
                                    del PyJsHolder_74_4307988
                        try:
                            var.get(u'e').callprop(u'setRequestHeader', Js(u'Accept'), Js(u'*/*'))
                        except PyJsException as PyJsTempException:
                            PyJsHolder_74_36911618 = var.own.get(u't')
                            var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                            try:
                                pass
                            finally:
                                if PyJsHolder_74_36911618 is not None:
                                    var.own[u't'] = PyJsHolder_74_36911618
                                else:
                                    del var.own[u't']
                                del PyJsHolder_74_36911618
                        def PyJs_LONG_498_(var=var):
                            @Js
                            def PyJs_anonymous_494_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                var.get(u'r').callprop(u'onLoad')
                            PyJs_anonymous_494_._set_name(u'anonymous')
                            @Js
                            def PyJs_anonymous_495_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                var.get(u'r').callprop(u'onError', var.get(u'e').get(u'responseText'))
                            PyJs_anonymous_495_._set_name(u'anonymous')
                            @Js
                            def PyJs_anonymous_496_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                @Js
                                def PyJs_anonymous_497_(this, arguments, var=var):
                                    var = Scope({u'this':this, u'arguments':arguments}, var)
                                    var.registers([])
                                    var.get(u'r').callprop(u'onError', (var.get(u'e').get(u'status') if (Js(u'number')==var.get(u'e').get(u'status').typeof()) else Js(0.0)))
                                PyJs_anonymous_497_._set_name(u'anonymous')
                                (PyJsStrictEq(Js(4.0),var.get(u'e').get(u'readyState')) and (var.get(u'r').callprop(u'onLoad') if (PyJsStrictEq(Js(200.0),var.get(u'e').get(u'status')) or PyJsStrictEq(Js(1223.0),var.get(u'e').get(u'status'))) else var.get(u'setTimeout')(PyJs_anonymous_497_, Js(0.0))))
                            PyJs_anonymous_496_._set_name(u'anonymous')
                            return PyJsComma(PyJsComma(PyJsComma((var.get(u'e').contains(Js(u'withCredentials')) and var.get(u'e').put(u'withCredentials', var.get(u"this").get(u'opts').get(u'withCredentials'))),(var.get(u"this").get(u'opts').get(u'requestTimeout') and var.get(u'e').put(u'timeout', var.get(u"this").get(u'opts').get(u'requestTimeout')))),(PyJsComma(var.get(u'e').put(u'onload', PyJs_anonymous_494_),var.get(u'e').put(u'onerror', PyJs_anonymous_495_)) if var.get(u"this").callprop(u'hasXDR') else var.get(u'e').put(u'onreadystatechange', PyJs_anonymous_496_))),var.get(u'e').callprop(u'send', var.get(u"this").get(u'data')))
                        PyJs_LONG_498_()
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_69346382 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            @Js
                            def PyJs_anonymous_499_(this, arguments, var=var):
                                var = Scope({u'this':this, u'arguments':arguments}, var)
                                var.registers([])
                                var.get(u'r').callprop(u'onError', var.get(u't'))
                            PyJs_anonymous_499_._set_name(u'anonymous')
                            return PyJsComma(var.get(u'setTimeout')(PyJs_anonymous_499_, Js(0.0)), Js(None))
                        finally:
                            if PyJsHolder_74_69346382 is not None:
                                var.own[u't'] = PyJsHolder_74_69346382
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_69346382
                    ((Js(u'undefined')!=var.get(u'document',throw=False).typeof()) and PyJsComma(var.get(u"this").put(u'index', (var.get(u'n').put(u'requestsCount',Js(var.get(u'n').get(u'requestsCount').to_number())+Js(1))-Js(1))),var.get(u'n').get(u'requests').put(var.get(u"this").get(u'index'), var.get(u"this"))))
                PyJs_anonymous_493_._set_name(u'anonymous')
                PyJs_Object_492_ = Js({u'key':Js(u'create'),u'value':PyJs_anonymous_493_})
                @Js
                def PyJs_anonymous_501_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    PyJsComma(var.get(u"this").callprop(u'emit', Js(u'success')),var.get(u"this").callprop(u'cleanup'))
                PyJs_anonymous_501_._set_name(u'anonymous')
                PyJs_Object_500_ = Js({u'key':Js(u'onSuccess'),u'value':PyJs_anonymous_501_})
                @Js
                def PyJs_anonymous_503_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    PyJsComma(var.get(u"this").callprop(u'emit', Js(u'data'), var.get(u't')),var.get(u"this").callprop(u'onSuccess'))
                PyJs_anonymous_503_._set_name(u'anonymous')
                PyJs_Object_502_ = Js({u'key':Js(u'onData'),u'value':PyJs_anonymous_503_})
                @Js
                def PyJs_anonymous_505_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    PyJsComma(var.get(u"this").callprop(u'emit', Js(u'error'), var.get(u't')),var.get(u"this").callprop(u'cleanup', Js(0.0).neg()))
                PyJs_anonymous_505_._set_name(u'anonymous')
                PyJs_Object_504_ = Js({u'key':Js(u'onError'),u'value':PyJs_anonymous_505_})
                @Js
                def PyJs_anonymous_507_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get(u'xhr')) and PyJsStrictNeq(var.get(u"null"),var.get(u"this").get(u'xhr'))):
                        if PyJsComma((var.get(u"this").get(u'xhr').put(u'onload', var.get(u"this").get(u'xhr').put(u'onerror', var.get(u'm'))) if var.get(u"this").callprop(u'hasXDR') else var.get(u"this").get(u'xhr').put(u'onreadystatechange', var.get(u'm'))),var.get(u't')):
                            try:
                                var.get(u"this").get(u'xhr').callprop(u'abort')
                            except PyJsException as PyJsTempException:
                                PyJsHolder_74_52692995 = var.own.get(u't')
                                var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                                try:
                                    pass
                                finally:
                                    if PyJsHolder_74_52692995 is not None:
                                        var.own[u't'] = PyJsHolder_74_52692995
                                    else:
                                        del var.own[u't']
                                    del PyJsHolder_74_52692995
                        PyJsComma(((Js(u'undefined')!=var.get(u'document',throw=False).typeof()) and var.get(u'n').get(u'requests').delete(var.get(u"this").get(u'index'))),var.get(u"this").put(u'xhr', var.get(u"null")))
                PyJs_anonymous_507_._set_name(u'anonymous')
                PyJs_Object_506_ = Js({u'key':Js(u'cleanup'),u'value':PyJs_anonymous_507_})
                @Js
                def PyJs_anonymous_509_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u't'])
                    var.put(u't', var.get(u"this").get(u'xhr').get(u'responseText'))
                    (PyJsStrictNeq(var.get(u"null"),var.get(u't')) and var.get(u"this").callprop(u'onData', var.get(u't')))
                PyJs_anonymous_509_._set_name(u'anonymous')
                PyJs_Object_508_ = Js({u'key':Js(u'onLoad'),u'value':PyJs_anonymous_509_})
                @Js
                def PyJs_anonymous_511_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return (((Js(u'undefined')!=var.get(u'XDomainRequest',throw=False).typeof()) and var.get(u"this").get(u'xs').neg()) and var.get(u"this").get(u'enablesXDR'))
                PyJs_anonymous_511_._set_name(u'anonymous')
                PyJs_Object_510_ = Js({u'key':Js(u'hasXDR'),u'value':PyJs_anonymous_511_})
                @Js
                def PyJs_anonymous_513_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    var.get(u"this").callprop(u'cleanup')
                PyJs_anonymous_513_._set_name(u'anonymous')
                PyJs_Object_512_ = Js({u'key':Js(u'abort'),u'value':PyJs_anonymous_513_})
                return PyJsComma(var.get(u'c')(var.get(u'n'), Js([PyJs_Object_492_, PyJs_Object_500_, PyJs_Object_502_, PyJs_Object_504_, PyJs_Object_506_, PyJs_Object_508_, PyJs_Object_510_, PyJs_Object_512_])),var.get(u'n'))
            PyJs_anonymous_490_._set_name(u'anonymous')
            var.put(u'w', PyJs_anonymous_490_(var.get(u'd')))
            PyJs_Object_514_ = Js({})
            if PyJsComma(PyJsComma(var.get(u'w').put(u'requestsCount', Js(0.0)),var.get(u'w').put(u'requests', PyJs_Object_514_)),(Js(u'undefined')!=var.get(u'document',throw=False).typeof())):
                if (Js(u'function')==var.get(u'attachEvent',throw=False).typeof()):
                    var.get(u'attachEvent')(Js(u'onunload'), var.get(u'_'))
                else:
                    if (Js(u'function')==var.get(u'addEventListener',throw=False).typeof()):
                        var.get(u'addEventListener')((Js(u'pagehide') if var.get(u'b').contains(Js(u'onpagehide')) else Js(u'unload')), var.get(u'_'), Js(1.0).neg())
            pass
            PyJsComma(var.get(u't').put(u'exports', var.get(u'k')),var.get(u't').get(u'exports').put(u'Request', var.get(u'w')))
        PyJs_anonymous_463_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_515_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'e', u'i', u'o', u'n', u's', u'r', u't'])
            var.put(u'r', var.get(u'n')(Js(11.0)).get(u'PACKET_TYPES'))
            var.put(u'o', ((Js(u'function')==var.get(u'Blob',throw=False).typeof()) or ((Js(u'undefined')!=var.get(u'Blob',throw=False).typeof()) and PyJsStrictEq(Js(u'[object BlobConstructor]'),var.get(u'Object').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Blob'))))))
            var.put(u'i', (Js(u'function')==var.get(u'ArrayBuffer',throw=False).typeof()))
            @Js
            def PyJs_anonymous_516_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't', u'n'])
                var.put(u'n', var.get(u'FileReader').create())
                @Js
                def PyJs_anonymous_517_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u't'])
                    var.put(u't', var.get(u'n').get(u'result').callprop(u'split', Js(u',')).get(u'1'))
                    var.get(u'e')((Js(u'b')+var.get(u't')))
                PyJs_anonymous_517_._set_name(u'anonymous')
                return PyJsComma(var.get(u'n').put(u'onload', PyJs_anonymous_517_),var.get(u'n').callprop(u'readAsDataURL', var.get(u't')))
            PyJs_anonymous_516_._set_name(u'anonymous')
            var.put(u's', PyJs_anonymous_516_)
            @Js
            def PyJs_anonymous_518_(t, e, n, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                var.registers([u'a', u'c', u'e', u'n', u'u', u't'])
                var.put(u'a', var.get(u't').get(u'type'))
                var.put(u'u', var.get(u't').get(u'data'))
                def PyJs_LONG_519_(var=var):
                    return ((var.get(u'n')((var.get(u'u') if var.get(u'u').instanceof(var.get(u'ArrayBuffer')) else var.get(u'u').get(u'buffer'))) if var.get(u'e') else var.get(u's')(var.get(u'Blob').create(Js([var.get(u'u')])), var.get(u'n'))) if (var.get(u'i') and (var.get(u'u').instanceof(var.get(u'ArrayBuffer')) or PyJsComma(var.put(u'c', var.get(u'u')),(var.get(u'ArrayBuffer').callprop(u'isView', var.get(u'c')) if (Js(u'function')==var.get(u'ArrayBuffer').get(u'isView').typeof()) else (var.get(u'c') and var.get(u'c').get(u'buffer').instanceof(var.get(u'ArrayBuffer'))))))) else var.get(u'n')((var.get(u'r').get(var.get(u'a'))+(var.get(u'u') or Js(u'')))))
                return ((var.get(u'n')(var.get(u'u')) if var.get(u'e') else var.get(u's')(var.get(u'u'), var.get(u'n'))) if (var.get(u'o') and var.get(u'u').instanceof(var.get(u'Blob'))) else PyJs_LONG_519_())
            PyJs_anonymous_518_._set_name(u'anonymous')
            var.get(u't').put(u'exports', PyJs_anonymous_518_)
        PyJs_anonymous_515_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_520_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'i', u'o', u'n', u's', u'r', u't'])
            var.put(u'o', var.get(u'n')(Js(11.0)))
            var.put(u'i', var.get(u'o').get(u'PACKET_TYPES_REVERSE'))
            var.put(u's', var.get(u'o').get(u'ERROR_PACKET'))
            ((Js(u'function')==var.get(u'ArrayBuffer',throw=False).typeof()) and var.put(u'r', var.get(u'n')(Js(25.0))))
            @Js
            def PyJs_anonymous_521_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't', u'n'])
                if var.get(u'r'):
                    var.put(u'n', var.get(u'r').callprop(u'decode', var.get(u't')))
                    return var.get(u'a')(var.get(u'n'), var.get(u'e'))
                PyJs_Object_522_ = Js({u'base64':Js(0.0).neg(),u'data':var.get(u't')})
                return PyJs_Object_522_
            PyJs_anonymous_521_._set_name(u'anonymous')
            var.put(u'c', PyJs_anonymous_521_)
            @Js
            def PyJs_anonymous_523_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get(u'e'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'blob')):
                        SWITCHED = True
                        return (var.get(u'Blob').create(Js([var.get(u't')])) if var.get(u't').instanceof(var.get(u'ArrayBuffer')) else var.get(u't'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(u'arraybuffer')):
                        SWITCHED = True
                        pass
                    if True:
                        SWITCHED = True
                        return var.get(u't')
                    SWITCHED = True
                    break
            PyJs_anonymous_523_._set_name(u'anonymous')
            var.put(u'a', PyJs_anonymous_523_)
            @Js
            def PyJs_anonymous_524_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't', u'n'])
                if (Js(u'string')!=var.get(u't',throw=False).typeof()):
                    PyJs_Object_525_ = Js({u'type':Js(u'message'),u'data':var.get(u'a')(var.get(u't'), var.get(u'e'))})
                    return PyJs_Object_525_
                var.put(u'n', var.get(u't').callprop(u'charAt', Js(0.0)))
                PyJs_Object_526_ = Js({u'type':Js(u'message'),u'data':var.get(u'c')(var.get(u't').callprop(u'substring', Js(1.0)), var.get(u'e'))})
                PyJs_Object_527_ = Js({u'type':var.get(u'i').get(var.get(u'n')),u'data':var.get(u't').callprop(u'substring', Js(1.0))})
                PyJs_Object_528_ = Js({u'type':var.get(u'i').get(var.get(u'n'))})
                return (PyJs_Object_526_ if PyJsStrictEq(Js(u'b'),var.get(u'n')) else ((PyJs_Object_527_ if (var.get(u't').get(u'length')>Js(1.0)) else PyJs_Object_528_) if var.get(u'i').get(var.get(u'n')) else var.get(u's')))
            PyJs_anonymous_524_._set_name(u'anonymous')
            var.get(u't').put(u'exports', PyJs_anonymous_524_)
        PyJs_anonymous_520_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_529_(t, e, this, arguments, var=var):
            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
            var.registers([u'e', u't'])
            @Js
            def PyJs_anonymous_530_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                Js(u'use strict')
                @Js
                def PyJs_anonymous_531_(e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                    var.registers([u'i', u'r', u'e', u'o', u'n'])
                    var.put(u'r', var.get(u'Uint8Array').create(var.get(u'e')))
                    var.put(u'o', var.get(u'r').get(u'length'))
                    var.put(u'i', Js(u''))
                    #for JS loop
                    var.put(u'n', Js(0.0))
                    while (var.get(u'n')<var.get(u'o')):
                        try:
                            def PyJs_LONG_532_(var=var):
                                return PyJsComma(PyJsComma(PyJsComma(var.put(u'i', var.get(u't').get((var.get(u'r').get(var.get(u'n'))>>Js(2.0))), u'+'),var.put(u'i', var.get(u't').get((((Js(3.0)&var.get(u'r').get(var.get(u'n')))<<Js(4.0))|(var.get(u'r').get((var.get(u'n')+Js(1.0)))>>Js(4.0)))), u'+')),var.put(u'i', var.get(u't').get((((Js(15.0)&var.get(u'r').get((var.get(u'n')+Js(1.0))))<<Js(2.0))|(var.get(u'r').get((var.get(u'n')+Js(2.0)))>>Js(6.0)))), u'+')),var.put(u'i', var.get(u't').get((Js(63.0)&var.get(u'r').get((var.get(u'n')+Js(2.0))))), u'+'))
                            PyJs_LONG_532_()
                        finally:
                                var.put(u'n', Js(3.0), u'+')
                    return PyJsComma((var.put(u'i', (var.get(u'i').callprop(u'substring', Js(0.0), (var.get(u'i').get(u'length')-Js(1.0)))+Js(u'='))) if ((var.get(u'o')%Js(3.0))==Js(2.0)) else (((var.get(u'o')%Js(3.0))==Js(1.0)) and var.put(u'i', (var.get(u'i').callprop(u'substring', Js(0.0), (var.get(u'i').get(u'length')-Js(2.0)))+Js(u'=='))))),var.get(u'i'))
                PyJs_anonymous_531_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_533_(e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                    var.registers([u'a', u'c', u'e', u'f', u'i', u'o', u'n', u'p', u's', u'r', u'u'])
                    var.put(u'c', (Js(0.75)*var.get(u'e').get(u'length')))
                    var.put(u'a', var.get(u'e').get(u'length'))
                    var.put(u'u', Js(0.0))
                    (PyJsStrictEq(Js(u'='),var.get(u'e').get((var.get(u'e').get(u'length')-Js(1.0)))) and PyJsComma((var.put(u'c',Js(var.get(u'c').to_number())-Js(1))+Js(1)),(PyJsStrictEq(Js(u'='),var.get(u'e').get((var.get(u'e').get(u'length')-Js(2.0)))) and (var.put(u'c',Js(var.get(u'c').to_number())-Js(1))+Js(1)))))
                    var.put(u'f', var.get(u'ArrayBuffer').create(var.get(u'c')))
                    var.put(u'p', var.get(u'Uint8Array').create(var.get(u'f')))
                    #for JS loop
                    var.put(u'n', Js(0.0))
                    while (var.get(u'n')<var.get(u'a')):
                        try:
                            def PyJs_LONG_534_(var=var):
                                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put(u'r', var.get(u't').callprop(u'indexOf', var.get(u'e').get(var.get(u'n')))),var.put(u'o', var.get(u't').callprop(u'indexOf', var.get(u'e').get((var.get(u'n')+Js(1.0)))))),var.put(u'i', var.get(u't').callprop(u'indexOf', var.get(u'e').get((var.get(u'n')+Js(2.0)))))),var.put(u's', var.get(u't').callprop(u'indexOf', var.get(u'e').get((var.get(u'n')+Js(3.0)))))),var.get(u'p').put((var.put(u'u',Js(var.get(u'u').to_number())+Js(1))-Js(1)), ((var.get(u'r')<<Js(2.0))|(var.get(u'o')>>Js(4.0))))),var.get(u'p').put((var.put(u'u',Js(var.get(u'u').to_number())+Js(1))-Js(1)), (((Js(15.0)&var.get(u'o'))<<Js(4.0))|(var.get(u'i')>>Js(2.0))))),var.get(u'p').put((var.put(u'u',Js(var.get(u'u').to_number())+Js(1))-Js(1)), (((Js(3.0)&var.get(u'i'))<<Js(6.0))|(Js(63.0)&var.get(u's')))))
                            PyJs_LONG_534_()
                        finally:
                                var.put(u'n', Js(4.0), u'+')
                    return var.get(u'f')
                PyJs_anonymous_533_._set_name(u'anonymous')
                PyJsComma(var.get(u'e').put(u'encode', PyJs_anonymous_531_),var.get(u'e').put(u'decode', PyJs_anonymous_533_))
            PyJs_anonymous_530_._set_name(u'anonymous')
            PyJs_anonymous_530_(Js(u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')).neg()
        PyJs_anonymous_529_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_535_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'e', u'd', u'f', u'i', u'h', u'l', u'o', u'n', u'p', u's', u'r', u'u', u't', u'v', u'y'])
            @Js
            def PyJsHoisted_a_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                return (var.get(u'u')(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_541_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_542_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_542_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_542_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_91920254 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_91920254 is not None:
                                var.own[u't'] = PyJsHolder_74_91920254
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_91920254
                PyJs_anonymous_541_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_541_())
                @Js
                def PyJs_anonymous_543_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'f')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'f')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'a')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_543_._set_name(u'anonymous')
                return PyJs_anonymous_543_
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_f_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_544_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_544_._set_name(u'anonymous')
                return var.put(u'f', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_544_))(var.get(u't'))
            PyJsHoisted_f_.func_name = u'f'
            var.put(u'f', PyJsHoisted_f_)
            @Js
            def PyJsHoisted_i_(t, e, n, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                var.registers([u'e', u't', u'n'])
                @Js
                def PyJs_anonymous_538_(t, e, n, this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
                    var.registers([u'r', u'e', u't', u'o', u'n'])
                    @Js
                    def PyJs_anonymous_539_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        #for JS loop
                        
                        while (var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u't'), var.get(u'e')).neg() and PyJsStrictNeq(var.get(u"null"),var.put(u't', var.get(u'f')(var.get(u't'))))):
                            pass
                        
                        return var.get(u't')
                    PyJs_anonymous_539_._set_name(u'anonymous')
                    var.put(u'r', PyJs_anonymous_539_(var.get(u't'), var.get(u'e')))
                    if var.get(u'r'):
                        var.put(u'o', var.get(u'Object').callprop(u'getOwnPropertyDescriptor', var.get(u'r'), var.get(u'e')))
                        return (var.get(u'o').get(u'get').callprop(u'call', var.get(u'n')) if var.get(u'o').get(u'get') else var.get(u'o').get(u'value'))
                PyJs_anonymous_538_._set_name(u'anonymous')
                return var.put(u'i', (var.get(u'Reflect').get(u'get') if ((Js(u'undefined')!=var.get(u'Reflect',throw=False).typeof()) and var.get(u'Reflect').get(u'get')) else PyJs_anonymous_538_))(var.get(u't'), var.get(u'e'), (var.get(u'n') or var.get(u't')))
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_o_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_s_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_540_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_540_._set_name(u'anonymous')
                return var.put(u's', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_540_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_536_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_536_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_537_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_537_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_536_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_537_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            @Js
            def PyJsHoisted_u_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                    PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                    raise PyJsTempException
                return var.get(u't')
            PyJsHoisted_u_.func_name = u'u'
            var.put(u'u', PyJsHoisted_u_)
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            var.put(u'l', var.get(u'n')(Js(10.0)))
            var.put(u'h', var.get(u'n')(Js(2.0)))
            var.put(u'y', JsRegExp(u'/\\n/g'))
            var.put(u'd', JsRegExp(u'/\\\\n/g'))
            @Js
            def PyJs_anonymous_545_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'e', u'l', u'n', u'r', u't'])
                @Js
                def PyJsHoisted_l_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    pass
                    @Js
                    def PyJs_anonymous_549_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        if var.get(u't').instanceof(var.get(u'e')).neg():
                            PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                            raise PyJsTempException
                    PyJs_anonymous_549_._set_name(u'anonymous')
                    PyJs_Object_550_ = Js({})
                    PyJsComma(PyJsComma(PyJsComma(PyJs_anonymous_549_(var.get(u"this"), var.get(u'l')).neg(),var.put(u'e', var.get(u'a').callprop(u'call', var.get(u"this"), var.get(u't'))).put(u'query', (var.get(u'e').get(u'query') or PyJs_Object_550_))),(var.get(u'p') or var.put(u'p', var.get(u'h').put(u'___eio', (var.get(u'h').get(u'___eio') or Js([])))))),var.get(u'e').put(u'index', var.get(u'p').get(u'length')))
                    var.put(u'n', var.get(u'u')(var.get(u'e')))
                    @Js
                    def PyJs_anonymous_551_(t, this, arguments, var=var):
                        var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                        var.registers([u't'])
                        var.get(u'n').callprop(u'onData', var.get(u't'))
                    PyJs_anonymous_551_._set_name(u'anonymous')
                    return PyJsComma(PyJsComma(var.get(u'p').callprop(u'push', PyJs_anonymous_551_),var.get(u'e').get(u'query').put(u'j', var.get(u'e').get(u'index'))),var.get(u'e'))
                PyJsHoisted_l_.func_name = u'l'
                var.put(u'l', PyJsHoisted_l_)
                @Js
                def PyJs_anonymous_546_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                        PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                        raise PyJsTempException
                    PyJs_Object_548_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                    PyJs_Object_547_ = Js({u'constructor':PyJs_Object_548_})
                    PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_547_)),(var.get(u'e') and var.get(u's')(var.get(u't'), var.get(u'e'))))
                PyJs_anonymous_546_._set_name(u'anonymous')
                PyJs_anonymous_546_(var.get(u'l'), var.get(u't')).neg()
                var.put(u'a', var.get(u'c')(var.get(u'l')))
                pass
                @Js
                def PyJs_anonymous_553_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    def PyJs_LONG_555_(var=var):
                        @Js
                        def PyJs_anonymous_554_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_554_._set_name(u'anonymous')
                        return PyJsComma(PyJsComma((var.get(u"this").get(u'script') and PyJsComma(PyJsComma(var.get(u"this").get(u'script').put(u'onerror', PyJs_anonymous_554_),var.get(u"this").get(u'script').get(u'parentNode').callprop(u'removeChild', var.get(u"this").get(u'script'))),var.get(u"this").put(u'script', var.get(u"null")))),(var.get(u"this").get(u'form') and PyJsComma(PyJsComma(var.get(u"this").get(u'form').get(u'parentNode').callprop(u'removeChild', var.get(u"this").get(u'form')),var.get(u"this").put(u'form', var.get(u"null"))),var.get(u"this").put(u'iframe', var.get(u"null"))))),var.get(u'i')(var.get(u'f')(var.get(u'l').get(u'prototype')), Js(u'doClose'), var.get(u"this")).callprop(u'call', var.get(u"this")))
                    PyJs_LONG_555_()
                PyJs_anonymous_553_._set_name(u'anonymous')
                PyJs_Object_552_ = Js({u'key':Js(u'doClose'),u'value':PyJs_anonymous_553_})
                @Js
                def PyJs_anonymous_557_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    var.put(u't', var.get(u"this"))
                    var.put(u'e', var.get(u'document').callprop(u'createElement', Js(u'script')))
                    @Js
                    def PyJs_anonymous_558_(e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                        var.registers([u'e'])
                        var.get(u't').callprop(u'onError', Js(u'jsonp poll error'), var.get(u'e'))
                    PyJs_anonymous_558_._set_name(u'anonymous')
                    PyJsComma(PyJsComma(PyJsComma((var.get(u"this").get(u'script') and PyJsComma(var.get(u"this").get(u'script').get(u'parentNode').callprop(u'removeChild', var.get(u"this").get(u'script')),var.get(u"this").put(u'script', var.get(u"null")))),var.get(u'e').put(u'async', Js(0.0).neg())),var.get(u'e').put(u'src', var.get(u"this").callprop(u'uri'))),var.get(u'e').put(u'onerror', PyJs_anonymous_558_))
                    var.put(u'n', var.get(u'document').callprop(u'getElementsByTagName', Js(u'script')).get(u'0'))
                    def PyJs_LONG_560_(var=var):
                        @Js
                        def PyJs_anonymous_559_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([u't'])
                            var.put(u't', var.get(u'document').callprop(u'createElement', Js(u'iframe')))
                            PyJsComma(var.get(u'document').get(u'body').callprop(u'appendChild', var.get(u't')),var.get(u'document').get(u'body').callprop(u'removeChild', var.get(u't')))
                        PyJs_anonymous_559_._set_name(u'anonymous')
                        return PyJsComma(PyJsComma((var.get(u'n').get(u'parentNode').callprop(u'insertBefore', var.get(u'e'), var.get(u'n')) if var.get(u'n') else (var.get(u'document').get(u'head') or var.get(u'document').get(u'body')).callprop(u'appendChild', var.get(u'e'))),var.get(u"this").put(u'script', var.get(u'e'))),(((Js(u'undefined')!=var.get(u'navigator',throw=False).typeof()) and JsRegExp(u'/gecko/i').callprop(u'test', var.get(u'navigator').get(u'userAgent'))) and var.get(u'setTimeout')(PyJs_anonymous_559_, Js(100.0))))
                    PyJs_LONG_560_()
                PyJs_anonymous_557_._set_name(u'anonymous')
                PyJs_Object_556_ = Js({u'key':Js(u'doPoll'),u'value':PyJs_anonymous_557_})
                @Js
                def PyJs_anonymous_562_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'a', u'c', u'e', u'i', u'o', u'n', u's', u'r', u't'])
                    @Js
                    def PyJsHoisted_a_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([u't'])
                        if var.get(u'r').get(u'iframe'):
                            try:
                                var.get(u'r').get(u'form').callprop(u'removeChild', var.get(u'r').get(u'iframe'))
                            except PyJsException as PyJsTempException:
                                PyJsHolder_74_81102897 = var.own.get(u't')
                                var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                                try:
                                    var.get(u'r').callprop(u'onError', Js(u'jsonp polling iframe removal error'), var.get(u't'))
                                finally:
                                    if PyJsHolder_74_81102897 is not None:
                                        var.own[u't'] = PyJsHolder_74_81102897
                                    else:
                                        del var.own[u't']
                                    del PyJsHolder_74_81102897
                        try:
                            var.put(u't', ((Js(u'<iframe src="javascript:0" name="')+var.get(u'r').get(u'iframeId'))+Js(u'">')))
                            var.put(u'n', var.get(u'document').callprop(u'createElement', var.get(u't')))
                        except PyJsException as PyJsTempException:
                            PyJsHolder_74_93981479 = var.own.get(u't')
                            var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                            try:
                                PyJsComma(var.put(u'n', var.get(u'document').callprop(u'createElement', Js(u'iframe'))).put(u'name', var.get(u'r').get(u'iframeId')),var.get(u'n').put(u'src', Js(u'javascript:0')))
                            finally:
                                if PyJsHolder_74_93981479 is not None:
                                    var.own[u't'] = PyJsHolder_74_93981479
                                else:
                                    del var.own[u't']
                                del PyJsHolder_74_93981479
                        PyJsComma(PyJsComma(var.get(u'n').put(u'id', var.get(u'r').get(u'iframeId')),var.get(u'r').get(u'form').callprop(u'appendChild', var.get(u'n'))),var.get(u'r').put(u'iframe', var.get(u'n')))
                    PyJsHoisted_a_.func_name = u'a'
                    var.put(u'a', PyJsHoisted_a_)
                    @Js
                    def PyJsHoisted_c_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        PyJsComma(var.get(u'a')(),var.get(u'e')())
                    PyJsHoisted_c_.func_name = u'c'
                    var.put(u'c', PyJsHoisted_c_)
                    var.put(u'r', var.get(u"this"))
                    if var.get(u"this").get(u'form').neg():
                        var.put(u'o', var.get(u'document').callprop(u'createElement', Js(u'form')))
                        var.put(u'i', var.get(u'document').callprop(u'createElement', Js(u'textarea')))
                        var.put(u's', var.get(u"this").put(u'iframeId', (Js(u'eio_iframe_')+var.get(u"this").get(u'index'))))
                        def PyJs_LONG_563_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'o').put(u'className', Js(u'socketio')),var.get(u'o').get(u'style').put(u'position', Js(u'absolute'))),var.get(u'o').get(u'style').put(u'top', Js(u'-1000px'))),var.get(u'o').get(u'style').put(u'left', Js(u'-1000px'))),var.get(u'o').put(u'target', var.get(u's'))),var.get(u'o').put(u'method', Js(u'POST'))),var.get(u'o').callprop(u'setAttribute', Js(u'accept-charset'), Js(u'utf-8'))),var.get(u'i').put(u'name', Js(u'd'))),var.get(u'o').callprop(u'appendChild', var.get(u'i'))),var.get(u'document').get(u'body').callprop(u'appendChild', var.get(u'o'))),var.get(u"this").put(u'form', var.get(u'o'))),var.get(u"this").put(u'area', var.get(u'i')))
                        PyJs_LONG_563_()
                    pass
                    pass
                    PyJsComma(PyJsComma(PyJsComma(var.get(u"this").get(u'form').put(u'action', var.get(u"this").callprop(u'uri')),var.get(u'a')()),var.put(u't', var.get(u't').callprop(u'replace', var.get(u'd'), Js(u'\\\n')))),var.get(u"this").get(u'area').put(u'value', var.get(u't').callprop(u'replace', var.get(u'y'), Js(u'\\n'))))
                    try:
                        var.get(u"this").get(u'form').callprop(u'submit')
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_81538741 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            pass
                        finally:
                            if PyJsHolder_74_81538741 is not None:
                                var.own[u't'] = PyJsHolder_74_81538741
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_81538741
                    @Js
                    def PyJs_anonymous_564_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        (PyJsStrictEq(Js(u'complete'),var.get(u'r').get(u'iframe').get(u'readyState')) and var.get(u'c')())
                    PyJs_anonymous_564_._set_name(u'anonymous')
                    (var.get(u"this").get(u'iframe').put(u'onreadystatechange', PyJs_anonymous_564_) if var.get(u"this").get(u'iframe').get(u'attachEvent') else var.get(u"this").get(u'iframe').put(u'onload', var.get(u'c')))
                PyJs_anonymous_562_._set_name(u'anonymous')
                PyJs_Object_561_ = Js({u'key':Js(u'doWrite'),u'value':PyJs_anonymous_562_})
                @Js
                def PyJs_anonymous_566_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return Js(1.0).neg()
                PyJs_anonymous_566_._set_name(u'anonymous')
                PyJs_Object_565_ = Js({u'key':Js(u'supportsBinary'),u'get':PyJs_anonymous_566_})
                return PyJsComma(PyJsComma(PyJsComma(var.put(u'e', var.get(u'l')),(var.put(u'n', Js([PyJs_Object_552_, PyJs_Object_556_, PyJs_Object_561_, PyJs_Object_565_])) and var.get(u'o')(var.get(u'e').get(u'prototype'), var.get(u'n')))),(var.get(u'r') and var.get(u'o')(var.get(u'e'), var.get(u'r')))),var.get(u'l'))
            PyJs_anonymous_545_._set_name(u'anonymous')
            var.put(u'v', PyJs_anonymous_545_(var.get(u'l')))
            var.get(u't').put(u'exports', var.get(u'v'))
        PyJs_anonymous_535_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_567_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'a', u'c', u'b', u'e', u'd', u'g', u'f', u'i', u'h', u'm', u'l', u'o', u'n', u'p', u's', u'r', u'u', u't', u'v', u'y'])
            @Js
            def PyJsHoisted_a_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_575_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (var.get(u't').get(u'__proto__') or var.get(u'Object').callprop(u'getPrototypeOf', var.get(u't')))
                PyJs_anonymous_575_._set_name(u'anonymous')
                return var.put(u'a', (var.get(u'Object').get(u'getPrototypeOf') if var.get(u'Object').get(u'setPrototypeOf') else PyJs_anonymous_575_))(var.get(u't'))
            PyJsHoisted_a_.func_name = u'a'
            var.put(u'a', PyJsHoisted_a_)
            @Js
            def PyJsHoisted_c_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_574_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u't')):
                        PyJsTempException = JsToPyException(var.get(u'ReferenceError').create(Js(u"this hasn't been initialised - super() hasn't been called")))
                        raise PyJsTempException
                    return var.get(u't')
                PyJs_anonymous_574_._set_name(u'anonymous')
                return (PyJs_anonymous_574_(var.get(u't')) if (var.get(u'e').neg() or (PyJsStrictNeq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and (Js(u'function')!=var.get(u'e',throw=False).typeof()))) else var.get(u'e'))
            PyJsHoisted_c_.func_name = u'c'
            var.put(u'c', PyJsHoisted_c_)
            @Js
            def PyJsHoisted_i_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_570_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return PyJsComma(var.get(u't').put(u'__proto__', var.get(u'e')),var.get(u't'))
                PyJs_anonymous_570_._set_name(u'anonymous')
                return var.put(u'i', (var.get(u'Object').get(u'setPrototypeOf') or PyJs_anonymous_570_))(var.get(u't'), var.get(u'e'))
            PyJsHoisted_i_.func_name = u'i'
            var.put(u'i', PyJsHoisted_i_)
            @Js
            def PyJsHoisted_o_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'r', u'e', u't', u'n'])
                #for JS loop
                var.put(u'n', Js(0.0))
                while (var.get(u'n')<var.get(u'e').get(u'length')):
                    try:
                        var.put(u'r', var.get(u'e').get(var.get(u'n')))
                        PyJsComma(PyJsComma(PyJsComma(var.get(u'r').put(u'enumerable', (var.get(u'r').get(u'enumerable') or Js(1.0).neg())),var.get(u'r').put(u'configurable', Js(0.0).neg())),(var.get(u'r').contains(Js(u'value')) and var.get(u'r').put(u'writable', Js(0.0).neg()))),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'r').get(u'key'), var.get(u'r')))
                    finally:
                            (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
            PyJsHoisted_o_.func_name = u'o'
            var.put(u'o', PyJsHoisted_o_)
            @Js
            def PyJsHoisted_s_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_anonymous_571_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    if ((Js(u'undefined')==var.get(u'Reflect',throw=False).typeof()) or var.get(u'Reflect').get(u'construct').neg()):
                        return Js(1.0).neg()
                    if var.get(u'Reflect').get(u'construct').get(u'sham'):
                        return Js(1.0).neg()
                    if (Js(u'function')==var.get(u'Proxy',throw=False).typeof()):
                        return Js(0.0).neg()
                    try:
                        @Js
                        def PyJs_anonymous_572_(this, arguments, var=var):
                            var = Scope({u'this':this, u'arguments':arguments}, var)
                            var.registers([])
                            pass
                        PyJs_anonymous_572_._set_name(u'anonymous')
                        return PyJsComma(var.get(u'Date').get(u'prototype').get(u'toString').callprop(u'call', var.get(u'Reflect').callprop(u'construct', var.get(u'Date'), Js([]), PyJs_anonymous_572_)),Js(0.0).neg())
                    except PyJsException as PyJsTempException:
                        PyJsHolder_74_9567658 = var.own.get(u't')
                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                        try:
                            return Js(1.0).neg()
                        finally:
                            if PyJsHolder_74_9567658 is not None:
                                var.own[u't'] = PyJsHolder_74_9567658
                            else:
                                del var.own[u't']
                            del PyJsHolder_74_9567658
                PyJs_anonymous_571_._set_name(u'anonymous')
                var.put(u'e', PyJs_anonymous_571_())
                @Js
                def PyJs_anonymous_573_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'r', u'o', u'n'])
                    var.put(u'r', var.get(u'a')(var.get(u't')))
                    if var.get(u'e'):
                        var.put(u'o', var.get(u'a')(var.get(u"this")).get(u'constructor'))
                        var.put(u'n', var.get(u'Reflect').callprop(u'construct', var.get(u'r'), var.get(u'arguments'), var.get(u'o')))
                    else:
                        var.put(u'n', var.get(u'r').callprop(u'apply', var.get(u"this"), var.get(u'arguments')))
                    return var.get(u'c')(var.get(u"this"), var.get(u'n'))
                PyJs_anonymous_573_._set_name(u'anonymous')
                return PyJs_anonymous_573_
            PyJsHoisted_s_.func_name = u's'
            var.put(u's', PyJsHoisted_s_)
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_568_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_568_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_569_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_569_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_568_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_569_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            pass
            pass
            pass
            pass
            pass
            pass
            var.put(u'u', var.get(u'n')(Js(3.0)))
            var.put(u'f', var.get(u'n')(Js(1.0)))
            var.put(u'p', var.get(u'n')(Js(4.0)))
            var.put(u'l', var.get(u'n')(Js(12.0)))
            var.put(u'h', var.get(u'n')(Js(13.0)).get(u'pick'))
            var.put(u'y', var.get(u'n')(Js(28.0)))
            var.put(u'd', var.get(u'y').get(u'WebSocket'))
            var.put(u'v', var.get(u'y').get(u'usingBrowserWebSocket'))
            var.put(u'b', var.get(u'y').get(u'defaultBinaryType'))
            var.put(u'm', (((Js(u'undefined')!=var.get(u'navigator',throw=False).typeof()) and (Js(u'string')==var.get(u'navigator').get(u'product').typeof())) and PyJsStrictEq(Js(u'reactnative'),var.get(u'navigator').get(u'product').callprop(u'toLowerCase'))))
            @Js
            def PyJs_anonymous_576_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'a', u'c', u'e', u'n', u'r', u't'])
                @Js
                def PyJsHoisted_a_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    pass
                    @Js
                    def PyJs_anonymous_580_(t, e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                        var.registers([u'e', u't'])
                        if var.get(u't').instanceof(var.get(u'e')).neg():
                            PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Cannot call a class as a function')))
                            raise PyJsTempException
                    PyJs_anonymous_580_._set_name(u'anonymous')
                    return PyJsComma(PyJsComma(PyJs_anonymous_580_(var.get(u"this"), var.get(u'a')),var.put(u'e', var.get(u'c').callprop(u'call', var.get(u"this"), var.get(u't'))).put(u'supportsBinary', var.get(u't').get(u'forceBase64').neg())),var.get(u'e'))
                PyJsHoisted_a_.func_name = u'a'
                var.put(u'a', PyJsHoisted_a_)
                @Js
                def PyJs_anonymous_577_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    if ((Js(u'function')!=var.get(u'e',throw=False).typeof()) and PyJsStrictNeq(var.get(u"null"),var.get(u'e'))):
                        PyJsTempException = JsToPyException(var.get(u'TypeError').create(Js(u'Super expression must either be null or a function')))
                        raise PyJsTempException
                    PyJs_Object_579_ = Js({u'value':var.get(u't'),u'writable':Js(0.0).neg(),u'configurable':Js(0.0).neg()})
                    PyJs_Object_578_ = Js({u'constructor':PyJs_Object_579_})
                    PyJsComma(var.get(u't').put(u'prototype', var.get(u'Object').callprop(u'create', (var.get(u'e') and var.get(u'e').get(u'prototype')), PyJs_Object_578_)),(var.get(u'e') and var.get(u'i')(var.get(u't'), var.get(u'e'))))
                PyJs_anonymous_577_._set_name(u'anonymous')
                PyJs_anonymous_577_(var.get(u'a'), var.get(u't')).neg()
                var.put(u'c', var.get(u's')(var.get(u'a')))
                pass
                @Js
                def PyJs_anonymous_582_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    if var.get(u"this").callprop(u'check'):
                        var.put(u't', var.get(u"this").callprop(u'uri'))
                        var.put(u'e', var.get(u"this").get(u'opts').get(u'protocols'))
                        PyJs_Object_583_ = Js({})
                        var.put(u'n', (PyJs_Object_583_ if var.get(u'm') else var.get(u'h')(var.get(u"this").get(u'opts'), Js(u'agent'), Js(u'perMessageDeflate'), Js(u'pfx'), Js(u'key'), Js(u'passphrase'), Js(u'cert'), Js(u'ca'), Js(u'ciphers'), Js(u'rejectUnauthorized'), Js(u'localAddress'), Js(u'protocolVersion'), Js(u'origin'), Js(u'maxPayload'), Js(u'family'), Js(u'checkServerIdentity'))))
                        (var.get(u"this").get(u'opts').get(u'extraHeaders') and var.get(u'n').put(u'headers', var.get(u"this").get(u'opts').get(u'extraHeaders')))
                        try:
                            var.get(u"this").put(u'ws', ((var.get(u'd').create(var.get(u't'), var.get(u'e')) if var.get(u'e') else var.get(u'd').create(var.get(u't'))) if (var.get(u'v') and var.get(u'm').neg()) else var.get(u'd').create(var.get(u't'), var.get(u'e'), var.get(u'n'))))
                        except PyJsException as PyJsTempException:
                            PyJsHolder_74_80511751 = var.own.get(u't')
                            var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                            try:
                                return var.get(u"this").callprop(u'emit', Js(u'error'), var.get(u't'))
                            finally:
                                if PyJsHolder_74_80511751 is not None:
                                    var.own[u't'] = PyJsHolder_74_80511751
                                else:
                                    del var.own[u't']
                                del PyJsHolder_74_80511751
                        PyJsComma(var.get(u"this").get(u'ws').put(u'binaryType', (var.get(u"this").get(u'socket').get(u'binaryType') or var.get(u'b'))),var.get(u"this").callprop(u'addEventListeners'))
                PyJs_anonymous_582_._set_name(u'anonymous')
                PyJs_Object_581_ = Js({u'key':Js(u'doOpen'),u'value':PyJs_anonymous_582_})
                @Js
                def PyJs_anonymous_585_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u't'])
                    var.put(u't', var.get(u"this"))
                    @Js
                    def PyJs_anonymous_586_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        var.get(u't').callprop(u'onOpen')
                    PyJs_anonymous_586_._set_name(u'anonymous')
                    @Js
                    def PyJs_anonymous_587_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        var.get(u't').callprop(u'onClose')
                    PyJs_anonymous_587_._set_name(u'anonymous')
                    @Js
                    def PyJs_anonymous_588_(e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                        var.registers([u'e'])
                        var.get(u't').callprop(u'onData', var.get(u'e').get(u'data'))
                    PyJs_anonymous_588_._set_name(u'anonymous')
                    @Js
                    def PyJs_anonymous_589_(e, this, arguments, var=var):
                        var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                        var.registers([u'e'])
                        var.get(u't').callprop(u'onError', Js(u'websocket error'), var.get(u'e'))
                    PyJs_anonymous_589_._set_name(u'anonymous')
                    PyJsComma(PyJsComma(PyJsComma(var.get(u"this").get(u'ws').put(u'onopen', PyJs_anonymous_586_),var.get(u"this").get(u'ws').put(u'onclose', PyJs_anonymous_587_)),var.get(u"this").get(u'ws').put(u'onmessage', PyJs_anonymous_588_)),var.get(u"this").get(u'ws').put(u'onerror', PyJs_anonymous_589_))
                PyJs_anonymous_585_._set_name(u'anonymous')
                PyJs_Object_584_ = Js({u'key':Js(u'addEventListeners'),u'value':PyJs_anonymous_585_})
                @Js
                def PyJs_anonymous_591_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'o', u'n'])
                    var.put(u'e', var.get(u"this"))
                    var.get(u"this").put(u'writable', Js(1.0).neg())
                    #for JS loop
                    var.put(u'n', var.get(u't').get(u'length'))
                    var.put(u'r', Js(0.0))
                    var.put(u'o', var.get(u'n'))
                    while (var.get(u'r')<var.get(u'o')):
                        try:
                            @Js
                            def PyJs_anonymous_592_(t, this, arguments, var=var):
                                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                                var.registers([u't'])
                                @Js
                                def PyJs_anonymous_593_(r, this, arguments, var=var):
                                    var = Scope({u'this':this, u'r':r, u'arguments':arguments}, var)
                                    var.registers([u'r', u'o'])
                                    PyJs_Object_594_ = Js({})
                                    var.put(u'o', PyJs_Object_594_)
                                    def PyJs_LONG_595_(var=var):
                                        return PyJsComma((var.get(u't').get(u'options') and var.get(u'o').put(u'compress', var.get(u't').get(u'options').get(u'compress'))),((var.get(u'e').get(u'opts').get(u'perMessageDeflate') and ((var.get(u'Buffer').callprop(u'byteLength', var.get(u'r')) if (Js(u'string')==var.get(u'r',throw=False).typeof()) else var.get(u'r').get(u'length'))<var.get(u'e').get(u'opts').get(u'perMessageDeflate').get(u'threshold'))) and var.get(u'o').put(u'compress', Js(1.0).neg())))
                                    (var.get(u'v') or PyJs_LONG_595_())
                                    try:
                                        (var.get(u'e').get(u'ws').callprop(u'send', var.get(u'r')) if var.get(u'v') else var.get(u'e').get(u'ws').callprop(u'send', var.get(u'r'), var.get(u'o')))
                                    except PyJsException as PyJsTempException:
                                        PyJsHolder_74_26257412 = var.own.get(u't')
                                        var.force_own_put(u't', PyExceptionToJs(PyJsTempException))
                                        try:
                                            pass
                                        finally:
                                            if PyJsHolder_74_26257412 is not None:
                                                var.own[u't'] = PyJsHolder_74_26257412
                                            else:
                                                del var.own[u't']
                                            del PyJsHolder_74_26257412
                                    @Js
                                    def PyJs_anonymous_596_(this, arguments, var=var):
                                        var = Scope({u'this':this, u'arguments':arguments}, var)
                                        var.registers([])
                                        PyJsComma(var.get(u'e').put(u'writable', Js(0.0).neg()),var.get(u'e').callprop(u'emit', Js(u'drain')))
                                    PyJs_anonymous_596_._set_name(u'anonymous')
                                    (var.put(u'n',Js(var.get(u'n').to_number())-Js(1)) or PyJsComma(var.get(u'e').callprop(u'emit', Js(u'flush')),var.get(u'setTimeout')(PyJs_anonymous_596_, Js(0.0))))
                                PyJs_anonymous_593_._set_name(u'anonymous')
                                var.get(u'f').callprop(u'encodePacket', var.get(u't'), var.get(u'e').get(u'supportsBinary'), PyJs_anonymous_593_)
                            PyJs_anonymous_592_._set_name(u'anonymous')
                            PyJs_anonymous_592_(var.get(u't').get(var.get(u'r'))).neg()
                        finally:
                                (var.put(u'r',Js(var.get(u'r').to_number())+Js(1))-Js(1))
                PyJs_anonymous_591_._set_name(u'anonymous')
                PyJs_Object_590_ = Js({u'key':Js(u'write'),u'value':PyJs_anonymous_591_})
                @Js
                def PyJs_anonymous_598_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    var.get(u'u').get(u'prototype').get(u'onClose').callprop(u'call', var.get(u"this"))
                PyJs_anonymous_598_._set_name(u'anonymous')
                PyJs_Object_597_ = Js({u'key':Js(u'onClose'),u'value':PyJs_anonymous_598_})
                @Js
                def PyJs_anonymous_600_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get(u'ws')) and PyJsComma(var.get(u"this").get(u'ws').callprop(u'close'),var.get(u"this").put(u'ws', var.get(u"null"))))
                PyJs_anonymous_600_._set_name(u'anonymous')
                PyJs_Object_599_ = Js({u'key':Js(u'doClose'),u'value':PyJs_anonymous_600_})
                @Js
                def PyJs_anonymous_602_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    PyJs_Object_603_ = Js({})
                    var.put(u't', (var.get(u"this").get(u'query') or PyJs_Object_603_))
                    var.put(u'e', (Js(u'wss') if var.get(u"this").get(u'opts').get(u'secure') else Js(u'ws')))
                    var.put(u'n', Js(u''))
                    def PyJs_LONG_604_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(((var.get(u"this").get(u'opts').get(u'port') and ((PyJsStrictEq(Js(u'wss'),var.get(u'e')) and PyJsStrictNeq(Js(443.0),var.get(u'Number')(var.get(u"this").get(u'opts').get(u'port')))) or (PyJsStrictEq(Js(u'ws'),var.get(u'e')) and PyJsStrictNeq(Js(80.0),var.get(u'Number')(var.get(u"this").get(u'opts').get(u'port')))))) and var.put(u'n', (Js(u':')+var.get(u"this").get(u'opts').get(u'port')))),(var.get(u"this").get(u'opts').get(u'timestampRequests') and var.get(u't').put(var.get(u"this").get(u'opts').get(u'timestampParam'), var.get(u'l')()))),(var.get(u"this").get(u'supportsBinary') or var.get(u't').put(u'b64', Js(1.0)))),(var.put(u't', var.get(u'p').callprop(u'encode', var.get(u't'))).get(u'length') and var.put(u't', (Js(u'?')+var.get(u't'))))),(((((var.get(u'e')+Js(u'://'))+(((Js(u'[')+var.get(u"this").get(u'opts').get(u'hostname'))+Js(u']')) if PyJsStrictNeq((-Js(1.0)),var.get(u"this").get(u'opts').get(u'hostname').callprop(u'indexOf', Js(u':'))) else var.get(u"this").get(u'opts').get(u'hostname')))+var.get(u'n'))+var.get(u"this").get(u'opts').get(u'path'))+var.get(u't')))
                    return PyJs_LONG_604_()
                PyJs_anonymous_602_._set_name(u'anonymous')
                PyJs_Object_601_ = Js({u'key':Js(u'uri'),u'value':PyJs_anonymous_602_})
                @Js
                def PyJs_anonymous_606_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return (var.get(u'd').neg() or (var.get(u'd').contains(Js(u'__initialize')) and PyJsStrictEq(var.get(u"this").get(u'name'),var.get(u'a').get(u'prototype').get(u'name')))).neg()
                PyJs_anonymous_606_._set_name(u'anonymous')
                PyJs_Object_605_ = Js({u'key':Js(u'check'),u'value':PyJs_anonymous_606_})
                @Js
                def PyJs_anonymous_608_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    return Js(u'websocket')
                PyJs_anonymous_608_._set_name(u'anonymous')
                PyJs_Object_607_ = Js({u'key':Js(u'name'),u'get':PyJs_anonymous_608_})
                return PyJsComma(PyJsComma(PyJsComma(var.put(u'e', var.get(u'a')),(var.put(u'n', Js([PyJs_Object_581_, PyJs_Object_584_, PyJs_Object_590_, PyJs_Object_597_, PyJs_Object_599_, PyJs_Object_601_, PyJs_Object_605_, PyJs_Object_607_])) and var.get(u'o')(var.get(u'e').get(u'prototype'), var.get(u'n')))),(var.get(u'r') and var.get(u'o')(var.get(u'e'), var.get(u'r')))),var.get(u'a'))
            PyJs_anonymous_576_._set_name(u'anonymous')
            var.put(u'g', PyJs_anonymous_576_(var.get(u'u')))
            var.get(u't').put(u'exports', var.get(u'g'))
        PyJs_anonymous_567_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_609_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'r', u'e', u't', u'n'])
            var.put(u'r', var.get(u'n')(Js(2.0)))
            PyJs_Object_610_ = Js({u'WebSocket':(var.get(u'r').get(u'WebSocket') or var.get(u'r').get(u'MozWebSocket')),u'usingBrowserWebSocket':Js(0.0).neg(),u'defaultBinaryType':Js(u'arraybuffer')})
            var.get(u't').put(u'exports', PyJs_Object_610_)
        PyJs_anonymous_609_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_611_(t, e, n, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'e':e, u't':t, u'n':n}, var)
            var.registers([u'r', u'e', u't', u'o', u'n'])
            @Js
            def PyJsHoisted_r_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                @Js
                def PyJs_anonymous_612_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return var.get(u't',throw=False).typeof()
                PyJs_anonymous_612_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_613_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    return (Js(u'symbol') if (((var.get(u't') and (Js(u'function')==var.get(u'Symbol',throw=False).typeof())) and PyJsStrictEq(var.get(u't').get(u'constructor'),var.get(u'Symbol'))) and PyJsStrictNeq(var.get(u't'),var.get(u'Symbol').get(u'prototype'))) else var.get(u't',throw=False).typeof())
                PyJs_anonymous_613_._set_name(u'anonymous')
                return var.put(u'r', (PyJs_anonymous_612_ if ((Js(u'function')==var.get(u'Symbol',throw=False).typeof()) and (Js(u'symbol')==var.get(u'Symbol').get(u'iterator').typeof())) else PyJs_anonymous_613_))(var.get(u't'))
            PyJsHoisted_r_.func_name = u'r'
            var.put(u'r', PyJsHoisted_r_)
            Js(u'use strict')
            pass
            PyJs_Object_614_ = Js({u'value':Js(0.0).neg()})
            PyJsComma(var.get(u'Object').callprop(u'defineProperty', var.get(u'e'), Js(u'__esModule'), PyJs_Object_614_),var.get(u'e').put(u'reconstructPacket', var.get(u'e').put(u'deconstructPacket', PyJsComma(Js(0.0), Js(None)))))
            var.put(u'o', var.get(u'n')(Js(15.0)))
            @Js
            def PyJs_anonymous_615_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u'i', u'e', u't', u'n'])
                var.put(u'e', Js([]))
                var.put(u'n', var.get(u't').get(u'data'))
                var.put(u'i', var.get(u't'))
                @Js
                def PyJs_t_616_(e, n, this, arguments, var=var):
                    var = Scope({u'this':this, u't':PyJs_t_616_, u'e':e, u'arguments':arguments, u'n':n}, var)
                    var.registers([u'a', u'c', u'e', u'i', u'n', u's', u'u'])
                    if var.get(u'e').neg():
                        return var.get(u'e')
                    if var.get(u'o').callprop(u'isBinary', var.get(u'e')):
                        PyJs_Object_617_ = Js({u'_placeholder':Js(0.0).neg(),u'num':var.get(u'n').get(u'length')})
                        var.put(u'i', PyJs_Object_617_)
                        return PyJsComma(var.get(u'n').callprop(u'push', var.get(u'e')),var.get(u'i'))
                    if var.get(u'Array').callprop(u'isArray', var.get(u'e')):
                        #for JS loop
                        var.put(u's', var.get(u'Array').create(var.get(u'e').get(u'length')))
                        var.put(u'c', Js(0.0))
                        while (var.get(u'c')<var.get(u'e').get(u'length')):
                            try:
                                var.get(u's').put(var.get(u'c'), var.get(u't')(var.get(u'e').get(var.get(u'c')), var.get(u'n')))
                            finally:
                                    (var.put(u'c',Js(var.get(u'c').to_number())+Js(1))-Js(1))
                        return var.get(u's')
                    if (PyJsStrictEq(Js(u'object'),var.get(u'r')(var.get(u'e'))) and var.get(u'e').instanceof(var.get(u'Date')).neg()):
                        PyJs_Object_618_ = Js({})
                        var.put(u'a', PyJs_Object_618_)
                        for PyJsTemp in var.get(u'e'):
                            var.put(u'u', PyJsTemp)
                            (var.get(u'e').callprop(u'hasOwnProperty', var.get(u'u')) and var.get(u'a').put(var.get(u'u'), var.get(u't')(var.get(u'e').get(var.get(u'u')), var.get(u'n'))))
                        return var.get(u'a')
                    return var.get(u'e')
                PyJs_t_616_._set_name(u't')
                PyJs_Object_619_ = Js({u'packet':var.get(u'i'),u'buffers':var.get(u'e')})
                return PyJsComma(PyJsComma(var.get(u'i').put(u'data', PyJs_t_616_(var.get(u'n'), var.get(u'e'))),var.get(u'i').put(u'attachments', var.get(u'e').get(u'length'))),PyJs_Object_619_)
            PyJs_anonymous_615_._set_name(u'anonymous')
            @Js
            def PyJs_anonymous_620_(t, e, this, arguments, var=var):
                var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                var.registers([u'e', u't'])
                @Js
                def PyJs_t_621_(e, n, this, arguments, var=var):
                    var = Scope({u'this':this, u't':PyJs_t_621_, u'e':e, u'arguments':arguments, u'n':n}, var)
                    var.registers([u'i', u'e', u'o', u'n'])
                    if var.get(u'e').neg():
                        return var.get(u'e')
                    if (var.get(u'e') and var.get(u'e').get(u'_placeholder')):
                        return var.get(u'n').get(var.get(u'e').get(u'num'))
                    if var.get(u'Array').callprop(u'isArray', var.get(u'e')):
                        #for JS loop
                        var.put(u'o', Js(0.0))
                        while (var.get(u'o')<var.get(u'e').get(u'length')):
                            try:
                                var.get(u'e').put(var.get(u'o'), var.get(u't')(var.get(u'e').get(var.get(u'o')), var.get(u'n')))
                            finally:
                                    (var.put(u'o',Js(var.get(u'o').to_number())+Js(1))-Js(1))
                    else:
                        if PyJsStrictEq(Js(u'object'),var.get(u'r')(var.get(u'e'))):
                            for PyJsTemp in var.get(u'e'):
                                var.put(u'i', PyJsTemp)
                                (var.get(u'e').callprop(u'hasOwnProperty', var.get(u'i')) and var.get(u'e').put(var.get(u'i'), var.get(u't')(var.get(u'e').get(var.get(u'i')), var.get(u'n'))))
                    return var.get(u'e')
                PyJs_t_621_._set_name(u't')
                return PyJsComma(PyJsComma(var.get(u't').put(u'data', PyJs_t_621_(var.get(u't').get(u'data'), var.get(u'e'))),var.get(u't').put(u'attachments', PyJsComma(Js(0.0), Js(None)))),var.get(u't'))
            PyJs_anonymous_620_._set_name(u'anonymous')
            PyJsComma(var.get(u'e').put(u'deconstructPacket', PyJs_anonymous_615_),var.get(u'e').put(u'reconstructPacket', PyJs_anonymous_620_))
        PyJs_anonymous_611_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_622_(t, e, this, arguments, var=var):
            var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
            var.registers([u'e', u't', u'n'])
            @Js
            def PyJsHoisted_n_(t, this, arguments, var=var):
                var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                var.registers([u't'])
                def PyJs_LONG_624_(var=var):
                    PyJs_Object_623_ = Js({})
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put(u't', (var.get(u't') or PyJs_Object_623_)),var.get(u"this").put(u'ms', (var.get(u't').get(u'min') or Js(100.0)))),var.get(u"this").put(u'max', (var.get(u't').get(u'max') or Js(10000.0)))),var.get(u"this").put(u'factor', (var.get(u't').get(u'factor') or Js(2.0)))),var.get(u"this").put(u'jitter', (var.get(u't').get(u'jitter') if ((var.get(u't').get(u'jitter')>Js(0.0)) and (var.get(u't').get(u'jitter')<=Js(1.0))) else Js(0.0)))),var.get(u"this").put(u'attempts', Js(0.0)))
                PyJs_LONG_624_()
            PyJsHoisted_n_.func_name = u'n'
            var.put(u'n', PyJsHoisted_n_)
            pass
            def PyJs_LONG_630_(var=var):
                @Js
                def PyJs_anonymous_625_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([u'e', u't', u'n'])
                    var.put(u't', (var.get(u"this").get(u'ms')*var.get(u'Math').callprop(u'pow', var.get(u"this").get(u'factor'), (var.get(u"this").put(u'attempts',Js(var.get(u"this").get(u'attempts').to_number())+Js(1))-Js(1)))))
                    if var.get(u"this").get(u'jitter'):
                        var.put(u'e', var.get(u'Math').callprop(u'random'))
                        var.put(u'n', var.get(u'Math').callprop(u'floor', ((var.get(u'e')*var.get(u"this").get(u'jitter'))*var.get(u't'))))
                        var.put(u't', ((var.get(u't')-var.get(u'n')) if (Js(0.0)==(Js(1.0)&var.get(u'Math').callprop(u'floor', (Js(10.0)*var.get(u'e'))))) else (var.get(u't')+var.get(u'n'))))
                    return (Js(0.0)|var.get(u'Math').callprop(u'min', var.get(u't'), var.get(u"this").get(u'max')))
                PyJs_anonymous_625_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_626_(this, arguments, var=var):
                    var = Scope({u'this':this, u'arguments':arguments}, var)
                    var.registers([])
                    var.get(u"this").put(u'attempts', Js(0.0))
                PyJs_anonymous_626_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_627_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    var.get(u"this").put(u'ms', var.get(u't'))
                PyJs_anonymous_627_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_628_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    var.get(u"this").put(u'max', var.get(u't'))
                PyJs_anonymous_628_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_629_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    var.get(u"this").put(u'jitter', var.get(u't'))
                PyJs_anonymous_629_._set_name(u'anonymous')
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u't').put(u'exports', var.get(u'n')),var.get(u'n').get(u'prototype').put(u'duration', PyJs_anonymous_625_)),var.get(u'n').get(u'prototype').put(u'reset', PyJs_anonymous_626_)),var.get(u'n').get(u'prototype').put(u'setMin', PyJs_anonymous_627_)),var.get(u'n').get(u'prototype').put(u'setMax', PyJs_anonymous_628_)),var.get(u'n').get(u'prototype').put(u'setJitter', PyJs_anonymous_629_))
            PyJs_LONG_630_()
        PyJs_anonymous_622_._set_name(u'anonymous')
        @Js
        def PyJs_anonymous_631_(t, this, arguments, var=var):
            var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
            var.registers([u'e', u't', u'n'])
            @Js
            def PyJsHoisted_n_(r, this, arguments, var=var):
                var = Scope({u'this':this, u'r':r, u'arguments':arguments}, var)
                var.registers([u'r', u'o'])
                if var.get(u'e').get(var.get(u'r')):
                    return var.get(u'e').get(var.get(u'r')).get(u'exports')
                PyJs_Object_634_ = Js({})
                PyJs_Object_633_ = Js({u'i':var.get(u'r'),u'l':Js(1.0).neg(),u'exports':PyJs_Object_634_})
                var.put(u'o', var.get(u'e').put(var.get(u'r'), PyJs_Object_633_))
                return PyJsComma(PyJsComma(var.get(u't').get(var.get(u'r')).callprop(u'call', var.get(u'o').get(u'exports'), var.get(u'o'), var.get(u'o').get(u'exports'), var.get(u'n')),var.get(u'o').put(u'l', Js(0.0).neg())),var.get(u'o').get(u'exports'))
            PyJsHoisted_n_.func_name = u'n'
            var.put(u'n', PyJsHoisted_n_)
            PyJs_Object_632_ = Js({})
            var.put(u'e', PyJs_Object_632_)
            pass
            def PyJs_LONG_647_(var=var):
                @Js
                def PyJs_anonymous_635_(t, e, r, this, arguments, var=var):
                    var = Scope({u'this':this, u'r':r, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't'])
                    PyJs_Object_636_ = Js({u'enumerable':Js(0.0).neg(),u'get':var.get(u'r')})
                    (var.get(u'n').callprop(u'o', var.get(u't'), var.get(u'e')) or var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'e'), PyJs_Object_636_))
                PyJs_anonymous_635_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_637_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u't'])
                    PyJs_Object_638_ = Js({u'value':Js(u'Module')})
                    PyJs_Object_639_ = Js({u'value':Js(0.0).neg()})
                    PyJsComma((((Js(u'undefined')!=var.get(u'Symbol',throw=False).typeof()) and var.get(u'Symbol').get(u'toStringTag')) and var.get(u'Object').callprop(u'defineProperty', var.get(u't'), var.get(u'Symbol').get(u'toStringTag'), PyJs_Object_638_)),var.get(u'Object').callprop(u'defineProperty', var.get(u't'), Js(u'__esModule'), PyJs_Object_639_))
                PyJs_anonymous_637_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_640_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'r', u'e', u't', u'o'])
                    if PyJsComma(((Js(1.0)&var.get(u'e')) and var.put(u't', var.get(u'n')(var.get(u't')))),(Js(8.0)&var.get(u'e'))):
                        return var.get(u't')
                    if ((((Js(4.0)&var.get(u'e')) and (Js(u'object')==var.get(u't',throw=False).typeof())) and var.get(u't')) and var.get(u't').get(u'__esModule')):
                        return var.get(u't')
                    var.put(u'r', var.get(u'Object').callprop(u'create', var.get(u"null")))
                    PyJs_Object_641_ = Js({u'enumerable':Js(0.0).neg(),u'value':var.get(u't')})
                    if PyJsComma(PyJsComma(var.get(u'n').callprop(u'r', var.get(u'r')),var.get(u'Object').callprop(u'defineProperty', var.get(u'r'), Js(u'default'), PyJs_Object_641_)),((Js(2.0)&var.get(u'e')) and (Js(u'string')!=var.get(u't',throw=False).typeof()))):
                        for PyJsTemp in var.get(u't'):
                            var.put(u'o', PyJsTemp)
                            @Js
                            def PyJs_anonymous_642_(e, this, arguments, var=var):
                                var = Scope({u'this':this, u'e':e, u'arguments':arguments}, var)
                                var.registers([u'e'])
                                return var.get(u't').get(var.get(u'e'))
                            PyJs_anonymous_642_._set_name(u'anonymous')
                            var.get(u'n').callprop(u'd', var.get(u'r'), var.get(u'o'), PyJs_anonymous_642_.callprop(u'bind', var.get(u"null"), var.get(u'o')))
                    return var.get(u'r')
                PyJs_anonymous_640_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_643_(t, this, arguments, var=var):
                    var = Scope({u'this':this, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    @Js
                    def PyJs_anonymous_644_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return var.get(u't').get(u'default')
                    PyJs_anonymous_644_._set_name(u'anonymous')
                    @Js
                    def PyJs_anonymous_645_(this, arguments, var=var):
                        var = Scope({u'this':this, u'arguments':arguments}, var)
                        var.registers([])
                        return var.get(u't')
                    PyJs_anonymous_645_._set_name(u'anonymous')
                    var.put(u'e', (PyJs_anonymous_644_ if (var.get(u't') and var.get(u't').get(u'__esModule')) else PyJs_anonymous_645_))
                    return PyJsComma(var.get(u'n').callprop(u'd', var.get(u'e'), Js(u'a'), var.get(u'e')),var.get(u'e'))
                PyJs_anonymous_643_._set_name(u'anonymous')
                @Js
                def PyJs_anonymous_646_(t, e, this, arguments, var=var):
                    var = Scope({u'this':this, u'e':e, u't':t, u'arguments':arguments}, var)
                    var.registers([u'e', u't'])
                    return var.get(u'Object').get(u'prototype').get(u'hasOwnProperty').callprop(u'call', var.get(u't'), var.get(u'e'))
                PyJs_anonymous_646_._set_name(u'anonymous')
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u'n').put(u'm', var.get(u't')),var.get(u'n').put(u'c', var.get(u'e'))),var.get(u'n').put(u'd', PyJs_anonymous_635_)),var.get(u'n').put(u'r', PyJs_anonymous_637_)),var.get(u'n').put(u't', PyJs_anonymous_640_)),var.get(u'n').put(u'n', PyJs_anonymous_643_)),var.get(u'n').put(u'o', PyJs_anonymous_646_)),var.get(u'n').put(u'p', Js(u''))),var.get(u'n')(var.get(u'n').put(u's', Js(17.0))))
            return PyJs_LONG_647_()
        PyJs_anonymous_631_._set_name(u'anonymous')
        return PyJs_anonymous_631_(Js([PyJs_anonymous_1_, PyJs_anonymous_15_, PyJs_anonymous_21_, PyJs_anonymous_22_, PyJs_anonymous_52_, PyJs_anonymous_56_, PyJs_anonymous_100_, PyJs_anonymous_108_, PyJs_anonymous_190_, PyJs_anonymous_192_, PyJs_anonymous_194_, PyJs_anonymous_232_, PyJs_anonymous_236_, PyJs_anonymous_239_, PyJs_anonymous_243_, PyJs_anonymous_347_, PyJs_anonymous_353_, PyJs_anonymous_357_, PyJs_anonymous_370_, PyJs_anonymous_376_, PyJs_anonymous_379_, PyJs_anonymous_462_, PyJs_anonymous_463_, PyJs_anonymous_515_, PyJs_anonymous_520_, PyJs_anonymous_529_, PyJs_anonymous_535_, PyJs_anonymous_567_, PyJs_anonymous_609_, PyJs_anonymous_611_, PyJs_anonymous_622_]))
    return PyJs_LONG_648_()
PyJs_anonymous_0_._set_name(u'anonymous')
