import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_112 = relay.var("var_112", dtype = "int32", shape = (2, 15, 3))#candidate|112|(2, 15, 3)|var|int32
var_113 = relay.var("var_113", dtype = "int32", shape = (2, 15, 3))#candidate|113|(2, 15, 3)|var|int32
bop_114 = relay.maximum(var_112.astype('int32'), relay.reshape(var_113.astype('int32'), relay.shape_of(var_112))) # shape=(2, 15, 3)
output = bop_114
output2 = bop_114
func_128 = relay.Function([var_112,var_113,], output)
mod['func_128'] = func_128
mod = relay.transform.InferType()(mod)
mutated_mod['func_128'] = func_128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_128_call = mutated_mod.get_global_var('func_128')
var_130 = relay.var("var_130", dtype = "int32", shape = (2, 15, 3))#candidate|130|(2, 15, 3)|var|int32
var_131 = relay.var("var_131", dtype = "int32", shape = (2, 15, 3))#candidate|131|(2, 15, 3)|var|int32
call_129 = func_128_call(var_130,var_131,)
output = call_129
func_132 = relay.Function([var_130,var_131,], output)
mutated_mod['func_132'] = func_132
mutated_mod = relay.transform.InferType()(mutated_mod)
const_484 = relay.const([[[-8,-5,-7,-2,-5,-9,-7,1,-6,-2,-4,-9,-10,5,7]],[[-2,-5,3,-1,2,1,-4,-2,8,-4,6,1,-4,6,-8]],[[3,9,4,-4,6,5,-9,-6,4,10,-6,-3,4,7,7]],[[7,7,2,8,8,-1,-3,-4,1,5,-5,10,8,-7,3]],[[2,8,6,1,-5,9,-6,8,1,9,3,-7,-3,-6,-9]],[[6,1,-1,3,2,-2,8,5,-9,9,2,-1,-6,3,-9]]], dtype = "uint8")#candidate|484|(6, 1, 15)|const|uint8
var_485 = relay.var("var_485", dtype = "uint8", shape = (6, 13, 15))#candidate|485|(6, 13, 15)|var|uint8
bop_486 = relay.less_equal(const_484.astype('bool'), var_485.astype('bool')) # shape=(6, 13, 15)
uop_489 = relay.acosh(bop_486.astype('float64')) # shape=(6, 13, 15)
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
call_492 = func_128_call(relay.reshape(const_484.astype('int32'), [2, 15, 3]), relay.reshape(const_484.astype('int32'), [2, 15, 3]), )
call_493 = func_128_call(relay.reshape(const_484.astype('int32'), [2, 15, 3]), relay.reshape(const_484.astype('int32'), [2, 15, 3]), )
output = relay.Tuple([uop_489,call_492,])
output2 = relay.Tuple([uop_489,call_493,])
func_498 = relay.Function([var_485,], output)
mod['func_498'] = func_498
mod = relay.transform.InferType()(mod)
mutated_mod['func_498'] = func_498
mutated_mod = relay.transform.InferType()(mutated_mod)
var_499 = relay.var("var_499", dtype = "uint8", shape = (6, 13, 15))#candidate|499|(6, 13, 15)|var|uint8
func_498_call = mutated_mod.get_global_var('func_498')
call_500 = func_498_call(var_499)
output = call_500
func_501 = relay.Function([var_499], output)
mutated_mod['func_501'] = func_501
mutated_mod = relay.transform.InferType()(mutated_mod)
var_947 = relay.var("var_947", dtype = "float32", shape = (6, 2, 1))#candidate|947|(6, 2, 1)|var|float32
var_948 = relay.var("var_948", dtype = "float32", shape = (6, 2, 13))#candidate|948|(6, 2, 13)|var|float32
bop_949 = relay.floor_mod(var_947.astype('float32'), var_948.astype('float32')) # shape=(6, 2, 13)
func_498_call = mod.get_global_var('func_498')
func_501_call = mutated_mod.get_global_var('func_501')
const_953 = relay.const([[-2,-4,7,9,10,7,-5,-1,-7,8,10,-7,7,7,-10,4,1,8,3,-9,-9,10,-3,4,3,-7,-8,-1,4,2,7,7,3,6,-5,10,1,7,-8,-6,-7,-8,-9,9,9,7,-5,-1,-2,-6,-4,-2,-8,-1,-1,9,-9,-2,8,-4,-1,2,-7,-6,-2,5,-3,-10,-5,-7,-9,-4,-5,-9,-8,-9,-5,-6,-6,1,-7,5,-1,-10,8,-3,-2,-7,5,-10,-10,1,2,8,-2,-7,3,-8,8,3,5,-3,4,4,6,10,4,1,-1,-7,8,-9,-7,7,6,1,7,8,4,1,-7,5,-4,-1,-5,-5,2,6,-2,-5,5,2,10,5,4,-3,5,-4,6,4,-6,6,3,-9,9,5,-10,7,-7,-3,6,-3,7,2,5,-7,-2,-10,9,2,-3,-1,4,-2,-8,-3,4,7,-3,7,4,-10,-10,-3,-8,-4,-4,4,1,-10,-3,-5,-10,10,-3,3,2,-6,-2,9,6,10,8,-7,-2,-10,-3,-3,7,-6,2,-8,3,-9,4,6,3,7,2,10,2,-10,-5,8,8,-2,3,7,3,2,3,-7,-8,6,10,-5,-6,-9,-7,2,-1,6,-6,2],[8,-7,4,5,-10,-3,1,-5,10,-9,-1,2,7,9,-2,5,7,-9,7,4,-9,8,-2,6,-8,-10,-7,-2,2,-10,-2,-4,-8,-1,-9,2,1,-7,-4,-6,-9,9,1,-4,3,-9,8,6,-6,-9,-2,-4,-3,-6,5,7,-10,-2,10,-8,-10,9,-2,-4,-10,5,5,4,2,5,6,3,-10,1,-3,-4,7,2,8,8,-10,1,4,-5,9,-4,-2,3,4,-4,2,-9,-1,6,7,-7,-9,-4,6,-1,-1,-10,-4,7,-6,4,-8,4,-3,9,6,-9,-6,10,-6,9,-6,2,-3,-7,-9,4,3,7,8,-8,-5,9,-3,5,10,7,-4,-7,8,-3,-4,-6,-5,-2,2,7,-10,9,7,-3,10,6,-10,3,6,7,-5,6,-8,4,2,-5,10,-6,-10,8,2,5,7,-10,-6,-5,-1,-2,1,7,9,-6,6,8,4,7,7,7,-10,9,5,-8,4,5,5,-9,-4,3,-8,7,6,5,3,-1,1,10,1,2,7,-1,9,-9,4,4,-5,-3,2,8,1,2,-7,-10,10,4,-9,-4,-4,1,4,-1,6,-2,5,6,9,-10,10,-7,-1,-10,7,-9],[6,2,-7,9,-8,-10,2,10,3,10,-7,-6,9,9,9,-6,9,-4,-10,10,5,2,7,9,-10,-3,-5,7,4,-9,-5,-7,2,3,-4,3,-2,-7,6,10,4,-5,2,-4,-2,-1,-7,-3,2,4,-8,5,1,-10,-7,-3,4,3,-3,-6,9,2,-8,6,1,-5,-4,-3,-2,2,-3,-2,4,-7,-2,2,2,7,8,-1,-1,2,-7,-2,7,-10,-10,1,10,3,-3,-3,-10,7,2,-1,-4,-2,-7,4,2,-6,8,8,-5,2,-7,-5,3,-7,7,2,8,-6,10,-8,-4,5,-2,-2,6,-7,6,2,-3,8,6,3,6,10,7,-8,-4,5,-10,7,8,10,5,7,10,7,-5,-1,-2,-7,-9,-2,-2,1,1,-7,-1,4,9,-3,7,7,4,5,1,7,-8,4,-3,1,2,-4,7,10,-1,8,-7,-4,-5,7,10,5,-10,-8,-4,10,1,1,-3,-5,-4,-6,8,-1,8,6,-1,-6,9,-5,-4,-9,10,2,-8,10,10,4,6,10,5,-2,6,-7,-3,-6,-9,2,4,3,-3,-6,8,10,5,-10,7,-7,9,7,-8,8,9,-9,8,-5,-4,5],[-10,8,6,-6,-9,3,8,-9,-5,6,-9,-7,6,7,2,3,-6,9,-10,-2,-7,6,-6,-2,2,-5,2,5,5,-9,3,-8,5,-10,2,2,8,7,-3,-7,8,3,5,9,9,6,1,10,3,9,-1,-7,10,-4,-4,5,2,-5,5,6,3,5,-8,-8,-4,-8,-9,-3,10,10,-8,-9,3,7,7,4,-7,-4,4,8,8,-5,3,-5,-5,9,4,-4,-2,-4,6,9,-7,-10,4,10,-6,-10,-3,3,4,3,-10,4,10,10,-6,-1,1,-7,-1,-6,4,-7,-1,-6,2,2,8,5,3,-6,-4,5,10,10,-9,-10,4,-9,-10,1,-6,-6,-6,4,6,-10,7,-8,5,10,-6,-6,-2,5,-10,5,-9,2,-4,7,-4,-2,4,10,8,5,2,2,6,5,-6,-2,3,-2,-10,-9,-6,7,-9,-9,-9,-10,-6,5,2,8,2,2,-5,4,-3,-10,-4,-1,6,-9,-6,5,3,-4,2,4,-3,1,1,3,-8,7,10,6,-7,2,-4,-7,-9,-4,4,-8,4,-5,5,-1,1,-9,-5,6,8,7,-6,-10,5,7,2,6,-5,1,9,6,-1,8,8,7],[-3,-9,-1,4,-5,-5,6,-10,-2,-2,-6,-8,3,-2,3,6,-6,-5,-8,-2,9,9,-1,-8,-4,4,9,5,-2,-1,-8,1,6,10,-4,-8,-2,-10,-7,-7,-7,1,5,-7,4,-1,7,-6,-5,-8,1,-4,2,-7,10,-10,-5,2,6,6,-7,4,-7,8,7,3,-1,-2,-10,-2,10,-7,4,4,1,1,7,4,6,-9,10,-2,8,-4,10,9,1,-5,-7,4,-1,6,2,3,1,-2,4,2,7,-2,-5,9,5,10,4,-10,10,-2,-5,10,-9,-9,-6,8,-8,-10,-9,8,4,-8,1,-3,3,3,2,-3,8,7,2,7,4,-4,6,-9,-9,9,2,-1,7,2,-1,-4,7,-1,7,-1,-5,3,7,4,-8,4,-4,6,2,5,-3,10,-2,-2,-1,9,-8,-9,-4,-8,7,2,-8,-7,6,-4,2,-10,-5,1,-5,-3,-3,-5,7,-1,5,10,-2,6,8,9,-3,2,1,-5,-6,-9,-1,7,-10,-4,2,10,10,3,7,-10,1,10,7,-10,6,-3,-8,6,-9,-2,-6,-8,-10,6,3,10,8,-7,7,-10,-1,-9,3,4,6,6,10,-10,-5,2]], dtype = "uint8")#candidate|953|(5, 234)|const|uint8
call_952 = relay.TupleGetItem(func_498_call(relay.reshape(const_953.astype('uint8'), [6, 13, 15])), 1)
call_954 = relay.TupleGetItem(func_501_call(relay.reshape(const_953.astype('uint8'), [6, 13, 15])), 1)
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
call_955 = func_128_call(relay.reshape(call_952.astype('int32'), [2, 15, 3]), relay.reshape(call_952.astype('int32'), [2, 15, 3]), )
call_956 = func_128_call(relay.reshape(call_952.astype('int32'), [2, 15, 3]), relay.reshape(call_952.astype('int32'), [2, 15, 3]), )
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
call_961 = func_128_call(relay.reshape(call_955.astype('int32'), [2, 15, 3]), relay.reshape(call_952.astype('int32'), [2, 15, 3]), )
call_962 = func_128_call(relay.reshape(call_955.astype('int32'), [2, 15, 3]), relay.reshape(call_952.astype('int32'), [2, 15, 3]), )
func_498_call = mod.get_global_var('func_498')
func_501_call = mutated_mod.get_global_var('func_501')
call_973 = relay.TupleGetItem(func_498_call(relay.reshape(const_953.astype('uint8'), [6, 13, 15])), 1)
call_974 = relay.TupleGetItem(func_501_call(relay.reshape(const_953.astype('uint8'), [6, 13, 15])), 1)
output = relay.Tuple([bop_949,call_952,const_953,call_955,call_961,call_973,])
output2 = relay.Tuple([bop_949,call_954,const_953,call_956,call_962,call_974,])
func_991 = relay.Function([var_947,var_948,], output)
mod['func_991'] = func_991
mod = relay.transform.InferType()(mod)
var_992 = relay.var("var_992", dtype = "float32", shape = (6, 2, 1))#candidate|992|(6, 2, 1)|var|float32
var_993 = relay.var("var_993", dtype = "float32", shape = (6, 2, 13))#candidate|993|(6, 2, 13)|var|float32
output = func_991(var_992,var_993,)
func_994 = relay.Function([var_992,var_993,], output)
mutated_mod['func_994'] = func_994
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1285 = relay.var("var_1285", dtype = "float32", shape = (10, 2, 1))#candidate|1285|(10, 2, 1)|var|float32
uop_1286 = relay.erf(var_1285.astype('float32')) # shape=(10, 2, 1)
const_1288 = relay.const([[[6.840294,-7.178746,-9.376651,-1.235585,3.993584,-5.287896,-0.974031,3.752493,-7.348952,-2.769088,-6.357793,3.641654,-7.134928],[-1.574217,9.925798,1.953836,6.332952,-1.950141,-9.436189,-0.618090,8.204267,-0.312636,-3.543292,-1.484085,4.390197,-7.696451]],[[7.265268,-2.428624,4.654793,9.687915,-1.634417,-0.867639,1.773283,-7.880397,4.159219,8.425538,4.707903,3.230450,6.636411],[2.809441,-7.544322,-7.290621,1.972244,1.093031,-9.274389,0.894611,1.826427,-5.938319,-7.067470,-3.617327,6.317214,6.503407]],[[9.209400,-7.113442,-7.066505,-6.362930,-4.073910,-7.526088,3.872735,-2.367676,0.181133,-3.324796,9.409508,5.957929,6.662589],[-2.818960,6.349113,-0.883030,-9.435102,1.504101,-3.317879,9.050969,-6.104601,-3.789750,-2.185567,5.858033,3.039879,-3.188076]],[[-0.343248,-5.463708,-9.972350,5.784620,-5.490367,-8.742179,-6.789328,-4.490931,4.992942,2.841953,3.984371,9.385635,3.026859],[9.188267,3.221776,7.819019,7.555764,6.806826,-5.531015,8.139017,-6.988014,2.448162,8.660699,9.046943,-5.132475,3.239988]],[[2.427111,8.834886,7.295428,1.971841,-3.366490,2.855633,-5.856761,4.892160,5.357504,-3.605742,1.589090,-1.638538,4.568860],[5.954439,4.971895,9.106662,-1.532483,3.864117,-7.523435,-8.037618,0.095332,-5.240160,-3.545049,3.164465,2.214128,-1.253011]],[[8.040108,1.193760,-7.832637,-1.567545,5.201023,-5.948253,-0.288249,-3.065642,-2.139233,-5.950563,-6.240348,-3.909092,-1.487401],[-2.719475,4.165887,-0.612965,9.018327,1.645231,4.807532,4.934065,3.299634,-6.939831,4.938207,-6.392505,3.402257,-4.121588]],[[-1.393399,-2.436527,-0.813135,-4.863363,1.279377,-7.591096,-4.848426,3.681065,-7.544603,4.773697,-4.654903,8.288566,-5.318703],[-8.542359,-2.036007,9.325081,2.258784,-9.759925,-6.745032,6.183750,4.021878,-8.541839,2.221848,5.097920,7.275109,9.687033]],[[-3.007699,6.387972,9.359335,-4.229029,-0.299344,-8.541784,-6.263587,1.182757,8.824278,-6.658020,7.248336,-2.256472,-5.296513],[-1.110593,-8.590414,-9.865074,-8.529864,0.750929,8.403021,-6.306414,9.550149,9.153209,6.741490,-7.648124,8.552042,9.077284]],[[-2.667341,3.837425,-2.293614,-5.618417,3.612343,5.872261,-6.613500,2.950299,8.739253,-3.039112,-4.109637,-4.923499,-4.224677],[-7.715311,2.677068,-5.744423,-8.628257,5.378623,6.820299,0.695043,-1.218367,0.788566,-8.616953,-7.095607,-9.265712,-1.990841]],[[-5.396728,-1.803917,-7.503431,-0.142352,-6.489375,4.275699,-7.630701,0.350585,-5.264784,-6.572178,-1.116623,1.607722,0.612463],[-3.093294,-0.044186,-6.987273,8.174411,-8.536724,-8.117804,2.044688,2.439393,0.579967,3.457590,-1.137178,2.980237,-9.484191]]], dtype = "float32")#candidate|1288|(10, 2, 13)|const|float32
bop_1289 = relay.mod(uop_1286.astype('float64'), const_1288.astype('float64')) # shape=(10, 2, 13)
bop_1293 = relay.maximum(uop_1286.astype('float64'), bop_1289.astype('float64')) # shape=(10, 2, 13)
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
var_1307 = relay.var("var_1307", dtype = "int32", shape = (90, 1))#candidate|1307|(90, 1)|var|int32
call_1306 = func_128_call(relay.reshape(var_1307.astype('int32'), [2, 15, 3]), relay.reshape(var_1307.astype('int32'), [2, 15, 3]), )
call_1308 = func_128_call(relay.reshape(var_1307.astype('int32'), [2, 15, 3]), relay.reshape(var_1307.astype('int32'), [2, 15, 3]), )
output = relay.Tuple([bop_1293,call_1306,var_1307,])
output2 = relay.Tuple([bop_1293,call_1308,var_1307,])
func_1311 = relay.Function([var_1285,var_1307,], output)
mod['func_1311'] = func_1311
mod = relay.transform.InferType()(mod)
var_1312 = relay.var("var_1312", dtype = "float32", shape = (10, 2, 1))#candidate|1312|(10, 2, 1)|var|float32
var_1313 = relay.var("var_1313", dtype = "int32", shape = (90, 1))#candidate|1313|(90, 1)|var|int32
output = func_1311(var_1312,var_1313,)
func_1314 = relay.Function([var_1312,var_1313,], output)
mutated_mod['func_1314'] = func_1314
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1343 = relay.var("var_1343", dtype = "int32", shape = ())#candidate|1343|()|var|int32
var_1344 = relay.var("var_1344", dtype = "int32", shape = (1, 10, 3))#candidate|1344|(1, 10, 3)|var|int32
bop_1345 = relay.less(var_1343.astype('bool'), var_1344.astype('bool')) # shape=(1, 10, 3)
output = bop_1345
output2 = bop_1345
func_1360 = relay.Function([var_1343,var_1344,], output)
mod['func_1360'] = func_1360
mod = relay.transform.InferType()(mod)
var_1361 = relay.var("var_1361", dtype = "int32", shape = ())#candidate|1361|()|var|int32
var_1362 = relay.var("var_1362", dtype = "int32", shape = (1, 10, 3))#candidate|1362|(1, 10, 3)|var|int32
output = func_1360(var_1361,var_1362,)
func_1363 = relay.Function([var_1361,var_1362,], output)
mutated_mod['func_1363'] = func_1363
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1524 = relay.var("var_1524", dtype = "float64", shape = (14, 3, 14))#candidate|1524|(14, 3, 14)|var|float64
uop_1525 = relay.log10(var_1524.astype('float64')) # shape=(14, 3, 14)
output = uop_1525
output2 = uop_1525
func_1527 = relay.Function([var_1524,], output)
mod['func_1527'] = func_1527
mod = relay.transform.InferType()(mod)
mutated_mod['func_1527'] = func_1527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1528 = relay.var("var_1528", dtype = "float64", shape = (14, 3, 14))#candidate|1528|(14, 3, 14)|var|float64
func_1527_call = mutated_mod.get_global_var('func_1527')
call_1529 = func_1527_call(var_1528)
output = call_1529
func_1530 = relay.Function([var_1528], output)
mutated_mod['func_1530'] = func_1530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1596 = relay.var("var_1596", dtype = "bool", shape = (11, 6, 16))#candidate|1596|(11, 6, 16)|var|bool
var_1597 = relay.var("var_1597", dtype = "bool", shape = (11, 6, 16))#candidate|1597|(11, 6, 16)|var|bool
bop_1598 = relay.logical_and(var_1596.astype('bool'), relay.reshape(var_1597.astype('bool'), relay.shape_of(var_1596))) # shape=(11, 6, 16)
uop_1607 = relay.acosh(var_1596.astype('float64')) # shape=(11, 6, 16)
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
const_1619 = relay.const([-5,-1,-6,-1,3,4,-10,6,10,-6,2,8,-7,7,-6,4,9,8,-10,-6,6,-10,-4,4,-2,10,-6,-8,-3,-8,-3,-10,-8,8,7,10,1,-10,6,-8,-4,4,7,6,-7,10,-7,-4,1,4,5,1,-5,2,-3,-10,1,1,-6,-9,-9,4,-1,2,10,10,-9,-1,10,-8,6,-3,1,-4,-9,9,3,-6,2,8,4,-7,-9,-9,-4,5,4,6,10,-2], dtype = "int32")#candidate|1619|(90,)|const|int32
call_1618 = func_128_call(relay.reshape(const_1619.astype('int32'), [2, 15, 3]), relay.reshape(const_1619.astype('int32'), [2, 15, 3]), )
call_1620 = func_128_call(relay.reshape(const_1619.astype('int32'), [2, 15, 3]), relay.reshape(const_1619.astype('int32'), [2, 15, 3]), )
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
call_1625 = func_128_call(relay.reshape(call_1618.astype('int32'), [2, 15, 3]), relay.reshape(const_1619.astype('int32'), [2, 15, 3]), )
call_1626 = func_128_call(relay.reshape(call_1618.astype('int32'), [2, 15, 3]), relay.reshape(const_1619.astype('int32'), [2, 15, 3]), )
uop_1629 = relay.log10(uop_1607.astype('float32')) # shape=(11, 6, 16)
output = relay.Tuple([bop_1598,call_1618,const_1619,call_1625,uop_1629,])
output2 = relay.Tuple([bop_1598,call_1620,const_1619,call_1626,uop_1629,])
func_1637 = relay.Function([var_1596,var_1597,], output)
mod['func_1637'] = func_1637
mod = relay.transform.InferType()(mod)
var_1638 = relay.var("var_1638", dtype = "bool", shape = (11, 6, 16))#candidate|1638|(11, 6, 16)|var|bool
var_1639 = relay.var("var_1639", dtype = "bool", shape = (11, 6, 16))#candidate|1639|(11, 6, 16)|var|bool
output = func_1637(var_1638,var_1639,)
func_1640 = relay.Function([var_1638,var_1639,], output)
mutated_mod['func_1640'] = func_1640
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1672 = relay.var("var_1672", dtype = "int32", shape = ())#candidate|1672|()|var|int32
const_1673 = relay.const([[[-4,6,4,-3,6,-7,-8,2,-5,-9,-9,-5,-6],[-2,-5,10,5,9,-9,-10,-8,-6,2,-2,-4,-8],[-6,3,-7,-1,-10,-4,-5,4,7,1,-3,-2,6],[1,-7,-4,-9,-4,-4,1,-4,-10,-7,-4,-10,-10],[1,-7,-7,10,7,-8,-1,-5,7,-10,8,-3,6],[-1,-2,1,-2,4,-7,5,8,-2,-8,-5,-10,8],[-5,-7,10,-1,-7,-8,3,2,6,-5,3,-5,-2],[-5,-5,4,-6,3,9,8,8,-6,-10,2,6,-2],[3,-9,10,-1,1,-5,6,-4,-3,2,-10,2,-9],[-8,10,-5,9,-1,-1,4,-8,10,-6,-1,-9,-8],[-3,1,-5,-8,-10,9,8,8,2,1,10,4,-6],[-3,-9,-3,3,4,-2,-4,-5,2,5,-5,4,9]]], dtype = "int32")#candidate|1673|(1, 12, 13)|const|int32
bop_1674 = relay.minimum(var_1672.astype('int32'), const_1673.astype('int32')) # shape=(1, 12, 13)
func_991_call = mod.get_global_var('func_991')
func_994_call = mutated_mod.get_global_var('func_994')
var_1697 = relay.var("var_1697", dtype = "float32", shape = (12,))#candidate|1697|(12,)|var|float32
call_1696 = relay.TupleGetItem(func_991_call(relay.reshape(var_1697.astype('float32'), [6, 2, 1]), relay.reshape(bop_1674.astype('float32'), [6, 2, 13]), ), 3)
call_1698 = relay.TupleGetItem(func_994_call(relay.reshape(var_1697.astype('float32'), [6, 2, 1]), relay.reshape(bop_1674.astype('float32'), [6, 2, 13]), ), 3)
output = relay.Tuple([bop_1674,call_1696,var_1697,])
output2 = relay.Tuple([bop_1674,call_1698,var_1697,])
func_1712 = relay.Function([var_1672,var_1697,], output)
mod['func_1712'] = func_1712
mod = relay.transform.InferType()(mod)
var_1713 = relay.var("var_1713", dtype = "int32", shape = ())#candidate|1713|()|var|int32
var_1714 = relay.var("var_1714", dtype = "float32", shape = (12,))#candidate|1714|(12,)|var|float32
output = func_1712(var_1713,var_1714,)
func_1715 = relay.Function([var_1713,var_1714,], output)
mutated_mod['func_1715'] = func_1715
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2160 = relay.const(3.244230, dtype = "float32")#candidate|2160|()|const|float32
var_2161 = relay.var("var_2161", dtype = "float32", shape = (3, 5, 1))#candidate|2161|(3, 5, 1)|var|float32
bop_2162 = relay.greater_equal(const_2160.astype('bool'), var_2161.astype('bool')) # shape=(3, 5, 1)
output = bop_2162
output2 = bop_2162
func_2165 = relay.Function([var_2161,], output)
mod['func_2165'] = func_2165
mod = relay.transform.InferType()(mod)
var_2166 = relay.var("var_2166", dtype = "float32", shape = (3, 5, 1))#candidate|2166|(3, 5, 1)|var|float32
output = func_2165(var_2166)
func_2167 = relay.Function([var_2166], output)
mutated_mod['func_2167'] = func_2167
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2236 = relay.var("var_2236", dtype = "uint32", shape = (11, 12, 4))#candidate|2236|(11, 12, 4)|var|uint32
var_2237 = relay.var("var_2237", dtype = "uint32", shape = (11, 12, 4))#candidate|2237|(11, 12, 4)|var|uint32
bop_2238 = relay.less_equal(var_2236.astype('bool'), relay.reshape(var_2237.astype('bool'), relay.shape_of(var_2236))) # shape=(11, 12, 4)
func_1360_call = mod.get_global_var('func_1360')
func_1363_call = mutated_mod.get_global_var('func_1363')
const_2242 = relay.const(-4, dtype = "int32")#candidate|2242|()|const|int32
const_2243 = relay.const([-6,-5,7,5,1,5,-3,-6,8,8,-9,-4,7,-6,-4,-8,-1,9,1,1,6,-3,10,7,-5,2,6,-2,9,3], dtype = "int32")#candidate|2243|(30,)|const|int32
call_2241 = func_1360_call(relay.reshape(const_2242.astype('int32'), []), relay.reshape(const_2243.astype('int32'), [1, 10, 3]), )
call_2244 = func_1360_call(relay.reshape(const_2242.astype('int32'), []), relay.reshape(const_2243.astype('int32'), [1, 10, 3]), )
bop_2252 = relay.equal(var_2237.astype('bool'), const_2242.astype('bool')) # shape=(11, 12, 4)
uop_2277 = relay.asinh(bop_2252.astype('float32')) # shape=(11, 12, 4)
output = relay.Tuple([bop_2238,call_2241,const_2243,uop_2277,])
output2 = relay.Tuple([bop_2238,call_2244,const_2243,uop_2277,])
func_2287 = relay.Function([var_2236,var_2237,], output)
mod['func_2287'] = func_2287
mod = relay.transform.InferType()(mod)
var_2288 = relay.var("var_2288", dtype = "uint32", shape = (11, 12, 4))#candidate|2288|(11, 12, 4)|var|uint32
var_2289 = relay.var("var_2289", dtype = "uint32", shape = (11, 12, 4))#candidate|2289|(11, 12, 4)|var|uint32
output = func_2287(var_2288,var_2289,)
func_2290 = relay.Function([var_2288,var_2289,], output)
mutated_mod['func_2290'] = func_2290
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2394 = relay.const([[[1,-2,10,8,1,-10],[6,3,8,-3,-2,4],[1,1,-9,1,3,-9],[-7,6,4,7,1,10],[-10,8,10,-7,3,-10],[5,6,-7,10,4,3],[1,-10,2,4,4,3],[5,-6,-10,-5,-8,-2],[6,10,-7,9,-5,-2],[8,-6,-1,-6,-8,9],[9,-2,4,5,-5,1]],[[-7,2,9,6,4,-10],[10,-1,8,-8,-3,5],[6,7,-4,3,-1,1],[1,-7,-1,9,-3,-2],[10,8,-2,-1,3,-10],[-8,-8,10,-1,1,7],[5,5,-6,-8,1,-2],[-9,9,-10,-10,-4,9],[2,-4,-10,-6,6,-4],[10,-1,-8,-4,-5,-10],[4,5,-2,1,-6,6]],[[-7,-10,4,5,6,5],[-8,-10,3,-8,-3,4],[-9,9,1,1,8,1],[7,-7,4,6,2,5],[-7,-4,-5,-8,-3,-2],[-4,2,-6,5,-1,-6],[-6,-6,-10,4,3,-2],[6,5,-6,-6,1,2],[3,3,-10,8,5,4],[5,5,-8,8,-6,5],[-1,-2,-1,2,-2,7]],[[-5,-7,8,-6,-9,-3],[-9,-3,6,-8,-9,1],[-7,-5,9,-2,-6,5],[-10,1,3,8,-6,10],[9,3,8,-1,9,3],[-7,-4,-4,10,-1,5],[4,-7,-4,-4,-5,-4],[-1,10,-8,-9,10,9],[2,7,-10,-9,-8,7],[-3,7,-10,-3,-6,2],[-7,-1,4,-10,9,2]],[[-2,6,-7,-3,7,-10],[-3,-9,-7,-2,-4,1],[5,6,1,-5,-7,4],[-5,-6,-7,7,-1,-6],[9,-5,5,1,-9,3],[-3,4,9,-5,5,5],[10,-9,-10,3,6,-2],[-6,-10,10,-7,-2,-4],[-1,7,10,7,6,3],[2,7,4,9,-4,6],[-2,4,6,-9,7,-2]],[[-8,9,2,3,-9,-3],[2,4,-1,-8,1,-1],[2,-3,-5,-7,1,-8],[1,-8,4,5,5,1],[-10,-1,5,-10,-1,7],[6,-9,-2,-2,10,5],[-3,-9,-10,4,-3,10],[8,-4,-3,-7,5,-7],[-6,-1,-1,10,7,-4],[-4,-8,5,5,-10,-4],[-2,-1,8,-5,9,1]],[[-4,-5,2,9,-8,-3],[7,-8,-8,9,5,6],[-9,8,-1,-9,-1,6],[-4,7,4,-6,-7,9],[7,5,7,5,-4,-4],[-3,-10,7,-8,-4,4],[-7,10,-5,9,-6,-3],[-6,9,-3,-7,-5,-3],[-4,5,7,8,10,-6],[-7,-8,-9,-4,-9,-7],[5,1,10,4,4,-1]],[[-1,-5,-7,7,-7,-4],[3,-3,2,-7,3,-9],[-1,-6,2,-7,6,-3],[4,8,-4,10,-2,-2],[-5,3,6,-9,-5,-3],[4,-2,-4,5,7,-1],[-6,10,6,-4,2,8],[-9,2,-4,5,-5,-10],[3,6,1,-3,-10,8],[-9,-6,-10,-7,-3,-5],[6,-5,-6,-1,-4,-1]],[[6,-3,8,-2,-4,8],[-5,4,-5,-5,10,1],[6,-5,9,-5,-9,-1],[2,6,4,-9,-8,-6],[-4,2,-10,-10,-5,9],[8,-8,4,5,-3,-9],[4,7,-3,-3,-6,10],[9,6,-4,9,7,-10],[9,7,6,-10,-6,-2],[-3,-9,-1,-7,-1,-8],[6,-7,-5,5,2,-7]],[[-10,7,-5,6,-4,-5],[5,7,4,9,3,4],[2,-3,3,-3,6,-8],[8,6,-10,9,4,-1],[5,8,-7,7,2,-6],[-9,-8,8,5,2,2],[-2,-7,-10,5,-10,1],[-7,-9,-8,6,5,-4],[9,-10,9,-5,4,-9],[2,-8,-7,2,-9,3],[-7,9,-2,-4,10,-4]],[[-8,2,-10,-6,5,7],[-5,5,9,5,10,5],[-5,-3,-2,4,5,-2],[4,-9,2,-10,4,-2],[7,6,-9,9,7,9],[-10,-9,-6,4,-9,-1],[-9,-7,-10,4,4,7],[1,7,10,9,-6,7],[-1,6,-5,10,-1,7],[-4,1,2,-1,-3,-1],[4,-3,10,6,2,-1]],[[8,1,6,1,10,8],[-9,7,9,5,9,6],[1,-9,2,1,1,1],[1,-9,-5,5,8,-6],[-9,10,10,-7,8,3],[8,-1,-6,-10,8,10],[-8,7,-6,-5,-5,-4],[3,-7,9,-10,-4,8],[5,8,7,7,2,5],[9,6,-7,1,4,-10],[8,10,2,3,-5,-9]],[[9,-10,-9,1,-5,4],[-9,-3,-4,6,4,7],[7,1,3,6,7,-4],[-3,8,4,-1,8,-6],[8,8,1,7,-7,9],[2,3,3,8,4,5],[10,1,-3,-2,-2,-2],[10,-2,-10,9,8,1],[-1,9,-7,-5,2,4],[-4,6,-1,-2,2,7],[5,-5,-10,-6,7,8]],[[2,10,-9,1,5,3],[8,4,-7,1,7,-7],[-2,7,10,7,9,6],[-4,-3,-6,2,2,-5],[8,-5,4,1,-4,-7],[-6,-6,2,4,1,-6],[6,3,5,-8,-6,10],[-4,-5,-1,-5,-9,-5],[5,8,9,-4,-3,4],[7,-10,7,-10,-1,1],[9,3,7,8,7,9]],[[-9,2,2,-9,10,-9],[-1,7,-3,-6,-2,-10],[-6,2,-4,1,4,5],[-1,-2,-6,-5,-1,1],[-9,-8,-7,-2,5,-10],[5,-2,5,4,6,7],[8,-10,-6,-4,-9,10],[1,1,-5,6,-2,-8],[8,5,7,-7,-5,5],[8,-8,4,-3,9,-2],[2,-4,-8,1,4,1]]], dtype = "int8")#candidate|2394|(15, 11, 6)|const|int8
const_2395 = relay.const([[[-7,4,-3,2,5,-8],[9,10,6,-5,-9,-4],[-2,5,1,9,-3,1],[-9,-9,-1,7,-10,2],[-1,2,9,-2,-5,2],[3,5,-4,1,9,10],[-6,10,3,3,-2,-5],[-9,3,6,-3,7,-6],[-6,6,8,5,-4,1],[8,1,-6,-10,5,-2],[-9,1,-3,-8,-5,-4]],[[2,-8,-6,-4,-2,-6],[-3,-7,2,-1,-4,-6],[1,-6,10,-1,1,9],[-10,-6,9,-3,10,3],[9,4,8,10,6,6],[-8,-10,-6,-8,3,-9],[6,5,1,-10,1,2],[6,7,-10,7,9,4],[-8,2,-6,4,-2,-8],[6,-3,-3,-4,-9,-10],[3,-4,7,-10,2,-6]],[[2,10,10,6,9,-3],[-4,-1,8,-1,-9,5],[-5,-10,-6,7,10,-1],[7,-6,-9,-9,4,8],[-9,4,6,-5,4,-9],[-6,10,4,-6,-1,9],[9,-2,6,-8,-9,-5],[2,5,5,-8,-2,7],[-10,-9,3,-10,4,9],[4,-6,-10,7,1,9],[9,9,8,9,8,10]],[[6,8,-3,-1,-4,9],[8,-5,-1,-6,-6,2],[-2,-3,-9,-2,2,-4],[-6,-2,-3,-4,9,1],[6,10,2,-5,3,5],[-2,6,6,10,6,-2],[-5,10,-6,5,8,-3],[9,5,7,-5,-6,4],[2,5,6,-9,-4,6],[-9,1,8,8,-3,1],[-4,8,9,3,5,-3]],[[5,-5,-10,10,-4,7],[-4,-1,-7,-6,1,2],[-7,-3,-2,5,-8,-8],[-1,-8,-9,7,9,10],[-10,-8,10,1,2,10],[-2,-3,5,-9,-10,-1],[3,2,-8,9,-9,-9],[4,6,7,1,-1,10],[-6,2,7,6,-3,-1],[9,1,6,6,-3,7],[8,-7,-4,7,-7,7]],[[4,5,2,-10,-7,-8],[4,-2,-8,-5,1,-9],[1,7,7,-2,-9,-10],[-5,3,-3,5,-7,-2],[-8,-3,-1,5,8,-7],[-8,-4,8,-10,-6,2],[-4,-7,-4,5,-8,-2],[-9,-8,-9,-2,6,3],[-1,4,4,7,5,-8],[-2,10,1,6,8,-9],[-1,-3,-8,-10,9,-6]],[[-1,2,6,-4,3,8],[-7,6,-10,-2,5,-7],[-2,-9,2,6,8,-9],[8,-3,-7,-6,5,10],[4,-8,5,-1,-4,-10],[8,10,-3,-10,-10,3],[4,-2,1,4,-3,-4],[8,7,-8,8,2,1],[5,-10,6,4,5,9],[-7,-9,7,-1,1,-9],[-3,-6,-5,2,-10,-6]],[[-6,-6,-8,4,10,-8],[-1,4,-4,-2,1,4],[4,-5,8,1,-4,4],[-2,9,-6,-10,3,10],[8,6,1,-3,-6,3],[4,8,1,-9,-4,6],[5,-8,2,8,1,7],[-4,9,1,-5,-6,-2],[-7,-3,-1,-1,-6,5],[-7,6,-8,2,-3,3],[-4,10,1,8,-5,9]],[[1,4,-8,-5,-3,5],[-6,-3,-9,-5,-3,3],[-9,2,-4,-3,10,2],[6,7,10,3,8,-7],[4,-7,8,-1,-1,-4],[5,-9,5,-6,-1,-2],[-2,7,3,-6,5,-4],[-3,2,9,10,3,10],[3,9,-7,-6,-8,-1],[-6,-5,-10,6,3,9],[5,-7,-3,6,-3,1]],[[-8,10,-10,6,-8,9],[-10,-3,-4,-5,6,-9],[1,4,-2,5,-9,-7],[-8,5,4,5,-8,6],[-3,-2,5,7,-7,-9],[5,1,8,3,1,-3],[-3,-6,9,4,5,2],[-5,5,9,1,7,-7],[9,3,1,4,6,-6],[2,-8,6,-6,-10,-5],[4,-4,9,7,5,-8]],[[8,10,-2,1,-8,2],[1,-9,10,4,3,4],[-1,-9,-3,-3,-1,-4],[-1,10,6,-5,1,-9],[-9,4,1,3,-10,-8],[-1,5,4,-6,6,6],[9,8,7,-10,10,-10],[3,3,-8,-10,2,1],[-7,-10,-5,7,-8,-4],[2,-3,10,-3,7,-10],[-9,-3,6,-6,3,9]],[[4,1,-9,-9,9,-3],[-5,3,4,-8,4,3],[-5,4,-5,-7,-7,1],[3,10,3,-2,2,2],[-9,-1,2,-2,3,5],[8,-8,-10,4,-10,5],[8,4,3,5,6,4],[10,-5,1,-2,3,6],[1,-7,2,4,9,9],[-4,3,-2,8,-10,-6],[4,-10,8,-10,-5,9]],[[9,7,-3,-2,-1,-7],[-10,7,-7,-3,-1,-7],[10,-9,6,-2,3,-5],[-4,-3,9,-9,4,-3],[7,3,-10,8,-2,4],[-6,3,4,6,-4,-4],[-7,-6,-9,4,-4,5],[-9,-5,-3,-9,7,-8],[1,-10,1,9,-7,10],[5,-3,3,4,-2,-3],[10,-3,5,8,3,2]],[[-4,-3,10,-8,-7,4],[8,2,-9,-4,-8,-7],[-8,2,5,-5,-6,9],[-2,-9,-7,-9,-2,-6],[7,-1,-8,-9,-5,6],[-4,8,-1,-6,-3,2],[-9,-6,9,2,-1,10],[-1,-4,1,-6,-4,4],[1,-6,6,-6,-8,-8],[4,4,4,5,-4,-4],[2,9,4,1,3,2]],[[7,8,2,-2,-5,4],[-2,-5,-9,-1,-8,-6],[4,-8,5,10,-7,7],[2,6,8,7,8,-8],[2,7,-10,2,10,-2],[-7,-9,9,-4,7,-8],[-9,-7,-8,3,4,10],[2,-7,10,-9,10,-3],[-4,-1,6,-6,-6,-1],[7,2,3,5,-4,10],[-2,10,7,-4,-2,-3]]], dtype = "int8")#candidate|2395|(15, 11, 6)|const|int8
bop_2396 = relay.bitwise_and(const_2394.astype('int8'), relay.reshape(const_2395.astype('int8'), relay.shape_of(const_2394))) # shape=(15, 11, 6)
output = bop_2396
output2 = bop_2396
func_2401 = relay.Function([], output)
mod['func_2401'] = func_2401
mod = relay.transform.InferType()(mod)
mutated_mod['func_2401'] = func_2401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2401_call = mutated_mod.get_global_var('func_2401')
call_2402 = func_2401_call()
output = call_2402
func_2403 = relay.Function([], output)
mutated_mod['func_2403'] = func_2403
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2404 = relay.var("var_2404", dtype = "float64", shape = (7, 8, 8))#candidate|2404|(7, 8, 8)|var|float64
uop_2405 = relay.sqrt(var_2404.astype('float64')) # shape=(7, 8, 8)
output = relay.Tuple([uop_2405,])
output2 = relay.Tuple([uop_2405,])
func_2409 = relay.Function([var_2404,], output)
mod['func_2409'] = func_2409
mod = relay.transform.InferType()(mod)
var_2410 = relay.var("var_2410", dtype = "float64", shape = (7, 8, 8))#candidate|2410|(7, 8, 8)|var|float64
output = func_2409(var_2410)
func_2411 = relay.Function([var_2410], output)
mutated_mod['func_2411'] = func_2411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2401_call = mod.get_global_var('func_2401')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_2436 = func_2401_call()
call_2437 = func_2401_call()
output = relay.Tuple([call_2436,])
output2 = relay.Tuple([call_2437,])
func_2460 = relay.Function([], output)
mod['func_2460'] = func_2460
mod = relay.transform.InferType()(mod)
mutated_mod['func_2460'] = func_2460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2460_call = mutated_mod.get_global_var('func_2460')
call_2461 = func_2460_call()
output = call_2461
func_2462 = relay.Function([], output)
mutated_mod['func_2462'] = func_2462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_2463 = relay.TupleGetItem(func_2460_call(), 0)
call_2464 = relay.TupleGetItem(func_2462_call(), 0)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
const_2470 = relay.const(-9, dtype = "int32")#candidate|2470|()|const|int32
var_2471 = relay.var("var_2471", dtype = "float32", shape = (12,))#candidate|2471|(12,)|var|float32
call_2469 = relay.TupleGetItem(func_1712_call(relay.reshape(const_2470.astype('int32'), []), relay.reshape(var_2471.astype('float32'), [12,]), ), 0)
call_2472 = relay.TupleGetItem(func_1715_call(relay.reshape(const_2470.astype('int32'), []), relay.reshape(var_2471.astype('float32'), [12,]), ), 0)
output = relay.Tuple([call_2463,call_2469,const_2470,var_2471,])
output2 = relay.Tuple([call_2464,call_2472,const_2470,var_2471,])
func_2482 = relay.Function([var_2471,], output)
mod['func_2482'] = func_2482
mod = relay.transform.InferType()(mod)
var_2483 = relay.var("var_2483", dtype = "float32", shape = (12,))#candidate|2483|(12,)|var|float32
output = func_2482(var_2483)
func_2484 = relay.Function([var_2483], output)
mutated_mod['func_2484'] = func_2484
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2502 = relay.var("var_2502", dtype = "int32", shape = (10, 4, 3))#candidate|2502|(10, 4, 3)|var|int32
var_2503 = relay.var("var_2503", dtype = "int32", shape = (10, 4, 3))#candidate|2503|(10, 4, 3)|var|int32
bop_2504 = relay.bitwise_and(var_2502.astype('int32'), relay.reshape(var_2503.astype('int32'), relay.shape_of(var_2502))) # shape=(10, 4, 3)
bop_2507 = relay.less_equal(var_2502.astype('bool'), relay.reshape(var_2503.astype('bool'), relay.shape_of(var_2502))) # shape=(10, 4, 3)
uop_2519 = relay.cosh(var_2502.astype('float32')) # shape=(10, 4, 3)
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
var_2526 = relay.var("var_2526", dtype = "int32", shape = (90,))#candidate|2526|(90,)|var|int32
call_2525 = func_128_call(relay.reshape(var_2526.astype('int32'), [2, 15, 3]), relay.reshape(var_2526.astype('int32'), [2, 15, 3]), )
call_2527 = func_128_call(relay.reshape(var_2526.astype('int32'), [2, 15, 3]), relay.reshape(var_2526.astype('int32'), [2, 15, 3]), )
var_2529 = relay.var("var_2529", dtype = "float32", shape = (10, 4, 3))#candidate|2529|(10, 4, 3)|var|float32
bop_2530 = relay.subtract(uop_2519.astype('float32'), relay.reshape(var_2529.astype('float32'), relay.shape_of(uop_2519))) # shape=(10, 4, 3)
bop_2535 = relay.minimum(uop_2519.astype('uint8'), relay.reshape(bop_2507.astype('uint8'), relay.shape_of(uop_2519))) # shape=(10, 4, 3)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
const_2548 = relay.const(8, dtype = "int32")#candidate|2548|()|const|int32
const_2549 = relay.const([1.397938,-3.001217,3.210640,-4.516934,-9.625300,1.017548,-8.392452,6.748757,-4.785302,1.672971,5.508598,-7.696571], dtype = "float32")#candidate|2549|(12,)|const|float32
call_2547 = relay.TupleGetItem(func_1712_call(relay.reshape(const_2548.astype('int32'), []), relay.reshape(const_2549.astype('float32'), [12,]), ), 1)
call_2550 = relay.TupleGetItem(func_1715_call(relay.reshape(const_2548.astype('int32'), []), relay.reshape(const_2549.astype('float32'), [12,]), ), 1)
output = relay.Tuple([bop_2504,call_2525,var_2526,bop_2530,bop_2535,call_2547,const_2548,const_2549,])
output2 = relay.Tuple([bop_2504,call_2527,var_2526,bop_2530,bop_2535,call_2550,const_2548,const_2549,])
func_2571 = relay.Function([var_2502,var_2503,var_2526,var_2529,], output)
mod['func_2571'] = func_2571
mod = relay.transform.InferType()(mod)
var_2572 = relay.var("var_2572", dtype = "int32", shape = (10, 4, 3))#candidate|2572|(10, 4, 3)|var|int32
var_2573 = relay.var("var_2573", dtype = "int32", shape = (10, 4, 3))#candidate|2573|(10, 4, 3)|var|int32
var_2574 = relay.var("var_2574", dtype = "int32", shape = (90,))#candidate|2574|(90,)|var|int32
var_2575 = relay.var("var_2575", dtype = "float32", shape = (10, 4, 3))#candidate|2575|(10, 4, 3)|var|float32
output = func_2571(var_2572,var_2573,var_2574,var_2575,)
func_2576 = relay.Function([var_2572,var_2573,var_2574,var_2575,], output)
mutated_mod['func_2576'] = func_2576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2401_call = mod.get_global_var('func_2401')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_2626 = func_2401_call()
call_2627 = func_2401_call()
output = call_2626
output2 = call_2627
func_2632 = relay.Function([], output)
mod['func_2632'] = func_2632
mod = relay.transform.InferType()(mod)
output = func_2632()
func_2633 = relay.Function([], output)
mutated_mod['func_2633'] = func_2633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_2638 = relay.TupleGetItem(func_2460_call(), 0)
call_2639 = relay.TupleGetItem(func_2462_call(), 0)
output = call_2638
output2 = call_2639
func_2645 = relay.Function([], output)
mod['func_2645'] = func_2645
mod = relay.transform.InferType()(mod)
output = func_2645()
func_2646 = relay.Function([], output)
mutated_mod['func_2646'] = func_2646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2401_call = mod.get_global_var('func_2401')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_2690 = func_2401_call()
call_2691 = func_2401_call()
output = relay.Tuple([call_2690,])
output2 = relay.Tuple([call_2691,])
func_2692 = relay.Function([], output)
mod['func_2692'] = func_2692
mod = relay.transform.InferType()(mod)
mutated_mod['func_2692'] = func_2692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2692_call = mutated_mod.get_global_var('func_2692')
call_2693 = func_2692_call()
output = call_2693
func_2694 = relay.Function([], output)
mutated_mod['func_2694'] = func_2694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2632_call = mod.get_global_var('func_2632')
func_2633_call = mutated_mod.get_global_var('func_2633')
call_2759 = func_2632_call()
call_2760 = func_2632_call()
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_2763 = relay.TupleGetItem(func_2460_call(), 0)
call_2764 = relay.TupleGetItem(func_2462_call(), 0)
bop_2765 = relay.greater(call_2763.astype('bool'), relay.reshape(call_2759.astype('bool'), relay.shape_of(call_2763))) # shape=(15, 11, 6)
bop_2768 = relay.greater(call_2764.astype('bool'), relay.reshape(call_2760.astype('bool'), relay.shape_of(call_2764))) # shape=(15, 11, 6)
uop_2770 = relay.tan(call_2763.astype('float32')) # shape=(15, 11, 6)
uop_2772 = relay.tan(call_2764.astype('float32')) # shape=(15, 11, 6)
bop_2774 = relay.less(bop_2765.astype('bool'), relay.reshape(call_2763.astype('bool'), relay.shape_of(bop_2765))) # shape=(15, 11, 6)
bop_2777 = relay.less(bop_2768.astype('bool'), relay.reshape(call_2764.astype('bool'), relay.shape_of(bop_2768))) # shape=(15, 11, 6)
bop_2781 = relay.floor_mod(uop_2770.astype('float64'), relay.reshape(bop_2774.astype('float64'), relay.shape_of(uop_2770))) # shape=(15, 11, 6)
bop_2784 = relay.floor_mod(uop_2772.astype('float64'), relay.reshape(bop_2777.astype('float64'), relay.shape_of(uop_2772))) # shape=(15, 11, 6)
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
const_2786 = relay.const([3,3,-6,3,-1,2,8,4,4,-4,-8,6,7,7,-3,7,8,9,2,3,8,-9,-9,-2,6,5,-2,9,-2,-7,1,-2,-5,-3,10,-10,-5,9,-3,8,-8,-1,-3,-10,-7,1,-2,-8,-1,3,9,4,-2,8,3,-3,9,1,-6,-9,9,-4,-3,7,-3,7,-4,8,1,3,1,7,2,6,-7,5,-6,-7,9,-3,6,6,1,10,-9,-8,-1,-4,2,-2], dtype = "int32")#candidate|2786|(90,)|const|int32
call_2785 = func_128_call(relay.reshape(const_2786.astype('int32'), [2, 15, 3]), relay.reshape(const_2786.astype('int32'), [2, 15, 3]), )
call_2787 = func_128_call(relay.reshape(const_2786.astype('int32'), [2, 15, 3]), relay.reshape(const_2786.astype('int32'), [2, 15, 3]), )
output = relay.Tuple([bop_2781,call_2785,const_2786,])
output2 = relay.Tuple([bop_2784,call_2787,const_2786,])
func_2793 = relay.Function([], output)
mod['func_2793'] = func_2793
mod = relay.transform.InferType()(mod)
output = func_2793()
func_2794 = relay.Function([], output)
mutated_mod['func_2794'] = func_2794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_2798 = relay.TupleGetItem(func_2793_call(), 1)
call_2799 = relay.TupleGetItem(func_2794_call(), 1)
func_2645_call = mod.get_global_var('func_2645')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_2800 = func_2645_call()
call_2801 = func_2645_call()
output = relay.Tuple([call_2798,call_2800,])
output2 = relay.Tuple([call_2799,call_2801,])
func_2824 = relay.Function([], output)
mod['func_2824'] = func_2824
mod = relay.transform.InferType()(mod)
mutated_mod['func_2824'] = func_2824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mutated_mod.get_global_var('func_2824')
call_2825 = func_2824_call()
output = call_2825
func_2826 = relay.Function([], output)
mutated_mod['func_2826'] = func_2826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2632_call = mod.get_global_var('func_2632')
func_2633_call = mutated_mod.get_global_var('func_2633')
call_2871 = func_2632_call()
call_2872 = func_2632_call()
output = relay.Tuple([call_2871,])
output2 = relay.Tuple([call_2872,])
func_2873 = relay.Function([], output)
mod['func_2873'] = func_2873
mod = relay.transform.InferType()(mod)
output = func_2873()
func_2874 = relay.Function([], output)
mutated_mod['func_2874'] = func_2874
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2951 = relay.var("var_2951", dtype = "float64", shape = (7, 9, 5))#candidate|2951|(7, 9, 5)|var|float64
uop_2952 = relay.atanh(var_2951.astype('float64')) # shape=(7, 9, 5)
func_2873_call = mod.get_global_var('func_2873')
func_2874_call = mutated_mod.get_global_var('func_2874')
call_2956 = relay.TupleGetItem(func_2873_call(), 0)
call_2957 = relay.TupleGetItem(func_2874_call(), 0)
output = relay.Tuple([uop_2952,call_2956,])
output2 = relay.Tuple([uop_2952,call_2957,])
func_2962 = relay.Function([var_2951,], output)
mod['func_2962'] = func_2962
mod = relay.transform.InferType()(mod)
var_2963 = relay.var("var_2963", dtype = "float64", shape = (7, 9, 5))#candidate|2963|(7, 9, 5)|var|float64
output = func_2962(var_2963)
func_2964 = relay.Function([var_2963], output)
mutated_mod['func_2964'] = func_2964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2401_call = mod.get_global_var('func_2401')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_2980 = func_2401_call()
call_2981 = func_2401_call()
uop_2983 = relay.cosh(call_2980.astype('float32')) # shape=(15, 11, 6)
uop_2985 = relay.cosh(call_2981.astype('float32')) # shape=(15, 11, 6)
output = uop_2983
output2 = uop_2985
func_2990 = relay.Function([], output)
mod['func_2990'] = func_2990
mod = relay.transform.InferType()(mod)
mutated_mod['func_2990'] = func_2990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2990_call = mutated_mod.get_global_var('func_2990')
call_2991 = func_2990_call()
output = call_2991
func_2992 = relay.Function([], output)
mutated_mod['func_2992'] = func_2992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2873_call = mod.get_global_var('func_2873')
func_2874_call = mutated_mod.get_global_var('func_2874')
call_3004 = relay.TupleGetItem(func_2873_call(), 0)
call_3005 = relay.TupleGetItem(func_2874_call(), 0)
var_3006 = relay.var("var_3006", dtype = "int8", shape = (15, 11, 6))#candidate|3006|(15, 11, 6)|var|int8
bop_3007 = relay.less_equal(call_3004.astype('bool'), relay.reshape(var_3006.astype('bool'), relay.shape_of(call_3004))) # shape=(15, 11, 6)
bop_3010 = relay.less_equal(call_3005.astype('bool'), relay.reshape(var_3006.astype('bool'), relay.shape_of(call_3005))) # shape=(15, 11, 6)
uop_3012 = relay.asin(call_3004.astype('float64')) # shape=(15, 11, 6)
uop_3014 = relay.asin(call_3005.astype('float64')) # shape=(15, 11, 6)
func_2873_call = mod.get_global_var('func_2873')
func_2874_call = mutated_mod.get_global_var('func_2874')
call_3025 = relay.TupleGetItem(func_2873_call(), 0)
call_3026 = relay.TupleGetItem(func_2874_call(), 0)
func_2990_call = mod.get_global_var('func_2990')
func_2992_call = mutated_mod.get_global_var('func_2992')
call_3027 = func_2990_call()
call_3028 = func_2990_call()
func_2692_call = mod.get_global_var('func_2692')
func_2694_call = mutated_mod.get_global_var('func_2694')
call_3035 = relay.TupleGetItem(func_2692_call(), 0)
call_3036 = relay.TupleGetItem(func_2694_call(), 0)
output = relay.Tuple([bop_3007,uop_3012,call_3025,call_3027,call_3035,])
output2 = relay.Tuple([bop_3010,uop_3014,call_3026,call_3028,call_3036,])
func_3038 = relay.Function([var_3006,], output)
mod['func_3038'] = func_3038
mod = relay.transform.InferType()(mod)
mutated_mod['func_3038'] = func_3038
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3039 = relay.var("var_3039", dtype = "int8", shape = (15, 11, 6))#candidate|3039|(15, 11, 6)|var|int8
func_3038_call = mutated_mod.get_global_var('func_3038')
call_3040 = func_3038_call(var_3039)
output = call_3040
func_3041 = relay.Function([var_3039], output)
mutated_mod['func_3041'] = func_3041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_3059 = relay.TupleGetItem(func_2793_call(), 2)
call_3060 = relay.TupleGetItem(func_2794_call(), 2)
output = relay.Tuple([call_3059,])
output2 = relay.Tuple([call_3060,])
func_3069 = relay.Function([], output)
mod['func_3069'] = func_3069
mod = relay.transform.InferType()(mod)
mutated_mod['func_3069'] = func_3069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mutated_mod.get_global_var('func_3069')
call_3070 = func_3069_call()
output = call_3070
func_3071 = relay.Function([], output)
mutated_mod['func_3071'] = func_3071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2632_call = mod.get_global_var('func_2632')
func_2633_call = mutated_mod.get_global_var('func_2633')
call_3082 = func_2632_call()
call_3083 = func_2632_call()
func_3069_call = mod.get_global_var('func_3069')
func_3071_call = mutated_mod.get_global_var('func_3071')
call_3091 = relay.TupleGetItem(func_3069_call(), 0)
call_3092 = relay.TupleGetItem(func_3071_call(), 0)
func_991_call = mod.get_global_var('func_991')
func_994_call = mutated_mod.get_global_var('func_994')
var_3100 = relay.var("var_3100", dtype = "float32", shape = (12,))#candidate|3100|(12,)|var|float32
const_3101 = relay.const([7.990945,4.576945,-4.722521,5.039420,-5.145023,9.721480,7.955499,-4.179405,-1.126779,7.527139,-8.628155,8.418462,2.128839,-8.123203,3.284491,5.848262,6.673878,8.348607,1.156361,3.746709,-9.145279,4.756679,5.229478,-2.235394,4.901497,-1.790276,6.611671,-6.232530,4.175009,4.478632,5.883239,4.590233,-0.155277,-3.643882,0.026516,5.954594,-5.005209,5.977396,2.840353,5.179389,-3.095214,-5.596421,7.371149,-0.247418,8.690539,6.463619,-8.826608,4.281065,-6.310217,-5.015276,7.163956,5.844544,5.070729,-9.383198,-1.436536,3.405672,1.935884,-2.379657,-9.798967,6.125673,9.633148,-4.847733,-8.770595,-8.205710,5.622716,-0.674249,-3.558599,-4.609700,3.866829,-4.540536,-4.025606,-2.337412,2.879873,-9.794706,0.197979,6.000558,2.441758,3.233805,6.930932,-4.943946,-1.643463,-8.952205,-4.984847,-9.234978,2.282198,-0.096520,-2.222148,9.729242,5.388464,-2.384370,-2.249715,6.558804,0.618629,6.267584,-1.539851,-4.248361,-7.146214,-9.523617,2.320397,-3.147449,1.252961,5.581198,0.943946,-2.389584,-9.739922,-2.207563,-4.475668,-3.092328,-5.590224,4.184009,2.707761,3.607586,-5.349677,7.731238,8.050423,-5.377604,-4.053467,-1.606605,-9.800210,-1.317046,9.309148,9.290186,6.736787,-4.100619,1.166402,-6.237765,2.931974,0.325162,5.615700,7.113428,-8.529428,-3.001645,0.515477,4.663545,9.829874,4.733062,-5.486757,-1.843236,-9.198022,5.746552,-6.174783,5.715013,5.389211,5.235491,1.454356,8.529262,-4.950752,-9.035470,4.758680,-1.275704,7.799968,3.951827,-8.284291,3.094530,-3.245215,9.810163], dtype = "float32")#candidate|3101|(156,)|const|float32
call_3099 = relay.TupleGetItem(func_991_call(relay.reshape(var_3100.astype('float32'), [6, 2, 1]), relay.reshape(const_3101.astype('float32'), [6, 2, 13]), ), 5)
call_3102 = relay.TupleGetItem(func_994_call(relay.reshape(var_3100.astype('float32'), [6, 2, 1]), relay.reshape(const_3101.astype('float32'), [6, 2, 13]), ), 5)
func_1311_call = mod.get_global_var('func_1311')
func_1314_call = mutated_mod.get_global_var('func_1314')
const_3105 = relay.const([-4.058618,6.413506,2.939718,-7.575631,8.928610,4.690552,2.483116,7.172588,-2.699407,-3.411499,7.350187,-5.244375,9.995525,-0.258569,-5.281058,-0.746046,-4.338762,6.257452,-1.682109,4.021368], dtype = "float32")#candidate|3105|(20,)|const|float32
call_3104 = relay.TupleGetItem(func_1311_call(relay.reshape(const_3105.astype('float32'), [10, 2, 1]), relay.reshape(call_3099.astype('int32'), [90, 1]), ), 2)
call_3106 = relay.TupleGetItem(func_1314_call(relay.reshape(const_3105.astype('float32'), [10, 2, 1]), relay.reshape(call_3099.astype('int32'), [90, 1]), ), 2)
bop_3114 = relay.greater_equal(call_3104.astype('bool'), relay.reshape(call_3091.astype('bool'), relay.shape_of(call_3104))) # shape=(90, 1)
bop_3117 = relay.greater_equal(call_3106.astype('bool'), relay.reshape(call_3092.astype('bool'), relay.shape_of(call_3106))) # shape=(90, 1)
output = relay.Tuple([call_3082,call_3099,var_3100,const_3101,const_3105,bop_3114,])
output2 = relay.Tuple([call_3083,call_3102,var_3100,const_3101,const_3105,bop_3117,])
func_3122 = relay.Function([var_3100,], output)
mod['func_3122'] = func_3122
mod = relay.transform.InferType()(mod)
var_3123 = relay.var("var_3123", dtype = "float32", shape = (12,))#candidate|3123|(12,)|var|float32
output = func_3122(var_3123)
func_3124 = relay.Function([var_3123], output)
mutated_mod['func_3124'] = func_3124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mod.get_global_var('func_3069')
func_3071_call = mutated_mod.get_global_var('func_3071')
call_3126 = relay.TupleGetItem(func_3069_call(), 0)
call_3127 = relay.TupleGetItem(func_3071_call(), 0)
output = call_3126
output2 = call_3127
func_3138 = relay.Function([], output)
mod['func_3138'] = func_3138
mod = relay.transform.InferType()(mod)
output = func_3138()
func_3139 = relay.Function([], output)
mutated_mod['func_3139'] = func_3139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2873_call = mod.get_global_var('func_2873')
func_2874_call = mutated_mod.get_global_var('func_2874')
call_3222 = relay.TupleGetItem(func_2873_call(), 0)
call_3223 = relay.TupleGetItem(func_2874_call(), 0)
func_1637_call = mod.get_global_var('func_1637')
func_1640_call = mutated_mod.get_global_var('func_1640')
var_3225 = relay.var("var_3225", dtype = "bool", shape = (2, 528))#candidate|3225|(2, 528)|var|bool
call_3224 = relay.TupleGetItem(func_1637_call(relay.reshape(var_3225.astype('bool'), [11, 6, 16]), relay.reshape(var_3225.astype('bool'), [11, 6, 16]), ), 3)
call_3226 = relay.TupleGetItem(func_1640_call(relay.reshape(var_3225.astype('bool'), [11, 6, 16]), relay.reshape(var_3225.astype('bool'), [11, 6, 16]), ), 3)
output = relay.Tuple([call_3222,call_3224,var_3225,])
output2 = relay.Tuple([call_3223,call_3226,var_3225,])
func_3238 = relay.Function([var_3225,], output)
mod['func_3238'] = func_3238
mod = relay.transform.InferType()(mod)
var_3239 = relay.var("var_3239", dtype = "bool", shape = (2, 528))#candidate|3239|(2, 528)|var|bool
output = func_3238(var_3239)
func_3240 = relay.Function([var_3239], output)
mutated_mod['func_3240'] = func_3240
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3246 = relay.var("var_3246", dtype = "uint8", shape = (2, 16, 8))#candidate|3246|(2, 16, 8)|var|uint8
var_3247 = relay.var("var_3247", dtype = "uint8", shape = (2, 16, 8))#candidate|3247|(2, 16, 8)|var|uint8
bop_3248 = relay.subtract(var_3246.astype('uint8'), relay.reshape(var_3247.astype('uint8'), relay.shape_of(var_3246))) # shape=(2, 16, 8)
func_2873_call = mod.get_global_var('func_2873')
func_2874_call = mutated_mod.get_global_var('func_2874')
call_3253 = relay.TupleGetItem(func_2873_call(), 0)
call_3254 = relay.TupleGetItem(func_2874_call(), 0)
func_2287_call = mod.get_global_var('func_2287')
func_2290_call = mutated_mod.get_global_var('func_2290')
const_3262 = relay.const([-1,4,8,2,-2,-1,-8,5,1,-7,-7,7,-9,-1,10,9,-5,-5,-2,1,9,-9,2,6,-6,-8,-1,10,-9,-9,1,10,-10,8,-3,8,-4,-8,2,8,8,8,-2,-9,9,9,5,-7,6,1,-6,-9,7,-7,-1,7,-2,9,5,-6,-8,-4,6,-10,-9,-10,-1,5,8,8,-8,9,2,-5,-7,-1,8,8,9,6,10,-10,7,-10,9,4,-3,-7,-2,1,-5,-4,10,-7,-3,-4,1,5,-1,-4,-3,8,-3,4,-5,-5,-7,-3,3,5,-7,9,5,7,-9,8,3,-9,-9,10,-7,-6,5,3,-3,4,-9,7,6,-4,7,8,-8,-6,1,-4,-2,5,2,-5,-8,3,9,3,-4,-2,-1,-2,-7,-7,-6,-7,1,-6,-9,8,-10,-7,2,6,-9,10,-7,6,-1,-2,-3,-5,-10,9,-2,9,9,2,-5,9,5,1,-2,-9,1,-9,-10,-1,7,-2,-7,2,-6,-7,-1,5,8,1,7,2,-1,4,-7,-2,3,3,4,3,-10,-2,-1,-8,-3,10,8,7,4,1,-4,-6,-8,6,4,3,-4,-6,2,-5,-4,-6,-6,2,-4,-1,-7,-7,4,10,-5,-4,7,-5,6,5,-4,4,4,9,-10,-10,5,-5,-3,9,-7,-8,-6,5,-2,4,1,-3,4,5,-10,5,2,-6,-5,4,1,8,4,9,-6,-9,9,-4,-6,10,-5,3,5,4,-4,1,10,-3,5,-10,5,1,-3,-8,5,-7,3,10,9,9,2,-1,1,9,-5,10,10,3,-6,2,-9,6,1,3,1,3,1,-8,-7,-2,-5,2,4,1,-6,-5,-4,-10,-6,2,4,1,-3,-10,7,3,-6,9,10,-2,-3,-3,8,1,-6,-1,10,6,2,-4,-1,1,5,5,-8,-4,-4,9,10,-5,-2,-7,-10,-8,2,-9,2,-10,10,2,4,10,-3,-9,-8,9,3,-2,10,3,-3,-7,-2,10,2,-1,-8,-4,1,-1,-10,-9,-8,-5,-1,2,-1,-7,-6,9,10,4,-3,6,4,5,10,6,-2,-6,-9,9,1,-5,4,5,-3,2,9,-2,-5,-6,10,1,-5,7,9,-4,-3,-7,4,-10,5,5,-10,-9,-5,-8,-9,6,-9,-5,-10,-9,9,-9,10,-10,-3,-8,-3,8,2,-10,6,-2,-1,-3,8,-4,-8,10,4,2,6,-10,7,-4,5,-9,-1,6,-1,-3,-1,-8,7,8,9,-9,-1,1,-7,8,-10,-3,-1,-3,7,1,-10,-6,6,-10,-5,-9,6,-4,-6,4,-1,-9,5,-5,7,-10,-5,-5,2,6,-4,2,7,-4,-10,9,7,-2,-9,5,-2,-4,-1,8,4,-1,-8,-8,-10,-8,-3,2], dtype = "uint32")#candidate|3262|(528,)|const|uint32
call_3261 = relay.TupleGetItem(func_2287_call(relay.reshape(const_3262.astype('uint32'), [11, 12, 4]), relay.reshape(const_3262.astype('uint32'), [11, 12, 4]), ), 2)
call_3263 = relay.TupleGetItem(func_2290_call(relay.reshape(const_3262.astype('uint32'), [11, 12, 4]), relay.reshape(const_3262.astype('uint32'), [11, 12, 4]), ), 2)
func_3069_call = mod.get_global_var('func_3069')
func_3071_call = mutated_mod.get_global_var('func_3071')
call_3269 = relay.TupleGetItem(func_3069_call(), 0)
call_3270 = relay.TupleGetItem(func_3071_call(), 0)
uop_3284 = relay.log10(const_3262.astype('float32')) # shape=(528,)
func_3038_call = mod.get_global_var('func_3038')
func_3041_call = mutated_mod.get_global_var('func_3041')
call_3286 = relay.TupleGetItem(func_3038_call(relay.reshape(call_3253.astype('int8'), [15, 11, 6])), 0)
call_3287 = relay.TupleGetItem(func_3041_call(relay.reshape(call_3253.astype('int8'), [15, 11, 6])), 0)
func_2962_call = mod.get_global_var('func_2962')
func_2964_call = mutated_mod.get_global_var('func_2964')
const_3302 = relay.const([[5.586308],[-1.080191],[3.833598],[-3.107454],[-6.640597],[-3.328731],[-4.743716],[2.800819],[-9.038242],[0.462247],[3.405278],[-1.534651],[-6.762621],[1.143152],[-0.199331],[0.354797],[4.627114],[-2.769460],[-1.615267],[9.884751],[5.543040],[-6.896578],[8.244113],[8.282880],[-0.962580],[-7.217745],[-4.942991],[-6.680007],[-9.785696],[-9.187983],[-2.551635],[-3.724389],[0.432109],[-6.229783],[-7.055180],[-3.636915],[7.024097],[9.673417],[-4.507461],[-6.571274],[-3.716644],[-4.329910],[2.415348],[2.357816],[-1.080775],[7.820486],[5.936922],[-3.691103],[-6.939915],[-0.409500],[4.428129],[4.186257],[5.723635],[9.438774],[6.681702],[-0.932622],[-4.276297],[2.525391],[2.296586],[1.801075],[-8.093574],[-6.009299],[6.563451],[-3.178057],[2.330552],[-2.089411],[6.138729],[7.435666],[-6.574786],[5.448767],[-5.176459],[8.729253],[-9.575165],[-1.576453],[6.503881],[-7.986271],[-4.165539],[5.783470],[2.918787],[-3.579598],[-8.412279],[0.807094],[-6.878835],[-8.727890],[-0.293165],[-4.618833],[9.953131],[1.387867],[-7.349037],[5.757967],[-9.520751],[9.691967],[-4.271002],[-6.966680],[-6.600547],[-9.310067],[8.242174],[4.101613],[-4.850196],[-5.754297],[5.110024],[9.049591],[7.372585],[-0.414950],[7.953657],[7.048969],[1.937646],[-2.605334],[-3.713002],[-9.702807],[6.728270],[1.424617],[-3.209246],[-9.722457],[4.639661],[9.549875],[-6.818061],[6.280037],[-3.466207],[6.565782],[-1.169305],[4.737426],[-2.796725],[5.648616],[-5.889280],[1.825977],[8.651783],[-1.287990],[6.075593],[-9.008946],[1.100663],[6.530775],[7.687342],[0.197583],[3.663130],[6.530598],[-7.434033],[4.721408],[-4.941739],[2.147977],[-7.611121],[8.565144],[3.020745],[-0.364289],[-1.010821],[2.173927],[-1.899694],[7.335316],[-2.840054],[2.522191],[-4.687066],[5.386767],[1.869624],[3.758233],[2.088647],[-1.576695],[2.058455],[3.385012],[7.262747],[-6.435320],[3.793526],[-7.101138],[-6.715766],[8.090703],[-9.002759],[-0.881339],[1.002053],[6.954926],[8.486295],[-3.906310],[2.326601],[-1.686938],[-8.007012],[-2.085854],[1.236479],[-6.818761],[-2.191997],[7.565282],[-9.569808],[1.558026],[8.325267],[2.520817],[1.479182],[-9.606467],[3.534388],[-8.614661],[8.121498],[-3.334905],[-2.474073],[-2.372570],[2.161997],[-0.617265],[4.474613],[-4.271576],[-9.304890],[-6.645467],[-8.789816],[-3.983406],[3.360679],[-1.483104],[-5.574271],[0.242708],[2.392463],[8.452508],[-9.708869],[-8.052164],[-8.993278],[-9.522327],[-0.542222],[-0.951270],[-8.194400],[-7.590374],[-5.707259],[2.130819],[7.685535],[1.083104],[-8.883818],[-9.251246],[-1.832067],[5.151492],[1.584290],[-9.244403],[3.908728],[3.095492],[7.546797],[-1.759442],[-8.865539],[-5.287758],[-1.421314],[-4.541094],[6.805464],[4.217854],[2.269590],[-1.566704],[9.477774],[-3.769177],[1.586314],[8.341022],[2.190362],[-6.301016],[-6.504962],[0.204208],[5.841103],[9.728227],[1.811740],[-3.010879],[7.277883],[-2.896334],[6.254905],[-9.989598],[-4.532997],[2.646825],[7.999112],[-5.639511],[3.930043],[-2.007516],[-0.183619],[-2.909760],[2.258618],[3.816593],[-7.356343],[-4.446288],[5.536622],[-4.367290],[8.467089],[2.675355],[0.976758],[1.393422],[1.370892],[-8.084816],[-8.561244],[-5.040838],[-6.134613],[-4.808894],[5.071800],[-9.948536],[3.243597],[3.602309],[8.024338],[1.257014],[5.054570],[-3.892288],[6.758202],[2.126613],[-3.066994],[4.732654],[-9.512230],[9.304326],[7.745802],[3.007871],[4.831316],[-6.157414],[-7.632675],[5.155907],[5.462124],[-1.627250],[0.801378],[7.558573],[-2.979438],[-0.063611],[-8.711509],[2.669703],[2.048687],[1.672432],[-0.096233],[9.762559],[-0.355191],[3.417610],[-4.727689],[-0.450233],[9.358445],[-6.658146],[-3.817528],[-6.107573],[-3.761858]], dtype = "float64")#candidate|3302|(315, 1)|const|float64
call_3301 = relay.TupleGetItem(func_2962_call(relay.reshape(const_3302.astype('float64'), [7, 9, 5])), 0)
call_3303 = relay.TupleGetItem(func_2964_call(relay.reshape(const_3302.astype('float64'), [7, 9, 5])), 0)
output = relay.Tuple([bop_3248,call_3253,call_3261,call_3269,uop_3284,call_3286,call_3301,const_3302,])
output2 = relay.Tuple([bop_3248,call_3254,call_3263,call_3270,uop_3284,call_3287,call_3303,const_3302,])
func_3304 = relay.Function([var_3246,var_3247,], output)
mod['func_3304'] = func_3304
mod = relay.transform.InferType()(mod)
var_3305 = relay.var("var_3305", dtype = "uint8", shape = (2, 16, 8))#candidate|3305|(2, 16, 8)|var|uint8
var_3306 = relay.var("var_3306", dtype = "uint8", shape = (2, 16, 8))#candidate|3306|(2, 16, 8)|var|uint8
output = func_3304(var_3305,var_3306,)
func_3307 = relay.Function([var_3305,var_3306,], output)
mutated_mod['func_3307'] = func_3307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2645_call = mod.get_global_var('func_2645')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_3314 = func_2645_call()
call_3315 = func_2645_call()
output = relay.Tuple([call_3314,])
output2 = relay.Tuple([call_3315,])
func_3330 = relay.Function([], output)
mod['func_3330'] = func_3330
mod = relay.transform.InferType()(mod)
output = func_3330()
func_3331 = relay.Function([], output)
mutated_mod['func_3331'] = func_3331
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3344 = relay.var("var_3344", dtype = "float64", shape = (6, 9, 12))#candidate|3344|(6, 9, 12)|var|float64
uop_3345 = relay.tan(var_3344.astype('float64')) # shape=(6, 9, 12)
func_3038_call = mod.get_global_var('func_3038')
func_3041_call = mutated_mod.get_global_var('func_3041')
var_3356 = relay.var("var_3356", dtype = "int8", shape = (990,))#candidate|3356|(990,)|var|int8
call_3355 = relay.TupleGetItem(func_3038_call(relay.reshape(var_3356.astype('int8'), [15, 11, 6])), 0)
call_3357 = relay.TupleGetItem(func_3041_call(relay.reshape(var_3356.astype('int8'), [15, 11, 6])), 0)
output = relay.Tuple([uop_3345,call_3355,var_3356,])
output2 = relay.Tuple([uop_3345,call_3357,var_3356,])
func_3358 = relay.Function([var_3344,var_3356,], output)
mod['func_3358'] = func_3358
mod = relay.transform.InferType()(mod)
var_3359 = relay.var("var_3359", dtype = "float64", shape = (6, 9, 12))#candidate|3359|(6, 9, 12)|var|float64
var_3360 = relay.var("var_3360", dtype = "int8", shape = (990,))#candidate|3360|(990,)|var|int8
output = func_3358(var_3359,var_3360,)
func_3361 = relay.Function([var_3359,var_3360,], output)
mutated_mod['func_3361'] = func_3361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_3467 = relay.TupleGetItem(func_2460_call(), 0)
call_3468 = relay.TupleGetItem(func_2462_call(), 0)
uop_3470 = relay.acosh(call_3467.astype('float32')) # shape=(15, 11, 6)
uop_3472 = relay.acosh(call_3468.astype('float32')) # shape=(15, 11, 6)
uop_3477 = relay.asinh(uop_3470.astype('float64')) # shape=(15, 11, 6)
uop_3479 = relay.asinh(uop_3472.astype('float64')) # shape=(15, 11, 6)
uop_3481 = relay.log10(uop_3477.astype('float64')) # shape=(15, 11, 6)
uop_3483 = relay.log10(uop_3479.astype('float64')) # shape=(15, 11, 6)
uop_3496 = relay.rsqrt(uop_3481.astype('float64')) # shape=(15, 11, 6)
uop_3498 = relay.rsqrt(uop_3483.astype('float64')) # shape=(15, 11, 6)
output = relay.Tuple([uop_3496,])
output2 = relay.Tuple([uop_3498,])
func_3508 = relay.Function([], output)
mod['func_3508'] = func_3508
mod = relay.transform.InferType()(mod)
output = func_3508()
func_3509 = relay.Function([], output)
mutated_mod['func_3509'] = func_3509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_3524 = relay.TupleGetItem(func_2793_call(), 2)
call_3525 = relay.TupleGetItem(func_2794_call(), 2)
output = call_3524
output2 = call_3525
func_3540 = relay.Function([], output)
mod['func_3540'] = func_3540
mod = relay.transform.InferType()(mod)
mutated_mod['func_3540'] = func_3540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3540_call = mutated_mod.get_global_var('func_3540')
call_3541 = func_3540_call()
output = call_3541
func_3542 = relay.Function([], output)
mutated_mod['func_3542'] = func_3542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mod.get_global_var('func_3069')
func_3071_call = mutated_mod.get_global_var('func_3071')
call_3587 = relay.TupleGetItem(func_3069_call(), 0)
call_3588 = relay.TupleGetItem(func_3071_call(), 0)
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_3601 = relay.TupleGetItem(func_2460_call(), 0)
call_3602 = relay.TupleGetItem(func_2462_call(), 0)
func_498_call = mod.get_global_var('func_498')
func_501_call = mutated_mod.get_global_var('func_501')
var_3604 = relay.var("var_3604", dtype = "uint8", shape = (1170,))#candidate|3604|(1170,)|var|uint8
call_3603 = relay.TupleGetItem(func_498_call(relay.reshape(var_3604.astype('uint8'), [6, 13, 15])), 1)
call_3605 = relay.TupleGetItem(func_501_call(relay.reshape(var_3604.astype('uint8'), [6, 13, 15])), 1)
var_3611 = relay.var("var_3611", dtype = "uint8", shape = (1170,))#candidate|3611|(1170,)|var|uint8
bop_3612 = relay.less(var_3604.astype('bool'), relay.reshape(var_3611.astype('bool'), relay.shape_of(var_3604))) # shape=(1170,)
func_2571_call = mod.get_global_var('func_2571')
func_2576_call = mutated_mod.get_global_var('func_2576')
const_3618 = relay.const([-8,-8,-1,-5,-10,4,-7,9,-9,-8,-3,-2,-6,-9,-7,-3,7,-7,8,9,2,-3,6,-6,-6,-7,3,-10,-8,-3,-9,-3,10,5,1,-5,9,1,-1,-2,3,-9,-3,-9,-10,-7,1,-7,7,6,-8,-10,-10,-4,-7,-1,6,-1,9,-9,2,-9,-5,1,-8,9,-1,-3,-9,3,1,-8,-2,-7,9,-1,3,6,-6,-9,6,-10,-6,-8,-8,-3,-5,-10,-2,-9,5,5,-1,6,-8,2,1,-2,5,-4,-3,3,-1,-8,-2,-5,-8,-4,1,-6,5,4,-10,-4,8,-7,6,10,5,-10], dtype = "int32")#candidate|3618|(120,)|const|int32
call_3617 = relay.TupleGetItem(func_2571_call(relay.reshape(const_3618.astype('int32'), [10, 4, 3]), relay.reshape(const_3618.astype('int32'), [10, 4, 3]), relay.reshape(call_3587.astype('int32'), [90,]), relay.reshape(const_3618.astype('float32'), [10, 4, 3]), ), 5)
call_3619 = relay.TupleGetItem(func_2576_call(relay.reshape(const_3618.astype('int32'), [10, 4, 3]), relay.reshape(const_3618.astype('int32'), [10, 4, 3]), relay.reshape(call_3587.astype('int32'), [90,]), relay.reshape(const_3618.astype('float32'), [10, 4, 3]), ), 5)
output = relay.Tuple([call_3587,call_3601,call_3603,bop_3612,call_3617,const_3618,])
output2 = relay.Tuple([call_3588,call_3602,call_3605,bop_3612,call_3619,const_3618,])
func_3622 = relay.Function([var_3604,var_3611,], output)
mod['func_3622'] = func_3622
mod = relay.transform.InferType()(mod)
mutated_mod['func_3622'] = func_3622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3622_call = mutated_mod.get_global_var('func_3622')
var_3624 = relay.var("var_3624", dtype = "uint8", shape = (1170,))#candidate|3624|(1170,)|var|uint8
var_3625 = relay.var("var_3625", dtype = "uint8", shape = (1170,))#candidate|3625|(1170,)|var|uint8
call_3623 = func_3622_call(var_3624,var_3625,)
output = call_3623
func_3626 = relay.Function([var_3624,var_3625,], output)
mutated_mod['func_3626'] = func_3626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mod.get_global_var('func_3069')
func_3071_call = mutated_mod.get_global_var('func_3071')
call_3628 = relay.TupleGetItem(func_3069_call(), 0)
call_3629 = relay.TupleGetItem(func_3071_call(), 0)
output = relay.Tuple([call_3628,])
output2 = relay.Tuple([call_3629,])
func_3636 = relay.Function([], output)
mod['func_3636'] = func_3636
mod = relay.transform.InferType()(mod)
mutated_mod['func_3636'] = func_3636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3636_call = mutated_mod.get_global_var('func_3636')
call_3637 = func_3636_call()
output = call_3637
func_3638 = relay.Function([], output)
mutated_mod['func_3638'] = func_3638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2645_call = mod.get_global_var('func_2645')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_3661 = func_2645_call()
call_3662 = func_2645_call()
var_3665 = relay.var("var_3665", dtype = "int8", shape = (15, 11, 6))#candidate|3665|(15, 11, 6)|var|int8
bop_3666 = relay.bitwise_or(call_3661.astype('int32'), relay.reshape(var_3665.astype('int32'), relay.shape_of(call_3661))) # shape=(15, 11, 6)
bop_3669 = relay.bitwise_or(call_3662.astype('int32'), relay.reshape(var_3665.astype('int32'), relay.shape_of(call_3662))) # shape=(15, 11, 6)
func_3304_call = mod.get_global_var('func_3304')
func_3307_call = mutated_mod.get_global_var('func_3307')
const_3675 = relay.const([-3,7,-3,1,7,2,-2,7,4,7,-9,10,-1,-2,-3,5,-1,7,-1,-6,6,-2,-6,10,-10,-9,8,-9,-2,-1,-1,-2,-9,8,7,10,2,2,2,-10,-6,3,6,2,4,4,10,-8,5,2,-10,5,-6,-9,-8,-1,6,8,-4,2,6,3,-4,-8,5,-10,2,-6,-2,-5,4,5,-9,-3,-5,-3,3,-8,5,5,-6,6,2,-4,-6,3,6,9,-2,8,-7,10,-7,6,-6,3,-8,8,2,4,-5,-6,-4,-6,-7,-4,7,4,-4,-5,3,-10,8,3,-4,-6,2,1,8,4,4,-2,4,3,8,8,-6,4,-8,4,2,2,5,-3,3,-10,7,-5,8,9,-8,7,5,9,-6,9,6,-3,-7,4,4,-4,-6,2,-9,-1,-7,-2,-10,8,-6,6,-8,-1,-5,-2,10,10,7,1,-2,-4,3,-9,-6,10,2,2,-5,5,-9,-1,-5,7,10,1,-2,-10,10,7,6,6,1,10,-4,-8,-3,1,9,-3,6,2,8,3,9,2,7,-5,-9,-6,1,-5,4,-6,4,1,-3,9,3,9,-4,-9,-2,-1,3,-3,3,1,-4,8,4,7,2,-1,10,9,1,-4,6,6,-3,4,-7,-3,9,8,-3,-3,2,2,-3,3,2,-1,-3,8], dtype = "uint8")#candidate|3675|(256,)|const|uint8
call_3674 = relay.TupleGetItem(func_3304_call(relay.reshape(const_3675.astype('uint8'), [2, 16, 8]), relay.reshape(const_3675.astype('uint8'), [2, 16, 8]), ), 5)
call_3676 = relay.TupleGetItem(func_3307_call(relay.reshape(const_3675.astype('uint8'), [2, 16, 8]), relay.reshape(const_3675.astype('uint8'), [2, 16, 8]), ), 5)
func_3508_call = mod.get_global_var('func_3508')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_3678 = relay.TupleGetItem(func_3508_call(), 0)
call_3679 = relay.TupleGetItem(func_3509_call(), 0)
var_3681 = relay.var("var_3681", dtype = "float64", shape = (15, 11, 6))#candidate|3681|(15, 11, 6)|var|float64
bop_3682 = relay.bitwise_xor(call_3678.astype('int16'), relay.reshape(var_3681.astype('int16'), relay.shape_of(call_3678))) # shape=(15, 11, 6)
bop_3685 = relay.bitwise_xor(call_3679.astype('int16'), relay.reshape(var_3681.astype('int16'), relay.shape_of(call_3679))) # shape=(15, 11, 6)
func_2962_call = mod.get_global_var('func_2962')
func_2964_call = mutated_mod.get_global_var('func_2964')
var_3704 = relay.var("var_3704", dtype = "float64", shape = (315,))#candidate|3704|(315,)|var|float64
call_3703 = relay.TupleGetItem(func_2962_call(relay.reshape(var_3704.astype('float64'), [7, 9, 5])), 1)
call_3705 = relay.TupleGetItem(func_2964_call(relay.reshape(var_3704.astype('float64'), [7, 9, 5])), 1)
func_128_call = mod.get_global_var('func_128')
func_132_call = mutated_mod.get_global_var('func_132')
var_3708 = relay.var("var_3708", dtype = "int32", shape = (90,))#candidate|3708|(90,)|var|int32
call_3707 = func_128_call(relay.reshape(var_3708.astype('int32'), [2, 15, 3]), relay.reshape(var_3708.astype('int32'), [2, 15, 3]), )
call_3709 = func_128_call(relay.reshape(var_3708.astype('int32'), [2, 15, 3]), relay.reshape(var_3708.astype('int32'), [2, 15, 3]), )
output = relay.Tuple([bop_3666,call_3674,const_3675,bop_3682,call_3703,var_3704,call_3707,var_3708,])
output2 = relay.Tuple([bop_3669,call_3676,const_3675,bop_3685,call_3705,var_3704,call_3709,var_3708,])
func_3738 = relay.Function([var_3665,var_3681,var_3704,var_3708,], output)
mod['func_3738'] = func_3738
mod = relay.transform.InferType()(mod)
var_3739 = relay.var("var_3739", dtype = "int8", shape = (15, 11, 6))#candidate|3739|(15, 11, 6)|var|int8
var_3740 = relay.var("var_3740", dtype = "float64", shape = (15, 11, 6))#candidate|3740|(15, 11, 6)|var|float64
var_3741 = relay.var("var_3741", dtype = "float64", shape = (315,))#candidate|3741|(315,)|var|float64
var_3742 = relay.var("var_3742", dtype = "int32", shape = (90,))#candidate|3742|(90,)|var|int32
output = func_3738(var_3739,var_3740,var_3741,var_3742,)
func_3743 = relay.Function([var_3739,var_3740,var_3741,var_3742,], output)
mutated_mod['func_3743'] = func_3743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3540_call = mod.get_global_var('func_3540')
func_3542_call = mutated_mod.get_global_var('func_3542')
call_3753 = func_3540_call()
call_3754 = func_3540_call()
output = relay.Tuple([call_3753,])
output2 = relay.Tuple([call_3754,])
func_3763 = relay.Function([], output)
mod['func_3763'] = func_3763
mod = relay.transform.InferType()(mod)
output = func_3763()
func_3764 = relay.Function([], output)
mutated_mod['func_3764'] = func_3764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2990_call = mod.get_global_var('func_2990')
func_2992_call = mutated_mod.get_global_var('func_2992')
call_3808 = func_2990_call()
call_3809 = func_2990_call()
output = call_3808
output2 = call_3809
func_3825 = relay.Function([], output)
mod['func_3825'] = func_3825
mod = relay.transform.InferType()(mod)
output = func_3825()
func_3826 = relay.Function([], output)
mutated_mod['func_3826'] = func_3826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3763_call = mod.get_global_var('func_3763')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_3870 = relay.TupleGetItem(func_3763_call(), 0)
call_3871 = relay.TupleGetItem(func_3764_call(), 0)
func_3825_call = mod.get_global_var('func_3825')
func_3826_call = mutated_mod.get_global_var('func_3826')
call_3890 = func_3825_call()
call_3891 = func_3825_call()
output = relay.Tuple([call_3870,call_3890,])
output2 = relay.Tuple([call_3871,call_3891,])
func_3901 = relay.Function([], output)
mod['func_3901'] = func_3901
mod = relay.transform.InferType()(mod)
mutated_mod['func_3901'] = func_3901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3901_call = mutated_mod.get_global_var('func_3901')
call_3902 = func_3901_call()
output = call_3902
func_3903 = relay.Function([], output)
mutated_mod['func_3903'] = func_3903
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3904 = relay.const(-3.932517, dtype = "float64")#candidate|3904|()|const|float64
var_3905 = relay.var("var_3905", dtype = "float64", shape = (10, 15, 12))#candidate|3905|(10, 15, 12)|var|float64
bop_3906 = relay.mod(const_3904.astype('float64'), var_3905.astype('float64')) # shape=(10, 15, 12)
output = relay.Tuple([bop_3906,])
output2 = relay.Tuple([bop_3906,])
func_3912 = relay.Function([var_3905,], output)
mod['func_3912'] = func_3912
mod = relay.transform.InferType()(mod)
var_3913 = relay.var("var_3913", dtype = "float64", shape = (10, 15, 12))#candidate|3913|(10, 15, 12)|var|float64
output = func_3912(var_3913)
func_3914 = relay.Function([var_3913], output)
mutated_mod['func_3914'] = func_3914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2990_call = mod.get_global_var('func_2990')
func_2992_call = mutated_mod.get_global_var('func_2992')
call_3936 = func_2990_call()
call_3937 = func_2990_call()
uop_3944 = relay.sin(call_3936.astype('float64')) # shape=(15, 11, 6)
uop_3946 = relay.sin(call_3937.astype('float64')) # shape=(15, 11, 6)
func_3636_call = mod.get_global_var('func_3636')
func_3638_call = mutated_mod.get_global_var('func_3638')
call_3954 = relay.TupleGetItem(func_3636_call(), 0)
call_3955 = relay.TupleGetItem(func_3638_call(), 0)
output = relay.Tuple([uop_3944,call_3954,])
output2 = relay.Tuple([uop_3946,call_3955,])
func_3964 = relay.Function([], output)
mod['func_3964'] = func_3964
mod = relay.transform.InferType()(mod)
mutated_mod['func_3964'] = func_3964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3964_call = mutated_mod.get_global_var('func_3964')
call_3965 = func_3964_call()
output = call_3965
func_3966 = relay.Function([], output)
mutated_mod['func_3966'] = func_3966
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3967 = relay.var("var_3967", dtype = "float32", shape = (6, 6, 5))#candidate|3967|(6, 6, 5)|var|float32
const_3968 = relay.const([[[3.150870,-2.110490,-3.563720,-0.483026,5.813013],[-1.152749,-2.580624,-8.583092,8.356652,-8.435409],[-2.447517,7.856397,1.540754,-6.405369,8.397507],[-9.663950,5.962632,-9.374770,-9.765964,-8.064276],[2.144507,-2.267026,-1.193727,0.179680,3.963289],[8.876572,-3.158833,-3.978804,0.988328,3.657420]],[[0.101888,-4.406760,7.259248,-8.200901,1.703676],[8.381135,-5.888440,-4.279888,-9.372512,-1.133504],[1.643420,6.525925,-5.471861,3.817639,-3.828861],[-5.030034,-1.147414,4.949270,-8.220171,1.202753],[-0.607226,-3.850701,7.515384,-6.185439,2.681377],[2.046286,-7.332934,-1.676511,4.997443,1.992225]],[[7.150358,4.610225,-1.159304,7.809317,-6.276180],[-6.376817,7.444205,9.985202,5.571184,2.553313],[-6.531580,0.851716,7.609743,-8.790610,-2.738781],[9.893739,6.314283,8.974251,4.329997,-5.800405],[-4.831349,-3.690362,-7.646557,-1.316601,8.350153],[-5.081913,-7.770237,8.451180,0.335717,-3.687289]],[[0.371842,3.998933,-7.108842,-0.220691,6.245661],[-3.866449,6.308761,-9.775772,-6.735964,6.638331],[-8.731064,-2.888204,3.493437,-8.406487,1.935871],[-7.772609,-3.334849,9.257935,0.638954,-4.587336],[0.457334,-0.246138,-8.313990,-8.536942,2.060549],[-3.529402,5.376306,-4.371484,-9.941544,1.270830]],[[-3.017628,-8.068880,-2.314313,1.097201,9.132751],[-1.647592,-0.130349,1.427577,3.968677,-8.673910],[3.550942,-8.626536,0.064623,-4.284640,-1.479395],[1.894852,9.938656,1.914373,2.175054,9.002494],[5.149437,2.677920,-8.805932,-3.956166,-9.003898],[-6.851442,4.120293,-8.460493,-1.908436,5.920842]],[[2.792017,3.775997,-7.721979,-7.017562,6.065752],[1.377017,9.382147,6.923327,7.646561,-3.540301],[-5.849908,-2.088182,3.569607,-5.966607,5.888461],[-5.562858,-6.728110,7.866797,9.799885,-1.201822],[-4.510085,7.603821,3.456071,4.606480,-9.325249],[-9.694450,1.451274,-4.344978,-3.197872,-5.604324]]], dtype = "float32")#candidate|3968|(6, 6, 5)|const|float32
bop_3969 = relay.power(var_3967.astype('float32'), relay.reshape(const_3968.astype('float32'), relay.shape_of(var_3967))) # shape=(6, 6, 5)
output = relay.Tuple([bop_3969,])
output2 = relay.Tuple([bop_3969,])
func_3978 = relay.Function([var_3967,], output)
mod['func_3978'] = func_3978
mod = relay.transform.InferType()(mod)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3979 = relay.var("var_3979", dtype = "float32", shape = (6, 6, 5))#candidate|3979|(6, 6, 5)|var|float32
func_3978_call = mutated_mod.get_global_var('func_3978')
call_3980 = func_3978_call(var_3979)
output = call_3980
func_3981 = relay.Function([var_3979], output)
mutated_mod['func_3981'] = func_3981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_3983 = relay.TupleGetItem(func_3508_call(), 0)
call_3984 = relay.TupleGetItem(func_3509_call(), 0)
func_1360_call = mod.get_global_var('func_1360')
func_1363_call = mutated_mod.get_global_var('func_1363')
var_3994 = relay.var("var_3994", dtype = "int32", shape = ())#candidate|3994|()|var|int32
const_3995 = relay.const([-10,8,2,-9,-5,-2,-8,-3,6,9,9,-7,5,-4,-10,10,2,9,9,-2,4,-5,-8,9,4,-4,-4,-1,4,1], dtype = "int32")#candidate|3995|(30,)|const|int32
call_3993 = func_1360_call(relay.reshape(var_3994.astype('int32'), []), relay.reshape(const_3995.astype('int32'), [1, 10, 3]), )
call_3996 = func_1360_call(relay.reshape(var_3994.astype('int32'), []), relay.reshape(const_3995.astype('int32'), [1, 10, 3]), )
output = relay.Tuple([call_3983,call_3993,var_3994,const_3995,])
output2 = relay.Tuple([call_3984,call_3996,var_3994,const_3995,])
func_3997 = relay.Function([var_3994,], output)
mod['func_3997'] = func_3997
mod = relay.transform.InferType()(mod)
var_3998 = relay.var("var_3998", dtype = "int32", shape = ())#candidate|3998|()|var|int32
output = func_3997(var_3998)
func_3999 = relay.Function([var_3998], output)
mutated_mod['func_3999'] = func_3999
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4029 = relay.var("var_4029", dtype = "float32", shape = (10, 10, 6))#candidate|4029|(10, 10, 6)|var|float32
var_4030 = relay.var("var_4030", dtype = "float32", shape = (10, 10, 6))#candidate|4030|(10, 10, 6)|var|float32
bop_4031 = relay.greater(var_4029.astype('bool'), relay.reshape(var_4030.astype('bool'), relay.shape_of(var_4029))) # shape=(10, 10, 6)
func_3330_call = mod.get_global_var('func_3330')
func_3331_call = mutated_mod.get_global_var('func_3331')
call_4034 = relay.TupleGetItem(func_3330_call(), 0)
call_4035 = relay.TupleGetItem(func_3331_call(), 0)
output = relay.Tuple([bop_4031,call_4034,])
output2 = relay.Tuple([bop_4031,call_4035,])
func_4038 = relay.Function([var_4029,var_4030,], output)
mod['func_4038'] = func_4038
mod = relay.transform.InferType()(mod)
mutated_mod['func_4038'] = func_4038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4038_call = mutated_mod.get_global_var('func_4038')
var_4040 = relay.var("var_4040", dtype = "float32", shape = (10, 10, 6))#candidate|4040|(10, 10, 6)|var|float32
var_4041 = relay.var("var_4041", dtype = "float32", shape = (10, 10, 6))#candidate|4041|(10, 10, 6)|var|float32
call_4039 = func_4038_call(var_4040,var_4041,)
output = call_4039
func_4042 = relay.Function([var_4040,var_4041,], output)
mutated_mod['func_4042'] = func_4042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_4077 = relay.TupleGetItem(func_2460_call(), 0)
call_4078 = relay.TupleGetItem(func_2462_call(), 0)
var_4095 = relay.var("var_4095", dtype = "int8", shape = (15, 11, 6))#candidate|4095|(15, 11, 6)|var|int8
bop_4096 = relay.floor_divide(call_4077.astype('float64'), relay.reshape(var_4095.astype('float64'), relay.shape_of(call_4077))) # shape=(15, 11, 6)
bop_4099 = relay.floor_divide(call_4078.astype('float64'), relay.reshape(var_4095.astype('float64'), relay.shape_of(call_4078))) # shape=(15, 11, 6)
output = relay.Tuple([bop_4096,])
output2 = relay.Tuple([bop_4099,])
func_4100 = relay.Function([var_4095,], output)
mod['func_4100'] = func_4100
mod = relay.transform.InferType()(mod)
var_4101 = relay.var("var_4101", dtype = "int8", shape = (15, 11, 6))#candidate|4101|(15, 11, 6)|var|int8
output = func_4100(var_4101)
func_4102 = relay.Function([var_4101], output)
mutated_mod['func_4102'] = func_4102
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4114 = relay.var("var_4114", dtype = "float64", shape = (3, 6, 10))#candidate|4114|(3, 6, 10)|var|float64
uop_4115 = relay.atanh(var_4114.astype('float64')) # shape=(3, 6, 10)
func_3825_call = mod.get_global_var('func_3825')
func_3826_call = mutated_mod.get_global_var('func_3826')
call_4117 = func_3825_call()
call_4118 = func_3825_call()
uop_4144 = relay.sqrt(uop_4115.astype('float32')) # shape=(3, 6, 10)
func_3978_call = mod.get_global_var('func_3978')
func_3981_call = mutated_mod.get_global_var('func_3981')
call_4147 = relay.TupleGetItem(func_3978_call(relay.reshape(uop_4144.astype('float32'), [6, 6, 5])), 0)
call_4148 = relay.TupleGetItem(func_3981_call(relay.reshape(uop_4144.astype('float32'), [6, 6, 5])), 0)
func_2824_call = mod.get_global_var('func_2824')
func_2826_call = mutated_mod.get_global_var('func_2826')
call_4152 = relay.TupleGetItem(func_2824_call(), 0)
call_4153 = relay.TupleGetItem(func_2826_call(), 0)
func_2645_call = mod.get_global_var('func_2645')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_4154 = func_2645_call()
call_4155 = func_2645_call()
output = relay.Tuple([call_4117,uop_4144,call_4147,call_4152,call_4154,])
output2 = relay.Tuple([call_4118,uop_4144,call_4148,call_4153,call_4155,])
func_4156 = relay.Function([var_4114,], output)
mod['func_4156'] = func_4156
mod = relay.transform.InferType()(mod)
var_4157 = relay.var("var_4157", dtype = "float64", shape = (3, 6, 10))#candidate|4157|(3, 6, 10)|var|float64
output = func_4156(var_4157)
func_4158 = relay.Function([var_4157], output)
mutated_mod['func_4158'] = func_4158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_4191 = relay.TupleGetItem(func_2793_call(), 0)
call_4192 = relay.TupleGetItem(func_2794_call(), 0)
const_4194 = relay.const([[[-6.153183,2.757897,5.937752,-6.725594,-7.442140,5.102271],[2.125514,-8.109293,-3.775206,-4.729564,2.006356,-1.085710],[3.604200,-7.693884,-7.792460,-8.555644,0.191873,1.462482],[8.922541,-5.322133,-9.498524,9.617735,0.324970,-1.714660],[1.745042,8.293147,0.135170,2.054352,-8.178028,-8.195476],[1.800380,1.080675,-6.622289,-5.345658,-3.244458,1.055288],[-1.354494,-3.368727,2.411742,3.759362,-3.207093,7.300400],[-6.383070,-2.129518,-7.718395,2.959838,-3.597502,-5.169287],[-7.628584,-0.628244,6.932662,4.868058,-5.458581,0.245010],[9.429852,-5.793244,3.183923,9.598134,-8.274861,-8.979954],[-9.211624,3.455793,-3.074131,6.310335,-4.876066,-0.595629]],[[7.708820,2.000844,5.880228,0.276052,6.303314,-1.567914],[-4.497978,9.867150,-6.006381,1.312150,9.122394,1.393910],[8.151599,-0.272397,-0.090318,5.062989,0.661459,8.683447],[-8.017554,3.875300,-6.488144,-9.959978,0.160287,-8.114187],[-3.205582,-0.037841,-2.901832,9.732694,-3.936317,5.281872],[-5.950913,-4.164752,5.418680,9.761224,9.065716,1.984987],[-7.001517,-2.606670,9.681960,0.464866,-9.619492,-3.417783],[9.921243,-1.077663,4.201577,-2.930223,0.076236,8.887628],[-4.458110,-6.333891,0.377091,-3.358043,4.109604,9.873224],[2.621703,-0.846186,-4.949043,-7.515297,2.287728,9.740110],[-5.835234,-0.217719,1.961165,-6.611938,-9.123269,9.535615]],[[-4.912629,-7.431604,-3.109947,4.193284,-5.976811,9.754213],[-0.731211,2.218141,7.765673,-2.627619,-8.903741,1.060460],[7.222529,-1.421752,-8.314181,8.244629,1.467239,-9.377902],[-8.923733,8.919157,-5.805840,2.318260,-6.956098,-8.232824],[-5.346389,7.534802,5.926812,-2.138922,-6.380006,1.445515],[-1.497049,9.786253,-3.201274,0.217811,5.797541,6.144035],[5.077213,-0.251860,2.182753,0.257685,-0.061754,1.286456],[9.667367,-4.511939,-6.785484,-1.461873,-4.335170,-1.720422],[-6.377444,8.512852,-5.467422,5.024466,-7.833376,2.319813],[-8.957216,2.890486,7.831108,-6.639041,-6.970195,-8.616491],[-9.690103,2.100940,-8.542220,1.115063,2.253827,4.927983]],[[-7.038315,6.580695,-5.596742,-6.717794,-1.986441,8.306060],[-9.725606,-2.898204,-2.749387,1.692523,-0.456617,-6.662101],[-4.252154,3.272362,-4.851639,3.868192,3.822726,9.587811],[8.986739,-2.731434,1.818654,2.064534,1.342560,-6.944970],[-8.765267,4.053633,-4.798832,-1.983343,5.779421,-0.562707],[-9.291136,-7.417574,2.076451,8.215202,-2.319065,-1.222329],[-1.576603,4.441669,3.059877,3.968444,-3.232625,-1.072662],[-1.481468,9.644033,-7.180991,-3.731717,-3.340820,-8.714516],[-9.826475,-8.539476,4.151419,8.046457,2.590068,-5.419154],[-0.821775,-6.709847,-5.414249,-0.510226,4.874686,-9.420951],[6.722867,-5.680377,-0.711768,4.541439,5.907697,1.105722]],[[-4.065413,-9.910540,8.741905,4.086351,-7.219640,-9.170660],[-5.112558,-4.486724,2.030014,-0.168229,1.654986,-6.402933],[8.632675,-0.364278,9.551688,-7.787822,-9.750426,6.823582],[5.772988,-7.361944,1.191725,-7.614818,3.279677,2.280919],[3.391021,3.697755,1.068988,-1.052550,-7.208715,6.823851],[-4.964790,4.723219,-0.096914,8.372382,5.081063,3.117186],[-7.949315,5.266826,-6.539254,-3.270025,-5.868304,-2.548700],[5.731531,-7.296624,-2.534564,-5.253221,1.571047,5.012545],[-6.992998,2.323007,-2.359634,-5.139350,-5.508013,-6.473046],[4.551660,8.982036,1.223798,2.931185,-1.402001,-9.268009],[3.949284,-3.492532,-5.566217,-5.881378,-8.911881,1.685239]],[[-8.484870,4.338229,3.816556,-8.544816,5.733908,-3.474177],[2.094807,2.355138,7.505496,-0.331498,-0.502942,-7.521746],[0.444734,-0.813225,-8.072976,-2.647127,9.227337,-6.504353],[-1.827932,8.362726,-0.639973,-5.262996,4.655606,7.651873],[3.186879,6.117598,-2.371773,-3.345287,-4.500513,5.684749],[-9.982375,-9.397921,-5.175296,-6.996660,1.065211,-3.942809],[6.788626,2.048433,-7.638536,-9.833137,9.824474,-3.988187],[5.756564,0.867847,2.693236,-6.718165,-7.154248,1.954642],[9.730007,3.228128,-2.346666,-3.123322,-0.553754,-6.800138],[6.466917,-7.522616,5.667774,-8.032485,-8.422414,-0.586963],[0.398535,1.789152,3.470827,-4.918595,9.816434,8.939534]],[[0.545912,5.425776,-4.598819,-7.043795,-7.506849,-8.139404],[9.036457,-5.982635,-4.629365,8.357873,-6.687495,1.188070],[-6.239685,-5.368220,-8.735963,1.091541,-8.217716,5.795260],[-2.405216,-3.323198,5.481738,-8.616758,1.970154,-9.598777],[-6.176992,6.797123,-2.544397,-3.065848,-7.092444,-6.854883],[8.635323,-8.096669,7.579920,-7.298675,-3.865398,-9.276043],[2.566760,-8.519530,-1.887872,-5.971197,7.077115,3.013396],[-6.490753,-7.849927,-6.883685,0.672759,-2.589864,7.556491],[-2.670548,5.131541,-9.492434,-7.895597,5.817289,8.244276],[9.056651,-9.752577,7.007421,-4.852045,1.768899,3.743655],[-1.430254,1.554805,-2.785980,-6.418748,-6.118574,3.167913]],[[0.693347,-9.027952,9.215043,-7.240810,4.923393,9.262984],[-0.165655,8.736903,-0.310442,-9.923693,5.139377,7.958696],[-3.491635,-7.905102,8.874085,-3.631375,5.445149,6.179889],[-6.959739,4.147602,-4.022717,-2.014060,3.199443,1.154998],[-1.455511,-4.844613,6.762928,-4.495572,6.499628,4.115111],[-9.952924,6.290634,-5.200359,-0.845527,2.292094,7.240369],[-8.732343,-9.142991,3.750898,3.090599,4.155955,1.398844],[7.295073,3.987534,0.842042,-6.676755,-3.835648,8.709232],[-2.207443,9.645707,-0.209829,-1.602996,-6.237678,-6.106084],[-2.203313,-9.870290,9.834695,-0.552227,6.220346,8.454554],[-8.610023,-2.201876,6.952453,-5.920129,-6.485202,7.279494]],[[-5.435036,1.995467,0.084094,-7.741695,-4.594116,9.992762],[-0.963721,-8.516766,8.725586,-9.745602,3.770976,-7.511328],[0.894239,8.265954,-0.284081,-8.485812,-8.261581,-6.627675],[2.665355,5.218450,1.880948,3.779893,-2.733475,1.804074],[3.310639,-4.484572,-0.256656,8.823230,8.437024,7.926611],[-4.270009,-6.119944,-8.858886,-5.989768,7.034187,6.892598],[-4.571286,-2.838855,-7.559653,5.329673,-9.557550,1.459462],[-6.811800,-3.264505,2.842867,-3.259840,4.185253,-1.246974],[4.877934,7.964841,-5.972868,0.586035,0.130198,8.738019],[9.930853,4.097190,-0.424808,-8.296969,5.030670,-6.696766],[3.916993,-1.399979,3.337077,-6.392678,1.385237,1.260214]],[[-3.410399,7.110994,6.770550,2.010395,9.220830,-0.858380],[8.082978,-3.316944,1.908427,5.846685,4.605142,1.992831],[-8.483194,0.940249,9.148914,6.959687,3.451282,6.453778],[-0.851927,6.084378,5.106968,9.131668,9.173854,8.573737],[1.440004,2.857784,0.575406,6.412149,-5.571880,8.063182],[-2.747078,1.483197,6.042224,-4.372793,6.600880,9.084004],[9.261376,-3.705340,8.083393,8.537172,-6.753887,0.656807],[4.649413,-2.209254,-3.103066,8.432109,-5.545463,-9.594171],[0.165533,1.547138,6.342643,8.813605,-0.447798,4.414851],[4.606519,-0.111582,4.105277,7.745236,-0.184699,-0.591600],[-1.456823,4.716356,-7.832739,-2.146206,-2.979838,-0.004809]],[[8.920831,-2.720835,2.891711,0.251729,-6.227906,3.402608],[0.319558,-1.939738,-8.978675,-1.141342,-7.773667,6.184287],[-6.064839,-7.503990,-3.070529,-6.202613,-6.346794,1.796379],[-6.922024,5.608559,-2.097017,-0.791764,9.980315,2.705339],[6.709083,-6.992317,-9.705558,-2.861534,-2.714981,0.194651],[4.226085,-5.349807,9.390656,-6.049555,-1.243178,-2.120055],[-4.447763,-7.829179,-4.902506,9.239951,-6.167193,1.832656],[1.868101,3.815482,0.008793,-2.106264,-8.908869,-0.195928],[-8.407913,7.343390,-5.404630,3.880544,-9.461097,4.871750],[-8.479229,-4.705073,-0.356241,6.022006,6.072175,3.536256],[6.737884,9.421465,-7.098222,3.252875,-9.619343,0.345350]],[[0.730099,6.173313,3.711673,-5.272015,2.071672,-2.110035],[-7.884819,-4.240440,-8.710814,-0.546239,4.258400,7.715809],[-1.572526,0.658287,0.073783,7.118719,5.306082,-6.643984],[7.517086,-6.147816,6.286449,7.560674,-0.944064,3.861698],[0.799965,1.072321,7.729422,8.426555,9.314269,2.492450],[5.953945,0.121121,3.298015,5.787200,-7.369239,-6.239680],[-6.579230,-5.030217,6.646838,5.357552,2.186692,5.614273],[9.791566,-3.859790,5.841501,3.417911,7.439694,-7.951848],[-2.667511,1.830474,6.632108,-2.727917,5.153779,3.472389],[-2.735264,-2.937512,6.555490,7.989186,-7.515572,0.048076],[6.532058,-4.629886,-3.665213,6.977388,9.178480,5.427668]],[[-2.681909,-1.837093,-0.715168,-6.461525,1.159317,9.359005],[7.195111,6.418456,-4.360661,1.000189,-9.624349,-3.220096],[-9.100328,6.697058,9.349595,1.709395,9.809859,3.925611],[0.764420,-2.127629,-4.644924,6.620172,-1.282126,7.989870],[2.933454,-0.138608,6.153340,-9.652395,2.000409,3.278276],[6.622375,-0.724639,-4.198674,-5.762910,-4.589693,-8.628371],[-5.255991,-9.351878,9.679294,-1.761469,-5.713345,-8.356451],[1.793065,-0.827701,-3.451259,2.038602,-9.341466,-8.950470],[-1.434892,-1.910918,-8.675989,1.006494,-0.847772,5.420495],[-6.021193,-2.697830,5.499914,-1.281040,-2.636429,4.108064],[-6.792295,-2.174290,-5.009797,5.979366,3.194671,1.530814]],[[0.208560,3.138908,-1.765416,1.519572,-4.088967,-0.932705],[-9.844939,-2.583305,8.101831,7.253567,5.926110,-2.116451],[1.293350,-8.071167,6.612686,-3.557844,-5.345459,-6.115450],[-2.315346,6.747880,4.968530,-6.297411,-0.304952,-4.216922],[-5.019434,7.887750,8.156726,-0.400259,-9.287506,-2.409200],[-3.191884,-8.436256,-0.660866,-8.549515,-7.687811,5.661222],[5.781039,6.738868,-3.496265,6.088368,9.482573,-8.288010],[-4.464622,1.240477,4.089504,-8.459133,-7.998931,8.892880],[2.036452,-2.088114,0.110240,3.079567,0.102589,0.313749],[9.350142,3.790722,6.470904,5.183409,-0.937301,-9.002720],[-6.671089,1.072711,3.698044,5.843872,-5.789530,-6.847611]],[[7.951382,-4.785783,-2.476700,1.997266,-7.636371,1.978544],[-6.840635,9.220976,6.751146,5.029792,-5.471647,0.919137],[6.637448,-6.288147,-3.120510,9.788639,4.389163,-8.639777],[3.046690,1.116485,-1.671608,-4.390358,3.376533,7.653434],[4.203299,5.145977,-7.308159,-9.708485,8.293049,9.742173],[3.922324,-5.059692,8.425635,9.218275,-0.259389,-6.798572],[1.860526,6.220124,3.842624,1.806214,2.172537,-7.802172],[2.994931,3.592778,-2.255535,-3.790462,-5.820370,-0.298181],[-5.838647,-1.885395,-0.347157,7.219981,0.739133,-3.891471],[-2.788604,-0.959687,-0.694431,6.154660,2.402202,8.116887],[3.109555,3.827789,-9.992365,1.139698,5.454786,9.497040]]], dtype = "float64")#candidate|4194|(15, 11, 6)|const|float64
bop_4195 = relay.mod(call_4191.astype('float64'), relay.reshape(const_4194.astype('float64'), relay.shape_of(call_4191))) # shape=(15, 11, 6)
bop_4198 = relay.mod(call_4192.astype('float64'), relay.reshape(const_4194.astype('float64'), relay.shape_of(call_4192))) # shape=(15, 11, 6)
output = bop_4195
output2 = bop_4198
func_4221 = relay.Function([], output)
mod['func_4221'] = func_4221
mod = relay.transform.InferType()(mod)
output = func_4221()
func_4222 = relay.Function([], output)
mutated_mod['func_4222'] = func_4222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2873_call = mod.get_global_var('func_2873')
func_2874_call = mutated_mod.get_global_var('func_2874')
call_4226 = relay.TupleGetItem(func_2873_call(), 0)
call_4227 = relay.TupleGetItem(func_2874_call(), 0)
func_2165_call = mod.get_global_var('func_2165')
func_2167_call = mutated_mod.get_global_var('func_2167')
const_4274 = relay.const([-4.130360,-4.781181,6.066965,-0.540712,-4.278313,7.398495,-1.287159,-8.975890,1.820044,-9.176145,-4.612731,-9.461573,1.092068,8.928599,1.904803], dtype = "float32")#candidate|4274|(15,)|const|float32
call_4273 = func_2165_call(relay.reshape(const_4274.astype('float32'), [3, 5, 1]))
call_4275 = func_2165_call(relay.reshape(const_4274.astype('float32'), [3, 5, 1]))
output = relay.Tuple([call_4226,call_4273,const_4274,])
output2 = relay.Tuple([call_4227,call_4275,const_4274,])
func_4276 = relay.Function([], output)
mod['func_4276'] = func_4276
mod = relay.transform.InferType()(mod)
mutated_mod['func_4276'] = func_4276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4276_call = mutated_mod.get_global_var('func_4276')
call_4277 = func_4276_call()
output = call_4277
func_4278 = relay.Function([], output)
mutated_mod['func_4278'] = func_4278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2692_call = mod.get_global_var('func_2692')
func_2694_call = mutated_mod.get_global_var('func_2694')
call_4340 = relay.TupleGetItem(func_2692_call(), 0)
call_4341 = relay.TupleGetItem(func_2694_call(), 0)
output = relay.Tuple([call_4340,])
output2 = relay.Tuple([call_4341,])
func_4344 = relay.Function([], output)
mod['func_4344'] = func_4344
mod = relay.transform.InferType()(mod)
mutated_mod['func_4344'] = func_4344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4344_call = mutated_mod.get_global_var('func_4344')
call_4345 = func_4344_call()
output = call_4345
func_4346 = relay.Function([], output)
mutated_mod['func_4346'] = func_4346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2692_call = mod.get_global_var('func_2692')
func_2694_call = mutated_mod.get_global_var('func_2694')
call_4374 = relay.TupleGetItem(func_2692_call(), 0)
call_4375 = relay.TupleGetItem(func_2694_call(), 0)
output = relay.Tuple([call_4374,])
output2 = relay.Tuple([call_4375,])
func_4376 = relay.Function([], output)
mod['func_4376'] = func_4376
mod = relay.transform.InferType()(mod)
output = func_4376()
func_4377 = relay.Function([], output)
mutated_mod['func_4377'] = func_4377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3330_call = mod.get_global_var('func_3330')
func_3331_call = mutated_mod.get_global_var('func_3331')
call_4407 = relay.TupleGetItem(func_3330_call(), 0)
call_4408 = relay.TupleGetItem(func_3331_call(), 0)
output = call_4407
output2 = call_4408
func_4417 = relay.Function([], output)
mod['func_4417'] = func_4417
mod = relay.transform.InferType()(mod)
output = func_4417()
func_4418 = relay.Function([], output)
mutated_mod['func_4418'] = func_4418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3636_call = mod.get_global_var('func_3636')
func_3638_call = mutated_mod.get_global_var('func_3638')
call_4441 = relay.TupleGetItem(func_3636_call(), 0)
call_4442 = relay.TupleGetItem(func_3638_call(), 0)
output = call_4441
output2 = call_4442
func_4446 = relay.Function([], output)
mod['func_4446'] = func_4446
mod = relay.transform.InferType()(mod)
mutated_mod['func_4446'] = func_4446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mutated_mod.get_global_var('func_4446')
call_4447 = func_4446_call()
output = call_4447
func_4448 = relay.Function([], output)
mutated_mod['func_4448'] = func_4448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3964_call = mod.get_global_var('func_3964')
func_3966_call = mutated_mod.get_global_var('func_3966')
call_4461 = relay.TupleGetItem(func_3964_call(), 0)
call_4462 = relay.TupleGetItem(func_3966_call(), 0)
const_4465 = relay.const([[[3.532721,-1.964631,-5.063894,7.937918,-1.258955,0.286123],[-2.561230,-9.562996,2.156546,-4.913710,0.067223,-2.985160],[1.475858,-8.768150,-5.695166,-9.442136,0.496648,-0.010632],[3.183980,-4.894746,-4.956914,-8.121759,3.062365,-0.765095],[3.421603,8.816141,8.262798,-5.150295,6.479733,3.344422],[-3.549477,-1.978226,-9.734397,-5.325765,-2.480724,6.114322],[-5.949341,7.198033,-6.063148,-6.058962,-1.842226,-1.758588],[7.641505,-6.306711,7.414676,4.784370,-2.369154,-7.269744],[-5.775256,-0.039419,2.780115,7.290951,7.741941,6.898999],[-7.946759,2.290702,-0.666993,8.718342,5.889502,-3.551373],[3.802138,-2.608719,4.861114,-1.212931,4.738937,7.258225]],[[-1.994457,5.357674,8.527131,-5.214597,-2.327458,1.304718],[5.763032,9.376631,-8.332107,-2.849959,0.913224,3.864127],[4.690695,-1.135447,-4.711031,7.990250,-0.713657,-5.075960],[-0.308503,-2.854675,6.108634,9.846070,-4.953158,5.839947],[-0.488699,-0.917615,-6.190297,2.941346,9.572390,8.869144],[1.386044,-0.928976,5.044189,9.085461,6.499987,-3.233908],[8.556962,-1.265695,-2.125144,0.789444,6.792910,-4.248333],[5.962797,1.994410,6.635082,2.738328,6.218877,8.943429],[-0.227411,-3.612396,-8.186051,-0.407325,-4.233675,6.046628],[-6.070972,-5.451934,-1.679956,-1.109913,-4.364387,-7.399015],[-8.091529,-5.350192,7.170888,-1.405654,-1.375078,-4.938188]],[[8.397950,1.852767,9.976704,4.272899,0.718797,3.402868],[-7.271037,7.489253,0.145363,2.623950,8.312886,8.618424],[7.333389,0.734617,9.774279,-7.714191,-1.746992,-5.121985],[-2.682713,-9.595412,0.071341,1.445781,6.959228,-8.551171],[-4.546819,-3.859715,9.937377,-4.954273,3.786810,5.025159],[9.516979,4.707669,5.267741,4.727083,7.513865,1.786134],[1.738622,1.071772,2.495253,7.761511,5.084916,-9.045276],[-7.651713,2.851503,-9.134463,-8.627701,-7.963611,9.155236],[3.134715,8.430000,-4.311491,-8.186532,0.524358,-4.006619],[4.335919,-0.736656,4.035232,-6.697049,2.755696,9.937980],[-2.588187,-1.879892,-5.711552,-8.126875,-3.297422,-1.376757]],[[-5.086211,4.211801,-4.292758,-2.939042,7.908736,-1.089989],[2.775275,-9.223502,-9.965355,-7.305572,0.959943,0.139934],[1.355829,-0.621182,6.861835,-0.991046,9.843401,8.439109],[-3.833949,6.968069,-0.844939,-2.696076,-7.189251,8.589195],[5.927212,8.859019,-8.990493,-5.108028,-4.143833,5.908121],[7.502761,1.747305,3.858087,9.656776,4.588487,-3.205594],[-6.563231,2.149085,6.925311,-7.450924,6.223621,-0.771325],[-9.131284,3.436668,4.368271,8.818570,-4.137580,1.342831],[5.875620,9.444391,6.537362,2.401383,0.455736,5.257525],[7.578065,9.414887,7.073990,-4.641788,-9.286338,6.782607],[-6.538175,-3.451261,4.487025,5.196712,-4.773591,5.412344]],[[-7.048116,-1.699502,-3.065095,-1.966820,7.380044,-4.856210],[1.845089,-6.223260,-6.343128,6.815885,-1.507708,6.580817],[5.070689,2.587022,-8.724941,-7.171303,2.102715,-6.947637],[-0.676603,3.050508,-0.366106,-1.160297,-5.082347,6.311545],[-9.655228,8.674845,-3.670145,7.869206,1.203775,-7.696000],[1.763077,-6.270846,4.164782,-2.503914,-1.197217,1.271384],[0.887505,-7.389147,-2.829618,-9.897199,4.940418,-2.072460],[9.582365,6.629158,-1.877994,-3.833409,-6.915726,-0.872469],[3.196019,9.566616,-6.057900,-0.599726,7.128697,9.940309],[-4.346542,-7.223616,0.661874,7.584517,-1.412308,-0.873290],[-5.521168,8.177767,5.766755,-0.526243,-0.310983,-9.556505]],[[-6.525547,0.601345,-1.165485,-8.381101,-2.303461,-9.687805],[3.884917,-8.249245,-5.448469,-5.542878,5.320472,-4.616613],[6.314432,7.665677,-3.815996,-3.885336,-5.059807,-8.745283],[-7.927189,2.761736,-8.013295,-6.381975,-1.301872,2.269568],[8.518586,4.662182,2.339721,-9.680127,8.222491,1.779676],[1.118177,-3.817007,1.271287,-6.988569,3.824611,-3.412088],[5.379396,5.262117,-9.149535,8.201392,-4.890071,-1.254878],[-7.760673,-5.492867,7.081368,5.140841,1.507582,-8.509636],[8.056152,-7.116103,1.223379,-9.243792,-5.157424,-6.755613],[-2.973912,-1.968982,-5.696521,8.146517,5.997963,-1.871367],[7.920235,-0.320681,-7.834005,3.809774,3.412122,-3.541875]],[[-9.442412,-1.092801,4.094664,0.749417,-4.032631,-9.706061],[8.599306,2.809427,-8.549461,8.881584,2.005736,-8.519911],[-1.881834,3.210312,-7.260084,-5.682721,-6.498140,9.190439],[0.516004,-6.929633,-9.347452,7.925833,-7.136715,3.955182],[-5.952775,-0.520170,-4.759401,7.785368,-6.731318,-9.704711],[5.929029,8.504086,7.085428,6.453296,-5.414674,-3.809118],[-7.793500,-5.849133,-5.483277,3.677295,-0.468608,8.708209],[7.648513,3.447438,6.067911,-5.987280,7.805721,8.191534],[-3.427994,1.643175,-0.984742,4.620720,4.382221,1.972531],[9.273391,0.807789,-4.156925,-4.191688,1.159967,5.963471],[-7.057807,7.080105,2.056160,-8.666945,9.664953,-7.126845]],[[-9.923004,9.888057,8.831906,0.661504,6.516563,-8.529503],[3.747958,4.297270,5.339910,-0.583560,-1.285314,3.263335],[-4.073571,4.578539,4.368768,2.499977,-3.646810,-8.060867],[7.389490,-9.930005,-6.636717,-6.881253,-6.244969,-6.860907],[-7.245909,2.093133,5.006383,-9.763960,-5.700802,1.526238],[-6.901578,5.423206,1.695488,-7.113958,-7.139384,-3.625468],[-8.331543,-9.579128,-9.486078,-5.428829,9.714575,-2.400250],[-2.936476,-8.464612,-4.664551,-2.908533,-9.341920,3.482475],[1.761400,-0.193112,3.654019,-5.851968,7.606920,-7.678547],[-6.922108,-5.089625,-6.934882,-9.168223,-5.234196,3.661505],[-1.399953,8.145783,-8.142330,2.901301,-5.347064,4.362466]],[[-7.969778,6.276928,-0.309405,7.941115,-6.175275,6.405765],[-5.150562,0.702652,-5.448525,-0.206849,5.216015,-8.032919],[-9.791852,4.526685,8.071779,-7.324987,0.616266,-6.479761],[3.482145,-8.259421,6.113713,-6.879665,5.294361,-3.769449],[3.292613,-8.676130,-4.182416,-4.450319,-9.479147,-8.908982],[-5.990629,2.358133,-2.111727,0.612920,-4.371955,-8.465635],[6.448177,3.231819,-5.730527,1.621079,-6.932970,-6.856464],[-4.258925,-7.680328,2.842106,-1.073278,6.011448,9.036623],[3.113062,-0.643520,-1.029479,-5.131124,8.093394,-0.600284],[7.690963,9.542498,3.643794,9.343788,-2.690793,2.660966],[-4.364677,9.434397,0.214899,1.036489,-4.239437,-3.039923]],[[-1.076195,-0.619762,0.623138,-3.175411,-2.846872,-6.915055],[3.372720,2.429891,1.629706,1.069909,0.723740,-7.279354],[7.158749,5.698197,7.675777,-9.053708,-5.977194,5.823641],[8.990132,3.243581,-7.859454,-2.918924,0.469547,6.657414],[-4.576128,-5.966427,-4.722128,-9.670439,-7.883304,2.890714],[-7.137390,-2.811204,-8.535149,-1.510097,2.540051,-0.810022],[4.422468,0.228794,-3.819735,-0.750930,-7.731885,-8.925917],[8.157107,-0.561782,3.002231,1.473911,-7.248578,-4.458073],[9.092567,-7.008598,-0.048145,-5.420757,4.321202,-3.053541],[9.939405,-2.075257,5.943942,-7.185232,-8.035398,9.406309],[-8.107393,9.615817,-2.095784,7.468105,-0.192183,-4.455046]],[[-3.078903,-0.732059,-7.041607,-2.410552,3.929636,7.316620],[8.728368,1.592481,0.385637,5.901265,0.212658,-5.569204],[9.708203,-2.255883,3.329913,-2.516131,5.182709,-6.577065],[-8.988201,1.060526,4.114744,-3.490327,-9.442046,-9.404154],[-0.326727,3.826647,-8.490301,2.916400,-2.644652,8.586506],[-4.820646,8.736419,7.217106,-2.593045,-6.591139,6.771659],[-6.143692,7.906300,-5.929156,-2.552074,9.093742,-6.263744],[1.808744,6.691694,7.079573,-2.339385,9.214336,-4.030345],[2.883096,-1.158659,-7.548795,4.717760,9.633297,-5.127262],[6.783633,8.801544,-4.520401,-3.838841,8.769387,9.549929],[2.892788,4.272528,-6.304806,5.390151,-9.541852,8.160934]],[[7.854269,4.303077,0.372594,-3.280832,9.014054,-6.383882],[-2.871304,5.421103,-1.498121,-6.697746,-2.929988,-8.089173],[3.585128,-4.203462,7.212551,6.051359,8.988306,-5.745691],[-8.473611,8.358344,-9.579961,7.191620,-0.430829,-1.243134],[-4.863089,-3.936850,-4.843004,3.302806,-6.000782,3.302235],[3.741674,1.641613,-9.417973,-9.882699,-8.141034,-0.249599],[6.654282,4.288043,-7.465222,-9.694211,1.550502,-7.589481],[-5.549464,8.619715,2.966084,-5.344257,6.523472,2.058492],[5.804670,-9.749648,8.287970,-7.077919,6.395445,8.856918],[-1.812866,-3.124070,-9.401484,8.306522,-5.570328,-1.017779],[-7.562062,-5.493209,-2.423691,6.813100,1.090881,5.799819]],[[-4.765045,3.656625,-5.883886,9.552693,8.182739,-6.160132],[-5.153111,-3.224793,-4.656251,5.262378,4.902328,8.511734],[5.890308,-9.217780,-7.222501,-6.073228,4.588225,-6.921981],[-6.241838,-2.008704,3.634647,8.416809,1.997133,-6.046436],[-3.356807,-6.033030,-7.540856,6.934926,-8.599206,-0.912185],[-6.190402,1.212214,7.738915,2.221146,9.616512,9.350645],[-9.621278,8.612317,-8.285326,8.342380,1.528227,-0.642106],[9.172473,3.766727,4.280113,4.201238,-3.908737,-9.314985],[-4.058481,3.465209,5.160924,3.188008,-7.642146,4.367158],[-9.799825,3.536496,-1.343297,7.247345,-3.304793,9.841104],[2.369788,2.259359,0.436325,8.625209,8.450471,-9.140270]],[[0.754568,-4.884081,-5.547989,-8.693929,-9.071808,-2.304841],[2.011755,3.884856,-8.734535,-1.911821,4.558827,-5.054168],[3.083876,-1.744862,-5.402490,3.581654,-7.194636,5.868929],[-7.276235,-7.187996,-4.564960,7.195217,-8.314024,4.251284],[-2.721552,-6.654328,1.107885,-6.621563,-5.086224,4.050437],[9.686370,-6.981086,-9.908681,-1.384325,8.265343,1.964142],[7.499753,-3.342706,8.123377,7.637437,0.211310,4.191825],[-4.386831,8.315836,5.237790,9.727322,0.436515,-5.519171],[-0.658757,-2.827019,1.294793,1.173976,0.466084,8.459688],[9.650634,-3.027290,-8.399447,5.999858,5.907804,-1.121069],[7.554723,-0.651820,9.039709,-4.559457,9.267671,-5.148540]],[[-4.242820,-6.568684,1.289895,1.156671,-2.024638,8.693596],[7.946092,8.519292,7.313645,1.139414,4.066595,2.050098],[9.559285,-0.108244,0.124847,5.218561,-9.091351,8.971591],[4.098290,-8.169046,-4.576151,3.274724,-6.292136,-2.087462],[-6.675514,-5.119022,4.195980,-0.946418,9.355193,-5.172583],[4.481875,0.676226,1.100451,8.550274,0.120788,-1.255003],[8.563964,7.738332,-5.556161,0.882489,-7.163013,-2.068309],[-0.751681,-2.105703,-1.999425,-9.394774,-1.489472,8.246971],[-2.519634,0.303011,2.018364,3.008363,6.116078,-8.670696],[-0.097127,-9.596994,-0.951620,1.164138,2.688202,-1.108817],[-7.953795,-9.068095,-2.861374,-9.651845,-3.646895,-7.752570]]], dtype = "float64")#candidate|4465|(15, 11, 6)|const|float64
bop_4466 = relay.maximum(call_4461.astype('int32'), relay.reshape(const_4465.astype('int32'), relay.shape_of(call_4461))) # shape=(15, 11, 6)
bop_4469 = relay.maximum(call_4462.astype('int32'), relay.reshape(const_4465.astype('int32'), relay.shape_of(call_4462))) # shape=(15, 11, 6)
output = bop_4466
output2 = bop_4469
func_4484 = relay.Function([], output)
mod['func_4484'] = func_4484
mod = relay.transform.InferType()(mod)
mutated_mod['func_4484'] = func_4484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4484_call = mutated_mod.get_global_var('func_4484')
call_4485 = func_4484_call()
output = call_4485
func_4486 = relay.Function([], output)
mutated_mod['func_4486'] = func_4486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2990_call = mod.get_global_var('func_2990')
func_2992_call = mutated_mod.get_global_var('func_2992')
call_4500 = func_2990_call()
call_4501 = func_2990_call()
output = relay.Tuple([call_4500,])
output2 = relay.Tuple([call_4501,])
func_4503 = relay.Function([], output)
mod['func_4503'] = func_4503
mod = relay.transform.InferType()(mod)
mutated_mod['func_4503'] = func_4503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4503_call = mutated_mod.get_global_var('func_4503')
call_4504 = func_4503_call()
output = call_4504
func_4505 = relay.Function([], output)
mutated_mod['func_4505'] = func_4505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4417_call = mod.get_global_var('func_4417')
func_4418_call = mutated_mod.get_global_var('func_4418')
call_4535 = func_4417_call()
call_4536 = func_4417_call()
const_4547 = relay.const([[[8,-4,-6,7,6,-3],[1,1,-9,-10,3,-6],[-7,-9,-10,10,3,-2],[-4,-10,-7,3,10,9],[-10,4,6,2,-4,6],[10,-2,1,-1,-3,7],[5,7,6,7,-7,-7],[2,6,2,2,9,4],[-5,5,9,-9,4,2],[-2,-5,-1,-1,4,10],[1,-10,3,-10,-3,8]],[[9,-6,1,-2,-8,-1],[-1,-3,10,-3,-3,-1],[10,-7,-8,-5,-2,9],[-1,-6,10,-10,-10,6],[-6,2,3,-8,-7,-8],[-9,4,-5,5,-6,5],[-8,6,7,9,2,-3],[-9,10,5,2,8,-5],[1,-9,1,-4,8,-7],[4,8,-1,1,-3,5],[8,4,-5,10,-1,4]],[[2,10,-10,7,-5,1],[8,-6,-4,1,-10,7],[7,5,6,-9,9,-8],[-6,-4,2,7,-7,10],[-3,1,-9,-3,6,4],[7,-10,-3,-5,5,-4],[-3,6,-3,1,-1,-3],[3,-5,-2,-10,-2,-3],[-3,6,8,-7,-10,-2],[1,-2,6,-1,9,-7],[-6,-10,-9,3,-3,-10]],[[-8,1,9,-4,-7,-3],[10,-9,1,-10,4,5],[-2,5,-7,6,1,-7],[1,3,6,10,-1,4],[4,10,3,1,-4,-3],[-1,-8,8,-7,5,-8],[7,6,6,3,-4,-8],[-8,6,-5,-3,-8,3],[4,-7,-1,9,-3,-7],[5,-9,-2,-5,7,-2],[-10,1,4,6,-7,7]],[[9,7,3,1,5,-4],[-8,-7,2,-9,4,2],[7,6,-2,1,10,-3],[1,10,5,-5,5,-10],[-3,9,1,5,-1,2],[-3,5,9,8,-4,-10],[-2,-6,8,4,-6,-9],[6,7,-3,9,9,3],[3,-2,10,10,6,1],[-3,-3,9,8,-6,-3],[3,6,7,2,1,-9]],[[-5,-4,-6,-2,1,-9],[-9,-6,-3,3,10,-10],[1,6,-7,4,5,-2],[7,1,-3,-8,7,-7],[-10,6,4,-6,-9,8],[9,-7,-3,7,-5,6],[9,10,8,8,-2,10],[2,10,10,5,-9,8],[-1,2,5,4,3,-2],[3,-1,-4,-10,8,-8],[-7,2,7,-10,4,6]],[[7,5,-6,-1,5,-6],[2,9,-8,-10,2,-3],[-1,1,2,-7,9,-10],[-9,6,4,4,1,-8],[2,6,-2,-5,3,-2],[-5,-7,-1,9,-10,5],[-8,2,2,-8,1,-10],[-4,-8,3,3,9,10],[7,-1,4,-2,4,-4],[5,-3,-8,7,-8,-1],[5,6,-4,-3,8,1]],[[-9,-6,7,9,4,6],[3,-3,10,-1,-10,8],[-5,-6,-4,-7,-9,6],[-5,-6,7,8,-7,2],[-7,-2,-9,-10,1,9],[2,-10,9,7,-3,2],[8,9,-2,-3,-3,3],[-5,-8,10,6,3,5],[4,-5,-8,6,-6,-1],[5,7,-1,1,5,6],[7,7,8,2,-5,-6]],[[6,9,6,-10,6,-10],[-10,-2,-10,-10,10,9],[-1,-7,-9,-9,6,9],[-10,4,8,10,5,-3],[-2,-4,-10,10,3,8],[-2,-9,7,-8,-6,-2],[6,-2,-7,8,8,4],[4,-7,-1,10,-4,-10],[6,-1,-2,-1,-6,-3],[-8,6,4,3,-4,-6],[-7,-8,7,3,8,10]],[[-6,2,3,-9,-6,-8],[3,-8,-2,-1,5,10],[-7,-9,-9,-7,-9,-1],[4,-5,2,-1,-5,-3],[-5,5,-2,-4,-10,-6],[-2,-5,1,3,-3,4],[-4,-2,3,-7,10,10],[9,-2,5,-9,8,7],[-10,-3,-1,-10,-3,7],[8,6,-7,1,-8,-6],[-9,-9,-9,-8,-7,1]],[[9,4,-6,8,6,-3],[10,-9,-6,-3,-8,-4],[7,5,3,3,-9,-6],[9,-10,-7,7,6,-8],[-1,-7,-1,7,5,3],[9,-1,-4,-3,10,9],[-6,-5,-4,-5,3,-5],[5,4,5,-7,5,3],[5,-2,9,10,-10,6],[-9,-9,4,-7,-6,-6],[-10,5,1,3,-2,-10]],[[-8,6,7,-2,-4,-1],[4,5,8,-1,6,-4],[-2,2,-3,6,-3,9],[-4,-8,-1,5,6,-5],[3,5,-2,6,-5,9],[-1,9,-7,5,9,-10],[-4,-4,-6,9,7,-9],[-2,-4,-3,6,9,-9],[-4,-8,2,3,-4,6],[-8,-1,10,3,-7,10],[-1,6,-10,6,3,-6]],[[3,-9,-8,9,2,10],[-2,-4,1,8,10,2],[1,5,6,-9,5,-8],[-4,9,-8,10,2,-8],[-9,5,-2,-1,-8,7],[2,-3,-3,-7,7,-5],[-5,-7,-8,-1,1,6],[4,-6,-6,4,-8,-4],[-7,10,-9,3,7,-2],[-2,1,9,-7,-7,-3],[6,2,6,9,-8,-9]],[[3,2,9,6,-7,7],[6,-8,4,7,-3,-8],[-4,-2,3,9,5,-7],[-7,8,-9,1,8,10],[5,4,6,-4,-6,-3],[10,-6,-5,-9,-3,6],[1,-1,7,1,-1,-7],[-6,9,9,-2,6,-2],[-10,-3,10,-8,7,10],[-3,7,5,-2,6,4],[5,-4,5,-4,-9,-9]],[[-8,-9,-6,-8,-9,2],[-8,-6,6,-2,7,4],[4,-8,-4,-1,4,7],[9,1,-10,-2,7,-5],[-10,-6,2,1,-7,-8],[-6,3,-1,3,8,9],[-7,8,-1,-9,-1,7],[6,-1,7,-5,-10,-4],[-1,-2,1,6,-4,-3],[9,-5,-8,6,-8,-8],[6,-9,-2,-7,2,-1]]], dtype = "int8")#candidate|4547|(15, 11, 6)|const|int8
bop_4548 = relay.greater_equal(call_4535.astype('bool'), relay.reshape(const_4547.astype('bool'), relay.shape_of(call_4535))) # shape=(15, 11, 6)
bop_4551 = relay.greater_equal(call_4536.astype('bool'), relay.reshape(const_4547.astype('bool'), relay.shape_of(call_4536))) # shape=(15, 11, 6)
func_991_call = mod.get_global_var('func_991')
func_994_call = mutated_mod.get_global_var('func_994')
var_4562 = relay.var("var_4562", dtype = "float32", shape = (12,))#candidate|4562|(12,)|var|float32
const_4563 = relay.const([-1.508513,0.255576,7.610042,-3.093779,-7.351384,-1.966491,-6.880223,7.996005,5.641389,-4.589215,9.442739,2.115243,-9.413470,-7.794864,-1.804128,-3.118159,2.997350,7.176021,-0.217477,7.573269,-7.718855,-6.249944,5.326768,-6.383060,-9.283964,7.841653,-2.286032,5.508379,0.840947,-4.145968,-3.374515,-1.712188,-5.055193,6.583843,-8.295293,5.598821,-0.492245,6.486468,6.236086,-6.300683,-0.464763,8.222106,-5.762912,8.406372,4.386138,7.309019,5.753615,3.441252,-6.062995,-5.878700,-5.127987,2.078099,-6.688743,-7.365149,-9.481128,3.391551,-3.077127,5.923578,9.448450,-8.905268,-5.672290,7.562591,2.134669,2.883669,8.751520,-3.062590,0.518736,-2.579979,-5.329485,-5.228090,5.743958,-5.808241,-0.329211,5.369743,-7.736850,-0.816998,7.320529,-1.714616,0.167197,-6.876090,-0.946851,-0.510887,-4.031908,5.998385,2.235158,-9.897687,9.795583,-8.271918,-4.660452,2.528050,8.558554,-0.809189,8.603574,6.347097,-7.069889,2.561259,8.238619,0.996111,-2.584060,-9.553719,-5.773390,8.893425,7.798690,8.983930,5.380559,0.201150,9.821348,5.594653,-5.840108,3.124338,1.082819,9.212570,-3.407511,-3.774066,1.094436,-5.137674,0.752146,8.104301,1.861183,8.951340,-9.649535,7.706952,-7.636121,-2.013279,4.939560,6.015484,1.398372,2.888294,3.068448,-9.528357,6.116883,-3.438974,-2.743953,0.577520,8.625476,-5.251672,6.382058,5.174180,8.301290,0.827643,7.067353,3.286437,3.024602,-4.078647,-0.958964,-4.122532,3.461673,2.879899,-4.105617,3.453874,3.470790,5.113609,0.995656,-8.359343,4.120634,0.945449], dtype = "float32")#candidate|4563|(156,)|const|float32
call_4561 = relay.TupleGetItem(func_991_call(relay.reshape(var_4562.astype('float32'), [6, 2, 1]), relay.reshape(const_4563.astype('float32'), [6, 2, 13]), ), 1)
call_4564 = relay.TupleGetItem(func_994_call(relay.reshape(var_4562.astype('float32'), [6, 2, 1]), relay.reshape(const_4563.astype('float32'), [6, 2, 13]), ), 1)
output = relay.Tuple([bop_4548,call_4561,var_4562,const_4563,])
output2 = relay.Tuple([bop_4551,call_4564,var_4562,const_4563,])
func_4567 = relay.Function([var_4562,], output)
mod['func_4567'] = func_4567
mod = relay.transform.InferType()(mod)
var_4568 = relay.var("var_4568", dtype = "float32", shape = (12,))#candidate|4568|(12,)|var|float32
output = func_4567(var_4568)
func_4569 = relay.Function([var_4568], output)
mutated_mod['func_4569'] = func_4569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_4600 = relay.TupleGetItem(func_4503_call(), 0)
call_4601 = relay.TupleGetItem(func_4505_call(), 0)
output = relay.Tuple([call_4600,])
output2 = relay.Tuple([call_4601,])
func_4614 = relay.Function([], output)
mod['func_4614'] = func_4614
mod = relay.transform.InferType()(mod)
output = func_4614()
func_4615 = relay.Function([], output)
mutated_mod['func_4615'] = func_4615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2645_call = mod.get_global_var('func_2645')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_4645 = func_2645_call()
call_4646 = func_2645_call()
func_2692_call = mod.get_global_var('func_2692')
func_2694_call = mutated_mod.get_global_var('func_2694')
call_4655 = relay.TupleGetItem(func_2692_call(), 0)
call_4656 = relay.TupleGetItem(func_2694_call(), 0)
func_3358_call = mod.get_global_var('func_3358')
func_3361_call = mutated_mod.get_global_var('func_3361')
var_4674 = relay.var("var_4674", dtype = "float64", shape = (18, 36))#candidate|4674|(18, 36)|var|float64
call_4673 = relay.TupleGetItem(func_3358_call(relay.reshape(var_4674.astype('float64'), [6, 9, 12]), relay.reshape(call_4645.astype('int8'), [990,]), ), 2)
call_4675 = relay.TupleGetItem(func_3361_call(relay.reshape(var_4674.astype('float64'), [6, 9, 12]), relay.reshape(call_4645.astype('int8'), [990,]), ), 2)
const_4681 = relay.const([[-0.695082,-9.733944,3.605961,-4.470414,6.947272,-7.466064,-7.444378,8.595572,-9.937367,-2.466210,-4.436922,8.597694,9.632523,5.794960,8.267833,5.276721,0.607857,-0.772413,1.391405,-7.127947,-7.157964,2.920068,1.430681,7.570533,-8.576870,8.614153,0.123402,-5.876014,8.009859,-0.160852,-2.667885,-3.584600,0.240153,-0.905420,-9.256307,-3.045999],[5.815383,6.283985,-5.585028,-4.958407,-8.030670,2.542946,6.993685,3.038499,3.244397,8.420587,0.682337,2.821601,-4.958800,1.775681,-4.717578,5.693088,4.721406,-7.527796,-3.510206,-5.834537,4.482497,-8.043746,0.330945,6.758903,2.208900,3.426451,5.308875,-3.077683,-0.477267,-8.433845,7.843351,7.831360,-9.044420,-7.360792,-5.749034,-2.643083],[-4.847660,-4.896652,-5.199051,-7.340721,1.005111,-3.369945,-2.412788,-3.959080,-7.960142,5.545795,3.510561,-2.436025,-8.919943,-3.659534,-0.471501,-6.223992,4.338627,-4.351413,3.325252,1.369968,-1.668192,8.212620,-7.988842,-3.036198,-0.555416,-4.668263,-6.629066,6.924557,3.370493,9.512505,-6.651018,-8.132876,9.236407,2.446965,5.875515,9.806295],[-9.352264,-5.365032,-5.869357,4.747094,-5.893052,-1.955527,1.584018,-4.637663,1.720448,-1.363762,4.172771,6.903579,8.637497,5.194569,-4.210851,1.158253,0.954826,6.275036,-3.103194,-3.380127,5.496872,4.359273,8.447323,0.810876,8.487745,-6.825469,9.684422,0.806539,5.540693,1.319609,2.342212,-3.877048,7.040886,6.293807,9.354547,-2.727013],[-1.190315,0.609720,5.029405,3.635262,-3.930993,-9.728825,4.624307,-1.863154,-2.211305,-3.206304,-2.084567,9.381825,5.123707,1.959711,-4.034725,7.751526,4.874131,-3.505757,5.987579,-2.429791,-1.363455,7.986612,-7.056242,-2.683939,-8.857272,5.956163,2.815332,-6.560722,8.044299,6.770486,6.059297,-6.768140,2.067434,-1.600596,-0.208351,-3.187602],[8.469985,2.050873,-1.607073,-8.076978,-4.122774,7.884351,-0.545794,-6.880822,-8.372056,-7.911630,-9.897769,-7.552236,5.754431,3.017608,6.914896,-2.389723,0.287096,4.748838,0.356685,-6.042927,9.817811,-5.450489,9.740862,7.910535,-9.785017,-3.234909,-0.853472,0.629660,7.075661,-7.562478,-2.230092,9.747084,-4.630608,3.257229,-5.044515,5.442375],[-6.610502,-0.554406,9.880236,3.382906,8.643134,-3.838474,-2.936376,4.986707,-1.793958,4.389560,9.152647,7.109789,5.910052,5.643312,-8.525722,8.449946,-4.187297,2.869700,7.496289,-6.835110,-6.847736,-7.861817,-7.174174,-9.136362,3.745374,2.701071,-1.009831,-8.923470,-0.725207,5.298426,1.632673,3.711571,-1.990658,5.611326,6.874563,-7.340307],[-2.651949,-6.784773,7.710567,-0.023662,-5.839080,4.413714,-3.104424,-6.821861,3.388100,9.669816,-9.764848,0.251766,7.484088,-2.120530,-3.828051,-0.094801,-1.239573,1.539137,5.040463,-0.037930,3.879230,-2.486905,-1.943450,-0.782298,1.668256,-6.080686,-7.760042,-6.636550,-3.550930,-1.616954,-3.058304,5.288927,-8.037622,-7.223368,-3.469774,5.066705],[-7.665417,8.219528,7.293128,-5.576027,-9.087533,-3.094686,-9.146791,-4.439698,-5.915300,5.880548,-9.030398,4.551691,9.060383,-2.705250,-8.227740,-4.791754,-4.663239,1.804611,5.574293,-5.494692,-3.979360,0.528099,6.844473,3.927950,-8.385029,-3.813925,-0.469825,9.757793,1.627306,3.484618,-0.192979,-9.894268,-8.790337,-1.878687,-1.207112,0.238379],[5.992980,0.550277,-5.943509,-8.693145,-1.489208,0.325379,-0.069928,-1.827024,2.595070,-6.909412,5.079144,-3.778683,-2.823386,-7.174736,8.147453,-1.931958,-3.143629,4.530589,-7.958564,2.199241,2.211428,1.353796,-4.631273,0.612074,-9.904657,5.065273,5.750722,9.955316,-2.559245,-8.638930,9.084144,-1.364275,-6.741159,-0.105820,-7.504570,8.029547],[5.270618,7.126746,9.395084,4.034319,-4.579580,4.204486,-4.878508,-2.661237,-6.257642,-2.371197,9.552725,9.493594,-1.961932,-7.654308,-2.836053,-3.098422,6.034524,4.311533,2.942175,-7.238945,9.900492,8.808052,-9.143373,-1.905182,-5.548352,-8.764380,4.281477,2.421766,2.617542,-8.725440,-0.083091,6.194545,3.101520,-0.693760,6.140905,-5.599879],[-3.788391,-4.433343,5.194870,-2.311153,5.504424,3.049092,-4.648629,9.265283,9.571095,3.561808,-1.129746,9.904745,5.155914,-1.133259,-4.770690,7.221949,-4.944757,2.691104,-3.996658,5.758935,-0.204056,2.796612,-9.614523,-9.619065,-3.054475,2.123424,8.218973,-1.650578,-2.194683,0.071516,-9.670283,8.260160,0.307616,-8.639805,-5.089225,4.290641],[2.127222,-0.555651,2.562983,0.828450,-7.391773,3.286889,9.632782,3.028875,-5.424217,-9.207248,9.861672,-6.066362,-6.146866,0.649060,-7.724775,1.929115,6.815094,5.494117,-3.385358,-6.929710,0.316487,-1.273426,-6.288072,-6.967739,4.884035,8.802837,1.769526,7.789548,-1.716687,-2.167626,8.286686,-3.937600,8.483130,-8.389367,-5.609046,7.452741],[-4.806986,-2.519656,9.726460,6.805275,8.375492,9.303008,-5.063322,-5.712572,9.296341,-3.405518,-1.610385,5.825917,-2.712276,-5.995995,6.532138,1.180787,0.952483,-6.574325,-6.931858,6.886759,-6.735541,-0.385156,3.584048,7.695999,-9.110898,-0.548569,8.339164,-7.869011,4.981547,-9.357870,-9.336981,-5.064823,-6.973629,-4.855645,-0.970385,-2.589273],[4.067432,-9.263020,-5.429869,1.401323,0.898444,4.992046,-5.096345,-4.362543,-7.160108,-5.946896,-7.052627,7.090820,2.019581,-8.226489,7.415198,-0.031565,2.155110,-0.067298,-7.665748,-0.769516,3.726998,-2.005789,-3.715101,9.719422,-0.903209,7.911279,-4.807491,6.914516,8.740651,1.347616,-2.783019,4.485868,-1.415794,4.983165,0.209945,-9.431224],[-5.758390,-3.816112,-7.399269,6.041641,7.037957,8.597642,5.995285,9.965710,-4.272183,-8.830065,-9.609711,4.805296,1.000083,-3.164962,-1.889962,7.114386,7.821045,8.539234,0.806437,-1.613085,-3.576460,-4.576255,-5.776400,-1.244841,-1.890176,-8.839344,-4.526771,-2.150124,-6.735591,-2.508785,9.115315,8.531835,-6.694096,-0.687534,-7.391791,-0.430705],[9.763560,-7.862587,9.738015,-6.160096,0.939395,-2.815901,-1.630482,0.220806,0.617654,-9.841348,8.477231,-5.609958,-8.544754,0.738205,5.871292,3.932589,-4.642380,0.600746,-1.512842,-6.838345,-5.103454,6.383880,0.490195,5.154453,2.231866,8.447787,-4.069410,-1.743768,7.760361,4.422579,2.445784,9.046655,-1.956434,3.872781,-7.699222,6.954650],[2.842124,-8.369219,4.809268,0.409738,8.326595,-2.483348,-3.191358,-7.173450,-3.919511,4.117207,8.865747,-4.380149,2.313487,-2.141033,9.633429,-3.071801,7.005965,9.399337,-5.995688,6.274937,0.236442,7.697672,-6.430022,5.853009,2.620032,-6.709363,5.705152,5.452453,8.302853,4.763126,9.513245,7.575619,-6.159365,3.763407,5.593699,-3.246726]], dtype = "float64")#candidate|4681|(18, 36)|const|float64
bop_4682 = relay.right_shift(var_4674.astype('uint16'), relay.reshape(const_4681.astype('uint16'), relay.shape_of(var_4674))) # shape=(18, 36)
func_3997_call = mod.get_global_var('func_3997')
func_3999_call = mutated_mod.get_global_var('func_3999')
const_4686 = relay.const(5, dtype = "int32")#candidate|4686|()|const|int32
call_4685 = relay.TupleGetItem(func_3997_call(relay.reshape(const_4686.astype('int32'), [])), 1)
call_4687 = relay.TupleGetItem(func_3999_call(relay.reshape(const_4686.astype('int32'), [])), 1)
uop_4697 = relay.atanh(call_4673.astype('float64')) # shape=(990,)
uop_4699 = relay.atanh(call_4675.astype('float64')) # shape=(990,)
output = relay.Tuple([call_4645,call_4655,bop_4682,call_4685,const_4686,uop_4697,])
output2 = relay.Tuple([call_4646,call_4656,bop_4682,call_4687,const_4686,uop_4699,])
func_4712 = relay.Function([var_4674,], output)
mod['func_4712'] = func_4712
mod = relay.transform.InferType()(mod)
var_4713 = relay.var("var_4713", dtype = "float64", shape = (18, 36))#candidate|4713|(18, 36)|var|float64
output = func_4712(var_4713)
func_4714 = relay.Function([var_4713], output)
mutated_mod['func_4714'] = func_4714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4221_call = mod.get_global_var('func_4221')
func_4222_call = mutated_mod.get_global_var('func_4222')
call_4733 = func_4221_call()
call_4734 = func_4221_call()
output = relay.Tuple([call_4733,])
output2 = relay.Tuple([call_4734,])
func_4737 = relay.Function([], output)
mod['func_4737'] = func_4737
mod = relay.transform.InferType()(mod)
mutated_mod['func_4737'] = func_4737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4737_call = mutated_mod.get_global_var('func_4737')
call_4738 = func_4737_call()
output = call_4738
func_4739 = relay.Function([], output)
mutated_mod['func_4739'] = func_4739
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4751 = relay.var("var_4751", dtype = "float32", shape = (11, 1, 4))#candidate|4751|(11, 1, 4)|var|float32
uop_4752 = relay.log2(var_4751.astype('float32')) # shape=(11, 1, 4)
uop_4761 = relay.sqrt(var_4751.astype('float64')) # shape=(11, 1, 4)
output = relay.Tuple([uop_4752,uop_4761,])
output2 = relay.Tuple([uop_4752,uop_4761,])
func_4767 = relay.Function([var_4751,], output)
mod['func_4767'] = func_4767
mod = relay.transform.InferType()(mod)
mutated_mod['func_4767'] = func_4767
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4768 = relay.var("var_4768", dtype = "float32", shape = (11, 1, 4))#candidate|4768|(11, 1, 4)|var|float32
func_4767_call = mutated_mod.get_global_var('func_4767')
call_4769 = func_4767_call(var_4768)
output = call_4769
func_4770 = relay.Function([var_4768], output)
mutated_mod['func_4770'] = func_4770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_4821 = relay.TupleGetItem(func_4503_call(), 0)
call_4822 = relay.TupleGetItem(func_4505_call(), 0)
func_3763_call = mod.get_global_var('func_3763')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_4830 = relay.TupleGetItem(func_3763_call(), 0)
call_4831 = relay.TupleGetItem(func_3764_call(), 0)
output = relay.Tuple([call_4821,call_4830,])
output2 = relay.Tuple([call_4822,call_4831,])
func_4832 = relay.Function([], output)
mod['func_4832'] = func_4832
mod = relay.transform.InferType()(mod)
output = func_4832()
func_4833 = relay.Function([], output)
mutated_mod['func_4833'] = func_4833
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4857 = relay.var("var_4857", dtype = "float64", shape = (8, 16, 6))#candidate|4857|(8, 16, 6)|var|float64
var_4858 = relay.var("var_4858", dtype = "float64", shape = (8, 16, 6))#candidate|4858|(8, 16, 6)|var|float64
bop_4859 = relay.greater(var_4857.astype('bool'), relay.reshape(var_4858.astype('bool'), relay.shape_of(var_4857))) # shape=(8, 16, 6)
output = bop_4859
output2 = bop_4859
func_4864 = relay.Function([var_4857,var_4858,], output)
mod['func_4864'] = func_4864
mod = relay.transform.InferType()(mod)
mutated_mod['func_4864'] = func_4864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4864_call = mutated_mod.get_global_var('func_4864')
var_4866 = relay.var("var_4866", dtype = "float64", shape = (8, 16, 6))#candidate|4866|(8, 16, 6)|var|float64
var_4867 = relay.var("var_4867", dtype = "float64", shape = (8, 16, 6))#candidate|4867|(8, 16, 6)|var|float64
call_4865 = func_4864_call(var_4866,var_4867,)
output = call_4865
func_4868 = relay.Function([var_4866,var_4867,], output)
mutated_mod['func_4868'] = func_4868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_4872 = relay.TupleGetItem(func_4503_call(), 0)
call_4873 = relay.TupleGetItem(func_4505_call(), 0)
func_2409_call = mod.get_global_var('func_2409')
func_2411_call = mutated_mod.get_global_var('func_2411')
var_4879 = relay.var("var_4879", dtype = "float64", shape = (448,))#candidate|4879|(448,)|var|float64
call_4878 = relay.TupleGetItem(func_2409_call(relay.reshape(var_4879.astype('float64'), [7, 8, 8])), 0)
call_4880 = relay.TupleGetItem(func_2411_call(relay.reshape(var_4879.astype('float64'), [7, 8, 8])), 0)
output = relay.Tuple([call_4872,call_4878,var_4879,])
output2 = relay.Tuple([call_4873,call_4880,var_4879,])
func_4883 = relay.Function([var_4879,], output)
mod['func_4883'] = func_4883
mod = relay.transform.InferType()(mod)
mutated_mod['func_4883'] = func_4883
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4884 = relay.var("var_4884", dtype = "float64", shape = (448,))#candidate|4884|(448,)|var|float64
func_4883_call = mutated_mod.get_global_var('func_4883')
call_4885 = func_4883_call(var_4884)
output = call_4885
func_4886 = relay.Function([var_4884], output)
mutated_mod['func_4886'] = func_4886
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4966 = relay.const([[[-4.351292,0.892768,-7.900102,4.872362,7.744068,3.986528,3.293071]],[[-9.618505,-3.710278,7.717111,2.479604,9.601103,-0.447920,-2.307163]],[[7.924535,1.851711,-8.296069,4.166385,-9.177298,-0.340582,0.997329]],[[-9.146863,1.457628,9.094536,4.362640,-4.679296,-8.477747,-8.722921]],[[-4.634516,-5.871668,-2.841241,2.827719,-5.972089,2.018707,8.378516]],[[6.786024,0.076683,-6.966093,-2.481937,-9.204127,-8.032420,-9.113109]],[[9.341494,4.746192,1.607542,7.047829,-4.784531,-8.196735,4.409523]],[[1.718596,9.795279,2.348811,-1.854507,-4.572272,-1.415051,-7.785141]]], dtype = "float64")#candidate|4966|(8, 1, 7)|const|float64
uop_4967 = relay.cos(const_4966.astype('float64')) # shape=(8, 1, 7)
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_4972 = relay.TupleGetItem(func_4614_call(), 0)
call_4973 = relay.TupleGetItem(func_4615_call(), 0)
output = relay.Tuple([uop_4967,call_4972,])
output2 = relay.Tuple([uop_4967,call_4973,])
func_4979 = relay.Function([], output)
mod['func_4979'] = func_4979
mod = relay.transform.InferType()(mod)
mutated_mod['func_4979'] = func_4979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4979_call = mutated_mod.get_global_var('func_4979')
call_4980 = func_4979_call()
output = call_4980
func_4981 = relay.Function([], output)
mutated_mod['func_4981'] = func_4981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3825_call = mod.get_global_var('func_3825')
func_3826_call = mutated_mod.get_global_var('func_3826')
call_5011 = func_3825_call()
call_5012 = func_3825_call()
output = relay.Tuple([call_5011,])
output2 = relay.Tuple([call_5012,])
func_5016 = relay.Function([], output)
mod['func_5016'] = func_5016
mod = relay.transform.InferType()(mod)
mutated_mod['func_5016'] = func_5016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5016_call = mutated_mod.get_global_var('func_5016')
call_5017 = func_5016_call()
output = call_5017
func_5018 = relay.Function([], output)
mutated_mod['func_5018'] = func_5018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2401_call = mod.get_global_var('func_2401')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_5023 = func_2401_call()
call_5024 = func_2401_call()
var_5036 = relay.var("var_5036", dtype = "int8", shape = (15, 11, 6))#candidate|5036|(15, 11, 6)|var|int8
bop_5037 = relay.logical_and(call_5023.astype('bool'), relay.reshape(var_5036.astype('bool'), relay.shape_of(call_5023))) # shape=(15, 11, 6)
bop_5040 = relay.logical_and(call_5024.astype('bool'), relay.reshape(var_5036.astype('bool'), relay.shape_of(call_5024))) # shape=(15, 11, 6)
output = bop_5037
output2 = bop_5040
func_5041 = relay.Function([var_5036,], output)
mod['func_5041'] = func_5041
mod = relay.transform.InferType()(mod)
var_5042 = relay.var("var_5042", dtype = "int8", shape = (15, 11, 6))#candidate|5042|(15, 11, 6)|var|int8
output = func_5041(var_5042)
func_5043 = relay.Function([var_5042], output)
mutated_mod['func_5043'] = func_5043
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5055 = relay.var("var_5055", dtype = "uint64", shape = ())#candidate|5055|()|var|uint64
var_5056 = relay.var("var_5056", dtype = "uint64", shape = (12, 2, 15))#candidate|5056|(12, 2, 15)|var|uint64
bop_5057 = relay.equal(var_5055.astype('bool'), var_5056.astype('bool')) # shape=(12, 2, 15)
output = relay.Tuple([bop_5057,])
output2 = relay.Tuple([bop_5057,])
func_5062 = relay.Function([var_5055,var_5056,], output)
mod['func_5062'] = func_5062
mod = relay.transform.InferType()(mod)
var_5063 = relay.var("var_5063", dtype = "uint64", shape = ())#candidate|5063|()|var|uint64
var_5064 = relay.var("var_5064", dtype = "uint64", shape = (12, 2, 15))#candidate|5064|(12, 2, 15)|var|uint64
output = func_5062(var_5063,var_5064,)
func_5065 = relay.Function([var_5063,var_5064,], output)
mutated_mod['func_5065'] = func_5065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5016_call = mod.get_global_var('func_5016')
func_5018_call = mutated_mod.get_global_var('func_5018')
call_5121 = relay.TupleGetItem(func_5016_call(), 0)
call_5122 = relay.TupleGetItem(func_5018_call(), 0)
output = relay.Tuple([call_5121,])
output2 = relay.Tuple([call_5122,])
func_5123 = relay.Function([], output)
mod['func_5123'] = func_5123
mod = relay.transform.InferType()(mod)
output = func_5123()
func_5124 = relay.Function([], output)
mutated_mod['func_5124'] = func_5124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5158 = relay.var("var_5158", dtype = "uint32", shape = (3, 16, 15))#candidate|5158|(3, 16, 15)|var|uint32
var_5159 = relay.var("var_5159", dtype = "uint32", shape = (3, 16, 15))#candidate|5159|(3, 16, 15)|var|uint32
bop_5160 = relay.less(var_5158.astype('bool'), relay.reshape(var_5159.astype('bool'), relay.shape_of(var_5158))) # shape=(3, 16, 15)
func_3763_call = mod.get_global_var('func_3763')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_5178 = relay.TupleGetItem(func_3763_call(), 0)
call_5179 = relay.TupleGetItem(func_3764_call(), 0)
bop_5180 = relay.greater(var_5159.astype('bool'), relay.reshape(var_5158.astype('bool'), relay.shape_of(var_5159))) # shape=(3, 16, 15)
uop_5183 = relay.exp(var_5158.astype('float32')) # shape=(3, 16, 15)
uop_5185 = relay.log2(uop_5183.astype('float64')) # shape=(3, 16, 15)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_5191 = relay.TupleGetItem(func_2793_call(), 0)
call_5192 = relay.TupleGetItem(func_2794_call(), 0)
func_2409_call = mod.get_global_var('func_2409')
func_2411_call = mutated_mod.get_global_var('func_2411')
const_5208 = relay.const([-9.029763,-9.787469,-8.235010,-0.507613,-4.154665,-9.969163,3.664253,-4.862729,-9.301005,-4.085409,3.331680,-4.968369,1.150318,-0.645240,4.769572,9.403764,3.165921,-4.114966,6.119930,1.967444,-8.365528,-9.933184,0.069156,-5.442746,-9.880409,-1.792986,-2.060334,3.805023,9.793461,-4.507976,-2.088073,-7.904937,-9.810000,9.027305,8.898131,5.219753,-8.654918,6.739629,7.417692,-6.372921,-0.766487,5.023841,9.263985,-2.360917,-5.910630,-2.900241,-3.429355,0.526275,4.662265,-6.440308,7.421748,-6.786062,5.386478,-2.398833,-8.527523,8.176043,5.858900,0.472765,4.279864,9.582122,9.419700,-8.999329,-3.629685,-3.419433,-7.235274,-8.232892,-9.971685,-6.747660,-4.896882,-0.962227,3.916090,-2.316038,-6.750590,2.276264,2.149343,-1.159341,-0.243414,2.221550,-1.854582,-9.237522,-7.361934,-2.493724,-9.984202,9.615535,3.297197,6.872496,5.917767,6.387200,6.358943,2.922639,0.261655,8.820227,2.505566,-7.752776,-4.628412,-3.871164,8.876098,-3.851308,1.407587,2.876897,1.247646,4.627419,-1.383455,0.004102,-1.837915,-0.518761,-4.515951,2.697836,-3.973356,7.501158,4.710929,-0.261925,-6.670801,-1.705070,-8.486627,6.494004,-2.798696,-8.710289,3.493771,-2.775225,-2.911594,-8.546529,7.371978,-1.757972,6.194501,-9.708143,-4.970696,-0.770408,7.457883,-2.275837,-5.686978,-9.962653,2.574166,0.649518,-3.652936,-7.101695,-4.486139,7.112604,-2.000498,-7.977650,8.069156,-3.842953,0.033170,-8.976652,8.454469,-0.318843,-8.421158,-3.109618,2.521763,4.998441,-8.708225,-8.977874,-1.531227,-6.211180,-7.190051,-3.506506,5.378694,5.110682,8.432743,-2.141709,-1.663172,-4.138514,5.618587,-3.262801,-1.399683,-6.660257,2.866479,-2.787091,-4.999472,0.369665,0.080154,-0.201141,-9.399420,8.071055,6.776288,8.304024,-7.740508,2.890335,-2.514461,-9.205085,3.563416,6.689582,3.383093,-8.288862,-6.697751,-0.585957,0.786420,1.644674,-4.552068,-5.339708,-6.450641,-2.497329,3.766861,-0.823332,9.488809,4.445571,0.002832,-1.999143,-6.253763,-2.982600,-8.717029,-9.270909,9.105745,2.911963,-8.838025,4.078734,8.860454,9.770028,0.704231,3.015524,-2.394178,2.640778,6.590930,-8.853082,-3.661610,2.509967,-0.767562,1.953832,9.675218,2.335682,-7.425516,-4.685715,-0.373423,-9.046248,0.039442,7.835684,-3.067713,1.901740,-7.288428,6.382064,-4.115672,0.542727,-2.861507,-6.448111,9.805329,3.563290,-1.207775,-9.406213,5.630340,0.946677,-6.186769,-8.735958,4.033911,-4.346421,-9.241702,2.495566,-2.646462,5.216139,8.500964,-0.096388,1.328096,-4.484271,0.090029,4.810816,2.111937,8.549690,2.499081,8.285889,9.729488,-6.700637,9.721943,-8.404250,-2.323303,5.637336,2.335482,-9.200873,7.393616,9.047058,4.118777,-5.940115,2.589255,-5.022867,5.563225,2.243153,-4.301670,-3.728983,5.859104,5.901069,-2.802936,1.030156,1.898335,6.236844,-7.842460,4.989957,6.697069,5.767566,-3.502618,8.526444,3.011456,-4.055344,-5.475851,3.047426,-0.141375,1.213008,5.272495,-0.364932,-2.966749,-9.922494,-6.382967,9.222411,1.174548,-6.999315,-7.498195,1.589345,9.431577,9.414716,5.035072,3.310252,-1.427586,-5.639509,-2.050902,-3.362516,-0.904570,3.678808,-0.048463,-4.699943,5.395628,9.869942,-6.050761,3.629243,1.736641,0.874539,-1.284840,-9.525279,8.453807,-8.866986,2.013461,8.806786,6.851714,7.104884,0.516452,9.028989,-0.363215,-3.179671,-8.833899,-9.767438,1.184213,-0.650965,3.849275,-3.442727,8.875478,-0.946201,4.844566,8.643577,-1.957520,-1.866494,-4.622423,7.052491,2.310399,-8.962904,2.039937,5.932791,-2.404413,-2.368334,-6.320718,6.551716,-8.762470,-3.735450,6.869513,-0.148247,-6.079848,0.951602,8.072398,-2.196072,-0.015449,-5.824355,0.225775,-5.923928,5.553330,4.912211,6.961594,8.442220,-4.685142,2.351272,5.946842,-9.997475,7.873088,4.115597,-9.489952,3.757083,-8.991209,-2.568178,8.573729,3.055190,-6.018458,-7.660270,6.125609,7.913109,5.492394,6.640747,-1.015348,4.478060,3.131679,-3.777591,-6.704399,7.202451,2.443399,-4.410708,-2.655936,1.782217,8.172687,8.724022,-8.135517,-8.944731,2.722195,-6.895297,7.481007,9.124754,-7.153203,-9.739011,5.229405,9.237099,-1.025971,3.377840,-0.438091,0.675999,-1.468779,-3.929236,1.235584,8.298299,3.523999,-9.494772,0.547960,4.179154,-1.671381,-3.858695,2.315040,-9.996444,7.000615,3.844140,9.652291,9.545541,0.986435,-5.641776,0.788326,8.054560,6.020406,2.467225,-6.729582,2.015680,3.853549,-1.604124,8.403988,-2.889745,8.098246,-6.908474,-2.601665,-7.933573], dtype = "float64")#candidate|5208|(448,)|const|float64
call_5207 = relay.TupleGetItem(func_2409_call(relay.reshape(const_5208.astype('float64'), [7, 8, 8])), 0)
call_5209 = relay.TupleGetItem(func_2411_call(relay.reshape(const_5208.astype('float64'), [7, 8, 8])), 0)
func_5123_call = mod.get_global_var('func_5123')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_5210 = relay.TupleGetItem(func_5123_call(), 0)
call_5211 = relay.TupleGetItem(func_5124_call(), 0)
uop_5218 = relay.acosh(uop_5183.astype('float64')) # shape=(3, 16, 15)
output = relay.Tuple([bop_5160,call_5178,bop_5180,uop_5185,call_5191,call_5207,const_5208,call_5210,uop_5218,])
output2 = relay.Tuple([bop_5160,call_5179,bop_5180,uop_5185,call_5192,call_5209,const_5208,call_5211,uop_5218,])
func_5230 = relay.Function([var_5158,var_5159,], output)
mod['func_5230'] = func_5230
mod = relay.transform.InferType()(mod)
mutated_mod['func_5230'] = func_5230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5230_call = mutated_mod.get_global_var('func_5230')
var_5232 = relay.var("var_5232", dtype = "uint32", shape = (3, 16, 15))#candidate|5232|(3, 16, 15)|var|uint32
var_5233 = relay.var("var_5233", dtype = "uint32", shape = (3, 16, 15))#candidate|5233|(3, 16, 15)|var|uint32
call_5231 = func_5230_call(var_5232,var_5233,)
output = call_5231
func_5234 = relay.Function([var_5232,var_5233,], output)
mutated_mod['func_5234'] = func_5234
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5243 = relay.var("var_5243", dtype = "float64", shape = (11, 7, 13))#candidate|5243|(11, 7, 13)|var|float64
uop_5244 = relay.sigmoid(var_5243.astype('float64')) # shape=(11, 7, 13)
output = uop_5244
output2 = uop_5244
func_5247 = relay.Function([var_5243,], output)
mod['func_5247'] = func_5247
mod = relay.transform.InferType()(mod)
mutated_mod['func_5247'] = func_5247
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5248 = relay.var("var_5248", dtype = "float64", shape = (11, 7, 13))#candidate|5248|(11, 7, 13)|var|float64
func_5247_call = mutated_mod.get_global_var('func_5247')
call_5249 = func_5247_call(var_5248)
output = call_5249
func_5250 = relay.Function([var_5248], output)
mutated_mod['func_5250'] = func_5250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3763_call = mod.get_global_var('func_3763')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_5252 = relay.TupleGetItem(func_3763_call(), 0)
call_5253 = relay.TupleGetItem(func_3764_call(), 0)
func_3636_call = mod.get_global_var('func_3636')
func_3638_call = mutated_mod.get_global_var('func_3638')
call_5260 = relay.TupleGetItem(func_3636_call(), 0)
call_5261 = relay.TupleGetItem(func_3638_call(), 0)
output = relay.Tuple([call_5252,call_5260,])
output2 = relay.Tuple([call_5253,call_5261,])
func_5267 = relay.Function([], output)
mod['func_5267'] = func_5267
mod = relay.transform.InferType()(mod)
mutated_mod['func_5267'] = func_5267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mutated_mod.get_global_var('func_5267')
call_5268 = func_5267_call()
output = call_5268
func_5269 = relay.Function([], output)
mutated_mod['func_5269'] = func_5269
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5293 = relay.var("var_5293", dtype = "float64", shape = (10, 2, 7))#candidate|5293|(10, 2, 7)|var|float64
uop_5294 = relay.atanh(var_5293.astype('float64')) # shape=(10, 2, 7)
func_1360_call = mod.get_global_var('func_1360')
func_1363_call = mutated_mod.get_global_var('func_1363')
const_5298 = relay.const(-3, dtype = "int32")#candidate|5298|()|const|int32
const_5299 = relay.const([-8,6,-7,-1,10,-6,6,-6,-6,7,-2,6,9,1,2,7,-6,5,9,8,5,-2,1,-9,-2,-8,-7,6,-8,9], dtype = "int32")#candidate|5299|(30,)|const|int32
call_5297 = func_1360_call(relay.reshape(const_5298.astype('int32'), []), relay.reshape(const_5299.astype('int32'), [1, 10, 3]), )
call_5300 = func_1360_call(relay.reshape(const_5298.astype('int32'), []), relay.reshape(const_5299.astype('int32'), [1, 10, 3]), )
output = relay.Tuple([uop_5294,call_5297,const_5298,const_5299,])
output2 = relay.Tuple([uop_5294,call_5300,const_5298,const_5299,])
func_5302 = relay.Function([var_5293,], output)
mod['func_5302'] = func_5302
mod = relay.transform.InferType()(mod)
mutated_mod['func_5302'] = func_5302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5303 = relay.var("var_5303", dtype = "float64", shape = (10, 2, 7))#candidate|5303|(10, 2, 7)|var|float64
func_5302_call = mutated_mod.get_global_var('func_5302')
call_5304 = func_5302_call(var_5303)
output = call_5304
func_5305 = relay.Function([var_5303], output)
mutated_mod['func_5305'] = func_5305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2990_call = mod.get_global_var('func_2990')
func_2992_call = mutated_mod.get_global_var('func_2992')
call_5311 = func_2990_call()
call_5312 = func_2990_call()
output = call_5311
output2 = call_5312
func_5318 = relay.Function([], output)
mod['func_5318'] = func_5318
mod = relay.transform.InferType()(mod)
mutated_mod['func_5318'] = func_5318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5318_call = mutated_mod.get_global_var('func_5318')
call_5319 = func_5318_call()
output = call_5319
func_5320 = relay.Function([], output)
mutated_mod['func_5320'] = func_5320
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5323 = relay.const([[[7.125736,-7.725757,8.237390],[-8.210089,-8.960133,1.039023],[9.919726,-5.114005,-9.507033],[-9.292550,4.914565,-8.295687],[-2.407375,5.374274,7.926867],[-8.687895,3.804809,-6.246913],[3.518027,3.142226,-5.774454],[-5.509222,3.612230,-8.830265],[-8.042762,7.213432,8.505126],[3.375437,-2.019626,6.199019],[-7.910546,-3.047814,-1.828048],[-0.415019,2.536134,3.525296]],[[1.846056,0.326295,-6.610174],[-1.107834,-4.778498,-4.147965],[6.323564,6.012219,-8.534566],[-5.218207,1.503924,2.670366],[4.428989,2.003656,3.377445],[-6.656404,5.114783,5.585489],[9.593293,-3.086592,9.975953],[-5.902168,8.512012,-3.270037],[-2.332752,-8.500246,7.445715],[-1.671008,5.227604,6.904902],[-7.555507,2.724165,0.323750],[-8.977788,7.398207,-8.189617]],[[6.667162,8.031125,0.086851],[7.289361,-7.910348,5.276155],[1.922026,-1.051445,7.017756],[8.941373,-9.019443,8.118702],[8.492528,-2.477883,4.032104],[-6.926858,4.953105,8.501077],[2.846805,7.233141,-2.376806],[-0.870334,-9.856622,-4.542811],[-7.952124,0.178126,2.288857],[5.717736,-5.173912,4.232412],[-0.249845,4.290978,5.339745],[-4.663072,5.530570,4.865152]],[[-0.463624,7.932311,-8.845286],[5.941307,3.042168,8.773159],[4.869232,4.176129,8.830699],[7.622230,-6.616868,1.291513],[6.298062,4.541523,7.291378],[-3.662458,-7.190769,-5.888035],[-7.140875,7.593939,1.942769],[-3.658602,1.438449,-5.512398],[-6.685502,7.657418,-8.825418],[-6.309263,-7.342282,-9.326774],[-0.510393,-1.025160,-1.367817],[-1.961262,-9.933027,-6.040147]],[[-7.526392,-6.318569,0.628894],[-6.715843,9.539391,-4.565789],[4.589912,0.955543,-5.034202],[1.161013,0.179658,9.236076],[7.683491,-3.370038,-3.897723],[4.554508,2.620974,-0.088547],[-6.985389,-5.263343,-2.528107],[-2.349274,5.326434,-3.835710],[5.374279,4.646703,0.598470],[9.975201,-7.458817,-9.506687],[-5.406617,3.417354,4.425098],[-6.460524,1.233771,1.747717]],[[-7.740557,5.804581,-4.945295],[1.266724,9.670917,-4.890404],[-9.766599,7.003609,5.772711],[4.301447,0.944157,5.192427],[-3.520780,0.242545,-4.926738],[-8.293628,-9.098755,-7.351121],[2.828429,-3.050992,-3.393765],[3.218210,-5.543710,4.371475],[-2.237067,-1.897908,-4.192998],[-4.251353,7.181872,-2.279548],[0.184432,-5.653569,-6.522293],[-8.795580,0.096151,-0.021588]],[[9.360681,-1.449741,4.141734],[2.451144,-7.800815,5.501019],[7.953756,2.339283,6.473149],[-5.577454,-7.174863,-6.673566],[5.673343,-5.900509,-5.263112],[7.047308,-1.148290,1.415696],[1.520231,7.499964,-2.979272],[-8.879357,1.207960,4.525292],[9.223725,8.319685,-9.907443],[-8.452830,-7.915571,-3.121668],[-9.009863,-0.952547,9.106133],[-4.597074,-5.792990,-3.809997]],[[-8.299405,-9.684342,3.536133],[9.352078,1.580761,-6.495142],[-4.517482,5.906798,-6.540188],[9.376201,8.535179,5.709937],[-8.521944,-9.117271,-2.414679],[3.470812,2.389899,-0.738208],[4.266261,-1.855944,-9.081204],[5.428526,4.525521,9.131561],[-5.434549,-0.357016,-1.821969],[1.401588,4.763780,9.762751],[-6.098730,8.554336,-5.748057],[-0.436617,9.839699,-9.619845]],[[-5.781181,-6.861140,-1.903906],[1.370742,9.775544,2.618908],[8.195006,-2.281304,-3.575397],[-1.688137,-8.169253,-0.485725],[9.784406,5.303484,7.007253],[-3.943300,7.951362,-1.282140],[-7.253164,-9.545812,7.926900],[0.105084,-3.678269,-9.091751],[8.322015,-5.577377,-7.536616],[-2.653143,1.829532,-5.408228],[9.489288,-7.263341,1.746434],[6.603292,-0.236380,5.606377]],[[1.652062,1.435937,-5.023540],[-3.130085,-9.254361,-5.927439],[2.906266,8.141201,-3.507077],[-7.603156,-7.220538,-0.534121],[7.354705,-3.726911,8.397261],[8.997386,-9.399668,7.215084],[-4.193688,6.094225,-9.853807],[9.202232,-8.669320,-8.614906],[-8.066020,9.214349,-3.409304],[0.907816,5.774938,8.565820],[9.367124,9.509473,1.585517],[4.184580,-2.180911,1.542673]],[[-1.255038,-9.212364,3.188281],[3.530636,6.297973,-6.979272],[-7.977625,1.747787,4.268733],[-1.152774,-5.672568,2.462445],[-7.179481,8.201506,5.869088],[8.988058,-5.870453,-9.846502],[1.039377,9.095756,-6.084652],[-5.376631,1.062624,-0.274194],[-5.323035,-9.122912,-3.968910],[6.102695,-6.138036,0.989598],[0.731827,1.774096,0.444981],[8.432404,6.571166,1.887777]],[[-6.708338,-5.105024,-0.187355],[6.235610,9.442348,2.106016],[1.296613,8.019146,2.613890],[4.534350,5.872643,-5.865447],[-7.175697,6.966344,6.173669],[-0.677479,-3.727045,1.161624],[1.228686,-2.532987,-8.358153],[3.197006,-2.834518,5.587676],[9.743229,-9.529252,1.340875],[8.332478,-9.090955,4.063752],[-6.115050,1.444244,-7.714425],[4.439188,9.807594,8.812998]],[[7.856660,8.368893,5.446238],[8.667053,7.142621,8.340890],[0.341975,2.649508,-8.695512],[5.956133,-5.895709,6.239371],[3.942783,-3.098422,-8.798448],[9.352303,-6.812747,9.651277],[6.061575,4.279250,-8.360915],[-9.848578,7.613444,6.713649],[-3.997800,-2.644294,-6.506971],[-7.766110,-2.615535,-8.127852],[-0.842484,-0.159983,9.404784],[-2.589514,2.900318,4.851481]],[[-3.956922,4.144435,2.376388],[7.660178,2.313591,-5.307365],[-1.181231,7.684666,-8.808986],[5.668638,2.516131,2.053124],[-0.312681,-3.935592,7.642448],[4.669725,4.876480,-9.065422],[-6.029665,-4.505270,6.498514],[5.517813,6.604783,8.020426],[-7.572628,-9.767776,-2.178770],[-5.081095,4.414129,-2.463317],[8.407263,4.584944,-8.681290],[6.823101,3.812641,-0.204681]],[[4.502586,-5.011101,8.783304],[-6.324106,3.339428,3.375294],[-7.197898,-9.373301,-4.355361],[0.968609,-9.006577,-1.090572],[-7.906158,0.583866,-7.980258],[-4.383399,5.484374,-9.609461],[-2.653866,1.647745,-2.602188],[-3.267915,-7.838166,-5.678262],[8.917739,-0.826228,-9.672461],[6.642978,2.571259,1.967273],[-3.642630,5.085367,-2.405592],[-0.161523,-5.336838,-6.907617]],[[5.371163,1.408844,8.858665],[-2.573493,3.709657,8.585297],[-6.743022,-6.228260,7.150505],[3.733613,-1.024337,-5.047808],[-2.880021,7.987148,-6.728897],[6.365422,-4.735399,1.992986],[9.719371,0.648304,2.481031],[-1.324293,6.872143,0.657480],[-9.209523,-3.397735,7.271800],[-2.300855,-1.414646,-9.373406],[9.323270,-9.261782,-6.972409],[-3.660649,7.704660,5.526561]]], dtype = "float32")#candidate|5323|(16, 12, 3)|const|float32
uop_5324 = relay.acosh(const_5323.astype('float32')) # shape=(16, 12, 3)
func_5016_call = mod.get_global_var('func_5016')
func_5018_call = mutated_mod.get_global_var('func_5018')
call_5326 = relay.TupleGetItem(func_5016_call(), 0)
call_5327 = relay.TupleGetItem(func_5018_call(), 0)
const_5343 = relay.const([[[6.189502,-1.859769,5.796017],[-8.799814,9.629061,-8.144552],[-6.572754,2.725590,-4.903225],[-5.671764,-7.143030,-1.803006],[2.930494,-8.830332,6.857060],[-0.756655,-4.284926,-9.912547],[-1.119184,6.714390,0.282705],[-9.994427,5.538648,-6.354142],[3.724678,-5.480834,-4.756080],[0.861995,-0.163888,3.209453],[3.952893,3.817255,9.655777],[1.225541,-4.361270,4.901767]],[[1.352783,9.157193,3.099049],[-7.141358,-8.896699,4.487086],[1.289333,4.683781,-9.856289],[5.842706,-2.352352,2.493193],[0.242889,4.343396,1.636890],[7.968137,-0.693829,8.457569],[8.468961,8.373142,-9.034966],[-1.813759,5.139159,0.211615],[-2.663773,3.183427,1.414273],[-7.668099,5.322974,-6.332293],[2.556746,6.758556,7.783322],[7.735735,1.168103,-8.127017]],[[2.054463,5.324498,-4.148706],[-2.151314,-6.341261,-0.876215],[-5.206622,-2.110311,-5.025966],[-0.891255,-7.439222,-2.617900],[-2.896454,-9.075996,-7.943946],[4.970909,4.048064,-8.546537],[-9.801501,5.145465,-9.574425],[-5.213469,-9.080784,-5.594635],[-6.086534,-3.712877,2.221514],[-9.615035,7.150727,0.196634],[5.498135,6.321450,7.271098],[8.412483,1.920131,-7.403300]],[[-7.508724,-2.303729,6.008875],[3.321896,-0.235745,8.808741],[-9.905968,3.740450,-3.595329],[4.257967,-6.025616,5.258527],[-3.915819,0.292690,6.279759],[0.270134,-5.290869,-1.782626],[4.326993,9.542582,-1.631049],[3.200322,-2.796199,-0.807403],[8.327757,6.909775,-4.860863],[5.674978,5.908141,-2.809987],[3.152093,-7.595768,-8.513943],[5.460205,-1.510669,2.947312]],[[1.171856,-8.156947,5.054867],[9.647919,-8.041982,-6.055893],[0.211003,-8.262877,-6.745890],[7.090481,-2.128755,-1.779284],[-3.344776,-4.014902,-2.125418],[2.659562,-8.860805,-3.658822],[-9.405028,-9.302232,-4.801649],[-3.648729,1.540357,-2.992995],[4.450226,4.747031,1.331670],[-8.573369,4.751448,-8.260933],[-8.791520,-3.138318,3.033158],[6.957044,-6.964692,7.895121]],[[-2.285237,-1.780458,-7.483724],[-8.492720,-7.985798,5.991492],[1.113307,9.001657,9.645405],[-2.014197,-2.144405,-7.921235],[3.013033,3.904066,-9.330719],[-0.455577,-3.974090,-0.332129],[8.628955,8.411627,-4.770599],[4.053212,-6.404161,-6.343543],[2.157179,-7.205841,5.146783],[7.849018,-5.826904,-3.139558],[0.825645,3.884917,7.716648],[-1.536695,-7.067792,-4.346213]],[[9.039370,-3.690765,4.120786],[0.505254,-0.693820,-0.744197],[-1.763355,-0.498052,-6.304093],[7.564023,-6.875682,-4.043783],[-7.011358,-0.314572,-6.368038],[4.766484,0.497236,3.940197],[2.475754,7.708798,-4.443998],[3.313914,2.660115,2.774710],[2.266195,-0.058306,-2.167467],[7.208989,5.057269,9.302957],[7.862714,3.561864,0.415271],[3.237668,1.938993,-9.775329]],[[-5.630029,4.872794,5.588113],[7.634586,3.325875,-5.558194],[-7.894147,8.904064,-9.964778],[7.307469,6.485389,-2.215141],[-6.040772,3.893276,-8.044385],[0.298521,-2.140967,-4.779749],[-9.127279,-0.193790,8.129392],[8.834792,-4.833700,-9.419268],[2.201490,-7.022313,-8.647110],[5.447253,-9.399037,6.831729],[-7.232686,0.911760,5.076487],[7.059405,-5.976620,7.904577]],[[-7.358832,5.187157,0.001989],[0.186939,-1.346696,-4.621769],[-3.302711,9.808233,-0.151237],[3.267029,8.462616,5.931465],[6.361295,-9.856134,-1.094880],[1.128645,-2.467563,-2.957879],[-0.304916,2.345982,2.032927],[-2.226362,9.356016,2.927087],[-5.137967,5.181212,1.401760],[-2.583741,5.915776,-6.239626],[-5.625998,-9.290407,7.341406],[0.040300,8.253816,-8.135248]],[[-4.912962,-4.204566,-0.068730],[2.857097,7.406773,-4.182117],[-8.234871,1.062783,-0.862380],[3.637091,3.025970,2.113615],[-0.551744,1.143531,5.318521],[0.377315,-5.837748,-3.906054],[6.214851,8.940054,-4.995938],[6.790150,-3.042673,-5.798760],[6.996777,9.855485,0.263441],[1.703382,0.621758,6.755123],[-2.534971,-7.453029,6.681529],[9.503379,6.791798,6.899190]],[[-6.873293,-3.818472,1.993475],[4.564684,-7.941091,7.849966],[-1.622445,-4.377993,5.166420],[-3.278503,-6.224777,-3.512837],[3.170263,-4.542580,-7.439480],[-8.809746,-6.744675,6.486152],[9.160557,-2.836095,-8.582317],[-0.187764,-8.039457,-1.544041],[-9.109668,7.508645,-8.109576],[-4.101330,2.254592,-5.606289],[-3.841597,6.431081,8.582075],[-7.612674,8.998511,-7.076014]],[[2.885057,-9.905802,7.238900],[3.917423,-4.604578,-3.120795],[8.748280,-2.204649,5.026122],[-0.344059,-7.084442,1.308228],[4.977016,-2.669256,-4.798254],[-0.855015,8.495305,-8.103123],[8.625863,8.043745,-3.195238],[-6.621458,-9.928497,5.981725],[8.341634,-6.336478,6.908358],[8.661550,7.084727,2.720483],[8.558313,8.861311,3.091810],[8.319636,-7.405479,-5.624395]],[[0.031200,-8.861650,5.701120],[3.005412,8.486199,-2.755099],[2.250132,2.131907,-8.604133],[7.139609,-8.963065,-1.238162],[-0.481781,6.128625,-8.659932],[2.256899,-1.775012,-4.427939],[1.221187,1.640951,9.721706],[4.035751,2.665831,4.343199],[-0.203541,1.596781,-0.213221],[-5.946729,-1.487663,3.204941],[6.802924,-5.340639,-0.118817],[6.000106,-2.282377,-8.008925]],[[6.810796,9.976990,7.526495],[-2.194121,0.460842,-9.598154],[7.746051,-0.810458,-5.890595],[1.099145,-3.102939,-7.870354],[-3.262683,4.588708,-8.420890],[-7.467262,8.992944,-9.881591],[-2.791722,-1.333364,4.615156],[1.815309,2.761168,-9.274000],[3.525441,0.978355,7.454903],[-9.199909,-3.745048,-8.642142],[-4.703588,-8.365310,-0.806697],[-6.036595,2.449420,-7.991868]],[[3.056065,6.922857,0.631366],[1.890297,2.321499,0.439190],[-0.428558,-2.864695,4.873899],[6.405054,8.826894,3.733961],[-5.753922,7.179117,3.417558],[-5.551987,7.490520,6.620037],[8.914878,-1.638945,-7.420961],[6.244472,3.634644,4.223867],[5.226596,-1.470752,-6.132412],[-4.699673,9.683314,-9.578414],[-7.280118,-7.020563,-4.584399],[-0.959561,-4.044647,7.588812]],[[-6.006338,0.144177,-5.697543],[-4.138997,6.565131,4.192535],[0.761497,-5.286178,5.471371],[1.920432,-3.155822,2.169149],[4.284922,-0.696771,-2.291931],[-7.421920,4.047039,7.633809],[-2.559546,4.469317,-8.350298],[3.261582,-8.510555,3.323182],[-9.844014,0.785428,-1.655452],[-3.318169,3.971024,4.814627],[-1.146369,-3.018498,0.167382],[1.494480,-0.232619,2.751695]]], dtype = "float32")#candidate|5343|(16, 12, 3)|const|float32
bop_5344 = relay.logical_or(uop_5324.astype('bool'), relay.reshape(const_5343.astype('bool'), relay.shape_of(uop_5324))) # shape=(16, 12, 3)
var_5347 = relay.var("var_5347", dtype = "bool", shape = (16, 12, 3))#candidate|5347|(16, 12, 3)|var|bool
bop_5348 = relay.floor_mod(bop_5344.astype('float32'), relay.reshape(var_5347.astype('float32'), relay.shape_of(bop_5344))) # shape=(16, 12, 3)
uop_5357 = relay.log2(uop_5324.astype('float64')) # shape=(16, 12, 3)
bop_5361 = relay.multiply(const_5343.astype('int32'), relay.reshape(bop_5348.astype('int32'), relay.shape_of(const_5343))) # shape=(16, 12, 3)
output = relay.Tuple([call_5326,uop_5357,bop_5361,])
output2 = relay.Tuple([call_5327,uop_5357,bop_5361,])
func_5367 = relay.Function([var_5347,], output)
mod['func_5367'] = func_5367
mod = relay.transform.InferType()(mod)
var_5368 = relay.var("var_5368", dtype = "bool", shape = (16, 12, 3))#candidate|5368|(16, 12, 3)|var|bool
output = func_5367(var_5368)
func_5369 = relay.Function([var_5368], output)
mutated_mod['func_5369'] = func_5369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_5400 = relay.TupleGetItem(func_4503_call(), 0)
call_5401 = relay.TupleGetItem(func_4505_call(), 0)
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_5408 = relay.TupleGetItem(func_4503_call(), 0)
call_5409 = relay.TupleGetItem(func_4505_call(), 0)
func_3901_call = mod.get_global_var('func_3901')
func_3903_call = mutated_mod.get_global_var('func_3903')
call_5444 = relay.TupleGetItem(func_3901_call(), 1)
call_5445 = relay.TupleGetItem(func_3903_call(), 1)
output = relay.Tuple([call_5400,call_5408,call_5444,])
output2 = relay.Tuple([call_5401,call_5409,call_5445,])
func_5447 = relay.Function([], output)
mod['func_5447'] = func_5447
mod = relay.transform.InferType()(mod)
output = func_5447()
func_5448 = relay.Function([], output)
mutated_mod['func_5448'] = func_5448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5472 = relay.var("var_5472", dtype = "float32", shape = (16, 8, 3))#candidate|5472|(16, 8, 3)|var|float32
var_5473 = relay.var("var_5473", dtype = "float32", shape = (16, 8, 3))#candidate|5473|(16, 8, 3)|var|float32
bop_5474 = relay.not_equal(var_5472.astype('bool'), relay.reshape(var_5473.astype('bool'), relay.shape_of(var_5472))) # shape=(16, 8, 3)
func_3508_call = mod.get_global_var('func_3508')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_5477 = relay.TupleGetItem(func_3508_call(), 0)
call_5478 = relay.TupleGetItem(func_3509_call(), 0)
output = relay.Tuple([bop_5474,call_5477,])
output2 = relay.Tuple([bop_5474,call_5478,])
func_5485 = relay.Function([var_5472,var_5473,], output)
mod['func_5485'] = func_5485
mod = relay.transform.InferType()(mod)
mutated_mod['func_5485'] = func_5485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5485_call = mutated_mod.get_global_var('func_5485')
var_5487 = relay.var("var_5487", dtype = "float32", shape = (16, 8, 3))#candidate|5487|(16, 8, 3)|var|float32
var_5488 = relay.var("var_5488", dtype = "float32", shape = (16, 8, 3))#candidate|5488|(16, 8, 3)|var|float32
call_5486 = func_5485_call(var_5487,var_5488,)
output = call_5486
func_5489 = relay.Function([var_5487,var_5488,], output)
mutated_mod['func_5489'] = func_5489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2826_call = mutated_mod.get_global_var('func_2826')
call_5508 = relay.TupleGetItem(func_2824_call(), 0)
call_5509 = relay.TupleGetItem(func_2826_call(), 0)
output = relay.Tuple([call_5508,])
output2 = relay.Tuple([call_5509,])
func_5512 = relay.Function([], output)
mod['func_5512'] = func_5512
mod = relay.transform.InferType()(mod)
output = func_5512()
func_5513 = relay.Function([], output)
mutated_mod['func_5513'] = func_5513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mod.get_global_var('func_3069')
func_3071_call = mutated_mod.get_global_var('func_3071')
call_5578 = relay.TupleGetItem(func_3069_call(), 0)
call_5579 = relay.TupleGetItem(func_3071_call(), 0)
output = call_5578
output2 = call_5579
func_5581 = relay.Function([], output)
mod['func_5581'] = func_5581
mod = relay.transform.InferType()(mod)
mutated_mod['func_5581'] = func_5581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5581_call = mutated_mod.get_global_var('func_5581')
call_5582 = func_5581_call()
output = call_5582
func_5583 = relay.Function([], output)
mutated_mod['func_5583'] = func_5583
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5590 = relay.var("var_5590", dtype = "uint16", shape = (1, 4, 11))#candidate|5590|(1, 4, 11)|var|uint16
var_5591 = relay.var("var_5591", dtype = "uint16", shape = (4, 4, 11))#candidate|5591|(4, 4, 11)|var|uint16
bop_5592 = relay.bitwise_or(var_5590.astype('uint16'), var_5591.astype('uint16')) # shape=(4, 4, 11)
func_4979_call = mod.get_global_var('func_4979')
func_4981_call = mutated_mod.get_global_var('func_4981')
call_5595 = relay.TupleGetItem(func_4979_call(), 1)
call_5596 = relay.TupleGetItem(func_4981_call(), 1)
func_3622_call = mod.get_global_var('func_3622')
func_3626_call = mutated_mod.get_global_var('func_3626')
var_5598 = relay.var("var_5598", dtype = "uint8", shape = (390, 3))#candidate|5598|(390, 3)|var|uint8
call_5597 = relay.TupleGetItem(func_3622_call(relay.reshape(var_5598.astype('uint8'), [1170,]), relay.reshape(var_5598.astype('uint8'), [1170,]), ), 1)
call_5599 = relay.TupleGetItem(func_3626_call(relay.reshape(var_5598.astype('uint8'), [1170,]), relay.reshape(var_5598.astype('uint8'), [1170,]), ), 1)
func_4038_call = mod.get_global_var('func_4038')
func_4042_call = mutated_mod.get_global_var('func_4042')
var_5611 = relay.var("var_5611", dtype = "float32", shape = (600,))#candidate|5611|(600,)|var|float32
call_5610 = relay.TupleGetItem(func_4038_call(relay.reshape(var_5611.astype('float32'), [10, 10, 6]), relay.reshape(var_5611.astype('float32'), [10, 10, 6]), ), 1)
call_5612 = relay.TupleGetItem(func_4042_call(relay.reshape(var_5611.astype('float32'), [10, 10, 6]), relay.reshape(var_5611.astype('float32'), [10, 10, 6]), ), 1)
uop_5616 = relay.tan(var_5591.astype('float64')) # shape=(4, 4, 11)
func_3964_call = mod.get_global_var('func_3964')
func_3966_call = mutated_mod.get_global_var('func_3966')
call_5620 = relay.TupleGetItem(func_3964_call(), 1)
call_5621 = relay.TupleGetItem(func_3966_call(), 1)
bop_5624 = relay.logical_or(uop_5616.astype('bool'), var_5590.astype('bool')) # shape=(4, 4, 11)
func_4156_call = mod.get_global_var('func_4156')
func_4158_call = mutated_mod.get_global_var('func_4158')
var_5629 = relay.var("var_5629", dtype = "float64", shape = (180,))#candidate|5629|(180,)|var|float64
call_5628 = relay.TupleGetItem(func_4156_call(relay.reshape(var_5629.astype('float64'), [3, 6, 10])), 0)
call_5630 = relay.TupleGetItem(func_4158_call(relay.reshape(var_5629.astype('float64'), [3, 6, 10])), 0)
func_2692_call = mod.get_global_var('func_2692')
func_2694_call = mutated_mod.get_global_var('func_2694')
call_5649 = relay.TupleGetItem(func_2692_call(), 0)
call_5650 = relay.TupleGetItem(func_2694_call(), 0)
func_3038_call = mod.get_global_var('func_3038')
func_3041_call = mutated_mod.get_global_var('func_3041')
call_5654 = relay.TupleGetItem(func_3038_call(relay.reshape(call_5597.astype('int8'), [15, 11, 6])), 0)
call_5655 = relay.TupleGetItem(func_3041_call(relay.reshape(call_5597.astype('int8'), [15, 11, 6])), 0)
bop_5659 = relay.floor_mod(uop_5616.astype('float64'), relay.reshape(var_5591.astype('float64'), relay.shape_of(uop_5616))) # shape=(4, 4, 11)
bop_5669 = relay.subtract(var_5590.astype('float32'), uop_5616.astype('float32')) # shape=(4, 4, 11)
output = relay.Tuple([bop_5592,call_5595,call_5597,var_5598,call_5610,var_5611,call_5620,bop_5624,call_5628,var_5629,call_5649,call_5654,bop_5659,bop_5669,])
output2 = relay.Tuple([bop_5592,call_5596,call_5599,var_5598,call_5612,var_5611,call_5621,bop_5624,call_5630,var_5629,call_5650,call_5655,bop_5659,bop_5669,])
func_5680 = relay.Function([var_5590,var_5591,var_5598,var_5611,var_5629,], output)
mod['func_5680'] = func_5680
mod = relay.transform.InferType()(mod)
mutated_mod['func_5680'] = func_5680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5680_call = mutated_mod.get_global_var('func_5680')
var_5682 = relay.var("var_5682", dtype = "uint16", shape = (1, 4, 11))#candidate|5682|(1, 4, 11)|var|uint16
var_5683 = relay.var("var_5683", dtype = "uint16", shape = (4, 4, 11))#candidate|5683|(4, 4, 11)|var|uint16
var_5684 = relay.var("var_5684", dtype = "uint8", shape = (390, 3))#candidate|5684|(390, 3)|var|uint8
var_5685 = relay.var("var_5685", dtype = "float32", shape = (600,))#candidate|5685|(600,)|var|float32
var_5686 = relay.var("var_5686", dtype = "float64", shape = (180,))#candidate|5686|(180,)|var|float64
call_5681 = func_5680_call(var_5682,var_5683,var_5684,var_5685,var_5686,)
output = call_5681
func_5687 = relay.Function([var_5682,var_5683,var_5684,var_5685,var_5686,], output)
mutated_mod['func_5687'] = func_5687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_5787 = relay.TupleGetItem(func_5267_call(), 1)
call_5788 = relay.TupleGetItem(func_5269_call(), 1)
output = call_5787
output2 = call_5788
func_5808 = relay.Function([], output)
mod['func_5808'] = func_5808
mod = relay.transform.InferType()(mod)
output = func_5808()
func_5809 = relay.Function([], output)
mutated_mod['func_5809'] = func_5809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5854 = relay.var("var_5854", dtype = "uint8", shape = (1, 9, 12))#candidate|5854|(1, 9, 12)|var|uint8
const_5855 = relay.const([[[-8,8,10,8,1,-7,9,3,9,-8,4,10],[-6,10,8,1,6,3,-1,6,-1,8,10,-1],[-7,-5,9,-6,10,3,4,3,-5,8,7,10],[6,9,9,8,1,8,-9,-4,-10,7,5,6],[4,6,7,-9,-3,-2,8,-8,-5,8,-1,-5],[3,5,-9,6,4,-5,7,7,-10,-2,-10,9],[7,1,10,-8,-7,-1,-5,-2,-10,-1,8,-8],[-8,-9,1,6,-5,-5,-5,10,-6,-10,7,-10],[-6,-5,-1,-5,3,9,-3,-3,6,-5,-9,-4]],[[-5,7,-4,-10,-10,-9,8,-9,-9,7,7,-10],[6,-3,10,3,2,9,7,-10,-4,7,2,-5],[6,3,-1,-6,10,-3,7,-8,-6,-6,-6,-1],[3,6,-5,6,-2,7,-6,10,2,-6,1,-9],[1,-1,2,-9,1,-2,-4,-10,-9,-2,1,1],[-7,-4,1,5,-3,-8,10,1,1,-10,4,-5],[-8,-10,-9,2,-9,6,4,-1,2,1,5,5],[-7,-4,6,6,6,-5,-8,-3,-5,-7,2,5],[5,6,-8,-9,8,8,3,-10,-3,-4,-1,-7]],[[7,7,-2,-5,-10,1,4,5,-3,7,-8,-3],[-1,-1,5,3,2,1,-4,-4,-9,-2,-5,4],[9,-4,-10,7,3,8,-4,9,-2,-3,-7,1],[-2,-9,-2,-4,6,-8,-4,-10,3,-6,8,4],[-6,-6,-3,-10,-2,1,6,6,3,10,1,6],[-7,-10,8,5,-2,-8,10,10,-9,-7,-8,8],[-7,1,-8,9,-9,-2,-2,10,10,8,8,-3],[3,-3,-2,-2,-7,8,-10,-3,-7,-6,2,4],[-6,1,2,-4,-5,-6,7,-10,3,-2,-7,3]],[[-7,-3,-7,-10,-1,8,6,-8,8,-2,4,-9],[-1,1,5,-10,-3,3,1,-2,6,-4,1,-7],[-10,1,-2,2,-3,-9,-8,-3,3,-10,1,5],[-1,10,-4,10,6,7,-4,-1,-3,5,9,-2],[-6,-7,6,4,2,1,1,-10,-3,-6,8,-3],[-8,-2,-8,1,9,-1,-9,-2,9,7,-5,8],[3,-4,-1,-2,7,8,-10,-9,5,4,3,7],[9,1,-2,-1,-2,8,4,-4,7,4,1,6],[3,1,6,-5,5,-9,4,-4,5,-4,5,9]],[[10,-9,9,6,-5,-8,-7,8,-1,-9,-6,-5],[-8,-1,-5,-4,4,-5,-9,4,9,9,-7,6],[-3,-4,9,-2,-6,-7,-3,-7,4,-1,4,9],[9,7,-6,-3,9,9,-7,-4,-6,-6,-4,8],[-7,-5,6,4,3,-3,-6,7,6,-5,7,-7],[-4,1,-6,-8,-10,1,6,-3,-7,-7,7,-10],[9,7,9,-10,5,-1,-2,3,3,-8,-9,9],[1,1,-9,2,-10,-6,3,10,-7,8,-1,1],[-4,2,-4,-1,8,-1,-7,-4,2,-4,8,-2]],[[6,-6,10,10,8,9,-4,7,4,-8,2,6],[4,8,5,-6,-9,-9,-10,5,10,2,-4,-3],[-6,9,-2,2,6,-7,10,-5,6,10,-10,5],[-10,-3,5,-5,6,-9,-1,-6,10,2,-9,-1],[-9,-2,-7,-1,6,-3,10,4,-4,-6,-3,-5],[-8,-3,4,-1,-4,-3,9,-9,-8,8,2,7],[4,-2,8,9,4,2,-7,-10,5,3,-9,-1],[-5,-8,10,3,-9,-10,-2,-2,3,4,-8,-3],[2,-8,-8,-10,9,-2,-1,2,1,6,1,10]],[[1,-3,10,3,4,3,-10,7,-10,10,-5,1],[2,-9,-3,-6,5,-5,-7,-9,10,3,6,1],[10,-7,-2,10,4,-9,-10,-3,-8,2,-9,-6],[-6,10,10,7,-1,-6,-1,-10,-8,3,-8,5],[-9,1,9,-6,6,-6,-7,10,-7,4,-5,-4],[5,-10,-6,-9,1,2,5,6,5,-2,7,10],[-8,-4,9,5,9,-7,10,9,-5,-3,10,4],[3,6,7,6,2,-8,9,-7,9,-3,-1,2],[5,6,7,9,-5,-10,2,-6,5,5,7,4]],[[7,7,-10,-2,6,-10,-8,-3,-5,3,-10,-2],[-5,2,-1,10,-4,6,5,10,-5,-4,-9,-6],[-1,-2,10,-9,4,-8,8,3,-6,7,-8,-3],[-9,-6,6,-3,-2,2,-10,8,-2,9,6,-3],[2,6,-9,2,9,-6,-1,4,3,-5,4,-9],[2,6,1,-2,9,4,10,6,8,-4,1,4],[1,9,5,-2,7,6,-7,-2,8,-6,3,-8],[6,-10,8,-2,-5,4,10,-6,-4,-2,1,-7],[1,-7,-5,-5,-7,-7,3,3,10,-8,3,-5]],[[6,-8,-5,-8,-8,1,4,-4,5,5,9,-5],[-5,-1,-7,-3,-6,-4,6,7,10,7,8,-2],[-1,10,-5,2,6,-8,10,9,-2,8,4,-2],[-5,-8,-10,-5,-9,2,-10,4,6,2,-3,3],[-2,5,-8,2,-8,8,1,1,-10,4,7,-7],[-9,-10,-8,10,-4,7,4,9,10,-1,3,-10],[5,5,1,-5,-1,-3,-8,10,-7,-5,-6,6],[2,-8,-1,9,10,8,-6,-2,-9,-5,-7,8],[3,7,-10,7,2,8,-2,9,-3,-5,-1,-3]],[[9,7,4,-10,-1,-6,1,4,9,-7,10,-4],[5,1,4,8,5,-1,-3,6,9,-4,5,4],[-1,-4,-8,-6,-8,3,-3,9,-6,-7,-1,-2],[4,1,-5,5,7,-9,-10,10,-3,1,-3,6],[-9,10,-5,-2,-8,10,1,1,5,-5,-6,2],[-7,9,-1,9,7,4,2,9,-1,5,-4,-2],[-6,-3,-9,6,-6,-5,-10,-1,-4,7,10,-7],[-6,-5,-9,-9,-1,1,-7,-7,4,2,-6,10],[-9,-7,-4,-4,-9,3,5,6,4,9,6,4]]], dtype = "uint8")#candidate|5855|(10, 9, 12)|const|uint8
bop_5856 = relay.minimum(var_5854.astype('uint8'), const_5855.astype('uint8')) # shape=(10, 9, 12)
output = bop_5856
output2 = bop_5856
func_5873 = relay.Function([var_5854,], output)
mod['func_5873'] = func_5873
mod = relay.transform.InferType()(mod)
mutated_mod['func_5873'] = func_5873
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5874 = relay.var("var_5874", dtype = "uint8", shape = (1, 9, 12))#candidate|5874|(1, 9, 12)|var|uint8
func_5873_call = mutated_mod.get_global_var('func_5873')
call_5875 = func_5873_call(var_5874)
output = call_5875
func_5876 = relay.Function([var_5874], output)
mutated_mod['func_5876'] = func_5876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3901_call = mod.get_global_var('func_3901')
func_3903_call = mutated_mod.get_global_var('func_3903')
call_5886 = relay.TupleGetItem(func_3901_call(), 0)
call_5887 = relay.TupleGetItem(func_3903_call(), 0)
output = relay.Tuple([call_5886,])
output2 = relay.Tuple([call_5887,])
func_5888 = relay.Function([], output)
mod['func_5888'] = func_5888
mod = relay.transform.InferType()(mod)
mutated_mod['func_5888'] = func_5888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5888_call = mutated_mod.get_global_var('func_5888')
call_5889 = func_5888_call()
output = call_5889
func_5890 = relay.Function([], output)
mutated_mod['func_5890'] = func_5890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5808_call = mod.get_global_var('func_5808')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_5896 = func_5808_call()
call_5897 = func_5808_call()
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_5904 = relay.TupleGetItem(func_4614_call(), 0)
call_5905 = relay.TupleGetItem(func_4615_call(), 0)
output = relay.Tuple([call_5896,call_5904,])
output2 = relay.Tuple([call_5897,call_5905,])
func_5918 = relay.Function([], output)
mod['func_5918'] = func_5918
mod = relay.transform.InferType()(mod)
output = func_5918()
func_5919 = relay.Function([], output)
mutated_mod['func_5919'] = func_5919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4344_call = mod.get_global_var('func_4344')
func_4346_call = mutated_mod.get_global_var('func_4346')
call_5963 = relay.TupleGetItem(func_4344_call(), 0)
call_5964 = relay.TupleGetItem(func_4346_call(), 0)
uop_5967 = relay.log2(call_5963.astype('float64')) # shape=(15, 11, 6)
uop_5969 = relay.log2(call_5964.astype('float64')) # shape=(15, 11, 6)
bop_5975 = relay.divide(uop_5967.astype('float64'), relay.reshape(call_5963.astype('float64'), relay.shape_of(uop_5967))) # shape=(15, 11, 6)
bop_5978 = relay.divide(uop_5969.astype('float64'), relay.reshape(call_5964.astype('float64'), relay.shape_of(uop_5969))) # shape=(15, 11, 6)
output = relay.Tuple([bop_5975,])
output2 = relay.Tuple([bop_5978,])
func_5979 = relay.Function([], output)
mod['func_5979'] = func_5979
mod = relay.transform.InferType()(mod)
output = func_5979()
func_5980 = relay.Function([], output)
mutated_mod['func_5980'] = func_5980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mod.get_global_var('func_3069')
func_3071_call = mutated_mod.get_global_var('func_3071')
call_5997 = relay.TupleGetItem(func_3069_call(), 0)
call_5998 = relay.TupleGetItem(func_3071_call(), 0)
uop_6001 = relay.sigmoid(call_5997.astype('float64')) # shape=(90,)
uop_6003 = relay.sigmoid(call_5998.astype('float64')) # shape=(90,)
func_5123_call = mod.get_global_var('func_5123')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_6005 = relay.TupleGetItem(func_5123_call(), 0)
call_6006 = relay.TupleGetItem(func_5124_call(), 0)
output = relay.Tuple([uop_6001,call_6005,])
output2 = relay.Tuple([uop_6003,call_6006,])
func_6007 = relay.Function([], output)
mod['func_6007'] = func_6007
mod = relay.transform.InferType()(mod)
mutated_mod['func_6007'] = func_6007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6007_call = mutated_mod.get_global_var('func_6007')
call_6008 = func_6007_call()
output = call_6008
func_6009 = relay.Function([], output)
mutated_mod['func_6009'] = func_6009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5016_call = mod.get_global_var('func_5016')
func_5018_call = mutated_mod.get_global_var('func_5018')
call_6020 = relay.TupleGetItem(func_5016_call(), 0)
call_6021 = relay.TupleGetItem(func_5018_call(), 0)
uop_6026 = relay.sigmoid(call_6020.astype('float64')) # shape=(15, 11, 6)
uop_6028 = relay.sigmoid(call_6021.astype('float64')) # shape=(15, 11, 6)
func_3622_call = mod.get_global_var('func_3622')
func_3626_call = mutated_mod.get_global_var('func_3626')
var_6033 = relay.var("var_6033", dtype = "uint8", shape = (130, 9))#candidate|6033|(130, 9)|var|uint8
call_6032 = relay.TupleGetItem(func_3622_call(relay.reshape(var_6033.astype('uint8'), [1170,]), relay.reshape(var_6033.astype('uint8'), [1170,]), ), 3)
call_6034 = relay.TupleGetItem(func_3626_call(relay.reshape(var_6033.astype('uint8'), [1170,]), relay.reshape(var_6033.astype('uint8'), [1170,]), ), 3)
func_4276_call = mod.get_global_var('func_4276')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_6038 = relay.TupleGetItem(func_4276_call(), 0)
call_6039 = relay.TupleGetItem(func_4278_call(), 0)
output = relay.Tuple([uop_6026,call_6032,var_6033,call_6038,])
output2 = relay.Tuple([uop_6028,call_6034,var_6033,call_6039,])
func_6044 = relay.Function([var_6033,], output)
mod['func_6044'] = func_6044
mod = relay.transform.InferType()(mod)
var_6045 = relay.var("var_6045", dtype = "uint8", shape = (130, 9))#candidate|6045|(130, 9)|var|uint8
output = func_6044(var_6045)
func_6046 = relay.Function([var_6045], output)
mutated_mod['func_6046'] = func_6046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2692_call = mod.get_global_var('func_2692')
func_2694_call = mutated_mod.get_global_var('func_2694')
call_6098 = relay.TupleGetItem(func_2692_call(), 0)
call_6099 = relay.TupleGetItem(func_2694_call(), 0)
output = call_6098
output2 = call_6099
func_6105 = relay.Function([], output)
mod['func_6105'] = func_6105
mod = relay.transform.InferType()(mod)
mutated_mod['func_6105'] = func_6105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6105_call = mutated_mod.get_global_var('func_6105')
call_6106 = func_6105_call()
output = call_6106
func_6107 = relay.Function([], output)
mutated_mod['func_6107'] = func_6107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6105_call = mod.get_global_var('func_6105')
func_6107_call = mutated_mod.get_global_var('func_6107')
call_6150 = func_6105_call()
call_6151 = func_6105_call()
output = call_6150
output2 = call_6151
func_6152 = relay.Function([], output)
mod['func_6152'] = func_6152
mod = relay.transform.InferType()(mod)
output = func_6152()
func_6153 = relay.Function([], output)
mutated_mod['func_6153'] = func_6153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3964_call = mod.get_global_var('func_3964')
func_3966_call = mutated_mod.get_global_var('func_3966')
call_6167 = relay.TupleGetItem(func_3964_call(), 0)
call_6168 = relay.TupleGetItem(func_3966_call(), 0)
uop_6172 = relay.exp(call_6167.astype('float32')) # shape=(15, 11, 6)
uop_6174 = relay.exp(call_6168.astype('float32')) # shape=(15, 11, 6)
func_3540_call = mod.get_global_var('func_3540')
func_3542_call = mutated_mod.get_global_var('func_3542')
call_6185 = func_3540_call()
call_6186 = func_3540_call()
func_3997_call = mod.get_global_var('func_3997')
func_3999_call = mutated_mod.get_global_var('func_3999')
var_6198 = relay.var("var_6198", dtype = "int32", shape = ())#candidate|6198|()|var|int32
call_6197 = relay.TupleGetItem(func_3997_call(relay.reshape(var_6198.astype('int32'), [])), 2)
call_6199 = relay.TupleGetItem(func_3999_call(relay.reshape(var_6198.astype('int32'), [])), 2)
func_3138_call = mod.get_global_var('func_3138')
func_3139_call = mutated_mod.get_global_var('func_3139')
call_6202 = func_3138_call()
call_6203 = func_3138_call()
func_5680_call = mod.get_global_var('func_5680')
func_5687_call = mutated_mod.get_global_var('func_5687')
const_6207 = relay.const([5,-4,2,5,4,-3,-2,-10,-2,-5,4,-8,-10,8,6,-6,5,10,-7,9,10,-2,-6,5,7,-6,7,-10,9,-3,-9,-8,2,4,-2,3,-5,-6,-5,9,-1,3,-7,7], dtype = "uint16")#candidate|6207|(44,)|const|uint16
var_6208 = relay.var("var_6208", dtype = "uint16", shape = (176,))#candidate|6208|(176,)|var|uint16
var_6209 = relay.var("var_6209", dtype = "uint8", shape = (1170,))#candidate|6209|(1170,)|var|uint8
var_6210 = relay.var("var_6210", dtype = "float32", shape = (600,))#candidate|6210|(600,)|var|float32
var_6211 = relay.var("var_6211", dtype = "float64", shape = (180,))#candidate|6211|(180,)|var|float64
call_6206 = relay.TupleGetItem(func_5680_call(relay.reshape(const_6207.astype('uint16'), [1, 4, 11]), relay.reshape(var_6208.astype('uint16'), [4, 4, 11]), relay.reshape(var_6209.astype('uint8'), [390, 3]), relay.reshape(var_6210.astype('float32'), [600,]), relay.reshape(var_6211.astype('float64'), [180,]), ), 6)
call_6212 = relay.TupleGetItem(func_5687_call(relay.reshape(const_6207.astype('uint16'), [1, 4, 11]), relay.reshape(var_6208.astype('uint16'), [4, 4, 11]), relay.reshape(var_6209.astype('uint8'), [390, 3]), relay.reshape(var_6210.astype('float32'), [600,]), relay.reshape(var_6211.astype('float64'), [180,]), ), 6)
func_4446_call = mod.get_global_var('func_4446')
func_4448_call = mutated_mod.get_global_var('func_4448')
call_6213 = func_4446_call()
call_6214 = func_4446_call()
const_6219 = relay.const([[[9.861607,2.493317,-1.653053,-5.005439,3.548953,-2.373114],[9.805661,3.600643,1.212038,4.041848,-5.753730,3.186410],[0.253825,7.546311,2.178422,-7.237934,-2.839225,-2.997125],[3.414514,7.951732,1.313686,-6.382061,4.722144,8.720183],[-0.006535,-5.638548,5.512584,8.543339,-6.781057,-7.170524],[-4.977027,-2.820321,6.928702,8.266823,1.883021,8.884500],[-8.114712,-0.760365,6.639552,-9.059485,-5.688220,9.115847],[-1.765547,-6.941259,2.111407,1.551912,2.689958,6.323921],[-4.396101,4.198075,9.829293,1.588586,5.350909,9.185859],[1.808355,-0.878383,-5.287894,0.176271,-7.137163,6.139950],[1.366714,1.203930,5.424192,2.140276,4.361017,6.933478]],[[8.941941,8.405757,-5.970100,-1.069558,-3.886673,-6.259986],[-8.089606,-9.721195,5.523435,-2.856234,-4.371788,-7.486132],[-1.849123,8.076190,-8.886543,-8.615912,3.710838,-2.659909],[2.820431,-3.055681,9.292337,-0.230219,-7.150158,7.339442],[3.378505,-1.955928,6.398725,1.951459,-8.019452,-0.421744],[5.839913,9.775190,-4.214200,1.090642,-2.401524,9.894187],[-3.974238,5.927860,-4.373120,-3.842086,-4.321375,7.112992],[8.206490,-5.377321,-8.562546,1.876418,7.757175,-3.575355],[-8.961031,4.722647,5.556115,7.069348,8.917090,2.792499],[2.354206,3.092809,-7.454926,8.254377,7.542971,-4.077626],[-0.762365,2.772432,-9.748667,1.003208,2.532229,8.838461]],[[-9.778063,-8.392662,7.823367,2.320271,-8.980407,-6.271576],[-6.096559,-0.648173,9.063804,7.234363,-6.044820,-7.775362],[-9.350920,-9.099361,-7.873708,7.461031,-7.041278,-7.504520],[3.485633,-2.581599,-1.131940,-1.966100,-1.103804,-8.444810],[7.447182,-4.156901,5.681747,-5.692195,-4.521558,7.259534],[-4.459057,8.888738,6.249645,-4.518373,-0.398439,-6.174456],[-4.727956,3.203551,6.011248,-6.594218,9.307764,3.016488],[1.715270,-3.811999,-5.955275,3.328990,-2.269196,5.778333],[-4.627809,-4.776329,-0.391812,-5.244690,-1.809064,5.005723],[6.090652,-4.385627,-9.384668,9.004261,-8.484989,-0.866794],[-4.129324,8.185047,-6.994384,-3.017570,1.007533,4.024114]],[[8.735013,-1.913810,2.676549,5.091109,7.721673,8.890836],[5.398165,-8.778153,4.066145,-4.871053,-7.730212,-2.336125],[-6.662722,0.542373,-6.651080,9.643850,-6.353697,1.321376],[-2.861034,5.921754,-5.207427,6.872688,6.091362,0.396093],[-7.918874,-1.825218,-8.825178,-4.911359,7.675446,-5.569226],[-1.061622,0.017382,2.586123,0.958934,-1.607041,6.845178],[1.276442,-7.302441,-3.855202,7.556409,-2.886930,9.209339],[7.334785,1.906702,-5.214036,-7.244610,-9.799210,9.696611],[-8.767093,8.618524,2.254755,6.826465,5.034476,-6.485746],[-8.416033,7.893041,1.448571,8.573001,-6.676869,-3.485148],[-1.260644,3.004469,-3.166175,-9.529592,7.493449,1.482115]],[[-2.956757,-5.581436,5.403210,-1.568409,-8.011939,-8.166509],[-2.357431,-4.619036,-2.478208,4.444911,5.452246,7.133403],[-2.208760,-2.046018,4.715300,-1.296083,5.812544,-6.219820],[2.696340,-0.947832,-2.663224,-0.483375,-5.728395,1.970236],[3.962167,0.990431,2.140308,-4.837980,-6.152263,-7.015740],[7.032597,6.221561,7.629359,6.130864,-8.006788,-8.341172],[-3.354712,-6.423628,-3.246572,9.500123,-4.511397,-1.465358],[-2.375869,7.788571,-7.393772,-9.001898,6.436507,-2.939791],[8.911710,5.693069,2.165140,-7.368972,-6.482914,-2.784081],[-9.951617,-2.966037,-2.108151,9.714267,-6.249641,1.589034],[-7.835701,-4.461654,5.213469,-7.526784,-6.051680,2.729589]],[[1.301002,4.367186,-0.705200,-6.263665,5.786807,5.202324],[-3.403383,-6.866322,-4.887769,6.165820,-7.136502,-1.907152],[-9.419755,-5.283513,-8.562014,-4.696780,-8.051642,-0.812693],[8.508734,2.360213,0.848001,-6.984642,6.115467,-2.598504],[-4.004410,-5.875990,8.444543,-3.943781,3.987828,-8.955253],[-1.974553,-6.457497,-3.129466,6.868401,9.024591,9.667389],[-0.953568,-9.463711,-4.683296,8.058693,-8.829271,6.458419],[-8.769020,8.769306,3.918982,0.839960,-7.321123,-9.001300],[-0.235691,-4.496154,-3.980170,2.892948,2.526108,2.311657],[-9.086078,-5.211936,-1.336988,1.612109,-0.992558,9.685957],[-6.226879,7.542807,-7.494401,-0.866569,-5.480249,-8.963160]],[[-5.161440,0.670661,-5.161834,6.403357,6.776392,7.860900],[-5.982599,-0.564198,-0.358195,-4.701315,-0.626222,1.973414],[0.371137,-9.975376,8.182863,-2.061930,-6.156053,0.326383],[-9.309391,5.480643,1.909163,-9.421659,7.527687,-7.637241],[-6.359095,4.524786,-6.059209,5.632602,-8.726036,8.880093],[-4.415181,4.371409,8.431509,4.820477,9.330114,8.455073],[-0.501976,-8.803637,-7.089781,5.715329,5.110367,-7.386594],[5.630294,8.848128,7.091924,9.258711,8.819968,-9.288668],[-5.235123,-0.685483,-7.252865,-7.442264,2.712694,1.067035],[5.756377,-9.025881,9.514970,-5.571751,-8.611284,-1.218747],[4.241489,-3.855022,-4.780590,3.371054,-0.096119,-3.873506]],[[-2.158633,1.262605,-6.915926,7.820833,2.100136,-3.782122],[-2.874995,-5.658377,3.147796,-1.967236,-1.939653,8.273506],[6.409629,9.710782,-7.174403,0.987211,-7.492158,2.921717],[1.242527,-1.513016,-2.390953,1.370724,-2.240493,-2.631747],[-4.461160,-7.074778,5.158647,9.084540,-6.027847,-4.149697],[-1.492930,0.573289,7.117943,5.209122,-4.106490,3.825698],[5.195080,5.602622,-9.995949,2.258089,2.815195,-6.319595],[4.705033,6.077371,-1.269370,-9.208049,1.796103,-5.639741],[-1.320659,0.571589,9.626161,-8.606096,7.718442,-2.777035],[2.833791,-1.153806,0.605106,9.707418,-3.002460,8.047635],[-2.063410,-3.534050,1.008566,-4.106214,-9.003696,-3.202246]],[[4.072170,-7.142777,1.141365,-7.162628,-7.115633,2.294964],[9.852387,-5.938523,9.358114,9.665653,-5.266738,-9.384663],[-8.193704,6.969200,-2.623371,-3.079391,-8.330435,6.098505],[-5.006022,-2.581580,-8.814909,-6.192761,-4.303879,-6.899272],[-8.386185,-1.612632,2.600850,3.120326,6.147822,-5.279939],[-3.952088,4.999048,-7.381156,-7.062003,1.673186,5.966839],[-4.346505,0.190314,7.407189,0.406534,5.830526,-8.360700],[-2.954800,-5.106390,-0.730275,2.820858,-5.702978,-4.749045],[4.479954,7.761079,5.414315,0.368787,-2.936969,2.101964],[-2.412723,-1.621082,-1.516386,-0.198754,-4.552816,-4.388734],[5.409664,2.594231,6.671641,-5.863422,9.758674,1.605460]],[[2.286352,-0.928417,0.288916,9.166045,-2.925193,-9.836872],[-0.077318,4.156416,4.516963,5.055165,-8.061015,-9.013755],[-5.908449,-5.298117,-3.137597,9.323689,-5.180341,-5.897718],[6.109399,3.831637,0.440064,-4.803943,-8.390310,-1.025866],[1.190346,0.936662,-3.740507,4.929985,-7.594392,-6.745420],[7.506127,-4.077274,-9.513673,-4.927678,-7.569837,1.627555],[6.835981,3.460883,-9.499834,4.169641,-7.372745,5.994099],[2.523674,5.894947,-3.167007,-9.342240,2.073080,-2.169276],[5.637295,8.746714,-1.367505,4.238922,-7.156168,-1.176334],[-5.686761,0.205032,-2.583430,-9.885916,4.863117,2.163944],[4.072728,-6.445760,1.143835,-6.807198,2.991570,-6.290536]],[[2.577934,6.873055,6.755711,-7.303177,0.743613,-1.621600],[-0.665498,6.305613,-1.431255,8.368038,3.772666,6.190107],[-4.267671,6.315863,5.183661,-3.665306,-5.499026,1.076381],[6.445667,7.081943,8.317378,-4.527044,-5.714286,2.447839],[-7.711973,5.247710,-3.381081,-7.438273,-1.050076,-4.382194],[-2.690356,-4.087872,-6.141012,-6.685154,1.043831,9.258324],[0.335185,-4.877170,7.405261,-0.999131,5.448023,0.529122],[-2.520974,-7.296066,-4.352486,4.911733,8.429004,2.803666],[4.961300,0.248919,0.910756,9.153978,-0.097266,4.109281],[4.156175,-0.708284,9.811701,8.969038,0.011502,-5.994644],[-1.195544,-5.680647,-2.764130,-4.998375,3.926866,-4.273447]],[[-2.109350,9.981951,-6.055793,-7.650645,3.565432,-6.996780],[1.881117,-3.958864,3.804832,-5.479305,-3.098807,-1.997330],[-5.128156,-8.407449,-2.529380,-3.181333,-3.244909,-7.617101],[-3.838399,2.929644,3.040687,-7.901423,5.268562,7.792957],[-7.129694,-6.651278,5.731150,5.568276,7.445020,1.427717],[-8.008701,-8.275391,-0.095925,0.672978,-2.470846,-4.902468],[-7.097113,-8.322756,9.018188,5.992494,5.577102,1.690140],[-7.095437,-8.965548,-6.014278,7.211477,8.778680,-2.921450],[-9.541549,3.966931,-9.351631,-1.120559,-9.947830,-9.333235],[8.646575,9.127494,8.967019,6.403817,5.360181,-8.276638],[8.062584,3.952148,4.270664,-8.604805,9.858864,-8.995838]],[[3.522516,0.963409,2.123126,-2.874091,9.357134,7.781318],[-0.464852,-1.286724,-3.405559,4.916351,-0.668361,9.765644],[-8.340277,-5.646199,7.764526,3.876651,5.554956,-1.108438],[-3.977276,4.248311,9.431527,7.196458,5.562865,0.110139],[-3.672176,-6.589332,2.498920,-3.857364,0.178874,-5.201429],[-6.427356,-6.184858,-2.057665,-8.146583,0.488830,-8.258529],[5.776659,-3.437076,8.290420,-2.100655,-6.855643,-4.145671],[-8.200405,-9.792934,0.523057,-9.648632,-1.316375,-6.481315],[-0.433477,-4.760760,-1.423985,-1.289526,-8.424554,5.597928],[-6.369751,3.381116,-5.104040,9.481602,-5.050622,-7.092071],[-5.205040,1.983154,4.867613,1.879306,2.212722,0.948101]],[[-9.333841,6.710063,-8.272392,-3.212759,-7.429072,-5.861132],[8.522378,-9.691578,4.135021,-1.018167,8.941203,-3.498069],[2.276006,-3.471555,6.422758,-6.049706,9.769084,-6.169155],[-4.413785,0.866827,-5.347441,3.057462,2.917098,-1.480703],[5.702576,-9.403011,-4.993388,3.831802,-4.793545,-4.207259],[-8.850391,8.527891,-0.085418,2.650404,-8.578642,-8.224759],[-4.734003,-2.178714,7.923930,-3.838683,2.542504,2.684734],[-0.555524,5.743183,1.567632,-9.458441,6.428091,8.922470],[-5.331517,-4.431202,8.094715,3.458278,2.300001,8.753300],[-0.292624,6.453139,-5.796863,-9.492591,3.040083,9.128922],[8.468724,-2.630005,8.903977,3.455166,5.893168,-7.436044]],[[-7.271477,-4.089639,-6.755111,-9.247545,-2.198620,-3.509337],[-2.384649,3.709475,7.342563,-4.148796,-7.072313,7.189997],[2.693108,1.865489,-3.043418,5.373393,-9.772970,-8.793716],[-0.634684,0.441624,-7.865415,6.357518,-6.584675,6.317882],[-9.807140,1.027761,-4.366393,-2.563675,1.723483,-8.008908],[-1.470257,-5.223970,-9.373186,4.284170,0.267715,1.937491],[-3.139781,-9.879212,7.710541,-1.655999,-4.482195,-2.578034],[-7.052958,-6.522842,9.437127,-6.277810,-1.578843,-2.291671],[3.360637,1.922311,-2.441987,9.672281,-8.088365,-0.393715],[6.581925,8.762973,-8.244809,-0.270146,-9.608584,-1.056498],[-4.095211,6.197454,7.536431,7.071994,5.922295,1.343720]]], dtype = "float32")#candidate|6219|(15, 11, 6)|const|float32
bop_6220 = relay.left_shift(uop_6172.astype('uint32'), relay.reshape(const_6219.astype('uint32'), relay.shape_of(uop_6172))) # shape=(15, 11, 6)
bop_6223 = relay.left_shift(uop_6174.astype('uint32'), relay.reshape(const_6219.astype('uint32'), relay.shape_of(uop_6174))) # shape=(15, 11, 6)
func_5302_call = mod.get_global_var('func_5302')
func_5305_call = mutated_mod.get_global_var('func_5305')
var_6240 = relay.var("var_6240", dtype = "float64", shape = (140,))#candidate|6240|(140,)|var|float64
call_6239 = relay.TupleGetItem(func_5302_call(relay.reshape(var_6240.astype('float64'), [10, 2, 7])), 3)
call_6241 = relay.TupleGetItem(func_5305_call(relay.reshape(var_6240.astype('float64'), [10, 2, 7])), 3)
func_5302_call = mod.get_global_var('func_5302')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_6247 = relay.TupleGetItem(func_5302_call(relay.reshape(var_6240.astype('float64'), [10, 2, 7])), 3)
call_6248 = relay.TupleGetItem(func_5305_call(relay.reshape(var_6240.astype('float64'), [10, 2, 7])), 3)
func_6105_call = mod.get_global_var('func_6105')
func_6107_call = mutated_mod.get_global_var('func_6107')
call_6249 = func_6105_call()
call_6250 = func_6105_call()
output = relay.Tuple([call_6185,call_6197,var_6198,call_6202,call_6206,const_6207,var_6208,var_6209,var_6210,var_6211,call_6213,bop_6220,call_6239,var_6240,call_6247,call_6249,])
output2 = relay.Tuple([call_6186,call_6199,var_6198,call_6203,call_6212,const_6207,var_6208,var_6209,var_6210,var_6211,call_6214,bop_6223,call_6241,var_6240,call_6248,call_6250,])
func_6253 = relay.Function([var_6198,var_6208,var_6209,var_6210,var_6211,var_6240,], output)
mod['func_6253'] = func_6253
mod = relay.transform.InferType()(mod)
mutated_mod['func_6253'] = func_6253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6253_call = mutated_mod.get_global_var('func_6253')
var_6255 = relay.var("var_6255", dtype = "int32", shape = ())#candidate|6255|()|var|int32
var_6256 = relay.var("var_6256", dtype = "uint16", shape = (176,))#candidate|6256|(176,)|var|uint16
var_6257 = relay.var("var_6257", dtype = "uint8", shape = (1170,))#candidate|6257|(1170,)|var|uint8
var_6258 = relay.var("var_6258", dtype = "float32", shape = (600,))#candidate|6258|(600,)|var|float32
var_6259 = relay.var("var_6259", dtype = "float64", shape = (180,))#candidate|6259|(180,)|var|float64
var_6260 = relay.var("var_6260", dtype = "float64", shape = (140,))#candidate|6260|(140,)|var|float64
call_6254 = func_6253_call(var_6255,var_6256,var_6257,var_6258,var_6259,var_6260,)
output = call_6254
func_6261 = relay.Function([var_6255,var_6256,var_6257,var_6258,var_6259,var_6260,], output)
mutated_mod['func_6261'] = func_6261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6105_call = mod.get_global_var('func_6105')
func_6107_call = mutated_mod.get_global_var('func_6107')
call_6263 = func_6105_call()
call_6264 = func_6105_call()
func_4221_call = mod.get_global_var('func_4221')
func_4222_call = mutated_mod.get_global_var('func_4222')
call_6272 = func_4221_call()
call_6273 = func_4221_call()
bop_6275 = relay.multiply(call_6263.astype('uint64'), relay.reshape(call_6272.astype('uint64'), relay.shape_of(call_6263))) # shape=(15, 11, 6)
bop_6278 = relay.multiply(call_6264.astype('uint64'), relay.reshape(call_6273.astype('uint64'), relay.shape_of(call_6264))) # shape=(15, 11, 6)
uop_6295 = relay.log(call_6263.astype('float32')) # shape=(15, 11, 6)
uop_6297 = relay.log(call_6264.astype('float32')) # shape=(15, 11, 6)
output = relay.Tuple([bop_6275,uop_6295,])
output2 = relay.Tuple([bop_6278,uop_6297,])
func_6302 = relay.Function([], output)
mod['func_6302'] = func_6302
mod = relay.transform.InferType()(mod)
mutated_mod['func_6302'] = func_6302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6302_call = mutated_mod.get_global_var('func_6302')
call_6303 = func_6302_call()
output = call_6303
func_6304 = relay.Function([], output)
mutated_mod['func_6304'] = func_6304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4376_call = mod.get_global_var('func_4376')
func_4377_call = mutated_mod.get_global_var('func_4377')
call_6332 = relay.TupleGetItem(func_4376_call(), 0)
call_6333 = relay.TupleGetItem(func_4377_call(), 0)
output = call_6332
output2 = call_6333
func_6337 = relay.Function([], output)
mod['func_6337'] = func_6337
mod = relay.transform.InferType()(mod)
output = func_6337()
func_6338 = relay.Function([], output)
mutated_mod['func_6338'] = func_6338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2692_call = mod.get_global_var('func_2692')
func_2694_call = mutated_mod.get_global_var('func_2694')
call_6351 = relay.TupleGetItem(func_2692_call(), 0)
call_6352 = relay.TupleGetItem(func_2694_call(), 0)
func_3304_call = mod.get_global_var('func_3304')
func_3307_call = mutated_mod.get_global_var('func_3307')
var_6359 = relay.var("var_6359", dtype = "uint8", shape = (32, 8))#candidate|6359|(32, 8)|var|uint8
call_6358 = relay.TupleGetItem(func_3304_call(relay.reshape(var_6359.astype('uint8'), [2, 16, 8]), relay.reshape(var_6359.astype('uint8'), [2, 16, 8]), ), 5)
call_6360 = relay.TupleGetItem(func_3307_call(relay.reshape(var_6359.astype('uint8'), [2, 16, 8]), relay.reshape(var_6359.astype('uint8'), [2, 16, 8]), ), 5)
func_4344_call = mod.get_global_var('func_4344')
func_4346_call = mutated_mod.get_global_var('func_4346')
call_6361 = relay.TupleGetItem(func_4344_call(), 0)
call_6362 = relay.TupleGetItem(func_4346_call(), 0)
func_5888_call = mod.get_global_var('func_5888')
func_5890_call = mutated_mod.get_global_var('func_5890')
call_6364 = relay.TupleGetItem(func_5888_call(), 0)
call_6365 = relay.TupleGetItem(func_5890_call(), 0)
output = relay.Tuple([call_6351,call_6358,var_6359,call_6361,call_6364,])
output2 = relay.Tuple([call_6352,call_6360,var_6359,call_6362,call_6365,])
func_6369 = relay.Function([var_6359,], output)
mod['func_6369'] = func_6369
mod = relay.transform.InferType()(mod)
var_6370 = relay.var("var_6370", dtype = "uint8", shape = (32, 8))#candidate|6370|(32, 8)|var|uint8
output = func_6369(var_6370)
func_6371 = relay.Function([var_6370], output)
mutated_mod['func_6371'] = func_6371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3138_call = mod.get_global_var('func_3138')
func_3139_call = mutated_mod.get_global_var('func_3139')
call_6381 = func_3138_call()
call_6382 = func_3138_call()
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_6395 = relay.TupleGetItem(func_5512_call(), 0)
call_6396 = relay.TupleGetItem(func_5513_call(), 0)
output = relay.Tuple([call_6381,call_6395,])
output2 = relay.Tuple([call_6382,call_6396,])
func_6399 = relay.Function([], output)
mod['func_6399'] = func_6399
mod = relay.transform.InferType()(mod)
mutated_mod['func_6399'] = func_6399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6399_call = mutated_mod.get_global_var('func_6399')
call_6400 = func_6399_call()
output = call_6400
func_6401 = relay.Function([], output)
mutated_mod['func_6401'] = func_6401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5016_call = mod.get_global_var('func_5016')
func_5018_call = mutated_mod.get_global_var('func_5018')
call_6408 = relay.TupleGetItem(func_5016_call(), 0)
call_6409 = relay.TupleGetItem(func_5018_call(), 0)
output = call_6408
output2 = call_6409
func_6427 = relay.Function([], output)
mod['func_6427'] = func_6427
mod = relay.transform.InferType()(mod)
mutated_mod['func_6427'] = func_6427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6427_call = mutated_mod.get_global_var('func_6427')
call_6428 = func_6427_call()
output = call_6428
func_6429 = relay.Function([], output)
mutated_mod['func_6429'] = func_6429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5918_call = mod.get_global_var('func_5918')
func_5919_call = mutated_mod.get_global_var('func_5919')
call_6443 = relay.TupleGetItem(func_5918_call(), 0)
call_6444 = relay.TupleGetItem(func_5919_call(), 0)
func_6302_call = mod.get_global_var('func_6302')
func_6304_call = mutated_mod.get_global_var('func_6304')
call_6445 = relay.TupleGetItem(func_6302_call(), 1)
call_6446 = relay.TupleGetItem(func_6304_call(), 1)
output = relay.Tuple([call_6443,call_6445,])
output2 = relay.Tuple([call_6444,call_6446,])
func_6450 = relay.Function([], output)
mod['func_6450'] = func_6450
mod = relay.transform.InferType()(mod)
output = func_6450()
func_6451 = relay.Function([], output)
mutated_mod['func_6451'] = func_6451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_6467 = relay.TupleGetItem(func_3508_call(), 0)
call_6468 = relay.TupleGetItem(func_3509_call(), 0)
func_4038_call = mod.get_global_var('func_4038')
func_4042_call = mutated_mod.get_global_var('func_4042')
var_6474 = relay.var("var_6474", dtype = "float32", shape = (12, 50))#candidate|6474|(12, 50)|var|float32
call_6473 = relay.TupleGetItem(func_4038_call(relay.reshape(var_6474.astype('float32'), [10, 10, 6]), relay.reshape(var_6474.astype('float32'), [10, 10, 6]), ), 0)
call_6475 = relay.TupleGetItem(func_4042_call(relay.reshape(var_6474.astype('float32'), [10, 10, 6]), relay.reshape(var_6474.astype('float32'), [10, 10, 6]), ), 0)
output = relay.Tuple([call_6467,call_6473,var_6474,])
output2 = relay.Tuple([call_6468,call_6475,var_6474,])
func_6488 = relay.Function([var_6474,], output)
mod['func_6488'] = func_6488
mod = relay.transform.InferType()(mod)
var_6489 = relay.var("var_6489", dtype = "float32", shape = (12, 50))#candidate|6489|(12, 50)|var|float32
output = func_6488(var_6489)
func_6490 = relay.Function([var_6489], output)
mutated_mod['func_6490'] = func_6490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_6541 = relay.TupleGetItem(func_5267_call(), 1)
call_6542 = relay.TupleGetItem(func_5269_call(), 1)
func_4376_call = mod.get_global_var('func_4376')
func_4377_call = mutated_mod.get_global_var('func_4377')
call_6561 = relay.TupleGetItem(func_4376_call(), 0)
call_6562 = relay.TupleGetItem(func_4377_call(), 0)
output = relay.Tuple([call_6541,call_6561,])
output2 = relay.Tuple([call_6542,call_6562,])
func_6571 = relay.Function([], output)
mod['func_6571'] = func_6571
mod = relay.transform.InferType()(mod)
output = func_6571()
func_6572 = relay.Function([], output)
mutated_mod['func_6572'] = func_6572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_6584 = relay.TupleGetItem(func_4503_call(), 0)
call_6585 = relay.TupleGetItem(func_4505_call(), 0)
output = call_6584
output2 = call_6585
func_6587 = relay.Function([], output)
mod['func_6587'] = func_6587
mod = relay.transform.InferType()(mod)
output = func_6587()
func_6588 = relay.Function([], output)
mutated_mod['func_6588'] = func_6588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4221_call = mod.get_global_var('func_4221')
func_4222_call = mutated_mod.get_global_var('func_4222')
call_6605 = func_4221_call()
call_6606 = func_4221_call()
output = call_6605
output2 = call_6606
func_6613 = relay.Function([], output)
mod['func_6613'] = func_6613
mod = relay.transform.InferType()(mod)
output = func_6613()
func_6614 = relay.Function([], output)
mutated_mod['func_6614'] = func_6614
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6626 = relay.const([[[4.120231],[-6.274653],[2.850106],[8.165601],[-2.388922],[-5.617143],[-0.961683],[0.609533],[-8.428345],[-2.433949],[-0.843197],[-3.235951],[9.433458],[-4.522234],[-1.574946]],[[-6.768436],[5.542520],[1.969348],[2.612195],[6.996420],[-5.372709],[1.651658],[5.881435],[-8.608791],[0.312665],[3.647434],[5.878697],[1.558746],[-9.072829],[2.258539]],[[-5.177558],[-9.027470],[-0.326936],[-5.796264],[-0.194275],[6.226130],[-0.091952],[2.360195],[-7.926882],[1.883435],[-8.316723],[0.362457],[-8.994267],[9.286247],[-3.606548]]], dtype = "float64")#candidate|6626|(3, 15, 1)|const|float64
var_6627 = relay.var("var_6627", dtype = "float64", shape = (3, 15, 15))#candidate|6627|(3, 15, 15)|var|float64
bop_6628 = relay.power(const_6626.astype('float64'), var_6627.astype('float64')) # shape=(3, 15, 15)
func_2824_call = mod.get_global_var('func_2824')
func_2826_call = mutated_mod.get_global_var('func_2826')
call_6634 = relay.TupleGetItem(func_2824_call(), 0)
call_6635 = relay.TupleGetItem(func_2826_call(), 0)
func_2401_call = mod.get_global_var('func_2401')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_6642 = func_2401_call()
call_6643 = func_2401_call()
func_6152_call = mod.get_global_var('func_6152')
func_6153_call = mutated_mod.get_global_var('func_6153')
call_6655 = func_6152_call()
call_6656 = func_6152_call()
output = relay.Tuple([bop_6628,call_6634,call_6642,call_6655,])
output2 = relay.Tuple([bop_6628,call_6635,call_6643,call_6656,])
func_6660 = relay.Function([var_6627,], output)
mod['func_6660'] = func_6660
mod = relay.transform.InferType()(mod)
var_6661 = relay.var("var_6661", dtype = "float64", shape = (3, 15, 15))#candidate|6661|(3, 15, 15)|var|float64
output = func_6660(var_6661)
func_6662 = relay.Function([var_6661], output)
mutated_mod['func_6662'] = func_6662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2692_call = mod.get_global_var('func_2692')
func_2694_call = mutated_mod.get_global_var('func_2694')
call_6696 = relay.TupleGetItem(func_2692_call(), 0)
call_6697 = relay.TupleGetItem(func_2694_call(), 0)
output = relay.Tuple([call_6696,])
output2 = relay.Tuple([call_6697,])
func_6698 = relay.Function([], output)
mod['func_6698'] = func_6698
mod = relay.transform.InferType()(mod)
output = func_6698()
func_6699 = relay.Function([], output)
mutated_mod['func_6699'] = func_6699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3763_call = mod.get_global_var('func_3763')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_6727 = relay.TupleGetItem(func_3763_call(), 0)
call_6728 = relay.TupleGetItem(func_3764_call(), 0)
func_6337_call = mod.get_global_var('func_6337')
func_6338_call = mutated_mod.get_global_var('func_6338')
call_6738 = func_6337_call()
call_6739 = func_6337_call()
output = relay.Tuple([call_6727,call_6738,])
output2 = relay.Tuple([call_6728,call_6739,])
func_6742 = relay.Function([], output)
mod['func_6742'] = func_6742
mod = relay.transform.InferType()(mod)
mutated_mod['func_6742'] = func_6742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6742_call = mutated_mod.get_global_var('func_6742')
call_6743 = func_6742_call()
output = call_6743
func_6744 = relay.Function([], output)
mutated_mod['func_6744'] = func_6744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5447_call = mod.get_global_var('func_5447')
func_5448_call = mutated_mod.get_global_var('func_5448')
call_6820 = relay.TupleGetItem(func_5447_call(), 1)
call_6821 = relay.TupleGetItem(func_5448_call(), 1)
output = relay.Tuple([call_6820,])
output2 = relay.Tuple([call_6821,])
func_6846 = relay.Function([], output)
mod['func_6846'] = func_6846
mod = relay.transform.InferType()(mod)
output = func_6846()
func_6847 = relay.Function([], output)
mutated_mod['func_6847'] = func_6847
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6862 = relay.var("var_6862", dtype = "float32", shape = (1, 8, 15))#candidate|6862|(1, 8, 15)|var|float32
uop_6863 = relay.sin(var_6862.astype('float32')) # shape=(1, 8, 15)
func_5367_call = mod.get_global_var('func_5367')
func_5369_call = mutated_mod.get_global_var('func_5369')
const_6870 = relay.const([False,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,True], dtype = "bool")#candidate|6870|(576,)|const|bool
call_6869 = relay.TupleGetItem(func_5367_call(relay.reshape(const_6870.astype('bool'), [16, 12, 3])), 1)
call_6871 = relay.TupleGetItem(func_5369_call(relay.reshape(const_6870.astype('bool'), [16, 12, 3])), 1)
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_6872 = relay.TupleGetItem(func_4614_call(), 0)
call_6873 = relay.TupleGetItem(func_4615_call(), 0)
var_6880 = relay.var("var_6880", dtype = "float32", shape = (11, 8, 15))#candidate|6880|(11, 8, 15)|var|float32
bop_6881 = relay.equal(uop_6863.astype('bool'), var_6880.astype('bool')) # shape=(11, 8, 15)
output = relay.Tuple([call_6869,const_6870,call_6872,bop_6881,])
output2 = relay.Tuple([call_6871,const_6870,call_6873,bop_6881,])
func_6888 = relay.Function([var_6862,var_6880,], output)
mod['func_6888'] = func_6888
mod = relay.transform.InferType()(mod)
var_6889 = relay.var("var_6889", dtype = "float32", shape = (1, 8, 15))#candidate|6889|(1, 8, 15)|var|float32
var_6890 = relay.var("var_6890", dtype = "float32", shape = (11, 8, 15))#candidate|6890|(11, 8, 15)|var|float32
output = func_6888(var_6889,var_6890,)
func_6891 = relay.Function([var_6889,var_6890,], output)
mutated_mod['func_6891'] = func_6891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_6916 = relay.TupleGetItem(func_2460_call(), 0)
call_6917 = relay.TupleGetItem(func_2462_call(), 0)
func_6587_call = mod.get_global_var('func_6587')
func_6588_call = mutated_mod.get_global_var('func_6588')
call_6936 = func_6587_call()
call_6937 = func_6587_call()
output = relay.Tuple([call_6916,call_6936,])
output2 = relay.Tuple([call_6917,call_6937,])
func_6949 = relay.Function([], output)
mod['func_6949'] = func_6949
mod = relay.transform.InferType()(mod)
output = func_6949()
func_6950 = relay.Function([], output)
mutated_mod['func_6950'] = func_6950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_6960 = relay.TupleGetItem(func_4503_call(), 0)
call_6961 = relay.TupleGetItem(func_4505_call(), 0)
func_3825_call = mod.get_global_var('func_3825')
func_3826_call = mutated_mod.get_global_var('func_3826')
call_6962 = func_3825_call()
call_6963 = func_3825_call()
func_6587_call = mod.get_global_var('func_6587')
func_6588_call = mutated_mod.get_global_var('func_6588')
call_6979 = func_6587_call()
call_6980 = func_6587_call()
func_2287_call = mod.get_global_var('func_2287')
func_2290_call = mutated_mod.get_global_var('func_2290')
var_6992 = relay.var("var_6992", dtype = "uint32", shape = (528,))#candidate|6992|(528,)|var|uint32
call_6991 = relay.TupleGetItem(func_2287_call(relay.reshape(var_6992.astype('uint32'), [11, 12, 4]), relay.reshape(var_6992.astype('uint32'), [11, 12, 4]), ), 2)
call_6993 = relay.TupleGetItem(func_2290_call(relay.reshape(var_6992.astype('uint32'), [11, 12, 4]), relay.reshape(var_6992.astype('uint32'), [11, 12, 4]), ), 2)
func_1637_call = mod.get_global_var('func_1637')
func_1640_call = mutated_mod.get_global_var('func_1640')
var_7005 = relay.var("var_7005", dtype = "bool", shape = (4, 264))#candidate|7005|(4, 264)|var|bool
call_7004 = relay.TupleGetItem(func_1637_call(relay.reshape(var_7005.astype('bool'), [11, 6, 16]), relay.reshape(var_7005.astype('bool'), [11, 6, 16]), ), 2)
call_7006 = relay.TupleGetItem(func_1640_call(relay.reshape(var_7005.astype('bool'), [11, 6, 16]), relay.reshape(var_7005.astype('bool'), [11, 6, 16]), ), 2)
uop_7014 = relay.acos(var_7005.astype('float32')) # shape=(4, 264)
output = relay.Tuple([call_6960,call_6962,call_6979,call_6991,var_6992,call_7004,uop_7014,])
output2 = relay.Tuple([call_6961,call_6963,call_6980,call_6993,var_6992,call_7006,uop_7014,])
func_7026 = relay.Function([var_6992,var_7005,], output)
mod['func_7026'] = func_7026
mod = relay.transform.InferType()(mod)
var_7027 = relay.var("var_7027", dtype = "uint32", shape = (528,))#candidate|7027|(528,)|var|uint32
var_7028 = relay.var("var_7028", dtype = "bool", shape = (4, 264))#candidate|7028|(4, 264)|var|bool
output = func_7026(var_7027,var_7028,)
func_7029 = relay.Function([var_7027,var_7028,], output)
mutated_mod['func_7029'] = func_7029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_7141 = relay.TupleGetItem(func_4614_call(), 0)
call_7142 = relay.TupleGetItem(func_4615_call(), 0)
func_5873_call = mod.get_global_var('func_5873')
func_5876_call = mutated_mod.get_global_var('func_5876')
const_7144 = relay.const([-6,-7,4,6,3,4,-6,-7,-6,-4,-4,6,-10,3,6,-5,3,-3,-3,1,-3,-7,8,3,10,10,6,3,10,-5,4,-1,1,3,2,-1,1,-4,-3,10,4,7,-7,8,-6,4,-5,6,2,2,-3,9,-3,10,1,7,-1,-5,-7,-8,10,-3,-8,2,6,3,7,5,6,3,-7,-1,7,1,-3,-6,-10,7,-6,9,1,3,-4,7,6,-5,2,-5,6,-2,-2,9,7,-1,4,-7,10,4,-10,3,-3,-1,8,6,2,10,-8,6], dtype = "uint8")#candidate|7144|(108,)|const|uint8
call_7143 = func_5873_call(relay.reshape(const_7144.astype('uint8'), [1, 9, 12]))
call_7145 = func_5873_call(relay.reshape(const_7144.astype('uint8'), [1, 9, 12]))
uop_7154 = relay.asinh(call_7143.astype('float64')) # shape=(10, 9, 12)
uop_7156 = relay.asinh(call_7145.astype('float64')) # shape=(10, 9, 12)
func_3763_call = mod.get_global_var('func_3763')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_7158 = relay.TupleGetItem(func_3763_call(), 0)
call_7159 = relay.TupleGetItem(func_3764_call(), 0)
uop_7162 = relay.cosh(uop_7154.astype('float64')) # shape=(10, 9, 12)
uop_7164 = relay.cosh(uop_7156.astype('float64')) # shape=(10, 9, 12)
output = relay.Tuple([call_7141,const_7144,call_7158,uop_7162,])
output2 = relay.Tuple([call_7142,const_7144,call_7159,uop_7164,])
func_7165 = relay.Function([], output)
mod['func_7165'] = func_7165
mod = relay.transform.InferType()(mod)
mutated_mod['func_7165'] = func_7165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7165_call = mutated_mod.get_global_var('func_7165')
call_7166 = func_7165_call()
output = call_7166
func_7167 = relay.Function([], output)
mutated_mod['func_7167'] = func_7167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4484_call = mod.get_global_var('func_4484')
func_4486_call = mutated_mod.get_global_var('func_4486')
call_7284 = func_4484_call()
call_7285 = func_4484_call()
func_1360_call = mod.get_global_var('func_1360')
func_1363_call = mutated_mod.get_global_var('func_1363')
const_7306 = relay.const(-2, dtype = "int32")#candidate|7306|()|const|int32
var_7307 = relay.var("var_7307", dtype = "int32", shape = (30,))#candidate|7307|(30,)|var|int32
call_7305 = func_1360_call(relay.reshape(const_7306.astype('int32'), []), relay.reshape(var_7307.astype('int32'), [1, 10, 3]), )
call_7308 = func_1360_call(relay.reshape(const_7306.astype('int32'), []), relay.reshape(var_7307.astype('int32'), [1, 10, 3]), )
uop_7314 = relay.erf(call_7284.astype('float32')) # shape=(15, 11, 6)
uop_7316 = relay.erf(call_7285.astype('float32')) # shape=(15, 11, 6)
func_5267_call = mod.get_global_var('func_5267')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_7330 = relay.TupleGetItem(func_5267_call(), 1)
call_7331 = relay.TupleGetItem(func_5269_call(), 1)
func_5485_call = mod.get_global_var('func_5485')
func_5489_call = mutated_mod.get_global_var('func_5489')
var_7340 = relay.var("var_7340", dtype = "float32", shape = (384,))#candidate|7340|(384,)|var|float32
call_7339 = relay.TupleGetItem(func_5485_call(relay.reshape(var_7340.astype('float32'), [16, 8, 3]), relay.reshape(var_7340.astype('float32'), [16, 8, 3]), ), 0)
call_7341 = relay.TupleGetItem(func_5489_call(relay.reshape(var_7340.astype('float32'), [16, 8, 3]), relay.reshape(var_7340.astype('float32'), [16, 8, 3]), ), 0)
func_2645_call = mod.get_global_var('func_2645')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_7348 = func_2645_call()
call_7349 = func_2645_call()
output = relay.Tuple([call_7305,const_7306,var_7307,uop_7314,call_7330,call_7339,var_7340,call_7348,])
output2 = relay.Tuple([call_7308,const_7306,var_7307,uop_7316,call_7331,call_7341,var_7340,call_7349,])
func_7350 = relay.Function([var_7307,var_7340,], output)
mod['func_7350'] = func_7350
mod = relay.transform.InferType()(mod)
var_7351 = relay.var("var_7351", dtype = "int32", shape = (30,))#candidate|7351|(30,)|var|int32
var_7352 = relay.var("var_7352", dtype = "float32", shape = (384,))#candidate|7352|(384,)|var|float32
output = func_7350(var_7351,var_7352,)
func_7353 = relay.Function([var_7351,var_7352,], output)
mutated_mod['func_7353'] = func_7353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2990_call = mod.get_global_var('func_2990')
func_2992_call = mutated_mod.get_global_var('func_2992')
call_7472 = func_2990_call()
call_7473 = func_2990_call()
output = relay.Tuple([call_7472,])
output2 = relay.Tuple([call_7473,])
func_7477 = relay.Function([], output)
mod['func_7477'] = func_7477
mod = relay.transform.InferType()(mod)
output = func_7477()
func_7478 = relay.Function([], output)
mutated_mod['func_7478'] = func_7478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5123_call = mod.get_global_var('func_5123')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_7492 = relay.TupleGetItem(func_5123_call(), 0)
call_7493 = relay.TupleGetItem(func_5124_call(), 0)
output = relay.Tuple([call_7492,])
output2 = relay.Tuple([call_7493,])
func_7509 = relay.Function([], output)
mod['func_7509'] = func_7509
mod = relay.transform.InferType()(mod)
output = func_7509()
func_7510 = relay.Function([], output)
mutated_mod['func_7510'] = func_7510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3964_call = mod.get_global_var('func_3964')
func_3966_call = mutated_mod.get_global_var('func_3966')
call_7588 = relay.TupleGetItem(func_3964_call(), 1)
call_7589 = relay.TupleGetItem(func_3966_call(), 1)
func_4883_call = mod.get_global_var('func_4883')
func_4886_call = mutated_mod.get_global_var('func_4886')
const_7610 = relay.const([4.437366,-9.628337,8.968020,-4.442008,8.438846,-1.307873,9.917999,-5.623162,6.424811,2.797478,-4.627453,0.010659,0.434030,-4.896640,-3.352628,6.235711,6.350569,-9.319512,-9.113208,-2.046714,6.640190,-1.696085,8.681786,-9.682743,7.971072,-2.477522,4.138663,2.725614,0.227613,6.126181,-5.462284,0.775006,-2.452103,-4.279589,8.474121,-2.971303,-9.958482,9.560841,6.431864,-3.508369,7.307329,1.107556,-1.819304,5.143757,-3.128238,3.372587,7.499158,-8.738879,-1.835907,-2.187540,8.174628,1.804873,0.164599,-0.654758,-4.172194,9.503087,3.860493,-7.692737,-2.989443,6.201570,6.824882,6.959503,-0.701713,-7.383173,-4.210789,-6.272933,-6.968250,4.337413,-5.118570,-4.623544,-4.350169,2.428205,-4.640047,7.721852,1.749641,-6.362020,7.638725,-9.013697,1.456577,6.036381,5.316764,-3.389578,0.947359,-0.898260,5.644081,-7.390299,-8.776031,3.998261,-4.455975,2.935998,7.376851,-7.545068,7.350379,-4.703641,6.993546,8.705273,9.208377,-7.251936,2.129161,3.728700,-3.730241,5.419683,1.170862,5.249266,8.325153,6.104441,-5.131859,-0.282116,-4.301803,1.701149,-3.235448,2.818753,-5.593317,-5.917916,-7.175874,-3.729768,4.916431,2.791423,-6.293490,-1.654784,-0.369684,-1.355213,5.547443,-4.859217,-6.990014,-8.240799,-5.187125,-2.931829,4.036717,3.302423,-6.984138,-2.977703,1.294494,-7.533239,1.295220,5.158011,2.846013,-8.226488,-8.169781,-4.231382,-8.859980,4.405481,-3.735997,4.247429,-2.667604,1.532994,-8.081935,5.402619,-0.533548,3.673382,-4.592280,7.453345,2.695128,8.849785,-9.713765,-4.421872,-9.693327,-3.539914,7.700459,-3.041364,-8.652260,4.416777,-4.424847,-8.881736,-1.303870,-3.058711,-4.032206,-4.880128,1.362848,-6.409586,-0.903236,0.069409,-4.813863,0.116553,4.017986,-6.714012,-4.531646,1.182135,-1.471341,0.724050,8.025730,5.279760,4.607027,4.126052,7.142643,-9.771060,-5.586309,-2.263742,6.914336,4.343993,-1.988621,-8.852849,5.686808,0.598875,3.306486,-2.066322,-5.891243,2.789775,-5.280449,-2.912695,-4.422450,7.627680,-1.985962,8.443683,3.861287,0.690169,-8.992212,-4.124570,8.874685,7.502429,-5.912355,6.339441,-2.445744,-4.795820,-1.115638,-2.454422,-8.043280,2.297270,-3.168089,-5.914393,1.999414,9.976737,-7.213265,6.392197,2.337783,-1.043298,5.548811,-7.687412,-4.199979,-0.387763,1.664627,2.268729,-4.614282,7.199321,-6.808649,-7.988984,2.270378,3.364634,-5.073345,9.800985,-6.878856,7.220829,3.364473,9.484150,1.977146,-1.893316,-9.538707,-4.781744,4.725650,7.914398,2.821710,0.763512,8.959064,-7.129387,-1.076121,1.516949,-6.771141,-0.079919,-1.998418,3.103888,2.464665,6.281960,-4.767024,-6.512469,2.034064,8.566751,3.145334,4.391733,2.174709,-9.630238,2.807905,-4.975319,4.796198,2.248649,-9.765839,0.941638,5.297202,-3.534047,-7.432159,9.001111,-2.997223,-2.779173,7.716204,3.540433,-7.177061,-0.828181,3.969707,1.027075,0.397900,6.045238,0.964964,9.248760,3.784020,-8.462726,-3.285182,5.891231,-4.619897,4.302940,3.369556,9.589763,-8.563740,7.920581,-8.768344,-4.672168,1.384724,-1.230879,-8.068661,6.298271,7.427907,7.323801,2.123368,-6.049223,4.169743,-3.854166,-2.445706,-0.754083,3.440208,9.285828,-7.429466,-0.977939,3.186278,-5.040140,-8.085871,9.299018,-8.824916,-0.679822,3.841368,2.771507,-1.830996,2.724493,7.022125,9.545818,4.003090,4.990666,8.569160,9.948664,-3.595670,-3.229893,-5.816657,-9.685693,7.801685,-6.528074,5.875547,3.393176,3.793288,2.096813,-0.205221,-8.458086,7.414532,1.026609,8.327796,1.761136,-6.655522,-0.652967,6.226045,7.487333,9.142143,9.251695,-2.276032,-9.121693,9.486590,-8.298539,3.579992,9.455906,-5.690955,1.115790,1.190828,3.198993,-0.164834,-5.568349,-9.497550,-7.922962,-9.168413,5.680325,-0.267153,-8.398356,3.183386,7.602580,2.290495,1.423982,4.107731,0.640746,8.238285,9.646740,7.298485,2.235202,6.181550,1.044859,7.578125,-7.625253,0.805107,5.949671,-8.775938,7.794176,4.951360,4.803882,4.461685,6.043592,-2.213610,-8.386514,5.620677,5.132992,-9.330183,-3.782727,0.052185,1.251096,8.163560,0.962525,-2.660047,-8.174346,8.195997,-4.921421,-3.267177,7.632458,-7.043342,-1.347042,1.235768,1.731046,5.577968,6.735585,-9.015456,9.231091,6.435843,4.605634,8.214147,1.212503,-3.342830,0.979771,-0.817591,6.803160,-0.669967,-9.530374,5.610006,7.268513,3.684545,-2.720881,-2.982051,1.615083,-5.754373,9.811920,-3.041137,8.516592,-1.076438,-6.921509,5.237881,-9.945143,2.166102,-6.958992], dtype = "float64")#candidate|7610|(448,)|const|float64
call_7609 = relay.TupleGetItem(func_4883_call(relay.reshape(const_7610.astype('float64'), [448,])), 0)
call_7611 = relay.TupleGetItem(func_4886_call(relay.reshape(const_7610.astype('float64'), [448,])), 0)
func_6888_call = mod.get_global_var('func_6888')
func_6891_call = mutated_mod.get_global_var('func_6891')
var_7631 = relay.var("var_7631", dtype = "float32", shape = (3, 40))#candidate|7631|(3, 40)|var|float32
var_7632 = relay.var("var_7632", dtype = "float32", shape = (1320,))#candidate|7632|(1320,)|var|float32
call_7630 = relay.TupleGetItem(func_6888_call(relay.reshape(var_7631.astype('float32'), [1, 8, 15]), relay.reshape(var_7632.astype('float32'), [11, 8, 15]), ), 0)
call_7633 = relay.TupleGetItem(func_6891_call(relay.reshape(var_7631.astype('float32'), [1, 8, 15]), relay.reshape(var_7632.astype('float32'), [11, 8, 15]), ), 0)
func_4767_call = mod.get_global_var('func_4767')
func_4770_call = mutated_mod.get_global_var('func_4770')
const_7652 = relay.const([-2.877563,-6.954654,5.538402,-4.669508,7.763695,0.704338,1.149857,2.981715,-2.143445,-0.803423,2.863016,1.158875,-3.419730,-0.484404,-0.054750,5.795272,-5.963908,1.179633,-4.861299,4.874877,-4.141412,-6.920644,5.722790,3.514455,2.761337,-2.450383,-8.568455,2.778697,-3.882059,-4.802468,8.917584,-7.621881,5.583068,5.038573,0.676644,-8.321279,9.704739,5.348602,-9.244786,-3.390130,-8.132645,-7.466147,0.219926,-2.029984], dtype = "float32")#candidate|7652|(44,)|const|float32
call_7651 = relay.TupleGetItem(func_4767_call(relay.reshape(const_7652.astype('float32'), [11, 1, 4])), 0)
call_7653 = relay.TupleGetItem(func_4770_call(relay.reshape(const_7652.astype('float32'), [11, 1, 4])), 0)
output = relay.Tuple([call_7588,call_7609,const_7610,call_7630,var_7631,var_7632,call_7651,const_7652,])
output2 = relay.Tuple([call_7589,call_7611,const_7610,call_7633,var_7631,var_7632,call_7653,const_7652,])
func_7654 = relay.Function([var_7631,var_7632,], output)
mod['func_7654'] = func_7654
mod = relay.transform.InferType()(mod)
var_7655 = relay.var("var_7655", dtype = "float32", shape = (3, 40))#candidate|7655|(3, 40)|var|float32
var_7656 = relay.var("var_7656", dtype = "float32", shape = (1320,))#candidate|7656|(1320,)|var|float32
output = func_7654(var_7655,var_7656,)
func_7657 = relay.Function([var_7655,var_7656,], output)
mutated_mod['func_7657'] = func_7657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mod.get_global_var('func_4446')
func_4448_call = mutated_mod.get_global_var('func_4448')
call_7659 = func_4446_call()
call_7660 = func_4446_call()
output = relay.Tuple([call_7659,])
output2 = relay.Tuple([call_7660,])
func_7678 = relay.Function([], output)
mod['func_7678'] = func_7678
mod = relay.transform.InferType()(mod)
mutated_mod['func_7678'] = func_7678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7678_call = mutated_mod.get_global_var('func_7678')
call_7679 = func_7678_call()
output = call_7679
func_7680 = relay.Function([], output)
mutated_mod['func_7680'] = func_7680
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7686 = relay.const([[[-6.881891,6.754098,-0.428277],[-2.764791,-6.590210,-6.466146],[2.552093,-0.439770,-2.867817],[5.275682,-3.039356,2.818194],[3.045606,-5.883084,-5.007514]],[[-2.670762,9.122748,9.928194],[0.701397,-1.895057,-3.364104],[-6.451306,-8.828691,1.175390],[-6.142453,5.455336,-6.192267],[-7.835683,9.174044,-0.533691]],[[5.338154,-2.788473,-9.451132],[-9.006641,-5.241680,0.506355],[-1.421065,-7.966217,-9.354521],[6.380295,8.270836,1.180977],[-6.692850,8.654608,-9.383550]],[[5.476486,-2.498978,2.227553],[5.477629,-6.458417,-7.305515],[-8.990644,-9.447009,-5.299042],[-1.477428,0.496993,-0.773604],[7.909894,-5.579165,3.521657]],[[0.480587,-6.554548,-3.641367],[-9.328291,-3.327806,1.952731],[8.372149,2.849063,6.084036],[-4.786689,8.387690,2.982807],[8.446190,-1.722005,1.121112]],[[-3.396979,-6.069588,1.700357],[-1.174275,-9.897737,-4.954403],[-5.608196,9.933575,7.040767],[5.395783,-1.169728,4.732308],[-4.324703,9.554122,5.433292]],[[-1.983041,8.406360,-9.003081],[-6.928459,-2.140929,1.877733],[-3.291515,-5.054210,3.473673],[-3.041140,-9.520459,-5.163586],[-8.601614,-6.664845,3.262555]]], dtype = "float32")#candidate|7686|(7, 5, 3)|const|float32
uop_7687 = relay.erf(const_7686.astype('float32')) # shape=(7, 5, 3)
func_4344_call = mod.get_global_var('func_4344')
func_4346_call = mutated_mod.get_global_var('func_4346')
call_7689 = relay.TupleGetItem(func_4344_call(), 0)
call_7690 = relay.TupleGetItem(func_4346_call(), 0)
func_6399_call = mod.get_global_var('func_6399')
func_6401_call = mutated_mod.get_global_var('func_6401')
call_7697 = relay.TupleGetItem(func_6399_call(), 0)
call_7698 = relay.TupleGetItem(func_6401_call(), 0)
func_4832_call = mod.get_global_var('func_4832')
func_4833_call = mutated_mod.get_global_var('func_4833')
call_7705 = relay.TupleGetItem(func_4832_call(), 1)
call_7706 = relay.TupleGetItem(func_4833_call(), 1)
output = relay.Tuple([uop_7687,call_7689,call_7697,call_7705,])
output2 = relay.Tuple([uop_7687,call_7690,call_7698,call_7706,])
func_7708 = relay.Function([], output)
mod['func_7708'] = func_7708
mod = relay.transform.InferType()(mod)
mutated_mod['func_7708'] = func_7708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7708_call = mutated_mod.get_global_var('func_7708')
call_7709 = func_7708_call()
output = call_7709
func_7710 = relay.Function([], output)
mutated_mod['func_7710'] = func_7710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6949_call = mod.get_global_var('func_6949')
func_6950_call = mutated_mod.get_global_var('func_6950')
call_7714 = relay.TupleGetItem(func_6949_call(), 1)
call_7715 = relay.TupleGetItem(func_6950_call(), 1)
output = relay.Tuple([call_7714,])
output2 = relay.Tuple([call_7715,])
func_7716 = relay.Function([], output)
mod['func_7716'] = func_7716
mod = relay.transform.InferType()(mod)
mutated_mod['func_7716'] = func_7716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7716_call = mutated_mod.get_global_var('func_7716')
call_7717 = func_7716_call()
output = call_7717
func_7718 = relay.Function([], output)
mutated_mod['func_7718'] = func_7718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2645_call = mod.get_global_var('func_2645')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_7782 = func_2645_call()
call_7783 = func_2645_call()
func_6888_call = mod.get_global_var('func_6888')
func_6891_call = mutated_mod.get_global_var('func_6891')
const_7826 = relay.const([2.339657,-3.429967,3.349377,8.562999,-5.248811,7.857566,7.392407,-4.850562,0.354855,8.012559,-0.589106,2.040487,-9.474768,-6.913941,-7.035264,8.285664,9.813321,-1.285814,8.026701,-8.397944,2.746721,9.657659,1.009160,5.523794,2.175574,-8.779566,-7.586425,-4.546992,4.466076,-9.187878,-2.669900,4.823937,-6.126926,-5.617026,-1.079851,7.811520,-8.359489,-3.951954,-6.737065,5.088042,-9.136355,-6.736250,5.665696,0.179758,4.210698,-4.420052,-5.101312,-5.925325,-5.728789,-4.280317,5.068568,-4.117256,9.078432,-3.706231,-7.658530,2.023785,6.220239,-0.890635,-1.977460,0.083530,1.998669,2.171774,-6.396440,-5.889616,-1.023192,8.016279,8.355854,-7.477172,-2.489575,-2.652263,-3.189924,2.713764,5.333753,-8.640761,-3.354283,-9.092605,-7.600906,8.832333,1.250395,5.311808,-3.703368,8.141770,-8.025077,-0.211627,-6.500586,0.222872,-0.445593,-3.949521,-2.439820,-9.991646,4.862556,7.649410,-2.227082,-6.198589,-9.842568,-0.652133,-9.449968,-6.817350,9.677606,8.169548,-6.647134,-5.973824,7.702994,-4.884214,2.288210,-4.937015,7.877079,-4.243623,-4.908617,7.523393,-4.570705,-2.190395,-3.246115,8.580155,2.677343,6.056026,-5.482473,3.294171,2.361540,1.927231], dtype = "float32")#candidate|7826|(120,)|const|float32
var_7827 = relay.var("var_7827", dtype = "float32", shape = (1320,))#candidate|7827|(1320,)|var|float32
call_7825 = relay.TupleGetItem(func_6888_call(relay.reshape(const_7826.astype('float32'), [1, 8, 15]), relay.reshape(var_7827.astype('float32'), [11, 8, 15]), ), 1)
call_7828 = relay.TupleGetItem(func_6891_call(relay.reshape(const_7826.astype('float32'), [1, 8, 15]), relay.reshape(var_7827.astype('float32'), [11, 8, 15]), ), 1)
func_991_call = mod.get_global_var('func_991')
func_994_call = mutated_mod.get_global_var('func_994')
const_7830 = relay.const([[-0.665060,-5.749075,1.395888,7.253812,9.963929,1.892532,3.771236,-1.346022,7.264858,2.734508,8.424806,-5.520449]], dtype = "float32")#candidate|7830|(1, 12)|const|float32
var_7831 = relay.var("var_7831", dtype = "float32", shape = (156,))#candidate|7831|(156,)|var|float32
call_7829 = relay.TupleGetItem(func_991_call(relay.reshape(const_7830.astype('float32'), [6, 2, 1]), relay.reshape(var_7831.astype('float32'), [6, 2, 13]), ), 5)
call_7832 = relay.TupleGetItem(func_994_call(relay.reshape(const_7830.astype('float32'), [6, 2, 1]), relay.reshape(var_7831.astype('float32'), [6, 2, 13]), ), 5)
uop_7838 = relay.cos(var_7831.astype('float64')) # shape=(156,)
func_3358_call = mod.get_global_var('func_3358')
func_3361_call = mutated_mod.get_global_var('func_3361')
var_7843 = relay.var("var_7843", dtype = "float64", shape = (648,))#candidate|7843|(648,)|var|float64
call_7842 = relay.TupleGetItem(func_3358_call(relay.reshape(var_7843.astype('float64'), [6, 9, 12]), relay.reshape(call_7782.astype('int8'), [990,]), ), 2)
call_7844 = relay.TupleGetItem(func_3361_call(relay.reshape(var_7843.astype('float64'), [6, 9, 12]), relay.reshape(call_7782.astype('int8'), [990,]), ), 2)
output = relay.Tuple([call_7782,call_7825,const_7826,var_7827,call_7829,const_7830,uop_7838,call_7842,var_7843,])
output2 = relay.Tuple([call_7783,call_7828,const_7826,var_7827,call_7832,const_7830,uop_7838,call_7844,var_7843,])
func_7860 = relay.Function([var_7827,var_7831,var_7843,], output)
mod['func_7860'] = func_7860
mod = relay.transform.InferType()(mod)
mutated_mod['func_7860'] = func_7860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7860_call = mutated_mod.get_global_var('func_7860')
var_7862 = relay.var("var_7862", dtype = "float32", shape = (1320,))#candidate|7862|(1320,)|var|float32
var_7863 = relay.var("var_7863", dtype = "float32", shape = (156,))#candidate|7863|(156,)|var|float32
var_7864 = relay.var("var_7864", dtype = "float64", shape = (648,))#candidate|7864|(648,)|var|float64
call_7861 = func_7860_call(var_7862,var_7863,var_7864,)
output = call_7861
func_7865 = relay.Function([var_7862,var_7863,var_7864,], output)
mutated_mod['func_7865'] = func_7865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5888_call = mod.get_global_var('func_5888')
func_5890_call = mutated_mod.get_global_var('func_5890')
call_7871 = relay.TupleGetItem(func_5888_call(), 0)
call_7872 = relay.TupleGetItem(func_5890_call(), 0)
output = relay.Tuple([call_7871,])
output2 = relay.Tuple([call_7872,])
func_7891 = relay.Function([], output)
mod['func_7891'] = func_7891
mod = relay.transform.InferType()(mod)
output = func_7891()
func_7892 = relay.Function([], output)
mutated_mod['func_7892'] = func_7892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4276_call = mod.get_global_var('func_4276')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_7938 = relay.TupleGetItem(func_4276_call(), 0)
call_7939 = relay.TupleGetItem(func_4278_call(), 0)
var_7945 = relay.var("var_7945", dtype = "int8", shape = (15, 11, 6))#candidate|7945|(15, 11, 6)|var|int8
bop_7946 = relay.minimum(call_7938.astype('float32'), relay.reshape(var_7945.astype('float32'), relay.shape_of(call_7938))) # shape=(15, 11, 6)
bop_7949 = relay.minimum(call_7939.astype('float32'), relay.reshape(var_7945.astype('float32'), relay.shape_of(call_7939))) # shape=(15, 11, 6)
func_4484_call = mod.get_global_var('func_4484')
func_4486_call = mutated_mod.get_global_var('func_4486')
call_7950 = func_4484_call()
call_7951 = func_4484_call()
func_5808_call = mod.get_global_var('func_5808')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_7955 = func_5808_call()
call_7956 = func_5808_call()
func_5062_call = mod.get_global_var('func_5062')
func_5065_call = mutated_mod.get_global_var('func_5065')
var_7962 = relay.var("var_7962", dtype = "uint64", shape = ())#candidate|7962|()|var|uint64
var_7963 = relay.var("var_7963", dtype = "uint64", shape = (36, 10))#candidate|7963|(36, 10)|var|uint64
call_7961 = relay.TupleGetItem(func_5062_call(relay.reshape(var_7962.astype('uint64'), []), relay.reshape(var_7963.astype('uint64'), [12, 2, 15]), ), 0)
call_7964 = relay.TupleGetItem(func_5065_call(relay.reshape(var_7962.astype('uint64'), []), relay.reshape(var_7963.astype('uint64'), [12, 2, 15]), ), 0)
output = relay.Tuple([bop_7946,call_7950,call_7955,call_7961,var_7962,var_7963,])
output2 = relay.Tuple([bop_7949,call_7951,call_7956,call_7964,var_7962,var_7963,])
func_7967 = relay.Function([var_7945,var_7962,var_7963,], output)
mod['func_7967'] = func_7967
mod = relay.transform.InferType()(mod)
mutated_mod['func_7967'] = func_7967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7967_call = mutated_mod.get_global_var('func_7967')
var_7969 = relay.var("var_7969", dtype = "int8", shape = (15, 11, 6))#candidate|7969|(15, 11, 6)|var|int8
var_7970 = relay.var("var_7970", dtype = "uint64", shape = ())#candidate|7970|()|var|uint64
var_7971 = relay.var("var_7971", dtype = "uint64", shape = (36, 10))#candidate|7971|(36, 10)|var|uint64
call_7968 = func_7967_call(var_7969,var_7970,var_7971,)
output = call_7968
func_7972 = relay.Function([var_7969,var_7970,var_7971,], output)
mutated_mod['func_7972'] = func_7972
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7992 = relay.var("var_7992", dtype = "float64", shape = (11, 5, 12))#candidate|7992|(11, 5, 12)|var|float64
uop_7993 = relay.erf(var_7992.astype('float64')) # shape=(11, 5, 12)
var_8000 = relay.var("var_8000", dtype = "float64", shape = (11, 5, 12))#candidate|8000|(11, 5, 12)|var|float64
bop_8001 = relay.equal(uop_7993.astype('bool'), relay.reshape(var_8000.astype('bool'), relay.shape_of(uop_7993))) # shape=(11, 5, 12)
output = relay.Tuple([bop_8001,])
output2 = relay.Tuple([bop_8001,])
F = relay.Function([var_7992,var_8000,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7992,var_8000,], output2)
mutated_mod['main'] = F
mutated_mod = relay.transform.InferType()(mutated_mod)
print('==========mutated_mod==========')
print(mutated_mod.astext(show_meta_data=False))
print('===================================')
graph, lib, params = relay.build(mod, target='llvm')
module1 = graph_runtime.create(graph, lib, tvm.device('llvm',0))
intrp2 = relay.build_module.create_executor('graph', mod, tvm.device('llvm',0),'llvm')
intrp3 = relay.build_module.create_executor('debug', mod, tvm.device('llvm',0),'llvm')
intrp4 = relay.build_module.create_executor('vm', mod, tvm.device('llvm',0),'llvm')
graph, lib, params = relay.build(mod, target='cuda')
module5 = graph_runtime.create(graph, lib, tvm.device('cuda',0))
intrp6 = relay.build_module.create_executor('graph', mod, tvm.device('cuda',0),'cuda')
intrp7 = relay.build_module.create_executor('debug', mod, tvm.device('cuda',0),'cuda')
intrp8 = relay.build_module.create_executor('vm', mod, tvm.device('cuda',0),'cuda')
seq = Sequential([
	relay.transform.AlterOpLayout(),
	relay.transform.AnnotateSpans(),
	relay.transform.BatchingOps(),
	relay.transform.CanonicalizeCast(),
	relay.transform.CanonicalizeOps(),
	relay.transform.DeadCodeElimination(),
	relay.transform.DynamicToStatic(),
])
mod = seq(mod)
print(mod.astext(show_meta_data=False))
graph, lib, params = relay.build(mod, target='llvm')
module9 = graph_runtime.create(graph, lib, tvm.device('llvm',0))
intrp10 = relay.build_module.create_executor('graph', mod, tvm.device('llvm',0),'llvm')
intrp11 = relay.build_module.create_executor('debug', mod, tvm.device('llvm',0),'llvm')
intrp12 = relay.build_module.create_executor('vm', mod, tvm.device('llvm',0),'llvm')
graph, lib, params = relay.build(mod, target='cuda')
module13 = graph_runtime.create(graph, lib, tvm.device('cuda',0))
intrp14 = relay.build_module.create_executor('graph', mod, tvm.device('cuda',0),'cuda')
intrp15 = relay.build_module.create_executor('debug', mod, tvm.device('cuda',0),'cuda')
intrp16 = relay.build_module.create_executor('vm', mod, tvm.device('cuda',0),'cuda')
graph, lib, params = relay.build(mutated_mod, target='llvm')
module17 = graph_runtime.create(graph, lib, tvm.device('llvm',0))
intrp18 = relay.build_module.create_executor('graph', mutated_mod, tvm.device('llvm',0),'llvm')
intrp19 = relay.build_module.create_executor('debug', mutated_mod, tvm.device('llvm',0),'llvm')
intrp20 = relay.build_module.create_executor('vm', mutated_mod, tvm.device('llvm',0),'llvm')
graph, lib, params = relay.build(mutated_mod, target='cuda')
module21 = graph_runtime.create(graph, lib, tvm.device('cuda',0))
intrp22 = relay.build_module.create_executor('graph', mutated_mod, tvm.device('cuda',0),'cuda')
intrp23 = relay.build_module.create_executor('debug', mutated_mod, tvm.device('cuda',0),'cuda')
intrp24 = relay.build_module.create_executor('vm', mutated_mod, tvm.device('cuda',0),'cuda')
