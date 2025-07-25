import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_108 = relay.const([[[-8.771931,-6.602982],[0.520289,-8.650059],[0.685879,-3.201887],[1.164594,7.091009],[-8.087812,0.057104],[-2.944311,0.699369]],[[-2.706368,-6.461060],[5.694826,8.037479],[4.716569,5.847458],[-4.439630,-0.474177],[-0.012532,-7.456184],[5.222234,-2.574212]],[[3.049971,-5.930116],[0.946196,4.300674],[6.039799,8.047361],[2.888042,8.494160],[-8.253511,6.657235],[-7.610015,-3.428128]],[[-9.196174,0.781688],[-7.560948,-8.986387],[2.937280,-8.090028],[-2.745424,-8.335034],[5.472924,-7.362648],[-0.265998,7.756832]],[[-8.101421,-7.362117],[-2.887502,4.590118],[7.972081,-4.481479],[-6.095484,9.726842],[-4.213896,1.690734],[8.570302,-2.782224]],[[1.868847,3.276151],[-8.979207,-3.348012],[-1.908302,-4.886412],[5.636786,2.425890],[-2.969390,8.476141],[-3.019394,-4.737565]],[[-6.650842,7.355183],[3.752350,-7.096418],[5.517868,6.400368],[3.631172,-2.535346],[-2.282485,-5.038140],[9.694301,-0.921451]],[[-9.342460,-4.245428],[-5.883141,7.256102],[-9.454967,-4.304943],[-8.939831,-1.438211],[-1.443232,-0.288449],[3.892190,9.222790]],[[8.742580,-6.701335],[-8.435922,-6.488614],[-0.295749,1.581090],[1.908724,5.564114],[-0.297397,9.460885],[-4.146329,-0.243926]]], dtype = "float32")#candidate|108|(9, 6, 2)|const|float32
uop_109 = relay.sin(const_108.astype('float32')) # shape=(9, 6, 2)
output = uop_109
output2 = uop_109
func_121 = relay.Function([], output)
mod['func_121'] = func_121
mod = relay.transform.InferType()(mod)
mutated_mod['func_121'] = func_121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mutated_mod.get_global_var('func_121')
call_122 = func_121_call()
output = call_122
func_123 = relay.Function([], output)
mutated_mod['func_123'] = func_123
mutated_mod = relay.transform.InferType()(mutated_mod)
var_139 = relay.var("var_139", dtype = "float64", shape = (14, 2, 5))#candidate|139|(14, 2, 5)|var|float64
uop_140 = relay.atanh(var_139.astype('float64')) # shape=(14, 2, 5)
bop_143 = relay.logical_xor(var_139.astype('uint64'), relay.reshape(uop_140.astype('uint64'), relay.shape_of(var_139))) # shape=(14, 2, 5)
output = relay.Tuple([bop_143,])
output2 = relay.Tuple([bop_143,])
func_158 = relay.Function([var_139,], output)
mod['func_158'] = func_158
mod = relay.transform.InferType()(mod)
mutated_mod['func_158'] = func_158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_159 = relay.var("var_159", dtype = "float64", shape = (14, 2, 5))#candidate|159|(14, 2, 5)|var|float64
func_158_call = mutated_mod.get_global_var('func_158')
call_160 = func_158_call(var_159)
output = call_160
func_161 = relay.Function([var_159], output)
mutated_mod['func_161'] = func_161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_175 = func_121_call()
call_176 = func_121_call()
var_183 = relay.var("var_183", dtype = "float32", shape = (9, 6, 2))#candidate|183|(9, 6, 2)|var|float32
bop_184 = relay.logical_xor(call_175.astype('int8'), relay.reshape(var_183.astype('int8'), relay.shape_of(call_175))) # shape=(9, 6, 2)
bop_187 = relay.logical_xor(call_176.astype('int8'), relay.reshape(var_183.astype('int8'), relay.shape_of(call_176))) # shape=(9, 6, 2)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_193 = func_121_call()
call_194 = func_121_call()
func_158_call = mod.get_global_var('func_158')
func_161_call = mutated_mod.get_global_var('func_161')
var_197 = relay.var("var_197", dtype = "float64", shape = (5, 28))#candidate|197|(5, 28)|var|float64
call_196 = relay.TupleGetItem(func_158_call(relay.reshape(var_197.astype('float64'), [14, 2, 5])), 0)
call_198 = relay.TupleGetItem(func_161_call(relay.reshape(var_197.astype('float64'), [14, 2, 5])), 0)
uop_209 = relay.tan(call_175.astype('float64')) # shape=(9, 6, 2)
uop_211 = relay.tan(call_176.astype('float64')) # shape=(9, 6, 2)
output = relay.Tuple([bop_184,call_193,call_196,var_197,uop_209,])
output2 = relay.Tuple([bop_187,call_194,call_198,var_197,uop_211,])
func_212 = relay.Function([var_183,var_197,], output)
mod['func_212'] = func_212
mod = relay.transform.InferType()(mod)
var_213 = relay.var("var_213", dtype = "float32", shape = (9, 6, 2))#candidate|213|(9, 6, 2)|var|float32
var_214 = relay.var("var_214", dtype = "float64", shape = (5, 28))#candidate|214|(5, 28)|var|float64
output = func_212(var_213,var_214,)
func_215 = relay.Function([var_213,var_214,], output)
mutated_mod['func_215'] = func_215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_217 = func_121_call()
call_218 = func_121_call()
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
const_221 = relay.const([9.440450,-4.161109,-3.010453,-4.069671,4.650425,6.353587,-0.979482,-6.524184,7.805097,7.658474,7.616738,9.081749,-5.710230,3.864478,7.659720,-1.001252,-6.284154,6.399955,9.538295,-5.562308,5.411813,7.074844,5.387952,-7.200890,-1.030002,-7.547893,-2.310699,4.089931,-0.303710,-5.115749,0.611801,-4.627858,8.784242,-8.200467,2.348820,1.414220,-0.886093,-5.240228,-0.721490,-1.426753,-2.896159,-7.654205,-7.564065,1.952884,-3.805916,3.109588,6.496654,8.871208,4.974511,0.794619,-1.994512,2.642336,7.056805,-1.967551,0.409147,-6.329902,-7.949776,-4.288714,3.482711,4.439828,6.651324,9.883465,-9.184695,7.593677,-7.495843,-7.124019,1.189759,7.990061,0.150964,-7.011178,-5.072838,-1.855924,-3.288654,-5.689091,2.021681,0.416307,-9.954047,2.289390,-5.231827,-4.888977,7.872418,1.812710,-1.836899,-9.812621,0.969008,-2.080367,8.857735,-3.289473,0.246927,4.446742,-1.377992,3.223929,4.717296,3.105894,9.114786,-9.094659,-9.495039,2.361649,-8.010366,-3.639842,3.660891,-5.216076,1.810210,-1.101109,2.587608,5.975203,-7.613663,-7.004820,6.611423,2.582071,6.100151,-5.429507,-6.713343,-6.372346,1.162215,-7.779842,-3.825706,9.113361,2.892531,-4.320389,-2.179141,-9.859323,7.513406,-4.284075,-7.870423,3.488404,-0.911184,0.415400,-6.644839,6.271169,-7.694417,-1.696290,-8.031763,-1.842201,0.549049,-6.866945,3.593431,-1.516630,5.556982,6.842116], dtype = "float64")#candidate|221|(140,)|const|float64
call_220 = relay.TupleGetItem(func_212_call(relay.reshape(call_217.astype('float32'), [9, 6, 2]), relay.reshape(const_221.astype('float64'), [5, 28]), ), 3)
call_222 = relay.TupleGetItem(func_215_call(relay.reshape(call_217.astype('float32'), [9, 6, 2]), relay.reshape(const_221.astype('float64'), [5, 28]), ), 3)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
call_225 = relay.TupleGetItem(func_212_call(relay.reshape(call_217.astype('float32'), [9, 6, 2]), relay.reshape(const_221.astype('float64'), [5, 28]), ), 3)
call_226 = relay.TupleGetItem(func_215_call(relay.reshape(call_217.astype('float32'), [9, 6, 2]), relay.reshape(const_221.astype('float64'), [5, 28]), ), 3)
uop_232 = relay.asinh(call_225.astype('float32')) # shape=(5, 28)
uop_234 = relay.asinh(call_226.astype('float32')) # shape=(5, 28)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
call_235 = relay.TupleGetItem(func_212_call(relay.reshape(call_217.astype('float32'), [9, 6, 2]), relay.reshape(call_220.astype('float64'), [5, 28]), ), 0)
call_236 = relay.TupleGetItem(func_215_call(relay.reshape(call_217.astype('float32'), [9, 6, 2]), relay.reshape(call_220.astype('float64'), [5, 28]), ), 0)
uop_237 = relay.sqrt(call_225.astype('float32')) # shape=(5, 28)
uop_239 = relay.sqrt(call_226.astype('float32')) # shape=(5, 28)
const_242 = relay.const([[-7.222097,-0.597945,-0.019521,-9.163808,1.481891,-3.163851,5.630693,-4.754318,4.320642,-4.535137,9.380582,-0.625016,-2.625690,-1.324393,-1.840374,2.418908,1.232747,6.779158,7.068281,-1.090241,-0.440262,8.421750,0.442694,-1.581996,-0.586775,-5.258199,-5.496510,1.800291],[-4.134493,-9.899016,-9.212819,-9.672640,8.487595,3.177955,0.473826,-6.978687,-3.781141,-2.844521,2.766662,-4.246925,5.154809,-7.064724,-1.644059,6.631006,4.220345,9.080753,4.597049,7.787701,1.766851,9.354801,4.892927,6.917139,1.159092,4.788143,-3.021041,2.857588],[4.742843,-9.305344,5.387536,-8.137592,4.059134,-4.447947,1.027979,-9.411961,-2.477838,-8.595701,7.321987,-0.263932,5.473259,6.223833,1.280014,2.858919,-6.962154,-7.243821,6.745452,-8.396169,7.890036,-0.531724,8.137825,0.677022,-5.064408,6.383608,1.743212,2.877575],[1.238603,3.746435,3.382727,2.671396,-3.869738,0.507223,8.612340,-7.999465,7.030065,4.650864,1.760435,-2.381631,-6.193556,1.429796,8.987543,-9.759304,-6.012002,-6.936697,7.748031,1.828095,4.249436,9.911111,6.440774,5.110468,-3.734537,7.415037,-4.697107,-4.634509],[7.693298,-2.395129,-9.094351,4.216475,-1.351917,-1.253668,-8.238457,8.027668,-3.918102,-4.141252,9.420106,-9.343983,-4.238932,5.865454,-2.858259,-3.642573,-9.520615,-8.565487,0.323833,2.756160,0.776602,0.448623,9.202952,-8.403565,-9.185475,8.940418,-3.793473,8.789257]], dtype = "float32")#candidate|242|(5, 28)|const|float32
bop_243 = relay.floor_mod(uop_232.astype('float64'), relay.reshape(const_242.astype('float64'), relay.shape_of(uop_232))) # shape=(5, 28)
bop_246 = relay.floor_mod(uop_234.astype('float64'), relay.reshape(const_242.astype('float64'), relay.shape_of(uop_234))) # shape=(5, 28)
output = relay.Tuple([call_217,call_220,const_221,call_235,uop_237,bop_243,])
output2 = relay.Tuple([call_218,call_222,const_221,call_236,uop_239,bop_246,])
func_249 = relay.Function([], output)
mod['func_249'] = func_249
mod = relay.transform.InferType()(mod)
mutated_mod['func_249'] = func_249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_249_call = mutated_mod.get_global_var('func_249')
call_250 = func_249_call()
output = call_250
func_251 = relay.Function([], output)
mutated_mod['func_251'] = func_251
mutated_mod = relay.transform.InferType()(mutated_mod)
var_297 = relay.var("var_297", dtype = "float32", shape = (14, 2, 9))#candidate|297|(14, 2, 9)|var|float32
var_298 = relay.var("var_298", dtype = "float32", shape = (14, 2, 9))#candidate|298|(14, 2, 9)|var|float32
bop_299 = relay.power(var_297.astype('float32'), relay.reshape(var_298.astype('float32'), relay.shape_of(var_297))) # shape=(14, 2, 9)
uop_303 = relay.erf(var_298.astype('float32')) # shape=(14, 2, 9)
uop_312 = relay.log(uop_303.astype('float64')) # shape=(14, 2, 9)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
var_321 = relay.var("var_321", dtype = "float32", shape = (108,))#candidate|321|(108,)|var|float32
var_322 = relay.var("var_322", dtype = "float64", shape = (140,))#candidate|322|(140,)|var|float64
call_320 = relay.TupleGetItem(func_212_call(relay.reshape(var_321.astype('float32'), [9, 6, 2]), relay.reshape(var_322.astype('float64'), [5, 28]), ), 1)
call_323 = relay.TupleGetItem(func_215_call(relay.reshape(var_321.astype('float32'), [9, 6, 2]), relay.reshape(var_322.astype('float64'), [5, 28]), ), 1)
uop_324 = relay.sqrt(uop_303.astype('float64')) # shape=(14, 2, 9)
func_158_call = mod.get_global_var('func_158')
func_161_call = mutated_mod.get_global_var('func_161')
call_328 = relay.TupleGetItem(func_158_call(relay.reshape(var_322.astype('float64'), [14, 2, 5])), 0)
call_329 = relay.TupleGetItem(func_161_call(relay.reshape(var_322.astype('float64'), [14, 2, 5])), 0)
func_249_call = mod.get_global_var('func_249')
func_251_call = mutated_mod.get_global_var('func_251')
call_338 = relay.TupleGetItem(func_249_call(), 3)
call_339 = relay.TupleGetItem(func_251_call(), 3)
output = relay.Tuple([bop_299,uop_312,call_320,var_321,var_322,uop_324,call_328,call_338,])
output2 = relay.Tuple([bop_299,uop_312,call_323,var_321,var_322,uop_324,call_329,call_339,])
func_349 = relay.Function([var_297,var_298,var_321,var_322,], output)
mod['func_349'] = func_349
mod = relay.transform.InferType()(mod)
mutated_mod['func_349'] = func_349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_349_call = mutated_mod.get_global_var('func_349')
var_351 = relay.var("var_351", dtype = "float32", shape = (14, 2, 9))#candidate|351|(14, 2, 9)|var|float32
var_352 = relay.var("var_352", dtype = "float32", shape = (14, 2, 9))#candidate|352|(14, 2, 9)|var|float32
var_353 = relay.var("var_353", dtype = "float32", shape = (108,))#candidate|353|(108,)|var|float32
var_354 = relay.var("var_354", dtype = "float64", shape = (140,))#candidate|354|(140,)|var|float64
call_350 = func_349_call(var_351,var_352,var_353,var_354,)
output = call_350
func_355 = relay.Function([var_351,var_352,var_353,var_354,], output)
mutated_mod['func_355'] = func_355
mutated_mod = relay.transform.InferType()(mutated_mod)
var_368 = relay.var("var_368", dtype = "uint8", shape = ())#candidate|368|()|var|uint8
const_369 = relay.const([[[9,9,-3,3],[-7,4,1,-6],[7,-3,-8,5],[-6,-1,-2,-10],[-10,-10,-6,-4],[10,-7,-4,-1],[-6,-3,7,-4],[-5,-4,10,7],[-5,-1,-9,-3],[7,-2,-7,-3],[1,7,1,3],[-4,4,-2,-4],[-7,-9,-3,7],[-4,-10,-4,-4],[-8,3,10,-7],[4,10,2,5]],[[2,6,-6,-5],[6,3,-8,-6],[-6,6,-6,4],[-4,-8,-10,-6],[6,-8,-8,7],[8,-3,5,-3],[-8,-10,-1,6],[1,-4,6,-3],[-3,-7,4,3],[3,8,-7,2],[-1,-2,7,10],[2,8,3,2],[-4,6,-4,2],[7,7,3,9],[-2,-6,9,-6],[9,10,-7,7]],[[3,1,-2,-7],[3,3,3,-9],[3,5,-1,-4],[9,2,6,9],[-3,-9,3,4],[-1,-3,-10,-1],[-8,-4,1,9],[2,6,-3,9],[5,-2,7,-6],[4,-3,2,7],[4,8,1,-3],[-9,3,4,-9],[-2,-9,9,-7],[7,-7,-6,10],[6,-5,-5,10],[-9,-7,4,4]]], dtype = "uint8")#candidate|369|(3, 16, 4)|const|uint8
bop_370 = relay.bitwise_xor(var_368.astype('uint8'), const_369.astype('uint8')) # shape=(3, 16, 4)
func_249_call = mod.get_global_var('func_249')
func_251_call = mutated_mod.get_global_var('func_251')
call_377 = relay.TupleGetItem(func_249_call(), 1)
call_378 = relay.TupleGetItem(func_251_call(), 1)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_383 = func_121_call()
call_384 = func_121_call()
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
call_389 = relay.TupleGetItem(func_212_call(relay.reshape(call_383.astype('float32'), [9, 6, 2]), relay.reshape(call_377.astype('float64'), [5, 28]), ), 2)
call_390 = relay.TupleGetItem(func_215_call(relay.reshape(call_383.astype('float32'), [9, 6, 2]), relay.reshape(call_377.astype('float64'), [5, 28]), ), 2)
output = relay.Tuple([bop_370,call_377,call_383,call_389,])
output2 = relay.Tuple([bop_370,call_378,call_384,call_390,])
func_391 = relay.Function([var_368,], output)
mod['func_391'] = func_391
mod = relay.transform.InferType()(mod)
mutated_mod['func_391'] = func_391
mutated_mod = relay.transform.InferType()(mutated_mod)
var_392 = relay.var("var_392", dtype = "uint8", shape = ())#candidate|392|()|var|uint8
func_391_call = mutated_mod.get_global_var('func_391')
call_393 = func_391_call(var_392)
output = call_393
func_394 = relay.Function([var_392], output)
mutated_mod['func_394'] = func_394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_420 = func_121_call()
call_421 = func_121_call()
var_422 = relay.var("var_422", dtype = "float32", shape = (9, 6, 2))#candidate|422|(9, 6, 2)|var|float32
bop_423 = relay.right_shift(call_420.astype('int32'), relay.reshape(var_422.astype('int32'), relay.shape_of(call_420))) # shape=(9, 6, 2)
bop_426 = relay.right_shift(call_421.astype('int32'), relay.reshape(var_422.astype('int32'), relay.shape_of(call_421))) # shape=(9, 6, 2)
var_429 = relay.var("var_429", dtype = "float32", shape = (9, 6, 2))#candidate|429|(9, 6, 2)|var|float32
bop_430 = relay.left_shift(call_420.astype('int8'), relay.reshape(var_429.astype('int8'), relay.shape_of(call_420))) # shape=(9, 6, 2)
bop_433 = relay.left_shift(call_421.astype('int8'), relay.reshape(var_429.astype('int8'), relay.shape_of(call_421))) # shape=(9, 6, 2)
func_349_call = mod.get_global_var('func_349')
func_355_call = mutated_mod.get_global_var('func_355')
var_439 = relay.var("var_439", dtype = "float32", shape = (1, 252))#candidate|439|(1, 252)|var|float32
const_440 = relay.const([2.521315,-2.332600,-5.754483,-5.179878,-6.782135,1.689377,-8.131905,-7.779373,-9.677730,-5.960659,-0.022147,-2.569642,-2.556956,1.860393,-2.157681,-7.735377,5.332024,4.089810,-1.228250,4.745921,-1.018856,9.435277,-1.133441,-6.594478,-9.591492,3.212783,7.882400,-6.604007,2.984357,8.882976,-0.325367,-1.714922,-2.724262,8.595879,2.546826,6.251630,2.636421,9.070036,-9.698435,4.480649,-7.286693,8.348325,-4.335824,-2.166056,6.331257,9.807396,5.249585,-6.379021,6.269124,-5.958989,-4.491602,9.572458,-3.697558,7.535935,-9.224730,-0.136182,0.355155,-3.578185,1.270416,-8.695898,-5.701126,-6.246382,0.392609,1.727992,-3.471414,1.640197,4.462273,-3.062908,6.778945,-6.944770,-6.868314,3.005257,9.027697,6.895620,-9.844389,9.535577,3.945660,-5.463193,-3.890459,-2.670636,-9.251652,-5.969007,-8.271375,1.911060,-7.557695,7.177396,-5.780426,4.525232,5.631678,-0.903362,-3.699794,-7.631897,9.907677,-8.815549,8.380210,-9.693716,-3.650476,5.751217,-9.855036,6.248175,8.903340,6.369625,8.124024,7.384327,-2.115898,-3.823359,1.409987,-9.163470,6.862690,7.720836,4.712961,-8.547337,-6.075520,-8.814376,7.211800,1.690718,7.822046,-1.794748,6.965718,7.738053,-5.864023,-9.064280,-5.048923,-6.182697,8.267945,-6.864083,-3.974296,8.846362,8.855619,1.286417,7.413984,6.360852,1.697190,4.507806,3.184132,-2.899754,-3.700026,0.445891,-3.160942,-9.159729], dtype = "float64")#candidate|440|(140,)|const|float64
call_438 = relay.TupleGetItem(func_349_call(relay.reshape(var_439.astype('float32'), [14, 2, 9]), relay.reshape(var_439.astype('float32'), [14, 2, 9]), relay.reshape(var_422.astype('float32'), [108,]), relay.reshape(const_440.astype('float64'), [140,]), ), 4)
call_441 = relay.TupleGetItem(func_355_call(relay.reshape(var_439.astype('float32'), [14, 2, 9]), relay.reshape(var_439.astype('float32'), [14, 2, 9]), relay.reshape(var_422.astype('float32'), [108,]), relay.reshape(const_440.astype('float64'), [140,]), ), 4)
output = relay.Tuple([bop_423,bop_430,call_438,var_439,const_440,])
output2 = relay.Tuple([bop_426,bop_433,call_441,var_439,const_440,])
func_450 = relay.Function([var_422,var_429,var_439,], output)
mod['func_450'] = func_450
mod = relay.transform.InferType()(mod)
mutated_mod['func_450'] = func_450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_450_call = mutated_mod.get_global_var('func_450')
var_452 = relay.var("var_452", dtype = "float32", shape = (9, 6, 2))#candidate|452|(9, 6, 2)|var|float32
var_453 = relay.var("var_453", dtype = "float32", shape = (9, 6, 2))#candidate|453|(9, 6, 2)|var|float32
var_454 = relay.var("var_454", dtype = "float32", shape = (1, 252))#candidate|454|(1, 252)|var|float32
call_451 = func_450_call(var_452,var_453,var_454,)
output = call_451
func_455 = relay.Function([var_452,var_453,var_454,], output)
mutated_mod['func_455'] = func_455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_249_call = mod.get_global_var('func_249')
func_251_call = mutated_mod.get_global_var('func_251')
call_493 = relay.TupleGetItem(func_249_call(), 3)
call_494 = relay.TupleGetItem(func_251_call(), 3)
output = relay.Tuple([call_493,])
output2 = relay.Tuple([call_494,])
func_501 = relay.Function([], output)
mod['func_501'] = func_501
mod = relay.transform.InferType()(mod)
mutated_mod['func_501'] = func_501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_501_call = mutated_mod.get_global_var('func_501')
call_502 = func_501_call()
output = call_502
func_503 = relay.Function([], output)
mutated_mod['func_503'] = func_503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_543 = relay.TupleGetItem(func_501_call(), 0)
call_544 = relay.TupleGetItem(func_503_call(), 0)
output = relay.Tuple([call_543,])
output2 = relay.Tuple([call_544,])
func_545 = relay.Function([], output)
mod['func_545'] = func_545
mod = relay.transform.InferType()(mod)
output = func_545()
func_546 = relay.Function([], output)
mutated_mod['func_546'] = func_546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_564 = relay.TupleGetItem(func_545_call(), 0)
call_565 = relay.TupleGetItem(func_546_call(), 0)
uop_566 = relay.sigmoid(call_564.astype('float32')) # shape=(9, 6, 2)
uop_568 = relay.sigmoid(call_565.astype('float32')) # shape=(9, 6, 2)
uop_571 = relay.log2(call_564.astype('float32')) # shape=(9, 6, 2)
uop_573 = relay.log2(call_565.astype('float32')) # shape=(9, 6, 2)
output = relay.Tuple([uop_566,uop_571,])
output2 = relay.Tuple([uop_568,uop_573,])
func_580 = relay.Function([], output)
mod['func_580'] = func_580
mod = relay.transform.InferType()(mod)
mutated_mod['func_580'] = func_580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mutated_mod.get_global_var('func_580')
call_581 = func_580_call()
output = call_581
func_582 = relay.Function([], output)
mutated_mod['func_582'] = func_582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_591 = relay.TupleGetItem(func_545_call(), 0)
call_592 = relay.TupleGetItem(func_546_call(), 0)
var_593 = relay.var("var_593", dtype = "int8", shape = (9, 6, 2))#candidate|593|(9, 6, 2)|var|int8
bop_594 = relay.equal(call_591.astype('bool'), relay.reshape(var_593.astype('bool'), relay.shape_of(call_591))) # shape=(9, 6, 2)
bop_597 = relay.equal(call_592.astype('bool'), relay.reshape(var_593.astype('bool'), relay.shape_of(call_592))) # shape=(9, 6, 2)
output = relay.Tuple([bop_594,])
output2 = relay.Tuple([bop_597,])
func_614 = relay.Function([var_593,], output)
mod['func_614'] = func_614
mod = relay.transform.InferType()(mod)
mutated_mod['func_614'] = func_614
mutated_mod = relay.transform.InferType()(mutated_mod)
var_615 = relay.var("var_615", dtype = "int8", shape = (9, 6, 2))#candidate|615|(9, 6, 2)|var|int8
func_614_call = mutated_mod.get_global_var('func_614')
call_616 = func_614_call(var_615)
output = call_616
func_617 = relay.Function([var_615], output)
mutated_mod['func_617'] = func_617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_624 = func_121_call()
call_625 = func_121_call()
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_633 = relay.TupleGetItem(func_545_call(), 0)
call_634 = relay.TupleGetItem(func_546_call(), 0)
bop_638 = relay.bitwise_or(call_633.astype('uint32'), relay.reshape(call_624.astype('uint32'), relay.shape_of(call_633))) # shape=(9, 6, 2)
bop_641 = relay.bitwise_or(call_634.astype('uint32'), relay.reshape(call_625.astype('uint32'), relay.shape_of(call_634))) # shape=(9, 6, 2)
output = bop_638
output2 = bop_641
func_646 = relay.Function([], output)
mod['func_646'] = func_646
mod = relay.transform.InferType()(mod)
mutated_mod['func_646'] = func_646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_646_call = mutated_mod.get_global_var('func_646')
call_647 = func_646_call()
output = call_647
func_648 = relay.Function([], output)
mutated_mod['func_648'] = func_648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_657 = relay.TupleGetItem(func_545_call(), 0)
call_658 = relay.TupleGetItem(func_546_call(), 0)
func_646_call = mod.get_global_var('func_646')
func_648_call = mutated_mod.get_global_var('func_648')
call_676 = func_646_call()
call_677 = func_646_call()
output = relay.Tuple([call_657,call_676,])
output2 = relay.Tuple([call_658,call_677,])
func_694 = relay.Function([], output)
mod['func_694'] = func_694
mod = relay.transform.InferType()(mod)
output = func_694()
func_695 = relay.Function([], output)
mutated_mod['func_695'] = func_695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_751 = relay.TupleGetItem(func_580_call(), 1)
call_752 = relay.TupleGetItem(func_582_call(), 1)
output = call_751
output2 = call_752
func_753 = relay.Function([], output)
mod['func_753'] = func_753
mod = relay.transform.InferType()(mod)
mutated_mod['func_753'] = func_753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mutated_mod.get_global_var('func_753')
call_754 = func_753_call()
output = call_754
func_755 = relay.Function([], output)
mutated_mod['func_755'] = func_755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_762 = func_121_call()
call_763 = func_121_call()
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_765 = func_121_call()
call_766 = func_121_call()
output = relay.Tuple([call_762,call_765,])
output2 = relay.Tuple([call_763,call_766,])
func_772 = relay.Function([], output)
mod['func_772'] = func_772
mod = relay.transform.InferType()(mod)
output = func_772()
func_773 = relay.Function([], output)
mutated_mod['func_773'] = func_773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_792 = func_121_call()
call_793 = func_121_call()
func_694_call = mod.get_global_var('func_694')
func_695_call = mutated_mod.get_global_var('func_695')
call_815 = relay.TupleGetItem(func_694_call(), 0)
call_816 = relay.TupleGetItem(func_695_call(), 0)
output = relay.Tuple([call_792,call_815,])
output2 = relay.Tuple([call_793,call_816,])
func_818 = relay.Function([], output)
mod['func_818'] = func_818
mod = relay.transform.InferType()(mod)
mutated_mod['func_818'] = func_818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_818_call = mutated_mod.get_global_var('func_818')
call_819 = func_818_call()
output = call_819
func_820 = relay.Function([], output)
mutated_mod['func_820'] = func_820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_850 = relay.TupleGetItem(func_580_call(), 1)
call_851 = relay.TupleGetItem(func_582_call(), 1)
func_450_call = mod.get_global_var('func_450')
func_455_call = mutated_mod.get_global_var('func_455')
var_853 = relay.var("var_853", dtype = "float32", shape = (252,))#candidate|853|(252,)|var|float32
call_852 = relay.TupleGetItem(func_450_call(relay.reshape(call_850.astype('float32'), [9, 6, 2]), relay.reshape(call_850.astype('float32'), [9, 6, 2]), relay.reshape(var_853.astype('float32'), [1, 252]), ), 0)
call_854 = relay.TupleGetItem(func_455_call(relay.reshape(call_850.astype('float32'), [9, 6, 2]), relay.reshape(call_850.astype('float32'), [9, 6, 2]), relay.reshape(var_853.astype('float32'), [1, 252]), ), 0)
func_391_call = mod.get_global_var('func_391')
func_394_call = mutated_mod.get_global_var('func_394')
const_856 = relay.const(5, dtype = "uint8")#candidate|856|()|const|uint8
call_855 = relay.TupleGetItem(func_391_call(relay.reshape(const_856.astype('uint8'), [])), 3)
call_857 = relay.TupleGetItem(func_394_call(relay.reshape(const_856.astype('uint8'), [])), 3)
output = relay.Tuple([call_850,call_852,var_853,call_855,const_856,])
output2 = relay.Tuple([call_851,call_854,var_853,call_857,const_856,])
func_863 = relay.Function([var_853,], output)
mod['func_863'] = func_863
mod = relay.transform.InferType()(mod)
mutated_mod['func_863'] = func_863
mutated_mod = relay.transform.InferType()(mutated_mod)
var_864 = relay.var("var_864", dtype = "float32", shape = (252,))#candidate|864|(252,)|var|float32
func_863_call = mutated_mod.get_global_var('func_863')
call_865 = func_863_call(var_864)
output = call_865
func_866 = relay.Function([var_864], output)
mutated_mod['func_866'] = func_866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_772_call = mod.get_global_var('func_772')
func_773_call = mutated_mod.get_global_var('func_773')
call_925 = relay.TupleGetItem(func_772_call(), 1)
call_926 = relay.TupleGetItem(func_773_call(), 1)
func_818_call = mod.get_global_var('func_818')
func_820_call = mutated_mod.get_global_var('func_820')
call_929 = relay.TupleGetItem(func_818_call(), 1)
call_930 = relay.TupleGetItem(func_820_call(), 1)
uop_934 = relay.log(call_925.astype('float64')) # shape=(9, 6, 2)
uop_936 = relay.log(call_926.astype('float64')) # shape=(9, 6, 2)
output = relay.Tuple([call_929,uop_934,])
output2 = relay.Tuple([call_930,uop_936,])
func_937 = relay.Function([], output)
mod['func_937'] = func_937
mod = relay.transform.InferType()(mod)
mutated_mod['func_937'] = func_937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_937_call = mutated_mod.get_global_var('func_937')
call_938 = func_937_call()
output = call_938
func_939 = relay.Function([], output)
mutated_mod['func_939'] = func_939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_965 = func_753_call()
call_966 = func_753_call()
func_349_call = mod.get_global_var('func_349')
func_355_call = mutated_mod.get_global_var('func_355')
const_968 = relay.const([-4.571134,6.809467,8.161867,1.682237,2.239741,-2.426413,5.553813,-0.041161,6.010509,6.480430,-3.419316,-4.405336,9.561946,5.900457,6.040273,5.623116,6.506115,6.112804,-1.293560,-9.784367,-5.304625,2.012157,1.966265,-2.219758,5.586036,9.015983,-4.124950,1.787051,-0.439538,-8.303239,3.902145,4.558623,-3.352539,1.072656,-9.890292,3.151642,-0.135114,-5.110487,-5.090080,6.140327,-0.043949,3.206913,-4.294565,-2.743947,9.195590,-3.774094,-5.726607,-9.259744,5.367427,8.451942,7.769052,-7.699325,2.320842,-7.828553,-4.108558,8.869072,-7.904254,5.332667,5.525391,1.468127,-1.742377,-0.739785,-1.141209,1.194159,-7.353012,8.873829,9.811074,-8.563978,-2.959746,2.043816,-0.759836,6.997124,1.626921,8.609510,-4.158219,-3.874612,-5.269640,4.733506,5.843468,-5.198381,-5.373335,4.887005,-5.984926,-7.809926,-3.209931,4.425040,6.403793,-6.100627,5.138214,6.055666,-5.233747,-8.295512,-7.031902,7.996209,-6.961967,-3.485889,3.538392,9.687217,2.151536,-4.825095,9.051296,-2.039397,-0.466629,2.799671,-4.056213,4.596661,-1.138268,5.290459,-4.872043,-9.632512,0.754963,1.574143,5.712663,-1.065569,-1.498404,-6.340633,-1.865818,-4.149524,6.164411,-5.137918,5.574274,4.154607,0.122882,-8.175329,6.553423,-2.433037,5.827918,-9.325915,-2.770853,4.369114,2.759066,-3.500883,-3.235208,4.363492,6.690785,7.146044,1.114631,-3.330939,-9.590553,-9.135791,-5.137585,-9.552341,-3.867225,-4.636525,9.678296,-7.586905,7.259169,-7.632554,3.116854,-9.126632,5.798979,0.002235,-2.465015,1.249213,8.604966,-8.866600,-5.566887,5.935734,1.592828,-7.469758,-2.361149,-9.324026,4.417230,2.358746,-2.142107,4.567923,-5.967661,-3.830884,2.295286,2.538494,-2.938332,-9.968590,-6.538997,6.113759,7.934581,-8.498124,-8.029084,4.305294,5.033802,2.556076,-2.571405,1.020750,2.568899,0.702258,6.536617,8.621306,8.572363,-9.265150,-7.288806,3.915609,2.104463,8.057756,-7.731832,-4.245444,2.244469,6.026729,-4.907404,-0.221031,0.802991,-8.890251,-1.060561,-8.073420,0.551856,9.454596,-3.901419,6.935072,-0.221511,-5.445601,-3.707225,-7.469142,-6.943738,5.639552,-0.683411,-0.614983,-9.764472,-1.303210,0.254957,-0.718819,-9.533954,-9.150076,-0.186517,-1.060603,-9.793018,-0.393283,9.680456,-4.880084,-2.091062,0.360534,-0.157323,-9.917636,-4.502401,6.102632,1.570531,2.333720,-4.189827,0.494429,9.158782,9.114204,-1.597317,-6.952856,1.981797,3.447545,4.011485,-8.024725,-5.478531,-5.702406,-2.314339,-8.597238,9.814874,7.675259,0.114061,-7.518424], dtype = "float32")#candidate|968|(252,)|const|float32
const_969 = relay.const([-0.375883,8.373238,6.880365,9.385776,-5.717847,-1.017063,9.365418,7.648511,-8.372798,-5.640881,4.225150,6.618411,2.012702,-9.695918,-9.640512,9.935865,-9.621350,-6.554154,-2.949566,8.048193,8.484706,9.436502,4.940243,7.837074,9.048935,2.573213,9.429428,7.263064,7.775260,8.661966,3.302551,-0.916386,9.379482,4.215119,-3.584382,7.590289,-9.334054,-3.240518,5.853900,-8.280920,-7.080575,3.357652,-6.331622,-8.259322,-2.369012,8.241204,-6.606501,9.317300,6.087562,6.026205,7.798456,3.252214,-5.128127,8.995849,-9.297981,-2.733632,-9.242427,-2.552655,-4.859436,-0.294732,-0.996760,-8.945181,6.281399,2.801285,-3.064806,-5.319149,9.709263,-5.999352,9.999078,0.601865,6.022898,-7.896185,5.139326,-1.176557,5.445687,-7.047412,-9.739011,-6.494957,-8.536463,-5.397508,2.786230,-4.525287,0.851494,-0.154490,9.802933,-6.851776,9.819183,-7.510178,2.067265,2.648788,3.036744,-9.649202,-5.786035,8.673668,-8.149618,-8.364587,-6.496202,-4.893612,2.547636,-0.057875,-2.178815,2.438645,-7.947239,-8.095238,-1.801985,-9.160004,6.263040,8.379920,-2.777819,-9.201238,6.328172,-8.807841,-3.540437,7.454461,1.190981,-3.314329,-3.282714,4.091638,6.885546,-4.277358,7.653758,5.554527,6.986835,8.197574,8.880738,4.349171,-8.580287,-1.432284,-1.842439,-2.164022,4.072442,-7.450947,-0.589584,-3.490720,9.468194,7.942035,-0.408376,-5.131473,4.890459,7.568817], dtype = "float64")#candidate|969|(140,)|const|float64
call_967 = relay.TupleGetItem(func_349_call(relay.reshape(const_968.astype('float32'), [14, 2, 9]), relay.reshape(const_968.astype('float32'), [14, 2, 9]), relay.reshape(call_965.astype('float32'), [108,]), relay.reshape(const_969.astype('float64'), [140,]), ), 6)
call_970 = relay.TupleGetItem(func_355_call(relay.reshape(const_968.astype('float32'), [14, 2, 9]), relay.reshape(const_968.astype('float32'), [14, 2, 9]), relay.reshape(call_965.astype('float32'), [108,]), relay.reshape(const_969.astype('float64'), [140,]), ), 6)
output = relay.Tuple([call_965,call_967,const_968,const_969,])
output2 = relay.Tuple([call_966,call_970,const_968,const_969,])
func_971 = relay.Function([], output)
mod['func_971'] = func_971
mod = relay.transform.InferType()(mod)
mutated_mod['func_971'] = func_971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mutated_mod.get_global_var('func_971')
call_972 = func_971_call()
output = call_972
func_973 = relay.Function([], output)
mutated_mod['func_973'] = func_973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_1018 = relay.TupleGetItem(func_545_call(), 0)
call_1019 = relay.TupleGetItem(func_546_call(), 0)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
var_1027 = relay.var("var_1027", dtype = "float64", shape = (140,))#candidate|1027|(140,)|var|float64
call_1026 = relay.TupleGetItem(func_212_call(relay.reshape(call_1018.astype('float32'), [9, 6, 2]), relay.reshape(var_1027.astype('float64'), [5, 28]), ), 4)
call_1028 = relay.TupleGetItem(func_215_call(relay.reshape(call_1018.astype('float32'), [9, 6, 2]), relay.reshape(var_1027.astype('float64'), [5, 28]), ), 4)
output = relay.Tuple([call_1018,call_1026,var_1027,])
output2 = relay.Tuple([call_1019,call_1028,var_1027,])
func_1041 = relay.Function([var_1027,], output)
mod['func_1041'] = func_1041
mod = relay.transform.InferType()(mod)
mutated_mod['func_1041'] = func_1041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1042 = relay.var("var_1042", dtype = "float64", shape = (140,))#candidate|1042|(140,)|var|float64
func_1041_call = mutated_mod.get_global_var('func_1041')
call_1043 = func_1041_call(var_1042)
output = call_1043
func_1044 = relay.Function([var_1042], output)
mutated_mod['func_1044'] = func_1044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_646_call = mod.get_global_var('func_646')
func_648_call = mutated_mod.get_global_var('func_648')
call_1060 = func_646_call()
call_1061 = func_646_call()
uop_1071 = relay.cosh(call_1060.astype('float64')) # shape=(9, 6, 2)
uop_1073 = relay.cosh(call_1061.astype('float64')) # shape=(9, 6, 2)
output = relay.Tuple([uop_1071,])
output2 = relay.Tuple([uop_1073,])
func_1079 = relay.Function([], output)
mod['func_1079'] = func_1079
mod = relay.transform.InferType()(mod)
output = func_1079()
func_1080 = relay.Function([], output)
mutated_mod['func_1080'] = func_1080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_818_call = mod.get_global_var('func_818')
func_820_call = mutated_mod.get_global_var('func_820')
call_1115 = relay.TupleGetItem(func_818_call(), 1)
call_1116 = relay.TupleGetItem(func_820_call(), 1)
uop_1119 = relay.log10(call_1115.astype('float32')) # shape=(9, 6, 2)
uop_1121 = relay.log10(call_1116.astype('float32')) # shape=(9, 6, 2)
uop_1122 = relay.exp(call_1115.astype('float64')) # shape=(9, 6, 2)
uop_1124 = relay.exp(call_1116.astype('float64')) # shape=(9, 6, 2)
func_158_call = mod.get_global_var('func_158')
func_161_call = mutated_mod.get_global_var('func_161')
const_1136 = relay.const([[-7.559104,8.277091,-3.368596,-4.369556,8.876987,-6.802990,5.873158,-3.308148,6.672309,2.195487,-2.256720,-6.496085,-7.423996,9.273394,1.381908,-4.872760,-4.854833,-1.532068,-6.544976,-5.481746,-1.015827,3.080881,5.688222,-7.551691,7.444752,8.981956,-1.970507,1.636496,2.207670,8.145221,7.464748,-3.506265,7.023857,-7.111947,-7.676465,3.370139,-8.522295,-8.423500,-6.357380,-2.536512,-1.476837,1.036360,-9.563811,-7.334689,2.934663,-5.194393,5.707528,-4.200578,3.921202,-5.885659,7.383452,9.743531,-5.860719,3.400085,-1.518944,-7.570675,-7.360296,2.468370,-5.040041,-4.410035,7.244784,7.655446,-7.629595,2.575615,-9.822110,1.593746,-8.377165,9.215099,-6.414411,3.674399,4.648780,9.033051,-7.269351,-9.090373,-0.461429,-6.612980,9.372312,1.909647,-8.322397,4.167115,-7.455490,-6.349349,4.485431,-1.244919,1.227474,-9.415685,5.913211,-4.774986,-3.327095,5.647926,3.206782,-5.262338,4.671815,-2.564418,4.873994,-0.513407,-5.922485,-6.705766,1.754366,7.235143,-0.889440,7.413627,-6.994049,6.063595,-0.703106,6.237161,3.809625,-5.527342,9.367596,-6.416276,-0.326787,3.224944,2.182113,6.771802,-8.801464,4.725215,-4.888801,-6.242687,-4.900190,-8.956293,-1.105708,5.582365,6.360669,-0.406440,-5.462273,6.621816,-2.799377,-9.098859,-8.577699,-4.671546,-7.373140,-0.199942,-7.123559,7.723202,-2.572415,5.926699,-2.391054,-3.972926,-3.148880,-4.496524]], dtype = "float64")#candidate|1136|(1, 140)|const|float64
call_1135 = relay.TupleGetItem(func_158_call(relay.reshape(const_1136.astype('float64'), [14, 2, 5])), 0)
call_1137 = relay.TupleGetItem(func_161_call(relay.reshape(const_1136.astype('float64'), [14, 2, 5])), 0)
output = relay.Tuple([uop_1119,uop_1122,call_1135,const_1136,])
output2 = relay.Tuple([uop_1121,uop_1124,call_1137,const_1136,])
func_1149 = relay.Function([], output)
mod['func_1149'] = func_1149
mod = relay.transform.InferType()(mod)
output = func_1149()
func_1150 = relay.Function([], output)
mutated_mod['func_1150'] = func_1150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_1167 = relay.TupleGetItem(func_937_call(), 1)
call_1168 = relay.TupleGetItem(func_939_call(), 1)
output = call_1167
output2 = call_1168
func_1178 = relay.Function([], output)
mod['func_1178'] = func_1178
mod = relay.transform.InferType()(mod)
mutated_mod['func_1178'] = func_1178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mutated_mod.get_global_var('func_1178')
call_1179 = func_1178_call()
output = call_1179
func_1180 = relay.Function([], output)
mutated_mod['func_1180'] = func_1180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_1189 = relay.TupleGetItem(func_580_call(), 0)
call_1190 = relay.TupleGetItem(func_582_call(), 0)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_1209 = relay.TupleGetItem(func_580_call(), 1)
call_1210 = relay.TupleGetItem(func_582_call(), 1)
func_863_call = mod.get_global_var('func_863')
func_866_call = mutated_mod.get_global_var('func_866')
const_1212 = relay.const([2.456544,8.152493,-9.480209,5.982961,-2.006287,-2.207958,-4.917433,1.203664,-5.572900,-7.723240,-2.915845,6.688313,-4.306944,6.570796,-0.307682,-7.037255,6.384733,4.614855,9.480515,0.736390,-4.054830,2.934955,-3.688685,-4.437896,1.035978,8.899767,9.503783,0.371291,7.858281,5.308064,5.730767,6.079206,-5.835340,6.502552,5.216250,3.153242,-4.071766,-9.569768,6.526702,2.883024,-8.403905,-1.329284,3.387225,9.256794,7.543860,-4.354921,7.594907,7.983514,-4.747905,2.767647,7.243060,8.175842,1.367981,-0.279279,6.830032,4.842417,6.334597,2.927513,3.183375,0.257894,-9.074598,-0.772817,0.642184,4.383396,-6.382655,1.382925,3.173414,0.426759,-8.065612,5.512240,7.601310,4.692445,5.649649,2.103467,-2.070598,5.628638,-1.644416,-5.863842,7.351749,-0.550998,-3.304691,6.322835,-8.598046,0.475729,-2.560662,-8.235063,1.063271,-2.217487,9.148846,-3.968921,-9.033663,-1.603647,2.761019,-8.605516,-4.684972,-3.010405,-2.957512,-1.137842,-8.335048,-8.434115,-1.116566,-6.039308,-9.261517,-1.837355,-7.193571,8.362978,-3.669507,9.207734,-6.680487,-5.396658,-4.834962,-5.795709,-7.270182,-1.786482,-3.411400,-3.439976,5.521934,-2.376357,1.295141,8.354689,5.387894,5.527982,-0.671240,4.965331,-5.540752,0.335213,-4.765553,-3.370370,-4.776116,9.985812,8.830712,-0.542714,-5.230285,-9.971265,2.739301,9.162534,2.745877,6.777776,-9.622726,-8.713270,-8.004154,3.348719,7.271557,-8.089092,-7.408013,-9.628349,7.543827,3.362444,-1.081140,8.614211,2.476602,-1.196569,7.521963,2.266620,3.514503,1.468283,3.945832,-4.758648,-2.245349,6.448325,4.475384,-1.743894,-3.679670,-4.217127,2.774574,-7.053301,9.167414,3.839785,-9.033350,-3.063648,6.800901,-0.900129,-9.934763,9.390791,7.709207,-3.822213,2.613693,1.589508,-9.466664,-5.950789,5.832665,-2.000813,5.590353,-6.510908,-8.067959,3.727731,-9.058968,9.501272,3.863648,0.429663,4.840998,5.276900,-3.909558,-8.758925,-1.528362,-3.749596,9.491846,-0.220824,2.006365,4.590330,3.994446,2.735482,-0.660017,8.984275,9.643220,-8.807108,-1.539886,1.584422,-7.420909,6.024861,-8.053422,-2.594932,-8.678639,8.971185,1.368376,-0.003892,3.453810,-8.420558,-3.882790,6.508516,-2.131626,-6.383175,7.548371,7.625232,3.506441,6.770806,7.231297,0.839118,-1.043389,2.871487,1.662745,9.869141,1.325392,-8.083860,6.244299,6.893242,8.971861,-9.725625,-0.572759,-7.476179,-6.726321,7.057701,-8.826012,6.401763,3.947935,-3.523573,-7.783185,-3.626314,-1.567237,6.791632,-6.167586,0.960758], dtype = "float32")#candidate|1212|(252,)|const|float32
call_1211 = relay.TupleGetItem(func_863_call(relay.reshape(const_1212.astype('float32'), [252,])), 2)
call_1213 = relay.TupleGetItem(func_866_call(relay.reshape(const_1212.astype('float32'), [252,])), 2)
output = relay.Tuple([call_1189,call_1209,call_1211,const_1212,])
output2 = relay.Tuple([call_1190,call_1210,call_1213,const_1212,])
func_1219 = relay.Function([], output)
mod['func_1219'] = func_1219
mod = relay.transform.InferType()(mod)
output = func_1219()
func_1220 = relay.Function([], output)
mutated_mod['func_1220'] = func_1220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_646_call = mod.get_global_var('func_646')
func_648_call = mutated_mod.get_global_var('func_648')
call_1237 = func_646_call()
call_1238 = func_646_call()
output = call_1237
output2 = call_1238
func_1242 = relay.Function([], output)
mod['func_1242'] = func_1242
mod = relay.transform.InferType()(mod)
mutated_mod['func_1242'] = func_1242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1242_call = mutated_mod.get_global_var('func_1242')
call_1243 = func_1242_call()
output = call_1243
func_1244 = relay.Function([], output)
mutated_mod['func_1244'] = func_1244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_1315 = relay.TupleGetItem(func_971_call(), 3)
call_1316 = relay.TupleGetItem(func_973_call(), 3)
func_249_call = mod.get_global_var('func_249')
func_251_call = mutated_mod.get_global_var('func_251')
call_1317 = relay.TupleGetItem(func_249_call(), 2)
call_1318 = relay.TupleGetItem(func_251_call(), 2)
output = relay.Tuple([call_1315,call_1317,])
output2 = relay.Tuple([call_1316,call_1318,])
func_1321 = relay.Function([], output)
mod['func_1321'] = func_1321
mod = relay.transform.InferType()(mod)
mutated_mod['func_1321'] = func_1321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mutated_mod.get_global_var('func_1321')
call_1322 = func_1321_call()
output = call_1322
func_1323 = relay.Function([], output)
mutated_mod['func_1323'] = func_1323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_1349 = func_753_call()
call_1350 = func_753_call()
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_1357 = func_121_call()
call_1358 = func_121_call()
bop_1372 = relay.logical_or(call_1357.astype('bool'), relay.reshape(call_1349.astype('bool'), relay.shape_of(call_1357))) # shape=(9, 6, 2)
bop_1375 = relay.logical_or(call_1358.astype('bool'), relay.reshape(call_1350.astype('bool'), relay.shape_of(call_1358))) # shape=(9, 6, 2)
output = bop_1372
output2 = bop_1375
func_1385 = relay.Function([], output)
mod['func_1385'] = func_1385
mod = relay.transform.InferType()(mod)
mutated_mod['func_1385'] = func_1385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mutated_mod.get_global_var('func_1385')
call_1386 = func_1385_call()
output = call_1386
func_1387 = relay.Function([], output)
mutated_mod['func_1387'] = func_1387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_1445 = relay.TupleGetItem(func_971_call(), 2)
call_1446 = relay.TupleGetItem(func_973_call(), 2)
output = relay.Tuple([call_1445,])
output2 = relay.Tuple([call_1446,])
func_1467 = relay.Function([], output)
mod['func_1467'] = func_1467
mod = relay.transform.InferType()(mod)
output = func_1467()
func_1468 = relay.Function([], output)
mutated_mod['func_1468'] = func_1468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_1482 = func_1178_call()
call_1483 = func_1178_call()
output = relay.Tuple([call_1482,])
output2 = relay.Tuple([call_1483,])
func_1484 = relay.Function([], output)
mod['func_1484'] = func_1484
mod = relay.transform.InferType()(mod)
output = func_1484()
func_1485 = relay.Function([], output)
mutated_mod['func_1485'] = func_1485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_772_call = mod.get_global_var('func_772')
func_773_call = mutated_mod.get_global_var('func_773')
call_1488 = relay.TupleGetItem(func_772_call(), 0)
call_1489 = relay.TupleGetItem(func_773_call(), 0)
var_1490 = relay.var("var_1490", dtype = "float32", shape = (9, 6, 2))#candidate|1490|(9, 6, 2)|var|float32
bop_1491 = relay.maximum(call_1488.astype('int32'), relay.reshape(var_1490.astype('int32'), relay.shape_of(call_1488))) # shape=(9, 6, 2)
bop_1494 = relay.maximum(call_1489.astype('int32'), relay.reshape(var_1490.astype('int32'), relay.shape_of(call_1489))) # shape=(9, 6, 2)
output = bop_1491
output2 = bop_1494
func_1515 = relay.Function([var_1490,], output)
mod['func_1515'] = func_1515
mod = relay.transform.InferType()(mod)
mutated_mod['func_1515'] = func_1515
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1516 = relay.var("var_1516", dtype = "float32", shape = (9, 6, 2))#candidate|1516|(9, 6, 2)|var|float32
func_1515_call = mutated_mod.get_global_var('func_1515')
call_1517 = func_1515_call(var_1516)
output = call_1517
func_1518 = relay.Function([var_1516], output)
mutated_mod['func_1518'] = func_1518
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1528 = relay.var("var_1528", dtype = "float64", shape = (10, 1, 14))#candidate|1528|(10, 1, 14)|var|float64
uop_1529 = relay.atan(var_1528.astype('float64')) # shape=(10, 1, 14)
bop_1533 = relay.equal(var_1528.astype('bool'), relay.reshape(uop_1529.astype('bool'), relay.shape_of(var_1528))) # shape=(10, 1, 14)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_1537 = relay.TupleGetItem(func_937_call(), 1)
call_1538 = relay.TupleGetItem(func_939_call(), 1)
bop_1539 = relay.logical_and(uop_1529.astype('bool'), relay.reshape(var_1528.astype('bool'), relay.shape_of(uop_1529))) # shape=(10, 1, 14)
bop_1546 = relay.logical_or(bop_1539.astype('bool'), relay.reshape(var_1528.astype('bool'), relay.shape_of(bop_1539))) # shape=(10, 1, 14)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_1550 = relay.TupleGetItem(func_971_call(), 0)
call_1551 = relay.TupleGetItem(func_973_call(), 0)
output = relay.Tuple([bop_1533,call_1537,bop_1546,call_1550,])
output2 = relay.Tuple([bop_1533,call_1538,bop_1546,call_1551,])
func_1552 = relay.Function([var_1528,], output)
mod['func_1552'] = func_1552
mod = relay.transform.InferType()(mod)
var_1553 = relay.var("var_1553", dtype = "float64", shape = (10, 1, 14))#candidate|1553|(10, 1, 14)|var|float64
output = func_1552(var_1553)
func_1554 = relay.Function([var_1553], output)
mutated_mod['func_1554'] = func_1554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_772_call = mod.get_global_var('func_772')
func_773_call = mutated_mod.get_global_var('func_773')
call_1556 = relay.TupleGetItem(func_772_call(), 0)
call_1557 = relay.TupleGetItem(func_773_call(), 0)
func_614_call = mod.get_global_var('func_614')
func_617_call = mutated_mod.get_global_var('func_617')
call_1558 = relay.TupleGetItem(func_614_call(relay.reshape(call_1556.astype('int8'), [9, 6, 2])), 0)
call_1559 = relay.TupleGetItem(func_617_call(relay.reshape(call_1556.astype('int8'), [9, 6, 2])), 0)
output = relay.Tuple([call_1556,call_1558,])
output2 = relay.Tuple([call_1557,call_1559,])
func_1564 = relay.Function([], output)
mod['func_1564'] = func_1564
mod = relay.transform.InferType()(mod)
output = func_1564()
func_1565 = relay.Function([], output)
mutated_mod['func_1565'] = func_1565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_646_call = mod.get_global_var('func_646')
func_648_call = mutated_mod.get_global_var('func_648')
call_1660 = func_646_call()
call_1661 = func_646_call()
var_1667 = relay.var("var_1667", dtype = "uint32", shape = (9, 6, 2))#candidate|1667|(9, 6, 2)|var|uint32
bop_1668 = relay.subtract(call_1660.astype('uint32'), relay.reshape(var_1667.astype('uint32'), relay.shape_of(call_1660))) # shape=(9, 6, 2)
bop_1671 = relay.subtract(call_1661.astype('uint32'), relay.reshape(var_1667.astype('uint32'), relay.shape_of(call_1661))) # shape=(9, 6, 2)
output = relay.Tuple([bop_1668,])
output2 = relay.Tuple([bop_1671,])
func_1684 = relay.Function([var_1667,], output)
mod['func_1684'] = func_1684
mod = relay.transform.InferType()(mod)
var_1685 = relay.var("var_1685", dtype = "uint32", shape = (9, 6, 2))#candidate|1685|(9, 6, 2)|var|uint32
output = func_1684(var_1685)
func_1686 = relay.Function([var_1685], output)
mutated_mod['func_1686'] = func_1686
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1745 = relay.var("var_1745", dtype = "int64", shape = (11, 1, 2))#candidate|1745|(11, 1, 2)|var|int64
var_1746 = relay.var("var_1746", dtype = "int64", shape = (11, 11, 2))#candidate|1746|(11, 11, 2)|var|int64
bop_1747 = relay.left_shift(var_1745.astype('int64'), var_1746.astype('int64')) # shape=(11, 11, 2)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_1769 = func_1385_call()
call_1770 = func_1385_call()
output = relay.Tuple([bop_1747,call_1769,])
output2 = relay.Tuple([bop_1747,call_1770,])
func_1781 = relay.Function([var_1745,var_1746,], output)
mod['func_1781'] = func_1781
mod = relay.transform.InferType()(mod)
var_1782 = relay.var("var_1782", dtype = "int64", shape = (11, 1, 2))#candidate|1782|(11, 1, 2)|var|int64
var_1783 = relay.var("var_1783", dtype = "int64", shape = (11, 11, 2))#candidate|1783|(11, 11, 2)|var|int64
output = func_1781(var_1782,var_1783,)
func_1784 = relay.Function([var_1782,var_1783,], output)
mutated_mod['func_1784'] = func_1784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_818_call = mod.get_global_var('func_818')
func_820_call = mutated_mod.get_global_var('func_820')
call_1845 = relay.TupleGetItem(func_818_call(), 1)
call_1846 = relay.TupleGetItem(func_820_call(), 1)
output = call_1845
output2 = call_1846
func_1847 = relay.Function([], output)
mod['func_1847'] = func_1847
mod = relay.transform.InferType()(mod)
output = func_1847()
func_1848 = relay.Function([], output)
mutated_mod['func_1848'] = func_1848
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1874 = relay.var("var_1874", dtype = "bool", shape = (7, 15, 5))#candidate|1874|(7, 15, 5)|var|bool
var_1875 = relay.var("var_1875", dtype = "bool", shape = (7, 15, 5))#candidate|1875|(7, 15, 5)|var|bool
bop_1876 = relay.logical_or(var_1874.astype('bool'), relay.reshape(var_1875.astype('bool'), relay.shape_of(var_1874))) # shape=(7, 15, 5)
output = bop_1876
output2 = bop_1876
func_1891 = relay.Function([var_1874,var_1875,], output)
mod['func_1891'] = func_1891
mod = relay.transform.InferType()(mod)
mutated_mod['func_1891'] = func_1891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mutated_mod.get_global_var('func_1891')
var_1893 = relay.var("var_1893", dtype = "bool", shape = (7, 15, 5))#candidate|1893|(7, 15, 5)|var|bool
var_1894 = relay.var("var_1894", dtype = "bool", shape = (7, 15, 5))#candidate|1894|(7, 15, 5)|var|bool
call_1892 = func_1891_call(var_1893,var_1894,)
output = call_1892
func_1895 = relay.Function([var_1893,var_1894,], output)
mutated_mod['func_1895'] = func_1895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_1900 = relay.TupleGetItem(func_971_call(), 2)
call_1901 = relay.TupleGetItem(func_973_call(), 2)
func_863_call = mod.get_global_var('func_863')
func_866_call = mutated_mod.get_global_var('func_866')
call_1905 = relay.TupleGetItem(func_863_call(relay.reshape(call_1900.astype('float32'), [252,])), 1)
call_1906 = relay.TupleGetItem(func_866_call(relay.reshape(call_1900.astype('float32'), [252,])), 1)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
var_1908 = relay.var("var_1908", dtype = "float64", shape = (140,))#candidate|1908|(140,)|var|float64
call_1907 = relay.TupleGetItem(func_212_call(relay.reshape(call_1905.astype('float32'), [9, 6, 2]), relay.reshape(var_1908.astype('float64'), [5, 28]), ), 4)
call_1909 = relay.TupleGetItem(func_215_call(relay.reshape(call_1905.astype('float32'), [9, 6, 2]), relay.reshape(var_1908.astype('float64'), [5, 28]), ), 4)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_1916 = relay.TupleGetItem(func_501_call(), 0)
call_1917 = relay.TupleGetItem(func_503_call(), 0)
output = relay.Tuple([call_1900,call_1905,call_1907,var_1908,call_1916,])
output2 = relay.Tuple([call_1901,call_1906,call_1909,var_1908,call_1917,])
func_1921 = relay.Function([var_1908,], output)
mod['func_1921'] = func_1921
mod = relay.transform.InferType()(mod)
var_1922 = relay.var("var_1922", dtype = "float64", shape = (140,))#candidate|1922|(140,)|var|float64
output = func_1921(var_1922)
func_1923 = relay.Function([var_1922], output)
mutated_mod['func_1923'] = func_1923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_1949 = func_1385_call()
call_1950 = func_1385_call()
func_1242_call = mod.get_global_var('func_1242')
func_1244_call = mutated_mod.get_global_var('func_1244')
call_1954 = func_1242_call()
call_1955 = func_1242_call()
func_772_call = mod.get_global_var('func_772')
func_773_call = mutated_mod.get_global_var('func_773')
call_1958 = relay.TupleGetItem(func_772_call(), 1)
call_1959 = relay.TupleGetItem(func_773_call(), 1)
func_1891_call = mod.get_global_var('func_1891')
func_1895_call = mutated_mod.get_global_var('func_1895')
var_1965 = relay.var("var_1965", dtype = "bool", shape = (525,))#candidate|1965|(525,)|var|bool
call_1964 = func_1891_call(relay.reshape(var_1965.astype('bool'), [7, 15, 5]), relay.reshape(var_1965.astype('bool'), [7, 15, 5]), )
call_1966 = func_1891_call(relay.reshape(var_1965.astype('bool'), [7, 15, 5]), relay.reshape(var_1965.astype('bool'), [7, 15, 5]), )
output = relay.Tuple([call_1949,call_1954,call_1958,call_1964,var_1965,])
output2 = relay.Tuple([call_1950,call_1955,call_1959,call_1966,var_1965,])
func_1976 = relay.Function([var_1965,], output)
mod['func_1976'] = func_1976
mod = relay.transform.InferType()(mod)
mutated_mod['func_1976'] = func_1976
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1977 = relay.var("var_1977", dtype = "bool", shape = (525,))#candidate|1977|(525,)|var|bool
func_1976_call = mutated_mod.get_global_var('func_1976')
call_1978 = func_1976_call(var_1977)
output = call_1978
func_1979 = relay.Function([var_1977], output)
mutated_mod['func_1979'] = func_1979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_1981 = relay.TupleGetItem(func_937_call(), 0)
call_1982 = relay.TupleGetItem(func_939_call(), 0)
func_391_call = mod.get_global_var('func_391')
func_394_call = mutated_mod.get_global_var('func_394')
const_1991 = relay.const(-6, dtype = "uint8")#candidate|1991|()|const|uint8
call_1990 = relay.TupleGetItem(func_391_call(relay.reshape(const_1991.astype('uint8'), [])), 3)
call_1992 = relay.TupleGetItem(func_394_call(relay.reshape(const_1991.astype('uint8'), [])), 3)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_1999 = func_1178_call()
call_2000 = func_1178_call()
output = relay.Tuple([call_1981,call_1990,const_1991,call_1999,])
output2 = relay.Tuple([call_1982,call_1992,const_1991,call_2000,])
func_2006 = relay.Function([], output)
mod['func_2006'] = func_2006
mod = relay.transform.InferType()(mod)
output = func_2006()
func_2007 = relay.Function([], output)
mutated_mod['func_2007'] = func_2007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2018 = func_1178_call()
call_2019 = func_1178_call()
func_772_call = mod.get_global_var('func_772')
func_773_call = mutated_mod.get_global_var('func_773')
call_2020 = relay.TupleGetItem(func_772_call(), 1)
call_2021 = relay.TupleGetItem(func_773_call(), 1)
var_2023 = relay.var("var_2023", dtype = "float32", shape = (9, 6, 2))#candidate|2023|(9, 6, 2)|var|float32
bop_2024 = relay.minimum(call_2020.astype('uint16'), relay.reshape(var_2023.astype('uint16'), relay.shape_of(call_2020))) # shape=(9, 6, 2)
bop_2027 = relay.minimum(call_2021.astype('uint16'), relay.reshape(var_2023.astype('uint16'), relay.shape_of(call_2021))) # shape=(9, 6, 2)
output = relay.Tuple([call_2018,bop_2024,])
output2 = relay.Tuple([call_2019,bop_2027,])
func_2042 = relay.Function([var_2023,], output)
mod['func_2042'] = func_2042
mod = relay.transform.InferType()(mod)
mutated_mod['func_2042'] = func_2042
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2043 = relay.var("var_2043", dtype = "float32", shape = (9, 6, 2))#candidate|2043|(9, 6, 2)|var|float32
func_2042_call = mutated_mod.get_global_var('func_2042')
call_2044 = func_2042_call(var_2043)
output = call_2044
func_2045 = relay.Function([var_2043], output)
mutated_mod['func_2045'] = func_2045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_2088 = relay.TupleGetItem(func_501_call(), 0)
call_2089 = relay.TupleGetItem(func_503_call(), 0)
output = relay.Tuple([call_2088,])
output2 = relay.Tuple([call_2089,])
func_2099 = relay.Function([], output)
mod['func_2099'] = func_2099
mod = relay.transform.InferType()(mod)
mutated_mod['func_2099'] = func_2099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mutated_mod.get_global_var('func_2099')
call_2100 = func_2099_call()
output = call_2100
func_2101 = relay.Function([], output)
mutated_mod['func_2101'] = func_2101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_249_call = mod.get_global_var('func_249')
func_251_call = mutated_mod.get_global_var('func_251')
call_2111 = relay.TupleGetItem(func_249_call(), 2)
call_2112 = relay.TupleGetItem(func_251_call(), 2)
func_158_call = mod.get_global_var('func_158')
func_161_call = mutated_mod.get_global_var('func_161')
call_2133 = relay.TupleGetItem(func_158_call(relay.reshape(call_2111.astype('float64'), [14, 2, 5])), 0)
call_2134 = relay.TupleGetItem(func_161_call(relay.reshape(call_2111.astype('float64'), [14, 2, 5])), 0)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2139 = func_1178_call()
call_2140 = func_1178_call()
func_1564_call = mod.get_global_var('func_1564')
func_1565_call = mutated_mod.get_global_var('func_1565')
call_2166 = relay.TupleGetItem(func_1564_call(), 1)
call_2167 = relay.TupleGetItem(func_1565_call(), 1)
bop_2178 = relay.less_equal(call_2133.astype('bool'), relay.reshape(call_2111.astype('bool'), relay.shape_of(call_2133))) # shape=(14, 2, 5)
bop_2181 = relay.less_equal(call_2134.astype('bool'), relay.reshape(call_2112.astype('bool'), relay.shape_of(call_2134))) # shape=(14, 2, 5)
output = relay.Tuple([call_2139,call_2166,bop_2178,])
output2 = relay.Tuple([call_2140,call_2167,bop_2181,])
func_2191 = relay.Function([], output)
mod['func_2191'] = func_2191
mod = relay.transform.InferType()(mod)
output = func_2191()
func_2192 = relay.Function([], output)
mutated_mod['func_2192'] = func_2192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2007_call = mutated_mod.get_global_var('func_2007')
call_2201 = relay.TupleGetItem(func_2006_call(), 1)
call_2202 = relay.TupleGetItem(func_2007_call(), 1)
output = call_2201
output2 = call_2202
func_2204 = relay.Function([], output)
mod['func_2204'] = func_2204
mod = relay.transform.InferType()(mod)
mutated_mod['func_2204'] = func_2204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2204_call = mutated_mod.get_global_var('func_2204')
call_2205 = func_2204_call()
output = call_2205
func_2206 = relay.Function([], output)
mutated_mod['func_2206'] = func_2206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_2270 = relay.TupleGetItem(func_937_call(), 0)
call_2271 = relay.TupleGetItem(func_939_call(), 0)
output = call_2270
output2 = call_2271
func_2279 = relay.Function([], output)
mod['func_2279'] = func_2279
mod = relay.transform.InferType()(mod)
output = func_2279()
func_2280 = relay.Function([], output)
mutated_mod['func_2280'] = func_2280
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2290 = relay.var("var_2290", dtype = "float64", shape = ())#candidate|2290|()|var|float64
var_2291 = relay.var("var_2291", dtype = "float64", shape = (14, 11, 13))#candidate|2291|(14, 11, 13)|var|float64
bop_2292 = relay.add(var_2290.astype('float64'), var_2291.astype('float64')) # shape=(14, 11, 13)
output = bop_2292
output2 = bop_2292
func_2299 = relay.Function([var_2290,var_2291,], output)
mod['func_2299'] = func_2299
mod = relay.transform.InferType()(mod)
mutated_mod['func_2299'] = func_2299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2299_call = mutated_mod.get_global_var('func_2299')
var_2301 = relay.var("var_2301", dtype = "float64", shape = ())#candidate|2301|()|var|float64
var_2302 = relay.var("var_2302", dtype = "float64", shape = (14, 11, 13))#candidate|2302|(14, 11, 13)|var|float64
call_2300 = func_2299_call(var_2301,var_2302,)
output = call_2300
func_2303 = relay.Function([var_2301,var_2302,], output)
mutated_mod['func_2303'] = func_2303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_2361 = relay.TupleGetItem(func_1321_call(), 0)
call_2362 = relay.TupleGetItem(func_1323_call(), 0)
func_249_call = mod.get_global_var('func_249')
func_251_call = mutated_mod.get_global_var('func_251')
call_2382 = relay.TupleGetItem(func_249_call(), 2)
call_2383 = relay.TupleGetItem(func_251_call(), 2)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_2384 = func_2204_call()
call_2385 = func_2204_call()
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_2387 = relay.TupleGetItem(func_1149_call(), 2)
call_2388 = relay.TupleGetItem(func_1150_call(), 2)
output = relay.Tuple([call_2361,call_2382,call_2384,call_2387,])
output2 = relay.Tuple([call_2362,call_2383,call_2385,call_2388,])
func_2393 = relay.Function([], output)
mod['func_2393'] = func_2393
mod = relay.transform.InferType()(mod)
output = func_2393()
func_2394 = relay.Function([], output)
mutated_mod['func_2394'] = func_2394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2191_call = mod.get_global_var('func_2191')
func_2192_call = mutated_mod.get_global_var('func_2192')
call_2395 = relay.TupleGetItem(func_2191_call(), 1)
call_2396 = relay.TupleGetItem(func_2192_call(), 1)
func_1041_call = mod.get_global_var('func_1041')
func_1044_call = mutated_mod.get_global_var('func_1044')
var_2402 = relay.var("var_2402", dtype = "float64", shape = (5, 28))#candidate|2402|(5, 28)|var|float64
call_2401 = relay.TupleGetItem(func_1041_call(relay.reshape(var_2402.astype('float64'), [140,])), 0)
call_2403 = relay.TupleGetItem(func_1044_call(relay.reshape(var_2402.astype('float64'), [140,])), 0)
func_1515_call = mod.get_global_var('func_1515')
func_1518_call = mutated_mod.get_global_var('func_1518')
call_2408 = func_1515_call(relay.reshape(call_2395.astype('float32'), [9, 6, 2]))
call_2409 = func_1515_call(relay.reshape(call_2395.astype('float32'), [9, 6, 2]))
uop_2410 = relay.acosh(call_2401.astype('float32')) # shape=(9, 6, 2)
uop_2412 = relay.acosh(call_2403.astype('float32')) # shape=(9, 6, 2)
func_818_call = mod.get_global_var('func_818')
func_820_call = mutated_mod.get_global_var('func_820')
call_2414 = relay.TupleGetItem(func_818_call(), 1)
call_2415 = relay.TupleGetItem(func_820_call(), 1)
output = relay.Tuple([call_2395,var_2402,call_2408,uop_2410,call_2414,])
output2 = relay.Tuple([call_2396,var_2402,call_2409,uop_2412,call_2415,])
func_2430 = relay.Function([var_2402,], output)
mod['func_2430'] = func_2430
mod = relay.transform.InferType()(mod)
mutated_mod['func_2430'] = func_2430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2431 = relay.var("var_2431", dtype = "float64", shape = (5, 28))#candidate|2431|(5, 28)|var|float64
func_2430_call = mutated_mod.get_global_var('func_2430')
call_2432 = func_2430_call(var_2431)
output = call_2432
func_2433 = relay.Function([var_2431], output)
mutated_mod['func_2433'] = func_2433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_694_call = mod.get_global_var('func_694')
func_695_call = mutated_mod.get_global_var('func_695')
call_2441 = relay.TupleGetItem(func_694_call(), 0)
call_2442 = relay.TupleGetItem(func_695_call(), 0)
output = call_2441
output2 = call_2442
func_2451 = relay.Function([], output)
mod['func_2451'] = func_2451
mod = relay.transform.InferType()(mod)
mutated_mod['func_2451'] = func_2451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2451_call = mutated_mod.get_global_var('func_2451')
call_2452 = func_2451_call()
output = call_2452
func_2453 = relay.Function([], output)
mutated_mod['func_2453'] = func_2453
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2454 = relay.var("var_2454", dtype = "int8", shape = (14, 5, 15))#candidate|2454|(14, 5, 15)|var|int8
var_2455 = relay.var("var_2455", dtype = "int8", shape = (14, 5, 15))#candidate|2455|(14, 5, 15)|var|int8
bop_2456 = relay.add(var_2454.astype('int8'), relay.reshape(var_2455.astype('int8'), relay.shape_of(var_2454))) # shape=(14, 5, 15)
func_1219_call = mod.get_global_var('func_1219')
func_1220_call = mutated_mod.get_global_var('func_1220')
call_2488 = relay.TupleGetItem(func_1219_call(), 0)
call_2489 = relay.TupleGetItem(func_1220_call(), 0)
output = relay.Tuple([bop_2456,call_2488,])
output2 = relay.Tuple([bop_2456,call_2489,])
func_2496 = relay.Function([var_2454,var_2455,], output)
mod['func_2496'] = func_2496
mod = relay.transform.InferType()(mod)
var_2497 = relay.var("var_2497", dtype = "int8", shape = (14, 5, 15))#candidate|2497|(14, 5, 15)|var|int8
var_2498 = relay.var("var_2498", dtype = "int8", shape = (14, 5, 15))#candidate|2498|(14, 5, 15)|var|int8
output = func_2496(var_2497,var_2498,)
func_2499 = relay.Function([var_2497,var_2498,], output)
mutated_mod['func_2499'] = func_2499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1242_call = mod.get_global_var('func_1242')
func_1244_call = mutated_mod.get_global_var('func_1244')
call_2548 = func_1242_call()
call_2549 = func_1242_call()
func_1552_call = mod.get_global_var('func_1552')
func_1554_call = mutated_mod.get_global_var('func_1554')
var_2560 = relay.var("var_2560", dtype = "float64", shape = (140,))#candidate|2560|(140,)|var|float64
call_2559 = relay.TupleGetItem(func_1552_call(relay.reshape(var_2560.astype('float64'), [10, 1, 14])), 2)
call_2561 = relay.TupleGetItem(func_1554_call(relay.reshape(var_2560.astype('float64'), [10, 1, 14])), 2)
func_2430_call = mod.get_global_var('func_2430')
func_2433_call = mutated_mod.get_global_var('func_2433')
call_2564 = relay.TupleGetItem(func_2430_call(relay.reshape(call_2559.astype('float64'), [5, 28])), 2)
call_2565 = relay.TupleGetItem(func_2433_call(relay.reshape(call_2559.astype('float64'), [5, 28])), 2)
func_2006_call = mod.get_global_var('func_2006')
func_2007_call = mutated_mod.get_global_var('func_2007')
call_2575 = relay.TupleGetItem(func_2006_call(), 2)
call_2576 = relay.TupleGetItem(func_2007_call(), 2)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
call_2581 = relay.TupleGetItem(func_212_call(relay.reshape(call_2564.astype('float32'), [9, 6, 2]), relay.reshape(call_2559.astype('float64'), [5, 28]), ), 3)
call_2582 = relay.TupleGetItem(func_215_call(relay.reshape(call_2564.astype('float32'), [9, 6, 2]), relay.reshape(call_2559.astype('float64'), [5, 28]), ), 3)
func_1891_call = mod.get_global_var('func_1891')
func_1895_call = mutated_mod.get_global_var('func_1895')
const_2584 = relay.const([[False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True],[False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True],[False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True],[False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False],[False,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True]], dtype = "bool")#candidate|2584|(5, 105)|const|bool
call_2583 = func_1891_call(relay.reshape(const_2584.astype('bool'), [7, 15, 5]), relay.reshape(const_2584.astype('bool'), [7, 15, 5]), )
call_2585 = func_1891_call(relay.reshape(const_2584.astype('bool'), [7, 15, 5]), relay.reshape(const_2584.astype('bool'), [7, 15, 5]), )
output = relay.Tuple([call_2548,call_2559,var_2560,call_2564,call_2575,call_2581,call_2583,const_2584,])
output2 = relay.Tuple([call_2549,call_2561,var_2560,call_2565,call_2576,call_2582,call_2585,const_2584,])
func_2594 = relay.Function([var_2560,], output)
mod['func_2594'] = func_2594
mod = relay.transform.InferType()(mod)
var_2595 = relay.var("var_2595", dtype = "float64", shape = (140,))#candidate|2595|(140,)|var|float64
output = func_2594(var_2595)
func_2596 = relay.Function([var_2595], output)
mutated_mod['func_2596'] = func_2596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_2607 = func_753_call()
call_2608 = func_753_call()
func_1242_call = mod.get_global_var('func_1242')
func_1244_call = mutated_mod.get_global_var('func_1244')
call_2610 = func_1242_call()
call_2611 = func_1242_call()
output = relay.Tuple([call_2607,call_2610,])
output2 = relay.Tuple([call_2608,call_2611,])
func_2619 = relay.Function([], output)
mod['func_2619'] = func_2619
mod = relay.transform.InferType()(mod)
mutated_mod['func_2619'] = func_2619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2619_call = mutated_mod.get_global_var('func_2619')
call_2620 = func_2619_call()
output = call_2620
func_2621 = relay.Function([], output)
mutated_mod['func_2621'] = func_2621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_2625 = func_1385_call()
call_2626 = func_1385_call()
func_1467_call = mod.get_global_var('func_1467')
func_1468_call = mutated_mod.get_global_var('func_1468')
call_2641 = relay.TupleGetItem(func_1467_call(), 0)
call_2642 = relay.TupleGetItem(func_1468_call(), 0)
uop_2673 = relay.erf(call_2625.astype('float64')) # shape=(9, 6, 2)
uop_2675 = relay.erf(call_2626.astype('float64')) # shape=(9, 6, 2)
func_1684_call = mod.get_global_var('func_1684')
func_1686_call = mutated_mod.get_global_var('func_1686')
call_2676 = relay.TupleGetItem(func_1684_call(relay.reshape(call_2625.astype('uint32'), [9, 6, 2])), 0)
call_2677 = relay.TupleGetItem(func_1686_call(relay.reshape(call_2625.astype('uint32'), [9, 6, 2])), 0)
func_450_call = mod.get_global_var('func_450')
func_455_call = mutated_mod.get_global_var('func_455')
call_2695 = relay.TupleGetItem(func_450_call(relay.reshape(call_2625.astype('float32'), [9, 6, 2]), relay.reshape(call_2625.astype('float32'), [9, 6, 2]), relay.reshape(call_2641.astype('float32'), [1, 252]), ), 0)
call_2696 = relay.TupleGetItem(func_455_call(relay.reshape(call_2625.astype('float32'), [9, 6, 2]), relay.reshape(call_2625.astype('float32'), [9, 6, 2]), relay.reshape(call_2641.astype('float32'), [1, 252]), ), 0)
bop_2716 = relay.multiply(uop_2673.astype('float64'), relay.reshape(call_2676.astype('float64'), relay.shape_of(uop_2673))) # shape=(9, 6, 2)
bop_2719 = relay.multiply(uop_2675.astype('float64'), relay.reshape(call_2677.astype('float64'), relay.shape_of(uop_2675))) # shape=(9, 6, 2)
output = relay.Tuple([call_2641,call_2695,bop_2716,])
output2 = relay.Tuple([call_2642,call_2696,bop_2719,])
func_2721 = relay.Function([], output)
mod['func_2721'] = func_2721
mod = relay.transform.InferType()(mod)
output = func_2721()
func_2722 = relay.Function([], output)
mutated_mod['func_2722'] = func_2722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2753 = func_1178_call()
call_2754 = func_1178_call()
func_450_call = mod.get_global_var('func_450')
func_455_call = mutated_mod.get_global_var('func_455')
const_2766 = relay.const([-6.948705,7.194643,-7.526073,2.504783,5.696502,-5.161339,7.555037,-7.838160,8.638480,8.173717,-5.887983,-7.499821,0.655834,1.888346,9.545583,-4.479558,3.574808,-5.508538,-7.570803,-0.564836,7.786462,-8.263725,2.239894,-6.157206,2.347817,6.988285,8.460336,2.897465,-6.389756,-8.111236,-3.006483,-8.068686,-1.099686,0.406293,-9.490480,-1.512360,7.986682,7.582279,5.295893,3.288383,5.550711,8.726410,-8.117922,6.103675,2.829802,-0.434885,-4.716974,0.740848,-0.077429,6.933051,-8.377571,-3.245268,-7.738605,-8.379824,-5.719316,6.112256,1.715225,-3.677678,2.433346,-6.395007,8.208516,4.059793,6.180006,8.311741,9.790125,2.990002,-5.807159,0.305943,1.002306,2.001038,0.965294,6.335857,6.440330,2.123560,1.394481,6.862176,-8.793301,5.123507,-8.994111,5.931393,1.258031,3.708532,7.240159,7.269202,3.040120,-8.822446,0.857150,4.069433,2.491536,6.873176,-8.227275,-2.170810,6.435842,9.891317,-7.379201,-4.740944,9.152260,5.318094,-4.708129,2.493759,5.978195,5.858995,2.203889,6.190275,8.675887,3.818697,-9.078737,-0.618174,8.695535,3.528424,8.890870,-7.728048,7.071457,4.744273,-7.683135,3.932158,-4.397362,-7.411636,0.436321,-8.403848,-6.004620,9.354841,7.233859,4.017526,1.116099,-9.191115,-7.936999,6.990398,2.703134,7.666266,5.035368,0.259187,6.771036,9.610543,-0.102045,9.857008,2.705138,0.037682,7.214501,-7.217714,2.961965,3.288834,6.358065,8.819240,2.724476,-6.003665,-9.688039,-9.552427,3.409929,-3.777174,2.823138,-5.136967,-8.733788,-1.025973,-5.526557,-5.885850,5.216788,9.245818,-8.743586,9.618211,-7.515050,-6.621690,-9.287269,-2.842119,-5.575241,8.983540,4.082885,8.710196,5.779707,7.116799,-1.349001,5.382365,9.853815,-1.973617,1.676442,3.739221,9.008676,-8.167810,-1.381665,5.434288,-1.016435,-4.845137,-9.351404,2.330764,5.900388,-8.503384,7.801749,-4.142166,-0.787781,-3.139831,-0.204582,0.652170,-8.797077,8.680228,2.337534,0.434802,1.265851,2.080179,6.280908,1.094679,4.665803,-9.564118,3.043847,1.015059,0.937301,-7.087634,7.782977,3.460057,7.363429,-7.646272,4.387643,-3.155909,4.336155,4.156435,8.585731,-2.062514,-2.479800,8.036933,9.590477,1.478658,-4.351204,-7.143572,-4.681130,5.108340,3.445390,-3.312935,-8.482729,0.358420,-6.097219,-9.379090,-5.887409,-2.901557,-0.639454,-4.455781,-1.231453,-7.953329,9.497471,-5.112805,4.240857,-0.120777,7.954609,0.990813,1.405337,8.242407,7.920335,6.263470,-8.471778,-6.562184,8.745775,-3.578579,6.373181,2.089934], dtype = "float32")#candidate|2766|(252,)|const|float32
call_2765 = relay.TupleGetItem(func_450_call(relay.reshape(call_2753.astype('float32'), [9, 6, 2]), relay.reshape(call_2753.astype('float32'), [9, 6, 2]), relay.reshape(const_2766.astype('float32'), [1, 252]), ), 1)
call_2767 = relay.TupleGetItem(func_455_call(relay.reshape(call_2753.astype('float32'), [9, 6, 2]), relay.reshape(call_2753.astype('float32'), [9, 6, 2]), relay.reshape(const_2766.astype('float32'), [1, 252]), ), 1)
output = relay.Tuple([call_2753,call_2765,const_2766,])
output2 = relay.Tuple([call_2754,call_2767,const_2766,])
func_2777 = relay.Function([], output)
mod['func_2777'] = func_2777
mod = relay.transform.InferType()(mod)
output = func_2777()
func_2778 = relay.Function([], output)
mutated_mod['func_2778'] = func_2778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2007_call = mutated_mod.get_global_var('func_2007')
call_2860 = relay.TupleGetItem(func_2006_call(), 3)
call_2861 = relay.TupleGetItem(func_2007_call(), 3)
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_2890 = relay.TupleGetItem(func_545_call(), 0)
call_2891 = relay.TupleGetItem(func_546_call(), 0)
var_2892 = relay.var("var_2892", dtype = "int8", shape = (9, 6, 2))#candidate|2892|(9, 6, 2)|var|int8
bop_2893 = relay.floor_mod(call_2890.astype('float32'), relay.reshape(var_2892.astype('float32'), relay.shape_of(call_2890))) # shape=(9, 6, 2)
bop_2896 = relay.floor_mod(call_2891.astype('float32'), relay.reshape(var_2892.astype('float32'), relay.shape_of(call_2891))) # shape=(9, 6, 2)
func_1515_call = mod.get_global_var('func_1515')
func_1518_call = mutated_mod.get_global_var('func_1518')
call_2930 = func_1515_call(relay.reshape(bop_2893.astype('float32'), [9, 6, 2]))
call_2931 = func_1515_call(relay.reshape(bop_2893.astype('float32'), [9, 6, 2]))
output = relay.Tuple([call_2860,bop_2893,call_2930,])
output2 = relay.Tuple([call_2861,bop_2896,call_2931,])
func_2940 = relay.Function([var_2892,], output)
mod['func_2940'] = func_2940
mod = relay.transform.InferType()(mod)
mutated_mod['func_2940'] = func_2940
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2941 = relay.var("var_2941", dtype = "int8", shape = (9, 6, 2))#candidate|2941|(9, 6, 2)|var|int8
func_2940_call = mutated_mod.get_global_var('func_2940')
call_2942 = func_2940_call(var_2941)
output = call_2942
func_2943 = relay.Function([var_2941], output)
mutated_mod['func_2943'] = func_2943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_646_call = mod.get_global_var('func_646')
func_648_call = mutated_mod.get_global_var('func_648')
call_2963 = func_646_call()
call_2964 = func_646_call()
output = call_2963
output2 = call_2964
func_2966 = relay.Function([], output)
mod['func_2966'] = func_2966
mod = relay.transform.InferType()(mod)
mutated_mod['func_2966'] = func_2966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2966_call = mutated_mod.get_global_var('func_2966')
call_2967 = func_2966_call()
output = call_2967
func_2968 = relay.Function([], output)
mutated_mod['func_2968'] = func_2968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2619_call = mod.get_global_var('func_2619')
func_2621_call = mutated_mod.get_global_var('func_2621')
call_2969 = relay.TupleGetItem(func_2619_call(), 1)
call_2970 = relay.TupleGetItem(func_2621_call(), 1)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2982 = func_1178_call()
call_2983 = func_1178_call()
output = relay.Tuple([call_2969,call_2982,])
output2 = relay.Tuple([call_2970,call_2983,])
func_2997 = relay.Function([], output)
mod['func_2997'] = func_2997
mod = relay.transform.InferType()(mod)
mutated_mod['func_2997'] = func_2997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2997_call = mutated_mod.get_global_var('func_2997')
call_2998 = func_2997_call()
output = call_2998
func_2999 = relay.Function([], output)
mutated_mod['func_2999'] = func_2999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_646_call = mod.get_global_var('func_646')
func_648_call = mutated_mod.get_global_var('func_648')
call_3003 = func_646_call()
call_3004 = func_646_call()
uop_3012 = relay.atanh(call_3003.astype('float32')) # shape=(9, 6, 2)
uop_3014 = relay.atanh(call_3004.astype('float32')) # shape=(9, 6, 2)
func_2966_call = mod.get_global_var('func_2966')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3026 = func_2966_call()
call_3027 = func_2966_call()
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_3041 = relay.TupleGetItem(func_971_call(), 0)
call_3042 = relay.TupleGetItem(func_973_call(), 0)
output = relay.Tuple([uop_3012,call_3026,call_3041,])
output2 = relay.Tuple([uop_3014,call_3027,call_3042,])
func_3059 = relay.Function([], output)
mod['func_3059'] = func_3059
mod = relay.transform.InferType()(mod)
output = func_3059()
func_3060 = relay.Function([], output)
mutated_mod['func_3060'] = func_3060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_3083 = relay.TupleGetItem(func_1321_call(), 1)
call_3084 = relay.TupleGetItem(func_1323_call(), 1)
output = call_3083
output2 = call_3084
func_3094 = relay.Function([], output)
mod['func_3094'] = func_3094
mod = relay.transform.InferType()(mod)
mutated_mod['func_3094'] = func_3094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3094_call = mutated_mod.get_global_var('func_3094')
call_3095 = func_3094_call()
output = call_3095
func_3096 = relay.Function([], output)
mutated_mod['func_3096'] = func_3096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3059_call = mod.get_global_var('func_3059')
func_3060_call = mutated_mod.get_global_var('func_3060')
call_3097 = relay.TupleGetItem(func_3059_call(), 1)
call_3098 = relay.TupleGetItem(func_3060_call(), 1)
output = relay.Tuple([call_3097,])
output2 = relay.Tuple([call_3098,])
func_3109 = relay.Function([], output)
mod['func_3109'] = func_3109
mod = relay.transform.InferType()(mod)
output = func_3109()
func_3110 = relay.Function([], output)
mutated_mod['func_3110'] = func_3110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_3201 = func_1178_call()
call_3202 = func_1178_call()
output = call_3201
output2 = call_3202
func_3203 = relay.Function([], output)
mod['func_3203'] = func_3203
mod = relay.transform.InferType()(mod)
mutated_mod['func_3203'] = func_3203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3203_call = mutated_mod.get_global_var('func_3203')
call_3204 = func_3203_call()
output = call_3204
func_3205 = relay.Function([], output)
mutated_mod['func_3205'] = func_3205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2451_call = mod.get_global_var('func_2451')
func_2453_call = mutated_mod.get_global_var('func_2453')
call_3253 = func_2451_call()
call_3254 = func_2451_call()
func_1564_call = mod.get_global_var('func_1564')
func_1565_call = mutated_mod.get_global_var('func_1565')
call_3261 = relay.TupleGetItem(func_1564_call(), 1)
call_3262 = relay.TupleGetItem(func_1565_call(), 1)
output = relay.Tuple([call_3253,call_3261,])
output2 = relay.Tuple([call_3254,call_3262,])
func_3272 = relay.Function([], output)
mod['func_3272'] = func_3272
mod = relay.transform.InferType()(mod)
mutated_mod['func_3272'] = func_3272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3272_call = mutated_mod.get_global_var('func_3272')
call_3273 = func_3272_call()
output = call_3273
func_3274 = relay.Function([], output)
mutated_mod['func_3274'] = func_3274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3203_call = mod.get_global_var('func_3203')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_3297 = func_3203_call()
call_3298 = func_3203_call()
output = call_3297
output2 = call_3298
func_3315 = relay.Function([], output)
mod['func_3315'] = func_3315
mod = relay.transform.InferType()(mod)
output = func_3315()
func_3316 = relay.Function([], output)
mutated_mod['func_3316'] = func_3316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_3361 = relay.TupleGetItem(func_2777_call(), 0)
call_3362 = relay.TupleGetItem(func_2778_call(), 0)
func_818_call = mod.get_global_var('func_818')
func_820_call = mutated_mod.get_global_var('func_820')
call_3368 = relay.TupleGetItem(func_818_call(), 0)
call_3369 = relay.TupleGetItem(func_820_call(), 0)
func_158_call = mod.get_global_var('func_158')
func_161_call = mutated_mod.get_global_var('func_161')
var_3380 = relay.var("var_3380", dtype = "float64", shape = (70, 2))#candidate|3380|(70, 2)|var|float64
call_3379 = relay.TupleGetItem(func_158_call(relay.reshape(var_3380.astype('float64'), [14, 2, 5])), 0)
call_3381 = relay.TupleGetItem(func_161_call(relay.reshape(var_3380.astype('float64'), [14, 2, 5])), 0)
bop_3387 = relay.maximum(var_3380.astype('float32'), relay.reshape(call_3379.astype('float32'), relay.shape_of(var_3380))) # shape=(70, 2)
bop_3390 = relay.maximum(var_3380.astype('float32'), relay.reshape(call_3381.astype('float32'), relay.shape_of(var_3380))) # shape=(70, 2)
output = relay.Tuple([call_3361,call_3368,bop_3387,])
output2 = relay.Tuple([call_3362,call_3369,bop_3390,])
func_3394 = relay.Function([var_3380,], output)
mod['func_3394'] = func_3394
mod = relay.transform.InferType()(mod)
var_3395 = relay.var("var_3395", dtype = "float64", shape = (70, 2))#candidate|3395|(70, 2)|var|float64
output = func_3394(var_3395)
func_3396 = relay.Function([var_3395], output)
mutated_mod['func_3396'] = func_3396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_3398 = relay.TupleGetItem(func_1149_call(), 2)
call_3399 = relay.TupleGetItem(func_1150_call(), 2)
var_3401 = relay.var("var_3401", dtype = "uint64", shape = (14, 2, 5))#candidate|3401|(14, 2, 5)|var|uint64
bop_3402 = relay.multiply(call_3398.astype('int32'), relay.reshape(var_3401.astype('int32'), relay.shape_of(call_3398))) # shape=(14, 2, 5)
bop_3405 = relay.multiply(call_3399.astype('int32'), relay.reshape(var_3401.astype('int32'), relay.shape_of(call_3399))) # shape=(14, 2, 5)
output = bop_3402
output2 = bop_3405
func_3406 = relay.Function([var_3401,], output)
mod['func_3406'] = func_3406
mod = relay.transform.InferType()(mod)
var_3407 = relay.var("var_3407", dtype = "uint64", shape = (14, 2, 5))#candidate|3407|(14, 2, 5)|var|uint64
output = func_3406(var_3407)
func_3408 = relay.Function([var_3407], output)
mutated_mod['func_3408'] = func_3408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1847_call = mod.get_global_var('func_1847')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_3416 = func_1847_call()
call_3417 = func_1847_call()
func_2430_call = mod.get_global_var('func_2430')
func_2433_call = mutated_mod.get_global_var('func_2433')
const_3438 = relay.const([-9.546723,-4.236620,-6.013473,-2.044212,8.526685,9.776948,-9.843037,4.770885,-4.782095,-1.358425,6.784860,-1.159501,-5.352203,-4.362490,8.438576,-9.914482,4.882861,-5.795664,-2.279835,6.006898,6.888100,-6.232385,5.936106,-8.678269,-1.402463,8.817857,-5.746307,-7.224338,2.873580,-8.419330,-6.494936,1.344551,-0.247171,2.979168,-3.151931,-7.537577,3.213037,0.400672,-0.572084,-4.920428,3.899508,-2.213810,5.097912,-1.710538,-5.788359,6.917835,3.680854,-7.802053,-8.235451,-3.274446,-9.856822,2.006551,4.151330,-4.049347,-7.262435,6.493767,-1.593685,0.161216,-4.688536,-7.226054,-4.132403,4.221454,-8.256640,5.850382,5.208983,-4.769862,-6.748826,2.641789,-9.816801,-6.546028,-4.808018,-3.019234,8.395500,-6.774669,8.547407,-7.388526,-9.395382,-4.691050,7.379358,-1.814658,4.221752,-1.414784,-3.892212,-5.897034,7.313259,2.029920,-6.026106,-0.202450,8.686819,8.599881,-0.859311,-1.643583,-0.801530,9.310364,6.450564,-0.228675,-5.066736,-8.599828,4.866485,-6.738678,1.358785,-8.604366,4.371289,-4.841404,-5.879798,-7.589367,4.127446,1.392913,5.145319,-4.392016,-5.025969,3.358792,1.123943,0.756174,-9.517857,-3.616893,2.663699,2.673450,4.979260,8.575989,-3.716018,-6.422550,8.963802,5.577839,3.360901,5.331363,-4.612805,-1.346563,-2.680494,-9.655890,2.910176,5.915518,-9.704906,-7.709369,-0.191950,4.537668,8.719581,-1.922398,3.639163,3.670828], dtype = "float64")#candidate|3438|(140,)|const|float64
call_3437 = relay.TupleGetItem(func_2430_call(relay.reshape(const_3438.astype('float64'), [5, 28])), 4)
call_3439 = relay.TupleGetItem(func_2433_call(relay.reshape(const_3438.astype('float64'), [5, 28])), 4)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_3440 = func_2204_call()
call_3441 = func_2204_call()
output = relay.Tuple([call_3416,call_3437,const_3438,call_3440,])
output2 = relay.Tuple([call_3417,call_3439,const_3438,call_3441,])
func_3443 = relay.Function([], output)
mod['func_3443'] = func_3443
mod = relay.transform.InferType()(mod)
mutated_mod['func_3443'] = func_3443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3443_call = mutated_mod.get_global_var('func_3443')
call_3444 = func_3443_call()
output = call_3444
func_3445 = relay.Function([], output)
mutated_mod['func_3445'] = func_3445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_818_call = mod.get_global_var('func_818')
func_820_call = mutated_mod.get_global_var('func_820')
call_3497 = relay.TupleGetItem(func_818_call(), 1)
call_3498 = relay.TupleGetItem(func_820_call(), 1)
uop_3511 = relay.sqrt(call_3497.astype('float32')) # shape=(9, 6, 2)
uop_3513 = relay.sqrt(call_3498.astype('float32')) # shape=(9, 6, 2)
output = relay.Tuple([uop_3511,])
output2 = relay.Tuple([uop_3513,])
func_3515 = relay.Function([], output)
mod['func_3515'] = func_3515
mod = relay.transform.InferType()(mod)
mutated_mod['func_3515'] = func_3515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3515_call = mutated_mod.get_global_var('func_3515')
call_3516 = func_3515_call()
output = call_3516
func_3517 = relay.Function([], output)
mutated_mod['func_3517'] = func_3517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1219_call = mod.get_global_var('func_1219')
func_1220_call = mutated_mod.get_global_var('func_1220')
call_3520 = relay.TupleGetItem(func_1219_call(), 0)
call_3521 = relay.TupleGetItem(func_1220_call(), 0)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_3539 = relay.TupleGetItem(func_580_call(), 1)
call_3540 = relay.TupleGetItem(func_582_call(), 1)
output = relay.Tuple([call_3520,call_3539,])
output2 = relay.Tuple([call_3521,call_3540,])
func_3572 = relay.Function([], output)
mod['func_3572'] = func_3572
mod = relay.transform.InferType()(mod)
output = func_3572()
func_3573 = relay.Function([], output)
mutated_mod['func_3573'] = func_3573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3203_call = mod.get_global_var('func_3203')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_3607 = func_3203_call()
call_3608 = func_3203_call()
output = relay.Tuple([call_3607,])
output2 = relay.Tuple([call_3608,])
func_3654 = relay.Function([], output)
mod['func_3654'] = func_3654
mod = relay.transform.InferType()(mod)
output = func_3654()
func_3655 = relay.Function([], output)
mutated_mod['func_3655'] = func_3655
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3660 = relay.var("var_3660", dtype = "uint64", shape = (3, 9, 11))#candidate|3660|(3, 9, 11)|var|uint64
var_3661 = relay.var("var_3661", dtype = "uint64", shape = (3, 9, 11))#candidate|3661|(3, 9, 11)|var|uint64
bop_3662 = relay.left_shift(var_3660.astype('uint64'), relay.reshape(var_3661.astype('uint64'), relay.shape_of(var_3660))) # shape=(3, 9, 11)
func_1041_call = mod.get_global_var('func_1041')
func_1044_call = mutated_mod.get_global_var('func_1044')
var_3678 = relay.var("var_3678", dtype = "float64", shape = (140,))#candidate|3678|(140,)|var|float64
call_3677 = relay.TupleGetItem(func_1041_call(relay.reshape(var_3678.astype('float64'), [140,])), 2)
call_3679 = relay.TupleGetItem(func_1044_call(relay.reshape(var_3678.astype('float64'), [140,])), 2)
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_3686 = relay.TupleGetItem(func_1149_call(), 3)
call_3687 = relay.TupleGetItem(func_1150_call(), 3)
bop_3692 = relay.add(call_3686.astype('int64'), relay.reshape(var_3678.astype('int64'), relay.shape_of(call_3686))) # shape=(1, 140)
bop_3695 = relay.add(call_3687.astype('int64'), relay.reshape(var_3678.astype('int64'), relay.shape_of(call_3687))) # shape=(1, 140)
uop_3703 = relay.log2(call_3686.astype('float64')) # shape=(1, 140)
uop_3705 = relay.log2(call_3687.astype('float64')) # shape=(1, 140)
output = relay.Tuple([bop_3662,call_3677,bop_3692,uop_3703,])
output2 = relay.Tuple([bop_3662,call_3679,bop_3695,uop_3705,])
func_3706 = relay.Function([var_3660,var_3661,var_3678,], output)
mod['func_3706'] = func_3706
mod = relay.transform.InferType()(mod)
var_3707 = relay.var("var_3707", dtype = "uint64", shape = (3, 9, 11))#candidate|3707|(3, 9, 11)|var|uint64
var_3708 = relay.var("var_3708", dtype = "uint64", shape = (3, 9, 11))#candidate|3708|(3, 9, 11)|var|uint64
var_3709 = relay.var("var_3709", dtype = "float64", shape = (140,))#candidate|3709|(140,)|var|float64
output = func_3706(var_3707,var_3708,var_3709,)
func_3710 = relay.Function([var_3707,var_3708,var_3709,], output)
mutated_mod['func_3710'] = func_3710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1242_call = mod.get_global_var('func_1242')
func_1244_call = mutated_mod.get_global_var('func_1244')
call_3719 = func_1242_call()
call_3720 = func_1242_call()
output = relay.Tuple([call_3719,])
output2 = relay.Tuple([call_3720,])
func_3721 = relay.Function([], output)
mod['func_3721'] = func_3721
mod = relay.transform.InferType()(mod)
output = func_3721()
func_3722 = relay.Function([], output)
mutated_mod['func_3722'] = func_3722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_3744 = relay.TupleGetItem(func_1321_call(), 1)
call_3745 = relay.TupleGetItem(func_1323_call(), 1)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
const_3753 = relay.const([0.839846,-7.385766,8.997070,6.448915,1.860678,6.303667,1.706422,3.665424,-9.250541,7.824012,-0.597421,-0.121576,-1.414478,4.982609,8.988434,5.260322,-4.575791,-5.716517,9.677319,1.887215,0.593294,-1.178536,-1.900459,-9.862550,9.601404,-0.112623,-2.333478,4.263507,4.853379,-2.895017,8.127202,8.259111,8.922749,0.531679,-0.890587,-7.570609,6.480860,-1.321523,-2.711989,-1.663198,-0.042303,0.927072,-8.853565,1.954129,3.658713,-5.260268,-9.109780,-9.053717,7.377402,-7.557006,-9.364852,7.819580,5.116705,4.162654,2.815230,9.004880,8.587839,-5.093030,2.894374,3.810957,8.462258,5.968366,5.480108,-2.960317,6.244680,-5.971117,2.250841,1.676330,-6.641979,-6.207205,-7.779269,5.612503,-7.403314,9.946281,-7.736380,-0.624651,-8.040770,7.292535,-0.344553,-1.496765,-8.917459,6.940559,6.946084,-4.686856,-3.620250,6.349683,-2.144891,-4.631081,-4.668069,-7.752986,-0.164224,-1.781128,-3.703280,-5.399256,9.734591,-7.052709,-7.792279,0.175086,-8.089627,8.308537,-4.433901,8.827122,7.743021,4.813265,-0.442545,-7.054249,7.512552,6.580245], dtype = "float32")#candidate|3753|(108,)|const|float32
call_3752 = relay.TupleGetItem(func_212_call(relay.reshape(const_3753.astype('float32'), [9, 6, 2]), relay.reshape(call_3744.astype('float64'), [5, 28]), ), 2)
call_3754 = relay.TupleGetItem(func_215_call(relay.reshape(const_3753.astype('float32'), [9, 6, 2]), relay.reshape(call_3744.astype('float64'), [5, 28]), ), 2)
func_1242_call = mod.get_global_var('func_1242')
func_1244_call = mutated_mod.get_global_var('func_1244')
call_3758 = func_1242_call()
call_3759 = func_1242_call()
func_614_call = mod.get_global_var('func_614')
func_617_call = mutated_mod.get_global_var('func_617')
call_3760 = relay.TupleGetItem(func_614_call(relay.reshape(call_3758.astype('int8'), [9, 6, 2])), 0)
call_3761 = relay.TupleGetItem(func_617_call(relay.reshape(call_3758.astype('int8'), [9, 6, 2])), 0)
output = relay.Tuple([call_3744,call_3752,const_3753,call_3758,call_3760,])
output2 = relay.Tuple([call_3745,call_3754,const_3753,call_3759,call_3761,])
func_3789 = relay.Function([], output)
mod['func_3789'] = func_3789
mod = relay.transform.InferType()(mod)
mutated_mod['func_3789'] = func_3789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mutated_mod.get_global_var('func_3789')
call_3790 = func_3789_call()
output = call_3790
func_3791 = relay.Function([], output)
mutated_mod['func_3791'] = func_3791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_3931 = relay.TupleGetItem(func_501_call(), 0)
call_3932 = relay.TupleGetItem(func_503_call(), 0)
output = relay.Tuple([call_3931,])
output2 = relay.Tuple([call_3932,])
func_3992 = relay.Function([], output)
mod['func_3992'] = func_3992
mod = relay.transform.InferType()(mod)
output = func_3992()
func_3993 = relay.Function([], output)
mutated_mod['func_3993'] = func_3993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_4061 = func_1385_call()
call_4062 = func_1385_call()
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_4072 = func_753_call()
call_4073 = func_753_call()
func_1079_call = mod.get_global_var('func_1079')
func_1080_call = mutated_mod.get_global_var('func_1080')
call_4076 = relay.TupleGetItem(func_1079_call(), 0)
call_4077 = relay.TupleGetItem(func_1080_call(), 0)
output = relay.Tuple([call_4061,call_4072,call_4076,])
output2 = relay.Tuple([call_4062,call_4073,call_4077,])
func_4080 = relay.Function([], output)
mod['func_4080'] = func_4080
mod = relay.transform.InferType()(mod)
output = func_4080()
func_4081 = relay.Function([], output)
mutated_mod['func_4081'] = func_4081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3791_call = mutated_mod.get_global_var('func_3791')
call_4123 = relay.TupleGetItem(func_3789_call(), 3)
call_4124 = relay.TupleGetItem(func_3791_call(), 3)
output = call_4123
output2 = call_4124
func_4130 = relay.Function([], output)
mod['func_4130'] = func_4130
mod = relay.transform.InferType()(mod)
mutated_mod['func_4130'] = func_4130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4130_call = mutated_mod.get_global_var('func_4130')
call_4131 = func_4130_call()
output = call_4131
func_4132 = relay.Function([], output)
mutated_mod['func_4132'] = func_4132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_4223 = func_121_call()
call_4224 = func_121_call()
func_3654_call = mod.get_global_var('func_3654')
func_3655_call = mutated_mod.get_global_var('func_3655')
call_4231 = relay.TupleGetItem(func_3654_call(), 0)
call_4232 = relay.TupleGetItem(func_3655_call(), 0)
output = relay.Tuple([call_4223,call_4231,])
output2 = relay.Tuple([call_4224,call_4232,])
func_4238 = relay.Function([], output)
mod['func_4238'] = func_4238
mod = relay.transform.InferType()(mod)
output = func_4238()
func_4239 = relay.Function([], output)
mutated_mod['func_4239'] = func_4239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1564_call = mod.get_global_var('func_1564')
func_1565_call = mutated_mod.get_global_var('func_1565')
call_4245 = relay.TupleGetItem(func_1564_call(), 1)
call_4246 = relay.TupleGetItem(func_1565_call(), 1)
output = call_4245
output2 = call_4246
func_4255 = relay.Function([], output)
mod['func_4255'] = func_4255
mod = relay.transform.InferType()(mod)
mutated_mod['func_4255'] = func_4255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4255_call = mutated_mod.get_global_var('func_4255')
call_4256 = func_4255_call()
output = call_4256
func_4257 = relay.Function([], output)
mutated_mod['func_4257'] = func_4257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mod.get_global_var('func_2099')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_4283 = relay.TupleGetItem(func_2099_call(), 0)
call_4284 = relay.TupleGetItem(func_2101_call(), 0)
output = call_4283
output2 = call_4284
func_4304 = relay.Function([], output)
mod['func_4304'] = func_4304
mod = relay.transform.InferType()(mod)
mutated_mod['func_4304'] = func_4304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4304_call = mutated_mod.get_global_var('func_4304')
call_4305 = func_4304_call()
output = call_4305
func_4306 = relay.Function([], output)
mutated_mod['func_4306'] = func_4306
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4310 = relay.const([[[2,-4,1,-2,1,-2,3,9,-2,-5,-2,3,-5],[10,10,8,5,10,3,5,-8,-3,2,-10,-10,-7],[7,-4,6,10,9,7,9,-10,-9,-6,-3,7,-4]],[[-2,-2,-5,-1,-1,4,5,9,-7,-1,-3,-3,-5],[-10,4,9,-8,-6,-2,-1,4,-4,9,2,4,-3],[2,-5,-2,1,-1,-1,5,-2,-4,10,10,-8,-7]],[[-3,2,7,-1,2,1,9,-6,-3,-8,6,9,2],[9,-6,-10,9,-6,7,3,1,3,-8,-8,9,-5],[8,2,1,1,10,-8,-5,-9,4,-4,-8,4,-7]],[[6,-10,1,-2,9,-4,3,-2,-5,7,-1,-8,7],[1,1,-4,6,-7,-4,-9,2,-5,-9,8,-6,-8],[8,-4,-1,6,5,-8,-6,7,3,4,3,-2,8]],[[6,5,-3,-1,9,1,5,-5,-6,-7,-2,-1,8],[6,6,-10,-10,-10,9,1,5,-3,-8,5,-9,9],[3,-8,5,2,9,-8,6,-5,1,-5,8,9,6]],[[1,6,-7,-1,-1,10,-2,5,10,-7,-8,-9,-5],[1,-4,-9,4,-5,6,7,-6,3,8,5,-9,2],[-1,2,-9,-1,4,8,-5,1,2,-1,7,-6,1]],[[-4,6,-10,1,2,-9,-3,-4,10,-5,-5,9,5],[9,2,3,-10,3,3,-4,-4,-1,-3,-9,8,-4],[-10,8,-10,7,5,-9,6,-5,-8,7,1,10,-4]],[[-6,6,5,2,1,8,-5,7,-10,-6,3,3,7],[-9,7,-9,-8,-1,-10,6,-7,9,-9,-4,9,-3],[7,6,9,2,-1,-9,3,-1,4,-4,2,-3,-10]],[[-2,-10,-3,1,8,5,8,-10,-4,-6,7,10,3],[7,-5,-2,5,-9,6,8,-2,7,-10,6,1,6],[-3,1,10,-9,-4,1,-4,10,2,5,2,5,-8]],[[-5,-2,9,7,1,-10,2,3,3,-4,7,-2,2],[-6,-5,10,7,1,7,-8,7,1,1,-3,-3,-9],[4,5,-7,-5,-7,-4,-4,10,5,4,-5,-1,10]],[[5,2,-2,-7,-2,-7,-7,-9,9,-8,-9,-7,4],[7,-10,-1,10,9,8,10,10,-7,4,-10,1,1],[10,10,-2,1,-6,9,6,8,5,5,5,-4,10]],[[-1,-1,-9,-2,5,8,8,-8,7,-6,-9,-3,6],[-8,7,4,9,2,-4,-8,8,5,-9,-4,9,3],[1,-4,-6,-5,2,-10,-5,-6,-7,-10,-2,5,-9]],[[2,-9,8,3,-4,6,-1,-1,9,3,6,2,7],[10,5,-10,-9,-4,-8,-9,-3,4,-5,-4,2,10],[9,4,5,-9,7,-9,-8,-3,9,9,-9,5,9]],[[-8,1,8,1,-8,-8,-9,6,-9,-3,1,6,-4],[-2,-1,-10,-1,-9,1,-9,-8,-5,1,-7,6,-5],[-9,-8,8,-2,10,-9,5,9,10,6,-6,5,4]],[[10,-1,8,5,-5,-5,-3,-10,-7,-4,2,6,-2],[-1,-10,8,-5,-4,-10,-9,4,-1,1,3,8,-6],[-9,-10,-7,-7,-6,-6,5,3,2,10,6,-5,5]]], dtype = "int32")#candidate|4310|(15, 3, 13)|const|int32
var_4311 = relay.var("var_4311", dtype = "int32", shape = (15, 3, 13))#candidate|4311|(15, 3, 13)|var|int32
bop_4312 = relay.maximum(const_4310.astype('int32'), relay.reshape(var_4311.astype('int32'), relay.shape_of(const_4310))) # shape=(15, 3, 13)
bop_4316 = relay.left_shift(bop_4312.astype('uint64'), relay.reshape(const_4310.astype('uint64'), relay.shape_of(bop_4312))) # shape=(15, 3, 13)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_4320 = relay.TupleGetItem(func_580_call(), 0)
call_4321 = relay.TupleGetItem(func_582_call(), 0)
output = relay.Tuple([bop_4316,call_4320,])
output2 = relay.Tuple([bop_4316,call_4321,])
func_4323 = relay.Function([var_4311,], output)
mod['func_4323'] = func_4323
mod = relay.transform.InferType()(mod)
mutated_mod['func_4323'] = func_4323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4324 = relay.var("var_4324", dtype = "int32", shape = (15, 3, 13))#candidate|4324|(15, 3, 13)|var|int32
func_4323_call = mutated_mod.get_global_var('func_4323')
call_4325 = func_4323_call(var_4324)
output = call_4325
func_4326 = relay.Function([var_4324], output)
mutated_mod['func_4326'] = func_4326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2191_call = mod.get_global_var('func_2191')
func_2192_call = mutated_mod.get_global_var('func_2192')
call_4440 = relay.TupleGetItem(func_2191_call(), 2)
call_4441 = relay.TupleGetItem(func_2192_call(), 2)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_4443 = func_121_call()
call_4444 = func_121_call()
func_1484_call = mod.get_global_var('func_1484')
func_1485_call = mutated_mod.get_global_var('func_1485')
call_4449 = relay.TupleGetItem(func_1484_call(), 0)
call_4450 = relay.TupleGetItem(func_1485_call(), 0)
output = relay.Tuple([call_4440,call_4443,call_4449,])
output2 = relay.Tuple([call_4441,call_4444,call_4450,])
func_4478 = relay.Function([], output)
mod['func_4478'] = func_4478
mod = relay.transform.InferType()(mod)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4478_call = mutated_mod.get_global_var('func_4478')
call_4479 = func_4478_call()
output = call_4479
func_4480 = relay.Function([], output)
mutated_mod['func_4480'] = func_4480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_4508 = relay.TupleGetItem(func_937_call(), 0)
call_4509 = relay.TupleGetItem(func_939_call(), 0)
func_4323_call = mod.get_global_var('func_4323')
func_4326_call = mutated_mod.get_global_var('func_4326')
const_4524 = relay.const([-10,9,-1,3,-3,4,8,8,-3,-2,10,-6,4,1,-9,-5,9,-7,5,4,1,-9,-3,-2,-10,7,8,-2,-1,6,7,-9,9,9,-5,2,-10,-7,-8,9,-5,5,-10,-4,9,-1,5,-5,7,6,6,2,-9,-8,9,-2,-6,6,5,6,-1,-2,-8,-9,-2,7,-3,3,9,8,3,-2,8,-4,9,-8,-7,-7,1,10,-2,-1,-7,8,8,-3,7,-1,-5,-9,4,-5,2,-6,1,-6,4,-10,4,8,-6,-4,-8,8,-7,-8,-8,4,6,-3,-7,-9,-6,5,-9,-1,-5,7,-9,9,-4,1,-9,-2,-4,-1,3,5,1,1,-2,-4,-9,-2,-8,6,-7,3,-1,-2,-1,-9,3,6,-3,-3,-9,-4,7,-7,-9,8,2,-2,8,2,-7,6,3,3,8,3,-4,-6,-2,-8,9,-7,-7,8,4,-7,-8,-10,-4,9,10,9,-8,5,-1,-3,6,3,-10,1,8,-5,-10,1,8,7,-3,-2,-3,-5,9,-5,9,-10,-9,-4,-8,5,-4,1,-8,1,-5,4,-7,4,-8,-1,-9,9,2,6,2,8,-10,9,-7,1,3,-2,6,-8,-5,3,-2,1,-6,3,-8,6,-8,-6,-5,-7,-4,-1,-4,-7,8,2,-4,3,8,10,5,-4,10,9,10,-4,-6,-7,3,-9,5,10,-2,9,-9,8,2,-10,-3,-8,9,-7,8,-5,-7,-4,4,10,-9,8,8,5,-7,2,5,4,5,-7,5,-6,6,5,-5,8,3,-5,3,1,-4,3,-7,1,8,7,-2,8,-4,-8,9,5,5,3,10,9,10,-1,-8,-9,2,2,8,2,4,-2,-7,2,-9,-9,2,-2,9,-1,10,3,-5,-6,4,8,-7,8,-9,7,9,8,-3,6,-8,10,7,9,-8,-9,-2,-10,-7,-4,-3,4,-6,-5,-5,-2,-8,-8,-6,10,-4,6,-6,-7,-9,9,10,5,-6,-7,-1,-3,-1,-7,9,-9,-6,9,3,7,6,3,-9,-4,-9,7,7,-3,10,5,7,2,-1,7,8,-6,-8,-2,7,4,-4,8,-1,-2,-10,8,-3,1,3,5,-10,4,10,-6,2,5,-3,9,-3,-4,-10,-2,-5,6,-1,-7,-4,10,9,-4,-8,-6,1,4,8,1,-10,-2,4,-3,1,-7,-3,10,2,2,3,8,3,2,-10,3,3,-5,3,3,7,10,6,-1,-4,-8,-9,2,10,7,-4,10,-6,-8,2,-5,-3,9,5,-8,1,7,-4,-5,-1,-2,1,-6,-8,7,8,-9,9,10,7,4,-6,1,-9,2,-7,9,-10,-8,-9,-8,-7,8,6,1,-10,3,-5,5,9,6,-6,7,-9,-2,-9,5,-7,1,5,-7,8,-2,-6,-9,-6,2,-9,6,3,-8,8,8,8,-9,3,9,-7,4,-8,8,-7,4,1,-8,7,9,-9,1,6,2,5,3,-2,7,10,-2,8,-7,-5,5,8,7,1,-7,-7,8,-2,-6,-8,4,8,8,-3,7,9,2,-6], dtype = "int32")#candidate|4524|(585,)|const|int32
call_4523 = relay.TupleGetItem(func_4323_call(relay.reshape(const_4524.astype('int32'), [15, 3, 13])), 1)
call_4525 = relay.TupleGetItem(func_4326_call(relay.reshape(const_4524.astype('int32'), [15, 3, 13])), 1)
output = relay.Tuple([call_4508,call_4523,const_4524,])
output2 = relay.Tuple([call_4509,call_4525,const_4524,])
func_4526 = relay.Function([], output)
mod['func_4526'] = func_4526
mod = relay.transform.InferType()(mod)
output = func_4526()
func_4527 = relay.Function([], output)
mutated_mod['func_4527'] = func_4527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_4530 = relay.TupleGetItem(func_580_call(), 1)
call_4531 = relay.TupleGetItem(func_582_call(), 1)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_4534 = relay.TupleGetItem(func_501_call(), 0)
call_4535 = relay.TupleGetItem(func_503_call(), 0)
bop_4538 = relay.bitwise_and(call_4530.astype('int64'), relay.reshape(call_4534.astype('int64'), relay.shape_of(call_4530))) # shape=(9, 6, 2)
bop_4541 = relay.bitwise_and(call_4531.astype('int64'), relay.reshape(call_4535.astype('int64'), relay.shape_of(call_4531))) # shape=(9, 6, 2)
func_1891_call = mod.get_global_var('func_1891')
func_1895_call = mutated_mod.get_global_var('func_1895')
var_4556 = relay.var("var_4556", dtype = "bool", shape = (525,))#candidate|4556|(525,)|var|bool
call_4555 = func_1891_call(relay.reshape(var_4556.astype('bool'), [7, 15, 5]), relay.reshape(var_4556.astype('bool'), [7, 15, 5]), )
call_4557 = func_1891_call(relay.reshape(var_4556.astype('bool'), [7, 15, 5]), relay.reshape(var_4556.astype('bool'), [7, 15, 5]), )
func_349_call = mod.get_global_var('func_349')
func_355_call = mutated_mod.get_global_var('func_355')
var_4560 = relay.var("var_4560", dtype = "float32", shape = (252,))#candidate|4560|(252,)|var|float32
const_4561 = relay.const([-7.407657,-6.462300,-5.948509,-1.687638,-9.550146,-9.556238,4.267367,9.837049,-9.708419,2.761249,8.708762,-3.233783,8.508058,-5.799259,-6.412037,4.859363,-3.414991,6.967968,0.060718,0.214203,-3.596873,-1.612554,-8.334066,-3.691131,-1.403711,4.009363,-1.363557,-2.713455,3.648998,-3.149099,-6.327878,5.093069,-1.894187,8.932987,-6.690204,5.804423,-6.052355,-9.293422,4.006514,8.730905,-5.611434,-5.760569,6.363472,5.237775,2.373339,-5.056707,5.025809,3.648341,-1.944623,6.007193,6.954945,4.618297,-3.679065,-3.798434,-3.362598,6.615257,9.514859,5.211301,-8.922985,1.760836,1.497252,8.318460,9.887048,-3.455335,-0.883654,3.640861,-2.473980,3.060034,-8.065889,-9.295921,-6.876080,-3.672492,8.456549,-9.572518,-1.141950,-1.959497,3.269191,-8.501823,-9.743306,-5.198212,-8.133409,-9.724673,0.085622,1.497593,-5.560658,-3.066411,-9.734742,-4.572444,0.594735,0.942120,-4.746523,9.087190,-4.712161,5.878361,-2.843741,2.302829,1.590170,3.113682,6.590272,-4.793435,-9.908946,-5.414748,7.403678,8.431950,3.428661,-8.204557,-4.176695,7.229717,6.159919,0.825278,9.832128,-9.681251,-7.851459,2.287533,1.899759,7.839836,-2.746904,-4.243589,-5.341041,-9.623789,-3.529984,-2.077237,-4.788441,7.960241,-3.922560,3.394264,9.483893,-9.647368,3.501301,-5.651058,3.325803,4.396243,5.009590,-8.964073,0.194891,-7.316492,5.978686,-6.149879,-2.026818,-7.896271], dtype = "float64")#candidate|4561|(140,)|const|float64
call_4559 = relay.TupleGetItem(func_349_call(relay.reshape(var_4560.astype('float32'), [14, 2, 9]), relay.reshape(var_4560.astype('float32'), [14, 2, 9]), relay.reshape(call_4530.astype('float32'), [108,]), relay.reshape(const_4561.astype('float64'), [140,]), ), 1)
call_4562 = relay.TupleGetItem(func_355_call(relay.reshape(var_4560.astype('float32'), [14, 2, 9]), relay.reshape(var_4560.astype('float32'), [14, 2, 9]), relay.reshape(call_4530.astype('float32'), [108,]), relay.reshape(const_4561.astype('float64'), [140,]), ), 1)
output = relay.Tuple([bop_4538,call_4555,var_4556,call_4559,var_4560,const_4561,])
output2 = relay.Tuple([bop_4541,call_4557,var_4556,call_4562,var_4560,const_4561,])
func_4574 = relay.Function([var_4556,var_4560,], output)
mod['func_4574'] = func_4574
mod = relay.transform.InferType()(mod)
var_4575 = relay.var("var_4575", dtype = "bool", shape = (525,))#candidate|4575|(525,)|var|bool
var_4576 = relay.var("var_4576", dtype = "float32", shape = (252,))#candidate|4576|(252,)|var|float32
output = func_4574(var_4575,var_4576,)
func_4577 = relay.Function([var_4575,var_4576,], output)
mutated_mod['func_4577'] = func_4577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2007_call = mutated_mod.get_global_var('func_2007')
call_4579 = relay.TupleGetItem(func_2006_call(), 2)
call_4580 = relay.TupleGetItem(func_2007_call(), 2)
output = relay.Tuple([call_4579,])
output2 = relay.Tuple([call_4580,])
func_4582 = relay.Function([], output)
mod['func_4582'] = func_4582
mod = relay.transform.InferType()(mod)
output = func_4582()
func_4583 = relay.Function([], output)
mutated_mod['func_4583'] = func_4583
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4696 = relay.var("var_4696", dtype = "bool", shape = (14, 5, 16))#candidate|4696|(14, 5, 16)|var|bool
const_4697 = relay.const([[[False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False],[False,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True],[True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False],[True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True],[False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,True]],[[False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False],[False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,True],[False,False,False,False,True,False,True,True,False,False,True,True,False,False,True,False],[True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False],[True,False,True,False,False,False,True,False,False,False,False,False,True,True,True,False]],[[True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False],[False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True],[True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True],[False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True],[False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True]],[[True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True],[True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,True],[True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False],[True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False],[True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False]],[[True,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True],[False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False],[False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False],[True,True,True,False,True,False,False,False,False,True,True,True,True,False,True,True],[True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,False]],[[True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True],[True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,False],[False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True],[False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False],[False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False]],[[False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False],[False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,False],[True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True],[False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False],[False,True,False,False,False,True,False,False,False,False,True,True,True,True,False,True]],[[True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False],[True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True],[False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True],[True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True],[False,True,False,False,True,True,False,False,True,True,False,True,True,False,False,True]],[[True,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False],[False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True],[True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True],[True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False],[False,True,True,False,False,True,False,False,True,True,True,False,False,False,True,True]],[[True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False],[False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True],[False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False],[True,False,True,False,True,False,True,False,False,True,False,False,False,True,True,False],[True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True]],[[True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False],[False,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True],[False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False],[True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,True],[True,True,False,False,True,False,False,False,True,True,False,True,True,False,True,True]],[[False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,False],[False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True],[True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,False],[True,False,True,True,True,True,True,True,True,True,True,True,False,True,False,True],[True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False]],[[True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True],[False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False],[False,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True],[True,True,False,True,False,False,True,False,True,False,True,False,True,False,False,True],[False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,True]],[[True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False],[True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,True],[False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True],[False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,False],[False,True,True,False,True,False,False,True,True,True,True,False,False,False,True,True]]], dtype = "bool")#candidate|4697|(14, 5, 16)|const|bool
bop_4698 = relay.logical_and(var_4696.astype('bool'), relay.reshape(const_4697.astype('bool'), relay.shape_of(var_4696))) # shape=(14, 5, 16)
func_2393_call = mod.get_global_var('func_2393')
func_2394_call = mutated_mod.get_global_var('func_2394')
call_4702 = relay.TupleGetItem(func_2393_call(), 3)
call_4703 = relay.TupleGetItem(func_2394_call(), 3)
func_1847_call = mod.get_global_var('func_1847')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_4707 = func_1847_call()
call_4708 = func_1847_call()
func_2299_call = mod.get_global_var('func_2299')
func_2303_call = mutated_mod.get_global_var('func_2303')
var_4716 = relay.var("var_4716", dtype = "float64", shape = ())#candidate|4716|()|var|float64
var_4717 = relay.var("var_4717", dtype = "float64", shape = (143, 14))#candidate|4717|(143, 14)|var|float64
call_4715 = func_2299_call(relay.reshape(var_4716.astype('float64'), []), relay.reshape(var_4717.astype('float64'), [14, 11, 13]), )
call_4718 = func_2299_call(relay.reshape(var_4716.astype('float64'), []), relay.reshape(var_4717.astype('float64'), [14, 11, 13]), )
func_4238_call = mod.get_global_var('func_4238')
func_4239_call = mutated_mod.get_global_var('func_4239')
call_4719 = relay.TupleGetItem(func_4238_call(), 1)
call_4720 = relay.TupleGetItem(func_4239_call(), 1)
func_2966_call = mod.get_global_var('func_2966')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_4731 = func_2966_call()
call_4732 = func_2966_call()
func_4080_call = mod.get_global_var('func_4080')
func_4081_call = mutated_mod.get_global_var('func_4081')
call_4733 = relay.TupleGetItem(func_4080_call(), 2)
call_4734 = relay.TupleGetItem(func_4081_call(), 2)
output = relay.Tuple([bop_4698,call_4702,call_4707,call_4715,var_4716,var_4717,call_4719,call_4731,call_4733,])
output2 = relay.Tuple([bop_4698,call_4703,call_4708,call_4718,var_4716,var_4717,call_4720,call_4732,call_4734,])
func_4739 = relay.Function([var_4696,var_4716,var_4717,], output)
mod['func_4739'] = func_4739
mod = relay.transform.InferType()(mod)
mutated_mod['func_4739'] = func_4739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4739_call = mutated_mod.get_global_var('func_4739')
var_4741 = relay.var("var_4741", dtype = "bool", shape = (14, 5, 16))#candidate|4741|(14, 5, 16)|var|bool
var_4742 = relay.var("var_4742", dtype = "float64", shape = ())#candidate|4742|()|var|float64
var_4743 = relay.var("var_4743", dtype = "float64", shape = (143, 14))#candidate|4743|(143, 14)|var|float64
call_4740 = func_4739_call(var_4741,var_4742,var_4743,)
output = call_4740
func_4744 = relay.Function([var_4741,var_4742,var_4743,], output)
mutated_mod['func_4744'] = func_4744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_4779 = relay.TupleGetItem(func_2777_call(), 1)
call_4780 = relay.TupleGetItem(func_2778_call(), 1)
output = relay.Tuple([call_4779,])
output2 = relay.Tuple([call_4780,])
func_4784 = relay.Function([], output)
mod['func_4784'] = func_4784
mod = relay.transform.InferType()(mod)
mutated_mod['func_4784'] = func_4784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4784_call = mutated_mod.get_global_var('func_4784')
call_4785 = func_4784_call()
output = call_4785
func_4786 = relay.Function([], output)
mutated_mod['func_4786'] = func_4786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3791_call = mutated_mod.get_global_var('func_3791')
call_4808 = relay.TupleGetItem(func_3789_call(), 0)
call_4809 = relay.TupleGetItem(func_3791_call(), 0)
output = relay.Tuple([call_4808,])
output2 = relay.Tuple([call_4809,])
func_4839 = relay.Function([], output)
mod['func_4839'] = func_4839
mod = relay.transform.InferType()(mod)
mutated_mod['func_4839'] = func_4839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4839_call = mutated_mod.get_global_var('func_4839')
call_4840 = func_4839_call()
output = call_4840
func_4841 = relay.Function([], output)
mutated_mod['func_4841'] = func_4841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_4859 = relay.TupleGetItem(func_1321_call(), 1)
call_4860 = relay.TupleGetItem(func_1323_call(), 1)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_4863 = func_4130_call()
call_4864 = func_4130_call()
func_2940_call = mod.get_global_var('func_2940')
func_2943_call = mutated_mod.get_global_var('func_2943')
call_4896 = relay.TupleGetItem(func_2940_call(relay.reshape(call_4863.astype('int8'), [9, 6, 2])), 2)
call_4897 = relay.TupleGetItem(func_2943_call(relay.reshape(call_4863.astype('int8'), [9, 6, 2])), 2)
output = relay.Tuple([call_4859,call_4863,call_4896,])
output2 = relay.Tuple([call_4860,call_4864,call_4897,])
func_4931 = relay.Function([], output)
mod['func_4931'] = func_4931
mod = relay.transform.InferType()(mod)
output = func_4931()
func_4932 = relay.Function([], output)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_4949 = func_1385_call()
call_4950 = func_1385_call()
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_4963 = relay.TupleGetItem(func_1149_call(), 3)
call_4964 = relay.TupleGetItem(func_1150_call(), 3)
var_4968 = relay.var("var_4968", dtype = "float64", shape = (6, 140))#candidate|4968|(6, 140)|var|float64
bop_4969 = relay.not_equal(call_4963.astype('bool'), var_4968.astype('bool')) # shape=(6, 140)
bop_4972 = relay.not_equal(call_4964.astype('bool'), var_4968.astype('bool')) # shape=(6, 140)
output = relay.Tuple([call_4949,bop_4969,])
output2 = relay.Tuple([call_4950,bop_4972,])
func_4973 = relay.Function([var_4968,], output)
mod['func_4973'] = func_4973
mod = relay.transform.InferType()(mod)
mutated_mod['func_4973'] = func_4973
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4974 = relay.var("var_4974", dtype = "float64", shape = (6, 140))#candidate|4974|(6, 140)|var|float64
func_4973_call = mutated_mod.get_global_var('func_4973')
call_4975 = func_4973_call(var_4974)
output = call_4975
func_4976 = relay.Function([var_4974], output)
mutated_mod['func_4976'] = func_4976
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5016 = relay.var("var_5016", dtype = "int8", shape = (7, 7, 16))#candidate|5016|(7, 7, 16)|var|int8
const_5017 = relay.const([[[-9,2,2,-3,2,1,6,8,-3,-1,10,1,7,-10,-2,-8],[9,-8,5,-1,-1,6,-2,-5,9,-3,-7,-1,-10,3,-7,4],[-8,-8,-4,-1,-1,-2,3,1,-5,-1,9,-9,2,-2,10,4],[6,2,-10,7,-1,-6,8,6,-2,-6,-8,1,-4,6,6,-1],[-9,6,-7,1,-2,2,-6,3,-3,10,-3,-1,3,2,-5,-6],[7,4,-5,-2,3,8,2,9,10,9,10,2,-7,-3,-7,-5],[-10,-10,5,3,8,7,-5,-9,6,10,-10,-7,7,7,10,-10]],[[-2,-5,-2,5,2,-10,-10,1,9,-10,-4,-5,-1,-4,-6,-9],[-3,-7,5,-5,-6,3,5,2,5,-2,2,-9,10,2,-8,-6],[7,5,5,-10,-6,9,-7,3,4,1,3,-7,-5,-6,-9,-5],[-6,-10,-2,-4,-3,8,-3,-2,-8,-2,-4,3,7,-2,4,5],[-8,2,3,-8,10,-6,9,-1,10,-10,-2,4,2,6,-3,-5],[3,-1,-3,5,-5,8,9,-2,1,-5,-5,-10,7,3,6,9],[7,-8,-8,-6,3,8,-1,5,10,-5,-1,2,-3,-7,4,8]],[[5,6,8,8,-5,-7,5,-8,-4,-2,10,-4,-10,1,7,9],[-3,5,4,5,10,-6,4,9,-1,-2,6,3,6,-2,-3,-5],[4,10,-5,-9,-8,9,-1,9,-1,2,-8,-5,-10,7,8,2],[6,-1,-8,6,-5,8,-5,-7,-8,6,-3,10,6,5,-1,-5],[10,10,6,3,-10,5,-8,4,1,-9,10,6,-9,1,9,-9],[-2,8,-4,9,-2,1,-9,5,6,-2,5,2,2,-4,-9,-1],[-1,-1,2,8,6,-5,6,-5,-3,-7,-9,-10,2,4,-8,-4]],[[-6,3,7,-1,1,-10,-3,9,3,4,-7,-5,-10,-2,-3,-7],[-3,6,-2,-5,-2,-1,-9,3,-8,-8,-1,6,1,10,-4,5],[-5,-7,8,9,-6,-5,3,-9,-4,6,1,7,-7,5,1,-9],[1,-5,-8,6,-7,9,10,-10,6,-2,-5,-8,-7,6,-5,6],[10,2,8,-2,-1,-6,10,7,-10,-4,1,9,-6,-6,1,4],[5,-9,-6,-9,-3,-9,-1,-8,9,-7,-5,6,3,-10,-4,-6],[-2,2,-10,-6,8,-4,4,-9,8,-3,4,2,-1,-4,1,-4]],[[6,3,-8,9,-4,2,-8,3,7,-7,-3,-8,3,9,-1,7],[8,-5,8,-2,-8,-2,-5,10,-9,5,-6,-8,5,3,10,-7],[-9,-7,-8,-1,3,-1,-8,-4,-10,1,-2,-4,-6,-6,8,-5],[8,8,-10,2,-4,-6,6,1,7,-1,-3,-7,-4,5,4,3],[-3,8,9,9,-3,-8,-2,-4,-5,9,9,-8,7,-9,5,-5],[-2,-2,-2,-8,5,-5,-5,8,-3,-7,-5,7,8,4,-9,-2],[3,6,4,-2,10,-5,-6,6,-2,-2,-7,8,9,1,-5,1]],[[-6,5,10,10,-5,-4,10,10,2,10,3,9,1,7,2,4],[-6,-1,-6,-6,-5,-2,2,-8,4,-6,-7,-8,-4,6,5,-7],[1,-7,8,-8,8,10,3,-4,6,-5,-6,3,8,-9,9,3],[-3,-7,-6,6,6,-3,3,-8,-1,4,-4,9,-4,4,-6,3],[9,-2,4,8,5,-1,-1,7,-1,-9,-8,8,1,-7,-3,6],[-10,-7,-10,8,-8,-2,-7,-9,2,5,10,-1,-9,6,9,-4],[-4,-5,7,8,2,2,-10,10,-1,-1,-10,10,1,3,-9,10]],[[9,-8,1,-10,5,-4,3,7,9,-4,10,-2,1,-2,-2,6],[10,-8,1,5,7,2,-3,5,7,-3,-7,-10,10,-1,-6,6],[4,-8,9,10,3,10,-1,8,-6,6,7,2,-10,2,1,-2],[3,9,-5,9,-10,-4,4,10,-6,-3,-2,10,7,8,1,4],[-9,-5,-3,2,3,-6,-1,-9,3,-10,5,7,-2,-4,4,-5],[3,9,4,1,1,-6,-6,-9,-7,3,9,-5,-6,1,9,7],[6,7,-9,-9,8,5,10,-2,-5,8,9,-2,-4,-5,1,-4]]], dtype = "int8")#candidate|5017|(7, 7, 16)|const|int8
bop_5018 = relay.left_shift(var_5016.astype('int8'), relay.reshape(const_5017.astype('int8'), relay.shape_of(var_5016))) # shape=(7, 7, 16)
func_2594_call = mod.get_global_var('func_2594')
func_2596_call = mutated_mod.get_global_var('func_2596')
var_5023 = relay.var("var_5023", dtype = "float64", shape = (140,))#candidate|5023|(140,)|var|float64
call_5022 = relay.TupleGetItem(func_2594_call(relay.reshape(var_5023.astype('float64'), [140,])), 0)
call_5024 = relay.TupleGetItem(func_2596_call(relay.reshape(var_5023.astype('float64'), [140,])), 0)
func_4526_call = mod.get_global_var('func_4526')
func_4527_call = mutated_mod.get_global_var('func_4527')
call_5025 = relay.TupleGetItem(func_4526_call(), 0)
call_5026 = relay.TupleGetItem(func_4527_call(), 0)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_5052 = relay.TupleGetItem(func_937_call(), 1)
call_5053 = relay.TupleGetItem(func_939_call(), 1)
func_2006_call = mod.get_global_var('func_2006')
func_2007_call = mutated_mod.get_global_var('func_2007')
call_5061 = relay.TupleGetItem(func_2006_call(), 2)
call_5062 = relay.TupleGetItem(func_2007_call(), 2)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_5068 = func_1385_call()
call_5069 = func_1385_call()
func_2393_call = mod.get_global_var('func_2393')
func_2394_call = mutated_mod.get_global_var('func_2394')
call_5079 = relay.TupleGetItem(func_2393_call(), 3)
call_5080 = relay.TupleGetItem(func_2394_call(), 3)
func_4784_call = mod.get_global_var('func_4784')
func_4786_call = mutated_mod.get_global_var('func_4786')
call_5083 = relay.TupleGetItem(func_4784_call(), 0)
call_5084 = relay.TupleGetItem(func_4786_call(), 0)
output = relay.Tuple([bop_5018,call_5022,var_5023,call_5025,call_5052,call_5061,call_5068,call_5079,call_5083,])
output2 = relay.Tuple([bop_5018,call_5024,var_5023,call_5026,call_5053,call_5062,call_5069,call_5080,call_5084,])
func_5089 = relay.Function([var_5016,var_5023,], output)
mod['func_5089'] = func_5089
mod = relay.transform.InferType()(mod)
var_5090 = relay.var("var_5090", dtype = "int8", shape = (7, 7, 16))#candidate|5090|(7, 7, 16)|var|int8
var_5091 = relay.var("var_5091", dtype = "float64", shape = (140,))#candidate|5091|(140,)|var|float64
output = func_5089(var_5090,var_5091,)
func_5092 = relay.Function([var_5090,var_5091,], output)
mutated_mod['func_5092'] = func_5092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_5102 = relay.TupleGetItem(func_1149_call(), 0)
call_5103 = relay.TupleGetItem(func_1150_call(), 0)
func_4304_call = mod.get_global_var('func_4304')
func_4306_call = mutated_mod.get_global_var('func_4306')
call_5109 = func_4304_call()
call_5110 = func_4304_call()
func_4238_call = mod.get_global_var('func_4238')
func_4239_call = mutated_mod.get_global_var('func_4239')
call_5111 = relay.TupleGetItem(func_4238_call(), 0)
call_5112 = relay.TupleGetItem(func_4239_call(), 0)
output = relay.Tuple([call_5102,call_5109,call_5111,])
output2 = relay.Tuple([call_5103,call_5110,call_5112,])
func_5121 = relay.Function([], output)
mod['func_5121'] = func_5121
mod = relay.transform.InferType()(mod)
output = func_5121()
func_5122 = relay.Function([], output)
mutated_mod['func_5122'] = func_5122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_5156 = func_121_call()
call_5157 = func_121_call()
func_3789_call = mod.get_global_var('func_3789')
func_3791_call = mutated_mod.get_global_var('func_3791')
call_5158 = relay.TupleGetItem(func_3789_call(), 3)
call_5159 = relay.TupleGetItem(func_3791_call(), 3)
bop_5173 = relay.bitwise_xor(call_5158.astype('int16'), relay.reshape(call_5156.astype('int16'), relay.shape_of(call_5158))) # shape=(9, 6, 2)
bop_5176 = relay.bitwise_xor(call_5159.astype('int16'), relay.reshape(call_5157.astype('int16'), relay.shape_of(call_5159))) # shape=(9, 6, 2)
output = bop_5173
output2 = bop_5176
func_5180 = relay.Function([], output)
mod['func_5180'] = func_5180
mod = relay.transform.InferType()(mod)
output = func_5180()
func_5181 = relay.Function([], output)
mutated_mod['func_5181'] = func_5181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3094_call = mod.get_global_var('func_3094')
func_3096_call = mutated_mod.get_global_var('func_3096')
call_5194 = func_3094_call()
call_5195 = func_3094_call()
func_1921_call = mod.get_global_var('func_1921')
func_1923_call = mutated_mod.get_global_var('func_1923')
call_5196 = relay.TupleGetItem(func_1921_call(relay.reshape(call_5194.astype('float64'), [140,])), 1)
call_5197 = relay.TupleGetItem(func_1923_call(relay.reshape(call_5194.astype('float64'), [140,])), 1)
output = relay.Tuple([call_5194,call_5196,])
output2 = relay.Tuple([call_5195,call_5197,])
func_5221 = relay.Function([], output)
mod['func_5221'] = func_5221
mod = relay.transform.InferType()(mod)
mutated_mod['func_5221'] = func_5221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5221_call = mutated_mod.get_global_var('func_5221')
call_5222 = func_5221_call()
output = call_5222
func_5223 = relay.Function([], output)
mutated_mod['func_5223'] = func_5223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_5227 = relay.TupleGetItem(func_1321_call(), 0)
call_5228 = relay.TupleGetItem(func_1323_call(), 0)
output = call_5227
output2 = call_5228
func_5231 = relay.Function([], output)
mod['func_5231'] = func_5231
mod = relay.transform.InferType()(mod)
mutated_mod['func_5231'] = func_5231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5231_call = mutated_mod.get_global_var('func_5231')
call_5232 = func_5231_call()
output = call_5232
func_5233 = relay.Function([], output)
mutated_mod['func_5233'] = func_5233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_5299 = relay.TupleGetItem(func_1321_call(), 1)
call_5300 = relay.TupleGetItem(func_1323_call(), 1)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_5326 = relay.TupleGetItem(func_1321_call(), 1)
call_5327 = relay.TupleGetItem(func_1323_call(), 1)
func_3992_call = mod.get_global_var('func_3992')
func_3993_call = mutated_mod.get_global_var('func_3993')
call_5329 = relay.TupleGetItem(func_3992_call(), 0)
call_5330 = relay.TupleGetItem(func_3993_call(), 0)
func_4839_call = mod.get_global_var('func_4839')
func_4841_call = mutated_mod.get_global_var('func_4841')
call_5349 = relay.TupleGetItem(func_4839_call(), 0)
call_5350 = relay.TupleGetItem(func_4841_call(), 0)
output = relay.Tuple([call_5299,call_5326,call_5329,call_5349,])
output2 = relay.Tuple([call_5300,call_5327,call_5330,call_5350,])
func_5357 = relay.Function([], output)
mod['func_5357'] = func_5357
mod = relay.transform.InferType()(mod)
output = func_5357()
func_5358 = relay.Function([], output)
mutated_mod['func_5358'] = func_5358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2279_call = mod.get_global_var('func_2279')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_5391 = func_2279_call()
call_5392 = func_2279_call()
func_818_call = mod.get_global_var('func_818')
func_820_call = mutated_mod.get_global_var('func_820')
call_5396 = relay.TupleGetItem(func_818_call(), 0)
call_5397 = relay.TupleGetItem(func_820_call(), 0)
output = relay.Tuple([call_5391,call_5396,])
output2 = relay.Tuple([call_5392,call_5397,])
func_5410 = relay.Function([], output)
mod['func_5410'] = func_5410
mod = relay.transform.InferType()(mod)
mutated_mod['func_5410'] = func_5410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5410_call = mutated_mod.get_global_var('func_5410')
call_5411 = func_5410_call()
output = call_5411
func_5412 = relay.Function([], output)
mutated_mod['func_5412'] = func_5412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3515_call = mod.get_global_var('func_3515')
func_3517_call = mutated_mod.get_global_var('func_3517')
call_5444 = relay.TupleGetItem(func_3515_call(), 0)
call_5445 = relay.TupleGetItem(func_3517_call(), 0)
func_3406_call = mod.get_global_var('func_3406')
func_3408_call = mutated_mod.get_global_var('func_3408')
const_5465 = relay.const([-10,-7,-7,1,-6,5,3,10,-2,-9,5,-9,7,-10,8,6,-4,-5,5,6,-2,-5,-8,-2,-3,5,9,7,-3,10,10,-1,10,-5,5,-8,4,-1,8,3,8,-9,1,-4,5,-10,-1,-1,-7,8,10,9,1,8,-7,1,10,2,-8,-8,2,7,-8,-6,5,-9,4,-10,-1,-2,-9,4,5,-1,-4,-5,8,2,2,-3,4,3,1,2,-2,-8,9,10,-2,8,-3,-4,5,-7,4,4,-1,5,-10,3,1,-3,-5,-6,-6,-3,-7,10,-1,-1,-6,-2,-1,10,-3,-3,4,7,-1,-6,-9,-5,-6,-10,-1,-3,-5,-5,-1,10,-6,10,-9,9,4,-6,-4,9,6,-10], dtype = "uint64")#candidate|5465|(140,)|const|uint64
call_5464 = func_3406_call(relay.reshape(const_5465.astype('uint64'), [14, 2, 5]))
call_5466 = func_3406_call(relay.reshape(const_5465.astype('uint64'), [14, 2, 5]))
func_4739_call = mod.get_global_var('func_4739')
func_4744_call = mutated_mod.get_global_var('func_4744')
var_5472 = relay.var("var_5472", dtype = "bool", shape = (560, 2))#candidate|5472|(560, 2)|var|bool
var_5473 = relay.var("var_5473", dtype = "float64", shape = ())#candidate|5473|()|var|float64
var_5474 = relay.var("var_5474", dtype = "float64", shape = (2002,))#candidate|5474|(2002,)|var|float64
call_5471 = relay.TupleGetItem(func_4739_call(relay.reshape(var_5472.astype('bool'), [14, 5, 16]), relay.reshape(var_5473.astype('float64'), []), relay.reshape(var_5474.astype('float64'), [143, 14]), ), 3)
call_5475 = relay.TupleGetItem(func_4744_call(relay.reshape(var_5472.astype('bool'), [14, 5, 16]), relay.reshape(var_5473.astype('float64'), []), relay.reshape(var_5474.astype('float64'), [143, 14]), ), 3)
func_772_call = mod.get_global_var('func_772')
func_773_call = mutated_mod.get_global_var('func_773')
call_5491 = relay.TupleGetItem(func_772_call(), 1)
call_5492 = relay.TupleGetItem(func_773_call(), 1)
func_1684_call = mod.get_global_var('func_1684')
func_1686_call = mutated_mod.get_global_var('func_1686')
call_5504 = relay.TupleGetItem(func_1684_call(relay.reshape(call_5444.astype('uint32'), [9, 6, 2])), 0)
call_5505 = relay.TupleGetItem(func_1686_call(relay.reshape(call_5444.astype('uint32'), [9, 6, 2])), 0)
const_5512 = relay.const([[[5,-9,-6,-2,-1],[5,-6,6,4,9]],[[-3,2,-3,4,8],[-9,5,5,-2,-4]],[[9,4,-10,-9,6],[-8,8,-10,6,6]],[[-9,4,-5,-5,8],[-2,1,-2,-8,9]],[[1,-2,9,2,7],[7,3,10,-2,6]],[[8,-7,-4,2,-4],[-6,10,5,-2,-5]],[[5,7,-5,7,-3],[9,1,-10,7,-8]],[[5,-7,4,4,-1],[4,-3,3,7,-7]],[[-6,-2,2,-3,6],[-9,7,-5,8,-6]],[[-8,-4,-1,-9,10],[1,-2,-3,6,3]],[[-7,-2,10,5,7],[-8,4,-6,-10,5]],[[10,-4,-8,-9,4],[6,-6,-8,-6,-4]],[[-6,7,-4,-3,7],[2,4,2,-4,-8]],[[-2,-10,3,-3,-10],[-3,9,6,-3,8]]], dtype = "int32")#candidate|5512|(14, 2, 5)|const|int32
bop_5513 = relay.minimum(call_5464.astype('uint64'), relay.reshape(const_5512.astype('uint64'), relay.shape_of(call_5464))) # shape=(14, 2, 5)
bop_5516 = relay.minimum(call_5466.astype('uint64'), relay.reshape(const_5512.astype('uint64'), relay.shape_of(call_5466))) # shape=(14, 2, 5)
uop_5530 = relay.log2(call_5471.astype('float64')) # shape=(14, 11, 13)
uop_5532 = relay.log2(call_5475.astype('float64')) # shape=(14, 11, 13)
uop_5533 = relay.asinh(call_5491.astype('float32')) # shape=(9, 6, 2)
uop_5535 = relay.asinh(call_5492.astype('float32')) # shape=(9, 6, 2)
output = relay.Tuple([call_5444,const_5465,var_5472,var_5473,var_5474,call_5504,bop_5513,uop_5530,uop_5533,])
output2 = relay.Tuple([call_5445,const_5465,var_5472,var_5473,var_5474,call_5505,bop_5516,uop_5532,uop_5535,])
func_5540 = relay.Function([var_5472,var_5473,var_5474,], output)
mod['func_5540'] = func_5540
mod = relay.transform.InferType()(mod)
mutated_mod['func_5540'] = func_5540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5540_call = mutated_mod.get_global_var('func_5540')
var_5542 = relay.var("var_5542", dtype = "bool", shape = (560, 2))#candidate|5542|(560, 2)|var|bool
var_5543 = relay.var("var_5543", dtype = "float64", shape = ())#candidate|5543|()|var|float64
var_5544 = relay.var("var_5544", dtype = "float64", shape = (2002,))#candidate|5544|(2002,)|var|float64
call_5541 = func_5540_call(var_5542,var_5543,var_5544,)
output = call_5541
func_5545 = relay.Function([var_5542,var_5543,var_5544,], output)
mutated_mod['func_5545'] = func_5545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_5585 = func_121_call()
call_5586 = func_121_call()
output = relay.Tuple([call_5585,])
output2 = relay.Tuple([call_5586,])
func_5597 = relay.Function([], output)
mod['func_5597'] = func_5597
mod = relay.transform.InferType()(mod)
output = func_5597()
func_5598 = relay.Function([], output)
mutated_mod['func_5598'] = func_5598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_5620 = func_2204_call()
call_5621 = func_2204_call()
var_5626 = relay.var("var_5626", dtype = "uint64", shape = (14, 2, 5))#candidate|5626|(14, 2, 5)|var|uint64
bop_5627 = relay.divide(call_5620.astype('float64'), relay.reshape(var_5626.astype('float64'), relay.shape_of(call_5620))) # shape=(14, 2, 5)
bop_5630 = relay.divide(call_5621.astype('float64'), relay.reshape(var_5626.astype('float64'), relay.shape_of(call_5621))) # shape=(14, 2, 5)
output = bop_5627
output2 = bop_5630
func_5632 = relay.Function([var_5626,], output)
mod['func_5632'] = func_5632
mod = relay.transform.InferType()(mod)
var_5633 = relay.var("var_5633", dtype = "uint64", shape = (14, 2, 5))#candidate|5633|(14, 2, 5)|var|uint64
output = func_5632(var_5633)
func_5634 = relay.Function([var_5633], output)
mutated_mod['func_5634'] = func_5634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_5663 = func_4130_call()
call_5664 = func_4130_call()
func_3515_call = mod.get_global_var('func_3515')
func_3517_call = mutated_mod.get_global_var('func_3517')
call_5667 = relay.TupleGetItem(func_3515_call(), 0)
call_5668 = relay.TupleGetItem(func_3517_call(), 0)
output = relay.Tuple([call_5663,call_5667,])
output2 = relay.Tuple([call_5664,call_5668,])
func_5671 = relay.Function([], output)
mod['func_5671'] = func_5671
mod = relay.transform.InferType()(mod)
mutated_mod['func_5671'] = func_5671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5671_call = mutated_mod.get_global_var('func_5671')
call_5672 = func_5671_call()
output = call_5672
func_5673 = relay.Function([], output)
mutated_mod['func_5673'] = func_5673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_818_call = mod.get_global_var('func_818')
func_820_call = mutated_mod.get_global_var('func_820')
call_5693 = relay.TupleGetItem(func_818_call(), 1)
call_5694 = relay.TupleGetItem(func_820_call(), 1)
var_5706 = relay.var("var_5706", dtype = "int8", shape = (9, 6, 2))#candidate|5706|(9, 6, 2)|var|int8
bop_5707 = relay.greater(call_5693.astype('bool'), relay.reshape(var_5706.astype('bool'), relay.shape_of(call_5693))) # shape=(9, 6, 2)
bop_5710 = relay.greater(call_5694.astype('bool'), relay.reshape(var_5706.astype('bool'), relay.shape_of(call_5694))) # shape=(9, 6, 2)
output = bop_5707
output2 = bop_5710
func_5743 = relay.Function([var_5706,], output)
mod['func_5743'] = func_5743
mod = relay.transform.InferType()(mod)
mutated_mod['func_5743'] = func_5743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5744 = relay.var("var_5744", dtype = "int8", shape = (9, 6, 2))#candidate|5744|(9, 6, 2)|var|int8
func_5743_call = mutated_mod.get_global_var('func_5743')
call_5745 = func_5743_call(var_5744)
output = call_5745
func_5746 = relay.Function([var_5744], output)
mutated_mod['func_5746'] = func_5746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4582_call = mod.get_global_var('func_4582')
func_4583_call = mutated_mod.get_global_var('func_4583')
call_5748 = relay.TupleGetItem(func_4582_call(), 0)
call_5749 = relay.TupleGetItem(func_4583_call(), 0)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_5750 = relay.TupleGetItem(func_4931_call(), 0)
call_5751 = relay.TupleGetItem(func_4932_call(), 0)
output = relay.Tuple([call_5748,call_5750,])
output2 = relay.Tuple([call_5749,call_5751,])
func_5755 = relay.Function([], output)
mod['func_5755'] = func_5755
mod = relay.transform.InferType()(mod)
mutated_mod['func_5755'] = func_5755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5755_call = mutated_mod.get_global_var('func_5755')
call_5756 = func_5755_call()
output = call_5756
func_5757 = relay.Function([], output)
mutated_mod['func_5757'] = func_5757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_121_call = mod.get_global_var('func_121')
func_123_call = mutated_mod.get_global_var('func_123')
call_5761 = func_121_call()
call_5762 = func_121_call()
func_863_call = mod.get_global_var('func_863')
func_866_call = mutated_mod.get_global_var('func_866')
const_5776 = relay.const([[-4.829361],[3.163863],[2.176502],[-9.776805],[-2.006817],[-1.031883],[-9.835676],[-5.483540],[-6.552534],[7.889998],[4.963170],[-9.205559],[2.103407],[0.830755],[-3.500122],[-8.552003],[0.016513],[6.524951],[-8.419860],[-6.416783],[8.066972],[-2.850587],[5.920842],[-6.380198],[-4.126648],[-2.747485],[-7.705132],[3.274012],[-7.173348],[6.727440],[-2.161193],[-3.317284],[2.265422],[4.840870],[9.929073],[-3.327426],[-1.224705],[-4.706715],[6.816892],[0.958718],[-9.722919],[0.170739],[-4.548673],[-2.294785],[9.220529],[-2.834670],[-0.194884],[-6.396815],[-5.153515],[0.228959],[3.756773],[-8.350194],[3.172258],[6.448656],[7.357018],[-8.443893],[-5.575492],[-9.007375],[-3.587305],[-2.593888],[-3.631206],[3.436208],[3.422879],[-1.529239],[6.610783],[1.527059],[3.818965],[1.466101],[-9.369152],[6.549775],[7.557410],[3.460193],[4.254653],[6.575493],[0.232084],[9.356379],[-5.309177],[-0.856426],[-1.233578],[1.054627],[-0.141549],[-7.933210],[-9.034136],[-8.864685],[-7.439199],[-4.106716],[1.996548],[-9.610616],[3.200244],[-0.428883],[7.463844],[-6.649343],[9.021318],[2.101166],[9.669103],[9.276568],[8.691998],[8.219962],[8.443071],[-2.629469],[1.994900],[-6.840589],[-4.549912],[7.172699],[-5.357176],[-9.450167],[7.454768],[0.038215],[8.194479],[8.095434],[2.939572],[6.553321],[-3.151444],[-4.761946],[-8.192452],[-0.109902],[7.721458],[3.922165],[2.781212],[0.940313],[-2.377923],[9.136386],[-6.593342],[-0.662042],[6.274028],[-5.668411],[6.549259],[4.871812],[-5.559502],[1.205436],[-0.012474],[-9.030098],[-2.475420],[0.778176],[-3.023750],[3.429678],[4.677653],[-8.148187],[6.833954],[2.583365],[-1.823360],[7.911475],[2.036113],[-6.527632],[-8.434547],[0.280914],[2.890819],[-8.681335],[7.412575],[0.200519],[-9.679946],[-4.788176],[2.436648],[5.686320],[-4.222667],[1.800144],[-1.756814],[-0.686409],[5.591007],[5.423063],[-5.949152],[-6.233397],[-9.572593],[-1.926865],[-7.757475],[9.131733],[-4.842107],[-4.506907],[2.338355],[7.982377],[5.530616],[-4.324669],[1.923451],[1.749431],[8.214189],[5.361975],[3.072291],[2.535707],[-1.865120],[4.629396],[9.534239],[-9.779482],[8.599828],[0.631560],[-6.647412],[-2.740434],[9.699959],[-1.069720],[0.779552],[6.017222],[-9.574441],[-9.023102],[-0.591026],[-8.524919],[1.210303],[-2.640698],[-7.208104],[0.702931],[1.411097],[-2.304141],[9.033409],[8.283537],[-9.602236],[6.863647],[-5.892876],[-1.187793],[1.810676],[-4.959088],[5.799649],[0.645725],[8.434977],[2.865367],[-9.341883],[9.238651],[-2.631046],[3.727772],[-0.025882],[-9.999240],[-0.324147],[-8.733596],[0.477214],[-9.027710],[7.600144],[-8.190408],[4.274103],[-0.084553],[0.109308],[-8.422450],[-6.049991],[-6.099675],[-4.044227],[-2.449862],[-6.387853],[5.529357],[-2.249773],[5.768193],[-1.807644],[5.989026],[0.839424],[-4.381727],[4.222407],[2.323040],[1.925012],[-7.596063],[0.370585],[-1.742742],[-1.460345],[-2.515760],[8.496655],[-8.553760],[2.006784],[2.375181]], dtype = "float32")#candidate|5776|(252, 1)|const|float32
call_5775 = relay.TupleGetItem(func_863_call(relay.reshape(const_5776.astype('float32'), [252,])), 2)
call_5777 = relay.TupleGetItem(func_866_call(relay.reshape(const_5776.astype('float32'), [252,])), 2)
output = relay.Tuple([call_5761,call_5775,const_5776,])
output2 = relay.Tuple([call_5762,call_5777,const_5776,])
func_5781 = relay.Function([], output)
mod['func_5781'] = func_5781
mod = relay.transform.InferType()(mod)
output = func_5781()
func_5782 = relay.Function([], output)
mutated_mod['func_5782'] = func_5782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3094_call = mod.get_global_var('func_3094')
func_3096_call = mutated_mod.get_global_var('func_3096')
call_5805 = func_3094_call()
call_5806 = func_3094_call()
func_4839_call = mod.get_global_var('func_4839')
func_4841_call = mutated_mod.get_global_var('func_4841')
call_5844 = relay.TupleGetItem(func_4839_call(), 0)
call_5845 = relay.TupleGetItem(func_4841_call(), 0)
func_3315_call = mod.get_global_var('func_3315')
func_3316_call = mutated_mod.get_global_var('func_3316')
call_5849 = func_3315_call()
call_5850 = func_3315_call()
uop_5857 = relay.rsqrt(call_5849.astype('float64')) # shape=(9, 6, 2)
uop_5859 = relay.rsqrt(call_5850.astype('float64')) # shape=(9, 6, 2)
func_5089_call = mod.get_global_var('func_5089')
func_5092_call = mutated_mod.get_global_var('func_5092')
const_5873 = relay.const([9,-9,-2,-8,-10,-1,-2,10,-9,6,-9,2,3,-3,1,-1,4,9,4,2,8,10,-10,-1,5,2,8,-8,-2,-1,7,-3,-3,-6,-10,3,-2,9,3,4,9,-4,1,-9,-6,-8,-4,3,5,-6,-8,4,-4,-3,-5,7,-10,-3,4,6,4,-5,6,6,7,-6,-3,-4,-5,3,1,-6,-10,4,2,-8,-5,-5,-10,2,-6,-4,-1,5,-5,-8,10,-7,-4,6,2,-2,-6,-8,1,8,8,-4,10,7,-2,2,-10,2,-2,1,4,-3,-2,9,-10,-9,-8,-9,6,6,2,8,6,7,-10,-2,-2,5,5,-7,2,3,-3,-10,10,-7,-3,4,4,-7,-10,9,3,7,-9,-3,4,-10,-10,-6,-8,3,-7,-1,10,7,7,3,-9,10,-9,-8,-10,-10,1,-3,6,-2,-2,-5,-1,4,6,7,-10,-3,1,1,-10,-4,-4,3,2,4,8,-6,-10,6,10,3,-2,8,-10,5,-8,2,-5,-4,10,-10,-5,-9,9,-3,9,-6,4,2,-10,5,-5,10,4,6,-1,-4,3,3,9,8,2,8,-5,-4,-7,-5,-8,4,-10,-7,5,7,-5,9,-6,1,-8,-8,9,-1,10,3,-10,9,-7,1,10,-1,10,-8,-4,4,7,-6,3,7,3,1,-6,5,9,-5,-6,3,-4,-2,-9,2,-10,6,-8,-7,10,-8,10,-10,-1,-7,1,3,-8,-6,3,7,-8,7,4,9,-5,2,10,4,5,10,-9,3,-10,-8,-5,-6,-8,9,10,7,4,-9,-9,8,6,2,-5,-7,-4,-7,10,3,10,-1,9,4,-9,-8,9,4,5,1,3,-4,2,5,9,-1,10,-9,-2,-2,7,-1,7,-2,-3,4,-2,10,-2,-8,-3,-1,-3,-1,3,-7,-3,-7,-4,-5,-3,-3,-9,-10,10,-3,-7,5,3,6,-9,-6,-1,-5,5,4,-10,4,-1,-2,2,-3,8,-10,6,-8,-1,9,1,-9,-7,4,-9,9,-5,-1,4,8,4,4,-6,-8,7,10,-5,-4,-3,10,-9,2,-7,2,6,5,8,3,2,-2,9,6,-3,6,9,10,4,3,-4,5,3,-2,-9,-6,6,-9,1,1,-8,-4,3,-6,-5,-10,-3,10,5,8,1,-5,3,-4,-3,-2,3,7,-9,5,-1,-4,-2,-10,-10,-2,-4,8,3,6,10,-7,4,-1,7,9,-2,2,-1,10,-3,-4,9,4,5,-10,-8,6,-8,-6,-4,3,-2,-10,7,6,-4,7,-10,7,-1,-10,3,2,4,8,-5,-4,6,-9,5,3,4,5,10,-1,1,1,-9,7,3,1,-6,4,-10,7,8,7,1,-8,-5,6,-2,2,-2,-5,6,-2,3,-6,-10,-2,-6,-10,2,10,9,-5,-4,2,-8,2,3,6,-1,2,-7,10,5,10,2,-7,7,1,1,-9,10,-2,-7,-10,-1,2,7,1,3,-1,3,-5,-2,-4,-8,1,-4,1,-1,10,5,2,-3,6,-6,9,7,-2,10,1,8,-8,-6,2,1,-1,-1,8,6,9,3,3,-4,8,-2,-2,4,3,-10,-7,-6,-7,1,-10,-1,1,9,-3,-3,-4,1,-5,7,-5,2,8,-2,4,2,10,-5,9,-7,6,5,-4,10,-1,9,4,10,9,6,-3,9,4,-6,-9,-7,-2,-7,-1,6,-3,-10,6,10,-9,-9,5,-10,2,-3,-9,-6,-7,9,-1,1,-10,3,-10,3,9,4,8,4,9,2,2,-1,2,-6,-5,-1,8,4,6,7,-7,-1,6,8,-5,-7,8,-5,-10,-7,7,-3,-1,3,2,5,3,-6,-3,6,5,-6,-1,-7,-1,-5,10,1,5,-9,4,-8,-9,-7,1,2,-7,10,9,-9,10,7,4,-3,4,5,5,-8,-10,-1,-8,-6,1,-3,3,-1,7,-5,9,-1,-2,-4,10,3,7,-10,7,8,-1,-8,-4,-9,10,2,-4,4,-9,-2,10,-10,1,2,7,-6,2,3,7,-6,8,6,-3,7,-9,-3,-6,8,5,5,-3,-2,-7], dtype = "int8")#candidate|5873|(784,)|const|int8
call_5872 = relay.TupleGetItem(func_5089_call(relay.reshape(const_5873.astype('int8'), [7, 7, 16]), relay.reshape(call_5844.astype('float64'), [140,]), ), 8)
call_5874 = relay.TupleGetItem(func_5092_call(relay.reshape(const_5873.astype('int8'), [7, 7, 16]), relay.reshape(call_5844.astype('float64'), [140,]), ), 8)
output = relay.Tuple([call_5805,call_5844,uop_5857,call_5872,const_5873,])
output2 = relay.Tuple([call_5806,call_5845,uop_5859,call_5874,const_5873,])
func_5876 = relay.Function([], output)
mod['func_5876'] = func_5876
mod = relay.transform.InferType()(mod)
output = func_5876()
func_5877 = relay.Function([], output)
mutated_mod['func_5877'] = func_5877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_5883 = relay.TupleGetItem(func_1149_call(), 0)
call_5884 = relay.TupleGetItem(func_1150_call(), 0)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_5930 = relay.TupleGetItem(func_4931_call(), 0)
call_5931 = relay.TupleGetItem(func_4932_call(), 0)
uop_5953 = relay.sigmoid(call_5930.astype('float64')) # shape=(140,)
uop_5955 = relay.sigmoid(call_5931.astype('float64')) # shape=(140,)
uop_5959 = relay.sqrt(uop_5953.astype('float32')) # shape=(140,)
uop_5961 = relay.sqrt(uop_5955.astype('float32')) # shape=(140,)
func_4839_call = mod.get_global_var('func_4839')
func_4841_call = mutated_mod.get_global_var('func_4841')
call_5989 = relay.TupleGetItem(func_4839_call(), 0)
call_5990 = relay.TupleGetItem(func_4841_call(), 0)
bop_6002 = relay.floor_divide(call_5930.astype('float64'), relay.reshape(call_5989.astype('float64'), relay.shape_of(call_5930))) # shape=(140,)
bop_6005 = relay.floor_divide(call_5931.astype('float64'), relay.reshape(call_5990.astype('float64'), relay.shape_of(call_5931))) # shape=(140,)
func_2619_call = mod.get_global_var('func_2619')
func_2621_call = mutated_mod.get_global_var('func_2621')
call_6022 = relay.TupleGetItem(func_2619_call(), 1)
call_6023 = relay.TupleGetItem(func_2621_call(), 1)
output = relay.Tuple([call_5883,uop_5959,bop_6002,call_6022,])
output2 = relay.Tuple([call_5884,uop_5961,bop_6005,call_6023,])
func_6041 = relay.Function([], output)
mod['func_6041'] = func_6041
mod = relay.transform.InferType()(mod)
output = func_6041()
func_6042 = relay.Function([], output)
mutated_mod['func_6042'] = func_6042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4238_call = mod.get_global_var('func_4238')
func_4239_call = mutated_mod.get_global_var('func_4239')
call_6052 = relay.TupleGetItem(func_4238_call(), 0)
call_6053 = relay.TupleGetItem(func_4239_call(), 0)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_6063 = relay.TupleGetItem(func_4931_call(), 2)
call_6064 = relay.TupleGetItem(func_4932_call(), 2)
func_1781_call = mod.get_global_var('func_1781')
func_1784_call = mutated_mod.get_global_var('func_1784')
const_6067 = relay.const([-5,-6,8,-7,-6,1,-10,7,-9,9,-2,4,2,8,6,-5,-8,2,-6,-8,-1,6], dtype = "int64")#candidate|6067|(22,)|const|int64
var_6068 = relay.var("var_6068", dtype = "int64", shape = (242,))#candidate|6068|(242,)|var|int64
call_6066 = relay.TupleGetItem(func_1781_call(relay.reshape(const_6067.astype('int64'), [11, 1, 2]), relay.reshape(var_6068.astype('int64'), [11, 11, 2]), ), 0)
call_6069 = relay.TupleGetItem(func_1784_call(relay.reshape(const_6067.astype('int64'), [11, 1, 2]), relay.reshape(var_6068.astype('int64'), [11, 11, 2]), ), 0)
func_5180_call = mod.get_global_var('func_5180')
func_5181_call = mutated_mod.get_global_var('func_5181')
call_6071 = func_5180_call()
call_6072 = func_5180_call()
output = relay.Tuple([call_6052,call_6063,call_6066,const_6067,var_6068,call_6071,])
output2 = relay.Tuple([call_6053,call_6064,call_6069,const_6067,var_6068,call_6072,])
func_6074 = relay.Function([var_6068,], output)
mod['func_6074'] = func_6074
mod = relay.transform.InferType()(mod)
mutated_mod['func_6074'] = func_6074
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6075 = relay.var("var_6075", dtype = "int64", shape = (242,))#candidate|6075|(242,)|var|int64
func_6074_call = mutated_mod.get_global_var('func_6074')
call_6076 = func_6074_call(var_6075)
output = call_6076
func_6077 = relay.Function([var_6075], output)
mutated_mod['func_6077'] = func_6077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_6110 = func_2204_call()
call_6111 = func_2204_call()
func_646_call = mod.get_global_var('func_646')
func_648_call = mutated_mod.get_global_var('func_648')
call_6119 = func_646_call()
call_6120 = func_646_call()
var_6131 = relay.var("var_6131", dtype = "uint64", shape = (14, 2, 5))#candidate|6131|(14, 2, 5)|var|uint64
bop_6132 = relay.not_equal(call_6110.astype('bool'), relay.reshape(var_6131.astype('bool'), relay.shape_of(call_6110))) # shape=(14, 2, 5)
bop_6135 = relay.not_equal(call_6111.astype('bool'), relay.reshape(var_6131.astype('bool'), relay.shape_of(call_6111))) # shape=(14, 2, 5)
output = relay.Tuple([call_6119,bop_6132,])
output2 = relay.Tuple([call_6120,bop_6135,])
func_6139 = relay.Function([var_6131,], output)
mod['func_6139'] = func_6139
mod = relay.transform.InferType()(mod)
mutated_mod['func_6139'] = func_6139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6140 = relay.var("var_6140", dtype = "uint64", shape = (14, 2, 5))#candidate|6140|(14, 2, 5)|var|uint64
func_6139_call = mutated_mod.get_global_var('func_6139')
call_6141 = func_6139_call(var_6140)
output = call_6141
func_6142 = relay.Function([var_6140], output)
mutated_mod['func_6142'] = func_6142
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6164 = relay.const([[[7.456642,-8.282937,-3.174163,-6.812334,8.969032,2.591580,-4.607914,0.310854,5.851736,7.370941,5.662180,9.598694,-4.829741],[9.060820,6.061612,-3.281622,-2.561289,3.589067,1.968570,2.422227,-2.208878,5.931473,5.621644,6.295369,-1.912952,6.679729],[-4.428498,-0.638896,-8.123943,-9.602646,-8.887074,-2.112738,4.722108,8.827363,6.552514,7.848150,5.144905,8.890807,7.900597],[4.021162,5.788029,7.132010,-0.898671,-5.500168,3.336940,-9.980682,2.303348,2.027544,9.252741,-6.319786,1.254322,-8.913575]],[[-0.073616,-8.366669,-9.126058,6.727533,-5.024668,3.367738,-8.850355,-2.539560,-8.560087,0.571507,0.131371,-9.593819,8.202523],[-0.324275,-4.486636,8.871233,-6.820406,7.666682,-8.257625,-9.368201,6.971952,2.404661,9.870850,-8.077274,-2.374962,8.920232],[-9.729195,-2.386078,-9.964959,-1.609072,3.033127,3.959340,0.540266,-9.298260,8.095332,9.812842,-8.870806,-2.989006,-4.219412],[1.080842,-9.599784,-7.435638,-7.004822,-8.833218,8.742495,-8.670453,1.537150,-5.447823,-2.743081,-0.440793,3.603642,-7.037660]],[[-6.101842,4.414796,3.148516,5.376405,-7.215149,-2.656835,8.706455,5.191256,-6.266508,0.709133,-1.992712,-0.327516,1.620242],[-8.950149,-3.831449,-5.094457,-3.969708,7.967807,3.089979,4.705237,3.083791,-1.107385,5.685064,3.356301,3.895645,1.543189],[7.825740,-8.339307,-8.649269,6.287616,-6.108049,5.685384,-7.268069,-1.781375,2.745155,8.666874,-0.447348,9.129731,3.113287],[8.469595,-3.545526,-7.867820,-5.367839,-3.930645,-7.438395,-8.824940,1.706390,0.933198,-4.413718,9.002780,0.898763,-4.790918]],[[2.343275,8.163195,1.216123,4.223160,5.107417,1.418294,2.913595,-4.114212,3.775302,-9.307287,-3.201578,-3.546368,0.877591],[8.628500,-3.579083,-8.689139,5.766568,1.426272,-6.604745,-3.650293,-5.765742,-4.059081,3.287948,6.901667,3.675095,-0.262871],[1.987743,-4.390193,-5.673352,-1.284229,-3.692506,-8.762996,-7.644652,-5.154258,6.741764,6.963407,-4.081387,9.626964,-3.119929],[-7.872501,-0.806126,-0.476690,-0.448944,-4.712061,-0.201369,0.093660,-1.112721,-1.073028,1.485222,7.211853,-1.724863,2.577232]],[[-7.947528,-4.304636,4.411372,-5.302974,7.949408,-5.157397,-2.498355,7.019835,5.511943,6.773756,-3.490388,-5.139235,-3.618610],[-4.951493,-2.358798,2.975215,-2.950134,-3.972281,-5.571734,6.788699,4.690182,1.869231,8.048326,-6.654644,-2.943857,-7.368930],[9.379184,-1.817178,-0.945204,-2.212192,-2.365652,-0.001909,-9.677792,7.002823,3.550021,-3.013822,-3.865612,-0.947135,-5.633816],[-7.687960,-9.681319,-0.557777,2.481672,0.691482,4.170703,7.713879,1.242606,9.475671,-0.716470,1.752589,8.596328,-0.185739]],[[9.301933,3.241421,5.470887,-6.471332,-8.030058,4.390393,-0.370796,-8.297538,1.978439,6.027822,6.662244,-5.116833,4.380328],[1.784018,3.243386,-3.682089,9.206077,2.554065,6.620281,-8.780641,-9.062900,-6.412106,1.634883,-5.276602,-3.893144,3.535554],[-7.381749,5.348351,2.411569,5.995958,-4.949262,-0.177308,5.908393,-3.569438,7.362300,2.680483,-7.897982,-2.605074,-0.773576],[-1.126037,5.967662,-0.253843,8.450999,1.576421,-5.913635,-0.691395,0.587312,-5.197892,-9.689163,2.198076,-2.506946,5.256724]],[[-1.808707,-1.943263,-0.056758,9.552488,-4.133370,-3.048963,5.612033,1.748259,-7.800086,-2.626424,-7.598992,-4.998723,0.649292],[-5.789315,-0.786480,8.681215,-1.938363,0.682462,-9.016614,-3.489916,-9.893044,2.905190,-0.674603,-4.330102,-2.702355,-2.152068],[7.981858,0.067738,6.034293,-7.606089,4.241948,-3.291573,5.877312,-3.820900,1.152882,8.535211,4.603550,4.225500,2.299683],[-3.727116,0.739821,-9.224171,-6.930507,9.466695,7.810005,4.215480,0.209285,-0.873921,-3.098574,6.977814,4.444909,3.999679]],[[7.360606,8.569160,-0.090765,-6.648394,-1.377516,4.860652,-7.222809,-8.640748,-8.064911,-8.205448,-1.692378,6.936223,1.747637],[-1.590618,1.210578,-4.944000,-2.842890,0.791664,8.658794,-8.317583,-8.970644,-5.919319,4.994971,-8.566998,3.171670,2.571944],[-5.655972,-2.532564,7.708851,-2.945389,-5.504024,4.850216,-2.022710,-0.786747,-5.650320,-9.746629,-2.747590,8.521035,2.339165],[4.946311,-7.811605,-9.045737,7.751427,7.689351,6.303569,7.248762,-0.083878,6.904739,6.083488,-7.355077,-5.833661,-0.211366]],[[-0.540039,-4.743860,-5.524841,-2.431193,6.649085,5.577976,4.953905,6.658860,-7.142813,-5.521746,-7.119738,-0.289077,7.529338],[9.434999,9.294635,-5.682667,-4.886640,2.373653,3.084053,8.610498,5.652594,1.763353,8.071043,9.287395,-1.519940,-5.377205],[8.003819,-5.654981,-7.560844,2.579024,-6.222155,4.209011,-6.690108,9.806394,-2.842319,-0.755692,0.517309,-6.747185,5.783384],[-5.027020,6.109095,-5.693447,8.354461,-4.970291,-9.115988,1.179290,9.122695,5.662894,-9.778959,5.891044,-3.475678,-8.608522]],[[-5.739778,-5.255108,-9.460125,2.363324,-0.049269,8.702276,-8.339520,0.179579,1.383036,2.759194,0.741773,-1.264902,0.373379],[-1.114166,-9.161888,6.484656,8.877689,-5.367799,3.493846,0.078643,4.426049,7.636691,-0.803285,-6.669782,-6.152766,0.517207],[5.958633,7.568256,8.917167,-2.835402,-1.590919,-7.482926,5.300939,8.966220,-4.328873,-6.204829,8.066749,-9.792199,-8.734096],[4.094940,-2.018916,-5.561532,3.665770,6.860117,3.983738,-9.970008,5.117069,4.707344,9.486442,5.482272,-9.663943,7.440113]],[[-8.247221,4.091982,-6.937301,9.310955,9.640843,-4.012042,4.001421,-5.346332,6.026559,-4.029138,6.426764,-7.662185,-4.896198],[5.007737,4.159446,0.046070,-7.450630,1.393668,2.202759,5.155281,-1.307543,8.786753,5.165976,6.001806,-1.525382,-8.038155],[5.912201,-2.571797,-3.640278,-3.449638,-7.894430,6.856444,3.481750,-5.986366,4.033227,1.556591,0.431233,6.625919,-5.980434],[-3.878702,-3.073110,6.745589,6.257509,-5.991727,6.229782,0.589981,-0.775332,-8.121899,9.930134,-8.853358,-8.798550,6.472370]],[[5.322352,9.924591,0.011971,-0.652953,-3.547866,2.282093,-8.764376,9.277374,1.163091,6.882972,-7.861667,1.285635,-6.316947],[-3.657236,7.410957,6.272277,4.812636,1.165230,-1.472965,-3.043376,0.947324,-1.737923,5.255749,8.894530,-0.701389,-0.194294],[-0.897103,1.624489,-4.023493,3.077005,8.932519,-2.508462,8.105198,5.013136,5.425943,-7.982894,2.621179,-9.747664,3.609729],[6.932458,1.280402,-9.352487,3.390172,-6.781508,8.737923,-4.431044,-1.141433,9.760009,-3.059590,6.945021,6.782341,-9.633622]],[[-6.108749,2.375101,-0.460980,-6.701488,9.700412,9.026309,-3.028389,-4.397432,2.678752,-3.809376,0.310760,-6.364831,-1.264295],[5.910402,3.341793,-0.879804,8.112036,3.660310,3.467455,7.486434,-7.794561,1.825114,-3.654741,0.488850,-0.254710,-5.338252],[1.265850,4.589043,-8.750897,8.484278,-0.183079,-2.210190,-5.429813,1.442197,7.490445,-1.411910,2.420218,-1.358698,9.229312],[-1.340263,1.663105,3.442284,3.170401,-0.333370,6.728537,2.621832,5.291712,9.679530,-3.132638,1.230840,8.944178,7.498602]],[[-4.478663,3.672455,2.202583,1.666454,-3.643137,-1.073870,-1.491501,4.180574,-2.301900,1.921365,-6.867926,8.044747,-5.628133],[-1.347930,-1.993410,-3.389707,9.558054,-0.230234,1.257779,7.718828,-8.934350,0.932583,-9.651221,3.938993,-5.847381,2.546674],[2.871120,2.797315,9.563123,-0.650988,0.827542,-2.805101,-8.342755,-5.194594,5.874534,9.444477,9.592966,-3.766975,6.504808],[-1.433547,-4.758262,3.160850,7.317602,2.524164,-6.692579,-7.839878,1.758038,6.612458,-7.595067,2.359980,9.004736,7.829412]],[[-3.973808,5.048236,3.205975,2.656967,6.002831,-6.226192,1.355028,4.386742,9.612847,5.701729,6.911152,-2.120222,-5.894233],[9.673196,-9.970518,-5.925049,-8.679175,-8.151292,-6.325711,5.464397,-4.391756,-9.389317,-6.382294,-7.734906,7.854204,-3.249741],[-8.718738,-5.039438,-1.452320,-9.237679,9.137276,9.633154,-7.684311,0.563057,1.335886,-6.791113,-0.128809,7.381058,1.863474],[-3.869735,-9.478988,1.905304,6.797906,2.890822,0.769424,-1.805546,8.494117,-1.361385,-2.444350,-4.901859,-7.243030,5.684012]]], dtype = "float64")#candidate|6164|(15, 4, 13)|const|float64
const_6165 = relay.const([[[1.408587,-7.427998,7.753984,-3.312486,2.684322,6.242788,-7.903789,6.525844,4.630617,-5.621905,-2.066224,8.546647,3.967701],[-0.531539,5.124519,2.810965,-3.899012,-7.835111,-3.819168,-5.887180,5.069547,8.591250,-6.889926,-0.723685,8.312305,3.800557],[7.089879,-5.790780,-9.001893,-3.146635,-6.201281,0.257861,0.324570,-2.908321,-4.661777,-0.143443,-0.315532,2.956206,-8.280146],[-8.437832,9.117568,2.293882,2.779459,4.387107,-7.555626,0.112392,2.343193,1.765113,-0.598285,8.074076,-7.831602,-1.214651]],[[0.231587,6.193310,-8.563507,9.405287,5.012183,-7.993319,-3.931738,3.206604,4.655984,3.173364,0.494335,-1.210699,-2.734577],[-3.824009,3.441302,-5.268269,3.538572,-3.499260,2.642718,1.828329,-5.804993,9.930167,6.259058,-0.623433,3.702081,9.310816],[-0.182491,1.535606,7.210825,-9.695747,-8.283501,1.597693,-3.631998,3.978295,1.052253,7.285829,1.266720,-3.763319,7.641684],[8.132048,-0.925052,4.344923,-8.926816,-2.130353,-8.519279,-3.157292,4.422793,-5.279610,7.407491,2.413633,-8.977763,5.826033]],[[-2.858546,-3.700903,-6.024898,-8.755660,9.546459,2.782443,-8.696929,8.957233,-0.216098,-3.767675,-6.142767,-9.274213,-2.743650],[-3.184735,-3.584480,-2.357328,-0.327777,-0.440729,9.871276,7.259103,-1.257964,-7.765832,-6.914998,5.515803,-2.154247,-2.053489],[1.201280,-4.535470,6.825256,-0.200779,-2.099959,-8.675638,-2.508094,8.071832,5.170674,-4.161930,-5.604028,2.808961,-9.290011],[4.769757,-8.343503,0.489895,-1.965927,4.652240,5.802586,6.421519,2.831252,-9.547358,-7.970479,3.000371,-7.785640,1.412200]],[[-9.588566,-7.063306,-9.599153,8.648619,8.661513,-8.129800,7.470622,4.973395,2.428334,-2.836327,-4.181159,-4.060379,7.922254],[8.914084,0.049462,-3.417466,1.333173,2.821161,-4.383506,-4.232139,6.922256,-4.012876,-7.378315,8.068887,-9.275579,-4.458417],[-5.177296,-6.470626,-0.309924,-1.906208,-8.654103,-3.181782,2.503915,5.163925,-1.611438,1.806378,-9.123688,-2.069102,-7.524649],[3.165911,-1.982462,6.212914,-4.271981,-2.794736,1.888459,3.042772,4.304780,2.462190,0.529053,-4.306272,-0.054618,9.732498]],[[6.215913,-1.590614,-2.915319,5.979226,6.682127,8.643946,-4.053904,6.009759,-1.557283,3.899523,-9.743596,-0.007695,-4.013939],[1.035458,3.628839,9.650611,6.403953,-4.237369,4.439064,-1.506520,-8.938241,3.508105,6.949867,9.224728,4.109964,8.931099],[2.012440,5.295211,-0.483601,7.878346,5.394885,7.767551,-5.788454,-3.663233,8.270144,-6.587603,0.121013,-7.369947,-1.920539],[-3.457133,-0.402838,4.454848,-1.997385,7.740009,-4.964447,-5.173547,-3.110362,-5.009631,8.237312,-9.310832,7.256708,-8.633682]],[[-7.547359,6.805767,-9.659447,-6.655011,6.080232,3.977443,-6.346682,-5.843418,5.894485,1.287847,-0.648593,-2.553444,-0.499604],[-0.681380,2.681117,-9.159822,1.861578,3.121591,-0.854630,4.261891,7.242147,9.254959,7.556535,-3.004220,-0.213091,-6.853842],[3.691438,-1.020718,-6.564537,8.400349,0.316373,6.136453,0.157368,3.428768,9.087856,3.965716,4.892168,-5.581022,3.529214],[3.500758,-4.443782,-7.601719,-5.487103,-9.282204,-7.780487,-2.578223,8.304916,-4.487691,-7.756248,-6.434171,-0.199138,2.634223]],[[-5.881287,4.457557,-4.684991,4.285552,-8.006690,3.172443,-1.412637,3.231980,1.262120,3.131457,-9.368327,-1.712369,6.668362],[-7.596264,-1.174656,5.499652,6.782250,-5.659521,8.958646,4.118351,-1.276789,-5.864762,-6.664470,7.728544,5.536174,-7.496131],[-2.849528,8.986640,-7.176845,-7.926275,6.166033,2.338613,-4.026751,-8.903198,-2.662502,3.085479,-3.558650,8.230392,-0.196059],[4.340937,1.554375,8.171496,-2.902543,7.114154,-3.150473,8.009180,8.521837,-3.924051,7.516132,4.978023,-8.407309,-9.969995]],[[-8.325582,4.946247,-4.871574,1.629563,8.687445,1.168201,3.621088,-8.168737,-3.709931,9.601780,-0.339588,6.387410,-2.461178],[4.860247,-8.178147,-4.109529,-8.521510,2.651453,-1.660315,-9.189970,9.087269,5.767802,0.270932,-1.646632,3.423306,8.897325],[5.846409,9.292829,-6.926670,3.026308,-3.941505,2.103675,3.517378,4.689501,3.053683,2.854773,-6.634169,1.493200,-7.733501],[5.378261,0.227501,-0.201078,-9.198718,9.419218,-7.197398,4.910899,-6.301082,5.033968,2.372270,7.560785,2.990743,4.100261]],[[1.538555,6.276756,-7.023220,8.625129,7.520187,-3.440287,-7.574766,-6.977186,-8.310699,5.354678,1.143037,2.877418,-7.250812],[4.843587,6.581617,8.607224,-8.290789,2.195795,5.539973,-4.422765,-4.448800,-0.463036,-5.497738,6.671803,-7.386667,9.091531],[-5.996415,-0.298773,0.912637,-5.535634,-2.779312,8.279492,-1.319767,2.244612,-8.427692,-9.809963,6.193095,4.628532,-5.809896],[-2.685513,3.264204,-0.123884,-6.810280,-9.069165,-5.635744,8.477664,-8.416696,7.605460,9.351707,2.672367,2.125461,-4.025014]],[[-2.221167,-5.763128,-4.826459,-3.811399,4.163013,3.900241,0.997522,0.275748,-2.108032,4.063890,-8.165870,9.151990,7.272352],[8.627077,8.947401,3.808864,7.080943,-7.211337,7.574253,3.032693,3.661804,-2.320121,8.886253,-6.468364,-2.531611,-9.336457],[0.961731,-0.186217,-6.019823,3.711698,1.588881,-7.123060,-4.966395,6.135742,0.519076,-5.672599,7.948936,3.354406,1.433248],[0.720147,5.029413,-7.745628,8.368561,-9.374064,-1.828048,9.765708,-4.069523,-3.364354,-3.221934,-1.621662,-4.716302,-8.662747]],[[-3.785894,-6.672883,-8.134092,8.929077,-7.619232,-1.486872,0.477681,0.593090,-8.367728,4.665817,-1.667195,9.195226,6.259073],[-0.998241,0.225447,-7.585332,7.893559,1.483138,-7.164583,6.986887,-6.857422,-8.545755,-0.998515,7.393327,7.701837,-2.545364],[-8.197329,-1.395005,2.874346,8.716101,-9.496871,-3.100641,9.082746,3.287625,0.281124,-6.531430,-6.831612,4.208180,-2.578285],[2.044156,8.923229,-3.515561,8.600827,-1.837087,6.938325,9.205441,1.387923,6.953471,6.882529,-7.430056,-2.602621,-6.884602]],[[9.372166,1.524046,-0.359959,4.598204,-7.395428,9.810883,4.166303,4.117684,-6.861417,-0.315279,-4.965965,-0.296912,-2.761571],[-6.791865,7.077164,7.243224,-0.554514,-4.151159,5.617868,3.966298,8.446520,1.745549,-8.245719,-8.894052,-1.104840,-8.487923],[-2.749233,-8.137618,2.126578,5.921027,-7.118889,2.903636,-9.525179,8.922750,-7.590002,4.666114,-7.721003,-1.445579,8.372466],[7.292004,2.008688,2.992329,-3.669765,-5.039484,-2.564597,-5.436753,-8.275482,-8.471548,8.792042,-7.010107,-3.312238,-2.039387]],[[-4.619865,8.235198,5.223007,9.698741,-4.943340,-2.122662,3.895034,-2.643322,1.520524,-9.499531,-2.755120,-9.728693,-0.928686],[1.989099,-1.773294,2.652060,-5.920770,8.451809,8.892196,-0.889167,5.096967,-7.419633,0.860418,-0.390462,1.436823,-3.935072],[4.171502,-7.036713,1.103629,-8.778882,6.480693,2.499112,-9.276115,9.681996,0.521510,6.478565,-3.155904,6.217268,-2.099944],[-6.937446,-0.539686,-3.775749,3.118814,-0.959461,-9.141712,9.690511,-7.894170,-4.923774,7.065065,7.932866,9.420164,7.500486]],[[-7.396805,-2.817915,-3.650503,0.382639,6.602342,7.605082,-6.112480,-0.553783,-2.129188,-8.719290,-5.322443,-0.579650,-2.404798],[-5.649699,-5.363461,4.959108,8.330207,-2.104866,6.296505,-1.906597,7.204726,3.321176,2.330675,-4.184094,9.889296,7.871460],[8.043237,8.644213,2.105601,-8.260056,1.063324,-2.136425,1.512893,2.403599,-5.541428,5.291767,1.451300,1.841017,-7.574274],[-9.089591,-6.547453,6.540625,3.609516,0.632302,5.042458,6.127271,-7.326688,3.562212,-2.020386,-9.784127,-3.247832,-5.055948]],[[-4.720212,3.945833,8.420902,7.641214,8.611108,-6.568718,4.098929,0.916566,7.952523,-8.072484,-5.567387,0.530941,-7.676732],[-4.067562,5.358423,-7.590512,-8.075282,8.916460,9.687008,-6.654243,2.287117,-7.836300,-2.493701,0.340665,-8.020544,6.457445],[7.744766,8.796934,-5.456840,3.725647,-2.368745,-6.369045,1.410355,-3.444502,-3.105142,7.455613,0.939191,-9.893690,5.973046],[2.322932,6.718729,-4.851233,6.557991,-8.147912,5.332376,-8.118656,3.348982,0.508148,-1.837767,-8.080857,-3.390364,-6.157136]]], dtype = "float64")#candidate|6165|(15, 4, 13)|const|float64
bop_6166 = relay.power(const_6164.astype('float64'), relay.reshape(const_6165.astype('float64'), relay.shape_of(const_6164))) # shape=(15, 4, 13)
output = relay.Tuple([bop_6166,])
output2 = relay.Tuple([bop_6166,])
func_6173 = relay.Function([], output)
mod['func_6173'] = func_6173
mod = relay.transform.InferType()(mod)
mutated_mod['func_6173'] = func_6173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6173_call = mutated_mod.get_global_var('func_6173')
call_6174 = func_6173_call()
output = call_6174
func_6175 = relay.Function([], output)
mutated_mod['func_6175'] = func_6175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4526_call = mod.get_global_var('func_4526')
func_4527_call = mutated_mod.get_global_var('func_4527')
call_6185 = relay.TupleGetItem(func_4526_call(), 1)
call_6186 = relay.TupleGetItem(func_4527_call(), 1)
output = call_6185
output2 = call_6186
func_6191 = relay.Function([], output)
mod['func_6191'] = func_6191
mod = relay.transform.InferType()(mod)
mutated_mod['func_6191'] = func_6191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6191_call = mutated_mod.get_global_var('func_6191')
call_6192 = func_6191_call()
output = call_6192
func_6193 = relay.Function([], output)
mutated_mod['func_6193'] = func_6193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_6214 = relay.TupleGetItem(func_545_call(), 0)
call_6215 = relay.TupleGetItem(func_546_call(), 0)
output = relay.Tuple([call_6214,])
output2 = relay.Tuple([call_6215,])
func_6221 = relay.Function([], output)
mod['func_6221'] = func_6221
mod = relay.transform.InferType()(mod)
output = func_6221()
func_6222 = relay.Function([], output)
mutated_mod['func_6222'] = func_6222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5755_call = mod.get_global_var('func_5755')
func_5757_call = mutated_mod.get_global_var('func_5757')
call_6265 = relay.TupleGetItem(func_5755_call(), 0)
call_6266 = relay.TupleGetItem(func_5757_call(), 0)
func_5755_call = mod.get_global_var('func_5755')
func_5757_call = mutated_mod.get_global_var('func_5757')
call_6312 = relay.TupleGetItem(func_5755_call(), 0)
call_6313 = relay.TupleGetItem(func_5757_call(), 0)
func_863_call = mod.get_global_var('func_863')
func_866_call = mutated_mod.get_global_var('func_866')
var_6318 = relay.var("var_6318", dtype = "float32", shape = (252,))#candidate|6318|(252,)|var|float32
call_6317 = relay.TupleGetItem(func_863_call(relay.reshape(var_6318.astype('float32'), [252,])), 1)
call_6319 = relay.TupleGetItem(func_866_call(relay.reshape(var_6318.astype('float32'), [252,])), 1)
func_4582_call = mod.get_global_var('func_4582')
func_4583_call = mutated_mod.get_global_var('func_4583')
call_6323 = relay.TupleGetItem(func_4582_call(), 0)
call_6324 = relay.TupleGetItem(func_4583_call(), 0)
var_6329 = relay.var("var_6329", dtype = "uint8", shape = (15, 1))#candidate|6329|(15, 1)|var|uint8
bop_6330 = relay.greater(call_6312.astype('bool'), var_6329.astype('bool')) # shape=(15, 1)
bop_6333 = relay.greater(call_6313.astype('bool'), var_6329.astype('bool')) # shape=(15, 1)
output = relay.Tuple([call_6265,call_6317,var_6318,call_6323,bop_6330,])
output2 = relay.Tuple([call_6266,call_6319,var_6318,call_6324,bop_6333,])
func_6335 = relay.Function([var_6318,var_6329,], output)
mod['func_6335'] = func_6335
mod = relay.transform.InferType()(mod)
mutated_mod['func_6335'] = func_6335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6335_call = mutated_mod.get_global_var('func_6335')
var_6337 = relay.var("var_6337", dtype = "float32", shape = (252,))#candidate|6337|(252,)|var|float32
var_6338 = relay.var("var_6338", dtype = "uint8", shape = (15, 1))#candidate|6338|(15, 1)|var|uint8
call_6336 = func_6335_call(var_6337,var_6338,)
output = call_6336
func_6339 = relay.Function([var_6337,var_6338,], output)
mutated_mod['func_6339'] = func_6339
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6386 = relay.var("var_6386", dtype = "float32", shape = ())#candidate|6386|()|var|float32
var_6387 = relay.var("var_6387", dtype = "float32", shape = (14, 1, 7))#candidate|6387|(14, 1, 7)|var|float32
bop_6388 = relay.mod(var_6386.astype('float32'), var_6387.astype('float32')) # shape=(14, 1, 7)
func_2619_call = mod.get_global_var('func_2619')
func_2621_call = mutated_mod.get_global_var('func_2621')
call_6395 = relay.TupleGetItem(func_2619_call(), 1)
call_6396 = relay.TupleGetItem(func_2621_call(), 1)
output = relay.Tuple([bop_6388,call_6395,])
output2 = relay.Tuple([bop_6388,call_6396,])
func_6407 = relay.Function([var_6386,var_6387,], output)
mod['func_6407'] = func_6407
mod = relay.transform.InferType()(mod)
var_6408 = relay.var("var_6408", dtype = "float32", shape = ())#candidate|6408|()|var|float32
var_6409 = relay.var("var_6409", dtype = "float32", shape = (14, 1, 7))#candidate|6409|(14, 1, 7)|var|float32
output = func_6407(var_6408,var_6409,)
func_6410 = relay.Function([var_6408,var_6409,], output)
mutated_mod['func_6410'] = func_6410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_6430 = func_753_call()
call_6431 = func_753_call()
output = relay.Tuple([call_6430,])
output2 = relay.Tuple([call_6431,])
func_6441 = relay.Function([], output)
mod['func_6441'] = func_6441
mod = relay.transform.InferType()(mod)
output = func_6441()
func_6442 = relay.Function([], output)
mutated_mod['func_6442'] = func_6442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5121_call = mod.get_global_var('func_5121')
func_5122_call = mutated_mod.get_global_var('func_5122')
call_6477 = relay.TupleGetItem(func_5121_call(), 2)
call_6478 = relay.TupleGetItem(func_5122_call(), 2)
output = call_6477
output2 = call_6478
func_6483 = relay.Function([], output)
mod['func_6483'] = func_6483
mod = relay.transform.InferType()(mod)
output = func_6483()
func_6484 = relay.Function([], output)
mutated_mod['func_6484'] = func_6484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6191_call = mod.get_global_var('func_6191')
func_6193_call = mutated_mod.get_global_var('func_6193')
call_6529 = func_6191_call()
call_6530 = func_6191_call()
output = relay.Tuple([call_6529,])
output2 = relay.Tuple([call_6530,])
func_6585 = relay.Function([], output)
mod['func_6585'] = func_6585
mod = relay.transform.InferType()(mod)
mutated_mod['func_6585'] = func_6585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6585_call = mutated_mod.get_global_var('func_6585')
call_6586 = func_6585_call()
output = call_6586
func_6587 = relay.Function([], output)
mutated_mod['func_6587'] = func_6587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2007_call = mutated_mod.get_global_var('func_2007')
call_6609 = relay.TupleGetItem(func_2006_call(), 3)
call_6610 = relay.TupleGetItem(func_2007_call(), 3)
output = relay.Tuple([call_6609,])
output2 = relay.Tuple([call_6610,])
func_6639 = relay.Function([], output)
mod['func_6639'] = func_6639
mod = relay.transform.InferType()(mod)
mutated_mod['func_6639'] = func_6639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6639_call = mutated_mod.get_global_var('func_6639')
call_6640 = func_6639_call()
output = call_6640
func_6641 = relay.Function([], output)
mutated_mod['func_6641'] = func_6641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4839_call = mod.get_global_var('func_4839')
func_4841_call = mutated_mod.get_global_var('func_4841')
call_6652 = relay.TupleGetItem(func_4839_call(), 0)
call_6653 = relay.TupleGetItem(func_4841_call(), 0)
func_3059_call = mod.get_global_var('func_3059')
func_3060_call = mutated_mod.get_global_var('func_3060')
call_6660 = relay.TupleGetItem(func_3059_call(), 0)
call_6661 = relay.TupleGetItem(func_3060_call(), 0)
func_1079_call = mod.get_global_var('func_1079')
func_1080_call = mutated_mod.get_global_var('func_1080')
call_6668 = relay.TupleGetItem(func_1079_call(), 0)
call_6669 = relay.TupleGetItem(func_1080_call(), 0)
func_6221_call = mod.get_global_var('func_6221')
func_6222_call = mutated_mod.get_global_var('func_6222')
call_6673 = relay.TupleGetItem(func_6221_call(), 0)
call_6674 = relay.TupleGetItem(func_6222_call(), 0)
output = relay.Tuple([call_6652,call_6660,call_6668,call_6673,])
output2 = relay.Tuple([call_6653,call_6661,call_6669,call_6674,])
func_6681 = relay.Function([], output)
mod['func_6681'] = func_6681
mod = relay.transform.InferType()(mod)
output = func_6681()
func_6682 = relay.Function([], output)
mutated_mod['func_6682'] = func_6682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5876_call = mod.get_global_var('func_5876')
func_5877_call = mutated_mod.get_global_var('func_5877')
call_6705 = relay.TupleGetItem(func_5876_call(), 2)
call_6706 = relay.TupleGetItem(func_5877_call(), 2)
func_4582_call = mod.get_global_var('func_4582')
func_4583_call = mutated_mod.get_global_var('func_4583')
call_6713 = relay.TupleGetItem(func_4582_call(), 0)
call_6714 = relay.TupleGetItem(func_4583_call(), 0)
func_2204_call = mod.get_global_var('func_2204')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_6740 = func_2204_call()
call_6741 = func_2204_call()
output = relay.Tuple([call_6705,call_6713,call_6740,])
output2 = relay.Tuple([call_6706,call_6714,call_6741,])
func_6761 = relay.Function([], output)
mod['func_6761'] = func_6761
mod = relay.transform.InferType()(mod)
mutated_mod['func_6761'] = func_6761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6761_call = mutated_mod.get_global_var('func_6761')
call_6762 = func_6761_call()
output = call_6762
func_6763 = relay.Function([], output)
mutated_mod['func_6763'] = func_6763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3515_call = mod.get_global_var('func_3515')
func_3517_call = mutated_mod.get_global_var('func_3517')
call_6772 = relay.TupleGetItem(func_3515_call(), 0)
call_6773 = relay.TupleGetItem(func_3517_call(), 0)
output = call_6772
output2 = call_6773
func_6774 = relay.Function([], output)
mod['func_6774'] = func_6774
mod = relay.transform.InferType()(mod)
mutated_mod['func_6774'] = func_6774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6774_call = mutated_mod.get_global_var('func_6774')
call_6775 = func_6774_call()
output = call_6775
func_6776 = relay.Function([], output)
mutated_mod['func_6776'] = func_6776
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6783 = relay.var("var_6783", dtype = "float64", shape = (10, 14, 16))#candidate|6783|(10, 14, 16)|var|float64
uop_6784 = relay.atan(var_6783.astype('float64')) # shape=(10, 14, 16)
output = uop_6784
output2 = uop_6784
func_6789 = relay.Function([var_6783,], output)
mod['func_6789'] = func_6789
mod = relay.transform.InferType()(mod)
var_6790 = relay.var("var_6790", dtype = "float64", shape = (10, 14, 16))#candidate|6790|(10, 14, 16)|var|float64
output = func_6789(var_6790)
func_6791 = relay.Function([var_6790], output)
mutated_mod['func_6791'] = func_6791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4238_call = mod.get_global_var('func_4238')
func_4239_call = mutated_mod.get_global_var('func_4239')
call_6823 = relay.TupleGetItem(func_4238_call(), 0)
call_6824 = relay.TupleGetItem(func_4239_call(), 0)
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_6825 = relay.TupleGetItem(func_1149_call(), 3)
call_6826 = relay.TupleGetItem(func_1150_call(), 3)
output = relay.Tuple([call_6823,call_6825,])
output2 = relay.Tuple([call_6824,call_6826,])
func_6837 = relay.Function([], output)
mod['func_6837'] = func_6837
mod = relay.transform.InferType()(mod)
output = func_6837()
func_6838 = relay.Function([], output)
mutated_mod['func_6838'] = func_6838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3059_call = mod.get_global_var('func_3059')
func_3060_call = mutated_mod.get_global_var('func_3060')
call_6843 = relay.TupleGetItem(func_3059_call(), 0)
call_6844 = relay.TupleGetItem(func_3060_call(), 0)
output = relay.Tuple([call_6843,])
output2 = relay.Tuple([call_6844,])
func_6846 = relay.Function([], output)
mod['func_6846'] = func_6846
mod = relay.transform.InferType()(mod)
output = func_6846()
func_6847 = relay.Function([], output)
mutated_mod['func_6847'] = func_6847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3515_call = mod.get_global_var('func_3515')
func_3517_call = mutated_mod.get_global_var('func_3517')
call_6859 = relay.TupleGetItem(func_3515_call(), 0)
call_6860 = relay.TupleGetItem(func_3517_call(), 0)
output = call_6859
output2 = call_6860
func_6878 = relay.Function([], output)
mod['func_6878'] = func_6878
mod = relay.transform.InferType()(mod)
output = func_6878()
func_6879 = relay.Function([], output)
mutated_mod['func_6879'] = func_6879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_6892 = relay.TupleGetItem(func_1321_call(), 1)
call_6893 = relay.TupleGetItem(func_1323_call(), 1)
uop_6897 = relay.sinh(call_6892.astype('float64')) # shape=(140,)
uop_6899 = relay.sinh(call_6893.astype('float64')) # shape=(140,)
output = uop_6897
output2 = uop_6899
func_6902 = relay.Function([], output)
mod['func_6902'] = func_6902
mod = relay.transform.InferType()(mod)
output = func_6902()
func_6903 = relay.Function([], output)
mutated_mod['func_6903'] = func_6903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5597_call = mod.get_global_var('func_5597')
func_5598_call = mutated_mod.get_global_var('func_5598')
call_6904 = relay.TupleGetItem(func_5597_call(), 0)
call_6905 = relay.TupleGetItem(func_5598_call(), 0)
func_3094_call = mod.get_global_var('func_3094')
func_3096_call = mutated_mod.get_global_var('func_3096')
call_6906 = func_3094_call()
call_6907 = func_3094_call()
func_6639_call = mod.get_global_var('func_6639')
func_6641_call = mutated_mod.get_global_var('func_6641')
call_6913 = relay.TupleGetItem(func_6639_call(), 0)
call_6914 = relay.TupleGetItem(func_6641_call(), 0)
output = relay.Tuple([call_6904,call_6906,call_6913,])
output2 = relay.Tuple([call_6905,call_6907,call_6914,])
func_6927 = relay.Function([], output)
mod['func_6927'] = func_6927
mod = relay.transform.InferType()(mod)
mutated_mod['func_6927'] = func_6927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6927_call = mutated_mod.get_global_var('func_6927')
call_6928 = func_6927_call()
output = call_6928
func_6929 = relay.Function([], output)
mutated_mod['func_6929'] = func_6929
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6932 = relay.const([[[-9.690660,-2.581475,3.455304,-1.666246,-7.636656,-5.511858,5.817571,-3.705779,4.785992,-2.310922,-0.316885],[-6.505303,-2.091321,-4.712488,2.190229,5.892578,1.747945,-8.149416,-3.159247,-9.378520,9.218676,-6.069864],[-0.630777,7.969905,-6.693651,-3.829393,-1.840457,-9.732297,-4.248866,0.733239,4.902568,7.748349,-4.997877]],[[2.285492,-3.196134,7.314035,2.178273,-2.142260,-9.383573,1.301127,7.746380,-2.468131,-0.612645,-7.427811],[8.532954,5.804971,9.315284,9.254800,-9.771128,-9.728772,9.482840,-5.098696,2.097999,-9.313309,8.713022],[-0.465524,1.795825,-3.035402,-1.275975,1.289312,-6.170036,-1.330142,6.447185,9.085540,-4.773452,2.291580]],[[7.605257,-5.454456,-2.970884,9.213946,3.804179,9.358440,-0.329137,-0.983393,-1.771494,-6.100100,-9.763378],[-4.000544,6.849877,0.637632,-0.026422,6.543965,0.677827,-9.332732,-9.861769,5.597193,-1.144644,-3.252320],[-9.189410,0.073657,-5.792485,-0.751740,-7.144500,5.986020,-0.722029,7.738187,9.532945,1.424174,3.452302]],[[-6.566828,1.237485,8.774775,-8.229304,-5.733556,-0.657074,-4.050765,7.819744,-6.476125,8.687223,7.220311],[-0.112279,-4.804381,6.781503,-3.182004,-3.469976,-5.632444,-7.269302,2.862418,-9.342331,-3.769765,6.085537],[9.059374,1.624241,-4.650373,1.207360,-9.361411,-3.679400,3.382514,-5.955249,-6.297734,4.717097,-8.366644]],[[-6.514225,-1.632786,8.718958,-9.264627,3.690583,-3.655055,4.369703,-7.483027,-1.402431,-7.784139,4.674503],[3.813908,-0.298605,-9.548273,-8.181155,2.510471,-1.611420,3.413786,-7.689475,-7.328225,-2.820160,-7.446351],[4.019852,-9.041065,-6.418020,7.576757,0.739856,4.928115,-4.169233,0.208385,4.150223,-3.358920,-2.750486]],[[7.052009,4.307278,4.265667,-2.885309,1.820826,-7.385819,-7.623082,-2.666104,-7.529105,-2.218565,0.459788],[-1.584557,8.464142,-8.901944,8.252139,-0.986827,3.593922,8.981973,1.987992,1.083842,9.859220,-0.265004],[-0.969562,0.069592,-9.983614,-0.178189,2.153853,-3.438745,-5.968354,-3.580704,-5.675437,6.709886,-9.318401]],[[-3.335818,-3.202370,-0.595332,4.476793,0.264711,6.281813,-8.368334,-6.759425,-3.259974,9.519704,1.307804],[7.728657,-0.420242,-1.145740,8.208127,-9.515015,-2.267088,8.719455,-9.388361,1.323673,-9.173125,6.299524],[4.006814,-8.233848,2.103439,-4.928572,5.151063,-4.766760,5.767615,8.871660,2.698356,-6.549526,7.273597]]], dtype = "float64")#candidate|6932|(7, 3, 11)|const|float64
uop_6933 = relay.atanh(const_6932.astype('float64')) # shape=(7, 3, 11)
uop_6937 = relay.sigmoid(uop_6933.astype('float64')) # shape=(7, 3, 11)
output = relay.Tuple([uop_6937,])
output2 = relay.Tuple([uop_6937,])
func_6939 = relay.Function([], output)
mod['func_6939'] = func_6939
mod = relay.transform.InferType()(mod)
mutated_mod['func_6939'] = func_6939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6939_call = mutated_mod.get_global_var('func_6939')
call_6940 = func_6939_call()
output = call_6940
func_6941 = relay.Function([], output)
mutated_mod['func_6941'] = func_6941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mod.get_global_var('func_4080')
func_4081_call = mutated_mod.get_global_var('func_4081')
call_6942 = relay.TupleGetItem(func_4080_call(), 1)
call_6943 = relay.TupleGetItem(func_4081_call(), 1)
output = call_6942
output2 = call_6943
func_6946 = relay.Function([], output)
mod['func_6946'] = func_6946
mod = relay.transform.InferType()(mod)
output = func_6946()
func_6947 = relay.Function([], output)
mutated_mod['func_6947'] = func_6947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2721_call = mod.get_global_var('func_2721')
func_2722_call = mutated_mod.get_global_var('func_2722')
call_6954 = relay.TupleGetItem(func_2721_call(), 2)
call_6955 = relay.TupleGetItem(func_2722_call(), 2)
func_6074_call = mod.get_global_var('func_6074')
func_6077_call = mutated_mod.get_global_var('func_6077')
var_6959 = relay.var("var_6959", dtype = "int64", shape = (242,))#candidate|6959|(242,)|var|int64
call_6958 = relay.TupleGetItem(func_6074_call(relay.reshape(var_6959.astype('int64'), [242,])), 2)
call_6960 = relay.TupleGetItem(func_6077_call(relay.reshape(var_6959.astype('int64'), [242,])), 2)
uop_6979 = relay.log2(call_6958.astype('float64')) # shape=(11, 11, 2)
uop_6981 = relay.log2(call_6960.astype('float64')) # shape=(11, 11, 2)
bop_6984 = relay.less_equal(call_6958.astype('bool'), relay.reshape(uop_6979.astype('bool'), relay.shape_of(call_6958))) # shape=(11, 11, 2)
bop_6987 = relay.less_equal(call_6960.astype('bool'), relay.reshape(uop_6981.astype('bool'), relay.shape_of(call_6960))) # shape=(11, 11, 2)
output = relay.Tuple([call_6954,var_6959,bop_6984,])
output2 = relay.Tuple([call_6955,var_6959,bop_6987,])
func_6988 = relay.Function([var_6959,], output)
mod['func_6988'] = func_6988
mod = relay.transform.InferType()(mod)
var_6989 = relay.var("var_6989", dtype = "int64", shape = (242,))#candidate|6989|(242,)|var|int64
output = func_6988(var_6989)
func_6990 = relay.Function([var_6989], output)
mutated_mod['func_6990'] = func_6990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_7013 = relay.TupleGetItem(func_1149_call(), 3)
call_7014 = relay.TupleGetItem(func_1150_call(), 3)
uop_7031 = relay.asin(call_7013.astype('float64')) # shape=(1, 140)
uop_7033 = relay.asin(call_7014.astype('float64')) # shape=(1, 140)
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_7045 = relay.TupleGetItem(func_545_call(), 0)
call_7046 = relay.TupleGetItem(func_546_call(), 0)
func_1467_call = mod.get_global_var('func_1467')
func_1468_call = mutated_mod.get_global_var('func_1468')
call_7048 = relay.TupleGetItem(func_1467_call(), 0)
call_7049 = relay.TupleGetItem(func_1468_call(), 0)
output = relay.Tuple([uop_7031,call_7045,call_7048,])
output2 = relay.Tuple([uop_7033,call_7046,call_7049,])
func_7054 = relay.Function([], output)
mod['func_7054'] = func_7054
mod = relay.transform.InferType()(mod)
mutated_mod['func_7054'] = func_7054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7054_call = mutated_mod.get_global_var('func_7054')
call_7055 = func_7054_call()
output = call_7055
func_7056 = relay.Function([], output)
mutated_mod['func_7056'] = func_7056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_7098 = func_1385_call()
call_7099 = func_1385_call()
output = relay.Tuple([call_7098,])
output2 = relay.Tuple([call_7099,])
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
var_7121 = relay.var("var_7121", dtype = "float32", shape = ())#candidate|7121|()|var|float32
var_7122 = relay.var("var_7122", dtype = "float32", shape = (8, 1, 2))#candidate|7122|(8, 1, 2)|var|float32
bop_7123 = relay.multiply(var_7121.astype('float32'), var_7122.astype('float32')) # shape=(8, 1, 2)
bop_7126 = relay.right_shift(var_7121.astype('uint8'), bop_7123.astype('uint8')) # shape=(8, 1, 2)
output = bop_7126
output2 = bop_7126
func_7133 = relay.Function([var_7121,var_7122,], output)
mod['func_7133'] = func_7133
mod = relay.transform.InferType()(mod)
var_7134 = relay.var("var_7134", dtype = "float32", shape = ())#candidate|7134|()|var|float32
var_7135 = relay.var("var_7135", dtype = "float32", shape = (8, 1, 2))#candidate|7135|(8, 1, 2)|var|float32
output = func_7133(var_7134,var_7135,)
func_7136 = relay.Function([var_7134,var_7135,], output)
mutated_mod['func_7136'] = func_7136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_7187 = relay.TupleGetItem(func_4931_call(), 1)
call_7188 = relay.TupleGetItem(func_4932_call(), 1)
func_2594_call = mod.get_global_var('func_2594')
func_2596_call = mutated_mod.get_global_var('func_2596')
var_7190 = relay.var("var_7190", dtype = "float64", shape = (140,))#candidate|7190|(140,)|var|float64
call_7189 = relay.TupleGetItem(func_2594_call(relay.reshape(var_7190.astype('float64'), [140,])), 7)
call_7191 = relay.TupleGetItem(func_2596_call(relay.reshape(var_7190.astype('float64'), [140,])), 7)
func_1564_call = mod.get_global_var('func_1564')
func_1565_call = mutated_mod.get_global_var('func_1565')
call_7192 = relay.TupleGetItem(func_1564_call(), 1)
call_7193 = relay.TupleGetItem(func_1565_call(), 1)
func_2997_call = mod.get_global_var('func_2997')
func_2999_call = mutated_mod.get_global_var('func_2999')
call_7195 = relay.TupleGetItem(func_2997_call(), 0)
call_7196 = relay.TupleGetItem(func_2999_call(), 0)
output = relay.Tuple([call_7187,call_7189,var_7190,call_7192,call_7195,])
output2 = relay.Tuple([call_7188,call_7191,var_7190,call_7193,call_7196,])
func_7201 = relay.Function([var_7190,], output)
mod['func_7201'] = func_7201
mod = relay.transform.InferType()(mod)
var_7202 = relay.var("var_7202", dtype = "float64", shape = (140,))#candidate|7202|(140,)|var|float64
output = func_7201(var_7202)
func_7203 = relay.Function([var_7202], output)
mutated_mod['func_7203'] = func_7203
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7205 = relay.var("var_7205", dtype = "int8", shape = (12, 2, 15))#candidate|7205|(12, 2, 15)|var|int8
const_7206 = relay.const([[[-4,5,-6,3,-9,7,2,9,10,5,-7,-10,6,9,-2],[1,6,5,-6,9,9,-7,-7,8,-6,-9,-9,-1,1,-2]],[[-3,-10,-10,-2,-5,4,-6,-2,9,-2,-2,-7,10,-5,-10],[-5,-1,3,-9,-10,7,-8,-4,9,2,-8,2,5,-5,-4]],[[-7,-9,5,-2,8,-9,-5,-9,-9,2,-2,4,-6,-6,7],[-6,-9,5,-9,-8,-10,-2,-6,-3,1,-4,4,7,-7,8]],[[4,-2,-1,7,-3,-6,4,7,-3,4,-4,9,8,-7,-8],[1,-3,5,10,-3,-8,6,-9,3,5,-5,6,8,-9,-9]],[[2,-9,4,8,-9,-7,-1,1,9,-1,-1,-3,8,1,6],[4,-1,-2,10,-9,2,6,-2,-3,-10,3,-1,-8,-6,6]],[[-10,-2,7,8,-4,6,4,1,-8,-6,9,2,6,8,-1],[-5,-7,6,9,-1,2,2,1,3,-8,-10,8,8,3,5]],[[-2,-7,-7,7,8,10,-7,-9,6,8,2,-2,9,4,7],[6,-10,-2,-7,-5,-9,8,-9,-4,10,8,9,2,-3,-8]],[[6,2,8,-2,-5,3,-2,-9,7,-6,5,-8,-8,-2,7],[-1,-5,-8,9,9,9,-9,2,-3,-1,-5,5,-1,-4,-3]],[[-3,5,-7,1,6,-3,2,7,-10,-3,3,7,3,-2,9],[9,10,-7,8,-7,10,9,-10,5,1,10,8,-2,5,8]],[[-9,-5,-1,-8,-2,1,-4,5,-1,3,10,5,-3,7,-3],[2,-1,3,-9,9,7,-5,-4,-5,1,-6,3,7,8,-6]],[[10,-5,4,1,10,-7,3,7,2,-2,-2,-4,-10,3,-6],[9,6,6,-3,-5,8,9,4,1,-8,9,-1,-6,-3,-1]],[[9,-4,5,7,7,-8,-6,8,-2,5,4,-1,6,-8,-8],[9,-10,-4,-3,2,5,-8,-8,10,-7,-2,-9,-6,2,-6]]], dtype = "int8")#candidate|7206|(12, 2, 15)|const|int8
bop_7207 = relay.less_equal(var_7205.astype('bool'), relay.reshape(const_7206.astype('bool'), relay.shape_of(var_7205))) # shape=(12, 2, 15)
output = relay.Tuple([bop_7207,])
output2 = relay.Tuple([bop_7207,])
func_7210 = relay.Function([var_7205,], output)
mod['func_7210'] = func_7210
mod = relay.transform.InferType()(mod)
mutated_mod['func_7210'] = func_7210
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7211 = relay.var("var_7211", dtype = "int8", shape = (12, 2, 15))#candidate|7211|(12, 2, 15)|var|int8
func_7210_call = mutated_mod.get_global_var('func_7210')
call_7212 = func_7210_call(var_7211)
output = call_7212
func_7213 = relay.Function([var_7211], output)
mutated_mod['func_7213'] = func_7213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6191_call = mod.get_global_var('func_6191')
func_6193_call = mutated_mod.get_global_var('func_6193')
call_7263 = func_6191_call()
call_7264 = func_6191_call()
output = relay.Tuple([call_7263,])
output2 = relay.Tuple([call_7264,])
func_7295 = relay.Function([], output)
mod['func_7295'] = func_7295
mod = relay.transform.InferType()(mod)
mutated_mod['func_7295'] = func_7295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7295_call = mutated_mod.get_global_var('func_7295')
call_7296 = func_7295_call()
output = call_7296
func_7297 = relay.Function([], output)
mutated_mod['func_7297'] = func_7297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4526_call = mod.get_global_var('func_4526')
func_4527_call = mutated_mod.get_global_var('func_4527')
call_7310 = relay.TupleGetItem(func_4526_call(), 1)
call_7311 = relay.TupleGetItem(func_4527_call(), 1)
output = relay.Tuple([call_7310,])
output2 = relay.Tuple([call_7311,])
func_7312 = relay.Function([], output)
mod['func_7312'] = func_7312
mod = relay.transform.InferType()(mod)
output = func_7312()
func_7313 = relay.Function([], output)
mutated_mod['func_7313'] = func_7313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5876_call = mod.get_global_var('func_5876')
func_5877_call = mutated_mod.get_global_var('func_5877')
call_7355 = relay.TupleGetItem(func_5876_call(), 2)
call_7356 = relay.TupleGetItem(func_5877_call(), 2)
func_2721_call = mod.get_global_var('func_2721')
func_2722_call = mutated_mod.get_global_var('func_2722')
call_7362 = relay.TupleGetItem(func_2721_call(), 1)
call_7363 = relay.TupleGetItem(func_2722_call(), 1)
bop_7369 = relay.greater_equal(call_7362.astype('bool'), relay.reshape(call_7355.astype('bool'), relay.shape_of(call_7362))) # shape=(9, 6, 2)
bop_7372 = relay.greater_equal(call_7363.astype('bool'), relay.reshape(call_7356.astype('bool'), relay.shape_of(call_7363))) # shape=(9, 6, 2)
output = bop_7369
output2 = bop_7372
func_7374 = relay.Function([], output)
mod['func_7374'] = func_7374
mod = relay.transform.InferType()(mod)
output = func_7374()
func_7375 = relay.Function([], output)
mutated_mod['func_7375'] = func_7375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_7386 = relay.TupleGetItem(func_2777_call(), 1)
call_7387 = relay.TupleGetItem(func_2778_call(), 1)
output = relay.Tuple([call_7386,])
output2 = relay.Tuple([call_7387,])
func_7388 = relay.Function([], output)
mod['func_7388'] = func_7388
mod = relay.transform.InferType()(mod)
mutated_mod['func_7388'] = func_7388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7388_call = mutated_mod.get_global_var('func_7388')
call_7389 = func_7388_call()
output = call_7389
func_7390 = relay.Function([], output)
mutated_mod['func_7390'] = func_7390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_7393 = func_1178_call()
call_7394 = func_1178_call()
func_3789_call = mod.get_global_var('func_3789')
func_3791_call = mutated_mod.get_global_var('func_3791')
call_7397 = relay.TupleGetItem(func_3789_call(), 0)
call_7398 = relay.TupleGetItem(func_3791_call(), 0)
output = relay.Tuple([call_7393,call_7397,])
output2 = relay.Tuple([call_7394,call_7398,])
func_7433 = relay.Function([], output)
mod['func_7433'] = func_7433
mod = relay.transform.InferType()(mod)
mutated_mod['func_7433'] = func_7433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7433_call = mutated_mod.get_global_var('func_7433')
call_7434 = func_7433_call()
output = call_7434
func_7435 = relay.Function([], output)
mutated_mod['func_7435'] = func_7435
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7436 = relay.var("var_7436", dtype = "float64", shape = (2, 4, 10))#candidate|7436|(2, 4, 10)|var|float64
uop_7437 = relay.rsqrt(var_7436.astype('float64')) # shape=(2, 4, 10)
output = relay.Tuple([uop_7437,])
output2 = relay.Tuple([uop_7437,])
func_7439 = relay.Function([var_7436,], output)
mod['func_7439'] = func_7439
mod = relay.transform.InferType()(mod)
var_7440 = relay.var("var_7440", dtype = "float64", shape = (2, 4, 10))#candidate|7440|(2, 4, 10)|var|float64
output = func_7439(var_7440)
func_7441 = relay.Function([var_7440], output)
mutated_mod['func_7441'] = func_7441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_7510 = func_753_call()
call_7511 = func_753_call()
func_7054_call = mod.get_global_var('func_7054')
func_7056_call = mutated_mod.get_global_var('func_7056')
call_7514 = relay.TupleGetItem(func_7054_call(), 0)
call_7515 = relay.TupleGetItem(func_7056_call(), 0)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_7516 = relay.TupleGetItem(func_4931_call(), 1)
call_7517 = relay.TupleGetItem(func_4932_call(), 1)
output = relay.Tuple([call_7510,call_7514,call_7516,])
output2 = relay.Tuple([call_7511,call_7515,call_7517,])
func_7527 = relay.Function([], output)
mod['func_7527'] = func_7527
mod = relay.transform.InferType()(mod)
mutated_mod['func_7527'] = func_7527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7527_call = mutated_mod.get_global_var('func_7527')
call_7528 = func_7527_call()
output = call_7528
func_7529 = relay.Function([], output)
mutated_mod['func_7529'] = func_7529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3203_call = mod.get_global_var('func_3203')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_7554 = func_3203_call()
call_7555 = func_3203_call()
output = relay.Tuple([call_7554,])
output2 = relay.Tuple([call_7555,])
func_7576 = relay.Function([], output)
mod['func_7576'] = func_7576
mod = relay.transform.InferType()(mod)
mutated_mod['func_7576'] = func_7576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7576_call = mutated_mod.get_global_var('func_7576')
call_7577 = func_7576_call()
output = call_7577
func_7578 = relay.Function([], output)
mutated_mod['func_7578'] = func_7578
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7598 = relay.const([[[5.661678,7.526661,5.112500,8.090885,5.341506,-4.265650,-6.223800,-0.486575,7.577588,3.685755,3.820075,-5.665561,0.421670,-9.809275,0.667109,-8.056873],[5.965143,-2.098635,7.292460,-3.667803,1.308633,-2.517226,-7.936791,-2.317522,-5.168684,5.295961,-6.399793,-2.147608,-7.252438,6.247773,-1.362317,-3.834789],[2.769434,8.689741,-5.773996,1.893056,-5.920485,-1.192127,9.654302,-9.458338,-0.070427,8.554320,2.369436,-5.937690,-7.890122,8.153895,-1.286286,8.943937],[7.307394,-7.648855,-5.700700,1.916898,9.374273,6.134431,8.369734,4.553749,-9.666947,-4.780789,-2.140150,1.198969,-6.902614,-8.865446,-4.238412,4.616833],[-4.377845,3.712785,8.797787,9.918093,-8.396765,2.398634,-8.720906,-3.278211,1.869412,9.869217,9.229401,4.407598,6.014436,-3.461291,5.792045,2.630521],[-0.107020,-4.988803,-6.916063,-9.694955,-3.174951,-0.946304,-4.424128,1.349647,0.021376,-8.246144,9.081665,-5.077312,7.936273,-3.939371,-3.306215,-3.726145],[8.582286,5.244668,-4.962506,-1.725881,5.550338,7.629872,3.187007,-7.339282,0.430721,-4.282039,-2.583420,-1.305359,5.102435,-6.128764,-4.729078,-5.289030],[8.088282,5.377697,-5.329861,-8.641408,-3.351273,5.832277,2.602340,-2.953453,-5.781020,7.806932,-9.918171,-3.610863,1.613050,1.071706,3.157437,8.165511],[1.025425,-3.213022,-0.531393,-5.628134,7.541667,0.539925,9.058134,0.767624,-4.736557,-1.446673,-6.464905,-1.116157,9.351981,-0.740968,-9.911677,5.728164]],[[-5.089431,1.021648,-3.086346,-2.331264,3.735606,-4.953797,0.812154,2.210793,8.577059,-7.003565,-9.825299,5.978905,0.308534,4.900353,4.722126,5.482646],[-4.658807,-2.354209,-7.823155,-7.769671,-8.029270,-6.153053,0.112696,0.298511,5.066402,-2.466271,5.385249,4.784725,6.961778,-6.878219,4.802394,5.670301],[-0.662075,4.079243,-0.441669,-5.932367,-0.703393,-6.265794,-3.991121,-0.634515,-5.549984,-5.155101,-0.759021,-7.000055,-5.645157,-7.609583,-9.495122,6.530304],[-8.187134,-4.992211,7.517743,3.268572,6.240378,5.334994,-0.146502,-4.857690,-5.128030,-2.206492,-2.837933,3.553882,6.631666,0.553795,4.058483,-4.836665],[3.744796,-6.678672,5.008230,-3.149711,0.883676,6.033920,-7.490274,-8.996158,-4.427405,6.379286,4.278396,5.673297,6.040749,8.236665,7.688618,-5.207342],[-4.195420,5.134253,-6.331140,-0.160856,5.994406,1.729175,5.633316,0.080270,-9.633958,2.079224,0.089093,-5.322441,3.098169,3.051509,9.912477,8.040789],[-4.756972,-0.356055,-1.431045,-3.175511,-4.669971,9.729941,-6.075207,5.880651,-2.189919,-5.791484,5.309836,-9.317932,-5.630020,4.101130,7.958052,8.609096],[-4.078844,-0.425262,2.370266,-1.197470,6.370131,4.225701,-0.647093,-2.922796,4.328575,-8.166704,-0.763000,6.289321,-5.238032,-5.026725,7.002471,5.844751],[5.079290,6.115628,9.331162,-0.366350,2.586802,-8.344385,-1.152838,-8.321880,6.942972,-2.035002,2.877801,9.776718,5.563154,2.027157,8.576947,-1.588262]],[[8.006455,3.216947,9.522608,1.688999,-8.613833,5.664733,-4.919198,-3.598311,-0.648749,0.021374,3.207805,-0.072393,9.489436,9.456353,-1.355355,7.027851],[5.274251,-9.285373,5.491795,-0.060160,7.047497,-4.577937,4.216711,-6.368900,-2.869666,-5.384396,-6.639472,-9.175258,-6.920273,-8.605930,1.110704,-1.049936],[9.372079,7.832212,-3.300802,-0.853534,9.716603,-8.586162,8.986675,2.432745,-0.009293,6.326181,-4.600652,-4.365787,-5.380308,5.326924,7.190573,-4.111415],[8.261469,3.743242,9.509032,4.042105,-1.670392,-7.803224,-5.081793,2.591455,5.105571,2.575427,-5.781988,-8.587744,8.659117,-1.155319,-3.889464,6.473402],[5.276381,9.017401,-2.900941,7.926286,-2.830285,-3.020677,5.712780,-5.346063,4.070922,-8.187884,1.942144,-1.155929,9.171753,8.898313,0.233623,2.123069],[3.655141,-2.012859,7.277636,8.517341,4.009842,7.735351,8.401382,1.475316,3.557884,4.894267,-1.695440,3.495324,-8.899095,2.558702,6.340650,-2.378592],[-6.800548,-5.810624,7.712272,2.201720,-1.214204,6.226276,-6.852928,-0.351567,9.175880,5.865096,2.461931,7.474641,6.168948,6.018613,6.851177,-4.631648],[-3.982384,2.342662,-5.604487,-0.121760,1.401433,-6.524776,-9.506482,-7.879744,-9.817842,-3.869252,-0.780672,-0.130758,-2.048815,5.611969,6.211697,4.433483],[-3.052071,0.655539,-6.548156,6.587520,-2.941301,6.365047,-3.553335,-4.161897,5.327726,-1.055246,-9.797986,-2.506612,9.854198,-2.106101,0.518282,-5.584869]],[[-3.618922,-9.504207,-1.308254,0.539499,8.859296,7.794879,-2.773493,2.123820,-5.060843,8.541224,-9.868511,-4.850970,8.872311,-4.484198,-8.115353,0.753520],[1.328640,0.619309,9.528283,-4.320594,-2.785294,5.462205,1.066824,-1.013538,-3.224141,-0.673104,8.893875,-3.693650,5.337492,5.797693,-8.381351,-7.385542],[-7.737095,6.206375,-6.434119,9.633074,1.086935,1.359273,1.876783,5.131284,-8.209218,-1.666484,-8.630229,-6.767916,0.453733,2.954915,-6.765284,4.233589],[-7.254022,5.319269,-6.950140,9.937344,2.070882,-0.561085,-2.194565,-5.289928,3.702388,6.127918,-9.548718,1.613668,8.225346,5.230099,3.472731,9.063868],[3.861637,-4.780976,1.815065,0.737036,2.311333,3.645183,0.839981,-6.743660,-3.608668,-1.933814,3.325646,-7.109013,3.714260,3.546102,4.676481,-8.767465],[3.222287,-0.449789,-0.474130,6.107249,-7.632716,3.035798,-9.762479,-7.985580,4.259387,9.179560,9.703379,-5.123223,6.723955,2.374130,-6.554687,9.440803],[-4.158179,-0.004743,-1.690443,-2.138772,-7.022413,-1.094174,8.209458,8.836797,-3.017031,-3.486596,-5.425122,-8.567740,-9.280876,-2.042381,4.189166,-4.206405],[-0.377851,-7.482504,-6.507004,6.607268,-5.799156,5.359181,-4.986640,2.529194,-0.394002,-9.897777,-3.266979,-0.086684,-4.422314,5.726665,7.897108,-4.873569],[-2.379070,-8.530899,2.337369,9.198929,2.856935,-8.848988,1.147223,-7.187298,8.380920,-0.343443,6.023953,-3.530039,-1.384076,9.346527,5.093594,4.149026]],[[-5.597162,-6.321982,5.706352,-7.058851,-4.240434,-5.712095,-0.159382,7.478059,-4.846323,5.343657,2.881088,7.102430,4.850262,0.106669,-5.477562,-2.775431],[-7.893931,3.490440,-1.687961,-0.347571,-3.726785,-2.270774,-4.279987,-0.816526,3.056753,-7.797616,1.125878,-8.772086,9.855536,4.284678,-3.247421,-2.945428],[-9.385067,-1.489535,2.851261,5.391931,-3.845323,-3.446739,-0.203712,4.227474,-7.399737,-2.136894,2.389844,-8.982368,-9.068797,5.159203,8.480096,7.110686],[4.024296,-1.244229,-0.517971,-1.378058,1.377200,6.688236,5.155342,-0.747770,8.352741,5.373949,9.991333,4.393162,0.891333,1.798725,-0.039253,-8.258390],[-1.746171,1.297734,-0.275505,2.487070,-9.212889,5.115176,4.574904,-4.376097,-9.232036,-1.092594,7.925030,5.409254,-5.389742,-9.861107,7.506759,-0.790960],[6.846409,1.670814,7.034403,-1.052576,2.776735,9.575082,7.542384,2.859010,0.483482,0.718564,3.897686,4.216344,7.776635,8.951201,-9.147972,9.960446],[6.316439,4.749718,5.847285,-7.618001,-0.624915,-8.852002,9.791446,5.089559,7.823510,-0.322080,-8.602953,-5.933765,8.066088,-3.236297,9.762652,8.880436],[-2.269882,2.888242,-6.749625,6.577518,4.879022,-8.356765,2.286901,0.355205,7.052823,-8.250294,5.172156,4.175130,-3.997156,-1.978165,4.121907,-3.852365],[-7.936736,-6.813419,7.928294,7.363454,1.353537,-0.024901,-2.697419,8.844531,5.857253,6.951639,-6.310184,6.445710,-3.231528,-1.240844,7.329013,-9.962155]],[[-4.759439,7.361669,-5.413075,-9.544133,-4.684535,-3.085468,-4.982128,-2.975105,8.976443,-9.932239,5.920046,-6.276254,5.319972,4.367343,4.865853,-7.567217],[-2.922790,-3.328874,9.699115,-6.925894,2.176109,-4.144986,-4.680412,0.568586,-6.114655,6.243596,8.002547,9.964734,-0.906737,3.592664,-9.969460,3.023760],[3.127276,5.699588,-9.821089,7.495360,4.620772,7.669092,-1.935073,7.993303,-1.734299,-9.148266,4.694832,-0.391927,7.035189,4.204325,-4.681727,-2.393157],[-1.689473,-3.638122,-5.244284,-4.257996,7.193298,5.681819,-4.962482,-6.376467,-2.891538,-6.918843,-9.221017,2.943238,5.217035,-8.536075,-4.679503,3.697632],[-4.962640,8.130910,7.722935,-5.296614,-3.686356,4.561514,6.012424,9.905179,-2.850611,4.982965,8.193083,-9.205651,0.621367,-5.710865,-6.907828,3.888044],[3.210729,6.460809,-1.575370,2.987564,5.909584,-0.716606,-1.062164,-0.304813,5.910727,1.934295,3.004610,4.346664,-8.202708,-6.122211,-7.299342,-3.598344],[-9.625486,-4.492755,2.333845,9.920964,-0.149058,0.041133,-0.396133,-9.938423,2.137124,-0.568246,0.797721,-1.115321,3.533519,-9.703608,-7.654138,7.104822],[-1.904433,9.231908,1.390388,0.431540,-6.289141,-7.018282,-2.294094,7.973796,-4.399615,-5.911020,0.238035,-3.759086,5.042081,-2.531891,9.736774,9.126861],[-1.945230,6.561928,4.157478,4.317546,-6.432041,-0.542181,-8.797597,-7.590503,6.401113,8.031076,8.525225,7.000088,-4.717414,-9.783593,0.609640,-6.794080]],[[4.540675,6.189932,-9.033879,-7.889396,-8.546951,0.831828,-6.597883,-7.717232,6.676171,3.905545,1.415717,1.217065,-5.176170,9.223392,7.653861,4.929436],[0.829045,-7.120416,-8.795439,-9.471673,5.714744,5.732176,-8.096806,-9.114895,2.276803,-0.330588,-0.611504,1.517991,-2.623836,4.162143,-0.427473,-1.059902],[7.059100,6.269459,3.273074,5.430983,5.453996,8.528272,-9.276651,3.090876,2.364513,-5.104360,-1.025517,-1.957336,-9.085839,-9.390706,9.811345,-6.631504],[5.014663,-1.107812,-8.674218,-2.952071,-8.407797,4.818877,8.875017,1.859192,-3.513181,-1.230914,3.958006,6.979258,-6.661645,-5.048433,-9.139562,0.409401],[-3.615868,0.707724,2.863833,-5.383457,6.034547,-0.757016,9.633658,6.215678,9.681948,-3.120358,-0.358859,-2.234140,0.081068,-9.629442,1.905048,-0.500417],[6.601201,-0.388547,3.045962,3.651582,-6.713352,8.874770,7.964108,-7.113436,-5.470838,3.632882,-1.880442,-6.017836,-1.986637,-2.148427,-4.514772,6.052335],[-3.260559,-3.066092,-2.386888,-9.106122,5.387182,-2.845229,-5.211669,2.585561,2.208437,2.245166,-7.941706,-3.908266,0.781256,-2.583313,9.428426,0.690242],[-8.137322,6.133934,6.031286,3.525994,6.449866,9.568104,-6.839142,-8.603522,2.381827,-6.328586,5.102882,-0.420954,8.388035,-6.797724,-6.232353,-3.729819],[6.260972,-8.210867,0.422491,0.217220,9.828964,-0.834582,6.725251,-3.610658,-0.854841,-6.520915,5.523165,-6.304584,-0.027425,0.439873,5.137589,2.976695]],[[2.983506,5.026718,2.707340,2.274729,-6.018056,5.724725,-9.641256,-5.871203,-6.211098,0.096288,-0.460744,-4.695375,-0.476493,2.300355,2.315429,0.287083],[-8.841684,2.179779,2.915256,8.447791,-5.889557,-4.250039,-2.440959,1.424186,9.573139,-8.101243,5.976568,-8.923414,-1.024307,1.668629,-3.833474,-6.977391],[6.933755,0.099115,-2.901904,-6.877635,9.478423,9.690836,-8.942825,-6.677455,8.838724,8.132221,0.352025,4.837559,8.304886,4.695991,7.601347,0.461960],[5.306061,4.577451,7.606779,-6.060924,-9.298731,-8.097332,-0.448295,1.213440,1.519206,-9.179234,-5.927658,-7.569638,-5.685815,-8.968459,5.297974,9.931271],[-5.094306,-1.659474,-5.236867,-5.822535,-7.285524,0.132520,4.559273,2.323854,7.268182,3.360335,4.370891,-6.095526,7.848516,7.786377,-2.818628,6.404497],[5.961051,-6.231297,-4.821593,8.230638,1.903327,0.253356,7.182155,7.114951,1.280809,-5.932974,-2.844872,-7.382221,0.445852,-4.222525,-1.045527,-8.906075],[8.634620,-1.574275,2.737026,-7.621104,-8.163017,4.066778,-6.852511,3.770094,1.002963,-9.665981,-7.318418,3.335252,-7.419428,2.845225,8.142052,1.981574],[-4.011684,-1.793921,6.312146,-9.227994,9.216492,8.294905,-9.808282,1.646985,-6.308420,9.769884,-7.620345,1.234060,-7.501225,-6.548591,-9.360127,-4.880331],[4.877869,1.782414,5.466544,-3.491009,6.026296,5.859208,-0.503067,-4.136295,-2.179865,6.748134,-5.492022,-3.559471,7.897148,3.032444,-5.549984,-5.936302]],[[-5.117306,-2.123636,1.007487,-1.954383,-4.614035,-5.397498,-6.715123,3.589399,-0.181170,-6.791382,9.780663,2.242427,0.385706,9.973058,-5.691237,1.110421],[1.179223,5.511240,-4.665612,2.661461,5.630549,-9.955531,-7.090489,-7.311570,-2.765011,-5.914503,5.540445,6.971890,-8.064118,-1.601990,-9.984217,8.854730],[2.535136,5.963968,0.572060,-1.865812,-1.589696,-2.492156,0.966916,-1.799399,9.084692,2.218253,-2.732450,5.861975,4.830200,-6.640277,1.342972,6.632098],[-7.305544,9.695082,-7.378175,-3.359301,-0.806451,9.057356,2.044948,0.462389,-6.049903,-7.961262,4.791963,8.633105,3.665747,9.485733,-5.267850,-0.122846],[3.293761,-1.680608,5.504491,-7.856752,4.545362,2.146399,2.488598,-1.290555,-5.698704,5.099733,-8.295645,-4.926827,-1.119027,4.423738,1.212040,8.882625],[2.634452,-9.243288,-1.880659,-4.027953,-1.824848,-6.916951,-2.779811,-6.402200,8.122314,5.576834,-4.958739,-6.408492,1.564755,4.542361,3.758207,6.287367],[-6.627895,0.122861,-7.994630,3.159944,-6.901722,9.645230,-6.202987,6.923616,2.838492,1.939881,-2.316453,-8.179669,1.271229,-1.765203,-6.050514,6.054813],[5.449722,0.954636,-3.994332,8.366578,-9.382847,-5.998380,-5.717922,2.373190,-7.136027,8.372863,-2.794936,-4.315409,-4.210134,-7.663778,-4.290493,2.280700],[-9.120379,9.616596,2.913549,9.804672,9.911251,-7.447427,0.132783,2.769793,3.393152,8.199838,-4.450001,1.775217,-6.080980,2.646373,-5.347007,8.143697]],[[5.935290,3.099846,9.900343,1.855145,-1.015523,-8.802708,2.275168,7.531848,-9.687073,-7.094024,-0.157471,7.567540,9.681857,7.655917,-1.512896,-1.415381],[-4.515395,-2.415163,6.745835,-5.890768,-0.659510,4.002076,6.392305,-3.353489,2.041793,-8.537476,-0.518054,7.841032,5.301622,3.961801,8.727653,1.467510],[-7.338421,3.943959,6.905502,7.017529,-8.975607,2.526603,-6.431163,9.075141,-3.403015,8.906321,-5.780683,-7.837428,-8.050380,8.631613,-9.489043,4.260066],[-4.665891,-2.154842,-9.310306,5.480478,-4.462860,-3.701329,-3.543563,1.815823,-5.052843,-4.961202,3.590538,-1.073040,-2.092249,3.718106,-0.347045,7.383696],[6.989747,2.399726,-8.942189,-1.398429,4.583870,7.821890,-0.843808,4.003052,7.443382,2.488527,-0.051836,-6.540694,5.752770,9.720997,-3.939145,8.851585],[-0.557885,-5.162332,4.157376,-0.282074,8.585102,7.136133,-8.539637,-8.030083,-3.710516,-2.012251,1.569491,8.711222,-7.273550,9.245588,-3.730194,-4.491139],[6.918549,8.675457,1.148731,6.640785,0.679846,-2.946027,5.930071,9.357487,5.745098,9.522705,6.816561,8.522659,8.994295,-6.032900,8.781959,9.179390],[6.543157,-5.168360,-3.210331,-4.503138,-4.213990,7.959296,8.309188,7.683533,-5.208672,-1.002574,4.537786,1.762768,-4.020567,-5.395778,-7.534528,-2.803526],[-9.501636,-7.217630,-0.167289,-6.252345,3.003532,5.136966,3.853824,6.848298,8.393032,6.050206,-8.409460,0.958716,-9.897661,-0.778448,3.907667,2.097638]],[[0.798152,-3.001058,-2.029843,-0.668367,-5.351183,-5.798628,-6.014089,0.392245,6.329475,8.816479,3.935744,-1.628888,-5.240238,-0.399930,1.763220,-0.512278],[5.485528,5.259807,8.790221,-3.768250,8.767966,1.900321,-6.696734,0.432679,0.348261,7.946915,3.303963,0.750694,8.330215,-0.062882,6.634569,4.889255],[8.657258,-1.646672,8.619175,9.664053,6.967991,-8.978895,3.763310,-1.157153,-5.192235,-9.022384,1.584059,-6.009603,1.181964,-3.751472,4.194218,-7.537684],[-0.211713,5.821004,3.432204,-4.927665,-6.580425,-9.319892,-8.097153,-3.894796,7.300124,-7.129779,-1.610217,9.581974,9.952354,-6.013521,4.949409,-2.876565],[0.245883,2.413261,-3.477198,-0.813354,4.719012,-2.945823,1.587434,-9.759512,4.819234,5.957543,0.924317,-0.845136,-4.536611,7.952497,0.359436,4.775645],[-0.305139,0.505566,-9.554876,3.737455,-6.501041,8.167655,-7.416615,-1.367729,8.128703,-9.794248,-5.260889,4.731084,6.518300,8.422882,-9.708394,-4.407817],[3.316137,6.795970,1.791664,4.065906,3.310540,8.338150,8.304049,7.193224,5.246485,9.557774,-2.318692,6.661158,-9.174039,-7.999418,3.655773,4.946989],[-3.638197,7.136080,3.377021,-4.430846,3.613851,-4.900943,6.411518,3.386693,1.774328,3.356522,-5.010449,-7.147410,1.281958,7.651513,1.608526,7.096850],[-9.326303,5.514159,-5.616846,-3.301219,1.712253,-5.497716,-4.619004,8.725025,-5.954318,-8.618364,9.898704,2.375275,7.160101,-5.239425,7.954532,9.820446]]], dtype = "float32")#candidate|7598|(11, 9, 16)|const|float32
uop_7599 = relay.sigmoid(const_7598.astype('float32')) # shape=(11, 9, 16)
uop_7605 = relay.sqrt(uop_7599.astype('float64')) # shape=(11, 9, 16)
func_694_call = mod.get_global_var('func_694')
func_695_call = mutated_mod.get_global_var('func_695')
call_7615 = relay.TupleGetItem(func_694_call(), 0)
call_7616 = relay.TupleGetItem(func_695_call(), 0)
uop_7619 = relay.sinh(uop_7599.astype('float32')) # shape=(11, 9, 16)
func_7201_call = mod.get_global_var('func_7201')
func_7203_call = mutated_mod.get_global_var('func_7203')
var_7628 = relay.var("var_7628", dtype = "float64", shape = (140,))#candidate|7628|(140,)|var|float64
call_7627 = relay.TupleGetItem(func_7201_call(relay.reshape(var_7628.astype('float64'), [140,])), 0)
call_7629 = relay.TupleGetItem(func_7203_call(relay.reshape(var_7628.astype('float64'), [140,])), 0)
uop_7634 = relay.cosh(uop_7605.astype('float32')) # shape=(11, 9, 16)
output = relay.Tuple([call_7615,uop_7619,call_7627,var_7628,uop_7634,])
output2 = relay.Tuple([call_7616,uop_7619,call_7629,var_7628,uop_7634,])
func_7658 = relay.Function([var_7628,], output)
mod['func_7658'] = func_7658
mod = relay.transform.InferType()(mod)
var_7659 = relay.var("var_7659", dtype = "float64", shape = (140,))#candidate|7659|(140,)|var|float64
output = func_7658(var_7659)
func_7660 = relay.Function([var_7659], output)
mutated_mod['func_7660'] = func_7660
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7664 = relay.var("var_7664", dtype = "float64", shape = (8, 15, 5))#candidate|7664|(8, 15, 5)|var|float64
uop_7665 = relay.cos(var_7664.astype('float64')) # shape=(8, 15, 5)
func_6407_call = mod.get_global_var('func_6407')
func_6410_call = mutated_mod.get_global_var('func_6410')
const_7670 = relay.const(-8.470927, dtype = "float32")#candidate|7670|()|const|float32
var_7671 = relay.var("var_7671", dtype = "float32", shape = (98,))#candidate|7671|(98,)|var|float32
call_7669 = relay.TupleGetItem(func_6407_call(relay.reshape(const_7670.astype('float32'), []), relay.reshape(var_7671.astype('float32'), [14, 1, 7]), ), 1)
call_7672 = relay.TupleGetItem(func_6410_call(relay.reshape(const_7670.astype('float32'), []), relay.reshape(var_7671.astype('float32'), [14, 1, 7]), ), 1)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
const_7674 = relay.const([[8.517149,4.207439,-7.610504,0.950859,-3.913520,2.771707,-5.716909,-2.165584,-3.594039,4.082012,2.551377,3.644661,-2.874073,5.151705,2.270619,6.899309,7.096155,-4.230274,-8.339906,-5.836684,-2.173748,2.909904,-4.969277,3.340942,-3.802376,-9.912052,-1.044127,3.813781],[4.496625,-2.705041,7.891021,0.564540,-0.013675,-2.622406,-0.958983,6.275899,-3.548630,9.619241,-8.022121,8.879736,2.246891,-9.212789,1.070396,6.258861,8.757995,9.791473,8.977234,8.485201,-6.820971,6.692191,-1.706556,-5.374792,7.924371,4.354431,-6.695130,-0.669169],[0.891531,4.505554,2.654791,3.041867,-7.110536,1.762707,1.545381,5.867176,-0.004397,-1.721327,1.166064,9.483042,-1.888411,-8.031281,6.156693,2.642088,-6.289184,9.048512,6.695635,-6.423642,-7.708241,5.708912,-9.816313,8.032930,1.515428,3.847241,-3.091104,-4.821353],[-1.187660,9.331338,3.010773,-2.499340,-3.511826,7.289291,-5.941294,7.963480,9.569825,-1.964221,-3.132865,-9.584036,-9.130134,-8.916249,-7.902408,3.559568,-1.711829,-2.960602,3.243324,0.966756,9.613445,3.730746,-4.932128,-2.262619,-0.061033,5.521449,-0.212107,-5.827247],[5.026803,-3.981534,5.987750,-5.647250,-4.425072,-0.437364,3.344960,2.281118,-6.430720,-7.073086,-0.567970,3.370742,-5.153046,5.060325,-0.965479,8.938139,-8.076411,-7.013022,7.981059,5.792932,0.944382,-7.017973,7.520008,9.264830,-7.931294,-0.005256,-0.644233,7.306731]], dtype = "float64")#candidate|7674|(5, 28)|const|float64
call_7673 = relay.TupleGetItem(func_212_call(relay.reshape(call_7669.astype('float32'), [9, 6, 2]), relay.reshape(const_7674.astype('float64'), [5, 28]), ), 2)
call_7675 = relay.TupleGetItem(func_215_call(relay.reshape(call_7669.astype('float32'), [9, 6, 2]), relay.reshape(const_7674.astype('float64'), [5, 28]), ), 2)
uop_7689 = relay.acos(uop_7665.astype('float64')) # shape=(8, 15, 5)
output = relay.Tuple([call_7669,const_7670,var_7671,call_7673,const_7674,uop_7689,])
output2 = relay.Tuple([call_7672,const_7670,var_7671,call_7675,const_7674,uop_7689,])
func_7692 = relay.Function([var_7664,var_7671,], output)
mod['func_7692'] = func_7692
mod = relay.transform.InferType()(mod)
var_7693 = relay.var("var_7693", dtype = "float64", shape = (8, 15, 5))#candidate|7693|(8, 15, 5)|var|float64
var_7694 = relay.var("var_7694", dtype = "float32", shape = (98,))#candidate|7694|(98,)|var|float32
output = func_7692(var_7693,var_7694,)
func_7695 = relay.Function([var_7693,var_7694,], output)
mutated_mod['func_7695'] = func_7695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4304_call = mod.get_global_var('func_4304')
func_4306_call = mutated_mod.get_global_var('func_4306')
call_7711 = func_4304_call()
call_7712 = func_4304_call()
func_7133_call = mod.get_global_var('func_7133')
func_7136_call = mutated_mod.get_global_var('func_7136')
const_7718 = relay.const(-0.640788, dtype = "float32")#candidate|7718|()|const|float32
var_7719 = relay.var("var_7719", dtype = "float32", shape = (16,))#candidate|7719|(16,)|var|float32
call_7717 = func_7133_call(relay.reshape(const_7718.astype('float32'), []), relay.reshape(var_7719.astype('float32'), [8, 1, 2]), )
call_7720 = func_7133_call(relay.reshape(const_7718.astype('float32'), []), relay.reshape(var_7719.astype('float32'), [8, 1, 2]), )
func_1149_call = mod.get_global_var('func_1149')
func_1150_call = mutated_mod.get_global_var('func_1150')
call_7722 = relay.TupleGetItem(func_1149_call(), 0)
call_7723 = relay.TupleGetItem(func_1150_call(), 0)
func_3406_call = mod.get_global_var('func_3406')
func_3408_call = mutated_mod.get_global_var('func_3408')
const_7728 = relay.const([[1,-6,-5,-3,2,8,8,-6,-6,8,-6,-9,-4,-6,2,-6,8,-2,-6,2,8,8,8,5,-4,7,7,10],[-7,-10,8,4,7,-9,-10,1,-10,3,2,6,-3,8,9,1,-6,-6,10,-2,-5,-2,-3,2,1,-3,-3,10],[2,-6,-8,8,2,2,-6,-9,-7,-8,5,4,-5,-10,8,6,10,2,1,-5,7,-4,-2,-6,3,9,-5,-3],[-4,1,-5,-1,-9,4,-6,-2,6,6,9,9,7,10,-5,-6,-8,-10,-4,-9,-5,-4,1,1,-9,9,10,-2],[8,-1,-6,1,-6,8,-3,4,9,-8,-1,2,-8,2,1,-5,5,-3,4,9,-4,-1,-4,-4,2,-7,-2,5]], dtype = "uint64")#candidate|7728|(5, 28)|const|uint64
call_7727 = func_3406_call(relay.reshape(const_7728.astype('uint64'), [14, 2, 5]))
call_7729 = func_3406_call(relay.reshape(const_7728.astype('uint64'), [14, 2, 5]))
output = relay.Tuple([call_7711,call_7717,const_7718,var_7719,call_7722,call_7727,const_7728,])
output2 = relay.Tuple([call_7712,call_7720,const_7718,var_7719,call_7723,call_7729,const_7728,])
func_7755 = relay.Function([var_7719,], output)
mod['func_7755'] = func_7755
mod = relay.transform.InferType()(mod)
mutated_mod['func_7755'] = func_7755
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7756 = relay.var("var_7756", dtype = "float32", shape = (16,))#candidate|7756|(16,)|var|float32
func_7755_call = mutated_mod.get_global_var('func_7755')
call_7757 = func_7755_call(var_7756)
output = call_7757
func_7758 = relay.Function([var_7756], output)
mutated_mod['func_7758'] = func_7758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6774_call = mod.get_global_var('func_6774')
func_6776_call = mutated_mod.get_global_var('func_6776')
call_7804 = func_6774_call()
call_7805 = func_6774_call()
output = relay.Tuple([call_7804,])
output2 = relay.Tuple([call_7805,])
func_7806 = relay.Function([], output)
mod['func_7806'] = func_7806
mod = relay.transform.InferType()(mod)
mutated_mod['func_7806'] = func_7806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7806_call = mutated_mod.get_global_var('func_7806')
call_7807 = func_7806_call()
output = call_7807
func_7808 = relay.Function([], output)
mutated_mod['func_7808'] = func_7808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mod.get_global_var('func_4080')
func_4081_call = mutated_mod.get_global_var('func_4081')
call_7831 = relay.TupleGetItem(func_4080_call(), 2)
call_7832 = relay.TupleGetItem(func_4081_call(), 2)
output = relay.Tuple([call_7831,])
output2 = relay.Tuple([call_7832,])
func_7838 = relay.Function([], output)
mod['func_7838'] = func_7838
mod = relay.transform.InferType()(mod)
mutated_mod['func_7838'] = func_7838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7838_call = mutated_mod.get_global_var('func_7838')
call_7839 = func_7838_call()
output = call_7839
func_7840 = relay.Function([], output)
mutated_mod['func_7840'] = func_7840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7838_call = mod.get_global_var('func_7838')
func_7840_call = mutated_mod.get_global_var('func_7840')
call_7905 = relay.TupleGetItem(func_7838_call(), 0)
call_7906 = relay.TupleGetItem(func_7840_call(), 0)
func_545_call = mod.get_global_var('func_545')
func_546_call = mutated_mod.get_global_var('func_546')
call_7932 = relay.TupleGetItem(func_545_call(), 0)
call_7933 = relay.TupleGetItem(func_546_call(), 0)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_7935 = func_4130_call()
call_7936 = func_4130_call()
func_3406_call = mod.get_global_var('func_3406')
func_3408_call = mutated_mod.get_global_var('func_3408')
var_7940 = relay.var("var_7940", dtype = "uint64", shape = (140,))#candidate|7940|(140,)|var|uint64
call_7939 = func_3406_call(relay.reshape(var_7940.astype('uint64'), [14, 2, 5]))
call_7941 = func_3406_call(relay.reshape(var_7940.astype('uint64'), [14, 2, 5]))
func_5781_call = mod.get_global_var('func_5781')
func_5782_call = mutated_mod.get_global_var('func_5782')
call_7944 = relay.TupleGetItem(func_5781_call(), 2)
call_7945 = relay.TupleGetItem(func_5782_call(), 2)
func_3572_call = mod.get_global_var('func_3572')
func_3573_call = mutated_mod.get_global_var('func_3573')
call_7950 = relay.TupleGetItem(func_3572_call(), 1)
call_7951 = relay.TupleGetItem(func_3573_call(), 1)
output = relay.Tuple([call_7905,call_7932,call_7935,call_7939,var_7940,call_7944,call_7950,])
output2 = relay.Tuple([call_7906,call_7933,call_7936,call_7941,var_7940,call_7945,call_7951,])
func_7953 = relay.Function([var_7940,], output)
mod['func_7953'] = func_7953
mod = relay.transform.InferType()(mod)
var_7954 = relay.var("var_7954", dtype = "uint64", shape = (140,))#candidate|7954|(140,)|var|uint64
output = func_7953(var_7954)
func_7955 = relay.Function([var_7954], output)
mutated_mod['func_7955'] = func_7955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_755_call = mutated_mod.get_global_var('func_755')
call_7981 = func_753_call()
call_7982 = func_753_call()
func_3992_call = mod.get_global_var('func_3992')
func_3993_call = mutated_mod.get_global_var('func_3993')
call_7991 = relay.TupleGetItem(func_3992_call(), 0)
call_7992 = relay.TupleGetItem(func_3993_call(), 0)
output = relay.Tuple([call_7981,call_7991,])
output2 = relay.Tuple([call_7982,call_7992,])
func_7996 = relay.Function([], output)
mod['func_7996'] = func_7996
mod = relay.transform.InferType()(mod)
mutated_mod['func_7996'] = func_7996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7996_call = mutated_mod.get_global_var('func_7996')
call_7997 = func_7996_call()
output = call_7997
func_7998 = relay.Function([], output)
mutated_mod['func_7998'] = func_7998
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8004 = relay.const([[[-10,3,-9,-4,2,-10,2,2,10,8,-4,-10],[-3,-5,2,4,-2,-3,-8,1,8,4,-9,-9],[8,1,-6,-2,-9,-5,-2,2,-8,5,5,-5],[9,3,6,9,9,-5,-2,-2,-3,2,8,9],[9,1,2,-5,5,-1,9,-4,-3,-1,-7,-3],[-4,8,-9,7,1,-1,1,-3,5,-7,7,1],[2,2,9,-2,2,-2,-4,-10,6,-9,-1,-5],[-10,1,6,7,7,7,-7,-6,6,-4,8,9],[-5,-3,1,-3,10,8,7,4,-7,10,10,4],[6,8,2,-8,-6,-5,8,-9,3,4,5,6],[9,-5,-9,-6,-9,-1,-4,9,-1,-10,-2,9],[10,-7,-3,6,-8,2,-4,-4,-5,-3,3,10],[6,-3,10,-8,-5,-5,10,2,-2,5,5,8],[-4,8,5,-1,9,-3,-6,-9,-6,1,4,3]],[[-2,-4,8,6,3,9,-3,10,4,10,4,3],[2,7,-1,-3,-9,-7,-9,10,8,-1,-2,10],[-4,-8,-10,8,6,9,6,-8,9,5,-10,-1],[6,9,2,-8,2,3,-6,3,8,9,3,10],[-5,-1,2,5,-3,8,6,2,-1,-1,5,10],[7,9,7,4,-6,8,1,8,10,1,-3,7],[7,-2,3,8,-1,9,-8,-3,2,-4,7,-8],[9,6,-10,5,-10,-10,1,2,-4,-2,-8,9],[-8,-4,3,3,-9,4,-3,-9,-8,-7,-8,2],[2,6,-1,-1,-8,-6,-4,2,10,-5,7,-6],[-6,5,-4,7,1,7,10,2,10,8,-7,-9],[8,-9,-9,-3,10,8,7,1,1,-1,-3,-9],[-9,6,9,4,-9,-6,2,3,9,7,9,3],[3,2,-5,10,8,-3,-3,-6,-1,-3,2,-4]],[[-9,5,8,-9,10,-8,2,2,-6,-7,-1,3],[3,-5,-4,-4,-8,3,6,7,-1,2,3,-3],[8,-7,-3,3,6,3,-4,3,7,-8,-7,-9],[-1,2,-5,-4,5,4,-2,5,2,10,-4,-8],[8,-2,-4,-3,-1,9,-10,-1,-6,4,-9,-8],[5,-6,10,8,3,-2,2,-2,-10,1,5,4],[4,-9,-7,5,-2,10,9,9,9,-9,-5,-6],[-3,5,-6,9,-7,6,-3,5,-5,7,-3,8],[-6,-3,-9,7,5,-9,-9,2,5,9,10,-5],[-8,-9,-9,-3,5,9,6,-7,6,-1,-6,-2],[-2,1,6,6,-8,-5,3,5,7,-5,10,3],[10,2,6,7,6,9,-3,5,2,-2,1,5],[3,-8,-2,8,4,5,1,-9,9,-8,3,-8],[5,-1,7,-4,-6,3,5,1,9,-9,-8,-9]],[[6,-1,-3,3,-9,6,-10,6,5,5,9,7],[-2,10,7,-10,9,2,-10,-1,9,7,-8,-7],[-2,-2,10,1,-8,-3,4,-7,-5,-4,4,-6],[-3,-2,5,3,-4,10,-6,8,-6,8,4,-1],[-4,6,10,-1,-6,-3,4,10,-3,-2,5,-3],[-2,-1,8,-7,-8,-10,-8,1,-4,7,-2,-4],[9,-6,-9,-7,1,7,-1,2,1,8,-1,-3],[5,2,7,4,3,4,10,3,9,-1,-8,8],[2,-9,6,9,2,-1,-7,-8,-7,-4,-2,-8],[-9,-1,-1,4,-8,-8,5,-8,-1,7,-5,10],[-5,-9,-3,10,-6,-9,-2,10,-6,-4,10,-9],[10,8,-8,7,5,4,5,-10,-7,-7,3,-8],[-10,1,4,-10,5,10,-10,-9,-3,5,-7,8],[-3,2,4,7,4,-5,-8,-5,-7,-6,-9,2]],[[-8,-1,-3,8,6,3,1,6,-6,6,-8,-6],[-3,1,-7,-8,-1,9,-8,9,-10,3,-2,9],[-2,1,5,6,-10,-1,-2,-2,-8,7,2,7],[10,-5,1,-10,8,-2,1,-10,4,7,-10,1],[10,3,5,3,-10,-8,2,-3,-1,5,4,2],[9,-6,-8,9,4,-1,-10,4,5,-2,-2,-9],[-1,-9,-10,-2,2,-7,4,10,8,7,-8,-9],[-5,-1,-7,1,5,-4,3,-3,6,5,8,8],[-9,-3,5,1,4,-8,2,-2,1,3,1,-7],[8,9,-7,1,1,4,-5,-8,7,-1,-5,-8],[-8,-8,-7,-8,-7,10,-5,2,2,-3,-1,7],[5,6,2,6,-3,10,9,2,8,-4,2,8],[1,2,-2,-7,10,9,-7,3,-9,-7,-5,-8],[4,4,7,-1,-7,10,3,-8,-3,8,-4,-8]]], dtype = "int8")#candidate|8004|(5, 14, 12)|const|int8
var_8005 = relay.var("var_8005", dtype = "int8", shape = (5, 14, 12))#candidate|8005|(5, 14, 12)|var|int8
bop_8006 = relay.minimum(const_8004.astype('int8'), relay.reshape(var_8005.astype('int8'), relay.shape_of(const_8004))) # shape=(5, 14, 12)
output = bop_8006
output2 = bop_8006
func_8012 = relay.Function([var_8005,], output)
mod['func_8012'] = func_8012
mod = relay.transform.InferType()(mod)
var_8013 = relay.var("var_8013", dtype = "int8", shape = (5, 14, 12))#candidate|8013|(5, 14, 12)|var|int8
output = func_8012(var_8013)
func_8014 = relay.Function([var_8013], output)
mutated_mod['func_8014'] = func_8014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6681_call = mod.get_global_var('func_6681')
func_6682_call = mutated_mod.get_global_var('func_6682')
call_8044 = relay.TupleGetItem(func_6681_call(), 2)
call_8045 = relay.TupleGetItem(func_6682_call(), 2)
output = relay.Tuple([call_8044,])
output2 = relay.Tuple([call_8045,])
func_8068 = relay.Function([], output)
mod['func_8068'] = func_8068
mod = relay.transform.InferType()(mod)
output = func_8068()
func_8069 = relay.Function([], output)
mutated_mod['func_8069'] = func_8069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4526_call = mod.get_global_var('func_4526')
func_4527_call = mutated_mod.get_global_var('func_4527')
call_8105 = relay.TupleGetItem(func_4526_call(), 2)
call_8106 = relay.TupleGetItem(func_4527_call(), 2)
uop_8108 = relay.asin(call_8105.astype('float32')) # shape=(585,)
uop_8110 = relay.asin(call_8106.astype('float32')) # shape=(585,)
uop_8115 = relay.cosh(call_8105.astype('float64')) # shape=(585,)
uop_8117 = relay.cosh(call_8106.astype('float64')) # shape=(585,)
var_8138 = relay.var("var_8138", dtype = "float64", shape = (585,))#candidate|8138|(585,)|var|float64
bop_8139 = relay.multiply(uop_8115.astype('uint32'), relay.reshape(var_8138.astype('uint32'), relay.shape_of(uop_8115))) # shape=(585,)
bop_8142 = relay.multiply(uop_8117.astype('uint32'), relay.reshape(var_8138.astype('uint32'), relay.shape_of(uop_8117))) # shape=(585,)
output = relay.Tuple([uop_8108,bop_8139,])
output2 = relay.Tuple([uop_8110,bop_8142,])
func_8158 = relay.Function([var_8138,], output)
mod['func_8158'] = func_8158
mod = relay.transform.InferType()(mod)
var_8159 = relay.var("var_8159", dtype = "float64", shape = (585,))#candidate|8159|(585,)|var|float64
output = func_8158(var_8159)
func_8160 = relay.Function([var_8159], output)
mutated_mod['func_8160'] = func_8160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mod.get_global_var('func_2006')
func_2007_call = mutated_mod.get_global_var('func_2007')
call_8179 = relay.TupleGetItem(func_2006_call(), 3)
call_8180 = relay.TupleGetItem(func_2007_call(), 3)
output = call_8179
output2 = call_8180
func_8181 = relay.Function([], output)
mod['func_8181'] = func_8181
mod = relay.transform.InferType()(mod)
output = func_8181()
func_8182 = relay.Function([], output)
mutated_mod['func_8182'] = func_8182
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8186 = relay.var("var_8186", dtype = "int64", shape = (12, 2, 8))#candidate|8186|(12, 2, 8)|var|int64
var_8187 = relay.var("var_8187", dtype = "int64", shape = (12, 2, 8))#candidate|8187|(12, 2, 8)|var|int64
bop_8188 = relay.multiply(var_8186.astype('int64'), relay.reshape(var_8187.astype('int64'), relay.shape_of(var_8186))) # shape=(12, 2, 8)
output = relay.Tuple([bop_8188,])
output2 = relay.Tuple([bop_8188,])
func_8191 = relay.Function([var_8186,var_8187,], output)
mod['func_8191'] = func_8191
mod = relay.transform.InferType()(mod)
var_8192 = relay.var("var_8192", dtype = "int64", shape = (12, 2, 8))#candidate|8192|(12, 2, 8)|var|int64
var_8193 = relay.var("var_8193", dtype = "int64", shape = (12, 2, 8))#candidate|8193|(12, 2, 8)|var|int64
output = func_8191(var_8192,var_8193,)
func_8194 = relay.Function([var_8192,var_8193,], output)
mutated_mod['func_8194'] = func_8194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5357_call = mod.get_global_var('func_5357')
func_5358_call = mutated_mod.get_global_var('func_5358')
call_8213 = relay.TupleGetItem(func_5357_call(), 0)
call_8214 = relay.TupleGetItem(func_5358_call(), 0)
func_3515_call = mod.get_global_var('func_3515')
func_3517_call = mutated_mod.get_global_var('func_3517')
call_8215 = relay.TupleGetItem(func_3515_call(), 0)
call_8216 = relay.TupleGetItem(func_3517_call(), 0)
func_5357_call = mod.get_global_var('func_5357')
func_5358_call = mutated_mod.get_global_var('func_5358')
call_8233 = relay.TupleGetItem(func_5357_call(), 1)
call_8234 = relay.TupleGetItem(func_5358_call(), 1)
output = relay.Tuple([call_8213,call_8215,call_8233,])
output2 = relay.Tuple([call_8214,call_8216,call_8234,])
func_8238 = relay.Function([], output)
mod['func_8238'] = func_8238
mod = relay.transform.InferType()(mod)
mutated_mod['func_8238'] = func_8238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8238_call = mutated_mod.get_global_var('func_8238')
call_8239 = func_8238_call()
output = call_8239
func_8240 = relay.Function([], output)
mutated_mod['func_8240'] = func_8240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1564_call = mod.get_global_var('func_1564')
func_1565_call = mutated_mod.get_global_var('func_1565')
call_8322 = relay.TupleGetItem(func_1564_call(), 1)
call_8323 = relay.TupleGetItem(func_1565_call(), 1)
output = call_8322
output2 = call_8323
func_8332 = relay.Function([], output)
mod['func_8332'] = func_8332
mod = relay.transform.InferType()(mod)
mutated_mod['func_8332'] = func_8332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8332_call = mutated_mod.get_global_var('func_8332')
call_8333 = func_8332_call()
output = call_8333
func_8334 = relay.Function([], output)
mutated_mod['func_8334'] = func_8334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6441_call = mod.get_global_var('func_6441')
func_6442_call = mutated_mod.get_global_var('func_6442')
call_8395 = relay.TupleGetItem(func_6441_call(), 0)
call_8396 = relay.TupleGetItem(func_6442_call(), 0)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_8397 = relay.TupleGetItem(func_4931_call(), 2)
call_8398 = relay.TupleGetItem(func_4932_call(), 2)
output = relay.Tuple([call_8395,call_8397,])
output2 = relay.Tuple([call_8396,call_8398,])
func_8400 = relay.Function([], output)
mod['func_8400'] = func_8400
mod = relay.transform.InferType()(mod)
output = func_8400()
func_8401 = relay.Function([], output)
mutated_mod['func_8401'] = func_8401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5781_call = mod.get_global_var('func_5781')
func_5782_call = mutated_mod.get_global_var('func_5782')
call_8404 = relay.TupleGetItem(func_5781_call(), 2)
call_8405 = relay.TupleGetItem(func_5782_call(), 2)
output = call_8404
output2 = call_8405
func_8417 = relay.Function([], output)
mod['func_8417'] = func_8417
mod = relay.transform.InferType()(mod)
output = func_8417()
func_8418 = relay.Function([], output)
mutated_mod['func_8418'] = func_8418
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8443 = relay.var("var_8443", dtype = "uint16", shape = (6, 10, 7))#candidate|8443|(6, 10, 7)|var|uint16
var_8444 = relay.var("var_8444", dtype = "uint16", shape = (6, 10, 7))#candidate|8444|(6, 10, 7)|var|uint16
bop_8445 = relay.less_equal(var_8443.astype('bool'), relay.reshape(var_8444.astype('bool'), relay.shape_of(var_8443))) # shape=(6, 10, 7)
func_1515_call = mod.get_global_var('func_1515')
func_1518_call = mutated_mod.get_global_var('func_1518')
var_8456 = relay.var("var_8456", dtype = "float32", shape = (108,))#candidate|8456|(108,)|var|float32
call_8455 = func_1515_call(relay.reshape(var_8456.astype('float32'), [9, 6, 2]))
call_8457 = func_1515_call(relay.reshape(var_8456.astype('float32'), [9, 6, 2]))
const_8465 = relay.const([[[-8,4,-8,1,-3,3,-10],[-6,2,-2,-3,4,8,4],[7,-3,-2,5,3,5,6],[-5,-3,-3,8,-10,6,-6],[4,-2,1,-6,-10,4,8],[-1,-9,3,1,9,-1,10],[-2,2,8,7,-7,2,-3],[-3,6,-5,2,7,4,-3],[-4,2,1,2,-6,-7,-3],[10,-5,-6,7,-8,-1,-4]],[[-2,2,2,-3,-6,10,-5],[4,-8,-3,7,8,5,3],[-10,3,-6,9,6,10,-7],[3,9,-10,-2,-4,4,-1],[5,-7,4,8,-4,5,6],[-4,-6,-5,-4,6,9,3],[1,6,-1,-2,2,3,4],[8,5,-3,10,-10,6,-2],[-5,2,-10,-3,-9,8,-2],[9,-10,7,2,-10,1,-9]],[[-5,2,6,7,2,9,-4],[5,7,-3,-5,-6,-2,9],[6,10,9,-5,-8,10,-2],[-1,7,2,2,-3,-8,3],[-5,7,10,-5,1,-3,2],[-9,4,3,-8,7,2,6],[-1,4,-1,9,8,2,8],[10,-1,-6,-1,-8,6,8],[5,2,2,4,-6,-7,-1],[-6,6,-8,-9,2,3,-8]],[[5,-9,-9,-6,6,6,-3],[8,4,10,4,-7,-2,2],[8,8,-5,4,7,-4,-10],[-7,-5,-8,1,-9,7,5],[-4,7,-6,-7,-2,-4,3],[-4,-10,7,-5,4,-4,-8],[-8,2,-1,-8,-6,7,-8],[-8,1,-5,2,6,-10,1],[3,6,-4,7,-9,-2,2],[4,-10,-2,-6,-2,10,6]],[[-10,3,-10,-9,9,-2,1],[-5,1,2,6,2,10,10],[4,1,5,-9,4,1,-2],[-2,-5,5,-10,9,8,10],[7,-9,8,-5,3,-7,-2],[10,1,8,-1,-4,-9,-9],[-4,6,-8,2,-6,-8,1],[-5,6,-8,7,3,-8,-1],[9,3,-8,7,-5,-2,6],[-1,9,-1,-1,-2,-4,8]],[[-3,10,-10,7,3,4,3],[-2,-9,-9,6,3,-8,8],[1,7,-7,-6,-1,5,-7],[3,-6,-2,-7,-1,-10,2],[1,-3,8,-6,6,-9,7],[10,-2,7,-9,1,1,-8],[-8,10,-10,4,2,2,4],[-4,5,6,-6,-5,3,10],[2,4,8,-9,-8,8,-3],[-9,-2,-9,-8,6,9,10]]], dtype = "uint16")#candidate|8465|(6, 10, 7)|const|uint16
bop_8466 = relay.mod(var_8444.astype('float32'), relay.reshape(const_8465.astype('float32'), relay.shape_of(var_8444))) # shape=(6, 10, 7)
func_3406_call = mod.get_global_var('func_3406')
func_3408_call = mutated_mod.get_global_var('func_3408')
const_8471 = relay.const([1,-7,-3,-3,2,3,10,-7,8,-3,-1,-2,-6,3,1,-3,7,5,-4,6,-2,3,6,5,7,10,4,-8,-9,10,-4,-4,2,8,10,1,2,3,5,3,-7,9,-2,-2,7,-1,-4,1,-4,1,4,5,-5,5,10,1,10,9,-8,-5,4,5,2,-5,6,10,5,7,8,9,1,-5,1,-2,-6,3,2,-9,5,-1,-9,2,-8,5,2,-2,-7,1,-1,-4,-10,9,6,-6,-4,-1,-10,9,3,-2,10,-7,10,-5,-3,-8,-6,6,-4,3,3,-1,1,9,-3,-1,6,10,-10,-7,-3,-7,-3,-3,9,-7,1,5,7,6,-6,5,-6,8,-9,8,-1,5,10,-2], dtype = "uint64")#candidate|8471|(140,)|const|uint64
call_8470 = func_3406_call(relay.reshape(const_8471.astype('uint64'), [14, 2, 5]))
call_8472 = func_3406_call(relay.reshape(const_8471.astype('uint64'), [14, 2, 5]))
var_8474 = relay.var("var_8474", dtype = "bool", shape = (6, 10, 7))#candidate|8474|(6, 10, 7)|var|bool
bop_8475 = relay.logical_xor(bop_8445.astype('uint64'), relay.reshape(var_8474.astype('uint64'), relay.shape_of(bop_8445))) # shape=(6, 10, 7)
var_8484 = relay.var("var_8484", dtype = "bool", shape = (6, 10, 7))#candidate|8484|(6, 10, 7)|var|bool
bop_8485 = relay.bitwise_xor(bop_8445.astype('int8'), relay.reshape(var_8484.astype('int8'), relay.shape_of(bop_8445))) # shape=(6, 10, 7)
bop_8493 = relay.greater(var_8484.astype('bool'), relay.reshape(bop_8485.astype('bool'), relay.shape_of(var_8484))) # shape=(6, 10, 7)
bop_8499 = relay.equal(bop_8475.astype('bool'), relay.reshape(bop_8466.astype('bool'), relay.shape_of(bop_8475))) # shape=(6, 10, 7)
output = relay.Tuple([call_8455,var_8456,call_8470,const_8471,bop_8493,bop_8499,])
output2 = relay.Tuple([call_8457,var_8456,call_8472,const_8471,bop_8493,bop_8499,])
func_8519 = relay.Function([var_8443,var_8444,var_8456,var_8474,var_8484,], output)
mod['func_8519'] = func_8519
mod = relay.transform.InferType()(mod)
var_8520 = relay.var("var_8520", dtype = "uint16", shape = (6, 10, 7))#candidate|8520|(6, 10, 7)|var|uint16
var_8521 = relay.var("var_8521", dtype = "uint16", shape = (6, 10, 7))#candidate|8521|(6, 10, 7)|var|uint16
var_8522 = relay.var("var_8522", dtype = "float32", shape = (108,))#candidate|8522|(108,)|var|float32
var_8523 = relay.var("var_8523", dtype = "bool", shape = (6, 10, 7))#candidate|8523|(6, 10, 7)|var|bool
var_8524 = relay.var("var_8524", dtype = "bool", shape = (6, 10, 7))#candidate|8524|(6, 10, 7)|var|bool
output = func_8519(var_8520,var_8521,var_8522,var_8523,var_8524,)
func_8525 = relay.Function([var_8520,var_8521,var_8522,var_8523,var_8524,], output)
mutated_mod['func_8525'] = func_8525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7295_call = mod.get_global_var('func_7295')
func_7297_call = mutated_mod.get_global_var('func_7297')
call_8556 = relay.TupleGetItem(func_7295_call(), 0)
call_8557 = relay.TupleGetItem(func_7297_call(), 0)
func_2393_call = mod.get_global_var('func_2393')
func_2394_call = mutated_mod.get_global_var('func_2394')
call_8581 = relay.TupleGetItem(func_2393_call(), 2)
call_8582 = relay.TupleGetItem(func_2394_call(), 2)
func_6927_call = mod.get_global_var('func_6927')
func_6929_call = mutated_mod.get_global_var('func_6929')
call_8583 = relay.TupleGetItem(func_6927_call(), 2)
call_8584 = relay.TupleGetItem(func_6929_call(), 2)
output = relay.Tuple([call_8556,call_8581,call_8583,])
output2 = relay.Tuple([call_8557,call_8582,call_8584,])
func_8591 = relay.Function([], output)
mod['func_8591'] = func_8591
mod = relay.transform.InferType()(mod)
output = func_8591()
func_8592 = relay.Function([], output)
mutated_mod['func_8592'] = func_8592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3109_call = mod.get_global_var('func_3109')
func_3110_call = mutated_mod.get_global_var('func_3110')
call_8595 = relay.TupleGetItem(func_3109_call(), 0)
call_8596 = relay.TupleGetItem(func_3110_call(), 0)
output = relay.Tuple([call_8595,])
output2 = relay.Tuple([call_8596,])
func_8605 = relay.Function([], output)
mod['func_8605'] = func_8605
mod = relay.transform.InferType()(mod)
output = func_8605()
func_8606 = relay.Function([], output)
mutated_mod['func_8606'] = func_8606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5755_call = mod.get_global_var('func_5755')
func_5757_call = mutated_mod.get_global_var('func_5757')
call_8640 = relay.TupleGetItem(func_5755_call(), 1)
call_8641 = relay.TupleGetItem(func_5757_call(), 1)
var_8643 = relay.var("var_8643", dtype = "float64", shape = (140,))#candidate|8643|(140,)|var|float64
bop_8644 = relay.power(call_8640.astype('float32'), relay.reshape(var_8643.astype('float32'), relay.shape_of(call_8640))) # shape=(140,)
bop_8647 = relay.power(call_8641.astype('float32'), relay.reshape(var_8643.astype('float32'), relay.shape_of(call_8641))) # shape=(140,)
func_8191_call = mod.get_global_var('func_8191')
func_8194_call = mutated_mod.get_global_var('func_8194')
const_8651 = relay.const([[-4,4,-3,-9,7,-1,8,4,9,4,-4,-5,10,-2,3,4,-9,3,-9,4,-8,-10,5,8,7,-1,-10,9,2,3,-5,1,7,6,6,-1,-7,3,-6,-5,-6,4,-5,-5,4,10,-9,5,-5,-2,-3,9,8,1,6,7,-6,-5,-5,6,10,-3,9,5,-1,6,3,-5,9,5,5,7,-4,-10,5,-10,-4,-6,-1,6,9,5,1,-5,7,8,-3,-3,7,5,1,-7,-8,-9,-3,10,-1,5,6,-4,1,5,5,10,1,-4,-3,-1,-3,10,7,9,9,-10,6,-8,-6,-1,-2,2,8,-8,-8,-2,9,-6,-3,2,1,-7,-6,5,9,-2,9,-4,2,6,9,1,-9,4,-4,-4,-8,1,5,7,-2,-4,-5,-5,-10,-8,-8,-9,-6,9,-9,4,-5,3,-8,5,-9,10,7,2,-6,-8,-9,-1,10,-6,6,-6,4,-10,-10,-4,-4,-7,-10,2,-1,-2,9,-7,5,8,5,2]], dtype = "int64")#candidate|8651|(1, 192)|const|int64
call_8650 = relay.TupleGetItem(func_8191_call(relay.reshape(const_8651.astype('int64'), [12, 2, 8]), relay.reshape(const_8651.astype('int64'), [12, 2, 8]), ), 0)
call_8652 = relay.TupleGetItem(func_8194_call(relay.reshape(const_8651.astype('int64'), [12, 2, 8]), relay.reshape(const_8651.astype('int64'), [12, 2, 8]), ), 0)
func_6335_call = mod.get_global_var('func_6335')
func_6339_call = mutated_mod.get_global_var('func_6339')
var_8675 = relay.var("var_8675", dtype = "float32", shape = (252,))#candidate|8675|(252,)|var|float32
const_8676 = relay.const([-1,-8,4,-3,9,-4,-1,3,2,-10,-6,-7,4,10,-7], dtype = "uint8")#candidate|8676|(15,)|const|uint8
call_8674 = relay.TupleGetItem(func_6335_call(relay.reshape(var_8675.astype('float32'), [252,]), relay.reshape(const_8676.astype('uint8'), [15, 1]), ), 1)
call_8677 = relay.TupleGetItem(func_6339_call(relay.reshape(var_8675.astype('float32'), [252,]), relay.reshape(const_8676.astype('uint8'), [15, 1]), ), 1)
output = relay.Tuple([bop_8644,call_8650,const_8651,call_8674,var_8675,const_8676,])
output2 = relay.Tuple([bop_8647,call_8652,const_8651,call_8677,var_8675,const_8676,])
func_8680 = relay.Function([var_8643,var_8675,], output)
mod['func_8680'] = func_8680
mod = relay.transform.InferType()(mod)
var_8681 = relay.var("var_8681", dtype = "float64", shape = (140,))#candidate|8681|(140,)|var|float64
var_8682 = relay.var("var_8682", dtype = "float32", shape = (252,))#candidate|8682|(252,)|var|float32
output = func_8680(var_8681,var_8682,)
func_8683 = relay.Function([var_8681,var_8682,], output)
mutated_mod['func_8683'] = func_8683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2619_call = mod.get_global_var('func_2619')
func_2621_call = mutated_mod.get_global_var('func_2621')
call_8713 = relay.TupleGetItem(func_2619_call(), 0)
call_8714 = relay.TupleGetItem(func_2621_call(), 0)
output = call_8713
output2 = call_8714
func_8727 = relay.Function([], output)
mod['func_8727'] = func_8727
mod = relay.transform.InferType()(mod)
output = func_8727()
func_8728 = relay.Function([], output)
mutated_mod['func_8728'] = func_8728
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8810 = relay.var("var_8810", dtype = "float64", shape = (2, 15, 1))#candidate|8810|(2, 15, 1)|var|float64
var_8811 = relay.var("var_8811", dtype = "float64", shape = (2, 15, 11))#candidate|8811|(2, 15, 11)|var|float64
bop_8812 = relay.subtract(var_8810.astype('float64'), var_8811.astype('float64')) # shape=(2, 15, 11)
func_7692_call = mod.get_global_var('func_7692')
func_7695_call = mutated_mod.get_global_var('func_7695')
var_8821 = relay.var("var_8821", dtype = "float64", shape = (600,))#candidate|8821|(600,)|var|float64
var_8822 = relay.var("var_8822", dtype = "float32", shape = (98,))#candidate|8822|(98,)|var|float32
call_8820 = relay.TupleGetItem(func_7692_call(relay.reshape(var_8821.astype('float64'), [8, 15, 5]), relay.reshape(var_8822.astype('float32'), [98,]), ), 5)
call_8823 = relay.TupleGetItem(func_7695_call(relay.reshape(var_8821.astype('float64'), [8, 15, 5]), relay.reshape(var_8822.astype('float32'), [98,]), ), 5)
func_694_call = mod.get_global_var('func_694')
func_695_call = mutated_mod.get_global_var('func_695')
call_8824 = relay.TupleGetItem(func_694_call(), 1)
call_8825 = relay.TupleGetItem(func_695_call(), 1)
func_2997_call = mod.get_global_var('func_2997')
func_2999_call = mutated_mod.get_global_var('func_2999')
call_8830 = relay.TupleGetItem(func_2997_call(), 0)
call_8831 = relay.TupleGetItem(func_2999_call(), 0)
output = relay.Tuple([bop_8812,call_8820,var_8821,var_8822,call_8824,call_8830,])
output2 = relay.Tuple([bop_8812,call_8823,var_8821,var_8822,call_8825,call_8831,])
func_8833 = relay.Function([var_8810,var_8811,var_8821,var_8822,], output)
mod['func_8833'] = func_8833
mod = relay.transform.InferType()(mod)
var_8834 = relay.var("var_8834", dtype = "float64", shape = (2, 15, 1))#candidate|8834|(2, 15, 1)|var|float64
var_8835 = relay.var("var_8835", dtype = "float64", shape = (2, 15, 11))#candidate|8835|(2, 15, 11)|var|float64
var_8836 = relay.var("var_8836", dtype = "float64", shape = (600,))#candidate|8836|(600,)|var|float64
var_8837 = relay.var("var_8837", dtype = "float32", shape = (98,))#candidate|8837|(98,)|var|float32
output = func_8833(var_8834,var_8835,var_8836,var_8837,)
func_8838 = relay.Function([var_8834,var_8835,var_8836,var_8837,], output)
mutated_mod['func_8838'] = func_8838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7388_call = mod.get_global_var('func_7388')
func_7390_call = mutated_mod.get_global_var('func_7390')
call_8920 = relay.TupleGetItem(func_7388_call(), 0)
call_8921 = relay.TupleGetItem(func_7390_call(), 0)
output = call_8920
output2 = call_8921
func_8948 = relay.Function([], output)
mod['func_8948'] = func_8948
mod = relay.transform.InferType()(mod)
mutated_mod['func_8948'] = func_8948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8948_call = mutated_mod.get_global_var('func_8948')
call_8949 = func_8948_call()
output = call_8949
func_8950 = relay.Function([], output)
mutated_mod['func_8950'] = func_8950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7312_call = mod.get_global_var('func_7312')
func_7313_call = mutated_mod.get_global_var('func_7313')
call_9023 = relay.TupleGetItem(func_7312_call(), 0)
call_9024 = relay.TupleGetItem(func_7313_call(), 0)
output = relay.Tuple([call_9023,])
output2 = relay.Tuple([call_9024,])
func_9028 = relay.Function([], output)
mod['func_9028'] = func_9028
mod = relay.transform.InferType()(mod)
mutated_mod['func_9028'] = func_9028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9028_call = mutated_mod.get_global_var('func_9028')
call_9029 = func_9028_call()
output = call_9029
func_9030 = relay.Function([], output)
mutated_mod['func_9030'] = func_9030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8417_call = mod.get_global_var('func_8417')
func_8418_call = mutated_mod.get_global_var('func_8418')
call_9095 = func_8417_call()
call_9096 = func_8417_call()
func_1219_call = mod.get_global_var('func_1219')
func_1220_call = mutated_mod.get_global_var('func_1220')
call_9097 = relay.TupleGetItem(func_1219_call(), 2)
call_9098 = relay.TupleGetItem(func_1220_call(), 2)
func_7054_call = mod.get_global_var('func_7054')
func_7056_call = mutated_mod.get_global_var('func_7056')
call_9101 = relay.TupleGetItem(func_7054_call(), 2)
call_9102 = relay.TupleGetItem(func_7056_call(), 2)
output = relay.Tuple([call_9095,call_9097,call_9101,])
output2 = relay.Tuple([call_9096,call_9098,call_9102,])
func_9116 = relay.Function([], output)
mod['func_9116'] = func_9116
mod = relay.transform.InferType()(mod)
output = func_9116()
func_9117 = relay.Function([], output)
mutated_mod['func_9117'] = func_9117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1467_call = mod.get_global_var('func_1467')
func_1468_call = mutated_mod.get_global_var('func_1468')
call_9140 = relay.TupleGetItem(func_1467_call(), 0)
call_9141 = relay.TupleGetItem(func_1468_call(), 0)
uop_9145 = relay.sigmoid(call_9140.astype('float32')) # shape=(252,)
uop_9147 = relay.sigmoid(call_9141.astype('float32')) # shape=(252,)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_9170 = relay.TupleGetItem(func_971_call(), 2)
call_9171 = relay.TupleGetItem(func_973_call(), 2)
func_4238_call = mod.get_global_var('func_4238')
func_4239_call = mutated_mod.get_global_var('func_4239')
call_9173 = relay.TupleGetItem(func_4238_call(), 0)
call_9174 = relay.TupleGetItem(func_4239_call(), 0)
func_2997_call = mod.get_global_var('func_2997')
func_2999_call = mutated_mod.get_global_var('func_2999')
call_9185 = relay.TupleGetItem(func_2997_call(), 1)
call_9186 = relay.TupleGetItem(func_2999_call(), 1)
output = relay.Tuple([uop_9145,call_9170,call_9173,call_9185,])
output2 = relay.Tuple([uop_9147,call_9171,call_9174,call_9186,])
func_9192 = relay.Function([], output)
mod['func_9192'] = func_9192
mod = relay.transform.InferType()(mod)
mutated_mod['func_9192'] = func_9192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9192_call = mutated_mod.get_global_var('func_9192')
call_9193 = func_9192_call()
output = call_9193
func_9194 = relay.Function([], output)
mutated_mod['func_9194'] = func_9194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1467_call = mod.get_global_var('func_1467')
func_1468_call = mutated_mod.get_global_var('func_1468')
call_9285 = relay.TupleGetItem(func_1467_call(), 0)
call_9286 = relay.TupleGetItem(func_1468_call(), 0)
output = relay.Tuple([call_9285,])
output2 = relay.Tuple([call_9286,])
func_9302 = relay.Function([], output)
mod['func_9302'] = func_9302
mod = relay.transform.InferType()(mod)
mutated_mod['func_9302'] = func_9302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9302_call = mutated_mod.get_global_var('func_9302')
call_9303 = func_9302_call()
output = call_9303
func_9304 = relay.Function([], output)
mutated_mod['func_9304'] = func_9304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2997_call = mod.get_global_var('func_2997')
func_2999_call = mutated_mod.get_global_var('func_2999')
call_9322 = relay.TupleGetItem(func_2997_call(), 0)
call_9323 = relay.TupleGetItem(func_2999_call(), 0)
output = call_9322
output2 = call_9323
func_9328 = relay.Function([], output)
mod['func_9328'] = func_9328
mod = relay.transform.InferType()(mod)
output = func_9328()
func_9329 = relay.Function([], output)
mutated_mod['func_9329'] = func_9329
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9333 = relay.var("var_9333", dtype = "float32", shape = (14, 7, 16))#candidate|9333|(14, 7, 16)|var|float32
uop_9334 = relay.rsqrt(var_9333.astype('float32')) # shape=(14, 7, 16)
output = relay.Tuple([uop_9334,])
output2 = relay.Tuple([uop_9334,])
F = relay.Function([var_9333,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9333,], output2)
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
