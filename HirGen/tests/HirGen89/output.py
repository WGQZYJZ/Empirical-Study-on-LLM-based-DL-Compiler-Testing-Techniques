import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_97 = relay.var("var_97", dtype = "uint64", shape = ())#candidate|97|()|var|uint64
var_98 = relay.var("var_98", dtype = "uint64", shape = (1, 16))#candidate|98|(1, 16)|var|uint64
bop_99 = relay.greater(var_97.astype('bool'), var_98.astype('bool')) # shape=(1, 16)
output = relay.Tuple([bop_99,])
output2 = relay.Tuple([bop_99,])
func_107 = relay.Function([var_97,var_98,], output)
mod['func_107'] = func_107
mod = relay.transform.InferType()(mod)
mutated_mod['func_107'] = func_107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_107_call = mutated_mod.get_global_var('func_107')
var_109 = relay.var("var_109", dtype = "uint64", shape = ())#candidate|109|()|var|uint64
var_110 = relay.var("var_110", dtype = "uint64", shape = (1, 16))#candidate|110|(1, 16)|var|uint64
call_108 = func_107_call(var_109,var_110,)
output = call_108
func_111 = relay.Function([var_109,var_110,], output)
mutated_mod['func_111'] = func_111
mutated_mod = relay.transform.InferType()(mutated_mod)
const_258 = relay.const([[[5,-1,10],[-9,-2,1],[4,6,10],[-4,-6,-9],[-4,-7,8],[-4,-3,-6],[-4,8,-10],[9,-5,-2],[4,6,-10],[4,6,4],[1,-9,-6],[7,-9,-3],[-8,-7,-9],[9,-4,3],[8,1,1]],[[1,3,6],[4,9,-10],[4,-7,10],[9,-9,-4],[10,2,-7],[-7,4,-8],[-1,-4,8],[5,10,3],[9,-9,7],[-1,-5,-10],[-5,-3,-9],[9,-5,-2],[-7,-5,8],[8,1,6],[-9,7,-9]],[[8,-6,-4],[4,-4,-8],[-4,-3,1],[8,-7,-7],[9,9,1],[4,3,-2],[2,-2,-9],[-5,5,-3],[-7,8,-1],[6,-10,-5],[2,-2,-9],[4,4,-10],[-4,5,10],[8,10,1],[8,1,-2]],[[-10,-8,-9],[-1,-8,9],[-10,-10,-4],[5,-8,-5],[-6,6,-2],[-6,3,9],[10,-7,6],[4,-10,-3],[5,-6,2],[-3,6,-8],[8,-3,7],[-4,-1,-3],[8,-5,4],[-5,-5,-3],[4,-7,-5]],[[-9,8,-5],[3,2,-2],[-2,-4,3],[6,-6,-8],[-8,-5,3],[10,3,1],[5,-7,7],[-5,4,-8],[9,4,5],[-4,-6,-9],[-9,8,-1],[9,-4,-4],[-10,4,10],[8,5,5],[-3,4,10]],[[-8,-2,-10],[-9,10,7],[-6,5,-10],[1,-4,-9],[-6,-8,4],[4,6,10],[1,-6,5],[-5,2,-1],[4,-2,8],[-5,-6,7],[-2,3,8],[-7,3,2],[-9,-8,-6],[5,1,-6],[9,-5,8]]], dtype = "int32")#candidate|258|(6, 15, 3)|const|int32
var_259 = relay.var("var_259", dtype = "int32", shape = (6, 15, 3))#candidate|259|(6, 15, 3)|var|int32
bop_260 = relay.minimum(const_258.astype('int32'), relay.reshape(var_259.astype('int32'), relay.shape_of(const_258))) # shape=(6, 15, 3)
uop_266 = relay.acosh(bop_260.astype('float64')) # shape=(6, 15, 3)
var_268 = relay.var("var_268", dtype = "float64", shape = (6, 15, 3))#candidate|268|(6, 15, 3)|var|float64
bop_269 = relay.divide(uop_266.astype('float64'), relay.reshape(var_268.astype('float64'), relay.shape_of(uop_266))) # shape=(6, 15, 3)
output = relay.Tuple([bop_269,])
output2 = relay.Tuple([bop_269,])
func_274 = relay.Function([var_259,var_268,], output)
mod['func_274'] = func_274
mod = relay.transform.InferType()(mod)
mutated_mod['func_274'] = func_274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_274_call = mutated_mod.get_global_var('func_274')
var_276 = relay.var("var_276", dtype = "int32", shape = (6, 15, 3))#candidate|276|(6, 15, 3)|var|int32
var_277 = relay.var("var_277", dtype = "float64", shape = (6, 15, 3))#candidate|277|(6, 15, 3)|var|float64
call_275 = func_274_call(var_276,var_277,)
output = call_275
func_278 = relay.Function([var_276,var_277,], output)
mutated_mod['func_278'] = func_278
mutated_mod = relay.transform.InferType()(mutated_mod)
const_282 = relay.const([[[1.591596,-0.522155,-1.033934,7.329314,-5.103166,7.700824,-2.610779,-8.694016,-1.342506,8.224432,9.121708],[-2.819628,-6.183657,2.284856,-8.945261,-1.640823,-8.639387,-7.658672,6.707611,1.970922,5.023620,-7.192821],[-7.905277,9.102115,-5.961960,1.191184,-5.364844,-5.200803,-9.619919,-6.618510,2.596642,-4.236960,-6.071014],[-6.213210,-6.465796,5.348789,-6.717174,-3.153466,-4.929611,-5.640929,-8.183197,6.748584,2.807593,5.524835],[9.940308,-4.897947,-8.926961,-1.705152,0.485663,-3.105889,5.804309,-1.959553,-0.693079,-1.979864,-9.376150],[6.734879,4.289765,8.369339,8.388524,-5.683751,-2.164240,6.094682,-6.182012,4.038895,-5.064150,5.261287]],[[-9.897608,-5.196819,-4.357543,9.896534,1.298965,-1.228233,9.273556,8.015564,-7.228345,7.136802,5.691099],[-1.301086,2.140494,6.408938,3.884573,6.565128,-7.753144,-8.842306,-6.701391,4.914640,7.780355,-2.936144],[3.065938,4.289518,-3.771418,5.285092,2.063463,6.078033,3.472535,-8.814984,8.240576,-4.563267,3.382597],[6.248290,8.249986,5.198299,-4.934194,2.423944,-3.884366,9.004072,-1.001004,-1.844993,-3.958738,-9.273324],[-1.104837,9.538757,-6.570170,-2.765434,-8.193443,8.112578,-7.857194,-5.339165,5.140045,3.530042,-5.806184],[-1.450002,3.641500,-0.009329,-9.090823,6.620945,-9.695196,-9.420533,3.967230,-2.749298,-6.871020,7.532505]],[[5.893864,9.163514,1.810125,-7.189709,-8.333665,-2.991204,9.845104,9.100133,8.344578,-3.263843,7.723643],[-7.982761,0.771849,7.587896,0.711188,5.934129,-8.505687,3.863252,0.288599,-1.386902,-0.993766,2.512696],[8.106353,4.922345,8.558694,-9.823954,-5.752080,2.938551,-6.167272,-2.681983,8.118093,-6.242969,-4.342965],[-1.084032,4.975459,3.239590,3.639808,2.535542,-4.701205,-9.079405,-1.333005,-2.777680,7.223298,4.131482],[-2.369843,5.901791,6.872528,-7.368243,5.155677,0.428542,1.299264,-2.129229,6.469305,8.068589,-1.486966],[5.590859,8.814855,-4.005877,-7.617692,-5.428296,7.436288,-4.736747,2.148391,-0.132848,4.131068,8.959563]],[[0.844139,-9.467400,9.973619,-9.310428,4.211688,-0.856157,3.127809,6.406506,-8.461353,6.757807,-1.701312],[-7.171926,-5.125617,-8.451317,-4.819514,-7.007452,-5.945800,-8.310511,-7.788901,8.887227,9.496828,-5.287195],[-0.323514,-5.176771,6.081157,-0.053289,8.773551,1.506808,-5.142221,-9.462197,3.538214,-5.981913,0.659025],[0.215150,5.811143,7.573706,3.179685,0.850140,7.704681,-6.567603,8.887014,-1.063811,-0.350698,-3.355196],[-2.466987,4.002140,4.336207,6.618791,8.616881,1.168137,0.726523,3.860399,-2.627809,6.435057,-3.840562],[2.553471,-9.686268,-2.500176,8.806988,9.555752,6.619325,-9.867828,-9.077940,0.939309,-3.310607,-9.620712]],[[0.237562,-2.730346,5.192586,-2.300507,-7.018353,0.050515,9.366377,3.809022,2.714841,-2.332584,4.990163],[1.326588,-5.383194,2.886480,8.888987,8.470420,6.863051,7.984346,0.669240,-9.155736,5.856497,-6.113544],[-2.835069,0.800014,3.468410,-7.855639,-1.647967,-1.575687,8.750935,-5.559655,-4.650267,8.106598,9.041478],[-8.793969,-7.355355,-1.067695,-9.698269,2.090149,-8.031440,-3.552674,-1.142209,0.608138,0.089566,-7.077175],[8.332459,2.604401,-0.805134,-4.168937,6.976860,-3.374854,4.389492,8.176050,6.236078,-4.894638,-2.505456],[6.296896,-2.072729,7.618847,1.225348,-6.517749,-0.920226,-0.494641,-6.208272,5.218680,7.615497,-6.774226]],[[-6.568524,-4.360022,-7.666605,-6.634946,-6.006253,0.132940,-7.575450,-5.485645,-6.228105,-7.147313,-4.189897],[8.002314,8.513000,0.610097,-9.169428,-3.760927,5.466813,2.086093,3.243294,-9.032490,8.037130,-2.945257],[0.626914,1.100368,7.621245,-5.979850,-7.208453,6.153657,-0.032522,-8.717903,-6.854177,-1.999621,-9.673121],[2.907151,4.008160,4.763334,4.096589,-3.595846,-1.154610,4.157097,3.811113,5.174538,9.893340,-6.169339],[7.067514,3.988542,7.855747,-3.580733,4.802051,8.880026,2.057953,7.504218,9.601041,6.629324,-8.712514],[5.714067,5.043649,8.638871,1.196304,-5.057955,3.439016,-9.752032,1.308924,-1.923618,-2.922981,9.581360]],[[-6.799347,7.351466,-3.740383,8.372542,7.723877,3.537901,2.380881,1.561902,-5.007347,-8.622914,0.491208],[-1.271600,9.731420,6.774615,-3.754445,6.312957,-2.918767,-2.344294,-1.336526,7.528094,0.086720,-4.396147],[3.395684,7.550943,9.051288,4.879737,1.216657,-4.885312,-1.886366,-5.594099,-0.687212,6.109085,-9.864196],[-5.125079,4.956618,-2.013134,-7.633918,-0.165533,3.686516,7.632911,8.743738,7.449121,-5.584865,0.565219],[-5.381333,0.779445,1.098597,1.964398,9.837229,-8.069150,2.358986,1.952297,8.782697,3.051149,7.657822],[-4.723679,-9.994741,0.209489,6.432201,2.292730,7.096502,-6.184335,-8.354102,-5.286507,6.637906,-1.419797]]], dtype = "float32")#candidate|282|(7, 6, 11)|const|float32
uop_283 = relay.log10(const_282.astype('float32')) # shape=(7, 6, 11)
uop_298 = relay.log2(const_282.astype('float32')) # shape=(7, 6, 11)
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
const_301 = relay.const(-5, dtype = "uint64")#candidate|301|()|const|uint64
const_302 = relay.const([-6,-4,10,6,-5,9,2,-7,7,-9,-10,-4,7,2,-2,5], dtype = "uint64")#candidate|302|(16,)|const|uint64
call_300 = relay.TupleGetItem(func_107_call(relay.reshape(const_301.astype('uint64'), []), relay.reshape(const_302.astype('uint64'), [1, 16]), ), 0)
call_303 = relay.TupleGetItem(func_111_call(relay.reshape(const_301.astype('uint64'), []), relay.reshape(const_302.astype('uint64'), [1, 16]), ), 0)
output = relay.Tuple([uop_283,uop_298,call_300,const_301,const_302,])
output2 = relay.Tuple([uop_283,uop_298,call_303,const_301,const_302,])
func_320 = relay.Function([], output)
mod['func_320'] = func_320
mod = relay.transform.InferType()(mod)
mutated_mod['func_320'] = func_320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_320_call = mutated_mod.get_global_var('func_320')
call_321 = func_320_call()
output = call_321
func_322 = relay.Function([], output)
mutated_mod['func_322'] = func_322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_320_call = mod.get_global_var('func_320')
func_322_call = mutated_mod.get_global_var('func_322')
call_349 = relay.TupleGetItem(func_320_call(), 3)
call_350 = relay.TupleGetItem(func_322_call(), 3)
output = call_349
output2 = call_350
func_364 = relay.Function([], output)
mod['func_364'] = func_364
mod = relay.transform.InferType()(mod)
mutated_mod['func_364'] = func_364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_364_call = mutated_mod.get_global_var('func_364')
call_365 = func_364_call()
output = call_365
func_366 = relay.Function([], output)
mutated_mod['func_366'] = func_366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_417 = func_364_call()
call_418 = func_364_call()
var_430 = relay.var("var_430", dtype = "uint64", shape = (3, 11, 16))#candidate|430|(3, 11, 16)|var|uint64
bop_431 = relay.logical_xor(call_417.astype('uint32'), var_430.astype('uint32')) # shape=(3, 11, 16)
bop_434 = relay.logical_xor(call_418.astype('uint32'), var_430.astype('uint32')) # shape=(3, 11, 16)
uop_436 = relay.sqrt(var_430.astype('float32')) # shape=(3, 11, 16)
output = relay.Tuple([bop_431,uop_436,])
output2 = relay.Tuple([bop_434,uop_436,])
func_438 = relay.Function([var_430,], output)
mod['func_438'] = func_438
mod = relay.transform.InferType()(mod)
mutated_mod['func_438'] = func_438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_439 = relay.var("var_439", dtype = "uint64", shape = (3, 11, 16))#candidate|439|(3, 11, 16)|var|uint64
func_438_call = mutated_mod.get_global_var('func_438')
call_440 = func_438_call(var_439)
output = call_440
func_441 = relay.Function([var_439], output)
mutated_mod['func_441'] = func_441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_320_call = mod.get_global_var('func_320')
func_322_call = mutated_mod.get_global_var('func_322')
call_462 = relay.TupleGetItem(func_320_call(), 4)
call_463 = relay.TupleGetItem(func_322_call(), 4)
output = call_462
output2 = call_463
func_467 = relay.Function([], output)
mod['func_467'] = func_467
mod = relay.transform.InferType()(mod)
mutated_mod['func_467'] = func_467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_467_call = mutated_mod.get_global_var('func_467')
call_468 = func_467_call()
output = call_468
func_469 = relay.Function([], output)
mutated_mod['func_469'] = func_469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_467_call = mod.get_global_var('func_467')
func_469_call = mutated_mod.get_global_var('func_469')
call_488 = func_467_call()
call_489 = func_467_call()
output = relay.Tuple([call_488,])
output2 = relay.Tuple([call_489,])
func_490 = relay.Function([], output)
mod['func_490'] = func_490
mod = relay.transform.InferType()(mod)
output = func_490()
func_491 = relay.Function([], output)
mutated_mod['func_491'] = func_491
mutated_mod = relay.transform.InferType()(mutated_mod)
var_555 = relay.var("var_555", dtype = "float32", shape = (2, 14, 13))#candidate|555|(2, 14, 13)|var|float32
uop_556 = relay.exp(var_555.astype('float32')) # shape=(2, 14, 13)
output = uop_556
output2 = uop_556
func_560 = relay.Function([var_555,], output)
mod['func_560'] = func_560
mod = relay.transform.InferType()(mod)
var_561 = relay.var("var_561", dtype = "float32", shape = (2, 14, 13))#candidate|561|(2, 14, 13)|var|float32
output = func_560(var_561)
func_562 = relay.Function([var_561], output)
mutated_mod['func_562'] = func_562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_467_call = mod.get_global_var('func_467')
func_469_call = mutated_mod.get_global_var('func_469')
call_584 = func_467_call()
call_585 = func_467_call()
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
const_594 = relay.const(9, dtype = "uint64")#candidate|594|()|const|uint64
call_593 = relay.TupleGetItem(func_107_call(relay.reshape(const_594.astype('uint64'), []), relay.reshape(call_584.astype('uint64'), [1, 16]), ), 0)
call_595 = relay.TupleGetItem(func_111_call(relay.reshape(const_594.astype('uint64'), []), relay.reshape(call_584.astype('uint64'), [1, 16]), ), 0)
func_490_call = mod.get_global_var('func_490')
func_491_call = mutated_mod.get_global_var('func_491')
call_596 = relay.TupleGetItem(func_490_call(), 0)
call_597 = relay.TupleGetItem(func_491_call(), 0)
output = relay.Tuple([call_584,call_593,const_594,call_596,])
output2 = relay.Tuple([call_585,call_595,const_594,call_597,])
func_601 = relay.Function([], output)
mod['func_601'] = func_601
mod = relay.transform.InferType()(mod)
mutated_mod['func_601'] = func_601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_601_call = mutated_mod.get_global_var('func_601')
call_602 = func_601_call()
output = call_602
func_603 = relay.Function([], output)
mutated_mod['func_603'] = func_603
mutated_mod = relay.transform.InferType()(mutated_mod)
var_632 = relay.var("var_632", dtype = "float32", shape = (1, 2, 3))#candidate|632|(1, 2, 3)|var|float32
uop_633 = relay.acos(var_632.astype('float32')) # shape=(1, 2, 3)
output = relay.Tuple([uop_633,])
output2 = relay.Tuple([uop_633,])
func_639 = relay.Function([var_632,], output)
mod['func_639'] = func_639
mod = relay.transform.InferType()(mod)
mutated_mod['func_639'] = func_639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_640 = relay.var("var_640", dtype = "float32", shape = (1, 2, 3))#candidate|640|(1, 2, 3)|var|float32
func_639_call = mutated_mod.get_global_var('func_639')
call_641 = func_639_call(var_640)
output = call_641
func_642 = relay.Function([var_640], output)
mutated_mod['func_642'] = func_642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_700 = func_364_call()
call_701 = func_364_call()
func_467_call = mod.get_global_var('func_467')
func_469_call = mutated_mod.get_global_var('func_469')
call_714 = func_467_call()
call_715 = func_467_call()
output = relay.Tuple([call_700,call_714,])
output2 = relay.Tuple([call_701,call_715,])
func_718 = relay.Function([], output)
mod['func_718'] = func_718
mod = relay.transform.InferType()(mod)
mutated_mod['func_718'] = func_718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mutated_mod.get_global_var('func_718')
call_719 = func_718_call()
output = call_719
func_720 = relay.Function([], output)
mutated_mod['func_720'] = func_720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_747 = relay.TupleGetItem(func_718_call(), 1)
call_748 = relay.TupleGetItem(func_720_call(), 1)
output = call_747
output2 = call_748
func_766 = relay.Function([], output)
mod['func_766'] = func_766
mod = relay.transform.InferType()(mod)
output = func_766()
func_767 = relay.Function([], output)
mutated_mod['func_767'] = func_767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_467_call = mod.get_global_var('func_467')
func_469_call = mutated_mod.get_global_var('func_469')
call_824 = func_467_call()
call_825 = func_467_call()
output = call_824
output2 = call_825
func_854 = relay.Function([], output)
mod['func_854'] = func_854
mod = relay.transform.InferType()(mod)
output = func_854()
func_855 = relay.Function([], output)
mutated_mod['func_855'] = func_855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_893 = func_364_call()
call_894 = func_364_call()
output = call_893
output2 = call_894
func_905 = relay.Function([], output)
mod['func_905'] = func_905
mod = relay.transform.InferType()(mod)
output = func_905()
func_906 = relay.Function([], output)
mutated_mod['func_906'] = func_906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_938 = relay.var("var_938", dtype = "float32", shape = (14, 10, 1))#candidate|938|(14, 10, 1)|var|float32
uop_939 = relay.atanh(var_938.astype('float32')) # shape=(14, 10, 1)
var_946 = relay.var("var_946", dtype = "float32", shape = (14, 10, 1))#candidate|946|(14, 10, 1)|var|float32
bop_947 = relay.bitwise_and(uop_939.astype('int64'), relay.reshape(var_946.astype('int64'), relay.shape_of(uop_939))) # shape=(14, 10, 1)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_958 = func_364_call()
call_959 = func_364_call()
func_639_call = mod.get_global_var('func_639')
func_642_call = mutated_mod.get_global_var('func_642')
const_983 = relay.const([-3.396826,-6.105087,-4.343663,-9.584320,-0.308288,-0.201628], dtype = "float32")#candidate|983|(6,)|const|float32
call_982 = relay.TupleGetItem(func_639_call(relay.reshape(const_983.astype('float32'), [1, 2, 3])), 0)
call_984 = relay.TupleGetItem(func_642_call(relay.reshape(const_983.astype('float32'), [1, 2, 3])), 0)
output = relay.Tuple([bop_947,call_958,call_982,const_983,])
output2 = relay.Tuple([bop_947,call_959,call_984,const_983,])
func_987 = relay.Function([var_938,var_946,], output)
mod['func_987'] = func_987
mod = relay.transform.InferType()(mod)
mutated_mod['func_987'] = func_987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_987_call = mutated_mod.get_global_var('func_987')
var_989 = relay.var("var_989", dtype = "float32", shape = (14, 10, 1))#candidate|989|(14, 10, 1)|var|float32
var_990 = relay.var("var_990", dtype = "float32", shape = (14, 10, 1))#candidate|990|(14, 10, 1)|var|float32
call_988 = func_987_call(var_989,var_990,)
output = call_988
func_991 = relay.Function([var_989,var_990,], output)
mutated_mod['func_991'] = func_991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_490_call = mod.get_global_var('func_490')
func_491_call = mutated_mod.get_global_var('func_491')
call_1008 = relay.TupleGetItem(func_490_call(), 0)
call_1009 = relay.TupleGetItem(func_491_call(), 0)
func_467_call = mod.get_global_var('func_467')
func_469_call = mutated_mod.get_global_var('func_469')
call_1018 = func_467_call()
call_1019 = func_467_call()
output = relay.Tuple([call_1008,call_1018,])
output2 = relay.Tuple([call_1009,call_1019,])
func_1039 = relay.Function([], output)
mod['func_1039'] = func_1039
mod = relay.transform.InferType()(mod)
mutated_mod['func_1039'] = func_1039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1039_call = mutated_mod.get_global_var('func_1039')
call_1040 = func_1039_call()
output = call_1040
func_1041 = relay.Function([], output)
mutated_mod['func_1041'] = func_1041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_490_call = mod.get_global_var('func_490')
func_491_call = mutated_mod.get_global_var('func_491')
call_1069 = relay.TupleGetItem(func_490_call(), 0)
call_1070 = relay.TupleGetItem(func_491_call(), 0)
output = relay.Tuple([call_1069,])
output2 = relay.Tuple([call_1070,])
func_1084 = relay.Function([], output)
mod['func_1084'] = func_1084
mod = relay.transform.InferType()(mod)
output = func_1084()
func_1085 = relay.Function([], output)
mutated_mod['func_1085'] = func_1085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_1095 = func_766_call()
call_1096 = func_766_call()
output = relay.Tuple([call_1095,])
output2 = relay.Tuple([call_1096,])
func_1097 = relay.Function([], output)
mod['func_1097'] = func_1097
mod = relay.transform.InferType()(mod)
output = func_1097()
func_1098 = relay.Function([], output)
mutated_mod['func_1098'] = func_1098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1099 = relay.TupleGetItem(func_1097_call(), 0)
call_1100 = relay.TupleGetItem(func_1098_call(), 0)
output = call_1099
output2 = call_1100
func_1116 = relay.Function([], output)
mod['func_1116'] = func_1116
mod = relay.transform.InferType()(mod)
mutated_mod['func_1116'] = func_1116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mutated_mod.get_global_var('func_1116')
call_1117 = func_1116_call()
output = call_1117
func_1118 = relay.Function([], output)
mutated_mod['func_1118'] = func_1118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_320_call = mod.get_global_var('func_320')
func_322_call = mutated_mod.get_global_var('func_322')
call_1232 = relay.TupleGetItem(func_320_call(), 4)
call_1233 = relay.TupleGetItem(func_322_call(), 4)
func_560_call = mod.get_global_var('func_560')
func_562_call = mutated_mod.get_global_var('func_562')
var_1240 = relay.var("var_1240", dtype = "float32", shape = (364,))#candidate|1240|(364,)|var|float32
call_1239 = func_560_call(relay.reshape(var_1240.astype('float32'), [2, 14, 13]))
call_1241 = func_560_call(relay.reshape(var_1240.astype('float32'), [2, 14, 13]))
output = relay.Tuple([call_1232,call_1239,var_1240,])
output2 = relay.Tuple([call_1233,call_1241,var_1240,])
func_1250 = relay.Function([var_1240,], output)
mod['func_1250'] = func_1250
mod = relay.transform.InferType()(mod)
var_1251 = relay.var("var_1251", dtype = "float32", shape = (364,))#candidate|1251|(364,)|var|float32
output = func_1250(var_1251)
func_1252 = relay.Function([var_1251], output)
mutated_mod['func_1252'] = func_1252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_1293 = relay.TupleGetItem(func_601_call(), 2)
call_1294 = relay.TupleGetItem(func_603_call(), 2)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_1300 = relay.TupleGetItem(func_718_call(), 0)
call_1301 = relay.TupleGetItem(func_720_call(), 0)
func_560_call = mod.get_global_var('func_560')
func_562_call = mutated_mod.get_global_var('func_562')
var_1321 = relay.var("var_1321", dtype = "float32", shape = (364,))#candidate|1321|(364,)|var|float32
call_1320 = func_560_call(relay.reshape(var_1321.astype('float32'), [2, 14, 13]))
call_1322 = func_560_call(relay.reshape(var_1321.astype('float32'), [2, 14, 13]))
func_1039_call = mod.get_global_var('func_1039')
func_1041_call = mutated_mod.get_global_var('func_1041')
call_1326 = relay.TupleGetItem(func_1039_call(), 1)
call_1327 = relay.TupleGetItem(func_1041_call(), 1)
func_905_call = mod.get_global_var('func_905')
func_906_call = mutated_mod.get_global_var('func_906')
call_1335 = func_905_call()
call_1336 = func_905_call()
uop_1348 = relay.sqrt(var_1321.astype('float32')) # shape=(364,)
uop_1355 = relay.cos(uop_1348.astype('float64')) # shape=(364,)
output = relay.Tuple([call_1293,call_1300,call_1320,call_1326,call_1335,uop_1355,])
output2 = relay.Tuple([call_1294,call_1301,call_1322,call_1327,call_1336,uop_1355,])
func_1358 = relay.Function([var_1321,], output)
mod['func_1358'] = func_1358
mod = relay.transform.InferType()(mod)
var_1359 = relay.var("var_1359", dtype = "float32", shape = (364,))#candidate|1359|(364,)|var|float32
output = func_1358(var_1359)
func_1360 = relay.Function([var_1359], output)
mutated_mod['func_1360'] = func_1360
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1396 = relay.var("var_1396", dtype = "float64", shape = (16, 15, 11))#candidate|1396|(16, 15, 11)|var|float64
uop_1397 = relay.sigmoid(var_1396.astype('float64')) # shape=(16, 15, 11)
uop_1400 = relay.sqrt(var_1396.astype('float32')) # shape=(16, 15, 11)
bop_1405 = relay.divide(uop_1400.astype('float64'), relay.reshape(uop_1397.astype('float64'), relay.shape_of(uop_1400))) # shape=(16, 15, 11)
var_1412 = relay.var("var_1412", dtype = "float32", shape = (16, 15, 11))#candidate|1412|(16, 15, 11)|var|float32
bop_1413 = relay.floor_divide(uop_1400.astype('float64'), relay.reshape(var_1412.astype('float64'), relay.shape_of(uop_1400))) # shape=(16, 15, 11)
func_1039_call = mod.get_global_var('func_1039')
func_1041_call = mutated_mod.get_global_var('func_1041')
call_1420 = relay.TupleGetItem(func_1039_call(), 1)
call_1421 = relay.TupleGetItem(func_1041_call(), 1)
output = relay.Tuple([bop_1405,bop_1413,call_1420,])
output2 = relay.Tuple([bop_1405,bop_1413,call_1421,])
func_1422 = relay.Function([var_1396,var_1412,], output)
mod['func_1422'] = func_1422
mod = relay.transform.InferType()(mod)
mutated_mod['func_1422'] = func_1422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1422_call = mutated_mod.get_global_var('func_1422')
var_1424 = relay.var("var_1424", dtype = "float64", shape = (16, 15, 11))#candidate|1424|(16, 15, 11)|var|float64
var_1425 = relay.var("var_1425", dtype = "float32", shape = (16, 15, 11))#candidate|1425|(16, 15, 11)|var|float32
call_1423 = func_1422_call(var_1424,var_1425,)
output = call_1423
func_1426 = relay.Function([var_1424,var_1425,], output)
mutated_mod['func_1426'] = func_1426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1438 = relay.TupleGetItem(func_1097_call(), 0)
call_1439 = relay.TupleGetItem(func_1098_call(), 0)
func_905_call = mod.get_global_var('func_905')
func_906_call = mutated_mod.get_global_var('func_906')
call_1463 = func_905_call()
call_1464 = func_905_call()
output = relay.Tuple([call_1438,call_1463,])
output2 = relay.Tuple([call_1439,call_1464,])
func_1485 = relay.Function([], output)
mod['func_1485'] = func_1485
mod = relay.transform.InferType()(mod)
output = func_1485()
func_1486 = relay.Function([], output)
mutated_mod['func_1486'] = func_1486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_467_call = mod.get_global_var('func_467')
func_469_call = mutated_mod.get_global_var('func_469')
call_1524 = func_467_call()
call_1525 = func_467_call()
output = call_1524
output2 = call_1525
func_1539 = relay.Function([], output)
mod['func_1539'] = func_1539
mod = relay.transform.InferType()(mod)
output = func_1539()
func_1540 = relay.Function([], output)
mutated_mod['func_1540'] = func_1540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_1627 = func_766_call()
call_1628 = func_766_call()
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1629 = relay.TupleGetItem(func_1097_call(), 0)
call_1630 = relay.TupleGetItem(func_1098_call(), 0)
func_987_call = mod.get_global_var('func_987')
func_991_call = mutated_mod.get_global_var('func_991')
var_1638 = relay.var("var_1638", dtype = "float32", shape = (140,))#candidate|1638|(140,)|var|float32
call_1637 = relay.TupleGetItem(func_987_call(relay.reshape(var_1638.astype('float32'), [14, 10, 1]), relay.reshape(var_1638.astype('float32'), [14, 10, 1]), ), 0)
call_1639 = relay.TupleGetItem(func_991_call(relay.reshape(var_1638.astype('float32'), [14, 10, 1]), relay.reshape(var_1638.astype('float32'), [14, 10, 1]), ), 0)
func_854_call = mod.get_global_var('func_854')
func_855_call = mutated_mod.get_global_var('func_855')
call_1640 = func_854_call()
call_1641 = func_854_call()
output = relay.Tuple([call_1627,call_1629,call_1637,var_1638,call_1640,])
output2 = relay.Tuple([call_1628,call_1630,call_1639,var_1638,call_1641,])
func_1656 = relay.Function([var_1638,], output)
mod['func_1656'] = func_1656
mod = relay.transform.InferType()(mod)
var_1657 = relay.var("var_1657", dtype = "float32", shape = (140,))#candidate|1657|(140,)|var|float32
output = func_1656(var_1657)
func_1658 = relay.Function([var_1657], output)
mutated_mod['func_1658'] = func_1658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_467_call = mod.get_global_var('func_467')
func_469_call = mutated_mod.get_global_var('func_469')
call_1776 = func_467_call()
call_1777 = func_467_call()
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_1781 = relay.TupleGetItem(func_601_call(), 3)
call_1782 = relay.TupleGetItem(func_603_call(), 3)
output = relay.Tuple([call_1776,call_1781,])
output2 = relay.Tuple([call_1777,call_1782,])
func_1793 = relay.Function([], output)
mod['func_1793'] = func_1793
mod = relay.transform.InferType()(mod)
mutated_mod['func_1793'] = func_1793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1793_call = mutated_mod.get_global_var('func_1793')
call_1794 = func_1793_call()
output = call_1794
func_1795 = relay.Function([], output)
mutated_mod['func_1795'] = func_1795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_320_call = mod.get_global_var('func_320')
func_322_call = mutated_mod.get_global_var('func_322')
call_1858 = relay.TupleGetItem(func_320_call(), 3)
call_1859 = relay.TupleGetItem(func_322_call(), 3)
output = call_1858
output2 = call_1859
func_1861 = relay.Function([], output)
mod['func_1861'] = func_1861
mod = relay.transform.InferType()(mod)
mutated_mod['func_1861'] = func_1861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1861_call = mutated_mod.get_global_var('func_1861')
call_1862 = func_1861_call()
output = call_1862
func_1863 = relay.Function([], output)
mutated_mod['func_1863'] = func_1863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_1896 = func_1116_call()
call_1897 = func_1116_call()
output = relay.Tuple([call_1896,])
output2 = relay.Tuple([call_1897,])
func_1904 = relay.Function([], output)
mod['func_1904'] = func_1904
mod = relay.transform.InferType()(mod)
output = func_1904()
func_1905 = relay.Function([], output)
mutated_mod['func_1905'] = func_1905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1485_call = mod.get_global_var('func_1485')
func_1486_call = mutated_mod.get_global_var('func_1486')
call_1955 = relay.TupleGetItem(func_1485_call(), 0)
call_1956 = relay.TupleGetItem(func_1486_call(), 0)
output = call_1955
output2 = call_1956
func_1957 = relay.Function([], output)
mod['func_1957'] = func_1957
mod = relay.transform.InferType()(mod)
mutated_mod['func_1957'] = func_1957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1957_call = mutated_mod.get_global_var('func_1957')
call_1958 = func_1957_call()
output = call_1958
func_1959 = relay.Function([], output)
mutated_mod['func_1959'] = func_1959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_1967 = relay.TupleGetItem(func_718_call(), 0)
call_1968 = relay.TupleGetItem(func_720_call(), 0)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_2025 = func_364_call()
call_2026 = func_364_call()
output = relay.Tuple([call_1967,call_2025,])
output2 = relay.Tuple([call_1968,call_2026,])
func_2083 = relay.Function([], output)
mod['func_2083'] = func_2083
mod = relay.transform.InferType()(mod)
mutated_mod['func_2083'] = func_2083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2083_call = mutated_mod.get_global_var('func_2083')
call_2084 = func_2083_call()
output = call_2084
func_2085 = relay.Function([], output)
mutated_mod['func_2085'] = func_2085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_320_call = mod.get_global_var('func_320')
func_322_call = mutated_mod.get_global_var('func_322')
call_2159 = relay.TupleGetItem(func_320_call(), 0)
call_2160 = relay.TupleGetItem(func_322_call(), 0)
func_1039_call = mod.get_global_var('func_1039')
func_1041_call = mutated_mod.get_global_var('func_1041')
call_2183 = relay.TupleGetItem(func_1039_call(), 1)
call_2184 = relay.TupleGetItem(func_1041_call(), 1)
output = relay.Tuple([call_2159,call_2183,])
output2 = relay.Tuple([call_2160,call_2184,])
func_2186 = relay.Function([], output)
mod['func_2186'] = func_2186
mod = relay.transform.InferType()(mod)
output = func_2186()
func_2187 = relay.Function([], output)
mutated_mod['func_2187'] = func_2187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_2260 = relay.TupleGetItem(func_1097_call(), 0)
call_2261 = relay.TupleGetItem(func_1098_call(), 0)
func_467_call = mod.get_global_var('func_467')
func_469_call = mutated_mod.get_global_var('func_469')
call_2264 = func_467_call()
call_2265 = func_467_call()
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_2283 = relay.TupleGetItem(func_718_call(), 0)
call_2284 = relay.TupleGetItem(func_720_call(), 0)
func_1358_call = mod.get_global_var('func_1358')
func_1360_call = mutated_mod.get_global_var('func_1360')
const_2310 = relay.const([-0.662295,-5.067477,-7.064610,6.289790,9.110201,0.812063,-9.652671,1.420514,-0.806665,-9.699243,-2.545277,8.065684,-2.512303,1.641135,3.080373,5.729402,9.783995,-7.833542,-0.822520,9.560846,-0.063554,8.458203,5.172371,2.829816,9.368440,-7.173460,-0.916962,-8.916453,-1.893361,-6.929939,9.399906,0.815360,8.054403,-6.462960,-2.294360,5.701538,-7.966013,4.463815,2.783147,3.042533,-5.232660,-6.496951,5.872773,7.224567,-3.670219,-0.467634,6.134178,-1.218211,4.696322,-0.901348,4.993328,-5.606878,-7.700660,1.921405,1.319155,-0.085074,-4.914381,-5.276363,4.874990,0.148860,5.616548,8.547287,-9.486992,-4.631132,-6.654531,7.888513,-5.552022,4.282816,0.153180,4.017456,5.216534,-1.198613,-9.402714,4.681011,-9.432196,-6.229853,-0.869095,-2.673165,8.723270,3.153883,4.249393,7.433909,-1.244344,-4.725716,1.451030,-5.919698,3.815300,-1.187820,8.340253,7.616558,4.493163,-0.750002,4.659943,-9.028584,0.512148,-5.739418,-2.719818,-6.540878,-1.208002,-4.681735,-8.630703,-0.494912,9.490609,-4.764309,-5.312303,-3.040700,2.449195,-9.189195,8.195822,8.401442,-5.489941,8.255755,-0.633368,2.030358,-6.801524,-6.216429,9.894697,-5.790353,-5.604593,7.000016,-5.307954,-9.188403,-8.602070,-8.064235,8.680446,-6.973425,4.356139,-9.545602,-1.094670,-2.306242,5.599560,2.197567,2.738658,4.462930,-8.000889,-5.516873,-9.010778,-4.862019,4.667715,-9.620295,0.664811,-8.667341,-4.069206,-2.335700,0.067960,3.676695,1.264754,9.099223,-0.218583,-0.567045,6.233864,6.502210,8.670381,6.533709,-7.475663,5.425606,-7.761061,-9.372678,-8.103656,2.321751,4.584100,-7.207432,-7.192925,8.141850,-0.580127,4.592787,-0.236384,5.444989,4.772515,7.211058,-2.059908,7.805164,-7.587877,8.055825,-6.628767,-2.737611,9.513468,-2.660658,-9.254846,-7.623608,-3.990699,7.899570,-6.719243,-7.133051,9.972728,6.200550,7.630794,-6.908618,-1.323726,-7.121085,5.265891,-4.394393,-9.067656,-1.833064,-5.180133,5.986268,-5.392326,-1.487168,-2.474258,-1.714116,-6.955869,2.222880,-5.639574,7.464624,-9.277361,3.306694,1.784687,-7.242031,9.912957,-1.884875,-9.065086,-3.231875,-8.417261,1.761103,5.894425,-3.281451,-5.600035,0.109180,-6.061815,1.691562,6.562499,-0.764498,5.130142,-2.849950,4.041017,-3.621387,-1.235655,-9.094745,4.950184,4.009344,-2.471030,-5.570126,-7.864729,4.931950,2.905456,4.887994,-4.013657,8.451526,-0.385964,-1.667893,-0.056533,0.922446,2.280213,-2.968339,-7.689809,1.054602,2.594137,8.514542,-4.700621,-5.332486,8.539235,-5.965548,6.870176,4.959705,6.231204,3.928440,5.135770,-9.401921,3.530814,8.536271,4.747750,-5.700717,7.233726,-9.856621,-2.518343,0.979833,-3.086736,3.514921,9.313774,6.042274,-4.540764,-0.892427,-3.242361,-8.100433,7.714242,1.277693,1.640472,-8.696592,9.832315,-6.768510,6.323719,4.297360,2.650013,-1.519039,-2.171786,7.334826,-5.356126,-3.697663,-5.050484,-8.160925,-0.718417,-4.726855,6.225288,-0.150278,3.785199,2.051034,-3.285390,-3.026985,4.159000,-4.729897,8.636816,6.304863,-9.677456,-6.468448,-0.495829,-0.139784,-4.524572,-2.160295,2.627411,-7.919481,7.022695,-9.863539,-2.009104,2.487093,6.538605,7.557757,2.582538,-3.523529,-1.160058,9.073298,-3.339525,-4.983015,-6.494421,-4.333360,6.672477,3.739771,-3.004974,7.591503,-1.141242,5.068308,-4.402416,-0.081600,4.546007,5.695511,8.604179,-9.309734,1.498320,-6.000101,-3.172928,7.505414,3.748368,-9.676046,-3.906734,9.830206,6.558382,-8.400894,4.960345,4.625552,-8.737204,6.258801,1.356594,6.363626,-5.848231,3.753497,-9.966060,-1.730912,5.476085,-8.874391,-9.813820,-6.082623,-1.500918,-1.313481,-8.216389,-1.250800], dtype = "float32")#candidate|2310|(364,)|const|float32
call_2309 = relay.TupleGetItem(func_1358_call(relay.reshape(const_2310.astype('float32'), [364,])), 0)
call_2311 = relay.TupleGetItem(func_1360_call(relay.reshape(const_2310.astype('float32'), [364,])), 0)
uop_2323 = relay.acosh(const_2310.astype('float32')) # shape=(364,)
output = relay.Tuple([call_2260,call_2264,call_2283,call_2309,uop_2323,])
output2 = relay.Tuple([call_2261,call_2265,call_2284,call_2311,uop_2323,])
func_2326 = relay.Function([], output)
mod['func_2326'] = func_2326
mod = relay.transform.InferType()(mod)
mutated_mod['func_2326'] = func_2326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2326_call = mutated_mod.get_global_var('func_2326')
call_2327 = func_2326_call()
output = call_2327
func_2328 = relay.Function([], output)
mutated_mod['func_2328'] = func_2328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2083_call = mod.get_global_var('func_2083')
func_2085_call = mutated_mod.get_global_var('func_2085')
call_2367 = relay.TupleGetItem(func_2083_call(), 1)
call_2368 = relay.TupleGetItem(func_2085_call(), 1)
func_1656_call = mod.get_global_var('func_1656')
func_1658_call = mutated_mod.get_global_var('func_1658')
var_2375 = relay.var("var_2375", dtype = "float32", shape = (140,))#candidate|2375|(140,)|var|float32
call_2374 = relay.TupleGetItem(func_1656_call(relay.reshape(var_2375.astype('float32'), [140,])), 0)
call_2376 = relay.TupleGetItem(func_1658_call(relay.reshape(var_2375.astype('float32'), [140,])), 0)
bop_2377 = relay.greater_equal(var_2375.astype('bool'), call_2367.astype('bool')) # shape=(140,)
bop_2380 = relay.greater_equal(var_2375.astype('bool'), call_2368.astype('bool')) # shape=(140,)
bop_2385 = relay.add(call_2367.astype('int64'), var_2375.astype('int64')) # shape=(140,)
bop_2388 = relay.add(call_2368.astype('int64'), var_2375.astype('int64')) # shape=(140,)
func_1861_call = mod.get_global_var('func_1861')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_2403 = func_1861_call()
call_2404 = func_1861_call()
output = relay.Tuple([call_2374,bop_2377,bop_2385,call_2403,])
output2 = relay.Tuple([call_2376,bop_2380,bop_2388,call_2404,])
func_2405 = relay.Function([var_2375,], output)
mod['func_2405'] = func_2405
mod = relay.transform.InferType()(mod)
var_2406 = relay.var("var_2406", dtype = "float32", shape = (140,))#candidate|2406|(140,)|var|float32
output = func_2405(var_2406)
func_2407 = relay.Function([var_2406], output)
mutated_mod['func_2407'] = func_2407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1039_call = mod.get_global_var('func_1039')
func_1041_call = mutated_mod.get_global_var('func_1041')
call_2427 = relay.TupleGetItem(func_1039_call(), 0)
call_2428 = relay.TupleGetItem(func_1041_call(), 0)
output = relay.Tuple([call_2427,])
output2 = relay.Tuple([call_2428,])
func_2449 = relay.Function([], output)
mod['func_2449'] = func_2449
mod = relay.transform.InferType()(mod)
mutated_mod['func_2449'] = func_2449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2449_call = mutated_mod.get_global_var('func_2449')
call_2450 = func_2449_call()
output = call_2450
func_2451 = relay.Function([], output)
mutated_mod['func_2451'] = func_2451
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2532 = relay.var("var_2532", dtype = "float32", shape = (7, 16, 13))#candidate|2532|(7, 16, 13)|var|float32
uop_2533 = relay.asin(var_2532.astype('float32')) # shape=(7, 16, 13)
func_2405_call = mod.get_global_var('func_2405')
func_2407_call = mutated_mod.get_global_var('func_2407')
var_2547 = relay.var("var_2547", dtype = "float32", shape = (35, 4))#candidate|2547|(35, 4)|var|float32
call_2546 = relay.TupleGetItem(func_2405_call(relay.reshape(var_2547.astype('float32'), [140,])), 1)
call_2548 = relay.TupleGetItem(func_2407_call(relay.reshape(var_2547.astype('float32'), [140,])), 1)
var_2551 = relay.var("var_2551", dtype = "float32", shape = (35, 4))#candidate|2551|(35, 4)|var|float32
bop_2552 = relay.greater(var_2547.astype('bool'), relay.reshape(var_2551.astype('bool'), relay.shape_of(var_2547))) # shape=(35, 4)
uop_2555 = relay.log(uop_2533.astype('float32')) # shape=(7, 16, 13)
func_1793_call = mod.get_global_var('func_1793')
func_1795_call = mutated_mod.get_global_var('func_1795')
call_2588 = relay.TupleGetItem(func_1793_call(), 0)
call_2589 = relay.TupleGetItem(func_1795_call(), 0)
bop_2590 = relay.add(uop_2555.astype('int16'), relay.reshape(var_2532.astype('int16'), relay.shape_of(uop_2555))) # shape=(7, 16, 13)
func_438_call = mod.get_global_var('func_438')
func_441_call = mutated_mod.get_global_var('func_441')
const_2595 = relay.const([9,-3,1,-5,-6,2,-2,2,-7,5,-4,3,10,-2,-7,10,-6,-5,3,-5,10,2,6,4,-3,-7,2,6,4,-3,-6,8,-8,-1,4,9,-5,8,9,3,10,8,1,-4,-3,-7,1,-10,-10,-9,9,10,3,5,1,1,-1,-3,-4,-7,-5,-5,-2,5,-10,-8,-4,-4,10,8,-9,-1,1,-3,3,3,6,4,5,-2,4,3,-2,-7,-6,2,-6,-8,-10,-2,-10,-9,-3,8,2,2,-4,6,-1,8,7,-5,-6,-10,3,-7,8,-1,1,-10,1,-1,-8,9,-9,9,9,-9,-6,-9,-2,1,-4,-3,-4,-10,-5,-8,-7,2,-5,1,4,7,10,6,2,-4,-2,3,-7,10,3,7,-6,3,-10,3,6,-4,8,8,9,-8,8,8,-4,9,4,-5,-3,-2,-5,-8,7,-7,4,-4,-7,6,4,1,10,-5,-6,-5,-1,3,-3,6,3,-4,-9,1,-3,-3,9,-6,6,3,2,-2,-6,10,7,9,9,8,6,-6,-4,-7,-7,-2,-6,6,7,-2,2,-4,8,-9,-9,-5,-6,-3,3,3,-4,-2,2,-8,-5,-3,2,6,-3,9,3,6,-6,-10,-10,7,-10,4,-9,2,-3,-1,-4,-7,5,8,9,-7,-4,3,2,10,3,3,-4,-3,9,2,-4,-8,-4,-7,2,-9,3,-4,4,-6,-6,6,-1,7,-5,-3,9,-8,-2,7,10,-2,-7,-9,-10,5,-3,4,-2,-6,-3,7,-2,6,-1,8,8,-8,8,-4,-4,2,2,3,-10,-2,-10,2,6,-6,10,10,-5,3,-6,10,5,-9,-2,2,1,-3,-5,-3,-5,-9,2,-5,6,10,4,-3,-6,8,3,7,6,-7,7,3,8,10,-9,-8,-2,8,2,5,-2,-3,-4,10,-4,-10,-6,4,-3,5,1,9,-4,9,6,2,-6,-4,-9,10,-1,6,-3,1,-7,10,-10,1,-5,7,-2,-9,8,-1,-8,-2,-3,-4,9,4,2,3,-4,3,3,-9,3,-7,1,-1,1,6,2,-2,-7,-6,-2,-8,-3,4,-3,3,2,8,-10,-2,2,6,-10,-4,7,-6,1,7,-5,2,-5,7,-6,3,-5,8,-3,-1,5,1,-9,4,1,6,4,7,4,9,8,-8,6,-10,2,-3,-1,2,-3,10,8,3,5,-3,1,-8,3,4,2,8,7,1,-8,-8,9,-7,5,1,10,-8,6,-2,2,6,-9,-9,6,8,3,6,-5,1,5,-9,-5,-5,-3,-10,4,10,-10,2,9,1,8,-5,4,-3,7,-3,-9,3,-7,6,1,-5,-4,-9,10,4,1,9,3,-4,5,5,8,-7,-3,6,-8,-4,-1,5,5,9,9,1,1,-6], dtype = "uint64")#candidate|2595|(528,)|const|uint64
call_2594 = relay.TupleGetItem(func_438_call(relay.reshape(const_2595.astype('uint64'), [3, 11, 16])), 1)
call_2596 = relay.TupleGetItem(func_441_call(relay.reshape(const_2595.astype('uint64'), [3, 11, 16])), 1)
uop_2598 = relay.exp(uop_2555.astype('float64')) # shape=(7, 16, 13)
func_1793_call = mod.get_global_var('func_1793')
func_1795_call = mutated_mod.get_global_var('func_1795')
call_2602 = relay.TupleGetItem(func_1793_call(), 1)
call_2603 = relay.TupleGetItem(func_1795_call(), 1)
func_2449_call = mod.get_global_var('func_2449')
func_2451_call = mutated_mod.get_global_var('func_2451')
call_2609 = relay.TupleGetItem(func_2449_call(), 0)
call_2610 = relay.TupleGetItem(func_2451_call(), 0)
func_1904_call = mod.get_global_var('func_1904')
func_1905_call = mutated_mod.get_global_var('func_1905')
call_2614 = relay.TupleGetItem(func_1904_call(), 0)
call_2615 = relay.TupleGetItem(func_1905_call(), 0)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
call_2623 = relay.TupleGetItem(func_2326_call(), 4)
call_2624 = relay.TupleGetItem(func_2328_call(), 4)
func_438_call = mod.get_global_var('func_438')
func_441_call = mutated_mod.get_global_var('func_441')
call_2634 = relay.TupleGetItem(func_438_call(relay.reshape(call_2594.astype('uint64'), [3, 11, 16])), 1)
call_2635 = relay.TupleGetItem(func_441_call(relay.reshape(call_2594.astype('uint64'), [3, 11, 16])), 1)
output = relay.Tuple([call_2546,bop_2552,call_2588,bop_2590,call_2594,const_2595,uop_2598,call_2602,call_2609,call_2614,call_2623,call_2634,])
output2 = relay.Tuple([call_2548,bop_2552,call_2589,bop_2590,call_2596,const_2595,uop_2598,call_2603,call_2610,call_2615,call_2624,call_2635,])
func_2636 = relay.Function([var_2532,var_2547,var_2551,], output)
mod['func_2636'] = func_2636
mod = relay.transform.InferType()(mod)
var_2637 = relay.var("var_2637", dtype = "float32", shape = (7, 16, 13))#candidate|2637|(7, 16, 13)|var|float32
var_2638 = relay.var("var_2638", dtype = "float32", shape = (35, 4))#candidate|2638|(35, 4)|var|float32
var_2639 = relay.var("var_2639", dtype = "float32", shape = (35, 4))#candidate|2639|(35, 4)|var|float32
output = func_2636(var_2637,var_2638,var_2639,)
func_2640 = relay.Function([var_2637,var_2638,var_2639,], output)
mutated_mod['func_2640'] = func_2640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_320_call = mod.get_global_var('func_320')
func_322_call = mutated_mod.get_global_var('func_322')
call_2656 = relay.TupleGetItem(func_320_call(), 2)
call_2657 = relay.TupleGetItem(func_322_call(), 2)
output = call_2656
output2 = call_2657
func_2664 = relay.Function([], output)
mod['func_2664'] = func_2664
mod = relay.transform.InferType()(mod)
mutated_mod['func_2664'] = func_2664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2664_call = mutated_mod.get_global_var('func_2664')
call_2665 = func_2664_call()
output = call_2665
func_2666 = relay.Function([], output)
mutated_mod['func_2666'] = func_2666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1485_call = mod.get_global_var('func_1485')
func_1486_call = mutated_mod.get_global_var('func_1486')
call_2673 = relay.TupleGetItem(func_1485_call(), 1)
call_2674 = relay.TupleGetItem(func_1486_call(), 1)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
call_2683 = relay.TupleGetItem(func_2326_call(), 3)
call_2684 = relay.TupleGetItem(func_2328_call(), 3)
output = relay.Tuple([call_2673,call_2683,])
output2 = relay.Tuple([call_2674,call_2684,])
func_2687 = relay.Function([], output)
mod['func_2687'] = func_2687
mod = relay.transform.InferType()(mod)
output = func_2687()
func_2688 = relay.Function([], output)
mutated_mod['func_2688'] = func_2688
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2693 = relay.var("var_2693", dtype = "float64", shape = (9, 8, 3))#candidate|2693|(9, 8, 3)|var|float64
const_2694 = relay.const([[[9.301209,3.540110,0.321668],[7.211441,4.803501,-2.964821],[-1.805877,-5.349872,-4.172045],[5.978657,8.614653,8.696626],[-3.380800,-4.625518,-0.680608],[8.917721,-2.285352,4.864398],[8.390881,-0.729415,8.457379],[-6.337379,-7.362440,3.764906]],[[-3.733003,8.397608,9.956207],[0.779803,3.827253,-2.324345],[3.966392,2.657790,-1.535332],[7.453542,-5.946428,-3.752785],[8.586891,4.623190,-0.698314],[-3.314755,0.213135,-0.109691],[-5.444152,-4.434909,-4.794026],[-7.786343,0.576146,0.070330]],[[-1.584748,9.506735,2.784567],[-0.136367,-5.576023,-1.510232],[9.808861,4.608276,7.517867],[2.373695,0.309643,0.413223],[-4.642310,-9.763927,-4.136921],[0.734376,-1.197988,4.812670],[7.139363,-8.556034,6.534479],[-7.546681,2.428449,0.747381]],[[4.809564,8.859253,-5.811296],[-6.431153,-6.380637,-3.692505],[2.000259,5.777589,1.148228],[0.653577,-6.265443,-8.401757],[-6.549722,-4.888249,7.448923],[-1.994686,5.929504,6.000444],[6.834777,-2.582454,-9.998695],[-6.793996,8.796781,-1.087873]],[[-3.044314,5.896050,4.170054],[-1.955129,-0.475204,-5.062017],[-7.607444,-8.877020,-5.568830],[3.160775,-2.231069,5.127509],[1.109420,-9.698433,9.859886],[0.707401,-7.615449,-2.624218],[-8.368896,8.923168,-8.979142],[-7.774052,0.731219,-9.414054]],[[3.992460,8.453184,4.054794],[-5.345366,-7.682295,9.045464],[6.581691,6.080464,2.790245],[-0.728987,-9.287112,-7.896287],[6.497114,6.669695,-7.775976],[-8.021692,8.213906,6.860365],[-3.940979,9.691836,-1.936404],[-4.833939,1.379692,1.707626]],[[9.890589,6.349547,8.657189],[-5.250305,-2.198441,3.005461],[7.560216,-2.565233,7.254675],[-1.198739,-7.887938,-0.303667],[-7.259175,-3.455633,-2.275075],[5.087554,3.476352,1.519189],[-2.647979,2.763648,1.992456],[8.937981,-3.734531,-9.318479]],[[3.413426,3.826831,-3.224459],[-5.820000,-9.879865,6.059387],[-6.835927,8.427994,5.898282],[1.617908,-7.766237,-6.527392],[7.362302,6.634779,-7.743815],[-0.729820,-6.829253,9.911062],[7.038281,2.981968,-2.901292],[0.257005,7.854652,2.874052]],[[5.241090,9.029963,7.904487],[-2.606271,7.828625,0.676256],[9.846283,-9.025293,2.041053],[-9.598895,4.918243,8.507054],[-2.830139,5.239635,1.990382],[-5.736646,7.291726,-4.491209],[-1.436209,6.234822,-2.779280],[0.674627,-8.224770,6.566684]]], dtype = "float64")#candidate|2694|(9, 8, 3)|const|float64
bop_2695 = relay.divide(var_2693.astype('float64'), relay.reshape(const_2694.astype('float64'), relay.shape_of(var_2693))) # shape=(9, 8, 3)
output = relay.Tuple([bop_2695,])
output2 = relay.Tuple([bop_2695,])
func_2700 = relay.Function([var_2693,], output)
mod['func_2700'] = func_2700
mod = relay.transform.InferType()(mod)
mutated_mod['func_2700'] = func_2700
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2701 = relay.var("var_2701", dtype = "float64", shape = (9, 8, 3))#candidate|2701|(9, 8, 3)|var|float64
func_2700_call = mutated_mod.get_global_var('func_2700')
call_2702 = func_2700_call(var_2701)
output = call_2702
func_2703 = relay.Function([var_2701], output)
mutated_mod['func_2703'] = func_2703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2186_call = mod.get_global_var('func_2186')
func_2187_call = mutated_mod.get_global_var('func_2187')
call_2755 = relay.TupleGetItem(func_2186_call(), 1)
call_2756 = relay.TupleGetItem(func_2187_call(), 1)
output = call_2755
output2 = call_2756
func_2789 = relay.Function([], output)
mod['func_2789'] = func_2789
mod = relay.transform.InferType()(mod)
mutated_mod['func_2789'] = func_2789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2789_call = mutated_mod.get_global_var('func_2789')
call_2790 = func_2789_call()
output = call_2790
func_2791 = relay.Function([], output)
mutated_mod['func_2791'] = func_2791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2664_call = mod.get_global_var('func_2664')
func_2666_call = mutated_mod.get_global_var('func_2666')
call_2814 = func_2664_call()
call_2815 = func_2664_call()
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
call_2839 = relay.TupleGetItem(func_2326_call(), 1)
call_2840 = relay.TupleGetItem(func_2328_call(), 1)
func_320_call = mod.get_global_var('func_320')
func_322_call = mutated_mod.get_global_var('func_322')
call_2853 = relay.TupleGetItem(func_320_call(), 4)
call_2854 = relay.TupleGetItem(func_322_call(), 4)
bop_2886 = relay.power(call_2814.astype('float64'), relay.reshape(call_2853.astype('float64'), relay.shape_of(call_2814))) # shape=(1, 16)
bop_2889 = relay.power(call_2815.astype('float64'), relay.reshape(call_2854.astype('float64'), relay.shape_of(call_2815))) # shape=(1, 16)
func_1656_call = mod.get_global_var('func_1656')
func_1658_call = mutated_mod.get_global_var('func_1658')
const_2895 = relay.const([[-8.996548,-9.447803,-5.384206,-5.687677,-4.455358,4.576530,4.549121,-2.348797,7.099539,7.702166,4.845701,6.684413,-6.771463,-2.346491,-1.819710,9.473096,-9.473229,-9.265545,-1.309910,2.869278,2.854522,-8.448038,-0.217082,-3.381921,-7.516656,6.778525,-8.782462,-1.494875,-3.135636,8.045411,-2.784942,5.400449,-7.197854,9.169836,-3.657069,-3.205089,5.210347,5.324500,0.112770,-5.225646,7.675865,5.011680,-6.374025,-1.286820,-3.253112,6.459082,-9.160260,3.269870,-6.536749,1.297408,-1.864528,-1.232595,-5.592345,0.243731,-8.755473,1.402575,9.717350,2.757999,1.465510,-3.339068,-7.980768,-4.575067,-2.972733,0.364649,6.851497,-2.377219,-5.570307,4.369638,-5.681409,-6.767297,-2.971290,-1.872449,-5.106630,7.174087,6.300789,0.115607,2.324296,-6.925655,-6.805034,-5.516226,-0.779095,7.435694,-4.285919,9.845680,5.185565,3.342743,-8.840350,1.935491,8.750670,-2.743531,8.155873,-2.901719,3.384953,-6.717135,0.945234,0.267197,4.029429,-3.230827,-3.598046,-4.396559,-3.350792,4.411973,2.812793,9.153586,-6.991157,7.499539,-2.119329,-9.459045,-2.292841,8.628352,-5.596537,3.171081,0.467935,5.202534,-9.080958,2.503533,0.280939,1.515820,4.205109,9.705653,-1.495749,1.796296,3.413184,-7.146853,7.755704,8.129722,6.272874,4.505426,-6.040608,-4.408723,4.495946,1.113453,-2.862381,2.460360,-3.671985,0.211300,-6.598311,0.985806,1.561216,6.482229]], dtype = "float32")#candidate|2895|(1, 140)|const|float32
call_2894 = relay.TupleGetItem(func_1656_call(relay.reshape(const_2895.astype('float32'), [140,])), 0)
call_2896 = relay.TupleGetItem(func_1658_call(relay.reshape(const_2895.astype('float32'), [140,])), 0)
output = relay.Tuple([call_2839,bop_2886,call_2894,const_2895,])
output2 = relay.Tuple([call_2840,bop_2889,call_2896,const_2895,])
func_2897 = relay.Function([], output)
mod['func_2897'] = func_2897
mod = relay.transform.InferType()(mod)
output = func_2897()
func_2898 = relay.Function([], output)
mutated_mod['func_2898'] = func_2898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1485_call = mod.get_global_var('func_1485')
func_1486_call = mutated_mod.get_global_var('func_1486')
call_2912 = relay.TupleGetItem(func_1485_call(), 0)
call_2913 = relay.TupleGetItem(func_1486_call(), 0)
func_987_call = mod.get_global_var('func_987')
func_991_call = mutated_mod.get_global_var('func_991')
var_2920 = relay.var("var_2920", dtype = "float32", shape = (140,))#candidate|2920|(140,)|var|float32
call_2919 = relay.TupleGetItem(func_987_call(relay.reshape(var_2920.astype('float32'), [14, 10, 1]), relay.reshape(var_2920.astype('float32'), [14, 10, 1]), ), 0)
call_2921 = relay.TupleGetItem(func_991_call(relay.reshape(var_2920.astype('float32'), [14, 10, 1]), relay.reshape(var_2920.astype('float32'), [14, 10, 1]), ), 0)
uop_2930 = relay.asin(call_2919.astype('float32')) # shape=(14, 10, 1)
uop_2932 = relay.asin(call_2921.astype('float32')) # shape=(14, 10, 1)
output = relay.Tuple([call_2912,var_2920,uop_2930,])
output2 = relay.Tuple([call_2913,var_2920,uop_2932,])
func_2933 = relay.Function([var_2920,], output)
mod['func_2933'] = func_2933
mod = relay.transform.InferType()(mod)
var_2934 = relay.var("var_2934", dtype = "float32", shape = (140,))#candidate|2934|(140,)|var|float32
output = func_2933(var_2934)
func_2935 = relay.Function([var_2934], output)
mutated_mod['func_2935'] = func_2935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2958 = relay.var("var_2958", dtype = "uint64", shape = (4, 11, 16))#candidate|2958|(4, 11, 16)|var|uint64
const_2959 = relay.const([[[-6,-4,-5,2,7,3,-6,3,5,-2,5,8,-3,10,3,-7],[-2,5,-7,-9,6,4,-2,-5,-7,5,7,5,-6,-3,6,-1],[10,6,-2,2,7,-1,-5,8,-3,5,6,1,4,2,-3,8],[6,3,-9,5,-2,-4,3,8,-5,-10,-4,3,-5,6,8,3],[8,-4,-10,-2,7,7,8,-8,10,-3,8,-2,3,-1,2,6],[10,6,9,2,3,-8,7,-3,-3,-3,4,-4,-3,-7,8,4],[3,10,7,-8,1,1,-1,7,3,-6,7,-2,-4,-7,10,2],[3,-5,-2,-1,10,-3,8,-6,-3,-6,2,-3,6,-1,-3,-2],[-5,-5,4,1,7,7,-5,-6,5,9,1,6,-1,-6,9,9],[6,10,1,4,-7,-5,3,-9,3,-8,9,4,10,-4,-9,-3],[-8,-5,-6,9,1,4,-3,-4,2,-3,-7,-4,-6,-4,-3,9]],[[9,2,-4,-9,-3,1,-9,-4,-9,3,-1,-3,-5,-1,-5,4],[6,-1,7,7,4,-5,5,3,6,9,5,6,10,-10,8,1],[10,-4,4,6,-1,1,2,-7,-2,-8,10,-8,-3,-7,4,7],[-10,10,4,1,9,-9,-6,9,-7,-6,3,7,-4,-9,2,4],[-10,-7,-10,-10,-10,10,-9,3,-6,-1,5,-6,-4,-7,2,-2],[6,7,-8,7,-7,-2,-5,-2,-6,-9,3,-9,-2,-5,8,7],[7,-1,2,-10,4,7,9,-10,2,-5,7,-4,-10,5,6,-1],[-7,-9,2,-2,-1,8,6,-6,-9,3,-5,-5,6,3,2,-9],[10,-2,5,-1,-10,-10,-6,7,7,3,9,-9,8,8,-5,2],[3,8,-5,6,-9,-4,-3,2,2,-4,-3,-5,4,-4,-8,-6],[10,1,-4,-3,-3,8,9,-10,3,-2,-8,9,8,-10,-8,9]],[[10,-3,7,7,-4,-10,5,4,3,-6,10,-2,9,-9,8,-4],[8,-7,5,6,1,2,5,7,9,10,1,2,-4,6,8,4],[-1,-2,-5,8,6,1,4,-3,1,6,5,-1,-10,-5,-1,6],[-10,-8,9,-8,-6,8,8,4,-5,1,-10,-3,1,1,-6,4],[5,8,8,9,-6,-5,-8,-4,-1,5,9,-4,-3,-2,1,-5],[-8,2,-9,-1,8,1,-2,9,10,-9,-9,9,7,2,-7,-8],[-10,-10,-9,-5,-4,-3,1,-4,-5,2,-5,7,-4,3,8,6],[-10,-8,-7,8,-1,-2,2,-5,-8,-10,-8,6,-9,-1,8,6],[6,-7,-9,6,5,-2,5,-3,-4,5,-1,4,-8,7,-4,4],[-7,3,-7,3,9,8,-3,-7,1,1,-3,-1,1,8,1,5],[4,-3,9,2,1,1,10,-5,2,-4,8,-7,-5,4,9,-5]],[[7,6,4,-3,-10,1,4,3,-1,-2,-4,9,6,-7,-3,9],[-8,8,-5,-9,7,2,-7,9,2,8,-2,5,-10,-4,3,-7],[-10,-5,7,-9,5,6,-6,9,-6,-6,-3,8,-1,8,-8,9],[9,-5,7,1,-5,3,3,1,-6,-10,6,-4,-10,5,7,-8],[-7,5,4,5,4,-1,9,-10,9,-5,8,5,2,-10,1,7],[8,1,7,-3,3,2,8,-8,2,3,3,-1,-6,-5,-6,7],[4,10,-4,-4,7,-1,-8,1,4,-1,1,-3,-1,-6,-1,-5],[-10,6,-5,3,6,6,-4,-1,10,5,-4,-10,9,5,10,-2],[-4,4,-9,-3,10,-7,8,-3,2,10,8,-2,-8,4,-7,-8],[-7,10,9,8,-3,-4,-7,-9,-6,-4,1,-3,4,-8,-6,-2],[9,8,5,9,-3,1,1,8,1,4,-1,-4,4,8,8,-4]]], dtype = "uint64")#candidate|2959|(4, 11, 16)|const|uint64
bop_2960 = relay.equal(var_2958.astype('bool'), relay.reshape(const_2959.astype('bool'), relay.shape_of(var_2958))) # shape=(4, 11, 16)
output = bop_2960
output2 = bop_2960
func_2970 = relay.Function([var_2958,], output)
mod['func_2970'] = func_2970
mod = relay.transform.InferType()(mod)
mutated_mod['func_2970'] = func_2970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2971 = relay.var("var_2971", dtype = "uint64", shape = (4, 11, 16))#candidate|2971|(4, 11, 16)|var|uint64
func_2970_call = mutated_mod.get_global_var('func_2970')
call_2972 = func_2970_call(var_2971)
output = call_2972
func_2973 = relay.Function([var_2971], output)
mutated_mod['func_2973'] = func_2973
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2994 = relay.var("var_2994", dtype = "bool", shape = (15, 1, 2))#candidate|2994|(15, 1, 2)|var|bool
var_2995 = relay.var("var_2995", dtype = "bool", shape = (15, 5, 2))#candidate|2995|(15, 5, 2)|var|bool
bop_2996 = relay.logical_or(var_2994.astype('bool'), var_2995.astype('bool')) # shape=(15, 5, 2)
output = relay.Tuple([bop_2996,])
output2 = relay.Tuple([bop_2996,])
func_3000 = relay.Function([var_2994,var_2995,], output)
mod['func_3000'] = func_3000
mod = relay.transform.InferType()(mod)
var_3001 = relay.var("var_3001", dtype = "bool", shape = (15, 1, 2))#candidate|3001|(15, 1, 2)|var|bool
var_3002 = relay.var("var_3002", dtype = "bool", shape = (15, 5, 2))#candidate|3002|(15, 5, 2)|var|bool
output = func_3000(var_3001,var_3002,)
func_3003 = relay.Function([var_3001,var_3002,], output)
mutated_mod['func_3003'] = func_3003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_3008 = func_766_call()
call_3009 = func_766_call()
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
const_3024 = relay.const(8, dtype = "uint64")#candidate|3024|()|const|uint64
call_3023 = relay.TupleGetItem(func_107_call(relay.reshape(const_3024.astype('uint64'), []), relay.reshape(call_3008.astype('uint64'), [1, 16]), ), 0)
call_3025 = relay.TupleGetItem(func_111_call(relay.reshape(const_3024.astype('uint64'), []), relay.reshape(call_3008.astype('uint64'), [1, 16]), ), 0)
output = relay.Tuple([call_3008,call_3023,const_3024,])
output2 = relay.Tuple([call_3009,call_3025,const_3024,])
func_3026 = relay.Function([], output)
mod['func_3026'] = func_3026
mod = relay.transform.InferType()(mod)
mutated_mod['func_3026'] = func_3026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3026_call = mutated_mod.get_global_var('func_3026')
call_3027 = func_3026_call()
output = call_3027
func_3028 = relay.Function([], output)
mutated_mod['func_3028'] = func_3028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1861_call = mod.get_global_var('func_1861')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_3042 = func_1861_call()
call_3043 = func_1861_call()
output = relay.Tuple([call_3042,])
output2 = relay.Tuple([call_3043,])
func_3057 = relay.Function([], output)
mod['func_3057'] = func_3057
mod = relay.transform.InferType()(mod)
mutated_mod['func_3057'] = func_3057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3057_call = mutated_mod.get_global_var('func_3057')
call_3058 = func_3057_call()
output = call_3058
func_3059 = relay.Function([], output)
mutated_mod['func_3059'] = func_3059
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3073 = relay.var("var_3073", dtype = "float64", shape = (5, 15, 12))#candidate|3073|(5, 15, 12)|var|float64
uop_3074 = relay.log10(var_3073.astype('float64')) # shape=(5, 15, 12)
func_1904_call = mod.get_global_var('func_1904')
func_1905_call = mutated_mod.get_global_var('func_1905')
call_3076 = relay.TupleGetItem(func_1904_call(), 0)
call_3077 = relay.TupleGetItem(func_1905_call(), 0)
func_274_call = mod.get_global_var('func_274')
func_278_call = mutated_mod.get_global_var('func_278')
var_3080 = relay.var("var_3080", dtype = "int32", shape = (270,))#candidate|3080|(270,)|var|int32
call_3079 = relay.TupleGetItem(func_274_call(relay.reshape(var_3080.astype('int32'), [6, 15, 3]), relay.reshape(var_3080.astype('float64'), [6, 15, 3]), ), 0)
call_3081 = relay.TupleGetItem(func_278_call(relay.reshape(var_3080.astype('int32'), [6, 15, 3]), relay.reshape(var_3080.astype('float64'), [6, 15, 3]), ), 0)
output = relay.Tuple([uop_3074,call_3076,call_3079,var_3080,])
output2 = relay.Tuple([uop_3074,call_3077,call_3081,var_3080,])
func_3082 = relay.Function([var_3073,var_3080,], output)
mod['func_3082'] = func_3082
mod = relay.transform.InferType()(mod)
mutated_mod['func_3082'] = func_3082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3082_call = mutated_mod.get_global_var('func_3082')
var_3084 = relay.var("var_3084", dtype = "float64", shape = (5, 15, 12))#candidate|3084|(5, 15, 12)|var|float64
var_3085 = relay.var("var_3085", dtype = "int32", shape = (270,))#candidate|3085|(270,)|var|int32
call_3083 = func_3082_call(var_3084,var_3085,)
output = call_3083
func_3086 = relay.Function([var_3084,var_3085,], output)
mutated_mod['func_3086'] = func_3086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_490_call = mod.get_global_var('func_490')
func_491_call = mutated_mod.get_global_var('func_491')
call_3108 = relay.TupleGetItem(func_490_call(), 0)
call_3109 = relay.TupleGetItem(func_491_call(), 0)
output = call_3108
output2 = call_3109
func_3115 = relay.Function([], output)
mod['func_3115'] = func_3115
mod = relay.transform.InferType()(mod)
output = func_3115()
func_3116 = relay.Function([], output)
mutated_mod['func_3116'] = func_3116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_854_call = mod.get_global_var('func_854')
func_855_call = mutated_mod.get_global_var('func_855')
call_3128 = func_854_call()
call_3129 = func_854_call()
output = relay.Tuple([call_3128,])
output2 = relay.Tuple([call_3129,])
func_3147 = relay.Function([], output)
mod['func_3147'] = func_3147
mod = relay.transform.InferType()(mod)
mutated_mod['func_3147'] = func_3147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mutated_mod.get_global_var('func_3147')
call_3148 = func_3147_call()
output = call_3148
func_3149 = relay.Function([], output)
mutated_mod['func_3149'] = func_3149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_3150 = relay.TupleGetItem(func_3147_call(), 0)
call_3151 = relay.TupleGetItem(func_3149_call(), 0)
output = relay.Tuple([call_3150,])
output2 = relay.Tuple([call_3151,])
func_3161 = relay.Function([], output)
mod['func_3161'] = func_3161
mod = relay.transform.InferType()(mod)
output = func_3161()
func_3162 = relay.Function([], output)
mutated_mod['func_3162'] = func_3162
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3186 = relay.var("var_3186", dtype = "float32", shape = (15, 11, 14))#candidate|3186|(15, 11, 14)|var|float32
const_3187 = relay.const([[[-9.944764,1.329067,-2.279831,8.634345,-3.011260,-8.933996,5.639454,-7.052128,1.024091,-6.435819,2.683799,-7.412585,-1.702165,-6.495570],[9.048162,0.765992,4.971066,-0.015634,5.497973,-9.747152,-4.113108,-7.660029,-8.850405,-5.372794,0.448479,-2.792309,-7.749798,-3.432122],[9.508737,8.019584,-1.880013,4.334364,5.340520,-8.083027,7.490723,7.849209,9.973485,7.812652,-5.571102,6.079183,-2.194685,1.480312],[3.705185,8.527399,-6.582684,2.938201,4.855389,-5.842040,-4.899238,1.571586,2.397991,-4.861740,2.836508,-8.151418,2.289288,7.218079],[8.896398,-2.874487,-7.597974,-6.980780,-9.594036,-1.474494,-3.531617,5.114804,6.073508,-5.984159,6.584914,7.143280,-0.110950,-5.365361],[9.327297,-7.069184,-4.147871,4.152540,-9.488390,7.253356,0.489594,3.404551,-8.556977,5.983402,7.482703,-6.898080,-7.249334,5.464955],[-1.483493,-9.211414,-6.080842,-0.468106,6.353111,5.685905,2.806478,-2.452554,-5.645704,-7.311659,-8.927839,-2.789623,0.078026,-7.855955],[-2.557521,5.756762,-8.458361,9.798653,-2.738000,2.309537,3.456241,3.659425,-3.873326,-9.640206,3.603534,3.127520,-1.287157,-7.627832],[1.964262,1.806375,-0.203684,-6.968962,-0.759450,0.570851,5.537834,-4.977317,-2.098223,-3.098735,2.456881,1.566742,5.755059,6.461896],[9.230109,-4.970330,-8.077813,-4.655175,-4.306840,3.904767,-6.802979,0.482502,-2.905477,2.216853,8.348116,3.973177,-6.969958,-7.688383],[0.034039,4.800928,5.029852,6.730788,6.873610,-3.132571,-2.492574,-6.006776,8.953411,3.148354,4.455364,-8.137960,-1.637991,7.253639]],[[-9.801296,-7.775392,1.774921,-9.813998,5.205446,8.997942,-4.508419,-2.636927,4.815867,9.673591,-9.845340,-1.787504,0.405889,2.673057],[-7.503833,-3.125140,-9.999098,9.781037,-8.055706,-2.833985,0.427262,-2.157935,5.201200,7.108000,7.357395,5.942699,2.379556,4.418652],[-3.665745,-2.809744,-3.400206,-7.903460,0.827704,-3.899040,8.449570,-4.063184,-2.654310,-9.720988,2.157637,2.687402,6.971152,4.230022],[-4.288190,5.279794,7.233091,-2.022204,1.251451,-6.762414,-9.224016,-5.016934,5.578516,-4.337831,-5.370637,4.503274,-2.075823,-4.877220],[-3.706714,-9.788064,6.607148,7.845407,8.087310,-1.013701,-2.963735,-7.703291,9.880537,8.767422,2.525714,6.976573,-9.469678,7.450728],[5.362914,-9.190672,7.855448,-6.805758,7.334651,1.750556,9.904153,8.279955,-8.120598,-3.776586,-7.705411,-8.721311,-2.965870,6.432951],[1.116346,6.979471,7.772256,-2.116171,5.450395,4.981319,-5.957520,7.157339,-8.040250,-7.398309,-0.642536,-9.424749,-5.245840,-6.895688],[-2.543649,9.980113,3.133688,-9.546133,5.344289,2.521199,-1.207060,6.875496,-0.959496,-3.500692,1.754586,7.368658,-8.905473,-9.197082],[9.344684,8.995901,3.729306,8.304180,3.396211,1.003012,-6.973319,3.962126,4.704873,6.393576,-1.943680,-9.784221,-0.985964,5.969850],[1.518142,5.304084,6.511339,0.655355,-5.179824,0.865390,-7.526517,-2.461597,3.823983,2.328233,-1.466526,-7.379048,5.188295,-2.214150],[5.957568,-4.235131,8.038766,6.481416,-2.318620,8.624475,3.658386,-6.347087,2.014811,-0.609125,0.103943,7.906632,-7.748975,-1.221019]],[[-0.273395,-3.159690,-9.244028,0.562960,-2.885809,-4.830407,0.913818,7.056499,-9.695923,-3.611779,-3.898979,0.557306,9.062395,9.889233],[-1.699391,4.044006,-6.770793,-1.036279,-6.974414,9.869885,-2.949618,3.174767,7.663711,-8.542498,-6.707685,-9.269220,4.169331,-0.646505],[-3.535747,1.767206,1.722876,-3.160063,-8.988912,0.510359,-9.138198,7.108829,-2.592079,-3.452560,-4.318690,-9.515514,3.756169,3.211942],[-2.610983,6.060876,-7.860060,3.513768,2.699744,9.040052,5.730668,-9.553027,3.234398,-5.227650,-2.863613,-8.070720,-2.667900,-7.107209],[5.558523,-7.183359,6.325785,-9.512717,-4.576558,-6.310343,4.520141,8.389489,-0.005273,-0.035406,-2.483462,9.867516,0.999186,5.913662],[-0.194161,-9.722054,1.038438,1.050731,-6.865496,-4.058210,-2.398300,8.456361,7.383846,-1.347322,-2.085375,4.556356,9.618050,-4.818108],[-2.734065,-7.691084,4.282006,-8.716088,-9.539472,8.822694,-3.697572,4.704719,-2.594031,-6.416173,-2.453676,1.619986,-2.040588,1.562741],[-1.355255,-4.549164,1.728451,9.862727,8.738665,1.534527,-6.267539,6.211316,7.488326,8.213791,7.109483,5.393748,-0.452049,-3.894105],[0.593187,-6.145196,4.563089,9.785335,-6.167372,8.728659,-1.955464,9.885684,-9.396043,6.388818,8.824196,0.582535,6.620538,-2.591594],[-8.470128,-1.044484,-7.420342,4.973478,8.387036,-9.583437,6.121631,-2.403606,8.860885,-3.901679,-2.284951,0.371457,-5.119364,-5.450041],[7.409481,7.314184,9.638881,6.997767,0.382880,-8.570406,2.885294,-1.043853,-7.332009,4.682407,-8.377395,6.390631,4.803819,-5.019437]],[[-9.326821,2.542173,-4.226537,7.572629,-8.508269,4.870381,1.614138,3.284965,6.487043,2.995103,-6.264587,2.897663,7.729467,5.158486],[6.428687,-5.707419,-2.540293,4.568670,8.990777,-8.211791,8.211044,9.010751,8.304049,-2.634082,-2.766355,8.698809,-6.145058,2.361292],[0.052287,-0.334169,-3.473652,-2.784879,7.910872,6.974340,-5.881208,-9.346524,-4.704780,-7.562478,-4.999516,-8.331546,6.031340,2.601882],[-0.247105,6.728829,6.278367,-0.273740,-5.557062,-2.606388,-6.202403,-5.596719,-6.380715,-3.885778,-9.258955,-5.883737,7.885827,3.985052],[-2.323174,-8.883576,3.938019,0.945838,-2.003427,5.660414,-5.375272,-4.526816,4.432619,-7.622205,5.744016,-7.741660,4.121217,0.374283],[4.193996,8.827326,4.403292,-3.289966,9.611308,-0.913723,2.033997,9.754326,9.788790,-4.792207,-2.113840,-4.442708,-4.737420,-7.528832],[-2.097075,-6.209924,-1.064039,9.608729,-1.796926,5.017255,1.342378,2.616770,0.067493,4.439062,-2.648532,6.847859,-8.487542,-5.006179],[8.687742,-8.501424,-8.809204,7.159647,5.511663,0.951098,5.429555,6.385984,-5.838904,3.025990,7.836219,-2.409091,8.679795,7.896533],[-6.152638,-5.536543,-9.148802,2.399711,2.112892,0.237844,8.723061,-6.926068,0.504075,-4.806132,-9.345784,5.858139,-0.355496,7.954859],[-9.077686,1.547517,9.312458,-5.408127,-9.660500,-1.138051,-5.049624,-2.336929,-8.529275,-2.474675,0.989890,8.560398,8.314278,8.444394],[0.578691,7.208806,6.888521,-0.378204,-0.030992,-3.672570,-8.046315,-1.426730,0.209600,-9.765472,-3.016198,6.709858,3.846870,7.299543]],[[-4.573592,-2.439455,-5.640025,4.887142,-9.003237,-0.714844,-0.579048,-3.053209,1.756636,0.721838,1.271611,8.691056,3.422263,0.281590],[9.195218,5.322188,-3.050109,2.188914,3.710720,-6.280321,-8.237939,-9.540554,-9.632034,2.895378,9.316654,-8.844832,4.447317,-4.784396],[-4.566413,9.711555,5.177991,1.536529,8.242151,-2.202359,0.749722,-9.358241,8.306605,-1.218900,3.460045,5.907241,2.154800,-7.517028],[3.850721,3.983494,-0.042928,-5.096087,1.873409,1.107703,-0.654445,8.475970,1.136671,-8.919676,-1.843242,-2.649252,-5.399978,-5.091925],[6.871955,-8.475760,-8.590714,-8.155180,4.712850,-9.914357,6.706630,6.803495,3.591899,2.652343,-8.875874,7.980379,4.139649,8.955334],[4.173630,4.253565,-5.668876,-2.694519,5.773529,4.697791,2.727378,2.068311,-1.723022,-6.934795,7.523908,-9.605793,0.964420,-0.650545],[4.544008,2.594986,5.302294,7.688959,-7.513067,-9.191079,-8.485593,-0.829100,8.845161,-9.962037,-8.876034,9.118990,5.868692,-7.117620],[0.354408,6.220065,-2.758052,-7.864131,5.329573,1.005823,2.190194,3.741498,4.389360,8.117984,2.097346,-0.110727,-3.935435,7.971294],[8.063744,3.417041,-5.090636,7.759710,8.552344,-8.635521,2.299347,-2.864876,-1.996246,5.523617,-0.012411,-3.164687,-9.158871,7.506338],[9.622494,-0.351971,-8.681198,3.616341,-6.538402,3.521625,-8.401613,-1.665677,2.585114,-2.101069,-5.285039,-2.839388,-2.458283,-4.720413],[0.494316,-1.923064,-8.396586,-5.273475,-9.141734,3.587570,-6.189371,-3.628593,8.521781,4.463562,6.185412,-2.041852,2.146380,-8.099687]],[[4.184787,-1.138861,7.251659,3.888602,-5.805899,-2.683460,-7.103704,6.736027,8.799816,9.571757,9.776702,3.879664,6.363586,-1.860617],[-4.329674,-4.372642,-3.588568,8.271231,4.038625,2.297397,-5.841382,-4.591468,-7.375256,4.684919,6.661488,-3.588797,9.840279,-6.993896],[9.605345,7.841334,8.881554,6.720964,2.763235,2.809083,-8.935572,-7.155584,1.615292,6.731915,-6.807838,5.736879,9.520966,-6.099582],[1.291016,6.931784,-6.580050,8.963295,3.919293,6.011777,8.736438,4.057374,9.471377,-0.514992,1.839576,-7.833116,-5.438182,1.136581],[6.025927,0.840689,-8.136744,0.377511,9.202639,9.002380,-1.014214,3.491029,6.092136,2.065355,-1.904402,9.442118,7.737077,-9.577933],[8.794692,6.852267,2.117845,-5.523212,-3.228362,-0.516178,-4.877715,-3.390692,-0.098546,-0.220048,-9.656808,1.764867,9.478583,-6.372601],[-0.021391,-1.476933,0.382642,6.808907,-0.813101,-9.401032,4.834325,8.970931,-9.451810,-9.599725,1.239987,8.876451,-9.241327,9.096921],[9.934199,-3.066721,-1.103978,-9.195328,4.440286,-2.225542,4.285627,-0.236153,-6.187119,-9.261977,7.908850,9.772269,2.423869,-5.209758],[3.124628,7.150625,-9.255436,0.294085,-1.558465,-3.972997,2.330298,-0.632971,0.859491,5.319108,-0.663055,9.364023,0.552908,-8.431945],[9.797904,-4.300595,-8.377048,0.791681,-8.845254,0.789375,-4.527482,-8.917861,0.370786,-9.322334,6.048566,-5.462302,5.737683,3.798487],[-1.329542,8.236435,-6.758467,8.986218,4.102321,6.318252,4.034102,2.126820,-2.201503,0.361609,-9.721534,3.496846,7.040029,0.824891]],[[1.548842,9.096486,-9.172144,8.565971,5.961895,-8.383350,2.231408,-1.425001,-7.463621,4.755352,0.730961,-5.799645,-0.824763,9.018395],[2.307706,4.440612,3.460502,0.286593,8.226840,-3.447562,8.358144,-9.650850,3.650718,9.556225,-5.622974,-8.313233,7.569690,1.530787],[-9.392014,2.945751,1.904213,-4.056867,-0.568401,-5.663030,-6.459421,-2.656249,7.819564,1.590690,2.099774,4.218629,7.353259,9.731008],[-9.434599,-7.907245,0.875158,7.508165,-7.718807,7.542945,6.140679,4.990090,-1.527793,2.848551,-0.076407,-8.118836,7.413940,2.104965],[-2.932034,7.752755,4.145139,5.146885,9.657601,1.946684,7.859751,-4.561438,-9.796015,-9.008411,9.729053,8.756387,-7.627386,6.039804],[0.693667,-8.604425,5.892201,-8.719927,-7.773122,4.865119,-8.822267,5.275753,9.095162,-3.779383,9.733587,7.482828,-8.888864,-6.278594],[-4.813757,-2.690992,-0.473070,3.370723,-7.647192,-1.300401,-8.716061,2.437506,-3.099187,-4.510814,-3.951672,-5.329409,1.445186,5.966155],[-1.784542,2.749105,1.191694,-6.342381,-1.455978,-5.231517,4.638737,6.312977,-2.334462,2.907391,-7.993709,4.896450,-1.342297,-5.543428],[3.019069,-4.472114,-7.288239,-2.767235,3.805604,0.826324,3.145671,7.673294,1.980207,-4.191561,8.750273,-9.551742,2.899985,-5.618736],[4.590244,8.476095,-1.830559,-5.553706,6.618054,8.038913,6.616645,4.544537,-7.908926,-3.125840,7.778944,1.269013,-8.704870,-9.344149],[6.795819,2.649703,-7.372021,2.859980,-9.731562,4.496708,8.878873,1.689246,0.137778,5.064713,7.556552,0.029478,-6.728522,6.932252]],[[1.874781,-0.220162,-7.760149,2.298287,-5.513792,-1.032485,8.012500,6.411343,-4.001756,0.174347,5.236674,0.206330,-4.283122,9.940776],[4.286168,1.537406,0.683480,-9.200748,-9.468766,-7.884123,-8.790872,6.107207,-6.785229,-3.219350,2.698427,-9.357798,-8.459505,3.450425],[4.273731,1.882436,5.199798,7.613393,-7.715642,6.026447,4.265805,-0.588959,-5.429887,9.271791,-5.216385,0.721729,-3.461864,-0.970753],[3.169844,8.437264,-0.545573,5.291296,-8.237813,-9.381471,-3.254589,0.794484,6.807230,-0.509610,6.332475,-5.302069,1.173548,-6.369912],[-8.971375,2.553054,-9.291933,-9.560779,7.344218,0.340421,-6.265466,8.005062,4.482105,-1.827106,-4.111633,-8.530876,5.807845,4.432668],[-5.633926,-5.255872,-2.498411,-1.728870,-8.818204,4.617143,-4.187042,8.245047,1.972899,-5.722625,9.228580,5.253144,1.658100,-6.072025],[1.942012,0.588549,3.139205,-4.227785,3.161240,-6.780991,9.634812,-9.964402,-6.146546,-8.245860,-4.083411,-5.092908,9.940758,4.471754],[3.405413,7.599839,9.115395,-5.328264,-3.496144,-3.387153,9.500464,-4.747254,-6.899790,6.673852,-6.632803,-3.659388,-6.249756,0.234622],[2.090537,-8.167042,-4.070557,2.783453,-1.133319,-2.782193,-9.051421,0.696062,0.959938,-0.658473,-6.940324,7.493526,2.260667,4.551241],[-0.707448,4.144592,6.620022,6.544593,-8.846080,8.733331,-2.516613,1.126619,-5.502822,1.671644,-2.242867,5.682103,6.339836,-9.911066],[2.737796,-3.249316,-3.577804,4.972911,1.168055,5.079306,4.416580,-9.850475,-5.797031,-9.579806,-2.171201,-1.680542,3.087030,6.774949]],[[-4.767041,3.429720,2.746936,-3.651527,7.884702,0.809184,-6.983548,-7.323141,1.971597,6.484278,9.182362,-0.614622,7.890533,-3.679403],[6.987318,5.393094,0.569977,4.974778,-9.378847,-9.453434,8.848374,-8.769397,-0.944200,0.343436,-9.037068,4.101672,-6.760161,2.160800],[1.093361,-1.430549,-4.523658,-4.788817,-1.813884,-9.945716,2.673885,-6.687121,5.241395,-0.743041,-9.470638,5.915087,9.692693,-3.228594],[5.560001,3.556068,1.675428,0.497360,-2.504106,-5.488824,5.347129,5.351015,2.353546,0.387361,1.262241,5.010966,3.186086,-6.467245],[0.740632,-7.515091,-2.968652,7.757478,9.166610,7.511179,2.778732,-4.912613,2.857522,3.628997,5.116381,6.129126,9.645948,-5.917854],[4.159015,0.086017,7.347119,4.606613,4.073531,-8.197461,2.858499,-4.639522,6.980761,6.229878,0.757663,1.384826,3.679103,7.233590],[0.859999,3.969664,-9.650880,-4.502411,-0.915037,6.844089,-6.195410,-2.545997,-2.508998,-0.762379,7.227789,-4.145190,0.857484,-8.793729],[-2.094825,9.374137,6.888456,-2.967519,1.241988,-2.391233,8.770846,1.267597,8.311705,7.300846,9.559756,3.697846,-0.470185,0.603150],[6.840429,-8.408077,9.555911,-3.736009,1.434315,-2.672923,7.700734,-0.977380,-3.652592,-0.568898,-6.410221,2.745964,-6.789342,-5.569515],[-5.338109,-7.683866,9.365073,4.533216,-0.657960,-6.616599,1.039107,-3.455991,3.503795,6.178362,-7.302506,5.096762,0.320001,-5.274031],[3.983383,-3.990492,-1.162437,6.711170,-8.985597,-5.499061,-0.563594,-9.400165,3.836329,-8.286704,8.539397,7.694966,-4.447828,-7.850708]],[[0.540567,3.835420,-5.021479,4.785120,-3.854602,-9.327040,0.269639,3.564690,8.101377,2.812562,-6.893973,6.198305,9.641264,3.658232],[6.648339,-4.449139,3.982213,6.011864,4.763957,-4.157062,-3.741528,-2.257221,-8.199081,7.414934,5.108628,-1.055294,3.989194,-4.744743],[-3.700112,-4.124979,0.407867,9.651798,-3.614804,-2.038835,7.261881,4.627234,-7.101501,0.855922,9.812755,-8.709228,-5.993033,-8.330767],[9.866889,-7.724760,-4.123352,9.378553,3.863390,-0.411043,-4.789203,-6.667045,-4.227492,6.488770,1.281549,1.991378,7.821725,-7.637174],[-3.205747,2.627253,7.517718,-6.482837,-2.402024,8.597495,-6.213241,6.557982,0.262937,-6.038698,6.269019,-1.415606,-0.464349,3.670077],[0.201092,8.534710,-5.402796,9.051070,8.652971,-5.795494,-9.274823,4.921471,1.492810,1.910956,-3.246893,-9.842816,2.381094,2.877534],[-0.413213,2.332477,-0.654548,-3.117326,-1.003447,-9.820760,6.653408,6.477452,-0.739184,-1.981993,-2.286279,-3.176072,2.493979,-3.893086],[7.267364,-6.836300,8.990174,-1.372430,5.032469,-4.882371,-3.036520,2.829919,4.966431,5.105063,2.659216,-4.807539,7.433059,0.500774],[7.645508,2.567606,5.610030,9.424070,-7.836279,-3.507008,-2.748546,2.154866,5.880787,-6.655827,5.595361,-9.975425,1.049293,-7.549575],[-2.174953,0.570738,-5.263072,-3.096001,-9.017360,-2.785339,7.221746,-2.603159,4.445884,2.614231,-9.520534,-4.079614,5.019596,3.109804],[7.356019,-9.436373,0.642072,0.318714,-6.608118,7.411638,3.583463,0.940704,-9.638105,-5.287916,7.744201,-5.390058,6.612088,-0.559023]],[[3.527687,5.199168,8.316904,-4.552116,9.205508,-5.527612,-9.324386,3.435205,5.637737,-3.160631,-5.156620,-8.044465,-8.632219,-3.952562],[3.803493,8.966371,-7.272894,7.787696,-3.831807,-5.642991,3.296723,1.235950,-7.013834,-4.005639,-8.959950,1.517397,5.270653,-6.455925],[-8.912413,-8.188675,2.060722,-6.835025,-6.308191,-3.074994,-5.417793,8.462595,3.435703,8.745565,8.022229,-7.151470,-5.984416,-6.410367],[5.566571,-3.816816,5.841915,6.416101,-8.566063,-1.808022,7.199613,9.542028,4.452970,7.885332,0.084677,-9.733297,-0.056902,-1.314478],[-7.272505,7.848402,-8.691466,2.830068,-6.084946,-8.551600,9.183858,3.071542,9.265890,-6.685624,2.997843,-1.611820,-3.784565,0.556049],[9.286527,5.313299,9.664200,2.798170,-0.987490,4.619337,3.435907,6.412548,4.637843,9.078395,1.561715,6.009994,9.070205,-2.116960],[5.285936,8.538718,4.937722,-3.034717,9.451718,-9.559137,0.063952,-4.945174,-9.846446,7.857593,-3.325924,-3.799329,-7.149517,7.556523],[4.715842,7.751020,5.952161,9.342630,8.797192,4.595848,8.972613,6.529796,-1.604594,7.079758,7.488685,-5.769794,5.060225,-2.848322],[-4.101199,-3.687937,4.952691,-0.228762,-3.105495,4.554131,-4.369242,-8.802904,2.672015,-4.121885,7.506073,-5.384152,-2.640566,-1.980571],[7.802905,0.231509,-4.774591,-2.831920,9.734087,0.693867,-1.863622,5.825150,4.300743,5.188321,1.008823,-9.621658,7.480698,-2.448872],[4.367134,-1.179516,0.615329,5.117507,1.992605,5.123242,-6.227571,-2.957419,3.659261,3.235273,3.373952,8.627058,-5.126980,0.400262]],[[-1.461191,2.892485,-5.642456,5.489719,7.253212,-7.047645,-7.911203,0.317315,-7.342842,9.303834,-7.928745,-6.743645,0.750174,-3.688352],[-7.258702,-1.036846,9.399310,-5.138440,4.453385,2.231040,-7.170727,4.590938,4.519680,-6.926448,-3.532054,-3.512431,-0.576380,-7.421821],[-3.459749,-4.895140,-8.948687,-6.350829,-9.390437,2.678139,-3.222890,1.874238,-0.816924,6.819832,2.016420,1.528484,1.582578,-9.167089],[6.243523,-6.084864,-5.374568,-1.782980,2.693478,-0.086371,7.967607,1.137327,5.353007,0.808750,2.062274,8.540793,-3.079808,-4.302701],[-5.256858,2.645793,1.447757,-2.076080,-1.206420,-5.696635,4.472700,-0.548989,-5.348436,-2.090096,-5.696353,-8.830777,-3.073768,-2.479962],[-2.315879,-2.130990,-6.991468,-8.607809,1.126216,8.796549,3.345187,3.549321,-3.401682,-6.368501,6.526648,-0.055145,-2.480778,8.879084],[6.319997,9.236592,-6.727226,-9.198082,5.747414,-4.795259,5.419242,0.885549,0.954255,4.033473,-1.152793,9.695733,-6.059661,4.711307],[-7.826133,6.262981,-0.749511,4.995045,9.976948,0.497135,6.297346,5.635686,9.911402,2.129480,-4.972392,6.702869,-9.677946,-2.720170],[-1.563227,0.566751,4.343620,-7.342912,5.856368,-6.954896,-3.749496,-2.472129,-1.537883,-6.076801,-9.000319,-4.452228,4.673813,0.118911],[-2.168341,-7.536371,2.281604,5.611798,7.241784,-0.927547,-2.133412,1.169549,5.514403,-2.446420,7.403082,0.650742,-7.043035,-8.754420],[4.191370,-3.010370,-9.493392,5.160017,-8.978207,-3.870019,-5.397628,6.879294,4.162388,3.367437,-5.232502,-6.156782,5.251676,4.288046]],[[-1.431112,2.665806,9.974942,6.774755,-1.657956,2.291326,-9.444356,-6.566416,-0.331891,5.770929,-7.180935,-0.269485,-3.538730,2.761937],[1.743908,2.902297,-1.506082,8.253896,-6.256231,3.999319,1.838561,-0.996294,-9.112957,5.313992,-7.895737,1.631014,4.398505,9.481112],[-2.592230,9.620297,2.655874,5.047004,2.862364,8.106437,-1.540094,1.826177,4.995762,8.409590,-0.321872,-1.412314,4.858589,-8.682901],[-5.621312,-3.444475,-8.909356,-2.504142,-9.190608,4.772384,-2.454090,-9.148085,-2.117061,0.967175,9.313936,7.087872,0.326185,-3.836068],[4.387728,2.197794,-5.203767,2.392762,-5.028846,-6.984645,4.140298,-8.914179,-5.620848,-4.151296,-9.650247,-0.012152,-5.029370,-6.052274],[9.120028,-8.463186,6.940253,-2.731608,2.690545,-1.940940,2.181928,4.297493,-1.272088,5.905105,-7.839900,4.152033,8.251307,-8.747185],[-3.177797,1.708657,4.149725,-9.841813,5.919880,-9.398209,-3.112010,-6.643420,6.364373,8.066226,-8.542927,-7.270636,-6.857818,0.489651],[7.947591,-7.346573,-6.271441,5.568098,2.021880,-4.390730,3.643730,-0.073236,6.160392,9.952122,-4.880630,3.988550,3.346007,5.080268],[8.110721,2.352950,-3.067694,-6.492353,5.190073,-8.270951,-8.329530,-6.514685,2.247719,9.121661,0.117625,9.924843,9.309905,-9.958142],[-5.295878,0.244675,8.152700,-7.188195,-7.646645,-4.111976,-3.304353,-0.184107,-3.552075,-6.790161,6.270008,-2.788533,8.613405,-3.132766],[-4.149289,1.934833,-4.368887,6.594426,-5.180562,2.368555,-5.713989,-6.509451,-4.563605,7.223503,5.512138,-6.325254,-6.196860,-6.791502]],[[-0.982063,-5.756274,4.133872,0.263542,-2.564780,5.979778,-1.302143,1.636355,9.917709,-4.231558,8.782676,-5.016165,1.626743,3.718252],[1.770877,5.578849,7.515106,2.723384,-5.532459,-0.695783,1.434322,4.437473,3.896740,-8.518691,-6.288563,-0.171278,2.831030,3.071041],[-3.086215,-8.462205,-5.092234,2.528191,3.406069,-7.315366,-8.178402,2.734401,1.757737,4.699996,3.202434,8.235983,-2.228935,1.418507],[-8.853341,3.757695,-9.593950,-3.110456,3.337564,-6.895751,-3.796431,-7.680436,9.960190,-8.063273,-1.438512,8.617718,-2.164141,-3.851591],[1.386097,-2.271071,-9.554871,-7.616374,3.872773,8.455415,-9.291026,4.463528,-2.818227,7.954346,2.581877,-6.506538,-3.043353,-9.113425],[-3.208394,6.021670,-7.754361,5.151253,4.424703,4.802881,8.322440,-2.255056,-6.321368,-8.244082,7.101519,6.041729,-7.439055,7.486307],[5.378818,7.626936,-0.231277,9.804482,-7.609153,1.182465,-2.527298,-8.652422,4.015267,-8.612350,-2.071795,-6.954499,-7.633623,6.638380],[-5.426285,9.777692,-9.872931,9.816157,-3.502336,8.249559,-9.808572,-4.872591,-7.991742,-2.866942,2.858935,4.991646,8.836435,-2.620331],[3.098947,-6.319881,-1.253566,-3.405624,-6.937126,9.320517,-3.626516,6.992066,9.273270,-7.828881,-2.013330,9.388861,0.895048,-2.200653],[-2.982143,-5.834138,-7.834272,0.185477,3.956051,1.490224,-2.627008,-7.114044,5.464910,3.195279,4.345142,-0.691224,-3.689617,-8.329956],[0.827095,-2.386029,6.950841,5.718179,-3.612733,-0.464785,-9.754797,4.281280,-0.571595,-8.409593,-2.677332,-9.498802,2.306610,4.281133]],[[-4.110729,3.936604,-4.198387,3.170147,-7.927484,3.053714,-1.911083,-4.737061,8.930524,5.403336,5.777658,-7.664694,9.408108,-6.516859],[8.178305,-3.348967,4.707372,4.717628,7.587770,1.581163,-5.793695,-5.743966,-4.304832,3.761502,4.000100,6.175055,-8.466198,-6.885804],[-2.063445,-6.670818,-2.642641,4.434357,-2.558400,-9.773990,8.319545,-2.528757,-5.371102,-8.314822,8.830459,2.609738,-6.036578,-5.038434],[-4.268082,-9.339008,4.592286,-1.798448,3.622721,9.499158,1.357130,-6.928677,8.578557,-8.757387,8.327175,-6.700940,-7.120457,7.657788],[-5.402575,-9.366978,-5.566554,4.657723,5.751092,-9.657118,8.437531,1.568027,1.650058,1.435229,-7.215557,-0.490991,8.876836,-5.930373],[-4.117725,-3.163364,7.296307,1.368042,-9.733942,1.085602,9.179996,-9.035198,7.562270,9.717228,9.524392,7.280249,-7.704379,-4.642187],[-6.950135,4.545310,-8.795083,7.521955,-3.104515,-1.721867,6.332950,6.025544,4.728308,8.185427,8.936627,6.446724,-6.421877,-7.827361],[-5.183580,-6.783991,4.129629,-7.330215,0.225212,-5.585311,-0.310128,-1.229909,-1.278919,-8.000961,-5.711403,3.240868,-4.695198,-7.851901],[2.837782,2.843003,5.988694,5.942968,-3.961603,3.019637,5.501969,4.430888,-8.669026,-1.963569,7.361540,-6.907380,-7.115049,8.487690],[-1.904980,2.935583,-8.363728,9.771158,-2.282627,1.375356,-0.707573,7.089148,-3.613826,-3.009748,-5.835557,0.719598,7.030077,9.557269],[9.261956,6.630265,7.735654,-6.286570,8.631306,0.782599,-5.549213,-7.038671,8.664185,-9.956525,3.054522,-6.994996,4.450085,2.103313]]], dtype = "float32")#candidate|3187|(15, 11, 14)|const|float32
bop_3188 = relay.multiply(var_3186.astype('float32'), relay.reshape(const_3187.astype('float32'), relay.shape_of(var_3186))) # shape=(15, 11, 14)
uop_3193 = relay.cos(const_3187.astype('float32')) # shape=(15, 11, 14)
output = relay.Tuple([bop_3188,uop_3193,])
output2 = relay.Tuple([bop_3188,uop_3193,])
func_3198 = relay.Function([var_3186,], output)
mod['func_3198'] = func_3198
mod = relay.transform.InferType()(mod)
mutated_mod['func_3198'] = func_3198
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3199 = relay.var("var_3199", dtype = "float32", shape = (15, 11, 14))#candidate|3199|(15, 11, 14)|var|float32
func_3198_call = mutated_mod.get_global_var('func_3198')
call_3200 = func_3198_call(var_3199)
output = call_3200
func_3201 = relay.Function([var_3199], output)
mutated_mod['func_3201'] = func_3201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_3203 = relay.TupleGetItem(func_3026_call(), 2)
call_3204 = relay.TupleGetItem(func_3028_call(), 2)
output = call_3203
output2 = call_3204
func_3210 = relay.Function([], output)
mod['func_3210'] = func_3210
mod = relay.transform.InferType()(mod)
output = func_3210()
func_3211 = relay.Function([], output)
mutated_mod['func_3211'] = func_3211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2687_call = mod.get_global_var('func_2687')
func_2688_call = mutated_mod.get_global_var('func_2688')
call_3229 = relay.TupleGetItem(func_2687_call(), 1)
call_3230 = relay.TupleGetItem(func_2688_call(), 1)
func_2636_call = mod.get_global_var('func_2636')
func_2640_call = mutated_mod.get_global_var('func_2640')
var_3236 = relay.var("var_3236", dtype = "float32", shape = (1456, 1))#candidate|3236|(1456, 1)|var|float32
const_3237 = relay.const([3.628181,-7.736978,-9.064275,-1.083969,-2.490943,3.395416,-5.977675,7.577660,5.116110,-2.666759,-3.511422,4.325250,9.427728,6.035236,-0.208476,9.180374,-8.474799,9.836647,6.495488,-0.932499,5.212815,-5.881306,-7.704215,-7.470943,7.981796,-9.689165,-5.098341,-5.126943,-9.985724,-9.426009,-2.669832,-9.802992,3.757952,-2.909302,9.794529,-0.460890,-0.797757,3.332751,-6.426524,9.494082,-8.747228,-5.028828,8.196388,5.567649,-3.020526,-4.668815,9.980526,4.124739,4.493752,2.190536,6.967710,4.145204,-2.626603,-5.755876,-4.535698,3.241451,7.765704,1.438730,-0.898566,-3.474408,0.783823,-4.998880,-1.256468,7.595725,1.023707,-8.944673,7.440320,-7.725447,-4.080433,-0.373669,-7.387878,-1.879374,6.813056,9.014447,-6.810913,2.046531,-5.719053,-7.661098,8.570701,-2.724943,-2.381571,6.882755,-1.894580,0.443175,-4.005603,-3.435358,8.122464,-3.355362,-9.398723,3.789859,-7.023484,-1.201437,-5.233931,0.379970,3.659472,-5.047970,-7.177917,6.690130,1.075115,-2.813999,-5.392680,7.508250,2.847868,1.560809,8.414044,-0.053199,2.862985,-1.373380,0.054009,6.838456,-4.636127,-3.812806,-3.846707,9.590217,-9.585367,1.369104,-5.506662,8.035695,3.320682,-3.552798,7.907735,-5.947357,6.752615,-1.011329,-0.087378,7.224364,0.471819,1.077080,1.614727,7.542349,-1.012180,9.687097,5.462716,-7.697219,5.594182,5.216726,5.949235,7.584981,6.947531,6.866084], dtype = "float32")#candidate|3237|(140,)|const|float32
call_3235 = relay.TupleGetItem(func_2636_call(relay.reshape(var_3236.astype('float32'), [7, 16, 13]), relay.reshape(const_3237.astype('float32'), [35, 4]), relay.reshape(const_3237.astype('float32'), [35, 4]), ), 4)
call_3238 = relay.TupleGetItem(func_2640_call(relay.reshape(var_3236.astype('float32'), [7, 16, 13]), relay.reshape(const_3237.astype('float32'), [35, 4]), relay.reshape(const_3237.astype('float32'), [35, 4]), ), 4)
func_987_call = mod.get_global_var('func_987')
func_991_call = mutated_mod.get_global_var('func_991')
call_3247 = relay.TupleGetItem(func_987_call(relay.reshape(const_3237.astype('float32'), [14, 10, 1]), relay.reshape(const_3237.astype('float32'), [14, 10, 1]), ), 1)
call_3248 = relay.TupleGetItem(func_991_call(relay.reshape(const_3237.astype('float32'), [14, 10, 1]), relay.reshape(const_3237.astype('float32'), [14, 10, 1]), ), 1)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_3251 = func_1116_call()
call_3252 = func_1116_call()
func_1250_call = mod.get_global_var('func_1250')
func_1252_call = mutated_mod.get_global_var('func_1252')
var_3254 = relay.var("var_3254", dtype = "float32", shape = (364,))#candidate|3254|(364,)|var|float32
call_3253 = relay.TupleGetItem(func_1250_call(relay.reshape(var_3254.astype('float32'), [364,])), 1)
call_3255 = relay.TupleGetItem(func_1252_call(relay.reshape(var_3254.astype('float32'), [364,])), 1)
output = relay.Tuple([call_3229,call_3235,var_3236,const_3237,call_3247,call_3251,call_3253,var_3254,])
output2 = relay.Tuple([call_3230,call_3238,var_3236,const_3237,call_3248,call_3252,call_3255,var_3254,])
func_3257 = relay.Function([var_3236,var_3254,], output)
mod['func_3257'] = func_3257
mod = relay.transform.InferType()(mod)
var_3258 = relay.var("var_3258", dtype = "float32", shape = (1456, 1))#candidate|3258|(1456, 1)|var|float32
var_3259 = relay.var("var_3259", dtype = "float32", shape = (364,))#candidate|3259|(364,)|var|float32
output = func_3257(var_3258,var_3259,)
func_3260 = relay.Function([var_3258,var_3259,], output)
mutated_mod['func_3260'] = func_3260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_854_call = mod.get_global_var('func_854')
func_855_call = mutated_mod.get_global_var('func_855')
call_3283 = func_854_call()
call_3284 = func_854_call()
func_1039_call = mod.get_global_var('func_1039')
func_1041_call = mutated_mod.get_global_var('func_1041')
call_3294 = relay.TupleGetItem(func_1039_call(), 1)
call_3295 = relay.TupleGetItem(func_1041_call(), 1)
func_905_call = mod.get_global_var('func_905')
func_906_call = mutated_mod.get_global_var('func_906')
call_3300 = func_905_call()
call_3301 = func_905_call()
output = relay.Tuple([call_3283,call_3294,call_3300,])
output2 = relay.Tuple([call_3284,call_3295,call_3301,])
func_3312 = relay.Function([], output)
mod['func_3312'] = func_3312
mod = relay.transform.InferType()(mod)
mutated_mod['func_3312'] = func_3312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3312_call = mutated_mod.get_global_var('func_3312')
call_3313 = func_3312_call()
output = call_3313
func_3314 = relay.Function([], output)
mutated_mod['func_3314'] = func_3314
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3319 = relay.var("var_3319", dtype = "float64", shape = (2, 6, 7))#candidate|3319|(2, 6, 7)|var|float64
uop_3320 = relay.log2(var_3319.astype('float64')) # shape=(2, 6, 7)
output = uop_3320
output2 = uop_3320
func_3336 = relay.Function([var_3319,], output)
mod['func_3336'] = func_3336
mod = relay.transform.InferType()(mod)
var_3337 = relay.var("var_3337", dtype = "float64", shape = (2, 6, 7))#candidate|3337|(2, 6, 7)|var|float64
output = func_3336(var_3337)
func_3338 = relay.Function([var_3337], output)
mutated_mod['func_3338'] = func_3338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_3340 = relay.TupleGetItem(func_601_call(), 1)
call_3341 = relay.TupleGetItem(func_603_call(), 1)
output = relay.Tuple([call_3340,])
output2 = relay.Tuple([call_3341,])
func_3343 = relay.Function([], output)
mod['func_3343'] = func_3343
mod = relay.transform.InferType()(mod)
mutated_mod['func_3343'] = func_3343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3343_call = mutated_mod.get_global_var('func_3343')
call_3344 = func_3343_call()
output = call_3344
func_3345 = relay.Function([], output)
mutated_mod['func_3345'] = func_3345
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3413 = relay.var("var_3413", dtype = "float64", shape = (2, 13, 9))#candidate|3413|(2, 13, 9)|var|float64
uop_3414 = relay.sinh(var_3413.astype('float64')) # shape=(2, 13, 9)
func_1250_call = mod.get_global_var('func_1250')
func_1252_call = mutated_mod.get_global_var('func_1252')
var_3423 = relay.var("var_3423", dtype = "float32", shape = (1, 364))#candidate|3423|(1, 364)|var|float32
call_3422 = relay.TupleGetItem(func_1250_call(relay.reshape(var_3423.astype('float32'), [364,])), 2)
call_3424 = relay.TupleGetItem(func_1252_call(relay.reshape(var_3423.astype('float32'), [364,])), 2)
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
const_3426 = relay.const(8, dtype = "uint64")#candidate|3426|()|const|uint64
const_3427 = relay.const([-8,8,-8,10,-5,-6,1,-4,-6,9,-5,9,10,3,3,-2], dtype = "uint64")#candidate|3427|(16,)|const|uint64
call_3425 = relay.TupleGetItem(func_107_call(relay.reshape(const_3426.astype('uint64'), []), relay.reshape(const_3427.astype('uint64'), [1, 16]), ), 0)
call_3428 = relay.TupleGetItem(func_111_call(relay.reshape(const_3426.astype('uint64'), []), relay.reshape(const_3427.astype('uint64'), [1, 16]), ), 0)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_3429 = func_1116_call()
call_3430 = func_1116_call()
func_2897_call = mod.get_global_var('func_2897')
func_2898_call = mutated_mod.get_global_var('func_2898')
call_3445 = relay.TupleGetItem(func_2897_call(), 3)
call_3446 = relay.TupleGetItem(func_2898_call(), 3)
output = relay.Tuple([uop_3414,call_3422,var_3423,call_3425,const_3426,const_3427,call_3429,call_3445,])
output2 = relay.Tuple([uop_3414,call_3424,var_3423,call_3428,const_3426,const_3427,call_3430,call_3446,])
func_3450 = relay.Function([var_3413,var_3423,], output)
mod['func_3450'] = func_3450
mod = relay.transform.InferType()(mod)
var_3451 = relay.var("var_3451", dtype = "float64", shape = (2, 13, 9))#candidate|3451|(2, 13, 9)|var|float64
var_3452 = relay.var("var_3452", dtype = "float32", shape = (1, 364))#candidate|3452|(1, 364)|var|float32
output = func_3450(var_3451,var_3452,)
func_3453 = relay.Function([var_3451,var_3452,], output)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3479 = relay.var("var_3479", dtype = "float64", shape = (3, 12, 14))#candidate|3479|(3, 12, 14)|var|float64
uop_3480 = relay.log10(var_3479.astype('float64')) # shape=(3, 12, 14)
output = relay.Tuple([uop_3480,])
output2 = relay.Tuple([uop_3480,])
func_3499 = relay.Function([var_3479,], output)
mod['func_3499'] = func_3499
mod = relay.transform.InferType()(mod)
mutated_mod['func_3499'] = func_3499
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3500 = relay.var("var_3500", dtype = "float64", shape = (3, 12, 14))#candidate|3500|(3, 12, 14)|var|float64
func_3499_call = mutated_mod.get_global_var('func_3499')
call_3501 = func_3499_call(var_3500)
output = call_3501
func_3502 = relay.Function([var_3500], output)
mutated_mod['func_3502'] = func_3502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_3530 = relay.TupleGetItem(func_1097_call(), 0)
call_3531 = relay.TupleGetItem(func_1098_call(), 0)
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
call_3555 = relay.TupleGetItem(func_3057_call(), 0)
call_3556 = relay.TupleGetItem(func_3059_call(), 0)
output = relay.Tuple([call_3530,call_3555,])
output2 = relay.Tuple([call_3531,call_3556,])
func_3563 = relay.Function([], output)
mod['func_3563'] = func_3563
mod = relay.transform.InferType()(mod)
output = func_3563()
func_3564 = relay.Function([], output)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1904_call = mod.get_global_var('func_1904')
func_1905_call = mutated_mod.get_global_var('func_1905')
call_3571 = relay.TupleGetItem(func_1904_call(), 0)
call_3572 = relay.TupleGetItem(func_1905_call(), 0)
func_639_call = mod.get_global_var('func_639')
func_642_call = mutated_mod.get_global_var('func_642')
var_3584 = relay.var("var_3584", dtype = "float32", shape = (6,))#candidate|3584|(6,)|var|float32
call_3583 = relay.TupleGetItem(func_639_call(relay.reshape(var_3584.astype('float32'), [1, 2, 3])), 0)
call_3585 = relay.TupleGetItem(func_642_call(relay.reshape(var_3584.astype('float32'), [1, 2, 3])), 0)
output = relay.Tuple([call_3571,call_3583,var_3584,])
output2 = relay.Tuple([call_3572,call_3585,var_3584,])
func_3586 = relay.Function([var_3584,], output)
mod['func_3586'] = func_3586
mod = relay.transform.InferType()(mod)
var_3587 = relay.var("var_3587", dtype = "float32", shape = (6,))#candidate|3587|(6,)|var|float32
output = func_3586(var_3587)
func_3588 = relay.Function([var_3587], output)
mutated_mod['func_3588'] = func_3588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_3592 = func_1116_call()
call_3593 = func_1116_call()
output = call_3592
output2 = call_3593
func_3595 = relay.Function([], output)
mod['func_3595'] = func_3595
mod = relay.transform.InferType()(mod)
mutated_mod['func_3595'] = func_3595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3595_call = mutated_mod.get_global_var('func_3595')
call_3596 = func_3595_call()
output = call_3596
func_3597 = relay.Function([], output)
mutated_mod['func_3597'] = func_3597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2687_call = mod.get_global_var('func_2687')
func_2688_call = mutated_mod.get_global_var('func_2688')
call_3628 = relay.TupleGetItem(func_2687_call(), 1)
call_3629 = relay.TupleGetItem(func_2688_call(), 1)
output = call_3628
output2 = call_3629
func_3644 = relay.Function([], output)
mod['func_3644'] = func_3644
mod = relay.transform.InferType()(mod)
mutated_mod['func_3644'] = func_3644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3644_call = mutated_mod.get_global_var('func_3644')
call_3645 = func_3644_call()
output = call_3645
func_3646 = relay.Function([], output)
mutated_mod['func_3646'] = func_3646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3312_call = mod.get_global_var('func_3312')
func_3314_call = mutated_mod.get_global_var('func_3314')
call_3732 = relay.TupleGetItem(func_3312_call(), 1)
call_3733 = relay.TupleGetItem(func_3314_call(), 1)
output = relay.Tuple([call_3732,])
output2 = relay.Tuple([call_3733,])
func_3734 = relay.Function([], output)
mod['func_3734'] = func_3734
mod = relay.transform.InferType()(mod)
mutated_mod['func_3734'] = func_3734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3734_call = mutated_mod.get_global_var('func_3734')
call_3735 = func_3734_call()
output = call_3735
func_3736 = relay.Function([], output)
mutated_mod['func_3736'] = func_3736
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3863 = relay.const(False, dtype = "bool")#candidate|3863|()|const|bool
var_3864 = relay.var("var_3864", dtype = "bool", shape = (16, 3, 7))#candidate|3864|(16, 3, 7)|var|bool
bop_3865 = relay.logical_and(const_3863.astype('bool'), var_3864.astype('bool')) # shape=(16, 3, 7)
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_3902 = func_766_call()
call_3903 = func_766_call()
func_1904_call = mod.get_global_var('func_1904')
func_1905_call = mutated_mod.get_global_var('func_1905')
call_3904 = relay.TupleGetItem(func_1904_call(), 0)
call_3905 = relay.TupleGetItem(func_1905_call(), 0)
func_1485_call = mod.get_global_var('func_1485')
func_1486_call = mutated_mod.get_global_var('func_1486')
call_3914 = relay.TupleGetItem(func_1485_call(), 0)
call_3915 = relay.TupleGetItem(func_1486_call(), 0)
output = relay.Tuple([bop_3865,call_3902,call_3904,call_3914,])
output2 = relay.Tuple([bop_3865,call_3903,call_3905,call_3915,])
func_3924 = relay.Function([var_3864,], output)
mod['func_3924'] = func_3924
mod = relay.transform.InferType()(mod)
mutated_mod['func_3924'] = func_3924
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3925 = relay.var("var_3925", dtype = "bool", shape = (16, 3, 7))#candidate|3925|(16, 3, 7)|var|bool
func_3924_call = mutated_mod.get_global_var('func_3924')
call_3926 = func_3924_call(var_3925)
output = call_3926
func_3927 = relay.Function([var_3925], output)
mutated_mod['func_3927'] = func_3927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1793_call = mod.get_global_var('func_1793')
func_1795_call = mutated_mod.get_global_var('func_1795')
call_3957 = relay.TupleGetItem(func_1793_call(), 1)
call_3958 = relay.TupleGetItem(func_1795_call(), 1)
output = call_3957
output2 = call_3958
func_3977 = relay.Function([], output)
mod['func_3977'] = func_3977
mod = relay.transform.InferType()(mod)
mutated_mod['func_3977'] = func_3977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mutated_mod.get_global_var('func_3977')
call_3978 = func_3977_call()
output = call_3978
func_3979 = relay.Function([], output)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3987 = relay.const([[[0.490896,4.248123,0.549723,1.461600,6.887467,4.947476,-6.740598,4.858712,-8.000426,1.268730,4.933987,4.144244,2.061514,-1.184380,-1.994331],[3.272187,-1.512506,-9.520428,-0.062252,-8.691338,6.681510,1.890564,-1.454900,-1.378324,-9.015001,0.915905,-4.237120,1.817063,4.503806,-4.644773],[7.626489,-3.360321,-3.732311,2.715436,-3.274609,0.084351,-0.405710,6.702196,1.226842,0.060025,4.671098,8.262122,-4.403822,5.539707,-3.679049],[2.784488,6.046502,-7.815700,-4.198799,-6.734062,1.908917,-9.062227,-9.157324,-1.952420,7.820828,9.780315,3.486191,-4.563745,0.910729,1.384524],[6.955261,-3.983997,-7.026695,2.540003,-4.855550,6.304780,9.936251,2.903762,6.252391,5.178446,-9.413228,2.966750,7.763115,0.870448,-2.890982],[5.900026,4.669133,-0.766290,-8.340023,-8.261975,-7.462086,-1.159132,8.811932,3.541583,-1.281107,6.964702,-9.316966,-3.114252,0.718812,-8.696633],[-7.604060,5.583206,5.842623,-5.536124,7.491027,0.860766,-2.487927,5.616153,6.399269,4.029367,2.911736,-9.972090,6.996057,-2.028945,-0.526767]],[[-4.504440,-9.751589,-2.742178,-0.300272,0.953792,7.223987,3.889089,-8.458588,5.638497,0.899649,7.468226,-7.394165,-5.707878,-5.500486,-7.077842],[-3.845737,-1.262314,-4.874021,-5.302739,1.963413,7.881507,-3.322061,-2.087956,9.138637,9.979985,-4.725697,-6.520014,-7.221262,1.612234,4.246410],[-0.470815,-5.822549,-1.323267,1.364230,5.828084,-0.558531,-4.706857,4.320156,4.550999,-8.435606,-8.593454,-5.860547,8.942229,3.222623,9.020847],[-8.072380,-9.909981,-1.460324,-5.223686,-1.130472,-1.080558,-1.009714,5.357779,-1.916678,-3.629367,1.695964,2.147185,1.419705,1.261909,7.570675],[1.103605,-0.553330,5.369566,-3.500358,-2.239991,4.159941,5.243488,0.281957,-8.727838,-7.616719,6.119646,4.743067,5.492173,4.894799,3.930240],[8.862486,6.831773,6.679292,5.496402,-8.834895,-7.411324,-6.521856,9.398614,-5.656524,9.985486,-3.376871,7.236642,-7.283261,7.433202,2.743850],[-9.590740,0.568120,-7.392023,-7.794057,2.799428,9.535502,8.120782,3.544057,-6.622684,-2.918310,-7.547804,-3.821729,-0.821735,-1.181471,-5.002858]],[[-8.460622,4.859036,-4.682830,-9.583914,5.971916,9.095390,6.689507,-7.309799,4.187574,0.986132,2.806431,9.201214,3.411445,-2.419818,6.658260],[8.467444,2.037358,1.252593,-0.959771,8.712649,9.473098,-1.821218,8.163769,-6.038928,4.916730,-2.532910,7.212731,-4.412204,4.469588,4.025180],[-3.597112,-9.189228,9.540650,6.106150,-2.838554,6.085651,-4.720483,-3.804870,-4.082652,-1.677751,-2.196857,-9.842100,-6.677828,-4.325523,0.813397],[-9.056816,-9.672010,-3.699406,4.757914,2.089472,-0.975317,3.789035,0.150058,-5.410663,-1.018279,2.625479,8.138889,1.798176,1.458313,5.004447],[7.016284,-6.573200,-1.903380,2.986863,-0.717492,6.138979,6.499983,2.206707,9.540505,-0.432362,3.753307,-6.183854,-8.382738,-0.162111,-5.416538],[-6.711474,-5.577269,0.522391,9.250390,-1.849554,-1.667980,-5.727988,-5.780615,-8.640228,2.933021,-9.269441,-8.850832,2.826470,-8.087522,-8.375724],[9.354560,-0.068477,3.202211,1.833929,-9.468809,9.546243,2.188919,-4.069179,2.872992,5.794036,9.465712,5.859764,9.080728,-8.298870,8.018173]],[[-2.280673,-8.281651,-9.811600,-9.488402,-5.971476,6.050010,8.845833,-8.854128,-3.605318,-3.788479,-8.076117,8.755736,-0.207801,9.202261,-8.910783],[4.460201,5.696499,2.246850,-8.514230,1.316114,-3.282079,-4.936574,-8.173886,1.253516,-5.275978,-1.603301,-4.736933,0.382456,-0.294807,2.204507],[4.966533,4.322344,-8.793088,-8.351320,7.030859,-8.066352,-0.213926,6.165049,2.060469,7.759496,0.705933,-0.921585,-1.368384,-8.120046,-6.752231],[3.446770,-3.623058,6.795783,-3.767091,0.236215,7.809184,0.115396,-7.674056,-7.542228,-4.798777,-5.050979,-2.749237,1.036365,-0.758878,9.156756],[1.143425,-6.267481,-1.122635,6.845257,7.418430,-7.005271,-9.139329,-2.502664,-8.541731,-0.053414,-9.321230,-4.987865,5.218988,6.303589,1.559301],[3.659033,-1.205042,5.924183,1.304809,6.037047,6.260547,1.587573,7.623967,0.848519,5.077928,-7.656612,-1.477297,-3.761865,-6.225448,2.667153],[-6.187104,0.351305,-0.274694,2.686374,5.375136,-2.438512,-6.183787,-3.463597,5.466521,-9.540326,9.078209,-8.329177,6.483433,4.325222,9.951115]],[[-9.137737,5.636136,-7.213847,-9.487617,2.862144,-1.497911,-2.781107,-7.839442,-6.797700,-3.394031,-8.271504,-9.022225,7.863791,9.647933,3.738772],[9.496717,-6.597064,1.228624,-6.295225,9.556122,7.792750,7.718957,-3.978501,-7.974764,3.605311,2.606758,-0.887571,0.912058,-0.636524,8.052646],[4.687311,4.948614,5.794770,-8.747156,-5.067683,-8.512314,5.282377,4.561689,2.963520,-6.604049,9.689545,-0.042532,3.455314,9.416174,-8.463148],[-1.451319,-3.304282,2.759830,-5.978893,6.594741,3.827947,1.870207,-9.965068,4.266785,-4.395795,-9.040408,4.846886,-9.300279,-6.031065,-1.668884],[-3.866698,-0.563096,-4.905488,-3.199370,8.613499,1.880712,0.890415,5.082981,-1.066999,9.970410,4.307178,-8.296995,-7.141067,2.539694,-4.808914],[2.145636,-6.415696,9.091625,-7.099593,-8.167769,-9.558187,-9.568591,-5.468577,9.578743,-2.176075,7.961637,-3.581146,5.134405,-7.434088,-4.094344],[-3.423753,6.494989,9.564508,-4.155321,0.277997,-4.557487,-5.317406,8.050065,-3.086242,4.151874,-2.688162,-3.314612,-7.399881,0.253609,2.660230]],[[-8.687053,-1.953792,-1.010564,-7.194775,7.247359,8.880944,5.409358,-9.751755,-5.855633,0.482331,-2.543425,2.427289,0.567237,-9.267311,-6.700778],[-9.593557,4.217223,7.174352,-5.536647,-4.647688,5.027855,0.886439,-4.564868,5.656572,9.351179,-6.171317,-5.148357,-8.169515,-9.368067,4.255427],[-7.933663,9.823527,-4.871157,-9.925967,-8.531987,-0.936100,-7.560370,6.450830,8.742128,-7.241467,9.460510,-9.899467,-7.781668,2.379519,0.830800],[0.271488,-4.121440,-9.405396,2.183066,-8.043033,8.962017,1.682054,-6.206354,-5.499701,-0.529782,-1.438085,-1.959696,5.106518,-3.488384,8.167960],[7.684123,8.311659,6.134148,-1.050429,-9.311346,-2.899474,9.652937,-5.959497,-0.652883,-3.648560,8.025558,6.487455,6.271845,-8.961751,5.658479],[-5.171721,-3.414788,0.528598,9.400258,4.120778,-0.291706,4.754873,2.212048,7.542046,5.540184,-1.496520,8.148969,-5.474491,5.008976,-6.735829],[-8.718289,7.463741,-8.875803,-1.218346,9.942436,-7.902666,2.892229,9.962639,8.902758,1.202134,-0.598781,2.430349,9.855234,9.888459,-3.273844]],[[5.145245,-1.981249,7.128789,2.462419,-6.710827,2.931795,-7.807905,-9.965195,-4.295214,2.329207,-8.281706,8.796033,3.883720,2.692424,0.033866],[-1.434009,-6.720189,-9.405351,1.164592,8.270116,-6.056378,-8.837148,-1.912288,-3.044249,-2.600144,-3.506045,-7.664885,-1.091433,-6.285618,-7.366629],[0.576813,-5.889028,9.590425,-0.690541,3.333346,-4.628777,-6.864699,-9.233145,1.427044,4.760462,-2.091213,8.557625,-6.252077,-2.980381,4.587686],[-5.446868,8.511419,5.057080,9.104329,-5.503521,7.114042,-8.402953,9.580407,-6.273290,-0.633754,3.770808,4.002503,4.164601,-1.740264,-0.554928],[-7.313650,1.607984,-6.442717,-7.366885,-0.959212,-7.518781,7.212443,0.762086,0.332789,9.681064,-8.539507,6.509464,5.102317,6.776052,-5.936951],[-5.931207,-0.322231,9.229365,-3.911842,7.934512,-6.077332,-9.367366,-5.087120,-2.053784,-8.429772,1.069745,-0.436633,-5.821275,9.561128,-1.197178],[-2.883569,-8.526424,-9.482403,9.140887,8.765957,1.179767,-4.413208,3.019943,9.745607,-5.811234,-3.683820,-5.444496,-2.362260,-3.420196,-9.155244]],[[-8.158882,0.381223,-4.108182,-3.703574,-4.383987,-4.318958,3.489065,-8.926351,7.102078,-0.562923,2.745966,-2.330581,-5.548018,-1.148374,-8.787021],[6.400039,5.210357,-8.597225,-1.245834,4.357980,-7.856712,-1.589493,-3.162928,9.367389,-5.354040,-6.655484,-6.022702,-7.997822,1.476688,7.710405],[8.223140,-2.917716,-2.430659,-3.430701,4.114499,4.278319,0.942053,3.091195,-6.240308,-0.624666,0.156794,-7.608040,5.144554,-7.470467,-7.252798],[-2.728633,-9.683821,-5.609946,4.189433,2.191672,3.974220,5.063384,-6.767259,-6.499585,9.039803,5.870848,2.055640,-3.348195,-9.959479,-2.903349],[-3.967797,9.006845,7.537012,0.577478,-3.645421,-8.886104,-9.029353,0.501506,-1.142731,5.462306,-0.251931,-1.231217,9.665198,-1.217417,2.722299],[-2.639469,8.419656,-4.839127,5.131243,-3.126106,-4.206274,9.765988,-2.269485,3.285442,3.214981,-4.979538,-0.054512,7.123432,4.922333,4.126580],[-0.483786,-9.573455,1.533227,5.221525,7.283820,3.789946,-1.606948,-8.038152,3.866328,7.152253,-4.214521,-9.778839,5.363541,-1.173531,9.945735]]], dtype = "float32")#candidate|3987|(8, 7, 15)|const|float32
var_3988 = relay.var("var_3988", dtype = "float32", shape = (8, 7, 15))#candidate|3988|(8, 7, 15)|var|float32
bop_3989 = relay.floor_mod(const_3987.astype('float32'), relay.reshape(var_3988.astype('float32'), relay.shape_of(const_3987))) # shape=(8, 7, 15)
func_3082_call = mod.get_global_var('func_3082')
func_3086_call = mutated_mod.get_global_var('func_3086')
var_3998 = relay.var("var_3998", dtype = "float64", shape = (900,))#candidate|3998|(900,)|var|float64
var_3999 = relay.var("var_3999", dtype = "int32", shape = (3, 90))#candidate|3999|(3, 90)|var|int32
call_3997 = relay.TupleGetItem(func_3082_call(relay.reshape(var_3998.astype('float64'), [5, 15, 12]), relay.reshape(var_3999.astype('int32'), [270,]), ), 1)
call_4000 = relay.TupleGetItem(func_3086_call(relay.reshape(var_3998.astype('float64'), [5, 15, 12]), relay.reshape(var_3999.astype('int32'), [270,]), ), 1)
uop_4001 = relay.acos(bop_3989.astype('float32')) # shape=(8, 7, 15)
func_3924_call = mod.get_global_var('func_3924')
func_3927_call = mutated_mod.get_global_var('func_3927')
var_4007 = relay.var("var_4007", dtype = "bool", shape = (24, 14))#candidate|4007|(24, 14)|var|bool
call_4006 = relay.TupleGetItem(func_3924_call(relay.reshape(var_4007.astype('bool'), [16, 3, 7])), 0)
call_4008 = relay.TupleGetItem(func_3927_call(relay.reshape(var_4007.astype('bool'), [16, 3, 7])), 0)
output = relay.Tuple([call_3997,var_3998,var_3999,uop_4001,call_4006,var_4007,])
output2 = relay.Tuple([call_4000,var_3998,var_3999,uop_4001,call_4008,var_4007,])
func_4019 = relay.Function([var_3988,var_3998,var_3999,var_4007,], output)
mod['func_4019'] = func_4019
mod = relay.transform.InferType()(mod)
mutated_mod['func_4019'] = func_4019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4019_call = mutated_mod.get_global_var('func_4019')
var_4021 = relay.var("var_4021", dtype = "float32", shape = (8, 7, 15))#candidate|4021|(8, 7, 15)|var|float32
var_4022 = relay.var("var_4022", dtype = "float64", shape = (900,))#candidate|4022|(900,)|var|float64
var_4023 = relay.var("var_4023", dtype = "int32", shape = (3, 90))#candidate|4023|(3, 90)|var|int32
var_4024 = relay.var("var_4024", dtype = "bool", shape = (24, 14))#candidate|4024|(24, 14)|var|bool
call_4020 = func_4019_call(var_4021,var_4022,var_4023,var_4024,)
output = call_4020
func_4025 = relay.Function([var_4021,var_4022,var_4023,var_4024,], output)
mutated_mod['func_4025'] = func_4025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3343_call = mod.get_global_var('func_3343')
func_3345_call = mutated_mod.get_global_var('func_3345')
call_4098 = relay.TupleGetItem(func_3343_call(), 0)
call_4099 = relay.TupleGetItem(func_3345_call(), 0)
func_2636_call = mod.get_global_var('func_2636')
func_2640_call = mutated_mod.get_global_var('func_2640')
var_4115 = relay.var("var_4115", dtype = "float32", shape = (1456,))#candidate|4115|(1456,)|var|float32
var_4116 = relay.var("var_4116", dtype = "float32", shape = (1, 140))#candidate|4116|(1, 140)|var|float32
call_4114 = relay.TupleGetItem(func_2636_call(relay.reshape(var_4115.astype('float32'), [7, 16, 13]), relay.reshape(var_4116.astype('float32'), [35, 4]), relay.reshape(var_4116.astype('float32'), [35, 4]), ), 4)
call_4117 = relay.TupleGetItem(func_2640_call(relay.reshape(var_4115.astype('float32'), [7, 16, 13]), relay.reshape(var_4116.astype('float32'), [35, 4]), relay.reshape(var_4116.astype('float32'), [35, 4]), ), 4)
bop_4121 = relay.logical_and(call_4114.astype('bool'), call_4098.astype('bool')) # shape=(3, 11, 16)
bop_4124 = relay.logical_and(call_4117.astype('bool'), call_4099.astype('bool')) # shape=(3, 11, 16)
func_4019_call = mod.get_global_var('func_4019')
func_4025_call = mutated_mod.get_global_var('func_4025')
var_4128 = relay.var("var_4128", dtype = "float32", shape = (840,))#candidate|4128|(840,)|var|float32
var_4129 = relay.var("var_4129", dtype = "float64", shape = (900,))#candidate|4129|(900,)|var|float64
var_4130 = relay.var("var_4130", dtype = "int32", shape = (30, 9))#candidate|4130|(30, 9)|var|int32
const_4131 = relay.const([True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,False], dtype = "bool")#candidate|4131|(336,)|const|bool
call_4127 = relay.TupleGetItem(func_4019_call(relay.reshape(var_4128.astype('float32'), [8, 7, 15]), relay.reshape(var_4129.astype('float64'), [900,]), relay.reshape(var_4130.astype('int32'), [3, 90]), relay.reshape(const_4131.astype('bool'), [24, 14]), ), 2)
call_4132 = relay.TupleGetItem(func_4025_call(relay.reshape(var_4128.astype('float32'), [8, 7, 15]), relay.reshape(var_4129.astype('float64'), [900,]), relay.reshape(var_4130.astype('int32'), [3, 90]), relay.reshape(const_4131.astype('bool'), [24, 14]), ), 2)
func_1422_call = mod.get_global_var('func_1422')
func_1426_call = mutated_mod.get_global_var('func_1426')
var_4157 = relay.var("var_4157", dtype = "float64", shape = (2640,))#candidate|4157|(2640,)|var|float64
call_4156 = relay.TupleGetItem(func_1422_call(relay.reshape(var_4157.astype('float64'), [16, 15, 11]), relay.reshape(var_4157.astype('float32'), [16, 15, 11]), ), 0)
call_4158 = relay.TupleGetItem(func_1426_call(relay.reshape(var_4157.astype('float64'), [16, 15, 11]), relay.reshape(var_4157.astype('float32'), [16, 15, 11]), ), 0)
bop_4164 = relay.not_equal(call_4127.astype('bool'), relay.reshape(var_4130.astype('bool'), relay.shape_of(call_4127))) # shape=(3, 90)
bop_4167 = relay.not_equal(call_4132.astype('bool'), relay.reshape(var_4130.astype('bool'), relay.shape_of(call_4132))) # shape=(3, 90)
output = relay.Tuple([var_4115,var_4116,bop_4121,var_4128,var_4129,const_4131,call_4156,var_4157,bop_4164,])
output2 = relay.Tuple([var_4115,var_4116,bop_4124,var_4128,var_4129,const_4131,call_4158,var_4157,bop_4167,])
func_4168 = relay.Function([var_4115,var_4116,var_4128,var_4129,var_4130,var_4157,], output)
mod['func_4168'] = func_4168
mod = relay.transform.InferType()(mod)
mutated_mod['func_4168'] = func_4168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4168_call = mutated_mod.get_global_var('func_4168')
var_4170 = relay.var("var_4170", dtype = "float32", shape = (1456,))#candidate|4170|(1456,)|var|float32
var_4171 = relay.var("var_4171", dtype = "float32", shape = (1, 140))#candidate|4171|(1, 140)|var|float32
var_4172 = relay.var("var_4172", dtype = "float32", shape = (840,))#candidate|4172|(840,)|var|float32
var_4173 = relay.var("var_4173", dtype = "float64", shape = (900,))#candidate|4173|(900,)|var|float64
var_4174 = relay.var("var_4174", dtype = "int32", shape = (30, 9))#candidate|4174|(30, 9)|var|int32
var_4175 = relay.var("var_4175", dtype = "float64", shape = (2640,))#candidate|4175|(2640,)|var|float64
call_4169 = func_4168_call(var_4170,var_4171,var_4172,var_4173,var_4174,var_4175,)
output = call_4169
func_4176 = relay.Function([var_4170,var_4171,var_4172,var_4173,var_4174,var_4175,], output)
mutated_mod['func_4176'] = func_4176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
call_4236 = relay.TupleGetItem(func_2326_call(), 3)
call_4237 = relay.TupleGetItem(func_2328_call(), 3)
output = call_4236
output2 = call_4237
func_4256 = relay.Function([], output)
mod['func_4256'] = func_4256
mod = relay.transform.InferType()(mod)
mutated_mod['func_4256'] = func_4256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4256_call = mutated_mod.get_global_var('func_4256')
call_4257 = func_4256_call()
output = call_4257
func_4258 = relay.Function([], output)
mutated_mod['func_4258'] = func_4258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4282 = relay.var("var_4282", dtype = "float32", shape = (12, 10, 11))#candidate|4282|(12, 10, 11)|var|float32
uop_4283 = relay.log(var_4282.astype('float32')) # shape=(12, 10, 11)
bop_4286 = relay.logical_xor(uop_4283.astype('uint64'), relay.reshape(var_4282.astype('uint64'), relay.shape_of(uop_4283))) # shape=(12, 10, 11)
uop_4290 = relay.sinh(var_4282.astype('float32')) # shape=(12, 10, 11)
output = relay.Tuple([bop_4286,uop_4290,])
output2 = relay.Tuple([bop_4286,uop_4290,])
func_4299 = relay.Function([var_4282,], output)
mod['func_4299'] = func_4299
mod = relay.transform.InferType()(mod)
mutated_mod['func_4299'] = func_4299
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4300 = relay.var("var_4300", dtype = "float32", shape = (12, 10, 11))#candidate|4300|(12, 10, 11)|var|float32
func_4299_call = mutated_mod.get_global_var('func_4299')
call_4301 = func_4299_call(var_4300)
output = call_4301
func_4302 = relay.Function([var_4300], output)
mutated_mod['func_4302'] = func_4302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1904_call = mod.get_global_var('func_1904')
func_1905_call = mutated_mod.get_global_var('func_1905')
call_4337 = relay.TupleGetItem(func_1904_call(), 0)
call_4338 = relay.TupleGetItem(func_1905_call(), 0)
output = relay.Tuple([call_4337,])
output2 = relay.Tuple([call_4338,])
func_4354 = relay.Function([], output)
mod['func_4354'] = func_4354
mod = relay.transform.InferType()(mod)
mutated_mod['func_4354'] = func_4354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4354_call = mutated_mod.get_global_var('func_4354')
call_4355 = func_4354_call()
output = call_4355
func_4356 = relay.Function([], output)
mutated_mod['func_4356'] = func_4356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3563_call = mod.get_global_var('func_3563')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_4360 = relay.TupleGetItem(func_3563_call(), 1)
call_4361 = relay.TupleGetItem(func_3564_call(), 1)
output = relay.Tuple([call_4360,])
output2 = relay.Tuple([call_4361,])
func_4397 = relay.Function([], output)
mod['func_4397'] = func_4397
mod = relay.transform.InferType()(mod)
mutated_mod['func_4397'] = func_4397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4397_call = mutated_mod.get_global_var('func_4397')
call_4398 = func_4397_call()
output = call_4398
func_4399 = relay.Function([], output)
mutated_mod['func_4399'] = func_4399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4407 = relay.var("var_4407", dtype = "float32", shape = (2, 16, 12))#candidate|4407|(2, 16, 12)|var|float32
uop_4408 = relay.sqrt(var_4407.astype('float32')) # shape=(2, 16, 12)
bop_4415 = relay.equal(uop_4408.astype('bool'), relay.reshape(var_4407.astype('bool'), relay.shape_of(uop_4408))) # shape=(2, 16, 12)
output = bop_4415
output2 = bop_4415
func_4439 = relay.Function([var_4407,], output)
mod['func_4439'] = func_4439
mod = relay.transform.InferType()(mod)
var_4440 = relay.var("var_4440", dtype = "float32", shape = (2, 16, 12))#candidate|4440|(2, 16, 12)|var|float32
output = func_4439(var_4440)
func_4441 = relay.Function([var_4440], output)
mutated_mod['func_4441'] = func_4441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1904_call = mod.get_global_var('func_1904')
func_1905_call = mutated_mod.get_global_var('func_1905')
call_4483 = relay.TupleGetItem(func_1904_call(), 0)
call_4484 = relay.TupleGetItem(func_1905_call(), 0)
func_4256_call = mod.get_global_var('func_4256')
func_4258_call = mutated_mod.get_global_var('func_4258')
call_4499 = func_4256_call()
call_4500 = func_4256_call()
output = relay.Tuple([call_4483,call_4499,])
output2 = relay.Tuple([call_4484,call_4500,])
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
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_4549 = relay.TupleGetItem(func_718_call(), 0)
call_4550 = relay.TupleGetItem(func_720_call(), 0)
func_1422_call = mod.get_global_var('func_1422')
func_1426_call = mutated_mod.get_global_var('func_1426')
const_4558 = relay.const([[-3.174610,1.106962,1.144255,-3.158128,0.715091,1.756075,-3.444636,7.879750,-7.920728,6.299370,4.782442,5.255349,-0.672386,9.544324,8.662890,-4.597038,-3.732526,-9.123047,6.996097,-7.562851],[4.310664,6.476533,8.057650,-3.026868,-4.891294,-4.005710,-0.518931,-0.239111,-5.994804,0.584597,-6.922899,5.729409,5.912418,-5.853838,1.279889,-1.310076,-0.196797,-9.596519,-1.541284,-5.547774],[-3.872231,-7.473953,-4.246483,9.473322,-4.678523,5.741119,-4.310929,6.044211,-4.008587,8.862895,-4.386582,-8.949736,9.980745,9.788975,-3.002487,0.499704,-3.758750,7.913167,-7.373062,9.256965],[1.070121,-2.291725,-1.549009,7.360477,0.976509,-6.829996,-6.792847,8.912017,5.827481,6.716054,-5.176674,-4.381431,-6.286099,6.870432,-1.088700,-7.995803,2.133407,4.355015,-8.114901,0.950479],[5.508154,-7.021794,-1.922302,-9.912727,-7.322592,2.239928,-3.892597,7.650578,0.727309,3.057453,7.912179,1.053923,-9.333760,-4.462165,-5.135313,1.162048,4.903603,6.639073,9.516316,4.804652],[-9.060645,-0.407796,-2.117703,5.835076,-3.224276,5.025554,-5.199888,7.501566,-2.753311,-2.738558,7.378232,-7.657100,8.347830,-2.001185,8.305837,-3.242453,4.493596,-6.648742,-5.216244,3.441412],[1.319944,-8.220995,-3.206825,-4.557399,-9.830784,8.303709,-8.787160,-4.868749,5.195460,-2.071126,5.846857,-0.746741,3.333653,-7.011429,1.273898,2.274962,3.801799,-6.652928,5.816715,-1.053595],[6.792178,8.145286,2.444914,8.534250,-4.238910,-0.733423,-0.753148,-0.388295,3.648217,8.586447,0.683835,0.108611,0.595752,-0.094556,3.655551,-6.583559,-3.703440,-9.118908,1.377637,-4.862783],[-1.241726,6.159207,-5.357811,-1.094036,8.220635,-4.510649,-3.299354,7.001047,6.675545,-9.768838,-1.693652,-7.677001,-1.716561,-0.199976,-9.137659,-7.326568,0.009561,-1.311089,8.330891,-9.533782],[-2.154677,1.698598,-2.264923,-0.190650,-0.554194,-5.970318,9.416264,4.706746,-1.641613,-2.700779,7.608745,5.333092,-8.547953,-3.958974,-5.508360,-4.252889,9.734917,-4.436640,-0.563738,3.190616],[5.053262,2.678572,-2.032639,1.344264,8.643659,-2.528997,-9.710942,9.768663,4.499433,-7.358879,-3.207919,-8.694400,1.455531,-3.183136,-2.534152,-3.546207,7.410611,-9.816999,1.634505,-4.763938],[5.343086,5.452809,-5.448787,0.923601,-0.820597,-7.129548,-1.198843,-7.400692,8.245613,-0.691484,-8.394881,6.300298,-3.339387,-1.641287,5.015554,-5.824765,0.493729,-2.269022,8.612049,0.366885],[-0.601412,-4.969248,-8.286996,-6.994469,7.406351,2.546213,9.978246,-2.748729,7.908100,1.724166,6.931979,0.345175,7.096976,8.980313,6.471010,-8.320543,-4.341332,4.600484,7.149060,-0.581879],[-0.071617,0.084718,-5.449424,8.765426,-3.405625,5.960181,5.408983,-7.615915,-1.944017,8.851002,-0.275891,8.873118,-5.354364,6.897930,-6.124645,6.010420,-1.881162,9.776064,-2.149172,-4.427848],[8.910229,-6.667418,-1.073310,-8.131103,-6.249115,4.648933,1.994197,6.689560,6.209021,-4.426119,-2.904886,-2.386563,-3.373290,-7.820900,-0.732558,9.275561,-8.426815,-4.951747,-4.322835,8.148914],[-3.946063,3.664339,-6.891267,-5.842539,4.805009,1.921206,-8.880162,-9.863346,3.708478,8.780291,1.478245,-3.833743,-9.025076,7.484786,5.541122,-9.159438,6.626085,2.396766,-0.822006,8.226829],[-6.822123,-7.159673,-4.291263,9.096080,2.466893,4.781400,3.736074,-6.671028,1.772759,-9.906034,-1.605672,-8.373632,-4.996531,3.921598,3.848676,8.204236,-8.629437,-0.441724,-3.407993,-2.865989],[-0.201338,4.680775,3.266097,-0.133246,6.731699,9.651037,5.363220,4.837435,-7.861761,-6.172239,9.911222,1.850085,4.019605,-1.757991,-9.003814,0.577851,-3.866512,-5.493344,-8.273527,-7.442790],[-3.194622,-4.818203,-9.166828,6.301604,-2.636911,-6.069032,1.538584,0.263008,-7.284725,9.163729,2.499567,8.034008,6.952292,1.759219,-8.069436,0.016317,-8.750217,-3.374873,0.019027,4.005471],[-1.701372,2.098082,6.082335,-0.207506,-6.307566,-7.643122,0.956369,0.048757,-1.607288,-9.070236,8.165365,7.528981,6.095653,-5.559076,7.366510,5.068694,4.178986,-1.837874,4.620024,-7.694327],[-8.969762,1.202741,7.783896,-0.548473,-1.034225,-1.764678,-1.855031,8.334184,-7.869001,-6.820809,8.249623,1.043960,-7.154408,3.472860,-7.159520,7.412385,0.551810,-6.251927,1.387865,-4.412132],[-1.947024,9.337884,-0.091184,-7.330592,-4.301494,-9.361151,-9.690531,2.681152,1.385885,9.571637,-9.913342,-8.762100,5.490979,-7.211124,5.367080,-3.231193,-9.443363,-8.712727,-4.443336,4.827750],[6.302345,-7.524880,9.139965,-6.924252,9.485491,-1.525420,-1.917250,9.737563,-7.814302,1.512175,-8.563436,1.047357,2.426787,5.104820,-6.243792,1.250789,-7.615360,-4.697194,9.351627,4.127324],[-3.564291,-7.314880,-2.333202,-9.243915,-2.703714,2.208002,-4.846040,0.995140,-6.792290,7.988020,1.174120,2.669385,3.182679,7.015505,-1.957571,9.958071,-4.205463,-3.050221,2.049356,8.376665],[-7.917807,-1.723174,0.085809,-6.131692,-4.076656,1.196723,-3.185510,3.613164,-3.447889,-8.791034,9.786771,8.488149,-8.268981,1.140168,-7.779324,7.007958,6.261041,1.979632,3.928567,-6.328159],[-4.781624,4.362333,-5.353254,-3.019166,8.647655,-6.110865,-1.009790,-0.687361,0.836508,-5.004740,8.632045,-1.348262,7.606977,8.103941,9.252515,-9.351911,7.664727,8.735458,-4.483318,-8.516009],[-1.515638,4.097284,-3.646194,4.945001,4.764771,-0.759434,1.193738,7.221020,-0.092823,0.019862,-2.273677,7.624064,4.896565,-9.198515,-7.191143,5.572734,8.747568,7.219229,0.575066,4.776666],[-8.635620,7.905191,-7.360519,-7.799980,5.939950,-8.943615,2.577756,-0.399757,-5.400677,6.341196,2.360616,-4.343173,1.046358,5.244898,-6.245801,2.204476,-6.022931,4.274827,1.399173,1.535211],[5.870182,-3.176096,-6.432309,-8.603739,5.264708,8.002628,-3.124320,1.381130,-1.285755,-8.568578,4.648676,7.961771,-1.162902,-9.718287,3.607925,9.094999,-1.311438,0.085075,-3.972422,4.987601],[7.732476,-4.840438,-4.316261,5.944704,-9.173968,-6.100828,0.150765,7.597353,-2.036528,9.528060,-0.013277,-6.062433,2.850573,0.071827,3.882645,7.248655,1.645806,2.406843,-9.310314,-5.738802],[-0.890429,-2.843845,6.800271,-8.671402,-5.029267,9.104144,-1.680215,4.459454,8.570069,6.194916,6.164170,-6.171827,-2.474129,9.646722,-8.650976,-7.283976,-8.167750,3.709198,-0.700639,6.294432],[5.701447,3.733107,-0.413953,4.464088,2.553742,9.877930,-1.804888,-5.308857,3.074513,0.891956,3.582104,-0.775990,-2.527607,8.174400,4.551947,6.063799,9.209496,-7.812811,5.495003,-3.821567],[-6.003591,-7.942247,5.393393,-7.903622,-1.632052,-2.384539,9.575958,1.125441,-9.713832,-8.162646,1.482879,9.918694,4.674888,-1.698971,8.391260,2.872941,-7.242581,-2.569052,-7.502400,-2.348206],[-5.886199,0.798432,-3.425280,-9.842479,2.982830,-4.187969,-9.959699,-5.386033,-1.128963,8.205583,4.601574,0.805997,-1.840006,5.435548,-4.167706,1.354636,-2.457591,-7.900214,5.837216,-1.475987],[-1.532168,1.927718,-7.808137,-7.847757,-7.876438,-0.468678,-2.238381,-5.414241,-7.796108,-4.296003,9.423209,2.814697,-9.381467,-6.920031,-0.820771,-9.482242,-0.632049,-2.155430,7.009471,2.168528],[-8.795404,7.625557,5.393626,8.420583,5.490971,4.964219,9.019733,9.424512,-2.615726,9.973925,-6.341126,6.063233,3.231391,3.367844,-2.243076,-0.276265,-6.537566,-5.397170,1.775737,4.480304],[5.249835,-1.152223,-5.518834,-0.741964,4.397345,6.357102,7.641889,-4.522299,-9.643638,-1.963939,-8.102020,9.710060,-1.864353,8.138215,3.477961,0.756236,0.499126,7.810274,1.675448,-0.682236],[0.440752,-6.153559,3.998894,9.732428,-3.291002,-1.914207,7.721296,2.337997,4.886202,2.812886,-2.721396,2.119591,-8.501576,6.288815,-0.159993,0.011100,7.623546,0.635571,-4.490799,4.174089],[-1.414089,-5.774375,5.052499,8.480486,-7.569773,-7.899329,1.509150,-9.012985,-9.048363,5.715048,0.771528,8.175118,-5.150222,6.407087,1.434981,7.150102,1.870757,4.269329,-3.680723,5.347095],[-7.142245,7.801754,-2.221934,9.219498,8.407865,1.355976,7.527458,5.021423,6.652217,6.047832,6.675708,-2.920573,-2.317073,-5.722839,9.603647,7.451319,3.977160,3.265568,-2.495637,-8.498082],[-2.386838,-2.092492,-0.607597,1.247024,2.114650,5.554429,-9.969767,8.867281,9.086737,2.133994,7.925809,-3.260781,4.239252,-2.517900,9.108758,6.408987,4.653116,0.203372,1.047086,3.061112],[5.140675,-7.615794,6.241209,-1.577920,5.113024,8.948762,-3.929854,2.624726,4.068909,0.600355,-5.849252,-5.081839,3.438747,-1.206594,1.276318,4.762417,-5.261649,-9.811006,0.353024,-1.929754],[-0.862236,5.906216,-6.235383,-1.438585,7.583703,-7.598823,-0.615716,2.877961,-2.165503,-5.217992,2.516218,7.527630,3.468821,7.157417,-8.866030,2.116807,0.861225,-2.112138,2.318163,-1.951038],[-8.005122,0.462221,3.654993,-2.955820,-8.563185,9.744211,-0.896560,7.112379,-9.889316,-7.134288,-9.934062,0.637639,7.366956,5.977266,-0.187331,5.896212,-2.918507,0.958974,1.588098,-5.657247],[1.038288,8.503413,-0.812729,0.535235,-3.400394,4.935615,-6.925275,-7.846159,-0.408226,-1.267104,1.340070,-4.625347,-8.463638,-6.213369,6.035702,1.727385,-6.640019,1.053555,8.953939,-3.892410],[-5.370065,6.728700,-1.628285,-9.753015,3.775790,-3.217698,-0.097707,7.510081,-8.897214,-1.010077,-9.243948,-9.471290,6.976469,4.250466,3.252975,-0.856084,6.422635,-5.581550,2.252119,2.219237],[3.134437,-5.482582,-1.599203,0.289861,2.733827,-7.638052,7.439842,-1.968968,-3.601651,-3.889326,0.807136,-7.771510,-5.968921,7.144317,8.777452,-7.511417,-5.415658,6.977005,-8.846381,3.625402],[-1.788890,8.619430,3.936931,-5.544405,5.823015,2.258273,7.614497,-7.417369,-7.851999,-0.732730,-7.984715,-6.812802,3.142762,0.004465,-3.024784,5.367145,-3.657494,8.521101,-3.880862,-8.784175],[-6.703705,0.381561,5.120830,9.824338,5.366539,3.268526,-9.439609,-8.564651,6.845552,-5.182672,-1.757938,0.786976,-0.629115,-9.665969,-2.125253,6.362218,-4.342659,0.642413,-8.171261,8.739442],[-9.704823,7.959868,2.092097,-2.444313,5.885088,-6.984284,-3.161859,-2.348678,-2.151778,5.798919,2.740784,6.918558,7.438993,2.212408,3.918516,9.939295,-7.072390,2.290167,-1.738476,-8.050646],[-7.875102,-8.896187,-3.198885,6.795078,9.905431,-5.616179,7.193556,2.815212,-1.644983,-1.489483,8.775878,9.782457,-9.914735,1.160634,-0.774866,-8.589917,2.111480,6.565962,-3.266644,-8.197595],[1.054223,-3.198728,4.363170,-0.070602,2.581309,3.343948,-2.099459,-0.648291,1.992962,-3.690745,3.072112,-2.990406,0.141675,4.342129,3.625478,0.874495,-0.452945,5.334542,8.208537,6.447846],[0.847757,-9.534697,9.392576,-1.884151,-9.920696,-0.192356,-2.127806,-0.537466,-8.624453,7.204926,-5.154207,-8.829000,-4.385893,-0.110693,0.639539,-5.175251,-5.770839,8.526091,0.375595,4.041900],[-3.120330,-7.559112,-1.466783,-0.128258,-7.509659,-4.821920,-9.877930,8.631344,7.172220,8.843332,7.117832,6.581587,-6.651186,6.334270,-6.976477,3.462567,-7.352202,0.315810,4.323690,2.247212],[2.521290,-6.029825,-1.127831,1.870950,1.452166,6.767412,-4.086663,-0.797671,0.556796,1.120898,-8.576644,-0.599130,-2.085999,-6.358853,4.228201,5.197026,9.284797,-3.061816,9.942163,3.282316],[-8.404629,2.548603,4.095176,5.600736,2.788104,4.444302,-1.984020,-7.028555,9.044594,-7.740949,-4.298093,-9.469670,4.024887,0.168196,-2.756365,3.194282,0.901100,6.846344,-4.657690,1.415705],[4.280211,-5.586467,-3.175030,-4.913020,6.579720,-1.922484,-6.102416,2.494119,-7.182487,-0.569855,-4.383498,9.442285,-4.508566,-1.662512,-0.064337,-9.405995,-3.098283,3.805141,1.651959,5.444972],[-8.203935,-8.938478,-3.439691,-8.802511,4.457935,5.342585,-2.439827,6.536182,1.086973,5.397928,-8.675638,-1.659672,-1.275841,2.123324,0.173138,-0.806213,1.306190,3.799714,8.574739,-0.408628],[-6.935869,-7.042609,-7.422012,-5.763948,7.056271,3.109601,0.865435,6.797046,8.790317,-9.153337,8.696941,-7.804545,5.113855,-6.814410,1.678959,7.934239,-4.359608,-9.862098,-6.782453,-2.666117],[1.107976,8.796875,3.443631,-2.089350,2.952569,-1.283989,-0.774396,9.583095,-8.489229,-1.047244,-4.246723,7.686845,2.400089,-2.094387,-0.332122,4.368925,-6.289622,7.238120,6.554854,9.504959],[-7.121365,4.686100,-0.182182,-7.842882,-1.163218,6.530435,9.948284,0.535242,-9.607893,-6.078008,7.369508,-5.934636,-6.930739,6.195850,-8.460351,-7.689428,-3.339725,1.105641,7.050118,8.203734],[-5.921587,-9.130326,-3.291729,-3.193571,6.508529,0.212651,-6.822002,3.828215,2.809443,3.146035,2.982722,-1.672981,0.125485,-7.809813,-8.230972,8.024897,-4.328766,-6.389745,5.299760,-6.256593],[5.887119,2.426343,0.507247,-3.167900,-7.241984,-3.882457,4.364475,4.742384,-8.973158,4.454072,-2.011711,8.445414,1.569888,4.669073,-3.931794,5.737255,9.321161,-0.871982,3.892524,-0.475377],[-4.629053,8.957902,8.657347,-7.930161,8.465856,-5.516619,-8.164625,-0.180480,4.917024,2.047367,5.818165,0.620185,8.020964,-7.409633,-4.158813,-3.885312,6.667821,5.925585,1.036545,6.012662],[4.767196,-0.993181,5.980206,3.530760,-1.058207,1.456708,-7.788286,-2.419238,-1.016738,-9.915232,4.780266,8.803449,3.375865,-4.658475,-8.900393,2.687367,0.658989,-6.307895,-4.128571,-2.194536],[-6.028531,8.960678,-9.694263,-5.369004,-0.217301,-9.006222,-4.283320,-1.653047,-4.447904,-7.175263,-3.881673,-6.513200,1.803817,1.403796,3.876588,-2.588095,8.674616,-0.858134,2.091882,-0.687363],[5.947802,-2.237636,-8.811352,2.146394,7.845588,5.183026,4.140771,6.868980,-8.479491,7.814116,-6.070271,3.860774,5.801286,-2.107814,8.733001,-1.908102,2.782684,-3.783688,7.789072,-9.584888],[1.802061,2.531042,7.540268,7.365414,8.157082,7.597975,-9.614568,3.033112,-1.988164,-4.801022,-8.423897,2.075828,4.628263,6.995653,4.606991,9.150107,1.456685,-7.095688,-3.143661,6.714167],[-2.685350,1.388853,8.192905,-8.037516,-1.799995,1.008494,2.358138,-0.777645,-6.782008,8.104977,0.311892,-4.830401,8.175234,-2.777273,-4.465921,7.316855,-3.501211,7.160390,1.319001,-5.353226],[0.934446,-3.211182,-2.730534,7.313102,-5.941801,-9.305168,-2.428633,9.325065,1.835364,2.829153,0.998483,-4.020061,1.633403,2.240366,2.086586,4.362385,-4.869295,6.524861,-4.234510,8.949901],[-4.280075,1.316953,4.661130,-4.765151,-1.698941,-7.367785,0.509223,2.603365,8.448570,2.523865,-2.557371,1.404023,1.705804,2.042462,5.060208,-9.752188,5.283467,-9.478245,-7.040567,4.280175],[-1.419753,-7.736311,4.094691,0.277801,6.841341,8.924370,5.793426,-1.237434,-2.489763,-7.980298,-4.695002,7.686677,-2.630303,-5.764523,-5.961717,4.970320,-8.175207,-6.372045,-4.023782,-8.297855],[0.540909,6.036906,-8.018662,3.419925,-7.155087,-1.808323,-2.599445,-6.422426,-1.117802,-4.311583,-1.086920,8.033438,4.310944,-3.976554,9.260872,6.611547,7.136292,3.161067,-1.637124,-3.660602],[8.087188,-1.801412,-9.157929,-2.529455,1.728169,4.953020,5.796921,-0.522497,1.510021,-7.671564,2.142409,4.344949,-3.210066,-9.458693,8.305891,0.092840,-8.490563,-7.285583,-2.291298,8.207184],[1.334544,-1.140794,0.357364,-2.810312,8.838864,-8.693184,-2.330108,7.999058,-6.169034,-9.493192,-5.985657,-6.558404,3.451230,7.853044,-9.588685,3.844254,-5.003372,-6.142440,4.600096,-2.491227],[2.318755,1.984513,-5.817115,-9.687837,2.379984,-1.962472,8.933027,-2.532869,1.717576,-6.391625,-7.421555,-1.654351,9.239670,-0.316490,1.094731,-8.484236,9.159427,-4.930743,-7.752989,7.522474],[9.491485,-6.849049,-3.346278,0.651208,-4.468082,7.236858,-5.681936,8.012448,-3.811722,-7.251233,-1.845079,-8.377602,-9.038977,9.533574,-8.783853,-6.250111,-9.431708,-9.133853,2.223359,3.589726],[6.034523,-9.363936,-4.131711,-3.914070,-9.834025,-2.146154,0.566701,-9.350418,0.913932,-7.594625,-5.278154,-6.240749,1.454290,-9.339772,-7.933987,8.811399,-7.109649,0.081393,5.376952,-1.200907],[-2.512005,4.658144,3.285179,-2.693092,8.107511,-9.708802,2.063222,8.650274,9.200133,-4.191906,6.215415,-7.222961,1.407705,-9.395636,1.289317,-5.751618,6.039533,9.709949,-4.067134,1.443124],[-2.463779,7.321428,-9.794496,6.420520,-5.654889,-7.346603,2.623890,-6.663965,-1.761201,0.581401,1.704017,-9.128682,9.233803,2.660941,0.143367,-3.981819,1.295916,1.060346,-2.577596,4.492791],[-6.936170,-5.534102,-6.810697,9.097243,9.509482,-4.866942,-9.111935,9.841915,-7.294776,8.668788,7.539845,-9.773501,-3.714697,7.299548,-2.400883,3.613095,-5.319964,-0.400648,-0.844651,1.675388],[-1.542155,-9.856019,-7.632042,0.435391,2.200175,-6.497205,-7.232202,7.221796,6.319214,5.252256,9.452984,-2.683886,-6.506937,0.738888,-9.705939,-3.611953,-2.540511,-5.267242,-3.928317,-1.028875],[-9.922597,-9.208456,1.179856,3.931761,-8.068262,-4.309378,-7.939866,6.319881,7.640243,5.684255,-2.659313,-7.188339,4.902919,0.121707,-0.513342,8.394138,2.753181,7.072024,4.850222,9.941658],[4.330536,6.784666,-2.369159,-9.743364,2.990649,-3.991680,3.789690,1.288160,7.238114,-1.089443,-3.448265,-9.759822,-2.324576,-3.138913,9.764445,3.751536,5.187011,-6.467611,-4.770434,4.528476],[-1.726457,5.125893,-7.131163,-9.189086,3.308625,-3.707136,-2.461576,3.936906,-8.294438,-8.717595,6.473794,1.554553,9.166096,7.861462,-9.259297,2.191843,-8.901129,7.468876,4.683871,-4.102936],[-0.184761,-1.005132,9.585371,2.568315,8.523337,8.830009,-5.787428,6.697818,-4.084352,3.450580,2.984365,-9.886801,2.701128,9.254904,8.795719,5.115136,-9.509826,3.330589,-8.057245,4.090004],[-1.310822,-3.442042,1.524931,-7.973266,-8.101780,9.308005,5.948980,6.092891,3.570972,5.545079,-9.777440,-8.570414,4.861246,9.930359,1.100217,2.763613,1.734932,-6.392525,-6.065758,9.991344],[-6.853158,-8.993752,-1.250091,-7.963094,-0.858099,-7.290756,-1.115682,4.185888,-4.584121,8.439372,-5.555749,-3.119058,2.591556,-7.721190,4.690573,-0.158993,-3.730228,2.687978,0.238973,-0.102127],[-7.418230,-7.844482,-4.124125,-7.206722,-8.386809,-1.201034,-3.598349,1.584307,4.918221,4.345698,1.421014,-5.360012,8.396231,-4.681694,9.936627,-3.123227,5.568364,-8.537534,2.274446,2.071452],[2.689363,-5.853196,-0.265284,8.860550,6.603436,-6.164214,-7.598406,7.667475,9.207541,-4.192303,-4.245379,-2.872129,-8.879711,3.032557,8.998244,4.095057,-0.456217,-2.151605,6.528572,-8.879109],[3.243461,8.845143,1.159289,2.299126,-0.626378,0.975291,-4.109437,3.363329,9.131001,-9.232917,8.817636,4.430943,9.085026,-0.609316,9.422040,-3.123799,6.848037,-0.724602,-5.713739,8.365531],[-3.782612,2.782193,-9.985898,9.974729,-3.602740,-6.376291,0.322888,8.138222,-4.766056,-0.393151,2.878980,-9.184138,-3.227394,6.088162,-2.440740,-7.633352,-5.813002,8.898899,-5.664948,-5.498574],[1.587249,-8.744929,-6.262247,4.261303,7.249028,-1.551562,-8.079776,1.969457,9.108875,5.904244,-4.348952,-0.201768,-7.602020,7.978019,-2.222018,7.778658,5.193938,4.798836,4.192654,-7.933778],[-9.673828,8.229881,7.818505,5.468905,-1.894232,-8.098487,-6.501568,9.471461,-4.982222,4.050036,-8.333513,-3.804273,-5.378511,2.365018,2.173817,-3.435150,-0.522393,-9.323350,4.893351,-8.281856],[5.527383,-8.499791,-2.012263,-3.559125,-0.598825,2.895379,-9.814095,-8.311351,0.451348,-8.534595,9.050204,-7.790687,4.088426,9.886184,5.226470,-4.279750,-3.678509,-3.172088,-3.331226,-2.166035],[7.717849,8.999267,5.280469,-2.586776,3.923498,8.050460,-1.677287,-1.698375,9.651796,-6.614958,8.144446,9.056561,3.567908,-1.631792,-6.307013,-0.099030,8.826734,9.101276,-6.535874,5.954352],[-2.833928,-8.601828,7.210700,-6.143908,6.823757,4.156972,8.395924,-2.874786,-0.134731,-5.885385,2.207656,-1.235322,-2.736877,-1.887043,-5.284183,-8.555398,-5.428457,0.996292,3.080619,-8.556689],[-4.987293,-0.477369,-1.568374,-9.463120,6.286456,3.327619,0.077487,5.824107,7.983186,-4.209250,-6.217250,4.339015,-4.621458,-8.661284,-8.096559,-8.215312,-1.267239,7.954915,4.945293,2.022815],[-3.334022,-6.423847,4.672992,-6.076184,2.052240,-1.351528,7.704093,-0.603016,-1.968595,-9.986548,-0.319899,5.088507,8.483845,7.186238,-4.104422,2.846122,-8.454555,-1.330307,-1.321206,-0.687823],[-5.518998,0.115543,-8.399870,1.140416,-1.109402,-1.774692,-4.754027,0.342989,-0.575955,-2.352235,1.013455,7.165875,4.717173,7.288557,-5.090829,2.725402,-8.447536,5.327448,0.239536,4.406218],[-0.301320,-2.522674,8.283828,-8.214344,-5.710467,-9.792326,-2.300996,3.492800,-7.799022,0.432834,5.247982,1.095530,6.517813,-2.536386,7.424928,-6.729238,4.614596,-4.619364,-9.701037,-5.359325],[1.083739,8.656894,8.641182,-7.875952,4.536644,-3.579780,-1.697448,1.423273,-5.718985,-6.659753,1.012029,3.886827,4.910025,-3.555414,-4.313913,6.304988,9.971816,-6.987100,0.642302,-1.008698],[-9.404196,7.819057,-4.117107,3.784384,6.905499,-6.829337,-4.514991,2.191229,4.059127,-8.735555,5.275596,-4.919800,-9.002643,2.378699,1.605428,-1.623783,-8.376460,-1.249883,-6.110202,-8.067635],[-2.755115,1.400304,-9.554178,-7.174898,-2.427709,-8.366070,-4.488841,-1.859808,1.863111,4.797178,-4.451706,-1.620683,4.451592,8.463136,-7.340405,2.236915,2.891869,-2.843721,-8.414454,3.672581],[4.550468,-5.861070,-4.847982,-1.741271,-0.588552,-2.843896,5.982357,6.441917,-0.356922,7.655032,-7.874067,9.160417,3.737502,-5.167020,-2.209839,-7.112024,5.398724,-5.548884,2.653168,2.422596],[-3.868315,-8.670301,-7.724798,-2.885667,0.639783,-1.444269,1.376160,4.502010,1.783296,-1.619613,1.762425,9.082090,0.351639,2.813294,-2.250116,-2.242188,-9.008985,-0.814298,-2.307405,1.232300],[-8.188370,-2.931851,9.098165,-5.287518,8.300180,4.277142,3.867408,3.589907,-8.659360,-3.671603,8.457025,5.205532,5.403921,-2.661400,-2.579492,2.304740,4.151005,-4.133223,0.966926,1.773900],[0.204805,-5.297702,7.724424,5.284363,-1.249391,-4.352890,-9.906681,1.723887,-7.350869,-5.712758,-8.232044,3.386562,1.760041,-5.160490,9.385347,5.111626,-3.304658,3.308735,7.101027,8.184128],[-7.233990,4.893360,5.621616,1.349762,-4.763361,9.118170,5.806965,5.721546,-4.568628,-5.234709,9.412530,4.587954,5.619471,-5.530809,7.983744,-0.494362,9.769676,5.760752,-3.793468,-2.820351],[-6.417748,7.137337,9.125653,-3.403865,7.906395,7.625589,-9.372903,-1.260248,3.081423,-3.855124,4.335275,3.881914,-9.280103,5.915642,6.511772,0.622716,7.379181,2.083786,0.100805,3.173920],[-3.711313,-1.241377,7.574673,-4.860595,3.149118,0.565620,7.382419,2.297325,4.768873,5.692116,9.605971,-4.603684,5.911772,3.737243,4.501093,8.706347,3.470054,-9.703951,2.873994,5.199938],[9.250679,9.552442,1.789810,-7.221317,9.505027,8.083540,9.318325,-2.775584,-8.706756,5.696572,-5.570474,5.243500,-1.656086,-5.668276,6.214095,-6.437395,-4.463516,2.461590,8.806961,5.783874],[9.459552,8.145077,-8.682406,-8.791560,4.047146,9.566254,-7.912442,2.830637,-4.838509,-9.151993,0.438684,5.529677,-2.177030,-9.205284,-2.656661,7.038988,-8.393400,-4.442983,-0.919512,8.137837],[7.275787,5.790661,-5.686311,-3.812442,-2.300810,-0.362869,-9.931012,1.579224,-0.878761,-1.090303,7.683529,1.968829,-9.502421,6.256866,-1.545265,-0.626030,9.597376,9.189820,-6.897158,-4.071570],[7.232970,-0.532828,-7.107350,-9.551838,9.681512,-7.306840,-8.427983,2.379296,2.637092,5.128083,7.162805,3.246374,6.771782,-4.780562,7.208780,-2.677077,6.980830,-7.036506,0.567285,3.188183],[9.288816,5.348867,2.602563,-7.730421,5.971735,-6.401015,8.196612,5.673503,-4.618131,-0.881769,8.550253,-2.699147,7.341128,-1.359240,-8.611203,-3.483543,1.256935,8.815186,-9.292679,-5.300273],[-7.248256,-5.865518,-6.919603,-9.579272,-4.877198,-6.418755,-1.760463,-6.283279,9.913122,-6.029073,-6.936973,7.457212,-5.978769,-9.169932,-9.085738,8.250110,6.656272,-0.457754,8.341730,5.782846],[0.830672,0.695998,-5.335729,-9.483429,4.043817,9.517825,1.300018,1.908606,-2.767924,-2.427097,-2.440944,6.566051,8.907581,-4.559726,-4.306322,-3.118864,4.897121,9.378631,-7.202831,-0.565489],[-5.475763,8.030078,-5.020150,-2.563183,9.071440,-4.400964,-3.996272,0.353973,1.027108,-7.511443,9.437593,-3.537700,3.554213,0.300229,6.010068,0.931566,2.852747,9.843699,2.257290,-7.736451],[-8.712667,2.751637,-7.143080,-5.918953,-0.297607,-3.185634,-5.781827,-1.134056,-7.687492,4.316472,6.392291,-1.172032,5.378229,1.530584,9.921125,4.615900,-4.436928,-2.234966,-7.164236,-3.999299],[5.681027,-0.884527,1.262077,4.125415,-0.491674,8.610671,1.329848,4.114687,3.447386,-4.219020,-8.354650,-6.945492,-7.441047,-8.980958,-9.319348,6.306925,4.315940,5.629257,-0.821041,-9.902321],[5.660205,9.429614,7.409076,8.058386,4.415187,8.609515,-0.598731,-3.531281,-9.338229,7.653386,8.205267,7.138185,-9.530873,-1.961099,4.053156,-4.521026,-5.166544,-6.558427,-4.576325,3.324325],[9.766530,7.487976,-2.650984,-8.897115,-2.304666,4.178125,-2.090890,-7.263245,3.582787,9.555346,-2.856043,1.025081,6.468558,-5.067344,-2.199519,0.887828,1.879450,5.754931,-9.907367,-7.329492],[4.867696,8.058594,-9.200131,-0.646537,-0.751095,9.016312,6.145193,8.528129,-9.816331,-4.409996,5.838061,-9.810920,9.435314,0.347839,6.392283,-3.646211,9.294828,-7.710698,-0.628499,-6.701844],[-2.096525,6.957702,-9.431665,4.768479,-9.620699,3.083008,8.243081,-2.921570,1.968789,9.299411,-6.797223,7.184898,9.266054,4.323793,5.984952,-8.406098,5.718997,6.399407,-0.973019,-7.080680],[5.204827,6.266595,8.215247,0.972470,3.126376,6.307723,-0.668051,9.254597,-1.577900,3.731807,-7.436214,-9.965983,7.648338,-7.301393,-7.833684,3.775004,-8.195860,-4.934845,-4.321169,3.452640],[-8.702073,1.000710,6.658326,-6.524542,-8.573173,4.459237,5.882325,-2.643989,-4.816887,4.628623,-4.201305,-7.612140,7.453153,-2.278412,-0.596274,0.469724,2.723842,2.470830,0.344266,-0.806554],[-7.086279,2.729942,2.288595,-6.826319,-1.167497,-3.212149,-2.875346,1.626964,-1.277727,-2.212470,6.828461,3.208294,-0.332937,-3.258416,3.148415,4.023720,-2.273574,9.253054,1.010714,2.144102],[7.286350,-6.581708,-5.477783,8.568981,5.202619,3.937063,2.675419,1.893787,-3.715840,-7.478467,7.834921,2.230920,-5.595059,3.078328,-0.750452,3.321527,9.307004,-0.279349,2.386428,-9.500543],[3.960061,-1.977655,-6.140481,-8.654459,3.389314,-1.720746,4.966511,-5.247340,2.560782,8.817162,7.264362,4.590223,-3.354318,-8.027740,-8.298952,-1.444381,9.721061,-2.834977,0.680878,-7.789583],[6.235788,6.626091,-4.834972,-1.405125,1.284710,8.554654,-3.431064,2.790022,-8.711660,1.585363,-8.575254,-5.852274,-3.419835,-0.224347,-3.003684,-8.781727,4.915992,-1.208815,0.617360,0.234038],[-8.092125,6.265048,-2.008167,7.577526,6.359892,0.052730,-8.358493,0.127715,-5.900552,-3.493131,-0.084318,4.765875,-0.998202,6.163428,-9.021256,8.476547,7.066299,-4.605306,4.272426,1.802861]], dtype = "float64")#candidate|4558|(132, 20)|const|float64
call_4557 = relay.TupleGetItem(func_1422_call(relay.reshape(const_4558.astype('float64'), [16, 15, 11]), relay.reshape(const_4558.astype('float32'), [16, 15, 11]), ), 1)
call_4559 = relay.TupleGetItem(func_1426_call(relay.reshape(const_4558.astype('float64'), [16, 15, 11]), relay.reshape(const_4558.astype('float32'), [16, 15, 11]), ), 1)
output = relay.Tuple([call_4549,call_4557,const_4558,])
output2 = relay.Tuple([call_4550,call_4559,const_4558,])
func_4565 = relay.Function([], output)
mod['func_4565'] = func_4565
mod = relay.transform.InferType()(mod)
output = func_4565()
func_4566 = relay.Function([], output)
mutated_mod['func_4566'] = func_4566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_4637 = relay.TupleGetItem(func_1084_call(), 0)
call_4638 = relay.TupleGetItem(func_1085_call(), 0)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_4664 = relay.TupleGetItem(func_601_call(), 0)
call_4665 = relay.TupleGetItem(func_603_call(), 0)
output = relay.Tuple([call_4637,call_4664,])
output2 = relay.Tuple([call_4638,call_4665,])
func_4671 = relay.Function([], output)
mod['func_4671'] = func_4671
mod = relay.transform.InferType()(mod)
mutated_mod['func_4671'] = func_4671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4671_call = mutated_mod.get_global_var('func_4671')
call_4672 = func_4671_call()
output = call_4672
func_4673 = relay.Function([], output)
mutated_mod['func_4673'] = func_4673
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4696 = relay.const([[[-7.588638,-9.091909,3.021863,-2.771514,9.546671,7.867119,4.577429,-1.990309],[-1.099945,9.595686,-4.419960,1.457047,1.556807,-5.999386,-5.331162,-7.960492],[4.243174,7.003989,-8.942852,5.378038,9.036289,2.748282,8.184741,6.273851],[-2.998526,0.381611,5.962472,-9.633213,4.452318,-7.276250,-3.836819,8.494370],[7.825204,4.931296,-9.854886,2.541103,2.358802,-3.800492,-1.310523,-0.138699],[6.530515,-0.433286,-1.291339,1.015268,3.486121,8.664079,-9.051072,1.419560],[8.027309,3.317204,8.104866,0.154266,1.883693,-7.228280,-2.385805,-8.957678],[-9.417253,-7.248534,4.326603,0.628204,6.972505,-6.299724,1.795902,9.008065],[-9.693458,-7.949464,3.412494,6.604474,-3.865658,5.097924,-3.960257,-9.014786],[-6.443262,-1.150288,-2.766537,-9.118076,-8.262424,1.800460,7.126735,2.421250],[9.137175,3.750252,0.790105,7.379976,-0.971861,-4.155598,-1.527820,-3.727882]],[[5.938628,-6.327502,-7.416305,3.890679,3.265705,-4.109613,7.540478,2.109853],[6.548691,-8.070130,7.228682,-7.229619,-0.183526,-0.697347,7.836612,4.420995],[2.474916,-9.701125,-4.616152,9.757032,-4.106590,-5.447567,5.933825,-6.284367],[6.868979,7.134420,-6.395937,-4.155642,5.766960,0.815235,3.570517,9.856207],[-0.368519,-6.092354,-3.044857,6.813363,5.173890,-8.021891,0.536041,-8.927044],[8.981780,3.321008,0.068451,-1.369950,-3.116688,-7.910902,-9.736591,2.730213],[8.512084,-3.228772,6.448617,0.588689,9.467239,7.676740,-8.412467,9.738357],[3.963953,-9.035301,2.839142,9.213158,-9.457850,3.823580,-2.572961,-1.740652],[6.829527,7.923893,-7.697494,9.270750,-4.872717,-8.692570,-2.248977,8.719636],[-0.389532,2.147319,-9.666325,4.195511,-2.153887,-2.820602,3.743257,-2.341313],[7.535328,1.856225,-9.643870,1.404918,9.109138,-3.998960,-4.606055,-4.868232]],[[4.313350,-4.378306,-2.435485,-6.906591,-3.011414,2.033056,6.898122,-2.567369],[7.765522,-8.103365,4.856675,6.313078,2.824131,-8.352983,9.047983,-4.212791],[-7.360295,-0.934086,0.679870,2.001424,4.067752,6.756267,3.109256,8.756942],[-9.253016,-0.600618,-1.218762,-6.539273,9.017973,1.406212,4.063858,9.934357],[-5.551707,3.418694,2.146586,2.551170,9.819987,1.700577,2.374048,-2.334500],[5.540529,0.623362,-6.960464,9.939944,-5.909507,-1.076863,5.503788,-2.363870],[3.827278,2.436509,-9.045328,-0.586567,3.180595,-6.574932,-4.569343,-5.614424],[-6.593201,6.775972,-8.019865,-6.907718,8.373711,-6.344853,5.959211,-5.287313],[-1.993636,5.928299,3.152091,6.945522,1.517092,3.339046,-6.348786,3.767330],[0.327792,7.445385,-1.246472,-9.521939,-5.613203,-0.901200,0.104001,-1.069682],[-3.927138,1.121472,1.706099,-8.084168,-4.313368,0.431654,-9.652093,2.496658]],[[7.018846,3.286452,5.921939,-6.547665,-9.876473,2.840861,0.207032,-2.467395],[3.070537,5.994667,-6.284067,8.404157,7.073024,2.119039,-5.203650,7.746615],[9.391218,0.318410,6.707647,-4.957372,-8.972661,6.554599,9.979945,9.787671],[1.999578,-1.610836,-9.718966,6.694751,-0.526342,8.570115,4.723781,-1.819004],[9.975891,4.004180,7.935957,6.749500,9.582153,-5.598122,-3.982102,2.441162],[-5.886877,7.813656,-8.595910,8.290433,5.634581,7.012698,3.483273,8.870758],[2.582355,2.496750,-1.399336,-4.579861,-1.748835,-2.409919,-3.219492,-3.902054],[4.473745,6.458886,-1.563710,-0.990669,-5.839660,7.093671,-3.366192,-8.637361],[0.047436,-7.046718,-2.844603,-4.089877,8.181465,9.270906,-4.285554,0.830032],[8.029539,5.172310,6.218791,8.772840,5.718086,1.620889,5.690260,9.798142],[-7.932004,-6.808585,-6.955697,2.704215,-1.979082,8.505487,-2.484031,-0.794567]],[[-8.525132,-1.568669,-1.585573,2.236907,-5.977939,0.392175,-7.939831,-6.787286],[-3.280542,-7.154850,6.399616,9.764413,-3.217660,2.444513,7.883841,8.902207],[7.388995,8.436349,2.999915,-1.241466,6.209416,-5.897564,-6.014813,-9.653787],[4.395384,-5.380630,-7.077552,-1.691855,-7.458664,-8.221605,-7.008031,4.072626],[3.873146,9.676588,3.422509,-9.905190,9.457917,6.003605,4.569967,-4.720262],[-9.028313,-7.306685,-4.336861,2.398142,-9.085587,-3.382463,5.345290,-9.882926],[-7.532577,-5.267607,9.989547,1.962597,6.856217,6.333460,-3.065281,7.664635],[-3.002514,-8.765763,9.682356,0.116348,2.883507,-2.828370,-4.072836,2.042667],[-7.058395,-3.375264,-5.356344,-6.205629,-7.499077,-8.897902,9.541426,4.715879],[2.841817,5.088697,-1.776235,-0.033392,-0.721281,-6.701246,-9.794567,-8.941046],[3.429468,-9.538696,-7.351298,5.451140,-8.309159,5.256092,-4.110447,9.972662]],[[-9.102553,-9.980046,-3.503696,-1.158489,7.735695,7.835298,-8.440315,-7.083689],[-1.746025,6.974280,2.748704,-3.588715,8.797337,4.487500,-3.191962,9.676354],[1.169158,7.995014,1.743144,1.954009,8.076601,-8.758257,-4.532046,5.393841],[8.966237,8.040063,-8.555790,8.237957,7.941944,9.229653,1.921775,0.845564],[-8.795246,-3.253011,-3.788024,-6.147175,-8.703620,-6.982607,4.639292,-0.372769],[-6.273166,9.769528,1.143722,-3.432922,9.836273,-5.857198,7.060113,-1.926952],[9.078689,0.449263,-6.088316,1.721002,-2.586704,7.832813,6.787030,-7.059133],[1.232010,-8.726900,-6.516908,4.557089,-1.507800,0.928694,1.457737,3.805597],[-1.940314,0.447234,-4.051430,-3.934436,-5.717546,-7.741409,1.436292,2.481548],[-4.458524,3.099325,3.547050,6.570437,-7.986438,2.360485,-1.724008,-6.027483],[0.442121,9.925134,-7.648938,-5.783794,6.418739,4.053367,7.917566,6.199200]],[[-6.607953,1.137597,5.890231,-7.752669,3.643845,-2.169350,-3.979506,-4.777427],[-6.174825,-6.601674,7.643121,3.123772,8.242231,9.810758,7.924123,3.149068],[6.219976,3.712864,4.061078,8.792390,5.367661,-0.218813,-5.804927,7.177537],[-6.155596,-2.876922,-4.768565,-9.868918,-8.721918,1.037215,-2.735404,6.371553],[5.713982,-5.418937,-0.769729,7.893642,6.143658,-8.236336,-6.873032,-2.892871],[7.242972,4.148869,-5.405829,7.478196,4.809155,2.020080,4.431085,-2.549140],[9.761908,6.340573,-4.698086,-6.608810,-1.191503,9.117957,-4.420692,9.164766],[-9.761378,-8.211287,-8.941514,8.437683,-4.485915,3.426378,-7.616388,-9.149665],[8.740211,4.478366,-2.681172,6.924010,-7.825209,0.704853,2.884097,-6.788057],[3.949118,-4.473753,9.243133,-9.642338,-3.112652,9.443794,7.136001,5.677129],[-8.798719,-1.716570,-0.409858,5.024618,-8.609486,8.242546,-5.702671,-4.244242]],[[-5.937157,2.658218,-6.307657,7.049895,-6.690298,6.990793,-7.054722,-9.612912],[-1.136882,3.474187,-1.049975,2.405357,-1.391718,-9.097250,2.516736,-8.424554],[-8.849281,0.001547,0.251082,1.100961,6.946401,4.807897,2.684573,-7.560431],[-8.053461,-1.521506,6.757761,-9.981126,9.748385,-5.839908,4.476929,-3.841889],[-7.258547,-9.019087,7.526458,9.410560,9.904548,-9.541840,-4.677334,-7.472678],[7.667205,-0.945365,-4.483227,-5.030750,2.087627,-9.159770,7.589637,-5.785646],[-1.191226,-4.972303,2.132588,3.804253,-1.605526,1.253600,-2.559016,-0.880983],[4.776577,-0.496653,0.314960,5.289078,9.134025,1.191700,-5.563323,3.662497],[-5.877867,-2.557719,9.918672,-4.261372,-5.473660,5.472701,8.438986,-1.986394],[-4.593660,4.371001,5.660611,-3.438554,-3.428490,4.805271,-6.716575,-4.477520],[-5.807292,-4.512823,-6.065851,-5.487882,-2.034874,3.620409,0.282735,-9.627956]],[[3.384880,6.357546,-9.119798,0.992088,8.552188,-9.524326,6.905135,-4.177451],[1.550293,-7.258266,-8.064441,-1.488239,-1.200833,-9.088784,2.012103,0.996806],[-4.558855,2.648851,-9.937662,-0.761342,-2.765178,1.777949,5.762544,0.329703],[-8.889412,-5.108299,-2.066047,-2.488521,-8.066335,-1.901601,2.580882,-2.093362],[-1.273186,7.631082,2.046403,-7.754960,-8.840238,8.101696,-4.789420,-1.967532],[-4.909534,7.408252,-1.373484,5.979018,-4.144389,-8.948316,8.577121,-1.069870],[2.710670,2.459740,6.231844,-0.725831,7.021156,8.147680,-6.959967,7.821549],[-9.040800,-2.222023,-8.181794,9.321090,6.797090,-6.592713,3.636606,8.711615],[-5.157800,3.782217,-0.198141,0.808439,2.201479,0.672559,4.832392,7.706460],[7.553832,-5.091392,0.831529,1.856431,7.731751,-0.865486,-2.022086,3.005732],[-4.856549,-6.406038,-9.565376,-6.680863,-8.259503,-1.156498,-5.984905,2.470350]],[[0.020918,9.479660,1.419389,6.855975,4.936597,7.298000,6.359125,-0.418390],[0.230822,7.215830,8.354881,-9.383873,4.103087,5.085048,-5.502307,-3.364702],[-4.451092,-6.632122,-6.377178,-2.429243,6.838342,9.116051,4.320746,-8.456436],[-7.629680,-8.361246,-0.518466,8.285270,8.983442,9.094418,1.882319,7.626723],[-7.229498,3.907166,-0.215722,-4.129502,-2.741121,-5.884733,6.824852,-9.723540],[-0.432902,0.454195,9.512751,5.456114,8.608247,-7.995104,-5.265982,-5.699431],[-4.511082,8.056380,-5.522702,-1.481371,4.770671,-0.512328,-0.422660,-9.446238],[8.019295,3.113936,-8.069267,-7.538876,0.869070,-3.542906,-9.494778,-9.676472],[-4.780544,3.890123,1.037816,4.341829,7.869871,-6.922960,6.093094,-5.226114],[-7.136741,9.238781,-4.251465,9.197778,3.058574,3.646892,-1.537958,-9.227795],[5.593522,6.977830,3.808778,8.047390,-9.340063,-1.925342,-9.516479,9.235749]],[[-9.008682,4.521267,-5.846010,3.008631,-4.342140,9.036355,-2.540753,-8.653881],[-6.958490,4.288960,-9.534636,-3.659792,-6.116703,-5.881295,7.928064,0.847397],[1.303067,9.153174,6.357505,3.195009,7.025434,3.820835,-1.415904,-6.348423],[2.821950,-1.247137,-4.364136,1.755991,-8.068486,-4.125626,1.834245,6.480291],[-6.252060,-3.181830,6.381848,-5.845019,-3.900907,9.173487,6.435663,1.361212],[6.223493,-5.369757,-3.159912,-7.985517,-4.190389,3.822880,-3.329201,-4.320874],[6.106739,2.558675,-6.905208,9.885329,7.955444,0.488635,-9.778291,1.043856],[-3.418597,-5.182581,7.295772,3.893621,1.234033,0.028535,-8.876006,-5.057495],[-8.868258,-2.028033,9.108613,-9.260882,-7.115229,7.402773,-6.216128,-6.170367],[0.404235,-4.926523,4.512666,-7.304161,-9.129109,8.585329,7.647973,-5.487426],[3.832630,-5.616867,-1.729407,7.206264,-5.099800,-1.506400,9.690270,3.109271]]], dtype = "float64")#candidate|4696|(11, 11, 8)|const|float64
uop_4697 = relay.cos(const_4696.astype('float64')) # shape=(11, 11, 8)
func_987_call = mod.get_global_var('func_987')
func_991_call = mutated_mod.get_global_var('func_991')
const_4705 = relay.const([-1.126283,9.960753,-1.219444,3.208987,-6.055514,7.698373,0.927781,-5.787540,-7.769288,-2.122080,2.504667,0.243841,-2.609921,-3.509981,-0.772255,-6.957944,6.841356,6.885205,9.882038,-5.182057,-8.267369,-9.710144,-1.420222,5.985103,2.390070,6.313504,-3.893290,5.679539,-2.906107,4.752058,-9.152112,3.586666,2.579445,7.461628,2.527504,-2.564804,-2.088706,-5.833853,2.633381,1.893632,2.327099,8.655354,2.387120,-6.496604,-0.350281,-7.352066,9.461017,2.648552,-9.841040,-3.134184,-6.239159,9.095645,6.781871,0.359941,4.307079,8.964166,2.866219,9.556795,-7.606197,-0.058608,6.564161,4.350391,-4.624035,7.299929,-8.941098,-8.873223,-4.221058,8.859699,2.372581,-6.793306,7.143640,3.975306,-7.369660,-5.015192,1.759736,-2.016632,6.245615,7.112601,-7.113723,6.756247,-8.893549,1.628714,8.317279,-1.393137,9.460454,-9.630707,2.119235,3.444402,-5.229429,-4.736728,-8.970819,-5.106844,-8.581413,1.162870,-4.694270,7.780585,-4.597637,5.084386,0.961101,3.550840,-1.339207,-0.046221,8.731986,1.350038,0.302492,7.509306,-4.734385,4.635060,-8.511433,9.254971,7.344891,2.654334,7.083518,-4.095855,9.910250,4.025530,0.613722,3.971960,2.082137,-3.527034,-6.541339,-5.874626,4.398631,0.228969,-2.745870,-1.336392,-7.025996,-5.316195,-8.067458,-1.279201,-5.691385,2.558296,8.955370,-2.824296,9.576259,0.592668,5.129115,8.292457,-6.157978,-1.396046], dtype = "float32")#candidate|4705|(140,)|const|float32
call_4704 = relay.TupleGetItem(func_987_call(relay.reshape(const_4705.astype('float32'), [14, 10, 1]), relay.reshape(const_4705.astype('float32'), [14, 10, 1]), ), 1)
call_4706 = relay.TupleGetItem(func_991_call(relay.reshape(const_4705.astype('float32'), [14, 10, 1]), relay.reshape(const_4705.astype('float32'), [14, 10, 1]), ), 1)
func_4439_call = mod.get_global_var('func_4439')
func_4441_call = mutated_mod.get_global_var('func_4441')
const_4717 = relay.const([[-8.843412],[-2.573006],[-3.702648],[-3.561250],[-3.666135],[-4.318814],[0.736821],[6.218814],[-2.682238],[-5.904323],[0.503348],[-5.923072],[-1.887485],[6.908595],[-1.008497],[-8.258284],[-2.527679],[3.910760],[5.972595],[5.129952],[-4.396745],[5.810353],[-9.084569],[-6.972982],[6.499454],[1.839089],[-8.698897],[-7.412586],[-1.795656],[9.584968],[3.195893],[8.480329],[-4.732327],[3.222300],[5.510334],[4.251496],[-2.284300],[1.934873],[-6.296080],[1.635355],[-2.660020],[-7.395359],[-8.377390],[-1.622769],[2.831408],[1.682121],[3.700924],[-6.706980],[5.560136],[2.869543],[-8.078137],[9.192958],[2.743631],[-2.552240],[-7.177314],[-8.813448],[-0.142205],[0.439829],[4.257523],[5.209904],[6.252387],[5.093578],[-3.865982],[6.505692],[8.676510],[-5.697692],[6.137234],[-4.227495],[-2.595737],[-9.841279],[-6.429911],[-8.084796],[-8.439376],[-5.441073],[0.245208],[-8.719220],[-6.354755],[6.528110],[9.152664],[8.771629],[7.496968],[-0.477487],[4.940591],[7.505315],[3.200812],[-5.844858],[-2.671251],[7.218556],[8.537631],[-2.827696],[3.238868],[8.759109],[6.053961],[-4.067400],[8.952541],[6.451130],[4.682463],[-4.593567],[3.587482],[2.998679],[7.304758],[-3.747723],[-9.957343],[-4.644338],[2.591450],[-1.020650],[3.855227],[7.482504],[-7.420415],[2.567331],[8.240160],[-2.424709],[9.652293],[7.236386],[-3.847454],[9.068259],[-3.402403],[-4.862674],[7.395009],[-4.997733],[5.491941],[-0.199184],[8.272261],[7.657907],[9.939321],[7.913301],[-7.083826],[-3.042244],[-8.767890],[-3.696548],[-0.746891],[4.083179],[6.359131],[7.151324],[-2.239120],[-0.884127],[-0.021929],[9.303303],[-8.986720],[4.727136],[1.331318],[-9.207693],[-7.180903],[3.664424],[-2.103387],[2.100132],[-8.642746],[9.820725],[-3.514863],[-9.318592],[1.692099],[9.813193],[3.503277],[7.599768],[0.807940],[-5.380647],[7.857226],[-9.046377],[9.018417],[4.529108],[4.090345],[-8.532946],[5.405585],[-5.973362],[-9.649802],[-2.756471],[8.263205],[7.970786],[-2.166337],[-5.454164],[2.169635],[1.133857],[4.607914],[-0.270821],[0.632083],[-9.247828],[-3.735590],[-6.973165],[-4.846366],[-8.890284],[-7.823858],[-9.179624],[-9.335060],[-3.035660],[-6.296673],[-5.930081],[7.385641],[6.748593],[-7.878367],[4.533296],[2.878754],[-7.808353],[-3.417243],[1.364884],[4.906830],[3.181399],[-0.525059],[7.489408],[8.499380],[-8.685624],[-3.816994],[3.857163],[-8.779587],[-4.925624],[-4.312175],[-8.619021],[2.533748],[-8.740900],[-6.908890],[5.813228],[4.233932],[3.448146],[-8.247865],[-2.416174],[-1.052461],[-3.548939],[2.095271],[4.057212],[-9.019114],[-3.987835],[1.800950],[-8.322046],[-7.127498],[9.481637],[-7.584544],[-4.835403],[6.471832],[2.943751],[7.816246],[-9.068048],[-3.739546],[-4.317476],[-4.435313],[0.390392],[-7.095288],[-4.703393],[3.264927],[-7.339974],[4.653013],[-5.383384],[-8.711740],[6.552814],[-2.806261],[-2.452151],[-8.949056],[2.351819],[7.111401],[-7.648947],[3.785591],[-9.674673],[-2.492246],[-2.618670],[2.438185],[9.965997],[-4.459223],[-3.973641],[-2.840041],[-1.878756],[-1.371429],[-2.739415],[7.849672],[-7.552268],[-4.511615],[0.455926],[-1.179234],[8.995377],[-5.635933],[-9.835336],[-7.426507],[-9.162822],[6.223188],[-2.058884],[-6.825918],[-0.031552],[8.712678],[9.920221],[8.790410],[6.485641],[-5.162647],[1.147517],[-6.484790],[5.508196],[-8.456866],[-8.399464],[1.640930],[8.644099],[4.349049],[7.080120],[7.829814],[-3.637707],[-8.913805],[0.297964],[0.103660],[4.662291],[1.050917],[8.753037],[8.951110],[-7.515301],[-1.086007],[9.631082],[4.850072],[8.800029],[-4.790924],[-1.374520],[-1.596857],[-4.274616],[-8.724972],[-3.507108],[-1.826861],[-7.760237],[2.635285],[3.567223],[-3.865486],[-4.668316],[-7.759439],[6.593762],[1.579667],[-7.824276],[7.225864],[7.728193],[8.678440],[-9.844101],[6.732356],[-8.175932],[9.080065],[-5.891762],[-0.252029],[0.707729],[9.539285],[7.381657],[8.292593],[-0.039753],[3.783136],[-8.349539],[6.773463],[3.897318],[3.056487],[9.885937],[-1.703324],[-9.240082],[-3.596237],[-8.977290],[-0.016735],[9.373263],[-1.387608],[2.419045],[3.638133],[-7.827559],[-2.850188],[9.613045],[-7.969732],[6.385688],[2.714202],[-6.656835],[-1.000433],[2.491260],[7.793147],[9.824465],[2.171406],[-6.081826],[6.370434],[-4.278210],[1.580612],[-7.290486],[2.151019],[6.376250],[-8.370265],[-4.054278],[8.721908],[2.105140],[2.896711],[-4.171378],[6.387235],[0.765012],[3.949066],[-0.555496],[3.437648],[6.490077],[7.385521],[8.394169],[-1.112683],[-9.939678],[5.354481],[-1.993570]], dtype = "float32")#candidate|4717|(384, 1)|const|float32
call_4716 = func_4439_call(relay.reshape(const_4717.astype('float32'), [2, 16, 12]))
call_4718 = func_4439_call(relay.reshape(const_4717.astype('float32'), [2, 16, 12]))
output = relay.Tuple([uop_4697,call_4704,const_4705,call_4716,const_4717,])
output2 = relay.Tuple([uop_4697,call_4706,const_4705,call_4718,const_4717,])
func_4726 = relay.Function([], output)
mod['func_4726'] = func_4726
mod = relay.transform.InferType()(mod)
mutated_mod['func_4726'] = func_4726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4726_call = mutated_mod.get_global_var('func_4726')
call_4727 = func_4726_call()
output = call_4727
func_4728 = relay.Function([], output)
mutated_mod['func_4728'] = func_4728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_4812 = relay.TupleGetItem(func_1097_call(), 0)
call_4813 = relay.TupleGetItem(func_1098_call(), 0)
func_560_call = mod.get_global_var('func_560')
func_562_call = mutated_mod.get_global_var('func_562')
var_4819 = relay.var("var_4819", dtype = "float32", shape = (364,))#candidate|4819|(364,)|var|float32
call_4818 = func_560_call(relay.reshape(var_4819.astype('float32'), [2, 14, 13]))
call_4820 = func_560_call(relay.reshape(var_4819.astype('float32'), [2, 14, 13]))
output = relay.Tuple([call_4812,call_4818,var_4819,])
output2 = relay.Tuple([call_4813,call_4820,var_4819,])
func_4827 = relay.Function([var_4819,], output)
mod['func_4827'] = func_4827
mod = relay.transform.InferType()(mod)
mutated_mod['func_4827'] = func_4827
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4828 = relay.var("var_4828", dtype = "float32", shape = (364,))#candidate|4828|(364,)|var|float32
func_4827_call = mutated_mod.get_global_var('func_4827')
call_4829 = func_4827_call(var_4828)
output = call_4829
func_4830 = relay.Function([var_4828], output)
mutated_mod['func_4830'] = func_4830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1485_call = mod.get_global_var('func_1485')
func_1486_call = mutated_mod.get_global_var('func_1486')
call_4846 = relay.TupleGetItem(func_1485_call(), 0)
call_4847 = relay.TupleGetItem(func_1486_call(), 0)
output = relay.Tuple([call_4846,])
output2 = relay.Tuple([call_4847,])
func_4861 = relay.Function([], output)
mod['func_4861'] = func_4861
mod = relay.transform.InferType()(mod)
mutated_mod['func_4861'] = func_4861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4861_call = mutated_mod.get_global_var('func_4861')
call_4862 = func_4861_call()
output = call_4862
func_4863 = relay.Function([], output)
mutated_mod['func_4863'] = func_4863
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4867 = relay.const([[[5.609008,6.095145,-8.112902,-7.690210,-3.678366,-7.438007,-4.259167,-9.580649,9.330248,-6.929197,2.240490,7.197751,4.417290,5.282802],[-1.901143,-7.352046,0.403080,-2.590120,-8.904122,7.993118,7.298266,9.736202,0.609239,-1.673036,-8.331856,-7.161462,3.990178,8.659262],[-8.495230,5.955310,5.741064,-6.974365,4.320103,-0.745289,9.174603,4.337987,-6.938493,-1.004232,-1.274643,-2.605030,-5.028592,-3.667450],[8.971168,-4.596887,-9.216864,-4.003423,-8.199073,9.565179,2.257018,4.325758,3.699422,8.368492,7.929782,6.190601,-9.454118,-8.530929],[-6.008000,7.783811,-3.848656,9.933562,5.391523,7.158554,-4.895240,1.270531,-1.901374,3.983303,5.051781,8.548973,-7.752824,-2.411411],[7.290533,3.086149,-8.659250,1.396498,9.854018,9.827502,-2.526462,-2.940495,0.335275,-1.667696,-9.136716,-5.649875,-0.056063,-8.380157],[-9.584778,-4.837529,8.129296,-8.061381,-7.733721,-7.517638,-2.256299,-8.198267,-5.973705,-1.948974,-6.157057,-8.491333,-3.647156,2.816909],[-9.032222,5.659881,-6.425002,-4.755470,-9.236121,6.470799,-3.065345,-1.444949,-1.516276,5.162367,4.596038,-8.431218,-7.654709,-6.299768],[5.501961,-1.136497,7.094383,7.272428,3.958382,2.960188,-6.476000,-9.434065,-2.054859,4.232878,7.782214,-1.297932,-3.121142,-1.042348]],[[7.924888,0.857085,-9.834983,-7.638322,-4.049879,-3.275465,-5.233140,1.801726,-3.488831,9.576607,-3.012031,4.731534,-0.882249,-0.604606],[3.881530,9.790441,0.076698,6.405389,-2.905211,6.225977,3.914032,-4.396092,6.154728,-2.210203,5.613730,-8.346054,5.584155,6.893751],[3.831306,-2.154710,2.483557,8.248809,0.066935,-5.188350,0.261845,-1.860617,4.461372,-2.264895,-6.589091,9.486849,-1.893623,6.452408],[8.075925,8.917569,-2.941946,5.526397,-6.260023,-8.821702,-6.012835,4.037123,-5.251717,-0.686411,5.333026,-3.793580,-5.366582,4.145137],[4.134332,-9.767333,-6.339537,-7.667767,5.713268,-2.107883,-7.964783,7.023143,2.620843,-4.955359,-4.732882,-0.400163,3.263199,9.898816],[-5.462666,4.820471,7.184675,-3.397847,7.731320,-0.949813,6.700005,-4.891826,8.092790,-5.995706,2.660211,-9.106327,2.689689,6.101379],[0.878090,-5.718734,6.460125,-0.206464,4.241074,-4.133492,6.264395,-8.541641,3.954317,-7.651533,-1.045592,-6.494058,-1.594963,-8.757060],[5.243900,-4.062722,-5.871675,-1.979028,-8.248782,0.233352,8.844054,6.079389,-0.677376,2.240843,-7.080134,4.015749,-9.647735,-1.984913],[-5.071135,0.439726,-3.137941,5.887605,-1.375002,6.001626,-8.223311,0.820990,-3.050475,-1.611260,-2.951776,0.180642,1.177362,6.451930]],[[-2.032533,-0.676181,-7.814542,-7.080954,-8.236870,-2.067022,2.208677,7.354745,-8.261129,3.746133,3.149477,0.676895,-9.308872,3.589150],[0.498519,4.163433,-2.015988,5.387951,8.234107,-8.628413,9.754833,7.935389,-3.250414,-5.660704,7.456013,5.036413,8.082419,-0.828700],[8.348681,4.159561,-0.849339,-8.406027,7.715437,-3.982734,7.493802,-9.363239,1.549752,3.081691,-8.469732,-4.016787,-0.371265,3.756445],[-7.428827,5.934313,7.462771,1.582124,2.738105,-4.281629,0.157441,-9.905070,0.541469,9.043022,-3.767406,-7.149329,-1.207419,-8.239627],[1.598240,-2.973838,8.696602,2.387510,-4.213947,-2.788747,5.351373,-6.487449,0.438796,1.420528,8.720343,7.304661,-3.953650,7.141348],[-9.465898,1.683572,2.509315,-3.735362,6.671281,8.887614,-6.535311,8.361052,-2.484222,-7.717913,-4.742038,6.817186,-4.390852,7.288340],[-2.763934,7.022643,-7.709696,-1.680628,-6.262823,-3.781637,6.729673,4.611600,-3.960550,9.002163,4.408819,-1.532072,9.432128,2.941020],[7.572501,-4.583759,7.342926,-8.836904,-9.695404,9.078053,5.614567,-4.361699,8.301895,-9.077633,5.992701,8.089711,3.249911,-9.949906],[6.825086,-2.878848,6.069458,-5.092710,-8.441972,-3.248444,-9.597464,9.099858,-3.552003,-1.220367,-1.504970,5.165839,-7.762458,-2.286928]],[[-4.704612,-7.081623,-0.992915,-8.812676,-9.453616,1.947231,-0.004083,5.820170,4.566746,-0.693277,1.927409,-2.807290,-6.296048,8.531600],[-7.041232,-4.210582,-9.032344,-6.366948,-7.410176,-0.825539,3.527225,0.712485,-4.741038,-0.909526,-1.698945,2.666487,9.725368,0.940475],[5.593601,-4.320751,-9.167094,-6.789226,-5.258997,5.145479,-2.955538,6.791672,3.962279,2.998726,0.355521,-5.676139,-6.983525,5.422391],[6.280717,3.269055,2.581478,-8.396149,8.543699,8.754962,9.057178,-7.216101,-8.598364,0.768226,-3.487447,5.286723,6.695592,6.122151],[5.893598,2.485616,7.267826,2.006896,4.967961,-6.637201,2.213652,-8.303801,8.067309,-3.140254,-2.984707,2.267776,-5.442699,-8.182311],[-5.311433,1.924743,3.146695,-6.487813,-6.812677,5.827986,5.012595,-6.153959,5.928148,7.324877,8.008208,0.370319,-8.502587,-1.409613],[7.317963,-2.419667,0.282403,-5.545918,-0.324088,5.942129,-6.937051,-9.677509,4.038341,-3.436816,5.864988,5.350788,7.530617,-9.164044],[7.078473,-1.538355,-7.298634,5.809377,4.696440,-0.722452,-2.749646,-9.801184,-4.523533,1.001398,8.789197,0.822241,7.002326,7.348827],[8.034197,-3.461839,-2.675341,1.224125,5.076787,-7.021362,-7.308325,1.352237,6.414523,-1.018758,-0.190123,0.340252,1.596596,3.135028]],[[0.816155,-8.213728,-1.020718,7.342111,7.340262,3.903422,5.871106,9.712346,-2.634674,8.595017,-5.286022,-9.949747,9.896120,-1.147089],[-7.593822,1.685431,-6.567201,-0.894733,6.672940,-3.187057,-8.055348,2.054984,4.348093,-0.575900,1.066842,3.964349,5.694401,1.947432],[0.742665,6.011113,4.752410,4.549424,-4.363013,-0.911366,-9.617973,1.688541,3.184745,-0.839912,5.981317,-4.860813,-9.512362,2.270440],[9.004636,-8.073578,-6.663702,-3.874584,1.903408,-4.332311,8.884415,2.997403,7.028481,6.352936,3.677017,4.917023,-5.627175,-9.226572],[-5.581060,-4.861941,-2.606029,-4.950127,-2.634224,-7.986202,1.556004,-1.342710,0.150115,-2.737105,-6.454343,1.884084,6.605673,-6.995163],[8.948441,7.728087,-4.793957,5.470517,-2.809875,-3.602075,7.977093,-9.541586,9.809985,3.183660,-0.885113,8.285173,7.926428,1.443216],[6.238660,-9.823874,-1.237841,-7.151985,3.146118,6.314038,-7.037344,4.193210,-7.839142,-1.895455,-3.558302,-4.322805,8.556445,6.515733],[2.123886,3.949072,-5.345331,8.262006,4.614568,-1.799863,4.585131,2.461989,0.294215,9.631053,-3.280570,5.136953,-9.656613,-9.422150],[1.829436,-2.063502,-4.674483,9.642293,-9.622168,6.539446,5.719019,-3.076709,9.856704,-3.813301,-9.566501,-7.839050,8.147585,3.229507]],[[0.694006,7.440768,1.126560,2.952483,9.809608,9.038585,0.542726,-5.262184,-5.763067,-4.396180,-5.895050,-3.226007,-9.009809,3.758998],[-8.049440,1.908429,-4.584025,-5.807312,5.547684,3.523000,-0.516478,-2.682731,3.566843,-8.945553,9.845300,7.477554,8.231672,3.373359],[-7.631049,2.901971,9.229967,1.405292,7.065056,-2.309835,7.204092,-8.766314,-3.020279,-7.172955,0.742077,2.064613,7.728155,-8.790861],[-4.195872,-5.843985,-2.836176,2.546125,0.269107,-7.152998,-8.674325,9.087658,-0.197349,0.649368,-1.051649,5.844052,0.809494,-4.197522],[3.247229,3.865140,-3.638508,9.423364,-4.128223,9.990010,4.039889,-5.670053,-6.410277,5.150693,7.140910,1.990634,-0.215774,7.441806],[9.402050,-0.130379,-7.307782,-3.488950,-6.449815,-3.593522,-9.768153,-5.608120,9.198603,9.371816,-1.320308,-8.986001,4.666011,9.509507],[-7.312867,5.652083,-9.882336,9.444062,-9.779497,-8.090735,7.041025,5.638361,-8.106598,1.752112,-6.853995,9.486128,9.680586,3.500981],[3.833377,7.479854,0.927745,1.081476,-5.189172,6.613705,-0.669355,1.220891,-7.422440,7.490161,-1.984420,-8.760009,7.776870,2.216509],[5.879429,3.113452,7.969802,8.281490,-9.791439,6.694679,6.964352,8.314297,-3.093366,2.541730,9.119077,8.162572,0.962796,-6.219245]],[[5.570869,2.063356,-8.753590,3.577264,1.737188,9.670330,7.098037,0.099808,4.671896,-7.352192,6.440982,-6.361466,-7.823485,7.316178],[6.876797,-7.574407,2.348825,0.667172,-5.031225,-7.057321,7.015276,3.266412,-0.141488,8.890125,0.114312,3.272364,0.144013,6.016481],[1.300426,3.725147,9.070216,6.798311,-9.953848,-7.525900,9.658266,-9.869225,-1.686425,9.585338,-2.067270,-9.547147,-9.287968,2.927171],[7.401294,6.848918,0.633638,0.295262,-4.182612,5.560793,-8.055647,8.818333,-6.927887,-7.958384,-4.081037,0.355070,4.997583,-7.874274],[1.182701,3.175647,1.436027,3.080788,-9.193346,6.355260,4.974247,7.696617,-9.658009,8.858868,-3.025701,-4.408221,3.832817,-1.686733],[1.810359,-4.441075,-2.808048,-7.381883,-5.376911,-1.775732,-0.041329,4.528905,-0.529541,7.219290,-6.135245,-7.941587,7.802499,8.764367],[-6.869432,6.281332,-2.054156,5.897187,6.510827,-4.967034,9.305873,-5.937526,-1.580491,-5.208497,-8.533300,-6.949589,-7.077995,-2.551574],[2.141206,1.678923,0.893442,1.654551,-0.030853,-8.458157,-8.135110,-4.711781,6.947654,-8.904870,-2.464965,-5.571265,-5.706138,8.334598],[6.665729,-6.255227,1.256008,5.902556,-7.060875,8.161202,8.990038,3.215628,-6.200076,7.462953,-9.855788,-3.296941,-8.875332,-9.622361]],[[6.250287,-8.985948,7.351530,0.703246,-8.601222,9.205811,0.405994,7.450861,-5.569964,5.353097,-4.273554,-3.966748,-3.050488,-5.896636],[0.288808,7.545303,-0.032487,-7.726593,0.912820,9.484028,-2.373126,-6.924813,2.754354,-3.841657,-9.983833,-5.818571,-0.618191,-6.774103],[4.973324,-9.587661,4.346456,8.128108,4.893102,0.084336,8.835431,-2.643221,9.104629,-2.463527,-0.348198,-6.976609,-0.912526,-4.024141],[9.444243,4.243551,2.480028,6.916561,2.243029,-8.265949,-5.344639,5.562608,-5.574944,7.177994,0.027209,-8.698765,-4.163534,-2.487931],[-4.947300,-4.016961,5.800311,-5.148346,0.840294,7.677770,7.459742,0.207457,8.750689,3.538991,-1.208093,8.823807,-9.310159,5.886052],[-7.729986,8.863164,-3.485705,-7.467732,6.687954,-0.028808,9.238134,-4.203210,-1.874671,-6.912820,-7.244395,2.266447,5.738743,-4.567129],[9.921266,-4.893596,-1.287771,-4.519430,8.728970,-8.504338,5.296068,0.075184,8.854355,1.531501,7.110276,1.866548,-1.145970,-1.794667],[-8.904892,6.850355,3.165620,1.549432,-5.785178,-8.504425,5.233617,-6.373064,-2.795372,0.294881,8.915733,1.100790,-9.443680,1.419788],[2.269990,-5.978068,-2.132363,9.859193,-1.809715,5.243685,-8.897225,-8.725763,7.039519,0.492842,1.430661,1.511421,3.212179,9.323167]],[[9.755345,-8.111349,6.301449,-7.763779,5.585078,1.757074,9.073682,-8.233990,-6.826968,1.504222,8.266041,9.499005,3.282435,-5.229710],[8.974445,-1.073158,-8.575899,-6.664761,-4.697726,8.149208,-6.298430,6.287456,-2.835409,-3.474555,-8.705166,-6.556528,-7.352246,-8.170676],[-5.417082,-1.039360,1.531072,-4.023623,-3.484442,1.163974,-1.142551,-4.035246,1.358731,-5.238786,3.803541,-0.679692,-5.493196,7.029595],[2.435541,-1.788005,-6.744298,5.434937,5.436712,7.767932,-2.293532,-6.773406,-3.076535,-3.505324,-0.721363,7.731006,0.614152,-4.334041],[-5.049316,-5.074641,5.883272,4.111176,4.183032,7.664859,-0.407615,-7.088821,8.077721,0.450686,8.650413,7.934309,-3.549341,8.254652],[8.332315,6.030051,-9.769423,2.392971,-1.989505,9.349050,8.896641,6.270738,-4.662934,5.276411,-0.186818,6.623322,-6.272593,-6.483940],[8.185256,-1.966964,2.847193,-4.791796,0.819527,1.987928,-4.479278,1.589345,-7.801127,9.184163,9.898888,-1.599270,-4.853749,1.827192],[3.926875,2.562500,-4.806384,6.813465,-2.157676,8.508288,9.064223,1.385081,1.535565,5.016491,9.154671,-9.764873,5.662375,5.627399],[-2.882979,-2.309851,-1.330494,-1.240931,7.217093,-3.611831,0.959655,8.569203,-1.967899,-5.806929,-2.894031,0.070843,8.429214,-8.253320]],[[8.636398,-3.395673,-3.201083,4.194901,-8.614212,0.141164,2.730597,5.440456,5.153600,7.384716,-0.812674,-5.441840,9.578564,-8.274705],[7.647821,-9.972215,-7.416371,6.846033,9.372539,8.870944,-8.414925,-2.113404,-6.382685,0.636186,-7.604221,-7.079649,-1.544252,5.131124],[-1.449082,-7.873043,-1.931719,-5.617443,0.447223,-4.409093,-9.001615,7.145523,-8.693793,-7.072999,2.006166,7.626858,-6.165561,-0.138030],[-6.723278,2.047976,-3.405259,-4.039815,-8.515586,9.478499,-7.077041,-3.034275,-1.720083,-1.949028,4.563986,8.089968,-3.101185,9.697582],[-7.850736,4.531923,6.150436,-8.145576,5.086170,3.035039,2.372892,0.600313,-9.511743,7.857289,7.072998,2.840335,-3.821040,-3.494220],[7.575018,-5.392608,0.219841,-7.529137,-0.566853,-1.396613,-1.524440,2.863662,3.278391,1.207891,-8.906390,-3.654750,-2.686078,2.207631],[-2.790307,5.552331,6.546590,-4.592217,-3.345934,0.484566,8.538149,-1.729765,9.986868,3.953347,-5.215202,-7.415331,7.310769,9.570817],[9.908939,4.964031,-2.018553,2.821509,-0.390824,-5.609314,2.426051,7.439128,-1.695479,-9.116853,6.794486,-7.161268,-6.332515,-0.227135],[2.310276,-0.312771,-2.884701,-4.379460,-6.920240,-4.009664,4.410572,1.044813,4.726278,6.290741,-5.053485,3.357700,-2.320434,-3.114686]],[[5.563403,-6.664768,-1.554781,2.627980,-7.512716,8.678157,6.325351,4.314078,-0.509836,9.928873,0.934604,2.935873,-3.563619,6.018043],[-0.729031,-1.593253,4.392981,-1.429863,7.754433,-4.290688,-9.381639,-9.478558,-1.832207,-7.327775,5.256936,-2.224036,3.480061,-5.505869],[-8.204743,-6.938384,8.066181,-7.860682,1.910390,-5.879391,-9.264239,4.747108,-1.017936,7.479238,0.691804,-8.962883,5.240517,-1.545682],[-7.747204,7.097176,-7.126213,-7.793066,-4.951592,-0.265177,3.307341,-6.787674,-9.107707,-4.264385,8.884667,2.885291,-3.471458,9.181886],[-6.105916,-9.821444,2.739673,8.228557,0.040384,1.630570,4.013012,0.589896,6.235588,-7.608054,4.796010,-4.493312,-0.940953,-8.705027],[2.568410,0.469204,0.311434,1.808801,0.222674,-5.518255,-3.157774,-3.976999,-8.479493,-2.838120,7.961092,1.014712,-6.318811,7.062488],[3.242343,4.396813,-8.357081,-7.109786,-8.564758,-6.638090,-6.827111,-1.101786,-3.754265,-7.273375,-6.915025,-0.642315,-4.626275,1.767070],[-4.348130,1.375740,-0.860822,-2.341614,8.923321,-6.594811,-7.794447,3.261607,0.221260,0.119915,-7.202305,-6.136453,2.254945,-6.728227],[-8.173191,-0.481647,1.443433,-6.169214,-8.423388,-6.733129,6.839324,3.355049,1.323004,1.420835,-2.740142,-8.759616,-5.857101,5.229426]],[[-0.526677,6.382469,1.350379,9.575869,-6.421795,-7.160485,-8.634504,-9.906014,2.784981,-8.846750,4.867855,-7.367785,-5.547497,-5.004231],[7.379741,-6.877114,-8.095211,0.389396,2.456316,-0.326213,-4.659947,-2.692845,3.975408,8.339630,-4.877486,6.997390,6.901296,1.705170],[-7.468694,-6.268531,-3.226504,3.078926,3.948427,-1.049724,5.251924,-2.739078,-6.109647,9.573902,5.831178,-1.720156,-9.376021,5.828943],[4.072082,1.774735,5.864221,-8.200172,6.768184,-0.835887,-9.275817,4.803568,1.168621,5.313785,7.703649,9.507143,5.256935,-6.191362],[4.773739,9.226650,5.962435,-6.197647,9.925027,-2.748674,0.269324,4.385107,1.169862,7.702121,-0.895690,-6.840631,4.549918,-5.771480],[-8.484469,-0.951987,5.453768,-4.803490,1.683932,9.609828,6.803545,7.133701,-2.770256,-7.974591,9.961324,-3.581172,7.856490,8.541315],[-0.420443,3.101247,9.763643,-2.821697,-9.879910,4.701990,1.572037,-6.245298,-2.147798,9.048531,-4.565486,-2.514160,-5.003642,6.839927],[-4.525645,-0.288024,-4.388256,2.857497,-4.036505,-5.731612,-3.915705,-6.904379,-1.530063,2.765863,-3.071533,5.984318,-8.929006,-8.418122],[-9.987160,-9.595361,2.938939,7.106965,9.199939,8.067128,-3.542510,-5.181890,8.583317,9.751963,1.707862,-6.209128,6.200123,-4.298396]],[[5.821362,-2.095547,-5.195779,-0.141087,-6.541856,2.057335,-5.557752,5.608181,1.485107,-7.889759,-0.235623,-8.555119,-4.117084,5.638403],[4.840798,1.588925,-3.852352,-4.223803,1.098099,-0.744713,0.171152,3.285763,-6.167139,-2.278535,-8.733870,-9.162981,-1.503500,-3.964005],[5.989141,5.279199,2.768768,-0.219140,-1.569862,-3.152486,7.284393,7.585759,-5.198064,2.506124,8.581747,-9.705982,-2.153296,-6.153408],[-3.638070,2.677979,-4.706634,-4.939841,4.117394,-2.281396,3.864122,6.033648,2.075622,8.347914,7.959564,7.558712,0.962058,-0.626191],[-5.427398,-1.944161,1.602478,6.844485,-2.184330,1.474947,-5.827648,-3.434298,-7.363674,-0.235724,-3.577120,-0.514720,-0.366924,5.490690],[0.715858,5.264957,-5.099757,-6.558659,0.137500,-2.037804,8.779941,-6.191256,8.781854,-3.215963,-6.554550,5.447447,-5.177286,2.954037],[1.164242,-8.043709,-0.513810,9.054469,-5.028444,7.891413,4.020230,0.040416,8.704459,-9.353261,-1.876898,0.993524,1.612323,-5.674790],[-4.044577,2.107534,-5.684318,-5.186114,8.785279,1.974520,-6.814326,-4.797022,-2.755146,-6.325210,8.932984,-8.236292,3.360706,-8.986114],[8.420001,3.087784,-3.823210,3.629400,-2.966418,-0.323321,1.393198,5.097725,-9.416531,6.710944,-0.454291,-7.806987,-9.495002,8.915547]],[[-2.082422,7.395091,-7.443884,8.587611,1.591910,8.426076,0.891880,0.303459,-2.158618,-5.886865,-4.313448,6.514678,0.607515,-3.323067],[2.445205,-2.784397,-4.925822,6.966360,-2.880958,7.438224,8.060806,4.284058,-7.013688,-7.009293,-1.633878,2.899684,-7.343204,4.621865],[2.302183,-8.325572,2.976817,-3.821449,-6.619567,9.773919,9.222918,-9.054700,2.159275,9.479242,-3.365118,-0.374727,-5.298278,-0.121507],[1.744830,-7.971051,7.278496,3.990366,6.513532,-9.197640,2.201451,-1.897420,4.922478,5.626924,9.348691,-9.153006,-0.341919,-0.102735],[0.804101,-0.205219,-3.107046,7.993944,4.616952,-3.445281,-5.759378,-5.948601,-5.000073,-3.701713,4.845556,7.413426,-4.324579,-8.057093],[-6.547654,6.065675,2.672176,-6.528550,0.254725,-2.501398,-5.243108,5.685457,9.276968,-1.309759,5.552547,3.908046,1.612334,4.010700],[2.947464,-9.717640,-6.215433,3.899710,1.050513,4.009779,9.130109,0.359382,-0.073530,-8.358134,-1.130575,-5.397903,-8.231585,-7.007605],[-8.086941,9.054171,-5.968176,6.232340,-6.299447,-1.759533,0.744295,-2.738978,5.095964,-5.231529,-2.902758,-9.483872,-2.996720,-7.827078],[-7.795884,-3.901722,-1.680352,-8.712202,5.100474,1.070594,-9.280774,-8.994159,5.512726,-2.812140,-7.271639,3.600327,-7.284529,-8.096648]],[[-6.081757,7.830594,0.120832,6.231420,3.288443,-8.631964,5.946144,-4.009921,-7.787070,0.633896,9.029172,-2.523872,5.508561,1.195552],[7.624152,-5.926396,-5.716887,4.137112,0.324444,-2.413981,-2.723976,3.649967,-8.268653,-6.588270,-6.138769,6.198693,5.427177,-4.701418],[3.285748,-8.831501,8.228504,-8.960018,-6.552533,3.315050,-6.575707,6.307102,6.641311,-1.301374,-4.101803,-6.303045,4.298218,8.429262],[8.222252,7.688419,5.786773,-3.217655,-9.915559,-0.596442,-7.225925,-7.188322,8.911256,7.142252,-2.782250,6.312396,-9.117331,-4.263120],[4.659720,3.744638,4.549654,9.507457,-9.639091,1.769451,-5.072667,-2.919411,5.215384,7.528303,-7.495607,5.182381,-9.048016,8.469664],[-6.484297,-8.499119,1.075377,2.691253,-4.019179,9.595953,-8.116131,8.646338,1.537669,6.233969,-2.332020,8.712989,1.655221,-3.253284],[9.822468,5.098871,4.580897,5.385814,8.801815,9.657722,3.341523,-6.016451,2.247872,-3.687638,3.491302,2.908442,-0.286464,-8.685847],[-7.604928,-6.827047,4.127485,1.632277,5.827048,2.963302,8.884222,1.641041,-9.574974,-0.195902,0.911753,-1.363978,-5.325444,6.943286],[-3.121340,1.960249,-9.563761,1.783529,1.243692,-1.983773,3.406833,7.545805,-8.472871,-9.142828,-9.022845,-1.937176,7.693628,4.670046]],[[-7.321409,4.040296,-2.881850,4.205161,-5.245778,-4.944890,-3.147588,-0.285535,5.185012,-8.361621,-6.948702,-4.143992,-0.884134,3.388558],[0.422137,3.371577,7.934848,-9.414912,8.004819,-2.366181,-8.409799,3.437559,1.767239,2.293268,3.599319,-7.689683,-5.797348,7.371969],[4.433677,-2.960555,5.800911,-8.763194,-2.249826,-1.854545,2.725013,5.028916,-8.109303,-4.594327,3.125421,-6.602497,9.207958,-5.854117],[9.488001,-4.532552,-7.620939,6.392395,1.397569,-8.952390,-1.425833,2.223471,4.145643,-4.795894,-7.965173,0.100391,-0.677692,-2.311683],[-1.567323,2.580210,-3.156744,-5.658581,-9.096626,-4.273790,-8.010636,-3.392007,-4.674603,-9.685571,-3.508410,2.108881,0.668146,-4.724998],[-2.009752,3.578010,-9.211969,-7.805376,3.669449,5.785427,-8.528504,4.571529,4.257329,5.024435,2.411548,1.239983,-2.373814,-3.845033],[-5.219744,0.253751,-6.878432,2.313449,6.062092,9.981633,4.840683,3.806633,0.228094,-8.134818,-0.333827,-3.896992,6.230594,0.373797],[-6.847976,7.207308,8.693019,1.961387,6.112566,-0.781350,-2.299870,8.864034,-3.221015,7.580662,7.170370,-3.171203,6.655500,-1.146807],[7.729379,1.314948,1.141650,-2.488529,7.844504,-0.209779,-0.431711,-7.778628,5.908742,-8.151259,-3.978391,4.155061,4.180116,7.727973]]], dtype = "float32")#candidate|4867|(16, 9, 14)|const|float32
var_4868 = relay.var("var_4868", dtype = "float32", shape = (16, 9, 14))#candidate|4868|(16, 9, 14)|var|float32
bop_4869 = relay.floor_divide(const_4867.astype('float32'), relay.reshape(var_4868.astype('float32'), relay.shape_of(const_4867))) # shape=(16, 9, 14)
uop_4873 = relay.acos(var_4868.astype('float32')) # shape=(16, 9, 14)
output = relay.Tuple([bop_4869,uop_4873,])
output2 = relay.Tuple([bop_4869,uop_4873,])
func_4879 = relay.Function([var_4868,], output)
mod['func_4879'] = func_4879
mod = relay.transform.InferType()(mod)
var_4880 = relay.var("var_4880", dtype = "float32", shape = (16, 9, 14))#candidate|4880|(16, 9, 14)|var|float32
output = func_4879(var_4880)
func_4881 = relay.Function([var_4880], output)
mutated_mod['func_4881'] = func_4881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2083_call = mod.get_global_var('func_2083')
func_2085_call = mutated_mod.get_global_var('func_2085')
call_4907 = relay.TupleGetItem(func_2083_call(), 1)
call_4908 = relay.TupleGetItem(func_2085_call(), 1)
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
const_4922 = relay.const([[10,10,-4,2,-2,-3,4,-2],[-5,5,6,4,-9,5,8,9]], dtype = "uint64")#candidate|4922|(2, 8)|const|uint64
call_4921 = relay.TupleGetItem(func_107_call(relay.reshape(call_4907.astype('uint64'), []), relay.reshape(const_4922.astype('uint64'), [1, 16]), ), 0)
call_4923 = relay.TupleGetItem(func_111_call(relay.reshape(call_4907.astype('uint64'), []), relay.reshape(const_4922.astype('uint64'), [1, 16]), ), 0)
uop_4930 = relay.log2(const_4922.astype('float32')) # shape=(2, 8)
func_2970_call = mod.get_global_var('func_2970')
func_2973_call = mutated_mod.get_global_var('func_2973')
var_4967 = relay.var("var_4967", dtype = "uint64", shape = (704,))#candidate|4967|(704,)|var|uint64
call_4966 = func_2970_call(relay.reshape(var_4967.astype('uint64'), [4, 11, 16]))
call_4968 = func_2970_call(relay.reshape(var_4967.astype('uint64'), [4, 11, 16]))
output = relay.Tuple([call_4907,call_4921,uop_4930,call_4966,var_4967,])
output2 = relay.Tuple([call_4908,call_4923,uop_4930,call_4968,var_4967,])
func_4974 = relay.Function([var_4967,], output)
mod['func_4974'] = func_4974
mod = relay.transform.InferType()(mod)
mutated_mod['func_4974'] = func_4974
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4975 = relay.var("var_4975", dtype = "uint64", shape = (704,))#candidate|4975|(704,)|var|uint64
func_4974_call = mutated_mod.get_global_var('func_4974')
call_4976 = func_4974_call(var_4975)
output = call_4976
func_4977 = relay.Function([var_4975], output)
mutated_mod['func_4977'] = func_4977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2449_call = mod.get_global_var('func_2449')
func_2451_call = mutated_mod.get_global_var('func_2451')
call_5016 = relay.TupleGetItem(func_2449_call(), 0)
call_5017 = relay.TupleGetItem(func_2451_call(), 0)
output = call_5016
output2 = call_5017
func_5018 = relay.Function([], output)
mod['func_5018'] = func_5018
mod = relay.transform.InferType()(mod)
output = func_5018()
func_5019 = relay.Function([], output)
mutated_mod['func_5019'] = func_5019
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5089 = relay.var("var_5089", dtype = "float64", shape = (8, 1, 4))#candidate|5089|(8, 1, 4)|var|float64
uop_5090 = relay.asin(var_5089.astype('float64')) # shape=(8, 1, 4)
bop_5096 = relay.bitwise_or(uop_5090.astype('uint8'), relay.reshape(var_5089.astype('uint8'), relay.shape_of(uop_5090))) # shape=(8, 1, 4)
bop_5103 = relay.right_shift(uop_5090.astype('uint32'), relay.reshape(bop_5096.astype('uint32'), relay.shape_of(uop_5090))) # shape=(8, 1, 4)
uop_5116 = relay.log(bop_5103.astype('float32')) # shape=(8, 1, 4)
func_2186_call = mod.get_global_var('func_2186')
func_2187_call = mutated_mod.get_global_var('func_2187')
call_5129 = relay.TupleGetItem(func_2186_call(), 1)
call_5130 = relay.TupleGetItem(func_2187_call(), 1)
uop_5140 = relay.atan(var_5089.astype('float64')) # shape=(8, 1, 4)
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
call_5142 = relay.TupleGetItem(func_3057_call(), 0)
call_5143 = relay.TupleGetItem(func_3059_call(), 0)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_5144 = relay.TupleGetItem(func_1097_call(), 0)
call_5145 = relay.TupleGetItem(func_1098_call(), 0)
output = relay.Tuple([uop_5116,call_5129,uop_5140,call_5142,call_5144,])
output2 = relay.Tuple([uop_5116,call_5130,uop_5140,call_5143,call_5145,])
func_5146 = relay.Function([var_5089,], output)
mod['func_5146'] = func_5146
mod = relay.transform.InferType()(mod)
mutated_mod['func_5146'] = func_5146
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5147 = relay.var("var_5147", dtype = "float64", shape = (8, 1, 4))#candidate|5147|(8, 1, 4)|var|float64
func_5146_call = mutated_mod.get_global_var('func_5146')
call_5148 = func_5146_call(var_5147)
output = call_5148
func_5149 = relay.Function([var_5147], output)
mutated_mod['func_5149'] = func_5149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_5160 = func_1116_call()
call_5161 = func_1116_call()
output = relay.Tuple([call_5160,])
output2 = relay.Tuple([call_5161,])
func_5190 = relay.Function([], output)
mod['func_5190'] = func_5190
mod = relay.transform.InferType()(mod)
output = func_5190()
func_5191 = relay.Function([], output)
mutated_mod['func_5191'] = func_5191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1793_call = mod.get_global_var('func_1793')
func_1795_call = mutated_mod.get_global_var('func_1795')
call_5192 = relay.TupleGetItem(func_1793_call(), 1)
call_5193 = relay.TupleGetItem(func_1795_call(), 1)
output = relay.Tuple([call_5192,])
output2 = relay.Tuple([call_5193,])
func_5237 = relay.Function([], output)
mod['func_5237'] = func_5237
mod = relay.transform.InferType()(mod)
mutated_mod['func_5237'] = func_5237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5237_call = mutated_mod.get_global_var('func_5237')
call_5238 = func_5237_call()
output = call_5238
func_5239 = relay.Function([], output)
mutated_mod['func_5239'] = func_5239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4861_call = mod.get_global_var('func_4861')
func_4863_call = mutated_mod.get_global_var('func_4863')
call_5258 = relay.TupleGetItem(func_4861_call(), 0)
call_5259 = relay.TupleGetItem(func_4863_call(), 0)
output = call_5258
output2 = call_5259
func_5268 = relay.Function([], output)
mod['func_5268'] = func_5268
mod = relay.transform.InferType()(mod)
mutated_mod['func_5268'] = func_5268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mutated_mod.get_global_var('func_5268')
call_5269 = func_5268_call()
output = call_5269
func_5270 = relay.Function([], output)
mutated_mod['func_5270'] = func_5270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2897_call = mod.get_global_var('func_2897')
func_2898_call = mutated_mod.get_global_var('func_2898')
call_5278 = relay.TupleGetItem(func_2897_call(), 3)
call_5279 = relay.TupleGetItem(func_2898_call(), 3)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_5291 = func_1957_call()
call_5292 = func_1957_call()
var_5302 = relay.var("var_5302", dtype = "float32", shape = (10, 140))#candidate|5302|(10, 140)|var|float32
bop_5303 = relay.floor_divide(call_5278.astype('float32'), var_5302.astype('float32')) # shape=(10, 140)
bop_5306 = relay.floor_divide(call_5279.astype('float32'), var_5302.astype('float32')) # shape=(10, 140)
uop_5323 = relay.erf(call_5278.astype('float64')) # shape=(1, 140)
uop_5325 = relay.erf(call_5279.astype('float64')) # shape=(1, 140)
output = relay.Tuple([call_5291,bop_5303,uop_5323,])
output2 = relay.Tuple([call_5292,bop_5306,uop_5325,])
func_5332 = relay.Function([var_5302,], output)
mod['func_5332'] = func_5332
mod = relay.transform.InferType()(mod)
var_5333 = relay.var("var_5333", dtype = "float32", shape = (10, 140))#candidate|5333|(10, 140)|var|float32
output = func_5332(var_5333)
func_5334 = relay.Function([var_5333], output)
mutated_mod['func_5334'] = func_5334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_5378 = relay.TupleGetItem(func_601_call(), 0)
call_5379 = relay.TupleGetItem(func_603_call(), 0)
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_5383 = relay.TupleGetItem(func_5190_call(), 0)
call_5384 = relay.TupleGetItem(func_5191_call(), 0)
output = relay.Tuple([call_5378,call_5383,])
output2 = relay.Tuple([call_5379,call_5384,])
func_5418 = relay.Function([], output)
mod['func_5418'] = func_5418
mod = relay.transform.InferType()(mod)
mutated_mod['func_5418'] = func_5418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5418_call = mutated_mod.get_global_var('func_5418')
call_5419 = func_5418_call()
output = call_5419
func_5420 = relay.Function([], output)
mutated_mod['func_5420'] = func_5420
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5537 = relay.var("var_5537", dtype = "float32", shape = (9, 1, 4))#candidate|5537|(9, 1, 4)|var|float32
uop_5538 = relay.atan(var_5537.astype('float32')) # shape=(9, 1, 4)
func_4565_call = mod.get_global_var('func_4565')
func_4566_call = mutated_mod.get_global_var('func_4566')
call_5543 = relay.TupleGetItem(func_4565_call(), 1)
call_5544 = relay.TupleGetItem(func_4566_call(), 1)
output = relay.Tuple([uop_5538,call_5543,])
output2 = relay.Tuple([uop_5538,call_5544,])
func_5547 = relay.Function([var_5537,], output)
mod['func_5547'] = func_5547
mod = relay.transform.InferType()(mod)
mutated_mod['func_5547'] = func_5547
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5548 = relay.var("var_5548", dtype = "float32", shape = (9, 1, 4))#candidate|5548|(9, 1, 4)|var|float32
func_5547_call = mutated_mod.get_global_var('func_5547')
call_5549 = func_5547_call(var_5548)
output = call_5549
func_5550 = relay.Function([var_5548], output)
mutated_mod['func_5550'] = func_5550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_5569 = relay.TupleGetItem(func_5190_call(), 0)
call_5570 = relay.TupleGetItem(func_5191_call(), 0)
output = relay.Tuple([call_5569,])
output2 = relay.Tuple([call_5570,])
func_5573 = relay.Function([], output)
mod['func_5573'] = func_5573
mod = relay.transform.InferType()(mod)
output = func_5573()
func_5574 = relay.Function([], output)
mutated_mod['func_5574'] = func_5574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1485_call = mod.get_global_var('func_1485')
func_1486_call = mutated_mod.get_global_var('func_1486')
call_5590 = relay.TupleGetItem(func_1485_call(), 1)
call_5591 = relay.TupleGetItem(func_1486_call(), 1)
func_3563_call = mod.get_global_var('func_3563')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_5600 = relay.TupleGetItem(func_3563_call(), 0)
call_5601 = relay.TupleGetItem(func_3564_call(), 0)
output = relay.Tuple([call_5590,call_5600,])
output2 = relay.Tuple([call_5591,call_5601,])
func_5607 = relay.Function([], output)
mod['func_5607'] = func_5607
mod = relay.transform.InferType()(mod)
output = func_5607()
func_5608 = relay.Function([], output)
mutated_mod['func_5608'] = func_5608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3115_call = mod.get_global_var('func_3115')
func_3116_call = mutated_mod.get_global_var('func_3116')
call_5620 = func_3115_call()
call_5621 = func_3115_call()
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_5634 = relay.TupleGetItem(func_3161_call(), 0)
call_5635 = relay.TupleGetItem(func_3162_call(), 0)
func_3734_call = mod.get_global_var('func_3734')
func_3736_call = mutated_mod.get_global_var('func_3736')
call_5640 = relay.TupleGetItem(func_3734_call(), 0)
call_5641 = relay.TupleGetItem(func_3736_call(), 0)
func_3257_call = mod.get_global_var('func_3257')
func_3260_call = mutated_mod.get_global_var('func_3260')
const_5646 = relay.const([-4.470377,-7.718165,1.521648,-3.012838,3.412666,-0.986799,-8.469274,-7.017821,4.809684,-3.328551,-6.539398,6.663834,7.919881,-3.959604,-8.235483,3.715983,-6.987621,0.042870,-7.277777,2.571070,7.522356,9.558820,2.178188,4.005093,9.222102,3.632348,-7.924311,-0.965622,-6.160988,-3.188448,-1.090036,7.042088,5.561355,1.091235,-7.223730,-4.586141,-9.405509,9.590424,1.724967,1.301038,8.005389,-1.421998,8.652854,7.033066,7.193872,-4.264140,-9.163590,-5.845891,-3.032661,2.572709,-2.224295,8.564086,-9.846227,3.502472,1.612210,-1.835694,6.233535,-1.230228,0.952677,-7.436794,9.684601,-7.484508,-3.298983,-0.060359,-5.200969,9.740985,0.305945,-9.935882,2.503004,9.181499,-4.473493,3.043287,-3.642485,-2.122439,-6.038728,-2.520553,1.169472,7.821023,8.580942,-9.854363,4.751167,5.259422,-3.653286,-5.278991,4.782346,6.909888,6.158960,8.077180,-8.257135,2.261861,-1.454422,2.812221,9.955155,3.038685,-4.279856,-5.047767,6.643002,-4.005907,7.478202,3.055531,-4.309075,-5.800381,-6.701490,8.352533,5.328259,0.097097,-8.124677,8.088821,8.153547,-5.901587,5.115916,8.469959,-1.149271,-5.902987,2.774079,-7.542806,-9.723952,1.657247,-7.295494,-3.014355,-5.976658,2.108128,-1.114636,-2.340242,6.119837,7.175580,6.781422,2.155311,-9.583960,-0.440264,-2.970300,0.651875,6.871307,9.361141,6.829012,-7.295921,7.577795,-3.609604,-5.405763,3.389496,4.715112,-7.718166,3.260277,4.458998,-6.624373,2.974489,-2.292943,8.149300,-3.613728,-6.753342,-3.897646,8.501672,-6.629434,0.807577,-9.740749,6.271261,1.143163,-8.943796,7.209085,-4.619092,7.892848,-3.090129,-0.432760,-2.343613,-2.328824,-3.403275,2.672450,-9.287740,1.666240,-4.503849,-3.941808,-3.389353,-9.509729,7.942306,-2.625487,0.375103,2.781233,6.601826,8.028576,-2.275239,-3.932850,1.948975,-3.394478,-2.707372,9.582145,5.601982,-7.176856,-7.616629,9.619201,-3.358165,2.632435,3.890525,-9.034708,6.897809,-0.993807,3.965527,-9.115364,-2.896103,3.752515,1.060276,-2.689906,-5.006768,-6.620409,9.182622,-3.466357,1.793279,9.980960,9.546545,0.573769,0.597011,-1.139201,2.965796,7.573172,-9.328064,-1.985012,-4.907008,-7.548748,9.084193,2.043488,-4.352042,-5.763379,5.205510,5.060742,1.992986,5.718591,-2.307848,-3.998932,8.210062,-8.181901,-6.446111,4.288824,5.060540,4.776684,-9.829932,7.057718,3.021536,-8.518505,7.147061,8.586153,-1.867978,3.562867,-2.828739,-1.700311,-8.174069,3.698061,2.292104,5.394504,2.810897,8.361740,1.509334,-7.369722,6.760234,7.814764,-6.738528,0.770663,-9.713434,-6.888919,-2.150078,-5.782809,5.837359,4.758262,-9.702231,7.280152,-6.870155,2.253635,6.781997,-9.470438,-1.541172,6.025801,-0.211926,2.297090,3.598380,4.432923,5.353921,-9.079699,-1.258528,4.673184,-0.009533,-2.034207,-0.273669,-7.866918,1.906303,-9.938527,5.900850,0.041395,-0.158733,-3.192197,-9.946010,-4.881727,5.169792,-1.639537,-3.096920,-8.570636,-0.180237,2.869702,-6.162708,-5.771238,-0.323948,4.910645,-9.380211,7.382534,3.142639,-7.567580,-3.898826,0.816635,-4.623390,7.223695,-6.402109,1.160738,-5.344114,0.946694,0.431735,-7.127016,-0.558216,3.145568,-0.649339,3.451093,-7.865787,9.580598,-3.240655,-9.582201,-8.682819,-2.527648,0.671495,5.361422,-0.478938,-7.303482,-8.671750,-1.704524,-8.731784,7.727691,-4.818660,-3.374710,8.407013,5.919633,7.753125,-6.542714,6.141687,-3.144341,-2.796422,-0.261382,-9.839694,-1.018825,-7.827194,2.026297,-4.966040,2.085764,3.201180,9.131544,-7.377344,6.012393,-7.646296,9.665602,-0.952838,-3.307995,-0.668026,8.079675,8.389725,1.408320,-7.725271,-5.697424,-0.359894,-3.283710,-8.612267,-2.500181,-0.879045,-4.636616,7.132431,9.234388,5.277056,-4.126520,-1.096013,-4.322458,-5.953202,2.840642,-3.133748,6.575727,-2.388992,-3.905740,-5.343887,1.506659,-6.095028,5.533533,1.525076,1.022968,3.308509,-3.648005,-0.680956,2.800113,9.838641,4.364577,3.605130,-6.135989,-3.743356,-5.729736,2.356398,-6.018796,7.141722,1.946561,-5.658467,2.891020,-2.483227,5.018663,-2.385450,4.177071,-6.175242,6.025507,-3.897840,3.189160,-5.185866,0.912093,9.544103,-6.946879,6.075203,6.996036,-3.094668,1.288377,4.822220,3.821818,-5.053804,7.006138,-5.196169,-4.540282,-1.125742,2.076241,2.375760,-3.674163,-5.555458,4.380894,-8.564645,7.781672,4.307696,4.770782,-0.955363,-6.962699,-9.408895,6.633595,-1.111287,0.759455,8.440194,2.052955,4.362941,7.546468,-7.336061,7.134343,2.429029,-1.236594,-9.281994,9.355889,-4.456706,3.222586,4.209849,0.058714,-8.862427,-4.776873,-5.169799,-2.267693,3.371301,9.043951,-3.538912,-8.230344,-8.829052,-6.173574,4.461376,1.204464,9.163328,-0.847992,3.479292,-7.049012,-3.012051,3.000796,-1.738981,-3.383756,7.790782,-0.376384,-9.200681,8.097772,1.969077,2.588618,-9.026180,-7.476775,1.139938,-7.793403,7.381778,-4.725091,-2.365675,-9.088456,1.635790,-2.180655,-9.757034,-8.008709,-2.497582,6.047972,4.236471,-5.380930,3.837540,4.822580,0.568678,1.787111,-7.010572,-6.868622,9.395741,-7.732208,2.664249,0.619216,5.675900,-2.047161,-1.541022,6.714066,1.913939,3.387087,-0.542700,9.184197,-2.263976,-0.647372,4.477894,2.862705,6.736766,9.518459,1.544824,8.993885,5.146569,-6.908122,3.552806,7.711277,1.753609,-4.590826,-0.150544,5.296882,-7.483402,0.904173,-7.548135,8.424519,-7.773157,-5.843897,0.906813,-2.309546,1.744188,-7.878763,-2.573703,7.254192,-9.174736,-3.665427,-2.615721,-9.490989,9.028971,-8.933583,-9.375802,-6.284790,-9.289324,-5.804977,-3.622799,-3.786931,8.734724,-0.530261,5.686534,5.832567,2.325518,-8.459662,1.211691,3.008113,-9.484988,-0.143522,9.984337,-3.858423,2.902356,6.828753,3.483983,-0.213960,3.160533,7.602703,-8.554435,-4.853944,-7.805056,2.028737,8.470022,-1.355492,-7.601960,5.251389,8.289122,-9.878175,-3.512407,-9.778890,2.856505,5.687560,-0.991040,8.580773,0.396526,-6.553850,-4.791769,-2.464837,-2.789296,-4.663507,3.363474,-6.240963,7.785091,-9.794487,4.411422,0.656048,1.793696,3.929177,1.272773,-4.796440,-8.018581,-0.411939,7.221849,9.510209,-6.281298,-8.442818,6.625764,-5.750337,5.089298,-3.753899,-3.681675,-4.086443,-9.070226,6.595483,-5.106657,0.992012,-9.687762,-0.387988,-8.156634,-2.919500,9.663957,-6.474838,3.307374,7.005229,9.060465,4.196094,0.849601,0.307776,6.755025,-2.630611,5.091580,5.478932,9.550931,6.031309,9.728358,-4.648020,-2.307506,7.398478,-1.288483,4.916152,-2.875745,4.292950,-9.283294,-0.898758,6.214865,2.572948,-4.535813,-3.404851,-5.980286,5.137765,9.012124,-0.065407,-9.425408,-1.632259,-4.813608,7.541974,-8.348920,6.867479,7.983405,2.795285,-0.275503,3.475276,3.375020,-7.368032,9.427334,9.396702,-0.003700,9.966385,7.171697,5.357689,9.673796,-3.476423,7.704471,-3.498632,4.995823,2.005424,-4.166704,-4.203776,-4.033725,-9.468956,-8.337516,2.405109,1.165573,-9.154597,-5.720461,0.428315,-3.138748,4.488266,5.288455,-8.450810,7.296920,-1.199323,7.932472,1.653728,9.528979,3.726033,3.686327,-6.147725,7.423262,9.937786,-0.581295,0.570685,3.978217,-5.829063,-2.061661,2.505959,-1.004327,-7.407585,2.939445,-4.034476,9.051082,-0.190891,-4.467457,5.814944,8.225740,0.078159,3.937893,-2.831888,7.181619,9.666566,-7.126732,-3.194615,-2.815597,-8.034920,-6.325654,4.675932,-1.926173,5.280752,-1.562421,7.296740,9.076856,-5.310442,7.631639,4.661966,7.593285,7.184892,-4.791997,5.432349,-5.666706,-5.554846,-6.071344,-2.264726,9.487369,3.817727,-6.660830,-1.189466,1.376498,6.924594,7.932771,2.899228,3.163261,-6.475623,-8.444762,4.277473,2.628903,-3.152857,0.830374,4.506011,-2.016998,-7.472087,9.562239,-9.459020,6.440913,0.912807,5.187527,-3.615847,7.323704,-0.240106,-0.481250,-1.425094,1.486819,3.292857,6.280581,8.212629,2.519852,8.453086,-1.426701,2.735941,9.989497,8.309122,1.915073,2.827807,-4.740676,0.516791,9.750408,2.194146,-9.026164,2.278485,0.753916,9.800572,6.817932,7.889351,-7.894493,1.124454,1.525228,-4.516059,-2.584417,-8.612406,5.591558,9.436483,6.404585,4.972967,8.257735,-9.372714,-4.527305,8.084525,-6.984772,5.116960,5.385802,-9.936414,0.653643,-4.278076,-3.238474,4.278027,-0.169256,0.757188,0.999773,0.476805,7.946294,4.107781,8.355964,3.870606,1.603819,-7.067641,-9.811174,5.632435,-1.401902,0.295645,-9.501917,-1.871712,-4.893903,8.461817,2.900000,-8.826022,-8.519491,-9.775913,0.040727,6.646421,-1.453174,5.052300,-0.967124,7.732227,-1.270908,3.371244,6.533237,9.909141,6.506690,5.449179,0.552071,-0.332180,7.667408,6.121947,-6.387301,8.185139,9.181533,0.351122,2.085720,-5.332937,-0.228278,7.582591,3.156786,0.297447,5.734574,1.389608,-1.722075,-6.069283,-3.748997,-9.604804,-6.002932,-8.256665,4.692091,3.643167,-8.072963,-5.156939,6.503102,-6.205745,4.116455,-9.893074,-1.532364,6.342835,9.459607,-7.508770,-1.830924,-9.261600,-6.911337,-5.094619,8.016257,-0.691407,8.828509,-9.180374,-8.896057,7.126296,-1.921062,-2.301568,-8.265557,2.028856,8.700054,9.306483,1.198569,-1.779142,-3.807698,7.333927,-9.488329,9.152956,-6.214095,3.719419,-9.061286,-1.164968,-6.953433,8.706731,6.046342,-9.090570,-2.166305,-2.862722,4.317842,3.386561,6.374431,2.806747,6.583627,8.131921,-7.585573,-0.518198,9.859580,6.198747,-5.526959,-3.314780,-9.510988,-7.963432,4.322317,-5.755929,-7.558643,-5.146348,-1.322844,4.485409,4.947457,3.219160,8.451840,-4.877423,3.390483,-9.041102,8.888494,5.322760,0.834728,-4.852600,-0.749473,-5.730326,9.435091,-0.493033,-5.344321,3.963720,-7.471284,-1.863715,-2.930534,-8.754725,-4.439293,4.545276,-6.860352,9.771921,1.905204,-1.991110,-5.223772,-1.339551,9.396511,3.768932,-6.833519,3.493609,-9.262777,1.475820,9.547901,-2.387734,-5.177151,7.520389,-8.071559,3.222517,-1.540689,2.063867,-6.443931,-2.172596,-4.750099,8.259967,-6.114961,9.941337,-0.996412,-3.654672,-1.405391,-5.085156,-2.032072,3.373275,-4.479354,-1.392175,-7.419478,-2.749879,1.368268,6.652795,-8.514738,6.743789,5.144124,8.572518,7.867678,4.896624,-1.611587,-2.638646,9.279489,8.180330,-9.349386,5.621429,4.010114,8.667865,-4.883801,-3.891388,-9.577073,-7.850970,-2.034620,5.277923,1.201809,-8.032005,-5.998885,-0.371215,-0.184257,-4.144119,-8.660874,-5.055196,9.083330,-7.547921,-2.801013,-0.571157,-8.763063,-2.155453,4.890469,-6.842700,0.886341,-8.769369,-7.514393,0.811138,4.962278,3.864143,6.249309,7.081163,-1.826201,6.416155,5.467529,9.803172,-0.720300,-4.373025,8.276622,-0.934683,6.108901,1.608965,4.125440,1.180524,-8.574428,-9.558859,-2.184460,-2.148622,-9.979532,9.104106,8.656423,4.452230,-9.121690,1.721066,1.326862,-2.655154,1.148078,-2.266054,9.846931,0.669329,-8.938535,8.678461,8.662060,9.623348,7.903031,4.583831,8.263519,-2.100194,1.458120,-1.427863,1.493383,0.992975,-9.697892,-7.652607,3.169996,4.382765,0.999238,-6.420579,-6.266728,-2.767906,-0.236346,-8.385215,8.508986,-3.096988,1.094374,4.972922,4.772415,3.648196,-4.505514,4.808913,3.832339,9.839359,-6.823211,1.999525,-3.449919,-8.125226,-4.612238,-5.136535,-0.015852,-0.443789,3.118037,-6.035759,-8.188986,-5.643246,7.199152,6.337430,-0.544821,-0.583334,-1.148675,5.647953,7.879832,-0.611553,7.266432,4.741434,1.889194,5.923997,3.209295,0.464863,5.081082,-0.824439,-2.157319,7.881619,3.495546,5.392603,9.537425,-2.652881,-4.871978,-4.588241,9.297777,7.444159,0.880013,-3.290982,4.975777,2.171702,4.551936,5.088469,0.939262,9.188481,-5.889638,-8.546319,0.589122,3.743413,7.459795,3.159143,5.261125,0.240851,3.733944,-8.629820,-0.978505,8.009455,0.640456,6.811138,4.885150,5.083624,4.974375,-6.692051,-4.725624,-8.373816,1.400467,5.718532,6.207763,-9.986539,-0.005113,8.357561,-7.370222,-4.257041,6.148040,-0.473379,-7.131471,3.136798,6.328726,7.523565,5.058677,-4.167860,2.174500,4.132523,-5.322361,-5.230290,-8.329535,7.791074,-0.317805,1.761577,8.743788,1.220677,6.429226,5.774866,-8.443886,3.872956,6.308956,-4.257598,3.946055,3.491578,5.496483,-9.179978,9.490598,-8.516291,6.573917,7.816922,0.854448,2.791946,0.712602,-4.226287,8.419181,3.514552,0.574359,4.090110,-0.825203,-7.890834,-3.636219,4.780192,8.216894,-3.114663,5.350928,5.271325,-8.723451,-2.141468,-7.186900,2.453701,-7.148251,-6.989140,-3.119124,-0.120726,-0.810598,3.461615,4.010991,-7.512631,-5.013883,6.546951,-0.985949,5.590563,8.911931,7.222037,-0.369555,5.771065,2.563174,-0.763845,-3.854859,-4.497517,6.247959,7.912184,0.770166,6.081834,-0.948539,6.385624,-5.923350,9.689621,-7.155550,2.447387,0.593658,9.260329,-5.243334,4.423279,-0.069232,7.362040,4.781129,-9.614501,-2.100278,-4.151094,8.548288,8.459393,-4.851068,8.112430,1.529610,3.219860,-0.987900,-1.194085,-2.528285,6.538193,8.004913,6.723326,8.175315,7.745842,3.503365,0.114493,-5.308408,-8.803879,0.518635,8.755037,-7.981400,-5.224496,-8.215115,7.856804,-6.498233,6.422396,7.594280,-8.420390,1.408145,-2.993458,1.097336,5.606777,2.931959,0.125331,0.635713,6.539415,6.109401,-6.939637,-7.580604,1.894917,-0.395897,8.482539,7.402244,7.607623,5.506940,2.836290,8.469576,-1.245729,6.473855,9.408666,3.262042,-7.631695,-1.603606,-5.774515,8.055253,6.130897,-8.558994,5.256953,-3.283443,-6.411078,9.252053,5.352780,-6.746871,2.962290,7.674001,6.181035,1.105995,0.717930,-9.695497,0.886625,5.202020,-2.846182,6.021041,3.620075,-6.292797,8.483248,-1.313872,-8.333631,0.832342,-0.406052,-9.676134,6.042981,3.909324,-8.759389,-2.578285,1.938550,-8.763284,3.452577,-3.965563,-5.793735,4.836877,-4.483281,-5.200873,-5.306942,-0.714130,-4.636896,-3.573433,-8.639718,-9.810849,-8.491361,-2.127554,3.591792,5.052999,-8.956134,4.367438,-2.701760,1.337017,-8.341923,9.281474,7.441949,3.417097,-4.731386,2.994875,-3.739146,1.656049,-0.475939,-8.420288,1.343767,-2.272790,2.193638,-3.850572,-3.218852,-3.152716,7.757250,-1.418390,1.634210,-9.259266,3.020665,3.306652,1.462701,-7.194381,-9.345460,1.347062,-9.379444,-3.137632,-1.687127,1.512188,-2.586534,3.316888,2.567857,-2.864054,-6.976738,1.707124,-4.855175,9.377903,2.589926,0.123301,-6.553436,7.784817,-1.841722,6.727508,-1.455475,-4.208525,-9.321454,-4.829863,4.156179,8.214300,9.789424,5.620447,6.513731,-2.098890,0.052290,-8.270774,-7.054228,-3.900774,4.101137,2.396529,9.276095,-2.437114,-1.866049,4.600510,6.057986,6.444360,1.045947,-8.873677,8.962602,-1.190782,-4.894778,-5.431871,-6.574996,-1.634053,-9.018040,-0.706396,0.560750,-5.991350,1.824908,0.683583,-3.986944,-9.189631], dtype = "float32")#candidate|5646|(1456,)|const|float32
const_5647 = relay.const([[2.924402,4.323417,-7.705738,3.198933],[-2.004196,0.390799,6.579938,9.169536],[-5.389849,6.031901,-7.955751,-3.917687],[-0.124921,6.776090,-2.388188,6.541511],[3.226938,0.202240,-3.180921,-3.054777],[9.518600,7.613338,-6.964654,-5.462396],[-6.443235,-9.831201,3.308457,9.813533],[-8.855563,-2.050201,4.206528,4.259477],[-4.432266,-3.852686,8.809480,3.239878],[-3.220254,1.035391,-8.952268,5.946090],[0.014267,4.544749,-1.455889,-1.822409],[3.045884,9.583533,-6.512897,1.777435],[-4.343939,-9.431256,-5.756262,-4.713053],[-3.543777,3.560310,0.295301,1.417912],[-7.495483,6.141216,8.217136,-0.159710],[-0.313779,8.836733,-5.455804,6.841977],[9.217652,-3.772933,-3.956997,-1.942888],[-9.226417,3.509013,7.010451,-6.032313],[4.869574,-0.714613,-4.205409,2.983434],[1.340444,8.254829,-9.009326,-0.530686],[-6.697535,3.859115,7.463976,-2.033991],[-8.530235,6.311026,-5.455573,6.389230],[7.614968,7.940236,-1.315493,-9.402376],[1.919583,1.863244,-5.778950,2.497189],[-5.694382,8.226901,9.061677,7.251500],[4.274456,4.928679,3.500764,8.929398],[-9.371099,-5.088451,-0.997765,-2.345370],[-5.722694,9.208578,3.129893,-4.291164],[8.253843,3.030142,2.989808,-6.634661],[8.359921,-7.411485,0.548281,5.515621],[-5.433087,-1.796195,-1.843030,0.513895],[4.454488,-0.580770,6.989931,-7.613063],[-8.424312,6.857734,9.020409,3.382422],[3.432955,9.259048,3.247446,3.198317],[-1.646126,-1.301345,-2.861986,8.815556],[-6.929677,3.608504,-8.226715,4.246105],[6.418591,-7.295062,-1.942965,-5.642447],[-5.906590,-4.261527,-6.534109,9.274719],[-5.964820,-2.656269,1.855707,-4.178216],[8.762548,-3.209850,0.357200,-3.177696],[-1.779816,8.507754,-1.063046,4.677455],[1.635433,8.367128,8.277096,-4.146790],[-2.433840,-2.300915,2.819249,-9.475229],[-2.482680,-9.226050,-4.243100,7.686963],[-7.689536,8.239046,-6.700960,3.403975],[5.801685,0.357261,3.843593,-6.355338],[-5.955257,-7.361371,8.647382,-5.403433],[5.440982,4.141820,-7.672363,-4.546616],[-4.614760,4.826694,-1.815253,-0.782523],[7.287887,-2.640548,-2.049860,7.305300],[-9.087836,-8.060120,-7.798295,7.927781],[4.873730,6.147368,9.035822,-4.387261],[1.129017,-4.743452,-1.112703,5.423972],[8.023427,6.556444,-1.156893,-5.461132],[-1.149389,-2.542779,-6.835328,-8.404568],[9.126629,6.790186,4.275127,-7.428250],[2.390780,2.516020,5.005661,-8.716144],[-4.245765,-8.142751,-9.041688,5.188018],[3.545868,7.888250,-7.528684,-4.811838],[0.626586,-0.105365,3.307061,0.336401],[-5.939095,5.765736,-2.319030,-2.132257],[4.230534,3.657541,2.811122,-2.071276],[9.523646,-8.039160,0.180429,5.991429],[-4.450875,1.244831,-4.139569,9.572691],[6.263393,-2.832246,-2.971642,5.258315],[-3.619888,4.196338,9.220932,-3.109622],[3.219312,-2.117563,6.684775,3.818337],[-4.478857,-7.753780,4.844806,3.478033],[-2.487289,-7.348414,-2.891042,-7.210824],[6.000460,-1.324718,4.355469,8.691889],[-2.898512,5.071579,8.016392,4.060383],[6.284123,-0.458707,5.941402,-2.807133],[7.896451,-1.792838,-8.487143,-7.375662],[-8.378382,-2.924724,-9.546644,-0.542866],[-0.534282,-0.414413,-8.726409,7.443861],[4.539550,9.034416,8.732795,-0.166983],[-6.133879,-0.291574,0.737538,-7.934178],[1.621110,0.191782,-6.729339,-8.164587],[6.208391,-2.933696,1.141833,-3.603998],[3.953230,0.534190,7.841157,-6.151034],[6.408727,-9.576480,7.679720,-5.398155],[1.007979,-3.773388,-4.768599,-3.499399],[-9.587720,7.097833,-1.929468,-8.296927],[9.548458,-4.721692,-3.194061,5.300164],[4.166964,-4.226773,-5.061570,-4.709924],[9.258151,-2.038916,6.026808,2.267438],[4.085948,2.382008,-3.888677,-2.804160],[-4.277591,-2.017210,9.555249,-5.946816],[4.630115,7.191695,3.197247,-3.850538],[4.143444,-4.296844,9.987649,-4.206597],[4.763369,7.331872,7.494082,6.841743]], dtype = "float32")#candidate|5647|(91, 4)|const|float32
call_5645 = relay.TupleGetItem(func_3257_call(relay.reshape(const_5646.astype('float32'), [1456, 1]), relay.reshape(const_5647.astype('float32'), [364,]), ), 7)
call_5648 = relay.TupleGetItem(func_3260_call(relay.reshape(const_5646.astype('float32'), [1456, 1]), relay.reshape(const_5647.astype('float32'), [364,]), ), 7)
bop_5657 = relay.bitwise_xor(call_5645.astype('uint16'), relay.reshape(const_5647.astype('uint16'), relay.shape_of(call_5645))) # shape=(364,)
bop_5660 = relay.bitwise_xor(call_5648.astype('uint16'), relay.reshape(const_5647.astype('uint16'), relay.shape_of(call_5648))) # shape=(364,)
output = relay.Tuple([call_5620,call_5634,call_5640,const_5646,bop_5657,])
output2 = relay.Tuple([call_5621,call_5635,call_5641,const_5646,bop_5660,])
func_5662 = relay.Function([], output)
mod['func_5662'] = func_5662
mod = relay.transform.InferType()(mod)
output = func_5662()
func_5663 = relay.Function([], output)
mutated_mod['func_5663'] = func_5663
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5668 = relay.const([[[4.896799,3.184616,8.700656,7.554300,-7.593293,-4.425648,9.114379,-2.641344],[-6.336075,4.869979,5.007684,6.783720,2.046897,3.478762,0.856945,1.408746],[-5.525822,6.317186,-2.615248,6.062405,-5.869566,2.182867,7.837384,-6.817157],[-6.356856,-5.311777,2.971807,-1.921368,-8.942061,-2.709195,-4.932781,3.470242],[-3.910873,-6.272630,6.531477,1.615635,2.307056,-0.189726,-1.653584,0.540452],[-1.431365,3.391983,6.238057,-3.423423,6.826064,2.633071,-0.190486,2.991663],[6.926690,-2.835065,4.928379,-9.748340,-3.321583,6.572323,0.590445,0.542700],[-8.347731,6.127319,8.689491,8.311369,-5.047904,-8.429874,7.933976,7.168643],[-4.618614,-0.256678,9.861524,-2.210301,4.454610,8.458417,-6.561919,-6.678459],[2.143472,-1.008328,8.549817,3.029719,-9.272833,-4.875852,1.811893,6.955334],[0.850848,6.624854,-7.482071,-3.706702,2.904620,7.082977,4.923473,-5.806974]],[[4.821461,6.262757,1.504204,1.662440,-4.036203,9.555024,9.151155,6.984490],[-1.239124,-9.657121,0.650876,-1.297333,-5.430097,-7.505091,5.435562,-2.406097],[-6.613752,7.124388,-2.713075,4.986625,1.820093,1.535415,0.649752,2.915905],[5.472077,9.822915,2.161431,-3.971931,3.146504,1.699789,6.858694,1.403004],[0.344309,3.901830,6.453739,-5.574227,-0.630427,-9.639875,1.629809,9.613378],[0.708298,3.916994,0.217149,-4.849774,-7.786985,1.972360,7.651155,1.075629],[-6.193514,-2.711465,-2.780301,-1.291120,-1.361527,-7.054535,-7.202466,2.483762],[-6.696923,-3.292418,-1.935401,-1.956908,-9.055972,-6.986964,3.661495,-6.821616],[3.457081,9.603244,-9.262140,-3.767393,-8.513937,-3.375679,-2.405257,-5.924469],[-2.634147,-5.819120,5.569359,5.860261,7.725570,9.521939,-6.515419,-5.280686],[9.686628,1.864818,4.426860,-5.493844,-0.704006,-5.471847,-5.440855,-5.978876]],[[-3.146557,7.145160,2.279117,8.463187,1.985564,2.225772,7.556520,5.971693],[-1.033988,-7.420557,-7.310724,3.299628,4.042561,2.194939,5.781490,-0.832406],[0.975242,6.453163,-4.731799,1.375649,-8.512178,0.258892,-3.287047,-7.787048],[7.770352,-6.416714,7.888362,9.707153,4.877945,4.468742,-9.528047,-7.309994],[6.065572,-0.765490,7.948877,1.923065,9.357162,5.629185,5.355152,-8.473106],[-4.175349,-5.485022,-6.365589,-3.782343,5.894704,-6.358151,1.182760,9.346257],[1.448746,-5.191341,1.017583,-1.738712,3.639763,-1.298384,9.632360,5.567309],[1.858321,3.525098,3.998506,1.318307,4.564711,-3.396767,9.334978,-1.473316],[-0.219880,7.971565,-2.555347,-4.922607,9.700546,1.934395,2.804225,-3.974264],[-4.975842,-7.342814,4.800663,-1.780166,-6.521281,3.366551,-1.002554,-9.759664],[-3.440302,-3.870545,8.040528,-1.817677,7.779413,8.105220,0.064172,6.202610]],[[0.875407,8.320770,-2.088726,-3.781296,2.648212,-8.102603,8.627676,-3.188969],[-5.208442,-5.476813,9.120437,-0.967238,-7.333405,8.923674,5.628170,-4.570336],[-7.557843,5.031696,6.864113,7.110075,5.402977,3.080740,-7.871652,-1.571170],[-3.512151,-5.552897,-0.781031,2.004721,-8.652005,-9.048676,0.615554,1.430275],[-3.225755,-3.001302,-1.514230,-9.554766,4.407710,-0.263597,4.825884,-8.664622],[5.136426,8.551169,2.786952,3.013002,3.843672,0.728093,-1.456218,7.659717],[1.577581,-7.726081,4.853036,3.139379,-6.058335,6.799724,0.746703,-0.695623],[-2.094828,-0.597093,-9.659623,-4.204962,1.999365,-1.468121,-7.418917,-3.290415],[-2.305138,1.399875,-4.852874,-8.164672,-2.036159,-6.513657,-4.090080,-5.112326],[1.642854,-5.569490,-4.811551,8.229777,4.535001,7.459687,6.444550,5.717554],[1.080682,-9.270499,-3.381686,-1.738487,-7.909755,-1.239304,7.662687,0.253673]],[[0.283065,-7.638699,-1.771432,6.832842,-2.967625,9.356375,-2.209164,7.110068],[4.519736,1.299633,-1.705062,-3.991033,7.563950,5.328145,-4.161862,6.309205],[8.027196,6.946479,5.381193,5.832243,-2.134209,-3.645166,2.810637,-3.569739],[3.084711,-3.311794,9.445593,-4.169298,6.463193,-8.738696,-5.070815,0.875880],[1.872465,-0.869436,8.052609,-4.922252,-0.797240,5.587866,-1.899173,3.178264],[0.727606,-4.134332,-2.091726,2.027009,-5.325996,7.121683,3.340706,-6.563980],[-5.493206,-5.850700,-8.305109,1.140498,6.030787,2.975046,-2.768914,2.012094],[-1.264387,-3.657259,-1.931423,4.396927,6.333953,5.719240,1.052107,-8.041432],[-0.167295,-5.034892,9.770689,-5.805904,-4.944857,8.556192,-5.810313,-0.168618],[-8.206553,7.298188,6.873385,4.566680,-7.148584,6.180997,7.327361,0.042666],[-5.312523,-1.807107,2.578326,-7.051488,-7.852788,-9.764749,-0.609256,-5.968569]],[[9.031954,7.558996,-2.182057,-1.290967,-8.246858,-6.073916,8.556940,6.781371],[1.096927,6.811132,-3.384677,-0.809612,0.337495,8.403970,-3.636002,-8.797993],[-1.698344,-1.539905,9.061341,3.345496,-7.173311,9.982336,5.093360,-9.245110],[-5.223333,2.712975,0.506731,-2.733636,-4.696639,6.996945,4.335086,-5.193075],[0.479145,-3.136042,3.379248,-4.010970,0.461154,4.404346,3.616155,-7.709602],[-9.719451,-2.834994,0.861107,-4.669377,0.656800,-1.825511,-6.635602,-4.244257],[7.314440,-0.130396,-3.050760,7.182437,-8.079123,-6.366896,-7.762080,4.024508],[-1.931642,-9.071015,-6.316509,7.035740,-7.957347,-2.044177,-9.263474,4.412051],[5.287650,8.169662,-0.822797,-7.344109,0.472927,-7.706827,7.065627,-8.818998],[-6.850287,1.390652,-3.582903,-3.005031,9.642560,0.498919,2.040345,0.281878],[-0.482626,-4.440681,5.901881,7.528694,2.905095,-9.851812,5.148096,-8.723738]],[[-3.388932,7.589353,-4.422315,1.022505,-7.620618,9.828478,7.743851,1.422238],[7.817395,6.895308,-3.432196,-6.353008,-3.857228,-9.576268,9.723183,2.067311],[-7.134179,-3.271245,-3.205634,-9.797952,-5.709144,-1.292654,3.664695,3.433434],[9.791355,5.553442,4.198328,4.940512,9.763562,-2.597386,-8.941739,-5.396464],[-8.174618,6.971147,-6.379988,5.713340,-0.899698,8.773719,9.733818,-0.904982],[7.630261,-0.366230,5.671791,-5.612043,9.904300,-6.588338,7.309381,4.042640],[6.179960,-7.848177,-0.649618,0.218636,-8.374215,-1.074837,1.961686,-9.559345],[1.594303,-5.800377,2.272622,5.276062,5.994241,-3.250188,-9.774979,-2.791042],[5.451515,0.604678,-6.079744,-7.750732,3.983036,2.739119,5.792287,2.194906],[-9.369194,-2.153938,7.844787,6.838875,7.815566,1.176383,3.394944,9.661531],[-0.304858,-0.970273,9.781464,6.594418,-9.694195,-8.978519,9.704550,-0.491000]]], dtype = "float32")#candidate|5668|(7, 11, 8)|const|float32
const_5669 = relay.const([[[5.028489,-6.302603,5.164668,-6.366904,9.926742,-7.514394,-2.616335,2.195504],[0.463236,7.208019,-9.779808,9.997884,-1.829127,-1.890645,1.206449,9.243006],[-3.601769,6.594845,0.785052,-9.160711,8.643247,1.139401,-2.875595,-7.065614],[-5.497572,-3.821680,4.984676,8.057146,-4.634153,-3.120514,5.442343,-6.791768],[7.288696,6.990356,-5.454695,6.819724,-9.051907,4.027532,-1.810511,-9.891343],[-5.523675,1.291045,4.573020,2.334010,-0.201005,2.206281,5.261881,-3.450870],[3.418389,3.625468,4.717190,9.412229,3.000269,-3.437645,-3.244415,-8.703734],[-2.185160,7.382290,-4.182880,0.707448,-1.701831,-6.777858,3.394812,7.049251],[-4.272897,-8.712973,3.149779,9.789367,-3.231681,-5.063003,2.134487,3.848848],[-5.668266,0.171724,4.394867,-8.934724,7.998200,8.247955,6.072632,6.871980],[2.914828,5.719519,8.701895,-4.880826,4.313952,-7.282746,7.579886,-6.178224]],[[-5.093830,9.218100,-6.668411,-9.546970,-9.899737,-2.666159,-0.241086,-2.486220],[0.424180,-7.163178,-3.362146,5.408046,-0.984150,-8.845150,2.451220,2.823914],[-9.028317,-8.159070,-1.342721,-9.017862,-7.583469,-8.678461,-8.927045,1.487362],[1.949124,-2.287151,-1.615920,3.485440,-3.246883,-4.048800,-8.634998,2.216589],[-9.027652,0.629128,-2.466709,-3.223792,4.734321,6.241840,7.306453,9.135859],[4.831133,-2.599214,2.825340,-6.366073,-5.772750,-7.291215,-8.343602,4.278063],[7.035498,-3.939238,4.108493,-0.603271,0.314030,-4.756719,-3.911245,2.171586],[-1.608984,7.766010,6.089087,4.047240,4.836763,-5.895725,4.110145,-1.052126],[9.689436,1.883567,3.686898,7.442757,8.469122,7.768726,3.578935,3.518169],[5.648594,-1.546527,-9.143173,-5.173405,3.815618,-8.892241,-5.178734,6.546575],[1.068311,-7.033538,-1.536061,4.130734,-9.496366,-9.494721,-0.279694,7.843144]],[[-4.324567,-3.475528,7.372181,-9.315773,-7.354013,7.786140,-6.271152,-9.172164],[1.880691,-2.255215,-7.145520,-9.018712,7.409733,-6.806324,-8.843757,2.885212],[5.357584,-0.623067,-9.433030,3.932264,9.898387,5.414142,2.904897,9.082258],[7.703044,7.077011,5.022440,-0.075592,-1.498135,-9.428994,-0.113636,8.359845],[-6.765489,-8.831011,5.048927,9.466291,-3.766365,-4.153217,-0.340201,6.426392],[7.160123,5.767026,-5.834478,2.157326,-1.979073,0.181036,2.524973,7.258102],[-4.688208,-9.672471,5.926286,-2.069517,0.865766,-4.777235,-3.498352,5.111911],[-5.634291,3.903705,-9.656853,9.422316,-6.343105,3.549558,3.948001,4.412003],[-1.822563,7.630784,6.758626,2.003908,-6.406554,-1.289214,3.067929,2.069341],[-4.669912,-5.409066,1.742349,-3.781650,3.053720,-7.896399,-8.359493,-5.620126],[0.074344,-0.068126,-9.999649,9.479312,4.689981,0.294551,4.480393,-8.171500]],[[4.318469,-3.521594,-0.867433,4.015420,-2.432539,6.829940,1.540575,0.478533],[5.366060,-6.706461,-7.034651,5.698770,6.230680,-5.861596,4.780084,2.867136],[-3.303918,9.500568,-4.918245,-9.564191,-5.447809,5.289682,0.988564,3.270510],[-5.020237,-3.676361,3.985810,7.465097,1.218007,-5.979652,-8.096852,6.867055],[8.089252,-3.948192,3.604641,0.158526,-1.838804,-0.321148,1.712474,-0.739821],[1.729893,-0.484451,-0.074369,2.005907,-7.809728,-2.237046,1.357155,9.943332],[5.692156,-6.953218,-1.901832,-8.823203,-3.510292,-1.935718,-9.693399,-1.826921],[-7.220781,1.209192,-7.511815,-0.885553,-8.940984,8.510575,-0.786474,-4.870212],[-1.388709,0.128862,-8.621224,2.658091,-5.877457,7.679839,1.762740,-5.292531],[-7.326936,-5.416016,-5.885777,3.924839,-4.014798,8.625242,3.276821,-1.118038],[-1.673217,-4.579878,4.122079,-3.867974,-0.578311,6.900281,4.143765,8.464423]],[[1.414682,-7.321802,-4.602025,-6.048735,-8.942680,0.379410,3.312757,-6.943201],[4.701514,2.293483,-7.882876,-3.851522,6.235338,-7.570541,0.366999,-3.866816],[-0.712961,3.885459,1.792500,4.744942,7.906501,4.021967,-9.453197,-1.813366],[6.199020,-1.451085,3.560978,-7.759319,-3.900069,3.803670,-8.075210,-2.361621],[-8.207388,7.701446,5.665204,-7.824853,6.831743,-0.046241,9.534918,-3.542966],[-1.357897,-9.770986,3.666010,-8.533275,-5.458757,-8.199722,0.729093,0.299056],[-7.837703,6.365459,4.646555,-3.824503,-9.028728,-5.053562,2.940158,-4.508467],[3.866523,-2.687928,4.369393,1.646797,-4.800442,-8.992669,-0.756946,-9.415666],[-5.497196,5.226169,1.862826,-0.289197,-5.076724,4.916753,0.405200,2.042383],[-4.201451,-7.163204,-0.610677,4.523437,7.594600,-8.401167,0.400213,-4.915238],[9.339064,8.753327,0.902257,-6.938451,-0.777272,8.477281,6.137575,3.652084]],[[-3.960124,2.992207,2.333757,-2.446925,-5.291848,-8.267185,2.017973,0.762921],[-9.888715,6.063096,-1.519415,4.455584,3.103448,3.301487,0.560706,-1.360885],[-5.570565,-8.535460,4.073992,-5.319264,-5.255709,4.857151,2.205000,-9.987245],[-5.116975,4.579905,2.774107,0.586178,4.736118,2.916898,0.075514,3.249335],[3.647067,6.828200,-6.360015,-0.545533,3.688594,-6.269461,-8.745819,-8.332933],[-1.161976,5.092862,6.530428,-6.527299,0.338495,6.922175,3.230436,-1.478240],[8.692179,3.847309,5.080476,-2.029020,-9.415918,9.773362,8.284352,8.835151],[2.500047,7.526798,2.925171,-5.807715,6.188379,-6.699074,-8.269728,8.715365],[-3.981894,7.307284,-0.397497,-4.892944,-5.166673,9.002485,-2.148493,4.537901],[2.958009,-9.192862,-0.199617,-1.261778,-0.764289,-4.960289,3.940589,-0.669153],[6.454343,-8.291206,3.363232,-3.043331,-7.455421,4.828410,-6.504511,0.058853]],[[8.697672,-4.315192,-3.912102,9.641388,4.062963,6.157172,6.922738,1.338590],[9.126090,-7.914304,-3.418162,-9.386030,-0.928717,2.036792,-3.406544,2.137431],[-7.036116,4.988018,-9.576118,-6.917563,-3.489280,-8.986596,3.248219,-1.057585],[7.875507,-5.629554,4.793020,3.227676,-2.980973,-7.386959,5.929677,6.424887],[-5.342821,-8.502624,5.582029,-3.348095,-5.624603,-4.027056,-3.037214,-0.633179],[0.505401,-9.217064,2.215945,6.155254,-3.872318,-2.720923,1.640592,-0.105701],[-6.349575,-8.336976,1.244121,3.294379,7.159097,0.667005,6.115281,-9.083780],[-5.079938,0.437659,-2.417418,-4.178039,3.216842,-7.476623,-8.982048,-9.177224],[5.264658,-3.949909,0.358716,-0.424040,8.988055,1.636522,1.887919,-9.270790],[-5.449749,8.409057,-9.686986,5.852276,-1.786387,-8.880007,-0.379621,4.339841],[2.023109,-4.151021,4.395039,5.408883,1.767121,2.029001,-6.597656,-9.580610]]], dtype = "float32")#candidate|5669|(7, 11, 8)|const|float32
bop_5670 = relay.power(const_5668.astype('float32'), relay.reshape(const_5669.astype('float32'), relay.shape_of(const_5668))) # shape=(7, 11, 8)
bop_5673 = relay.multiply(const_5669.astype('uint32'), relay.reshape(const_5668.astype('uint32'), relay.shape_of(const_5669))) # shape=(7, 11, 8)
output = relay.Tuple([bop_5670,bop_5673,])
output2 = relay.Tuple([bop_5670,bop_5673,])
func_5688 = relay.Function([], output)
mod['func_5688'] = func_5688
mod = relay.transform.InferType()(mod)
output = func_5688()
func_5689 = relay.Function([], output)
mutated_mod['func_5689'] = func_5689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5573_call = mod.get_global_var('func_5573')
func_5574_call = mutated_mod.get_global_var('func_5574')
call_5695 = relay.TupleGetItem(func_5573_call(), 0)
call_5696 = relay.TupleGetItem(func_5574_call(), 0)
func_560_call = mod.get_global_var('func_560')
func_562_call = mutated_mod.get_global_var('func_562')
const_5705 = relay.const([[5.542065,-9.755322,-0.324451,-8.754082,9.156875,-8.687597,-2.420292,8.924721,2.908745,-0.036577,-4.533460,-4.034610,7.992889,3.920848,-8.347833,4.593485,-2.641391,4.646370,-8.086021,-3.552642,-0.176013,-2.129354,3.662761,-7.151363,9.996088,7.353035,6.486126,-4.802205,-2.498016,-8.662229,-3.081574,-4.265831,2.363442,6.212476,4.573934,1.887517,-6.857374,9.108419,5.410657,-2.580014,-2.031911,-7.562297,7.953296,-4.689570,1.854634,-1.346804,-9.156916,-9.167286,-8.059951,-2.616169,8.408593,-3.167534],[1.710462,-5.419509,1.529166,1.298215,-2.588140,9.891713,-4.037442,8.510870,-8.316337,6.437917,-1.868094,-0.031318,0.197829,6.962961,-8.665579,-5.062840,2.541606,-0.997490,5.877143,-9.044382,-6.954927,7.489189,-8.900682,-9.998805,0.098231,0.376749,5.518378,-6.002769,-2.898454,-6.795547,8.071151,-2.175906,9.167766,0.781194,4.268005,-7.338059,3.479459,-5.512799,3.040452,-7.640883,0.858400,-4.537122,3.645073,9.515156,-7.326910,-1.483346,7.185051,-6.241255,-8.510685,3.441528,-1.565675,1.351611],[-4.909773,8.909001,-6.090924,-5.885384,7.666136,-4.575366,2.691769,3.326465,9.656684,-5.431730,-8.457395,7.302078,-2.212536,-9.267238,7.077863,7.850097,-4.510133,7.285766,-5.036845,-9.811668,-0.881846,7.834324,-3.863855,-8.222954,-4.856370,-0.463353,6.539989,2.349787,3.729850,-2.130680,4.451585,-4.019418,-1.647379,-9.894650,9.450239,8.253400,-0.328160,8.811740,0.303526,-0.419962,-4.846694,-0.068882,2.835783,-5.114911,-0.814584,0.862050,-3.201568,8.803905,8.471594,4.275421,-4.766183,-2.643271],[4.689107,5.958015,2.022196,1.114625,9.553315,-8.962980,0.096199,9.534013,9.273706,-0.002690,-1.342866,2.647386,1.301027,-6.838174,1.147236,-7.368025,-7.348385,9.718263,-4.785423,-2.853771,-5.097465,-7.375215,1.276247,5.502840,-3.049379,-6.954343,0.360889,-3.488085,-4.685969,-1.032642,3.113449,5.240354,1.743428,-6.819850,3.295545,5.809617,3.245622,6.086952,3.305799,1.598852,-3.860333,-0.821233,2.351815,7.040026,7.058539,8.872295,-7.259783,-4.314427,0.850437,2.758971,8.190074,7.179271],[-0.933636,0.056266,0.551429,1.533329,-3.216920,-4.465423,-6.701362,-1.119057,5.557457,5.899320,-3.286716,1.776254,-5.320209,-7.204593,9.095102,-4.044639,-2.170099,5.076202,-5.750576,-7.365724,-8.126250,7.564440,-5.233864,-5.492920,9.581807,7.014484,-9.121080,-0.271783,-4.159133,-6.845600,-9.224151,1.176444,7.990560,-7.958507,-7.758155,-0.666016,9.346498,4.547503,4.342613,-4.655985,7.190895,-2.312786,-3.376031,-1.476055,3.359564,0.608218,6.609119,1.172897,8.510765,6.713672,-0.706340,4.147541],[8.425584,6.452185,-1.869009,6.443004,7.602180,7.177548,-3.134995,-7.375712,0.232059,9.099394,1.024157,1.526822,3.627160,-2.205275,-9.062409,9.978840,-1.327343,6.919587,-8.076097,6.325578,-9.543800,-2.722912,-5.840031,6.990615,-0.782485,6.257490,2.718144,-4.951255,7.453207,-5.881707,-0.746302,1.409724,-5.724382,-4.881189,3.890043,-1.275596,-2.389533,0.569102,-3.813007,-8.203781,9.023198,-5.353335,-0.996364,5.909297,8.701720,-8.348585,-6.626239,-1.021571,-6.038681,3.862998,-5.515318,3.337122],[-6.346773,-4.413381,7.450464,2.321607,-1.964448,8.710621,6.124491,-4.590652,-8.902336,-4.679741,-0.753424,4.641124,2.257110,-7.053226,5.055342,2.284975,-4.099121,-2.698532,-0.830839,5.012493,8.153890,-3.860922,5.664004,6.567832,4.694923,-0.260801,-4.703459,-4.591508,4.942162,-6.907862,-6.812822,-3.081337,6.528855,3.259924,9.313106,-8.864225,1.997493,2.810509,1.922488,1.551384,-6.443353,-5.569084,2.170390,4.196326,7.338543,1.450640,9.089862,6.567475,-8.452308,-3.136049,5.406162,-8.212380]], dtype = "float32")#candidate|5705|(7, 52)|const|float32
call_5704 = func_560_call(relay.reshape(const_5705.astype('float32'), [2, 14, 13]))
call_5706 = func_560_call(relay.reshape(const_5705.astype('float32'), [2, 14, 13]))
func_2687_call = mod.get_global_var('func_2687')
func_2688_call = mutated_mod.get_global_var('func_2688')
call_5707 = relay.TupleGetItem(func_2687_call(), 1)
call_5708 = relay.TupleGetItem(func_2688_call(), 1)
uop_5715 = relay.acos(const_5705.astype('float32')) # shape=(7, 52)
func_639_call = mod.get_global_var('func_639')
func_642_call = mutated_mod.get_global_var('func_642')
const_5721 = relay.const([-8.569116,8.819977,-8.083768,-3.657665,7.781793,2.997300], dtype = "float32")#candidate|5721|(6,)|const|float32
call_5720 = relay.TupleGetItem(func_639_call(relay.reshape(const_5721.astype('float32'), [1, 2, 3])), 0)
call_5722 = relay.TupleGetItem(func_642_call(relay.reshape(const_5721.astype('float32'), [1, 2, 3])), 0)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_5730 = relay.TupleGetItem(func_601_call(), 3)
call_5731 = relay.TupleGetItem(func_603_call(), 3)
bop_5732 = relay.bitwise_or(const_5705.astype('int8'), relay.reshape(call_5704.astype('int8'), relay.shape_of(const_5705))) # shape=(7, 52)
bop_5735 = relay.bitwise_or(const_5705.astype('int8'), relay.reshape(call_5706.astype('int8'), relay.shape_of(const_5705))) # shape=(7, 52)
func_987_call = mod.get_global_var('func_987')
func_991_call = mutated_mod.get_global_var('func_991')
var_5738 = relay.var("var_5738", dtype = "float32", shape = (140,))#candidate|5738|(140,)|var|float32
call_5737 = relay.TupleGetItem(func_987_call(relay.reshape(var_5738.astype('float32'), [14, 10, 1]), relay.reshape(var_5738.astype('float32'), [14, 10, 1]), ), 0)
call_5739 = relay.TupleGetItem(func_991_call(relay.reshape(var_5738.astype('float32'), [14, 10, 1]), relay.reshape(var_5738.astype('float32'), [14, 10, 1]), ), 0)
bop_5744 = relay.bitwise_xor(uop_5715.astype('int32'), relay.reshape(call_5704.astype('int32'), relay.shape_of(uop_5715))) # shape=(7, 52)
bop_5747 = relay.bitwise_xor(uop_5715.astype('int32'), relay.reshape(call_5706.astype('int32'), relay.shape_of(uop_5715))) # shape=(7, 52)
bop_5755 = relay.greater(uop_5715.astype('bool'), relay.reshape(call_5704.astype('bool'), relay.shape_of(uop_5715))) # shape=(7, 52)
bop_5758 = relay.greater(uop_5715.astype('bool'), relay.reshape(call_5706.astype('bool'), relay.shape_of(uop_5715))) # shape=(7, 52)
output = relay.Tuple([call_5695,call_5707,call_5720,const_5721,call_5730,bop_5732,call_5737,var_5738,bop_5744,bop_5755,])
output2 = relay.Tuple([call_5696,call_5708,call_5722,const_5721,call_5731,bop_5735,call_5739,var_5738,bop_5747,bop_5758,])
func_5760 = relay.Function([var_5738,], output)
mod['func_5760'] = func_5760
mod = relay.transform.InferType()(mod)
var_5761 = relay.var("var_5761", dtype = "float32", shape = (140,))#candidate|5761|(140,)|var|float32
output = func_5760(var_5761)
func_5762 = relay.Function([var_5761], output)
mutated_mod['func_5762'] = func_5762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4671_call = mod.get_global_var('func_4671')
func_4673_call = mutated_mod.get_global_var('func_4673')
call_5801 = relay.TupleGetItem(func_4671_call(), 1)
call_5802 = relay.TupleGetItem(func_4673_call(), 1)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_5803 = func_1957_call()
call_5804 = func_1957_call()
func_1250_call = mod.get_global_var('func_1250')
func_1252_call = mutated_mod.get_global_var('func_1252')
const_5824 = relay.const([[0.011095,-2.614859],[-8.461237,6.108518],[5.556415,-4.996134],[-9.597543,6.945797],[8.648378,-5.952416],[-3.067008,-7.869757],[-7.402488,-7.832536],[9.398512,3.313051],[8.513237,-7.909833],[-7.147242,-9.157339],[0.640880,1.826314],[6.427005,-3.514457],[6.312678,-7.306703],[2.214667,5.734109],[-4.755721,-3.308996],[9.173737,-4.236132],[4.370682,-9.798387],[-9.618845,-4.045284],[-5.328994,-6.706949],[-1.010852,-9.831716],[8.760810,-4.496579],[-4.638781,-4.693769],[9.167661,-1.632569],[-6.165594,2.969182],[0.165411,4.725914],[-4.659977,-9.797481],[-7.841844,4.557207],[0.409291,-4.977794],[-2.333978,0.022459],[-4.886456,-1.765009],[-5.329977,-4.942805],[4.693271,7.931140],[2.622484,4.401754],[-0.942987,-3.750145],[-8.731059,6.177701],[-1.872923,-1.025767],[-5.683957,7.329943],[5.852470,-7.982045],[-0.885783,-0.123790],[2.504283,-0.993072],[0.387882,-1.844498],[1.011357,-5.676353],[-8.636296,8.856867],[4.836690,-6.933106],[6.211492,-6.828803],[4.347756,3.329303],[1.249335,8.114562],[7.063415,2.408046],[1.608328,-9.045461],[9.410093,-3.416063],[-5.640682,-9.777480],[9.394147,-2.648239],[-4.983136,5.088243],[9.231440,2.979825],[3.786930,0.598725],[-6.692266,2.371995],[8.127863,0.170863],[-3.667277,-3.960461],[6.878575,-2.598209],[2.769283,-7.788205],[4.037922,4.956436],[-0.879554,8.448600],[-7.494210,-1.627714],[0.329046,-8.040645],[5.494127,3.582029],[-5.531085,-5.588533],[-6.892882,-3.153601],[0.362045,8.420050],[1.845877,-8.220239],[3.207420,7.335847],[-2.699371,2.685571],[5.949263,-4.519031],[4.061759,-1.757265],[-8.880724,6.356482],[6.605313,-4.561849],[-3.895505,9.371171],[0.214662,1.910363],[7.571188,-8.540104],[-6.968745,4.541114],[9.742243,-0.327937],[-2.198104,-5.415598],[-2.436166,4.732807],[-5.370557,-3.724257],[-3.651827,-8.466541],[2.590995,-5.098323],[-9.418032,3.980307],[-8.775878,-0.442645],[-7.688864,-8.488880],[9.032931,1.947602],[7.229803,1.736087],[2.786395,-4.734324],[1.750074,0.248565],[7.781965,5.306098],[-7.827221,-9.145144],[4.243701,-6.460462],[-4.536820,-9.339989],[-1.716431,8.647354],[5.489207,9.287354],[-5.863399,-9.216358],[-5.258784,7.725699],[8.526528,9.273729],[9.999309,2.778507],[-2.866453,-1.342332],[-4.237358,-3.614118],[1.960641,-1.311071],[-4.468483,9.467693],[-3.326585,-1.309723],[5.095971,-1.497138],[-6.301591,-8.500589],[7.470373,-1.710871],[6.243594,-5.580821],[-9.517773,-6.648870],[-6.799018,-5.231183],[-8.445246,-3.352714],[6.658274,9.270103],[-5.924485,7.125880],[5.981046,-2.083015],[1.418092,-8.486858],[7.367233,7.846954],[7.466250,5.228856],[-0.206769,-6.398444],[8.008363,3.120254],[4.645293,2.017569],[-1.766979,-6.204474],[-2.870663,0.825378],[-1.026725,5.518907],[-7.051233,8.068640],[-8.746149,-6.196225],[-2.519878,-7.986551],[2.091109,-4.360437],[-5.011060,-2.104479],[-2.633251,8.454401],[5.917515,3.961105],[-9.918023,1.464169],[8.016367,0.351418],[-3.873887,-4.831221],[-8.274677,-6.687273],[8.917146,2.150339],[5.885441,-6.433560],[-7.743785,-1.031064],[-6.116849,8.503383],[-4.824920,-4.336558],[8.450073,-8.333836],[6.093922,-8.869647],[2.757989,3.627699],[4.627455,-8.337987],[-5.992335,9.800433],[-9.367781,-6.165818],[4.181727,-8.634418],[-7.805269,2.263868],[-5.566302,4.021614],[-3.669107,3.858483],[6.373269,-6.992540],[7.574943,1.823548],[-3.741976,9.843783],[-8.768845,1.250633],[7.242390,-5.269186],[-8.581923,-3.115514],[7.182108,-7.004182],[0.802010,0.233365],[-0.573262,-8.930966],[-2.813393,7.716437],[-2.751909,-2.692492],[-8.548198,-6.695163],[7.512199,-9.821674],[-1.064172,-6.898690],[-6.049891,8.848121],[-1.494090,-0.518941],[6.886115,1.749615],[-9.679270,-0.541660],[4.926473,-4.909484],[-0.547786,5.955465],[2.642032,-9.860774],[-3.309627,3.445866],[0.526477,6.495244],[6.619847,1.913014],[-5.051214,-8.657859],[0.118691,4.344210],[2.470662,9.121694],[-7.115205,3.073069],[-9.135211,1.873746],[-6.821332,6.057138]], dtype = "float32")#candidate|5824|(182, 2)|const|float32
call_5823 = relay.TupleGetItem(func_1250_call(relay.reshape(const_5824.astype('float32'), [364,])), 0)
call_5825 = relay.TupleGetItem(func_1252_call(relay.reshape(const_5824.astype('float32'), [364,])), 0)
func_3499_call = mod.get_global_var('func_3499')
func_3502_call = mutated_mod.get_global_var('func_3502')
const_5837 = relay.const([2.193977,-6.377251,4.816650,-8.480165,-4.827926,-6.576259,7.150572,-7.776960,1.910098,-6.834988,7.899365,-1.716607,-5.620063,-3.086630,-8.644918,1.384360,-7.897317,-5.535850,-1.277951,-8.542286,-5.300165,-9.094353,-1.104497,7.953256,-8.197080,2.001889,-5.826020,4.475821,-9.772752,-4.221465,-6.961716,-8.647126,8.379117,-1.806196,-7.112827,2.496295,1.785077,-5.513590,-6.594586,4.363131,-0.874722,-6.418065,3.286100,8.113053,-5.952432,-6.401057,-7.460313,6.221863,9.261590,7.648171,-8.165807,-8.918455,-8.624924,0.541245,-8.233111,-5.555404,-1.958803,9.681392,-5.971399,1.811960,-3.626563,5.474464,-6.761337,9.000915,-6.072763,2.447727,5.357747,-8.051935,2.471742,-8.511910,0.999441,-3.256739,-1.054297,3.247494,-4.213535,6.392982,-5.294354,7.117530,9.720323,-4.934997,8.696083,9.094942,0.254524,0.848893,2.978413,8.717788,-6.956745,-0.777422,8.504286,0.700931,-2.596345,3.194660,0.990749,-2.270166,1.175006,-8.225463,-2.010605,6.421865,1.666860,-8.994685,-5.571112,8.935457,1.906119,7.670047,8.299528,1.606603,6.015697,-2.827864,2.784599,-9.677224,6.908694,-3.338065,-1.109505,-6.091674,-2.719813,-5.890387,-7.869917,4.862814,-6.803795,-1.566090,4.499461,1.249048,-5.039125,3.584129,-6.762623,-0.254510,-7.958417,-0.536758,-7.314266,-8.799877,4.814123,-0.413472,3.034386,-6.665662,-0.051405,0.756507,-6.050752,5.112793,4.950444,-0.588149,-5.540498,4.431895,1.448083,0.196337,-4.027678,-1.504625,-7.121667,5.825498,-4.975323,7.309098,3.166244,-5.432252,-0.636708,-6.561356,-6.847031,4.703464,-5.112468,0.016754,-9.336932,3.801973,3.136124,7.462060,-9.188507,4.786660,-6.718854,-6.124259,8.739941,0.209675,-7.364934,6.478688,-4.880683,1.337668,-8.126611,8.065075,5.358212,0.622392,-5.295659,-4.228347,-3.530983,-2.718829,8.995427,-4.825741,7.580291,-5.601931,5.758372,8.253181,-3.685552,-3.930355,4.641138,-9.039739,9.323969,3.733773,-8.620437,-1.882373,7.584835,9.885254,3.804023,-1.429147,4.982862,-8.368439,-1.902083,-4.988464,-5.002976,8.303085,-0.195372,-9.217226,-4.025729,-2.973746,-9.698225,6.844249,0.869040,-7.414826,-5.761530,7.961413,6.059539,-1.429424,3.321324,-9.362887,-3.797154,-4.385297,5.689144,-1.429934,-4.815159,-0.991237,5.121471,2.364894,-7.223236,-8.747412,-0.929283,-4.367279,2.841452,8.129397,-1.760693,7.757904,-8.555346,0.642128,-6.637287,1.872813,-3.304060,1.824399,6.219517,-4.774133,-7.552016,-7.145379,1.212179,-5.388695,2.288420,7.972224,-0.498470,-1.836601,-7.588364,-9.938949,4.382896,-0.834474,-1.691445,-2.202788,-2.316988,1.707260,6.535353,4.971587,0.915218,9.338024,1.641024,-1.240639,3.548786,-2.584894,-6.919731,9.972845,-3.435719,-8.478446,0.887134,-5.642958,8.164307,7.014359,3.388815,0.585415,-9.710928,-3.426125,-2.407800,4.139761,6.283154,2.186596,6.291806,-7.108346,-0.198459,-7.271723,6.884127,7.159956,-6.677985,3.990989,4.918067,-6.972748,9.948405,-0.603228,2.920143,-3.177047,0.785626,9.215770,-1.913410,1.597998,-6.181705,-5.080373,-7.883076,-1.031337,-7.727777,4.480655,3.594142,-4.841250,-2.646925,-6.618354,-0.026385,-1.293475,-3.268503,-5.952989,3.247020,-5.955823,3.136840,3.825777,-5.834274,5.052475,0.003561,9.602149,-6.158639,-9.243060,-9.752556,1.842206,5.383510,-4.846682,9.685312,-8.308862,-0.563321,-0.417222,0.263382,-2.886254,1.809371,3.122463,-7.297256,6.690867,-5.967071,9.055643,-7.060973,5.483839,-1.187892,-3.825422,6.502407,8.864987,1.787074,6.069549,7.931035,-4.772174,8.882556,-8.773887,-5.908159,7.161441,1.438558,4.083054,7.709264,5.531079,8.211831,3.524683,-8.552666,-8.417646,-5.989320,-3.218661,4.816188,-6.723184,-7.083737,-0.805395,5.023819,7.675405,-1.437274,-8.794899,-0.991556,-9.844665,1.754542,-3.831528,-3.148542,8.438457,-4.684381,-8.151136,7.595242,7.960030,1.819755,-5.117082,7.246145,7.128686,0.312351,3.520095,8.825401,2.696360,1.458489,-4.442825,-7.516872,-2.898254,-3.195869,5.326885,2.514463,5.555722,-7.499184,7.837783,-3.842008,-8.453639,5.989626,3.639051,9.600421,9.713355,-5.038748,-2.591926,-1.214752,5.471864,4.446565,-6.947555,6.457701,-6.649572,6.207759,2.285800,-4.622560,5.789835,8.759877,7.685958,6.987342,9.632529,-1.698236,5.769587,-5.553017,2.907406,1.600445,0.007353,-3.239659,-5.469663,1.013464,7.991632,5.164502,6.916574,1.777885,1.785172,-3.584483,-7.894785,-2.069706,4.273135,-0.403012,4.449653,-4.515007,8.043026,-6.977049,-3.834211,2.912836,0.900895,5.463843,-7.053664,6.846053,9.986202,-2.866734,4.387092,3.831085,-1.996359,7.964815,4.558699,-8.504536,-8.646035,4.964044,-6.695414,-2.855484,5.836445,9.737015,-5.199959,-0.072456,-4.968063,7.371031,6.101804,-5.424203,4.616449,9.883518,9.204622,9.417574,-0.765583,-7.606046,3.591227,9.441214,-3.297107,-4.138938,1.548584,5.958754,-3.794847,4.001989,1.625510,9.527051,-0.573034,-2.554414,-9.182481,9.776136,-0.139628,9.360861,6.553191,-7.949738,8.722431,-1.627862,9.554037,-9.343884,5.211957,-7.482269,3.689564,8.446584,-1.764810], dtype = "float64")#candidate|5837|(504,)|const|float64
call_5836 = relay.TupleGetItem(func_3499_call(relay.reshape(const_5837.astype('float64'), [3, 12, 14])), 0)
call_5838 = relay.TupleGetItem(func_3502_call(relay.reshape(const_5837.astype('float64'), [3, 12, 14])), 0)
var_5841 = relay.var("var_5841", dtype = "float64", shape = (3, 12, 14))#candidate|5841|(3, 12, 14)|var|float64
bop_5842 = relay.less(call_5836.astype('bool'), relay.reshape(var_5841.astype('bool'), relay.shape_of(call_5836))) # shape=(3, 12, 14)
bop_5845 = relay.less(call_5838.astype('bool'), relay.reshape(var_5841.astype('bool'), relay.shape_of(call_5838))) # shape=(3, 12, 14)
output = relay.Tuple([call_5801,call_5803,call_5823,const_5824,const_5837,bop_5842,])
output2 = relay.Tuple([call_5802,call_5804,call_5825,const_5824,const_5837,bop_5845,])
func_5848 = relay.Function([var_5841,], output)
mod['func_5848'] = func_5848
mod = relay.transform.InferType()(mod)
var_5849 = relay.var("var_5849", dtype = "float64", shape = (3, 12, 14))#candidate|5849|(3, 12, 14)|var|float64
output = func_5848(var_5849)
func_5850 = relay.Function([var_5849], output)
mutated_mod['func_5850'] = func_5850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2789_call = mod.get_global_var('func_2789')
func_2791_call = mutated_mod.get_global_var('func_2791')
call_5863 = func_2789_call()
call_5864 = func_2789_call()
output = call_5863
output2 = call_5864
func_5883 = relay.Function([], output)
mod['func_5883'] = func_5883
mod = relay.transform.InferType()(mod)
mutated_mod['func_5883'] = func_5883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5883_call = mutated_mod.get_global_var('func_5883')
call_5884 = func_5883_call()
output = call_5884
func_5885 = relay.Function([], output)
mutated_mod['func_5885'] = func_5885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_5904 = func_3977_call()
call_5905 = func_3977_call()
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_5915 = func_766_call()
call_5916 = func_766_call()
func_5237_call = mod.get_global_var('func_5237')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_5938 = relay.TupleGetItem(func_5237_call(), 0)
call_5939 = relay.TupleGetItem(func_5239_call(), 0)
func_2897_call = mod.get_global_var('func_2897')
func_2898_call = mutated_mod.get_global_var('func_2898')
call_5947 = relay.TupleGetItem(func_2897_call(), 2)
call_5948 = relay.TupleGetItem(func_2898_call(), 2)
output = relay.Tuple([call_5904,call_5915,call_5938,call_5947,])
output2 = relay.Tuple([call_5905,call_5916,call_5939,call_5948,])
func_5957 = relay.Function([], output)
mod['func_5957'] = func_5957
mod = relay.transform.InferType()(mod)
output = func_5957()
func_5958 = relay.Function([], output)
mutated_mod['func_5958'] = func_5958
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6011 = relay.const([[[0.288009],[9.661881]],[[-2.921218],[0.994448]],[[-3.644781],[4.341155]],[[-3.542054],[-2.019770]],[[-9.326848],[-3.782876]],[[-8.179313],[5.546439]],[[-0.920015],[0.364116]],[[5.634359],[-6.277474]],[[8.458244],[-3.117945]],[[3.909782],[7.843931]],[[6.620015],[-5.447906]],[[-0.734681],[7.553375]]], dtype = "float32")#candidate|6011|(12, 2, 1)|const|float32
uop_6012 = relay.sigmoid(const_6011.astype('float32')) # shape=(12, 2, 1)
output = relay.Tuple([uop_6012,])
output2 = relay.Tuple([uop_6012,])
func_6023 = relay.Function([], output)
mod['func_6023'] = func_6023
mod = relay.transform.InferType()(mod)
mutated_mod['func_6023'] = func_6023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6023_call = mutated_mod.get_global_var('func_6023')
call_6024 = func_6023_call()
output = call_6024
func_6025 = relay.Function([], output)
mutated_mod['func_6025'] = func_6025
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6080 = relay.var("var_6080", dtype = "float64", shape = (4, 8, 8))#candidate|6080|(4, 8, 8)|var|float64
uop_6081 = relay.acos(var_6080.astype('float64')) # shape=(4, 8, 8)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_6084 = relay.TupleGetItem(func_3026_call(), 2)
call_6085 = relay.TupleGetItem(func_3028_call(), 2)
bop_6086 = relay.floor_divide(uop_6081.astype('float64'), relay.reshape(var_6080.astype('float64'), relay.shape_of(uop_6081))) # shape=(4, 8, 8)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_6095 = relay.TupleGetItem(func_3161_call(), 0)
call_6096 = relay.TupleGetItem(func_3162_call(), 0)
func_3595_call = mod.get_global_var('func_3595')
func_3597_call = mutated_mod.get_global_var('func_3597')
call_6102 = func_3595_call()
call_6103 = func_3595_call()
bop_6111 = relay.bitwise_xor(bop_6086.astype('uint64'), relay.reshape(uop_6081.astype('uint64'), relay.shape_of(bop_6086))) # shape=(4, 8, 8)
func_2449_call = mod.get_global_var('func_2449')
func_2451_call = mutated_mod.get_global_var('func_2451')
call_6119 = relay.TupleGetItem(func_2449_call(), 0)
call_6120 = relay.TupleGetItem(func_2451_call(), 0)
uop_6133 = relay.sinh(bop_6086.astype('float32')) # shape=(4, 8, 8)
output = relay.Tuple([call_6084,call_6095,call_6102,bop_6111,call_6119,uop_6133,])
output2 = relay.Tuple([call_6085,call_6096,call_6103,bop_6111,call_6120,uop_6133,])
func_6136 = relay.Function([var_6080,], output)
mod['func_6136'] = func_6136
mod = relay.transform.InferType()(mod)
mutated_mod['func_6136'] = func_6136
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6137 = relay.var("var_6137", dtype = "float64", shape = (4, 8, 8))#candidate|6137|(4, 8, 8)|var|float64
func_6136_call = mutated_mod.get_global_var('func_6136')
call_6138 = func_6136_call(var_6137)
output = call_6138
func_6139 = relay.Function([var_6137], output)
mutated_mod['func_6139'] = func_6139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6151 = relay.var("var_6151", dtype = "float64", shape = (13, 9, 13))#candidate|6151|(13, 9, 13)|var|float64
uop_6152 = relay.asin(var_6151.astype('float64')) # shape=(13, 9, 13)
func_5018_call = mod.get_global_var('func_5018')
func_5019_call = mutated_mod.get_global_var('func_5019')
call_6162 = func_5018_call()
call_6163 = func_5018_call()
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_6169 = relay.TupleGetItem(func_5190_call(), 0)
call_6170 = relay.TupleGetItem(func_5191_call(), 0)
output = relay.Tuple([uop_6152,call_6162,call_6169,])
output2 = relay.Tuple([uop_6152,call_6163,call_6170,])
func_6171 = relay.Function([var_6151,], output)
mod['func_6171'] = func_6171
mod = relay.transform.InferType()(mod)
mutated_mod['func_6171'] = func_6171
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6172 = relay.var("var_6172", dtype = "float64", shape = (13, 9, 13))#candidate|6172|(13, 9, 13)|var|float64
func_6171_call = mutated_mod.get_global_var('func_6171')
call_6173 = func_6171_call(var_6172)
output = call_6173
func_6174 = relay.Function([var_6172], output)
mutated_mod['func_6174'] = func_6174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3644_call = mod.get_global_var('func_3644')
func_3646_call = mutated_mod.get_global_var('func_3646')
call_6214 = func_3644_call()
call_6215 = func_3644_call()
output = relay.Tuple([call_6214,])
output2 = relay.Tuple([call_6215,])
func_6221 = relay.Function([], output)
mod['func_6221'] = func_6221
mod = relay.transform.InferType()(mod)
mutated_mod['func_6221'] = func_6221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6221_call = mutated_mod.get_global_var('func_6221')
call_6222 = func_6221_call()
output = call_6222
func_6223 = relay.Function([], output)
mutated_mod['func_6223'] = func_6223
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6224 = relay.var("var_6224", dtype = "float64", shape = (2, 5, 8))#candidate|6224|(2, 5, 8)|var|float64
uop_6225 = relay.log(var_6224.astype('float64')) # shape=(2, 5, 8)
func_3336_call = mod.get_global_var('func_3336')
func_3338_call = mutated_mod.get_global_var('func_3338')
var_6231 = relay.var("var_6231", dtype = "float64", shape = (3, 28))#candidate|6231|(3, 28)|var|float64
call_6230 = func_3336_call(relay.reshape(var_6231.astype('float64'), [2, 6, 7]))
call_6232 = func_3336_call(relay.reshape(var_6231.astype('float64'), [2, 6, 7]))
bop_6234 = relay.left_shift(uop_6225.astype('int8'), relay.reshape(var_6224.astype('int8'), relay.shape_of(uop_6225))) # shape=(2, 5, 8)
func_4726_call = mod.get_global_var('func_4726')
func_4728_call = mutated_mod.get_global_var('func_4728')
call_6238 = relay.TupleGetItem(func_4726_call(), 2)
call_6239 = relay.TupleGetItem(func_4728_call(), 2)
var_6248 = relay.var("var_6248", dtype = "float32", shape = (140,))#candidate|6248|(140,)|var|float32
bop_6249 = relay.less_equal(call_6238.astype('bool'), relay.reshape(var_6248.astype('bool'), relay.shape_of(call_6238))) # shape=(140,)
bop_6252 = relay.less_equal(call_6239.astype('bool'), relay.reshape(var_6248.astype('bool'), relay.shape_of(call_6239))) # shape=(140,)
output = relay.Tuple([call_6230,var_6231,bop_6234,bop_6249,])
output2 = relay.Tuple([call_6232,var_6231,bop_6234,bop_6252,])
func_6256 = relay.Function([var_6224,var_6231,var_6248,], output)
mod['func_6256'] = func_6256
mod = relay.transform.InferType()(mod)
mutated_mod['func_6256'] = func_6256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6256_call = mutated_mod.get_global_var('func_6256')
var_6258 = relay.var("var_6258", dtype = "float64", shape = (2, 5, 8))#candidate|6258|(2, 5, 8)|var|float64
var_6259 = relay.var("var_6259", dtype = "float64", shape = (3, 28))#candidate|6259|(3, 28)|var|float64
var_6260 = relay.var("var_6260", dtype = "float32", shape = (140,))#candidate|6260|(140,)|var|float32
call_6257 = func_6256_call(var_6258,var_6259,var_6260,)
output = call_6257
func_6261 = relay.Function([var_6258,var_6259,var_6260,], output)
mutated_mod['func_6261'] = func_6261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6268 = relay.var("var_6268", dtype = "int16", shape = (13, 6, 1))#candidate|6268|(13, 6, 1)|var|int16
const_6269 = relay.const([[[8,-3,2,-3,4,2,7,-5,-4,-5,8,-3],[1,2,1,-7,4,6,-2,4,-2,-2,-2,4],[-9,10,8,-6,5,-4,6,5,-1,-7,-1,-1],[-7,-4,7,-9,-8,6,2,3,-2,4,-6,7],[10,-2,-4,4,5,-2,-7,-1,-10,10,-10,9],[-8,9,2,5,9,2,2,5,-5,2,-8,8]],[[-3,-9,-9,-7,1,-5,2,-4,-9,4,-2,1],[-6,9,7,3,4,-2,-2,2,-7,-6,-8,1],[7,-9,4,4,4,-7,1,-2,4,9,-5,1],[7,10,-10,-3,6,-5,3,-4,5,9,-1,-2],[-4,-3,2,-8,3,-4,-9,-9,-8,-7,6,-9],[3,8,8,-1,10,1,9,-1,-9,3,-2,5]],[[9,-5,3,5,-2,2,-2,2,8,-2,-7,7],[-7,-6,-5,3,2,8,-9,-3,-5,-3,-9,-6],[10,-4,-2,3,-3,10,-9,-1,-8,8,1,10],[-10,10,-10,8,6,-7,5,8,6,-6,-1,-7],[6,-10,-9,-1,-5,-8,-9,3,8,-2,9,-9],[-7,1,3,-9,-1,6,-9,-9,-7,-7,3,2]],[[9,2,-3,4,-7,-8,-1,9,-3,-4,-1,-5],[1,-5,-2,-4,10,-1,-7,10,8,-2,4,2],[6,10,-8,6,-8,4,9,-3,1,1,-8,2],[1,-4,-7,2,2,-9,-6,-2,7,4,-1,4],[-10,-2,7,4,-9,-3,-5,-10,-9,-9,-7,1],[8,-9,-4,-3,-9,3,-2,-4,-7,9,-3,1]],[[9,7,5,-9,3,2,-2,-2,-1,-7,-5,-3],[-9,6,-1,-4,-9,8,10,4,5,1,-2,-6],[-1,7,-3,8,-3,4,1,8,-10,3,4,-3],[3,6,-8,-10,7,-5,-6,-4,5,-6,-5,-6],[3,-5,7,7,2,5,8,-9,1,-9,6,9],[-1,-8,3,3,3,2,8,10,-5,-1,2,-9]],[[-5,1,2,-3,-9,1,-6,8,4,9,-1,3],[-4,8,6,9,6,5,2,-10,10,2,6,5],[-2,-2,-3,-9,-9,5,6,1,5,-1,3,-9],[1,-8,3,-6,8,-8,-3,10,-5,9,8,-5],[-5,2,-8,-10,-4,7,-4,10,1,4,4,5],[-8,3,4,1,-6,7,3,4,-8,5,-4,-5]],[[-3,-8,-5,-10,-9,1,3,-5,6,-7,-1,-8],[-4,2,-8,-4,10,-9,6,7,4,-1,1,-8],[-7,-8,7,-9,7,-6,2,5,1,6,5,5],[3,-6,1,3,-10,8,5,6,-1,-8,-4,3],[-10,7,4,5,-5,4,-7,-5,8,-6,-3,6],[7,-6,-8,10,-10,1,6,-1,-9,8,2,4]],[[-9,2,3,5,-1,-2,-10,4,9,1,-3,8],[-7,-7,4,-8,4,-4,-7,6,7,-4,-2,6],[6,-9,-10,-1,5,-8,1,-1,-4,-1,-1,-9],[-9,-5,3,-4,-1,-8,-2,-9,-8,8,-3,-6],[4,-9,6,-5,-1,8,4,-1,-9,-5,9,-9],[-1,6,-8,10,-10,6,7,3,-4,1,4,-2]],[[-2,-3,-2,-6,9,-6,6,8,-7,4,-8,9],[7,-9,-2,2,-9,-5,-7,-2,6,-5,6,-10],[10,4,-10,-7,4,8,8,-2,-6,7,-1,-2],[-9,-9,2,7,-3,9,5,-10,3,-7,-9,9],[-7,9,-5,4,9,8,-3,3,-7,9,8,1],[7,-4,8,-2,-8,-4,9,7,-1,9,-10,-10]],[[-5,-9,8,4,-1,-4,10,5,-4,-10,-6,2],[2,1,-4,-10,-10,1,10,-5,-4,1,4,1],[-6,-4,-8,10,-8,3,-4,2,-4,3,-8,7],[9,7,4,5,1,-2,4,10,-7,-5,-7,-4],[-9,5,5,-1,-9,-2,-10,-5,-4,1,-3,1],[5,-10,4,3,10,3,1,-2,4,-7,10,-5]],[[-1,4,9,-5,-3,9,6,9,4,-1,-5,7],[-8,-6,-6,-1,-9,-4,-10,3,1,-1,5,-3],[3,4,-9,-9,-5,3,8,-10,-1,-3,1,-6],[-9,-9,8,-3,-8,-9,8,-1,-7,-4,-10,-9],[-9,2,2,4,5,-6,-7,-4,-6,9,-2,-6],[-7,-3,-5,6,7,-7,5,10,7,3,-7,-9]],[[1,-8,10,-4,-4,-4,9,4,9,5,-3,6],[-1,3,7,10,2,10,1,1,-1,6,-6,-6],[-4,-10,5,8,-4,-3,-5,-8,-2,8,-2,-9],[-3,-3,-5,-3,1,7,-9,4,-6,-6,-2,7],[-5,-7,6,-10,-1,10,-3,5,6,9,-7,-9],[-10,3,1,7,-8,3,-10,-5,-7,9,7,3]],[[7,9,5,-6,-4,8,-2,-1,9,4,-8,-4],[-3,-4,-6,4,-9,7,2,8,4,-3,-10,5],[-8,-1,-8,-9,8,1,-2,-7,-9,-6,10,7],[9,8,-2,-1,4,7,8,4,1,10,-2,6],[-3,-10,-8,7,-9,-9,10,3,3,-7,-6,-7],[-8,-4,-5,-2,5,-3,3,10,-5,-2,10,-8]]], dtype = "int16")#candidate|6269|(13, 6, 12)|const|int16
bop_6270 = relay.bitwise_xor(var_6268.astype('int16'), const_6269.astype('int16')) # shape=(13, 6, 12)
func_5883_call = mod.get_global_var('func_5883')
func_5885_call = mutated_mod.get_global_var('func_5885')
call_6273 = func_5883_call()
call_6274 = func_5883_call()
output = relay.Tuple([bop_6270,call_6273,])
output2 = relay.Tuple([bop_6270,call_6274,])
func_6279 = relay.Function([var_6268,], output)
mod['func_6279'] = func_6279
mod = relay.transform.InferType()(mod)
var_6280 = relay.var("var_6280", dtype = "int16", shape = (13, 6, 1))#candidate|6280|(13, 6, 1)|var|int16
output = func_6279(var_6280)
func_6281 = relay.Function([var_6280], output)
mutated_mod['func_6281'] = func_6281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4671_call = mod.get_global_var('func_4671')
func_4673_call = mutated_mod.get_global_var('func_4673')
call_6283 = relay.TupleGetItem(func_4671_call(), 1)
call_6284 = relay.TupleGetItem(func_4673_call(), 1)
func_6279_call = mod.get_global_var('func_6279')
func_6281_call = mutated_mod.get_global_var('func_6281')
var_6307 = relay.var("var_6307", dtype = "int16", shape = (78,))#candidate|6307|(78,)|var|int16
call_6306 = relay.TupleGetItem(func_6279_call(relay.reshape(var_6307.astype('int16'), [13, 6, 1])), 0)
call_6308 = relay.TupleGetItem(func_6281_call(relay.reshape(var_6307.astype('int16'), [13, 6, 1])), 0)
var_6309 = relay.var("var_6309", dtype = "int16", shape = (13, 6, 12))#candidate|6309|(13, 6, 12)|var|int16
bop_6310 = relay.greater(call_6306.astype('bool'), relay.reshape(var_6309.astype('bool'), relay.shape_of(call_6306))) # shape=(13, 6, 12)
bop_6313 = relay.greater(call_6308.astype('bool'), relay.reshape(var_6309.astype('bool'), relay.shape_of(call_6308))) # shape=(13, 6, 12)
uop_6317 = relay.acos(bop_6310.astype('float32')) # shape=(13, 6, 12)
uop_6319 = relay.acos(bop_6313.astype('float32')) # shape=(13, 6, 12)
func_5332_call = mod.get_global_var('func_5332')
func_5334_call = mutated_mod.get_global_var('func_5334')
var_6334 = relay.var("var_6334", dtype = "float32", shape = (1400,))#candidate|6334|(1400,)|var|float32
call_6333 = relay.TupleGetItem(func_5332_call(relay.reshape(var_6334.astype('float32'), [10, 140])), 0)
call_6335 = relay.TupleGetItem(func_5334_call(relay.reshape(var_6334.astype('float32'), [10, 140])), 0)
func_3924_call = mod.get_global_var('func_3924')
func_3927_call = mutated_mod.get_global_var('func_3927')
var_6347 = relay.var("var_6347", dtype = "bool", shape = (336,))#candidate|6347|(336,)|var|bool
call_6346 = relay.TupleGetItem(func_3924_call(relay.reshape(var_6347.astype('bool'), [16, 3, 7])), 2)
call_6348 = relay.TupleGetItem(func_3927_call(relay.reshape(var_6347.astype('bool'), [16, 3, 7])), 2)
output = relay.Tuple([call_6283,var_6307,uop_6317,call_6333,var_6334,call_6346,var_6347,])
output2 = relay.Tuple([call_6284,var_6307,uop_6319,call_6335,var_6334,call_6348,var_6347,])
func_6356 = relay.Function([var_6307,var_6309,var_6334,var_6347,], output)
mod['func_6356'] = func_6356
mod = relay.transform.InferType()(mod)
var_6357 = relay.var("var_6357", dtype = "int16", shape = (78,))#candidate|6357|(78,)|var|int16
var_6358 = relay.var("var_6358", dtype = "int16", shape = (13, 6, 12))#candidate|6358|(13, 6, 12)|var|int16
var_6359 = relay.var("var_6359", dtype = "float32", shape = (1400,))#candidate|6359|(1400,)|var|float32
var_6360 = relay.var("var_6360", dtype = "bool", shape = (336,))#candidate|6360|(336,)|var|bool
output = func_6356(var_6357,var_6358,var_6359,var_6360,)
func_6361 = relay.Function([var_6357,var_6358,var_6359,var_6360,], output)
mutated_mod['func_6361'] = func_6361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_6378 = func_766_call()
call_6379 = func_766_call()
func_1539_call = mod.get_global_var('func_1539')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_6382 = func_1539_call()
call_6383 = func_1539_call()
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_6391 = func_364_call()
call_6392 = func_364_call()
func_5883_call = mod.get_global_var('func_5883')
func_5885_call = mutated_mod.get_global_var('func_5885')
call_6393 = func_5883_call()
call_6394 = func_5883_call()
func_987_call = mod.get_global_var('func_987')
func_991_call = mutated_mod.get_global_var('func_991')
const_6398 = relay.const([[-5.067505,8.427024],[1.453810,7.271688],[-1.576110,4.442565],[-8.905772,-3.792159],[-0.217090,5.278814],[-0.026410,7.808055],[-1.012260,2.929664],[-6.062712,5.028941],[4.619383,7.575215],[-4.261017,-3.240719],[0.801534,7.293426],[-3.816736,8.937179],[3.271845,3.760747],[8.825058,-0.727267],[7.500776,4.849876],[6.585390,-2.269706],[7.944250,1.648149],[-2.133466,-9.617573],[6.515465,-4.934245],[-4.562544,2.523028],[-8.493459,7.783035],[7.955099,7.592280],[6.567146,-3.607456],[5.069565,3.746729],[1.827109,-5.353796],[-2.671099,3.022041],[-1.999913,-9.227348],[3.689757,-9.379406],[-0.916172,-9.118046],[0.331337,-3.346884],[-9.401147,6.541436],[1.160524,-5.237122],[5.969977,-5.668427],[8.670626,-4.253580],[9.271275,-1.584360],[-0.978741,-2.766021],[-9.679610,-4.701786],[-6.879500,-3.550207],[5.692725,2.415336],[-2.054538,5.731022],[-1.398723,-4.821070],[-3.839541,-7.350187],[8.089955,-3.394631],[6.254329,-5.523024],[6.645037,-5.675428],[5.161286,-0.718864],[-6.595736,2.322453],[3.722191,2.061108],[-4.413308,-0.912638],[-3.289204,2.600714],[7.566656,2.042409],[-7.794774,4.726446],[-6.754974,-0.275467],[-7.301514,-9.320152],[-7.925783,-5.613389],[0.257387,0.498318],[5.125805,-2.055413],[-1.437902,0.859644],[8.350955,2.633590],[-7.531498,-5.884868],[-5.371451,-8.561382],[3.658787,6.148420],[-1.834347,-4.925350],[6.176815,0.099547],[0.360145,-2.488988],[6.330571,3.888037],[-5.840178,4.162418],[7.284127,8.277243],[-2.155777,5.242518],[9.472576,8.167596]], dtype = "float32")#candidate|6398|(70, 2)|const|float32
call_6397 = relay.TupleGetItem(func_987_call(relay.reshape(const_6398.astype('float32'), [14, 10, 1]), relay.reshape(const_6398.astype('float32'), [14, 10, 1]), ), 1)
call_6399 = relay.TupleGetItem(func_991_call(relay.reshape(const_6398.astype('float32'), [14, 10, 1]), relay.reshape(const_6398.astype('float32'), [14, 10, 1]), ), 1)
output = relay.Tuple([call_6378,call_6382,call_6391,call_6393,call_6397,const_6398,])
output2 = relay.Tuple([call_6379,call_6383,call_6392,call_6394,call_6399,const_6398,])
func_6406 = relay.Function([], output)
mod['func_6406'] = func_6406
mod = relay.transform.InferType()(mod)
output = func_6406()
func_6407 = relay.Function([], output)
mutated_mod['func_6407'] = func_6407
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6472 = relay.var("var_6472", dtype = "float32", shape = (3, 2, 2))#candidate|6472|(3, 2, 2)|var|float32
uop_6473 = relay.atanh(var_6472.astype('float32')) # shape=(3, 2, 2)
func_639_call = mod.get_global_var('func_639')
func_642_call = mutated_mod.get_global_var('func_642')
const_6481 = relay.const([2.682554,-6.306670,-2.151464,3.535603,-3.303945,4.740876], dtype = "float32")#candidate|6481|(6,)|const|float32
call_6480 = relay.TupleGetItem(func_639_call(relay.reshape(const_6481.astype('float32'), [1, 2, 3])), 0)
call_6482 = relay.TupleGetItem(func_642_call(relay.reshape(const_6481.astype('float32'), [1, 2, 3])), 0)
bop_6486 = relay.subtract(uop_6473.astype('int16'), relay.reshape(var_6472.astype('int16'), relay.shape_of(uop_6473))) # shape=(3, 2, 2)
func_490_call = mod.get_global_var('func_490')
func_491_call = mutated_mod.get_global_var('func_491')
call_6508 = relay.TupleGetItem(func_490_call(), 0)
call_6509 = relay.TupleGetItem(func_491_call(), 0)
output = relay.Tuple([call_6480,const_6481,bop_6486,call_6508,])
output2 = relay.Tuple([call_6482,const_6481,bop_6486,call_6509,])
func_6529 = relay.Function([var_6472,], output)
mod['func_6529'] = func_6529
mod = relay.transform.InferType()(mod)
var_6530 = relay.var("var_6530", dtype = "float32", shape = (3, 2, 2))#candidate|6530|(3, 2, 2)|var|float32
output = func_6529(var_6530)
func_6531 = relay.Function([var_6530], output)
mutated_mod['func_6531'] = func_6531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_6557 = func_766_call()
call_6558 = func_766_call()
output = relay.Tuple([call_6557,])
output2 = relay.Tuple([call_6558,])
func_6594 = relay.Function([], output)
mod['func_6594'] = func_6594
mod = relay.transform.InferType()(mod)
output = func_6594()
func_6595 = relay.Function([], output)
mutated_mod['func_6595'] = func_6595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6594_call = mod.get_global_var('func_6594')
func_6595_call = mutated_mod.get_global_var('func_6595')
call_6652 = relay.TupleGetItem(func_6594_call(), 0)
call_6653 = relay.TupleGetItem(func_6595_call(), 0)
func_4019_call = mod.get_global_var('func_4019')
func_4025_call = mutated_mod.get_global_var('func_4025')
var_6660 = relay.var("var_6660", dtype = "float32", shape = (6, 140))#candidate|6660|(6, 140)|var|float32
const_6661 = relay.const([-2.003651,-3.141596,-1.035377,-3.240155,-4.460403,3.360506,5.125676,0.913636,-0.977320,3.699363,-3.380340,-3.427752,8.982876,-2.394751,6.124104,2.890421,9.858763,-8.517976,-9.813671,-6.150985,-6.850134,-9.165658,-7.600823,8.496788,9.581090,-8.723532,-4.007413,-3.209403,-9.905673,-0.670477,-1.504930,-9.774756,4.407379,8.356768,0.323416,3.868055,-9.266880,8.619847,3.869704,5.838149,-4.659601,-4.470682,-4.136705,-8.699647,-2.276320,-4.207770,-7.905867,-9.999094,2.062949,4.202717,-7.078322,-9.242638,-7.018757,7.467465,-1.997981,-0.794396,-3.047074,9.646633,4.175218,-8.405647,0.615166,0.202827,5.292355,2.493909,9.597936,9.089819,1.242852,-4.184898,-8.019394,-8.501601,-6.630414,2.153429,8.407571,9.582000,-3.330280,-4.725761,-3.465577,-6.753399,-5.551079,-9.720584,-4.514316,0.850485,3.245473,-4.901841,6.476498,-0.526032,6.813300,-0.963799,1.465076,-1.772177,9.226117,0.924195,-7.408799,3.320686,3.522144,-5.086851,-5.059728,-7.791828,-1.470423,1.155238,9.307945,0.171411,8.429318,7.089608,-1.577681,-6.774566,5.756616,6.115912,3.150103,-3.222365,5.819190,2.461935,-1.400702,6.754703,-8.538814,-3.868971,5.021222,-6.636483,8.888221,1.635328,4.807268,-3.989243,3.281876,-6.597419,-2.867857,7.014526,-4.543170,0.454465,-6.459545,4.045314,6.925839,-2.635815,9.264708,7.766201,2.398927,-7.907045,9.820550,0.316469,0.880256,9.610809,-6.535146,2.333401,6.286262,9.601301,8.751727,-1.928930,-4.779221,1.506051,-4.833977,-4.255337,0.586948,-3.819025,6.027055,8.443727,-2.480257,5.246048,-2.429718,6.476052,1.287305,9.322506,8.483041,-1.130114,6.759419,1.762833,-6.343657,7.625207,2.900148,-3.009196,5.441050,6.415859,2.496405,-9.878537,3.964894,9.585043,-9.258601,2.559038,0.167723,9.168925,-2.688659,-9.272835,-3.521098,-0.777716,8.277762,6.063699,1.063159,-0.212135,4.720610,-0.787669,-5.411799,6.053546,-2.851154,-0.595609,-7.986097,-1.393514,8.138355,-7.093053,-0.625359,1.954105,2.762387,-2.617180,5.967358,4.851995,7.514606,0.707085,-9.441827,-5.416565,6.920862,-1.557318,-5.211605,-1.258883,3.832295,-4.864732,-7.554977,0.234237,-2.867698,-3.981976,7.445034,-2.180778,7.209178,-7.937855,-6.443075,-5.156925,-8.133457,-6.114868,-2.777149,-8.930227,7.811579,4.531701,-0.189953,7.196026,2.764420,-9.546193,-5.043387,1.697143,-2.029778,9.255416,3.839499,-8.973001,-2.854713,-8.338317,-6.596589,-8.138733,4.888273,0.069204,-6.187600,-5.810834,-9.274259,-5.777523,3.689446,-6.562970,-6.717508,7.184875,3.539927,1.036163,-4.292187,-9.845962,-0.029852,-1.427435,1.043506,5.552819,-5.964704,7.821824,-0.772797,6.060631,3.380001,3.086988,9.284658,2.466848,-4.407143,-9.581043,8.235887,4.005269,8.724472,7.359067,4.637381,9.058004,7.242803,-9.917195,-2.069215,7.391004,9.982294,5.757842,8.037182,-0.082185,3.726507,-2.414005,8.090777,-1.317442,8.873023,2.282613,-6.559646,7.055098,5.354673,1.391877,8.580687,-3.574557,8.783951,-4.556021,-0.760754,5.690687,3.843169,-0.494071,1.848289,-1.514964,0.537988,-6.357394,-7.888801,3.297348,8.025633,4.592682,6.727233,-3.654138,-1.502574,-0.959828,9.935629,-5.734458,5.797319,1.528457,-6.525044,-0.231981,-6.206366,4.748417,-7.536454,-8.056683,-0.766727,-0.740651,1.741956,-2.639122,0.584164,0.004656,-4.360283,-7.948435,-7.826560,4.329409,5.808702,-8.563627,-0.944405,-8.388387,-1.832342,-0.669808,-5.545361,6.700491,9.309213,7.928689,-2.749539,0.357241,7.406008,-4.468166,-6.315317,-8.858331,8.810017,1.149003,-9.330078,-1.609837,-9.621967,5.502569,-7.547140,9.732939,2.997435,-0.169949,3.124569,-6.500184,9.440083,-2.214634,-5.663550,8.605850,-6.422390,6.741777,-8.318920,4.627770,0.881599,-2.877477,2.659183,9.230976,-2.806338,-6.721179,-3.744188,-7.030355,-3.821964,4.011632,2.912459,-2.304063,9.450235,8.686462,-0.339181,-7.510859,2.348456,7.039024,-9.763405,9.743837,-1.474453,-9.835082,5.649265,9.175173,-6.975825,-0.753344,4.818521,2.485393,1.091343,4.107621,3.818580,8.307487,-2.763132,-3.594891,3.040805,6.644026,9.704446,-2.701835,0.008370,-1.899229,-7.233572,6.690281,-5.716735,-9.126391,4.666081,4.940912,-9.284433,-9.005227,6.894498,7.603593,-1.923655,-4.687590,5.961131,-0.074336,-2.778770,-5.401816,-9.044943,4.763438,-8.210923,-9.599470,2.806967,-9.928721,-6.891378,-9.107991,6.366373,-9.911832,-0.814236,-3.248514,-2.310427,-9.988846,6.175354,2.679167,8.254160,-8.387398,9.190150,8.868425,-5.992227,-6.941387,-8.806093,-3.053813,-5.711486,-5.072499,-9.234378,-5.457412,7.146998,4.622830,9.779820,-7.778387,2.652329,-3.788645,3.575049,2.674445,-4.593613,-8.657080,-7.884512,-6.271768,-2.969974,-8.145932,1.120426,2.852999,9.225604,-6.548347,2.355692,6.437358,7.816015,9.377963,-4.153888,4.007508,-0.618144,7.055439,-7.183558,-3.953726,-5.668916,0.363272,5.091710,8.955349,-0.539297,-7.567164,-4.148438,-7.934313,0.371598,5.841034,0.845795,-7.986695,-6.661918,-4.201814,-8.956824,7.084984,5.799473,-1.171371,8.994869,-3.441938,5.090251,-7.440899,-3.958088,-8.575553,-6.388184,1.580586,-5.213550,-7.096239,-2.164892,4.356071,0.428852,6.874268,-7.443043,1.247296,3.712460,1.705753,-4.085926,8.422459,-4.796806,1.331541,5.243872,-0.268671,-8.847969,-1.907420,-1.872759,7.564462,6.646918,-0.983276,7.599774,3.778968,1.016123,6.915609,-6.215497,5.218439,-4.521830,-3.772347,5.796768,8.016521,8.218399,-2.202701,-5.337608,1.182141,8.688264,0.098968,1.633874,4.176296,9.965236,0.549982,9.822068,-6.373455,2.672496,7.236507,-7.805319,-7.428014,9.997571,5.046696,4.140875,6.636698,-0.214288,4.947876,7.691648,7.425271,9.185727,5.126440,9.688484,1.551091,-0.133045,8.185425,7.109056,-1.923874,8.316843,-9.336022,-5.369112,3.894146,-7.515569,-5.146520,0.586314,-1.485545,-5.832178,-4.251760,-6.595368,-7.769554,-3.135840,0.140071,-1.734461,-9.254634,7.243151,-7.869110,-7.137396,-4.829605,-6.969497,5.064713,-7.010908,-5.841894,4.760060,-5.654888,-4.490911,-1.855203,9.013585,5.951578,9.993559,8.189662,-8.257864,-1.206917,0.805038,-1.094401,5.852237,0.581989,0.031184,1.047081,-3.329404,-4.969093,-9.900114,-5.124844,-3.324641,1.477698,2.680626,-5.580042,-7.958055,8.802145,-4.918249,6.483773,7.964298,8.242251,5.510659,7.998790,3.679108,-5.781659,-7.056417,5.870508,-7.493536,-2.912863,5.968977,-3.231351,5.081139,4.760021,8.499601,5.707992,4.897858,6.818000,4.819063,6.790388,5.011809,0.802379,-6.365143,-7.322383,1.034804,-0.683454,-0.318848,7.477366,-7.195541,4.079410,7.644937,-7.595212,3.100469,5.096121,-3.903440,6.729167,6.645269,7.114216,9.576972,-5.422483,-0.553039,8.433650,4.527073,-7.163535,8.834290,4.410764,6.117151,-7.882685,-8.579597,4.542927,-2.333314,-0.817059,8.160892,4.590880,9.842846,-7.626717,-2.983394,-6.425960,-4.184733,-2.744772,-6.788770,-1.415604,4.802337,6.443113,3.381088,5.484074,5.025877,3.404450,2.597055,-7.022970,-0.772603,1.699839,-2.231103,5.107606,-6.832312,5.630211,9.816629,-6.346041,-2.806230,-3.498708,2.691153,4.674782,7.626674,0.268352,5.812428,-7.878899,-0.382881,-9.059900,0.770523,9.626225,4.833681,6.146307,5.464140,-8.442815,5.871457,1.719007,-1.910024,3.407762,0.373792,-1.442489,-5.444320,-2.462226,-8.181467,-3.989366,-6.882252,-1.205754,-1.586714,5.922616,5.328500,0.071826,-9.439773,8.784485,8.883990,7.520429,-8.092622,1.347111,-1.069520,2.334072,-1.479810,-3.002123,-5.726206,5.681419,-9.434086,-7.952100,-6.473112,-5.954870,-3.883435,9.860459,7.733482,-7.461118,-0.616924,-3.914071,6.970953,-0.625795,1.120857,8.461194,3.046413,-1.095294,7.978435,1.439089,-1.146812,-1.369114,-6.503782,-4.985185,-7.758193,6.924981,-1.076990,8.760340,9.244427,-1.067128,0.853331,-9.108708,-8.281107,-3.535466,6.400916,3.014563,-9.008633,-5.194180,8.404481,-4.826734,5.299374,-3.558597,9.953532,-8.672869,1.590951,-5.732310,-0.045646,5.001819,8.832601,-8.039040,-7.545637,4.000221,4.328840,1.673905,-6.413583,0.485163,3.779515,-6.326233,0.160648,5.395057,7.848273,1.961947,0.171279,-6.255294,5.892525,2.231091,-0.889676,-7.141356,3.477109,-8.412878,9.468844,5.914991,1.904750,9.356449,-0.445181,-7.164214,-3.156646,7.517510,-4.076291,7.761585,-0.667778,7.240154,6.856696,1.123839,2.758268,-1.383737,1.068231,1.729207,7.474458,2.214420,-4.495635,6.875646,-3.930880,-2.017468,-9.493246,-6.106005,-5.432314,2.819841,4.447180,-3.386110,-2.497249,5.608451,9.467855,9.964749,7.153966,-0.523946,-6.204601,9.574815,8.190886,0.026028,9.022559,-0.249636,-9.923829,1.981424,-0.013771,-1.944734,-0.037310,-0.244426,1.698825,5.540930,4.868051,-6.349402,8.937040,-5.555227,5.454735,2.578320,1.414201,-5.507452,5.836482,1.496204,-7.244188,7.305719,0.923444,-8.266707,0.108811,2.957686,2.140330,-5.401663,0.869686,1.902005,-8.211712,1.385140,8.853221,1.394316,9.405440,-4.287032,4.692674,3.816279,-2.701050,8.828857,5.183153,-4.582654,-0.248874,5.703082,9.414756,-3.951214], dtype = "float64")#candidate|6661|(900,)|const|float64
const_6662 = relay.const([-1,-1,10,-5,-1,-7,-8,-10,9,2,1,7,-4,-3,-3,2,-5,-7,8,-7,10,-9,10,-9,-1,6,-6,7,5,6,4,-2,-10,5,10,-7,5,1,5,4,-1,-9,3,-7,-8,6,9,-3,6,-7,10,-7,7,-10,-9,8,3,7,3,-4,-4,-5,8,-4,-5,-1,4,-10,9,5,2,-8,-1,3,-6,7,9,5,-9,2,-9,-9,-2,-5,-8,-8,4,-9,8,10,-9,6,-2,-5,-9,5,1,-2,-4,5,7,-4,9,7,5,3,-8,-2,-1,1,8,-9,-1,-6,-10,-9,-4,2,-6,3,8,-5,-5,5,8,6,-2,-4,8,10,-1,-8,1,10,-9,-9,7,3,5,-9,-6,6,10,2,2,-9,-2,9,7,3,2,-2,7,2,5,-4,6,10,-4,7,6,-10,-3,4,-10,-5,-10,-3,2,1,-9,-10,-7,-3,3,-6,6,-9,-6,-8,-9,-9,9,8,-7,1,-3,1,1,10,5,-5,3,9,-5,6,-9,-5,-6,2,-3,1,5,-8,7,-2,-8,-3,-1,10,1,-1,4,-1,-10,-6,-7,9,-1,8,-6,10,9,3,-10,-5,-3,-3,4,-7,-10,-5,2,-9,-10,-2,-9,-8,-8,8,8,-8,10,7,-7,8,9,-4,-9,5,10,-6,8,7,9,-3,-9,-9,2,4,-2,9,-8,-4,4,6,5,-4,10,-10], dtype = "int32")#candidate|6662|(270,)|const|int32
const_6663 = relay.const([False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False], dtype = "bool")#candidate|6663|(336,)|const|bool
call_6659 = relay.TupleGetItem(func_4019_call(relay.reshape(var_6660.astype('float32'), [8, 7, 15]), relay.reshape(const_6661.astype('float64'), [900,]), relay.reshape(const_6662.astype('int32'), [3, 90]), relay.reshape(const_6663.astype('bool'), [24, 14]), ), 4)
call_6664 = relay.TupleGetItem(func_4025_call(relay.reshape(var_6660.astype('float32'), [8, 7, 15]), relay.reshape(const_6661.astype('float64'), [900,]), relay.reshape(const_6662.astype('int32'), [3, 90]), relay.reshape(const_6663.astype('bool'), [24, 14]), ), 4)
output = relay.Tuple([call_6652,call_6659,var_6660,const_6661,const_6662,const_6663,])
output2 = relay.Tuple([call_6653,call_6664,var_6660,const_6661,const_6662,const_6663,])
func_6687 = relay.Function([var_6660,], output)
mod['func_6687'] = func_6687
mod = relay.transform.InferType()(mod)
mutated_mod['func_6687'] = func_6687
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6688 = relay.var("var_6688", dtype = "float32", shape = (6, 140))#candidate|6688|(6, 140)|var|float32
func_6687_call = mutated_mod.get_global_var('func_6687')
call_6689 = func_6687_call(var_6688)
output = call_6689
func_6690 = relay.Function([var_6688], output)
mutated_mod['func_6690'] = func_6690
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6720 = relay.var("var_6720", dtype = "int64", shape = (9, 14, 9))#candidate|6720|(9, 14, 9)|var|int64
var_6721 = relay.var("var_6721", dtype = "int64", shape = (9, 14, 9))#candidate|6721|(9, 14, 9)|var|int64
bop_6722 = relay.multiply(var_6720.astype('int64'), relay.reshape(var_6721.astype('int64'), relay.shape_of(var_6720))) # shape=(9, 14, 9)
output = bop_6722
output2 = bop_6722
func_6725 = relay.Function([var_6720,var_6721,], output)
mod['func_6725'] = func_6725
mod = relay.transform.InferType()(mod)
var_6726 = relay.var("var_6726", dtype = "int64", shape = (9, 14, 9))#candidate|6726|(9, 14, 9)|var|int64
var_6727 = relay.var("var_6727", dtype = "int64", shape = (9, 14, 9))#candidate|6727|(9, 14, 9)|var|int64
output = func_6725(var_6726,var_6727,)
func_6728 = relay.Function([var_6726,var_6727,], output)
mutated_mod['func_6728'] = func_6728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4256_call = mod.get_global_var('func_4256')
func_4258_call = mutated_mod.get_global_var('func_4258')
call_6733 = func_4256_call()
call_6734 = func_4256_call()
output = relay.Tuple([call_6733,])
output2 = relay.Tuple([call_6734,])
func_6740 = relay.Function([], output)
mod['func_6740'] = func_6740
mod = relay.transform.InferType()(mod)
mutated_mod['func_6740'] = func_6740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6740_call = mutated_mod.get_global_var('func_6740')
call_6741 = func_6740_call()
output = call_6741
func_6742 = relay.Function([], output)
mutated_mod['func_6742'] = func_6742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_905_call = mod.get_global_var('func_905')
func_906_call = mutated_mod.get_global_var('func_906')
call_6757 = func_905_call()
call_6758 = func_905_call()
output = call_6757
output2 = call_6758
func_6759 = relay.Function([], output)
mod['func_6759'] = func_6759
mod = relay.transform.InferType()(mod)
output = func_6759()
func_6760 = relay.Function([], output)
mutated_mod['func_6760'] = func_6760
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6801 = relay.var("var_6801", dtype = "float32", shape = (4, 16, 8))#candidate|6801|(4, 16, 8)|var|float32
uop_6802 = relay.atanh(var_6801.astype('float32')) # shape=(4, 16, 8)
var_6811 = relay.var("var_6811", dtype = "float32", shape = (4, 16, 8))#candidate|6811|(4, 16, 8)|var|float32
bop_6812 = relay.subtract(var_6801.astype('uint8'), relay.reshape(var_6811.astype('uint8'), relay.shape_of(var_6801))) # shape=(4, 16, 8)
output = relay.Tuple([uop_6802,bop_6812,])
output2 = relay.Tuple([uop_6802,bop_6812,])
func_6823 = relay.Function([var_6801,var_6811,], output)
mod['func_6823'] = func_6823
mod = relay.transform.InferType()(mod)
mutated_mod['func_6823'] = func_6823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6823_call = mutated_mod.get_global_var('func_6823')
var_6825 = relay.var("var_6825", dtype = "float32", shape = (4, 16, 8))#candidate|6825|(4, 16, 8)|var|float32
var_6826 = relay.var("var_6826", dtype = "float32", shape = (4, 16, 8))#candidate|6826|(4, 16, 8)|var|float32
call_6824 = func_6823_call(var_6825,var_6826,)
output = call_6824
func_6827 = relay.Function([var_6825,var_6826,], output)
mutated_mod['func_6827'] = func_6827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4397_call = mod.get_global_var('func_4397')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_6875 = relay.TupleGetItem(func_4397_call(), 0)
call_6876 = relay.TupleGetItem(func_4399_call(), 0)
func_4861_call = mod.get_global_var('func_4861')
func_4863_call = mutated_mod.get_global_var('func_4863')
call_6891 = relay.TupleGetItem(func_4861_call(), 0)
call_6892 = relay.TupleGetItem(func_4863_call(), 0)
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
call_6904 = relay.TupleGetItem(func_3057_call(), 0)
call_6905 = relay.TupleGetItem(func_3059_call(), 0)
output = relay.Tuple([call_6875,call_6891,call_6904,])
output2 = relay.Tuple([call_6876,call_6892,call_6905,])
func_6909 = relay.Function([], output)
mod['func_6909'] = func_6909
mod = relay.transform.InferType()(mod)
mutated_mod['func_6909'] = func_6909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mutated_mod.get_global_var('func_6909')
call_6910 = func_6909_call()
output = call_6910
func_6911 = relay.Function([], output)
mutated_mod['func_6911'] = func_6911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6946 = relay.var("var_6946", dtype = "float32", shape = (7, 12, 4))#candidate|6946|(7, 12, 4)|var|float32
uop_6947 = relay.sqrt(var_6946.astype('float32')) # shape=(7, 12, 4)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
const_6950 = relay.const([4.707211,-8.060567,-5.495653,0.397871,1.301647,-2.713863,-6.301928,3.865259,-7.347969,9.597404,-9.207828,-4.820858], dtype = "float32")#candidate|6950|(12,)|const|float32
call_6949 = relay.TupleGetItem(func_6529_call(relay.reshape(const_6950.astype('float32'), [3, 2, 2])), 0)
call_6951 = relay.TupleGetItem(func_6531_call(relay.reshape(const_6950.astype('float32'), [3, 2, 2])), 0)
output = relay.Tuple([uop_6947,call_6949,const_6950,])
output2 = relay.Tuple([uop_6947,call_6951,const_6950,])
func_6955 = relay.Function([var_6946,], output)
mod['func_6955'] = func_6955
mod = relay.transform.InferType()(mod)
var_6956 = relay.var("var_6956", dtype = "float32", shape = (7, 12, 4))#candidate|6956|(7, 12, 4)|var|float32
output = func_6955(var_6956)
func_6957 = relay.Function([var_6956], output)
mutated_mod['func_6957'] = func_6957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5237_call = mod.get_global_var('func_5237')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_6999 = relay.TupleGetItem(func_5237_call(), 0)
call_7000 = relay.TupleGetItem(func_5239_call(), 0)
func_5607_call = mod.get_global_var('func_5607')
func_5608_call = mutated_mod.get_global_var('func_5608')
call_7003 = relay.TupleGetItem(func_5607_call(), 1)
call_7004 = relay.TupleGetItem(func_5608_call(), 1)
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_7007 = func_766_call()
call_7008 = func_766_call()
output = relay.Tuple([call_6999,call_7003,call_7007,])
output2 = relay.Tuple([call_7000,call_7004,call_7008,])
func_7051 = relay.Function([], output)
mod['func_7051'] = func_7051
mod = relay.transform.InferType()(mod)
output = func_7051()
func_7052 = relay.Function([], output)
mutated_mod['func_7052'] = func_7052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6911_call = mutated_mod.get_global_var('func_6911')
call_7071 = relay.TupleGetItem(func_6909_call(), 2)
call_7072 = relay.TupleGetItem(func_6911_call(), 2)
func_5146_call = mod.get_global_var('func_5146')
func_5149_call = mutated_mod.get_global_var('func_5149')
const_7089 = relay.const([2.943706,8.282732,1.312603,-9.461586,-7.321605,-4.910476,-6.542628,-7.020500,9.233484,-6.741018,9.525612,2.944595,-0.566755,6.430572,-0.309046,-7.973818,-4.581709,-9.719453,-5.504955,6.173533,-6.825466,7.434490,-8.620183,2.877696,4.377124,7.559175,0.403396,9.363752,4.838631,-4.137875,-7.503485,-2.345475], dtype = "float64")#candidate|7089|(32,)|const|float64
call_7088 = relay.TupleGetItem(func_5146_call(relay.reshape(const_7089.astype('float64'), [8, 1, 4])), 1)
call_7090 = relay.TupleGetItem(func_5149_call(relay.reshape(const_7089.astype('float64'), [8, 1, 4])), 1)
func_1250_call = mod.get_global_var('func_1250')
func_1252_call = mutated_mod.get_global_var('func_1252')
var_7092 = relay.var("var_7092", dtype = "float32", shape = (364,))#candidate|7092|(364,)|var|float32
call_7091 = relay.TupleGetItem(func_1250_call(relay.reshape(var_7092.astype('float32'), [364,])), 2)
call_7093 = relay.TupleGetItem(func_1252_call(relay.reshape(var_7092.astype('float32'), [364,])), 2)
func_2933_call = mod.get_global_var('func_2933')
func_2935_call = mutated_mod.get_global_var('func_2935')
var_7096 = relay.var("var_7096", dtype = "float32", shape = (140, 1))#candidate|7096|(140, 1)|var|float32
call_7095 = relay.TupleGetItem(func_2933_call(relay.reshape(var_7096.astype('float32'), [140,])), 1)
call_7097 = relay.TupleGetItem(func_2935_call(relay.reshape(var_7096.astype('float32'), [140,])), 1)
func_5760_call = mod.get_global_var('func_5760')
func_5762_call = mutated_mod.get_global_var('func_5762')
call_7113 = relay.TupleGetItem(func_5760_call(relay.reshape(var_7096.astype('float32'), [140,])), 2)
call_7114 = relay.TupleGetItem(func_5762_call(relay.reshape(var_7096.astype('float32'), [140,])), 2)
output = relay.Tuple([call_7071,call_7088,const_7089,call_7091,var_7092,call_7095,var_7096,call_7113,])
output2 = relay.Tuple([call_7072,call_7090,const_7089,call_7093,var_7092,call_7097,var_7096,call_7114,])
func_7119 = relay.Function([var_7092,var_7096,], output)
mod['func_7119'] = func_7119
mod = relay.transform.InferType()(mod)
mutated_mod['func_7119'] = func_7119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7119_call = mutated_mod.get_global_var('func_7119')
var_7121 = relay.var("var_7121", dtype = "float32", shape = (364,))#candidate|7121|(364,)|var|float32
var_7122 = relay.var("var_7122", dtype = "float32", shape = (140, 1))#candidate|7122|(140, 1)|var|float32
call_7120 = func_7119_call(var_7121,var_7122,)
output = call_7120
func_7123 = relay.Function([var_7121,var_7122,], output)
mutated_mod['func_7123'] = func_7123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2664_call = mod.get_global_var('func_2664')
func_2666_call = mutated_mod.get_global_var('func_2666')
call_7134 = func_2664_call()
call_7135 = func_2664_call()
output = relay.Tuple([call_7134,])
output2 = relay.Tuple([call_7135,])
func_7190 = relay.Function([], output)
mod['func_7190'] = func_7190
mod = relay.transform.InferType()(mod)
mutated_mod['func_7190'] = func_7190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7190_call = mutated_mod.get_global_var('func_7190')
call_7191 = func_7190_call()
output = call_7191
func_7192 = relay.Function([], output)
mutated_mod['func_7192'] = func_7192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3147_call = mod.get_global_var('func_3147')
func_3149_call = mutated_mod.get_global_var('func_3149')
call_7246 = relay.TupleGetItem(func_3147_call(), 0)
call_7247 = relay.TupleGetItem(func_3149_call(), 0)
output = call_7246
output2 = call_7247
func_7258 = relay.Function([], output)
mod['func_7258'] = func_7258
mod = relay.transform.InferType()(mod)
mutated_mod['func_7258'] = func_7258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7258_call = mutated_mod.get_global_var('func_7258')
call_7259 = func_7258_call()
output = call_7259
func_7260 = relay.Function([], output)
mutated_mod['func_7260'] = func_7260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5688_call = mod.get_global_var('func_5688')
func_5689_call = mutated_mod.get_global_var('func_5689')
call_7333 = relay.TupleGetItem(func_5688_call(), 0)
call_7334 = relay.TupleGetItem(func_5689_call(), 0)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_7340 = relay.TupleGetItem(func_1097_call(), 0)
call_7341 = relay.TupleGetItem(func_1098_call(), 0)
output = relay.Tuple([call_7333,call_7340,])
output2 = relay.Tuple([call_7334,call_7341,])
func_7343 = relay.Function([], output)
mod['func_7343'] = func_7343
mod = relay.transform.InferType()(mod)
output = func_7343()
func_7344 = relay.Function([], output)
mutated_mod['func_7344'] = func_7344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7365 = relay.var("var_7365", dtype = "float64", shape = (8, 13))#candidate|7365|(8, 13)|var|float64
uop_7366 = relay.sin(var_7365.astype('float64')) # shape=(8, 13)
output = uop_7366
output2 = uop_7366
func_7375 = relay.Function([var_7365,], output)
mod['func_7375'] = func_7375
mod = relay.transform.InferType()(mod)
var_7376 = relay.var("var_7376", dtype = "float64", shape = (8, 13))#candidate|7376|(8, 13)|var|float64
output = func_7375(var_7376)
func_7377 = relay.Function([var_7376], output)
mutated_mod['func_7377'] = func_7377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5237_call = mod.get_global_var('func_5237')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_7398 = relay.TupleGetItem(func_5237_call(), 0)
call_7399 = relay.TupleGetItem(func_5239_call(), 0)
func_2687_call = mod.get_global_var('func_2687')
func_2688_call = mutated_mod.get_global_var('func_2688')
call_7400 = relay.TupleGetItem(func_2687_call(), 1)
call_7401 = relay.TupleGetItem(func_2688_call(), 1)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
call_7438 = relay.TupleGetItem(func_2326_call(), 0)
call_7439 = relay.TupleGetItem(func_2328_call(), 0)
func_2933_call = mod.get_global_var('func_2933')
func_2935_call = mutated_mod.get_global_var('func_2935')
const_7443 = relay.const([-8.329781,1.011447,-0.667799,-1.813731,-8.991430,-8.643534,5.611516,7.683539,-1.101143,-8.410876,-7.794094,-2.792155,-8.608116,7.846035,5.124296,4.976310,6.949107,-1.196544,-7.319796,-1.432733,4.671432,-8.029097,-6.098455,8.175879,-1.824093,-8.680071,-6.894657,-5.911553,-6.165645,3.417790,-4.866608,8.628725,6.192640,9.614125,-3.281802,-2.196573,7.674521,2.534372,9.579679,-1.954254,-2.183861,-9.892787,2.116658,5.155421,-9.914020,6.304305,5.232160,-2.663046,-8.493333,2.518014,1.133797,-8.800680,-9.257598,-1.443839,2.747457,-1.166547,5.684028,-8.160337,5.438266,5.103588,-9.831694,-6.710561,4.902193,6.260722,7.897260,1.806326,-8.153686,3.348435,7.216112,-3.765736,-7.054073,-0.005990,7.066838,-3.375080,3.660790,-0.305929,-3.896983,1.299705,0.915182,-9.830633,9.809352,7.840405,0.394917,7.394796,0.724517,7.051110,-2.222866,6.636855,1.819476,-7.199387,9.517855,-1.834025,-9.126375,-2.452528,-9.410755,-7.804611,-2.688085,-9.247246,-3.275471,-1.776080,7.977198,9.007184,9.687715,-9.060959,-4.084538,7.856843,0.072037,6.204792,-4.138580,-3.209808,-7.333555,-8.063685,-7.513526,1.845333,-6.740644,-1.109304,3.536333,2.266356,0.367272,2.775293,9.613255,7.206633,4.914769,-1.290394,-0.147636,-1.734610,7.698721,3.840013,7.905042,-0.265097,-1.858921,-2.882166,-6.988571,6.282857,2.213951,1.320716,4.754244,2.299751,8.521184,-2.274210], dtype = "float32")#candidate|7443|(140,)|const|float32
call_7442 = relay.TupleGetItem(func_2933_call(relay.reshape(const_7443.astype('float32'), [140,])), 2)
call_7444 = relay.TupleGetItem(func_2935_call(relay.reshape(const_7443.astype('float32'), [140,])), 2)
output = relay.Tuple([call_7398,call_7400,call_7438,call_7442,const_7443,])
output2 = relay.Tuple([call_7399,call_7401,call_7439,call_7444,const_7443,])
func_7447 = relay.Function([], output)
mod['func_7447'] = func_7447
mod = relay.transform.InferType()(mod)
output = func_7447()
func_7448 = relay.Function([], output)
mutated_mod['func_7448'] = func_7448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2687_call = mod.get_global_var('func_2687')
func_2688_call = mutated_mod.get_global_var('func_2688')
call_7468 = relay.TupleGetItem(func_2687_call(), 0)
call_7469 = relay.TupleGetItem(func_2688_call(), 0)
output = call_7468
output2 = call_7469
func_7470 = relay.Function([], output)
mod['func_7470'] = func_7470
mod = relay.transform.InferType()(mod)
output = func_7470()
func_7471 = relay.Function([], output)
mutated_mod['func_7471'] = func_7471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6911_call = mutated_mod.get_global_var('func_6911')
call_7544 = relay.TupleGetItem(func_6909_call(), 1)
call_7545 = relay.TupleGetItem(func_6911_call(), 1)
func_3312_call = mod.get_global_var('func_3312')
func_3314_call = mutated_mod.get_global_var('func_3314')
call_7554 = relay.TupleGetItem(func_3312_call(), 0)
call_7555 = relay.TupleGetItem(func_3314_call(), 0)
output = relay.Tuple([call_7544,call_7554,])
output2 = relay.Tuple([call_7545,call_7555,])
func_7561 = relay.Function([], output)
mod['func_7561'] = func_7561
mod = relay.transform.InferType()(mod)
output = func_7561()
func_7562 = relay.Function([], output)
mutated_mod['func_7562'] = func_7562
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7597 = relay.var("var_7597", dtype = "uint32", shape = ())#candidate|7597|()|var|uint32
var_7598 = relay.var("var_7598", dtype = "uint32", shape = (12, 13, 8))#candidate|7598|(12, 13, 8)|var|uint32
bop_7599 = relay.multiply(var_7597.astype('uint32'), var_7598.astype('uint32')) # shape=(12, 13, 8)
output = bop_7599
output2 = bop_7599
func_7607 = relay.Function([var_7597,var_7598,], output)
mod['func_7607'] = func_7607
mod = relay.transform.InferType()(mod)
var_7608 = relay.var("var_7608", dtype = "uint32", shape = ())#candidate|7608|()|var|uint32
var_7609 = relay.var("var_7609", dtype = "uint32", shape = (12, 13, 8))#candidate|7609|(12, 13, 8)|var|uint32
output = func_7607(var_7608,var_7609,)
func_7610 = relay.Function([var_7608,var_7609,], output)
mutated_mod['func_7610'] = func_7610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5018_call = mod.get_global_var('func_5018')
func_5019_call = mutated_mod.get_global_var('func_5019')
call_7648 = func_5018_call()
call_7649 = func_5018_call()
func_905_call = mod.get_global_var('func_905')
func_906_call = mutated_mod.get_global_var('func_906')
call_7670 = func_905_call()
call_7671 = func_905_call()
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_7679 = relay.TupleGetItem(func_4503_call(), 1)
call_7680 = relay.TupleGetItem(func_4505_call(), 1)
output = relay.Tuple([call_7648,call_7670,call_7679,])
output2 = relay.Tuple([call_7649,call_7671,call_7680,])
func_7737 = relay.Function([], output)
mod['func_7737'] = func_7737
mod = relay.transform.InferType()(mod)
output = func_7737()
func_7738 = relay.Function([], output)
mutated_mod['func_7738'] = func_7738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6759_call = mod.get_global_var('func_6759')
func_6760_call = mutated_mod.get_global_var('func_6760')
call_7847 = func_6759_call()
call_7848 = func_6759_call()
var_7849 = relay.var("var_7849", dtype = "uint64", shape = (7, 1))#candidate|7849|(7, 1)|var|uint64
bop_7850 = relay.logical_or(call_7847.astype('bool'), var_7849.astype('bool')) # shape=(7, 1)
bop_7853 = relay.logical_or(call_7848.astype('bool'), var_7849.astype('bool')) # shape=(7, 1)
func_1904_call = mod.get_global_var('func_1904')
func_1905_call = mutated_mod.get_global_var('func_1905')
call_7856 = relay.TupleGetItem(func_1904_call(), 0)
call_7857 = relay.TupleGetItem(func_1905_call(), 0)
output = relay.Tuple([bop_7850,call_7856,])
output2 = relay.Tuple([bop_7853,call_7857,])
func_7860 = relay.Function([var_7849,], output)
mod['func_7860'] = func_7860
mod = relay.transform.InferType()(mod)
mutated_mod['func_7860'] = func_7860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7861 = relay.var("var_7861", dtype = "uint64", shape = (7, 1))#candidate|7861|(7, 1)|var|uint64
func_7860_call = mutated_mod.get_global_var('func_7860')
call_7862 = func_7860_call(var_7861)
output = call_7862
func_7863 = relay.Function([var_7861], output)
mutated_mod['func_7863'] = func_7863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_7873 = func_1116_call()
call_7874 = func_1116_call()
func_5332_call = mod.get_global_var('func_5332')
func_5334_call = mutated_mod.get_global_var('func_5334')
const_7888 = relay.const([[-4.783251,5.129582,4.632951,1.235506,-8.064454,-5.562240,4.259060,-4.510844,-3.718529,4.507289,6.634850,8.258741,-2.245259,0.459600,-2.519798,-9.578851,4.101169,8.852183,-1.501419,-7.929662,-2.726027,0.283536,7.223945,6.543621,1.295965,6.632013,-6.442463,-2.835176,3.760244,3.070230,6.833456,-8.817248,4.279516,7.614952,-2.957174,-7.357226,-1.701079,3.100732,7.351126,-9.307797,1.050835,6.153357,-0.665273,7.770032,5.876788,-0.120850,-6.546446,-5.806486,-8.623447,-5.465904,7.119391,0.308418,-3.756607,5.405044,3.006858,-6.989891,4.378654,-2.740080,0.062499,-1.598158,-4.660450,-4.905883,2.182340,-2.484148,-3.633497,4.572641,-4.207227,-0.406211,0.990992,-8.254602,2.808100,1.120337,0.818454,-1.275673,7.402913,9.291990,5.031831,1.273927,-9.123840,-0.194471,-7.077080,3.034156,-1.263109,3.870791,6.537347,0.330316,8.210970,-6.268332,-0.435696,1.786892,6.965846,-9.871639,-8.699649,2.870375,4.386732,-0.752708,4.546191,-9.712932,8.265523,2.355045,-9.439816,1.411961,-9.486261,-9.465731,-2.096450,-5.727921,-6.475984,9.918487,-9.634878,-7.771927,-3.899223,5.375985,-5.837723,-4.739396,-8.384655,-3.744162,-2.466927,-4.302159,7.720209,3.335227,-2.514890,5.771374,-2.389689,-4.580039,-6.549447,2.847160,3.402183,-1.345922,-3.875994,9.821624,9.490090,7.013599,9.988113,-6.891248,-0.115905,-1.060879,0.385132,-4.018234,-5.869816,5.862856],[4.847718,-7.286184,3.805104,-5.397538,3.459009,-5.307676,7.147342,-9.585869,7.104939,-7.678544,-3.224123,2.771362,-9.259771,-9.837758,-1.339824,1.154328,-2.724287,-6.514429,5.557490,3.511209,-0.943749,2.521174,-8.598117,-1.711244,-2.885977,4.207164,0.161220,-6.966205,-6.826666,4.058967,-4.904325,-9.020583,-1.607804,4.656071,7.992904,-5.843745,-5.335845,-8.313577,2.743420,3.894477,6.606884,-5.777435,0.881781,-4.316475,0.548784,-9.536618,8.516951,-7.183731,7.959519,1.579085,2.899684,-9.166790,4.328926,-4.783193,7.284710,-9.123306,-2.909302,3.284710,7.007515,-9.981417,8.631541,3.104763,1.084732,-8.298725,9.406262,-7.521670,2.424649,-2.987957,8.854363,8.148507,-4.465263,4.749317,5.644823,-2.385643,-0.707832,2.480698,4.775885,-9.533632,4.289977,7.974108,-8.829683,1.332614,-1.766379,-8.576901,-3.427906,-0.600051,4.743877,9.270315,9.699030,-6.073847,-0.559680,2.064353,-8.729994,2.375504,8.736542,-3.224889,-8.050833,4.429469,3.652395,-3.690506,-9.669607,3.484361,-3.080053,-4.958491,-5.004119,0.625245,-5.736452,3.080606,6.498178,-5.277433,9.234242,-8.690816,-7.314316,2.487083,-0.397108,9.082670,-2.307220,-3.184714,-8.347814,-6.977114,3.986241,2.583899,0.860766,-4.316678,1.691349,6.862661,9.685970,-8.449045,3.422901,-8.392420,6.355852,-1.436039,-2.745565,-7.258166,2.277191,2.170997,5.902263,6.268174,5.237372,6.477681],[-5.936752,-7.826463,-5.949724,-8.818017,-6.866784,3.360594,-9.190082,4.869439,9.279902,6.152427,2.993657,2.211041,-5.388849,1.229314,8.621143,-3.835123,0.695603,8.591578,-5.934617,8.140983,-3.963700,-8.612288,0.620218,5.275236,-8.011670,6.638393,-8.934119,-3.366914,0.882219,-0.277874,-7.798907,1.037348,3.469887,6.701495,-2.159740,-3.103542,-6.225273,0.580423,6.076918,-1.388929,-9.111367,4.613887,-8.834806,3.026057,9.360827,-1.283495,-0.416042,1.222998,8.527446,6.186292,5.959192,-8.983583,5.590103,8.788427,6.692130,-2.538592,-5.446991,-8.800779,6.907312,-5.817386,0.519295,-8.264363,-5.816523,-6.234695,-3.442000,4.623008,7.662523,2.653192,-5.854270,9.674342,-6.809905,1.552201,5.865320,-3.484974,1.583378,5.307414,6.750912,-3.906679,5.509491,9.055121,5.378126,-2.823794,8.003763,6.474787,-3.836584,0.289456,-9.795043,1.774869,-8.166340,-6.554935,2.153514,-8.586788,6.487275,-6.454116,6.753416,-3.256429,8.117421,-6.904873,2.131506,-9.828277,-4.861518,-6.020077,-6.045078,9.506435,8.575368,-5.815694,7.017724,-1.546311,8.031103,-3.525032,-1.984783,4.779634,2.041215,-0.155932,9.794722,-6.212897,-1.878115,-4.433000,5.841038,5.929641,7.501414,0.867344,2.939951,3.204812,-1.747133,3.811198,7.344664,-1.361908,-7.143531,7.731982,6.554888,-4.530672,-7.568987,-1.573518,-8.614770,9.609686,6.302271,-4.298698,-5.514264,-4.168430],[6.203183,2.154677,-2.052786,0.571342,3.609413,1.690067,7.121403,-2.588038,-1.403701,5.716493,3.015593,1.269310,8.315925,6.089024,5.404363,-8.603659,2.484224,7.564274,-8.710331,1.622129,3.245416,-8.815085,-2.322936,6.720356,-4.324931,2.713812,2.358518,-6.511406,-0.517438,-8.844460,7.455266,8.515009,-6.862255,6.246051,1.402077,-3.980038,5.925747,6.010487,-2.179276,-4.540593,7.157470,-7.565847,-0.586071,9.827497,-4.766985,2.551806,5.878784,-3.335602,0.050887,-1.130872,-9.669586,-8.083373,6.049641,7.876192,-0.298772,-7.317077,1.171148,-6.594963,-1.907784,9.010743,7.877955,-3.456071,8.136629,-4.375412,-2.436047,5.365006,-8.243360,-5.331358,-5.581908,3.271005,-0.392915,-5.555636,-3.130554,9.645210,0.362295,0.830418,2.577014,4.747774,-9.895860,-3.132592,-5.625945,-9.693391,9.681795,-0.686412,-7.987480,-3.452986,-5.231331,1.763922,6.286051,1.839801,8.688757,1.441361,-5.298889,5.038083,-3.314330,-7.252560,3.404311,9.910310,8.981000,-3.336238,0.056176,-2.309166,-4.799430,-6.956461,1.294162,-9.210416,-0.261041,1.772121,-2.747084,-7.271261,-5.543548,1.915984,8.828260,-7.498494,-0.715075,-0.394077,5.478768,4.967062,-7.508879,3.639730,9.096849,-0.403138,8.487577,6.941961,-9.222342,7.033022,-0.174852,7.241701,6.694123,-0.852512,-7.099601,-5.398606,-9.270903,5.601411,2.559693,-6.953878,-2.608794,5.415670,-8.331935,6.444892],[-3.513726,-5.904137,8.263767,-4.409740,2.533973,0.968100,5.717264,-3.058373,0.790032,2.612605,-2.575591,-2.912755,-5.120985,8.720990,-6.668111,-4.693570,1.276210,2.835288,-8.943201,3.210537,-7.913089,7.218410,-5.359568,1.234588,-4.000009,0.424592,-1.904181,9.515327,0.235896,-7.030205,-1.072864,-1.260134,0.898165,-9.858829,2.905314,8.147874,-2.657011,1.726659,-7.803358,0.133471,1.474488,-5.572294,-9.498837,3.620935,-1.522872,6.601363,-7.254331,-3.828076,4.046711,4.385646,-3.089358,-6.499496,1.867762,-7.966644,9.014391,-9.315138,-5.141995,-9.930052,5.020806,-2.145374,7.248764,-2.026708,5.337340,5.737686,8.851334,5.918118,-8.045360,3.787881,4.179377,8.311025,7.509320,-5.710085,-7.985514,-8.150098,-7.418314,5.758375,-9.682106,7.997089,-1.771423,-8.301502,2.304403,-9.829309,5.464064,4.081667,0.069253,4.032995,7.246262,-6.963950,0.889419,7.274138,4.995326,3.298918,-8.874661,1.906589,-5.133010,-9.319666,1.026151,8.268309,-3.927706,0.839414,9.946348,-6.083405,-1.728567,6.984722,3.116798,2.999030,4.797056,-6.478519,3.293359,9.437417,7.255409,7.640985,-7.072802,-6.671423,-0.408589,-5.550129,-7.497003,-8.835359,0.018090,-4.313423,-2.914169,9.841756,2.017109,8.325014,3.688794,-7.101429,-7.278414,9.267649,-7.500812,-9.172506,5.209376,-1.227367,8.661567,2.325809,-6.363033,-2.123566,2.970690,5.338363,0.260882,-4.229743],[2.731343,-1.098592,-6.522035,-4.741005,6.568050,5.435795,5.131262,-6.056392,-5.149686,6.132133,-2.780630,0.591441,3.502823,-3.979981,5.087464,8.400260,9.297570,1.249040,1.931688,-6.046816,-7.822199,2.937123,4.694141,-3.188194,1.212425,1.664217,4.564426,-9.107231,9.056899,-7.427897,8.845042,2.464857,8.637444,-8.805928,-1.898094,2.179370,0.077474,-3.426822,-7.289471,-3.605136,-9.725432,8.453087,1.150406,-3.122543,-5.892673,7.273021,-8.609156,-6.575583,4.724915,-0.567301,7.231762,-4.590900,-3.125287,-1.992305,-0.351418,9.428134,-5.847940,-3.711683,-3.323099,-8.750976,6.133662,-0.958634,-8.578258,9.281002,6.704511,5.323372,5.906098,4.059330,-6.556988,4.872250,0.443757,1.453922,4.486330,3.852496,-3.130307,0.281529,4.057744,3.447115,-0.991442,-4.812240,-3.198230,4.041795,6.364679,9.246495,-2.898576,-8.673880,2.182058,4.458773,-5.475966,-3.579323,-9.733360,-4.179289,8.383678,3.166665,9.963341,-2.063176,3.545647,3.982913,-3.216618,-7.263944,0.763576,-4.054028,-7.910853,-0.375801,-8.032463,0.303663,-0.247752,0.729255,4.866482,8.414322,-4.908607,-8.111510,7.796559,-0.062072,-5.193472,-5.277588,-3.437722,4.558883,-8.904665,4.106380,-3.514840,9.053225,-4.315361,0.808442,9.541620,-9.928764,-4.002837,8.395503,4.265001,4.574001,-7.389363,8.320038,6.415147,0.094427,-5.286048,-6.623470,8.703468,2.251536,-7.285758,9.350788],[-4.488927,6.509198,-4.785076,-1.646325,6.465922,-2.025645,-7.619755,-3.495756,-0.186440,1.799660,-5.751349,9.957369,-4.408256,3.738858,8.902656,-7.975992,9.218424,-9.272942,0.876553,2.674065,1.477310,-2.199467,1.792982,6.714402,7.256885,9.564965,-5.153971,1.146226,0.456922,-4.462561,-7.497240,-5.103364,-9.276758,7.633179,-7.617164,-2.852201,-7.975354,2.546427,7.619850,0.882848,4.584996,-9.552036,-3.441019,-5.757538,0.466788,-6.765799,-1.214667,6.250493,-1.288802,-8.030098,5.492933,-0.042309,2.122670,2.240915,-4.733988,0.846659,5.150162,6.052409,-6.162881,-7.014242,-4.423660,4.107509,2.734601,-7.368317,6.927493,-8.961665,2.435207,1.502652,-0.877102,-5.409978,4.200711,9.350313,2.008568,-5.136738,-3.111218,5.329850,-3.498289,5.066582,4.958645,7.040631,-4.256284,9.501710,-3.567376,7.736437,-1.604456,5.161006,6.115692,-9.283169,0.208459,-5.385643,4.141603,0.886573,-0.325971,-0.709212,-7.574170,3.300966,1.468380,-5.606953,3.992685,9.676068,4.998004,1.102306,6.661230,-1.915555,2.405766,-3.443494,-6.423405,-0.065355,0.642502,7.464661,-2.596653,-5.213721,8.050257,5.082588,-3.738057,-7.205976,2.823105,3.425494,-6.062566,9.946713,-8.206952,-5.367355,6.601420,-8.048543,6.639996,-7.924085,-9.386692,-7.339422,-5.422509,-1.568012,-4.082077,-6.997649,-0.217074,-0.239698,5.921248,-5.950229,3.460096,3.099623,7.577396,9.356936],[6.701425,-4.297711,8.563522,9.709624,-5.322839,-5.037544,9.107230,-8.785021,-7.749198,-0.166963,6.403881,-4.336821,6.204835,4.782287,9.460471,-4.209107,4.804758,-2.359114,4.052076,-5.768685,7.763492,-7.747322,1.319574,-4.732934,5.422377,-1.553393,-6.466127,4.283927,-4.634639,-6.962159,-6.370367,-9.028172,-0.716103,-9.107927,-9.151974,5.253525,4.586911,-3.456718,6.560535,0.976997,6.225302,3.286279,-5.896001,-2.317190,0.856448,-2.654218,6.801694,2.726223,6.539682,3.181080,-0.995648,7.076652,-4.904748,8.290548,-2.652590,-3.688583,-9.010409,8.254395,-0.918265,6.483001,6.754379,2.616698,-5.405954,-5.495891,-2.193825,8.092163,-5.829120,0.514916,7.953938,-4.087886,9.660748,9.574535,-6.541966,-4.112749,-9.607996,3.573581,0.981251,-8.330722,6.556427,7.247122,-1.081538,2.255840,4.459143,5.587044,3.795842,-9.140728,-4.800749,-7.718312,8.756053,-7.558801,-6.042944,9.205354,-3.865162,8.669313,-8.860315,-5.075738,6.913460,0.501384,-9.433090,4.484023,6.958772,-4.537714,-5.277345,-8.943988,2.657716,3.639683,-9.721830,6.552090,4.538342,9.047653,1.345664,-3.017426,9.212692,5.492895,2.886268,7.476565,-7.311221,-3.428144,-1.391584,-0.192775,3.706147,1.163708,-2.918923,0.487197,0.613584,8.941197,-3.624670,4.185024,-0.239915,9.969226,-1.117264,-5.619048,-7.151607,6.380469,3.324101,-7.565923,4.429118,1.963384,-4.416345,0.312087],[0.188041,-5.160909,1.903045,0.666106,-4.379655,9.882650,8.298166,0.772372,-6.540447,-6.787812,1.233506,7.103863,-0.232900,-5.050788,8.902850,-6.219099,6.721255,-2.518593,-4.193027,-1.124593,-9.535647,3.126306,2.149240,2.515094,1.473860,5.479889,-2.943770,-0.986211,9.248372,1.166255,-1.047396,2.970640,-5.478415,-3.815120,3.614124,6.848667,-3.883954,7.472851,5.813155,-9.320100,-5.023361,1.891601,-5.668147,6.155183,6.066074,-8.542627,-5.478241,5.006955,3.134105,-6.619561,-5.547000,-6.229148,-1.077957,-0.627290,-2.562356,9.048128,-5.281434,3.083951,-8.890648,9.132398,7.110699,3.484378,8.898637,-8.584483,6.271301,-8.894235,-0.786970,-5.043376,-0.886666,-5.610491,7.515871,-0.142747,6.443664,-2.801605,-5.346480,2.597588,7.671894,-5.183382,2.269302,4.946932,5.535304,-8.645261,-0.562506,-9.302714,6.015451,2.379409,-2.236637,-9.058117,7.493060,0.597572,-1.960900,8.937942,-4.763130,4.560214,-5.499149,-1.069197,-1.181500,8.688494,9.994312,3.721637,3.547503,-7.856478,-9.114372,5.744222,9.502566,-7.516942,4.894387,-9.130277,0.225812,6.667968,-9.865364,6.605276,-9.402917,-8.408411,-2.618628,-5.770357,-5.088807,-2.346861,5.625562,1.735103,-2.753252,0.694396,0.068156,2.732678,3.780552,6.476106,-8.202763,-5.279481,0.391686,1.218887,-1.602332,2.539269,-5.863773,-3.892032,2.801193,-9.101915,3.316705,9.586489,7.494052,5.012146],[7.489022,6.360418,4.593497,-0.038523,-0.043126,-9.187705,9.235846,1.680644,7.331876,-8.818039,4.204058,4.401175,-0.888054,-6.976168,5.255885,-1.237864,-1.830024,6.522561,4.257642,-8.533338,6.655034,-4.934223,7.804257,-5.000642,5.856491,3.921251,3.992419,7.171201,-9.999149,-0.152654,2.506658,-0.289210,-5.522710,5.043583,-1.981133,0.164182,0.709223,-0.924906,5.004237,7.781091,5.006011,-8.539774,9.275881,-4.759984,1.725559,-7.746894,0.479639,-5.697683,-9.536045,0.038543,1.161688,-3.633362,9.957621,4.049580,2.923664,4.269853,-6.546015,1.168024,-2.054229,5.060388,-6.059995,-4.505694,-1.833977,5.795081,2.653456,2.242795,3.563069,0.993783,4.158648,-5.905917,1.559598,2.079025,6.586625,-6.639074,6.707488,2.752774,1.245650,4.689839,-6.751600,-7.744633,-2.773001,-9.910115,3.935418,-2.273425,2.913703,5.592357,-5.672599,-1.686314,9.494819,1.585770,-2.748886,1.225302,0.021962,9.094187,8.666028,4.853344,-6.299578,-6.565424,0.333265,-2.182682,2.189480,2.572966,-9.457607,0.794786,-9.660134,-7.110738,6.897751,-1.983601,7.441145,-5.664939,1.552520,-8.545993,6.670323,5.309335,0.021047,1.680490,5.533389,-4.264330,-2.424961,-3.614997,6.494842,7.695970,-7.251805,3.455414,-4.454992,-1.935402,1.892266,6.198956,1.855983,1.359656,-3.026888,0.680707,7.237823,4.657538,1.324506,6.964200,6.382149,5.947259,-8.083966,4.865869]], dtype = "float32")#candidate|7888|(10, 140)|const|float32
call_7887 = relay.TupleGetItem(func_5332_call(relay.reshape(const_7888.astype('float32'), [10, 140])), 1)
call_7889 = relay.TupleGetItem(func_5334_call(relay.reshape(const_7888.astype('float32'), [10, 140])), 1)
output = relay.Tuple([call_7873,call_7887,const_7888,])
output2 = relay.Tuple([call_7874,call_7889,const_7888,])
func_7893 = relay.Function([], output)
mod['func_7893'] = func_7893
mod = relay.transform.InferType()(mod)
output = func_7893()
func_7894 = relay.Function([], output)
mutated_mod['func_7894'] = func_7894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5018_call = mod.get_global_var('func_5018')
func_5019_call = mutated_mod.get_global_var('func_5019')
call_7906 = func_5018_call()
call_7907 = func_5018_call()
func_3586_call = mod.get_global_var('func_3586')
func_3588_call = mutated_mod.get_global_var('func_3588')
const_7924 = relay.const([-9.706380,-3.734609,-7.577741,-1.354018,-7.797912,-8.342432], dtype = "float32")#candidate|7924|(6,)|const|float32
call_7923 = relay.TupleGetItem(func_3586_call(relay.reshape(const_7924.astype('float32'), [6,])), 2)
call_7925 = relay.TupleGetItem(func_3588_call(relay.reshape(const_7924.astype('float32'), [6,])), 2)
output = relay.Tuple([call_7906,call_7923,const_7924,])
output2 = relay.Tuple([call_7907,call_7925,const_7924,])
func_7934 = relay.Function([], output)
mod['func_7934'] = func_7934
mod = relay.transform.InferType()(mod)
output = func_7934()
func_7935 = relay.Function([], output)
mutated_mod['func_7935'] = func_7935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7968 = relay.var("var_7968", dtype = "uint32", shape = (2, 11, 6))#candidate|7968|(2, 11, 6)|var|uint32
var_7969 = relay.var("var_7969", dtype = "uint32", shape = (2, 11, 6))#candidate|7969|(2, 11, 6)|var|uint32
bop_7970 = relay.bitwise_or(var_7968.astype('uint32'), relay.reshape(var_7969.astype('uint32'), relay.shape_of(var_7968))) # shape=(2, 11, 6)
uop_7976 = relay.exp(var_7968.astype('float32')) # shape=(2, 11, 6)
output = relay.Tuple([bop_7970,uop_7976,])
output2 = relay.Tuple([bop_7970,uop_7976,])
func_7981 = relay.Function([var_7968,var_7969,], output)
mod['func_7981'] = func_7981
mod = relay.transform.InferType()(mod)
mutated_mod['func_7981'] = func_7981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7981_call = mutated_mod.get_global_var('func_7981')
var_7983 = relay.var("var_7983", dtype = "uint32", shape = (2, 11, 6))#candidate|7983|(2, 11, 6)|var|uint32
var_7984 = relay.var("var_7984", dtype = "uint32", shape = (2, 11, 6))#candidate|7984|(2, 11, 6)|var|uint32
call_7982 = func_7981_call(var_7983,var_7984,)
output = call_7982
func_7985 = relay.Function([var_7983,var_7984,], output)
mutated_mod['func_7985'] = func_7985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_7995 = relay.TupleGetItem(func_1097_call(), 0)
call_7996 = relay.TupleGetItem(func_1098_call(), 0)
func_3026_call = mod.get_global_var('func_3026')
func_3028_call = mutated_mod.get_global_var('func_3028')
call_7997 = relay.TupleGetItem(func_3026_call(), 0)
call_7998 = relay.TupleGetItem(func_3028_call(), 0)
func_7860_call = mod.get_global_var('func_7860')
func_7863_call = mutated_mod.get_global_var('func_7863')
var_8000 = relay.var("var_8000", dtype = "uint64", shape = (1, 7))#candidate|8000|(1, 7)|var|uint64
call_7999 = relay.TupleGetItem(func_7860_call(relay.reshape(var_8000.astype('uint64'), [7, 1])), 0)
call_8001 = relay.TupleGetItem(func_7863_call(relay.reshape(var_8000.astype('uint64'), [7, 1])), 0)
output = relay.Tuple([call_7995,call_7997,call_7999,var_8000,])
output2 = relay.Tuple([call_7996,call_7998,call_8001,var_8000,])
func_8006 = relay.Function([var_8000,], output)
mod['func_8006'] = func_8006
mod = relay.transform.InferType()(mod)
mutated_mod['func_8006'] = func_8006
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8007 = relay.var("var_8007", dtype = "uint64", shape = (1, 7))#candidate|8007|(1, 7)|var|uint64
func_8006_call = mutated_mod.get_global_var('func_8006')
call_8008 = func_8006_call(var_8007)
output = call_8008
func_8009 = relay.Function([var_8007], output)
mutated_mod['func_8009'] = func_8009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4397_call = mod.get_global_var('func_4397')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_8041 = relay.TupleGetItem(func_4397_call(), 0)
call_8042 = relay.TupleGetItem(func_4399_call(), 0)
output = call_8041
output2 = call_8042
func_8064 = relay.Function([], output)
mod['func_8064'] = func_8064
mod = relay.transform.InferType()(mod)
output = func_8064()
func_8065 = relay.Function([], output)
mutated_mod['func_8065'] = func_8065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5237_call = mod.get_global_var('func_5237')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_8126 = relay.TupleGetItem(func_5237_call(), 0)
call_8127 = relay.TupleGetItem(func_5239_call(), 0)
func_1250_call = mod.get_global_var('func_1250')
func_1252_call = mutated_mod.get_global_var('func_1252')
var_8156 = relay.var("var_8156", dtype = "float32", shape = (1, 364))#candidate|8156|(1, 364)|var|float32
call_8155 = relay.TupleGetItem(func_1250_call(relay.reshape(var_8156.astype('float32'), [364,])), 1)
call_8157 = relay.TupleGetItem(func_1252_call(relay.reshape(var_8156.astype('float32'), [364,])), 1)
func_3586_call = mod.get_global_var('func_3586')
func_3588_call = mutated_mod.get_global_var('func_3588')
var_8159 = relay.var("var_8159", dtype = "float32", shape = (6,))#candidate|8159|(6,)|var|float32
call_8158 = relay.TupleGetItem(func_3586_call(relay.reshape(var_8159.astype('float32'), [6,])), 2)
call_8160 = relay.TupleGetItem(func_3588_call(relay.reshape(var_8159.astype('float32'), [6,])), 2)
output = relay.Tuple([call_8126,call_8155,var_8156,call_8158,var_8159,])
output2 = relay.Tuple([call_8127,call_8157,var_8156,call_8160,var_8159,])
func_8163 = relay.Function([var_8156,var_8159,], output)
mod['func_8163'] = func_8163
mod = relay.transform.InferType()(mod)
mutated_mod['func_8163'] = func_8163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8163_call = mutated_mod.get_global_var('func_8163')
var_8165 = relay.var("var_8165", dtype = "float32", shape = (1, 364))#candidate|8165|(1, 364)|var|float32
var_8166 = relay.var("var_8166", dtype = "float32", shape = (6,))#candidate|8166|(6,)|var|float32
call_8164 = func_8163_call(var_8165,var_8166,)
output = call_8164
func_8167 = relay.Function([var_8165,var_8166,], output)
mutated_mod['func_8167'] = func_8167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3210_call = mod.get_global_var('func_3210')
func_3211_call = mutated_mod.get_global_var('func_3211')
call_8174 = func_3210_call()
call_8175 = func_3210_call()
output = call_8174
output2 = call_8175
func_8176 = relay.Function([], output)
mod['func_8176'] = func_8176
mod = relay.transform.InferType()(mod)
mutated_mod['func_8176'] = func_8176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8176_call = mutated_mod.get_global_var('func_8176')
call_8177 = func_8176_call()
output = call_8177
func_8178 = relay.Function([], output)
mutated_mod['func_8178'] = func_8178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6911_call = mutated_mod.get_global_var('func_6911')
call_8250 = relay.TupleGetItem(func_6909_call(), 1)
call_8251 = relay.TupleGetItem(func_6911_call(), 1)
func_2700_call = mod.get_global_var('func_2700')
func_2703_call = mutated_mod.get_global_var('func_2703')
const_8278 = relay.const([3.580091,2.988129,4.422150,4.145050,6.498219,9.412919,-6.014234,5.146899,3.296581,-3.917725,-8.669775,6.536361,5.832393,7.844528,9.240395,9.722782,-2.310466,5.534696,-9.345505,4.795734,-7.159357,6.651595,9.837247,9.496126,-3.258796,-4.693622,-4.861781,3.229646,-7.580972,-1.422455,-0.903100,-0.934470,-1.260398,-1.385451,-6.047424,-6.503355,-4.274682,9.228579,-8.977386,-9.014145,7.107159,-8.866228,-0.033501,6.454672,-0.339883,8.640057,7.315774,7.499555,8.266404,-3.259960,6.918514,-2.423168,-7.685422,0.421159,-4.558467,5.123587,-2.497741,6.539719,-6.566607,8.973730,-3.639491,6.718416,3.394215,9.243883,-2.100482,-9.941485,-8.033810,2.400943,6.537705,-2.111331,5.069744,9.597710,7.809574,-5.954317,9.078633,-7.508240,-4.913130,7.787758,-3.591023,-0.758719,-5.051562,-7.798915,0.854112,1.846473,0.099720,-5.653730,-8.903556,-5.611478,-9.550357,2.751634,0.443945,5.746987,6.631990,4.544804,8.052736,-9.511573,-7.096772,6.866620,-7.343838,-4.516934,-4.883724,-0.651367,-9.734565,-5.103369,-9.017700,-8.772527,0.716904,4.246211,-9.084741,-9.290052,4.969467,7.228752,4.844694,6.900608,-3.563742,8.602517,7.709561,0.617621,0.160227,-1.431737,2.609379,1.167851,6.890792,6.804064,1.830319,2.852227,-4.867799,-1.368737,1.952108,5.885883,-9.342141,-6.139124,8.633239,9.370007,0.035090,-2.866960,4.133326,8.427048,-2.292847,-1.183166,-8.289152,-3.764197,2.831958,3.925743,7.846543,-1.489435,8.180280,3.638434,-2.313149,0.966290,-9.053833,-4.590854,9.793151,-4.838323,-0.230655,4.059213,1.876314,7.195705,5.141662,7.870247,9.913465,-6.408201,8.335743,1.190589,-2.601651,0.172838,-3.905563,-5.017141,-3.942578,-7.448510,-3.094245,9.251715,2.250916,-1.968462,1.152821,0.045500,0.549112,-4.854526,2.903362,-2.852681,-9.152928,1.147604,0.110529,0.389400,-3.093365,-7.263145,2.687639,-6.954640,-8.377304,0.253569,1.926816,-8.426976,-7.024793,1.183823,1.071258,-9.875779,9.906223,-9.770411,4.669398,-6.207289,2.357581,-6.969793,6.318756,-4.284069,2.909894,2.252149,-5.625595,6.682738,-0.276114,6.384618,-1.914520,-1.307698,6.050003,-5.961793,-3.853259,-6.958592], dtype = "float64")#candidate|8278|(216,)|const|float64
call_8277 = relay.TupleGetItem(func_2700_call(relay.reshape(const_8278.astype('float64'), [9, 8, 3])), 0)
call_8279 = relay.TupleGetItem(func_2703_call(relay.reshape(const_8278.astype('float64'), [9, 8, 3])), 0)
output = relay.Tuple([call_8250,call_8277,const_8278,])
output2 = relay.Tuple([call_8251,call_8279,const_8278,])
func_8315 = relay.Function([], output)
mod['func_8315'] = func_8315
mod = relay.transform.InferType()(mod)
mutated_mod['func_8315'] = func_8315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8315_call = mutated_mod.get_global_var('func_8315')
call_8316 = func_8315_call()
output = call_8316
func_8317 = relay.Function([], output)
mutated_mod['func_8317'] = func_8317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8064_call = mod.get_global_var('func_8064')
func_8065_call = mutated_mod.get_global_var('func_8065')
call_8354 = func_8064_call()
call_8355 = func_8064_call()
output = relay.Tuple([call_8354,])
output2 = relay.Tuple([call_8355,])
func_8390 = relay.Function([], output)
mod['func_8390'] = func_8390
mod = relay.transform.InferType()(mod)
output = func_8390()
func_8391 = relay.Function([], output)
mutated_mod['func_8391'] = func_8391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7190_call = mod.get_global_var('func_7190')
func_7192_call = mutated_mod.get_global_var('func_7192')
call_8404 = relay.TupleGetItem(func_7190_call(), 0)
call_8405 = relay.TupleGetItem(func_7192_call(), 0)
func_6823_call = mod.get_global_var('func_6823')
func_6827_call = mutated_mod.get_global_var('func_6827')
const_8424 = relay.const([-2.397567,3.717474,-1.067879,3.629164,-4.997654,5.588044,2.252212,-1.798311,7.736939,-7.377158,-9.395653,1.157255,-5.984011,-7.195255,1.816190,6.485591,4.288846,0.999079,-9.329394,-7.501130,2.426034,-8.816871,9.580390,-7.058390,3.323804,2.119690,1.225552,-2.742093,0.147342,6.610103,4.217930,3.394646,-4.065747,-1.654527,1.730750,5.914259,2.119033,-6.773712,-0.454042,4.897287,3.260798,7.178502,9.823917,-4.026578,2.830962,5.364575,3.185463,7.327485,5.954324,-0.468894,-9.737340,3.240614,0.525816,9.497002,-7.900011,3.821328,4.900464,5.950571,8.319435,-8.700617,6.614020,9.376245,-4.003266,-2.738480,-3.485099,-6.014735,-7.448938,-4.502066,9.865392,0.957249,-3.363801,8.597839,-8.156269,-5.974570,4.725034,-8.077536,-6.848751,5.296550,-7.677809,-1.433657,-1.849953,-2.952422,-2.721857,9.036652,-7.107623,-0.139856,5.365385,-9.258128,-2.329916,5.944107,3.388556,-8.615896,5.861943,-7.758761,-3.905502,9.819964,-6.106101,9.196076,-1.196006,-0.862729,-9.759680,-5.430252,0.020698,0.058495,9.123269,3.269349,-2.023348,1.027837,5.311188,5.602215,-6.544053,-4.170232,-7.433748,-9.159218,-6.017984,7.025318,6.491055,2.133677,9.728849,-6.658318,1.830537,7.272490,3.701214,-0.487946,1.919724,-7.801792,-1.768475,-7.544818,2.047881,3.330522,4.547214,-0.925767,-1.868459,5.285724,-7.087261,0.084100,8.913521,8.956071,6.693091,4.568599,6.860073,-0.368912,0.720699,5.841661,9.694143,-0.114919,8.084070,2.465453,-4.971141,5.259934,-1.656078,5.302318,-0.230734,2.122463,-6.264886,-5.838101,-4.019309,2.227687,1.873635,-2.734582,5.305067,9.154097,9.488218,5.432501,-3.705012,-6.842877,2.368676,-5.901144,-8.953357,5.580933,6.988441,1.736573,-6.036515,2.526817,5.030859,8.202468,-7.508087,9.606614,3.634186,-2.316744,-6.408465,0.785079,-3.062707,3.805841,9.948190,7.475160,-2.257037,-8.746480,6.706656,-5.514304,-0.144433,3.085533,-9.560076,-8.271788,5.493013,4.577897,-2.469231,1.670816,8.238337,7.327391,3.410561,4.916558,7.663831,0.413106,1.071750,0.373104,0.024402,-7.600714,-2.619952,8.900998,4.596129,3.356881,7.243639,-5.206828,1.111059,4.046631,-4.412332,-7.512179,6.227590,-6.284643,7.815068,-1.469308,2.177891,-0.088415,2.015792,9.949730,1.825053,-8.690334,-9.800589,2.760347,6.768303,-6.611216,8.316420,5.776002,-0.476857,0.194493,-1.447862,-8.281892,-4.284690,4.799129,8.322035,8.168826,8.073693,8.365483,-9.692214,6.306563,-3.769554,-7.654915,-1.340392,-0.103295,5.141323,-2.801076,8.684489,0.911257,8.718959,1.328484,-7.342284,3.613835,1.011701,1.872457,8.613653,1.363356,-0.989045,7.213645,0.881825,-5.730174,5.369041,-6.774397,8.512192,0.183000,-3.471421,5.465507,2.189074,-2.827009,-1.809727,-2.656316,-3.707575,3.252382,7.213760,2.632812,-0.057277,-6.942724,-7.511464,-6.545256,-8.579974,1.574980,-2.109601,0.885252,8.661916,-6.732715,5.477565,-7.386646,-0.356528,1.426079,-8.016869,8.204294,-4.051342,0.366463,-6.506623,-8.885801,0.389996,-9.397137,3.417481,8.341867,3.895517,-1.422076,-3.694420,6.789587,-7.849388,9.439295,6.976621,2.504436,-6.508304,6.999778,-1.318763,3.606492,8.041631,3.965432,-1.982325,9.014085,0.943739,-3.491887,-6.308468,-7.935351,-6.843745,-4.698504,-8.155157,3.252819,-3.178584,-4.653300,0.467588,-2.509648,0.448956,7.203589,-9.410697,5.324071,-9.871626,1.337065,9.034294,2.432143,0.075801,-8.564656,3.581220,-0.050178,-7.197418,-6.164188,8.669980,-3.633397,-2.560555,-1.214164,-9.052562,-4.909364,8.968247,-9.396660,-8.694381,7.275699,8.361263,0.732309,5.867555,-7.782383,-6.504998,9.072631,6.440825,-9.779035,4.507683,-1.456354,9.928231,-3.127205,-1.228083,1.317035,-3.498429,0.682629,-8.699568,-2.958771,-0.938301,4.579103,0.952133,-7.536314,-8.317074,1.457005,1.870162,-6.214103,-5.076792,-6.845271,5.410542,9.927916,-4.540494,3.096589,-9.015183,-6.263382,-6.201426,1.533303,3.791916,-4.311644,0.112063,9.811527,0.287428,1.015945,9.076031,-4.046925,4.756711,-8.026690,-8.831405,6.172086,-7.506990,-4.927195,6.811202,-9.525063,6.531535,7.828722,-9.576891,-0.374548,-1.176671,-7.034256,8.438697,-4.422186,-7.404568,-7.008935,-0.971620,7.488987,7.581256,8.101243,-2.514552,0.439799,-1.323320,-0.373557,-7.167126,-6.762629,-4.587520,-3.750299,1.471070,-9.256350,6.220691,5.426340,-8.849049,-2.180193,-3.688156,4.098449,-4.278100,-0.337600,9.683448,4.132156,0.816131,-5.480573,-4.919127,5.932758,3.106402,-8.182400,-9.123665,-5.836715,-5.919859,8.055392,-2.057514,4.244806,7.878092,3.193528,-9.890572,-3.391215,-9.410736,2.649336,6.698233,-9.044752,7.696991,-9.090991,-1.127212,-5.004545,5.448761,2.675249,-1.840778,-4.904812,6.770487,-2.144298,6.999022,9.816069,3.445800,-4.322831,-4.291455,7.709848,7.573114,2.184537,-7.988230,5.869323,0.229226,8.400821,7.530745,-2.962157,6.234404,9.223578,7.063639,-9.924178,7.066305,-3.135452,-1.213848,3.119221,9.697487,8.739571,1.889855,7.698887,-1.269805,-4.829899,7.557894,-0.422056,-4.900748,3.416184,-1.329839,-3.386079,-8.270110,3.250829,5.993475,2.776508,-1.130171,-4.307084], dtype = "float32")#candidate|8424|(512,)|const|float32
call_8423 = relay.TupleGetItem(func_6823_call(relay.reshape(const_8424.astype('float32'), [4, 16, 8]), relay.reshape(const_8424.astype('float32'), [4, 16, 8]), ), 0)
call_8425 = relay.TupleGetItem(func_6827_call(relay.reshape(const_8424.astype('float32'), [4, 16, 8]), relay.reshape(const_8424.astype('float32'), [4, 16, 8]), ), 0)
uop_8441 = relay.sigmoid(const_8424.astype('float32')) # shape=(512,)
bop_8451 = relay.greater(uop_8441.astype('bool'), relay.reshape(const_8424.astype('bool'), relay.shape_of(uop_8441))) # shape=(512,)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_8454 = relay.TupleGetItem(func_3161_call(), 0)
call_8455 = relay.TupleGetItem(func_3162_call(), 0)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_8461 = func_1116_call()
call_8462 = func_1116_call()
func_2083_call = mod.get_global_var('func_2083')
func_2085_call = mutated_mod.get_global_var('func_2085')
call_8467 = relay.TupleGetItem(func_2083_call(), 1)
call_8468 = relay.TupleGetItem(func_2085_call(), 1)
uop_8471 = relay.log2(bop_8451.astype('float32')) # shape=(512,)
func_1422_call = mod.get_global_var('func_1422')
func_1426_call = mutated_mod.get_global_var('func_1426')
var_8474 = relay.var("var_8474", dtype = "float64", shape = (1, 2640))#candidate|8474|(1, 2640)|var|float64
call_8473 = relay.TupleGetItem(func_1422_call(relay.reshape(var_8474.astype('float64'), [16, 15, 11]), relay.reshape(var_8474.astype('float32'), [16, 15, 11]), ), 2)
call_8475 = relay.TupleGetItem(func_1426_call(relay.reshape(var_8474.astype('float64'), [16, 15, 11]), relay.reshape(var_8474.astype('float32'), [16, 15, 11]), ), 2)
output = relay.Tuple([call_8404,call_8423,call_8454,call_8461,call_8467,uop_8471,call_8473,var_8474,])
output2 = relay.Tuple([call_8405,call_8425,call_8455,call_8462,call_8468,uop_8471,call_8475,var_8474,])
func_8476 = relay.Function([var_8474,], output)
mod['func_8476'] = func_8476
mod = relay.transform.InferType()(mod)
mutated_mod['func_8476'] = func_8476
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8477 = relay.var("var_8477", dtype = "float64", shape = (1, 2640))#candidate|8477|(1, 2640)|var|float64
func_8476_call = mutated_mod.get_global_var('func_8476')
call_8478 = func_8476_call(var_8477)
output = call_8478
func_8479 = relay.Function([var_8477], output)
mutated_mod['func_8479'] = func_8479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2687_call = mod.get_global_var('func_2687')
func_2688_call = mutated_mod.get_global_var('func_2688')
call_8489 = relay.TupleGetItem(func_2687_call(), 0)
call_8490 = relay.TupleGetItem(func_2688_call(), 0)
func_8163_call = mod.get_global_var('func_8163')
func_8167_call = mutated_mod.get_global_var('func_8167')
var_8492 = relay.var("var_8492", dtype = "float32", shape = (364,))#candidate|8492|(364,)|var|float32
var_8493 = relay.var("var_8493", dtype = "float32", shape = (6,))#candidate|8493|(6,)|var|float32
call_8491 = relay.TupleGetItem(func_8163_call(relay.reshape(var_8492.astype('float32'), [1, 364]), relay.reshape(var_8493.astype('float32'), [6,]), ), 1)
call_8494 = relay.TupleGetItem(func_8167_call(relay.reshape(var_8492.astype('float32'), [1, 364]), relay.reshape(var_8493.astype('float32'), [6,]), ), 1)
output = relay.Tuple([call_8489,call_8491,var_8492,var_8493,])
output2 = relay.Tuple([call_8490,call_8494,var_8492,var_8493,])
func_8498 = relay.Function([var_8492,var_8493,], output)
mod['func_8498'] = func_8498
mod = relay.transform.InferType()(mod)
mutated_mod['func_8498'] = func_8498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8498_call = mutated_mod.get_global_var('func_8498')
var_8500 = relay.var("var_8500", dtype = "float32", shape = (364,))#candidate|8500|(364,)|var|float32
var_8501 = relay.var("var_8501", dtype = "float32", shape = (6,))#candidate|8501|(6,)|var|float32
call_8499 = func_8498_call(var_8500,var_8501,)
output = call_8499
func_8502 = relay.Function([var_8500,var_8501,], output)
mutated_mod['func_8502'] = func_8502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_601_call = mod.get_global_var('func_601')
func_603_call = mutated_mod.get_global_var('func_603')
call_8519 = relay.TupleGetItem(func_601_call(), 0)
call_8520 = relay.TupleGetItem(func_603_call(), 0)
func_3450_call = mod.get_global_var('func_3450')
func_3453_call = mutated_mod.get_global_var('func_3453')
var_8529 = relay.var("var_8529", dtype = "float64", shape = (234,))#candidate|8529|(234,)|var|float64
const_8530 = relay.const([4.262398,-1.296314,-1.878821,-0.055663,-9.835955,-9.872514,-7.032101,6.770917,0.181347,-5.159859,-1.800257,-1.448897,9.588289,2.879922,9.696787,-6.759154,1.119078,7.543708,-0.370161,-5.208268,5.600754,1.292888,0.235541,-3.973774,6.451580,-2.529372,-4.128799,-5.697806,-3.541105,9.936373,-8.596838,3.152750,-0.601861,-2.335784,-0.282259,2.193368,5.979765,8.694798,2.840739,9.441482,-1.486306,-3.589499,-5.247843,-9.730544,2.939452,-8.502788,-2.472190,5.569303,-8.778443,2.584664,-5.387673,-0.660612,-1.981253,-9.684694,9.498945,-6.998560,8.042214,7.403926,1.853038,-3.810596,3.528665,8.221033,-6.717895,-5.289977,-3.166591,2.115600,-9.144874,-2.339212,7.331867,-9.823382,-2.736418,-7.445866,-4.554853,6.940176,-1.259611,-5.696256,4.155775,0.514979,-1.821990,-5.657997,5.557177,9.193550,-5.087660,-9.968803,-6.818604,-2.399338,9.861101,-3.442029,-8.845927,-1.260019,1.898339,-6.508053,-5.303464,8.086658,7.239596,5.254180,9.365925,-2.113074,-6.481560,-5.993693,-3.257672,2.630751,1.271097,7.272024,2.417193,-4.896712,-7.969265,1.298337,-3.033496,8.030654,2.106956,7.048447,7.324101,-5.288667,-8.817785,-9.986887,4.048263,2.924700,2.772817,1.435218,-6.916254,4.587204,-8.637382,4.979522,2.637486,8.261074,0.515264,-0.035180,-2.380322,-2.599553,8.245472,5.445890,-6.038830,4.776679,7.724890,-0.534433,9.278550,-5.875075,0.850547,-6.902207,-9.845198,1.874095,-4.835296,-1.316050,-1.132879,-3.813170,0.168907,-0.114483,-2.588120,8.333751,-9.660425,4.248573,-3.516181,-8.367159,5.227097,-3.188638,-7.123524,2.342657,4.377673,2.787733,-7.103844,8.687140,-0.052265,8.169740,-8.168098,-9.129193,-5.168735,-5.343394,-4.997095,-0.384244,8.479573,9.482618,-8.245591,5.507057,2.593016,8.671995,-9.716001,5.440201,7.624353,3.686411,-8.407990,-9.879124,1.892326,6.940325,6.848450,2.169949,-5.035704,-6.754914,3.713400,9.559310,3.681328,-0.004679,9.617859,-2.887551,-3.398335,-5.438310,0.809945,5.999030,6.381444,-8.673267,8.527856,-8.196369,7.815061,-3.252037,-9.764573,6.594535,0.932338,1.812752,3.273307,1.866497,7.858473,-2.258836,-8.264887,3.711322,-2.437155,9.463881,2.630982,-8.637292,-6.513671,3.657387,-5.767055,-8.009461,-2.140428,-8.611043,8.327518,9.996783,-6.223860,-6.473265,3.832027,-0.707042,4.011992,4.622751,8.637915,0.850503,0.617031,-4.286351,2.045923,3.133392,-3.422208,-3.361224,3.828391,-4.354541,0.063258,-9.998308,-6.470238,2.124971,-2.702144,-3.286236,-1.502828,-3.437146,-3.468856,1.978194,3.938769,6.372153,-2.861010,-4.134342,9.616382,1.964042,3.746624,-9.102759,0.428704,1.609428,-3.674573,3.021080,-1.803777,-6.040643,7.922818,-8.025931,-4.439014,-4.563265,9.191348,-0.890315,-8.845716,-3.362918,-6.194249,8.543983,-4.590679,4.819230,3.513832,2.157192,-6.066406,-4.172599,0.842505,4.776732,5.765560,-1.482373,-3.221497,4.014888,9.957555,-2.709552,-8.747971,9.145484,-1.143683,-2.453385,4.441266,6.453838,9.084735,9.111972,2.331078,7.972074,5.095888,2.829513,-5.595659,-4.250825,-2.268321,3.274186,-1.074736,6.754149,-3.240463,-9.258782,1.080089,3.148251,-6.800921,4.666271,0.838455,-1.243784,1.369411,-2.238519,-4.987869,7.809339,7.003696,-1.872057,7.430506,4.419540,8.131507,2.860220,7.428731,7.145593,-2.001090,0.444325,7.917378,-3.522857,-3.497883,4.606422,0.151913,3.628882,8.284330,-2.458325,-8.233939,-5.592241,-4.701772,-8.309671,1.036903,7.261294,2.934473,9.538068,-7.410511,3.558038,0.763852,4.803558,3.695458,5.312079,-8.049729,2.872213,3.050723,-6.231303,5.407496,-8.450202,6.915905,-5.525933,-7.397340,6.946256,1.993866,8.691881], dtype = "float32")#candidate|8530|(364,)|const|float32
call_8528 = relay.TupleGetItem(func_3450_call(relay.reshape(var_8529.astype('float64'), [2, 13, 9]), relay.reshape(const_8530.astype('float32'), [1, 364]), ), 4)
call_8531 = relay.TupleGetItem(func_3453_call(relay.reshape(var_8529.astype('float64'), [2, 13, 9]), relay.reshape(const_8530.astype('float32'), [1, 364]), ), 4)
func_7470_call = mod.get_global_var('func_7470')
func_7471_call = mutated_mod.get_global_var('func_7471')
call_8535 = func_7470_call()
call_8536 = func_7470_call()
output = relay.Tuple([call_8519,call_8528,var_8529,const_8530,call_8535,])
output2 = relay.Tuple([call_8520,call_8531,var_8529,const_8530,call_8536,])
func_8538 = relay.Function([var_8529,], output)
mod['func_8538'] = func_8538
mod = relay.transform.InferType()(mod)
var_8539 = relay.var("var_8539", dtype = "float64", shape = (234,))#candidate|8539|(234,)|var|float64
output = func_8538(var_8539)
func_8540 = relay.Function([var_8539], output)
mutated_mod['func_8540'] = func_8540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_8566 = func_3977_call()
call_8567 = func_3977_call()
func_8006_call = mod.get_global_var('func_8006')
func_8009_call = mutated_mod.get_global_var('func_8009')
var_8593 = relay.var("var_8593", dtype = "uint64", shape = (7,))#candidate|8593|(7,)|var|uint64
call_8592 = relay.TupleGetItem(func_8006_call(relay.reshape(var_8593.astype('uint64'), [1, 7])), 0)
call_8594 = relay.TupleGetItem(func_8009_call(relay.reshape(var_8593.astype('uint64'), [1, 7])), 0)
func_364_call = mod.get_global_var('func_364')
func_366_call = mutated_mod.get_global_var('func_366')
call_8601 = func_364_call()
call_8602 = func_364_call()
output = relay.Tuple([call_8566,call_8592,var_8593,call_8601,])
output2 = relay.Tuple([call_8567,call_8594,var_8593,call_8602,])
func_8612 = relay.Function([var_8593,], output)
mod['func_8612'] = func_8612
mod = relay.transform.InferType()(mod)
var_8613 = relay.var("var_8613", dtype = "uint64", shape = (7,))#candidate|8613|(7,)|var|uint64
output = func_8612(var_8613)
func_8614 = relay.Function([var_8613], output)
mutated_mod['func_8614'] = func_8614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_8648 = relay.TupleGetItem(func_5190_call(), 0)
call_8649 = relay.TupleGetItem(func_5191_call(), 0)
output = call_8648
output2 = call_8649
func_8658 = relay.Function([], output)
mod['func_8658'] = func_8658
mod = relay.transform.InferType()(mod)
output = func_8658()
func_8659 = relay.Function([], output)
mutated_mod['func_8659'] = func_8659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5688_call = mod.get_global_var('func_5688')
func_5689_call = mutated_mod.get_global_var('func_5689')
call_8678 = relay.TupleGetItem(func_5688_call(), 0)
call_8679 = relay.TupleGetItem(func_5689_call(), 0)
const_8688 = relay.const([[[-3.716061,5.494127,6.069462,-5.933958,-4.772114,-5.949059,7.571941,-3.604574],[0.374098,6.902862,-0.819025,-0.628916,4.786598,-4.039430,-6.653583,8.493044],[7.458011,9.534244,-5.304366,2.368184,-9.889526,-7.593386,-5.296045,9.548384],[-8.412519,-5.300983,0.613712,-1.778753,0.532765,6.121401,-8.474791,-9.647587],[9.421658,9.011936,-6.497808,-7.937744,-5.291563,-9.044492,0.249661,-8.004621],[8.593276,-2.029969,-5.828040,6.099904,-6.316277,2.589342,4.944520,-1.349582],[5.136041,8.237964,5.336652,-8.083165,-2.044583,-5.321741,0.900180,9.516388],[9.800915,2.820949,-1.328500,-3.175725,6.875644,4.881065,1.651233,5.151424],[6.997034,-5.659222,4.656282,-0.100575,-5.305062,6.314529,-3.000568,-6.166097],[4.210153,4.332625,-2.232377,-5.829711,9.667924,-1.157737,9.697519,-7.686108],[-6.065574,3.033646,9.689805,5.036497,-4.968070,5.279878,1.297343,1.137488]],[[6.110167,-3.172162,-0.902990,0.959356,2.050687,-2.162606,-0.676640,6.677081],[-0.263706,-5.706343,4.136556,1.592200,-8.939677,-4.772121,-8.927383,-3.057048],[-9.624500,8.674576,5.744216,-9.878389,-8.118029,-8.215248,4.285540,-9.239067],[-3.795076,-7.626896,-2.180053,-1.723037,-8.512713,1.308784,-8.206163,0.640456],[-0.092318,6.296727,8.194011,-1.074225,-0.898942,-0.761444,2.842295,6.807289],[9.115298,5.894911,5.459955,4.363048,-6.003541,-2.188794,-5.863621,0.742104],[-1.477059,8.954662,-9.734306,-5.478399,-9.494159,9.681970,9.385826,5.472369],[-1.190403,-4.159425,-8.617453,0.988942,-7.460798,1.022209,0.555553,-2.960060],[3.143832,-5.709242,0.113328,0.381115,1.048421,9.631543,7.155351,-7.966830],[9.439758,-4.717175,-1.914919,-2.201430,0.339621,5.273539,-9.444630,7.169247],[4.529975,-4.919063,-4.561207,-4.822815,-7.439370,-8.202656,7.373784,3.803303]],[[6.028761,-4.203119,3.628995,6.338279,5.326653,-9.493684,-7.480145,1.504145],[1.875198,-8.541547,0.954782,7.270477,9.044619,-9.270819,-1.069830,3.716974],[1.996183,4.062381,7.787590,1.536198,-7.944148,-1.331783,2.031860,-6.594245],[8.366989,-0.782362,-1.717749,-0.478267,9.113804,-3.041652,-7.388307,-4.369869],[8.511340,5.927100,-5.410874,7.052088,-8.884175,4.308180,-8.155841,-0.671395],[-9.071448,-6.423437,-2.614544,-4.740322,7.072339,-5.726488,4.298416,2.827447],[-6.272504,7.664200,-6.203913,2.423205,-8.798719,-0.618463,8.958209,5.064821],[-0.817120,-2.233560,-4.504109,-1.715150,5.508210,-6.203433,2.478168,2.948028],[-9.076330,-2.359992,-0.571947,0.105192,-9.673575,5.277187,-2.957837,-6.124558],[-9.717149,6.618378,1.501516,5.992774,-9.649921,1.433340,0.844543,-9.242461],[4.081833,-5.394340,-8.669013,3.589583,-5.218057,-3.712408,7.989140,1.970667]],[[8.762596,-6.590134,-7.558890,0.931559,3.516090,2.900634,-5.099773,-1.104236],[-0.314914,9.180042,-4.041407,-8.013275,5.280875,0.346638,1.461473,-6.775265],[-9.943080,5.368416,-6.629012,3.954980,-6.972960,3.978804,-1.624405,-3.228489],[-2.882166,-7.945995,-5.695673,0.652892,8.970678,-8.326725,0.123395,-5.673749],[-8.269450,4.968748,-0.440702,-4.132075,0.423381,9.884171,-2.004022,-0.877184],[5.039048,7.444053,2.730556,9.518439,-2.160150,1.442866,1.225531,3.400103],[-2.780233,-5.705742,4.350216,8.428018,-9.613013,6.377706,-1.891091,-9.984142],[-0.993598,-9.142246,-2.706142,-3.092650,3.142220,0.852223,0.372646,-4.484015],[9.911658,0.585646,-2.110058,6.721284,3.146341,5.544757,-5.813570,-7.446587],[2.203015,7.979815,-3.513253,-0.453509,0.335053,-6.840740,-6.517890,-0.654014],[-9.193520,3.658946,-4.331438,9.864175,7.678981,-6.588301,-0.091289,-6.829794]],[[0.095491,-6.963279,0.631492,1.448570,-7.051322,-0.668563,7.174538,-7.807053],[-1.079069,-4.025222,-7.510420,-1.680312,-9.110013,6.360805,8.781853,-4.094277],[0.499430,5.279907,-1.681613,-3.062891,-5.571228,6.219379,1.968257,7.475889],[1.034685,4.606840,-9.858707,0.799317,-0.171481,3.687558,-3.744457,-8.016269],[-2.353309,7.338410,-3.267592,4.853122,-6.323229,-0.097668,-2.921426,9.339972],[7.439116,4.523898,-5.200644,-1.440392,-7.287027,3.271814,-8.636867,-9.598327],[0.666689,1.638785,7.189831,-8.342934,5.713587,-9.683428,7.094177,-6.139242],[-6.953971,-7.480665,-4.078385,5.347692,-6.823938,-1.559039,-2.708566,-1.851824],[-5.836277,1.916854,-3.910694,1.216518,8.776046,-6.232788,9.576370,2.236147],[-1.220235,-6.360783,2.421515,5.186830,-6.532318,-5.409519,1.866052,-4.245167],[-7.075077,3.764788,-4.790700,-6.362658,-6.005471,-4.212444,9.594859,6.730290]],[[6.626574,5.156856,4.890856,-2.188895,-1.753335,-9.598435,4.202635,8.209541],[0.659174,5.916255,4.696021,4.028363,-5.140813,6.805779,7.806423,0.378809],[-9.978280,9.532601,-4.955930,-9.530072,-0.466895,-1.158804,3.591878,5.247065],[-7.603863,-6.695551,7.600907,-2.698629,4.497305,5.901379,-7.202018,1.222885],[9.945824,7.195540,2.945118,-8.643741,-5.513192,7.764508,-0.156754,-1.561038],[1.405104,-3.393415,-8.004888,-4.532564,-5.337494,8.608565,3.129931,-9.638651],[3.338444,-5.550061,9.387652,4.866734,7.056418,9.478057,0.573377,-3.196648],[2.361115,2.277696,1.118319,5.583071,-9.198504,0.719239,-8.771007,-7.400603],[8.002966,-0.917218,-0.231720,-6.382625,-7.113834,2.677849,-6.024254,3.646533],[8.308115,0.670569,-5.634069,-5.165737,0.388311,-2.227208,0.647112,-8.515376],[3.872685,1.998161,-9.940639,2.725085,-9.397847,-4.150871,1.347487,-1.268097]],[[3.527337,3.598398,-7.875322,-0.629340,9.056944,5.555000,8.459874,9.067157],[-1.364444,-9.399910,6.470811,-8.345061,0.879214,-5.872220,-7.631442,7.812224],[-7.016938,7.246841,-0.210551,2.625685,3.150248,4.392858,-3.949016,5.545649],[9.005257,3.091135,-9.734031,-9.592365,-1.664001,-7.693137,3.882826,-5.013881],[-6.204215,0.727808,4.377000,2.021094,9.673459,-8.775756,5.980789,6.345063],[2.274631,8.195917,-9.368554,7.490420,-6.478311,9.675288,5.243986,-2.049681],[9.192674,0.590278,-0.481138,6.871393,7.112864,6.099272,-8.726463,0.674511],[7.001150,4.843843,7.464109,-6.140745,-8.277489,9.546513,-2.932347,2.497456],[6.383431,-1.756353,2.276810,-6.578513,0.099800,-6.776167,-9.841287,-5.869025],[-4.141088,1.052998,-1.231778,-0.064405,6.123657,0.158031,2.582319,1.003754],[6.865908,-1.452105,-0.178014,8.915128,-3.795495,4.344735,1.541694,-9.964286]]], dtype = "float32")#candidate|8688|(7, 11, 8)|const|float32
bop_8689 = relay.logical_xor(call_8678.astype('uint8'), relay.reshape(const_8688.astype('uint8'), relay.shape_of(call_8678))) # shape=(7, 11, 8)
bop_8692 = relay.logical_xor(call_8679.astype('uint8'), relay.reshape(const_8688.astype('uint8'), relay.shape_of(call_8679))) # shape=(7, 11, 8)
output = relay.Tuple([bop_8689,])
output2 = relay.Tuple([bop_8692,])
func_8705 = relay.Function([], output)
mod['func_8705'] = func_8705
mod = relay.transform.InferType()(mod)
mutated_mod['func_8705'] = func_8705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8705_call = mutated_mod.get_global_var('func_8705')
call_8706 = func_8705_call()
output = call_8706
func_8707 = relay.Function([], output)
mutated_mod['func_8707'] = func_8707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5018_call = mod.get_global_var('func_5018')
func_5019_call = mutated_mod.get_global_var('func_5019')
call_8732 = func_5018_call()
call_8733 = func_5018_call()
func_5607_call = mod.get_global_var('func_5607')
func_5608_call = mutated_mod.get_global_var('func_5608')
call_8748 = relay.TupleGetItem(func_5607_call(), 0)
call_8749 = relay.TupleGetItem(func_5608_call(), 0)
output = relay.Tuple([call_8732,call_8748,])
output2 = relay.Tuple([call_8733,call_8749,])
func_8759 = relay.Function([], output)
mod['func_8759'] = func_8759
mod = relay.transform.InferType()(mod)
output = func_8759()
func_8760 = relay.Function([], output)
mutated_mod['func_8760'] = func_8760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3312_call = mod.get_global_var('func_3312')
func_3314_call = mutated_mod.get_global_var('func_3314')
call_8769 = relay.TupleGetItem(func_3312_call(), 0)
call_8770 = relay.TupleGetItem(func_3314_call(), 0)
func_8163_call = mod.get_global_var('func_8163')
func_8167_call = mutated_mod.get_global_var('func_8167')
var_8816 = relay.var("var_8816", dtype = "float32", shape = (1, 364))#candidate|8816|(1, 364)|var|float32
const_8817 = relay.const([-7.179200,-3.013237,5.259794,2.988718,-9.836057,4.134504], dtype = "float32")#candidate|8817|(6,)|const|float32
call_8815 = relay.TupleGetItem(func_8163_call(relay.reshape(var_8816.astype('float32'), [1, 364]), relay.reshape(const_8817.astype('float32'), [6,]), ), 3)
call_8818 = relay.TupleGetItem(func_8167_call(relay.reshape(var_8816.astype('float32'), [1, 364]), relay.reshape(const_8817.astype('float32'), [6,]), ), 3)
output = relay.Tuple([call_8769,call_8815,var_8816,const_8817,])
output2 = relay.Tuple([call_8770,call_8818,var_8816,const_8817,])
func_8822 = relay.Function([var_8816,], output)
mod['func_8822'] = func_8822
mod = relay.transform.InferType()(mod)
var_8823 = relay.var("var_8823", dtype = "float32", shape = (1, 364))#candidate|8823|(1, 364)|var|float32
output = func_8822(var_8823)
func_8824 = relay.Function([var_8823], output)
mutated_mod['func_8824'] = func_8824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_8839 = relay.TupleGetItem(func_1097_call(), 0)
call_8840 = relay.TupleGetItem(func_1098_call(), 0)
output = call_8839
output2 = call_8840
func_8843 = relay.Function([], output)
mod['func_8843'] = func_8843
mod = relay.transform.InferType()(mod)
output = func_8843()
func_8844 = relay.Function([], output)
mutated_mod['func_8844'] = func_8844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4861_call = mod.get_global_var('func_4861')
func_4863_call = mutated_mod.get_global_var('func_4863')
call_8887 = relay.TupleGetItem(func_4861_call(), 0)
call_8888 = relay.TupleGetItem(func_4863_call(), 0)
output = call_8887
output2 = call_8888
func_8911 = relay.Function([], output)
mod['func_8911'] = func_8911
mod = relay.transform.InferType()(mod)
output = func_8911()
func_8912 = relay.Function([], output)
mutated_mod['func_8912'] = func_8912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3312_call = mod.get_global_var('func_3312')
func_3314_call = mutated_mod.get_global_var('func_3314')
call_8937 = relay.TupleGetItem(func_3312_call(), 0)
call_8938 = relay.TupleGetItem(func_3314_call(), 0)
output = call_8937
output2 = call_8938
func_8946 = relay.Function([], output)
mod['func_8946'] = func_8946
mod = relay.transform.InferType()(mod)
mutated_mod['func_8946'] = func_8946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8946_call = mutated_mod.get_global_var('func_8946')
call_8947 = func_8946_call()
output = call_8947
func_8948 = relay.Function([], output)
mutated_mod['func_8948'] = func_8948
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8953 = relay.const([[[-5],[-8],[-9]],[[10],[-7],[-9]],[[4],[-7],[-9]],[[-4],[6],[5]],[[3],[-2],[-1]],[[-10],[10],[-1]],[[-2],[-6],[-9]],[[-5],[10],[-3]]], dtype = "int8")#candidate|8953|(8, 3, 1)|const|int8
var_8954 = relay.var("var_8954", dtype = "int8", shape = (8, 3, 11))#candidate|8954|(8, 3, 11)|var|int8
bop_8955 = relay.right_shift(const_8953.astype('int8'), var_8954.astype('int8')) # shape=(8, 3, 11)
func_8946_call = mod.get_global_var('func_8946')
func_8948_call = mutated_mod.get_global_var('func_8948')
call_8964 = func_8946_call()
call_8965 = func_8946_call()
func_766_call = mod.get_global_var('func_766')
func_767_call = mutated_mod.get_global_var('func_767')
call_8968 = func_766_call()
call_8969 = func_766_call()
output = relay.Tuple([bop_8955,call_8964,call_8968,])
output2 = relay.Tuple([bop_8955,call_8965,call_8969,])
func_8992 = relay.Function([var_8954,], output)
mod['func_8992'] = func_8992
mod = relay.transform.InferType()(mod)
mutated_mod['func_8992'] = func_8992
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8993 = relay.var("var_8993", dtype = "int8", shape = (8, 3, 11))#candidate|8993|(8, 3, 11)|var|int8
func_8992_call = mutated_mod.get_global_var('func_8992')
call_8994 = func_8992_call(var_8993)
output = call_8994
func_8995 = relay.Function([var_8993], output)
mutated_mod['func_8995'] = func_8995
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9024 = relay.var("var_9024", dtype = "int64", shape = (7, 6, 13))#candidate|9024|(7, 6, 13)|var|int64
var_9025 = relay.var("var_9025", dtype = "int64", shape = (7, 6, 13))#candidate|9025|(7, 6, 13)|var|int64
bop_9026 = relay.logical_xor(var_9024.astype('int64'), relay.reshape(var_9025.astype('int64'), relay.shape_of(var_9024))) # shape=(7, 6, 13)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_9036 = func_3977_call()
call_9037 = func_3977_call()
var_9038 = relay.var("var_9038", dtype = "int64", shape = (7, 6, 13))#candidate|9038|(7, 6, 13)|var|int64
bop_9039 = relay.left_shift(bop_9026.astype('int64'), relay.reshape(var_9038.astype('int64'), relay.shape_of(bop_9026))) # shape=(7, 6, 13)
func_490_call = mod.get_global_var('func_490')
func_491_call = mutated_mod.get_global_var('func_491')
call_9042 = relay.TupleGetItem(func_490_call(), 0)
call_9043 = relay.TupleGetItem(func_491_call(), 0)
output = relay.Tuple([call_9036,bop_9039,call_9042,])
output2 = relay.Tuple([call_9037,bop_9039,call_9043,])
func_9047 = relay.Function([var_9024,var_9025,var_9038,], output)
mod['func_9047'] = func_9047
mod = relay.transform.InferType()(mod)
var_9048 = relay.var("var_9048", dtype = "int64", shape = (7, 6, 13))#candidate|9048|(7, 6, 13)|var|int64
var_9049 = relay.var("var_9049", dtype = "int64", shape = (7, 6, 13))#candidate|9049|(7, 6, 13)|var|int64
var_9050 = relay.var("var_9050", dtype = "int64", shape = (7, 6, 13))#candidate|9050|(7, 6, 13)|var|int64
output = func_9047(var_9048,var_9049,var_9050,)
func_9051 = relay.Function([var_9048,var_9049,var_9050,], output)
mutated_mod['func_9051'] = func_9051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7934_call = mod.get_global_var('func_7934')
func_7935_call = mutated_mod.get_global_var('func_7935')
call_9107 = relay.TupleGetItem(func_7934_call(), 2)
call_9108 = relay.TupleGetItem(func_7935_call(), 2)
output = call_9107
output2 = call_9108
func_9122 = relay.Function([], output)
mod['func_9122'] = func_9122
mod = relay.transform.InferType()(mod)
mutated_mod['func_9122'] = func_9122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9122_call = mutated_mod.get_global_var('func_9122')
call_9123 = func_9122_call()
output = call_9123
func_9124 = relay.Function([], output)
mutated_mod['func_9124'] = func_9124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3162_call = mutated_mod.get_global_var('func_3162')
call_9181 = relay.TupleGetItem(func_3161_call(), 0)
call_9182 = relay.TupleGetItem(func_3162_call(), 0)
output = call_9181
output2 = call_9182
func_9186 = relay.Function([], output)
mod['func_9186'] = func_9186
mod = relay.transform.InferType()(mod)
output = func_9186()
func_9187 = relay.Function([], output)
mutated_mod['func_9187'] = func_9187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_905_call = mod.get_global_var('func_905')
func_906_call = mutated_mod.get_global_var('func_906')
call_9264 = func_905_call()
call_9265 = func_905_call()
func_6136_call = mod.get_global_var('func_6136')
func_6139_call = mutated_mod.get_global_var('func_6139')
const_9267 = relay.const([[8.048987,-9.167885,-5.054454,5.042259,-2.670909,1.787098,-7.466610,-7.987522,6.309319,-5.752382,-0.746112,7.795952,-9.569502,-5.780751,9.526871,-4.037675],[9.599260,-6.312665,-5.230233,-6.899117,4.639980,0.644888,3.681929,-5.014080,9.610415,6.079046,-4.440608,0.116946,3.307595,0.270349,8.684961,1.657637],[-3.170109,-5.419036,1.856039,-1.851117,-5.317181,-4.686260,8.813185,-7.421014,-4.017967,-4.414011,8.375842,6.430254,-3.693763,4.555421,8.479063,-9.009632],[-1.856148,-2.399035,3.611507,-0.890339,-0.268060,-8.661123,4.436063,9.939326,-7.718666,-3.546106,1.869165,-3.804873,9.037715,6.513747,-5.675462,-4.039965],[4.617773,-6.285871,1.617990,-8.862512,-1.374925,7.664801,-9.738109,4.233956,2.186030,-1.358537,3.883433,-3.987665,-4.632855,2.752801,8.011516,3.381156],[-2.916618,-6.699817,6.651552,-5.106420,1.886363,2.031069,-4.793275,-0.828021,7.933081,-2.854193,4.376777,6.283923,7.928768,-8.436537,-3.517011,3.466981],[7.250036,7.357474,-8.108851,-8.717722,7.613683,4.017158,-0.204880,8.321087,-1.533688,0.899015,-2.368003,2.261322,2.188694,2.309702,-8.880820,5.903702],[-3.708621,-2.012827,-0.186173,-9.088728,-0.954231,8.586209,0.727106,-0.006871,-8.024144,7.377903,-1.874561,-7.782514,-5.285902,-1.931390,-6.335674,-1.009979],[-9.127168,-7.115733,-2.199517,-5.198764,-8.262899,2.831270,3.615155,-0.408035,7.741793,-6.860500,-6.988621,-5.230753,-8.841745,3.794612,-0.110187,9.666215],[-5.060116,3.682145,-3.369844,-3.026718,4.202637,-3.102558,7.083014,-2.359472,-9.653953,7.376623,-7.658794,3.367116,-4.636437,4.976975,8.288809,6.392426],[-5.216644,-2.396342,-8.206641,-5.256491,-1.052327,-4.737717,0.003399,5.960260,-8.947292,-9.281903,-3.314231,8.594700,0.482725,4.784243,-2.139459,-8.949178],[7.387967,9.381256,5.935910,7.488018,1.338367,-2.126351,-4.369382,-1.289643,-4.762172,4.529047,6.544673,6.251221,-4.849199,4.732793,9.719854,4.890938],[-7.045524,-3.000497,-8.326798,8.654204,-0.907371,-3.185072,7.332080,2.714387,-7.998078,-3.312305,6.945216,-0.252273,-7.692633,-9.200610,2.380929,-9.321685],[9.069485,-9.019453,-6.355974,5.101398,7.892132,-1.383392,-1.335365,-0.869955,-4.891813,-0.509291,-5.406945,8.823721,-7.632574,-1.135722,-2.936961,3.753890],[4.035003,8.848657,-9.469654,-0.884557,4.342043,-2.742683,-7.186012,-4.080109,-8.081237,3.606564,6.204668,2.755539,-5.447694,7.931926,4.626857,-0.980639],[-4.788256,-4.114967,-0.840565,-0.841346,4.358230,-5.380993,6.641987,0.336146,2.123166,-6.390767,0.565134,7.648834,0.426162,-1.021853,6.400654,-3.693280]], dtype = "float64")#candidate|9267|(16, 16)|const|float64
call_9266 = relay.TupleGetItem(func_6136_call(relay.reshape(const_9267.astype('float64'), [4, 8, 8])), 2)
call_9268 = relay.TupleGetItem(func_6139_call(relay.reshape(const_9267.astype('float64'), [4, 8, 8])), 2)
output = relay.Tuple([call_9264,call_9266,const_9267,])
output2 = relay.Tuple([call_9265,call_9268,const_9267,])
func_9277 = relay.Function([], output)
mod['func_9277'] = func_9277
mod = relay.transform.InferType()(mod)
mutated_mod['func_9277'] = func_9277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9277_call = mutated_mod.get_global_var('func_9277')
call_9278 = func_9277_call()
output = call_9278
func_9279 = relay.Function([], output)
mutated_mod['func_9279'] = func_9279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7190_call = mod.get_global_var('func_7190')
func_7192_call = mutated_mod.get_global_var('func_7192')
call_9309 = relay.TupleGetItem(func_7190_call(), 0)
call_9310 = relay.TupleGetItem(func_7192_call(), 0)
output = relay.Tuple([call_9309,])
output2 = relay.Tuple([call_9310,])
func_9317 = relay.Function([], output)
mod['func_9317'] = func_9317
mod = relay.transform.InferType()(mod)
output = func_9317()
func_9318 = relay.Function([], output)
mutated_mod['func_9318'] = func_9318
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9319 = relay.var("var_9319", dtype = "uint16", shape = ())#candidate|9319|()|var|uint16
var_9320 = relay.var("var_9320", dtype = "uint16", shape = (8, 8, 1))#candidate|9320|(8, 8, 1)|var|uint16
bop_9321 = relay.logical_xor(var_9319.astype('uint16'), var_9320.astype('uint16')) # shape=(8, 8, 1)
output = bop_9321
output2 = bop_9321
func_9327 = relay.Function([var_9319,var_9320,], output)
mod['func_9327'] = func_9327
mod = relay.transform.InferType()(mod)
var_9328 = relay.var("var_9328", dtype = "uint16", shape = ())#candidate|9328|()|var|uint16
var_9329 = relay.var("var_9329", dtype = "uint16", shape = (8, 8, 1))#candidate|9329|(8, 8, 1)|var|uint16
output = func_9327(var_9328,var_9329,)
func_9330 = relay.Function([var_9328,var_9329,], output)
mutated_mod['func_9330'] = func_9330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5237_call = mod.get_global_var('func_5237')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_9356 = relay.TupleGetItem(func_5237_call(), 0)
call_9357 = relay.TupleGetItem(func_5239_call(), 0)
output = relay.Tuple([call_9356,])
output2 = relay.Tuple([call_9357,])
func_9368 = relay.Function([], output)
mod['func_9368'] = func_9368
mod = relay.transform.InferType()(mod)
output = func_9368()
func_9369 = relay.Function([], output)
mutated_mod['func_9369'] = func_9369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9186_call = mod.get_global_var('func_9186')
func_9187_call = mutated_mod.get_global_var('func_9187')
call_9381 = func_9186_call()
call_9382 = func_9186_call()
output = relay.Tuple([call_9381,])
output2 = relay.Tuple([call_9382,])
func_9385 = relay.Function([], output)
mod['func_9385'] = func_9385
mod = relay.transform.InferType()(mod)
output = func_9385()
func_9386 = relay.Function([], output)
mutated_mod['func_9386'] = func_9386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9277_call = mod.get_global_var('func_9277')
func_9279_call = mutated_mod.get_global_var('func_9279')
call_9393 = relay.TupleGetItem(func_9277_call(), 1)
call_9394 = relay.TupleGetItem(func_9279_call(), 1)
output = relay.Tuple([call_9393,])
output2 = relay.Tuple([call_9394,])
func_9409 = relay.Function([], output)
mod['func_9409'] = func_9409
mod = relay.transform.InferType()(mod)
mutated_mod['func_9409'] = func_9409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9409_call = mutated_mod.get_global_var('func_9409')
call_9410 = func_9409_call()
output = call_9410
func_9411 = relay.Function([], output)
mutated_mod['func_9411'] = func_9411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_9502 = relay.TupleGetItem(func_7447_call(), 1)
call_9503 = relay.TupleGetItem(func_7448_call(), 1)
func_2083_call = mod.get_global_var('func_2083')
func_2085_call = mutated_mod.get_global_var('func_2085')
call_9515 = relay.TupleGetItem(func_2083_call(), 0)
call_9516 = relay.TupleGetItem(func_2085_call(), 0)
func_3734_call = mod.get_global_var('func_3734')
func_3736_call = mutated_mod.get_global_var('func_3736')
call_9523 = relay.TupleGetItem(func_3734_call(), 0)
call_9524 = relay.TupleGetItem(func_3736_call(), 0)
output = relay.Tuple([call_9502,call_9515,call_9523,])
output2 = relay.Tuple([call_9503,call_9516,call_9524,])
func_9544 = relay.Function([], output)
mod['func_9544'] = func_9544
mod = relay.transform.InferType()(mod)
output = func_9544()
func_9545 = relay.Function([], output)
mutated_mod['func_9545'] = func_9545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_320_call = mod.get_global_var('func_320')
func_322_call = mutated_mod.get_global_var('func_322')
call_9588 = relay.TupleGetItem(func_320_call(), 0)
call_9589 = relay.TupleGetItem(func_322_call(), 0)
output = call_9588
output2 = call_9589
func_9592 = relay.Function([], output)
mod['func_9592'] = func_9592
mod = relay.transform.InferType()(mod)
mutated_mod['func_9592'] = func_9592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9592_call = mutated_mod.get_global_var('func_9592')
call_9593 = func_9592_call()
output = call_9593
func_9594 = relay.Function([], output)
mutated_mod['func_9594'] = func_9594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7561_call = mod.get_global_var('func_7561')
func_7562_call = mutated_mod.get_global_var('func_7562')
call_9595 = relay.TupleGetItem(func_7561_call(), 1)
call_9596 = relay.TupleGetItem(func_7562_call(), 1)
func_3343_call = mod.get_global_var('func_3343')
func_3345_call = mutated_mod.get_global_var('func_3345')
call_9599 = relay.TupleGetItem(func_3343_call(), 0)
call_9600 = relay.TupleGetItem(func_3345_call(), 0)
func_7607_call = mod.get_global_var('func_7607')
func_7610_call = mutated_mod.get_global_var('func_7610')
var_9616 = relay.var("var_9616", dtype = "uint32", shape = ())#candidate|9616|()|var|uint32
var_9617 = relay.var("var_9617", dtype = "uint32", shape = (1248,))#candidate|9617|(1248,)|var|uint32
call_9615 = func_7607_call(relay.reshape(var_9616.astype('uint32'), []), relay.reshape(var_9617.astype('uint32'), [12, 13, 8]), )
call_9618 = func_7607_call(relay.reshape(var_9616.astype('uint32'), []), relay.reshape(var_9617.astype('uint32'), [12, 13, 8]), )
output = relay.Tuple([call_9595,call_9599,call_9615,var_9616,var_9617,])
output2 = relay.Tuple([call_9596,call_9600,call_9618,var_9616,var_9617,])
func_9622 = relay.Function([var_9616,var_9617,], output)
mod['func_9622'] = func_9622
mod = relay.transform.InferType()(mod)
var_9623 = relay.var("var_9623", dtype = "uint32", shape = ())#candidate|9623|()|var|uint32
var_9624 = relay.var("var_9624", dtype = "uint32", shape = (1248,))#candidate|9624|(1248,)|var|uint32
output = func_9622(var_9623,var_9624,)
func_9625 = relay.Function([var_9623,var_9624,], output)
mutated_mod['func_9625'] = func_9625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6740_call = mod.get_global_var('func_6740')
func_6742_call = mutated_mod.get_global_var('func_6742')
call_9629 = relay.TupleGetItem(func_6740_call(), 0)
call_9630 = relay.TupleGetItem(func_6742_call(), 0)
output = relay.Tuple([call_9629,])
output2 = relay.Tuple([call_9630,])
func_9631 = relay.Function([], output)
mod['func_9631'] = func_9631
mod = relay.transform.InferType()(mod)
output = func_9631()
func_9632 = relay.Function([], output)
mutated_mod['func_9632'] = func_9632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9694 = relay.var("var_9694", dtype = "float64", shape = (4, 1, 4))#candidate|9694|(4, 1, 4)|var|float64
uop_9695 = relay.erf(var_9694.astype('float64')) # shape=(4, 1, 4)
func_8006_call = mod.get_global_var('func_8006')
func_8009_call = mutated_mod.get_global_var('func_8009')
const_9699 = relay.const([3,2,-3,-9,-10,-4,2], dtype = "uint64")#candidate|9699|(7,)|const|uint64
call_9698 = relay.TupleGetItem(func_8006_call(relay.reshape(const_9699.astype('uint64'), [1, 7])), 0)
call_9700 = relay.TupleGetItem(func_8009_call(relay.reshape(const_9699.astype('uint64'), [1, 7])), 0)
func_8946_call = mod.get_global_var('func_8946')
func_8948_call = mutated_mod.get_global_var('func_8948')
call_9701 = func_8946_call()
call_9702 = func_8946_call()
func_639_call = mod.get_global_var('func_639')
func_642_call = mutated_mod.get_global_var('func_642')
const_9713 = relay.const([-8.526702,-4.942438,6.849475,4.066093,2.993556,6.695902], dtype = "float32")#candidate|9713|(6,)|const|float32
call_9712 = relay.TupleGetItem(func_639_call(relay.reshape(const_9713.astype('float32'), [1, 2, 3])), 0)
call_9714 = relay.TupleGetItem(func_642_call(relay.reshape(const_9713.astype('float32'), [1, 2, 3])), 0)
output = relay.Tuple([uop_9695,call_9698,const_9699,call_9701,call_9712,const_9713,])
output2 = relay.Tuple([uop_9695,call_9700,const_9699,call_9702,call_9714,const_9713,])
func_9727 = relay.Function([var_9694,], output)
mod['func_9727'] = func_9727
mod = relay.transform.InferType()(mod)
var_9728 = relay.var("var_9728", dtype = "float64", shape = (4, 1, 4))#candidate|9728|(4, 1, 4)|var|float64
output = func_9727(var_9728)
func_9729 = relay.Function([var_9728], output)
mutated_mod['func_9729'] = func_9729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4503_call = mod.get_global_var('func_4503')
func_4505_call = mutated_mod.get_global_var('func_4505')
call_9734 = relay.TupleGetItem(func_4503_call(), 1)
call_9735 = relay.TupleGetItem(func_4505_call(), 1)
output = relay.Tuple([call_9734,])
output2 = relay.Tuple([call_9735,])
func_9747 = relay.Function([], output)
mod['func_9747'] = func_9747
mod = relay.transform.InferType()(mod)
mutated_mod['func_9747'] = func_9747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9747_call = mutated_mod.get_global_var('func_9747')
call_9748 = func_9747_call()
output = call_9748
func_9749 = relay.Function([], output)
mutated_mod['func_9749'] = func_9749
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9778 = relay.var("var_9778", dtype = "float32", shape = (7, 7))#candidate|9778|(7, 7)|var|float32
uop_9779 = relay.log(var_9778.astype('float32')) # shape=(7, 7)
output = relay.Tuple([uop_9779,])
output2 = relay.Tuple([uop_9779,])
F = relay.Function([var_9778,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9778,], output2)
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
	relay.transform.MergeCompilerRegions(),
	relay.transform.Inline(),
	relay.transform.LambdaLift(),
	relay.transform.LazyGradientInit(),
	relay.transform.PartialEvaluate(),
	relay.transform.Legalize(),
	relay.transform.FoldConstant(),
	relay.transform.ToANormalForm(),
	relay.transform.ToGraphNormalForm(),
	relay.transform.SimplifyInference(),
	relay.transform.ToBasicBlockNormalForm(),
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
