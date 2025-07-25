import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_62 = relay.var("var_62", dtype = "float32", shape = (15, 16, 3))#candidate|62|(15, 16, 3)|var|float32
uop_63 = relay.acos(var_62.astype('float32')) # shape=(15, 16, 3)
output = relay.Tuple([uop_63,])
output2 = relay.Tuple([uop_63,])
func_68 = relay.Function([var_62,], output)
mod['func_68'] = func_68
mod = relay.transform.InferType()(mod)
mutated_mod['func_68'] = func_68
mutated_mod = relay.transform.InferType()(mutated_mod)
var_69 = relay.var("var_69", dtype = "float32", shape = (15, 16, 3))#candidate|69|(15, 16, 3)|var|float32
func_68_call = mutated_mod.get_global_var('func_68')
call_70 = func_68_call(var_69)
output = call_70
func_71 = relay.Function([var_69], output)
mutated_mod['func_71'] = func_71
mutated_mod = relay.transform.InferType()(mutated_mod)
var_738 = relay.var("var_738", dtype = "float64", shape = (10, 11, 2))#candidate|738|(10, 11, 2)|var|float64
uop_739 = relay.log(var_738.astype('float64')) # shape=(10, 11, 2)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
var_745 = relay.var("var_745", dtype = "float32", shape = (180, 4))#candidate|745|(180, 4)|var|float32
call_744 = relay.TupleGetItem(func_68_call(relay.reshape(var_745.astype('float32'), [15, 16, 3])), 0)
call_746 = relay.TupleGetItem(func_71_call(relay.reshape(var_745.astype('float32'), [15, 16, 3])), 0)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
call_747 = relay.TupleGetItem(func_68_call(relay.reshape(call_744.astype('float32'), [15, 16, 3])), 0)
call_748 = relay.TupleGetItem(func_71_call(relay.reshape(call_744.astype('float32'), [15, 16, 3])), 0)
output = relay.Tuple([uop_739,call_744,var_745,call_747,])
output2 = relay.Tuple([uop_739,call_746,var_745,call_748,])
func_754 = relay.Function([var_738,var_745,], output)
mod['func_754'] = func_754
mod = relay.transform.InferType()(mod)
mutated_mod['func_754'] = func_754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_754_call = mutated_mod.get_global_var('func_754')
var_756 = relay.var("var_756", dtype = "float64", shape = (10, 11, 2))#candidate|756|(10, 11, 2)|var|float64
var_757 = relay.var("var_757", dtype = "float32", shape = (180, 4))#candidate|757|(180, 4)|var|float32
call_755 = func_754_call(var_756,var_757,)
output = call_755
func_758 = relay.Function([var_756,var_757,], output)
mutated_mod['func_758'] = func_758
mutated_mod = relay.transform.InferType()(mutated_mod)
var_809 = relay.var("var_809", dtype = "float64", shape = (9, 15, 14))#candidate|809|(9, 15, 14)|var|float64
var_810 = relay.var("var_810", dtype = "float64", shape = (9, 15, 14))#candidate|810|(9, 15, 14)|var|float64
bop_811 = relay.mod(var_809.astype('float64'), relay.reshape(var_810.astype('float64'), relay.shape_of(var_809))) # shape=(9, 15, 14)
output = bop_811
output2 = bop_811
func_821 = relay.Function([var_809,var_810,], output)
mod['func_821'] = func_821
mod = relay.transform.InferType()(mod)
mutated_mod['func_821'] = func_821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_821_call = mutated_mod.get_global_var('func_821')
var_823 = relay.var("var_823", dtype = "float64", shape = (9, 15, 14))#candidate|823|(9, 15, 14)|var|float64
var_824 = relay.var("var_824", dtype = "float64", shape = (9, 15, 14))#candidate|824|(9, 15, 14)|var|float64
call_822 = func_821_call(var_823,var_824,)
output = call_822
func_825 = relay.Function([var_823,var_824,], output)
mutated_mod['func_825'] = func_825
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1074 = relay.const(-3, dtype = "int64")#candidate|1074|()|const|int64
var_1075 = relay.var("var_1075", dtype = "int64", shape = (7, 6, 11))#candidate|1075|(7, 6, 11)|var|int64
bop_1076 = relay.bitwise_xor(const_1074.astype('int64'), var_1075.astype('int64')) # shape=(7, 6, 11)
output = bop_1076
output2 = bop_1076
func_1084 = relay.Function([var_1075,], output)
mod['func_1084'] = func_1084
mod = relay.transform.InferType()(mod)
mutated_mod['func_1084'] = func_1084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1085 = relay.var("var_1085", dtype = "int64", shape = (7, 6, 11))#candidate|1085|(7, 6, 11)|var|int64
func_1084_call = mutated_mod.get_global_var('func_1084')
call_1086 = func_1084_call(var_1085)
output = call_1086
func_1087 = relay.Function([var_1085], output)
mutated_mod['func_1087'] = func_1087
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1185 = relay.var("var_1185", dtype = "float32", shape = (9, 3, 9))#candidate|1185|(9, 3, 9)|var|float32
uop_1186 = relay.sqrt(var_1185.astype('float32')) # shape=(9, 3, 9)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
var_1192 = relay.var("var_1192", dtype = "float32", shape = (720, 1))#candidate|1192|(720, 1)|var|float32
call_1191 = relay.TupleGetItem(func_68_call(relay.reshape(var_1192.astype('float32'), [15, 16, 3])), 0)
call_1193 = relay.TupleGetItem(func_71_call(relay.reshape(var_1192.astype('float32'), [15, 16, 3])), 0)
uop_1196 = relay.sin(call_1191.astype('float64')) # shape=(15, 16, 3)
uop_1198 = relay.sin(call_1193.astype('float64')) # shape=(15, 16, 3)
func_754_call = mod.get_global_var('func_754')
func_758_call = mutated_mod.get_global_var('func_758')
const_1212 = relay.const([-4.259601,-1.148099,6.090383,-4.123222,4.675996,8.102253,-3.651334,-9.668113,-0.368443,-7.793527,8.014150,-3.014975,3.372262,-9.557231,-5.511597,1.830689,-4.628769,-4.845975,7.761060,-4.253622,-4.866977,0.705636,7.971912,4.207880,-8.842683,3.242129,9.884659,2.393200,-5.408268,9.486914,3.572838,0.855641,9.718622,8.562613,-3.206647,0.862222,0.577204,-6.755449,-5.339626,-1.240353,9.177178,-1.903198,4.020952,-9.350571,4.890413,0.082430,-1.939740,-8.481480,-7.885420,3.423259,3.897690,3.867302,8.226396,7.757286,1.847213,-5.076143,1.250162,-1.440529,0.344203,-6.492118,-8.871330,0.708973,5.678941,-9.387772,5.292192,-0.559130,-1.912321,2.857004,7.341108,0.553421,0.080466,-5.696075,-1.804249,6.962624,4.808643,-7.763107,7.240583,-3.083409,0.162500,-8.171259,-6.567096,1.247670,-7.620349,-0.276000,7.190170,5.070486,-5.553461,-4.604631,-4.258230,-9.504898,6.598849,6.385230,-7.126431,6.222301,6.746263,-4.766526,4.660775,-7.089526,-4.248496,6.594886,5.112894,-3.404194,-1.295316,-8.484585,0.770168,-0.671438,-8.167936,9.953957,-2.839261,-1.360885,8.888941,5.410579,9.466641,-8.755604,8.766928,3.265554,-6.618780,-5.895936,-8.675698,1.245936,7.864990,0.299125,-3.800939,-4.778447,2.021486,-2.282615,5.701428,2.965757,2.180459,-7.813141,-6.172324,4.839768,-8.453863,6.973476,9.480809,-1.258242,5.185624,-0.125074,-9.438516,-6.769563,1.282991,-0.209849,-8.820676,6.649101,-8.905192,-1.204777,-0.919255,7.436381,7.447403,9.723653,-7.615503,7.719926,8.940928,7.718673,-6.477948,-7.889025,-2.242702,-4.839455,-3.791345,-5.993235,-5.681606,1.613089,0.081101,2.947309,-2.349614,9.757584,-6.005712,-9.930925,-8.137842,9.246635,4.855131,-1.826265,5.467590,-2.553575,0.648659,-0.089620,-5.865951,-0.790146,-8.059213,-2.428411,-1.388603,9.844706,3.098644,8.932477,3.823455,-5.056421,-3.679116,-3.709984,-1.099453,4.279067,-1.866155,0.990383,-0.730688,-7.614386,7.236488,9.857398,-1.893976,-1.787435,-4.688369,0.691566,-8.932581,-3.731534,-3.270688,-3.856769,0.877427,-2.930544,2.577475,-2.687366,8.746034,0.469735,-4.380711,2.462560,2.158070,-8.815922,7.218321,-2.504648,1.187730,-3.293971,0.577450,-1.228296], dtype = "float64")#candidate|1212|(220,)|const|float64
call_1211 = relay.TupleGetItem(func_754_call(relay.reshape(const_1212.astype('float64'), [10, 11, 2]), relay.reshape(var_1192.astype('float32'), [180, 4]), ), 0)
call_1213 = relay.TupleGetItem(func_758_call(relay.reshape(const_1212.astype('float64'), [10, 11, 2]), relay.reshape(var_1192.astype('float32'), [180, 4]), ), 0)
func_1084_call = mod.get_global_var('func_1084')
func_1087_call = mutated_mod.get_global_var('func_1087')
var_1226 = relay.var("var_1226", dtype = "int64", shape = (462,))#candidate|1226|(462,)|var|int64
call_1225 = func_1084_call(relay.reshape(var_1226.astype('int64'), [7, 6, 11]))
call_1227 = func_1084_call(relay.reshape(var_1226.astype('int64'), [7, 6, 11]))
uop_1232 = relay.atan(uop_1196.astype('float64')) # shape=(15, 16, 3)
uop_1234 = relay.atan(uop_1198.astype('float64')) # shape=(15, 16, 3)
bop_1238 = relay.bitwise_xor(uop_1186.astype('int8'), relay.reshape(var_1185.astype('int8'), relay.shape_of(uop_1186))) # shape=(9, 3, 9)
uop_1242 = relay.sqrt(uop_1232.astype('float32')) # shape=(15, 16, 3)
uop_1244 = relay.sqrt(uop_1234.astype('float32')) # shape=(15, 16, 3)
output = relay.Tuple([var_1192,call_1211,const_1212,call_1225,var_1226,bop_1238,uop_1242,])
output2 = relay.Tuple([var_1192,call_1213,const_1212,call_1227,var_1226,bop_1238,uop_1244,])
func_1251 = relay.Function([var_1185,var_1192,var_1226,], output)
mod['func_1251'] = func_1251
mod = relay.transform.InferType()(mod)
mutated_mod['func_1251'] = func_1251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1251_call = mutated_mod.get_global_var('func_1251')
var_1253 = relay.var("var_1253", dtype = "float32", shape = (9, 3, 9))#candidate|1253|(9, 3, 9)|var|float32
var_1254 = relay.var("var_1254", dtype = "float32", shape = (720, 1))#candidate|1254|(720, 1)|var|float32
var_1255 = relay.var("var_1255", dtype = "int64", shape = (462,))#candidate|1255|(462,)|var|int64
call_1252 = func_1251_call(var_1253,var_1254,var_1255,)
output = call_1252
func_1256 = relay.Function([var_1253,var_1254,var_1255,], output)
mutated_mod['func_1256'] = func_1256
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1291 = relay.var("var_1291", dtype = "int64", shape = ())#candidate|1291|()|var|int64
var_1292 = relay.var("var_1292", dtype = "int64", shape = (1, 15, 6))#candidate|1292|(1, 15, 6)|var|int64
bop_1293 = relay.less_equal(var_1291.astype('bool'), var_1292.astype('bool')) # shape=(1, 15, 6)
output = bop_1293
output2 = bop_1293
func_1302 = relay.Function([var_1291,var_1292,], output)
mod['func_1302'] = func_1302
mod = relay.transform.InferType()(mod)
mutated_mod['func_1302'] = func_1302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mutated_mod.get_global_var('func_1302')
var_1304 = relay.var("var_1304", dtype = "int64", shape = ())#candidate|1304|()|var|int64
var_1305 = relay.var("var_1305", dtype = "int64", shape = (1, 15, 6))#candidate|1305|(1, 15, 6)|var|int64
call_1303 = func_1302_call(var_1304,var_1305,)
output = call_1303
func_1306 = relay.Function([var_1304,var_1305,], output)
mutated_mod['func_1306'] = func_1306
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1671 = relay.var("var_1671", dtype = "int32", shape = ())#candidate|1671|()|var|int32
const_1672 = relay.const([[-9,-6,-5]], dtype = "int32")#candidate|1672|(1, 3)|const|int32
bop_1673 = relay.less_equal(var_1671.astype('bool'), const_1672.astype('bool')) # shape=(1, 3)
output = bop_1673
output2 = bop_1673
func_1679 = relay.Function([var_1671,], output)
mod['func_1679'] = func_1679
mod = relay.transform.InferType()(mod)
mutated_mod['func_1679'] = func_1679
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1680 = relay.var("var_1680", dtype = "int32", shape = ())#candidate|1680|()|var|int32
func_1679_call = mutated_mod.get_global_var('func_1679')
call_1681 = func_1679_call(var_1680)
output = call_1681
func_1682 = relay.Function([var_1680], output)
mutated_mod['func_1682'] = func_1682
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1847 = relay.var("var_1847", dtype = "float64", shape = (16, 16, 8))#candidate|1847|(16, 16, 8)|var|float64
uop_1848 = relay.exp(var_1847.astype('float64')) # shape=(16, 16, 8)
output = uop_1848
output2 = uop_1848
func_1863 = relay.Function([var_1847,], output)
mod['func_1863'] = func_1863
mod = relay.transform.InferType()(mod)
var_1864 = relay.var("var_1864", dtype = "float64", shape = (16, 16, 8))#candidate|1864|(16, 16, 8)|var|float64
output = func_1863(var_1864)
func_1865 = relay.Function([var_1864], output)
mutated_mod['func_1865'] = func_1865
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2033 = relay.var("var_2033", dtype = "uint64", shape = (1, 2, 3))#candidate|2033|(1, 2, 3)|var|uint64
var_2034 = relay.var("var_2034", dtype = "uint64", shape = (10, 2, 3))#candidate|2034|(10, 2, 3)|var|uint64
bop_2035 = relay.subtract(var_2033.astype('uint64'), var_2034.astype('uint64')) # shape=(10, 2, 3)
output = bop_2035
output2 = bop_2035
func_2040 = relay.Function([var_2033,var_2034,], output)
mod['func_2040'] = func_2040
mod = relay.transform.InferType()(mod)
mutated_mod['func_2040'] = func_2040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2040_call = mutated_mod.get_global_var('func_2040')
var_2042 = relay.var("var_2042", dtype = "uint64", shape = (1, 2, 3))#candidate|2042|(1, 2, 3)|var|uint64
var_2043 = relay.var("var_2043", dtype = "uint64", shape = (10, 2, 3))#candidate|2043|(10, 2, 3)|var|uint64
call_2041 = func_2040_call(var_2042,var_2043,)
output = call_2041
func_2044 = relay.Function([var_2042,var_2043,], output)
mutated_mod['func_2044'] = func_2044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2259 = relay.var("var_2259", dtype = "int16", shape = (7, 11, 7))#candidate|2259|(7, 11, 7)|var|int16
var_2260 = relay.var("var_2260", dtype = "int16", shape = (7, 11, 7))#candidate|2260|(7, 11, 7)|var|int16
bop_2261 = relay.greater(var_2259.astype('bool'), relay.reshape(var_2260.astype('bool'), relay.shape_of(var_2259))) # shape=(7, 11, 7)
func_1251_call = mod.get_global_var('func_1251')
func_1256_call = mutated_mod.get_global_var('func_1256')
var_2279 = relay.var("var_2279", dtype = "float32", shape = (243,))#candidate|2279|(243,)|var|float32
var_2280 = relay.var("var_2280", dtype = "float32", shape = (720,))#candidate|2280|(720,)|var|float32
var_2281 = relay.var("var_2281", dtype = "int64", shape = (462,))#candidate|2281|(462,)|var|int64
call_2278 = relay.TupleGetItem(func_1251_call(relay.reshape(var_2279.astype('float32'), [9, 3, 9]), relay.reshape(var_2280.astype('float32'), [720, 1]), relay.reshape(var_2281.astype('int64'), [462,]), ), 4)
call_2282 = relay.TupleGetItem(func_1256_call(relay.reshape(var_2279.astype('float32'), [9, 3, 9]), relay.reshape(var_2280.astype('float32'), [720, 1]), relay.reshape(var_2281.astype('int64'), [462,]), ), 4)
uop_2289 = relay.tan(call_2278.astype('float32')) # shape=(462,)
uop_2291 = relay.tan(call_2282.astype('float32')) # shape=(462,)
uop_2292 = relay.exp(bop_2261.astype('float32')) # shape=(7, 11, 7)
output = relay.Tuple([var_2279,var_2280,var_2281,uop_2289,uop_2292,])
output2 = relay.Tuple([var_2279,var_2280,var_2281,uop_2291,uop_2292,])
func_2297 = relay.Function([var_2259,var_2260,var_2279,var_2280,var_2281,], output)
mod['func_2297'] = func_2297
mod = relay.transform.InferType()(mod)
var_2298 = relay.var("var_2298", dtype = "int16", shape = (7, 11, 7))#candidate|2298|(7, 11, 7)|var|int16
var_2299 = relay.var("var_2299", dtype = "int16", shape = (7, 11, 7))#candidate|2299|(7, 11, 7)|var|int16
var_2300 = relay.var("var_2300", dtype = "float32", shape = (243,))#candidate|2300|(243,)|var|float32
var_2301 = relay.var("var_2301", dtype = "float32", shape = (720,))#candidate|2301|(720,)|var|float32
var_2302 = relay.var("var_2302", dtype = "int64", shape = (462,))#candidate|2302|(462,)|var|int64
output = func_2297(var_2298,var_2299,var_2300,var_2301,var_2302,)
func_2303 = relay.Function([var_2298,var_2299,var_2300,var_2301,var_2302,], output)
mutated_mod['func_2303'] = func_2303
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2406 = relay.var("var_2406", dtype = "int16", shape = (7, 16, 2))#candidate|2406|(7, 16, 2)|var|int16
var_2407 = relay.var("var_2407", dtype = "int16", shape = (7, 16, 2))#candidate|2407|(7, 16, 2)|var|int16
bop_2408 = relay.greater_equal(var_2406.astype('bool'), relay.reshape(var_2407.astype('bool'), relay.shape_of(var_2406))) # shape=(7, 16, 2)
func_1302_call = mod.get_global_var('func_1302')
func_1306_call = mutated_mod.get_global_var('func_1306')
var_2415 = relay.var("var_2415", dtype = "int64", shape = ())#candidate|2415|()|var|int64
var_2416 = relay.var("var_2416", dtype = "int64", shape = (90, 1))#candidate|2416|(90, 1)|var|int64
call_2414 = func_1302_call(relay.reshape(var_2415.astype('int64'), []), relay.reshape(var_2416.astype('int64'), [1, 15, 6]), )
call_2417 = func_1302_call(relay.reshape(var_2415.astype('int64'), []), relay.reshape(var_2416.astype('int64'), [1, 15, 6]), )
output = relay.Tuple([bop_2408,call_2414,var_2415,var_2416,])
output2 = relay.Tuple([bop_2408,call_2417,var_2415,var_2416,])
func_2419 = relay.Function([var_2406,var_2407,var_2415,var_2416,], output)
mod['func_2419'] = func_2419
mod = relay.transform.InferType()(mod)
var_2420 = relay.var("var_2420", dtype = "int16", shape = (7, 16, 2))#candidate|2420|(7, 16, 2)|var|int16
var_2421 = relay.var("var_2421", dtype = "int16", shape = (7, 16, 2))#candidate|2421|(7, 16, 2)|var|int16
var_2422 = relay.var("var_2422", dtype = "int64", shape = ())#candidate|2422|()|var|int64
var_2423 = relay.var("var_2423", dtype = "int64", shape = (90, 1))#candidate|2423|(90, 1)|var|int64
output = func_2419(var_2420,var_2421,var_2422,var_2423,)
func_2424 = relay.Function([var_2420,var_2421,var_2422,var_2423,], output)
mutated_mod['func_2424'] = func_2424
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2503 = relay.var("var_2503", dtype = "float32", shape = ())#candidate|2503|()|var|float32
var_2504 = relay.var("var_2504", dtype = "float32", shape = (14, 7, 9))#candidate|2504|(14, 7, 9)|var|float32
bop_2505 = relay.floor_mod(var_2503.astype('float32'), var_2504.astype('float32')) # shape=(14, 7, 9)
output = relay.Tuple([bop_2505,])
output2 = relay.Tuple([bop_2505,])
func_2528 = relay.Function([var_2503,var_2504,], output)
mod['func_2528'] = func_2528
mod = relay.transform.InferType()(mod)
var_2529 = relay.var("var_2529", dtype = "float32", shape = ())#candidate|2529|()|var|float32
var_2530 = relay.var("var_2530", dtype = "float32", shape = (14, 7, 9))#candidate|2530|(14, 7, 9)|var|float32
output = func_2528(var_2529,var_2530,)
func_2531 = relay.Function([var_2529,var_2530,], output)
mutated_mod['func_2531'] = func_2531
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2538 = relay.const(5.518871, dtype = "float64")#candidate|2538|()|const|float64
var_2539 = relay.var("var_2539", dtype = "float64", shape = (11, 5, 7))#candidate|2539|(11, 5, 7)|var|float64
bop_2540 = relay.mod(const_2538.astype('float64'), var_2539.astype('float64')) # shape=(11, 5, 7)
func_2419_call = mod.get_global_var('func_2419')
func_2424_call = mutated_mod.get_global_var('func_2424')
var_2549 = relay.var("var_2549", dtype = "int16", shape = (224,))#candidate|2549|(224,)|var|int16
var_2550 = relay.var("var_2550", dtype = "int64", shape = (90,))#candidate|2550|(90,)|var|int64
call_2548 = relay.TupleGetItem(func_2419_call(relay.reshape(var_2549.astype('int16'), [7, 16, 2]), relay.reshape(var_2549.astype('int16'), [7, 16, 2]), relay.reshape(const_2538.astype('int64'), []), relay.reshape(var_2550.astype('int64'), [90, 1]), ), 1)
call_2551 = relay.TupleGetItem(func_2424_call(relay.reshape(var_2549.astype('int16'), [7, 16, 2]), relay.reshape(var_2549.astype('int16'), [7, 16, 2]), relay.reshape(const_2538.astype('int64'), []), relay.reshape(var_2550.astype('int64'), [90, 1]), ), 1)
output = relay.Tuple([bop_2540,call_2548,var_2549,var_2550,])
output2 = relay.Tuple([bop_2540,call_2551,var_2549,var_2550,])
func_2557 = relay.Function([var_2539,var_2549,var_2550,], output)
mod['func_2557'] = func_2557
mod = relay.transform.InferType()(mod)
var_2558 = relay.var("var_2558", dtype = "float64", shape = (11, 5, 7))#candidate|2558|(11, 5, 7)|var|float64
var_2559 = relay.var("var_2559", dtype = "int16", shape = (224,))#candidate|2559|(224,)|var|int16
var_2560 = relay.var("var_2560", dtype = "int64", shape = (90,))#candidate|2560|(90,)|var|int64
output = func_2557(var_2558,var_2559,var_2560,)
func_2561 = relay.Function([var_2558,var_2559,var_2560,], output)
mutated_mod['func_2561'] = func_2561
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2680 = relay.const([[[True,True,False,True,True,True,True,True],[True,False,False,True,True,False,False,True],[False,True,False,False,True,False,True,True],[False,False,False,False,True,True,False,False],[True,False,True,False,True,False,True,False],[True,True,True,False,False,True,True,False],[True,True,False,False,True,True,True,True],[True,False,True,True,True,True,True,False]],[[True,True,False,False,True,False,False,False],[True,True,True,True,True,False,True,False],[False,True,False,True,True,True,True,False],[True,False,True,True,False,True,True,True],[False,False,False,True,False,False,False,True],[False,True,True,True,True,False,True,True],[False,True,True,True,False,False,True,False],[False,True,True,False,False,False,False,False]],[[False,False,True,False,False,True,False,False],[False,True,True,False,True,False,True,True],[True,False,False,False,False,False,False,True],[True,True,True,True,True,True,True,False],[True,False,False,False,False,False,False,False],[True,False,False,True,False,False,False,False],[False,True,False,True,True,False,False,False],[True,True,True,False,True,False,False,False]],[[False,True,False,False,True,True,True,True],[True,True,False,True,True,False,True,False],[True,True,True,False,True,True,False,False],[False,True,True,True,True,True,False,False],[False,False,False,False,True,True,True,False],[True,True,False,False,True,True,False,True],[True,True,True,False,False,False,True,True],[True,False,False,True,True,False,True,False]],[[True,True,False,False,True,True,True,False],[False,True,False,True,False,True,False,True],[False,False,False,True,False,True,False,True],[True,False,False,False,True,True,False,False],[True,False,False,False,True,True,False,True],[False,False,True,True,True,True,False,False],[True,False,True,True,True,True,True,False],[True,True,True,False,True,True,False,False]],[[False,True,False,True,False,False,True,True],[False,False,False,False,True,False,False,True],[True,True,False,False,False,True,True,True],[True,False,False,False,True,False,False,True],[True,False,True,False,False,False,True,False],[False,True,False,True,True,False,False,False],[True,True,True,True,False,False,True,True],[False,True,True,True,True,True,True,True]],[[True,False,True,True,False,False,False,False],[True,False,True,False,True,False,True,False],[True,False,False,True,False,True,True,False],[False,False,True,True,False,False,False,True],[False,True,True,False,True,True,False,False],[True,False,True,False,False,False,True,True],[False,True,False,False,False,True,False,False],[False,True,True,False,False,False,True,False]],[[True,False,True,True,True,True,True,True],[True,False,True,True,False,False,False,False],[True,True,False,True,False,False,True,False],[False,True,False,False,True,False,False,False],[False,True,True,False,True,True,True,False],[True,False,False,False,True,False,False,False],[True,True,False,False,True,True,False,True],[False,True,True,True,True,False,False,True]],[[True,True,True,False,False,False,True,False],[True,True,False,False,True,False,False,True],[True,False,True,True,False,True,False,False],[False,False,False,True,False,False,True,True],[True,False,False,False,True,True,False,False],[False,False,False,True,False,False,False,False],[True,True,True,True,True,True,True,True],[True,True,True,True,True,False,True,True]]], dtype = "bool")#candidate|2680|(9, 8, 8)|const|bool
const_2681 = relay.const([[[True,True,True,False,True,True,False,True],[True,True,True,False,False,True,True,True],[False,False,False,False,True,False,True,True],[True,True,False,True,False,True,True,True],[False,True,True,True,False,True,False,False],[False,False,False,False,True,True,False,False],[True,False,False,False,False,True,True,True],[False,False,False,False,True,False,True,False]],[[True,False,True,True,True,False,True,False],[False,True,False,True,False,False,True,True],[True,True,False,True,True,True,True,True],[True,True,False,True,True,True,True,False],[False,False,False,True,False,True,True,False],[True,False,False,True,False,True,True,True],[True,True,True,False,False,False,True,False],[True,True,True,True,True,False,True,True]],[[False,True,False,True,True,False,True,False],[False,True,True,False,True,False,False,False],[True,True,False,False,True,True,False,False],[True,True,True,False,True,True,True,True],[False,True,False,True,True,False,True,True],[True,True,False,False,True,False,False,True],[True,False,True,False,False,True,False,True],[False,False,True,True,True,False,False,True]],[[True,True,True,True,True,False,False,False],[True,False,True,True,False,True,False,True],[False,True,True,False,False,False,True,False],[False,False,True,True,False,True,False,True],[False,True,False,True,False,True,False,True],[True,True,False,False,False,False,True,False],[True,True,False,True,True,True,True,True],[True,False,False,True,False,False,True,False]],[[False,True,False,False,False,False,True,False],[True,False,False,True,False,True,False,False],[False,False,True,True,False,True,False,True],[True,False,True,True,True,False,False,True],[True,False,True,False,False,False,False,True],[False,False,False,True,True,False,True,False],[True,False,True,True,True,False,False,True],[False,True,False,True,True,False,False,True]],[[False,True,True,False,False,True,True,False],[True,False,True,False,False,False,False,True],[True,False,False,False,False,True,True,False],[False,False,False,False,False,False,True,True],[False,False,True,False,True,True,False,False],[True,False,False,True,False,True,True,True],[True,True,False,True,False,True,True,True],[True,True,True,False,False,False,True,False]],[[False,False,False,True,True,False,True,False],[False,True,False,True,False,True,False,True],[False,False,False,True,False,False,False,True],[True,True,True,True,True,False,True,True],[True,True,False,False,False,True,True,False],[False,True,True,True,False,False,False,False],[False,True,True,False,True,True,False,False],[False,True,False,True,False,True,False,True]],[[True,False,True,True,True,False,True,False],[True,True,True,True,True,True,False,True],[False,True,False,True,True,False,False,True],[True,False,True,True,True,True,False,False],[False,False,True,True,False,True,True,False],[False,False,True,True,False,True,False,False],[True,False,False,False,False,False,True,False],[False,False,True,True,False,False,False,False]],[[False,True,True,False,False,True,False,False],[True,False,True,True,True,False,False,False],[False,False,False,True,False,False,True,False],[False,False,True,False,False,True,False,False],[True,False,True,True,True,True,False,False],[True,True,False,True,True,False,True,False],[False,False,True,False,False,False,False,False],[False,True,True,True,True,True,True,False]]], dtype = "bool")#candidate|2681|(9, 8, 8)|const|bool
bop_2682 = relay.logical_and(const_2680.astype('bool'), relay.reshape(const_2681.astype('bool'), relay.shape_of(const_2680))) # shape=(9, 8, 8)
func_754_call = mod.get_global_var('func_754')
func_758_call = mutated_mod.get_global_var('func_758')
const_2686 = relay.const([-7.673303,-7.631177,-6.518355,-6.143635,2.132133,3.365466,-0.961208,6.923341,5.969252,-2.989336,0.124192,-2.382141,-0.874217,9.313253,-5.606309,-6.721304,0.081473,9.139860,6.735352,-1.749808,-1.697276,-6.736704,-2.859994,3.190459,-2.287567,0.427163,-4.986745,-0.387173,-9.874098,-8.973427,4.793380,3.891073,3.263820,-4.695131,-4.303050,-4.291848,2.665286,5.762876,-5.626120,2.976307,-4.822340,-2.328643,3.236912,2.069319,-1.777122,-8.614923,-3.884532,-4.006944,-0.493797,-1.948250,-1.762629,9.519986,-5.092270,9.143849,-3.614746,5.330055,1.058456,6.291421,-0.744430,-1.039783,-9.023971,6.191145,-7.632955,-9.049655,-4.085052,1.441838,5.407823,-1.421397,6.215393,-9.686360,1.557594,-3.191635,9.566208,4.679794,-4.953685,-1.152907,-2.454473,6.665697,-1.706724,-7.629886,7.522378,1.070382,-0.068995,-3.036917,8.763883,5.903991,-6.081673,6.819614,4.001620,-9.419261,2.110095,-5.707221,-2.494400,-5.686809,-5.643261,1.956558,5.355312,-5.790085,3.589951,9.182474,-2.811938,8.191954,8.359558,-8.893813,0.359191,-1.919117,-6.439497,-7.647940,7.558816,5.589230,2.355444,7.276166,6.707937,8.004515,-7.743425,1.735187,3.812939,0.524655,1.753843,-7.553195,-8.556223,5.286820,0.874760,2.100310,4.274899,-9.610434,-3.705347,2.537629,-5.757409,-4.005567,5.786363,0.991860,-3.758956,9.823007,-6.087615,-6.317369,5.082849,9.563714,8.649141,7.784471,3.758682,-0.352094,6.689892,3.830703,-0.229697,-7.727446,3.300796,-8.423989,-1.739854,-5.573745,3.670998,-3.623880,-5.477872,-4.007604,-8.732224,-9.257421,3.040234,5.332928,-4.124982,-0.498500,-4.115430,4.875677,-6.400703,0.421862,7.530083,-4.615270,-0.950650,7.393937,-9.861781,7.689191,5.928208,9.292338,-7.112916,3.594623,8.172214,5.439088,-1.983565,-6.184788,-2.076627,-0.513878,7.344266,2.010090,5.399242,-8.908458,-8.269998,-3.035706,-9.553664,-1.617121,1.301941,3.483119,-3.319147,-9.201953,2.652028,4.121717,1.224302,-0.517817,-8.177211,-9.505743,-6.445082,-8.895700,-4.511616,2.326967,-4.308404,9.548296,3.625573,-7.677326,6.765528,6.311808,2.098632,1.870871,-4.493521,6.191297,8.666679,-3.725508,4.492293,-1.349443,5.649629,-2.180794,4.473585,0.453207], dtype = "float64")#candidate|2686|(220,)|const|float64
var_2687 = relay.var("var_2687", dtype = "float32", shape = (720,))#candidate|2687|(720,)|var|float32
call_2685 = relay.TupleGetItem(func_754_call(relay.reshape(const_2686.astype('float64'), [10, 11, 2]), relay.reshape(var_2687.astype('float32'), [180, 4]), ), 0)
call_2688 = relay.TupleGetItem(func_758_call(relay.reshape(const_2686.astype('float64'), [10, 11, 2]), relay.reshape(var_2687.astype('float32'), [180, 4]), ), 0)
func_2297_call = mod.get_global_var('func_2297')
func_2303_call = mutated_mod.get_global_var('func_2303')
const_2696 = relay.const([10,-8,-8,-3,5,1,-5,4,1,1,-9,10,-10,-10,-6,-4,10,3,4,10,-3,-9,-3,2,3,6,10,7,-5,-7,-6,9,2,-2,7,-4,-7,1,-7,4,4,-3,-7,4,-9,-7,1,1,-8,-8,8,-7,8,-5,-3,-7,10,-1,4,3,8,10,-3,-3,-3,8,-6,6,-7,10,-1,-4,9,-10,-5,-6,-10,-4,-7,-8,9,-4,2,-10,-1,6,-5,3,-10,-7,-5,-7,1,-9,-8,1,-2,-4,-4,-3,3,9,2,4,-6,-6,-5,-7,4,-5,5,-2,10,3,-10,-1,8,5,-3,-1,-1,9,9,2,-3,8,4,7,5,10,-8,8,-10,-5,1,1,4,10,7,9,-9,-2,-6,-9,-2,-6,-9,-6,9,-3,1,4,5,1,6,-5,-6,9,7,4,-6,-10,7,3,1,-6,-1,8,-6,1,-8,8,3,-9,-5,10,5,4,7,-8,7,-1,-6,-6,9,-4,-2,-4,-10,-7,-5,-4,-8,2,10,-6,-6,5,7,4,-7,-4,1,-5,-10,-5,3,5,2,9,-9,-8,3,5,-3,9,-9,10,-10,2,9,-6,9,-6,-1,10,1,3,1,7,10,5,-8,1,10,-9,-9,3,-8,-8,3,9,7,-1,3,-2,3,-2,2,10,-5,3,6,3,-3,5,8,-2,-9,3,3,4,-5,-9,-10,-1,10,10,-7,3,3,-8,3,7,-6,-1,10,-3,2,3,2,8,5,-9,-4,-6,10,9,5,3,-8,10,-10,2,6,-7,-9,-10,4,9,-10,6,-1,3,-10,-7,1,-6,-2,-6,-4,-5,-7,-9,4,10,3,6,-10,9,-5,10,-6,6,7,-6,-4,-3,-6,3,-10,-4,8,8,8,10,8,9,8,-1,9,7,-8,4,5,-4,10,-10,1,-6,7,-2,10,8,9,5,9,-1,2,-3,-1,-4,8,-9,1,-7,3,-5,3,3,7,1,-9,4,-8,-10,5,-1,-7,-1,-8,-9,8,-6,-1,6,-4,-3,9,-4,-8,7,-8,6,9,-4,-6,7,-10,8,9,-9,-10,8,2,8,8,-3,4,-2,1,-9,2,2,7,1,-3,-1,-5,-4,-10,-6,8,5,-3,4,-2,10,8,-5,-3,3,9,10,-4,10,7,-4,-7,8,5,-3,-4,2,4,-7,4,-4,-5,-4,9,4,-9,-2,5,-8,1,-9,2,-4,-7,-5,10,-3,-4,-5,2,-8,6,-9,9,3,-9,-4,2,-9,-9,-1,4,8,-4,10,10,8,9,9,5,7,-2,4,8,-4,-10,10,10,3,-8,-9,10,-6,-5,6,-7,-3,-5,-5,-4,2,6,9,7,-10,-2,5,6,-2,6,-2,-2,-2,-4,2,7,-4,-3,9,-5,-6,7,1,-3,-6,-3,-2,3,-4,2,-7,-7], dtype = "int16")#candidate|2696|(539,)|const|int16
const_2697 = relay.const([-4.811780,1.161543,4.620408,8.934563,-2.361580,4.717689,4.157439,-0.525688,0.628250,1.387440,-3.825197,-3.486950,7.379378,-5.230871,-2.575754,-7.059907,5.890196,-1.973386,-8.600357,2.467556,8.314788,-3.860479,-7.597611,5.213249,-9.275641,3.717751,8.632668,7.473269,-3.412057,5.718310,3.815818,8.098320,4.403921,-0.631467,5.772370,-6.757416,-6.011097,-3.834260,-6.215714,-3.544767,-3.401274,5.942788,8.011328,-1.119309,-5.679640,2.283635,2.277924,-0.333883,-0.653607,9.398585,-3.293102,-2.422690,-9.741775,0.849963,-3.205358,7.890403,-6.583942,-2.784572,5.064063,9.533761,-2.114716,4.914381,-1.822601,-9.429671,-5.239668,-8.732576,8.737824,4.863916,3.151363,-9.568066,-0.375721,2.862853,8.156281,5.531396,-2.562685,-1.224693,5.055654,1.275149,-0.344346,-2.092472,4.504574,4.677013,8.570904,-2.681716,-8.792615,-5.708474,-5.266362,1.289436,1.451016,-1.772174,6.923692,-9.141307,-3.825105,-7.879851,6.312365,-8.027983,-7.965520,6.136677,-2.200498,-6.520884,0.527325,-0.799147,-5.743044,2.088613,-1.350001,-2.995241,-7.980417,-6.536749,-3.649836,9.593725,9.199913,-7.752300,-1.445184,9.662823,9.499694,6.401604,-1.825865,-0.234401,7.251340,-6.576262,1.653376,8.260988,7.451315,-5.026527,6.244129,7.570088,8.096209,-0.156205,7.032931,0.927538,2.761222,3.270578,-9.788547,8.677719,4.968841,2.312675,-2.972439,7.276407,-4.682846,0.586452,6.918341,-7.206086,-3.078822,-9.982711,-8.903340,-6.251986,-7.188683,0.693227,3.378199,-6.215659,-1.004866,4.727742,6.717252,-2.509519,-3.918132,7.652259,-5.451747,1.601797,-2.248582,-8.799049,4.655000,-0.147075,0.204824,-8.136534,-3.004010,1.712302,-0.985148,2.515820,9.725985,1.803234,9.347486,-8.763052,-0.408224,-8.584176,5.237302,8.527416,0.437838,5.269933,8.165138,9.690625,-6.997587,-0.993276,6.745190,-1.615945,5.670260,1.346217,-7.672111,-4.156478,7.736176,5.048929,7.692007,4.353064,3.585190,6.156779,-9.218696,-7.301973,-4.268750,6.254383,5.602359,-7.391436,6.580076,9.777189,5.496139,-4.032901,9.677785,-0.668326,-0.400783,9.170825,-6.540224,-1.096374,-3.622294,7.088689,7.872093,-5.701681,6.236950,9.963775,-5.689904,-0.860480,-7.724407,-6.794468,6.383323,-6.029879,-6.222070,5.590278,5.365493,4.201764,-5.293052,-5.531750,7.686575,-8.974915,0.054819,2.457145,1.213941,-7.588461,-2.917351,7.518233,3.553816,9.541984,7.203605,-3.783324,-7.638325,-0.934505,-5.170864], dtype = "float32")#candidate|2697|(243,)|const|float32
var_2698 = relay.var("var_2698", dtype = "int64", shape = (462, 1))#candidate|2698|(462, 1)|var|int64
call_2695 = relay.TupleGetItem(func_2297_call(relay.reshape(const_2696.astype('int16'), [7, 11, 7]), relay.reshape(const_2696.astype('int16'), [7, 11, 7]), relay.reshape(const_2697.astype('float32'), [243,]), relay.reshape(var_2687.astype('float32'), [720,]), relay.reshape(var_2698.astype('int64'), [462,]), ), 3)
call_2699 = relay.TupleGetItem(func_2303_call(relay.reshape(const_2696.astype('int16'), [7, 11, 7]), relay.reshape(const_2696.astype('int16'), [7, 11, 7]), relay.reshape(const_2697.astype('float32'), [243,]), relay.reshape(var_2687.astype('float32'), [720,]), relay.reshape(var_2698.astype('int64'), [462,]), ), 3)
output = relay.Tuple([bop_2682,call_2685,const_2686,var_2687,call_2695,const_2696,const_2697,var_2698,])
output2 = relay.Tuple([bop_2682,call_2688,const_2686,var_2687,call_2699,const_2696,const_2697,var_2698,])
func_2702 = relay.Function([var_2687,var_2698,], output)
mod['func_2702'] = func_2702
mod = relay.transform.InferType()(mod)
mutated_mod['func_2702'] = func_2702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2702_call = mutated_mod.get_global_var('func_2702')
var_2704 = relay.var("var_2704", dtype = "float32", shape = (720,))#candidate|2704|(720,)|var|float32
var_2705 = relay.var("var_2705", dtype = "int64", shape = (462, 1))#candidate|2705|(462, 1)|var|int64
call_2703 = func_2702_call(var_2704,var_2705,)
output = call_2703
func_2706 = relay.Function([var_2704,var_2705,], output)
mutated_mod['func_2706'] = func_2706
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3282 = relay.const([[[-7,2,-9,-9,-9,-4,-6],[3,-10,3,7,4,-5,9],[1,9,10,-2,-10,1,7],[-4,-10,-2,-3,-4,8,-10],[-10,-7,6,1,-5,5,5],[-7,-5,3,5,8,2,-10]],[[-10,3,9,5,6,-1,10],[-8,-6,-5,-5,6,6,10],[6,10,2,9,5,-9,9],[-2,10,2,-7,4,-7,-2],[4,3,-5,7,-6,3,8],[2,3,-6,6,-8,-7,4]],[[5,-9,9,-9,4,-4,-2],[-4,8,-10,2,6,6,-2],[10,-6,-6,-4,-6,-1,-10],[-3,-1,-5,-4,10,10,7],[-3,8,-7,-8,9,7,-4],[-8,-3,-5,9,-3,-4,1]]], dtype = "int32")#candidate|3282|(3, 6, 7)|const|int32
var_3283 = relay.var("var_3283", dtype = "int32", shape = (3, 6, 7))#candidate|3283|(3, 6, 7)|var|int32
bop_3284 = relay.right_shift(const_3282.astype('int32'), relay.reshape(var_3283.astype('int32'), relay.shape_of(const_3282))) # shape=(3, 6, 7)
func_1302_call = mod.get_global_var('func_1302')
func_1306_call = mutated_mod.get_global_var('func_1306')
const_3294 = relay.const(10, dtype = "int64")#candidate|3294|()|const|int64
var_3295 = relay.var("var_3295", dtype = "int64", shape = (90,))#candidate|3295|(90,)|var|int64
call_3293 = func_1302_call(relay.reshape(const_3294.astype('int64'), []), relay.reshape(var_3295.astype('int64'), [1, 15, 6]), )
call_3296 = func_1302_call(relay.reshape(const_3294.astype('int64'), []), relay.reshape(var_3295.astype('int64'), [1, 15, 6]), )
func_2419_call = mod.get_global_var('func_2419')
func_2424_call = mutated_mod.get_global_var('func_2424')
var_3299 = relay.var("var_3299", dtype = "int16", shape = (16, 14))#candidate|3299|(16, 14)|var|int16
call_3298 = relay.TupleGetItem(func_2419_call(relay.reshape(var_3299.astype('int16'), [7, 16, 2]), relay.reshape(var_3299.astype('int16'), [7, 16, 2]), relay.reshape(const_3294.astype('int64'), []), relay.reshape(call_3293.astype('int64'), [90, 1]), ), 3)
call_3300 = relay.TupleGetItem(func_2424_call(relay.reshape(var_3299.astype('int16'), [7, 16, 2]), relay.reshape(var_3299.astype('int16'), [7, 16, 2]), relay.reshape(const_3294.astype('int64'), []), relay.reshape(call_3293.astype('int64'), [90, 1]), ), 3)
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
const_3304 = relay.const([-7.108151,3.351805,-9.087043,5.661728,-3.489511,-0.891320,3.020140,-4.854953,-9.248755,-3.715199,3.586291,2.555683,5.016834,-4.208063,6.011696,-0.207089,-0.257572,-9.522610,-7.927752,4.900771,-1.329634,-2.126985,0.311118,-6.814520,-4.954416,1.622422,9.725498,0.936431,-6.154225,0.132967,-8.707646,-7.657202,0.644425,4.740838,-4.122470,4.172221,-1.509302,-3.331432,-5.796482,6.938309,1.170623,-6.924957,1.365254,4.356485,5.195947,-2.352098,-7.333075,-0.510548,6.343131,4.924358,7.318495,4.847482,-9.294528,0.647496,-4.227652,5.472120,2.271295,-0.081136,-7.159101,-6.519329,6.121680,5.063541,3.648854,7.798892,-6.126451,1.341788,4.722635,1.150099,-0.962066,-4.558966,-0.572375,5.495329,8.560841,-5.694440,2.337492,6.359189,6.126981,6.868261,7.325135,-3.700249,2.231490,5.323107,-3.395833,4.694944,5.978598,4.638400,4.798897,0.867861,1.279395,-0.530435,-0.539407,7.022109,1.320237,6.283334,5.437726,-8.693865,0.292218,-9.789296,-4.022577,-9.678601,0.173761,8.847697,-2.078763,-6.112282,4.872850,1.991341,-5.496115,4.726782,9.781861,-4.289127,-6.794506,3.340313,-4.567879,7.338637,8.496920,-6.573284,-3.315932,-6.258569,-5.706722,-7.545538,0.324602,-4.582326,-7.084279,2.210659,-2.098187,-0.422039,-7.787303,-5.767714,5.976829,-4.931088,1.171535,-2.523473,-6.635302,4.546296,5.699966,-2.495702,1.749813,-7.953286,3.855450,5.336359,-8.760354,-5.931635,8.679287,4.631807,0.684023,-2.921035,7.319496,-9.692835,3.914359,-8.930247,0.860679,3.165641,7.564896,-7.946782,-7.349768,-0.129545,1.856708,8.541714,5.782556,-0.645355,-9.305580,-7.722595,1.550819,-3.155664,-5.228535,5.966118,3.038593,-1.237997,-4.712522,9.653630,-2.208103,5.500661,5.613373,-2.240190,-2.518738,1.484453,0.150356,-8.072802,-1.272321,7.939577,1.878501,-1.367383,-0.257696,-6.608090,1.716253,4.742668,6.510508,0.095896,3.746420,-5.933020,-5.412768,8.341161,9.552736,-6.962841,-7.482094,-3.622272,-7.980859,-7.153192,3.091736,-0.708144,1.561368,-3.767862,-9.972609,9.342631,3.645608,8.852811,3.918864,-0.802044,-2.437249,-9.308180,-4.818876,2.031989,8.909117,7.223847,-6.651043,8.237556,4.465671,-6.163519,1.366069,-1.366711,1.567600,7.622745,-5.371222,0.832365,-7.758133,0.217932,-1.873939,-5.953271,-1.760843,-9.293136,0.695713,-3.579753,2.613997,-9.599489,-8.146989,-0.875968,6.383707,-6.998187,3.158930,-9.832851,2.505067,-9.185303,-8.977554,8.756433,6.863517,9.122915,8.563459,0.055776,6.735983,-0.697263,-9.706032,1.391102,-6.468553,4.945866,-6.602012,7.641707,3.462433,9.002524,-9.737128,4.209011,0.417550,-0.163198,-2.107988,6.518217,-7.262427,-4.046426,-2.095917,-0.434572,5.744336,-1.882685,4.012032,-4.116393,-9.802917,4.534829,-6.126715,-7.325545,5.606744,6.330755,-3.425649,1.318817,-0.174601,-5.526685,-8.375406,3.902231,-7.884894,7.776819,6.765749,4.374419,4.132387,6.798671,7.899436,3.411535,-0.365565,-6.714695,-5.472731,1.315061,5.843390,6.338883,-6.965806,-4.466730,5.167674,9.255507,2.828583,-8.750321,5.057997,-7.848968,1.064520,7.397470,-0.686895,-3.566413,-2.796655,6.816670,9.209975,4.125325,1.145751,1.647548,6.616427,-6.631194,5.206433,9.432100,-2.626599,5.579681,-0.043948,4.295494,-1.206323,2.559606,-2.825591,8.127615,1.086665,9.522958,-5.416988,1.751918,6.336415,-7.173366,-1.407315,2.519559,3.919952,-9.146642,-0.106068,4.254616,-1.336991,8.609087,2.323882,-5.613571,4.484329,-6.647175,-2.275840,1.669921,7.548098,-5.760238,2.964523,-4.482269,-4.543992,-5.779891,-5.325616,-1.636808,-1.346553,8.520533,-7.651165,7.697777,-0.755196,4.513992,7.102989,-3.691204,-5.726499,5.616691,0.144911,-6.235552,-9.785564,-3.615188,-5.507191,0.157456,-8.378276,5.201148,9.467099,-6.799911,-1.361094,-3.562482,-3.129169,-0.468327,-0.351958,-8.847949,1.800671,6.318201,-1.784579,-2.658962,-2.339641,8.928564,9.734652,3.253249,2.181598,-9.071898,6.265740,-2.076303,0.302624,-6.083008,-3.982362,6.436011,-5.653786,0.303933,-1.676656,3.901723,-9.136414,5.017544,9.104653,-9.948239,-9.723127,-4.421221,7.801370,7.011413,4.425491,-6.041922,6.778712,1.799388,2.077084,-6.906249,2.643895,-2.756083,-0.583802,5.737593,6.561541,7.326522,-0.942046,4.366890,-2.000398,-9.222146,1.658953,3.823863,4.664666,-2.231291,6.573000,-9.413992,-8.866535,-4.773076,7.160506,3.846598,6.928360,-9.643394,-1.869217,-2.410468,3.786469,9.197784,3.366630,0.835881,8.498427,4.522429,-4.596428,9.120251,7.523253,3.652955,3.443736,8.442658,8.121041,-6.706446,1.558515,-7.661542,-5.863674,3.314715,-3.228764,-3.918902,-7.032972,5.927780,7.660398,-0.223465,-2.395560,0.955075,-7.055682,8.018528,9.727132,2.471834,-0.646138,4.798057,1.331952,-0.308009,3.702399,-8.270137,1.247755,-5.849784,-0.365170,6.861893,-2.735756,6.740464,7.863942,6.108392,-4.793608,1.213549,-6.787757,5.899910,-8.067851,-9.945803,-4.199387,8.576308,-4.582433,4.827613,-8.566969,6.355118,5.323470,3.698470,7.707498,6.113686,-1.033425,-2.963961,9.322693,-9.133501,-5.085205,3.738628,1.658917,-0.376189,-4.896847,5.337246,-1.861831,-2.108220,4.317166,-9.575062,-1.055307,-6.512335,-3.318493,3.749140,4.199456,8.195325,-7.692870,-1.845713,-0.729787,2.849761,-5.937670,7.043750,-8.127431,6.216092,-8.698833,-3.151402,1.836080,4.695157,-0.902790,-8.802415,-3.681358,8.193355,-4.848580,7.754693,-1.478228,-2.385577,0.447290,7.672283,8.566969,1.813660,-2.346983,-2.606759,-6.168855,4.381335,-1.924839,-2.365603,-5.316172,-9.426226,-6.795693,4.295964,-8.169273,2.082268,9.127722,9.353860,6.115394,-9.592275,2.840342,-1.581465,-3.466033,-4.945150,3.119703,-7.540223,-2.363511,-5.032848,-6.643875,7.985996,2.843889,-6.937538,1.886198,6.398587,-5.796454,-8.155714,-9.712238,8.591949,-4.794040,-1.840368,4.683310,3.646500,2.571799,-9.524562,1.187918,-2.780787,-8.022633,-6.778513,0.022867,8.013651,5.809076,2.789019,-7.217230,1.482661,-9.302122,-8.614134,-5.418850,6.615683,5.772244,8.841459,0.349735,-2.267222,-4.684156,7.512121,-5.317673,9.947478,-3.128521,-5.709148,9.766275,3.715069,0.469171,7.229520,-7.675619,3.236180,-5.200937,-1.207051,-7.631475,-4.396184,6.430400,-5.914248,-8.635049,-9.326968,-7.068861,7.600727,-2.997990,6.829850,-4.385064,8.696037,8.156236,-9.560792,9.198813,9.334434,3.758607,-9.098613,9.008377,2.896048,-9.562538,-2.795455,-7.519231,-9.137378,3.373181,-3.763091,8.860245,-3.525437,-7.501240,-3.297882,7.273320,7.159011,3.889333,-4.073163,9.691055,-8.073341,8.564686,-9.923770,-9.384490,-8.404086,6.663262,6.856175,-1.543708,6.449587,7.959595,-6.077489,-9.667507,3.863344,8.097505,-9.526023,9.640885,-9.024032,-8.054746,-1.452897,0.789936,-0.247170,1.128490,8.384844,1.819609,-1.115702,5.095895,9.249404,8.188933,9.702354,-2.416186,3.042049,9.182180,-3.221887,-3.207014,-7.748444,9.308984,-4.344108,8.535204,-9.691194,6.671086,2.899339,2.590307,-7.316485,2.902726,3.050641,2.549423,-4.543128,-2.930692,-8.792088,1.563455,3.945294,7.069550,-9.249275,2.848465,5.175997,9.984490,7.665611,-3.205670,4.003068,-1.388977,9.570835,5.360597,-3.762132,0.931831,0.047674,2.105248,0.394805,-1.520557,9.521538,2.811734,-9.353529,9.651554,2.411272,2.536913,-7.707379,-7.968929,-8.674788,2.934174,3.379888,8.677434,2.992283,4.071941,-7.061280,-8.090332,-5.415343,-8.542360,7.472518,-5.238514,2.832289,8.466837,3.475138,-0.761331,-0.211089,-3.598363,-4.170739,-4.710434,1.299016,-9.589966,6.657870,4.117259,-9.036270,1.894077,-5.156817,8.719558,5.501517,5.880500,-0.619699,-3.508396,9.960082,-8.106510,0.339746,3.046999,9.159170,-5.224082,9.981911,-5.175589,4.241018,3.448062,1.611067,-5.931345,8.594159,-1.327380,6.169189,-0.515150,9.719110,-7.177562,7.563445,5.047964,6.188815,-3.826659,-5.734652,8.218430,-7.066807,0.087175,9.934413,-2.365774,0.275400,-6.071698,-0.227358,3.865528,9.751910,-4.332577,7.777869,5.811324,3.220023,6.334332,-3.271650,2.145948,5.215124,7.725582,-3.689324,-8.051483,-4.401710,-7.185781,3.619742,-8.160102,9.170438,-5.640496,7.137574,-3.492892,4.202708,-3.397282,-9.930857,-5.645607,-1.494446,-4.736076,7.418013,-9.573589,1.416489,-7.730964,-2.116754,9.477247,8.567746,-5.042996,-5.239621,4.608593,7.323654,6.879017,-8.460139,9.924618,6.846354,4.126165,-6.189876,-8.033819,5.422537,4.739954,-7.003761,4.054755,-4.520619,-5.655506,-6.719425,-5.373959,2.503853,0.297161,0.180111,-5.915758,-1.820990,8.421775,7.085074,-0.941340,9.066670,-0.616921,4.025907,7.158015,1.853854,-0.034751,-0.111747,0.339896,-4.065940,1.043846,-3.363978,7.172943,1.152998,9.165325,-1.353083,2.968591,8.194218,7.554189,-3.060318,-3.496848,-4.949540,7.891612,1.464167,-5.476931,-2.105205,3.017331,6.422631,7.158756,-8.163142,2.058604,9.193827,-2.833152,-7.806969,5.804293,-5.397710,8.888653,-1.751946,9.060166,4.158491,0.891812,9.334922,-6.155323,4.631818,-0.610045,5.389474,5.098250,-4.917115,2.206685,7.415384,6.485888,9.774080,4.870014,-0.660363,2.502746,-9.211413,0.776003,-5.993088,3.711543,5.162193,7.911134,4.344715,4.968587,-7.024213,3.880191,4.144632,0.934627,9.564387,-4.756563,-2.244061,4.098991,4.238216,-0.192750,2.741226,5.290156,7.396926,8.136354,6.434252,6.856855,7.758709,-1.826980,3.898602,5.431118,-6.927613,-2.511877,-3.469308,3.541537,-0.584640,6.551062,9.343493,5.493272,6.394699,-9.999176,5.741100,-2.783181,-3.103481,-7.640795,-4.947390,-8.361191,0.782112,6.407361,-4.260564,0.054908,0.298398,-3.897163,-8.778859,1.187733,-5.280236,-6.430534,0.249769,6.407392,2.429357,-1.065373,9.510225,-2.911914,6.828177,-3.339254,5.766260,5.516469,-3.189060,3.998594,9.319195,-1.786989,-2.577833,8.951002,7.819399,1.500957,-7.562609,0.666390,-4.626774,6.885781,2.712267,-7.629649,3.377179,1.106805,0.586004,-1.186753,-3.999963,7.639282,-9.793702,-8.373827,8.550858,-9.385762,2.000616,4.738629,-4.789636,-2.412691,3.115066,-2.040874,-3.466701,-2.889279,-8.762025,-9.622561,-7.184148,-6.209838,-3.126391,-3.754171,-0.243425,-6.701658,-2.340131,-0.793864,-9.940581,3.378146,1.692204,-0.407805,7.848627,0.204945,-2.267157,-3.153996,1.938197,1.418214,-6.451621,4.897221,-0.241455,-6.708081,-0.622566,8.653548,5.172542,-9.351024,-5.146461,-1.333942,7.401429,-9.288441,6.398029,-5.905204,8.160201,0.939361,-7.596132,-0.114422,-4.312754,0.201731,7.917346,9.628831,9.711367,8.157633,-0.756186,-1.704982,-0.889903,7.507035,8.681632,-9.984896,8.073668,-1.208720,3.026583,0.854691,-1.715299,-9.762021,0.982479,-5.815375,9.065620,1.413604,-5.521122,7.544705,-0.889197,-1.505092,8.830323,-4.330564,-5.103228,-9.983530,2.404969,4.017767,-8.252073,-8.140317,8.342313,0.151559,-3.554608,5.438100,-0.962863,2.494065,6.698743,-8.155256,6.880665,-2.465908,-8.869551,1.415684,-2.291041,8.430794,-5.411043,-8.965997,-3.611424,-3.853940,-1.112933,4.151318,-5.194127,4.009120,1.678710,-5.295480,-5.991834,-6.436829,3.700947,3.755952,4.779515,9.513072,-2.722024,5.069416,7.306544,2.855619,8.504554,-1.692978,-4.438421,-8.762014,9.545011,-8.343905,8.781684,-5.565012,-5.290907,-9.920117,-2.030053,8.330236,9.758660,-6.293122,-3.310822,2.803581,-9.874214,9.010059,5.718773,-9.759917,6.564290,7.072442,-2.732960,1.390487,0.361769,-3.453184,7.789452,-7.452520,-0.625479,8.221521,-1.382400,6.579813,-8.887798,9.238329,-7.116919,3.612759,-6.018150,-4.791947,-4.185919,3.020810,6.752976,-5.092890,5.754517,5.943017,3.059173,-7.098834,8.386566,-9.118070,9.105138,-8.830960,-6.085440,3.666460,-3.844671,2.729228,7.703415,-4.568580,-4.859185,-9.587372,1.719481,1.189036,-0.470138,-2.666874,7.680664,-9.872435,3.167438,-7.095339,-9.293703,-9.316056,9.998409,9.745205,3.700766,4.566779,-9.620466,8.796613,-2.770903,-7.835654,3.445518,-9.920282,-9.566448,3.030444,9.430168,5.056904,7.015790,-7.810014,7.231205,5.942032,5.239892,-4.940243,-3.305405,7.267495,-8.658403,-1.670654,0.631631,8.648768,2.706733,3.404335,-6.792613,-7.664544,-5.865020,1.552671,-2.922481,-0.632657,3.570418,-1.478678,2.181014,-9.196039,0.824381,9.003103,-4.436338,-0.961977,4.822530,-5.544648,-6.961526,7.649957,-2.671450,-6.595383,4.826576,-2.602932,9.809932,4.070206,7.487866,5.927613,-0.984698,1.088868,2.331172,-6.347154,9.335892,-4.529495,5.433613,-7.643519,-5.400857,-2.265753,-3.428052,6.838891,1.172601,-7.100744,-3.685384,-8.075221,-8.202838,4.000193,8.914016,-4.942194,9.331870,2.982366,-7.869478,-2.982121,-8.636773,-8.550284,4.844972,0.946464,-7.493624,0.890261,5.570857,1.774356,7.552697,1.998938,-2.964421,7.484829,-5.601408,-7.493884,1.262065,-5.966447,-8.539218,-2.796346,-2.837641,-0.075683,7.042416,4.845060,8.800511,-1.005877,-1.772472,-8.088076,4.032403,-0.858760,-9.465914,-6.232166,0.112979,4.489328,1.407560,9.467190,9.886869,7.091219,-3.521944,9.525347,2.315795,-7.889275,9.247379,2.605950,4.336714,8.497983,-9.025674,6.965813,-4.340306,6.823610,-6.533973,0.631208,1.073921,-5.921075,2.059993,0.927788,6.899766,-5.600657,-1.815846,7.144813,8.213392,7.081867,-7.080689,5.484864,-3.122715,-4.465980,-3.962293,-0.114705,-8.240196,2.615311,6.635756,1.228289,-2.091976,2.094978,1.777910,-0.362751,6.014666,-1.381706,-1.041953,-0.042453,1.822399,4.121224,-2.559370,5.874665,-5.430727,3.789994,7.117753,-6.156382,-3.029268,1.762389,-0.751839,6.669680,4.628000,4.356241,1.018129,-4.553158,8.462112,-2.433936,-2.052981,-0.694178,-0.881129,-1.848049,-9.887228,-3.456300,-1.080208,-3.267587,9.456815,8.019723,-4.005268,1.516716,-6.070689,-0.493787,0.935456,-5.691892,-8.283670,3.002216,-5.051290,-6.268341,-2.112051,7.894051,-3.354974,-7.967226,9.755977,7.428591,-4.023739,-4.475630,-5.217906,-8.847765,4.956825,3.648493,-0.168676,4.853211,-7.387744,2.298979,-9.163048,-7.483805,6.946328,-8.374814,-3.898855,-2.225527,-8.248453,6.888372,5.076998,3.672163,-6.054852,-9.055045,0.416758,1.851354,7.169397,-4.995131,-2.759416,5.717988,3.430944,-4.666152,7.244385,9.411941,9.718931,-7.224599,-6.139990,-8.651763,0.902912,0.767230,-8.680493,-6.774403,-2.467441,8.193021,1.910179,-9.851614,-9.453317,-6.934365,0.270514,-5.258165,5.639113,6.535845,-2.358929,-5.509443,-6.138517,-3.514265,0.551076,-8.986999,7.929246,-5.961271,-9.662576,-6.567857,7.345043,-6.673410,-9.864918,-1.020007,-0.059496,4.795950,6.968729,-5.352909,-4.379041,-1.483279,7.326541,4.074718,-9.105933,-8.486737,-5.361060,3.239980,1.459659,-1.233340,-9.240564,0.364612,-0.347339,4.902198,3.624981,3.434398,-2.593163,9.453485,-8.307412,1.165815,-9.591234,-6.199137,-5.408036,-2.628614,9.433150,1.493796,1.442711,-0.802648,2.210641,5.348903,8.283155,-1.212964,-4.929865,-4.030128,-6.913192,6.655301,4.180442,2.418580,-3.306926,3.245960,-6.516837,8.217111,-5.265053,5.978633,-0.109177,-4.242966,6.718278,4.409186,-2.448449,5.762533,0.326120,3.151077,-9.719794,-3.430123,-7.462210,-2.908256,-1.777306,7.700529,-0.943451,8.002769,4.308552,-2.758998,-8.346894,9.203197,0.551925,-8.346851,7.885992,1.279630,-6.753502,-7.806845,-3.404071,-6.541351,9.399769,7.912855,-4.536946,-7.251978,-5.353721,6.336261,-9.608203,0.897089,7.077290,6.216884,0.258247,-0.126269,-0.812841,-7.908153,2.771687,-3.737703,-7.561315,-3.698043,-7.179864,2.648041,-5.661451,1.545354,2.284879,-6.199311,-7.242999,8.701918,7.712301,-0.167144,8.426108,-5.117914,9.638025,1.911926,-7.085032,-4.260454,-9.771786,0.801533,-2.484782,0.500620,6.391432,-2.619474,0.144487,7.578643,5.004462,9.848938,-9.294501,-5.473857,-8.972335,-5.541933,5.981601,4.764504,-1.371765,-9.933417,9.375495,-5.629329,-0.147483,6.489082,-1.555580,-2.216289,-8.996030,-1.678729,3.555851,-6.659763,-4.143707,-9.935132,8.744459,9.964098,-1.041386,0.695416,-1.728537,-0.678304,-1.272655,-4.550928,-8.994822,5.365732,-7.254402,6.602262,-6.305795,1.738956,-7.383448,-9.569211,3.550730,8.245046,-1.432060,-2.318741,-4.588888,6.580974,-4.614162,-4.135858,-4.645522,5.382565,1.498304,-6.604426,-4.664224,3.069546,2.553354,-0.943866,6.409946,-8.006708,-0.695003,-8.052683,7.457189,-6.549998,-8.383098,-0.100203,-6.565934,5.824069,-1.526258,5.491306,-6.357681,-0.938763,-2.113592,-2.546581,-8.180959,4.844830,4.681942,-6.647525,2.354001,-7.973523,2.003598,-0.732177,-8.880187,2.521265,4.799090,9.538213,3.259161,9.554663,4.083671,-6.836077,-8.814917,-4.123968,9.569966,-2.769084,2.059654,-2.068389,3.619791,-2.920447,7.776306,3.965894,-7.337118,-3.785684,-1.508327,-3.058458,2.242492,9.048773,-7.700386,-7.578671,-7.862474,0.261394,7.517657,-6.079406,-7.710173,0.966011,8.119605,0.628667,2.716094,0.530582,5.650003,6.239314,-9.082791,4.959856,8.133244,3.363268,-5.686975,8.655211,-1.830153,0.687348,6.361877,-7.096573,9.375762,-5.861438,1.221768,-8.355067,1.240938,-2.199121,-5.617541,1.387541,7.617220,-8.574093,4.003682,6.938347,2.418140,-4.281270,1.263511,8.920913,-8.797825,-6.102001,-1.299559,2.070876,-1.592509,2.054461,5.372026,-6.192112,1.309644,-8.059250,3.358005,0.222868,-5.949277,9.651372,-7.767809,-0.692317,-6.166973,2.928422,3.969308,3.694053,-5.419537,6.104699,9.583789,-8.172295,-8.843821,0.337693,-6.190238,-1.446098,-3.810642,1.054464,3.774219,-8.643612,-2.676156,-5.233008,-0.258499,5.105197,-1.239145,-1.078795,9.081059,7.410831,4.232219,3.831639,0.101903,3.023702,2.211049,-8.717336,-4.425472,-7.334735,-2.850911,3.259128,-7.456838,1.733668,3.608016,-0.352145,-6.245767,-8.771339,-2.860313,-7.584624,2.072967,-1.028299,-1.909940,6.782992,7.685986,6.427287,-6.833164,-6.086035,8.214061,-6.172584,2.657310,9.432235,-8.999947,5.498957,8.172859,-0.572325,5.443170,4.394795,1.089792,3.120367,7.933853,1.076117,5.610588,-4.265851,3.515432,1.228807,-4.277216,0.187082,-4.740617,9.270656,-6.454175,-4.298091,-9.724623,0.535251,2.077392,-2.377232,1.659990,-6.412183,0.691463,1.415397,1.153692,0.615922,-4.751971,-8.482879,-7.008991,-1.634151,2.341098,-9.631225,0.943147,-3.891213,-9.221600,9.629686,-8.078089,-7.429433,-4.666217,-5.520325,-9.086289,5.477684,-3.842361,3.467709,-3.031894,8.161604,7.309006,9.604518,0.644181,7.155472,4.288567,9.909305,-9.124202,4.985757,-7.610491,0.189424,-6.564892,9.556276,-7.506539,1.976091,-9.526498,4.955734,-7.958617,-3.427640,-6.532581,-3.275898,-6.491686,5.713068,8.530740,-1.585968,-0.406936,6.016610,-4.113790,-7.396230,4.482058,5.713865,-8.084697,0.616189,-9.987700,7.143559,4.259599,-9.826009,1.734605,9.767127,-6.668221,-9.325753,0.865224,8.498790,-4.364275,-5.645920,7.108631,-7.062229,-8.782888,5.001179,1.103891,9.478861,-4.599292,4.106795,5.979190,-6.038140,-8.045124,1.151635,-6.270540,3.475082,-3.775323,2.154033,-4.048398,3.392550,1.142397,7.896007,7.517369,-1.366433,-3.295140,-0.304744,-0.818995,0.035548,3.206282,-3.056421,-0.446006,1.572487,6.523115,-5.870236,-1.759409,8.350900,-2.611665,-8.366497,2.058281,5.668266,-3.562707,-1.391299,4.699620,8.854219,-1.724947,-3.222467,-9.992164,7.677229,-4.414175,4.571682,8.835219,3.773810,8.782914,-8.648297,-9.704230,-8.334804,8.220281,3.008980,-6.807606,5.257744,-0.977594,7.061403,7.221311,-2.641227,4.004698,-5.852632,-1.042573,-5.837512,-4.229868,5.591563,2.484696,1.966985,-2.313811,0.434184,-5.907085,7.260085,-2.206988,8.121689,2.425799,-2.231280,0.951165,6.210136,-6.563458,3.767187,-6.348628,4.725492,-4.886756,-9.170909,0.352828,5.333738,3.530893,-3.269868,-7.769097,1.332134,7.083778,-4.894025,6.697995,0.849324,1.175554,-0.766812,7.101146,0.656295,-4.231816,-2.058050,7.088431,3.762873,-7.390784,4.248028,5.622390,-0.248624,-6.958682,4.528317,-5.256169,8.190208,5.485472,-2.623977,3.006440,-4.768910,7.646255,2.630073,1.491646,5.031668,-5.725571,-4.018735,-1.393835,-8.819874,7.922204,-6.639582,-3.528485,4.883631,0.276503,-6.855418,-8.546119,-4.671178,7.977684,-9.064799,3.981355,-0.197756,-9.878241,8.134456,8.165710,7.754560,-4.383918,8.771309,7.529464,-3.531815,-7.171388,4.420859,-4.221811,-4.787915,2.087136,-0.635685,5.244595,-4.102933,3.849263,-1.022809,-8.324732,2.966278,9.797961,7.184480,7.225476,0.971682,8.532002,-0.349652,-6.275406,8.554329,-6.128200,-0.610792,5.114126,6.390841,0.914005,5.605233,-5.623420,-4.354124,2.179939,-9.011858,4.583148,-8.769945,9.387029,-9.640114,-2.292448,8.402534,7.146606,-5.694143,0.454621,0.893890,8.110140], dtype = "float64")#candidate|3304|(2048,)|const|float64
call_3303 = func_1863_call(relay.reshape(const_3304.astype('float64'), [16, 16, 8]))
call_3305 = func_1863_call(relay.reshape(const_3304.astype('float64'), [16, 16, 8]))
func_1084_call = mod.get_global_var('func_1084')
func_1087_call = mutated_mod.get_global_var('func_1087')
const_3309 = relay.const([6,4,2,7,1,-8,3,-4,3,8,6,-3,6,8,-8,9,-6,3,7,10,7,-6,4,-5,-5,7,3,-6,7,-10,2,10,-6,-4,3,3,-1,-4,-1,6,-10,-9,-2,1,-8,4,-4,-8,9,5,7,2,7,7,-3,-3,-3,-5,9,4,-10,-7,-5,7,8,-4,8,-3,3,2,-10,-10,-9,-9,2,-6,-2,-7,8,8,3,-1,9,-7,-3,-10,-8,-7,5,5,-9,-10,-4,9,10,-7,1,-6,-1,5,-6,8,-3,-10,3,8,6,7,6,1,-3,-6,8,5,9,-5,4,8,10,-8,3,7,5,-9,-7,-4,1,-5,6,-10,9,-7,-9,-10,2,4,-5,3,4,-10,2,-1,6,4,5,4,-9,7,-5,-9,-7,2,-3,-2,7,-7,-4,4,4,9,-9,-7,5,8,-3,6,-9,1,-3,6,3,-1,-2,8,-10,-9,-1,1,10,-5,-6,2,9,-5,6,-4,-5,-9,-7,-4,5,10,-10,1,10,-3,-9,10,-8,-2,-6,-5,-1,-7,1,-7,-5,-2,10,4,-1,4,2,10,1,-4,10,10,-6,-10,-10,-3,8,1,1,5,2,4,7,4,9,7,-9,-1,-7,2,-1,-4,10,-4,3,-5,-3,7,-4,-8,-8,2,-3,4,5,-7,1,-3,9,4,-9,6,-7,-9,-5,5,3,3,-10,6,-1,10,-6,-4,2,-8,-6,-2,9,-5,-10,8,-8,1,-7,3,-2,1,6,5,-1,1,-9,-2,4,-3,-10,10,-9,5,-10,6,-1,-9,10,7,9,3,-10,-8,-2,1,-9,9,-5,-6,5,4,8,-5,7,4,-1,-8,9,5,7,5,-10,6,1,8,-5,-3,6,-3,-1,3,-3,-1,6,-6,-4,1,-5,9,10,-5,-10,9,-6,10,-1,-9,3,7,-8,2,-3,-7,-1,-8,4,7,-2,1,-3,5,-4,-8,-4,6,-9,-3,-3,-5,-7,-5,-8,6,-3,8,-9,-9,9,4,4,5,-10,10,-1,8,-9,10,7,5,-6,-5,-8,-2,10,10,5,9,-8,-1,-3,-6,3,-8,-3,-10,8,3,-10,2,-10,5,-10,1,3,-6,10,-7,-9,3,9,-10,-1,-10,-10,10,-7,-5,9,-6,7,-9,3,10,-2,-5,-8,-6,1,-1,-2,-1,6,-5,-4,-1,2,-6,7,-6,-10,-8,7,-9,-3,9,1,-2,8,6], dtype = "int64")#candidate|3309|(462,)|const|int64
call_3308 = func_1084_call(relay.reshape(const_3309.astype('int64'), [7, 6, 11]))
call_3310 = func_1084_call(relay.reshape(const_3309.astype('int64'), [7, 6, 11]))
uop_3314 = relay.rsqrt(call_3293.astype('float64')) # shape=(1, 15, 6)
uop_3316 = relay.rsqrt(call_3296.astype('float64')) # shape=(1, 15, 6)
output = relay.Tuple([bop_3284,const_3294,var_3295,call_3298,var_3299,call_3303,const_3304,call_3308,const_3309,uop_3314,])
output2 = relay.Tuple([bop_3284,const_3294,var_3295,call_3300,var_3299,call_3305,const_3304,call_3310,const_3309,uop_3316,])
func_3320 = relay.Function([var_3283,var_3295,var_3299,], output)
mod['func_3320'] = func_3320
mod = relay.transform.InferType()(mod)
mutated_mod['func_3320'] = func_3320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3320_call = mutated_mod.get_global_var('func_3320')
var_3322 = relay.var("var_3322", dtype = "int32", shape = (3, 6, 7))#candidate|3322|(3, 6, 7)|var|int32
var_3323 = relay.var("var_3323", dtype = "int64", shape = (90,))#candidate|3323|(90,)|var|int64
var_3324 = relay.var("var_3324", dtype = "int16", shape = (16, 14))#candidate|3324|(16, 14)|var|int16
call_3321 = func_3320_call(var_3322,var_3323,var_3324,)
output = call_3321
func_3325 = relay.Function([var_3322,var_3323,var_3324,], output)
mutated_mod['func_3325'] = func_3325
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3486 = relay.var("var_3486", dtype = "int8", shape = (14, 9, 8))#candidate|3486|(14, 9, 8)|var|int8
var_3487 = relay.var("var_3487", dtype = "int8", shape = (14, 9, 8))#candidate|3487|(14, 9, 8)|var|int8
bop_3488 = relay.bitwise_and(var_3486.astype('int8'), relay.reshape(var_3487.astype('int8'), relay.shape_of(var_3486))) # shape=(14, 9, 8)
output = bop_3488
output2 = bop_3488
func_3502 = relay.Function([var_3486,var_3487,], output)
mod['func_3502'] = func_3502
mod = relay.transform.InferType()(mod)
mutated_mod['func_3502'] = func_3502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3502_call = mutated_mod.get_global_var('func_3502')
var_3504 = relay.var("var_3504", dtype = "int8", shape = (14, 9, 8))#candidate|3504|(14, 9, 8)|var|int8
var_3505 = relay.var("var_3505", dtype = "int8", shape = (14, 9, 8))#candidate|3505|(14, 9, 8)|var|int8
call_3503 = func_3502_call(var_3504,var_3505,)
output = call_3503
func_3506 = relay.Function([var_3504,var_3505,], output)
mutated_mod['func_3506'] = func_3506
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3676 = relay.var("var_3676", dtype = "float64", shape = (14, 15, 14))#candidate|3676|(14, 15, 14)|var|float64
uop_3677 = relay.sin(var_3676.astype('float64')) # shape=(14, 15, 14)
uop_3690 = relay.sinh(var_3676.astype('float64')) # shape=(14, 15, 14)
output = relay.Tuple([uop_3677,uop_3690,])
output2 = relay.Tuple([uop_3677,uop_3690,])
func_3704 = relay.Function([var_3676,], output)
mod['func_3704'] = func_3704
mod = relay.transform.InferType()(mod)
var_3705 = relay.var("var_3705", dtype = "float64", shape = (14, 15, 14))#candidate|3705|(14, 15, 14)|var|float64
output = func_3704(var_3705)
func_3706 = relay.Function([var_3705], output)
mutated_mod['func_3706'] = func_3706
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3870 = relay.const(1.728497, dtype = "float64")#candidate|3870|()|const|float64
var_3871 = relay.var("var_3871", dtype = "float64", shape = (16, 7, 16))#candidate|3871|(16, 7, 16)|var|float64
bop_3872 = relay.divide(const_3870.astype('float64'), var_3871.astype('float64')) # shape=(16, 7, 16)
func_1679_call = mod.get_global_var('func_1679')
func_1682_call = mutated_mod.get_global_var('func_1682')
call_3876 = func_1679_call(relay.reshape(const_3870.astype('int32'), []))
call_3877 = func_1679_call(relay.reshape(const_3870.astype('int32'), []))
func_2702_call = mod.get_global_var('func_2702')
func_2706_call = mutated_mod.get_global_var('func_2706')
var_3880 = relay.var("var_3880", dtype = "float32", shape = (720,))#candidate|3880|(720,)|var|float32
const_3881 = relay.const([[1,-3,5,3,2,9],[-5,7,3,-9,3,9],[-5,-6,-4,2,2,-8],[-9,-5,4,2,-3,7],[6,-6,7,-5,-6,1],[1,-7,-7,2,-8,4],[-10,-1,9,8,-6,-6],[-2,5,-2,-1,-8,-8],[5,-10,8,7,4,3],[-6,9,-7,-4,6,8],[6,4,8,-10,1,-6],[-7,9,10,5,2,7],[10,10,-1,-5,10,2],[1,-10,3,3,10,-9],[3,6,9,7,-7,5],[-9,-4,2,-4,-9,7],[-2,-9,-4,3,-6,5],[4,-5,10,8,4,8],[-9,9,7,-7,-10,-1],[7,-2,-3,-8,-8,6],[5,-9,6,-5,8,-3],[1,5,-8,-6,10,-8],[4,8,1,1,-7,-4],[-8,10,-4,2,-4,-9],[-5,7,-4,8,3,3],[9,-1,-4,1,-6,9],[-5,7,10,-2,-4,2],[-8,-7,4,6,-4,2],[-1,-2,-6,-9,4,2],[6,10,-5,-6,-1,-3],[-5,-10,5,10,7,-5],[5,-5,1,-2,1,5],[-4,-8,-7,2,9,2],[-6,-10,-4,-7,10,-7],[-9,-8,-3,-6,-5,2],[5,-4,5,-10,8,-3],[6,3,-10,-7,-1,9],[9,3,-10,-7,-8,-1],[9,-4,-3,1,-7,-7],[7,5,-10,-4,-10,4],[3,-6,2,-5,-9,10],[-6,-3,-7,1,4,-6],[2,5,8,-3,1,-1],[5,6,5,-5,-8,5],[9,-3,-1,9,-8,7],[-4,-6,-8,-7,-5,8],[-10,-2,-3,6,-4,-5],[8,10,6,4,8,4],[9,10,6,-3,-10,7],[-1,-5,3,-9,4,9],[-7,-10,2,-2,5,2],[-7,-8,-9,2,7,6],[7,-1,7,1,-2,10],[4,5,-3,3,-2,-8],[-5,3,-10,-3,6,-8],[-5,-6,1,-9,7,8],[-10,9,1,7,10,1],[-10,-6,10,7,6,-10],[-1,-4,4,-8,3,8],[-5,-4,-4,-4,1,1],[8,9,-1,-1,-10,1],[-6,-8,-6,-7,-9,5],[-7,-8,-1,-2,-6,10],[-9,-2,-7,3,-1,4],[-7,-8,3,-10,2,-1],[-8,1,3,3,-4,3],[7,-5,-8,6,4,-10],[7,7,9,-4,10,-2],[9,-7,10,4,-9,-6],[2,2,5,-2,3,2],[7,10,-1,10,-8,5],[-10,-5,-10,6,2,9],[-10,-2,8,9,-9,-3],[-3,-2,-2,9,6,3],[-5,-9,6,6,6,-1],[1,-10,-8,1,-7,-2],[-8,3,3,1,2,4]], dtype = "int64")#candidate|3881|(77, 6)|const|int64
call_3879 = relay.TupleGetItem(func_2702_call(relay.reshape(var_3880.astype('float32'), [720,]), relay.reshape(const_3881.astype('int64'), [462, 1]), ), 4)
call_3882 = relay.TupleGetItem(func_2706_call(relay.reshape(var_3880.astype('float32'), [720,]), relay.reshape(const_3881.astype('int64'), [462, 1]), ), 4)
output = relay.Tuple([bop_3872,call_3876,call_3879,var_3880,const_3881,])
output2 = relay.Tuple([bop_3872,call_3877,call_3882,var_3880,const_3881,])
func_3889 = relay.Function([var_3871,var_3880,], output)
mod['func_3889'] = func_3889
mod = relay.transform.InferType()(mod)
var_3890 = relay.var("var_3890", dtype = "float64", shape = (16, 7, 16))#candidate|3890|(16, 7, 16)|var|float64
var_3891 = relay.var("var_3891", dtype = "float32", shape = (720,))#candidate|3891|(720,)|var|float32
output = func_3889(var_3890,var_3891,)
func_3892 = relay.Function([var_3890,var_3891,], output)
mutated_mod['func_3892'] = func_3892
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3916 = relay.var("var_3916", dtype = "float32", shape = (12, 16, 11))#candidate|3916|(12, 16, 11)|var|float32
uop_3917 = relay.sinh(var_3916.astype('float32')) # shape=(12, 16, 11)
bop_3920 = relay.logical_xor(uop_3917.astype('uint32'), relay.reshape(var_3916.astype('uint32'), relay.shape_of(uop_3917))) # shape=(12, 16, 11)
uop_3925 = relay.tan(var_3916.astype('float64')) # shape=(12, 16, 11)
func_1302_call = mod.get_global_var('func_1302')
func_1306_call = mutated_mod.get_global_var('func_1306')
var_3932 = relay.var("var_3932", dtype = "int64", shape = ())#candidate|3932|()|var|int64
const_3933 = relay.const([[-8,2],[-5,7],[-6,-3],[-5,-5],[-6,2],[-10,3],[3,-2],[9,10],[4,-5],[-3,-5],[3,3],[6,3],[-2,-8],[-8,-6],[9,8],[5,5],[-9,8],[-5,4],[2,7],[7,4],[5,-2],[2,-5],[-7,9],[8,1],[6,-1],[6,-8],[3,8],[5,9],[-3,2],[8,-6],[-10,-7],[3,-8],[-1,10],[4,-6],[3,-7],[6,-8],[-5,-4],[-10,2],[-9,8],[8,9],[-5,-7],[-8,6],[-6,2],[6,-9],[-2,8]], dtype = "int64")#candidate|3933|(45, 2)|const|int64
call_3931 = func_1302_call(relay.reshape(var_3932.astype('int64'), []), relay.reshape(const_3933.astype('int64'), [1, 15, 6]), )
call_3934 = func_1302_call(relay.reshape(var_3932.astype('int64'), []), relay.reshape(const_3933.astype('int64'), [1, 15, 6]), )
output = relay.Tuple([bop_3920,uop_3925,call_3931,var_3932,const_3933,])
output2 = relay.Tuple([bop_3920,uop_3925,call_3934,var_3932,const_3933,])
func_3937 = relay.Function([var_3916,var_3932,], output)
mod['func_3937'] = func_3937
mod = relay.transform.InferType()(mod)
var_3938 = relay.var("var_3938", dtype = "float32", shape = (12, 16, 11))#candidate|3938|(12, 16, 11)|var|float32
var_3939 = relay.var("var_3939", dtype = "int64", shape = ())#candidate|3939|()|var|int64
output = func_3937(var_3938,var_3939,)
func_3940 = relay.Function([var_3938,var_3939,], output)
mutated_mod['func_3940'] = func_3940
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3958 = relay.var("var_3958", dtype = "float32", shape = (8, 14, 8))#candidate|3958|(8, 14, 8)|var|float32
uop_3959 = relay.acosh(var_3958.astype('float32')) # shape=(8, 14, 8)
output = relay.Tuple([uop_3959,])
output2 = relay.Tuple([uop_3959,])
func_3973 = relay.Function([var_3958,], output)
mod['func_3973'] = func_3973
mod = relay.transform.InferType()(mod)
var_3974 = relay.var("var_3974", dtype = "float32", shape = (8, 14, 8))#candidate|3974|(8, 14, 8)|var|float32
output = func_3973(var_3974)
func_3975 = relay.Function([var_3974], output)
mutated_mod['func_3975'] = func_3975
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4012 = relay.const(1, dtype = "int64")#candidate|4012|()|const|int64
var_4013 = relay.var("var_4013", dtype = "int64", shape = (3, 13, 2))#candidate|4013|(3, 13, 2)|var|int64
bop_4014 = relay.not_equal(const_4012.astype('bool'), var_4013.astype('bool')) # shape=(3, 13, 2)
output = bop_4014
output2 = bop_4014
func_4017 = relay.Function([var_4013,], output)
mod['func_4017'] = func_4017
mod = relay.transform.InferType()(mod)
mutated_mod['func_4017'] = func_4017
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4018 = relay.var("var_4018", dtype = "int64", shape = (3, 13, 2))#candidate|4018|(3, 13, 2)|var|int64
func_4017_call = mutated_mod.get_global_var('func_4017')
call_4019 = func_4017_call(var_4018)
output = call_4019
func_4020 = relay.Function([var_4018], output)
mutated_mod['func_4020'] = func_4020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4181 = relay.var("var_4181", dtype = "int16", shape = (16, 8, 13))#candidate|4181|(16, 8, 13)|var|int16
const_4182 = relay.const([[[4,2,2,9,4,10,-4,8,-3,-8,8,-4,7],[-9,-9,-1,-10,-7,10,6,-6,2,7,1,-4,-8],[10,1,7,8,-10,-3,6,5,-5,-2,7,3,5],[6,3,-4,-6,-2,-4,3,1,-6,-3,3,-4,-1],[8,-5,-9,4,2,7,-4,3,1,-2,1,9,1],[-3,6,5,9,-9,-8,-2,-3,-10,-8,-5,-8,-1],[-6,-2,2,-3,-1,-2,-8,-1,-4,-7,-2,1,10],[8,2,-9,-10,7,-8,8,-1,-2,-1,-3,7,-1]],[[-9,-6,-8,-8,-6,3,8,5,2,-7,-6,-2,-3],[-2,-7,9,5,4,10,8,-9,-1,10,-4,3,-7],[-2,6,4,-8,-2,8,2,3,-3,9,1,-10,-8],[-3,-8,8,9,-9,-3,-5,-4,2,-4,10,-7,1],[9,-7,6,5,-2,5,-8,-4,1,-8,4,-1,-7],[8,-7,10,-10,10,8,-3,-10,-10,3,1,-7,9],[9,2,8,-9,-10,-3,-7,10,10,-6,10,-9,1],[-6,-9,10,4,5,3,-1,3,5,8,-5,-7,-9]],[[8,3,-9,8,4,7,1,4,-6,-6,8,10,7],[4,-8,-2,-2,4,3,-1,-9,9,-8,3,-5,-4],[-10,-8,-10,10,5,2,8,9,9,2,-8,-9,1],[10,-1,-10,-9,-6,1,6,-10,3,6,1,4,3],[-2,8,-4,-3,5,6,4,-2,9,-10,6,-7,7],[-6,-9,1,-3,7,7,2,5,-5,-1,-3,3,-9],[7,1,-6,-5,10,-8,-6,10,-7,5,-4,1,7],[6,-7,9,3,-10,-9,-3,4,1,8,-3,-8,9]],[[9,5,-3,-6,-6,-4,6,-5,2,3,-1,4,-6],[6,-7,5,-4,4,3,-6,6,7,8,7,2,-6],[2,4,-8,3,-7,3,-1,7,-6,3,6,4,-4],[4,8,-10,-9,-2,7,2,6,-5,2,-10,-8,-10],[7,-8,4,-6,9,5,-2,-5,-4,5,4,-6,-4],[5,-3,6,-1,-8,4,7,2,3,1,-5,9,-3],[-9,-9,7,-5,-1,8,-3,4,2,5,5,10,-8],[-1,6,-9,-4,8,-2,-2,3,-2,-8,-8,-2,-4]],[[10,5,10,4,1,-1,-2,6,3,7,-8,4,7],[-6,-4,-6,-6,-2,-6,-2,-10,1,1,7,3,-2],[1,7,-10,7,-3,8,-3,-6,7,-5,3,2,-3],[-10,1,7,9,-1,7,3,-10,-9,-1,1,7,8],[4,-3,-9,3,-4,1,6,-2,-10,5,6,-3,3],[9,-4,7,7,2,5,-3,8,2,-7,-7,1,-9],[7,6,-7,-7,1,8,-6,-3,8,9,3,-9,8],[-9,9,-6,9,-6,6,-7,1,-7,8,7,-8,-1]],[[10,1,-8,-6,6,5,3,-2,-9,10,-6,7,6],[9,2,5,10,9,4,-6,7,-6,7,1,-10,-5],[7,8,8,7,7,-10,-8,6,-4,4,6,-4,-9],[8,-8,-6,5,-10,1,-2,9,-7,3,-1,-4,10],[5,2,9,-3,-4,-3,5,3,1,6,7,1,5],[-7,-4,-10,1,3,3,-8,-7,8,-4,-7,6,9],[7,3,9,-10,9,4,-3,9,-4,-4,9,2,3],[-10,-3,2,8,-1,-9,4,2,-7,4,2,4,9]],[[-8,-7,-10,-9,6,2,-1,5,-3,-8,-4,1,-3],[-7,9,-8,-9,-7,2,4,9,5,1,10,6,1],[4,-9,-3,4,2,-8,-9,-10,10,10,-1,1,-5],[-6,-10,-1,8,-3,-6,-2,9,9,-4,-10,4,6],[-6,-7,-10,2,-1,6,2,-10,-6,-7,4,-4,5],[-5,-7,4,9,-4,6,1,-8,-7,-6,-9,3,7],[1,6,-9,-5,-3,10,10,-1,10,4,-8,-10,-9],[-5,4,2,7,-1,10,-1,-5,-2,-6,1,-4,-6]],[[7,-5,5,-1,-5,-8,10,9,7,2,2,9,9],[-4,7,5,7,10,-3,-3,-5,-3,10,6,3,-1],[2,-4,10,-3,-9,-10,-10,8,-3,-2,-2,5,6],[-3,-9,-5,-4,3,-7,2,-7,-10,-5,10,9,-6],[8,7,3,4,-4,-5,6,-4,-8,-8,-9,4,9],[1,8,1,9,10,9,5,3,-2,2,3,-2,-5],[-1,4,2,8,-5,6,8,-7,1,10,6,4,-8],[9,8,-3,-2,-7,-6,-6,5,-4,-9,-1,7,-6]],[[-5,-2,-5,-5,7,-2,-6,-5,7,3,5,-6,-10],[-7,-10,1,-3,-8,-6,-1,-2,-1,-5,1,10,-3],[-1,1,8,8,3,3,2,4,6,-10,2,7,8],[7,-3,-4,1,-6,5,9,5,6,5,5,7,2],[-7,-5,8,-6,4,7,-7,-4,-9,2,5,1,-8],[-3,-4,-2,-5,-7,-1,-6,-2,10,-6,-2,7,6],[2,4,-6,4,-4,-10,-5,2,1,-1,-8,2,7],[-8,-10,8,2,5,-1,-7,-5,-3,-5,6,-10,-8]],[[-10,-4,-8,1,7,-1,5,8,-5,10,3,2,-8],[-3,-9,-9,-3,6,-7,9,-10,4,8,-1,8,-3],[-5,-6,-7,-1,2,-3,-5,4,10,6,6,3,-4],[7,6,-1,-6,3,-8,8,-4,-2,-4,3,-2,1],[-8,1,9,-4,-7,5,1,-7,-2,-6,-9,-9,9],[-4,8,-10,-10,-10,1,5,6,1,7,8,-4,10],[-5,6,-9,-6,6,5,6,-6,-9,5,10,-5,-6],[10,7,5,9,7,-2,4,6,-5,-7,9,1,-1]],[[2,1,7,1,-3,8,-8,9,8,9,5,8,6],[-7,-3,-9,4,-4,3,-7,-2,8,9,-3,1,3],[-7,-9,10,9,4,-10,-9,-9,10,9,-2,5,2],[-10,-9,2,-4,8,-7,-9,4,-1,-4,5,8,-9],[1,-4,1,8,7,-7,-1,6,1,-10,5,-9,-4],[6,-10,-4,8,-4,2,-10,-3,1,-1,3,2,-10],[-9,-7,-5,6,-7,-6,8,3,-5,-8,-9,4,6],[5,-5,5,6,-6,7,6,-2,-9,4,10,-5,10]],[[7,-6,-3,9,8,1,-9,4,-9,-10,-5,-1,8],[-10,2,-9,-6,-10,-5,-7,4,-6,-5,9,-1,4],[7,-6,-9,-10,-8,7,-3,3,7,-3,-9,6,-7],[7,5,5,9,6,8,8,-6,-10,-4,-1,4,-4],[10,7,4,-9,-7,10,6,3,-6,1,-8,3,5],[-2,7,-2,-5,-8,4,9,-2,7,-9,-3,3,-8],[-9,2,-4,-3,-10,10,3,-6,5,-10,6,-6,-10],[-9,7,6,10,-7,2,-7,-4,-10,7,6,1,9]],[[-3,-2,6,-10,1,-6,-3,5,-3,-10,1,6,5],[-10,-7,-4,3,-5,-7,1,-10,9,2,-9,-6,3],[-8,-5,-10,9,-1,-8,-9,7,-10,6,-7,-3,8],[-5,-2,2,-7,3,10,-3,-7,9,-5,-3,-5,5],[1,1,2,4,2,4,-2,7,10,-5,2,-4,8],[-4,-4,5,8,5,-1,2,4,5,2,10,-3,-1],[-6,-5,-10,-9,7,2,-1,-5,-7,-8,-4,8,4],[-10,-10,-5,5,5,7,4,10,-1,-2,-5,-5,9]],[[-5,-5,-5,-7,5,-5,2,-10,6,4,9,-8,2],[-9,6,4,6,-2,4,8,-1,-2,3,-1,5,4],[1,-4,-7,9,10,7,-3,-9,-8,8,9,4,1],[10,3,9,-10,-8,-5,-2,-10,-5,8,4,8,-7],[2,-1,-9,1,7,-7,-5,3,9,7,4,6,5],[-10,-2,1,2,-6,-3,4,-7,8,-3,-3,8,-6],[1,6,2,10,7,-5,-3,2,8,-7,-7,10,-6],[4,3,8,-2,2,4,-5,3,-2,2,2,9,8]],[[4,10,9,6,6,7,-10,-1,1,5,-9,-10,-10],[3,-2,9,-7,8,3,-9,7,6,-5,2,-4,-1],[4,1,4,7,-5,3,-5,1,4,8,5,9,-10],[9,-7,-6,2,9,3,5,4,1,9,-9,1,-4],[-1,8,1,-7,8,1,3,7,6,4,-7,9,-9],[9,-6,-6,-6,-10,4,7,-3,1,8,9,-9,4],[-10,-4,-1,-8,-5,-6,3,-10,-7,8,-7,3,-6],[-1,-7,-10,10,-5,8,10,10,-6,5,-9,-5,10]],[[5,-9,-8,-7,-7,-2,-3,-10,10,4,-9,4,-6],[-6,-9,1,2,6,-2,2,10,-8,1,-3,9,5],[-8,2,2,-3,6,7,-5,5,6,7,-3,2,-3],[7,2,10,8,4,-9,3,2,-3,-4,4,-8,-7],[-6,-5,4,2,3,-8,3,-3,8,10,-9,-4,-3],[-3,9,-4,-1,-5,2,-2,7,-7,1,-5,-7,8],[-7,-9,1,3,-3,7,5,-2,-7,-1,-6,7,10],[6,-6,-3,7,5,-5,-7,3,-6,-6,-7,-3,-9]]], dtype = "int16")#candidate|4182|(16, 8, 13)|const|int16
bop_4183 = relay.equal(var_4181.astype('bool'), relay.reshape(const_4182.astype('bool'), relay.shape_of(var_4181))) # shape=(16, 8, 13)
const_4195 = relay.const([[[-5,-7,2,-1,8,1,8,3,-2,1,2,5,-3],[8,-2,2,-2,8,-7,-8,10,8,-7,-1,-9,9],[4,-9,-4,7,-1,-5,-9,8,-1,-2,6,-9,10],[4,-6,-1,6,7,4,-5,-4,10,3,-9,4,5],[1,5,-8,1,1,-6,1,-4,-7,1,-9,-3,1],[-9,5,-7,2,10,-10,-5,2,-5,-5,9,7,-3],[3,1,10,-8,-3,-3,-6,4,3,-6,-1,9,1],[-7,-10,-9,6,6,9,3,1,-9,-9,5,-4,-1]],[[6,-2,10,7,10,4,3,2,-5,8,-8,-5,1],[1,4,2,-3,-7,2,4,8,-7,-7,-7,-3,10],[-1,2,-6,-7,6,8,-2,2,-9,-7,2,9,5],[6,8,-1,3,-1,6,-9,5,-2,4,-2,-8,-9],[-5,4,4,-7,-5,3,2,9,10,-10,7,4,4],[4,7,4,2,1,5,-10,8,10,-5,-8,9,4],[8,7,5,3,5,-5,5,-4,-6,3,-6,-4,4],[-10,7,-8,1,8,7,10,-1,10,3,-6,-8,4]],[[4,9,-1,-10,2,-5,3,10,5,5,-7,9,1],[-2,4,5,6,-5,-4,5,-5,10,4,-2,-10,-4],[-2,-8,10,-1,7,-4,9,-10,-6,-8,5,-1,-8],[7,-7,-8,4,1,-5,10,-8,5,-6,2,-9,-5],[10,5,-10,-9,-3,-6,-2,-3,-9,1,9,-5,-10],[-9,9,5,-1,-7,-3,7,-3,5,2,-2,-2,8],[-8,8,-2,-9,10,-8,6,-1,-4,-9,1,-2,-3],[-4,9,8,-7,-7,3,9,2,4,7,-9,4,-9]],[[1,8,8,-8,-5,6,3,2,9,-9,1,9,1],[-8,-5,9,-8,1,-10,5,-7,1,6,8,-5,4],[-2,-3,-2,-7,-5,4,-5,1,4,-5,9,-3,-9],[10,-5,1,9,2,4,8,-8,-5,9,-2,-4,-6],[-3,7,7,10,-2,-1,5,-2,-5,-10,-7,9,1],[-9,-8,-7,3,5,-1,-1,-7,6,8,-3,-10,-7],[8,-3,7,3,8,-6,-5,-10,-5,-1,-5,-4,-5],[-7,10,4,-2,-6,-2,4,-10,-10,1,-1,-10,1]],[[-7,8,4,9,-9,-1,-3,-10,7,-4,6,9,-3],[-8,-3,10,-3,-4,-6,-2,-9,8,1,4,3,6],[1,9,-8,-10,-5,10,1,-7,-10,-3,-4,-10,10],[5,-1,5,6,9,10,-4,-2,-2,-10,-1,8,9],[5,-8,-3,-8,-4,8,6,6,7,-8,-6,-1,1],[-7,3,2,-7,-3,-5,-5,-2,1,-2,-4,8,-7],[4,1,7,-6,-7,-10,-1,5,4,5,4,-5,-6],[5,-3,-8,-8,4,-10,10,1,2,-5,-7,6,6]],[[-1,-6,2,-1,-2,3,2,7,-10,-9,-9,4,-5],[-2,5,3,-2,3,10,8,4,2,-1,-6,-6,-3],[-6,-8,7,4,-9,-10,-5,5,-6,7,-6,-4,10],[7,6,2,4,5,-1,5,-5,10,-7,-5,-10,3],[-3,-3,8,10,10,8,-1,7,-1,1,7,-5,-8],[5,5,4,-6,3,-6,2,5,10,-2,-10,-9,-6],[-6,-9,3,4,4,8,-6,-6,3,8,7,-8,7],[9,-10,-10,-7,-3,-7,-8,5,-2,8,5,5,1]],[[-3,10,-6,-6,5,-5,7,3,-4,-6,9,-2,-6],[-8,2,5,-8,-7,-4,-5,9,1,7,-1,-7,2],[4,2,-2,-3,10,10,-2,6,-10,-7,10,-6,-2],[-10,3,-4,7,-9,6,3,-9,-8,2,9,5,-10],[3,-4,4,-5,-7,5,5,-10,3,9,-6,5,10],[-9,-9,10,6,1,9,8,5,7,-5,-2,-2,-10],[-7,6,8,-4,8,-3,9,4,-9,3,6,-3,9],[-9,6,9,6,-5,-3,-5,3,5,1,-2,-4,4]],[[7,2,5,-4,3,-6,-1,5,-8,-4,10,6,3],[-2,5,8,5,7,-1,1,-4,-5,6,10,-2,-8],[6,-4,4,-7,-1,-2,-4,6,-9,9,4,8,-4],[7,-5,-8,10,1,7,-4,2,7,-4,3,-2,7],[-6,9,3,8,4,8,-10,-10,6,5,10,6,-7],[-5,1,8,-7,1,-4,10,7,-1,-9,-1,-5,-5],[-2,-8,1,-9,-7,2,-5,-6,2,-8,5,5,2],[-1,6,-3,8,-7,-7,1,-5,-8,8,1,9,10]],[[-1,-10,-4,-10,-6,7,6,-2,2,7,-10,8,-8],[-1,-10,-2,7,4,4,10,-8,-5,2,-5,5,-4],[6,7,2,-2,-9,3,-8,-7,-10,-6,5,3,1],[4,2,4,-9,-2,7,3,-8,-1,-1,1,-5,-4],[-8,-10,4,6,-1,4,1,2,7,3,-10,-2,-3],[6,9,8,6,-8,-1,6,7,3,5,-6,-9,-8],[5,3,4,-4,9,2,-10,-6,7,3,2,-1,-9],[9,-6,-10,8,9,-3,7,-4,7,-9,5,5,-9]],[[-1,-3,-7,-2,-9,6,-6,-7,7,-10,3,7,10],[-10,-9,1,-9,-10,-5,9,-5,-9,-9,1,-2,-1],[10,-1,-9,5,-9,-7,1,3,2,-9,-9,9,9],[-6,-2,-8,-4,-3,9,10,-6,-6,-6,4,3,6],[-4,-9,-6,-5,-9,-1,3,5,-5,2,4,10,-7],[10,8,1,1,-6,-3,5,6,-5,1,-1,-5,-8],[10,-10,2,6,-6,-1,-7,3,-8,1,6,2,-6],[-6,7,1,-3,6,-1,-3,-1,3,3,-7,-6,-4]],[[-4,2,1,-2,-1,8,6,-9,-8,3,9,7,-3],[3,-3,-4,3,-1,-3,7,-8,9,-10,-2,-1,8],[-2,-1,9,4,1,3,5,10,-6,3,-1,7,-1],[10,5,-3,2,10,8,-5,4,-4,-1,7,1,-1],[-2,-4,9,-4,-3,-9,-3,-8,5,-1,-3,-9,9],[-10,-6,5,-9,-1,-4,-3,2,-3,1,5,7,8],[-2,4,3,-4,-5,8,-9,-4,-4,1,7,10,-9],[5,-2,6,9,7,-4,-2,-9,4,-9,-2,-3,8]],[[9,7,4,4,4,2,-9,-5,10,-3,10,-7,-4],[-2,2,-7,8,8,8,10,1,-5,-8,5,-2,7],[6,2,2,6,-6,4,-9,-7,-4,10,6,-8,-6],[4,-3,-9,-4,-8,-7,-2,-1,6,-9,-8,-10,10],[4,2,-3,9,7,5,-10,-10,9,-9,-8,-10,-8],[2,7,-3,2,-10,-2,-10,-6,2,8,-3,6,9],[7,-3,-10,-2,-8,9,-4,2,-7,-7,-7,-10,-3],[-4,-5,2,-2,6,1,8,-4,-7,5,6,-4,-8]],[[-2,-6,1,3,-10,-5,-2,-4,-8,-2,1,-3,-1],[-10,-2,7,-7,8,-2,-4,-7,-7,-10,4,5,-4],[-7,3,-6,4,1,3,-4,-6,3,9,8,1,-8],[8,10,8,-9,-7,5,-4,-3,-4,7,3,9,1],[9,7,-8,-9,-5,8,-1,8,4,-2,-10,-2,-10],[6,-7,9,1,-3,1,7,-10,-9,-8,7,-2,9],[-9,6,5,9,10,-10,-3,8,-5,-9,10,8,-8],[9,5,-9,-8,4,-8,-7,-10,-1,-2,-9,4,3]],[[-8,1,7,-6,-6,7,-2,9,-3,-10,7,-7,10],[5,-6,9,3,-1,-10,3,2,3,-2,-5,1,1],[9,-5,6,7,2,5,8,6,-3,-5,10,10,-10],[-8,-4,-9,6,4,-5,3,6,3,-6,-3,7,-5],[-6,10,1,7,8,8,9,8,-2,-3,1,-4,4],[-7,5,-1,-8,-9,10,4,-1,6,4,-5,-6,-9],[-4,-7,10,3,-5,-8,-5,2,2,-7,-10,-4,8],[-3,8,5,-6,-2,4,4,10,-4,1,-4,2,10]],[[6,-8,-3,-9,2,-3,-4,-7,-2,10,4,-1,-10],[10,8,-5,3,-7,4,-9,9,7,9,-4,4,5],[9,-5,-10,-4,6,-3,5,-9,-5,7,10,-9,-9],[-2,-10,3,4,2,-6,4,-6,-4,6,-1,-10,5],[4,1,-9,-8,-1,-10,-2,10,-7,-1,3,5,7],[-10,-6,-8,-1,8,1,10,-9,-8,-1,1,7,2],[-9,7,6,-2,-4,-5,-9,-4,-8,-6,-5,10,-5],[5,-4,1,-5,-9,8,3,4,-7,-10,-7,5,7]],[[-8,-7,1,8,-8,-1,9,-6,-3,-9,9,-4,-6],[9,-4,3,-7,-6,10,-4,-3,1,-4,9,8,-8],[1,-5,-3,-8,3,9,-2,8,1,2,6,-5,2],[10,1,4,10,-9,-8,-9,10,2,-5,6,2,-1],[1,1,-2,-3,10,7,9,-2,4,-9,-9,8,1],[1,2,-2,-8,8,5,-2,-9,5,-4,-6,-10,5],[-5,-5,-7,-8,8,3,4,-5,3,3,4,-3,-7],[-7,3,6,4,-4,10,9,-5,-4,-6,-7,-6,-2]]], dtype = "int16")#candidate|4195|(16, 8, 13)|const|int16
bop_4196 = relay.mod(var_4181.astype('float32'), relay.reshape(const_4195.astype('float32'), relay.shape_of(var_4181))) # shape=(16, 8, 13)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
var_4203 = relay.var("var_4203", dtype = "float32", shape = (720,))#candidate|4203|(720,)|var|float32
call_4202 = relay.TupleGetItem(func_68_call(relay.reshape(var_4203.astype('float32'), [15, 16, 3])), 0)
call_4204 = relay.TupleGetItem(func_71_call(relay.reshape(var_4203.astype('float32'), [15, 16, 3])), 0)
func_4017_call = mod.get_global_var('func_4017')
func_4020_call = mutated_mod.get_global_var('func_4020')
const_4230 = relay.const([9,-10,-5,-8,1,-9,-1,-4,7,2,10,8,5,2,-7,1,2,5,-10,-8,8,-1,4,-9,7,-10,3,4,9,-1,-9,-4,-6,8,-1,-8,-6,7,-6,-10,2,-1,-1,-4,3,7,-10,4,-10,-1,-1,-2,-9,6,7,-10,7,3,8,-8,-5,-2,-6,8,-9,10,7,8,1,3,1,9,5,-7,1,4,10,8], dtype = "int64")#candidate|4230|(78,)|const|int64
call_4229 = func_4017_call(relay.reshape(const_4230.astype('int64'), [3, 13, 2]))
call_4231 = func_4017_call(relay.reshape(const_4230.astype('int64'), [3, 13, 2]))
func_1679_call = mod.get_global_var('func_1679')
func_1682_call = mutated_mod.get_global_var('func_1682')
const_4250 = relay.const(-8, dtype = "int32")#candidate|4250|()|const|int32
call_4249 = func_1679_call(relay.reshape(const_4250.astype('int32'), []))
call_4251 = func_1679_call(relay.reshape(const_4250.astype('int32'), []))
uop_4252 = relay.cos(const_4230.astype('float32')) # shape=(78,)
output = relay.Tuple([bop_4183,bop_4196,call_4202,var_4203,call_4229,call_4249,const_4250,uop_4252,])
output2 = relay.Tuple([bop_4183,bop_4196,call_4204,var_4203,call_4231,call_4251,const_4250,uop_4252,])
func_4255 = relay.Function([var_4181,var_4203,], output)
mod['func_4255'] = func_4255
mod = relay.transform.InferType()(mod)
var_4256 = relay.var("var_4256", dtype = "int16", shape = (16, 8, 13))#candidate|4256|(16, 8, 13)|var|int16
var_4257 = relay.var("var_4257", dtype = "float32", shape = (720,))#candidate|4257|(720,)|var|float32
output = func_4255(var_4256,var_4257,)
func_4258 = relay.Function([var_4256,var_4257,], output)
mutated_mod['func_4258'] = func_4258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4270 = relay.var("var_4270", dtype = "int16", shape = (16, 4, 4))#candidate|4270|(16, 4, 4)|var|int16
var_4271 = relay.var("var_4271", dtype = "int16", shape = (16, 4, 4))#candidate|4271|(16, 4, 4)|var|int16
bop_4272 = relay.add(var_4270.astype('int16'), relay.reshape(var_4271.astype('int16'), relay.shape_of(var_4270))) # shape=(16, 4, 4)
uop_4277 = relay.sinh(bop_4272.astype('float64')) # shape=(16, 4, 4)
bop_4282 = relay.less(uop_4277.astype('bool'), relay.reshape(bop_4272.astype('bool'), relay.shape_of(uop_4277))) # shape=(16, 4, 4)
uop_4285 = relay.log2(bop_4272.astype('float32')) # shape=(16, 4, 4)
output = relay.Tuple([bop_4282,uop_4285,])
output2 = relay.Tuple([bop_4282,uop_4285,])
func_4289 = relay.Function([var_4270,var_4271,], output)
mod['func_4289'] = func_4289
mod = relay.transform.InferType()(mod)
mutated_mod['func_4289'] = func_4289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4289_call = mutated_mod.get_global_var('func_4289')
var_4291 = relay.var("var_4291", dtype = "int16", shape = (16, 4, 4))#candidate|4291|(16, 4, 4)|var|int16
var_4292 = relay.var("var_4292", dtype = "int16", shape = (16, 4, 4))#candidate|4292|(16, 4, 4)|var|int16
call_4290 = func_4289_call(var_4291,var_4292,)
output = call_4290
func_4293 = relay.Function([var_4291,var_4292,], output)
mutated_mod['func_4293'] = func_4293
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4452 = relay.const(4.570016, dtype = "float32")#candidate|4452|()|const|float32
const_4453 = relay.const([[[4.037939,-5.101939,-9.296183,-9.510160,2.686382,4.238604],[-0.376135,8.155596,-9.012644,-5.314759,-0.399850,-1.567415],[6.479859,1.960290,-0.673305,-6.604769,7.790274,4.587559],[7.829096,8.302630,0.492880,6.488492,-0.552523,2.782874],[9.291429,-1.007139,-6.393894,-2.274609,-3.392725,8.655766],[-5.762940,-0.463473,-2.830106,5.514105,9.022522,-8.602520],[-8.921548,-9.392431,4.184617,6.608932,-9.876732,-2.540716],[-8.116532,-3.633827,5.191489,9.995951,7.152355,4.035960],[3.346560,7.664969,9.380699,3.996914,-1.531340,-3.691922],[-4.740285,-8.945433,-8.971804,9.235715,3.009864,6.740314],[-7.598020,1.695965,-3.332686,2.043552,1.988494,-7.701422],[7.825590,-5.360711,6.709252,5.265186,-6.867849,-8.364125],[-1.524340,-1.956259,-9.055193,-7.489497,-8.102757,-5.507077],[-3.500902,6.308373,6.330841,-2.600756,8.178340,-0.310934],[-5.532889,-8.080594,5.171067,4.903595,6.422470,-2.781782],[8.928662,-5.926224,-5.381230,-2.673478,-0.187890,-4.699664]],[[4.259587,-1.581292,-5.634774,2.493498,-3.465976,7.190675],[7.282896,-1.982392,-0.613157,-8.297561,8.902480,-7.228838],[8.044619,9.874159,-9.378790,3.936576,-4.014899,-9.046613],[-2.226006,4.789256,-2.917164,7.780625,8.695796,-7.237293],[-8.783489,1.285757,2.753988,6.689248,-8.614616,-2.744403],[-7.659425,-6.119971,-3.307653,2.204842,0.848445,4.192208],[-8.878385,5.321097,-5.420965,0.930018,-0.001889,2.185726],[-5.119226,-5.969788,1.379302,4.490198,2.040878,-3.218250],[3.725969,-2.378105,7.276627,-0.235123,-3.455457,9.788650],[9.664913,9.837040,-4.041059,8.178212,5.446488,7.410912],[-1.077977,2.812357,4.473426,8.543971,9.826461,1.998011],[-6.299898,-2.285874,0.734494,8.495363,2.942274,-3.292641],[0.537938,-4.248474,1.086756,3.370569,7.340592,0.516709],[8.100393,6.295627,9.345945,2.122404,-5.937203,-7.467725],[3.918349,-1.372550,0.106330,-0.410796,-9.140520,8.091114],[3.982073,3.377494,4.241725,2.621216,-9.502577,-1.049244]],[[3.294594,8.743091,2.705957,6.584910,0.482490,4.145963],[-2.408243,-8.433956,5.229451,-5.060155,-4.221688,5.400492],[9.954834,-8.999130,5.277464,1.007396,-2.207829,-0.152059],[-3.398193,5.628184,1.861834,-7.159935,-3.374360,-6.211093],[5.493593,-6.702271,-0.970125,6.482164,-9.021120,2.718406],[-0.668024,-5.187628,2.594454,2.341355,-5.974484,-5.199715],[3.542705,1.465306,3.011375,2.863384,2.768245,-4.535557],[2.310628,7.615972,-8.215722,7.899719,6.025694,6.165458],[-7.338084,-2.544187,6.909702,-0.669089,-7.830682,4.883218],[6.958743,-9.689741,-0.849140,5.606361,-1.088717,-2.290879],[3.906031,-0.961689,8.609805,-2.161963,-5.172260,9.829201],[8.909021,-1.669380,0.839874,2.208322,5.989405,9.516833],[-6.720575,4.281992,4.956611,3.866372,-7.122197,2.082326],[-4.522921,3.873735,4.343538,-4.961011,9.305689,-0.303177],[-4.647830,8.180996,9.308070,-3.527333,2.309115,-4.746924],[2.565663,-9.540803,2.814531,6.197646,3.131963,-2.463618]],[[8.837837,6.082914,-9.820540,-6.261524,3.968004,-1.083378],[-9.540084,-7.911928,-5.327679,4.661740,4.268665,9.159182],[9.554176,-5.517548,-2.088804,0.416912,9.186222,-0.725989],[-9.358355,5.886840,-5.167894,-1.786338,-5.188525,7.888265],[-9.945546,-1.870170,-0.029164,-6.431449,-8.290456,-8.005517],[-0.130875,2.547210,-8.623535,0.599849,-4.925293,-8.756598],[-6.502911,0.102677,7.274871,8.765342,5.518335,9.422077],[-0.457020,-2.669943,-5.487836,1.104557,-2.928690,3.895933],[-1.058307,-2.525413,6.423815,0.413075,8.807589,-5.711917],[2.524297,-4.808671,3.608536,-1.066594,-9.128933,-2.589673],[4.474631,8.542324,-9.831254,-8.609520,9.723499,8.403839],[4.475742,-7.939330,-0.129556,-1.946311,-2.097188,-2.800032],[-0.325323,5.486763,7.312029,-5.746500,8.926206,8.966424],[-4.876310,-5.345691,-2.000159,-8.852645,7.134474,-9.488910],[3.588561,2.792869,-4.059682,3.865767,3.525496,4.585265],[-5.905725,0.875283,4.737405,-2.229626,2.748588,3.863775]],[[-6.446656,6.843246,-6.295144,1.836530,-5.667002,2.007766],[2.896521,-0.270316,-3.960500,1.850663,7.372601,-4.928922],[3.834737,-9.413656,-5.689420,-3.443763,2.572474,-0.200414],[-8.466025,9.656561,-1.315800,5.487245,4.533074,-1.708947],[4.655567,-3.354170,3.829869,4.459440,0.198895,1.501241],[7.039726,6.989391,8.416548,-1.670398,1.911918,9.719500],[-0.057372,5.605489,-2.963034,0.363308,-9.056663,-7.024630],[8.950897,-5.410471,8.951402,-5.595058,-1.739437,0.650704],[7.434520,9.538376,0.905584,-5.637334,4.513856,9.335109],[-4.163394,7.015217,-1.501728,-8.318256,9.242934,3.495887],[-3.277478,6.108694,4.225512,-9.247299,-9.668543,1.257013],[-4.034975,3.385404,-9.909001,1.546598,-9.610386,5.731164],[-6.156147,-3.403303,-3.006354,-2.974970,6.869097,9.740957],[-6.693889,0.633038,9.932188,-6.232829,-2.243767,1.025843],[-6.637284,6.299838,2.353152,-3.465817,-3.759403,0.393650],[-9.443817,3.619927,9.860444,-5.666590,0.205805,-7.294588]],[[-2.001208,-8.464251,5.035383,1.143592,0.147134,-8.046535],[2.203901,-2.165103,7.752924,4.891702,-6.604646,5.446193],[8.878876,9.998414,7.180008,-9.142396,9.016757,-9.979018],[-5.891032,-5.388790,2.701453,0.410525,2.753987,-9.100720],[2.768358,-5.106219,6.737474,-1.620093,4.207854,2.590441],[9.962202,1.608376,-5.818308,4.686693,9.639920,-7.756162],[-4.744886,-2.478370,-6.228185,-1.792113,-4.238384,2.734415],[-0.323721,-0.589225,4.057847,-6.572687,9.236594,1.306188],[-1.380600,1.979181,1.782532,-8.543684,0.173058,3.296209],[9.673699,2.472826,4.151161,7.805775,-4.226918,1.672318],[3.408995,2.109179,2.896797,4.833005,4.157855,-6.205676],[-8.381832,7.366224,5.611730,5.707400,-7.385305,-7.904187],[8.463920,-6.007728,2.725655,-5.954867,4.080635,-8.473864],[-7.996614,-0.753674,-6.691524,-8.941888,2.475695,-1.402679],[2.429938,-5.721392,-3.524029,5.079120,-4.564652,-1.720946],[1.219311,5.125643,-0.584463,-6.952861,3.745158,-8.229681]],[[9.510605,-9.448318,-1.601356,2.718623,7.629949,-7.444675],[-8.064980,6.626698,6.868778,-1.534132,-0.334635,1.139607],[2.219330,-0.834695,7.922628,-4.739542,0.665860,5.161425],[2.997662,5.848796,-7.566201,6.880040,7.735122,-8.431381],[-5.002497,-3.633301,-0.545006,7.426601,8.916054,-9.509960],[-0.602562,5.324682,0.262538,-4.940659,7.736595,2.411329],[7.024530,-1.447168,-9.972034,3.807302,4.215046,4.703924],[6.648048,-2.422532,-2.629668,4.143359,4.058232,9.707608],[-6.222190,-6.215316,4.065283,7.502044,-8.763838,-4.413329],[-1.384263,0.581603,6.021419,4.949066,5.500466,2.115787],[-9.027736,-0.258168,2.250323,8.615991,8.412212,7.471500],[1.595332,7.771271,-4.143094,-1.879293,6.139213,-3.093188],[8.314934,-3.656913,8.405198,-4.313601,-9.800275,-5.383228],[-5.842797,1.091082,6.430880,8.160914,-7.560867,-2.910707],[-8.889928,8.274648,-3.342153,-4.719350,-2.372515,-7.859004],[-1.510646,1.404605,4.506401,-6.645187,8.167888,-9.570584]],[[-9.575107,-7.369210,-8.998626,1.569206,4.574885,1.984520],[-5.087040,7.672048,-9.367572,3.618442,7.856775,2.033315],[-2.199325,-1.252010,-9.850463,-8.618432,-9.196831,0.672804],[8.846851,2.837945,6.863744,-1.928956,-5.078795,-9.523391],[7.833191,2.040024,4.886617,3.241412,-3.505542,4.359237],[-4.126299,4.159764,-3.270292,-7.467002,3.297827,6.236889],[-4.456211,7.489439,8.882827,8.010474,8.099035,2.695134],[5.944707,-0.228596,7.310749,-1.870897,4.844578,-7.169945],[-7.179809,8.364885,8.779768,5.295149,-1.254742,-8.019638],[-7.597670,-2.485036,3.330464,-9.595392,-0.699306,-2.573071],[0.955768,-1.386101,9.530123,-2.261819,8.495230,0.734238],[-2.118432,-7.005966,7.544215,9.648863,-6.585774,7.612749],[1.276966,-8.400868,-5.031020,6.114776,-1.979659,-6.734529],[8.706591,6.782296,-5.810897,8.387950,9.707945,1.366517],[-9.667887,1.470733,-2.357228,-5.966589,-9.983720,-9.373010],[-2.192526,-7.843407,5.585462,-1.977930,-8.662068,4.052781]],[[-9.977536,5.136463,-2.842787,0.203796,1.825296,7.947444],[2.837152,-1.335839,-1.860279,4.360934,-0.335652,0.108951],[-9.921011,-0.346905,-3.113351,-7.408504,-9.880538,-7.845110],[-8.544562,-2.169272,-9.943627,-3.397719,6.021605,-1.553760],[0.809535,-5.979969,8.447208,8.700443,8.308758,-6.635336],[6.338502,0.431496,6.237703,-5.287442,9.655904,4.834052],[-5.606996,0.502803,-0.447069,5.598250,6.432802,-9.864976],[-9.138361,8.555906,0.594238,1.339578,-2.302386,0.681506],[-3.862445,1.152942,-7.192866,-0.823826,-9.792295,-8.062922],[7.392946,-0.625937,-8.889315,5.612292,-2.273556,-1.136788],[7.633993,-7.152487,-3.828707,2.859560,9.264379,-4.439251],[3.773572,-2.438870,9.075503,5.982041,4.127260,7.955462],[-5.294820,-5.125994,1.932609,-1.242013,-0.488799,-9.415353],[-9.011491,7.164663,1.514105,6.121643,-1.204387,-2.919511],[7.133776,-1.950974,-8.044417,-1.128782,6.069850,1.264841],[8.368483,3.614244,5.312189,5.537370,4.905023,5.172235]]], dtype = "float32")#candidate|4453|(9, 16, 6)|const|float32
bop_4454 = relay.minimum(const_4452.astype('float32'), const_4453.astype('float32')) # shape=(9, 16, 6)
output = relay.Tuple([bop_4454,])
output2 = relay.Tuple([bop_4454,])
func_4460 = relay.Function([], output)
mod['func_4460'] = func_4460
mod = relay.transform.InferType()(mod)
output = func_4460()
func_4461 = relay.Function([], output)
mutated_mod['func_4461'] = func_4461
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4462 = relay.var("var_4462", dtype = "int16", shape = (6, 9, 4))#candidate|4462|(6, 9, 4)|var|int16
const_4463 = relay.const([[[-10,9,-8,-5],[8,1,6,-9],[8,-7,-2,3],[2,2,6,-5],[6,-10,-3,-9],[-6,6,-10,5],[2,-10,9,-2],[7,-8,1,-1],[-5,9,-8,1]],[[-3,-6,-4,9],[-4,-2,2,-4],[7,4,-3,-5],[6,8,-4,-7],[-6,10,-3,7],[9,10,3,-10],[6,-8,-7,-9],[7,-8,-6,10],[8,-1,-10,-8]],[[-8,-10,-2,9],[4,-7,10,-5],[-5,8,10,3],[-1,-8,-5,-9],[7,-3,-10,7],[2,7,1,-9],[-5,-6,-6,-4],[7,7,10,-6],[7,-6,-4,3]],[[8,-7,1,3],[-2,2,10,-6],[-8,1,-1,7],[-6,7,7,-5],[-7,1,-8,-6],[5,-2,-2,4],[-3,9,1,4],[-8,-7,-10,-9],[-7,-6,7,7]],[[10,9,-10,-1],[1,1,-6,1],[-5,-9,3,1],[-8,-6,9,-9],[5,-10,-4,-1],[2,6,4,-2],[-6,-3,8,-8],[1,3,9,8],[9,-10,8,7]],[[3,8,9,-8],[10,3,-5,4],[4,5,-7,-7],[10,1,-1,8],[10,-1,5,-3],[1,10,-6,2],[-10,-3,-2,5],[-10,-8,7,-2],[1,5,3,8]]], dtype = "int16")#candidate|4463|(6, 9, 4)|const|int16
bop_4464 = relay.right_shift(var_4462.astype('int16'), relay.reshape(const_4463.astype('int16'), relay.shape_of(var_4462))) # shape=(6, 9, 4)
uop_4469 = relay.asinh(const_4463.astype('float64')) # shape=(6, 9, 4)
output = relay.Tuple([bop_4464,uop_4469,])
output2 = relay.Tuple([bop_4464,uop_4469,])
func_4473 = relay.Function([var_4462,], output)
mod['func_4473'] = func_4473
mod = relay.transform.InferType()(mod)
mutated_mod['func_4473'] = func_4473
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4474 = relay.var("var_4474", dtype = "int16", shape = (6, 9, 4))#candidate|4474|(6, 9, 4)|var|int16
func_4473_call = mutated_mod.get_global_var('func_4473')
call_4475 = func_4473_call(var_4474)
output = call_4475
func_4476 = relay.Function([var_4474], output)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_4521 = relay.TupleGetItem(func_4460_call(), 0)
call_4522 = relay.TupleGetItem(func_4461_call(), 0)
const_4525 = relay.const([[[-0.232054,-3.910990,-5.251264,-9.980254,-4.236798,1.090127],[8.838497,-0.489957,-2.479890,-0.358023,-4.174597,-1.089981],[6.267338,3.342250,-0.334304,-7.910796,0.818891,-4.292351],[-6.341580,6.406927,3.822977,8.405292,6.617019,-8.029674],[9.679619,5.555906,7.206676,-3.326116,3.614735,-3.278301],[3.337241,7.524092,6.747784,-3.618398,-8.027231,-6.285389],[-0.399564,-2.904962,5.813368,8.774649,1.473405,8.841701],[8.293341,2.751362,4.060280,-2.457722,0.213365,6.481036],[7.981393,-7.902669,-5.478516,3.594049,-0.507840,-6.248081],[-6.763985,-7.061779,2.659005,5.002458,-6.017945,8.419760],[-4.437131,-8.624803,4.722911,-2.817297,7.289436,-4.884702],[-4.388793,-3.496288,-8.776410,-9.629178,-9.285657,-0.709671],[-5.543324,-1.172019,1.340012,8.464657,4.129473,4.752460],[6.118453,8.916915,-8.862762,-7.366769,3.994217,-2.405583],[-5.827127,1.065180,2.876824,-5.094229,3.466123,-2.179762],[-5.617851,-9.874306,6.987188,1.975097,5.811341,8.004011]],[[-7.949721,-2.330307,-1.380459,3.757045,-4.198980,-9.492238],[5.759095,2.957018,9.065422,8.670133,4.496102,-1.426673],[2.926407,-9.156647,-6.688790,-9.635056,3.554688,2.137417],[9.604083,-3.773327,8.707549,-0.199917,6.306662,0.255163],[7.883451,4.361153,-8.288974,-1.081183,2.963590,-8.712098],[-5.122284,-7.305418,-5.351518,-0.303233,6.256829,5.534296],[6.776226,3.661759,1.321904,4.162164,1.597455,-1.917833],[-7.589394,8.769470,8.662982,-5.932444,-5.903763,0.498591],[-7.945958,8.647363,4.624937,-3.462248,-4.788442,5.943535],[-8.976969,-4.008639,2.779675,7.624231,0.425651,4.123124],[-9.376581,4.359250,3.449614,7.977958,-3.674398,0.778874],[7.376100,-9.147552,0.715891,-6.483677,-8.942326,8.899153],[7.744141,-9.542365,1.828273,7.777219,1.949821,-9.523224],[1.828057,-2.908981,-7.255087,1.530966,7.251764,7.454721],[-2.011132,-9.437833,5.628778,-1.009392,-0.013795,6.301766],[3.342365,3.121525,4.557340,6.230390,-8.753627,-2.686648]],[[3.332945,-6.657961,3.596835,2.332053,7.678429,8.534994],[1.065182,2.742517,-8.001384,9.234657,1.449195,-5.644287],[-3.294112,-0.783574,1.002017,-0.691740,-4.960035,4.269389],[-9.276706,1.859122,-7.014714,-8.245288,2.313537,0.476547],[4.193202,7.433923,4.432984,7.604834,7.266730,-6.991445],[5.202369,7.068721,-9.317345,5.386165,5.163153,-1.768217],[1.385707,6.750998,2.336498,-5.956228,2.472668,8.861180],[4.979320,-4.822426,-3.574816,1.700386,2.004613,-6.349854],[9.225695,7.461407,-2.668854,-9.313267,-8.414342,-3.352617],[-4.450091,-6.139995,-7.656436,8.569893,8.545464,-5.952020],[-9.333529,4.997956,-9.284942,7.225936,2.426065,-0.573197],[7.613535,-5.699883,-3.161345,9.280103,3.134703,-9.145492],[7.819484,-8.252648,-1.993679,4.733402,-2.955505,-7.103261],[-1.723220,4.831481,-5.004123,3.897498,-7.653491,-4.095020],[2.990223,-9.270260,2.991842,-7.997004,-6.123130,3.046814],[-7.460287,8.606519,2.174559,2.563778,-3.833743,-0.259564]],[[2.761140,-7.033852,8.425359,-0.760561,-4.425190,4.332325],[-0.824877,-3.734682,-1.604400,1.557847,-5.814494,-4.443039],[-5.849934,7.394356,-5.837411,-8.595381,-4.421564,9.951440],[2.341720,-0.108821,-9.745828,5.136562,6.344978,6.880112],[-3.178194,-1.329305,-1.984682,-6.277627,2.264444,6.257918],[1.232720,4.107137,-5.728718,3.732550,-4.858107,8.200598],[-5.961192,2.687140,-1.778016,0.878472,6.202372,-6.722576],[-1.557398,1.413819,-8.199747,1.276101,-8.177665,1.463653],[-5.309635,-7.595088,-7.110309,6.556644,-6.878587,7.485294],[-6.035874,7.623942,-4.818217,0.351052,5.856923,-8.893804],[0.332161,6.737518,-8.749861,-5.252564,-6.858915,-1.252434],[-7.362089,3.418753,-5.605672,2.505113,6.426414,0.881658],[-3.382326,0.402278,9.232211,-6.288666,7.818579,-3.218799],[-0.696163,-8.288429,1.805838,-9.018159,8.978878,-0.340293],[-5.351056,-8.668977,3.374713,0.310578,-9.923301,7.645141],[5.126625,-2.471785,1.984939,-5.150967,8.034649,-5.157442]],[[9.016884,-0.544388,-8.252401,0.389840,-8.146526,9.594026],[9.726992,-4.280262,3.919820,1.165183,6.341744,8.782734],[-3.439331,-8.437427,2.595102,-4.130981,0.794230,6.730498],[2.377501,-5.383256,-8.879300,5.771731,3.704579,4.862833],[2.254639,2.335944,-0.941652,-4.765504,-5.162606,-6.123796],[0.007979,3.591592,8.224377,3.299930,4.851521,-1.770724],[6.851877,0.650682,1.659467,1.010347,3.116174,9.959212],[9.172770,-0.998259,5.851996,4.573043,8.893755,9.224890],[8.435240,9.313405,9.533051,-1.271974,-2.741140,7.613732],[-7.039050,-4.244271,5.804966,0.801021,2.168223,-6.447582],[-0.949684,-9.163903,-5.210483,-7.416844,-8.690196,-0.519883],[-9.526536,-5.320828,-9.522987,-8.196424,-9.542990,-6.470152],[7.103391,-9.705646,1.944652,5.447818,1.216545,0.259267],[6.721220,0.425794,-9.240083,0.212737,9.080911,7.965109],[1.402481,-1.693167,-7.931374,7.754896,8.080386,5.557409],[6.911482,-4.522509,-4.955960,-1.153925,-7.159937,2.777936]],[[-3.614465,3.526912,-4.059512,5.806426,-7.703542,1.416201],[4.321679,-2.202518,-1.089765,4.897504,-4.055243,-6.193085],[-3.903490,3.962041,6.642334,0.183016,0.808253,9.207191],[9.164053,-3.537752,-6.966245,-6.106504,-5.566989,-5.080787],[-3.379255,-9.553587,-7.961353,4.601092,-3.122742,4.715192],[9.297868,2.060815,6.838783,-2.160258,9.440680,-6.453096],[-5.491031,7.090250,-1.858685,-6.652766,-9.455432,9.985505],[7.658428,3.924991,9.970318,5.384491,9.641563,-6.243127],[2.209448,8.454741,6.493184,9.644708,-8.919311,-8.735823],[-8.803103,-2.512137,-0.115819,5.521617,-9.521513,4.942801],[9.697765,6.598969,6.340623,1.617148,-1.328324,2.026097],[5.561439,-0.161303,-8.959563,-2.846360,7.527652,5.457301],[-8.701726,8.347580,2.826874,4.331312,-5.077191,9.920890],[-1.074377,-0.317308,6.282192,-8.884541,-6.820795,-9.847238],[4.473588,-2.056615,8.321724,-7.512418,-6.702177,2.481386],[-5.285005,6.415341,5.874082,-6.651512,0.064991,-8.304644]],[[9.619974,3.728347,7.312918,-4.570371,-5.568832,0.327118],[-3.872581,-8.712457,-0.544129,-3.069816,-5.266861,5.869158],[-8.665378,9.776975,-3.066853,-6.610835,-9.522251,-7.268239],[2.727634,-8.339288,4.527536,-6.704150,-1.611252,-4.398533],[-9.902319,5.667989,-6.786500,-0.550278,4.702297,7.237149],[7.136413,3.817235,8.942328,-2.280673,-5.216224,8.003923],[-2.139535,8.314108,-5.824630,1.859421,-3.042185,0.401152],[3.386367,0.121651,8.039372,7.571701,-3.782336,-6.751487],[-6.722057,-6.913014,7.722886,-6.593549,6.420392,-6.053032],[4.661045,-4.831629,9.432247,6.118781,9.245638,9.810402],[5.871553,-4.253029,3.928296,8.835147,1.047313,-3.607521],[9.825081,-3.828660,-8.677185,-0.087725,9.197305,2.284633],[-9.962581,1.744012,2.915665,-3.290047,7.248286,-2.919384],[2.145661,-8.626399,3.996760,-5.844971,6.633911,-5.105916],[6.064277,-4.621830,8.186877,3.066614,-6.543634,-8.066582],[2.530139,-0.130162,9.817523,3.678340,-8.559916,9.249699]],[[-6.071851,4.565588,-8.583234,6.957529,-8.044307,-1.156126],[9.118502,-3.997183,8.591221,1.821522,5.241891,6.027513],[-7.770699,-8.918733,4.529583,4.454264,0.592516,0.644240],[-1.712042,0.539110,-6.637747,-7.416353,-5.726309,3.475649],[6.722688,-4.180462,-6.636836,4.938402,5.796246,-3.492120],[2.734326,-1.899607,-2.005246,8.603699,8.651426,9.800580],[-1.602780,8.715043,-2.781172,-5.854202,-0.474282,1.467088],[1.341328,7.604212,-9.473116,3.955606,6.306351,-6.608766],[9.850689,-8.302349,-3.562787,3.962019,-6.841629,8.375638],[9.923182,-1.899842,7.154505,7.477334,6.285434,5.905047],[-1.003939,0.780872,-3.078562,0.093863,5.681334,-4.626152],[6.985162,0.895362,0.635250,3.436162,-6.855965,-6.605469],[6.680799,-3.330105,-1.440499,-1.040270,-2.913903,9.356287],[1.797427,7.839826,-6.272344,-4.646856,8.874537,1.452897],[2.492644,0.833160,9.293479,0.485158,9.148526,5.623268],[7.254101,-3.692955,0.396753,-7.962364,-9.401611,-3.900356]],[[-8.844869,8.194903,-0.044225,-7.824817,0.428384,5.332278],[6.410266,8.215095,1.856236,-0.021636,-5.223122,-2.828967],[-7.352569,-4.145655,-3.212906,-6.582504,7.657541,-0.563907],[-1.524396,6.687793,9.905081,-2.506516,4.465307,2.284100],[-9.750480,7.895242,3.822353,3.559892,9.892295,-7.170197],[-7.374039,-1.306401,-9.856158,8.967163,6.049559,-5.256171],[0.695446,1.054293,-2.667638,5.031929,-9.000373,6.577894],[5.879150,-8.484809,-1.348605,-5.084318,8.070073,0.165091],[-8.509310,-2.937661,4.113646,-5.873130,-4.581369,-7.377104],[-2.857690,2.685388,-5.438421,-6.346664,5.373874,-6.653119],[-0.019220,-3.287106,1.469658,0.353477,-2.882516,0.030846],[2.139785,7.895948,4.013490,-8.096568,8.207445,4.246106],[8.723599,2.292900,-9.120605,-4.347703,5.964564,-1.389765],[-9.698402,-3.805340,8.252567,4.378439,1.352180,-3.058015],[-8.420466,-0.903077,3.539997,3.813482,-6.503092,0.236118],[9.240008,1.001586,7.625569,2.342269,8.428612,-5.321193]]], dtype = "float32")#candidate|4525|(9, 16, 6)|const|float32
bop_4526 = relay.left_shift(call_4521.astype('uint32'), relay.reshape(const_4525.astype('uint32'), relay.shape_of(call_4521))) # shape=(9, 16, 6)
bop_4529 = relay.left_shift(call_4522.astype('uint32'), relay.reshape(const_4525.astype('uint32'), relay.shape_of(call_4522))) # shape=(9, 16, 6)
output = relay.Tuple([bop_4526,])
output2 = relay.Tuple([bop_4529,])
func_4537 = relay.Function([], output)
mod['func_4537'] = func_4537
mod = relay.transform.InferType()(mod)
output = func_4537()
func_4538 = relay.Function([], output)
mutated_mod['func_4538'] = func_4538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_4544 = relay.TupleGetItem(func_4460_call(), 0)
call_4545 = relay.TupleGetItem(func_4461_call(), 0)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_4548 = relay.TupleGetItem(func_4460_call(), 0)
call_4549 = relay.TupleGetItem(func_4461_call(), 0)
func_3502_call = mod.get_global_var('func_3502')
func_3506_call = mutated_mod.get_global_var('func_3506')
const_4557 = relay.const([[-9],[-2],[-8],[7],[7],[7],[-2],[-7],[9],[-1],[-5],[-4],[-10],[1],[-9],[8],[7],[2],[-7],[1],[-2],[3],[-1],[-1],[6],[-3],[-2],[-9],[-3],[2],[-9],[-1],[-8],[-2],[-9],[1],[1],[-9],[6],[-5],[1],[5],[-6],[-10],[5],[5],[10],[-2],[7],[5],[9],[1],[-10],[6],[-10],[8],[10],[9],[-8],[-7],[10],[-8],[-7],[1],[8],[-2],[-2],[9],[-3],[7],[6],[9],[9],[-2],[-6],[1],[-2],[-4],[-3],[1],[-1],[-6],[-7],[-4],[-8],[6],[-4],[-9],[-2],[1],[1],[-1],[5],[2],[-10],[-7],[7],[5],[-8],[4],[8],[1],[-4],[7],[5],[-1],[-4],[-9],[-10],[4],[5],[3],[5],[-8],[5],[-3],[2],[6],[-8],[4],[-3],[-10],[-7],[-3],[-2],[-9],[8],[-1],[-9],[10],[-10],[6],[-8],[-2],[5],[8],[10],[2],[-8],[6],[-4],[7],[4],[9],[-6],[7],[3],[-10],[6],[-7],[-5],[-9],[-4],[-2],[-8],[2],[-1],[3],[6],[1],[10],[-8],[1],[-4],[-9],[2],[-8],[8],[-3],[-6],[-1],[2],[7],[9],[9],[5],[-8],[-4],[2],[-10],[1],[-6],[-10],[-2],[-7],[6],[7],[9],[-5],[-9],[-8],[4],[9],[7],[-6],[-2],[-6],[5],[-3],[10],[9],[9],[4],[-2],[-8],[-1],[-5],[-4],[-5],[-6],[7],[-7],[6],[-10],[-2],[2],[-6],[7],[-9],[-7],[10],[-3],[5],[9],[-8],[10],[-3],[-8],[-10],[10],[9],[-3],[-3],[5],[1],[-8],[1],[6],[-9],[-7],[-10],[-2],[-5],[-1],[-9],[1],[5],[2],[-6],[1],[-8],[6],[10],[-7],[-7],[-8],[3],[-9],[4],[-5],[5],[10],[-2],[9],[9],[3],[8],[-7],[1],[9],[-10],[4],[-1],[-2],[-5],[8],[5],[-9],[2],[2],[7],[-9],[7],[5],[-1],[8],[3],[5],[-7],[9],[-5],[1],[6],[-6],[-7],[10],[-6],[-8],[6],[-2],[8],[-8],[-6],[-7],[9],[-6],[-6],[4],[-6],[-2],[1],[-8],[2],[1],[-1],[-5],[-7],[-4],[-8],[-5],[-8],[1],[9],[-7],[6],[-9],[-1],[5],[4],[1],[10],[-8],[3],[-7],[2],[7],[-4],[-5],[-4],[7],[2],[-8],[-4],[-6],[8],[8],[5],[3],[6],[8],[4],[8],[-6],[1],[5],[-1],[-8],[10],[9],[-2],[5],[-4],[-4],[8],[-9],[-7],[-2],[2],[-10],[-9],[3],[-4],[8],[-4],[-1],[-3],[-6],[5],[-4],[-1],[-9],[-5],[-5],[-10],[-10],[-4],[8],[5],[-1],[2],[-5],[8],[-4],[3],[-8],[-10],[-3],[10],[3],[-7],[-9],[-7],[8],[-3],[-3],[2],[-4],[9],[-3],[-5],[-7],[10],[1],[1],[9],[7],[8],[7],[8],[-4],[-6],[8],[7],[7],[10],[-3],[-8],[-8],[-2],[-3],[7],[-9],[5],[-3],[-7],[-3],[3],[5],[1],[-2],[-4],[9],[-9],[-1],[5],[1],[5],[1],[7],[5],[10],[9],[9],[5],[-7],[-10],[-3],[5],[5],[-10],[1],[6],[-3],[-7],[8],[-4],[-10],[-4],[-8],[1],[-6],[-6],[-10],[-1],[-6],[-9],[4],[4],[2],[-8],[3],[-1],[-7],[-2],[-3],[-10],[-3],[-10],[-7],[2],[-3],[2],[-6],[-5],[-8],[-1],[4],[-4],[6],[-8],[8],[-10],[4],[8],[2],[-5],[-10],[-4],[-5],[-7],[3],[4],[9],[-10],[5],[-5],[-4],[5],[-4],[9],[2],[-5],[-5],[1],[10],[-3],[-7],[2],[-4],[-2],[-8],[3],[10],[2],[-1],[-2],[-9],[5],[5],[-3],[5],[10],[2],[9],[-4],[-6],[-8],[6],[5],[3],[-3],[8],[3],[-7],[1],[-5],[-6],[10],[7],[-4],[10],[5],[9],[5],[-1],[1],[-5],[-9],[4],[7],[8],[6],[9],[1],[-7],[8],[7],[5],[-5],[1],[1],[4],[-10],[-4],[-9],[-4],[7],[10],[-5],[-5],[-10],[-10],[-6],[-4],[-7],[1],[-4],[6],[7],[2],[5],[4],[3],[-9],[7],[-1],[-6],[-3],[-7],[-5],[9],[-4],[10],[10],[-2],[-5],[8],[10],[-3],[2],[-2],[6],[-5],[10],[5],[8],[-3],[10],[-4],[3],[3],[-4],[9],[-4],[2],[4],[-10],[-2],[1],[-9],[-9],[-2],[-9],[6],[-3],[9],[8],[6],[-9],[10],[8],[-5],[-6],[5],[1],[6],[1],[10],[10],[-3],[-4],[-10],[-8],[-10],[9],[-10],[3],[7],[-4],[-7],[-8],[-5],[-10],[-1],[1],[-5],[10],[9],[-2],[-7],[-8],[7],[-2],[-1],[9],[-1],[2],[8],[-1],[4],[4],[-8],[5],[-4],[-6],[-7],[6],[6],[-2],[-6],[8],[8],[3],[3],[6],[5],[9],[6],[-1],[-2],[-1],[-1],[-6],[-7],[-5],[-7],[-10],[4],[4],[5],[-7],[2],[6],[-1],[-10],[5],[-3],[-10],[-5],[-7],[-10],[5],[1],[1],[-7],[5],[-1],[-9],[9],[-5],[4],[-2],[-8],[5],[-9],[-8],[-9],[9],[2],[-7],[-10],[-2],[-1],[9],[2],[9],[-6],[2],[3],[-1],[-2],[-3],[2],[10],[4],[5],[-10],[-9],[8],[3],[2],[6],[4],[5],[-7],[-2],[-3],[-9],[7],[-1],[7],[-8],[-2],[9],[3],[-2],[3],[6],[-9],[-5],[-7],[-7],[-9],[7],[6],[-10],[-3],[1],[3],[7],[-10],[-4],[10],[10],[-1],[6],[-1],[-8],[9],[-8],[-5],[-9],[5],[6],[-10],[8],[4],[4],[-2],[-3],[-9],[-10],[-2],[-3],[-8],[-10],[-9],[1],[-1],[-4],[2],[10],[3],[-9],[-8],[9],[1],[-10],[-10],[8],[3],[-10],[8],[-6],[10],[1],[-1],[-7],[-5],[-9],[-9],[2],[10],[7],[-6],[7],[-4],[2],[10],[-3],[8],[-10],[5],[3],[-6],[-4],[-3],[-6],[-10],[-2],[-9],[-4],[7],[7],[3],[-6],[3],[10],[-5],[-9],[9],[5],[10],[4],[6],[4],[8],[10],[-5],[-3],[-6],[9],[-6],[9],[-6],[-4],[10],[7],[-3],[-9],[9],[-4],[-5],[-2],[-1],[1],[5],[9],[1],[-7],[-4],[1],[8],[-5],[-1],[10],[2],[-8],[-10],[7],[7],[-3],[8],[-6],[-9],[5],[3],[9],[-4],[-4],[1],[-4],[10],[9],[-2],[5],[4],[2],[9],[-2],[-2],[-2],[-3],[-6],[-7],[3],[-4],[2],[10],[-6],[-10],[4],[7],[8],[5],[-4],[7],[3],[9],[10],[-10],[8],[1],[-10],[1],[-3],[-6],[-5],[-4],[-1],[-2],[-7],[-1],[10],[10],[7],[-10],[-7],[-7],[2],[-2],[-9],[4],[1],[8],[7],[7],[9],[-4],[7],[9],[-7],[-1],[2],[9],[5],[10],[10],[-1],[-4],[-3],[9],[6],[-7],[8],[-6],[9],[8]], dtype = "int8")#candidate|4557|(1008, 1)|const|int8
call_4556 = func_3502_call(relay.reshape(const_4557.astype('int8'), [14, 9, 8]), relay.reshape(const_4557.astype('int8'), [14, 9, 8]), )
call_4558 = func_3502_call(relay.reshape(const_4557.astype('int8'), [14, 9, 8]), relay.reshape(const_4557.astype('int8'), [14, 9, 8]), )
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
const_4561 = relay.const([7.470879,7.128844,-8.828454,-6.395830,2.259230,9.331860,-9.056093,6.950264,-2.469507,-3.327506,2.088141,9.035822,-9.607396,1.508897,8.118572,7.034425,2.531705,6.044213,-3.990945,-1.039124,-0.968479,-2.739637,-8.574912,7.966210,-7.257949,0.693263,6.525479,-5.669738,1.809501,8.789738,-0.715810,7.602882,3.711526,6.551808,-2.950806,9.991440,5.063775,-4.251731,7.523091,-5.282799,5.783219,0.008391,8.899236,-2.582515,0.487154,6.239423,8.123218,-3.114178,8.662141,-3.543263,9.247327,-5.739160,-6.858618,-9.255978,-2.092451,9.262995,3.710579,-3.183327,-1.369669,6.369314,7.147713,3.271209,3.409459,2.357966,4.585718,-4.133428,-2.222340,0.834277,3.210728,-2.380067,0.293088,-5.228017,5.306783,4.742069,5.562599,0.719247,8.170927,5.614258,-1.391029,9.516527,4.127968,-5.597963,-7.258630,-4.475026,-6.598599,6.080717,-2.725786,-9.456868,9.925858,-5.575975,-5.996269,8.160835,-4.914035,-6.290434,4.758556,5.786994,7.799584,-9.815546,1.987827,-7.259935,-6.409422,1.301192,6.215734,-8.186457,2.066967,3.696966,-8.844742,6.012487,-2.663870,-9.459972,8.052520,-9.869288,3.105384,-4.837833,4.240466,-7.820067,6.744164,-4.148952,8.413625,2.630119,1.534194,-6.325556,9.010360,6.124077,3.397405,9.568804,7.002432,-6.943075,1.504413,7.502568,8.385678,-6.281498,-1.377546,0.009081,5.393244,-9.809144,1.285827,-6.221578,2.711915,-6.295020,9.087637,3.726273,6.283207,-6.797545,8.197689,1.220430,9.446371,6.691753,8.401950,-3.597737,3.512499,8.745231,7.112895,5.706149,0.366136,-8.311870,8.269240,3.514230,1.727700,8.038956,-1.212729,5.420697,-8.917462,7.583804,0.735425,-7.067825,-4.461545,7.162685,-3.267279,-2.485402,3.116289,-8.105921,2.612353,8.340500,5.472197,3.139742,-0.307362,-4.525238,6.934460,-5.650010,7.382299,0.197316,-9.334550,9.062556,8.378318,7.821581,-0.388501,2.130537,7.881197,-4.443576,-4.579456,-7.414967,-6.960752,4.029948,-4.749632,-2.116035,6.140678,-8.575424,8.437452,-9.307596,5.917491,7.928212,9.987030,0.114026,5.564935,-6.677825,4.451296,-0.849495,9.758082,0.845499,1.056953,4.339097,1.094030,9.523153,3.457821,0.985542,5.592443,8.662439,-0.983510,8.421617,-6.963109,1.270822,0.692820,-2.163672,9.497026,-5.918040,5.233356,1.015413,7.035482,6.273205,-8.410400,-0.940644,4.602637,0.204451,-5.666993,-9.179573,-5.761225,0.487242,5.127489,-7.037784,8.650244,-5.884703,-0.089578,-1.322167,-5.106839,-3.744158,-7.510863,-1.808699,-1.611308,3.180830,-9.710297,-9.780621,9.962696,-9.965738,0.223934,-7.149705,-4.166893,8.514414,-4.989664,-1.058540,-6.931725,-5.808673,4.806797,-0.099011,-5.873739,9.080183,5.241163,5.366468,8.141995,-1.676502,-1.633642,7.293615,5.687095,4.476172,-6.199063,-4.053628,-1.281393,-0.410875,3.342138,-1.699640,-8.021449,-1.973020,7.938634,4.773751,-4.324755,2.643289,-2.403065,2.517204,8.369389,8.656563,-4.175881,-8.092656,-7.018627,8.622101,-4.297593,5.676939,8.788989,-1.037767,4.177879,3.759412,4.919398,-2.425578,5.604720,8.800161,-4.990808,7.934108,-5.192508,-5.620699,-8.566598,-5.496198,8.929123,5.112723,-0.846356,2.983312,1.817231,4.719782,4.239780,-0.503499,8.195361,0.753171,9.419070,-6.408691,7.610640,-7.695508,-3.918649,-4.479236,5.716253,-5.824373,1.924711,7.443012,-8.912205,-4.272350,7.490307,9.254126,-4.843452,-6.670762,3.325699,-6.816934,1.212730,-5.667004,4.795143,8.416731,-2.843077,-9.875247,4.544287,2.807946,-7.312760,3.229735,-9.614461,-8.433121,-5.847997,-9.332656,-0.613917,-9.482561,-9.663220,1.369887,3.126891,-3.334131,1.063746,8.296241,-2.520184,-1.167799,-0.939611,-5.067709,-0.478639,-7.447991,-0.823219,-6.540400,2.581726,-4.620660,3.207611,3.073380,7.150863,4.254371,7.422158,3.088791,5.886246,-4.262554,-5.960861,-4.822543,-8.384812,0.234457,-0.155243,9.044783,-3.127564,6.361078,2.626172,-1.095758,-1.203610,7.108695,-3.265627,3.978040,6.141776,-1.907171,1.570442,-9.885442,7.400237,-9.659900,-3.570387,4.456759,7.667134,-1.947829,1.853015,9.997483,-7.459282,8.617060,-9.971303,-3.775972,8.168140,2.738222,-7.460862,-2.915065,9.650649,7.988559,-8.826700,-6.558671,6.460076,-1.857307,0.404924,-8.809919,3.521105,-5.767083,-6.491845,9.671231,3.196372,-2.691146,-1.115605,4.619213,1.901715,5.652275,3.096843,-2.162683,4.645828,-9.183278,-5.698951,-1.600809,-4.164615,9.673848,-9.859837,-3.206520,5.850000,0.477082,7.457764,8.604196,4.991094,-9.692904,-4.629535,6.005226,-9.448637,-5.735888,-6.992057,-8.858167,-3.792580,7.069486,-9.132522,-1.017040,0.934364,0.127530,3.223743,4.768578,-0.218666,3.888184,-0.401054,-8.850621,-1.704312,-5.470006,7.798848,-9.376005,-1.928889,-7.182258,5.133842,7.743325,-0.862017,-7.089577,6.019106,-8.503486,2.847383,5.990210,-4.610930,-3.455473,-5.941279,9.232101,9.299059,5.346168,-0.879012,-9.177040,2.249261,-2.512061,4.845060,1.180648,-1.616221,-4.312399,5.195409,-9.918696,3.900246,9.272187,6.611125,3.082010,-2.051366,-8.340097,0.709387,-8.527077,-3.771344,-9.132657,8.103238,1.505099,-5.489632,-2.755778,6.471215,2.179707,3.643990,-9.953724,-0.214441,-0.678800,2.276253,8.120204,5.511065,1.017833,-0.193723,6.345595,5.213267,0.905875,-9.638470,3.672765,-8.547087,-1.946968,9.846771,-7.797261,5.428783,-8.534127,-0.661076,7.004470,-0.020662,0.057979,-0.888813,-1.618683,3.254478,1.344214,5.133721,7.059480,-1.293169,-8.088426,5.766145,0.848367,9.757118,9.999151,7.119641,2.746493,7.036103,-4.423664,-6.317371,9.454988,-1.427573,4.618050,6.045559,-3.495328,4.424469,-5.105577,7.266891,7.890227,3.010315,-9.810917,2.307571,-1.731329,2.087035,-5.952715,-0.720320,8.022176,1.926771,-3.247581,-5.347190,-4.259674,3.030833,-3.633534,-1.933886,7.759960,-8.164748,-4.482057,-3.522628,-5.060309,1.397609,9.831701,-1.312630,-2.023467,2.921147,-5.113067,7.230216,1.046220,0.498174,-8.228003,7.866479,-7.827580,1.248272,0.831746,7.303840,5.274844,0.765940,-6.957067,-5.431657,6.599773,-1.421984,5.104400,-4.575798,-7.064662,-8.097525,6.263747,8.950933,0.900662,-4.423520,-4.475069,-6.113412,-4.691111,-6.049371,2.040845,0.267103,-0.897057,-9.333144,-8.768075,3.758806,4.786292,2.250478,0.702530,-9.592800,9.923646,-9.002012,-2.106169,-9.074947,-2.075408,-2.732575,8.067628,-9.031821,1.011414,9.394302,8.903408,-5.461572,-8.986274,4.678960,-0.655996,-6.237847,-5.864747,3.456517,3.896345,9.537983,-5.243746,8.378516,3.319581,-3.657350,-9.400663,-3.115282,-1.793786,-7.905544,-4.149236,-8.435927,3.994559,5.192379,5.515225,8.677826,-6.616476,-4.363327,-5.009480,-7.095026,5.567690,-6.924539,-0.732452,9.253926,1.487894,6.369190,6.422500,4.471357,-1.346634,-0.309399,2.699118,-0.828531,-2.992884,5.973322,-6.760327,7.733857,-2.766522,7.307147,-2.691242,7.563102,4.646991,-8.998222,-5.058222,6.504629,-8.261722,8.092951,3.224423,3.111757,-1.240597,-0.319453,-6.540836,8.468906,9.025782,8.376098,1.698895,-6.008350,9.663660,-6.234923,-3.612290,-0.528432,8.211306,-8.420565,0.657947,1.604065,-5.320228,-3.060063,7.318238,6.902931,-7.241521,-8.247203,6.517345,-9.758004,8.148801,3.131817,6.841149,-4.736226,2.585610,3.798771,-3.393351,-1.671515,1.057193,0.287367,-0.750747,3.653333,8.402420,7.203840,-0.056684,2.660192,-3.580259,1.515226,-6.289840,-8.711599,8.384975,-2.807438,-0.163476,-6.872146,6.074313,-0.644486,4.210109,4.175035,-2.036284,2.701089,-9.539895,-9.238113,9.610412,-8.941296,-1.244182,3.982272,4.449470,7.850032,1.488885,8.114192,-8.012999,-2.914616,3.719458,-8.650262,-7.296886,2.371584,8.856243,3.667617,8.474817,-7.592138,2.207501,8.096853,-4.052994,-6.586001,5.816720,-4.347674,-4.072841,4.602639,-8.755549,2.449732,8.127268,-8.683053,-9.978005,-6.379329,1.630785,1.014323,-0.209651,2.722916,-4.708637,-9.059757,6.717004,4.819177,-9.296230,-1.401865,-3.522472,7.010263,-6.268059,-2.445510,-4.912955,-0.476051,-3.702329,-5.151521,0.377794,7.361285,5.063101,3.149452,-2.555062,-3.111142,2.234091,-5.134733,-1.252068,6.480092,2.710612,-2.122045,-9.767222,4.242231,-2.413915,-3.909978,-6.871402,3.658163,3.747307,-7.733352,6.625794,-3.036545,7.889116,8.732977,4.230864,-6.625131,-0.469377,-6.650439,-0.977312,8.890369,5.783740,-7.166737,6.612799,1.613920,-6.977694,1.993392,0.669684,-7.749868,-0.961896,-3.423196,-2.243614,-6.402005,5.361279,-3.061976,-9.687430,7.428340,7.197205,4.162326,3.815224,7.080505,3.000859,-9.642717,5.179278,0.629933,-6.007013,0.832658,1.741311,2.223248,-1.920942,-1.736723,-4.401878,-4.919751,1.870063,-0.773546,-5.979812,-5.411001,-8.757376,-7.811757,3.203564,7.016583,-7.097890,-0.944545,-6.171248,-0.670956,9.200397,-4.899918,-1.811432,5.253310,-8.052428,9.868285,-0.826174,-4.344571,-8.907186,-1.639530,3.312606,7.236708,-7.441473,1.007609,9.860543,1.904720,-0.104311,-0.714130,-2.412166,-8.822938,-5.617244,6.274027,8.214437,0.048550,9.112216,1.269008,-5.879379,-0.335833,-1.545452,2.054411,0.490453,1.687227,-0.811312,3.044998,3.976061,-9.553995,4.033536,-0.648008,4.960274,-2.157642,1.098315,2.263618,-9.864716,-8.613532,0.219082,-8.708586,-3.946815,-1.144991,-6.163569,4.934919,2.674578,9.415266,-8.133833,7.618225,1.949924,-0.817396,7.578892,-5.736885,5.062334,0.481282,0.092805,4.041840,5.381304,-8.578990,3.564309,1.569444,0.020995,8.248906,4.714658,-4.617015,-0.098908,8.213178,-7.424139,0.506899,2.608394,7.964142,9.865394,-6.331299,-8.209551,-1.418675,2.245834,0.027774,-1.395335,-5.860947,8.421699,-5.095039,7.641904,-6.420714,-3.797590,1.721487,-8.534159,-4.491231,9.649893,-0.282010,5.378439,-4.983501,-4.947425,-0.306774,-8.094761,-2.383116,6.762971,-7.620716,0.556660,-9.850390,-5.810352,5.261213,-1.270702,-7.470531,-8.511774,-4.958262,2.659193,-5.485105,-8.170119,-8.581769,5.827403,-5.040496,-6.463032,4.763275,5.761333,1.408380,3.196701,-7.677740,-8.438482,-0.539925,3.314307,-4.548879,2.231261,8.646702,1.129051,-7.610596,-5.905871,3.457011,3.237796,-2.827568,6.915014,3.072689,-0.031185,-5.531421,-3.807038,-4.061467,9.874289,1.632576,4.616938,-2.988607,-4.691020,-0.828529,-5.018388,4.038413,-3.983229,-9.233884,9.691106,4.833092,-6.075003,-2.285887,-1.736200,-0.925535,-1.472216,-2.763008,-1.674051,-1.632910,1.933708,-3.232456,6.981565,-5.528239,8.105441,8.455544,-2.978347,2.506524,-7.600722,2.092728,-5.600237,1.193599,0.615544,-7.167749,-3.896461,4.925566,2.226858,4.868658,6.493435,4.631320,4.518493,-5.267080,9.702532,-7.886035,9.112314,-4.554611,1.735388,-2.026749,0.250341,7.444905,-7.857572,0.733833,-9.753625,-3.224498,-5.031473,-0.639442,-4.027773,9.562107,-6.320248,8.822859,-6.303043,1.410958,5.027060,-5.386141,1.732664,9.077401,-5.080571,5.628799,5.020480,6.091586,5.914737,6.047433,-4.733947,8.486007,-8.666757,-2.208688,-7.431826,9.524856,-8.395012,-6.810083,3.786086,6.469016,0.284814,-8.113836,-5.579068,-6.154505,5.112051,0.822160,4.680507,8.847878,3.769040,-1.393866,6.165176,-9.828543,0.385490,3.019937,-1.058044,5.641337,-5.816842,-3.942405,6.554544,-4.598806,5.301665,-7.520393,9.897167,-5.803147,1.075862,-9.923735,-1.652522,-8.781957,-7.127317,-1.513774,-7.926710,-1.282477,3.274059,0.033829,1.826444,-6.431675,3.479168,9.466325,-1.004092,-3.150796,-7.701338,-0.068329,8.193249,4.559062,5.091762,-7.358169,4.248196,-1.969010,2.104841,2.250902,4.775285,5.316469,-3.581773,6.412156,3.399840,-4.882673,6.411358,-5.343150,-7.679584,-8.339139,-0.299434,4.465194,5.226691,-9.170917,-5.258366,3.387360,4.349491,-5.499201,-6.226744,-0.322266,1.076176,1.079157,-3.174256,4.460584,1.598233,-0.085012,-9.493572,5.779244,7.442146,0.301654,0.391091,8.318056,0.928393,-2.509774,-2.900196,1.575247,-2.509303,-8.032274,2.697992,5.973021,0.814552,-9.320964,3.661481,7.332649,4.628028,-6.908319,3.673352,-0.561229,-7.604819,-0.391213,7.150254,-8.995471,4.235556,-1.635646,5.832246,0.580329,3.942837,-3.344782,-1.608113,0.557174,-4.347127,-9.869740,-4.285897,6.864048,-8.491963,2.621913,1.198361,9.880476,-0.174796,3.273209,9.475971,-5.383335,-6.294463,7.739093,-7.493494,0.435089,4.477806,-2.884640,-1.112857,-6.685021,-7.182276,-8.097656,6.588742,-2.324539,-1.171542,7.908423,-8.319667,-0.544412,7.928562,6.470699,3.783933,-7.418519,7.790579,-3.292338,-7.685383,-6.531082,-9.352676,1.521380,-1.478077,9.588598,8.827826,-5.477852,-2.625299,5.776993,-6.148069,1.303850,6.100319,-8.339897,-9.288502,-2.811552,2.610504,6.514502,7.465392,-2.935641,-1.027135,-4.366286,-2.951871,-5.819895,-7.384232,-9.920157,-7.263945,-2.582830,-6.094338,-4.438274,7.528540,6.445726,8.187993,-8.701264,5.243444,-9.469904,-8.252056,-9.244660,2.039386,3.086242,-4.719811,0.326253,2.569466,-4.518738,-7.310789,-6.675004,6.454337,0.958310,7.483348,4.653775,-9.419143,-4.925073,4.940766,7.042904,3.619733,-4.780792,6.331016,9.528945,7.491098,-7.672481,-9.942374,5.827708,-5.683536,3.236196,-7.579796,9.653219,-6.894756,0.747750,-0.808499,1.453240,4.372720,2.021742,7.196321,0.072695,-2.198468,-9.771873,-5.814289,-7.344336,-9.033736,-6.128232,-1.349273,2.356590,-9.543359,-5.319002,-5.771681,-7.814477,1.028617,-0.817376,-4.318825,5.337574,1.381152,-6.767343,4.374521,-7.198852,-3.282613,-4.074048,-2.580370,4.487939,-3.059022,5.121113,7.077234,-0.434341,8.687150,8.856896,-9.468203,-1.613059,8.467814,-4.183602,1.632065,-0.880685,1.014408,3.368508,9.667895,-7.999614,-1.526667,-5.049354,-4.364264,5.526421,8.274632,4.283846,4.057190,3.981592,-2.586365,-5.748688,-6.888307,1.776681,1.995188,-7.184418,-9.895811,7.335717,-1.317957,-8.644609,-7.186169,6.271789,9.070054,-1.498803,-7.428212,6.721969,9.511157,6.124441,-7.681018,7.920683,8.177621,-9.576867,9.367429,-2.952965,2.345535,-6.923627,-8.052495,9.683348,-8.045583,7.391573,4.404328,-3.234471,-9.241758,8.790396,-9.425265,-3.655698,-0.125440,4.708961,-6.351483,4.588057,6.602927,-6.330029,3.245186,4.324877,5.109841,8.302976,5.546170,5.982747,4.402381,-7.395576,3.478054,9.876136,-5.283831,9.410399,-8.985343,-1.204793,-3.443586,-7.195190,6.121392,-0.773676,-9.479118,6.997958,5.403884,6.076413,0.832008,-7.623778,-5.476808,-4.771252,4.877858,-6.209726,5.935051,0.672139,2.741937,1.190182,3.746159,3.963569,1.025417,9.910082,1.629821,7.835630,-1.227524,2.632809,4.631239,4.738271,-4.280703,6.570603,7.570623,2.317671,-4.940017,8.038160,-3.503964,7.410928,4.439489,-9.137179,6.144841,-4.950641,-6.925893,-1.857908,9.404930,-6.359392,2.052569,0.560659,-7.924292,2.237562,-2.770387,-6.200637,7.537253,-6.295429,-7.444856,9.226035,0.939804,1.159273,-1.744382,1.478948,-2.616234,9.494036,9.883212,-5.636229,7.204140,-5.639070,-1.445890,5.858627,-7.565202,-8.918042,-0.245608,-3.043601,2.223323,0.801975,-7.129303,-3.466120,-5.572696,-9.357461,-9.001570,5.239296,3.935617,3.078826,-1.472583,1.565789,8.805775,8.119480,-7.316392,4.302582,-1.458620,0.383833,7.381050,1.287188,8.398743,-6.795450,-7.125901,0.751370,0.975911,9.355563,7.205633,6.939480,-1.996589,3.459955,-6.272358,1.383190,1.084009,4.894580,-2.388189,8.401665,4.578815,7.304506,1.982888,2.028011,-2.137538,1.221307,8.469434,-5.109142,5.014986,-0.201096,-4.870297,-4.290385,-2.279840,-8.290901,-1.632239,-8.662406,4.840491,1.117838,5.368021,-5.559722,9.374198,2.714060,-6.214655,5.808199,4.658514,6.971353,4.396402,-5.054356,-6.206217,-1.901865,-6.944775,-7.482067,-5.293879,-5.904074,-5.159453,0.091898,-1.986580,-1.195039,-2.124817,8.190745,-7.549531,2.962704,-1.681239,7.772495,5.068251,-3.663133,2.119380,7.044118,-1.293789,1.924439,-0.601848,2.450014,7.842099,3.955242,9.787017,-8.242721,-7.934598,9.025096,3.999418,2.427058,-8.289830,-9.766969,-4.509944,5.002853,5.807457,7.623870,-1.312279,9.263393,-9.824360,9.417253,3.805365,1.830150,-3.396472,-7.168022,-7.640143,-6.248224,7.579664,-2.572680,-0.770887,2.548811,-2.670096,-3.131804,6.046312,-8.345817,-1.927476,5.050640,8.817555,8.610330,6.669662,4.423165,1.637584,-4.941171,-4.376727,-8.490707,-4.312362,3.274035,-1.498554,2.023749,4.718984,-3.184963,-9.739614,7.947386,-2.809833,7.086114,-7.717733,3.909224,-4.230059,2.374197,-0.509972,1.925520,8.314656,9.828491,-1.696652,2.078305,9.311880,-4.418599,9.439239,5.957856,-2.951839,0.083559,-9.665779,9.770953,-9.957803,3.109075,-7.455273,8.306804,6.829205,-1.673124,-3.446833,4.855449,1.092325,3.694793,1.563537,-2.225785,7.299603,9.565104,0.030974,-4.192268,5.057192,-3.732712,-9.488764,7.415315,5.273274,-1.564569,3.920480,0.365778,7.358699,3.958324,6.548858,-7.453520,5.091478,-1.710338,-3.191968,-4.884652,4.833321,-4.451839,-8.886727,3.478885,0.176594,4.314870,-4.088161,1.282237,8.771595,-0.477880,-7.428404,3.491410,-1.459555,-8.931485,-0.638196,-6.599612,-9.758123,-1.656693,-0.101522,-5.171605,7.375150,-7.347781,-7.918193,3.883988,-2.218311,-9.568132,-0.463282,-2.586104,-4.438756,-8.179854,7.820612,-0.998116,4.995909,9.175369,-7.597148,0.979058,7.642436,4.163689,4.789955,-1.555381,0.111699,-5.875522,-6.622801,-3.189212,-6.542328,-1.759062,-2.250460,1.572699,0.886709,0.387487,-6.913516,8.304959,8.184686,8.917314,9.458021,-3.036915,-7.322364,-7.392213,-2.700888,2.750618,5.932853,-6.693299,-5.310594,5.059792,-4.068657,-1.029957,0.815176,3.667054,-7.056185,5.723096,-6.967615,-2.702656,4.368233,8.615910,-4.685996,-9.014647,-3.876679,9.062646,-6.318348,-2.347724,9.959410,4.617870,-7.967770,2.701005,8.680075,-1.485876,6.272166,-1.742451,-8.573504,-5.216753,3.822112,-4.075299,0.341433,-8.606373,8.930137,2.870051,7.019494,3.802263,8.876141,0.106230,-5.808645,-2.597066,-6.784223,-4.405037,-2.631963,3.138536,1.806035,-8.432188,8.814314,-9.769899,1.119900,-6.751340,-0.739020,2.258440,-3.508609,-9.058899,-9.435288,-0.679434,6.416880,6.480561,1.936950,0.784331,4.236301,-3.425216,2.358003,3.826918,-4.169892,5.451989,8.302553,-9.956044,0.726267,-2.786990,7.562352,2.044827,9.195027,-5.168752,7.089191,9.457251,9.135931,-7.733820,-3.590161,-0.046788,5.957608,1.651100,-3.184807,-1.615051,-6.980652,9.215893,-8.561667,8.907732,-6.089864,-3.521908,6.277351,-2.834086,5.091338,1.206136,-8.999315,-7.028941,-0.862020,-8.056555,6.197688,-5.526189,-9.869635,0.776764,-1.868367,-3.648084,4.527319,9.965370,1.536552,4.499865,-4.503896,-8.393831,-5.706780,-3.577069,1.806828,9.482326,5.086199,-4.807628,-5.700636,-7.145015,-2.984542,0.578282,-0.183491,6.947665,-1.378030,-2.194335,4.163238,2.379051,-4.427386,-2.375197,-5.624326,-5.470983,-0.380751,4.581668,0.821094,5.621737,3.934214,6.648378,4.951500,1.184081,0.605083,-5.058146,-3.821828,3.649817,1.410613,-6.943087,2.108032,-6.853536,-6.736170,-2.073576,4.526239,2.562962,-3.883339,-5.242075,4.050984,6.757282,-3.408426,-8.408146,1.304845,3.187465,3.473617,7.088706,-6.055551,-0.018296,1.230739,-2.456650,9.825846,1.878716,-3.917462,1.652757,5.536279,0.413702,2.312670,3.666119,0.574516,1.420271,-4.081398,3.274330,-0.684942,4.842304,1.924498,3.525865,-0.665596,-2.777490,-7.358556,-0.641078,0.363299,8.750078,1.253809,7.956809,0.851903,-7.427953,1.752431,4.286866,0.947948,-1.856760,-2.129970,0.527001,-4.432725,-6.366037,-3.957602,1.700284,-8.982827,-8.835338,6.695987,-5.932184,-4.187775,-3.509443,-4.360125,-1.921928,1.748009,-0.551177,-7.437129,-9.372084,-6.882405,6.544981,1.104636,-3.362596,-7.936772,-9.277129,-1.838236,-2.180689,4.600679,5.908309,-4.394997,2.310070,-5.761208,-6.977545,-7.991543,0.331165,9.763029,1.263696,3.059119,-5.894188,-4.829391,8.195146,3.192510,1.458387,2.187951,-7.136736,-5.025691,5.463021,-0.754933,4.944533,-6.601761,5.676524,-3.940767,-0.531791,-6.829637,8.550860,5.871186,2.666389,-2.448352,8.942955,9.420513,-0.124387,-1.465309,-5.367339,2.927858,9.932559,0.010851,2.019844,8.812046,0.371103,-9.299336,-1.564061,-4.881300,-1.762932,-0.972904,-2.790545,8.279477,-6.509433,-0.952138,-1.654933,-4.299963,2.090836,-4.218441,4.348273,-9.511448,9.225619,3.900827,5.387482,-3.380997,5.438000,7.890581,-5.427252,-6.612786,-4.562165,-9.146160,-2.950664,-1.223427,-6.137392,-0.756111,-6.694004,-7.427346,7.354582,5.657437,4.084792,-6.373066,2.356236,-0.738088,-3.899737,-0.638212,6.596912,-0.814972,2.431680,6.508706,9.909291,-9.400660,4.794809,-9.370276,-8.964210,1.682098,2.672979,-0.332103], dtype = "float64")#candidate|4561|(2048,)|const|float64
call_4560 = func_1863_call(relay.reshape(const_4561.astype('float64'), [16, 16, 8]))
call_4562 = func_1863_call(relay.reshape(const_4561.astype('float64'), [16, 16, 8]))
bop_4565 = relay.logical_or(call_4560.astype('bool'), relay.reshape(const_4561.astype('bool'), relay.shape_of(call_4560))) # shape=(16, 16, 8)
bop_4568 = relay.logical_or(call_4562.astype('bool'), relay.reshape(const_4561.astype('bool'), relay.shape_of(call_4562))) # shape=(16, 16, 8)
output = relay.Tuple([call_4544,call_4548,call_4556,const_4557,bop_4565,])
output2 = relay.Tuple([call_4545,call_4549,call_4558,const_4557,bop_4568,])
func_4580 = relay.Function([], output)
mod['func_4580'] = func_4580
mod = relay.transform.InferType()(mod)
mutated_mod['func_4580'] = func_4580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mutated_mod.get_global_var('func_4580')
call_4581 = func_4580_call()
output = call_4581
func_4582 = relay.Function([], output)
mutated_mod['func_4582'] = func_4582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_4754 = relay.TupleGetItem(func_4580_call(), 4)
call_4755 = relay.TupleGetItem(func_4582_call(), 4)
output = call_4754
output2 = call_4755
func_4763 = relay.Function([], output)
mod['func_4763'] = func_4763
mod = relay.transform.InferType()(mod)
output = func_4763()
func_4764 = relay.Function([], output)
mutated_mod['func_4764'] = func_4764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_4765 = relay.TupleGetItem(func_4580_call(), 3)
call_4766 = relay.TupleGetItem(func_4582_call(), 3)
func_4763_call = mod.get_global_var('func_4763')
func_4764_call = mutated_mod.get_global_var('func_4764')
call_4779 = func_4763_call()
call_4780 = func_4763_call()
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_4799 = func_1863_call(relay.reshape(call_4779.astype('float64'), [16, 16, 8]))
call_4800 = func_1863_call(relay.reshape(call_4779.astype('float64'), [16, 16, 8]))
uop_4804 = relay.log(call_4765.astype('float64')) # shape=(1008, 1)
uop_4806 = relay.log(call_4766.astype('float64')) # shape=(1008, 1)
func_1251_call = mod.get_global_var('func_1251')
func_1256_call = mutated_mod.get_global_var('func_1256')
var_4808 = relay.var("var_4808", dtype = "float32", shape = (243,))#candidate|4808|(243,)|var|float32
var_4809 = relay.var("var_4809", dtype = "float32", shape = (720,))#candidate|4809|(720,)|var|float32
var_4810 = relay.var("var_4810", dtype = "int64", shape = (462,))#candidate|4810|(462,)|var|int64
call_4807 = relay.TupleGetItem(func_1251_call(relay.reshape(var_4808.astype('float32'), [9, 3, 9]), relay.reshape(var_4809.astype('float32'), [720, 1]), relay.reshape(var_4810.astype('int64'), [462,]), ), 6)
call_4811 = relay.TupleGetItem(func_1256_call(relay.reshape(var_4808.astype('float32'), [9, 3, 9]), relay.reshape(var_4809.astype('float32'), [720, 1]), relay.reshape(var_4810.astype('int64'), [462,]), ), 6)
func_4473_call = mod.get_global_var('func_4473')
func_4476_call = mutated_mod.get_global_var('func_4476')
var_4819 = relay.var("var_4819", dtype = "int16", shape = (216,))#candidate|4819|(216,)|var|int16
call_4818 = relay.TupleGetItem(func_4473_call(relay.reshape(var_4819.astype('int16'), [6, 9, 4])), 0)
call_4820 = relay.TupleGetItem(func_4476_call(relay.reshape(var_4819.astype('int16'), [6, 9, 4])), 0)
func_4580_call = mod.get_global_var('func_4580')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_4826 = relay.TupleGetItem(func_4580_call(), 2)
call_4827 = relay.TupleGetItem(func_4582_call(), 2)
output = relay.Tuple([call_4779,call_4799,uop_4804,call_4807,var_4808,var_4809,var_4810,call_4818,var_4819,call_4826,])
output2 = relay.Tuple([call_4780,call_4800,uop_4806,call_4811,var_4808,var_4809,var_4810,call_4820,var_4819,call_4827,])
func_4828 = relay.Function([var_4808,var_4809,var_4810,var_4819,], output)
mod['func_4828'] = func_4828
mod = relay.transform.InferType()(mod)
mutated_mod['func_4828'] = func_4828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4828_call = mutated_mod.get_global_var('func_4828')
var_4830 = relay.var("var_4830", dtype = "float32", shape = (243,))#candidate|4830|(243,)|var|float32
var_4831 = relay.var("var_4831", dtype = "float32", shape = (720,))#candidate|4831|(720,)|var|float32
var_4832 = relay.var("var_4832", dtype = "int64", shape = (462,))#candidate|4832|(462,)|var|int64
var_4833 = relay.var("var_4833", dtype = "int16", shape = (216,))#candidate|4833|(216,)|var|int16
call_4829 = func_4828_call(var_4830,var_4831,var_4832,var_4833,)
output = call_4829
func_4834 = relay.Function([var_4830,var_4831,var_4832,var_4833,], output)
mutated_mod['func_4834'] = func_4834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_4883 = relay.TupleGetItem(func_4460_call(), 0)
call_4884 = relay.TupleGetItem(func_4461_call(), 0)
var_4889 = relay.var("var_4889", dtype = "float32", shape = (9, 16, 6))#candidate|4889|(9, 16, 6)|var|float32
bop_4890 = relay.subtract(call_4883.astype('uint64'), relay.reshape(var_4889.astype('uint64'), relay.shape_of(call_4883))) # shape=(9, 16, 6)
bop_4893 = relay.subtract(call_4884.astype('uint64'), relay.reshape(var_4889.astype('uint64'), relay.shape_of(call_4884))) # shape=(9, 16, 6)
func_4763_call = mod.get_global_var('func_4763')
func_4764_call = mutated_mod.get_global_var('func_4764')
call_4896 = func_4763_call()
call_4897 = func_4763_call()
output = relay.Tuple([bop_4890,call_4896,])
output2 = relay.Tuple([bop_4893,call_4897,])
func_4910 = relay.Function([var_4889,], output)
mod['func_4910'] = func_4910
mod = relay.transform.InferType()(mod)
mutated_mod['func_4910'] = func_4910
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4911 = relay.var("var_4911", dtype = "float32", shape = (9, 16, 6))#candidate|4911|(9, 16, 6)|var|float32
func_4910_call = mutated_mod.get_global_var('func_4910')
call_4912 = func_4910_call(var_4911)
output = call_4912
func_4913 = relay.Function([var_4911], output)
mutated_mod['func_4913'] = func_4913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_4933 = relay.TupleGetItem(func_4460_call(), 0)
call_4934 = relay.TupleGetItem(func_4461_call(), 0)
var_4940 = relay.var("var_4940", dtype = "float32", shape = (9, 16, 6))#candidate|4940|(9, 16, 6)|var|float32
bop_4941 = relay.divide(call_4933.astype('float32'), relay.reshape(var_4940.astype('float32'), relay.shape_of(call_4933))) # shape=(9, 16, 6)
bop_4944 = relay.divide(call_4934.astype('float32'), relay.reshape(var_4940.astype('float32'), relay.shape_of(call_4934))) # shape=(9, 16, 6)
uop_4948 = relay.acos(var_4940.astype('float32')) # shape=(9, 16, 6)
func_3320_call = mod.get_global_var('func_3320')
func_3325_call = mutated_mod.get_global_var('func_3325')
const_4951 = relay.const([[-10],[1],[6],[8],[4],[7],[5],[1],[-2],[8],[-3],[-1],[10],[4],[2],[8],[-6],[-9],[2],[-2],[-7],[6],[-10],[2],[7],[7],[-8],[-8],[2],[10],[5],[-7],[-9],[-5],[4],[-7],[-4],[-4],[1],[8],[6],[7],[-6],[4],[-8],[-2],[-4],[-6],[-5],[-2],[-6],[-1],[4],[-7],[-3],[-3],[10],[5],[-7],[-4],[5],[10],[6],[10],[4],[-2],[3],[-3],[3],[3],[2],[-7],[8],[-10],[2],[1],[-3],[7],[-6],[-1],[-1],[3],[10],[-2],[-5],[-9],[1],[-1],[1],[-5],[7],[-2],[-9],[-10],[-6],[-7],[5],[2],[7],[8],[-10],[-1],[4],[-3],[3],[-10],[4],[-1],[-9],[-7],[-1],[3],[-8],[3],[2],[9],[8],[-5],[2],[-9],[-6],[5],[9],[2],[-6],[-4]], dtype = "int32")#candidate|4951|(126, 1)|const|int32
const_4952 = relay.const([5,5,-3,9,8,-4,2,-1,-10,8,-8,1,6,10,6,-6,-3,9,7,-7,-7,-10,-6,-10,9,-2,-4,6,10,-9,-1,7,5,9,-6,-6,9,2,6,-2,7,-1,-4,-2,-1,1,5,8,-6,1,-7,-4,5,-2,5,8,-5,-4,4,-5,6,-10,8,2,-7,5,-2,-8,5,9,-3,4,4,1,6,6,4,5,-4,-5,10,2,-10,-10,-2,5,-6,5,6,1], dtype = "int64")#candidate|4952|(90,)|const|int64
var_4953 = relay.var("var_4953", dtype = "int16", shape = (224,))#candidate|4953|(224,)|var|int16
call_4950 = relay.TupleGetItem(func_3320_call(relay.reshape(const_4951.astype('int32'), [3, 6, 7]), relay.reshape(const_4952.astype('int64'), [90,]), relay.reshape(var_4953.astype('int16'), [16, 14]), ), 1)
call_4954 = relay.TupleGetItem(func_3325_call(relay.reshape(const_4951.astype('int32'), [3, 6, 7]), relay.reshape(const_4952.astype('int64'), [90,]), relay.reshape(var_4953.astype('int16'), [16, 14]), ), 1)
output = relay.Tuple([bop_4941,uop_4948,call_4950,const_4951,const_4952,var_4953,])
output2 = relay.Tuple([bop_4944,uop_4948,call_4954,const_4951,const_4952,var_4953,])
func_4976 = relay.Function([var_4940,var_4953,], output)
mod['func_4976'] = func_4976
mod = relay.transform.InferType()(mod)
var_4977 = relay.var("var_4977", dtype = "float32", shape = (9, 16, 6))#candidate|4977|(9, 16, 6)|var|float32
var_4978 = relay.var("var_4978", dtype = "int16", shape = (224,))#candidate|4978|(224,)|var|int16
output = func_4976(var_4977,var_4978,)
func_4979 = relay.Function([var_4977,var_4978,], output)
mutated_mod['func_4979'] = func_4979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4763_call = mod.get_global_var('func_4763')
func_4764_call = mutated_mod.get_global_var('func_4764')
call_4996 = func_4763_call()
call_4997 = func_4763_call()
var_5014 = relay.var("var_5014", dtype = "bool", shape = (16, 16, 8))#candidate|5014|(16, 16, 8)|var|bool
bop_5015 = relay.maximum(call_4996.astype('uint32'), relay.reshape(var_5014.astype('uint32'), relay.shape_of(call_4996))) # shape=(16, 16, 8)
bop_5018 = relay.maximum(call_4997.astype('uint32'), relay.reshape(var_5014.astype('uint32'), relay.shape_of(call_4997))) # shape=(16, 16, 8)
func_4289_call = mod.get_global_var('func_4289')
func_4293_call = mutated_mod.get_global_var('func_4293')
const_5030 = relay.const([-5,10,5,-2,-7,2,-10,5,8,7,4,4,-5,-9,4,-4,-10,-3,-6,-8,1,-3,8,4,-9,-9,-5,10,-5,4,-3,-10,-5,-8,7,5,7,-10,-6,-3,5,8,5,1,7,1,4,-2,4,9,7,1,2,1,6,-2,5,1,10,-2,-7,-8,6,-1,2,-2,-4,5,6,5,-1,3,9,-8,5,-5,-6,-3,-2,1,-4,5,7,5,7,5,7,3,-1,-2,-2,-7,7,-1,4,-3,6,-6,7,8,3,9,3,-3,-5,-9,3,7,5,9,9,-8,9,2,7,-9,5,-10,1,3,10,5,7,5,8,-3,-7,4,5,1,7,-2,-9,-3,8,6,-5,1,-1,-5,-10,7,-9,3,-10,8,8,10,-4,8,6,-10,-5,4,-9,6,-9,-9,8,2,10,-3,-10,4,7,-4,5,5,-4,5,-2,-5,6,9,5,1,-9,-2,9,-1,-9,9,-10,4,-7,-9,2,10,-7,-3,10,10,8,8,-9,4,-5,-1,-1,-9,2,7,-2,-3,8,3,-7,7,4,-3,-4,2,1,-6,-6,1,5,-3,7,-7,-9,-2,3,4,-3,-2,-5,10,-6,8,-1,2,-7,2,1,8,10,-8,9,2,-10,-3,-1,-3,-7,-10,8,-6,-7,8,10,7,7,-4,-1,2], dtype = "int16")#candidate|5030|(256,)|const|int16
call_5029 = relay.TupleGetItem(func_4289_call(relay.reshape(const_5030.astype('int16'), [16, 4, 4]), relay.reshape(const_5030.astype('int16'), [16, 4, 4]), ), 0)
call_5031 = relay.TupleGetItem(func_4293_call(relay.reshape(const_5030.astype('int16'), [16, 4, 4]), relay.reshape(const_5030.astype('int16'), [16, 4, 4]), ), 0)
uop_5034 = relay.atanh(call_5029.astype('float64')) # shape=(16, 4, 4)
uop_5036 = relay.atanh(call_5031.astype('float64')) # shape=(16, 4, 4)
output = relay.Tuple([bop_5015,const_5030,uop_5034,])
output2 = relay.Tuple([bop_5018,const_5030,uop_5036,])
func_5043 = relay.Function([var_5014,], output)
mod['func_5043'] = func_5043
mod = relay.transform.InferType()(mod)
mutated_mod['func_5043'] = func_5043
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5044 = relay.var("var_5044", dtype = "bool", shape = (16, 16, 8))#candidate|5044|(16, 16, 8)|var|bool
func_5043_call = mutated_mod.get_global_var('func_5043')
call_5045 = func_5043_call(var_5044)
output = call_5045
func_5046 = relay.Function([var_5044], output)
mutated_mod['func_5046'] = func_5046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_5089 = relay.TupleGetItem(func_4460_call(), 0)
call_5090 = relay.TupleGetItem(func_4461_call(), 0)
output = relay.Tuple([call_5089,])
output2 = relay.Tuple([call_5090,])
func_5092 = relay.Function([], output)
mod['func_5092'] = func_5092
mod = relay.transform.InferType()(mod)
mutated_mod['func_5092'] = func_5092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mutated_mod.get_global_var('func_5092')
call_5093 = func_5092_call()
output = call_5093
func_5094 = relay.Function([], output)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_5145 = relay.TupleGetItem(func_4580_call(), 2)
call_5146 = relay.TupleGetItem(func_4582_call(), 2)
uop_5154 = relay.log(call_5145.astype('float32')) # shape=(14, 9, 8)
uop_5156 = relay.log(call_5146.astype('float32')) # shape=(14, 9, 8)
bop_5159 = relay.minimum(uop_5154.astype('float32'), relay.reshape(call_5145.astype('float32'), relay.shape_of(uop_5154))) # shape=(14, 9, 8)
bop_5162 = relay.minimum(uop_5156.astype('float32'), relay.reshape(call_5146.astype('float32'), relay.shape_of(uop_5156))) # shape=(14, 9, 8)
output = bop_5159
output2 = bop_5162
func_5171 = relay.Function([], output)
mod['func_5171'] = func_5171
mod = relay.transform.InferType()(mod)
output = func_5171()
func_5172 = relay.Function([], output)
mutated_mod['func_5172'] = func_5172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_5224 = func_5171_call()
call_5225 = func_5171_call()
output = relay.Tuple([call_5224,])
output2 = relay.Tuple([call_5225,])
func_5239 = relay.Function([], output)
mod['func_5239'] = func_5239
mod = relay.transform.InferType()(mod)
output = func_5239()
func_5240 = relay.Function([], output)
mutated_mod['func_5240'] = func_5240
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5286 = relay.var("var_5286", dtype = "float64", shape = (5, 5, 10))#candidate|5286|(5, 5, 10)|var|float64
uop_5287 = relay.acos(var_5286.astype('float64')) # shape=(5, 5, 10)
output = uop_5287
output2 = uop_5287
func_5291 = relay.Function([var_5286,], output)
mod['func_5291'] = func_5291
mod = relay.transform.InferType()(mod)
mutated_mod['func_5291'] = func_5291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5292 = relay.var("var_5292", dtype = "float64", shape = (5, 5, 10))#candidate|5292|(5, 5, 10)|var|float64
func_5291_call = mutated_mod.get_global_var('func_5291')
call_5293 = func_5291_call(var_5292)
output = call_5293
func_5294 = relay.Function([var_5292], output)
mutated_mod['func_5294'] = func_5294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_5368 = relay.TupleGetItem(func_4580_call(), 3)
call_5369 = relay.TupleGetItem(func_4582_call(), 3)
output = call_5368
output2 = call_5369
func_5372 = relay.Function([], output)
mod['func_5372'] = func_5372
mod = relay.transform.InferType()(mod)
output = func_5372()
func_5373 = relay.Function([], output)
mutated_mod['func_5373'] = func_5373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5372_call = mod.get_global_var('func_5372')
func_5373_call = mutated_mod.get_global_var('func_5373')
call_5433 = func_5372_call()
call_5434 = func_5372_call()
uop_5443 = relay.exp(call_5433.astype('float64')) # shape=(1008, 1)
uop_5445 = relay.exp(call_5434.astype('float64')) # shape=(1008, 1)
output = relay.Tuple([uop_5443,])
output2 = relay.Tuple([uop_5445,])
func_5448 = relay.Function([], output)
mod['func_5448'] = func_5448
mod = relay.transform.InferType()(mod)
mutated_mod['func_5448'] = func_5448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mutated_mod.get_global_var('func_5448')
call_5449 = func_5448_call()
output = call_5449
func_5450 = relay.Function([], output)
mutated_mod['func_5450'] = func_5450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_5500 = relay.TupleGetItem(func_4537_call(), 0)
call_5501 = relay.TupleGetItem(func_4538_call(), 0)
func_4910_call = mod.get_global_var('func_4910')
func_4913_call = mutated_mod.get_global_var('func_4913')
call_5511 = relay.TupleGetItem(func_4910_call(relay.reshape(call_5500.astype('float32'), [9, 16, 6])), 0)
call_5512 = relay.TupleGetItem(func_4913_call(relay.reshape(call_5500.astype('float32'), [9, 16, 6])), 0)
output = relay.Tuple([call_5500,call_5511,])
output2 = relay.Tuple([call_5501,call_5512,])
func_5519 = relay.Function([], output)
mod['func_5519'] = func_5519
mod = relay.transform.InferType()(mod)
mutated_mod['func_5519'] = func_5519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5519_call = mutated_mod.get_global_var('func_5519')
call_5520 = func_5519_call()
output = call_5520
func_5521 = relay.Function([], output)
mutated_mod['func_5521'] = func_5521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4763_call = mod.get_global_var('func_4763')
func_4764_call = mutated_mod.get_global_var('func_4764')
call_5566 = func_4763_call()
call_5567 = func_4763_call()
output = call_5566
output2 = call_5567
func_5587 = relay.Function([], output)
mod['func_5587'] = func_5587
mod = relay.transform.InferType()(mod)
output = func_5587()
func_5588 = relay.Function([], output)
mutated_mod['func_5588'] = func_5588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_5610 = relay.TupleGetItem(func_4580_call(), 4)
call_5611 = relay.TupleGetItem(func_4582_call(), 4)
output = relay.Tuple([call_5610,])
output2 = relay.Tuple([call_5611,])
func_5620 = relay.Function([], output)
mod['func_5620'] = func_5620
mod = relay.transform.InferType()(mod)
mutated_mod['func_5620'] = func_5620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5620_call = mutated_mod.get_global_var('func_5620')
call_5621 = func_5620_call()
output = call_5621
func_5622 = relay.Function([], output)
mutated_mod['func_5622'] = func_5622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_5705 = relay.TupleGetItem(func_4537_call(), 0)
call_5706 = relay.TupleGetItem(func_4538_call(), 0)
var_5707 = relay.var("var_5707", dtype = "uint32", shape = (9, 16, 6))#candidate|5707|(9, 16, 6)|var|uint32
bop_5708 = relay.not_equal(call_5705.astype('bool'), relay.reshape(var_5707.astype('bool'), relay.shape_of(call_5705))) # shape=(9, 16, 6)
bop_5711 = relay.not_equal(call_5706.astype('bool'), relay.reshape(var_5707.astype('bool'), relay.shape_of(call_5706))) # shape=(9, 16, 6)
func_2419_call = mod.get_global_var('func_2419')
func_2424_call = mutated_mod.get_global_var('func_2424')
const_5718 = relay.const([5,5,10,-2,-3,-2,6,-6,2,-7,-4,-8,-4,2,-5,6,-6,7,-4,9,-3,-10,2,5,5,-7,-2,3,-1,10,5,3,7,-7,10,-8,8,-1,-3,4,-6,-6,7,-6,4,4,2,-3,9,1,8,2,9,-6,-8,10,-1,-2,-6,7,-6,1,8,8,6,7,-1,9,2,2,-4,-2,1,-3,4,-8,1,-10,-5,-8,-8,-2,4,10,-7,-6,7,7,-3,4,2,-10,3,-2,8,7,5,-6,-3,6,9,2,-9,-5,-3,2,2,8,3,4,-10,-9,10,-5,-4,-4,3,2,-7,6,5,-5,3,-2,3,-10,-7,-9,6,10,7,6,2,-3,2,-10,9,-4,9,1,-2,-5,1,5,-10,-9,1,-6,-1,3,-8,2,6,-2,-2,7,5,2,-9,-3,-6,-3,-8,-1,8,4,-4,-5,-2,7,1,9,-9,-10,-2,5,-3,-4,-7,-2,6,1,4,-2,3,2,5,-10,4,1,2,1,-6,8,9,-10,-6,5,-7,6,-6,3,-10,4,-2,-2,-2,-10,8,-4,10,2,-5,5,3,3,2,9,-1,-9,-1,-7,-4,3], dtype = "int16")#candidate|5718|(224,)|const|int16
var_5719 = relay.var("var_5719", dtype = "int64", shape = ())#candidate|5719|()|var|int64
var_5720 = relay.var("var_5720", dtype = "int64", shape = (90,))#candidate|5720|(90,)|var|int64
call_5717 = relay.TupleGetItem(func_2419_call(relay.reshape(const_5718.astype('int16'), [7, 16, 2]), relay.reshape(const_5718.astype('int16'), [7, 16, 2]), relay.reshape(var_5719.astype('int64'), []), relay.reshape(var_5720.astype('int64'), [90, 1]), ), 2)
call_5721 = relay.TupleGetItem(func_2424_call(relay.reshape(const_5718.astype('int16'), [7, 16, 2]), relay.reshape(const_5718.astype('int16'), [7, 16, 2]), relay.reshape(var_5719.astype('int64'), []), relay.reshape(var_5720.astype('int64'), [90, 1]), ), 2)
bop_5737 = relay.less_equal(call_5705.astype('bool'), relay.reshape(bop_5708.astype('bool'), relay.shape_of(call_5705))) # shape=(9, 16, 6)
bop_5740 = relay.less_equal(call_5706.astype('bool'), relay.reshape(bop_5711.astype('bool'), relay.shape_of(call_5706))) # shape=(9, 16, 6)
func_2040_call = mod.get_global_var('func_2040')
func_2044_call = mutated_mod.get_global_var('func_2044')
const_5742 = relay.const([-9,8,-10,4,8,5], dtype = "uint64")#candidate|5742|(6,)|const|uint64
const_5743 = relay.const([-4,-1,7,-3,-3,9,-7,6,-8,5,-1,-9,-1,4,-6,1,3,-4,-4,-7,-3,4,3,2,-6,-9,3,1,-4,2,-7,-9,-6,3,10,-8,6,3,-1,1,1,4,8,8,8,4,-4,8,-8,10,8,-10,-8,-4,-9,6,-4,6,4,4], dtype = "uint64")#candidate|5743|(60,)|const|uint64
call_5741 = func_2040_call(relay.reshape(const_5742.astype('uint64'), [1, 2, 3]), relay.reshape(const_5743.astype('uint64'), [10, 2, 3]), )
call_5744 = func_2040_call(relay.reshape(const_5742.astype('uint64'), [1, 2, 3]), relay.reshape(const_5743.astype('uint64'), [10, 2, 3]), )
bop_5748 = relay.logical_or(call_5741.astype('bool'), relay.reshape(const_5743.astype('bool'), relay.shape_of(call_5741))) # shape=(10, 2, 3)
bop_5751 = relay.logical_or(call_5744.astype('bool'), relay.reshape(const_5743.astype('bool'), relay.shape_of(call_5744))) # shape=(10, 2, 3)
output = relay.Tuple([call_5717,const_5718,var_5719,var_5720,bop_5737,const_5742,bop_5748,])
output2 = relay.Tuple([call_5721,const_5718,var_5719,var_5720,bop_5740,const_5742,bop_5751,])
func_5768 = relay.Function([var_5707,var_5719,var_5720,], output)
mod['func_5768'] = func_5768
mod = relay.transform.InferType()(mod)
mutated_mod['func_5768'] = func_5768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5768_call = mutated_mod.get_global_var('func_5768')
var_5770 = relay.var("var_5770", dtype = "uint32", shape = (9, 16, 6))#candidate|5770|(9, 16, 6)|var|uint32
var_5771 = relay.var("var_5771", dtype = "int64", shape = ())#candidate|5771|()|var|int64
var_5772 = relay.var("var_5772", dtype = "int64", shape = (90,))#candidate|5772|(90,)|var|int64
call_5769 = func_5768_call(var_5770,var_5771,var_5772,)
output = call_5769
func_5773 = relay.Function([var_5770,var_5771,var_5772,], output)
mutated_mod['func_5773'] = func_5773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_5775 = relay.TupleGetItem(func_5092_call(), 0)
call_5776 = relay.TupleGetItem(func_5094_call(), 0)
func_2528_call = mod.get_global_var('func_2528')
func_2531_call = mutated_mod.get_global_var('func_2531')
const_5792 = relay.const(-9.439644, dtype = "float32")#candidate|5792|()|const|float32
var_5793 = relay.var("var_5793", dtype = "float32", shape = (882,))#candidate|5793|(882,)|var|float32
call_5791 = relay.TupleGetItem(func_2528_call(relay.reshape(const_5792.astype('float32'), []), relay.reshape(var_5793.astype('float32'), [14, 7, 9]), ), 0)
call_5794 = relay.TupleGetItem(func_2531_call(relay.reshape(const_5792.astype('float32'), []), relay.reshape(var_5793.astype('float32'), [14, 7, 9]), ), 0)
uop_5800 = relay.exp(call_5791.astype('float32')) # shape=(14, 7, 9)
uop_5802 = relay.exp(call_5794.astype('float32')) # shape=(14, 7, 9)
func_1302_call = mod.get_global_var('func_1302')
func_1306_call = mutated_mod.get_global_var('func_1306')
const_5804 = relay.const([-7,-5,-3,4,8,-8,-2,-1,-6,-8,8,3,2,-4,-4,-1,-3,6,7,-3,-3,-3,9,-3,2,3,1,8,8,4,-10,-5,-1,8,-10,-6,3,8,-3,9,6,9,-10,9,-10,9,9,-2,4,2,-2,-9,-8,-1,9,10,3,-3,6,-2,6,-8,-5,9,2,-5,10,3,10,2,-3,-7,10,1,1,-4,-5,5,-3,-3,-8,3,-2,-7,-10,6,-1,-2,-10,-7], dtype = "int64")#candidate|5804|(90,)|const|int64
call_5803 = func_1302_call(relay.reshape(const_5792.astype('int64'), []), relay.reshape(const_5804.astype('int64'), [1, 15, 6]), )
call_5805 = func_1302_call(relay.reshape(const_5792.astype('int64'), []), relay.reshape(const_5804.astype('int64'), [1, 15, 6]), )
output = relay.Tuple([call_5775,const_5792,var_5793,uop_5800,call_5803,const_5804,])
output2 = relay.Tuple([call_5776,const_5792,var_5793,uop_5802,call_5805,const_5804,])
func_5814 = relay.Function([var_5793,], output)
mod['func_5814'] = func_5814
mod = relay.transform.InferType()(mod)
mutated_mod['func_5814'] = func_5814
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5815 = relay.var("var_5815", dtype = "float32", shape = (882,))#candidate|5815|(882,)|var|float32
func_5814_call = mutated_mod.get_global_var('func_5814')
call_5816 = func_5814_call(var_5815)
output = call_5816
func_5817 = relay.Function([var_5815], output)
mutated_mod['func_5817'] = func_5817
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5854 = relay.var("var_5854", dtype = "int16", shape = (1, 5, 13))#candidate|5854|(1, 5, 13)|var|int16
var_5855 = relay.var("var_5855", dtype = "int16", shape = (9, 5, 13))#candidate|5855|(9, 5, 13)|var|int16
bop_5856 = relay.minimum(var_5854.astype('int16'), var_5855.astype('int16')) # shape=(9, 5, 13)
func_5043_call = mod.get_global_var('func_5043')
func_5046_call = mutated_mod.get_global_var('func_5046')
const_5861 = relay.const([False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,True], dtype = "bool")#candidate|5861|(2048,)|const|bool
call_5860 = relay.TupleGetItem(func_5043_call(relay.reshape(const_5861.astype('bool'), [16, 16, 8])), 0)
call_5862 = relay.TupleGetItem(func_5046_call(relay.reshape(const_5861.astype('bool'), [16, 16, 8])), 0)
bop_5869 = relay.greater_equal(call_5860.astype('bool'), relay.reshape(const_5861.astype('bool'), relay.shape_of(call_5860))) # shape=(16, 16, 8)
bop_5872 = relay.greater_equal(call_5862.astype('bool'), relay.reshape(const_5861.astype('bool'), relay.shape_of(call_5862))) # shape=(16, 16, 8)
output = relay.Tuple([bop_5856,bop_5869,])
output2 = relay.Tuple([bop_5856,bop_5872,])
func_5876 = relay.Function([var_5854,var_5855,], output)
mod['func_5876'] = func_5876
mod = relay.transform.InferType()(mod)
var_5877 = relay.var("var_5877", dtype = "int16", shape = (1, 5, 13))#candidate|5877|(1, 5, 13)|var|int16
var_5878 = relay.var("var_5878", dtype = "int16", shape = (9, 5, 13))#candidate|5878|(9, 5, 13)|var|int16
output = func_5876(var_5877,var_5878,)
func_5879 = relay.Function([var_5877,var_5878,], output)
mutated_mod['func_5879'] = func_5879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_5881 = relay.TupleGetItem(func_5092_call(), 0)
call_5882 = relay.TupleGetItem(func_5094_call(), 0)
output = relay.Tuple([call_5881,])
output2 = relay.Tuple([call_5882,])
func_5887 = relay.Function([], output)
mod['func_5887'] = func_5887
mod = relay.transform.InferType()(mod)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5887_call = mutated_mod.get_global_var('func_5887')
call_5888 = func_5887_call()
output = call_5888
func_5889 = relay.Function([], output)
mutated_mod['func_5889'] = func_5889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_5902 = relay.TupleGetItem(func_4537_call(), 0)
call_5903 = relay.TupleGetItem(func_4538_call(), 0)
output = call_5902
output2 = call_5903
func_5917 = relay.Function([], output)
mod['func_5917'] = func_5917
mod = relay.transform.InferType()(mod)
mutated_mod['func_5917'] = func_5917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5917_call = mutated_mod.get_global_var('func_5917')
call_5918 = func_5917_call()
output = call_5918
func_5919 = relay.Function([], output)
mutated_mod['func_5919'] = func_5919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_5955 = func_5171_call()
call_5956 = func_5171_call()
output = relay.Tuple([call_5955,])
output2 = relay.Tuple([call_5956,])
func_5964 = relay.Function([], output)
mod['func_5964'] = func_5964
mod = relay.transform.InferType()(mod)
output = func_5964()
func_5965 = relay.Function([], output)
mutated_mod['func_5965'] = func_5965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_5969 = relay.TupleGetItem(func_4460_call(), 0)
call_5970 = relay.TupleGetItem(func_4461_call(), 0)
uop_5975 = relay.sin(call_5969.astype('float64')) # shape=(9, 16, 6)
uop_5977 = relay.sin(call_5970.astype('float64')) # shape=(9, 16, 6)
uop_5985 = relay.sqrt(call_5969.astype('float64')) # shape=(9, 16, 6)
uop_5987 = relay.sqrt(call_5970.astype('float64')) # shape=(9, 16, 6)
output = relay.Tuple([uop_5975,uop_5985,])
output2 = relay.Tuple([uop_5977,uop_5987,])
func_5991 = relay.Function([], output)
mod['func_5991'] = func_5991
mod = relay.transform.InferType()(mod)
output = func_5991()
func_5992 = relay.Function([], output)
mutated_mod['func_5992'] = func_5992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5887_call = mod.get_global_var('func_5887')
func_5889_call = mutated_mod.get_global_var('func_5889')
call_6033 = relay.TupleGetItem(func_5887_call(), 0)
call_6034 = relay.TupleGetItem(func_5889_call(), 0)
output = call_6033
output2 = call_6034
func_6040 = relay.Function([], output)
mod['func_6040'] = func_6040
mod = relay.transform.InferType()(mod)
output = func_6040()
func_6041 = relay.Function([], output)
mutated_mod['func_6041'] = func_6041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5620_call = mod.get_global_var('func_5620')
func_5622_call = mutated_mod.get_global_var('func_5622')
call_6047 = relay.TupleGetItem(func_5620_call(), 0)
call_6048 = relay.TupleGetItem(func_5622_call(), 0)
var_6049 = relay.var("var_6049", dtype = "bool", shape = (16, 16, 8))#candidate|6049|(16, 16, 8)|var|bool
bop_6050 = relay.floor_mod(call_6047.astype('float64'), relay.reshape(var_6049.astype('float64'), relay.shape_of(call_6047))) # shape=(16, 16, 8)
bop_6053 = relay.floor_mod(call_6048.astype('float64'), relay.reshape(var_6049.astype('float64'), relay.shape_of(call_6048))) # shape=(16, 16, 8)
uop_6054 = relay.acosh(call_6047.astype('float64')) # shape=(16, 16, 8)
uop_6056 = relay.acosh(call_6048.astype('float64')) # shape=(16, 16, 8)
output = relay.Tuple([bop_6050,uop_6054,])
output2 = relay.Tuple([bop_6053,uop_6056,])
func_6058 = relay.Function([var_6049,], output)
mod['func_6058'] = func_6058
mod = relay.transform.InferType()(mod)
var_6059 = relay.var("var_6059", dtype = "bool", shape = (16, 16, 8))#candidate|6059|(16, 16, 8)|var|bool
output = func_6058(var_6059)
func_6060 = relay.Function([var_6059], output)
mutated_mod['func_6060'] = func_6060
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6129 = relay.var("var_6129", dtype = "uint16", shape = (1, 6, 8))#candidate|6129|(1, 6, 8)|var|uint16
var_6130 = relay.var("var_6130", dtype = "uint16", shape = (2, 6, 8))#candidate|6130|(2, 6, 8)|var|uint16
bop_6131 = relay.less_equal(var_6129.astype('bool'), var_6130.astype('bool')) # shape=(2, 6, 8)
func_5991_call = mod.get_global_var('func_5991')
func_5992_call = mutated_mod.get_global_var('func_5992')
call_6144 = relay.TupleGetItem(func_5991_call(), 0)
call_6145 = relay.TupleGetItem(func_5992_call(), 0)
var_6159 = relay.var("var_6159", dtype = "uint16", shape = (9, 6, 8))#candidate|6159|(9, 6, 8)|var|uint16
bop_6160 = relay.right_shift(var_6129.astype('int16'), var_6159.astype('int16')) # shape=(9, 6, 8)
output = relay.Tuple([bop_6131,call_6144,bop_6160,])
output2 = relay.Tuple([bop_6131,call_6145,bop_6160,])
func_6163 = relay.Function([var_6129,var_6130,var_6159,], output)
mod['func_6163'] = func_6163
mod = relay.transform.InferType()(mod)
mutated_mod['func_6163'] = func_6163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6163_call = mutated_mod.get_global_var('func_6163')
var_6165 = relay.var("var_6165", dtype = "uint16", shape = (1, 6, 8))#candidate|6165|(1, 6, 8)|var|uint16
var_6166 = relay.var("var_6166", dtype = "uint16", shape = (2, 6, 8))#candidate|6166|(2, 6, 8)|var|uint16
var_6167 = relay.var("var_6167", dtype = "uint16", shape = (9, 6, 8))#candidate|6167|(9, 6, 8)|var|uint16
call_6164 = func_6163_call(var_6165,var_6166,var_6167,)
output = call_6164
func_6168 = relay.Function([var_6165,var_6166,var_6167,], output)
mutated_mod['func_6168'] = func_6168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5991_call = mod.get_global_var('func_5991')
func_5992_call = mutated_mod.get_global_var('func_5992')
call_6340 = relay.TupleGetItem(func_5991_call(), 0)
call_6341 = relay.TupleGetItem(func_5992_call(), 0)
func_5876_call = mod.get_global_var('func_5876')
func_5879_call = mutated_mod.get_global_var('func_5879')
var_6359 = relay.var("var_6359", dtype = "int16", shape = (65,))#candidate|6359|(65,)|var|int16
var_6360 = relay.var("var_6360", dtype = "int16", shape = (585,))#candidate|6360|(585,)|var|int16
call_6358 = relay.TupleGetItem(func_5876_call(relay.reshape(var_6359.astype('int16'), [1, 5, 13]), relay.reshape(var_6360.astype('int16'), [9, 5, 13]), ), 0)
call_6361 = relay.TupleGetItem(func_5879_call(relay.reshape(var_6359.astype('int16'), [1, 5, 13]), relay.reshape(var_6360.astype('int16'), [9, 5, 13]), ), 0)
func_2297_call = mod.get_global_var('func_2297')
func_2303_call = mutated_mod.get_global_var('func_2303')
const_6366 = relay.const([[8],[1],[-3],[1],[-2],[8],[-8],[4],[-8],[10],[-1],[-5],[-7],[-1],[-1],[-3],[8],[10],[-7],[-3],[-7],[-2],[1],[-7],[-4],[-8],[1],[4],[-10],[-8],[8],[1],[-7],[7],[1],[5],[-2],[-1],[5],[-2],[6],[-2],[1],[5],[-10],[2],[6],[6],[-4],[7],[5],[-3],[1],[10],[3],[-4],[1],[-8],[-1],[4],[7],[3],[-1],[5],[2],[-1],[6],[-5],[-8],[-2],[8],[2],[2],[-2],[2],[-6],[3],[-10],[-8],[10],[-1],[-10],[6],[5],[-2],[-7],[-2],[10],[6],[9],[-9],[6],[-6],[-6],[5],[8],[-10],[-4],[-4],[2],[-5],[6],[7],[-3],[9],[2],[-7],[-2],[7],[9],[8],[10],[6],[4],[-3],[3],[5],[-7],[-7],[-7],[10],[-8],[10],[-4],[-10],[10],[2],[5],[6],[-5],[-8],[-10],[10],[-7],[-6],[7],[4],[7],[-5],[-10],[5],[2],[2],[3],[-9],[-10],[9],[-9],[-5],[-9],[-1],[-1],[2],[-6],[10],[-4],[5],[-2],[3],[6],[6],[-8],[6],[-7],[6],[-6],[-2],[9],[-6],[1],[-2],[-10],[-10],[6],[10],[7],[8],[2],[-7],[-6],[4],[-7],[6],[10],[-2],[9],[5],[10],[4],[9],[6],[1],[-3],[9],[-3],[-2],[-5],[-3],[4],[5],[4],[9],[5],[-3],[5],[-2],[-9],[-6],[-7],[4],[-10],[-7],[5],[7],[1],[7],[-6],[-5],[6],[-10],[1],[2],[7],[6],[-5],[-2],[-7],[9],[8],[3],[-8],[7],[7],[-6],[9],[5],[-10],[-9],[7],[8],[6],[-6],[-10],[-6],[10],[10],[-8],[-3],[6],[-9],[7],[-4],[-1],[1],[10],[9],[-1],[8],[-7],[-10],[4],[5],[6],[6],[-9],[-6],[8],[-3],[-4],[-6],[-6],[-10],[-9],[10],[5],[-3],[1],[-10],[9],[-8],[2],[5],[5],[1],[-4],[4],[2],[-1],[-6],[-7],[3],[1],[-9],[9],[-10],[6],[-1],[4],[-1],[-7],[-9],[-7],[7],[-2],[-8],[-8],[-8],[-5],[2],[4],[-10],[-4],[1],[9],[2],[-9],[7],[4],[5],[-10],[2],[6],[-5],[-6],[4],[8],[2],[5],[9],[-7],[9],[2],[1],[1],[9],[-9],[-7],[2],[5],[-10],[-9],[2],[-10],[5],[2],[10],[6],[-7],[-5],[3],[10],[-6],[10],[-9],[-5],[-5],[-9],[6],[-6],[9],[-2],[9],[-9],[7],[5],[-10],[5],[-1],[6],[-9],[1],[7],[-10],[9],[3],[6],[-5],[3],[1],[7],[-1],[2],[5],[-8],[-5],[1],[-2],[-6],[-9],[-10],[3],[10],[-1],[1],[3],[10],[7],[10],[5],[-2],[-7],[-8],[1],[-3],[1],[5],[-9],[3],[7],[2],[3],[6],[5],[-1],[-3],[3],[-6],[-1],[7],[7],[7],[-3],[6],[6],[9],[3],[-1],[-2],[-4],[9],[8],[9],[2],[-10],[6],[-8],[-1],[1],[6],[-1],[7],[-7],[-5],[-7],[1],[-6],[7],[-2],[-7],[-10],[2],[-6],[-9],[-2],[-6],[4],[-1],[4],[-9],[6],[-4],[-1],[-10],[-9],[-7],[-10],[7],[6],[4],[-4],[3],[4],[8],[-9],[-6],[9],[7],[-2],[-4],[6],[2],[-4],[3],[-6],[8],[-5],[-6],[4],[-6],[3],[7],[-5],[-3],[-3],[-10],[2],[-6],[-10],[6],[6],[-3],[-4],[2],[5],[10],[2],[-1],[4],[-2],[2],[-8],[3],[-1],[-3],[-8],[-1],[-1],[-2],[-3],[-1],[-6],[-10],[9],[-2],[1],[-4],[-8],[-2],[-1],[-6],[-3],[-10],[5],[7],[10],[3],[-2],[6],[7]], dtype = "int16")#candidate|6366|(539, 1)|const|int16
const_6367 = relay.const([-0.684932,-5.324895,7.379930,2.153487,6.703310,-9.495559,-1.289686,0.867874,8.554702,9.126344,5.749515,-7.699673,-9.563792,-6.706233,2.365374,-7.583691,2.896305,9.537370,7.923809,6.412393,7.738689,4.351975,6.167180,4.471878,-5.349365,5.934546,4.994300,-4.763423,-0.943308,6.439675,7.455715,7.041967,-9.756610,0.748652,-4.339245,-5.853338,-4.023350,6.647838,-2.259091,3.405335,3.079118,2.358102,-3.652569,5.702484,-1.262376,-8.609961,-3.631442,-4.250859,7.005787,7.479160,5.002716,9.930562,1.423398,1.751848,2.584370,3.981699,3.924451,3.143833,-5.591439,-0.350701,5.863572,-6.526939,3.654332,-3.151103,-2.222838,-2.488720,-5.636977,-0.047461,-3.515903,4.174616,-4.109713,-1.784265,1.583105,3.379811,-3.077983,9.991797,0.120976,-7.370823,-4.109308,5.231999,-7.001175,-7.674435,2.341793,-0.048470,-5.233767,-7.225451,-1.193466,-9.221165,-2.532631,-0.750112,-8.273298,4.196345,5.191532,-3.970973,-5.698889,1.992721,6.645409,3.784827,-9.189307,-5.146449,-6.462902,2.776926,1.986973,-4.494236,1.887184,9.388379,-5.653900,5.818375,-3.195675,-0.666194,2.701463,4.743197,8.977295,-7.387906,-6.556659,9.060083,4.416949,-4.843674,-8.002949,-4.914334,3.854549,1.677832,-6.706989,5.754601,-7.799221,-7.347404,1.155901,-7.359961,-9.896953,-6.624836,9.070297,8.077690,-8.178996,-4.794420,0.593449,6.043337,-0.056589,-3.904479,3.122893,9.843709,8.060622,-8.243059,5.061932,-8.892229,0.598220,-6.052486,-9.533317,0.026125,2.679340,9.763714,-4.564948,0.490329,-7.378551,-3.139248,-5.794308,0.339571,2.977627,-4.912094,6.523836,-1.231311,-8.630404,5.588147,1.697811,2.135027,-8.800097,1.779875,6.669727,3.599083,-7.685645,-0.860713,1.903705,2.701420,5.368452,4.466283,-2.420780,1.748929,8.353421,5.719937,0.700761,6.877209,5.254223,-9.325849,-6.766130,-0.236483,1.955838,7.107781,5.322829,9.072315,-0.462965,8.497918,2.698418,9.180603,2.307957,6.407682,-9.607822,3.924361,5.760016,-7.428081,0.029617,-1.388656,5.885472,-9.452442,-2.913104,2.895742,-8.655457,4.980133,3.900239,-7.437808,6.963387,5.915059,4.355719,-3.817359,0.967210,-8.297489,6.791783,7.304725,-1.701339,6.186492,-5.117761,4.931854,6.567534,-1.596641,-4.031780,-8.761776,-4.121501,1.506102,-4.582722,-0.642658,-3.589485,-1.768062,1.776606,8.032782,5.959045,7.935365,3.995551,6.948747,8.865409,-8.798560,-0.460797,-9.559141,-2.975189,-3.067231,4.195546], dtype = "float32")#candidate|6367|(243,)|const|float32
var_6368 = relay.var("var_6368", dtype = "float32", shape = (720,))#candidate|6368|(720,)|var|float32
const_6369 = relay.const([-10,10,6,4,-8,8,-5,3,2,-4,6,8,8,-5,2,10,6,-9,-5,-2,-1,-8,-5,-8,3,-2,7,4,-7,-8,8,-3,7,9,-5,6,3,2,-4,-7,-2,5,-10,-7,-9,6,-4,-4,-10,-4,3,-1,-3,-4,-3,4,-9,-5,10,-6,8,6,2,2,2,9,3,10,4,2,7,5,7,-5,-1,-5,4,10,1,9,9,9,-7,9,-4,-1,9,5,5,4,-2,6,2,9,9,7,6,-9,4,6,-8,-9,10,-4,5,-2,9,-2,-3,2,-8,9,6,7,-3,10,-10,10,-6,-5,-4,-7,-5,2,9,-8,-5,-1,5,3,-10,3,3,-10,-8,9,3,3,-6,-4,10,-1,10,-8,-1,7,5,3,-1,-6,-9,-3,2,10,2,4,-9,9,-9,6,-9,5,-1,3,-1,-3,7,-5,-1,-8,1,4,-6,-1,9,9,10,-3,10,5,8,-6,-5,3,-7,10,2,-10,-7,5,8,-6,-6,9,9,-1,-3,2,-9,-5,-8,6,9,8,7,-1,-7,-1,-10,-1,6,5,-1,7,-6,6,-7,3,8,-1,-7,10,-1,-9,3,9,-3,9,3,-2,10,2,10,-3,-9,1,-7,1,2,-9,9,-4,-4,4,9,-8,-6,6,6,-2,4,-2,-4,8,-1,3,-5,-2,-8,-8,-4,5,5,-6,1,-7,-1,3,-1,5,10,-4,5,-5,4,-1,8,-8,7,7,2,-2,-4,-10,8,9,-3,4,-8,-10,-2,1,-7,6,-3,-4,6,7,3,-7,3,10,6,2,4,-6,-3,10,-6,-5,-9,3,5,7,9,8,9,-8,5,-9,-1,7,2,5,-6,-6,-7,4,2,9,-7,-3,-8,-1,10,2,-5,-9,-10,4,3,3,-2,4,-10,5,-2,2,-9,3,-3,3,5,6,6,-1,1,-1,-3,-6,7,-10,10,-7,7,10,-4,-7,-5,-4,4,-10,-1,9,-5,7,-8,9,9,9,-7,-5,2,-1,6,7,-3,6,-7,10,-1,2,-3,9,10,-9,7,-9,7,-5,9,4,9,8,4,8,2,-5,4,9,2,-10,-2,-9,2,4,5,3,-10,2,6,1,3,-5,10,10,1,-2,-10,4,4,-3,-7,-5,-7,3,10,-3,10,7,-1,-1,-6,3,-3,-9,-4,5,1,10,-8,5,-7,-10,-6,4,-3,-8,-9,8,10,8], dtype = "int64")#candidate|6369|(462,)|const|int64
call_6365 = relay.TupleGetItem(func_2297_call(relay.reshape(const_6366.astype('int16'), [7, 11, 7]), relay.reshape(const_6366.astype('int16'), [7, 11, 7]), relay.reshape(const_6367.astype('float32'), [243,]), relay.reshape(var_6368.astype('float32'), [720,]), relay.reshape(const_6369.astype('int64'), [462,]), ), 3)
call_6370 = relay.TupleGetItem(func_2303_call(relay.reshape(const_6366.astype('int16'), [7, 11, 7]), relay.reshape(const_6366.astype('int16'), [7, 11, 7]), relay.reshape(const_6367.astype('float32'), [243,]), relay.reshape(var_6368.astype('float32'), [720,]), relay.reshape(const_6369.astype('int64'), [462,]), ), 3)
func_4017_call = mod.get_global_var('func_4017')
func_4020_call = mutated_mod.get_global_var('func_4020')
var_6377 = relay.var("var_6377", dtype = "int64", shape = (78,))#candidate|6377|(78,)|var|int64
call_6376 = func_4017_call(relay.reshape(var_6377.astype('int64'), [3, 13, 2]))
call_6378 = func_4017_call(relay.reshape(var_6377.astype('int64'), [3, 13, 2]))
output = relay.Tuple([call_6340,call_6358,var_6359,var_6360,call_6365,const_6366,const_6367,var_6368,const_6369,call_6376,var_6377,])
output2 = relay.Tuple([call_6341,call_6361,var_6359,var_6360,call_6370,const_6366,const_6367,var_6368,const_6369,call_6378,var_6377,])
func_6386 = relay.Function([var_6359,var_6360,var_6368,var_6377,], output)
mod['func_6386'] = func_6386
mod = relay.transform.InferType()(mod)
var_6387 = relay.var("var_6387", dtype = "int16", shape = (65,))#candidate|6387|(65,)|var|int16
var_6388 = relay.var("var_6388", dtype = "int16", shape = (585,))#candidate|6388|(585,)|var|int16
var_6389 = relay.var("var_6389", dtype = "float32", shape = (720,))#candidate|6389|(720,)|var|float32
var_6390 = relay.var("var_6390", dtype = "int64", shape = (78,))#candidate|6390|(78,)|var|int64
output = func_6386(var_6387,var_6388,var_6389,var_6390,)
func_6391 = relay.Function([var_6387,var_6388,var_6389,var_6390,], output)
mutated_mod['func_6391'] = func_6391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_6439 = relay.TupleGetItem(func_5448_call(), 0)
call_6440 = relay.TupleGetItem(func_5450_call(), 0)
var_6442 = relay.var("var_6442", dtype = "float64", shape = (1008, 3))#candidate|6442|(1008, 3)|var|float64
bop_6443 = relay.equal(call_6439.astype('bool'), var_6442.astype('bool')) # shape=(1008, 3)
bop_6446 = relay.equal(call_6440.astype('bool'), var_6442.astype('bool')) # shape=(1008, 3)
output = relay.Tuple([bop_6443,])
output2 = relay.Tuple([bop_6446,])
func_6447 = relay.Function([var_6442,], output)
mod['func_6447'] = func_6447
mod = relay.transform.InferType()(mod)
var_6448 = relay.var("var_6448", dtype = "float64", shape = (1008, 3))#candidate|6448|(1008, 3)|var|float64
output = func_6447(var_6448)
func_6449 = relay.Function([var_6448], output)
mutated_mod['func_6449'] = func_6449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_6451 = relay.TupleGetItem(func_5448_call(), 0)
call_6452 = relay.TupleGetItem(func_5450_call(), 0)
func_1084_call = mod.get_global_var('func_1084')
func_1087_call = mutated_mod.get_global_var('func_1087')
var_6456 = relay.var("var_6456", dtype = "int64", shape = (462,))#candidate|6456|(462,)|var|int64
call_6455 = func_1084_call(relay.reshape(var_6456.astype('int64'), [7, 6, 11]))
call_6457 = func_1084_call(relay.reshape(var_6456.astype('int64'), [7, 6, 11]))
bop_6465 = relay.greater(var_6456.astype('bool'), relay.reshape(call_6455.astype('bool'), relay.shape_of(var_6456))) # shape=(462,)
bop_6468 = relay.greater(var_6456.astype('bool'), relay.reshape(call_6457.astype('bool'), relay.shape_of(var_6456))) # shape=(462,)
func_5043_call = mod.get_global_var('func_5043')
func_5046_call = mutated_mod.get_global_var('func_5046')
const_6474 = relay.const([True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False], dtype = "bool")#candidate|6474|(2048,)|const|bool
call_6473 = relay.TupleGetItem(func_5043_call(relay.reshape(const_6474.astype('bool'), [16, 16, 8])), 1)
call_6475 = relay.TupleGetItem(func_5046_call(relay.reshape(const_6474.astype('bool'), [16, 16, 8])), 1)
output = relay.Tuple([call_6451,bop_6465,call_6473,const_6474,])
output2 = relay.Tuple([call_6452,bop_6468,call_6475,const_6474,])
func_6483 = relay.Function([var_6456,], output)
mod['func_6483'] = func_6483
mod = relay.transform.InferType()(mod)
var_6484 = relay.var("var_6484", dtype = "int64", shape = (462,))#candidate|6484|(462,)|var|int64
output = func_6483(var_6484)
func_6485 = relay.Function([var_6484], output)
mutated_mod['func_6485'] = func_6485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5587_call = mod.get_global_var('func_5587')
func_5588_call = mutated_mod.get_global_var('func_5588')
call_6550 = func_5587_call()
call_6551 = func_5587_call()
var_6559 = relay.var("var_6559", dtype = "bool", shape = (16, 16, 8))#candidate|6559|(16, 16, 8)|var|bool
bop_6560 = relay.less(call_6550.astype('bool'), relay.reshape(var_6559.astype('bool'), relay.shape_of(call_6550))) # shape=(16, 16, 8)
bop_6563 = relay.less(call_6551.astype('bool'), relay.reshape(var_6559.astype('bool'), relay.shape_of(call_6551))) # shape=(16, 16, 8)
output = bop_6560
output2 = bop_6563
func_6564 = relay.Function([var_6559,], output)
mod['func_6564'] = func_6564
mod = relay.transform.InferType()(mod)
var_6565 = relay.var("var_6565", dtype = "bool", shape = (16, 16, 8))#candidate|6565|(16, 16, 8)|var|bool
output = func_6564(var_6565)
func_6566 = relay.Function([var_6565], output)
mutated_mod['func_6566'] = func_6566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_6601 = relay.TupleGetItem(func_5448_call(), 0)
call_6602 = relay.TupleGetItem(func_5450_call(), 0)
uop_6603 = relay.rsqrt(call_6601.astype('float32')) # shape=(1008, 1)
uop_6605 = relay.rsqrt(call_6602.astype('float32')) # shape=(1008, 1)
func_5768_call = mod.get_global_var('func_5768')
func_5773_call = mutated_mod.get_global_var('func_5773')
var_6613 = relay.var("var_6613", dtype = "uint32", shape = (864,))#candidate|6613|(864,)|var|uint32
var_6614 = relay.var("var_6614", dtype = "int64", shape = ())#candidate|6614|()|var|int64
const_6615 = relay.const([-9,2,-2,-5,-5,2,10,2,4,-3,-3,-6,2,3,-4,-3,-7,8,-6,-6,2,2,7,-7,8,-5,5,-8,-5,8,1,-2,-4,10,3,-10,3,-8,-6,9,-5,2,8,-6,-3,2,-6,2,5,10,5,-5,-4,9,8,-1,-6,2,5,7,-4,1,3,8,3,-8,-7,-9,7,-10,-7,7,-6,-7,7,-10,-1,9,-4,4,6,-8,-8,-6,6,-8,-7,-8,4,-5], dtype = "int64")#candidate|6615|(90,)|const|int64
call_6612 = relay.TupleGetItem(func_5768_call(relay.reshape(var_6613.astype('uint32'), [9, 16, 6]), relay.reshape(var_6614.astype('int64'), []), relay.reshape(const_6615.astype('int64'), [90,]), ), 3)
call_6616 = relay.TupleGetItem(func_5773_call(relay.reshape(var_6613.astype('uint32'), [9, 16, 6]), relay.reshape(var_6614.astype('int64'), []), relay.reshape(const_6615.astype('int64'), [90,]), ), 3)
output = relay.Tuple([uop_6603,call_6612,var_6613,var_6614,const_6615,])
output2 = relay.Tuple([uop_6605,call_6616,var_6613,var_6614,const_6615,])
func_6618 = relay.Function([var_6613,var_6614,], output)
mod['func_6618'] = func_6618
mod = relay.transform.InferType()(mod)
mutated_mod['func_6618'] = func_6618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6618_call = mutated_mod.get_global_var('func_6618')
var_6620 = relay.var("var_6620", dtype = "uint32", shape = (864,))#candidate|6620|(864,)|var|uint32
var_6621 = relay.var("var_6621", dtype = "int64", shape = ())#candidate|6621|()|var|int64
call_6619 = func_6618_call(var_6620,var_6621,)
output = call_6619
func_6622 = relay.Function([var_6620,var_6621,], output)
mutated_mod['func_6622'] = func_6622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5239_call = mod.get_global_var('func_5239')
func_5240_call = mutated_mod.get_global_var('func_5240')
call_6649 = relay.TupleGetItem(func_5239_call(), 0)
call_6650 = relay.TupleGetItem(func_5240_call(), 0)
uop_6651 = relay.exp(call_6649.astype('float32')) # shape=(14, 9, 8)
uop_6653 = relay.exp(call_6650.astype('float32')) # shape=(14, 9, 8)
uop_6658 = relay.tan(uop_6651.astype('float64')) # shape=(14, 9, 8)
uop_6660 = relay.tan(uop_6653.astype('float64')) # shape=(14, 9, 8)
uop_6665 = relay.cos(uop_6658.astype('float32')) # shape=(14, 9, 8)
uop_6667 = relay.cos(uop_6660.astype('float32')) # shape=(14, 9, 8)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_6691 = relay.TupleGetItem(func_4460_call(), 0)
call_6692 = relay.TupleGetItem(func_4461_call(), 0)
func_6483_call = mod.get_global_var('func_6483')
func_6485_call = mutated_mod.get_global_var('func_6485')
var_6707 = relay.var("var_6707", dtype = "int64", shape = (462,))#candidate|6707|(462,)|var|int64
call_6706 = relay.TupleGetItem(func_6483_call(relay.reshape(var_6707.astype('int64'), [462,])), 2)
call_6708 = relay.TupleGetItem(func_6485_call(relay.reshape(var_6707.astype('int64'), [462,])), 2)
output = relay.Tuple([uop_6665,call_6691,call_6706,var_6707,])
output2 = relay.Tuple([uop_6667,call_6692,call_6708,var_6707,])
func_6710 = relay.Function([var_6707,], output)
mod['func_6710'] = func_6710
mod = relay.transform.InferType()(mod)
var_6711 = relay.var("var_6711", dtype = "int64", shape = (462,))#candidate|6711|(462,)|var|int64
output = func_6710(var_6711)
func_6712 = relay.Function([var_6711], output)
mutated_mod['func_6712'] = func_6712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5519_call = mod.get_global_var('func_5519')
func_5521_call = mutated_mod.get_global_var('func_5521')
call_6839 = relay.TupleGetItem(func_5519_call(), 0)
call_6840 = relay.TupleGetItem(func_5521_call(), 0)
output = relay.Tuple([call_6839,])
output2 = relay.Tuple([call_6840,])
func_6846 = relay.Function([], output)
mod['func_6846'] = func_6846
mod = relay.transform.InferType()(mod)
output = func_6846()
func_6847 = relay.Function([], output)
mutated_mod['func_6847'] = func_6847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5917_call = mod.get_global_var('func_5917')
func_5919_call = mutated_mod.get_global_var('func_5919')
call_6910 = func_5917_call()
call_6911 = func_5917_call()
func_5814_call = mod.get_global_var('func_5814')
func_5817_call = mutated_mod.get_global_var('func_5817')
const_6914 = relay.const([-9.138618,-3.228100,4.878700,3.877249,-4.086662,2.340482,-5.651858,-4.729437,6.861842,-4.936300,-8.999573,-1.708062,-8.567936,-9.044065,7.129486,8.048175,-2.792427,1.104569,7.258785,-0.398883,9.277688,3.478068,-8.171912,-5.501324,6.473161,-7.171045,3.113708,8.126353,4.390868,8.895648,6.249797,2.080047,0.161265,8.410877,8.679415,-4.181353,5.451322,-9.023480,2.799149,6.774418,3.754288,7.802413,-7.270080,-8.005117,-0.958699,0.360629,9.357318,5.027119,2.783842,7.242887,-4.103193,8.826351,1.906380,1.618840,0.452793,-8.772500,-6.353005,3.435995,-9.654502,2.318050,8.463456,2.228696,7.954759,0.801804,5.658480,8.289760,-1.398203,-8.472658,-2.170350,2.040965,-9.605357,5.269306,2.686867,-5.602391,-3.718533,-7.606358,-9.644514,-7.180270,-4.849173,-1.764378,4.797064,1.358326,4.725610,5.471160,9.465652,3.086247,-2.339162,7.370813,0.829244,-5.569913,7.470530,8.680329,-3.172118,1.339852,-4.793563,-6.269954,5.458782,4.957621,0.021705,-8.013380,9.223239,5.534808,-5.961089,4.918864,-8.393018,-7.196565,-4.356873,9.812234,9.248321,3.704079,-1.067460,8.870969,2.280197,-4.014768,-1.629192,-9.333291,-7.141395,7.066759,-5.913197,-4.566368,-8.637754,-5.720088,7.853827,7.455329,-9.691197,-0.586395,7.372330,-0.818142,-7.671090,0.667922,8.875828,0.663237,9.001927,4.676034,9.859668,-7.019083,-3.723768,2.339291,-8.210727,-7.632495,6.097959,-1.331838,4.505390,-6.364546,9.611063,-9.577344,2.767647,4.516084,-0.491309,-7.073634,-4.511565,-7.433099,2.542398,-0.974430,-4.637741,-8.218415,7.173750,-1.491986,9.201017,8.641557,7.570149,3.561366,3.912884,3.893062,5.737678,0.910477,8.059138,-4.665973,3.256917,-9.568871,-5.707147,-1.143345,3.215311,-0.995409,4.609443,-8.337423,8.874015,3.215359,-6.707735,-2.587470,-1.591380,3.582565,4.598273,-5.110550,5.620663,4.671551,7.520002,7.801557,-8.157054,1.780458,1.611015,-8.585854,7.086700,0.546668,4.214816,-4.937461,-6.671911,5.799827,3.125471,-5.683808,-0.212319,-9.996280,7.250931,9.184907,4.188818,3.813377,-9.345619,4.106752,4.004214,0.651603,9.501579,-5.427252,3.883060,5.063106,2.572945,2.282801,3.544763,5.521617,-9.730654,7.588763,3.685997,-6.609520,-2.743501,-8.967691,7.284334,-4.239443,7.796400,-4.338386,-4.983029,9.760327,2.331830,-7.600258,8.004880,-2.048181,-7.648466,2.570027,-1.294152,8.386076,-4.476037,9.688375,7.529377,-6.359083,-6.847858,9.400314,-2.976513,7.770436,-2.613279,8.153060,3.601809,5.434711,0.599285,-2.741994,-4.398271,-4.310588,6.659428,-7.526923,-6.529393,6.427773,9.628957,0.521604,6.701074,-8.651174,-9.644431,4.765397,0.534050,5.159849,-7.221533,-4.708861,3.733426,2.016270,-0.395412,3.373701,-5.008492,-1.612932,-9.329607,5.637808,-3.207748,8.644998,9.793085,-7.148008,3.212008,0.144082,2.637617,-8.277488,4.262709,0.578992,-0.684309,-5.759537,4.643089,-3.363967,-4.099037,-4.238564,7.577229,-3.893268,-0.801966,8.463022,-8.568256,5.780087,6.696560,0.055451,8.582523,-5.508454,2.175455,-6.673802,6.688751,-2.195983,4.769165,-6.800932,-0.994969,0.060857,-6.326835,-8.130257,-6.104686,-8.160968,-2.150204,-3.747783,0.095874,3.755547,9.712050,8.047085,-7.678215,-7.198563,-3.027974,6.215166,0.303594,-6.578153,6.806970,3.293262,-4.957466,6.096252,5.418607,1.405121,2.052128,0.076622,-2.645019,3.454000,3.175792,-4.969092,7.636891,-9.667471,2.888221,-9.102401,-9.246155,-5.014501,0.612439,3.314215,4.433188,3.922774,4.602935,2.881818,-4.928905,-8.496275,-3.165314,3.497256,-2.451241,9.710425,-5.638830,8.348776,8.279242,-5.540031,0.377910,4.133384,-7.780169,8.878832,5.044551,5.923144,-2.768863,3.882944,0.460801,-5.735415,5.703208,3.602988,9.301948,-4.946843,-5.807701,0.379760,-5.383286,-2.837356,-0.067357,-8.818415,-0.054345,0.636410,4.786428,5.436458,7.023375,4.909896,5.139781,1.583436,7.562173,1.281957,-8.510538,6.190725,6.921142,2.727922,-7.384263,-1.263751,8.505527,4.264602,-6.290213,3.684912,-3.990672,-9.367017,9.278601,-3.261451,0.176296,-3.392102,-4.929246,-6.295177,4.400579,3.780297,0.094004,-9.955484,0.643960,-3.943911,5.228416,-7.854403,-6.333368,7.737240,-8.028766,-2.990471,-5.098453,1.122952,-4.448240,-6.929176,6.052449,7.238386,3.059051,8.922191,5.799805,3.035400,-8.686687,-8.025616,-1.679625,-4.678816,0.124638,0.362562,-5.584377,8.707984,-1.845323,-5.583343,4.124284,9.753338,-6.117466,-2.016261,-9.445676,-0.560299,0.750026,8.903627,-5.227078,-4.407723,-1.290696,6.897747,-2.032193,9.620824,1.917835,-8.983334,-4.525029,6.145217,-9.604394,-3.875578,7.532960,6.697527,-2.526112,4.636844,9.888562,-5.126543,5.157716,-6.512614,-4.356452,-6.864417,1.768916,0.585301,-2.649682,-5.167096,-0.411219,7.120128,0.048624,-0.895412,9.271548,6.624625,8.615871,-1.265244,4.026553,-9.695454,1.342798,3.719028,3.539698,-4.270114,-1.988294,-6.314795,3.048422,-4.097278,3.718128,-5.719145,-2.173994,8.624536,-9.210895,-4.639210,-2.607685,7.757923,-9.472115,-6.955753,1.027006,8.119564,-0.450192,-1.432190,-2.193932,-4.453789,0.851018,-7.376163,-7.462194,8.666158,-2.409767,0.896746,-6.122058,-6.531115,5.981273,-0.604523,2.879951,-6.216208,-5.981827,9.237969,-0.355156,-6.831588,6.860463,8.146851,-3.323628,-9.875045,6.511611,8.850712,-1.996820,-8.834811,-4.605206,7.878874,-8.115989,9.771580,-1.012824,8.298724,0.625466,0.623862,3.775301,-7.221312,5.871560,-9.671386,-6.614113,2.251580,1.165731,3.557108,-5.992689,1.720095,-4.704153,1.564276,5.843890,7.444105,-3.322921,1.490444,-4.319054,3.625270,-4.610485,-3.990635,1.554372,-9.471127,5.267447,2.811315,-3.218273,-0.335341,0.269986,9.876693,4.982612,2.332688,1.926280,9.900852,1.608263,-4.688929,-3.429072,-9.417920,-5.699378,-8.197784,-3.431951,3.326635,-7.572343,-9.373946,-9.007223,-7.396211,-6.875268,3.386170,3.777211,6.608722,-6.558994,-4.925868,-0.248158,-8.628478,4.258544,-2.822984,-4.700732,-8.613991,-0.562434,3.136089,3.892324,-6.330399,1.731735,9.304982,-5.217826,1.734058,-4.955812,9.436716,4.778446,6.585486,-8.011170,-6.268848,-0.105256,2.034727,4.010748,0.644319,-0.510932,7.890508,1.222298,-3.545748,2.156983,-9.941470,-8.428298,1.766437,-9.279821,-6.070390,-0.367457,0.362360,-3.993253,5.025390,7.367891,-2.085167,-8.210713,-5.217922,-5.696473,2.270998,-5.679849,-7.816683,5.551344,-8.861232,-9.056521,-8.355694,-9.493007,6.560220,-8.872799,-9.385219,6.723101,-9.749887,-7.263914,-9.046511,3.559547,6.640397,3.276329,-9.052302,3.381706,-7.009590,-1.950317,-8.800448,5.690259,5.914758,0.732140,6.294710,-1.016210,-9.426392,-0.255233,2.396973,1.335750,-1.728253,-1.609013,0.841955,8.560073,-8.023620,3.677575,-5.704908,-2.985148,-2.763280,-8.145160,6.062802,6.469419,8.123319,-1.865121,-3.073717,7.716004,-0.792463,7.156606,9.537609,-7.227492,-2.844840,1.547924,-4.557241,-8.612350,7.909208,-6.138750,1.810396,-2.780453,-0.003581,-5.346500,-4.286307,0.254454,1.892422,7.221789,6.546947,-2.038352,7.783690,4.299942,-7.770207,-6.347409,-5.956787,-8.224123,1.746223,-4.517586,3.979970,-9.671665,8.302893,-1.755905,-1.475618,7.042904,9.607367,-9.889143,4.074388,-8.097335,4.930703,3.960440,-7.859081,-9.027658,3.562538,8.532743,2.187237,-0.474313,4.286884,7.441175,-0.546753,4.859671,2.072308,-5.793827,0.693551,-0.135860,-7.960722,-7.867072,5.798643,-1.123742,-5.983886,3.493652,8.217676,-6.284533,-4.802192,-2.033700,-9.257221,1.004384,1.729418,3.473783,-5.827658,-9.228155,6.864283,6.140485,9.704656,3.836055,8.452360,0.113942,4.860006,3.141140,2.514200,-8.160488,-9.719376,5.996974,-7.831284,-6.224788,-7.560913,8.678251,-0.052793,-4.546276,-0.272706,4.101114,-4.861791,-2.095940,-8.772488,-9.813921,1.436044,8.049647,-5.696301,-9.504456,0.909260,4.732991,8.875167,-6.959491,-3.122024,2.533966,-5.013217,-1.575395,1.197045,-1.502482,4.430922,2.671310,-3.812548,-3.489118,-7.112911,7.373553,7.490715,8.145982,2.020188,-3.768394,7.212998,-6.984978,-2.150671,-2.648178,8.457606,1.555959,5.560177,7.841184,-2.555931,-6.496952,-7.099242,-6.442098,5.481530,-6.480962,0.006519,-9.433046,-4.091384,5.963511,0.986720,-9.747456,-6.867794,3.201011,4.875236,2.173505,-2.374804,-9.036585,5.478705,6.628524,-6.126789,8.230828,-8.899968,-2.436742,-7.714959,-1.907681,-0.976624,-3.884087,-9.091573,-4.209213,9.829033,3.783619,-8.439913,-7.619044,1.536576,-1.250621,-3.704908,9.175164,5.618822,8.607558,0.773020,7.886307,5.943110,3.473960,-8.954900,9.395832,7.221374,5.658357,-1.535669,-6.693657,9.064600,5.162058,-3.199874,2.658353,5.451091,-5.125429,-3.239697,-2.248668,7.723997,3.524370,9.210317,3.373555,-5.879606,-8.774361,8.214210,-3.480253,4.909798,-9.567850,-8.473160,6.118197,-2.966843,2.822177,-9.660097,-8.760291,5.008171], dtype = "float32")#candidate|6914|(882,)|const|float32
call_6913 = relay.TupleGetItem(func_5814_call(relay.reshape(const_6914.astype('float32'), [882,])), 5)
call_6915 = relay.TupleGetItem(func_5817_call(relay.reshape(const_6914.astype('float32'), [882,])), 5)
output = relay.Tuple([call_6910,call_6913,const_6914,])
output2 = relay.Tuple([call_6911,call_6915,const_6914,])
func_6916 = relay.Function([], output)
mod['func_6916'] = func_6916
mod = relay.transform.InferType()(mod)
output = func_6916()
func_6917 = relay.Function([], output)
mutated_mod['func_6917'] = func_6917
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6920 = relay.var("var_6920", dtype = "float32", shape = (9, 7, 11))#candidate|6920|(9, 7, 11)|var|float32
uop_6921 = relay.sigmoid(var_6920.astype('float32')) # shape=(9, 7, 11)
uop_6925 = relay.sin(uop_6921.astype('float32')) # shape=(9, 7, 11)
func_5964_call = mod.get_global_var('func_5964')
func_5965_call = mutated_mod.get_global_var('func_5965')
call_6927 = relay.TupleGetItem(func_5964_call(), 0)
call_6928 = relay.TupleGetItem(func_5965_call(), 0)
output = relay.Tuple([uop_6925,call_6927,])
output2 = relay.Tuple([uop_6925,call_6928,])
func_6931 = relay.Function([var_6920,], output)
mod['func_6931'] = func_6931
mod = relay.transform.InferType()(mod)
var_6932 = relay.var("var_6932", dtype = "float32", shape = (9, 7, 11))#candidate|6932|(9, 7, 11)|var|float32
output = func_6931(var_6932)
func_6933 = relay.Function([var_6932], output)
mutated_mod['func_6933'] = func_6933
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7013 = relay.var("var_7013", dtype = "float64", shape = (16, 5, 15))#candidate|7013|(16, 5, 15)|var|float64
uop_7014 = relay.exp(var_7013.astype('float64')) # shape=(16, 5, 15)
output = uop_7014
output2 = uop_7014
func_7020 = relay.Function([var_7013,], output)
mod['func_7020'] = func_7020
mod = relay.transform.InferType()(mod)
var_7021 = relay.var("var_7021", dtype = "float64", shape = (16, 5, 15))#candidate|7021|(16, 5, 15)|var|float64
output = func_7020(var_7021)
func_7022 = relay.Function([var_7021], output)
mutated_mod['func_7022'] = func_7022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_7053 = relay.TupleGetItem(func_5092_call(), 0)
call_7054 = relay.TupleGetItem(func_5094_call(), 0)
output = call_7053
output2 = call_7054
func_7057 = relay.Function([], output)
mod['func_7057'] = func_7057
mod = relay.transform.InferType()(mod)
mutated_mod['func_7057'] = func_7057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7057_call = mutated_mod.get_global_var('func_7057')
call_7058 = func_7057_call()
output = call_7058
func_7059 = relay.Function([], output)
mutated_mod['func_7059'] = func_7059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_7063 = relay.TupleGetItem(func_4460_call(), 0)
call_7064 = relay.TupleGetItem(func_4461_call(), 0)
func_5587_call = mod.get_global_var('func_5587')
func_5588_call = mutated_mod.get_global_var('func_5588')
call_7087 = func_5587_call()
call_7088 = func_5587_call()
uop_7092 = relay.erf(call_7063.astype('float64')) # shape=(9, 16, 6)
uop_7094 = relay.erf(call_7064.astype('float64')) # shape=(9, 16, 6)
output = relay.Tuple([call_7087,uop_7092,])
output2 = relay.Tuple([call_7088,uop_7094,])
func_7096 = relay.Function([], output)
mod['func_7096'] = func_7096
mod = relay.transform.InferType()(mod)
output = func_7096()
func_7097 = relay.Function([], output)
mutated_mod['func_7097'] = func_7097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6846_call = mod.get_global_var('func_6846')
func_6847_call = mutated_mod.get_global_var('func_6847')
call_7129 = relay.TupleGetItem(func_6846_call(), 0)
call_7130 = relay.TupleGetItem(func_6847_call(), 0)
output = relay.Tuple([call_7129,])
output2 = relay.Tuple([call_7130,])
func_7135 = relay.Function([], output)
mod['func_7135'] = func_7135
mod = relay.transform.InferType()(mod)
mutated_mod['func_7135'] = func_7135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7135_call = mutated_mod.get_global_var('func_7135')
call_7136 = func_7135_call()
output = call_7136
func_7137 = relay.Function([], output)
mutated_mod['func_7137'] = func_7137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_7145 = func_5171_call()
call_7146 = func_5171_call()
output = relay.Tuple([call_7145,])
output2 = relay.Tuple([call_7146,])
func_7179 = relay.Function([], output)
mod['func_7179'] = func_7179
mod = relay.transform.InferType()(mod)
output = func_7179()
func_7180 = relay.Function([], output)
mutated_mod['func_7180'] = func_7180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4763_call = mod.get_global_var('func_4763')
func_4764_call = mutated_mod.get_global_var('func_4764')
call_7194 = func_4763_call()
call_7195 = func_4763_call()
output = relay.Tuple([call_7194,])
output2 = relay.Tuple([call_7195,])
func_7198 = relay.Function([], output)
mod['func_7198'] = func_7198
mod = relay.transform.InferType()(mod)
output = func_7198()
func_7199 = relay.Function([], output)
mutated_mod['func_7199'] = func_7199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6040_call = mod.get_global_var('func_6040')
func_6041_call = mutated_mod.get_global_var('func_6041')
call_7205 = func_6040_call()
call_7206 = func_6040_call()
func_3320_call = mod.get_global_var('func_3320')
func_3325_call = mutated_mod.get_global_var('func_3325')
var_7227 = relay.var("var_7227", dtype = "int32", shape = (3, 42))#candidate|7227|(3, 42)|var|int32
const_7228 = relay.const([[3],[6],[3],[-1],[7],[-5],[5],[-4],[10],[-9],[-3],[-5],[-2],[9],[-1],[4],[4],[-10],[-6],[-10],[-8],[1],[-7],[-2],[-7],[7],[-4],[8],[-5],[3],[-1],[-10],[8],[2],[8],[-7],[8],[-2],[3],[4],[-5],[-1],[1],[-8],[-6],[4],[7],[-4],[1],[1],[9],[6],[7],[4],[3],[1],[-7],[8],[2],[8],[-4],[-5],[4],[6],[-5],[-5],[-4],[-2],[2],[-1],[2],[-1],[-6],[10],[-5],[-6],[-1],[-10],[2],[10],[-2],[4],[9],[-6],[-1],[-6],[-3],[-3],[7],[7]], dtype = "int64")#candidate|7228|(90, 1)|const|int64
var_7229 = relay.var("var_7229", dtype = "int16", shape = (224,))#candidate|7229|(224,)|var|int16
call_7226 = relay.TupleGetItem(func_3320_call(relay.reshape(var_7227.astype('int32'), [3, 6, 7]), relay.reshape(const_7228.astype('int64'), [90,]), relay.reshape(var_7229.astype('int16'), [16, 14]), ), 9)
call_7230 = relay.TupleGetItem(func_3325_call(relay.reshape(var_7227.astype('int32'), [3, 6, 7]), relay.reshape(const_7228.astype('int64'), [90,]), relay.reshape(var_7229.astype('int16'), [16, 14]), ), 9)
output = relay.Tuple([call_7205,call_7226,var_7227,const_7228,var_7229,])
output2 = relay.Tuple([call_7206,call_7230,var_7227,const_7228,var_7229,])
func_7233 = relay.Function([var_7227,var_7229,], output)
mod['func_7233'] = func_7233
mod = relay.transform.InferType()(mod)
mutated_mod['func_7233'] = func_7233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7233_call = mutated_mod.get_global_var('func_7233')
var_7235 = relay.var("var_7235", dtype = "int32", shape = (3, 42))#candidate|7235|(3, 42)|var|int32
var_7236 = relay.var("var_7236", dtype = "int16", shape = (224,))#candidate|7236|(224,)|var|int16
call_7234 = func_7233_call(var_7235,var_7236,)
output = call_7234
func_7237 = relay.Function([var_7235,var_7236,], output)
mutated_mod['func_7237'] = func_7237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5620_call = mod.get_global_var('func_5620')
func_5622_call = mutated_mod.get_global_var('func_5622')
call_7275 = relay.TupleGetItem(func_5620_call(), 0)
call_7276 = relay.TupleGetItem(func_5622_call(), 0)
output = relay.Tuple([call_7275,])
output2 = relay.Tuple([call_7276,])
func_7277 = relay.Function([], output)
mod['func_7277'] = func_7277
mod = relay.transform.InferType()(mod)
mutated_mod['func_7277'] = func_7277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7277_call = mutated_mod.get_global_var('func_7277')
call_7278 = func_7277_call()
output = call_7278
func_7279 = relay.Function([], output)
mutated_mod['func_7279'] = func_7279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7277_call = mod.get_global_var('func_7277')
func_7279_call = mutated_mod.get_global_var('func_7279')
call_7301 = relay.TupleGetItem(func_7277_call(), 0)
call_7302 = relay.TupleGetItem(func_7279_call(), 0)
output = relay.Tuple([call_7301,])
output2 = relay.Tuple([call_7302,])
func_7343 = relay.Function([], output)
mod['func_7343'] = func_7343
mod = relay.transform.InferType()(mod)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7343_call = mutated_mod.get_global_var('func_7343')
call_7344 = func_7343_call()
output = call_7344
func_7345 = relay.Function([], output)
mutated_mod['func_7345'] = func_7345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_7383 = relay.TupleGetItem(func_5448_call(), 0)
call_7384 = relay.TupleGetItem(func_5450_call(), 0)
uop_7387 = relay.atanh(call_7383.astype('float64')) # shape=(1008, 1)
uop_7389 = relay.atanh(call_7384.astype('float64')) # shape=(1008, 1)
bop_7394 = relay.right_shift(uop_7387.astype('int64'), relay.reshape(call_7383.astype('int64'), relay.shape_of(uop_7387))) # shape=(1008, 1)
bop_7397 = relay.right_shift(uop_7389.astype('int64'), relay.reshape(call_7384.astype('int64'), relay.shape_of(uop_7389))) # shape=(1008, 1)
uop_7398 = relay.log2(call_7383.astype('float64')) # shape=(1008, 1)
uop_7400 = relay.log2(call_7384.astype('float64')) # shape=(1008, 1)
const_7421 = relay.const([[-6.221945,-8.170519],[4.531736,-6.389269],[-6.884138,9.645829],[-4.959730,-1.925363],[4.388277,-7.807798],[2.853068,-8.697150],[7.683093,3.973000],[1.181929,-0.974441],[-2.837615,6.329376],[-0.865360,-6.386240],[6.099534,-7.028154],[8.006942,-8.238640],[4.063838,-6.887846],[-3.363613,3.932179],[-3.549667,3.830118],[-4.056569,1.609498],[8.552002,-9.053497],[-6.823594,-5.959356],[-0.171197,3.048500],[-7.174484,7.727479],[-7.546715,-8.287553],[-9.091259,-1.637245],[-7.322405,-2.643527],[5.346970,5.358690],[-5.894560,-6.244094],[9.738035,1.681604],[-3.729892,1.022468],[-9.876541,-1.471950],[-0.043966,2.284700],[-0.353127,9.662336],[-6.933533,1.695269],[7.859471,-4.756024],[5.131981,4.535245],[0.384881,-4.462024],[2.010023,-4.351978],[-6.329463,1.781293],[4.466481,5.755090],[-4.102281,3.596768],[-6.363105,7.240924],[4.259205,-7.996548],[-4.431196,9.616476],[-5.180089,3.746924],[0.756975,9.903502],[-1.285305,0.047175],[5.916806,-1.751895],[3.851363,-7.083070],[-2.294848,-2.819884],[9.039036,-1.658173],[-9.205132,-4.038867],[-9.890491,-8.844771],[0.882038,9.768179],[-8.290467,-0.874058],[-1.734776,-3.572817],[-4.026188,2.377545],[-4.833594,-1.343388],[-9.546986,8.675398],[2.135941,5.741595],[-4.230700,2.088014],[0.622743,5.338160],[8.482737,-5.949245],[-2.749004,-3.485355],[6.221941,-4.984579],[1.983381,-6.779008],[6.918340,-1.429206],[5.303958,-8.029029],[0.172723,5.160079],[7.491037,1.465243],[-0.444029,-4.389817],[-7.069625,2.990431],[-2.305037,6.797360],[7.143032,-0.527135],[3.891152,3.212995],[-8.393566,-0.662402],[3.238585,4.975628],[4.767371,-4.586106],[-7.541392,-9.422245],[2.012591,-6.853621],[1.304189,9.507819],[7.068807,-8.497190],[-4.360804,8.362898],[0.437140,-3.463072],[-2.099886,1.352974],[-3.062566,7.031346],[-3.835150,2.647484],[-0.314771,-7.315095],[9.232036,-7.024606],[8.215241,-9.011569],[-3.124394,-2.836291],[5.946322,-9.123679],[-7.151465,1.989054],[1.410050,8.269641],[9.746417,4.556731],[8.491844,5.140337],[7.864678,7.770800],[-9.830818,-5.735518],[-0.941928,8.718062],[-1.090856,2.485078],[3.921851,7.784890],[6.880303,9.877603],[-3.410575,-8.066589],[-6.391712,-9.766514],[5.204898,-9.701712],[0.664497,-9.400206],[8.549393,-3.418024],[-6.677215,3.239795],[-8.031050,-2.750509],[3.722364,-0.165116],[4.464811,0.043773],[5.918248,7.676027],[-7.553718,-9.830210],[8.525174,1.911492],[-0.239793,-0.960035],[1.665283,8.525503],[-3.938243,8.244232],[8.966702,9.447382],[2.581297,-0.914911],[9.684479,1.511977],[8.009761,0.085418],[1.864122,8.464090],[-1.179099,-6.629747],[7.916731,-4.302220],[7.486895,-5.962230],[1.005252,9.082686],[-4.956530,1.575768],[-0.606087,4.577303],[6.517356,-4.986050],[0.629230,-7.438314],[3.019647,9.948685],[-3.300029,-6.075826],[-8.018201,-6.478247],[2.096967,-0.404740],[3.598603,6.615486],[-2.694414,6.429204],[3.877628,-5.437247],[-1.152481,4.788691],[5.418033,-0.962842],[-8.758977,-3.534832],[2.747419,-8.837337],[-2.117185,4.868696],[2.254365,7.663411],[7.496086,4.714650],[-5.107469,-9.401411],[-5.826220,-0.904606],[-2.821542,-5.034710],[-8.019126,3.209473],[4.809072,-5.792278],[-8.827761,-7.885341],[-0.599975,-7.680121],[-8.126184,-4.914401],[5.048889,9.273182],[-1.518593,-8.954608],[1.031885,9.434519],[0.603454,6.107226],[9.953919,-3.073599],[6.089020,3.953952],[1.055266,-2.004597],[3.275624,-7.366232],[1.666232,-1.381482],[-4.786459,-2.907344],[5.236098,9.372581],[7.224932,-3.704633],[-9.092011,-3.583484],[4.630890,1.752376],[8.322701,-2.231883],[-4.837877,-5.378196],[3.751924,-4.150759],[6.019797,6.320714],[-3.276314,3.005946],[5.740830,-5.044197],[-0.793261,-8.604665],[-0.351046,-7.286858],[8.155280,-1.194034],[-1.122799,4.400798],[-2.928626,8.758520],[-8.448316,-2.747221],[3.169846,-9.809499],[8.434220,-8.340405],[-2.479610,8.013548],[-7.492769,-1.822444],[9.575335,7.488097],[4.519879,0.662508],[-5.048259,6.713673],[9.762282,-5.835856],[1.967136,3.967965],[2.718329,5.661546],[-1.641085,8.795102],[-7.192620,-4.647431],[-9.265634,8.960717],[-7.272913,7.888347],[0.497909,-0.357810],[8.558873,1.929905],[7.877038,1.123215],[-3.094989,-6.339679],[-6.548764,2.238367],[-0.071329,-1.607614],[-2.311684,-4.402868],[-6.767509,0.846569],[7.230980,-2.028931],[-9.593477,5.004556],[-6.718527,4.060762],[0.706202,-1.161115],[2.965511,4.704928],[0.996818,-5.373397],[5.286213,5.827331],[3.844614,-7.655883],[-4.961190,4.382740],[-6.536849,-9.125913],[1.707949,-7.016569],[-7.840654,-5.863028],[-6.111536,2.492421],[2.819657,1.979143],[-8.382531,-2.740524],[-8.613719,-8.254493],[9.028343,7.215994],[9.959167,4.403721],[5.977810,9.728955],[-1.879065,1.030614],[7.503107,-5.109340],[8.581967,-7.581835],[-0.260902,9.781793],[4.963186,7.200976],[4.232907,-7.806145],[5.052238,0.319363],[4.826912,-2.661073],[0.789215,5.025114],[-7.038281,2.743541],[2.444230,8.927384],[8.821387,-8.165046],[9.522132,8.157105],[7.370447,0.513098],[7.501728,0.232887],[7.615113,-5.880509],[-6.988628,-6.590507],[-2.219220,-0.181162],[9.222416,1.621326],[-5.223252,8.296929],[-5.900409,-3.697120],[-4.516423,-0.490094],[-6.397099,1.811119],[3.745284,-9.217360],[2.182949,-9.676258],[3.798484,7.335262],[-1.605738,7.808996],[1.123668,-6.707282],[7.784187,9.353606],[-9.978200,-1.624170],[5.724725,8.023065],[3.011097,-3.580735],[-9.266358,-4.597449],[2.046175,-6.150688],[8.170816,-0.045386],[-3.188861,-8.643421],[6.140413,9.705487],[6.900790,4.429319],[0.165457,3.404266],[-4.172925,9.510202],[-6.268625,-9.177732],[-2.621890,9.822262],[-9.550808,-2.985006],[0.288242,9.535462],[-2.784852,-6.187720],[-0.477701,-1.051304],[-5.577379,-6.829273],[-8.242958,6.595869],[-9.895673,-9.725985],[-3.964584,-1.593322],[-6.533377,8.091715],[9.977852,-7.477386],[-2.941881,4.303693],[-0.925721,-5.431956],[6.467990,-5.988868],[5.429235,-0.760678],[5.149651,-7.359138],[-6.686081,6.934663],[7.952054,-1.788507],[5.633653,-7.465724],[-6.296826,-7.894275],[1.252192,2.783483],[7.796016,-7.699979],[-0.571361,-8.204470],[-4.930811,6.178646],[0.962960,7.653026],[-9.831321,0.154763],[-5.502892,3.196908],[4.597472,-0.207195],[-1.495351,3.376013],[9.556634,-3.349870],[-1.837777,6.830551],[7.473371,-0.319076],[5.804434,3.749162],[6.162967,7.963295],[-9.997309,-2.044923],[-3.695273,5.552721],[7.909948,0.176912],[-6.007354,-4.452521],[-9.458536,6.969001],[-5.606283,5.522085],[1.592495,2.916977],[1.740262,7.082694],[5.149477,-5.892518],[-6.510129,2.566935],[-4.259586,-7.405602],[-8.587280,-7.838317],[-4.568076,7.430358],[3.280477,6.215563],[5.599465,1.302674],[0.442044,8.732283],[7.954965,1.475869],[2.870972,3.145465],[4.042724,-8.180763],[-2.645701,-7.602277],[1.012622,0.766515],[-3.364322,7.064484],[-0.446209,4.446135],[5.671041,-8.879269],[-8.856354,-2.377316],[-7.360415,8.170277],[6.507127,-4.165140],[-9.314010,0.735108],[-2.173800,-1.291410],[4.425822,-7.414670],[8.900235,4.967541],[-7.917262,7.703340],[6.615028,-1.056144],[8.605341,7.392928],[-0.039562,-2.939237],[7.057265,-2.769793],[-1.631551,-9.246699],[-2.745735,9.343751],[-5.355219,6.874130],[9.181275,3.743314],[-4.542391,-8.677352],[-7.156710,4.246448],[1.178558,8.704941],[5.741759,-7.166907],[8.761591,2.033102],[-0.610787,2.447535],[0.136452,4.778201],[6.335081,-9.317216],[5.001187,3.904735],[-8.843859,-9.728671],[-9.752192,-7.105895],[8.081299,8.583258],[-5.075672,-7.898911],[-8.457837,9.580473],[-2.859053,-4.050049],[-8.238255,-3.995187],[8.364346,1.167991],[-8.075239,-7.917508],[1.095920,-9.984968],[8.119819,2.086500],[-4.442954,-9.763701],[4.815111,-7.485049],[6.642536,5.188318],[8.536141,6.734876],[9.221140,7.265534],[-4.127192,-1.153179],[-5.146806,-4.595140],[6.288105,9.530315],[7.707803,-4.979705],[-2.451289,0.390201],[4.066908,2.642117],[-3.058119,4.967782],[7.833066,8.432710],[-9.371480,3.974918],[-5.008452,9.550890],[-3.632322,7.312910],[-9.012232,-8.972125],[-9.707850,-0.703101],[8.903421,1.249512],[-8.504740,4.060513],[6.789393,1.871635],[1.430417,-4.394768],[-8.184047,6.139543],[5.563671,0.310000],[-2.164264,-3.963901],[7.125162,-1.875974],[-7.721477,-4.069682],[-4.910412,-8.784381],[-1.518051,-4.972559],[-1.868268,0.514836],[-9.039622,2.394072],[7.889647,0.331901],[5.730080,-4.695882],[3.573097,5.580198],[-1.960038,-2.166912],[3.371927,-2.307350],[4.621364,6.295094],[-5.458916,-4.122508],[5.377862,-1.338002],[-3.961189,-4.471259],[3.165877,-2.025712],[1.407242,-6.705423],[3.877955,9.468781],[2.710119,-2.961785],[-7.478158,-3.553033],[-1.723499,1.577128],[8.102375,-7.900898],[5.984556,5.043271],[-6.645206,3.716298],[8.886947,0.331774],[3.322167,2.647499],[1.240856,5.281256],[-9.131383,-3.769674],[-9.146572,-1.376519],[7.294465,-9.406461],[-3.723569,3.431514],[1.061990,-4.722936],[-1.363243,-5.129449],[-3.209593,-5.116924],[1.052053,2.094340],[2.648806,9.254851],[3.870400,6.728763],[-3.063521,-0.324212],[7.239770,1.655531],[-9.003958,5.665659],[-5.542901,-3.883060],[-4.554296,-5.683023],[-4.209904,6.815278],[9.117055,-7.816468],[-0.093529,8.542934],[5.074523,3.209673],[7.099480,0.360917],[1.072183,-2.378173],[-0.378272,-8.018330],[5.356511,5.352908],[9.549908,6.250046],[0.740841,7.280859],[-5.170969,-9.978226],[-0.282279,-2.483418],[2.931332,-5.440352],[5.536990,-9.510845],[4.316909,-6.357198],[2.252138,0.006619],[-2.150768,1.322512],[-8.501320,3.956177],[9.200191,-4.080639],[-7.607514,4.225763],[-2.127854,-2.745083],[-3.425493,-0.250991],[3.460328,-0.143519],[-7.490702,9.540380],[-0.336632,-8.640863],[-2.612748,3.563399],[0.581222,3.070655],[0.158047,2.102407],[-8.295029,2.668203],[-4.974147,4.212221],[-4.641205,-2.180832],[9.252626,1.843001],[-1.002404,-0.334974],[8.007281,-1.959442],[1.694614,-1.392787],[-9.151165,-6.980940],[4.885742,5.297067],[4.591750,-7.299461],[-8.416950,-6.211939],[-8.081919,-4.222761],[6.809594,6.752798],[-7.752283,-4.624469],[-1.511915,-6.157386],[-5.650912,0.956141],[-4.869168,-7.712949],[3.428817,0.632018],[6.159301,6.567761],[0.459645,2.525135],[-8.724612,-5.726507],[-6.896658,-2.885399],[8.119261,-8.744953],[-7.524075,-2.949680],[-5.568299,-9.761935],[7.436365,-4.321172],[-9.481543,-8.865045],[0.442363,-6.973447],[9.175308,-5.211219],[9.970360,-2.406396],[-7.726796,2.688149],[-4.860444,3.785965],[-8.869682,6.167710],[-6.189585,-1.202096],[4.104234,-2.927557],[-0.316844,7.629777],[5.301150,-0.653399],[-8.471375,-8.475955],[3.788349,8.138899],[9.039310,-8.071160],[6.880884,4.083035],[6.064195,-8.730882],[-0.155520,3.697127],[9.975156,-3.215372],[2.531528,-5.035640],[7.030009,-4.952833],[-9.321786,8.731486],[-9.493456,5.863266],[7.518903,0.713430],[-3.651280,6.412091],[2.486010,-4.829577],[0.526518,4.454095],[5.916194,9.299126],[-3.817165,7.485792],[4.798665,-4.758947],[-0.033526,0.241192],[-2.730245,4.438487],[-6.967393,-1.981117],[1.440657,4.338560],[2.412148,6.549956],[-0.620249,-8.493025],[-6.334777,6.366993],[-2.780260,-2.977885],[0.923845,-3.121764],[-8.990628,-1.646584],[-3.704108,-7.657406],[7.759200,3.195340],[0.269045,4.192211],[3.990956,-3.672999],[2.978770,8.212409],[-0.615299,0.826513],[-3.435057,0.079677],[0.242627,3.948265],[-7.222673,5.877744],[0.614465,7.139271],[-9.940128,-1.533469],[-9.543226,6.630946],[-9.183248,2.497668],[-4.764579,-9.245074],[-2.836912,-2.574224],[-1.089415,5.827611],[1.040900,-6.784871],[5.240954,2.003481],[1.279715,4.668718],[3.892140,5.591211],[-5.652316,-1.211126],[8.856876,2.587074],[-8.281609,5.111990],[0.739127,-0.394067],[-2.911583,-8.830868],[-9.272239,5.701084],[1.744769,5.465635],[2.208867,9.084086],[6.331170,2.272645],[-4.066718,-5.621646],[-9.586181,9.540262],[-5.599041,-9.095349],[1.447982,3.860209],[6.544899,3.028812],[4.237155,2.293064],[1.133994,-8.562868],[-5.204913,-0.835318],[-9.694160,2.226224],[-5.124306,0.856951],[-6.694103,6.927376],[-9.144273,7.576682],[5.467524,-1.893678],[2.029555,-1.623431],[-6.570385,6.197991],[-1.191845,-0.840227],[-8.101408,7.602762],[-5.423709,-4.300330],[-3.000822,-3.249475],[-3.811624,-5.973966],[-4.401833,-8.845403],[-4.692910,1.071374],[-7.848122,2.496610],[-7.562041,6.160396],[-7.770229,8.994754],[7.671726,8.024020],[-7.676239,-1.982896],[-6.944023,-8.798802],[-4.137202,-2.347852],[8.110785,4.382056],[6.929774,-2.046819],[-0.112255,-8.833779],[-7.641002,-8.406792],[7.655266,-0.568343],[0.637320,-7.634215],[9.926181,0.040237],[-1.603061,4.189671],[7.124036,8.407427],[9.498522,-4.849018],[8.230308,-5.573277],[-9.236526,-9.526681],[7.596175,5.768534],[9.228990,-6.540974],[6.017736,-0.700657],[7.886816,4.006274],[1.439941,7.344914],[8.411964,-4.407067],[3.175691,-1.013599],[9.326840,0.271984],[4.979826,-5.107815],[7.602727,-3.986240],[-5.286955,-9.204586],[-9.258459,-7.525502],[-8.060376,-1.769396],[4.484488,-0.014277],[-9.893913,-9.875953],[1.080375,-3.025610],[9.764304,-4.571548],[7.231364,0.078403],[0.075078,8.185691],[4.891598,6.669253],[-5.053246,0.746850],[4.443586,-3.491702],[6.622786,5.838098],[-7.653324,5.478345],[-2.460942,-7.266575],[-5.787235,0.638847],[0.879013,1.473162],[-7.395657,-8.310762],[5.730734,-7.221064],[-0.509279,-4.323269],[-5.138486,-8.228239],[3.600440,-4.812398],[4.619154,5.528855],[-2.599769,-7.137990],[6.852499,-2.140025],[-4.431034,-2.476185],[1.288487,-7.437476],[1.757705,4.898820],[4.878191,9.744066],[0.560743,-5.232586],[-4.840199,9.083663],[3.871123,8.275281],[9.438676,-1.241563],[-0.765420,3.531462],[-0.718048,4.474431],[-5.604087,1.198623],[8.173058,-7.556938],[-2.073081,1.907505],[-6.561103,6.427144],[-9.891671,0.526552],[-0.001576,-8.691964],[-7.210132,-8.760326],[3.346936,7.231938],[-1.933301,1.875409],[6.079214,5.177824],[7.791808,-9.806180],[0.559682,6.618424],[-3.974765,4.547815],[-6.569152,-8.197404],[-0.506664,4.826529],[-1.122757,9.027281],[4.364970,-1.029796],[7.345438,-8.484706],[3.235011,-4.233132],[-5.252837,-5.960058],[-6.405206,-8.642389],[6.039435,-7.257526],[3.293999,-8.784907],[-8.794505,7.400916],[-2.929362,-8.970795],[1.266145,-5.354493],[0.819490,6.991503],[-0.658867,7.350140],[0.507627,-7.172281],[-6.929131,-7.829573],[-3.716219,2.176112],[0.380065,3.848607],[9.763194,0.822264],[-3.339869,9.003493],[-8.598484,-9.363564],[-5.681358,-2.392315],[6.301779,1.668804],[4.221902,6.409399],[-9.712446,-0.014832],[3.317541,7.155019],[0.985148,0.851009],[9.451126,0.572880],[7.366743,-5.078536],[4.766825,-8.674449],[3.280453,-4.934480],[0.472794,6.002213],[7.508732,2.258294],[4.276217,0.576142],[8.840659,-2.330798],[4.221144,7.241617],[6.039087,-0.822282],[-1.450457,3.290676],[-4.528247,-9.896559],[-0.404503,9.151229],[0.917292,-9.415090],[-9.710090,3.908551],[2.688656,-6.992423],[2.371503,2.670791],[1.380152,-4.938056],[-7.101062,-6.771447],[4.997998,5.174543],[-1.155039,7.497468],[7.903843,-7.294426],[8.976995,-6.457619],[5.934642,5.765161],[-3.945706,-3.570576],[0.428969,5.179629],[-4.008107,-3.626139],[-0.546124,4.529758],[3.238945,-0.499358],[7.237475,-7.203357],[-1.397420,3.978074],[7.473829,-7.625648],[9.934875,3.915879],[2.436113,4.605741],[-1.660126,-3.403845],[6.767834,6.558327],[-3.618571,6.776759],[-1.973689,6.446127],[-7.828911,4.603143],[5.747079,5.530635],[-6.253724,4.290720],[4.549640,5.085054],[4.414038,-7.272199],[-5.959263,3.617836],[8.692137,-4.260303],[-4.229979,-5.729603],[-3.998604,-2.588053],[-0.147789,-9.182217],[-5.086252,-0.344879],[-2.967098,-9.922819],[5.849027,-7.258919],[-6.761539,5.933205],[7.928991,-6.422502],[1.096994,-7.339388],[-5.054121,7.117146],[0.484278,1.001377],[-9.706717,9.347560],[4.617616,-3.217852],[8.716980,-4.545770],[-9.105049,8.123174],[3.891292,0.280671],[7.934335,-8.861252],[-3.019326,-6.306413],[-4.600669,0.733443],[7.787025,0.594545],[-7.438842,-5.233721],[3.337586,-1.465866],[-8.122564,1.292044],[2.292328,-0.476396],[-8.161768,-8.059924],[-4.277293,-6.235304],[-7.004873,7.808092],[8.629738,-8.297081],[-6.593918,6.439318],[-1.306156,4.142744],[7.987301,-6.646439],[2.823857,7.622916],[-2.718782,-7.152702],[-9.885419,2.532135],[4.607257,1.746872],[0.845903,-2.036213],[-6.601004,7.220801],[0.032780,8.387507],[6.740136,6.056368],[-3.589785,9.568862],[-5.110008,6.102472],[-8.729198,1.087278],[-3.670687,-5.056691],[7.708247,2.298559],[-2.230300,-9.800438],[-4.692704,1.923157],[9.907819,-6.958025],[6.111281,-9.297187],[-8.505783,9.264640],[-3.121104,-0.485803],[0.540383,4.334859],[1.097759,-9.687442],[2.401626,-9.400123],[-0.415958,-2.014843],[-1.109011,4.795138],[-6.174150,-6.056614],[7.087939,9.584795],[-8.621506,-0.818580],[9.618929,-3.293528],[3.220388,-9.805787],[9.430047,-2.044909],[-8.777259,-9.370826],[5.875890,7.693387],[3.594866,-5.025942],[1.325293,9.940986],[5.780862,7.840180],[4.868102,-1.573942],[-8.433719,2.738693],[1.449409,5.880425],[-1.698807,-2.195902],[4.337740,4.296582],[5.841287,6.939978],[-8.185369,3.363369],[4.836621,-9.081011],[-2.110182,3.184288],[4.379782,2.234839],[-0.640818,9.782799],[-2.351446,-2.034724],[6.219123,-6.351326],[-2.522873,6.102411],[-0.992513,-6.731595],[5.882447,-8.987093],[2.072732,-8.945599],[2.988571,4.600707],[-5.467744,-0.665946],[2.034235,-3.999924],[0.014885,4.474682],[-1.681794,-4.565121],[4.287604,-4.609483],[8.560308,8.695359],[-9.080164,0.976218],[9.479676,5.664579],[8.015744,-7.438498],[1.382989,1.473420],[1.724688,-4.805502],[3.725721,6.674579],[0.233757,2.024709],[-7.320395,-5.658007],[-1.168787,-4.109482],[-8.417538,5.928696],[-5.723905,-0.777654],[-9.361818,-8.356422],[3.804875,-3.728480],[8.832747,4.952891],[6.553679,3.265711],[7.683118,6.551819],[2.144748,0.687724],[3.113560,-7.582636],[-6.461541,3.368218],[-5.536085,0.946300],[-5.608681,2.758737],[2.744259,0.531469],[1.440145,-8.375206],[-6.876796,2.476099],[-3.381248,5.306233],[2.907994,7.390923],[9.064629,8.375526],[-1.777130,1.021698],[-8.084730,-6.223183],[0.647855,-4.728163],[-1.058037,-9.338812],[-3.183862,-1.932651],[-2.424443,0.355881],[7.341369,-6.392408],[4.829161,8.425755],[-9.393768,1.078879],[1.538469,-5.105164],[4.145849,6.375849],[3.203093,-8.999308],[7.119838,-0.855143],[-7.952480,-6.807025],[-5.064208,-2.316388],[-0.257914,7.119204],[-1.411271,5.996189],[-6.052082,5.744459],[-0.616986,2.700971],[-8.641279,-3.579595],[4.545475,3.383356],[-3.011845,5.803422],[-4.338244,-8.354076],[7.384238,2.051383],[-0.137455,3.018075],[-3.591512,-7.987264],[-3.027929,0.347637],[1.250814,-6.419796],[-4.118055,1.654121],[5.345619,-7.251643],[-0.327414,-5.447887],[-1.199128,-0.892707],[-3.905570,-0.792184],[-8.266568,-6.747353],[-9.704756,4.576349],[0.504823,-9.045902],[6.595340,-1.536622],[6.275575,6.853634],[9.956224,0.775551],[5.436149,8.864751],[-9.652453,9.965230],[-7.260089,3.543467],[2.167332,2.113823],[-2.093952,-5.263118],[5.108456,5.176546],[7.425011,-4.689993],[-1.809100,8.727870],[0.229362,-7.415807],[-9.062106,-4.185634],[0.708185,3.774109],[-8.032409,0.311061],[8.391949,2.894919],[-1.751845,3.566824],[4.140381,-3.001016],[4.445609,1.652900],[-9.969163,-2.263991],[4.724219,-9.979833],[-4.932242,2.421211],[-0.101557,-1.114033],[3.810910,-0.254695],[-7.669534,9.085525],[9.057997,5.193607],[4.293854,-1.993973],[-8.459281,-0.104521],[3.425341,-8.778094],[5.276874,9.223537],[-9.049287,8.091774],[2.865000,7.700423],[5.194999,6.246749],[9.732655,1.525094],[6.331804,-4.149051],[9.375296,-3.654857],[9.786376,-6.533226],[-0.658605,-7.937581],[1.165681,-6.602796],[5.695263,-1.134973],[5.374545,-2.207237],[4.884781,7.106137],[4.258132,-7.582162],[1.325015,6.317027],[-0.021008,5.071306],[5.399834,1.354166],[2.299937,1.145841],[-9.062393,7.594050],[7.635415,-8.280471],[9.868096,-7.240259],[5.740272,2.016914],[6.972947,-6.092313],[2.999258,-2.632199],[0.231061,7.423774],[-8.566834,-1.874838],[0.035943,-0.395202],[6.806539,4.251596],[-5.912313,5.778255],[-3.741540,-7.212238],[3.883894,1.162804],[-8.024993,-1.776513],[-5.773061,-2.859667],[-0.325880,8.200784],[-5.691621,5.181474],[-1.285275,1.873351],[-8.331927,-5.431538],[5.076125,-1.645401],[7.324698,3.345181],[6.724535,-1.205060],[-3.541219,-8.194393],[5.596105,-4.520966],[7.055835,3.987905],[-3.965800,5.944441],[1.712344,2.554504],[-4.552746,4.278698],[-9.389037,-0.235723],[-0.577598,6.269955],[5.472198,-2.944789],[6.848515,9.142264],[-9.587361,-5.133326],[2.482673,5.260960],[6.537423,6.847008],[-6.466500,-4.687464],[-2.920417,-8.228761],[1.402941,8.032624],[-8.604705,2.710647],[-4.579466,-0.681117],[2.850924,0.621446],[-6.433817,7.375274],[7.305876,-4.028023],[5.003640,-0.464849],[2.827672,6.168102],[-0.297390,5.508516],[-7.579188,-0.536539],[7.835765,6.371166],[8.806246,5.576262],[2.003244,-1.138175],[-6.289044,-3.682022],[1.773824,3.073610],[5.379531,4.947918],[4.428040,-4.129200],[5.523008,-9.965006],[-0.831787,8.619993],[-4.031003,7.408746],[6.768679,-2.720850],[-0.114253,6.421957],[-4.775283,-4.255363],[1.076870,2.155579],[2.659039,-2.686044],[0.072096,9.841713],[-0.355007,3.572538],[-0.906466,-1.323926],[-5.736499,0.211415],[0.858855,-8.124662],[3.620855,-6.527947],[-5.213540,4.383780],[7.627481,-4.361099],[-7.299108,-8.602397],[-2.553559,9.313426],[8.162817,-7.397316],[-0.548686,-2.010327],[6.853182,0.172926],[-4.273890,3.233599],[-0.676707,-0.208904],[3.006967,-3.465020],[-2.794135,-5.946455],[-2.608480,8.336586],[-1.818261,-9.441106],[2.495068,-6.770029],[0.833424,0.037936],[5.153046,0.681121],[2.244757,-3.535625],[-8.979310,-6.098094],[1.287615,-4.893716],[-6.173936,2.237887],[2.620429,-5.393778],[4.587770,1.638297],[-3.621318,-9.479260],[-7.742190,3.602802],[4.685803,-9.277893],[-3.957753,-2.562995],[5.831527,-9.458526],[6.025785,-9.698605]], dtype = "float64")#candidate|7421|(1008, 2)|const|float64
bop_7422 = relay.logical_xor(uop_7398.astype('uint8'), const_7421.astype('uint8')) # shape=(1008, 2)
bop_7425 = relay.logical_xor(uop_7400.astype('uint8'), const_7421.astype('uint8')) # shape=(1008, 2)
bop_7433 = relay.add(uop_7398.astype('float32'), relay.reshape(bop_7394.astype('float32'), relay.shape_of(uop_7398))) # shape=(1008, 1)
bop_7436 = relay.add(uop_7400.astype('float32'), relay.reshape(bop_7397.astype('float32'), relay.shape_of(uop_7400))) # shape=(1008, 1)
output = relay.Tuple([bop_7422,bop_7433,])
output2 = relay.Tuple([bop_7425,bop_7436,])
func_7441 = relay.Function([], output)
mod['func_7441'] = func_7441
mod = relay.transform.InferType()(mod)
output = func_7441()
func_7442 = relay.Function([], output)
mutated_mod['func_7442'] = func_7442
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7443 = relay.var("var_7443", dtype = "float32", shape = (7, 12, 2))#candidate|7443|(7, 12, 2)|var|float32
uop_7444 = relay.acosh(var_7443.astype('float32')) # shape=(7, 12, 2)
output = uop_7444
output2 = uop_7444
func_7450 = relay.Function([var_7443,], output)
mod['func_7450'] = func_7450
mod = relay.transform.InferType()(mod)
mutated_mod['func_7450'] = func_7450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7451 = relay.var("var_7451", dtype = "float32", shape = (7, 12, 2))#candidate|7451|(7, 12, 2)|var|float32
func_7450_call = mutated_mod.get_global_var('func_7450')
call_7452 = func_7450_call(var_7451)
output = call_7452
func_7453 = relay.Function([var_7451], output)
mutated_mod['func_7453'] = func_7453
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7563 = relay.var("var_7563", dtype = "int16", shape = ())#candidate|7563|()|var|int16
var_7564 = relay.var("var_7564", dtype = "int16", shape = (3, 15, 11))#candidate|7564|(3, 15, 11)|var|int16
bop_7565 = relay.less(var_7563.astype('bool'), var_7564.astype('bool')) # shape=(3, 15, 11)
output = relay.Tuple([bop_7565,])
output2 = relay.Tuple([bop_7565,])
func_7582 = relay.Function([var_7563,var_7564,], output)
mod['func_7582'] = func_7582
mod = relay.transform.InferType()(mod)
var_7583 = relay.var("var_7583", dtype = "int16", shape = ())#candidate|7583|()|var|int16
var_7584 = relay.var("var_7584", dtype = "int16", shape = (3, 15, 11))#candidate|7584|(3, 15, 11)|var|int16
output = func_7582(var_7583,var_7584,)
func_7585 = relay.Function([var_7583,var_7584,], output)
mutated_mod['func_7585'] = func_7585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7441_call = mod.get_global_var('func_7441')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_7591 = relay.TupleGetItem(func_7441_call(), 1)
call_7592 = relay.TupleGetItem(func_7442_call(), 1)
func_2040_call = mod.get_global_var('func_2040')
func_2044_call = mutated_mod.get_global_var('func_2044')
var_7594 = relay.var("var_7594", dtype = "uint64", shape = (6,))#candidate|7594|(6,)|var|uint64
const_7595 = relay.const([5,-9,-1,-6,-7,1,-5,8,1,8,-7,-5,8,5,2,-5,3,-4,8,1,10,-1,-4,-2,-1,9,9,-9,8,4,-3,-8,1,-3,1,-6,-8,5,4,-9,2,-2,-1,-8,6,10,-1,6,-10,4,-2,10,7,-4,-5,-7,10,-7,-10,-2], dtype = "uint64")#candidate|7595|(60,)|const|uint64
call_7593 = func_2040_call(relay.reshape(var_7594.astype('uint64'), [1, 2, 3]), relay.reshape(const_7595.astype('uint64'), [10, 2, 3]), )
call_7596 = func_2040_call(relay.reshape(var_7594.astype('uint64'), [1, 2, 3]), relay.reshape(const_7595.astype('uint64'), [10, 2, 3]), )
output = relay.Tuple([call_7591,call_7593,var_7594,const_7595,])
output2 = relay.Tuple([call_7592,call_7596,var_7594,const_7595,])
func_7598 = relay.Function([var_7594,], output)
mod['func_7598'] = func_7598
mod = relay.transform.InferType()(mod)
var_7599 = relay.var("var_7599", dtype = "uint64", shape = (6,))#candidate|7599|(6,)|var|uint64
output = func_7598(var_7599)
func_7600 = relay.Function([var_7599], output)
mutated_mod['func_7600'] = func_7600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7135_call = mod.get_global_var('func_7135')
func_7137_call = mutated_mod.get_global_var('func_7137')
call_7642 = relay.TupleGetItem(func_7135_call(), 0)
call_7643 = relay.TupleGetItem(func_7137_call(), 0)
func_4255_call = mod.get_global_var('func_4255')
func_4258_call = mutated_mod.get_global_var('func_4258')
var_7664 = relay.var("var_7664", dtype = "int16", shape = (1664,))#candidate|7664|(1664,)|var|int16
const_7665 = relay.const([[5.698173],[-0.227810],[0.477791],[1.725367],[-7.918496],[-9.244734],[-9.616371],[7.495434],[-5.440156],[2.285774],[3.436524],[-4.610287],[-8.411149],[0.497733],[1.227481],[-5.479330],[-2.313870],[1.411071],[9.305823],[-5.805701],[-9.469029],[8.535211],[-9.092396],[-3.738680],[-5.775693],[9.060086],[9.120883],[-4.993789],[3.704069],[-2.434791],[4.078985],[8.007037],[1.157036],[2.579864],[2.222547],[7.260333],[-1.240100],[-6.353587],[7.458087],[2.402520],[3.506026],[8.597137],[9.584483],[-3.475716],[-3.341113],[8.969146],[6.331154],[0.372382],[3.290064],[-1.279022],[-0.700475],[-6.203198],[-5.981317],[0.578858],[7.086772],[1.390279],[-6.196956],[8.198130],[-5.849925],[-1.339333],[4.127108],[-0.832677],[0.066691],[0.196329],[9.157772],[8.321231],[6.893890],[-6.510140],[0.017524],[4.349628],[5.210086],[1.409205],[-9.437667],[5.065379],[-2.430562],[8.041458],[9.426710],[7.500491],[4.767549],[3.146425],[-7.636621],[1.462497],[-1.723656],[3.712047],[5.851212],[2.513594],[5.809038],[-8.677343],[4.709117],[9.324112],[-0.686355],[0.098980],[-7.142861],[-1.604267],[-1.129558],[-1.330810],[-0.463624],[-4.206201],[-3.171535],[-4.396233],[6.942947],[-2.143460],[-6.898328],[-9.957280],[-4.573368],[-6.706098],[-0.557010],[-7.060016],[-8.350312],[-5.335601],[-5.572490],[6.389808],[-4.358669],[0.063013],[2.197153],[0.101216],[1.954273],[5.922185],[-8.326042],[-2.978920],[2.819400],[9.416391],[-3.786862],[8.301829],[-7.152401],[9.868150],[-9.972690],[-1.165377],[8.955984],[3.045933],[5.050692],[1.159470],[-8.078149],[9.338531],[-6.104781],[1.473217],[-1.143298],[7.941666],[-0.853022],[4.467510],[-4.745973],[4.813078],[3.459085],[-4.366270],[-0.765385],[0.040308],[-3.951998],[-2.096625],[1.451888],[6.545484],[8.265083],[-5.024360],[-1.973614],[1.052406],[-4.870567],[2.895473],[9.888820],[3.068778],[-0.449438],[2.915243],[-4.299625],[7.458816],[3.829070],[0.292374],[3.923535],[-6.372632],[-5.072932],[-3.222045],[-4.061636],[4.350544],[-6.261214],[-2.546824],[-5.138065],[-6.103493],[3.714205],[9.635753],[-7.314488],[-4.243342],[-0.674013],[-7.224432],[-0.064469],[2.701542],[5.682501],[6.344651],[0.845999],[-0.093334],[-3.595626],[3.328142],[3.531858],[6.319927],[-6.540394],[-8.994204],[9.374620],[-7.139063],[-1.329274],[1.318837],[-4.700751],[9.158097],[-7.267882],[8.805989],[-7.098838],[9.861313],[-5.163109],[7.432142],[-3.270750],[-4.213273],[4.822023],[9.127480],[1.932640],[-0.099275],[2.303348],[1.560974],[-8.413802],[2.502553],[1.447975],[-5.057213],[0.335269],[-8.465461],[0.431915],[8.390503],[3.123253],[-1.637290],[-9.833228],[2.880658],[8.568862],[5.814321],[-8.832821],[-2.515609],[-0.173001],[6.345603],[3.760484],[3.165268],[-4.058810],[-1.484215],[0.620307],[2.238043],[-5.886251],[7.801558],[-9.085361],[-1.622182],[-0.357927],[-5.343243],[-0.840470],[-2.284362],[-1.196839],[2.085571],[1.610805],[-7.879741],[-3.712231],[0.113371],[-2.336677],[-9.013564],[-2.251264],[6.568343],[6.779528],[4.304923],[-3.328761],[-4.864851],[-5.518157],[7.574885],[-6.335145],[-8.783878],[4.574238],[3.816347],[-3.583244],[7.924673],[-8.887443],[1.223827],[2.548683],[5.640140],[-3.083069],[-3.614274],[-6.266254],[-0.380848],[6.201503],[9.767172],[-8.104440],[-2.440633],[8.849499],[1.765576],[-0.622307],[-8.018553],[6.986875],[-6.484385],[1.378752],[8.630653],[-9.401896],[-1.258859],[-7.020805],[6.940566],[-6.309375],[3.088719],[2.283353],[-0.163997],[-5.022345],[-6.196523],[-5.563998],[8.822568],[-5.519219],[-7.672001],[7.027071],[8.632117],[6.530600],[-4.670237],[-7.627518],[-4.430119],[-0.978848],[2.497863],[4.367603],[-5.519411],[-5.498403],[-2.108561],[-2.818727],[-6.584006],[7.885185],[-0.962806],[-8.594066],[-7.119455],[5.325722],[2.542322],[8.429521],[-3.851033],[6.774113],[0.069538],[7.049773],[-7.947342],[-9.564127],[-8.720789],[-9.255133],[9.924648],[1.776019],[-8.811026],[8.015712],[3.676289],[7.024955],[6.191091],[-6.686166],[1.060862],[3.250441],[-9.415566],[-7.444438],[-4.530804],[-4.738611],[8.062264],[9.030257],[-8.281405],[-0.742462],[-9.044938],[-6.117702],[-5.219397],[-9.208294],[-4.012877],[7.137316],[5.309532],[-3.016419],[7.496319],[-1.537850],[8.740391],[-5.016816],[-3.700540],[1.554801],[-8.441478],[6.492476],[4.312234],[8.502103],[-5.373807],[6.967749],[-2.300094],[-6.108573],[-3.138612],[-4.086796],[5.534258],[9.781991],[7.534228],[-5.064789],[-3.588636],[-6.406694],[0.352191],[0.411655],[1.962437],[2.507933],[1.349436],[-1.178012],[5.586953],[4.431488],[9.726685],[-8.344733],[-2.885804],[1.838121],[8.191104],[5.879086],[7.895932],[1.864918],[-8.520452],[-2.774918],[6.685316],[4.605004],[-3.930468],[-6.251555],[-1.277264],[0.651233],[8.848070],[-7.224431],[-7.702575],[1.600421],[8.164067],[6.700930],[3.023967],[-3.044648],[7.230593],[8.426071],[-5.291583],[9.072150],[8.175851],[-2.478066],[0.309626],[0.971253],[1.262917],[7.750295],[-6.764445],[-2.193169],[5.704981],[-4.911975],[-2.650168],[-8.117851],[9.182448],[-6.945993],[-3.005631],[6.283884],[9.870573],[3.716421],[6.162286],[-5.459708],[5.327908],[-7.568474],[-5.599251],[7.693640],[-7.862730],[-4.285781],[-7.346278],[2.897022],[3.557396],[2.664569],[1.106150],[9.956936],[1.664943],[-8.466481],[7.593172],[6.116925],[-0.872626],[-1.504173],[-5.839885],[-9.411492],[-1.019563],[2.733185],[-0.746551],[-3.333464],[-4.500758],[9.622353],[-7.805972],[6.312561],[-0.440646],[5.127422],[-5.128622],[-1.959717],[-9.912880],[0.399506],[-2.449681],[-9.987267],[8.055524],[-0.797127],[-1.697873],[2.502883],[-1.341010],[-0.061329],[1.987306],[-3.700958],[6.320447],[8.498036],[3.821130],[-9.148528],[8.696782],[-8.268981],[-4.314996],[-7.987428],[4.523550],[6.330379],[1.689663],[-4.714324],[1.503693],[1.145747],[-0.813746],[-3.536488],[0.418861],[9.501942],[0.607260],[-3.559702],[-7.176661],[9.298313],[7.534972],[-0.774092],[-0.120193],[-1.640027],[-7.307314],[5.113121],[-9.017152],[-9.309475],[9.515714],[-6.446006],[-4.272566],[1.189637],[-6.768156],[-2.509984],[-2.399331],[0.468734],[5.820532],[-8.760750],[0.997371],[-3.130043],[-5.045308],[6.767129],[-7.173214],[8.641990],[0.355112],[-6.756799],[-1.268227],[2.220729],[5.573677],[2.856763],[7.661961],[-7.557319],[-4.080647],[-8.312791],[8.016979],[1.165403],[7.398491],[-2.160326],[-6.047038],[9.294870],[-1.225958],[9.843933],[2.171193],[4.578139],[3.142205],[-7.295129],[2.401285],[7.352081],[-2.946324],[0.074372],[-1.685697],[6.087533],[6.867930],[6.499098],[8.203901],[9.170887],[-7.580767],[-8.344530],[-4.150485],[4.657573],[-1.061938],[-1.744387],[-7.754742],[5.736037],[-6.293240],[-6.183230],[5.216793],[-1.407515],[-2.644067],[-6.104132],[-5.802714],[5.734506],[5.405471],[-4.599807],[8.691745],[5.587630],[3.738462],[8.282952],[1.369187],[-3.620021],[8.332391],[8.625626],[-7.486764],[3.301156],[9.927577],[1.386870],[-6.584571],[3.214818],[-7.919271],[6.679785],[1.814393],[-5.364879],[-3.411730],[-6.488753],[-5.425613],[6.026742],[7.195099],[2.051138],[-4.602255],[-5.280693],[-0.881626],[1.168667],[-0.138476],[-0.972497],[-9.689060],[-9.656408],[-8.930228],[3.066356],[-2.755627],[0.628065],[-8.104193],[-8.047313],[4.729014],[-8.191237],[9.326333],[6.994163],[-1.270826],[-1.398982],[2.753444],[2.634878],[-2.306051],[7.881565],[-5.677933],[4.649889],[-9.973104],[-6.311860],[-2.599218],[0.291388],[-4.538692],[9.642608],[-5.996122],[9.687961],[-7.895571],[-2.703396],[4.835793],[9.052517],[0.514471],[-7.235158],[9.701508],[5.109094],[-8.273047],[4.252731],[-5.917679],[-0.967807],[-1.502923],[-5.058837],[0.077949],[2.775412],[4.792899],[5.082476],[1.848448],[-1.522072],[-8.200033],[9.419812],[9.662403],[4.039393],[-1.709303],[-0.054094],[1.791057],[2.372390],[-2.859134],[9.752125],[8.455204],[4.275138],[-7.201932],[1.546375],[-6.830788],[-0.779184],[4.441746],[-3.840430],[-0.187755],[-0.665577],[-5.507022],[-6.279878],[-3.336294],[8.799772],[6.061730],[-0.452148],[5.482280],[-3.717195],[-5.463292],[-1.090413],[1.884428],[2.492440],[-2.788427],[9.342195],[-2.710547],[7.450666],[-5.360409],[-1.352816],[3.254457],[-8.768032],[-0.536473],[2.081225],[-6.356926],[7.362441],[-3.305295],[9.183052],[8.848532],[-5.473213],[9.612463],[-5.521980],[4.176541],[-0.303569],[3.706659],[-1.579883],[5.251383],[-8.317644],[2.426912],[6.560498],[1.683580],[8.809699],[-2.257415],[8.598455],[7.523761],[6.995667],[-7.667212],[-9.556909],[3.404129],[7.196944],[-9.960865]], dtype = "float32")#candidate|7665|(720, 1)|const|float32
call_7663 = relay.TupleGetItem(func_4255_call(relay.reshape(var_7664.astype('int16'), [16, 8, 13]), relay.reshape(const_7665.astype('float32'), [720,]), ), 5)
call_7666 = relay.TupleGetItem(func_4258_call(relay.reshape(var_7664.astype('int16'), [16, 8, 13]), relay.reshape(const_7665.astype('float32'), [720,]), ), 5)
bop_7673 = relay.floor_mod(const_7665.astype('float64'), var_7664.astype('float64')) # shape=(720, 1664)
uop_7681 = relay.log10(const_7665.astype('float32')) # shape=(720, 1)
bop_7684 = relay.greater_equal(bop_7673.astype('bool'), var_7664.astype('bool')) # shape=(720, 1664)
bop_7693 = relay.maximum(uop_7681.astype('int16'), call_7663.astype('int16')) # shape=(720, 3)
bop_7696 = relay.maximum(uop_7681.astype('int16'), call_7666.astype('int16')) # shape=(720, 3)
const_7716 = relay.const([[-2.791796,-6.812616,-8.575923,-1.401677],[-1.288614,9.133210,6.122189,6.853840],[-8.751902,-1.282898,-9.873834,0.634500],[-7.073734,-1.378089,-7.937964,9.113587],[-9.209130,8.746681,6.427849,-6.677738],[-1.294974,-5.406847,1.920597,8.288309],[6.728545,-8.777600,-7.601893,8.383597],[1.313457,4.457546,4.271983,-0.393962],[-4.832710,-5.941560,8.974716,-1.035486],[-7.990043,6.716765,-1.204120,5.949224],[7.470295,6.590633,7.129097,-2.292900],[-1.096578,-9.239420,-8.944851,5.007727],[-1.743819,-8.926826,-9.199538,7.965678],[7.020510,2.064598,2.864602,0.798659],[-8.617223,-2.505584,1.498377,-2.232536],[7.183561,8.522484,1.654419,-1.108053],[-1.506157,4.535848,5.239601,2.430294],[4.042829,-0.054492,0.697286,3.293481],[-8.149702,-8.512248,-7.388457,8.401361],[4.446130,3.429311,1.220419,1.423898],[-6.427568,6.090280,7.081941,7.675243],[0.925096,-4.048782,0.602702,-9.718471],[9.424870,-6.303703,7.612446,2.617577],[-8.658248,8.639399,0.212500,-6.990213],[0.538690,5.650295,-2.441535,2.651876],[0.031928,1.071792,-3.433099,-2.610776],[-8.214348,1.070563,0.729635,-3.003159],[-2.037920,7.801778,-3.931079,7.478387],[7.210345,4.026176,9.709912,0.904912],[-8.082502,-0.725275,-4.168863,-7.848999],[6.613477,-6.235422,6.300955,-7.095597],[-1.717271,4.846229,1.822445,-9.501841],[2.321695,2.150529,8.099064,2.883591],[3.372929,-4.010491,7.479423,-4.892541],[-9.165726,0.784705,2.656958,9.127110],[0.664089,1.150575,-0.597647,-9.055946],[7.801102,-7.742625,-0.137254,-4.262323],[2.429208,-2.712551,6.991974,7.238868],[1.180360,8.284969,1.517850,4.861411],[2.636947,0.181652,-6.193926,-9.353472],[9.034654,-7.350465,-4.040102,0.745779],[6.413166,-6.769864,-8.808975,4.014802],[-5.697697,4.512763,5.841008,5.365159],[3.301450,-1.187974,-6.759989,2.514896],[-3.688645,0.783146,-6.551755,-5.577430],[-3.180360,-8.333938,8.382640,4.202465],[1.522851,1.885554,0.987553,2.991054],[0.062169,-2.949588,-9.112973,-6.687979],[-0.547454,-2.592131,-1.062913,-7.285231],[1.008976,-5.735714,-8.600439,4.284793],[-1.634435,9.174155,9.380363,-0.499590],[-0.764696,-2.768587,-5.849742,4.869203],[-7.244921,9.802936,4.248656,-9.728102],[-2.146292,2.178351,-5.769239,-3.496025],[7.048943,-4.993833,1.751779,9.016705],[6.836699,-4.301684,-2.429816,-9.826953],[2.129010,-5.081328,-4.786496,-6.780640],[2.767701,0.916539,-1.852125,-2.426109],[3.531846,-0.840243,2.133889,8.459697],[7.470115,-7.558991,4.566156,-2.936070],[-4.956000,2.629307,4.981989,5.376385],[9.865074,-6.907880,1.789644,7.598771],[3.787725,2.770920,-0.793034,-5.613936],[-4.854633,6.431263,5.048487,5.903050],[-3.058026,-4.970480,-3.987265,-2.519212],[6.519352,9.595177,8.370326,2.001570],[-7.947346,7.479233,7.876133,-8.055183],[-3.656550,-2.518978,6.309412,9.142857],[-9.802012,-9.786170,-6.846138,5.544590],[2.454806,-9.234560,0.521723,-5.846106],[-8.130991,-4.815111,4.961293,4.112675],[5.610547,3.261314,3.388341,-0.731894],[5.789402,-0.740868,-6.393846,3.541943],[-1.198704,-4.507728,1.129417,7.776866],[5.396508,-8.102015,-5.396755,-0.757383],[5.166995,9.054992,1.097984,-1.096740],[-3.361307,-0.036072,-9.165043,-3.863970],[0.892297,0.639233,0.760841,-7.473287],[-5.984296,3.418492,-3.028968,-1.957975],[-2.420877,1.419467,-2.941387,-2.676152],[-1.842742,7.913107,-8.883433,-8.063381],[-2.992778,-6.250812,-8.598209,-5.415443],[2.354080,-6.607882,-4.572458,3.318944],[-8.006004,-1.105789,0.463667,2.353179],[6.314673,-0.256262,-3.433008,6.132542],[-5.740586,8.671866,-9.185062,-3.836400],[2.828033,1.008504,3.947286,-0.128357],[3.886817,-7.632418,4.264100,1.959010],[-3.944302,-0.578884,-9.279663,-4.920747],[-1.785483,8.803310,7.959104,-1.623432],[-7.342368,-5.648048,1.242572,4.778822],[0.428014,5.555866,7.494755,7.309942],[-3.487728,2.599289,9.765233,-6.836945],[0.084938,-1.024504,8.694374,8.289350],[0.739453,0.321585,8.471636,1.211073],[5.200157,7.803668,3.857842,-2.037814],[9.621120,-1.661439,1.347119,-9.869347],[6.665537,-4.493019,1.931589,-2.176677],[6.253197,4.744616,2.228526,-2.598413],[4.376105,9.978409,-4.092702,6.735591],[0.159100,4.738073,-0.086970,2.817029],[-5.795108,-8.943121,-4.184776,-9.776987],[-2.365783,-9.814632,9.232700,-2.326993],[-4.453052,5.890630,-3.787079,-6.162891],[2.644750,-4.099924,6.641410,7.158164],[6.293357,-1.296475,-0.738408,-8.768943],[-7.062275,-2.454127,7.346694,1.909491],[7.946636,-1.988959,1.099912,8.620740],[-1.784023,-5.054556,-0.562585,-5.834490],[7.674518,2.985828,6.817222,-6.626088],[-2.998055,5.257734,-1.374457,8.953515],[-3.412270,1.970282,7.074921,-4.257331],[-5.479171,6.851023,-2.584203,5.500135],[-2.281598,3.086178,-5.479898,-4.109821],[9.214622,-1.078112,-9.302018,1.667454],[6.806287,-3.705495,1.220706,9.227897],[4.074257,-4.393871,-0.274355,6.444679],[-6.930387,-2.563375,-3.188839,9.576274],[8.655508,0.687438,-4.903758,-9.332475],[2.241290,-7.236334,4.587365,1.842075],[-2.425201,-1.707255,8.384282,-8.132124],[-0.190649,-3.590661,8.870120,-0.704791],[4.120418,-1.173955,-2.124677,6.304529],[7.929885,0.267906,5.319687,5.006240],[-4.839609,-8.056167,1.575184,-5.767712],[-9.612793,-0.468573,-2.701846,-0.039742],[8.417846,6.372710,0.382658,4.626446],[-4.050952,0.410857,7.575480,-6.758556],[-2.403348,7.536592,1.064249,3.647092],[-5.525202,9.756616,0.345657,-3.394620],[-5.467744,-0.758228,6.302800,-0.818879],[-2.294502,8.713736,-3.547856,-0.852639],[7.137379,-1.133861,3.202850,-9.855791],[4.796013,-5.878323,6.902612,9.935068],[1.493165,3.229736,-9.926320,-0.194636],[0.592261,-3.662498,2.169996,-3.132727],[0.568301,7.563423,-2.913061,-3.294593],[7.313899,-6.524033,-6.913622,-9.979372],[-0.992203,-3.672892,5.657162,1.201439],[-7.256212,-7.148525,-5.231921,-2.745471],[3.499354,-1.535635,2.213665,-8.932644],[-2.388417,3.322671,-9.625184,-3.928155],[1.105327,5.906921,2.998960,9.785988],[2.640151,-7.182948,-3.432942,4.359521],[-6.432804,-8.242082,-8.291004,0.654683],[4.217540,7.403235,-1.938729,-9.828023],[-1.654010,1.666839,2.743700,-9.647895],[-2.264745,-2.414585,2.367913,6.085141],[-3.633232,-5.483806,-6.471943,5.324501],[-4.182025,1.987126,-6.605282,1.120465],[-0.008647,-9.139822,7.856704,-7.535333],[1.777947,4.617624,-1.739844,9.434856],[-3.961598,5.417865,6.363881,-4.916705],[-9.104255,-7.531357,-5.551804,3.361640],[-9.641925,-4.484913,-8.686709,-4.658784],[2.260166,1.300918,-4.752219,-7.178210],[-9.462776,2.973218,-1.996871,7.223357],[8.079094,3.141889,8.048144,-8.940187],[1.439719,-5.271044,4.600012,8.589112],[-2.379613,-8.967964,4.166659,1.920473],[1.068554,5.731140,-5.135759,-5.649042],[9.448124,0.069337,-6.044165,-7.513430],[-7.382616,-7.059668,5.514296,5.279818],[-0.695238,-7.817628,-4.986135,3.165026],[-0.544632,-1.391329,9.465224,4.647788],[-5.781855,-6.427077,-7.154457,-8.297114],[1.462454,3.564567,8.164168,-2.525093],[-4.999442,2.884151,-1.226070,-9.652330],[-2.518491,7.829231,3.172772,-4.703772],[-5.954736,5.530344,3.718616,3.802516],[-0.198597,-5.698993,0.610004,3.622546],[1.429181,3.881512,7.916933,2.335072],[-1.896602,0.691052,6.153352,6.760999],[-9.432387,-8.481592,9.622386,-0.427711],[-9.231758,5.682675,9.879187,-5.963016],[4.286532,-6.691442,6.593782,-0.155381],[1.239725,-7.718010,4.401128,-1.213783],[-8.008301,-3.060979,-1.607486,0.755286],[0.530572,1.628533,9.037808,7.062035],[9.115246,9.802777,9.388460,-0.187812],[2.680220,6.811944,-5.075284,1.881977],[8.363214,-8.751522,-0.863186,-0.769609],[-4.056115,3.548638,7.441436,1.283841],[-8.992882,-5.546160,-7.008293,-2.581600],[6.297870,5.285372,2.979258,-7.219777],[-7.907792,1.332871,-0.176086,-5.055149],[6.643701,-0.673653,-5.090128,3.930978],[-9.577083,6.470280,-8.872307,-8.513425],[4.212949,5.141871,-8.630341,3.812893],[3.277287,-3.785841,5.644035,-4.663260],[-2.137744,2.462890,-6.938870,8.017967],[-5.183009,-4.012527,0.727833,-1.531684],[-4.991994,8.311541,4.009011,1.666569],[8.720260,-3.290127,-5.039617,6.273285],[1.959295,7.831325,0.074066,-5.433245],[3.148754,-1.747418,-9.471154,-7.982687],[4.335757,2.606147,-0.318501,2.898072],[-6.610826,-6.907025,-8.164901,9.370389],[9.855406,-2.340568,-3.106248,-8.084569],[8.622160,-3.334648,-0.805919,-9.763654],[-7.900577,-2.759151,-8.883981,2.526756],[-8.406807,5.386408,0.597978,-9.478903],[7.945168,-1.272678,-5.369892,-6.786098],[5.525966,5.986571,9.207192,2.350328],[5.022666,-1.133966,9.793373,4.296105],[-6.893013,8.685804,2.076350,-1.074863],[-0.747145,-5.853691,8.837553,-5.910132],[5.512301,-4.497540,3.019148,3.545996],[-1.632974,-4.456956,3.437247,4.868984],[-8.341194,2.536191,-3.492901,-8.102659],[-5.951386,0.120937,7.229418,8.556479],[2.474676,3.590836,2.602832,-7.145709],[9.228423,-5.264650,-7.015319,-0.934142],[-2.371917,-0.214102,3.270996,8.078012],[-5.741868,1.920301,-9.070630,-5.606044],[7.869391,-9.574051,-6.807213,-0.841077],[3.153399,-4.393514,-0.766585,-9.432512],[7.656184,5.664077,5.140916,-1.729280],[-5.183130,-4.250025,-4.974247,-8.246053],[-1.306927,7.881832,3.400150,-9.064007],[-9.011668,-1.720736,4.720648,7.634880],[-8.321593,8.939058,4.497095,2.210202],[-1.202904,-6.388650,-0.727084,-6.238197],[4.232161,-3.216598,7.948657,4.448111],[5.602009,-4.692255,-3.290823,8.968273],[-0.033375,-7.529618,0.005465,4.336578],[9.734922,-8.535419,9.807417,0.891828],[-2.796866,3.936884,-8.478968,8.687482],[1.310346,3.229414,3.790769,-1.116883],[7.227467,8.249134,-1.551504,-1.861856],[-4.047641,4.389083,8.424707,-4.323599],[-2.846838,1.840893,-1.280021,9.743112],[-6.293921,3.441400,5.311498,-8.304273],[5.160083,4.165704,-8.619809,9.351573],[3.704223,-9.568915,0.449446,-1.452329],[7.747549,5.006004,6.949572,9.603454],[7.101011,5.210644,-3.980725,2.059812],[-1.819003,5.187628,9.530329,8.472621],[0.908562,4.894919,6.594810,4.702481],[-9.399706,-3.940772,3.191769,9.230413],[6.695939,4.441764,-3.139181,7.041458],[-3.326920,-4.435036,4.116233,-5.549820],[6.564904,-0.127555,0.578226,2.619755],[-3.142096,4.986378,6.037087,-3.800365],[-7.656290,-5.361964,-2.888806,8.030183],[-0.545299,-7.214787,6.396116,9.757353],[9.106185,3.491150,1.004594,-6.609856],[4.906960,2.295127,-6.646847,7.950442],[4.080509,-2.043169,6.189210,-2.596678],[1.481086,2.738751,5.109874,5.524656],[-5.665496,-0.946312,-9.465097,8.529924],[-6.441655,-6.271022,-8.511974,7.789796],[-9.182642,-4.169817,4.914064,4.005935],[2.879800,-4.866490,5.458206,2.294996],[-3.653518,5.591229,-7.895954,-1.468089],[1.937412,-7.520582,-9.602464,-3.468264],[5.953891,-5.758179,5.322276,7.715924],[5.215363,-9.241744,1.538370,-8.544943],[8.800177,-3.925382,8.372560,-4.105967],[-2.228613,-4.530527,2.978061,7.712410],[2.183580,0.586731,9.828836,-4.194693],[-2.439257,-4.236046,-9.077846,-9.813254],[-6.756363,-1.589632,4.097989,7.985022],[1.195372,6.114202,-5.823531,7.591676],[-3.212350,-0.730654,4.096149,-8.660932],[9.192485,9.415342,-3.966568,7.261013],[8.887848,-1.743968,3.069242,-4.575794],[7.773953,8.732996,-6.477934,-3.905720],[5.139441,-1.913641,2.218600,1.787656],[4.544807,-5.129333,-1.995959,3.857975],[2.913316,-7.241017,8.795662,2.717593],[-1.941865,-6.632734,5.556244,-4.373430],[0.960369,4.504118,8.664625,-4.329324],[-0.197644,-4.737973,-0.661942,-7.313829],[7.372263,-9.066450,4.891237,-9.577331],[-2.469138,-5.545581,5.659981,8.996337],[9.012408,2.825307,6.990321,-4.720621],[-6.707526,-4.964816,-5.405631,4.578830],[8.304180,-5.878568,4.059353,2.172087],[8.513489,-9.789693,-1.259722,4.791907],[-7.182121,-5.456877,-2.239200,2.001956],[-1.882455,-8.521403,-3.429879,-9.443106],[4.440012,-1.152270,7.007051,4.006995],[5.165019,0.770728,1.692048,-1.498533],[4.115550,2.117069,2.655265,6.267444],[-3.990715,-7.372458,2.773946,-2.757633],[9.077765,1.795306,-5.862099,8.603895],[-9.303189,3.016885,1.821758,-3.102668],[2.426370,7.380884,-7.943370,-0.599448],[-3.649959,-2.571186,6.923288,-4.843045],[4.605473,-9.097294,-6.625953,-0.484197],[-2.157725,-5.365782,8.570950,8.127206],[-0.046356,6.288633,2.162408,8.387961],[-2.921943,1.623457,9.787213,-9.458146],[9.173127,-7.649860,-6.888211,3.403587],[2.095922,-9.053535,-5.427124,9.667894],[-4.545864,8.254011,-5.200339,6.488288],[-1.881223,-0.491432,4.239825,3.390830],[1.516048,-9.872069,-8.526410,3.742464],[-9.278881,-1.046551,5.810391,9.587226],[-1.308052,7.902088,-4.806159,5.607258],[7.859351,-4.825176,-6.130717,8.013274],[2.125876,8.598359,2.400746,8.048398],[-9.423901,-4.796393,6.659499,-4.722871],[7.704787,-8.267291,-3.892002,-1.870805],[-4.003264,-8.260691,-0.467285,-2.269713],[-5.858748,0.084918,-7.261275,3.996067],[-0.424117,-2.978152,9.987158,4.589279],[-7.287424,-1.421392,1.075268,-7.858485],[1.110109,-3.369453,2.697809,-5.593611],[-6.361469,0.494687,-4.521121,-0.443692],[0.830459,9.513181,6.292201,7.455655],[-0.758225,-1.687272,-9.445116,1.076050],[-8.252973,-1.664886,7.317240,4.495634],[-6.116763,-3.091575,2.052547,-3.440569],[-8.460819,3.140845,-1.844978,2.794137],[5.812315,9.573517,1.189027,4.628518],[-4.506005,4.557982,-0.843544,-2.196032],[1.168342,-7.601331,8.704026,1.631617],[-6.722732,1.113780,8.091336,4.605182],[-7.306577,1.782043,-2.978489,1.329530],[-0.213547,-0.292988,6.207890,1.793266],[5.045088,0.799554,-1.965469,-9.948938],[-0.771643,-4.309183,9.262924,-9.913116],[-1.468418,9.509858,-5.198633,0.110664],[4.530894,-9.789933,-6.991673,8.346836],[3.390092,-4.402034,-8.046306,-9.168341],[-1.854565,-8.096007,-7.474642,-0.227089],[-1.751797,0.604889,-4.626587,5.872781],[-6.384492,0.657380,-7.499008,0.776471],[8.284092,5.580882,-4.960918,-5.978485],[-3.172345,-5.032167,3.889120,6.055057],[-9.261774,4.878525,-7.567975,-1.830226],[-0.056439,4.185235,5.087618,-5.339729],[4.723074,-5.487241,1.665887,-4.792626],[9.255706,-6.533924,5.401644,6.622807],[3.727813,3.200380,4.993794,-8.481608],[2.180217,-2.741318,-0.053443,8.731224],[8.950752,-7.785576,3.177315,-7.014788],[8.458870,3.561558,7.117888,3.791656],[8.086645,-9.795857,-9.994612,-8.435762],[-5.535877,-7.806008,9.125616,-2.593123],[2.754890,7.529225,-8.382046,-2.550850],[0.965467,-5.979192,-9.545234,7.030260],[-3.835651,-0.547709,-8.492724,-5.169335],[-9.578084,-2.778205,5.539301,-6.806821],[7.674395,2.760078,3.963940,6.702042],[0.630409,1.030669,2.979770,-0.867837],[-0.826762,0.971171,3.745840,-9.719398],[-5.169871,-7.392246,5.081872,3.396363],[-1.061002,-9.153506,-3.791075,-4.514613],[-2.717605,8.199537,-3.811743,9.211597],[-7.330930,-7.672038,5.414420,5.375307],[5.441714,2.723912,-8.227217,0.748100],[5.078484,9.286098,1.606326,8.677050],[4.339466,-8.875648,-0.694057,6.228140],[-0.206305,6.846032,-5.547088,2.469812],[-7.994899,-0.231645,8.613605,3.926044],[-1.101623,-3.348810,2.169303,9.883233],[-4.633580,-2.609082,0.194021,-8.121598],[5.583865,7.215098,-0.116746,8.961207],[4.128083,-0.284242,2.362655,1.045465],[-8.747040,-7.411251,-8.840561,-2.280214],[9.903888,2.151208,-8.237120,-5.935651],[0.898279,2.972170,-0.298912,-6.402490],[0.710105,9.996138,1.631320,-7.619087],[-8.666905,1.295760,-6.171294,-5.250764],[-1.655156,-7.547260,3.566309,8.891630],[7.149718,-4.301246,1.670718,2.668187],[1.369985,-6.401952,-5.995776,-1.191139],[3.980833,4.395717,-6.892934,3.448860],[7.908963,2.664637,-8.466956,-2.363555],[-0.402734,0.852631,8.470156,-3.979107],[6.646799,9.877093,8.385166,2.554374],[2.643590,-8.375857,-6.667254,8.054254],[8.737631,-0.078917,0.789491,9.588051],[0.262498,5.333990,-3.975090,-5.596283],[-3.793190,6.623885,4.880258,-7.962698],[7.103403,-9.674266,-5.691142,2.258057],[3.037197,0.711286,-0.429135,-7.969157],[-6.655948,3.004861,0.517228,-0.050590],[3.579936,2.923469,-8.216699,-1.845029],[-6.429950,8.388410,-0.735554,-3.300968],[-4.035288,-7.350510,3.281809,3.515201],[-3.786894,-1.924985,-3.926708,-5.920051],[-5.398221,-4.142172,1.065416,-8.984163],[-3.971008,9.698974,-3.863242,-4.588140],[8.649740,-5.798237,5.165573,-0.267425],[-3.435532,2.829930,-6.410561,-9.817662],[7.615628,6.950667,4.080007,-1.465084],[-3.974606,-1.954086,0.186635,7.957267],[2.103421,6.292351,8.932661,2.128528],[-1.404253,-1.073757,-7.400850,1.036620],[-3.120611,-5.510992,-1.208416,4.940667],[-4.807848,-9.279992,-8.067421,8.903337],[9.282448,-0.017359,-6.937466,-2.085500],[-3.532008,4.253100,1.665347,-9.430441],[-3.918409,-0.118999,0.845086,6.325002],[5.289426,3.107683,6.669742,-5.897347],[-0.010879,-4.876681,-1.588698,7.746147],[9.113474,3.904739,-9.074591,-8.545888],[-4.000740,3.000409,-9.319499,-4.591588],[-1.573716,4.228852,-9.193352,-1.985161],[-5.487449,5.753595,8.458061,4.527633],[-7.019975,-3.544601,-7.558271,2.888779],[2.440441,-3.609177,4.418278,8.109856],[7.876104,6.856647,-8.865585,-8.080978],[-1.093787,6.966663,-7.870535,7.093245],[8.353032,7.352453,-7.902198,1.184426],[-8.910365,-1.389877,-4.969436,1.784272],[-8.714374,0.038319,8.617895,-7.462265],[3.335153,2.894539,-6.683801,-3.623414],[-9.788720,-8.105286,-6.751179,-8.208008],[2.068130,-5.334003,9.856322,0.292278],[3.020511,-6.966097,-5.084632,-5.852422],[4.613341,-7.323741,-3.023836,2.946936],[-5.378383,-4.949531,7.674908,5.569826],[5.781516,-5.610808,-4.930403,-6.691424],[-4.135959,-4.024460,0.557172,4.809953],[-4.140425,2.560707,-1.651637,-1.211618],[-6.320868,-7.460584,9.749888,-8.767294],[1.151372,8.340378,4.966228,2.221437],[5.961033,-5.222826,6.633639,0.604585],[0.473535,-3.433280,9.087522,0.558508],[5.306133,-7.329670,2.157808,0.483095],[7.136906,-7.792210,9.962606,2.218611],[1.654565,1.777554,6.792084,4.835988],[1.143288,-5.950314,-8.551363,-6.344851],[3.657880,-9.486676,-3.417645,-5.104908],[2.052676,-9.034131,-1.880601,4.318328],[3.848834,-0.746332,7.674767,-6.148408],[-1.946786,1.201391,-4.050905,-3.069957],[-5.333392,-8.721973,4.097102,8.608607],[-8.718906,5.383452,7.691860,-6.950651],[5.572390,1.144338,-9.101351,-8.746192],[-2.140027,2.874981,0.754995,8.660788],[3.842410,-0.634610,-8.557649,1.003063],[6.338427,8.126579,9.844587,-6.689994],[0.587725,7.556999,8.488768,-9.363598],[7.547174,-7.412126,1.181946,0.416873],[6.730802,5.298585,7.047905,-7.499563],[4.491898,3.461143,-7.395115,-4.978305],[8.961534,2.928098,2.205691,-9.293400],[-3.299690,7.503318,-9.909148,-2.089099],[0.128568,4.643349,-0.301257,4.441222],[-1.362748,-7.993620,-0.471532,-5.269846],[-5.946156,-4.577503,8.434190,-8.132792],[6.554830,6.066404,-6.685930,-2.896538],[-2.809731,-6.582368,3.172973,-3.671634],[-7.729913,-7.387879,0.303593,-8.516459],[9.383936,8.889753,-4.361624,-2.148993],[-8.232485,9.824464,1.535014,-6.671124],[-1.527843,-6.962139,-0.743823,9.399166],[7.136250,-9.765170,-3.959035,-2.998747],[0.338853,-7.738315,4.289929,-8.539500],[-4.173393,7.419592,5.276673,4.711981],[-3.755957,0.268119,4.909115,-3.903653],[4.532531,4.521281,0.515279,1.535980],[-6.725904,-3.128511,-6.547770,3.770896],[9.322008,-7.383801,-1.726206,-9.907576],[3.231757,8.300161,-4.347872,0.623287],[-6.335025,0.232287,-3.882455,6.721821],[-8.654197,-6.196116,-9.507005,2.409510],[-9.325020,-8.609906,-5.710399,-9.151790],[-4.079675,-8.597060,8.882922,-5.114894],[-0.490863,7.223159,-6.535045,0.260693],[4.071469,7.294031,4.796067,6.201302],[-1.226619,-5.678195,-2.375405,-1.403981],[8.346670,0.299372,-9.458572,-7.235214],[0.388466,4.781571,-2.217930,-3.087263],[1.435473,6.529236,-8.816270,-6.965413],[-9.471288,3.651461,6.544096,-6.146777],[-6.332510,4.078168,8.568641,-9.076315],[-8.237960,8.508271,-6.869089,-5.103668],[5.676263,5.849852,-1.707012,2.532692],[-3.258265,2.663028,-7.056270,-5.860263],[3.377596,-2.884340,-9.341148,2.070286],[-5.210410,6.323013,-1.213776,-7.012348],[-5.290194,8.512244,-9.664841,8.483261],[-1.314379,-6.831336,-1.439137,1.835867],[7.915843,4.052228,-1.023251,-6.541179],[1.301452,-0.755680,5.330310,0.523875],[-0.871900,-8.460523,3.888822,6.054759],[-7.029055,2.465984,2.043729,-0.197050],[-1.425082,-4.030101,-3.395006,3.619950],[-0.881415,1.659839,7.870244,6.171195],[3.503009,-0.488163,-4.815915,-7.761690],[9.669956,5.092206,0.073632,1.387919],[0.844884,-3.546573,-5.773232,8.630711],[3.880406,-1.427797,-3.029366,-4.295384],[9.034053,-1.408556,4.086436,-3.118327],[-3.688064,3.850310,0.310133,7.746780],[-7.277490,-6.251145,-0.567286,6.399249],[-4.658970,-0.018531,-4.933242,8.330779],[9.505410,7.025749,-4.613428,5.948293],[4.597029,-7.435868,-6.852488,-1.327034],[-1.145006,0.645687,-6.440789,-0.159711],[1.908478,0.150713,-6.647081,8.817689],[7.229973,-5.214057,5.354976,-0.125109],[-6.193662,8.615582,0.970107,6.019440],[0.256394,-7.275040,1.463956,-8.118715],[9.419398,-4.367572,-6.168511,0.632349],[-0.906030,-8.146589,9.043724,7.453013],[5.475745,-8.575624,-2.582452,-6.352689],[2.211468,7.112914,-0.474843,0.266449],[-1.786146,8.404070,7.605534,-6.049309],[-4.440359,4.846271,7.087442,8.282178],[-9.067577,7.070662,4.528590,-8.516882],[-3.506825,6.926515,1.495617,-0.675720],[9.052910,8.515245,-4.510405,-5.027476],[-4.481149,9.173470,-3.155178,-4.790986],[-4.817483,1.220890,-7.629362,-8.757434],[-5.966373,0.303989,-3.222086,4.045336],[3.366060,8.603722,-5.768225,-8.786412],[0.411156,-0.597254,-1.319001,-4.366780],[6.045368,-0.299362,9.517033,-4.110906],[-0.841955,-2.357130,-2.682936,-0.057736],[-6.029093,4.619984,-5.055857,2.014318],[6.217745,5.388873,-9.460612,6.607489],[-8.497451,9.584947,-6.690567,7.887683],[8.945946,-7.959456,2.553651,7.789545],[-4.415588,-0.976118,-6.583555,-7.765374],[1.736839,7.422390,-3.872749,0.312778],[-9.148832,-4.180114,9.806667,-5.509965],[7.429229,-7.085255,6.180118,-0.386358],[-7.454172,-3.591520,-0.853824,7.484026],[4.195513,-9.106089,3.183039,-2.909540],[-1.256103,-0.448335,-1.161912,3.662056],[7.480385,-0.038176,8.216783,-7.447146],[6.667374,4.321940,-6.415474,4.175552],[8.130906,6.428658,-9.565181,2.892645],[-1.559670,-2.698011,-5.926697,3.205233],[7.591871,-5.232813,-7.945973,-7.610716],[-5.523300,-9.943358,-3.599188,-5.750823],[5.200879,-2.454135,1.463664,-8.249746],[-9.931423,-1.899766,-7.180314,-0.855828],[2.760754,5.744513,-6.068404,4.462484],[1.226111,4.560050,6.445259,9.939423],[4.939253,-5.416792,8.249480,-9.009262],[8.584961,-3.380342,-2.917168,3.141926],[-3.107931,-8.794168,6.706767,4.769025],[0.428227,-5.415170,-9.922020,5.521124],[-6.764532,-3.798131,-5.023764,0.689566],[1.363234,-8.870181,-0.820286,4.011985],[-0.377441,7.908659,3.351165,-9.102164],[0.333677,8.312846,-9.811437,9.252188],[2.043696,4.166591,1.793992,1.576775],[-2.579773,-2.868915,-6.991536,9.963317],[2.934406,-8.089895,5.640758,9.727376],[4.910154,-4.662870,2.335679,-6.430041],[3.953524,9.128522,-2.669392,3.588316],[-3.226616,-1.129299,3.068026,1.399926],[-5.899453,2.836731,-9.742659,0.326967],[-2.674450,2.308880,3.632838,-1.916511],[3.693811,9.854431,-3.542259,5.020427],[8.047683,1.043218,2.237197,1.064076],[-8.161802,-7.116131,-5.516543,1.513064],[4.239278,-1.406120,-9.245561,-1.880636],[-0.391836,-3.723013,-9.974314,1.298287],[9.028956,0.999828,4.605354,-7.428669],[2.051005,-8.163194,-3.866765,-2.198045],[2.975152,7.988259,6.581051,7.674789],[4.737273,6.752251,9.511803,8.131793],[5.568451,-4.645670,-6.598415,6.437647],[4.222676,1.152631,4.826304,5.921887],[-8.234974,-9.776952,-1.571935,-2.543700],[9.514218,-5.380790,-8.049965,2.702419],[-3.043501,9.322416,0.146987,-0.632839],[-8.342885,-1.959756,-7.221999,-0.844388],[-3.275983,-2.616403,5.081321,7.960723],[-6.600324,8.456115,3.691358,5.844936],[-5.481500,-3.333647,0.284422,-2.161624],[-8.724995,0.587077,6.855805,-9.917804],[-9.564526,-2.912765,5.407232,9.018935],[5.835147,-1.951594,3.081756,-6.028147],[-5.911562,3.276651,-9.263927,-7.134805],[7.426056,1.022936,3.723767,-6.403979],[-2.713515,0.831620,-9.987490,-7.403926],[-7.565430,2.155290,-5.796256,1.005034],[-2.504214,-2.530413,0.688251,-3.225118],[-5.002631,0.648654,0.741902,0.626861],[-4.309418,6.145545,3.644682,6.790384],[-0.483407,-4.308459,-7.606782,-3.531860],[-1.225618,7.270251,8.732234,-7.481516],[6.719169,1.045795,-1.327331,4.503333],[-8.279998,7.359319,-2.267545,4.738347],[8.117035,3.468084,3.852400,7.136268],[-9.108796,9.959507,-9.528461,9.961653],[2.024389,-6.993093,6.972884,5.914986],[-6.248333,-3.455012,7.124513,5.670679],[1.366288,-8.607271,-3.863875,-1.951908],[2.360754,-6.836138,-5.091885,6.973102],[6.458880,0.680672,1.107801,-4.186322],[7.670509,-3.214953,-8.251416,-1.974373],[-4.655507,-7.626506,-7.531160,8.407745],[1.907261,0.126588,6.992477,0.275744],[-1.030626,-9.783989,0.398074,0.526095],[7.599680,8.819339,7.114238,6.732318],[1.859908,4.253839,-6.305488,9.505353],[-7.120230,4.411747,6.688293,-6.143823],[5.156708,-0.409660,3.454097,-8.008957],[3.430384,-1.724297,6.694797,3.850358],[-8.269044,-2.703244,0.322654,-9.385060],[-3.911549,-0.346800,-5.425699,3.497731],[2.581130,6.738023,0.020179,3.981840],[3.326675,9.352163,0.381190,7.718760],[3.269102,-1.011466,0.104767,4.255532],[4.291999,-2.836350,-4.504140,7.317818],[5.989295,4.785587,-3.793698,1.945017],[-3.537015,-5.545790,4.798510,3.546198],[8.114208,-0.773533,-4.387109,-2.553147],[9.412695,-6.726559,-4.667085,6.074616],[-8.963879,-6.338762,3.808220,-8.716116],[3.889729,1.102958,1.118756,7.449953],[-2.223124,8.328013,7.102138,-6.605575],[-1.215102,2.470834,3.008852,-8.667092],[5.324976,-8.046811,3.093960,-8.035424],[-9.655736,2.182195,4.961598,-6.489071],[-3.115300,-0.033739,-9.186898,-6.941422],[2.153072,8.037900,-7.393102,-7.499639],[7.878702,-9.259918,-6.802080,2.531191],[-6.622840,-1.582227,9.656357,-4.172935],[-6.268728,-8.544891,1.188078,-8.882536],[-3.163122,2.408152,2.343483,-1.691248],[3.713819,2.702065,6.171717,-8.967854],[-2.315875,9.570903,3.293198,2.335882],[0.633291,-8.296603,6.312601,6.324464],[9.495641,-7.134206,3.274477,0.557616],[-6.963486,-2.212086,1.004061,6.708953],[9.411884,4.653284,-4.889483,-7.621962],[-9.312902,9.624858,2.396783,1.298501],[1.825354,-0.230706,-7.667713,4.752134],[-9.834666,7.168307,-4.085249,7.066366],[9.457363,4.582819,-0.379434,4.567532],[-4.399818,-4.801006,-2.251310,-5.184555],[3.198410,-8.704859,-6.129914,-8.213558],[2.156380,-4.378396,0.927361,5.429006],[8.714684,-8.945397,-5.325054,-6.703156],[-6.454080,8.525190,6.443721,8.632701],[-7.910216,-6.051319,5.639216,0.580645],[-7.758995,6.804564,-5.883050,6.626624],[9.204965,8.572593,1.399080,-2.570047],[-2.497648,-8.783236,-5.269440,-7.943726],[4.021743,8.083735,-6.322917,7.375592],[7.838671,-0.616377,9.303442,9.867318],[5.931546,3.032633,-2.161529,7.220056],[7.759241,-7.139416,7.193894,-9.121938],[-1.935281,7.191875,-3.655182,3.280081],[1.893451,0.161676,0.572486,2.218332],[4.924587,-5.394568,1.011114,-9.252356],[6.037433,-6.780237,-3.735987,-6.939826],[-6.499988,4.251829,-0.046647,-5.064914],[-7.526595,7.525031,-6.896238,-2.623803],[4.281346,-7.047918,-0.310407,8.639716],[2.917568,-5.992040,-1.100247,-8.707717],[2.030167,5.688380,6.723324,2.742130],[-1.386101,6.522750,-1.256762,-1.907385],[-2.083131,-7.333478,-3.702383,1.163485],[3.953772,8.539397,-7.873432,-9.632306],[4.261127,5.030959,-7.894409,-6.381835],[2.136167,7.402147,4.902633,3.756755],[-2.724609,1.960289,1.187072,4.032307],[-1.774175,-9.267571,-0.775408,-5.332569],[4.348611,-1.069528,8.511640,-6.333118],[0.304312,-6.794049,2.315604,-5.978032],[7.927576,-9.350772,-5.840237,5.492960],[-3.561029,6.639614,-3.787672,-0.348148],[-5.706485,5.374489,7.556956,-2.691749],[-2.999794,-5.112960,2.148801,2.541311],[-3.028812,1.133148,2.561604,9.431723],[3.717928,6.042256,6.320487,8.692315],[-2.811246,3.832251,-5.087958,-6.646240],[-8.408481,-2.872530,-8.519844,-3.765149],[-8.756271,2.643699,-7.296703,8.611968],[-5.270609,3.467268,3.559828,8.512267],[-3.865164,9.512332,-3.420776,2.236567],[-2.475258,-6.484917,6.539491,7.904873],[6.083523,-7.870370,-9.122825,7.886991],[-4.200537,-3.848157,2.351207,7.643321],[-7.705191,-2.147997,9.102098,1.553657],[6.560994,-9.580271,-8.958206,-6.124961],[-2.314482,2.305511,7.357936,1.000826],[1.689195,5.313560,0.573172,-9.182808],[4.626047,9.298537,-4.930518,4.058709],[-1.194282,3.964173,2.018543,-1.469613],[-7.555838,-4.015131,-6.278331,9.568847],[6.609785,-9.993167,8.166658,-4.601727],[1.033330,8.097987,-1.715589,-8.004307],[-1.418698,3.534734,0.334263,-2.548211],[4.671066,7.743995,-6.433350,-1.534660],[6.796666,9.097964,8.438258,-0.363005],[1.628200,5.483485,-1.748143,-8.835083],[6.548822,-8.044738,-3.112265,-5.914930],[-4.275678,6.970302,-6.718583,-4.391521],[1.414646,-6.503667,-1.309711,7.342818],[0.372376,2.542832,-9.649089,-6.893567],[-3.276244,5.542479,3.139573,-6.456072],[2.912631,0.216989,0.183539,-8.846099],[2.622016,-1.484451,3.665528,5.429144],[-7.944987,-7.493429,-8.066625,-6.090079],[7.111789,1.719140,8.840387,-6.929744],[-6.990064,-0.864465,-5.918298,-4.289950],[4.023806,6.860026,-3.862520,9.918871],[3.496089,-7.087907,3.652020,-7.834555],[-8.633352,6.790726,-2.385912,-0.188235],[6.688729,-4.278199,0.924082,8.623636],[5.158476,9.530313,5.485390,-5.645361],[-5.965296,5.918484,9.821663,0.541187],[0.843522,3.453348,-7.299189,-3.476432],[-3.681881,3.481516,2.099075,7.370184],[2.963909,4.796664,0.421524,-2.044811],[-6.578211,7.932661,8.647932,1.923028],[-9.679506,-8.055474,-2.600637,-2.740538],[-2.278407,0.220684,6.705599,-4.756597],[7.928109,6.674972,-1.623624,0.345959],[9.081387,-5.228766,4.973980,-7.606988],[1.650965,-0.541754,7.049018,-9.460680],[9.384599,-3.439672,-3.508790,2.398580],[-1.827564,9.621327,-5.968338,2.697461],[2.650305,6.073580,7.172077,-6.271057]], dtype = "float32")#candidate|7716|(720, 4)|const|float32
bop_7717 = relay.logical_or(uop_7681.astype('bool'), const_7716.astype('bool')) # shape=(720, 4)
output = relay.Tuple([call_7642,bop_7684,bop_7693,bop_7717,])
output2 = relay.Tuple([call_7643,bop_7684,bop_7696,bop_7717,])
func_7728 = relay.Function([var_7664,], output)
mod['func_7728'] = func_7728
mod = relay.transform.InferType()(mod)
mutated_mod['func_7728'] = func_7728
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7729 = relay.var("var_7729", dtype = "int16", shape = (1664,))#candidate|7729|(1664,)|var|int16
func_7728_call = mutated_mod.get_global_var('func_7728')
call_7730 = func_7728_call(var_7729)
output = call_7730
func_7731 = relay.Function([var_7729], output)
mutated_mod['func_7731'] = func_7731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7851 = relay.var("var_7851", dtype = "float64", shape = (3, 5, 5))#candidate|7851|(3, 5, 5)|var|float64
uop_7852 = relay.sigmoid(var_7851.astype('float64')) # shape=(3, 5, 5)
func_7057_call = mod.get_global_var('func_7057')
func_7059_call = mutated_mod.get_global_var('func_7059')
call_7854 = func_7057_call()
call_7855 = func_7057_call()
output = relay.Tuple([uop_7852,call_7854,])
output2 = relay.Tuple([uop_7852,call_7855,])
func_7856 = relay.Function([var_7851,], output)
mod['func_7856'] = func_7856
mod = relay.transform.InferType()(mod)
mutated_mod['func_7856'] = func_7856
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7857 = relay.var("var_7857", dtype = "float64", shape = (3, 5, 5))#candidate|7857|(3, 5, 5)|var|float64
func_7856_call = mutated_mod.get_global_var('func_7856')
call_7858 = func_7856_call(var_7857)
output = call_7858
func_7859 = relay.Function([var_7857], output)
mutated_mod['func_7859'] = func_7859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5620_call = mod.get_global_var('func_5620')
func_5622_call = mutated_mod.get_global_var('func_5622')
call_7879 = relay.TupleGetItem(func_5620_call(), 0)
call_7880 = relay.TupleGetItem(func_5622_call(), 0)
uop_7882 = relay.sqrt(call_7879.astype('float64')) # shape=(16, 16, 8)
uop_7884 = relay.sqrt(call_7880.astype('float64')) # shape=(16, 16, 8)
func_1302_call = mod.get_global_var('func_1302')
func_1306_call = mutated_mod.get_global_var('func_1306')
var_7891 = relay.var("var_7891", dtype = "int64", shape = ())#candidate|7891|()|var|int64
var_7892 = relay.var("var_7892", dtype = "int64", shape = (90,))#candidate|7892|(90,)|var|int64
call_7890 = func_1302_call(relay.reshape(var_7891.astype('int64'), []), relay.reshape(var_7892.astype('int64'), [1, 15, 6]), )
call_7893 = func_1302_call(relay.reshape(var_7891.astype('int64'), []), relay.reshape(var_7892.astype('int64'), [1, 15, 6]), )
func_2557_call = mod.get_global_var('func_2557')
func_2561_call = mutated_mod.get_global_var('func_2561')
const_7903 = relay.const([8.608119,-6.913676,-0.605564,-2.559141,-7.504879,-6.118274,9.726455,9.864826,1.244202,4.051285,2.957020,-6.510086,4.417903,0.001614,6.551930,-9.129461,0.981912,7.592534,-0.757219,-0.430808,-4.435899,-8.386004,2.576143,0.723335,0.334692,2.798501,5.049498,0.459025,-0.972871,0.314192,1.420783,7.905539,-6.749737,-8.027387,-1.046256,5.399710,0.852035,-4.473892,2.400251,-3.114271,5.842349,0.195133,4.668846,1.035788,0.364471,-7.460199,-3.479792,3.764124,-7.498274,4.267733,2.474710,-4.814037,3.715669,2.822750,-0.009880,3.394788,4.907466,-5.466637,-3.742516,1.090509,-7.253964,-6.642507,4.308400,8.513957,4.593318,-5.646078,6.998621,7.092740,-3.825255,6.894221,-4.999000,-6.963956,-9.477870,9.420884,-5.335015,-6.105501,-3.802472,8.355222,0.748444,5.841477,-1.492919,9.956919,-9.394942,-8.124226,6.904738,5.097952,-2.564479,-2.295564,-1.541552,4.042910,-2.678462,3.278050,-8.661947,-0.379954,3.980833,-5.579870,5.756867,0.602198,8.318467,-3.518526,-8.596769,-4.777017,2.963179,7.274002,-1.006374,-7.579124,-9.006667,9.688396,4.416006,-9.010569,-9.840205,-0.687653,-5.746809,1.699863,3.494581,7.149265,-2.909329,-2.086078,-4.028128,2.364845,4.116780,6.893469,-5.221509,-7.248099,-3.670634,-0.180632,-0.111484,-6.931265,5.178323,-3.789484,-7.628383,-1.406743,0.928093,-3.750131,-7.525707,3.443193,-4.444541,3.672225,3.918707,-3.038822,2.810357,-9.595444,2.647363,-3.865372,8.191879,9.540295,-5.745738,-2.945158,-0.890380,2.969224,-1.633220,-3.408560,8.516173,5.978611,-9.681000,-6.533378,3.983786,0.599858,-8.814123,8.386929,-1.198458,9.080815,-1.779059,-6.960229,-2.190492,3.943924,-6.980219,7.768606,3.078542,4.346217,-7.999257,7.708459,-4.433357,-9.800281,0.328812,-7.143255,-8.940964,-5.247338,1.428383,-5.907799,3.161420,8.499846,4.926511,0.958051,3.678667,-7.520290,4.552828,8.225267,-1.193371,-5.582144,2.370385,8.477752,-0.452874,-1.158567,2.097030,3.945205,-4.134693,-3.557125,-8.845478,7.703692,-8.730980,4.559536,8.196070,-0.479819,3.949449,6.301739,7.186282,-5.584540,2.175794,-9.377615,9.591212,7.100774,-8.781691,-0.575446,7.724472,-1.731523,6.568525,4.220053,1.160872,6.092302,-5.322441,0.784586,3.967828,3.279694,8.860876,6.677616,-3.444683,-4.075462,4.872892,1.852134,-3.656136,-6.967030,1.755250,6.237321,4.598098,4.255210,0.461678,-6.835134,7.949325,6.285561,3.768586,8.314018,6.487778,-5.041151,-4.168038,-6.080329,5.883621,3.062456,-3.872568,4.652771,4.345858,-0.502148,-8.388712,5.503692,-6.164905,-8.805300,-9.598373,3.395124,2.584984,-8.535842,3.536920,2.120140,4.406137,-2.442019,0.743503,-8.573427,-5.323935,9.862675,5.377628,-4.877602,-2.168859,2.758790,4.956213,-2.366723,-1.800878,-8.178899,2.223040,-4.826979,-8.636936,3.589941,6.239982,-6.337742,-4.561715,-4.788249,9.722523,4.606856,8.520805,-2.469500,-9.449658,7.416694,7.652694,-3.607899,7.762612,2.485837,5.249526,8.067981,-3.754105,9.858275,-2.932269,-5.290021,-0.608541,2.171718,-4.396289,-3.615729,-5.717630,7.551904,-2.325445,3.681737,6.833179,1.652385,3.559046,1.234633,6.081209,-0.363252,-1.103656,2.066451,-3.539506,-2.532689,-4.369538,4.955557,-1.358457,-2.100324,7.775826,6.824728,-9.348789,3.666154,5.469557,-3.343170,9.183130,-4.562323,6.311672,8.584386,-2.745940,7.288997,-3.278747,-2.988656,8.004758,8.958181,-4.772286,2.673622,-0.982628,-4.450746,2.028457,-1.812383,5.206831,-1.839045,-3.505403,-0.500363,6.070295,2.528415,4.043729,9.488878,-9.259677,8.063190,0.380311,7.030409,0.746421,4.746199,-8.897043,-7.874670,7.004929,6.102586,-9.285673,-5.684329,8.491564,6.873181,2.952052,9.546102,-1.085507,-3.464146,-8.228748,3.872137,1.565404,-9.863218,-6.020352,6.832139,-7.833120,5.997156,6.656408,-8.353311,4.190567,1.657943,-0.637697,-0.938490,1.821051], dtype = "float64")#candidate|7903|(385,)|const|float64
var_7904 = relay.var("var_7904", dtype = "int16", shape = (8, 28))#candidate|7904|(8, 28)|var|int16
call_7902 = relay.TupleGetItem(func_2557_call(relay.reshape(const_7903.astype('float64'), [11, 5, 7]), relay.reshape(var_7904.astype('int16'), [224,]), relay.reshape(var_7892.astype('int64'), [90,]), ), 3)
call_7905 = relay.TupleGetItem(func_2561_call(relay.reshape(const_7903.astype('float64'), [11, 5, 7]), relay.reshape(var_7904.astype('int16'), [224,]), relay.reshape(var_7892.astype('int64'), [90,]), ), 3)
uop_7906 = relay.log2(const_7903.astype('float32')) # shape=(385,)
func_3320_call = mod.get_global_var('func_3320')
func_3325_call = mutated_mod.get_global_var('func_3325')
const_7928 = relay.const([1,-9,-7,-6,9,5,-5,-5,-3,2,5,-2,-7,-9,3,5,-3,-9,-5,1,6,-7,-9,9,-5,1,-2,10,-8,-4,-1,5,3,6,10,3,-5,5,5,7,7,-1,-3,-10,7,9,5,4,7,-6,-9,-3,1,8,1,5,7,7,-4,8,1,9,-3,-1,-3,9,6,-6,-9,-3,4,-6,-4,9,-10,-9,-8,4,-3,6,-4,10,7,8,-2,8,-9,-7,7,-10,4,-7,-10,-6,8,1,-6,-3,-8,-3,-2,-8,-5,-5,-2,-9,-4,1,-9,-9,8,8,-2,1,2,10,-2,8,-3,2,-5,2,-9,-5,9,-3], dtype = "int32")#candidate|7928|(126,)|const|int32
call_7927 = relay.TupleGetItem(func_3320_call(relay.reshape(const_7928.astype('int32'), [3, 6, 7]), relay.reshape(var_7892.astype('int64'), [90,]), relay.reshape(var_7904.astype('int16'), [16, 14]), ), 9)
call_7929 = relay.TupleGetItem(func_3325_call(relay.reshape(const_7928.astype('int32'), [3, 6, 7]), relay.reshape(var_7892.astype('int64'), [90,]), relay.reshape(var_7904.astype('int16'), [16, 14]), ), 9)
func_7441_call = mod.get_global_var('func_7441')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_7937 = relay.TupleGetItem(func_7441_call(), 1)
call_7938 = relay.TupleGetItem(func_7442_call(), 1)
output = relay.Tuple([uop_7882,call_7890,var_7891,var_7892,call_7902,var_7904,uop_7906,call_7927,const_7928,call_7937,])
output2 = relay.Tuple([uop_7884,call_7893,var_7891,var_7892,call_7905,var_7904,uop_7906,call_7929,const_7928,call_7938,])
func_7945 = relay.Function([var_7891,var_7892,var_7904,], output)
mod['func_7945'] = func_7945
mod = relay.transform.InferType()(mod)
var_7946 = relay.var("var_7946", dtype = "int64", shape = ())#candidate|7946|()|var|int64
var_7947 = relay.var("var_7947", dtype = "int64", shape = (90,))#candidate|7947|(90,)|var|int64
var_7948 = relay.var("var_7948", dtype = "int16", shape = (8, 28))#candidate|7948|(8, 28)|var|int16
output = func_7945(var_7946,var_7947,var_7948,)
func_7949 = relay.Function([var_7946,var_7947,var_7948,], output)
mutated_mod['func_7949'] = func_7949
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7961 = relay.var("var_7961", dtype = "float32", shape = (10, 1, 11))#candidate|7961|(10, 1, 11)|var|float32
uop_7962 = relay.asin(var_7961.astype('float32')) # shape=(10, 1, 11)
output = relay.Tuple([uop_7962,])
output2 = relay.Tuple([uop_7962,])
func_7965 = relay.Function([var_7961,], output)
mod['func_7965'] = func_7965
mod = relay.transform.InferType()(mod)
mutated_mod['func_7965'] = func_7965
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7966 = relay.var("var_7966", dtype = "float32", shape = (10, 1, 11))#candidate|7966|(10, 1, 11)|var|float32
func_7965_call = mutated_mod.get_global_var('func_7965')
call_7967 = func_7965_call(var_7966)
output = call_7967
func_7968 = relay.Function([var_7966], output)
mutated_mod['func_7968'] = func_7968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_8035 = relay.TupleGetItem(func_4460_call(), 0)
call_8036 = relay.TupleGetItem(func_4461_call(), 0)
output = relay.Tuple([call_8035,])
output2 = relay.Tuple([call_8036,])
func_8040 = relay.Function([], output)
mod['func_8040'] = func_8040
mod = relay.transform.InferType()(mod)
mutated_mod['func_8040'] = func_8040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8040_call = mutated_mod.get_global_var('func_8040')
call_8041 = func_8040_call()
output = call_8041
func_8042 = relay.Function([], output)
mutated_mod['func_8042'] = func_8042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6040_call = mod.get_global_var('func_6040')
func_6041_call = mutated_mod.get_global_var('func_6041')
call_8046 = func_6040_call()
call_8047 = func_6040_call()
output = relay.Tuple([call_8046,])
output2 = relay.Tuple([call_8047,])
func_8057 = relay.Function([], output)
mod['func_8057'] = func_8057
mod = relay.transform.InferType()(mod)
mutated_mod['func_8057'] = func_8057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8057_call = mutated_mod.get_global_var('func_8057')
call_8058 = func_8057_call()
output = call_8058
func_8059 = relay.Function([], output)
mutated_mod['func_8059'] = func_8059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5991_call = mod.get_global_var('func_5991')
func_5992_call = mutated_mod.get_global_var('func_5992')
call_8060 = relay.TupleGetItem(func_5991_call(), 0)
call_8061 = relay.TupleGetItem(func_5992_call(), 0)
output = call_8060
output2 = call_8061
func_8066 = relay.Function([], output)
mod['func_8066'] = func_8066
mod = relay.transform.InferType()(mod)
mutated_mod['func_8066'] = func_8066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8066_call = mutated_mod.get_global_var('func_8066')
call_8067 = func_8066_call()
output = call_8067
func_8068 = relay.Function([], output)
mutated_mod['func_8068'] = func_8068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7441_call = mod.get_global_var('func_7441')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_8069 = relay.TupleGetItem(func_7441_call(), 0)
call_8070 = relay.TupleGetItem(func_7442_call(), 0)
var_8074 = relay.var("var_8074", dtype = "uint8", shape = (1008, 2))#candidate|8074|(1008, 2)|var|uint8
bop_8075 = relay.logical_and(call_8069.astype('bool'), relay.reshape(var_8074.astype('bool'), relay.shape_of(call_8069))) # shape=(1008, 2)
bop_8078 = relay.logical_and(call_8070.astype('bool'), relay.reshape(var_8074.astype('bool'), relay.shape_of(call_8070))) # shape=(1008, 2)
uop_8082 = relay.log2(bop_8075.astype('float32')) # shape=(1008, 2)
uop_8084 = relay.log2(bop_8078.astype('float32')) # shape=(1008, 2)
var_8089 = relay.var("var_8089", dtype = "float32", shape = (1008, 2))#candidate|8089|(1008, 2)|var|float32
bop_8090 = relay.add(uop_8082.astype('int32'), relay.reshape(var_8089.astype('int32'), relay.shape_of(uop_8082))) # shape=(1008, 2)
bop_8093 = relay.add(uop_8084.astype('int32'), relay.reshape(var_8089.astype('int32'), relay.shape_of(uop_8084))) # shape=(1008, 2)
func_4017_call = mod.get_global_var('func_4017')
func_4020_call = mutated_mod.get_global_var('func_4020')
const_8103 = relay.const([[-8,7,-7,6,4,1],[6,-1,-3,1,-6,-5],[5,-2,-3,-5,-3,8],[-9,9,-8,-3,10,-1],[1,-10,-4,-7,1,5],[-8,-7,-3,2,-1,7],[-3,-4,-6,-6,8,5],[-1,2,2,7,6,-2],[9,10,6,9,-10,2],[9,-5,4,-10,-2,10],[-10,3,-1,6,8,-1],[-5,-4,5,-3,4,3],[9,6,6,5,-2,-3]], dtype = "int64")#candidate|8103|(13, 6)|const|int64
call_8102 = func_4017_call(relay.reshape(const_8103.astype('int64'), [3, 13, 2]))
call_8104 = func_4017_call(relay.reshape(const_8103.astype('int64'), [3, 13, 2]))
bop_8114 = relay.equal(uop_8082.astype('bool'), relay.reshape(bop_8090.astype('bool'), relay.shape_of(uop_8082))) # shape=(1008, 2)
bop_8117 = relay.equal(uop_8084.astype('bool'), relay.reshape(bop_8093.astype('bool'), relay.shape_of(uop_8084))) # shape=(1008, 2)
uop_8128 = relay.log10(var_8089.astype('float64')) # shape=(1008, 2)
output = relay.Tuple([call_8102,const_8103,bop_8114,uop_8128,])
output2 = relay.Tuple([call_8104,const_8103,bop_8117,uop_8128,])
func_8140 = relay.Function([var_8074,var_8089,], output)
mod['func_8140'] = func_8140
mod = relay.transform.InferType()(mod)
mutated_mod['func_8140'] = func_8140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8140_call = mutated_mod.get_global_var('func_8140')
var_8142 = relay.var("var_8142", dtype = "uint8", shape = (1008, 2))#candidate|8142|(1008, 2)|var|uint8
var_8143 = relay.var("var_8143", dtype = "float32", shape = (1008, 2))#candidate|8143|(1008, 2)|var|float32
call_8141 = func_8140_call(var_8142,var_8143,)
output = call_8141
func_8144 = relay.Function([var_8142,var_8143,], output)
mutated_mod['func_8144'] = func_8144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4538_call = mutated_mod.get_global_var('func_4538')
call_8154 = relay.TupleGetItem(func_4537_call(), 0)
call_8155 = relay.TupleGetItem(func_4538_call(), 0)
output = call_8154
output2 = call_8155
func_8197 = relay.Function([], output)
mod['func_8197'] = func_8197
mod = relay.transform.InferType()(mod)
output = func_8197()
func_8198 = relay.Function([], output)
mutated_mod['func_8198'] = func_8198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7179_call = mod.get_global_var('func_7179')
func_7180_call = mutated_mod.get_global_var('func_7180')
call_8214 = relay.TupleGetItem(func_7179_call(), 0)
call_8215 = relay.TupleGetItem(func_7180_call(), 0)
func_7020_call = mod.get_global_var('func_7020')
func_7022_call = mutated_mod.get_global_var('func_7022')
var_8234 = relay.var("var_8234", dtype = "float64", shape = (4, 300))#candidate|8234|(4, 300)|var|float64
call_8233 = func_7020_call(relay.reshape(var_8234.astype('float64'), [16, 5, 15]))
call_8235 = func_7020_call(relay.reshape(var_8234.astype('float64'), [16, 5, 15]))
uop_8237 = relay.log(call_8233.astype('float32')) # shape=(16, 5, 15)
uop_8239 = relay.log(call_8235.astype('float32')) # shape=(16, 5, 15)
bop_8256 = relay.floor_mod(uop_8237.astype('float32'), relay.reshape(call_8233.astype('float32'), relay.shape_of(uop_8237))) # shape=(16, 5, 15)
bop_8259 = relay.floor_mod(uop_8239.astype('float32'), relay.reshape(call_8235.astype('float32'), relay.shape_of(uop_8239))) # shape=(16, 5, 15)
output = relay.Tuple([call_8214,var_8234,bop_8256,])
output2 = relay.Tuple([call_8215,var_8234,bop_8259,])
func_8261 = relay.Function([var_8234,], output)
mod['func_8261'] = func_8261
mod = relay.transform.InferType()(mod)
mutated_mod['func_8261'] = func_8261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8262 = relay.var("var_8262", dtype = "float64", shape = (4, 300))#candidate|8262|(4, 300)|var|float64
func_8261_call = mutated_mod.get_global_var('func_8261')
call_8263 = func_8261_call(var_8262)
output = call_8263
func_8264 = relay.Function([var_8262], output)
mutated_mod['func_8264'] = func_8264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8057_call = mod.get_global_var('func_8057')
func_8059_call = mutated_mod.get_global_var('func_8059')
call_8361 = relay.TupleGetItem(func_8057_call(), 0)
call_8362 = relay.TupleGetItem(func_8059_call(), 0)
output = relay.Tuple([call_8361,])
output2 = relay.Tuple([call_8362,])
func_8378 = relay.Function([], output)
mod['func_8378'] = func_8378
mod = relay.transform.InferType()(mod)
mutated_mod['func_8378'] = func_8378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8378_call = mutated_mod.get_global_var('func_8378')
call_8379 = func_8378_call()
output = call_8379
func_8380 = relay.Function([], output)
mutated_mod['func_8380'] = func_8380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8040_call = mod.get_global_var('func_8040')
func_8042_call = mutated_mod.get_global_var('func_8042')
call_8441 = relay.TupleGetItem(func_8040_call(), 0)
call_8442 = relay.TupleGetItem(func_8042_call(), 0)
output = call_8441
output2 = call_8442
func_8443 = relay.Function([], output)
mod['func_8443'] = func_8443
mod = relay.transform.InferType()(mod)
mutated_mod['func_8443'] = func_8443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8443_call = mutated_mod.get_global_var('func_8443')
call_8444 = func_8443_call()
output = call_8444
func_8445 = relay.Function([], output)
mutated_mod['func_8445'] = func_8445
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8448 = relay.var("var_8448", dtype = "float64", shape = (15, 2, 1))#candidate|8448|(15, 2, 1)|var|float64
uop_8449 = relay.log10(var_8448.astype('float64')) # shape=(15, 2, 1)
output = uop_8449
output2 = uop_8449
F = relay.Function([var_8448,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8448,], output2)
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
