import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_199 = relay.var("var_199", dtype = "float64", shape = ())#candidate|199|()|var|float64
var_200 = relay.var("var_200", dtype = "float64", shape = (7, 3, 15))#candidate|200|(7, 3, 15)|var|float64
bop_201 = relay.power(var_199.astype('float64'), var_200.astype('float64')) # shape=(7, 3, 15)
uop_207 = relay.log(bop_201.astype('float32')) # shape=(7, 3, 15)
output = uop_207
output2 = uop_207
func_228 = relay.Function([var_199,var_200,], output)
mod['func_228'] = func_228
mod = relay.transform.InferType()(mod)
var_229 = relay.var("var_229", dtype = "float64", shape = ())#candidate|229|()|var|float64
var_230 = relay.var("var_230", dtype = "float64", shape = (7, 3, 15))#candidate|230|(7, 3, 15)|var|float64
output = func_228(var_229,var_230,)
func_231 = relay.Function([var_229,var_230,], output)
mutated_mod['func_231'] = func_231
mutated_mod = relay.transform.InferType()(mutated_mod)
var_385 = relay.var("var_385", dtype = "uint64", shape = (16, 5, 3))#candidate|385|(16, 5, 3)|var|uint64
var_386 = relay.var("var_386", dtype = "uint64", shape = (16, 5, 3))#candidate|386|(16, 5, 3)|var|uint64
bop_387 = relay.greater(var_385.astype('bool'), relay.reshape(var_386.astype('bool'), relay.shape_of(var_385))) # shape=(16, 5, 3)
func_228_call = mod.get_global_var('func_228')
func_231_call = mutated_mod.get_global_var('func_231')
var_400 = relay.var("var_400", dtype = "float64", shape = ())#candidate|400|()|var|float64
const_401 = relay.const([-7.683988,5.705275,-3.031603,-8.594692,3.443820,-4.040000,9.450295,-1.081879,2.881707,4.063129,9.497478,-9.002214,-3.563499,6.251295,-6.633660,9.057499,-8.951867,9.768981,-2.897685,4.515798,-7.990575,-7.425015,-6.042593,7.312724,6.489302,4.117793,-9.240635,9.858751,-6.731654,-0.279792,8.967928,-3.155766,-1.382149,-4.527069,4.887802,3.545707,8.440255,4.794248,-3.537548,-1.467520,2.896952,-1.951420,2.479603,4.682711,-3.221960,2.001905,5.890894,-5.098795,3.943781,3.516987,-1.747522,-0.444067,-2.918496,0.454049,-2.689921,-9.500892,1.109657,9.942691,2.195976,5.809179,2.565631,5.838476,-4.501752,-8.758705,-7.166212,-2.371080,-3.875133,-6.036966,-0.538123,-9.016427,3.462467,-8.305279,7.234399,-1.172052,-0.866280,5.898137,-9.759336,8.123064,-5.059017,-3.850374,2.598584,7.002016,-3.080748,-3.848339,3.336073,5.849048,-8.940729,-0.139489,-0.562049,-1.948468,-1.787054,-1.155606,-6.657195,9.345054,7.275900,5.737878,-5.878422,6.471524,-8.858535,2.263102,-9.825568,6.655406,-3.948368,-5.109047,-8.014424,-4.096159,-7.970626,7.496119,-1.370214,1.338820,-9.130262,-9.459142,4.673786,6.059164,3.867120,-5.192940,-7.579911,-5.645267,5.052276,5.483445,8.655276,-7.586070,-2.603279,-1.745897,-0.704130,-1.828405,-7.646410,5.150024,-4.233721,-0.672999,3.398717,1.414046,-5.693899,-3.720248,3.281980,4.365287,4.543705,-0.224630,7.652383,-7.617496,9.556765,-1.707857,8.898482,6.776532,4.452116,-7.860004,-0.953501,-0.290849,4.681324,-9.129944,-9.466846,-9.652928,7.316342,4.787791,6.756392,-1.095860,-8.505192,1.652846,-7.437877,-9.552552,-2.170067,-8.604049,-5.171962,2.359680,-0.278965,-2.833141,1.281205,-7.096199,-8.147818,1.310020,-0.906388,-1.987982,-5.095807,-9.562431,-4.456957,-3.488735,3.268064,-9.957060,2.702767,-1.833201,6.351739,-9.248012,5.267657,-9.348232,-0.354635,4.627913,9.249047,-6.882458,8.700932,6.317476,7.893636,-3.448128,-7.007682,-3.572247,-5.547192,3.296267,-5.243698,-1.169992,9.362594,0.215366,-2.865070,-5.973540,-6.704203,-1.075309,1.258060,8.554674,6.115566,-7.074501,-6.029201,-3.508659,1.882947,8.535140,8.799723,1.398660,-5.465051,9.821565,2.331213,-0.245055,-2.691858,-4.345843,-4.331589,-7.057038,0.295625,-7.006476,0.354032,9.613388,-3.900481,-3.185311,-8.580009,-5.354637,-3.248003,-6.208959,6.909757,6.843791,5.688104,-5.065646,-0.587176,0.414816,5.384415,2.513478,-0.787555,4.019792,3.865209,0.903991,4.287101,-0.099659,7.237860,1.550317,-5.338394,-6.941740,-2.817728,7.071096,8.164213,5.909756,-8.330621,0.701094,4.442789,-5.112324,0.831432,-7.143507,0.326119,-5.380036,9.386456,-8.690598,0.841178,0.357315,4.933359,-5.820311,-1.205134,4.598976,-9.095491,0.237597,3.965511,9.020765,6.196406,8.391462,-9.869708,3.782014,0.030516,0.583717,-6.258432,1.658989,-5.338436,-0.860797,5.394386,7.783818,3.225488,6.625114,-1.645835,1.646678,-1.981263,7.986635,-3.585581,1.600303,-3.861991,-5.811509,6.031284,-7.797730,6.498897,-5.633744,-7.986912,2.602878,5.280445,-4.603561,9.047794,8.582844,-7.768835,-8.559104,-4.286582,-3.134872,7.746000,8.339042,-0.779834,-5.383728,7.768122], dtype = "float64")#candidate|401|(315,)|const|float64
call_399 = func_228_call(relay.reshape(var_400.astype('float64'), []), relay.reshape(const_401.astype('float64'), [7, 3, 15]), )
call_402 = func_228_call(relay.reshape(var_400.astype('float64'), []), relay.reshape(const_401.astype('float64'), [7, 3, 15]), )
bop_417 = relay.floor_divide(call_399.astype('float64'), relay.reshape(const_401.astype('float64'), relay.shape_of(call_399))) # shape=(7, 3, 15)
bop_420 = relay.floor_divide(call_402.astype('float64'), relay.reshape(const_401.astype('float64'), relay.shape_of(call_402))) # shape=(7, 3, 15)
func_228_call = mod.get_global_var('func_228')
func_231_call = mutated_mod.get_global_var('func_231')
call_421 = func_228_call(relay.reshape(var_400.astype('float64'), []), relay.reshape(call_399.astype('float64'), [7, 3, 15]), )
call_422 = func_228_call(relay.reshape(var_400.astype('float64'), []), relay.reshape(call_399.astype('float64'), [7, 3, 15]), )
bop_423 = relay.less(var_385.astype('bool'), relay.reshape(bop_387.astype('bool'), relay.shape_of(var_385))) # shape=(16, 5, 3)
func_228_call = mod.get_global_var('func_228')
func_231_call = mutated_mod.get_global_var('func_231')
call_438 = func_228_call(relay.reshape(var_400.astype('float64'), []), relay.reshape(call_421.astype('float64'), [7, 3, 15]), )
call_439 = func_228_call(relay.reshape(var_400.astype('float64'), []), relay.reshape(call_421.astype('float64'), [7, 3, 15]), )
output = relay.Tuple([var_400,bop_417,call_421,bop_423,call_438,])
output2 = relay.Tuple([var_400,bop_420,call_422,bop_423,call_439,])
func_444 = relay.Function([var_385,var_386,var_400,], output)
mod['func_444'] = func_444
mod = relay.transform.InferType()(mod)
var_445 = relay.var("var_445", dtype = "uint64", shape = (16, 5, 3))#candidate|445|(16, 5, 3)|var|uint64
var_446 = relay.var("var_446", dtype = "uint64", shape = (16, 5, 3))#candidate|446|(16, 5, 3)|var|uint64
var_447 = relay.var("var_447", dtype = "float64", shape = ())#candidate|447|()|var|float64
output = func_444(var_445,var_446,var_447,)
func_448 = relay.Function([var_445,var_446,var_447,], output)
mutated_mod['func_448'] = func_448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_972 = relay.var("var_972", dtype = "bool", shape = (9, 12, 4))#candidate|972|(9, 12, 4)|var|bool
var_973 = relay.var("var_973", dtype = "bool", shape = (9, 12, 4))#candidate|973|(9, 12, 4)|var|bool
bop_974 = relay.logical_and(var_972.astype('bool'), relay.reshape(var_973.astype('bool'), relay.shape_of(var_972))) # shape=(9, 12, 4)
bop_978 = relay.less_equal(bop_974.astype('bool'), relay.reshape(var_972.astype('bool'), relay.shape_of(bop_974))) # shape=(9, 12, 4)
output = relay.Tuple([bop_978,])
output2 = relay.Tuple([bop_978,])
func_987 = relay.Function([var_972,var_973,], output)
mod['func_987'] = func_987
mod = relay.transform.InferType()(mod)
var_988 = relay.var("var_988", dtype = "bool", shape = (9, 12, 4))#candidate|988|(9, 12, 4)|var|bool
var_989 = relay.var("var_989", dtype = "bool", shape = (9, 12, 4))#candidate|989|(9, 12, 4)|var|bool
output = func_987(var_988,var_989,)
func_990 = relay.Function([var_988,var_989,], output)
mutated_mod['func_990'] = func_990
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1264 = relay.var("var_1264", dtype = "float64", shape = (7, 11, 12))#candidate|1264|(7, 11, 12)|var|float64
var_1265 = relay.var("var_1265", dtype = "float64", shape = (7, 11, 12))#candidate|1265|(7, 11, 12)|var|float64
bop_1266 = relay.power(var_1264.astype('float64'), relay.reshape(var_1265.astype('float64'), relay.shape_of(var_1264))) # shape=(7, 11, 12)
uop_1270 = relay.acosh(bop_1266.astype('float64')) # shape=(7, 11, 12)
output = relay.Tuple([uop_1270,])
output2 = relay.Tuple([uop_1270,])
func_1272 = relay.Function([var_1264,var_1265,], output)
mod['func_1272'] = func_1272
mod = relay.transform.InferType()(mod)
mutated_mod['func_1272'] = func_1272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1272_call = mutated_mod.get_global_var('func_1272')
var_1274 = relay.var("var_1274", dtype = "float64", shape = (7, 11, 12))#candidate|1274|(7, 11, 12)|var|float64
var_1275 = relay.var("var_1275", dtype = "float64", shape = (7, 11, 12))#candidate|1275|(7, 11, 12)|var|float64
call_1273 = func_1272_call(var_1274,var_1275,)
output = call_1273
func_1276 = relay.Function([var_1274,var_1275,], output)
mutated_mod['func_1276'] = func_1276
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1292 = relay.var("var_1292", dtype = "float32", shape = (11, 12))#candidate|1292|(11, 12)|var|float32
uop_1293 = relay.atan(var_1292.astype('float32')) # shape=(11, 12)
func_987_call = mod.get_global_var('func_987')
func_990_call = mutated_mod.get_global_var('func_990')
var_1304 = relay.var("var_1304", dtype = "bool", shape = (2, 216))#candidate|1304|(2, 216)|var|bool
call_1303 = relay.TupleGetItem(func_987_call(relay.reshape(var_1304.astype('bool'), [9, 12, 4]), relay.reshape(var_1304.astype('bool'), [9, 12, 4]), ), 0)
call_1305 = relay.TupleGetItem(func_990_call(relay.reshape(var_1304.astype('bool'), [9, 12, 4]), relay.reshape(var_1304.astype('bool'), [9, 12, 4]), ), 0)
output = relay.Tuple([uop_1293,call_1303,var_1304,])
output2 = relay.Tuple([uop_1293,call_1305,var_1304,])
func_1316 = relay.Function([var_1292,var_1304,], output)
mod['func_1316'] = func_1316
mod = relay.transform.InferType()(mod)
mutated_mod['func_1316'] = func_1316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mutated_mod.get_global_var('func_1316')
var_1318 = relay.var("var_1318", dtype = "float32", shape = (11, 12))#candidate|1318|(11, 12)|var|float32
var_1319 = relay.var("var_1319", dtype = "bool", shape = (2, 216))#candidate|1319|(2, 216)|var|bool
call_1317 = func_1316_call(var_1318,var_1319,)
output = call_1317
func_1320 = relay.Function([var_1318,var_1319,], output)
mutated_mod['func_1320'] = func_1320
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1406 = relay.const([[[-7,8,1,-6,-2,7,4,8,-7,-6,7,-1,-4,5],[-10,1,6,-7,9,3,4,7,-5,-8,5,5,3,-2],[7,-5,10,6,7,-4,-9,-8,-6,10,1,-6,-5,-8],[-6,-7,6,10,8,-2,3,3,-3,-6,-7,-2,6,7],[-8,-2,-3,-9,-1,-7,-7,5,-6,-2,3,-10,4,-1],[2,6,10,8,6,-4,-6,-5,-1,3,-3,6,2,-4],[-10,1,-2,-5,2,8,1,-3,5,10,-2,-3,9,-9],[-7,-9,10,2,4,6,1,6,-8,-8,8,-8,2,-3],[3,2,-7,-9,-1,-8,-6,-3,-8,8,-7,-10,-6,-5],[-2,-7,-2,-4,-2,-7,4,7,2,9,-8,-8,5,10],[-8,8,-7,4,-6,8,3,-10,-1,-7,7,-4,4,10],[10,9,-6,8,3,-3,-2,8,8,-10,-3,3,4,-4],[7,-6,-3,7,-3,5,6,-5,-10,-2,1,7,-1,-3],[-6,-3,-9,2,-5,3,3,-4,-3,7,-3,2,-3,7],[9,-10,7,10,4,9,-2,-9,-8,3,-3,-7,-9,2]],[[7,-7,9,1,-5,-3,-2,10,5,-8,4,6,-10,-6],[1,-3,7,-5,9,4,7,-3,-10,-5,-2,-7,4,6],[6,5,7,-6,-7,-1,-6,-10,-2,2,-8,8,9,8],[1,-7,3,-4,1,-5,10,-7,-2,-7,-2,8,-7,-1],[4,-2,-1,-9,3,7,3,2,-1,-10,-6,7,10,-7],[2,5,-7,-10,-4,-5,4,10,-5,3,-9,-8,1,-2],[-3,-8,-7,10,8,2,-10,-10,10,-2,-2,2,-9,8],[-8,-1,-1,5,-1,-2,6,2,3,-8,4,10,6,-9],[4,7,10,-10,-6,-9,-9,-8,8,-9,-6,6,1,-7],[-9,4,-6,5,6,4,-2,2,5,6,-2,6,6,-9],[9,-3,-4,4,-7,-3,4,-6,-2,8,8,3,-3,-1],[1,5,6,10,7,8,-3,-7,-10,-3,-1,10,-7,3],[-1,8,-4,4,2,-10,10,-1,2,-9,-10,3,-5,5],[5,3,-2,-10,5,6,9,-6,-7,1,-4,-2,-1,8],[-9,10,-10,-1,-4,-1,-6,6,-5,6,9,3,-6,-10]],[[1,4,2,3,-7,-6,-3,9,4,-7,-10,-4,8,6],[2,2,-5,-3,-10,-3,-9,7,-6,3,4,2,3,-6],[-3,7,-8,1,7,2,-10,-2,4,3,6,3,-10,-5],[-8,5,3,9,3,5,-3,5,4,4,-9,-9,5,-6],[-4,9,3,-5,6,-8,-3,-6,9,-2,3,10,-3,6],[10,4,-4,-8,-4,3,-5,10,-3,-4,10,-5,2,-4],[6,-2,1,-2,8,3,-1,6,7,-5,2,3,5,-4],[7,1,-7,2,10,4,4,-4,4,-2,-3,1,4,9],[4,-8,1,-4,4,-6,-2,4,6,10,9,-10,6,-10],[-3,-2,2,10,1,2,2,2,8,9,-6,-3,8,7],[-5,4,6,7,-10,-1,-10,8,3,-5,6,5,2,8],[3,4,4,8,-6,10,-1,-8,-6,-5,6,9,6,5],[4,-8,9,-7,-9,-5,-9,2,-7,-4,-7,-3,-3,-7],[6,8,5,9,5,-9,10,-1,10,-2,4,-2,-7,5],[5,10,4,-3,2,-5,7,-3,-7,-9,-8,3,-7,6]],[[-10,-5,-3,-8,10,5,3,-1,3,1,-10,8,9,1],[-8,1,8,-3,-8,-7,2,2,-2,-8,-7,-7,-9,-5],[6,-6,5,-2,-3,3,4,2,1,-1,-7,8,-10,-10],[-9,7,5,2,3,10,-9,-9,-2,-8,5,4,2,7],[-6,-1,4,-2,3,8,8,-4,-2,1,-4,-6,10,-2],[-3,-6,-5,-6,7,9,-4,8,8,10,-4,3,9,10],[9,-4,2,3,-9,8,9,-7,-8,-6,8,-6,6,-4],[-1,6,8,-4,2,-10,8,-6,-9,9,-2,4,2,6],[-3,3,-7,-6,9,-7,-9,9,-7,4,1,-3,-2,-5],[-9,10,-1,6,2,-5,1,-9,9,8,6,-9,-9,2],[-1,4,7,-2,9,-8,-9,9,5,2,9,-7,4,-1],[-2,4,9,-1,-4,-5,-2,-1,6,-1,-1,2,-3,-4],[-8,-1,10,-2,-5,-7,10,9,5,-1,1,9,-4,-1],[-3,-5,-4,1,-4,-4,8,6,-3,7,7,10,-1,2],[-1,6,2,5,10,1,-9,-2,8,6,-7,3,3,3]]], dtype = "uint8")#candidate|1406|(4, 15, 14)|const|uint8
var_1407 = relay.var("var_1407", dtype = "uint8", shape = (4, 15, 14))#candidate|1407|(4, 15, 14)|var|uint8
bop_1408 = relay.not_equal(const_1406.astype('bool'), relay.reshape(var_1407.astype('bool'), relay.shape_of(const_1406))) # shape=(4, 15, 14)
output = bop_1408
output2 = bop_1408
func_1418 = relay.Function([var_1407,], output)
mod['func_1418'] = func_1418
mod = relay.transform.InferType()(mod)
mutated_mod['func_1418'] = func_1418
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1419 = relay.var("var_1419", dtype = "uint8", shape = (4, 15, 14))#candidate|1419|(4, 15, 14)|var|uint8
func_1418_call = mutated_mod.get_global_var('func_1418')
call_1420 = func_1418_call(var_1419)
output = call_1420
func_1421 = relay.Function([var_1419], output)
mutated_mod['func_1421'] = func_1421
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1616 = relay.const([[[6.958234,8.841664,9.888880],[-5.476754,-8.189864,-3.882177],[-4.414175,-1.539881,-9.744798],[4.688012,-7.174155,4.162799],[2.428285,2.550248,-6.565947],[0.851576,0.687082,-7.464058],[-5.361425,5.000163,1.244522],[-4.683776,-5.579558,0.174038],[7.216250,0.622617,-1.964401],[6.603255,3.246539,5.945321]],[[7.236482,0.808698,1.322891],[8.244218,-7.777256,6.782580],[7.587509,-6.536747,-1.861028],[-9.478223,-5.710373,8.892645],[-6.156729,8.286833,-3.547933],[-4.686934,7.287272,-0.189098],[7.227603,-8.497870,-3.410522],[3.537441,-0.860197,-7.305861],[1.000762,-0.059673,-4.446206],[-1.891962,-8.050203,-1.359820]],[[-3.151002,-0.171270,-8.010136],[6.557442,6.655907,-1.476553],[1.063335,0.136084,2.768984],[-9.745814,-6.724498,-6.139940],[-0.308126,-6.153354,-3.479090],[1.806401,9.213069,9.779165],[-7.175820,8.501566,-2.567229],[-6.770180,1.796456,8.670604],[1.469164,0.591402,-1.294880],[-4.376259,-2.676750,5.789425]],[[-5.891748,-0.003504,2.208542],[0.575753,-9.806524,6.036082],[-0.678692,-4.877068,8.482091],[-8.587366,8.145779,-2.063491],[-0.726011,-5.447749,3.074101],[6.109322,6.091319,4.934931],[6.605301,-2.828601,8.853273],[5.134342,9.502913,4.247113],[1.424128,5.174358,4.501310],[5.987191,6.746243,7.775770]],[[0.288319,-7.456881,-8.733841],[3.962034,-7.198062,4.144469],[2.434372,-3.963613,-2.191521],[8.585079,8.376378,-4.222215],[2.601014,-1.140941,1.347527],[1.560202,2.333024,0.106614],[-2.267346,1.883870,5.044155],[-9.434103,8.366538,3.052547],[9.961670,-3.056919,-7.086710],[9.839356,-4.341736,-8.936629]],[[2.204565,-2.440828,6.894525],[-0.827007,5.896127,-7.102860],[-7.872572,7.184792,6.606515],[0.331546,-1.936430,-5.073842],[-7.243641,-1.078760,2.079252],[4.618621,-1.321600,0.832120],[1.156675,3.061617,-0.987136],[5.072349,9.463814,-9.985077],[-3.704654,6.582094,0.088448],[4.267099,2.449195,-2.722789]],[[-1.485318,-0.784334,-7.337313],[-3.755510,9.379470,-1.420050],[6.298574,2.314618,-8.978430],[-3.266376,0.727064,4.568083],[6.288861,6.924154,-9.060060],[3.641016,5.551336,-6.316909],[-2.229770,9.003310,-9.374664],[8.809947,-3.369814,-4.704870],[-3.615414,3.032169,-4.199562],[0.528424,9.071787,1.972675]],[[-9.122230,-7.972251,-9.915676],[4.843815,6.948511,-1.561413],[-1.126374,6.028610,-3.566280],[-0.034809,-5.621732,3.078534],[-5.958983,-8.519972,4.798761],[-8.013687,6.590615,2.831507],[5.355422,-5.662927,9.057751],[-5.442347,-7.257461,-1.170281],[-6.859355,4.896379,-9.804478],[1.599561,7.423978,-7.205504]],[[0.117524,6.369719,0.363555],[-5.201149,2.708242,1.173316],[-8.018250,9.354356,-5.732361],[8.267523,-5.719680,7.523592],[3.030355,7.755443,0.371589],[6.759405,-2.653642,3.164858],[6.854790,-6.358729,-6.551424],[-3.031468,-6.117952,3.768142],[4.148229,4.278647,6.166620],[2.908788,7.168302,-6.582025]],[[-3.172084,-9.047689,-2.639518],[7.091747,3.044032,-0.693113],[8.979488,-4.123293,-4.710240],[-9.717383,8.487626,0.012564],[9.994474,2.996978,-1.979796],[4.003621,-0.860817,1.873975],[9.825735,-4.625881,2.241616],[-4.604668,6.459661,-7.420954],[-4.192179,-9.286385,-1.239815],[-8.969297,-6.025158,-7.199876]],[[6.392179,6.729569,5.207421],[-0.280722,2.279280,-1.252820],[-7.400618,-9.142607,3.048591],[7.439920,9.238550,0.205744],[-6.205484,8.942225,-8.154962],[7.084339,4.432777,9.138867],[3.962651,0.587429,-9.746432],[0.623534,-6.070117,8.811606],[-2.587825,9.008873,-0.212997],[5.967125,9.443505,6.642774]]], dtype = "float32")#candidate|1616|(11, 10, 3)|const|float32
uop_1617 = relay.rsqrt(const_1616.astype('float32')) # shape=(11, 10, 3)
func_444_call = mod.get_global_var('func_444')
func_448_call = mutated_mod.get_global_var('func_448')
const_1623 = relay.const([[-2,2,-5,9,8,7,-3,-4,-4,8,-3,-10,5,-4,5,1,-8,-7,2,8,-1,-1,6,1,-8,-9,-8,-4,1,3],[9,-5,7,-9,-5,-10,3,-3,7,-9,5,-8,9,5,7,7,-1,4,-2,8,-1,8,-2,-3,6,-5,-1,5,2,-9],[-7,-6,9,-8,-4,-2,7,-1,10,-7,7,9,-5,-10,-4,8,7,10,6,9,-6,-7,3,-1,3,1,-10,-1,-7,-1],[-2,-10,5,-7,10,2,-8,-9,8,-6,-10,4,9,4,-8,5,-6,-1,9,-3,-5,-4,-4,6,7,-5,-10,6,6,-5],[8,4,-9,6,-4,-6,2,4,5,9,3,-8,5,-2,3,-5,9,7,-6,-5,-10,1,-1,9,6,-9,-4,-2,10,-1],[-3,-5,8,2,5,-8,8,-6,-6,-6,-2,3,-1,-6,1,5,-4,8,-4,-7,8,3,-5,-5,-5,3,-6,-5,1,10],[-7,-8,9,4,-8,2,8,-4,-4,4,-9,-9,5,-6,3,10,2,4,6,7,-9,-2,4,-10,6,-10,-4,2,2,6],[3,-7,6,10,-9,7,-6,7,-6,10,2,7,-10,-5,-6,-8,-9,-7,6,6,-4,5,4,10,8,2,-2,8,-9,-4]], dtype = "uint64")#candidate|1623|(8, 30)|const|uint64
const_1624 = relay.const(0.475677, dtype = "float64")#candidate|1624|()|const|float64
call_1622 = relay.TupleGetItem(func_444_call(relay.reshape(const_1623.astype('uint64'), [16, 5, 3]), relay.reshape(const_1623.astype('uint64'), [16, 5, 3]), relay.reshape(const_1624.astype('float64'), []), ), 2)
call_1625 = relay.TupleGetItem(func_448_call(relay.reshape(const_1623.astype('uint64'), [16, 5, 3]), relay.reshape(const_1623.astype('uint64'), [16, 5, 3]), relay.reshape(const_1624.astype('float64'), []), ), 2)
output = relay.Tuple([uop_1617,call_1622,const_1623,const_1624,])
output2 = relay.Tuple([uop_1617,call_1625,const_1623,const_1624,])
func_1626 = relay.Function([], output)
mod['func_1626'] = func_1626
mod = relay.transform.InferType()(mod)
mutated_mod['func_1626'] = func_1626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1626_call = mutated_mod.get_global_var('func_1626')
call_1627 = func_1626_call()
output = call_1627
func_1628 = relay.Function([], output)
mutated_mod['func_1628'] = func_1628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
call_1660 = relay.TupleGetItem(func_1626_call(), 0)
call_1661 = relay.TupleGetItem(func_1628_call(), 0)
output = call_1660
output2 = call_1661
func_1668 = relay.Function([], output)
mod['func_1668'] = func_1668
mod = relay.transform.InferType()(mod)
mutated_mod['func_1668'] = func_1668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1668_call = mutated_mod.get_global_var('func_1668')
call_1669 = func_1668_call()
output = call_1669
func_1670 = relay.Function([], output)
mutated_mod['func_1670'] = func_1670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
call_1728 = relay.TupleGetItem(func_1626_call(), 2)
call_1729 = relay.TupleGetItem(func_1628_call(), 2)
func_444_call = mod.get_global_var('func_444')
func_448_call = mutated_mod.get_global_var('func_448')
const_1733 = relay.const(-1.219742, dtype = "float64")#candidate|1733|()|const|float64
call_1732 = relay.TupleGetItem(func_444_call(relay.reshape(call_1728.astype('uint64'), [16, 5, 3]), relay.reshape(call_1728.astype('uint64'), [16, 5, 3]), relay.reshape(const_1733.astype('float64'), []), ), 2)
call_1734 = relay.TupleGetItem(func_448_call(relay.reshape(call_1728.astype('uint64'), [16, 5, 3]), relay.reshape(call_1728.astype('uint64'), [16, 5, 3]), relay.reshape(const_1733.astype('float64'), []), ), 2)
func_228_call = mod.get_global_var('func_228')
func_231_call = mutated_mod.get_global_var('func_231')
call_1742 = func_228_call(relay.reshape(const_1733.astype('float64'), []), relay.reshape(call_1732.astype('float64'), [7, 3, 15]), )
call_1743 = func_228_call(relay.reshape(const_1733.astype('float64'), []), relay.reshape(call_1732.astype('float64'), [7, 3, 15]), )
func_987_call = mod.get_global_var('func_987')
func_990_call = mutated_mod.get_global_var('func_990')
const_1747 = relay.const([[False,False,False,True,False,False,False,True,False,True,False,False],[True,True,True,False,False,False,False,True,True,False,True,True],[False,False,True,True,True,True,False,True,True,False,False,False],[False,True,True,False,False,False,True,True,True,False,True,True],[False,True,False,True,False,True,False,False,False,False,False,True],[True,False,False,False,False,True,False,False,False,False,True,False],[False,False,True,True,False,True,False,False,False,False,False,False],[False,False,True,False,False,True,True,True,True,True,False,True],[False,False,True,False,False,False,False,False,False,False,True,False],[True,True,True,True,False,True,False,False,True,True,False,False],[False,True,True,True,False,True,False,True,False,True,True,False],[False,False,True,False,False,False,True,True,False,False,False,False],[True,False,False,False,True,False,False,True,True,False,False,True],[True,False,False,True,False,False,False,False,False,True,False,False],[True,True,True,True,True,True,True,False,False,True,True,True],[True,True,True,False,True,True,False,True,False,False,False,False],[False,False,False,False,True,False,False,True,False,True,False,True],[True,False,False,True,True,True,False,True,False,True,True,False],[True,True,True,True,False,True,True,False,False,True,True,True],[True,True,False,True,True,True,True,False,True,True,True,False],[False,True,True,False,True,True,False,False,False,True,True,False],[True,False,True,True,True,False,False,False,True,True,False,False],[False,True,False,True,False,True,True,False,True,True,False,False],[False,True,False,False,False,True,True,True,True,False,False,False],[False,True,False,True,False,False,False,False,True,False,True,True],[False,False,True,True,True,False,True,True,True,True,False,True],[False,True,True,True,True,True,True,True,False,True,False,False],[False,False,False,True,True,True,True,True,False,False,False,True],[False,True,True,True,False,True,True,False,False,False,True,True],[True,False,False,False,True,False,False,True,True,True,True,False],[False,False,True,False,False,True,False,True,False,True,False,False],[False,True,False,False,True,True,True,True,True,True,True,False],[True,True,False,False,False,True,False,True,True,True,True,True],[False,True,False,False,False,True,False,False,False,False,False,False],[True,True,True,False,False,False,True,False,True,True,False,False],[False,True,True,True,False,False,False,True,False,True,True,False]], dtype = "bool")#candidate|1747|(36, 12)|const|bool
call_1746 = relay.TupleGetItem(func_987_call(relay.reshape(const_1747.astype('bool'), [9, 12, 4]), relay.reshape(const_1747.astype('bool'), [9, 12, 4]), ), 0)
call_1748 = relay.TupleGetItem(func_990_call(relay.reshape(const_1747.astype('bool'), [9, 12, 4]), relay.reshape(const_1747.astype('bool'), [9, 12, 4]), ), 0)
bop_1763 = relay.less(const_1733.astype('bool'), call_1728.astype('bool')) # shape=(8, 30)
bop_1766 = relay.less(const_1733.astype('bool'), call_1729.astype('bool')) # shape=(8, 30)
func_987_call = mod.get_global_var('func_987')
func_990_call = mutated_mod.get_global_var('func_990')
call_1767 = relay.TupleGetItem(func_987_call(relay.reshape(call_1746.astype('bool'), [9, 12, 4]), relay.reshape(const_1747.astype('bool'), [9, 12, 4]), ), 0)
call_1768 = relay.TupleGetItem(func_990_call(relay.reshape(call_1746.astype('bool'), [9, 12, 4]), relay.reshape(const_1747.astype('bool'), [9, 12, 4]), ), 0)
func_228_call = mod.get_global_var('func_228')
func_231_call = mutated_mod.get_global_var('func_231')
call_1809 = func_228_call(relay.reshape(const_1733.astype('float64'), []), relay.reshape(call_1732.astype('float64'), [7, 3, 15]), )
call_1810 = func_228_call(relay.reshape(const_1733.astype('float64'), []), relay.reshape(call_1732.astype('float64'), [7, 3, 15]), )
var_1818 = relay.var("var_1818", dtype = "bool", shape = (8, 30))#candidate|1818|(8, 30)|var|bool
bop_1819 = relay.logical_and(bop_1763.astype('bool'), relay.reshape(var_1818.astype('bool'), relay.shape_of(bop_1763))) # shape=(8, 30)
bop_1822 = relay.logical_and(bop_1766.astype('bool'), relay.reshape(var_1818.astype('bool'), relay.shape_of(bop_1766))) # shape=(8, 30)
uop_1823 = relay.acosh(var_1818.astype('float32')) # shape=(8, 30)
output = relay.Tuple([call_1732,call_1742,call_1746,const_1747,call_1767,call_1809,bop_1819,uop_1823,])
output2 = relay.Tuple([call_1734,call_1743,call_1748,const_1747,call_1768,call_1810,bop_1822,uop_1823,])
func_1825 = relay.Function([var_1818,], output)
mod['func_1825'] = func_1825
mod = relay.transform.InferType()(mod)
mutated_mod['func_1825'] = func_1825
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1826 = relay.var("var_1826", dtype = "bool", shape = (8, 30))#candidate|1826|(8, 30)|var|bool
func_1825_call = mutated_mod.get_global_var('func_1825')
call_1827 = func_1825_call(var_1826)
output = call_1827
func_1828 = relay.Function([var_1826], output)
mutated_mod['func_1828'] = func_1828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1668_call = mod.get_global_var('func_1668')
func_1670_call = mutated_mod.get_global_var('func_1670')
call_1862 = func_1668_call()
call_1863 = func_1668_call()
output = relay.Tuple([call_1862,])
output2 = relay.Tuple([call_1863,])
func_1864 = relay.Function([], output)
mod['func_1864'] = func_1864
mod = relay.transform.InferType()(mod)
mutated_mod['func_1864'] = func_1864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mutated_mod.get_global_var('func_1864')
call_1865 = func_1864_call()
output = call_1865
func_1866 = relay.Function([], output)
mutated_mod['func_1866'] = func_1866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1668_call = mod.get_global_var('func_1668')
func_1670_call = mutated_mod.get_global_var('func_1670')
call_1874 = func_1668_call()
call_1875 = func_1668_call()
uop_1878 = relay.exp(call_1874.astype('float32')) # shape=(11, 10, 3)
uop_1880 = relay.exp(call_1875.astype('float32')) # shape=(11, 10, 3)
func_987_call = mod.get_global_var('func_987')
func_990_call = mutated_mod.get_global_var('func_990')
const_1886 = relay.const([True,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,True], dtype = "bool")#candidate|1886|(432,)|const|bool
call_1885 = relay.TupleGetItem(func_987_call(relay.reshape(const_1886.astype('bool'), [9, 12, 4]), relay.reshape(const_1886.astype('bool'), [9, 12, 4]), ), 0)
call_1887 = relay.TupleGetItem(func_990_call(relay.reshape(const_1886.astype('bool'), [9, 12, 4]), relay.reshape(const_1886.astype('bool'), [9, 12, 4]), ), 0)
output = relay.Tuple([uop_1878,call_1885,const_1886,])
output2 = relay.Tuple([uop_1880,call_1887,const_1886,])
func_1892 = relay.Function([], output)
mod['func_1892'] = func_1892
mod = relay.transform.InferType()(mod)
mutated_mod['func_1892'] = func_1892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mutated_mod.get_global_var('func_1892')
call_1893 = func_1892_call()
output = call_1893
func_1894 = relay.Function([], output)
mutated_mod['func_1894'] = func_1894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1866_call = mutated_mod.get_global_var('func_1866')
call_1897 = relay.TupleGetItem(func_1864_call(), 0)
call_1898 = relay.TupleGetItem(func_1866_call(), 0)
func_228_call = mod.get_global_var('func_228')
func_231_call = mutated_mod.get_global_var('func_231')
const_1907 = relay.const(-3.357602, dtype = "float64")#candidate|1907|()|const|float64
var_1908 = relay.var("var_1908", dtype = "float64", shape = (315, 1))#candidate|1908|(315, 1)|var|float64
call_1906 = func_228_call(relay.reshape(const_1907.astype('float64'), []), relay.reshape(var_1908.astype('float64'), [7, 3, 15]), )
call_1909 = func_228_call(relay.reshape(const_1907.astype('float64'), []), relay.reshape(var_1908.astype('float64'), [7, 3, 15]), )
func_444_call = mod.get_global_var('func_444')
func_448_call = mutated_mod.get_global_var('func_448')
var_1912 = relay.var("var_1912", dtype = "uint64", shape = (240,))#candidate|1912|(240,)|var|uint64
call_1911 = relay.TupleGetItem(func_444_call(relay.reshape(var_1912.astype('uint64'), [16, 5, 3]), relay.reshape(var_1912.astype('uint64'), [16, 5, 3]), relay.reshape(const_1907.astype('float64'), []), ), 0)
call_1913 = relay.TupleGetItem(func_448_call(relay.reshape(var_1912.astype('uint64'), [16, 5, 3]), relay.reshape(var_1912.astype('uint64'), [16, 5, 3]), relay.reshape(const_1907.astype('float64'), []), ), 0)
output = relay.Tuple([call_1897,call_1906,const_1907,var_1908,call_1911,var_1912,])
output2 = relay.Tuple([call_1898,call_1909,const_1907,var_1908,call_1913,var_1912,])
func_1924 = relay.Function([var_1908,var_1912,], output)
mod['func_1924'] = func_1924
mod = relay.transform.InferType()(mod)
mutated_mod['func_1924'] = func_1924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1924_call = mutated_mod.get_global_var('func_1924')
var_1926 = relay.var("var_1926", dtype = "float64", shape = (315, 1))#candidate|1926|(315, 1)|var|float64
var_1927 = relay.var("var_1927", dtype = "uint64", shape = (240,))#candidate|1927|(240,)|var|uint64
call_1925 = func_1924_call(var_1926,var_1927,)
output = call_1925
func_1928 = relay.Function([var_1926,var_1927,], output)
mutated_mod['func_1928'] = func_1928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
call_1933 = relay.TupleGetItem(func_1626_call(), 1)
call_1934 = relay.TupleGetItem(func_1628_call(), 1)
func_1418_call = mod.get_global_var('func_1418')
func_1421_call = mutated_mod.get_global_var('func_1421')
var_1955 = relay.var("var_1955", dtype = "uint8", shape = (840,))#candidate|1955|(840,)|var|uint8
call_1954 = func_1418_call(relay.reshape(var_1955.astype('uint8'), [4, 15, 14]))
call_1956 = func_1418_call(relay.reshape(var_1955.astype('uint8'), [4, 15, 14]))
func_1864_call = mod.get_global_var('func_1864')
func_1866_call = mutated_mod.get_global_var('func_1866')
call_1959 = relay.TupleGetItem(func_1864_call(), 0)
call_1960 = relay.TupleGetItem(func_1866_call(), 0)
output = relay.Tuple([call_1933,call_1954,var_1955,call_1959,])
output2 = relay.Tuple([call_1934,call_1956,var_1955,call_1960,])
func_1963 = relay.Function([var_1955,], output)
mod['func_1963'] = func_1963
mod = relay.transform.InferType()(mod)
var_1964 = relay.var("var_1964", dtype = "uint8", shape = (840,))#candidate|1964|(840,)|var|uint8
output = func_1963(var_1964)
func_1965 = relay.Function([var_1964], output)
mutated_mod['func_1965'] = func_1965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1866_call = mutated_mod.get_global_var('func_1866')
call_2017 = relay.TupleGetItem(func_1864_call(), 0)
call_2018 = relay.TupleGetItem(func_1866_call(), 0)
output = call_2017
output2 = call_2018
func_2027 = relay.Function([], output)
mod['func_2027'] = func_2027
mod = relay.transform.InferType()(mod)
output = func_2027()
func_2028 = relay.Function([], output)
mutated_mod['func_2028'] = func_2028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_2057 = relay.TupleGetItem(func_1892_call(), 0)
call_2058 = relay.TupleGetItem(func_1894_call(), 0)
output = call_2057
output2 = call_2058
func_2059 = relay.Function([], output)
mod['func_2059'] = func_2059
mod = relay.transform.InferType()(mod)
mutated_mod['func_2059'] = func_2059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mutated_mod.get_global_var('func_2059')
call_2060 = func_2059_call()
output = call_2060
func_2061 = relay.Function([], output)
mutated_mod['func_2061'] = func_2061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2067 = func_2059_call()
call_2068 = func_2059_call()
func_1864_call = mod.get_global_var('func_1864')
func_1866_call = mutated_mod.get_global_var('func_1866')
call_2077 = relay.TupleGetItem(func_1864_call(), 0)
call_2078 = relay.TupleGetItem(func_1866_call(), 0)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
var_2095 = relay.var("var_2095", dtype = "uint8", shape = (840,))#candidate|2095|(840,)|var|uint8
call_2094 = relay.TupleGetItem(func_1963_call(relay.reshape(var_2095.astype('uint8'), [840,])), 3)
call_2096 = relay.TupleGetItem(func_1965_call(relay.reshape(var_2095.astype('uint8'), [840,])), 3)
func_1418_call = mod.get_global_var('func_1418')
func_1421_call = mutated_mod.get_global_var('func_1421')
call_2097 = func_1418_call(relay.reshape(var_2095.astype('uint8'), [4, 15, 14]))
call_2098 = func_1418_call(relay.reshape(var_2095.astype('uint8'), [4, 15, 14]))
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_2101 = relay.TupleGetItem(func_1892_call(), 0)
call_2102 = relay.TupleGetItem(func_1894_call(), 0)
uop_2110 = relay.sqrt(var_2095.astype('float32')) # shape=(840,)
output = relay.Tuple([call_2067,call_2077,call_2094,call_2097,call_2101,uop_2110,])
output2 = relay.Tuple([call_2068,call_2078,call_2096,call_2098,call_2102,uop_2110,])
func_2117 = relay.Function([var_2095,], output)
mod['func_2117'] = func_2117
mod = relay.transform.InferType()(mod)
mutated_mod['func_2117'] = func_2117
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2118 = relay.var("var_2118", dtype = "uint8", shape = (840,))#candidate|2118|(840,)|var|uint8
func_2117_call = mutated_mod.get_global_var('func_2117')
call_2119 = func_2117_call(var_2118)
output = call_2119
func_2120 = relay.Function([var_2118], output)
mutated_mod['func_2120'] = func_2120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1668_call = mod.get_global_var('func_1668')
func_1670_call = mutated_mod.get_global_var('func_1670')
call_2127 = func_1668_call()
call_2128 = func_1668_call()
uop_2158 = relay.log(call_2127.astype('float64')) # shape=(11, 10, 3)
uop_2160 = relay.log(call_2128.astype('float64')) # shape=(11, 10, 3)
output = uop_2158
output2 = uop_2160
func_2161 = relay.Function([], output)
mod['func_2161'] = func_2161
mod = relay.transform.InferType()(mod)
output = func_2161()
func_2162 = relay.Function([], output)
mutated_mod['func_2162'] = func_2162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_2212 = relay.TupleGetItem(func_1892_call(), 0)
call_2213 = relay.TupleGetItem(func_1894_call(), 0)
output = relay.Tuple([call_2212,])
output2 = relay.Tuple([call_2213,])
func_2218 = relay.Function([], output)
mod['func_2218'] = func_2218
mod = relay.transform.InferType()(mod)
mutated_mod['func_2218'] = func_2218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2218_call = mutated_mod.get_global_var('func_2218')
call_2219 = func_2218_call()
output = call_2219
func_2220 = relay.Function([], output)
mutated_mod['func_2220'] = func_2220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_2227 = relay.TupleGetItem(func_1892_call(), 0)
call_2228 = relay.TupleGetItem(func_1894_call(), 0)
uop_2229 = relay.asinh(call_2227.astype('float32')) # shape=(11, 10, 3)
uop_2231 = relay.asinh(call_2228.astype('float32')) # shape=(11, 10, 3)
func_2117_call = mod.get_global_var('func_2117')
func_2120_call = mutated_mod.get_global_var('func_2120')
const_2233 = relay.const([-10,-3,-3,-2,-6,-8,-8,-6,8,9,-8,6,-6,7,2,1,4,1,-10,-8,-4,3,-7,-7,5,-6,4,3,2,9,7,-6,-2,10,-1,-8,-7,1,10,-8,3,7,5,-7,-1,3,-4,9,-5,10,7,3,7,-9,-1,3,2,-5,-2,-6,-9,-3,7,1,-10,9,8,-5,-7,5,1,6,-10,2,3,6,-8,-5,2,-6,8,2,-1,-5,1,-8,8,10,5,9,-2,10,-6,5,-2,10,8,9,1,8,4,8,10,-9,10,10,4,1,4,8,7,-9,-2,-4,10,4,-8,7,10,10,5,3,-2,1,-10,-4,-9,-4,9,1,-2,5,-9,7,-8,1,-10,5,1,-8,7,10,6,6,-5,-7,3,-6,-6,-6,-1,2,-3,3,-4,-5,-4,-8,10,-8,-10,2,10,-10,3,3,-2,7,-1,-9,3,8,8,10,10,3,-2,5,-4,-10,-10,-1,7,10,-8,5,-3,-9,-10,9,4,10,-8,9,10,7,2,4,7,9,3,5,10,-6,-2,8,10,3,3,-8,-3,4,-6,-7,6,-6,-2,6,-6,2,-9,3,8,-7,-10,-7,3,-8,-4,2,3,-9,-1,-8,-7,-5,1,-8,-6,2,-2,-10,-2,4,5,4,-3,4,-7,-1,3,3,-1,-2,7,-2,-5,-4,3,3,-3,6,9,10,-10,-10,-4,-6,-7,-4,4,-3,-10,-8,-6,-9,-7,5,-4,-1,5,-9,8,5,-4,10,-5,-9,-4,8,-7,1,3,-1,2,-3,-5,7,6,9,-1,9,5,-10,6,-9,4,-8,-5,-4,-1,5,9,-1,3,6,10,9,5,4,-7,6,-10,-10,3,3,1,10,-9,-7,-1,-6,10,6,-7,9,-1,7,9,-10,1,6,1,-2,-7,3,-1,10,-4,-7,7,7,2,3,9,-4,7,2,6,-8,-2,2,10,5,8,-7,9,-5,5,-10,1,7,-4,6,3,-4,7,-8,-9,2,-4,-4,-10,4,9,4,-10,8,1,3,-1,1,-4,-4,-2,2,-3,9,-7,3,-6,6,7,9,1,4,-2,10,5,-9,-10,3,9,-9,4,2,8,-8,-5,4,3,-8,4,1,1,6,-2,5,10,8,7,-8,10,-9,-4,-1,-1,-4,-6,-4,-6,8,-9,7,-10,-5,-7,-1,8,-1,5,3,-8,2,-9,-3,-7,3,6,5,-7,3,5,10,-6,-8,-1,-8,6,-5,6,-2,-8,1,6,-10,-8,6,8,7,-5,6,5,-6,-2,10,8,-3,6,10,1,5,-4,-3,7,10,-6,-9,-8,4,6,2,-5,-8,-10,-2,-10,-10,-10,-9,-2,2,-5,9,-5,-5,-6,-5,-3,-1,-3,4,4,8,-5,-2,7,-7,4,-8,-8,2,-2,-2,-1,-8,7,-10,3,4,6,-9,1,-7,-9,-6,8,10,6,-4,6,-5,-3,-4,2,8,-6,-3,10,-4,5,-7,-9,-2,8,5,-10,-7,-5,3,8,7,8,-1,-2,-9,-6,-9,-1,9,10,3,4,7,2,-7,1,4,-6,8,-1,-4,-3,-1,7,-6,-6,7,1,-7,3,-3,10,4,4,3,-10,4,9,8,7,-2,-2,-1,4,4,-4,2,4,-9,1,-8,6,-2,7,-2,3,7,3,-6,8,4,9,-7,5,5,-7,-7,-5,9,-9,6,4,-7,1,-6,5,2,-8,-9,4,-9,7,3,4,-3,2,-5,5,7,-5,-7,-3,-6,-10,5,9,5,9,7,10,6,-1,2,3,4,-10,-10,-1,-5,-1,7,4,7,9,-7,-4,-5,-6,-3,-6,-8,-1,1,-5,5,9,-8,-3,6,-9,-5,6,1,6,-10,2,-1,8,-5,2,-1,-3,2,5,9,1,-8,3,6,3,4,-5,10,-8,-8,-6,-1,-9,-4,3,10,-7,-10,10,-10,3,2,-10,3,7,8,10,4,-4,-8,4,-10,10,1,-5,5,-6,6,-1,-4,10,-4,3,4,6,6,-9,1,4,9,7,-7,-5,9,-4,4,6,6,6,9,-1,-4,-1,10,-8,-7,7,8,-1,-5,9,-10,-7,-8,-6,5,-4,-8,5,-2,-8,-10,3,6,6,-8,1,1,6,-1,8,10,6,-7,-7,-5,-6,-2,4,2,9,4,9,10,-7,-8,8,5,7,6,-10,8,6,6,6,-10,9,-9,-1,6,3,-1,3,6], dtype = "uint8")#candidate|2233|(840,)|const|uint8
call_2232 = relay.TupleGetItem(func_2117_call(relay.reshape(const_2233.astype('uint8'), [840,])), 3)
call_2234 = relay.TupleGetItem(func_2120_call(relay.reshape(const_2233.astype('uint8'), [840,])), 3)
func_1825_call = mod.get_global_var('func_1825')
func_1828_call = mutated_mod.get_global_var('func_1828')
var_2236 = relay.var("var_2236", dtype = "bool", shape = (8, 30))#candidate|2236|(8, 30)|var|bool
call_2235 = relay.TupleGetItem(func_1825_call(relay.reshape(var_2236.astype('bool'), [8, 30])), 0)
call_2237 = relay.TupleGetItem(func_1828_call(relay.reshape(var_2236.astype('bool'), [8, 30])), 0)
uop_2240 = relay.cosh(uop_2229.astype('float64')) # shape=(11, 10, 3)
uop_2242 = relay.cosh(uop_2231.astype('float64')) # shape=(11, 10, 3)
uop_2248 = relay.log2(call_2235.astype('float64')) # shape=(7, 3, 15)
uop_2250 = relay.log2(call_2237.astype('float64')) # shape=(7, 3, 15)
output = relay.Tuple([call_2232,const_2233,var_2236,uop_2240,uop_2248,])
output2 = relay.Tuple([call_2234,const_2233,var_2236,uop_2242,uop_2250,])
func_2253 = relay.Function([var_2236,], output)
mod['func_2253'] = func_2253
mod = relay.transform.InferType()(mod)
var_2254 = relay.var("var_2254", dtype = "bool", shape = (8, 30))#candidate|2254|(8, 30)|var|bool
output = func_2253(var_2254)
func_2255 = relay.Function([var_2254], output)
mutated_mod['func_2255'] = func_2255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1668_call = mod.get_global_var('func_1668')
func_1670_call = mutated_mod.get_global_var('func_1670')
call_2259 = func_1668_call()
call_2260 = func_1668_call()
func_2253_call = mod.get_global_var('func_2253')
func_2255_call = mutated_mod.get_global_var('func_2255')
var_2267 = relay.var("var_2267", dtype = "bool", shape = (240,))#candidate|2267|(240,)|var|bool
call_2266 = relay.TupleGetItem(func_2253_call(relay.reshape(var_2267.astype('bool'), [8, 30])), 3)
call_2268 = relay.TupleGetItem(func_2255_call(relay.reshape(var_2267.astype('bool'), [8, 30])), 3)
func_1418_call = mod.get_global_var('func_1418')
func_1421_call = mutated_mod.get_global_var('func_1421')
const_2272 = relay.const([6,9,-10,8,-5,-9,2,-9,7,-10,3,5,-6,9,-5,-2,-6,10,5,-2,-3,-5,-2,5,-4,-6,-6,2,10,-5,-6,8,2,-1,-10,-9,-6,7,9,-1,6,1,10,5,5,-7,-1,-6,-6,9,-10,8,-5,5,-6,6,-6,3,10,-8,-10,-7,-3,-3,8,5,-4,-5,8,2,10,6,-7,-4,9,-2,-6,-3,2,7,1,9,3,-4,-7,6,8,-3,-3,10,8,4,-10,2,2,-1,9,8,-5,-4,-1,-10,-2,-2,10,6,5,-2,6,7,1,-1,-8,-4,-1,7,-9,-3,-10,4,10,-7,-2,9,1,4,-4,6,-3,-6,1,10,-10,10,9,-9,-6,3,-5,3,-8,10,3,-5,6,-3,-7,-6,-6,-7,10,6,-4,5,-3,5,-7,-5,-1,-7,2,-6,2,7,8,-5,-2,6,3,-5,-10,-8,-7,7,3,-7,-3,5,-6,-3,6,3,-2,6,-2,2,3,-9,4,10,-8,-2,1,6,10,10,-1,6,5,9,-4,9,2,10,4,3,7,4,-3,-5,-2,-8,9,-6,-7,2,-7,-1,-9,-5,10,-6,3,5,2,10,-5,7,-4,10,2,-5,5,10,-6,8,2,1,5,3,5,1,2,4,5,-7,6,-5,-7,-6,9,9,9,9,7,1,-3,-2,4,-1,9,-5,-2,-7,-7,-4,-8,-10,-2,-1,10,10,8,-8,-7,-1,-9,-3,-1,1,-5,6,7,-10,-4,-9,3,-8,3,-3,-7,7,5,8,-2,5,6,-1,-7,4,-2,-6,2,7,-9,6,-9,3,-2,-1,10,4,-9,-10,5,-10,5,-1,-1,4,1,8,-2,-3,10,1,-9,-7,-9,7,-1,1,2,-4,-10,-4,10,-10,-3,-9,6,4,-6,-4,-9,10,-7,-5,3,-5,-10,6,1,2,-9,-8,2,10,6,-2,-6,-7,3,5,3,-1,-7,3,-2,-5,-6,8,6,6,4,6,-2,7,5,1,10,-1,8,-6,-10,3,-3,-4,9,-10,1,6,-9,9,3,-1,2,9,-7,10,7,3,-6,-8,8,9,3,1,8,-5,-9,-1,10,3,-8,-3,8,-4,3,-9,-9,-10,-4,4,2,3,8,4,-6,5,2,9,-6,-4,5,1,4,8,-2,-1,4,6,8,1,-9,-9,6,2,-1,2,2,1,5,-5,4,3,-10,1,1,5,8,-2,2,-8,-10,10,-4,-9,4,9,-2,7,3,1,2,5,-9,-4,-3,-3,-3,-7,8,9,2,10,-10,5,5,-9,-1,6,-3,1,5,9,9,-6,-1,-8,2,-4,-5,8,-6,-8,3,-9,6,-2,-3,10,6,10,-2,-10,-6,-1,-5,10,5,-8,-2,7,-6,1,-2,5,1,-5,4,9,10,-9,-8,6,-7,-4,-3,10,-9,-1,4,-9,9,-7,-9,-3,8,-4,10,-2,6,9,8,-9,10,8,-3,-8,10,7,2,10,1,6,4,10,7,-9,1,-2,7,-5,-8,5,6,9,2,-8,3,-4,-4,-9,6,-4,6,-7,7,-3,5,-4,10,1,-3,4,-2,7,5,-7,-5,-9,10,-4,-10,-1,-7,-7,8,-8,6,-9,2,-6,-3,1,7,-9,-8,3,1,2,-1,-4,7,-2,-6,3,8,-9,4,6,-2,8,9,-9,-9,6,-1,1,-2,1,5,-10,-3,3,-8,9,-6,-3,10,5,4,9,2,3,2,-4,8,-1,2,6,-5,-4,-2,7,-9,-1,-4,8,10,-1,-3,-3,-10,2,8,-4,3,-5,-4,-10,5,-4,2,6,-1,-8,4,7,-6,6,7,9,5,-8,8,-2,9,-3,-7,-5,-6,7,2,1,-3,2,-6,-1,-4,-2,6,5,-9,6,-7,-6,-4,2,7,2,2,-1,6,9,-2,2,4,-3,6,-9,-2,6,6,-2,3,4,-9,-4,-6,4,-6,5,-4,1,10,2,4,10,6,-4,5,4,10,8,3,-1,-8,8,-7,-1,10,-10,1,-4,-9,8,4,-9,-2,-10,9,-3,-10,-9,2,3,-3,-4,-3,3,-7,-10,-5,-5,6,-1,9,-1,6,7,8,-10,4,-5,-4,-3,-9,10,-1,-8,-2,-1,-6,-1,2,2,9,1,8,2,-4,1,-7,-7,9,5,-6,-4,9,-7,-5,-3,3,-8,1,2,-7,1,7,-2,3,8,4,-4,-7,-5,1,7], dtype = "uint8")#candidate|2272|(840,)|const|uint8
call_2271 = func_1418_call(relay.reshape(const_2272.astype('uint8'), [4, 15, 14]))
call_2273 = func_1418_call(relay.reshape(const_2272.astype('uint8'), [4, 15, 14]))
output = relay.Tuple([call_2259,call_2266,var_2267,call_2271,const_2272,])
output2 = relay.Tuple([call_2260,call_2268,var_2267,call_2273,const_2272,])
func_2274 = relay.Function([var_2267,], output)
mod['func_2274'] = func_2274
mod = relay.transform.InferType()(mod)
var_2275 = relay.var("var_2275", dtype = "bool", shape = (240,))#candidate|2275|(240,)|var|bool
output = func_2274(var_2275)
func_2276 = relay.Function([var_2275], output)
mutated_mod['func_2276'] = func_2276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1668_call = mod.get_global_var('func_1668')
func_1670_call = mutated_mod.get_global_var('func_1670')
call_2295 = func_1668_call()
call_2296 = func_1668_call()
func_1924_call = mod.get_global_var('func_1924')
func_1928_call = mutated_mod.get_global_var('func_1928')
const_2308 = relay.const([8.256621,-1.356276,-4.781049,8.898407,-6.923117,-9.781771,0.166925,-3.003043,-1.091566,1.652598,-1.583714,-6.886771,-2.551156,7.438362,0.045474,-3.280183,6.881651,2.999581,7.336329,-3.743118,0.748288,7.049404,-1.693217,-2.851700,-4.512610,0.014848,7.960635,0.981648,-3.635487,0.330176,-4.467705,-5.800444,-4.654169,9.605031,3.519804,-1.065079,-6.018216,5.514746,5.951988,-6.163163,3.991417,-7.910177,9.401058,8.607145,-6.120863,8.611367,-2.571193,-6.943699,-2.667500,-7.775686,4.972375,-9.248418,-1.988628,-6.217395,-9.993718,3.112379,8.292979,-3.268606,4.700703,-7.510943,-0.373531,3.513370,-1.604738,-9.644162,3.863204,-0.329485,5.964257,9.364383,-0.414766,2.150159,-1.637125,9.737181,-9.890635,-6.162358,5.234301,8.837390,2.342597,-8.544175,4.045326,-6.577540,0.766804,2.945525,5.445803,-9.152032,1.325449,-3.854154,1.147822,3.836331,7.489717,0.726215,-0.421173,1.447696,3.039941,1.388998,-7.322595,-1.500355,-7.752067,-7.188936,-9.411882,-9.749785,-6.349161,4.792244,-1.287302,6.680471,-8.605976,-3.001559,4.035879,-6.881631,9.415437,0.396903,7.408261,3.605687,-9.334159,-0.065223,-5.156780,-9.613846,5.321794,-2.792461,-1.508317,-8.185572,0.210287,2.150009,-5.010459,9.611636,-6.104570,0.922419,-8.967527,3.913783,-0.304125,1.414173,-8.468733,7.880076,0.083148,3.768544,8.077590,2.012103,-5.093053,6.166595,-6.221357,-7.820214,-0.616643,6.350496,-1.379346,5.430729,-7.736598,-5.548404,-0.905071,-4.246444,6.827556,3.510631,0.780364,1.160983,5.465737,-8.771685,-1.621792,-6.644049,-4.847326,5.835408,0.437295,5.055611,-8.788105,-5.759105,2.952255,-1.601081,6.213660,2.812021,-5.102370,-1.410366,-6.363606,-1.355692,-9.288124,6.596715,-4.020908,9.087354,8.305917,8.600041,-2.491031,-1.015171,-1.036590,7.339367,-6.040720,1.210763,1.479400,-5.182397,-0.812018,-9.331175,-9.590934,-1.294363,8.447590,-5.134125,-1.114378,-9.140081,6.041726,2.913369,5.867853,0.674804,1.626891,1.710895,0.091751,-2.434128,-7.900018,-4.503165,-8.408457,2.363908,-8.476306,-5.918150,7.650368,-1.689864,9.838301,-7.677307,-1.239767,-4.662589,-6.403687,-6.875208,-9.455204,-1.376442,-6.963722,0.406308,7.198373,-3.150759,-3.736547,-4.526563,0.041108,-4.849117,-2.181127,7.043171,6.685958,0.044727,1.616909,9.258971,-1.634785,-5.368271,-5.393605,-2.265810,-4.164042,9.420312,0.552821,-2.075573,-2.718109,-1.293513,-3.393153,1.511255,2.480029,1.953149,1.151689,-2.952052,-9.239034,-8.435390,-5.728467,-6.444466,4.211326,8.438972,-0.460948,8.201204,5.257128,7.069926,8.895715,1.594705,9.086299,-1.890792,8.212515,3.108937,6.078472,-0.148141,-2.754426,2.980548,-6.897158,-8.406311,-6.592659,-7.880992,9.565448,9.099464,-1.750292,-9.305408,-1.613989,-1.949446,3.363443,4.742294,3.303913,7.026084,4.784398,8.722652,1.222092,-4.924136,8.710545,2.403954,-7.764456,-3.854601,6.025394,9.418037,0.592859,4.482798,0.169560,5.264381,-1.909623,-7.605177,5.796257,-2.898858,8.545069,6.437279,3.452876,-8.563596,6.760334,-3.641803,3.664456,-0.537826,-2.482691,3.588318,1.232774,-1.085548,5.242520,2.797592,3.399622,-3.843155,-0.842297], dtype = "float64")#candidate|2308|(315,)|const|float64
const_2309 = relay.const([[2,-5,7,7,8,6,-9,-8,-3,-7],[2,2,-9,-4,4,-5,9,-9,8,10],[2,-1,-4,-3,-1,8,4,1,-8,10],[-10,10,7,-6,5,-2,3,-10,-2,5],[-3,7,4,5,-4,6,10,-3,-5,-1],[-6,-9,-8,-5,-4,-2,-5,8,-10,1],[-6,9,-1,2,-1,8,7,8,6,4],[6,-7,-8,8,8,1,6,-9,-2,5],[-5,3,-8,-7,-6,2,-8,1,-6,5],[8,-7,6,1,6,-5,9,-10,1,-1],[10,-7,4,6,6,-3,7,-9,3,-5],[8,-9,8,-3,-9,-3,8,9,9,4],[-9,10,-7,3,10,1,5,-4,1,1],[-2,1,6,3,-9,9,-6,-6,-9,-6],[-4,-9,-9,4,-10,2,-9,3,-6,1],[5,-3,-10,-7,7,-1,10,-2,3,-3],[-10,5,9,-5,4,2,7,-4,4,7],[3,-2,8,-6,-9,1,3,9,6,8],[-1,1,8,4,-7,3,10,4,1,-6],[8,-8,-7,-4,-2,-3,5,-10,9,4],[6,5,7,6,1,8,3,-2,-4,1],[3,6,8,-10,1,-3,3,5,-9,-8],[4,2,2,6,-2,-10,1,-2,4,-7],[10,-2,-10,-3,-9,-9,-6,8,7,-4]], dtype = "uint64")#candidate|2309|(24, 10)|const|uint64
call_2307 = relay.TupleGetItem(func_1924_call(relay.reshape(const_2308.astype('float64'), [315, 1]), relay.reshape(const_2309.astype('uint64'), [240,]), ), 1)
call_2310 = relay.TupleGetItem(func_1928_call(relay.reshape(const_2308.astype('float64'), [315, 1]), relay.reshape(const_2309.astype('uint64'), [240,]), ), 1)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2318 = func_2059_call()
call_2319 = func_2059_call()
uop_2322 = relay.log(const_2309.astype('float64')) # shape=(24, 10)
var_2324 = relay.var("var_2324", dtype = "float64", shape = (24, 10))#candidate|2324|(24, 10)|var|float64
bop_2325 = relay.mod(uop_2322.astype('float64'), relay.reshape(var_2324.astype('float64'), relay.shape_of(uop_2322))) # shape=(24, 10)
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
call_2328 = relay.TupleGetItem(func_1626_call(), 2)
call_2329 = relay.TupleGetItem(func_1628_call(), 2)
uop_2346 = relay.cosh(bop_2325.astype('float64')) # shape=(24, 10)
bop_2358 = relay.maximum(uop_2346.astype('float64'), relay.reshape(bop_2325.astype('float64'), relay.shape_of(uop_2346))) # shape=(24, 10)
output = relay.Tuple([call_2295,call_2307,const_2308,call_2318,call_2328,bop_2358,])
output2 = relay.Tuple([call_2296,call_2310,const_2308,call_2319,call_2329,bop_2358,])
func_2365 = relay.Function([var_2324,], output)
mod['func_2365'] = func_2365
mod = relay.transform.InferType()(mod)
var_2366 = relay.var("var_2366", dtype = "float64", shape = (24, 10))#candidate|2366|(24, 10)|var|float64
output = func_2365(var_2366)
func_2367 = relay.Function([var_2366], output)
mutated_mod['func_2367'] = func_2367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_2380 = relay.TupleGetItem(func_1892_call(), 1)
call_2381 = relay.TupleGetItem(func_1894_call(), 1)
output = call_2380
output2 = call_2381
func_2382 = relay.Function([], output)
mod['func_2382'] = func_2382
mod = relay.transform.InferType()(mod)
mutated_mod['func_2382'] = func_2382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2382_call = mutated_mod.get_global_var('func_2382')
call_2383 = func_2382_call()
output = call_2383
func_2384 = relay.Function([], output)
mutated_mod['func_2384'] = func_2384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2401 = func_2059_call()
call_2402 = func_2059_call()
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2403 = func_2059_call()
call_2404 = func_2059_call()
output = relay.Tuple([call_2401,call_2403,])
output2 = relay.Tuple([call_2402,call_2404,])
func_2410 = relay.Function([], output)
mod['func_2410'] = func_2410
mod = relay.transform.InferType()(mod)
output = func_2410()
func_2411 = relay.Function([], output)
mutated_mod['func_2411'] = func_2411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2429 = func_2059_call()
call_2430 = func_2059_call()
output = relay.Tuple([call_2429,])
output2 = relay.Tuple([call_2430,])
func_2431 = relay.Function([], output)
mod['func_2431'] = func_2431
mod = relay.transform.InferType()(mod)
mutated_mod['func_2431'] = func_2431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2431_call = mutated_mod.get_global_var('func_2431')
call_2432 = func_2431_call()
output = call_2432
func_2433 = relay.Function([], output)
mutated_mod['func_2433'] = func_2433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1866_call = mutated_mod.get_global_var('func_1866')
call_2489 = relay.TupleGetItem(func_1864_call(), 0)
call_2490 = relay.TupleGetItem(func_1866_call(), 0)
output = call_2489
output2 = call_2490
func_2495 = relay.Function([], output)
mod['func_2495'] = func_2495
mod = relay.transform.InferType()(mod)
mutated_mod['func_2495'] = func_2495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2495_call = mutated_mod.get_global_var('func_2495')
call_2496 = func_2495_call()
output = call_2496
func_2497 = relay.Function([], output)
mutated_mod['func_2497'] = func_2497
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2501 = relay.const([[[False,True,False],[True,True,False],[False,False,False]],[[False,True,True],[False,True,False],[False,True,False]],[[False,False,True],[False,True,True],[True,False,True]],[[True,False,True],[True,False,True],[True,True,False]],[[False,True,False],[False,True,True],[True,True,False]],[[True,True,False],[True,True,False],[False,True,False]],[[False,False,False],[True,False,False],[False,True,False]],[[True,True,True],[True,True,False],[True,True,True]],[[False,False,False],[True,True,True],[True,False,False]],[[True,False,False],[True,False,False],[True,True,False]],[[True,False,False],[True,True,True],[False,True,False]]], dtype = "bool")#candidate|2501|(11, 3, 3)|const|bool
var_2502 = relay.var("var_2502", dtype = "bool", shape = (11, 3, 3))#candidate|2502|(11, 3, 3)|var|bool
bop_2503 = relay.logical_and(const_2501.astype('bool'), relay.reshape(var_2502.astype('bool'), relay.shape_of(const_2501))) # shape=(11, 3, 3)
output = relay.Tuple([bop_2503,])
output2 = relay.Tuple([bop_2503,])
func_2512 = relay.Function([var_2502,], output)
mod['func_2512'] = func_2512
mod = relay.transform.InferType()(mod)
mutated_mod['func_2512'] = func_2512
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2513 = relay.var("var_2513", dtype = "bool", shape = (11, 3, 3))#candidate|2513|(11, 3, 3)|var|bool
func_2512_call = mutated_mod.get_global_var('func_2512')
call_2514 = func_2512_call(var_2513)
output = call_2514
func_2515 = relay.Function([var_2513], output)
mutated_mod['func_2515'] = func_2515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
call_2558 = func_2495_call()
call_2559 = func_2495_call()
output = call_2558
output2 = call_2559
func_2578 = relay.Function([], output)
mod['func_2578'] = func_2578
mod = relay.transform.InferType()(mod)
mutated_mod['func_2578'] = func_2578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2578_call = mutated_mod.get_global_var('func_2578')
call_2579 = func_2578_call()
output = call_2579
func_2580 = relay.Function([], output)
mutated_mod['func_2580'] = func_2580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2028_call = mutated_mod.get_global_var('func_2028')
call_2586 = func_2027_call()
call_2587 = func_2027_call()
output = relay.Tuple([call_2586,])
output2 = relay.Tuple([call_2587,])
func_2604 = relay.Function([], output)
mod['func_2604'] = func_2604
mod = relay.transform.InferType()(mod)
mutated_mod['func_2604'] = func_2604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2604_call = mutated_mod.get_global_var('func_2604')
call_2605 = func_2604_call()
output = call_2605
func_2606 = relay.Function([], output)
mutated_mod['func_2606'] = func_2606
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2645 = relay.const([[[-2.444634,9.135889,-7.791898,-5.393334,-2.666650],[4.377851,-1.222317,-0.142876,-7.695218,-2.643721],[-9.812211,5.703942,8.052253,5.851190,8.385294],[-9.006367,2.427981,1.104916,6.739298,4.156090],[9.727783,5.855641,8.644129,6.464907,4.045391],[-9.204699,-9.863824,4.851067,3.124936,-7.087526],[0.857858,-1.191977,-6.215643,-0.877820,-6.796333],[9.882579,-1.829365,5.176363,3.948778,-4.053851],[-7.904118,-8.347577,-1.628887,-4.316233,4.410174],[-6.922934,1.922069,7.114718,-4.340854,-0.419610]],[[5.922293,0.741304,-2.499825,4.177622,1.089496],[-7.587101,-2.375553,-0.828696,-6.995397,-3.620447],[7.181587,5.478789,2.419359,-6.164009,-9.012456],[-1.091445,5.064839,-3.622940,-4.232140,0.001976],[8.209626,3.980076,-4.807347,-6.096279,-7.144036],[-0.304682,-0.553736,7.415419,-9.750202,5.295951],[-6.268594,-1.488061,2.532207,6.688614,-0.471538],[1.626639,-9.446992,2.742483,-7.494291,9.824119],[-0.750523,-4.733432,7.684180,9.645327,-8.920691],[7.714420,-3.715207,-0.282453,-3.453168,-9.993311]],[[-6.499863,-3.590100,-8.260120,8.763154,8.798264],[-9.869056,5.498925,-5.413122,-6.488347,-1.055555],[3.151509,6.483512,-0.314393,8.433129,0.715844],[9.846637,-3.935435,-6.847718,-1.176676,6.930928],[-3.604078,5.121312,4.610400,6.315380,6.239526],[-7.585086,5.260079,2.571252,6.136053,-4.388536],[-0.324388,-0.182993,9.315573,3.416226,-1.369582],[1.540577,-4.956041,-6.534380,4.260355,3.742010],[-9.841643,6.086173,8.120147,5.395059,3.140108],[4.253715,4.202071,-3.956917,-3.693964,-4.153838]],[[0.873603,-5.723340,7.052838,5.539306,-4.762140],[1.769787,-1.098378,-2.894909,8.014653,-3.369695],[5.104358,-1.196292,1.616023,2.236706,6.546235],[-9.090476,3.603349,-8.789211,-9.050344,5.215880],[8.182378,2.996038,5.428331,2.522660,5.278996],[-7.439481,-6.914091,7.759715,5.539485,4.442926],[1.954434,0.261102,-6.939212,5.383235,8.137018],[6.458267,7.741485,-5.592012,-9.076573,-8.338606],[3.797085,-8.634003,4.400232,5.964053,-8.074580],[5.349209,0.695204,9.470964,8.963940,-9.506929]],[[6.599161,6.152314,-0.596913,-6.060110,2.878514],[-3.225644,6.854625,-7.228762,-3.832246,0.990062],[6.073548,-7.174056,-6.546408,-6.375642,-2.160014],[-7.856944,1.678496,1.323137,-3.317316,-3.994011],[-3.040677,-6.958460,-2.768952,-6.439485,8.021752],[0.072809,7.946813,2.207474,6.854150,2.603614],[-8.649849,-0.133098,6.667018,9.998864,8.208663],[7.085530,-4.623022,2.555324,5.760936,7.695806],[1.462259,5.673823,3.039461,-6.531916,-1.452125],[-3.666716,-8.165417,-4.443369,-6.464712,4.914568]],[[-0.098308,7.965981,-5.219036,6.923745,9.524510],[-4.416183,6.106395,4.579244,-8.660190,-9.649602],[6.514756,4.004339,9.582181,6.988313,2.516474],[6.748226,5.570427,-9.287339,9.153632,6.135621],[5.571574,5.550635,5.232418,1.520590,3.148164],[5.380545,-0.394830,-1.711344,-8.290666,-8.925949],[-9.895086,7.682505,-1.457693,9.752800,7.569568],[-8.051290,3.276210,-5.564137,-9.466758,-9.489599],[3.062247,-6.932750,5.490098,0.319773,-1.329830],[1.207894,4.053815,9.355253,2.779280,8.607404]],[[8.821858,6.248142,6.869139,-3.673800,2.995248],[4.464479,-3.413049,-3.209411,-5.489102,2.281868],[7.766681,5.366336,-4.253344,9.369080,-1.482043],[-8.152583,-6.973203,-0.701761,9.257411,-2.508212],[1.124186,1.593236,6.741484,0.889806,3.849141],[2.032328,-2.096290,5.590716,2.999025,-8.270814],[9.266285,4.769597,-8.521723,-7.952470,-2.335934],[-0.757430,-2.152188,3.675660,1.012510,-3.863426],[-1.873578,-2.581654,-3.782785,1.985672,-8.630541],[0.139997,-5.509831,6.735561,-3.514479,9.540794]],[[-2.847425,0.028245,2.756034,6.798467,1.526494],[-4.607212,1.532912,-3.179524,-7.841174,7.764378],[6.928685,2.989540,4.808215,-9.440710,-4.552445],[2.334709,1.701607,8.065299,0.945000,-2.620488],[-9.958327,-4.458009,1.517887,-5.042060,-6.948316],[-0.209115,-5.181665,-0.394924,-4.830804,-0.372169],[-1.984648,-8.792922,-9.782666,-3.461608,-1.729566],[-9.934277,3.517435,-5.252300,-8.903575,7.209472],[-4.957108,-7.385926,5.681356,-1.167638,-4.685703],[-0.708488,-1.305079,-1.332766,-0.751182,2.712686]],[[1.532600,-8.701111,-6.134502,3.050142,0.757707],[-1.465983,-1.857839,-3.559771,4.496392,-0.658130],[8.747192,-0.692770,3.597337,-2.462055,7.370394],[-4.580268,-6.210504,-6.550561,8.049058,3.234792],[-4.252611,-0.225813,-2.153981,-0.692486,9.585697],[3.082556,3.652285,0.094426,2.242859,-6.354760],[0.584669,1.108729,1.163338,-2.241659,-2.051085],[4.031383,1.064750,4.575863,7.993102,2.040869],[-5.909508,2.934727,-5.467029,-3.988563,9.999504],[0.561293,7.488577,-6.785782,-7.804827,6.966794]],[[-6.290365,5.122708,-1.807499,9.601400,-6.906363],[5.874036,-0.632298,-8.318546,2.215595,-6.412943],[0.029690,3.965901,-6.974205,-3.454673,-7.869775],[6.566209,-8.855379,7.181045,-7.589331,-3.669779],[6.365140,1.689296,1.828819,9.927622,4.129798],[9.441193,4.306977,4.090268,-2.709182,-7.827545],[-3.988244,9.511409,-0.954183,0.553422,4.350131],[2.213502,9.603662,-7.444567,-4.341797,4.509733],[7.049292,-5.767058,3.028461,2.508448,6.773703],[7.826885,2.881764,9.948931,3.060760,-6.649898]],[[-3.672826,6.572297,8.315689,-5.555275,5.677991],[7.544936,-2.653714,6.762019,4.636997,8.659049],[-6.013886,-3.715290,2.533826,3.369571,4.008598],[-3.016772,8.515321,2.042227,5.640565,-1.499176],[-5.696429,-4.853423,-8.906226,-1.445446,-0.928882],[-0.378531,-9.860631,-3.388960,-7.667528,-2.667502],[-1.976886,-1.893831,2.529278,-0.088291,6.548665],[4.920255,-4.842636,7.052318,-4.202856,-0.141176],[1.007209,7.744896,-6.212379,-8.306436,-7.908890],[-3.101042,9.207962,-7.244953,-5.968226,1.388242]],[[-9.388012,7.105708,-2.004134,3.631021,2.408786],[5.121685,-5.875722,-2.542363,1.707004,-3.346476],[-2.561054,-9.473917,8.091353,-1.600329,6.358795],[3.232453,-8.448254,-2.223753,1.975260,1.893340],[5.545234,-5.935086,-9.034739,-3.396419,6.725648],[6.065218,4.433582,1.867698,-3.844208,4.404548],[9.669505,0.139395,6.931545,9.055253,6.591606],[1.774283,0.002360,7.257599,8.963555,7.501822],[-9.883063,-7.740450,-4.157274,-6.079413,0.862902],[-9.822264,-5.394749,-8.933860,6.699817,2.978116]],[[6.976200,-7.050984,-3.256241,-4.986859,3.626759],[-1.008750,-5.787603,-2.532044,-4.062980,2.354308],[-5.433725,-8.976004,-4.786681,-3.365092,-8.838296],[-6.647017,5.667294,3.558934,-4.225671,6.787485],[2.205935,2.549949,-1.126122,8.977584,-8.293554],[-5.991477,-1.520317,-0.551522,0.915337,2.200602],[-4.716130,9.902150,-5.449496,5.953366,-6.579809],[-7.325582,-2.309215,0.296127,6.128592,1.723772],[-2.512156,-8.467779,-8.155843,7.577804,-4.880536],[-9.325985,-1.562986,-6.470805,-2.894027,-8.526176]],[[-3.037760,-6.083359,-7.985871,2.342233,-1.203353],[-6.059553,-7.900993,-9.759596,1.888824,-9.106835],[-4.125798,-4.979435,5.239073,7.014235,-1.233232],[-8.196335,-5.870535,9.143554,9.978502,5.946616],[3.917431,-6.983365,-7.841447,-2.441119,-2.596554],[9.147330,4.287829,1.158875,-6.155400,-0.644910],[-8.746658,2.735785,-5.098927,-3.599548,2.086382],[1.437255,9.311305,-2.709314,-7.306574,3.753615],[-0.849856,5.340389,-7.370731,-3.390684,8.767188],[4.409618,8.842686,5.057018,7.172274,6.442884]],[[4.636784,1.160515,-1.886343,-6.444005,-0.864096],[4.612156,0.308673,8.487420,-3.382479,-8.761356],[-3.773463,6.183087,8.389255,3.690331,-9.883591],[3.310021,-0.182723,-0.967387,4.554294,4.302043],[-8.328967,-2.603455,-5.175893,7.465060,0.148430],[-7.966740,7.185395,9.763740,-4.160366,5.574494],[-5.569099,-5.687343,4.998496,0.355903,-4.130712],[9.521713,-6.782586,-3.280038,0.919037,4.723229],[7.165243,-5.094649,5.449914,0.530334,4.622796],[9.469044,-8.901179,-9.618686,-9.529261,-7.642248]]], dtype = "float32")#candidate|2645|(15, 10, 5)|const|float32
uop_2646 = relay.atanh(const_2645.astype('float32')) # shape=(15, 10, 5)
bop_2648 = relay.equal(const_2645.astype('bool'), relay.reshape(uop_2646.astype('bool'), relay.shape_of(const_2645))) # shape=(15, 10, 5)
func_2027_call = mod.get_global_var('func_2027')
func_2028_call = mutated_mod.get_global_var('func_2028')
call_2653 = func_2027_call()
call_2654 = func_2027_call()
bop_2663 = relay.bitwise_xor(bop_2648.astype('uint8'), relay.reshape(uop_2646.astype('uint8'), relay.shape_of(bop_2648))) # shape=(15, 10, 5)
uop_2679 = relay.erf(bop_2663.astype('float32')) # shape=(15, 10, 5)
bop_2692 = relay.mod(uop_2679.astype('float64'), relay.reshape(bop_2648.astype('float64'), relay.shape_of(uop_2679))) # shape=(15, 10, 5)
var_2701 = relay.var("var_2701", dtype = "float64", shape = (15, 10, 5))#candidate|2701|(15, 10, 5)|var|float64
bop_2702 = relay.right_shift(bop_2692.astype('uint16'), relay.reshape(var_2701.astype('uint16'), relay.shape_of(bop_2692))) # shape=(15, 10, 5)
func_1825_call = mod.get_global_var('func_1825')
func_1828_call = mutated_mod.get_global_var('func_1828')
var_2707 = relay.var("var_2707", dtype = "bool", shape = (240,))#candidate|2707|(240,)|var|bool
call_2706 = relay.TupleGetItem(func_1825_call(relay.reshape(var_2707.astype('bool'), [8, 30])), 7)
call_2708 = relay.TupleGetItem(func_1828_call(relay.reshape(var_2707.astype('bool'), [8, 30])), 7)
output = relay.Tuple([call_2653,bop_2702,call_2706,var_2707,])
output2 = relay.Tuple([call_2654,bop_2702,call_2708,var_2707,])
func_2713 = relay.Function([var_2701,var_2707,], output)
mod['func_2713'] = func_2713
mod = relay.transform.InferType()(mod)
mutated_mod['func_2713'] = func_2713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2713_call = mutated_mod.get_global_var('func_2713')
var_2715 = relay.var("var_2715", dtype = "float64", shape = (15, 10, 5))#candidate|2715|(15, 10, 5)|var|float64
var_2716 = relay.var("var_2716", dtype = "bool", shape = (240,))#candidate|2716|(240,)|var|bool
call_2714 = func_2713_call(var_2715,var_2716,)
output = call_2714
func_2717 = relay.Function([var_2715,var_2716,], output)
mutated_mod['func_2717'] = func_2717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mod.get_global_var('func_2410')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_2846 = relay.TupleGetItem(func_2410_call(), 0)
call_2847 = relay.TupleGetItem(func_2411_call(), 0)
output = call_2846
output2 = call_2847
func_2853 = relay.Function([], output)
mod['func_2853'] = func_2853
mod = relay.transform.InferType()(mod)
output = func_2853()
func_2854 = relay.Function([], output)
mutated_mod['func_2854'] = func_2854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2431_call = mod.get_global_var('func_2431')
func_2433_call = mutated_mod.get_global_var('func_2433')
call_2936 = relay.TupleGetItem(func_2431_call(), 0)
call_2937 = relay.TupleGetItem(func_2433_call(), 0)
output = call_2936
output2 = call_2937
func_2948 = relay.Function([], output)
mod['func_2948'] = func_2948
mod = relay.transform.InferType()(mod)
output = func_2948()
func_2949 = relay.Function([], output)
mutated_mod['func_2949'] = func_2949
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2962 = relay.var("var_2962", dtype = "int8", shape = (9, 8, 16))#candidate|2962|(9, 8, 16)|var|int8
var_2963 = relay.var("var_2963", dtype = "int8", shape = (9, 8, 16))#candidate|2963|(9, 8, 16)|var|int8
bop_2964 = relay.bitwise_or(var_2962.astype('int8'), relay.reshape(var_2963.astype('int8'), relay.shape_of(var_2962))) # shape=(9, 8, 16)
bop_2979 = relay.subtract(var_2963.astype('float32'), relay.reshape(bop_2964.astype('float32'), relay.shape_of(var_2963))) # shape=(9, 8, 16)
output = bop_2979
output2 = bop_2979
func_2982 = relay.Function([var_2962,var_2963,], output)
mod['func_2982'] = func_2982
mod = relay.transform.InferType()(mod)
var_2983 = relay.var("var_2983", dtype = "int8", shape = (9, 8, 16))#candidate|2983|(9, 8, 16)|var|int8
var_2984 = relay.var("var_2984", dtype = "int8", shape = (9, 8, 16))#candidate|2984|(9, 8, 16)|var|int8
output = func_2982(var_2983,var_2984,)
func_2985 = relay.Function([var_2983,var_2984,], output)
mutated_mod['func_2985'] = func_2985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
call_3041 = func_2495_call()
call_3042 = func_2495_call()
output = call_3041
output2 = call_3042
func_3043 = relay.Function([], output)
mod['func_3043'] = func_3043
mod = relay.transform.InferType()(mod)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3043_call = mutated_mod.get_global_var('func_3043')
call_3044 = func_3043_call()
output = call_3044
func_3045 = relay.Function([], output)
mutated_mod['func_3045'] = func_3045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2948_call = mod.get_global_var('func_2948')
func_2949_call = mutated_mod.get_global_var('func_2949')
call_3066 = func_2948_call()
call_3067 = func_2948_call()
var_3077 = relay.var("var_3077", dtype = "float32", shape = (11, 10, 3))#candidate|3077|(11, 10, 3)|var|float32
bop_3078 = relay.maximum(call_3066.astype('uint32'), relay.reshape(var_3077.astype('uint32'), relay.shape_of(call_3066))) # shape=(11, 10, 3)
bop_3081 = relay.maximum(call_3067.astype('uint32'), relay.reshape(var_3077.astype('uint32'), relay.shape_of(call_3067))) # shape=(11, 10, 3)
bop_3085 = relay.divide(bop_3078.astype('float64'), relay.reshape(var_3077.astype('float64'), relay.shape_of(bop_3078))) # shape=(11, 10, 3)
bop_3088 = relay.divide(bop_3081.astype('float64'), relay.reshape(var_3077.astype('float64'), relay.shape_of(bop_3081))) # shape=(11, 10, 3)
output = relay.Tuple([bop_3085,])
output2 = relay.Tuple([bop_3088,])
func_3099 = relay.Function([var_3077,], output)
mod['func_3099'] = func_3099
mod = relay.transform.InferType()(mod)
var_3100 = relay.var("var_3100", dtype = "float32", shape = (11, 10, 3))#candidate|3100|(11, 10, 3)|var|float32
output = func_3099(var_3100)
func_3101 = relay.Function([var_3100], output)
mutated_mod['func_3101'] = func_3101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2028_call = mutated_mod.get_global_var('func_2028')
call_3121 = func_2027_call()
call_3122 = func_2027_call()
func_1272_call = mod.get_global_var('func_1272')
func_1276_call = mutated_mod.get_global_var('func_1276')
var_3133 = relay.var("var_3133", dtype = "float64", shape = (924,))#candidate|3133|(924,)|var|float64
call_3132 = relay.TupleGetItem(func_1272_call(relay.reshape(var_3133.astype('float64'), [7, 11, 12]), relay.reshape(var_3133.astype('float64'), [7, 11, 12]), ), 0)
call_3134 = relay.TupleGetItem(func_1276_call(relay.reshape(var_3133.astype('float64'), [7, 11, 12]), relay.reshape(var_3133.astype('float64'), [7, 11, 12]), ), 0)
var_3177 = relay.var("var_3177", dtype = "float32", shape = (11, 10, 3))#candidate|3177|(11, 10, 3)|var|float32
bop_3178 = relay.not_equal(call_3121.astype('bool'), relay.reshape(var_3177.astype('bool'), relay.shape_of(call_3121))) # shape=(11, 10, 3)
bop_3181 = relay.not_equal(call_3122.astype('bool'), relay.reshape(var_3177.astype('bool'), relay.shape_of(call_3122))) # shape=(11, 10, 3)
func_2604_call = mod.get_global_var('func_2604')
func_2606_call = mutated_mod.get_global_var('func_2606')
call_3182 = relay.TupleGetItem(func_2604_call(), 0)
call_3183 = relay.TupleGetItem(func_2606_call(), 0)
func_1626_call = mod.get_global_var('func_1626')
func_1628_call = mutated_mod.get_global_var('func_1628')
call_3186 = relay.TupleGetItem(func_1626_call(), 2)
call_3187 = relay.TupleGetItem(func_1628_call(), 2)
output = relay.Tuple([call_3132,var_3133,bop_3178,call_3182,call_3186,])
output2 = relay.Tuple([call_3134,var_3133,bop_3181,call_3183,call_3187,])
func_3224 = relay.Function([var_3133,var_3177,], output)
mod['func_3224'] = func_3224
mod = relay.transform.InferType()(mod)
mutated_mod['func_3224'] = func_3224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3224_call = mutated_mod.get_global_var('func_3224')
var_3226 = relay.var("var_3226", dtype = "float64", shape = (924,))#candidate|3226|(924,)|var|float64
var_3227 = relay.var("var_3227", dtype = "float32", shape = (11, 10, 3))#candidate|3227|(11, 10, 3)|var|float32
call_3225 = func_3224_call(var_3226,var_3227,)
output = call_3225
func_3228 = relay.Function([var_3226,var_3227,], output)
mutated_mod['func_3228'] = func_3228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_3236 = func_2059_call()
call_3237 = func_2059_call()
func_1272_call = mod.get_global_var('func_1272')
func_1276_call = mutated_mod.get_global_var('func_1276')
var_3245 = relay.var("var_3245", dtype = "float64", shape = (924,))#candidate|3245|(924,)|var|float64
call_3244 = relay.TupleGetItem(func_1272_call(relay.reshape(var_3245.astype('float64'), [7, 11, 12]), relay.reshape(var_3245.astype('float64'), [7, 11, 12]), ), 0)
call_3246 = relay.TupleGetItem(func_1276_call(relay.reshape(var_3245.astype('float64'), [7, 11, 12]), relay.reshape(var_3245.astype('float64'), [7, 11, 12]), ), 0)
func_1668_call = mod.get_global_var('func_1668')
func_1670_call = mutated_mod.get_global_var('func_1670')
call_3264 = func_1668_call()
call_3265 = func_1668_call()
func_2431_call = mod.get_global_var('func_2431')
func_2433_call = mutated_mod.get_global_var('func_2433')
call_3266 = relay.TupleGetItem(func_2431_call(), 0)
call_3267 = relay.TupleGetItem(func_2433_call(), 0)
output = relay.Tuple([call_3236,call_3244,var_3245,call_3264,call_3266,])
output2 = relay.Tuple([call_3237,call_3246,var_3245,call_3265,call_3267,])
func_3277 = relay.Function([var_3245,], output)
mod['func_3277'] = func_3277
mod = relay.transform.InferType()(mod)
var_3278 = relay.var("var_3278", dtype = "float64", shape = (924,))#candidate|3278|(924,)|var|float64
output = func_3277(var_3278)
func_3279 = relay.Function([var_3278], output)
mutated_mod['func_3279'] = func_3279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_3288 = relay.TupleGetItem(func_1892_call(), 0)
call_3289 = relay.TupleGetItem(func_1894_call(), 0)
func_2512_call = mod.get_global_var('func_2512')
func_2515_call = mutated_mod.get_global_var('func_2515')
var_3300 = relay.var("var_3300", dtype = "bool", shape = (99,))#candidate|3300|(99,)|var|bool
call_3299 = relay.TupleGetItem(func_2512_call(relay.reshape(var_3300.astype('bool'), [11, 3, 3])), 0)
call_3301 = relay.TupleGetItem(func_2515_call(relay.reshape(var_3300.astype('bool'), [11, 3, 3])), 0)
output = relay.Tuple([call_3288,call_3299,var_3300,])
output2 = relay.Tuple([call_3289,call_3301,var_3300,])
func_3318 = relay.Function([var_3300,], output)
mod['func_3318'] = func_3318
mod = relay.transform.InferType()(mod)
var_3319 = relay.var("var_3319", dtype = "bool", shape = (99,))#candidate|3319|(99,)|var|bool
output = func_3318(var_3319)
func_3320 = relay.Function([var_3319], output)
mutated_mod['func_3320'] = func_3320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mod.get_global_var('func_2410')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_3371 = relay.TupleGetItem(func_2410_call(), 0)
call_3372 = relay.TupleGetItem(func_2411_call(), 0)
output = call_3371
output2 = call_3372
func_3375 = relay.Function([], output)
mod['func_3375'] = func_3375
mod = relay.transform.InferType()(mod)
mutated_mod['func_3375'] = func_3375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3375_call = mutated_mod.get_global_var('func_3375')
call_3376 = func_3375_call()
output = call_3376
func_3377 = relay.Function([], output)
mutated_mod['func_3377'] = func_3377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2161_call = mod.get_global_var('func_2161')
func_2162_call = mutated_mod.get_global_var('func_2162')
call_3461 = func_2161_call()
call_3462 = func_2161_call()
output = relay.Tuple([call_3461,])
output2 = relay.Tuple([call_3462,])
func_3476 = relay.Function([], output)
mod['func_3476'] = func_3476
mod = relay.transform.InferType()(mod)
mutated_mod['func_3476'] = func_3476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3476_call = mutated_mod.get_global_var('func_3476')
call_3477 = func_3476_call()
output = call_3477
func_3478 = relay.Function([], output)
mutated_mod['func_3478'] = func_3478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3476_call = mod.get_global_var('func_3476')
func_3478_call = mutated_mod.get_global_var('func_3478')
call_3505 = relay.TupleGetItem(func_3476_call(), 0)
call_3506 = relay.TupleGetItem(func_3478_call(), 0)
func_3043_call = mod.get_global_var('func_3043')
func_3045_call = mutated_mod.get_global_var('func_3045')
call_3507 = func_3043_call()
call_3508 = func_3043_call()
bop_3509 = relay.less(call_3505.astype('bool'), relay.reshape(call_3507.astype('bool'), relay.shape_of(call_3505))) # shape=(11, 10, 3)
bop_3512 = relay.less(call_3506.astype('bool'), relay.reshape(call_3508.astype('bool'), relay.shape_of(call_3506))) # shape=(11, 10, 3)
func_1668_call = mod.get_global_var('func_1668')
func_1670_call = mutated_mod.get_global_var('func_1670')
call_3514 = func_1668_call()
call_3515 = func_1668_call()
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_3523 = func_2382_call()
call_3524 = func_2382_call()
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_3526 = relay.TupleGetItem(func_1892_call(), 0)
call_3527 = relay.TupleGetItem(func_1894_call(), 0)
bop_3532 = relay.bitwise_and(call_3514.astype('int8'), relay.reshape(call_3507.astype('int8'), relay.shape_of(call_3514))) # shape=(11, 10, 3)
bop_3535 = relay.bitwise_and(call_3515.astype('int8'), relay.reshape(call_3508.astype('int8'), relay.shape_of(call_3515))) # shape=(11, 10, 3)
output = relay.Tuple([bop_3509,call_3523,call_3526,bop_3532,])
output2 = relay.Tuple([bop_3512,call_3524,call_3527,bop_3535,])
func_3542 = relay.Function([], output)
mod['func_3542'] = func_3542
mod = relay.transform.InferType()(mod)
mutated_mod['func_3542'] = func_3542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mutated_mod.get_global_var('func_3542')
call_3543 = func_3542_call()
output = call_3543
func_3544 = relay.Function([], output)
mutated_mod['func_3544'] = func_3544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3375_call = mod.get_global_var('func_3375')
func_3377_call = mutated_mod.get_global_var('func_3377')
call_3548 = func_3375_call()
call_3549 = func_3375_call()
output = relay.Tuple([call_3548,])
output2 = relay.Tuple([call_3549,])
func_3561 = relay.Function([], output)
mod['func_3561'] = func_3561
mod = relay.transform.InferType()(mod)
output = func_3561()
func_3562 = relay.Function([], output)
mutated_mod['func_3562'] = func_3562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2853_call = mod.get_global_var('func_2853')
func_2854_call = mutated_mod.get_global_var('func_2854')
call_3563 = func_2853_call()
call_3564 = func_2853_call()
output = call_3563
output2 = call_3564
func_3572 = relay.Function([], output)
mod['func_3572'] = func_3572
mod = relay.transform.InferType()(mod)
mutated_mod['func_3572'] = func_3572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3572_call = mutated_mod.get_global_var('func_3572')
call_3573 = func_3572_call()
output = call_3573
func_3574 = relay.Function([], output)
mutated_mod['func_3574'] = func_3574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3043_call = mod.get_global_var('func_3043')
func_3045_call = mutated_mod.get_global_var('func_3045')
call_3605 = func_3043_call()
call_3606 = func_3043_call()
output = relay.Tuple([call_3605,])
output2 = relay.Tuple([call_3606,])
func_3611 = relay.Function([], output)
mod['func_3611'] = func_3611
mod = relay.transform.InferType()(mod)
output = func_3611()
func_3612 = relay.Function([], output)
mutated_mod['func_3612'] = func_3612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2948_call = mod.get_global_var('func_2948')
func_2949_call = mutated_mod.get_global_var('func_2949')
call_3671 = func_2948_call()
call_3672 = func_2948_call()
func_3277_call = mod.get_global_var('func_3277')
func_3279_call = mutated_mod.get_global_var('func_3279')
var_3677 = relay.var("var_3677", dtype = "float64", shape = (924,))#candidate|3677|(924,)|var|float64
call_3676 = relay.TupleGetItem(func_3277_call(relay.reshape(var_3677.astype('float64'), [924,])), 1)
call_3678 = relay.TupleGetItem(func_3279_call(relay.reshape(var_3677.astype('float64'), [924,])), 1)
output = relay.Tuple([call_3671,call_3676,var_3677,])
output2 = relay.Tuple([call_3672,call_3678,var_3677,])
func_3693 = relay.Function([var_3677,], output)
mod['func_3693'] = func_3693
mod = relay.transform.InferType()(mod)
var_3694 = relay.var("var_3694", dtype = "float64", shape = (924,))#candidate|3694|(924,)|var|float64
output = func_3693(var_3694)
func_3695 = relay.Function([var_3694], output)
mutated_mod['func_3695'] = func_3695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3789 = relay.var("var_3789", dtype = "uint8", shape = (7, 6, 13))#candidate|3789|(7, 6, 13)|var|uint8
var_3790 = relay.var("var_3790", dtype = "uint8", shape = (7, 6, 13))#candidate|3790|(7, 6, 13)|var|uint8
bop_3791 = relay.minimum(var_3789.astype('uint8'), relay.reshape(var_3790.astype('uint8'), relay.shape_of(var_3789))) # shape=(7, 6, 13)
uop_3794 = relay.rsqrt(var_3789.astype('float64')) # shape=(7, 6, 13)
uop_3796 = relay.log(bop_3791.astype('float32')) # shape=(7, 6, 13)
output = relay.Tuple([uop_3794,uop_3796,])
output2 = relay.Tuple([uop_3794,uop_3796,])
func_3805 = relay.Function([var_3789,var_3790,], output)
mod['func_3805'] = func_3805
mod = relay.transform.InferType()(mod)
mutated_mod['func_3805'] = func_3805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3805_call = mutated_mod.get_global_var('func_3805')
var_3807 = relay.var("var_3807", dtype = "uint8", shape = (7, 6, 13))#candidate|3807|(7, 6, 13)|var|uint8
var_3808 = relay.var("var_3808", dtype = "uint8", shape = (7, 6, 13))#candidate|3808|(7, 6, 13)|var|uint8
call_3806 = func_3805_call(var_3807,var_3808,)
output = call_3806
func_3809 = relay.Function([var_3807,var_3808,], output)
mutated_mod['func_3809'] = func_3809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2853_call = mod.get_global_var('func_2853')
func_2854_call = mutated_mod.get_global_var('func_2854')
call_3830 = func_2853_call()
call_3831 = func_2853_call()
output = relay.Tuple([call_3830,])
output2 = relay.Tuple([call_3831,])
func_3845 = relay.Function([], output)
mod['func_3845'] = func_3845
mod = relay.transform.InferType()(mod)
mutated_mod['func_3845'] = func_3845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3845_call = mutated_mod.get_global_var('func_3845')
call_3846 = func_3845_call()
output = call_3846
func_3847 = relay.Function([], output)
mutated_mod['func_3847'] = func_3847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mod.get_global_var('func_2410')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_3889 = relay.TupleGetItem(func_2410_call(), 0)
call_3890 = relay.TupleGetItem(func_2411_call(), 0)
func_2512_call = mod.get_global_var('func_2512')
func_2515_call = mutated_mod.get_global_var('func_2515')
var_3908 = relay.var("var_3908", dtype = "bool", shape = (11, 9))#candidate|3908|(11, 9)|var|bool
call_3907 = relay.TupleGetItem(func_2512_call(relay.reshape(var_3908.astype('bool'), [11, 3, 3])), 0)
call_3909 = relay.TupleGetItem(func_2515_call(relay.reshape(var_3908.astype('bool'), [11, 3, 3])), 0)
output = relay.Tuple([call_3889,call_3907,var_3908,])
output2 = relay.Tuple([call_3890,call_3909,var_3908,])
func_3912 = relay.Function([var_3908,], output)
mod['func_3912'] = func_3912
mod = relay.transform.InferType()(mod)
var_3913 = relay.var("var_3913", dtype = "bool", shape = (11, 9))#candidate|3913|(11, 9)|var|bool
output = func_3912(var_3913)
func_3914 = relay.Function([var_3913], output)
mutated_mod['func_3914'] = func_3914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2218_call = mod.get_global_var('func_2218')
func_2220_call = mutated_mod.get_global_var('func_2220')
call_3932 = relay.TupleGetItem(func_2218_call(), 0)
call_3933 = relay.TupleGetItem(func_2220_call(), 0)
var_3949 = relay.var("var_3949", dtype = "float32", shape = (11, 10, 3))#candidate|3949|(11, 10, 3)|var|float32
bop_3950 = relay.right_shift(call_3932.astype('int32'), relay.reshape(var_3949.astype('int32'), relay.shape_of(call_3932))) # shape=(11, 10, 3)
bop_3953 = relay.right_shift(call_3933.astype('int32'), relay.reshape(var_3949.astype('int32'), relay.shape_of(call_3933))) # shape=(11, 10, 3)
func_2253_call = mod.get_global_var('func_2253')
func_2255_call = mutated_mod.get_global_var('func_2255')
const_3960 = relay.const([False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False], dtype = "bool")#candidate|3960|(240,)|const|bool
call_3959 = relay.TupleGetItem(func_2253_call(relay.reshape(const_3960.astype('bool'), [8, 30])), 1)
call_3961 = relay.TupleGetItem(func_2255_call(relay.reshape(const_3960.astype('bool'), [8, 30])), 1)
func_3611_call = mod.get_global_var('func_3611')
func_3612_call = mutated_mod.get_global_var('func_3612')
call_3963 = relay.TupleGetItem(func_3611_call(), 0)
call_3964 = relay.TupleGetItem(func_3612_call(), 0)
output = relay.Tuple([bop_3950,call_3959,const_3960,call_3963,])
output2 = relay.Tuple([bop_3953,call_3961,const_3960,call_3964,])
func_3975 = relay.Function([var_3949,], output)
mod['func_3975'] = func_3975
mod = relay.transform.InferType()(mod)
mutated_mod['func_3975'] = func_3975
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3976 = relay.var("var_3976", dtype = "float32", shape = (11, 10, 3))#candidate|3976|(11, 10, 3)|var|float32
func_3975_call = mutated_mod.get_global_var('func_3975')
call_3977 = func_3975_call(var_3976)
output = call_3977
func_3978 = relay.Function([var_3976], output)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2853_call = mod.get_global_var('func_2853')
func_2854_call = mutated_mod.get_global_var('func_2854')
call_3980 = func_2853_call()
call_3981 = func_2853_call()
func_3912_call = mod.get_global_var('func_3912')
func_3914_call = mutated_mod.get_global_var('func_3914')
var_3989 = relay.var("var_3989", dtype = "bool", shape = (33, 3))#candidate|3989|(33, 3)|var|bool
call_3988 = relay.TupleGetItem(func_3912_call(relay.reshape(var_3989.astype('bool'), [11, 9])), 0)
call_3990 = relay.TupleGetItem(func_3914_call(relay.reshape(var_3989.astype('bool'), [11, 9])), 0)
output = relay.Tuple([call_3980,call_3988,var_3989,])
output2 = relay.Tuple([call_3981,call_3990,var_3989,])
func_4000 = relay.Function([var_3989,], output)
mod['func_4000'] = func_4000
mod = relay.transform.InferType()(mod)
var_4001 = relay.var("var_4001", dtype = "bool", shape = (33, 3))#candidate|4001|(33, 3)|var|bool
output = func_4000(var_4001)
func_4002 = relay.Function([var_4001], output)
mutated_mod['func_4002'] = func_4002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2604_call = mod.get_global_var('func_2604')
func_2606_call = mutated_mod.get_global_var('func_2606')
call_4020 = relay.TupleGetItem(func_2604_call(), 0)
call_4021 = relay.TupleGetItem(func_2606_call(), 0)
func_228_call = mod.get_global_var('func_228')
func_231_call = mutated_mod.get_global_var('func_231')
var_4030 = relay.var("var_4030", dtype = "float64", shape = ())#candidate|4030|()|var|float64
const_4031 = relay.const([1.424164,-0.057547,-1.803083,-5.787254,4.887707,-6.105298,0.481756,2.912207,4.285736,8.438652,1.127745,5.159899,-2.046737,4.161747,-7.397410,5.556019,-5.191088,-9.826977,8.773560,8.228996,8.639228,-3.012398,6.487798,-7.864231,4.862031,-9.591401,6.885811,0.026373,-5.830653,0.944186,2.941406,-7.622588,8.501684,-9.720257,0.720666,8.203640,-7.018066,-2.481659,2.387816,-1.806300,-9.822073,2.544239,-4.334250,4.637533,0.549545,-1.171566,-5.561377,-6.533256,7.195132,-5.918184,1.213008,-1.110210,-9.163742,4.488714,5.858466,-6.357355,-6.698696,-8.500802,-0.847838,8.470358,-0.230558,-8.532850,-4.180703,-4.361519,2.569128,2.642650,-4.352223,-7.883441,-0.537383,1.875382,-1.384909,6.097022,4.277183,1.641676,-4.673200,-1.683940,-9.966615,2.710774,6.102563,2.471353,-7.303833,8.993700,-6.423054,8.248355,9.145044,-4.716201,-4.435978,8.313769,9.074648,9.449197,2.532149,8.064103,-8.973078,6.996780,-0.585311,1.563399,3.655859,-1.262238,-0.857257,-7.475007,-1.281614,9.741069,-1.351958,-3.008226,-0.298208,8.481485,2.468401,9.285558,5.174357,-4.359594,4.173434,5.221575,-9.847599,-7.176579,0.210609,8.688092,-9.415553,7.586113,2.336407,-9.326418,3.583830,2.372551,-3.034311,3.441389,7.344685,-4.786936,2.665189,7.253817,9.883374,-1.214838,-7.483086,-0.156817,0.150110,-1.057902,0.474631,-2.099208,-0.546700,-8.354139,-3.516679,9.620453,1.197820,8.241933,8.816749,-8.802241,-4.216012,2.768329,-5.613173,8.485177,3.858708,-9.176241,8.950522,-2.014394,3.603765,-7.983363,-1.159149,8.042334,6.018137,-8.177608,-8.264623,8.189368,4.568181,5.606419,-0.479367,6.730973,-0.797726,5.035380,-1.149194,-3.613153,-9.265820,-8.160892,-0.343806,-8.823099,-7.131943,-4.006997,3.373345,8.500658,-0.838768,7.097249,-9.207918,4.553184,-1.774733,-4.631443,-7.874578,-6.137024,1.008674,9.652695,9.222182,-1.846461,-2.051716,-6.346318,-8.892410,-7.888576,-9.202380,-4.658638,3.334079,-8.289004,-6.549270,-9.334817,7.535527,9.661076,7.619118,-5.697174,-3.421138,-8.788489,8.438389,-9.493032,3.113078,-7.050327,-3.009364,-4.499930,-7.621085,-2.431255,8.130226,3.107744,5.934147,7.679379,5.595030,5.733636,-9.491788,-0.419354,-3.594675,-5.430304,-1.006352,-6.644540,9.214992,-2.013095,4.638178,-0.851905,6.971284,5.928037,-1.092270,-4.036935,-2.002294,3.489491,2.257427,-5.895794,-9.917246,0.072481,0.847351,-9.769229,-3.839678,7.541472,0.253637,-1.928356,2.853796,2.091059,9.987846,-6.757769,-0.160836,-0.921682,1.186108,1.965362,7.042859,-0.036953,-4.988714,8.340669,0.150999,-1.044459,-1.995917,-9.333949,-1.229986,3.739076,7.476733,2.015268,0.209763,2.339509,-9.413953,0.100192,-1.249920,6.727609,-4.242923,4.199894,8.807516,-5.541221,5.359519,3.093559,-6.445647,8.048174,-3.766153,0.310651,-2.627667,2.532348,-0.796057,3.181101,-3.869322,2.640837,1.557207,2.378382,0.314933,5.346483,-9.591599,-6.925414,1.070000,-8.341016,9.544787,-0.475257,-2.255558,-2.453532,-7.932277,7.379258,-7.759750,2.532172,-6.640960,-1.670008,-3.047724,-1.613885,2.801794,5.371716,-9.618468,-9.491202,-3.305908,7.397773,-6.782836,1.644666,5.374000], dtype = "float64")#candidate|4031|(315,)|const|float64
call_4029 = func_228_call(relay.reshape(var_4030.astype('float64'), []), relay.reshape(const_4031.astype('float64'), [7, 3, 15]), )
call_4032 = func_228_call(relay.reshape(var_4030.astype('float64'), []), relay.reshape(const_4031.astype('float64'), [7, 3, 15]), )
output = relay.Tuple([call_4020,call_4029,var_4030,const_4031,])
output2 = relay.Tuple([call_4021,call_4032,var_4030,const_4031,])
func_4041 = relay.Function([var_4030,], output)
mod['func_4041'] = func_4041
mod = relay.transform.InferType()(mod)
var_4042 = relay.var("var_4042", dtype = "float64", shape = ())#candidate|4042|()|var|float64
output = func_4041(var_4042)
func_4043 = relay.Function([var_4042], output)
mutated_mod['func_4043'] = func_4043
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4221 = relay.const([[[-0.565067,-5.218480,-3.964822,-4.613506,5.226056,-5.919435,-3.693144,8.441200,6.997291,-2.942562],[-4.894718,-9.045616,7.284480,8.391750,-6.147566,7.823052,8.140291,2.416434,6.238387,3.863067],[0.456805,-5.960951,9.838198,-3.860239,6.842833,5.674146,6.354877,-8.884669,-1.127588,-3.756855],[1.979965,9.166967,2.393023,-7.681796,6.359907,9.028429,6.936748,-4.565383,6.978350,5.365139],[-9.501375,-0.559229,5.985180,-9.807042,3.220795,-5.719174,-9.770248,2.981643,-0.963025,3.420466],[2.483468,-5.852154,-7.777693,6.462968,8.030147,-1.933947,8.545458,-5.213207,2.972759,-0.440483],[7.646808,2.437648,-3.886883,-0.326020,-8.717005,-6.639528,-7.884379,-5.924537,-4.199444,4.738380],[7.624691,7.759621,-3.824048,4.952733,-2.533103,-9.893223,-6.421236,8.871893,-2.177674,0.457791],[1.738207,-6.741051,-9.743638,-8.250924,-1.341762,-9.087706,3.669057,-1.755071,7.279816,-1.077910],[9.072137,-1.862272,-4.966877,0.673441,2.781831,-7.193568,-0.885412,-2.448886,6.817051,1.254885],[-9.069069,1.402027,6.522997,-4.241906,9.697943,-4.198001,1.086039,-6.876362,4.773827,9.713147],[-5.366995,8.205902,-8.232416,4.255867,5.981913,-8.736661,6.999772,2.966608,5.794623,2.184065]],[[-7.458624,-7.275392,-5.005500,-7.732977,-4.636330,-3.884935,5.359005,1.168017,-1.548202,7.329321],[-8.095464,5.587688,-7.185939,-5.896367,-0.003892,-6.574551,-2.747017,6.215737,-2.120700,-1.640173],[9.135139,7.344730,-8.564755,-1.761997,-0.006676,-9.073172,3.234454,-3.880293,5.220851,-4.013292],[-9.952879,-6.252778,1.848734,-4.963482,7.915022,-8.720437,3.877195,7.496153,-6.919649,-8.961361],[-5.857144,8.716377,2.793334,5.660729,3.550984,-4.003415,-4.281314,-7.011866,-8.135947,3.481651],[4.818849,-1.388403,-6.353442,-1.471182,-2.846071,7.036222,-2.398742,-6.790771,-0.537245,-4.863457],[0.816939,9.312845,9.233172,2.722848,-9.446299,-4.163382,-7.815711,0.969771,-9.965619,-8.302563],[-3.387837,2.181510,-1.361440,-8.111111,6.175169,-9.971357,-5.935024,6.001472,3.474048,4.508713],[3.345037,7.814404,2.376313,-8.963300,4.662743,-3.846713,-7.710700,-7.328414,7.833026,7.797392],[2.038537,-2.520541,-1.655745,7.499665,-6.327323,4.431110,-2.988276,-4.357780,7.697642,-7.164370],[7.766631,3.100257,-0.846701,-7.291229,-1.558027,8.369415,-2.888089,4.019266,7.092825,-5.576762],[-7.793833,2.937960,5.891721,-0.459097,7.992526,9.419628,4.352831,-3.645836,-3.191373,0.600495]],[[6.978604,-7.671611,-9.856194,-6.062244,-2.838173,-1.848966,-3.837517,-6.478818,5.366310,8.266791],[6.152279,2.456894,8.691074,-1.427315,-1.653441,-8.858346,-2.770376,2.052519,3.064665,-2.197693],[2.047189,-8.141803,2.740636,9.841132,2.881308,5.913245,6.059452,8.876619,-0.635764,-0.947617],[5.574044,-8.653559,0.259563,5.000880,6.852180,-6.317993,-9.063988,2.025328,3.971281,-1.119158],[1.818247,8.890572,-4.054677,1.514162,1.089502,4.595260,-3.758023,-1.961917,-0.981320,-8.531854],[-5.624135,-2.886430,3.444786,-2.005669,-3.956432,6.377589,-3.754349,-4.970287,8.555553,9.120076],[4.134296,-6.064885,2.613296,4.922768,-5.366245,4.798945,-5.904817,8.279837,2.205713,1.975053],[-1.742179,1.286862,5.758600,4.869712,7.603364,3.162798,7.941150,4.913754,6.841687,-1.330876],[-4.846679,-8.488007,6.288814,4.252878,6.095174,-6.630072,0.919888,-2.805893,1.808639,-2.924388],[-4.688642,4.550032,5.751537,-2.501505,5.416295,-9.068567,3.226019,7.478148,-3.394534,2.866525],[3.436513,1.333840,-3.340426,7.415580,3.961217,-4.262621,-2.675208,8.746423,-9.653849,-9.383471],[2.978874,-1.275912,6.000892,6.693989,-1.161261,1.453972,9.201176,-5.414355,-5.443308,1.823796]],[[5.878659,6.175306,-3.534265,6.649599,5.289304,-9.066520,-0.772338,9.934103,-4.589568,1.921342],[0.777075,-3.563226,2.787264,-5.991503,6.547521,3.631041,-7.817999,-2.650470,-7.899065,2.987721],[1.633234,-1.768684,-1.679664,3.279187,-3.971044,8.941495,5.524510,-3.146416,9.204030,-7.563315],[2.357638,8.037913,-8.517060,-9.657694,-1.288624,-5.380946,3.370112,3.811860,-6.666500,5.253847],[-5.569317,0.563389,-1.011424,-1.687817,-4.666443,-1.841716,9.553186,3.190203,0.004566,-3.677481],[-0.087951,4.240803,4.271197,8.229014,8.315053,-2.563061,-6.095669,8.335377,-1.823216,-1.988509],[-5.994914,-8.789593,-8.922214,-7.074513,2.874708,2.658743,3.705879,7.703446,-3.275593,8.473724],[0.979524,0.391153,2.027007,1.166805,-6.256798,-4.665903,-9.810051,-3.176647,4.239108,9.850638],[0.795228,-4.556677,9.917121,2.856468,-1.652006,-1.707710,9.474319,6.279595,-3.796941,-4.173439],[-4.665783,-8.628545,3.219713,-9.802870,5.473345,1.811515,-9.562951,1.301629,5.178675,1.483241],[5.358074,-0.644438,4.258321,2.913012,-0.736333,8.088643,9.662620,4.456849,-0.041997,6.484842],[9.998767,1.908976,-0.236150,-5.306622,0.236160,6.189207,6.254597,0.669013,-1.230522,-1.499205]],[[-4.923048,2.699900,9.064081,-9.881081,-2.741251,0.177822,-6.827795,-7.007006,-3.602362,3.933532],[-1.974566,-4.453773,-4.639423,0.553328,4.340656,4.762551,0.912563,6.331896,1.609890,-2.034954],[4.268883,-6.559663,-1.752400,-7.622336,9.254772,9.750612,-4.902072,7.884703,1.397242,9.542079],[-1.639928,6.393992,-7.284537,8.003516,-7.802111,7.557697,6.027463,-0.746740,-6.773141,-3.411100],[-9.616262,-8.850393,-7.963710,5.172301,-6.378057,-5.409314,3.390975,-5.799714,-5.696117,4.165587],[1.578993,-5.557752,-7.567594,4.758893,5.810734,-8.258239,9.599293,-4.091929,-0.273016,6.733413],[0.165312,-8.019201,7.492946,-9.483640,-8.499971,8.246551,-8.189970,-6.175634,-4.586836,-4.085773],[-5.803711,6.007760,2.851760,5.940360,0.266584,-2.600793,-0.572041,9.406570,5.468878,1.277205],[6.302268,1.971114,-6.146398,6.427062,3.859926,-3.778581,-1.393145,3.901464,0.434494,-2.710842],[-1.799534,1.476780,8.565020,-3.564400,-5.128935,-6.082912,-3.393632,-2.681280,9.050728,6.571364],[2.012045,-4.561362,1.976938,9.960780,-8.223521,5.394094,-3.925815,9.359477,4.337113,-3.221692],[7.554625,-3.453469,-3.749480,-8.211709,-4.857630,0.794589,5.869487,6.879911,7.103803,-2.248099]],[[-9.854868,-9.864791,-7.268869,-8.954114,-1.435266,-6.532433,3.351879,8.435124,4.011933,-6.632511],[-2.643674,7.634265,7.105003,-1.673977,2.234803,9.198645,2.889072,-0.898654,7.606975,3.921393],[0.509831,-8.939228,-5.997868,-6.687758,1.518384,8.008620,-8.050994,-5.116708,-9.409509,7.725959],[6.167033,4.950926,-7.374200,-6.150024,7.087538,3.093538,6.670269,7.444071,-9.217798,1.767266],[-7.260775,1.431851,7.128447,6.646770,-0.971655,4.092361,5.017419,-1.332349,-6.603868,4.114661],[0.112493,-3.826742,-6.371867,-4.646220,-9.723773,1.512594,8.936773,7.098424,-9.231218,-9.315163],[2.844067,-8.747510,-6.272104,9.056667,5.956760,-2.289490,8.767721,-6.805867,1.854326,-2.451354],[-7.621389,-4.349524,-3.910798,4.562386,-7.098448,-8.125041,1.421821,-5.829128,4.658166,4.997277],[0.833266,9.004493,-9.526500,-5.475539,5.667333,4.832646,-2.669704,7.060767,-9.022227,3.317999],[-3.569834,-6.521838,-7.204843,6.474308,-4.894881,3.616147,3.114279,2.500030,-8.702342,7.455129],[-0.699102,4.676469,-1.004438,-2.024780,1.309938,-1.162047,3.940010,-7.901870,2.830119,1.448484],[-4.018102,4.842328,-1.083526,4.481561,3.751509,-6.402160,-2.674783,-8.400669,-0.759449,8.043582]],[[7.483029,6.198135,-7.187442,-7.267316,3.582191,-0.475639,-2.157878,6.295292,-7.848869,6.393986],[7.290541,1.788658,-9.540826,2.568030,-9.760889,-4.017440,-6.311186,-1.060656,6.010981,-7.049620],[4.305832,-0.359547,8.108467,-9.205185,8.229004,3.601166,9.407992,-3.904190,-8.605519,-4.677886],[-9.642449,-9.225722,-1.523987,2.987999,-4.211211,-6.762408,-2.125280,5.968395,4.978382,1.857104],[-6.672381,9.905529,-6.087768,1.719766,0.831038,3.940172,-6.704635,-2.138279,3.470505,2.428372],[-2.850618,8.455955,-1.854908,-5.003279,-9.687397,-3.881790,-5.924605,-7.553112,7.237250,2.733946],[4.519209,-7.419792,0.005897,-6.124656,2.788122,-8.747260,3.902609,-3.397046,-2.578485,6.748620],[1.564635,5.907378,-0.651890,-0.836547,0.455728,-5.745852,-5.656817,1.874714,-3.906850,-3.790399],[4.974982,7.991643,-7.816592,-4.597028,-4.593833,5.471997,-1.635679,9.084838,-4.970270,-1.507022],[2.804397,-4.715664,-1.514360,6.617071,4.920387,-7.340700,-8.459214,-7.921991,9.518221,-8.214794],[-8.126051,2.726945,-5.114890,6.814410,-5.724707,1.280668,6.327040,-9.671906,6.636496,-4.774205],[3.025824,6.320090,-5.415059,0.837184,-2.348856,3.458138,5.783281,0.361272,0.961637,3.706082]],[[5.675496,1.503704,-1.274511,-3.177741,-9.568515,0.151044,1.533541,0.147251,-2.388451,3.015890],[-1.705947,7.617612,-5.189331,-8.702675,-0.477699,0.578742,-9.104306,-6.451233,-1.886879,-2.579856],[3.239965,0.119534,-8.541947,-1.691265,4.794073,8.273993,-9.254334,0.697756,-0.659737,-1.471731],[2.585677,-7.463630,-6.600510,9.451314,5.755054,3.461030,7.677655,7.642887,-0.562172,-9.899286],[5.296625,3.633103,-5.239588,-6.473959,-6.004571,7.626629,4.445016,6.846878,-2.675418,-7.600449],[-9.602701,-0.659107,-1.272615,7.594738,6.083655,-6.059529,-8.925949,-2.923049,3.386067,8.145263],[6.107192,3.326517,-5.231230,6.981424,0.843378,-8.128870,1.870978,7.953020,-2.976406,-1.273839],[-0.196802,-5.906570,8.571856,-0.779003,-5.194353,-9.260410,-9.523475,-9.406638,6.178226,-2.640632],[2.042008,-2.587473,4.128413,6.628170,2.567840,-7.517180,-4.049595,-2.772334,3.025822,-1.933468],[-2.291425,-5.373439,4.735969,9.198212,-2.973388,1.906264,-9.996856,-6.726738,-1.361844,7.179891],[-1.126042,0.155911,-5.685184,-7.377871,-6.135418,9.385999,1.415917,-8.034519,-4.926004,4.391306],[9.570038,5.511724,4.698263,3.292764,0.485205,2.898618,-1.501846,-2.117577,-7.342460,3.475679]],[[-2.801423,9.327094,-4.581226,-1.019512,6.139098,5.699980,-2.054593,-2.372747,-7.271292,0.060226],[-9.733129,9.820944,-7.057570,4.838768,-3.677878,0.980770,-8.443897,1.576524,-2.602369,8.740179],[8.100201,-9.091998,0.869109,5.402706,1.590117,9.103601,2.005668,-2.004494,9.945162,-6.602400],[-0.626414,-8.248130,-1.348938,2.979674,7.946149,-9.599648,9.663452,-6.332002,3.717109,3.861003],[1.638326,-2.350391,9.503431,-8.122444,7.320018,2.318358,-3.283111,-5.756860,1.727887,-3.545349],[-0.405442,1.246353,2.016463,7.535180,-9.511319,1.253940,1.524232,-5.749771,9.375459,5.308617],[-6.135518,-0.367818,-8.101420,6.093189,1.651556,-8.364097,9.521379,3.978133,-9.277187,4.302228],[1.114412,-1.953020,5.244069,-9.046732,2.235918,9.274717,-7.891521,-9.872400,-1.498416,-9.228378],[3.347266,0.366259,-0.762858,-1.376453,8.511778,6.475652,-6.095806,-9.816819,8.932116,-8.013293],[-9.368443,-8.243108,-9.585992,-3.079113,-7.104151,-7.975397,7.482843,-9.181768,-6.372356,-1.356784],[2.904482,1.832001,8.366611,5.934838,-8.849116,2.430092,4.193822,6.980314,1.273094,-0.485418],[-3.763343,8.289699,-3.869872,7.582824,-3.112672,5.787520,-6.399856,-7.680390,-6.527430,-3.901442]],[[7.727010,5.750097,4.894948,-7.135370,-9.959427,-7.574283,4.986907,6.734036,-4.728386,9.924969],[-9.354852,-6.111152,1.207195,8.898142,-0.882914,-8.584479,2.249158,-6.185539,-0.251825,7.435380],[7.733309,3.435462,-7.048960,-9.588323,0.599351,0.484167,-1.995988,-8.131719,-7.755050,2.990122],[2.953905,3.179234,-2.564534,3.256809,-4.980350,6.550354,4.852422,9.716503,9.359835,-4.786908],[0.793264,3.286960,8.405708,2.515727,4.676401,-7.247372,-6.160186,8.126301,1.709204,9.516547],[-1.268316,6.953935,9.887745,5.534970,-1.012180,0.270606,9.205524,-9.812047,7.600176,1.326721],[-5.053257,1.741879,0.997457,3.596964,-3.002570,-0.097125,-9.829411,-2.987954,-1.880724,-1.054316],[8.236752,-7.659870,-8.933490,1.046224,-2.391875,-1.929457,-8.612971,4.168849,4.541249,-7.360515],[9.980508,-3.315116,-5.742550,1.285454,-3.992027,0.007465,-1.988401,-8.112578,-2.564721,-4.092876],[-3.422916,-7.848078,-4.132339,-5.986181,-9.005911,3.470661,-2.673559,3.271364,-2.448097,4.060614],[6.105556,-7.251405,4.007751,-3.691805,-2.434578,-0.441694,-2.435125,2.762375,7.041401,-5.217486],[-8.897950,3.663662,5.945373,2.858841,-6.079155,-2.601937,-2.905960,1.789503,9.569357,7.853674]]], dtype = "float64")#candidate|4221|(10, 12, 10)|const|float64
var_4222 = relay.var("var_4222", dtype = "float64", shape = (10, 12, 10))#candidate|4222|(10, 12, 10)|var|float64
bop_4223 = relay.less(const_4221.astype('bool'), relay.reshape(var_4222.astype('bool'), relay.shape_of(const_4221))) # shape=(10, 12, 10)
func_2365_call = mod.get_global_var('func_2365')
func_2367_call = mutated_mod.get_global_var('func_2367')
const_4228 = relay.const([-0.463330,1.926970,-4.837253,-0.787989,-0.411875,7.153971,9.876325,6.611148,4.605565,-7.431359,-9.845080,-1.182478,-0.063791,7.157460,5.741385,5.574797,-7.557933,7.303408,7.388254,-4.656140,-9.099579,7.580948,-3.131883,-5.548398,8.658228,1.810712,8.666476,5.597772,-7.544543,-8.525135,-9.003172,-9.662376,-4.022539,1.101860,6.682042,5.692939,-4.556749,7.272738,8.453813,-0.232904,-3.957365,7.983709,0.983156,1.211715,4.463424,1.901908,5.054561,-5.146291,9.855757,3.256368,9.559691,-9.419376,-2.854892,-1.700230,-2.962692,-1.594427,-5.317729,-5.207507,-5.315299,-3.095612,1.748906,-9.217470,3.786696,-1.010771,-0.006638,4.292065,1.253513,4.294220,7.086370,9.505022,1.314078,-6.833995,5.234810,5.464389,-8.645570,5.930452,-0.294401,-2.266495,-3.303968,-9.599847,-2.810829,7.560843,-9.325015,0.703544,-1.466976,4.995306,-2.951586,-3.442824,-7.347646,-1.217248,6.544469,2.044827,8.134023,1.513886,-2.304850,-7.357834,0.516576,-3.299412,8.552167,3.844485,9.057649,1.478709,-5.887591,9.183804,3.621669,8.121527,-4.347019,-9.709108,-6.157028,0.940080,-0.936013,6.403760,4.963550,1.590517,-7.363138,5.840940,9.257062,5.426793,-5.184011,-7.325919,-6.873945,-4.380388,-1.395779,-3.922902,-4.981665,-3.825373,-7.525811,-9.140641,2.016229,-2.798554,-7.263456,7.522775,-2.067312,5.275973,-5.778615,-3.328470,3.872511,5.268080,-1.339524,-2.163681,3.050073,1.220407,-6.076315,-1.303237,9.107793,7.127107,-7.434003,1.811438,-7.249287,9.812224,-9.327578,3.754150,-2.622626,-1.344460,8.748001,3.191990,9.661679,-3.314194,-0.990003,1.898039,5.503285,7.060397,-9.731243,-7.324443,3.172041,2.861813,5.150198,6.273178,1.957414,-0.582040,-9.568412,1.374359,-4.195284,5.567524,-8.485918,-3.226270,-5.517767,5.051776,-0.353071,7.252595,2.087080,-5.851209,3.135114,-0.559219,5.235674,4.934730,-9.181690,5.732769,-0.476235,7.334632,0.918984,-3.444628,1.549546,-2.020312,9.020822,7.458591,-8.549168,-3.583616,5.993012,-5.816225,0.437285,-1.936857,2.776963,2.335564,8.622215,-5.245911,-9.180284,-3.303571,0.154854,-9.167412,-9.031687,1.498411,6.731200,-4.252181,5.121996,5.510777,1.528816,-2.434862,0.820647,-2.894607,7.438566,7.864040,-0.494233,0.419193,4.126956,-2.642403,-0.953347,-8.941278,3.591253,-4.180281,-8.201299,-5.777359,-2.825715,-4.482770,-1.366390,-8.488810,3.569149,4.586629,1.213753,5.523172], dtype = "float64")#candidate|4228|(240,)|const|float64
call_4227 = relay.TupleGetItem(func_2365_call(relay.reshape(const_4228.astype('float64'), [24, 10])), 5)
call_4229 = relay.TupleGetItem(func_2367_call(relay.reshape(const_4228.astype('float64'), [24, 10])), 5)
uop_4231 = relay.sinh(call_4227.astype('float32')) # shape=(24, 10)
uop_4233 = relay.sinh(call_4229.astype('float32')) # shape=(24, 10)
output = relay.Tuple([bop_4223,const_4228,uop_4231,])
output2 = relay.Tuple([bop_4223,const_4228,uop_4233,])
func_4259 = relay.Function([var_4222,], output)
mod['func_4259'] = func_4259
mod = relay.transform.InferType()(mod)
var_4260 = relay.var("var_4260", dtype = "float64", shape = (10, 12, 10))#candidate|4260|(10, 12, 10)|var|float64
output = func_4259(var_4260)
func_4261 = relay.Function([var_4260], output)
mutated_mod['func_4261'] = func_4261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2948_call = mod.get_global_var('func_2948')
func_2949_call = mutated_mod.get_global_var('func_2949')
call_4316 = func_2948_call()
call_4317 = func_2948_call()
output = relay.Tuple([call_4316,])
output2 = relay.Tuple([call_4317,])
func_4318 = relay.Function([], output)
mod['func_4318'] = func_4318
mod = relay.transform.InferType()(mod)
mutated_mod['func_4318'] = func_4318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4318_call = mutated_mod.get_global_var('func_4318')
call_4319 = func_4318_call()
output = call_4319
func_4320 = relay.Function([], output)
mutated_mod['func_4320'] = func_4320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2604_call = mod.get_global_var('func_2604')
func_2606_call = mutated_mod.get_global_var('func_2606')
call_4377 = relay.TupleGetItem(func_2604_call(), 0)
call_4378 = relay.TupleGetItem(func_2606_call(), 0)
var_4397 = relay.var("var_4397", dtype = "float32", shape = (11, 10, 3))#candidate|4397|(11, 10, 3)|var|float32
bop_4398 = relay.bitwise_or(call_4377.astype('uint64'), relay.reshape(var_4397.astype('uint64'), relay.shape_of(call_4377))) # shape=(11, 10, 3)
bop_4401 = relay.bitwise_or(call_4378.astype('uint64'), relay.reshape(var_4397.astype('uint64'), relay.shape_of(call_4378))) # shape=(11, 10, 3)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
call_4410 = func_2495_call()
call_4411 = func_2495_call()
output = relay.Tuple([bop_4398,call_4410,])
output2 = relay.Tuple([bop_4401,call_4411,])
func_4424 = relay.Function([var_4397,], output)
mod['func_4424'] = func_4424
mod = relay.transform.InferType()(mod)
var_4425 = relay.var("var_4425", dtype = "float32", shape = (11, 10, 3))#candidate|4425|(11, 10, 3)|var|float32
output = func_4424(var_4425)
func_4426 = relay.Function([var_4425], output)
mutated_mod['func_4426'] = func_4426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3375_call = mod.get_global_var('func_3375')
func_3377_call = mutated_mod.get_global_var('func_3377')
call_4440 = func_3375_call()
call_4441 = func_3375_call()
func_2410_call = mod.get_global_var('func_2410')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_4461 = relay.TupleGetItem(func_2410_call(), 0)
call_4462 = relay.TupleGetItem(func_2411_call(), 0)
uop_4470 = relay.tan(call_4461.astype('float64')) # shape=(11, 10, 3)
uop_4472 = relay.tan(call_4462.astype('float64')) # shape=(11, 10, 3)
output = relay.Tuple([call_4440,uop_4470,])
output2 = relay.Tuple([call_4441,uop_4472,])
func_4478 = relay.Function([], output)
mod['func_4478'] = func_4478
mod = relay.transform.InferType()(mod)
output = func_4478()
func_4479 = relay.Function([], output)
mutated_mod['func_4479'] = func_4479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3561_call = mod.get_global_var('func_3561')
func_3562_call = mutated_mod.get_global_var('func_3562')
call_4488 = relay.TupleGetItem(func_3561_call(), 0)
call_4489 = relay.TupleGetItem(func_3562_call(), 0)
func_2410_call = mod.get_global_var('func_2410')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_4528 = relay.TupleGetItem(func_2410_call(), 0)
call_4529 = relay.TupleGetItem(func_2411_call(), 0)
output = relay.Tuple([call_4488,call_4528,])
output2 = relay.Tuple([call_4489,call_4529,])
func_4536 = relay.Function([], output)
mod['func_4536'] = func_4536
mod = relay.transform.InferType()(mod)
output = func_4536()
func_4537 = relay.Function([], output)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4538 = relay.var("var_4538", dtype = "float64", shape = (7, 1, 13))#candidate|4538|(7, 1, 13)|var|float64
uop_4539 = relay.erf(var_4538.astype('float64')) # shape=(7, 1, 13)
output = uop_4539
output2 = uop_4539
func_4543 = relay.Function([var_4538,], output)
mod['func_4543'] = func_4543
mod = relay.transform.InferType()(mod)
mutated_mod['func_4543'] = func_4543
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4544 = relay.var("var_4544", dtype = "float64", shape = (7, 1, 13))#candidate|4544|(7, 1, 13)|var|float64
func_4543_call = mutated_mod.get_global_var('func_4543')
call_4545 = func_4543_call(var_4544)
output = call_4545
func_4546 = relay.Function([var_4544], output)
mutated_mod['func_4546'] = func_4546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_4566 = relay.TupleGetItem(func_1892_call(), 2)
call_4567 = relay.TupleGetItem(func_1894_call(), 2)
func_1272_call = mod.get_global_var('func_1272')
func_1276_call = mutated_mod.get_global_var('func_1276')
const_4573 = relay.const([[0.275236,4.534692,5.299717,6.359916,1.386174,-6.468573,8.536700,7.603215,-0.270499,3.048185,-6.270653,-1.462419,-1.770097,2.740987,-1.885931,0.151969,-4.956253,6.794316,2.790676,-0.819106,0.302512,-7.698767,3.580934,4.650909,-4.577947,2.967902,-5.009386,0.570064,1.430955,4.757950,4.450410,-0.754536,1.423315,5.644696,-8.828848,2.287915,0.526589,-5.044863,4.020116,-4.045688,-5.392567,-4.134762,1.854022,-7.076944,3.695200,-2.384801,-3.528216,-5.108306,8.724148,-5.802704,6.309307,5.261049,3.334648,-1.252410,8.095462,-3.582616,-8.782044,-8.328805,-1.539305,-1.118003,-1.941405,0.763573,7.177714,-3.040121,4.358516,-5.892578],[-1.526877,7.664944,-4.759623,-2.367984,-0.131178,5.826800,3.711268,-6.073818,-8.316278,7.407747,-0.803004,1.378911,3.404116,-3.188321,9.787178,1.627233,-2.534860,7.704859,-9.364330,-9.943653,4.706722,3.625287,1.377034,-0.094859,7.965814,-1.355730,-1.284805,3.991172,5.575133,8.868417,9.032503,-0.380458,2.752860,-1.880116,0.988940,8.270097,-7.824378,7.296287,-9.425382,-3.127359,-3.270098,1.475071,-4.571036,-7.548583,-8.299044,-9.234950,-1.143345,2.138270,4.154836,-8.666731,-9.630597,9.776444,-7.980544,-9.675007,-1.117547,-9.746659,0.922228,-0.676134,7.014860,4.442967,-2.069225,2.806258,-0.857938,-6.153758,-7.649567,-2.124074],[-0.160164,1.191156,3.356073,-7.130332,-9.407656,-6.128272,-7.760588,-8.323096,8.360529,-3.879365,1.980554,-5.891648,-9.088963,4.503100,2.450654,-4.097622,1.370637,3.702998,8.670527,7.276143,-3.876088,-9.322282,-6.644357,-3.129717,-7.769705,8.330373,-6.825697,-3.782036,-0.587990,2.261142,8.944581,-7.190902,-8.792317,8.012247,5.135966,7.971408,-5.891920,-0.208573,-8.721805,-5.293115,4.262117,4.892302,-0.786469,6.485496,2.547354,-0.243344,-6.461288,-3.046416,-8.051502,-9.802606,-7.017298,-9.069196,7.026676,9.535961,1.611821,0.740331,1.479899,3.546477,-9.187386,-9.133550,6.209481,-5.673375,7.777834,-0.569964,8.701869,9.795805],[1.382793,-5.364236,6.924688,-3.728602,-2.715065,6.208811,-5.235641,6.739555,4.490916,7.283608,-7.473312,-1.130477,-2.952308,-3.226808,-2.641342,2.065212,2.587934,-7.891401,4.483065,5.090089,-0.839026,0.740557,3.576565,0.685566,-0.674713,-0.824588,0.824365,1.462906,5.224005,8.910004,8.847811,0.246400,-5.407977,9.255343,2.690461,3.483079,-3.415973,-5.215220,3.736113,-1.122915,-2.144420,8.775301,-0.800119,5.808241,-4.566017,7.891733,6.454272,-3.847928,-2.943267,5.671214,-4.107105,-9.738812,4.627026,8.535530,-8.010360,8.500521,-3.704577,-7.479610,0.054825,-8.440494,-2.730573,5.283736,5.648374,-8.402475,-8.133380,5.750139],[-1.930521,6.672393,-7.366649,1.002580,-0.179284,-8.970064,4.279624,0.703653,-4.816124,-1.429176,7.565411,1.728433,3.564647,0.189309,1.991376,-5.912091,-1.377128,-2.177962,-6.892714,4.826979,-5.656078,1.308684,0.326432,-8.507560,2.434226,-7.889999,-3.779435,3.262532,1.828686,9.103008,2.310026,2.000695,1.495308,-0.644921,0.738644,7.800155,0.681887,4.543367,8.490557,3.426653,-8.596288,-1.844946,2.626620,-6.584119,-8.499749,5.223140,1.226976,7.400645,-4.404439,3.279716,8.581204,4.993418,2.914458,4.882496,-8.620096,0.053529,8.235835,-3.259075,4.640771,1.460529,-6.743791,6.936991,0.799621,8.005054,0.363695,2.141057],[5.104976,8.514935,1.669100,7.738483,3.974572,-3.525687,-9.997970,1.427381,0.911843,3.697275,-2.785029,-8.223417,7.680046,3.507038,-9.311822,-5.557852,-4.939819,-4.662177,-6.360800,4.394331,3.921773,-8.978223,-5.842559,0.285990,1.157819,-9.140979,-6.992045,6.360721,-8.509574,-7.484422,-8.957365,-0.198027,-8.604341,-0.545790,-0.262948,1.801495,-5.749991,-9.041436,9.849413,-9.100255,-0.062028,-5.747456,8.990477,0.183520,3.215292,-8.981839,-4.841009,-4.455796,-7.058439,1.104675,-8.691205,-7.807681,1.153703,-4.782826,-9.272629,5.677760,3.912720,7.736661,3.773292,-2.544906,-3.398462,-5.556180,7.414669,-7.086767,-2.074838,-2.699818],[-9.854339,7.854351,3.129578,-1.003052,-0.963568,5.814368,-1.900541,3.044888,5.219106,-9.451214,-1.430182,-0.736540,0.517391,8.229883,-9.695623,-8.975808,-3.553581,-7.586291,5.315400,-8.403480,-0.877451,2.812335,-0.008025,4.925305,-8.748826,-2.713317,-4.234470,-3.188139,1.335553,4.963295,-7.227915,-2.942455,8.826632,-5.773787,5.112665,0.250848,-7.675524,-7.211598,5.556333,-7.324670,0.896503,-1.886284,0.075120,6.439934,4.411917,7.785667,7.010175,-0.625129,-7.023355,6.927944,8.100064,-6.106338,-6.237306,0.695126,-4.872050,8.600828,-6.249767,1.821849,0.485030,-7.753576,-1.031868,-5.336587,5.790002,-7.367441,5.704957,0.622515],[-5.214602,6.273541,4.775091,-9.700512,-6.535159,2.822134,-7.689645,0.959592,-5.279211,-2.621109,0.615540,-2.040637,3.296422,-6.423526,-8.816238,-1.824731,0.192507,6.668267,-8.555846,-4.449727,-0.404038,3.906753,1.583242,-3.498474,-9.711030,-0.659409,0.920811,-5.428188,7.154012,1.074288,-7.230377,4.631097,7.753209,-7.395396,-2.726880,8.710798,2.268709,5.986110,4.737190,-1.797562,-6.567852,5.000631,2.596068,9.091231,-3.269985,-5.645417,-3.621350,7.628237,6.360701,1.996199,-8.245302,-8.635290,7.018148,-3.856498,1.230730,-6.252791,6.001670,1.025540,1.250041,-9.483449,1.183888,-3.693531,-1.977297,-9.960327,-0.694312,0.684428],[-3.993637,-1.595232,-7.898170,-7.964507,9.235571,7.303565,-0.051781,3.662701,1.968801,1.046352,-2.755962,-0.715466,6.535291,-8.135874,-9.792419,6.539905,1.104870,-5.749767,-5.604548,9.807354,3.421626,3.192575,8.054306,1.711338,-3.636942,-5.030808,3.821599,4.287311,6.656332,-0.385671,5.322177,-1.591102,4.638068,-3.062816,7.625288,7.128367,4.823155,-7.028797,6.808801,3.256228,-4.413688,-5.052382,0.696218,3.833741,-4.356636,-1.406212,8.442262,-6.625407,-3.993207,-7.429155,9.897388,-1.911763,-8.726393,5.498644,4.829783,0.500513,-7.509756,2.152346,0.561296,-1.010414,-8.280836,-8.474862,6.692359,-9.321069,1.934395,4.121223],[-8.578998,9.394574,-9.710068,-1.458437,-3.770403,-5.259062,7.531822,-4.479891,-3.996084,-8.893826,2.101105,-0.052211,-3.238811,-8.504848,6.649940,-3.512532,-7.363121,7.408969,-6.267241,-4.319257,1.384479,-6.452813,-4.887667,-0.926306,6.634934,9.817197,0.080004,-5.585565,-3.636965,5.300625,-7.131652,5.542912,-7.984112,-3.527867,-9.142252,3.917019,2.579986,-9.142530,-3.773814,-5.036454,-4.464761,-7.818458,0.252728,3.655061,-3.125887,6.174533,-7.920532,8.892828,2.057899,9.063030,-1.316811,-3.143615,-7.537647,9.288010,0.429479,3.837273,0.351490,8.516644,-4.595629,-3.973681,2.339324,9.791511,-0.531341,-7.019191,-9.070342,5.145527],[-6.676031,-1.197023,-3.485101,6.540850,6.913351,7.273704,5.988818,4.485142,9.908705,-0.350566,-8.237197,-9.538202,-7.447610,-3.566183,9.920129,5.421021,3.395564,-2.143951,6.535246,3.932544,-1.065673,7.235600,3.262388,3.459404,-6.946172,-0.747413,-6.909977,9.361319,9.842305,2.417503,6.936922,6.213405,7.826810,-4.155168,7.773878,4.577346,6.167181,1.338411,-6.874251,4.538293,-9.947572,8.721063,7.363449,9.390481,-8.689906,8.502740,6.903015,5.497700,-3.471897,3.728615,3.803852,-8.984798,1.618088,-0.883833,-8.026751,-6.632397,3.480564,2.312588,-5.822979,0.500635,-7.683645,-4.404905,7.690782,-5.284430,-9.145726,-9.255991],[-6.117154,-1.241029,-0.550273,1.059542,-2.879502,-3.497760,0.297027,-1.597860,-4.978975,4.918308,-9.772939,4.616480,5.743151,-4.262760,1.700362,3.025788,3.541940,-6.862335,-5.893782,-2.589065,1.364150,-2.422706,3.323099,7.090950,7.208469,-0.273195,-1.424729,0.433922,3.545740,3.370971,-2.219489,-5.066950,-6.159648,-8.341373,9.417787,-7.600795,7.201388,7.305142,3.586176,-7.849635,3.280715,2.108093,-2.224997,7.601383,-2.711636,5.244428,-6.706750,-1.376595,-4.574166,4.582775,8.450872,-9.393781,6.264382,2.410284,-4.910409,0.742138,-6.491896,-6.971505,5.974098,-1.457730,-1.851768,2.892096,-4.958192,-3.433036,-1.959899,-0.618622],[0.439057,-6.647482,-9.822440,1.765837,6.232358,4.177284,8.140814,3.174764,4.553769,-7.602950,3.862319,-6.279839,0.904219,-9.490211,9.111249,-2.436375,6.494619,9.212036,-0.211632,1.999157,4.330419,-5.803488,-6.279850,7.251546,8.552129,4.040713,8.089686,-6.537106,-6.759013,-4.164621,9.272629,-0.790943,2.790695,3.144700,2.242894,-5.971215,7.588142,3.581076,-0.062027,3.538122,1.395254,-8.914559,0.979198,1.728454,8.628155,3.862649,-2.037784,6.835718,7.174776,-0.638732,9.313936,0.624741,0.729607,-5.010338,1.169484,3.175154,8.647081,-2.967109,5.581675,-3.974139,3.355001,7.446999,-9.778855,-3.554492,7.195861,-9.410746],[2.932222,1.089122,-2.765381,-3.319459,-5.211503,-3.337040,1.870107,-5.432669,4.030447,5.254014,-7.845095,-2.921465,2.271018,-1.436805,9.128132,-3.758023,-8.000594,0.856795,0.469413,-2.241622,-1.549079,2.942174,0.780954,-7.698919,1.720046,-3.440740,-9.001356,-8.640297,6.066656,7.632116,4.351276,5.630865,6.456956,-5.823689,-8.878226,-5.441507,-0.185047,-3.151585,7.585163,-0.328801,-9.838627,-0.036436,6.144535,-5.908673,1.241259,-9.453681,6.382691,-7.608154,-9.913527,-4.720371,-8.817865,1.325830,-3.415985,-8.019906,-7.691076,-9.542042,7.195593,-6.074030,2.170801,1.654327,-1.550457,1.830494,9.161012,-9.967953,7.914308,-8.111040]], dtype = "float64")#candidate|4573|(14, 66)|const|float64
call_4572 = relay.TupleGetItem(func_1272_call(relay.reshape(const_4573.astype('float64'), [7, 11, 12]), relay.reshape(const_4573.astype('float64'), [7, 11, 12]), ), 0)
call_4574 = relay.TupleGetItem(func_1276_call(relay.reshape(const_4573.astype('float64'), [7, 11, 12]), relay.reshape(const_4573.astype('float64'), [7, 11, 12]), ), 0)
output = relay.Tuple([call_4566,call_4572,const_4573,])
output2 = relay.Tuple([call_4567,call_4574,const_4573,])
func_4583 = relay.Function([], output)
mod['func_4583'] = func_4583
mod = relay.transform.InferType()(mod)
output = func_4583()
func_4584 = relay.Function([], output)
mutated_mod['func_4584'] = func_4584
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4598 = relay.const([[[3,-4],[-10,-10],[4,-7],[4,2]],[[-4,6],[-5,9],[3,7],[-2,10]],[[8,10],[6,9],[3,-6],[-3,-8]],[[7,3],[5,2],[-9,-5],[-7,-4]],[[8,-4],[-5,2],[-8,-4],[-7,8]]], dtype = "int64")#candidate|4598|(5, 4, 2)|const|int64
var_4599 = relay.var("var_4599", dtype = "int64", shape = (5, 4, 2))#candidate|4599|(5, 4, 2)|var|int64
bop_4600 = relay.bitwise_and(const_4598.astype('int64'), relay.reshape(var_4599.astype('int64'), relay.shape_of(const_4598))) # shape=(5, 4, 2)
uop_4603 = relay.atanh(bop_4600.astype('float32')) # shape=(5, 4, 2)
output = uop_4603
output2 = uop_4603
func_4609 = relay.Function([var_4599,], output)
mod['func_4609'] = func_4609
mod = relay.transform.InferType()(mod)
var_4610 = relay.var("var_4610", dtype = "int64", shape = (5, 4, 2))#candidate|4610|(5, 4, 2)|var|int64
output = func_4609(var_4610)
func_4611 = relay.Function([var_4610], output)
mutated_mod['func_4611'] = func_4611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3611_call = mod.get_global_var('func_3611')
func_3612_call = mutated_mod.get_global_var('func_3612')
call_4743 = relay.TupleGetItem(func_3611_call(), 0)
call_4744 = relay.TupleGetItem(func_3612_call(), 0)
output = relay.Tuple([call_4743,])
output2 = relay.Tuple([call_4744,])
func_4745 = relay.Function([], output)
mod['func_4745'] = func_4745
mod = relay.transform.InferType()(mod)
mutated_mod['func_4745'] = func_4745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4745_call = mutated_mod.get_global_var('func_4745')
call_4746 = func_4745_call()
output = call_4746
func_4747 = relay.Function([], output)
mutated_mod['func_4747'] = func_4747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_4787 = relay.TupleGetItem(func_1892_call(), 2)
call_4788 = relay.TupleGetItem(func_1894_call(), 2)
func_4259_call = mod.get_global_var('func_4259')
func_4261_call = mutated_mod.get_global_var('func_4261')
var_4790 = relay.var("var_4790", dtype = "float64", shape = (1200,))#candidate|4790|(1200,)|var|float64
call_4789 = relay.TupleGetItem(func_4259_call(relay.reshape(var_4790.astype('float64'), [10, 12, 10])), 2)
call_4791 = relay.TupleGetItem(func_4261_call(relay.reshape(var_4790.astype('float64'), [10, 12, 10])), 2)
func_1864_call = mod.get_global_var('func_1864')
func_1866_call = mutated_mod.get_global_var('func_1866')
call_4798 = relay.TupleGetItem(func_1864_call(), 0)
call_4799 = relay.TupleGetItem(func_1866_call(), 0)
func_3975_call = mod.get_global_var('func_3975')
func_3978_call = mutated_mod.get_global_var('func_3978')
call_4806 = relay.TupleGetItem(func_3975_call(relay.reshape(call_4798.astype('float32'), [11, 10, 3])), 0)
call_4807 = relay.TupleGetItem(func_3978_call(relay.reshape(call_4798.astype('float32'), [11, 10, 3])), 0)
var_4812 = relay.var("var_4812", dtype = "float32", shape = (24, 10))#candidate|4812|(24, 10)|var|float32
bop_4813 = relay.power(call_4789.astype('float64'), relay.reshape(var_4812.astype('float64'), relay.shape_of(call_4789))) # shape=(24, 10)
bop_4816 = relay.power(call_4791.astype('float64'), relay.reshape(var_4812.astype('float64'), relay.shape_of(call_4791))) # shape=(24, 10)
bop_4819 = relay.minimum(bop_4813.astype('uint16'), relay.reshape(call_4789.astype('uint16'), relay.shape_of(bop_4813))) # shape=(24, 10)
bop_4822 = relay.minimum(bop_4816.astype('uint16'), relay.reshape(call_4791.astype('uint16'), relay.shape_of(bop_4816))) # shape=(24, 10)
uop_4824 = relay.atanh(call_4789.astype('float64')) # shape=(24, 10)
uop_4826 = relay.atanh(call_4791.astype('float64')) # shape=(24, 10)
output = relay.Tuple([call_4787,var_4790,call_4798,call_4806,bop_4819,uop_4824,])
output2 = relay.Tuple([call_4788,var_4790,call_4799,call_4807,bop_4822,uop_4826,])
func_4827 = relay.Function([var_4790,var_4812,], output)
mod['func_4827'] = func_4827
mod = relay.transform.InferType()(mod)
mutated_mod['func_4827'] = func_4827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4827_call = mutated_mod.get_global_var('func_4827')
var_4829 = relay.var("var_4829", dtype = "float64", shape = (1200,))#candidate|4829|(1200,)|var|float64
var_4830 = relay.var("var_4830", dtype = "float32", shape = (24, 10))#candidate|4830|(24, 10)|var|float32
call_4828 = func_4827_call(var_4829,var_4830,)
output = call_4828
func_4831 = relay.Function([var_4829,var_4830,], output)
mutated_mod['func_4831'] = func_4831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
call_4863 = func_2495_call()
call_4864 = func_2495_call()
output = call_4863
output2 = call_4864
func_4866 = relay.Function([], output)
mod['func_4866'] = func_4866
mod = relay.transform.InferType()(mod)
mutated_mod['func_4866'] = func_4866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4866_call = mutated_mod.get_global_var('func_4866')
call_4867 = func_4866_call()
output = call_4867
func_4868 = relay.Function([], output)
mutated_mod['func_4868'] = func_4868
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4883 = relay.var("var_4883", dtype = "float32", shape = (5, 3, 3))#candidate|4883|(5, 3, 3)|var|float32
uop_4884 = relay.rsqrt(var_4883.astype('float32')) # shape=(5, 3, 3)
output = relay.Tuple([uop_4884,])
output2 = relay.Tuple([uop_4884,])
func_4889 = relay.Function([var_4883,], output)
mod['func_4889'] = func_4889
mod = relay.transform.InferType()(mod)
var_4890 = relay.var("var_4890", dtype = "float32", shape = (5, 3, 3))#candidate|4890|(5, 3, 3)|var|float32
output = func_4889(var_4890)
func_4891 = relay.Function([var_4890], output)
mutated_mod['func_4891'] = func_4891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2431_call = mod.get_global_var('func_2431')
func_2433_call = mutated_mod.get_global_var('func_2433')
call_4953 = relay.TupleGetItem(func_2431_call(), 0)
call_4954 = relay.TupleGetItem(func_2433_call(), 0)
output = relay.Tuple([call_4953,])
output2 = relay.Tuple([call_4954,])
func_4963 = relay.Function([], output)
mod['func_4963'] = func_4963
mod = relay.transform.InferType()(mod)
output = func_4963()
func_4964 = relay.Function([], output)
mutated_mod['func_4964'] = func_4964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2853_call = mod.get_global_var('func_2853')
func_2854_call = mutated_mod.get_global_var('func_2854')
call_5003 = func_2853_call()
call_5004 = func_2853_call()
func_2512_call = mod.get_global_var('func_2512')
func_2515_call = mutated_mod.get_global_var('func_2515')
const_5027 = relay.const([False,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True], dtype = "bool")#candidate|5027|(99,)|const|bool
call_5026 = relay.TupleGetItem(func_2512_call(relay.reshape(const_5027.astype('bool'), [11, 3, 3])), 0)
call_5028 = relay.TupleGetItem(func_2515_call(relay.reshape(const_5027.astype('bool'), [11, 3, 3])), 0)
func_4543_call = mod.get_global_var('func_4543')
func_4546_call = mutated_mod.get_global_var('func_4546')
var_5032 = relay.var("var_5032", dtype = "float64", shape = (91,))#candidate|5032|(91,)|var|float64
call_5031 = func_4543_call(relay.reshape(var_5032.astype('float64'), [7, 1, 13]))
call_5033 = func_4543_call(relay.reshape(var_5032.astype('float64'), [7, 1, 13]))
uop_5037 = relay.log2(call_5031.astype('float32')) # shape=(7, 1, 13)
uop_5039 = relay.log2(call_5033.astype('float32')) # shape=(7, 1, 13)
bop_5053 = relay.floor_divide(uop_5037.astype('float64'), relay.reshape(var_5032.astype('float64'), relay.shape_of(uop_5037))) # shape=(7, 1, 13)
bop_5056 = relay.floor_divide(uop_5039.astype('float64'), relay.reshape(var_5032.astype('float64'), relay.shape_of(uop_5039))) # shape=(7, 1, 13)
func_3043_call = mod.get_global_var('func_3043')
func_3045_call = mutated_mod.get_global_var('func_3045')
call_5058 = func_3043_call()
call_5059 = func_3043_call()
output = relay.Tuple([call_5003,call_5026,const_5027,bop_5053,call_5058,])
output2 = relay.Tuple([call_5004,call_5028,const_5027,bop_5056,call_5059,])
func_5061 = relay.Function([var_5032,], output)
mod['func_5061'] = func_5061
mod = relay.transform.InferType()(mod)
mutated_mod['func_5061'] = func_5061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5062 = relay.var("var_5062", dtype = "float64", shape = (91,))#candidate|5062|(91,)|var|float64
func_5061_call = mutated_mod.get_global_var('func_5061')
call_5063 = func_5061_call(var_5062)
output = call_5063
func_5064 = relay.Function([var_5062], output)
mutated_mod['func_5064'] = func_5064
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5080 = relay.var("var_5080", dtype = "float64", shape = (4, 12, 2))#candidate|5080|(4, 12, 2)|var|float64
var_5081 = relay.var("var_5081", dtype = "float64", shape = (4, 12, 2))#candidate|5081|(4, 12, 2)|var|float64
bop_5082 = relay.floor_divide(var_5080.astype('float64'), relay.reshape(var_5081.astype('float64'), relay.shape_of(var_5080))) # shape=(4, 12, 2)
uop_5092 = relay.exp(var_5081.astype('float64')) # shape=(4, 12, 2)
bop_5099 = relay.greater(uop_5092.astype('bool'), relay.reshape(var_5081.astype('bool'), relay.shape_of(uop_5092))) # shape=(4, 12, 2)
uop_5103 = relay.asin(var_5080.astype('float64')) # shape=(4, 12, 2)
bop_5111 = relay.divide(uop_5092.astype('float64'), relay.reshape(bop_5082.astype('float64'), relay.shape_of(uop_5092))) # shape=(4, 12, 2)
bop_5116 = relay.bitwise_xor(bop_5099.astype('int64'), relay.reshape(uop_5092.astype('int64'), relay.shape_of(bop_5099))) # shape=(4, 12, 2)
bop_5122 = relay.maximum(bop_5099.astype('float32'), relay.reshape(bop_5082.astype('float32'), relay.shape_of(bop_5099))) # shape=(4, 12, 2)
func_1892_call = mod.get_global_var('func_1892')
func_1894_call = mutated_mod.get_global_var('func_1894')
call_5125 = relay.TupleGetItem(func_1892_call(), 2)
call_5126 = relay.TupleGetItem(func_1894_call(), 2)
output = relay.Tuple([uop_5103,bop_5111,bop_5116,bop_5122,call_5125,])
output2 = relay.Tuple([uop_5103,bop_5111,bop_5116,bop_5122,call_5126,])
func_5127 = relay.Function([var_5080,var_5081,], output)
mod['func_5127'] = func_5127
mod = relay.transform.InferType()(mod)
var_5128 = relay.var("var_5128", dtype = "float64", shape = (4, 12, 2))#candidate|5128|(4, 12, 2)|var|float64
var_5129 = relay.var("var_5129", dtype = "float64", shape = (4, 12, 2))#candidate|5129|(4, 12, 2)|var|float64
output = func_5127(var_5128,var_5129,)
func_5130 = relay.Function([var_5128,var_5129,], output)
mutated_mod['func_5130'] = func_5130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1668_call = mod.get_global_var('func_1668')
func_1670_call = mutated_mod.get_global_var('func_1670')
call_5156 = func_1668_call()
call_5157 = func_1668_call()
output = call_5156
output2 = call_5157
func_5162 = relay.Function([], output)
mod['func_5162'] = func_5162
mod = relay.transform.InferType()(mod)
mutated_mod['func_5162'] = func_5162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5162_call = mutated_mod.get_global_var('func_5162')
call_5163 = func_5162_call()
output = call_5163
func_5164 = relay.Function([], output)
mutated_mod['func_5164'] = func_5164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5183 = relay.var("var_5183", dtype = "float32", shape = (4, 11, 12))#candidate|5183|(4, 11, 12)|var|float32
uop_5184 = relay.sinh(var_5183.astype('float32')) # shape=(4, 11, 12)
func_3693_call = mod.get_global_var('func_3693')
func_3695_call = mutated_mod.get_global_var('func_3695')
const_5188 = relay.const([-8.136704,1.166193,-2.613759,3.513619,-9.704974,3.097652,5.479203,6.422102,-3.008752,-8.391051,6.080835,-6.426581,1.955449,-0.986188,-6.201171,1.285709,3.683947,4.072150,8.839573,2.434541,6.459988,-9.223088,-9.015776,-8.717977,-9.338704,1.854780,-8.407340,8.047061,-0.664135,-9.651791,-0.234800,-3.343756,4.908486,9.633440,-5.475733,-5.464901,8.086385,-9.944645,-6.191897,-4.592508,9.378752,-9.145393,-3.734800,0.575349,-9.166002,6.688043,6.615183,-9.772418,5.622877,5.986311,-7.870424,1.553777,1.922256,-5.866527,8.498040,-8.233882,-6.883310,-8.521826,-1.303732,4.523652,-5.449931,2.351241,-2.379657,-4.717402,5.590348,8.887963,3.959862,0.482411,-5.930084,-2.239380,6.987324,-9.690399,-0.311246,-0.445021,5.947986,4.448933,-4.580669,3.164421,-7.465056,-1.787329,-2.842685,-5.081898,-3.530003,-0.719328,8.702327,-5.445587,5.154407,-3.227110,-4.810227,-7.832516,-2.414562,0.846285,0.089321,-3.939481,-5.308668,2.875987,-6.416495,-7.177831,-8.354133,-3.014489,8.183964,-4.860062,1.556521,-5.130486,0.304929,2.098861,-8.620787,-3.979575,-6.877684,-1.629297,2.517197,9.227845,8.773854,-0.320317,-5.153823,7.996559,-4.653666,-9.355013,-9.124287,3.884208,7.467539,3.140356,3.411332,5.927460,-7.783698,-5.280405,-7.455790,-6.816393,9.848319,7.737103,3.064764,1.305870,-5.716127,2.334539,7.797523,-5.836735,-8.959066,-4.980759,0.235790,0.835698,4.155732,4.097352,6.813202,7.366560,-7.834933,-8.823429,5.786741,5.004618,0.267461,-7.502517,8.769411,0.391242,0.602492,0.433096,-9.152576,-5.869576,-2.902100,7.900589,5.028848,-5.005193,9.875541,1.419300,6.711514,-9.507226,-1.387632,3.689910,9.264708,6.977959,-2.807671,8.766907,5.518068,8.702910,2.788616,0.623592,0.380950,-2.652882,-7.261138,-1.081106,3.915637,-1.872576,8.898568,1.501519,-6.560737,6.223053,-2.113997,0.178478,2.500991,3.461809,5.817661,0.123954,1.888149,4.733751,-9.178470,0.693230,-3.837469,6.656799,9.943862,-4.988677,9.328249,-5.826324,-3.298688,1.435450,-6.184107,-3.142565,7.778722,1.369071,-1.399987,-0.193863,-1.746428,-3.054274,2.458403,-6.554395,-4.444954,-6.044662,2.333754,3.567634,1.456190,2.436556,-4.359756,7.194717,9.359616,-6.838668,-7.163354,-2.689741,-3.664816,3.455884,-3.636112,-0.917055,7.524693,-9.670147,8.914321,-8.539814,-4.096041,6.626593,-3.873871,-8.455653,5.919439,1.623684,8.439083,-7.281769,-1.032115,0.274853,0.920723,6.198690,6.027171,9.769131,-9.228445,0.400248,3.579406,2.913075,0.558791,-1.545305,-9.618480,-0.302378,9.464276,3.543435,3.265294,7.527192,-4.957675,4.521180,-6.451008,-3.936654,-2.691789,-7.370616,-5.154179,8.646293,8.259846,-0.531255,2.673816,-3.285213,4.117788,-0.846139,-9.199225,-1.178350,5.565894,-5.280733,-5.707843,-6.409186,-2.394653,3.150596,-1.774311,6.461700,-4.383407,6.323725,-0.755316,-1.814843,1.740162,-2.672604,-9.004060,-4.218412,-1.554981,-6.258074,4.123673,-0.293324,0.341926,7.486254,-2.325449,4.464956,-8.960639,9.791774,-4.794190,9.746109,-2.275181,-8.880162,-5.314581,-2.575927,7.647235,9.021086,8.425617,2.578317,4.198453,-3.791467,5.699364,-4.870051,-9.513754,-1.541157,-5.938606,-6.114776,-1.031498,2.533961,2.352945,0.267449,-6.316454,-5.205068,-8.811535,-0.467681,-1.078991,-2.047513,0.126480,6.311243,-9.230440,-2.526797,9.571994,5.849962,0.798656,-6.320421,1.994660,-9.005858,7.118064,5.145412,-9.437087,3.092411,9.688545,-3.360952,3.160702,-9.233821,8.680011,-2.058625,-1.795478,-1.176236,-7.233592,-5.788063,9.813930,-1.928490,3.917117,-6.871168,3.973301,-6.615473,4.632754,9.101737,4.590335,-0.029239,7.434119,9.137535,5.326755,2.479401,5.121740,9.369904,-9.435091,4.473756,3.090140,1.079009,6.434254,0.660469,-2.423234,0.494478,9.138885,3.775086,-0.765447,-4.045398,-9.526078,-0.210653,1.906012,-8.542782,6.364971,-4.931989,-6.951460,5.465752,6.123813,-7.172198,-1.114285,6.363981,-7.241051,-9.531125,-8.507784,-8.090563,-4.085478,-0.577319,-2.989774,-6.224304,-6.400241,-2.098707,-6.776665,-4.805323,7.660961,-6.931668,3.379397,4.806058,-7.577693,-4.471993,-5.682779,5.682269,2.401901,-7.927151,5.545548,3.314020,8.495283,-5.935785,-9.898998,-2.997162,8.871897,1.304788,-4.560795,-8.389202,-1.525473,1.370833,3.979778,9.416513,-7.954915,-0.576379,-9.790538,3.274201,-8.381980,-0.627475,4.972179,-0.229740,9.338967,9.316592,-3.118758,-1.507515,-2.220181,6.046049,-9.780339,6.765960,-7.610148,-4.755864,5.307638,7.497852,3.840394,-0.748369,-4.563322,-1.395793,-6.882829,2.451232,8.838280,4.175941,-0.169091,-6.209419,-5.603896,9.790538,2.935693,3.001230,-2.163489,-8.093527,-8.242875,-3.664933,9.240943,-4.135856,-3.782126,-1.917552,8.753936,1.928915,-1.362498,5.906917,6.414962,-1.015594,-0.041678,-8.540930,-1.118485,2.290236,5.602456,5.421934,-0.793027,4.882359,9.297075,-4.722604,1.053203,-4.349901,5.476886,-9.621172,5.145078,-0.724564,7.068930,-7.373187,1.044775,-9.216421,0.321680,-2.629458,-8.309368,-6.691756,0.326548,-6.633767,-4.225556,2.620831,-4.193823,9.895392,-9.024178,-1.472710,-6.805876,2.732818,-3.580483,-4.661908,0.580060,0.818942,-1.727899,5.567084,-9.335900,1.278196,1.002877,7.935931,-0.547728,9.922665,-9.362541,-2.345640,-3.040853,-0.496465,-1.753596,-7.947425,1.351262,3.720289,0.694007,-9.335038,-2.291707,-3.607948,-9.197719,-5.142145,-4.194684,8.955676,2.683257,7.408787,7.932025,-7.598753,1.046779,6.034957,-8.320740,-7.414781,8.240311,6.188646,-1.799835,9.417204,3.490388,-7.851645,0.640279,-2.397752,2.712654,-9.354663,-5.471891,-8.373504,5.726140,-6.029733,-7.346151,2.793902,0.911384,-5.666774,4.080108,-1.762622,6.485958,-1.573060,-4.204966,3.492011,5.102618,-7.889109,-5.823983,0.177477,-2.620586,0.542180,-2.812045,3.148610,4.509049,-0.563473,5.316418,-1.053584,1.485119,-2.405449,7.479868,3.698302,5.938493,-4.527151,9.187459,-8.068130,-5.892321,-4.443673,-4.106707,-3.103654,1.059614,-3.393367,-8.368417,2.120201,-4.690650,9.935915,5.243244,-2.836717,3.244480,-0.734031,-8.367756,-2.976458,-1.701913,8.172969,-2.434339,5.466685,-3.681047,5.288017,-8.549126,-7.721837,-9.470654,-3.935126,4.010278,-7.694615,-5.568799,9.228921,2.194805,3.027103,-4.159317,1.004990,-9.668611,8.451511,-4.773943,4.199498,2.346592,8.796873,-9.468611,-6.867763,-5.629272,-3.361354,2.260928,1.223855,4.242732,7.951787,-3.456878,3.043672,5.680663,5.450578,8.470326,-6.281145,0.251483,-2.822629,5.201336,9.396025,1.568472,-8.723317,4.138481,-0.496373,-6.006295,-6.432172,-5.987536,-1.957482,-8.421138,9.637301,-6.559146,5.927897,-4.237411,9.028091,-2.812812,0.629522,-9.202493,-7.609295,-4.227743,7.407433,-6.394291,1.274556,0.101503,-3.513126,4.158998,0.599121,9.940911,6.377951,-1.643080,-8.445155,1.626771,-0.326242,8.362885,5.306042,0.563784,1.494144,9.426796,-9.789844,-3.539121,-0.232492,4.201975,8.642387,-5.392396,-3.592890,-3.745156,3.000963,-8.325934,3.716242,8.310990,8.800799,5.161534,-6.198323,2.682728,9.516186,-6.327354,-7.231600,6.697439,-5.483777,-4.946332,-0.561981,7.259664,7.484036,-5.315423,-2.613834,4.020479,-5.862450,-4.457375,7.710589,-0.657928,4.994443,6.332320,-8.868527,4.951847,-0.001269,6.247252,-4.398310,8.114668,-2.801386,5.717867,2.404370,7.076028,7.388325,-2.060447,7.832223,-2.666952,9.226706,-5.767864,-9.929726,5.888111,-6.647713,-8.985251,1.186574,-9.971625,5.654812,-1.964153,-1.197589,-2.727206,5.952725,8.475431,0.414768,9.088711,1.895358,-9.426242,-8.656129,-8.215014,-2.847866,0.393578,-4.250711,-2.501063,9.725489,-5.560028,-7.228550,-4.338454,-0.098867,-2.353660,9.099957,-4.058640,-9.951954,-1.374532,-9.786018,9.876042,1.559843,4.289757,-3.560714,9.299839,-4.651881,2.718781,0.121862,4.674387,3.849770,6.573496,3.819491,4.681427,3.752873,-1.175102,4.113813,-7.581311,0.501812,-2.866966,1.148147,0.052887,-8.885875,-4.100100,-3.312493,1.787662,-0.556301,-0.767143,-9.737191,2.690719,-0.478744,-9.026646,1.368371,-4.136807,-2.195055,-3.739769,1.320916,3.551410,-7.036293,5.483145,5.125843,1.291973,1.341236,-1.645344,2.847972,4.832517,2.933613,8.050902,5.838925,9.680340,3.285644,6.820978,-2.384312,-1.560950,1.054316,1.160962,-1.889847,-8.485508,7.337780,7.645611,-5.194159,-5.114912,-4.356226,-1.676081,9.657734,9.675113,8.154709,7.405455,-5.369843,-1.781711,6.920519,-6.878020,-3.942686,-1.015495,5.982317,0.786714,-9.072363,-1.502255,5.717332,-8.692160,-0.943054,1.815004,4.537788,2.085001,-4.465155,5.863042,-2.626139,0.957182,-3.233117,-1.788641,-9.125465,4.636318,3.267655,4.672400,-9.014048,8.458699,-3.942527,-5.359207,-2.076987,0.476288,1.829230,-9.324386,-1.761883,9.688861,6.224021,6.768923,3.058983,0.260816,-7.520378,5.470027,-9.799220,6.571437,-2.123642,-6.147844,-4.874847,7.243757,-6.102972,3.442522,-6.042574,6.304826,-0.831718,2.866073,5.882355,-9.014799,9.013742,-2.764483,-6.777042,-0.771208,0.360525,0.800929,-6.337396,-8.262401,3.573293,-8.742233,-8.599787,7.082808,-7.350282,-8.667096,5.733908,7.325677,-0.968987,0.660697,8.787807,3.673794,-3.820633,-6.478283,-7.145046,-7.770897,-1.202568,4.026442,-1.527582,1.259560,7.386096,1.192521,-2.133948,6.340618,-8.362670], dtype = "float64")#candidate|5188|(924,)|const|float64
call_5187 = relay.TupleGetItem(func_3693_call(relay.reshape(const_5188.astype('float64'), [924,])), 1)
call_5189 = relay.TupleGetItem(func_3695_call(relay.reshape(const_5188.astype('float64'), [924,])), 1)
output = relay.Tuple([uop_5184,call_5187,const_5188,])
output2 = relay.Tuple([uop_5184,call_5189,const_5188,])
func_5202 = relay.Function([var_5183,], output)
mod['func_5202'] = func_5202
mod = relay.transform.InferType()(mod)
mutated_mod['func_5202'] = func_5202
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5203 = relay.var("var_5203", dtype = "float32", shape = (4, 11, 12))#candidate|5203|(4, 11, 12)|var|float32
func_5202_call = mutated_mod.get_global_var('func_5202')
call_5204 = func_5202_call(var_5203)
output = call_5204
func_5205 = relay.Function([var_5203], output)
mutated_mod['func_5205'] = func_5205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2853_call = mod.get_global_var('func_2853')
func_2854_call = mutated_mod.get_global_var('func_2854')
call_5234 = func_2853_call()
call_5235 = func_2853_call()
func_5202_call = mod.get_global_var('func_5202')
func_5205_call = mutated_mod.get_global_var('func_5205')
var_5238 = relay.var("var_5238", dtype = "float32", shape = (528,))#candidate|5238|(528,)|var|float32
call_5237 = relay.TupleGetItem(func_5202_call(relay.reshape(var_5238.astype('float32'), [4, 11, 12])), 0)
call_5239 = relay.TupleGetItem(func_5205_call(relay.reshape(var_5238.astype('float32'), [4, 11, 12])), 0)
output = relay.Tuple([call_5234,call_5237,var_5238,])
output2 = relay.Tuple([call_5235,call_5239,var_5238,])
func_5240 = relay.Function([var_5238,], output)
mod['func_5240'] = func_5240
mod = relay.transform.InferType()(mod)
var_5241 = relay.var("var_5241", dtype = "float32", shape = (528,))#candidate|5241|(528,)|var|float32
output = func_5240(var_5241)
func_5242 = relay.Function([var_5241], output)
mutated_mod['func_5242'] = func_5242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_5244 = func_2059_call()
call_5245 = func_2059_call()
func_2948_call = mod.get_global_var('func_2948')
func_2949_call = mutated_mod.get_global_var('func_2949')
call_5246 = func_2948_call()
call_5247 = func_2948_call()
uop_5257 = relay.atan(call_5244.astype('float32')) # shape=(11, 10, 3)
uop_5259 = relay.atan(call_5245.astype('float32')) # shape=(11, 10, 3)
output = relay.Tuple([call_5246,uop_5257,])
output2 = relay.Tuple([call_5247,uop_5259,])
func_5264 = relay.Function([], output)
mod['func_5264'] = func_5264
mod = relay.transform.InferType()(mod)
output = func_5264()
func_5265 = relay.Function([], output)
mutated_mod['func_5265'] = func_5265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4745_call = mod.get_global_var('func_4745')
func_4747_call = mutated_mod.get_global_var('func_4747')
call_5296 = relay.TupleGetItem(func_4745_call(), 0)
call_5297 = relay.TupleGetItem(func_4747_call(), 0)
const_5322 = relay.const([[[-9.352901,2.543617,0.574379],[9.651486,-5.203855,-1.525639],[-5.575913,1.291859,-7.768569],[-5.490871,-9.326557,4.541070],[-6.389864,4.077984,5.869766],[8.139297,4.698174,-8.983772],[-7.835626,4.465829,5.421854],[9.919882,-2.717332,3.846023],[7.592191,-7.260403,6.797939],[7.347108,-7.201438,-5.169180]],[[2.160150,5.279007,-7.398999],[6.361551,-3.894434,2.095482],[-0.923023,7.041698,7.781136],[3.305225,-2.078948,5.781244],[-4.001994,1.293997,5.286817],[-1.738514,-0.345360,4.841566],[-8.540845,6.455120,8.478965],[-8.059009,8.632135,1.134433],[8.443004,4.802748,-5.166177],[5.486416,1.391178,6.902026]],[[-2.036669,8.766127,-5.985828],[3.162146,5.417579,9.482885],[0.975426,3.030470,2.724203],[6.569609,2.082220,-0.847216],[6.713381,-6.755529,4.250263],[-0.220379,-4.636276,-8.693758],[-7.110259,6.056603,-0.971186],[0.281951,-7.054361,4.623808],[0.218191,-8.432283,7.565804],[-4.783422,-0.052562,-0.557546]],[[-8.879329,4.767890,-0.711212],[4.753825,6.242110,3.987170],[7.300875,5.529326,3.907552],[7.370939,-8.299338,7.827059],[7.661941,-1.135876,9.644547],[6.036038,1.516206,-7.796780],[-7.156004,6.739642,-1.504768],[8.817089,8.097479,7.612712],[9.391550,7.864263,1.714132],[-6.331218,-8.365096,-8.099805]],[[6.745339,4.589871,7.357688],[-4.902427,-9.022756,6.350092],[-1.253728,-4.843766,-0.018943],[-5.353576,1.222451,4.577254],[0.331947,4.343607,-4.185942],[9.035078,9.582133,6.153813],[-1.210761,-1.571224,6.289969],[8.181116,-8.643518,2.964585],[9.746960,3.794068,9.095687],[3.872784,-8.713821,-8.049519]],[[4.714463,-8.815047,-6.808272],[5.332828,3.690810,3.297502],[0.208620,6.507152,0.430530],[-4.192276,-0.934259,8.157553],[-2.853948,-9.838095,9.449813],[-0.578753,-5.580369,6.594518],[-5.401462,5.063571,-4.511902],[-9.250100,3.526227,2.456850],[-8.055491,-0.755662,0.659880],[-4.539235,-6.564738,-3.780273]],[[1.874496,-6.726416,7.941718],[-3.870758,-8.923979,-3.297788],[8.848029,6.712343,-3.343790],[5.050396,-4.492469,8.171770],[8.355891,-8.604857,4.038159],[9.513745,0.693550,-2.358680],[4.472178,-8.169706,3.754220],[-2.534812,7.551507,3.750883],[-8.500617,-8.126083,-9.464519],[2.782567,6.308175,-1.536879]],[[-0.390698,4.704876,0.511439],[9.162047,-6.037132,6.252191],[-2.440880,-5.225706,5.199361],[3.039367,-4.823629,-4.871336],[4.126359,-2.031803,5.613592],[1.036605,-2.756637,6.075649],[2.628485,-7.927379,-6.017102],[2.832226,0.376324,-0.090293],[8.808680,6.511333,0.031900],[6.411102,4.808185,5.156853]],[[-5.138703,-9.809495,0.607723],[-1.225098,-1.005336,0.287438],[-8.369459,8.701155,-8.110721],[-3.471348,1.598154,-2.942893],[-5.866047,-4.843659,6.404849],[-0.674789,-7.413421,0.274379],[0.895185,-5.973638,-6.152820],[-9.961037,-8.326770,7.212414],[-6.892229,2.428050,0.195396],[-1.882571,6.837050,4.042715]],[[2.238309,-1.497702,-4.873308],[0.234078,0.250794,-4.690870],[1.817297,2.620973,-8.396806],[3.443522,-0.791453,2.483380],[-3.512896,8.228833,-5.302382],[-4.898683,9.002779,9.661941],[-6.009107,8.119497,5.418419],[-5.398216,-7.743892,-5.869273],[-4.073578,4.596637,-7.845261],[-4.667062,8.713558,-2.790730]],[[-4.754989,6.581493,0.075137],[3.723865,0.948388,-4.291000],[-5.183014,-4.185050,-7.048039],[-0.240083,-2.321803,1.925382],[-7.673410,4.532568,-9.374263],[6.484916,-8.120022,-7.925654],[1.603999,-7.387671,-6.384562],[1.656346,2.958811,5.033368],[1.519670,-9.902057,-9.722133],[-3.482606,4.041100,-5.554326]]], dtype = "float32")#candidate|5322|(11, 10, 3)|const|float32
bop_5323 = relay.floor_mod(call_5296.astype('float32'), relay.reshape(const_5322.astype('float32'), relay.shape_of(call_5296))) # shape=(11, 10, 3)
bop_5326 = relay.floor_mod(call_5297.astype('float32'), relay.reshape(const_5322.astype('float32'), relay.shape_of(call_5297))) # shape=(11, 10, 3)
output = relay.Tuple([bop_5323,])
output2 = relay.Tuple([bop_5326,])
func_5343 = relay.Function([], output)
mod['func_5343'] = func_5343
mod = relay.transform.InferType()(mod)
output = func_5343()
func_5344 = relay.Function([], output)
mutated_mod['func_5344'] = func_5344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mod.get_global_var('func_5343')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_5410 = relay.TupleGetItem(func_5343_call(), 0)
call_5411 = relay.TupleGetItem(func_5344_call(), 0)
func_1825_call = mod.get_global_var('func_1825')
func_1828_call = mutated_mod.get_global_var('func_1828')
const_5415 = relay.const([[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[True],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False]], dtype = "bool")#candidate|5415|(240, 1)|const|bool
call_5414 = relay.TupleGetItem(func_1825_call(relay.reshape(const_5415.astype('bool'), [8, 30])), 7)
call_5416 = relay.TupleGetItem(func_1828_call(relay.reshape(const_5415.astype('bool'), [8, 30])), 7)
uop_5422 = relay.sinh(call_5410.astype('float32')) # shape=(11, 10, 3)
uop_5424 = relay.sinh(call_5411.astype('float32')) # shape=(11, 10, 3)
func_2713_call = mod.get_global_var('func_2713')
func_2717_call = mutated_mod.get_global_var('func_2717')
var_5432 = relay.var("var_5432", dtype = "float64", shape = (750,))#candidate|5432|(750,)|var|float64
call_5431 = relay.TupleGetItem(func_2713_call(relay.reshape(var_5432.astype('float64'), [15, 10, 5]), relay.reshape(call_5414.astype('bool'), [240,]), ), 3)
call_5433 = relay.TupleGetItem(func_2717_call(relay.reshape(var_5432.astype('float64'), [15, 10, 5]), relay.reshape(call_5414.astype('bool'), [240,]), ), 3)
func_1963_call = mod.get_global_var('func_1963')
func_1965_call = mutated_mod.get_global_var('func_1965')
const_5435 = relay.const([[-10,-3],[10,-8],[-10,1],[-6,3],[-5,-4],[4,10],[8,-1],[-9,-4],[-7,3],[-3,-4],[-3,9],[3,9],[-6,7],[-6,7],[-6,-2],[1,-5],[5,6],[10,-2],[-6,4],[2,7],[4,-9],[-10,6],[-9,10],[-6,-10],[4,10],[-7,7],[-3,1],[4,-7],[-2,1],[-3,6],[5,1],[3,-4],[-7,-1],[9,8],[-10,-7],[-6,3],[1,8],[10,5],[1,9],[-9,-1],[9,3],[-1,-10],[-9,-3],[3,3],[-9,7],[8,-5],[2,-3],[8,7],[7,5],[-10,-6],[4,-4],[-7,-9],[1,-8],[-2,7],[6,2],[5,1],[-1,9],[3,-10],[7,2],[-4,-2],[8,3],[-2,3],[10,4],[-7,7],[-3,-1],[2,-1],[-9,4],[-5,8],[8,-5],[-2,10],[4,-9],[-1,2],[1,-8],[5,1],[-4,7],[5,3],[9,-6],[6,6],[2,-4],[-10,-6],[-8,-5],[6,10],[4,9],[5,3],[-2,8],[4,2],[7,-8],[-10,1],[9,-4],[-3,4],[2,-5],[7,-2],[6,9],[-1,-8],[4,-9],[-10,-6],[-6,3],[5,-5],[3,5],[-9,-9],[4,-4],[6,5],[-8,6],[-5,-9],[5,10],[-1,10],[-8,-4],[-1,-1],[8,1],[-7,-5],[3,5],[6,-10],[-7,-2],[9,4],[4,-4],[8,1],[1,1],[-10,-7],[8,2],[-7,4],[7,2],[-5,-5],[4,-5],[5,8],[9,5],[6,4],[-3,5],[-1,4],[4,-5],[-2,-9],[8,-9],[-1,10],[-8,1],[7,5],[2,-10],[10,2],[-9,2],[-5,-10],[-6,-7],[-7,9],[2,-9],[-3,-8],[6,-7],[-3,-10],[-6,-8],[5,4],[-6,-8],[-8,10],[5,8],[4,5],[6,-8],[-3,-3],[-3,7],[-8,9],[2,9],[-4,-9],[-8,9],[2,4],[7,9],[2,-6],[3,-3],[6,5],[9,9],[4,-4],[-4,-6],[8,6],[-4,5],[9,3],[5,-2],[-9,-1],[10,-2],[8,7],[-3,-8],[-5,-6],[1,6],[-3,1],[6,10],[-8,-4],[9,-5],[3,8],[-4,-7],[-3,7],[4,-6],[-4,-4],[-8,-6],[5,9],[3,2],[-5,-2],[-9,10],[-3,7],[-2,-4],[-8,7],[-5,4],[-10,-6],[6,-2],[8,-2],[4,10],[10,-5],[-10,1],[9,6],[2,4],[3,-6],[7,10],[4,4],[-5,-5],[2,7],[1,10],[7,-4],[5,10],[7,7],[-8,1],[10,-9],[-10,9],[-6,-5],[-6,7],[-10,4],[-8,-5],[4,10],[2,1],[-7,-6],[7,-8],[-4,2],[-8,5],[9,-7],[-6,3],[-6,-2],[-4,-10],[-5,7],[-4,7],[-10,9],[-7,9],[-6,2],[-9,-3],[-7,5],[8,-2],[6,5],[8,9],[10,-7],[-4,10],[3,3],[-6,-8],[9,-4],[-1,-10],[-8,6],[-8,4],[-2,-4],[9,8],[7,-5],[8,-3],[9,6],[6,6],[2,9],[-6,5],[-4,-8],[-4,-5],[8,3],[5,6],[5,-3],[-1,-4],[10,10],[-4,8],[5,-3],[2,1],[9,-7],[2,-6],[9,-8],[8,-1],[3,8],[8,9],[10,4],[1,-2],[-9,-3],[-6,8],[10,-8],[-7,-1],[-2,-10],[-3,-4],[3,6],[5,-4],[-1,-5],[-8,4],[8,10],[-3,-6],[8,-5],[-8,-7],[-9,5],[-5,8],[6,4],[-4,-3],[10,-8],[4,8],[-3,-6],[-2,-2],[-8,-4],[-3,-8],[4,4],[8,-2],[3,-3],[-7,1],[-4,1],[-10,8],[7,10],[4,1],[-7,8],[4,-8],[-4,-4],[-4,1],[3,-7],[-2,-2],[6,-10],[-9,-8],[6,6],[10,9],[-6,4],[-9,9],[6,5],[-10,-8],[-9,7],[-9,-6],[5,-7],[5,8],[10,-1],[-9,-2],[-8,-7],[-6,-5],[3,-2],[-10,-7],[10,9],[-1,-5],[9,3],[8,-4],[-4,3],[6,-4],[-3,-1],[-7,-8],[-6,2],[-4,-10],[5,-2],[9,-9],[9,-3],[-3,3],[-3,9],[-5,-9],[-3,-8],[-10,-1],[-4,-9],[-9,5],[2,2],[-5,1],[9,8],[-8,3],[-9,-8],[1,-5],[-2,-7],[-5,-8],[2,-2],[7,7],[-3,10],[-3,3],[-5,-1],[2,-1],[-10,-5],[5,-4],[7,6],[-9,-8],[7,6],[-2,-1],[1,3],[-6,8],[-7,5],[-10,8],[2,9],[-4,-6],[6,10],[10,-3],[3,-4],[4,-9],[7,-10],[-10,4],[2,-5],[-10,-9],[2,4],[-1,5],[-5,-5],[3,8],[5,-8],[-8,-8],[6,9],[6,-4],[-7,10],[-5,4],[-4,-9],[-10,-8],[6,-9],[-8,5],[2,-4],[1,-5],[-6,8],[2,1],[10,2],[6,-6],[-7,7],[4,1],[-7,4],[-3,-6],[-8,10],[6,-5],[-3,10],[-8,-4],[-3,-10],[4,-5],[-6,-6],[-10,10],[7,-7],[3,-3],[10,6],[10,-2],[-2,10],[-6,6],[5,-3]], dtype = "uint8")#candidate|5435|(420, 2)|const|uint8
call_5434 = relay.TupleGetItem(func_1963_call(relay.reshape(const_5435.astype('uint8'), [840,])), 0)
call_5436 = relay.TupleGetItem(func_1965_call(relay.reshape(const_5435.astype('uint8'), [840,])), 0)
output = relay.Tuple([call_5414,const_5415,uop_5422,call_5431,var_5432,call_5434,const_5435,])
output2 = relay.Tuple([call_5416,const_5415,uop_5424,call_5433,var_5432,call_5436,const_5435,])
func_5437 = relay.Function([var_5432,], output)
mod['func_5437'] = func_5437
mod = relay.transform.InferType()(mod)
var_5438 = relay.var("var_5438", dtype = "float64", shape = (750,))#candidate|5438|(750,)|var|float64
output = func_5437(var_5438)
func_5439 = relay.Function([var_5438], output)
mutated_mod['func_5439'] = func_5439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4745_call = mod.get_global_var('func_4745')
func_4747_call = mutated_mod.get_global_var('func_4747')
call_5477 = relay.TupleGetItem(func_4745_call(), 0)
call_5478 = relay.TupleGetItem(func_4747_call(), 0)
func_4583_call = mod.get_global_var('func_4583')
func_4584_call = mutated_mod.get_global_var('func_4584')
call_5505 = relay.TupleGetItem(func_4583_call(), 0)
call_5506 = relay.TupleGetItem(func_4584_call(), 0)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
call_5513 = func_2495_call()
call_5514 = func_2495_call()
output = relay.Tuple([call_5477,call_5505,call_5513,])
output2 = relay.Tuple([call_5478,call_5506,call_5514,])
func_5519 = relay.Function([], output)
mod['func_5519'] = func_5519
mod = relay.transform.InferType()(mod)
output = func_5519()
func_5520 = relay.Function([], output)
mutated_mod['func_5520'] = func_5520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
call_5524 = func_2495_call()
call_5525 = func_2495_call()
func_4318_call = mod.get_global_var('func_4318')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_5559 = relay.TupleGetItem(func_4318_call(), 0)
call_5560 = relay.TupleGetItem(func_4320_call(), 0)
output = relay.Tuple([call_5524,call_5559,])
output2 = relay.Tuple([call_5525,call_5560,])
func_5563 = relay.Function([], output)
mod['func_5563'] = func_5563
mod = relay.transform.InferType()(mod)
mutated_mod['func_5563'] = func_5563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5563_call = mutated_mod.get_global_var('func_5563')
call_5564 = func_5563_call()
output = call_5564
func_5565 = relay.Function([], output)
mutated_mod['func_5565'] = func_5565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4963_call = mod.get_global_var('func_4963')
func_4964_call = mutated_mod.get_global_var('func_4964')
call_5573 = relay.TupleGetItem(func_4963_call(), 0)
call_5574 = relay.TupleGetItem(func_4964_call(), 0)
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_5577 = func_2382_call()
call_5578 = func_2382_call()
func_2578_call = mod.get_global_var('func_2578')
func_2580_call = mutated_mod.get_global_var('func_2580')
call_5603 = func_2578_call()
call_5604 = func_2578_call()
func_3805_call = mod.get_global_var('func_3805')
func_3809_call = mutated_mod.get_global_var('func_3809')
const_5607 = relay.const([-4,6,-5,-10,1,1,5,-3,10,1,1,3,9,-4,-9,-7,-7,4,2,-10,-3,2,1,-9,9,4,-9,9,-5,9,3,8,8,4,7,4,-5,1,2,-10,9,-1,10,-6,-7,10,10,-8,9,10,-5,5,-1,-9,-6,5,2,-6,6,-9,7,-2,5,-5,1,-10,2,-10,4,7,8,-7,-8,3,5,6,1,-8,8,-1,-1,-9,8,7,9,-4,-5,-7,4,-6,4,-10,2,1,1,10,7,-6,-9,9,-6,4,3,-4,-5,-3,-4,4,-1,5,1,6,5,2,-5,-1,-5,-2,-8,5,-7,-4,3,9,5,8,9,3,-7,1,8,-3,-9,-1,-9,2,-7,1,4,-4,1,-6,-7,8,8,6,-1,10,1,-9,-10,-10,-9,4,8,4,-1,4,3,-10,3,-6,-4,-6,-8,9,8,-2,10,-10,-6,-2,7,5,-9,-9,-10,7,-1,-2,8,6,1,-2,-8,3,-7,2,-2,3,1,-6,-9,8,-7,-1,-10,-2,-7,-5,-9,10,5,1,9,3,-8,-3,-5,8,-1,-9,-6,-3,-7,7,-9,1,10,-5,8,1,8,-2,4,5,7,-6,4,5,10,-7,-10,6,2,1,3,5,-5,-6,-7,4,-4,-8,-2,4,-6,4,1,7,3,-5,-9,8,9,3,-5,-1,-9,-1,-3,-4,6,-6,10,-4,5,-9,-2,-8,-1,9,2,-8,3,2,2,5,-6,9,-8,8,2,8,4,-7,9,-2,-9,1,-10,8,-3,-2,-7,4,1,9,-9,9,4,-10,-5,-5,-5,-8,1,6,10,2,8,3,8,-7,10,10,-6,-9,5,5,10,4,1,7,8,9,5,-9,7,-2,4,2,-6,-10,5,-8,1,10,2,3,7,9,-5,7,-6,10,-4,-1,3,9,9,7,-1,-1,-4,-6,8,3,4,7,10,4,-10,-4,6,-3,5,4,6,-1,-10,1,10,3,-3,-8,8,9,-6,-10,-6,-5,4,-7,5,-3,4,-6,8,-2,10,4,-1,5,-5,8,-10,2,-4,-6,-6,-7,3,-5,-3,-1,-7,10,-7,-5,-3,-4,8,7,-5,-3,4,-1,3,5,5,8,3,9,-4,4,7,-10,-4,-9,2,3,-1,-2,-2,-10,-4,-10,8,-7,-6,-10,9,-10,-1,-5,10,-10,2,-7,10,3,6,1,5,-8,10,-3,-10,-3,1,-5,-6,2,-4,2,6,7,3,10,7,8,-6,4,4,-8,-5,-6,7,-9,-6,-4,-10,-8,9,8,6,3,7,-1,-7,5,-3,5,8,-10,4,-1,-4,-7,9,-1,1,8,-1,10,9,2,-8,-1,-10,5,4,8,6,-5,1,9,-9,-4,7,10,1,7,10,8,-10,2,8,6,-7,7,6,-2,5,7,1,-8,-1,4,5,-1,-4,1,-5,5], dtype = "uint8")#candidate|5607|(546,)|const|uint8
call_5606 = relay.TupleGetItem(func_3805_call(relay.reshape(const_5607.astype('uint8'), [7, 6, 13]), relay.reshape(const_5607.astype('uint8'), [7, 6, 13]), ), 1)
call_5608 = relay.TupleGetItem(func_3809_call(relay.reshape(const_5607.astype('uint8'), [7, 6, 13]), relay.reshape(const_5607.astype('uint8'), [7, 6, 13]), ), 1)
output = relay.Tuple([call_5573,call_5577,call_5603,call_5606,const_5607,])
output2 = relay.Tuple([call_5574,call_5578,call_5604,call_5608,const_5607,])
func_5612 = relay.Function([], output)
mod['func_5612'] = func_5612
mod = relay.transform.InferType()(mod)
output = func_5612()
func_5613 = relay.Function([], output)
mutated_mod['func_5613'] = func_5613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2578_call = mod.get_global_var('func_2578')
func_2580_call = mutated_mod.get_global_var('func_2580')
call_5621 = func_2578_call()
call_5622 = func_2578_call()
var_5638 = relay.var("var_5638", dtype = "float32", shape = (11, 10, 3))#candidate|5638|(11, 10, 3)|var|float32
bop_5639 = relay.logical_and(call_5621.astype('bool'), relay.reshape(var_5638.astype('bool'), relay.shape_of(call_5621))) # shape=(11, 10, 3)
bop_5642 = relay.logical_and(call_5622.astype('bool'), relay.reshape(var_5638.astype('bool'), relay.shape_of(call_5622))) # shape=(11, 10, 3)
func_2161_call = mod.get_global_var('func_2161')
func_2162_call = mutated_mod.get_global_var('func_2162')
call_5646 = func_2161_call()
call_5647 = func_2161_call()
func_2218_call = mod.get_global_var('func_2218')
func_2220_call = mutated_mod.get_global_var('func_2220')
call_5658 = relay.TupleGetItem(func_2218_call(), 0)
call_5659 = relay.TupleGetItem(func_2220_call(), 0)
output = relay.Tuple([bop_5639,call_5646,call_5658,])
output2 = relay.Tuple([bop_5642,call_5647,call_5659,])
func_5660 = relay.Function([var_5638,], output)
mod['func_5660'] = func_5660
mod = relay.transform.InferType()(mod)
mutated_mod['func_5660'] = func_5660
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5661 = relay.var("var_5661", dtype = "float32", shape = (11, 10, 3))#candidate|5661|(11, 10, 3)|var|float32
func_5660_call = mutated_mod.get_global_var('func_5660')
call_5662 = func_5660_call(var_5661)
output = call_5662
func_5663 = relay.Function([var_5661], output)
mutated_mod['func_5663'] = func_5663
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5707 = relay.const([[[-9,2,4,3,-5,-9,6,7,-6,6],[-2,-2,-2,-9,-5,4,-3,9,2,3],[-4,8,-6,1,3,-7,-4,5,-1,1],[-1,-9,1,4,-9,3,-1,-7,-9,10],[-4,7,5,-8,-6,2,3,-2,1,-10],[-2,6,-5,10,-1,-3,7,-7,-4,1],[-3,7,-6,10,4,-10,2,-2,10,10],[4,8,-5,-6,-7,9,9,8,5,-3],[-10,9,-10,1,-3,-1,4,10,2,6],[-2,1,-1,7,9,-8,4,4,-8,-1],[-6,10,2,7,6,5,-10,-9,7,8],[-7,-6,-4,4,5,-3,-10,1,4,5],[-3,8,-7,6,-5,10,1,-5,-8,4]],[[-4,6,-3,5,-5,7,-1,3,4,-1],[-4,-2,-9,-9,-6,4,-4,-4,-9,4],[1,4,-8,9,-6,2,-1,4,-3,-9],[-8,9,-5,-6,-5,-10,4,6,1,-6],[6,-9,-6,7,6,8,-2,5,-1,-4],[3,-3,-8,-9,-6,5,6,-7,7,-2],[1,-6,-9,10,1,-6,-8,1,10,4],[-6,-6,-3,7,-8,-4,8,-3,10,-7],[-9,-7,-4,2,10,-9,-7,1,1,-9],[-6,9,-2,1,6,-6,2,2,4,1],[-10,-2,-9,-6,-10,1,-9,-2,-3,-4],[10,3,-5,-2,-9,-3,-7,-7,-10,9],[9,8,10,-10,10,1,-5,-5,-7,9]],[[2,-4,-9,-5,3,8,4,1,-3,-7],[6,6,10,4,-8,5,7,7,10,6],[6,9,-10,-3,3,8,8,1,-5,7],[-9,5,2,5,-6,7,-3,-3,9,5],[-6,1,9,1,-8,1,-1,-5,-8,4],[9,5,10,-6,6,10,6,-5,3,1],[6,-9,8,-9,6,10,7,-1,5,-7],[-9,-2,-8,2,-5,-3,6,-10,-9,9],[-4,-3,6,1,1,10,-5,-7,-9,2],[-1,-7,-10,1,7,5,1,-4,1,-8],[-3,10,-3,9,-5,8,-8,5,3,7],[8,-1,9,-7,3,1,-4,-2,-10,-10],[3,-3,4,-1,5,-7,10,-5,-5,9]],[[6,4,3,-8,10,-7,8,6,-9,-9],[6,9,-7,-5,7,-10,4,-4,3,-9],[9,-6,8,-1,10,3,-7,10,-9,6],[-10,8,2,10,-3,8,7,-1,7,-3],[-1,1,-9,1,7,-1,-6,9,-10,-5],[2,-4,-9,-5,8,-1,2,-6,2,-8],[-7,-4,-7,-4,5,-9,5,5,10,-10],[8,7,3,1,-3,4,8,-6,4,4],[-7,6,6,-6,3,-7,7,-1,9,6],[2,3,-2,7,-9,5,3,10,7,10],[-1,-3,10,9,-7,-1,-6,1,5,4],[-10,-10,2,-6,5,1,2,-4,-7,4],[-7,2,-3,-9,-10,2,2,3,-1,3]],[[5,-4,5,3,-9,7,-4,-9,-2,5],[1,-2,-9,-7,5,8,3,9,10,-1],[9,-6,6,9,-4,-10,10,-8,-8,-1],[4,-7,3,-6,-7,3,6,8,7,-10],[2,7,-1,-2,9,-5,3,1,-7,-1],[5,-10,-5,3,-8,2,2,-1,-4,3],[6,-8,10,-7,8,1,1,-6,-2,8],[-1,-9,2,5,4,-9,10,3,7,-6],[7,-8,-1,-7,-3,-4,-7,-7,-4,5],[4,2,3,3,7,-5,-9,5,7,-4],[8,5,10,6,-6,-3,7,4,1,10],[-9,4,-7,-9,-2,-3,10,6,9,5],[3,8,3,9,-3,4,3,-1,9,-3]],[[4,9,-5,5,7,1,-10,-9,3,9],[-9,8,-2,-4,-1,-2,-4,-3,8,-3],[10,6,-5,2,-6,-5,-5,9,-4,-8],[2,3,3,-7,4,7,-5,1,-1,-9],[-4,-4,-9,-6,-5,-1,-6,-5,8,1],[1,5,4,-8,-1,-2,3,-5,8,-7],[-8,2,-1,-3,8,-3,4,4,6,-3],[-1,3,10,6,9,-2,2,-1,2,3],[7,-6,-4,9,4,-6,-6,7,-8,5],[-8,4,-3,-2,8,3,-1,-10,-3,4],[2,2,-10,-5,4,4,9,2,5,-4],[-9,-2,-8,-5,1,8,-9,3,-9,-6],[8,-5,-1,8,-10,9,-9,-2,-3,-10]],[[8,10,-8,7,-9,2,-6,-6,-5,1],[7,7,-2,5,-7,2,2,-5,2,8],[6,3,-7,8,-1,7,10,-4,-4,8],[5,-9,1,-5,-5,-8,-3,4,8,-9],[-1,-9,-2,-3,-3,2,-2,-4,6,-10],[2,-3,-9,-4,6,-7,2,8,-10,-4],[4,10,-6,3,-4,2,-10,-1,-1,5],[-8,6,10,-6,7,-3,6,8,-8,4],[3,9,3,10,5,-5,10,5,-7,10],[10,6,-7,-8,7,-8,-9,4,7,8],[-1,-4,-6,3,-9,9,6,-5,-4,-1],[-4,1,-8,-7,-9,6,10,3,1,1],[-8,-9,-8,1,-7,10,1,-7,8,-3]],[[-3,-9,1,10,9,-9,-2,3,-3,1],[-7,1,4,-7,4,-1,9,1,-3,1],[2,1,8,-5,8,-9,7,-5,10,5],[-3,2,-8,3,1,3,4,9,-8,3],[10,-5,3,-10,-1,8,3,6,-10,3],[3,-9,10,10,-4,-7,6,3,-1,4],[-10,-6,4,-4,-10,-8,-3,-1,4,-2],[-4,-3,3,2,1,-6,10,-3,1,-1],[-2,-6,-7,-7,-8,-1,2,-5,-2,-8],[2,-3,3,9,5,9,-10,-4,1,7],[-2,4,-4,10,-5,-6,-2,1,7,3],[1,-1,4,7,-7,-9,-7,-5,-1,5],[-3,2,2,-3,5,-2,6,9,-9,7]],[[5,4,-8,-10,-2,-4,-8,10,-2,-2],[7,-5,-9,2,1,1,5,5,-4,10],[-2,1,-3,-9,-2,-1,-4,1,-9,9],[-2,7,8,1,-8,8,-7,7,7,-4],[6,-1,2,-4,-5,-2,-5,-6,-10,7],[-8,-8,-1,5,-1,-1,4,7,-4,-8],[4,-9,8,6,-2,6,5,7,8,-7],[10,-6,-10,10,-4,4,-8,-10,8,-4],[6,-2,-5,8,8,-2,5,-3,-3,-2],[1,8,9,-6,4,9,2,-3,-8,-2],[-10,7,4,-2,-4,7,-10,-5,-5,-8],[-10,10,-8,-1,-8,5,9,3,3,-4],[8,2,-8,-7,-7,3,1,1,10,6]],[[-7,6,-4,-9,4,5,5,-10,-4,6],[-3,1,4,-1,-6,-10,7,-6,5,-9],[-1,1,-2,8,9,9,5,-5,-2,1],[3,-8,7,3,-3,1,9,-1,2,-8],[5,2,-7,-7,3,-6,9,-9,2,-10],[-6,-9,2,5,9,-6,3,4,-7,1],[-1,8,-3,-8,-9,-9,9,10,-10,-7],[8,-5,1,3,2,-10,4,-5,-3,3],[-3,-6,2,4,-1,-1,4,2,-5,5],[-2,2,-3,3,2,-7,-8,-7,-9,2],[-4,8,9,5,-8,3,7,6,-4,3],[6,-9,5,7,-9,-3,-2,-10,3,-6],[8,-1,-7,-3,5,-7,8,-7,3,6]],[[-3,-4,-1,7,-10,7,6,-10,-4,-6],[-1,-1,-10,-3,-10,-9,-9,9,7,-6],[-3,-4,-10,2,9,4,-2,2,-3,8],[-5,8,8,-6,5,4,4,7,-4,7],[-8,5,5,-1,-4,2,4,5,-9,-8],[4,4,-10,1,1,-7,-10,8,-2,4],[8,5,-5,-5,-3,9,-7,-5,-6,-10],[8,-6,10,4,3,-7,-5,4,-5,4],[-3,5,-8,6,-9,-10,4,7,-10,-7],[10,-7,-6,-3,-1,9,4,4,6,-5],[-6,2,-3,-3,10,9,4,3,6,-3],[6,10,5,9,6,6,1,10,-9,-6],[-3,-10,-10,8,-2,-2,4,6,8,3]]], dtype = "int64")#candidate|5707|(11, 13, 10)|const|int64
const_5708 = relay.const([[[8,3,4,-9,-4,2,9,8,-8,-6],[3,-3,1,3,5,9,-9,5,10,-2],[2,-2,-3,-6,-1,-1,-6,-3,8,4],[1,9,8,1,-7,-2,-6,-1,3,10],[-10,2,-5,7,-10,-9,6,9,1,4],[5,-4,-10,-2,2,9,-2,2,-6,3],[9,5,9,9,-7,5,-1,-5,-5,4],[-8,1,-5,-9,9,-7,3,4,-9,1],[8,-10,-6,7,-3,-1,5,-2,3,1],[5,-10,1,2,7,-6,1,3,2,-3],[1,5,-3,6,8,10,5,-4,4,-6],[1,-5,7,-2,-5,3,6,-4,5,-7],[-7,-10,8,1,-2,-10,-1,5,-2,9]],[[1,-5,-10,-10,-1,1,5,-2,-5,-5],[-2,-10,-2,10,-4,-3,-1,-4,9,9],[2,-8,1,-1,5,-5,-3,-7,-2,8],[6,-10,10,-9,9,-1,-7,-9,-10,-9],[8,-1,1,-5,7,-8,5,-1,2,-5],[9,4,-4,-8,-7,1,-3,6,2,-6],[3,5,1,-2,-7,6,3,-4,4,3],[-9,5,-7,-5,-2,-2,-8,-4,3,2],[5,8,7,-4,1,2,-2,-3,8,9],[-2,7,-6,-7,-9,8,8,-9,-7,-7],[10,10,8,10,3,8,-8,3,7,2],[-2,7,8,6,1,-4,5,-3,-9,-9],[-2,-8,-3,4,-3,-4,-1,-5,-9,4]],[[8,-10,-4,-6,-8,7,-3,2,-6,-5],[-7,3,2,-4,-3,-2,6,4,7,-5],[6,-6,-7,-6,-7,1,4,9,-4,-8],[1,7,-1,9,2,4,-10,-8,1,9],[7,-3,5,-6,6,7,-3,7,5,4],[4,5,10,-10,-9,10,-10,-6,4,-6],[-7,8,-9,-8,2,2,-1,9,-10,4],[-7,-5,9,4,7,-6,4,8,10,8],[7,-10,-6,-10,10,-6,-10,4,6,5],[-9,-10,4,4,2,-7,-1,7,-8,4],[5,-6,2,-4,-9,4,7,-9,-9,-6],[7,2,-2,5,-10,-9,10,-9,7,-3],[-2,2,-8,-2,-8,-2,2,2,4,6]],[[-6,-8,2,9,1,-4,8,4,-1,-4],[7,-3,-1,4,2,-1,7,-7,9,6],[7,-4,-10,-2,7,9,4,-4,6,-2],[8,-9,3,3,1,3,-1,-4,9,1],[1,-1,-3,2,3,-10,-7,7,4,-3],[9,-2,5,3,-9,10,-8,9,-6,-1],[-4,1,9,-1,-9,-5,-2,-1,2,-1],[-10,-2,-3,-8,-1,9,9,7,9,-10],[-4,-9,1,-3,5,3,-6,4,8,-8],[2,-6,-9,-10,1,-9,4,-1,-7,9],[8,-7,-8,4,4,5,-1,-8,4,-1],[7,-1,-7,9,5,-7,-1,7,-7,5],[3,7,3,-4,-1,-3,4,-1,-4,-8]],[[10,4,-2,-1,2,-10,10,-10,-3,1],[1,4,9,10,-8,4,6,9,9,-8],[-8,7,-8,-10,-5,-6,-6,-4,8,8],[-4,5,-2,-9,4,3,8,7,-9,10],[1,-2,6,2,2,9,-4,-6,-9,-7],[-2,5,2,-9,-1,7,-5,-9,-5,-5],[2,-2,10,-5,5,-4,-4,-9,10,-1],[9,5,7,6,-6,10,9,-8,-2,-10],[7,-3,10,9,-4,-3,8,-10,3,-8],[9,10,-2,8,1,10,-1,-1,7,-3],[10,-5,-5,3,10,-8,1,-8,-6,8],[4,7,3,8,-8,2,-8,-6,3,-2],[3,4,8,7,-6,-5,-3,6,10,5]],[[-5,-8,3,8,3,8,10,10,-4,5],[-1,2,3,-7,4,-3,-8,-3,-4,6],[-3,-5,-8,2,-3,-6,7,8,8,5],[7,2,-10,4,-8,-5,-9,-5,-7,-1],[-5,-5,-4,4,-6,1,-6,9,-10,10],[-5,8,-5,-1,9,3,8,6,-8,-2],[-9,10,-8,1,-1,-5,-6,-10,-7,5],[4,9,5,2,8,-10,6,2,8,-3],[4,7,2,-5,10,-4,8,-4,1,-10],[9,5,1,-3,-1,-10,-4,-9,6,-3],[3,-1,-1,8,1,10,-8,-9,-4,-10],[7,-2,-6,-5,-4,-9,8,-10,4,-10],[3,-7,8,-10,8,-7,-9,-6,-9,-9]],[[1,-10,7,7,-5,8,-8,-1,-3,-9],[10,-4,5,5,-10,9,-4,10,6,-5],[-4,-10,-10,-9,3,-3,-5,3,-6,-6],[-5,-10,1,-2,-7,1,-10,6,-4,-4],[-4,-10,-4,9,-3,10,7,9,-2,-8],[-6,2,9,-7,-10,10,7,-3,2,3],[-6,-5,3,-4,3,-3,10,-6,-3,4],[5,9,3,-3,3,-4,6,-3,-1,5],[-6,2,6,-5,-2,-2,2,-7,1,-3],[5,-3,-5,2,-3,10,7,-5,2,10],[10,9,3,-8,7,1,1,2,2,3],[-1,5,7,-1,-10,4,-2,2,10,-10],[-3,6,-6,-9,-2,-2,-7,1,4,4]],[[-2,6,9,1,-7,-6,-1,6,1,-4],[10,-8,-2,9,-2,4,1,-9,-5,2],[1,-6,-10,-2,10,8,3,-4,-6,4],[8,-3,5,9,-4,4,9,-2,4,4],[1,1,7,-10,10,10,-10,-7,8,-5],[-7,10,2,-6,5,10,1,9,-9,-10],[2,9,4,-7,3,5,-4,7,4,-2],[-3,-4,-4,-2,-1,-3,2,-5,7,-7],[7,-2,6,6,-3,8,3,-2,-2,-1],[7,-5,6,-3,1,5,3,-8,-7,8],[5,7,7,-6,-4,-1,-8,7,-6,9],[2,7,3,6,-2,-9,-8,6,6,4],[6,10,-4,2,-9,9,-6,9,-2,1]],[[-7,10,9,-3,-7,-4,6,10,10,10],[-4,-1,5,-10,-4,8,1,1,5,4],[2,-8,-3,8,10,-3,9,5,-5,-1],[-5,-2,-9,8,-8,-10,2,9,-6,-1],[7,3,9,1,4,-4,-3,7,1,9],[-10,8,-7,-7,5,1,1,9,-1,-5],[4,-6,-6,-8,10,4,6,-2,-10,6],[-9,9,-1,2,-1,-9,-6,10,9,9],[-7,1,-7,-6,4,-2,9,6,2,-3],[5,-5,-8,3,7,9,4,-9,3,-8],[7,3,-1,-7,-5,5,-4,-10,-9,10],[-4,-2,-8,-7,-6,9,5,1,-9,3],[1,-5,-10,7,-10,7,-5,2,10,4]],[[4,-1,-5,9,3,9,9,8,1,-1],[4,4,-7,-5,-6,2,4,3,6,-5],[-3,2,10,-3,5,3,10,-1,4,3],[-4,-3,6,8,-7,10,9,4,-2,-2],[1,-8,-5,-7,2,-10,-2,-5,-9,2],[-5,-8,4,4,8,-3,-3,9,8,6],[5,8,-1,8,7,-5,-10,-9,-4,-10],[-10,1,-4,1,6,3,5,9,-4,5],[-6,-4,-5,3,-5,-4,-8,8,5,3],[7,5,5,10,-2,1,-9,-8,-9,4],[6,8,-2,3,6,-1,9,-6,1,-6],[-5,2,-5,8,1,-7,-3,8,-3,-5],[6,3,1,2,9,6,6,-8,6,4]],[[-2,-2,-7,-10,-1,9,-2,-3,-4,-6],[4,5,-8,10,2,1,4,-1,-4,-1],[-8,4,-3,-3,-3,-9,9,-6,8,-2],[9,-8,-7,-4,-10,7,7,7,10,8],[9,10,-1,6,2,2,9,4,9,-8],[7,6,-9,-4,3,2,-7,-9,-1,-8],[10,4,-9,7,8,-6,1,9,-5,8],[-6,9,5,2,4,8,-1,5,-3,-8],[8,-6,-6,-8,9,-10,-8,-8,10,10],[-1,7,-3,2,5,-4,3,-3,-6,-1],[-8,-8,3,-9,6,-6,10,-9,-6,-6],[10,-5,2,4,-10,3,-10,-4,10,8],[5,-3,5,-7,-4,3,4,8,5,-6]]], dtype = "int64")#candidate|5708|(11, 13, 10)|const|int64
bop_5709 = relay.greater_equal(const_5707.astype('bool'), relay.reshape(const_5708.astype('bool'), relay.shape_of(const_5707))) # shape=(11, 13, 10)
output = bop_5709
output2 = bop_5709
func_5715 = relay.Function([], output)
mod['func_5715'] = func_5715
mod = relay.transform.InferType()(mod)
mutated_mod['func_5715'] = func_5715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5715_call = mutated_mod.get_global_var('func_5715')
call_5716 = func_5715_call()
output = call_5716
func_5717 = relay.Function([], output)
mutated_mod['func_5717'] = func_5717
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5718 = relay.const(-3, dtype = "int16")#candidate|5718|()|const|int16
var_5719 = relay.var("var_5719", dtype = "int16", shape = (6, 1, 11))#candidate|5719|(6, 1, 11)|var|int16
bop_5720 = relay.logical_xor(const_5718.astype('int16'), var_5719.astype('int16')) # shape=(6, 1, 11)
output = relay.Tuple([bop_5720,])
output2 = relay.Tuple([bop_5720,])
func_5734 = relay.Function([var_5719,], output)
mod['func_5734'] = func_5734
mod = relay.transform.InferType()(mod)
var_5735 = relay.var("var_5735", dtype = "int16", shape = (6, 1, 11))#candidate|5735|(6, 1, 11)|var|int16
output = func_5734(var_5735)
func_5736 = relay.Function([var_5735], output)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5743 = relay.var("var_5743", dtype = "bool", shape = (15, 8, 16))#candidate|5743|(15, 8, 16)|var|bool
var_5744 = relay.var("var_5744", dtype = "bool", shape = (15, 8, 16))#candidate|5744|(15, 8, 16)|var|bool
bop_5745 = relay.logical_or(var_5743.astype('bool'), relay.reshape(var_5744.astype('bool'), relay.shape_of(var_5743))) # shape=(15, 8, 16)
func_3912_call = mod.get_global_var('func_3912')
func_3914_call = mutated_mod.get_global_var('func_3914')
var_5757 = relay.var("var_5757", dtype = "bool", shape = (99,))#candidate|5757|(99,)|var|bool
call_5756 = relay.TupleGetItem(func_3912_call(relay.reshape(var_5757.astype('bool'), [11, 9])), 0)
call_5758 = relay.TupleGetItem(func_3914_call(relay.reshape(var_5757.astype('bool'), [11, 9])), 0)
output = relay.Tuple([bop_5745,call_5756,var_5757,])
output2 = relay.Tuple([bop_5745,call_5758,var_5757,])
func_5759 = relay.Function([var_5743,var_5744,var_5757,], output)
mod['func_5759'] = func_5759
mod = relay.transform.InferType()(mod)
var_5760 = relay.var("var_5760", dtype = "bool", shape = (15, 8, 16))#candidate|5760|(15, 8, 16)|var|bool
var_5761 = relay.var("var_5761", dtype = "bool", shape = (15, 8, 16))#candidate|5761|(15, 8, 16)|var|bool
var_5762 = relay.var("var_5762", dtype = "bool", shape = (99,))#candidate|5762|(99,)|var|bool
output = func_5759(var_5760,var_5761,var_5762,)
func_5763 = relay.Function([var_5760,var_5761,var_5762,], output)
mutated_mod['func_5763'] = func_5763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
call_5768 = func_2495_call()
call_5769 = func_2495_call()
output = relay.Tuple([call_5768,])
output2 = relay.Tuple([call_5769,])
func_5770 = relay.Function([], output)
mod['func_5770'] = func_5770
mod = relay.transform.InferType()(mod)
mutated_mod['func_5770'] = func_5770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5770_call = mutated_mod.get_global_var('func_5770')
call_5771 = func_5770_call()
output = call_5771
func_5772 = relay.Function([], output)
mutated_mod['func_5772'] = func_5772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mod.get_global_var('func_3542')
func_3544_call = mutated_mod.get_global_var('func_3544')
call_5773 = relay.TupleGetItem(func_3542_call(), 3)
call_5774 = relay.TupleGetItem(func_3544_call(), 3)
func_5660_call = mod.get_global_var('func_5660')
func_5663_call = mutated_mod.get_global_var('func_5663')
call_5777 = relay.TupleGetItem(func_5660_call(relay.reshape(call_5773.astype('float32'), [11, 10, 3])), 0)
call_5778 = relay.TupleGetItem(func_5663_call(relay.reshape(call_5773.astype('float32'), [11, 10, 3])), 0)
func_5437_call = mod.get_global_var('func_5437')
func_5439_call = mutated_mod.get_global_var('func_5439')
var_5785 = relay.var("var_5785", dtype = "float64", shape = (750,))#candidate|5785|(750,)|var|float64
call_5784 = relay.TupleGetItem(func_5437_call(relay.reshape(var_5785.astype('float64'), [750,])), 4)
call_5786 = relay.TupleGetItem(func_5439_call(relay.reshape(var_5785.astype('float64'), [750,])), 4)
bop_5787 = relay.logical_or(call_5784.astype('bool'), relay.reshape(var_5785.astype('bool'), relay.shape_of(call_5784))) # shape=(750,)
bop_5790 = relay.logical_or(call_5786.astype('bool'), relay.reshape(var_5785.astype('bool'), relay.shape_of(call_5786))) # shape=(750,)
output = relay.Tuple([call_5773,call_5777,bop_5787,])
output2 = relay.Tuple([call_5774,call_5778,bop_5790,])
func_5796 = relay.Function([var_5785,], output)
mod['func_5796'] = func_5796
mod = relay.transform.InferType()(mod)
var_5797 = relay.var("var_5797", dtype = "float64", shape = (750,))#candidate|5797|(750,)|var|float64
output = func_5796(var_5797)
func_5798 = relay.Function([var_5797], output)
mutated_mod['func_5798'] = func_5798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2578_call = mod.get_global_var('func_2578')
func_2580_call = mutated_mod.get_global_var('func_2580')
call_5935 = func_2578_call()
call_5936 = func_2578_call()
output = relay.Tuple([call_5935,])
output2 = relay.Tuple([call_5936,])
func_5937 = relay.Function([], output)
mod['func_5937'] = func_5937
mod = relay.transform.InferType()(mod)
output = func_5937()
func_5938 = relay.Function([], output)
mutated_mod['func_5938'] = func_5938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5770_call = mod.get_global_var('func_5770')
func_5772_call = mutated_mod.get_global_var('func_5772')
call_5993 = relay.TupleGetItem(func_5770_call(), 0)
call_5994 = relay.TupleGetItem(func_5772_call(), 0)
output = relay.Tuple([call_5993,])
output2 = relay.Tuple([call_5994,])
func_6030 = relay.Function([], output)
mod['func_6030'] = func_6030
mod = relay.transform.InferType()(mod)
output = func_6030()
func_6031 = relay.Function([], output)
mutated_mod['func_6031'] = func_6031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2853_call = mod.get_global_var('func_2853')
func_2854_call = mutated_mod.get_global_var('func_2854')
call_6130 = func_2853_call()
call_6131 = func_2853_call()
output = call_6130
output2 = call_6131
func_6136 = relay.Function([], output)
mod['func_6136'] = func_6136
mod = relay.transform.InferType()(mod)
output = func_6136()
func_6137 = relay.Function([], output)
mutated_mod['func_6137'] = func_6137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1866_call = mutated_mod.get_global_var('func_1866')
call_6173 = relay.TupleGetItem(func_1864_call(), 0)
call_6174 = relay.TupleGetItem(func_1866_call(), 0)
output = relay.Tuple([call_6173,])
output2 = relay.Tuple([call_6174,])
func_6195 = relay.Function([], output)
mod['func_6195'] = func_6195
mod = relay.transform.InferType()(mod)
mutated_mod['func_6195'] = func_6195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6195_call = mutated_mod.get_global_var('func_6195')
call_6196 = func_6195_call()
output = call_6196
func_6197 = relay.Function([], output)
mutated_mod['func_6197'] = func_6197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3572_call = mod.get_global_var('func_3572')
func_3574_call = mutated_mod.get_global_var('func_3574')
call_6298 = func_3572_call()
call_6299 = func_3572_call()
uop_6310 = relay.acosh(call_6298.astype('float32')) # shape=(11, 10, 3)
uop_6312 = relay.acosh(call_6299.astype('float32')) # shape=(11, 10, 3)
func_5162_call = mod.get_global_var('func_5162')
func_5164_call = mutated_mod.get_global_var('func_5164')
call_6323 = func_5162_call()
call_6324 = func_5162_call()
output = relay.Tuple([uop_6310,call_6323,])
output2 = relay.Tuple([uop_6312,call_6324,])
func_6327 = relay.Function([], output)
mod['func_6327'] = func_6327
mod = relay.transform.InferType()(mod)
output = func_6327()
func_6328 = relay.Function([], output)
mutated_mod['func_6328'] = func_6328
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6408 = relay.var("var_6408", dtype = "int16", shape = (1, 1, 3))#candidate|6408|(1, 1, 3)|var|int16
var_6409 = relay.var("var_6409", dtype = "int16", shape = (10, 13, 3))#candidate|6409|(10, 13, 3)|var|int16
bop_6410 = relay.add(var_6408.astype('int16'), var_6409.astype('int16')) # shape=(10, 13, 3)
const_6424 = relay.const([[[-9,4,-7],[2,5,-9]],[[8,2,5],[-4,-10,-10]],[[8,-10,5],[8,10,-5]],[[5,3,1],[-2,7,8]],[[8,8,8],[8,9,4]],[[-10,7,-4],[-7,2,-10]],[[3,-1,6],[2,-9,1]],[[-8,5,7],[-5,-4,8]],[[-7,-9,-4],[1,5,-10]],[[1,-4,-2],[-10,-5,2]],[[-6,10,-9],[8,-3,4]],[[-7,7,-5],[2,6,-8]],[[2,3,-5],[-9,1,-9]],[[-8,-6,-1],[8,-5,10]],[[9,8,10],[8,-4,-9]]], dtype = "int16")#candidate|6424|(15, 2, 3)|const|int16
bop_6425 = relay.minimum(var_6408.astype('int64'), const_6424.astype('int64')) # shape=(15, 2, 3)
func_1316_call = mod.get_global_var('func_1316')
func_1320_call = mutated_mod.get_global_var('func_1320')
const_6443 = relay.const([6.111687,6.767010,-2.875689,-9.738139,8.059331,-1.759538,7.837780,-3.855763,7.457599,-6.649994,2.436233,0.913152,-2.938295,-3.913073,1.886910,-5.184853,-7.460395,9.915129,-2.568220,-5.944354,-1.436487,-1.547417,-6.068387,-1.885599,7.709653,-5.914882,-7.695020,-4.923761,-1.996213,-6.476103,0.334805,8.676056,-2.872437,4.837861,-6.445036,-2.449218,-6.030286,-2.935871,9.586398,-0.376647,6.336187,-6.185260,9.124027,6.950481,2.019589,4.680621,-0.578137,-7.446264,8.375804,1.326776,5.589572,-2.693086,3.781217,9.567334,8.514209,7.024314,-0.692746,-8.621716,3.078940,5.705095,2.104029,2.390522,5.582298,9.172972,2.391167,-9.085799,-6.141761,-1.444143,-9.209020,9.989772,-5.778197,-9.926446,-9.665178,-2.109084,-0.652481,-8.944815,-4.660963,3.496537,1.683189,-1.473252,-8.815208,4.489356,1.892767,-2.283352,5.665160,8.104739,-0.696126,-0.665237,8.218179,-7.895557,2.278818,1.959983,0.119639,9.459260,8.939482,2.832417,4.677981,7.680185,1.855302,-8.099595,8.415996,-2.639241,2.199890,-6.868596,2.719578,1.595542,2.195448,-9.179822,5.409801,7.330293,9.567329,-1.975086,3.776482,0.015435,5.102411,-8.097721,3.967561,8.906362,7.612473,3.195717,-3.879978,5.918587,-9.321662,-2.294980,-5.346090,-3.620531,9.337953,-9.297061,-4.478701,7.973539,4.642902,-8.999164], dtype = "float32")#candidate|6443|(132,)|const|float32
var_6444 = relay.var("var_6444", dtype = "bool", shape = (432,))#candidate|6444|(432,)|var|bool
call_6442 = relay.TupleGetItem(func_1316_call(relay.reshape(const_6443.astype('float32'), [11, 12]), relay.reshape(var_6444.astype('bool'), [2, 216]), ), 1)
call_6445 = relay.TupleGetItem(func_1320_call(relay.reshape(const_6443.astype('float32'), [11, 12]), relay.reshape(var_6444.astype('bool'), [2, 216]), ), 1)
output = relay.Tuple([bop_6410,bop_6425,call_6442,const_6443,var_6444,])
output2 = relay.Tuple([bop_6410,bop_6425,call_6445,const_6443,var_6444,])
func_6451 = relay.Function([var_6408,var_6409,var_6444,], output)
mod['func_6451'] = func_6451
mod = relay.transform.InferType()(mod)
mutated_mod['func_6451'] = func_6451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6451_call = mutated_mod.get_global_var('func_6451')
var_6453 = relay.var("var_6453", dtype = "int16", shape = (1, 1, 3))#candidate|6453|(1, 1, 3)|var|int16
var_6454 = relay.var("var_6454", dtype = "int16", shape = (10, 13, 3))#candidate|6454|(10, 13, 3)|var|int16
var_6455 = relay.var("var_6455", dtype = "bool", shape = (432,))#candidate|6455|(432,)|var|bool
call_6452 = func_6451_call(var_6453,var_6454,var_6455,)
output = call_6452
func_6456 = relay.Function([var_6453,var_6454,var_6455,], output)
mutated_mod['func_6456'] = func_6456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mod.get_global_var('func_5343')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_6458 = relay.TupleGetItem(func_5343_call(), 0)
call_6459 = relay.TupleGetItem(func_5344_call(), 0)
func_3975_call = mod.get_global_var('func_3975')
func_3978_call = mutated_mod.get_global_var('func_3978')
call_6477 = relay.TupleGetItem(func_3975_call(relay.reshape(call_6458.astype('float32'), [11, 10, 3])), 3)
call_6478 = relay.TupleGetItem(func_3978_call(relay.reshape(call_6458.astype('float32'), [11, 10, 3])), 3)
output = relay.Tuple([call_6458,call_6477,])
output2 = relay.Tuple([call_6459,call_6478,])
func_6481 = relay.Function([], output)
mod['func_6481'] = func_6481
mod = relay.transform.InferType()(mod)
output = func_6481()
func_6482 = relay.Function([], output)
mutated_mod['func_6482'] = func_6482
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6543 = relay.const([[[-1.287075,-4.926618,2.108821,9.966060,0.173656,-8.933628,-5.972432,-4.795267],[-6.481155,-3.577139,7.307097,6.644005,-3.442222,5.621408,-9.987515,-5.526283],[-9.058307,-7.433158,-0.447943,-9.162864,7.578575,0.999448,-8.809706,-1.761992],[3.927336,4.702359,3.526334,-9.485274,-0.111040,1.551137,-8.001352,1.373877],[-0.353633,1.330212,7.802856,-5.873496,-4.627396,-6.754995,-1.949945,2.340957],[-6.056429,-8.483719,9.490876,1.041394,-8.027472,4.181270,-1.797985,-2.577984],[-3.272449,3.472051,1.159241,-1.762136,-1.646657,6.480657,-1.451838,-6.605830],[8.426383,-8.799910,-0.419419,9.433576,-7.649879,7.024923,3.154198,3.966495],[3.296924,-5.144731,3.684441,-7.297997,4.425261,-0.250224,5.575862,-7.540006],[1.923795,1.026007,-1.077627,7.431209,6.467178,3.661664,-6.627599,-6.757042],[-4.504748,-2.630549,-5.473649,3.768292,-9.665665,0.864600,-2.524316,2.688099],[-6.547346,5.528621,5.167948,-5.055442,-1.967661,7.004942,-1.039881,-6.393947]],[[-7.112857,-5.564540,-5.530539,6.154587,9.240585,-0.593893,-1.953139,-0.534321],[-1.520017,-1.327013,-0.895604,8.483592,-2.841540,9.739608,-1.676559,9.366728],[-1.681553,0.723599,3.444508,-3.211383,5.241837,0.589278,-2.319192,8.701867],[0.280638,-2.256345,-1.748043,-7.070178,-1.573810,7.804398,-0.656663,-1.451463],[3.598420,5.136807,-5.584069,4.216047,-7.192724,5.162555,-3.446556,3.318685],[-7.124658,3.199633,0.124220,-6.171454,5.830729,6.199515,-3.045450,1.146500],[2.698451,4.316888,-6.933147,-0.009720,5.656321,0.234314,-6.264756,6.099104],[-5.505760,3.282408,2.462747,2.656529,5.009543,-0.507641,-0.841535,2.710197],[-2.922033,5.063742,-1.163144,2.951337,-3.282018,0.684729,1.039637,7.945278],[-6.571120,-9.284166,-2.632788,-3.827041,-5.293213,-7.406478,-7.683708,-3.624039],[-8.740532,7.137926,7.616761,-1.857090,9.170529,-4.556059,-7.869035,-8.177300],[-4.728534,-4.549184,7.634156,3.246523,7.464131,-9.085197,6.300726,-3.872691]],[[9.894416,-8.749974,-8.957264,-6.832058,7.653773,9.394082,-6.719417,-2.448678],[-1.651595,-7.618557,0.123772,6.254789,8.776187,7.286750,-8.733756,-6.599088],[8.813296,8.213321,6.243154,-9.777736,-9.796275,-6.671226,6.627658,-7.661363],[-9.588901,6.626602,-5.090940,-4.020909,2.304058,-7.242721,-9.507350,4.326679],[-5.350500,2.456003,-4.174167,-8.517617,3.522004,6.375930,1.862852,-3.491717],[-6.378327,2.332677,-0.285597,-5.089007,7.375887,-9.774971,7.170980,-1.593469],[-3.223883,2.120012,7.476034,4.505740,2.369013,0.356507,-8.999903,-1.274570],[-4.524860,4.746756,5.802012,-7.573409,7.189920,-9.684606,-5.233795,-7.289938],[5.102510,5.476591,4.228750,5.123050,3.844847,3.520295,5.280871,2.775848],[3.092770,-6.432494,-6.551709,-2.195564,7.682618,5.623293,8.636166,-7.105820],[5.071523,3.372060,9.854241,8.518460,6.779952,-3.156982,-8.029845,-0.539098],[6.360199,5.978856,5.171227,9.076163,-7.635026,-9.162732,-4.214580,-2.893574]],[[-6.755317,-5.276319,0.926923,8.081919,-4.138093,4.350185,6.753602,-5.032184],[-0.769147,-4.737248,3.360752,2.983004,-4.749478,3.753060,-0.130592,8.468226],[8.341659,-5.016653,7.259483,-9.646244,-7.016351,3.035706,0.934779,-8.389108],[5.496321,-5.935340,-8.876134,-8.201766,4.187587,5.658446,-1.698698,3.950398],[-3.242320,-0.558962,9.108484,3.750257,-4.143017,6.541309,-2.308470,9.619263],[-9.640299,2.547088,6.327658,-7.895984,1.437930,8.140204,-1.443033,-4.699641],[-0.562549,-7.226630,6.909596,7.483828,-6.106504,2.075250,-2.773198,-0.251888],[-5.576146,4.398590,-2.523776,7.366250,6.397214,2.207594,9.957242,-8.352847],[-3.497376,3.996995,-5.243556,3.148181,4.625523,-8.734658,1.395950,-9.898988],[-3.263512,-6.045606,4.544779,-1.426137,-4.677493,-6.533147,2.437152,0.121417],[-3.760209,9.662528,-0.324150,2.303561,-6.002504,0.213225,8.840249,9.167252],[-7.000965,-9.875724,1.963381,-7.715462,-1.588278,2.247943,-5.704769,4.685160]]], dtype = "float32")#candidate|6543|(4, 12, 8)|const|float32
uop_6544 = relay.asinh(const_6543.astype('float32')) # shape=(4, 12, 8)
output = uop_6544
output2 = uop_6544
func_6546 = relay.Function([], output)
mod['func_6546'] = func_6546
mod = relay.transform.InferType()(mod)
mutated_mod['func_6546'] = func_6546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6546_call = mutated_mod.get_global_var('func_6546')
call_6547 = func_6546_call()
output = call_6547
func_6548 = relay.Function([], output)
mutated_mod['func_6548'] = func_6548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6481_call = mod.get_global_var('func_6481')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_6624 = relay.TupleGetItem(func_6481_call(), 0)
call_6625 = relay.TupleGetItem(func_6482_call(), 0)
output = call_6624
output2 = call_6625
func_6626 = relay.Function([], output)
mod['func_6626'] = func_6626
mod = relay.transform.InferType()(mod)
mutated_mod['func_6626'] = func_6626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6626_call = mutated_mod.get_global_var('func_6626')
call_6627 = func_6626_call()
output = call_6627
func_6628 = relay.Function([], output)
mutated_mod['func_6628'] = func_6628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mod.get_global_var('func_5343')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_6658 = relay.TupleGetItem(func_5343_call(), 0)
call_6659 = relay.TupleGetItem(func_5344_call(), 0)
output = call_6658
output2 = call_6659
func_6668 = relay.Function([], output)
mod['func_6668'] = func_6668
mod = relay.transform.InferType()(mod)
mutated_mod['func_6668'] = func_6668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6668_call = mutated_mod.get_global_var('func_6668')
call_6669 = func_6668_call()
output = call_6669
func_6670 = relay.Function([], output)
mutated_mod['func_6670'] = func_6670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5715_call = mod.get_global_var('func_5715')
func_5717_call = mutated_mod.get_global_var('func_5717')
call_6690 = func_5715_call()
call_6691 = func_5715_call()
var_6692 = relay.var("var_6692", dtype = "bool", shape = (11, 13, 10))#candidate|6692|(11, 13, 10)|var|bool
bop_6693 = relay.left_shift(call_6690.astype('uint8'), relay.reshape(var_6692.astype('uint8'), relay.shape_of(call_6690))) # shape=(11, 13, 10)
bop_6696 = relay.left_shift(call_6691.astype('uint8'), relay.reshape(var_6692.astype('uint8'), relay.shape_of(call_6691))) # shape=(11, 13, 10)
bop_6697 = relay.right_shift(var_6692.astype('int8'), relay.reshape(bop_6693.astype('int8'), relay.shape_of(var_6692))) # shape=(11, 13, 10)
bop_6700 = relay.right_shift(var_6692.astype('int8'), relay.reshape(bop_6696.astype('int8'), relay.shape_of(var_6692))) # shape=(11, 13, 10)
uop_6701 = relay.cos(call_6690.astype('float64')) # shape=(11, 13, 10)
uop_6703 = relay.cos(call_6691.astype('float64')) # shape=(11, 13, 10)
uop_6712 = relay.acosh(uop_6701.astype('float64')) # shape=(11, 13, 10)
uop_6714 = relay.acosh(uop_6703.astype('float64')) # shape=(11, 13, 10)
output = relay.Tuple([bop_6697,uop_6712,])
output2 = relay.Tuple([bop_6700,uop_6714,])
func_6718 = relay.Function([var_6692,], output)
mod['func_6718'] = func_6718
mod = relay.transform.InferType()(mod)
mutated_mod['func_6718'] = func_6718
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6719 = relay.var("var_6719", dtype = "bool", shape = (11, 13, 10))#candidate|6719|(11, 13, 10)|var|bool
func_6718_call = mutated_mod.get_global_var('func_6718')
call_6720 = func_6718_call(var_6719)
output = call_6720
func_6721 = relay.Function([var_6719], output)
mutated_mod['func_6721'] = func_6721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3561_call = mod.get_global_var('func_3561')
func_3562_call = mutated_mod.get_global_var('func_3562')
call_6753 = relay.TupleGetItem(func_3561_call(), 0)
call_6754 = relay.TupleGetItem(func_3562_call(), 0)
func_4583_call = mod.get_global_var('func_4583')
func_4584_call = mutated_mod.get_global_var('func_4584')
call_6758 = relay.TupleGetItem(func_4583_call(), 2)
call_6759 = relay.TupleGetItem(func_4584_call(), 2)
output = relay.Tuple([call_6753,call_6758,])
output2 = relay.Tuple([call_6754,call_6759,])
func_6766 = relay.Function([], output)
mod['func_6766'] = func_6766
mod = relay.transform.InferType()(mod)
output = func_6766()
func_6767 = relay.Function([], output)
mutated_mod['func_6767'] = func_6767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4318_call = mod.get_global_var('func_4318')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_6812 = relay.TupleGetItem(func_4318_call(), 0)
call_6813 = relay.TupleGetItem(func_4320_call(), 0)
var_6829 = relay.var("var_6829", dtype = "float32", shape = (11, 10, 3))#candidate|6829|(11, 10, 3)|var|float32
bop_6830 = relay.mod(call_6812.astype('float64'), relay.reshape(var_6829.astype('float64'), relay.shape_of(call_6812))) # shape=(11, 10, 3)
bop_6833 = relay.mod(call_6813.astype('float64'), relay.reshape(var_6829.astype('float64'), relay.shape_of(call_6813))) # shape=(11, 10, 3)
output = relay.Tuple([bop_6830,])
output2 = relay.Tuple([bop_6833,])
func_6840 = relay.Function([var_6829,], output)
mod['func_6840'] = func_6840
mod = relay.transform.InferType()(mod)
mutated_mod['func_6840'] = func_6840
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6841 = relay.var("var_6841", dtype = "float32", shape = (11, 10, 3))#candidate|6841|(11, 10, 3)|var|float32
func_6840_call = mutated_mod.get_global_var('func_6840')
call_6842 = func_6840_call(var_6841)
output = call_6842
func_6843 = relay.Function([var_6841], output)
mutated_mod['func_6843'] = func_6843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3845_call = mod.get_global_var('func_3845')
func_3847_call = mutated_mod.get_global_var('func_3847')
call_6897 = relay.TupleGetItem(func_3845_call(), 0)
call_6898 = relay.TupleGetItem(func_3847_call(), 0)
output = relay.Tuple([call_6897,])
output2 = relay.Tuple([call_6898,])
func_6899 = relay.Function([], output)
mod['func_6899'] = func_6899
mod = relay.transform.InferType()(mod)
mutated_mod['func_6899'] = func_6899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6899_call = mutated_mod.get_global_var('func_6899')
call_6900 = func_6899_call()
output = call_6900
func_6901 = relay.Function([], output)
mutated_mod['func_6901'] = func_6901
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6905 = relay.var("var_6905", dtype = "float64", shape = (10, 1, 10))#candidate|6905|(10, 1, 10)|var|float64
const_6906 = relay.const([[[1.735355,3.542052,-4.351916,-3.183266,-5.986922,-0.301653,4.940827,5.322345,-2.307780,7.736369],[5.970713,-0.857341,-3.837401,6.408476,-2.908609,-8.144401,-2.545605,-2.556909,8.836380,3.652251],[0.021863,-5.043405,8.894114,3.932986,-1.293130,-9.917777,-9.067438,2.126571,8.141175,-2.485581],[8.614104,3.391335,-3.984388,4.931210,-6.328624,8.470452,-1.351977,-5.122846,-7.675796,7.845211],[-4.002954,-9.532805,-4.952783,-7.164389,-2.058944,5.627873,5.787780,8.889586,7.315419,1.488334]],[[5.841090,9.009451,-8.075883,1.328733,-3.145761,5.147451,-3.236062,4.381076,-2.288706,-0.946152],[-0.560692,-9.202354,-5.335388,1.708948,-4.145637,3.820251,2.097816,-6.086810,-9.872627,-2.717056],[-1.993271,-7.463689,-0.472412,-3.240757,3.650537,6.118277,-9.368222,5.653958,-2.856841,-6.283803],[1.230138,-1.884473,8.483647,-2.998907,8.601632,-1.069044,1.668338,-1.927254,-8.745419,-2.867754],[-3.316912,2.823527,3.601424,1.725323,1.621280,0.193477,-7.128352,7.190681,-6.380879,1.392270]],[[4.195781,0.767457,-1.414680,-8.046235,-9.422886,-6.514580,-3.968663,-0.499058,-3.323834,4.317889],[8.069730,-8.290317,5.263416,7.626780,-5.680418,0.655197,-4.688088,-5.237487,-3.800680,7.038681],[2.996049,7.522331,7.244736,6.474206,-5.349054,5.260168,8.095762,4.705943,-1.176401,-4.230436],[1.314882,-6.328161,9.819400,3.712633,0.251843,-9.067893,-6.141660,-3.174418,6.301347,-5.239583],[0.796434,-6.261631,0.350377,9.474917,-9.268878,-2.022259,4.414655,-6.229993,4.867824,-2.989703]],[[-2.234103,3.607013,9.849870,9.955609,-2.262155,-5.004955,9.912092,-2.215835,-4.832635,-3.364530],[-6.361431,-8.967123,5.785066,-8.219222,-9.246804,3.946521,0.164000,-1.271123,7.260163,-9.610753],[3.087870,3.294342,6.025908,6.224890,1.582042,-9.301506,9.466260,4.951452,1.630736,7.927832],[-3.731115,9.560204,-1.725773,-9.347392,8.211904,7.632269,1.230775,4.194241,-5.949491,-6.303586],[3.296785,8.785461,-6.805794,1.221511,-9.600630,3.603146,-2.546586,6.449354,-4.127181,-6.122115]],[[-0.269119,-9.760290,-8.100899,-5.503961,3.914702,-5.616863,5.571693,1.196227,-8.172174,-1.100063],[7.699667,0.547048,-7.666169,-7.957500,3.036476,-6.647709,-7.869136,6.424723,-0.021995,-3.425031],[3.658994,-7.845982,-0.299023,-0.382430,5.933135,-1.836265,-9.105554,-5.431489,-2.150766,-3.215220],[0.977840,4.794495,4.868241,-6.437566,-9.757736,2.675966,3.085989,-8.723959,8.209958,-5.417630],[5.451939,-5.300291,-0.108469,-9.180202,2.609850,-9.678006,1.835371,7.147162,6.644974,7.204816]],[[-4.223185,0.641364,-4.377406,0.756663,-0.903141,-6.600638,-7.730812,6.904803,9.334894,9.904984],[-8.182781,4.716748,6.822992,2.351070,-7.488585,-2.981060,8.398993,-8.651728,-5.544506,-7.806113],[2.749596,-1.529212,4.231103,3.327044,-9.705461,0.896192,-5.529794,-5.971305,6.112364,-9.262291],[-2.098865,-3.659129,-1.351377,-4.608532,3.593710,5.718254,1.652659,-1.695278,-0.888779,-8.375416],[0.604747,9.701724,-8.035699,3.296193,4.133618,-4.755321,6.811396,-3.898647,0.998534,-3.489335]],[[0.980830,-9.650942,6.956343,1.464816,-5.574173,-6.001863,0.733914,3.552309,-9.349009,-9.662849],[7.482400,7.590786,8.279073,-6.582264,-2.882017,1.753237,7.782700,1.848250,8.790645,-9.319569],[-0.687147,1.971209,-8.916162,0.051008,3.651738,8.259250,-2.217689,2.561675,-8.307082,8.083377],[-0.120988,-4.951465,-2.612854,1.881869,-2.400228,7.111613,-5.830264,-3.536289,6.526749,5.547722],[9.190121,7.781804,-0.966125,-1.300701,1.587685,1.177357,-5.423710,4.699715,5.612928,-5.465710]],[[-3.816095,-1.032951,-8.960644,6.134166,0.768107,7.451526,1.612516,-5.432982,5.210457,-1.061288],[-2.634459,0.599311,3.051081,8.379550,5.197734,-9.502228,5.316723,-4.383196,-4.409147,-0.787497],[4.713731,-3.196790,-3.748838,-9.351528,7.652967,-8.897142,-9.371867,9.519828,-5.633886,0.958676],[-5.849251,3.449441,-9.336475,-3.603500,-7.886350,-9.610473,-0.161029,-5.099268,-6.300287,-6.024520],[-5.443860,5.041117,-3.592201,-7.026382,-5.471936,-4.671808,-9.866518,-4.022727,-5.058743,2.812540]],[[4.534343,-4.885188,-9.566393,9.848866,9.521826,9.337922,-5.329638,-1.642520,3.905685,-2.191393],[-1.843260,-3.088091,-6.267844,-8.348928,9.780688,2.337937,3.708162,-8.465149,9.891277,-3.596104],[-7.367152,-3.841759,1.994106,1.684269,9.541926,-4.104112,7.858827,-1.267498,8.898178,-2.033677],[-2.441852,-6.698427,8.995770,-4.197525,-4.967010,8.530400,-6.886119,4.310503,-4.329543,-5.574219],[-7.707484,-5.594340,6.516487,-8.611722,8.125631,-9.139258,-8.937239,1.085708,2.911588,-8.403029]],[[2.731976,-5.604665,5.791509,5.363976,9.582063,-5.630315,-7.123025,1.506048,9.342567,-0.413558],[-0.298336,3.654197,3.418845,-4.327184,-7.562498,-3.674903,-3.130831,6.476568,6.610462,2.971797],[-9.325487,-8.816887,-8.579904,-0.688306,9.363974,-1.589703,8.298361,5.131618,4.180165,-1.111177],[-4.535192,1.574666,5.081977,9.454476,1.689937,1.951406,-3.798757,-6.747568,8.164640,-5.699409],[3.016584,-8.230645,-2.057862,-3.884141,4.192131,0.957618,5.444131,-4.979238,8.994208,2.403365]]], dtype = "float64")#candidate|6906|(10, 5, 10)|const|float64
bop_6907 = relay.power(var_6905.astype('float64'), const_6906.astype('float64')) # shape=(10, 5, 10)
func_5127_call = mod.get_global_var('func_5127')
func_5130_call = mutated_mod.get_global_var('func_5130')
var_6911 = relay.var("var_6911", dtype = "float64", shape = (96,))#candidate|6911|(96,)|var|float64
call_6910 = relay.TupleGetItem(func_5127_call(relay.reshape(var_6911.astype('float64'), [4, 12, 2]), relay.reshape(var_6911.astype('float64'), [4, 12, 2]), ), 2)
call_6912 = relay.TupleGetItem(func_5130_call(relay.reshape(var_6911.astype('float64'), [4, 12, 2]), relay.reshape(var_6911.astype('float64'), [4, 12, 2]), ), 2)
output = relay.Tuple([bop_6907,call_6910,var_6911,])
output2 = relay.Tuple([bop_6907,call_6912,var_6911,])
func_6921 = relay.Function([var_6905,var_6911,], output)
mod['func_6921'] = func_6921
mod = relay.transform.InferType()(mod)
mutated_mod['func_6921'] = func_6921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6921_call = mutated_mod.get_global_var('func_6921')
var_6923 = relay.var("var_6923", dtype = "float64", shape = (10, 1, 10))#candidate|6923|(10, 1, 10)|var|float64
var_6924 = relay.var("var_6924", dtype = "float64", shape = (96,))#candidate|6924|(96,)|var|float64
call_6922 = func_6921_call(var_6923,var_6924,)
output = call_6922
func_6925 = relay.Function([var_6923,var_6924,], output)
mutated_mod['func_6925'] = func_6925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7032 = relay.var("var_7032", dtype = "float32", shape = (5, 4, 9))#candidate|7032|(5, 4, 9)|var|float32
uop_7033 = relay.sinh(var_7032.astype('float32')) # shape=(5, 4, 9)
func_3611_call = mod.get_global_var('func_3611')
func_3612_call = mutated_mod.get_global_var('func_3612')
call_7044 = relay.TupleGetItem(func_3611_call(), 0)
call_7045 = relay.TupleGetItem(func_3612_call(), 0)
bop_7051 = relay.subtract(uop_7033.astype('uint64'), relay.reshape(var_7032.astype('uint64'), relay.shape_of(uop_7033))) # shape=(5, 4, 9)
var_7066 = relay.var("var_7066", dtype = "float32", shape = (11, 10, 3))#candidate|7066|(11, 10, 3)|var|float32
bop_7067 = relay.minimum(call_7044.astype('float32'), relay.reshape(var_7066.astype('float32'), relay.shape_of(call_7044))) # shape=(11, 10, 3)
bop_7070 = relay.minimum(call_7045.astype('float32'), relay.reshape(var_7066.astype('float32'), relay.shape_of(call_7045))) # shape=(11, 10, 3)
output = relay.Tuple([bop_7051,bop_7067,])
output2 = relay.Tuple([bop_7051,bop_7070,])
func_7091 = relay.Function([var_7032,var_7066,], output)
mod['func_7091'] = func_7091
mod = relay.transform.InferType()(mod)
mutated_mod['func_7091'] = func_7091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7091_call = mutated_mod.get_global_var('func_7091')
var_7093 = relay.var("var_7093", dtype = "float32", shape = (5, 4, 9))#candidate|7093|(5, 4, 9)|var|float32
var_7094 = relay.var("var_7094", dtype = "float32", shape = (11, 10, 3))#candidate|7094|(11, 10, 3)|var|float32
call_7092 = func_7091_call(var_7093,var_7094,)
output = call_7092
func_7095 = relay.Function([var_7093,var_7094,], output)
mutated_mod['func_7095'] = func_7095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_7151 = relay.TupleGetItem(func_4536_call(), 0)
call_7152 = relay.TupleGetItem(func_4537_call(), 0)
func_4609_call = mod.get_global_var('func_4609')
func_4611_call = mutated_mod.get_global_var('func_4611')
var_7156 = relay.var("var_7156", dtype = "int64", shape = (40,))#candidate|7156|(40,)|var|int64
call_7155 = func_4609_call(relay.reshape(var_7156.astype('int64'), [5, 4, 2]))
call_7157 = func_4609_call(relay.reshape(var_7156.astype('int64'), [5, 4, 2]))
bop_7160 = relay.mod(call_7155.astype('float64'), relay.reshape(var_7156.astype('float64'), relay.shape_of(call_7155))) # shape=(5, 4, 2)
bop_7163 = relay.mod(call_7157.astype('float64'), relay.reshape(var_7156.astype('float64'), relay.shape_of(call_7157))) # shape=(5, 4, 2)
uop_7168 = relay.sqrt(call_7151.astype('float32')) # shape=(11, 10, 3)
uop_7170 = relay.sqrt(call_7152.astype('float32')) # shape=(11, 10, 3)
output = relay.Tuple([bop_7160,uop_7168,])
output2 = relay.Tuple([bop_7163,uop_7170,])
func_7172 = relay.Function([var_7156,], output)
mod['func_7172'] = func_7172
mod = relay.transform.InferType()(mod)
var_7173 = relay.var("var_7173", dtype = "int64", shape = (40,))#candidate|7173|(40,)|var|int64
output = func_7172(var_7173)
func_7174 = relay.Function([var_7173], output)
mutated_mod['func_7174'] = func_7174
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7182 = relay.var("var_7182", dtype = "float64", shape = (13, 15, 13))#candidate|7182|(13, 15, 13)|var|float64
uop_7183 = relay.acos(var_7182.astype('float64')) # shape=(13, 15, 13)
output = relay.Tuple([uop_7183,])
output2 = relay.Tuple([uop_7183,])
func_7189 = relay.Function([var_7182,], output)
mod['func_7189'] = func_7189
mod = relay.transform.InferType()(mod)
mutated_mod['func_7189'] = func_7189
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7190 = relay.var("var_7190", dtype = "float64", shape = (13, 15, 13))#candidate|7190|(13, 15, 13)|var|float64
func_7189_call = mutated_mod.get_global_var('func_7189')
call_7191 = func_7189_call(var_7190)
output = call_7191
func_7192 = relay.Function([var_7190], output)
mutated_mod['func_7192'] = func_7192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5937_call = mod.get_global_var('func_5937')
func_5938_call = mutated_mod.get_global_var('func_5938')
call_7196 = relay.TupleGetItem(func_5937_call(), 0)
call_7197 = relay.TupleGetItem(func_5938_call(), 0)
func_5240_call = mod.get_global_var('func_5240')
func_5242_call = mutated_mod.get_global_var('func_5242')
var_7201 = relay.var("var_7201", dtype = "float32", shape = (528,))#candidate|7201|(528,)|var|float32
call_7200 = relay.TupleGetItem(func_5240_call(relay.reshape(var_7201.astype('float32'), [528,])), 2)
call_7202 = relay.TupleGetItem(func_5242_call(relay.reshape(var_7201.astype('float32'), [528,])), 2)
func_3224_call = mod.get_global_var('func_3224')
func_3228_call = mutated_mod.get_global_var('func_3228')
const_7212 = relay.const([-3.111237,8.758206,-7.680552,-7.344954,-9.709548,3.824937,-0.374245,-3.770328,-7.854828,5.529918,-7.538849,-0.852722,4.353863,6.377660,3.191904,2.995004,-1.319706,-1.542253,7.201111,3.828966,4.413097,-7.137756,-3.060805,-1.206844,-6.332147,-8.285225,-0.822241,-4.911274,9.137984,-3.572604,-3.863471,-6.143716,-2.383180,-3.555329,3.959819,-9.428431,-5.273664,-0.448840,0.267958,8.863975,0.496706,-0.305813,-7.668105,1.984911,8.854620,9.456881,4.706008,-7.584608,-8.381181,5.574575,-4.692627,-4.983726,-3.468978,8.010700,5.630912,0.448072,-0.774874,-0.217066,7.444350,-2.819277,-0.614540,-4.807827,2.115546,0.313402,5.384556,-0.491905,-7.336690,-7.728548,1.853667,7.373729,3.319334,2.420177,-8.740296,-5.539214,9.203148,-1.786694,-4.682007,9.226771,9.759867,4.025028,7.625810,-7.012484,-7.496323,-6.806470,-0.294878,7.274215,6.907372,7.990846,-9.917016,7.421429,-1.488120,2.801730,-1.051764,2.100671,-2.703839,1.599814,-1.363365,9.167794,-2.510329,-7.775400,8.377703,-6.458277,0.090383,6.083544,-5.436590,9.723432,-4.923409,7.346300,-4.598138,9.980567,-4.762609,-9.605337,-9.636318,6.908957,-3.496933,-9.734953,8.827396,-8.184050,-4.651743,1.889557,-5.499659,-9.646683,7.001258,0.081006,-3.137059,-6.880220,8.563705,0.341344,1.019887,1.033593,-6.295638,5.048062,-3.120960,-9.963268,2.644285,2.013286,5.229181,6.262799,-5.762326,-8.010156,8.923802,6.131764,5.312946,-0.947326,7.097741,-9.345929,8.398695,-2.658130,7.916775,1.868917,-0.066826,-3.610912,-8.078938,-7.315317,7.845836,1.918765,-0.248220,6.742218,7.277523,-0.468741,5.936181,-0.169463,-0.293838,2.505440,-1.032181,2.236311,3.560194,-0.614848,2.337082,-9.801838,8.367835,2.710428,-3.823398,8.802753,-9.794398,2.847456,0.208539,2.265508,-5.558799,0.619364,3.544297,6.052723,2.529038,-1.118225,-2.069226,9.950514,-8.693424,0.669576,3.786485,-1.555898,-5.875449,-5.489949,1.146683,-0.366827,-8.728295,-7.156698,-6.818237,-8.100925,1.125810,-5.429898,-3.441228,9.073818,-1.527592,2.201148,-7.675562,5.861014,9.612501,-3.006231,6.880527,-8.693281,-0.121798,8.390321,-2.253698,-0.137227,-8.484634,-4.835769,-2.413960,2.710645,-0.955771,5.640727,-6.475054,-9.501928,-4.984611,7.494316,2.462343,9.312452,-9.856675,-8.121211,-3.041099,3.480227,9.110671,8.016054,6.099806,-5.947856,-8.245665,-0.164584,-3.776536,-1.754778,5.482303,8.395418,-5.909196,0.246027,7.755067,2.822140,-9.181822,6.431463,-1.800753,-9.146861,6.319987,-5.222111,-0.993533,0.491794,8.003650,9.525699,7.078786,6.673183,7.541469,-0.361078,-6.836041,-6.751259,-7.097112,-0.307295,1.347831,8.121178,4.839190,-1.072624,-0.894419,-4.498466,5.630478,5.393128,-9.560885,-0.029474,9.654189,9.413762,0.456624,-9.208145,1.785740,-9.161807,1.216663,3.777683,4.065559,-6.478936,2.166939,9.483919,-9.033288,9.797742,3.299322,-6.477171,3.870256,-4.437610,-6.534521,-0.269713,9.752077,-4.641951,-6.529159,1.795445,5.895783,-7.171208,9.415796,9.525969,-4.177478,-8.090002,4.368851,-7.172636,-7.166723,9.105221,2.362100,-0.503662,-6.780146,-8.883395,6.734124,2.304636,3.985683,6.082699,8.130389,3.543027,-5.039730,-8.262285,-2.839470,-6.751026,7.472884,1.161854,9.019949,-8.043744,-4.699328,2.635495,-1.638798,-2.572695,-9.860465,-4.110457,0.785077,4.314546,-1.840985,3.066322,-6.197872,3.934456,3.923826,-1.236047,5.024675,-5.294494,5.866064,5.521585,-0.167781,-9.651163,9.626968,7.268464,-1.788360,-8.301181,-0.844645,9.149742,0.508650,-0.768356,-9.954402,-5.823875,1.307856,4.344249,-8.963246,7.575069,6.293826,1.828231,-9.728961,4.086760,0.527627,1.976437,1.202103,-4.510211,-1.269508,1.408334,6.370655,-5.916759,-8.163564,-3.457666,-7.826518,-6.444778,1.083153,-8.831893,-4.731690,-5.151079,-5.521478,3.166366,-8.841397,-9.359164,-5.509750,4.094871,2.357208,7.030895,-6.888828,-7.845696,7.271671,-8.866287,-6.794503,-1.000875,-0.710921,-5.023742,2.870803,-8.029108,9.721152,-1.141354,-5.605755,-3.282029,7.490391,3.335990,2.005176,-2.379121,-8.439737,6.344628,4.211076,6.481478,-2.710560,-2.021244,9.150069,2.247017,-4.837666,3.073633,-5.675301,-8.988309,1.590874,3.425949,-5.514223,0.596621,-1.423083,1.942516,-7.588907,0.722395,8.406988,-1.301126,-4.328162,7.645324,3.456324,6.758017,-5.953945,6.540138,4.495681,-8.587036,-8.741562,7.314203,-6.712767,5.904123,3.638645,8.339187,-2.351440,-0.677488,-7.177885,9.500763,-5.767981,1.204356,5.246735,-7.454540,3.410831,-5.827223,-5.888436,-2.279722,-0.657570,7.188088,-4.995555,-8.716957,5.949762,1.728110,4.527913,4.038485,6.000659,-5.264519,-0.307426,5.819242,-4.773528,8.459356,2.728673,5.075912,7.844552,-1.098868,-3.692009,7.811314,9.988076,3.337436,3.299331,-2.704800,7.865510,5.813976,5.681089,2.644457,-4.396940,-3.598443,-2.502383,-4.632166,-6.609883,1.263129,9.536286,-0.006930,9.300868,0.685200,6.107896,8.134266,0.237854,-9.099065,9.923862,-7.759510,-5.490759,-4.536813,-1.324721,5.266599,0.433577,5.096445,9.359318,5.757449,5.356704,9.463801,-8.417040,1.283138,-7.278253,-5.376923,4.018449,9.768216,5.675293,-5.024734,-9.087734,-3.232871,-6.464490,1.286783,-5.115696,-2.608010,1.784829,-5.513278,-7.526315,1.382620,3.335737,4.366888,-6.011678,-8.204022,-4.765439,-2.109478,-5.957818,-4.297925,-5.278418,-6.336845,-4.659932,0.457714,9.033342,5.344822,0.632102,-9.194448,-0.292215,-7.557537,-7.451066,-0.868436,4.350796,-3.039743,8.489331,7.401687,-2.446598,-7.660171,-7.103804,-3.798677,8.277789,-7.507887,5.558381,3.193762,-9.032921,-7.014088,9.472634,5.316400,1.824492,-6.435294,-5.632004,3.620574,-3.758267,1.801487,3.331099,-7.611003,9.675620,9.041042,1.953804,-1.122524,-4.435231,-9.436862,2.987859,9.742681,2.169418,2.259267,1.395320,-2.193098,7.718398,-4.866072,-5.134347,5.780600,6.664879,-0.117801,-6.843857,-3.114591,1.457640,-8.447822,-8.592688,-3.016275,2.633145,2.208279,-7.773720,-9.821914,6.559662,-7.034166,8.855920,4.918295,-3.366327,9.259992,-9.356879,-5.693506,6.797246,-4.574177,-3.927865,2.717613,2.296723,-1.070140,9.096829,6.029124,6.237518,-4.169789,8.396230,-0.619184,8.474987,-9.802400,3.822625,7.067504,1.765885,0.726769,-1.496271,-3.167481,4.438599,7.355918,1.460303,-6.965838,-5.578623,-1.233336,-4.110556,-6.161007,-4.670618,-5.522714,5.459160,-3.549678,1.536776,-6.285167,8.539267,1.997287,4.594748,4.852852,9.840468,5.825121,-2.431472,-5.247766,-2.064453,-1.397452,2.489889,2.036643,-5.171806,-7.570904,0.892224,-0.189634,8.152641,0.372537,-2.490515,0.455744,-5.131958,-4.384156,-2.801440,-0.302766,8.068022,-2.471386,7.079295,8.756514,0.665610,1.849460,-8.595315,3.754178,-2.509210,-1.879935,4.195715,-1.755047,-2.840378,-7.714907,6.774416,-9.417323,9.038741,-7.647060,-2.872725,9.624953,3.159211,-0.400573,-4.925275,7.078804,-2.369084,8.143262,7.421998,-0.514776,-1.935503,4.673221,7.542199,-1.168562,-6.204055,7.982567,-2.954812,-5.410396,4.058242,7.881812,5.780397,-1.695903,-3.902988,0.239111,-2.923785,-2.899644,8.900695,-1.414465,8.293178,8.169813,4.700154,-3.348712,6.722475,5.636647,9.011506,-7.859211,3.695184,-1.022885,0.334930,-6.235580,6.738357,-9.775732,-1.556155,5.034254,-6.722670,5.607405,7.003289,0.523030,-7.156780,-2.074823,-8.710292,-8.193808,9.765445,2.020311,2.115548,-8.802427,-3.417668,3.499967,-2.088043,-1.873618,3.674709,-2.103611,2.261224,-1.613349,9.259773,9.548365,0.612328,1.601840,3.518341,7.808122,-5.719243,6.658621,9.010038,3.427797,-8.261574,-1.304010,3.159509,-3.746120,-8.764103,2.677561,6.930859,0.206303,-7.954663,-6.271286,-5.865313,-0.667198,2.408483,5.640453,-7.699505,-5.631441,3.756659,7.417711,-0.181662,6.241263,-5.882659,-8.883267,-9.764110,-2.704731,-5.170180,-5.369008,4.495693,-6.328553,-1.723499,2.908854,-1.451024,1.465546,-1.210494,2.948160,7.437078,8.207503,0.745851,0.466412,-4.821292,-3.195091,-1.904131,8.527482,-4.374754,5.569832,9.277648,8.975568,-4.807855,1.999970,9.127181,2.972779,-4.834599,-9.579360,-5.985527,4.355226,-4.837496,-7.204543,-7.738026,-4.793245,0.699511,2.401263,-3.628102,-7.107537,-9.641242,4.760960,-6.026127,-9.386499,2.215689,-0.184588,-9.274889,-3.275038,-9.874626,-2.861802,-5.160833,5.364613,-8.465383,6.818906,8.615559,3.126616,9.110396,-1.063968,-6.426373,-1.353915,6.721063,7.830566,-3.459213,-4.325334,-7.331797,7.137823,3.438353,-9.057164,-2.626014,-2.285786,-9.624204,3.646728,-4.747996,0.793986,-6.017678,0.689648,4.845369,4.191047,-4.797627,-0.443283,-3.150664,-8.172007,-2.050481,3.252369,-9.986984,-3.416007,-3.779258,-3.927952,4.503677,6.363585,-6.806451,-5.404439,2.521269,8.095946,3.297375,1.210389,-0.508047,-8.763702,-9.709583,7.317689,5.212820,2.555414,1.249893,6.514858,-8.782137,-0.362877,9.358924,-2.296134,-6.249671,-5.028084,5.404941,-1.666020,6.382260,-6.083732,-7.734792,-2.821398,9.140567,9.644863,-6.114472,-1.162918,0.921586,6.144507,5.470976,-8.809692,4.851843,4.052185,-7.414782,-0.719992,-5.754723,9.174881,-7.032229,5.309832,-8.327214,-8.216573,9.998333,0.753836,9.176537,9.089672,-7.209937,8.572162,-7.995176,-4.702770,-4.031538,8.894778,4.876129,3.611013,-6.836438,2.019201], dtype = "float64")#candidate|7212|(924,)|const|float64
call_7211 = relay.TupleGetItem(func_3224_call(relay.reshape(const_7212.astype('float64'), [924,]), relay.reshape(call_7196.astype('float32'), [11, 10, 3]), ), 3)
call_7213 = relay.TupleGetItem(func_3228_call(relay.reshape(const_7212.astype('float64'), [924,]), relay.reshape(call_7196.astype('float32'), [11, 10, 3]), ), 3)
output = relay.Tuple([call_7196,call_7200,var_7201,call_7211,const_7212,])
output2 = relay.Tuple([call_7197,call_7202,var_7201,call_7213,const_7212,])
func_7217 = relay.Function([var_7201,], output)
mod['func_7217'] = func_7217
mod = relay.transform.InferType()(mod)
var_7218 = relay.var("var_7218", dtype = "float32", shape = (528,))#candidate|7218|(528,)|var|float32
output = func_7217(var_7218)
func_7219 = relay.Function([var_7218], output)
mutated_mod['func_7219'] = func_7219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2161_call = mod.get_global_var('func_2161')
func_2162_call = mutated_mod.get_global_var('func_2162')
call_7274 = func_2161_call()
call_7275 = func_2161_call()
output = call_7274
output2 = call_7275
func_7287 = relay.Function([], output)
mod['func_7287'] = func_7287
mod = relay.transform.InferType()(mod)
mutated_mod['func_7287'] = func_7287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7287_call = mutated_mod.get_global_var('func_7287')
call_7288 = func_7287_call()
output = call_7288
func_7289 = relay.Function([], output)
mutated_mod['func_7289'] = func_7289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5563_call = mod.get_global_var('func_5563')
func_5565_call = mutated_mod.get_global_var('func_5565')
call_7295 = relay.TupleGetItem(func_5563_call(), 0)
call_7296 = relay.TupleGetItem(func_5565_call(), 0)
output = relay.Tuple([call_7295,])
output2 = relay.Tuple([call_7296,])
func_7312 = relay.Function([], output)
mod['func_7312'] = func_7312
mod = relay.transform.InferType()(mod)
output = func_7312()
func_7313 = relay.Function([], output)
mutated_mod['func_7313'] = func_7313
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7337 = relay.const([[[-5.804552,-5.183058,-4.153738,3.440341,5.089876,-3.668230,6.148927,-1.792498,-7.742591,0.762092,2.102474,-7.159253,0.405874,0.925480,0.032891,-9.686778],[-4.147632,5.599935,-6.552136,1.853734,-0.606581,-6.858936,1.599982,-5.650347,1.580206,4.142680,9.850214,-3.799149,-3.800146,5.839889,-5.749468,1.895337],[-8.747843,-2.832634,-1.627466,-4.334969,7.645076,-8.444346,0.577264,-3.191788,-1.731816,1.305812,3.692135,-3.777768,3.497982,2.308492,2.768546,-4.212048],[-3.267234,-9.170671,-5.454891,8.373884,9.571254,-8.176885,-0.138232,-5.556785,-7.901709,5.084817,8.766006,7.644700,1.136094,8.089870,-5.494647,-4.452242],[-0.917365,2.751348,5.674629,-8.230064,-0.022955,1.585779,-2.107811,-0.648598,3.633687,-4.625693,6.081391,3.373321,5.325288,-8.916502,-0.447379,-6.118992],[0.775428,9.651368,-0.847151,-9.762817,-6.825745,-8.756717,8.353705,4.813133,-8.376670,5.164601,-0.623393,-8.695980,2.617915,0.890250,9.068039,-6.383646],[2.606488,6.578467,-0.072025,-3.146875,6.274192,9.462111,0.496142,8.029789,-4.965360,-1.493415,3.963145,-7.617521,5.964521,-2.924958,9.645951,6.135851],[-7.054506,7.779086,-8.662703,7.120271,-3.930769,-4.173944,1.202233,6.220503,6.336573,-3.031022,-5.923621,5.530909,-0.891257,-2.611969,9.832013,-0.475424],[-1.694955,-8.980123,-1.861171,-1.439609,-0.199862,-9.600807,-6.388138,8.920796,1.253588,-7.759810,6.835490,6.571038,0.965225,3.937276,-1.804606,-4.659998]],[[3.126847,1.311141,-8.011951,-1.991787,4.473462,-0.349845,-6.522187,7.951401,-9.321022,9.076085,7.274897,5.510752,-9.994947,2.411247,2.841739,6.660964],[-6.791744,-9.089331,-2.802926,5.004994,5.605453,2.519381,-4.932951,-2.366477,-9.524437,-3.498182,-6.331037,-6.535371,-7.769063,2.220908,8.838292,7.926290],[-9.062649,-9.283933,-7.328352,-3.823324,-6.837483,-2.188846,-8.909299,4.699376,-1.015340,-0.568248,0.900933,-0.405740,5.141117,3.886026,-7.681970,-6.329360],[-6.871850,-2.173599,4.505714,4.366710,-4.068853,-9.374709,-2.308117,-2.212925,0.632118,1.522741,5.687059,-5.268545,-7.304923,-3.264912,-2.422009,2.950113],[9.252905,-9.644241,-4.358617,-6.765464,9.222309,3.466549,-0.732892,-7.369126,-3.817015,3.842611,0.043468,-4.218049,8.415808,2.964464,-7.116798,4.512087],[-3.784568,-0.289711,1.872398,9.854273,5.637753,-0.282149,-3.699167,3.374502,-8.464774,8.613527,-1.797700,9.994781,-8.878913,-2.873935,6.401939,-8.400916],[8.488184,-0.571484,-7.579652,6.008944,-0.734086,8.349822,-6.551639,-2.488336,8.253802,0.735556,7.870378,-2.762953,7.419335,-5.717055,-9.182399,-6.369310],[6.098592,-8.034807,-0.172734,6.539182,6.715548,-2.522665,0.103065,-8.811627,-9.241152,2.744432,4.609261,3.925893,-5.224121,8.007598,-6.115186,-9.587374],[0.674369,5.580917,-0.248835,-8.274770,-2.188847,4.099690,1.888788,-5.578314,6.354251,-2.364961,4.741449,1.644644,1.509619,-7.023593,-5.679996,-9.201605]],[[3.038089,-0.432446,-8.602176,5.394869,1.609011,1.201372,3.155496,-7.324680,2.583673,9.942378,-5.417428,-4.745465,1.048018,9.098732,0.547607,9.199469],[-4.076015,-8.136371,1.123389,2.038179,-6.675810,8.463704,-4.597146,1.823374,-7.740199,6.486150,3.225584,0.847259,-7.642012,7.120747,-9.169036,0.924805],[-9.010210,4.335428,2.087885,-1.793835,7.116789,7.802939,5.531543,9.011985,2.338302,-2.987597,-7.504944,-2.789495,-8.035821,-0.267418,-8.869281,6.814956],[5.788413,-0.485853,8.702269,2.210337,5.837097,5.147408,2.510094,-9.817207,6.184377,1.383098,-9.207603,-4.928296,1.216380,8.631033,-0.475569,-2.452860],[-9.333581,3.574944,4.249461,-4.354195,9.264062,8.048654,4.177120,-4.450269,-0.006692,-7.772019,2.537083,-9.273217,-3.500871,-4.175273,-3.220273,-9.775799],[-8.933579,3.275055,-9.829945,-9.878602,3.779442,-4.413624,5.597065,6.065158,1.656969,3.778492,-4.510385,4.317201,8.233602,-9.674216,0.081887,-5.669970],[-3.130865,6.519108,-7.888066,-6.452131,-1.282211,-0.321082,3.593094,9.890106,9.328010,9.395818,-5.919338,-7.724496,9.402975,-4.036972,-5.740938,-1.190717],[-2.628242,7.073679,9.220291,-4.852380,9.810143,8.596228,-7.539478,1.623877,8.277076,2.904943,6.064396,-7.983585,-3.920661,4.750197,8.365476,5.923083],[-6.552416,-0.113179,3.997548,7.647049,4.445776,4.440016,8.252273,-7.632480,-9.336770,6.255784,9.487262,-9.446881,-6.870823,-5.605249,7.824914,6.492524]],[[9.434071,5.694301,-9.661434,4.572612,9.151902,1.312665,5.987209,-7.215678,0.741651,5.436572,5.757193,2.159631,-7.208608,5.194994,6.165248,2.348908],[6.966751,5.197143,7.568717,3.708817,-3.922680,0.012866,-7.103751,1.417590,0.443773,4.313561,-7.187651,-9.366100,-0.918730,-2.390070,-4.547135,-5.651668],[-8.376881,7.555489,-2.629730,-9.983045,1.981329,-7.702003,0.264756,-9.803374,0.677103,8.555407,-1.099003,-8.557458,-3.858679,-8.547808,-3.949672,-0.582831],[5.009836,-0.341199,-8.375836,-4.719235,-5.617088,-8.434916,-1.351822,7.458936,-7.496616,4.803794,-0.225678,6.623517,-0.627744,-7.751568,4.476428,5.265123],[-7.045228,-2.948889,-1.121799,7.900611,-4.958847,7.420874,-6.822311,-0.829268,9.163514,2.252679,0.149120,-8.213534,-3.558941,-1.100709,0.018875,-6.740813],[3.324902,3.266744,5.481731,-5.348088,-6.598205,-0.331234,-3.288018,1.574961,-6.860858,-5.691089,3.875415,3.852665,5.191786,4.827879,5.103171,-6.049728],[5.326366,3.038484,-7.260803,-0.499398,1.373656,9.595875,6.581217,5.189076,7.022624,7.142981,7.380744,4.183600,-9.250833,7.046765,-8.914190,-2.319739],[4.874157,5.043448,7.809123,-7.531213,-3.394508,1.541255,-9.159396,-4.066542,-3.463194,9.901390,-0.490010,-4.833533,2.833177,2.801753,3.930658,5.877782],[8.412411,3.534073,-8.230036,9.301983,7.708499,-5.213438,0.865351,-9.201590,-7.265315,1.863173,-1.550966,2.415316,-2.082066,5.798138,-9.615512,-2.375030]],[[8.836599,8.356148,-3.808373,9.701106,9.431070,7.934433,-1.845712,-0.285557,7.124672,3.423044,5.376978,-2.598885,0.422425,7.435750,-6.860368,4.370389],[9.049746,-3.429554,6.556980,-6.869770,4.980377,-6.697012,7.286701,5.596230,-5.836934,-4.614592,8.148860,7.004988,-3.224435,8.597464,3.049890,1.296422],[2.162068,-8.811500,4.509364,6.948024,-4.445400,-3.948348,-0.899686,9.111400,-8.776376,-6.748352,-9.973038,1.638268,-8.306905,0.087037,7.389816,3.402824],[-0.966128,-3.410170,-5.736972,5.066212,1.669389,-2.112834,3.666826,-2.984155,1.310804,1.645086,4.039439,-0.881799,4.951988,2.129194,-6.200032,1.069064],[-6.017685,-8.696987,5.397951,6.838350,9.605371,-8.169153,3.387576,6.398833,4.631397,-4.099171,4.791328,7.537320,3.171980,7.115616,3.818045,-3.395135],[-4.110238,-0.616162,-2.012018,-6.707111,8.897086,-0.880127,-1.866354,4.266018,8.841172,-7.471813,-1.251007,8.605180,-2.447410,-4.820460,-6.962980,9.967685],[0.014811,-3.955266,2.847220,-7.198893,-9.275054,-6.514455,-5.679376,-9.389250,3.339443,-3.993859,-0.955681,0.868481,-1.069589,-0.916679,0.077770,-7.891528],[0.671422,-6.667179,0.437118,1.685680,-3.533966,-3.860495,2.761536,-0.898741,3.214667,4.189512,-4.079097,-7.699746,-9.223742,5.696857,-6.360719,-5.104528],[2.844989,3.614896,5.262414,-5.258891,-8.531424,-6.493317,8.661308,-1.422944,7.873129,7.795762,4.333293,4.772601,-9.076342,7.682279,-2.217136,2.892853]],[[-2.095072,-9.393406,1.325741,1.621792,-1.465460,-8.362663,-2.489768,-0.119993,-7.010373,-3.299718,-2.188501,9.256661,-5.759984,0.758414,-0.269021,-0.081723],[0.632557,0.181971,2.789562,-9.843615,-3.807957,-8.335561,-2.749958,8.324276,-3.755235,-8.465045,7.094949,1.383062,-3.612031,-6.499015,2.067869,8.592333],[0.437617,-4.376880,-1.276761,-8.206751,8.148856,3.068595,-8.473966,-0.408048,-0.242455,0.255031,-4.271373,-2.050397,6.524296,5.683207,9.189421,-0.168260],[6.895032,-9.913521,7.011364,8.398632,5.111513,-8.979380,3.001125,-1.834026,7.280463,3.111424,-9.989515,-4.125953,-6.418760,7.204944,2.205399,-6.247396],[-6.277101,-8.887982,-4.686529,-1.917101,-5.092266,7.867306,8.861604,-6.433616,5.945087,-1.036406,9.510291,8.802620,-6.876027,2.481331,-7.859055,0.372003],[-4.087116,6.281336,8.293274,-5.528848,-7.387993,5.672225,5.924943,7.834699,3.251013,5.146302,-8.793379,-4.960147,0.306086,-9.922781,8.927274,-5.079708],[2.100228,-5.156858,8.946416,2.961769,-0.611268,2.434507,-0.114107,-0.654612,-5.259778,-6.877908,5.507608,3.394080,-8.252988,-9.496464,6.288242,-6.929793],[-3.677339,8.725386,5.737844,-0.026220,7.513739,-0.390072,-9.422218,3.842712,-6.859852,1.772933,-8.370182,-0.653842,4.704259,5.127023,6.768016,5.485567],[-0.409327,0.471613,5.019045,-9.534576,6.349713,-3.386126,5.195330,-7.437131,4.700980,4.173552,-9.342176,6.095800,2.660609,0.266959,-4.168298,-5.144653]],[[1.270509,-3.735604,5.805454,-2.388885,1.604484,-9.686861,-3.938592,-5.163853,7.311350,-4.860973,0.252646,4.188701,-5.843869,7.450838,6.246664,5.533778],[5.020143,-0.170792,-4.560995,8.100523,0.167637,0.106688,-0.494495,-6.594939,4.375214,-2.746205,-9.879919,0.987808,-0.074753,1.878689,4.687961,-5.097896],[-8.087849,5.022570,1.053274,6.495848,1.325648,9.614832,-6.258253,2.211248,-3.748915,2.860228,8.304783,7.553925,8.866034,2.983105,8.044720,-3.074350],[-9.610589,3.338935,-1.130781,1.451672,0.503068,-2.971539,-7.078065,2.926703,7.871679,5.754388,-7.520843,-4.927850,2.291355,-1.910341,8.653078,-1.167246],[-6.922353,-4.918581,-5.301060,-5.299005,-8.639330,-2.301707,-4.364644,1.668308,-5.626261,-9.181836,5.999281,-0.098124,5.687228,6.656872,5.296922,-9.612406],[3.136388,1.771068,-5.404401,9.283417,-4.827520,3.005384,-8.832587,-7.906783,4.548868,8.066104,5.723890,3.562920,-2.967302,3.319886,7.835708,3.162130],[-1.296477,-1.402277,2.984325,7.302446,1.941281,-0.901725,0.643534,-0.002831,-5.318877,9.313913,-3.548771,-1.917763,-5.926566,-9.529774,2.479014,-4.174863],[-1.634458,1.013565,0.435137,9.331864,0.166917,-1.624742,-9.476695,-1.511435,-4.311044,-8.505708,-4.237178,1.037370,4.984316,-2.910214,9.936098,-3.407718],[-1.720747,7.407934,7.633303,-0.794994,2.198058,0.949661,-6.100591,-7.346799,-7.649593,6.973053,3.701841,8.412102,-7.355944,8.661727,-2.472307,-4.259817]],[[4.275499,-8.887000,-5.264577,-4.241705,1.865256,-1.567149,1.635749,-0.625838,6.880278,-1.807179,-2.239734,1.577133,-1.365104,1.608183,9.416184,8.277757],[0.761959,3.565576,-9.536307,3.155282,2.020578,3.571207,-1.447185,-1.041470,0.610579,-8.197724,-9.190183,3.877804,8.583473,-5.815525,-4.290440,6.287180],[7.945931,8.915747,-5.290622,-6.247952,-9.176203,-7.584330,4.612605,8.993811,-2.386177,4.858631,1.365168,8.279003,4.301010,3.817764,4.817980,6.260320],[5.155514,-5.260975,-3.128477,-1.153180,1.636365,5.956717,2.931858,0.649789,1.105224,6.742232,1.968609,0.056541,-2.587959,-3.912965,7.254157,-7.178647],[3.861376,6.649591,5.149055,-3.994353,-1.741380,-5.785311,-5.743135,7.366372,-6.917291,6.349994,3.161244,-1.206043,8.333419,6.185543,-1.669168,-7.707011],[8.913809,3.282003,0.543237,3.023906,-7.072652,8.690464,3.532234,-4.875476,1.674397,-3.798385,-8.972685,-4.126495,8.955360,-0.639137,-6.882536,3.905367],[-1.719872,-0.391306,2.525155,-7.349473,0.582423,-9.720918,-9.768469,-2.485773,-4.388457,1.074102,0.183448,8.815887,9.445513,3.180556,-3.656467,7.976774],[7.193016,-1.776396,3.473479,-5.049582,-7.734580,-4.417485,7.189432,0.628351,7.436812,-5.224210,-9.063975,4.143618,-5.674599,5.379755,-9.772421,3.308763],[2.823195,-9.638456,-4.416188,8.182946,5.008614,-0.154780,0.482049,4.573817,-0.507350,9.037327,1.069322,-9.584396,8.674132,-6.914844,2.089069,-3.881232]]], dtype = "float64")#candidate|7337|(8, 9, 16)|const|float64
uop_7338 = relay.asin(const_7337.astype('float64')) # shape=(8, 9, 16)
uop_7343 = relay.rsqrt(uop_7338.astype('float32')) # shape=(8, 9, 16)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_7348 = func_2059_call()
call_7349 = func_2059_call()
bop_7350 = relay.logical_xor(uop_7338.astype('uint16'), relay.reshape(uop_7343.astype('uint16'), relay.shape_of(uop_7338))) # shape=(8, 9, 16)
bop_7356 = relay.minimum(bop_7350.astype('int8'), relay.reshape(uop_7338.astype('int8'), relay.shape_of(bop_7350))) # shape=(8, 9, 16)
func_5796_call = mod.get_global_var('func_5796')
func_5798_call = mutated_mod.get_global_var('func_5798')
var_7366 = relay.var("var_7366", dtype = "float64", shape = (1, 750))#candidate|7366|(1, 750)|var|float64
call_7365 = relay.TupleGetItem(func_5796_call(relay.reshape(var_7366.astype('float64'), [750,])), 0)
call_7367 = relay.TupleGetItem(func_5798_call(relay.reshape(var_7366.astype('float64'), [750,])), 0)
uop_7371 = relay.exp(bop_7350.astype('float64')) # shape=(8, 9, 16)
output = relay.Tuple([call_7348,bop_7356,call_7365,var_7366,uop_7371,])
output2 = relay.Tuple([call_7349,bop_7356,call_7367,var_7366,uop_7371,])
func_7382 = relay.Function([var_7366,], output)
mod['func_7382'] = func_7382
mod = relay.transform.InferType()(mod)
mutated_mod['func_7382'] = func_7382
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7383 = relay.var("var_7383", dtype = "float64", shape = (1, 750))#candidate|7383|(1, 750)|var|float64
func_7382_call = mutated_mod.get_global_var('func_7382')
call_7384 = func_7382_call(var_7383)
output = call_7384
func_7385 = relay.Function([var_7383], output)
mutated_mod['func_7385'] = func_7385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2027_call = mod.get_global_var('func_2027')
func_2028_call = mutated_mod.get_global_var('func_2028')
call_7400 = func_2027_call()
call_7401 = func_2027_call()
output = relay.Tuple([call_7400,])
output2 = relay.Tuple([call_7401,])
func_7410 = relay.Function([], output)
mod['func_7410'] = func_7410
mod = relay.transform.InferType()(mod)
output = func_7410()
func_7411 = relay.Function([], output)
mutated_mod['func_7411'] = func_7411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5715_call = mod.get_global_var('func_5715')
func_5717_call = mutated_mod.get_global_var('func_5717')
call_7497 = func_5715_call()
call_7498 = func_5715_call()
uop_7501 = relay.asin(call_7497.astype('float64')) # shape=(11, 13, 10)
uop_7503 = relay.asin(call_7498.astype('float64')) # shape=(11, 13, 10)
output = relay.Tuple([uop_7501,])
output2 = relay.Tuple([uop_7503,])
func_7504 = relay.Function([], output)
mod['func_7504'] = func_7504
mod = relay.transform.InferType()(mod)
mutated_mod['func_7504'] = func_7504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7504_call = mutated_mod.get_global_var('func_7504')
call_7505 = func_7504_call()
output = call_7505
func_7506 = relay.Function([], output)
mutated_mod['func_7506'] = func_7506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4318_call = mod.get_global_var('func_4318')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_7515 = relay.TupleGetItem(func_4318_call(), 0)
call_7516 = relay.TupleGetItem(func_4320_call(), 0)
output = call_7515
output2 = call_7516
func_7528 = relay.Function([], output)
mod['func_7528'] = func_7528
mod = relay.transform.InferType()(mod)
output = func_7528()
func_7529 = relay.Function([], output)
mutated_mod['func_7529'] = func_7529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5519_call = mod.get_global_var('func_5519')
func_5520_call = mutated_mod.get_global_var('func_5520')
call_7537 = relay.TupleGetItem(func_5519_call(), 1)
call_7538 = relay.TupleGetItem(func_5520_call(), 1)
func_2853_call = mod.get_global_var('func_2853')
func_2854_call = mutated_mod.get_global_var('func_2854')
call_7557 = func_2853_call()
call_7558 = func_2853_call()
func_228_call = mod.get_global_var('func_228')
func_231_call = mutated_mod.get_global_var('func_231')
const_7576 = relay.const(1.629362, dtype = "float64")#candidate|7576|()|const|float64
var_7577 = relay.var("var_7577", dtype = "float64", shape = (315,))#candidate|7577|(315,)|var|float64
call_7575 = func_228_call(relay.reshape(const_7576.astype('float64'), []), relay.reshape(var_7577.astype('float64'), [7, 3, 15]), )
call_7578 = func_228_call(relay.reshape(const_7576.astype('float64'), []), relay.reshape(var_7577.astype('float64'), [7, 3, 15]), )
func_7091_call = mod.get_global_var('func_7091')
func_7095_call = mutated_mod.get_global_var('func_7095')
const_7587 = relay.const([5.932798,-5.016809,-4.561442,6.676186,-1.951291,-4.008497,4.003705,-3.108675,8.377028,3.091013,8.990237,7.152159,7.920813,-9.563463,7.187883,-5.246618,-5.905430,-9.938697,2.383484,0.910182,-9.415003,-5.242732,-1.985317,-8.621814,5.635936,-6.710632,7.385365,7.079597,7.318495,0.674750,0.450169,3.975760,5.048233,4.032415,0.656060,-3.975884,-1.666863,-8.353305,-8.826410,-0.883356,-2.755691,-1.672676,7.333377,-4.575592,0.137009,5.504824,6.646612,-0.260161,8.553614,9.348717,-9.021331,-9.425925,0.161939,-0.375371,8.182228,5.365358,1.788025,5.093792,6.939731,4.063322,4.724798,-2.537843,-1.899152,3.986516,-9.578086,-7.171846,1.352914,7.756264,5.530365,-0.470528,9.524797,-9.345856,0.522319,7.222884,1.344647,6.649627,6.767701,1.326217,0.217732,2.727761,-3.843501,-7.534021,-9.691902,-3.648983,6.039097,-0.308526,-0.444641,-2.986412,-9.373948,1.535334,-2.364762,9.842888,-5.142667,9.089862,5.711955,1.380685,9.726565,1.510286,5.165935,2.972680,-1.356829,4.476420,7.769176,-0.880539,7.482532,1.833807,0.877734,-7.199147,-9.399843,3.505677,-9.571505,4.372655,-2.574376,-0.038689,-6.544057,5.161441,2.563891,3.116393,-8.485646,2.947882,2.975249,7.329531,6.540314,-5.164774,-9.587121,9.789413,-0.839322,-5.826602,-4.158147,9.006501,-8.964000,1.577715,2.428228,-5.666168,9.974593,-4.495010,8.651058,9.668876,6.100485,-2.088513,9.577411,-2.312639,-1.772047,-8.308952,7.934364,4.897759,-1.911341,-3.259516,7.921194,8.273015,-8.406237,-3.673902,-8.117081,-4.554239,8.498848,2.307723,-8.521234,7.603093,-0.549891,0.747521,0.339973,1.178650,-9.762651,7.352127,2.810589,-2.266772,-2.021637,4.675521,-0.491449,-8.751810,-0.141496,-3.957730,-5.540975,6.577886,1.134800,-1.206115,9.037944,4.442128,1.161759,9.533992], dtype = "float32")#candidate|7587|(180,)|const|float32
call_7586 = relay.TupleGetItem(func_7091_call(relay.reshape(const_7587.astype('float32'), [5, 4, 9]), relay.reshape(call_7557.astype('float32'), [11, 10, 3]), ), 0)
call_7588 = relay.TupleGetItem(func_7095_call(relay.reshape(const_7587.astype('float32'), [5, 4, 9]), relay.reshape(call_7557.astype('float32'), [11, 10, 3]), ), 0)
output = relay.Tuple([call_7537,call_7557,call_7575,const_7576,var_7577,call_7586,const_7587,])
output2 = relay.Tuple([call_7538,call_7558,call_7578,const_7576,var_7577,call_7588,const_7587,])
func_7589 = relay.Function([var_7577,], output)
mod['func_7589'] = func_7589
mod = relay.transform.InferType()(mod)
var_7590 = relay.var("var_7590", dtype = "float64", shape = (315,))#candidate|7590|(315,)|var|float64
output = func_7589(var_7590)
func_7591 = relay.Function([var_7590], output)
mutated_mod['func_7591'] = func_7591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5770_call = mod.get_global_var('func_5770')
func_5772_call = mutated_mod.get_global_var('func_5772')
call_7606 = relay.TupleGetItem(func_5770_call(), 0)
call_7607 = relay.TupleGetItem(func_5772_call(), 0)
output = call_7606
output2 = call_7607
func_7611 = relay.Function([], output)
mod['func_7611'] = func_7611
mod = relay.transform.InferType()(mod)
mutated_mod['func_7611'] = func_7611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7611_call = mutated_mod.get_global_var('func_7611')
call_7612 = func_7611_call()
output = call_7612
func_7613 = relay.Function([], output)
mutated_mod['func_7613'] = func_7613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5563_call = mod.get_global_var('func_5563')
func_5565_call = mutated_mod.get_global_var('func_5565')
call_7626 = relay.TupleGetItem(func_5563_call(), 1)
call_7627 = relay.TupleGetItem(func_5565_call(), 1)
output = call_7626
output2 = call_7627
func_7628 = relay.Function([], output)
mod['func_7628'] = func_7628
mod = relay.transform.InferType()(mod)
output = func_7628()
func_7629 = relay.Function([], output)
mutated_mod['func_7629'] = func_7629
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7639 = relay.var("var_7639", dtype = "float64", shape = (11, 13, 14))#candidate|7639|(11, 13, 14)|var|float64
const_7640 = relay.const([[[-9.838123,8.941645,-8.907503,1.630957,7.283681,-9.281693,-2.855643,-8.526693,-5.597744,3.327998,-4.621992,-5.612344,0.716086,-9.075706],[-3.700262,-4.069048,-5.334629,-5.166904,6.064743,-3.833306,-9.087819,-1.898968,5.228903,-5.534056,-7.993168,-9.733081,5.578265,6.711222],[-9.419558,5.588267,5.891161,5.611717,5.307786,-0.532418,7.544105,-3.864593,-0.372440,4.541617,8.414862,9.603268,2.276906,7.105051],[-0.583525,1.316658,-6.230466,-1.698731,2.649856,0.995130,3.172596,8.759396,-2.447521,-7.565569,-4.695116,-5.100719,8.258988,-8.836765],[-8.717875,8.488090,-9.138162,8.690731,-0.446716,-6.148205,1.014731,-8.470059,5.713498,-0.049931,5.450203,-8.108962,-9.694776,-0.391246],[7.265723,-2.895224,-9.806489,-1.116469,2.330657,7.407576,9.340425,1.893322,-7.332483,8.560191,6.243257,3.585492,-5.490711,0.159133],[9.140225,3.723911,-9.456142,-4.868870,7.363275,1.111186,-5.777526,-4.136417,-8.589236,-2.195122,-0.365261,-9.438210,0.144036,-6.132619],[-0.957044,-4.793213,7.374671,-8.292193,-4.646195,-5.834130,6.005706,-6.709209,2.911425,-9.106020,-3.856900,-1.278895,-3.754331,-4.231383],[-9.333676,-8.109933,-9.250725,-6.481178,-0.835674,6.384022,6.235806,-8.510270,5.433142,-1.455303,-5.469463,-6.082340,-8.538686,1.003943],[-5.528463,-0.660490,-6.538807,6.776873,-8.096819,3.494116,-3.338558,9.825272,-7.165838,-9.966310,-1.968141,-8.005507,2.281684,4.795236],[8.550013,8.557118,-6.268445,6.923974,-0.144270,-2.101142,-2.667979,9.006158,-1.132884,1.898677,-5.403631,0.762467,-9.894852,9.945465],[-8.728818,6.835545,0.032917,8.447349,9.266779,3.362397,4.184431,-4.333860,4.103885,-3.086624,-6.005590,-9.453292,-0.863164,5.298699],[-3.174736,-4.679490,3.535826,-4.411669,-6.259232,-0.019605,-8.218528,7.594728,0.338324,-3.730313,1.444975,2.800403,-8.006307,6.583407]],[[1.609321,3.529173,2.551761,-7.062861,-2.131322,-6.252668,4.978131,-6.722197,-1.929751,9.450389,4.665310,-1.966588,0.054321,-3.855727],[3.442917,-7.296139,-7.235221,-8.375611,2.235280,-6.074967,-3.262967,2.620096,0.606651,4.525149,7.629238,-0.444845,-2.105813,-2.487049],[-9.625025,7.371393,-1.627190,-9.564256,-6.020673,-4.208667,9.066450,9.857883,5.929880,4.218708,-5.323170,-4.043300,-2.124362,-8.766824],[3.542945,-3.969892,3.584178,-9.154963,2.921224,-2.286373,7.173622,5.170694,0.909050,-5.895880,5.247762,4.660953,5.970397,-1.215229],[-2.689258,-2.142103,8.998123,7.815169,8.892010,-5.269745,-6.320312,-9.797482,2.229633,5.742607,-6.416498,-6.393197,0.791605,3.859115],[9.474298,-9.623445,-7.704263,-2.923336,7.879999,-0.381997,2.570164,3.422311,2.065035,2.948093,-7.282132,2.102566,5.594376,-9.623531],[7.262220,2.713379,0.554621,1.058723,-9.564133,1.512354,4.677671,-7.509739,-9.099155,5.423730,7.703110,1.175526,5.748900,-7.627818],[-1.249694,9.997133,-3.491767,-7.031826,0.113730,4.815783,3.579929,5.045763,-5.751739,2.630026,-7.990411,-8.935611,-3.545173,1.217004],[-9.159959,-8.300023,-1.559901,2.079198,-3.708646,9.372855,3.298172,3.158494,4.581359,9.661403,4.018586,6.464025,4.067900,4.717800],[3.076060,2.709363,7.709973,-6.517420,-7.049966,-5.671484,0.260309,-4.915422,3.491087,-6.525150,-5.294144,-9.764029,-9.452597,3.196559],[-4.141749,8.660677,2.037830,8.466967,-4.457202,3.682726,9.994744,1.310814,3.994765,4.982460,-0.339928,0.391009,-1.832588,-0.422550],[2.429242,-1.943223,-7.265110,3.733499,7.272059,-6.889472,-2.147954,-2.850849,-1.722941,4.605218,3.898552,-5.033227,-4.642171,-7.450854],[7.676781,1.487338,9.062891,-0.080375,-4.741338,6.813591,3.804697,2.367254,6.267496,0.686899,-7.971248,5.934895,-8.864333,2.949402]],[[-7.748809,9.550249,-5.448321,-0.659983,-9.123708,2.400546,6.241558,-5.034481,6.110393,-2.889437,9.988849,-1.595614,-2.202687,2.025589],[0.875538,8.693466,0.226606,0.446780,-7.569761,1.677077,9.801520,2.161968,6.912203,2.404241,7.758308,-2.652186,2.844964,-8.130340],[-1.985369,-9.539526,-6.842680,5.486069,-3.248488,7.960659,8.137632,-1.421515,-2.214464,9.601301,2.693209,-9.394223,-8.639234,-3.443406],[3.631108,-5.865551,-6.357372,8.161763,-0.720651,-0.056539,9.363424,6.781483,-3.099381,4.544314,1.580297,1.568731,0.831510,-7.496221],[-7.113358,-3.032288,0.541859,4.807485,5.949574,3.725636,-9.951609,4.963177,1.760400,-3.659200,-2.618826,-6.507687,-5.020550,-3.764061],[7.321716,5.884746,0.791246,9.387544,-1.380240,5.079910,0.690294,-1.795036,-8.914130,-5.315694,-8.772904,-2.540737,-5.495882,9.177624],[-2.176479,5.230023,-6.577651,5.388296,-7.067180,-1.053603,2.813355,-6.910258,-0.931862,-4.992347,-7.200977,3.791038,8.981523,7.741132],[-4.681680,-7.748791,6.366943,3.523764,5.860876,0.530403,3.891341,-4.096250,5.484543,-6.423860,5.494700,7.084173,3.472199,8.114669],[-1.937886,-5.752007,9.544449,8.264462,-5.734436,-7.577360,5.569238,5.086102,4.825303,8.402049,4.625448,8.020478,8.184568,-4.500395],[5.923727,3.974075,2.104423,-4.798179,9.762401,8.714333,-3.241811,9.795504,3.436610,7.113476,-7.279517,-9.935384,-7.502602,9.255880],[-4.850385,-5.755315,2.557395,3.791524,7.985594,6.812656,4.487415,2.775764,-4.639917,7.307752,2.431872,-2.209518,1.389893,9.575129],[-9.432405,4.400959,4.363678,-3.542164,-1.557162,7.723210,-8.570848,-5.490536,6.455868,4.748522,-1.325890,6.920240,5.234279,9.011398],[-7.904998,-9.438596,1.861206,1.161524,3.370058,6.056426,4.714004,-0.713637,8.118831,4.224794,-4.158442,-4.767369,9.164975,-4.846713]],[[-9.315387,-3.118713,1.967747,8.096236,-0.699383,1.006464,2.567041,8.796579,1.917280,-3.494288,-1.018666,9.347886,-5.231408,4.927695],[5.868809,2.330949,-0.493701,1.060741,-5.500545,-1.409144,4.017188,1.329567,3.702604,-2.037160,-2.358396,4.732476,-6.154369,7.017511],[6.930200,2.739001,-3.581023,-3.757526,-2.800694,-6.339238,-6.658991,1.911775,-1.814287,-5.921271,-6.237584,-5.252569,0.315389,8.865839],[-5.939131,8.346976,-8.408551,9.013344,4.409205,2.655754,1.191067,-8.798151,-0.107856,2.115324,-6.533845,-5.651565,-0.150240,9.229874],[9.321714,-7.409486,0.822350,0.535663,-5.448593,9.362071,-1.892450,9.529912,-2.413063,9.555241,1.496500,-3.261662,6.747030,-8.972360],[9.831133,2.097367,8.086749,3.414150,3.885006,-8.635392,4.610042,7.669196,-9.817074,2.852758,1.816156,7.126441,5.928805,-2.182397],[9.247478,0.981131,5.381874,0.469829,-0.885033,3.022578,4.624786,8.306394,8.697703,-6.854283,9.805271,5.652447,-8.985587,0.193170],[-8.817060,-8.105685,9.126704,-8.149233,7.559865,1.896700,-9.590432,8.451592,-4.414017,-3.907670,-3.077013,5.817883,-1.213100,-4.915762],[3.706487,0.548778,0.792320,5.826554,4.719616,1.488487,5.146163,-1.729652,-9.820933,1.682217,-1.150804,-3.737742,-8.610893,-5.699261],[-4.390932,-2.339020,-5.042665,5.725005,4.181438,-8.346744,8.085830,7.611138,-4.304691,-8.344912,-9.426228,0.888890,-8.197718,3.599979],[7.156583,9.412464,-4.850900,-6.138148,3.814390,-3.060556,-4.752439,2.196845,1.991672,3.626572,-4.746123,-3.870871,2.633493,1.840200],[1.834903,4.778689,-4.275135,3.739807,-3.488324,-8.615103,9.018324,-4.363325,8.453062,2.068295,1.153184,1.323288,7.117480,-3.186523],[6.890248,-2.615815,-5.319477,-5.837605,-5.410543,0.069056,9.787371,4.577874,-1.347205,-2.536970,8.830382,-7.880815,-6.854235,5.171763]],[[7.536538,0.467428,6.840982,-3.613789,1.970743,1.647041,-3.631640,-4.062273,-2.449821,-2.207086,4.965179,-8.805771,5.579013,3.121574],[-1.342338,3.112167,-1.991772,7.366520,-8.535701,9.392958,-5.320349,1.769437,6.252755,-3.333903,4.449889,1.969956,1.765238,-2.500598],[-1.058858,0.087618,-9.991154,9.342328,2.742997,-4.856325,-2.021301,8.188659,-1.568680,8.929097,-1.387878,6.204327,-8.806966,-6.972400],[5.119645,-7.557724,8.428762,-6.459792,-8.904276,-9.607757,-9.629152,2.246753,5.831858,3.897708,-6.051852,0.041532,-1.643891,-7.377181],[4.608930,8.483994,0.070197,5.659543,4.465934,-2.571590,5.447427,3.978501,-4.696628,-5.117571,9.143692,0.235267,-3.280990,-6.501975],[-5.203880,7.031989,3.504545,-9.706227,1.162100,6.432776,9.916239,-5.494661,7.550173,6.499687,8.043319,8.999491,0.766467,-0.268721],[0.755394,4.065514,3.089344,-3.955697,6.150189,-9.395904,-7.234994,8.398072,8.433018,-6.241749,7.358811,-1.569010,9.724444,9.339240],[3.309028,-2.783717,-2.423315,-2.436306,-5.377995,-9.772776,0.656249,-0.484007,9.443009,2.920600,-3.157809,5.220081,0.824940,-2.993487],[6.027300,-4.911403,4.952187,2.526841,-1.309913,7.811419,-5.704876,-9.871910,-1.171400,6.125996,-6.494480,2.358853,-1.231833,-1.535099],[-1.565098,-0.592707,-4.083529,-0.578010,4.970389,4.624837,6.754460,8.865094,-7.712895,9.700324,-8.069027,-8.109674,-7.919915,0.870181],[-8.022552,-5.147832,-1.430237,-3.647445,7.223141,-1.317340,7.671605,-8.522764,2.995307,-1.265765,4.986185,-7.325211,1.749126,-4.012271],[-8.343248,-7.318309,6.960146,-1.594140,-1.408352,-5.666221,6.456795,-7.805749,-8.112277,-0.911902,-6.678530,-1.868485,-1.064584,-4.499284],[3.308249,3.107140,-1.596361,6.928445,3.929538,-7.598430,-1.244435,2.655317,6.926831,-6.544934,2.947787,8.767239,-7.480021,5.270981]],[[7.240340,-8.932817,8.886129,-3.836118,4.684800,7.282562,7.298133,-6.773531,8.305834,-5.001858,-1.965395,-1.185938,4.089449,4.928190],[9.230075,-8.556853,-3.859603,-6.203197,7.893904,-8.311794,-4.916777,8.016395,5.100902,6.246232,9.246498,1.861027,0.413943,3.674111],[-4.347014,-7.519554,-3.193565,-0.797734,5.658920,-4.909889,3.503208,5.288533,-3.120220,-4.375730,5.358575,-0.887726,3.089287,-9.440618],[-7.880443,8.373970,-1.218513,-0.887634,-4.488051,-5.694055,7.264418,-0.636553,9.054836,-0.292464,-9.377510,4.917139,4.517223,8.021846],[2.323307,3.161481,6.069303,-1.384076,-0.286331,-3.262783,1.310555,-4.843111,9.844303,-5.918313,-2.248918,5.053689,7.903072,-3.111828],[-1.746948,9.138871,0.829063,7.902648,5.558012,3.093875,1.815011,-5.806470,-3.597549,3.110085,-3.634977,-6.283121,6.190149,1.312989],[-8.661116,7.739912,1.148600,-7.769977,5.505787,-8.812091,-3.015223,-3.962383,8.762219,-0.817775,3.228422,-0.338585,5.533946,-8.812930],[-2.442213,8.588171,-0.602959,5.576879,4.630560,-9.774651,-7.858970,2.384593,-0.821445,-2.839172,1.353868,7.110763,-1.798970,-1.971402],[-6.210207,-4.638812,-6.545344,1.276089,-9.480660,5.949094,1.380710,-8.685053,-5.265371,-0.271941,4.591314,-6.766861,2.640606,6.529908],[4.708029,-0.977580,8.991172,-6.923704,-4.659420,-5.712588,0.363446,1.630415,7.807437,-9.701494,1.158037,0.440328,1.529874,3.064650],[6.589839,-4.418763,-3.244101,7.824942,-6.840258,-8.728053,9.311553,5.640565,-2.837274,7.447924,4.068560,8.508315,-6.378025,0.653299],[-6.483816,3.348372,-5.282538,9.022513,-8.181861,-3.246268,-2.874311,6.227657,8.678442,-4.796831,6.750641,3.222720,6.532020,-7.784540],[6.546243,7.006728,-1.140134,-7.318111,4.142877,-1.713600,-1.340229,-7.159302,4.083006,-4.413784,-6.036728,-0.304497,4.385180,-4.339063]],[[-1.490375,-1.412509,2.089906,1.243649,-3.017762,-5.071898,9.463111,1.204635,8.992850,0.253119,-2.134691,9.349351,-9.162652,-9.740977],[3.883682,4.260640,5.218942,-9.206384,9.954329,8.859258,1.189615,7.073969,-5.522457,-1.398582,-3.531867,-9.107969,9.820119,-4.654816],[7.655004,1.981450,1.422724,-3.962420,5.634589,3.332058,-5.039484,-3.063474,-2.601812,1.461629,6.382754,-2.700370,4.410911,-2.576462],[-5.474121,-1.537969,2.619396,2.897375,-2.397629,-7.053309,-9.879391,2.349376,-3.617626,-8.419235,0.095416,5.956197,0.986653,4.885352],[-9.251909,4.841328,-6.519082,-8.958346,-5.850815,-9.636072,9.556417,-1.176497,3.805631,-8.704608,3.507436,-4.482107,-6.109692,9.611039],[-2.612391,-6.093813,-7.285114,1.680298,-0.339708,1.722153,4.771764,2.142751,-4.813093,-0.555071,5.588751,7.713368,6.412935,-9.346053],[0.327766,3.677474,-2.240685,-1.236899,-9.783542,9.719212,1.602935,3.714983,-1.896985,2.048087,-1.774968,-7.431992,-7.538415,-3.533776],[-6.770820,-2.480625,0.510051,4.467988,5.902099,-9.868540,2.684124,-5.745252,-3.836496,-8.848715,8.435056,8.165425,1.271428,1.059855],[8.571460,-0.738321,-8.629881,3.973032,-2.280617,5.765392,-2.258196,4.743486,1.906963,-8.858790,2.470990,7.571886,-9.934486,-5.390388],[-4.232369,-3.628752,-4.108031,1.857955,5.741399,-5.266781,8.295973,2.292705,9.622348,-7.438114,0.085456,4.913367,4.287340,6.953155],[2.781637,2.937829,4.181478,-1.409839,-2.062764,2.230133,-5.346783,-1.490657,8.891766,-4.901970,-7.209587,-8.441427,3.711949,9.000743],[-6.634068,6.588175,-3.129794,5.818705,-3.795126,7.501885,-2.704938,-9.809787,-1.797733,-0.129597,-6.088824,5.967545,4.563822,-2.619104],[5.784102,0.724048,-7.886532,3.151521,-1.435974,0.053970,-7.011761,1.418533,8.997619,-2.035101,-1.501454,6.267174,1.675609,-8.750335]],[[-9.453626,1.771800,-7.297804,1.079447,6.559495,7.102458,-9.775196,-7.726797,-3.671049,6.436518,1.247424,8.968429,-9.651668,6.014055],[0.316156,5.078248,-3.938877,3.071006,8.558520,-2.342885,-4.266642,-0.327649,-6.438017,7.572393,2.254711,-4.939998,-1.508831,-3.431391],[-4.481931,-7.243808,9.932828,-6.822596,1.987516,-4.497297,-9.095177,6.269575,5.528131,4.592735,0.615782,-9.215114,6.366871,8.682082],[-8.638125,5.619743,5.975372,4.971155,6.652468,2.093751,0.422468,7.317636,-3.608117,-3.499174,5.716070,1.337642,6.030715,4.501762],[-1.468975,-9.467684,-3.230508,0.154201,-7.985899,9.560316,-5.330215,-3.294009,-1.904214,-3.718467,-2.045413,-6.352868,-2.083276,-1.209001],[8.428193,7.319242,7.818874,6.623667,9.235373,2.527309,0.464072,8.098670,8.032682,0.955402,6.182989,-8.088851,8.478873,4.818545],[-3.442620,6.943284,0.774089,8.925572,-6.906306,5.870771,-3.611544,0.129173,0.048619,2.118150,-0.576922,-2.676357,-2.545903,-9.377585],[-4.590517,-3.191318,1.049699,-5.277274,-9.219577,5.646118,-2.949234,-2.501384,-1.969442,-9.791273,-2.120336,-6.663694,3.409344,-0.456861],[-7.760433,3.332405,0.487142,8.543372,7.572919,1.761797,-0.875221,-2.490651,6.724686,7.809574,9.065222,7.718987,1.910809,-4.414084],[0.141573,9.293739,6.782238,-6.381047,-7.478250,-9.800568,3.891143,4.751567,-0.466095,4.187746,-4.009717,0.778402,-0.839604,7.657312],[0.997578,-4.020416,-5.934211,-5.571730,-2.601801,-5.807774,-9.975425,-3.914520,0.164075,5.210795,-7.844947,0.397423,8.941188,-4.017044],[-7.169492,-4.242708,1.275974,-6.071047,-1.328827,-3.727365,8.204848,0.237101,1.501077,0.911017,9.407423,-4.425977,5.498209,-8.081640],[5.109350,8.498412,-5.683788,1.560533,-8.397095,3.184496,-4.793454,-7.588758,2.435743,8.362363,4.259995,3.825782,-9.375707,-3.258769]],[[7.947340,-7.405770,6.513361,-6.287725,4.991657,-6.273422,6.337677,-9.494338,3.393814,6.175083,-1.174210,9.387787,-3.541980,-3.392947],[-3.231565,-3.954826,2.333438,-9.016667,-9.484302,-0.974416,-6.700215,-6.646305,4.825640,8.070654,0.061431,4.881409,-0.067733,9.592663],[4.019766,3.885246,8.048554,3.969680,-6.879144,2.583410,5.831034,3.006100,-3.370056,1.746575,-6.793334,-1.209306,-0.667464,-2.769933],[-9.792138,0.952399,9.947525,-2.212468,-3.951886,-9.226787,0.028184,-6.336929,5.019530,5.476492,9.413101,5.660940,3.602397,0.179613],[6.374054,-3.328763,3.521671,6.149143,-7.990421,8.641598,-1.340387,-0.135808,-8.598157,-4.077714,-2.913321,4.392036,-9.352915,7.096702],[9.079077,5.295433,-2.932730,-3.860420,3.301388,4.898581,6.109913,5.432761,-8.985405,-0.866124,-5.018840,-0.813036,-1.419344,-4.132063],[8.225046,-0.645568,-1.687737,7.828333,-6.505135,-8.257521,-1.272070,3.159454,7.292688,7.992769,-4.957999,-0.609793,-4.961876,6.511133],[-4.587657,5.626158,-1.073968,-5.170996,-1.940230,5.491722,-3.035970,-4.231217,2.803939,-8.381669,-0.651651,-9.640533,1.810695,7.099421],[-3.502051,-7.272662,-5.817626,-8.930893,-9.590838,8.476968,-9.003655,5.786056,9.515049,1.579491,6.763244,7.805019,2.366793,4.622770],[-0.961767,-6.538358,1.277868,1.168565,1.724639,-5.020194,3.331776,-8.587382,4.379146,-0.365972,3.018463,2.239840,9.006761,4.058076],[9.284434,-1.743665,7.933218,-7.848606,2.000062,3.670088,7.345988,-7.009067,8.817851,-7.230100,-0.386876,0.654391,2.678225,1.699105],[9.160185,7.161611,2.162460,-6.963850,0.169708,7.930241,0.226826,5.342322,8.020573,1.157720,-1.694739,5.217861,-7.981927,-9.525215],[7.168777,-8.303093,-5.149879,9.095169,7.116819,4.310917,-4.394603,-1.883471,5.059330,-4.870185,1.559193,5.229226,-7.695070,6.469030]],[[-7.036696,-9.951212,0.358387,-3.488688,-9.769113,5.070457,-3.636294,-8.231792,6.323709,-5.981509,-5.880524,1.173811,-4.004582,6.812428],[3.795028,3.131669,6.297288,-1.419901,-7.460001,-8.650084,-2.129296,8.543599,-2.456555,-4.699107,-0.112039,-1.101212,4.230296,-7.203715],[4.873146,-0.657359,-8.811607,-7.274738,7.734117,-4.384804,2.523739,5.442233,-5.389298,-0.408747,-1.736618,3.861863,4.268087,-3.370237],[2.726459,-1.230996,-0.888040,-4.606778,-2.270116,-7.366968,6.228973,-1.835159,-3.414611,-7.706698,-0.610697,1.837318,5.606775,0.202191],[3.837721,-9.216358,-0.534376,8.455384,3.871873,-6.880417,-0.789179,-8.523649,9.607597,-4.012570,-4.876103,1.249225,-1.942287,7.330277],[3.422658,-7.820320,-1.470517,9.174590,-0.148730,-4.698941,-1.243026,3.263270,5.185921,-9.130971,-0.447302,-8.223807,-7.762557,4.504548],[5.400444,-6.098458,4.886939,0.993569,0.205757,6.547931,6.259589,-8.405193,-3.291836,-3.724811,0.124638,-2.078450,5.298298,-1.525156],[-7.121263,-4.213585,-9.498769,-8.287348,-9.485689,-4.924016,7.075810,1.753428,2.482926,-9.156364,4.022370,5.805518,-7.529409,9.707379],[6.982246,8.904760,0.596317,1.048022,-3.683377,-7.886522,2.015037,4.736544,-4.489455,6.508749,-4.366017,9.377546,-4.192150,-8.115594],[-9.122665,-6.141139,1.546881,-2.215452,-5.440595,-6.307135,4.572652,6.949870,1.778190,2.054897,7.322671,3.390878,4.242954,0.229751],[-7.541766,-2.084418,3.846496,-2.340977,-6.741667,-7.005089,-0.786689,0.955950,6.950943,-9.772649,9.306642,-1.331398,-3.895029,-4.638273],[-3.592715,2.112573,1.097413,6.001699,-3.610032,6.495728,-5.054671,9.369869,5.369322,2.144110,7.750450,4.779007,3.575622,1.595343],[-9.392488,8.441484,-9.283937,1.463789,-4.757491,-0.751321,-3.685914,3.090885,6.790318,6.296707,-6.130219,6.653331,-2.943510,-8.870112]],[[-1.497085,3.089622,-4.622145,2.557085,7.147998,-7.998392,-5.461695,-7.293171,4.887291,6.131075,6.259823,8.573049,4.210859,3.605612],[4.338890,-3.437303,-7.433876,-4.354468,-8.908282,3.687125,-2.404761,-0.528399,-6.787059,3.675064,-1.902978,0.891839,3.241030,7.758098],[3.870056,-5.005902,8.239630,5.119896,-9.899554,-6.917783,7.908986,-3.046127,0.393898,-5.633269,-2.801386,6.095640,4.465724,-3.985268],[0.862415,3.309446,-4.382684,-7.856518,-9.119681,5.542946,2.194919,-5.255338,8.738103,1.724187,8.767769,0.455901,5.995643,-2.256262],[3.380740,-0.675647,2.860926,5.685606,6.156989,1.475504,3.009271,6.145771,-3.078703,-7.186728,-8.267882,-5.591567,6.991563,7.365110],[5.799304,7.068349,-2.504194,7.377125,-7.799433,-3.331802,-0.115855,2.481765,-1.849645,9.286249,-2.036726,6.972298,7.229314,-6.192400],[5.171440,5.596559,-8.884856,7.328887,-6.119867,-9.045117,0.164248,4.793605,-0.097864,-6.586290,2.721999,3.708367,5.423724,-2.636835],[-1.375157,0.540051,4.157191,-1.752705,-3.644558,-6.247165,5.566102,4.520666,6.707304,-5.951709,3.227451,7.307982,-2.694669,7.081982],[0.478417,-7.787097,-9.223900,0.552654,4.376113,1.357347,3.104647,-1.263859,-6.355568,6.965997,-5.602235,8.125040,-1.433864,-9.530378],[5.638719,-2.812892,-5.659059,8.855591,6.141439,-8.342914,-4.713387,-8.513586,7.270936,-1.830054,-2.424091,-8.940657,-6.263546,-2.370149],[-5.814260,4.369860,-9.032199,-4.341663,8.438161,-0.121895,-9.146336,4.719114,-9.352988,-2.544601,-1.907726,-7.419398,-3.978181,-0.769226],[-0.152407,-4.819535,9.658394,8.333850,6.000361,-5.842769,1.943076,2.915165,5.230434,-6.069516,-7.778527,-3.187188,-4.994298,7.034175],[4.494058,4.638953,7.541524,-6.433764,5.450002,-9.053028,8.134801,3.690297,0.666790,-3.032748,8.838693,2.646840,2.819000,6.185553]]], dtype = "float64")#candidate|7640|(11, 13, 14)|const|float64
bop_7641 = relay.floor_divide(var_7639.astype('float64'), relay.reshape(const_7640.astype('float64'), relay.shape_of(var_7639))) # shape=(11, 13, 14)
bop_7648 = relay.power(bop_7641.astype('float64'), relay.reshape(const_7640.astype('float64'), relay.shape_of(bop_7641))) # shape=(11, 13, 14)
func_5061_call = mod.get_global_var('func_5061')
func_5064_call = mutated_mod.get_global_var('func_5064')
var_7661 = relay.var("var_7661", dtype = "float64", shape = (91, 1))#candidate|7661|(91, 1)|var|float64
call_7660 = relay.TupleGetItem(func_5061_call(relay.reshape(var_7661.astype('float64'), [91,])), 3)
call_7662 = relay.TupleGetItem(func_5064_call(relay.reshape(var_7661.astype('float64'), [91,])), 3)
output = relay.Tuple([bop_7648,call_7660,var_7661,])
output2 = relay.Tuple([bop_7648,call_7662,var_7661,])
func_7683 = relay.Function([var_7639,var_7661,], output)
mod['func_7683'] = func_7683
mod = relay.transform.InferType()(mod)
var_7684 = relay.var("var_7684", dtype = "float64", shape = (11, 13, 14))#candidate|7684|(11, 13, 14)|var|float64
var_7685 = relay.var("var_7685", dtype = "float64", shape = (91, 1))#candidate|7685|(91, 1)|var|float64
output = func_7683(var_7684,var_7685,)
func_7686 = relay.Function([var_7684,var_7685,], output)
mutated_mod['func_7686'] = func_7686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mod.get_global_var('func_3542')
func_3544_call = mutated_mod.get_global_var('func_3544')
call_7743 = relay.TupleGetItem(func_3542_call(), 2)
call_7744 = relay.TupleGetItem(func_3544_call(), 2)
output = relay.Tuple([call_7743,])
output2 = relay.Tuple([call_7744,])
func_7745 = relay.Function([], output)
mod['func_7745'] = func_7745
mod = relay.transform.InferType()(mod)
output = func_7745()
func_7746 = relay.Function([], output)
mutated_mod['func_7746'] = func_7746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7749 = relay.var("var_7749", dtype = "uint16", shape = (7, 7, 2))#candidate|7749|(7, 7, 2)|var|uint16
const_7750 = relay.const([[[6,-3],[8,-4],[2,-7],[-6,-9],[-6,7],[8,-7],[-4,-2]],[[3,-9],[2,1],[-3,-4],[-9,-1],[10,7],[-4,-3],[10,7]],[[-4,-7],[1,-6],[-7,2],[-10,-7],[7,-5],[10,6],[4,6]],[[-9,8],[-4,-10],[10,-7],[-5,-6],[-7,-5],[3,-5],[3,6]],[[-1,1],[-5,-5],[5,-5],[3,1],[3,2],[-2,-6],[8,7]],[[3,9],[8,-5],[-3,6],[-4,-3],[5,5],[-1,9],[6,8]],[[9,7],[1,-5],[10,-3],[-8,8],[-10,-1],[3,2],[-4,7]]], dtype = "uint16")#candidate|7750|(7, 7, 2)|const|uint16
bop_7751 = relay.add(var_7749.astype('uint16'), relay.reshape(const_7750.astype('uint16'), relay.shape_of(var_7749))) # shape=(7, 7, 2)
bop_7757 = relay.bitwise_and(const_7750.astype('uint8'), relay.reshape(bop_7751.astype('uint8'), relay.shape_of(const_7750))) # shape=(7, 7, 2)
output = relay.Tuple([bop_7757,])
output2 = relay.Tuple([bop_7757,])
func_7760 = relay.Function([var_7749,], output)
mod['func_7760'] = func_7760
mod = relay.transform.InferType()(mod)
mutated_mod['func_7760'] = func_7760
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7761 = relay.var("var_7761", dtype = "uint16", shape = (7, 7, 2))#candidate|7761|(7, 7, 2)|var|uint16
func_7760_call = mutated_mod.get_global_var('func_7760')
call_7762 = func_7760_call(var_7761)
output = call_7762
func_7763 = relay.Function([var_7761], output)
mutated_mod['func_7763'] = func_7763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7312_call = mod.get_global_var('func_7312')
func_7313_call = mutated_mod.get_global_var('func_7313')
call_7843 = relay.TupleGetItem(func_7312_call(), 0)
call_7844 = relay.TupleGetItem(func_7313_call(), 0)
func_4543_call = mod.get_global_var('func_4543')
func_4546_call = mutated_mod.get_global_var('func_4546')
const_7853 = relay.const([-9.612261,-3.573299,8.137511,-7.589136,-6.456765,3.610859,0.373790,1.204933,5.385697,-7.680587,0.755647,-8.477530,-3.104699,-6.455117,-0.084108,8.306889,2.297892,6.194660,6.565708,3.629711,-3.918964,-6.781167,-4.376206,4.969047,4.729635,8.359219,-1.228205,-0.952643,-6.540934,-9.740211,-7.719923,5.843577,1.893326,-2.205901,-1.170465,3.677885,-8.486310,-5.273170,8.958224,-2.438609,3.651485,3.195144,5.515087,-6.996619,-3.063758,-4.195286,8.230442,-3.188251,-4.977158,9.884544,0.300503,0.370876,-6.900606,-2.177325,-6.639064,2.268980,8.730859,8.542720,-1.888111,-0.514705,-0.798843,8.051527,-0.817701,3.557465,-7.779110,3.678502,1.281776,-9.569580,-3.043121,9.319174,9.431309,3.783709,-2.797749,-1.393758,-4.388665,1.968020,0.689664,-4.543469,8.672446,7.414580,1.540525,0.822634,5.921221,-7.864422,-4.106829,-2.266448,-5.322557,-9.908213,-9.272637,3.741386,5.523520], dtype = "float64")#candidate|7853|(91,)|const|float64
call_7852 = func_4543_call(relay.reshape(const_7853.astype('float64'), [7, 1, 13]))
call_7854 = func_4543_call(relay.reshape(const_7853.astype('float64'), [7, 1, 13]))
output = relay.Tuple([call_7843,call_7852,const_7853,])
output2 = relay.Tuple([call_7844,call_7854,const_7853,])
func_7855 = relay.Function([], output)
mod['func_7855'] = func_7855
mod = relay.transform.InferType()(mod)
mutated_mod['func_7855'] = func_7855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7855_call = mutated_mod.get_global_var('func_7855')
call_7856 = func_7855_call()
output = call_7856
func_7857 = relay.Function([], output)
mutated_mod['func_7857'] = func_7857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7628_call = mod.get_global_var('func_7628')
func_7629_call = mutated_mod.get_global_var('func_7629')
call_7902 = func_7628_call()
call_7903 = func_7628_call()
output = relay.Tuple([call_7902,])
output2 = relay.Tuple([call_7903,])
func_7912 = relay.Function([], output)
mod['func_7912'] = func_7912
mod = relay.transform.InferType()(mod)
output = func_7912()
func_7913 = relay.Function([], output)
mutated_mod['func_7913'] = func_7913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7528_call = mod.get_global_var('func_7528')
func_7529_call = mutated_mod.get_global_var('func_7529')
call_7944 = func_7528_call()
call_7945 = func_7528_call()
output = relay.Tuple([call_7944,])
output2 = relay.Tuple([call_7945,])
func_7950 = relay.Function([], output)
mod['func_7950'] = func_7950
mod = relay.transform.InferType()(mod)
mutated_mod['func_7950'] = func_7950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7950_call = mutated_mod.get_global_var('func_7950')
call_7951 = func_7950_call()
output = call_7951
func_7952 = relay.Function([], output)
mutated_mod['func_7952'] = func_7952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6546_call = mod.get_global_var('func_6546')
func_6548_call = mutated_mod.get_global_var('func_6548')
call_7964 = func_6546_call()
call_7965 = func_6546_call()
output = relay.Tuple([call_7964,])
output2 = relay.Tuple([call_7965,])
func_7973 = relay.Function([], output)
mod['func_7973'] = func_7973
mod = relay.transform.InferType()(mod)
output = func_7973()
func_7974 = relay.Function([], output)
mutated_mod['func_7974'] = func_7974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7287_call = mod.get_global_var('func_7287')
func_7289_call = mutated_mod.get_global_var('func_7289')
call_8045 = func_7287_call()
call_8046 = func_7287_call()
func_4543_call = mod.get_global_var('func_4543')
func_4546_call = mutated_mod.get_global_var('func_4546')
var_8051 = relay.var("var_8051", dtype = "float64", shape = (91,))#candidate|8051|(91,)|var|float64
call_8050 = func_4543_call(relay.reshape(var_8051.astype('float64'), [7, 1, 13]))
call_8052 = func_4543_call(relay.reshape(var_8051.astype('float64'), [7, 1, 13]))
output = relay.Tuple([call_8045,call_8050,var_8051,])
output2 = relay.Tuple([call_8046,call_8052,var_8051,])
func_8056 = relay.Function([var_8051,], output)
mod['func_8056'] = func_8056
mod = relay.transform.InferType()(mod)
mutated_mod['func_8056'] = func_8056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8057 = relay.var("var_8057", dtype = "float64", shape = (91,))#candidate|8057|(91,)|var|float64
func_8056_call = mutated_mod.get_global_var('func_8056')
call_8058 = func_8056_call(var_8057)
output = call_8058
func_8059 = relay.Function([var_8057], output)
mutated_mod['func_8059'] = func_8059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2382_call = mod.get_global_var('func_2382')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_8099 = func_2382_call()
call_8100 = func_2382_call()
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
call_8110 = func_2059_call()
call_8111 = func_2059_call()
output = relay.Tuple([call_8099,call_8110,])
output2 = relay.Tuple([call_8100,call_8111,])
func_8113 = relay.Function([], output)
mod['func_8113'] = func_8113
mod = relay.transform.InferType()(mod)
output = func_8113()
func_8114 = relay.Function([], output)
mutated_mod['func_8114'] = func_8114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5519_call = mod.get_global_var('func_5519')
func_5520_call = mutated_mod.get_global_var('func_5520')
call_8115 = relay.TupleGetItem(func_5519_call(), 1)
call_8116 = relay.TupleGetItem(func_5520_call(), 1)
func_3277_call = mod.get_global_var('func_3277')
func_3279_call = mutated_mod.get_global_var('func_3279')
var_8123 = relay.var("var_8123", dtype = "float64", shape = (7, 132))#candidate|8123|(7, 132)|var|float64
call_8122 = relay.TupleGetItem(func_3277_call(relay.reshape(var_8123.astype('float64'), [924,])), 4)
call_8124 = relay.TupleGetItem(func_3279_call(relay.reshape(var_8123.astype('float64'), [924,])), 4)
output = relay.Tuple([call_8115,call_8122,var_8123,])
output2 = relay.Tuple([call_8116,call_8124,var_8123,])
func_8125 = relay.Function([var_8123,], output)
mod['func_8125'] = func_8125
mod = relay.transform.InferType()(mod)
var_8126 = relay.var("var_8126", dtype = "float64", shape = (7, 132))#candidate|8126|(7, 132)|var|float64
output = func_8125(var_8126)
func_8127 = relay.Function([var_8126], output)
mutated_mod['func_8127'] = func_8127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2578_call = mod.get_global_var('func_2578')
func_2580_call = mutated_mod.get_global_var('func_2580')
call_8132 = func_2578_call()
call_8133 = func_2578_call()
output = call_8132
output2 = call_8133
func_8136 = relay.Function([], output)
mod['func_8136'] = func_8136
mod = relay.transform.InferType()(mod)
mutated_mod['func_8136'] = func_8136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8136_call = mutated_mod.get_global_var('func_8136')
call_8137 = func_8136_call()
output = call_8137
func_8138 = relay.Function([], output)
mutated_mod['func_8138'] = func_8138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2218_call = mod.get_global_var('func_2218')
func_2220_call = mutated_mod.get_global_var('func_2220')
call_8180 = relay.TupleGetItem(func_2218_call(), 0)
call_8181 = relay.TupleGetItem(func_2220_call(), 0)
func_7745_call = mod.get_global_var('func_7745')
func_7746_call = mutated_mod.get_global_var('func_7746')
call_8185 = relay.TupleGetItem(func_7745_call(), 0)
call_8186 = relay.TupleGetItem(func_7746_call(), 0)
uop_8203 = relay.acos(call_8185.astype('float64')) # shape=(11, 10, 3)
uop_8205 = relay.acos(call_8186.astype('float64')) # shape=(11, 10, 3)
output = relay.Tuple([call_8180,uop_8203,])
output2 = relay.Tuple([call_8181,uop_8205,])
func_8206 = relay.Function([], output)
mod['func_8206'] = func_8206
mod = relay.transform.InferType()(mod)
mutated_mod['func_8206'] = func_8206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8206_call = mutated_mod.get_global_var('func_8206')
call_8207 = func_8206_call()
output = call_8207
func_8208 = relay.Function([], output)
mutated_mod['func_8208'] = func_8208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4478_call = mod.get_global_var('func_4478')
func_4479_call = mutated_mod.get_global_var('func_4479')
call_8216 = relay.TupleGetItem(func_4478_call(), 1)
call_8217 = relay.TupleGetItem(func_4479_call(), 1)
func_3845_call = mod.get_global_var('func_3845')
func_3847_call = mutated_mod.get_global_var('func_3847')
call_8242 = relay.TupleGetItem(func_3845_call(), 0)
call_8243 = relay.TupleGetItem(func_3847_call(), 0)
output = relay.Tuple([call_8216,call_8242,])
output2 = relay.Tuple([call_8217,call_8243,])
func_8244 = relay.Function([], output)
mod['func_8244'] = func_8244
mod = relay.transform.InferType()(mod)
mutated_mod['func_8244'] = func_8244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8244_call = mutated_mod.get_global_var('func_8244')
call_8245 = func_8244_call()
output = call_8245
func_8246 = relay.Function([], output)
mutated_mod['func_8246'] = func_8246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7528_call = mod.get_global_var('func_7528')
func_7529_call = mutated_mod.get_global_var('func_7529')
call_8250 = func_7528_call()
call_8251 = func_7528_call()
func_6195_call = mod.get_global_var('func_6195')
func_6197_call = mutated_mod.get_global_var('func_6197')
call_8253 = relay.TupleGetItem(func_6195_call(), 0)
call_8254 = relay.TupleGetItem(func_6197_call(), 0)
func_4259_call = mod.get_global_var('func_4259')
func_4261_call = mutated_mod.get_global_var('func_4261')
var_8263 = relay.var("var_8263", dtype = "float64", shape = (1, 1200))#candidate|8263|(1, 1200)|var|float64
call_8262 = relay.TupleGetItem(func_4259_call(relay.reshape(var_8263.astype('float64'), [10, 12, 10])), 0)
call_8264 = relay.TupleGetItem(func_4261_call(relay.reshape(var_8263.astype('float64'), [10, 12, 10])), 0)
output = relay.Tuple([call_8250,call_8253,call_8262,var_8263,])
output2 = relay.Tuple([call_8251,call_8254,call_8264,var_8263,])
func_8268 = relay.Function([var_8263,], output)
mod['func_8268'] = func_8268
mod = relay.transform.InferType()(mod)
mutated_mod['func_8268'] = func_8268
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8269 = relay.var("var_8269", dtype = "float64", shape = (1, 1200))#candidate|8269|(1, 1200)|var|float64
func_8268_call = mutated_mod.get_global_var('func_8268')
call_8270 = func_8268_call(var_8269)
output = call_8270
func_8271 = relay.Function([var_8269], output)
mutated_mod['func_8271'] = func_8271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2431_call = mod.get_global_var('func_2431')
func_2433_call = mutated_mod.get_global_var('func_2433')
call_8402 = relay.TupleGetItem(func_2431_call(), 0)
call_8403 = relay.TupleGetItem(func_2433_call(), 0)
var_8405 = relay.var("var_8405", dtype = "float32", shape = (11, 10, 3))#candidate|8405|(11, 10, 3)|var|float32
bop_8406 = relay.bitwise_xor(call_8402.astype('uint16'), relay.reshape(var_8405.astype('uint16'), relay.shape_of(call_8402))) # shape=(11, 10, 3)
bop_8409 = relay.bitwise_xor(call_8403.astype('uint16'), relay.reshape(var_8405.astype('uint16'), relay.shape_of(call_8403))) # shape=(11, 10, 3)
output = relay.Tuple([bop_8406,])
output2 = relay.Tuple([bop_8409,])
F = relay.Function([var_8405,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8405,], output2)
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
