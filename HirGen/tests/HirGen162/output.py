import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_391 = relay.var("var_391", dtype = "int64", shape = (15, 7, 6))#candidate|391|(15, 7, 6)|var|int64
var_392 = relay.var("var_392", dtype = "int64", shape = (15, 7, 6))#candidate|392|(15, 7, 6)|var|int64
bop_393 = relay.bitwise_xor(var_391.astype('int64'), relay.reshape(var_392.astype('int64'), relay.shape_of(var_391))) # shape=(15, 7, 6)
uop_397 = relay.acos(bop_393.astype('float64')) # shape=(15, 7, 6)
bop_403 = relay.subtract(uop_397.astype('uint16'), relay.reshape(bop_393.astype('uint16'), relay.shape_of(uop_397))) # shape=(15, 7, 6)
bop_406 = relay.power(bop_403.astype('float64'), relay.reshape(var_392.astype('float64'), relay.shape_of(bop_403))) # shape=(15, 7, 6)
output = bop_406
output2 = bop_406
func_432 = relay.Function([var_391,var_392,], output)
mod['func_432'] = func_432
mod = relay.transform.InferType()(mod)
mutated_mod['func_432'] = func_432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_432_call = mutated_mod.get_global_var('func_432')
var_434 = relay.var("var_434", dtype = "int64", shape = (15, 7, 6))#candidate|434|(15, 7, 6)|var|int64
var_435 = relay.var("var_435", dtype = "int64", shape = (15, 7, 6))#candidate|435|(15, 7, 6)|var|int64
call_433 = func_432_call(var_434,var_435,)
output = call_433
func_436 = relay.Function([var_434,var_435,], output)
mutated_mod['func_436'] = func_436
mutated_mod = relay.transform.InferType()(mutated_mod)
var_562 = relay.var("var_562", dtype = "float32", shape = (16, 7, 1))#candidate|562|(16, 7, 1)|var|float32
uop_563 = relay.erf(var_562.astype('float32')) # shape=(16, 7, 1)
output = uop_563
output2 = uop_563
func_567 = relay.Function([var_562,], output)
mod['func_567'] = func_567
mod = relay.transform.InferType()(mod)
var_568 = relay.var("var_568", dtype = "float32", shape = (16, 7, 1))#candidate|568|(16, 7, 1)|var|float32
output = func_567(var_568)
func_569 = relay.Function([var_568], output)
mutated_mod['func_569'] = func_569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_735 = relay.var("var_735", dtype = "float64", shape = (4, 1, 10))#candidate|735|(4, 1, 10)|var|float64
uop_736 = relay.erf(var_735.astype('float64')) # shape=(4, 1, 10)
bop_750 = relay.bitwise_and(uop_736.astype('uint64'), relay.reshape(var_735.astype('uint64'), relay.shape_of(uop_736))) # shape=(4, 1, 10)
func_432_call = mod.get_global_var('func_432')
func_436_call = mutated_mod.get_global_var('func_436')
var_755 = relay.var("var_755", dtype = "int64", shape = (630,))#candidate|755|(630,)|var|int64
call_754 = func_432_call(relay.reshape(var_755.astype('int64'), [15, 7, 6]), relay.reshape(var_755.astype('int64'), [15, 7, 6]), )
call_756 = func_432_call(relay.reshape(var_755.astype('int64'), [15, 7, 6]), relay.reshape(var_755.astype('int64'), [15, 7, 6]), )
const_757 = relay.const([[[-1,-1,9,-2,6,-7,-5,-8,9,3],[-9,4,5,-1,5,5,10,8,5,4],[-7,-10,-2,-1,2,-1,-5,8,-2,-8],[-1,-3,-9,2,-3,9,7,-4,-6,2],[-9,10,7,-5,-4,-6,-6,-8,9,10],[6,2,9,-2,3,4,8,-5,9,-4],[10,10,8,-10,-7,9,-2,-7,-10,-9],[-5,-4,-6,-8,6,-9,-9,-2,-8,3],[3,-9,6,-9,6,-9,8,4,2,-10],[-3,5,-10,10,-9,3,7,-8,-1,1],[-4,8,8,7,-5,8,-6,9,-10,-5],[-4,-1,-2,5,-8,1,-1,-6,-3,8],[-2,6,-9,-5,6,8,-8,-10,-9,-6],[-5,1,-5,4,-1,-6,7,10,-8,5],[-5,-5,-1,3,-2,-1,5,-3,-8,-8]],[[9,2,7,2,-7,1,-9,4,3,-3],[8,4,-3,-4,5,-2,8,-10,5,2],[10,-3,4,-10,5,-4,7,-6,8,-3],[-6,9,10,10,-3,7,-10,4,-8,-10],[10,-7,3,-7,-7,-6,-9,8,-6,3],[3,-5,-2,6,3,-4,10,-8,-9,6],[9,-9,-8,-6,-5,6,-10,-2,7,-4],[-2,3,-4,-4,8,-6,-3,5,-2,-8],[1,7,-4,-6,5,-3,-10,8,9,-6],[-6,-6,-7,-2,2,-6,-3,-6,9,10],[-4,2,9,-10,4,5,-6,8,-2,2],[10,10,-10,10,10,5,3,10,7,-10],[5,10,-8,7,-1,-7,9,-6,-4,10],[6,-8,3,1,-7,3,-10,-5,3,2],[1,7,-7,-10,-9,6,6,-4,-3,10]],[[-8,4,-6,-8,-9,5,10,-1,-4,1],[-1,-9,-3,7,10,8,10,7,10,-9],[6,2,-7,-4,-4,-6,-1,2,-8,2],[6,-3,3,-6,-5,-6,10,-6,1,-10],[6,9,-9,-3,-10,2,-8,-6,-6,6],[7,4,-7,6,2,-2,2,-8,-2,7],[-8,2,7,-7,-10,6,-2,-7,-1,-7],[-9,-3,-10,-1,2,8,8,-3,6,7],[10,3,4,-3,3,9,-8,-2,-3,-5],[-10,4,1,-4,-7,10,4,1,3,4],[3,7,-8,-2,-9,-6,7,10,5,-4],[-3,-2,-10,-7,-9,9,4,5,-5,3],[-3,-5,-8,10,-9,8,1,-10,-4,-5],[8,7,10,-4,-9,10,-7,-6,-2,-8],[3,2,7,6,-9,-6,-5,-8,5,1]],[[-10,-7,8,10,10,-10,6,-8,1,4],[-4,-6,-3,3,6,-1,-7,-3,-2,4],[3,-6,3,9,7,-6,6,-10,-6,-7],[9,9,8,8,7,1,-3,8,-10,-1],[-4,6,1,-9,8,-9,5,2,4,-3],[-1,10,9,3,-8,-6,3,2,-9,1],[8,6,-2,7,8,6,4,7,-5,-3],[-5,5,3,4,-8,-9,8,10,-4,5],[-6,-1,-6,-4,-9,6,-7,5,-8,-4],[-7,5,-8,7,-1,-4,-3,5,-7,2],[7,-1,-1,-6,7,-7,3,-2,-6,-5],[-1,-2,-7,-6,8,-8,8,-1,8,-7],[-5,3,-8,-1,4,-9,-6,-9,-10,5],[5,-4,7,-1,1,1,-6,-8,-9,-9],[6,8,-1,-2,4,-10,3,3,7,6]]], dtype = "uint64")#candidate|757|(4, 15, 10)|const|uint64
bop_758 = relay.less_equal(bop_750.astype('bool'), const_757.astype('bool')) # shape=(4, 15, 10)
output = relay.Tuple([call_754,var_755,bop_758,])
output2 = relay.Tuple([call_756,var_755,bop_758,])
func_762 = relay.Function([var_735,var_755,], output)
mod['func_762'] = func_762
mod = relay.transform.InferType()(mod)
var_763 = relay.var("var_763", dtype = "float64", shape = (4, 1, 10))#candidate|763|(4, 1, 10)|var|float64
var_764 = relay.var("var_764", dtype = "int64", shape = (630,))#candidate|764|(630,)|var|int64
output = func_762(var_763,var_764,)
func_765 = relay.Function([var_763,var_764,], output)
mutated_mod['func_765'] = func_765
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1070 = relay.var("var_1070", dtype = "bool", shape = (13, 16, 1))#candidate|1070|(13, 16, 1)|var|bool
var_1071 = relay.var("var_1071", dtype = "bool", shape = (13, 16, 7))#candidate|1071|(13, 16, 7)|var|bool
bop_1072 = relay.logical_and(var_1070.astype('bool'), var_1071.astype('bool')) # shape=(13, 16, 7)
func_567_call = mod.get_global_var('func_567')
func_569_call = mutated_mod.get_global_var('func_569')
var_1078 = relay.var("var_1078", dtype = "float32", shape = (112,))#candidate|1078|(112,)|var|float32
call_1077 = func_567_call(relay.reshape(var_1078.astype('float32'), [16, 7, 1]))
call_1079 = func_567_call(relay.reshape(var_1078.astype('float32'), [16, 7, 1]))
uop_1082 = relay.log10(var_1071.astype('float64')) # shape=(13, 16, 7)
bop_1087 = relay.logical_or(uop_1082.astype('bool'), relay.reshape(var_1071.astype('bool'), relay.shape_of(uop_1082))) # shape=(13, 16, 7)
output = relay.Tuple([bop_1072,call_1077,var_1078,bop_1087,])
output2 = relay.Tuple([bop_1072,call_1079,var_1078,bop_1087,])
func_1090 = relay.Function([var_1070,var_1071,var_1078,], output)
mod['func_1090'] = func_1090
mod = relay.transform.InferType()(mod)
var_1091 = relay.var("var_1091", dtype = "bool", shape = (13, 16, 1))#candidate|1091|(13, 16, 1)|var|bool
var_1092 = relay.var("var_1092", dtype = "bool", shape = (13, 16, 7))#candidate|1092|(13, 16, 7)|var|bool
var_1093 = relay.var("var_1093", dtype = "float32", shape = (112,))#candidate|1093|(112,)|var|float32
output = func_1090(var_1091,var_1092,var_1093,)
func_1094 = relay.Function([var_1091,var_1092,var_1093,], output)
mutated_mod['func_1094'] = func_1094
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1440 = relay.const([[[-5,7,1,-2,5,-4,6,3,6],[9,-2,-7,6,-5,-2,-7,5,4],[-6,-3,-8,-5,3,-6,7,4,6],[6,-7,-7,3,-7,9,-2,-10,5],[4,-2,-8,-7,4,4,1,2,-1],[7,2,-2,-7,-8,-3,-5,-1,-3],[-3,-5,2,-7,-1,10,-7,-8,3],[1,-6,9,10,-6,8,1,10,10],[-9,-4,7,4,3,2,2,7,10],[7,7,10,-5,-1,-1,8,10,-2],[-5,9,-8,3,-2,-10,-6,2,-2]]], dtype = "int32")#candidate|1440|(1, 11, 9)|const|int32
var_1441 = relay.var("var_1441", dtype = "int32", shape = (1, 11, 9))#candidate|1441|(1, 11, 9)|var|int32
bop_1442 = relay.right_shift(const_1440.astype('int32'), relay.reshape(var_1441.astype('int32'), relay.shape_of(const_1440))) # shape=(1, 11, 9)
func_567_call = mod.get_global_var('func_567')
func_569_call = mutated_mod.get_global_var('func_569')
const_1454 = relay.const([-8.950320,9.854270,-5.845491,-8.340615,-2.233994,-2.573264,-1.948119,9.764193,-1.856385,-5.340761,-0.783312,9.842551,-3.908288,-2.932611,-7.928385,3.557477,-5.870505,-3.616813,1.302797,2.417231,-0.879826,-3.085851,-4.124969,-2.620811,9.717756,-1.168906,-1.204653,-0.711634,-6.027367,-0.151872,-8.213917,0.616875,-2.405552,2.614116,-3.055541,9.665521,5.582985,4.558927,-0.045472,-1.450579,-1.185132,7.075554,-4.122774,6.871351,-1.307834,-2.134890,-2.128288,5.491665,1.318372,-5.111294,-3.223636,-2.517563,9.038368,1.247546,6.951555,4.359995,-2.086280,-1.347471,-9.069916,2.508370,0.876942,3.071679,1.545138,-7.017062,-2.047297,-0.158068,0.713491,-1.931582,-1.837184,-3.509400,0.463918,-6.221787,-5.995344,-8.155809,-0.268169,7.305436,2.150706,1.504257,4.333316,8.998098,9.894051,-0.400690,-6.859458,9.045163,-7.987328,-8.423964,-3.128568,-8.067802,8.174694,4.316771,-0.548475,4.215487,-8.562946,7.496973,0.302249,8.289830,-4.804829,8.552471,-6.087758,-9.509794,-5.179100,-5.867478,2.021352,1.225279,0.670030,-5.607657,2.502751,-0.190255,5.922944,6.006320,-5.777499,7.344350], dtype = "float32")#candidate|1454|(112,)|const|float32
call_1453 = func_567_call(relay.reshape(const_1454.astype('float32'), [16, 7, 1]))
call_1455 = func_567_call(relay.reshape(const_1454.astype('float32'), [16, 7, 1]))
func_567_call = mod.get_global_var('func_567')
func_569_call = mutated_mod.get_global_var('func_569')
call_1456 = func_567_call(relay.reshape(const_1454.astype('float32'), [16, 7, 1]))
call_1457 = func_567_call(relay.reshape(const_1454.astype('float32'), [16, 7, 1]))
output = relay.Tuple([bop_1442,call_1453,const_1454,call_1456,])
output2 = relay.Tuple([bop_1442,call_1455,const_1454,call_1457,])
func_1469 = relay.Function([var_1441,], output)
mod['func_1469'] = func_1469
mod = relay.transform.InferType()(mod)
mutated_mod['func_1469'] = func_1469
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1470 = relay.var("var_1470", dtype = "int32", shape = (1, 11, 9))#candidate|1470|(1, 11, 9)|var|int32
func_1469_call = mutated_mod.get_global_var('func_1469')
call_1471 = func_1469_call(var_1470)
output = call_1471
func_1472 = relay.Function([var_1470], output)
mutated_mod['func_1472'] = func_1472
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1813 = relay.const([[[-2.697533,-5.784781,-9.814741],[-4.102497,-3.268029,-4.178663],[6.971266,2.145113,-8.016755],[7.943951,-4.458437,5.273450],[0.941201,-5.900694,-0.098670],[8.894553,-5.480799,-0.792252],[9.316776,-7.702756,-3.298708],[-6.534708,-6.664577,-3.863083],[7.474811,-6.135931,-4.141850],[-1.187228,9.290891,-1.540187]],[[-6.485376,-9.644113,6.991736],[-8.286876,2.668614,-1.395333],[1.979614,1.061749,-4.054568],[-7.044294,5.174189,-6.323609],[8.151882,7.849939,6.767174],[-6.924474,-9.899769,9.451106],[-5.590377,-8.139108,-6.738344],[3.673538,4.419843,0.549516],[-8.499361,3.581059,-2.196655],[9.479441,4.694277,-7.182456]]], dtype = "float64")#candidate|1813|(2, 10, 3)|const|float64
var_1814 = relay.var("var_1814", dtype = "float64", shape = (2, 10, 3))#candidate|1814|(2, 10, 3)|var|float64
bop_1815 = relay.mod(const_1813.astype('float64'), relay.reshape(var_1814.astype('float64'), relay.shape_of(const_1813))) # shape=(2, 10, 3)
bop_1823 = relay.subtract(var_1814.astype('float32'), relay.reshape(const_1813.astype('float32'), relay.shape_of(var_1814))) # shape=(2, 10, 3)
func_762_call = mod.get_global_var('func_762')
func_765_call = mutated_mod.get_global_var('func_765')
const_1829 = relay.const([8.975704,-7.644309,-6.482034,3.945825,2.987360,4.882948,2.778100,-4.348108,5.173936,-0.234627,-8.108540,-2.723498,-2.890915,-7.843990,7.235206,6.830348,6.008959,-5.964877,4.671488,1.432731,3.521207,2.765999,-0.520730,-7.147961,-4.296863,4.802031,-7.078275,6.856074,-2.211873,-0.576227,1.197977,-4.514079,-3.612302,-6.525499,6.378925,-9.018403,-2.033360,3.667055,8.095808,-8.132366], dtype = "float64")#candidate|1829|(40,)|const|float64
var_1830 = relay.var("var_1830", dtype = "int64", shape = (10, 63))#candidate|1830|(10, 63)|var|int64
call_1828 = relay.TupleGetItem(func_762_call(relay.reshape(const_1829.astype('float64'), [4, 1, 10]), relay.reshape(var_1830.astype('int64'), [630,]), ), 1)
call_1831 = relay.TupleGetItem(func_765_call(relay.reshape(const_1829.astype('float64'), [4, 1, 10]), relay.reshape(var_1830.astype('int64'), [630,]), ), 1)
uop_1833 = relay.tan(bop_1823.astype('float64')) # shape=(2, 10, 3)
func_1469_call = mod.get_global_var('func_1469')
func_1472_call = mutated_mod.get_global_var('func_1472')
var_1836 = relay.var("var_1836", dtype = "int32", shape = (99,))#candidate|1836|(99,)|var|int32
call_1835 = relay.TupleGetItem(func_1469_call(relay.reshape(var_1836.astype('int32'), [1, 11, 9])), 3)
call_1837 = relay.TupleGetItem(func_1472_call(relay.reshape(var_1836.astype('int32'), [1, 11, 9])), 3)
bop_1840 = relay.divide(var_1830.astype('float32'), relay.reshape(call_1828.astype('float32'), relay.shape_of(var_1830))) # shape=(10, 63)
bop_1843 = relay.divide(var_1830.astype('float32'), relay.reshape(call_1831.astype('float32'), relay.shape_of(var_1830))) # shape=(10, 63)
bop_1857 = relay.bitwise_xor(uop_1833.astype('uint16'), relay.reshape(bop_1815.astype('uint16'), relay.shape_of(uop_1833))) # shape=(2, 10, 3)
func_567_call = mod.get_global_var('func_567')
func_569_call = mutated_mod.get_global_var('func_569')
call_1868 = func_567_call(relay.reshape(call_1835.astype('float32'), [16, 7, 1]))
call_1869 = func_567_call(relay.reshape(call_1835.astype('float32'), [16, 7, 1]))
bop_1886 = relay.not_equal(uop_1833.astype('bool'), relay.reshape(bop_1857.astype('bool'), relay.shape_of(uop_1833))) # shape=(2, 10, 3)
bop_1895 = relay.minimum(uop_1833.astype('float32'), relay.reshape(bop_1815.astype('float32'), relay.shape_of(uop_1833))) # shape=(2, 10, 3)
output = relay.Tuple([const_1829,call_1835,var_1836,bop_1840,call_1868,bop_1886,bop_1895,])
output2 = relay.Tuple([const_1829,call_1837,var_1836,bop_1843,call_1869,bop_1886,bop_1895,])
func_1898 = relay.Function([var_1814,var_1830,var_1836,], output)
mod['func_1898'] = func_1898
mod = relay.transform.InferType()(mod)
mutated_mod['func_1898'] = func_1898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1898_call = mutated_mod.get_global_var('func_1898')
var_1900 = relay.var("var_1900", dtype = "float64", shape = (2, 10, 3))#candidate|1900|(2, 10, 3)|var|float64
var_1901 = relay.var("var_1901", dtype = "int64", shape = (10, 63))#candidate|1901|(10, 63)|var|int64
var_1902 = relay.var("var_1902", dtype = "int32", shape = (99,))#candidate|1902|(99,)|var|int32
call_1899 = func_1898_call(var_1900,var_1901,var_1902,)
output = call_1899
func_1903 = relay.Function([var_1900,var_1901,var_1902,], output)
mutated_mod['func_1903'] = func_1903
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1952 = relay.const([[[-1,7,2,-1,5,2,8,4,9,-4],[-2,10,-6,-4,9,-6,-5,-10,-1,2],[6,5,-9,-8,8,5,8,-9,-2,3],[-5,4,1,6,5,-7,3,-7,-8,1],[8,-7,3,3,1,9,-6,-3,-6,-9],[9,4,-8,6,-7,-4,-3,3,7,3]],[[3,-1,6,-6,-6,-7,-10,9,-3,6],[2,-5,10,-2,4,-6,-9,6,2,-2],[-6,3,10,-6,7,-3,1,-3,-5,-2],[10,8,5,-7,-7,-7,-7,-10,2,-10],[-7,7,8,-3,-5,-4,10,-6,-7,4],[-1,-6,1,5,-4,-4,7,-1,3,10]]], dtype = "int8")#candidate|1952|(2, 6, 10)|const|int8
var_1953 = relay.var("var_1953", dtype = "int8", shape = (2, 6, 10))#candidate|1953|(2, 6, 10)|var|int8
bop_1954 = relay.left_shift(const_1952.astype('int8'), relay.reshape(var_1953.astype('int8'), relay.shape_of(const_1952))) # shape=(2, 6, 10)
output = relay.Tuple([bop_1954,])
output2 = relay.Tuple([bop_1954,])
func_1964 = relay.Function([var_1953,], output)
mod['func_1964'] = func_1964
mod = relay.transform.InferType()(mod)
var_1965 = relay.var("var_1965", dtype = "int8", shape = (2, 6, 10))#candidate|1965|(2, 6, 10)|var|int8
output = func_1964(var_1965)
func_1966 = relay.Function([var_1965], output)
mutated_mod['func_1966'] = func_1966
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2132 = relay.const([[[False,True,False,True,False,True,True,True,True],[True,False,True,False,True,True,False,False,False],[True,False,True,True,False,True,False,False,False],[False,True,False,False,False,False,False,True,False],[False,False,False,True,True,False,False,True,True],[True,True,True,True,True,False,False,False,False],[True,False,False,True,False,True,True,True,True],[True,True,False,False,True,False,False,False,True],[False,False,True,True,True,False,False,False,True],[False,False,True,False,True,False,False,False,False],[False,False,True,True,True,True,False,True,False],[False,True,True,False,True,True,True,False,True]],[[True,True,True,True,True,False,False,False,True],[False,False,False,True,False,False,False,False,True],[True,False,True,False,False,False,True,False,False],[False,True,False,True,True,True,True,False,True],[True,False,True,False,True,True,False,False,False],[False,False,False,False,False,False,True,False,False],[True,True,True,True,True,False,False,True,True],[True,False,True,False,True,False,True,True,True],[True,False,True,True,False,True,True,False,True],[True,True,True,True,True,False,False,False,False],[True,False,True,False,False,True,False,False,False],[False,False,True,True,True,True,False,False,False]],[[True,True,False,True,False,False,False,True,True],[True,False,True,True,True,False,False,True,False],[True,True,False,True,True,False,False,False,True],[False,False,True,False,False,False,False,True,False],[False,True,False,True,False,False,True,True,True],[True,True,False,True,False,False,True,True,True],[False,False,False,True,False,False,True,False,False],[True,False,True,False,True,True,False,False,True],[False,True,True,True,False,False,True,True,True],[True,True,False,True,True,False,True,False,False],[True,True,False,False,True,True,True,True,False],[False,True,False,False,True,False,True,False,False]],[[True,True,False,False,True,True,True,False,False],[True,True,False,False,False,False,False,False,True],[True,False,False,True,False,True,False,False,False],[False,True,False,False,True,True,False,True,False],[True,False,False,True,False,True,False,False,False],[False,False,False,True,False,False,True,True,True],[False,True,True,False,True,True,False,False,False],[True,False,True,False,False,False,False,True,False],[False,True,False,False,True,False,False,False,False],[True,True,False,False,True,True,True,True,True],[False,True,True,False,True,True,False,True,True],[False,True,True,False,True,False,False,True,False]],[[False,False,False,True,True,False,True,True,True],[False,False,True,True,True,False,False,True,True],[False,True,False,True,True,False,False,True,True],[True,True,True,True,False,True,True,True,False],[True,False,True,True,False,True,False,False,False],[False,False,False,False,False,True,False,False,True],[False,False,False,False,True,False,True,False,False],[False,False,True,False,True,True,True,False,True],[False,False,True,True,True,False,True,True,False],[False,True,False,True,False,True,False,False,False],[False,True,True,False,True,True,True,True,False],[False,False,True,True,False,True,True,True,False]],[[True,False,True,True,True,True,False,False,True],[True,False,True,True,False,False,False,False,True],[True,True,False,False,True,False,True,True,False],[False,False,False,True,True,False,False,False,True],[True,False,False,False,True,False,True,True,True],[True,True,True,False,True,True,False,True,False],[False,False,True,True,False,True,True,True,False],[True,False,True,True,True,True,True,False,True],[True,True,False,False,True,True,False,True,False],[True,False,True,True,False,True,True,True,False],[False,False,True,True,False,True,False,True,True],[True,False,True,False,True,False,False,False,True]]], dtype = "bool")#candidate|2132|(6, 12, 9)|const|bool
var_2133 = relay.var("var_2133", dtype = "bool", shape = (6, 12, 9))#candidate|2133|(6, 12, 9)|var|bool
bop_2134 = relay.logical_or(const_2132.astype('bool'), relay.reshape(var_2133.astype('bool'), relay.shape_of(const_2132))) # shape=(6, 12, 9)
bop_2147 = relay.less(var_2133.astype('bool'), relay.reshape(const_2132.astype('bool'), relay.shape_of(var_2133))) # shape=(6, 12, 9)
output = relay.Tuple([bop_2134,bop_2147,])
output2 = relay.Tuple([bop_2134,bop_2147,])
func_2150 = relay.Function([var_2133,], output)
mod['func_2150'] = func_2150
mod = relay.transform.InferType()(mod)
mutated_mod['func_2150'] = func_2150
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2151 = relay.var("var_2151", dtype = "bool", shape = (6, 12, 9))#candidate|2151|(6, 12, 9)|var|bool
func_2150_call = mutated_mod.get_global_var('func_2150')
call_2152 = func_2150_call(var_2151)
output = call_2152
func_2153 = relay.Function([var_2151], output)
mutated_mod['func_2153'] = func_2153
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2385 = relay.var("var_2385", dtype = "float64", shape = (3, 1, 16))#candidate|2385|(3, 1, 16)|var|float64
uop_2386 = relay.log10(var_2385.astype('float64')) # shape=(3, 1, 16)
func_432_call = mod.get_global_var('func_432')
func_436_call = mutated_mod.get_global_var('func_436')
var_2397 = relay.var("var_2397", dtype = "int64", shape = (630,))#candidate|2397|(630,)|var|int64
call_2396 = func_432_call(relay.reshape(var_2397.astype('int64'), [15, 7, 6]), relay.reshape(var_2397.astype('int64'), [15, 7, 6]), )
call_2398 = func_432_call(relay.reshape(var_2397.astype('int64'), [15, 7, 6]), relay.reshape(var_2397.astype('int64'), [15, 7, 6]), )
func_1469_call = mod.get_global_var('func_1469')
func_1472_call = mutated_mod.get_global_var('func_1472')
const_2400 = relay.const([[2,8,-9],[-2,9,-7],[-6,3,-5],[8,-6,-6],[-7,-8,-9],[-8,6,-10],[-7,8,-4],[4,-7,9],[6,10,4],[4,-5,4],[7,-4,10],[-10,6,4],[-4,-9,-5],[-1,-8,3],[-4,-3,-7],[4,1,-9],[-2,7,-6],[8,-7,-2],[-5,-3,3],[3,1,10],[-5,4,-2],[4,-9,-4],[1,-8,8],[1,3,6],[-10,-5,7],[10,10,5],[-4,-10,9],[1,-5,-8],[-7,6,-5],[-5,-3,7],[-8,9,9],[-3,-4,-10],[-8,-5,-10]], dtype = "int32")#candidate|2400|(33, 3)|const|int32
call_2399 = relay.TupleGetItem(func_1469_call(relay.reshape(const_2400.astype('int32'), [1, 11, 9])), 2)
call_2401 = relay.TupleGetItem(func_1472_call(relay.reshape(const_2400.astype('int32'), [1, 11, 9])), 2)
output = relay.Tuple([uop_2386,call_2396,var_2397,call_2399,const_2400,])
output2 = relay.Tuple([uop_2386,call_2398,var_2397,call_2401,const_2400,])
func_2402 = relay.Function([var_2385,var_2397,], output)
mod['func_2402'] = func_2402
mod = relay.transform.InferType()(mod)
var_2403 = relay.var("var_2403", dtype = "float64", shape = (3, 1, 16))#candidate|2403|(3, 1, 16)|var|float64
var_2404 = relay.var("var_2404", dtype = "int64", shape = (630,))#candidate|2404|(630,)|var|int64
output = func_2402(var_2403,var_2404,)
func_2405 = relay.Function([var_2403,var_2404,], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2429 = relay.const([[[0.950367,1.623049,2.891919,-0.909898],[3.514262,7.568827,2.620956,8.409758],[6.401069,2.005193,-6.163648,0.033003]],[[-1.142915,-1.043771,-2.263006,-7.826683],[-0.145316,2.701142,-8.089535,-3.262704],[1.484896,4.538655,-7.052486,-1.394515]],[[-8.916303,-7.867754,-4.540192,6.766642],[8.729260,8.225589,5.116728,5.313944],[8.074383,-3.264101,-1.652988,5.722919]],[[-3.364165,7.406240,6.801047,-7.760254],[7.371732,-5.991626,-2.149443,-4.074546],[-9.204402,3.662039,3.140805,0.231168]],[[-0.872529,-6.542205,-0.296983,-7.047616],[1.087026,4.956893,4.234224,-0.741737],[-1.669366,-1.555264,4.425298,-7.956004]],[[-6.271259,8.237696,-3.089501,-5.889614],[-0.206357,-0.762928,-1.974756,0.020298],[-5.415842,-3.853400,-9.851970,-7.738582]],[[-7.671932,-0.939897,-0.214074,8.057388],[-1.498603,-0.010915,8.029752,8.957499],[-1.012037,-2.335312,-5.125949,-5.394555]],[[-2.394261,7.233089,8.980238,3.983289],[-4.420157,0.186054,3.204888,-1.226539],[-7.689216,-4.618449,7.154915,4.133019]],[[1.585526,1.220724,-2.092264,-3.893833],[-8.517375,7.941577,-4.709563,9.562780],[-3.790977,9.869603,9.731075,-2.725614]],[[-4.643476,6.264304,-4.790082,2.630715],[-6.254493,-3.144772,-6.847552,4.901493],[-5.449282,4.804675,-4.836765,5.754000]],[[9.314543,-1.450592,-2.897124,-9.600992],[3.998341,5.221432,0.988956,-9.153410],[4.817166,-6.056709,3.139434,-8.707357]],[[-7.489269,-0.240213,0.184151,-9.711980],[-0.626290,0.410606,5.197735,-5.799363],[-6.254615,-5.010715,-5.078107,6.719418]],[[7.944089,-8.309429,-7.119765,-7.699620],[-0.209922,3.469615,7.317212,-8.732600],[-5.390838,-1.446062,-2.247910,-3.525353]],[[-2.056478,-6.719949,5.516245,-4.237795],[5.486556,-3.013305,-7.472575,-5.016602],[6.652884,-5.262499,8.512939,3.662831]]], dtype = "float64")#candidate|2429|(14, 3, 4)|const|float64
var_2430 = relay.var("var_2430", dtype = "float64", shape = (14, 3, 4))#candidate|2430|(14, 3, 4)|var|float64
bop_2431 = relay.floor_divide(const_2429.astype('float64'), relay.reshape(var_2430.astype('float64'), relay.shape_of(const_2429))) # shape=(14, 3, 4)
output = bop_2431
output2 = bop_2431
func_2436 = relay.Function([var_2430,], output)
mod['func_2436'] = func_2436
mod = relay.transform.InferType()(mod)
mutated_mod['func_2436'] = func_2436
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2437 = relay.var("var_2437", dtype = "float64", shape = (14, 3, 4))#candidate|2437|(14, 3, 4)|var|float64
func_2436_call = mutated_mod.get_global_var('func_2436')
call_2438 = func_2436_call(var_2437)
output = call_2438
func_2439 = relay.Function([var_2437], output)
mutated_mod['func_2439'] = func_2439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2596 = relay.var("var_2596", dtype = "float32", shape = (2, 1, 9))#candidate|2596|(2, 1, 9)|var|float32
uop_2597 = relay.exp(var_2596.astype('float32')) # shape=(2, 1, 9)
bop_2599 = relay.minimum(var_2596.astype('uint64'), relay.reshape(uop_2597.astype('uint64'), relay.shape_of(var_2596))) # shape=(2, 1, 9)
uop_2608 = relay.sin(bop_2599.astype('float32')) # shape=(2, 1, 9)
output = uop_2608
output2 = uop_2608
func_2633 = relay.Function([var_2596,], output)
mod['func_2633'] = func_2633
mod = relay.transform.InferType()(mod)
var_2634 = relay.var("var_2634", dtype = "float32", shape = (2, 1, 9))#candidate|2634|(2, 1, 9)|var|float32
output = func_2633(var_2634)
func_2635 = relay.Function([var_2634], output)
mutated_mod['func_2635'] = func_2635
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3177 = relay.var("var_3177", dtype = "int32", shape = (1, 1, 1))#candidate|3177|(1, 1, 1)|var|int32
var_3178 = relay.var("var_3178", dtype = "int32", shape = (7, 1, 8))#candidate|3178|(7, 1, 8)|var|int32
bop_3179 = relay.add(var_3177.astype('int32'), var_3178.astype('int32')) # shape=(7, 1, 8)
output = bop_3179
output2 = bop_3179
func_3183 = relay.Function([var_3177,var_3178,], output)
mod['func_3183'] = func_3183
mod = relay.transform.InferType()(mod)
mutated_mod['func_3183'] = func_3183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mutated_mod.get_global_var('func_3183')
var_3185 = relay.var("var_3185", dtype = "int32", shape = (1, 1, 1))#candidate|3185|(1, 1, 1)|var|int32
var_3186 = relay.var("var_3186", dtype = "int32", shape = (7, 1, 8))#candidate|3186|(7, 1, 8)|var|int32
call_3184 = func_3183_call(var_3185,var_3186,)
output = call_3184
func_3187 = relay.Function([var_3185,var_3186,], output)
mutated_mod['func_3187'] = func_3187
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3192 = relay.var("var_3192", dtype = "int64", shape = ())#candidate|3192|()|var|int64
var_3193 = relay.var("var_3193", dtype = "int64", shape = (5, 5, 5))#candidate|3193|(5, 5, 5)|var|int64
bop_3194 = relay.bitwise_xor(var_3192.astype('int64'), var_3193.astype('int64')) # shape=(5, 5, 5)
output = relay.Tuple([bop_3194,])
output2 = relay.Tuple([bop_3194,])
func_3199 = relay.Function([var_3192,var_3193,], output)
mod['func_3199'] = func_3199
mod = relay.transform.InferType()(mod)
var_3200 = relay.var("var_3200", dtype = "int64", shape = ())#candidate|3200|()|var|int64
var_3201 = relay.var("var_3201", dtype = "int64", shape = (5, 5, 5))#candidate|3201|(5, 5, 5)|var|int64
output = func_3199(var_3200,var_3201,)
func_3202 = relay.Function([var_3200,var_3201,], output)
mutated_mod['func_3202'] = func_3202
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3352 = relay.const([[[-4.737410],[9.889667],[-9.562533],[6.578504],[-8.147554],[3.603246],[-0.601081],[1.555673],[8.374723]],[[0.173164],[-7.871933],[8.090894],[9.272586],[8.899921],[-0.489938],[-6.382172],[-2.999673],[-3.945207]],[[6.277117],[-5.453348],[-2.035618],[-0.659917],[6.672990],[9.796130],[-4.244642],[9.405407],[-3.580173]],[[6.451317],[0.415843],[-6.816767],[2.383860],[4.344069],[5.832774],[-5.988549],[5.029134],[-7.737271]],[[7.136507],[-2.996446],[-3.289782],[2.570274],[-7.811724],[-6.159528],[-9.534994],[-7.519990],[-2.854082]],[[6.582949],[1.425901],[2.953726],[-0.558358],[6.480911],[-3.854551],[-0.068818],[-7.583028],[-5.101128]],[[-7.976296],[-7.343500],[-0.615375],[-9.035103],[-7.920492],[7.465871],[2.560177],[-3.564259],[3.249238]],[[5.277990],[-3.323158],[6.721882],[-9.559609],[-5.364238],[-8.487345],[-3.172701],[-9.801290],[1.410623]],[[7.128428],[0.155063],[-3.318607],[-7.364337],[5.676066],[-1.580476],[-9.283360],[8.088315],[-3.412832]]], dtype = "float64")#candidate|3352|(9, 9, 1)|const|float64
var_3353 = relay.var("var_3353", dtype = "float64", shape = (9, 9, 15))#candidate|3353|(9, 9, 15)|var|float64
bop_3354 = relay.floor_mod(const_3352.astype('float64'), var_3353.astype('float64')) # shape=(9, 9, 15)
uop_3361 = relay.log2(var_3353.astype('float32')) # shape=(9, 9, 15)
output = relay.Tuple([bop_3354,uop_3361,])
output2 = relay.Tuple([bop_3354,uop_3361,])
func_3363 = relay.Function([var_3353,], output)
mod['func_3363'] = func_3363
mod = relay.transform.InferType()(mod)
var_3364 = relay.var("var_3364", dtype = "float64", shape = (9, 9, 15))#candidate|3364|(9, 9, 15)|var|float64
output = func_3363(var_3364)
func_3365 = relay.Function([var_3364], output)
mutated_mod['func_3365'] = func_3365
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3594 = relay.var("var_3594", dtype = "float32", shape = (1, 6, 6))#candidate|3594|(1, 6, 6)|var|float32
uop_3595 = relay.log10(var_3594.astype('float32')) # shape=(1, 6, 6)
bop_3603 = relay.bitwise_and(uop_3595.astype('int8'), relay.reshape(var_3594.astype('int8'), relay.shape_of(uop_3595))) # shape=(1, 6, 6)
bop_3607 = relay.floor_divide(uop_3595.astype('float32'), relay.reshape(bop_3603.astype('float32'), relay.shape_of(uop_3595))) # shape=(1, 6, 6)
func_1964_call = mod.get_global_var('func_1964')
func_1966_call = mutated_mod.get_global_var('func_1966')
const_3611 = relay.const([[-6,-1,4,-3],[7,-3,9,2],[3,-8,3,5],[4,-3,-9,-5],[7,8,-3,6],[-2,6,5,5],[-10,-10,6,-2],[-3,1,9,-1],[-3,8,9,-9],[5,2,-5,-9],[7,2,5,6],[-1,3,4,-6],[10,-6,-8,-10],[10,4,-9,4],[2,-3,-10,-6],[7,-10,-1,9],[-2,2,8,4],[6,-5,1,-2],[5,-2,4,5],[7,-4,6,4],[8,8,2,6],[-8,-4,2,3],[-1,4,5,9],[-7,-4,8,-10],[8,4,8,7],[-3,-6,-8,4],[-6,-7,8,-6],[-10,-9,-2,5],[-7,-9,9,10],[10,-8,-4,8]], dtype = "int8")#candidate|3611|(30, 4)|const|int8
call_3610 = relay.TupleGetItem(func_1964_call(relay.reshape(const_3611.astype('int8'), [2, 6, 10])), 0)
call_3612 = relay.TupleGetItem(func_1966_call(relay.reshape(const_3611.astype('int8'), [2, 6, 10])), 0)
func_3199_call = mod.get_global_var('func_3199')
func_3202_call = mutated_mod.get_global_var('func_3202')
const_3632 = relay.const(-3, dtype = "int64")#candidate|3632|()|const|int64
const_3633 = relay.const([[-6,-10,4,10,-4],[7,8,5,7,4],[4,-9,9,1,-7],[-7,-8,8,8,10],[-4,3,-9,5,6],[1,1,-5,9,6],[-6,1,-9,8,6],[1,-4,-2,-3,-8],[-8,8,-10,-2,8],[-7,10,-10,6,10],[3,9,-4,-10,-10],[3,-1,7,-4,2],[-8,8,-6,9,-4],[3,-8,7,-5,-8],[-9,-3,4,2,1],[-1,3,-7,10,1],[6,-5,6,8,-1],[6,-1,-10,1,4],[8,-10,-7,-9,6],[-2,4,7,-9,3],[5,-2,10,-1,6],[2,-3,6,-1,8],[5,-8,-9,-10,3],[-10,7,-5,4,8],[3,7,-2,7,-7]], dtype = "int64")#candidate|3633|(25, 5)|const|int64
call_3631 = relay.TupleGetItem(func_3199_call(relay.reshape(const_3632.astype('int64'), []), relay.reshape(const_3633.astype('int64'), [5, 5, 5]), ), 0)
call_3634 = relay.TupleGetItem(func_3202_call(relay.reshape(const_3632.astype('int64'), []), relay.reshape(const_3633.astype('int64'), [5, 5, 5]), ), 0)
bop_3636 = relay.subtract(bop_3603.astype('uint16'), relay.reshape(uop_3595.astype('uint16'), relay.shape_of(bop_3603))) # shape=(1, 6, 6)
bop_3642 = relay.bitwise_or(bop_3603.astype('uint64'), const_3632.astype('uint64')) # shape=(1, 6, 6)
func_3199_call = mod.get_global_var('func_3199')
func_3202_call = mutated_mod.get_global_var('func_3202')
call_3648 = relay.TupleGetItem(func_3199_call(relay.reshape(const_3632.astype('int64'), []), relay.reshape(call_3631.astype('int64'), [5, 5, 5]), ), 0)
call_3649 = relay.TupleGetItem(func_3202_call(relay.reshape(const_3632.astype('int64'), []), relay.reshape(call_3631.astype('int64'), [5, 5, 5]), ), 0)
bop_3652 = relay.left_shift(bop_3636.astype('int16'), const_3632.astype('int16')) # shape=(1, 6, 6)
func_2402_call = mod.get_global_var('func_2402')
func_2405_call = mutated_mod.get_global_var('func_2405')
var_3657 = relay.var("var_3657", dtype = "float64", shape = (48,))#candidate|3657|(48,)|var|float64
const_3658 = relay.const([-1,-2,-9,-6,-3,5,3,10,6,1,-2,2,6,-6,8,2,6,6,6,-6,-6,4,-9,-9,8,5,-5,-1,6,-9,-7,-4,4,-2,1,-1,9,8,-10,4,-9,7,6,2,7,8,2,-1,-1,7,1,1,-5,-9,-8,-2,-2,8,9,3,3,2,-3,-2,-7,8,-8,7,8,8,-1,-2,1,4,-3,-6,6,2,2,-4,2,9,9,-3,4,-4,2,-9,-5,3,-9,4,6,3,-1,-10,-8,-3,5,-5,-9,-5,2,-4,-6,-7,-5,-10,-9,10,1,3,9,8,3,-4,-2,-3,-2,3,5,4,-3,10,9,-9,2,-10,7,-6,1,3,8,8,-3,1,-1,8,9,-5,2,9,-6,-6,6,3,1,-1,-2,-10,-1,4,5,-7,2,3,6,7,-8,6,6,-3,5,-7,-6,3,7,1,-9,-6,-10,2,-8,9,3,-4,-5,3,5,-1,6,-8,1,-7,-8,9,2,4,-2,8,10,-2,10,-7,7,6,1,-8,-1,-1,8,7,-3,9,-5,9,-10,-10,-8,5,-4,1,-3,8,-6,5,8,5,4,-7,3,-6,-6,-3,-5,2,-9,7,-5,-8,-3,-4,-4,2,-5,8,-4,-10,3,9,-2,-9,5,3,-10,-1,-3,-4,6,-6,7,-8,8,-3,1,-9,4,-4,-4,9,5,5,-8,6,6,-4,5,6,-2,-4,-3,-6,9,-6,-4,-6,-8,8,1,10,5,2,8,3,9,10,10,-10,5,-1,2,9,-8,6,10,-9,-9,-7,3,4,-7,5,-2,6,1,-6,5,-3,-2,-4,-4,-9,6,-8,4,-10,-10,-8,-9,2,4,-3,3,1,6,8,-8,2,1,-2,4,9,6,8,4,5,8,-6,-7,-8,4,-4,-5,10,-6,2,-4,-6,8,8,-4,1,-3,4,-6,5,-8,-6,-5,8,9,-1,-3,-5,-3,-5,6,-8,3,-10,-4,-10,-6,-5,5,2,5,6,2,-9,2,1,-9,6,-3,-10,-3,-9,-1,10,10,-7,-5,3,4,-2,5,4,-2,-4,9,4,-8,-3,-9,-4,-2,4,-6,5,-8,-6,-8,-6,3,9,-6,7,6,-5,-2,-6,10,4,-8,5,5,10,4,-6,-6,2,-8,7,1,-2,1,-9,-1,-8,-1,-6,6,10,4,10,2,3,3,5,4,-4,7,-7,-6,7,7,2,1,-7,7,-6,-1,9,1,-5,3,-1,5,-9,10,-8,9,-2,1,7,9,9,2,-4,-3,-9,2,-9,7,-10,3,-6,10,-5,9,3,3,8,9,10,2,-10,-9,-1,-4,3,-1,-2,-9,1,6,8,5,7,-9,-6,6,5,-5,-10,-9,8,2,-10,6,-10,5,-6,-3,4,9,3,8,-1,-8,3,5,-7,3,9,9,4,5,-4,-2,-10,-10,8,-5,-2,9,-8,1,1,-3,3,-10,-5,8,3,10,3,-10,-2,10,-6,1,5,-1,6,-9,-5,-8,3,-2,6,-2,3,-9,-5,-9,10,-8,2,3,5,-8,8,3,-4,8,4,-10,-1,2,-10,8,-8,6,6,-9,1,1,5,-3,-8,8,10,-9,-9,-7,-9,-10,1,-1,7,-8,-7,-8,-5,-1,1,-3,9,1,2,-6,3,1,4,-1,-2,-7,-9], dtype = "int64")#candidate|3658|(630,)|const|int64
call_3656 = relay.TupleGetItem(func_2402_call(relay.reshape(var_3657.astype('float64'), [3, 1, 16]), relay.reshape(const_3658.astype('int64'), [630,]), ), 3)
call_3659 = relay.TupleGetItem(func_2405_call(relay.reshape(var_3657.astype('float64'), [3, 1, 16]), relay.reshape(const_3658.astype('int64'), [630,]), ), 3)
output = relay.Tuple([bop_3607,call_3610,const_3611,call_3631,const_3633,bop_3642,call_3648,bop_3652,call_3656,var_3657,const_3658,])
output2 = relay.Tuple([bop_3607,call_3612,const_3611,call_3634,const_3633,bop_3642,call_3649,bop_3652,call_3659,var_3657,const_3658,])
func_3674 = relay.Function([var_3594,var_3657,], output)
mod['func_3674'] = func_3674
mod = relay.transform.InferType()(mod)
mutated_mod['func_3674'] = func_3674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3674_call = mutated_mod.get_global_var('func_3674')
var_3676 = relay.var("var_3676", dtype = "float32", shape = (1, 6, 6))#candidate|3676|(1, 6, 6)|var|float32
var_3677 = relay.var("var_3677", dtype = "float64", shape = (48,))#candidate|3677|(48,)|var|float64
call_3675 = func_3674_call(var_3676,var_3677,)
output = call_3675
func_3678 = relay.Function([var_3676,var_3677,], output)
mutated_mod['func_3678'] = func_3678
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3707 = relay.const([[[-9.946199,3.606204,6.462952,9.424408,6.474328,5.526710,3.124014,6.091754,-1.094256,-5.149920,8.121233,-1.402016,7.603939,-3.994566,-0.845178],[9.586666,-3.688797,4.097293,-3.590337,4.127019,-1.583056,-7.289714,-8.464505,2.026904,9.525904,-9.081944,-5.946198,2.340493,5.810169,-8.142089],[0.629990,-6.663090,-6.240171,-6.788565,-6.583213,4.196118,-1.543797,-3.238192,6.743601,1.642407,-5.270030,-4.737160,-0.493182,-0.347073,6.402627],[4.762724,-0.509614,-7.552623,4.906442,2.406486,7.440627,3.441050,5.832265,-7.550301,8.259943,0.487753,1.794979,1.417049,-8.862864,1.605432],[-6.871771,-8.650479,-7.612357,-9.060106,1.308388,5.756811,-5.449310,6.619813,9.384244,-4.502302,5.276233,-4.875633,5.958381,6.176604,4.793683],[-9.955132,9.161283,-9.582105,6.645880,-5.182739,4.147850,8.516403,-6.727774,9.915559,-9.179178,-9.605806,4.781037,-1.091313,-1.668425,-6.913650],[-2.617651,-3.034848,-9.520386,5.080247,4.421663,-1.555541,-3.208064,-3.032695,-2.400906,-1.970299,9.450036,2.840172,1.955178,-8.370222,8.687972],[3.146827,3.749043,4.409106,-9.887000,3.065646,-2.188147,-3.473799,-8.818074,5.867510,-9.285096,2.769065,4.470928,2.810049,0.970385,-8.301793],[-8.863648,-6.794946,0.381338,0.030310,0.489075,8.779563,7.703469,-4.157129,-4.121820,-1.790070,8.853257,4.624756,-4.607517,0.805875,-0.302620],[-9.436041,1.822177,-3.534845,0.111404,-9.744990,-6.341383,-8.976371,-0.503741,8.323927,3.926386,5.108154,-2.107733,0.337148,8.278456,-9.655871],[-3.262547,3.575315,5.178158,4.242820,6.106909,8.734935,3.777976,3.165261,-0.955005,4.224376,7.490007,-4.204073,3.804094,-6.972308,-2.888457],[-4.600904,-7.636946,-1.599395,8.591771,-0.976184,-5.714694,-4.408333,6.163224,5.497553,8.760213,6.322444,4.332729,-0.567342,3.579923,-0.157678]],[[9.188302,6.346190,-0.364893,9.397649,6.801580,-1.014368,-4.680739,3.797440,5.191507,1.698611,4.388239,2.990549,5.943138,6.793272,-5.219104],[-8.425557,-4.860956,6.808998,-7.511641,-9.178870,-9.773133,3.132357,-9.306224,8.742378,8.082391,-3.292856,9.462092,1.005804,0.672932,-3.167449],[-5.408343,3.914401,-5.851335,7.144198,4.325486,-0.624510,9.480889,-2.269399,-5.423753,2.732384,5.196657,1.466810,7.658616,7.104736,7.903365],[-9.267517,-0.451015,3.022606,2.397513,4.902568,-2.166759,-3.319795,1.170871,4.487522,-5.414997,8.270855,-3.786087,8.311272,-1.016313,-5.821363],[-9.252236,4.708024,-2.541655,1.441806,-2.373871,1.562359,-4.533392,-2.337490,-6.687101,0.422523,-7.017099,-6.765362,3.941958,-2.633883,-8.274653],[-9.592366,4.243386,-5.812563,-2.947503,2.955359,-1.803706,7.422447,1.867454,3.779114,-0.114890,-2.239086,7.207088,3.382394,-1.241548,-2.918948],[3.719471,0.684491,1.478048,-0.993905,0.683819,-4.700368,-0.553230,-6.991048,7.849404,-8.383917,6.412140,-9.353338,3.553850,5.944666,3.455705],[1.643147,-0.289192,0.582974,-9.095949,8.261523,-4.698758,9.314303,-4.449264,-1.915593,8.501827,6.744423,4.760731,-9.757544,6.258915,4.463887],[8.713472,6.620863,2.787645,7.773760,5.681929,-2.508123,-4.633041,-7.907015,4.876099,-5.104205,4.157247,1.554283,7.179205,-2.311987,-9.691770],[7.176737,-1.526604,0.921960,-7.421007,0.470913,-6.325969,3.992037,7.959349,5.342526,-8.942565,-5.610339,6.808781,-6.434733,6.768883,6.314926],[-9.906659,4.211715,-9.932579,9.217586,-3.136063,-0.359844,-0.123508,0.398897,7.251318,-8.454525,3.599104,-5.226382,1.296898,7.810469,1.047935],[-5.888767,-7.744513,-1.881459,-3.233588,6.077281,-2.394196,7.300985,4.024701,-0.797275,3.102631,-9.853022,5.760010,5.125686,0.028191,5.459894]],[[-3.250038,8.758556,-4.175083,0.788540,1.376861,1.608481,-0.768506,-7.585570,6.691332,-6.767131,2.115113,7.512976,3.831744,4.264027,-4.239270],[1.722377,-9.702317,3.957109,-9.089438,-6.172691,2.062555,7.043869,-1.155788,3.886579,6.126295,8.441418,-3.536846,9.250330,4.572646,-8.987683],[-3.127411,-5.518811,-2.572679,3.548526,-7.864342,-6.956639,6.798855,7.218498,2.448518,7.725599,1.581353,-9.914403,-2.223152,0.562211,-8.034568],[8.841962,-0.362784,-1.010775,0.178531,6.817509,1.233013,0.329551,-4.026452,-3.328225,9.966462,-6.320539,-9.935986,-7.771724,-1.747523,7.431096],[0.931743,5.390738,-2.321122,9.048750,6.271282,-9.815082,-0.890977,8.055031,-9.697224,4.931177,-5.326627,-5.435172,-6.703317,4.367241,7.016807],[4.731327,8.172975,-8.400307,-8.703666,4.765872,-6.168501,-8.375662,4.923424,1.782122,-0.384205,5.564675,-7.638141,5.686998,-3.714025,-6.486958],[2.838367,-9.534658,-1.245038,6.162113,-0.664186,7.975833,-9.033631,-1.391138,5.154976,6.345926,-1.913522,-4.292522,1.548612,6.661675,-0.128144],[9.253478,7.706013,-1.852433,-8.879377,3.118599,-1.929385,1.140371,-3.374555,-1.454267,-4.620489,9.607787,-7.302846,9.311796,-6.318522,8.528525],[-4.019088,-6.777580,8.808356,-2.019620,-0.745923,-1.517430,-3.837959,8.343854,3.077178,-9.640179,-2.691167,-6.115680,-7.518259,-0.686304,-7.620965],[1.013170,-8.510320,9.046180,3.143227,4.372688,7.753066,-1.468074,2.689798,-4.982253,-5.841214,-1.607940,2.510710,3.237748,2.722344,-2.852041],[-0.340413,-7.843071,3.029321,-5.469864,7.486307,7.224613,2.475862,-9.969705,0.944570,-9.884422,-2.265346,-1.104401,5.554204,1.883159,0.660321],[5.119512,8.951819,-9.639831,0.534062,0.942844,-0.441332,1.364829,7.372180,9.367175,-9.703517,-3.001730,-7.805682,-9.928355,-3.087546,-8.407288]],[[7.844134,2.516343,-8.530271,-7.178738,-5.914324,-3.109678,-5.671880,3.575392,-4.177591,-9.990591,-8.209367,1.659787,-3.036678,-0.180535,8.003502],[-2.738260,-2.291192,2.804479,-5.112127,-9.693682,-0.255084,2.189947,-7.704439,-1.575887,6.759771,-5.081324,0.400901,7.699611,6.552677,-1.351059],[-9.295388,-8.631939,8.617810,8.511287,3.532003,-4.729109,9.598916,-9.910168,-0.305729,-8.241953,9.389206,3.217847,-0.174729,-7.243429,4.864902],[-3.289316,-5.012814,-0.034604,-3.736461,2.308146,-9.818997,1.812134,3.910526,6.892922,-0.586014,-4.911499,-9.324997,-7.245075,-0.020278,1.237126],[-0.913757,9.847530,-2.631582,-5.986291,-5.444980,-4.635838,7.174715,-5.649750,2.091350,2.800703,3.098013,9.121734,9.564360,-2.244146,5.859769],[8.817521,7.985342,-9.121912,5.665136,-8.274071,-0.127063,-0.033977,8.847202,-7.345054,-4.041278,-8.820547,1.477354,-2.748097,-1.544148,-4.668734],[-2.187169,6.766643,3.117228,3.380831,-1.695800,-4.454275,-5.415798,-5.835978,9.834010,-1.878134,-0.216052,4.086028,-4.356136,1.274373,-1.708884],[-1.440806,8.133043,-8.141440,9.306278,4.384923,5.817073,-0.920939,-0.174537,9.210894,-1.514318,-6.367503,2.437435,-6.700722,0.848403,-4.359845],[-9.106938,-0.422612,-8.715914,-3.561394,-1.193623,4.940194,9.828784,3.526087,-5.119175,2.352197,-4.678706,-4.202819,9.382255,6.680691,-8.852256],[-3.389915,7.630989,-1.377933,1.916633,7.330818,7.877254,1.215569,7.386799,-0.275218,-9.408026,-0.591518,2.888663,-4.101449,5.104046,3.748899],[3.560197,-3.133762,-8.351989,-8.772844,6.549314,3.954466,-0.415459,5.748217,2.435817,4.222225,2.571855,-9.624248,-3.993612,9.218243,0.682884],[3.032786,-0.132381,6.076630,7.942284,-3.887172,5.707462,7.407228,6.074744,6.125137,-2.766638,-7.126913,-2.475663,9.170531,9.637517,4.742956]],[[5.541413,5.386849,-1.601495,2.939532,-8.815577,1.371557,0.387152,8.824997,7.694196,-9.105751,1.852379,-7.089262,6.201190,2.872808,-2.554557],[1.939963,3.368498,-3.979387,5.926273,5.160964,8.504156,-0.182218,5.464466,3.152997,-0.359768,9.299494,-2.194000,-1.520844,3.088995,-0.145293],[-8.518784,6.388188,-9.747950,6.905054,7.149327,6.542459,1.035441,-6.122199,5.305131,-8.052382,8.935701,-0.439233,7.800850,2.857259,-0.122328],[-1.890275,-6.009328,-0.769788,2.284935,-9.925420,2.135561,-5.217867,7.429388,9.072382,-4.823520,9.331934,6.130844,-5.164669,-3.749723,2.720591],[9.858285,7.965617,-6.147590,1.954504,3.800454,-0.774418,2.321711,-1.789520,2.163250,-1.493478,5.076659,8.542641,7.391505,7.551230,-0.133066],[-0.865791,-5.920134,5.610964,9.407694,3.132730,-9.213245,4.939158,-9.573406,9.544871,-3.009265,7.374205,6.289027,-3.509153,-0.594777,-4.825951],[5.829478,4.711471,-5.217780,-5.809042,8.537570,-6.943624,6.755900,5.420751,7.675110,-0.599869,-1.459218,3.381069,-3.174169,-4.408066,0.140733],[9.241181,4.385420,5.679149,9.596405,-5.303740,0.208737,0.587284,-3.225878,-8.264790,8.676608,5.367648,-0.060619,3.802965,3.409021,-6.955812],[-8.109994,4.977090,-6.644094,7.547854,-1.891855,-3.137038,-6.936034,-3.084763,-7.028799,9.112313,6.276618,-5.285519,8.676903,0.587260,7.393586],[-7.476220,9.172432,-7.076302,-7.745189,-4.837755,9.444576,-1.737428,-4.429442,-0.535435,7.654680,-9.679525,6.613546,-4.766993,-1.524628,3.404997],[8.660802,2.244285,6.702049,-9.037521,2.670505,-0.551591,5.637177,-6.177637,9.917528,6.534636,-3.794535,-6.550375,-6.213507,2.586237,-4.954570],[-7.180029,-9.906119,-7.582265,4.572515,3.460406,6.170982,1.031280,-0.595890,-2.182748,5.355648,-1.038093,6.268744,7.703279,4.401158,-8.674938]],[[1.593222,-0.641029,-0.196848,5.894578,9.801442,-1.420305,-7.173675,-7.262653,-2.537907,-8.403272,-6.829509,5.201241,0.479512,0.227937,0.693703],[-6.542673,-0.155457,-1.388597,-3.740303,3.766637,-2.273074,-3.104626,7.398766,4.207054,-0.186894,6.184612,-4.307123,-2.059887,2.692227,1.017366],[-2.848576,7.557273,-7.103796,1.760699,8.360444,-8.602941,0.481529,-9.917377,2.287958,-0.062948,-6.055101,-4.932179,-5.495960,-4.191221,-2.581472],[2.677005,-8.105582,-7.478283,-4.342279,6.589117,-9.737879,-8.716299,-6.574163,-0.689836,-3.528583,7.297677,7.531745,-8.107199,0.103208,5.809068],[-3.113832,-1.482489,-5.804054,1.672938,-1.878907,-3.126635,-0.789347,-9.253459,-3.836501,2.899208,8.556899,8.030107,-5.976353,9.598296,-6.095613],[-8.100373,0.988905,9.456292,2.565542,-7.311744,8.369604,-3.683242,1.173604,7.622332,5.546260,1.858291,3.237792,3.038293,-4.612832,9.700260],[-8.868316,7.060992,-6.756784,7.967318,0.604821,-6.795643,-9.193101,-3.112268,3.776575,7.244062,-9.966287,-1.815477,9.542660,-3.427883,-7.951538],[8.781343,1.562006,-4.817388,9.782668,5.040099,7.265275,-3.695963,-6.705543,-2.549660,-8.344618,-8.250967,-0.600154,-5.227345,5.781265,3.409733],[7.125852,-7.809676,5.412208,-2.517397,-2.424862,0.564748,0.347346,0.050630,-6.608273,-1.420989,-3.351671,-7.090739,0.125695,-3.105118,2.603195],[-3.828704,-1.061410,7.308028,2.106247,8.302661,8.159246,7.382217,-3.238902,-3.561091,-4.548812,4.357151,2.320901,9.591150,-0.162423,2.838263],[2.147385,-4.934060,-0.375175,0.422878,-9.667923,8.434587,8.365987,-6.576210,-1.481899,9.250135,4.130342,4.308565,-3.536838,8.113307,-8.096493],[-3.300093,-8.206476,-2.765457,-1.655075,-5.898123,-4.622928,-4.324029,8.197413,4.187161,2.615947,-2.063640,3.580328,2.316653,8.220528,-5.175785]],[[-4.040576,9.307506,-7.868092,4.242148,-2.813038,0.300509,-1.633684,-7.404744,-5.878801,3.800597,-8.626065,4.557472,9.714074,2.324712,6.773999],[-6.165184,-1.004461,3.157247,0.021018,2.835905,-3.666483,-2.065179,-4.179695,-5.069967,-6.687973,-2.882718,-7.692737,-1.847605,7.049154,-5.094304],[-8.786771,-0.279646,-8.605224,3.821854,-4.819313,6.276922,9.963399,7.218597,7.323147,-8.114948,9.332867,-3.599830,-3.531752,4.444052,6.501888],[6.884220,5.019174,-3.079291,9.880923,5.812852,9.033514,-7.420985,8.190326,-7.748193,-2.117379,-8.991944,-3.567420,0.294029,-9.643371,-8.839029],[-6.706165,9.506710,5.958790,1.076790,0.181881,-9.246187,-5.771819,4.291370,6.370963,-8.531919,-8.519771,6.697823,3.383596,-9.425790,-6.976894],[9.212551,-5.061579,-9.735950,7.533776,-5.931294,-2.838268,5.297759,6.303344,-1.616623,-4.485439,-4.130821,-5.592351,6.408240,-7.842681,7.929825],[-0.132707,0.787788,7.495385,-1.211427,-9.985506,8.446949,-0.972614,7.187482,4.126985,-6.310673,-4.214507,-2.856762,-7.923411,-5.937126,6.277520],[4.720394,3.999018,-2.932900,-3.308675,6.319375,3.366779,-9.002877,9.644839,-3.093136,0.268741,-5.418993,6.433367,-4.102721,8.117744,6.472103],[-6.579179,-2.666053,5.859110,-1.280834,-0.642793,-8.177055,-2.891775,1.058158,-5.073042,-1.051758,-9.791213,7.011679,-9.542869,5.024610,2.232082],[-9.772924,-9.620877,2.180253,-3.497063,8.733057,7.362252,-7.534656,-6.907990,2.165127,6.656277,7.319556,-3.374534,-7.255336,-7.080855,-9.277914],[-8.454715,-1.773160,-0.867591,-3.447457,8.763479,6.682983,-0.776310,8.630302,2.677192,3.875104,-0.336705,-7.072826,-8.058078,4.745067,-1.116283],[-0.504719,7.223338,6.727167,-5.468913,-8.986810,-8.509910,-5.950748,9.194071,9.970964,-5.480291,-6.097585,0.861063,9.384623,3.333085,9.309178]],[[8.646979,-7.331238,-4.665400,-1.612378,7.807364,-9.010999,-8.152796,-4.135299,-4.073609,-8.590022,1.163239,-2.875374,1.083101,-0.239348,-7.293987],[-0.959451,6.843027,-3.573614,5.336783,-5.163994,5.446921,-2.890857,9.400367,-0.402882,-9.502594,-5.468585,2.290431,3.308529,-3.838418,7.048324],[3.386858,-5.568902,-3.484602,-9.664527,1.705916,-1.297301,2.637212,-5.345133,-0.640410,6.283088,4.597334,-5.280929,-1.990449,1.316600,1.060237],[6.525661,6.563998,8.614005,3.747613,7.296025,-0.818795,9.062296,-4.810713,-2.572727,-7.305110,1.952891,1.376870,-3.785456,3.029239,-5.656238],[-1.701556,7.495403,-5.238312,9.857157,-2.522994,-1.069854,3.914080,5.520523,-6.625234,-3.248718,3.764142,-0.731994,8.157487,-3.654503,1.506706],[9.558372,-3.842180,0.984745,5.457645,-1.079063,3.263833,-6.233734,6.830250,-8.087035,1.120299,-7.905823,-3.966301,7.030236,-9.984692,7.135121],[-6.317887,5.303823,4.679009,2.683584,-5.500240,7.169928,3.304309,-5.461367,8.968892,-7.380762,1.477683,8.191625,1.013719,2.657744,-7.324784],[9.999782,7.468839,0.111640,6.008698,7.971881,0.640662,4.714122,-5.808508,9.858076,-2.099800,-4.823527,-6.368603,-7.474047,-9.160743,8.487733],[-5.316270,9.440870,-0.918875,-2.145742,-5.262801,3.767432,-8.768739,-0.265109,-2.505344,-6.272895,5.321312,-8.081042,-7.967804,0.051609,-8.967541],[5.763265,-9.673555,-3.749415,-6.605997,-2.577177,-0.883196,-8.240507,9.078470,3.815776,-1.830726,-3.217792,-5.026756,2.035915,8.770018,0.685283],[-5.838368,-7.781136,3.827163,8.114939,-1.383991,-0.626456,6.423071,3.499399,0.901440,-4.237039,5.041776,5.907961,3.342258,-1.113576,-3.629246],[-7.513538,0.428858,3.650562,6.933342,-7.029436,-2.562853,-9.276381,0.610851,-3.348626,-6.453924,-1.760577,-6.793067,2.839537,-7.487382,-6.004326]],[[9.673440,7.187679,-8.201515,7.102992,0.445285,7.834506,6.706961,3.507442,8.249250,0.005520,-7.497672,3.473725,-2.862021,-1.918638,2.383444],[3.710636,0.580511,4.324272,1.280340,7.553423,-1.601035,-4.148761,-7.679080,-9.233884,-6.137990,7.606082,0.493088,4.704125,9.524014,-9.088969],[-9.410211,2.009921,0.100761,4.595699,-7.941775,1.181121,0.463514,-8.237959,-4.820630,-4.405555,-3.375951,3.185146,-4.671124,7.417280,0.018611],[-6.569318,4.797180,1.793222,-3.532127,9.155462,-3.893904,6.956435,7.177913,2.469227,-0.274319,-3.711554,-6.823319,-7.348867,-2.078972,-3.792975],[-8.729773,8.630021,4.319459,-6.959305,-6.826734,-2.497651,-0.161858,-6.526868,2.377804,1.667278,0.561543,-3.904832,-9.732320,8.098463,2.414123],[-9.493457,-3.320052,8.657385,-5.771940,-6.922938,-9.985625,4.642017,-9.212946,-7.542513,-1.240125,-9.937745,5.419678,9.453995,1.239512,-9.702677],[-2.262522,-6.568371,-0.054152,-2.043111,9.572661,1.171029,1.068317,0.688454,7.641178,6.756396,5.679486,4.106821,9.528690,-5.668640,5.638893],[3.679240,9.930072,5.732990,8.644417,2.474049,-6.094041,-1.538146,7.391094,0.582956,6.514486,-4.371237,-1.105244,0.217480,-4.119755,0.619659],[-0.411493,-6.814749,-8.480373,-7.223195,5.599852,4.226408,-3.332561,-9.605173,3.356419,-4.996204,-3.079983,5.517382,7.850612,-2.932132,7.194083],[9.393825,-3.798528,9.509240,6.572333,5.985315,5.882690,-0.038512,-4.380790,-5.528453,5.292297,0.799009,1.892618,-6.729576,4.180745,5.872948],[-3.922052,5.707818,-6.646923,-3.984369,-6.297929,-0.514850,-5.838609,8.531094,6.844654,-9.495002,1.369432,6.546301,-0.410817,4.402895,-6.615186],[-5.344552,2.903551,-5.183188,1.268375,-4.515053,-9.495703,5.228123,3.838421,1.592729,-4.410440,3.158333,9.201851,0.554543,8.576472,-4.472000]],[[7.075069,-2.435055,-9.985286,-7.566602,1.194109,3.953401,2.512129,-5.047977,9.158195,-8.185976,6.301491,6.936532,-5.825877,3.324828,4.491347],[7.938578,-5.205318,-7.655142,-0.005168,-6.074561,4.024049,3.797861,8.917628,5.298874,-7.683791,-1.817391,-0.959644,-3.876226,-4.361581,-2.964790],[0.432997,-7.188756,8.030440,-5.190051,3.913255,-3.436341,-5.611233,-7.673339,7.642693,0.123197,8.259024,-5.583456,8.955570,-1.446161,-6.384362],[-0.475335,-1.507778,9.156760,7.916402,-4.497045,1.824110,5.959211,-7.916372,2.834531,3.666724,9.399121,-5.200146,-5.547496,6.016269,-6.996646],[2.515770,6.266760,4.883402,-3.651112,3.785502,-7.324842,5.277136,-8.166345,3.819886,0.967385,-4.902973,7.417185,-8.717756,9.620526,-7.709742],[7.696378,-6.682170,5.374686,-9.429928,-8.638467,-1.496648,-4.234452,-7.464114,-2.448722,-4.751291,-9.833002,-7.330276,2.212578,-8.615416,-9.775252],[-5.990063,-4.890176,8.834441,4.755112,8.864617,5.205007,-2.738108,4.570529,-2.010896,-3.304103,-3.405264,-1.615099,-1.683747,6.557949,-1.316141],[8.545273,-3.041420,6.288592,7.519233,4.375053,-7.326275,9.970217,-2.052366,9.922721,-3.944871,5.089110,-6.496859,4.222811,4.246513,0.986610],[7.899945,9.629130,5.253104,1.813278,8.062738,0.375653,9.364513,-5.092689,-6.253862,-9.466345,3.516898,0.480891,6.383087,-5.051395,4.135002],[-3.693215,-9.741404,-3.660543,-0.974810,-8.521696,-8.074204,8.063972,-9.544204,2.612327,5.131227,7.954710,1.893715,1.239701,-2.816146,-7.345275],[2.754729,-2.336003,-5.011910,9.713067,-1.141018,-5.462177,-4.498717,-4.862418,7.020053,3.372484,0.248665,9.237940,4.850055,-7.230187,-8.920455],[4.023285,2.322711,0.034063,5.687647,6.690313,-3.490320,-9.653069,6.682825,-1.204391,2.576736,-9.564628,-6.683064,0.622818,-0.719785,0.472877]],[[-3.368581,-7.828886,-3.082127,7.956742,4.035908,3.015634,-2.398870,-0.767849,-9.760557,-7.144585,-3.333504,7.728401,-4.090172,-5.305133,-3.906336],[0.286367,-2.429931,-6.598792,2.591462,-6.484022,-4.636085,5.197131,-8.941466,9.348490,-1.467033,-7.919458,-0.118745,8.031335,-0.160679,8.394912],[-0.445340,-8.308285,-3.844223,4.184036,-5.622715,-6.674587,-0.572652,-6.183326,9.084019,8.716302,3.197678,-7.200803,5.557160,2.511119,7.401331],[-5.730185,6.692973,6.474632,-4.396532,-8.556002,-8.133564,7.045959,-8.541832,7.517835,4.415841,6.567897,-4.754688,-4.273826,5.337598,-1.862467],[-1.647635,-7.309808,9.476456,-2.225194,4.206735,-2.022082,3.574000,-4.253093,1.108816,-2.435667,-6.210998,-2.544383,1.889133,8.866292,-2.687221],[-1.902097,-0.879104,-0.771008,-4.522861,1.326165,6.064981,2.579482,-5.345100,-6.606138,-2.537362,-3.303630,-7.621544,5.551823,-5.066194,4.439312],[-1.006425,4.579372,-4.298930,-3.763242,-5.536264,-0.758103,-0.247218,0.114455,9.114399,-4.014151,-9.996209,6.154200,5.140776,-6.109433,2.270328],[-5.173281,1.862490,-6.520057,-8.982222,-8.988002,4.471997,-5.365758,9.663733,-7.642829,-1.313634,-7.577260,9.264969,0.782078,-3.465351,-5.126558],[2.918521,-3.766375,4.818748,7.956036,7.655575,-8.676707,-5.017719,-5.877149,-4.712740,8.419350,-2.815741,7.559573,1.987112,-9.765809,5.783217],[5.817513,-0.077303,0.723651,-2.362684,4.748723,9.720475,-9.726451,-4.461475,3.619140,7.383835,2.197764,-7.106296,-6.330541,-6.448894,3.367218],[5.001162,-2.658987,-6.828191,7.015232,-2.986158,6.375191,2.132596,-3.874588,-7.015151,-6.962577,-4.065580,0.708734,4.683873,-4.822676,8.371384],[8.180297,-0.922762,-8.610521,6.744533,4.552276,-3.999892,7.103732,4.994432,6.906251,0.537422,0.689879,-6.688856,-5.497508,-0.591032,8.574697]]], dtype = "float64")#candidate|3707|(11, 12, 15)|const|float64
uop_3708 = relay.erf(const_3707.astype('float64')) # shape=(11, 12, 15)
output = relay.Tuple([uop_3708,])
output2 = relay.Tuple([uop_3708,])
func_3714 = relay.Function([], output)
mod['func_3714'] = func_3714
mod = relay.transform.InferType()(mod)
mutated_mod['func_3714'] = func_3714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mutated_mod.get_global_var('func_3714')
call_3715 = func_3714_call()
output = call_3715
func_3716 = relay.Function([], output)
mutated_mod['func_3716'] = func_3716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_3745 = relay.TupleGetItem(func_3714_call(), 0)
call_3746 = relay.TupleGetItem(func_3716_call(), 0)
output = call_3745
output2 = call_3746
func_3765 = relay.Function([], output)
mod['func_3765'] = func_3765
mod = relay.transform.InferType()(mod)
output = func_3765()
func_3766 = relay.Function([], output)
mutated_mod['func_3766'] = func_3766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_3780 = func_3765_call()
call_3781 = func_3765_call()
func_1090_call = mod.get_global_var('func_1090')
func_1094_call = mutated_mod.get_global_var('func_1094')
const_3799 = relay.const([True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False], dtype = "bool")#candidate|3799|(208,)|const|bool
const_3800 = relay.const([True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,False], dtype = "bool")#candidate|3800|(1456,)|const|bool
var_3801 = relay.var("var_3801", dtype = "float32", shape = (28, 4))#candidate|3801|(28, 4)|var|float32
call_3798 = relay.TupleGetItem(func_1090_call(relay.reshape(const_3799.astype('bool'), [13, 16, 1]), relay.reshape(const_3800.astype('bool'), [13, 16, 7]), relay.reshape(var_3801.astype('float32'), [112,]), ), 2)
call_3802 = relay.TupleGetItem(func_1094_call(relay.reshape(const_3799.astype('bool'), [13, 16, 1]), relay.reshape(const_3800.astype('bool'), [13, 16, 7]), relay.reshape(var_3801.astype('float32'), [112,]), ), 2)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_3805 = func_3765_call()
call_3806 = func_3765_call()
var_3809 = relay.var("var_3809", dtype = "bool", shape = (208,))#candidate|3809|(208,)|var|bool
bop_3810 = relay.minimum(const_3799.astype('uint16'), relay.reshape(var_3809.astype('uint16'), relay.shape_of(const_3799))) # shape=(208,)
output = relay.Tuple([call_3780,call_3798,const_3800,var_3801,call_3805,bop_3810,])
output2 = relay.Tuple([call_3781,call_3802,const_3800,var_3801,call_3806,bop_3810,])
func_3826 = relay.Function([var_3801,var_3809,], output)
mod['func_3826'] = func_3826
mod = relay.transform.InferType()(mod)
mutated_mod['func_3826'] = func_3826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3826_call = mutated_mod.get_global_var('func_3826')
var_3828 = relay.var("var_3828", dtype = "float32", shape = (28, 4))#candidate|3828|(28, 4)|var|float32
var_3829 = relay.var("var_3829", dtype = "bool", shape = (208,))#candidate|3829|(208,)|var|bool
call_3827 = func_3826_call(var_3828,var_3829,)
output = call_3827
func_3830 = relay.Function([var_3828,var_3829,], output)
mutated_mod['func_3830'] = func_3830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_3850 = relay.TupleGetItem(func_3714_call(), 0)
call_3851 = relay.TupleGetItem(func_3716_call(), 0)
output = call_3850
output2 = call_3851
func_3853 = relay.Function([], output)
mod['func_3853'] = func_3853
mod = relay.transform.InferType()(mod)
mutated_mod['func_3853'] = func_3853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3853_call = mutated_mod.get_global_var('func_3853')
call_3854 = func_3853_call()
output = call_3854
func_3855 = relay.Function([], output)
mutated_mod['func_3855'] = func_3855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_3869 = func_3765_call()
call_3870 = func_3765_call()
var_3873 = relay.var("var_3873", dtype = "float64", shape = (11, 12, 15))#candidate|3873|(11, 12, 15)|var|float64
bop_3874 = relay.not_equal(call_3869.astype('bool'), relay.reshape(var_3873.astype('bool'), relay.shape_of(call_3869))) # shape=(11, 12, 15)
bop_3877 = relay.not_equal(call_3870.astype('bool'), relay.reshape(var_3873.astype('bool'), relay.shape_of(call_3870))) # shape=(11, 12, 15)
uop_3878 = relay.acosh(call_3869.astype('float64')) # shape=(11, 12, 15)
uop_3880 = relay.acosh(call_3870.astype('float64')) # shape=(11, 12, 15)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_3881 = func_3765_call()
call_3882 = func_3765_call()
output = relay.Tuple([bop_3874,uop_3878,call_3881,])
output2 = relay.Tuple([bop_3877,uop_3880,call_3882,])
func_3883 = relay.Function([var_3873,], output)
mod['func_3883'] = func_3883
mod = relay.transform.InferType()(mod)
mutated_mod['func_3883'] = func_3883
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3884 = relay.var("var_3884", dtype = "float64", shape = (11, 12, 15))#candidate|3884|(11, 12, 15)|var|float64
func_3883_call = mutated_mod.get_global_var('func_3883')
call_3885 = func_3883_call(var_3884)
output = call_3885
func_3886 = relay.Function([var_3884], output)
mutated_mod['func_3886'] = func_3886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3853_call = mod.get_global_var('func_3853')
func_3855_call = mutated_mod.get_global_var('func_3855')
call_3901 = func_3853_call()
call_3902 = func_3853_call()
output = call_3901
output2 = call_3902
func_3903 = relay.Function([], output)
mod['func_3903'] = func_3903
mod = relay.transform.InferType()(mod)
output = func_3903()
func_3904 = relay.Function([], output)
mutated_mod['func_3904'] = func_3904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_3957 = relay.TupleGetItem(func_3714_call(), 0)
call_3958 = relay.TupleGetItem(func_3716_call(), 0)
output = relay.Tuple([call_3957,])
output2 = relay.Tuple([call_3958,])
func_3959 = relay.Function([], output)
mod['func_3959'] = func_3959
mod = relay.transform.InferType()(mod)
mutated_mod['func_3959'] = func_3959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3959_call = mutated_mod.get_global_var('func_3959')
call_3960 = func_3959_call()
output = call_3960
func_3961 = relay.Function([], output)
mutated_mod['func_3961'] = func_3961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3853_call = mod.get_global_var('func_3853')
func_3855_call = mutated_mod.get_global_var('func_3855')
call_3982 = func_3853_call()
call_3983 = func_3853_call()
var_3986 = relay.var("var_3986", dtype = "float64", shape = (11, 12, 15))#candidate|3986|(11, 12, 15)|var|float64
bop_3987 = relay.subtract(call_3982.astype('int32'), relay.reshape(var_3986.astype('int32'), relay.shape_of(call_3982))) # shape=(11, 12, 15)
bop_3990 = relay.subtract(call_3983.astype('int32'), relay.reshape(var_3986.astype('int32'), relay.shape_of(call_3983))) # shape=(11, 12, 15)
output = relay.Tuple([bop_3987,])
output2 = relay.Tuple([bop_3990,])
func_3993 = relay.Function([var_3986,], output)
mod['func_3993'] = func_3993
mod = relay.transform.InferType()(mod)
mutated_mod['func_3993'] = func_3993
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3994 = relay.var("var_3994", dtype = "float64", shape = (11, 12, 15))#candidate|3994|(11, 12, 15)|var|float64
func_3993_call = mutated_mod.get_global_var('func_3993')
call_3995 = func_3993_call(var_3994)
output = call_3995
func_3996 = relay.Function([var_3994], output)
mutated_mod['func_3996'] = func_3996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_4017 = relay.TupleGetItem(func_3714_call(), 0)
call_4018 = relay.TupleGetItem(func_3716_call(), 0)
uop_4019 = relay.log10(call_4017.astype('float32')) # shape=(11, 12, 15)
uop_4021 = relay.log10(call_4018.astype('float32')) # shape=(11, 12, 15)
output = uop_4019
output2 = uop_4021
func_4027 = relay.Function([], output)
mod['func_4027'] = func_4027
mod = relay.transform.InferType()(mod)
output = func_4027()
func_4028 = relay.Function([], output)
mutated_mod['func_4028'] = func_4028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3959_call = mod.get_global_var('func_3959')
func_3961_call = mutated_mod.get_global_var('func_3961')
call_4043 = relay.TupleGetItem(func_3959_call(), 0)
call_4044 = relay.TupleGetItem(func_3961_call(), 0)
output = call_4043
output2 = call_4044
func_4070 = relay.Function([], output)
mod['func_4070'] = func_4070
mod = relay.transform.InferType()(mod)
output = func_4070()
func_4071 = relay.Function([], output)
mutated_mod['func_4071'] = func_4071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4087 = relay.var("var_4087", dtype = "uint8", shape = (10, 14, 15))#candidate|4087|(10, 14, 15)|var|uint8
const_4088 = relay.const([[[-10,-3,10,9,-1,-7,-10,-1,-8,1,-7,2,2,2,9],[-10,-7,-5,6,-4,-7,-8,-1,5,-3,5,9,-9,-5,-7],[-5,1,-3,10,2,-6,4,6,-6,-3,9,-1,7,-1,3],[5,6,9,-6,-7,-2,7,-1,-1,8,-6,-4,-5,-8,-1],[4,-10,-6,8,-9,-10,1,7,2,9,-4,7,3,-8,8],[-4,7,-5,-3,3,-9,3,10,-2,-9,-4,-7,10,-1,-10],[8,-3,8,-8,-10,-10,-5,9,-4,10,3,6,-3,9,-7],[-4,3,-1,-3,9,-3,-2,-2,4,3,9,5,5,4,-5],[3,9,7,4,-1,3,1,-2,8,1,7,-9,-7,-4,8],[-3,7,4,4,-5,-2,8,-6,6,-6,7,-9,8,3,-7],[1,2,4,3,-8,2,7,-1,10,-10,6,-10,6,-1,1],[-1,-9,-2,3,-10,4,-8,2,7,-1,-10,4,4,-9,-10],[2,-5,-6,-4,10,7,6,6,-7,1,10,6,3,-6,4],[7,9,9,-6,-4,8,2,-1,3,-3,-7,-10,-9,-3,-7]],[[2,3,5,9,-4,10,6,-8,-4,4,-9,-10,-4,-2,-3],[3,5,9,7,-3,-10,-5,-7,-5,5,-10,-10,3,-1,-2],[6,-2,-3,-10,8,3,8,-8,2,8,3,-2,-10,9,-10],[6,6,6,8,10,-9,5,3,-4,5,4,2,2,-1,-3],[-2,6,6,7,-7,-9,-10,-6,8,-9,2,2,9,5,-5],[-10,9,4,7,-9,-8,3,-5,-2,8,7,-3,5,-4,-2],[1,7,8,-5,-3,-9,5,9,-10,-4,-2,-2,3,-7,-2],[-8,-10,2,8,-3,4,-4,-6,10,3,6,-6,-2,-6,7],[-7,10,2,7,1,-5,-4,5,-1,5,8,1,10,4,2],[5,-8,1,10,2,-10,8,5,5,8,-3,-3,-2,-10,10],[-10,5,1,8,6,5,-8,-3,6,-10,-9,-5,-1,-5,5],[-5,2,3,-8,7,10,1,4,-10,1,7,6,2,10,8],[-5,-2,-5,-2,-5,-8,-8,-2,2,-5,3,2,-5,-5,-6],[-4,-8,-9,1,-7,-10,-1,3,-3,5,-7,-1,6,-5,-4]],[[-5,-3,-5,5,4,2,6,-4,-5,3,6,-8,9,4,-4],[7,7,4,2,7,3,2,3,10,5,-9,1,10,1,4],[-4,-7,-10,-10,10,8,7,5,-8,-7,6,5,-1,-9,-1],[-8,-3,6,5,6,3,9,6,7,8,-8,-8,-4,-10,-1],[-6,-7,-5,-2,1,6,-2,2,-10,3,-5,-4,3,-3,-1],[-7,-5,-5,9,1,-5,-4,3,-4,-6,-10,-7,-3,-2,-7],[-1,9,-1,6,-2,-10,3,4,1,-8,-7,8,-3,-6,7],[8,-6,-6,9,-8,9,8,3,10,1,1,-8,-2,1,-6],[1,-8,10,5,6,-10,1,-8,1,-8,-8,2,7,-9,-4],[-9,-8,4,-1,-9,2,1,-9,-8,7,-5,-5,10,-1,-10],[-1,-9,-6,-9,2,3,7,-9,-2,-9,5,1,8,-1,10],[5,-2,2,-7,-6,-1,5,4,-8,-3,5,-10,-7,8,9],[-3,9,9,5,6,-7,10,-9,-7,9,4,9,10,2,8],[-8,-6,-4,2,-10,-1,-7,10,5,3,-1,-10,8,-10,10]],[[2,7,-6,-4,2,-7,1,-4,-2,-2,3,-9,-6,2,9],[-2,-1,10,1,6,-8,-6,8,3,1,4,-9,-6,2,-10],[2,-4,4,10,10,1,-10,-8,-1,8,-6,-5,-5,-3,10],[8,9,7,-7,-1,5,-6,10,-3,7,-10,-2,-2,-5,4],[8,9,5,1,5,1,-3,-2,1,4,7,-2,1,5,-7],[-3,-8,-2,-8,-5,4,-2,-2,-2,10,-2,-9,5,8,-8],[-7,-2,3,10,-9,-6,-2,2,3,-9,-9,9,3,10,1],[6,6,5,-2,-3,-9,-5,-7,4,-10,-2,-4,-1,-4,10],[-8,3,4,5,2,-10,7,5,2,-4,4,5,5,-5,-6],[4,3,8,-7,7,3,4,1,-3,-9,-9,-3,9,10,-6],[-10,10,8,-3,3,6,-5,5,8,-3,7,9,6,-7,-3],[3,-1,-9,1,6,1,-7,2,4,-3,8,7,-9,5,-1],[7,6,-7,1,-6,-1,10,-5,1,4,-4,-4,-10,-6,-7],[7,-3,3,7,-7,10,-2,-5,3,-4,-1,-1,-3,-8,-8]],[[-8,-10,-8,-8,-7,-8,2,-9,6,-4,-3,1,10,5,-3],[-4,7,-1,-6,-10,5,-4,-7,-5,-7,5,3,-3,2,-2],[10,7,9,4,8,-2,1,9,9,1,2,-5,4,8,6],[2,-6,-3,6,2,-1,-6,-8,-10,-10,2,-9,-6,5,-10],[4,6,10,4,-7,1,-9,-10,-1,-4,1,2,5,2,2],[2,3,-5,-7,10,-5,4,7,3,-2,10,4,-1,8,10],[7,-5,10,-7,10,3,-10,1,8,-7,10,-4,-9,-3,10],[6,-7,-2,-2,-4,-8,-10,-1,-6,-3,-9,-10,9,-10,6],[-8,-9,-5,2,10,2,10,-6,2,-1,-5,-10,-5,-6,-3],[-5,5,6,5,-1,-1,-4,-6,-3,2,-3,-4,4,4,-4],[-2,-8,3,1,3,4,5,-6,-6,-9,-2,-7,-7,-8,3],[-10,1,2,-3,9,-4,-9,-10,-10,-5,-7,3,-5,-7,3],[-7,2,10,-9,8,-8,-2,1,-3,10,-4,-5,1,9,-5],[5,-5,9,5,-8,-9,-5,-5,-2,-9,-6,-9,2,-3,5]],[[1,-1,1,2,1,8,8,8,10,-4,4,4,3,1,-4],[5,10,-4,9,4,-7,7,-6,3,-8,-4,6,-4,-3,6],[-3,7,-8,-2,-6,-6,-1,-10,-9,2,9,8,6,-6,-8],[10,-5,3,-5,-2,-5,6,1,-2,1,10,4,7,1,-10],[-8,-8,-7,-8,-10,-7,-1,1,-1,4,9,-1,-1,2,2],[1,-6,2,-2,8,-3,6,-10,-7,2,-2,-7,-3,-1,-2],[-10,-2,-4,10,9,7,-4,7,2,6,7,-4,-1,3,-3],[-7,-8,9,-7,7,10,-7,8,10,-8,-1,-2,-9,1,9],[9,-9,6,10,-9,-9,-2,3,8,10,-8,3,8,-7,6],[-5,3,-3,-1,4,9,-9,10,10,7,-6,-5,-7,2,3],[3,2,-1,-6,-5,4,-4,4,-7,3,-6,-9,9,3,-3],[7,4,1,-4,10,7,-5,9,6,4,9,10,1,5,9],[10,-3,9,10,9,5,5,9,-1,-9,-6,-7,8,6,-1],[1,-4,6,8,-7,9,5,3,-8,-10,-1,5,5,-5,-7]],[[7,-10,4,-4,-3,9,4,3,-7,4,-8,-8,-5,6,-3],[6,3,-2,-1,9,-7,5,-2,1,-1,-9,-1,2,9,6],[1,3,-10,-10,1,-7,8,2,-10,1,9,10,6,-6,10],[-8,-5,-6,6,-6,-7,-7,-2,-5,3,6,6,4,8,9],[-1,10,8,1,-1,-10,7,-3,8,3,-6,3,-5,-5,6],[-2,3,-3,5,6,8,-6,7,5,-9,-5,9,6,5,-8],[9,6,-9,4,2,2,10,-6,-9,-10,-9,-3,5,2,-3],[8,10,4,4,5,-10,7,-5,8,-2,-10,5,9,3,7],[4,7,-1,5,-1,-3,-5,2,1,-4,8,6,-9,1,-8],[9,-6,-8,-9,4,1,-10,10,-8,2,6,8,-3,-8,-3],[5,-2,10,9,5,9,5,-4,-1,-5,-6,5,4,-3,4],[-1,-9,3,-3,9,8,-3,7,-7,2,3,3,-2,-8,9],[2,-5,3,10,-2,5,9,2,-5,-8,1,5,-1,-10,3],[-3,9,5,5,9,8,-7,2,-5,-10,-6,-4,4,-9,4]],[[-4,-6,-4,9,8,-7,2,3,3,4,3,-4,-2,-4,-3],[-2,7,3,1,-3,10,7,-1,-7,-10,-8,3,-10,10,-6],[6,9,-8,-5,4,9,-7,5,7,-4,5,10,4,4,5],[7,10,5,10,-6,-9,6,1,3,5,5,-9,-1,6,-7],[5,-2,-1,2,8,-4,5,2,3,-4,-1,10,5,-3,5],[1,5,7,-2,-5,-9,9,1,1,-7,2,-5,7,4,-10],[1,10,-5,-10,-8,-1,-6,-10,-2,-10,-8,-6,-5,-3,-5],[9,-2,-2,10,8,-10,4,9,-4,-6,9,-7,7,10,-2],[-10,-10,3,-3,-5,8,10,-1,7,10,-10,-5,4,10,1],[8,4,-4,-2,-8,10,4,10,-8,1,-8,7,-9,-7,-2],[10,10,9,-10,2,10,6,1,9,2,-7,2,-8,-2,9],[-3,-5,-2,-8,-7,-10,4,9,3,5,8,6,6,9,8],[6,-7,-8,-7,-1,9,-1,9,-10,-8,8,7,-5,9,-2],[4,-10,-9,9,-7,2,4,-10,-3,-5,-5,6,8,-6,-7]],[[-4,6,-1,-4,-3,-3,-6,-6,9,-7,10,-9,4,8,-2],[6,-6,-2,9,9,5,-7,-10,7,4,-6,-4,1,-2,-5],[5,-2,8,-10,-10,-9,3,-5,-2,-4,6,1,7,-7,-4],[-5,8,10,3,-10,-10,-7,-6,-6,5,-5,10,-1,1,-5],[-10,1,-2,-1,2,-8,-2,-5,-7,9,9,-3,1,5,9],[4,-4,7,-8,1,-4,2,3,-6,-8,-2,-8,-7,8,10],[4,9,1,-4,-6,8,-3,6,8,10,-7,-3,9,4,2],[5,10,-3,-7,9,-1,5,-9,-2,5,3,6,8,7,-1],[8,6,7,6,-6,1,-1,-1,-9,7,7,-7,7,-6,-7],[-3,2,-10,9,-5,10,10,2,2,-6,-5,-9,4,8,-10],[9,-10,3,10,-6,4,-8,-9,-6,4,-2,-5,-3,-6,-8],[-6,10,-8,7,-4,2,1,2,2,3,-10,-5,7,-3,-9],[-1,-10,2,-5,-7,-2,-7,-8,-4,-7,-8,-3,3,1,5],[8,6,7,7,4,1,2,-10,-6,-5,-3,-3,6,-6,-3]],[[6,7,1,-7,-7,4,-9,-5,1,3,-8,8,3,-7,-2],[4,-2,-9,6,-3,9,1,6,-8,1,6,10,-9,10,5],[-6,8,-7,-1,5,6,-1,-5,-6,7,-6,5,7,-8,1],[6,10,5,5,2,10,-5,6,-2,-2,-10,-2,-4,-10,-5],[-4,8,9,3,1,-5,3,4,1,-2,4,3,6,6,-8],[8,-6,-9,-4,-10,-8,-4,4,-2,3,-7,-5,-5,-8,10],[-4,9,7,-6,10,3,-10,9,-6,-8,-5,8,-5,-3,-5],[-8,-1,8,5,-8,9,-3,2,-2,2,-9,-5,9,1,-3],[-6,5,10,-7,9,-1,1,-9,7,1,-9,8,-9,-4,-10],[-9,9,-4,-9,-5,-10,-9,2,4,-7,-1,-7,-2,6,9],[4,2,1,-4,9,-9,6,10,3,-9,10,9,-7,-6,-1],[-8,-2,-10,-6,-3,6,4,9,-1,-9,-5,8,-6,8,-9],[6,4,8,1,10,9,-8,-7,-8,-1,9,-3,1,4,-1],[8,8,5,6,10,-4,10,-3,-8,5,7,5,-1,-1,-8]]], dtype = "uint8")#candidate|4088|(10, 14, 15)|const|uint8
bop_4089 = relay.equal(var_4087.astype('bool'), relay.reshape(const_4088.astype('bool'), relay.shape_of(var_4087))) # shape=(10, 14, 15)
output = bop_4089
output2 = bop_4089
func_4093 = relay.Function([var_4087,], output)
mod['func_4093'] = func_4093
mod = relay.transform.InferType()(mod)
mutated_mod['func_4093'] = func_4093
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4094 = relay.var("var_4094", dtype = "uint8", shape = (10, 14, 15))#candidate|4094|(10, 14, 15)|var|uint8
func_4093_call = mutated_mod.get_global_var('func_4093')
call_4095 = func_4093_call(var_4094)
output = call_4095
func_4096 = relay.Function([var_4094], output)
mutated_mod['func_4096'] = func_4096
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4098 = relay.var("var_4098", dtype = "int16", shape = (11, 14, 10))#candidate|4098|(11, 14, 10)|var|int16
var_4099 = relay.var("var_4099", dtype = "int16", shape = (11, 14, 10))#candidate|4099|(11, 14, 10)|var|int16
bop_4100 = relay.not_equal(var_4098.astype('bool'), relay.reshape(var_4099.astype('bool'), relay.shape_of(var_4098))) # shape=(11, 14, 10)
output = relay.Tuple([bop_4100,])
output2 = relay.Tuple([bop_4100,])
func_4105 = relay.Function([var_4098,var_4099,], output)
mod['func_4105'] = func_4105
mod = relay.transform.InferType()(mod)
var_4106 = relay.var("var_4106", dtype = "int16", shape = (11, 14, 10))#candidate|4106|(11, 14, 10)|var|int16
var_4107 = relay.var("var_4107", dtype = "int16", shape = (11, 14, 10))#candidate|4107|(11, 14, 10)|var|int16
output = func_4105(var_4106,var_4107,)
func_4108 = relay.Function([var_4106,var_4107,], output)
mutated_mod['func_4108'] = func_4108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4027_call = mod.get_global_var('func_4027')
func_4028_call = mutated_mod.get_global_var('func_4028')
call_4110 = func_4027_call()
call_4111 = func_4027_call()
func_3674_call = mod.get_global_var('func_3674')
func_3678_call = mutated_mod.get_global_var('func_3678')
const_4117 = relay.const([-2.192100,-6.019894,-6.751087,0.899859,-0.971242,5.875580,-0.232075,-8.203119,-3.154980,-3.156978,5.579476,3.296701,7.389035,7.072158,-1.488889,-3.616599,-7.387771,6.208191,9.158476,3.028840,7.100295,7.742331,-6.459512,3.838767,6.214726,1.907249,8.673130,-6.869694,-0.252230,4.026636,2.823494,4.495018,9.140649,-9.080355,3.130244,-2.824603], dtype = "float32")#candidate|4117|(36,)|const|float32
var_4118 = relay.var("var_4118", dtype = "float64", shape = (12, 4))#candidate|4118|(12, 4)|var|float64
call_4116 = relay.TupleGetItem(func_3674_call(relay.reshape(const_4117.astype('float32'), [1, 6, 6]), relay.reshape(var_4118.astype('float64'), [48,]), ), 8)
call_4119 = relay.TupleGetItem(func_3678_call(relay.reshape(const_4117.astype('float32'), [1, 6, 6]), relay.reshape(var_4118.astype('float64'), [48,]), ), 8)
func_3903_call = mod.get_global_var('func_3903')
func_3904_call = mutated_mod.get_global_var('func_3904')
call_4127 = func_3903_call()
call_4128 = func_3903_call()
output = relay.Tuple([call_4110,call_4116,const_4117,var_4118,call_4127,])
output2 = relay.Tuple([call_4111,call_4119,const_4117,var_4118,call_4128,])
func_4136 = relay.Function([var_4118,], output)
mod['func_4136'] = func_4136
mod = relay.transform.InferType()(mod)
mutated_mod['func_4136'] = func_4136
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4137 = relay.var("var_4137", dtype = "float64", shape = (12, 4))#candidate|4137|(12, 4)|var|float64
func_4136_call = mutated_mod.get_global_var('func_4136')
call_4138 = func_4136_call(var_4137)
output = call_4138
func_4139 = relay.Function([var_4137], output)
mutated_mod['func_4139'] = func_4139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_4141 = relay.TupleGetItem(func_3714_call(), 0)
call_4142 = relay.TupleGetItem(func_3716_call(), 0)
output = call_4141
output2 = call_4142
func_4149 = relay.Function([], output)
mod['func_4149'] = func_4149
mod = relay.transform.InferType()(mod)
mutated_mod['func_4149'] = func_4149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mutated_mod.get_global_var('func_4149')
call_4150 = func_4149_call()
output = call_4150
func_4151 = relay.Function([], output)
mutated_mod['func_4151'] = func_4151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_4180 = func_3765_call()
call_4181 = func_3765_call()
var_4182 = relay.var("var_4182", dtype = "float64", shape = (11, 12, 15))#candidate|4182|(11, 12, 15)|var|float64
bop_4183 = relay.bitwise_or(call_4180.astype('int16'), relay.reshape(var_4182.astype('int16'), relay.shape_of(call_4180))) # shape=(11, 12, 15)
bop_4186 = relay.bitwise_or(call_4181.astype('int16'), relay.reshape(var_4182.astype('int16'), relay.shape_of(call_4181))) # shape=(11, 12, 15)
var_4188 = relay.var("var_4188", dtype = "float64", shape = (11, 12, 15))#candidate|4188|(11, 12, 15)|var|float64
bop_4189 = relay.multiply(call_4180.astype('uint32'), relay.reshape(var_4188.astype('uint32'), relay.shape_of(call_4180))) # shape=(11, 12, 15)
bop_4192 = relay.multiply(call_4181.astype('uint32'), relay.reshape(var_4188.astype('uint32'), relay.shape_of(call_4181))) # shape=(11, 12, 15)
func_4105_call = mod.get_global_var('func_4105')
func_4108_call = mutated_mod.get_global_var('func_4108')
var_4213 = relay.var("var_4213", dtype = "int16", shape = (1540,))#candidate|4213|(1540,)|var|int16
call_4212 = relay.TupleGetItem(func_4105_call(relay.reshape(var_4213.astype('int16'), [11, 14, 10]), relay.reshape(var_4213.astype('int16'), [11, 14, 10]), ), 0)
call_4214 = relay.TupleGetItem(func_4108_call(relay.reshape(var_4213.astype('int16'), [11, 14, 10]), relay.reshape(var_4213.astype('int16'), [11, 14, 10]), ), 0)
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_4257 = func_4070_call()
call_4258 = func_4070_call()
output = relay.Tuple([bop_4183,bop_4189,call_4212,var_4213,call_4257,])
output2 = relay.Tuple([bop_4186,bop_4192,call_4214,var_4213,call_4258,])
func_4273 = relay.Function([var_4182,var_4188,var_4213,], output)
mod['func_4273'] = func_4273
mod = relay.transform.InferType()(mod)
mutated_mod['func_4273'] = func_4273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4273_call = mutated_mod.get_global_var('func_4273')
var_4275 = relay.var("var_4275", dtype = "float64", shape = (11, 12, 15))#candidate|4275|(11, 12, 15)|var|float64
var_4276 = relay.var("var_4276", dtype = "float64", shape = (11, 12, 15))#candidate|4276|(11, 12, 15)|var|float64
var_4277 = relay.var("var_4277", dtype = "int16", shape = (1540,))#candidate|4277|(1540,)|var|int16
call_4274 = func_4273_call(var_4275,var_4276,var_4277,)
output = call_4274
func_4278 = relay.Function([var_4275,var_4276,var_4277,], output)
mutated_mod['func_4278'] = func_4278
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4286 = relay.const([[[8.563657,-8.086761,2.114416,-5.521837,4.761459,9.668978,5.766808,8.179062,-9.731050,8.722209,6.848364],[1.895425,-4.815714,-3.685470,0.316800,5.022132,-3.362039,-3.040667,6.665767,8.983680,-0.341846,1.382569],[-1.322469,-2.891204,2.923128,4.900274,6.788566,-8.597276,-3.589137,-5.156677,-8.553723,-2.370000,0.444995],[-5.578613,5.256938,4.798468,-4.864305,5.900542,-5.002364,1.539528,2.694821,-6.383773,-7.897089,-1.264587],[-4.443261,-8.333901,4.355045,0.670965,-2.579280,9.677769,8.569565,0.051147,-9.761388,6.837223,-6.890358],[-9.359275,3.418871,-7.095271,-2.707285,8.327986,2.367740,6.463613,-4.463787,-6.371892,2.041675,3.261406],[-3.345402,-9.443590,5.459556,9.546114,1.915726,-5.777614,3.784166,-5.329573,2.079167,-8.879776,2.204605],[7.068986,-6.863071,-8.482840,-7.291010,9.932903,-0.656012,9.637749,6.314890,6.663982,-6.159070,7.547349],[9.074673,2.384809,1.004280,5.463634,-8.116041,7.064524,-9.107420,-5.292221,2.554469,-1.359568,6.361019],[6.607138,-0.881323,6.178903,-4.726248,-3.798249,-7.695244,4.240327,7.542104,0.952511,5.114750,6.321886],[-1.038145,-8.875533,9.247196,-5.264141,-0.557624,4.775890,-6.558137,-8.839346,8.735963,-8.803939,-8.878028],[-5.565314,2.515358,2.706685,-2.510509,-3.108741,-9.677835,-5.605003,4.847873,4.452739,-4.799844,7.837654],[0.515395,-2.093123,-6.917202,0.238838,-5.271881,7.471371,3.382222,-2.833847,3.919203,-7.642660,-3.090468],[8.063687,9.226676,2.513278,2.594496,1.382546,-1.879449,9.920514,-5.797555,-4.024715,-1.538783,-4.798656],[-6.583304,8.669497,-7.971209,-8.030075,-3.641047,-4.600918,-4.753325,-8.437836,-9.118800,-0.850864,8.512629],[-6.661194,-6.457936,-7.752319,-4.833199,-9.132492,6.392260,-2.831766,-1.718615,-6.862425,-4.300868,-5.083666]],[[9.625051,-0.055175,-4.659713,-8.688466,-7.111217,-3.488351,8.094446,-2.089566,4.115957,8.392582,-9.299515],[-3.605689,-1.956708,-3.924362,-7.910806,6.548168,0.589548,2.952754,-9.391291,8.736064,-3.517179,-3.050165],[-6.026796,1.619334,1.689824,-1.194020,-3.786774,-2.411830,-9.068701,8.111965,-2.245070,-7.576733,-4.650840],[3.691641,7.538744,-2.462173,-2.404596,-4.765070,4.732865,9.037582,-9.895906,-9.065124,-8.418984,1.650421],[2.760143,0.433312,6.063132,4.624892,-6.893222,-3.868451,7.176009,9.798566,5.930965,-0.866983,-2.960581],[-7.589622,-5.891144,2.717186,0.915480,7.320885,-0.499119,-1.180850,-9.525680,6.712470,2.242035,-2.522137],[-2.293877,-9.433301,3.914257,-5.490553,-0.112919,-4.736970,-3.916201,-2.404856,-4.136207,-3.864126,-3.514260],[-1.734693,5.421955,9.678722,-5.259355,0.659426,-2.738051,-2.308994,6.275511,0.308818,9.328979,-5.303455],[1.079429,-5.666840,-6.020324,-3.871783,1.124601,8.758930,9.220737,8.343930,-9.995664,-5.754249,8.079429],[9.711466,-2.822081,-4.235942,-2.144815,6.482969,2.009702,-9.815278,-4.364013,4.507245,0.272549,-6.150456],[0.988130,-2.225472,8.324670,-5.191935,-0.678859,1.242938,-5.244754,-4.920909,-8.627892,9.828989,7.520351],[8.841395,-0.509161,-4.588501,2.273410,-9.436200,-4.277505,-0.578482,-8.624102,-6.508587,-8.011136,7.604621],[-3.650706,-3.296330,7.798263,-1.055083,6.475788,-3.440170,-4.427342,6.336076,-5.287550,2.103687,6.615011],[-0.450286,-3.174809,-0.075587,-4.578114,-0.161128,2.199689,3.760317,-4.728511,-1.260999,4.659643,4.252196],[3.968457,1.200941,9.870654,-2.934144,-0.261310,-3.342183,-5.644993,-4.752948,-2.885045,7.149892,3.599575],[-0.747795,-4.458150,7.996245,9.279542,-1.884838,4.329902,-2.084115,-9.080763,7.209260,2.793902,3.805273]],[[-5.985550,-2.772449,-2.555858,9.123390,-1.254235,1.548171,-8.302871,-4.277000,-9.451779,-1.919311,-2.967214],[-2.731135,5.882906,-2.275015,1.653347,-9.486853,5.850382,-4.910842,-4.844555,2.719197,5.683606,-6.547293],[7.879014,3.728822,8.719247,4.398936,6.510134,-6.758814,-0.721997,9.514109,-1.809960,7.504176,3.910235],[-2.048908,5.850630,-3.589419,-4.462970,-5.206766,-0.705508,0.098186,8.210137,8.216805,-4.028021,-4.489587],[-6.665228,-0.472086,7.382272,-2.588152,3.369592,5.930498,-1.406209,9.508221,-1.653727,-7.367752,-1.268237],[-4.251576,5.753823,-2.340802,8.074101,-6.252149,-0.987206,-6.253806,-8.959554,-0.617481,5.929859,9.666391],[-4.791222,5.953163,-3.896238,2.688240,3.631583,5.900403,7.187692,6.710059,-5.232769,2.900611,-1.878072],[-2.515798,-9.773993,6.779498,-6.392082,-7.435900,9.198096,4.806812,1.287326,-1.753609,-6.619806,2.990998],[5.944149,-1.710404,-8.157977,6.170166,-4.441416,-7.272479,-0.471231,-5.037413,-4.888971,0.848964,-4.300732],[2.839093,1.476780,9.882874,5.667424,-4.199487,4.954650,-3.671995,-0.390510,-8.957741,-7.670342,8.480471],[-0.506034,5.152363,-4.017587,7.134316,-5.848766,4.911467,-2.979052,6.342898,7.605929,2.889210,3.285961],[5.818464,9.403422,-6.211345,-9.417737,-6.544770,1.275295,1.490004,0.910935,2.399159,2.512650,3.189530],[6.132642,-3.473660,-6.118338,8.868098,7.451559,2.905139,-4.410843,-5.846919,-6.557378,-1.944699,6.737395],[3.023180,-1.565370,-1.179562,1.189016,6.377139,-4.932186,-8.092996,8.671679,-0.735043,-0.200607,5.701299],[1.409452,5.682524,1.311720,-2.151634,7.906032,7.809082,-7.488758,5.898686,7.558288,-1.731205,-5.659115],[7.386517,-8.496426,9.411131,6.026398,0.539537,-0.455358,-1.446220,-7.395782,-5.307954,4.412679,4.001523]],[[4.883483,4.814048,-6.121615,6.708947,-6.804811,-2.536985,-6.456037,7.657079,8.966679,7.327871,1.855936],[0.844925,-2.936532,6.124818,7.702258,2.481209,-3.479623,9.832426,-8.355253,5.632118,3.264860,6.195558],[5.840212,-6.614406,8.426634,2.302928,2.864639,6.464949,-3.519851,4.203176,1.194882,1.994170,-1.802238],[-5.690472,6.611901,2.342202,-5.973161,-6.647388,-2.616201,-8.193030,-0.147916,-9.937057,-6.990438,1.160139],[6.056661,-6.127973,4.658699,-0.330675,-4.477282,-1.310083,-2.363172,3.810577,-1.025290,1.816378,-2.527058],[2.025200,9.771292,-2.212841,2.614982,-0.981670,9.363336,0.822927,-3.901864,-7.233973,2.107300,-2.889129],[-4.826847,-5.459705,-5.856875,2.922879,2.677056,9.132658,1.493444,-9.849157,-7.870030,6.612355,0.257757],[-6.566881,-3.033268,-7.434262,-6.264346,8.931431,-7.632167,8.846691,5.850850,0.679717,3.263290,4.093250],[5.189280,6.216710,3.101308,2.845649,-8.303931,-6.667090,-8.688374,-4.459029,-5.713628,1.492666,1.730993],[5.971376,-4.607870,8.876376,7.008504,-9.491268,-0.375570,-4.417413,-2.440083,-8.565890,-7.101219,5.409132],[6.860848,4.806387,5.257155,4.495660,2.232630,-0.623854,8.929423,-9.853508,-9.563642,8.936694,-4.102178],[-8.454320,3.784128,4.935256,-4.207144,-1.422228,-2.610024,0.373691,8.856517,-3.702945,5.202729,-7.946149],[-3.480299,6.125056,4.423582,5.721683,6.460714,-3.664922,-7.768881,-3.977740,-7.588333,3.540534,-4.727781],[-4.578819,6.645706,-5.253701,0.153551,9.439898,3.428050,6.691309,-2.547382,6.395587,-5.542793,-6.560796],[1.034654,3.669850,-6.654884,9.672726,9.960117,-2.848340,-0.748246,7.267183,3.338878,-9.724512,-9.305668],[4.994873,-1.979527,-3.537813,-8.928785,-1.732288,4.206208,7.246490,-3.626131,-4.579970,-7.702002,-6.820472]],[[0.872063,9.729536,-4.349769,-2.404592,3.364543,2.876963,-7.574561,-1.532606,0.536498,-7.998949,4.379411],[-5.345982,-4.758995,3.920447,3.810630,-0.472534,-5.002842,2.834888,8.986981,3.435890,9.758819,-2.733389],[-0.188027,-6.508261,1.973527,-7.033171,-5.352356,-0.378965,9.073128,4.034173,9.251078,7.343040,5.365903],[9.629295,-3.243685,2.161952,4.395882,1.344124,5.992830,4.156020,7.173346,4.167950,-5.971487,-2.908017],[7.458613,-3.046373,6.404102,-1.991446,-6.727142,4.332193,-3.378327,-4.927902,5.822851,3.500299,2.719446],[4.887521,-9.738767,-4.696280,5.641389,-5.038807,3.378906,2.091774,2.079385,0.361382,3.569757,-1.639404],[-5.388361,-5.595683,9.289754,-5.918817,-9.214922,5.952658,-1.097235,-3.880168,-2.185683,-4.313475,6.513491],[5.847638,-4.833059,4.425920,2.968083,4.792950,-4.521392,7.984704,-4.753940,4.238563,-4.913312,4.742512],[-7.439961,-3.448378,8.722026,-5.364438,-6.123818,6.851770,4.903822,7.750286,-9.340081,-5.778852,-2.871914],[-5.938820,3.365841,6.421160,-4.998268,-3.001214,-2.754322,-3.717407,4.877729,4.542586,-3.737717,-5.051970],[6.694964,-7.539573,5.290417,-0.771046,0.662789,-9.121242,-7.554303,-7.598406,-6.876369,-2.551032,2.155739],[-3.320034,1.585547,-4.388819,-9.537712,0.949683,-3.350288,-1.389472,-6.347220,2.720392,4.934632,-3.157277],[-4.224177,5.930301,9.966384,9.486932,-9.464021,-6.859252,0.696693,3.944945,0.679313,1.558741,-1.102204],[6.235804,6.546606,-7.869283,-5.772890,-0.890667,6.538656,-4.490137,4.301230,7.668373,3.701899,-1.725714],[2.961035,2.850819,-9.692833,-9.534816,-6.230358,-4.846142,6.855776,-4.478852,5.300661,-9.911408,-1.888846],[-2.815039,-7.684895,0.072774,2.747058,9.834146,6.495968,2.927909,6.826402,0.633884,-3.647372,5.893559]],[[-3.504465,0.460154,1.116456,7.735998,-6.030991,9.634843,1.825549,9.737550,-6.908802,5.750608,9.608964],[-8.861524,7.677887,-2.371208,6.568720,1.044289,3.747438,5.780027,-4.257580,2.570496,-0.609068,8.851985],[7.081518,-3.466601,1.665780,-8.343243,0.028130,-8.851852,-6.121689,-4.399450,-3.911753,1.596322,-4.797442],[-0.085724,6.100184,-6.545421,5.615110,-1.558617,-6.019799,-7.035591,-4.282494,-4.631496,3.287391,-4.309446],[2.688848,1.960054,-6.308349,1.035284,-0.714607,2.973902,1.547876,5.211929,-5.674906,-9.948790,4.128501],[-1.262698,6.052308,3.676304,9.786838,-7.066189,-6.894188,1.115692,-4.816983,7.715813,-1.181114,6.801045],[-4.781126,-7.325114,-8.739753,3.917765,-4.483524,2.951719,-1.794227,-2.429470,8.689774,-9.026044,0.889539],[-1.985436,0.040251,-0.814443,9.831899,9.635169,-4.729344,-8.387555,-1.044531,-4.539628,3.206956,-8.682228],[-4.701557,-3.902625,1.171228,8.569936,-8.411801,2.991369,-8.101515,6.621224,6.240308,1.420208,9.157361],[-9.642659,-3.045653,-5.721676,-7.542198,5.553036,5.640444,-0.316075,8.830365,8.745404,-4.479561,2.236513],[-6.475494,-9.376365,9.390023,-3.947770,2.120987,0.916798,8.878383,3.698954,-4.568622,9.000188,-5.045586],[7.453654,6.663556,6.095273,6.460913,-8.744573,-2.038107,3.369036,6.622970,-7.401633,-2.433198,-5.360845],[0.487643,7.164193,-3.817942,9.566663,6.500521,-2.907208,-3.147344,-2.244440,-2.349993,9.963705,9.998660],[8.588479,-7.116510,0.408371,5.141121,6.882374,1.131214,-3.316814,9.618709,2.905279,-2.587528,5.072571],[5.245741,-3.018003,3.729985,-2.675498,-3.131206,0.552113,1.149505,5.375179,-5.173370,3.640216,-4.945792],[8.116282,-2.378514,-4.438668,2.720418,5.802547,7.390183,-1.045334,9.862489,9.659002,-3.136310,6.194251]],[[8.235239,-2.898931,3.374091,7.012097,-6.627563,2.176144,4.103051,5.086781,3.988468,-9.910019,6.418994],[5.260636,8.980523,-8.051046,9.960408,-7.688726,9.891578,-1.188335,-8.941628,-6.870985,8.616811,7.910360],[4.233032,4.964175,2.784193,3.194990,-0.164756,-8.109177,2.445983,-0.630450,-8.730828,3.169169,2.416571],[-0.304495,3.028800,-6.261717,-5.505260,-9.720538,2.671831,-8.876580,0.003006,5.834711,8.909025,7.963056],[-9.708616,0.167813,-6.721745,-1.612365,5.959051,-8.138110,1.464960,3.431708,-9.213820,4.544372,1.677441],[5.926262,1.127526,-2.418607,-7.049963,2.812646,1.262639,0.203688,4.655625,-4.804202,-5.977488,-3.174323],[6.764070,2.698147,9.027698,8.033812,-7.538375,7.885266,1.949523,-6.768918,2.834383,8.514097,8.504736],[8.014191,-0.093762,4.639140,-0.192080,7.723322,9.715312,0.381046,4.478652,6.072645,4.089579,-7.646042],[-7.384861,-7.076360,-8.024861,1.061988,-7.003977,4.734614,-6.182428,8.685641,-8.356300,-3.277859,1.124553],[-8.723185,7.665062,7.575799,-5.257286,0.409616,-5.042459,-3.760512,9.258345,-8.223160,-9.112621,2.147337],[-6.338001,1.396327,8.859166,-7.487970,-2.612291,6.458164,-9.801002,-6.958685,-9.908827,-0.517733,-7.969664],[-0.694975,-6.095020,4.599781,-5.591656,3.332918,-7.925628,6.463552,-6.638369,-1.128427,-6.207787,-7.552768],[-1.018481,6.823618,4.928784,-9.345442,-0.198200,3.626189,2.247019,-8.197017,3.749117,4.709891,-2.865476],[5.329417,-3.556421,0.834253,-6.790211,-2.496249,2.299284,8.900675,6.133771,-4.883891,-2.298852,-4.781371],[-6.056978,0.377204,-9.498625,7.439661,2.770762,3.457952,0.232706,-3.997071,5.126572,-2.485836,-2.881839],[9.627036,4.720290,-5.985301,1.237464,-6.179149,8.882175,-4.581214,-6.065702,-2.822361,-3.142863,3.026691]],[[1.113525,3.057503,-9.832653,3.929754,-1.921271,-7.808337,-4.217975,1.837318,5.467889,0.154928,-4.365174],[-4.723048,-4.349379,-9.337460,3.456352,-4.751787,-8.019970,2.031102,0.479394,1.136250,0.344217,-5.512575],[-0.816664,8.928375,6.811324,-4.995638,-8.980948,-4.251977,-0.871155,-6.102345,-3.767170,-6.331268,-9.484051],[-7.056360,-9.573723,9.366523,3.933608,5.572577,-6.264339,-2.970546,1.247901,9.630431,2.218652,-1.369852],[-6.276534,3.217610,3.986309,1.481723,4.744155,-6.810993,-1.779366,5.155553,7.571588,2.534284,-2.123746],[1.774889,6.949165,7.383756,-6.804731,-7.818076,-2.178695,4.128963,0.045197,-1.762131,-2.606496,-2.826452],[-5.927829,6.500423,-7.391291,2.281648,-7.982779,-3.476852,4.688487,-9.879928,-9.882426,1.764533,0.152556],[-2.627736,4.467659,6.118998,7.530888,-7.718191,-8.644561,3.611357,3.994302,5.260574,7.544321,5.567584],[4.507402,-7.137033,-2.144752,3.614380,0.592025,-7.421622,-7.800036,-6.502894,7.373574,1.564436,-6.755060],[-0.680690,-8.311665,1.623913,2.733233,-3.290850,0.868766,-2.649585,-6.531086,8.294957,-6.299430,0.076288],[8.068608,-5.940974,-2.696249,-0.106855,0.163386,-7.238371,-7.103116,9.022490,-1.134903,8.116037,7.142545],[1.679956,4.058793,5.580792,-9.539730,-7.123954,-9.513027,-8.267620,-7.061057,-9.871002,7.605609,7.152726],[-0.117752,-0.543866,3.834800,-0.359139,6.214031,-5.687983,-8.371658,-7.649220,-3.841649,5.063515,-8.419732],[-4.476604,-5.258022,-0.112489,1.125392,-0.553593,-0.721211,9.345094,-0.775272,-2.044178,4.682899,-5.417643],[-0.611309,6.632226,2.257543,-9.401834,-0.396541,-6.128871,8.181362,4.983214,4.274915,-9.176773,-0.454065],[5.953970,-8.961551,-2.345666,-5.580472,2.939422,-2.245458,-0.010718,8.841665,4.597114,0.657430,9.813778]],[[-0.581194,4.270015,-2.515353,2.043584,3.514631,1.547135,8.382978,-3.169423,-5.600024,-0.660441,-1.565614],[-3.545111,4.490574,4.809024,9.453700,0.495230,1.674100,2.892821,5.973416,-9.110466,3.684208,-8.300980],[-4.114699,4.360241,-7.019858,9.732514,-8.895392,0.146712,3.145462,-3.573107,6.760433,-5.497050,-7.232805],[-7.443621,-2.513332,9.306661,-5.624077,-3.439043,-4.295897,2.956850,-8.755679,7.250886,-8.886285,-0.095563],[4.417063,-1.233744,4.918758,-4.778334,6.998256,8.563108,8.657733,6.816832,-9.760831,-1.496350,9.657923],[8.926078,-1.282692,-0.337791,2.873261,-2.822530,9.018220,1.373309,0.552330,0.360067,-0.057116,1.009178],[4.877039,0.280539,-2.334359,-2.360204,0.165611,6.280727,-7.718348,-7.729618,1.150592,-3.892976,-4.295754],[7.665562,2.441899,-1.146187,3.479793,-3.024472,-4.898116,-5.407135,7.552698,6.543912,-3.251726,8.318429],[-9.075748,5.902955,-8.951773,1.483483,2.302664,5.067306,1.964435,0.264591,7.187077,0.443879,6.017771],[-6.791189,-4.767478,-1.606614,7.151851,5.170392,8.983292,6.306858,-7.158149,-7.803387,6.533481,6.490935],[5.497350,5.650595,-8.252414,7.757395,-0.026761,-5.734660,8.743729,1.732054,-9.762301,-4.891029,6.317921],[-1.758629,-5.874780,-0.717264,-0.462645,-1.972648,-7.170008,-4.834939,-2.294012,-6.183851,3.163786,1.595427],[5.453562,3.789809,4.925931,-3.514752,5.924221,7.482227,4.384774,9.067464,6.852242,-1.073541,7.166555],[-9.865814,-5.746963,-7.012210,3.567230,-9.576926,3.675098,4.203988,2.905322,2.839378,-2.237473,1.772789],[-2.272801,6.848951,-3.736562,7.132339,-0.071749,-0.094030,4.251118,-5.900178,-2.059460,8.352159,8.865951],[7.288948,-0.014734,4.784090,9.311426,2.777403,-2.582310,0.748900,-0.617485,-2.165018,-3.195732,1.349861]],[[-8.432917,-7.089756,-9.635106,-8.773947,-1.218201,-4.705787,-7.652823,6.286578,-2.883363,-0.300798,3.817435],[-6.440587,-2.789710,-5.040022,1.942228,-1.976172,-8.717398,-0.358310,0.064090,-3.858961,-5.175604,-2.264726],[-8.000925,-4.630904,-5.258688,8.470212,-7.476637,3.849442,3.202631,6.104702,0.649895,-2.242523,8.905208],[-6.589679,8.050935,-6.075887,-1.009055,-3.793535,0.415583,2.664352,1.334978,7.495627,-6.458135,1.981051],[3.167431,-3.655957,-7.083268,-8.496522,-9.921037,-4.732451,4.382113,9.174357,-7.753722,-4.104988,1.110068],[7.703889,0.900845,-5.073675,-1.175072,7.422870,6.625003,-0.841917,-5.102576,8.699272,-0.001698,-2.083038],[-9.013566,1.547821,3.942097,-6.516651,8.354396,-1.365068,8.533253,0.416606,-7.751621,3.077214,-6.102164],[6.132638,-7.661295,5.340423,5.647447,-7.357121,-1.934986,-6.686058,2.932780,-9.182143,-7.511132,8.480603],[4.121676,6.440624,4.564893,1.736868,5.753918,-2.360176,0.538342,-3.325346,9.470801,3.524879,-6.583614],[-8.304789,-2.118234,-8.039951,0.764048,-3.692791,-3.462479,-6.033845,-8.654869,-0.821529,-0.483019,0.259558],[-2.577556,-6.601614,-4.379950,4.324816,6.516156,7.317325,-3.401871,6.334989,0.811693,8.587387,7.639320],[-6.865723,6.321667,4.418680,9.553859,-3.838666,-5.199056,-9.258251,-4.048728,9.552314,2.449663,0.391277],[0.828180,5.172736,7.196896,-8.712598,-4.482210,-0.465199,5.225142,7.546867,4.828990,4.309149,7.496981],[-6.647412,0.119301,9.966822,-0.600571,9.180676,4.100583,0.727993,2.608338,-2.192895,-2.711970,0.403124],[-2.722961,-3.363672,-8.642238,-1.417577,8.307263,7.767604,-5.593186,0.068960,-5.706990,-8.987448,6.824299],[-1.550285,-9.388435,-9.253526,7.278168,-8.260671,2.932527,5.382884,-8.209777,7.114731,3.168149,6.355615]],[[5.606570,-4.823975,9.213539,-5.911346,-0.230679,3.823070,3.637709,8.847053,7.279960,-0.088214,3.446820],[8.333105,2.421673,2.741965,2.082807,8.065146,-5.053532,-1.730332,-3.380418,-1.646744,3.369965,3.961358],[-6.841498,-2.282866,6.852058,-6.486397,-0.688173,-1.280158,-8.852507,-6.955786,-7.191579,-2.775225,-6.321448],[-8.566731,6.194064,8.040077,-4.944632,8.508032,-8.388703,4.298766,0.841189,-0.578586,3.199505,5.251948],[-1.013074,8.014166,3.331059,8.819229,3.895115,0.611066,6.950146,7.871514,6.329123,-8.634730,-0.888187],[9.645461,6.376299,-2.091485,1.788492,-1.520528,7.205240,-0.162267,1.720469,-7.666434,-7.326442,-3.166938],[4.929029,4.064935,-2.626676,-1.342805,4.816370,-8.412142,5.203671,2.404196,8.599389,-1.136465,-5.511484],[8.638687,8.726527,-2.781089,0.370744,0.363528,-7.795355,-9.145202,-2.600889,-5.500932,-4.591076,-0.848900],[4.517941,-4.063324,5.874878,5.379374,-7.003377,6.924522,7.156095,6.106415,-3.401279,3.886311,6.316024],[-8.174748,-0.357858,-8.310866,1.158780,-1.334806,-7.336674,0.376404,0.332298,1.699790,-7.447325,9.466650],[-2.879952,-0.057426,4.884718,-4.976363,0.662856,-2.043371,2.304833,6.362982,9.859474,2.277283,-9.106083],[0.926874,7.729652,4.749964,-2.109036,9.743414,4.098588,9.989389,5.455879,-8.107572,-7.700840,-1.241932],[8.605987,4.267649,2.441346,-0.790575,8.127342,-8.395498,8.951979,-2.031614,-8.756226,-5.451596,-6.237055],[1.389877,6.854091,-1.995712,-8.237015,8.779950,-6.642447,4.589197,6.142563,-5.119137,2.515779,-9.080775],[-6.859558,-3.477709,-2.486697,0.403855,2.899338,5.003386,-1.680124,-8.107145,-6.999685,-9.936740,-3.555186],[1.816233,1.317044,6.658121,-2.389096,4.376213,-6.333471,3.757637,7.248910,9.071934,3.541058,4.808864]],[[2.734952,0.615059,-4.237163,-5.512352,7.906018,-2.652997,1.161222,9.937020,8.796463,8.192103,8.937565],[2.210783,3.509119,9.055359,3.829851,-2.442488,-4.573966,-3.373972,0.342298,-4.953852,-2.667389,1.977528],[-2.153092,4.248000,-1.625428,6.168560,-7.297858,-4.528980,-9.342979,-3.839666,-9.376003,-4.075368,-0.171208],[2.397524,0.054098,-3.557105,6.013286,-6.091135,2.946547,0.511085,-0.883926,0.802764,1.012528,-5.273874],[1.366741,7.779201,3.528819,-5.129535,3.251809,2.710073,2.510652,-9.588037,6.169452,-8.534486,3.541321],[-0.487247,1.411202,-9.378914,9.423986,-1.990275,6.824884,7.931842,0.983051,5.253925,7.484769,6.867962],[-5.430399,2.833905,-9.257236,-8.078714,-8.591465,6.240738,-8.239642,-6.866569,-7.431224,-0.537163,7.922032],[-0.886786,-7.399018,5.977665,-5.939053,-3.682570,-0.188731,9.009118,-4.639071,-1.527522,-9.381922,-8.146613],[9.742878,0.200358,8.892471,-9.513430,0.594834,4.482013,-8.840620,2.366717,9.587390,1.329081,-7.980007],[9.777226,0.140165,5.882623,7.644286,-8.031763,-9.190934,6.666885,-5.437899,-5.816500,-1.488796,2.919411],[-5.730665,-1.087975,-2.503876,-3.749066,-8.616306,7.458141,4.788694,7.896711,-3.898472,-7.564566,2.763134],[-1.907029,9.157095,9.125208,-1.421511,-5.818159,-3.757877,1.807351,-1.246329,7.760131,1.105707,-1.789256],[6.461869,2.219064,-9.825987,-7.995117,0.245888,4.688372,-9.383026,3.148012,4.089841,8.655902,-1.881260],[-1.878135,-9.893454,1.322362,3.856113,4.812964,6.726238,-3.639191,-5.890848,-7.455977,-7.637693,-8.583080],[-0.624441,9.361872,4.743338,3.837613,9.790929,-3.325900,8.121503,2.150879,-0.368026,7.894326,-2.500945],[9.590641,4.029235,-2.198312,5.167943,-9.944460,-9.190665,1.443771,-3.571241,2.845092,-2.361727,-9.941256]]], dtype = "float32")#candidate|4286|(12, 16, 11)|const|float32
uop_4287 = relay.atan(const_4286.astype('float32')) # shape=(12, 16, 11)
func_432_call = mod.get_global_var('func_432')
func_436_call = mutated_mod.get_global_var('func_436')
const_4291 = relay.const([2,4,2,-9,-8,-7,2,10,-8,6,4,1,-10,-10,-10,-7,-1,-10,-5,-1,-9,-2,10,4,-5,-3,-6,-4,-5,3,-9,10,3,4,10,3,-8,4,-8,-5,-9,-1,3,5,-10,-3,-9,1,-2,-2,-4,4,1,-9,-6,-2,-3,4,-10,1,-7,9,7,8,6,-2,6,-2,3,5,-4,-6,4,10,-7,4,-5,-10,4,2,9,-10,-1,1,4,3,7,-4,7,4,6,10,10,6,7,4,5,10,-8,9,-8,-7,-2,-5,6,-5,-7,8,4,-1,-3,8,1,-3,8,9,4,1,1,-7,5,-3,-8,10,-4,-4,8,-4,-9,-7,9,-4,-6,-1,1,5,-1,-8,7,2,1,-10,-7,7,3,2,4,7,1,6,-5,9,9,-6,5,10,3,4,-6,5,-7,-3,4,-10,7,8,6,9,-7,4,10,-8,5,4,-3,1,9,10,4,-10,-5,-3,8,-8,7,-6,7,-2,6,-2,-7,10,8,7,9,3,8,4,-9,10,6,5,-10,6,2,-8,2,3,7,2,-9,-9,-4,-4,9,9,2,1,-10,1,-6,1,6,-9,-5,-8,-7,-5,1,-4,-3,-6,-6,8,-3,-9,5,-8,-5,-3,-8,-9,9,-8,1,-3,-4,1,7,7,8,10,8,-6,6,5,2,1,-6,-6,-8,3,-9,1,6,7,-5,-9,8,6,-5,-8,-5,-2,5,-7,-6,-6,-7,-2,-6,-4,9,-4,9,9,-2,-4,-3,7,-6,-2,5,9,6,4,2,2,3,6,-5,7,1,4,10,3,-6,-10,4,4,1,-9,5,-4,-9,-2,5,-4,3,-2,7,-8,-2,-5,-8,-6,4,3,9,10,10,-2,1,3,4,-6,-1,-6,-7,-1,8,5,3,3,-7,-9,5,4,-9,-10,2,-4,4,-10,-8,7,8,-10,-2,-4,6,-8,7,6,10,-7,-6,7,-10,3,8,8,2,7,-10,4,4,-6,-5,9,2,8,-8,10,-2,9,-2,5,2,-7,3,-8,-7,-10,-9,-8,6,7,-10,1,9,-3,-7,-7,8,-1,7,-10,6,-7,-8,3,10,7,8,-6,-9,10,-5,5,10,4,7,-2,-3,-5,-3,-6,-10,-4,2,7,-9,9,3,5,2,-3,-5,-4,-5,1,9,2,2,-8,-8,-8,-4,-8,3,-2,-7,5,-3,10,8,-5,-1,-6,5,-7,-1,-7,-2,-3,10,-9,4,9,-5,-5,-2,-1,7,4,-3,4,-6,10,6,4,-1,-5,8,-10,2,-5,-6,-5,-6,-5,-2,5,-10,7,-10,-5,3,-4,3,6,-1,-10,-9,-10,-6,6,-5,-7,7,4,4,-8,7,-9,-8,-6,6,-6,2,2,2,-7,8,-6,7,-4,-7,-9,-6,7,-3,-3,-10,6,4,10,-5,-4,1,9,10,-9,8,5,6,8,-6,2,7,-8,7,8,4,-6,4,5,1,-2,1,4,7,1,-2,-9,-1,1,-4,-2,3,-3,5,10,1,-6,-7,-4,-2,-8,-7,3,-4,8,3,6,7,-10,9,-8,-10,-7,-5,-1,-7,1,-10,6,9,1,5,8,1,4,-10,4,-9,8,3,2,2,8,10,-5,-7,10,8,-5,8,10,-4,-9,-7,-8,6,-2,5,-10,1,3], dtype = "int64")#candidate|4291|(630,)|const|int64
call_4290 = func_432_call(relay.reshape(const_4291.astype('int64'), [15, 7, 6]), relay.reshape(const_4291.astype('int64'), [15, 7, 6]), )
call_4292 = func_432_call(relay.reshape(const_4291.astype('int64'), [15, 7, 6]), relay.reshape(const_4291.astype('int64'), [15, 7, 6]), )
output = relay.Tuple([uop_4287,call_4290,const_4291,])
output2 = relay.Tuple([uop_4287,call_4292,const_4291,])
func_4303 = relay.Function([], output)
mod['func_4303'] = func_4303
mod = relay.transform.InferType()(mod)
output = func_4303()
func_4304 = relay.Function([], output)
mutated_mod['func_4304'] = func_4304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3903_call = mod.get_global_var('func_3903')
func_3904_call = mutated_mod.get_global_var('func_3904')
call_4413 = func_3903_call()
call_4414 = func_3903_call()
output = call_4413
output2 = call_4414
func_4443 = relay.Function([], output)
mod['func_4443'] = func_4443
mod = relay.transform.InferType()(mod)
mutated_mod['func_4443'] = func_4443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4443_call = mutated_mod.get_global_var('func_4443')
call_4444 = func_4443_call()
output = call_4444
func_4445 = relay.Function([], output)
mutated_mod['func_4445'] = func_4445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_4446 = func_3765_call()
call_4447 = func_3765_call()
func_4027_call = mod.get_global_var('func_4027')
func_4028_call = mutated_mod.get_global_var('func_4028')
call_4456 = func_4027_call()
call_4457 = func_4027_call()
output = relay.Tuple([call_4446,call_4456,])
output2 = relay.Tuple([call_4447,call_4457,])
func_4461 = relay.Function([], output)
mod['func_4461'] = func_4461
mod = relay.transform.InferType()(mod)
output = func_4461()
func_4462 = relay.Function([], output)
mutated_mod['func_4462'] = func_4462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4027_call = mod.get_global_var('func_4027')
func_4028_call = mutated_mod.get_global_var('func_4028')
call_4480 = func_4027_call()
call_4481 = func_4027_call()
uop_4508 = relay.rsqrt(call_4480.astype('float64')) # shape=(11, 12, 15)
uop_4510 = relay.rsqrt(call_4481.astype('float64')) # shape=(11, 12, 15)
uop_4512 = relay.acos(uop_4508.astype('float64')) # shape=(11, 12, 15)
uop_4514 = relay.acos(uop_4510.astype('float64')) # shape=(11, 12, 15)
func_567_call = mod.get_global_var('func_567')
func_569_call = mutated_mod.get_global_var('func_569')
const_4517 = relay.const([9.851551,-5.950003,0.723774,4.033527,-4.738903,-5.499389,5.417610,-5.585311,-4.495388,-7.193388,8.578788,8.917744,9.739818,-3.154163,9.550569,0.060345,6.769123,-4.729459,-3.019552,3.574727,7.150630,5.811656,4.394482,-5.674255,-8.097311,-7.418286,7.975334,-3.477339,3.870803,-7.283400,9.381363,0.116808,8.574261,6.698549,2.091647,-7.069203,-1.520758,-9.273260,9.285562,-8.094111,7.965765,3.887781,-6.853810,8.206375,5.538769,-4.681552,-2.158564,6.577324,3.619341,0.553632,3.859399,3.106658,-8.675697,-8.260046,-4.819387,0.810855,2.247839,4.753342,-3.930491,0.275133,-2.986239,-5.921777,0.166083,-4.885453,-4.421722,-2.522864,5.717459,-2.574050,0.673855,5.195847,4.081846,2.609999,-5.864591,-1.295392,5.139183,-2.721313,0.795813,-5.370830,-1.701494,2.703582,6.688503,-6.127055,2.572433,-6.886212,6.234338,-4.905365,-2.216703,-0.273898,-0.157119,3.911214,-9.464861,5.007290,2.623920,8.624708,-4.894996,-7.150175,-6.088558,-1.859596,3.397138,-7.260328,2.575537,7.412914,-6.371682,-4.981195,-4.087628,-3.233609,2.426477,-0.954691,-9.268452,-8.717149,-3.162199,-7.830193], dtype = "float32")#candidate|4517|(112,)|const|float32
call_4516 = func_567_call(relay.reshape(const_4517.astype('float32'), [16, 7, 1]))
call_4518 = func_567_call(relay.reshape(const_4517.astype('float32'), [16, 7, 1]))
func_1469_call = mod.get_global_var('func_1469')
func_1472_call = mutated_mod.get_global_var('func_1472')
const_4523 = relay.const([-10,-5,-10,5,5,5,-2,-2,10,6,9,-2,-2,1,2,8,-1,-2,-9,2,-4,-7,-1,5,-10,-9,-3,-5,-9,-2,8,-10,4,-1,8,-8,-2,3,5,7,9,6,7,8,8,7,-10,9,1,-7,-5,3,2,-3,6,-4,-5,8,2,10,-5,-9,7,7,8,-9,10,4,-10,9,-8,10,3,-7,-3,8,7,-1,3,-2,-3,-8,3,-5,9,-8,8,2,5,8,-8,3,4,-10,1,10,3,9,9], dtype = "int32")#candidate|4523|(99,)|const|int32
call_4522 = relay.TupleGetItem(func_1469_call(relay.reshape(const_4523.astype('int32'), [1, 11, 9])), 0)
call_4524 = relay.TupleGetItem(func_1472_call(relay.reshape(const_4523.astype('int32'), [1, 11, 9])), 0)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_4526 = func_3765_call()
call_4527 = func_3765_call()
output = relay.Tuple([uop_4512,call_4516,const_4517,call_4522,const_4523,call_4526,])
output2 = relay.Tuple([uop_4514,call_4518,const_4517,call_4524,const_4523,call_4527,])
func_4530 = relay.Function([], output)
mod['func_4530'] = func_4530
mod = relay.transform.InferType()(mod)
mutated_mod['func_4530'] = func_4530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mutated_mod.get_global_var('func_4530')
call_4531 = func_4530_call()
output = call_4531
func_4532 = relay.Function([], output)
mutated_mod['func_4532'] = func_4532
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4533 = relay.const([[[-5.948041,7.767888,7.753829,-6.620012],[6.408256,7.143701,0.499042,4.460842],[-6.116577,7.562395,9.877649,-3.765065],[4.755355,-7.324918,-8.581190,4.308235],[-6.965377,-7.854802,-3.789110,4.766324],[-1.425875,4.855616,5.373834,9.100621],[-3.332734,-8.853130,-9.588759,-3.112031],[-1.684266,0.152136,7.951948,-3.865976],[1.609693,4.406614,0.765477,5.972584],[-5.946877,3.819569,0.988807,1.847907],[-0.641408,9.282613,2.904378,-7.700593],[3.992558,-7.455701,-6.610775,-9.062438],[-0.786439,-5.905662,-6.720015,5.639312]],[[-8.223687,-9.011551,3.077981,-5.740020],[7.664547,-8.063063,5.254057,-8.729241],[4.246016,5.882725,6.482748,9.508511],[-8.959571,-3.395199,-4.000385,9.939518],[-7.423075,-0.477981,3.425190,3.891287],[9.315692,9.775211,4.605017,8.091280],[5.853057,-8.969369,-0.645024,-9.682223],[6.538574,3.981411,-8.007045,5.151645],[-3.590883,3.433509,-7.498151,-7.618863],[-4.585185,-5.013317,2.675560,-5.261215],[7.550454,-1.393877,9.638204,-6.978407],[0.638582,-8.722867,-3.911442,-5.293897],[2.704502,-7.201647,0.313100,0.762269]],[[3.654381,8.897232,5.766257,1.146913],[-0.297176,-7.944355,-5.029555,1.112445],[-2.073964,3.390036,8.737067,0.058369],[9.045825,-1.183308,-6.731713,8.845776],[5.449659,4.432754,-1.374066,6.196481],[-5.097093,-0.948687,-6.113739,-5.421138],[4.917879,7.472557,4.324617,-1.744787],[7.161436,2.350230,-0.968274,9.222782],[8.566692,3.705572,0.620644,6.889609],[-6.887362,-5.621888,4.475704,-7.090146],[-7.982321,5.315897,-2.271847,9.568627],[-3.150693,-6.679171,1.063938,-8.158401],[-2.056465,-0.642301,5.797671,1.908383]],[[-7.063196,-6.030206,-9.519588,-7.727775],[5.292422,-2.824333,1.609711,1.023383],[9.645232,2.940769,2.307536,0.306394],[4.962429,8.008177,4.235599,-1.940642],[-1.005338,7.635301,8.333735,6.884504],[0.039399,4.866628,8.530597,-5.308439],[-1.888993,0.503630,-4.661968,8.796505],[1.717236,-8.715975,7.723039,-4.232070],[2.502604,-4.681436,4.912967,6.752706],[5.491952,-9.642828,2.372440,7.172934],[-1.854596,9.350267,-1.189075,-5.985779],[5.856071,-4.143072,0.612964,-9.868315],[9.097133,-8.905755,4.337175,8.281826]],[[-9.426739,0.656246,4.253657,6.503675],[-7.392302,-9.654330,3.892786,-0.428872],[5.490607,8.502263,5.296920,7.775846],[-0.879322,8.407673,-9.203740,-0.070149],[-2.375157,-0.757235,5.964109,8.741680],[8.888862,-1.096472,-7.607574,3.511303],[5.189283,3.602586,6.863979,9.919012],[-0.783088,1.183889,-4.144889,7.552724],[4.668783,-0.230451,9.016786,-2.032793],[2.642502,3.886219,2.563314,1.502272],[4.418302,8.976815,3.202090,-4.993655],[-9.217029,-7.957032,2.941890,9.817408],[-3.378411,9.529075,-8.135007,-6.739675]],[[-2.452644,5.466389,-3.934874,7.386347],[6.604913,-5.159817,1.312658,-9.419920],[-5.824992,-5.013193,-5.608675,8.951338],[3.301956,-3.248422,-4.657208,7.605245],[-3.796093,3.891573,1.995677,-4.210372],[3.298531,-8.879758,2.905356,-6.911304],[0.110686,-1.182995,9.531987,-7.563027],[-4.681336,-6.366899,8.175711,-9.254182],[-6.397211,5.725915,-2.268728,9.280714],[-4.962269,-0.333103,-7.077154,-8.730587],[-8.933564,-6.320301,-7.790843,-6.647486],[2.052412,5.077137,7.907872,9.385291],[3.789442,4.160944,-6.747456,-3.700274]],[[-8.602200,2.764928,6.164926,4.927941],[-7.916739,4.791235,-0.341544,2.702925],[-2.205302,4.333063,-6.922313,-4.023675],[7.818277,5.753990,-7.379599,-2.235577],[7.499851,0.342277,7.144938,-5.516854],[-0.396713,-0.219337,8.566147,8.566443],[1.694286,2.915475,0.505188,2.727102],[-0.415598,-8.215739,-5.062803,2.432288],[-1.690622,5.180074,4.025960,0.254088],[8.733043,0.508201,-0.072529,5.296553],[7.062329,9.916379,-4.938334,8.752107],[-3.646694,2.671489,-7.803829,-7.584729],[1.671806,1.545153,1.519665,6.658338]],[[-2.320279,1.006726,0.678582,-5.560667],[-1.251437,5.848580,1.589686,5.395500],[-4.808621,-3.630148,5.067883,-0.823326],[-4.683378,-9.187928,-8.091265,5.829777],[-3.889829,6.010236,7.215702,-6.182635],[-8.245941,-4.412898,-4.607393,7.461765],[-3.175905,7.298836,-0.189777,-4.281189],[6.381950,-6.910253,-9.611544,7.558665],[-9.888913,-1.700397,-4.106921,7.481802],[-2.507401,-1.090002,6.897660,-5.476972],[-9.144949,-4.896602,2.445636,2.129678],[5.100537,-8.397112,2.440080,-2.452607],[6.432262,1.855436,3.141896,-0.735794]],[[-0.596058,-5.362169,-7.356229,6.115800],[-6.578323,3.246909,3.616891,0.896645],[-0.827333,-4.635176,8.020102,1.570774],[-3.071269,-0.586680,-2.508141,2.693420],[-8.287798,-6.311462,-7.163260,3.818637],[4.652608,-2.970194,5.130417,5.290607],[-4.687879,-8.430166,-5.849699,-9.325225],[-9.456532,-3.545621,3.070055,-1.692623],[7.738575,-6.285510,-4.507409,8.493527],[-3.271121,-4.107710,5.022592,4.779456],[-1.627186,7.336698,3.631561,1.707970],[-8.620961,-9.778212,8.344636,1.665123],[-8.429290,7.787686,8.313675,-4.949537]],[[-7.052319,-1.099276,2.374317,4.375001],[6.000199,-0.823977,-8.307106,-7.596059],[-5.589785,-4.028376,2.118832,-5.526525],[2.361776,2.564620,-6.027479,-7.899902],[-6.498962,-5.053359,-2.995476,4.823561],[-3.400312,2.960061,0.918025,-4.996712],[-8.362222,-1.910119,-1.519412,4.704251],[-1.661148,7.398597,1.638630,2.822895],[-1.748335,4.533520,-6.420198,-9.041967],[-8.118938,9.783379,7.705982,7.563860],[6.895290,-9.148388,5.695063,0.575538],[-0.680404,-7.475187,9.444655,5.354673],[-2.562764,-0.758543,-3.302792,9.088706]],[[-3.603905,-9.694930,-8.019162,-8.240176],[4.620419,-7.234446,-3.308237,-5.754829],[-3.931898,-9.220946,9.664011,9.314732],[-7.093195,-1.006125,-4.201250,-8.770304],[-5.503457,-1.791212,-6.586709,-7.133662],[1.561380,-1.629523,9.596840,-6.075146],[-6.787065,6.523778,8.350833,0.963238],[-3.759140,-5.193737,6.826684,-0.785621],[6.476887,3.717460,6.035773,-1.403612],[-8.573042,-9.035255,2.860395,2.969470],[-0.268878,5.821174,1.073201,7.992680],[-7.407595,-5.620083,-5.547799,-9.126218],[8.706339,-8.431203,4.358540,-9.483495]],[[1.630555,6.770192,0.270560,-4.068377],[4.380867,3.300877,-0.313434,4.373675],[-8.589516,2.392484,-8.183053,6.228911],[9.564305,-9.483996,-6.904506,-2.978521],[8.787536,-4.802268,-0.863812,-2.724007],[7.767421,-8.545800,0.174383,-1.648865],[2.820638,-2.513046,2.504730,7.616807],[1.365729,-3.402095,-0.462601,-8.504905],[-6.338474,0.690364,0.810011,6.946721],[5.549460,2.159519,4.991614,5.039503],[1.780513,-7.776121,8.021819,8.106943],[4.343045,-9.143542,-7.953012,1.786718],[4.958167,7.708324,2.162287,3.593219]],[[-4.649055,8.741988,1.607647,-9.651094],[-0.804794,6.231618,-1.785768,5.151383],[-0.858703,-7.708999,-0.538884,-3.391331],[-2.213879,-9.081065,-5.709770,-3.043990],[-8.690174,-0.727561,-6.846723,-6.037680],[8.866528,-7.870147,-9.261179,1.428669],[2.178434,9.761449,1.980304,-6.100975],[9.393858,0.879183,-1.438856,-9.910894],[1.695752,-0.635436,1.404414,0.662040],[7.785004,9.622559,1.312005,-0.664916],[-5.885048,-9.128529,8.051737,6.100050],[7.194482,-8.374016,-1.991514,1.157711],[3.600431,-9.340369,-0.782770,5.360486]]], dtype = "float32")#candidate|4533|(13, 13, 4)|const|float32
uop_4534 = relay.sqrt(const_4533.astype('float32')) # shape=(13, 13, 4)
uop_4536 = relay.log10(uop_4534.astype('float64')) # shape=(13, 13, 4)
bop_4549 = relay.floor_mod(const_4533.astype('float64'), relay.reshape(uop_4534.astype('float64'), relay.shape_of(const_4533))) # shape=(13, 13, 4)
bop_4556 = relay.logical_or(uop_4536.astype('bool'), relay.reshape(bop_4549.astype('bool'), relay.shape_of(uop_4536))) # shape=(13, 13, 4)
const_4567 = relay.const([[[-1.683222,8.328798,-3.903526,-7.483597],[5.094491,-7.912975,5.484366,-5.712093],[-5.910705,8.994140,4.247637,9.134152],[-5.871843,-4.734995,-3.946473,-9.498548],[-8.516274,5.168864,9.690112,4.568197],[-9.470741,-3.289849,7.830510,8.213463],[-0.951677,-8.918026,-3.094200,-0.347096],[-6.775700,1.278951,-6.372886,5.816093],[5.238542,6.748871,3.458508,5.212834],[-5.870508,1.708490,-4.261770,-6.282361],[-9.062336,-5.276559,-4.702217,4.579607],[2.779140,-7.426053,-2.922213,1.187518],[-6.281711,-7.838418,7.811844,5.253940]],[[2.701453,9.576144,3.239929,-0.659752],[9.855559,4.464627,8.615787,-6.632649],[2.828857,5.540775,9.745577,4.610398],[4.448132,2.274411,4.841647,3.660857],[1.992345,0.026051,-1.654697,-7.510711],[-3.875200,3.538886,2.556535,0.364962],[-6.481547,-4.551595,6.321619,-8.848880],[-5.282781,3.017725,-1.421067,-6.408841],[-6.196835,8.580178,-5.575490,-8.260177],[6.703521,-8.836485,8.289896,7.773304],[-4.997728,1.360853,1.075852,4.561043],[3.470168,8.800710,3.154904,-6.321224],[9.316716,-9.775947,9.002755,7.060778]],[[-9.616228,4.082891,1.154332,-5.134266],[4.709936,5.606644,8.725920,-9.327858],[5.237674,-7.164514,7.020946,-2.665775],[-6.489811,-5.329647,2.935265,-2.670186],[-9.126236,-3.740872,-9.302816,0.667754],[-4.993132,-8.978336,0.095709,2.782742],[8.316302,2.787633,-9.774138,7.630087],[-1.622640,-7.094082,3.742522,-3.560351],[5.391175,8.629080,0.027957,2.941553],[4.656059,4.353278,-8.152507,-0.848291],[-0.177354,-6.920361,5.039509,-3.055334],[-0.684066,-0.142263,1.231003,5.181275],[2.339240,6.145538,8.384479,-3.149757]],[[-6.191084,-0.947176,-9.149356,-5.542991],[-1.754868,2.111217,5.413783,-7.196726],[1.718461,5.188215,9.944009,0.077772],[-6.573347,0.857808,1.439653,-8.798948],[3.490733,-2.715942,1.016331,-7.541417],[9.297504,-5.641459,3.305071,-1.713552],[4.967327,-2.234346,-0.216259,0.730577],[-7.516543,1.909877,-1.479137,9.698293],[-0.854777,-0.160616,9.688284,9.470966],[-2.415672,6.172599,-5.103340,-0.121994],[7.966476,-5.927056,-3.531008,-5.386327],[-6.251244,-4.845143,-5.951638,-8.120402],[1.611137,-6.832368,-3.100584,-3.912111]],[[4.857001,-7.627263,0.910634,6.020867],[7.840201,0.727727,4.361620,-7.120410],[9.164624,1.850511,9.681090,-0.256079],[-9.122125,3.386884,-7.369148,8.298719],[6.474633,-5.578670,2.252837,8.102061],[9.210723,-1.104618,6.146996,0.484579],[-4.307846,-3.004582,-2.212981,-0.680082],[5.350182,2.679738,8.708593,-3.381958],[4.572732,-0.067397,-0.230976,8.272442],[-1.994723,6.489162,3.296850,-0.780369],[5.860688,1.916576,2.017957,-4.908741],[5.663596,-2.884360,-2.296883,6.429576],[7.647947,-9.163601,7.348864,-0.516789]],[[-2.441781,5.453234,-7.645264,5.775956],[-6.277068,3.769625,-8.587172,2.637916],[-2.362453,8.146518,-9.032784,-9.964452],[-5.776064,3.306224,-1.660742,9.878961],[4.670005,-3.703253,-2.112180,9.312568],[-2.283380,-6.245803,-8.984929,-7.435010],[3.053676,-1.267983,-4.584352,-3.149519],[6.926694,3.979755,5.031931,-5.232253],[6.505422,-5.396693,-9.940772,9.475015],[-5.710779,-2.058039,1.718810,7.166147],[-8.938842,-1.342395,-1.411749,4.368204],[-9.527948,-8.057367,3.185140,7.239117],[6.083907,-8.238824,1.310684,6.175770]],[[1.014904,1.698439,-5.754752,4.475283],[-9.280938,-0.365196,-0.730145,-4.879271],[-9.436999,-0.310891,-9.877898,-0.642847],[0.300982,2.579041,-7.616031,8.556474],[-3.400492,-1.859719,5.807642,2.369260],[9.079333,8.791701,1.529699,1.274732],[-1.936688,0.700928,7.418533,-8.027891],[-1.858616,4.776517,-0.947649,-9.267751],[5.404610,-6.007736,1.607253,-6.414128],[1.499539,-6.680197,-4.622277,-1.446867],[-1.309962,7.825979,0.269403,-6.986532],[1.938220,4.942197,-2.732306,8.979802],[-6.758815,8.737069,4.840341,8.225439]],[[9.210429,-5.328046,3.858270,-0.791603],[-3.757936,9.608182,8.496633,-3.359678],[4.845758,8.677641,9.735947,-1.914880],[-9.755647,2.363279,0.546507,-7.960083],[9.723875,-5.630618,0.326531,-2.437787],[-3.604090,8.751918,2.124303,7.662259],[3.409323,3.657643,3.473193,7.895643],[8.515881,7.916817,5.600728,2.584023],[-5.955263,8.881535,-8.915627,-1.925935],[8.635943,-4.826177,1.855248,8.601388],[-3.475346,6.279746,-1.353907,8.402197],[-9.474491,3.855552,-3.787130,-9.568572],[-6.639523,-6.391594,8.923660,-0.611584]],[[9.994590,1.569501,-5.430387,3.988454],[3.580202,-2.167156,3.865644,9.728765],[-7.331562,2.702535,0.966908,-4.562776],[3.841797,-0.153368,9.753245,0.667354],[-7.682223,1.731085,-3.354722,7.647552],[3.879846,1.175433,-3.307023,-4.227306],[5.551064,3.584472,1.106493,8.348295],[8.107612,6.645200,-9.553317,9.704553],[-1.677111,6.317523,2.277866,-7.830682],[-3.244145,-5.907010,0.690265,8.291969],[-6.356655,9.524178,-5.790270,7.138360],[1.734552,-2.084010,2.265079,-0.487515],[-6.403791,-3.030183,-5.884754,7.143591]],[[9.901773,3.539853,-2.228054,0.026838],[-3.905804,5.613545,2.356010,-5.126398],[7.556605,-0.605955,-0.440515,-9.810995],[-4.946878,-5.828151,-3.935560,1.664295],[4.730088,-9.090510,-1.854678,4.413583],[-1.473013,9.457388,4.244392,-9.137907],[3.000867,9.251846,8.943480,-8.342388],[4.897620,8.603160,-3.615930,5.708238],[9.004302,-1.239495,8.508347,-2.005968],[-0.565460,-3.541284,8.137348,-9.887070],[9.211526,-9.204450,-0.151422,2.171356],[-6.909186,3.799878,8.126828,-0.977759],[-8.926677,-7.683315,-9.916086,9.624869]],[[7.017441,-0.001737,0.505597,3.718017],[2.522085,7.970996,-2.503292,0.006867],[7.287995,-3.990148,1.919251,-6.182939],[7.785628,1.726799,3.438631,-8.358054],[-5.890383,-2.565057,6.449129,8.024951],[0.617778,-8.395520,9.366019,-4.685058],[-4.673604,5.040271,-1.925826,7.871421],[7.237849,0.449772,-7.761226,8.472837],[4.217834,-5.665572,5.989650,3.684312],[-1.717989,-6.297331,5.586455,6.625158],[2.118445,2.083699,-3.105200,2.662786],[3.867323,-8.162457,-8.693117,4.017199],[0.755053,6.100442,4.848162,-7.487681]],[[-1.137123,7.044287,7.074038,-6.871995],[4.312516,-6.622226,-6.373038,5.009933],[6.886968,9.348458,2.111990,4.088975],[-5.505509,6.049789,9.728851,-9.323459],[6.236717,4.789939,-7.524798,5.971963],[2.338470,6.720005,-8.049579,3.491741],[-4.207381,4.092836,9.960701,4.797761],[1.707536,3.311722,-8.892506,3.620178],[6.083382,-0.167652,-7.242511,-6.355271],[-9.288178,3.591379,-0.264136,-5.311217],[-0.170081,8.133635,-7.416942,9.788518],[2.147060,-7.129462,-0.542177,6.496298],[-9.768120,6.110442,-0.760222,-0.805277]],[[0.398264,7.271978,-9.575451,3.238944],[7.287945,3.627407,1.875894,-5.016115],[3.516058,-7.658073,-9.746522,-2.436388],[0.479343,5.923222,3.853873,-2.623795],[4.711182,-8.827935,0.179017,-3.891670],[-6.955992,-3.920460,4.513238,1.925233],[2.917073,-5.618890,9.755778,-2.225262],[9.701388,-6.856341,0.070063,2.162457],[-4.049408,5.206626,6.610893,1.432832],[4.170220,9.130775,-7.482005,8.111712],[-3.290969,9.357859,-9.429571,5.978914],[8.681614,-9.813081,-2.024606,0.231352],[-0.340583,5.271434,1.180834,5.871219]]], dtype = "float64")#candidate|4567|(13, 13, 4)|const|float64
bop_4568 = relay.equal(uop_4536.astype('bool'), relay.reshape(const_4567.astype('bool'), relay.shape_of(uop_4536))) # shape=(13, 13, 4)
output = relay.Tuple([bop_4556,bop_4568,])
output2 = relay.Tuple([bop_4556,bop_4568,])
func_4573 = relay.Function([], output)
mod['func_4573'] = func_4573
mod = relay.transform.InferType()(mod)
mutated_mod['func_4573'] = func_4573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4573_call = mutated_mod.get_global_var('func_4573')
call_4574 = func_4573_call()
output = call_4574
func_4575 = relay.Function([], output)
mutated_mod['func_4575'] = func_4575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4573_call = mod.get_global_var('func_4573')
func_4575_call = mutated_mod.get_global_var('func_4575')
call_4582 = relay.TupleGetItem(func_4573_call(), 1)
call_4583 = relay.TupleGetItem(func_4575_call(), 1)
uop_4590 = relay.cosh(call_4582.astype('float64')) # shape=(13, 13, 4)
uop_4592 = relay.cosh(call_4583.astype('float64')) # shape=(13, 13, 4)
bop_4599 = relay.left_shift(uop_4590.astype('uint32'), relay.reshape(call_4582.astype('uint32'), relay.shape_of(uop_4590))) # shape=(13, 13, 4)
bop_4602 = relay.left_shift(uop_4592.astype('uint32'), relay.reshape(call_4583.astype('uint32'), relay.shape_of(uop_4592))) # shape=(13, 13, 4)
bop_4603 = relay.mod(bop_4599.astype('float64'), relay.reshape(uop_4590.astype('float64'), relay.shape_of(bop_4599))) # shape=(13, 13, 4)
bop_4606 = relay.mod(bop_4602.astype('float64'), relay.reshape(uop_4592.astype('float64'), relay.shape_of(bop_4602))) # shape=(13, 13, 4)
output = bop_4603
output2 = bop_4606
func_4628 = relay.Function([], output)
mod['func_4628'] = func_4628
mod = relay.transform.InferType()(mod)
mutated_mod['func_4628'] = func_4628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mutated_mod.get_global_var('func_4628')
call_4629 = func_4628_call()
output = call_4629
func_4630 = relay.Function([], output)
mutated_mod['func_4630'] = func_4630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_4661 = relay.TupleGetItem(func_3714_call(), 0)
call_4662 = relay.TupleGetItem(func_3716_call(), 0)
func_3199_call = mod.get_global_var('func_3199')
func_3202_call = mutated_mod.get_global_var('func_3202')
var_4674 = relay.var("var_4674", dtype = "int64", shape = ())#candidate|4674|()|var|int64
const_4675 = relay.const([2,10,3,-1,-8,-8,-1,8,-6,2,-6,-6,1,-10,-2,4,8,-5,3,1,-8,4,9,3,-2,-1,8,-9,-9,-5,5,-6,-5,-7,-8,10,5,-7,5,-10,-5,-7,8,-9,-6,-9,-4,-5,-7,-9,-9,3,2,-10,10,-6,-3,-7,1,-2,-10,8,-8,-5,5,10,-3,-10,4,4,4,-10,-4,-9,-3,-2,4,9,2,6,9,3,-10,-9,-5,-10,-2,5,7,3,-7,-3,6,2,9,7,-6,2,-3,4,-3,-6,-5,2,-5,10,-9,-2,8,-3,3,-6,10,7,-8,-1,5,5,8,-10,10,4,4,4,-1], dtype = "int64")#candidate|4675|(125,)|const|int64
call_4673 = relay.TupleGetItem(func_3199_call(relay.reshape(var_4674.astype('int64'), []), relay.reshape(const_4675.astype('int64'), [5, 5, 5]), ), 0)
call_4676 = relay.TupleGetItem(func_3202_call(relay.reshape(var_4674.astype('int64'), []), relay.reshape(const_4675.astype('int64'), [5, 5, 5]), ), 0)
uop_4683 = relay.sin(call_4673.astype('float32')) # shape=(5, 5, 5)
uop_4685 = relay.sin(call_4676.astype('float32')) # shape=(5, 5, 5)
output = relay.Tuple([call_4661,var_4674,const_4675,uop_4683,])
output2 = relay.Tuple([call_4662,var_4674,const_4675,uop_4685,])
func_4686 = relay.Function([var_4674,], output)
mod['func_4686'] = func_4686
mod = relay.transform.InferType()(mod)
var_4687 = relay.var("var_4687", dtype = "int64", shape = ())#candidate|4687|()|var|int64
output = func_4686(var_4687)
func_4688 = relay.Function([var_4687], output)
mutated_mod['func_4688'] = func_4688
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4789 = relay.const([[[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[False],[True],[False]],[[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False],[False]],[[True],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False]],[[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False]],[[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[False]],[[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True]],[[False],[False],[False],[False],[False],[False],[True],[False],[False],[True],[True],[True],[False],[False],[False],[False]],[[True],[False],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[True]],[[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[True],[True]],[[False],[True],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True]],[[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[True],[False],[True],[False],[True],[True]],[[False],[False],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False]],[[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True]],[[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[True],[False],[True],[False],[False],[True]],[[False],[True],[True],[False],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False]],[[False],[False],[False],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False]]], dtype = "bool")#candidate|4789|(16, 16, 1)|const|bool
const_4790 = relay.const([[[False,False,True],[False,True,True],[False,False,True],[True,False,True],[False,False,True],[False,True,False],[False,True,False],[False,True,False],[False,False,True],[True,False,True],[True,True,True],[True,True,False],[False,False,True],[True,True,True],[False,True,True],[False,True,False]],[[False,False,True],[False,False,True],[False,False,True],[False,True,True],[True,True,False],[True,False,False],[True,False,False],[False,True,True],[True,False,True],[False,False,False],[False,False,False],[False,False,True],[True,False,True],[False,False,True],[True,False,False],[False,True,False]],[[False,False,False],[False,True,True],[True,False,True],[False,True,True],[True,True,True],[True,True,True],[False,False,False],[False,False,False],[True,False,False],[True,False,True],[True,False,False],[True,False,True],[False,True,True],[False,False,False],[True,True,False],[True,False,True]],[[False,True,False],[False,True,False],[True,False,False],[True,True,False],[True,False,False],[True,True,False],[False,True,False],[True,True,False],[False,True,True],[False,False,True],[True,False,False],[True,True,True],[False,False,True],[False,True,False],[True,False,False],[True,True,True]],[[False,True,True],[False,True,False],[False,True,True],[True,True,True],[False,False,False],[True,False,True],[False,False,True],[False,False,False],[False,True,True],[True,True,False],[False,True,False],[True,True,True],[False,True,False],[True,False,True],[True,False,True],[True,True,True]],[[False,False,True],[True,False,False],[True,False,True],[False,True,False],[True,False,True],[True,True,False],[False,True,True],[False,True,True],[True,False,False],[False,True,True],[False,True,True],[True,False,True],[True,True,False],[True,False,True],[True,True,True],[True,False,True]],[[True,False,False],[True,False,True],[False,True,True],[False,True,False],[False,True,True],[True,True,True],[True,False,True],[True,True,True],[False,True,False],[False,False,False],[True,True,False],[True,False,False],[True,True,True],[False,True,False],[True,True,False],[False,True,True]],[[False,False,True],[True,True,True],[False,True,False],[False,True,False],[False,False,True],[False,False,False],[False,True,True],[True,True,False],[True,False,False],[True,True,True],[False,True,True],[False,False,False],[True,False,True],[True,False,True],[True,False,True],[False,False,True]],[[False,False,False],[True,True,False],[False,False,False],[False,False,True],[True,False,False],[False,False,False],[False,True,False],[True,False,False],[False,True,False],[False,False,False],[True,False,False],[False,False,True],[False,False,False],[False,False,False],[False,True,False],[False,True,True]],[[True,True,False],[True,False,True],[False,True,False],[False,True,False],[True,False,True],[True,False,True],[True,False,True],[True,True,True],[True,True,False],[True,True,True],[False,False,False],[True,False,False],[False,False,True],[False,False,False],[True,True,True],[False,True,True]],[[True,False,False],[False,True,True],[True,False,False],[True,True,True],[False,False,False],[False,True,False],[False,True,False],[False,True,False],[False,False,False],[True,False,True],[True,True,True],[True,True,False],[False,False,False],[False,True,True],[True,True,True],[True,True,False]],[[True,False,True],[True,False,True],[False,False,True],[False,False,False],[True,True,True],[False,False,True],[False,False,True],[False,False,True],[True,True,False],[True,True,False],[True,False,False],[True,False,False],[False,False,False],[True,False,False],[True,True,True],[True,True,True]],[[False,True,True],[True,True,True],[False,False,True],[True,True,False],[True,True,False],[True,False,False],[True,False,False],[True,True,False],[False,True,True],[True,False,False],[True,False,True],[False,True,False],[False,False,True],[True,True,False],[True,False,True],[True,True,True]],[[False,False,True],[False,True,True],[True,True,False],[False,True,False],[True,False,False],[False,False,True],[True,False,True],[False,True,False],[False,False,False],[False,False,True],[True,False,True],[True,False,True],[False,True,False],[False,False,True],[False,True,True],[False,True,False]],[[True,False,False],[True,False,False],[True,True,False],[False,True,False],[True,False,False],[True,True,True],[False,True,False],[False,True,False],[False,True,True],[True,True,True],[True,True,True],[False,False,False],[False,True,True],[False,True,False],[True,True,False],[True,False,False]],[[False,False,True],[True,False,True],[True,False,False],[True,False,False],[False,True,True],[True,True,True],[True,True,False],[False,False,False],[False,True,True],[True,False,True],[True,True,True],[False,False,True],[True,True,False],[False,False,False],[False,False,True],[True,False,True]]], dtype = "bool")#candidate|4790|(16, 16, 3)|const|bool
bop_4791 = relay.logical_and(const_4789.astype('bool'), const_4790.astype('bool')) # shape=(16, 16, 3)
func_3903_call = mod.get_global_var('func_3903')
func_3904_call = mutated_mod.get_global_var('func_3904')
call_4795 = func_3903_call()
call_4796 = func_3903_call()
uop_4807 = relay.sigmoid(const_4790.astype('float32')) # shape=(16, 16, 3)
uop_4815 = relay.cosh(const_4790.astype('float64')) # shape=(16, 16, 3)
bop_4817 = relay.multiply(uop_4815.astype('float64'), relay.reshape(bop_4791.astype('float64'), relay.shape_of(uop_4815))) # shape=(16, 16, 3)
bop_4821 = relay.mod(uop_4815.astype('float64'), relay.reshape(bop_4791.astype('float64'), relay.shape_of(uop_4815))) # shape=(16, 16, 3)
output = relay.Tuple([call_4795,uop_4807,bop_4817,bop_4821,])
output2 = relay.Tuple([call_4796,uop_4807,bop_4817,bop_4821,])
func_4830 = relay.Function([], output)
mod['func_4830'] = func_4830
mod = relay.transform.InferType()(mod)
mutated_mod['func_4830'] = func_4830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4830_call = mutated_mod.get_global_var('func_4830')
call_4831 = func_4830_call()
output = call_4831
func_4832 = relay.Function([], output)
mutated_mod['func_4832'] = func_4832
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4849 = relay.var("var_4849", dtype = "float32", shape = (4, 8, 7))#candidate|4849|(4, 8, 7)|var|float32
uop_4850 = relay.cosh(var_4849.astype('float32')) # shape=(4, 8, 7)
output = uop_4850
output2 = uop_4850
func_4852 = relay.Function([var_4849,], output)
mod['func_4852'] = func_4852
mod = relay.transform.InferType()(mod)
mutated_mod['func_4852'] = func_4852
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4853 = relay.var("var_4853", dtype = "float32", shape = (4, 8, 7))#candidate|4853|(4, 8, 7)|var|float32
func_4852_call = mutated_mod.get_global_var('func_4852')
call_4854 = func_4852_call(var_4853)
output = call_4854
func_4855 = relay.Function([var_4853], output)
mutated_mod['func_4855'] = func_4855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mod.get_global_var('func_4149')
func_4151_call = mutated_mod.get_global_var('func_4151')
call_4857 = func_4149_call()
call_4858 = func_4149_call()
func_4303_call = mod.get_global_var('func_4303')
func_4304_call = mutated_mod.get_global_var('func_4304')
call_4864 = relay.TupleGetItem(func_4303_call(), 1)
call_4865 = relay.TupleGetItem(func_4304_call(), 1)
var_4868 = relay.var("var_4868", dtype = "float64", shape = (11, 12, 15))#candidate|4868|(11, 12, 15)|var|float64
bop_4869 = relay.minimum(call_4857.astype('uint8'), relay.reshape(var_4868.astype('uint8'), relay.shape_of(call_4857))) # shape=(11, 12, 15)
bop_4872 = relay.minimum(call_4858.astype('uint8'), relay.reshape(var_4868.astype('uint8'), relay.shape_of(call_4858))) # shape=(11, 12, 15)
uop_4877 = relay.sin(var_4868.astype('float32')) # shape=(11, 12, 15)
output = relay.Tuple([call_4864,bop_4869,uop_4877,])
output2 = relay.Tuple([call_4865,bop_4872,uop_4877,])
func_4906 = relay.Function([var_4868,], output)
mod['func_4906'] = func_4906
mod = relay.transform.InferType()(mod)
mutated_mod['func_4906'] = func_4906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4907 = relay.var("var_4907", dtype = "float64", shape = (11, 12, 15))#candidate|4907|(11, 12, 15)|var|float64
func_4906_call = mutated_mod.get_global_var('func_4906')
call_4908 = func_4906_call(var_4907)
output = call_4908
func_4909 = relay.Function([var_4907], output)
mutated_mod['func_4909'] = func_4909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4443_call = mod.get_global_var('func_4443')
func_4445_call = mutated_mod.get_global_var('func_4445')
call_4933 = func_4443_call()
call_4934 = func_4443_call()
var_4938 = relay.var("var_4938", dtype = "float64", shape = (11, 12, 15))#candidate|4938|(11, 12, 15)|var|float64
bop_4939 = relay.greater(call_4933.astype('bool'), relay.reshape(var_4938.astype('bool'), relay.shape_of(call_4933))) # shape=(11, 12, 15)
bop_4942 = relay.greater(call_4934.astype('bool'), relay.reshape(var_4938.astype('bool'), relay.shape_of(call_4934))) # shape=(11, 12, 15)
func_4686_call = mod.get_global_var('func_4686')
func_4688_call = mutated_mod.get_global_var('func_4688')
var_4950 = relay.var("var_4950", dtype = "int64", shape = ())#candidate|4950|()|var|int64
call_4949 = relay.TupleGetItem(func_4686_call(relay.reshape(var_4950.astype('int64'), [])), 1)
call_4951 = relay.TupleGetItem(func_4688_call(relay.reshape(var_4950.astype('int64'), [])), 1)
func_1898_call = mod.get_global_var('func_1898')
func_1903_call = mutated_mod.get_global_var('func_1903')
var_4954 = relay.var("var_4954", dtype = "float64", shape = (30, 2))#candidate|4954|(30, 2)|var|float64
const_4955 = relay.const([-3,8,-10,-1,5,4,4,5,-7,8,5,-7,-8,-7,10,-5,-8,9,5,-10,1,8,-5,-7,-8,-2,9,-3,-2,-3,10,-7,3,4,-4,-8,-2,10,-3,-10,4,-6,-3,1,-9,8,-4,-6,1,-5,-8,-1,1,-8,10,5,-3,-8,10,-4,6,8,8,-7,6,3,-2,6,6,8,-3,-2,4,3,-1,-2,-8,5,4,3,1,-8,2,8,6,-6,1,-3,9,-8,2,5,10,-4,-3,6,6,-1,-6,6,7,2,3,-10,3,3,9,3,-10,-4,7,7,6,10,6,-5,-2,-8,2,7,9,-1,8,8,3,10,-3,-3,-4,-2,-1,-3,4,7,-3,-3,4,1,-8,-7,2,-10,4,-6,8,-9,5,-3,-5,-6,7,-1,3,-1,2,3,7,10,9,-10,-2,-6,-2,5,-3,6,-10,1,2,4,3,-7,-1,2,3,-6,2,3,5,1,-8,-8,-7,-4,2,-2,-7,5,-8,-9,8,7,9,6,-7,-2,6,-7,-10,2,9,6,7,-4,-8,-7,10,8,3,5,-1,-8,8,9,-6,-9,7,1,-7,-10,-9,1,10,-1,1,6,3,-8,9,9,8,-10,-3,10,7,-5,6,10,-3,-10,6,-8,-10,-2,-4,4,-8,9,-7,-3,9,-5,-2,-9,-5,-1,5,-10,6,3,2,1,4,-3,-9,7,2,2,-8,-1,2,-4,3,-1,5,-10,3,-10,3,10,-10,1,1,-10,-6,10,4,4,-7,8,-9,2,2,-1,-5,-7,7,9,-9,7,-9,-3,10,-10,-2,-10,9,-5,3,-3,6,-3,6,-1,10,-2,4,2,3,-2,2,-8,-5,1,-8,8,4,6,-3,9,-4,4,6,-3,-10,6,10,-5,4,5,-8,-5,-4,4,-8,3,-4,2,-5,-1,-10,8,-10,5,9,-7,2,-1,4,4,-8,6,3,4,-2,6,-1,-2,-9,8,-8,7,8,4,3,8,4,5,-3,-9,1,9,-2,-6,9,-9,8,6,-3,-10,10,-10,-3,4,-2,-2,-10,9,-1,3,9,-6,-9,5,-3,-2,2,-9,-7,-2,8,5,5,2,-1,6,8,-8,-4,-10,-5,-2,-4,-5,-4,1,-1,1,-2,-9,-7,-2,-7,-3,1,-8,6,7,-10,3,7,5,-10,-3,-9,-5,7,3,-10,-5,-10,9,-4,5,9,6,-2,6,-1,-6,1,-9,1,-4,-8,1,-3,-1,-9,1,-6,5,-1,-4,10,-3,5,9,3,8,2,7,-2,-4,-9,-10,-3,-5,-6,5,2,6,9,3,9,-3,-1,-8,-1,7,-9,-4,-1,-7,9,4,-1,9,8,-1,-3,9,5,10,-2,-3,-3,-5,8,-5,3,10,-2,3,-3,8,-9,2,6,7,9,1,8,8,8,-7,-3,-5,8,-6,2,-6,2,-4,-2,-8,-2,-2,-7,-8,-4,-5,6,5,-10,4,6,5,-10,8,-10,4,9,4,-8,10,9,-10,-7,-8,5,-1,4,9,-6,7,-7,-8,6,-2,-4,6,-2,-8,-9,-8,-10,5,6,9,5,8,8,-8,-7,9,-5,-5,-3,-5,-1,9,5,-7,-10,-3,-2,-6,-8,-5,7,6,-2,10,-8,-8,-10,-2,2,6,-6,8,-3,-8,-1,5,10,-1,-6,8], dtype = "int64")#candidate|4955|(630,)|const|int64
const_4956 = relay.const([-5,-4,10,6,8,8,-10,2,-9,5,-2,-7,7,-3,-7,10,5,-9,-10,4,9,-7,2,-8,-4,-7,10,-3,-7,-2,7,8,-10,9,-4,-9,5,-1,-7,8,-6,10,-10,2,1,4,10,10,-9,-9,3,5,3,-7,-8,2,1,-7,6,8,5,-3,-6,-2,-5,-9,8,8,-1,-4,1,3,9,-3,-1,-10,5,-1,10,5,6,-4,9,10,9,8,-7,4,-3,10,-9,2,8,2,-9,-3,-2,-3,-3], dtype = "int32")#candidate|4956|(99,)|const|int32
call_4953 = relay.TupleGetItem(func_1898_call(relay.reshape(var_4954.astype('float64'), [2, 10, 3]), relay.reshape(const_4955.astype('int64'), [10, 63]), relay.reshape(const_4956.astype('int32'), [99,]), ), 5)
call_4957 = relay.TupleGetItem(func_1903_call(relay.reshape(var_4954.astype('float64'), [2, 10, 3]), relay.reshape(const_4955.astype('int64'), [10, 63]), relay.reshape(const_4956.astype('int32'), [99,]), ), 5)
func_1469_call = mod.get_global_var('func_1469')
func_1472_call = mutated_mod.get_global_var('func_1472')
call_4962 = relay.TupleGetItem(func_1469_call(relay.reshape(const_4956.astype('int32'), [1, 11, 9])), 3)
call_4963 = relay.TupleGetItem(func_1472_call(relay.reshape(const_4956.astype('int32'), [1, 11, 9])), 3)
output = relay.Tuple([bop_4939,call_4949,var_4950,call_4953,var_4954,const_4955,const_4956,call_4962,])
output2 = relay.Tuple([bop_4942,call_4951,var_4950,call_4957,var_4954,const_4955,const_4956,call_4963,])
func_4968 = relay.Function([var_4938,var_4950,var_4954,], output)
mod['func_4968'] = func_4968
mod = relay.transform.InferType()(mod)
mutated_mod['func_4968'] = func_4968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4968_call = mutated_mod.get_global_var('func_4968')
var_4970 = relay.var("var_4970", dtype = "float64", shape = (11, 12, 15))#candidate|4970|(11, 12, 15)|var|float64
var_4971 = relay.var("var_4971", dtype = "int64", shape = ())#candidate|4971|()|var|int64
var_4972 = relay.var("var_4972", dtype = "float64", shape = (30, 2))#candidate|4972|(30, 2)|var|float64
call_4969 = func_4968_call(var_4970,var_4971,var_4972,)
output = call_4969
func_4973 = relay.Function([var_4970,var_4971,var_4972,], output)
mutated_mod['func_4973'] = func_4973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4303_call = mod.get_global_var('func_4303')
func_4304_call = mutated_mod.get_global_var('func_4304')
call_4981 = relay.TupleGetItem(func_4303_call(), 0)
call_4982 = relay.TupleGetItem(func_4304_call(), 0)
func_1469_call = mod.get_global_var('func_1469')
func_1472_call = mutated_mod.get_global_var('func_1472')
const_4992 = relay.const([10,4,-2,3,-8,2,-4,7,-2,6,-5,1,10,-1,-6,8,4,5,-7,-9,5,-4,-2,9,-3,-2,-1,-4,3,-9,-10,8,10,-10,-2,-3,-10,5,9,-8,2,-3,-4,-3,2,9,2,-6,1,-1,-4,-9,1,-6,10,3,5,5,10,-6,2,6,3,6,7,8,-10,-4,2,9,4,-2,-7,8,-6,2,2,-10,10,-10,1,-6,6,4,-10,10,7,2,-10,1,-7,-2,3,-3,-7,-7,4,3,-5], dtype = "int32")#candidate|4992|(99,)|const|int32
call_4991 = relay.TupleGetItem(func_1469_call(relay.reshape(const_4992.astype('int32'), [1, 11, 9])), 2)
call_4993 = relay.TupleGetItem(func_1472_call(relay.reshape(const_4992.astype('int32'), [1, 11, 9])), 2)
var_4994 = relay.var("var_4994", dtype = "float32", shape = (12, 16, 11))#candidate|4994|(12, 16, 11)|var|float32
bop_4995 = relay.floor_divide(call_4981.astype('float32'), relay.reshape(var_4994.astype('float32'), relay.shape_of(call_4981))) # shape=(12, 16, 11)
bop_4998 = relay.floor_divide(call_4982.astype('float32'), relay.reshape(var_4994.astype('float32'), relay.shape_of(call_4982))) # shape=(12, 16, 11)
uop_5007 = relay.log(var_4994.astype('float64')) # shape=(12, 16, 11)
output = relay.Tuple([call_4991,const_4992,bop_4995,uop_5007,])
output2 = relay.Tuple([call_4993,const_4992,bop_4998,uop_5007,])
func_5022 = relay.Function([var_4994,], output)
mod['func_5022'] = func_5022
mod = relay.transform.InferType()(mod)
var_5023 = relay.var("var_5023", dtype = "float32", shape = (12, 16, 11))#candidate|5023|(12, 16, 11)|var|float32
output = func_5022(var_5023)
func_5024 = relay.Function([var_5023], output)
mutated_mod['func_5024'] = func_5024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4573_call = mod.get_global_var('func_4573')
func_4575_call = mutated_mod.get_global_var('func_4575')
call_5037 = relay.TupleGetItem(func_4573_call(), 1)
call_5038 = relay.TupleGetItem(func_4575_call(), 1)
output = relay.Tuple([call_5037,])
output2 = relay.Tuple([call_5038,])
func_5043 = relay.Function([], output)
mod['func_5043'] = func_5043
mod = relay.transform.InferType()(mod)
output = func_5043()
func_5044 = relay.Function([], output)
mutated_mod['func_5044'] = func_5044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_5110 = func_4070_call()
call_5111 = func_4070_call()
output = relay.Tuple([call_5110,])
output2 = relay.Tuple([call_5111,])
func_5168 = relay.Function([], output)
mod['func_5168'] = func_5168
mod = relay.transform.InferType()(mod)
output = func_5168()
func_5169 = relay.Function([], output)
mutated_mod['func_5169'] = func_5169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_5192 = func_4070_call()
call_5193 = func_4070_call()
output = call_5192
output2 = call_5193
func_5206 = relay.Function([], output)
mod['func_5206'] = func_5206
mod = relay.transform.InferType()(mod)
mutated_mod['func_5206'] = func_5206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5206_call = mutated_mod.get_global_var('func_5206')
call_5207 = func_5206_call()
output = call_5207
func_5208 = relay.Function([], output)
mutated_mod['func_5208'] = func_5208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mod.get_global_var('func_4149')
func_4151_call = mutated_mod.get_global_var('func_4151')
call_5233 = func_4149_call()
call_5234 = func_4149_call()
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_5250 = func_4070_call()
call_5251 = func_4070_call()
output = relay.Tuple([call_5233,call_5250,])
output2 = relay.Tuple([call_5234,call_5251,])
func_5280 = relay.Function([], output)
mod['func_5280'] = func_5280
mod = relay.transform.InferType()(mod)
output = func_5280()
func_5281 = relay.Function([], output)
mutated_mod['func_5281'] = func_5281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_5290 = relay.TupleGetItem(func_3714_call(), 0)
call_5291 = relay.TupleGetItem(func_3716_call(), 0)
output = call_5290
output2 = call_5291
func_5295 = relay.Function([], output)
mod['func_5295'] = func_5295
mod = relay.transform.InferType()(mod)
output = func_5295()
func_5296 = relay.Function([], output)
mutated_mod['func_5296'] = func_5296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4027_call = mod.get_global_var('func_4027')
func_4028_call = mutated_mod.get_global_var('func_4028')
call_5297 = func_4027_call()
call_5298 = func_4027_call()
func_2402_call = mod.get_global_var('func_2402')
func_2405_call = mutated_mod.get_global_var('func_2405')
var_5321 = relay.var("var_5321", dtype = "float64", shape = (4, 12))#candidate|5321|(4, 12)|var|float64
const_5322 = relay.const([-3,-9,1,9,-5,9,7,10,-9,-4,-6,-7,7,9,-1,-3,3,9,-4,-1,5,6,5,9,-4,5,8,-10,1,-6,10,-9,1,-7,6,-5,-8,-2,5,-9,6,1,-5,9,-10,10,-2,5,7,-8,1,-4,4,-4,-7,10,-6,-9,1,8,-1,-1,7,6,-7,-7,-10,7,-6,3,-3,-1,1,9,8,-3,-6,-1,2,5,4,8,-2,7,6,-5,10,-8,-6,5,4,2,-4,-1,10,6,9,-7,-8,10,4,-7,-1,-5,1,10,8,5,5,-8,3,9,7,4,-2,-1,10,-9,2,2,6,9,6,-7,4,-5,9,-9,-2,2,-7,-8,-3,-2,5,-8,-5,-8,-5,-1,-10,5,2,8,9,8,4,-5,-5,4,2,-2,1,10,-4,-4,-7,8,5,3,-5,-1,7,8,4,3,-3,3,-6,3,-5,-8,8,-2,-1,8,-6,-5,-7,-6,-6,-7,3,-5,4,-10,-7,-1,-2,9,-10,9,7,8,8,3,2,-3,1,-5,-7,1,-1,10,-5,-9,5,-10,4,6,-1,-8,-8,-7,10,-1,-5,3,-7,1,2,-9,-8,1,7,5,-6,-1,3,-3,-10,-2,-1,2,9,-9,5,-10,-7,6,8,-3,4,9,4,2,8,-10,10,6,7,-2,3,7,5,-5,-5,-9,4,6,-4,1,-2,-1,-3,4,2,4,8,-9,-3,9,-5,-8,-8,7,3,-4,-9,9,-3,3,9,-3,9,3,8,-1,-10,-2,-5,2,6,-5,2,8,1,9,1,8,-5,1,4,-6,2,5,-4,-5,3,-7,8,-8,-9,8,10,9,8,1,-5,-6,-3,-4,6,-9,-1,-3,4,-7,-8,-4,-10,6,-4,-10,1,5,5,-3,9,1,8,9,3,6,1,-2,2,9,-4,-6,4,-1,1,1,5,1,4,-7,8,-8,3,1,7,-3,8,-8,-3,1,-2,-5,2,10,8,3,-1,6,-1,9,-9,-9,-4,-9,-5,-10,-5,-1,10,5,9,7,-10,-3,-2,-1,5,-7,-6,-5,-1,7,9,-4,-1,1,6,-1,-1,-9,7,5,9,-2,-10,-7,1,6,-4,-8,-9,5,5,4,-2,-2,-3,2,8,-1,10,-9,2,8,-6,-10,-5,10,3,-9,-7,4,7,5,10,4,-2,1,-8,1,-7,-7,-6,-6,1,3,-6,1,3,-9,-10,4,-5,7,8,-7,8,9,3,2,1,-3,2,-10,-7,-9,3,-10,-2,4,-6,-5,5,8,-9,1,6,7,-7,3,8,-3,-7,1,-2,9,4,-2,-8,-8,-3,-9,2,-6,-4,4,-3,5,2,1,-1,-3,6,5,-8,-3,1,-9,-9,-5,-6,-7,8,10,7,5,4,4,-5,-4,-1,7,10,-6,-1,-1,10,5,-9,-9,6,8,-3,-10,1,-5,-10,6,-6,-6,-3,-5,7,2,-5,-6,-6,1,-5,8,-4,8,-5,1,-9,10,7,7,-5,2,2,1,10,-7,-4,3,-10,-1,7,8,-2,-8,-6,-3,-5,-3,2,-7,7,-9,1,-10,-3,5,2,6,4,2,-8,-10,-1,2,-6,-4,-4,-7,-5,7,-7,-9,-8,4,-8,1,-3,-1,-4,6,5,-7,6,-6,-9,10,5,-5,-4,-4,-7,-10,-6,5], dtype = "int64")#candidate|5322|(630,)|const|int64
call_5320 = relay.TupleGetItem(func_2402_call(relay.reshape(var_5321.astype('float64'), [3, 1, 16]), relay.reshape(const_5322.astype('int64'), [630,]), ), 2)
call_5323 = relay.TupleGetItem(func_2405_call(relay.reshape(var_5321.astype('float64'), [3, 1, 16]), relay.reshape(const_5322.astype('int64'), [630,]), ), 2)
func_4273_call = mod.get_global_var('func_4273')
func_4278_call = mutated_mod.get_global_var('func_4278')
const_5325 = relay.const([-9,8,2,-10,-8,2,-4,7,-10,8,-7,7,-10,10,-5,-5,-1,-6,6,8,7,-8,-4,-8,5,-8,10,-10,6,4,-1,4,5,-3,-7,7,-4,-4,7,5,-10,4,-8,-10,6,-4,4,-7,9,10,-2,8,9,4,-4,7,2,5,8,2,1,1,3,2,9,-8,6,-8,-7,-2,1,-6,3,-3,-9,6,-1,3,6,-8,7,9,3,10,-10,-3,-4,-6,-2,-9,-5,9,2,2,9,-5,5,10,9,-7,6,2,1,-8,-8,-4,-4,9,-6,3,10,-10,2,-2,-3,10,1,9,1,-4,4,3,2,-3,-4,4,4,10,5,7,-3,5,-10,-7,-2,3,9,-4,-10,9,-5,10,6,-5,2,-9,10,8,-8,4,-5,6,5,-7,8,10,9,-3,8,6,-2,4,10,-4,6,-8,7,7,5,6,7,7,4,3,-9,-1,-3,-3,-6,1,6,-2,-3,-2,10,2,-4,5,10,-9,6,-8,-4,4,-9,-3,-6,8,4,10,10,5,-2,1,8,-8,1,-7,-8,-6,-8,4,3,-3,-1,-3,6,4,-8,-7,6,-5,3,3,-3,-2,9,-4,7,-1,2,-9,4,6,8,-10,-3,1,-7,9,5,-2,7,-9,5,3,6,8,7,1,1,2,-6,-10,-9,-4,10,9,2,-2,-9,-6,6,4,2,-9,-9,-7,-3,-10,7,7,10,5,-5,10,-9,-1,-2,8,-10,-7,7,-4,2,-3,7,-6,-7,10,-7,7,9,-3,-5,-5,2,-4,7,-1,5,5,5,1,-2,7,-3,7,4,-5,5,-4,3,5,-9,6,-2,5,2,-1,-9,4,-5,-6,-3,6,2,-2,-9,4,5,1,10,-7,2,-7,-8,-4,5,10,10,5,-7,8,6,-5,9,8,-9,-4,-3,-1,3,2,5,6,-1,1,10,5,9,-6,-5,10,9,7,4,-3,-5,-6,8,-10,-5,-8,-10,10,4,-8,2,6,-3,-3,3,5,-2,2,7,2,5,-8,4,2,5,10,-9,9,9,8,-10,4,8,-6,10,-8,8,7,3,2,1,-5,6,4,-8,9,-7,-1,-9,-1,-5,-3,4,-4,9,-7,6,3,-8,9,-1,-5,1,5,-5,10,-7,2,1,10,-10,4,-9,-9,-6,-2,-7,5,-2,-10,7,6,3,7,4,5,4,-1,6,9,-8,-9,7,5,-4,-4,-6,-7,8,2,9,5,9,-8,6,9,8,9,1,3,-8,8,-9,3,-7,9,-4,-1,10,10,-7,-10,-8,-8,-10,4,-10,-1,7,8,1,-2,-4,10,4,-2,10,6,10,8,-7,-9,7,7,6,-8,3,-1,-6,-2,2,9,-3,-3,9,4,-4,-4,-5,-4,8,-7,3,7,1,-10,-3,-9,4,-1,3,-10,8,-7,6,-3,5,-5,-8,-10,2,-5,8,3,-8,-8,10,8,-1,9,8,2,-2,4,9,-10,-5,-8,-1,-7,-3,-7,-3,1,2,3,-3,-7,-10,-4,6,-2,1,4,-8,8,-7,4,-4,6,-6,7,-4,4,-7,4,2,-4,3,4,10,5,-9,-9,-6,10,-6,1,3,-7,-4,4,9,9,-6,5,7,7,-1,-10,3,-10,6,10,-9,-10,10,-8,-1,-2,2,-7,7,6,8,6,-3,-10,-10,-8,9,-1,-1,-9,8,1,7,10,10,4,1,1,8,4,-4,-6,-2,6,-4,6,-4,-3,-3,-9,-10,-2,4,-4,7,-10,-10,-5,-1,-6,4,10,-8,-1,7,-7,2,7,-3,8,-1,-10,-5,5,-6,5,-4,-7,8,-5,-9,-2,-4,-9,-2,-6,5,3,-10,8,-9,5,-7,-6,-4,8,5,-4,-10,5,-10,-4,6,-9,-6,-4,1,10,2,1,-9,9,2,5,8,2,1,-7,3,-5,2,-6,7,-10,-2,-6,3,-4,-1,-5,-9,7,4,8,9,-8,3,5,-10,10,8,-4,3,6,-9,3,1,-7,-3,4,-8,-2,-8,10,3,-1,-8,-4,3,5,2,-9,7,7,10,-3,-6,9,3,4,-9,-7,-2,-8,-10,6,-10,-4,-2,10,-4,10,7,4,9,3,4,3,-2,10,5,-3,-2,3,-8,6,5,2,7,9,3,-2,-4,3,-7,8,-9,-6,-8,7,-3,7,-10,9,4,-3,-1,-4,-3,3,-9,3,-3,-1,9,8,2,1,4,-1,-7,-7,-1,-3,7,-4,6,6,-8,10,-6,1,-6,10,-2,10,5,-8,-6,1,-9,-2,4,-4,-5,-10,-5,-9,-5,10,-9,-9,-6,1,9,9,-10,-3,-9,9,-3,6,-1,-10,-3,-4,-1,-7,9,10,1,-6,-10,-7,7,-4,-4,10,-5,-2,1,1,8,-8,5,6,9,8,2,2,-3,10,7,5,-10,-2,-2,10,8,-8,8,-10,-6,10,-6,-7,-9,10,-5,-9,1,-6,2,-4,6,5,6,2,-4,1,-5,2,-3,1,7,-5,-1,3,6,8,-1,-7,8,10,2,-3,8,-2,-8,-3,2,5,-8,1,-8,-8,-9,6,6,1,-5,-6,10,6,-8,-4,6,4,-8,9,-3,4,4,1,-6,-8,7,-8,2,6,2,10,9,-3,10,-6,-3,-5,2,8,8,-1,-2,1,-2,3,9,5,9,7,-3,10,-5,4,-1,-5,10,4,-6,5,-2,-3,2,-8,-7,-8,-10,-6,-5,10,5,-7,-3,7,5,-9,-10,9,2,3,-4,10,1,-9,-10,-6,-6,10,-3,-1,8,-7,-4,-2,-6,6,10,-4,-3,9,1,8,8,1,4,-2,-3,5,-7,-4,6,3,-7,6,9,5,1,-9,3,10,3,-4,-1,4,7,-1,9,6,-10,-9,-8,-8,10,-5,9,-2,7,9,-2,6,-2,-2,-10,8,-1,-8,3,-7,7,-6,7,-1,2,2,4,5,6,8,8,-5,-4,7,3,10,5,-8,-4,9,-8,1,-1,-7,-6,5,2,-2,-5,2,4,-7,8,3,4,-7,7,6,4,6,-10,-5,-1,7,-9,-5,2,2,-9,9,9,8,4,3,-7,2,-10,-10,-6,-6,-7,-8,4,7,6,-7,-6,2,-6,9,-6,3,-10,6,9,2,4,4,-1,9,1,-4,-10,-6,-1,-2,-6,2,7,1,-1,-3,-3,3,10,-1,10,5,-2,-8,5,-10,6,-8,-10,-10,-4,-6,-2,2,4,10,-1,-6,5,5,-4,3,-5,-3,-2,5,-8,4,3,9,-1,3,-5,6,3,-1,4,-6,-7,-5,-6,6,3,-3,7,-6,-10,-2,-8,-4,-8,9,-1,5,6,8,2,5,3,4,9,-8,-8,3,-7,-6,-3,10,-10,1,-7,-9,2,-6,1,5,-1,6,-3,3,7,8,-4,4,-3,1,6,1,-3,3,9,1,-2,9,-7,7,4,6,4,-2,-6,9,3,2,-8,-8,-4,7,8,-3,-10,1,-6,10,8,8,-4,-8,8,-3,-4,3,1,-5,-8,6,-9,-10,5,-2,3,-8,7,-6,-7,-1,-3,10,6,3,-4,-2,7,5,-3,8,8,-4,4,-10,-10,-2,7,7,7,-9,-10,-3,4,-2,8,-4,-7,-1,-10,-2,4,-5,5,-6,3,-5,-6,-1,-10,-9,4,5,4,2,9,-6,5,-5,1,-5,5,-7,-10,-3,-5,7,8,3,-7,5,7,10,3,4,-7,8,9,-4,8,-9,2,4,-9,-1,2,-4,-9,2,-10,-6,5,10,3,-5,1,-6,2,-2,-9,-1,1,9,-10,2,9,-8,3,-10,-1,-7,-1,-7,5,5,-6,-2,-2,9,-3,-3,-8,-9,-10,-7,-4,-5,-7,9,4,3,-10,7,9,-5,6,5,10,4,2,1,4,-2,-8,3,7,-2,-3,1,6,4,-6,5,-2,-8,-10,2,-4,-9,7,6,7,3,8,2,3,-7,5,-7,-3,-3,5,-1,2,-3,9,3,7,6,3,1,-1,5,10,-3,6,-6,-1,-1,-6,-2,-4,-10,2,-8,3,-10,-8,2,-6,9,-1,4,3,-5,-10,3,-1,-6], dtype = "int16")#candidate|5325|(1540,)|const|int16
call_5324 = relay.TupleGetItem(func_4273_call(relay.reshape(call_5297.astype('float64'), [11, 12, 15]), relay.reshape(call_5297.astype('float64'), [11, 12, 15]), relay.reshape(const_5325.astype('int16'), [1540,]), ), 0)
call_5326 = relay.TupleGetItem(func_4278_call(relay.reshape(call_5297.astype('float64'), [11, 12, 15]), relay.reshape(call_5297.astype('float64'), [11, 12, 15]), relay.reshape(const_5325.astype('int16'), [1540,]), ), 0)
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_5331 = func_4070_call()
call_5332 = func_4070_call()
func_3853_call = mod.get_global_var('func_3853')
func_3855_call = mutated_mod.get_global_var('func_3855')
call_5333 = func_3853_call()
call_5334 = func_3853_call()
output = relay.Tuple([call_5297,call_5320,var_5321,const_5322,call_5324,const_5325,call_5331,call_5333,])
output2 = relay.Tuple([call_5298,call_5323,var_5321,const_5322,call_5326,const_5325,call_5332,call_5334,])
func_5335 = relay.Function([var_5321,], output)
mod['func_5335'] = func_5335
mod = relay.transform.InferType()(mod)
mutated_mod['func_5335'] = func_5335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5336 = relay.var("var_5336", dtype = "float64", shape = (4, 12))#candidate|5336|(4, 12)|var|float64
func_5335_call = mutated_mod.get_global_var('func_5335')
call_5337 = func_5335_call(var_5336)
output = call_5337
func_5338 = relay.Function([var_5336], output)
mutated_mod['func_5338'] = func_5338
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5342 = relay.const([[[-5,9,-10,-9,-2,-10,4,-1,9,2,-4,-2,1],[-3,9,8,-8,-5,3,-5,2,9,3,8,-5,3],[-1,-8,-10,-5,-6,2,-10,-4,2,10,-7,9,9],[3,-10,-3,-3,3,1,-4,-1,-3,-5,7,-8,-1],[-8,-4,8,2,4,-8,6,4,-9,6,-7,4,6],[9,-8,9,-9,-2,-10,4,10,5,-5,-5,7,6],[-2,4,-2,2,-3,6,3,8,4,9,8,-4,-1],[9,2,-2,8,2,10,9,-6,5,7,-3,9,-7],[-6,-10,-9,4,6,6,3,3,-2,5,1,7,3],[-9,2,9,-8,-4,2,10,6,-4,-4,10,-1,-3],[-7,10,-8,4,6,9,-4,3,-3,-4,9,-7,4],[8,-4,-10,1,1,-9,-1,-8,-1,7,8,8,-10],[9,1,-9,-1,-10,-4,-8,-2,1,6,-6,-4,10],[3,-4,-5,2,-8,-7,-4,9,9,4,-6,5,-6],[8,3,2,8,-9,-8,-10,-2,5,-5,-3,-2,4]],[[-3,2,1,9,-10,10,-6,-4,1,-3,1,8,-4],[10,9,-8,4,-4,-1,-1,-4,10,1,8,-8,-7],[-1,-6,-10,-3,-4,-1,-2,-5,10,4,6,-5,10],[1,4,-10,6,2,-4,-3,7,-7,3,-9,-8,6],[-1,-3,2,-8,3,-1,-3,3,7,8,-3,2,8],[8,6,-2,-3,-7,-8,-3,-4,9,9,-7,-9,-2],[-9,-8,-6,3,-10,-9,9,-10,-3,-7,9,-4,-8],[-7,-5,1,1,-1,6,1,10,-9,-7,7,1,-7],[-9,-1,10,-6,-4,9,8,4,-7,-2,-6,5,9],[3,7,2,-1,-5,-10,-5,9,10,7,3,-9,-10],[-5,8,8,-6,1,1,1,-2,10,-5,-5,-8,9],[6,-6,2,-1,5,-4,-2,-9,7,-2,2,10,3],[-4,-8,2,-10,-8,10,-5,-9,-8,-3,8,8,1],[-2,-1,6,7,6,-8,10,1,7,6,4,-9,-10],[9,6,2,-2,-2,6,-4,9,-1,2,-8,9,-7]],[[8,1,2,6,1,6,10,-4,7,1,4,6,5],[6,-8,6,-8,3,-9,8,8,-5,-1,-5,7,-6],[-7,6,6,5,-5,-1,-9,5,-5,8,-6,-2,-2],[-7,10,-1,-6,8,-8,-8,-5,6,-5,-2,3,-6],[4,7,-4,4,-10,2,1,9,-2,-2,8,-10,8],[-3,-3,9,-6,1,1,-3,-4,8,-6,7,-6,4],[-7,-6,6,6,-8,-5,1,4,5,4,4,-5,1],[-8,-2,-10,5,-6,5,10,-6,8,3,1,1,7],[1,6,5,8,6,-6,4,-2,3,2,7,7,4],[-7,-7,-10,8,10,-10,9,-8,7,-7,1,-2,-9],[5,-8,6,-1,2,9,7,-3,8,5,9,8,-2],[5,-3,5,-10,6,2,9,9,6,-7,-7,3,3],[-3,-9,3,2,-10,-4,10,8,-7,6,5,4,-10],[-1,2,-8,-8,-3,-5,-4,2,5,8,-5,-10,-1],[-2,-9,7,-9,5,-7,6,-1,-4,4,-5,-9,-4]],[[-9,5,1,8,-2,-3,5,10,-10,-1,5,-8,-3],[-10,7,5,10,8,9,-5,-9,4,6,-8,-8,7],[-6,2,9,4,-8,4,10,3,-5,2,7,-10,2],[9,-8,-5,3,-8,1,-10,10,1,3,-9,2,-2],[9,-2,-1,1,7,-6,5,-3,-3,-7,5,4,2],[6,-7,3,-10,7,7,-3,-5,-5,10,-7,10,-7],[-10,5,-6,-5,9,9,4,3,7,6,-2,2,-10],[8,-1,-9,5,4,-4,4,-1,-5,2,-6,3,-1],[-4,8,10,-6,-10,-3,-8,8,-7,5,5,3,-7],[6,-5,-4,8,5,-9,-8,-5,-6,9,2,4,4],[-7,-9,-7,4,-10,3,2,7,-6,-10,7,3,-10],[3,-4,5,3,-8,7,-4,-10,-6,-2,4,9,2],[-10,1,2,3,-1,1,-2,-8,-1,-7,-9,5,-7],[3,3,-1,10,2,-6,-2,-1,2,-2,-4,3,5],[-6,5,-7,7,-4,2,10,8,7,4,-2,3,7]],[[6,9,-1,-10,-6,7,-7,-4,6,3,2,5,9],[-4,-1,10,-10,9,-3,10,-7,5,-5,-3,4,7],[5,4,7,-8,9,-6,-6,10,5,1,6,-8,-6],[2,-8,-8,10,8,-9,6,4,-7,-10,-2,-9,-8],[8,6,8,5,-6,10,-4,3,-5,-3,4,9,-9],[8,-1,-10,4,-4,3,-10,-2,-7,1,4,-1,-2],[9,9,-2,5,-7,4,-3,6,8,9,8,-8,7],[4,-9,5,8,5,2,5,6,-1,-10,7,4,-7],[3,1,7,8,-2,3,8,3,-9,9,10,6,-6],[-7,10,-5,1,-1,-1,-4,3,-6,7,-8,6,2],[9,5,1,-6,-7,-2,-6,7,-3,2,-8,6,6],[10,3,-9,9,8,7,3,-6,2,-9,1,10,9],[-2,3,-8,3,6,4,7,9,7,-9,6,-4,2],[8,-9,-10,-9,10,-10,1,-6,-5,-6,-10,-6,-5],[-2,-7,4,-6,2,5,-3,-1,9,-8,6,7,-8]],[[6,-8,6,7,4,-1,-6,10,-6,-8,5,8,2],[7,-7,-8,6,-3,-6,8,-4,2,-1,1,5,-4],[-5,-4,-8,6,-5,-10,10,5,-6,6,1,-9,-4],[10,10,-2,8,-1,6,-4,6,5,-9,-2,3,-2],[7,7,-2,3,-10,-6,-10,5,-8,8,-4,8,3],[-6,-9,1,2,9,6,5,-4,4,-9,9,-9,1],[-10,-7,-10,-9,3,-5,7,-8,-6,9,-3,-4,-6],[-10,-4,10,-2,6,2,-3,5,-2,1,-5,3,7],[-9,-10,7,-9,3,-4,-8,8,-6,-7,-8,3,-8],[-6,-4,-9,-7,-7,-9,5,6,8,2,4,-7,-8],[1,-6,-2,2,-7,-1,9,9,4,1,-5,-6,7],[2,-10,-8,-6,9,-7,5,3,-8,-2,4,1,8],[4,-1,-1,-4,-7,-3,9,10,7,9,1,-4,-6],[-9,-4,3,10,-1,-10,3,9,10,-1,3,-8,-10],[2,2,-10,5,9,-4,-5,-9,9,-4,-1,6,7]],[[-2,2,3,-5,1,7,1,-7,4,-9,-7,-6,-7],[-5,1,-10,6,6,-7,-6,6,6,9,2,5,8],[-10,-3,3,7,10,8,1,-7,5,-7,-5,10,-8],[9,4,7,2,-8,-10,9,-4,5,-3,4,-6,-10],[-7,6,1,-1,3,-8,10,9,2,-9,7,4,8],[7,-2,-6,-5,4,-10,-4,7,-9,7,6,-8,-8],[10,-4,-9,-2,-7,-9,1,-2,-10,-3,6,3,-9],[-5,-5,1,-4,-4,7,-5,4,-9,-7,5,7,4],[9,-9,8,5,-8,9,-3,-4,-10,-5,2,9,-4],[9,-4,7,2,-4,-1,-4,-7,-10,7,-1,4,1],[-1,-5,7,-8,-7,-6,10,-1,-1,9,-7,10,-4],[1,8,-4,-4,-6,3,4,7,-10,2,-10,-6,2],[-10,9,5,2,2,4,4,-7,-4,-8,-4,1,-2],[10,-2,3,-7,7,-2,7,2,-10,-3,-3,1,-9],[-10,1,-1,-9,-5,6,5,-6,-10,-1,-6,1,9]],[[6,5,-2,-6,-8,6,-10,2,-5,-7,1,3,2],[-2,-7,-8,10,-8,10,-7,-1,-10,4,-6,8,-9],[3,-3,-1,9,-10,3,-2,-4,5,3,-4,6,6],[6,-9,6,-7,8,-8,8,-6,7,1,10,-1,-1],[-7,-5,-3,10,-6,-4,5,-2,1,-10,2,2,-7],[1,-7,-4,-3,9,10,8,6,-10,3,6,4,10],[-1,1,-7,7,5,10,10,4,1,-7,-3,9,-9],[-2,1,8,8,-10,-10,-3,-8,-4,4,-10,9,1],[-2,-2,7,3,9,10,1,-4,-6,-7,-10,5,-9],[9,4,-4,2,9,-9,7,-6,-5,4,-7,6,7],[4,-10,-10,-5,-8,-1,4,-10,-4,10,2,4,-5],[-8,-6,-1,-10,-5,9,-3,8,9,-5,4,-8,9],[10,-7,6,-9,4,-5,10,-3,10,8,-1,2,10],[7,-2,7,2,8,3,2,-5,2,-7,-4,2,-8],[1,-10,8,6,-6,2,8,9,5,-9,-8,-4,5]],[[-3,10,-9,-1,-1,-8,7,-1,-3,-6,2,-4,2],[3,9,3,-6,-3,-3,6,3,10,-10,-10,-2,3],[-10,7,1,7,10,1,-5,1,-9,2,2,4,7],[-3,2,4,-5,5,3,-5,6,-6,-10,-8,5,3],[-6,-9,2,-1,-10,-10,6,-2,-9,-1,-2,-3,6],[-1,3,-10,2,-1,1,-3,-7,-9,-8,3,7,2],[2,2,-7,1,-9,-1,10,7,2,-4,5,-3,4],[10,-9,-1,-8,-1,5,8,-2,-5,9,-4,4,-1],[1,1,1,7,4,2,-10,-8,4,-9,3,9,-5],[-6,-2,5,-2,-9,8,4,5,-5,-1,-1,8,-3],[1,-4,6,-5,-8,4,-7,-2,10,-8,-4,-1,5],[-1,-10,-6,8,-9,-2,5,-5,10,1,-8,10,7],[10,-10,-9,-7,-7,2,-3,-2,-5,4,5,1,-6],[10,-6,1,-6,-10,3,-8,10,-6,2,9,6,-7],[-5,-8,9,6,-6,1,9,-8,9,-3,-5,4,-8]],[[5,4,4,2,2,-1,-9,7,-8,1,9,4,-3],[-2,6,-9,1,-5,-5,-8,-10,-5,-5,-9,1,2],[2,-3,-5,-1,6,-4,-5,1,-7,9,9,6,-10],[-8,5,-10,-6,-1,1,-1,-3,-3,5,-2,-4,-10],[7,-6,1,8,6,2,-3,10,-6,-1,8,-9,8],[5,-2,-3,-3,6,5,-9,-1,10,3,-10,-2,9],[-4,5,10,2,-7,3,-5,5,2,-10,2,-1,-1],[5,3,-5,2,7,-10,-4,-5,8,-5,-10,4,3],[10,-4,-6,-6,2,-4,-1,-4,1,7,-4,-5,-7],[-7,-7,-10,4,-7,10,-9,-7,7,-3,9,9,-9],[-3,2,-1,5,-9,2,7,-6,-5,1,8,-9,7],[5,6,-8,10,10,-1,7,8,-3,-1,3,-4,9],[2,-2,-8,6,-1,-4,8,-2,9,-9,9,3,1],[-9,2,-6,9,-5,5,2,10,8,-10,-5,8,-7],[5,10,-7,2,8,-6,-6,-4,6,6,2,2,-4]],[[4,-2,-10,10,-7,-10,8,9,-5,-7,-5,-6,9],[-4,-3,-9,-10,-7,-9,4,-6,5,2,-10,-8,-7],[9,5,-5,-8,-7,3,-9,-2,7,-6,-10,-9,-6],[3,-3,8,-6,-10,2,-9,-5,8,5,4,-8,7],[1,2,2,-1,6,8,2,4,6,-3,-6,-6,-3],[-2,-9,8,-4,5,-6,2,-8,5,-10,2,-2,8],[-7,8,-3,10,-1,9,-1,-3,5,-2,-10,10,7],[6,10,7,8,-7,8,-2,8,-6,10,-7,-7,-5],[-7,6,1,-3,-8,6,8,9,-3,-6,-4,1,4],[-8,-8,-7,-10,-10,9,-1,6,4,-3,1,-4,8],[-9,-2,8,3,3,-4,7,5,9,-2,5,10,-9],[-7,-8,-2,5,-10,-6,-2,5,5,10,-5,-7,-6],[2,-2,5,-7,4,9,-5,-4,-2,-1,2,8,-5],[-3,-1,-5,-2,-8,-6,-1,-4,10,7,-2,10,-7],[-1,-6,-7,1,5,3,-4,-6,3,1,-8,-7,-8]],[[-6,-4,3,-6,-2,-6,-1,8,10,-4,-2,-6,4],[-7,8,4,4,-5,-3,-3,-5,9,-2,1,-1,-2],[2,8,-3,9,-10,5,10,10,2,8,4,5,-4],[-10,9,-8,2,-9,2,-6,2,6,-3,5,10,3],[3,-10,4,4,5,-6,-7,-4,2,1,1,-6,-4],[2,-4,-5,-4,-4,6,2,9,10,1,-6,2,-7],[-7,-9,-1,2,-7,4,6,8,7,5,7,3,7],[-1,1,4,-10,-6,8,-8,-8,4,10,6,-3,-3],[-4,8,-8,-2,6,6,3,-7,-1,-3,7,1,-3],[-5,7,7,-4,5,-4,2,5,8,-9,8,-9,-7],[2,4,-6,-10,-4,-6,-1,-4,-10,-7,-6,4,9],[5,2,-4,1,-10,4,-2,6,-1,-3,-4,-1,9],[-3,3,2,7,10,-10,9,10,9,-4,-3,4,9],[-8,-6,-8,-7,-8,-8,5,-8,1,-5,3,-4,-7],[-1,5,-8,10,10,-10,8,-10,-4,-4,-9,2,-5]],[[-6,-3,10,-5,-3,7,-4,1,6,3,-6,10,-3],[-7,3,-1,3,-5,7,-5,2,2,-1,-1,4,4],[4,2,-4,-2,10,-7,7,-5,1,-3,-4,-10,-9],[1,-6,-3,-8,8,1,9,3,-4,8,-3,9,-4],[2,-9,5,-4,4,3,-2,6,-1,7,-2,4,-10],[1,-2,4,8,-5,-3,6,-6,-1,-10,-4,-3,6],[-1,5,5,1,-8,-1,8,9,-5,-1,4,9,-1],[6,3,-9,-10,6,-8,-5,3,3,4,-5,9,-1],[-9,6,5,-6,-3,3,-7,1,7,4,-3,-9,2],[-7,-9,-1,-1,10,10,4,-9,1,7,5,-9,2],[-7,1,7,8,6,-4,-10,-3,-10,-8,-6,-7,8],[-9,-1,10,-3,9,9,-8,1,-4,-6,-3,-5,-5],[7,-6,-4,-3,5,6,4,-2,5,8,1,6,8],[-4,-10,4,3,-4,6,-3,-1,-2,6,-8,1,-8],[-9,-10,6,1,-2,-5,6,1,9,4,-7,-4,8]]], dtype = "uint64")#candidate|5342|(13, 15, 13)|const|uint64
var_5343 = relay.var("var_5343", dtype = "uint64", shape = (13, 15, 13))#candidate|5343|(13, 15, 13)|var|uint64
bop_5344 = relay.bitwise_and(const_5342.astype('uint64'), relay.reshape(var_5343.astype('uint64'), relay.shape_of(const_5342))) # shape=(13, 15, 13)
func_4461_call = mod.get_global_var('func_4461')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_5356 = relay.TupleGetItem(func_4461_call(), 0)
call_5357 = relay.TupleGetItem(func_4462_call(), 0)
output = relay.Tuple([bop_5344,call_5356,])
output2 = relay.Tuple([bop_5344,call_5357,])
func_5358 = relay.Function([var_5343,], output)
mod['func_5358'] = func_5358
mod = relay.transform.InferType()(mod)
mutated_mod['func_5358'] = func_5358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5359 = relay.var("var_5359", dtype = "uint64", shape = (13, 15, 13))#candidate|5359|(13, 15, 13)|var|uint64
func_5358_call = mutated_mod.get_global_var('func_5358')
call_5360 = func_5358_call(var_5359)
output = call_5360
func_5361 = relay.Function([var_5359], output)
mutated_mod['func_5361'] = func_5361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_5401 = func_3765_call()
call_5402 = func_3765_call()
output = relay.Tuple([call_5401,])
output2 = relay.Tuple([call_5402,])
func_5405 = relay.Function([], output)
mod['func_5405'] = func_5405
mod = relay.transform.InferType()(mod)
mutated_mod['func_5405'] = func_5405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5405_call = mutated_mod.get_global_var('func_5405')
call_5406 = func_5405_call()
output = call_5406
func_5407 = relay.Function([], output)
mutated_mod['func_5407'] = func_5407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_5416 = func_3765_call()
call_5417 = func_3765_call()
func_2402_call = mod.get_global_var('func_2402')
func_2405_call = mutated_mod.get_global_var('func_2405')
var_5419 = relay.var("var_5419", dtype = "float64", shape = (48,))#candidate|5419|(48,)|var|float64
const_5420 = relay.const([[-4,-9,-1],[-8,-1,-1],[8,8,-9],[7,3,3],[1,8,7],[-5,6,-10],[9,4,-2],[2,8,7],[5,1,5],[9,-10,-10],[-4,10,9],[9,-7,-5],[-7,-10,-9],[2,-2,1],[-1,-5,-7],[7,-8,-3],[6,-4,-2],[-3,-7,4],[9,9,-3],[1,1,4],[-9,-1,-8],[5,-6,-9],[9,9,-3],[2,-1,5],[3,7,-10],[-4,-1,-9],[1,5,4],[-8,-3,8],[2,-10,-3],[8,-1,-10],[7,1,8],[9,5,-7],[-5,1,-3],[-8,9,1],[-4,-7,-5],[5,10,-10],[-7,8,-2],[-8,-9,6],[8,-9,1],[10,-9,10],[6,6,3],[-2,6,10],[-4,-6,9],[-7,6,-3],[-3,4,-2],[8,2,-3],[1,-5,5],[4,6,-4],[-1,-10,-6],[6,10,3],[-4,1,4],[-9,9,-1],[-9,-8,4],[10,3,-2],[4,10,8],[7,4,-6],[-2,-5,-10],[7,-1,4],[7,1,-3],[8,-1,-3],[-2,8,8],[6,10,-1],[8,-2,3],[4,-2,-7],[-10,-4,3],[-9,-8,5],[-3,-8,-4],[7,-6,-1],[-5,-6,-2],[1,10,-2],[-3,-2,-7],[8,7,7],[4,-1,1],[7,9,-2],[-6,2,8],[-1,-4,-3],[7,3,7],[5,-3,2],[-10,-9,-2],[-1,-6,6],[-8,7,1],[5,1,-4],[-7,2,7],[4,-10,-8],[8,1,-6],[-9,6,-8],[-4,-5,-10],[-5,-7,-9],[-10,-2,7],[-3,3,10],[4,4,3],[-7,5,-6],[-4,-2,-8],[5,-3,8],[-1,5,-8],[-3,-4,4],[-9,8,4],[8,3,-9],[8,-10,-5],[1,3,9],[-2,-4,9],[8,9,-3],[8,-3,9],[5,-9,8],[-5,-9,-6],[-10,9,7],[-3,8,-10],[9,10,10],[-5,9,-10],[-8,-8,3],[-5,4,-10],[4,5,5],[2,-3,7],[4,-10,8],[1,-5,4],[5,-5,-5],[-10,-6,10],[-2,7,-5],[-1,-8,1],[9,5,1],[5,1,4],[3,-5,-1],[-2,5,8],[-6,8,-8],[-4,-1,2],[-10,-9,-5],[7,7,8],[-6,10,-2],[3,5,-3],[-2,-1,-8],[6,-10,-7],[8,-4,7],[-4,2,6],[4,3,-3],[-4,5,-8],[8,9,9],[-4,1,3],[-4,2,-2],[-2,-2,-8],[1,-9,-7],[9,3,5],[7,8,-1],[-7,1,-1],[-10,1,-7],[-8,-1,5],[6,-3,-6],[-10,10,-3],[2,-4,-1],[-7,-7,4],[7,2,-9],[-6,-5,-5],[-7,-3,4],[6,8,-8],[-6,-2,3],[-6,-10,-6],[7,5,1],[10,6,3],[-1,-5,-10],[10,7,-8],[9,-9,-2],[1,9,9],[7,-5,5],[2,-10,7],[-9,-5,-8],[-5,7,-10],[-10,-8,7],[8,9,5],[-3,1,4],[-3,-4,7],[9,3,-9],[5,-1,8],[-10,-2,-10],[-4,5,-8],[7,10,-8],[-5,3,3],[8,1,10],[-9,-6,1],[7,-2,-3],[1,-10,1],[-10,-6,-4],[-4,8,-2],[-5,-9,2],[-10,5,1],[-10,10,-3],[-1,7,7],[8,-4,7],[5,8,6],[5,-9,7],[8,4,1],[-9,2,10],[7,-3,6],[-8,-5,-8],[6,-6,-2],[7,-2,10],[-8,-6,6],[2,-5,6],[-4,-6,-1],[-9,-8,4],[-7,1,-1],[3,-9,2],[6,-9,-8],[6,-9,10],[-7,-9,-5],[4,-5,3],[6,-5,-6],[10,-10,5],[-6,-9,-5],[7,9,8],[10,-6,-9],[-10,5,-9]], dtype = "int64")#candidate|5420|(210, 3)|const|int64
call_5418 = relay.TupleGetItem(func_2402_call(relay.reshape(var_5419.astype('float64'), [3, 1, 16]), relay.reshape(const_5420.astype('int64'), [630,]), ), 0)
call_5421 = relay.TupleGetItem(func_2405_call(relay.reshape(var_5419.astype('float64'), [3, 1, 16]), relay.reshape(const_5420.astype('int64'), [630,]), ), 0)
bop_5430 = relay.bitwise_or(call_5418.astype('int64'), relay.reshape(var_5419.astype('int64'), relay.shape_of(call_5418))) # shape=(3, 1, 16)
bop_5433 = relay.bitwise_or(call_5421.astype('int64'), relay.reshape(var_5419.astype('int64'), relay.shape_of(call_5421))) # shape=(3, 1, 16)
output = relay.Tuple([call_5416,const_5420,bop_5430,])
output2 = relay.Tuple([call_5417,const_5420,bop_5433,])
func_5435 = relay.Function([var_5419,], output)
mod['func_5435'] = func_5435
mod = relay.transform.InferType()(mod)
mutated_mod['func_5435'] = func_5435
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5436 = relay.var("var_5436", dtype = "float64", shape = (48,))#candidate|5436|(48,)|var|float64
func_5435_call = mutated_mod.get_global_var('func_5435')
call_5437 = func_5435_call(var_5436)
output = call_5437
func_5438 = relay.Function([var_5436], output)
mutated_mod['func_5438'] = func_5438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4443_call = mod.get_global_var('func_4443')
func_4445_call = mutated_mod.get_global_var('func_4445')
call_5557 = func_4443_call()
call_5558 = func_4443_call()
output = relay.Tuple([call_5557,])
output2 = relay.Tuple([call_5558,])
func_5564 = relay.Function([], output)
mod['func_5564'] = func_5564
mod = relay.transform.InferType()(mod)
mutated_mod['func_5564'] = func_5564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5564_call = mutated_mod.get_global_var('func_5564')
call_5565 = func_5564_call()
output = call_5565
func_5566 = relay.Function([], output)
mutated_mod['func_5566'] = func_5566
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5573 = relay.var("var_5573", dtype = "float64", shape = (10, 10, 13))#candidate|5573|(10, 10, 13)|var|float64
var_5574 = relay.var("var_5574", dtype = "float64", shape = (10, 10, 13))#candidate|5574|(10, 10, 13)|var|float64
bop_5575 = relay.add(var_5573.astype('float64'), relay.reshape(var_5574.astype('float64'), relay.shape_of(var_5573))) # shape=(10, 10, 13)
output = relay.Tuple([bop_5575,])
output2 = relay.Tuple([bop_5575,])
func_5583 = relay.Function([var_5573,var_5574,], output)
mod['func_5583'] = func_5583
mod = relay.transform.InferType()(mod)
var_5584 = relay.var("var_5584", dtype = "float64", shape = (10, 10, 13))#candidate|5584|(10, 10, 13)|var|float64
var_5585 = relay.var("var_5585", dtype = "float64", shape = (10, 10, 13))#candidate|5585|(10, 10, 13)|var|float64
output = func_5583(var_5584,var_5585,)
func_5586 = relay.Function([var_5584,var_5585,], output)
mutated_mod['func_5586'] = func_5586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4573_call = mod.get_global_var('func_4573')
func_4575_call = mutated_mod.get_global_var('func_4575')
call_5588 = relay.TupleGetItem(func_4573_call(), 1)
call_5589 = relay.TupleGetItem(func_4575_call(), 1)
func_4628_call = mod.get_global_var('func_4628')
func_4630_call = mutated_mod.get_global_var('func_4630')
call_5594 = func_4628_call()
call_5595 = func_4628_call()
output = relay.Tuple([call_5588,call_5594,])
output2 = relay.Tuple([call_5589,call_5595,])
func_5607 = relay.Function([], output)
mod['func_5607'] = func_5607
mod = relay.transform.InferType()(mod)
mutated_mod['func_5607'] = func_5607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5607_call = mutated_mod.get_global_var('func_5607')
call_5608 = func_5607_call()
output = call_5608
func_5609 = relay.Function([], output)
mutated_mod['func_5609'] = func_5609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4573_call = mod.get_global_var('func_4573')
func_4575_call = mutated_mod.get_global_var('func_4575')
call_5686 = relay.TupleGetItem(func_4573_call(), 0)
call_5687 = relay.TupleGetItem(func_4575_call(), 0)
uop_5688 = relay.atanh(call_5686.astype('float32')) # shape=(13, 13, 4)
uop_5690 = relay.atanh(call_5687.astype('float32')) # shape=(13, 13, 4)
func_432_call = mod.get_global_var('func_432')
func_436_call = mutated_mod.get_global_var('func_436')
var_5699 = relay.var("var_5699", dtype = "int64", shape = (630,))#candidate|5699|(630,)|var|int64
call_5698 = func_432_call(relay.reshape(var_5699.astype('int64'), [15, 7, 6]), relay.reshape(var_5699.astype('int64'), [15, 7, 6]), )
call_5700 = func_432_call(relay.reshape(var_5699.astype('int64'), [15, 7, 6]), relay.reshape(var_5699.astype('int64'), [15, 7, 6]), )
bop_5705 = relay.bitwise_and(uop_5688.astype('uint32'), relay.reshape(call_5686.astype('uint32'), relay.shape_of(uop_5688))) # shape=(13, 13, 4)
bop_5708 = relay.bitwise_and(uop_5690.astype('uint32'), relay.reshape(call_5687.astype('uint32'), relay.shape_of(uop_5690))) # shape=(13, 13, 4)
output = relay.Tuple([call_5698,var_5699,bop_5705,])
output2 = relay.Tuple([call_5700,var_5699,bop_5708,])
func_5716 = relay.Function([var_5699,], output)
mod['func_5716'] = func_5716
mod = relay.transform.InferType()(mod)
var_5717 = relay.var("var_5717", dtype = "int64", shape = (630,))#candidate|5717|(630,)|var|int64
output = func_5716(var_5717)
func_5718 = relay.Function([var_5717], output)
mutated_mod['func_5718'] = func_5718
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5759 = relay.var("var_5759", dtype = "float64", shape = (8, 7, 11))#candidate|5759|(8, 7, 11)|var|float64
uop_5760 = relay.asinh(var_5759.astype('float64')) # shape=(8, 7, 11)
uop_5764 = relay.asin(var_5759.astype('float32')) # shape=(8, 7, 11)
bop_5774 = relay.divide(var_5759.astype('float64'), relay.reshape(uop_5760.astype('float64'), relay.shape_of(var_5759))) # shape=(8, 7, 11)
func_5022_call = mod.get_global_var('func_5022')
func_5024_call = mutated_mod.get_global_var('func_5024')
var_5778 = relay.var("var_5778", dtype = "float32", shape = (2112,))#candidate|5778|(2112,)|var|float32
call_5777 = relay.TupleGetItem(func_5022_call(relay.reshape(var_5778.astype('float32'), [12, 16, 11])), 3)
call_5779 = relay.TupleGetItem(func_5024_call(relay.reshape(var_5778.astype('float32'), [12, 16, 11])), 3)
output = relay.Tuple([uop_5764,bop_5774,call_5777,var_5778,])
output2 = relay.Tuple([uop_5764,bop_5774,call_5779,var_5778,])
func_5782 = relay.Function([var_5759,var_5778,], output)
mod['func_5782'] = func_5782
mod = relay.transform.InferType()(mod)
mutated_mod['func_5782'] = func_5782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5782_call = mutated_mod.get_global_var('func_5782')
var_5784 = relay.var("var_5784", dtype = "float64", shape = (8, 7, 11))#candidate|5784|(8, 7, 11)|var|float64
var_5785 = relay.var("var_5785", dtype = "float32", shape = (2112,))#candidate|5785|(2112,)|var|float32
call_5783 = func_5782_call(var_5784,var_5785,)
output = call_5783
func_5786 = relay.Function([var_5784,var_5785,], output)
mutated_mod['func_5786'] = func_5786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mod.get_global_var('func_4149')
func_4151_call = mutated_mod.get_global_var('func_4151')
call_5798 = func_4149_call()
call_5799 = func_4149_call()
func_4852_call = mod.get_global_var('func_4852')
func_4855_call = mutated_mod.get_global_var('func_4855')
const_5801 = relay.const([-5.760286,-2.995100,-1.091168,-3.288609,1.629741,4.599850,5.754813,-8.293866,-8.212195,0.686656,-0.026430,-7.355170,-2.028735,3.921408,-5.156426,9.399605,-6.033459,5.945119,0.831137,-2.243912,-9.721206,1.799260,-2.715459,-8.458887,-4.419787,-5.124597,4.765021,-1.290393,-2.434719,3.339390,-8.429932,6.065884,4.995199,-8.402170,-5.212032,0.216534,-9.124691,-0.494170,2.773564,8.415371,-5.973964,-2.957703,-7.588280,-2.399895,3.127862,4.741556,-5.373463,-7.916695,8.134446,-0.659429,-9.623478,-1.471213,-7.942748,3.294022,-1.061736,8.818351,-2.016397,-7.378540,-9.642120,-0.351555,8.113280,8.721896,-0.921321,0.010651,-9.265318,-4.441935,1.164166,9.261692,7.516469,8.407301,-8.175241,4.526981,7.345457,4.671066,-0.544016,8.904002,-6.554186,5.760269,-7.139841,-8.719182,-2.173043,1.333445,-3.349520,5.443799,0.137232,6.166008,6.228381,4.290777,-0.040699,-6.921096,-7.747849,-2.114755,-4.616009,1.735849,-5.321525,-3.451325,-1.931205,5.507129,-6.453125,7.141638,4.573246,1.290538,3.071603,7.486712,-0.218318,-0.900462,3.994890,1.308643,-2.246323,0.860526,-2.808630,1.371928,4.906302,3.149993,2.960205,-9.247005,0.955057,6.936332,-6.319525,0.188311,-8.402136,2.619820,-0.501248,7.664943,0.506101,-7.599828,-2.749936,3.021077,-0.840034,-5.045359,3.365623,-1.520019,-6.369512,8.700307,0.734941,5.597225,-3.998969,3.318595,4.462322,5.054688,6.160210,4.608098,1.367858,-8.580148,8.530805,6.951410,1.874620,-2.611612,3.095161,-2.302729,-8.274712,-5.206486,-0.942380,2.736045,-3.481646,-7.890556,-7.475091,-8.543727,-9.884295,3.535900,2.902414,-0.881062,7.593455,-0.215771,-1.390429,3.261011,8.189748,9.463815,7.537691,6.085254,4.115820,-0.164055,9.788255,4.958291,3.267372,-5.564018,6.846387,3.157552,4.144347,1.375361,-4.602011,-0.193225,-9.087424,3.984302,-3.765784,-9.892471,-7.173264,-6.477955,5.897050,-5.001937,-6.155470,3.135658,3.479987,-4.989083,-4.065350,1.755208,-0.780452,-7.277678,0.263832,8.969948,8.878507,-9.639061,-2.195655,1.363366,-7.497411,-8.866042,-2.801824,6.655648,-7.237071,-9.303156,3.043990,6.810370,3.333140,2.713199,3.353621,1.605129,-1.117333,-0.869640,-6.412795,-3.077724,3.391446,9.105244,-9.239352,-9.928217], dtype = "float32")#candidate|5801|(224,)|const|float32
call_5800 = func_4852_call(relay.reshape(const_5801.astype('float32'), [4, 8, 7]))
call_5802 = func_4852_call(relay.reshape(const_5801.astype('float32'), [4, 8, 7]))
func_3853_call = mod.get_global_var('func_3853')
func_3855_call = mutated_mod.get_global_var('func_3855')
call_5812 = func_3853_call()
call_5813 = func_3853_call()
func_4149_call = mod.get_global_var('func_4149')
func_4151_call = mutated_mod.get_global_var('func_4151')
call_5821 = func_4149_call()
call_5822 = func_4149_call()
func_3853_call = mod.get_global_var('func_3853')
func_3855_call = mutated_mod.get_global_var('func_3855')
call_5831 = func_3853_call()
call_5832 = func_3853_call()
output = relay.Tuple([call_5798,call_5800,const_5801,call_5812,call_5821,call_5831,])
output2 = relay.Tuple([call_5799,call_5802,const_5801,call_5813,call_5822,call_5832,])
func_5857 = relay.Function([], output)
mod['func_5857'] = func_5857
mod = relay.transform.InferType()(mod)
mutated_mod['func_5857'] = func_5857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5857_call = mutated_mod.get_global_var('func_5857')
call_5858 = func_5857_call()
output = call_5858
func_5859 = relay.Function([], output)
mutated_mod['func_5859'] = func_5859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4027_call = mod.get_global_var('func_4027')
func_4028_call = mutated_mod.get_global_var('func_4028')
call_5901 = func_4027_call()
call_5902 = func_4027_call()
output = relay.Tuple([call_5901,])
output2 = relay.Tuple([call_5902,])
func_5907 = relay.Function([], output)
mod['func_5907'] = func_5907
mod = relay.transform.InferType()(mod)
output = func_5907()
func_5908 = relay.Function([], output)
mutated_mod['func_5908'] = func_5908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4461_call = mod.get_global_var('func_4461')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_5932 = relay.TupleGetItem(func_4461_call(), 0)
call_5933 = relay.TupleGetItem(func_4462_call(), 0)
output = call_5932
output2 = call_5933
func_5953 = relay.Function([], output)
mod['func_5953'] = func_5953
mod = relay.transform.InferType()(mod)
output = func_5953()
func_5954 = relay.Function([], output)
mutated_mod['func_5954'] = func_5954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5168_call = mod.get_global_var('func_5168')
func_5169_call = mutated_mod.get_global_var('func_5169')
call_5965 = relay.TupleGetItem(func_5168_call(), 0)
call_5966 = relay.TupleGetItem(func_5169_call(), 0)
output = call_5965
output2 = call_5966
func_6004 = relay.Function([], output)
mod['func_6004'] = func_6004
mod = relay.transform.InferType()(mod)
output = func_6004()
func_6005 = relay.Function([], output)
mutated_mod['func_6005'] = func_6005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5168_call = mod.get_global_var('func_5168')
func_5169_call = mutated_mod.get_global_var('func_5169')
call_6045 = relay.TupleGetItem(func_5168_call(), 0)
call_6046 = relay.TupleGetItem(func_5169_call(), 0)
func_3883_call = mod.get_global_var('func_3883')
func_3886_call = mutated_mod.get_global_var('func_3886')
call_6052 = relay.TupleGetItem(func_3883_call(relay.reshape(call_6045.astype('float64'), [11, 12, 15])), 1)
call_6053 = relay.TupleGetItem(func_3886_call(relay.reshape(call_6045.astype('float64'), [11, 12, 15])), 1)
func_5583_call = mod.get_global_var('func_5583')
func_5586_call = mutated_mod.get_global_var('func_5586')
const_6063 = relay.const([6.827128,-8.659313,0.610553,-0.536263,-4.340612,5.319933,1.199122,-1.811701,-2.193927,0.083955,2.816777,0.077737,6.693320,-5.142278,-2.814502,-8.374083,-3.614321,-1.496507,-7.779059,8.408790,0.054006,-3.972708,9.268497,5.743965,-8.581285,9.331396,4.211391,-0.739734,-5.672777,-7.014424,-1.572157,-3.236874,1.836492,-7.265235,-9.205778,-0.213059,-2.113076,-2.536295,7.993696,-8.122406,-9.056318,3.642595,-2.437361,-6.671927,1.234355,-1.329531,-4.692029,-8.536208,1.574070,4.022068,5.025328,5.622799,-9.729389,4.079979,6.898990,0.711336,4.829835,-2.123842,-4.840557,2.864532,5.077173,8.737781,-6.205548,4.832492,0.174177,8.493355,-1.367170,-9.490987,-6.364800,-5.612078,7.340695,-0.579900,-1.859029,1.696595,0.046117,-9.761898,-7.130178,-0.925605,-5.281834,-0.902128,-1.356361,-0.125630,1.301373,7.135245,-6.386686,1.911611,0.735826,-4.735133,-2.528356,-1.388521,-5.687933,-5.775497,2.776745,-3.712929,-6.746879,4.798056,-9.331573,4.763331,-7.717706,-9.529906,-3.896157,2.393269,5.169521,-4.048955,7.360498,4.705563,6.770835,-9.090892,5.181744,-9.679222,5.260773,-3.906868,7.212163,5.535718,5.039902,-0.238492,-9.938169,1.758983,-8.113993,0.293178,6.243578,5.381592,1.168403,0.182361,-7.026103,-9.280503,0.763559,-0.034260,7.552149,-2.031679,7.768810,-3.794549,-6.189966,9.726265,3.690318,-6.592722,5.111712,-0.153039,0.474270,5.105565,0.543539,-2.298925,6.218337,-9.227586,-6.517978,6.008501,0.503168,9.465606,4.028458,-3.333317,-3.861025,4.318087,7.834334,-7.048845,0.013544,-9.751211,2.655584,8.485393,5.555752,5.005937,9.758187,3.236692,8.853138,-2.084950,3.822262,3.734741,-4.464430,-4.604282,-9.070231,-2.632678,-2.406519,7.655660,7.765878,-7.512049,-0.651460,2.954394,-8.904853,-7.004488,5.618198,2.440405,-4.133283,-3.233396,5.113792,-8.042576,7.187515,-8.167631,5.199901,-8.875806,-7.225440,-6.555688,-3.140324,-3.343532,-6.391673,-4.448207,-2.144861,0.870143,1.600826,7.403916,-6.756942,-6.863592,-6.727519,7.197709,-8.568343,7.947361,7.814719,9.729938,2.710085,-3.438674,9.357520,7.572389,-3.057475,-6.302759,7.689779,9.122047,4.835782,9.965794,-9.122975,2.524730,-0.577176,5.874079,-0.543844,-6.054576,8.876466,-8.271594,8.344578,-6.289200,-3.970501,8.042437,-2.320069,6.460944,2.781215,3.360715,4.048449,-4.703683,8.843060,1.855230,8.095381,6.787674,0.292832,4.223042,-4.273723,-2.823376,-5.689072,-4.037678,-4.786017,-9.001167,-2.838683,4.282524,-5.920321,-8.367366,-2.050177,-9.275859,2.191062,-4.375582,0.501417,2.569406,8.724045,-6.742185,-0.494330,-3.141128,-2.057595,-8.898226,-1.035285,-9.684990,4.504035,3.385272,6.468723,3.754706,9.607686,5.080597,6.293950,-4.611362,-4.733480,-4.780278,8.042279,-0.483593,4.376107,0.279365,-2.396810,0.881149,-3.472865,8.151331,-8.069897,-1.287733,-1.195366,-2.076386,-3.785870,-5.868799,7.328373,7.813996,0.480691,-0.311821,-6.654557,9.230010,2.130718,3.802076,5.016537,2.448738,6.901182,2.771117,2.534374,-0.198869,0.499893,5.889799,2.269060,7.100373,-1.099032,-5.726844,6.065062,7.328718,-8.565040,-5.789470,-1.994414,8.716885,1.788226,1.743676,-4.849136,7.891366,9.373041,-8.727507,6.206278,9.380392,2.583194,0.472546,3.847152,1.134225,5.580469,3.356786,-2.049960,5.762586,-5.457507,-2.973246,-1.949277,-0.094417,-1.405791,0.031756,-6.828813,0.115787,-3.085813,4.244110,-9.581894,2.033480,-2.857242,0.852218,0.518238,3.306936,0.216237,-1.822127,1.098833,5.842221,6.424092,3.968150,-1.867907,1.833936,4.558693,-4.973342,6.136375,6.996336,9.725466,-3.499809,-0.616801,-6.459860,-3.403849,0.302640,8.316743,9.998971,1.977973,-5.928031,-7.718282,-1.121561,-7.978124,4.067862,-8.602603,-6.531167,2.784982,-7.948576,-9.762942,7.979155,1.687533,-7.374123,-2.701847,6.165523,-7.007205,6.381991,2.130948,2.450072,-0.355913,-6.855640,4.897885,-8.802533,3.133593,-5.374451,6.504714,-9.754255,4.786798,1.696949,2.828379,7.974431,4.111653,-6.692474,7.510335,-7.324537,-2.815190,-0.234070,4.884997,-2.800770,-9.862643,-4.172349,-4.098672,-2.035235,3.044115,9.308333,5.101389,2.727825,7.882284,6.814149,5.340032,7.779834,-4.377065,4.235117,-8.833566,3.620815,3.665397,6.444333,-1.468929,8.008293,9.526561,-2.432700,5.690409,0.508842,9.255515,6.060112,0.688124,-6.836784,1.643176,1.919064,6.772448,-5.216345,3.371611,8.772960,5.067521,9.475646,1.176122,0.767920,5.083509,-4.843248,-1.808688,2.040459,-4.600053,2.599001,-4.649171,3.009122,9.933086,-3.711124,1.753798,7.465745,-4.797748,-8.909959,-2.208073,-6.859373,-3.792206,0.883669,2.104314,-3.756447,-5.376824,8.707160,5.855010,6.317095,-3.455757,1.635967,3.514554,-4.346828,1.038315,0.215938,3.907573,-1.957476,-2.120211,-6.972507,-5.455123,9.863503,-0.978735,6.079761,-8.004285,2.112992,-4.082731,-7.209899,6.400745,4.178850,1.594859,-2.506481,5.438231,4.647953,-6.059210,6.958809,-9.813341,-7.709468,1.193770,-2.776802,-1.006586,-2.856989,-9.511250,-0.406146,6.921844,4.958698,-7.802217,5.706208,-9.211263,-8.513757,-5.755579,9.863329,-5.608244,-7.970583,-2.569471,6.254237,-7.119228,8.272809,4.812418,-6.819453,-8.496279,5.357825,1.565540,-2.171733,6.324877,4.927141,-2.377536,1.099689,-7.523759,-4.164052,-6.341761,5.322506,2.970150,-2.758009,-6.051169,4.047959,-6.122470,5.383747,-2.238177,0.977808,-2.986713,3.702807,3.636981,-0.240390,-9.363904,-5.031781,-5.960474,6.107504,3.567926,-3.179966,-2.491289,-1.441695,0.230418,8.694226,5.427010,5.647646,7.521767,-8.444697,3.945577,-6.447591,0.282506,8.872206,-4.817266,0.181788,-2.616622,3.572672,9.644934,8.212268,5.987541,-9.311434,1.553765,4.843552,6.224753,4.557296,-2.288372,-5.733607,2.718551,4.392421,5.577172,0.898518,6.396459,-1.437673,-5.730859,0.285623,-6.969100,-0.876449,3.722139,-9.659786,7.523072,-2.238867,8.135057,5.287919,-1.616856,-9.409128,8.025453,1.430589,-8.295616,4.167447,3.370975,0.547105,2.422150,2.443415,4.395861,4.417252,7.122203,-9.100707,-3.838282,9.558451,-3.140402,-8.083377,0.414505,-5.813031,-1.456342,-4.498678,-5.382620,4.736709,9.229332,4.185371,4.926778,4.548234,-5.950218,5.704440,8.743237,9.133543,6.039548,6.206133,4.685339,-0.026422,-8.743697,5.716154,-6.192154,-4.550047,2.511676,-3.463002,-9.586581,0.114416,0.289052,1.192017,-1.699384,9.795360,0.977610,-8.180049,-9.124723,-8.465897,-9.155792,-6.540717,-2.749358,-6.910883,-6.270358,-5.692985,4.075007,3.885524,6.351649,1.898854,0.521990,4.256285,-4.942845,7.488186,-9.953640,9.297215,4.049657,-2.768701,-2.778029,3.405260,8.515803,9.927438,2.633434,-0.010690,3.451227,-5.914786,-3.982345,1.895927,-1.488859,1.178588,-8.034449,2.157640,-8.310700,-8.184111,-6.561775,1.125367,5.003017,-0.072481,5.331195,4.342336,5.549656,7.676885,7.872721,-7.099251,0.085410,7.447274,-9.654999,8.819157,-4.203760,5.157533,7.108300,-5.420541,5.148274,-3.461525,8.895568,9.282407,3.729293,-8.137209,-7.875335,-3.180557,5.651458,3.247947,-4.870457,-8.411732,-8.398324,-6.942178,9.824346,1.576751,0.745346,9.600882,6.093984,7.030437,-3.913501,-9.261969,-6.736043,-6.422226,-9.928781,5.118774,4.497081,3.768009,0.308546,5.536175,-1.627550,5.812870,-7.780550,5.921778,-3.828024,6.374659,-7.375590,1.112561,-1.132658,-0.809440,6.035755,-7.705198,-4.320527,3.047111,5.238470,-0.285448,7.036380,2.018440,-7.616617,7.095364,-8.631108,8.461315,-4.476316,2.276402,2.775828,1.710780,-1.417028,0.067044,2.477553,-9.117858,0.362352,7.672506,1.904178,0.216240,4.570746,-9.709974,7.331024,-4.324147,-0.614590,-2.114602,-5.019592,-8.238773,8.150065,7.317802,-4.513635,8.157781,-2.341133,-3.126765,-8.391099,4.921387,5.702433,1.860367,-8.703785,-5.564152,7.160360,-2.942836,7.112035,-0.209466,-3.890781,5.194023,-6.085015,-0.433510,3.298810,-0.274785,-0.319175,7.723641,2.170520,-9.954304,9.897985,-9.407276,-1.943133,-0.959425,6.179433,-9.323270,-2.981456,8.932000,4.218297,1.352873,-4.980233,-0.191145,7.433375,-3.162541,-2.318366,-2.600164,-8.316018,-2.802647,2.921219,-8.690306,-1.337386,-5.422390,-1.638847,3.329544,-3.261456,7.069483,-8.495337,2.619277,0.607659,-5.395295,2.611115,8.439144,6.822564,-7.484066,-5.800400,5.802827,5.815371,7.217695,5.544241,5.735265,9.294098,4.497952,-0.824147,-4.278266,-1.726870,3.584738,2.952563,2.345426,3.801323,-3.368739,-6.577368,-7.103287,1.614907,-0.114115,-3.684002,-3.426296,-5.749373,7.694318,7.125358,-1.004445,-9.267606,4.672032,3.197767,-8.140656,-8.131706,-6.514491,-3.915303,-0.121204,6.019879,6.915959,6.380817,0.706235,2.364019,-4.211336,-8.526235,-7.711189,9.293585,0.354743,4.504024,6.272746,-5.295754,-7.802036,-9.227855,-9.821573,4.508628,7.245526,-5.755404,-5.405401,0.683490,-7.527670,-6.974273,-7.339613,-5.024809,-6.479362,0.911195,3.604840,4.087016,-1.417672,-2.715122,9.591099,-2.115723,-2.127576,-4.845117,-9.139187,-7.357060,7.061274,-8.146448,-0.137082,2.081071,-4.430601,-6.854160,-0.489107,9.006973,3.183845,-7.718690,-4.589581,5.963717,3.363718,3.009991,0.976967,-5.395565,-2.896645,-4.760201,6.805483,1.944738,-5.687469,4.392392,-6.683309,7.001976,-4.349003,-6.739311,0.397190,-2.735591,9.301290,-5.352640,8.402647,-2.225962,1.391986,-7.336174,-8.862737,-4.859951,9.143894,-6.778381,3.264707,8.189569,6.673889,-5.962790,4.245912,2.524231,-2.805230,5.903963,-2.116231,-1.811025,-1.089702,-1.178312,-4.735637,2.254834,-0.466864,7.757260,1.821052,6.261140,1.939680,4.428771,-0.760091,6.153790,6.711542,-3.602703,-9.727356,8.013313,4.287346,-9.277853,1.400900,4.828846,6.605951,1.972868,8.967380,7.714707,-5.960357,1.546394,2.216530,1.372218,1.179445,-3.889611,-2.251714,-5.497742,8.296773,-6.389247,-2.173748,-1.829555,-0.198099,1.352599,-8.233442,-5.024103,4.078012,-7.900723,9.409956,5.880257,0.281201,-0.008808,-1.896742,-8.185626,0.521381,-9.320731,-8.182815,7.953296,-3.849146,2.839268,0.647308,1.518980,8.998097,2.300300,6.977922,-3.527995,-1.551757,0.344642,7.190445,-6.062403,-4.187802,0.894002,3.046348,9.538853,9.010660,8.567422,1.254507,0.380932,-0.327331,2.413236,-8.439284,-3.286626,-9.960817,5.893070,7.066434,6.391447,-9.512038,3.793009,8.750192,1.758188,2.313313,-8.152308,7.255079,4.461604,-6.655209,1.880171,-2.750549,-8.957618,8.599447,3.656597,8.460513,-7.153208,8.878868,-8.141330,5.292293,7.330689,-9.842323,8.751572,1.629778,7.230354,6.881108,-3.790068,-7.184329,-4.629114,-4.889171,9.393903,-5.771100,4.358396,6.235507,5.662387,8.512618,3.819498,-5.256932,1.509729,6.560624,3.557206,-5.288956,7.085930,-3.592433,-4.219769,5.709513,1.970047,-9.249817,6.127445,-4.043787,-9.970007,1.048764,7.493012,-3.148028,0.043054,9.271167,-2.628432,4.567028,-7.016626,3.331540,-6.113159,-7.776899,4.790658,8.147550,-6.675632,2.565431,6.181796,-4.409070,-8.570644,-1.017552,5.862685,-1.475153,8.382410,9.703761,-4.394586,-1.520704,4.747258,-3.053756,2.610408,4.250587,7.028712,-6.583777,4.699699,5.061040,0.141658,9.280522,7.722412,-1.305015,3.926069,-5.717105,1.367018,8.501916,-1.809164,0.620005,2.161463,8.964483,0.371797,2.367403,2.531960,-6.047408,-9.430164,4.048675,8.517132,-7.101453,7.688332,-4.000285,-8.743346,9.352954,0.549248,-2.848791,2.763301,3.639929,-4.620725,9.419301,7.601597,-6.044748,9.257352,0.092401,-5.575724,-7.301898,2.484003,-7.388060,-6.173086,-8.489377,-0.371686,-1.951793,-6.734953,-0.567893,-3.873674,-7.593521,7.644071,-0.259386,-2.068764,2.321121,9.281154,-9.372975,5.221585,-4.753594,-8.404703,0.104117,-7.549520,-8.208953,-9.373031,1.578714,-5.395707,-5.926265,-9.500981,4.399846,4.195171,8.841539,-8.014659,7.066319,-5.345670,3.784144,-4.330041,9.547291,-1.620292,9.403371,-9.260065,9.983966,5.292481,-3.920690,-9.594377,-1.172553,3.793996,3.066369,-9.620421,0.215568,-0.737115,2.029248,2.384661,7.402356,0.178232,-6.071361,4.001714,-9.309716,-2.005525,3.485819,-6.694120,-7.719027,5.243001,0.437666,-1.343737,6.309415,1.010061,5.020347,8.861578,-9.343313,1.331301,7.686350,0.299657,5.916287,-0.132745,-2.843341,3.370613,-0.369615,-5.461218,-5.804303,-7.104759,-4.373349,-9.495850,1.833396,-4.893159,-9.950865,-5.383470,6.499213,-7.789528,1.045986,0.669632,4.001504,-0.079954,9.323358,-6.386917,7.825926,4.603450,-8.130278,2.772893,-9.207855,-7.815930,-4.946110,-8.022444,-7.329263,-3.851165,3.515054,9.443736,-2.191378,9.786288,2.855552,0.788729,-2.760736,-6.692984,4.556727,-8.610682,8.719166,-2.366199,-7.612679,5.378553,1.826880,-5.720587,2.512831,-3.352210,-7.928971,-2.980017,4.510900,-0.942814,-2.186607,-5.348722,5.025821,0.835489,6.851664,-0.698945,-7.319065,-5.908651,8.257017,0.831017,5.773816,9.767892,6.879460,3.629284,6.578506,-9.875695,-6.789008,4.758677,-1.843050,-3.644561,3.933738,1.295744,9.652657,7.584741,-9.364272,4.748817,-2.399820,6.334702,-0.204983,-4.405983,7.532822], dtype = "float64")#candidate|6063|(1300,)|const|float64
call_6062 = relay.TupleGetItem(func_5583_call(relay.reshape(const_6063.astype('float64'), [10, 10, 13]), relay.reshape(const_6063.astype('float64'), [10, 10, 13]), ), 0)
call_6064 = relay.TupleGetItem(func_5586_call(relay.reshape(const_6063.astype('float64'), [10, 10, 13]), relay.reshape(const_6063.astype('float64'), [10, 10, 13]), ), 0)
output = relay.Tuple([call_6045,call_6052,call_6062,const_6063,])
output2 = relay.Tuple([call_6046,call_6053,call_6064,const_6063,])
func_6071 = relay.Function([], output)
mod['func_6071'] = func_6071
mod = relay.transform.InferType()(mod)
output = func_6071()
func_6072 = relay.Function([], output)
mutated_mod['func_6072'] = func_6072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_6111 = func_4070_call()
call_6112 = func_4070_call()
func_3199_call = mod.get_global_var('func_3199')
func_3202_call = mutated_mod.get_global_var('func_3202')
var_6116 = relay.var("var_6116", dtype = "int64", shape = ())#candidate|6116|()|var|int64
const_6117 = relay.const([6,-3,1,-9,-10,4,4,8,3,-3,3,5,-5,8,-9,-2,-7,5,-5,-6,1,-2,-8,-1,8,4,-5,9,-3,-2,8,-7,-10,-4,-9,8,10,3,10,-9,-7,10,-1,1,-6,6,8,-10,8,-1,-4,-4,-1,-4,-8,-1,-3,8,2,8,4,-3,-9,-1,4,-1,3,5,-10,-8,10,-7,2,1,-7,-3,2,5,6,-8,8,-1,3,-8,2,5,-5,9,10,-1,-8,9,-10,-1,10,7,9,2,3,-8,6,-9,8,8,7,-8,-6,6,3,2,-9,3,6,-9,-7,-6,-2,6,4,-9,-5,-7,-4,-7,-2], dtype = "int64")#candidate|6117|(125,)|const|int64
call_6115 = relay.TupleGetItem(func_3199_call(relay.reshape(var_6116.astype('int64'), []), relay.reshape(const_6117.astype('int64'), [5, 5, 5]), ), 0)
call_6118 = relay.TupleGetItem(func_3202_call(relay.reshape(var_6116.astype('int64'), []), relay.reshape(const_6117.astype('int64'), [5, 5, 5]), ), 0)
output = relay.Tuple([call_6111,call_6115,var_6116,const_6117,])
output2 = relay.Tuple([call_6112,call_6118,var_6116,const_6117,])
func_6124 = relay.Function([var_6116,], output)
mod['func_6124'] = func_6124
mod = relay.transform.InferType()(mod)
var_6125 = relay.var("var_6125", dtype = "int64", shape = ())#candidate|6125|()|var|int64
output = func_6124(var_6125)
func_6126 = relay.Function([var_6125], output)
mutated_mod['func_6126'] = func_6126
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6131 = relay.var("var_6131", dtype = "int32", shape = (10, 2, 1))#candidate|6131|(10, 2, 1)|var|int32
var_6132 = relay.var("var_6132", dtype = "int32", shape = (10, 2, 10))#candidate|6132|(10, 2, 10)|var|int32
bop_6133 = relay.add(var_6131.astype('int32'), var_6132.astype('int32')) # shape=(10, 2, 10)
var_6136 = relay.var("var_6136", dtype = "int32", shape = (10, 2, 10))#candidate|6136|(10, 2, 10)|var|int32
bop_6137 = relay.right_shift(var_6132.astype('uint32'), relay.reshape(var_6136.astype('uint32'), relay.shape_of(var_6132))) # shape=(10, 2, 10)
func_4093_call = mod.get_global_var('func_4093')
func_4096_call = mutated_mod.get_global_var('func_4096')
const_6144 = relay.const([10,-8,8,6,5,7,9,7,10,-7,-5,-4,6,2,-1,-5,-4,5,8,-6,-7,-3,6,10,-4,-7,-7,-3,-3,10,-9,-4,7,5,-3,8,-5,-6,3,-9,3,5,10,-5,-4,-6,-10,-3,10,-2,-8,-2,-1,6,-4,-10,-4,9,2,9,-8,6,5,-3,-7,7,5,-2,8,2,-6,9,5,6,-9,-3,9,-5,9,9,-2,5,8,8,5,5,10,1,-1,7,1,-9,9,7,1,-6,-4,2,8,7,-10,5,6,9,5,7,4,-8,-9,3,-3,-3,-9,1,7,-1,10,-6,3,6,-1,-6,9,8,-1,8,-1,2,-7,7,3,-10,-7,-1,-4,-10,10,-10,2,-6,10,-8,6,10,3,7,7,-10,6,5,-8,2,1,-6,-1,-5,-8,-1,2,-8,-9,2,-2,10,-4,5,10,-8,3,-5,8,-5,-2,1,-8,-1,-3,10,-5,-1,-5,-9,-8,-7,2,-5,-1,-7,9,-7,8,-1,-10,6,3,-4,-6,5,-1,6,4,4,-4,-8,-10,9,2,-8,-2,2,2,6,-1,5,-3,5,-4,1,-9,-2,-4,4,-2,-10,7,-2,8,-8,-8,10,3,7,4,9,6,2,-4,-8,1,1,-2,6,10,10,8,-7,7,10,3,5,-1,-1,-5,1,9,-3,-6,2,6,4,-1,-3,-7,10,-2,-3,-1,-8,-3,2,3,-4,8,-5,-5,-6,-9,5,-4,10,-9,9,-7,-8,-7,4,-10,7,4,10,-10,-8,-7,-7,-7,7,9,-7,4,-7,-8,9,1,5,9,-5,-4,-7,5,2,-2,7,6,8,-1,-10,-7,-8,8,-2,-9,-3,-9,3,-8,-5,3,-2,9,-8,-6,-1,9,1,-3,4,3,4,-10,7,2,-8,7,-6,1,-5,4,2,-7,1,-10,-1,-2,7,4,10,8,-2,8,-9,2,6,2,-9,2,7,5,-5,7,-9,-5,-10,8,6,-10,5,-9,-9,-10,9,8,-6,-6,-10,-4,-5,-9,-2,8,3,2,-1,-10,3,-7,-3,-8,8,1,-8,-8,-4,9,3,3,-5,-5,-8,-5,6,5,8,10,9,7,-8,2,1,-7,9,2,5,-10,-2,-7,-8,-8,6,-6,1,2,-8,9,-4,-6,6,-6,-5,7,-3,4,7,-10,9,-7,9,10,-2,7,-5,8,10,4,2,3,-6,-7,-8,-3,4,9,-9,-1,8,-6,10,6,-2,5,2,7,4,8,-10,-1,2,8,-9,-2,-8,9,6,7,-6,10,-10,-5,-3,-8,-7,-7,-9,2,-5,-4,-5,-10,8,7,-2,3,5,8,-4,-1,5,2,5,1,-8,-1,-8,4,-8,4,-9,2,7,-10,-8,2,10,-9,-7,3,5,-8,4,-1,-2,-2,1,5,-8,1,-7,-9,-6,-2,-9,8,-8,9,8,-6,-6,-3,4,7,4,-8,-10,10,5,8,-6,8,-3,-5,8,3,-2,10,-4,-8,2,3,-4,7,4,3,-4,-3,-9,-7,-4,8,-9,-1,-5,5,-6,-9,-1,8,-4,7,-2,-4,-1,-8,3,10,-6,5,10,9,8,6,4,5,5,-3,-2,-9,-8,-9,-7,-3,8,6,-9,5,3,-7,5,5,5,8,7,-2,8,-7,10,8,1,-7,-9,10,-4,-10,-10,-9,-5,4,-6,-6,-10,9,-5,10,-3,6,1,-5,-2,4,-10,-1,-9,6,3,-8,-6,-3,-6,-7,-3,-10,-9,-1,-7,-7,5,-1,-2,10,10,-6,-6,7,5,-8,9,3,10,10,-7,4,2,-8,4,-8,7,1,7,5,4,-10,-1,8,7,9,-5,-9,10,-1,-7,-7,7,8,-5,-7,6,9,-10,-9,7,2,2,-10,1,7,2,-2,1,4,5,-7,9,-8,-5,8,6,-5,-3,1,6,-2,1,9,6,-9,3,3,2,-2,10,-2,-2,-3,1,1,-1,8,-8,3,10,-6,8,6,-3,-8,10,9,6,-9,7,8,2,9,5,-6,6,10,5,5,-6,-1,2,8,-4,-8,-4,1,2,-8,2,2,7,-3,9,10,-10,10,3,-1,-3,-9,3,5,-8,4,6,-1,9,-5,9,-4,6,-10,-1,5,-9,-3,2,10,10,3,2,-8,5,9,-7,-4,6,10,-4,1,9,8,1,-3,-1,-6,-10,4,-6,-3,6,5,-1,7,-2,-3,-4,4,6,-6,-6,10,5,-5,-4,5,6,-2,-7,-6,-7,9,7,-7,-3,-2,5,4,3,-2,-8,9,-9,2,-9,-4,-7,-8,-8,-1,-9,-9,2,-4,-3,-4,-3,6,1,9,-8,6,8,4,-2,9,6,4,1,5,-4,6,1,1,-2,3,3,-7,-7,9,6,9,-5,-1,10,-10,-6,-4,-10,2,7,-4,-7,3,4,3,1,-3,4,-3,-4,1,-1,9,-3,-5,-6,-1,2,7,8,-5,2,5,5,-4,-3,9,1,-5,-6,-5,1,-5,1,-6,-4,8,-10,3,3,2,-2,9,-8,-8,-7,9,10,-9,-8,10,8,7,2,-3,7,8,8,-5,-4,-3,7,-8,-5,-7,-2,4,-4,-9,-1,1,10,9,9,-6,-10,-3,-10,5,-8,8,-9,1,3,2,-2,4,-4,-2,9,-7,7,-6,-9,-2,-3,-8,-3,8,6,-10,4,-10,6,-5,-8,-4,10,-1,10,7,-4,-8,1,2,5,-6,7,1,-8,10,9,-2,-5,10,-8,1,-2,-10,-4,-2,6,9,-6,7,-9,1,-1,6,7,3,5,-9,4,3,2,6,5,-1,8,-6,-7,4,1,-5,-8,-6,-4,-1,4,6,-1,-6,-8,9,9,4,6,3,9,-8,8,-1,10,-3,-8,-2,1,-5,-7,4,2,1,5,-7,-3,1,-10,-6,-4,3,-7,-9,3,7,10,7,1,-2,-1,3,4,5,-6,-2,-1,-10,-2,-9,5,-6,-9,-9,-10,-1,7,-4,7,5,-2,4,2,2,-5,10,6,6,-10,8,-3,-10,2,-3,3,2,5,-9,-10,-2,9,-6,9,-2,5,6,10,10,9,-3,-3,10,-1,-4,7,7,-9,2,-2,-6,4,-5,-9,-8,-10,3,-6,-1,9,7,3,-3,-6,2,-9,5,10,10,6,-8,-7,-10,-3,9,8,7,9,-6,4,2,-6,-9,-6,-8,6,-9,-8,-5,3,10,-9,3,-6,4,-6,-3,3,1,-10,-4,-4,1,-5,10,10,7,6,1,10,-1,-4,-9,8,-8,8,7,6,-3,-4,-7,4,6,-6,1,2,10,-10,-7,-10,9,7,-7,3,2,-4,4,2,5,6,-4,2,8,-5,-10,-8,-1,4,9,-10,7,-1,10,-2,3,-5,-8,-1,8,-9,-10,-5,5,-9,-9,7,-4,10,2,-3,9,2,-4,4,-10,2,4,-9,9,3,-10,5,-9,-8,-6,-7,-10,4,3,-7,3,-1,7,5,-1,-5,9,4,6,8,-4,8,-6,-9,-2,-2,-6,-3,-6,-10,-9,7,-4,7,-5,-3,-1,-3,3,8,8,4,4,6,8,-6,-8,6,-5,3,9,7,7,1,-1,9,8,3,9,-3,-5,5,-5,7,-5,8,-8,-5,6,-7,4,8,7,5,1,4,-10,-1,-9,5,-1,-7,-7,-4,-10,-3,6,6,5,3,3,3,-8,8,-5,3,-3,6,5,-6,10,-9,3,2,-9,3,2,-5,10,-10,-6,2,-3,3,10,-5,9,9,-1,9,5,4,-5,10,2,-4,-10,10,-7,-3,2,-7,2,-4,-6,3,-2,1,-5,7,-10,8,7,5,-2,-1,6,7,4,1,4,-3,2,-6,-6,8,3,-8,-5,6,-1,2,-7,-7,10,-2,5,-1,-1,6,9,5,-2,-2,-6,-6,7,8,9,-6,-3,-3,8,-7,-10,-8,9,-9,-6,9,9,-1,-7,2,-4,5,1,-8,-2,7,8,-1,9,-9,10,7,5,-8,8,-8,-10,-10,3,-7,-2,8,-10,-6,-6,-3,5,8,7,2,-5,8,5,4,7,-4,-8,9,-9,6,-2,-4,9,6,-7,1,-3,7,6,-6,5,-2,-10,10,9,-7,-6,-9,10,-3,6,-8,3,-6,9,4,4,4,8,-5,1,-8,-10,4,-4,8,-2,-8,-4,-8,10,4,7,-10,-3,1,-5,-4,8,7,-6,-2,3,-5,-8,-1,-2,-2,4,-5,-7,2,-7,-8,-4,-7,-2,-9,2,-6,-5,-9,-2,10,-5,3,-1,-3,-1,3,8,8,-10,-6,10,-3,9,-4,4,-6,-6,8,-8,-6,-4,6,1,-1,-8,-5,1,3,-1,2,2,-4,-9,-8,5,-5,4,-8,-5,8,-8,-4,-3,8,6,7,9,6,6,-6,9,10,5,10,9,-5,-3,5,-6,7,-2,-1,8,1,-3,-4,10,-6,4,-5,6,-7,9,-4,-4,10,-7,-8,-10,10,-6,8,10,1,1,-4,-5,5,-2,2,10,-3,3,-6,10,8,2,-4,-1,-8,-10,-9,-5,1,-3,-5,-5,10,10,2,-1,6,6,8,4,10,-10,10,-3,-3,6,-7,-6,2,4,6,4,-3,-3,-10,8,-10,8,4,-5,-8,-6,-3,-4,8,8,-7,5,7,-2,-2,8,1,-6,-7,-1,-1,2,9,10,5,-9,-2,-4,-10,-5,-9,8,1,2,-2,-3,-1,-8,10,-8,-8,9,1,9,2,-6,9,8,6,7,4,-3,-6,5,-1,-3,8,-8,-7,-10,3,7,-10,1,4,5,8,3,1,10,-9,-2,6,7,7,10,3,-1,4,-8,9,-8,-3,3,-9,9,-7,-6,-1,6,-2,9,8,10,-3,10,-2,-1,7,1,8,-5,-9,9,4,9,6,1,9,3,10,3,10,-8,-7,-5,9,1,-1,-1,10,2,9,9,7,-9,7,-2,6,-6,-1,10,-2,-9,3,-9,9,10,-7,7,1,2,9,-5,-3,10,3,-3,2,10,-1,10,-2,-9,7,4,1,-8,-1,-5,-7,8,6,-6,3,-4,5,-4,2,6,9,-1,-8,-1,3,1,3,-9,3,7,-1,2,-5,-1,-10,-8,8,9,8,3,8,-1,-5,3,-6,-6,1,1,2,5,-2,3,2,-4,-4,2,-2,6,-1,-5,-9,-4,-7,-6,-10,5,6,9,-9,-8,1,6,3,1,1,3,-7,10,-5,-6,-9,-6,-6,3,-10,-10,-1,4,-10,-7,1,1,-8,-3,-7,-7,-10,1,10,3,5,2,-4,9,1,5,8,1,4,9,3,-10,-1,-10,5,10,9,-7,8,6,-5,-3,-4,-1,8,-2,9,3,2,-8,7,8,-10,8,4,9,-3,-4,-5,-7,-8,4,-2,-7,2,-3,3,-4,8,-1,8,-4,2,-9,-7,-2,7,4,4,-4,-5,5,8,-1,5,-1,-3,1,-6,-4,9,10,1,7,-3,2,-10,8,-10,6,-2,-6,3,2,-10,-2,2,6,6,-9,-6,7,-1,4,3,-5,-9,3,10,3,4,2,-9,-1,4,2,-2,8,3,5,3,2,-2], dtype = "uint8")#candidate|6144|(2100,)|const|uint8
call_6143 = func_4093_call(relay.reshape(const_6144.astype('uint8'), [10, 14, 15]))
call_6145 = func_4093_call(relay.reshape(const_6144.astype('uint8'), [10, 14, 15]))
bop_6164 = relay.less_equal(bop_6137.astype('bool'), relay.reshape(bop_6133.astype('bool'), relay.shape_of(bop_6137))) # shape=(10, 2, 10)
uop_6170 = relay.log(bop_6137.astype('float32')) # shape=(10, 2, 10)
output = relay.Tuple([call_6143,const_6144,bop_6164,uop_6170,])
output2 = relay.Tuple([call_6145,const_6144,bop_6164,uop_6170,])
func_6179 = relay.Function([var_6131,var_6132,var_6136,], output)
mod['func_6179'] = func_6179
mod = relay.transform.InferType()(mod)
var_6180 = relay.var("var_6180", dtype = "int32", shape = (10, 2, 1))#candidate|6180|(10, 2, 1)|var|int32
var_6181 = relay.var("var_6181", dtype = "int32", shape = (10, 2, 10))#candidate|6181|(10, 2, 10)|var|int32
var_6182 = relay.var("var_6182", dtype = "int32", shape = (10, 2, 10))#candidate|6182|(10, 2, 10)|var|int32
output = func_6179(var_6180,var_6181,var_6182,)
func_6183 = relay.Function([var_6180,var_6181,var_6182,], output)
mutated_mod['func_6183'] = func_6183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mod.get_global_var('func_4530')
func_4532_call = mutated_mod.get_global_var('func_4532')
call_6212 = relay.TupleGetItem(func_4530_call(), 1)
call_6213 = relay.TupleGetItem(func_4532_call(), 1)
uop_6229 = relay.sigmoid(call_6212.astype('float32')) # shape=(16, 7, 1)
uop_6231 = relay.sigmoid(call_6213.astype('float32')) # shape=(16, 7, 1)
output = relay.Tuple([uop_6229,])
output2 = relay.Tuple([uop_6231,])
func_6239 = relay.Function([], output)
mod['func_6239'] = func_6239
mod = relay.transform.InferType()(mod)
output = func_6239()
func_6240 = relay.Function([], output)
mutated_mod['func_6240'] = func_6240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4303_call = mod.get_global_var('func_4303')
func_4304_call = mutated_mod.get_global_var('func_4304')
call_6241 = relay.TupleGetItem(func_4303_call(), 1)
call_6242 = relay.TupleGetItem(func_4304_call(), 1)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_6256 = func_3765_call()
call_6257 = func_3765_call()
func_3199_call = mod.get_global_var('func_3199')
func_3202_call = mutated_mod.get_global_var('func_3202')
const_6281 = relay.const(6, dtype = "int64")#candidate|6281|()|const|int64
var_6282 = relay.var("var_6282", dtype = "int64", shape = (125,))#candidate|6282|(125,)|var|int64
call_6280 = relay.TupleGetItem(func_3199_call(relay.reshape(const_6281.astype('int64'), []), relay.reshape(var_6282.astype('int64'), [5, 5, 5]), ), 0)
call_6283 = relay.TupleGetItem(func_3202_call(relay.reshape(const_6281.astype('int64'), []), relay.reshape(var_6282.astype('int64'), [5, 5, 5]), ), 0)
bop_6299 = relay.less(const_6281.astype('bool'), call_6241.astype('bool')) # shape=(15, 7, 6)
bop_6302 = relay.less(const_6281.astype('bool'), call_6242.astype('bool')) # shape=(15, 7, 6)
output = relay.Tuple([call_6256,call_6280,var_6282,bop_6299,])
output2 = relay.Tuple([call_6257,call_6283,var_6282,bop_6302,])
func_6308 = relay.Function([var_6282,], output)
mod['func_6308'] = func_6308
mod = relay.transform.InferType()(mod)
var_6309 = relay.var("var_6309", dtype = "int64", shape = (125,))#candidate|6309|(125,)|var|int64
output = func_6308(var_6309)
func_6310 = relay.Function([var_6309], output)
mutated_mod['func_6310'] = func_6310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3853_call = mod.get_global_var('func_3853')
func_3855_call = mutated_mod.get_global_var('func_3855')
call_6321 = func_3853_call()
call_6322 = func_3853_call()
func_3183_call = mod.get_global_var('func_3183')
func_3187_call = mutated_mod.get_global_var('func_3187')
const_6342 = relay.const([[8]], dtype = "int32")#candidate|6342|(1, 1)|const|int32
const_6343 = relay.const([3,-4,4,5,-1,-1,-4,4,-6,-8,-2,7,8,-9,-9,2,-8,-4,4,-8,-8,2,7,6,1,-8,4,8,1,8,-6,4,7,-8,7,-5,-6,7,-5,9,-6,10,4,-1,7,-7,-10,-9,-10,7,5,-2,-3,6,-3,-3], dtype = "int32")#candidate|6343|(56,)|const|int32
call_6341 = func_3183_call(relay.reshape(const_6342.astype('int32'), [1, 1, 1]), relay.reshape(const_6343.astype('int32'), [7, 1, 8]), )
call_6344 = func_3183_call(relay.reshape(const_6342.astype('int32'), [1, 1, 1]), relay.reshape(const_6343.astype('int32'), [7, 1, 8]), )
const_6347 = relay.const([[8],[-3],[5],[5],[6],[5],[8],[8]], dtype = "int32")#candidate|6347|(8, 1)|const|int32
bop_6348 = relay.less(const_6342.astype('bool'), const_6347.astype('bool')) # shape=(8, 1)
func_5335_call = mod.get_global_var('func_5335')
func_5338_call = mutated_mod.get_global_var('func_5338')
const_6391 = relay.const([-2.201347,-4.831549,8.358391,-2.375992,-9.204114,9.966567,-3.428722,0.160400,-8.640205,-8.092483,-7.045399,9.146526,9.455365,-6.268570,5.835765,4.806569,-7.737715,-0.745499,-1.550523,7.061489,-8.038680,-9.599779,-3.972641,5.416072,3.283141,7.303334,-0.322290,-9.410610,0.272491,-2.689822,-7.566774,-6.889376,-1.305434,-3.056964,9.145387,7.935108,-7.846463,3.193544,9.443131,7.037443,-7.052250,-6.530074,8.935926,-6.397490,-9.824617,9.908706,-4.562831,7.001336], dtype = "float64")#candidate|6391|(48,)|const|float64
call_6390 = relay.TupleGetItem(func_5335_call(relay.reshape(const_6391.astype('float64'), [4, 12])), 2)
call_6392 = relay.TupleGetItem(func_5338_call(relay.reshape(const_6391.astype('float64'), [4, 12])), 2)
func_4906_call = mod.get_global_var('func_4906')
func_4909_call = mutated_mod.get_global_var('func_4909')
call_6401 = relay.TupleGetItem(func_4906_call(relay.reshape(call_6321.astype('float64'), [11, 12, 15])), 0)
call_6402 = relay.TupleGetItem(func_4909_call(relay.reshape(call_6321.astype('float64'), [11, 12, 15])), 0)
output = relay.Tuple([call_6321,call_6341,const_6343,bop_6348,call_6390,const_6391,call_6401,])
output2 = relay.Tuple([call_6322,call_6344,const_6343,bop_6348,call_6392,const_6391,call_6402,])
func_6433 = relay.Function([], output)
mod['func_6433'] = func_6433
mod = relay.transform.InferType()(mod)
output = func_6433()
func_6434 = relay.Function([], output)
mutated_mod['func_6434'] = func_6434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4830_call = mod.get_global_var('func_4830')
func_4832_call = mutated_mod.get_global_var('func_4832')
call_6451 = relay.TupleGetItem(func_4830_call(), 3)
call_6452 = relay.TupleGetItem(func_4832_call(), 3)
output = call_6451
output2 = call_6452
func_6456 = relay.Function([], output)
mod['func_6456'] = func_6456
mod = relay.transform.InferType()(mod)
output = func_6456()
func_6457 = relay.Function([], output)
mutated_mod['func_6457'] = func_6457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5857_call = mod.get_global_var('func_5857')
func_5859_call = mutated_mod.get_global_var('func_5859')
call_6529 = relay.TupleGetItem(func_5857_call(), 3)
call_6530 = relay.TupleGetItem(func_5859_call(), 3)
output = call_6529
output2 = call_6530
func_6533 = relay.Function([], output)
mod['func_6533'] = func_6533
mod = relay.transform.InferType()(mod)
mutated_mod['func_6533'] = func_6533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6533_call = mutated_mod.get_global_var('func_6533')
call_6534 = func_6533_call()
output = call_6534
func_6535 = relay.Function([], output)
mutated_mod['func_6535'] = func_6535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5043_call = mod.get_global_var('func_5043')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_6544 = relay.TupleGetItem(func_5043_call(), 0)
call_6545 = relay.TupleGetItem(func_5044_call(), 0)
uop_6555 = relay.exp(call_6544.astype('float32')) # shape=(13, 13, 4)
uop_6557 = relay.exp(call_6545.astype('float32')) # shape=(13, 13, 4)
func_5022_call = mod.get_global_var('func_5022')
func_5024_call = mutated_mod.get_global_var('func_5024')
var_6559 = relay.var("var_6559", dtype = "float32", shape = (2112,))#candidate|6559|(2112,)|var|float32
call_6558 = relay.TupleGetItem(func_5022_call(relay.reshape(var_6559.astype('float32'), [12, 16, 11])), 3)
call_6560 = relay.TupleGetItem(func_5024_call(relay.reshape(var_6559.astype('float32'), [12, 16, 11])), 3)
func_5907_call = mod.get_global_var('func_5907')
func_5908_call = mutated_mod.get_global_var('func_5908')
call_6566 = relay.TupleGetItem(func_5907_call(), 0)
call_6567 = relay.TupleGetItem(func_5908_call(), 0)
bop_6573 = relay.logical_and(uop_6555.astype('bool'), relay.reshape(call_6544.astype('bool'), relay.shape_of(uop_6555))) # shape=(13, 13, 4)
bop_6576 = relay.logical_and(uop_6557.astype('bool'), relay.reshape(call_6545.astype('bool'), relay.shape_of(uop_6557))) # shape=(13, 13, 4)
output = relay.Tuple([call_6558,var_6559,call_6566,bop_6573,])
output2 = relay.Tuple([call_6560,var_6559,call_6567,bop_6576,])
func_6581 = relay.Function([var_6559,], output)
mod['func_6581'] = func_6581
mod = relay.transform.InferType()(mod)
mutated_mod['func_6581'] = func_6581
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6582 = relay.var("var_6582", dtype = "float32", shape = (2112,))#candidate|6582|(2112,)|var|float32
func_6581_call = mutated_mod.get_global_var('func_6581')
call_6583 = func_6581_call(var_6582)
output = call_6583
func_6584 = relay.Function([var_6582], output)
mutated_mod['func_6584'] = func_6584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3959_call = mod.get_global_var('func_3959')
func_3961_call = mutated_mod.get_global_var('func_3961')
call_6648 = relay.TupleGetItem(func_3959_call(), 0)
call_6649 = relay.TupleGetItem(func_3961_call(), 0)
output = relay.Tuple([call_6648,])
output2 = relay.Tuple([call_6649,])
func_6664 = relay.Function([], output)
mod['func_6664'] = func_6664
mod = relay.transform.InferType()(mod)
output = func_6664()
func_6665 = relay.Function([], output)
mutated_mod['func_6665'] = func_6665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4303_call = mod.get_global_var('func_4303')
func_4304_call = mutated_mod.get_global_var('func_4304')
call_6682 = relay.TupleGetItem(func_4303_call(), 0)
call_6683 = relay.TupleGetItem(func_4304_call(), 0)
func_4461_call = mod.get_global_var('func_4461')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_6694 = relay.TupleGetItem(func_4461_call(), 1)
call_6695 = relay.TupleGetItem(func_4462_call(), 1)
func_5564_call = mod.get_global_var('func_5564')
func_5566_call = mutated_mod.get_global_var('func_5566')
call_6696 = relay.TupleGetItem(func_5564_call(), 0)
call_6697 = relay.TupleGetItem(func_5566_call(), 0)
output = relay.Tuple([call_6682,call_6694,call_6696,])
output2 = relay.Tuple([call_6683,call_6695,call_6697,])
func_6706 = relay.Function([], output)
mod['func_6706'] = func_6706
mod = relay.transform.InferType()(mod)
output = func_6706()
func_6707 = relay.Function([], output)
mutated_mod['func_6707'] = func_6707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6071_call = mod.get_global_var('func_6071')
func_6072_call = mutated_mod.get_global_var('func_6072')
call_6708 = relay.TupleGetItem(func_6071_call(), 3)
call_6709 = relay.TupleGetItem(func_6072_call(), 3)
output = relay.Tuple([call_6708,])
output2 = relay.Tuple([call_6709,])
func_6712 = relay.Function([], output)
mod['func_6712'] = func_6712
mod = relay.transform.InferType()(mod)
output = func_6712()
func_6713 = relay.Function([], output)
mutated_mod['func_6713'] = func_6713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4830_call = mod.get_global_var('func_4830')
func_4832_call = mutated_mod.get_global_var('func_4832')
call_6732 = relay.TupleGetItem(func_4830_call(), 1)
call_6733 = relay.TupleGetItem(func_4832_call(), 1)
func_762_call = mod.get_global_var('func_762')
func_765_call = mutated_mod.get_global_var('func_765')
const_6735 = relay.const([-3.860113,4.236101,8.901581,-7.269505,-8.015513,6.198718,-9.400381,-2.533762,7.399390,8.355680,-0.169967,0.869624,6.486574,9.803735,-7.772861,7.596479,0.120927,-7.550507,5.448942,-4.175248,-7.672818,-9.047823,9.972259,-3.905879,0.900496,-0.928126,-2.989921,9.926849,5.048007,-2.162208,5.337048,-1.781036,-8.120540,-9.100822,-6.832490,3.259677,-5.908078,3.188201,-1.985118,-9.052318], dtype = "float64")#candidate|6735|(40,)|const|float64
const_6736 = relay.const([-2,-9,-4,-7,-7,9,-10,2,-6,2,4,10,1,-3,-2,-6,-7,-7,5,9,8,7,4,-3,-2,4,2,-7,-9,-7,-7,5,10,-6,-5,5,4,-1,-5,9,-1,5,-6,-8,3,7,-8,5,-6,3,5,-5,1,-7,2,4,-8,1,-1,10,6,-5,10,4,-10,-7,4,6,-10,2,1,-9,4,3,-1,-1,-10,1,8,-8,-2,-5,-9,-2,6,-2,1,-3,1,2,9,-9,2,1,-5,8,1,4,4,8,-1,6,4,-6,-5,9,4,5,9,-5,2,-2,9,-5,-3,5,-7,-5,-10,8,-9,-3,4,-8,3,-7,-9,2,-6,-4,-3,-2,-10,1,-8,-9,-3,-10,2,2,-3,2,10,1,2,7,-4,6,-6,8,-4,-2,1,6,10,-9,-6,7,9,-2,-5,8,9,-5,-1,-10,-2,-3,-4,4,-8,-9,8,-10,3,-7,2,8,-9,8,-8,6,1,-10,-2,-9,1,-5,-3,3,-1,-4,8,-6,-7,-9,-3,2,8,-8,-8,1,6,-6,4,-3,-2,8,9,8,-10,-10,4,8,-3,2,-5,9,-10,-10,-6,7,-10,-9,1,-6,4,4,7,10,10,1,3,-9,-7,-7,-2,3,1,4,1,3,-5,5,-2,-1,-5,10,-2,-2,7,-4,-6,-2,10,9,5,1,10,3,-1,4,7,-7,-4,10,10,4,-10,3,2,3,5,-9,-10,-6,-7,8,-6,-4,3,6,7,-7,4,-9,1,6,-6,10,-7,6,9,-9,8,-9,-9,-4,3,-5,3,-7,-6,10,-8,-9,-9,9,10,6,3,-8,-10,-1,4,-2,-2,1,2,1,4,-4,-6,4,3,1,-7,8,-1,-2,9,-4,-5,-10,-8,6,10,8,7,1,4,-5,10,10,-6,-10,8,-3,-9,-9,-3,-1,-9,10,-3,-5,2,-7,5,8,10,4,10,-1,10,7,7,8,-7,9,1,8,-3,-8,2,8,1,-2,-1,9,-10,-7,-4,-2,-5,-2,6,10,7,-8,1,3,-9,-3,5,-2,-10,-4,5,-7,9,-7,-1,4,2,-7,9,-4,-6,-9,-3,-7,-1,9,-7,6,-10,-10,-7,-9,6,3,9,-6,-8,-5,7,6,-3,3,3,-7,-4,4,-3,2,2,-7,-3,-5,5,4,1,1,4,5,5,10,9,3,-8,1,10,-10,-10,-6,6,8,-7,-1,-5,8,-8,-1,2,-9,9,-10,-8,2,7,3,-7,1,2,-4,-10,-6,1,-3,9,3,2,7,-6,-9,8,-8,-5,-8,3,-3,-6,-9,-4,2,-6,3,10,9,-8,9,-2,-10,6,-5,2,1,-5,-7,-5,-4,5,7,7,1,6,-1,7,-7,-9,-3,8,-9,4,-6,6,-8,-7,-6,4,-10,-7,9,4,10,-6,-4,-9,-1,-10,2,7,7,-8,8,2,10,-3,-5,5,-10,-10,-7,-1,2,3,9,5,-6,1,-4,-4,-4,5,5,7,-9,2,-6,4,6,1,9,-3,8,9,-9,-8,1,2,-1,3,-8,8,10,9,1,-1,-7,-5,10,-8,-8,-4,10,-7,7,-3,-5,-6,-4,10,6,-6,-8,7,-5,-9,-3,-4,-8,-6,-2,-9,-1,-1,3,-8,3,-3,5,8,-7,4,7,3,-2,-2,7], dtype = "int64")#candidate|6736|(630,)|const|int64
call_6734 = relay.TupleGetItem(func_762_call(relay.reshape(const_6735.astype('float64'), [4, 1, 10]), relay.reshape(const_6736.astype('int64'), [630,]), ), 2)
call_6737 = relay.TupleGetItem(func_765_call(relay.reshape(const_6735.astype('float64'), [4, 1, 10]), relay.reshape(const_6736.astype('int64'), [630,]), ), 2)
output = relay.Tuple([call_6732,call_6734,const_6735,const_6736,])
output2 = relay.Tuple([call_6733,call_6737,const_6735,const_6736,])
func_6738 = relay.Function([], output)
mod['func_6738'] = func_6738
mod = relay.transform.InferType()(mod)
mutated_mod['func_6738'] = func_6738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6738_call = mutated_mod.get_global_var('func_6738')
call_6739 = func_6738_call()
output = call_6739
func_6740 = relay.Function([], output)
mutated_mod['func_6740'] = func_6740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3903_call = mod.get_global_var('func_3903')
func_3904_call = mutated_mod.get_global_var('func_3904')
call_6741 = func_3903_call()
call_6742 = func_3903_call()
output = call_6741
output2 = call_6742
func_6743 = relay.Function([], output)
mod['func_6743'] = func_6743
mod = relay.transform.InferType()(mod)
output = func_6743()
func_6744 = relay.Function([], output)
mutated_mod['func_6744'] = func_6744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4461_call = mod.get_global_var('func_4461')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_6753 = relay.TupleGetItem(func_4461_call(), 0)
call_6754 = relay.TupleGetItem(func_4462_call(), 0)
func_5280_call = mod.get_global_var('func_5280')
func_5281_call = mutated_mod.get_global_var('func_5281')
call_6755 = relay.TupleGetItem(func_5280_call(), 1)
call_6756 = relay.TupleGetItem(func_5281_call(), 1)
output = relay.Tuple([call_6753,call_6755,])
output2 = relay.Tuple([call_6754,call_6756,])
func_6762 = relay.Function([], output)
mod['func_6762'] = func_6762
mod = relay.transform.InferType()(mod)
mutated_mod['func_6762'] = func_6762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6762_call = mutated_mod.get_global_var('func_6762')
call_6763 = func_6762_call()
output = call_6763
func_6764 = relay.Function([], output)
mutated_mod['func_6764'] = func_6764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6762_call = mod.get_global_var('func_6762')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_6765 = relay.TupleGetItem(func_6762_call(), 0)
call_6766 = relay.TupleGetItem(func_6764_call(), 0)
func_3903_call = mod.get_global_var('func_3903')
func_3904_call = mutated_mod.get_global_var('func_3904')
call_6783 = func_3903_call()
call_6784 = func_3903_call()
func_3674_call = mod.get_global_var('func_3674')
func_3678_call = mutated_mod.get_global_var('func_3678')
var_6790 = relay.var("var_6790", dtype = "float32", shape = (36, 1))#candidate|6790|(36, 1)|var|float32
const_6791 = relay.const([-3.834755,6.006167,-0.656776,-1.267823,-6.175023,4.739148,-6.519009,0.637891,1.550601,-9.795883,6.701670,-2.805026,0.943737,0.200946,1.802246,-3.832825,5.690045,3.648911,8.000288,6.051470,-4.005023,-8.375949,-7.974908,-0.608707,7.809949,-6.043783,3.568183,4.697569,9.258118,4.064941,-5.514555,-1.756755,6.033502,-2.971759,4.916132,-2.143018,-0.663843,-2.841169,9.529103,-5.102366,-4.860300,9.266933,0.555339,-0.529798,2.512649,-3.900699,-4.604963,1.183800], dtype = "float64")#candidate|6791|(48,)|const|float64
call_6789 = relay.TupleGetItem(func_3674_call(relay.reshape(var_6790.astype('float32'), [1, 6, 6]), relay.reshape(const_6791.astype('float64'), [48,]), ), 8)
call_6792 = relay.TupleGetItem(func_3678_call(relay.reshape(var_6790.astype('float32'), [1, 6, 6]), relay.reshape(const_6791.astype('float64'), [48,]), ), 8)
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_6793 = func_4070_call()
call_6794 = func_4070_call()
func_4273_call = mod.get_global_var('func_4273')
func_4278_call = mutated_mod.get_global_var('func_4278')
var_6797 = relay.var("var_6797", dtype = "int16", shape = (1540,))#candidate|6797|(1540,)|var|int16
call_6796 = relay.TupleGetItem(func_4273_call(relay.reshape(call_6765.astype('float64'), [11, 12, 15]), relay.reshape(call_6793.astype('float64'), [11, 12, 15]), relay.reshape(var_6797.astype('int16'), [1540,]), ), 1)
call_6798 = relay.TupleGetItem(func_4278_call(relay.reshape(call_6765.astype('float64'), [11, 12, 15]), relay.reshape(call_6793.astype('float64'), [11, 12, 15]), relay.reshape(var_6797.astype('int16'), [1540,]), ), 1)
output = relay.Tuple([call_6765,call_6783,call_6789,var_6790,const_6791,call_6793,call_6796,var_6797,])
output2 = relay.Tuple([call_6766,call_6784,call_6792,var_6790,const_6791,call_6794,call_6798,var_6797,])
func_6799 = relay.Function([var_6790,var_6797,], output)
mod['func_6799'] = func_6799
mod = relay.transform.InferType()(mod)
mutated_mod['func_6799'] = func_6799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6799_call = mutated_mod.get_global_var('func_6799')
var_6801 = relay.var("var_6801", dtype = "float32", shape = (36, 1))#candidate|6801|(36, 1)|var|float32
var_6802 = relay.var("var_6802", dtype = "int16", shape = (1540,))#candidate|6802|(1540,)|var|int16
call_6800 = func_6799_call(var_6801,var_6802,)
output = call_6800
func_6803 = relay.Function([var_6801,var_6802,], output)
mutated_mod['func_6803'] = func_6803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5043_call = mod.get_global_var('func_5043')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_6874 = relay.TupleGetItem(func_5043_call(), 0)
call_6875 = relay.TupleGetItem(func_5044_call(), 0)
func_6799_call = mod.get_global_var('func_6799')
func_6803_call = mutated_mod.get_global_var('func_6803')
const_6897 = relay.const([-1.664578,0.867260,-0.455224,1.300940,7.667644,1.088143,-7.807177,2.623417,-2.751153,7.786970,-1.479373,1.556010,-6.794789,6.921750,-3.197248,-3.362952,-4.333859,-7.449921,0.237513,0.797641,-5.201034,2.464631,4.829466,-8.757985,7.707132,-8.280908,9.432600,-9.809892,6.467635,1.383247,-0.081643,1.888910,-6.945664,4.308693,3.967510,-3.614511], dtype = "float32")#candidate|6897|(36,)|const|float32
const_6898 = relay.const([[4,-4],[10,1],[6,-8],[-8,9],[-10,-9],[5,5],[-4,-1],[-4,-10],[8,-1],[-5,8],[2,8],[-10,-9],[4,-1],[5,10],[-2,-2],[5,7],[5,-4],[8,6],[10,9],[3,-10],[-5,-3],[-7,-10],[5,7],[3,7],[-10,2],[3,-10],[-2,-2],[-9,9],[3,4],[6,-1],[5,4],[10,8],[10,-1],[-8,5],[10,-2],[-8,-10],[-4,3],[10,10],[1,-5],[-5,2],[5,-8],[4,10],[1,-10],[-4,1],[7,-5],[-9,-4],[10,1],[2,-3],[-9,-7],[-4,-7],[-10,5],[-9,1],[2,5],[-4,-2],[-6,-2],[-8,-5],[-5,2],[-3,6],[5,-9],[-8,10],[-8,-3],[-4,9],[-10,8],[5,7],[-10,-1],[7,6],[1,-6],[-4,10],[1,-6],[-10,5],[-5,6],[-8,2],[-1,1],[-4,-9],[10,3],[2,-8],[9,-8],[-9,7],[-5,6],[9,5],[2,-9],[1,-1],[-3,-9],[-8,-10],[2,-7],[10,-5],[-8,-2],[8,6],[-1,8],[3,7],[2,3],[-2,10],[-10,5],[1,-6],[-2,8],[6,-1],[1,3],[9,-1],[3,-4],[6,8],[-10,-5],[4,4],[10,7],[-9,4],[-8,-5],[-6,-9],[-2,-3],[6,4],[6,-7],[-3,-8],[4,-10],[4,3],[1,-10],[-6,-6],[-1,-7],[-4,-2],[-10,-5],[-1,-7],[-6,8],[-3,3],[-10,-2],[1,5],[1,-10],[-4,-7],[1,-9],[-3,-7],[-3,1],[7,9],[7,6],[-1,2],[4,5],[4,2],[4,-10],[-8,-7],[4,-7],[2,-2],[9,-8],[10,10],[-4,2],[9,-3],[-7,-9],[10,8],[-6,6],[-4,6],[6,-4],[6,10],[1,7],[-8,-2],[-3,-2],[8,8],[-8,1],[-5,-5],[-5,-7],[3,2],[-9,-1],[-1,-2],[7,-9],[5,-9],[6,-4],[1,1],[-8,-6],[6,-2],[-8,2],[7,4],[-9,9],[4,8],[9,8],[1,5],[-10,8],[-10,-10],[3,-6],[7,4],[-6,-1],[-2,8],[-1,3],[-10,1],[1,5],[-10,-8],[7,5],[7,-2],[-6,-1],[2,-2],[-10,4],[5,-7],[5,-8],[6,-1],[-1,9],[-8,10],[3,-4],[3,-7],[1,10],[-7,2],[8,10],[-5,9],[7,-5],[8,-1],[-9,4],[-9,4],[2,-7],[2,2],[1,-5],[3,6],[1,-5],[7,8],[8,-9],[-4,-10],[8,7],[9,1],[3,8],[-10,-4],[-6,-10],[2,8],[-9,-1],[-9,-1],[-8,-8],[-10,-7],[-4,7],[-9,-7],[-1,-5],[-4,-4],[-1,7],[-4,8],[7,-9],[2,-9],[10,4],[-8,-2],[7,-3],[4,5],[-2,5],[1,10],[-9,6],[-4,10],[1,-3],[7,8],[-5,-7],[8,-4],[4,-8],[5,6],[6,5],[-5,6],[-3,4],[6,-3],[3,-2],[2,3],[7,3],[-9,6],[-9,7],[-10,-9],[-4,10],[-7,5],[-5,-2],[4,2],[-5,7],[-4,-1],[-6,8],[-5,-8],[3,3],[4,-9],[6,3],[5,5],[-2,5],[-5,-10],[9,8],[8,5],[7,9],[-3,-8],[10,-10],[1,-6],[-8,-9],[-9,6],[1,-4],[-2,-10],[4,-10],[-10,7],[-2,-4],[2,5],[2,3],[-7,1],[-2,8],[-3,-3],[-2,5],[1,-3],[-1,-7],[-8,5],[10,-1],[-6,4],[-9,-4],[-3,-9],[-7,-8],[-8,-3],[-9,-4],[-5,-6],[8,10],[2,-5],[-8,-5],[-5,-7],[-1,-3],[5,10],[6,-10],[-4,4],[4,9],[1,8],[1,2],[8,-8],[-6,9],[-7,-5],[4,6],[2,3],[5,3],[-4,-7],[4,10],[-1,-2],[1,8],[2,-3],[-9,-6],[10,-6],[-1,-2],[9,9],[1,5],[2,-8],[-1,-3],[10,-9],[6,9],[-5,2],[3,1],[5,5],[-3,-7],[10,-8],[-2,3],[-8,10],[-10,-1],[-3,10],[-10,9],[-5,1],[-7,-1],[-4,9],[1,-7],[-6,6],[-5,10],[-1,-7],[5,6],[2,-6],[-8,7],[7,7],[2,10],[10,-4],[2,-6],[-8,5],[8,-3],[-9,-1],[-7,8],[-8,3],[-10,8],[8,6],[9,2],[6,1],[9,6],[5,6],[8,8],[-10,4],[6,9],[-7,4],[8,3],[3,9],[2,-3],[-3,-8],[4,6],[9,-1],[5,6],[4,8],[-6,-7],[-7,-5],[10,-5],[-9,-5],[-1,7],[3,2],[8,8],[10,8],[-6,-6],[-9,-3],[1,3],[1,2],[-9,1],[-7,-9],[-2,10],[2,-9],[1,3],[-8,-1],[4,-8],[-4,-8],[-9,6],[-3,2],[-2,9],[-10,-4],[6,1],[4,3],[-7,-5],[-3,-5],[-4,-8],[-6,4],[3,-1],[4,4],[-3,-3],[8,-4],[-1,6],[-4,6],[-2,6],[-5,5],[4,10],[1,9],[8,10],[-2,-1],[-5,-6],[-7,-8],[-7,6],[-5,-1],[-7,8],[-3,-2],[10,7],[8,4],[-4,-6],[-3,10],[1,3],[7,4],[2,-3],[-10,6],[-9,-2],[10,2],[-4,-4],[5,6],[-2,-1],[-2,-4],[-8,1],[-2,-7],[-1,-9],[5,-4],[-2,-8],[4,2],[-5,-4],[7,-1],[-5,-4],[-1,-9],[2,-3],[9,-7],[-6,7],[-1,6],[1,2],[8,-4],[8,-1],[1,-1],[-5,-1],[2,5],[-3,9],[-1,-1],[-5,-2],[-6,5],[6,-3],[5,1],[8,6],[10,-1],[-4,-10],[-5,9],[1,2],[-10,3],[2,-5],[2,9],[-10,4],[-6,4],[3,-7],[2,-8],[-9,-4],[7,5],[5,-8],[-5,-1],[-2,4],[7,-10],[-1,-9],[-6,10],[9,-2],[-1,-10],[6,7],[7,-6],[-10,8],[8,10],[-6,-4],[7,-8],[8,-5],[-9,-7],[-2,-6],[-2,-7],[3,-2],[5,2],[-2,-6],[2,7],[5,1],[8,-9],[-4,-1],[-9,1],[-6,-5],[-4,2],[7,6],[1,-1],[7,2],[-10,6],[-6,-10],[-7,-7],[5,-2],[10,4],[-2,-7],[4,-1],[10,6],[4,5],[1,5],[8,1],[-5,-2],[-8,4],[-9,-5],[1,-5],[9,2],[-7,3],[2,-8],[-1,6],[5,-5],[-6,-5],[2,-9],[-7,-3],[-8,-10],[-9,5],[-3,6],[1,4],[-9,10],[-7,-2],[4,1],[8,8],[6,2],[-2,-9],[-9,1],[-6,-7],[3,2],[-10,-1],[6,8],[6,9],[-5,-9],[8,-4],[-4,7],[1,7],[-1,7],[3,-8],[2,10],[-1,1],[-2,4],[10,-6],[-4,-6],[-1,8],[2,-3],[-3,-4],[8,-4],[5,-8],[-8,6],[10,-4],[-9,9],[3,-1],[-5,10],[7,5],[-7,8],[-4,10],[7,-2],[10,-3],[-6,10],[-10,-4],[5,-2],[-9,-2],[6,10],[-4,-4],[8,2],[-1,8],[5,-7],[-9,9],[9,10],[10,6],[-2,8],[7,-9],[-9,3],[-5,-9],[1,5],[-1,3],[8,7],[5,-4],[2,-3],[3,5],[2,-3],[-1,7],[-2,-1],[9,-2],[9,-4],[5,-9],[9,7],[5,-5],[-10,-6],[-5,-4],[-7,10],[10,4],[-1,4],[-6,4],[-7,9],[-3,-1],[-5,5],[-1,-8],[5,-4],[-8,-6],[7,-9],[-7,8],[2,-7],[2,-7],[6,8],[2,-6],[4,5],[10,-2],[-3,10],[2,3],[-5,-10],[-10,-7],[-10,6],[1,-10],[-3,8],[6,10],[1,-1],[-10,-10],[7,-4],[-6,7],[-6,-7],[-4,3],[-1,3],[-10,-9],[3,-5],[-6,-7],[-4,2],[-2,5],[2,4],[-6,3],[9,-5],[9,10],[-3,6],[-2,2],[6,6],[-3,-5],[-3,-10],[7,6],[-1,4],[4,3],[-1,-9],[-4,8],[5,7],[7,2],[2,-8],[-5,-4],[5,8],[4,-1],[10,9],[-10,-3],[3,4],[9,-9],[-10,-9],[-1,-3],[5,-10],[-1,-5],[2,5],[10,-9],[-6,-6],[-1,-8],[-2,-5],[-4,-3],[-10,-7],[7,-1],[5,-1],[6,2],[4,-8],[1,-5],[-7,-9],[-1,-9],[9,-1],[7,3],[10,8],[3,7],[-6,-4],[5,3],[2,-10],[-8,3],[6,-2],[-5,-6],[1,2],[-4,3],[6,-10],[-7,-2],[6,-1],[2,2],[7,10],[10,-9],[-1,-5],[10,8],[5,8],[2,-8],[-3,-5],[-2,-2],[10,1],[1,1],[10,9],[-5,-9],[-5,-10],[-8,-7],[7,7],[-8,6],[-4,-10],[-6,-7],[8,-8],[2,-1],[6,-4],[-10,-7],[-5,-4],[-5,1],[-9,4],[-1,-4],[6,-9],[-1,5],[-2,4],[-2,-8],[-7,-7],[5,2],[10,-1],[-7,-9],[-1,1],[-1,-1],[-5,-6],[6,-1],[-6,-5],[-10,-5],[5,1],[-3,6],[1,5],[-4,-8],[1,-6],[-5,10],[-7,2],[-4,-8],[-3,2],[9,7],[5,-5],[-8,8],[4,6],[2,3],[-3,-7],[-2,-7],[-5,-10],[-8,6],[10,-4],[2,-6],[7,10],[-8,-9],[7,-9],[2,-5],[-6,1],[3,9],[1,-10],[7,-1],[-9,-6],[-3,-7],[2,1],[-3,-2],[3,-3],[3,10]], dtype = "int16")#candidate|6898|(770, 2)|const|int16
call_6896 = relay.TupleGetItem(func_6799_call(relay.reshape(const_6897.astype('float32'), [36, 1]), relay.reshape(const_6898.astype('int16'), [1540,]), ), 1)
call_6899 = relay.TupleGetItem(func_6803_call(relay.reshape(const_6897.astype('float32'), [36, 1]), relay.reshape(const_6898.astype('int16'), [1540,]), ), 1)
func_5907_call = mod.get_global_var('func_5907')
func_5908_call = mutated_mod.get_global_var('func_5908')
call_6912 = relay.TupleGetItem(func_5907_call(), 0)
call_6913 = relay.TupleGetItem(func_5908_call(), 0)
output = relay.Tuple([call_6874,call_6896,const_6897,const_6898,call_6912,])
output2 = relay.Tuple([call_6875,call_6899,const_6897,const_6898,call_6913,])
func_6922 = relay.Function([], output)
mod['func_6922'] = func_6922
mod = relay.transform.InferType()(mod)
mutated_mod['func_6922'] = func_6922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mutated_mod.get_global_var('func_6922')
call_6923 = func_6922_call()
output = call_6923
func_6924 = relay.Function([], output)
mutated_mod['func_6924'] = func_6924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mod.get_global_var('func_4149')
func_4151_call = mutated_mod.get_global_var('func_4151')
call_6942 = func_4149_call()
call_6943 = func_4149_call()
func_4303_call = mod.get_global_var('func_4303')
func_4304_call = mutated_mod.get_global_var('func_4304')
call_6966 = relay.TupleGetItem(func_4303_call(), 2)
call_6967 = relay.TupleGetItem(func_4304_call(), 2)
var_6968 = relay.var("var_6968", dtype = "float64", shape = (11, 12, 15))#candidate|6968|(11, 12, 15)|var|float64
bop_6969 = relay.logical_and(call_6942.astype('bool'), relay.reshape(var_6968.astype('bool'), relay.shape_of(call_6942))) # shape=(11, 12, 15)
bop_6972 = relay.logical_and(call_6943.astype('bool'), relay.reshape(var_6968.astype('bool'), relay.shape_of(call_6943))) # shape=(11, 12, 15)
func_1964_call = mod.get_global_var('func_1964')
func_1966_call = mutated_mod.get_global_var('func_1966')
const_7015 = relay.const([[10],[-6],[10],[-4],[6],[-9],[9],[8],[-9],[2],[-4],[-7],[-5],[-8],[-4],[-3],[-6],[3],[-5],[-6],[-4],[9],[-6],[-3],[-1],[-10],[7],[2],[6],[4],[-10],[4],[-6],[-2],[2],[9],[-5],[-9],[-5],[-6],[7],[-9],[-5],[-6],[-1],[-9],[-7],[-9],[-10],[3],[-10],[-9],[-3],[6],[1],[4],[9],[-2],[-6],[-3],[9],[10],[-7],[-1],[9],[-10],[-10],[-4],[7],[1],[-1],[6],[10],[-4],[6],[-3],[-3],[3],[1],[8],[1],[9],[-5],[2],[-2],[-10],[10],[4],[-3],[6],[8],[-4],[-4],[1],[-4],[3],[7],[5],[-4],[5],[-2],[8],[-2],[1],[3],[-7],[-9],[-1],[10],[6],[3],[9],[3],[5],[5],[-3],[7],[-8],[-6],[-6]], dtype = "int8")#candidate|7015|(120, 1)|const|int8
call_7014 = relay.TupleGetItem(func_1964_call(relay.reshape(const_7015.astype('int8'), [2, 6, 10])), 0)
call_7016 = relay.TupleGetItem(func_1966_call(relay.reshape(const_7015.astype('int8'), [2, 6, 10])), 0)
output = relay.Tuple([call_6966,bop_6969,call_7014,const_7015,])
output2 = relay.Tuple([call_6967,bop_6972,call_7016,const_7015,])
func_7018 = relay.Function([var_6968,], output)
mod['func_7018'] = func_7018
mod = relay.transform.InferType()(mod)
var_7019 = relay.var("var_7019", dtype = "float64", shape = (11, 12, 15))#candidate|7019|(11, 12, 15)|var|float64
output = func_7018(var_7019)
func_7020 = relay.Function([var_7019], output)
mutated_mod['func_7020'] = func_7020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mod.get_global_var('func_6922')
func_6924_call = mutated_mod.get_global_var('func_6924')
call_7101 = relay.TupleGetItem(func_6922_call(), 4)
call_7102 = relay.TupleGetItem(func_6924_call(), 4)
func_6738_call = mod.get_global_var('func_6738')
func_6740_call = mutated_mod.get_global_var('func_6740')
call_7110 = relay.TupleGetItem(func_6738_call(), 0)
call_7111 = relay.TupleGetItem(func_6740_call(), 0)
func_3959_call = mod.get_global_var('func_3959')
func_3961_call = mutated_mod.get_global_var('func_3961')
call_7112 = relay.TupleGetItem(func_3959_call(), 0)
call_7113 = relay.TupleGetItem(func_3961_call(), 0)
output = relay.Tuple([call_7101,call_7110,call_7112,])
output2 = relay.Tuple([call_7102,call_7111,call_7113,])
func_7114 = relay.Function([], output)
mod['func_7114'] = func_7114
mod = relay.transform.InferType()(mod)
mutated_mod['func_7114'] = func_7114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7114_call = mutated_mod.get_global_var('func_7114')
call_7115 = func_7114_call()
output = call_7115
func_7116 = relay.Function([], output)
mutated_mod['func_7116'] = func_7116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6664_call = mod.get_global_var('func_6664')
func_6665_call = mutated_mod.get_global_var('func_6665')
call_7236 = relay.TupleGetItem(func_6664_call(), 0)
call_7237 = relay.TupleGetItem(func_6665_call(), 0)
output = call_7236
output2 = call_7237
func_7238 = relay.Function([], output)
mod['func_7238'] = func_7238
mod = relay.transform.InferType()(mod)
mutated_mod['func_7238'] = func_7238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7238_call = mutated_mod.get_global_var('func_7238')
call_7239 = func_7238_call()
output = call_7239
func_7240 = relay.Function([], output)
mutated_mod['func_7240'] = func_7240
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7282 = relay.var("var_7282", dtype = "float64", shape = ())#candidate|7282|()|var|float64
var_7283 = relay.var("var_7283", dtype = "float64", shape = (2, 5, 6))#candidate|7283|(2, 5, 6)|var|float64
bop_7284 = relay.floor_divide(var_7282.astype('float64'), var_7283.astype('float64')) # shape=(2, 5, 6)
output = relay.Tuple([bop_7284,])
output2 = relay.Tuple([bop_7284,])
func_7307 = relay.Function([var_7282,var_7283,], output)
mod['func_7307'] = func_7307
mod = relay.transform.InferType()(mod)
mutated_mod['func_7307'] = func_7307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7307_call = mutated_mod.get_global_var('func_7307')
var_7309 = relay.var("var_7309", dtype = "float64", shape = ())#candidate|7309|()|var|float64
var_7310 = relay.var("var_7310", dtype = "float64", shape = (2, 5, 6))#candidate|7310|(2, 5, 6)|var|float64
call_7308 = func_7307_call(var_7309,var_7310,)
output = call_7308
func_7311 = relay.Function([var_7309,var_7310,], output)
mutated_mod['func_7311'] = func_7311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_7366 = relay.TupleGetItem(func_3714_call(), 0)
call_7367 = relay.TupleGetItem(func_3716_call(), 0)
uop_7379 = relay.sinh(call_7366.astype('float32')) # shape=(11, 12, 15)
uop_7381 = relay.sinh(call_7367.astype('float32')) # shape=(11, 12, 15)
func_6004_call = mod.get_global_var('func_6004')
func_6005_call = mutated_mod.get_global_var('func_6005')
call_7394 = func_6004_call()
call_7395 = func_6004_call()
output = relay.Tuple([uop_7379,call_7394,])
output2 = relay.Tuple([uop_7381,call_7395,])
func_7420 = relay.Function([], output)
mod['func_7420'] = func_7420
mod = relay.transform.InferType()(mod)
mutated_mod['func_7420'] = func_7420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7420_call = mutated_mod.get_global_var('func_7420')
call_7421 = func_7420_call()
output = call_7421
func_7422 = relay.Function([], output)
mutated_mod['func_7422'] = func_7422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_7444 = func_4070_call()
call_7445 = func_4070_call()
func_6071_call = mod.get_global_var('func_6071')
func_6072_call = mutated_mod.get_global_var('func_6072')
call_7479 = relay.TupleGetItem(func_6071_call(), 3)
call_7480 = relay.TupleGetItem(func_6072_call(), 3)
output = relay.Tuple([call_7444,call_7479,])
output2 = relay.Tuple([call_7445,call_7480,])
func_7500 = relay.Function([], output)
mod['func_7500'] = func_7500
mod = relay.transform.InferType()(mod)
mutated_mod['func_7500'] = func_7500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7500_call = mutated_mod.get_global_var('func_7500')
call_7501 = func_7500_call()
output = call_7501
func_7502 = relay.Function([], output)
mutated_mod['func_7502'] = func_7502
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7514 = relay.var("var_7514", dtype = "float32", shape = (10, 2, 9))#candidate|7514|(10, 2, 9)|var|float32
uop_7515 = relay.atan(var_7514.astype('float32')) # shape=(10, 2, 9)
bop_7518 = relay.subtract(var_7514.astype('float64'), relay.reshape(uop_7515.astype('float64'), relay.shape_of(var_7514))) # shape=(10, 2, 9)
output = bop_7518
output2 = bop_7518
func_7522 = relay.Function([var_7514,], output)
mod['func_7522'] = func_7522
mod = relay.transform.InferType()(mod)
var_7523 = relay.var("var_7523", dtype = "float32", shape = (10, 2, 9))#candidate|7523|(10, 2, 9)|var|float32
output = func_7522(var_7523)
func_7524 = relay.Function([var_7523], output)
mutated_mod['func_7524'] = func_7524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6743_call = mod.get_global_var('func_6743')
func_6744_call = mutated_mod.get_global_var('func_6744')
call_7568 = func_6743_call()
call_7569 = func_6743_call()
output = relay.Tuple([call_7568,])
output2 = relay.Tuple([call_7569,])
func_7579 = relay.Function([], output)
mod['func_7579'] = func_7579
mod = relay.transform.InferType()(mod)
output = func_7579()
func_7580 = relay.Function([], output)
mutated_mod['func_7580'] = func_7580
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7584 = relay.const([[[9.284377,-6.151938,-1.382586,6.788226,1.321420,8.987020,-9.540376,-2.025935,7.022713],[8.265773,-7.420319,-9.822335,-3.412568,-4.034310,-0.886079,-2.362797,-7.147771,-0.639002],[5.565186,6.260306,9.358304,7.301476,8.840541,-7.147328,-0.454729,2.524788,1.330789],[-2.495013,9.948478,9.960795,-1.139898,1.310801,-8.834683,-7.746044,-0.342211,-7.455737],[-3.907624,2.356990,-9.315439,1.782883,8.083465,1.991487,-7.080561,4.741228,-9.223452]],[[0.974134,-8.612451,4.832942,-0.943485,-0.990180,9.812690,-4.678457,-6.213995,4.218001],[1.739640,3.888435,5.635108,0.741356,8.271411,-7.226117,-8.805558,-7.523036,-3.582200],[2.378530,5.353090,3.626291,1.651465,2.549250,8.881853,-6.618095,4.509197,-6.694429],[-2.807414,-9.628724,-9.993708,1.021699,-3.242145,7.330401,6.523795,9.362937,-8.928477],[-7.507726,-0.250172,0.661143,-2.646874,0.537292,9.070632,8.779802,1.142683,7.374294]],[[-5.206629,-9.380507,2.436954,0.468071,7.019926,1.537064,-3.441507,5.973389,2.887234],[-7.172609,-3.392799,0.733230,3.328564,1.542861,-3.329650,-5.779189,8.028126,2.528910],[-6.507838,8.302130,6.141287,8.783941,-3.201949,3.537985,3.195266,-9.213676,7.206725],[-8.240846,-6.991126,7.563516,-6.323135,3.509407,3.232647,-7.997951,5.114006,0.269041],[0.489823,-1.036407,8.763357,4.282572,-7.385741,-0.604383,-3.903030,-4.666844,-5.766491]],[[1.141952,-8.069840,-6.854139,-6.795284,2.079310,-4.705976,-1.730641,-3.052849,-5.768746],[-3.733158,-7.137089,0.834578,-2.084305,0.105959,-1.281736,2.754269,4.613165,-5.096161],[1.695312,-4.008007,-3.343540,5.865332,-1.157056,-1.672329,6.322883,2.746972,2.308921],[-4.376284,-8.831206,-8.745534,7.848517,-5.212383,9.802079,-4.992212,6.470550,-9.997169],[0.254391,9.838989,5.872330,-3.818193,-0.276932,-3.444860,-6.744376,-2.827818,9.492216]],[[2.447419,-4.486467,3.484751,-4.986730,-6.076784,-0.284162,-7.193159,-9.400594,-9.560874],[3.214655,-5.206868,-7.526945,7.012655,9.050325,5.607983,-5.664927,1.292106,-1.633269],[5.852447,-9.492127,6.536145,-7.257414,-8.600895,0.649800,-8.355218,-0.726508,-6.336650],[7.112046,2.497320,3.175072,0.536352,-6.405124,-9.639003,6.880597,4.147244,4.501081],[3.995491,-7.347859,-2.936581,-7.095485,-5.518302,5.810561,4.673683,-8.197144,3.622456]]], dtype = "float64")#candidate|7584|(5, 5, 9)|const|float64
uop_7585 = relay.sqrt(const_7584.astype('float64')) # shape=(5, 5, 9)
func_5716_call = mod.get_global_var('func_5716')
func_5718_call = mutated_mod.get_global_var('func_5718')
const_7592 = relay.const([-3,-8,-2,6,-1,6,10,3,-3,-5,-6,-10,-5,-6,-8,8,7,-8,-8,-3,-1,-9,3,5,8,5,-6,-10,3,-8,4,2,-3,-10,-5,10,-2,-7,10,2,-1,-1,-3,9,-7,-9,-2,-2,-1,6,5,-2,-4,3,2,-3,2,9,4,-3,5,-4,1,4,8,8,7,-2,10,8,-1,-4,-4,10,10,-1,-3,4,8,-6,1,2,3,-10,1,4,8,7,-10,9,8,7,-4,-7,-2,-1,-6,-8,10,3,-7,-3,2,6,-7,-4,-5,-8,1,-3,8,-3,-10,-3,-2,-10,-3,1,-3,9,-1,4,-1,7,8,6,-6,10,1,-6,10,-1,9,8,8,1,-10,7,9,-5,4,5,-10,7,10,6,9,5,-1,1,2,-1,9,4,-2,9,10,-7,10,-4,7,-2,-9,-6,2,4,-9,6,4,10,-9,-3,4,1,-8,-6,-7,3,5,-10,7,1,-8,-6,7,10,4,8,5,-3,4,-8,-8,-1,-10,-2,-3,-5,-1,5,6,5,9,9,3,-7,-1,-10,-5,6,9,2,-2,-7,7,-3,7,4,-3,10,-9,3,-1,1,-3,1,6,8,-2,4,-8,4,-7,3,-5,4,-1,4,-1,10,-3,-9,-8,-8,3,2,9,9,6,3,-7,5,-7,10,5,3,-2,-8,1,-1,-10,-6,-8,-4,-6,-6,-8,-1,-10,-5,2,3,-2,4,-7,-8,7,5,-8,8,7,-5,6,10,-6,1,2,-1,6,-8,2,9,9,-3,-2,8,-6,4,10,8,-8,-5,-4,5,-4,3,10,-3,8,3,-8,1,8,6,9,4,-4,6,-7,-7,5,-5,4,3,6,1,-8,10,8,-4,1,-4,8,4,-2,-6,-3,-3,1,-8,-1,2,3,-7,-9,8,10,-6,4,6,1,5,3,2,4,-2,8,4,6,-2,4,-7,-4,5,-1,3,2,-7,-8,8,8,4,-4,7,2,6,-1,-2,-4,-2,9,8,-5,-6,-5,-2,-4,8,7,-7,7,6,-4,3,-7,-2,10,10,6,-6,-10,-1,7,2,7,4,1,-3,10,5,-3,-6,9,-8,-3,4,-3,8,8,-3,-9,10,8,-7,3,6,10,-7,-7,2,9,3,-4,-1,3,9,4,-4,-5,9,-4,4,-6,-1,-5,-2,2,6,8,-8,5,5,-7,2,-1,-1,-7,-8,-3,-7,-5,-5,-6,-1,-2,5,6,-9,-8,-4,3,3,10,2,-4,4,-9,4,-9,8,-6,9,5,-5,-8,-2,-6,-10,10,-10,2,-2,2,-6,3,-4,-9,10,-10,6,6,10,5,-8,3,-9,-1,-8,9,6,8,-4,5,-2,1,-5,-6,-8,-5,7,-4,3,-9,2,4,3,-10,-10,1,9,10,6,9,10,-2,-1,3,-6,4,-2,6,10,-10,-10,-4,10,5,3,-2,9,10,-10,4,7,4,8,-3,-7,-1,-4,7,1,10,7,7,-5,6,3,-1,-9,10,-4,-8,-5,-7,-5,1,-6,2,-4,-9,-9,4,4,2,2,-5,-4,9,-3,6,-3,-6,9,-2,8,-4,6,-8,-5,6,-2,-8,-5,4,3,5,-1,5,-10,5,-8,-6,-6,5,-7,-3,-3,7,-7,-5,3,6,-3,-3,10,5,-8,-2,-7], dtype = "int64")#candidate|7592|(630,)|const|int64
call_7591 = relay.TupleGetItem(func_5716_call(relay.reshape(const_7592.astype('int64'), [630,])), 0)
call_7593 = relay.TupleGetItem(func_5718_call(relay.reshape(const_7592.astype('int64'), [630,])), 0)
uop_7596 = relay.exp(uop_7585.astype('float32')) # shape=(5, 5, 9)
func_3883_call = mod.get_global_var('func_3883')
func_3886_call = mutated_mod.get_global_var('func_3886')
const_7623 = relay.const([[2.746766,1.663017,-0.942141,8.023853,-2.496595,4.425569,-8.337938,-5.522067,-9.155525,-1.136183,-6.853690,-0.046212,-5.293029,4.750395,9.681779,0.852735,1.826352,7.339134,9.892923,1.688138,-7.136817,0.163409,2.436409,6.953741,-3.923400,9.288669,6.291078,3.848736,5.670744,-8.713811,-1.638561,-8.465346,-9.071914,6.827354,-0.752650,-7.708058,5.272905,7.082025,2.671087,1.484722,-6.775978,-2.868837,-9.787921,-9.028767,-3.473340,-9.707441,-4.756937,-8.966696,-0.025959,-5.434659,-3.073587,6.115683,-1.651721,6.979353,7.065697,6.456234,5.987084,-9.967456,-7.846042,-2.377430,4.139507,7.844872,6.443031,3.442797,1.193230,-2.276981,-0.400865,-6.417910,-1.015058,-3.152561,-7.906219,-4.295828,5.997408,8.514966,6.326177,-9.118346,7.554530,-9.366474,-7.259694,-9.599800,-0.753947,3.720560,0.310557,6.668633,6.550675,7.672006,-3.347050,-6.742954,-4.215382,0.459635,4.610971,8.120830,9.744892,7.578686,6.260591,5.197722,-8.197592,-9.754762,-2.420465,8.809211,4.026165,8.234200,-7.347475,9.271791,-0.096348,-2.676540,-3.278031,-1.576766,-9.442568,2.491104,0.048835,0.489961,-3.916782,0.022006,8.759262,-9.083408,-2.922050,-2.926988,8.683178,3.201064,-5.568612,8.273282,8.557120,-6.122532,8.139349,7.378128,4.240507,-9.231400,-2.928266,-7.587071,6.624675,-0.257832,0.870798,-6.992604,-5.641679,-3.568417,-1.400075,-9.246249,8.102351,9.949548,-4.910700,6.348500,9.524454,0.428070,-3.898820,3.240850,5.421594,3.936582,4.700828,8.535386,6.410415,-3.436475,-5.624260,-7.224695,-5.160342,-0.886578,-5.607101,-2.921464,-1.102999,-3.648940,1.336733,-2.401257,4.442311,7.345052,6.085021,1.839137,-6.448919,-7.282744,-0.099673,-5.956653,-4.140195,1.165552,8.920043,-7.989612,-9.002283,-5.707747,5.753938,-7.605117,-4.300978,0.234932,-8.893687,-5.817046,-3.275614,9.553381,5.088631,8.767666,4.862261,2.232789,-2.653008,-9.782238,-5.723736,2.396032,8.801708,-1.981504,4.556053,2.400745,-8.359300,3.334137,2.371001,1.401789,-6.525765,-1.707326,-4.046598,-0.932918,-1.320178,7.275424,9.555336,-4.283121,-0.175361,-7.850695,-0.760452,9.905893,-0.487214,5.353826,-6.590484,-7.527927,-5.746283,-9.679460,-6.616609,3.886365,1.091941,7.587323,2.694739,4.988568,8.809942,-8.525528,1.945670,-4.982582,-4.708673,3.085361,2.574104,6.654168,9.948384,-7.257344,1.774724,-1.441232,-1.052422,3.131832,5.439934,7.486482,7.308320,-6.879922,2.136790,-9.721934,-1.605587,-9.399986,7.783440,3.345732,5.072573,9.041726,-1.443007,9.289681,0.877037,-0.307165,9.645995,5.265278,2.689515,-0.073689,7.939563,-8.763878,-6.842483,5.433479,6.557606,-3.808107,-5.647613,0.472563,0.710436,7.152905,7.481049,0.048488,3.001156,2.907427,-2.395557,5.699828,-4.097651,-7.867127,5.287081,5.416095,-3.295050,7.854522,8.635734,4.130586,-8.066995,6.061716,3.696210,-2.099259,-2.838519,0.097731,3.072843,-8.184234,5.408701,4.932214,-5.572129,0.600002,-3.355116,0.473772,5.129845,2.208245,0.891724,3.461127,3.548221,5.171081,-1.632142,0.812024,7.488444,8.379231,-1.281515,0.850865,0.589151,3.430532,-5.833553,9.762326,-1.659498,8.486641,-5.202428,-0.809895,-3.595949,8.170144,-3.574204,9.368556,-9.128116,-0.719033,6.808889,4.377047,-4.572166,-3.250061,0.068777,-0.405446,-9.096346,1.105203,1.692017,3.103516,5.293116,-6.253667,4.789774,0.771422,-4.074142,-0.898560,-0.141007,6.576706,-8.802989,1.849489,6.583273,7.489034,2.779404,-1.326692,-0.253553,-3.375192,-4.847350,-3.196467,-7.832581,2.176170,1.920649,-9.801218,8.150531,1.740767,-1.610910,3.106565,-3.317409,2.999741,1.076674,-3.627954,8.552409,0.505934,1.187352,3.854647,-0.100148,3.630365,-9.585077,4.406106,9.735400,-8.546250,9.618483,9.832923,-6.841414,2.703024,7.358514,-8.978276,-7.883030,-1.705257,2.835074,-9.778850,6.250770,5.408700,8.454375,2.435122,4.909675,-7.797128,-0.526106,3.095855,5.570131,-5.409777,-2.137617,6.507414,5.949401,6.435548,-3.815586,-7.680697,2.853230,4.381396,-1.365955,1.156718,-7.541140,-4.064435,5.550764,-6.853916,-1.717625,1.274642,5.714790,5.641013,5.178818,3.991529,-7.164378,3.633266,0.269207,5.606168,0.052156,-0.989163,-8.860433,-1.331836,-0.524959,-9.900846,-4.993370,9.430467,1.729709,-7.783605,6.549078,-4.703930,1.110866,8.138846,-3.395895,-2.043120,1.844878,-6.198010,1.600666,-9.668796,8.863121,-1.411439,-1.102298,4.390347,-2.232166,-1.956596,6.645471,-9.675492,-2.808182,4.016366,-7.010107,0.009989,-2.105836,5.222152,-7.845330,3.809417,8.257019,0.114051,-2.139455,8.583345,-7.489508,-7.964999,-3.236580,-4.569118,8.403459,7.601163,2.058984,1.314928,-3.038174,0.133649,-9.725121,-4.755987,-0.790867,-2.494793,-4.791089,-3.864246,1.536452,-4.537970,7.204445,6.135477,4.891970,-0.743750,2.395360,-1.181208,-3.787935,-9.600063,2.358976,-9.199461,0.504278,-2.138013,-5.574358,-5.564485,8.557931,7.823687,-4.636118,2.548859,-9.122750,-6.365325,-7.678655,1.074628,2.685414,0.744043,2.720953,-3.019237,-4.476313,-7.002848,3.373211,7.724886,-2.136708,7.031144,8.201749,-7.847541,-6.430794,8.094390,1.244759,-8.124288,-6.506863,2.666992,2.990283,-1.099926,-2.581308,7.137370,-9.326230,2.212497,5.104979,3.430395,5.529961,-2.018880,-4.554070,-9.368018,9.569768,-8.742550,6.990123,1.179084,-6.174345,-5.017601,-0.015348,-0.559807,-6.841824,2.930230,1.251361,-2.618473,-4.930076,-3.345037,-2.054455,9.520240,9.069637,-3.152165,4.502465,-9.644004,9.919777,1.813438,-5.843007,-0.641023,4.942140,-4.990408,-5.134029,6.208611,-3.625350,-0.184851,9.094492,-7.650759,2.781105,5.884368,-8.780052,-2.572114,-7.343101,2.688008,-4.144521,-5.428626,-5.763643,-6.900932,6.952498,4.875576,6.819279,4.805946,4.169083,-9.241034,-7.395771,-6.988819,6.112611,-0.863582,-1.919768,-9.322615,-2.251365,-9.162504,0.197221,9.564975,-3.868394,-5.658856,-3.351325,-1.098274,2.042599,8.119079,-1.682535,-5.482595,-7.240188,-2.230360,0.705570,4.363991,1.438736,-9.737102,-3.765903,5.991347,-1.852368,5.020447,6.516545,8.240267,-8.106137,-1.005645,-7.135741,-7.052766,-8.374339,2.886510,6.287782,0.643309,-3.911720,7.768657,3.397685,3.233991,0.004922,7.909145,4.174126,8.296816,2.817918,-5.492011,4.600004,-2.678815,3.141705,0.729675,6.114825,9.492351,-7.189422,-8.836593,-8.200585,2.402632,-4.756430,-9.134812,7.271124,3.287391,-3.513809,-6.190248,-2.122803,0.773766,-5.827081,-5.111257,3.791006,6.593513,8.933185,0.408652,-9.041063,4.542107,0.510845,-8.096022,1.386720,2.156033,5.070650,1.636997,9.902371,-2.638071,1.748507,3.926070,-7.104774,-8.018159],[-5.365897,4.288146,3.206883,-2.989239,3.008284,9.198240,-2.100712,-7.138388,9.165453,-1.133086,-3.940373,-7.417791,0.667346,-4.167940,0.932481,9.285513,-8.504982,-8.878357,1.328889,4.768024,5.617005,-5.611725,4.153385,1.882825,-2.070396,8.604731,-0.023844,0.879496,0.173404,-5.733241,-5.076485,2.008221,-5.516887,-6.660715,-0.665284,-4.164252,4.914083,0.651935,4.454548,3.984815,-6.829795,-6.436802,-8.123218,8.221753,2.116963,-3.344007,9.599416,8.100710,4.975249,-3.492665,4.227100,4.834125,8.932961,0.519186,-9.191512,-1.725669,-3.305545,0.586798,-7.568660,-6.381872,-5.044312,-6.273142,-0.053460,-7.467537,0.294681,2.704512,4.189989,7.119477,-2.894903,-7.454366,0.692576,1.621563,1.008672,6.499635,0.734540,-7.075156,-7.048081,-5.331323,-9.375455,9.166992,6.752027,-7.629776,7.394374,1.234467,-7.488135,-3.595822,-6.948121,6.648042,7.499600,-8.897708,0.193935,-1.842444,0.973406,-3.980017,4.352925,5.695718,9.419051,-1.886730,-4.538505,-2.838780,3.467451,-2.650364,-2.773679,1.534653,-3.032465,7.814994,-5.602727,-5.521201,-5.137482,3.100644,-5.638176,-3.993047,-7.306899,-9.535782,-9.067229,-0.782544,-7.772071,7.141336,-2.303699,-0.353996,-6.795759,-7.812138,2.742754,-8.301766,-4.397966,-6.997500,1.786717,-7.164334,0.894359,-1.731527,5.701011,1.046883,5.308761,-5.632498,9.405967,9.971119,-5.021995,7.930623,-9.070090,1.155377,7.604219,2.358991,-5.122334,2.673960,-6.819890,6.052045,-0.660428,3.358942,-3.002376,8.690879,-5.215701,7.878135,6.740945,3.609711,2.968809,-6.758180,-5.713618,4.491695,6.108180,-8.158994,-9.530161,8.717974,-0.935686,-7.204560,-2.890594,-6.614511,-2.126903,-6.372421,-6.800995,9.027499,-8.447007,3.751962,0.645428,-3.085613,4.753060,3.389455,-1.672947,-4.388678,4.188418,0.486235,-9.667816,5.180849,-2.544189,-3.142986,5.752442,-7.948353,5.056936,-1.728188,-1.335151,2.996884,7.991334,3.257468,6.034049,-8.195531,-5.796314,0.538778,9.839458,-0.840829,-8.182221,1.780776,-3.019740,9.750022,0.720954,7.172311,-4.804949,3.078207,3.913345,-2.426836,-6.577885,5.620483,-3.602951,5.276799,9.997271,1.221438,2.307487,9.681305,-8.142761,9.233910,-8.774685,0.085846,-5.762271,-0.578682,8.058419,-9.860783,1.309367,7.301541,-2.303079,-2.856941,-6.224664,2.826170,-7.620411,7.396868,-3.478905,-9.819086,1.650980,7.773415,-9.255366,9.220144,-4.435708,2.828118,-9.601900,-5.556516,5.109907,-3.105191,-7.548321,4.321358,0.788871,-8.163051,-7.056617,-8.073196,-2.689787,7.376524,-9.117272,3.702445,-4.483167,-8.056579,2.248546,-0.844282,2.569308,-3.552508,-7.980359,-9.805073,-4.100125,1.170298,4.405145,3.535544,-8.210031,-0.833116,6.624997,9.641507,-6.226894,-7.813225,-6.902270,5.859196,-8.093742,-7.567023,5.404316,-4.902500,3.609330,-7.516649,2.431820,-1.611405,-2.617307,-0.529142,-9.433323,-3.531553,-8.712932,-4.225227,6.723468,-8.967955,7.573283,-6.084225,-2.733810,5.767312,2.455178,-4.040521,2.050376,-0.150543,-8.124646,5.414258,-3.926213,3.763180,4.937011,-9.817092,5.974013,-8.280497,8.951633,-7.263924,9.662010,6.737427,6.851181,4.406469,-4.518130,0.443277,4.734111,-2.986499,-9.768745,-4.242268,8.925609,-3.252069,9.653730,-7.990118,1.421734,-4.867085,-0.696943,1.931500,-0.499002,-0.992782,-6.873686,8.001450,-1.979162,-8.652455,0.523989,-6.578903,4.858339,-5.809235,8.379635,7.863620,9.457144,2.128234,7.341193,9.494268,-9.838532,-7.505696,0.677518,-3.615803,5.996418,-6.431447,2.219938,-1.401666,8.524351,1.974123,6.459338,-9.936680,4.382727,-2.187514,-2.893769,-1.053659,2.294167,-7.593417,-0.841006,-1.876566,2.138203,-7.972902,-9.753843,4.492858,6.517012,-4.352136,1.914656,7.106090,0.172721,4.849161,-8.020376,-2.615797,-6.310162,-9.758346,1.449307,2.825415,-1.411139,7.988757,-2.160437,-7.493281,6.791885,-8.592624,1.220209,9.441583,7.756726,4.213241,-6.576528,7.930247,-9.803471,7.142441,-0.287714,-7.929595,6.909407,3.458069,-3.099276,7.790327,3.063825,-9.292738,-8.527482,3.687613,-1.257969,3.896351,-1.346908,5.352872,-8.564403,-3.117852,0.810359,9.219188,-4.584483,-7.305996,6.738989,-1.028267,2.646375,2.217782,9.815756,2.875642,3.881205,-1.869575,7.590556,-5.696745,3.337318,6.185361,6.403085,0.974279,2.525767,-9.120079,7.724612,4.500267,9.150097,-5.891100,4.100556,-1.982620,-3.148825,-3.518637,0.314761,-6.674487,1.869419,3.327748,-9.605089,-4.222869,9.488838,-8.349843,-2.791246,3.179505,1.682993,-3.801603,-1.500826,7.691428,6.759955,-3.857583,0.004302,3.860843,-5.354646,4.681882,2.384055,0.223864,1.247243,-7.303040,9.955001,8.669874,2.541444,-1.629547,8.637827,2.140083,3.709682,2.659526,-5.298290,-5.368935,7.348204,0.558368,2.353850,4.114358,3.016893,-1.303430,-7.218860,3.451628,2.804931,3.317895,9.622540,-5.603237,-9.836508,4.784022,-0.714366,-5.268129,-5.913510,3.597137,-7.346365,-9.635516,-4.082383,-2.930042,-6.332124,-7.067519,3.081755,-8.917678,-6.531657,-5.054837,-6.388939,0.631841,9.869163,1.799897,-1.616065,2.885812,0.806135,-2.215502,3.420505,-4.259335,-4.128025,4.725300,-5.147283,-9.997906,-6.836034,-9.717809,0.097828,-0.011321,1.521591,-1.087517,-7.346968,-4.154959,9.086392,3.749216,9.117282,-0.247581,-3.905420,-7.391205,-0.421056,-8.556041,9.869022,9.320007,-3.184110,5.159585,0.400421,2.678808,8.544382,-0.696404,-4.601852,6.034894,9.020971,1.479731,-8.597949,9.521843,1.996706,8.343481,-3.142257,9.204488,-5.883234,-6.704326,-6.262051,7.546115,8.015090,-2.733220,4.699378,4.600258,8.613852,6.944307,-6.071393,-0.331839,-3.969670,-6.136465,5.029256,6.083094,-4.616300,0.551500,-9.724132,3.321258,-5.176248,6.059063,7.787350,0.373085,-0.688734,-9.392822,0.275534,-3.144712,8.666931,-4.257472,-4.015989,-8.959044,4.104517,4.387552,1.876785,7.578165,-9.995667,6.188948,2.567876,-3.667893,1.325433,0.688310,-2.747646,-0.451439,-2.382110,-3.286918,6.168999,-3.092880,-3.823858,-3.542660,-0.297766,-9.550155,-0.155772,-0.763213,-6.954769,4.771076,-0.207140,-4.745336,-9.594332,-4.955462,8.162562,3.729724,2.091055,4.620978,0.842722,7.730173,8.718404,-3.467833,-1.015948,9.002682,-7.728323,-0.897586,1.383157,3.859059,-4.904980,8.662822,-4.132945,-1.936429,-6.690330,4.710427,7.782329,6.805483,-7.546627,-0.034382,-2.038444,6.619206,6.835767,8.412553,-2.357586,-4.075914,-0.606996,-7.883772,5.673137,0.217694,-6.051314,7.972832,7.517648,-4.206210,4.604442,-2.449500,8.911772,-7.516276,-2.684747,7.296058,-2.665841,2.378335,4.345287,4.589169,-9.688711,-5.982372,5.436585,-7.806551,-3.078418,6.945112],[0.919513,-1.905509,0.724047,3.258791,-3.727696,1.868731,3.469793,-5.630759,-7.803101,4.601256,-6.763014,-3.483365,3.511875,-6.819964,2.236722,2.411176,-6.473906,8.816248,-8.244794,6.828045,-7.991416,8.010136,8.617024,-9.005914,9.429191,-7.066068,-2.687300,-8.691604,8.752747,2.797927,-8.177425,2.693379,-1.960696,-4.791560,-7.291617,-3.863230,-8.765343,-3.485567,2.790247,-4.309722,-1.378680,-9.280367,9.599639,-3.849618,5.516110,5.547921,0.620136,-4.644133,-6.340073,-7.408676,-7.373875,8.205899,0.617965,-7.010727,-3.767649,3.886873,0.159434,3.044321,-8.440784,2.437889,-6.455454,2.523754,-0.506883,4.209015,3.901785,6.591940,-8.166142,-1.528581,-5.554733,-5.226555,2.859952,3.304606,7.995173,6.828226,-4.364733,-0.159702,-1.113548,-7.110216,1.765288,5.744198,-2.914074,4.281822,3.031079,-7.335109,-6.683908,-3.870366,-8.898385,9.522302,4.719982,-9.904993,3.396604,-3.295349,-3.193918,-5.482269,-1.873532,-3.730103,-9.896696,-3.590538,-7.185399,5.951027,0.654772,-2.217389,0.123533,-9.550744,6.638056,9.101759,9.711833,-2.213347,-4.589905,5.662174,-7.728725,2.771356,2.891049,-9.501079,-7.546195,4.827262,9.651443,-6.490549,0.750056,7.362675,2.845058,5.500813,-0.229928,-1.322943,7.888710,-6.642903,-9.290210,-5.176584,3.715586,7.359510,2.891026,2.517812,-5.700581,9.991989,-3.540808,-8.688900,8.165376,-7.714563,5.505612,1.448750,5.434552,-2.695011,1.481153,6.345479,1.366535,7.425166,6.845581,-9.499810,-5.120545,6.432769,-0.665419,-4.221523,-3.216124,-1.992463,1.919619,-4.444527,2.104820,-4.814013,7.904629,7.462663,-4.214226,4.880774,5.143071,-7.831890,-8.687825,8.840893,0.276658,-0.271065,-5.423857,-9.273261,-2.102191,-2.902380,5.899836,3.123149,2.463094,-4.355402,7.455071,2.732930,4.475126,-9.596201,-4.710577,-4.925682,3.363954,7.253144,8.661801,2.939508,-7.384490,0.645137,4.052714,-1.119443,8.184707,-3.374064,1.262470,-6.113290,5.075137,-8.953902,-4.808561,-5.182940,8.747574,8.218410,5.464420,9.083432,5.832962,5.889373,0.800772,6.275809,-7.860620,5.392111,0.487652,-8.265564,-3.623968,-0.336060,-4.359569,-6.632145,-7.082562,-8.328833,-3.629642,0.154254,0.497405,-8.319442,6.825923,7.099504,-2.759410,9.221733,-1.338318,-8.257345,-6.273615,1.819848,6.347746,-2.911746,-6.919405,6.411810,-5.350290,-2.281323,-5.781568,-8.066887,-9.512525,3.001854,-1.965485,-8.573997,7.347890,7.170286,-3.885109,-6.345816,-8.292330,7.895316,4.362376,-8.904746,-0.634236,7.490924,1.927961,-5.287864,-5.877711,-1.558249,-5.515640,1.408125,-5.121120,7.570662,-9.749546,-4.756513,-6.440151,3.773887,6.335642,-4.906608,-8.235702,-9.721680,2.775571,9.649579,-6.073214,4.138676,-2.239665,-9.537685,0.175083,3.435055,7.069444,6.680032,-5.430022,-0.797342,-8.101209,2.470272,-3.048391,-8.979370,-4.751671,0.874129,-1.042294,6.430766,-9.375691,4.139516,4.518700,3.995678,-5.279611,-3.223162,2.515521,-7.707847,7.785281,-9.634859,5.168576,-0.168152,-7.344671,3.233915,-9.945425,0.842364,-4.653731,-9.391915,-2.313772,8.839661,-5.066083,4.494348,-7.594440,1.753953,3.364713,3.629234,3.772963,-0.242745,-0.577365,-2.487227,-2.949446,9.674897,-3.337165,-9.911964,7.909351,1.249832,9.619984,8.351964,7.437854,-2.473931,-3.745698,4.340931,9.066433,3.069580,1.806338,-1.088455,2.602284,3.341390,2.586214,-3.883384,6.239332,5.176870,-3.372176,-3.137781,0.200582,-6.757658,-3.279002,4.799986,3.168434,0.158524,-1.540899,-8.923798,0.347768,6.083075,9.249470,3.640987,-1.774403,-8.860103,5.984760,-0.936590,9.113795,-6.952717,-1.403614,9.924641,-9.500653,3.382702,-8.780261,7.525841,6.751398,-5.545214,-9.248274,6.734626,-7.594462,-5.914631,-6.987545,1.850773,8.392925,0.738267,2.842522,-0.294080,-0.807798,2.232065,8.403509,-9.018333,5.531292,-9.410430,9.379221,-2.780476,8.466411,4.580528,5.595630,1.732147,3.631448,0.143053,2.121107,-7.658201,2.474637,-5.888155,-0.196855,0.551919,2.279210,-7.297820,2.977849,8.781904,5.430288,-4.137513,7.439651,8.652638,-4.928703,0.727137,-7.435886,2.055486,0.862952,2.984489,9.256903,-5.060655,-4.556151,0.465826,5.499675,-1.568473,5.487540,-5.204290,-5.307703,4.780026,-3.288510,-3.357368,9.546273,-5.991229,8.432826,-4.886053,-1.200245,7.097126,9.207971,-7.330392,9.159516,8.784156,1.333906,6.864834,-3.825922,-1.492018,-4.743203,2.812319,9.890433,-6.716012,9.406010,9.304480,9.040520,-9.779711,4.880740,-0.603593,2.649630,3.669134,4.923080,-8.426504,-0.923137,-2.972050,7.219980,-1.955990,2.018866,3.183229,4.246726,-9.527935,-1.705212,-2.476271,8.451982,-1.159344,-1.805629,1.504739,5.456336,1.074185,-0.360291,-3.945406,-6.350313,-1.437833,8.217399,-2.528613,-7.190082,-8.649255,-7.024779,-5.753219,6.503579,-2.305115,0.820577,2.204591,-1.154736,-0.945030,-6.992320,-5.379614,3.050465,-3.506513,4.551852,1.106883,0.044646,-3.715396,-7.814918,0.300129,5.526401,-2.070880,6.713516,7.242623,-0.892307,-9.224116,-5.784893,2.308164,-4.900696,3.857773,3.195114,5.014435,-3.310116,-4.763982,5.690533,-0.662682,3.869921,5.387335,-0.999110,-4.328835,-1.452211,1.889074,-0.186876,-4.790098,-6.284473,-5.078451,-6.100226,-0.815594,3.132552,-8.253441,-3.457027,0.828177,3.500427,-0.383408,-8.563681,-1.749705,2.630848,2.709248,4.077539,-6.417769,4.373739,7.239819,0.771652,-1.358851,-1.497707,4.163827,4.655423,-7.812393,3.514911,-1.839270,-7.273552,-1.298921,-9.561409,3.148250,6.188812,5.488393,-5.424639,-8.688666,-8.780664,-5.618558,8.914637,5.460897,-8.932238,2.681129,-8.585858,5.224992,0.895142,0.287554,-8.692714,9.893837,-4.198517,-1.442446,3.255149,-0.799065,-9.667836,-2.475582,-4.652689,-9.116277,4.928771,-5.281924,-2.732937,-6.478925,0.579948,9.651184,-1.180449,8.708744,-8.460455,9.810004,2.929842,1.151658,-6.977642,1.118482,-8.647964,-8.672956,-7.100126,4.351048,-5.632882,-5.845517,6.591303,0.171056,-1.911613,4.608699,7.384140,-6.506780,-2.710198,-7.261436,2.017046,-0.528885,7.643253,3.016777,7.230396,-4.078042,1.539477,-1.593185,0.487709,-2.623938,-1.187154,-5.151892,0.416605,-9.021528,-1.753538,-3.990071,9.819698,6.496375,8.302063,-6.109376,-3.201000,0.631719,8.203560,-1.961583,7.892053,-7.435290,-6.279344,0.085347,6.475037,-3.037412,-6.015927,8.670900,4.348437,4.677334,1.311489,8.545499,-2.347875,4.256143,-5.727388,-1.275307,3.095409,-4.629961,3.875574,0.832866,1.899385,3.487832,-2.626338,6.876235,0.317313,0.931405,-1.257349,-1.154141,3.625947,-4.520032,-4.380148,4.836402,1.610645,3.912670,-4.569716,2.875952,-9.639688,7.879059]], dtype = "float64")#candidate|7623|(3, 660)|const|float64
call_7622 = relay.TupleGetItem(func_3883_call(relay.reshape(const_7623.astype('float64'), [11, 12, 15])), 0)
call_7624 = relay.TupleGetItem(func_3886_call(relay.reshape(const_7623.astype('float64'), [11, 12, 15])), 0)
output = relay.Tuple([call_7591,const_7592,uop_7596,call_7622,const_7623,])
output2 = relay.Tuple([call_7593,const_7592,uop_7596,call_7624,const_7623,])
func_7643 = relay.Function([], output)
mod['func_7643'] = func_7643
mod = relay.transform.InferType()(mod)
mutated_mod['func_7643'] = func_7643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7643_call = mutated_mod.get_global_var('func_7643')
call_7644 = func_7643_call()
output = call_7644
func_7645 = relay.Function([], output)
mutated_mod['func_7645'] = func_7645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5168_call = mod.get_global_var('func_5168')
func_5169_call = mutated_mod.get_global_var('func_5169')
call_7646 = relay.TupleGetItem(func_5168_call(), 0)
call_7647 = relay.TupleGetItem(func_5169_call(), 0)
uop_7666 = relay.exp(call_7646.astype('float32')) # shape=(11, 12, 15)
uop_7668 = relay.exp(call_7647.astype('float32')) # shape=(11, 12, 15)
output = uop_7666
output2 = uop_7668
func_7672 = relay.Function([], output)
mod['func_7672'] = func_7672
mod = relay.transform.InferType()(mod)
output = func_7672()
func_7673 = relay.Function([], output)
mutated_mod['func_7673'] = func_7673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5168_call = mod.get_global_var('func_5168')
func_5169_call = mutated_mod.get_global_var('func_5169')
call_7839 = relay.TupleGetItem(func_5168_call(), 0)
call_7840 = relay.TupleGetItem(func_5169_call(), 0)
func_3674_call = mod.get_global_var('func_3674')
func_3678_call = mutated_mod.get_global_var('func_3678')
var_7848 = relay.var("var_7848", dtype = "float32", shape = (9, 4))#candidate|7848|(9, 4)|var|float32
const_7849 = relay.const([0.253102,-0.670817,-1.615550,-8.598719,-1.919787,-5.230369,-9.689398,2.370886,-3.993672,3.541977,4.273910,-9.116780,-6.023634,-5.265912,7.135493,0.431078,0.220117,-3.400064,-6.230951,9.573688,-9.314627,4.029437,7.290757,-9.503446,3.406578,1.126657,6.276621,-0.141598,4.930756,-8.114538,-8.776592,8.798508,1.444354,9.130785,-1.944851,-5.607717,2.054951,3.436364,8.273120,-1.535676,-5.318111,6.946714,-9.517032,2.268066,6.926191,-5.401758,0.916735,7.896486], dtype = "float64")#candidate|7849|(48,)|const|float64
call_7847 = relay.TupleGetItem(func_3674_call(relay.reshape(var_7848.astype('float32'), [1, 6, 6]), relay.reshape(const_7849.astype('float64'), [48,]), ), 5)
call_7850 = relay.TupleGetItem(func_3678_call(relay.reshape(var_7848.astype('float32'), [1, 6, 6]), relay.reshape(const_7849.astype('float64'), [48,]), ), 5)
output = relay.Tuple([call_7839,call_7847,var_7848,const_7849,])
output2 = relay.Tuple([call_7840,call_7850,var_7848,const_7849,])
func_7861 = relay.Function([var_7848,], output)
mod['func_7861'] = func_7861
mod = relay.transform.InferType()(mod)
var_7862 = relay.var("var_7862", dtype = "float32", shape = (9, 4))#candidate|7862|(9, 4)|var|float32
output = func_7861(var_7862)
func_7863 = relay.Function([var_7862], output)
mutated_mod['func_7863'] = func_7863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7238_call = mod.get_global_var('func_7238')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_7879 = func_7238_call()
call_7880 = func_7238_call()
func_6799_call = mod.get_global_var('func_6799')
func_6803_call = mutated_mod.get_global_var('func_6803')
const_7904 = relay.const([[-6.949369,-6.754806,-8.579371,-1.043784,0.747058,-0.580819,-0.301138,1.168765,-7.319383,4.840645,-3.725188,-7.750795],[-0.473257,-5.355938,-1.716418,-2.295386,-4.381583,7.495159,-1.334941,-5.143322,-2.939301,8.254737,-9.593054,-1.936153],[-7.669405,5.796670,-1.281501,-5.892853,7.698941,1.158270,-1.940483,7.491340,-5.058165,-5.675444,-8.274836,-5.977057]], dtype = "float32")#candidate|7904|(3, 12)|const|float32
const_7905 = relay.const([-6,-6,8,7,-7,-7,-5,-8,4,9,10,-1,5,3,10,-2,4,3,3,1,6,-10,5,-7,10,6,-2,-8,-2,-6,10,-9,3,-8,1,-10,-7,9,8,8,4,8,1,-2,-9,-5,6,5,5,8,1,4,-8,-10,3,-4,4,-4,10,-9,-4,-7,-8,10,6,-1,7,6,10,-4,6,1,-4,4,-1,-10,-7,5,-9,-1,4,1,7,1,-5,-2,4,10,6,-1,-7,4,-8,-1,6,2,-4,-3,2,10,-10,-8,-6,2,2,-1,-4,3,3,-1,-6,9,9,10,-8,1,-3,-2,-7,2,-8,8,-7,-6,-5,-9,1,10,2,1,2,-7,1,5,6,7,2,7,-8,-10,-9,3,-7,-10,-5,-8,-3,4,-6,3,-8,-7,-6,10,9,-7,8,-8,7,5,-9,10,10,7,7,-8,-10,7,-1,-2,-8,-1,-10,-3,-9,10,-1,-1,8,-7,-7,2,-1,-3,-8,5,3,4,6,-2,-8,-2,-5,-10,-2,10,3,7,10,10,-7,4,2,-5,7,-3,4,-4,10,-3,-10,-4,-2,-8,-2,-10,5,1,10,-4,-7,-2,2,-9,-9,-7,-5,3,-1,-10,1,-2,-4,2,10,2,4,-6,9,1,10,-8,-6,-2,4,-9,-2,9,-5,9,-8,-1,-5,9,4,2,7,-9,-9,-9,3,-7,-9,2,-9,9,1,10,-1,-10,10,-1,9,7,10,-2,3,7,-8,-8,-9,-4,9,10,4,6,-1,-8,-6,-2,-2,9,-8,1,-5,-2,-8,-9,-2,-8,9,10,-1,-4,-5,3,-5,-5,9,8,7,-10,-8,-3,-10,-7,-4,-2,-7,-2,-5,2,-7,4,4,-2,1,5,3,-10,-6,-1,-3,-7,-1,3,-6,-7,-1,-1,-2,4,-4,-5,-7,-9,9,5,-3,2,-5,-2,-7,6,-10,1,-7,-7,7,8,-6,-9,7,9,-8,5,-4,-4,6,9,4,-9,-6,-4,10,-7,8,-3,1,4,1,-3,-6,5,7,-9,-3,-6,7,-4,-1,-5,-6,-4,10,-6,-7,5,-8,-7,-2,9,-7,4,4,-4,8,4,10,3,-5,-9,10,10,-4,-4,-5,4,6,5,8,7,-1,-2,-10,-8,-5,-9,-3,-2,6,-5,-9,-3,7,-8,-7,2,5,-8,-10,2,-3,10,-10,5,10,-6,-9,5,7,10,8,4,6,10,6,1,3,-7,4,10,2,-5,5,6,3,7,-7,-5,-3,-9,7,10,1,-4,9,-9,7,1,-3,-3,-2,8,-3,2,-9,5,-3,5,-4,7,2,6,1,3,-4,-2,9,6,2,8,-1,7,-9,7,1,9,-1,3,4,-8,4,-5,-10,5,-10,-3,-5,6,5,7,9,-9,3,-4,10,5,4,7,2,-7,-4,-7,3,4,9,3,-9,8,-6,9,8,2,-6,5,-2,4,5,8,7,5,1,-3,2,-2,-8,8,7,-8,-10,2,-7,9,-10,-1,7,2,-6,10,-10,10,-7,2,8,-8,-2,10,9,-3,-6,-3,-2,5,-1,8,9,-9,-4,-10,-2,-1,-9,6,-10,-4,-3,1,5,3,-1,9,-9,-6,-1,5,5,8,7,-1,-4,3,-3,1,10,-5,-5,3,-3,6,5,5,-9,3,10,-5,8,-10,-4,-10,6,-7,8,-6,-9,4,8,-4,-6,-5,1,-9,-7,2,1,-6,-7,-2,3,7,2,5,-3,-7,6,-5,9,7,-2,-5,-3,4,4,-7,3,8,-5,5,2,7,1,6,-6,6,-4,-5,-2,6,-4,-6,7,2,6,2,-9,-9,-10,10,10,6,-7,-2,9,-8,1,9,7,-1,-1,3,1,10,-9,-9,-6,-4,5,3,-5,6,2,-5,-1,2,-9,-1,8,-4,-4,5,-10,-5,4,9,-9,-5,-2,-10,7,4,8,8,9,-3,5,-2,-7,-9,5,10,5,-4,6,-10,7,-10,-9,3,8,-10,-3,9,-1,1,-8,-9,6,10,9,-6,-3,-5,3,-2,-5,-8,-9,8,-5,6,-2,6,10,4,5,-8,-4,-3,-1,2,1,4,-6,8,5,-5,-2,-7,-9,4,10,-4,-6,-3,-4,-3,-4,-3,-3,-2,-8,5,9,4,4,-2,1,9,3,-6,-9,-1,8,-3,-8,9,-3,-6,8,-10,8,-7,8,-10,-9,9,5,-1,6,6,-9,10,1,4,-5,-4,-8,6,8,-6,-10,5,5,-2,1,6,5,2,1,-7,-2,-3,-3,-6,-5,-8,-7,2,-10,-4,-4,-1,-4,5,10,-6,-3,5,-6,-7,-3,-7,7,-4,-4,5,9,-7,8,-10,1,3,5,-2,-8,1,1,4,7,-4,-6,-1,7,-8,9,5,6,-6,5,1,6,-5,-9,-6,6,-9,2,-7,-9,6,-7,-8,1,1,3,-1,3,7,-6,-10,4,9,1,-5,-3,8,3,10,-1,2,-4,-4,-3,-8,-5,-3,10,-5,8,-1,10,-10,7,-7,-2,4,-3,2,3,-5,10,7,10,1,1,-8,3,-4,-9,-1,-1,6,7,-10,-7,7,4,7,8,-3,-2,-10,10,-7,6,-9,-5,2,2,10,-8,-7,3,-6,4,9,-10,-2,6,9,-9,10,-3,4,4,-7,3,7,-9,-6,-2,-10,-8,5,6,-6,4,7,-8,-5,4,-9,7,2,6,-1,-5,-3,7,-6,3,6,-10,5,5,-4,-1,6,6,-3,8,-5,7,7,-5,5,-9,-5,5,8,-9,10,5,9,-6,8,-8,-8,-10,-1,1,4,8,-8,-9,-4,1,10,10,1,-6,1,-1,-1,5,9,7,-6,3,9,-10,-10,-6,9,2,3,9,3,4,-5,7,7,-7,8,-6,-2,9,9,4,1,-8,-5,-8,-10,-4,1,1,5,10,-10,2,3,5,7,2,7,-4,-10,3,-7,5,8,8,5,-7,-4,-6,10,-1,-1,9,-2,2,-7,1,2,2,3,-3,7,3,1,-8,-3,2,-9,-3,3,-2,10,2,1,-10,-3,-3,5,10,9,8,7,7,-8,9,-8,10,6,8,6,-2,-2,-9,-4,4,-7,5,-10,-9,7,-2,1,-2,3,-4,9,10,-2,-2,-8,-2,-9,-8,-1,1,-7,2,-4,4,-6,8,6,-1,-7,-7,-9,9,-5,-9,5,4,-3,-9,3,-4,-4,6,-2,-8,-10,-5,5,-9,10,7,-9,7,-1,9,-2,5,-7,5,10,10,10,10,-1,6,-8,9,7,-1,4,2,-5,1,-10,3,2,9,-1,9,-8,5,9,-7,-10,5,-10,-2,-6,7,1,-5,7,5,10,10,-1,8,-9,-6,-3,4,2,8,-1,5,9,5,1,-4,7,3,-10,-8,5,-9,9,-2,3,8,-9,6,-10,-1,-4,-3,8,-9,-6,9,-10,-10,4,-7,-5,1,-7,-9,-1,-9,-5,5,10,-4,-10,-8,1,-9,-3,4,-3,-2,-3,9,-1,-8,-5,-2,7,-1,-8,7,-8,-8,5,9,-4,-8,1,-10,10,-1,-3,9,-8,8,9,7,2,-10,-7,4,-9,-10,-4,3,8,-8,-6,10,-7,-1,-4,6,4,-4,5,4,-10,6,-3,-7,-4,2,2,-3,-2,9,-5,-3,-1,1,7,-1,8,-3,6,-1,-5,-10,7,-9,-10,-7,3,5,9,1,-1,-2,-10,9,-5,6,-5,8,-4,3,5,-10,-1,2,10,5,6,8,10,-1,10,-4,6,1,1,3,-3,4,-5,-4,-10,6,-6,-1,4,3,1,-10,-1,6,-4,-10,1,3,-2,3,-7,9,7,-10,-4,-6,-10,2,9,7,-7,2,-3,-6,-5,-9,9,-6,10,7,10,-8,2,-4,-8,-6,-10,-2,7,-7,8,5,-8,6,-8,1,-8,10,9,-3,-7,-1,-9,-7,3,-1,4,10,8,9,9,-3,10,-7,7,5,10,10,-1,8,-3,-4,-4,8,-8,-7,8,2,-3,-9,10,6,-2,-9,-3,6,5,-4,4,-10,-10,9,-7,8,-1,-2,-2,1,3,8,9,4,4,5,-10,10,10,-6,10,6,-10,2,-5,6,5], dtype = "int16")#candidate|7905|(1540,)|const|int16
call_7903 = relay.TupleGetItem(func_6799_call(relay.reshape(const_7904.astype('float32'), [36, 1]), relay.reshape(const_7905.astype('int16'), [1540,]), ), 5)
call_7906 = relay.TupleGetItem(func_6803_call(relay.reshape(const_7904.astype('float32'), [36, 1]), relay.reshape(const_7905.astype('int16'), [1540,]), ), 5)
output = relay.Tuple([call_7879,call_7903,const_7904,const_7905,])
output2 = relay.Tuple([call_7880,call_7906,const_7904,const_7905,])
func_7911 = relay.Function([], output)
mod['func_7911'] = func_7911
mod = relay.transform.InferType()(mod)
mutated_mod['func_7911'] = func_7911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7911_call = mutated_mod.get_global_var('func_7911')
call_7912 = func_7911_call()
output = call_7912
func_7913 = relay.Function([], output)
mutated_mod['func_7913'] = func_7913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7579_call = mod.get_global_var('func_7579')
func_7580_call = mutated_mod.get_global_var('func_7580')
call_7943 = relay.TupleGetItem(func_7579_call(), 0)
call_7944 = relay.TupleGetItem(func_7580_call(), 0)
func_4149_call = mod.get_global_var('func_4149')
func_4151_call = mutated_mod.get_global_var('func_4151')
call_7958 = func_4149_call()
call_7959 = func_4149_call()
output = relay.Tuple([call_7943,call_7958,])
output2 = relay.Tuple([call_7944,call_7959,])
func_7968 = relay.Function([], output)
mod['func_7968'] = func_7968
mod = relay.transform.InferType()(mod)
mutated_mod['func_7968'] = func_7968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7968_call = mutated_mod.get_global_var('func_7968')
call_7969 = func_7968_call()
output = call_7969
func_7970 = relay.Function([], output)
mutated_mod['func_7970'] = func_7970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5168_call = mod.get_global_var('func_5168')
func_5169_call = mutated_mod.get_global_var('func_5169')
call_7989 = relay.TupleGetItem(func_5168_call(), 0)
call_7990 = relay.TupleGetItem(func_5169_call(), 0)
func_3674_call = mod.get_global_var('func_3674')
func_3678_call = mutated_mod.get_global_var('func_3678')
const_7992 = relay.const([[-0.015927,6.936736,-1.827629,4.836869,7.486323,9.215478,-9.186590,4.780145,0.480282,9.894718,-3.479930,5.652217],[-6.081281,1.702846,6.128084,-8.620625,9.473392,6.732924,-3.341056,7.963846,6.533351,3.204485,-6.028798,8.341655],[4.230632,-2.689985,5.095456,7.644973,-5.600879,3.970585,-2.780156,-7.702877,6.829973,-8.670835,-9.046386,5.124991]], dtype = "float32")#candidate|7992|(3, 12)|const|float32
var_7993 = relay.var("var_7993", dtype = "float64", shape = (48,))#candidate|7993|(48,)|var|float64
call_7991 = relay.TupleGetItem(func_3674_call(relay.reshape(const_7992.astype('float32'), [1, 6, 6]), relay.reshape(var_7993.astype('float64'), [48,]), ), 9)
call_7994 = relay.TupleGetItem(func_3678_call(relay.reshape(const_7992.astype('float32'), [1, 6, 6]), relay.reshape(var_7993.astype('float64'), [48,]), ), 9)
func_1090_call = mod.get_global_var('func_1090')
func_1094_call = mutated_mod.get_global_var('func_1094')
var_8007 = relay.var("var_8007", dtype = "bool", shape = (208,))#candidate|8007|(208,)|var|bool
var_8008 = relay.var("var_8008", dtype = "bool", shape = (1456,))#candidate|8008|(1456,)|var|bool
var_8009 = relay.var("var_8009", dtype = "float32", shape = (112,))#candidate|8009|(112,)|var|float32
call_8006 = relay.TupleGetItem(func_1090_call(relay.reshape(var_8007.astype('bool'), [13, 16, 1]), relay.reshape(var_8008.astype('bool'), [13, 16, 7]), relay.reshape(var_8009.astype('float32'), [112,]), ), 1)
call_8010 = relay.TupleGetItem(func_1094_call(relay.reshape(var_8007.astype('bool'), [13, 16, 1]), relay.reshape(var_8008.astype('bool'), [13, 16, 7]), relay.reshape(var_8009.astype('float32'), [112,]), ), 1)
func_6664_call = mod.get_global_var('func_6664')
func_6665_call = mutated_mod.get_global_var('func_6665')
call_8022 = relay.TupleGetItem(func_6664_call(), 0)
call_8023 = relay.TupleGetItem(func_6665_call(), 0)
func_4070_call = mod.get_global_var('func_4070')
func_4071_call = mutated_mod.get_global_var('func_4071')
call_8035 = func_4070_call()
call_8036 = func_4070_call()
func_5335_call = mod.get_global_var('func_5335')
func_5338_call = mutated_mod.get_global_var('func_5338')
call_8037 = relay.TupleGetItem(func_5335_call(relay.reshape(var_7993.astype('float64'), [4, 12])), 0)
call_8038 = relay.TupleGetItem(func_5338_call(relay.reshape(var_7993.astype('float64'), [4, 12])), 0)
bop_8054 = relay.less(call_8006.astype('bool'), relay.reshape(var_8009.astype('bool'), relay.shape_of(call_8006))) # shape=(16, 7, 1)
bop_8057 = relay.less(call_8010.astype('bool'), relay.reshape(var_8009.astype('bool'), relay.shape_of(call_8010))) # shape=(16, 7, 1)
uop_8062 = relay.sqrt(call_8035.astype('float32')) # shape=(11, 12, 15)
uop_8064 = relay.sqrt(call_8036.astype('float32')) # shape=(11, 12, 15)
output = relay.Tuple([call_7989,call_7991,const_7992,var_7993,var_8007,var_8008,call_8022,call_8037,bop_8054,uop_8062,])
output2 = relay.Tuple([call_7990,call_7994,const_7992,var_7993,var_8007,var_8008,call_8023,call_8038,bop_8057,uop_8064,])
func_8066 = relay.Function([var_7993,var_8007,var_8008,var_8009,], output)
mod['func_8066'] = func_8066
mod = relay.transform.InferType()(mod)
var_8067 = relay.var("var_8067", dtype = "float64", shape = (48,))#candidate|8067|(48,)|var|float64
var_8068 = relay.var("var_8068", dtype = "bool", shape = (208,))#candidate|8068|(208,)|var|bool
var_8069 = relay.var("var_8069", dtype = "bool", shape = (1456,))#candidate|8069|(1456,)|var|bool
var_8070 = relay.var("var_8070", dtype = "float32", shape = (112,))#candidate|8070|(112,)|var|float32
output = func_8066(var_8067,var_8068,var_8069,var_8070,)
func_8071 = relay.Function([var_8067,var_8068,var_8069,var_8070,], output)
mutated_mod['func_8071'] = func_8071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mod.get_global_var('func_4149')
func_4151_call = mutated_mod.get_global_var('func_4151')
call_8123 = func_4149_call()
call_8124 = func_4149_call()
output = call_8123
output2 = call_8124
func_8144 = relay.Function([], output)
mod['func_8144'] = func_8144
mod = relay.transform.InferType()(mod)
output = func_8144()
func_8145 = relay.Function([], output)
mutated_mod['func_8145'] = func_8145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5168_call = mod.get_global_var('func_5168')
func_5169_call = mutated_mod.get_global_var('func_5169')
call_8160 = relay.TupleGetItem(func_5168_call(), 0)
call_8161 = relay.TupleGetItem(func_5169_call(), 0)
func_5716_call = mod.get_global_var('func_5716')
func_5718_call = mutated_mod.get_global_var('func_5718')
var_8174 = relay.var("var_8174", dtype = "int64", shape = (630,))#candidate|8174|(630,)|var|int64
call_8173 = relay.TupleGetItem(func_5716_call(relay.reshape(var_8174.astype('int64'), [630,])), 1)
call_8175 = relay.TupleGetItem(func_5718_call(relay.reshape(var_8174.astype('int64'), [630,])), 1)
bop_8186 = relay.logical_xor(var_8174.astype('int64'), relay.reshape(call_8173.astype('int64'), relay.shape_of(var_8174))) # shape=(630,)
bop_8189 = relay.logical_xor(var_8174.astype('int64'), relay.reshape(call_8175.astype('int64'), relay.shape_of(var_8174))) # shape=(630,)
output = relay.Tuple([call_8160,bop_8186,])
output2 = relay.Tuple([call_8161,bop_8189,])
func_8194 = relay.Function([var_8174,], output)
mod['func_8194'] = func_8194
mod = relay.transform.InferType()(mod)
mutated_mod['func_8194'] = func_8194
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8195 = relay.var("var_8195", dtype = "int64", shape = (630,))#candidate|8195|(630,)|var|int64
func_8194_call = mutated_mod.get_global_var('func_8194')
call_8196 = func_8194_call(var_8195)
output = call_8196
func_8197 = relay.Function([var_8195], output)
mutated_mod['func_8197'] = func_8197
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8237 = relay.var("var_8237", dtype = "float64", shape = (14, 5, 12))#candidate|8237|(14, 5, 12)|var|float64
var_8238 = relay.var("var_8238", dtype = "float64", shape = (14, 5, 12))#candidate|8238|(14, 5, 12)|var|float64
bop_8239 = relay.power(var_8237.astype('float64'), relay.reshape(var_8238.astype('float64'), relay.shape_of(var_8237))) # shape=(14, 5, 12)
func_6533_call = mod.get_global_var('func_6533')
func_6535_call = mutated_mod.get_global_var('func_6535')
call_8255 = func_6533_call()
call_8256 = func_6533_call()
output = relay.Tuple([bop_8239,call_8255,])
output2 = relay.Tuple([bop_8239,call_8256,])
func_8261 = relay.Function([var_8237,var_8238,], output)
mod['func_8261'] = func_8261
mod = relay.transform.InferType()(mod)
var_8262 = relay.var("var_8262", dtype = "float64", shape = (14, 5, 12))#candidate|8262|(14, 5, 12)|var|float64
var_8263 = relay.var("var_8263", dtype = "float64", shape = (14, 5, 12))#candidate|8263|(14, 5, 12)|var|float64
output = func_8261(var_8262,var_8263,)
func_8264 = relay.Function([var_8262,var_8263,], output)
mutated_mod['func_8264'] = func_8264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7579_call = mod.get_global_var('func_7579')
func_7580_call = mutated_mod.get_global_var('func_7580')
call_8323 = relay.TupleGetItem(func_7579_call(), 0)
call_8324 = relay.TupleGetItem(func_7580_call(), 0)
output = relay.Tuple([call_8323,])
output2 = relay.Tuple([call_8324,])
func_8342 = relay.Function([], output)
mod['func_8342'] = func_8342
mod = relay.transform.InferType()(mod)
output = func_8342()
func_8343 = relay.Function([], output)
mutated_mod['func_8343'] = func_8343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7238_call = mod.get_global_var('func_7238')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_8351 = func_7238_call()
call_8352 = func_7238_call()
func_5335_call = mod.get_global_var('func_5335')
func_5338_call = mutated_mod.get_global_var('func_5338')
const_8361 = relay.const([-2.704048,5.578715,7.879193,-1.102908,8.359192,-3.251117,8.184671,-8.268644,-3.170100,-8.723378,1.443167,6.196505,0.432946,5.360786,-7.575608,-9.577356,6.228873,6.141037,-6.560251,9.687970,7.791696,7.135444,6.005850,-1.690923,-8.819222,-9.186667,-7.866700,-8.477535,-8.255066,-5.041580,-5.093472,9.363944,7.449147,-3.999250,1.862659,3.715829,4.973981,0.979883,-3.767639,6.185738,-8.054334,-6.664918,6.608035,3.552822,-9.413947,-2.938221,-7.588583,4.144830], dtype = "float64")#candidate|8361|(48,)|const|float64
call_8360 = relay.TupleGetItem(func_5335_call(relay.reshape(const_8361.astype('float64'), [4, 12])), 0)
call_8362 = relay.TupleGetItem(func_5338_call(relay.reshape(const_8361.astype('float64'), [4, 12])), 0)
output = relay.Tuple([call_8351,call_8360,const_8361,])
output2 = relay.Tuple([call_8352,call_8362,const_8361,])
func_8363 = relay.Function([], output)
mod['func_8363'] = func_8363
mod = relay.transform.InferType()(mod)
mutated_mod['func_8363'] = func_8363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8363_call = mutated_mod.get_global_var('func_8363')
call_8364 = func_8363_call()
output = call_8364
func_8365 = relay.Function([], output)
mutated_mod['func_8365'] = func_8365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7911_call = mod.get_global_var('func_7911')
func_7913_call = mutated_mod.get_global_var('func_7913')
call_8434 = relay.TupleGetItem(func_7911_call(), 1)
call_8435 = relay.TupleGetItem(func_7913_call(), 1)
output = call_8434
output2 = call_8435
func_8489 = relay.Function([], output)
mod['func_8489'] = func_8489
mod = relay.transform.InferType()(mod)
mutated_mod['func_8489'] = func_8489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8489_call = mutated_mod.get_global_var('func_8489')
call_8490 = func_8489_call()
output = call_8490
func_8491 = relay.Function([], output)
mutated_mod['func_8491'] = func_8491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5043_call = mod.get_global_var('func_5043')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_8495 = relay.TupleGetItem(func_5043_call(), 0)
call_8496 = relay.TupleGetItem(func_5044_call(), 0)
output = call_8495
output2 = call_8496
func_8501 = relay.Function([], output)
mod['func_8501'] = func_8501
mod = relay.transform.InferType()(mod)
mutated_mod['func_8501'] = func_8501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8501_call = mutated_mod.get_global_var('func_8501')
call_8502 = func_8501_call()
output = call_8502
func_8503 = relay.Function([], output)
mutated_mod['func_8503'] = func_8503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5295_call = mod.get_global_var('func_5295')
func_5296_call = mutated_mod.get_global_var('func_5296')
call_8530 = func_5295_call()
call_8531 = func_5295_call()
func_4830_call = mod.get_global_var('func_4830')
func_4832_call = mutated_mod.get_global_var('func_4832')
call_8539 = relay.TupleGetItem(func_4830_call(), 2)
call_8540 = relay.TupleGetItem(func_4832_call(), 2)
const_8545 = relay.const([[[2.329124,-0.810023,-9.221916,-6.468391,2.839548,-4.155291,-1.285722,-6.217815,-8.020720,4.342102,2.746360,6.266182,-8.499128,-1.714149,6.539975],[7.438547,-9.719249,5.530396,-2.851628,-9.836582,-9.722944,9.888569,3.454927,-6.157390,8.047984,9.314215,8.775066,-6.600385,6.249285,4.918302],[2.241414,-7.594318,-6.765073,-7.561046,0.415193,0.755818,9.092518,2.406580,-5.612682,-1.780393,1.853037,-2.838161,-4.681826,-4.851246,8.243333],[6.363990,0.502382,4.792187,0.637052,-4.188334,-2.693471,3.154089,-7.037315,7.448230,-6.735025,-4.227886,2.975742,-6.378409,-4.942925,1.439907],[-1.351336,-8.096903,-5.425842,-6.946213,5.356228,0.693101,-0.731227,8.795709,3.388951,3.362000,-6.955330,3.932686,8.616821,4.917378,9.088195],[3.043671,2.259879,6.381402,2.229254,-1.874806,-4.608490,0.974255,-3.705817,6.498352,6.320080,1.161699,7.948610,8.203984,7.511172,-0.708380],[7.649674,-7.139528,4.542551,0.315278,2.961383,2.168979,3.169371,-9.996100,8.719382,3.989651,9.006610,-1.033107,8.223924,2.227137,-8.430910],[3.298169,1.139882,7.173863,6.437297,-1.804215,-1.780829,-6.696053,-1.683752,9.489347,8.201061,-7.764147,0.832585,3.752261,-7.060609,5.428463],[-5.234398,-0.242847,6.439760,-2.646987,-5.604154,8.547782,-3.495035,-7.180954,2.319468,-5.179293,-8.266113,3.121372,2.670829,5.245542,5.364891],[-4.610643,1.329893,0.324957,-6.961710,-7.325667,-3.067529,9.664184,4.003943,6.232462,7.346296,5.930636,-7.220636,-2.439131,5.042019,6.353095],[-0.873865,-0.283002,6.567006,-1.970529,0.509529,-3.170936,7.651724,-2.102049,-8.241039,9.547756,6.921324,4.138829,4.418055,4.946683,9.508578],[6.106827,1.443898,-2.574952,3.569488,-9.956148,8.402915,3.276069,9.315083,1.984572,0.771252,7.239243,-7.020421,2.125537,-2.225633,-3.840007]],[[3.870920,-0.342039,-3.490374,3.294582,7.955846,-3.516331,0.662412,7.212354,-8.867219,-0.163620,9.318271,-7.666971,-3.482988,9.618813,0.277140],[9.646311,4.084038,2.943230,-2.003722,-6.199985,-9.768451,-9.337672,-2.389096,-6.032272,-6.674920,-7.878635,9.691574,1.600512,-0.602213,-4.082440],[6.511498,3.288044,7.425741,-7.504816,1.516517,-1.218331,6.750241,5.199291,-8.895411,-5.775750,-7.862168,8.394747,-6.691206,-6.880942,6.193508],[-8.652284,-5.865229,-8.128073,-7.138554,7.291270,6.667880,2.896535,-7.825531,-0.143976,0.997079,1.927175,4.287588,1.440508,-6.101541,1.838024],[-9.172711,-8.505338,7.285533,6.800621,4.121020,3.800548,-8.690238,7.243268,-6.265651,6.487217,7.350065,5.712979,8.618156,-9.222894,-9.829190],[-2.969649,3.481370,9.188713,7.738600,-0.485050,2.042777,4.909939,-6.094985,-2.231112,-7.616900,-1.352126,9.585633,-4.523877,-8.458600,-3.405173],[-7.037580,-8.978581,7.275952,-4.368839,-8.910051,3.491227,7.001586,4.157947,1.852567,-7.760213,5.208364,1.902119,-4.039785,-3.367045,-4.736316],[-6.377066,0.469045,-5.264210,-5.617732,9.169410,1.044061,9.162395,4.028741,8.911819,-4.619356,-9.844001,-1.075836,-1.968334,5.832362,-2.645441],[5.394538,6.103381,9.580539,7.714166,-9.006516,-4.689393,9.290852,-5.982010,-6.157229,-9.536499,0.923184,-4.026949,-1.374449,2.655477,8.777892],[-2.347374,-6.336930,0.828868,4.547425,1.910934,9.663282,-9.775318,8.744111,3.768011,-0.908114,6.639604,-6.209008,2.463882,-0.132435,8.577689],[-1.725151,2.864927,5.012396,-9.104735,7.511450,-5.488322,1.662905,-8.071137,-2.753192,-7.258134,1.286949,-6.979155,-0.037221,-9.887665,-5.563785],[-7.060900,5.097690,3.597428,1.016985,-1.797630,-5.774901,2.190305,4.865778,-1.773714,-9.026661,-1.806318,-1.615820,2.831343,-8.918769,-2.668538]],[[1.979778,-9.005716,-9.588654,5.777688,8.957215,-2.682428,2.506960,-3.643789,7.712837,-2.099005,0.786501,3.423789,5.939014,-7.288604,0.457712],[2.202240,-4.197218,7.420845,2.002069,-3.937743,-5.268401,-5.525044,-0.303118,-1.253742,-7.924499,6.696184,7.425215,3.695032,-3.287520,2.229509],[-2.296248,-1.881685,-8.438642,3.745280,7.714073,-4.696145,1.303035,1.980003,4.941535,3.058198,-3.016151,-0.705341,-5.246521,-6.908701,9.328609],[-3.129825,-2.065197,-3.690617,-6.000398,9.139931,9.202756,-6.920679,-3.376517,7.185491,3.956302,4.144810,7.904793,-2.920243,-1.733101,-3.579406],[-6.182318,7.765603,-5.499215,2.868751,-3.321961,-2.758511,-9.481375,-5.312435,-4.069982,3.702105,-1.896782,2.735840,-1.767378,4.837586,-3.654601],[-1.826897,-2.278228,-6.387327,-9.209416,-2.099956,-5.222540,-1.387421,0.196294,7.152373,-4.226428,7.897318,-8.446467,8.854688,-8.255223,8.557182],[-8.083066,6.676928,9.857829,5.314155,8.585029,-6.132905,-8.957865,5.272988,5.808812,1.620855,2.361149,0.705400,2.545859,-8.307347,0.946463],[8.888520,1.349578,4.573265,-8.187716,-5.380469,-9.001907,8.329302,-3.138399,-4.104892,2.613301,2.938130,-6.881547,-7.364512,0.700843,-2.079311],[-8.407309,3.072016,-6.491717,8.877217,5.808016,4.027946,-3.853244,2.070891,5.551962,8.882638,0.027247,8.011863,8.245728,-2.140271,-4.964815],[8.155917,-1.832848,-1.302694,6.023419,8.114663,-3.268408,-9.198874,1.304775,1.997770,6.220077,8.720666,9.562723,6.526801,1.323291,-8.933854],[-2.226786,-5.830527,-1.841526,4.990855,-4.495197,-3.409440,3.873734,-5.080577,-3.854494,0.107209,-3.307972,2.727642,7.321248,-7.942920,-2.646585],[-1.522881,-7.478717,3.717939,-7.436772,8.380522,9.112829,1.782438,-8.560570,2.904837,0.999148,2.268886,8.198893,3.238457,1.891275,3.840141]],[[-3.444588,-2.608267,4.933872,0.089542,-4.186529,-1.861051,1.535566,8.617646,3.944632,-9.643532,7.722963,-1.433643,-4.221412,-9.800959,9.940770],[5.119870,4.923697,7.034772,8.951858,-4.548879,7.879421,3.158085,-4.220356,-4.144448,7.810949,-0.996715,-0.436682,-3.220478,2.113625,-0.008155],[-9.968288,-2.261619,4.769085,-2.642166,0.223933,6.036261,-7.861263,3.479242,0.352892,-6.013068,-8.193905,0.533578,-5.403672,-0.801955,-0.616618],[-7.965109,-9.324983,6.019781,-0.286392,3.517289,-5.491000,-7.079957,5.554918,-3.748969,-1.096970,-2.600602,6.545992,7.701181,1.804450,3.733238],[5.510528,-3.576573,3.464749,4.033016,-5.962624,4.759273,0.535004,5.833424,3.188745,0.463649,-5.221373,-8.606096,-2.417895,7.846634,9.015484],[6.475576,4.944007,0.598794,8.753829,-3.486782,1.523104,9.227752,-3.456514,7.805923,-8.905844,5.723015,-8.383706,-4.445038,8.411936,-0.697948],[4.544824,4.623866,-5.105534,7.970264,-1.272206,2.280790,1.541499,-7.508709,5.442452,4.440856,9.233887,-2.871869,-1.273808,-3.960659,8.505759],[6.938079,-3.211770,6.899274,8.602678,3.965404,-9.412652,8.922287,1.527374,9.309517,9.072547,-6.262162,8.443334,1.322246,3.616010,-2.572739],[-7.815508,7.259561,-6.843939,4.038300,5.356625,3.558027,2.616726,8.516477,3.976333,9.967502,5.351392,8.838985,9.646892,9.786757,-8.530838],[3.835648,8.910506,1.576206,7.008290,3.867462,4.094919,-2.286206,7.257173,6.336459,1.234597,1.633596,-8.256879,7.200649,1.238743,3.257071],[-3.467179,3.350619,9.707852,-6.907830,3.167681,-5.605117,-1.060639,-3.539022,-9.404388,-8.277922,-7.251372,0.648390,-4.602763,-0.353096,6.830648],[4.835271,-1.887530,5.710721,-7.842427,-6.380776,4.471328,-4.961877,-2.017756,3.746909,1.549131,-9.944197,7.241237,-8.464841,-6.993671,-7.419763]],[[-0.042775,-4.985676,-9.967721,7.612742,0.501602,-8.747077,-4.642749,-0.895106,0.522845,7.137758,-1.427888,1.226206,1.141997,8.525235,-0.266464],[5.051504,-2.164474,-4.867777,9.480001,8.224513,4.282998,6.591199,-3.323211,-1.536707,1.811074,-8.328237,1.295003,-9.197991,-0.790395,3.179456],[2.638941,8.604017,-6.380798,-0.900208,0.755654,-9.787824,0.774300,-4.336945,4.820579,-3.707737,4.555938,-9.187032,-8.745870,0.023767,5.589656],[9.269594,-8.872352,-3.557305,-6.361344,-7.207621,-4.041306,5.385997,1.231438,0.209311,-5.896915,6.101645,6.558274,2.768305,-3.583067,-7.052669],[9.659911,-3.426325,-4.337985,-7.731328,2.128120,4.809698,5.999444,-6.582226,-0.865085,2.799813,2.726355,-4.521532,4.933167,-1.464497,2.812307],[4.973233,-2.899218,-1.811256,-5.667097,-7.019662,6.081992,1.678481,-4.569832,1.106136,8.701043,8.808686,-5.075398,1.906430,5.996961,5.214052],[-5.232431,1.245069,0.962421,-1.602767,-7.591026,3.951293,-1.912938,-9.856324,-0.793067,1.451884,1.755400,-3.503969,1.837278,2.105164,6.878096],[6.122751,2.447528,6.605884,-8.112215,-4.992480,-6.240185,-9.921835,-5.355484,2.881394,4.969515,-0.133123,6.508580,-1.444854,1.417756,-6.763803],[-6.287121,-7.818995,-4.820120,-8.910576,7.708278,-8.486450,1.428038,-6.299764,7.741772,-0.964364,9.004393,1.159773,-2.752290,7.132727,3.640002],[-2.517984,4.791145,1.694543,-7.422758,-8.621942,-8.641746,5.905589,4.619142,0.572702,9.034080,3.398092,0.548374,-0.494023,-2.452643,1.905435],[3.710840,-1.082989,-3.428352,-9.279200,6.141659,0.377832,1.594776,7.972217,-1.153714,-6.888250,3.031747,-0.161422,-7.207250,-0.269806,-3.837655],[7.870740,5.481433,-6.181717,0.116967,6.306067,2.345548,7.925899,8.793985,-6.193850,3.781858,-6.355669,-4.743331,3.668325,4.289813,-6.391375]],[[6.383879,8.279252,5.532837,9.981896,-8.704494,7.378046,6.366250,4.862057,-3.360072,-3.755559,-3.124288,-4.466333,-5.351527,0.342132,1.636072],[2.144676,8.375988,4.438839,5.762619,-2.209211,7.953748,1.820672,-8.731654,-4.278778,-0.002962,-4.251718,3.239272,-9.661324,4.871737,1.096979],[6.735450,6.363584,8.905298,7.584039,1.802526,-6.386139,9.569330,4.934566,-6.974351,-1.809774,9.973490,9.510723,6.911552,-4.333495,-4.005495],[1.458885,-8.020497,-2.212021,-5.457644,-6.339832,0.184898,-4.752190,3.353655,-6.846099,2.350659,-9.839979,-5.390069,9.090676,8.942607,-9.548696],[9.499124,1.628692,-7.196297,3.849951,6.227021,1.477717,2.522914,-5.076909,1.216444,-1.792305,9.375026,7.314932,5.480363,-2.440475,-7.286384],[-8.692599,-0.771707,-6.389567,4.916569,8.954619,5.118322,-2.050054,0.448350,1.281573,0.890579,9.479515,3.276337,-0.482886,-0.579685,7.824255],[5.020608,-6.885456,-4.757746,0.809316,5.926003,-8.260187,8.225432,5.661039,4.609264,5.786127,-4.895834,-4.023568,-5.313851,-1.898339,7.369338],[4.825437,6.941868,-0.753438,-3.864610,-7.036007,0.847755,4.204830,3.087183,8.821384,6.289816,5.982580,2.616935,2.933928,4.879716,-8.488197],[-0.256394,8.728583,-4.217698,6.808010,5.195312,-1.424641,-8.846016,0.736552,-1.281582,6.192662,-1.853618,2.995454,-0.713363,0.119913,2.852216],[-3.910642,3.115487,9.598725,8.862647,3.443686,-1.422821,7.431159,4.243951,-8.294089,7.244630,6.661818,9.112685,-1.673894,-9.805473,3.123950],[6.964246,4.125492,7.252801,-1.082330,2.863309,-8.852556,4.197831,-7.406786,-6.761119,-9.592611,-5.178282,2.458985,3.073699,7.726605,1.407923],[2.240578,-5.091276,-9.076900,5.048416,3.705271,-2.058736,8.875564,3.481748,-7.633322,-9.735829,-5.026769,-5.508052,-6.649352,0.342772,5.839153]],[[-6.498206,3.357033,4.205261,2.140073,9.364842,4.794403,-3.409132,0.329658,5.524716,9.794505,3.576365,-5.638992,-5.024797,3.843610,4.412593],[-7.794590,6.844308,-7.866093,0.414783,2.415160,-5.427444,-0.098399,2.438733,4.845225,5.486512,4.506568,-5.526634,0.499590,-9.120276,-5.138052],[2.699394,-8.789798,-7.043516,-7.490097,-6.638690,-7.517494,-7.246410,4.909742,9.847142,-4.771930,0.878253,4.518844,-0.798486,-0.469383,8.315212],[-7.547675,-3.560581,8.984819,0.435168,-8.755470,3.562058,3.163923,-2.128784,-0.034959,2.749743,-5.196943,-4.322090,-0.644379,-0.136191,2.905241],[0.724803,8.038572,-7.708181,-9.246054,-3.674237,6.064683,-3.589891,5.436404,9.353287,-4.844139,0.395469,-4.812117,-0.389718,-1.141792,4.621707],[-1.108892,2.751448,-7.486888,-9.663168,0.767551,-0.770607,-9.048021,6.331698,4.194559,0.829309,7.339597,-0.167085,-1.134369,-4.847739,-9.265059],[3.977178,-7.408231,-7.500237,-4.813186,-2.357463,9.933558,4.751210,2.371568,3.718118,9.423632,-7.983504,3.273917,-5.170111,2.936582,-9.997096],[2.859728,-7.424492,-1.941915,-4.919287,9.626723,0.512168,4.375984,-7.266002,2.239868,9.850201,9.932677,-9.152351,0.225207,-7.405152,7.258690],[-1.289797,-0.090233,7.439348,5.969432,-6.645569,-5.673972,9.171925,-4.090263,-9.288569,5.981016,-5.180908,3.440765,-7.946005,-1.406934,7.192861],[8.179180,-8.895157,-9.392039,1.076810,2.618638,-2.505597,1.595582,-1.438152,5.304225,6.902272,-6.507020,6.181566,-2.527675,-0.516204,6.396921],[5.306485,7.444720,-2.972604,7.015756,4.947385,6.241952,-9.432752,9.425878,-4.273692,5.742039,-8.237735,-5.102102,9.921083,0.987420,5.136710],[4.911023,6.382157,-1.711438,-2.397029,6.622517,-6.338738,3.952297,0.586325,0.470625,1.733828,-5.561284,2.813563,-8.956115,9.954326,-2.547612]],[[-7.656969,9.134379,7.760768,8.716722,1.487963,2.279971,-2.983751,-2.350490,-0.105837,8.578863,-7.899561,6.768311,-7.940608,-7.212826,1.610756],[-9.783918,-3.050226,4.755903,4.620302,7.426584,-1.252515,6.747867,2.579311,-1.901444,4.311402,-0.601747,5.092353,3.092799,7.123195,-4.129907],[0.652088,-0.788293,-6.260282,3.684994,-7.648798,9.470032,3.914203,7.216845,-1.103205,-4.470704,-5.188572,-1.414196,-6.172820,2.734008,4.515840],[-8.941219,6.811889,7.453694,6.569925,1.663643,8.610962,-2.372970,4.385266,-3.136325,1.560034,-2.333404,1.053826,-6.289489,-1.307848,7.894606],[0.467383,-2.393738,-6.965390,-6.055284,-7.438047,6.070378,-5.424634,4.557064,-2.108674,-2.756623,-1.883541,0.746185,7.607207,-9.785279,9.993362],[0.892980,3.220331,5.913474,3.876228,4.030362,-4.027547,-2.736140,-0.721112,-8.727338,7.021197,8.228245,0.677534,7.908221,-7.234251,8.248197],[2.726829,-5.833920,-5.739752,-3.606266,0.256506,-0.275356,-1.055693,9.420199,-4.567610,6.348701,-4.691818,9.305982,9.446027,-6.674820,-9.191840],[-1.443989,-8.208859,0.671696,-8.623190,4.639177,2.260030,9.995326,-9.360921,2.534555,6.661953,-0.172830,4.531633,2.330780,-5.161100,-0.437626],[5.066957,-1.684479,8.804802,2.174053,7.080166,8.222304,-2.277490,-9.450423,8.575852,3.762554,1.107376,-7.171833,6.851401,0.071629,7.794005],[5.475464,-9.212757,6.459251,7.499142,-7.662972,0.021566,5.003102,-1.345360,-3.272215,9.712938,-7.338827,2.293042,4.714402,7.376132,-5.543517],[-5.502402,4.120384,6.009967,-3.269037,4.870646,2.992363,8.575699,-8.800075,-2.626500,7.726864,-8.559831,-1.158037,0.501261,1.951860,5.928925],[6.465892,3.623228,-7.878802,1.067420,3.468497,1.579166,3.119332,1.231853,2.701587,-7.491293,-1.288469,-3.026707,-6.953397,-6.511792,-0.377375]],[[7.226510,-1.872334,4.021813,2.839789,5.641421,6.446255,4.299839,3.138342,5.829449,7.670305,-5.098356,-6.064280,-8.071925,-5.986644,-6.855920],[-9.517972,-9.464255,-8.340594,-2.658462,7.644085,-7.491200,-8.489519,7.848687,8.613463,-7.200437,0.924864,-1.718689,-9.425432,-8.447921,7.040010],[5.561653,5.021350,-1.759998,8.695175,9.264663,5.557181,-8.238547,-9.322491,8.175897,-5.196220,-7.889282,-0.058146,1.264557,0.414221,9.656330],[3.201529,6.618879,9.552909,-2.221844,-3.144632,6.993864,-0.969584,6.445681,7.249123,-1.660365,8.927993,5.066115,9.406746,-5.240248,0.717345],[0.021814,-3.438306,1.438193,4.056153,2.968090,7.249551,8.011341,-8.197435,-8.100244,0.564987,4.642770,4.308582,6.950886,5.004795,-3.033506],[0.176146,7.272286,-4.073018,7.375252,9.026566,0.435501,9.574746,-1.451280,3.192088,-9.355369,6.365115,8.481962,-0.928809,3.390368,-4.112168],[-8.415352,0.537511,-6.938685,-3.623385,1.232532,-7.029944,3.303799,7.569508,1.863637,-7.432705,-9.272948,3.168449,9.432506,-2.381151,2.046204],[-8.094672,-2.054535,-0.688173,7.878461,1.921345,-7.247847,9.506845,4.260929,1.465253,1.558851,-6.960620,6.112007,-3.668282,-3.021359,8.596401],[3.049097,1.549618,1.943343,-9.611902,7.270031,-6.182796,0.290173,8.564285,-7.332994,8.373303,-8.813331,7.586338,7.683827,-6.916618,-2.953476],[-2.031717,9.077141,-8.326911,1.706011,9.824611,-0.605568,-6.168831,1.410916,-4.145564,-0.396257,-6.715231,-4.647231,-0.667852,2.318596,1.966243],[-2.508932,6.182615,4.343242,-7.416444,9.096610,6.711533,5.048529,3.418545,9.374741,7.235152,-1.976968,0.884742,5.302825,-0.338097,-1.755810],[4.621948,0.905882,0.314169,-7.626525,0.325611,2.888972,7.518998,-3.625540,-4.968816,-3.427900,6.133839,2.211500,2.709357,-4.064025,6.589604]],[[2.917950,0.588087,7.216135,-0.562663,0.022201,2.467126,-3.202557,4.574863,-6.376843,8.242886,8.867327,9.650748,0.763928,-1.207155,-9.293481],[-4.353509,-9.775141,4.126216,-3.805563,2.930229,6.770018,7.958311,7.241978,4.936666,-9.858688,-5.817274,8.248769,-3.828005,6.830982,3.782578],[-7.181784,8.532053,8.824206,-6.319256,-1.467140,3.966931,6.923334,-3.834160,-7.682088,-1.403323,-2.337854,-4.212559,-1.795733,-9.450822,3.214029],[5.307729,6.564245,-3.923107,7.183041,5.402922,-0.594374,-6.936555,6.912541,-0.735244,-4.530642,-8.647753,-5.553022,-1.709241,6.071732,-7.762752],[-7.810469,-8.298420,-5.229649,6.666797,8.814269,-2.832381,9.211659,5.383636,9.256846,-2.053489,-1.541147,-7.011128,-0.976888,4.152470,5.191063],[-9.030019,-2.374136,9.357656,-0.124077,-8.759553,9.580171,7.491291,4.453107,6.185759,5.140102,-9.101550,-4.254069,-4.110874,-4.499925,-7.746938],[1.848920,0.891083,9.624726,-7.674625,5.958261,-3.546544,4.902668,-8.718792,-2.747391,4.144758,9.801917,-6.497154,-1.340188,-0.439610,-0.487126],[-6.071282,-4.469836,5.567422,2.221362,1.872454,8.207319,7.720150,4.095838,4.240684,-5.208498,6.445530,2.068214,1.446983,-8.548042,-8.393109],[7.560421,-9.475432,-6.754147,8.898413,-0.916831,8.271178,-3.330217,-9.563608,-2.903075,-4.302407,5.930571,-3.670651,6.673959,-8.452219,-9.816100],[-3.585289,-3.473569,9.982273,2.511834,-5.136909,1.129478,0.656004,-6.415588,2.532312,8.521839,2.340979,-3.328730,1.988106,-2.027641,9.873648],[-1.597655,-1.029806,9.229233,-6.210799,-0.968025,-6.956242,-0.996369,-1.013436,0.912333,1.361834,5.851143,3.111803,-0.346000,4.187835,3.803615],[4.953386,-4.621150,-9.121106,2.811285,-6.545059,9.492575,3.092425,-8.983756,-9.780918,-2.949327,4.408791,4.201048,3.540977,4.258734,-4.880013]],[[8.878852,1.300012,4.620257,2.849301,-8.787964,-1.057351,-3.553211,9.350141,0.187535,6.231204,0.973536,5.282531,6.634924,-3.433096,1.559457],[2.186213,5.221068,9.606203,-4.352770,9.391517,-5.617143,-6.388088,-3.122638,-3.260606,-8.375386,4.987722,-6.017191,-5.223335,7.905110,-5.305929],[0.784270,3.719017,-4.432309,0.329224,-6.443702,4.336910,-3.942603,3.630270,2.115828,9.644228,1.513765,1.135437,5.372231,-7.281417,4.191048],[-5.426813,-6.677347,5.171450,-2.275261,-7.068114,4.794299,2.034967,8.212559,-3.203911,-3.515798,-0.770495,-2.263023,9.344453,1.257418,-8.850690],[0.960067,0.002707,2.377723,-6.521185,9.281035,-0.159791,1.301781,2.746285,-2.309359,2.974507,2.520305,5.657137,-1.234188,8.934967,-9.959458],[-8.830258,-3.596075,3.610871,-7.256390,0.293292,-8.029916,-4.968364,-3.225159,5.068781,-1.667189,8.029904,-7.899882,7.490725,-9.680248,0.530071],[4.875972,-9.059948,8.234415,7.618247,5.906315,-4.995969,-9.632731,0.726484,-4.327027,2.456369,-9.015240,-3.483083,7.990399,6.697686,-2.208136],[-1.247708,-3.530461,-2.430381,3.292989,9.788656,-0.973864,-6.972302,-4.189276,4.626908,-8.684581,0.463834,-8.559599,-4.319958,-4.799792,6.487399],[-2.771566,-7.627704,-1.140976,-6.740602,-1.986370,-4.459351,1.489138,0.682913,7.176325,-2.761234,8.730572,-8.402359,1.367059,-9.790621,-3.484907],[3.946604,8.739162,5.840718,-5.456519,2.880993,9.259640,6.431455,9.961520,-9.592868,-1.136265,-3.813823,5.287005,2.461303,8.608479,-7.602683],[1.607658,-5.742002,5.276260,-5.771493,-9.859653,-0.037038,4.341370,-1.139920,-9.151012,3.225588,-1.147246,-1.644967,-8.786777,-9.008720,4.542697],[9.376307,-2.847206,-2.879719,2.816375,7.512788,-5.330016,2.635994,-2.588360,-6.944813,4.479282,1.765281,-2.122995,8.700162,4.778942,-8.604586]]], dtype = "float64")#candidate|8545|(11, 12, 15)|const|float64
bop_8546 = relay.left_shift(call_8530.astype('int64'), relay.reshape(const_8545.astype('int64'), relay.shape_of(call_8530))) # shape=(11, 12, 15)
bop_8549 = relay.left_shift(call_8531.astype('int64'), relay.reshape(const_8545.astype('int64'), relay.shape_of(call_8531))) # shape=(11, 12, 15)
output = relay.Tuple([call_8539,bop_8546,])
output2 = relay.Tuple([call_8540,bop_8549,])
F = relay.Function([], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([], output2)
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
	relay.transform.FastMath(),
	relay.transform.FirstOrderGradient(),
	relay.transform.EliminateCommonSubexpr(),
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
