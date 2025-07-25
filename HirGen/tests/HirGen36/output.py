import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_76 = relay.var("var_76", dtype = "float32", shape = (15, 1, 9))#candidate|76|(15, 1, 9)|var|float32
uop_77 = relay.erf(var_76.astype('float32')) # shape=(15, 1, 9)
uop_79 = relay.log2(uop_77.astype('float32')) # shape=(15, 1, 9)
output = relay.Tuple([uop_79,])
output2 = relay.Tuple([uop_79,])
func_81 = relay.Function([var_76,], output)
mod['func_81'] = func_81
mod = relay.transform.InferType()(mod)
mutated_mod['func_81'] = func_81
mutated_mod = relay.transform.InferType()(mutated_mod)
var_82 = relay.var("var_82", dtype = "float32", shape = (15, 1, 9))#candidate|82|(15, 1, 9)|var|float32
func_81_call = mutated_mod.get_global_var('func_81')
call_83 = func_81_call(var_82)
output = call_83
func_84 = relay.Function([var_82], output)
mutated_mod['func_84'] = func_84
mutated_mod = relay.transform.InferType()(mutated_mod)
var_169 = relay.var("var_169", dtype = "float32", shape = (15, 9, 16))#candidate|169|(15, 9, 16)|var|float32
uop_170 = relay.cosh(var_169.astype('float32')) # shape=(15, 9, 16)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
var_181 = relay.var("var_181", dtype = "float32", shape = (15, 9))#candidate|181|(15, 9)|var|float32
call_180 = relay.TupleGetItem(func_81_call(relay.reshape(var_181.astype('float32'), [15, 1, 9])), 0)
call_182 = relay.TupleGetItem(func_84_call(relay.reshape(var_181.astype('float32'), [15, 1, 9])), 0)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
call_183 = relay.TupleGetItem(func_81_call(relay.reshape(call_180.astype('float32'), [15, 1, 9])), 0)
call_184 = relay.TupleGetItem(func_84_call(relay.reshape(call_180.astype('float32'), [15, 1, 9])), 0)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
call_211 = relay.TupleGetItem(func_81_call(relay.reshape(call_180.astype('float32'), [15, 1, 9])), 0)
call_212 = relay.TupleGetItem(func_84_call(relay.reshape(call_180.astype('float32'), [15, 1, 9])), 0)
output = relay.Tuple([uop_170,call_180,var_181,call_183,call_211,])
output2 = relay.Tuple([uop_170,call_182,var_181,call_184,call_212,])
func_235 = relay.Function([var_169,var_181,], output)
mod['func_235'] = func_235
mod = relay.transform.InferType()(mod)
var_236 = relay.var("var_236", dtype = "float32", shape = (15, 9, 16))#candidate|236|(15, 9, 16)|var|float32
var_237 = relay.var("var_237", dtype = "float32", shape = (15, 9))#candidate|237|(15, 9)|var|float32
output = func_235(var_236,var_237,)
func_238 = relay.Function([var_236,var_237,], output)
mutated_mod['func_238'] = func_238
mutated_mod = relay.transform.InferType()(mutated_mod)
var_290 = relay.var("var_290", dtype = "uint32", shape = (5, 13, 15))#candidate|290|(5, 13, 15)|var|uint32
var_291 = relay.var("var_291", dtype = "uint32", shape = (5, 13, 15))#candidate|291|(5, 13, 15)|var|uint32
bop_292 = relay.bitwise_and(var_290.astype('uint32'), relay.reshape(var_291.astype('uint32'), relay.shape_of(var_290))) # shape=(5, 13, 15)
var_312 = relay.var("var_312", dtype = "uint32", shape = (5, 13, 15))#candidate|312|(5, 13, 15)|var|uint32
bop_313 = relay.bitwise_or(var_291.astype('uint32'), relay.reshape(var_312.astype('uint32'), relay.shape_of(var_291))) # shape=(5, 13, 15)
output = relay.Tuple([bop_292,bop_313,])
output2 = relay.Tuple([bop_292,bop_313,])
func_316 = relay.Function([var_290,var_291,var_312,], output)
mod['func_316'] = func_316
mod = relay.transform.InferType()(mod)
var_317 = relay.var("var_317", dtype = "uint32", shape = (5, 13, 15))#candidate|317|(5, 13, 15)|var|uint32
var_318 = relay.var("var_318", dtype = "uint32", shape = (5, 13, 15))#candidate|318|(5, 13, 15)|var|uint32
var_319 = relay.var("var_319", dtype = "uint32", shape = (5, 13, 15))#candidate|319|(5, 13, 15)|var|uint32
output = func_316(var_317,var_318,var_319,)
func_320 = relay.Function([var_317,var_318,var_319,], output)
mutated_mod['func_320'] = func_320
mutated_mod = relay.transform.InferType()(mutated_mod)
const_643 = relay.const([[[0.530322,-6.214179,6.282808,5.559840,-5.693161,-9.238464,1.133664]],[[-6.212854,0.727891,6.563920,-9.222997,-3.788279,2.140598,6.546031]],[[1.200163,-9.210366,1.680025,8.474054,2.802175,-6.613578,1.567074]],[[4.938217,5.941727,9.689096,2.918280,1.583073,-7.866498,-0.320255]],[[1.076615,-4.604494,-1.576557,0.563037,-9.523833,-3.033513,4.063985]],[[8.409022,4.710505,6.000902,5.919491,2.407212,9.141278,-9.408337]],[[-9.454114,0.792533,-5.214353,-8.386393,5.346905,6.837542,3.638752]],[[8.962242,-5.325491,4.067318,1.400100,-1.563826,2.461034,2.904495]],[[-3.736007,1.388392,-4.945270,-0.108625,-1.584175,4.447476,-8.678144]],[[0.407251,-1.364709,-0.623685,-2.159078,-3.221595,-6.379417,-4.786840]],[[2.554435,-1.934797,7.544249,-8.724744,9.067293,-2.205547,-4.937517]],[[3.949295,-3.859837,-2.440505,6.797632,0.659354,-1.943760,8.860123]],[[3.806961,-6.774250,7.471842,-0.627609,-9.613899,4.417877,-4.471006]],[[-0.294662,1.224884,6.560676,-4.174258,7.567590,7.936961,4.773353]],[[-7.144936,-8.238473,-2.332912,-4.691500,-5.797864,-5.600138,-7.563355]]], dtype = "float32")#candidate|643|(15, 1, 7)|const|float32
uop_644 = relay.erf(const_643.astype('float32')) # shape=(15, 1, 7)
uop_655 = relay.atanh(uop_644.astype('float64')) # shape=(15, 1, 7)
uop_658 = relay.cosh(uop_644.astype('float32')) # shape=(15, 1, 7)
func_316_call = mod.get_global_var('func_316')
func_320_call = mutated_mod.get_global_var('func_320')
var_669 = relay.var("var_669", dtype = "uint32", shape = (975,))#candidate|669|(975,)|var|uint32
call_668 = relay.TupleGetItem(func_316_call(relay.reshape(var_669.astype('uint32'), [5, 13, 15]), relay.reshape(var_669.astype('uint32'), [5, 13, 15]), relay.reshape(var_669.astype('uint32'), [5, 13, 15]), ), 0)
call_670 = relay.TupleGetItem(func_320_call(relay.reshape(var_669.astype('uint32'), [5, 13, 15]), relay.reshape(var_669.astype('uint32'), [5, 13, 15]), relay.reshape(var_669.astype('uint32'), [5, 13, 15]), ), 0)
output = relay.Tuple([uop_655,uop_658,call_668,var_669,])
output2 = relay.Tuple([uop_655,uop_658,call_670,var_669,])
func_685 = relay.Function([var_669,], output)
mod['func_685'] = func_685
mod = relay.transform.InferType()(mod)
mutated_mod['func_685'] = func_685
mutated_mod = relay.transform.InferType()(mutated_mod)
var_686 = relay.var("var_686", dtype = "uint32", shape = (975,))#candidate|686|(975,)|var|uint32
func_685_call = mutated_mod.get_global_var('func_685')
call_687 = func_685_call(var_686)
output = call_687
func_688 = relay.Function([var_686], output)
mutated_mod['func_688'] = func_688
mutated_mod = relay.transform.InferType()(mutated_mod)
var_763 = relay.var("var_763", dtype = "float64", shape = (13, 3, 2))#candidate|763|(13, 3, 2)|var|float64
var_764 = relay.var("var_764", dtype = "float64", shape = (13, 3, 2))#candidate|764|(13, 3, 2)|var|float64
bop_765 = relay.multiply(var_763.astype('float64'), relay.reshape(var_764.astype('float64'), relay.shape_of(var_763))) # shape=(13, 3, 2)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
var_773 = relay.var("var_773", dtype = "float32", shape = (135,))#candidate|773|(135,)|var|float32
call_772 = relay.TupleGetItem(func_81_call(relay.reshape(var_773.astype('float32'), [15, 1, 9])), 0)
call_774 = relay.TupleGetItem(func_84_call(relay.reshape(var_773.astype('float32'), [15, 1, 9])), 0)
output = relay.Tuple([bop_765,call_772,var_773,])
output2 = relay.Tuple([bop_765,call_774,var_773,])
func_777 = relay.Function([var_763,var_764,var_773,], output)
mod['func_777'] = func_777
mod = relay.transform.InferType()(mod)
var_778 = relay.var("var_778", dtype = "float64", shape = (13, 3, 2))#candidate|778|(13, 3, 2)|var|float64
var_779 = relay.var("var_779", dtype = "float64", shape = (13, 3, 2))#candidate|779|(13, 3, 2)|var|float64
var_780 = relay.var("var_780", dtype = "float32", shape = (135,))#candidate|780|(135,)|var|float32
output = func_777(var_778,var_779,var_780,)
func_781 = relay.Function([var_778,var_779,var_780,], output)
mutated_mod['func_781'] = func_781
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1004 = relay.var("var_1004", dtype = "uint32", shape = (3, 5, 2))#candidate|1004|(3, 5, 2)|var|uint32
const_1005 = relay.const([[[1,-10],[4,-7],[5,9],[-5,9],[2,-10]],[[6,-10],[-7,3],[5,7],[-3,-4],[-2,-6]],[[-4,-8],[-1,-4],[2,-10],[7,5],[8,-4]]], dtype = "uint32")#candidate|1005|(3, 5, 2)|const|uint32
bop_1006 = relay.add(var_1004.astype('uint32'), relay.reshape(const_1005.astype('uint32'), relay.shape_of(var_1004))) # shape=(3, 5, 2)
func_777_call = mod.get_global_var('func_777')
func_781_call = mutated_mod.get_global_var('func_781')
var_1010 = relay.var("var_1010", dtype = "float64", shape = (78,))#candidate|1010|(78,)|var|float64
const_1011 = relay.const([[9.326834,1.324181,3.777243,-4.538742,-5.509053,4.645226,-1.092465,-4.197781,1.829335,2.050788,-2.232059,-6.783238,-5.000442,7.443092,-7.554544,5.088291,2.794105,-1.881262,8.287944,-5.100187,9.917204,-0.819149,-0.836458,9.250039,4.187495,7.952266,6.070396,1.820842,8.816193,9.155526,6.560338,0.841714,2.422231,1.446999,5.882341,2.616767,-5.562092,-0.862518,-0.853622,-1.666777,-9.709768,4.167855,0.888214,-2.805479,6.963335,-1.712319,-0.806538,-0.682905,7.127381,-8.782781,3.135824,-0.407723,1.632598,-6.598736,-6.933197,6.356843,-2.768402,-5.346488,-5.592093,1.879012,-0.158662,-6.926036,4.915049,4.592684,-6.662122,7.316314,1.429545,0.415448,-0.039938,-6.554133,-1.601990,-1.381980,-0.879617,-4.692521,9.139907,6.368630,-0.020403,-4.569888,-8.382365,-8.240833,8.394228,-4.694304,6.871472,-6.907290,-5.593468,-4.031181,-1.436237,7.879510,-2.147631,2.506105,2.437944,4.916533,-3.550297,-0.858968,9.231876,-7.036330,-6.798797,6.503023,-9.431023,-6.201828,-1.385286,-9.410003,5.109072,-6.479386,7.446746,6.298200,-1.726884,-0.237194,-9.944022,7.344637,-9.649777,-6.813340,-4.962942,-2.824577,9.028746,6.288654,-1.312385,6.012398,-6.577240,1.200305,8.867862,-5.472488,2.344570,2.638956,9.394285,-4.325993,-8.417117,3.561905,-8.255695,0.202420,-8.903752,-7.047410,-7.039771,-8.517392,1.004460]], dtype = "float32")#candidate|1011|(1, 135)|const|float32
call_1009 = relay.TupleGetItem(func_777_call(relay.reshape(var_1010.astype('float64'), [13, 3, 2]), relay.reshape(var_1010.astype('float64'), [13, 3, 2]), relay.reshape(const_1011.astype('float32'), [135,]), ), 1)
call_1012 = relay.TupleGetItem(func_781_call(relay.reshape(var_1010.astype('float64'), [13, 3, 2]), relay.reshape(var_1010.astype('float64'), [13, 3, 2]), relay.reshape(const_1011.astype('float32'), [135,]), ), 1)
bop_1018 = relay.equal(call_1009.astype('bool'), relay.reshape(const_1011.astype('bool'), relay.shape_of(call_1009))) # shape=(15, 1, 9)
bop_1021 = relay.equal(call_1012.astype('bool'), relay.reshape(const_1011.astype('bool'), relay.shape_of(call_1012))) # shape=(15, 1, 9)
output = relay.Tuple([bop_1006,var_1010,bop_1018,])
output2 = relay.Tuple([bop_1006,var_1010,bop_1021,])
func_1022 = relay.Function([var_1004,var_1010,], output)
mod['func_1022'] = func_1022
mod = relay.transform.InferType()(mod)
mutated_mod['func_1022'] = func_1022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1022_call = mutated_mod.get_global_var('func_1022')
var_1024 = relay.var("var_1024", dtype = "uint32", shape = (3, 5, 2))#candidate|1024|(3, 5, 2)|var|uint32
var_1025 = relay.var("var_1025", dtype = "float64", shape = (78,))#candidate|1025|(78,)|var|float64
call_1023 = func_1022_call(var_1024,var_1025,)
output = call_1023
func_1026 = relay.Function([var_1024,var_1025,], output)
mutated_mod['func_1026'] = func_1026
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1128 = relay.var("var_1128", dtype = "bool", shape = (5, 10, 7))#candidate|1128|(5, 10, 7)|var|bool
const_1129 = relay.const([[[True,True,False,True,True,True,False],[False,False,False,False,True,True,True],[True,False,True,False,True,True,True],[False,False,True,False,True,True,False],[False,True,False,True,False,False,False],[False,True,True,False,True,True,False],[True,True,False,False,True,True,False],[True,False,False,True,True,True,False],[False,False,False,False,True,False,True],[True,False,False,True,True,True,True]],[[False,False,False,True,True,False,True],[True,True,False,False,True,False,True],[False,True,True,True,True,True,True],[False,True,True,True,True,True,True],[False,False,False,True,False,False,False],[False,False,False,True,True,False,True],[True,False,False,True,True,False,False],[False,True,False,False,True,True,True],[False,False,False,True,False,True,False],[False,True,False,False,False,False,True]],[[True,False,False,False,False,True,False],[True,True,False,True,False,False,True],[True,True,True,False,True,True,True],[True,False,True,False,False,True,False],[False,False,False,True,False,False,False],[True,True,False,False,False,False,False],[True,True,True,False,False,False,False],[False,False,True,True,False,False,True],[False,False,False,False,False,False,False],[False,False,False,True,False,False,False]],[[False,False,False,True,True,True,False],[False,False,False,False,False,False,True],[False,False,True,True,False,True,True],[False,True,True,True,True,True,False],[True,True,False,False,False,False,True],[True,False,True,True,False,False,True],[False,False,True,False,False,False,True],[True,True,True,True,False,False,False],[True,False,True,True,True,True,True],[True,False,False,True,False,False,False]],[[False,False,False,False,False,True,False],[False,True,False,True,False,True,True],[False,True,True,True,True,False,False],[True,False,True,False,False,False,True],[False,False,False,False,False,False,False],[False,True,False,False,False,False,False],[False,True,True,False,True,False,True],[False,True,False,True,True,True,False],[True,True,True,True,True,True,True],[True,True,True,True,False,True,False]]], dtype = "bool")#candidate|1129|(5, 10, 7)|const|bool
bop_1130 = relay.logical_or(var_1128.astype('bool'), relay.reshape(const_1129.astype('bool'), relay.shape_of(var_1128))) # shape=(5, 10, 7)
bop_1149 = relay.divide(var_1128.astype('float32'), relay.reshape(bop_1130.astype('float32'), relay.shape_of(var_1128))) # shape=(5, 10, 7)
output = relay.Tuple([bop_1149,])
output2 = relay.Tuple([bop_1149,])
func_1152 = relay.Function([var_1128,], output)
mod['func_1152'] = func_1152
mod = relay.transform.InferType()(mod)
var_1153 = relay.var("var_1153", dtype = "bool", shape = (5, 10, 7))#candidate|1153|(5, 10, 7)|var|bool
output = func_1152(var_1153)
func_1154 = relay.Function([var_1153], output)
mutated_mod['func_1154'] = func_1154
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1491 = relay.var("var_1491", dtype = "float32", shape = (14, 4, 1))#candidate|1491|(14, 4, 1)|var|float32
uop_1492 = relay.cosh(var_1491.astype('float32')) # shape=(14, 4, 1)
uop_1496 = relay.rsqrt(var_1491.astype('float64')) # shape=(14, 4, 1)
bop_1506 = relay.logical_or(var_1491.astype('bool'), relay.reshape(uop_1496.astype('bool'), relay.shape_of(var_1491))) # shape=(14, 4, 1)
const_1510 = relay.const([[[5.061434,2.220078,2.865303,-6.231404,-7.737564,-1.016994,-5.458541,9.283794,8.594947,9.371754,0.024396,-5.696985,-5.653456],[-8.686944,7.184867,-5.583180,-2.683050,-9.828363,2.077788,3.013954,-4.259604,6.452167,8.424297,-1.609730,5.648136,-9.982264],[-3.697902,3.401968,-6.241318,-1.793575,7.889237,-4.337359,-6.429702,-2.837581,8.042026,4.144800,7.770287,9.473245,0.991907],[9.743190,4.221530,-0.457519,6.185359,-8.794248,4.984016,8.825075,2.386615,-5.896666,-0.759604,-6.433626,-4.029280,3.814522]],[[-2.443491,-3.384099,-3.498378,3.805396,-4.875728,9.672132,4.406896,0.023419,-8.373802,5.550163,-5.996237,8.322868,-0.522254],[8.939975,6.820290,9.178902,2.100042,8.066739,3.419453,9.507255,-9.401776,6.138769,-0.034683,-3.972887,2.133673,9.549222],[0.590298,-5.549055,-2.040698,-0.777084,-1.036030,5.097064,-7.855614,4.476907,7.096425,2.171849,1.906304,4.894264,7.267185],[-4.440867,-7.037883,-2.215691,-2.983161,0.130115,-7.327603,-1.958524,0.646703,-2.324183,9.553045,-0.150069,-3.087877,-0.691482]],[[-5.203486,-5.648018,-1.466598,3.225788,-0.373683,-1.264357,-8.992613,6.486763,-9.952061,-0.402110,6.987903,2.716394,-6.953975],[-7.516801,0.652259,0.709035,-8.357798,5.226281,-0.360514,7.921114,-8.820770,-8.222052,-2.979331,-3.238943,4.723111,-4.550242],[0.676310,4.634777,6.742453,4.592195,0.969474,4.586677,-7.076980,-0.329230,7.478423,6.341856,9.588613,-0.623717,9.632436],[-3.926819,3.305007,7.780120,-0.385407,0.795587,-4.449057,-7.743331,8.647586,-0.326823,-6.234097,-0.654570,-3.324970,-5.712577]],[[9.692013,5.382442,4.276593,-2.243142,5.369342,6.774385,-8.847031,7.000327,3.442769,-4.755197,5.968476,-9.618137,0.027717],[2.500602,-7.599227,-4.914683,8.581311,-8.636652,9.605665,4.933142,4.302408,3.433193,1.211745,-6.827991,-9.234757,9.927266],[7.455040,-9.557344,4.480045,8.437657,1.468831,4.321170,3.857701,4.775847,-7.180415,6.493454,9.852717,-0.991237,-0.429790],[-2.400169,7.945636,-6.540692,9.983281,-6.723597,0.264462,3.937008,2.735370,1.105661,-3.244123,3.638772,1.253536,-0.698555]],[[7.272976,-8.980459,-4.758560,9.961294,-6.922206,-7.745596,-7.818314,-5.542119,-0.206038,-1.475738,9.261864,5.291488,-1.406437],[-8.008247,9.781738,-8.406908,8.850631,-8.221523,9.303983,-5.695115,-7.130863,-8.258144,8.338983,-4.856143,-4.068807,6.995700],[-2.647354,1.248384,7.611928,-9.498772,8.425854,-6.885676,9.519660,-6.131198,-6.273472,0.209633,8.037551,6.146074,-6.970738],[1.757288,-2.301428,-5.205326,0.574333,8.234301,-9.624436,0.850573,-8.460217,-7.830860,5.612967,1.400566,0.196927,-7.223855]],[[-0.696087,5.349572,6.025334,6.193943,0.990539,-5.965127,0.686902,-8.704011,5.235320,7.926556,7.863520,-9.227395,-3.954193],[-5.791031,-7.873034,1.611971,-0.386809,7.370289,6.039696,3.019384,5.239508,2.827377,4.638069,-8.199800,3.054610,-6.667529],[5.360364,5.098547,-3.106799,-8.365574,-7.473239,6.979552,-0.750835,-2.876386,9.823763,7.665904,9.957129,-5.195826,-1.259190],[-7.529913,-1.586960,-5.444607,2.144058,-1.049473,4.698766,-9.868165,-6.310822,-6.713451,-1.224840,-8.626573,-7.830333,-0.671660]],[[-4.694673,-1.933809,0.117841,-9.461661,1.661346,-5.086442,9.104642,1.543400,9.785085,-1.670652,7.383396,-1.971155,-7.889893],[-1.380514,-2.023249,-9.452930,7.766494,8.577985,6.421882,-0.690796,-1.332281,3.468501,4.766529,-3.131025,-4.953570,-6.119918],[7.494565,-6.144541,5.667263,-9.985477,4.011105,-3.260387,8.114494,-2.799511,-9.574292,-6.078700,8.459542,-2.531635,-3.954243],[3.013843,5.725544,-3.950347,-6.851800,-8.080028,7.984004,-2.322505,-3.713405,2.353882,-3.618552,-9.736859,4.801096,-2.355212]],[[9.753445,9.162518,3.716833,-1.869496,0.101750,-0.226097,7.731347,5.868399,0.517214,-0.820534,7.810922,-8.136586,2.878959],[-2.312186,0.877750,2.933353,3.739656,-1.999930,6.874993,7.837320,1.357003,-5.268260,7.072489,-3.394535,3.054877,-6.418158],[-2.838140,8.506841,0.791513,-9.859563,-2.843776,6.653698,9.463411,-7.472755,3.158763,7.413843,0.626719,5.556953,9.883078],[-8.413384,-8.189399,3.078023,4.743621,-2.295016,-8.363499,9.818272,-2.090631,-9.451240,-2.746638,-9.091261,2.306562,-5.871142]],[[-2.246656,3.733134,3.513660,-0.360019,-4.357875,9.290674,-0.700168,-1.439408,-7.478113,8.414715,6.401545,-2.670605,7.666006],[0.514314,-4.964938,7.499185,5.197107,9.819584,-6.025386,1.577920,4.497329,-4.428227,-2.616153,9.017440,-1.068008,-0.707143],[-6.416169,3.690647,5.282703,-4.963892,6.339365,-7.577084,-7.016663,5.153644,-8.614447,5.854557,5.641371,4.486829,0.753092],[9.531678,-4.186022,6.703196,-4.181615,-9.714331,1.971981,-8.173582,-6.555901,3.699048,-0.518563,-6.112083,7.454531,-2.459279]],[[9.288992,4.864308,-7.206607,8.879797,-0.518223,-5.567287,7.364032,-9.125332,5.407808,9.268951,-4.863050,9.372325,-8.996043],[7.769027,2.848341,-0.555953,4.747964,9.759539,-3.834515,-7.133914,9.154946,-6.153966,6.931489,0.728030,2.367057,6.359101],[-8.870892,-8.250936,-6.407328,-9.264305,8.568307,-9.537073,-0.535988,7.561725,-0.104969,8.217337,-4.927429,9.880733,0.007137],[-9.078504,2.848550,-4.890135,-2.999241,-9.955177,-0.451865,9.621705,-3.190646,-8.250139,7.257993,4.766649,-6.270511,-4.860438]],[[-1.859940,-6.065973,-8.962910,-2.049350,-5.493466,3.744710,6.790473,3.977991,6.728250,-7.105234,3.791126,-3.421395,-8.518855],[-9.754915,7.105880,2.208020,-8.590262,4.917216,-3.757555,4.430083,-4.322086,-6.472553,-1.512832,2.930728,-7.915037,2.223151],[-6.988351,-1.185156,-0.644628,2.543714,1.925661,7.547353,1.383925,5.942543,3.630863,-4.432626,4.961645,9.065086,7.830849],[3.188153,-0.595070,4.445830,1.722283,6.501399,-8.876397,0.174877,7.827324,-6.451165,0.656568,4.250655,-3.267820,-7.378287]],[[-1.676363,7.243028,-3.129281,2.700584,-6.211217,1.417683,-9.960515,0.496077,-7.821682,9.107976,5.490332,-1.350001,3.065403],[0.676733,3.967823,2.200962,-6.053735,6.423712,-4.938209,1.779963,3.877438,-2.204257,-5.277688,0.217683,-4.205263,-4.422270],[-4.905838,-7.568201,-7.892060,1.611070,0.578554,6.728778,5.617378,-7.338269,2.188974,-6.704331,-0.435047,4.953070,-9.688478],[6.782405,3.417682,6.243214,-1.869189,9.498584,1.085836,6.271371,0.776311,-9.691969,7.781576,-2.878299,5.304571,-9.361289]],[[4.450783,-6.722510,-8.462505,-9.995408,3.555935,3.377555,2.976616,8.937888,1.461119,3.278184,3.889148,6.405916,-5.343903],[-3.487219,1.291676,-6.116436,-7.611576,-8.038637,-1.366979,-9.985169,-3.913147,-4.953121,-5.297834,4.557572,-8.414912,-4.594691],[-9.470570,-0.153441,-4.538957,-8.339721,4.983950,-3.026019,1.661520,-8.061826,-7.225505,-0.771788,-6.161858,-7.384157,-4.112772],[-0.087802,9.945311,-0.023064,5.195030,-0.445096,4.288410,7.472066,6.495873,-0.378768,-5.057435,3.259095,2.108590,-4.760101]],[[-2.612574,-4.555097,-0.840279,3.471930,-0.027402,0.933209,-8.549853,4.873324,5.081536,1.964967,-8.930786,9.526252,-8.429907],[4.779312,-7.742492,-2.826943,1.163830,4.550909,7.557425,0.692158,0.092446,1.446387,-9.067998,7.629206,8.518215,6.931848],[5.814069,6.988258,1.243357,3.398349,-3.161915,-5.158735,4.871623,1.688712,-1.604275,-3.705901,5.769175,9.805032,-4.783597],[9.029973,4.755194,9.540552,-2.754986,1.090370,-3.280115,6.927523,-6.953744,-0.819004,-7.560311,-1.128485,-7.417605,-6.133896]]], dtype = "float32")#candidate|1510|(14, 4, 13)|const|float32
bop_1511 = relay.left_shift(var_1491.astype('uint64'), const_1510.astype('uint64')) # shape=(14, 4, 13)
func_777_call = mod.get_global_var('func_777')
func_781_call = mutated_mod.get_global_var('func_781')
var_1518 = relay.var("var_1518", dtype = "float64", shape = (78,))#candidate|1518|(78,)|var|float64
const_1519 = relay.const([4.813470,-8.636280,2.305632,5.221243,3.404422,-5.483318,5.895955,8.688159,-8.898691,-3.493774,-7.250215,-5.726718,9.202298,7.656304,-8.760836,6.076208,-6.049062,5.500538,0.031872,7.573534,9.244239,0.743399,-0.114738,5.946413,0.708328,-5.124018,7.921580,8.111807,-2.374120,5.400126,-3.804417,-0.959057,0.769180,-9.822165,-9.169199,1.149483,7.715329,6.047351,0.784411,-1.125666,-8.871748,-6.581626,6.064748,-9.824733,3.831212,-1.196453,-4.541193,-4.359398,-1.505990,-8.007704,-3.360222,-9.372319,4.258468,8.108002,4.558424,0.990098,-1.969571,6.103368,9.090595,-3.269332,8.171763,-7.219064,8.176502,3.858670,7.822993,1.969938,2.403923,1.346085,1.031149,-9.487265,8.710557,-3.022511,0.432732,3.283571,9.578979,9.395708,4.280756,4.712625,-1.252819,-9.462812,-6.213237,5.796518,-0.015959,-7.692517,-3.821978,-4.173825,-8.805853,9.071165,-1.883983,-3.147717,-8.337197,-7.524490,8.121112,5.776327,6.148993,8.650955,0.888176,0.709460,-6.832632,2.264814,-3.131744,-4.518059,-7.135404,9.548915,-2.781726,-1.867171,5.653067,-8.040491,-3.571931,2.428086,-6.059877,-3.948078,4.710261,0.037970,5.748533,-2.465178,-5.432424,9.143536,8.083431,0.586063,-0.720557,-8.530938,-5.399205,2.760862,-4.018155,-5.043118,3.206726,-5.699698,6.981498,-4.441363,-3.395083,-9.355221,5.731135,7.197687,-7.124193], dtype = "float32")#candidate|1519|(135,)|const|float32
call_1517 = relay.TupleGetItem(func_777_call(relay.reshape(var_1518.astype('float64'), [13, 3, 2]), relay.reshape(var_1518.astype('float64'), [13, 3, 2]), relay.reshape(const_1519.astype('float32'), [135,]), ), 0)
call_1520 = relay.TupleGetItem(func_781_call(relay.reshape(var_1518.astype('float64'), [13, 3, 2]), relay.reshape(var_1518.astype('float64'), [13, 3, 2]), relay.reshape(const_1519.astype('float32'), [135,]), ), 0)
output = relay.Tuple([uop_1492,bop_1506,bop_1511,call_1517,var_1518,const_1519,])
output2 = relay.Tuple([uop_1492,bop_1506,bop_1511,call_1520,var_1518,const_1519,])
func_1521 = relay.Function([var_1491,var_1518,], output)
mod['func_1521'] = func_1521
mod = relay.transform.InferType()(mod)
mutated_mod['func_1521'] = func_1521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1521_call = mutated_mod.get_global_var('func_1521')
var_1523 = relay.var("var_1523", dtype = "float32", shape = (14, 4, 1))#candidate|1523|(14, 4, 1)|var|float32
var_1524 = relay.var("var_1524", dtype = "float64", shape = (78,))#candidate|1524|(78,)|var|float64
call_1522 = func_1521_call(var_1523,var_1524,)
output = call_1522
func_1525 = relay.Function([var_1523,var_1524,], output)
mutated_mod['func_1525'] = func_1525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1606 = relay.var("var_1606", dtype = "int16", shape = (4, 6, 9))#candidate|1606|(4, 6, 9)|var|int16
const_1607 = relay.const([[[5,-6,-7,7,6,-6,-5,-8,-7],[8,7,-10,-2,9,8,3,-7,-6],[-4,6,8,-6,7,10,5,5,2],[8,-4,3,-9,7,-5,-2,5,-10],[-2,-8,2,-4,-3,-10,6,2,7],[2,-4,-3,4,-10,3,-2,10,-3]],[[-9,1,6,9,-1,2,8,5,-4],[3,-2,-7,-6,-10,-10,-9,10,10],[-1,-9,-2,10,6,-2,-2,10,-9],[-10,7,-1,5,-7,10,-2,-10,3],[4,2,9,-4,-2,-6,3,-7,-10],[-9,-8,9,-8,9,1,-2,5,7]],[[-1,-6,5,-3,2,9,8,-4,-8],[4,-5,6,5,3,1,4,10,2],[-4,2,-6,-7,-10,-1,-5,4,6],[-5,7,10,7,9,-6,1,-7,7],[5,-8,-4,-3,1,-8,-9,-9,1],[4,5,-5,4,2,-10,-7,-4,10]],[[-3,8,2,3,9,8,1,-9,-5],[9,10,-3,2,-5,-6,-4,-10,2],[-8,-3,-7,8,3,4,10,7,5],[-10,1,-3,10,5,2,2,-2,-1],[-6,-7,-6,6,2,-8,5,-4,-1],[3,-8,1,-8,2,-8,1,1,2]]], dtype = "int16")#candidate|1607|(4, 6, 9)|const|int16
bop_1608 = relay.add(var_1606.astype('int16'), relay.reshape(const_1607.astype('int16'), relay.shape_of(var_1606))) # shape=(4, 6, 9)
const_1622 = relay.const([[[-9,3,7,9,10,-3,-6,6,-1],[10,-10,-6,-2,7,-9,9,4,-6],[-9,8,4,2,6,-3,-6,2,-3],[-2,1,-10,6,8,1,-3,-10,10],[4,4,-7,-6,-10,-3,-5,10,4],[-8,-9,-10,-2,-3,-6,8,4,-8]],[[1,-7,2,-3,-5,-5,-1,1,3],[4,-6,10,1,-10,2,-9,-3,3],[6,-4,-7,2,-4,-1,4,-2,4],[2,2,4,1,-6,-10,2,2,-7],[-5,-8,9,5,5,-6,1,-6,-10],[-6,4,9,-10,-9,7,1,2,2]],[[-9,9,-8,2,-2,2,-9,-5,10],[-8,-7,3,3,-7,-3,8,-7,5],[1,5,-8,-5,5,1,-4,-4,-5],[6,-10,3,-3,7,-8,-7,2,2],[9,8,-7,-9,-7,3,-1,8,-1],[7,3,-4,-8,2,3,9,-1,-7]],[[-5,1,-1,-4,3,-4,-4,-8,4],[-10,5,2,7,-1,8,9,6,5],[-6,10,2,6,2,5,-10,-8,-8],[-2,-2,3,2,-3,-4,8,9,1],[-9,-9,5,-6,-10,9,-5,-1,5],[-6,8,9,-10,-3,-2,-2,1,1]]], dtype = "int16")#candidate|1622|(4, 6, 9)|const|int16
bop_1623 = relay.maximum(const_1607.astype('uint8'), relay.reshape(const_1622.astype('uint8'), relay.shape_of(const_1607))) # shape=(4, 6, 9)
func_685_call = mod.get_global_var('func_685')
func_688_call = mutated_mod.get_global_var('func_688')
var_1637 = relay.var("var_1637", dtype = "uint32", shape = (975,))#candidate|1637|(975,)|var|uint32
call_1636 = relay.TupleGetItem(func_685_call(relay.reshape(var_1637.astype('uint32'), [975,])), 2)
call_1638 = relay.TupleGetItem(func_688_call(relay.reshape(var_1637.astype('uint32'), [975,])), 2)
func_1521_call = mod.get_global_var('func_1521')
func_1525_call = mutated_mod.get_global_var('func_1525')
var_1645 = relay.var("var_1645", dtype = "float32", shape = (56,))#candidate|1645|(56,)|var|float32
var_1646 = relay.var("var_1646", dtype = "float64", shape = (78,))#candidate|1646|(78,)|var|float64
call_1644 = relay.TupleGetItem(func_1521_call(relay.reshape(var_1645.astype('float32'), [14, 4, 1]), relay.reshape(var_1646.astype('float64'), [78,]), ), 3)
call_1647 = relay.TupleGetItem(func_1525_call(relay.reshape(var_1645.astype('float32'), [14, 4, 1]), relay.reshape(var_1646.astype('float64'), [78,]), ), 3)
bop_1671 = relay.floor_mod(call_1644.astype('float32'), relay.reshape(var_1646.astype('float32'), relay.shape_of(call_1644))) # shape=(13, 3, 2)
bop_1674 = relay.floor_mod(call_1647.astype('float32'), relay.reshape(var_1646.astype('float32'), relay.shape_of(call_1647))) # shape=(13, 3, 2)
output = relay.Tuple([bop_1608,bop_1623,call_1636,var_1637,var_1645,bop_1671,])
output2 = relay.Tuple([bop_1608,bop_1623,call_1638,var_1637,var_1645,bop_1674,])
func_1682 = relay.Function([var_1606,var_1637,var_1645,var_1646,], output)
mod['func_1682'] = func_1682
mod = relay.transform.InferType()(mod)
mutated_mod['func_1682'] = func_1682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1682_call = mutated_mod.get_global_var('func_1682')
var_1684 = relay.var("var_1684", dtype = "int16", shape = (4, 6, 9))#candidate|1684|(4, 6, 9)|var|int16
var_1685 = relay.var("var_1685", dtype = "uint32", shape = (975,))#candidate|1685|(975,)|var|uint32
var_1686 = relay.var("var_1686", dtype = "float32", shape = (56,))#candidate|1686|(56,)|var|float32
var_1687 = relay.var("var_1687", dtype = "float64", shape = (78,))#candidate|1687|(78,)|var|float64
call_1683 = func_1682_call(var_1684,var_1685,var_1686,var_1687,)
output = call_1683
func_1688 = relay.Function([var_1684,var_1685,var_1686,var_1687,], output)
mutated_mod['func_1688'] = func_1688
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1695 = relay.var("var_1695", dtype = "float32", shape = (5, 11, 8))#candidate|1695|(5, 11, 8)|var|float32
var_1696 = relay.var("var_1696", dtype = "float32", shape = (5, 11, 8))#candidate|1696|(5, 11, 8)|var|float32
bop_1697 = relay.less_equal(var_1695.astype('bool'), relay.reshape(var_1696.astype('bool'), relay.shape_of(var_1695))) # shape=(5, 11, 8)
output = relay.Tuple([bop_1697,])
output2 = relay.Tuple([bop_1697,])
func_1703 = relay.Function([var_1695,var_1696,], output)
mod['func_1703'] = func_1703
mod = relay.transform.InferType()(mod)
var_1704 = relay.var("var_1704", dtype = "float32", shape = (5, 11, 8))#candidate|1704|(5, 11, 8)|var|float32
var_1705 = relay.var("var_1705", dtype = "float32", shape = (5, 11, 8))#candidate|1705|(5, 11, 8)|var|float32
output = func_1703(var_1704,var_1705,)
func_1706 = relay.Function([var_1704,var_1705,], output)
mutated_mod['func_1706'] = func_1706
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1892 = relay.var("var_1892", dtype = "uint64", shape = (2, 7, 10))#candidate|1892|(2, 7, 10)|var|uint64
var_1893 = relay.var("var_1893", dtype = "uint64", shape = (2, 7, 10))#candidate|1893|(2, 7, 10)|var|uint64
bop_1894 = relay.minimum(var_1892.astype('uint64'), relay.reshape(var_1893.astype('uint64'), relay.shape_of(var_1892))) # shape=(2, 7, 10)
uop_1902 = relay.rsqrt(var_1893.astype('float32')) # shape=(2, 7, 10)
uop_1904 = relay.sinh(var_1892.astype('float32')) # shape=(2, 7, 10)
func_316_call = mod.get_global_var('func_316')
func_320_call = mutated_mod.get_global_var('func_320')
var_1909 = relay.var("var_1909", dtype = "uint32", shape = (975,))#candidate|1909|(975,)|var|uint32
call_1908 = relay.TupleGetItem(func_316_call(relay.reshape(var_1909.astype('uint32'), [5, 13, 15]), relay.reshape(var_1909.astype('uint32'), [5, 13, 15]), relay.reshape(var_1909.astype('uint32'), [5, 13, 15]), ), 1)
call_1910 = relay.TupleGetItem(func_320_call(relay.reshape(var_1909.astype('uint32'), [5, 13, 15]), relay.reshape(var_1909.astype('uint32'), [5, 13, 15]), relay.reshape(var_1909.astype('uint32'), [5, 13, 15]), ), 1)
bop_1940 = relay.minimum(var_1909.astype('int32'), relay.reshape(call_1908.astype('int32'), relay.shape_of(var_1909))) # shape=(975,)
bop_1943 = relay.minimum(var_1909.astype('int32'), relay.reshape(call_1910.astype('int32'), relay.shape_of(var_1909))) # shape=(975,)
uop_1952 = relay.sin(uop_1904.astype('float64')) # shape=(2, 7, 10)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
const_1961 = relay.const([2.218716,8.205912,-4.485148,1.991284,-0.824294,-3.523476,0.844088,-4.221100,-7.851005,9.903036,-1.679490,6.316467,-5.570361,-2.508776,-2.558699,-2.848286,-1.973350,-7.180410,0.836783,-3.027313,7.045438,-4.710406,-9.532940,-3.159267,4.195124,8.700919,-8.670453,-9.253365,-6.978643,-9.327352,-5.028936,5.035859,-1.161592,9.133662,7.115212,8.695335,7.788778,6.312043,-3.359919,-9.286346,3.460860,-0.528796,-8.265429,-2.653992,1.518511,0.875198,-5.659683,-6.817823,6.468062,-4.724729,-5.658727,8.689927,3.663156,1.881317,-4.338138,-8.664785,9.930284,6.382143,9.894595,7.481942,-4.832398,-4.070720,6.636666,8.455833,6.637974,0.509533,1.183445,8.431288,5.480136,5.539119,-2.035712,9.411274,-2.759894,5.281016,-3.211023,-2.718948,6.647530,4.468805,-0.304501,9.736926,9.229983,5.974125,3.368980,1.408461,7.198693,-3.542379,-5.743716,5.961558,-3.724183,-9.061487,1.311081,1.761726,-7.552518,5.544128,4.503290,-3.583157,2.470940,-5.367886,-2.877747,8.367330,-9.304470,4.633600,4.568770,3.906850,3.077895,5.848379,-8.140122,5.858108,2.688842,3.516095,-8.124221,5.158705,2.394447,-5.532941,-9.408446,0.516464,-0.281476,9.247940,-7.916729,7.771043,8.069038,-4.981686,-2.547554,-0.973359,0.221325,-9.272908,8.706696,5.960275,1.575513,-3.578270,-6.233583,-3.603031,-4.994250,-3.499325,-0.134094], dtype = "float32")#candidate|1961|(135,)|const|float32
call_1960 = relay.TupleGetItem(func_81_call(relay.reshape(const_1961.astype('float32'), [15, 1, 9])), 0)
call_1962 = relay.TupleGetItem(func_84_call(relay.reshape(const_1961.astype('float32'), [15, 1, 9])), 0)
output = relay.Tuple([bop_1894,uop_1902,bop_1940,uop_1952,call_1960,const_1961,])
output2 = relay.Tuple([bop_1894,uop_1902,bop_1943,uop_1952,call_1962,const_1961,])
func_1975 = relay.Function([var_1892,var_1893,var_1909,], output)
mod['func_1975'] = func_1975
mod = relay.transform.InferType()(mod)
var_1976 = relay.var("var_1976", dtype = "uint64", shape = (2, 7, 10))#candidate|1976|(2, 7, 10)|var|uint64
var_1977 = relay.var("var_1977", dtype = "uint64", shape = (2, 7, 10))#candidate|1977|(2, 7, 10)|var|uint64
var_1978 = relay.var("var_1978", dtype = "uint32", shape = (975,))#candidate|1978|(975,)|var|uint32
output = func_1975(var_1976,var_1977,var_1978,)
func_1979 = relay.Function([var_1976,var_1977,var_1978,], output)
mutated_mod['func_1979'] = func_1979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2076 = relay.var("var_2076", dtype = "float32", shape = ())#candidate|2076|()|var|float32
var_2077 = relay.var("var_2077", dtype = "float32", shape = (1, 14, 7))#candidate|2077|(1, 14, 7)|var|float32
bop_2078 = relay.power(var_2076.astype('float32'), var_2077.astype('float32')) # shape=(1, 14, 7)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
const_2083 = relay.const([-1.029549,1.259800,5.299461,-7.885307,2.911785,-1.050457,8.789864,6.424581,9.268600,1.584679,6.165084,-6.964071,-7.525890,-0.712821,0.952999,7.545895,-7.534568,-1.902053,7.781005,-8.194067,-0.994811,3.747830,-5.037701,-6.216623,-3.734605,-7.839986,-5.142935,-5.218584,7.703760,-9.421896,-6.506947,-0.695964,5.480777,-1.697112,1.637736,4.473182,9.508973,-0.668072,-9.509733,5.299391,-8.186305,-1.454600,5.120207,9.166190,0.258776,0.431201,0.017025,2.577056,-0.081928,-1.716301,-0.426810,0.318784,-1.884061,6.216806,-4.617445,-3.290304,-0.131277,9.051398,0.772667,-5.575373,7.605322,-5.824158,-4.461093,0.574889,-0.311285,-8.766720,3.209340,-9.830375,1.767120,-8.827650,2.765921,-6.123057,-2.860545,2.996534,-6.774668,-0.990687,1.950876,1.989879,-5.134496,-9.315701,-2.466894,-2.842140,-3.293594,3.289233,-4.900529,4.726376,-4.727914,-2.669965,-2.335547,-0.624681,3.514729,-2.428538,-9.954333,-0.246261,-1.189068,7.478610,-2.740218,-6.564101,-6.533671,-1.874324,-0.002425,-8.265819,-0.454870,9.088200,-2.301695,4.858375,-5.921368,-0.247819,3.153854,-0.561846,5.982242,-8.466733,7.289304,-2.748326,2.428883,-3.591466,9.901802,-9.470922,1.386962,-5.574750,-1.175111,-5.452856,7.788916,8.605936,7.252378,-7.368116,2.088774,-1.738633,6.719276,-0.066411,-4.153719,-9.643921,-6.803732,9.775892,-6.997112], dtype = "float32")#candidate|2083|(135,)|const|float32
call_2082 = relay.TupleGetItem(func_81_call(relay.reshape(const_2083.astype('float32'), [15, 1, 9])), 0)
call_2084 = relay.TupleGetItem(func_84_call(relay.reshape(const_2083.astype('float32'), [15, 1, 9])), 0)
output = relay.Tuple([bop_2078,call_2082,const_2083,])
output2 = relay.Tuple([bop_2078,call_2084,const_2083,])
func_2089 = relay.Function([var_2076,var_2077,], output)
mod['func_2089'] = func_2089
mod = relay.transform.InferType()(mod)
var_2090 = relay.var("var_2090", dtype = "float32", shape = ())#candidate|2090|()|var|float32
var_2091 = relay.var("var_2091", dtype = "float32", shape = (1, 14, 7))#candidate|2091|(1, 14, 7)|var|float32
output = func_2089(var_2090,var_2091,)
func_2092 = relay.Function([var_2090,var_2091,], output)
mutated_mod['func_2092'] = func_2092
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2103 = relay.const([[[10,1,4,-4,9,9,6,-4,1,7,5,1,-10],[-6,-2,6,-7,-7,-4,-1,2,-9,-7,9,2,8],[-9,-7,-5,-7,-1,10,-1,-1,9,9,2,-10,-10],[-7,-4,-10,-1,9,1,5,-10,-2,-4,-9,2,4]],[[6,1,4,8,10,-8,-6,-8,-4,1,-10,6,-3],[-6,-3,-9,6,-2,-7,-8,-8,-9,-5,3,2,3],[8,-7,-4,-6,-5,3,4,-2,6,7,8,10,2],[3,1,7,3,10,9,2,10,5,-1,-4,-9,-2]],[[-6,-10,-10,-4,9,8,-7,9,6,-8,-9,2,-2],[-8,9,7,4,6,2,-5,-3,-3,3,6,7,6],[9,-7,-4,1,7,-9,-7,5,6,10,-2,2,9],[3,-4,-4,-6,-3,8,-4,-1,-5,9,-8,9,4]]], dtype = "uint16")#candidate|2103|(3, 4, 13)|const|uint16
var_2104 = relay.var("var_2104", dtype = "uint16", shape = (3, 4, 13))#candidate|2104|(3, 4, 13)|var|uint16
bop_2105 = relay.logical_xor(const_2103.astype('uint16'), relay.reshape(var_2104.astype('uint16'), relay.shape_of(const_2103))) # shape=(3, 4, 13)
func_685_call = mod.get_global_var('func_685')
func_688_call = mutated_mod.get_global_var('func_688')
const_2112 = relay.const([-9,-2,8,10,-10,7,9,-5,5,3,9,6,6,2,-10,4,1,-10,-6,8,7,5,5,-4,-7,-8,-2,10,10,1,-2,-9,1,-1,2,-4,7,4,-9,-6,-7,5,-1,-7,-8,10,5,2,-9,-4,-6,-9,-10,-7,-3,-7,7,2,-8,2,-9,-5,-2,-2,-4,3,7,-3,6,5,-10,4,6,-9,4,8,4,8,4,6,-6,-8,-2,9,-8,1,-9,-9,-10,-9,10,8,5,-7,-7,7,-3,-8,3,-4,4,-10,10,-9,-6,5,-8,-9,10,-9,10,-2,-8,-9,-8,1,8,-6,-1,-7,3,-4,-4,3,-8,2,-10,-10,-7,-9,-1,8,4,-6,-10,3,-4,4,7,-5,-2,2,3,10,2,-6,2,2,9,2,-2,3,-1,5,6,4,7,10,9,-10,9,-3,2,-10,3,2,-6,-1,-4,6,8,-10,7,5,-1,-6,4,5,5,9,-7,3,-8,2,-3,-3,-8,4,-4,3,7,-8,-9,7,6,1,-6,7,-7,5,-7,8,3,3,4,-3,-5,10,-3,9,-2,3,3,2,-8,9,-7,-3,3,-8,-3,-8,3,6,4,5,4,-5,-7,6,-6,-3,5,5,-3,7,-5,8,-2,6,-8,3,9,8,7,-1,10,-7,-9,5,7,-10,4,4,10,3,1,1,-5,7,-2,6,2,9,8,-5,-3,-9,3,-2,-1,3,10,-5,-1,-9,-1,-5,10,6,7,5,6,-6,5,-2,-4,2,8,-10,-10,-2,-4,7,2,-4,-5,-8,2,2,3,-6,8,2,5,-5,-3,-7,-5,-4,8,-5,-6,-5,-6,-8,10,7,-1,-4,-2,-3,-5,3,5,-6,-5,7,5,-2,9,-1,5,7,-6,4,9,5,8,-1,-7,-7,9,6,7,4,-9,7,2,1,6,-7,3,-6,-2,-5,5,1,-5,7,-6,-10,-5,-10,2,6,-7,2,7,-10,-6,-9,-6,-4,-9,4,1,2,-10,2,6,-9,-10,-2,8,7,-6,6,7,4,10,-1,4,6,8,8,-5,6,8,2,9,-4,6,-8,10,6,1,-3,-1,-1,-9,2,5,-9,5,3,-3,-10,6,9,-9,8,-2,-7,1,1,-6,-2,-8,-6,-4,-8,5,-5,3,7,-3,-4,-7,10,-6,8,4,2,2,-7,-6,-5,-1,4,-6,-8,7,4,10,1,-4,9,-10,-10,-9,-1,9,8,6,-6,2,-1,-3,-2,-8,-10,-6,10,9,10,-6,5,-9,-7,-6,9,-4,-8,7,1,-4,8,1,-8,8,10,-1,9,-1,-4,7,4,4,-8,3,6,10,9,-4,2,7,7,-9,7,-3,7,-4,1,5,1,-1,-5,-3,-2,3,10,-8,-7,3,6,-5,-6,-6,-9,8,-8,6,-10,10,-7,-8,3,6,-2,2,-5,-1,-5,1,9,-3,8,10,8,2,5,2,3,-7,-7,2,-5,-6,-1,6,6,-7,-9,-4,9,10,-5,1,10,-4,-7,2,1,-4,-5,-4,-10,-7,8,-5,9,-10,-8,4,-8,-9,-5,7,-1,2,-1,-8,5,-1,-9,1,-2,2,-3,7,5,6,-7,7,4,-5,-6,-10,-8,-6,-7,-5,-10,-6,3,4,-1,7,-5,-7,4,6,5,-2,6,2,-5,-10,-3,-7,2,-4,2,-3,6,6,10,-1,-9,-7,-1,6,-5,-10,-3,-7,-8,9,2,9,-10,9,8,-6,-5,1,2,-9,-4,-7,7,5,3,-9,4,5,4,5,-6,-8,3,-6,-7,-4,-5,1,5,9,-7,-4,-6,-6,-5,-4,-1,-3,-4,-1,-3,3,8,-9,-9,10,9,-9,-5,5,6,-10,-2,1,-9,6,-9,-9,2,-9,-8,-8,-7,2,-2,9,-6,4,1,5,-10,-3,9,-8,-1,3,8,-6,8,6,-7,-7,5,3,7,-7,9,5,-3,3,10,5,7,4,1,7,-4,-1,4,-4,-3,9,2,-2,-7,-8,10,8,5,5,1,-4,-4,3,-10,-2,-9,-3,-5,7,-9,-10,8,-8,-9,1,-5,-4,-9,-9,-5,9,10,-6,-8,-6,7,10,3,10,-1,1,-5,4,-3,2,4,3,-5,10,3,4,3,7,2,-9,8,8,4,-7,5,-4,-1,2,7,1,1,9,-9,-1,4,3,-7,-7,-1,7,-6,-4,7,4,1,1,3,3,6,3,3,6,-7,2,-9,-5,-9,3,6,-7,3,6,-9,7,4,-9,-6,-10,8,-2,-2,-10,-5,-6,-10,-7,-2,-10,3,-8,7,-5,-10,7,-6,5,-7,10,9,2,-8,4,-1,10,-2,-10,-6,6,-1,-6,-4,-6,5,3,-9,-3,4,-6,-2,1,-7,-4,8,-10,5,-6,6,-9,6,-5,7,-2,5,-9,8,-2,-1,-7,8,-7,-5,3,-3,-10,-6,-5,-5,5,-7,-7,-4,-10,-7,3,-6,8,1,3,-6,6,10,-5,8,-2,-6,-2,10,-3,-2,-2,-7,10,-4,6,5,-1,1,9,6,8,2,2,5,9,-2,-6,1,-8,10,-6,6,-2,-1,-10,-4,-1,-10,8,-8,3], dtype = "uint32")#candidate|2112|(975,)|const|uint32
call_2111 = relay.TupleGetItem(func_685_call(relay.reshape(const_2112.astype('uint32'), [975,])), 1)
call_2113 = relay.TupleGetItem(func_688_call(relay.reshape(const_2112.astype('uint32'), [975,])), 1)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
const_2120 = relay.const([9.486254,3.016449,6.749497,-3.410920,-6.177245,7.072742,4.195006,5.974477,-0.400059,-1.517115,9.902709,8.319073,0.476283,-2.605431,8.860932,6.079940,-5.156897,-6.815397,7.462477,2.510489,3.989359,3.720446,-6.244851,7.958848,3.050893,-7.538570,-9.168845,5.701869,6.425914,1.676052,8.071795,3.497025,4.067753,6.404550,-6.156544,-5.712385,9.736861,-7.406631,7.867723,-1.839359,-9.428413,4.946645,-3.344309,-3.235661,-9.027879,-2.319060,-9.880077,5.737487,-5.168868,2.197068,2.780413,-7.343779,2.692978,-9.396823,-9.833999,3.300942,-8.871771,8.186574,-4.232680,-2.867572,0.982544,-1.702462,-4.238173,3.412403,1.188559,0.310098,7.847364,9.097388,7.698692,2.452051,8.549688,-7.644733,3.799094,-0.985643,3.499726,-6.074745,-8.219435,3.845080,-6.399448,9.834340,8.945177,9.097890,-3.731574,1.559292,-8.464341,2.421030,-8.143021,8.401751,2.019907,2.692624,-8.828047,-6.578068,-5.481196,2.337382,-6.117582,-0.437931,-5.358737,-2.561205,5.407290,-7.784803,-2.012526,3.976172,2.719050,-2.618084,-0.006075,5.849001,5.946054,4.761089,4.759346,3.082006,5.443628,1.595438,9.260100,-0.525046,-0.682627,-9.962320,-7.094407,8.964500,8.756452,4.763721,7.698739,-1.291446,-4.904104,-7.739691,6.010303,8.204670,-1.583099,-0.675689,5.045123,-5.854574,9.619398,-5.305778,-6.337730,2.760157,-0.417673], dtype = "float32")#candidate|2120|(135,)|const|float32
call_2119 = relay.TupleGetItem(func_81_call(relay.reshape(const_2120.astype('float32'), [15, 1, 9])), 0)
call_2121 = relay.TupleGetItem(func_84_call(relay.reshape(const_2120.astype('float32'), [15, 1, 9])), 0)
output = relay.Tuple([bop_2105,call_2111,const_2112,call_2119,const_2120,])
output2 = relay.Tuple([bop_2105,call_2113,const_2112,call_2121,const_2120,])
func_2129 = relay.Function([var_2104,], output)
mod['func_2129'] = func_2129
mod = relay.transform.InferType()(mod)
mutated_mod['func_2129'] = func_2129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2130 = relay.var("var_2130", dtype = "uint16", shape = (3, 4, 13))#candidate|2130|(3, 4, 13)|var|uint16
func_2129_call = mutated_mod.get_global_var('func_2129')
call_2131 = func_2129_call(var_2130)
output = call_2131
func_2132 = relay.Function([var_2130], output)
mutated_mod['func_2132'] = func_2132
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2387 = relay.var("var_2387", dtype = "uint32", shape = (9, 12, 3))#candidate|2387|(9, 12, 3)|var|uint32
var_2388 = relay.var("var_2388", dtype = "uint32", shape = (9, 12, 3))#candidate|2388|(9, 12, 3)|var|uint32
bop_2389 = relay.not_equal(var_2387.astype('bool'), relay.reshape(var_2388.astype('bool'), relay.shape_of(var_2387))) # shape=(9, 12, 3)
uop_2393 = relay.cosh(var_2388.astype('float64')) # shape=(9, 12, 3)
bop_2395 = relay.right_shift(uop_2393.astype('uint32'), relay.reshape(var_2388.astype('uint32'), relay.shape_of(uop_2393))) # shape=(9, 12, 3)
output = relay.Tuple([bop_2389,bop_2395,])
output2 = relay.Tuple([bop_2389,bop_2395,])
func_2400 = relay.Function([var_2387,var_2388,], output)
mod['func_2400'] = func_2400
mod = relay.transform.InferType()(mod)
var_2401 = relay.var("var_2401", dtype = "uint32", shape = (9, 12, 3))#candidate|2401|(9, 12, 3)|var|uint32
var_2402 = relay.var("var_2402", dtype = "uint32", shape = (9, 12, 3))#candidate|2402|(9, 12, 3)|var|uint32
output = func_2400(var_2401,var_2402,)
func_2403 = relay.Function([var_2401,var_2402,], output)
mutated_mod['func_2403'] = func_2403
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2442 = relay.var("var_2442", dtype = "uint8", shape = ())#candidate|2442|()|var|uint8
var_2443 = relay.var("var_2443", dtype = "uint8", shape = (12, 1, 6))#candidate|2443|(12, 1, 6)|var|uint8
bop_2444 = relay.bitwise_or(var_2442.astype('uint8'), var_2443.astype('uint8')) # shape=(12, 1, 6)
output = relay.Tuple([bop_2444,])
output2 = relay.Tuple([bop_2444,])
func_2447 = relay.Function([var_2442,var_2443,], output)
mod['func_2447'] = func_2447
mod = relay.transform.InferType()(mod)
var_2448 = relay.var("var_2448", dtype = "uint8", shape = ())#candidate|2448|()|var|uint8
var_2449 = relay.var("var_2449", dtype = "uint8", shape = (12, 1, 6))#candidate|2449|(12, 1, 6)|var|uint8
output = func_2447(var_2448,var_2449,)
func_2450 = relay.Function([var_2448,var_2449,], output)
mutated_mod['func_2450'] = func_2450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2786 = relay.var("var_2786", dtype = "uint32", shape = ())#candidate|2786|()|var|uint32
var_2787 = relay.var("var_2787", dtype = "uint32", shape = (14, 16, 10))#candidate|2787|(14, 16, 10)|var|uint32
bop_2788 = relay.bitwise_or(var_2786.astype('uint32'), var_2787.astype('uint32')) # shape=(14, 16, 10)
func_2129_call = mod.get_global_var('func_2129')
func_2132_call = mutated_mod.get_global_var('func_2132')
const_2806 = relay.const([9,-10,-3,-4,10,9,5,-2,-5,-1,8,-3,-7,-10,-5,7,-8,9,-4,10,-4,-9,9,8,-4,2,-8,-9,-7,1,10,6,-7,-9,9,-2,-10,-2,4,-3,-8,10,-10,-2,-10,3,-1,5,-5,8,4,6,2,-3,5,-5,-2,10,6,3,3,5,4,-3,-6,2,2,4,-4,-2,-4,4,4,8,-4,-5,6,4,-9,8,9,-5,-5,-6,-5,-10,7,-3,-7,-10,-3,-1,-2,8,3,7,5,4,-9,1,-3,3,6,-1,-6,-6,-4,7,-2,-9,10,-9,-8,-6,-7,2,-1,-8,-8,2,9,-4,-6,1,7,-5,6,5,8,10,10,3,-5,-10,1,-1,-1,3,10,-5,4,6,-5,3,-4,-7,4,-6,1,6,-8,-2,3,-6,9,-10], dtype = "uint16")#candidate|2806|(156,)|const|uint16
call_2805 = relay.TupleGetItem(func_2129_call(relay.reshape(const_2806.astype('uint16'), [3, 4, 13])), 1)
call_2807 = relay.TupleGetItem(func_2132_call(relay.reshape(const_2806.astype('uint16'), [3, 4, 13])), 1)
output = relay.Tuple([bop_2788,call_2805,const_2806,])
output2 = relay.Tuple([bop_2788,call_2807,const_2806,])
func_2813 = relay.Function([var_2786,var_2787,], output)
mod['func_2813'] = func_2813
mod = relay.transform.InferType()(mod)
var_2814 = relay.var("var_2814", dtype = "uint32", shape = ())#candidate|2814|()|var|uint32
var_2815 = relay.var("var_2815", dtype = "uint32", shape = (14, 16, 10))#candidate|2815|(14, 16, 10)|var|uint32
output = func_2813(var_2814,var_2815,)
func_2816 = relay.Function([var_2814,var_2815,], output)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2843 = relay.var("var_2843", dtype = "float64", shape = ())#candidate|2843|()|var|float64
var_2844 = relay.var("var_2844", dtype = "float64", shape = (11, 6, 4))#candidate|2844|(11, 6, 4)|var|float64
bop_2845 = relay.power(var_2843.astype('float64'), var_2844.astype('float64')) # shape=(11, 6, 4)
uop_2848 = relay.tan(bop_2845.astype('float64')) # shape=(11, 6, 4)
output = uop_2848
output2 = uop_2848
func_2860 = relay.Function([var_2843,var_2844,], output)
mod['func_2860'] = func_2860
mod = relay.transform.InferType()(mod)
var_2861 = relay.var("var_2861", dtype = "float64", shape = ())#candidate|2861|()|var|float64
var_2862 = relay.var("var_2862", dtype = "float64", shape = (11, 6, 4))#candidate|2862|(11, 6, 4)|var|float64
output = func_2860(var_2861,var_2862,)
func_2863 = relay.Function([var_2861,var_2862,], output)
mutated_mod['func_2863'] = func_2863
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2965 = relay.var("var_2965", dtype = "float64", shape = (14, 16, 7))#candidate|2965|(14, 16, 7)|var|float64
uop_2966 = relay.sin(var_2965.astype('float64')) # shape=(14, 16, 7)
uop_2982 = relay.acos(uop_2966.astype('float64')) # shape=(14, 16, 7)
func_685_call = mod.get_global_var('func_685')
func_688_call = mutated_mod.get_global_var('func_688')
const_2992 = relay.const([-6,-4,-2,3,-2,-2,6,5,-8,1,7,10,9,4,-1,-7,-1,-1,4,8,10,-2,-1,2,-5,9,-6,3,8,-5,-6,7,5,-8,-10,4,8,8,5,1,5,-4,-10,8,6,-6,-8,-10,10,4,8,-10,6,-8,-10,-2,10,7,5,-9,-1,-5,-7,-3,-5,-7,-5,-1,-4,3,-9,-8,1,10,-3,8,3,4,-8,-9,4,-8,-2,1,8,-10,8,-6,3,4,-5,3,-6,2,-6,9,-6,8,-5,-3,-4,2,9,1,-5,2,-9,-2,2,9,2,7,-6,-7,5,-8,3,2,-7,5,-10,-6,2,4,-9,-1,4,2,-2,-2,6,-7,-9,2,2,10,6,2,3,1,2,4,7,-5,2,5,9,-1,-1,-6,2,-6,3,8,6,7,-1,-4,-6,9,-6,10,-6,-4,3,1,-8,-6,5,-5,3,-10,5,-3,3,-1,-6,-6,1,9,-2,9,-7,8,-9,6,-7,6,-8,-4,-1,-10,5,1,-6,2,-1,7,-6,-4,10,-6,-4,-8,3,5,-7,3,3,-10,6,-8,-2,7,-9,-4,-10,-5,-5,9,7,2,-1,7,-10,-2,8,-3,4,-8,-10,-2,-5,7,4,-7,-9,8,-3,3,-2,8,-4,10,-3,-1,-1,5,1,-5,7,-9,-9,6,10,7,-4,-3,8,-6,-10,-3,-1,-6,-8,1,-2,-2,5,-5,9,8,9,-4,3,-7,1,5,-8,-6,3,-4,8,-8,-7,-10,6,-2,9,1,7,8,-10,10,7,6,5,-5,-7,-8,7,-1,-5,-8,-8,-8,-9,-5,-1,-8,-2,8,-6,2,7,10,-5,-5,-3,-7,-1,7,3,-10,-8,-3,-5,-8,6,-8,10,-5,8,-7,4,-3,-9,7,-4,-8,-7,3,-2,7,-10,10,-3,-5,6,4,-6,-5,1,8,-2,8,-7,-3,3,-8,-7,3,3,2,1,-1,3,1,9,1,-6,-1,1,2,8,-7,8,4,9,5,2,-5,2,-10,5,-4,-10,2,1,-5,5,3,-1,7,4,8,-7,-4,-10,2,8,6,9,1,-3,-10,-10,2,-1,-3,-2,-3,-5,8,3,-1,-3,1,5,5,-10,-6,5,2,-8,3,6,-7,-4,8,-4,-8,-4,-1,3,-6,-9,1,-8,-2,-10,6,-2,8,-7,-3,5,-8,-2,-7,4,-8,-6,9,-6,2,-7,-1,-1,-4,7,-1,-1,-1,-9,10,2,8,-6,1,9,7,2,-6,-9,3,-8,-8,5,-3,-10,10,10,-9,7,8,5,-4,5,10,-8,2,7,-6,1,-7,-10,-2,-4,-7,-3,7,-2,3,-10,-3,-5,-8,-7,5,2,9,-6,4,-4,-1,8,2,-2,1,-9,-2,-1,9,5,-8,-3,-10,-9,-10,-7,-9,2,9,8,6,4,6,-8,-3,-8,-9,9,-9,-6,-3,-2,10,-4,6,8,-3,-9,6,-3,-2,2,-1,3,-1,-1,-3,-5,-6,3,4,3,-4,8,2,10,2,5,3,5,8,6,-6,-6,3,4,3,-7,-4,6,8,-1,-10,-6,-6,-6,-7,-8,5,-7,3,10,-3,-2,3,2,-6,4,1,8,2,-2,6,4,-3,-4,2,-4,-10,-1,-6,6,8,-7,-1,6,9,-2,7,-10,7,-7,-7,-6,-7,2,2,5,-8,-8,-9,10,-2,5,-10,-10,-9,8,9,-3,-10,10,-2,1,9,-7,-2,6,-1,3,-8,-8,1,-2,-9,7,-1,3,-3,-3,4,1,-7,1,-10,9,7,-4,3,-1,3,4,-6,-7,-1,-3,10,-10,3,-7,6,-2,5,-3,3,3,-3,-10,-3,-10,-7,1,9,4,-3,-8,9,3,-7,2,-4,6,3,-6,4,3,1,9,-5,1,-4,-8,10,-6,-2,6,5,-3,1,5,5,7,1,-5,10,6,-6,8,-8,2,-3,7,-4,8,-10,-1,2,3,5,-2,6,9,-4,8,1,3,-10,-4,1,-10,-7,-7,8,-2,8,7,4,5,-3,2,-5,-10,7,9,-7,10,1,-1,-5,-1,-9,-6,4,-2,6,-3,-1,8,-6,-6,8,-7,3,-8,-2,-3,9,5,3,-2,-1,10,7,-10,6,6,-1,-3,-10,5,9,-5,7,2,7,-9,-9,10,6,1,-5,-6,-1,-3,9,4,-3,-6,1,10,-4,-8,-7,-10,-10,7,-9,4,-3,2,-4,-9,5,9,5,-6,8,3,4,-10,-6,2,9,5,6,3,-4,-8,8,-7,-1,-2,-8,-4,-8,-1,-1,-10,-10,2,2,7,-8,7,4,-6,10,4,3,-2,-4,3,-5,-6,8,2,-5,-8,-4,6,-2,5,-2,-9,8,-4,-4,8,10,6,-3,-7,-9,-1,1,-3,2,4,6,9,-3,-6,1,-8,-9,-8,5,3,4,9,3,-8,-1,-1,6,-10,-4,-5,2,6,10,-4,-3,10,-10,3,-2,-8,-5,-1,10,9,-10,9,-10,1,-10,6,1,1,7,-3,-6,4,-2,2,6,6,-8,8,-1,-9,-6,-4,-2,-6,-8,-2,2,6,2,-5,-9,-6,5,6,-7,-7,-1,9], dtype = "uint32")#candidate|2992|(975,)|const|uint32
call_2991 = relay.TupleGetItem(func_685_call(relay.reshape(const_2992.astype('uint32'), [975,])), 0)
call_2993 = relay.TupleGetItem(func_688_call(relay.reshape(const_2992.astype('uint32'), [975,])), 0)
func_2447_call = mod.get_global_var('func_2447')
func_2450_call = mutated_mod.get_global_var('func_2450')
var_2999 = relay.var("var_2999", dtype = "uint8", shape = ())#candidate|2999|()|var|uint8
const_3000 = relay.const([6,4,-9,7,5,1,9,5,4,-10,10,-9,3,-3,10,4,1,-5,-4,-6,-6,-1,5,-5,-9,9,2,-8,-9,2,4,7,-3,6,7,-6,-9,10,-4,2,-1,-3,-8,-7,-1,-8,4,8,2,-5,-8,-3,-10,8,9,5,10,10,10,-6,-6,-4,2,8,-10,2,-5,-2,10,-9,9,-7], dtype = "uint8")#candidate|3000|(72,)|const|uint8
call_2998 = relay.TupleGetItem(func_2447_call(relay.reshape(var_2999.astype('uint8'), []), relay.reshape(const_3000.astype('uint8'), [12, 1, 6]), ), 0)
call_3001 = relay.TupleGetItem(func_2450_call(relay.reshape(var_2999.astype('uint8'), []), relay.reshape(const_3000.astype('uint8'), [12, 1, 6]), ), 0)
func_1022_call = mod.get_global_var('func_1022')
func_1026_call = mutated_mod.get_global_var('func_1026')
var_3016 = relay.var("var_3016", dtype = "uint32", shape = (30,))#candidate|3016|(30,)|var|uint32
var_3017 = relay.var("var_3017", dtype = "float64", shape = (78,))#candidate|3017|(78,)|var|float64
call_3015 = relay.TupleGetItem(func_1022_call(relay.reshape(var_3016.astype('uint32'), [3, 5, 2]), relay.reshape(var_3017.astype('float64'), [78,]), ), 1)
call_3018 = relay.TupleGetItem(func_1026_call(relay.reshape(var_3016.astype('uint32'), [3, 5, 2]), relay.reshape(var_3017.astype('float64'), [78,]), ), 1)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
var_3024 = relay.var("var_3024", dtype = "float32", shape = (135,))#candidate|3024|(135,)|var|float32
call_3023 = relay.TupleGetItem(func_81_call(relay.reshape(var_3024.astype('float32'), [15, 1, 9])), 0)
call_3025 = relay.TupleGetItem(func_84_call(relay.reshape(var_3024.astype('float32'), [15, 1, 9])), 0)
output = relay.Tuple([uop_2982,call_2991,const_2992,call_2998,var_2999,const_3000,call_3015,var_3016,var_3017,call_3023,var_3024,])
output2 = relay.Tuple([uop_2982,call_2993,const_2992,call_3001,var_2999,const_3000,call_3018,var_3016,var_3017,call_3025,var_3024,])
func_3044 = relay.Function([var_2965,var_2999,var_3016,var_3017,var_3024,], output)
mod['func_3044'] = func_3044
mod = relay.transform.InferType()(mod)
mutated_mod['func_3044'] = func_3044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3044_call = mutated_mod.get_global_var('func_3044')
var_3046 = relay.var("var_3046", dtype = "float64", shape = (14, 16, 7))#candidate|3046|(14, 16, 7)|var|float64
var_3047 = relay.var("var_3047", dtype = "uint8", shape = ())#candidate|3047|()|var|uint8
var_3048 = relay.var("var_3048", dtype = "uint32", shape = (30,))#candidate|3048|(30,)|var|uint32
var_3049 = relay.var("var_3049", dtype = "float64", shape = (78,))#candidate|3049|(78,)|var|float64
var_3050 = relay.var("var_3050", dtype = "float32", shape = (135,))#candidate|3050|(135,)|var|float32
call_3045 = func_3044_call(var_3046,var_3047,var_3048,var_3049,var_3050,)
output = call_3045
func_3051 = relay.Function([var_3046,var_3047,var_3048,var_3049,var_3050,], output)
mutated_mod['func_3051'] = func_3051
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3076 = relay.var("var_3076", dtype = "float32", shape = (2, 11, 13))#candidate|3076|(2, 11, 13)|var|float32
uop_3077 = relay.sinh(var_3076.astype('float32')) # shape=(2, 11, 13)
output = relay.Tuple([uop_3077,])
output2 = relay.Tuple([uop_3077,])
func_3080 = relay.Function([var_3076,], output)
mod['func_3080'] = func_3080
mod = relay.transform.InferType()(mod)
mutated_mod['func_3080'] = func_3080
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3081 = relay.var("var_3081", dtype = "float32", shape = (2, 11, 13))#candidate|3081|(2, 11, 13)|var|float32
func_3080_call = mutated_mod.get_global_var('func_3080')
call_3082 = func_3080_call(var_3081)
output = call_3082
func_3083 = relay.Function([var_3081], output)
mutated_mod['func_3083'] = func_3083
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3131 = relay.const([[[4.803855,-2.829533,-0.121109,-7.250797,3.878624,-4.764363,-1.847219,-6.364387,-0.104452,-3.772650,-5.441262,3.599936,-9.109641,0.347899,-1.087517],[-2.841870,3.968274,-8.955034,-8.928164,-6.217157,-4.705159,-1.776541,-7.934888,-3.505875,8.455005,-2.646543,4.223036,-6.634775,6.124928,-0.428880],[-4.831989,4.859614,2.864518,-6.274132,6.157869,7.119310,0.153994,-6.832800,-4.207649,-3.993220,5.692052,-8.600746,4.212205,-0.151877,-2.831805],[-0.723783,8.989890,-1.223420,3.066295,-5.195143,-5.668523,-9.980843,-1.152258,2.052480,7.795531,-6.317194,-2.602658,4.690155,7.288925,-6.238518],[-9.911363,-5.622979,8.566720,9.817462,9.506073,2.375251,3.221119,-7.899619,-8.469353,6.730851,4.433827,4.786169,-3.556428,7.857836,-4.718858],[3.582966,-0.937111,2.574677,2.822257,-9.072567,-8.978777,-9.365292,1.816502,5.973876,-1.143533,8.265065,-3.040061,-1.995344,-5.802830,-3.593722],[8.284874,9.470513,-3.056455,5.819560,5.364342,-5.159853,9.562695,-3.372851,9.253842,2.455601,-4.032382,-7.040649,7.863587,6.337259,-6.234034],[-2.617414,0.895801,-8.325869,-6.649190,4.037602,0.124980,-0.538670,-8.655903,-6.453346,-9.938532,-7.808437,-1.226698,-8.962124,4.080020,6.389914],[9.823255,4.382631,-8.856190,-1.407400,-5.832108,-8.528731,-6.169483,-3.366570,0.031127,-3.324262,-2.206314,-6.916633,6.537349,-0.427699,-0.480877],[5.104974,-1.291141,3.249226,-7.231722,2.514286,3.466176,-5.992636,-9.479377,6.795499,6.340143,-8.539416,-5.944029,0.528771,6.919889,-8.802830],[4.939341,0.298663,-4.796913,-6.616917,8.463426,0.486662,-0.665967,-4.587359,5.724065,-9.250399,7.243773,-6.696513,-0.411500,-5.570719,-4.587764],[1.264244,-5.667252,9.001415,7.137053,0.745851,4.716419,-2.679677,-7.431376,8.866929,-2.275916,1.266962,-5.952652,1.440592,9.653612,-7.680208],[-7.157520,7.848405,-1.086331,8.729686,5.283864,-3.251114,-8.395130,-3.685006,1.782766,-5.404141,9.217163,-2.856143,4.556659,-5.977519,7.632676],[-4.292054,7.451402,-3.149174,-2.475859,2.205333,-6.378596,8.632614,-3.845938,6.607153,1.385345,4.374136,7.977024,-2.236129,8.142380,9.481003],[3.244670,-7.020018,-7.828796,-5.582167,7.333805,-7.571523,-6.016795,-0.041995,5.575811,-0.777326,6.945511,4.798096,2.506741,0.121873,6.281167],[1.667617,3.041998,3.377663,-7.013371,-3.915477,5.554640,3.456776,-6.337212,3.944665,-9.350775,-8.077094,4.118622,-9.221007,0.944462,-8.923507]],[[7.630358,6.954942,1.814706,-3.949131,0.881189,2.997403,5.048135,-1.447198,-5.283765,0.754432,5.211809,-9.820706,2.242143,-5.044484,0.822791],[9.828148,-5.974872,9.400291,3.607612,-9.153987,-7.594804,-9.665664,-1.444102,-2.465414,-3.274922,0.116703,2.456986,-9.643260,1.140327,-6.534469],[3.277519,5.191272,-2.340779,-3.669441,-3.449943,-7.344361,-5.651712,-1.507779,1.075505,-5.746871,-5.775924,-1.882892,3.544000,-7.658162,3.393386],[4.529476,4.821271,-7.203307,7.366500,0.527986,0.442902,9.172577,-9.525907,3.655254,-1.977326,1.789493,3.420819,-5.528498,2.499823,6.724990],[4.971474,6.065261,0.965997,7.665517,-6.231349,-1.319698,-9.155196,-8.085214,6.860553,6.300246,3.988859,-4.118474,-2.204651,3.038901,-4.459706],[-3.679463,-0.815217,-1.686294,9.557432,-7.721099,-2.600385,-6.736259,-0.438468,-2.299743,-3.549605,3.823351,-7.208627,-0.092068,2.943232,-8.086173],[2.746115,0.144172,5.830717,9.612490,2.004103,-6.390071,9.088613,8.549587,7.703748,2.212395,3.306292,1.098477,5.779647,-1.446413,-6.546536],[-4.040928,7.293456,2.241785,0.079684,8.010811,-9.324222,-6.820213,-5.307423,-7.441206,6.427798,2.842846,-7.462488,5.379919,4.376424,-1.776452],[-9.551165,9.748863,2.818392,-0.053430,8.500019,5.799204,-4.509678,2.036356,0.135240,-1.780074,-1.828338,3.735821,1.174705,-2.927806,-3.560914],[-3.561572,2.660180,-0.401799,-6.679936,9.706654,2.635166,5.626032,-9.297291,-4.515055,-2.094234,1.909136,2.897190,-0.562440,9.717278,0.932033],[7.190595,-7.170659,0.483242,8.541495,-2.953418,7.919048,-1.565609,3.684120,-5.572570,-9.624164,-3.973314,4.546879,6.625379,-4.220527,-4.006557],[-5.505652,2.807262,-7.175896,-8.146675,-0.099331,-0.462803,-2.314401,5.661390,3.446827,2.902039,-4.638897,8.368050,6.170636,5.400200,2.604715],[2.273157,-2.979787,4.127098,1.028940,-1.035160,-4.020327,-4.482892,4.378637,-5.004089,3.894869,9.761101,2.596200,0.300493,7.068218,1.211600],[-4.657710,-8.179240,2.785882,5.879975,3.467117,9.583119,-6.108581,-3.185403,0.224678,-5.163254,9.891987,-8.669085,6.159516,5.633681,9.713279],[3.392591,-9.845526,-6.246498,6.001719,-2.669260,8.657438,-0.242342,2.478730,-1.017144,0.101057,0.781109,-8.385118,-9.644116,6.277460,-4.700048],[-2.278639,-2.889925,7.019213,-9.084388,-2.352673,-8.843240,-8.087653,4.898532,4.379133,-5.209962,0.409020,1.614845,-4.485807,0.825791,-6.217251]],[[-0.429421,0.773163,0.236510,9.926898,-9.519152,-2.360625,9.305212,9.663982,5.529050,-4.048321,-0.794903,0.014943,1.029124,7.680537,-6.007354],[-0.389291,-8.254668,8.148827,9.490805,7.439017,9.245070,-5.141037,9.998066,9.242245,-0.588990,-4.653186,9.165184,6.107402,7.061606,2.665375],[-9.417108,-1.938316,-2.641395,-4.434839,-7.837354,5.271164,6.866335,8.786657,8.834843,4.751076,-9.900233,-8.523870,-8.730980,8.688738,-8.815182],[4.138627,-0.927803,3.254367,9.702981,-4.056678,-2.143053,7.724454,3.893278,-9.938955,-3.449426,4.444769,4.081657,-2.748559,9.852591,-6.939596],[6.258360,-6.008171,0.962586,-3.325286,5.303971,3.209913,-1.297190,6.992760,9.814203,-4.559213,-5.880115,-5.238306,-3.536222,0.720131,-4.134496],[2.958320,7.711163,-5.720948,-9.568198,0.196115,0.004140,9.517235,-4.948172,-3.050934,-9.930668,4.682010,-1.057065,-0.607394,-2.253491,-0.044930],[2.709418,-2.459774,0.303024,-9.293184,8.434804,1.242982,-9.568794,-3.885191,5.093703,-1.448392,-2.767650,-0.702961,5.115876,8.987248,-6.657826],[8.723051,7.614600,-5.555749,-4.240184,-0.500420,5.375137,-1.660495,-7.106319,-6.994980,5.154508,4.256145,-8.016450,-7.584518,2.039007,4.805899],[7.632894,9.464592,4.755673,7.071108,-6.358362,8.141669,2.240213,6.438917,5.961035,-1.549946,-6.223401,-4.044620,7.613823,8.483423,-5.250402],[9.011380,5.548216,-1.783813,-9.394270,-7.394164,-1.718269,-6.399438,8.242165,7.676790,4.722911,-7.114114,-7.272437,-9.585465,1.723946,-2.343600],[6.879280,-2.278587,-9.580840,8.262155,-3.009442,-8.216037,3.420366,7.978032,-8.087763,8.327213,-0.696147,-2.932268,-4.628328,-7.118659,-8.303877],[3.222465,-5.518424,-2.913416,6.338677,-7.647209,5.549422,-9.730429,1.852829,6.714768,-9.405467,-6.011473,-8.750889,7.215340,6.984329,7.743138],[-0.010049,2.090252,-9.329358,-3.599383,4.805839,5.835718,1.877892,-0.406377,3.629786,-9.874962,-3.638666,-4.833652,2.095692,-9.242843,-7.482326],[-0.610094,-8.074126,2.168084,4.772791,-2.751307,-7.722366,0.419170,8.300666,3.454375,-3.359835,8.106346,-7.951064,1.752975,0.112603,-7.241477],[1.414442,5.003062,7.429580,-2.662128,-1.476340,0.536638,9.231974,-0.469143,-8.612513,1.468131,1.746827,-9.320790,2.705829,-1.779248,6.630423],[-0.759163,9.685342,-7.734636,-2.308906,-1.042280,-1.426694,-0.890103,-2.035128,-3.516206,-6.463359,5.509642,-7.593242,8.333069,-1.544928,9.160236]],[[-9.369251,-3.142282,9.129533,-2.531869,-8.428028,-2.039741,8.674962,-7.263939,7.024123,-5.114259,-2.724668,7.889734,0.209662,-8.143433,-6.355154],[2.922028,9.860703,1.096219,8.183112,8.326190,-5.698902,-8.596245,-4.126142,6.067400,6.070010,7.171920,-9.214045,7.357715,1.418620,9.167405],[2.788253,-9.786003,-5.887994,0.689649,-1.107197,1.928464,-6.042024,-5.064784,-7.660219,-2.508866,0.948933,-8.127074,-8.399733,-9.724522,6.860476],[-3.997024,-8.468140,-2.744385,-5.818627,-3.256949,-0.463538,0.265928,2.965166,0.520169,3.436429,-8.305512,1.263563,-5.304715,-8.154865,9.349925],[-2.341586,-0.660121,-7.250887,-3.039863,-8.414297,6.780589,-4.372895,6.087630,-8.071801,-6.459392,-4.409543,7.319071,6.974352,7.221017,-6.182476],[0.192851,-1.249859,0.011813,-4.572053,1.793216,8.624333,2.749848,4.682090,0.619045,5.194431,-9.786138,-2.075868,8.804250,3.906699,4.132515],[1.546910,3.954666,-5.774635,8.440968,-2.485268,0.183959,1.805398,9.771888,3.205800,6.682946,-0.375109,-5.027270,6.729704,-0.006488,3.741064],[-1.294142,4.411285,-6.709139,-0.787659,-5.963330,1.935396,-7.596422,3.598078,7.412486,4.460977,3.848898,-6.027487,-8.099861,-0.537879,4.601419],[1.947354,-8.426901,0.696991,-0.706747,-8.619104,-0.397238,2.475526,2.286234,-3.954600,8.730621,6.439802,-1.975369,0.897327,9.335009,3.052057],[3.370559,-7.680276,0.279022,-7.534189,4.874296,9.166267,-5.665790,5.154255,3.591906,4.373356,3.211320,3.468196,-4.468630,-6.572861,-6.981338],[-0.064841,-5.122542,-4.705789,-1.908139,-0.900111,2.593312,9.523638,-2.224323,3.225862,5.301246,-0.316266,3.036332,-4.717657,-1.337656,6.269353],[-7.412898,-7.501487,-2.394164,6.848612,-1.842255,1.135749,1.798766,8.055251,5.216431,0.984911,6.008133,1.399562,1.282043,0.052229,-2.249919],[0.099252,-5.234765,-5.191787,-2.013908,-2.002957,2.873778,-6.710424,-6.111032,-0.772277,8.636388,-1.451992,4.932363,2.887306,8.992185,8.719767],[-5.524652,7.622029,-7.751908,8.817826,0.319140,3.583158,5.080454,6.752115,-5.161061,7.616159,5.466377,-2.145333,0.853835,8.612759,-8.147919],[0.158199,6.654938,-5.137851,-1.713329,-8.734716,8.293377,-8.449327,-3.406332,-4.495412,0.806042,-6.056101,-5.604559,2.016243,-7.702819,-1.371906],[4.660844,5.752821,-5.895770,3.419023,-9.345136,-4.000672,2.533913,-3.264575,-9.161311,-1.047565,1.219186,-0.565850,-7.098429,5.031786,7.802218]],[[3.964032,8.415189,7.450135,-4.370913,-6.573223,5.079207,-9.308744,9.184554,-1.531023,-0.082728,7.518872,5.634087,5.983186,-8.275950,-4.676253],[-0.868060,-5.510122,0.502324,-2.970628,-7.144299,-6.561627,1.773089,7.798537,7.177754,8.709920,-2.779291,2.363216,-1.056404,6.717809,-4.869821],[-9.388964,-5.046505,-8.686081,5.035545,7.318403,-6.156726,5.228340,9.153099,-6.861133,-5.891118,-4.069619,9.400144,-2.747901,-2.827193,-8.282328],[6.939958,5.931929,8.816367,4.135241,-6.615888,4.382469,-5.689381,6.473793,2.009068,8.797630,1.291226,-8.967851,6.067341,-0.921773,1.560661],[-6.610468,-0.924076,-9.625256,-5.169808,-0.318289,-9.204685,9.509879,-0.784623,-8.167873,-5.323669,4.984689,4.450513,-8.397338,-5.458224,-5.728390],[5.826436,-0.808980,0.416035,-5.406032,5.423428,-6.244462,-7.805094,-4.121747,-7.049729,-0.583112,-4.370095,-7.101467,9.178325,0.336731,-2.264655],[5.790210,-9.752539,7.030052,-0.543710,0.728623,-8.795405,-5.371719,1.401920,8.083796,4.340591,1.167529,9.115190,-9.880749,-6.415697,-1.118451],[3.408000,0.929906,4.780696,6.241675,-4.877888,2.891747,3.720156,8.503958,8.412748,-4.392009,-2.490572,-7.216176,-6.555981,-0.105688,-8.866414],[6.336338,0.970575,-6.307263,7.836768,-8.587371,-4.841600,-9.357153,8.264582,9.154880,-8.210778,-5.809489,1.228039,-1.819918,6.435642,-7.077634],[6.548455,2.735197,-8.546757,5.922867,-0.094772,1.709287,-1.371656,-5.953435,9.735075,-0.506164,7.951888,-4.975031,5.149642,-3.151047,-3.055294],[6.241607,-8.798441,-2.262362,-7.571796,-6.311514,8.074354,1.813205,2.522525,-3.371587,6.089819,-4.375864,4.559857,6.495977,4.930340,0.318660],[5.239213,8.552038,4.215666,-3.710136,-5.211127,-4.215845,5.190990,8.226679,5.905712,2.825145,-5.242300,-4.839488,6.387176,-2.485814,6.327913],[-3.550683,-1.366976,5.998917,8.597498,5.205759,-3.171798,4.802285,-5.340393,3.945380,-1.347091,-9.753024,-9.338752,-9.696073,6.760261,3.885959],[-4.880837,5.415153,5.290405,4.666971,-1.774896,-4.602427,-9.353891,-7.048502,-1.085497,5.652310,7.698359,5.792404,-2.799625,5.584240,2.417376],[-2.912572,-8.356725,-3.934985,-5.539724,-3.431145,6.296766,-4.458943,-5.607887,-3.312928,-5.852273,-5.964577,3.485432,5.409438,7.669969,2.650745],[6.382021,0.309642,6.076439,-2.724263,8.114205,6.333667,5.296137,-0.782437,-0.542395,5.212262,-3.664458,-4.912445,4.718035,9.399583,-5.306534]],[[1.185600,6.987561,1.271800,4.616049,-5.281141,-9.083204,2.980277,8.139009,-3.732838,-8.680392,-3.871528,0.087708,-4.196897,9.567533,4.457264],[3.324880,2.498350,4.121354,9.925042,-6.842789,1.314207,3.852857,2.204836,9.493383,6.756216,0.057060,-2.116956,-1.012808,7.448318,1.783399],[-9.810802,-4.279635,3.399452,-8.285566,-8.743471,-9.500641,-8.435354,-5.700951,6.383075,5.902438,9.113309,-3.684860,3.864472,-8.729573,-7.419499],[2.136866,-2.469321,7.159852,-2.616320,4.866989,-8.607374,-9.656328,0.200966,-4.471395,-8.586154,3.145881,-2.136670,-1.155547,1.030716,0.218369],[-1.578487,-0.131640,-0.967222,-3.569878,2.080707,2.145470,8.072334,-6.728640,-6.818828,1.038931,-1.861478,-2.949199,8.839318,-8.739010,7.392928],[-8.594393,8.442371,3.548327,-3.766035,-1.258568,3.395045,-8.122878,4.926938,7.158970,7.212958,7.690720,-8.202712,8.394203,-4.237007,-3.847894],[5.467174,8.469843,3.756585,-5.674252,-7.250810,2.646099,-4.101874,-5.419313,7.136628,4.738995,3.995976,-0.579668,-2.014455,6.076824,-1.041956],[-7.812019,-4.026821,-9.537493,-0.649285,-0.933112,8.028601,-4.217446,0.588964,7.700922,8.380356,3.927648,1.823649,-8.931910,3.971092,-5.398059],[9.622831,6.546522,-5.182761,1.736528,-3.329651,3.426015,8.807525,7.916899,3.212126,4.730818,0.356491,3.313507,3.713807,-2.946556,4.334307],[-9.460693,-1.846137,-5.274499,0.681944,6.942496,6.385876,4.637265,7.585940,1.367272,0.078895,1.813797,-8.941253,-0.273810,-2.448740,-0.362624],[7.788172,-0.350217,2.355631,4.988471,-5.367632,-1.346597,4.117101,-1.805032,5.555110,2.715025,0.219759,8.039930,0.343598,3.301314,2.354449],[0.930606,-3.894580,-1.984010,7.219819,-7.848748,-4.393378,8.986278,-2.061622,-7.539668,-5.000455,-6.120611,-6.178169,0.455615,0.355896,8.114976],[-1.969824,-7.891689,-4.567442,-8.343508,-7.530258,7.602613,-0.670350,-7.394085,2.061016,-5.594367,5.160581,5.243878,-7.189513,6.973028,3.243139],[-7.787535,-1.645310,-8.606097,5.502528,-1.171542,4.762188,8.422109,-2.225813,-6.360496,-7.945034,6.157771,5.427364,-8.695466,6.287806,-0.683307],[-1.327910,0.871027,9.927843,-1.749905,-1.484005,-4.932781,-7.476323,3.934011,4.013456,-6.344806,-5.700198,7.476730,-3.848524,-4.891528,-7.178662],[-3.123356,0.061790,2.647079,5.659657,-8.168940,-5.229606,4.813618,-6.934293,1.264231,-9.466269,8.360930,-7.175579,0.666245,-9.398163,-5.028527]],[[-4.485031,-8.104677,-0.542385,-8.480441,2.635787,-3.100111,9.496081,-6.165522,-4.021748,2.317539,-0.338517,-5.523598,-4.990395,9.645663,8.282580],[8.211462,8.734740,7.569528,7.746045,4.614460,-0.448792,-9.394494,-9.115296,8.162455,-0.772846,3.095948,-8.147482,2.608814,0.696899,4.090984],[4.411438,-9.210002,-8.277602,-1.863582,0.481987,-0.342588,5.415734,6.569232,-8.147299,5.927937,-9.429145,5.368101,-4.906825,0.469625,3.773636],[-7.054174,3.798759,0.756937,-1.109840,1.440099,-7.234203,-3.995596,-8.172101,1.762159,-5.863069,0.146157,3.203980,2.547341,-3.821977,-6.551611],[-1.510734,-9.044683,9.364946,9.919404,3.108975,-2.629617,8.975945,-4.903513,-5.149001,-6.902158,-0.736448,8.050841,-3.140939,6.201981,0.861392],[-2.766673,-6.871081,6.479457,7.464887,8.531779,0.241323,-4.744670,-5.713869,-1.719044,-4.614156,-9.488445,2.911995,-5.054187,-8.360641,-6.867331],[3.622862,2.511292,7.270961,-7.101360,-2.433151,0.060752,2.283195,-4.501065,-6.401381,-5.569945,9.131794,0.395939,8.510973,-2.949271,5.146888],[2.002974,4.928691,-4.084581,-9.013449,5.209714,4.685107,-4.721430,-0.975683,-5.607728,-0.090436,9.367762,0.455758,-2.502890,5.216052,3.550960],[4.898260,0.554151,7.832666,3.498112,-8.651428,-4.935689,5.352637,-5.203070,9.163593,4.165832,-6.992141,0.342482,7.812814,-9.002679,-2.114416],[-0.186726,-9.807923,4.367873,1.947647,2.563505,1.447344,5.763336,2.350532,3.955400,2.680002,-2.508518,2.397562,1.108386,8.782205,1.309459],[4.574960,4.204846,-3.819303,-2.284959,2.836114,7.122244,5.402005,0.013098,3.248716,-5.662332,7.904323,-0.460494,-1.246541,-7.854204,7.469434],[-9.327345,2.009590,-5.631486,-1.637117,2.014912,8.761478,-2.736048,-9.826433,4.752123,-6.294934,-5.001285,-0.205272,0.986923,-5.244719,-1.918410],[3.725037,5.383324,-2.406270,-8.854217,-2.998715,-0.410751,8.714338,-9.414035,-9.521398,9.105411,3.637203,4.426158,-4.601402,9.474093,-9.756617],[-9.386974,-7.427579,-2.395087,5.933625,4.444509,-7.059962,1.796632,-5.157341,6.054825,1.085828,-8.071853,-6.324499,-6.106310,-5.911359,-1.258869],[0.604951,-7.669644,-7.924988,-0.325607,-7.670259,9.822511,7.650094,-8.303492,-0.764661,4.438768,-7.651180,4.586106,5.735794,2.667966,8.482260],[-8.028990,-0.734982,-1.157414,3.013156,-7.735818,-8.087590,-0.234310,0.736166,9.138456,3.347518,4.041933,-8.573321,-9.655754,7.093636,3.628846]],[[6.733693,6.132692,9.685642,-2.135704,8.244339,-1.730278,-2.895661,3.109272,1.241892,-8.028896,6.880999,-1.402679,-9.462015,0.107285,-2.071657],[-8.029047,-8.535032,8.961605,9.660918,-8.712074,-6.789533,-4.125647,-4.796989,-5.845671,-4.691406,-2.298015,4.655617,-1.456372,3.826608,1.981135],[-3.903476,-2.672053,2.540880,-6.238059,5.040916,3.982079,4.967588,2.033077,-2.387534,5.411433,-3.800700,-1.140047,-3.312960,5.344130,4.403885],[2.477888,-8.271085,-6.146101,3.538400,-2.229991,-7.048456,1.301553,2.350603,9.837459,-0.789511,-0.549992,-5.201100,-2.200031,9.500197,-7.827970],[-9.051036,0.170377,0.465109,3.319193,-8.713611,-8.021306,8.608194,7.589759,-5.920152,-4.381775,1.026658,3.647821,-6.368022,3.446280,9.831454],[-3.065261,6.351839,-4.707155,8.272890,-5.343677,2.650082,-3.417757,-8.561273,7.685487,-1.193091,4.074038,-4.045694,2.294112,7.889481,2.221538],[0.038672,-7.251035,0.031923,9.876676,-1.504871,-2.164150,-4.347525,4.211146,-3.293702,9.179648,-2.771274,5.124411,5.842123,8.589434,6.481180],[2.699794,-9.879183,5.286984,-0.410383,7.770805,-8.969083,-1.223132,-9.847287,2.636635,-0.205964,-3.648142,-9.245826,-3.433065,-2.297795,-8.677674],[-1.278129,-5.936075,6.817253,-9.280015,7.562892,7.530087,4.389338,-0.693835,5.287012,6.100624,5.121489,-7.941145,5.804944,3.324423,1.445256],[4.413119,-7.050882,-2.692402,1.114123,9.912905,-3.778957,5.820573,0.045385,-5.327082,3.086282,-8.030561,7.638362,-0.471446,0.174366,-5.481853],[3.573955,-4.148478,-7.375428,-3.992242,0.565938,-2.256883,-3.927410,-3.936880,1.968182,-7.559404,-3.565245,8.588290,1.678188,-9.680790,-3.011258],[7.462929,-2.640795,5.549662,4.599895,-1.159963,7.232819,-6.652918,-4.059316,0.347739,6.247620,3.113156,0.997309,9.347531,-6.777400,9.739668],[0.772717,9.840687,2.813992,-8.966440,-0.558814,8.677276,7.458202,2.172564,-0.123641,4.883766,-7.606278,9.599223,-8.076331,-0.329922,-6.780449],[8.737719,6.626935,4.981747,9.170123,6.253152,2.357250,6.268259,-9.151205,-1.761120,-8.562897,3.744867,-7.021556,-7.104056,7.327217,-7.436407],[-1.032140,4.368737,-8.263893,-6.420270,-1.557337,4.881545,4.653119,-2.227616,9.649997,-4.838205,5.364780,-4.533175,1.751659,-6.046886,6.148846],[-9.221572,-0.214471,5.421801,0.147703,-5.380843,5.841656,4.960764,-2.389849,2.118583,-1.614840,9.031403,7.013775,-8.880108,-0.679234,1.153030]],[[8.168628,-1.422852,-0.360103,-4.114891,8.465481,8.974562,-3.039273,3.612741,1.249861,-0.395570,2.137992,8.995262,8.997697,1.843340,-6.501823],[1.607487,-5.217600,5.508399,-6.583352,-5.638879,-6.555744,-8.791484,-0.155105,2.849844,-4.586288,-2.868816,-2.956496,-8.229546,3.644593,0.791005],[2.280889,3.232270,-1.730964,-8.194976,-3.365339,4.119409,-3.413822,0.795531,8.244629,-7.897703,-8.073360,4.650019,-6.207106,-9.485612,8.249596],[8.113251,-5.016323,9.089728,4.649324,3.969610,-9.936294,-4.736081,9.695185,-3.051927,4.218177,-4.565007,2.149022,-7.848761,-3.847189,7.596353],[-6.100081,-8.382852,9.216413,-9.240212,4.618209,-7.487363,-2.723212,-1.508772,-7.630276,-3.632687,-6.280093,0.328450,3.849259,2.609415,-4.012093],[7.721746,-2.845035,0.118948,8.020423,-3.343394,-2.243523,1.382163,-0.612478,-8.564652,-6.183324,-9.791381,4.808897,-5.321932,3.880935,-2.552503],[-5.553962,-9.852483,4.262293,-2.491297,1.893178,7.309581,3.092975,-6.869362,5.220415,-2.980122,-2.690935,-7.358314,-9.520454,-3.493636,-0.373369],[2.860988,-5.646089,3.789472,7.298683,4.727453,8.520641,-5.797513,7.630335,-3.520489,3.714489,-8.846386,9.421222,-5.950072,6.616177,6.828070],[0.416042,-0.811507,-6.762748,-7.056091,7.551934,2.726154,-8.920785,1.183357,-2.738532,-8.742431,-8.723417,7.800098,4.611228,9.916568,-9.956946],[3.066365,5.220583,-5.510441,2.692497,8.302817,-0.209770,1.809050,8.986912,-2.846293,-6.067644,9.812431,9.633900,-5.661108,-1.567667,0.729638],[-3.139672,0.107460,-6.172110,-4.358135,-5.984789,-8.433418,-1.418251,6.114387,-1.894569,3.815077,1.842942,5.826432,-0.305394,7.478923,0.027532],[2.327001,9.517556,1.999664,-9.632221,-3.482224,1.013226,7.155114,-8.827856,2.918665,-4.762278,-5.018058,-5.809968,-2.617358,3.438956,0.870856],[-7.048259,7.235643,4.631917,9.033889,-4.915532,-5.276001,-8.124116,6.469203,4.942738,3.645942,9.004637,0.279421,7.121671,-9.011058,7.201048],[4.971123,4.363985,-8.162042,6.833608,-3.474119,6.812191,-6.481884,2.013096,-3.553028,-9.668692,-0.059977,5.691123,0.676689,-7.825392,-9.001711],[-2.985948,6.893860,-2.147071,-0.787317,-9.925663,2.439051,-1.634831,5.635603,7.000618,-8.606848,-2.145767,7.658683,-9.123888,-6.570226,0.836347],[-4.477605,8.279917,7.089982,9.792427,7.352995,-2.429790,0.083838,-1.140238,-4.809504,4.358085,-2.555112,-4.422467,9.147708,-6.895696,1.707768]],[[-4.635657,6.945405,5.719095,8.371414,3.731342,-0.993025,1.158102,-5.461807,0.868484,2.303050,1.765862,-8.860503,-9.070385,-0.317352,7.599690],[-7.320578,3.122894,8.377646,-5.798109,-5.093610,-5.335671,2.427363,-1.309163,3.758633,5.797292,-5.360895,-0.631941,-1.925667,4.167885,-8.944798],[-0.536659,-1.891847,-5.767254,-6.715648,6.882865,-4.059240,-0.252143,0.361749,7.991433,-4.126438,-0.216863,5.175662,4.990828,6.029792,-0.139415],[4.055172,-5.577705,9.303319,-2.997011,0.419983,-8.390988,8.327810,8.955175,8.113901,0.449240,7.517868,2.863398,4.481457,-5.671658,1.716364],[-5.736098,4.410211,-8.855640,5.654756,0.242799,-9.079292,3.355396,-8.868516,9.346739,2.237435,3.588653,-8.613336,-8.327429,1.034971,-7.851483],[5.514181,1.012338,5.037826,6.091680,-9.199832,9.503268,-9.749984,-3.898967,9.973348,1.237383,0.350470,-8.594180,4.513043,1.522366,8.493760],[3.888068,-4.416520,-0.871912,-6.886376,-6.989629,-9.665885,-9.237298,-4.408824,1.386773,-5.107719,4.073669,0.432735,3.999017,-0.869732,0.877292],[-7.458791,-9.961854,7.292597,-1.695172,5.044648,1.018351,-0.851894,-0.780871,-2.803535,-3.931262,-1.976482,-6.395909,7.166660,-2.492864,-4.387268],[-4.364277,-7.110725,8.330574,3.156200,-2.300944,4.388317,-2.425012,1.190767,-0.330185,-2.901167,-4.379460,-0.783642,-0.559837,-6.815034,0.620660],[-0.612855,9.869465,6.593530,-4.870175,-8.244944,8.279138,-9.057888,7.878698,-8.205542,-3.085134,-2.229701,-5.183668,9.593689,6.697139,2.180645],[9.399201,-5.693170,5.224440,9.557336,-1.941836,-2.262228,1.474339,2.188355,-6.750994,2.623430,-0.102335,8.823119,-9.731611,9.294944,-5.576222],[7.414371,-6.263139,-0.034307,7.643422,3.065329,6.521498,6.711245,2.663019,7.771352,-4.146858,-8.712684,-6.082108,5.348770,-3.442405,-9.218771],[-9.012783,-9.852935,1.438258,-3.918831,5.461175,-2.484466,9.703447,2.132841,-7.038196,-1.308732,6.630202,9.178384,-6.613567,5.789628,4.186384],[9.950958,0.010299,-5.402270,-8.105772,7.209436,4.367957,-6.657666,5.640241,4.034603,-3.558684,-8.506963,-7.296221,6.034760,1.574267,6.709806],[3.462386,-8.093582,9.805554,5.048056,9.202772,1.845409,4.561273,0.312609,6.956337,-8.416131,-6.156958,-3.198788,4.848193,9.443509,-5.033814],[7.586007,9.018898,-8.263944,5.307677,-9.383043,-5.540598,9.362760,7.476239,-7.877870,4.786430,-8.790295,8.971180,-4.598606,-1.471799,8.943934]],[[-3.914238,-1.789694,-9.169113,-0.008964,9.089171,-6.140067,-9.572144,5.512309,-0.210919,3.417857,-7.457847,8.052295,-2.518805,-1.369292,5.800378],[4.158474,9.512893,9.867050,-5.527414,7.796692,-2.670598,6.654870,4.283677,-0.807237,-5.018470,5.072425,5.940708,-5.809943,-5.218288,8.412859],[8.942949,7.745694,-8.453078,-7.761154,7.690565,-3.941432,-9.314352,-5.540748,-6.418826,7.224286,-4.647288,-9.307371,-8.547631,6.040984,5.844253],[-8.025493,5.028268,7.801054,9.507678,-2.275278,5.383556,-6.211615,-5.613570,2.074684,-5.135044,4.066974,8.106132,-5.266180,4.330843,-7.408006],[-2.120682,6.873477,1.345801,-1.222721,-4.086186,7.730846,4.881987,3.482954,-3.918123,8.662784,-2.782372,-7.983273,-4.086537,0.540477,-3.838933],[-2.458685,-1.294580,1.290094,1.196458,-9.741897,-8.186491,3.759826,-5.857599,-5.643124,-7.482117,9.400204,-6.018115,-1.400124,-8.296443,-1.472798],[-7.821823,-4.444086,-5.134546,-6.273024,2.718137,-1.660997,-7.811719,0.552175,-1.624734,9.290730,2.747845,6.616210,-7.786244,-8.132741,1.461772],[-0.659174,-8.277209,1.566876,-5.407014,-1.887370,-6.435602,5.396235,-2.850398,3.246226,-4.759751,7.237320,4.613379,-3.556883,2.207504,5.480709],[6.051513,-9.019782,-0.291609,6.609538,0.280544,-0.843908,-0.617317,-3.869290,-3.924120,0.731543,-5.809879,3.660884,-7.943886,-5.030453,-1.707284],[-2.184459,1.081412,4.230145,-0.085445,-4.511485,-1.510292,-3.999015,-9.161618,-9.714128,-6.041845,-2.032216,-1.286534,2.569375,7.737662,-2.800165],[1.050764,8.795865,3.777589,-2.130393,4.202156,3.951818,9.148754,-2.860940,-7.146289,-0.615759,4.996931,-3.615915,-8.297652,-9.190864,1.197955],[-3.131738,8.102810,6.326530,-5.211962,2.666434,-7.314525,-4.805605,-5.528002,2.119712,4.432542,4.021830,-1.800734,-9.795367,7.014737,-9.859109],[-4.615277,4.157586,9.383351,-3.808720,-3.889733,1.099118,0.335983,-5.725283,3.807474,-9.365344,-1.906301,9.601702,6.072781,6.517899,-2.740494],[6.839846,-5.338671,-0.209246,7.309835,-3.489744,-3.007749,-0.572552,0.844320,7.302689,0.988872,1.014993,-5.743853,-2.270814,-5.339234,-0.771972],[-6.839590,5.822907,8.539932,-9.756782,9.502578,-2.982894,-1.600529,4.750537,-7.033621,-0.137424,-0.440101,2.348724,-6.186235,4.349665,3.018668],[6.291338,1.231082,7.865254,2.874083,-6.420330,-7.627321,-6.348665,6.619292,-3.644186,9.194313,4.974843,-0.595862,-2.589441,6.517618,3.813069]],[[4.908519,-2.757082,-7.579142,2.683125,7.190316,-8.768713,0.234712,-7.583997,-1.789529,-4.582241,-9.251329,1.190055,-3.809474,8.924845,2.536825],[-6.826083,-4.464248,-7.932469,-9.799877,-9.539117,5.845490,2.020861,6.351778,9.656206,-1.007911,9.041913,-0.795277,4.708777,-6.505647,-9.208605],[-7.887258,0.254895,8.850241,2.937580,9.408779,0.614791,-8.319818,0.108051,-4.483611,0.253422,-6.648133,4.379967,5.840052,4.336343,-2.309073],[-2.520315,9.420846,6.675240,3.259701,-9.411410,-3.159410,0.960314,7.779469,-2.160329,1.632720,-6.116834,7.744075,-6.230439,8.341858,-0.566078],[1.695396,-4.739498,-4.050514,3.084376,-6.375129,9.095787,4.141152,0.371211,9.535309,2.374356,0.983635,8.628731,8.994439,8.107030,8.179502],[-7.699610,-4.463785,9.039151,-1.278822,-6.966002,4.661817,5.331288,-5.144603,1.962233,6.679335,3.735655,-8.990705,1.659381,-4.946759,-5.099679],[-0.091346,1.545379,7.334762,-2.736600,1.569137,-5.612281,-6.062532,-2.339862,-2.058919,-7.453848,-5.513307,-8.435686,-8.856883,-3.449384,7.716253],[2.673098,-5.899744,-3.379473,6.746209,9.826052,-6.230258,8.107613,-7.579039,9.630931,8.067483,-7.034496,2.554198,0.955890,-0.552012,5.896869],[-7.039664,9.028498,2.106626,3.947083,-5.364673,8.302351,-6.854197,5.019504,-9.630418,-5.009490,4.783603,5.402719,8.336794,-2.559999,5.167887],[6.194592,-3.105113,-4.425112,9.559067,5.141877,-0.918018,-2.077263,3.310084,1.256542,-1.561341,-1.869066,-2.796846,0.638101,-4.953400,1.099727],[3.188072,8.249937,-0.556973,5.808745,6.373509,3.376094,7.175559,1.999723,-1.762536,2.335928,-7.385469,-7.508543,2.412761,-6.741387,2.241437],[3.043241,2.724589,7.191896,-5.797141,5.447495,3.235493,-6.072119,-9.000628,1.241661,-0.252811,3.897605,-9.808036,-4.032300,3.871355,8.048585],[-0.297547,1.532743,-8.850042,6.856565,7.144397,-2.083652,-7.181750,-4.530460,-2.441576,0.681829,-3.866794,9.437998,-4.443344,-3.871886,4.899090],[-3.949665,3.324258,4.795830,-3.938315,-8.094229,8.565561,-4.877222,3.963145,-2.210240,4.444311,5.646770,-1.563629,-9.188674,-4.046349,7.782148],[3.851856,6.494343,0.591965,-4.190121,-1.171914,-7.448815,0.375485,1.421732,7.202091,2.342994,4.222978,-5.658934,5.206221,-4.631962,1.218488],[2.765749,8.962413,2.173642,0.721661,3.512905,1.539181,8.854518,-8.408483,0.642746,-8.634831,-7.377673,6.795953,-7.865697,-5.455011,-5.859394]],[[-7.156883,-9.208334,5.859223,-2.446834,8.975464,-1.299345,5.367766,8.098684,-0.188521,5.371993,5.706095,-1.517105,-7.479442,-9.795914,6.696831],[8.036031,-7.171886,0.197472,8.531758,6.351579,8.865368,2.430962,6.559539,8.210806,-9.223806,0.184800,-1.508458,-7.692050,-7.617141,2.972521],[-7.543715,7.830840,-8.161902,-3.776429,-1.836245,-4.280631,2.418045,0.345991,2.093149,-2.510706,5.550649,1.479113,5.275590,1.529373,-2.894332],[4.670442,0.930236,-4.343724,3.992831,5.063132,-2.060237,-4.322862,-2.429293,-2.949200,-7.298854,7.096672,-7.433859,4.882189,-1.867740,1.604312],[-4.052747,4.452419,8.229430,8.547279,-9.458996,1.479671,1.337274,-6.282528,8.446238,2.696767,7.824694,1.403882,4.403647,7.222470,3.689754],[2.908658,1.547705,9.900222,-6.240615,-0.827946,-2.571711,3.264391,4.621287,6.982809,-7.700185,-2.875649,6.939642,-7.284453,-8.077578,-7.640658],[-5.943285,9.770147,6.842906,3.850986,-7.048206,-5.170007,8.937557,-4.684511,-5.123285,6.355626,-2.157187,-5.750037,7.304084,-4.203818,3.126803],[-2.391780,-6.503595,5.331823,-3.060311,7.998916,-0.284923,3.659823,9.218367,-3.758626,5.013571,1.093952,2.063272,0.836331,-6.421727,6.536560],[4.646840,0.981930,1.781494,5.628512,6.936783,-2.365193,-0.008999,7.805223,2.047726,5.094438,9.161810,-9.308152,8.107517,-1.998060,-2.083832],[0.901467,6.484772,6.514051,2.949179,-1.043794,-0.905687,4.809005,3.589175,-9.548932,-4.593420,1.663225,-8.787293,0.821676,-9.343199,4.119822],[7.082211,-9.959620,-9.122916,3.212252,-6.348886,-1.259046,7.141008,2.697604,7.574691,4.302987,-9.735060,7.032431,7.285165,-9.765118,-7.331367],[-3.849383,-0.478154,-9.995506,-2.469313,-1.176833,-5.689775,6.023204,-0.577902,-0.095902,4.760361,-2.139340,-7.617944,-8.928056,-3.101436,5.902184],[1.629972,-4.520059,-4.175836,-5.236467,-2.981425,7.658402,6.350487,-3.333732,-6.600362,9.031078,1.013185,1.536350,-3.013882,2.499002,-3.124773],[9.221857,-5.395594,9.872120,0.528223,9.149120,-6.630280,-4.960162,-6.138865,-8.443520,7.293633,-6.691672,3.915879,-4.658464,9.868769,-1.066249],[1.913085,4.801104,0.253057,-9.523334,-8.710440,-4.144916,0.349389,4.869109,-0.094530,-3.559148,5.917810,-4.685036,-7.249447,-7.351392,-2.098438],[4.152491,8.668989,8.609331,8.654871,8.874521,3.282944,-9.907145,-0.857922,-2.784646,9.883461,-6.964031,9.657327,8.520836,4.974349,-5.078042]],[[-9.930872,5.408950,-5.716237,-9.758491,9.591370,-5.269455,-9.776663,1.591440,-7.987416,1.442225,-8.800402,-6.161468,-8.559637,9.144514,-8.724987],[8.762308,9.719449,-0.428189,6.258234,0.062774,-9.689030,1.054492,-1.860263,9.016929,1.159040,8.807819,-7.569185,8.830852,6.600627,-7.303814],[-3.214936,9.184962,0.875166,-3.587023,-8.522422,5.343349,9.198643,8.037363,1.927196,-7.452819,0.894732,-6.435048,7.999404,-3.280586,-2.703125],[-4.165403,-0.412903,-1.837535,0.186296,-4.772607,-5.273707,-4.476530,9.991950,5.328850,-0.394817,6.469417,7.620974,1.394266,8.649773,-1.948292],[4.240161,1.395714,-2.749950,3.266838,-1.493756,4.179778,3.421489,-0.769467,-7.609827,4.535134,2.797284,-1.483212,-8.508920,2.345928,-1.763799],[5.263912,3.348980,9.170586,-5.972841,4.536166,3.235014,4.425015,9.322035,0.251414,8.118515,-9.482613,2.376702,-0.476740,0.148169,6.915202],[3.171938,4.756585,8.007306,-8.182423,7.360813,-6.790004,-9.992704,8.863748,6.877657,1.747211,1.159488,2.771643,7.333253,-8.731764,-8.586420],[-2.105393,-0.711679,-8.395178,-6.269485,7.366686,-8.798341,-4.200790,0.295345,-6.778146,-1.112780,3.179464,-8.872942,-0.447964,-7.100221,-4.281995],[3.772729,-6.373206,-5.980977,5.886246,8.872783,-2.260701,5.867326,4.952594,-8.995669,8.938382,9.635237,-8.894056,-0.886892,9.477107,6.266907],[5.019419,-2.675969,-0.477485,-0.664355,-5.673214,-2.511619,9.682279,2.651358,-6.800610,0.792801,6.884549,-7.360288,-8.916879,-2.087302,-5.377195],[0.181319,-5.802013,8.158773,-6.680654,4.574685,-5.292572,8.697372,5.255994,-1.657650,-0.554948,4.631133,-9.733983,3.180966,-6.271269,9.238164],[2.838880,-4.669396,-9.241953,-6.510071,0.167930,6.663453,5.819525,-5.705081,-2.470482,-8.809342,-5.246311,-5.960775,4.125528,6.437112,2.743640],[-7.785725,9.789263,3.878074,4.487291,-3.181338,8.563873,-6.316374,-2.520026,2.961183,8.090223,9.677721,8.064366,-5.532948,8.062881,1.925082],[-6.261427,7.497590,-1.637434,-4.140459,-6.318344,8.467533,-8.532860,-5.768461,-3.141589,1.458182,8.275395,6.413303,-1.093637,1.711967,7.623943],[7.806382,6.330267,8.864880,8.663917,7.187640,-1.503102,6.270910,-8.648108,7.856942,2.106809,-4.527815,9.623108,8.270331,9.960423,8.369010],[2.200883,9.532804,6.693938,3.024002,-4.307417,-1.260892,6.339382,3.281180,4.004156,-6.711922,-6.679999,1.840523,-3.757659,6.895624,6.839046]]], dtype = "float32")#candidate|3131|(14, 16, 15)|const|float32
uop_3132 = relay.acosh(const_3131.astype('float32')) # shape=(14, 16, 15)
func_2860_call = mod.get_global_var('func_2860')
func_2863_call = mutated_mod.get_global_var('func_2863')
const_3144 = relay.const(-8.577117, dtype = "float64")#candidate|3144|()|const|float64
var_3145 = relay.var("var_3145", dtype = "float64", shape = (264,))#candidate|3145|(264,)|var|float64
call_3143 = func_2860_call(relay.reshape(const_3144.astype('float64'), []), relay.reshape(var_3145.astype('float64'), [11, 6, 4]), )
call_3146 = func_2860_call(relay.reshape(const_3144.astype('float64'), []), relay.reshape(var_3145.astype('float64'), [11, 6, 4]), )
output = relay.Tuple([uop_3132,call_3143,const_3144,var_3145,])
output2 = relay.Tuple([uop_3132,call_3146,const_3144,var_3145,])
func_3156 = relay.Function([var_3145,], output)
mod['func_3156'] = func_3156
mod = relay.transform.InferType()(mod)
mutated_mod['func_3156'] = func_3156
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3157 = relay.var("var_3157", dtype = "float64", shape = (264,))#candidate|3157|(264,)|var|float64
func_3156_call = mutated_mod.get_global_var('func_3156')
call_3158 = func_3156_call(var_3157)
output = call_3158
func_3159 = relay.Function([var_3157], output)
mutated_mod['func_3159'] = func_3159
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3192 = relay.var("var_3192", dtype = "uint16", shape = (8, 14, 13))#candidate|3192|(8, 14, 13)|var|uint16
var_3193 = relay.var("var_3193", dtype = "uint16", shape = (8, 14, 13))#candidate|3193|(8, 14, 13)|var|uint16
bop_3194 = relay.add(var_3192.astype('uint16'), relay.reshape(var_3193.astype('uint16'), relay.shape_of(var_3192))) # shape=(8, 14, 13)
func_777_call = mod.get_global_var('func_777')
func_781_call = mutated_mod.get_global_var('func_781')
var_3198 = relay.var("var_3198", dtype = "float64", shape = (78,))#candidate|3198|(78,)|var|float64
const_3199 = relay.const([9.890576,-1.793484,0.977693,3.790861,6.390702,0.291295,-0.289651,0.556413,-7.499284,-7.199389,4.575123,-6.349910,6.838490,2.892455,-5.108208,0.689986,-7.762441,1.019818,-3.837572,-2.504605,-4.321451,7.089568,-8.611338,-3.129697,5.571490,-2.076747,-9.538426,3.728601,-3.939385,-2.830035,6.947200,-5.153000,5.785398,6.545900,0.909590,3.332690,3.658367,-3.441944,-2.488667,-8.711210,3.671707,-1.934526,1.682373,6.067776,-6.557131,-1.255802,0.841500,5.723283,-6.238176,4.711423,-1.001803,-1.072926,7.282686,2.891954,4.166206,-9.874291,-1.879461,-5.776575,-0.312296,7.158556,4.540658,-7.189797,9.466227,5.079496,-8.261577,1.818044,-5.217140,-4.710301,-0.096961,8.721307,0.808394,-5.703346,-8.099968,5.908373,-5.258329,5.677759,5.423072,6.633387,5.622048,-3.227940,2.973301,-7.904355,4.949084,1.481472,6.684772,-1.057022,-7.527895,-9.155326,9.953252,4.587834,1.060299,-9.987396,-7.957255,1.010872,-2.396666,5.619489,9.833541,5.260986,-1.995965,-4.946253,7.269995,-9.274666,8.182019,-0.101152,0.760286,-2.600985,-6.454957,6.584906,-0.325347,-9.727792,-5.913453,-0.796676,-1.545060,1.495664,9.661663,-1.282831,-7.351028,-7.088035,9.309197,-4.266649,6.312780,6.870072,4.686119,-5.759687,1.775537,4.337287,6.758859,1.767796,9.285185,-0.003897,-0.818449,-6.902934,-9.928417,-6.932981,5.182452], dtype = "float32")#candidate|3199|(135,)|const|float32
call_3197 = relay.TupleGetItem(func_777_call(relay.reshape(var_3198.astype('float64'), [13, 3, 2]), relay.reshape(var_3198.astype('float64'), [13, 3, 2]), relay.reshape(const_3199.astype('float32'), [135,]), ), 0)
call_3200 = relay.TupleGetItem(func_781_call(relay.reshape(var_3198.astype('float64'), [13, 3, 2]), relay.reshape(var_3198.astype('float64'), [13, 3, 2]), relay.reshape(const_3199.astype('float32'), [135,]), ), 0)
func_3044_call = mod.get_global_var('func_3044')
func_3051_call = mutated_mod.get_global_var('func_3051')
var_3216 = relay.var("var_3216", dtype = "float64", shape = (1568,))#candidate|3216|(1568,)|var|float64
const_3217 = relay.const(-5, dtype = "uint8")#candidate|3217|()|const|uint8
var_3218 = relay.var("var_3218", dtype = "uint32", shape = (30,))#candidate|3218|(30,)|var|uint32
call_3215 = relay.TupleGetItem(func_3044_call(relay.reshape(var_3216.astype('float64'), [14, 16, 7]), relay.reshape(const_3217.astype('uint8'), []), relay.reshape(var_3218.astype('uint32'), [30,]), relay.reshape(var_3198.astype('float64'), [78,]), relay.reshape(const_3199.astype('float32'), [135,]), ), 1)
call_3219 = relay.TupleGetItem(func_3051_call(relay.reshape(var_3216.astype('float64'), [14, 16, 7]), relay.reshape(const_3217.astype('uint8'), []), relay.reshape(var_3218.astype('uint32'), [30,]), relay.reshape(var_3198.astype('float64'), [78,]), relay.reshape(const_3199.astype('float32'), [135,]), ), 1)
bop_3222 = relay.logical_or(bop_3194.astype('bool'), relay.reshape(var_3193.astype('bool'), relay.shape_of(bop_3194))) # shape=(8, 14, 13)
func_777_call = mod.get_global_var('func_777')
func_781_call = mutated_mod.get_global_var('func_781')
call_3229 = relay.TupleGetItem(func_777_call(relay.reshape(call_3197.astype('float64'), [13, 3, 2]), relay.reshape(call_3197.astype('float64'), [13, 3, 2]), relay.reshape(const_3199.astype('float32'), [135,]), ), 0)
call_3230 = relay.TupleGetItem(func_781_call(relay.reshape(call_3197.astype('float64'), [13, 3, 2]), relay.reshape(call_3197.astype('float64'), [13, 3, 2]), relay.reshape(const_3199.astype('float32'), [135,]), ), 0)
var_3242 = relay.var("var_3242", dtype = "float64", shape = (1568,))#candidate|3242|(1568,)|var|float64
bop_3243 = relay.logical_xor(var_3216.astype('uint32'), relay.reshape(var_3242.astype('uint32'), relay.shape_of(var_3216))) # shape=(1568,)
uop_3250 = relay.rsqrt(bop_3222.astype('float64')) # shape=(8, 14, 13)
output = relay.Tuple([call_3197,var_3198,const_3199,call_3215,const_3217,var_3218,call_3229,bop_3243,uop_3250,])
output2 = relay.Tuple([call_3200,var_3198,const_3199,call_3219,const_3217,var_3218,call_3230,bop_3243,uop_3250,])
func_3253 = relay.Function([var_3192,var_3193,var_3198,var_3216,var_3218,var_3242,], output)
mod['func_3253'] = func_3253
mod = relay.transform.InferType()(mod)
mutated_mod['func_3253'] = func_3253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3253_call = mutated_mod.get_global_var('func_3253')
var_3255 = relay.var("var_3255", dtype = "uint16", shape = (8, 14, 13))#candidate|3255|(8, 14, 13)|var|uint16
var_3256 = relay.var("var_3256", dtype = "uint16", shape = (8, 14, 13))#candidate|3256|(8, 14, 13)|var|uint16
var_3257 = relay.var("var_3257", dtype = "float64", shape = (78,))#candidate|3257|(78,)|var|float64
var_3258 = relay.var("var_3258", dtype = "float64", shape = (1568,))#candidate|3258|(1568,)|var|float64
var_3259 = relay.var("var_3259", dtype = "uint32", shape = (30,))#candidate|3259|(30,)|var|uint32
var_3260 = relay.var("var_3260", dtype = "float64", shape = (1568,))#candidate|3260|(1568,)|var|float64
call_3254 = func_3253_call(var_3255,var_3256,var_3257,var_3258,var_3259,var_3260,)
output = call_3254
func_3261 = relay.Function([var_3255,var_3256,var_3257,var_3258,var_3259,var_3260,], output)
mutated_mod['func_3261'] = func_3261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3767 = relay.var("var_3767", dtype = "float32", shape = (16, 15, 2))#candidate|3767|(16, 15, 2)|var|float32
const_3768 = relay.const([[[1.185418,0.175893],[-9.285162,-2.855618],[-5.229981,1.624236],[-7.256413,-0.741298],[3.566987,-7.578491],[-3.168987,-4.893352],[-0.873942,8.549747],[8.113532,-4.433796],[-5.315656,-5.747098],[-9.864065,7.992805],[5.129973,-1.477572],[-0.614834,-3.290336],[1.032907,7.544669],[1.288125,0.641974],[3.718596,9.456611]],[[-0.543036,5.791671],[-8.587230,4.487703],[-6.710312,7.419305],[0.178870,8.309303],[-2.923251,-0.126741],[7.171483,2.243622],[8.072643,-3.681391],[1.741662,5.062181],[2.603913,0.029901],[-6.956049,-6.745847],[8.769349,1.748833],[2.934578,9.902913],[-0.224708,1.698085],[4.127384,8.053747],[-5.682456,5.909825]],[[2.902304,4.723493],[-8.817634,-8.990123],[8.949598,5.764887],[-3.019399,0.754366],[-3.959120,-0.879383],[-8.460070,-9.112218],[-8.193636,-0.926281],[3.753912,6.456950],[1.832042,-7.586469],[3.858200,-7.848675],[2.504271,2.111102],[-7.811650,-8.834004],[0.297631,-6.701753],[-7.351112,-0.923506],[-8.600648,2.309814]],[[-7.637657,-0.960920],[7.750619,2.675367],[-9.675550,4.142475],[-2.602120,6.533008],[-2.278067,2.938922],[-5.883887,2.070932],[-8.364459,-5.241473],[0.579742,-2.360918],[-0.922446,4.876001],[1.235351,-6.877939],[-5.835192,-6.594521],[-9.689064,-8.210340],[1.909957,6.241424],[7.325209,-2.669752],[-3.746129,-7.688684]],[[3.897577,1.477583],[0.295189,4.391458],[-7.815102,-6.330969],[-1.638101,4.385067],[8.493381,2.828399],[6.285972,-5.752407],[9.154909,-5.975091],[0.235499,0.502161],[0.785055,-8.293828],[8.671100,-1.834145],[3.721686,0.627138],[4.052391,4.291166],[-3.419891,0.263097],[1.028837,-4.330544],[-7.064885,-9.363026]],[[9.685748,-4.319693],[-1.628953,1.581283],[1.626426,6.290094],[7.452234,-2.955105],[5.567508,8.622537],[-6.642067,7.330942],[-9.396225,-3.378431],[-8.718988,7.550839],[6.793830,3.391826],[-2.091393,8.956529],[-8.128744,8.829443],[9.337753,-7.047436],[7.675570,-1.247025],[-1.232618,0.441603],[3.127712,8.109373]],[[-2.398846,6.839118],[3.919878,2.888111],[-6.250035,3.697928],[-7.171249,-8.661030],[-7.161467,-5.348214],[-8.844144,1.007674],[5.868086,3.313326],[-5.608913,-1.195150],[1.456193,-1.974466],[-1.431956,8.671556],[4.318043,2.470205],[7.192666,9.853689],[-9.942193,6.845066],[4.024519,4.660757],[4.087001,7.622652]],[[-3.438178,-9.587956],[-0.108837,-4.466453],[-6.579016,3.916139],[-5.840253,9.298582],[-8.190210,8.489478],[8.394706,4.552738],[9.510406,6.076972],[0.718581,-0.920534],[-8.801457,-5.203947],[-2.607498,-7.529716],[-0.372244,-1.155283],[-4.900189,-0.929996],[-2.201818,-5.860954],[-7.247731,-9.526038],[-3.083435,-0.818562]],[[8.624562,0.847222],[4.450658,-9.341246],[-4.198126,-5.321033],[-5.911493,2.567161],[5.516767,7.758581],[1.049947,4.240970],[2.557797,8.782619],[8.469124,2.950537],[3.965666,-1.369960],[-7.306660,-0.857403],[4.466766,9.944693],[7.434710,6.922173],[-2.250435,-1.019258],[-1.398874,6.510532],[-8.846260,9.188812]],[[-9.275106,-1.643123],[-1.995708,-0.840964],[0.189540,3.880147],[-4.158350,-1.764340],[-5.660722,-9.419782],[-4.673561,-9.329707],[-0.822145,-3.208170],[8.166490,-4.573094],[-6.337728,9.898219],[7.539114,-5.689021],[-7.539661,-3.364631],[-3.941707,-1.920462],[-7.322968,-4.481016],[5.321815,2.408860],[-1.476806,-0.029884]],[[5.239758,-8.414900],[6.626115,-5.515323],[4.172046,0.821323],[6.639477,-5.931849],[-4.400213,-2.928936],[4.638378,9.984207],[2.539985,-4.578028],[-0.925537,7.351748],[5.578681,-0.103891],[2.249429,-3.345589],[3.255947,-5.287405],[4.250045,-8.140363],[9.347080,-8.951652],[7.185406,-1.748380],[-5.521708,4.260583]],[[7.228761,-4.285470],[-5.889848,-0.596091],[-3.887196,-4.873702],[-5.505903,-2.048430],[-1.933048,-4.953753],[1.545982,-5.824881],[-4.376254,9.352453],[-9.170748,-0.578846],[-8.268492,-6.603689],[9.037873,-2.324772],[8.684769,0.871130],[-7.288051,8.863002],[-8.444383,-0.369591],[-1.829563,7.162290],[8.180533,0.958765]],[[2.905146,-3.463382],[1.999106,-4.882682],[0.409178,-8.762922],[1.221980,-2.816472],[5.075894,-6.493392],[2.582393,2.325956],[-8.130125,0.352545],[5.199169,8.786711],[-6.993149,-0.818809],[-6.973661,-7.097150],[-8.156946,5.623769],[-1.546973,7.921373],[2.077146,2.317416],[-6.770220,9.793508],[7.848326,5.068260]],[[5.102288,4.104085],[-2.126205,7.284950],[-0.299012,-6.508681],[-4.822207,4.485474],[5.697386,-2.454912],[-0.707293,-6.172315],[-3.998207,1.619632],[-1.928377,5.319972],[3.487963,3.259154],[-0.856233,2.752710],[-6.506733,1.317294],[0.328697,5.386551],[7.231173,5.832588],[6.297523,8.844439],[5.582910,-3.048697]],[[3.159391,-0.778310],[-7.710902,-2.062532],[-7.965077,-8.335228],[3.459104,-4.614775],[-5.710840,4.303964],[1.887858,2.374174],[-9.786229,4.296144],[-4.704658,1.627522],[3.295009,-6.141994],[2.500745,-8.804659],[-4.493425,-0.691065],[3.448484,-7.167009],[-7.076869,7.200673],[0.971676,5.909762],[1.841412,4.919266]],[[-7.683011,4.664679],[-5.245696,2.951569],[-3.384479,-5.578742],[-2.481925,-3.970573],[9.956854,3.774481],[1.543482,0.482578],[-4.310196,-5.096606],[7.790951,5.694361],[2.408333,8.426223],[-5.904291,9.936421],[4.808944,-9.578567],[9.133276,8.638816],[8.426276,-3.924327],[4.531471,3.306820],[-3.445301,-9.223101]]], dtype = "float32")#candidate|3768|(16, 15, 2)|const|float32
bop_3769 = relay.floor_divide(var_3767.astype('float32'), relay.reshape(const_3768.astype('float32'), relay.shape_of(var_3767))) # shape=(16, 15, 2)
func_2447_call = mod.get_global_var('func_2447')
func_2450_call = mutated_mod.get_global_var('func_2450')
const_3780 = relay.const(-2, dtype = "uint8")#candidate|3780|()|const|uint8
const_3781 = relay.const([5,7,5,-3,9,7,-8,-4,-8,-5,2,6,6,-2,-9,2,2,-5,1,10,-1,-8,8,3,-6,-8,-8,-8,2,-5,-10,6,-4,9,-10,7,-3,-10,7,-6,-2,3,9,-6,-3,4,6,5,3,-7,-2,2,-9,8,-6,9,9,7,5,-8,4,2,-2,-2,-1,-5,5,-10,-10,10,-1,1], dtype = "uint8")#candidate|3781|(72,)|const|uint8
call_3779 = relay.TupleGetItem(func_2447_call(relay.reshape(const_3780.astype('uint8'), []), relay.reshape(const_3781.astype('uint8'), [12, 1, 6]), ), 0)
call_3782 = relay.TupleGetItem(func_2450_call(relay.reshape(const_3780.astype('uint8'), []), relay.reshape(const_3781.astype('uint8'), [12, 1, 6]), ), 0)
output = relay.Tuple([bop_3769,call_3779,const_3780,const_3781,])
output2 = relay.Tuple([bop_3769,call_3782,const_3780,const_3781,])
func_3788 = relay.Function([var_3767,], output)
mod['func_3788'] = func_3788
mod = relay.transform.InferType()(mod)
mutated_mod['func_3788'] = func_3788
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3789 = relay.var("var_3789", dtype = "float32", shape = (16, 15, 2))#candidate|3789|(16, 15, 2)|var|float32
func_3788_call = mutated_mod.get_global_var('func_3788')
call_3790 = func_3788_call(var_3789)
output = call_3790
func_3791 = relay.Function([var_3789], output)
mutated_mod['func_3791'] = func_3791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3818 = relay.var("var_3818", dtype = "float64", shape = (1, 9, 1))#candidate|3818|(1, 9, 1)|var|float64
uop_3819 = relay.rsqrt(var_3818.astype('float64')) # shape=(1, 9, 1)
const_3821 = relay.const([[[1.212195,1.940163,-3.901367,-6.834348,-3.219297],[6.709443,-1.787615,1.907646,-4.169083,-2.335201],[6.343177,-6.603373,-2.814340,-7.110505,8.854499],[9.479865,-1.987599,-8.845533,-6.414986,-3.887620],[-0.335683,8.251429,3.281919,-7.308907,2.595996],[-5.458367,5.411683,8.406062,5.357346,-8.581630],[4.001126,-8.390207,-7.603564,9.383496,0.782041],[5.000367,2.732888,-4.789862,-7.174772,8.305689],[-3.479917,-3.536150,-4.067437,1.718126,9.839874]],[[-4.043954,-5.143830,-2.753723,7.819160,5.350022],[-5.446449,-0.004855,0.167615,-0.868759,9.522905],[6.770833,-2.557225,-5.083437,-9.616135,-0.269830],[9.891473,-3.569167,1.255381,-3.355885,-2.372292],[-8.638213,0.340152,9.612909,2.213986,-0.345491],[8.864928,-3.655569,3.753432,-2.269644,7.949000],[5.502483,-6.192720,-8.537405,-1.184599,-5.753715],[-4.838031,2.417435,-6.451998,-8.144414,7.257787],[-6.133786,0.305572,-7.528769,4.015503,-7.440878]]], dtype = "float64")#candidate|3821|(2, 9, 5)|const|float64
bop_3822 = relay.logical_xor(uop_3819.astype('uint32'), const_3821.astype('uint32')) # shape=(2, 9, 5)
output = bop_3822
output2 = bop_3822
func_3855 = relay.Function([var_3818,], output)
mod['func_3855'] = func_3855
mod = relay.transform.InferType()(mod)
var_3856 = relay.var("var_3856", dtype = "float64", shape = (1, 9, 1))#candidate|3856|(1, 9, 1)|var|float64
output = func_3855(var_3856)
func_3857 = relay.Function([var_3856], output)
mutated_mod['func_3857'] = func_3857
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3913 = relay.var("var_3913", dtype = "float32", shape = (3, 10))#candidate|3913|(3, 10)|var|float32
uop_3914 = relay.sigmoid(var_3913.astype('float32')) # shape=(3, 10)
output = relay.Tuple([uop_3914,])
output2 = relay.Tuple([uop_3914,])
func_3925 = relay.Function([var_3913,], output)
mod['func_3925'] = func_3925
mod = relay.transform.InferType()(mod)
mutated_mod['func_3925'] = func_3925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3926 = relay.var("var_3926", dtype = "float32", shape = (3, 10))#candidate|3926|(3, 10)|var|float32
func_3925_call = mutated_mod.get_global_var('func_3925')
call_3927 = func_3925_call(var_3926)
output = call_3927
func_3928 = relay.Function([var_3926], output)
mutated_mod['func_3928'] = func_3928
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4125 = relay.var("var_4125", dtype = "float32", shape = (10, 1, 2))#candidate|4125|(10, 1, 2)|var|float32
uop_4126 = relay.cos(var_4125.astype('float32')) # shape=(10, 1, 2)
uop_4130 = relay.asinh(uop_4126.astype('float64')) # shape=(10, 1, 2)
bop_4138 = relay.subtract(uop_4126.astype('int8'), relay.reshape(var_4125.astype('int8'), relay.shape_of(uop_4126))) # shape=(10, 1, 2)
func_3080_call = mod.get_global_var('func_3080')
func_3083_call = mutated_mod.get_global_var('func_3083')
const_4148 = relay.const([9.675019,-5.014536,-2.960082,-9.874221,7.060109,8.358649,-4.771604,-0.185632,-3.342703,0.653963,3.769810,-3.006741,9.504262,-0.760279,7.541059,-6.175809,-2.727994,6.980915,-5.438195,-4.561674,6.184879,-5.871153,7.660526,-7.607894,-1.883970,7.964477,-7.886681,-7.476795,-0.789941,-9.834872,-2.235365,-6.520839,4.011443,6.506348,4.447185,-1.785072,6.070137,-4.696061,1.201851,-6.875959,7.125589,-7.215750,-2.564767,3.871867,0.724923,-6.329598,2.311437,-6.064698,-5.097653,-0.905362,-6.564050,3.514063,0.538636,-6.867519,-4.779215,-8.245676,-3.804933,-3.347076,3.762165,8.956779,4.378055,-2.752910,4.048667,-9.171387,5.229753,0.501651,1.133640,8.370545,1.822015,7.346009,4.427981,0.848611,-8.350214,-6.682157,8.264015,2.213045,0.770345,4.573169,-7.062070,-0.522714,-9.785531,1.103442,-4.667273,1.348742,-1.393500,-5.795190,-9.502805,5.225894,1.704873,4.584408,-5.457339,7.227835,-2.081252,-6.939033,-1.415898,-9.407737,-9.951557,-4.026567,0.340854,-7.306506,1.319417,3.158822,-0.278688,-0.296119,-8.797682,7.718609,-4.785646,-9.499686,0.247322,-7.438007,0.692665,8.406685,-5.779438,2.639310,6.684988,-0.614836,-9.359306,-9.029061,-7.029191,-3.085054,-8.513050,9.129440,-9.918608,-3.640012,-4.515532,-1.013349,4.055114,-3.591357,7.051283,1.103018,2.511866,5.990424,8.427166,8.876219,4.894619,-3.318868,5.234500,-7.622331,9.688550,0.917228,8.854601,-6.007800,4.175305,1.997077,-6.146337,3.940311,-1.147155,1.725464,0.654234,8.074278,-0.732061,-1.995693,-4.226772,8.261617,1.045600,3.206767,-3.218887,-7.098487,-8.370782,7.940238,-6.183394,1.976163,5.653476,5.584632,1.311274,1.260469,-4.575154,4.880141,2.662996,5.810143,8.045976,1.174508,-1.667727,-5.803700,8.377126,2.372066,-3.043469,-6.263974,1.572209,-5.986931,1.676370,-9.797401,-7.578028,-3.594861,-2.615337,-5.970991,-6.457704,-2.266177,1.499098,-8.041283,-0.954321,1.151519,-1.682412,-8.673384,4.324992,-8.623476,9.220080,-8.902965,-0.970934,7.847915,-8.597106,-2.575801,6.380818,7.926181,6.409487,-6.749161,2.865738,9.103917,0.579663,6.058187,-1.404392,1.875541,-1.749022,4.316090,-5.414518,-4.881514,1.317236,-4.131928,1.446632,1.815048,1.877025,-2.418449,8.585848,-7.677525,1.723682,4.427947,7.282507,7.250920,9.917205,-0.047216,4.104598,-5.523401,0.697759,-6.091133,1.875244,-2.446231,8.650018,3.228216,-6.727933,3.683932,-3.506072,4.816715,-4.996636,8.590471,-7.383250,0.525835,-2.374375,-0.897544,-4.294906,-7.354019,-0.116374,-9.462143,1.891499,1.727845,3.158683,-2.911579,2.826853,9.301860,-2.892872,8.581390,-9.515632,2.522626,6.339821,5.738056,-9.858607,5.725693,-1.211500,-8.223430,2.486984,3.717667,-3.251241,-1.174435,0.181915,8.162639,8.342445,-8.941249,-5.781663,-9.988836,6.928470,2.685626,-5.135185,7.171976,5.678316,-9.801317,2.639938,5.400043], dtype = "float32")#candidate|4148|(286,)|const|float32
call_4147 = relay.TupleGetItem(func_3080_call(relay.reshape(const_4148.astype('float32'), [2, 11, 13])), 0)
call_4149 = relay.TupleGetItem(func_3083_call(relay.reshape(const_4148.astype('float32'), [2, 11, 13])), 0)
output = relay.Tuple([uop_4130,bop_4138,call_4147,const_4148,])
output2 = relay.Tuple([uop_4130,bop_4138,call_4149,const_4148,])
func_4151 = relay.Function([var_4125,], output)
mod['func_4151'] = func_4151
mod = relay.transform.InferType()(mod)
mutated_mod['func_4151'] = func_4151
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4152 = relay.var("var_4152", dtype = "float32", shape = (10, 1, 2))#candidate|4152|(10, 1, 2)|var|float32
func_4151_call = mutated_mod.get_global_var('func_4151')
call_4153 = func_4151_call(var_4152)
output = call_4153
func_4154 = relay.Function([var_4152], output)
mutated_mod['func_4154'] = func_4154
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4248 = relay.var("var_4248", dtype = "float32", shape = (4, 16, 9))#candidate|4248|(4, 16, 9)|var|float32
uop_4249 = relay.sqrt(var_4248.astype('float32')) # shape=(4, 16, 9)
func_1682_call = mod.get_global_var('func_1682')
func_1688_call = mutated_mod.get_global_var('func_1688')
const_4252 = relay.const([8,6,8,6,-6,4,-10,-1,3,-5,-7,5,7,3,9,9,2,3,-9,-9,-10,10,1,4,-1,4,-5,6,-8,8,-5,-3,4,-6,-4,7,10,-4,1,9,-7,2,2,4,8,-7,10,-9,-7,7,-2,5,-4,-6,-9,6,8,7,-9,1,-4,-10,8,1,6,7,4,3,3,4,-6,9,10,5,-9,-7,-5,-9,8,-6,-10,2,7,4,7,-1,8,-7,5,10,-8,-7,5,4,6,6,5,9,-5,1,9,-5,1,7,-3,10,-3,-4,2,2,2,-1,-7,-10,-3,6,-4,-9,4,2,5,1,-10,-8,3,-2,7,-3,-4,-9,-3,-9,6,3,-5,9,9,-10,3,3,6,-2,-9,-7,7,1,1,-8,-9,-8,7,6,5,9,4,5,-7,4,3,2,9,1,-3,-10,-1,-9,-6,-8,-1,-1,7,6,7,4,3,-10,-9,-4,-2,-5,3,-5,6,-1,8,-1,-2,-3,-9,8,2,6,-1,-2,-5,7,-8,8,-6,3,5,-9,3,5,-8,3,1,9,-10,-6,-7,-4,7,-1,2,-7], dtype = "int16")#candidate|4252|(216,)|const|int16
const_4253 = relay.const([3,9,-3,-1,6,4,5,-8,8,7,-2,-5,-7,8,6,-1,9,-9,8,-9,-3,2,8,2,-5,9,3,-4,-2,6,10,-9,9,3,9,2,6,3,-3,-9,3,-8,3,9,-4,5,4,7,5,1,-2,7,4,-2,-6,5,-3,8,-5,-3,-3,5,6,1,1,-5,-2,3,-4,-4,9,10,4,-10,-4,-2,-3,4,-10,-3,4,6,-2,-5,7,5,-3,-8,2,8,10,4,-8,5,1,10,5,5,-8,-4,-2,-1,-5,-1,-6,4,10,1,6,9,3,-5,7,8,2,10,-8,-8,9,-9,-10,-1,2,-2,8,-8,-9,1,-4,-1,8,10,-2,10,-8,8,-5,8,-3,-8,2,-3,-8,8,3,8,-3,-9,7,-8,-10,2,-5,3,-3,-10,6,5,-6,-7,2,-2,6,-10,3,-7,-4,8,-9,9,1,-4,-1,-10,2,9,3,-9,-3,1,8,-6,-6,2,-7,-7,2,-5,2,1,-3,10,-2,-4,-9,-8,10,9,-10,1,-4,6,-2,9,8,-10,2,6,10,-6,4,5,-10,2,-5,-9,-3,-5,8,1,-5,7,-2,9,5,-2,-1,-5,-1,-5,9,-7,1,-7,7,-6,-10,10,-8,-5,-6,1,4,-10,-10,1,-9,2,-10,8,7,-10,7,-9,8,-5,9,-4,2,7,-7,1,-7,-7,-2,-6,8,-3,5,9,6,-10,4,5,7,7,-10,-1,3,-6,2,-3,-10,-7,-10,10,4,8,-5,-1,-7,-8,9,6,7,9,5,-2,-2,-10,7,8,-2,-7,-3,1,9,9,-1,3,8,-9,-6,8,2,-10,-9,-10,7,10,-8,-10,-2,-6,-3,-3,1,-5,-5,-6,-2,5,7,2,3,-1,-7,-9,-7,4,-3,4,8,-2,-2,-7,-7,6,8,-5,4,-3,7,9,-6,-6,9,3,-7,10,7,6,4,7,1,-4,-8,-5,-10,8,9,-4,-4,-8,6,-4,7,-7,3,-2,8,9,-6,2,9,1,6,6,6,10,-2,-5,4,2,7,-4,-4,2,7,6,-4,4,4,-7,-6,2,-3,8,10,7,-8,4,-1,-9,-8,6,4,1,10,8,-7,3,-1,9,3,-1,-4,2,-1,8,8,3,-2,9,2,-9,2,-9,4,-4,-2,9,-2,-5,-2,4,5,-1,10,2,-9,-1,2,4,7,-5,7,-7,5,-1,5,6,-1,-10,8,2,-2,8,2,9,2,-8,-10,-7,9,1,-3,5,-5,-6,-6,10,-1,1,2,5,-6,2,-10,-10,-7,2,-9,6,1,-6,-8,2,-5,-7,2,1,-6,3,-4,-2,5,2,10,-9,8,5,-2,-9,9,3,9,9,-9,-9,9,-5,-5,10,5,-6,7,-2,8,9,9,-9,8,-4,-2,1,6,6,4,-9,-7,3,6,-6,-9,10,-7,-6,6,-1,5,-2,9,-4,-5,-4,-8,8,-4,-8,7,3,-6,-8,-1,3,-2,-6,-2,-6,5,-1,6,-7,-4,-5,3,-5,-7,3,4,1,-2,1,-9,-3,6,7,1,-4,1,6,-9,2,5,-3,3,9,3,1,8,6,6,-7,7,2,3,1,10,-6,-3,6,-5,1,-6,9,4,7,9,7,-5,6,-6,8,2,-10,4,-1,2,6,6,-1,1,10,-10,-7,-7,-3,-2,10,-6,1,8,-9,-5,8,2,-2,7,-2,1,4,-4,3,-7,-10,-3,2,-2,-2,8,8,1,-3,-4,-9,-8,-4,-9,8,10,-8,-10,6,3,-1,-10,-3,9,-1,-2,-9,-3,-3,-10,8,-9,-4,-9,3,10,5,2,-1,3,-5,4,7,7,-10,1,8,6,-10,-4,-7,6,-4,-1,9,-1,-2,6,-2,9,1,-2,3,3,-3,8,-3,5,1,4,-9,-4,-10,10,5,-4,3,-5,3,2,7,7,2,-9,7,7,-10,7,-3,-10,10,3,1,10,6,-10,-9,4,9,8,-7,-2,-4,-7,-9,5,2,-1,-8,4,2,-8,3,4,-3,7,-7,-7,9,-10,-10,8,-5,-4,3,-6,4,-5,5,-8,-4,-10,-4,-2,2,3,-4,-5,-3,1,-9,-10,2,9,-7,-8,9,-1,-9,-10,-4,-5,6,-9,-1,5,-9,2,-10,-1,-7,9,-8,-1,-3,8,-3,-6,-4,-10,-5,-6,1,8,-10,-10,9,-3,10,-4,4,-2,8,10,5,9,-6,-6,5,-8,-2,-2,-8,8,10,4,-7,-4,4,-6,-3,-1,-2,-4,1,-1,-10,4,9,-9,3,6,-10,4,4,3,9,-6,10,-7,2,4,3,4,-9,5,-6,3,-1,10,-10,-5,-8,7,9,-1,-4,-6,2,-10,-5,-4,-8,-9,-7,-6,-3,-6,-10,-10,-9,-3,-5,-9,-1,9,-6,8,-3,4,-7,7,-1,-2,-5,3,3,-4,-7,5,-4,5,-9,-5,-2,-4,-9,-1,-1,-3,-5,-10,-4,-7,1,-10,-10,6,-10,4,10,-2,-9,1,-8,-8,-1,-3,5,8,6,3,-3,-5,-10,8,7,10,5,-7,6,-7,-4,-3,-2,6,-7,4,-8,6], dtype = "uint32")#candidate|4253|(975,)|const|uint32
var_4254 = relay.var("var_4254", dtype = "float32", shape = (56,))#candidate|4254|(56,)|var|float32
const_4255 = relay.const([[-8.107034,-5.442144,9.740081],[-8.295633,-1.175670,-8.455839],[4.191307,-5.834310,2.177930],[-4.870814,9.451999,-8.351607],[9.626134,-9.017742,9.976615],[-2.239982,-6.207763,-9.118957],[-3.186194,5.643746,5.220947],[-9.734376,-1.691877,-9.029348],[5.272294,-7.359593,6.570787],[7.278894,-3.487976,-3.182905],[-7.081616,-8.629811,9.899756],[-3.987637,6.341146,1.226560],[-2.130297,-2.802514,-8.649440],[-9.224485,3.360765,9.181290],[8.810421,3.714948,-4.358946],[6.245015,9.699026,7.777429],[-8.411071,-4.154265,-3.689136],[-6.528046,-6.924198,9.764575],[-0.846950,-0.354449,9.384679],[-1.871775,0.588803,-1.830665],[-2.925997,-9.580103,7.120422],[-0.610500,7.162355,-9.297169],[-8.217108,-6.230096,8.468598],[-3.843763,3.716947,8.261437],[-5.322615,9.776604,-9.361364],[1.327423,-9.832086,-9.421193]], dtype = "float64")#candidate|4255|(26, 3)|const|float64
call_4251 = relay.TupleGetItem(func_1682_call(relay.reshape(const_4252.astype('int16'), [4, 6, 9]), relay.reshape(const_4253.astype('uint32'), [975,]), relay.reshape(var_4254.astype('float32'), [56,]), relay.reshape(const_4255.astype('float64'), [78,]), ), 4)
call_4256 = relay.TupleGetItem(func_1688_call(relay.reshape(const_4252.astype('int16'), [4, 6, 9]), relay.reshape(const_4253.astype('uint32'), [975,]), relay.reshape(var_4254.astype('float32'), [56,]), relay.reshape(const_4255.astype('float64'), [78,]), ), 4)
func_1975_call = mod.get_global_var('func_1975')
func_1979_call = mutated_mod.get_global_var('func_1979')
const_4262 = relay.const([[-2,-1,-8,10,-7,7,2,-6,5,-2,1,-4,5,-4,3,7,8,2,-9,7,-5,-2,4,5,5,-6,-1,-9,10,7,3,7,-3,9,-3,6,1,-4,5,6,-7,8,3,-4,-3,8,-4,9,-6,-7,-5,7,-2,-2,-2,-1,-3,7,-8,-10,-2,7,3,-1,-4,-8,-5,4,-7,8,-5,10,-8,3,-10,7,1,-7,-9,3,-1,2,-7,-5,1,6,2,5,7,-6,-10,8,-8,-8,-5,10,-4,-2,-9,9,-10,-9,3,6,9,-6,4,2,8,9,-3,-9,-5,1,-8,5,5,2,-7,7,-10,-7,-6,-8,-3,10,-10,-4,-8,9,3,-5,10,-8,8,3,10,-4,-2,-5]], dtype = "uint64")#candidate|4262|(1, 140)|const|uint64
call_4261 = relay.TupleGetItem(func_1975_call(relay.reshape(const_4262.astype('uint64'), [2, 7, 10]), relay.reshape(const_4262.astype('uint64'), [2, 7, 10]), relay.reshape(const_4253.astype('uint32'), [975,]), ), 0)
call_4263 = relay.TupleGetItem(func_1979_call(relay.reshape(const_4262.astype('uint64'), [2, 7, 10]), relay.reshape(const_4262.astype('uint64'), [2, 7, 10]), relay.reshape(const_4253.astype('uint32'), [975,]), ), 0)
func_235_call = mod.get_global_var('func_235')
func_238_call = mutated_mod.get_global_var('func_238')
var_4272 = relay.var("var_4272", dtype = "float32", shape = (2160,))#candidate|4272|(2160,)|var|float32
const_4273 = relay.const([7.318387,8.566704,4.601954,1.508151,-4.611221,-5.775438,5.714204,9.365400,-7.343233,5.426562,-4.386930,-0.786621,-2.557350,-8.318549,3.672742,8.108043,5.454629,-4.463177,-5.101166,5.205003,4.813620,1.428746,-1.008802,7.713692,-7.440143,-3.200309,1.217357,2.696430,8.236624,1.027521,-6.928318,7.735541,2.238713,-5.984722,1.840374,-7.554555,4.530764,3.237965,7.440639,5.113156,1.685705,-1.971301,-6.359233,2.291600,-7.236126,-7.042385,3.276263,-1.660258,3.553897,-7.362279,-1.562045,8.218085,-7.452442,6.698493,-6.192442,1.748330,-1.982665,-9.339427,-4.086565,-0.762258,3.326540,9.270166,4.596426,8.773768,3.267796,9.820767,3.131353,0.484771,-0.549009,4.621892,2.224999,-5.247255,-1.271961,-7.263979,-0.819701,1.358346,-8.601694,7.068236,-4.622315,-2.713374,-3.672224,7.085549,9.324746,-6.166247,3.478450,-3.606018,-0.332256,-3.030320,7.393693,0.238011,-7.665681,0.747534,-6.520392,-1.681860,-5.498206,-0.362831,-3.404350,-1.281270,-3.953033,0.880564,-3.103437,2.424217,1.873332,5.324597,-4.216577,-5.081122,-3.523045,6.575430,-0.701971,7.442239,9.376581,-0.138246,-1.952251,5.177054,5.644311,-6.290549,-9.038723,-3.543254,-0.668851,-1.386673,3.528700,5.437850,8.315189,-3.303913,-8.880056,-8.261267,5.615606,7.372574,6.146073,-3.043027,-6.664321,-4.506866,-5.570686,-2.431822,-2.774733], dtype = "float32")#candidate|4273|(135,)|const|float32
call_4271 = relay.TupleGetItem(func_235_call(relay.reshape(var_4272.astype('float32'), [15, 9, 16]), relay.reshape(const_4273.astype('float32'), [15, 9]), ), 2)
call_4274 = relay.TupleGetItem(func_238_call(relay.reshape(var_4272.astype('float32'), [15, 9, 16]), relay.reshape(const_4273.astype('float32'), [15, 9]), ), 2)
output = relay.Tuple([uop_4249,call_4251,const_4252,const_4253,var_4254,const_4255,call_4261,const_4262,call_4271,var_4272,const_4273,])
output2 = relay.Tuple([uop_4249,call_4256,const_4252,const_4253,var_4254,const_4255,call_4263,const_4262,call_4274,var_4272,const_4273,])
func_4281 = relay.Function([var_4248,var_4254,var_4272,], output)
mod['func_4281'] = func_4281
mod = relay.transform.InferType()(mod)
var_4282 = relay.var("var_4282", dtype = "float32", shape = (4, 16, 9))#candidate|4282|(4, 16, 9)|var|float32
var_4283 = relay.var("var_4283", dtype = "float32", shape = (56,))#candidate|4283|(56,)|var|float32
var_4284 = relay.var("var_4284", dtype = "float32", shape = (2160,))#candidate|4284|(2160,)|var|float32
output = func_4281(var_4282,var_4283,var_4284,)
func_4285 = relay.Function([var_4282,var_4283,var_4284,], output)
mutated_mod['func_4285'] = func_4285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4372 = relay.var("var_4372", dtype = "bool", shape = (11, 3, 6))#candidate|4372|(11, 3, 6)|var|bool
var_4373 = relay.var("var_4373", dtype = "bool", shape = (11, 3, 6))#candidate|4373|(11, 3, 6)|var|bool
bop_4374 = relay.logical_and(var_4372.astype('bool'), relay.reshape(var_4373.astype('bool'), relay.shape_of(var_4372))) # shape=(11, 3, 6)
output = bop_4374
output2 = bop_4374
func_4383 = relay.Function([var_4372,var_4373,], output)
mod['func_4383'] = func_4383
mod = relay.transform.InferType()(mod)
var_4384 = relay.var("var_4384", dtype = "bool", shape = (11, 3, 6))#candidate|4384|(11, 3, 6)|var|bool
var_4385 = relay.var("var_4385", dtype = "bool", shape = (11, 3, 6))#candidate|4385|(11, 3, 6)|var|bool
output = func_4383(var_4384,var_4385,)
func_4386 = relay.Function([var_4384,var_4385,], output)
mutated_mod['func_4386'] = func_4386
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4437 = relay.var("var_4437", dtype = "float64", shape = (9, 8, 16))#candidate|4437|(9, 8, 16)|var|float64
uop_4438 = relay.rsqrt(var_4437.astype('float64')) # shape=(9, 8, 16)
func_2129_call = mod.get_global_var('func_2129')
func_2132_call = mutated_mod.get_global_var('func_2132')
const_4445 = relay.const([-7,-5,1,9,-3,-7,7,9,-5,5,-3,3,2,10,-3,9,-9,6,-2,-1,-1,8,-4,-9,-2,-3,1,-4,7,8,6,-3,-2,6,-3,-3,-9,-6,9,-2,-10,-5,-10,-1,-4,8,-6,4,9,4,-7,8,-7,9,-10,5,5,-10,-3,-3,-1,5,-3,7,-9,5,7,1,8,10,-10,-9,-8,-1,3,6,-6,-3,-9,10,3,-3,-7,-6,4,-6,-10,-1,-5,9,-6,-1,-3,-1,9,10,5,2,-8,8,4,-10,10,-5,6,2,-7,6,1,4,-7,2,10,5,-4,-1,8,3,5,-4,1,4,-10,10,8,-1,-10,8,-7,-7,-7,-9,2,-4,1,-7,-5,-2,1,-8,8,5,-2,-10,-7,10,-7,-10,3,5,3,6,-3,3,-10,5], dtype = "uint16")#candidate|4445|(156,)|const|uint16
call_4444 = relay.TupleGetItem(func_2129_call(relay.reshape(const_4445.astype('uint16'), [3, 4, 13])), 0)
call_4446 = relay.TupleGetItem(func_2132_call(relay.reshape(const_4445.astype('uint16'), [3, 4, 13])), 0)
func_2447_call = mod.get_global_var('func_2447')
func_2450_call = mutated_mod.get_global_var('func_2450')
var_4448 = relay.var("var_4448", dtype = "uint8", shape = ())#candidate|4448|()|var|uint8
const_4449 = relay.const([3,-2,6,4,-8,2,-10,-5,3,3,-6,-8,-1,-2,-3,4,9,-3,-5,10,5,-9,7,1,6,5,-9,4,1,8,3,2,-5,-4,1,6,-6,-10,10,10,-7,7,-9,-5,-5,6,4,9,-2,-4,8,10,-6,6,4,-10,-4,9,8,-4,9,-2,-8,2,5,-5,-5,-1,-9,-7,-7,-4], dtype = "uint8")#candidate|4449|(72,)|const|uint8
call_4447 = relay.TupleGetItem(func_2447_call(relay.reshape(var_4448.astype('uint8'), []), relay.reshape(const_4449.astype('uint8'), [12, 1, 6]), ), 0)
call_4450 = relay.TupleGetItem(func_2450_call(relay.reshape(var_4448.astype('uint8'), []), relay.reshape(const_4449.astype('uint8'), [12, 1, 6]), ), 0)
bop_4455 = relay.logical_and(uop_4438.astype('bool'), relay.reshape(var_4437.astype('bool'), relay.shape_of(uop_4438))) # shape=(9, 8, 16)
func_2860_call = mod.get_global_var('func_2860')
func_2863_call = mutated_mod.get_global_var('func_2863')
var_4466 = relay.var("var_4466", dtype = "float64", shape = (264,))#candidate|4466|(264,)|var|float64
call_4465 = func_2860_call(relay.reshape(var_4448.astype('float64'), []), relay.reshape(var_4466.astype('float64'), [11, 6, 4]), )
call_4467 = func_2860_call(relay.reshape(var_4448.astype('float64'), []), relay.reshape(var_4466.astype('float64'), [11, 6, 4]), )
func_2129_call = mod.get_global_var('func_2129')
func_2132_call = mutated_mod.get_global_var('func_2132')
call_4469 = relay.TupleGetItem(func_2129_call(relay.reshape(const_4445.astype('uint16'), [3, 4, 13])), 1)
call_4470 = relay.TupleGetItem(func_2132_call(relay.reshape(const_4445.astype('uint16'), [3, 4, 13])), 1)
var_4475 = relay.var("var_4475", dtype = "uint8", shape = (12, 15, 6))#candidate|4475|(12, 15, 6)|var|uint8
bop_4476 = relay.less(call_4447.astype('bool'), var_4475.astype('bool')) # shape=(12, 15, 6)
bop_4479 = relay.less(call_4450.astype('bool'), var_4475.astype('bool')) # shape=(12, 15, 6)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
var_4494 = relay.var("var_4494", dtype = "bool", shape = (350,))#candidate|4494|(350,)|var|bool
call_4493 = relay.TupleGetItem(func_1152_call(relay.reshape(var_4494.astype('bool'), [5, 10, 7])), 0)
call_4495 = relay.TupleGetItem(func_1154_call(relay.reshape(var_4494.astype('bool'), [5, 10, 7])), 0)
output = relay.Tuple([call_4444,const_4445,var_4448,const_4449,bop_4455,call_4465,var_4466,call_4469,bop_4476,call_4493,var_4494,])
output2 = relay.Tuple([call_4446,const_4445,var_4448,const_4449,bop_4455,call_4467,var_4466,call_4470,bop_4479,call_4495,var_4494,])
func_4499 = relay.Function([var_4437,var_4448,var_4466,var_4475,var_4494,], output)
mod['func_4499'] = func_4499
mod = relay.transform.InferType()(mod)
mutated_mod['func_4499'] = func_4499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4499_call = mutated_mod.get_global_var('func_4499')
var_4501 = relay.var("var_4501", dtype = "float64", shape = (9, 8, 16))#candidate|4501|(9, 8, 16)|var|float64
var_4502 = relay.var("var_4502", dtype = "uint8", shape = ())#candidate|4502|()|var|uint8
var_4503 = relay.var("var_4503", dtype = "float64", shape = (264,))#candidate|4503|(264,)|var|float64
var_4504 = relay.var("var_4504", dtype = "uint8", shape = (12, 15, 6))#candidate|4504|(12, 15, 6)|var|uint8
var_4505 = relay.var("var_4505", dtype = "bool", shape = (350,))#candidate|4505|(350,)|var|bool
call_4500 = func_4499_call(var_4501,var_4502,var_4503,var_4504,var_4505,)
output = call_4500
func_4506 = relay.Function([var_4501,var_4502,var_4503,var_4504,var_4505,], output)
mutated_mod['func_4506'] = func_4506
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4512 = relay.var("var_4512", dtype = "int16", shape = (1, 8, 13))#candidate|4512|(1, 8, 13)|var|int16
const_4513 = relay.const([[[-9,-6,-4,2,4,-7,7,7,-5,-8,-10,-1,-4],[-10,4,-9,-3,-10,5,6,-7,6,-10,-2,9,7],[-1,-6,9,-1,4,-3,-5,3,-8,3,-1,-7,-2],[-5,9,2,-4,-4,-6,3,-7,4,-1,3,-5,5],[5,-8,-3,2,9,-1,-2,-4,-3,8,-3,-1,-1],[-6,-3,4,-4,-7,-7,10,-10,-7,-9,-3,-7,-10],[3,-9,-8,-3,-7,-8,-9,-10,1,4,-5,8,-3],[-4,-9,-3,10,7,8,-8,6,7,-3,6,9,7]],[[-1,7,5,-4,-10,7,8,7,-5,-10,4,-8,6],[-1,2,-10,3,4,-9,-10,-5,8,-2,-9,1,-8],[7,-2,-8,10,8,-2,5,9,-6,4,8,5,6],[-9,-3,4,4,5,-6,3,-4,7,3,-7,6,10],[-3,8,-9,8,5,-4,-9,-3,5,-3,1,2,5],[-4,-1,7,-1,5,1,4,7,-4,-10,-3,3,7],[5,9,-1,1,9,-7,-2,-10,6,-8,5,-9,-1],[9,-8,9,8,-3,10,10,-3,-10,9,-7,-8,-10]]], dtype = "int16")#candidate|4513|(2, 8, 13)|const|int16
bop_4514 = relay.less(var_4512.astype('bool'), const_4513.astype('bool')) # shape=(2, 8, 13)
bop_4517 = relay.multiply(bop_4514.astype('uint16'), var_4512.astype('uint16')) # shape=(2, 8, 13)
bop_4527 = relay.not_equal(bop_4517.astype('bool'), relay.reshape(const_4513.astype('bool'), relay.shape_of(bop_4517))) # shape=(2, 8, 13)
output = relay.Tuple([bop_4527,])
output2 = relay.Tuple([bop_4527,])
func_4534 = relay.Function([var_4512,], output)
mod['func_4534'] = func_4534
mod = relay.transform.InferType()(mod)
var_4535 = relay.var("var_4535", dtype = "int16", shape = (1, 8, 13))#candidate|4535|(1, 8, 13)|var|int16
output = func_4534(var_4535)
func_4536 = relay.Function([var_4535], output)
mutated_mod['func_4536'] = func_4536
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4658 = relay.var("var_4658", dtype = "float64", shape = (7, 13, 5))#candidate|4658|(7, 13, 5)|var|float64
uop_4659 = relay.atan(var_4658.astype('float64')) # shape=(7, 13, 5)
output = relay.Tuple([uop_4659,])
output2 = relay.Tuple([uop_4659,])
func_4662 = relay.Function([var_4658,], output)
mod['func_4662'] = func_4662
mod = relay.transform.InferType()(mod)
mutated_mod['func_4662'] = func_4662
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4663 = relay.var("var_4663", dtype = "float64", shape = (7, 13, 5))#candidate|4663|(7, 13, 5)|var|float64
func_4662_call = mutated_mod.get_global_var('func_4662')
call_4664 = func_4662_call(var_4663)
output = call_4664
func_4665 = relay.Function([var_4663], output)
mutated_mod['func_4665'] = func_4665
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4672 = relay.const([[[5,8,8,4,5,-8,1,4]],[[6,2,-9,9,-7,-7,-4,-10]],[[10,-9,-10,-4,9,9,-9,-3]],[[-7,3,9,-7,8,-7,9,-3]],[[7,-9,-3,1,8,-1,5,2]],[[-10,-7,6,-3,-8,-7,10,-9]]], dtype = "int16")#candidate|4672|(6, 1, 8)|const|int16
var_4673 = relay.var("var_4673", dtype = "int16", shape = (6, 14, 8))#candidate|4673|(6, 14, 8)|var|int16
bop_4674 = relay.not_equal(const_4672.astype('bool'), var_4673.astype('bool')) # shape=(6, 14, 8)
func_2860_call = mod.get_global_var('func_2860')
func_2863_call = mutated_mod.get_global_var('func_2863')
const_4697 = relay.const(-5.028725, dtype = "float64")#candidate|4697|()|const|float64
var_4698 = relay.var("var_4698", dtype = "float64", shape = (264,))#candidate|4698|(264,)|var|float64
call_4696 = func_2860_call(relay.reshape(const_4697.astype('float64'), []), relay.reshape(var_4698.astype('float64'), [11, 6, 4]), )
call_4699 = func_2860_call(relay.reshape(const_4697.astype('float64'), []), relay.reshape(var_4698.astype('float64'), [11, 6, 4]), )
output = relay.Tuple([bop_4674,call_4696,const_4697,var_4698,])
output2 = relay.Tuple([bop_4674,call_4699,const_4697,var_4698,])
func_4706 = relay.Function([var_4673,var_4698,], output)
mod['func_4706'] = func_4706
mod = relay.transform.InferType()(mod)
var_4707 = relay.var("var_4707", dtype = "int16", shape = (6, 14, 8))#candidate|4707|(6, 14, 8)|var|int16
var_4708 = relay.var("var_4708", dtype = "float64", shape = (264,))#candidate|4708|(264,)|var|float64
output = func_4706(var_4707,var_4708,)
func_4709 = relay.Function([var_4707,var_4708,], output)
mutated_mod['func_4709'] = func_4709
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4878 = relay.var("var_4878", dtype = "int8", shape = (11, 14, 6))#candidate|4878|(11, 14, 6)|var|int8
var_4879 = relay.var("var_4879", dtype = "int8", shape = (11, 14, 6))#candidate|4879|(11, 14, 6)|var|int8
bop_4880 = relay.equal(var_4878.astype('bool'), relay.reshape(var_4879.astype('bool'), relay.shape_of(var_4878))) # shape=(11, 14, 6)
output = relay.Tuple([bop_4880,])
output2 = relay.Tuple([bop_4880,])
func_4883 = relay.Function([var_4878,var_4879,], output)
mod['func_4883'] = func_4883
mod = relay.transform.InferType()(mod)
mutated_mod['func_4883'] = func_4883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4883_call = mutated_mod.get_global_var('func_4883')
var_4885 = relay.var("var_4885", dtype = "int8", shape = (11, 14, 6))#candidate|4885|(11, 14, 6)|var|int8
var_4886 = relay.var("var_4886", dtype = "int8", shape = (11, 14, 6))#candidate|4886|(11, 14, 6)|var|int8
call_4884 = func_4883_call(var_4885,var_4886,)
output = call_4884
func_4887 = relay.Function([var_4885,var_4886,], output)
mutated_mod['func_4887'] = func_4887
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4974 = relay.const([[[-9.612029,-0.995703,-7.246105,-7.247461,9.433931,9.992050,-0.286673,5.178785,2.206608,-4.061313,-3.777270,-5.183302,3.557431,7.900666],[-1.886664,-2.798890,-7.437527,0.236004,-3.907564,0.865019,2.634088,4.585957,-0.510065,1.932475,0.339851,-0.677196,-3.630358,-1.247432],[-7.754949,6.971516,-9.194502,6.750918,0.221800,-6.563700,-1.529560,6.218001,-4.136926,2.445996,-3.428341,-7.096702,-8.200907,5.525292],[8.100647,7.812944,5.046508,-1.156931,-8.026417,-8.885483,6.660629,4.622962,-5.664397,6.712869,0.422426,9.825303,3.310340,-6.204026],[-6.484447,6.344723,4.808383,4.842525,2.464550,3.512864,3.272441,8.876951,-1.046067,-5.750978,-8.870852,7.608469,-7.479784,1.864919],[2.456878,3.582627,8.730162,8.935822,9.459670,2.070033,4.055155,-0.381675,-4.643646,9.072398,4.272799,2.370205,1.143147,2.138444],[3.656104,-9.234238,-8.593841,-2.375343,-8.150015,5.385163,-8.727377,-6.856964,7.705030,-7.906514,1.521288,-0.635895,6.586096,-2.401116],[-1.719826,-3.171155,-3.250616,-5.795720,-9.120905,-4.424188,6.306449,1.844970,-6.885874,9.455108,-2.081737,6.913971,1.247929,-9.726080],[6.631729,9.011559,7.177826,3.936579,-1.586633,-0.570072,-4.722350,0.633520,-6.476086,4.299541,3.719991,-5.386571,-7.527488,2.238604],[1.767289,-2.928530,-4.430416,5.466565,6.510547,4.978112,-3.631779,-9.033121,-4.076155,-2.934759,-1.851609,7.744834,-7.858733,-5.804867],[2.187541,-7.200742,8.635155,7.610515,6.869597,1.861225,8.287109,-2.124641,5.517624,-2.701100,0.090679,-1.860611,-3.889924,9.625418],[-6.004476,6.183255,6.657476,-1.147585,-1.609043,-5.293925,-8.350650,-0.342676,-5.641293,-8.465988,0.677946,0.620459,6.728473,5.149044],[4.248805,2.820042,-9.775854,7.548274,-5.061301,-9.457232,2.493045,-4.052645,7.825972,6.742417,-1.757837,2.100780,-5.477488,-6.126855]],[[-8.596564,0.944018,-6.173998,6.418637,6.735496,-0.929302,0.645853,-2.011634,3.084038,-2.413782,4.582016,-2.852901,2.581534,5.298181],[-3.117312,-4.023752,1.229760,-4.471066,-6.637175,-6.170746,-2.188076,6.138438,-6.728271,-9.277701,5.159261,-7.526116,-5.043636,-2.878505],[-8.582907,6.011925,8.035800,2.897636,4.065331,-0.371612,-9.187565,0.759030,0.956908,-4.580389,-0.219525,5.503018,9.794359,-5.794775],[-3.335581,-3.342729,-4.700324,9.644873,3.351304,8.431239,-6.138777,-3.252348,-1.428022,8.597049,-9.711328,5.174877,-8.102814,-8.942154],[-6.081818,9.804557,3.340236,3.481303,7.182541,2.029528,-1.555207,2.048640,-5.305701,6.827709,2.884003,-3.396997,-3.151962,-0.094433],[-0.664574,-4.521601,6.322896,0.391868,3.697571,-2.859527,4.846120,9.123311,-5.625671,-1.137998,-3.608041,-5.595008,-4.174450,-6.452916],[-0.154337,6.323039,8.382339,-9.690383,9.256091,-6.897921,-7.548343,6.481329,-2.556230,1.173973,7.082258,-2.805077,0.545696,9.264486],[6.697184,-0.580221,-7.742316,6.628155,-0.802727,-4.838831,4.329438,-5.643623,-3.820816,-7.171311,6.521624,2.681481,1.551496,-1.208670],[-7.820514,6.850929,9.202313,-5.414852,9.661036,-4.457109,9.083168,-7.893411,4.688863,-3.500139,-1.418873,-6.736037,7.680334,2.170705],[4.042083,6.678611,8.107951,-0.052657,0.710800,8.840535,-4.781034,-7.235935,-1.447592,-5.778809,0.735817,6.236380,6.282520,7.107693],[-7.169237,-7.010291,1.545310,3.758854,-2.348166,9.595455,-8.098342,-8.384064,-0.405127,-7.970706,0.469577,-9.454104,-5.543994,5.832845],[-8.218978,-1.976039,1.293956,-4.842806,-6.111605,6.331232,1.982486,-2.289746,1.194317,-4.522267,6.014615,7.269978,-7.100328,-4.684959],[4.706073,-5.326293,-9.043342,-0.774250,9.594946,-1.485871,5.743248,-4.383329,2.193213,-9.574888,-9.840185,-4.893658,-6.217856,-6.357658]]], dtype = "float64")#candidate|4974|(2, 13, 14)|const|float64
uop_4975 = relay.sin(const_4974.astype('float64')) # shape=(2, 13, 14)
output = uop_4975
output2 = uop_4975
func_4981 = relay.Function([], output)
mod['func_4981'] = func_4981
mod = relay.transform.InferType()(mod)
mutated_mod['func_4981'] = func_4981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4981_call = mutated_mod.get_global_var('func_4981')
call_4982 = func_4981_call()
output = call_4982
func_4983 = relay.Function([], output)
mutated_mod['func_4983'] = func_4983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4981_call = mod.get_global_var('func_4981')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_5013 = func_4981_call()
call_5014 = func_4981_call()
func_3156_call = mod.get_global_var('func_3156')
func_3159_call = mutated_mod.get_global_var('func_3159')
var_5039 = relay.var("var_5039", dtype = "float64", shape = (6, 44))#candidate|5039|(6, 44)|var|float64
call_5038 = relay.TupleGetItem(func_3156_call(relay.reshape(var_5039.astype('float64'), [264,])), 0)
call_5040 = relay.TupleGetItem(func_3159_call(relay.reshape(var_5039.astype('float64'), [264,])), 0)
func_3044_call = mod.get_global_var('func_3044')
func_3051_call = mutated_mod.get_global_var('func_3051')
var_5055 = relay.var("var_5055", dtype = "float64", shape = (1568,))#candidate|5055|(1568,)|var|float64
const_5056 = relay.const(-8, dtype = "uint8")#candidate|5056|()|const|uint8
const_5057 = relay.const([[10,-8,4],[-9,-6,-2],[-10,7,-7],[-8,-9,-10],[5,-8,1],[-6,9,-4],[-1,-5,-5],[-7,-1,10],[-3,7,-3],[3,-6,3]], dtype = "uint32")#candidate|5057|(10, 3)|const|uint32
var_5058 = relay.var("var_5058", dtype = "float64", shape = (78,))#candidate|5058|(78,)|var|float64
var_5059 = relay.var("var_5059", dtype = "float32", shape = (135,))#candidate|5059|(135,)|var|float32
call_5054 = relay.TupleGetItem(func_3044_call(relay.reshape(var_5055.astype('float64'), [14, 16, 7]), relay.reshape(const_5056.astype('uint8'), []), relay.reshape(const_5057.astype('uint32'), [30,]), relay.reshape(var_5058.astype('float64'), [78,]), relay.reshape(var_5059.astype('float32'), [135,]), ), 7)
call_5060 = relay.TupleGetItem(func_3051_call(relay.reshape(var_5055.astype('float64'), [14, 16, 7]), relay.reshape(const_5056.astype('uint8'), []), relay.reshape(const_5057.astype('uint32'), [30,]), relay.reshape(var_5058.astype('float64'), [78,]), relay.reshape(var_5059.astype('float32'), [135,]), ), 7)
output = relay.Tuple([call_5013,call_5038,var_5039,call_5054,var_5055,const_5056,const_5057,var_5058,var_5059,])
output2 = relay.Tuple([call_5014,call_5040,var_5039,call_5060,var_5055,const_5056,const_5057,var_5058,var_5059,])
func_5079 = relay.Function([var_5039,var_5055,var_5058,var_5059,], output)
mod['func_5079'] = func_5079
mod = relay.transform.InferType()(mod)
mutated_mod['func_5079'] = func_5079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5079_call = mutated_mod.get_global_var('func_5079')
var_5081 = relay.var("var_5081", dtype = "float64", shape = (6, 44))#candidate|5081|(6, 44)|var|float64
var_5082 = relay.var("var_5082", dtype = "float64", shape = (1568,))#candidate|5082|(1568,)|var|float64
var_5083 = relay.var("var_5083", dtype = "float64", shape = (78,))#candidate|5083|(78,)|var|float64
var_5084 = relay.var("var_5084", dtype = "float32", shape = (135,))#candidate|5084|(135,)|var|float32
call_5080 = func_5079_call(var_5081,var_5082,var_5083,var_5084,)
output = call_5080
func_5085 = relay.Function([var_5081,var_5082,var_5083,var_5084,], output)
mutated_mod['func_5085'] = func_5085
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5100 = relay.const([[-8.822918,7.701121,0.466025,-8.595442,8.967924,-4.199912,8.539614,-1.573010,-5.648213],[2.603405,-5.499221,-6.536201,-7.961074,0.112826,-2.719006,4.024309,-3.439372,7.040855],[-8.222842,-9.258726,-0.469513,-1.578158,-2.922315,3.692135,-7.786484,0.518450,4.886075],[-9.915340,-6.208952,-1.019215,-5.179439,5.824658,-3.271370,-4.749402,-1.328168,-4.404676],[-4.993720,-8.708813,4.740207,2.270598,-4.091710,7.924096,-5.656364,-6.679606,4.972978],[0.848613,-4.086509,-3.209294,-6.792227,6.937651,8.927120,7.871110,5.174883,7.776577],[1.769264,-1.290624,5.569099,-7.808822,6.805173,-6.913127,5.932336,-9.122681,-6.860612]], dtype = "float64")#candidate|5100|(7, 9)|const|float64
uop_5101 = relay.acos(const_5100.astype('float64')) # shape=(7, 9)
output = relay.Tuple([uop_5101,])
output2 = relay.Tuple([uop_5101,])
func_5115 = relay.Function([], output)
mod['func_5115'] = func_5115
mod = relay.transform.InferType()(mod)
mutated_mod['func_5115'] = func_5115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mutated_mod.get_global_var('func_5115')
call_5116 = func_5115_call()
output = call_5116
func_5117 = relay.Function([], output)
mutated_mod['func_5117'] = func_5117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4981_call = mod.get_global_var('func_4981')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_5121 = func_4981_call()
call_5122 = func_4981_call()
uop_5132 = relay.sqrt(call_5121.astype('float32')) # shape=(2, 13, 14)
uop_5134 = relay.sqrt(call_5122.astype('float32')) # shape=(2, 13, 14)
output = uop_5132
output2 = uop_5134
func_5136 = relay.Function([], output)
mod['func_5136'] = func_5136
mod = relay.transform.InferType()(mod)
mutated_mod['func_5136'] = func_5136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5136_call = mutated_mod.get_global_var('func_5136')
call_5137 = func_5136_call()
output = call_5137
func_5138 = relay.Function([], output)
mutated_mod['func_5138'] = func_5138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5136_call = mod.get_global_var('func_5136')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_5203 = func_5136_call()
call_5204 = func_5136_call()
const_5208 = relay.const([[[1.535756,-8.014676,4.702563,2.117722,-6.992813,2.943068,-9.808186,-1.867065,-3.578439,3.287066,-1.111237,-1.653798,3.136611,9.903701],[-2.741657,-7.423100,-5.167517,-6.078974,-6.743633,7.288747,2.545294,9.027476,8.742435,5.231604,1.598859,-8.551094,3.320004,5.213690],[1.522255,7.526725,-9.389624,4.439763,-3.006360,-0.014062,2.755381,9.781465,4.471477,-8.033044,8.741485,-6.973913,0.110029,-6.181302],[7.160132,5.721342,-1.258272,0.764012,-8.862682,-6.468968,-8.609340,-0.184238,-4.939992,-1.941144,-2.680021,-0.976636,-5.729712,-1.304063],[7.435248,-1.757100,-7.527468,-1.291717,5.462050,2.730741,-4.157065,-5.188057,3.366042,4.751760,6.896066,9.655501,-6.827435,9.156043],[-0.678846,-7.647854,-0.335302,-1.010517,6.011221,-2.686121,-3.161156,-1.155040,8.106151,4.204725,7.090114,-7.316120,-3.441503,-9.991777],[2.807822,-7.573263,5.600309,9.541868,1.738269,7.767615,-3.860169,2.480822,3.002312,-8.958119,6.143708,0.717058,-0.340860,7.707666],[3.445460,8.803270,9.871095,-1.172610,7.873300,-2.000150,-5.620095,8.779616,1.789669,9.435993,-8.990280,9.222346,-4.445401,6.680667],[-2.398141,8.037725,-4.195733,-3.293131,-3.737791,7.726216,4.552760,3.469517,0.346890,-6.581917,6.730884,1.641947,2.647066,0.251141],[-9.830929,-6.521874,2.284741,-8.075277,3.398342,1.016939,-7.974303,4.611292,2.179833,0.178921,9.443616,9.689685,6.933036,-2.393565],[-2.173394,-7.581579,-7.325515,5.185631,2.133269,-0.445439,2.657858,-6.133193,-2.998248,1.617905,-1.278389,-7.891522,-3.420000,3.530219],[-7.321940,7.795944,1.153444,1.899588,-1.140337,-4.364268,1.947968,-1.825228,-2.719254,-1.217772,-2.852484,-6.095789,-4.056287,-1.687087],[2.556523,-3.894206,-9.049076,-2.623766,-3.132567,1.936252,-7.441046,-1.218386,-3.682012,-6.171620,9.357920,3.467297,-9.057293,0.391371]],[[-6.395403,-0.482984,3.297624,-3.940045,-5.191129,4.068061,-6.304120,6.314695,-5.378745,-4.594602,1.534018,-7.138937,4.355491,-7.002217],[9.626975,-2.355265,-2.214549,7.128759,-5.607992,5.053157,-0.210324,0.123479,7.759975,-1.207921,-5.002932,3.601964,8.618138,-9.370524],[0.316061,6.714023,-9.445739,8.872077,-3.533589,-7.393817,-5.111422,6.751025,3.524360,2.113498,7.804064,-8.880822,4.149409,6.425169],[1.936039,4.886097,8.424066,-6.113938,0.170960,-0.604282,-0.017013,-1.956089,-1.082476,-0.128460,-5.673815,-0.757038,0.314733,4.620554],[-2.650306,0.132925,-4.753025,3.238307,6.749328,-5.305748,8.712158,-3.647825,9.842542,-4.241377,-8.375032,9.965920,-8.947592,9.577119],[1.877532,-3.068673,7.913815,4.675472,9.828613,8.530986,-1.336046,3.462312,-7.178611,-2.691615,-7.777897,5.791164,4.168236,1.649937],[1.925071,8.428929,9.181905,-0.866077,1.159129,-7.856832,-8.974726,-4.058998,8.065153,-6.876920,4.025876,-2.477287,6.077267,7.787726],[-3.835855,5.480477,5.150386,-0.382278,-3.803928,6.168485,4.078556,-1.787582,-7.439500,-1.433783,-2.990469,1.468466,9.670132,0.132499],[-4.564644,8.183815,7.394375,-7.309306,0.429324,0.740256,1.172049,-6.987714,9.029885,4.713750,2.279386,1.234951,-9.174371,5.709040],[-2.270941,9.845758,9.804656,-2.017782,5.029490,1.563184,3.960217,-1.143557,-2.959430,8.844667,-5.788538,0.286880,8.413935,7.801999],[4.577784,8.735372,-5.265242,-7.721201,-7.366487,-9.588584,6.281080,-2.765800,0.538556,-4.478525,4.223792,8.028796,-1.936262,3.742370],[4.925772,5.520790,-8.400062,7.784656,6.916352,-3.763474,-1.250884,0.659294,1.337034,-0.716715,2.420264,-9.541992,2.588065,-5.299332],[-2.977421,8.063768,-4.035536,-5.228967,8.573374,8.160794,-0.927300,-2.577919,0.308259,-1.326649,-0.426354,6.917463,1.379717,-1.714662]]], dtype = "float32")#candidate|5208|(2, 13, 14)|const|float32
bop_5209 = relay.floor_mod(call_5203.astype('float32'), relay.reshape(const_5208.astype('float32'), relay.shape_of(call_5203))) # shape=(2, 13, 14)
bop_5212 = relay.floor_mod(call_5204.astype('float32'), relay.reshape(const_5208.astype('float32'), relay.shape_of(call_5204))) # shape=(2, 13, 14)
bop_5215 = relay.multiply(bop_5209.astype('int32'), relay.reshape(call_5203.astype('int32'), relay.shape_of(bop_5209))) # shape=(2, 13, 14)
bop_5218 = relay.multiply(bop_5212.astype('int32'), relay.reshape(call_5204.astype('int32'), relay.shape_of(bop_5212))) # shape=(2, 13, 14)
var_5224 = relay.var("var_5224", dtype = "float32", shape = (2, 13, 14))#candidate|5224|(2, 13, 14)|var|float32
bop_5225 = relay.bitwise_xor(const_5208.astype('uint64'), relay.reshape(var_5224.astype('uint64'), relay.shape_of(const_5208))) # shape=(2, 13, 14)
output = relay.Tuple([bop_5215,bop_5225,])
output2 = relay.Tuple([bop_5218,bop_5225,])
func_5236 = relay.Function([var_5224,], output)
mod['func_5236'] = func_5236
mod = relay.transform.InferType()(mod)
mutated_mod['func_5236'] = func_5236
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5237 = relay.var("var_5237", dtype = "float32", shape = (2, 13, 14))#candidate|5237|(2, 13, 14)|var|float32
func_5236_call = mutated_mod.get_global_var('func_5236')
call_5238 = func_5236_call(var_5237)
output = call_5238
func_5239 = relay.Function([var_5237], output)
mutated_mod['func_5239'] = func_5239
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5249 = relay.var("var_5249", dtype = "float32", shape = (2, 11, 3))#candidate|5249|(2, 11, 3)|var|float32
uop_5250 = relay.rsqrt(var_5249.astype('float32')) # shape=(2, 11, 3)
const_5255 = relay.const([[[3.517295,-8.593288,-4.583938],[3.907212,-2.727135,-2.460845],[-6.724753,-9.266474,3.244877],[-7.441103,6.159759,8.359140],[3.338165,4.996444,-3.818578],[7.479031,9.731920,-3.776037],[-3.605869,-6.883896,-6.333643],[4.020636,8.481407,-9.172642],[-2.474362,-4.986869,2.325429],[8.609347,7.242456,5.200436],[-9.117701,6.299159,-3.335500]],[[0.255068,-7.909877,2.044275],[-9.018657,8.548724,-6.935039],[-9.759838,-4.844346,9.558269],[0.501646,0.043273,0.040120],[-8.646011,9.890465,2.234891],[-3.716654,-3.807090,-3.016189],[5.037224,-1.376378,-5.305473],[-0.615638,-9.555150,-5.804583],[0.901589,-6.587254,-9.627707],[8.489739,4.595388,8.383925],[-6.255425,1.175353,-4.769195]]], dtype = "float32")#candidate|5255|(2, 11, 3)|const|float32
bop_5256 = relay.right_shift(var_5249.astype('uint64'), relay.reshape(const_5255.astype('uint64'), relay.shape_of(var_5249))) # shape=(2, 11, 3)
uop_5260 = relay.log10(uop_5250.astype('float64')) # shape=(2, 11, 3)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
const_5263 = relay.const([[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[False],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[False],[True],[True],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True]], dtype = "bool")#candidate|5263|(350, 1)|const|bool
call_5262 = relay.TupleGetItem(func_1152_call(relay.reshape(const_5263.astype('bool'), [5, 10, 7])), 0)
call_5264 = relay.TupleGetItem(func_1154_call(relay.reshape(const_5263.astype('bool'), [5, 10, 7])), 0)
uop_5270 = relay.tan(uop_5260.astype('float32')) # shape=(2, 11, 3)
uop_5284 = relay.sinh(uop_5260.astype('float64')) # shape=(2, 11, 3)
bop_5292 = relay.greater_equal(const_5255.astype('bool'), relay.reshape(uop_5250.astype('bool'), relay.shape_of(const_5255))) # shape=(2, 11, 3)
func_3253_call = mod.get_global_var('func_3253')
func_3261_call = mutated_mod.get_global_var('func_3261')
const_5310 = relay.const([[3,3,-9,-9,2,-8,4,10,4,3,1,-8,-4,-8,-6,8,-4,-7,2,5,-5,-10,-4,5,8,-10],[5,3,8,-10,-2,6,-9,-8,-10,-6,-7,-7,7,-1,-10,-3,2,-6,-1,-7,-5,8,7,-7,-10,-1],[7,8,-10,8,-1,-4,-1,3,7,5,-2,-7,1,-3,7,6,4,10,2,-5,-3,3,-1,7,6,-1],[-7,7,-4,-8,8,7,-7,-7,4,-3,-5,2,5,-8,-1,9,-9,5,9,-4,-7,-9,5,5,-2,-8],[-7,4,10,-2,1,9,10,-3,5,-5,8,9,2,7,-4,-10,7,-4,-6,-8,-10,8,8,8,-1,-6],[-5,-4,-10,-10,8,-5,3,-10,6,7,2,5,-9,5,-5,10,-7,8,5,-10,-7,-6,6,1,-5,-7],[4,-8,6,2,6,1,6,1,-7,-4,7,9,7,5,-8,10,-6,-4,4,2,-10,3,4,5,4,10],[-1,-5,6,-2,-2,-6,-1,-1,-10,4,9,4,-3,7,-10,9,3,-2,3,5,6,-6,-4,3,1,4],[7,3,6,-7,4,-10,1,-6,-3,2,2,6,6,-2,7,4,3,-3,-5,7,-6,8,10,2,7,-5],[-3,-7,-2,-5,-6,-4,6,7,-8,5,-5,3,-7,9,10,-2,-4,-3,9,-7,7,-3,-9,-6,-9,2],[2,-9,2,-2,1,7,-5,4,-6,-1,2,-6,4,-7,3,-7,7,-5,-6,-3,-4,-4,1,-3,9,-2],[7,2,-1,6,-10,-10,-1,-8,-3,5,3,6,-7,3,-4,9,-2,-5,-1,7,-6,-10,2,-5,9,4],[-9,-6,-1,6,-5,-9,5,-9,4,8,5,-10,-6,-3,7,8,8,-4,-6,-6,-5,-5,-6,-9,-2,-4],[-6,5,-3,8,-6,6,4,-4,-10,9,-3,8,-3,-4,3,-4,-4,1,-7,-7,-9,8,-3,-4,-3,10],[1,7,-4,-1,-1,-8,-3,-2,9,-5,2,-2,6,-10,10,6,8,5,6,-1,-2,4,9,10,-7,6],[6,6,3,2,-8,5,2,9,10,7,-8,-9,-8,5,-4,7,-9,4,9,-7,4,2,-6,8,-1,-7],[-9,-8,-7,-4,-5,3,-4,-8,-4,-1,-7,-8,5,8,-2,-9,-5,-8,1,5,3,-10,8,-3,2,-3],[-8,-3,-7,-1,10,-10,6,-9,-1,4,6,-2,-3,7,10,6,10,-1,2,8,3,-9,5,7,-6,-10],[7,7,9,-5,3,-7,3,-10,1,9,5,2,-7,7,-1,6,-3,8,-6,-10,-8,-1,-6,-8,-10,-10],[6,-6,2,6,2,-1,-6,6,-6,2,3,5,-8,-6,-1,-5,8,-9,7,-6,-9,6,8,7,8,7],[7,-3,-6,-3,-7,3,-10,-8,8,-5,-10,2,3,-3,-1,6,-4,-2,2,-7,-2,6,1,-8,-7,5],[6,-7,-7,3,1,-7,-2,5,-4,3,-1,9,-3,2,-4,1,-6,-10,-9,2,-4,-4,8,10,-2,-10],[-2,-8,10,6,8,-3,-6,-7,9,6,8,2,9,-2,3,-5,-2,1,-4,-5,6,7,2,8,3,7],[-4,-9,-8,-6,-2,-9,6,6,7,-2,-9,5,-3,5,9,-7,-10,7,-9,3,6,8,2,-3,7,-1],[6,-10,-3,5,8,2,-10,9,2,3,-4,3,6,4,-5,10,3,2,-8,7,-1,-5,7,-4,-4,10],[-9,3,-1,9,-3,7,10,1,8,-3,6,4,1,-6,-5,4,-9,9,5,-6,-8,4,4,-5,3,5],[-7,-7,-9,3,7,-9,-4,8,6,-8,7,-2,7,-7,-7,-2,-3,3,1,-5,-3,7,-1,-9,-7,3],[6,8,5,6,8,-6,-6,-1,5,5,10,-7,7,2,-10,-9,-10,-10,2,7,-3,-1,4,-7,-9,8],[4,-2,1,4,-9,-10,10,4,-7,2,-5,-10,-4,-9,9,4,-3,4,-2,-7,-1,-10,6,-1,-6,-2],[5,-2,-1,3,8,-3,8,7,6,-3,-9,-6,-8,8,1,6,4,-4,-1,-4,8,10,-5,-8,-10,-7],[-5,-6,3,10,7,-9,-6,-5,4,3,-9,8,3,4,-8,-4,8,-9,-3,-5,4,1,-9,-6,10,-2],[6,2,9,-1,-8,1,5,7,8,-10,5,2,-2,6,-8,10,10,3,7,-6,1,3,7,5,1,10],[9,-2,10,4,6,-4,-5,6,1,8,-1,-7,2,-6,9,1,-7,10,2,-7,-5,5,-8,-3,4,10],[-2,-6,8,9,9,5,6,-5,-9,-5,3,-6,2,9,-1,-3,-5,9,-4,-3,10,-1,5,-3,8,1],[-9,-2,6,-8,10,10,-2,-1,7,1,5,-4,-6,7,8,-5,6,-9,-7,-9,-10,-4,-8,-1,10,6],[2,8,-8,1,-4,2,-4,-4,10,9,2,2,-10,-7,-3,-8,3,-2,-2,9,-1,-7,4,7,-5,-3],[2,7,8,-2,8,-5,-7,-6,-4,-6,5,-10,-5,2,5,-8,-1,-9,-2,-10,-5,3,-4,1,-3,-2],[10,-9,9,8,-7,3,1,6,4,-4,-3,-1,6,-6,8,-7,-10,-5,8,-4,-10,-4,10,-4,10,-3],[5,-1,-3,9,-4,2,-5,-4,-10,1,-9,1,-8,4,-3,10,-1,8,-9,7,-7,9,6,8,-6,-8],[-5,4,5,9,5,5,-2,9,-4,-7,3,-5,-3,-7,-2,-4,3,10,6,-6,-1,-4,-4,6,-9,-8],[-1,3,8,1,-4,-8,-4,7,-8,-10,3,-1,7,6,-10,-10,9,-3,3,8,-2,8,-7,-6,7,-5],[10,-9,5,4,-2,-6,-8,-10,6,10,-6,-4,3,-9,7,-3,2,-5,9,-2,-6,4,1,6,-3,5],[-7,4,10,2,-9,-6,9,8,3,-9,-2,2,6,-9,6,-10,-5,-3,-10,-2,-2,-2,10,-8,-1,3],[-9,-5,4,-6,9,1,2,9,-3,-3,-9,-5,-4,-3,2,-8,-2,-8,8,5,9,3,4,-7,3,1],[6,1,2,7,-2,5,-10,8,-6,-7,-1,-8,2,-1,5,5,9,-1,1,-5,3,-7,-10,2,10,-10],[-2,7,4,-7,9,10,1,10,-1,7,2,8,-10,7,2,2,-8,5,6,-2,-7,4,-8,-10,-9,5],[-10,7,-3,-2,4,8,5,-5,-9,-6,1,-4,4,8,-10,9,5,-10,10,5,7,5,9,1,-7,6],[-6,-7,-4,-6,-5,2,10,-8,5,-4,9,4,-1,7,1,6,-4,10,5,2,-10,9,8,2,-3,6],[6,-9,5,5,-7,-5,-1,1,-10,7,7,2,5,9,-10,7,4,-3,2,-5,8,-2,-5,-8,-3,-5],[-10,6,-2,-5,-9,-6,-8,2,-8,1,-8,-6,5,8,-8,-10,3,-6,-10,-5,3,4,2,-3,4,8],[-6,-7,-10,-9,-1,7,-5,-6,5,-6,5,-10,-5,-9,7,-4,-6,4,-7,4,-1,1,5,-1,-1,7],[-6,-2,1,9,-1,-3,-4,-2,-9,9,7,-8,-9,3,7,-3,8,-3,9,1,6,8,10,-3,6,2],[3,-6,-10,-10,8,9,9,6,-3,9,-10,9,6,-10,-3,-4,2,-9,-8,9,-2,-1,-10,10,-4,5],[7,6,8,-6,8,-7,1,-5,3,-2,-4,-8,9,-2,-9,9,-2,9,-10,-1,4,-1,4,-3,-1,3],[-7,-4,1,9,4,5,-10,-6,-1,1,4,2,9,4,10,7,-8,-4,-8,10,1,-10,2,-3,2,10],[-5,4,8,4,-7,5,-4,6,-2,-4,4,5,-9,-10,-2,8,3,-3,-2,-8,8,6,-4,3,-1,-8]], dtype = "uint16")#candidate|5310|(56, 26)|const|uint16
const_5311 = relay.const([-0.562025,-1.531891,5.563459,1.838289,6.039238,-8.821224,1.118551,6.158263,-2.928451,4.839489,-6.659698,1.411969,-9.470790,8.469673,6.464005,-5.736237,-9.883750,5.765450,6.579432,-7.639265,-2.305009,-2.851292,0.725136,8.133439,-4.478242,-1.540128,-2.972857,1.353527,-1.527010,-8.282456,-0.339347,6.804728,7.335697,4.750379,-7.070907,-4.852316,-2.677971,-4.179391,-6.692334,-5.240731,-1.046984,1.513995,-1.774951,-1.479599,-8.295672,-3.895517,1.004517,8.282953,-3.825414,3.641657,2.650871,-7.672495,0.254351,9.489623,-1.703138,-0.735918,-9.523622,2.252718,7.477822,9.503325,0.737174,-0.173162,-7.545148,6.264957,-0.105739,5.287291,-7.853105,-3.059776,-5.311929,-6.443254,7.354768,5.417674,-0.382942,-3.759740,-9.231194,2.266213,-6.664749,-7.608874], dtype = "float64")#candidate|5311|(78,)|const|float64
var_5312 = relay.var("var_5312", dtype = "float64", shape = (1568,))#candidate|5312|(1568,)|var|float64
const_5313 = relay.const([6,4,6,-4,-10,10,2,-1,-10,-5,-8,-6,1,-1,9,3,-7,1,-4,4,1,9,6,8,-8,-1,-9,5,2,-4], dtype = "uint32")#candidate|5313|(30,)|const|uint32
call_5309 = relay.TupleGetItem(func_3253_call(relay.reshape(const_5310.astype('uint16'), [8, 14, 13]), relay.reshape(const_5310.astype('uint16'), [8, 14, 13]), relay.reshape(const_5311.astype('float64'), [78,]), relay.reshape(var_5312.astype('float64'), [1568,]), relay.reshape(const_5313.astype('uint32'), [30,]), relay.reshape(var_5312.astype('float64'), [1568,]), ), 1)
call_5314 = relay.TupleGetItem(func_3261_call(relay.reshape(const_5310.astype('uint16'), [8, 14, 13]), relay.reshape(const_5310.astype('uint16'), [8, 14, 13]), relay.reshape(const_5311.astype('float64'), [78,]), relay.reshape(var_5312.astype('float64'), [1568,]), relay.reshape(const_5313.astype('uint32'), [30,]), relay.reshape(var_5312.astype('float64'), [1568,]), ), 1)
func_1975_call = mod.get_global_var('func_1975')
func_1979_call = mutated_mod.get_global_var('func_1979')
const_5320 = relay.const([1,9,-8,3,-1,1,2,9,-3,-10,-10,-3,-4,3,1,8,-10,9,-7,-9,7,-10,-6,-3,-3,9,3,10,1,5,9,-6,-10,6,7,-8,9,-5,6,-4,-3,2,-5,5,-8,-7,-4,6,8,-1,-1,-1,-4,5,-6,-9,-2,-7,3,-10,-4,10,2,2,-1,-6,2,3,8,8,-5,-5,9,-3,-5,5,-1,-9,-2,4,-4,6,-10,3,-6,-3,7,-9,1,-9,4,8,-1,-10,-10,8,7,-1,4,-6,-3,1,-7,6,-10,-6,1,4,3,-8,-10,-8,-2,-3,-10,-7,6,-5,-6,-2,-8,-5,-2,-4,4,-7,-10,-1,-3,1,3,-8,-3,3,4,10,-2,2,5,-1], dtype = "uint64")#candidate|5320|(140,)|const|uint64
const_5321 = relay.const([9,-6,7,4,-3,9,-4,-5,5,5,-4,10,-8,-1,5,2,3,-8,7,-2,-2,2,-4,-1,9,-7,-9,-4,-4,-5,3,4,5,-8,-3,-3,-3,-10,-3,6,-9,7,-1,-6,6,-5,-9,8,-2,-6,-9,1,5,-7,-4,-2,-7,2,-2,5,2,-10,1,-4,-4,-10,-1,-3,4,-5,-4,-1,6,8,-2,7,-3,4,2,-8,2,9,1,-10,-1,-3,-1,-5,8,6,-4,-3,-7,10,-8,-8,-8,-4,9,4,-8,-9,1,-8,5,8,-7,8,-9,5,-9,-8,2,-6,3,-4,-8,1,-5,8,-3,1,7,-3,-8,-6,3,-3,-5,7,10,-10,-4,-10,2,-1,2,2,-3,-10,5,-9,-9,3,-3,3,-2,4,5,-5,9,1,-7,-3,-10,-1,-8,-3,-3,2,-7,-9,-9,2,-6,1,2,9,7,-2,-6,3,-5,2,3,4,-10,-8,8,2,-9,-1,9,2,1,-4,-9,10,5,2,7,-7,-2,5,7,4,-4,-6,-5,10,2,-3,-3,5,-7,4,-4,1,8,-6,5,8,6,-4,-4,-9,6,-9,6,-7,-2,7,3,-4,3,-5,-1,-10,9,-10,-6,-9,-10,5,2,-9,2,10,3,6,5,6,6,-5,-2,8,-3,-4,3,8,-9,10,10,-9,-6,-1,-8,-9,5,-9,-10,-8,-4,-3,-2,-4,8,4,-6,1,10,4,-8,-4,6,3,10,8,-4,3,-2,8,-1,-7,9,-8,1,9,-5,-4,6,-7,-1,-4,-8,10,2,-1,4,9,-6,-2,-8,-8,-4,6,-2,-10,-9,-5,-1,-6,-6,-5,5,-4,2,-9,9,-5,-10,4,-3,-2,-1,9,5,-5,2,-3,-6,9,-5,8,6,8,4,5,-8,-2,-7,1,8,-2,7,-9,-4,-1,-9,-4,4,-10,-4,8,3,3,2,-1,-1,3,8,-1,2,-1,2,-5,-7,-5,-9,5,2,3,5,4,-7,-3,1,-7,-7,6,-6,-8,-6,-4,-7,-9,8,-4,-6,-8,-7,9,-7,3,-7,-5,-9,-5,-7,2,-7,-4,-6,7,-7,6,6,-2,-2,-4,3,3,2,7,-7,3,3,-9,6,-1,-9,-6,2,5,-2,-4,-10,-7,7,4,-6,-7,6,7,2,-4,-5,-5,8,-1,-2,-7,4,-9,-9,-4,-1,3,-7,-7,8,-9,2,2,-7,-2,9,-3,3,-3,-4,7,-6,-3,3,-3,1,-6,9,3,-2,-4,6,4,-1,4,-2,3,3,2,-7,-7,-8,-1,2,10,3,-4,5,-8,3,-4,-5,6,4,-4,-4,9,-3,-6,8,-8,3,-10,10,-7,-2,-1,-9,-4,4,7,-8,-9,-9,-7,-4,-8,9,-7,7,-5,6,-5,2,1,-7,5,5,8,10,2,10,-2,9,-9,3,5,-9,-6,4,-8,-4,-6,-6,2,10,3,6,-1,7,1,-6,-9,1,-6,3,-5,7,-5,-8,3,2,9,1,3,2,8,-4,-2,4,-1,-4,-3,2,7,4,-9,6,-2,-8,3,-1,-7,-9,2,-9,-10,1,-5,9,2,-10,8,7,-2,-9,6,-7,-6,1,10,3,2,-3,-5,-7,-6,8,-4,7,1,-1,7,1,4,3,2,6,-10,-1,1,-3,-8,4,5,7,7,-4,-8,8,-7,-8,7,-4,-2,1,4,2,-5,5,-8,-6,4,9,-5,6,8,-2,9,-1,1,-4,-5,7,3,-10,6,-5,-9,2,1,-7,-3,3,3,3,-5,-6,-5,2,7,-8,1,-3,8,-4,5,-8,-8,-4,-5,4,-6,-10,-5,9,-6,9,10,8,9,-7,-1,7,-7,2,-8,10,7,4,-6,-8,-2,2,10,2,-9,-6,-5,4,1,-2,10,-4,-5,3,-3,-4,7,-1,-3,6,1,6,4,5,-6,6,-10,5,9,5,-8,-9,4,-3,2,-10,-1,8,-6,1,-2,8,-7,7,10,8,-10,4,-8,10,-6,2,7,-3,4,5,-10,8,-5,-3,-7,-6,9,-1,-6,-8,3,10,-9,5,6,9,-2,-5,-2,-3,-1,-7,8,7,1,8,5,-6,-2,10,-8,8,-10,6,-1,-2,-7,-3,7,10,-7,-3,-10,-9,-9,-2,1,-6,3,2,2,-6,-3,5,9,9,8,10,-1,10,-9,-7,-4,-9,7,-1,-7,10,-6,-9,2,2,-10,-8,1,-10,-4,-9,10,-3,3,-7,-3,-10,4,3,-7,-8,7,-9,5,9,6,8,-9,-4,7,3,-10,8,-10,10,7,-6,3,5,5,-9,-5,7,-10,-6,-4,-8,10,8,6,-1,5,9,3,8,-9,8,-6,8,10,4,1,-8,-7,-4,2,5,-3,7,-10,5,-2,3,-10,3,-3,3,8,-8,8,9,5,9,-10,-5,9,-10,-3,-10,-4,-2,-1,-2,6,5,1,-6,-8,6,9,-8,1,1,3,-8,6,5,-7,-6,6,-9,-5,-5,9,-3,-5,9,1,2,3,10,-2,-7,-1,-5,6,3,-10,6,-2,-10,-10,-2,2,4,4,7,6,-6,-8,-3,7,-8,6,8,5,-4,-8,-5], dtype = "uint32")#candidate|5321|(975,)|const|uint32
call_5319 = relay.TupleGetItem(func_1975_call(relay.reshape(const_5320.astype('uint64'), [2, 7, 10]), relay.reshape(const_5320.astype('uint64'), [2, 7, 10]), relay.reshape(const_5321.astype('uint32'), [975,]), ), 3)
call_5322 = relay.TupleGetItem(func_1979_call(relay.reshape(const_5320.astype('uint64'), [2, 7, 10]), relay.reshape(const_5320.astype('uint64'), [2, 7, 10]), relay.reshape(const_5321.astype('uint32'), [975,]), ), 3)
output = relay.Tuple([bop_5256,call_5262,const_5263,uop_5270,uop_5284,bop_5292,call_5309,const_5310,const_5311,var_5312,const_5313,call_5319,const_5320,const_5321,])
output2 = relay.Tuple([bop_5256,call_5264,const_5263,uop_5270,uop_5284,bop_5292,call_5314,const_5310,const_5311,var_5312,const_5313,call_5322,const_5320,const_5321,])
func_5325 = relay.Function([var_5249,var_5312,], output)
mod['func_5325'] = func_5325
mod = relay.transform.InferType()(mod)
var_5326 = relay.var("var_5326", dtype = "float32", shape = (2, 11, 3))#candidate|5326|(2, 11, 3)|var|float32
var_5327 = relay.var("var_5327", dtype = "float64", shape = (1568,))#candidate|5327|(1568,)|var|float64
output = func_5325(var_5326,var_5327,)
func_5328 = relay.Function([var_5326,var_5327,], output)
mutated_mod['func_5328'] = func_5328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5136_call = mod.get_global_var('func_5136')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_5337 = func_5136_call()
call_5338 = func_5136_call()
func_4981_call = mod.get_global_var('func_4981')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_5339 = func_4981_call()
call_5340 = func_4981_call()
output = relay.Tuple([call_5337,call_5339,])
output2 = relay.Tuple([call_5338,call_5340,])
func_5343 = relay.Function([], output)
mod['func_5343'] = func_5343
mod = relay.transform.InferType()(mod)
mutated_mod['func_5343'] = func_5343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mutated_mod.get_global_var('func_5343')
call_5344 = func_5343_call()
output = call_5344
func_5345 = relay.Function([], output)
mutated_mod['func_5345'] = func_5345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
call_5389 = relay.TupleGetItem(func_5115_call(), 0)
call_5390 = relay.TupleGetItem(func_5117_call(), 0)
output = relay.Tuple([call_5389,])
output2 = relay.Tuple([call_5390,])
func_5430 = relay.Function([], output)
mod['func_5430'] = func_5430
mod = relay.transform.InferType()(mod)
output = func_5430()
func_5431 = relay.Function([], output)
mutated_mod['func_5431'] = func_5431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5430_call = mod.get_global_var('func_5430')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_5443 = relay.TupleGetItem(func_5430_call(), 0)
call_5444 = relay.TupleGetItem(func_5431_call(), 0)
output = call_5443
output2 = call_5444
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
func_5430_call = mod.get_global_var('func_5430')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_5456 = relay.TupleGetItem(func_5430_call(), 0)
call_5457 = relay.TupleGetItem(func_5431_call(), 0)
func_1703_call = mod.get_global_var('func_1703')
func_1706_call = mutated_mod.get_global_var('func_1706')
var_5462 = relay.var("var_5462", dtype = "float32", shape = (440, 1))#candidate|5462|(440, 1)|var|float32
call_5461 = relay.TupleGetItem(func_1703_call(relay.reshape(var_5462.astype('float32'), [5, 11, 8]), relay.reshape(var_5462.astype('float32'), [5, 11, 8]), ), 0)
call_5463 = relay.TupleGetItem(func_1706_call(relay.reshape(var_5462.astype('float32'), [5, 11, 8]), relay.reshape(var_5462.astype('float32'), [5, 11, 8]), ), 0)
func_5343_call = mod.get_global_var('func_5343')
func_5345_call = mutated_mod.get_global_var('func_5345')
call_5464 = relay.TupleGetItem(func_5343_call(), 1)
call_5465 = relay.TupleGetItem(func_5345_call(), 1)
uop_5473 = relay.exp(var_5462.astype('float64')) # shape=(440, 1)
output = relay.Tuple([call_5456,call_5461,call_5464,uop_5473,])
output2 = relay.Tuple([call_5457,call_5463,call_5465,uop_5473,])
func_5475 = relay.Function([var_5462,], output)
mod['func_5475'] = func_5475
mod = relay.transform.InferType()(mod)
mutated_mod['func_5475'] = func_5475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5476 = relay.var("var_5476", dtype = "float32", shape = (440, 1))#candidate|5476|(440, 1)|var|float32
func_5475_call = mutated_mod.get_global_var('func_5475')
call_5477 = func_5475_call(var_5476)
output = call_5477
func_5478 = relay.Function([var_5476], output)
mutated_mod['func_5478'] = func_5478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4981_call = mod.get_global_var('func_4981')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_5577 = func_4981_call()
call_5578 = func_4981_call()
uop_5596 = relay.asin(call_5577.astype('float64')) # shape=(2, 13, 14)
uop_5598 = relay.asin(call_5578.astype('float64')) # shape=(2, 13, 14)
func_2400_call = mod.get_global_var('func_2400')
func_2403_call = mutated_mod.get_global_var('func_2403')
var_5606 = relay.var("var_5606", dtype = "uint32", shape = (324,))#candidate|5606|(324,)|var|uint32
call_5605 = relay.TupleGetItem(func_2400_call(relay.reshape(var_5606.astype('uint32'), [9, 12, 3]), relay.reshape(var_5606.astype('uint32'), [9, 12, 3]), ), 1)
call_5607 = relay.TupleGetItem(func_2403_call(relay.reshape(var_5606.astype('uint32'), [9, 12, 3]), relay.reshape(var_5606.astype('uint32'), [9, 12, 3]), ), 1)
func_81_call = mod.get_global_var('func_81')
func_84_call = mutated_mod.get_global_var('func_84')
var_5628 = relay.var("var_5628", dtype = "float32", shape = (135,))#candidate|5628|(135,)|var|float32
call_5627 = relay.TupleGetItem(func_81_call(relay.reshape(var_5628.astype('float32'), [15, 1, 9])), 0)
call_5629 = relay.TupleGetItem(func_84_call(relay.reshape(var_5628.astype('float32'), [15, 1, 9])), 0)
output = relay.Tuple([uop_5596,call_5605,var_5606,call_5627,var_5628,])
output2 = relay.Tuple([uop_5598,call_5607,var_5606,call_5629,var_5628,])
func_5651 = relay.Function([var_5606,var_5628,], output)
mod['func_5651'] = func_5651
mod = relay.transform.InferType()(mod)
mutated_mod['func_5651'] = func_5651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5651_call = mutated_mod.get_global_var('func_5651')
var_5653 = relay.var("var_5653", dtype = "uint32", shape = (324,))#candidate|5653|(324,)|var|uint32
var_5654 = relay.var("var_5654", dtype = "float32", shape = (135,))#candidate|5654|(135,)|var|float32
call_5652 = func_5651_call(var_5653,var_5654,)
output = call_5652
func_5655 = relay.Function([var_5653,var_5654,], output)
mutated_mod['func_5655'] = func_5655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5430_call = mod.get_global_var('func_5430')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_5670 = relay.TupleGetItem(func_5430_call(), 0)
call_5671 = relay.TupleGetItem(func_5431_call(), 0)
output = call_5670
output2 = call_5671
func_5686 = relay.Function([], output)
mod['func_5686'] = func_5686
mod = relay.transform.InferType()(mod)
output = func_5686()
func_5687 = relay.Function([], output)
mutated_mod['func_5687'] = func_5687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
call_5731 = relay.TupleGetItem(func_5115_call(), 0)
call_5732 = relay.TupleGetItem(func_5117_call(), 0)
func_4383_call = mod.get_global_var('func_4383')
func_4386_call = mutated_mod.get_global_var('func_4386')
var_5736 = relay.var("var_5736", dtype = "bool", shape = (198,))#candidate|5736|(198,)|var|bool
call_5735 = func_4383_call(relay.reshape(var_5736.astype('bool'), [11, 3, 6]), relay.reshape(var_5736.astype('bool'), [11, 3, 6]), )
call_5737 = func_4383_call(relay.reshape(var_5736.astype('bool'), [11, 3, 6]), relay.reshape(var_5736.astype('bool'), [11, 3, 6]), )
output = relay.Tuple([call_5731,call_5735,var_5736,])
output2 = relay.Tuple([call_5732,call_5737,var_5736,])
func_5772 = relay.Function([var_5736,], output)
mod['func_5772'] = func_5772
mod = relay.transform.InferType()(mod)
mutated_mod['func_5772'] = func_5772
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5773 = relay.var("var_5773", dtype = "bool", shape = (198,))#candidate|5773|(198,)|var|bool
func_5772_call = mutated_mod.get_global_var('func_5772')
call_5774 = func_5772_call(var_5773)
output = call_5774
func_5775 = relay.Function([var_5773], output)
mutated_mod['func_5775'] = func_5775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_5787 = func_5448_call()
call_5788 = func_5448_call()
output = call_5787
output2 = call_5788
func_5792 = relay.Function([], output)
mod['func_5792'] = func_5792
mod = relay.transform.InferType()(mod)
output = func_5792()
func_5793 = relay.Function([], output)
mutated_mod['func_5793'] = func_5793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mod.get_global_var('func_5343')
func_5345_call = mutated_mod.get_global_var('func_5345')
call_5804 = relay.TupleGetItem(func_5343_call(), 0)
call_5805 = relay.TupleGetItem(func_5345_call(), 0)
output = call_5804
output2 = call_5805
func_5808 = relay.Function([], output)
mod['func_5808'] = func_5808
mod = relay.transform.InferType()(mod)
mutated_mod['func_5808'] = func_5808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5808_call = mutated_mod.get_global_var('func_5808')
call_5809 = func_5808_call()
output = call_5809
func_5810 = relay.Function([], output)
mutated_mod['func_5810'] = func_5810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mod.get_global_var('func_5343')
func_5345_call = mutated_mod.get_global_var('func_5345')
call_5814 = relay.TupleGetItem(func_5343_call(), 1)
call_5815 = relay.TupleGetItem(func_5345_call(), 1)
output = call_5814
output2 = call_5815
func_5816 = relay.Function([], output)
mod['func_5816'] = func_5816
mod = relay.transform.InferType()(mod)
output = func_5816()
func_5817 = relay.Function([], output)
mutated_mod['func_5817'] = func_5817
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5821 = relay.const([[[9.810816,5.541377,-2.890387,0.851315,1.120324,2.613511,-1.223102,-3.817489,1.801849,-7.675258,-5.800075,5.035263,-4.175196,2.857362],[4.964580,-9.708352,3.287561,6.484087,1.820387,-3.902810,-5.626341,8.826357,2.530449,-1.234492,3.694236,-8.464763,2.520995,6.888662],[7.522246,-3.540089,2.996980,3.930143,-3.855479,2.217199,2.848982,-3.176215,0.277853,1.902093,5.202863,2.205905,-5.613862,-5.948228],[9.920795,-0.955479,3.400357,4.070344,9.939797,5.905145,0.692265,-6.195282,-2.277574,0.961337,-0.117658,5.349472,-6.849362,-7.569757],[-7.565574,-5.286339,8.809552,-6.587054,5.422886,1.125443,-0.640755,2.805190,2.945424,8.922410,-4.101004,2.193494,4.602736,7.886437],[3.179712,-1.009561,-3.521553,1.610127,0.561247,-3.389319,2.508199,-3.018204,-9.387465,-7.388855,5.788821,-3.526068,-1.566619,-4.945915],[-3.078838,5.902760,-6.852911,8.874059,-5.246171,-9.708505,9.140195,-5.446899,-1.602406,-4.581496,-0.955097,4.131211,-2.117885,-9.344989],[9.004406,-2.003960,-1.606807,-1.194623,-7.341782,2.809274,-5.576037,-1.067153,2.651011,4.353213,9.905397,-0.311770,-9.694621,3.798802],[7.457864,9.156481,0.159726,-9.751845,6.411534,-2.322950,8.497042,-0.158602,0.587176,9.431707,4.141290,-4.314950,-0.580426,8.916055],[-2.610427,-3.730943,-5.455898,0.392614,5.795732,2.790738,-4.628228,-7.390965,1.783917,8.445643,-6.912922,0.399090,8.852451,-6.127795],[4.534615,-6.616603,9.837796,4.302319,-4.800849,4.154913,5.422627,-2.720348,-8.858948,4.461789,6.374994,-5.415384,2.000974,-3.396109],[5.813080,-2.923353,-4.734361,0.163668,8.424988,6.966027,0.493906,-5.264038,0.380594,-7.728088,7.278980,5.083826,-4.455721,-8.449590],[-3.798919,6.212103,-2.971780,-5.617468,-6.750186,-8.966137,-0.652775,-9.913370,-3.593398,-2.372658,1.111520,4.494513,-4.652536,-8.613614],[-7.099577,-8.997704,1.585572,-9.872502,-0.676176,-9.474259,-7.188711,-2.698787,-6.618509,-0.432006,9.525820,-7.732129,7.403690,-0.744412],[-7.069389,5.335832,2.710530,0.500042,9.522466,-8.234278,-3.474245,-5.353427,6.092091,-1.827745,5.468574,-4.084097,8.982179,-3.806134]],[[-3.620064,0.317340,0.044623,8.201466,-1.924767,0.377122,4.221949,2.899812,-8.527891,-6.187988,1.970793,9.135495,-9.230436,0.496927],[-3.657875,-8.345297,-1.110280,8.130007,-3.198979,7.709859,-3.424552,-0.898346,-9.545508,3.666066,-1.178877,9.435620,-9.052179,-4.942732],[-7.413012,6.803501,0.699944,-8.963930,2.664391,8.034401,-9.507439,-0.013058,9.958960,-9.109542,2.896692,-6.091866,-5.548844,1.470691],[-7.950383,2.871440,4.643517,0.260428,-5.980840,7.502131,-4.102071,-5.029496,3.990681,0.729947,2.627785,-4.974636,2.752855,-3.140756],[-4.328269,4.009477,-5.153128,-4.340348,0.261047,-9.819804,1.249455,9.578269,9.919143,-1.082617,-2.381378,4.243225,-8.979279,-2.664310],[4.441650,0.483396,-4.835461,-9.582566,9.828063,3.039785,4.238465,-8.123140,1.620827,-1.121494,6.108974,2.931338,-0.935440,-5.454085],[-4.713302,-5.657328,2.016707,-0.258604,-2.877746,-8.584060,7.632442,-5.882752,-8.353452,9.609481,-2.790181,-0.517811,-9.850710,-0.382257],[-2.970031,3.787145,5.849800,-0.294638,1.538912,0.502713,-5.631234,4.528289,8.117290,-6.487342,5.363069,2.093414,3.862414,8.962997],[0.533614,-7.292543,-8.467343,-6.223228,1.102010,7.009622,2.620956,1.259265,-3.374596,8.315165,-4.941337,8.610739,1.906507,-8.381280],[-1.843325,5.523669,1.206089,-0.872732,4.371630,5.377483,5.437464,-1.565817,9.251934,-6.062644,-1.338852,3.302389,3.468469,-0.404566],[3.845435,8.658593,2.561212,0.728757,-4.633595,-0.978006,3.690727,3.970583,-8.370465,7.491488,1.387702,-3.164635,-8.462924,-7.710881],[-2.880393,-7.525729,4.970527,-1.293652,-5.399874,4.862717,9.020727,5.761252,-7.203371,1.415631,-4.377212,-5.545387,8.503410,2.754912],[2.877536,6.401623,7.349714,6.480623,-4.481300,2.196689,-6.411885,3.948756,-4.293370,-1.856266,7.441687,-5.287079,-5.381427,6.339928],[8.375976,5.221488,1.854825,-4.763260,9.811330,2.034885,8.618281,-4.790252,-7.273689,2.135090,-8.366553,4.716095,-6.882825,6.783737],[-6.120284,-5.390340,-2.998626,-8.183225,-4.193772,-6.813729,1.700924,7.260288,-9.151713,-8.800572,-6.456489,4.596877,1.795706,-9.288895]],[[-8.429297,-0.346545,7.014292,-6.086498,3.967510,6.833201,-0.561079,3.799385,6.384159,-3.929339,-5.989705,-4.061420,9.343673,-7.811365],[-9.917536,-9.880387,-3.094628,-9.868565,3.520089,8.595708,9.324467,-0.240641,-3.142262,6.340921,6.896519,5.478196,-0.906491,-9.291910],[-1.749412,-0.206468,8.364201,5.790332,-0.306688,3.511354,7.281347,-4.012938,0.422092,-9.875695,-7.547197,-1.826144,0.946302,2.875062],[3.717209,4.569531,-3.920281,9.522721,-9.291069,-8.934907,-5.965713,-6.292131,-0.934166,-6.722558,-4.920887,-6.044553,3.276813,-6.793915],[-5.450730,-2.039059,6.758001,7.210124,-5.125511,7.948308,-9.280970,1.479174,-2.290549,-1.793896,-2.941925,-6.013034,3.202281,4.391435],[6.237797,5.163103,7.113322,-7.008127,-5.222609,4.549659,-9.668664,8.865705,-1.533689,6.614052,2.658980,1.869657,-2.872937,-6.421667],[-5.120222,-9.632561,6.903670,-9.215143,-5.119319,6.806269,-9.234268,4.555684,3.835919,4.960176,7.372585,-9.306409,-0.611297,-9.050659],[-3.562138,-7.890926,-0.902140,-2.628137,7.544299,-0.062397,4.690744,-3.279957,-6.067478,-7.160172,-5.947709,9.584152,-2.038585,-3.540360],[-6.413653,-9.532867,3.618834,8.891646,5.083897,4.812047,-0.799374,-7.641404,3.254624,-7.841963,-2.298653,-1.663918,-7.529105,-0.939717],[6.160118,-4.004436,9.999116,-0.244973,0.812562,-1.502662,-5.922781,3.129697,-0.531602,-7.522323,-2.051368,4.534956,-3.754425,-5.235888],[-4.496052,8.891565,7.850482,6.196855,-1.204725,-2.378471,0.247024,2.575836,-1.837171,9.555186,-9.266259,5.976337,-9.108631,-3.521149],[-6.878239,2.907015,1.413579,-3.107839,-6.878160,-4.340971,-6.000335,8.332547,1.528698,2.252586,3.835474,-8.030234,-2.980645,9.364741],[8.866386,3.469000,-5.022614,-1.860864,-4.975635,-9.804151,-0.160708,0.953147,2.237375,-2.788861,7.977905,1.327785,-5.302526,3.728380],[4.506486,3.419920,-8.013355,-5.684269,-1.304182,-8.582679,8.804496,5.411689,5.136294,-2.500811,0.820486,-7.452479,-1.057110,-5.542732],[1.427757,-8.212923,-5.129864,3.112617,-9.888182,0.502564,-4.970180,1.193710,-1.727273,2.999318,-9.276350,4.555714,3.093043,-3.882842]],[[7.601986,-3.074294,-4.743551,7.194707,7.092578,7.173666,-2.858219,-1.905318,2.860760,-5.531728,-2.470539,7.724734,-3.644975,1.053513],[-1.994417,4.923108,-5.824678,8.357321,-8.041996,5.409910,7.604542,-8.251259,8.792327,0.767885,-1.247761,-5.048004,7.647363,0.668092],[-9.473519,1.844107,2.132848,-5.631378,7.396942,-3.163550,-4.027185,7.926421,6.024062,8.942332,-8.902490,4.475641,5.995541,9.487373],[9.173515,-8.713248,4.648235,8.543869,-8.248386,-7.041931,5.761904,-4.015861,-1.167330,2.547494,8.569197,-7.995064,6.252778,-2.655277],[-2.633207,-5.250009,0.502199,2.485686,-9.317799,4.702654,4.245492,-0.494701,-8.077245,-6.148959,-9.239898,-3.169601,6.230649,4.906176],[-6.483667,7.991054,-8.640694,2.973456,-4.406528,-0.516099,0.411921,5.121322,-8.987447,0.205590,-9.227628,4.709540,9.903305,-0.129268],[3.611213,-9.253142,-9.172709,-2.062814,2.109748,-4.674933,-4.729199,-1.169455,-6.292427,-3.923042,-4.491297,3.680314,-1.793899,6.198701],[8.380013,-7.902606,-8.335578,-8.903820,-1.194207,6.361112,-3.784821,9.297821,-7.010664,-0.092395,2.825920,4.702721,-6.212309,1.737138],[-6.710506,3.579078,-2.686059,-1.030331,-3.625673,4.685286,6.227102,-4.430948,-2.003572,-2.171289,2.828971,6.606764,-3.436644,-1.015649],[-3.349907,8.679774,8.948968,-9.189176,-7.302238,-7.129276,3.198091,7.401899,-1.626200,8.879076,5.734239,5.698772,-3.316573,9.748510],[-1.242109,-6.464967,0.927124,8.366132,-4.769977,3.537770,-0.123091,0.676892,8.519543,-9.747533,-8.502897,2.596885,7.670301,-8.550083],[2.796646,-5.725028,-4.510778,-1.376645,-6.924146,-6.980626,7.354938,6.959431,1.696652,-8.216643,2.915172,-2.739182,-9.484091,9.308434],[-1.181077,3.504729,-1.657175,9.165677,-4.480824,-6.726025,9.863991,6.793892,-5.201339,-1.100044,2.343760,2.115571,7.171703,-5.767973],[3.080856,-1.821527,-1.818611,2.972595,7.776161,4.323810,7.176686,1.762232,-1.887000,9.882659,7.209088,-7.863191,-8.978480,-2.853093],[2.086542,1.264404,-5.340356,-7.394428,-2.693731,6.262175,4.059702,6.433554,9.337144,8.773585,-4.025279,-0.626202,9.058761,-6.983552]],[[-0.769656,3.817025,-3.101185,-7.422176,-9.136274,7.417260,8.753753,6.055363,2.940846,7.130777,7.590592,-6.702815,8.652137,6.026610],[5.303800,8.409100,-0.220903,5.031206,6.077379,-5.290736,-7.703480,-9.991381,-9.025328,-5.508777,0.288495,-8.747213,5.176335,-4.152552],[-3.049161,6.842003,0.615542,6.229894,4.792413,-5.688732,7.682116,9.097111,-8.440021,5.288928,3.656826,-6.635392,3.299066,7.368585],[9.892716,8.760124,9.520655,7.873793,7.828414,1.819599,8.012325,-0.565278,-2.848433,5.965730,8.748401,4.053205,-4.437959,5.340302],[4.434066,-7.609684,-4.245837,-1.666939,-9.180739,5.192546,-8.166495,3.084771,-3.094220,-6.295855,1.855525,-8.961637,-5.122865,8.093468],[7.240565,-4.039169,3.725428,-3.357031,5.732384,2.579378,-1.195678,2.475818,5.613093,7.998016,-8.947601,-4.674615,0.788897,9.217642],[3.032309,-9.990353,4.418267,9.769507,-6.779450,8.285913,-0.462322,6.727981,3.821295,0.906445,7.604154,-2.768921,2.072633,9.939488],[7.036598,-1.336976,8.330221,-9.166563,-1.822252,8.945485,9.345896,-2.258305,-1.373637,-0.659497,-8.991411,-6.017292,-4.345951,-8.956252],[-9.058552,-5.376411,-1.593980,-6.524466,-8.728426,-7.503618,-2.139330,5.606458,-3.957418,6.435495,3.897212,-3.732663,6.418549,-3.416297],[-9.346154,8.452760,-9.186056,-0.335957,9.459294,7.892338,4.770467,-4.358519,9.064603,2.595738,1.549364,-8.852813,2.805528,-6.028234],[-2.682228,-4.164753,9.418884,1.132967,-7.032731,-7.156160,-2.351124,4.745688,-5.351786,4.329379,5.910851,4.653480,0.516342,1.077270],[7.520792,9.866209,-1.573315,-5.941472,-4.867344,-9.806539,4.945834,-0.898745,-4.295764,-1.305365,9.885380,-6.538955,-3.797366,0.385799],[-9.000724,-7.045826,-1.028020,4.241941,-0.895867,0.440586,4.468507,4.850960,-1.811047,-3.095514,5.822795,2.280245,-2.156480,1.623975],[-0.644650,-9.926051,4.968140,-6.643283,-9.575754,1.044214,8.843720,7.783209,-1.554827,8.183023,-0.491700,1.524334,-2.485341,-0.967640],[-7.654878,-2.299909,-6.779980,7.796393,9.460310,-0.610102,8.574935,-6.887835,-6.726329,5.637514,-0.818932,3.494886,-4.812412,-7.989111]],[[-2.415786,7.906503,-8.028307,0.507435,-8.421405,2.527029,-4.474710,-5.616413,9.979323,-8.729130,-4.437156,-8.917801,-3.690220,-3.440393],[-8.822253,-4.042723,0.705174,6.182657,0.436620,5.214133,-8.961995,2.833901,-3.551408,-8.013305,7.927911,8.944752,5.421007,-6.647399],[9.613574,-7.982763,-2.690822,-9.449998,6.260805,9.535694,-3.914036,-3.599851,5.242470,2.315943,2.933547,1.008117,-9.677733,7.349880],[-3.618572,-1.103458,-7.865351,0.979394,5.684263,-3.544622,-8.027760,6.530812,-5.152407,3.357781,9.647793,6.086390,-3.875067,2.717873],[4.287740,-2.681810,3.938703,-9.988062,-6.961304,-4.352139,3.487636,-1.111532,-4.416732,0.191160,2.815336,4.429419,1.276381,-9.035055],[7.298354,5.747169,-4.904788,3.269135,-5.729978,4.878221,9.236387,-4.325462,-8.464504,-1.706564,-1.842269,-6.137512,-4.307997,-7.967675],[-2.893284,-1.845291,8.096024,6.866058,3.256687,8.480601,-2.106701,-1.908651,-9.801005,-9.682859,2.073257,9.786570,-8.693981,-6.775731],[5.012037,1.365543,4.451726,-7.445683,3.702524,-0.338538,-9.646500,-7.719231,-2.559113,-3.226435,3.508475,0.008310,-8.501778,-4.611576],[-0.808095,6.076445,3.964429,-8.836195,-6.739901,5.327965,-4.913012,6.918690,2.433156,0.468021,-2.544863,-3.592667,-0.949868,9.419681],[3.650100,-2.894823,-4.869118,9.511234,-6.524318,-1.212936,-6.160242,-7.546627,9.658307,4.909315,0.455843,-0.208004,7.370882,5.820203],[-6.522119,-6.875305,-4.868009,-3.217046,-4.462460,-2.913990,3.678131,-1.339816,6.985924,-3.106144,-4.004405,4.856327,-2.189344,9.201927],[0.603155,4.009386,3.544804,3.331888,-4.281819,-0.043240,0.445589,3.346925,7.200301,4.525786,-2.122942,1.275958,5.451634,-3.000102],[-1.125602,7.979403,-8.504598,-0.493736,-6.508268,6.097044,7.299636,-0.147857,1.999752,0.213723,6.965863,0.319051,-0.495854,-1.975477],[0.087122,7.783562,-9.902145,1.010482,3.585995,3.617859,0.810858,1.018996,-4.388878,-9.847491,0.849120,2.712726,-2.817795,4.739144],[7.875407,-1.634024,-7.875334,1.415227,3.793740,-0.348334,-1.918404,-6.331803,-1.837940,-1.602417,2.616574,-1.345159,-9.905402,9.451462]],[[-1.396683,6.531576,-9.660762,0.802193,5.731052,-9.664656,7.494261,5.199724,-8.497606,-6.451754,3.115357,8.920781,1.787826,-8.517323],[8.636015,-9.997286,-3.929461,-7.900423,7.045757,6.276209,-9.592945,8.424960,-7.940490,7.957228,3.643322,-4.252667,-3.900771,9.078243],[9.832786,4.821677,-6.799996,5.292135,5.589020,2.005151,2.978042,0.485568,-0.294052,1.712862,1.089942,5.607117,-3.158129,-9.157676],[-5.906252,-3.823720,6.896271,-9.967130,4.619480,-4.689872,0.344596,-3.655780,-8.670400,-9.697285,-1.247877,-4.174836,-3.650445,-9.440828],[6.929802,1.492771,7.602971,0.937968,3.475799,-0.519477,1.765342,0.610824,-0.837444,3.727467,8.316669,-1.111784,-9.878162,-9.410260],[-2.654863,7.723015,2.585758,3.959170,2.142307,5.257239,8.198104,9.528534,-4.866908,8.411235,-6.190610,4.743508,9.512618,-7.282384],[-9.495280,-8.185005,8.290928,-4.927079,4.202604,6.514389,7.606341,9.220975,-6.429176,7.684980,-8.372345,-3.740449,-0.899931,-0.863953],[9.953226,0.796117,9.391008,-0.055394,4.562293,2.776832,7.610354,0.281545,2.238613,0.020419,-7.714841,-6.211583,3.196516,3.332329],[3.916699,2.919142,-9.299011,-4.070268,5.212681,3.941388,-4.186338,8.372035,1.280389,-6.588056,4.241009,8.607976,-9.097777,-7.444290],[-5.615277,8.328315,-7.800372,-4.785370,3.119590,-1.745515,5.983356,-6.808799,8.024924,5.313743,-0.669907,0.412600,4.256966,2.653471],[7.523799,-1.938408,-6.360033,1.492297,-7.189958,3.023797,-4.950478,-0.351059,9.287982,0.035072,-0.691717,-0.349421,-9.214116,0.512370],[-2.591228,-0.541260,-8.720169,4.752925,-0.416130,5.530412,-0.277691,5.879542,2.496559,-3.799977,-8.183214,4.530420,8.261941,2.660690],[8.824323,5.767447,-2.310908,9.380195,-3.943306,8.382997,5.651671,-7.110991,8.406049,4.563749,7.513623,-5.423244,8.296945,5.215070],[6.237269,0.505912,9.828297,-8.181524,-1.256340,-1.334452,-5.861319,8.098593,7.759884,1.651310,3.525734,7.219866,-9.784849,-2.394820],[4.840757,-9.153663,4.021449,9.772498,0.660905,-5.813517,-7.211688,-7.044855,-6.763109,-3.797463,2.997066,-8.306849,-0.700802,-8.431216]]], dtype = "float32")#candidate|5821|(7, 15, 14)|const|float32
uop_5822 = relay.acos(const_5821.astype('float32')) # shape=(7, 15, 14)
output = uop_5822
output2 = uop_5822
func_5832 = relay.Function([], output)
mod['func_5832'] = func_5832
mod = relay.transform.InferType()(mod)
output = func_5832()
func_5833 = relay.Function([], output)
mutated_mod['func_5833'] = func_5833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5832_call = mod.get_global_var('func_5832')
func_5833_call = mutated_mod.get_global_var('func_5833')
call_5854 = func_5832_call()
call_5855 = func_5832_call()
output = call_5854
output2 = call_5855
func_5856 = relay.Function([], output)
mod['func_5856'] = func_5856
mod = relay.transform.InferType()(mod)
output = func_5856()
func_5857 = relay.Function([], output)
mutated_mod['func_5857'] = func_5857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5686_call = mod.get_global_var('func_5686')
func_5687_call = mutated_mod.get_global_var('func_5687')
call_5883 = func_5686_call()
call_5884 = func_5686_call()
output = relay.Tuple([call_5883,])
output2 = relay.Tuple([call_5884,])
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
var_5892 = relay.var("var_5892", dtype = "int8", shape = ())#candidate|5892|()|var|int8
var_5893 = relay.var("var_5893", dtype = "int8", shape = (3, 11, 9))#candidate|5893|(3, 11, 9)|var|int8
bop_5894 = relay.bitwise_or(var_5892.astype('int8'), var_5893.astype('int8')) # shape=(3, 11, 9)
output = bop_5894
output2 = bop_5894
func_5897 = relay.Function([var_5892,var_5893,], output)
mod['func_5897'] = func_5897
mod = relay.transform.InferType()(mod)
var_5898 = relay.var("var_5898", dtype = "int8", shape = ())#candidate|5898|()|var|int8
var_5899 = relay.var("var_5899", dtype = "int8", shape = (3, 11, 9))#candidate|5899|(3, 11, 9)|var|int8
output = func_5897(var_5898,var_5899,)
func_5900 = relay.Function([var_5898,var_5899,], output)
mutated_mod['func_5900'] = func_5900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mod.get_global_var('func_5343')
func_5345_call = mutated_mod.get_global_var('func_5345')
call_5936 = relay.TupleGetItem(func_5343_call(), 0)
call_5937 = relay.TupleGetItem(func_5345_call(), 0)
func_235_call = mod.get_global_var('func_235')
func_238_call = mutated_mod.get_global_var('func_238')
const_5956 = relay.const([6.850551,-4.372469,-1.796077,-5.565325,7.835307,-5.627483,9.968442,-9.106431,-9.484764,4.780223,9.188121,-4.065596,-9.025164,-7.176800,-3.217341,9.144446,-8.622321,-2.217471,1.778346,0.023205,7.278428,6.666386,-2.049271,-9.924578,7.029934,0.647968,5.261896,-3.047213,-9.602934,1.626224,0.077447,1.282290,3.612037,-9.289268,-2.035449,0.016719,3.393672,-6.980962,-5.619968,-4.199527,-1.088898,-8.936662,-8.778218,5.227785,-9.157948,4.737808,-8.352526,6.213576,-3.849692,-2.100848,8.759394,-9.096014,3.159527,2.422265,8.332579,3.001884,3.796521,-2.163055,3.521361,9.836491,-7.856678,2.779118,1.014785,-8.175394,-5.997924,-4.439363,7.232754,-0.646203,1.858463,-4.248079,-4.826229,-9.099639,-7.141553,2.031627,-1.130110,2.566225,8.586239,7.586118,2.683732,-0.781411,6.519942,7.225866,6.741396,0.788763,3.996990,-1.582282,7.507566,-7.226980,5.797173,3.139503,-6.864496,-8.298998,1.551284,-6.432227,-0.565665,-8.342925,9.431732,-6.500587,-0.396962,9.307030,9.664177,8.645728,-0.152689,-3.730899,7.479432,8.604856,-7.472525,8.703432,-8.565711,-2.782210,-1.124725,-5.122041,5.931633,-4.827891,-8.377646,1.570457,8.087859,-5.260379,-0.617702,3.732351,0.244030,1.670144,2.871560,6.105395,-2.094936,-7.647313,1.746932,-3.238279,8.465114,-4.516889,-5.667145,6.279398,-3.429491,7.508715,8.642901,-8.378878,-4.127861,-6.034257,-9.823323,7.906433,-8.202785,9.630716,-7.577281,-7.028957,-1.820722,9.478162,-1.755044,7.659734,-0.323673,-2.244492,7.004168,-8.372580,-2.701071,0.573910,0.555965,-4.218181,-2.422339,8.497549,2.254220,-0.554218,-7.430837,4.789728,0.539656,0.072102,3.529427,6.860240,-9.790890,-6.326645,-5.263649,4.414057,-2.522616,6.961279,1.533444,0.556889,-0.463472,-9.793027,5.826444,-6.359950,-1.191763,1.624614,2.364669,5.034380,-8.725887,-9.216368,6.228622,-7.463164,6.541166,6.604143,-3.826001,-7.407662,-7.512566,2.766116,-7.806194,-0.761055,9.643401,-8.703928,-9.497156,-9.478357,-3.126843,-8.837829,-0.719340,1.407972,-9.916712,-7.352947,-9.265975,-5.219244,-3.198584,-2.434106,1.078043,5.622882,-0.029849,9.223168,4.456206,-4.966001,-6.351444,-2.100068,8.476548,7.989880,-7.671326,3.371649,-2.841887,5.211749,8.182458,3.039609,3.425411,-3.717925,-8.589908,-2.445248,0.891044,0.525803,5.567993,2.221606,-1.225237,2.603514,-9.173260,2.374995,-9.424230,9.920423,-4.199289,-3.361194,-6.535390,-6.957847,-5.175205,-2.020245,2.516356,5.120599,2.638004,8.434360,4.144125,-4.036808,6.655865,-3.208795,6.012512,-0.218660,-1.548631,2.970717,1.651753,-7.048126,-7.885675,7.442418,-5.334555,7.528921,8.937732,6.183138,1.791482,9.174045,9.710836,-3.924521,5.278171,5.533129,9.784964,-2.028562,-0.997366,-0.376974,-9.920237,-1.969452,-1.362653,-5.213662,-4.363892,7.826215,-2.351535,5.998078,-3.217407,-5.306345,-2.312890,-8.376152,-5.070043,-8.520596,4.227215,0.176861,-9.579483,-9.733368,7.383653,2.811141,5.312593,5.280737,2.042660,6.495271,-8.136586,6.544745,0.697423,-5.729807,1.508442,-8.148179,4.385114,-1.766839,9.386808,5.038857,9.932537,6.148194,6.506446,-8.753051,3.343956,-9.662268,6.246462,-5.769014,0.097176,-0.677217,0.054959,2.806707,2.929702,-7.244799,4.909346,7.347256,-8.867969,2.184379,-6.733470,-1.019538,0.783051,1.643778,2.688796,-5.068063,7.793026,5.948455,7.370885,6.176554,-9.675312,-9.163423,1.857733,-9.849090,-2.547706,9.122813,-9.525716,-6.265627,4.786617,-0.313099,7.082390,7.190264,-1.605275,9.340507,-2.485943,-9.635346,-9.825537,-7.344806,-1.679835,-8.453059,-6.484018,0.989798,7.334360,-5.885488,-2.746469,4.837657,8.426429,-1.018108,3.355718,-7.908553,-5.615985,-8.535210,5.144993,6.337338,-6.879499,-1.696242,8.790841,7.374858,8.588244,5.215559,-2.704207,7.810934,-3.542926,3.189739,0.544028,6.750253,-1.852051,-0.560537,-4.856012,-0.366030,9.884733,2.145501,-2.041983,-3.030934,-8.417568,2.726646,-2.921820,1.471445,-2.396312,2.367650,-3.988411,-5.723037,-6.654604,-0.375895,-2.171252,0.631915,5.693337,-5.904631,2.787413,0.633329,4.266750,1.239324,2.802923,-1.506547,2.931020,3.728980,-2.803350,2.180988,-6.688094,9.252064,-1.240335,9.779839,2.804358,2.894017,-8.292875,-0.291347,-6.092612,5.708261,-1.994581,5.388866,2.320490,2.141715,-8.343653,8.334156,-8.663575,7.440103,5.286332,-5.151886,2.191085,-7.304453,-6.705311,0.376788,-4.876071,-7.119666,-5.634381,-8.875560,-4.113394,6.446195,-1.378946,-2.748743,6.087525,3.110844,-0.656103,8.230680,-4.370695,3.953152,-7.876903,3.652228,0.587382,-6.935206,0.667713,-9.809008,-6.493779,7.972236,-0.278587,-6.781258,8.329023,-8.694046,0.584177,3.926445,3.757321,6.107976,1.871035,-1.446067,-7.774671,-9.894057,-8.155951,-8.710820,-5.764662,8.271070,1.595770,-8.539333,-6.081895,-7.818823,-1.349360,9.692126,-2.492803,-1.831773,3.984125,-7.327887,7.724857,8.268293,0.746589,-9.618888,2.600318,-8.922867,5.680170,-9.884478,-6.767888,-1.076060,-8.184682,-9.158842,-0.548977,5.866760,-0.803223,3.794681,-6.375575,3.044573,-5.752671,-5.375939,4.643417,-2.676993,6.092041,-3.915905,1.361381,4.384641,-2.004411,-7.467225,-7.688679,-0.850725,-7.194424,-5.183917,6.769443,-0.426496,6.064535,2.906333,-1.601341,-7.472903,-3.701306,7.252077,6.241591,-2.875729,-2.955599,-5.433797,-7.961655,9.556425,-1.500829,7.873291,3.271022,-7.018868,-4.479225,-6.728391,5.419423,3.283461,6.325118,-6.685281,6.721243,9.942453,2.416457,-3.966482,-4.193285,-7.219979,4.351773,-4.702223,-5.582047,2.569729,6.867387,0.664220,-1.219435,-1.429707,8.533963,-0.154570,0.631291,-1.166298,5.607557,-1.708484,4.515560,3.854380,7.562287,5.914362,-6.515237,-5.102831,-9.144858,-7.618938,-2.021262,3.323285,5.985653,-6.569133,9.551204,-2.506684,1.283688,-6.209650,4.750806,4.964846,-3.562041,-7.778789,-9.318079,-3.908743,-1.223588,3.471921,2.157056,-9.921658,3.214566,-4.567771,-3.922254,5.415396,2.920421,-4.410124,1.273455,0.169483,-6.172434,-1.923922,7.088133,-2.076571,-9.308621,-4.548913,-7.897683,-2.439285,-2.802094,-7.129793,7.010166,-0.570386,0.094236,-9.039453,6.968223,-6.551577,9.440610,-6.220828,7.926556,4.472486,-5.193943,-6.683238,-9.925223,-6.373602,5.826098,6.215926,5.017162,1.171499,-1.437082,2.588411,-9.744601,-0.536868,0.736811,-0.503841,9.886568,-9.496019,6.928399,-6.863468,4.107823,-6.583877,3.987909,-9.343542,-5.282028,7.738819,4.741748,-2.002501,4.283217,3.101685,1.235689,7.231320,9.928866,-5.134101,-6.320249,1.677356,-2.220108,-8.476404,1.938646,-7.334872,9.360826,5.545911,-4.684802,-9.372923,-4.772574,-2.903332,9.972092,-4.565750,1.276769,5.876787,8.183219,-3.927782,8.720455,1.934365,2.924188,-4.368739,1.894700,4.099005,2.330718,4.360198,0.587559,4.562063,-3.585710,-9.391035,-7.344392,9.227723,-6.527060,4.767439,6.664346,-3.412523,-4.802723,7.573964,-4.290769,-2.698692,-6.854338,6.433136,1.997518,-6.597450,-9.007569,-6.141940,-8.229268,-4.151877,7.590193,-8.024359,-8.956159,8.912105,2.711765,4.986981,1.404171,6.877629,7.399931,7.023692,0.392435,-9.426456,-3.935165,9.890081,2.394069,9.549860,0.084347,3.327364,7.789165,5.845130,7.784700,-3.246956,-0.767284,-6.406784,9.119537,-3.890901,2.911541,-5.128159,1.200641,-5.952256,-7.166122,5.295115,-5.575077,6.522739,3.647682,-3.109357,9.455395,1.738638,7.522078,-6.901600,-6.214912,1.333208,0.182940,8.379776,2.663020,4.669219,-6.043152,-2.066592,4.003051,-7.703090,-8.466202,1.997783,1.693730,7.901021,-2.663652,7.499711,-4.670047,-8.056787,3.587782,3.625989,-6.237168,-3.057987,3.265644,9.804694,-7.360924,-8.264256,-5.477477,2.210193,-3.629128,-4.259511,-7.464828,1.066880,3.631672,-2.141397,-7.567116,3.241813,2.329548,2.016875,-9.654284,7.756219,-3.382651,0.727995,-6.814363,-3.355139,8.339139,3.018314,2.589193,6.642619,0.045481,4.371909,8.435919,-2.690048,-0.285134,4.288528,-8.509116,7.438398,-2.612225,4.354200,0.513686,-4.632429,1.068094,-1.958503,-2.651402,2.048112,-0.260985,6.576800,7.430308,-8.492401,8.901321,6.013826,-6.250001,-2.796512,4.176419,5.824075,-8.004336,-3.326383,-6.585184,-1.760983,-8.296234,-6.036244,-4.559992,-1.394778,4.067680,6.178416,-2.841120,-0.963417,5.253066,-4.971110,-0.221780,-5.239435,5.825866,-4.098330,2.155407,-2.880873,-7.452004,-2.765464,2.196375,7.810938,0.914002,4.299642,9.994226,0.096676,2.138255,3.359924,5.277999,-5.938845,-9.218578,-0.223263,3.777123,7.783425,7.229426,-9.063445,-0.775410,1.015328,-4.810570,-9.989293,-4.820080,-4.071369,0.169490,-8.314605,5.981972,9.710461,2.779574,-8.960963,-8.299946,1.528667,3.082222,-9.781605,5.654151,-3.721585,4.229013,6.841437,-7.705201,0.176998,7.533348,-8.532094,-3.908759,2.381690,-5.085535,-8.490836,4.167506,-7.250011,5.124883,9.892601,1.524153,-5.511426,-6.935573,-2.280284,8.143897,-8.338914,3.543567,-4.294894,-5.572011,-9.065577,0.081373,3.957539,-9.270240,7.415524,2.820093,-2.454735,-1.039632,9.614693,-4.259734,2.352936,1.578410,-9.866188,1.364490,-3.346971,-5.559459,-3.475839,1.040764,2.020965,0.583079,1.642088,1.314342,4.935668,-6.002516,-5.014303,7.620187,-6.412744,0.250951,9.164954,8.589872,-9.139419,-7.788483,3.275692,-6.039835,4.318396,-0.902422,-9.478764,-7.628797,0.846577,-8.715120,4.095450,-8.950965,-6.056964,2.431049,-1.686371,7.335681,-8.283563,4.826153,1.419580,-0.197779,6.561354,5.438293,-0.555352,-2.000616,-1.216880,1.166413,-5.804861,-8.415340,6.172267,-1.718165,-4.242034,-7.103714,-1.716633,3.614167,-0.773353,-2.653036,-0.455394,5.534731,-2.225996,-4.923082,5.804043,-8.484573,0.553705,-9.479145,-7.177358,-9.511267,1.476462,-9.822274,-5.706398,5.893166,6.867669,7.052179,-5.225502,1.457354,-8.354780,7.247346,6.589197,6.319783,-6.337504,-4.756240,-4.146158,-4.161416,2.581083,6.994979,-4.146046,-8.685934,4.409321,0.907332,3.999244,-7.917491,-0.647892,0.656128,6.473851,7.253773,-8.994741,2.768105,-7.300447,-0.437311,-5.240717,-3.484026,7.286686,-3.573318,-4.169095,-8.580205,-5.592028,0.269745,-2.766963,2.409983,6.973383,-8.832834,-0.480591,-6.678355,8.020406,-5.846220,6.104946,-3.356155,-9.078862,3.586954,-6.353679,-1.711136,-2.112870,7.606542,-1.731354,-3.724216,0.254970,1.193364,-0.310874,4.467388,3.228738,8.949317,-2.883345,4.703014,1.010708,0.413139,-6.265343,-6.362826,8.937774,1.156668,-9.868359,6.433462,-4.429945,4.818602,-8.457079,-1.734578,3.773930,-3.580910,1.287505,-9.596845,-5.822355,-2.385874,8.308959,1.675682,7.809667,-8.152750,2.477361,0.537221,-0.705741,-8.817684,0.862783,-9.164600,5.932754,-5.987296,-9.342340,6.636307,-1.665783,3.915986,-4.413656,-2.070524,-5.459204,-0.072866,-5.953613,7.729697,-9.139100,-0.802779,1.159048,-2.892752,1.882907,7.447293,0.578260,9.172363,4.158078,7.842641,7.591362,7.918469,-8.129491,5.408378,4.477671,-8.236559,7.001539,-2.152525,2.936746,0.800947,1.103275,3.731236,9.807867,1.015456,3.478565,-6.635157,-8.389707,-2.888593,7.085056,-7.288808,7.964560,5.880405,0.068675,3.496711,-5.832368,6.149777,2.305266,3.432172,0.933250,2.547174,9.957763,-5.686037,7.503700,1.328618,-8.114232,-9.479949,-7.783061,-9.650900,2.098807,-0.264906,-0.064170,0.707386,-1.564905,-3.906450,5.372870,2.364411,-3.768349,6.792218,-4.213656,-5.666404,-4.698972,-4.226807,-5.801915,-3.952790,-1.101434,-0.041715,-7.589088,8.122937,-1.894690,6.530790,6.738325,-5.970746,-8.610139,-3.038667,-0.153300,8.394934,4.525724,4.250160,3.125519,8.784958,2.729201,-1.288978,7.754203,-4.074167,-3.825518,-6.503090,-4.685458,3.913328,-6.365873,-4.782285,-8.535726,8.735463,5.156758,-5.585539,-8.689584,2.118361,3.802049,6.023962,1.386041,-9.387677,7.817761,3.422991,8.288449,-0.718988,-8.990924,6.157214,3.260870,-3.819550,0.172016,4.217234,-7.812124,3.670102,-3.160283,1.657393,7.012411,2.945375,-2.436772,-7.746430,7.051913,2.167203,9.704134,3.017500,9.330109,-7.551646,-6.414958,-5.720122,-5.137760,-5.690519,-1.806800,-7.975612,6.038447,7.721214,-6.028907,6.776796,-9.724563,-9.875610,0.458207,-4.704007,5.239999,-2.588164,-3.666978,9.700837,-9.499649,-6.360994,8.491439,-1.751042,-4.767018,-9.839104,-2.668179,5.938884,-9.354557,-4.044386,8.885318,-5.829642,9.296733,-7.696528,5.970722,-4.832584,9.917049,-1.462802,6.873538,4.373200,-3.342667,2.099521,8.877083,-4.208410,-6.767155,-9.601695,4.445605,-1.110730,6.556829,7.931250,-7.544172,-8.439889,-9.142994,-5.938519,-4.410604,4.655436,0.410801,6.084039,1.635958,-9.750354,-5.578394,7.872875,4.150948,2.643741,-0.094698,9.368299,-2.302067,-0.894815,7.996117,4.915241,-0.649975,-8.921046,4.506269,2.447213,3.558036,-5.852851,-7.939838,-4.694627,7.687060,-9.882149,-0.894031,0.098568,5.068311,8.472333,-5.053940,-2.169727,3.162855,5.981408,-7.570684,-2.030059,-6.004005,-3.656170,-1.028661,7.835456,-5.611004,-6.918787,2.615418,4.009937,8.378571,4.187484,7.363304,5.271965,9.059738,7.931004,7.526589,7.270702,-8.984018,-6.140835,-5.219561,8.274009,7.349844,2.432368,1.734405,6.370475,4.630626,-4.036928,8.467021,-9.878180,-8.893099,-1.913664,2.316690,-4.742784,6.158672,-4.991264,-9.114607,-9.012352,1.096352,-1.838345,1.039686,-7.674969,8.944686,3.467197,-5.073650,3.246255,-4.555228,-9.653069,3.264015,0.506190,9.289680,8.737703,5.323665,4.736852,3.123690,4.473312,2.228149,-7.300246,1.885979,4.831803,8.557067,-2.967704,3.001607,7.988326,0.812819,9.506961,-6.836681,-1.592359,2.696069,8.793688,-7.394079,7.587343,-8.468926,-5.009132,1.594883,8.409517,-8.320311,-3.416508,-1.994591,-4.303380,7.681434,-9.418579,-6.562618,6.959136,-1.692161,5.249544,-5.845874,-8.940511,-1.037333,-2.996955,1.193032,-9.364075,9.174041,6.078019,-4.023661,-0.329741,8.416879,3.168019,8.697497,0.824101,8.662002,-5.065139,8.110598,-5.130511,9.833435,-7.024766,-7.658529,-5.014003,8.072847,3.673947,-7.002006,9.963303,-2.890152,7.849583,-8.572200,3.228634,5.823062,3.188836,6.878787,-7.040435,-2.451835,2.871797,3.098077,-5.164459,9.497808,-5.242724,8.728693,7.670758,2.984674,-7.184366,-2.584019,0.481136,2.190273,-6.451735,5.114397,-4.576606,0.552971,-0.231639,5.868806,-3.966967,9.952112,-4.111591,-0.666661,-7.264566,3.165678,1.774430,1.821371,3.019874,2.279225,0.486409,2.005232,-1.336140,9.835813,1.800209,-1.490747,0.641960,5.977369,-6.470778,9.976549,1.787409,9.580345,-3.384403,5.246572,-5.627204,-7.498125,4.162808,8.281155,-1.066099,1.478311,1.871323,4.391188,9.547666,0.187140,6.917328,-3.420233,2.153262,5.257518,-3.182992,9.723792,-6.631704,-7.077714,3.910089,1.788701,-4.079143,-9.256542,-1.410593,-3.432555,-6.108720,-2.979120,4.475075,-0.800271,-2.402390,-3.065170,-0.395566,4.792784,1.322723,8.224149,0.104544,5.753515,1.699306,-5.569515,6.581692,3.955656,-4.549119,4.353054,-1.553784,-1.461519,-3.490033,-4.761520,-3.669254,4.069172,3.462233,4.262144,5.114101,0.165482,-0.256985,5.302315,-3.829633,5.853819,-6.935797,-4.215132,-6.106249,8.365246,-7.795700,3.832546,-9.920057,-8.521310,1.670626,-7.971417,-7.738333,4.922129,0.703140,8.889257,9.280016,-7.096332,9.476173,0.300660,4.070871,-3.373974,-1.299566,2.693546,-7.147584,-2.671624,2.256727,9.024570,-3.384271,-3.803612,9.092533,-0.832709,-6.449452,-5.355677,8.301542,0.932264,-2.029565,-2.113083,5.638856,0.862507,-2.406052,-6.839708,0.406733,7.372537,-5.515617,1.129025,4.950789,9.451249,9.330369,-5.088323,2.059901,5.786202,2.314589,-9.284633,6.201711,4.065823,5.557513,4.115636,9.694227,2.924879,-8.258377,7.546318,-5.268256,3.086736,-7.467291,-4.250325,2.026713,2.792046,-9.270976,-2.996540,-0.764443,1.559603,4.522340,-1.551100,9.479835,-9.899926,-7.365740,-7.561859,-5.593454,-6.524534,3.260999,-5.865957,7.956596,0.005214,6.486003,2.699468,2.734678,-4.232786,-9.395677,1.331741,-9.748212,5.394893,8.984735,0.531009,-3.897294,-6.233556,-6.872159,-9.295291,2.135033,2.717892,2.382023,-0.463667,0.336582,6.693945,1.229868,-9.302912,0.084748,-2.713077,8.847665,-1.483266,-3.418090,4.943139,-6.528406,-2.429897,0.486616,-6.763793,-7.151225,-0.556711,6.214288,9.661651,-1.401065,-3.325641,-3.984365,2.060769,-0.815701,8.911140,-7.449694,-6.108219,-7.240155,-0.262627,-2.626565,2.824263,0.340711,8.339575,7.121282,5.663193,-7.669823,5.484447,9.019562,-3.524258,4.691080,-0.415904,-3.256556,-6.577070,7.945189,-7.072853,7.125717,-2.837443,2.642318,-6.610215,0.069069,3.275023,3.313762,-1.675226,0.578968,8.266586,-9.696199,-3.934555,-2.113243,6.502588,-9.081302,1.118655,4.168432,-9.101690,5.642539,-1.393785,4.739085,-2.738085,-4.073950,3.386561,8.618239,-0.666690,-0.897696,-4.387084,5.115146,-6.533793,-5.918199,-5.327082,8.390450,-7.857925,8.296729,1.954037,-4.856775,7.810313,-5.489296,-0.844788,1.576902,8.425771,-0.745605,-1.708605,-0.369655,1.753675,9.983621,-5.480190,-6.292585,1.926613,7.404713,-8.766845,7.004761,8.367550,-0.151616,7.070464,-1.133624,1.524907,2.083393,0.350522,-3.775732,-8.737733,-2.781445,8.602485,3.121910,-9.299051,5.608156,0.102602,-4.796543,3.259538,-2.594061,2.590170,5.006753,2.132650,-8.134196,-3.214436,2.706054,-5.690182,-7.926476,1.613632,5.811537,-5.189041,-4.416317,3.413150,-5.149266,-4.024273,3.456437,-0.525482,-4.126914,6.882696,-7.909215,-3.853711,-5.399232,8.122759,-7.322215,1.888222,-8.909049,-5.987897,6.628302,3.409267,-2.496455,-5.961380,8.785877,9.708557,9.928003,3.776008,-6.989493,9.461428,-1.830646,1.441356,0.158283,-7.723397,7.163763,2.155462,-1.996016,-0.936245,-5.837458,1.154257,0.971020,5.451000,9.250831,-0.719362,-6.078689,4.199609,-7.012256,2.421082,0.617017,1.563780,7.559684,6.186595,-5.591377,-1.386440,-6.454249,-6.228042,-4.414782,-3.237829,-2.433932,-7.737280,0.116024,-7.543118,-6.764977,1.981597,4.006419,-4.423707,0.988843,2.595336,-2.668689,-5.427225,5.937318,-8.232907,5.096379,2.157509,-0.992527,-5.815619,0.188611,6.315399,6.574160,4.868369,-2.789676,4.238901,6.730186,8.867265,-1.601933,2.725484,-3.332277,-2.208618,-4.737394,-4.846382,1.695662,-0.178856,9.066263,-4.227245,8.545752,9.200068,-0.013535,6.955572,4.578355,1.375429,3.479299,7.357877,-3.809187,8.267034,-2.490094,4.530706,-6.827796,-2.006568,-4.074157,-0.252406,4.948674,7.776026,-5.179331,0.504104,3.023889,-0.373958,4.706178,-5.515628,8.093150,7.714581,1.424311,8.573355,-1.213868,5.656630,-4.514729,-3.200690,-5.205125,2.485969,3.663964,-9.845547,8.980541,3.291090,7.574868,9.596364,4.307512,-8.113453,5.021985,-9.000508,0.363570,-4.227103,-2.987518,3.962135,-9.079834,1.460984,-3.128659,-8.343100,-7.677883,-8.443506,-7.721399,-0.066541,-9.508761,-1.854444,-9.808833,-8.719322,4.457359,-9.682919,0.669094,-6.529743,-9.447821,1.152271,0.168012,9.217281,0.985747,3.335510,6.182313,8.557945,-8.336266,2.522533,5.838224,7.479014,2.011811,-8.949540,8.347371,-4.258889,-6.356158,-3.331301,-6.677232,-6.998093,-2.884951,9.159641,3.546629,6.767928,-0.898237,6.355127,-7.792485,-5.833143,-9.385697,2.437407,2.807597,4.438582,7.053791,-2.438671,1.164572,-4.581025,-8.039159,7.103729,-1.869954,-8.893519,-4.334422,-4.794070,-6.249280,-0.980058,4.690470,-1.649980,8.012262,1.872378,-8.147122,-2.454043,-3.338165,0.517278,-7.610643,-2.223642,9.729977,-7.081109,-4.419764,5.913094,3.016173,4.868723,2.766914,-8.905400,-3.679253,0.764709,7.399504,-2.193555,-6.761479,-0.228209,0.660518,-4.262346,6.656282,-5.046586,4.240072,-1.977425,0.375249,-2.245886,-2.118366,7.970680,-0.895647,9.728435,5.886636,8.140014,6.849045,-5.958322,-0.574987,0.287124,3.015932,-1.653621,9.249339,-2.298064,-7.072392,4.406484,6.292999,0.139812,-4.486390,4.672780,0.978056,8.220040,-3.712681,8.591912,-6.107356,9.486924,-9.246908,4.312745,-8.595840,-2.280975,-0.511216,6.928879,-3.101318,6.935281,2.220665,-5.486979,7.176648,0.451681,-2.750681,-6.255855,-1.575345,-5.990028,8.017143,-0.895937,4.190359,5.951574,8.199186,9.109932,9.480501,-3.617014,3.836593,0.286969,-3.596377,0.815272,5.591319,-8.726725,6.603833,-2.435370,-9.222157,-8.817268,2.264488,2.644787,0.251638,2.497169,7.872900,4.883083,-4.921192,4.701191,-0.502513,0.644247,-1.773551,2.573128,9.098726,8.210379,-7.952032,4.030495,9.013852,-3.187059,-1.343739,1.347556,5.092118,-7.961007,-9.046956,2.488539,-9.782829,-1.792458,-8.820472,-7.426654,-5.250127,2.357107,-6.362540,-4.504318,9.549654,-0.945242,-9.949560,7.247004,-3.434966,-6.645907,9.872795,2.827504,-6.281754,-1.423356,9.828577,-0.123162,-5.404060,8.100722,1.168942,-1.475660,-4.610126,-9.097007,5.996201,0.155573,5.997538,-9.998657,5.461952,3.116871,5.130955,-9.835069,-2.904166,-3.600079,-4.567800,2.069784,-8.271115,-0.865722,-8.471891,0.756682,-9.827416,-0.005216,-4.849011,-9.586923,-3.457754,-3.847783,9.336233,4.701296,9.364808,4.873202,7.010533,4.151457,-4.375528,-1.715707,-3.979905,-1.621028,-4.767498,0.089450,8.619547,-5.085023,5.929643,-7.700888,5.754802,-6.345001,3.737650,-6.076228,7.484081,-3.537421,3.319924,-3.074607,3.054251,-2.482542,6.277005,-3.207578,0.208669,8.939820,6.046044,-4.169332,7.559934,-9.261600,-0.099787,3.521223,-8.490546,4.183515,-1.629368,-5.569157,3.707236,-1.497418,-9.473589,2.982998,7.365388,-9.924335,-8.542557,-0.342617,7.971943,0.582896,2.655579,1.452887,-6.535941,-3.391536,2.594474,-6.354252,2.659434,6.933123,-9.420737,-3.692535,2.475520,-0.810766,7.222669,5.451382,1.695757,-8.472014,3.208405,0.066090,-3.770554,5.303210,-5.468766,-4.783945], dtype = "float32")#candidate|5956|(2160,)|const|float32
var_5957 = relay.var("var_5957", dtype = "float32", shape = (135,))#candidate|5957|(135,)|var|float32
call_5955 = relay.TupleGetItem(func_235_call(relay.reshape(const_5956.astype('float32'), [15, 9, 16]), relay.reshape(var_5957.astype('float32'), [15, 9]), ), 3)
call_5958 = relay.TupleGetItem(func_238_call(relay.reshape(const_5956.astype('float32'), [15, 9, 16]), relay.reshape(var_5957.astype('float32'), [15, 9]), ), 3)
uop_5959 = relay.cosh(const_5956.astype('float32')) # shape=(2160,)
uop_5971 = relay.asin(uop_5959.astype('float64')) # shape=(2160,)
output = relay.Tuple([call_5936,call_5955,var_5957,uop_5971,])
output2 = relay.Tuple([call_5937,call_5958,var_5957,uop_5971,])
func_5973 = relay.Function([var_5957,], output)
mod['func_5973'] = func_5973
mod = relay.transform.InferType()(mod)
mutated_mod['func_5973'] = func_5973
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5974 = relay.var("var_5974", dtype = "float32", shape = (135,))#candidate|5974|(135,)|var|float32
func_5973_call = mutated_mod.get_global_var('func_5973')
call_5975 = func_5973_call(var_5974)
output = call_5975
func_5976 = relay.Function([var_5974], output)
mutated_mod['func_5976'] = func_5976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5686_call = mod.get_global_var('func_5686')
func_5687_call = mutated_mod.get_global_var('func_5687')
call_5995 = func_5686_call()
call_5996 = func_5686_call()
output = relay.Tuple([call_5995,])
output2 = relay.Tuple([call_5996,])
func_6013 = relay.Function([], output)
mod['func_6013'] = func_6013
mod = relay.transform.InferType()(mod)
mutated_mod['func_6013'] = func_6013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6013_call = mutated_mod.get_global_var('func_6013')
call_6014 = func_6013_call()
output = call_6014
func_6015 = relay.Function([], output)
mutated_mod['func_6015'] = func_6015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_6040 = func_5448_call()
call_6041 = func_5448_call()
func_4883_call = mod.get_global_var('func_4883')
func_4887_call = mutated_mod.get_global_var('func_4887')
const_6080 = relay.const([[3,1,-5,-2,9,7],[8,8,-2,3,10,-7],[2,-1,-8,-7,2,8],[2,-10,-2,10,-7,-7],[-3,-10,-2,-1,-7,-5],[1,7,-2,3,-4,3],[-4,-6,-1,9,3,1],[10,-8,-6,3,4,1],[4,-8,-8,4,5,-2],[1,2,-5,-9,-5,-4],[-1,6,-7,-1,-2,-9],[1,-4,-3,5,-2,-10],[-10,-3,-10,-5,4,-6],[10,-1,-6,5,-6,-6],[-7,-5,-9,-5,-7,-7],[-3,-6,6,7,-9,8],[-3,-5,-2,-9,3,8],[-2,5,1,-6,4,3],[-4,-8,3,10,-1,-4],[-5,3,-9,-4,-6,-10],[-2,-3,-10,8,9,9],[-2,-7,-4,-5,5,9],[-9,-7,-5,-3,-5,5],[5,9,9,-7,7,-3],[6,-9,6,-7,2,-1],[10,4,-2,-9,2,2],[-6,-2,4,3,3,-3],[2,7,3,-1,-4,8],[-5,3,-9,-9,-6,7],[6,4,-3,-10,6,-7],[5,-3,6,-5,2,-10],[-2,5,10,10,3,-3],[10,1,1,8,-7,-5],[4,-8,7,-9,-5,-9],[-8,10,2,10,-9,1],[-9,5,9,1,-9,2],[-6,-5,5,5,2,7],[-9,9,5,7,6,-2],[-2,-10,1,-7,3,8],[-5,-3,8,-4,-6,6],[-2,7,-5,-4,-1,7],[6,-1,-5,9,1,8],[4,10,-4,5,-9,5],[1,-10,4,6,-3,-1],[5,-8,-3,-8,10,-9],[4,2,6,7,9,-2],[7,4,-5,8,-6,6],[5,-6,-4,1,1,-1],[-3,6,8,-8,8,-6],[-9,-4,-1,2,-6,2],[5,10,-7,5,-1,-3],[-9,-5,2,-1,-8,-6],[7,6,8,5,-1,1],[6,-1,7,6,-6,-4],[-6,1,-1,-2,7,-2],[-6,-10,2,9,9,2],[6,3,-3,-10,3,-1],[-8,-3,-1,-10,1,-5],[3,-8,-6,10,10,-1],[4,2,-5,-2,-5,10],[9,4,1,-5,-5,-9],[-5,10,6,-10,7,8],[4,6,6,-7,5,-6],[-9,1,4,-5,-10,-6],[-8,-7,-6,-4,-4,2],[-6,6,8,-6,-5,-3],[8,9,10,-4,-10,3],[5,-6,10,2,7,-7],[-2,-2,-9,-5,2,5],[-7,-2,2,-3,-3,-10],[9,8,10,10,8,6],[-8,6,-4,2,2,10],[-9,2,4,-8,-2,10],[2,1,-4,9,9,-4],[6,6,-1,-1,9,-6],[-3,-9,-1,-6,-1,-4],[5,8,1,-9,-9,-7],[3,-3,-1,-7,-1,1],[5,4,-8,2,-6,-9],[4,5,5,4,-2,-10],[3,-9,-4,-6,-2,7],[-3,-5,-1,7,4,-7],[-6,7,-7,2,4,4],[-4,1,5,5,-8,8],[-5,-5,8,8,-2,-3],[1,8,-7,-7,7,6],[-7,1,-3,5,7,-7],[-3,-1,1,5,-9,9],[-7,6,6,7,5,9],[8,-6,-7,2,-9,4],[-6,1,-1,-1,9,-2],[9,8,-7,10,4,-2],[8,-8,6,-6,-2,8],[-1,2,6,5,-3,-9],[-2,8,6,7,-8,2],[1,-6,7,4,1,-8],[-10,-2,5,-3,-2,-7],[5,-4,-10,-6,-4,-4],[4,-7,-4,4,7,6],[1,3,4,-4,3,-1],[2,-6,10,7,7,-3],[-10,-4,-4,1,10,9],[-3,3,10,-10,3,-9],[5,-9,10,3,8,7],[8,7,1,1,10,-1],[-10,-3,9,6,-5,-6],[4,5,7,-5,-9,2],[-10,-5,9,-3,6,-1],[-5,1,-3,-7,6,-10],[3,7,-8,1,4,-2],[-1,-1,8,-6,-1,5],[3,3,-3,2,8,7],[10,8,5,6,-3,-6],[1,6,-6,7,10,-9],[-3,-8,-4,-9,-6,-8],[-6,-8,1,10,4,3],[-6,1,10,-8,3,-6],[-4,1,3,-10,4,-8],[1,-7,5,-7,2,-6],[8,-7,-1,-7,-9,4],[10,9,-1,8,-4,-9],[7,-7,-3,-1,-6,-3],[-1,-3,-1,-2,-2,-4],[5,-6,-9,7,10,2],[8,8,2,-4,-2,-3],[5,-3,-6,9,10,-2],[10,-2,-5,8,10,9],[7,-4,10,3,5,-10],[4,-2,-7,-1,6,-9],[-10,6,3,3,-9,-9],[6,-2,-10,4,6,-8],[2,9,-5,-1,-7,6],[-2,-2,-5,8,4,6],[6,8,6,2,5,8],[-4,-6,5,3,-10,6],[5,-1,-6,3,-5,-4],[6,10,9,-1,6,4],[-9,7,-1,7,1,-6],[-4,-10,9,1,10,-7],[9,4,7,-5,8,-8],[-8,-6,4,7,1,9],[1,-7,3,-2,4,-8],[-7,-7,-8,3,-9,-7],[10,-1,9,-3,9,-3],[-4,7,-2,-6,9,-3],[6,4,-4,-6,-3,7],[6,4,10,10,-2,-9],[-1,3,-8,-8,2,-10],[1,3,3,-7,10,6],[9,-3,2,-5,-6,-4],[7,-9,-4,-7,4,-10],[-10,8,10,-1,2,8],[-5,-9,-3,7,7,-9],[2,-5,-6,5,-3,9]], dtype = "int8")#candidate|6080|(154, 6)|const|int8
call_6079 = relay.TupleGetItem(func_4883_call(relay.reshape(const_6080.astype('int8'), [11, 14, 6]), relay.reshape(const_6080.astype('int8'), [11, 14, 6]), ), 0)
call_6081 = relay.TupleGetItem(func_4887_call(relay.reshape(const_6080.astype('int8'), [11, 14, 6]), relay.reshape(const_6080.astype('int8'), [11, 14, 6]), ), 0)
output = relay.Tuple([call_6040,call_6079,const_6080,])
output2 = relay.Tuple([call_6041,call_6081,const_6080,])
func_6083 = relay.Function([], output)
mod['func_6083'] = func_6083
mod = relay.transform.InferType()(mod)
output = func_6083()
func_6084 = relay.Function([], output)
mutated_mod['func_6084'] = func_6084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6150 = relay.var("var_6150", dtype = "float64", shape = (11, 11, 1))#candidate|6150|(11, 11, 1)|var|float64
var_6151 = relay.var("var_6151", dtype = "float64", shape = (11, 11, 14))#candidate|6151|(11, 11, 14)|var|float64
bop_6152 = relay.mod(var_6150.astype('float64'), var_6151.astype('float64')) # shape=(11, 11, 14)
output = relay.Tuple([bop_6152,])
output2 = relay.Tuple([bop_6152,])
func_6176 = relay.Function([var_6150,var_6151,], output)
mod['func_6176'] = func_6176
mod = relay.transform.InferType()(mod)
var_6177 = relay.var("var_6177", dtype = "float64", shape = (11, 11, 1))#candidate|6177|(11, 11, 1)|var|float64
var_6178 = relay.var("var_6178", dtype = "float64", shape = (11, 11, 14))#candidate|6178|(11, 11, 14)|var|float64
output = func_6176(var_6177,var_6178,)
func_6179 = relay.Function([var_6177,var_6178,], output)
mutated_mod['func_6179'] = func_6179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_6184 = func_5448_call()
call_6185 = func_5448_call()
output = relay.Tuple([call_6184,])
output2 = relay.Tuple([call_6185,])
func_6189 = relay.Function([], output)
mod['func_6189'] = func_6189
mod = relay.transform.InferType()(mod)
output = func_6189()
func_6190 = relay.Function([], output)
mutated_mod['func_6190'] = func_6190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5808_call = mod.get_global_var('func_5808')
func_5810_call = mutated_mod.get_global_var('func_5810')
call_6241 = func_5808_call()
call_6242 = func_5808_call()
var_6246 = relay.var("var_6246", dtype = "float32", shape = (2, 13, 14))#candidate|6246|(2, 13, 14)|var|float32
bop_6247 = relay.add(call_6241.astype('int64'), relay.reshape(var_6246.astype('int64'), relay.shape_of(call_6241))) # shape=(2, 13, 14)
bop_6250 = relay.add(call_6242.astype('int64'), relay.reshape(var_6246.astype('int64'), relay.shape_of(call_6242))) # shape=(2, 13, 14)
output = relay.Tuple([bop_6247,])
output2 = relay.Tuple([bop_6250,])
func_6255 = relay.Function([var_6246,], output)
mod['func_6255'] = func_6255
mod = relay.transform.InferType()(mod)
mutated_mod['func_6255'] = func_6255
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6256 = relay.var("var_6256", dtype = "float32", shape = (2, 13, 14))#candidate|6256|(2, 13, 14)|var|float32
func_6255_call = mutated_mod.get_global_var('func_6255')
call_6257 = func_6255_call(var_6256)
output = call_6257
func_6258 = relay.Function([var_6256], output)
mutated_mod['func_6258'] = func_6258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5856_call = mod.get_global_var('func_5856')
func_5857_call = mutated_mod.get_global_var('func_5857')
call_6266 = func_5856_call()
call_6267 = func_5856_call()
func_4981_call = mod.get_global_var('func_4981')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_6276 = func_4981_call()
call_6277 = func_4981_call()
const_6287 = relay.const([[[-1.099933,4.803878,2.249981,2.940154,-5.175256,-6.445142,-0.178892,0.795473,5.609845,-0.234557,3.512606,-6.870251,6.487114,4.034173],[-6.655286,5.615288,-9.555955,8.332271,-0.434373,3.484760,-3.252620,-9.662388,4.723463,1.843579,5.463265,9.605898,-7.607483,-6.570316],[-4.502125,3.265073,-8.925468,7.624266,0.197601,-5.388440,5.908676,-0.974257,-5.548868,-7.248504,-9.924854,-7.459418,3.680711,-7.699656],[0.803046,-5.783767,-3.006506,-2.265011,-5.176594,2.012280,1.062428,7.613460,-3.115388,-3.069291,5.794189,-7.720652,-8.257611,1.916786],[-1.216097,8.445329,-6.551952,0.322668,2.819210,4.958077,7.201927,1.527679,5.845669,3.426566,-9.217494,-7.809847,6.642308,-1.980726],[3.434031,5.142026,0.726019,9.663939,-5.484613,2.942505,-7.746512,2.284577,3.656696,-2.496875,-4.889540,-8.124104,3.057894,-7.618287],[-4.098960,-4.209088,-4.901712,6.147245,5.688003,3.617591,-5.034221,6.094546,8.064226,-1.325711,-2.518590,8.055694,9.498853,9.342321],[-2.878433,9.831471,-4.468260,-7.056605,8.043450,5.670671,-2.743062,8.859922,4.771576,-2.224966,6.037173,7.687152,2.091184,-9.707730],[6.371970,-5.868461,4.534475,-1.430215,0.189009,-4.512889,-3.771090,2.528050,-8.503654,1.944014,-4.394184,0.167026,0.075135,2.315997],[2.254659,0.495057,9.872045,3.199709,8.073010,6.653052,-9.846084,5.791340,3.742450,-0.618386,2.825079,6.271084,9.256187,-0.480545],[4.562695,7.968733,2.937867,8.899445,-0.676684,-4.069477,-4.146398,9.670596,5.226210,-6.657509,9.478787,1.905142,-0.932774,-1.330969],[3.237620,-0.649018,-1.294078,1.528651,-4.064513,5.721423,6.620176,-8.297158,3.635091,1.837741,1.065511,4.200837,-1.354497,0.806896],[9.656327,-9.187584,-6.585666,1.079317,-3.098725,6.534867,-0.909203,-4.834625,-6.715268,8.068614,-5.805506,-2.388295,-1.578658,-6.486888]],[[-5.109637,-2.285409,-7.275686,-5.765060,9.882860,4.034419,0.385529,1.816215,1.194905,7.838281,-4.784106,0.796089,7.124169,-4.739123],[2.294826,-0.731461,2.567377,4.500638,1.720258,-3.480390,-0.004847,1.017104,-7.890890,7.060597,-1.821498,4.505809,5.142398,7.128544],[0.045929,2.932598,-7.390800,-3.437553,-5.963979,8.243790,-0.013383,-4.476721,-1.901275,-1.260230,-3.345573,-7.753702,-8.209227,-1.125428],[1.592487,4.053680,9.240603,4.338603,-8.415856,7.784942,-1.678444,9.230961,8.308158,3.736838,3.226075,-3.754031,8.943840,-8.649858],[0.056717,8.513390,-5.844489,3.263848,3.783039,0.805810,-4.944441,-6.184533,-6.929597,9.260877,-3.663831,7.766796,-8.932136,3.989008],[-3.304205,-4.413706,-6.565713,-8.473265,-1.697424,4.846467,7.180960,0.035124,1.966958,-5.925414,4.632549,2.038063,-4.662704,6.383890],[7.131971,-6.595136,-6.821344,8.484711,-4.103464,6.601022,1.045593,7.136453,-3.914300,-0.393037,-7.588612,9.666577,7.993957,0.305837],[7.227090,-1.416621,-3.202354,-6.266240,5.554594,6.436352,-8.032174,-4.809503,5.063420,-1.700333,2.799894,-8.463727,3.948057,4.508327],[-7.953048,-6.145082,-2.294562,-3.684409,4.206534,4.707311,-1.074319,-7.435166,-0.097852,-1.664685,-1.245761,8.342597,-6.803309,-2.440821],[1.699366,-8.350116,-2.952592,8.892227,8.297909,5.908982,-7.522807,-4.044158,-8.152703,6.705009,9.590506,-9.793038,-2.747461,0.309200],[0.383189,-2.060438,-9.822365,6.040961,5.036925,9.774061,-0.396500,4.734729,0.804051,-5.727035,5.530654,-4.161771,7.935771,-8.029325],[-5.385340,-8.595551,5.226452,-0.359408,5.311434,6.286223,-8.599529,-9.230265,8.482568,-6.581824,6.451348,-7.970119,-7.441480,9.223934],[-6.832966,-6.758038,-1.893490,-8.040350,9.493033,3.705441,-2.460314,-6.889706,2.943914,-6.249901,-6.610672,7.407833,5.659077,-0.164519]]], dtype = "float64")#candidate|6287|(2, 13, 14)|const|float64
bop_6288 = relay.equal(call_6276.astype('bool'), relay.reshape(const_6287.astype('bool'), relay.shape_of(call_6276))) # shape=(2, 13, 14)
bop_6291 = relay.equal(call_6277.astype('bool'), relay.reshape(const_6287.astype('bool'), relay.shape_of(call_6277))) # shape=(2, 13, 14)
func_1521_call = mod.get_global_var('func_1521')
func_1525_call = mutated_mod.get_global_var('func_1525')
const_6296 = relay.const([3.388908,-6.083531,6.169120,3.393014,-3.333021,-3.506800,-2.060733,-3.763629,7.734736,-2.657994,-7.296018,6.550201,5.645729,-3.004720,-8.680675,-8.747293,-1.774497,-4.231840,-9.065965,4.160078,-7.046094,3.019002,6.503542,-1.107189,2.159519,7.398718,5.710186,0.431687,-4.942744,8.301744,9.834883,-4.733992,-2.366443,9.789894,-2.099769,0.168424,4.299334,-8.516441,-2.775328,5.060534,5.843157,-0.131345,-7.545208,6.607917,1.266090,1.690675,1.604095,-7.751057,-8.180231,-1.940803,-7.744827,4.622986,-4.398637,5.386858,-8.078436,8.011195], dtype = "float32")#candidate|6296|(56,)|const|float32
const_6297 = relay.const([6.352991,-9.898946,1.627438,2.933413,0.137095,5.947782,-1.485759,-0.861233,9.312498,-9.078708,8.808090,6.042612,-4.828969,8.757170,-5.019208,6.388966,-1.222986,-5.890727,9.886096,-7.870503,-9.422112,-8.654425,4.901624,7.497118,8.016731,-7.295534,8.947857,-5.164238,-9.889052,8.946979,-1.599100,-0.338518,-4.015193,9.249921,1.938988,-2.962328,6.997400,-1.192850,-5.701869,4.373044,6.790764,-8.854216,5.744072,-7.905330,9.465201,-6.679599,2.005049,-7.991150,-8.239038,7.725104,6.628138,2.181085,9.070140,0.571326,8.323184,5.663917,-5.999676,-8.100734,-3.969028,-1.890862,-4.935344,-5.189067,7.074403,-5.778735,-3.023938,3.660621,1.263931,-9.243474,-0.068496,-0.460406,-4.268074,-4.213982,-1.109253,2.150906,-0.722476,-6.481971,-3.806319,-9.671760], dtype = "float64")#candidate|6297|(78,)|const|float64
call_6295 = relay.TupleGetItem(func_1521_call(relay.reshape(const_6296.astype('float32'), [14, 4, 1]), relay.reshape(const_6297.astype('float64'), [78,]), ), 3)
call_6298 = relay.TupleGetItem(func_1525_call(relay.reshape(const_6296.astype('float32'), [14, 4, 1]), relay.reshape(const_6297.astype('float64'), [78,]), ), 3)
func_2089_call = mod.get_global_var('func_2089')
func_2092_call = mutated_mod.get_global_var('func_2092')
var_6302 = relay.var("var_6302", dtype = "float32", shape = ())#candidate|6302|()|var|float32
const_6303 = relay.const([[-5.829863,4.847782,-3.167853,-4.332359,-8.657800,6.485556,-6.570393,7.259221,-3.301199,8.147215,-1.004548,-5.996641,-9.521595,0.829649,-1.476207,2.722695,3.671360,-6.022223,6.399593,2.376019,2.776306,-6.529628,2.719670,-1.661009,-5.648095,3.967261,-6.682051,2.329669,8.058712,3.565108,9.661534,-1.002846,-0.809231,-6.196830,-4.006033,0.061853,-4.242153,8.115682,4.996455,2.857358,5.454284,0.648693,7.510752,3.288474,6.771379,-8.649762,4.871838,-0.813808,4.594707,6.127054,-0.050336,3.826534,9.927309,0.733716,-1.728201,-0.296441,3.722770,8.525019,-7.438409,6.541813,-1.483184,-6.657314,4.292182,3.699248,7.053184,-2.349263,3.811246,-0.467979,-0.979539,4.433132,-9.289753,-8.448971,8.456130,-5.855818,-5.743509,-2.482642,0.769513,8.212643,5.181985,-2.394101,9.613469,-7.933637,-6.530619,2.438867,-8.311561,-0.877469,-0.482554,-0.027481,-4.326013,3.954606,4.490280,0.366080,-1.536339,8.568805,9.543296,-5.979399,-4.875659,5.770244]], dtype = "float32")#candidate|6303|(1, 98)|const|float32
call_6301 = relay.TupleGetItem(func_2089_call(relay.reshape(var_6302.astype('float32'), []), relay.reshape(const_6303.astype('float32'), [1, 14, 7]), ), 1)
call_6304 = relay.TupleGetItem(func_2092_call(relay.reshape(var_6302.astype('float32'), []), relay.reshape(const_6303.astype('float32'), [1, 14, 7]), ), 1)
bop_6308 = relay.greater_equal(call_6301.astype('bool'), var_6302.astype('bool')) # shape=(15, 1, 9)
bop_6311 = relay.greater_equal(call_6304.astype('bool'), var_6302.astype('bool')) # shape=(15, 1, 9)
uop_6313 = relay.sin(call_6301.astype('float32')) # shape=(15, 1, 9)
uop_6315 = relay.sin(call_6304.astype('float32')) # shape=(15, 1, 9)
output = relay.Tuple([call_6266,bop_6288,call_6295,const_6296,const_6297,const_6303,bop_6308,uop_6313,])
output2 = relay.Tuple([call_6267,bop_6291,call_6298,const_6296,const_6297,const_6303,bop_6311,uop_6315,])
func_6327 = relay.Function([var_6302,], output)
mod['func_6327'] = func_6327
mod = relay.transform.InferType()(mod)
mutated_mod['func_6327'] = func_6327
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6328 = relay.var("var_6328", dtype = "float32", shape = ())#candidate|6328|()|var|float32
func_6327_call = mutated_mod.get_global_var('func_6327')
call_6329 = func_6327_call(var_6328)
output = call_6329
func_6330 = relay.Function([var_6328], output)
mutated_mod['func_6330'] = func_6330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
call_6334 = relay.TupleGetItem(func_5115_call(), 0)
call_6335 = relay.TupleGetItem(func_5117_call(), 0)
output = relay.Tuple([call_6334,])
output2 = relay.Tuple([call_6335,])
func_6339 = relay.Function([], output)
mod['func_6339'] = func_6339
mod = relay.transform.InferType()(mod)
output = func_6339()
func_6340 = relay.Function([], output)
mutated_mod['func_6340'] = func_6340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6013_call = mod.get_global_var('func_6013')
func_6015_call = mutated_mod.get_global_var('func_6015')
call_6350 = relay.TupleGetItem(func_6013_call(), 0)
call_6351 = relay.TupleGetItem(func_6015_call(), 0)
func_5475_call = mod.get_global_var('func_5475')
func_5478_call = mutated_mod.get_global_var('func_5478')
var_6355 = relay.var("var_6355", dtype = "float32", shape = (440,))#candidate|6355|(440,)|var|float32
call_6354 = relay.TupleGetItem(func_5475_call(relay.reshape(var_6355.astype('float32'), [440, 1])), 2)
call_6356 = relay.TupleGetItem(func_5478_call(relay.reshape(var_6355.astype('float32'), [440, 1])), 2)
func_5816_call = mod.get_global_var('func_5816')
func_5817_call = mutated_mod.get_global_var('func_5817')
call_6359 = func_5816_call()
call_6360 = func_5816_call()
output = relay.Tuple([call_6350,call_6354,var_6355,call_6359,])
output2 = relay.Tuple([call_6351,call_6356,var_6355,call_6360,])
func_6389 = relay.Function([var_6355,], output)
mod['func_6389'] = func_6389
mod = relay.transform.InferType()(mod)
var_6390 = relay.var("var_6390", dtype = "float32", shape = (440,))#candidate|6390|(440,)|var|float32
output = func_6389(var_6390)
func_6391 = relay.Function([var_6390], output)
mutated_mod['func_6391'] = func_6391
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6418 = relay.var("var_6418", dtype = "float64", shape = (4, 4, 4))#candidate|6418|(4, 4, 4)|var|float64
uop_6419 = relay.sqrt(var_6418.astype('float64')) # shape=(4, 4, 4)
uop_6423 = relay.cosh(var_6418.astype('float32')) # shape=(4, 4, 4)
output = relay.Tuple([uop_6419,uop_6423,])
output2 = relay.Tuple([uop_6419,uop_6423,])
func_6427 = relay.Function([var_6418,], output)
mod['func_6427'] = func_6427
mod = relay.transform.InferType()(mod)
mutated_mod['func_6427'] = func_6427
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6428 = relay.var("var_6428", dtype = "float64", shape = (4, 4, 4))#candidate|6428|(4, 4, 4)|var|float64
func_6427_call = mutated_mod.get_global_var('func_6427')
call_6429 = func_6427_call(var_6428)
output = call_6429
func_6430 = relay.Function([var_6428], output)
mutated_mod['func_6430'] = func_6430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6464 = relay.var("var_6464", dtype = "float64", shape = (8, 16, 2))#candidate|6464|(8, 16, 2)|var|float64
uop_6465 = relay.sqrt(var_6464.astype('float64')) # shape=(8, 16, 2)
output = relay.Tuple([uop_6465,])
output2 = relay.Tuple([uop_6465,])
func_6474 = relay.Function([var_6464,], output)
mod['func_6474'] = func_6474
mod = relay.transform.InferType()(mod)
mutated_mod['func_6474'] = func_6474
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6475 = relay.var("var_6475", dtype = "float64", shape = (8, 16, 2))#candidate|6475|(8, 16, 2)|var|float64
func_6474_call = mutated_mod.get_global_var('func_6474')
call_6476 = func_6474_call(var_6475)
output = call_6476
func_6477 = relay.Function([var_6475], output)
mutated_mod['func_6477'] = func_6477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mod.get_global_var('func_5816')
func_5817_call = mutated_mod.get_global_var('func_5817')
call_6501 = func_5816_call()
call_6502 = func_5816_call()
var_6504 = relay.var("var_6504", dtype = "float64", shape = (2, 13, 14))#candidate|6504|(2, 13, 14)|var|float64
bop_6505 = relay.greater_equal(call_6501.astype('bool'), relay.reshape(var_6504.astype('bool'), relay.shape_of(call_6501))) # shape=(2, 13, 14)
bop_6508 = relay.greater_equal(call_6502.astype('bool'), relay.reshape(var_6504.astype('bool'), relay.shape_of(call_6502))) # shape=(2, 13, 14)
output = relay.Tuple([bop_6505,])
output2 = relay.Tuple([bop_6508,])
func_6512 = relay.Function([var_6504,], output)
mod['func_6512'] = func_6512
mod = relay.transform.InferType()(mod)
var_6513 = relay.var("var_6513", dtype = "float64", shape = (2, 13, 14))#candidate|6513|(2, 13, 14)|var|float64
output = func_6512(var_6513)
func_6514 = relay.Function([var_6513], output)
mutated_mod['func_6514'] = func_6514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5856_call = mod.get_global_var('func_5856')
func_5857_call = mutated_mod.get_global_var('func_5857')
call_6527 = func_5856_call()
call_6528 = func_5856_call()
var_6530 = relay.var("var_6530", dtype = "float32", shape = (7, 15, 14))#candidate|6530|(7, 15, 14)|var|float32
bop_6531 = relay.bitwise_xor(call_6527.astype('uint16'), relay.reshape(var_6530.astype('uint16'), relay.shape_of(call_6527))) # shape=(7, 15, 14)
bop_6534 = relay.bitwise_xor(call_6528.astype('uint16'), relay.reshape(var_6530.astype('uint16'), relay.shape_of(call_6528))) # shape=(7, 15, 14)
output = bop_6531
output2 = bop_6534
func_6548 = relay.Function([var_6530,], output)
mod['func_6548'] = func_6548
mod = relay.transform.InferType()(mod)
var_6549 = relay.var("var_6549", dtype = "float32", shape = (7, 15, 14))#candidate|6549|(7, 15, 14)|var|float32
output = func_6548(var_6549)
func_6550 = relay.Function([var_6549], output)
mutated_mod['func_6550'] = func_6550
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6559 = relay.var("var_6559", dtype = "float64", shape = (4, 1, 3))#candidate|6559|(4, 1, 3)|var|float64
uop_6560 = relay.atanh(var_6559.astype('float64')) # shape=(4, 1, 3)
output = relay.Tuple([uop_6560,])
output2 = relay.Tuple([uop_6560,])
func_6575 = relay.Function([var_6559,], output)
mod['func_6575'] = func_6575
mod = relay.transform.InferType()(mod)
mutated_mod['func_6575'] = func_6575
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6576 = relay.var("var_6576", dtype = "float64", shape = (4, 1, 3))#candidate|6576|(4, 1, 3)|var|float64
func_6575_call = mutated_mod.get_global_var('func_6575')
call_6577 = func_6575_call(var_6576)
output = call_6577
func_6578 = relay.Function([var_6576], output)
mutated_mod['func_6578'] = func_6578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
call_6596 = relay.TupleGetItem(func_5115_call(), 0)
call_6597 = relay.TupleGetItem(func_5117_call(), 0)
func_235_call = mod.get_global_var('func_235')
func_238_call = mutated_mod.get_global_var('func_238')
var_6607 = relay.var("var_6607", dtype = "float32", shape = (2160,))#candidate|6607|(2160,)|var|float32
const_6608 = relay.const([8.944669,4.100577,-1.945391,7.309374,-0.431122,-9.609900,-1.331864,4.446967,-9.253986,-4.240827,-0.892698,2.904600,1.001455,0.111896,2.639122,-6.825014,1.556293,-0.465060,7.869897,-3.872149,8.816678,9.031837,-9.747894,-4.794298,5.235214,0.669763,-8.307732,-3.237467,-0.032282,-2.119481,-0.270472,-1.996091,5.916580,6.450567,-6.972550,-4.986154,-1.821246,-8.437640,9.459326,-9.516124,3.211096,-9.169847,-8.670643,7.466955,-2.956972,2.092179,-2.564918,-1.059752,-1.323561,3.746281,0.555122,1.585638,0.903636,-3.777899,-2.616854,9.705018,6.829997,-8.434226,0.985629,-6.348897,0.357424,-6.992529,3.950723,9.431810,1.548215,9.211296,5.931025,-6.623014,-5.158752,8.526210,8.790247,-9.883861,-0.144181,5.295125,-5.562033,8.283664,7.438645,-1.026291,-0.611326,-3.607263,-0.775018,-5.759066,-8.579528,-8.518431,-3.084372,-7.033969,-6.119473,-2.738272,9.578760,-7.422733,1.380015,5.980174,-3.403764,2.302252,-7.324406,-0.477697,0.638046,-0.066696,7.522960,-1.066358,-9.593019,-0.420314,6.251002,3.965264,-0.268399,3.240924,5.245645,-0.181565,-5.101225,-3.121148,5.229059,0.062069,5.808640,2.998865,-9.631890,-2.350736,-6.925095,4.554897,9.689275,-5.550065,9.448057,9.443182,-0.971442,-2.566037,-9.675927,4.204483,3.452570,-8.003838,-6.838746,2.384435,-3.973424,6.216893,-7.911355,-8.498320,6.620913], dtype = "float32")#candidate|6608|(135,)|const|float32
call_6606 = relay.TupleGetItem(func_235_call(relay.reshape(var_6607.astype('float32'), [15, 9, 16]), relay.reshape(const_6608.astype('float32'), [15, 9]), ), 2)
call_6609 = relay.TupleGetItem(func_238_call(relay.reshape(var_6607.astype('float32'), [15, 9, 16]), relay.reshape(const_6608.astype('float32'), [15, 9]), ), 2)
func_5887_call = mod.get_global_var('func_5887')
func_5889_call = mutated_mod.get_global_var('func_5889')
call_6649 = relay.TupleGetItem(func_5887_call(), 0)
call_6650 = relay.TupleGetItem(func_5889_call(), 0)
output = relay.Tuple([call_6596,call_6606,var_6607,const_6608,call_6649,])
output2 = relay.Tuple([call_6597,call_6609,var_6607,const_6608,call_6650,])
func_6654 = relay.Function([var_6607,], output)
mod['func_6654'] = func_6654
mod = relay.transform.InferType()(mod)
var_6655 = relay.var("var_6655", dtype = "float32", shape = (2160,))#candidate|6655|(2160,)|var|float32
output = func_6654(var_6655)
func_6656 = relay.Function([var_6655], output)
mutated_mod['func_6656'] = func_6656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mod.get_global_var('func_5816')
func_5817_call = mutated_mod.get_global_var('func_5817')
call_6728 = func_5816_call()
call_6729 = func_5816_call()
uop_6733 = relay.asinh(call_6728.astype('float32')) # shape=(2, 13, 14)
uop_6735 = relay.asinh(call_6729.astype('float32')) # shape=(2, 13, 14)
output = relay.Tuple([uop_6733,])
output2 = relay.Tuple([uop_6735,])
func_6744 = relay.Function([], output)
mod['func_6744'] = func_6744
mod = relay.transform.InferType()(mod)
mutated_mod['func_6744'] = func_6744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6744_call = mutated_mod.get_global_var('func_6744')
call_6745 = func_6744_call()
output = call_6745
func_6746 = relay.Function([], output)
mutated_mod['func_6746'] = func_6746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6013_call = mod.get_global_var('func_6013')
func_6015_call = mutated_mod.get_global_var('func_6015')
call_6772 = relay.TupleGetItem(func_6013_call(), 0)
call_6773 = relay.TupleGetItem(func_6015_call(), 0)
output = relay.Tuple([call_6772,])
output2 = relay.Tuple([call_6773,])
func_6804 = relay.Function([], output)
mod['func_6804'] = func_6804
mod = relay.transform.InferType()(mod)
mutated_mod['func_6804'] = func_6804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6804_call = mutated_mod.get_global_var('func_6804')
call_6805 = func_6804_call()
output = call_6805
func_6806 = relay.Function([], output)
mutated_mod['func_6806'] = func_6806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5686_call = mod.get_global_var('func_5686')
func_5687_call = mutated_mod.get_global_var('func_5687')
call_6819 = func_5686_call()
call_6820 = func_5686_call()
output = call_6819
output2 = call_6820
func_6825 = relay.Function([], output)
mod['func_6825'] = func_6825
mod = relay.transform.InferType()(mod)
output = func_6825()
func_6826 = relay.Function([], output)
mutated_mod['func_6826'] = func_6826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5792_call = mod.get_global_var('func_5792')
func_5793_call = mutated_mod.get_global_var('func_5793')
call_6829 = func_5792_call()
call_6830 = func_5792_call()
func_2813_call = mod.get_global_var('func_2813')
func_2816_call = mutated_mod.get_global_var('func_2816')
var_6832 = relay.var("var_6832", dtype = "uint32", shape = ())#candidate|6832|()|var|uint32
var_6833 = relay.var("var_6833", dtype = "uint32", shape = (2240,))#candidate|6833|(2240,)|var|uint32
call_6831 = relay.TupleGetItem(func_2813_call(relay.reshape(var_6832.astype('uint32'), []), relay.reshape(var_6833.astype('uint32'), [14, 16, 10]), ), 1)
call_6834 = relay.TupleGetItem(func_2816_call(relay.reshape(var_6832.astype('uint32'), []), relay.reshape(var_6833.astype('uint32'), [14, 16, 10]), ), 1)
func_235_call = mod.get_global_var('func_235')
func_238_call = mutated_mod.get_global_var('func_238')
const_6841 = relay.const([-2.280747,-9.507644,0.861840,2.157065,7.250276,2.028334,-9.811706,2.440410,-8.264085,9.975827,-0.875380,-2.556819,-8.030276,7.143328,1.241290,-6.444927,2.732477,4.554094,-8.529069,-4.859736,-8.070597,-8.925582,-6.921132,2.283947,-0.302173,-6.611807,-6.032135,0.979131,5.749473,-4.015905,-1.470356,-3.035662,-2.243159,-7.643221,-7.430921,-9.801585,-7.579118,-2.828894,3.124997,-2.894302,-0.828351,-0.700487,6.102936,-1.447211,-6.222255,3.697105,5.343030,5.875317,9.665571,-3.934842,-7.052956,1.371613,-5.647487,1.127316,7.801064,2.472566,9.880163,-4.324614,-4.685460,5.221279,5.641972,6.375424,-1.403692,-5.263063,-2.425453,4.299611,-4.624492,-6.957609,-4.612851,-4.841940,6.719616,-4.939179,5.405181,6.347043,3.208737,-0.877190,0.194250,2.214930,-4.611197,-6.291907,1.341545,-0.253742,-1.742192,-4.349667,-2.615719,-5.263120,-9.322485,-2.418225,2.176380,9.078437,-2.410060,2.233127,1.221825,8.233753,2.937631,9.140272,-7.317685,-8.426159,-4.566847,6.829129,2.734183,-8.111941,-0.093119,0.387191,-6.974832,-9.025286,-4.822472,-2.176373,7.368411,-7.129517,5.072600,4.231819,1.880240,-9.215742,-2.336292,-3.672975,4.733845,6.440683,-5.054791,3.793829,-8.565829,9.422958,-8.326631,-8.609560,-6.046985,-9.526817,-4.372404,8.502432,6.823527,6.882250,1.216243,6.893523,-5.214946,6.275881,7.265231,2.100816,-9.748910,-2.717237,0.087614,-1.586897,3.263160,5.672232,-0.703659,0.209685,8.045521,9.319131,9.240975,4.018732,-3.146082,-7.719442,-2.071303,2.136156,-1.521073,7.743658,-8.503980,3.342075,-2.164145,-1.895518,3.057381,-6.685180,-9.622092,-0.643885,-1.347777,-4.615624,-9.895622,-4.982898,-9.480397,2.917235,9.876398,-0.724813,2.008224,-3.412177,9.908217,-3.952049,-7.751004,9.984164,5.821021,-9.734626,4.442556,-1.763595,9.698211,-8.604217,-1.178779,5.228152,-4.573188,7.978151,7.308898,3.086061,-3.219891,-0.290325,-1.995987,-7.203698,2.068827,6.536078,8.354480,-1.603510,-0.753309,-5.441754,-1.534175,2.918369,-0.184892,-4.335536,-9.598114,-7.951484,-1.821894,9.727071,-6.584254,-3.525218,1.420307,-0.683877,6.420423,8.804842,-7.649818,-4.047767,8.723664,4.816284,-9.908513,-0.591038,-5.311760,-5.493819,7.462117,0.676467,3.044425,6.853136,-4.211447,0.691351,-5.426792,3.762424,-4.952782,8.686942,9.906879,0.776418,6.752324,-1.476142,-2.377707,-5.940748,2.575383,9.317222,8.940852,7.859987,4.278262,4.362219,3.691478,-0.324902,-5.890821,-1.370716,-9.958266,2.393564,5.859668,1.689104,-0.973416,7.657869,-9.249299,-9.960361,6.604729,4.989536,-9.176489,-6.051343,3.705370,-0.545534,-0.848321,-6.550197,-9.493741,-1.044569,3.394191,-8.169031,8.318987,0.757077,-3.493737,8.073476,1.193173,-1.865027,4.263627,-7.500461,7.097560,-7.051102,7.334794,9.315823,7.492910,1.106080,4.195743,-3.595920,3.575103,-6.411455,-2.141459,5.095576,-9.680283,7.925409,-4.030672,4.093286,-1.690777,1.356694,-3.549591,-7.928261,5.537739,-8.955566,9.045311,7.702510,3.306346,-1.008016,-2.338646,0.250323,-2.194852,-3.984345,-5.414540,-1.241471,-2.158650,-6.311526,-0.892152,-0.899465,-9.786400,7.799326,0.101017,-5.426154,-9.993097,-1.511778,-1.432988,-1.748635,9.667472,4.568137,-9.567957,-0.289051,-5.207563,4.835163,0.919498,-4.753784,-9.446461,3.377022,-1.555842,-0.984691,5.559523,8.714509,0.201798,-4.839241,3.796417,-3.203611,0.087827,-1.558704,-9.826029,6.242772,0.596487,9.978554,2.390000,7.751199,8.208257,-5.039631,0.332599,-7.048949,8.385454,5.213494,5.961294,-1.615914,-8.572662,-5.388212,-9.221527,0.488457,1.877222,-2.168778,1.807555,-4.503836,7.710283,1.999485,6.899970,0.754862,-5.079914,1.937922,8.659926,6.274362,-3.602750,-9.688062,4.631529,-1.315207,-4.359572,3.023372,-5.715871,-1.939098,-5.133318,-6.273633,-9.289622,9.344469,-7.298242,-3.378905,-2.897360,-5.025161,0.015841,-3.944216,-9.067405,9.324165,0.516799,-0.912801,-1.928085,4.283534,1.075260,-2.137251,-8.223741,-5.552430,-9.015944,-2.359051,-3.881431,2.273607,9.637509,-1.555139,-2.572460,-4.230763,-3.551425,-5.922272,-2.102543,-8.454081,7.165675,2.957623,-6.226800,1.594128,-7.149258,2.649603,-1.114735,-1.886181,-0.662488,5.685633,-1.837960,-5.959645,-3.019047,7.296583,0.328498,-0.650773,4.566842,-6.206122,-6.602088,-5.058172,0.102968,6.129229,0.314962,1.590622,1.116472,-1.717958,-4.055024,-8.137681,8.031209,4.506399,7.075894,-8.168937,6.265011,-6.481633,-5.004260,-6.615353,2.742765,6.604093,2.643844,-7.326662,7.360430,-9.454202,-9.203298,-1.716322,7.581462,-2.961521,-2.738091,2.460364,9.898916,4.218128,-2.243607,6.403508,4.452103,-6.677256,9.047362,2.471355,-4.470472,-8.083312,2.513920,-1.612527,6.519727,6.856407,9.134149,7.273089,9.939723,-1.723995,0.805242,9.553955,-4.111987,2.445162,-5.709641,-3.629192,3.451009,9.648449,-4.683878,3.443911,-9.315636,0.967286,5.027900,-6.361744,0.181479,-7.103288,-4.776602,2.492788,-3.986318,-2.965639,-3.187965,9.508164,-0.899088,-7.850861,-2.006153,-2.398087,-9.282891,7.510086,-8.147730,-8.164462,-2.470255,-0.310751,-0.993148,-3.272038,3.358723,-3.120478,1.638255,0.124352,-6.627472,-4.939456,5.407901,-5.400255,-2.713798,4.852183,7.362821,-8.876605,-6.109363,3.025306,5.011596,7.293857,-0.482479,-5.623840,1.815383,8.107848,0.974013,1.997701,-4.528817,-3.873156,3.002128,-2.634308,-0.185472,-6.546694,4.218755,1.421507,7.514690,3.625451,-2.957007,-0.038907,7.547339,-2.000992,4.173386,6.828107,6.108730,2.909457,1.805359,7.327536,-8.538962,2.461118,7.697045,-0.391691,2.731910,0.922194,0.980807,-6.320965,2.056178,7.449564,-3.052384,1.275480,1.553854,-9.440830,-8.910959,-5.932992,8.850050,-6.346564,-3.614549,-0.101787,0.753530,-3.377904,9.018083,1.177000,2.366468,9.983551,-4.811830,3.336883,4.017607,-0.545497,4.416237,5.440768,-8.931206,-9.146252,-2.098727,3.663915,-5.127948,7.891826,-3.378487,-0.105808,6.714856,0.584859,-0.987750,6.701766,-7.918169,6.540994,-9.714048,-5.974900,2.717689,-8.255642,8.523238,8.732426,2.936997,1.889307,3.380572,7.401529,-8.683085,-7.657031,0.569303,-6.133930,-0.930510,4.890006,-6.286074,7.570156,-3.754695,-8.252610,0.101247,2.651672,-9.503291,-5.727564,5.378453,-7.267230,-8.420508,-9.628286,6.473081,0.468771,1.368865,-2.564566,6.690608,3.940468,0.187784,1.940845,7.339273,0.197118,-9.372401,8.924716,8.959661,7.598128,3.059792,9.966731,-7.891660,-7.208061,-9.716351,-6.726620,-1.914825,9.940719,1.433523,8.572250,-4.238638,-7.835546,-7.972133,-3.363994,8.417444,-1.960899,8.912636,5.536162,-7.655265,5.910537,1.179251,-3.152462,3.324163,1.866465,4.818066,2.073887,-0.245466,-0.607137,-5.360575,-8.620155,-0.009544,-2.590677,3.526839,2.987419,4.758000,-6.934910,-2.512899,-2.008866,-3.334758,-4.994799,-0.272392,8.296265,5.835511,-1.989654,-0.686556,-4.575401,4.887223,3.270271,-9.418767,-7.853549,3.349862,-0.689300,-3.488140,-7.804647,4.427171,-0.008456,-8.182327,-1.941058,1.641661,4.439645,4.031944,-5.706188,-8.449207,4.508420,-1.857975,-1.110220,-4.027805,-7.794887,-5.994188,-5.269193,0.108407,6.771008,-0.814063,-7.884047,-6.194932,-4.606085,2.993650,-5.778173,-9.878323,-7.291237,-9.375561,-6.034627,-1.556873,7.258817,9.512659,-3.932143,-8.593299,3.550672,9.036505,-4.581882,0.805484,0.872849,7.259760,1.151367,-1.904677,-0.603176,-4.064192,1.171442,8.862563,9.943132,-3.987850,-3.979049,-8.983194,-1.557165,9.954789,1.069202,4.149441,0.696619,8.600273,-2.360349,-4.475823,-6.727854,4.500895,8.056395,-0.712028,-4.835369,-6.509097,8.525053,-9.107011,-1.915189,-2.228821,-0.288058,5.822230,-5.097006,-4.887619,-6.639772,5.440466,-8.272396,-6.138312,-4.976117,-4.296459,-5.628311,8.156878,1.670410,7.351099,2.830582,-5.471663,9.299204,7.689054,-2.775852,-6.048203,-8.916705,8.513323,-5.543221,9.274642,-0.478159,8.866200,-4.312007,-4.715452,-6.812548,-0.282071,5.783690,-3.954935,-8.512527,-5.854858,5.146418,1.782781,-4.367282,-9.344133,-0.851296,5.503479,-8.887543,0.759309,9.784699,-8.863776,0.793489,5.240057,3.970363,6.493059,8.260449,-7.304410,-2.966012,0.481512,-6.657041,-3.538359,4.971973,1.653296,-2.697954,-8.775458,-2.603694,-0.831835,7.848411,-0.330237,0.250393,-2.041768,4.021820,0.787068,-7.524390,4.465805,0.320044,-2.248754,4.752620,-9.323318,-9.797034,-4.726380,4.054992,3.412483,-8.910073,-8.646169,6.659187,8.948616,6.332740,2.054874,7.050449,2.431034,-0.570641,1.601357,5.738898,8.381602,-1.733707,8.655986,-8.019590,9.538487,-0.815148,-8.317791,-0.934858,0.263012,4.889262,-4.978983,2.371120,0.050906,2.758448,8.709655,-6.856306,-8.640874,-2.769200,-2.367905,-1.500704,-1.911164,3.753918,2.917198,-5.648878,-5.648673,0.955930,-7.111253,-2.179145,-7.796750,-3.346520,-7.608777,-9.922818,2.606595,-8.536009,-4.363045,2.959122,-7.939875,1.355751,3.216933,-6.947034,3.758077,-8.188391,-3.755354,4.240681,-2.417501,-0.338252,-8.799901,8.902137,-6.020233,-2.277197,1.238722,1.092783,-5.029153,1.398328,-1.299217,6.487515,4.948969,1.156836,-5.984296,-1.410219,-9.651413,-9.593528,0.617455,-6.098567,5.231764,-2.388480,6.589347,-2.720733,3.481002,3.559220,9.157654,7.928668,-0.801740,-4.456298,-6.896872,4.255679,-0.522959,2.770716,9.771884,6.114760,-4.179074,6.235506,7.638136,-4.013774,4.308141,-9.187552,-3.437455,4.115750,-0.370893,-0.449477,-6.295499,9.501235,3.683126,7.283060,-2.612096,2.876231,-2.733182,-8.754933,1.098805,-0.076702,-4.271349,6.501002,8.501440,3.469670,8.367229,-3.161535,1.188525,-8.716490,-9.324548,-8.817562,-5.564930,-6.299894,-4.856294,-6.481925,8.442472,6.859135,8.457781,-2.094963,3.492566,-1.154510,8.306914,1.252942,-7.391513,4.972979,6.902975,6.973950,-5.517313,-5.119356,8.278185,-6.963508,-5.192392,-4.818851,-3.119793,-5.016622,2.228984,-4.924714,1.101887,9.153705,5.875291,-7.025788,-1.515780,-4.510680,6.834605,-6.217313,2.768964,2.133600,-1.644696,4.881569,2.442007,-9.438353,-4.773089,3.745106,-0.352545,5.802681,-4.496425,-2.526405,-8.679155,2.664841,-8.476202,-5.236378,-7.230288,2.060069,2.771011,5.136508,-5.209475,2.360093,7.970143,-4.149880,-3.226550,4.494556,9.881571,9.375416,3.818203,-0.775350,-0.522499,6.628623,-6.979161,8.648035,-4.290964,-3.524726,5.999595,2.173947,1.551610,-2.681173,-6.143295,-5.614433,-5.045055,6.767591,-3.525241,4.181285,-1.745656,3.900111,5.440341,-4.858914,9.378531,-6.217554,9.155982,2.217164,1.823660,-0.982041,-0.587516,4.795240,-7.911124,-0.827578,-2.652097,-0.426903,-2.479355,-7.897052,-1.341854,6.338932,2.130660,-3.647571,-0.105807,7.533374,-6.159840,0.093759,-6.853259,8.843444,3.806357,5.273917,6.424729,-0.099990,6.307559,9.848602,6.184232,-1.654315,-5.499983,6.583626,-8.358304,-2.417241,-3.627324,2.862227,-8.847320,-5.901743,-0.099997,-8.521887,4.154103,-8.836928,1.834534,-7.051541,-6.186558,2.695696,-4.553351,6.661178,-5.322345,5.112723,7.880188,4.118564,5.741846,0.451781,-3.530891,5.725272,-9.506752,-1.498143,1.860245,5.656155,9.467885,-0.149977,5.635820,4.035933,4.123763,9.232614,6.399253,-2.720326,-7.786531,5.629261,4.044189,-4.650788,-2.307443,6.470711,0.772171,2.710135,-5.791664,-6.790593,-3.015682,5.490440,-2.196245,-4.521794,1.437882,-4.220924,0.195857,-0.459870,-3.119624,-4.320022,-1.763685,-3.028480,-4.954933,-0.649446,1.092002,9.663271,-7.695083,3.053198,4.743466,0.249286,4.750470,-3.103021,8.264611,0.038792,3.081820,-5.105429,-6.473816,3.265381,-8.921311,1.076823,3.824795,9.180569,0.529044,-0.044939,7.852708,4.027318,-3.597753,2.958549,2.577626,4.736091,-6.191465,-4.338506,3.802453,-1.355490,3.880846,4.513311,-2.889854,6.837360,-5.911356,-5.377785,3.569669,-6.173197,4.533612,0.974346,-1.734953,3.164377,-6.700303,4.480379,9.169784,8.513048,7.668007,0.631794,-8.910406,5.034986,2.758604,-4.161102,-8.414160,-4.392075,-2.013585,-2.353017,-5.086031,3.539403,0.395047,-1.350226,-3.318475,5.179257,3.875457,4.793631,8.455347,-8.992527,-9.978265,6.391898,0.175664,-5.251986,7.217426,-3.717252,-7.071473,-0.782641,2.130530,7.909993,1.056296,5.435866,9.595686,-1.401065,-2.614898,7.379774,8.003542,3.994937,-7.750966,-4.666616,-4.939934,-4.117263,-5.590571,-5.607860,7.520988,-7.657130,-6.829821,7.682014,-5.054305,0.360573,-8.272044,-9.357417,3.501414,-1.751357,1.662589,-5.766515,-3.768009,0.873738,0.373691,-3.871613,2.602013,8.672067,-0.482919,7.213620,-6.411296,4.132639,-9.004907,-4.052991,2.802003,4.461236,1.817414,-7.040498,-0.224500,3.032146,0.646105,3.259673,-9.379051,8.379142,9.112914,2.645995,3.432299,4.884062,-0.643840,3.142458,-4.273532,7.172358,-2.905958,5.648486,1.329070,3.289007,-1.593785,6.541530,4.196847,-6.972671,7.879819,9.777372,-0.541448,-2.915777,-5.201572,2.303365,8.460521,3.648582,-9.758858,-8.927424,2.569328,4.768562,-7.788527,-7.126229,6.423678,3.536448,-8.466555,7.446331,9.493538,-6.012136,5.975035,-5.209311,-1.469567,4.037668,7.837060,-3.844564,2.907387,-3.652413,-0.470002,6.438191,0.364508,-0.257996,1.837765,1.658853,-5.425761,7.272513,7.195567,-7.125612,5.307523,-1.751701,4.288982,9.954546,-1.304363,7.967986,-7.337636,-9.871785,8.297409,0.210879,-0.277457,2.937468,-4.386699,1.500377,-8.600240,5.831488,6.250176,-6.190273,-7.942382,4.373998,-9.093345,6.017327,9.800784,-4.680080,1.430346,-9.559105,-1.950988,-3.684616,-3.650630,-0.049952,6.126474,-7.146913,-5.172505,3.934899,-5.164588,0.542269,2.791938,7.952325,2.819321,1.585504,6.229814,-5.359610,2.650981,8.459584,-2.272265,9.263754,1.280859,-5.236085,-6.920425,3.274355,-7.514479,3.214402,3.834276,8.004319,9.814147,2.999115,-7.963627,-0.561137,-3.498492,2.713626,-2.287972,-3.551075,-4.782690,4.836962,9.683703,8.412924,6.461455,8.668584,0.183398,3.065191,-5.618322,4.572909,0.784547,-5.781239,2.864234,-5.687194,-6.576656,-7.659263,-8.769897,-3.821213,-7.000802,1.003385,-4.698479,-0.217309,3.780464,-2.240703,4.832645,-3.344182,-2.286418,-6.800633,-5.863047,3.435838,-3.159490,3.302115,4.830822,-5.312863,0.959216,2.679057,-9.539169,4.884342,-8.053285,2.328673,-3.880052,-3.248132,6.115001,-6.498702,0.087957,-8.057258,1.397859,-8.045132,2.107047,-5.064413,6.500547,2.422396,-2.547619,2.588265,-3.686137,-5.158592,8.079375,9.467675,5.257845,-4.956608,2.641304,-5.604623,0.714198,0.799635,6.653631,5.035705,-4.598529,7.304668,-7.052709,0.391951,3.358580,4.930912,-0.846764,1.950073,-2.395541,-5.589663,7.697018,3.503348,-3.537533,2.510338,-6.805215,-4.734123,0.414441,1.371155,-6.415711,3.664454,-3.847966,-2.745434,9.244351,2.434186,-8.910432,-4.992539,-0.108908,-6.276552,-7.461010,7.133736,-7.394021,4.364887,6.211422,1.510226,9.026257,6.195935,6.451216,-3.822398,-3.386321,8.717983,-6.520349,-0.042287,8.246071,7.746493,-3.882535,-1.325821,-5.698862,7.240189,5.395954,5.303592,2.303554,-3.989294,1.678793,2.332744,-8.250637,-2.028587,-4.377883,-0.665552,5.075193,-6.790392,-5.698951,-4.208339,-0.838169,-8.608738,5.208369,6.057503,-8.874864,4.979652,-2.081626,9.711330,7.996527,3.681989,-8.323193,5.456924,0.339239,-2.872531,7.498219,-2.793072,-9.600017,0.530500,3.989483,-2.718358,-2.008337,4.320238,-9.180631,-0.350376,-5.149106,-9.838322,6.940664,-9.322715,8.189959,-5.061438,2.904004,-6.107687,5.322896,4.032653,-0.582236,-3.075373,-1.041872,-0.861715,6.771570,-8.411620,-4.922981,-6.145984,1.632810,9.580562,7.139294,6.742262,-4.656222,-4.166015,7.144258,-3.691000,7.242802,-9.961105,-9.540525,5.708668,7.288943,2.702177,-2.678684,3.849351,-7.158207,-1.009427,-6.850922,6.055677,7.089512,-7.573692,2.869619,0.348300,-3.629938,-1.691355,-5.715406,-2.788251,-0.800021,3.450852,1.011087,-3.350840,8.786219,-3.014816,-2.577203,6.913337,3.257474,-6.711607,-9.763370,-6.250233,6.209409,-9.282262,-9.154787,-4.545395,-7.513462,7.483135,-4.534672,-5.318659,-9.709708,-4.625770,-5.158839,-9.692297,1.610612,-3.048756,-7.410806,-3.607774,-2.670872,5.846593,7.303961,8.372772,-6.078363,-7.257167,-8.122755,-9.660538,8.962248,9.489943,-9.479548,7.926963,-7.588567,-1.644271,-9.038798,-9.579708,1.177395,9.928378,1.041050,-6.405350,7.241716,2.069666,8.866962,-5.654012,-0.949635,-8.895976,-2.859684,-9.527742,-0.989718,9.262867,-1.783173,9.456835,-8.651695,-5.891961,9.387008,9.257017,2.051565,-2.304461,-7.064881,5.393711,-3.997993,-7.519718,-7.887220,0.451722,0.408418,9.686870,-8.225180,5.527605,-7.673547,2.104035,-0.674776,-0.439459,0.459000,1.974790,-7.688269,-2.164791,-3.280773,9.275706,3.518752,9.510318,3.413722,-3.820556,9.875701,-0.051825,-1.820277,2.047542,-2.896605,-8.304120,-7.516930,-5.414594,7.806319,9.412465,7.426330,-6.781411,9.785959,8.638801,-3.579885,6.037114,5.446099,9.929373,5.395697,-1.270752,5.753453,2.496091,-6.719988,-2.201466,-4.528619,-1.445066,-7.441165,-9.666325,-8.794091,-2.975740,-6.766946,8.362411,-1.657374,5.882144,0.273677,8.513259,-2.295367,3.686956,-5.904260,-6.461762,9.507693,-8.844537,4.433420,-0.980352,-3.560797,7.885164,-7.086396,-1.350311,0.022131,-6.653070,-5.617235,7.286944,-6.371153,0.349485,-6.233581,4.012120,-1.053448,6.735774,-0.003474,-3.171758,9.989492,6.852871,-7.266358,-3.926403,8.027033,-2.205021,-6.162036,3.390580,-4.182504,-7.619040,-8.000157,4.518330,1.818194,5.432556,-4.662594,6.823901,3.068655,6.704636,-5.367603,6.679790,-5.111664,2.520829,-2.537186,0.090402,-1.950645,9.704993,2.762958,6.261716,-8.350546,-8.772880,-1.076048,-5.803961,5.655514,2.102261,1.217428,8.941177,0.289540,-4.805522,2.565287,-5.839792,0.359779,6.174205,-2.274574,-7.047926,9.114479,4.844262,-8.153790,3.664905,3.331583,2.596928,5.922416,-7.543490,-8.031345,-8.424237,-5.067218,9.033855,8.691652,-8.749777,8.208979,-8.709042,-3.949385,2.924858,9.076184,-9.997245,3.171479,5.311222,-3.173254,0.143686,-1.647965,0.359868,2.413858,7.985121,3.500759,-9.237699,-3.361624,3.785874,7.873188,1.419917,9.122694,8.668277,3.614691,3.374384,2.254906,-2.859866,1.015895,-0.220121,-7.150268,4.347616,-6.479570,3.878620,-5.051106,7.860791,1.023159,-4.294720,-3.641250,4.016373,-7.675393,9.093895,-5.813550,8.445639,3.540289,-2.325403,3.471497,0.901867,7.547697,-1.950721,8.253444,7.228054,-9.088899,0.283927,-8.328280,0.345766,-0.972978,-4.071054,-3.023448,-9.154260,7.500888,-2.067792,-1.648548,-6.756308,-4.712230,1.942038,-0.888162,-8.009066,-2.307646,8.112464,-0.314345,5.919338,-7.653247,4.269185,6.544516,-1.041379,-2.452459,-8.992130,2.002442,3.219197,0.283364,1.820526,0.598566,8.771005,-6.044453,-9.795009,5.207452,1.852132,8.820673,-2.812692,-4.902050,-6.154363,0.609920,5.618626,0.382470,-2.067002,6.963294,8.873266,5.599631,-6.925083,0.185008,9.604597,-0.180073,-0.962371,0.562708,-1.459240,-3.816827,0.283534,0.432462,-0.432781,1.665823,-5.897432,-5.089929,5.176544,-9.727706,6.307010,8.376576,-8.403620,0.081062,1.591652,5.466485,-7.395270,-7.637377,-5.484166,-0.225966,1.554303,4.994764,-6.136316,4.843159,-9.682701,3.047191,5.814449,-9.712527,-1.066160,3.333169,-4.343198,-8.157837,-6.434072,-6.857295,-8.815260,4.840590,-2.057358,8.432424,-2.900257,3.655854,-3.715524,5.594918,1.275259,6.824093,2.325468,8.337734,-5.948784,3.896689,7.460483,3.066008,-8.556238,4.824146,4.932764,-2.800805,6.949678,-4.522034,-9.479255,1.482631,5.767307,-8.460525,3.569591,0.927318,1.792021,-2.484512,-6.609885,-4.312290,-1.230767,-2.555615,1.262097,-7.246349,-0.209263,-8.493901,-9.946350,-1.702166,3.367137,-8.394209,-3.654879,-6.648438,-2.707330,-3.262076,-7.047303,-3.121000,-0.090371,-4.483193,8.722494,-6.017918,-8.306889,-7.030232,6.678834,-3.149398,4.161476,3.403202,-3.429984,0.723704,8.690434,-4.122482,3.783925,-6.357944,5.296091,8.380913,6.352515,-4.277911,-1.205084,-6.413087,1.964988,-0.243924,-1.981565,-0.622225,4.342164,7.053317,-6.155678,-1.567913,-0.508760,4.230503,-4.243316,-7.341844,7.966358,3.614685,-1.353111,1.848824,-5.554706,-1.671527,3.633270,-9.826975,1.834681,6.434982,9.664358,0.540609,6.668453,9.636426,8.070647,5.020837,-5.088660,-6.805412,2.889741,-4.360538,-2.029980,-4.041322,3.230268,-4.613362,-7.006552,-4.338605,-4.138642,-8.442929,6.742654,4.163694,1.917888,6.602615,2.355348,-0.324196,7.529325,-7.469252,-5.014618,5.745618,8.593775,-4.784677,-0.882790,6.904167,-4.706957,-7.447330,2.790173,-0.232986,-9.854684,-2.233579,7.471793,-7.644735,9.012440,-3.625953,3.733420,-7.794104,-4.868146,8.595503,4.952425,7.801492,-4.671622,5.192328,2.820775,-1.205544,6.341978,1.045953,-2.708258,3.701340,-0.447262,0.338402,-3.377293,4.198731,-1.315461,8.980887,8.087563,7.204229,-2.142190,-2.919672,-8.860338,2.934229,3.881946,-0.904595,6.322886,-2.005853,-2.521782,9.744374,4.644309,6.161994,9.547925,9.254921,9.781684,-7.041749,-7.965427,6.731589,-0.298378,-8.622358,3.725319,9.887715,7.600666,-7.539757,9.009295,-4.980007,-5.891114,-5.253083,-5.409194,5.724029,-1.796651,1.518591,-0.206819,1.613905,8.129013,-7.635798,-0.365519,5.405207,9.152283,2.856659,-3.896112,1.041093,7.852694,-3.472674,-1.068874,3.116758,-8.706189,3.516446,5.954166,4.773432,-8.755587,8.954899,0.468951,-7.494513,7.617555,2.815191,0.620809,-5.136544,-4.410403,-3.577784,-5.354505,8.076826,-8.077913,0.537643,2.009636,9.589668,3.612199,-1.446503,8.898588,0.456371,0.024227,-7.347944,-6.576729,1.678062,-2.278525,1.340302,-1.603233,2.915297,3.705311,-7.656491,7.266505,-4.811529,8.909834,0.053993,-2.804372,8.206243,5.137085], dtype = "float32")#candidate|6841|(2160,)|const|float32
var_6842 = relay.var("var_6842", dtype = "float32", shape = (45, 3))#candidate|6842|(45, 3)|var|float32
call_6840 = relay.TupleGetItem(func_235_call(relay.reshape(const_6841.astype('float32'), [15, 9, 16]), relay.reshape(var_6842.astype('float32'), [15, 9]), ), 3)
call_6843 = relay.TupleGetItem(func_238_call(relay.reshape(const_6841.astype('float32'), [15, 9, 16]), relay.reshape(var_6842.astype('float32'), [15, 9]), ), 3)
func_4883_call = mod.get_global_var('func_4883')
func_4887_call = mutated_mod.get_global_var('func_4887')
var_6846 = relay.var("var_6846", dtype = "int8", shape = (924,))#candidate|6846|(924,)|var|int8
call_6845 = relay.TupleGetItem(func_4883_call(relay.reshape(var_6846.astype('int8'), [11, 14, 6]), relay.reshape(var_6846.astype('int8'), [11, 14, 6]), ), 0)
call_6847 = relay.TupleGetItem(func_4887_call(relay.reshape(var_6846.astype('int8'), [11, 14, 6]), relay.reshape(var_6846.astype('int8'), [11, 14, 6]), ), 0)
output = relay.Tuple([call_6829,call_6831,var_6832,var_6833,call_6840,const_6841,var_6842,call_6845,var_6846,])
output2 = relay.Tuple([call_6830,call_6834,var_6832,var_6833,call_6843,const_6841,var_6842,call_6847,var_6846,])
func_6867 = relay.Function([var_6832,var_6833,var_6842,var_6846,], output)
mod['func_6867'] = func_6867
mod = relay.transform.InferType()(mod)
var_6868 = relay.var("var_6868", dtype = "uint32", shape = ())#candidate|6868|()|var|uint32
var_6869 = relay.var("var_6869", dtype = "uint32", shape = (2240,))#candidate|6869|(2240,)|var|uint32
var_6870 = relay.var("var_6870", dtype = "float32", shape = (45, 3))#candidate|6870|(45, 3)|var|float32
var_6871 = relay.var("var_6871", dtype = "int8", shape = (924,))#candidate|6871|(924,)|var|int8
output = func_6867(var_6868,var_6869,var_6870,var_6871,)
func_6872 = relay.Function([var_6868,var_6869,var_6870,var_6871,], output)
mutated_mod['func_6872'] = func_6872
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6874 = relay.var("var_6874", dtype = "int64", shape = ())#candidate|6874|()|var|int64
const_6875 = relay.const([[[-3,-10,6,1,-6,3],[-6,7,-6,-9,1,-3],[-5,-1,-9,4,2,1],[1,-1,2,8,5,-7],[-4,7,-10,-6,-3,-3],[-5,-4,-1,4,8,-9],[-1,8,2,-7,4,2],[6,10,4,-10,10,-8]],[[1,-5,9,-9,2,-8],[-5,-1,-1,-6,10,4],[9,6,2,-2,-8,-1],[-2,-7,10,-9,2,-5],[-6,8,6,1,-10,5],[-3,-2,-8,5,-3,-4],[-10,9,6,3,-4,-9],[6,6,-9,5,-1,-2]],[[-4,-9,-1,-2,-10,3],[5,-10,-8,9,-9,10],[-7,-1,-6,5,1,-8],[9,-3,9,4,3,-2],[1,7,-6,1,5,-2],[-4,-10,-1,7,-8,-8],[10,10,-4,-4,-4,8],[-9,-3,-10,7,2,-10]],[[8,4,2,3,-1,-3],[5,-3,-10,9,9,-8],[-9,-4,-2,5,-2,6],[-10,-5,-1,-8,-8,5],[2,-1,-6,-2,2,5],[8,6,10,5,-8,-2],[1,-5,-3,-8,4,7],[-8,6,-3,-8,2,5]],[[3,-1,2,-1,-5,1],[9,-2,1,-5,-8,-3],[-4,6,-4,-10,-2,-1],[6,5,-10,-7,6,-2],[-1,-7,9,-4,10,9],[-2,2,-9,8,5,-7],[10,4,5,4,-2,-9],[-1,-4,-6,5,-1,1]],[[10,-7,3,-7,-10,-10],[6,3,4,-1,-8,8],[-9,1,1,-1,-1,3],[-2,6,3,7,9,9],[3,-10,6,-4,-2,4],[6,4,6,1,8,-2],[-3,-10,10,-8,1,5],[-8,2,-3,-5,4,6]],[[7,-7,-7,5,7,-2],[7,1,10,5,4,-9],[-4,6,4,-7,3,7],[3,10,9,7,4,4],[-2,3,6,5,-6,9],[4,2,-10,-7,-1,2],[-9,-6,7,-6,-10,-6],[-10,-10,1,10,-7,-5]],[[9,1,9,10,2,-10],[7,-7,6,7,4,6],[-7,5,7,1,1,8],[5,9,-5,8,6,2],[1,-10,5,2,-10,-5],[6,5,-10,-9,-2,-4],[-7,10,8,-5,-9,3],[1,-7,-2,-10,-10,6]],[[-9,-7,-3,-7,-1,-2],[-8,7,-2,-5,-8,5],[-5,-6,9,9,9,8],[-4,10,3,6,1,-3],[6,5,10,-1,5,2],[-1,4,6,2,1,7],[6,-9,7,-9,10,6],[-5,5,-6,6,9,-1]],[[-3,6,5,-10,-7,7],[1,-8,9,8,-2,-4],[1,10,-9,6,-4,-6],[4,-9,4,-6,1,3],[9,-1,-6,1,-4,-7],[4,5,-6,6,-8,10],[2,-7,1,2,-3,10],[10,7,4,7,9,-5]],[[-4,4,7,-3,1,1],[-2,-9,6,6,-3,-9],[1,7,9,-5,-5,6],[5,3,1,-8,-7,-10],[8,-10,-9,2,-7,9],[10,-9,-7,9,4,9],[-7,10,6,10,4,-7],[-9,4,-7,-1,9,4]],[[-5,-9,6,-4,-5,-9],[-4,4,-9,2,9,5],[1,3,-8,-7,9,-1],[1,9,2,6,-9,4],[1,-7,4,-6,-9,-4],[-5,9,-6,-10,8,5],[-7,5,-3,-5,5,-5],[-5,-3,-2,-1,-9,-3]],[[-3,-3,2,2,-3,7],[-4,-8,-4,7,8,4],[-6,-6,-7,1,2,2],[6,-5,-1,-2,-5,-3],[7,-6,9,-4,-5,1],[9,-4,7,-5,2,-1],[2,-7,6,-4,9,6],[10,-6,-10,8,10,-2]]], dtype = "int64")#candidate|6875|(13, 8, 6)|const|int64
bop_6876 = relay.bitwise_xor(var_6874.astype('int64'), const_6875.astype('int64')) # shape=(13, 8, 6)
output = relay.Tuple([bop_6876,])
output2 = relay.Tuple([bop_6876,])
func_6898 = relay.Function([var_6874,], output)
mod['func_6898'] = func_6898
mod = relay.transform.InferType()(mod)
var_6899 = relay.var("var_6899", dtype = "int64", shape = ())#candidate|6899|()|var|int64
output = func_6898(var_6899)
func_6900 = relay.Function([var_6899], output)
mutated_mod['func_6900'] = func_6900
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6907 = relay.const([[[-4.412793,1.066823,-9.503236,-3.144616,-9.781846,2.080479,-5.544276,2.155116,-2.829723,2.277019,1.842012,-9.112965,-0.570307],[-1.501082,8.794702,-3.271308,6.271721,-6.289422,-9.250282,-4.069287,-6.424491,-7.036738,-7.194163,3.516901,5.201294,3.226541],[4.325932,-8.090677,0.039353,6.182088,-8.932838,-3.528213,5.985454,-1.411701,0.738684,6.126394,-4.872477,-4.520228,4.148437],[3.119479,5.160607,9.403614,-7.119139,-2.187353,-0.458680,-4.878072,9.735433,-3.067080,1.895079,6.570333,6.085192,-0.605453],[-6.549561,-4.521425,0.282008,-4.123298,-5.842750,7.344432,6.578973,-2.244232,0.158173,0.620875,4.027568,-5.000902,-4.182630],[2.021802,-3.588011,6.990134,7.207035,-0.544554,4.085635,0.924908,-4.310234,7.414149,-5.800003,-3.921198,-4.975039,7.641467],[7.413251,2.675799,5.291375,-0.609318,-5.650258,-0.072828,9.105761,-1.231069,8.103902,9.856861,-0.923642,-9.178753,-2.985929],[5.566753,-2.986896,1.379930,-5.244967,4.619501,0.777206,8.125679,5.196047,6.449047,-5.025698,7.130904,0.454744,9.594079],[5.418790,6.500338,-6.000253,2.570219,9.270767,7.768628,9.698755,1.465276,-1.562638,-1.881249,-2.549429,-5.131654,-6.121761],[-2.740030,-4.854919,5.472953,9.527928,-4.713734,5.028684,-0.446358,-8.450634,-7.956931,-0.231715,-5.717233,-3.254348,-7.825286],[7.211684,8.117255,2.912916,8.965530,-2.594893,8.816953,2.209946,9.913141,2.486966,0.311354,0.426895,0.688370,4.921509],[-8.506721,4.967358,-5.143488,-7.622062,-5.097541,-7.329483,0.627071,-2.929174,-7.842178,-0.583484,3.270366,-0.667079,0.875958],[-9.442849,7.177622,7.504806,-1.843233,9.270876,2.548509,-8.902895,8.690870,7.715226,6.805511,4.168941,-7.072228,-8.513875],[-3.986266,-7.262815,-4.563825,-0.008122,6.987260,-3.324869,-0.922447,-9.442713,2.327004,4.998361,2.298835,3.295506,6.344077],[9.349106,1.277901,5.078812,-5.022272,0.233866,-0.507546,-2.358448,1.356072,4.170090,-5.587529,1.344438,7.034883,-0.539043]],[[-8.857984,1.145563,3.040011,0.517553,-9.945146,-6.582143,-4.250498,-8.763471,8.766762,-6.537042,8.460376,9.731333,-0.572327],[9.855330,6.373284,-8.911791,7.773726,6.885942,-3.768046,5.391815,5.589818,9.006788,-5.991280,9.911699,5.933067,-8.130475],[3.300537,-7.707017,0.670054,5.828878,-5.112093,-7.037204,-6.132333,-4.169170,-5.716141,2.262641,5.114220,7.056913,-5.979855],[7.186220,3.420968,-3.073986,6.119825,-3.389764,-1.702306,-8.530468,5.643013,0.051217,-8.792933,2.392757,8.835390,0.926397],[6.545221,-9.525347,5.328143,4.583198,-7.795741,0.373650,4.393042,-9.065209,-0.007805,-7.330683,6.686856,9.492180,8.890504],[-7.146526,5.785393,6.734108,-1.984603,2.871715,6.782332,-2.099070,-9.222838,-8.552326,7.367967,-6.949198,3.293838,-3.952344],[-4.044769,-7.564125,-5.032628,-0.351744,-8.770685,-2.367107,-8.557659,-7.835993,0.411004,4.617104,3.980424,7.085730,-9.538851],[-0.197684,-3.954365,-5.082488,-2.858064,-8.253251,0.288005,-3.576726,-4.247991,-3.372964,-6.496953,-5.855476,-6.886327,-0.233012],[4.418855,-8.199281,9.104597,9.369928,8.209639,-6.569756,2.884488,-2.271288,5.921862,-5.282257,-3.187863,-6.582189,-4.084039],[-4.698859,-6.360307,-4.153794,-0.129704,5.871588,9.857497,0.214706,-9.862146,-2.748610,-1.500460,-7.469058,6.578726,8.079321],[-8.649830,0.352053,-0.398902,6.784113,-3.056560,4.193117,-0.988073,-4.873569,2.280197,4.256161,8.858204,3.780262,-9.697415],[2.752790,2.803557,9.393364,7.499187,-5.615181,-9.214380,-4.925612,4.240970,2.573008,1.270660,4.482081,4.386256,-0.703868],[-9.115732,-2.238248,-3.637970,-7.190412,-9.037297,4.545517,-2.073565,-9.618704,5.696650,0.575511,-8.904446,-3.384136,-1.778388],[-0.768969,-1.641629,-2.765727,8.900248,-3.057781,2.620150,3.320628,-8.273166,9.459252,-9.027999,-9.509315,-7.166645,-7.226897],[-4.918150,-4.044876,-7.369916,3.637897,-6.743804,0.914754,-4.078109,2.461898,-3.205650,-6.694002,8.789903,-9.067434,4.081593]],[[7.729972,-8.089094,-0.597416,-9.556106,-8.413154,6.390504,-5.284841,4.465047,9.554542,0.635785,2.541119,6.819158,-3.121014],[1.301913,-3.859047,3.589065,2.879271,6.567234,7.036300,-4.460084,-4.484711,3.915054,1.278917,-0.224750,-3.856918,1.585089],[-1.548818,6.300759,6.975477,4.217381,8.452034,5.033787,-7.759873,-3.678246,1.905637,5.184780,1.614782,-0.542817,-1.205402],[4.667138,-0.253950,-0.465204,-9.287913,2.055995,6.444079,9.442577,-7.789270,7.474924,-4.696678,-5.813048,-5.033283,6.539685],[-1.106826,7.046174,7.170102,9.255890,1.361940,-0.198157,-0.818089,-8.445523,-4.222935,-4.307487,-0.702732,7.424635,-5.439925],[-8.882294,-0.702124,-9.375733,7.995713,6.164675,-2.729654,-9.677768,-0.006976,1.448362,1.896577,-2.405817,-4.635787,-5.220810],[-4.353710,5.748793,3.171155,-0.348735,2.175685,-6.071651,-7.784027,6.759944,-4.005088,-9.458705,-0.793527,2.753146,5.410534],[1.761215,6.105710,3.567682,-7.580724,-5.152218,-5.106462,8.503985,7.304081,8.391256,1.497653,-7.726767,-2.442763,-6.597030],[7.858418,-6.785541,-5.500923,-8.413582,5.411073,7.445483,-9.584634,9.947449,-6.682199,-5.759549,-5.907143,5.338669,0.947955],[-5.352399,5.989040,-3.726727,-8.966651,9.840850,5.564091,-7.798983,5.837791,-9.146851,2.182627,1.690033,-7.899086,2.639891],[7.705144,-8.689808,7.161012,-3.103423,2.706193,4.668477,-6.810591,-8.746267,-1.813154,-8.601714,1.681310,2.962301,0.795376],[-7.718287,-3.762701,-8.561288,9.871291,-3.309058,9.734122,3.401789,-4.689904,6.919775,5.026335,-7.351838,-2.797356,-1.662169],[9.612207,8.494325,-4.849815,-4.533183,5.998938,-1.260623,0.671346,4.108953,3.226763,3.775973,6.901105,-3.233524,1.308204],[-5.095880,-6.737497,3.653622,-3.272529,-4.347346,-3.098036,-8.105402,7.722436,-7.857382,5.295706,-3.202004,-7.685078,-6.692891],[-6.529850,8.488842,2.321431,2.628408,-2.474109,2.703236,6.127478,3.902614,-1.022428,-1.333059,-0.984490,-1.764613,-3.279151]],[[-0.771954,6.025927,5.727298,-5.844897,9.311403,-9.931569,2.387566,4.997148,-6.556847,-6.057889,-0.366349,2.709643,-3.008849],[-1.638418,2.284384,3.699321,7.617236,3.839532,-8.521730,6.786551,6.017005,6.567341,-5.204625,-0.075359,3.391498,-9.165310],[2.876295,-8.527148,9.041040,0.909169,-2.022342,1.386051,6.603937,-9.735553,-9.049778,9.421476,5.710664,-6.331548,9.341449],[-6.651686,2.096789,-7.963502,-2.170995,-7.342823,5.976123,2.613419,6.976890,-9.186484,2.842900,-4.404335,-6.542177,0.867083],[-2.768955,-3.037220,-3.319298,8.204177,5.933291,2.703242,-2.093117,-1.514735,1.981730,7.687531,-4.837664,3.959484,-1.015498],[4.864340,0.536500,8.252676,-3.807736,8.809182,-4.021458,-3.617509,-5.665496,-3.491180,9.239406,8.993913,-9.816938,5.541355],[-1.515988,-6.324277,0.969992,1.840241,-1.195359,-5.270742,-7.267142,-7.704672,-6.999784,2.321983,-8.411596,-5.976109,-2.976865],[-2.162532,-7.018015,1.741120,-8.379143,-4.619893,9.227293,-0.261442,-3.392039,-2.263035,-7.832933,1.573374,8.832664,0.486219],[-1.657233,5.823886,0.928317,2.193769,-6.315224,-9.843115,-1.253686,-5.448621,6.614519,-7.874391,7.314271,-5.603974,1.123423],[3.004927,-8.242216,-9.666182,-1.299091,7.182960,1.188053,8.646211,4.797662,-6.248852,-7.777147,4.591124,4.815893,8.733886],[-1.226731,-5.568875,-9.790775,-2.875860,-6.049609,0.414571,1.844684,8.267261,-4.577471,-6.013703,-9.353697,9.963148,3.065424],[-1.353141,-5.023656,3.141715,-1.586923,-3.253445,4.569235,5.083513,4.649764,-6.044454,-3.731232,2.644605,5.227475,-7.362876],[-7.131985,-8.476184,4.992009,-8.114442,3.645401,-9.397014,6.369118,-1.297297,-8.976786,5.873965,-9.926265,-8.971412,2.169253],[1.132445,9.329291,-2.789123,-6.680080,5.225136,-4.073525,7.312292,3.175179,9.852883,6.210423,-3.280101,6.112458,3.994859],[6.859471,-2.057091,-5.812786,9.714369,-1.206657,0.354545,1.766511,-7.490863,4.442425,8.123096,0.355603,1.425816,-1.788175]],[[-5.554933,0.936325,7.959661,9.777579,7.673974,-6.119807,9.682686,8.314445,3.502213,6.140243,-8.281081,2.751661,-8.046162],[-5.171063,1.752296,3.801152,-2.040487,-9.440397,8.161779,-1.271240,1.977742,-7.322874,5.575487,4.264458,-5.299972,-6.223666],[3.551623,-9.478617,-9.421130,-6.417226,2.816268,-1.572472,-6.040593,4.398720,-9.257821,4.706341,-2.126995,5.243344,0.451727],[-7.882654,0.687198,-5.936332,9.229560,-6.694279,7.743602,6.280642,-1.584567,-0.515478,-6.318560,3.184862,6.194217,-6.313600],[-0.926888,9.691855,4.189219,6.055413,-8.710059,3.535691,-8.646651,-0.227994,-9.443269,-9.713806,0.004454,-4.059332,-6.363850],[-6.010966,-6.221404,-7.466922,-0.500248,-7.548963,8.145457,4.406868,2.078122,7.888570,-9.562180,2.041567,-6.920843,-5.223346],[-5.929267,7.243650,-3.685919,6.727533,3.471338,2.277094,3.867210,9.975613,0.719782,0.463233,4.260917,-8.002464,-2.482505],[3.747232,9.747814,-0.892772,-8.977088,-3.125583,8.097038,2.553626,9.200497,6.716624,-8.101062,-5.729185,8.039564,-6.541998],[-0.099538,-0.721285,-8.527270,7.853978,1.796982,1.747225,-8.449396,-6.394486,6.109724,-5.389587,-3.042387,-7.979593,-0.510707],[-6.911774,-3.463640,-9.713914,0.093362,8.672888,-7.171274,9.116312,-2.387662,4.064797,3.695117,-7.564732,4.469343,8.808464],[-8.304994,-4.739613,-8.919483,-8.854469,0.476778,-1.329021,-2.754791,-3.115176,-5.114293,-0.853085,4.444703,1.068436,-5.940938],[1.869866,-4.608661,6.531736,-7.904618,5.898648,8.421124,7.015224,8.819130,0.500202,5.543095,-4.621548,-3.727800,-8.697120],[8.943585,-3.431334,-2.841936,2.880536,-3.422041,7.735428,9.211638,-2.309821,3.158939,6.582904,6.935987,-9.110979,9.398073],[-9.632350,2.477195,1.799148,7.601343,-8.760130,0.672748,-6.264268,5.494176,5.069459,4.323771,1.962857,0.381424,8.143543],[1.794531,-5.537684,-4.894957,-3.600912,0.705207,-6.739077,6.249330,-3.550214,1.434624,9.750645,6.320825,0.195408,-8.827361]],[[5.417953,8.063053,-5.914651,-8.010048,2.246972,6.053809,-2.276309,5.749983,8.667700,-7.915309,-2.269153,0.554680,-5.506482],[-0.266118,9.859212,-9.509736,-4.562413,0.653997,-9.241570,5.244959,-3.112854,-6.438813,-4.508182,-7.266107,-0.669069,2.017347],[-1.935100,-5.718398,1.758480,-5.710880,4.660834,7.047335,-7.508551,-7.502607,-4.240766,8.301339,1.039456,-6.494749,0.850519],[1.393438,8.975338,-2.707993,9.333914,-7.886000,4.931504,5.691357,3.470315,1.877249,0.482934,-9.941864,9.835140,6.090288],[9.019285,-3.272161,-9.304233,9.545754,4.595942,6.855314,-3.547081,8.542617,-7.851510,3.250927,-8.578296,6.326322,-5.827158],[8.396957,8.617110,-6.582460,-1.351312,-9.267009,1.771819,-9.622304,1.995985,3.026644,4.625426,-4.456156,-7.055208,0.134629],[-6.301920,-0.957568,6.579585,-8.588355,-8.741471,6.525175,-3.277993,9.885349,0.466668,-7.232929,0.469008,1.284197,-2.242931],[-7.688659,9.312737,3.230255,9.838757,-4.321581,-6.741595,9.893514,-3.518752,1.843735,-0.159074,-0.239397,7.640737,8.179360],[-4.918466,0.033546,-8.293381,9.869566,-6.866023,9.227796,7.102829,-6.344631,-0.593317,-6.231908,-7.856625,5.840323,7.596646],[2.555244,-7.011727,2.358832,5.174912,-0.115175,4.322583,6.874362,-8.727243,6.400613,-7.364990,5.487787,3.218670,2.125476],[-6.675213,0.212363,-9.538995,-6.569248,5.296541,-0.410432,-8.635337,-6.227421,-1.031435,3.414491,-4.925763,-7.925421,-3.248341],[4.848503,-3.553351,-8.748586,-2.290205,-5.711815,-8.329466,1.391997,-4.917742,-7.463024,-7.883331,-3.084545,-2.494274,-1.483140],[-3.158717,8.680195,-2.834048,5.602969,-4.930074,2.807359,0.610589,1.221016,-7.680475,7.341007,-0.282367,-1.525441,-2.148746],[-9.091426,-0.158299,5.230815,7.712889,-8.702670,1.944724,-7.392139,5.259051,-0.027333,8.469251,-3.129622,2.592194,5.831119],[6.983924,-1.939614,-6.472317,-2.007035,3.140450,-1.136032,-0.995387,3.703545,-8.654682,1.340168,1.290578,-9.837319,-0.817113]],[[6.222011,-3.150221,4.597815,-2.805461,1.607046,-5.090254,0.369987,1.878281,9.603402,-4.192652,1.360303,-2.136267,-2.682354],[8.943988,4.994847,5.965469,4.719261,8.061257,9.176188,-9.874107,-4.786358,-1.429946,4.377097,7.767792,-0.657170,5.029655],[-9.914547,-8.699230,1.309069,1.489872,5.837354,4.306856,-6.081285,-4.319104,-0.732150,-5.485154,1.287547,1.933169,-2.207494],[8.525725,-1.169688,4.306818,2.636987,-6.281876,0.342897,4.825474,-3.177298,9.810345,0.192399,5.928964,-9.704271,-0.857459],[-1.381054,-5.591253,0.895753,7.565836,-9.750657,-6.994887,8.067505,0.395567,1.024468,9.817642,6.135837,-6.300094,-1.670470],[5.676298,-3.499660,1.328852,6.614098,8.217836,2.636400,-4.856832,5.279284,9.409084,4.455728,7.147461,7.149863,3.457675],[5.893813,4.679738,4.732334,2.606869,6.382997,-0.619427,-5.895114,3.942294,8.168269,-9.698230,-8.166419,9.779600,-3.131752],[-2.480837,0.785409,-3.348789,-2.413266,6.127919,-8.377850,4.317324,8.297708,-6.675753,6.488621,8.065227,-4.846290,-6.443621],[-6.544151,-3.697986,-2.952957,-3.215641,-5.357806,3.956559,7.481561,-4.504552,1.730725,4.577118,-3.067520,-5.140476,2.185446],[-3.343746,9.545349,-1.223728,-3.987272,-2.620092,-1.187853,-4.039182,-9.885620,1.331805,-3.051270,6.483214,7.691480,-0.509307],[4.152384,9.509401,4.988059,-7.317631,-3.394144,-6.367380,7.237431,-8.716204,7.305209,8.763885,-9.355306,2.895710,-9.691203],[-8.007645,2.808085,6.697154,0.131611,5.463248,-0.608192,-9.210632,4.159379,0.364214,1.667195,-3.682769,7.330579,-8.688576],[-3.341799,-6.052983,9.841601,-4.305975,-2.785540,1.858497,-5.205778,-9.059837,-0.389458,-3.548122,6.595069,-4.598478,2.155764],[2.170736,-1.156878,-1.799283,-7.352463,-4.944183,5.929797,-8.993287,-9.130688,5.570109,7.127520,-3.827462,-8.014344,8.744066],[-0.170362,7.407522,-0.358117,-9.973787,-5.097893,1.325749,-6.737958,-7.322249,-6.047658,1.419996,-2.711923,9.215059,-0.654744]]], dtype = "float32")#candidate|6907|(7, 15, 13)|const|float32
uop_6908 = relay.sigmoid(const_6907.astype('float32')) # shape=(7, 15, 13)
func_6083_call = mod.get_global_var('func_6083')
func_6084_call = mutated_mod.get_global_var('func_6084')
call_6915 = relay.TupleGetItem(func_6083_call(), 2)
call_6916 = relay.TupleGetItem(func_6084_call(), 2)
bop_6918 = relay.equal(uop_6908.astype('bool'), relay.reshape(const_6907.astype('bool'), relay.shape_of(uop_6908))) # shape=(7, 15, 13)
uop_6921 = relay.sqrt(bop_6918.astype('float32')) # shape=(7, 15, 13)
const_6923 = relay.const([[[-2.029708,8.089126,-9.541614,-5.224354,0.860631,-6.933998,7.147445,9.182975,9.847165,8.613208,7.653885,8.444668,-7.202458],[3.930463,3.599827,-7.863361,4.868408,1.361354,-0.890597,-8.104108,-4.888314,-9.560070,-1.879388,-5.790306,-9.766401,3.714458],[-6.343823,7.309994,7.243355,-5.172383,2.030651,-6.456434,3.768197,8.000878,-6.160106,6.765714,-2.624986,-9.289277,3.977299],[-0.571702,-1.072569,9.317503,-7.668784,3.647957,-8.634583,6.721217,-3.935608,-3.559136,1.857450,-5.990667,-4.898510,6.195166],[2.766259,3.853896,-7.776980,-1.638125,4.252921,8.754693,-5.830301,2.442987,-1.797596,8.090812,6.955618,-8.554258,8.228273],[-0.332105,-7.281920,-7.829864,6.216303,3.378939,6.333989,-6.123828,1.058960,-5.276892,8.778062,-4.111084,-8.991676,-3.028206],[-7.828742,2.085711,8.199421,3.485528,7.608065,3.618925,9.444940,-3.826094,7.945219,-5.657006,-6.993487,-1.443979,-5.258961],[7.835400,-7.243412,-7.387151,5.112297,-5.586730,0.393490,-9.289109,2.742734,3.590013,-1.645153,2.263930,9.528215,3.037160],[2.978531,8.702496,-6.268995,-2.660896,-2.856112,2.139169,-9.769437,0.823920,2.749775,-2.936208,8.215118,-9.610324,3.565271],[6.484545,1.217503,-3.651443,7.988470,-4.077047,4.209800,-8.276328,-6.618547,7.859866,-2.318851,-6.488464,-0.200344,-2.186237],[6.803592,-2.514595,7.820516,3.680091,-4.014087,8.614651,0.561186,6.469770,-2.422094,-0.568479,-2.613496,-7.203418,-4.265714],[-9.876230,4.369718,0.126300,3.859939,-9.424050,1.092191,9.005189,2.555020,8.305939,1.735161,4.680131,2.991426,-3.101686],[5.117143,-1.080152,1.850099,2.962083,9.289104,3.328903,-7.130639,7.659753,1.523636,1.206565,5.876493,6.452574,8.797777],[8.210558,2.321136,-3.702045,-6.100535,-1.854998,-3.344714,-4.626168,-2.530902,-4.966328,7.770209,4.356721,6.668305,-0.364520],[1.809005,5.286137,-5.385265,6.945872,-0.675570,6.468365,-1.487866,-3.650291,9.668433,3.595782,3.516541,-0.231326,8.157532]],[[0.906347,-6.321002,-6.994369,-2.878066,-0.078406,-1.164894,-8.896253,-7.730938,2.924450,9.532357,0.363234,-9.824398,8.861300],[-6.634397,4.307726,2.849698,-1.718174,-7.417577,2.612284,-0.324234,2.427560,-0.964770,5.625671,1.434781,7.238643,4.800130],[8.070522,0.911166,9.942888,-4.727595,-5.358074,7.138666,7.814795,8.953062,-5.300809,7.188287,-3.771812,1.971819,-1.631155],[-4.647433,-7.315274,-6.223002,4.740762,-3.473930,2.473692,7.275780,-5.875302,5.710339,-5.891667,-3.136574,-3.297052,0.889169],[6.164973,9.511801,6.008890,-1.867226,8.680846,-2.599132,-3.539247,1.393824,3.020588,2.396205,3.105508,-8.786436,5.557166],[4.582566,-1.932507,-4.996101,2.718490,0.173448,6.079093,-2.950948,-7.833195,-2.886066,4.933493,-7.299604,-5.885445,-5.471474],[-1.494135,-3.641409,-5.125719,-9.013837,-8.132268,-1.669078,-8.821062,-1.806751,6.462656,-6.156691,2.541067,9.664362,-5.999083],[-4.297745,5.340811,-1.948492,2.092261,-1.872135,-5.999748,-9.776076,7.043820,6.074750,-6.769706,-9.712471,-0.904009,8.122108],[2.769686,6.332685,-7.223994,-1.170703,-5.748782,-2.156155,1.065736,0.988054,8.701359,-1.349542,5.183561,-0.911241,-2.129120],[4.354462,4.741915,-9.096326,3.247034,-8.022810,1.635791,-0.773814,6.459159,8.678779,7.631342,7.066724,-9.470398,8.146309],[2.607584,4.016209,-1.854073,-7.891017,8.990799,-2.703856,-1.886856,2.408192,-4.226022,-2.528801,-1.114058,-9.317564,-0.416409],[-7.784157,-2.453127,-7.302928,4.759683,3.168021,2.112409,5.006448,-4.135489,7.182853,-3.257443,8.465594,-1.568045,-1.956261],[5.958770,-9.380214,-4.203705,5.430064,7.029135,-2.173414,0.567624,-0.725138,-8.710035,-0.153437,-8.483485,9.602329,-0.001953],[9.948211,-5.422420,0.658620,-4.003599,-7.225228,-9.511539,2.051223,4.250387,-6.497323,0.482592,3.534823,-8.144237,1.242412],[-5.986865,6.648032,8.079957,4.055251,-6.750876,0.904580,0.042637,-0.166007,4.048479,0.920237,2.908199,-3.023969,-0.319140]],[[-1.990084,3.761336,4.124828,9.721681,-4.154563,0.869725,-4.749728,-6.779972,4.751416,8.200597,4.443635,7.291435,-6.211100],[-6.826599,-1.403490,-8.952204,5.865002,-3.686539,7.765215,8.662114,-4.396113,-8.330770,-1.996290,-2.461162,-5.622792,4.506132],[0.145711,-9.172689,-0.668310,-6.047783,5.234211,8.947026,-3.257838,-6.861263,0.092815,6.336121,-1.453631,3.023629,-2.858594],[-3.972679,7.472404,-0.487503,5.669260,-5.153694,1.400416,-6.446499,-3.294508,6.421108,4.541656,-8.001761,8.977566,-2.216968],[5.075173,-5.956482,0.632589,-0.739888,1.183526,7.236084,8.789084,-7.320032,-0.292729,-8.943643,-0.772226,1.508822,2.533293],[9.780630,9.550115,-1.714951,0.248983,-6.046809,-8.958094,2.521102,3.815084,-2.091038,4.749079,8.653961,1.886246,-8.487993],[9.960882,4.144186,9.625188,7.826839,-9.100416,-8.067602,2.731013,-4.502166,4.998315,9.067378,1.259223,-0.394973,-3.229381],[-9.665658,7.228369,0.306579,0.931172,5.595724,0.856097,8.669062,-9.161819,4.326492,6.237036,1.319968,-2.800028,7.747040],[-1.903907,-8.312024,-7.205965,-8.617480,1.766690,-8.866107,-2.194276,3.442335,5.745260,8.826989,-0.713936,8.584938,5.568186],[2.726483,0.843162,1.619588,-9.420045,-4.975048,-0.467515,-8.955272,-8.460807,-8.078634,-2.380538,4.849220,5.910592,9.076629],[5.855508,0.631449,-8.426138,-9.364537,5.373655,3.121115,3.234746,-0.306438,3.905151,7.518633,-1.058681,-6.802675,-8.732750],[-8.473925,5.025723,6.269449,-1.379050,8.369530,8.293127,-1.238802,1.667868,-5.282162,4.014059,-5.698360,5.468195,-3.982107],[-8.219114,-2.470287,-6.318373,-4.158590,9.913354,3.674813,-6.195436,-9.179189,-2.655177,-7.498238,-6.958012,8.611877,-7.664491],[-9.862864,6.968389,8.000031,-6.504558,-3.124765,-8.501959,-4.192758,0.739193,8.088366,-4.193987,1.968191,-0.672840,-1.291150],[8.677587,-4.435801,7.019915,2.183251,1.316542,-4.581748,0.283213,7.718293,5.999364,1.650457,0.643476,-2.938193,-7.685953]],[[-6.745167,-1.395733,5.273880,-0.057584,5.335108,0.744383,2.420792,5.452690,-1.732368,-4.063489,-1.562505,7.317422,-4.371097],[-8.962824,-0.872379,7.892745,2.123013,0.742204,0.504225,-2.982076,5.388846,2.987382,-6.339762,8.803884,0.185739,-3.315868],[6.299038,0.473478,-6.095216,4.837482,-3.047439,-0.863915,-6.270859,7.802254,9.748425,-9.733974,2.504580,0.027705,-5.976543],[-8.809799,6.527139,9.559709,-1.986210,-9.065167,-4.413281,9.383564,-7.022907,-6.485911,6.802982,-3.444484,4.303038,6.059848],[9.571458,-2.353161,5.947189,0.250664,-8.039800,-7.494163,-4.117280,0.113410,-5.071468,3.851363,-1.527887,2.682766,9.685724],[3.743003,-2.025785,3.907338,2.949247,5.932233,-4.123565,2.419319,2.793947,4.150726,1.503262,-1.953514,8.959445,-1.548819],[1.935471,1.217884,-4.731886,2.826824,-6.358059,-9.843316,-8.733552,-6.039179,-3.277911,8.200639,8.410609,2.425298,-4.255417],[-1.547407,-8.920979,4.667753,-7.859354,-7.349119,9.529181,1.108936,6.737446,-3.613556,9.062990,-2.206436,-4.491510,2.174045],[4.210319,-6.079487,-9.900901,7.780163,-3.041423,-3.854568,-3.958478,4.865729,-4.809716,8.997959,-4.585659,-8.922617,-9.207428],[2.874326,-5.349897,8.938616,-4.887335,6.245679,-0.605288,5.120813,-5.774769,-2.894998,-7.186404,-4.154537,-1.520199,-9.436296],[4.107346,2.759143,-2.859889,0.828629,1.237321,-4.716078,-0.811023,0.663376,-6.635704,1.788329,-8.064432,8.874902,5.018135],[-0.052055,3.874681,-1.258758,0.676590,5.917695,1.250486,-8.675321,3.700263,-1.079882,6.644708,-5.698708,-0.139818,-6.163533],[1.201919,1.654406,5.281217,8.784259,8.670814,-8.832994,0.372474,-3.672503,-4.368197,2.780219,3.309071,5.311928,2.714843],[-6.006584,-6.911654,9.236514,6.360599,-3.511807,-3.210661,7.631394,-9.613936,-8.307508,1.678398,-5.362682,2.648021,6.834410],[0.620076,6.000583,9.420296,-4.848306,-4.462147,7.341244,-3.432371,3.538277,2.377057,-7.121846,-6.184708,0.905687,1.661860]],[[5.836287,-5.796581,8.768439,0.052775,-7.090664,8.360482,-1.908518,-2.637876,4.523981,-7.144564,7.339790,4.290174,2.370618],[-1.711344,-8.844171,-0.105929,5.468664,-6.553237,-1.234329,6.644957,-7.463404,1.509117,9.247106,0.581722,-5.310915,3.382698],[5.082273,-7.935134,-2.219514,-1.850784,-9.098784,-7.784308,0.616728,7.387129,-3.658729,-7.454123,3.696580,-4.078985,-5.639818],[8.447689,5.039793,-3.809636,7.020598,4.700650,-2.539510,-4.879232,-1.058173,-2.976021,-5.738221,4.088768,-0.911875,9.543736],[1.399562,-4.660556,8.305435,-4.723485,-3.313411,-3.174535,9.112215,2.974298,1.648779,2.392659,-5.033559,0.511354,4.542878],[-5.999723,-7.409632,4.853393,1.349900,9.864523,1.831379,8.520656,1.755021,0.453101,7.701685,-0.857743,4.298821,-9.576773],[4.661424,-8.269482,-4.753159,-5.003193,-0.852912,-6.014589,-3.777448,0.070251,9.271779,3.836886,-5.135561,-6.583508,-1.863938],[-6.190210,-9.353122,7.655227,-0.719177,-2.264872,-1.196635,0.187568,-8.294242,-9.500495,-6.435359,-7.856713,-8.422231,-5.674313],[-1.010661,-6.854784,6.982621,-6.701754,9.100261,7.834366,5.003585,-1.508261,-7.939379,3.645043,3.703523,5.141337,7.555483],[-2.080918,-5.237709,-4.175864,9.852897,7.884602,0.902031,-9.155174,8.692088,-0.252707,8.245674,7.398177,-4.689566,-0.278930],[-1.971529,2.941184,3.130693,-6.295462,-1.905538,-9.955549,7.268223,-1.227728,-7.203783,-7.052204,-9.719854,-0.667139,9.517225],[-6.788856,-0.907526,-5.377280,-8.975637,-2.249228,7.216480,6.538034,7.537511,7.360116,0.869905,4.534999,-7.567540,-3.232703],[-7.159058,-5.036539,-6.753609,-1.858647,3.833228,4.733306,-1.790255,2.662454,-3.339487,-9.572881,-1.127939,1.522938,9.445493],[2.003957,-8.060166,6.683340,6.329009,-8.150134,-0.819093,-3.823272,1.996878,5.512904,-8.074206,8.133546,-3.012426,-7.476772],[6.374385,-4.780773,4.009037,-8.254723,1.734493,-8.273003,6.544231,-5.532311,0.204919,8.446025,3.428374,5.376052,3.202594]],[[-3.702357,-4.083632,3.633566,-1.996823,-5.262106,8.351025,4.091129,-5.458545,2.302614,2.754546,4.039040,1.432332,4.219959],[-8.101421,-0.943514,-6.281082,4.073396,0.439919,-4.824796,-3.204512,8.514815,-7.231316,3.434271,5.058797,-5.638146,-0.001996],[2.571241,2.625737,-5.522908,6.712508,0.922744,-7.395186,-2.704694,2.697230,2.828585,-0.018170,-2.802333,-1.570784,9.080989],[-9.761822,-7.810182,-0.455566,-4.810643,-8.282623,3.571552,7.258711,8.558400,2.576950,-3.147009,5.997406,-0.957165,-5.077236],[-2.321970,-8.227065,-7.610843,4.061481,-4.847499,9.587983,4.480237,3.138304,6.313536,-3.899027,-2.974471,4.122225,-2.746674],[9.152417,-2.710256,7.960137,-7.611976,-7.045374,9.944556,0.933208,9.208274,-8.477157,-3.793628,4.969453,1.379948,1.214199],[9.800846,-8.585361,8.611519,8.230675,2.249017,-1.615226,-5.727942,0.330243,-9.389927,0.892505,9.187198,8.457566,-4.800869],[4.131560,-9.508964,6.715264,5.174842,2.809187,1.163469,-6.619425,-4.245113,-5.790290,-1.505806,-0.963748,-9.765859,-2.239428],[2.759362,-3.026845,6.854280,5.446849,-8.332377,6.877190,-0.501424,-2.960874,0.481188,2.329242,9.660479,7.056125,9.100559],[-8.989998,7.286493,8.407093,-1.256271,-1.798873,7.999447,4.234715,5.736192,-3.538503,-7.792315,5.275072,2.897648,8.662772],[4.194142,-6.151208,-5.515794,-0.375041,-4.370121,-7.176954,3.134408,-1.952318,1.143727,-0.777582,-6.029941,-0.880327,8.257232],[2.269963,-3.298222,5.611211,8.481521,-9.155298,5.912682,9.546088,-9.680409,-2.933737,9.142276,5.452838,2.697361,0.822196],[-3.807491,-2.945216,1.181797,-3.456355,-8.562924,2.389248,-1.864062,8.337178,9.142905,8.307922,-0.081691,8.092481,-9.492982],[-5.563408,5.494305,7.583675,-9.202692,1.376322,4.255276,6.601258,-5.383990,0.246293,1.436172,-9.576476,-3.406553,-9.294433],[4.516857,-0.983136,-0.895742,1.556311,-4.545099,6.734098,-4.315280,-2.008428,0.842169,5.124395,5.002350,-5.846988,5.252609]],[[7.231000,-7.471757,8.136402,0.102256,8.989843,-7.014113,3.287866,5.348013,7.567057,-4.129891,-7.400405,-1.167243,8.998889],[-0.552457,-8.351214,-5.510004,2.780678,3.262779,-6.657118,-7.022467,2.133409,7.370929,6.254323,3.225023,-8.632896,5.699081],[7.479784,8.899144,6.026169,-3.646047,7.634232,1.898192,1.216475,7.975838,2.412519,4.451281,7.206969,-6.511204,-7.755611],[9.987499,6.155012,3.416780,-6.727362,9.350149,-6.716125,3.100764,-1.341482,5.121728,-4.882091,2.745576,-9.897293,-6.917962],[8.634378,9.220969,-5.637420,0.538181,4.580107,2.318642,1.261667,2.974966,-3.219435,7.032721,4.177996,5.757950,-5.791030],[9.249376,0.049835,-7.605947,-5.331565,-8.500301,-8.031963,-2.830710,-0.290833,-6.999908,-5.339206,-0.633340,-9.843259,5.261026],[-2.442973,8.361504,-6.025675,5.398265,-5.351850,-0.074303,2.843266,-2.386568,-3.871676,5.784344,-7.802442,-2.037722,5.532041],[5.253950,9.341755,3.853753,8.924550,-6.888915,-2.108487,-9.726752,8.195941,2.333552,4.403370,-4.053209,6.131227,9.016206],[8.901761,-0.700435,-1.379100,5.544403,1.205870,2.456249,0.089116,-1.943053,4.417974,6.774996,7.332204,-7.410047,-6.052731],[6.654479,-9.366833,3.469104,-2.694762,1.053857,2.321750,-6.801640,6.719834,-6.337695,0.801505,-0.134823,2.697791,2.893608],[7.568721,5.555297,4.233050,6.743872,8.968835,5.274344,-4.162655,-5.284866,4.420328,-9.830748,-7.095003,-3.067329,7.830196],[9.221994,-0.997416,-4.438213,-7.665671,6.671795,-7.994343,8.542671,0.553612,0.848881,7.511402,5.396310,6.145235,-6.171859],[-2.988905,6.961198,4.082748,-1.192507,-1.848942,6.701039,8.803597,-8.314951,1.568274,8.585493,-7.062084,1.761618,0.501185],[4.455407,-9.340196,-5.059475,-2.083040,5.470951,-1.053580,5.285797,-9.264480,5.309145,7.965394,2.562356,-6.640684,0.026360],[2.208124,-1.213216,4.598026,4.103059,0.118495,1.168936,-2.929729,-7.039098,-2.080403,2.099751,-3.071070,-1.394262,-9.440628]]], dtype = "float32")#candidate|6923|(7, 15, 13)|const|float32
bop_6924 = relay.not_equal(uop_6921.astype('bool'), relay.reshape(const_6923.astype('bool'), relay.shape_of(uop_6921))) # shape=(7, 15, 13)
bop_6930 = relay.multiply(bop_6924.astype('int64'), relay.reshape(bop_6918.astype('int64'), relay.shape_of(bop_6924))) # shape=(7, 15, 13)
bop_6939 = relay.bitwise_or(uop_6921.astype('int8'), relay.reshape(bop_6924.astype('int8'), relay.shape_of(uop_6921))) # shape=(7, 15, 13)
output = relay.Tuple([call_6915,bop_6930,bop_6939,])
output2 = relay.Tuple([call_6916,bop_6930,bop_6939,])
func_6942 = relay.Function([], output)
mod['func_6942'] = func_6942
mod = relay.transform.InferType()(mod)
output = func_6942()
func_6943 = relay.Function([], output)
mutated_mod['func_6943'] = func_6943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6942_call = mod.get_global_var('func_6942')
func_6943_call = mutated_mod.get_global_var('func_6943')
call_6944 = relay.TupleGetItem(func_6942_call(), 2)
call_6945 = relay.TupleGetItem(func_6943_call(), 2)
func_6512_call = mod.get_global_var('func_6512')
func_6514_call = mutated_mod.get_global_var('func_6514')
var_6973 = relay.var("var_6973", dtype = "float64", shape = (91, 4))#candidate|6973|(91, 4)|var|float64
call_6972 = relay.TupleGetItem(func_6512_call(relay.reshape(var_6973.astype('float64'), [2, 13, 14])), 0)
call_6974 = relay.TupleGetItem(func_6514_call(relay.reshape(var_6973.astype('float64'), [2, 13, 14])), 0)
uop_7014 = relay.cosh(call_6972.astype('float64')) # shape=(2, 13, 14)
uop_7016 = relay.cosh(call_6974.astype('float64')) # shape=(2, 13, 14)
output = relay.Tuple([call_6944,var_6973,uop_7014,])
output2 = relay.Tuple([call_6945,var_6973,uop_7016,])
func_7044 = relay.Function([var_6973,], output)
mod['func_7044'] = func_7044
mod = relay.transform.InferType()(mod)
var_7045 = relay.var("var_7045", dtype = "float64", shape = (91, 4))#candidate|7045|(91, 4)|var|float64
output = func_7044(var_7045)
func_7046 = relay.Function([var_7045], output)
mutated_mod['func_7046'] = func_7046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_7059 = func_5448_call()
call_7060 = func_5448_call()
func_5325_call = mod.get_global_var('func_5325')
func_5328_call = mutated_mod.get_global_var('func_5328')
const_7067 = relay.const([[2.455482],[1.312280],[-5.069616],[-0.659060],[-4.094533],[9.016977],[0.436813],[-4.080373],[7.613927],[-9.633332],[-1.849914],[-2.733337],[-1.373277],[4.005162],[2.953351],[-6.562159],[7.499719],[6.143840],[2.028050],[-1.282463],[-7.347825],[-0.281734],[-6.836190],[-9.328347],[-3.895319],[5.763308],[2.534368],[8.618151],[3.522605],[1.464045],[-8.450042],[1.162765],[7.009283],[-5.199605],[-3.120722],[-5.392848],[-6.283792],[-4.255065],[-1.098568],[-9.107994],[5.826275],[7.616474],[5.220448],[3.241680],[-9.897132],[3.076059],[-3.737878],[-3.320472],[6.849661],[-7.835181],[-6.005049],[0.032053],[0.343387],[3.784867],[-8.922587],[-2.036902],[5.872531],[-0.663379],[-1.655932],[-5.267336],[-2.179449],[-5.377686],[-1.320385],[-3.079257],[3.990649],[-2.997477]], dtype = "float32")#candidate|7067|(66, 1)|const|float32
var_7068 = relay.var("var_7068", dtype = "float64", shape = (1568,))#candidate|7068|(1568,)|var|float64
call_7066 = relay.TupleGetItem(func_5325_call(relay.reshape(const_7067.astype('float32'), [2, 11, 3]), relay.reshape(var_7068.astype('float64'), [1568,]), ), 1)
call_7069 = relay.TupleGetItem(func_5328_call(relay.reshape(const_7067.astype('float32'), [2, 11, 3]), relay.reshape(var_7068.astype('float64'), [1568,]), ), 1)
func_1022_call = mod.get_global_var('func_1022')
func_1026_call = mutated_mod.get_global_var('func_1026')
var_7088 = relay.var("var_7088", dtype = "uint32", shape = (30,))#candidate|7088|(30,)|var|uint32
const_7089 = relay.const([-6.721051,4.822737,-5.707578,-2.722853,-8.193777,-4.553490,-1.616519,-7.851094,-6.214217,-6.470326,-4.395175,-0.462429,0.297309,-4.038014,4.007740,4.531496,-2.267735,5.026251,-0.871502,-3.086150,6.285381,2.843606,1.849290,-2.903700,-5.743701,-4.091024,6.938439,3.956319,-2.813609,7.402021,-6.039439,5.159780,7.960501,5.521103,-7.194947,1.269543,-3.697542,-4.122934,-5.027693,-4.992462,7.417294,6.927909,1.765486,-9.169569,-6.608250,6.087575,-7.946530,8.830437,-4.508765,5.347379,-1.487207,-2.668862,-2.696534,-5.690879,0.306293,7.053472,-5.746620,4.593637,2.706759,5.218726,5.676384,-6.316312,5.544764,-6.471515,-6.299344,9.111799,-1.379091,-4.346963,-3.532890,4.106386,9.104661,-5.888303,5.493579,9.231984,9.330854,-6.758674,5.527245,-3.273952], dtype = "float64")#candidate|7089|(78,)|const|float64
call_7087 = relay.TupleGetItem(func_1022_call(relay.reshape(var_7088.astype('uint32'), [3, 5, 2]), relay.reshape(const_7089.astype('float64'), [78,]), ), 0)
call_7090 = relay.TupleGetItem(func_1026_call(relay.reshape(var_7088.astype('uint32'), [3, 5, 2]), relay.reshape(const_7089.astype('float64'), [78,]), ), 0)
var_7092 = relay.var("var_7092", dtype = "float32", shape = (66, 1))#candidate|7092|(66, 1)|var|float32
bop_7093 = relay.bitwise_or(const_7067.astype('uint8'), relay.reshape(var_7092.astype('uint8'), relay.shape_of(const_7067))) # shape=(66, 1)
output = relay.Tuple([call_7059,call_7066,var_7068,call_7087,var_7088,const_7089,bop_7093,])
output2 = relay.Tuple([call_7060,call_7069,var_7068,call_7090,var_7088,const_7089,bop_7093,])
F = relay.Function([var_7068,var_7088,var_7092,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7068,var_7088,var_7092,], output2)
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
	relay.transform.FuseOps(3),
	relay.transform.DefuseOps(),
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
