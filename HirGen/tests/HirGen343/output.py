import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_21 = relay.var("var_21", dtype = "float64", shape = ())#candidate|21|()|var|float64
var_22 = relay.var("var_22", dtype = "float64", shape = (5, 1, 1))#candidate|22|(5, 1, 1)|var|float64
bop_23 = relay.mod(var_21.astype('float64'), var_22.astype('float64')) # shape=(5, 1, 1)
bop_41 = relay.less_equal(var_22.astype('bool'), var_21.astype('bool')) # shape=(5, 1, 1)
output = relay.Tuple([bop_23,bop_41,])
output2 = relay.Tuple([bop_23,bop_41,])
func_47 = relay.Function([var_21,var_22,], output)
mod['func_47'] = func_47
mod = relay.transform.InferType()(mod)
var_48 = relay.var("var_48", dtype = "float64", shape = ())#candidate|48|()|var|float64
var_49 = relay.var("var_49", dtype = "float64", shape = (5, 1, 1))#candidate|49|(5, 1, 1)|var|float64
output = func_47(var_48,var_49,)
func_50 = relay.Function([var_48,var_49,], output)
mutated_mod['func_50'] = func_50
mutated_mod = relay.transform.InferType()(mutated_mod)
const_55 = relay.const([[[8.670335,2.095681,-0.477855,2.512219,-2.467091,-6.444396,-2.170897,5.522561,-7.147233,3.528008,-9.716652,4.051553,-2.289798,8.407194]],[[-6.283531,-7.607308,5.266202,-1.362888,8.076935,5.291416,-7.819776,-2.560331,5.608341,3.359091,2.464395,-0.587154,-9.897216,5.505865]],[[-7.650911,0.994979,0.392322,-1.490416,0.987959,-5.431772,-3.437451,-2.704064,-2.741702,-8.139379,4.650507,1.602310,-6.106852,-1.073126]],[[9.836203,-8.836455,-4.526168,-6.974899,8.870280,2.155265,-0.174814,6.227080,3.035951,8.742939,-1.222360,4.806424,7.544992,-7.400222]],[[1.387061,-7.068363,-6.838812,-1.054698,-7.852695,-6.757788,-2.585642,6.937712,-6.716840,3.363354,-6.943150,2.254668,-5.057157,-7.096662]],[[3.176172,-5.096867,9.407184,-4.316766,1.378153,5.362830,3.027224,2.176334,2.162656,-9.522390,4.872429,2.294033,5.703513,4.826390]],[[-6.173910,3.493595,-1.607216,-4.872081,5.325246,-1.286843,2.394493,-6.928776,6.973492,-8.720706,-9.318029,-8.633906,6.930300,-9.942335]],[[-3.721099,-2.258264,3.737469,3.744255,1.818737,-8.121692,-3.266682,1.863419,-0.397826,-7.995822,6.904752,-3.622163,-2.691423,-4.254413]],[[-1.415552,-0.255718,-3.459723,9.480975,-7.498294,0.086888,-4.856416,-3.475781,-1.434604,6.342367,-6.615103,6.059155,-3.798300,3.920436]],[[-9.088128,-7.880425,-5.806106,-1.054771,-5.100598,9.897928,-5.713638,-9.909877,-4.072726,2.840294,9.205777,0.160023,-0.155412,3.005294]],[[-7.149140,6.766488,-4.647902,5.276967,-9.017902,9.590972,-0.601197,-7.143835,-7.517731,7.940608,7.101794,1.011545,5.907878,-4.814530]]], dtype = "float32")#candidate|55|(11, 1, 14)|const|float32
uop_56 = relay.cosh(const_55.astype('float32')) # shape=(11, 1, 14)
output = uop_56
output2 = uop_56
func_64 = relay.Function([], output)
mod['func_64'] = func_64
mod = relay.transform.InferType()(mod)
mutated_mod['func_64'] = func_64
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mutated_mod.get_global_var('func_64')
call_65 = func_64_call()
output = call_65
func_66 = relay.Function([], output)
mutated_mod['func_66'] = func_66
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_70 = func_64_call()
call_71 = func_64_call()
output = call_70
output2 = call_71
func_77 = relay.Function([], output)
mod['func_77'] = func_77
mod = relay.transform.InferType()(mod)
output = func_77()
func_78 = relay.Function([], output)
mutated_mod['func_78'] = func_78
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_79 = func_64_call()
call_80 = func_64_call()
uop_83 = relay.sqrt(call_79.astype('float32')) # shape=(11, 1, 14)
uop_85 = relay.sqrt(call_80.astype('float32')) # shape=(11, 1, 14)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
const_87 = relay.const(0.053013, dtype = "float64")#candidate|87|()|const|float64
const_88 = relay.const([-0.066898,-3.163789,1.498594,-9.777823,2.046744], dtype = "float64")#candidate|88|(5,)|const|float64
call_86 = relay.TupleGetItem(func_47_call(relay.reshape(const_87.astype('float64'), []), relay.reshape(const_88.astype('float64'), [5, 1, 1]), ), 1)
call_89 = relay.TupleGetItem(func_50_call(relay.reshape(const_87.astype('float64'), []), relay.reshape(const_88.astype('float64'), [5, 1, 1]), ), 1)
bop_96 = relay.add(uop_83.astype('int64'), relay.reshape(call_79.astype('int64'), relay.shape_of(uop_83))) # shape=(11, 1, 14)
bop_99 = relay.add(uop_85.astype('int64'), relay.reshape(call_80.astype('int64'), relay.shape_of(uop_85))) # shape=(11, 1, 14)
bop_111 = relay.subtract(bop_96.astype('int64'), const_87.astype('int64')) # shape=(11, 1, 14)
bop_114 = relay.subtract(bop_99.astype('int64'), const_87.astype('int64')) # shape=(11, 1, 14)
bop_119 = relay.bitwise_and(uop_83.astype('int16'), relay.reshape(call_79.astype('int16'), relay.shape_of(uop_83))) # shape=(11, 1, 14)
bop_122 = relay.bitwise_and(uop_85.astype('int16'), relay.reshape(call_80.astype('int16'), relay.shape_of(uop_85))) # shape=(11, 1, 14)
func_77_call = mod.get_global_var('func_77')
func_78_call = mutated_mod.get_global_var('func_78')
call_123 = func_77_call()
call_124 = func_77_call()
bop_128 = relay.mod(bop_119.astype('float32'), relay.reshape(call_123.astype('float32'), relay.shape_of(bop_119))) # shape=(11, 1, 14)
bop_131 = relay.mod(bop_122.astype('float32'), relay.reshape(call_124.astype('float32'), relay.shape_of(bop_122))) # shape=(11, 1, 14)
bop_137 = relay.greater(call_86.astype('bool'), const_87.astype('bool')) # shape=(5, 1, 1)
bop_140 = relay.greater(call_89.astype('bool'), const_87.astype('bool')) # shape=(5, 1, 1)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_155 = func_64_call()
call_156 = func_64_call()
output = relay.Tuple([const_88,bop_111,bop_128,bop_137,call_155,])
output2 = relay.Tuple([const_88,bop_114,bop_131,bop_140,call_156,])
func_160 = relay.Function([], output)
mod['func_160'] = func_160
mod = relay.transform.InferType()(mod)
output = func_160()
func_161 = relay.Function([], output)
mutated_mod['func_161'] = func_161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_164 = func_64_call()
call_165 = func_64_call()
output = relay.Tuple([call_164,])
output2 = relay.Tuple([call_165,])
func_167 = relay.Function([], output)
mod['func_167'] = func_167
mod = relay.transform.InferType()(mod)
output = func_167()
func_168 = relay.Function([], output)
mutated_mod['func_168'] = func_168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_187 = relay.TupleGetItem(func_167_call(), 0)
call_188 = relay.TupleGetItem(func_168_call(), 0)
func_160_call = mod.get_global_var('func_160')
func_161_call = mutated_mod.get_global_var('func_161')
call_210 = relay.TupleGetItem(func_160_call(), 4)
call_211 = relay.TupleGetItem(func_161_call(), 4)
uop_217 = relay.rsqrt(call_187.astype('float64')) # shape=(11, 1, 14)
uop_219 = relay.rsqrt(call_188.astype('float64')) # shape=(11, 1, 14)
output = relay.Tuple([call_210,uop_217,])
output2 = relay.Tuple([call_211,uop_219,])
func_220 = relay.Function([], output)
mod['func_220'] = func_220
mod = relay.transform.InferType()(mod)
output = func_220()
func_221 = relay.Function([], output)
mutated_mod['func_221'] = func_221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_330 = relay.TupleGetItem(func_167_call(), 0)
call_331 = relay.TupleGetItem(func_168_call(), 0)
var_344 = relay.var("var_344", dtype = "float32", shape = (11, 11, 14))#candidate|344|(11, 11, 14)|var|float32
bop_345 = relay.logical_xor(call_330.astype('int8'), var_344.astype('int8')) # shape=(11, 11, 14)
bop_348 = relay.logical_xor(call_331.astype('int8'), var_344.astype('int8')) # shape=(11, 11, 14)
output = bop_345
output2 = bop_348
func_349 = relay.Function([var_344,], output)
mod['func_349'] = func_349
mod = relay.transform.InferType()(mod)
var_350 = relay.var("var_350", dtype = "float32", shape = (11, 11, 14))#candidate|350|(11, 11, 14)|var|float32
output = func_349(var_350)
func_351 = relay.Function([var_350], output)
mutated_mod['func_351'] = func_351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_379 = func_64_call()
call_380 = func_64_call()
func_220_call = mod.get_global_var('func_220')
func_221_call = mutated_mod.get_global_var('func_221')
call_387 = relay.TupleGetItem(func_220_call(), 0)
call_388 = relay.TupleGetItem(func_221_call(), 0)
output = relay.Tuple([call_379,call_387,])
output2 = relay.Tuple([call_380,call_388,])
func_389 = relay.Function([], output)
mod['func_389'] = func_389
mod = relay.transform.InferType()(mod)
output = func_389()
func_390 = relay.Function([], output)
mutated_mod['func_390'] = func_390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_220_call = mod.get_global_var('func_220')
func_221_call = mutated_mod.get_global_var('func_221')
call_408 = relay.TupleGetItem(func_220_call(), 1)
call_409 = relay.TupleGetItem(func_221_call(), 1)
output = relay.Tuple([call_408,])
output2 = relay.Tuple([call_409,])
func_418 = relay.Function([], output)
mod['func_418'] = func_418
mod = relay.transform.InferType()(mod)
mutated_mod['func_418'] = func_418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_418_call = mutated_mod.get_global_var('func_418')
call_419 = func_418_call()
output = call_419
func_420 = relay.Function([], output)
mutated_mod['func_420'] = func_420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_77_call = mod.get_global_var('func_77')
func_78_call = mutated_mod.get_global_var('func_78')
call_429 = func_77_call()
call_430 = func_77_call()
output = call_429
output2 = call_430
func_435 = relay.Function([], output)
mod['func_435'] = func_435
mod = relay.transform.InferType()(mod)
output = func_435()
func_436 = relay.Function([], output)
mutated_mod['func_436'] = func_436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_435_call = mod.get_global_var('func_435')
func_436_call = mutated_mod.get_global_var('func_436')
call_437 = func_435_call()
call_438 = func_435_call()
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_486 = func_64_call()
call_487 = func_64_call()
func_77_call = mod.get_global_var('func_77')
func_78_call = mutated_mod.get_global_var('func_78')
call_488 = func_77_call()
call_489 = func_77_call()
func_435_call = mod.get_global_var('func_435')
func_436_call = mutated_mod.get_global_var('func_436')
call_493 = func_435_call()
call_494 = func_435_call()
output = relay.Tuple([call_437,call_486,call_488,call_493,])
output2 = relay.Tuple([call_438,call_487,call_489,call_494,])
func_496 = relay.Function([], output)
mod['func_496'] = func_496
mod = relay.transform.InferType()(mod)
mutated_mod['func_496'] = func_496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mutated_mod.get_global_var('func_496')
call_497 = func_496_call()
output = call_497
func_498 = relay.Function([], output)
mutated_mod['func_498'] = func_498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_511 = func_64_call()
call_512 = func_64_call()
output = relay.Tuple([call_511,])
output2 = relay.Tuple([call_512,])
func_523 = relay.Function([], output)
mod['func_523'] = func_523
mod = relay.transform.InferType()(mod)
output = func_523()
func_524 = relay.Function([], output)
mutated_mod['func_524'] = func_524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_568 = relay.TupleGetItem(func_496_call(), 0)
call_569 = relay.TupleGetItem(func_498_call(), 0)
output = call_568
output2 = call_569
func_573 = relay.Function([], output)
mod['func_573'] = func_573
mod = relay.transform.InferType()(mod)
output = func_573()
func_574 = relay.Function([], output)
mutated_mod['func_574'] = func_574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_609 = func_573_call()
call_610 = func_573_call()
output = relay.Tuple([call_609,])
output2 = relay.Tuple([call_610,])
func_614 = relay.Function([], output)
mod['func_614'] = func_614
mod = relay.transform.InferType()(mod)
output = func_614()
func_615 = relay.Function([], output)
mutated_mod['func_615'] = func_615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_643 = relay.TupleGetItem(func_496_call(), 2)
call_644 = relay.TupleGetItem(func_498_call(), 2)
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_648 = relay.TupleGetItem(func_418_call(), 0)
call_649 = relay.TupleGetItem(func_420_call(), 0)
const_655 = relay.const([[[9.162613,4.982536,-0.503687,-5.261146,0.787946,-5.464248,9.947723,-4.685168,-9.966862,3.078139,-4.072228,-7.235331,9.668700,6.401925],[8.177164,-6.785340,6.276563,8.231968,-5.354774,-4.321878,7.015168,1.318647,-5.816109,5.597583,-1.830423,9.013558,3.890714,-5.994477],[-2.711398,-5.640471,-1.566795,-3.085880,-2.234794,2.421848,-6.443544,-1.508938,-3.160211,-1.928174,9.774742,8.399440,-7.498075,1.983115],[5.235602,0.434109,8.442090,8.838381,-5.220249,2.306394,2.738850,4.531980,8.715933,7.017553,9.625922,-9.134981,1.265357,1.078918],[-5.264953,-1.225346,-7.222576,-0.207494,5.609140,8.239134,8.385200,-4.516879,-1.955316,-2.323216,6.247118,4.640781,-0.574212,-4.326695],[-8.687390,6.428630,-8.482201,-8.238194,1.341535,-5.740392,-2.892716,1.720343,-5.838392,6.183851,1.178958,-0.497766,7.381993,-2.597675],[8.813039,-2.500176,-4.984047,9.832953,7.201896,9.858432,-3.304685,3.616568,4.896702,-6.849501,-5.314043,-2.087272,-1.007077,-1.706925],[3.785938,6.554270,8.261463,-3.544138,3.135169,-5.330337,9.220161,-7.074080,4.788603,-3.950425,-5.927476,5.712467,-4.204790,-0.590307],[-9.313470,2.424776,8.773981,9.074398,-7.280338,-7.133558,8.020399,-2.932278,-6.382986,-7.629304,-4.341108,0.235474,6.197251,6.094673]],[[-9.176923,-7.983614,-6.775258,-8.320627,-3.795338,9.266558,6.974895,2.198094,-7.867413,1.046238,-6.779497,0.609954,7.098845,8.772957],[1.250528,-3.811632,-2.290938,-1.520708,-4.634706,2.659248,-5.302715,4.650822,-6.763408,-9.751396,-6.326647,-4.283981,9.326675,9.007731],[-4.462178,-7.272464,2.486669,6.835456,9.856455,6.649635,7.285230,4.464142,5.892266,1.275847,6.258252,-4.358887,-0.752138,-1.810993],[-4.138629,-2.844837,-8.466858,-3.840996,9.743248,1.517165,-8.144236,5.385902,2.943441,3.520772,5.051677,3.823803,0.262618,0.702112],[-2.969381,8.217901,1.845019,4.301527,-2.838330,-0.370274,5.222313,4.346880,-7.525775,5.614149,8.437696,-9.627020,-3.015810,9.166578],[7.344428,3.300246,-6.019586,7.475756,-8.441411,8.432392,-4.027643,-2.787379,6.088527,7.794197,-0.783156,-4.428494,-1.720097,8.070563],[-3.894544,-1.654397,3.579313,1.744535,-2.650048,6.248678,9.241327,-0.129580,-1.199971,0.005058,-1.047947,7.973701,-7.444180,-7.199658],[-9.322864,0.180713,-4.918703,5.912676,7.180020,0.303933,4.834330,-6.956538,0.414385,-5.325077,8.762176,9.479858,7.826173,2.452273],[-9.952144,-9.370183,3.139318,7.548219,8.619242,5.353142,7.308443,-1.637006,1.380191,0.410659,7.503501,6.595546,-2.571306,-5.561597]],[[9.214796,0.480036,3.664554,7.466080,3.856361,-0.529167,5.726561,2.196761,-5.781827,5.157413,-9.557854,-6.919345,-5.404829,-1.168460],[6.927956,-4.788833,-6.566586,-6.424811,3.602554,-5.261640,6.117314,9.930646,-8.708018,3.498518,1.451547,5.062325,-1.638691,9.320799],[6.031994,9.856135,0.903041,7.839199,9.557627,7.725182,8.618886,0.479081,9.429425,3.446372,6.450909,-0.953758,9.863854,-9.306112],[-4.668090,5.925831,9.669124,-9.282659,-0.460390,8.930790,2.254203,3.204411,-3.068508,4.568713,3.622396,-3.371156,-6.649782,3.807603],[-0.290193,7.746444,-9.662301,-0.404679,9.691078,-0.937913,-5.200714,9.859485,-9.618943,6.032059,2.692865,-8.103307,5.093222,8.917923],[-5.444172,-9.839002,-0.476507,0.740690,-5.844069,-0.128187,-7.309877,9.472222,-1.319702,-1.790528,0.646303,-4.487861,0.463719,-8.861102],[1.135025,-2.791524,-8.295153,-9.530168,-7.939576,2.203822,7.755002,-9.001831,-0.702897,-4.621307,-0.160140,-5.552987,-8.366105,-4.700788],[8.039535,2.628211,-0.204267,-3.419720,-0.197559,4.865491,-6.811444,9.739587,-9.780747,9.884613,5.466350,-7.939021,5.172756,-4.152754],[7.065849,0.214733,2.098954,0.532197,-0.938121,-6.927363,-2.098416,9.024668,0.338632,-3.943009,-0.409237,-6.243553,3.746125,2.441432]],[[0.979917,6.719651,-1.247470,-5.719114,1.576586,2.879444,7.909671,-1.704773,7.917610,2.232755,-9.416131,-4.505049,3.765117,-4.117411],[6.837388,2.171145,3.420111,3.834539,9.537596,1.635769,8.479961,-2.359989,0.826392,-8.053349,-9.124069,9.569155,3.545438,4.636871],[-4.569918,-6.608965,1.758694,5.881621,-4.036611,-0.798646,-7.700791,-6.582910,-7.290444,-6.806103,0.660526,-5.476005,-5.424904,-3.763262],[-4.328404,5.579179,1.104005,-2.330791,0.527202,-6.308031,9.590757,-1.952752,-6.635729,2.050493,2.980446,-7.451747,6.357463,8.027835],[-0.233601,1.765276,9.088681,-4.021084,-3.078142,-6.857760,-8.412379,7.471345,5.787851,5.787064,-6.679667,6.802835,-2.487413,-8.726440],[-1.280441,-3.676285,6.538625,1.110265,-7.943867,-0.516544,6.631432,-9.972786,1.642010,6.348054,1.026148,-2.815482,1.028566,-7.424020],[-7.345370,8.934162,-9.839111,0.590379,-8.095304,-4.219043,-8.980103,8.493568,3.985003,2.915545,-6.454664,-2.327155,3.763746,5.306199],[-7.155646,7.537245,1.769103,5.961626,-0.400573,9.352610,-9.385586,9.965307,-8.475949,-4.340466,-5.271200,-0.624163,-5.168265,7.429315],[-4.679796,-4.228381,-6.169618,3.740052,8.866349,4.105683,5.562916,-5.675109,-9.108025,7.519249,-0.153102,2.096642,9.923103,1.550001]],[[-3.758670,-4.979576,-0.424921,1.597410,-3.081001,-1.131052,0.998324,9.571952,-9.576244,-6.019962,5.457879,-8.587287,4.255797,-2.340155],[2.470021,-1.984440,-4.856317,-6.171851,-6.010870,9.630265,-9.468661,-9.664628,2.569232,4.825370,1.231897,5.742825,2.816138,-0.593420],[2.337463,8.823045,6.778233,-4.359960,-5.457672,-2.570703,-5.349937,2.520091,5.019273,-2.634967,3.073085,-4.566521,-2.646888,4.259245],[7.298505,-9.517408,8.667370,-1.615958,-5.672854,-3.316972,2.794782,8.603663,4.676986,4.134260,-1.991393,0.198384,4.361616,-4.722806],[7.108752,9.794900,4.244915,2.890263,7.822598,5.639930,-8.482981,4.091717,-3.931214,6.521091,2.906939,-9.552391,4.817344,-8.157907],[-5.435676,-2.741182,-9.931774,-6.610478,4.364798,-1.669493,5.413325,-7.733711,-8.963618,-1.284521,-7.740636,-7.084824,-2.508462,0.641612],[-2.251146,-3.657476,-2.966885,8.240906,-3.640216,5.991137,8.731357,-4.107427,3.148594,0.693201,-9.603281,6.852510,1.022221,3.188646],[-9.581253,9.618990,-8.568538,7.638266,-8.825454,0.224530,8.523973,4.235809,5.396872,9.689986,-4.177617,-9.572082,-8.173093,-5.795460],[5.120920,6.628716,-9.953540,-5.094822,-2.104191,-5.609872,-1.659230,2.905872,-0.864306,6.295399,8.921789,-1.909764,8.924323,-1.345330]],[[-7.022373,0.872817,-9.717616,-0.823313,-0.044031,1.547253,-2.814411,7.131935,-6.047460,-6.815732,7.519260,-3.551237,0.446783,9.732107],[7.336558,-0.977179,-0.248723,9.707291,0.636720,6.826776,-9.173918,-7.317507,-0.609045,-7.891408,1.269765,2.725538,-8.558205,5.341875],[4.757353,-1.421257,-2.263396,-8.578613,-0.481834,-3.519837,3.782564,0.009044,-7.632524,2.321759,-7.401037,1.837794,-8.653884,-5.952249],[-4.477593,-5.607012,-5.852626,-5.754890,-2.539564,6.704780,-4.675152,-0.153242,-4.424433,-0.874463,9.678016,3.337894,7.309789,9.840233],[-1.250379,-8.684129,8.795001,-2.336218,0.673203,1.181691,0.328801,-6.003436,-4.217871,-5.958492,0.948878,8.514547,-9.421442,-2.953772],[-0.054496,7.548722,6.679955,5.922290,9.570105,6.354055,4.653724,-1.300804,7.129178,-4.731114,0.679536,-1.208937,9.372392,2.081705],[6.686944,3.157471,-7.857717,-3.189183,-2.825089,-4.341213,2.744505,-8.072344,-1.615663,5.309248,-7.695697,9.854097,-6.216638,-7.124477],[-6.197977,3.683425,4.326307,8.822096,-2.519529,8.974806,2.133269,-1.295668,4.923153,1.852804,5.980897,-4.395456,0.731463,3.336848],[3.548735,5.104604,7.437416,4.444823,-1.350224,-8.518676,-8.987416,2.365488,-8.104321,-5.510421,5.106702,0.422538,7.063265,-6.699232]],[[-3.901043,-2.025496,5.126968,5.398282,9.522799,4.885009,3.386034,-8.346499,7.385019,4.801589,5.966989,-1.135061,-2.018855,9.231395],[4.140265,-9.535492,4.181914,8.273127,-4.326294,4.946574,-1.886478,8.171209,0.392128,8.166005,-1.635771,-5.668566,0.245332,-0.521213],[-8.734872,6.388220,0.729372,8.792750,-2.539556,5.583175,3.664322,-8.467732,7.011450,1.130467,3.087225,5.927876,-7.259180,4.287957],[-0.418172,2.692141,9.016691,-0.705732,-3.755956,6.550967,3.066599,7.842001,-5.223848,-4.327698,-4.249363,-1.292851,-0.721088,7.939894],[3.631450,-8.968737,-7.232112,-0.118747,-7.528225,-7.699346,7.129728,-7.047712,-1.077188,7.232871,6.527973,-2.704652,-9.132097,-0.137142],[-2.681079,0.745183,-8.053485,-3.948162,8.859990,8.741029,9.815217,-1.161118,2.352717,8.856618,-6.005152,-9.182404,-8.894858,2.191427],[2.043536,-1.061122,1.930991,0.202445,3.418278,-8.977269,7.001176,9.681526,1.557680,2.807154,-3.519260,-1.437413,8.464563,-8.966554],[1.208817,-8.244047,0.182195,8.289602,-9.763616,7.017382,-2.821042,-3.237360,2.702288,-5.234345,4.825224,5.905012,7.376627,1.417291],[2.701287,-8.503687,2.583482,8.488515,4.280909,-1.757051,-7.736684,-8.300122,3.809674,-5.769680,-2.979082,-3.231983,-5.010673,6.234950]],[[8.477418,-6.865714,-7.292002,-1.414115,-3.216496,4.658511,-0.099383,0.075962,8.709767,7.913106,3.945693,5.599544,-9.349585,5.171658],[8.729699,-6.395217,9.877635,0.837609,-6.235658,-8.718674,-4.799267,-9.587073,5.838123,7.211125,2.600139,3.125465,-2.267792,-3.150681],[-9.800974,2.074448,-0.021737,8.931271,-0.461685,-9.325144,-5.403730,6.265988,-1.106296,8.496859,-1.519851,-0.805977,4.764052,-8.586306],[-0.770125,-8.687256,-0.621246,-9.999060,-3.838907,7.759488,0.429975,4.716994,-5.872126,-5.475213,-9.727953,-8.100402,-6.543859,2.348807],[-5.294394,2.651814,-4.029806,-3.802897,1.891562,-5.112911,-5.581368,-4.367956,1.138362,5.431841,8.483390,-8.109803,0.675183,-7.965003],[1.842241,9.823332,3.946449,-2.399751,-6.053700,-9.738668,1.024557,6.330860,-6.971814,2.912242,5.887989,0.253585,-3.405499,8.878059],[-5.779684,7.216477,7.470204,-7.501132,6.486807,-1.293168,2.648994,0.985790,3.540326,-7.388611,2.816931,9.220237,-1.488485,3.268336],[-7.867895,-1.504423,-0.380022,-2.269371,-9.691119,-6.631031,3.223044,9.144891,7.218006,-1.746226,-3.267853,5.076735,-0.292660,-2.577790],[9.658419,-0.584249,-6.831374,8.312567,-7.383389,-5.447892,-4.339778,6.089683,-5.186783,-0.192644,2.626646,-6.727021,0.516053,9.208264]],[[8.992879,-2.267622,4.139270,-9.383154,1.283277,-9.307918,-3.099410,-8.918054,2.354715,-8.480563,-2.533837,-1.288043,4.231965,0.939046],[-9.760818,2.965343,8.497653,-3.708371,-4.469754,-4.977466,-5.863003,8.890982,-1.263746,3.528070,4.089211,1.888098,-9.919992,-5.960386],[-9.909002,-4.463884,-2.110346,-4.179895,9.886980,5.533927,-4.873045,8.050414,-8.891019,3.887322,-2.025680,9.680980,-7.830563,-7.258336],[-6.784944,1.868206,-3.674737,1.130292,6.144636,-0.123755,-6.870962,-9.735695,-2.876163,-3.115129,-5.235409,8.441848,-4.283787,5.757329],[2.953865,-8.495384,-6.643922,-5.267716,7.365095,8.323182,-0.043018,-3.441885,4.709028,2.438565,-0.132755,1.225260,3.491329,-9.521631],[2.095059,-0.654572,1.938863,-7.661880,-2.661946,-7.381454,-6.222993,-8.572716,-3.016917,6.791847,6.440389,9.537563,-8.626810,1.132433],[7.615450,-0.762361,6.263560,5.906102,7.414231,-6.635956,-2.641324,3.993795,-4.396843,3.737021,-3.509005,4.999542,6.082928,-9.416903],[5.844609,7.240847,9.975199,0.494911,6.945008,9.321525,-5.781401,-6.575256,-6.379648,4.455068,-9.606627,1.206191,6.863246,-8.805255],[9.467612,2.820688,-4.551899,0.992623,-9.510680,-4.827058,9.543234,-5.383721,1.072489,9.309478,-4.090845,6.068572,0.342432,-2.920593]],[[6.043641,-9.282649,4.740886,4.969030,-6.131356,2.298952,2.081662,-7.079547,2.892969,-6.227566,-7.909401,-7.328105,-4.253250,5.371198],[0.804426,-0.179822,-9.025410,4.470850,-1.451923,-6.306357,-8.899592,1.383196,5.034519,-4.920141,-6.992237,-1.943096,-7.821248,-7.640179],[-9.552429,2.020886,8.809063,-2.237409,-3.981117,6.775648,-2.290659,7.360912,9.591694,-1.858686,8.761190,0.822624,9.831055,-5.759490],[-2.515614,-7.530715,-0.443174,-9.169038,1.897552,4.147359,6.427379,6.323542,-8.422685,-2.583510,9.733076,8.081472,6.706346,4.254319],[-9.043593,7.622114,-6.401973,8.350082,6.407921,-8.134472,-3.494331,-7.958211,-9.559636,8.053033,-5.788377,-4.077765,-2.697831,-5.761434],[-6.912882,-4.769916,2.221137,3.599136,3.924232,-1.625886,9.003182,8.736236,3.166483,8.864291,5.185089,-0.231935,-6.674691,-0.222342],[-4.544698,-9.333800,-4.733779,9.819576,-8.233368,0.428910,4.282425,-8.476283,-0.267175,-4.335550,0.424156,7.695066,-0.460519,5.516253],[-7.700730,6.340659,-9.318567,1.520220,-3.307885,1.334439,6.244324,-3.410890,-0.247240,4.875292,3.521202,-5.705203,5.467878,1.373915],[-0.179415,-7.453899,-0.316500,8.314750,-6.604862,4.097159,-7.005237,9.285853,3.093793,-5.329816,0.486639,-9.016829,-6.542131,9.536775]],[[-0.220219,9.000331,7.991503,5.836568,-7.150097,2.284480,2.818730,2.294893,7.237965,-7.340259,6.240264,-5.896696,-2.122495,4.013752],[-2.891927,5.872455,0.433260,5.478257,-8.205005,9.437124,1.842046,4.835587,3.062513,-8.938707,-9.933130,-7.489742,-3.357598,-3.203308],[3.101751,0.438185,-9.811532,0.706239,2.371666,1.917911,7.097457,-3.833663,3.865923,-1.100417,0.764047,3.218584,3.258805,7.936031],[-0.632938,-3.648307,2.633417,7.369951,-0.898225,5.423159,5.188226,-2.739710,3.865879,-1.121525,-4.201409,-3.563682,5.805132,4.991797],[8.582278,-4.069907,-9.183046,0.848184,-3.326266,-4.567056,3.764446,1.740267,-3.387412,-5.038450,-4.645460,-1.387632,7.116173,-8.761382],[-3.821798,8.045105,-7.106846,8.546000,-7.915410,-6.149410,-9.018076,-8.325811,5.134537,-2.968278,0.742358,8.267938,0.105344,-5.039815],[-4.547488,-8.971742,0.844280,-6.135900,3.215610,-6.762036,8.945353,1.008354,5.118921,9.966323,7.285687,-0.001609,-0.459770,-9.909396],[2.715251,-9.791175,-9.812048,-6.227262,-3.468606,9.121078,7.382149,-6.995374,7.168586,-5.708170,0.823291,2.418298,5.281312,4.295248],[4.417680,-8.329985,-8.997681,5.296796,0.380719,-1.896403,-7.932846,1.733195,-0.588186,-5.959377,2.133214,-1.413099,9.190968,3.907081]]], dtype = "float64")#candidate|655|(11, 9, 14)|const|float64
bop_656 = relay.bitwise_xor(call_648.astype('uint8'), const_655.astype('uint8')) # shape=(11, 9, 14)
bop_659 = relay.bitwise_xor(call_649.astype('uint8'), const_655.astype('uint8')) # shape=(11, 9, 14)
uop_660 = relay.sinh(bop_656.astype('float64')) # shape=(11, 9, 14)
uop_662 = relay.sinh(bop_659.astype('float64')) # shape=(11, 9, 14)
uop_681 = relay.sqrt(bop_656.astype('float32')) # shape=(11, 9, 14)
uop_683 = relay.sqrt(bop_659.astype('float32')) # shape=(11, 9, 14)
bop_690 = relay.not_equal(uop_681.astype('bool'), relay.reshape(uop_660.astype('bool'), relay.shape_of(uop_681))) # shape=(11, 9, 14)
bop_693 = relay.not_equal(uop_683.astype('bool'), relay.reshape(uop_662.astype('bool'), relay.shape_of(uop_683))) # shape=(11, 9, 14)
uop_711 = relay.sin(bop_690.astype('float32')) # shape=(11, 9, 14)
uop_713 = relay.sin(bop_693.astype('float32')) # shape=(11, 9, 14)
bop_731 = relay.floor_divide(uop_711.astype('float32'), relay.reshape(bop_690.astype('float32'), relay.shape_of(uop_711))) # shape=(11, 9, 14)
bop_734 = relay.floor_divide(uop_713.astype('float32'), relay.reshape(bop_693.astype('float32'), relay.shape_of(uop_713))) # shape=(11, 9, 14)
output = relay.Tuple([call_643,bop_731,])
output2 = relay.Tuple([call_644,bop_734,])
func_735 = relay.Function([], output)
mod['func_735'] = func_735
mod = relay.transform.InferType()(mod)
output = func_735()
func_736 = relay.Function([], output)
mutated_mod['func_736'] = func_736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_435_call = mod.get_global_var('func_435')
func_436_call = mutated_mod.get_global_var('func_436')
call_794 = func_435_call()
call_795 = func_435_call()
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_805 = relay.TupleGetItem(func_167_call(), 0)
call_806 = relay.TupleGetItem(func_168_call(), 0)
bop_812 = relay.equal(call_805.astype('bool'), relay.reshape(call_794.astype('bool'), relay.shape_of(call_805))) # shape=(11, 1, 14)
bop_815 = relay.equal(call_806.astype('bool'), relay.reshape(call_795.astype('bool'), relay.shape_of(call_806))) # shape=(11, 1, 14)
bop_823 = relay.right_shift(bop_812.astype('int16'), relay.reshape(call_794.astype('int16'), relay.shape_of(bop_812))) # shape=(11, 1, 14)
bop_826 = relay.right_shift(bop_815.astype('int16'), relay.reshape(call_795.astype('int16'), relay.shape_of(bop_815))) # shape=(11, 1, 14)
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_840 = relay.TupleGetItem(func_523_call(), 0)
call_841 = relay.TupleGetItem(func_524_call(), 0)
output = relay.Tuple([bop_823,call_840,])
output2 = relay.Tuple([bop_826,call_841,])
func_848 = relay.Function([], output)
mod['func_848'] = func_848
mod = relay.transform.InferType()(mod)
mutated_mod['func_848'] = func_848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mutated_mod.get_global_var('func_848')
call_849 = func_848_call()
output = call_849
func_850 = relay.Function([], output)
mutated_mod['func_850'] = func_850
mutated_mod = relay.transform.InferType()(mutated_mod)
var_879 = relay.var("var_879", dtype = "float64", shape = (3, 13, 4))#candidate|879|(3, 13, 4)|var|float64
var_880 = relay.var("var_880", dtype = "float64", shape = (3, 13, 4))#candidate|880|(3, 13, 4)|var|float64
bop_881 = relay.equal(var_879.astype('bool'), relay.reshape(var_880.astype('bool'), relay.shape_of(var_879))) # shape=(3, 13, 4)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_886 = relay.var("var_886", dtype = "float64", shape = ())#candidate|886|()|var|float64
var_887 = relay.var("var_887", dtype = "float64", shape = (5,))#candidate|887|(5,)|var|float64
call_885 = relay.TupleGetItem(func_47_call(relay.reshape(var_886.astype('float64'), []), relay.reshape(var_887.astype('float64'), [5, 1, 1]), ), 0)
call_888 = relay.TupleGetItem(func_50_call(relay.reshape(var_886.astype('float64'), []), relay.reshape(var_887.astype('float64'), [5, 1, 1]), ), 0)
uop_889 = relay.cosh(bop_881.astype('float32')) # shape=(3, 13, 4)
var_892 = relay.var("var_892", dtype = "float32", shape = (3, 13, 4))#candidate|892|(3, 13, 4)|var|float32
bop_893 = relay.floor_mod(uop_889.astype('float32'), relay.reshape(var_892.astype('float32'), relay.shape_of(uop_889))) # shape=(3, 13, 4)
uop_907 = relay.atanh(bop_893.astype('float32')) # shape=(3, 13, 4)
uop_911 = relay.rsqrt(bop_881.astype('float32')) # shape=(3, 13, 4)
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_921 = relay.TupleGetItem(func_523_call(), 0)
call_922 = relay.TupleGetItem(func_524_call(), 0)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_924 = relay.TupleGetItem(func_167_call(), 0)
call_925 = relay.TupleGetItem(func_168_call(), 0)
output = relay.Tuple([call_885,var_886,var_887,uop_907,uop_911,call_921,call_924,])
output2 = relay.Tuple([call_888,var_886,var_887,uop_907,uop_911,call_922,call_925,])
func_926 = relay.Function([var_879,var_880,var_886,var_887,var_892,], output)
mod['func_926'] = func_926
mod = relay.transform.InferType()(mod)
mutated_mod['func_926'] = func_926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_926_call = mutated_mod.get_global_var('func_926')
var_928 = relay.var("var_928", dtype = "float64", shape = (3, 13, 4))#candidate|928|(3, 13, 4)|var|float64
var_929 = relay.var("var_929", dtype = "float64", shape = (3, 13, 4))#candidate|929|(3, 13, 4)|var|float64
var_930 = relay.var("var_930", dtype = "float64", shape = ())#candidate|930|()|var|float64
var_931 = relay.var("var_931", dtype = "float64", shape = (5,))#candidate|931|(5,)|var|float64
var_932 = relay.var("var_932", dtype = "float32", shape = (3, 13, 4))#candidate|932|(3, 13, 4)|var|float32
call_927 = func_926_call(var_928,var_929,var_930,var_931,var_932,)
output = call_927
func_933 = relay.Function([var_928,var_929,var_930,var_931,var_932,], output)
mutated_mod['func_933'] = func_933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_961 = func_64_call()
call_962 = func_64_call()
output = relay.Tuple([call_961,])
output2 = relay.Tuple([call_962,])
func_965 = relay.Function([], output)
mod['func_965'] = func_965
mod = relay.transform.InferType()(mod)
mutated_mod['func_965'] = func_965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mutated_mod.get_global_var('func_965')
call_966 = func_965_call()
output = call_966
func_967 = relay.Function([], output)
mutated_mod['func_967'] = func_967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_220_call = mod.get_global_var('func_220')
func_221_call = mutated_mod.get_global_var('func_221')
call_1000 = relay.TupleGetItem(func_220_call(), 0)
call_1001 = relay.TupleGetItem(func_221_call(), 0)
func_220_call = mod.get_global_var('func_220')
func_221_call = mutated_mod.get_global_var('func_221')
call_1010 = relay.TupleGetItem(func_220_call(), 0)
call_1011 = relay.TupleGetItem(func_221_call(), 0)
output = relay.Tuple([call_1000,call_1010,])
output2 = relay.Tuple([call_1001,call_1011,])
func_1015 = relay.Function([], output)
mod['func_1015'] = func_1015
mod = relay.transform.InferType()(mod)
output = func_1015()
func_1016 = relay.Function([], output)
mutated_mod['func_1016'] = func_1016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_77_call = mod.get_global_var('func_77')
func_78_call = mutated_mod.get_global_var('func_78')
call_1050 = func_77_call()
call_1051 = func_77_call()
func_614_call = mod.get_global_var('func_614')
func_615_call = mutated_mod.get_global_var('func_615')
call_1052 = relay.TupleGetItem(func_614_call(), 0)
call_1053 = relay.TupleGetItem(func_615_call(), 0)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_1059 = func_573_call()
call_1060 = func_573_call()
bop_1061 = relay.less(call_1050.astype('bool'), relay.reshape(call_1059.astype('bool'), relay.shape_of(call_1050))) # shape=(11, 1, 14)
bop_1064 = relay.less(call_1051.astype('bool'), relay.reshape(call_1060.astype('bool'), relay.shape_of(call_1051))) # shape=(11, 1, 14)
bop_1073 = relay.power(bop_1061.astype('float64'), relay.reshape(call_1059.astype('float64'), relay.shape_of(bop_1061))) # shape=(11, 1, 14)
bop_1076 = relay.power(bop_1064.astype('float64'), relay.reshape(call_1060.astype('float64'), relay.shape_of(bop_1064))) # shape=(11, 1, 14)
func_349_call = mod.get_global_var('func_349')
func_351_call = mutated_mod.get_global_var('func_351')
const_1080 = relay.const([-7.534490,-7.727093,-0.338986,9.342100,5.076356,1.991828,-7.864738,0.616232,-9.088537,-1.747727,4.788713,-2.404629,4.348559,4.343048,-4.446230,-9.188638,3.921260,-5.500817,-8.810339,-2.263262,-4.655395,-9.528152,7.825970,-5.860068,5.667378,-8.554653,7.540676,-3.789769,3.016386,-0.396810,-3.165657,6.602435,7.225344,7.762826,9.332699,-9.234594,-1.850256,1.920324,-5.270326,0.396771,-2.613622,-4.380375,-5.347884,-4.722558,-4.497653,2.453789,-5.105353,-0.679899,-0.395165,6.301466,3.821305,0.271709,-5.164053,-1.069816,-3.244445,-9.910838,4.051340,-0.886650,9.071455,-7.016423,6.668928,4.305167,-4.095069,-5.680319,2.012661,-1.015963,0.043013,-0.740178,-1.406552,-1.580384,-4.894077,9.043392,4.030386,5.980518,4.122961,-4.115424,7.475691,-9.507989,6.808790,-9.606653,-9.669082,-7.861976,-7.017853,3.426092,9.666599,0.846420,-9.468498,2.831387,6.130148,0.166596,-3.461304,5.104029,9.855381,0.904166,-2.302591,5.927519,6.207175,-1.537852,8.926579,-3.826135,0.963538,-2.540767,7.274475,5.016886,1.549468,5.090821,-3.748730,8.673452,-3.284220,0.579827,0.401178,7.713220,-5.504114,-2.745198,9.314871,-9.079193,2.867733,-8.834861,-3.511687,2.137204,-4.727079,-2.276783,7.856306,-8.004663,-1.818144,6.841373,2.430982,-5.366753,-9.161939,9.461572,-2.454600,2.059445,-9.907841,-0.699574,0.972480,-1.313408,-9.479014,8.285428,5.994646,8.791556,8.963192,8.999349,8.281791,-8.182525,-9.752607,4.288243,5.832207,-9.207783,-4.693093,-5.020731,-6.292583,-7.783241,4.989927,9.229184,0.549393,5.958848,4.161413,0.743051,-4.790376,-5.085099,8.733036,2.582581,-9.432364,4.515013,-6.307550,0.007485,-9.456592,7.617473,3.373094,-4.588818,0.221737,1.138268,-1.534457,7.313910,-3.183563,-2.723952,6.216141,-3.312863,0.704665,5.945091,0.155817,0.025588,-0.281331,-4.029042,5.409521,-6.218189,-6.564092,8.283389,3.188674,0.801174,-5.232495,3.676420,-9.937831,-3.657983,3.050262,3.948918,-0.473020,8.740115,-7.065512,-8.218513,-9.318094,-9.534750,-2.230899,-9.696891,6.446671,4.111952,2.748188,6.466739,-2.794659,1.524050,3.321784,-5.479020,0.710551,-3.388947,1.661811,7.845693,-5.559283,-2.880001,0.021541,-5.027778,9.582359,5.745939,-6.219355,-9.920196,-2.773385,0.781805,-9.305676,4.484974,8.950731,1.823065,-8.567665,-1.811615,9.693383,0.808059,5.755866,2.148958,1.338906,3.791743,7.197398,-7.010449,-4.758658,-5.287396,5.642360,-9.442127,3.097945,-7.285887,8.855958,-8.852039,6.671585,4.405568,3.046088,4.485650,5.968852,8.357435,-4.187040,-8.081665,3.907069,-1.141506,-4.965672,3.544396,-2.879403,1.723065,-5.884257,-6.319326,5.774662,6.006600,-6.348508,4.691311,4.213744,3.176613,-2.338767,-3.318117,-6.342872,2.724246,-4.598900,-9.897297,-1.127145,-2.339997,-3.699164,-0.952586,-2.195154,-5.489812,4.665112,4.448215,-1.642877,-2.209633,-1.038011,-5.367238,2.765124,-4.708834,-6.081829,0.944807,-0.738465,-8.881851,-2.561145,0.315858,-4.086210,-3.863731,0.988953,-0.427968,-3.605814,9.091638,-8.451054,1.023248,3.692307,9.915907,-1.822212,-5.660727,-7.941581,6.200015,5.266977,5.170492,0.800512,7.968717,3.963314,-6.903960,7.916568,7.007794,-5.436959,4.022955,-3.133093,0.781451,4.912727,8.369312,-1.968467,0.166304,3.732519,7.749836,-4.896887,-0.970323,6.929280,1.690392,-5.775651,-3.282945,5.170175,-3.145476,-0.360293,-5.574157,7.829250,1.579458,5.349292,8.485328,9.954245,6.519246,-7.705511,-7.652788,-0.782969,-5.105842,-0.126799,2.741806,-2.872629,4.066170,-2.348223,2.994905,5.059333,8.753269,0.755358,-7.475913,-0.206584,-7.044678,8.160467,-5.556240,-0.764504,-8.593367,5.360284,-2.686396,1.303754,-3.793182,0.317859,6.487123,-5.492362,7.925817,7.456083,-2.460391,5.017455,-5.362552,7.453906,8.902802,5.880799,-5.658952,7.199032,7.774842,-0.957756,-3.254021,1.338503,8.165746,0.755492,5.069408,-7.780031,-7.990894,-0.266138,-4.742026,5.118492,4.305686,3.132366,4.871932,-5.671334,6.274929,-2.059571,-7.617464,9.722895,3.298216,3.835444,0.910831,-9.248886,3.711040,2.097659,5.431409,3.437863,2.607658,-8.278030,-1.454653,0.822503,-7.587111,5.512167,5.430841,-8.293496,8.526828,7.249374,3.643809,-0.372906,-3.804816,-8.682077,-0.313387,-7.746757,-5.278571,-6.481988,6.056612,-4.592940,8.539527,3.350852,-7.562948,6.633490,5.910378,-3.785513,5.030059,1.969703,-8.690847,3.417861,-4.692729,7.045274,-0.303823,9.887251,6.950410,1.436170,1.819206,-7.999935,-3.895026,-1.714171,-9.359921,-8.912808,8.075174,-0.010229,6.994478,4.669220,9.951195,-3.401705,-4.686846,-1.147217,6.256345,9.009881,-9.370395,-2.835192,5.925622,-4.101456,-7.629906,8.889667,-5.040226,2.161311,2.763022,0.266731,4.906783,2.017116,1.917944,-0.819557,3.611605,-9.656839,0.683699,4.142228,2.998021,-2.068268,-2.090091,8.245466,5.207688,6.958040,5.689459,-8.629264,-9.545668,3.066486,2.784734,4.555726,2.586879,-3.527025,-1.637128,5.605629,3.840030,4.520749,-1.276388,-5.164018,-7.976348,-5.349662,8.141908,-8.676826,-1.075752,6.420289,3.998102,6.641997,-3.792455,5.053725,8.927481,-2.883665,0.638996,-1.786834,4.465561,1.612706,-0.157700,9.271984,-2.951140,-4.539058,1.827286,-8.565547,-5.767917,6.849862,6.977983,7.631088,-9.628194,9.585737,-7.022670,1.076892,7.966449,1.062112,-5.799185,6.268468,-8.178521,-4.268607,8.014496,6.700225,-4.387245,2.113324,0.601994,-8.942525,-8.591936,5.807759,6.861295,-2.011309,-4.842833,8.435080,3.168079,2.635863,-8.627924,7.358812,2.574420,2.203462,-8.825578,3.148154,6.340811,7.783252,-7.346564,-0.521808,8.094897,-3.973266,-4.960091,-2.359631,-3.237319,-4.266449,1.319151,-6.644062,-9.919212,-2.007790,-9.569508,-6.846578,5.413510,-6.094867,5.010169,-9.664303,9.939814,-5.514084,-5.841888,4.364160,-0.918631,7.323402,-6.828432,-9.244707,5.080697,6.503556,1.967841,0.193515,5.381907,-7.587432,4.225796,8.934664,4.275348,-8.237705,-8.390165,-9.720383,1.460768,9.544241,3.979716,-7.808864,-9.011894,6.357245,-2.559152,0.394322,-9.091794,-9.845767,-7.564254,-5.575074,0.322612,2.928519,8.837081,-7.718413,6.075671,-2.671858,-4.315864,8.298776,-4.403278,-8.421506,4.663130,-4.485732,9.160231,8.287334,-5.665562,5.378525,7.140502,6.356924,-1.373393,6.838977,0.865793,-6.223872,8.819295,1.420019,-3.607117,-8.360908,1.977701,1.091421,3.978997,-3.217016,0.112344,3.311615,-6.065179,7.763790,-7.515271,-0.208399,-3.950723,3.555916,-2.578861,4.186382,-0.445474,-7.075456,-8.567967,-1.862247,1.274941,7.828636,-9.694649,5.285008,0.308483,7.730106,3.462527,-8.324671,6.850457,6.336165,-9.386728,-3.429086,-9.373297,-9.845627,8.826880,-3.260351,7.249174,8.773222,-8.227873,-0.632738,3.638347,-3.956667,7.026059,-9.573344,-3.166333,-5.869856,-1.421964,-5.885852,7.739520,5.278246,1.813995,3.667053,0.635166,7.807709,4.438887,7.599597,2.129172,-1.647867,-3.560177,8.809516,-8.501911,5.058304,8.368604,-7.138486,-7.973129,8.625594,9.023011,-6.048834,0.869917,6.926223,7.215127,7.483872,-4.280891,3.864211,-0.428294,2.308131,-0.551252,0.995906,-1.331483,4.581689,2.324611,7.660650,5.796383,3.059292,4.315991,-3.597467,2.818751,4.295783,4.056134,2.542760,-4.178958,-5.132808,0.176278,-2.316499,2.122177,5.104341,-7.717499,-7.524577,-2.196580,-2.336085,-4.166158,0.596729,-1.115547,2.107489,3.569883,8.601289,8.785940,8.816742,9.057808,0.125925,6.422796,1.856253,0.060627,7.088751,0.446883,5.479714,-9.079435,8.835939,8.303299,-0.978178,0.815198,-8.725315,-7.986437,-0.655077,1.381923,-5.275485,-5.072100,-3.942545,8.193104,4.952197,3.447446,-2.233315,8.502091,-9.144575,-4.592464,-5.399190,-0.541282,9.524971,-0.476241,-6.407857,9.087957,-8.332844,-7.782815,8.989645,-2.602654,-1.490589,0.576469,-0.585369,8.194199,5.807649,7.692322,2.198429,1.077880,-3.914500,-4.833676,6.095842,-5.352137,9.624391,0.774346,-1.760518,-7.888196,1.798442,-7.677274,-6.707820,7.870778,0.913321,4.453234,-1.169020,0.667225,-0.072217,-6.071269,4.918675,5.019866,3.877333,5.008831,0.218281,9.049086,0.057108,-6.922004,2.268458,-3.987848,-1.943208,0.944299,-8.623176,-1.650579,8.012235,-1.826104,1.471198,8.116574,-3.684920,-0.848194,-9.286202,5.789124,2.428578,-3.956530,2.967851,-2.027172,-0.526714,-0.430326,-7.452331,-1.032021,3.522670,1.914989,-2.518202,-3.244543,7.816058,-5.149904,-9.363773,-0.463972,8.008901,-7.382874,0.808997,7.664149,-9.515006,-2.191882,-1.848051,-7.180437,0.809417,-8.953405,3.661306,3.883699,9.922614,-6.589865,3.204396,-3.247720,2.177853,4.981329,0.052409,7.635451,-6.437699,-7.290888,-4.074148,4.822788,-3.478320,0.525728,-7.911161,7.030849,6.995792,5.536647,-3.259565,4.854667,-0.830275,-2.087767,5.634129,5.779458,6.533150,-9.836388,0.344860,3.600066,9.946063,8.597061,9.716205,-9.957278,-4.340548,4.362167,8.113215,6.048514,5.101807,0.438507,8.161232,7.424208,-3.940701,-3.586350,5.282540,-9.268097,-6.564927,-8.436878,-3.762241,-4.408650,-4.361521,2.157938,0.155190,2.583300,-2.280341,0.418721,7.478781,-4.834613,1.742641,6.521870,-8.075838,2.238424,5.165175,6.529743,-7.394905,3.437359,3.128878,-5.542091,9.572737,-0.496594,-4.784089,9.771414,-0.547086,-5.367891,-8.209963,-8.590292,7.548039,4.465757,1.070741,-3.075985,5.298521,-2.749626,-0.978520,5.064693,-8.166864,1.720287,4.875026,-3.563344,-4.105227,3.384516,9.416629,2.990123,-3.682969,4.935260,5.351394,9.489943,1.628765,-3.480930,9.725845,4.606296,3.633999,-7.094420,8.253384,-3.905913,8.550394,-6.231347,8.701600,2.328553,9.960271,2.364393,-9.460059,2.339307,-5.312549,6.370608,8.632248,3.492702,1.034306,3.237610,-7.236789,-4.280842,-4.007633,-9.584841,7.454991,7.096429,5.512301,5.010234,6.314102,6.004760,-6.242096,3.433353,-1.701309,-4.124049,6.759042,-3.909346,1.099251,6.196483,-2.870984,9.211799,-1.563435,-4.156127,7.475560,6.928490,-9.097776,-0.625762,-1.676682,-6.183795,-5.281083,-7.001135,-2.765341,-4.182395,-3.547795,1.132933,2.365430,-0.814931,4.753682,8.736770,-1.203059,-7.178260,-3.524964,-1.286520,-2.606626,8.588966,4.594708,-4.420966,-1.531490,-5.631868,2.972774,6.487598,-0.620185,-1.081648,-0.966163,5.129915,-4.014669,5.974522,-8.461745,2.827780,-8.702105,-9.642924,0.502297,-9.467283,9.527688,-2.276629,-0.056242,1.001974,0.748446,1.524586,-7.715720,-9.997776,-5.858900,2.822643,8.854050,5.795318,3.512664,-1.483120,2.151261,-8.802371,2.477684,4.115190,8.558359,-2.917893,-3.139964,-0.989226,-2.977642,2.358173,3.765229,-6.718141,-4.307473,-8.302679,8.661324,-5.304609,0.023835,3.344903,9.095400,1.384665,7.433438,4.339098,3.495648,-4.190824,-0.279927,-1.170617,-0.375054,1.575460,-0.952315,-0.571524,-7.120660,-5.390850,-7.284731,-9.206734,-4.533520,-6.501820,5.859457,1.233636,3.454476,1.066290,-3.050352,0.579049,-7.716232,1.834775,3.563123,-8.278972,-6.034138,8.125844,-2.176023,-6.372994,5.125740,-3.680995,-1.408798,4.670824,-3.305424,2.879490,-0.889652,5.806902,4.708559,-5.461341,8.636227,-4.156678,1.521104,-6.186476,2.789878,7.598008,3.853655,-0.761209,9.036163,2.901089,-9.773850,-2.904556,-0.968232,6.396384,-2.498351,-1.558672,-0.154133,2.023077,-1.636426,9.350688,-1.036075,0.590765,-9.140905,3.176022,1.425388,2.167703,-6.396032,7.327646,-2.078388,-7.982891,-3.154815,-1.640810,-0.748124,-8.323777,2.257454,-4.924596,-3.692679,5.257297,0.966552,5.286681,6.183689,-3.509247,-6.830181,-0.192907,-6.447279,-4.430478,2.143319,4.502764,-3.645976,0.917768,4.421335,-3.611709,6.636490,4.971679,-2.496607,3.680351,6.438045,2.695589,3.357723,-5.406177,0.079294,-2.867866,6.752419,-9.480667,-6.413973,1.337555,8.871728,6.794093,4.425222,-0.479524,3.395380,-5.856248,6.196232,5.774278,3.551914,8.412491,-0.908568,-6.789386,9.389262,8.153620,-2.286183,-2.967954,-0.892530,-3.689182,-6.798964,-9.123277,-0.080999,-2.110625,-5.722242,3.699770,-3.300856,-7.722007,-4.108954,-4.951686,3.760848,9.376056,4.047639,-7.442290,-3.529953,8.969390,3.844899,-4.702473,-3.523294,3.772323,-9.723011,4.412052,4.145027,3.460406,-1.939337,-9.737221,-3.380698,0.711429,1.403525,3.259301,-3.774593,-5.466323,-1.047115,9.211021,3.966841,-4.058153,5.121271,-9.699647,2.277699,4.926499,-9.950607,-2.109412,2.251572,-5.674733,7.633135,-6.203071,-0.902142,6.200058,-2.921104,-6.752720,2.860250,0.150445,-9.367497,-2.921149,-7.317332,4.449122,0.759669,2.522704,1.976075,6.903827,6.703207,-3.140039,-5.316481,3.498603,-7.617512,-4.589936,-3.835385,0.005109,-6.067665,-0.090824,2.618520,6.927900,8.964961,6.950117,-8.056218,0.018555,1.245453,5.888029,5.053923,-0.143496,-2.015173,-1.019573,-6.519121,9.964794,4.162802,1.377946,2.338881,7.822125,4.726808,0.122951,6.585558,-9.473636,-2.337030,-0.220441,-4.053655,-6.314780,3.764652,0.159106,-8.457652,-7.487964,-9.742610,-2.111346,-9.440511,9.553099,-5.355696,6.580484,7.215982,-7.533805,-3.635330,-4.079411,1.307597,2.030081,8.939460,8.422273,-4.371675,8.163841,3.910922,-8.288789,9.233264,-5.541677,0.362247,7.171208,4.867897,-6.637367,-4.210377,-7.529143,2.530315,-8.810221,-9.083759,-4.600108,-2.720127,0.608250,5.226138,4.963462,3.305676,6.107306,-3.826858,-8.341701,-3.903227,1.038249,0.475972,1.779311,9.396073,4.425149,4.479888,-3.936943,8.713583,3.795057,-3.239498,8.228256,-5.179867,-8.019148,7.305841,-2.924756,6.054911,-3.476117,7.741991,-6.585745,6.676365,-1.055841,0.581903,-3.724459,9.096436,-6.776058,8.069973,6.368566,-1.279504,-3.093802,-9.628630,8.119038,-2.342356,-9.456481,6.777735,-7.535865,-0.393808,4.283343,-5.826572,-5.629730,-4.859014,6.731640,-6.301642,8.305879,-6.397959,-6.972920,4.527527,-1.553856,9.678924,1.297792,7.532203,-0.533547,7.755919,-0.076617,8.660852,0.372714,4.047269,0.996712,7.604247,-5.830747,-6.403711,9.871083,-3.704551,2.935594,-6.800421,3.608248,0.983198,-2.058265,7.132888,-0.663269,2.438269,-3.343005,-1.443011,6.622015,7.371724,0.136449,-5.705517,3.449673,-6.711435,9.810968,1.006950,2.403391,-6.072982,5.953696,-2.522381,-0.783255,3.345948,-2.600938,3.587365,-9.440851,3.753021,-2.909378,-9.748623,-4.951491,7.066839,5.353139,-6.084596,2.064381,-3.928417,6.848484,-9.806215,9.118536,-5.881717,5.475949,4.472115,-8.676957,3.217329,-0.913249,-8.108417,-7.548025,-6.956698,5.527869,-2.533268,3.589376,3.922289,7.452233,4.250957,-8.658472,-4.153916,1.959986,4.625283,-1.531753,-8.400340,-0.010076,-4.106325,-1.522613,-4.998380,5.655499,-5.799294,-2.053931,6.195026,9.855041,-2.336904,7.481029,3.579511,-6.905104,-3.256000,3.220522,0.905752,-8.780883,3.894904,9.724303,-5.616432,-9.593196,4.637552,-0.768214,9.458531,7.594121,5.685226,-7.059402,1.356411,1.054132,-1.518981,3.031763,-4.658369,3.030282,-5.494213,-4.547870,5.473246,-3.278971,8.433049,-9.225973,-2.467618,-3.614785,-3.949767,3.548851,3.971678,8.350750,6.974352,8.772284,-3.705595,0.036984,7.297886,3.624826,2.982264,-9.419205,3.005957,3.833663,-1.814482,0.507025,-7.327532,9.052733,-4.925227,0.671552,6.516172,5.079834,6.396028,-6.579842,-0.487052,-8.252603,3.884869,-8.744372,5.214385,1.622019,2.681406,-0.173295,6.143770,5.142548,-1.126897,1.852370,-6.304087,-3.949328,-5.973744,-7.003337,-5.346265,-3.815570,4.067891,-0.518713,-8.676757,9.420741,9.845154,4.285353,5.316619,-1.158926,-1.344462,0.571093,-9.904021,-9.025431,-8.208544,-6.234189,1.392223,4.081994,2.197274,1.093918,8.435935,-2.276011,-5.970880,8.744202,-7.988204,-0.254940,7.001612,8.702519,4.179241,-2.074380,4.259998,-2.141577,6.711478,6.614779,-7.268071,-3.858144,2.418148,-0.226812,0.615253,3.791273,8.896006,-0.636996,6.506431,-3.844743,0.151017,5.283300,9.922924,-4.609283,0.527501,-8.907077,-1.402953,8.109113,1.110654,-8.530968,6.035000,-9.797523,5.328512,9.086237,7.777210,1.417014,2.222595,3.869691,-2.670932,5.754986,0.831725,5.775752,9.091432,-4.089266,-6.224011,7.398017,-3.159567,-3.907499,-7.581606,4.751432,-8.888426,-1.654652,3.338842,-7.125001,3.871160,4.712726,0.482201,0.067096,7.804297,7.025082,-3.030197,0.702944,5.152913,-2.044316,3.211648,3.778875,-8.396456,7.339796,1.349993,8.895508,-1.831012,0.793074,-0.113931,-5.263527,-4.891326,9.972164,-6.762765,-3.362141,4.431204,0.108936,-3.405190,-6.346608,-1.160090,-7.092477,6.921490,5.129363,-4.768002,-9.937242,2.745715,-0.137198,-2.576392,-0.262666,-5.779478,-7.978252,8.373921,-0.478513,-0.286256,-6.946129,1.577397,-0.024310,-0.598867,-5.874481,4.789380,3.180343,0.234696,-4.454548,-5.097381,-0.716854,8.894349,-0.474236,-5.669304,-0.358221,2.178268,0.323656,3.497910,7.781960,8.346128,-6.781096,-4.448931,8.978494,0.997072,-6.418443,-3.708691,-4.581504,8.863938,-8.891621,-8.859276,8.347687,9.804402,-1.107344,-9.912661,3.400834,6.453464,-7.571272,1.115037,6.461943,-7.663439,-7.015651,-4.193088,-1.635810], dtype = "float32")#candidate|1080|(1694,)|const|float32
call_1079 = func_349_call(relay.reshape(const_1080.astype('float32'), [11, 11, 14]))
call_1081 = func_349_call(relay.reshape(const_1080.astype('float32'), [11, 11, 14]))
output = relay.Tuple([call_1052,bop_1073,call_1079,const_1080,])
output2 = relay.Tuple([call_1053,bop_1076,call_1081,const_1080,])
func_1083 = relay.Function([], output)
mod['func_1083'] = func_1083
mod = relay.transform.InferType()(mod)
output = func_1083()
func_1084 = relay.Function([], output)
mutated_mod['func_1084'] = func_1084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1093 = relay.var("var_1093", dtype = "float32", shape = (1, 7, 9))#candidate|1093|(1, 7, 9)|var|float32
uop_1094 = relay.asin(var_1093.astype('float32')) # shape=(1, 7, 9)
bop_1102 = relay.right_shift(uop_1094.astype('int16'), relay.reshape(var_1093.astype('int16'), relay.shape_of(uop_1094))) # shape=(1, 7, 9)
uop_1109 = relay.rsqrt(var_1093.astype('float32')) # shape=(1, 7, 9)
bop_1122 = relay.less_equal(var_1093.astype('bool'), relay.reshape(uop_1094.astype('bool'), relay.shape_of(var_1093))) # shape=(1, 7, 9)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_1125 = relay.TupleGetItem(func_167_call(), 0)
call_1126 = relay.TupleGetItem(func_168_call(), 0)
func_349_call = mod.get_global_var('func_349')
func_351_call = mutated_mod.get_global_var('func_351')
const_1128 = relay.const([7.867273,4.211951,-6.170973,4.666022,-1.129946,6.823297,9.186138,0.770556,-7.469156,-0.296757,-4.348925,4.777799,-7.785394,-9.966901,-4.624230,-7.066110,-0.168406,7.233552,6.342774,-1.838092,-6.088810,8.755363,-5.545416,7.144545,-4.600972,6.825274,5.904554,-2.759086,1.508581,-8.324384,-4.121418,-3.818497,-9.923694,2.119547,-0.144504,8.948918,6.831073,-7.655468,9.635563,-6.051000,1.512929,-6.328202,1.516744,-3.753912,0.070371,-5.492923,6.635557,3.792857,-7.105367,-5.160859,-6.847632,1.452353,-0.834994,7.511235,1.799535,0.139504,1.238949,8.059061,-9.317974,-0.235478,-4.488305,4.327152,2.538671,3.865242,5.722485,-5.332303,4.805908,-0.504382,4.283246,8.482522,0.176302,6.232155,-1.647687,8.051695,-3.379778,9.341738,-4.562962,7.505016,7.224550,1.096135,-5.372211,-3.300091,4.220157,9.100940,-5.071003,7.792852,1.353217,7.414779,-2.415970,-9.420792,-5.958626,4.166404,-3.619687,-8.249257,-1.022642,-4.703989,3.935297,-7.844609,5.516729,6.365632,2.231512,-0.122657,3.576432,-6.991287,-0.031797,-0.050528,-4.946965,-8.178168,-9.409999,-4.181000,-2.638489,0.917913,1.568257,1.517197,4.497735,9.200841,9.349159,2.521163,2.225180,-0.120837,-3.873474,-0.807588,5.843451,5.386934,9.673168,-8.414639,1.851493,7.847998,8.564525,2.229760,6.302741,3.475422,-6.016867,4.452736,2.323110,-4.645000,-7.847252,-4.154494,0.850705,-6.897831,-6.734884,-9.516605,-5.427851,-7.933258,-4.021460,3.054646,-2.322104,7.477949,6.876797,-1.718279,-1.869225,8.472739,5.107155,-0.331374,4.918608,3.656289,3.157414,7.488462,2.638403,-7.873354,-1.143510,6.576808,-8.378592,0.614725,2.548102,-1.783670,-4.814396,3.350835,-7.693727,-4.623209,-9.720330,6.145885,-1.952047,9.407847,-5.593811,2.366209,8.524526,-9.007563,6.729161,-3.545291,5.672895,5.336374,-2.818999,-3.468212,-2.032328,-5.515081,-4.511627,9.787899,8.786309,0.915650,-2.326026,-2.239130,6.357940,5.401870,-4.056280,-8.493340,1.379761,-2.437355,-2.631345,-1.552394,2.742714,1.335355,-3.369795,-7.437086,7.151225,9.501885,2.683634,-8.579059,-3.568103,7.814420,3.335042,6.449840,9.327405,-1.890347,-5.696792,7.116285,1.152129,4.195227,2.012673,3.457924,0.312817,-9.114397,-4.186517,-9.006397,-1.464168,-3.046158,0.734269,-5.095539,5.089236,-3.933840,6.761230,6.958158,-3.021345,-0.690763,8.904269,-5.894695,3.393000,8.851153,4.128616,-4.824246,1.598757,4.162785,-2.560297,-5.691647,-8.068190,5.907685,-1.875191,2.525871,-5.261316,-9.068767,5.266969,-8.404369,9.218477,2.059066,6.494514,-3.833652,-0.867112,9.070775,-6.565688,-7.729772,-6.564568,-0.839504,-8.295678,0.314976,-3.353033,-4.026422,2.387106,-7.010683,-1.103285,6.514010,1.525119,3.747142,-0.645239,9.672208,-9.630429,9.493343,8.531384,3.362106,0.384678,-2.446683,-3.117502,-8.792112,-1.711580,-4.737293,-9.012168,-1.632963,1.233046,6.648394,9.341299,-3.570432,-2.483606,-3.164865,-7.279047,7.704418,1.003716,6.865155,2.804646,2.056495,-5.248173,-7.648690,2.947383,-3.164808,-5.038034,-3.029499,-4.079340,7.649189,7.146500,4.413437,5.374194,4.571709,-9.347068,-4.846464,-0.494810,7.872847,4.362525,2.434103,8.633162,-0.832037,4.232118,2.387301,9.668869,-9.706930,-8.558603,-8.782036,8.031055,-1.906805,-6.991923,5.863343,-4.081192,8.448879,-9.045068,8.935165,2.720270,-3.857846,-7.625578,-5.361382,-1.650455,-2.303648,-5.117252,5.096135,2.751615,-0.666237,-1.008012,-7.238882,-5.085596,2.316749,5.854504,-9.173548,-8.536432,9.094609,-7.119758,-8.647105,6.175614,-1.210530,-6.503567,3.653327,8.400233,6.599415,7.474183,2.273108,-9.639238,-0.998195,4.239140,-4.545723,3.495473,-0.406354,2.123786,0.144083,-3.628256,4.866124,3.669356,-7.854412,-2.824798,-5.341478,3.757125,7.274342,-7.574463,1.287586,2.005709,6.699233,-4.498211,-1.043730,4.807175,-2.702956,2.345709,-5.561858,-4.613714,-5.015581,-2.165013,-3.250080,-0.210717,5.858176,8.481266,-1.011259,-8.793506,-6.224276,3.555389,1.463244,-4.236389,-0.148787,9.060714,-2.748537,6.607335,-8.999100,7.105541,-2.834600,-4.526968,5.469872,-2.026771,-3.364416,4.153321,1.979880,-6.758435,5.396864,-9.965172,-1.976768,-5.376708,7.506070,9.735546,-0.626340,-0.763365,-3.217272,-4.957721,8.027491,5.382486,-1.421200,-1.522693,-6.594594,-9.394473,9.292925,5.051421,-3.286850,-0.514290,-4.827064,7.838355,-5.221401,5.223266,-8.126112,-1.832415,-1.224834,-1.630591,4.681345,6.274606,2.576342,5.810586,-1.398786,-8.077060,9.298076,4.407359,6.947844,-9.222008,-7.849047,-5.851202,5.892446,-5.871670,8.839924,-5.653960,1.031007,-4.752959,9.873339,6.117133,-5.100520,-8.814204,-2.044595,1.663334,-2.478836,-5.129781,9.970767,-7.332486,5.412900,8.687728,9.449872,9.137490,4.764407,8.275957,-2.784792,-2.304517,-7.325211,-3.855475,-0.286143,-3.729842,2.722500,-6.888461,-5.544069,6.620302,6.205971,-7.696616,0.546236,-5.173048,2.750778,0.942881,-5.450109,-6.533803,9.743989,-2.099418,8.825897,-0.053436,2.425208,3.998310,3.989567,2.176851,4.986284,8.022656,-3.934343,3.844168,0.425900,4.502579,0.002272,7.407477,-5.915930,-6.316221,-8.585782,-6.778114,4.907699,2.093830,-9.162616,-7.897058,-8.833067,-9.282782,6.665017,-1.756462,0.727832,-1.756539,-6.277798,6.893827,4.462712,-4.351341,-5.963947,3.282381,-4.714329,8.445438,-1.839631,1.554870,3.228244,7.028495,5.998091,-4.779055,3.008127,8.112503,-2.306832,-5.097505,3.966529,4.463660,9.492298,2.301493,-8.600672,-2.742444,-9.939783,5.205959,-8.261345,-9.950639,8.914596,-4.843662,-7.246098,-7.025813,-2.796295,-5.833367,3.751662,4.786304,5.161743,-0.281962,8.125385,-5.443536,-2.406733,-1.456276,-4.474303,2.531201,4.232722,-4.817739,1.707688,-8.442929,0.668701,1.500060,-0.557044,4.228281,-4.311580,4.505963,-8.305991,6.209113,-4.286562,1.469380,6.328878,-1.431489,-4.173193,-2.881869,0.899860,4.123066,2.210426,1.811999,-8.871465,2.847645,-7.187440,-4.881078,-6.703995,-4.917208,2.945972,6.135305,-6.757495,2.223529,-1.870903,-9.029421,-0.595407,-9.730103,3.403593,-1.552342,-1.132546,-0.307293,-7.966606,-0.623829,-3.860302,2.327596,-8.452081,-0.705958,-1.897809,-0.911211,7.459792,-8.981229,-1.304182,-3.127607,-4.646710,1.265197,-3.860120,-3.687380,1.807249,-5.739403,5.308963,1.225399,-5.691912,-8.861627,-2.698460,-9.704107,4.722765,4.524895,0.868811,7.415154,-8.752882,4.644042,-7.270990,-1.772740,-2.704621,-4.783023,-8.657351,2.499572,1.483910,-2.419883,-2.084282,-1.389697,7.202115,-1.531861,9.387215,2.891062,-6.241750,-2.280645,-4.443692,-9.792680,8.578255,-7.737913,2.137813,2.327297,0.103708,-8.645009,-4.018930,3.343542,-8.397126,-7.402975,-4.902928,-7.820817,-3.591511,9.681231,2.616340,8.965089,-8.604235,-6.477530,-8.444451,3.200629,6.758148,9.488598,-1.559244,-6.564600,-7.385646,-6.865524,-1.461100,-5.140125,8.119029,6.003671,8.990956,-7.080010,-8.044683,6.637678,-5.372065,-0.447943,-2.996917,2.066655,-8.299411,-6.597517,-0.264306,9.631167,0.680609,-7.012554,-5.273521,8.656918,-1.207551,6.418110,-9.315447,2.166428,5.139502,2.663937,-8.084915,-6.317517,-6.526303,8.387691,4.647761,1.907003,-0.021118,-3.461219,8.535096,4.058605,3.086654,-4.510883,3.748939,-2.307209,7.149887,5.537750,-5.024984,-2.904263,-4.103827,7.715012,5.950718,-3.303248,-2.764706,-2.109941,-6.654845,-6.419818,-4.571749,5.816954,-2.733899,9.213820,4.418014,9.749433,-4.686274,-5.696210,-8.698704,8.285613,-6.161540,7.814019,-2.462642,-4.856778,9.568786,-9.263345,4.485750,-7.820579,8.152225,2.973765,-6.364085,-8.365109,2.093299,1.857455,-3.011504,5.835824,-9.267133,-8.586850,-4.961383,6.502886,6.868694,8.568052,2.992469,-3.280112,6.901617,-0.770621,7.242201,0.927277,4.990591,-4.757670,0.169492,2.452844,-0.244400,-2.074940,-4.068524,9.325623,1.897790,7.035421,-8.784510,6.500542,1.948577,9.130695,-1.639864,4.122357,7.468363,5.625794,3.227473,-4.939880,-6.947421,-9.825697,-5.559756,-4.926299,3.588773,-2.683933,-4.190102,1.292445,1.269941,-2.191804,6.123393,-7.949122,1.294568,3.204935,-6.575884,-9.534526,-6.338050,8.347624,-8.677253,-0.943395,3.650146,6.611869,-4.258866,-9.646295,9.020410,9.359343,-3.440397,7.468376,-4.543081,4.906310,-1.207633,9.726318,-8.780327,0.122816,4.806285,-0.742354,6.878929,-6.407675,6.544528,4.450672,2.210716,5.757864,-8.366131,7.745408,-3.931953,6.697678,-2.286594,2.334572,-9.416100,-4.118885,3.801348,-4.411824,-3.621212,-2.437236,1.663603,6.383681,8.651641,2.699980,5.827822,-6.161172,4.814192,8.089165,-1.601071,-0.071300,5.418839,-8.512102,-1.193794,3.048079,5.348214,-6.556642,-3.066742,3.021441,-1.125546,6.013114,9.374341,5.278555,-2.665191,3.985954,-1.601103,2.588064,-6.631747,-3.701481,-8.102334,6.462794,4.606091,0.974355,3.118935,1.529177,4.827725,-6.400923,-6.949182,4.111289,-5.428486,-9.549602,-2.635090,-1.389453,9.935120,1.830317,6.632551,-3.510603,-3.154620,-4.358795,-1.266182,-1.377242,-3.725178,3.838076,-3.229608,0.247583,1.054285,3.190585,0.860461,-7.605961,-5.980031,4.873714,-7.420853,4.398533,5.019341,8.356858,1.713362,4.832711,-7.057705,4.121354,2.419919,2.678287,-4.713507,-9.600847,-2.030031,-1.991051,2.922522,-6.946701,0.336761,-5.749526,7.400420,3.921046,3.501383,1.800230,6.613419,6.822458,7.195491,7.066195,3.553402,-9.056192,-3.217832,2.863308,-6.395024,7.413374,8.153942,-8.989215,4.347868,8.023462,-7.330173,-3.914832,2.334946,-2.613494,-9.708443,-5.972931,5.847587,-8.232139,-6.298501,8.279280,4.339922,-4.669726,4.445485,-2.967816,-4.394893,4.464793,-0.262259,-6.012711,1.772524,-0.557780,-8.081014,-2.059823,4.088109,4.908065,-9.790169,-8.319094,-0.793039,-1.353775,8.466647,-6.312553,-6.933309,-8.705470,-3.068549,5.695701,6.925170,3.889965,-1.398683,-8.364916,-3.977592,5.558266,-3.930090,9.063940,1.231602,-5.890069,-3.321508,-4.092401,2.925157,0.436137,-3.636529,5.955829,-3.827092,5.775334,-3.862222,0.608596,-7.226316,9.521817,-2.797334,7.828998,-9.215291,8.534958,-4.551485,-2.564199,-4.637754,5.812393,-9.673818,7.836549,-7.683093,5.940019,-7.793009,6.384924,-5.225465,0.974195,8.668466,-1.433526,9.464803,-2.893821,4.108793,1.618584,-7.105922,-9.948580,3.477843,-6.872296,2.800714,7.791693,-5.189781,-4.060171,5.490736,5.942595,-1.114793,6.314585,7.502854,2.437371,-8.520968,0.870397,-7.170218,4.797522,8.956127,8.087154,9.226744,-9.637503,1.699050,-9.191211,-9.919999,-1.477514,2.211941,-1.509159,3.336659,-9.810263,-6.785157,2.221158,6.415457,8.426367,-2.915528,0.907236,1.031905,7.978616,-6.569719,7.644619,3.476938,8.059006,6.985469,-6.087008,-2.430700,-2.509036,-3.634099,4.662181,-8.363575,-2.141776,5.716104,3.208921,2.771710,9.569690,-4.219211,-1.373046,-1.000480,8.348766,-3.247590,5.477611,-2.200908,9.794049,4.047793,-8.834121,0.459470,-5.640062,9.993526,5.068664,-1.157528,-6.752219,-9.713726,-6.576656,7.037681,-4.217035,9.840272,-7.106142,-0.339520,-9.640310,-4.789906,3.202936,4.253156,-8.202164,4.373732,8.037444,-0.557798,7.397816,1.094251,-5.808208,2.688036,-5.023788,-0.126113,-0.231733,-2.609909,-3.692146,0.960315,1.193121,2.311244,1.644019,2.403606,-3.016868,2.787466,-4.511503,8.589507,5.611879,-0.782201,-0.597201,-8.019253,2.939439,1.178247,6.942156,2.910183,-1.297488,-1.177277,-9.535104,-7.779114,0.633223,-5.661304,-4.940677,-5.865929,-6.976545,1.325573,7.853823,1.719175,3.526560,-5.911291,5.124673,9.918053,-7.320306,-3.605497,0.037276,7.312860,-3.943374,2.930004,-7.958236,-0.050256,-4.791003,9.757620,4.364792,-5.346622,3.732165,7.095607,-0.328311,-6.521424,-1.163913,3.526697,-0.198616,-3.147106,-5.328144,2.517705,-1.362451,7.308884,-6.318407,-5.887279,5.173047,-5.965781,-0.291566,-9.805628,-3.486121,8.453997,8.066624,-0.582899,-4.678893,-5.199625,-0.493779,9.570919,6.014199,1.636274,6.093379,6.382055,-1.753535,1.797592,9.737528,-3.884025,6.630406,-4.607435,-8.252147,-1.288292,9.236335,-1.654370,-6.892148,-9.921216,-0.773649,9.585709,-1.028284,3.269112,-5.651342,9.395375,-5.754490,9.940609,9.499444,-6.777034,2.228668,-5.218896,5.303083,-6.746329,-8.113485,2.917152,6.691702,-9.446142,0.122371,-7.533477,4.715273,7.056729,8.349038,7.560631,-5.951392,4.435615,-8.327366,-3.107311,-8.225451,5.940347,-1.760624,5.712190,-5.639206,6.428441,7.962125,8.366632,4.558767,-1.831484,-6.999084,2.850726,3.678742,-9.957060,0.174451,4.183787,2.229757,-4.560792,5.088390,2.297511,-8.420708,8.243119,6.929589,-7.967249,6.841180,5.442298,-9.402870,-6.052695,0.804183,7.077395,-0.796281,-2.459512,9.558800,2.422648,2.175542,-6.613763,7.125606,0.697515,9.039836,4.524814,0.083917,-8.354592,1.412580,6.737997,2.735754,8.394378,-8.350038,8.448344,1.489093,-8.532535,-1.107372,-6.364884,1.829309,-3.480382,6.368487,7.445253,-7.798491,-0.063227,9.537657,6.190262,-8.994251,-5.280626,-9.865355,-6.206108,-8.433911,-7.151806,-8.817452,-0.282394,8.902610,-0.576289,-2.613277,3.742938,0.280573,-9.659302,0.320378,2.821112,4.770885,-0.942379,5.476449,6.813581,-5.138370,-3.008012,-5.927627,-2.021477,2.017387,-6.422112,-3.626225,9.038691,5.090575,-4.023699,6.782268,-2.679916,8.197893,-5.835870,2.633764,-8.853528,-8.793267,-5.310594,1.114298,-1.832267,2.345582,-7.213744,-6.490393,9.067798,-9.622706,-8.269040,4.109868,-3.838591,-6.571475,-7.307111,-1.516843,9.699358,6.883872,9.535186,-3.610792,-9.554172,-0.265687,0.958179,-4.338354,-0.404832,0.589911,-7.103315,9.523387,6.575788,2.972679,6.389339,8.549684,-5.585132,8.583999,3.647636,2.856208,5.462685,6.245035,-1.196677,-0.488001,-7.357971,-8.534647,-9.741676,1.514471,6.636758,9.534937,-7.555298,9.198802,-8.771598,-5.388757,-5.904231,5.024211,6.390839,-4.799735,-4.784541,-7.737980,-3.328878,0.320203,-9.071538,8.473758,0.615236,-8.943695,7.666814,0.071013,-4.942116,3.112515,9.099859,0.250794,1.723101,3.097538,-1.078075,-9.301340,-6.922470,4.943777,-0.539780,-4.941864,-4.612176,1.231425,-6.120112,5.316322,-5.893974,5.981019,7.663891,-8.888292,-2.997300,-8.019583,5.913945,-1.544259,-1.495185,-3.332086,-5.106356,-8.879817,-6.348334,-0.426495,-9.437775,6.672074,-6.495400,6.153454,7.225224,8.186397,3.148132,-4.513331,-0.905485,-0.338844,4.738233,-7.603550,7.102511,-8.503447,-2.579907,-0.066304,-8.628326,-6.555378,-7.621328,-2.788894,2.661404,5.426265,8.155892,-0.106545,-4.935451,-0.581953,6.677119,8.609485,0.466299,-6.321590,-9.980959,1.008986,5.469120,-2.635540,1.891824,0.900431,-2.975081,4.515148,9.975514,7.998648,-8.289075,7.021553,-4.607347,-2.416095,-5.795939,-0.279253,7.256911,9.950392,8.142796,-3.369120,-3.104216,2.838240,-3.216021,-4.656939,-0.667798,-2.564821,1.658907,4.704660,-9.239836,3.988345,-9.643475,-8.744525,4.506415,-0.955042,3.855543,8.279896,8.988832,-8.865979,5.946605,4.308436,-8.460819,-4.887981,7.377511,-0.166209,7.543800,-7.982174,9.302448,6.923060,-5.867510,5.472784,-9.898440,5.285334,6.457776,-2.092905,-4.491512,8.408936,0.943071,-5.541343,1.586906,-5.712220,-6.737617,-0.065256,1.634068,7.319335,-1.172065,9.947814,5.683533,-2.746893,-5.834988,-4.086683,-0.875696,-2.536282,6.463063,-5.509490,2.697106,-3.189394,1.602720,4.703974,-1.576086,-9.240710,6.071608,-4.938639,-0.037376,7.864397,3.051649,9.620239,8.181556,9.646171,-6.743496,7.271404,-3.310458,7.808769,1.288612,3.333440,0.665817,-2.465627,1.276455,-2.094597,8.232571,9.401303,5.224381,-0.742049,-3.526028,2.275854,0.931582,-9.857154,-8.570067,3.772491,-1.440596,-3.711231,-8.501839,-1.257498,5.598822,3.749520,-1.764218,4.446246,4.620936,1.258222,6.456556,-4.034753,4.398659,-7.930338,-6.705404,1.146647,-7.059744,7.818799,-7.446757,5.539495,-7.205522,-4.559878,3.902053,-7.566847,4.083507,-8.862256,-7.527997,7.149954,9.640243,-2.534438,4.840382,-6.649244,4.566170,-8.793158,2.808632,1.643716,-2.605468,-6.020327,8.138588,-4.467157,-4.025738,1.887985,9.509081,8.489597,-9.887636,7.874494,5.499192,-9.819352,0.402725,6.613110,-7.729990,-8.747846,-8.898801,-7.097763,2.503284,5.101282,5.078717,-2.323899,1.090048,8.624338,9.881213,-2.048716,-5.016293,6.655199,9.072459,-0.531652,7.680656,3.180600,9.524802,7.063372,-5.857545,5.114539,4.760423,7.801769,2.000305,6.433846,7.859012,5.789242,-0.808243,3.502599,9.709832,4.714564,-4.794763,8.837917,-0.445208,-5.003708,7.682190,-1.370204,8.592801,2.737947,-2.157552,-3.940639,-9.435233,0.436719,-4.160989,5.837226,-7.648103,5.267620,5.296910,-2.511707,3.779206,-9.018984,-2.206581,-0.319870,-6.405308,-8.083814,-0.759632,-4.897351,5.328461,7.557325,-0.104151,5.965567,0.327755,2.355909,2.444147,-2.265910,-8.201568,6.994289,4.364560,2.079212,-3.229797,-7.792684,-2.579788,3.498736,-2.613094,5.910314,1.364279,2.723449,1.653937,0.764990,-8.970014,-7.139864,8.951528,-2.108850,1.885641,-5.011517,5.820461,-7.764431,-4.741969], dtype = "float32")#candidate|1128|(1694,)|const|float32
call_1127 = func_349_call(relay.reshape(const_1128.astype('float32'), [11, 11, 14]))
call_1129 = func_349_call(relay.reshape(const_1128.astype('float32'), [11, 11, 14]))
output = relay.Tuple([bop_1102,uop_1109,bop_1122,call_1125,call_1127,const_1128,])
output2 = relay.Tuple([bop_1102,uop_1109,bop_1122,call_1126,call_1129,const_1128,])
func_1132 = relay.Function([var_1093,], output)
mod['func_1132'] = func_1132
mod = relay.transform.InferType()(mod)
mutated_mod['func_1132'] = func_1132
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1133 = relay.var("var_1133", dtype = "float32", shape = (1, 7, 9))#candidate|1133|(1, 7, 9)|var|float32
func_1132_call = mutated_mod.get_global_var('func_1132')
call_1134 = func_1132_call(var_1133)
output = call_1134
func_1135 = relay.Function([var_1133], output)
mutated_mod['func_1135'] = func_1135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_1143 = relay.TupleGetItem(func_965_call(), 0)
call_1144 = relay.TupleGetItem(func_967_call(), 0)
func_220_call = mod.get_global_var('func_220')
func_221_call = mutated_mod.get_global_var('func_221')
call_1150 = relay.TupleGetItem(func_220_call(), 1)
call_1151 = relay.TupleGetItem(func_221_call(), 1)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_1154 = relay.TupleGetItem(func_1015_call(), 1)
call_1155 = relay.TupleGetItem(func_1016_call(), 1)
bop_1158 = relay.logical_and(call_1143.astype('bool'), relay.reshape(call_1154.astype('bool'), relay.shape_of(call_1143))) # shape=(11, 1, 14)
bop_1161 = relay.logical_and(call_1144.astype('bool'), relay.reshape(call_1155.astype('bool'), relay.shape_of(call_1144))) # shape=(11, 1, 14)
output = relay.Tuple([call_1150,bop_1158,])
output2 = relay.Tuple([call_1151,bop_1161,])
func_1177 = relay.Function([], output)
mod['func_1177'] = func_1177
mod = relay.transform.InferType()(mod)
output = func_1177()
func_1178 = relay.Function([], output)
mutated_mod['func_1178'] = func_1178
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1242 = relay.var("var_1242", dtype = "float32", shape = (10, 1, 5))#candidate|1242|(10, 1, 5)|var|float32
uop_1243 = relay.tan(var_1242.astype('float32')) # shape=(10, 1, 5)
bop_1260 = relay.bitwise_or(uop_1243.astype('uint8'), relay.reshape(var_1242.astype('uint8'), relay.shape_of(uop_1243))) # shape=(10, 1, 5)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
const_1271 = relay.const(3.849020, dtype = "float64")#candidate|1271|()|const|float64
const_1272 = relay.const([1.882989,-6.819719,0.745592,9.069762,-6.536786], dtype = "float64")#candidate|1272|(5,)|const|float64
call_1270 = relay.TupleGetItem(func_47_call(relay.reshape(const_1271.astype('float64'), []), relay.reshape(const_1272.astype('float64'), [5, 1, 1]), ), 0)
call_1273 = relay.TupleGetItem(func_50_call(relay.reshape(const_1271.astype('float64'), []), relay.reshape(const_1272.astype('float64'), [5, 1, 1]), ), 0)
output = relay.Tuple([bop_1260,call_1270,const_1271,const_1272,])
output2 = relay.Tuple([bop_1260,call_1273,const_1271,const_1272,])
func_1294 = relay.Function([var_1242,], output)
mod['func_1294'] = func_1294
mod = relay.transform.InferType()(mod)
mutated_mod['func_1294'] = func_1294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1295 = relay.var("var_1295", dtype = "float32", shape = (10, 1, 5))#candidate|1295|(10, 1, 5)|var|float32
func_1294_call = mutated_mod.get_global_var('func_1294')
call_1296 = func_1294_call(var_1295)
output = call_1296
func_1297 = relay.Function([var_1295], output)
mutated_mod['func_1297'] = func_1297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_1341 = relay.TupleGetItem(func_167_call(), 0)
call_1342 = relay.TupleGetItem(func_168_call(), 0)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_1343 = func_573_call()
call_1344 = func_573_call()
func_160_call = mod.get_global_var('func_160')
func_161_call = mutated_mod.get_global_var('func_161')
call_1345 = relay.TupleGetItem(func_160_call(), 2)
call_1346 = relay.TupleGetItem(func_161_call(), 2)
uop_1352 = relay.cos(call_1341.astype('float64')) # shape=(11, 1, 14)
uop_1354 = relay.cos(call_1342.astype('float64')) # shape=(11, 1, 14)
uop_1361 = relay.sinh(uop_1352.astype('float64')) # shape=(11, 1, 14)
uop_1363 = relay.sinh(uop_1354.astype('float64')) # shape=(11, 1, 14)
bop_1372 = relay.less_equal(uop_1361.astype('bool'), relay.reshape(call_1341.astype('bool'), relay.shape_of(uop_1361))) # shape=(11, 1, 14)
bop_1375 = relay.less_equal(uop_1363.astype('bool'), relay.reshape(call_1342.astype('bool'), relay.shape_of(uop_1363))) # shape=(11, 1, 14)
bop_1379 = relay.logical_or(call_1343.astype('bool'), relay.reshape(uop_1361.astype('bool'), relay.shape_of(call_1343))) # shape=(11, 1, 14)
bop_1382 = relay.logical_or(call_1344.astype('bool'), relay.reshape(uop_1363.astype('bool'), relay.shape_of(call_1344))) # shape=(11, 1, 14)
output = relay.Tuple([call_1345,bop_1372,bop_1379,])
output2 = relay.Tuple([call_1346,bop_1375,bop_1382,])
func_1425 = relay.Function([], output)
mod['func_1425'] = func_1425
mod = relay.transform.InferType()(mod)
mutated_mod['func_1425'] = func_1425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1425_call = mutated_mod.get_global_var('func_1425')
call_1426 = func_1425_call()
output = call_1426
func_1427 = relay.Function([], output)
mutated_mod['func_1427'] = func_1427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_1514 = relay.TupleGetItem(func_965_call(), 0)
call_1515 = relay.TupleGetItem(func_967_call(), 0)
output = relay.Tuple([call_1514,])
output2 = relay.Tuple([call_1515,])
func_1518 = relay.Function([], output)
mod['func_1518'] = func_1518
mod = relay.transform.InferType()(mod)
output = func_1518()
func_1519 = relay.Function([], output)
mutated_mod['func_1519'] = func_1519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_1542 = relay.TupleGetItem(func_418_call(), 0)
call_1543 = relay.TupleGetItem(func_420_call(), 0)
uop_1551 = relay.acosh(call_1542.astype('float64')) # shape=(11, 1, 14)
uop_1553 = relay.acosh(call_1543.astype('float64')) # shape=(11, 1, 14)
uop_1555 = relay.tan(uop_1551.astype('float32')) # shape=(11, 1, 14)
uop_1557 = relay.tan(uop_1553.astype('float32')) # shape=(11, 1, 14)
output = uop_1555
output2 = uop_1557
func_1560 = relay.Function([], output)
mod['func_1560'] = func_1560
mod = relay.transform.InferType()(mod)
output = func_1560()
func_1561 = relay.Function([], output)
mutated_mod['func_1561'] = func_1561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_1594 = relay.TupleGetItem(func_167_call(), 0)
call_1595 = relay.TupleGetItem(func_168_call(), 0)
var_1600 = relay.var("var_1600", dtype = "float32", shape = (11, 9, 14))#candidate|1600|(11, 9, 14)|var|float32
bop_1601 = relay.right_shift(call_1594.astype('int32'), var_1600.astype('int32')) # shape=(11, 9, 14)
bop_1604 = relay.right_shift(call_1595.astype('int32'), var_1600.astype('int32')) # shape=(11, 9, 14)
func_389_call = mod.get_global_var('func_389')
func_390_call = mutated_mod.get_global_var('func_390')
call_1613 = relay.TupleGetItem(func_389_call(), 1)
call_1614 = relay.TupleGetItem(func_390_call(), 1)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_1617 = func_64_call()
call_1618 = func_64_call()
uop_1634 = relay.tan(var_1600.astype('float64')) # shape=(11, 9, 14)
uop_1644 = relay.sigmoid(uop_1634.astype('float32')) # shape=(11, 9, 14)
output = relay.Tuple([bop_1601,call_1613,call_1617,uop_1644,])
output2 = relay.Tuple([bop_1604,call_1614,call_1618,uop_1644,])
func_1660 = relay.Function([var_1600,], output)
mod['func_1660'] = func_1660
mod = relay.transform.InferType()(mod)
mutated_mod['func_1660'] = func_1660
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1661 = relay.var("var_1661", dtype = "float32", shape = (11, 9, 14))#candidate|1661|(11, 9, 14)|var|float32
func_1660_call = mutated_mod.get_global_var('func_1660')
call_1662 = func_1660_call(var_1661)
output = call_1662
func_1663 = relay.Function([var_1661], output)
mutated_mod['func_1663'] = func_1663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_1673 = relay.TupleGetItem(func_965_call(), 0)
call_1674 = relay.TupleGetItem(func_967_call(), 0)
uop_1681 = relay.asinh(call_1673.astype('float64')) # shape=(11, 1, 14)
uop_1683 = relay.asinh(call_1674.astype('float64')) # shape=(11, 1, 14)
output = uop_1681
output2 = uop_1683
func_1686 = relay.Function([], output)
mod['func_1686'] = func_1686
mod = relay.transform.InferType()(mod)
output = func_1686()
func_1687 = relay.Function([], output)
mutated_mod['func_1687'] = func_1687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_1745 = relay.TupleGetItem(func_496_call(), 0)
call_1746 = relay.TupleGetItem(func_498_call(), 0)
func_1518_call = mod.get_global_var('func_1518')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_1750 = relay.TupleGetItem(func_1518_call(), 0)
call_1751 = relay.TupleGetItem(func_1519_call(), 0)
uop_1752 = relay.sigmoid(call_1745.astype('float32')) # shape=(11, 1, 14)
uop_1754 = relay.sigmoid(call_1746.astype('float32')) # shape=(11, 1, 14)
uop_1773 = relay.erf(call_1750.astype('float32')) # shape=(11, 1, 14)
uop_1775 = relay.erf(call_1751.astype('float32')) # shape=(11, 1, 14)
func_435_call = mod.get_global_var('func_435')
func_436_call = mutated_mod.get_global_var('func_436')
call_1821 = func_435_call()
call_1822 = func_435_call()
output = relay.Tuple([uop_1752,uop_1773,call_1821,])
output2 = relay.Tuple([uop_1754,uop_1775,call_1822,])
func_1823 = relay.Function([], output)
mod['func_1823'] = func_1823
mod = relay.transform.InferType()(mod)
mutated_mod['func_1823'] = func_1823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mutated_mod.get_global_var('func_1823')
call_1824 = func_1823_call()
output = call_1824
func_1825 = relay.Function([], output)
mutated_mod['func_1825'] = func_1825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_389_call = mod.get_global_var('func_389')
func_390_call = mutated_mod.get_global_var('func_390')
call_1911 = relay.TupleGetItem(func_389_call(), 1)
call_1912 = relay.TupleGetItem(func_390_call(), 1)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_1930 = func_573_call()
call_1931 = func_573_call()
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_1952 = relay.TupleGetItem(func_496_call(), 1)
call_1953 = relay.TupleGetItem(func_498_call(), 1)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
const_1960 = relay.const(8.037148, dtype = "float64")#candidate|1960|()|const|float64
const_1961 = relay.const([0.162721,5.707069,-6.495799,-7.764344,5.265585], dtype = "float64")#candidate|1961|(5,)|const|float64
call_1959 = relay.TupleGetItem(func_47_call(relay.reshape(const_1960.astype('float64'), []), relay.reshape(const_1961.astype('float64'), [5, 1, 1]), ), 1)
call_1962 = relay.TupleGetItem(func_50_call(relay.reshape(const_1960.astype('float64'), []), relay.reshape(const_1961.astype('float64'), [5, 1, 1]), ), 1)
output = relay.Tuple([call_1911,call_1930,call_1952,call_1959,const_1960,const_1961,])
output2 = relay.Tuple([call_1912,call_1931,call_1953,call_1962,const_1960,const_1961,])
func_1969 = relay.Function([], output)
mod['func_1969'] = func_1969
mod = relay.transform.InferType()(mod)
mutated_mod['func_1969'] = func_1969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1969_call = mutated_mod.get_global_var('func_1969')
call_1970 = func_1969_call()
output = call_1970
func_1971 = relay.Function([], output)
mutated_mod['func_1971'] = func_1971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1560_call = mod.get_global_var('func_1560')
func_1561_call = mutated_mod.get_global_var('func_1561')
call_2004 = func_1560_call()
call_2005 = func_1560_call()
output = call_2004
output2 = call_2005
func_2009 = relay.Function([], output)
mod['func_2009'] = func_2009
mod = relay.transform.InferType()(mod)
output = func_2009()
func_2010 = relay.Function([], output)
mutated_mod['func_2010'] = func_2010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2010_call = mutated_mod.get_global_var('func_2010')
call_2182 = func_2009_call()
call_2183 = func_2009_call()
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_2196 = func_573_call()
call_2197 = func_573_call()
func_735_call = mod.get_global_var('func_735')
func_736_call = mutated_mod.get_global_var('func_736')
call_2198 = relay.TupleGetItem(func_735_call(), 0)
call_2199 = relay.TupleGetItem(func_736_call(), 0)
output = relay.Tuple([call_2182,call_2196,call_2198,])
output2 = relay.Tuple([call_2183,call_2197,call_2199,])
func_2200 = relay.Function([], output)
mod['func_2200'] = func_2200
mod = relay.transform.InferType()(mod)
output = func_2200()
func_2201 = relay.Function([], output)
mutated_mod['func_2201'] = func_2201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2200_call = mod.get_global_var('func_2200')
func_2201_call = mutated_mod.get_global_var('func_2201')
call_2218 = relay.TupleGetItem(func_2200_call(), 2)
call_2219 = relay.TupleGetItem(func_2201_call(), 2)
output = relay.Tuple([call_2218,])
output2 = relay.Tuple([call_2219,])
func_2220 = relay.Function([], output)
mod['func_2220'] = func_2220
mod = relay.transform.InferType()(mod)
mutated_mod['func_2220'] = func_2220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mutated_mod.get_global_var('func_2220')
call_2221 = func_2220_call()
output = call_2221
func_2222 = relay.Function([], output)
mutated_mod['func_2222'] = func_2222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_850_call = mutated_mod.get_global_var('func_850')
call_2250 = relay.TupleGetItem(func_848_call(), 1)
call_2251 = relay.TupleGetItem(func_850_call(), 1)
output = relay.Tuple([call_2250,])
output2 = relay.Tuple([call_2251,])
func_2254 = relay.Function([], output)
mod['func_2254'] = func_2254
mod = relay.transform.InferType()(mod)
output = func_2254()
func_2255 = relay.Function([], output)
mutated_mod['func_2255'] = func_2255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_160_call = mod.get_global_var('func_160')
func_161_call = mutated_mod.get_global_var('func_161')
call_2324 = relay.TupleGetItem(func_160_call(), 1)
call_2325 = relay.TupleGetItem(func_161_call(), 1)
output = call_2324
output2 = call_2325
func_2326 = relay.Function([], output)
mod['func_2326'] = func_2326
mod = relay.transform.InferType()(mod)
output = func_2326()
func_2327 = relay.Function([], output)
mutated_mod['func_2327'] = func_2327
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2348 = relay.const([[[False,False,True,False,False,True,True,False],[False,True,True,True,False,True,True,False],[False,True,False,True,False,True,True,True],[False,False,False,True,True,True,False,False]],[[True,True,False,True,True,True,True,True],[False,False,False,True,False,True,True,False],[False,False,True,True,True,False,False,True],[True,False,True,False,True,True,False,False]]], dtype = "bool")#candidate|2348|(2, 4, 8)|const|bool
var_2349 = relay.var("var_2349", dtype = "bool", shape = (2, 4, 8))#candidate|2349|(2, 4, 8)|var|bool
bop_2350 = relay.logical_and(const_2348.astype('bool'), relay.reshape(var_2349.astype('bool'), relay.shape_of(const_2348))) # shape=(2, 4, 8)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_2391 = relay.TupleGetItem(func_496_call(), 1)
call_2392 = relay.TupleGetItem(func_498_call(), 1)
var_2395 = relay.var("var_2395", dtype = "float32", shape = (11, 6, 14))#candidate|2395|(11, 6, 14)|var|float32
bop_2396 = relay.less(call_2391.astype('bool'), var_2395.astype('bool')) # shape=(11, 6, 14)
bop_2399 = relay.less(call_2392.astype('bool'), var_2395.astype('bool')) # shape=(11, 6, 14)
output = relay.Tuple([bop_2350,bop_2396,])
output2 = relay.Tuple([bop_2350,bop_2399,])
func_2401 = relay.Function([var_2349,var_2395,], output)
mod['func_2401'] = func_2401
mod = relay.transform.InferType()(mod)
var_2402 = relay.var("var_2402", dtype = "bool", shape = (2, 4, 8))#candidate|2402|(2, 4, 8)|var|bool
var_2403 = relay.var("var_2403", dtype = "float32", shape = (11, 6, 14))#candidate|2403|(11, 6, 14)|var|float32
output = func_2401(var_2402,var_2403,)
func_2404 = relay.Function([var_2402,var_2403,], output)
mutated_mod['func_2404'] = func_2404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_2425 = relay.TupleGetItem(func_2220_call(), 0)
call_2426 = relay.TupleGetItem(func_2222_call(), 0)
uop_2430 = relay.log(call_2425.astype('float32')) # shape=(11, 1, 14)
uop_2432 = relay.log(call_2426.astype('float32')) # shape=(11, 1, 14)
func_1969_call = mod.get_global_var('func_1969')
func_1971_call = mutated_mod.get_global_var('func_1971')
call_2465 = relay.TupleGetItem(func_1969_call(), 0)
call_2466 = relay.TupleGetItem(func_1971_call(), 0)
func_1132_call = mod.get_global_var('func_1132')
func_1135_call = mutated_mod.get_global_var('func_1135')
const_2491 = relay.const([[-5.955034,8.857928,-1.406543,-1.401773,6.298685,2.085938,0.180532,-3.885056,1.287072],[-2.168249,4.389218,3.306749,-5.906677,2.246748,-9.505489,1.934518,9.114863,6.933010],[8.170271,1.967415,8.464834,2.210322,9.360241,6.946677,-2.304782,-8.612324,5.949371],[8.962634,-8.360594,1.438319,6.081658,0.712010,1.513955,-5.835759,-5.635950,5.062180],[-0.296647,4.662975,3.490335,-3.974083,-7.355023,1.450624,3.666425,-6.399436,7.672834],[-3.720165,-5.706264,2.122332,-3.475785,-2.913243,-8.340710,0.301006,-0.342634,-7.530147],[2.990634,-1.165620,-8.577522,8.354194,-0.893729,3.925068,1.722876,-4.812929,-7.858111]], dtype = "float32")#candidate|2491|(7, 9)|const|float32
call_2490 = relay.TupleGetItem(func_1132_call(relay.reshape(const_2491.astype('float32'), [1, 7, 9])), 1)
call_2492 = relay.TupleGetItem(func_1135_call(relay.reshape(const_2491.astype('float32'), [1, 7, 9])), 1)
bop_2503 = relay.bitwise_or(uop_2430.astype('uint8'), relay.reshape(call_2465.astype('uint8'), relay.shape_of(uop_2430))) # shape=(11, 1, 14)
bop_2506 = relay.bitwise_or(uop_2432.astype('uint8'), relay.reshape(call_2466.astype('uint8'), relay.shape_of(uop_2432))) # shape=(11, 1, 14)
bop_2510 = relay.left_shift(uop_2430.astype('uint8'), relay.reshape(call_2425.astype('uint8'), relay.shape_of(uop_2430))) # shape=(11, 1, 14)
bop_2513 = relay.left_shift(uop_2432.astype('uint8'), relay.reshape(call_2426.astype('uint8'), relay.shape_of(uop_2432))) # shape=(11, 1, 14)
output = relay.Tuple([call_2490,const_2491,bop_2503,bop_2510,])
output2 = relay.Tuple([call_2492,const_2491,bop_2506,bop_2513,])
func_2515 = relay.Function([], output)
mod['func_2515'] = func_2515
mod = relay.transform.InferType()(mod)
mutated_mod['func_2515'] = func_2515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2515_call = mutated_mod.get_global_var('func_2515')
call_2516 = func_2515_call()
output = call_2516
func_2517 = relay.Function([], output)
mutated_mod['func_2517'] = func_2517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_2551 = relay.TupleGetItem(func_1823_call(), 2)
call_2552 = relay.TupleGetItem(func_1825_call(), 2)
output = call_2551
output2 = call_2552
func_2555 = relay.Function([], output)
mod['func_2555'] = func_2555
mod = relay.transform.InferType()(mod)
output = func_2555()
func_2556 = relay.Function([], output)
mutated_mod['func_2556'] = func_2556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_735_call = mod.get_global_var('func_735')
func_736_call = mutated_mod.get_global_var('func_736')
call_2563 = relay.TupleGetItem(func_735_call(), 1)
call_2564 = relay.TupleGetItem(func_736_call(), 1)
func_2555_call = mod.get_global_var('func_2555')
func_2556_call = mutated_mod.get_global_var('func_2556')
call_2583 = func_2555_call()
call_2584 = func_2555_call()
bop_2595 = relay.left_shift(call_2563.astype('int8'), call_2583.astype('int8')) # shape=(11, 9, 14)
bop_2598 = relay.left_shift(call_2564.astype('int8'), call_2584.astype('int8')) # shape=(11, 9, 14)
output = bop_2595
output2 = bop_2598
func_2601 = relay.Function([], output)
mod['func_2601'] = func_2601
mod = relay.transform.InferType()(mod)
output = func_2601()
func_2602 = relay.Function([], output)
mutated_mod['func_2602'] = func_2602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1518_call = mod.get_global_var('func_1518')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_2608 = relay.TupleGetItem(func_1518_call(), 0)
call_2609 = relay.TupleGetItem(func_1519_call(), 0)
var_2627 = relay.var("var_2627", dtype = "float32", shape = (11, 2, 14))#candidate|2627|(11, 2, 14)|var|float32
bop_2628 = relay.greater(call_2608.astype('bool'), var_2627.astype('bool')) # shape=(11, 2, 14)
bop_2631 = relay.greater(call_2609.astype('bool'), var_2627.astype('bool')) # shape=(11, 2, 14)
func_2401_call = mod.get_global_var('func_2401')
func_2404_call = mutated_mod.get_global_var('func_2404')
var_2635 = relay.var("var_2635", dtype = "bool", shape = (64,))#candidate|2635|(64,)|var|bool
const_2636 = relay.const([9.694194,-6.628398,6.134910,6.401720,5.651529,1.819494,7.215647,-1.614516,-1.319318,-0.120687,5.855478,9.691843,1.087561,7.812788,-0.020819,9.022400,-5.969636,4.979810,8.990211,8.985122,-7.687235,-3.861694,-1.628517,9.019560,-8.656064,-8.205028,5.599168,9.091750,1.742616,-8.787325,-4.619582,8.825466,8.801442,-9.401263,3.373033,6.970212,-5.150391,5.958720,-9.832697,0.136703,-0.840665,-9.776904,-5.284884,1.978826,-2.663345,3.221781,4.713665,-2.716349,0.725891,2.939950,-3.224000,-1.243954,-3.678699,1.416119,5.198718,-5.607668,4.525933,1.591321,-8.842447,0.893828,-2.023071,8.784504,4.729419,7.076721,-7.471937,1.604265,0.027515,-4.622488,1.081485,6.810470,-9.873878,2.348515,-9.608909,3.544025,1.057535,-9.096417,3.691755,7.937227,1.908852,-7.131946,-5.303051,-1.329920,2.060760,5.138750,-4.187941,9.436592,-1.676621,-7.288693,-0.788350,-1.334957,-0.869034,4.758301,-4.351998,-3.886841,5.661898,-0.695875,-8.588547,-8.175930,0.387671,7.338587,-5.373293,-4.078918,7.403471,6.748906,3.202172,3.188123,-2.815836,2.466960,4.547527,-9.775279,-3.567981,-1.415190,0.239411,9.930650,2.197021,8.836706,9.436329,-9.039203,-9.410119,-2.759109,6.666848,-3.447840,9.541206,3.945579,3.985246,8.913691,-1.077346,0.661850,-9.169319,-8.371265,3.080106,6.943059,1.382386,6.995999,-3.603645,1.450291,7.829695,4.839754,-7.553863,6.917125,5.056941,0.002167,0.494791,0.005351,2.004269,2.288484,6.281616,-5.924544,-4.757970,5.193764,0.536645,1.500661,-4.448635,1.829788,3.178475,-3.750477,-7.218415,-7.530367,-7.349507,1.941892,6.205166,-7.260611,-7.004956,2.982779,-3.271782,4.887406,-7.620731,-5.855565,9.690046,0.543284,6.500039,6.726588,7.471331,3.693393,-0.325518,-3.137622,6.139676,-3.565686,5.940572,-4.015307,-2.306630,8.115879,-1.901337,3.056292,-7.597509,-5.104996,9.157208,1.491772,8.636590,-3.890178,5.884002,6.757553,-8.699376,-0.885828,-0.163136,8.039281,-3.695191,6.873094,6.021391,0.929301,3.940056,8.115635,7.142338,0.616899,2.739780,-5.925759,-6.827636,4.615011,-1.026455,-1.560897,-3.117756,0.712412,9.900522,-7.531368,-6.717034,-1.979658,6.454377,-7.164365,-7.495940,-2.087489,7.559221,-8.332816,-9.496473,-1.554663,-5.946878,3.729023,8.622302,7.045286,5.655221,7.552344,9.256853,5.711569,6.145648,-5.916812,-6.593633,5.654155,9.702657,8.594441,8.381993,-3.833129,2.472429,-6.732191,6.002927,3.349317,5.232959,-6.331255,-8.769887,-2.838972,7.305404,6.313013,7.509539,2.806971,-0.676793,-6.983722,8.419530,6.174438,3.207960,1.510686,-6.932357,5.370693,0.540026,-5.352764,-2.151312,2.555727,2.195710,6.063932,5.751866,-2.980858,5.873105,8.877379,3.872485,5.816675,-4.365189,9.958095,7.433620,7.607765,-1.390760,-0.036277,-5.889685,-3.213443,-6.914789,-9.330814,0.857137,-5.760701,1.254647,8.328770,-8.967267,7.159389,8.373305,2.379716,-5.951863,5.496443,6.397293,0.024230,4.598470,7.758690,2.853681,2.072985,-7.191221,7.368880,0.883675,6.720133,-8.266636,-4.062304,9.386677,-9.502966,-0.687591,5.594069,-4.417096,3.759192,-3.528395,3.543215,-4.250037,-8.675969,-1.044729,7.640302,-3.385958,-6.655422,6.150458,-4.450233,-0.925619,-0.615672,-5.881884,-5.884170,-3.424775,-9.826610,1.457741,-9.413406,-8.042514,-4.476184,8.967596,-1.090216,-1.408206,-7.309024,-2.739379,4.802710,2.261759,3.476463,2.254725,-9.266018,-4.174233,-5.907983,9.798212,4.850131,-4.457785,-2.917678,7.055561,0.945272,3.343881,-0.697955,8.537064,2.374975,4.400736,-6.353837,-5.824962,5.302810,-5.759643,-0.072223,-1.498162,6.264126,-9.913112,-1.016837,4.896306,7.464145,3.850795,-1.693528,8.825133,-5.263140,-5.652779,1.964415,3.836610,9.893533,3.554651,4.266956,-2.629890,-7.471501,8.123181,-5.874029,-3.950375,9.609378,3.055445,-2.537970,1.893181,-3.026468,-1.572684,0.502067,-8.639360,5.624999,-5.878268,9.638379,4.502864,5.662752,6.323804,4.397911,-0.264680,3.730504,-7.802610,-7.486188,-3.493090,-1.681606,6.721965,0.984919,-5.568993,8.388765,5.999136,4.125618,-0.261167,5.912207,2.478290,6.126620,-0.587341,8.624460,3.513076,-7.020321,-7.425573,-1.151773,-0.300651,1.805484,-9.704026,-1.192844,-0.543931,-8.916476,-2.923269,-9.389769,0.887819,0.313052,-3.689261,-7.297635,5.590506,-7.630107,0.027932,2.006328,-5.840533,1.983769,5.657954,-5.489226,0.411513,-1.109280,4.713029,0.981818,-5.555307,-4.365124,-8.078516,-5.077225,3.756538,5.611521,5.106319,8.065608,-8.401757,-5.784573,-4.062200,5.597777,-2.916224,1.257251,-6.633956,-3.705717,-9.389483,0.427077,4.243419,-8.993136,-6.885419,-9.230664,-8.353924,0.185258,-1.899026,-1.252221,2.297093,-1.006043,2.555788,5.969941,2.491587,-3.514473,-5.829838,-4.910712,-9.756243,-9.191323,-9.078596,-6.616067,-7.558937,2.900779,-7.497098,7.216109,0.702893,3.947984,-9.506405,-3.990768,-6.569243,9.372287,5.438350,-3.903450,-1.923169,-1.919343,1.723570,5.820269,4.492250,-0.735107,-3.924615,3.046430,-0.345999,-1.061131,4.845465,-3.107244,5.850792,-8.021254,8.112080,-3.258341,8.344235,-0.565117,-2.925477,5.996351,2.349074,3.081826,3.008391,0.249238,3.164641,-9.894330,4.183458,-4.077588,-7.773335,5.874918,4.024685,5.177691,-1.611522,-0.710981,3.740098,-2.991434,3.047578,-9.265807,-6.618533,-8.541507,7.073907,-9.483896,0.335530,-1.390448,9.515252,2.909592,9.231241,-7.416208,2.648682,-4.564850,-9.759532,6.419751,-6.562469,-6.707581,7.880505,-9.493259,-1.785849,2.638784,9.451237,9.189807,3.457482,-5.397170,-9.595895,0.264656,1.114224,-9.363901,-9.369864,7.788207,-8.513955,-6.007257,1.692605,-5.497266,7.056767,5.228040,2.946400,-3.034462,-2.288263,-0.830102,7.507482,-4.723164,7.215421,-9.394501,-7.335870,1.917348,0.931027,-4.982317,-2.398317,-2.087898,4.319969,8.777678,3.340191,6.905468,-6.788045,-3.238197,4.583168,-7.411418,4.392976,6.072625,-6.422561,-2.586553,-0.091889,-6.283151,-8.580432,-1.154754,7.009478,-2.035628,2.349364,-9.168454,7.703383,7.336714,0.479079,-7.913833,-3.300076,-4.209864,-0.679132,3.586584,6.124275,2.143192,-7.241861,0.311414,8.757999,-7.150993,-1.330592,-1.596146,5.959681,-8.325013,5.852871,-1.029107,-9.315031,5.508406,3.108899,6.404982,-2.527190,-3.485471,4.739371,-2.736695,-0.360967,8.364833,2.912582,-1.461967,-2.980549,9.641586,7.553422,3.289073,-9.626968,-9.404054,9.325803,3.924850,1.915417,0.324403,4.215671,2.642904,-9.473100,-9.784914,4.011513,4.997792,-7.791935,6.390640,-2.928962,5.890894,9.228529,-9.733693,-8.241866,7.204788,-2.644535,-0.094180,-6.872606,2.678822,-8.018700,8.971918,-4.425334,3.086118,1.026316,3.365618,-9.948819,0.638052,-6.414938,-1.179543,2.440966,-1.584684,-1.342600,4.959302,4.209108,-2.543923,6.766515,6.562172,-3.383102,-9.152154,2.905844,5.758708,-5.622321,-5.133683,-9.079391,0.843704,-9.058429,2.214463,-5.343891,3.605042,5.333838,-6.334718,1.344676,4.766434,-4.857642,-6.292182,9.191741,7.695786,-8.312931,-4.576045,8.668843,-1.566991,-0.701524,-1.550667,-9.975674,-6.366817,8.929487,-5.230603,-2.828373,-3.959828,2.549302,-3.903460,-0.163439,3.743537,3.413204,-2.389097,5.876098,-1.274894,-5.886401,5.463119,3.765823,4.823364,-9.049645,7.657845,5.674962,1.189950,-4.451266,9.232775,-8.291611,7.314073,-0.544189,-2.511951,-9.383677,1.850056,8.177003,-0.374719,-9.335257,-2.447556,1.941978,6.981994,0.929219,-0.369418,3.776696,3.987772,-4.161774,5.012477,-0.667523,-4.605285,2.589665,8.039860,-2.731821,4.689435,2.463564,5.324577,6.353381,0.724179,-5.241221,6.986296,5.263048,0.886420,0.148761,0.902836,-9.137117,4.814770,9.093501,-5.949146,-2.129408,4.301083,3.227502,-9.275452,3.821716,-4.352502,5.027909,1.472257,-6.112724,-6.787303,-4.862514,2.516654,-3.576195,-5.553545,1.924391,3.620009,-3.243479,-1.259338,-0.183834,-6.162816,-7.948297,2.087331,-9.091953,7.510353,4.353705,3.540390,5.365967,-1.185620,7.782435,5.073127,9.049741,-7.110360,3.960434,-9.491945,0.845034,-8.854732,3.960444,-9.020292,-9.743230,-5.729523,1.142424,2.295316,-5.813653,-6.537774,-6.172258,-4.529580,4.763373,3.293304,4.235336,-6.480992,0.787174,1.473400,-7.296032,-3.962478,0.676997,-1.394795,-7.456097,3.580025,4.431603,-2.420152,1.529720,0.239352,3.110726,-5.227060,-7.201806,-2.648521,4.190253,-2.755416,1.404177,-4.987017,1.341131,7.085713,6.361731,-7.794218,4.128194,-6.598267,-7.006312,2.431963,0.432512,-8.149827,-2.236948,6.376195,-3.109280,2.249193,-6.232554,-1.483338,-8.679255,-6.314294,-6.030689,-1.677044,2.522759,1.995904,-8.110083,-4.954763,-6.999408,-3.852664,5.822089,-1.878827,0.230789,8.950367,1.231409,-8.488592,8.805876,6.066854,3.711307,6.428090,2.175607,-0.513356,7.725641,9.340959,-6.481801,-5.027571,5.555270,0.962677,-3.903793,-9.650795,5.692956,1.083040,2.554867,-5.470752,-3.881771,-1.661058,-4.962768,-9.478596,5.656614,4.293970,8.881146,4.600105,-3.284973,8.632407,7.236725,0.508724,-5.634792,7.451699,3.643665,0.463587,-6.996073,6.073432,-5.405433,-3.691039,7.691687,4.669798,-1.497876,2.202211,-2.870056,5.725147,2.229708,-4.934475,-2.222243,7.475053,3.940750,7.375274,-3.382251,0.448861,-0.954624,-5.428503,2.595387,-6.576209,-8.071413,0.143328], dtype = "float32")#candidate|2636|(924,)|const|float32
call_2634 = relay.TupleGetItem(func_2401_call(relay.reshape(var_2635.astype('bool'), [2, 4, 8]), relay.reshape(const_2636.astype('float32'), [11, 6, 14]), ), 0)
call_2637 = relay.TupleGetItem(func_2404_call(relay.reshape(var_2635.astype('bool'), [2, 4, 8]), relay.reshape(const_2636.astype('float32'), [11, 6, 14]), ), 0)
bop_2644 = relay.less_equal(var_2627.astype('bool'), call_2608.astype('bool')) # shape=(11, 2, 14)
bop_2647 = relay.less_equal(var_2627.astype('bool'), call_2609.astype('bool')) # shape=(11, 2, 14)
output = relay.Tuple([bop_2628,call_2634,var_2635,const_2636,bop_2644,])
output2 = relay.Tuple([bop_2631,call_2637,var_2635,const_2636,bop_2647,])
func_2652 = relay.Function([var_2627,var_2635,], output)
mod['func_2652'] = func_2652
mod = relay.transform.InferType()(mod)
var_2653 = relay.var("var_2653", dtype = "float32", shape = (11, 2, 14))#candidate|2653|(11, 2, 14)|var|float32
var_2654 = relay.var("var_2654", dtype = "bool", shape = (64,))#candidate|2654|(64,)|var|bool
output = func_2652(var_2653,var_2654,)
func_2655 = relay.Function([var_2653,var_2654,], output)
mutated_mod['func_2655'] = func_2655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_389_call = mod.get_global_var('func_389')
func_390_call = mutated_mod.get_global_var('func_390')
call_2672 = relay.TupleGetItem(func_389_call(), 0)
call_2673 = relay.TupleGetItem(func_390_call(), 0)
func_735_call = mod.get_global_var('func_735')
func_736_call = mutated_mod.get_global_var('func_736')
call_2674 = relay.TupleGetItem(func_735_call(), 1)
call_2675 = relay.TupleGetItem(func_736_call(), 1)
const_2679 = relay.const([[[-4.164295,4.028895,5.808114,-6.349127,3.209641,-0.565659,9.769725,5.879462,3.685638,7.710238,1.530614,6.231093,0.674617,-5.931874],[-8.583790,-5.528686,8.504676,8.470443,-8.294315,-1.490626,5.458832,1.863250,4.954722,-9.417684,-9.028064,-5.276231,4.130488,5.018458],[5.003620,-8.746009,6.625947,-3.169618,-0.037383,0.334258,0.593516,-1.690983,-6.911555,-8.152855,-8.018507,8.692040,-5.617986,6.651642],[2.823033,-6.506900,-6.319126,4.549020,-3.557916,-8.533138,3.033374,0.928964,6.570004,3.825281,-5.635766,5.471312,-0.750880,6.060233],[-1.444467,3.282460,7.948890,-8.321404,-9.359788,1.244161,-9.773778,2.438252,7.123522,-9.687376,8.474278,4.333704,8.324993,-5.388334],[6.331058,2.328666,-9.163161,3.351303,-5.960343,5.377319,5.815534,0.480152,-4.680992,2.683345,-1.388501,-7.917404,-8.030620,6.691954],[-8.920526,3.561006,7.847161,7.561970,1.140834,-9.313894,3.026550,-6.727860,-7.149650,-1.077366,9.178759,7.392623,6.415473,9.603175],[0.069679,-7.501680,-4.573141,0.392262,-9.470288,-1.694977,4.980081,2.938523,-9.362575,-7.079284,-1.157967,-9.671412,-9.324030,4.745280],[9.243422,6.480724,1.681738,1.713180,-4.378833,3.434967,3.982661,-6.426287,-3.084551,2.502139,-8.047878,-9.287250,-3.390688,-2.183972]],[[-9.401107,9.781429,-0.478657,-3.624398,-4.211952,8.972473,-9.139476,6.629258,-8.188227,-2.998014,9.999773,-2.249695,2.413844,-7.392155],[8.415934,8.634945,-3.872804,5.662994,8.431836,-6.212018,3.895858,-9.024622,8.593749,-1.042069,-9.869682,-3.030373,-5.588606,0.258648],[6.656808,-3.762445,-3.149707,-0.694117,-6.489316,9.418954,9.298027,2.586242,9.418714,-2.035160,3.220042,4.604285,-7.547206,4.867717],[-9.086991,-9.127729,9.001948,-0.361068,-5.255568,-9.697083,-5.275333,7.166910,-8.609981,6.075217,-5.812777,-8.932467,-5.939455,2.814811],[5.699075,2.204603,0.201344,-3.745592,-7.792429,-6.430142,7.683914,1.045857,-4.574707,-7.812760,9.875004,0.274458,1.641667,4.456967],[8.303848,-1.207498,-8.341184,-1.220323,-4.650477,-7.728987,5.047080,6.958997,8.298999,-3.016953,5.760773,-6.701358,-1.702742,4.053784],[5.785615,7.698613,1.615879,-8.188766,-3.160996,-4.069977,5.549352,7.940756,8.690388,7.774561,-2.762972,9.588708,-0.668795,-7.433533],[9.566621,3.266974,6.658533,3.374946,-4.070993,-3.987270,-4.811867,2.204997,0.611864,-9.583002,-4.156827,0.709436,5.433349,-9.559621],[6.782465,5.506786,-3.769414,2.772008,5.510338,0.758468,-7.000339,-3.383729,-1.605920,-1.677254,4.930227,-5.609680,5.853175,-1.038577]],[[-2.905805,-0.542254,1.881838,-9.578531,-6.210057,4.366697,-1.590071,-8.711723,-6.168911,2.100023,-3.314493,-2.378661,-2.207647,6.234396],[9.480637,9.764815,1.172751,3.788176,9.261085,-4.406704,4.283775,2.614357,-8.223394,4.297645,7.180408,7.513108,-8.014268,2.232350],[4.666421,-3.532407,-5.548076,-2.402683,-7.881906,-6.078126,-5.425194,1.969028,0.543160,6.354122,-5.626557,-4.257112,-4.660677,-3.531310],[-4.479008,1.076943,-4.143922,-6.680520,9.813419,-2.974393,-3.489354,4.227252,-9.723237,-6.651965,-0.614396,3.360200,-1.793414,-7.348073],[-1.942910,-3.992761,-6.120180,-9.552783,6.775818,3.342617,4.166299,-6.095756,-9.943235,-1.536290,4.526501,-2.645659,6.326767,-4.347283],[-1.299421,-4.364365,6.538723,1.323826,-1.469346,2.699777,-4.630364,0.858006,-2.284660,3.394586,8.602154,0.228449,-8.446123,-6.852970],[-6.961786,-8.115823,6.074252,5.071607,5.380225,-8.464626,-4.903205,1.656952,-9.719633,-1.834242,6.789505,-2.230863,-6.961360,5.972117],[4.367143,-9.570642,-6.277943,-2.374365,0.585809,9.209587,-8.822354,-7.284879,3.182572,6.633678,-1.929198,-4.085874,3.415733,2.280573],[6.391005,8.727066,-1.065363,-7.085183,-9.852334,7.706911,-6.163175,-2.413392,-1.121766,7.312760,-4.687079,-9.909621,-1.102224,-8.025004]],[[0.005415,9.070903,-9.498696,5.399175,-5.945769,-9.459350,5.124044,-6.462264,-8.219684,-5.524706,-2.040341,-8.856968,7.830437,9.681538],[1.529733,2.520385,6.077796,1.352850,3.833407,9.299068,-0.521632,-9.857278,5.382847,6.917093,4.398988,-6.525212,2.039033,6.388745],[7.079248,6.605418,-7.757136,5.412339,5.147259,-3.777000,-8.739266,6.522170,8.280396,-7.619371,-4.710859,-4.608814,4.085484,9.396312],[5.897514,7.312425,-5.037462,0.718529,-4.855714,-6.099604,-2.032084,-2.321968,-7.295268,5.113069,-4.373326,-2.917495,-4.220166,-5.217844],[-7.141538,-9.029031,-6.509443,-6.566020,-8.137274,-5.820763,7.664124,0.999096,7.711699,-9.738042,3.972971,4.591086,3.008216,-2.249101],[-4.751117,4.333632,0.333342,-4.593662,-5.029369,-5.653612,-3.936065,3.101660,5.720387,6.454514,-2.696521,1.039287,-6.659259,1.266275],[-4.960044,2.598907,7.423581,5.467519,-9.093825,-2.385054,5.777292,-5.966882,7.805571,2.299973,-3.577055,0.680624,-9.135593,-6.310556],[4.800372,-4.454334,8.359427,-2.862327,-5.876959,7.933191,9.584231,2.609379,-8.786419,6.683394,1.060595,1.813233,0.452239,9.123310],[6.927954,-0.585524,7.335829,-4.080754,-9.989303,9.227286,0.245850,-0.151309,0.826164,2.325205,3.917905,6.127063,9.540062,-9.590710]],[[-2.334017,-4.968329,5.465884,-4.841570,2.086027,3.129241,-1.566111,-7.872211,-4.975303,-1.706481,1.275426,0.694808,-3.967884,9.633749],[0.287855,9.366173,1.847841,0.471772,-3.462143,-3.264864,2.275395,-6.988466,-3.157525,5.141329,8.283471,-4.357754,7.730552,8.641497],[9.886179,0.206584,-3.363546,-6.337762,-7.509469,-2.925233,5.724687,-7.657691,-0.976671,-6.644720,7.713303,6.503281,-6.161498,7.358235],[-0.800057,2.644433,-9.435746,-6.540232,5.273406,-7.741932,5.942954,9.312511,0.205075,0.435119,-4.542829,6.094485,2.162289,-4.221856],[-5.112969,4.824388,-8.982277,-9.268767,6.773440,0.561677,1.384953,-9.551152,-9.904867,-4.679201,2.950317,1.610554,0.577371,4.908423],[-0.433483,-9.740735,-0.858590,3.629403,0.376404,9.646735,-3.103745,9.787165,-0.511252,-9.368831,5.435775,3.659897,-3.535464,-7.946773],[6.764696,-3.167388,1.073902,-8.488121,-3.575893,-4.033407,-5.378592,-0.902078,-1.149182,-1.547679,8.207937,6.970987,3.850187,8.985669],[-9.728936,-1.575209,-8.554700,5.364843,9.892051,7.873892,0.091598,9.065153,1.708096,-9.491709,-6.732010,-6.028019,-8.005329,-2.502508],[-2.724656,4.437756,-4.382708,-4.173410,9.881148,-8.771369,-2.877157,-1.960834,-4.208180,6.864402,-8.090078,9.623790,-2.615294,-2.900985]],[[-8.429539,8.140211,4.448378,3.161742,-1.017530,-8.442507,1.837897,-3.749406,-0.720589,7.101949,1.422196,-1.648696,-1.590039,-7.803952],[9.599044,4.872121,5.417317,2.665856,-3.354473,-0.012135,-4.784118,-7.868829,-2.265800,4.862414,7.148222,6.361683,1.310507,-2.383331],[3.436835,8.250484,-4.151919,-6.593464,2.081582,-4.016118,-6.818237,-8.956773,2.178155,-1.699118,6.456165,-8.665524,-8.823744,1.101697],[2.488104,-4.692890,-5.921627,4.554602,-6.901800,9.996570,2.889956,7.360140,-8.839091,4.925514,-2.324977,5.255005,5.375060,2.653675],[3.607641,-0.543792,-1.249793,-3.841782,-2.453417,0.311867,4.931161,-9.011953,-6.354086,9.372622,6.338389,-6.056489,-7.237120,6.812211],[4.415364,-1.370106,-7.653560,9.386189,8.818642,8.839972,-5.510662,-7.580938,2.646525,-2.246501,6.269758,4.750146,-7.521938,-6.671822],[4.236211,3.607771,-0.852404,-0.335087,-8.928164,-1.019300,8.891689,1.760660,-3.427898,8.535775,-1.401580,-9.731975,7.212922,-1.200228],[4.600331,2.750326,-7.260646,-1.432240,-8.060615,9.582183,-8.937260,-4.037434,-6.054636,4.285819,5.806176,-1.173516,8.669893,2.984342],[-5.479219,-2.417457,9.418012,9.737297,-2.266062,-4.459567,-0.654875,0.249401,5.215522,-4.537368,6.278897,8.314677,-8.542369,-0.904140]],[[-0.476394,4.334501,8.555772,-0.642129,8.784768,5.103818,3.498199,-3.083938,7.742002,0.216182,0.363426,-2.498923,7.669909,2.295649],[-9.557837,5.009228,-1.929394,8.779763,8.145236,-0.428468,8.990607,-0.643487,8.269590,-2.392061,2.327452,-6.580500,1.829110,8.883788],[-7.122750,7.971448,4.782583,4.877811,2.948849,0.482608,-4.683429,5.059716,1.020558,7.988116,-7.233242,-3.850051,0.810471,-7.255877],[4.377866,3.016451,-3.155809,-5.904886,-0.998701,5.422888,9.439384,-4.696770,-0.118666,2.516379,1.412625,1.729635,4.414443,0.990627],[-9.871018,8.463414,-9.025164,6.752374,1.293436,-5.169722,7.114984,8.288087,-9.640293,-5.963111,6.075895,5.044834,-1.137120,-4.461586],[-6.051735,-0.832493,6.226811,-7.978159,1.131299,1.877769,-1.715334,-6.926358,8.142712,-7.439265,4.757597,6.108277,-1.378199,7.796446],[0.475893,-4.445728,-4.517905,-2.143512,1.973890,9.007416,-1.282562,2.824529,-2.519685,-6.989571,-2.485191,5.513365,1.793105,-7.917059],[7.415608,7.403487,-3.933547,-8.447800,-6.538405,-6.668642,-9.354855,-8.972943,-8.388816,8.776657,9.916422,8.150543,-5.677337,4.180498],[0.617196,2.670198,-5.168210,7.020946,4.462829,5.216436,-7.792298,3.261182,9.132064,7.022306,1.491859,-1.060823,-0.278376,-6.394841]],[[-8.770521,-7.097826,-4.345922,4.174457,-2.453992,7.342203,-9.140665,-0.844391,-2.965454,2.333034,6.928763,-9.212487,2.043637,-0.748372],[-4.741267,-1.283123,-3.763990,-3.544168,6.717725,8.512338,-2.488878,3.937970,1.087060,5.679246,0.475767,5.750038,6.522108,3.902185],[-7.768651,-8.579709,0.559281,-1.820278,2.205339,-3.045957,-6.172120,0.998755,-2.919852,5.952573,-9.373267,5.299334,-9.451160,-1.719727],[-9.811135,-7.754859,0.590349,9.542764,-6.213850,3.080689,-9.641341,-7.588220,3.096476,6.592115,-3.331908,-2.064937,0.590000,-9.193183],[-9.283298,6.333345,-6.195677,-2.052313,-7.040680,-1.592389,5.274155,4.421526,7.092676,-4.097080,8.729663,-1.093945,-3.555628,-0.223822],[6.842292,7.867668,3.887988,-6.016943,5.717910,-5.747507,3.485355,-1.276126,-6.301802,-9.032609,9.425294,-7.386584,0.575519,-9.401042],[0.594631,1.855016,5.986081,6.119420,-1.289530,-6.348845,-1.475791,4.236578,-1.331877,-9.070433,7.760104,-9.192669,8.114367,5.572567],[-4.355266,-0.582948,-4.751223,-8.108326,4.473051,6.901971,2.354208,3.710094,-3.085242,6.111760,-5.654519,9.180862,6.930261,-8.703220],[-6.619940,0.764631,0.076661,6.637192,9.250320,3.896726,9.174132,-7.228377,-9.088624,-1.218458,8.420196,6.301307,2.885616,3.686960]],[[9.175318,8.997701,-7.567937,-6.599416,-2.004144,8.649270,5.587062,-9.645676,8.450393,8.382051,-5.706061,-0.943068,-1.532513,4.227951],[-4.163945,-8.141691,-8.843227,-7.552141,-4.356195,-5.386939,-2.126279,-6.449161,-4.784677,-1.204409,-3.393836,-3.889494,0.665373,-8.121763],[-8.900528,0.007533,-6.204670,-7.464483,1.006253,8.018261,1.255004,-8.368352,-4.706795,6.904176,-7.528317,-5.290315,-6.816124,3.160804],[-6.441644,1.811169,-4.587105,3.909289,-7.347770,6.779297,-9.671334,8.151847,1.997004,3.969330,-1.252596,-8.450799,-7.794509,5.548322],[8.974403,-3.882749,-9.743236,1.876375,-8.154109,-1.576691,-0.616240,-5.274772,-6.926398,6.048554,-0.889893,0.339523,3.504661,6.426868],[2.770446,-9.687757,2.741136,-5.010160,-1.130613,-8.724197,-2.414924,7.977533,5.785839,-1.570077,6.827214,1.838417,-0.928219,8.049058],[-0.268124,-4.984875,6.435881,7.849285,6.798441,1.962660,4.168683,8.487729,-5.377062,-6.589123,-1.944871,6.914210,-7.524030,1.775841],[-1.514897,1.472545,2.796572,-8.578296,-8.558549,-7.782174,1.951849,-1.125374,4.143599,-3.840158,-1.826689,5.874928,7.187635,5.877012],[5.651216,6.221205,7.501232,3.908247,-2.997393,9.125981,0.086686,-3.382903,6.042538,1.866620,-8.923290,-2.540448,-5.084271,-3.012317]],[[3.174107,-9.108516,-1.006406,-3.964071,-4.131766,8.054911,5.728697,1.495346,-9.518476,2.618492,-3.694529,-1.680140,-8.304610,-9.669060],[8.548941,4.986475,-3.782898,9.619035,7.141423,-3.647633,9.625553,-7.752492,-3.525929,4.800802,8.410394,3.428479,9.101090,4.017736],[-6.990023,8.563757,-4.975555,-4.742040,-5.978402,9.188520,9.604343,3.557275,2.619916,7.119330,6.725772,-1.246292,2.155430,7.062003],[-7.051909,7.817203,-2.380623,-3.903550,7.205658,7.763646,-1.004848,7.253230,-0.483242,9.363329,-0.799620,0.662541,7.869104,-7.455196],[5.185446,-2.663774,-7.457327,1.147726,-7.990268,3.233923,-3.324826,1.735146,-1.203913,9.129715,6.390982,-6.094677,3.451990,7.655130],[-9.654745,-8.334345,5.440293,7.265409,-4.992805,-1.066797,-3.902715,-9.920921,-2.420003,8.807681,-0.085362,9.659441,3.569329,6.919960],[-9.349310,-9.674219,-7.724464,-5.331749,8.604902,-6.922401,-8.934508,-4.349440,-6.441014,-1.018571,-0.924952,6.099137,-8.608996,-2.369777],[9.236014,-0.067147,-6.649285,-3.780374,5.982329,7.260492,-2.975328,-8.821670,-5.117352,3.070127,9.317756,-0.480415,6.293401,-2.600488],[-9.371320,-7.770029,-5.922397,9.428459,3.949329,-1.861913,8.610803,1.528873,0.384266,-1.555703,-0.255073,-1.027935,6.459406,1.191827]],[[5.089155,-4.477558,-2.539075,1.627514,-1.191222,6.707721,-1.198178,-2.186565,5.739489,0.750303,-0.743122,7.162996,8.600773,-4.397865],[-6.336220,8.495776,-3.423752,5.564601,-3.883025,7.102323,-0.282539,-5.438961,-9.723159,-1.215037,-6.042800,-4.654406,9.640645,1.211992],[-9.484762,-0.355416,2.931306,-5.900362,3.675205,-4.635405,-4.957905,-1.183933,9.498589,3.388958,-8.997818,5.287404,3.662990,7.266747],[4.043219,8.356740,-2.551892,-8.739816,9.304285,8.783159,4.179868,6.195750,-4.068469,-5.207688,-0.855473,5.615057,0.629238,-8.967017],[7.964288,4.763348,-9.567294,-8.088229,-3.550467,1.608610,4.718163,8.988595,-6.508132,-4.681606,-1.209822,-3.698994,-1.461594,8.804322],[3.202604,-8.502529,5.230829,5.090361,-5.878894,5.213459,1.053573,-1.090626,4.130212,4.334201,-2.994503,-2.272510,-1.190512,-2.135208],[1.201883,-1.840166,0.966089,9.969850,-9.230079,-2.885272,-0.433013,-0.702411,-8.952238,-3.362191,-0.302397,-2.787613,5.891632,7.854851],[5.938814,-3.448361,-7.663639,3.772968,4.598774,-5.043264,-5.713076,-2.256173,-0.200129,-5.228871,6.958376,4.773462,-2.555841,8.998627],[-1.244422,2.826235,-6.320408,-4.243108,-1.627518,-3.691520,-5.813515,2.919507,8.720882,8.495323,-6.042500,7.172287,-7.187563,7.261271]]], dtype = "float32")#candidate|2679|(11, 9, 14)|const|float32
bop_2680 = relay.bitwise_and(call_2674.astype('uint16'), relay.reshape(const_2679.astype('uint16'), relay.shape_of(call_2674))) # shape=(11, 9, 14)
bop_2683 = relay.bitwise_and(call_2675.astype('uint16'), relay.reshape(const_2679.astype('uint16'), relay.shape_of(call_2675))) # shape=(11, 9, 14)
output = relay.Tuple([call_2672,bop_2680,])
output2 = relay.Tuple([call_2673,bop_2683,])
func_2693 = relay.Function([], output)
mod['func_2693'] = func_2693
mod = relay.transform.InferType()(mod)
mutated_mod['func_2693'] = func_2693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2693_call = mutated_mod.get_global_var('func_2693')
call_2694 = func_2693_call()
output = call_2694
func_2695 = relay.Function([], output)
mutated_mod['func_2695'] = func_2695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_614_call = mod.get_global_var('func_614')
func_615_call = mutated_mod.get_global_var('func_615')
call_2696 = relay.TupleGetItem(func_614_call(), 0)
call_2697 = relay.TupleGetItem(func_615_call(), 0)
output = relay.Tuple([call_2696,])
output2 = relay.Tuple([call_2697,])
func_2698 = relay.Function([], output)
mod['func_2698'] = func_2698
mod = relay.transform.InferType()(mod)
output = func_2698()
func_2699 = relay.Function([], output)
mutated_mod['func_2699'] = func_2699
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2711 = relay.var("var_2711", dtype = "int64", shape = ())#candidate|2711|()|var|int64
var_2712 = relay.var("var_2712", dtype = "int64", shape = (1, 6, 16))#candidate|2712|(1, 6, 16)|var|int64
bop_2713 = relay.right_shift(var_2711.astype('int64'), var_2712.astype('int64')) # shape=(1, 6, 16)
output = relay.Tuple([bop_2713,])
output2 = relay.Tuple([bop_2713,])
func_2719 = relay.Function([var_2711,var_2712,], output)
mod['func_2719'] = func_2719
mod = relay.transform.InferType()(mod)
mutated_mod['func_2719'] = func_2719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2719_call = mutated_mod.get_global_var('func_2719')
var_2721 = relay.var("var_2721", dtype = "int64", shape = ())#candidate|2721|()|var|int64
var_2722 = relay.var("var_2722", dtype = "int64", shape = (1, 6, 16))#candidate|2722|(1, 6, 16)|var|int64
call_2720 = func_2719_call(var_2721,var_2722,)
output = call_2720
func_2723 = relay.Function([var_2721,var_2722,], output)
mutated_mod['func_2723'] = func_2723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_2729 = func_2601_call()
call_2730 = func_2601_call()
output = relay.Tuple([call_2729,])
output2 = relay.Tuple([call_2730,])
func_2736 = relay.Function([], output)
mod['func_2736'] = func_2736
mod = relay.transform.InferType()(mod)
output = func_2736()
func_2737 = relay.Function([], output)
mutated_mod['func_2737'] = func_2737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_2789 = relay.TupleGetItem(func_418_call(), 0)
call_2790 = relay.TupleGetItem(func_420_call(), 0)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_2802 = relay.var("var_2802", dtype = "float64", shape = ())#candidate|2802|()|var|float64
const_2803 = relay.const([9.293125,1.237743,-6.801485,4.338286,-8.917361], dtype = "float64")#candidate|2803|(5,)|const|float64
call_2801 = relay.TupleGetItem(func_47_call(relay.reshape(var_2802.astype('float64'), []), relay.reshape(const_2803.astype('float64'), [5, 1, 1]), ), 1)
call_2804 = relay.TupleGetItem(func_50_call(relay.reshape(var_2802.astype('float64'), []), relay.reshape(const_2803.astype('float64'), [5, 1, 1]), ), 1)
output = relay.Tuple([call_2789,call_2801,var_2802,const_2803,])
output2 = relay.Tuple([call_2790,call_2804,var_2802,const_2803,])
func_2805 = relay.Function([var_2802,], output)
mod['func_2805'] = func_2805
mod = relay.transform.InferType()(mod)
var_2806 = relay.var("var_2806", dtype = "float64", shape = ())#candidate|2806|()|var|float64
output = func_2805(var_2806)
func_2807 = relay.Function([var_2806], output)
mutated_mod['func_2807'] = func_2807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_2823 = relay.TupleGetItem(func_2220_call(), 0)
call_2824 = relay.TupleGetItem(func_2222_call(), 0)
output = call_2823
output2 = call_2824
func_2826 = relay.Function([], output)
mod['func_2826'] = func_2826
mod = relay.transform.InferType()(mod)
mutated_mod['func_2826'] = func_2826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2826_call = mutated_mod.get_global_var('func_2826')
call_2827 = func_2826_call()
output = call_2827
func_2828 = relay.Function([], output)
mutated_mod['func_2828'] = func_2828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2010_call = mutated_mod.get_global_var('func_2010')
call_2847 = func_2009_call()
call_2848 = func_2009_call()
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_2849 = relay.TupleGetItem(func_1823_call(), 2)
call_2850 = relay.TupleGetItem(func_1825_call(), 2)
uop_2851 = relay.sin(call_2847.astype('float64')) # shape=(11, 1, 14)
uop_2853 = relay.sin(call_2848.astype('float64')) # shape=(11, 1, 14)
bop_2865 = relay.greater(uop_2851.astype('bool'), relay.reshape(call_2847.astype('bool'), relay.shape_of(uop_2851))) # shape=(11, 1, 14)
bop_2868 = relay.greater(uop_2853.astype('bool'), relay.reshape(call_2848.astype('bool'), relay.shape_of(uop_2853))) # shape=(11, 1, 14)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_2869 = relay.TupleGetItem(func_965_call(), 0)
call_2870 = relay.TupleGetItem(func_967_call(), 0)
func_2652_call = mod.get_global_var('func_2652')
func_2655_call = mutated_mod.get_global_var('func_2655')
const_2874 = relay.const([[-4.420678,8.048819],[-5.536271,-5.713531],[2.158237,5.208290],[-8.216778,-5.908664],[0.296596,5.444567],[-7.524033,-5.720449],[-8.172887,-4.425766],[-6.970479,-7.833540],[-7.483555,3.491406],[8.789378,-7.124233],[-3.424825,9.839902],[-7.189419,4.680928],[-8.898304,-1.794577],[3.206840,3.379015],[-9.522366,-5.856779],[2.436254,2.362351],[-0.986224,1.196362],[0.349199,-1.334716],[9.093512,-1.498154],[0.175908,0.987797],[-5.655737,-6.121620],[-1.187425,-6.010519],[-1.802810,1.157992],[5.522185,7.667014],[-3.569282,6.383619],[-4.032986,5.362451],[5.716295,1.232014],[-5.019789,-5.027948],[9.052757,-9.600121],[0.044390,-9.616432],[1.382349,5.854960],[2.881662,0.011116],[0.967916,0.617620],[-8.534685,9.253292],[-8.112870,4.753268],[-2.254490,6.768868],[-7.085411,0.030015],[-9.148519,2.845338],[-5.359631,-2.877924],[8.208882,7.542790],[-4.840025,3.221376],[7.350478,-0.593013],[8.248792,-0.836204],[-6.439673,6.720878],[4.547184,-4.269265],[6.756102,-3.650819],[-8.210736,5.588719],[-8.275597,1.752315],[5.450274,2.453637],[4.707609,-6.829460],[8.537550,-0.484872],[-3.508507,9.970240],[2.695666,-9.675564],[7.825000,-7.434118],[6.184296,-9.699584],[-2.267683,2.259786],[-7.376827,-5.259301],[-5.080538,-6.455877],[-5.933732,8.925207],[9.610271,-1.916421],[-2.377877,6.090836],[6.141692,-6.176188],[8.649564,-0.667999],[-6.369111,9.454965],[9.977090,-7.219240],[-4.118076,9.253860],[-5.400459,3.651604],[1.714950,-6.032127],[-7.964563,-6.604199],[4.614133,8.956560],[8.278421,-4.721308],[1.229325,-3.390573],[0.114377,-9.210738],[3.291298,-2.876347],[0.274305,6.461849],[-9.319879,-3.202344],[2.622706,-9.866747],[1.434969,4.050097],[-7.649088,-6.833322],[4.353250,-6.106845],[-7.438349,-4.246079],[-4.074813,7.342077],[4.468532,4.610275],[-4.013909,-4.687928],[-7.763919,-4.008520],[-4.153705,-9.752109],[3.929067,-9.683796],[6.414737,2.487960],[-3.121424,1.981332],[7.350392,-0.041695],[-2.397769,-9.022670],[1.691083,-3.947423],[6.546014,-4.824650],[8.378398,-9.407892],[3.263853,6.089716],[6.680822,-3.284294],[2.397449,5.543151],[-4.492572,6.187251],[3.255857,8.951694],[-4.656566,-1.240077],[-2.121792,-7.348226],[6.636405,-0.945171],[6.251777,0.971901],[3.517411,-6.658284],[7.166303,2.775844],[6.513933,-0.981243],[-8.206184,-3.295381],[-9.876913,-4.083223],[9.173601,-9.561048],[-0.450632,8.090781],[-6.477510,-1.304196],[2.882475,-7.702192],[-9.008325,-4.594445],[-0.334281,-5.152098],[4.752217,-9.895894],[3.240188,-7.157150],[1.278252,1.450475],[-5.227909,2.866809],[3.099654,-6.589678],[3.243939,-2.862494],[-3.330499,1.303631],[6.725405,5.713728],[-5.941712,-1.600811],[-9.482442,-7.472793],[2.076970,3.617252],[8.267834,7.927265],[5.522002,2.190743],[-8.924412,-2.587174],[-5.956030,-6.595232],[-4.359547,-5.560241],[3.446591,-2.538333],[-3.865836,3.471060],[0.663467,5.328845],[5.991412,0.381786],[-8.167210,6.891160],[-8.331563,1.773766],[-8.379677,2.428523],[3.471256,0.211211],[-0.360207,-0.503474],[0.762110,0.654258],[9.523720,4.959653],[1.305715,3.806285],[1.517123,-1.796887],[-2.927156,-1.721161],[9.464297,4.367636],[-4.559045,1.257937],[5.932576,3.517687],[5.328680,8.768556],[7.914971,-8.427317],[6.483759,-2.986023],[-6.079023,7.153795],[-4.608142,8.568077],[6.030698,-3.812784],[-9.199587,-8.893741]], dtype = "float32")#candidate|2874|(154, 2)|const|float32
const_2875 = relay.const([[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[False],[False],[True],[True],[True]], dtype = "bool")#candidate|2875|(64, 1)|const|bool
call_2873 = relay.TupleGetItem(func_2652_call(relay.reshape(const_2874.astype('float32'), [11, 2, 14]), relay.reshape(const_2875.astype('bool'), [64,]), ), 1)
call_2876 = relay.TupleGetItem(func_2655_call(relay.reshape(const_2874.astype('float32'), [11, 2, 14]), relay.reshape(const_2875.astype('bool'), [64,]), ), 1)
output = relay.Tuple([call_2849,bop_2865,call_2869,call_2873,const_2874,const_2875,])
output2 = relay.Tuple([call_2850,bop_2868,call_2870,call_2876,const_2874,const_2875,])
func_2888 = relay.Function([], output)
mod['func_2888'] = func_2888
mod = relay.transform.InferType()(mod)
mutated_mod['func_2888'] = func_2888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2888_call = mutated_mod.get_global_var('func_2888')
call_2889 = func_2888_call()
output = call_2889
func_2890 = relay.Function([], output)
mutated_mod['func_2890'] = func_2890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_2959 = func_64_call()
call_2960 = func_64_call()
output = call_2959
output2 = call_2960
func_2966 = relay.Function([], output)
mod['func_2966'] = func_2966
mod = relay.transform.InferType()(mod)
output = func_2966()
func_2967 = relay.Function([], output)
mutated_mod['func_2967'] = func_2967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_3010 = relay.TupleGetItem(func_965_call(), 0)
call_3011 = relay.TupleGetItem(func_967_call(), 0)
func_2652_call = mod.get_global_var('func_2652')
func_2655_call = mutated_mod.get_global_var('func_2655')
var_3015 = relay.var("var_3015", dtype = "float32", shape = (308,))#candidate|3015|(308,)|var|float32
var_3016 = relay.var("var_3016", dtype = "bool", shape = (64,))#candidate|3016|(64,)|var|bool
call_3014 = relay.TupleGetItem(func_2652_call(relay.reshape(var_3015.astype('float32'), [11, 2, 14]), relay.reshape(var_3016.astype('bool'), [64,]), ), 3)
call_3017 = relay.TupleGetItem(func_2655_call(relay.reshape(var_3015.astype('float32'), [11, 2, 14]), relay.reshape(var_3016.astype('bool'), [64,]), ), 3)
func_2693_call = mod.get_global_var('func_2693')
func_2695_call = mutated_mod.get_global_var('func_2695')
call_3025 = relay.TupleGetItem(func_2693_call(), 1)
call_3026 = relay.TupleGetItem(func_2695_call(), 1)
func_1425_call = mod.get_global_var('func_1425')
func_1427_call = mutated_mod.get_global_var('func_1427')
call_3032 = relay.TupleGetItem(func_1425_call(), 2)
call_3033 = relay.TupleGetItem(func_1427_call(), 2)
func_349_call = mod.get_global_var('func_349')
func_351_call = mutated_mod.get_global_var('func_351')
var_3044 = relay.var("var_3044", dtype = "float32", shape = (847, 2))#candidate|3044|(847, 2)|var|float32
call_3043 = func_349_call(relay.reshape(var_3044.astype('float32'), [11, 11, 14]))
call_3045 = func_349_call(relay.reshape(var_3044.astype('float32'), [11, 11, 14]))
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_3047 = func_64_call()
call_3048 = func_64_call()
output = relay.Tuple([call_3010,call_3014,var_3015,var_3016,call_3025,call_3032,call_3043,var_3044,call_3047,])
output2 = relay.Tuple([call_3011,call_3017,var_3015,var_3016,call_3026,call_3033,call_3045,var_3044,call_3048,])
func_3059 = relay.Function([var_3015,var_3016,var_3044,], output)
mod['func_3059'] = func_3059
mod = relay.transform.InferType()(mod)
mutated_mod['func_3059'] = func_3059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3059_call = mutated_mod.get_global_var('func_3059')
var_3061 = relay.var("var_3061", dtype = "float32", shape = (308,))#candidate|3061|(308,)|var|float32
var_3062 = relay.var("var_3062", dtype = "bool", shape = (64,))#candidate|3062|(64,)|var|bool
var_3063 = relay.var("var_3063", dtype = "float32", shape = (847, 2))#candidate|3063|(847, 2)|var|float32
call_3060 = func_3059_call(var_3061,var_3062,var_3063,)
output = call_3060
func_3064 = relay.Function([var_3061,var_3062,var_3063,], output)
mutated_mod['func_3064'] = func_3064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_735_call = mod.get_global_var('func_735')
func_736_call = mutated_mod.get_global_var('func_736')
call_3078 = relay.TupleGetItem(func_735_call(), 1)
call_3079 = relay.TupleGetItem(func_736_call(), 1)
output = call_3078
output2 = call_3079
func_3082 = relay.Function([], output)
mod['func_3082'] = func_3082
mod = relay.transform.InferType()(mod)
output = func_3082()
func_3083 = relay.Function([], output)
mutated_mod['func_3083'] = func_3083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_848_call = mod.get_global_var('func_848')
func_850_call = mutated_mod.get_global_var('func_850')
call_3155 = relay.TupleGetItem(func_848_call(), 1)
call_3156 = relay.TupleGetItem(func_850_call(), 1)
func_2719_call = mod.get_global_var('func_2719')
func_2723_call = mutated_mod.get_global_var('func_2723')
const_3166 = relay.const(9, dtype = "int64")#candidate|3166|()|const|int64
var_3167 = relay.var("var_3167", dtype = "int64", shape = (96,))#candidate|3167|(96,)|var|int64
call_3165 = relay.TupleGetItem(func_2719_call(relay.reshape(const_3166.astype('int64'), []), relay.reshape(var_3167.astype('int64'), [1, 6, 16]), ), 0)
call_3168 = relay.TupleGetItem(func_2723_call(relay.reshape(const_3166.astype('int64'), []), relay.reshape(var_3167.astype('int64'), [1, 6, 16]), ), 0)
output = relay.Tuple([call_3155,call_3165,const_3166,var_3167,])
output2 = relay.Tuple([call_3156,call_3168,const_3166,var_3167,])
func_3182 = relay.Function([var_3167,], output)
mod['func_3182'] = func_3182
mod = relay.transform.InferType()(mod)
var_3183 = relay.var("var_3183", dtype = "int64", shape = (96,))#candidate|3183|(96,)|var|int64
output = func_3182(var_3183)
func_3184 = relay.Function([var_3183], output)
mutated_mod['func_3184'] = func_3184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1177_call = mod.get_global_var('func_1177')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_3242 = relay.TupleGetItem(func_1177_call(), 0)
call_3243 = relay.TupleGetItem(func_1178_call(), 0)
output = call_3242
output2 = call_3243
func_3247 = relay.Function([], output)
mod['func_3247'] = func_3247
mod = relay.transform.InferType()(mod)
mutated_mod['func_3247'] = func_3247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3247_call = mutated_mod.get_global_var('func_3247')
call_3248 = func_3247_call()
output = call_3248
func_3249 = relay.Function([], output)
mutated_mod['func_3249'] = func_3249
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3271 = relay.const([[[7,3,-6,-3,4,-6,9,7,-4,4,9,-4,10,-5,3,-10],[-1,-6,3,-2,1,9,9,-5,-1,8,5,-5,3,-3,1,9],[-6,9,-6,-8,10,-6,5,4,2,-8,-6,-4,-4,7,2,-7],[3,-10,6,6,7,-9,-3,8,6,2,8,-3,5,-8,-8,-7],[-1,-9,-7,7,7,6,-10,3,10,-8,-3,1,-2,7,5,2],[3,7,6,-3,9,-3,6,4,3,-4,-4,-6,-5,-6,-9,8],[-10,1,6,-1,7,-5,1,-7,-1,1,-8,-2,2,-3,8,2],[-6,-8,-10,9,-2,-8,-4,-7,8,2,7,-8,4,1,-5,-4],[7,-5,-8,4,-1,-2,9,-9,9,2,-5,-6,-4,-5,-3,9],[-8,9,-9,7,-5,-4,-10,3,4,7,8,2,-2,2,-3,-5],[5,8,-7,5,-6,8,4,7,-9,-1,8,10,8,7,-10,2],[-8,-1,-5,-7,-7,-9,6,-1,10,1,-3,10,-10,-3,-1,8],[-7,-2,-7,-5,4,3,8,5,6,-6,7,-10,-4,9,-10,-3],[-8,-9,-6,7,-6,1,6,4,4,-1,-7,-9,-4,6,-7,-10],[6,8,-4,1,7,6,2,5,1,8,-7,-8,-7,-4,5,-7]],[[-3,-10,-4,-7,-7,-6,2,-4,7,10,10,4,2,10,-2,-8],[-6,2,-1,10,-9,-6,8,-3,-3,1,-10,-1,-5,-2,9,-3],[-8,4,-3,7,9,-4,-3,-3,9,10,-3,6,3,6,-7,9],[-4,-5,5,1,-7,-4,2,-9,-3,4,1,5,-7,-5,2,2],[-7,4,-10,10,10,8,-1,-6,-5,2,10,9,10,4,10,-9],[2,10,8,7,-2,-1,3,1,8,5,3,-7,-10,5,4,8],[7,8,-6,5,-4,-2,6,5,7,1,-4,2,-9,5,-3,1],[-10,9,-8,3,3,-8,-1,4,-3,-7,-3,-2,-8,-8,-1,-4],[10,7,8,-9,-9,3,-10,-5,1,-7,-3,-9,-7,5,-5,-10],[-2,4,-9,2,-10,8,-1,-10,-7,7,7,2,-10,-3,-5,2],[10,-7,9,-6,6,8,9,8,-6,-5,-8,8,-5,6,5,-7],[-4,-5,4,1,-7,7,-4,1,1,-2,4,-8,-2,-9,2,4],[-10,6,-2,6,-3,-7,-10,-8,4,-10,1,-7,4,-10,4,2],[-4,-10,5,-8,-10,7,1,3,-5,-4,-2,-9,-1,-5,-4,-8],[3,-5,-5,9,7,-7,3,-6,2,-7,2,-3,7,-7,4,9]],[[5,-8,-8,8,-6,8,7,-10,-5,-7,2,-2,-9,10,-4,1],[-5,-4,7,-2,8,-4,5,8,-10,-9,-5,1,-9,7,2,-5],[-8,-1,10,10,3,-7,-8,10,-7,10,9,-10,-4,2,-7,-10],[5,-2,5,6,-5,-8,-7,-1,-7,-8,4,-3,-5,4,-1,6],[8,-4,9,-2,-3,9,9,4,-3,-10,-2,-5,7,8,-4,5],[-4,4,9,10,-6,-3,1,9,-2,2,2,-1,-9,-7,5,6],[3,3,-5,5,3,6,-5,-1,4,1,1,4,-2,2,5,9],[7,1,8,-5,3,-9,8,7,1,7,1,1,-4,-5,2,-6],[-9,-5,2,7,1,8,-4,-1,-5,9,4,3,7,-7,-3,10],[-2,6,4,3,-1,-7,6,-2,-10,8,2,-2,-9,-10,5,-2],[-6,3,4,-7,9,-10,4,7,-4,8,6,7,-10,-6,6,2],[-6,1,-2,-5,-2,7,8,2,1,-9,9,-2,2,3,-8,9],[-9,6,-9,-2,7,-1,-5,8,-2,-5,-5,-1,7,-5,7,8],[6,-7,4,-8,-3,5,-3,-4,-2,-7,5,3,9,6,-4,4],[-8,-5,-4,-3,-3,5,-1,-10,-7,9,-4,-4,10,1,-6,-4]],[[-5,7,3,6,-10,1,-9,6,9,-10,8,3,5,4,8,4],[-6,-5,-2,-4,-2,-6,5,7,-7,-6,-10,-5,-5,-4,6,8],[-10,-10,4,7,-8,-6,-4,8,7,-6,-2,-10,9,-2,4,8],[3,-8,-9,-4,9,1,-3,3,-2,-7,-10,-1,-2,6,3,10],[10,-6,5,8,-1,5,8,6,-9,-4,3,-7,-8,-1,-7,-10],[8,-7,-7,-7,4,4,2,-1,6,-9,1,-4,-3,2,7,-6],[-8,-10,-8,3,10,3,9,4,-9,6,3,1,-6,-3,-6,6],[1,-1,4,10,-3,-6,9,10,5,10,-6,1,7,-3,-2,-9],[8,10,5,-3,-5,1,-1,3,-8,1,5,8,-5,-5,3,-9],[-3,10,-1,6,-6,-9,1,4,-5,5,-8,-2,-5,1,10,-8],[9,2,-5,-5,7,-9,-3,8,-7,-8,6,-7,4,1,-7,10],[7,7,10,2,-3,-8,1,6,8,4,-3,-7,10,-2,6,-5],[4,4,2,-5,-6,-5,6,-8,5,-10,-2,7,6,-9,1,-5],[3,-3,9,4,-1,-4,-2,3,2,-8,-4,-6,-4,3,8,2],[-1,-8,5,6,5,-2,2,-4,1,-1,-9,-5,2,8,-8,-3]],[[9,9,-5,7,5,-7,-7,5,5,4,5,-6,-9,-8,9,8],[-3,10,-10,-8,-8,-3,-7,4,-4,-5,8,-5,8,-6,3,4],[10,3,-1,-6,7,-4,8,6,4,1,5,-1,-1,9,-2,1],[-7,4,7,-6,9,-7,-8,1,4,-6,-1,-3,7,-6,7,10],[4,-1,-4,-3,7,-4,-3,-8,10,-8,-2,-3,5,9,9,-3],[5,-1,-2,-6,6,-5,6,10,7,6,8,-2,9,4,-1,8],[-2,-9,-5,3,-4,2,2,-5,-9,2,-8,-2,-6,-2,3,4],[-1,2,-5,-7,5,-8,-9,-8,4,6,4,9,-4,6,-3,5],[-3,-1,-1,-9,8,-3,-2,7,-1,-6,-3,-3,-7,6,-9,-5],[-7,-1,5,-3,7,1,-7,5,-3,2,-7,-3,-6,-4,10,-9],[4,-3,10,-1,4,-8,10,10,6,9,1,-6,3,-3,-9,-9],[-2,9,2,3,-2,8,6,-5,-4,-6,8,-1,3,-3,-8,-5],[-7,-4,-6,7,-10,2,-5,-10,3,3,7,-2,9,3,10,-8],[4,-7,1,-8,9,10,-7,2,-4,1,8,-6,-1,-4,6,-9],[6,-1,-10,-1,-9,2,9,5,-10,9,-10,-4,-3,-3,2,1]],[[9,-8,-3,9,-10,-9,8,4,-10,3,7,2,-10,1,10,2],[6,-10,7,-10,-4,-7,10,-8,6,2,-3,-5,1,4,8,3],[-4,-10,4,-9,8,1,-9,10,-2,-9,9,7,10,3,5,-1],[-9,-1,4,3,6,-9,5,-10,-6,-2,-5,-6,8,4,-5,2],[9,-9,5,-4,-6,-8,4,7,-9,4,-8,10,10,-1,10,-1],[9,1,-1,-5,-7,7,-10,-3,5,-4,8,3,9,-4,-1,9],[4,6,-6,2,3,-7,8,-6,7,-8,-4,-2,-6,2,-1,7],[-3,-1,-3,2,-6,3,-1,7,-6,1,-5,-3,-9,-8,7,6],[-8,7,-1,9,10,-1,8,-8,-4,-6,-4,-10,7,-5,-5,2],[-9,-7,2,10,-6,4,9,-2,-1,-2,9,-9,-3,-9,-5,-2],[-4,5,-4,7,-3,6,2,-7,-6,9,-4,-2,-3,5,-3,-2],[-7,2,-1,-1,-9,10,-5,-8,7,-6,8,-10,-10,10,-4,-2],[-1,-10,3,-7,-6,-8,4,-2,1,-6,6,1,10,9,6,-3],[-6,-7,4,-3,-3,-3,-5,9,-3,-7,10,-6,1,-4,-7,-4],[-2,1,-7,8,7,6,-8,-10,-10,1,6,8,-3,4,1,-4]],[[-9,1,-1,-5,-2,-10,5,-3,-8,-5,-2,-2,5,-8,4,-9],[8,8,-9,-8,3,1,-8,3,9,-10,10,9,-10,4,-8,6],[5,5,-6,-6,3,-6,-4,-6,-6,-5,10,2,2,3,-10,-5],[-2,8,-5,10,-4,8,-5,10,-1,-6,10,1,5,-3,3,-8],[10,7,-2,3,1,-1,-6,-8,7,-9,5,2,-4,-2,3,-1],[10,10,3,8,-7,-2,2,-3,7,10,2,1,5,2,-5,-2],[-1,7,-8,-9,3,-9,5,-4,5,-4,3,4,9,7,9,1],[2,5,10,-6,-7,-8,8,-5,-7,10,6,-10,-10,-1,6,10],[-9,-1,-10,1,-3,-10,-2,-4,5,9,-9,-6,-7,7,-10,-3],[-3,7,-3,-1,-9,7,-7,10,-6,3,9,-4,8,-10,-2,7],[-9,-7,3,7,8,-5,9,-6,6,2,-1,-2,2,7,-4,7],[9,6,-3,-5,-10,-5,8,4,3,1,-2,10,4,-8,-2,-4],[1,4,-4,5,1,-1,-3,5,10,-9,9,-8,7,-3,-1,1],[-6,5,3,-2,-4,-5,9,-3,6,-5,1,7,-1,10,-7,5],[-5,-3,-4,5,1,5,10,3,9,-2,-3,-2,-1,-10,3,-4]],[[-8,7,4,-10,-1,-7,10,-6,7,-3,9,7,-8,-8,2,7],[9,-4,7,-9,6,9,5,-6,5,3,5,-4,4,-1,-4,-8],[4,9,3,-10,-4,-4,-6,1,2,-5,-3,9,1,-6,10,-9],[6,-6,5,-10,6,-10,-6,4,-5,4,-8,-7,-3,-3,7,-9],[-9,3,-2,-5,-7,-1,-5,1,-1,-8,-8,-7,8,-3,-3,1],[7,8,-7,10,-7,6,-3,10,10,5,4,10,-2,-10,-5,-9],[-5,6,9,3,-4,-5,-6,2,-4,-5,-9,-2,-7,-7,5,9],[-10,-9,10,4,3,-2,4,-6,-1,9,-5,2,-5,-8,-3,-8],[1,-4,3,6,5,6,2,-10,-2,-2,9,-1,-4,-7,-8,-2],[6,2,3,-5,4,10,3,8,10,-4,-5,-5,6,6,9,-2],[5,2,10,8,1,1,-9,-9,8,-8,-10,3,-7,9,6,-8],[-3,-9,-10,-10,-5,4,7,-3,-7,-9,-5,3,1,7,3,-10],[-8,1,8,-8,2,8,-5,6,3,-1,10,-2,5,-10,-7,-7],[9,-2,1,9,3,-5,-10,10,-6,6,6,7,-9,2,-7,-8],[8,3,-1,-3,2,3,-8,-7,-4,2,-1,3,-6,-4,1,9]],[[-4,-9,7,-1,1,-10,7,-5,10,-2,8,9,-10,7,8,3],[8,-9,7,1,6,-8,9,-5,-3,-10,-4,-5,3,-6,-5,5],[2,-8,5,-6,3,3,7,10,9,-3,10,-7,-9,4,-3,-9],[4,-1,-7,10,-1,3,-3,10,-5,-6,10,-8,8,2,2,6],[9,2,6,-7,7,5,-4,-3,-9,-2,4,-7,-3,-6,2,-8],[1,6,-2,-4,-2,-10,-5,5,-1,4,-8,-10,4,5,-7,-5],[-5,-6,6,7,-1,6,9,2,10,-5,-9,-1,-10,8,-1,6],[6,4,-3,1,7,10,9,-6,-9,9,-8,10,-9,5,-1,-8],[4,10,5,1,-9,10,2,8,8,9,10,-4,-8,-10,2,10],[2,-3,-1,10,3,7,7,9,5,-9,-9,-3,-4,8,1,-1],[-7,-3,-7,6,5,9,3,5,-6,-10,-9,-2,5,6,7,2],[-2,-2,-8,-10,4,-2,7,-4,2,-8,6,-4,9,9,-9,-1],[6,9,2,4,9,4,3,-9,-1,-10,6,-7,5,-4,-9,-3],[-6,6,2,-5,-7,-8,-6,-7,-5,-1,-10,7,-6,-10,-4,9],[-7,-2,-6,1,6,4,-8,9,10,4,10,-7,-2,3,-2,-10]],[[7,8,-6,7,-2,-6,-1,-4,4,-3,1,3,7,-3,-10,7],[-2,-1,8,4,8,-10,2,-4,-4,-1,6,-10,1,3,-6,-9],[9,-9,-9,-7,-3,-7,-1,-1,7,1,7,-10,5,-8,-6,-1],[8,-2,-3,5,5,10,5,2,5,-7,7,9,-3,-4,5,-5],[-5,9,7,-5,5,10,-9,4,-8,-4,-8,-6,9,9,-3,-6],[-3,-8,8,3,-9,5,-7,-9,10,7,-6,1,3,1,6,6],[-10,-8,-8,-4,-3,-4,-8,5,-8,-5,5,2,-8,6,8,-1],[-6,1,-1,-2,3,-7,1,-8,4,5,-9,-9,-10,9,7,-10],[-1,1,-5,-6,-9,9,5,-2,1,10,6,7,6,-6,7,8],[-9,10,1,2,1,3,9,4,-3,-9,6,5,-1,-7,-10,-6],[3,3,-4,-6,-6,-10,6,-6,2,8,-1,-2,-7,-1,-3,6],[-5,-1,-3,5,-10,6,-10,-3,-8,-2,5,3,10,-8,5,10],[2,10,-2,5,-1,-6,-5,-5,1,4,-9,1,-5,4,-3,-9],[-8,10,-5,2,8,-8,10,-6,1,8,-8,-1,7,10,-2,7],[-1,1,-4,3,4,4,5,4,9,5,-10,10,-4,9,1,-9]],[[7,-8,5,-4,3,1,-8,-5,7,-6,-8,6,9,1,5,4],[-10,-4,6,-3,4,8,-9,10,-2,-4,-5,4,10,-3,5,-7],[-10,9,-9,-4,8,-6,2,4,-4,-6,-1,-2,8,-7,3,-10],[-7,10,1,8,5,-8,-9,4,-1,4,-3,-4,-2,-5,-7,9],[-2,-7,-2,-4,-8,-5,-5,2,-9,9,-3,-2,7,9,10,7],[6,9,-8,6,-7,5,-1,-9,5,2,-4,2,-4,5,-8,8],[-6,-3,-3,-2,-9,-4,6,-1,-5,7,-9,-1,10,7,-8,-4],[-5,1,-4,-10,-10,5,10,-6,-9,2,-2,1,1,-1,-6,-5],[2,8,-1,-10,5,-8,1,7,7,-10,-4,-2,-2,6,-2,8],[1,1,-6,-4,6,5,-3,9,-4,10,1,-5,-9,-10,3,4],[-6,5,-5,3,10,1,8,5,3,2,-9,7,-7,8,5,-4],[-6,10,-8,5,1,-1,-7,3,-4,-4,-1,3,-7,7,-3,-10],[-10,10,-5,5,-10,7,7,-9,-4,-5,3,-2,-9,2,-10,10],[-5,9,5,8,-4,-7,4,1,-9,2,2,-4,-10,2,-1,1],[5,5,-4,7,7,-9,10,-8,6,-10,-3,9,3,7,-4,-9]],[[8,8,9,2,-9,-7,-10,-7,7,7,6,-7,-7,-10,-3,-1],[4,-3,-7,7,5,-7,2,-3,5,-1,8,-9,-2,-8,-7,4],[-10,-4,-1,5,6,-2,7,-7,7,-5,-6,10,3,-3,-8,-2],[5,5,7,-3,-3,-1,-4,5,8,6,4,4,-5,8,5,2],[-5,7,1,7,6,-4,-8,-2,1,-2,6,-2,4,-6,9,-2],[-7,8,-10,-1,7,-9,-6,-3,10,4,3,9,-4,-8,-3,9],[9,7,6,-6,-5,8,-5,-10,6,3,10,9,-4,-8,7,-6],[-9,-6,3,6,6,-9,4,-7,5,-2,-9,8,-7,-10,-6,-3],[-1,9,-10,2,-8,-8,-2,7,-5,2,-1,7,9,-4,-6,-9],[5,-1,-3,-2,5,5,5,5,-10,-3,-9,9,-10,2,-2,-2],[-9,2,7,-4,4,-10,-1,10,-3,-4,-3,-10,-8,10,-5,4],[5,-5,2,5,-1,6,1,5,8,8,-2,6,-1,7,7,10],[-1,-6,-8,-8,5,1,7,10,5,7,-6,-7,-7,5,-8,-8],[1,2,5,6,-2,-6,3,6,-3,5,-8,-8,-9,-1,-7,-7],[-6,-8,7,-3,-3,1,6,-5,-2,10,-3,7,1,-10,-10,7]],[[-4,-7,8,-1,10,8,9,6,-6,-3,7,2,1,-4,-6,7],[5,10,-5,-6,-3,10,8,7,-4,-2,2,7,-3,-4,-4,-9],[-6,-2,-2,-3,-3,-8,9,-6,8,4,-1,5,5,-4,-2,-8],[4,7,-10,-10,5,5,-5,-9,-8,-3,5,4,-7,9,-3,-8],[-8,-2,7,-5,-4,-6,-3,2,-7,2,-2,2,-5,9,-7,-5],[-3,-7,-3,-3,-3,7,-6,-7,3,7,-4,-5,7,8,-2,-10],[4,-3,10,-5,7,-8,1,7,3,-9,10,-9,-7,-2,-4,4],[-2,6,-5,4,2,-4,-5,5,5,-8,-8,-4,4,6,8,5],[-8,-9,-1,-4,5,4,-3,10,4,2,3,-9,-2,6,-6,10],[-1,7,-2,-4,3,8,8,-3,-4,-6,-1,-5,-9,-10,3,9],[9,-5,-8,-9,-9,-6,-5,-1,4,-7,2,5,-4,-6,-5,10],[-10,-6,-5,9,3,3,4,8,-3,10,-10,9,-10,-10,8,10],[6,6,2,-7,3,-7,-6,-7,-2,6,-4,4,10,10,6,7],[5,-5,-1,5,2,2,-7,-9,-8,8,2,5,-8,9,4,-9],[-9,9,7,-5,4,-9,6,9,-4,5,9,-7,6,4,-4,-10]],[[-7,5,3,-3,7,9,1,-7,-2,-3,4,-1,-10,10,-8,-6],[-1,9,9,10,-5,9,-6,-2,-1,-1,-7,-5,7,-8,8,-8],[-5,3,-2,-9,-2,2,7,6,1,4,10,-4,9,-10,7,5],[8,7,-1,-6,7,10,-3,3,-4,1,-10,-2,10,5,-3,-1],[-8,-10,5,1,3,-7,10,2,8,-9,-10,-7,-3,8,-3,-7],[-7,10,-1,3,4,2,-1,7,8,8,-7,10,9,5,9,3],[-7,8,-7,3,1,7,-10,1,-2,-9,8,-8,9,7,5,6],[4,-9,-4,-4,10,9,6,9,3,-7,-9,-5,8,10,3,-5],[-7,10,9,-8,-7,-8,-9,1,8,10,-2,-10,9,2,-4,-1],[-1,4,-6,8,3,6,-6,-3,-4,-4,2,-7,-3,-4,-5,-10],[7,6,-10,9,-4,-5,-4,5,-3,-6,-4,-5,1,-4,4,3],[-9,7,7,1,2,2,-6,6,7,-4,5,7,-1,-2,-2,6],[-8,-1,8,-6,9,6,4,-5,-4,-1,-2,-4,-7,6,3,-3],[5,-8,7,1,10,1,9,-5,7,-9,2,10,2,-3,9,8],[1,5,7,-1,-5,-1,8,-5,-1,4,10,5,9,8,5,2]],[[-3,-1,4,9,4,-4,-5,-7,-3,-2,-4,-6,-6,-3,-2,6],[-1,-6,-8,-6,5,5,9,8,3,-7,-6,2,-7,4,9,5],[-6,-6,-5,9,10,-2,7,3,10,9,-4,10,5,1,4,3],[-4,-6,-9,1,-8,10,-2,9,4,-10,8,-8,-3,-6,-4,7],[-6,-10,-6,6,-3,3,-1,7,-8,-2,6,9,10,4,-4,5],[-4,7,-6,-5,-1,-4,9,-6,10,-5,-9,-4,2,6,-1,-8],[-7,-4,-9,-4,9,1,-1,9,6,-6,10,7,-9,10,5,4],[2,-7,-9,9,8,8,-10,9,-10,-2,-4,-2,1,3,-9,-10],[-7,4,-5,-5,-5,-2,-9,3,-5,-10,6,-4,-6,-5,-7,8],[9,1,-4,-6,-9,-6,-9,-8,5,-7,-9,-8,-1,-10,5,2],[1,-7,-8,-6,3,-5,-2,-1,2,8,1,6,10,-10,-7,10],[-4,3,-1,-10,10,1,10,-10,1,6,7,-6,10,-1,-8,5],[7,-5,6,7,3,-9,-9,5,-1,4,5,-5,7,3,9,7],[-5,-6,-10,-6,-10,-5,-8,-1,-3,6,-6,-2,9,8,3,-3],[10,9,2,-10,-2,5,5,-8,-10,6,-5,9,-4,-1,-2,5]],[[-4,1,-2,2,6,-4,1,1,6,1,6,5,-7,-6,9,-1],[6,10,-3,-1,-8,-1,-7,-4,2,4,5,9,-4,-1,6,7],[-3,9,-1,-4,5,10,2,5,-9,-3,8,6,-6,-8,-8,4],[4,-7,6,-4,9,-3,7,-6,-8,-3,-2,10,-8,10,-3,-7],[-2,2,8,-6,-7,9,-10,-4,-5,-7,-8,4,-7,-1,-1,-7],[-5,-10,4,-1,7,-9,-6,-7,10,7,-3,3,5,10,6,-10],[8,-5,6,-5,5,-9,-5,-1,2,-2,-9,5,-10,-10,4,-7],[-10,5,8,8,-2,-6,5,3,-5,2,-9,-8,2,5,-9,-6],[-3,-2,3,-4,-9,3,10,-9,8,-9,-8,5,-6,-4,3,2],[3,8,-6,-2,-5,-6,10,9,9,-6,-6,7,-3,5,-2,-1],[4,2,4,-4,-8,3,8,-7,-10,5,4,-8,-2,-3,1,-3],[7,-5,-9,9,9,-7,-4,5,-7,-9,-2,-10,-1,3,10,7],[1,-8,8,10,-9,-4,1,-8,10,1,-6,10,-5,9,9,3],[-7,10,10,5,-9,4,-8,10,10,4,2,3,-7,5,8,3],[10,-3,5,8,6,-4,4,6,5,10,-4,-7,7,4,-9,-3]]], dtype = "uint16")#candidate|3271|(16, 15, 16)|const|uint16
var_3272 = relay.var("var_3272", dtype = "uint16", shape = (16, 15, 16))#candidate|3272|(16, 15, 16)|var|uint16
bop_3273 = relay.not_equal(const_3271.astype('bool'), relay.reshape(var_3272.astype('bool'), relay.shape_of(const_3271))) # shape=(16, 15, 16)
output = bop_3273
output2 = bop_3273
func_3279 = relay.Function([var_3272,], output)
mod['func_3279'] = func_3279
mod = relay.transform.InferType()(mod)
mutated_mod['func_3279'] = func_3279
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3280 = relay.var("var_3280", dtype = "uint16", shape = (16, 15, 16))#candidate|3280|(16, 15, 16)|var|uint16
func_3279_call = mutated_mod.get_global_var('func_3279')
call_3281 = func_3279_call(var_3280)
output = call_3281
func_3282 = relay.Function([var_3280], output)
mutated_mod['func_3282'] = func_3282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_3319 = relay.TupleGetItem(func_1015_call(), 0)
call_3320 = relay.TupleGetItem(func_1016_call(), 0)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_3336 = relay.TupleGetItem(func_167_call(), 0)
call_3337 = relay.TupleGetItem(func_168_call(), 0)
output = relay.Tuple([call_3319,call_3336,])
output2 = relay.Tuple([call_3320,call_3337,])
func_3342 = relay.Function([], output)
mod['func_3342'] = func_3342
mod = relay.transform.InferType()(mod)
output = func_3342()
func_3343 = relay.Function([], output)
mutated_mod['func_3343'] = func_3343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2515_call = mod.get_global_var('func_2515')
func_2517_call = mutated_mod.get_global_var('func_2517')
call_3355 = relay.TupleGetItem(func_2515_call(), 2)
call_3356 = relay.TupleGetItem(func_2517_call(), 2)
output = relay.Tuple([call_3355,])
output2 = relay.Tuple([call_3356,])
func_3367 = relay.Function([], output)
mod['func_3367'] = func_3367
mod = relay.transform.InferType()(mod)
mutated_mod['func_3367'] = func_3367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3367_call = mutated_mod.get_global_var('func_3367')
call_3368 = func_3367_call()
output = call_3368
func_3369 = relay.Function([], output)
mutated_mod['func_3369'] = func_3369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2010_call = mutated_mod.get_global_var('func_2010')
call_3375 = func_2009_call()
call_3376 = func_2009_call()
func_389_call = mod.get_global_var('func_389')
func_390_call = mutated_mod.get_global_var('func_390')
call_3379 = relay.TupleGetItem(func_389_call(), 0)
call_3380 = relay.TupleGetItem(func_390_call(), 0)
output = relay.Tuple([call_3375,call_3379,])
output2 = relay.Tuple([call_3376,call_3380,])
func_3383 = relay.Function([], output)
mod['func_3383'] = func_3383
mod = relay.transform.InferType()(mod)
output = func_3383()
func_3384 = relay.Function([], output)
mutated_mod['func_3384'] = func_3384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2693_call = mod.get_global_var('func_2693')
func_2695_call = mutated_mod.get_global_var('func_2695')
call_3439 = relay.TupleGetItem(func_2693_call(), 1)
call_3440 = relay.TupleGetItem(func_2695_call(), 1)
func_614_call = mod.get_global_var('func_614')
func_615_call = mutated_mod.get_global_var('func_615')
call_3441 = relay.TupleGetItem(func_614_call(), 0)
call_3442 = relay.TupleGetItem(func_615_call(), 0)
output = relay.Tuple([call_3439,call_3441,])
output2 = relay.Tuple([call_3440,call_3442,])
func_3453 = relay.Function([], output)
mod['func_3453'] = func_3453
mod = relay.transform.InferType()(mod)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3453_call = mutated_mod.get_global_var('func_3453')
call_3454 = func_3453_call()
output = call_3454
func_3455 = relay.Function([], output)
mutated_mod['func_3455'] = func_3455
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3461 = relay.var("var_3461", dtype = "uint16", shape = (14, 8, 10))#candidate|3461|(14, 8, 10)|var|uint16
const_3462 = relay.const([[[-1,9,9,-2,-1,-7,-8,-3,-1,-1],[5,-4,-8,-3,1,8,-4,5,10,-2],[-8,4,-6,-1,7,10,9,10,4,-6],[7,-7,2,4,-9,6,5,-7,6,-8],[10,-5,-3,8,8,-10,-9,-6,9,4],[-6,9,-10,-4,4,9,1,-3,-1,-2],[7,6,1,1,-1,9,-5,1,-5,-2],[-7,3,5,2,8,-6,8,-3,1,-8]],[[-8,10,-7,1,-5,3,3,2,1,-3],[8,4,-1,-4,2,5,-8,5,5,9],[8,2,7,9,-7,-7,-4,-2,1,-7],[7,4,8,-5,7,5,-8,-7,2,-5],[10,8,4,-9,8,-7,-10,2,-2,5],[1,-5,8,5,9,10,3,-5,8,3],[2,10,-3,-1,9,4,-5,-10,2,2],[-5,-1,8,7,-10,1,2,-3,4,-2]],[[10,-3,-5,-8,6,8,-2,-2,-7,-6],[1,8,-9,-8,6,5,6,-3,-1,-9],[10,-10,8,-3,-3,1,-6,-7,1,9],[-5,-5,2,-5,-8,-2,4,1,8,-7],[2,-4,7,7,-7,7,-9,-7,8,-6],[6,7,1,-10,-1,-9,6,-5,-7,3],[7,7,2,-10,4,9,5,-8,3,7],[-6,8,2,-5,8,-2,-7,2,3,-10]],[[-10,-8,4,-1,-5,-10,7,-5,3,-9],[-9,5,-9,5,-1,-10,-5,-3,-6,5],[-5,4,-3,2,-8,-9,1,3,3,4],[7,2,-4,-3,3,4,3,1,-7,-5],[1,2,-8,-2,4,-4,1,5,4,8],[7,5,-9,7,-9,-1,-6,4,7,-8],[3,-4,-9,2,8,-3,3,5,4,8],[-4,-6,1,8,-6,-10,8,3,-4,3]],[[8,-7,5,3,-3,5,-7,2,8,7],[-4,-3,3,-2,-5,-9,2,-2,-9,6],[-5,1,-1,1,1,-3,6,-9,-4,-6],[-5,-1,-2,-4,9,2,1,7,4,-1],[-5,2,-4,8,2,-8,10,4,2,4],[-7,7,-10,2,-10,1,-1,7,-5,-3],[1,-4,9,-7,-5,4,9,-4,4,5],[8,1,10,-5,5,2,7,10,-5,1]],[[-8,-3,-6,8,-2,-8,-10,2,-7,6],[2,9,-5,7,6,9,-3,-4,9,1],[-4,4,7,3,10,7,7,-1,-7,-10],[6,-10,2,-10,-4,4,9,10,-3,-2],[-2,5,5,4,6,-6,5,-3,-7,-10],[5,9,-2,-2,1,6,-2,-7,-8,-8],[6,7,9,-8,5,7,2,4,4,8],[7,-3,6,-6,2,7,10,-9,5,7]],[[-5,-10,2,-2,-7,4,-4,-2,8,5],[4,9,-7,4,6,-4,8,10,7,6],[2,-9,-8,7,1,-7,-3,10,5,-3],[-7,-3,-2,-5,-7,-4,-1,-5,4,-7],[3,1,-10,-5,-6,5,-9,10,-3,2],[-8,-9,1,-9,6,-9,10,5,10,-5],[10,2,8,3,-9,-1,1,-5,4,7],[-2,10,-8,-3,5,-5,-8,4,-8,-9]],[[-2,-3,10,7,-2,7,3,-7,2,-9],[8,2,10,-3,-5,-5,-3,-1,-6,1],[3,3,5,6,8,4,1,3,4,-2],[-10,-7,7,10,-4,-3,-10,4,-4,3],[-10,-1,5,-2,2,9,3,9,-3,5],[-1,-6,-3,-6,-5,-1,6,-3,6,1],[3,3,7,6,-2,-7,9,4,6,-1],[9,-3,5,-7,5,-10,9,4,7,5]],[[-1,2,6,2,-6,-2,-6,-1,2,2],[7,4,9,-1,8,-6,8,10,8,7],[-6,10,-3,3,-8,-1,-10,10,-4,6],[8,-4,-3,-2,8,-4,8,8,-4,5],[7,6,2,7,-8,-2,6,-3,-2,-10],[4,-9,-10,4,-8,-8,4,4,-2,5],[-3,-6,-5,-10,4,9,5,-2,5,-3],[-4,7,6,5,-2,8,7,8,3,-1]],[[9,-6,-10,-1,4,-7,4,-6,7,6],[2,-7,-8,-1,3,7,-3,-6,3,7],[1,6,10,-6,3,-6,-8,4,-8,-6],[-8,-10,-5,-4,-6,-6,5,-2,5,-1],[2,3,-2,5,-1,-10,-3,2,9,-8],[8,-1,7,-9,-1,-3,10,2,-5,2],[7,7,-4,-2,6,9,-6,-7,4,-9],[8,8,8,-10,7,10,-5,6,5,-6]],[[7,-3,4,10,-7,4,1,-1,-2,-3],[-6,2,8,-3,-3,-4,-4,5,-8,-7],[4,-8,3,-3,2,-3,8,2,-1,-9],[-5,7,9,-9,-9,-9,10,-7,9,-10],[-7,-1,-6,1,7,-4,-2,-2,-4,-9],[9,-5,7,4,3,1,6,-5,5,2],[7,-6,6,1,1,5,9,-1,-4,-4],[-6,9,5,4,1,3,1,-6,-9,1]],[[8,-10,-5,-5,3,-6,-2,-2,-10,-8],[2,8,3,4,-4,10,10,10,10,-6],[3,-3,-8,4,1,8,5,1,-1,-10],[10,8,-1,-7,4,-3,5,3,-8,3],[9,5,7,-4,10,5,5,2,-10,6],[-4,10,-4,5,10,-3,9,-2,1,7],[9,1,-3,-1,-4,6,7,-7,1,-5],[10,-7,-8,-5,7,2,4,-10,-8,10]],[[8,-10,-4,-8,-1,-5,2,1,-2,-9],[-10,5,-6,-1,-5,-6,8,10,7,6],[-10,10,-4,-2,-9,7,3,1,8,4],[2,-8,8,-2,-3,-2,1,7,-4,6],[-1,3,7,-5,-6,8,-1,-10,-4,5],[-3,2,-10,1,-7,7,2,-6,-4,5],[2,-1,2,3,2,-3,4,10,4,9],[-10,9,-6,4,6,3,-5,-2,-4,2]],[[2,2,3,-1,3,8,6,-7,2,4],[1,7,-2,10,3,-3,-9,2,-6,1],[-5,-5,6,-5,3,8,9,-9,-4,6],[-3,4,-5,-8,-1,2,-7,7,1,4],[3,10,-9,2,10,-5,-8,-6,5,-6],[2,4,-9,5,-5,5,-10,2,6,7],[4,10,8,7,-10,4,2,-3,9,10],[4,-1,-2,8,-7,-5,-4,2,-1,-9]]], dtype = "uint16")#candidate|3462|(14, 8, 10)|const|uint16
bop_3463 = relay.bitwise_and(var_3461.astype('uint16'), relay.reshape(const_3462.astype('uint16'), relay.shape_of(var_3461))) # shape=(14, 8, 10)
output = relay.Tuple([bop_3463,])
output2 = relay.Tuple([bop_3463,])
func_3466 = relay.Function([var_3461,], output)
mod['func_3466'] = func_3466
mod = relay.transform.InferType()(mod)
mutated_mod['func_3466'] = func_3466
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3467 = relay.var("var_3467", dtype = "uint16", shape = (14, 8, 10))#candidate|3467|(14, 8, 10)|var|uint16
func_3466_call = mutated_mod.get_global_var('func_3466')
call_3468 = func_3466_call(var_3467)
output = call_3468
func_3469 = relay.Function([var_3467], output)
mutated_mod['func_3469'] = func_3469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2699_call = mutated_mod.get_global_var('func_2699')
call_3515 = relay.TupleGetItem(func_2698_call(), 0)
call_3516 = relay.TupleGetItem(func_2699_call(), 0)
const_3519 = relay.const([[[7.844774,9.227966,-8.455839,-3.151184,-5.882501,-7.037952,5.985593,-7.877224,-2.931234,6.216592,-6.147116,-3.652726,4.539378,1.917560],[2.077947,-2.274966,-1.280514,-2.051221,6.473774,-9.079182,-5.149036,-0.592752,-9.042520,5.249465,4.319289,-7.145145,7.245152,8.061065],[-8.763298,1.744149,0.855733,6.351336,-9.152822,-6.932554,-2.510474,3.985334,8.134906,-5.274111,-6.083144,6.496857,-1.090452,-2.617067],[-5.438427,0.103388,-2.951136,5.874762,-6.201411,5.150963,-4.549188,-5.357051,-7.003054,1.292454,-4.582344,9.352071,4.086573,-9.595521],[-0.192163,2.688567,-3.101271,-5.816164,-9.511978,-0.803329,-2.501933,8.628461,-9.128465,0.504343,3.622211,-7.210455,-5.708938,4.731373],[-4.140479,-7.445022,-3.561032,-5.816771,-6.552288,3.206010,-7.607733,8.529807,-2.177733,8.831153,3.900916,6.421291,4.226945,-9.924421],[-5.860979,8.450818,6.793298,1.162989,-2.433475,1.408745,-5.720372,9.841798,-4.074599,3.755657,0.834329,3.355007,1.548042,3.215908],[4.391770,3.495505,5.054022,-1.281734,-3.845483,-9.254456,5.285921,0.364214,2.081364,-8.748186,0.923269,-0.589635,-1.780472,4.152295],[-0.411024,-2.947069,-5.728686,2.031848,4.987567,3.481565,-6.378989,-8.804506,3.170875,7.101192,-2.023985,-0.024692,-7.730145,-6.756608],[6.028029,-8.883124,-1.746890,0.342740,-0.227730,2.123502,-3.741141,7.268852,-0.645287,7.082658,3.023063,-9.217079,-5.680225,-3.119729],[0.213946,-9.267235,-4.981798,3.389638,5.347154,-4.129685,6.427793,0.211805,-8.648972,-4.459205,-1.554332,-6.782729,3.037691,6.345434]],[[5.924469,-9.348188,-3.448775,8.278748,0.435774,-9.353721,0.182891,4.743946,-6.460269,4.242387,6.779603,2.871068,1.637494,-7.316528],[1.038916,-0.796999,2.925290,3.765018,7.037840,-5.335737,8.699602,-8.881067,0.948441,-9.966081,-3.923343,-9.446558,2.006074,-8.264022],[6.892019,7.990645,-1.177471,-4.710243,-9.514139,-8.784267,-5.090269,1.033294,6.989734,6.940774,4.645161,-8.128350,0.622146,3.971161],[-2.694719,0.496845,-0.692041,-1.757803,-0.118270,-6.065073,2.641471,8.055934,-4.971553,3.238360,-0.902196,-9.077276,-9.959642,8.860098],[-6.040441,8.856035,-7.098592,-4.238443,8.442433,-4.032752,1.062331,3.080407,3.388876,6.471119,4.337026,4.870158,5.424667,9.392629],[-8.253536,6.650328,7.666400,2.443551,7.209366,3.715228,0.653726,-1.995564,-1.089627,1.658860,-0.025099,9.366113,7.276170,3.108532],[4.095922,1.690116,-4.472587,-9.704927,3.910622,8.842971,4.377302,3.249243,-2.723773,-5.137963,8.711554,-2.498908,-9.280680,7.113151],[-5.152473,-9.510980,7.946398,3.990191,-7.915185,-9.080127,-6.483724,-4.607935,-8.634034,-4.188817,0.660898,8.567075,-7.854723,9.451030],[-9.498491,-4.690039,2.145476,-2.915629,-9.041680,-0.341465,6.236231,-7.026276,8.526287,5.262874,8.866455,-2.610525,-6.063522,5.880254],[-1.948703,4.714097,-5.737513,6.787551,-7.958459,-6.146915,-6.274957,9.535199,1.491948,1.488304,-9.962382,-0.584478,-8.903662,8.867090],[7.748811,3.023784,6.983374,-2.140739,-4.569821,2.812183,6.247762,-6.123046,8.778168,4.320380,8.984820,7.834076,4.022760,3.185397]],[[-4.689661,2.459824,-4.456636,0.345250,1.084802,9.708339,-5.653747,8.043318,-3.323563,5.097783,2.721296,8.398779,3.556706,8.887589],[-8.960859,-7.446958,3.529909,-4.042261,-2.030946,2.794808,9.969126,2.186591,3.262641,5.433393,-9.642310,9.152147,9.580556,4.301636],[3.205571,-1.728874,2.718502,0.563946,-8.747337,-6.780412,3.593006,-9.895341,-0.269264,-3.771186,-0.355042,-4.640512,-3.973128,2.722446],[-8.652391,-0.399557,8.963025,6.046827,4.426872,5.984592,2.868791,-3.904804,7.082136,2.824310,3.317568,3.334744,-8.433120,-0.035720],[-4.710173,-0.904422,-4.198234,-0.733806,7.017151,6.808160,-3.895125,-7.645748,-8.896684,4.040906,-3.420755,-7.250733,-5.686034,4.446710],[7.162255,-1.016708,1.080451,-8.698463,4.888316,0.378244,-1.868464,-9.818752,7.941916,-4.645849,9.295940,4.884551,2.816531,4.102626],[-9.705625,-7.064482,2.183456,6.561301,0.797001,-2.556306,-2.319054,-1.938160,-3.669601,-0.598878,2.845159,-4.483865,-9.139432,-0.310689],[3.000728,5.752373,7.311558,7.990712,-2.626628,2.413752,-9.676393,3.312884,-1.857265,7.328724,-6.241477,-8.274793,2.392355,-7.731057],[7.137578,9.003389,1.021978,-2.249159,-9.157202,1.758172,-5.211349,-5.330835,-2.157625,8.607286,1.997289,-9.879988,-8.967678,-7.968329],[9.033246,0.315078,7.388935,1.223671,-0.257474,9.067212,2.344281,6.601098,-0.996565,-0.723987,0.380575,0.773243,-7.165706,-3.941974],[-1.060385,-6.645367,-6.503885,-7.921119,-1.633615,-3.761074,5.516411,0.246247,-2.973841,-5.048807,1.923900,3.110026,6.957477,6.442597]],[[-2.595580,-7.267934,-1.828892,-8.895462,6.268736,6.582708,-2.012254,-3.897229,1.042897,-0.560213,-6.719490,-3.446544,7.879122,5.683443],[-0.201675,5.721154,-4.231434,-5.287832,-9.997459,7.622530,2.764046,-9.564287,-8.951824,-8.285396,-3.418682,7.319565,1.249080,-9.993227],[-6.939396,1.693251,4.563026,5.717556,2.453849,-0.808248,8.066733,5.008148,-0.943200,-1.316463,-4.636852,5.257450,-8.347704,4.413270],[-8.884535,-4.466072,4.555365,-9.629906,-7.100735,3.866010,7.264517,-4.720197,0.554272,4.280503,5.731320,1.533653,-5.191857,-2.147111],[7.329092,3.967709,-9.199992,-0.537993,1.763534,-4.253668,8.636407,8.000261,9.250933,3.245782,0.967315,3.823057,-1.147709,-6.082386],[6.556461,3.274154,6.007248,-3.065099,1.496909,3.652537,7.076108,-1.886188,8.891965,8.642435,4.978582,-7.029856,-5.973937,8.574142],[-2.960224,4.896572,5.747415,-3.215228,4.471365,-7.497984,-2.221078,-2.375444,9.844862,-5.661007,-1.419022,6.555931,-2.883947,5.842472],[7.889219,9.788210,-7.911630,4.104437,-3.389070,-7.246409,2.945809,-2.200340,4.015166,0.416401,2.427807,2.392172,-2.311781,-4.494111],[-2.281867,3.194746,-2.104158,7.484675,4.401661,-3.852399,8.209133,-0.686005,6.266190,-2.954803,0.547449,4.673901,0.087707,-8.061783],[-3.128917,-0.669312,-2.531775,-9.652978,-0.033525,-4.763104,2.905098,6.459480,7.732418,2.265629,-4.244831,2.537686,4.054905,5.385535],[-3.840751,-0.495402,-0.425853,9.673638,-8.690001,3.743536,-3.778563,7.443859,8.895992,-1.497783,-0.322810,4.898862,1.229808,-9.060625]],[[-6.024082,3.992993,6.241218,6.992437,-8.230133,3.393691,-6.326677,0.902289,-6.609741,-3.845881,-0.419534,-6.293418,-2.609127,9.204122],[5.184792,5.786701,6.253487,-8.442389,-3.567630,-6.767464,-1.223395,-5.404841,4.266468,9.904809,-1.754245,3.534872,-9.978594,0.979893],[1.400120,-1.533285,-8.342580,-1.011681,-3.092476,-7.511637,-2.576172,1.820813,-1.673806,-4.457301,-3.308733,3.902431,7.574679,9.473514],[2.810332,8.143685,8.497138,1.170908,7.627595,-1.359619,-9.135789,-6.087110,6.229530,8.533596,0.226307,5.141001,-2.912083,-7.345742],[4.066284,7.356103,-3.409000,-2.464243,8.400375,3.890042,3.536662,-4.907857,7.352176,2.712658,4.861920,-3.125476,-6.982280,-6.548323],[6.403571,-9.146545,-1.545683,4.555028,-6.332636,-5.044829,0.307326,-2.196335,0.829675,-7.765567,-9.477662,-1.570541,-7.896612,-1.243419],[-4.411385,3.354297,-1.217012,7.747989,-7.735928,4.516931,-5.820667,-3.625438,-4.513354,-3.315099,4.310147,-5.378088,-0.907274,6.757881],[1.880437,0.967369,-8.911624,4.152769,9.590401,2.602736,3.690607,-5.328662,5.815093,0.770204,-2.060794,9.052534,-4.868013,7.534319],[-4.560293,-3.685287,-7.952582,-0.986785,-5.309955,6.085780,-9.067799,5.706687,-9.232001,7.127188,-2.963648,6.740956,-8.359844,1.845871],[-5.393881,-1.268379,1.364732,-9.748912,-9.474694,6.079576,8.537217,-8.014573,0.713325,2.155324,-0.074610,4.833391,-1.340739,3.898888],[-6.234453,1.193009,3.183392,0.216875,-3.423723,-5.753285,-4.433098,-5.766305,6.252983,1.174413,-7.033558,-7.705788,1.050824,-0.533776]],[[-7.452152,9.263789,-1.860957,8.320660,-5.427949,-0.759320,-4.071966,0.756978,-9.687666,-8.415308,3.424531,6.695832,2.175471,-5.308391],[6.049731,-2.496266,-2.222338,-1.729798,-9.601874,-0.323698,2.797759,-6.041506,1.196481,-6.913713,1.176254,1.239619,4.744961,-8.497013],[-4.319365,0.951618,0.204198,2.876432,6.828318,-4.031267,2.686710,-0.551635,-8.802912,9.938544,1.492952,3.219276,-9.986555,0.846929],[2.779277,-9.914259,-4.557699,-6.196086,6.184162,7.469810,1.900379,9.963709,-5.081561,2.492460,-4.219164,-3.857181,8.798040,-5.803637],[0.898864,0.072097,6.504411,-8.981752,7.576652,-2.569592,6.911421,-7.535476,1.006139,3.951511,7.807215,-5.671096,9.852950,4.495833],[2.414345,8.424637,5.045237,3.184970,-0.021322,-2.922343,-9.368228,6.874311,-2.335723,9.757075,5.726006,5.555985,2.874756,-3.050289],[5.814217,0.360402,2.623470,5.678105,4.366485,0.410037,-5.652124,-0.940041,-8.613346,-5.579800,9.568286,4.505161,7.825345,9.502081],[-7.988677,2.210372,-9.032744,-2.774079,2.835662,-6.548471,3.031451,2.822486,-2.443651,-2.570687,9.731317,9.069745,-1.716004,9.459725],[-8.940803,7.542343,-8.714258,-1.298305,7.109349,-6.996521,-4.138011,-9.073604,-0.108321,7.280359,4.587957,-0.804164,5.419119,8.788979],[-3.234602,1.369158,6.801109,3.995817,8.464316,-7.386979,7.878157,-1.832997,-5.433140,0.533863,-1.952004,5.194685,-2.621620,-4.739966],[9.173268,-9.974720,-1.359791,-3.858719,-0.418161,6.182305,5.372768,-7.307689,-4.487058,-9.435058,3.183293,9.732878,8.042104,8.210900]],[[-5.008567,1.129325,5.363971,9.732438,0.311255,-3.742465,-2.782137,2.709688,6.152706,-8.649523,-2.626141,-0.601580,-6.275506,0.193767],[-9.460892,7.476848,-9.828635,8.974519,-6.232034,5.412458,-6.915650,7.667931,3.617494,4.875180,9.816177,-6.611982,-2.004852,2.783630],[6.815909,-6.492995,-3.358146,-1.977716,-0.757763,-4.773135,0.253157,-9.199125,7.147410,-0.224353,3.448518,-4.335209,0.239075,-7.151147],[8.628438,-4.935562,7.990313,8.787056,-0.777411,-6.947517,1.213834,-2.553673,9.408276,-1.138664,-7.646230,0.759031,-3.737396,-8.575366],[2.913691,-0.981533,9.703348,3.348776,4.327493,-0.656850,-7.207236,2.555978,0.068541,-1.869520,-6.152690,-1.143359,4.986882,-5.954035],[2.222366,9.092950,-6.073595,7.263810,-9.120261,-0.785178,8.180832,-8.670554,8.337418,2.537616,0.847800,3.414990,1.693404,-4.575247],[-0.212793,-1.034537,-2.790498,-6.351223,5.666697,-0.200024,-0.899913,-8.247056,2.313209,8.319189,-5.648935,9.454011,3.205120,4.607501],[-5.847102,7.869131,5.556894,-6.586314,-7.561685,-3.907733,8.390373,9.442315,2.718556,6.232149,-8.656894,7.829392,-6.114584,-0.154730],[-1.099012,-8.479743,-4.899455,2.915594,5.467291,9.596253,-5.733416,-8.444634,-7.638016,4.228343,2.745651,-8.248637,7.776214,-1.632368],[-0.205576,7.092009,-8.482286,-8.067942,-7.573517,-6.637201,2.746709,3.509192,8.308591,4.806858,2.261270,7.904443,-4.236936,3.812379],[-0.845005,4.269003,-2.563525,4.903783,-6.860793,7.700459,5.328167,-2.372257,5.822903,-6.794178,8.462952,-5.081340,-0.668203,2.229903]],[[5.581605,-0.310208,-5.939752,2.741263,6.096279,-9.837689,-8.098322,-1.866810,2.188277,-8.546508,-3.771448,-4.988120,2.038171,-4.317729],[-3.738200,-3.255000,-2.036068,0.496431,-6.992226,-3.343250,5.226279,2.487190,-6.969008,9.584478,-2.501169,6.526817,-2.221253,4.700198],[-5.438813,8.406503,7.658988,5.356181,2.744191,0.385984,1.885862,8.568027,-1.728046,-5.986800,-2.216400,-0.836929,0.529191,3.373423],[1.662777,7.435831,-5.767763,4.657916,-1.916797,-9.464346,9.586242,6.288011,0.095193,-4.221465,0.720155,-1.880462,-8.941061,8.144966],[-0.394358,-3.767461,1.741519,-2.542758,-4.212277,1.928429,-7.465934,-6.779227,7.325552,-8.451813,-8.590333,-7.632354,0.727476,7.519857],[-0.304879,3.464782,2.652681,-1.020623,-0.051890,3.894161,-5.979087,8.745564,-4.167740,1.902244,-1.114597,-2.884557,-1.100073,-7.771409],[9.513225,0.774926,-0.341446,8.770088,-5.868686,-5.567798,-8.043446,-8.699515,3.574850,8.150131,1.715882,7.582712,-3.514138,9.642901],[9.984329,-2.205662,8.981995,-9.153850,-2.061253,-8.867371,6.718293,4.659530,-9.254183,0.844965,-3.143052,0.663680,2.408614,7.840232],[-3.051002,-4.083056,-1.068673,-0.691982,-7.963154,-9.767580,-8.735085,-8.576187,5.745787,8.594310,2.685721,0.401190,4.336773,6.106217],[-0.178538,-4.734370,3.424523,-5.258073,5.737097,-0.617223,9.443888,0.660962,6.050019,6.767200,0.251585,-9.930919,2.537691,-5.357333],[-3.535832,6.003827,-2.177784,2.873992,-9.014115,-5.420940,-6.226830,-6.837564,0.540277,-1.096141,0.386833,4.744182,-9.451899,5.739388]],[[-1.157553,5.224048,2.803022,5.760871,-9.424038,-7.322879,-7.678438,5.020228,7.169661,-4.818402,3.924812,9.263410,-2.451784,4.079359],[-4.355651,5.606597,8.492992,7.178738,0.889083,-3.399286,1.655467,9.790583,3.829004,-0.727501,-2.363585,4.803179,4.553142,-9.819495],[-1.982557,0.382198,-5.518467,2.491497,9.615547,-3.241120,6.760540,-5.439250,9.326721,-7.954910,-4.997049,1.122502,7.326140,-0.379612],[5.660390,-9.995210,8.400195,-3.047303,-2.679080,1.997292,-8.520820,4.646662,-8.680869,-6.336085,9.712649,7.972265,-3.992317,-6.562359],[9.267913,-2.781157,3.988261,-0.680662,-8.693947,-7.612362,-7.483602,-2.532034,6.592054,-0.248989,-8.248604,-4.750584,5.194192,8.357743],[-2.130477,5.293998,5.814619,9.413323,5.332359,1.045051,-1.080088,-3.976542,7.682071,-1.523818,-0.430154,-0.443278,9.404973,-3.341062],[-6.815439,-5.444297,7.690797,8.087373,-6.477491,9.702195,-4.961264,9.211993,-9.771700,-9.253011,3.873597,3.545374,5.516382,-1.218980],[-4.799277,-9.623581,-5.287845,9.788982,-0.923612,-6.790734,5.348431,-9.196990,-1.969363,3.455968,-4.108985,-6.593462,-0.226095,8.372448],[-3.986427,-5.934382,6.288531,9.594478,-9.492315,9.842092,4.742436,3.901670,-4.099955,8.249630,1.240801,8.275852,-6.667120,4.956721],[4.111904,-4.609211,-5.803197,-2.529128,4.905774,-8.477492,6.007122,8.238064,6.908592,4.748648,-7.856340,8.293845,4.203145,8.823429],[-8.525760,-9.726556,-5.302193,9.412188,-5.915062,-4.677620,-5.400604,2.906979,-7.091538,-6.186954,3.818052,3.103574,-9.453310,8.698064]],[[-0.708765,6.072883,-2.296488,-8.191387,1.771951,3.268279,-3.756729,7.961547,-7.349411,-2.279629,8.402070,5.768038,-3.595255,6.184096],[1.589954,2.508894,4.096282,-6.103952,-0.916771,-3.478686,3.731768,7.595973,1.466986,-9.148047,0.149436,9.315977,2.078511,7.883807],[2.561965,6.890419,-7.435770,-5.053890,2.070298,9.741924,-6.672879,5.294959,3.351926,6.569751,-6.602437,2.534998,-9.877374,-9.266498],[4.165538,8.671058,-0.588537,8.320368,5.717552,6.263751,-9.950902,4.184398,-2.400030,-7.647914,4.729599,2.059175,6.239381,-8.937446],[6.622115,-8.821256,-3.374571,3.403267,-5.265486,5.699321,7.136855,-3.128119,8.636700,-1.759251,4.231023,-3.622134,-9.093961,-0.484838],[-1.713756,4.734186,2.166605,-4.498608,8.509701,2.691187,-3.646833,-1.674551,9.186251,5.201919,-5.790579,-9.438387,9.329354,-2.851111],[-9.541774,9.948726,2.323703,-7.752298,-8.143077,4.136228,9.499557,9.049380,6.493969,6.827155,0.644657,-0.178460,-8.915812,7.099729],[0.677650,3.246070,-8.093558,-9.427220,2.554533,-7.518309,9.081458,9.485697,-4.678271,-8.431572,-4.331201,-2.953768,-6.596170,4.383187],[-9.793412,-8.519905,1.240495,7.451417,0.230082,4.592154,1.065697,-8.063453,0.410485,7.886395,4.253330,-5.554844,8.897371,3.504232],[2.182324,-0.899094,7.509084,1.896721,-4.842162,-8.219927,-6.188335,-6.391119,6.175682,-2.832097,-3.818279,1.204208,6.886413,-1.488739],[-6.754772,-7.400266,-1.455277,6.865476,-5.727612,-6.633730,-2.719929,-6.682404,5.390019,-3.425391,0.399324,2.659024,-3.846293,3.853346]],[[-1.827469,-7.504532,2.230199,-3.583197,2.201253,9.419290,-7.978683,-0.570294,-3.108758,8.669237,2.989875,6.812735,-9.962962,-6.387487],[9.463454,-9.445573,6.388192,-0.370096,-6.113756,2.397044,2.379596,0.131322,-0.100130,-8.197815,-7.875865,-9.590176,7.625988,-2.365889],[6.936404,-4.827976,5.015307,-0.035198,3.599341,1.715183,-9.574615,7.138182,-5.747775,2.096705,-2.925579,6.462674,-1.177014,-4.423522],[1.002576,0.875006,8.551958,3.082172,8.361773,-3.048615,7.536153,-2.699766,-3.888817,7.120264,-0.122409,6.398551,-3.491486,1.134760],[5.774882,-5.602044,-5.754407,4.708435,5.847670,-1.797143,-0.960629,6.311803,5.554957,0.761400,1.701205,-3.510373,-7.511063,-9.981196],[-2.855476,3.359716,3.649712,1.447614,2.529401,4.813996,9.295627,4.082094,-9.093932,8.027953,-5.391245,7.009428,4.589199,5.697677],[-8.534666,-0.680215,1.365106,-3.382641,6.544789,5.494629,-1.961010,7.359328,-0.491858,2.435504,6.758338,-9.045595,-3.395301,6.097757],[9.273986,4.602044,-5.145372,6.887909,6.184658,-7.715314,9.542537,1.263729,5.561513,5.768703,-2.165200,-5.501663,-1.793067,0.088269],[5.299383,-1.847927,-0.505690,-6.041769,-9.513839,-9.083064,2.775823,-7.077372,-7.474961,-5.595075,9.563118,-1.606776,-9.835933,3.487899],[6.581374,9.653399,-3.132820,-4.721665,0.914128,7.928186,-1.413235,3.920600,1.465744,-1.158698,-6.501302,9.161105,-1.141147,3.641600],[-4.443000,3.209869,0.280921,-5.836354,3.804954,-4.744541,9.998277,-4.290574,-9.968962,7.023320,8.020769,8.162108,-9.423383,2.806752]]], dtype = "float32")#candidate|3519|(11, 11, 14)|const|float32
bop_3520 = relay.bitwise_and(call_3515.astype('int32'), const_3519.astype('int32')) # shape=(11, 11, 14)
bop_3523 = relay.bitwise_and(call_3516.astype('int32'), const_3519.astype('int32')) # shape=(11, 11, 14)
func_1294_call = mod.get_global_var('func_1294')
func_1297_call = mutated_mod.get_global_var('func_1297')
const_3526 = relay.const([-9.545332,-6.105638,8.430345,2.164364,-7.448461,3.475665,-0.710981,4.429806,-2.388200,-8.162920,-8.118022,0.849536,1.110645,1.154312,1.998134,5.306444,-1.655276,4.763453,-9.170363,8.985359,-3.424517,5.888119,8.567366,8.850298,5.926869,-7.710920,4.239425,8.684101,-3.722786,-2.806785,-4.682126,9.259320,2.263008,-6.569768,-2.075136,1.556417,-2.440366,8.575298,1.949176,-9.612702,-2.266043,-4.808112,-1.975130,-3.850138,0.128225,-2.387569,-9.371386,-3.180422,-7.431407,2.413415], dtype = "float32")#candidate|3526|(50,)|const|float32
call_3525 = relay.TupleGetItem(func_1294_call(relay.reshape(const_3526.astype('float32'), [10, 1, 5])), 0)
call_3527 = relay.TupleGetItem(func_1297_call(relay.reshape(const_3526.astype('float32'), [10, 1, 5])), 0)
output = relay.Tuple([bop_3520,call_3525,const_3526,])
output2 = relay.Tuple([bop_3523,call_3527,const_3526,])
func_3528 = relay.Function([], output)
mod['func_3528'] = func_3528
mod = relay.transform.InferType()(mod)
mutated_mod['func_3528'] = func_3528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3528_call = mutated_mod.get_global_var('func_3528')
call_3529 = func_3528_call()
output = call_3529
func_3530 = relay.Function([], output)
mutated_mod['func_3530'] = func_3530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2736_call = mod.get_global_var('func_2736')
func_2737_call = mutated_mod.get_global_var('func_2737')
call_3560 = relay.TupleGetItem(func_2736_call(), 0)
call_3561 = relay.TupleGetItem(func_2737_call(), 0)
func_573_call = mod.get_global_var('func_573')
func_574_call = mutated_mod.get_global_var('func_574')
call_3564 = func_573_call()
call_3565 = func_573_call()
output = relay.Tuple([call_3560,call_3564,])
output2 = relay.Tuple([call_3561,call_3565,])
func_3576 = relay.Function([], output)
mod['func_3576'] = func_3576
mod = relay.transform.InferType()(mod)
output = func_3576()
func_3577 = relay.Function([], output)
mutated_mod['func_3577'] = func_3577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1560_call = mod.get_global_var('func_1560')
func_1561_call = mutated_mod.get_global_var('func_1561')
call_3603 = func_1560_call()
call_3604 = func_1560_call()
uop_3612 = relay.exp(call_3603.astype('float64')) # shape=(11, 1, 14)
uop_3614 = relay.exp(call_3604.astype('float64')) # shape=(11, 1, 14)
bop_3625 = relay.multiply(uop_3612.astype('int32'), relay.reshape(call_3603.astype('int32'), relay.shape_of(uop_3612))) # shape=(11, 1, 14)
bop_3628 = relay.multiply(uop_3614.astype('int32'), relay.reshape(call_3604.astype('int32'), relay.shape_of(uop_3614))) # shape=(11, 1, 14)
func_848_call = mod.get_global_var('func_848')
func_850_call = mutated_mod.get_global_var('func_850')
call_3635 = relay.TupleGetItem(func_848_call(), 0)
call_3636 = relay.TupleGetItem(func_850_call(), 0)
const_3638 = relay.const([[[-0.334403,-6.173567,4.145962,9.645694,-3.417256,-4.604739,-7.349770,-9.077771,4.021189,5.999004,-1.181285,3.916320,-5.474851,9.708591],[-7.892892,0.575559,-0.208234,-1.230626,2.354843,-1.822983,-2.545256,-3.621542,9.245782,-4.650942,7.448978,8.619250,-1.652600,9.186422],[7.225668,-3.111244,6.876823,-9.522975,1.571715,0.870052,-0.306799,-7.308691,-9.697074,-6.085617,1.814625,7.157344,-1.502702,5.317119],[1.959102,6.099517,3.501183,7.688621,-6.146158,-6.418750,-8.448701,-9.237773,7.744932,6.334528,3.034860,4.198727,-9.315600,9.443757],[-5.967376,-2.141967,1.972073,-6.234845,0.846764,1.024512,5.496491,6.769262,-4.290288,9.944518,-9.823985,4.358917,-7.286112,4.454269],[7.164215,8.022220,5.917821,-0.372233,0.256673,7.378560,-4.572739,-1.968955,-0.005772,7.352412,-0.021851,-5.635610,-4.586087,-5.252931]],[[-1.730369,0.456836,2.189743,5.265839,-3.463435,5.539456,-9.885613,-4.191298,-4.191076,1.565761,-2.079720,4.559414,0.344983,-4.550747],[3.216025,-9.452414,-4.778208,-9.211689,-3.791243,-3.915630,2.427953,-7.136273,-7.797856,-2.193941,-9.229494,6.939700,-5.730086,3.949507],[-4.891390,9.775356,-9.137606,5.254013,-1.625200,-0.451557,-2.683981,0.316993,5.162561,1.078959,5.788448,-5.493445,5.599482,-0.506059],[-5.939096,4.925612,0.066251,-3.043622,-0.090676,-7.582024,9.652006,0.734633,5.263851,7.926225,5.451361,-7.076680,-0.316774,-8.323932],[-1.963408,-4.501121,-4.273039,3.949936,-3.658089,3.750104,-3.687765,2.821316,5.230161,9.421086,-0.310432,2.819464,1.700561,-0.004774],[-1.756628,-7.980948,1.858241,8.307531,-6.415741,-1.424370,-7.209002,-6.080000,5.640298,3.784191,-2.202615,-1.484655,4.633718,-1.961015]],[[5.247745,0.921890,0.544618,1.309431,-8.385088,-0.652722,4.270987,9.770477,8.317544,-5.589793,-3.539991,1.515025,-9.271921,5.972539],[5.089408,2.832690,-0.194187,-2.712976,-0.603696,-8.089136,-7.132668,0.925129,9.585211,4.913352,-7.577351,-7.042269,7.402628,-4.214803],[1.141738,-8.572148,6.600231,1.797770,-8.483739,-4.842708,0.368461,7.848438,9.346910,-2.320191,1.990238,0.787718,5.553895,-7.747220],[6.783432,8.552054,-5.795526,4.123143,3.830528,8.400992,-2.122365,-0.301788,5.701114,0.042127,-7.759577,4.556554,-1.754160,-7.694415],[-8.755381,-0.828933,2.608278,-5.507355,1.635036,7.457918,6.663477,-2.988415,-7.103890,5.870789,-9.847991,4.275002,-5.217611,7.229117],[7.169116,9.609714,-6.407695,-9.902210,9.857909,-3.186181,-1.953065,8.437853,-8.833895,-0.144253,-2.685264,-8.513507,-6.985860,2.966661]],[[5.014202,9.963975,-7.990329,-6.152120,9.232598,-9.607592,-8.976909,1.309797,2.184053,-4.946009,9.120385,-7.853236,-1.535833,-5.891216],[-6.105716,-2.344559,-7.995249,3.021153,-1.911588,-7.228512,-5.819791,-7.482184,6.085343,6.626416,-2.697759,-8.716086,-2.574737,7.789842],[-9.304100,-5.090699,5.679949,-4.525581,-8.034437,0.673493,3.301657,-4.052908,-2.048450,-8.449999,0.773280,-8.908209,6.984807,3.448975],[-3.586423,8.843516,-3.843779,1.023833,-6.271626,-1.763387,2.810499,4.130745,2.658006,-7.505578,-3.101247,2.967803,6.083666,8.484805],[-5.194091,-6.313874,9.846230,4.606971,4.335876,2.206396,-1.837110,7.842125,8.855694,1.393762,-9.231246,3.399386,-5.983134,-2.603261],[-8.481148,2.295095,-6.269403,3.722638,8.380803,-0.206947,-3.037322,-3.839711,4.390514,-6.148640,-9.557099,7.988219,-2.913392,5.207991]],[[8.222993,-2.542475,5.812980,-1.595895,7.700415,8.369900,3.932382,-9.084562,1.340444,-1.770239,-7.188835,-4.215220,-4.443487,8.487105],[-0.439763,-3.597133,3.153489,0.241691,-6.699075,-0.698687,-3.750383,-1.843951,9.360237,6.428083,1.559378,6.590030,-2.150765,-4.808994],[3.859955,6.190099,-3.788196,9.941170,-8.783006,-8.946758,0.141189,7.289830,-6.918778,3.529622,-3.821231,-4.008239,-2.577899,8.145382],[5.609166,-9.663072,2.477223,-4.024274,4.793655,3.427317,4.213904,-1.676231,5.015993,-2.479979,4.442562,4.936867,-1.172355,1.962670],[-3.101654,4.958418,-1.685530,-8.881235,-3.577427,1.588603,1.298901,7.074032,-0.819663,9.670446,8.891745,3.892803,8.791964,-6.381142],[-6.917455,-3.716485,-6.822298,7.773006,5.075139,2.766738,-3.240054,8.433242,9.033663,-3.185093,-0.039118,4.662003,6.247642,-8.413871]],[[-8.127370,-5.002026,-1.040172,0.646218,3.645646,1.409090,-2.694778,-6.208853,7.177632,-6.200993,-7.632954,-3.394707,-5.467981,5.234913],[-3.906302,-7.897346,-4.338160,-6.217101,-8.744070,-3.689630,-4.825166,-1.137351,-4.170722,5.665354,0.968969,-6.622687,2.544782,-8.526425],[1.139831,0.426321,-0.617606,-3.789443,0.306443,6.864675,-5.898637,2.644202,-0.957488,3.081225,-7.379280,-5.810001,2.575036,7.587758],[-9.870643,-0.020006,3.986069,2.473306,-1.191501,0.137175,-5.038111,4.507357,-3.566185,1.634766,-2.834579,8.283192,-2.682267,-7.781820],[-0.756318,-0.220748,-1.052509,-7.617235,-0.608152,0.990673,6.431057,-2.571299,6.171171,-6.850974,-5.111397,-6.122651,0.340139,1.482682],[-7.895691,1.874135,-5.885932,6.076757,-8.604618,-2.144011,2.650865,0.024677,-6.537411,0.813319,8.767870,4.709253,1.580117,7.954642]],[[4.891513,-1.396156,-8.977593,9.782304,6.350091,5.784265,-6.172082,3.211638,6.152887,9.590009,-7.712665,-8.254976,-0.062641,-7.468476],[6.463875,-2.518160,-6.674172,-7.623794,-4.392850,6.894712,-8.663991,-4.034659,1.453394,3.563554,-0.386277,-6.195616,5.481659,0.606692],[7.375604,2.599010,8.697173,4.672773,7.813704,-9.773338,5.378121,8.673762,7.852967,2.320140,3.744340,1.607220,8.726838,9.411642],[-9.071054,-6.087995,-8.481877,6.537967,-5.967476,2.181921,-3.294090,8.234732,-1.064476,-4.929668,-0.168891,-3.325886,-1.171092,-8.390744],[1.316542,-3.964919,-3.543933,7.106012,-3.459734,-1.022818,-9.248229,-2.455010,2.861018,-4.720582,2.998213,1.992535,-9.766116,0.469027],[-1.529219,-9.405389,4.901480,3.278678,-1.016138,-1.724124,7.735224,3.580508,6.635280,6.046535,7.837592,-3.212219,-1.733400,0.720395]],[[9.903728,3.157744,-6.772725,6.451513,-6.160221,9.494000,-9.696405,0.388607,-4.420311,0.608725,9.450311,-9.617440,-8.412171,3.540125],[7.743049,-8.914327,0.759207,-4.439453,2.943904,-0.459340,-4.622940,-7.983701,3.569543,8.115776,-4.442860,4.948359,2.688735,7.586411],[-6.869766,-0.378180,8.118525,-8.690756,-9.781358,-6.322280,6.780131,8.716178,-8.947671,-5.460932,7.765839,1.318596,-2.406008,4.036683],[-4.344810,6.483510,7.938203,-2.477468,-8.511659,-8.609275,8.850636,0.807607,1.011924,1.946792,-6.199122,8.615923,4.429035,-6.271164],[-9.956040,6.231843,-0.382779,2.186100,-7.828635,-2.631548,6.582217,1.902414,0.510907,7.132616,8.607049,-8.974410,-5.731988,9.124157],[-5.820062,8.245435,-4.936854,3.098107,3.596678,-3.177333,0.876714,5.090056,9.941648,2.885620,2.099724,1.765341,2.203082,-9.798039]],[[-4.091118,3.339843,3.735436,3.419293,6.606554,-4.757492,9.380549,-2.959736,1.471447,0.203068,-7.110970,5.669215,6.819313,-2.238355],[-6.132553,-2.032879,7.010798,3.483373,-8.876889,-9.551947,-4.162150,2.044799,9.047335,-3.814937,5.984685,-1.088452,-3.682655,3.228893],[-8.366228,2.511943,-5.387536,6.751499,5.580009,5.402231,5.112625,-0.155602,-2.332662,-6.250684,8.518260,4.357521,-7.013060,2.622131],[8.992925,1.083509,-2.139729,0.731265,-7.619608,-9.485773,6.155517,-5.197008,7.172442,-4.307531,-2.907552,-0.583770,9.793380,-7.242957],[8.150678,8.380861,-9.297754,-1.259891,6.800601,6.885491,0.521884,1.080247,6.562518,0.542413,-8.512626,2.751242,-5.133012,9.787779],[4.751461,-3.593249,0.103956,0.788562,-3.516667,-7.126953,4.461257,3.571854,-3.489487,-1.015884,-7.335472,-9.665952,9.048533,1.307274]],[[5.497550,-9.324020,-4.058662,5.675831,-1.973262,2.940664,4.495684,-9.418270,-5.891555,3.281995,-2.278660,-0.052987,4.698882,-8.344415],[-2.698908,8.226669,-8.473000,-6.431495,-4.714961,-6.252302,4.316368,4.605062,8.969628,6.111064,4.747913,-6.987909,-6.069530,4.264856],[-4.434932,4.115386,5.502248,-8.860591,-1.990105,1.854830,3.025744,4.828733,7.582609,1.869272,-5.233912,-2.568383,3.157915,5.450540],[-6.641313,2.287067,-8.658855,0.867572,8.230539,4.345872,4.575483,-9.809962,-9.162573,3.009693,-6.775729,8.079779,2.551439,0.359209],[-1.556360,2.218368,6.472799,0.750374,8.822218,1.239564,8.207678,-4.252677,3.999704,9.586406,-7.769733,-2.229707,3.667032,5.640696],[6.524717,0.503093,1.525718,-5.133964,7.100409,7.050296,0.698388,-3.924062,1.453345,4.086578,4.870854,2.611355,9.054305,2.700279]],[[1.883292,3.047143,6.867535,-0.494311,3.282308,3.536290,6.116602,1.961128,6.754066,4.431726,-9.398228,-2.455552,0.566726,7.740223],[9.793662,8.643700,9.565617,3.923776,1.847548,-6.795512,1.189290,8.294987,-5.579659,8.306639,-8.961960,-8.299079,4.171324,9.511290],[-0.822069,3.823094,3.232359,-9.583487,3.011569,2.428010,-7.561511,-4.525066,8.345377,-9.558961,-7.132611,2.131185,-8.924437,-1.661696],[-9.010397,-6.894422,-1.550470,-3.317521,-0.041692,5.158633,5.715806,-1.314065,-8.404606,3.999437,-6.759157,7.192057,3.980119,-4.633532],[-9.133697,6.682189,-4.119149,-7.646834,0.770589,-2.547092,9.683975,2.942529,-4.983009,-1.339603,-5.914728,-0.979830,9.911774,-9.436242],[-7.758055,-8.216118,2.857368,-6.627775,4.826083,-2.098499,5.435871,-9.349356,-1.957988,6.242300,7.915039,0.077065,4.819699,5.332370]]], dtype = "float64")#candidate|3638|(11, 6, 14)|const|float64
bop_3639 = relay.bitwise_or(uop_3612.astype('int8'), const_3638.astype('int8')) # shape=(11, 6, 14)
bop_3642 = relay.bitwise_or(uop_3614.astype('int8'), const_3638.astype('int8')) # shape=(11, 6, 14)
func_160_call = mod.get_global_var('func_160')
func_161_call = mutated_mod.get_global_var('func_161')
call_3646 = relay.TupleGetItem(func_160_call(), 0)
call_3647 = relay.TupleGetItem(func_161_call(), 0)
output = relay.Tuple([bop_3625,call_3635,bop_3639,call_3646,])
output2 = relay.Tuple([bop_3628,call_3636,bop_3642,call_3647,])
func_3651 = relay.Function([], output)
mod['func_3651'] = func_3651
mod = relay.transform.InferType()(mod)
output = func_3651()
func_3652 = relay.Function([], output)
mutated_mod['func_3652'] = func_3652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_3666 = relay.TupleGetItem(func_2220_call(), 0)
call_3667 = relay.TupleGetItem(func_2222_call(), 0)
output = relay.Tuple([call_3666,])
output2 = relay.Tuple([call_3667,])
func_3685 = relay.Function([], output)
mod['func_3685'] = func_3685
mod = relay.transform.InferType()(mod)
mutated_mod['func_3685'] = func_3685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3685_call = mutated_mod.get_global_var('func_3685')
call_3686 = func_3685_call()
output = call_3686
func_3687 = relay.Function([], output)
mutated_mod['func_3687'] = func_3687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_523_call = mod.get_global_var('func_523')
func_524_call = mutated_mod.get_global_var('func_524')
call_3738 = relay.TupleGetItem(func_523_call(), 0)
call_3739 = relay.TupleGetItem(func_524_call(), 0)
output = call_3738
output2 = call_3739
func_3743 = relay.Function([], output)
mod['func_3743'] = func_3743
mod = relay.transform.InferType()(mod)
mutated_mod['func_3743'] = func_3743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3743_call = mutated_mod.get_global_var('func_3743')
call_3744 = func_3743_call()
output = call_3744
func_3745 = relay.Function([], output)
mutated_mod['func_3745'] = func_3745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_389_call = mod.get_global_var('func_389')
func_390_call = mutated_mod.get_global_var('func_390')
call_3758 = relay.TupleGetItem(func_389_call(), 1)
call_3759 = relay.TupleGetItem(func_390_call(), 1)
func_3383_call = mod.get_global_var('func_3383')
func_3384_call = mutated_mod.get_global_var('func_3384')
call_3768 = relay.TupleGetItem(func_3383_call(), 1)
call_3769 = relay.TupleGetItem(func_3384_call(), 1)
output = relay.Tuple([call_3758,call_3768,])
output2 = relay.Tuple([call_3759,call_3769,])
func_3770 = relay.Function([], output)
mod['func_3770'] = func_3770
mod = relay.transform.InferType()(mod)
output = func_3770()
func_3771 = relay.Function([], output)
mutated_mod['func_3771'] = func_3771
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3790 = relay.const([[[5,6,-7,1,5,6,5,2,10,4,-2,-1,-1],[-9,9,10,4,-5,6,-8,-2,-9,-4,10,6,-9],[-8,-7,-3,1,8,8,-9,2,-1,-6,-5,-1,-6],[5,2,2,8,3,10,5,-7,-10,8,-2,2,-1],[1,-6,-10,10,-6,-5,4,8,-4,-1,-6,7,-3],[-2,-7,4,4,4,2,5,6,4,10,5,-5,-2],[7,4,8,-9,-10,2,4,5,10,5,1,-10,-1],[2,-3,-8,4,2,-9,-7,-3,-2,-5,-2,8,4],[9,10,-9,8,7,-2,-10,-4,-5,-10,2,-5,9],[-3,-7,6,-1,5,-9,1,9,-10,10,-9,-7,-7],[-1,7,10,-8,-6,-2,-3,6,2,-1,-5,-1,6]],[[-3,-1,3,1,-3,-7,9,-9,10,-9,-5,6,-1],[6,-7,4,-5,-8,-4,-8,3,9,-9,-4,10,5],[-4,3,1,9,-4,-6,5,-9,5,7,-3,10,7],[-10,7,4,6,9,9,-5,-1,3,-7,5,10,-7],[-10,-2,3,6,7,3,9,1,10,-2,7,6,-8],[3,5,-8,9,4,3,-1,-1,-4,-8,10,-8,-10],[-8,8,-9,5,-5,1,-4,-5,4,-9,-2,-5,7],[10,-8,2,-9,5,3,2,-2,1,7,-6,4,5],[-10,10,-8,5,-3,5,7,-9,-9,-10,3,8,7],[-10,9,1,-10,7,1,5,8,5,-9,8,5,-8],[9,-8,-9,-1,4,10,-3,1,8,6,-5,1,-5]],[[-1,-1,1,-4,-8,5,-1,-3,4,-7,-8,2,-1],[4,10,-5,4,-9,-5,1,-6,-5,9,10,-2,8],[-2,-3,-7,6,-10,10,4,6,4,5,6,-9,-7],[-8,-5,-10,-9,1,2,5,6,-8,9,-4,-3,-5],[8,-4,2,-6,10,-6,-9,-7,2,-6,1,3,-8],[-3,5,-10,1,-9,-7,3,-3,8,-6,4,9,8],[-4,10,-9,2,2,-6,5,-9,2,-10,9,-8,5],[4,-4,3,-5,-9,-9,-8,-1,5,4,8,6,-3],[-8,-1,-3,-6,-7,-4,-6,-9,-3,6,-3,-2,7],[-3,10,7,4,-2,2,3,-8,4,-1,-9,-9,-10],[7,9,6,6,-9,5,-10,-2,2,2,4,4,-8]],[[-2,9,1,-6,10,4,7,9,-9,-6,3,-6,-9],[-2,6,7,9,9,-2,2,-6,-7,2,-4,7,1],[1,-5,-6,3,-9,7,6,9,3,-9,-2,4,6],[-6,-10,-5,2,1,-8,-9,7,-6,4,-1,1,-7],[-8,-8,1,-9,10,-3,-3,10,1,8,-9,-2,-2],[-1,-3,-5,-9,7,-4,10,8,6,-8,-3,-10,-8],[7,-4,-1,1,3,-8,6,4,-2,6,8,3,2],[6,1,1,-1,7,1,-9,4,9,-5,-10,7,-8],[9,2,9,3,1,-8,-10,6,2,6,-3,6,7],[-4,3,1,5,-3,-3,-4,2,-9,-6,-2,10,-4],[2,-10,5,5,-8,-10,-4,-7,9,5,1,4,7]],[[-6,5,-2,8,-7,-8,9,-3,-8,1,-7,-5,4],[4,-3,-3,10,9,-6,-3,-9,7,8,-8,8,2],[-2,6,4,3,3,-8,-5,-4,-5,-5,-2,6,-4],[-6,6,8,6,-5,5,8,7,10,5,4,-5,-6],[-1,6,-7,-8,2,-10,-9,7,-4,-2,2,-2,10],[-5,-2,3,-1,9,-3,10,2,-4,-4,6,7,-8],[2,6,-3,8,-1,-1,9,-2,-6,10,4,-8,8],[-8,-2,5,-4,7,-1,-3,7,7,-5,-10,3,8],[5,-6,9,-7,-10,-6,-3,-10,-9,7,8,-4,4],[3,-6,-5,-6,-4,-6,-4,3,-1,-5,1,5,-2],[1,-7,9,-2,-10,6,1,8,2,4,-4,-2,-5]],[[4,10,-4,-3,-5,10,7,-4,3,-4,-3,-5,-2],[3,9,-8,9,-1,8,-3,-6,10,-2,-8,-2,-7],[9,-5,2,-6,5,6,-1,-6,-10,-1,1,-2,8],[7,4,-6,-6,3,-8,-1,-2,-6,3,-1,-10,-1],[-4,3,5,-1,-3,-2,-7,-9,6,7,-8,-1,6],[5,-4,6,-9,9,8,-3,-8,-2,-1,-1,2,5],[10,2,-5,1,-5,-7,-5,-8,-10,-6,5,-5,-10],[3,4,-3,-1,-2,3,-6,-2,3,-1,2,4,-10],[-5,-7,-1,8,-8,4,5,-8,9,9,6,1,-6],[9,-3,1,3,-5,-8,-4,4,-6,1,-1,7,-6],[-3,2,-1,9,9,-4,-8,1,-1,-10,10,-6,-9]]], dtype = "uint8")#candidate|3790|(6, 11, 13)|const|uint8
const_3791 = relay.const([[[5,10,9,2,-8,-8,-2,3,-5,-9,-3,-3,-3],[3,10,1,5,7,-7,-4,1,6,-10,1,-2,-8],[-3,-3,-1,4,-6,-9,6,4,2,8,9,7,5],[-7,-10,3,5,-10,2,10,-8,-8,-2,8,2,5],[4,-3,2,7,4,-5,-5,7,-10,-5,3,-3,-8],[7,10,3,6,2,-5,-9,-8,8,-9,9,2,-8],[-7,-8,-3,-7,6,7,-8,-9,-8,2,3,7,6],[1,-10,-3,-7,4,-5,-3,2,5,8,3,-4,-2],[-8,9,7,-4,-7,5,-5,6,-1,2,-10,3,1],[-6,2,2,-6,-6,10,-9,-4,-3,-5,-10,1,-10],[-9,8,1,-6,3,5,-10,-2,10,9,10,-6,2]],[[-1,-9,3,6,-9,7,-1,7,10,6,8,-7,-1],[-1,-10,-2,6,-4,9,-4,8,-6,-2,5,-10,7],[-9,7,9,-7,-10,4,2,7,-9,-10,2,7,10],[-9,-5,10,-1,5,4,-3,-3,-2,-4,-4,2,9],[3,2,-8,-6,7,6,-3,-10,-3,5,7,-10,-8],[1,2,6,5,-9,-6,3,-10,-1,-2,-2,-3,2],[4,-10,-8,-2,2,6,-3,10,9,-5,6,2,9],[4,2,-4,10,9,-7,-10,9,8,-8,-3,4,6],[6,-8,3,-8,10,9,8,-9,1,7,5,3,-4],[2,6,7,-5,10,-7,-1,2,8,-10,-6,8,2],[-9,-9,-1,2,-7,3,6,-10,-2,1,-4,4,7]],[[4,3,1,1,6,10,-3,-9,-1,-8,9,5,-3],[-8,-3,-1,2,-5,8,2,-9,-6,-9,7,-1,4],[-6,-7,-6,-8,-9,5,2,4,-5,-6,1,7,8],[-2,8,6,-5,-2,7,9,10,-9,6,-4,4,-7],[3,-4,7,-7,-4,-10,-7,9,4,-2,-3,-7,-8],[10,-3,6,-3,5,10,7,-9,4,-1,2,10,10],[-6,-2,9,8,-1,6,-7,-3,6,-1,-9,1,-8],[5,-6,1,3,-8,-5,2,1,9,-10,-4,-4,-1],[10,3,4,7,-3,4,10,-8,-10,-1,10,-10,-2],[-7,9,-7,2,10,8,-8,4,6,-7,10,-7,-10],[-1,-7,5,9,-4,5,-8,3,-2,8,-6,1,1]],[[1,-4,-4,3,10,-5,-2,-9,8,3,5,4,-1],[-10,-4,-6,8,7,-5,-3,-8,5,-1,8,2,-3],[-7,2,7,-2,4,7,-6,-6,-5,-7,9,-1,-6],[2,-10,-9,-1,-7,-3,-9,-5,-9,-9,3,3,-6],[-1,5,-6,9,1,5,9,8,8,-8,-4,-5,1],[-8,9,-9,1,-2,-10,-4,-7,2,-10,-7,-10,5],[-4,-8,10,9,9,2,1,-8,-4,-3,1,8,-8],[4,-10,3,-9,8,6,-3,-7,-7,-10,3,-7,-5],[-4,4,8,9,6,3,-2,9,10,4,-6,8,-8],[-7,7,-7,-7,-2,-8,-4,-2,2,-9,1,10,9],[-8,9,9,-3,10,-7,1,-1,-10,-5,-1,6,5]],[[-9,5,-10,-6,1,9,-2,-3,5,8,-5,2,-1],[-7,4,6,-9,-3,4,-10,-3,-8,-7,3,5,1],[-10,-9,7,-1,8,-6,8,5,-9,6,5,8,-5],[7,2,9,10,-6,4,10,5,-8,-5,5,-10,-9],[-3,9,8,7,4,6,7,-3,-1,4,10,9,7],[-1,-2,-5,7,-4,-10,7,-10,9,4,8,-6,-1],[6,-4,-1,3,-7,-10,-2,9,7,9,-10,-3,-2],[-2,-5,7,-3,8,7,-9,10,9,6,-8,-6,8],[-5,2,6,-8,-9,4,-5,7,-6,6,-6,1,-3],[-2,-6,-6,-5,-10,4,-2,4,-2,2,3,-6,3],[-2,-3,-3,-5,-9,-10,9,5,-8,6,-7,-1,10]],[[7,2,7,4,10,-8,8,6,-2,-8,10,-6,-9],[5,-1,3,10,-10,1,8,3,6,3,-9,-9,-4],[4,7,4,-3,-6,5,-4,-4,8,6,-10,-1,6],[-10,7,-6,-5,-4,5,-3,6,1,-2,-6,-9,-2],[-5,-3,-4,-8,8,-4,6,-1,-5,-6,-4,-2,-9],[5,-1,6,1,-8,2,-6,9,3,-7,-8,9,-3],[10,9,4,-9,2,-10,5,-8,2,-9,-5,8,-7],[4,2,-10,3,-2,-5,1,-6,-10,8,10,-3,3],[-1,10,9,7,3,4,7,4,-8,-9,7,7,-9],[-7,8,-2,3,9,8,-5,-3,7,-6,-4,-8,-9],[4,10,5,-8,9,3,4,6,-10,-2,-2,5,-2]]], dtype = "uint8")#candidate|3791|(6, 11, 13)|const|uint8
bop_3792 = relay.less_equal(const_3790.astype('bool'), relay.reshape(const_3791.astype('bool'), relay.shape_of(const_3790))) # shape=(6, 11, 13)
bop_3817 = relay.greater_equal(bop_3792.astype('bool'), relay.reshape(const_3791.astype('bool'), relay.shape_of(bop_3792))) # shape=(6, 11, 13)
bop_3826 = relay.bitwise_xor(const_3790.astype('int16'), relay.reshape(bop_3792.astype('int16'), relay.shape_of(const_3790))) # shape=(6, 11, 13)
output = relay.Tuple([bop_3817,bop_3826,])
output2 = relay.Tuple([bop_3817,bop_3826,])
func_3830 = relay.Function([], output)
mod['func_3830'] = func_3830
mod = relay.transform.InferType()(mod)
mutated_mod['func_3830'] = func_3830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3830_call = mutated_mod.get_global_var('func_3830')
call_3831 = func_3830_call()
output = call_3831
func_3832 = relay.Function([], output)
mutated_mod['func_3832'] = func_3832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1686_call = mod.get_global_var('func_1686')
func_1687_call = mutated_mod.get_global_var('func_1687')
call_3870 = func_1686_call()
call_3871 = func_1686_call()
func_614_call = mod.get_global_var('func_614')
func_615_call = mutated_mod.get_global_var('func_615')
call_3907 = relay.TupleGetItem(func_614_call(), 0)
call_3908 = relay.TupleGetItem(func_615_call(), 0)
output = relay.Tuple([call_3870,call_3907,])
output2 = relay.Tuple([call_3871,call_3908,])
func_3910 = relay.Function([], output)
mod['func_3910'] = func_3910
mod = relay.transform.InferType()(mod)
mutated_mod['func_3910'] = func_3910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3910_call = mutated_mod.get_global_var('func_3910')
call_3911 = func_3910_call()
output = call_3911
func_3912 = relay.Function([], output)
mutated_mod['func_3912'] = func_3912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1686_call = mod.get_global_var('func_1686')
func_1687_call = mutated_mod.get_global_var('func_1687')
call_4004 = func_1686_call()
call_4005 = func_1686_call()
output = call_4004
output2 = call_4005
func_4016 = relay.Function([], output)
mod['func_4016'] = func_4016
mod = relay.transform.InferType()(mod)
output = func_4016()
func_4017 = relay.Function([], output)
mutated_mod['func_4017'] = func_4017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2693_call = mod.get_global_var('func_2693')
func_2695_call = mutated_mod.get_global_var('func_2695')
call_4067 = relay.TupleGetItem(func_2693_call(), 0)
call_4068 = relay.TupleGetItem(func_2695_call(), 0)
func_1425_call = mod.get_global_var('func_1425')
func_1427_call = mutated_mod.get_global_var('func_1427')
call_4070 = relay.TupleGetItem(func_1425_call(), 2)
call_4071 = relay.TupleGetItem(func_1427_call(), 2)
output = relay.Tuple([call_4067,call_4070,])
output2 = relay.Tuple([call_4068,call_4071,])
func_4075 = relay.Function([], output)
mod['func_4075'] = func_4075
mod = relay.transform.InferType()(mod)
output = func_4075()
func_4076 = relay.Function([], output)
mutated_mod['func_4076'] = func_4076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_4119 = func_2601_call()
call_4120 = func_2601_call()
output = call_4119
output2 = call_4120
func_4124 = relay.Function([], output)
mod['func_4124'] = func_4124
mod = relay.transform.InferType()(mod)
mutated_mod['func_4124'] = func_4124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4124_call = mutated_mod.get_global_var('func_4124')
call_4125 = func_4124_call()
output = call_4125
func_4126 = relay.Function([], output)
mutated_mod['func_4126'] = func_4126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2966_call = mod.get_global_var('func_2966')
func_2967_call = mutated_mod.get_global_var('func_2967')
call_4156 = func_2966_call()
call_4157 = func_2966_call()
output = relay.Tuple([call_4156,])
output2 = relay.Tuple([call_4157,])
func_4165 = relay.Function([], output)
mod['func_4165'] = func_4165
mod = relay.transform.InferType()(mod)
output = func_4165()
func_4166 = relay.Function([], output)
mutated_mod['func_4166'] = func_4166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_4188 = func_2601_call()
call_4189 = func_2601_call()
var_4193 = relay.var("var_4193", dtype = "int8", shape = (11, 9, 14))#candidate|4193|(11, 9, 14)|var|int8
bop_4194 = relay.less(call_4188.astype('bool'), relay.reshape(var_4193.astype('bool'), relay.shape_of(call_4188))) # shape=(11, 9, 14)
bop_4197 = relay.less(call_4189.astype('bool'), relay.reshape(var_4193.astype('bool'), relay.shape_of(call_4189))) # shape=(11, 9, 14)
uop_4203 = relay.log(bop_4194.astype('float64')) # shape=(11, 9, 14)
uop_4205 = relay.log(bop_4197.astype('float64')) # shape=(11, 9, 14)
output = uop_4203
output2 = uop_4205
func_4211 = relay.Function([var_4193,], output)
mod['func_4211'] = func_4211
mod = relay.transform.InferType()(mod)
mutated_mod['func_4211'] = func_4211
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4212 = relay.var("var_4212", dtype = "int8", shape = (11, 9, 14))#candidate|4212|(11, 9, 14)|var|int8
func_4211_call = mutated_mod.get_global_var('func_4211')
call_4213 = func_4211_call(var_4212)
output = call_4213
func_4214 = relay.Function([var_4212], output)
mutated_mod['func_4214'] = func_4214
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4265 = relay.var("var_4265", dtype = "float64", shape = (10, 7, 14))#candidate|4265|(10, 7, 14)|var|float64
uop_4266 = relay.sinh(var_4265.astype('float64')) # shape=(10, 7, 14)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_4294 = relay.TupleGetItem(func_167_call(), 0)
call_4295 = relay.TupleGetItem(func_168_call(), 0)
uop_4303 = relay.asin(var_4265.astype('float64')) # shape=(10, 7, 14)
bop_4309 = relay.equal(uop_4303.astype('bool'), relay.reshape(uop_4266.astype('bool'), relay.shape_of(uop_4303))) # shape=(10, 7, 14)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_4321 = func_2601_call()
call_4322 = func_2601_call()
func_2555_call = mod.get_global_var('func_2555')
func_2556_call = mutated_mod.get_global_var('func_2556')
call_4323 = func_2555_call()
call_4324 = func_2555_call()
output = relay.Tuple([call_4294,bop_4309,call_4321,call_4323,])
output2 = relay.Tuple([call_4295,bop_4309,call_4322,call_4324,])
func_4329 = relay.Function([var_4265,], output)
mod['func_4329'] = func_4329
mod = relay.transform.InferType()(mod)
var_4330 = relay.var("var_4330", dtype = "float64", shape = (10, 7, 14))#candidate|4330|(10, 7, 14)|var|float64
output = func_4329(var_4330)
func_4331 = relay.Function([var_4330], output)
mutated_mod['func_4331'] = func_4331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_4351 = relay.TupleGetItem(func_496_call(), 0)
call_4352 = relay.TupleGetItem(func_498_call(), 0)
output = relay.Tuple([call_4351,])
output2 = relay.Tuple([call_4352,])
func_4354 = relay.Function([], output)
mod['func_4354'] = func_4354
mod = relay.transform.InferType()(mod)
output = func_4354()
func_4355 = relay.Function([], output)
mutated_mod['func_4355'] = func_4355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2736_call = mod.get_global_var('func_2736')
func_2737_call = mutated_mod.get_global_var('func_2737')
call_4421 = relay.TupleGetItem(func_2736_call(), 0)
call_4422 = relay.TupleGetItem(func_2737_call(), 0)
func_3059_call = mod.get_global_var('func_3059')
func_3064_call = mutated_mod.get_global_var('func_3064')
var_4426 = relay.var("var_4426", dtype = "float32", shape = (77, 4))#candidate|4426|(77, 4)|var|float32
const_4427 = relay.const([False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,True], dtype = "bool")#candidate|4427|(64,)|const|bool
var_4428 = relay.var("var_4428", dtype = "float32", shape = (1694,))#candidate|4428|(1694,)|var|float32
call_4425 = relay.TupleGetItem(func_3059_call(relay.reshape(var_4426.astype('float32'), [308,]), relay.reshape(const_4427.astype('bool'), [64,]), relay.reshape(var_4428.astype('float32'), [847, 2]), ), 8)
call_4429 = relay.TupleGetItem(func_3064_call(relay.reshape(var_4426.astype('float32'), [308,]), relay.reshape(const_4427.astype('bool'), [64,]), relay.reshape(var_4428.astype('float32'), [847, 2]), ), 8)
func_2966_call = mod.get_global_var('func_2966')
func_2967_call = mutated_mod.get_global_var('func_2967')
call_4432 = func_2966_call()
call_4433 = func_2966_call()
output = relay.Tuple([call_4421,call_4425,var_4426,const_4427,var_4428,call_4432,])
output2 = relay.Tuple([call_4422,call_4429,var_4426,const_4427,var_4428,call_4433,])
func_4447 = relay.Function([var_4426,var_4428,], output)
mod['func_4447'] = func_4447
mod = relay.transform.InferType()(mod)
mutated_mod['func_4447'] = func_4447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4447_call = mutated_mod.get_global_var('func_4447')
var_4449 = relay.var("var_4449", dtype = "float32", shape = (77, 4))#candidate|4449|(77, 4)|var|float32
var_4450 = relay.var("var_4450", dtype = "float32", shape = (1694,))#candidate|4450|(1694,)|var|float32
call_4448 = func_4447_call(var_4449,var_4450,)
output = call_4448
func_4451 = relay.Function([var_4449,var_4450,], output)
mutated_mod['func_4451'] = func_4451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2010_call = mutated_mod.get_global_var('func_2010')
call_4453 = func_2009_call()
call_4454 = func_2009_call()
output = call_4453
output2 = call_4454
func_4468 = relay.Function([], output)
mod['func_4468'] = func_4468
mod = relay.transform.InferType()(mod)
output = func_4468()
func_4469 = relay.Function([], output)
mutated_mod['func_4469'] = func_4469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1686_call = mod.get_global_var('func_1686')
func_1687_call = mutated_mod.get_global_var('func_1687')
call_4481 = func_1686_call()
call_4482 = func_1686_call()
func_160_call = mod.get_global_var('func_160')
func_161_call = mutated_mod.get_global_var('func_161')
call_4523 = relay.TupleGetItem(func_160_call(), 4)
call_4524 = relay.TupleGetItem(func_161_call(), 4)
output = relay.Tuple([call_4481,call_4523,])
output2 = relay.Tuple([call_4482,call_4524,])
func_4542 = relay.Function([], output)
mod['func_4542'] = func_4542
mod = relay.transform.InferType()(mod)
output = func_4542()
func_4543 = relay.Function([], output)
mutated_mod['func_4543'] = func_4543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_4644 = relay.TupleGetItem(func_496_call(), 0)
call_4645 = relay.TupleGetItem(func_498_call(), 0)
var_4676 = relay.var("var_4676", dtype = "float32", shape = (11, 16, 14))#candidate|4676|(11, 16, 14)|var|float32
bop_4677 = relay.divide(call_4644.astype('float64'), var_4676.astype('float64')) # shape=(11, 16, 14)
bop_4680 = relay.divide(call_4645.astype('float64'), var_4676.astype('float64')) # shape=(11, 16, 14)
func_3651_call = mod.get_global_var('func_3651')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_4686 = relay.TupleGetItem(func_3651_call(), 2)
call_4687 = relay.TupleGetItem(func_3652_call(), 2)
var_4694 = relay.var("var_4694", dtype = "float64", shape = (11, 16, 14))#candidate|4694|(11, 16, 14)|var|float64
bop_4695 = relay.right_shift(bop_4677.astype('int16'), relay.reshape(var_4694.astype('int16'), relay.shape_of(bop_4677))) # shape=(11, 16, 14)
bop_4698 = relay.right_shift(bop_4680.astype('int16'), relay.reshape(var_4694.astype('int16'), relay.shape_of(bop_4680))) # shape=(11, 16, 14)
bop_4701 = relay.greater_equal(call_4686.astype('bool'), call_4644.astype('bool')) # shape=(11, 6, 14)
bop_4704 = relay.greater_equal(call_4687.astype('bool'), call_4645.astype('bool')) # shape=(11, 6, 14)
output = relay.Tuple([bop_4695,bop_4701,])
output2 = relay.Tuple([bop_4698,bop_4704,])
func_4708 = relay.Function([var_4676,var_4694,], output)
mod['func_4708'] = func_4708
mod = relay.transform.InferType()(mod)
mutated_mod['func_4708'] = func_4708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4708_call = mutated_mod.get_global_var('func_4708')
var_4710 = relay.var("var_4710", dtype = "float32", shape = (11, 16, 14))#candidate|4710|(11, 16, 14)|var|float32
var_4711 = relay.var("var_4711", dtype = "float64", shape = (11, 16, 14))#candidate|4711|(11, 16, 14)|var|float64
call_4709 = func_4708_call(var_4710,var_4711,)
output = call_4709
func_4712 = relay.Function([var_4710,var_4711,], output)
mutated_mod['func_4712'] = func_4712
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4764 = relay.const([[[-1,-7,-10,-1,4,-10,-2,-7,10,-2,2,-8,-10,7],[10,-9,10,-9,3,-9,4,5,8,-6,3,-3,-7,5],[-9,-5,-6,1,10,-4,10,1,-5,-1,10,5,7,-6],[6,2,-6,6,1,5,7,-6,7,10,6,8,9,7],[9,2,7,-1,-1,4,-4,3,2,-8,-7,-10,-2,-8],[2,-8,-1,6,-2,-2,4,5,8,-1,7,9,10,8],[-10,2,4,-2,-8,-4,5,-5,3,-9,8,-1,-9,-9],[-10,8,5,-9,-10,5,-9,-10,6,-5,5,-10,-4,-8]],[[-1,-2,5,-10,-2,1,-2,-9,7,7,-5,2,8,1],[-7,7,-5,9,-10,10,10,1,-8,-6,8,-8,-8,2],[-6,-8,-3,1,3,-8,10,5,1,-3,4,6,3,-6],[-6,-6,3,-5,10,-6,5,8,-4,-7,-6,-6,10,-4],[-5,5,-1,4,-5,-2,-7,10,4,7,-8,5,-5,-4],[-2,-1,1,10,6,-9,5,6,2,5,-3,-4,-7,2],[-9,-10,-7,9,6,3,5,3,-3,-5,-6,-9,-3,7],[-1,3,-9,2,-3,-7,2,10,-10,-1,-5,-8,-5,9]],[[9,7,7,9,-4,-4,-3,5,-1,-5,2,-3,-4,-8],[-7,6,-1,5,4,5,-6,4,-2,-7,8,3,9,6],[7,2,-9,2,-3,9,3,-7,7,-10,-10,1,8,7],[9,1,-5,4,3,-3,4,-6,-8,-8,2,-3,3,-10],[9,8,-1,6,2,-10,-5,-1,-5,-6,10,9,9,6],[-9,3,-6,-5,-2,2,10,-10,5,2,8,4,-1,2],[8,-2,-4,4,-7,-6,-10,2,-10,-3,-4,6,4,-2],[6,4,9,10,10,3,3,-4,-8,10,-9,-7,-9,-4]],[[5,-7,9,-5,-7,2,-1,5,-6,6,7,4,-1,8],[-3,5,8,9,5,-8,10,-2,-6,-6,5,-4,8,-8],[-8,2,-9,-9,1,6,1,10,5,4,-8,2,10,8],[6,10,-4,-7,-9,4,6,8,6,-1,-2,10,3,5],[-10,5,1,-1,-8,-10,7,-9,-5,-10,-8,2,6,-10],[-6,6,8,-1,7,-5,-2,-1,10,4,8,-6,7,-6],[4,3,3,-5,1,9,1,2,-9,-4,7,-4,-4,-3],[2,5,7,5,5,10,-9,-3,-5,4,2,-4,-10,3]],[[-1,-4,-6,-7,6,3,-4,-9,-2,-3,-9,-2,9,-9],[-4,-2,9,-6,-6,9,6,5,-5,-5,9,5,-7,1],[2,-4,2,-9,-3,-9,-9,10,10,-7,10,-1,10,-8],[-4,-4,7,-1,3,4,-7,4,9,3,-9,-4,2,9],[5,10,4,-4,-1,4,6,-1,-10,9,9,1,-2,-9],[2,8,-5,7,-2,4,5,-9,-5,2,-3,5,2,-2],[-10,-1,-10,2,-7,9,-7,3,9,2,10,9,8,-7],[-9,7,1,2,6,1,10,-5,2,-2,9,7,2,5]],[[10,-10,-3,6,6,-9,3,-8,-9,3,-10,-4,-9,-8],[-7,-10,-7,5,9,5,-3,-10,6,9,-10,9,-7,8],[-4,-6,-1,9,7,9,-7,-1,-1,-7,8,2,-10,7],[4,3,4,-8,-8,-3,10,10,6,-10,-4,-4,6,-2],[9,-4,-7,-10,8,5,4,10,-8,5,-6,1,-5,2],[-2,-8,6,-3,-10,-3,10,4,-6,10,-7,-9,2,-2],[-8,-6,9,-1,-7,9,7,8,1,-3,-8,-4,10,7],[5,8,-4,-4,-10,9,9,-7,-9,6,-8,-9,-2,1]],[[-6,3,-8,5,-5,6,-3,-5,2,-1,-6,2,-5,-10],[4,8,-10,1,4,-9,-6,6,-9,-4,-2,1,-1,4],[4,3,-5,-7,-6,2,-4,-10,-7,2,7,6,-10,-1],[-2,6,-9,5,2,7,-10,-7,-2,-5,-5,-3,-2,4],[-8,4,10,-7,1,-10,-3,2,-8,8,-7,-6,-1,-7],[-2,6,7,-1,1,3,1,6,2,7,-8,9,9,10],[-8,2,7,9,7,-1,9,10,-9,4,-4,-1,-10,-10],[8,1,-6,-6,-1,8,-5,6,-3,2,3,-5,-10,1]],[[-9,-9,2,2,4,-2,-3,5,-9,9,-7,6,-10,-7],[7,2,-1,-2,-2,-1,-4,-1,3,-4,7,6,8,-4],[-3,1,-10,-6,4,2,-6,-2,5,-9,9,3,-9,-8],[3,7,4,7,-9,-3,-5,-10,-7,1,-4,-2,-4,-9],[-8,-1,-10,8,-6,-7,10,-9,6,-5,-2,7,-9,-10],[-6,9,7,-6,8,-10,10,1,-9,6,10,8,-2,-9],[-4,7,8,-5,-5,10,6,10,-9,-10,1,-4,9,-2],[-7,-5,8,2,-7,-10,9,-10,2,-2,8,1,-8,-10]],[[-5,2,-3,-2,9,8,-4,-2,8,9,-9,3,5,-7],[-7,3,-9,-3,-2,-5,2,10,-2,8,-2,4,-9,1],[10,-6,6,10,-4,10,-9,-8,-10,6,1,-4,10,6],[-4,3,6,-3,-9,-8,6,-9,-2,-8,5,6,8,9],[-7,-7,-6,7,10,-4,10,9,1,3,-5,8,6,6],[-6,-2,-3,-6,-1,-1,-2,7,-9,10,-6,-7,-7,-3],[-1,-5,-5,9,-9,-5,9,-9,-2,-5,-5,-5,9,4],[-7,8,-5,4,-1,-7,2,-9,9,4,-6,-4,-3,6]],[[9,9,-6,-5,-10,-10,-5,-3,9,8,4,9,8,-3],[-10,-6,-8,6,-1,-4,1,-6,-10,-1,-3,-9,10,6],[-9,10,7,-10,-10,6,9,-4,5,7,9,6,-9,-8],[1,7,-1,3,3,-3,-2,-4,-1,1,6,-1,10,-6],[2,-7,8,-7,3,8,-3,-6,-2,-4,-9,-8,5,-10],[9,-5,2,4,-8,-10,10,6,9,-6,2,-3,-7,6],[10,-8,-5,-8,4,8,4,4,6,-5,2,5,3,5],[-6,-3,-8,-5,-5,2,8,3,6,6,-5,-6,-4,3]],[[8,7,-10,2,5,-2,2,-10,-4,10,2,3,-7,-6],[-1,-8,6,2,-8,-5,2,3,-5,-4,-8,10,-2,-7],[1,10,2,-10,-3,-6,9,-4,-3,8,-10,5,-7,-7],[-8,-8,8,3,-5,-10,-9,9,-10,-2,-10,8,-3,7],[10,10,8,10,-7,-8,10,-3,4,9,-7,-6,-3,6],[-1,-7,6,-10,-5,-4,5,-7,10,4,-1,10,5,-4],[2,4,2,-4,-9,5,-5,8,-1,-5,-4,8,3,5],[6,6,-1,9,4,-4,-8,-6,-9,4,-9,4,-9,3]],[[2,10,9,-4,-8,4,8,4,-8,-10,-7,9,-3,-1],[5,4,2,-5,-10,9,-2,2,2,6,8,-9,8,1],[10,6,6,5,2,8,7,-3,-4,-10,3,-6,-2,8],[-2,-3,-2,10,-7,-7,2,-2,-7,-9,2,-7,5,-7],[-10,-7,5,7,-9,9,-9,-6,6,-2,-2,1,-2,10],[4,4,-4,8,-3,1,9,7,-8,3,-10,4,7,8],[8,7,-5,5,2,-1,8,6,-1,9,7,-3,8,10],[5,-5,6,-4,-2,10,-4,-10,4,2,-10,-5,5,-5]],[[5,6,-3,-4,4,-10,1,-2,-3,-9,-10,-4,-6,-9],[-7,1,10,-6,10,-4,2,-1,-5,7,-7,7,-1,-10],[-10,-5,-5,-10,8,10,8,2,-9,10,-10,-4,-7,-4],[1,-3,-5,7,7,-7,-3,-2,-2,-10,1,-2,9,8],[6,4,6,-8,8,-10,-5,1,-3,-1,-1,-5,1,3],[-5,5,1,-1,-9,-9,-6,-5,6,-1,10,6,-10,-2],[-10,2,6,-7,9,5,6,-6,-4,3,6,1,-3,5],[-7,8,-4,3,8,-8,-7,-6,10,5,-2,4,-2,3]],[[-1,1,-5,-7,9,-10,9,5,-4,1,4,6,4,-3],[-4,-4,-5,4,3,-3,-3,-1,-3,-10,-7,9,-5,-7],[-6,7,-7,4,5,-3,1,-5,9,7,-10,8,-6,-9],[5,-1,-8,-8,1,-8,2,-7,9,7,7,1,9,-7],[10,7,3,4,-8,6,-8,6,-8,-3,6,-7,4,-2],[-9,9,6,5,-3,1,-3,1,-3,-1,3,-10,-6,3],[6,2,-4,-5,6,-10,-8,10,-7,-5,9,3,-10,2],[1,5,-1,-3,7,-5,-9,-1,5,-10,-2,5,9,-5]]], dtype = "int8")#candidate|4764|(14, 8, 14)|const|int8
var_4765 = relay.var("var_4765", dtype = "int8", shape = (14, 8, 14))#candidate|4765|(14, 8, 14)|var|int8
bop_4766 = relay.right_shift(const_4764.astype('int8'), relay.reshape(var_4765.astype('int8'), relay.shape_of(const_4764))) # shape=(14, 8, 14)
output = bop_4766
output2 = bop_4766
func_4770 = relay.Function([var_4765,], output)
mod['func_4770'] = func_4770
mod = relay.transform.InferType()(mod)
var_4771 = relay.var("var_4771", dtype = "int8", shape = (14, 8, 14))#candidate|4771|(14, 8, 14)|var|int8
output = func_4770(var_4771)
func_4772 = relay.Function([var_4771], output)
mutated_mod['func_4772'] = func_4772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_4836 = relay.TupleGetItem(func_965_call(), 0)
call_4837 = relay.TupleGetItem(func_967_call(), 0)
output = call_4836
output2 = call_4837
func_4848 = relay.Function([], output)
mod['func_4848'] = func_4848
mod = relay.transform.InferType()(mod)
output = func_4848()
func_4849 = relay.Function([], output)
mutated_mod['func_4849'] = func_4849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2888_call = mod.get_global_var('func_2888')
func_2890_call = mutated_mod.get_global_var('func_2890')
call_4850 = relay.TupleGetItem(func_2888_call(), 0)
call_4851 = relay.TupleGetItem(func_2890_call(), 0)
func_1083_call = mod.get_global_var('func_1083')
func_1084_call = mutated_mod.get_global_var('func_1084')
call_4865 = relay.TupleGetItem(func_1083_call(), 3)
call_4866 = relay.TupleGetItem(func_1084_call(), 3)
uop_4881 = relay.sinh(call_4865.astype('float64')) # shape=(1694,)
uop_4883 = relay.sinh(call_4866.astype('float64')) # shape=(1694,)
func_3466_call = mod.get_global_var('func_3466')
func_3469_call = mutated_mod.get_global_var('func_3469')
const_4894 = relay.const([8,-6,10,3,10,10,-4,-9,-10,-5,-5,7,-7,3,10,-10,9,-9,4,4,-1,-1,-3,-5,7,7,-6,7,7,9,-3,6,-5,-3,-6,4,1,2,8,-7,1,7,10,9,4,-7,-1,1,7,-6,2,10,-5,-7,4,-8,-10,10,-8,7,1,1,6,-7,-9,-6,10,4,10,10,9,-7,-2,-9,8,-4,-2,10,-8,-1,-9,-8,4,-6,-7,-8,-4,-5,6,9,-2,4,6,3,2,-1,-2,-3,2,3,-8,4,-10,10,-7,-9,-10,4,-8,9,1,-2,-10,-9,4,10,3,-4,6,-6,-1,-1,-9,-6,-10,-8,7,-1,-4,-9,-2,-2,6,-7,-10,-3,-1,3,-9,-8,5,9,-5,1,3,-10,3,-2,-8,9,-4,-10,-9,5,-1,9,9,10,-10,-5,-2,-10,7,-4,-10,2,9,7,4,-8,-4,-10,6,-7,2,-3,-9,1,-4,-10,10,-8,-5,-9,-8,-1,-5,-7,3,-1,-8,-1,-7,10,9,-6,3,10,-1,-4,-7,3,-7,4,4,7,10,-6,4,8,7,4,10,-7,-2,-1,-7,-10,-5,-6,-10,1,-5,-6,-5,2,-10,2,-2,-2,2,-5,8,-5,2,3,6,-3,-1,10,5,9,-10,-5,2,9,1,-2,9,-3,9,-6,-10,-8,10,-8,-1,2,8,6,-7,3,-8,8,-2,-2,-8,6,7,-2,3,4,7,-7,-3,6,-9,9,-3,7,-1,6,5,-9,7,1,-3,6,-9,6,8,-6,-2,4,-4,-3,-10,-4,1,9,-7,8,3,2,6,8,2,3,-8,3,10,7,-5,8,6,-5,-8,-5,-6,-7,-6,10,-8,6,-10,10,-3,3,-7,3,8,10,-3,-9,3,5,2,9,-6,7,-2,-9,1,-4,-3,-6,6,-7,3,10,-3,-7,-8,-4,-1,-4,8,-1,-5,9,-1,9,3,6,3,1,-9,-2,5,3,6,1,3,3,5,6,-1,5,10,-9,7,10,8,-7,7,-9,9,9,1,8,7,6,-8,9,2,2,8,9,1,9,6,-2,-9,7,-4,8,10,7,-4,-7,-6,10,-8,-2,-5,-10,10,-7,5,-8,10,10,3,9,6,6,4,6,6,-2,8,3,-4,-6,6,-7,4,-6,3,-4,1,10,7,7,5,-6,1,-10,4,3,-2,6,-6,-10,-10,-9,-6,8,7,9,-7,5,-8,5,1,-2,8,8,2,2,-4,-7,-2,-4,-4,-8,-7,1,8,-7,-5,3,-9,-5,10,-7,10,5,-10,-10,-1,7,3,-3,-7,-1,1,4,-8,-3,8,-5,3,-2,-8,-9,-5,6,6,1,2,-6,8,3,8,-4,-3,9,-10,10,5,6,-6,10,-2,7,-2,6,-10,-8,4,-9,5,-4,-8,1,-4,5,-9,-3,-5,4,-3,1,-1,4,-5,2,-10,2,-9,-3,-2,-2,-5,-2,5,-10,-8,2,4,-5,-10,6,1,7,-3,-4,9,5,-1,6,5,-4,9,-4,-5,-1,-6,-4,8,-1,-4,-5,-1,8,-9,7,10,-1,-1,-3,8,1,2,-2,-9,-1,-8,-7,-9,10,-7,4,-10,8,3,-8,-5,4,-4,-8,-9,-7,5,7,-9,2,6,5,2,-9,-7,4,6,9,-4,7,6,-4,8,-5,-10,4,4,6,-5,2,2,3,-6,9,1,-7,10,8,-3,-6,1,-1,-9,4,1,-7,-4,10,5,1,-5,-3,-8,-2,5,5,8,-2,2,3,1,-6,-2,-4,8,-3,2,8,8,-2,-8,10,5,-2,-7,2,-7,-5,-5,-6,-4,5,-4,7,-3,-2,8,-6,3,9,5,1,10,-10,5,-9,2,7,7,7,-5,-10,2,-5,5,6,5,-1,3,1,7,9,4,-7,-1,10,3,8,-5,2,-7,10,-8,-9,2,1,10,1,9,4,2,6,3,1,-7,7,-3,-5,10,2,-2,1,6,-7,-8,4,4,-5,4,-4,-1,4,-10,5,-1,-1,-1,-6,-4,3,-3,-2,-7,-3,-7,3,-9,-3,3,10,6,-8,2,5,8,-10,3,9,10,-4,-8,8,1,8,-9,8,10,2,10,9,-5,1,10,-9,-10,9,9,9,9,4,8,5,9,-9,7,9,7,-10,-7,-7,-4,-9,6,-3,-5,-4,8,-10,-9,8,-9,7,-4,-2,8,10,-10,6,-4,2,3,-4,-5,10,7,9,-4,1,5,-8,3,-6,-6,-8,9,-2,5,-7,-4,6,6,5,-4,-7,10,-2,3,5,-8,10,4,-2,-9,1,8,3,5,-2,-8,5,-4,10,-5,-7,-1,-2,8,-4,-3,-10,-2,-4,5,-5,-7,-9,-9,10,-6,-7,-1,-2,3,6,10,-8,9,9,-2,-4,-7,1,4,10,-6,8,5,8,7,7,-10,-10,-9,-4,5,1,3,-8,3,8,6,-9,-8,-1,3,-2,3,5,-1,6,-8,-10,8,9,-7,-3,5,-3,10,-9,4,-9,3,10,4,-2,2,5,-9,3,3,8,-7,2,7,-2,3,7,-7,10,4,4,-1,5,-3,-5,-2,6,-3,7,-2,-10,-10,10,3,-9,-1,2,1,-3,8,5,-2,1,1,-7,7,-7,4,6,-9,-6,-7,-4,8,7,7,7,-2,7,6,-6,1,2,3,5,-3,4,-1,-10,-8,-6,8,-4,-2,4,5,3,-3,1,2,-8,9,7,-10,1,-4,3,-2,4,8,-4,-6,-8,1,-5,-5,8,-4,-4,-1,-2,-3,9,-4,1,-1,-6,1,7,5,-5,-4,-6,5,5,-6,1,4,5,4,-1,-1,5,-10,4,-4,-8,1,9,4,1,2,9,5,5,2,-6,2,-6,6,10,8,-10,-1,-4,4,-7,9,-4,2,4,5,6,3,-2,2,9,-9,9,-8,7,8,10,-1,-10,4,-4,5,-6,2,7], dtype = "uint16")#candidate|4894|(1120,)|const|uint16
call_4893 = relay.TupleGetItem(func_3466_call(relay.reshape(const_4894.astype('uint16'), [14, 8, 10])), 0)
call_4895 = relay.TupleGetItem(func_3469_call(relay.reshape(const_4894.astype('uint16'), [14, 8, 10])), 0)
output = relay.Tuple([call_4850,uop_4881,call_4893,const_4894,])
output2 = relay.Tuple([call_4851,uop_4883,call_4895,const_4894,])
func_4903 = relay.Function([], output)
mod['func_4903'] = func_4903
mod = relay.transform.InferType()(mod)
mutated_mod['func_4903'] = func_4903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4903_call = mutated_mod.get_global_var('func_4903')
call_4904 = func_4903_call()
output = call_4904
func_4905 = relay.Function([], output)
mutated_mod['func_4905'] = func_4905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3082_call = mod.get_global_var('func_3082')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_4937 = func_3082_call()
call_4938 = func_3082_call()
var_4973 = relay.var("var_4973", dtype = "float32", shape = (11, 9, 14))#candidate|4973|(11, 9, 14)|var|float32
bop_4974 = relay.greater_equal(call_4937.astype('bool'), relay.reshape(var_4973.astype('bool'), relay.shape_of(call_4937))) # shape=(11, 9, 14)
bop_4977 = relay.greater_equal(call_4938.astype('bool'), relay.reshape(var_4973.astype('bool'), relay.shape_of(call_4938))) # shape=(11, 9, 14)
output = relay.Tuple([bop_4974,])
output2 = relay.Tuple([bop_4977,])
func_4978 = relay.Function([var_4973,], output)
mod['func_4978'] = func_4978
mod = relay.transform.InferType()(mod)
mutated_mod['func_4978'] = func_4978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4979 = relay.var("var_4979", dtype = "float32", shape = (11, 9, 14))#candidate|4979|(11, 9, 14)|var|float32
func_4978_call = mutated_mod.get_global_var('func_4978')
call_4980 = func_4978_call(var_4979)
output = call_4980
func_4981 = relay.Function([var_4979], output)
mutated_mod['func_4981'] = func_4981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3528_call = mod.get_global_var('func_3528')
func_3530_call = mutated_mod.get_global_var('func_3530')
call_5001 = relay.TupleGetItem(func_3528_call(), 2)
call_5002 = relay.TupleGetItem(func_3530_call(), 2)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_5006 = relay.TupleGetItem(func_965_call(), 0)
call_5007 = relay.TupleGetItem(func_967_call(), 0)
func_4354_call = mod.get_global_var('func_4354')
func_4355_call = mutated_mod.get_global_var('func_4355')
call_5012 = relay.TupleGetItem(func_4354_call(), 0)
call_5013 = relay.TupleGetItem(func_4355_call(), 0)
output = relay.Tuple([call_5001,call_5006,call_5012,])
output2 = relay.Tuple([call_5002,call_5007,call_5013,])
func_5034 = relay.Function([], output)
mod['func_5034'] = func_5034
mod = relay.transform.InferType()(mod)
output = func_5034()
func_5035 = relay.Function([], output)
mutated_mod['func_5035'] = func_5035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5038 = relay.var("var_5038", dtype = "uint16", shape = ())#candidate|5038|()|var|uint16
var_5039 = relay.var("var_5039", dtype = "uint16", shape = (3, 4, 1))#candidate|5039|(3, 4, 1)|var|uint16
bop_5040 = relay.left_shift(var_5038.astype('uint16'), var_5039.astype('uint16')) # shape=(3, 4, 1)
bop_5047 = relay.less(bop_5040.astype('bool'), relay.reshape(var_5039.astype('bool'), relay.shape_of(bop_5040))) # shape=(3, 4, 1)
output = bop_5047
output2 = bop_5047
func_5058 = relay.Function([var_5038,var_5039,], output)
mod['func_5058'] = func_5058
mod = relay.transform.InferType()(mod)
mutated_mod['func_5058'] = func_5058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5058_call = mutated_mod.get_global_var('func_5058')
var_5060 = relay.var("var_5060", dtype = "uint16", shape = ())#candidate|5060|()|var|uint16
var_5061 = relay.var("var_5061", dtype = "uint16", shape = (3, 4, 1))#candidate|5061|(3, 4, 1)|var|uint16
call_5059 = func_5058_call(var_5060,var_5061,)
output = call_5059
func_5062 = relay.Function([var_5060,var_5061,], output)
mutated_mod['func_5062'] = func_5062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4354_call = mod.get_global_var('func_4354')
func_4355_call = mutated_mod.get_global_var('func_4355')
call_5081 = relay.TupleGetItem(func_4354_call(), 0)
call_5082 = relay.TupleGetItem(func_4355_call(), 0)
output = call_5081
output2 = call_5082
func_5083 = relay.Function([], output)
mod['func_5083'] = func_5083
mod = relay.transform.InferType()(mod)
output = func_5083()
func_5084 = relay.Function([], output)
mutated_mod['func_5084'] = func_5084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5124 = relay.var("var_5124", dtype = "float32", shape = (16, 12, 7))#candidate|5124|(16, 12, 7)|var|float32
uop_5125 = relay.asin(var_5124.astype('float32')) # shape=(16, 12, 7)
uop_5127 = relay.cosh(uop_5125.astype('float64')) # shape=(16, 12, 7)
output = relay.Tuple([uop_5127,])
output2 = relay.Tuple([uop_5127,])
func_5131 = relay.Function([var_5124,], output)
mod['func_5131'] = func_5131
mod = relay.transform.InferType()(mod)
mutated_mod['func_5131'] = func_5131
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5132 = relay.var("var_5132", dtype = "float32", shape = (16, 12, 7))#candidate|5132|(16, 12, 7)|var|float32
func_5131_call = mutated_mod.get_global_var('func_5131')
call_5133 = func_5131_call(var_5132)
output = call_5133
func_5134 = relay.Function([var_5132], output)
mutated_mod['func_5134'] = func_5134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_5158 = func_64_call()
call_5159 = func_64_call()
output = relay.Tuple([call_5158,])
output2 = relay.Tuple([call_5159,])
func_5160 = relay.Function([], output)
mod['func_5160'] = func_5160
mod = relay.transform.InferType()(mod)
output = func_5160()
func_5161 = relay.Function([], output)
mutated_mod['func_5161'] = func_5161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_64_call = mod.get_global_var('func_64')
func_66_call = mutated_mod.get_global_var('func_66')
call_5178 = func_64_call()
call_5179 = func_64_call()
output = call_5178
output2 = call_5179
func_5198 = relay.Function([], output)
mod['func_5198'] = func_5198
mod = relay.transform.InferType()(mod)
output = func_5198()
func_5199 = relay.Function([], output)
mutated_mod['func_5199'] = func_5199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_5241 = relay.TupleGetItem(func_1823_call(), 1)
call_5242 = relay.TupleGetItem(func_1825_call(), 1)
var_5245 = relay.var("var_5245", dtype = "float32", shape = (11, 9, 14))#candidate|5245|(11, 9, 14)|var|float32
bop_5246 = relay.power(call_5241.astype('float32'), var_5245.astype('float32')) # shape=(11, 9, 14)
bop_5249 = relay.power(call_5242.astype('float32'), var_5245.astype('float32')) # shape=(11, 9, 14)
output = relay.Tuple([bop_5246,])
output2 = relay.Tuple([bop_5249,])
func_5257 = relay.Function([var_5245,], output)
mod['func_5257'] = func_5257
mod = relay.transform.InferType()(mod)
var_5258 = relay.var("var_5258", dtype = "float32", shape = (11, 9, 14))#candidate|5258|(11, 9, 14)|var|float32
output = func_5257(var_5258)
func_5259 = relay.Function([var_5258], output)
mutated_mod['func_5259'] = func_5259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1084_call = mutated_mod.get_global_var('func_1084')
call_5306 = relay.TupleGetItem(func_1083_call(), 1)
call_5307 = relay.TupleGetItem(func_1084_call(), 1)
output = call_5306
output2 = call_5307
func_5317 = relay.Function([], output)
mod['func_5317'] = func_5317
mod = relay.transform.InferType()(mod)
mutated_mod['func_5317'] = func_5317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5317_call = mutated_mod.get_global_var('func_5317')
call_5318 = func_5317_call()
output = call_5318
func_5319 = relay.Function([], output)
mutated_mod['func_5319'] = func_5319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4075_call = mod.get_global_var('func_4075')
func_4076_call = mutated_mod.get_global_var('func_4076')
call_5350 = relay.TupleGetItem(func_4075_call(), 0)
call_5351 = relay.TupleGetItem(func_4076_call(), 0)
output = call_5350
output2 = call_5351
func_5370 = relay.Function([], output)
mod['func_5370'] = func_5370
mod = relay.transform.InferType()(mod)
output = func_5370()
func_5371 = relay.Function([], output)
mutated_mod['func_5371'] = func_5371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2200_call = mod.get_global_var('func_2200')
func_2201_call = mutated_mod.get_global_var('func_2201')
call_5402 = relay.TupleGetItem(func_2200_call(), 0)
call_5403 = relay.TupleGetItem(func_2201_call(), 0)
output = relay.Tuple([call_5402,])
output2 = relay.Tuple([call_5403,])
func_5407 = relay.Function([], output)
mod['func_5407'] = func_5407
mod = relay.transform.InferType()(mod)
mutated_mod['func_5407'] = func_5407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5407_call = mutated_mod.get_global_var('func_5407')
call_5408 = func_5407_call()
output = call_5408
func_5409 = relay.Function([], output)
mutated_mod['func_5409'] = func_5409
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5438 = relay.var("var_5438", dtype = "float64", shape = (11, 12, 16))#candidate|5438|(11, 12, 16)|var|float64
var_5439 = relay.var("var_5439", dtype = "float64", shape = (11, 12, 16))#candidate|5439|(11, 12, 16)|var|float64
bop_5440 = relay.less(var_5438.astype('bool'), relay.reshape(var_5439.astype('bool'), relay.shape_of(var_5438))) # shape=(11, 12, 16)
func_5257_call = mod.get_global_var('func_5257')
func_5259_call = mutated_mod.get_global_var('func_5259')
const_5447 = relay.const([[-1.291029,-8.555212,-8.992842,-9.066389,-8.253391,5.269148,-0.427149,-3.998695,-3.407126,-5.563773,-6.959813,8.903588,6.093611,1.584283,-4.446522,-4.918804,-9.561185,8.912583,0.031849,4.939934,-4.154475,2.348338,-8.377359,-7.699947,9.065549,1.461143,-6.799193,6.274109,3.834122,3.341525,3.028135,8.476590,-9.831328,-1.919916,-1.853526,9.594160,-5.053552,1.473121,-7.778392,8.164881,6.591013,-7.046434,-7.800205,1.932728,-2.399216,2.298082,-6.364046,0.078223,4.446771,7.153869,1.118062,5.097772,8.780297,2.268300,-6.918783,6.886598,1.503546,3.483356,8.653929,-8.555826,1.914289,2.244417,-2.301274,8.237048,-0.034243,8.392521,2.447618,-7.218188,3.165923,6.821317,-8.972914,7.614667,-5.569625,7.583455,-5.166399,9.309742,-1.814279,3.745432,-0.738134,-1.102877,4.603710,-0.159037,-2.156211,4.142365,-2.808015,-2.418092,4.392144,9.687820,-8.957121,9.629660,-1.756315,0.742968,3.907242,6.005751,1.479982,4.263381,0.464054,4.832166,-2.561690,8.699920,4.309537,7.598147,-3.346672,-7.481283,-3.663443,6.275404,8.207544,8.111432,2.557816,-4.637926,-6.237164,-3.118001,8.010401,-1.389428,-4.675530,7.425359,4.061217,7.982108,1.195777,-5.668275,3.289317,-1.715711,-4.149703,-0.465534,-8.679367,-6.829058,-9.161851,-9.750109,1.499613,6.682756,-8.190701,2.519279,3.725977,1.501790,6.582230,-7.965205,2.334848,4.282947,-2.822928,-9.028684,-1.263100,-9.885436,5.163011,-4.040059,5.295063,-8.426670,-2.898377,1.174190,-8.862288,-3.938868,-7.767338,4.099678,7.639634,-2.010220,-8.799792,-3.319268,5.429091,1.308487,1.896814,4.895488,9.370265,6.177416,-8.365761,5.927465,9.393736,-6.787475,2.764143,-6.398091,-3.021279,-2.345243,8.897928,6.444894,9.139082,2.857149,-2.929600,4.397067,-5.518103,-2.723588,0.408735,-1.328770,7.081023,4.258266,-0.722742,-2.015180,-2.600106,9.676082,6.831969,-1.050176,0.986867,-5.379638,7.646240,8.889472,-1.238987,-1.848991,0.460799,-0.404223,3.245376,4.119017,3.109638,-5.491036,4.401061,7.400824,-7.006889,4.237992,4.025304,2.426567,-9.418186,6.840580,-7.837670,-5.429296,-5.068397,8.424511,-3.354932,8.508792,-1.970229,7.827984,3.838488,-6.862335,8.532142,0.607939,0.123453,6.217038,8.635222,-7.199663,-1.165359,1.974515,-8.772527,-0.342313,-5.890949,-1.194435,4.329121,-7.849553,2.533681,-0.516426,-3.670283,6.919774,-0.315961,7.036209,8.347546,-3.628888,1.114812,-7.175275,-6.746558,-2.137252,-2.426739,8.326219,6.366039,-0.985003,-2.471616,4.003155,-2.056488,8.350171,2.653875,-3.824045,-2.693711,-4.885752,4.516396,1.621412,9.885570,-3.898859,0.575666,9.166557,4.213139,7.733681,-9.060609,-3.607457,3.356847,0.010651,0.912617,-5.305988,-3.397755,7.529517,6.100290,4.767751,-9.915121,4.153734,9.567575,-1.788635,-1.300400,9.752858,-0.511243,-3.035631,1.119352,-0.844849,1.991182,-7.844029,0.469454,0.933818,1.411899,5.970176,-8.395184,6.507335,8.635978,-7.981396,8.285183,-5.685937,-1.802571,9.580486,8.359845,-8.822051,-2.793876,-6.728882,-4.464223,3.345306,8.949324,5.691378,8.232963,0.951647,7.975791,-3.084297,0.420870,-6.907072,2.909412,2.898022,-2.772778,-2.201822,3.342330,-5.797868,-2.273370,8.932491,0.823147,-0.637663,5.747079,5.426650,3.214624,0.455813,3.520454,-9.771578,4.940582,4.147502,9.034900,7.591236,-0.123652,-2.841519,7.695551,-9.829979,1.016654,5.201527,2.563451,0.109561,-3.111259,0.851945,-4.161504,7.297743,-6.272847,8.970171,-0.806923,-7.304564,4.347704,9.058346,-0.875178,5.675990,-3.017105,-5.706414,6.527181,2.717969,-8.941041,8.399018,-8.230735,-7.061395,8.100917,3.005042,-8.764443,7.203503,-2.343505,-9.017982,-6.670526,-3.154066,-0.397382,-4.652361,-5.401783,-6.543306,4.164158,-3.339731,-0.246031,-7.109021,-2.068760,0.910379,4.695069,-4.235653,2.929907,-6.471917,-8.182359,1.555624,8.582719,9.428271,8.454740,-8.663108,9.371948,-7.462463,4.108787,-9.726013,-2.593593,3.987065,-8.768027,-1.295572,-9.882441,0.811000,1.471819,-3.854201,0.842299,3.421035,0.576892,9.335733,-9.452035,-4.839324,-4.490316,1.354979,-7.653587,-8.122735,8.358825,-0.438342,7.539862,-4.170909,-3.424611,6.501822,-6.162842,-7.305148,-7.097458,3.636413,-6.696003,-8.039069,-6.337589,9.313976,-4.915890,5.513429,-6.951010,-4.194594,0.129770,0.673901,0.472760,2.862205,0.254739,5.732063,3.645865,-0.410691,-9.717577,-0.387579,-2.332977,3.419287,3.180381,-0.573896,-5.430153,6.812499,-1.591773,-4.229090,3.342688,8.418254,4.959177,-7.291166,7.487443,-5.082725,-3.189855,-7.454519,8.385741,4.591891,-1.427625,-1.381144,-6.315533,8.166040,-7.730388,-3.144242,6.794535,-3.820651,-3.237274,-4.387703,0.669377,9.637986,6.388237,9.637649,0.063802,-0.441346,-8.811196,3.903238,-7.027208,1.187689,-8.959133,6.413968,-0.318367,-4.572915,-2.844585,-0.758931,-4.480085,6.826432,-8.261120,-7.382437,-0.413032,6.214198,1.324356,7.585534,6.726728,9.400056,6.701794,-3.418829,-8.320805,-2.986576,9.025650,7.991704,2.858642,9.195544,8.956793,7.914871,-5.356915,-6.586430,4.137629,-0.283012,5.901359,-7.613985,-9.108398,-5.068780,-2.328011,2.490479,2.156731,6.485362,-4.990951,-3.225627,-2.432272,7.308746,8.584905,-4.599238,9.014194,3.604368,-3.943128,4.480744,-6.226525,-5.689973,9.809142,-1.157037,-9.240706,9.092353,4.303098,-6.748242,6.629107,-1.766502,3.441570,-9.315297,0.985267,5.897775,2.519531,-5.012716,-3.311337,-8.198927,0.804936,5.528534,-2.781888,-1.521382,-2.782932,7.294482,-2.726866,-2.037295,0.797878,-1.810402,1.447180,-1.238717,6.081684,-6.328575,8.636602,5.262803,-0.813590,-6.023130,7.014577,-9.811657,8.554668,4.206969,4.575414,-2.565007,-8.179484,-2.189775,-4.935919,6.220739,9.399797,-0.437656,-0.708944,1.810126,-2.823938,-6.002067,-9.149194,9.008056,-4.926675,4.074489,5.287758,-0.583131,2.881202,5.792687,-0.800616,9.969812,-9.341720,-3.716701,5.474885,2.748067,-8.898874,6.137002,-7.443634,-2.935450,0.591209,1.978565,3.544880,9.829710,-6.389409,1.311800,1.272463,-1.847543,-9.116508,-0.938194,6.195457,0.326628,8.402224,-1.849395,4.935343,7.942050,5.668217,9.352679,-8.463231,5.082721,1.916587,8.255842,9.746613,3.353619,3.215079,7.873054,4.822520,-9.521700,4.476869,6.547395,7.807411,8.733923,4.250379,-5.582364,4.842460,-3.766224,-8.019989,5.960408,7.094299,9.832370,1.234227,4.684584,6.848802,3.270985,3.981060,0.994610,5.030563,9.046621,-0.114388,4.051562,2.551135,-1.142248,8.172903,1.005057,-0.496671,0.117300,9.257198,5.570957,-9.944503,5.541504,1.594629,1.216282,5.455787,8.049967,-9.341709,-1.697677,-4.372714,1.286615,-9.197583,-3.364072,2.014072,-3.574041,3.012193,4.921400,9.194389,2.067600,1.700212,2.781157,4.788779,-9.258549,7.545551,6.618064,-9.266545,-4.122926,6.124211,8.158025,-6.006200,5.172055,2.427391,-5.585499,8.485904,6.845892,-9.884945,9.461738,4.916292,5.050135,-7.058420,-3.923112,0.101310,-4.435216,-9.115712,5.828492,7.905262,-7.896501,4.471591,4.532472,-6.018037,6.416291,-4.666372,-2.741480,1.797664,-8.659262,-4.326365,-2.080433,9.704074,-7.674564,-6.057848,4.875029,-6.723516,2.130643,-9.897187,-1.812334,1.626412,3.308947,-1.024043,-6.977145,6.862666,-9.854416,1.545714,8.669855,2.023015,-4.571654,0.187379,5.192740,2.480288,8.773710,-2.056764,-7.831530,5.462562,9.768533,1.529202,5.880860,-9.112843,-9.359961,-1.697294,8.634512,2.250979,-2.615470,9.172423,-7.649522,-7.204029,-3.825213,6.578912,-2.339265,-5.269743,1.243499,9.428311,-7.036747,-0.272887,-4.621667,-4.359069,-7.762781,9.895320,-0.462562,-9.051222,-1.307144,-3.110588,7.976056,4.823531,-8.392061,7.789219,-8.543505,2.093155,7.066991,8.480342,-7.599121,5.351545,-7.895949,5.910596,5.603324,6.654918,-2.669236,-9.735914,-5.430456,-6.814426,7.816875,-8.529423,-7.312534,-0.657927,2.524172,7.141936,3.739418,-1.494468,-0.247178,-5.745939,6.626266,5.134861,3.883830,-3.476892,4.028182,-9.506692,-8.103253,-3.622026,-6.264855,-7.712331,0.363461,-7.302746,-1.331518,-8.406338,-5.257341,-7.680560,-6.063338,-8.057195,0.826082,3.762119,9.578879,2.690555,-2.149948,-2.989653,-3.970828,-1.811019,2.258733,-7.223480,5.371033,-3.442350,5.873977,-2.753876,-7.982941,8.669782,1.569926,-0.998959,6.379558,-3.368251,-2.553944,-0.258207,-5.208849,-7.543389,8.362851,8.020980,4.146629,7.534969,3.580994,-4.845478,-4.269294,9.600771,4.499672,-4.149533,-3.967611,-6.642315,1.750514,0.476659,-8.069799,2.046162,0.760381,-9.401485,-4.248364,9.494954,1.904792,2.948451,-9.565552,2.899852,8.623253,-8.032405,9.742663,-4.454126,3.572300,-2.955112,8.503960,-2.367790,-2.323137,8.872299,-8.275720,-4.315174,-3.954285,8.191174,8.112766,-1.732781,-1.441108,-5.557070,-6.167669,-4.405563,-4.699760,2.638854,0.605749,-3.310172,-7.914467,-7.814231,7.070116,4.603671,3.252619,-5.455044,7.985752,5.964319,5.277085,9.951555,-9.187841,8.958328,-1.393143,-9.427179,-6.690680,-7.164027,-4.037507,4.302165,2.894284,1.149069,3.491345,1.752965,1.985468,-6.075782,-8.800688,-9.244028,-7.954931,-7.746016,-1.741151,-6.190563,9.052140,8.656042,1.072139,2.982179,4.194972,4.330400,-3.058834,-9.744451,0.339323,-9.703057,-9.850770,-4.548916,2.418452,-1.639806,8.714430,-2.507815,8.851583,-1.082895,7.624895,9.720411,4.012178,9.324689,-1.513669,0.556490,6.772393,1.029892,-0.792572,-2.233492,-0.657784,5.578760,0.829526,0.709374,3.730450,1.349186,3.834319,-6.461366,-6.553334,7.672143,3.984873,-7.372662,-5.478791,-4.714512,-0.039739,-0.832846,6.496721,-7.839205,-5.469319,4.157526,-3.620628,-0.505387,-1.208396,-6.398651,-8.906371,7.768902,-3.036063,-5.270221,6.473905,9.055443,3.868328,1.151144,0.180410,8.825602,5.353944,5.124348,-6.682367,1.860022,-7.449902,6.402841,6.011789,-4.987854,-2.873284,2.284733,-7.366416,0.867995,-9.345072,-4.762257,3.615158,6.463066,5.340666,-9.333946,-9.983719,-5.813065,9.244252,-9.825701,-3.183448,-2.167706,0.674982,-8.761661,-1.366039,-3.532254,-1.953492,-6.001244,-4.761155,-2.563289,-3.535467,4.026919,5.859621,-4.108088,8.998561,9.939112,4.433918,0.804837,2.124546,-4.206732,3.953058,0.074079,-3.639306,8.255959,0.774442,-8.872029,-5.801938,5.256966,1.123557,-0.987082,-9.425115,-4.063945,3.958244,-1.514252,2.552258,-9.981778,9.778939,6.689820,3.437314,1.028752,-0.541449,2.293303,1.144351,-0.082712,-6.987962,-3.604466,8.318292,-6.367261,-9.648933,0.979234,-4.775389,-7.465209,0.257920,1.707842,8.399274,-2.660679,-7.394495,-7.138543,-7.149265,-6.897351,-2.337143,9.066359,4.630498,-4.975277,-9.328628,9.542673,-8.175185,2.559839,3.769513,-3.399657,2.635840,8.370151,-5.031918,6.504857,-9.643070,7.678659,-0.214075,-7.446046,9.611294,4.403342,6.287663,-0.670179,1.852121,5.305703,-1.799023,4.512726,-7.283578,6.148488,-5.118785,8.883265,-1.103121,9.578659,5.941800,-7.011090,8.906809,1.606378,-0.266591,-5.246224,4.463847,2.243169,1.933818,9.822655,0.981714,1.703399,1.133082,-9.851359,8.796813,7.481240,-9.381102,3.548627,0.424770,-7.854367,-3.500402,2.948010,-3.814189,6.562916,5.587674,-3.300371,6.084002,3.990370,-9.965199,-5.374357,8.557920,0.398688,3.388333,1.949790,5.652627,7.814141,-2.623022,2.960974,2.435913,4.965074,3.149030,0.482307,7.153893,1.742778,-2.281690,2.257142,8.933285,2.842423,-4.537359,-7.469281,-0.275037,8.348488,-3.458765,-2.496275,-6.199362,9.146486,8.893722,-8.488708,8.486802,-6.134251,-0.843583,0.431341,-3.407895,-9.044110,-2.737430,-1.103353,-5.193793,6.806599,-4.204967,-5.629242,1.978117,-4.260265,-2.865123,4.030086,6.115880,-4.299245,-5.801639,4.229558,-0.941674,9.506337,-3.597051,-0.050189,3.330328,-9.802284,1.054009,-0.375334,-9.314037,9.921124,-6.564819,-7.611209,-3.982103,9.100370,-1.636575,-2.113273,-6.319337,1.915968,4.748182,-8.786041,-7.589665,0.115696,2.393957,-1.089148,-6.223944,7.630881,1.991436,-6.980380,-1.944114,-3.279989,7.198606,2.788661,-0.263629,-7.313311,-9.521101,-9.756831,4.706143,-8.166529,-4.194033,-0.478568,-0.483400,5.645282,8.445510,-1.741660,7.922298,0.686954,3.270405,-8.919997,7.078767,6.592880,1.192644,-4.425342,0.726612,-4.500154,-0.003655,8.377206,-1.123896,-9.602045,-8.862963,5.461392,6.098494,-9.164845,4.058934,-3.414610,-1.781815,8.274040,4.147023,-3.031446,-6.520496,-6.532807,-6.069983,-1.974716,-2.407642,-8.323511,8.095251,-3.088567,-6.916158,7.295711,-4.576007,4.344188,0.433584,-4.690096,-6.858275,-4.613413,3.286194,9.812763,-2.516649,-7.823194,-1.415394,4.028109,-5.317922,-0.210029,0.917665,7.079273,4.447239,-3.152873,6.689747,-2.945078,3.128034,-8.070295,2.277702,-1.574321,6.126823,1.699731,-9.358077,5.271569,-3.661029,5.246812,4.815999,0.863457,4.728378,-0.699089,4.757630,3.508025,6.785756,2.234846,7.668502,-7.721132,7.100072,8.725718,-9.393569,-6.154370,-1.324097,-8.814603,-3.363966,3.254487,8.851643,-7.750665,-6.792416,-0.057799,-7.763875,-7.268514,9.693055,-8.013022,-4.211075,-4.776689,7.749711,-1.656554,4.320279,5.755321,-9.289240,0.920451,-9.330244,-8.437524,5.904624,-9.464665,3.467301,-6.544261,3.152064,0.873381,-0.567620,3.489884,-5.147510,7.209158,-3.125293,-2.917666,1.032381,4.133983,2.774375,-7.072400,-2.394531,-4.024760,-0.655450,-5.704221,-0.901962,2.251760,-0.203984,-6.698636,-2.609231,-9.275881,-2.062363,-0.166331,-6.641846,-0.080673,2.474721,8.619798,7.587465,2.173111,-6.865375,-1.974706,3.204265,3.761410,-6.395989,8.909248,7.663444,2.453189,-9.287719,-5.316573,4.137015,-8.737519,4.675086,-0.871679,-3.049350,-8.918901,-8.384891,4.222750,1.090991,2.549294,-5.102948,-3.209173,-9.016561,1.602630,0.392493,5.323115,-2.309574,-9.645251,8.801596,2.563874,-0.326312,-7.114893,-6.311379,3.921155,-8.669574,5.045270,3.481145,1.385591,9.029577,-9.621069,-2.396128,-8.982116,9.969961,-0.285887,9.493086]], dtype = "float32")#candidate|5447|(1, 1386)|const|float32
call_5446 = relay.TupleGetItem(func_5257_call(relay.reshape(const_5447.astype('float32'), [11, 9, 14])), 0)
call_5448 = relay.TupleGetItem(func_5259_call(relay.reshape(const_5447.astype('float32'), [11, 9, 14])), 0)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
var_5459 = relay.var("var_5459", dtype = "int8", shape = (2, 784))#candidate|5459|(2, 784)|var|int8
call_5458 = func_4770_call(relay.reshape(var_5459.astype('int8'), [14, 8, 14]))
call_5460 = func_4770_call(relay.reshape(var_5459.astype('int8'), [14, 8, 14]))
uop_5462 = relay.log2(var_5438.astype('float64')) # shape=(11, 12, 16)
func_2966_call = mod.get_global_var('func_2966')
func_2967_call = mutated_mod.get_global_var('func_2967')
call_5470 = func_2966_call()
call_5471 = func_2966_call()
uop_5476 = relay.exp(call_5446.astype('float64')) # shape=(11, 9, 14)
uop_5478 = relay.exp(call_5448.astype('float64')) # shape=(11, 9, 14)
output = relay.Tuple([bop_5440,const_5447,call_5458,var_5459,uop_5462,call_5470,uop_5476,])
output2 = relay.Tuple([bop_5440,const_5447,call_5460,var_5459,uop_5462,call_5471,uop_5478,])
func_5479 = relay.Function([var_5438,var_5439,var_5459,], output)
mod['func_5479'] = func_5479
mod = relay.transform.InferType()(mod)
var_5480 = relay.var("var_5480", dtype = "float64", shape = (11, 12, 16))#candidate|5480|(11, 12, 16)|var|float64
var_5481 = relay.var("var_5481", dtype = "float64", shape = (11, 12, 16))#candidate|5481|(11, 12, 16)|var|float64
var_5482 = relay.var("var_5482", dtype = "int8", shape = (2, 784))#candidate|5482|(2, 784)|var|int8
output = func_5479(var_5480,var_5481,var_5482,)
func_5483 = relay.Function([var_5480,var_5481,var_5482,], output)
mutated_mod['func_5483'] = func_5483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1425_call = mod.get_global_var('func_1425')
func_1427_call = mutated_mod.get_global_var('func_1427')
call_5487 = relay.TupleGetItem(func_1425_call(), 2)
call_5488 = relay.TupleGetItem(func_1427_call(), 2)
output = relay.Tuple([call_5487,])
output2 = relay.Tuple([call_5488,])
func_5506 = relay.Function([], output)
mod['func_5506'] = func_5506
mod = relay.transform.InferType()(mod)
mutated_mod['func_5506'] = func_5506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5506_call = mutated_mod.get_global_var('func_5506')
call_5507 = func_5506_call()
output = call_5507
func_5508 = relay.Function([], output)
mutated_mod['func_5508'] = func_5508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5198_call = mod.get_global_var('func_5198')
func_5199_call = mutated_mod.get_global_var('func_5199')
call_5515 = func_5198_call()
call_5516 = func_5198_call()
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_5530 = relay.TupleGetItem(func_1015_call(), 1)
call_5531 = relay.TupleGetItem(func_1016_call(), 1)
bop_5535 = relay.floor_divide(call_5515.astype('float64'), relay.reshape(call_5530.astype('float64'), relay.shape_of(call_5515))) # shape=(11, 1, 14)
bop_5538 = relay.floor_divide(call_5516.astype('float64'), relay.reshape(call_5531.astype('float64'), relay.shape_of(call_5516))) # shape=(11, 1, 14)
func_4848_call = mod.get_global_var('func_4848')
func_4849_call = mutated_mod.get_global_var('func_4849')
call_5540 = func_4848_call()
call_5541 = func_4848_call()
output = relay.Tuple([bop_5535,call_5540,])
output2 = relay.Tuple([bop_5538,call_5541,])
func_5543 = relay.Function([], output)
mod['func_5543'] = func_5543
mod = relay.transform.InferType()(mod)
output = func_5543()
func_5544 = relay.Function([], output)
mutated_mod['func_5544'] = func_5544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5198_call = mod.get_global_var('func_5198')
func_5199_call = mutated_mod.get_global_var('func_5199')
call_5549 = func_5198_call()
call_5550 = func_5198_call()
const_5551 = relay.const([[[2.080878,2.900387,2.410477,3.046064,-6.877271,-9.250287,-4.273344,-2.117430,8.238843,-7.652052,2.119103,-2.481669,-4.660514,2.360710],[0.092929,-0.248034,5.533475,4.744811,8.755991,2.119830,-5.942584,8.028390,4.070320,-9.635056,0.474478,-4.313987,6.523241,-1.977773],[-7.509688,9.051968,6.805286,-8.513096,1.443562,4.744808,-1.043134,3.429197,-5.957177,-3.201541,-9.883972,-7.005252,1.651588,-5.857229],[7.620537,-4.103034,-8.384883,-5.189197,0.096302,-9.931166,-7.257694,3.282122,8.302318,1.752146,-8.279597,9.912197,-2.190153,-7.318473],[-0.324749,8.557484,3.019590,-8.102635,8.554149,0.464067,7.833511,4.181383,3.222895,4.701564,7.899950,-6.501950,-3.340302,-8.885509],[-8.072898,-4.417105,-8.471904,-1.959268,4.208681,6.346580,9.793452,1.273426,0.794530,-8.889051,-2.526734,6.219039,-0.306506,0.074340],[8.726070,-4.897191,-0.399951,-3.026446,-6.204707,-3.232582,9.914793,-2.475331,6.515711,-1.538112,-4.195447,4.329642,-6.382049,1.880437],[5.544391,9.354566,-6.831013,-7.571056,-7.003462,2.543991,1.677919,-3.128264,-5.231519,-9.315765,-4.735023,-6.146358,7.104199,6.642038]],[[-5.413144,1.190205,9.154566,-9.078942,-8.181773,-6.869306,7.162425,5.996796,-3.167510,-5.359608,-9.381638,-2.575536,0.936800,9.575386],[-7.058312,-4.124409,4.686135,-6.423723,-7.817548,1.395586,9.394553,4.365373,9.926266,-9.171426,-1.508698,-9.882298,7.088137,0.778878],[1.840235,8.196507,-2.428570,-0.315875,1.475386,-8.734537,4.260712,-4.458502,-1.715864,-0.354550,-8.639527,0.700452,9.712161,4.291010],[-1.479311,3.384545,-5.704711,0.231742,-9.413641,-2.060254,9.413220,7.195200,-8.380226,2.872023,3.112458,3.315748,-8.623654,-3.400744],[-2.488796,-8.958357,-3.145486,2.623045,1.018169,9.970964,-9.968852,7.316893,2.919210,5.590455,9.121476,-5.460883,-5.570202,-7.244934],[-1.618898,-8.107527,6.516471,6.677817,-9.575747,-8.650724,7.711066,2.784533,6.449568,4.300391,3.308468,8.736856,-4.963287,9.388847],[6.664615,7.907000,-8.126902,-7.612074,6.266822,8.072452,-6.169518,6.117768,-5.121131,-5.019043,5.026964,-6.882335,-8.046633,9.133470],[9.127884,3.647973,8.684780,-6.844207,-0.173998,0.522839,-1.201435,7.589124,-3.690195,-1.084628,1.537724,-5.642277,8.707689,9.857362]],[[-4.804950,-8.854665,7.666977,-4.616547,-5.375960,-8.838173,-6.123161,-3.189124,-7.599263,5.620704,-7.156123,2.629847,-8.781578,0.599823],[-9.049411,4.510397,6.592038,-7.683873,5.803943,6.829470,9.528109,-9.125738,2.241955,-1.961583,-5.042840,-6.227420,-4.841773,-0.781833],[-2.761303,-4.836747,-8.497997,7.002748,2.822088,-7.284383,8.269877,-7.367008,5.721707,-0.838131,-5.172992,0.652658,-4.654081,8.885642],[9.097400,-9.648273,9.861837,2.799019,-7.344924,-6.059872,-3.377352,1.240188,-3.121648,2.731289,-9.393519,7.770605,-0.637349,-5.597155],[-0.823017,3.912992,6.550185,3.703760,-1.101495,9.040274,-7.308006,-8.963293,-6.497574,-9.180202,-0.121371,1.226030,4.878468,7.007964],[7.262772,-9.197970,5.705545,0.275186,6.911898,-3.901304,4.983403,2.975744,7.952936,7.922005,3.797286,-5.442809,2.823312,-4.167606],[-1.736033,-2.280930,4.989115,-2.803735,8.567360,-0.176221,-8.101411,-9.645726,-2.443110,0.167352,-1.711393,4.453381,-1.817462,3.218865],[4.037036,-4.687923,2.968821,6.731330,-1.838606,3.021162,-1.185921,-4.556458,-5.367520,-5.269695,-6.876355,-8.038268,-6.950566,-3.130077]],[[-9.036595,-9.574568,-6.689010,6.714130,-5.911391,-2.778140,-5.925999,-3.441523,2.069146,-5.973004,7.980210,-1.637270,-5.593761,-8.991614],[8.571384,-7.523674,-3.148259,3.602612,6.898789,-2.780267,-7.318041,-2.204146,2.779243,4.665052,-0.496020,-9.694067,-4.732154,2.125449],[-2.013623,-5.606421,4.721692,6.293909,6.487056,-1.815632,3.957704,-8.325546,9.083896,3.559315,6.481099,-5.460966,-9.873035,-3.845403],[6.385834,8.561696,7.885910,1.503419,-4.602981,7.026244,-5.428074,7.406661,-9.220979,5.483652,-1.648590,-1.411648,6.655105,1.693272],[-7.304439,-3.202697,-0.881628,3.939043,0.454650,-7.155589,3.626637,-8.271220,7.494333,4.728164,5.748061,9.776283,1.551301,-2.788330],[-1.025382,-1.462591,1.368235,1.329565,5.329385,5.954809,5.636216,-1.963778,5.221176,-2.327424,-9.853543,3.216709,-1.454781,-6.864157],[-3.562618,-8.481600,-8.104070,6.831519,-7.790083,8.115061,9.714039,-6.356695,-6.237808,7.100414,6.770501,-8.637895,-2.274418,-1.013438],[9.196679,-7.978103,5.924759,-7.904035,-6.952362,6.326199,-7.544810,-8.633883,3.545002,3.522445,5.212052,-8.296389,-8.043358,9.454262]],[[-2.217266,-0.901374,-8.029277,2.641071,5.989149,3.858857,-4.204437,-7.246424,-1.253793,-5.865585,-8.173850,6.834208,1.420644,-7.250114],[1.107431,-1.223031,3.248211,8.083663,5.118003,6.128264,-9.139124,-0.262151,0.764423,-2.776929,1.914240,-9.132811,-3.619412,-4.484943],[7.784785,8.771540,-9.124825,-2.102572,-7.553488,2.311933,-0.435639,9.350996,1.471358,9.794834,-3.090398,-8.099357,5.640376,9.432672],[7.004109,2.419006,0.395246,6.607218,-2.683842,2.247025,7.133303,-5.901135,-2.875720,-8.084035,-3.504724,-5.025597,0.636385,-2.139127],[4.364872,-8.507852,1.493328,0.243294,4.003970,-8.164424,-6.422516,-8.881508,-2.894761,-1.964287,-7.364030,7.051990,-8.661604,-4.334196],[-8.494520,-6.877960,-4.421100,-0.763175,-8.054386,-0.282660,-7.462701,0.595402,1.644334,-0.293221,9.142525,-2.773051,-8.991116,-5.421419],[3.442025,-4.407398,9.807830,-4.999949,-2.683957,-2.016355,-4.572589,-7.283895,9.186946,-9.360975,6.921391,0.362505,8.635998,3.312584],[6.243527,-9.697577,-1.221513,-9.580408,-3.536758,9.625152,-8.157092,4.874719,1.390053,1.637473,-3.018441,7.741181,3.977023,-3.592760]],[[-2.277707,-1.052083,7.657175,-3.479523,9.877113,5.607101,3.421465,-0.406235,-5.026460,4.775754,6.587483,1.533205,-1.117415,-4.779523],[1.227008,-3.672969,-3.772880,3.806905,4.286952,0.923327,-2.895474,-6.935965,9.824184,4.741180,1.289542,5.286001,-0.159015,-6.463695],[6.616387,-3.037816,9.107476,-4.424646,7.798735,9.687285,-1.643579,2.261214,0.060950,-5.122517,6.597754,4.466752,-5.167222,1.414814],[9.048385,5.589880,-4.323011,1.041041,-8.876725,8.072345,5.723887,6.202843,0.018799,-5.069215,-2.256014,-4.636226,1.880606,-8.909348],[-0.038907,-4.503549,2.720363,5.508421,1.459387,1.473850,-5.397687,7.702588,9.538091,1.510653,5.961725,-7.722623,5.761835,7.430253],[-1.188728,-9.520652,-9.536561,-1.471897,7.848486,3.689065,-8.778373,-0.168898,-6.730165,-9.420277,-6.272735,-0.185235,8.964431,-0.796350],[3.909559,6.869186,4.124458,7.371226,-4.755413,-1.257601,9.704824,-1.162090,-6.964488,-3.966728,-4.218368,5.127446,7.415482,0.937819],[-6.726721,5.777889,2.563435,8.537447,-0.570863,-2.079805,-4.556583,-1.725681,6.441681,4.489472,-6.761215,-0.274059,-0.580453,3.655121]],[[8.806188,-3.301686,-2.841172,-6.049993,1.244779,5.075029,-6.961371,-7.092719,-2.212189,-3.014012,-3.174773,9.468880,4.747026,1.646400],[0.952565,7.989305,7.560369,-7.734275,5.667988,-4.212530,-5.963603,0.979241,5.910268,0.321387,-5.039187,0.946725,5.282748,3.090695],[-7.012405,-6.945830,-7.455152,0.205073,-0.248896,4.157301,-5.643367,-6.415300,4.662217,1.893746,4.358653,-1.177487,-2.200315,-7.094878],[7.147352,-1.581343,1.323806,0.426288,7.451488,6.903982,0.975736,4.907024,-6.594095,-6.880427,2.156878,0.318188,8.445920,5.669998],[4.768629,3.117964,7.241275,5.346097,8.412523,-1.434241,0.851667,-2.974160,8.939805,-9.285649,9.398495,4.752169,-7.385185,9.504787],[2.561635,8.845973,0.596709,2.366219,-1.328525,6.415040,7.530165,-2.964208,0.283312,9.292198,8.590001,5.340668,4.642661,4.134700],[4.295444,3.800071,1.171137,9.854174,0.855325,-1.187307,5.794454,0.778131,8.762193,8.301169,-0.648656,1.690095,-2.899080,-8.037715],[-3.267775,7.649669,2.770001,-6.421171,0.514913,5.496277,-0.654320,9.293061,4.373792,-5.840217,-1.821172,7.685334,3.879903,-7.511119]],[[5.961053,4.438666,2.885810,2.260142,9.262875,2.823742,-3.597125,6.074671,-7.235972,-2.542497,-1.358367,1.810072,2.851846,6.768953],[2.464915,-5.861521,5.513790,-7.405621,9.288090,8.359291,7.476209,6.661723,2.459199,-9.833740,8.830137,9.164628,-3.189762,0.266385],[9.728205,-4.912385,-8.391508,-5.102465,-9.299863,-1.728274,-0.186045,-3.026557,4.088062,4.399678,-5.415533,-8.566537,4.959945,4.304316],[-9.300548,7.955104,-4.416935,4.604728,-3.704901,-2.367505,-7.360912,-1.470144,-4.957462,2.365739,3.297990,-0.177935,-0.201890,1.141285],[-6.112346,0.322241,4.265572,-1.578399,-3.079426,3.447992,2.505478,9.781896,-9.296653,9.744711,-8.926667,-1.851724,1.393311,-8.769086],[-1.327575,6.522025,-6.817366,3.445261,4.187798,5.348011,8.373819,9.098502,-0.228270,9.220693,-5.019401,0.705781,8.575689,-1.079175],[-5.725940,-0.017605,9.338843,0.397631,7.716728,1.642066,5.094571,-5.886604,9.395412,1.193565,3.145012,2.819839,6.523022,-1.178187],[-6.935874,-4.121634,9.007616,6.568272,-4.702176,7.495710,-8.653626,7.269506,1.699490,-6.130795,4.146561,3.390757,-3.797068,-4.119932]],[[0.107616,-2.125623,-3.436373,0.967088,-3.008793,-4.925224,2.218988,-5.136085,-0.426043,3.031962,7.149873,4.350042,-0.115108,9.820638],[2.244693,-3.528360,2.041660,-8.133600,2.021066,3.608965,7.654886,9.146258,6.636577,-3.657683,6.522501,-4.531073,8.360883,7.924910],[-0.463815,4.350844,-3.616003,-6.092525,-8.092838,7.022812,-3.926235,7.555898,-5.493881,9.576147,-0.716770,-6.304116,5.998981,5.222263],[-8.690208,-5.844972,6.621047,-7.154797,-0.825382,9.047828,0.988313,-3.312224,-8.612258,5.888195,-1.344352,-0.912098,-8.569443,-5.553167],[1.480805,3.796431,-7.659630,-6.981780,1.485224,-7.759387,-5.429191,-1.142702,-3.933238,9.079920,3.828144,-7.882335,6.941920,-3.352836],[3.488871,-0.448609,-6.648696,-3.085675,6.834199,4.381536,4.948255,-0.122471,8.821090,4.600443,-4.355767,-7.091584,-7.457591,8.419256],[-6.501057,1.930685,8.951122,-9.999121,8.661812,-2.107826,-9.477531,5.717055,3.129680,6.639258,5.795809,3.534982,7.372544,3.584279],[-2.034705,-3.925119,-6.171561,-5.551104,0.888845,-7.890532,8.953133,1.390681,-6.711325,8.724287,8.180903,-1.333753,5.359540,-5.467605]],[[-3.858271,-5.861453,-8.952939,4.663879,3.495472,-1.537674,-2.235246,9.954073,-8.480106,1.847482,-5.572734,-2.058994,3.525635,-3.328147],[-2.817241,-0.397748,-4.913938,8.603383,8.589545,8.124042,-1.036973,9.472549,-5.239309,-9.697779,2.930781,9.926957,-6.350196,4.100706],[0.835429,3.350725,-3.904439,-1.514946,-5.976329,-1.755283,-2.180887,-2.883808,1.215571,6.596207,3.276359,-9.811717,-7.892557,-4.316498],[-1.566903,-9.393143,4.281876,3.229562,0.209748,-7.041782,-1.525220,6.657607,-9.084529,8.208915,3.820660,-5.478935,2.489394,-3.531716],[-6.067197,-8.532243,-3.384760,-5.781493,-7.600706,-3.991814,7.589412,-6.310165,6.098848,-6.957887,5.946738,5.069577,0.266823,2.897918],[7.627028,-5.484002,-6.272852,-5.470300,1.343578,-3.332744,-5.627110,-7.163930,7.909777,8.539988,-4.863512,8.248640,-2.280085,8.411323],[-3.569447,-9.093510,-5.724549,7.005314,7.187792,6.787852,2.597971,8.046079,-9.485968,4.420020,-7.207925,-7.459399,1.781725,-4.382002],[8.492280,9.161637,0.642910,9.024070,-4.785148,-5.019507,-2.543705,-0.522651,-8.217427,8.765758,7.712872,-5.811635,-9.917746,4.222724]],[[-8.377610,0.511463,9.934845,5.303498,-7.050412,-7.737788,-4.340537,-8.900253,-7.408971,-4.117746,-5.814933,-2.037247,-5.912808,6.632064],[4.047341,-3.678407,4.196914,2.328528,-0.204623,9.886801,7.364277,4.306414,-8.309072,-1.654362,4.773505,2.344120,7.778948,9.448423],[7.276463,-9.109010,4.676077,-6.424712,-3.523525,9.521353,7.552664,8.939674,-8.611575,-5.986798,-9.187035,-3.188976,5.431392,-8.915782],[6.284111,-5.756061,-7.434946,5.442254,-1.424701,-0.996780,-2.630109,2.075578,-9.508273,-4.278957,-0.731165,-9.214029,-3.120242,-5.445413],[-6.641302,-6.752854,-1.165141,-7.385091,4.604995,8.110435,-6.985672,-7.093082,7.037906,-5.943450,-2.007855,6.762376,5.795926,4.884485],[-7.099175,5.126328,-3.702730,-3.427822,-7.750231,-1.950177,-6.755559,7.501831,0.008083,5.368479,-8.176287,9.259667,2.791213,1.723358],[-1.360993,-7.662198,-5.419447,1.677775,9.403376,5.618612,9.730803,2.274365,0.437529,-1.040531,-4.001910,-5.781198,4.641214,5.384887],[-7.895007,2.188872,7.741334,4.027890,3.895675,0.442699,-7.237458,-9.411653,-5.552098,7.000493,2.304706,-4.072679,-7.042065,-1.165501]]], dtype = "float32")#candidate|5551|(11, 8, 14)|const|float32
bop_5552 = relay.greater_equal(call_5549.astype('bool'), const_5551.astype('bool')) # shape=(11, 8, 14)
bop_5555 = relay.greater_equal(call_5550.astype('bool'), const_5551.astype('bool')) # shape=(11, 8, 14)
func_4708_call = mod.get_global_var('func_4708')
func_4712_call = mutated_mod.get_global_var('func_4712')
var_5560 = relay.var("var_5560", dtype = "float32", shape = (2464,))#candidate|5560|(2464,)|var|float32
call_5559 = relay.TupleGetItem(func_4708_call(relay.reshape(var_5560.astype('float32'), [11, 16, 14]), relay.reshape(var_5560.astype('float64'), [11, 16, 14]), ), 1)
call_5561 = relay.TupleGetItem(func_4712_call(relay.reshape(var_5560.astype('float32'), [11, 16, 14]), relay.reshape(var_5560.astype('float64'), [11, 16, 14]), ), 1)
func_2888_call = mod.get_global_var('func_2888')
func_2890_call = mutated_mod.get_global_var('func_2890')
call_5572 = relay.TupleGetItem(func_2888_call(), 2)
call_5573 = relay.TupleGetItem(func_2890_call(), 2)
func_5160_call = mod.get_global_var('func_5160')
func_5161_call = mutated_mod.get_global_var('func_5161')
call_5576 = relay.TupleGetItem(func_5160_call(), 0)
call_5577 = relay.TupleGetItem(func_5161_call(), 0)
output = relay.Tuple([bop_5552,call_5559,var_5560,call_5572,call_5576,])
output2 = relay.Tuple([bop_5555,call_5561,var_5560,call_5573,call_5577,])
func_5579 = relay.Function([var_5560,], output)
mod['func_5579'] = func_5579
mod = relay.transform.InferType()(mod)
mutated_mod['func_5579'] = func_5579
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5580 = relay.var("var_5580", dtype = "float32", shape = (2464,))#candidate|5580|(2464,)|var|float32
func_5579_call = mutated_mod.get_global_var('func_5579')
call_5581 = func_5579_call(var_5580)
output = call_5581
func_5582 = relay.Function([var_5580], output)
mutated_mod['func_5582'] = func_5582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4542_call = mod.get_global_var('func_4542')
func_4543_call = mutated_mod.get_global_var('func_4543')
call_5595 = relay.TupleGetItem(func_4542_call(), 1)
call_5596 = relay.TupleGetItem(func_4543_call(), 1)
output = relay.Tuple([call_5595,])
output2 = relay.Tuple([call_5596,])
func_5599 = relay.Function([], output)
mod['func_5599'] = func_5599
mod = relay.transform.InferType()(mod)
mutated_mod['func_5599'] = func_5599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5599_call = mutated_mod.get_global_var('func_5599')
call_5600 = func_5599_call()
output = call_5600
func_5601 = relay.Function([], output)
mutated_mod['func_5601'] = func_5601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_220_call = mod.get_global_var('func_220')
func_221_call = mutated_mod.get_global_var('func_221')
call_5619 = relay.TupleGetItem(func_220_call(), 0)
call_5620 = relay.TupleGetItem(func_221_call(), 0)
output = relay.Tuple([call_5619,])
output2 = relay.Tuple([call_5620,])
func_5647 = relay.Function([], output)
mod['func_5647'] = func_5647
mod = relay.transform.InferType()(mod)
output = func_5647()
func_5648 = relay.Function([], output)
mutated_mod['func_5648'] = func_5648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5599_call = mod.get_global_var('func_5599')
func_5601_call = mutated_mod.get_global_var('func_5601')
call_5869 = relay.TupleGetItem(func_5599_call(), 0)
call_5870 = relay.TupleGetItem(func_5601_call(), 0)
func_5599_call = mod.get_global_var('func_5599')
func_5601_call = mutated_mod.get_global_var('func_5601')
call_5874 = relay.TupleGetItem(func_5599_call(), 0)
call_5875 = relay.TupleGetItem(func_5601_call(), 0)
output = relay.Tuple([call_5869,call_5874,])
output2 = relay.Tuple([call_5870,call_5875,])
func_5879 = relay.Function([], output)
mod['func_5879'] = func_5879
mod = relay.transform.InferType()(mod)
mutated_mod['func_5879'] = func_5879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5879_call = mutated_mod.get_global_var('func_5879')
call_5880 = func_5879_call()
output = call_5880
func_5881 = relay.Function([], output)
mutated_mod['func_5881'] = func_5881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2200_call = mod.get_global_var('func_2200')
func_2201_call = mutated_mod.get_global_var('func_2201')
call_5917 = relay.TupleGetItem(func_2200_call(), 0)
call_5918 = relay.TupleGetItem(func_2201_call(), 0)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_5920 = relay.TupleGetItem(func_1015_call(), 0)
call_5921 = relay.TupleGetItem(func_1016_call(), 0)
output = relay.Tuple([call_5917,call_5920,])
output2 = relay.Tuple([call_5918,call_5921,])
func_5923 = relay.Function([], output)
mod['func_5923'] = func_5923
mod = relay.transform.InferType()(mod)
output = func_5923()
func_5924 = relay.Function([], output)
mutated_mod['func_5924'] = func_5924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4848_call = mod.get_global_var('func_4848')
func_4849_call = mutated_mod.get_global_var('func_4849')
call_5953 = func_4848_call()
call_5954 = func_4848_call()
func_1177_call = mod.get_global_var('func_1177')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_5960 = relay.TupleGetItem(func_1177_call(), 1)
call_5961 = relay.TupleGetItem(func_1178_call(), 1)
output = relay.Tuple([call_5953,call_5960,])
output2 = relay.Tuple([call_5954,call_5961,])
func_5966 = relay.Function([], output)
mod['func_5966'] = func_5966
mod = relay.transform.InferType()(mod)
output = func_5966()
func_5967 = relay.Function([], output)
mutated_mod['func_5967'] = func_5967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mod.get_global_var('func_2698')
func_2699_call = mutated_mod.get_global_var('func_2699')
call_5970 = relay.TupleGetItem(func_2698_call(), 0)
call_5971 = relay.TupleGetItem(func_2699_call(), 0)
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_6008 = relay.var("var_6008", dtype = "float64", shape = ())#candidate|6008|()|var|float64
var_6009 = relay.var("var_6009", dtype = "float64", shape = (5,))#candidate|6009|(5,)|var|float64
call_6007 = relay.TupleGetItem(func_47_call(relay.reshape(var_6008.astype('float64'), []), relay.reshape(var_6009.astype('float64'), [5, 1, 1]), ), 0)
call_6010 = relay.TupleGetItem(func_50_call(relay.reshape(var_6008.astype('float64'), []), relay.reshape(var_6009.astype('float64'), [5, 1, 1]), ), 0)
uop_6031 = relay.rsqrt(call_6007.astype('float32')) # shape=(5, 1, 1)
uop_6033 = relay.rsqrt(call_6010.astype('float32')) # shape=(5, 1, 1)
func_614_call = mod.get_global_var('func_614')
func_615_call = mutated_mod.get_global_var('func_615')
call_6066 = relay.TupleGetItem(func_614_call(), 0)
call_6067 = relay.TupleGetItem(func_615_call(), 0)
func_3466_call = mod.get_global_var('func_3466')
func_3469_call = mutated_mod.get_global_var('func_3469')
var_6075 = relay.var("var_6075", dtype = "uint16", shape = (1120,))#candidate|6075|(1120,)|var|uint16
call_6074 = relay.TupleGetItem(func_3466_call(relay.reshape(var_6075.astype('uint16'), [14, 8, 10])), 0)
call_6076 = relay.TupleGetItem(func_3469_call(relay.reshape(var_6075.astype('uint16'), [14, 8, 10])), 0)
func_926_call = mod.get_global_var('func_926')
func_933_call = mutated_mod.get_global_var('func_933')
var_6078 = relay.var("var_6078", dtype = "float64", shape = (156,))#candidate|6078|(156,)|var|float64
call_6077 = relay.TupleGetItem(func_926_call(relay.reshape(var_6078.astype('float64'), [3, 13, 4]), relay.reshape(var_6078.astype('float64'), [3, 13, 4]), relay.reshape(var_6008.astype('float64'), []), relay.reshape(uop_6031.astype('float64'), [5,]), relay.reshape(var_6078.astype('float32'), [3, 13, 4]), ), 2)
call_6079 = relay.TupleGetItem(func_933_call(relay.reshape(var_6078.astype('float64'), [3, 13, 4]), relay.reshape(var_6078.astype('float64'), [3, 13, 4]), relay.reshape(var_6008.astype('float64'), []), relay.reshape(uop_6031.astype('float64'), [5,]), relay.reshape(var_6078.astype('float32'), [3, 13, 4]), ), 2)
bop_6086 = relay.greater(uop_6031.astype('bool'), var_6075.astype('bool')) # shape=(5, 1, 1120)
bop_6089 = relay.greater(uop_6033.astype('bool'), var_6075.astype('bool')) # shape=(5, 1, 1120)
func_5543_call = mod.get_global_var('func_5543')
func_5544_call = mutated_mod.get_global_var('func_5544')
call_6103 = relay.TupleGetItem(func_5543_call(), 0)
call_6104 = relay.TupleGetItem(func_5544_call(), 0)
bop_6107 = relay.not_equal(bop_6086.astype('bool'), var_6008.astype('bool')) # shape=(5, 1, 1120)
bop_6110 = relay.not_equal(bop_6089.astype('bool'), var_6008.astype('bool')) # shape=(5, 1, 1120)
func_2652_call = mod.get_global_var('func_2652')
func_2655_call = mutated_mod.get_global_var('func_2655')
var_6113 = relay.var("var_6113", dtype = "float32", shape = (308,))#candidate|6113|(308,)|var|float32
const_6114 = relay.const([False,False,True,True,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True], dtype = "bool")#candidate|6114|(64,)|const|bool
call_6112 = relay.TupleGetItem(func_2652_call(relay.reshape(var_6113.astype('float32'), [11, 2, 14]), relay.reshape(const_6114.astype('bool'), [64,]), ), 3)
call_6115 = relay.TupleGetItem(func_2655_call(relay.reshape(var_6113.astype('float32'), [11, 2, 14]), relay.reshape(const_6114.astype('bool'), [64,]), ), 3)
bop_6116 = relay.mod(uop_6031.astype('float64'), var_6075.astype('float64')) # shape=(5, 1, 1120)
bop_6119 = relay.mod(uop_6033.astype('float64'), var_6075.astype('float64')) # shape=(5, 1, 1120)
output = relay.Tuple([call_5970,var_6009,call_6066,call_6074,call_6077,var_6078,call_6103,bop_6107,call_6112,var_6113,const_6114,bop_6116,])
output2 = relay.Tuple([call_5971,var_6009,call_6067,call_6076,call_6079,var_6078,call_6104,bop_6110,call_6115,var_6113,const_6114,bop_6119,])
func_6122 = relay.Function([var_6008,var_6009,var_6075,var_6078,var_6113,], output)
mod['func_6122'] = func_6122
mod = relay.transform.InferType()(mod)
mutated_mod['func_6122'] = func_6122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6122_call = mutated_mod.get_global_var('func_6122')
var_6124 = relay.var("var_6124", dtype = "float64", shape = ())#candidate|6124|()|var|float64
var_6125 = relay.var("var_6125", dtype = "float64", shape = (5,))#candidate|6125|(5,)|var|float64
var_6126 = relay.var("var_6126", dtype = "uint16", shape = (1120,))#candidate|6126|(1120,)|var|uint16
var_6127 = relay.var("var_6127", dtype = "float64", shape = (156,))#candidate|6127|(156,)|var|float64
var_6128 = relay.var("var_6128", dtype = "float32", shape = (308,))#candidate|6128|(308,)|var|float32
call_6123 = func_6122_call(var_6124,var_6125,var_6126,var_6127,var_6128,)
output = call_6123
func_6129 = relay.Function([var_6124,var_6125,var_6126,var_6127,var_6128,], output)
mutated_mod['func_6129'] = func_6129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_6159 = func_2601_call()
call_6160 = func_2601_call()
func_47_call = mod.get_global_var('func_47')
func_50_call = mutated_mod.get_global_var('func_50')
var_6179 = relay.var("var_6179", dtype = "float64", shape = ())#candidate|6179|()|var|float64
const_6180 = relay.const([[3.456899],[8.954889],[-2.189208],[1.639477],[8.159064]], dtype = "float64")#candidate|6180|(5, 1)|const|float64
call_6178 = relay.TupleGetItem(func_47_call(relay.reshape(var_6179.astype('float64'), []), relay.reshape(const_6180.astype('float64'), [5, 1, 1]), ), 0)
call_6181 = relay.TupleGetItem(func_50_call(relay.reshape(var_6179.astype('float64'), []), relay.reshape(const_6180.astype('float64'), [5, 1, 1]), ), 0)
func_5599_call = mod.get_global_var('func_5599')
func_5601_call = mutated_mod.get_global_var('func_5601')
call_6183 = relay.TupleGetItem(func_5599_call(), 0)
call_6184 = relay.TupleGetItem(func_5601_call(), 0)
func_4124_call = mod.get_global_var('func_4124')
func_4126_call = mutated_mod.get_global_var('func_4126')
call_6188 = func_4124_call()
call_6189 = func_4124_call()
output = relay.Tuple([call_6159,call_6178,var_6179,const_6180,call_6183,call_6188,])
output2 = relay.Tuple([call_6160,call_6181,var_6179,const_6180,call_6184,call_6189,])
func_6204 = relay.Function([var_6179,], output)
mod['func_6204'] = func_6204
mod = relay.transform.InferType()(mod)
var_6205 = relay.var("var_6205", dtype = "float64", shape = ())#candidate|6205|()|var|float64
output = func_6204(var_6205)
func_6206 = relay.Function([var_6205], output)
mutated_mod['func_6206'] = func_6206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5198_call = mod.get_global_var('func_5198')
func_5199_call = mutated_mod.get_global_var('func_5199')
call_6215 = func_5198_call()
call_6216 = func_5198_call()
output = relay.Tuple([call_6215,])
output2 = relay.Tuple([call_6216,])
func_6219 = relay.Function([], output)
mod['func_6219'] = func_6219
mod = relay.transform.InferType()(mod)
output = func_6219()
func_6220 = relay.Function([], output)
mutated_mod['func_6220'] = func_6220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2555_call = mod.get_global_var('func_2555')
func_2556_call = mutated_mod.get_global_var('func_2556')
call_6229 = func_2555_call()
call_6230 = func_2555_call()
output = relay.Tuple([call_6229,])
output2 = relay.Tuple([call_6230,])
func_6245 = relay.Function([], output)
mod['func_6245'] = func_6245
mod = relay.transform.InferType()(mod)
output = func_6245()
func_6246 = relay.Function([], output)
mutated_mod['func_6246'] = func_6246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_220_call = mod.get_global_var('func_220')
func_221_call = mutated_mod.get_global_var('func_221')
call_6277 = relay.TupleGetItem(func_220_call(), 1)
call_6278 = relay.TupleGetItem(func_221_call(), 1)
output = call_6277
output2 = call_6278
func_6292 = relay.Function([], output)
mod['func_6292'] = func_6292
mod = relay.transform.InferType()(mod)
mutated_mod['func_6292'] = func_6292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6292_call = mutated_mod.get_global_var('func_6292')
call_6293 = func_6292_call()
output = call_6293
func_6294 = relay.Function([], output)
mutated_mod['func_6294'] = func_6294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6349 = relay.var("var_6349", dtype = "float32", shape = (7, 11, 12))#candidate|6349|(7, 11, 12)|var|float32
uop_6350 = relay.cos(var_6349.astype('float32')) # shape=(7, 11, 12)
uop_6361 = relay.log10(var_6349.astype('float64')) # shape=(7, 11, 12)
func_4468_call = mod.get_global_var('func_4468')
func_4469_call = mutated_mod.get_global_var('func_4469')
call_6364 = func_4468_call()
call_6365 = func_4468_call()
output = relay.Tuple([uop_6350,uop_6361,call_6364,])
output2 = relay.Tuple([uop_6350,uop_6361,call_6365,])
func_6370 = relay.Function([var_6349,], output)
mod['func_6370'] = func_6370
mod = relay.transform.InferType()(mod)
var_6371 = relay.var("var_6371", dtype = "float32", shape = (7, 11, 12))#candidate|6371|(7, 11, 12)|var|float32
output = func_6370(var_6371)
func_6372 = relay.Function([var_6371], output)
mutated_mod['func_6372'] = func_6372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2966_call = mod.get_global_var('func_2966')
func_2967_call = mutated_mod.get_global_var('func_2967')
call_6377 = func_2966_call()
call_6378 = func_2966_call()
output = call_6377
output2 = call_6378
func_6379 = relay.Function([], output)
mod['func_6379'] = func_6379
mod = relay.transform.InferType()(mod)
output = func_6379()
func_6380 = relay.Function([], output)
mutated_mod['func_6380'] = func_6380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2010_call = mutated_mod.get_global_var('func_2010')
call_6389 = func_2009_call()
call_6390 = func_2009_call()
func_6122_call = mod.get_global_var('func_6122')
func_6129_call = mutated_mod.get_global_var('func_6129')
const_6393 = relay.const(-0.650065, dtype = "float64")#candidate|6393|()|const|float64
const_6394 = relay.const([[9.089651,1.316044,9.972047,2.730466,-5.074821]], dtype = "float64")#candidate|6394|(1, 5)|const|float64
var_6395 = relay.var("var_6395", dtype = "uint16", shape = (56, 20))#candidate|6395|(56, 20)|var|uint16
var_6396 = relay.var("var_6396", dtype = "float64", shape = (156,))#candidate|6396|(156,)|var|float64
var_6397 = relay.var("var_6397", dtype = "float32", shape = (308,))#candidate|6397|(308,)|var|float32
call_6392 = relay.TupleGetItem(func_6122_call(relay.reshape(const_6393.astype('float64'), []), relay.reshape(const_6394.astype('float64'), [5,]), relay.reshape(var_6395.astype('uint16'), [1120,]), relay.reshape(var_6396.astype('float64'), [156,]), relay.reshape(var_6397.astype('float32'), [308,]), ), 7)
call_6398 = relay.TupleGetItem(func_6129_call(relay.reshape(const_6393.astype('float64'), []), relay.reshape(const_6394.astype('float64'), [5,]), relay.reshape(var_6395.astype('uint16'), [1120,]), relay.reshape(var_6396.astype('float64'), [156,]), relay.reshape(var_6397.astype('float32'), [308,]), ), 7)
output = relay.Tuple([call_6389,call_6392,const_6393,const_6394,var_6395,var_6396,var_6397,])
output2 = relay.Tuple([call_6390,call_6398,const_6393,const_6394,var_6395,var_6396,var_6397,])
func_6406 = relay.Function([var_6395,var_6396,var_6397,], output)
mod['func_6406'] = func_6406
mod = relay.transform.InferType()(mod)
mutated_mod['func_6406'] = func_6406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6406_call = mutated_mod.get_global_var('func_6406')
var_6408 = relay.var("var_6408", dtype = "uint16", shape = (56, 20))#candidate|6408|(56, 20)|var|uint16
var_6409 = relay.var("var_6409", dtype = "float64", shape = (156,))#candidate|6409|(156,)|var|float64
var_6410 = relay.var("var_6410", dtype = "float32", shape = (308,))#candidate|6410|(308,)|var|float32
call_6407 = func_6406_call(var_6408,var_6409,var_6410,)
output = call_6407
func_6411 = relay.Function([var_6408,var_6409,var_6410,], output)
mutated_mod['func_6411'] = func_6411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5198_call = mod.get_global_var('func_5198')
func_5199_call = mutated_mod.get_global_var('func_5199')
call_6425 = func_5198_call()
call_6426 = func_5198_call()
var_6427 = relay.var("var_6427", dtype = "float32", shape = (11, 5, 14))#candidate|6427|(11, 5, 14)|var|float32
bop_6428 = relay.logical_and(call_6425.astype('bool'), var_6427.astype('bool')) # shape=(11, 5, 14)
bop_6431 = relay.logical_and(call_6426.astype('bool'), var_6427.astype('bool')) # shape=(11, 5, 14)
bop_6435 = relay.maximum(var_6427.astype('float32'), relay.reshape(bop_6428.astype('float32'), relay.shape_of(var_6427))) # shape=(11, 5, 14)
bop_6438 = relay.maximum(var_6427.astype('float32'), relay.reshape(bop_6431.astype('float32'), relay.shape_of(var_6427))) # shape=(11, 5, 14)
bop_6452 = relay.mod(call_6425.astype('float64'), bop_6428.astype('float64')) # shape=(11, 5, 14)
bop_6455 = relay.mod(call_6426.astype('float64'), bop_6431.astype('float64')) # shape=(11, 5, 14)
func_5407_call = mod.get_global_var('func_5407')
func_5409_call = mutated_mod.get_global_var('func_5409')
call_6460 = relay.TupleGetItem(func_5407_call(), 0)
call_6461 = relay.TupleGetItem(func_5409_call(), 0)
bop_6473 = relay.left_shift(bop_6452.astype('uint16'), relay.reshape(var_6427.astype('uint16'), relay.shape_of(bop_6452))) # shape=(11, 5, 14)
bop_6476 = relay.left_shift(bop_6455.astype('uint16'), relay.reshape(var_6427.astype('uint16'), relay.shape_of(bop_6455))) # shape=(11, 5, 14)
bop_6479 = relay.subtract(bop_6452.astype('uint64'), relay.reshape(bop_6473.astype('uint64'), relay.shape_of(bop_6452))) # shape=(11, 5, 14)
bop_6482 = relay.subtract(bop_6455.astype('uint64'), relay.reshape(bop_6476.astype('uint64'), relay.shape_of(bop_6455))) # shape=(11, 5, 14)
uop_6485 = relay.acosh(bop_6428.astype('float32')) # shape=(11, 5, 14)
uop_6487 = relay.acosh(bop_6431.astype('float32')) # shape=(11, 5, 14)
uop_6489 = relay.cosh(var_6427.astype('float64')) # shape=(11, 5, 14)
output = relay.Tuple([bop_6435,call_6460,bop_6479,uop_6485,uop_6489,])
output2 = relay.Tuple([bop_6438,call_6461,bop_6482,uop_6487,uop_6489,])
F = relay.Function([var_6427,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6427,], output2)
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
