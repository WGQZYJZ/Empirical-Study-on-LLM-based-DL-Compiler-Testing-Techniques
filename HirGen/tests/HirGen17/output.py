import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_127 = relay.const([[[-2.422401,7.558609,-0.685412,4.417419,-0.236175],[7.190591,7.640956,1.633730,8.430392,6.598367],[-7.309137,8.198094,6.059211,-0.283325,0.732450],[-0.095361,-1.924412,-5.073569,5.249195,-8.532342],[0.490622,-3.540919,-3.890757,-4.584083,8.760422],[8.355136,9.625088,-2.992470,-2.110641,8.877065]],[[2.149497,-5.665052,-3.019165,-3.655476,-1.953178],[2.965893,-0.115807,-8.427892,4.958158,0.492880],[-9.664539,4.343612,2.519608,-2.039190,-6.497141],[6.730078,-2.347919,8.787660,-7.420297,-9.380175],[4.268594,-0.682524,3.552295,-5.861878,4.400264],[1.326384,7.279167,-9.051940,5.295831,-2.761065]],[[-2.763103,7.952408,8.100273,4.830560,-4.933733],[-2.340868,-5.736571,9.391320,5.324961,-1.483019],[6.462216,2.416268,-9.957006,5.338968,-9.339994],[6.749676,-3.653148,7.432516,-7.583023,8.434093],[7.593649,-8.498281,9.154529,0.150291,5.300851],[6.567259,-6.864926,0.980751,-5.312776,-1.964865]],[[5.313812,-8.464639,-5.973905,8.492279,-8.131444],[6.414412,6.542065,9.477402,0.457451,3.898575],[7.128054,-2.927009,6.482352,-7.834856,-6.678358],[1.530812,7.778231,6.171338,5.351320,-0.070118],[-7.297549,8.294215,3.265582,-9.745583,-8.367312],[9.029646,-2.982232,0.671153,-6.729282,-8.313016]]], dtype = "float32")#candidate|127|(4, 6, 5)|const|float32
uop_128 = relay.asin(const_127.astype('float32')) # shape=(4, 6, 5)
const_131 = relay.const([[[-9.276120,3.304027,-5.454482,-1.033785,6.164360],[-1.376316,-3.414907,-5.997556,7.525843,2.983965],[-6.100374,4.800664,-9.666170,9.979664,-5.232397],[-0.662771,9.976464,9.172989,1.651495,-5.519499],[-4.411715,1.148828,-4.003313,9.394217,-1.179693],[-1.972414,6.457182,-5.655224,7.895196,4.404041]],[[-6.337315,-9.643858,2.744985,-0.706912,2.144935],[-6.545514,4.297984,3.704020,3.559144,-3.315206],[3.407192,-7.433455,-3.204157,7.529359,9.292552],[6.621395,-2.312670,0.625524,1.817207,-7.951150],[4.212055,-3.851996,-6.635478,-2.927746,8.011731],[6.358793,-0.084189,1.257624,5.340643,-2.966921]],[[6.736241,-2.638938,6.720802,2.717637,6.377897],[-8.874421,-5.899732,-7.444795,-2.974285,-1.229730],[6.879178,-8.966755,-4.271911,-4.643561,-1.155453],[-9.727102,4.778258,8.906330,-8.800234,1.012971],[-9.246982,-0.601368,9.939585,4.219105,-1.826744],[7.990986,-4.977496,3.387273,0.455896,-3.746550]],[[-1.021695,3.132484,3.831893,-7.858010,4.307082],[-0.518070,0.803862,8.950696,4.082881,-0.396411],[-4.592694,1.807097,-7.145055,0.336310,-6.260834],[7.449027,-2.763552,-9.295152,-7.668029,-3.583021],[7.291753,4.206128,9.671312,9.928746,-8.110725],[-3.541435,4.975636,9.628042,-3.657310,6.011317]]], dtype = "float32")#candidate|131|(4, 6, 5)|const|float32
bop_132 = relay.bitwise_and(uop_128.astype('uint64'), relay.reshape(const_131.astype('uint64'), relay.shape_of(uop_128))) # shape=(4, 6, 5)
output = bop_132
output2 = bop_132
func_135 = relay.Function([], output)
mod['func_135'] = func_135
mod = relay.transform.InferType()(mod)
output = func_135()
func_136 = relay.Function([], output)
mutated_mod['func_136'] = func_136
mutated_mod = relay.transform.InferType()(mutated_mod)
var_177 = relay.var("var_177", dtype = "float64", shape = (14, 13, 2))#candidate|177|(14, 13, 2)|var|float64
uop_178 = relay.acosh(var_177.astype('float64')) # shape=(14, 13, 2)
output = uop_178
output2 = uop_178
func_184 = relay.Function([var_177,], output)
mod['func_184'] = func_184
mod = relay.transform.InferType()(mod)
var_185 = relay.var("var_185", dtype = "float64", shape = (14, 13, 2))#candidate|185|(14, 13, 2)|var|float64
output = func_184(var_185)
func_186 = relay.Function([var_185], output)
mutated_mod['func_186'] = func_186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_191 = func_135_call()
call_192 = func_135_call()
func_184_call = mod.get_global_var('func_184')
func_186_call = mutated_mod.get_global_var('func_186')
const_194 = relay.const([8.856961,3.666975,0.672776,9.949732,5.263920,1.467286,-7.756899,-5.612415,7.811515,-5.018752,3.234580,5.768278,0.242498,-2.202059,7.839291,-6.029128,8.858365,5.775955,-5.184206,4.215964,6.372465,8.323005,3.484707,3.993764,-7.338070,3.914204,2.946177,5.892280,6.384994,5.036525,7.194839,2.013328,4.854000,-0.114561,5.947574,-7.590568,-1.150164,-5.762893,2.448055,-4.984791,-8.249883,0.651045,8.153157,-3.014334,-2.900454,1.626802,1.997339,-3.091109,-0.074531,-9.673857,-7.834518,-6.743868,4.541419,-1.038351,-7.106549,-1.668608,0.882006,0.353066,4.869698,4.886244,5.241209,2.619229,3.397316,-2.226749,-0.647344,-7.217385,8.231623,2.199244,8.417397,1.404655,2.440730,-6.615415,-9.615015,8.963246,-7.349108,2.234977,4.350332,-4.223889,8.353675,-7.883962,-9.808768,-6.662115,-6.749665,-2.847044,-5.831248,7.156316,8.867056,-3.526959,1.420180,7.381725,-3.219501,-2.120884,-7.196410,-3.105279,4.164859,9.015585,9.566778,6.864344,-1.294772,-6.456776,1.699248,-3.039438,2.869862,-1.664604,-4.035614,-0.212692,1.708097,-2.828543,-8.711124,9.041552,-8.104259,9.687356,-2.358961,2.431221,-5.764501,9.850751,9.846794,-8.593697,-9.712874,-1.025787,4.657661,0.917631,8.430112,-4.095806,2.045015,0.349140,-8.960327,1.529239,7.392145,6.507976,-6.013672,7.760593,-9.915768,1.293063,8.857854,0.440307,-1.361259,8.242858,4.835061,5.659145,5.008857,-7.793304,6.730614,-4.364488,-5.090943,-5.132696,3.220725,-6.209425,-4.943600,-2.982446,2.693802,-8.602417,2.152444,4.682864,9.105989,8.199619,5.288517,-8.932601,5.989831,3.507981,9.607553,8.406697,-7.282363,-2.821548,0.582534,-7.539989,7.600354,-9.548627,-9.990971,7.504717,0.191924,-4.151624,-0.233940,6.227752,7.160455,4.826381,9.686349,6.749534,-5.605717,-1.380831,9.003092,7.211947,4.214379,2.199608,6.457019,8.041979,6.210665,-0.727852,-9.124312,7.693773,-3.535830,-0.999441,2.921151,5.593424,-3.606960,0.660966,-3.001376,-4.480947,6.693623,1.317164,-9.345856,2.523661,-3.374370,4.589689,0.954382,3.836605,6.492478,9.560129,1.253222,-8.027893,-0.040314,9.182018,-8.266466,-0.847067,5.309591,4.807838,-8.886499,7.034653,-3.548465,-0.464361,-6.018131,0.345980,1.642134,-9.321985,-3.485394,-1.710779,2.835569,4.323442,8.905690,0.304946,-7.989303,-4.316237,7.547266,3.445443,-6.066268,6.458652,8.281184,-5.645290,-8.360394,-9.859036,-0.972424,9.909301,-6.813523,1.309496,1.057334,5.453979,9.977286,-9.684694,7.241127,-0.772688,4.579056,-6.206528,1.096691,-5.167274,-6.190342,-1.149847,7.604580,-6.230430,-1.967914,-1.569778,-9.821175,4.836476,4.590202,-7.720095,-4.073510,8.286268,-2.333816,-6.827585,-1.870106,6.861542,3.982337,2.698396,-9.635792,4.609927,-3.810852,-3.096302,2.002645,-3.428634,9.337118,9.126427,-9.612027,-7.747767,1.362960,-7.517236,7.252998,-3.742540,6.930769,9.579203,9.271708,-0.944624,-7.237202,-9.606097,0.876644,2.582668,8.424276,-4.320279,2.756027,-0.494911,2.177756,-2.792572,7.994977,-2.458604,2.848198,-3.198261,-6.503871,-3.805926,1.361251,-8.884815,6.173271,6.023252,-3.621580,-3.921377,-3.329016,-0.301130,1.120039,-8.482504,6.234959,4.687961,2.038817,9.809336,0.352507,-0.407468,-6.077025,6.487814,-0.095929,-7.970321,-5.345802,-4.444989,-3.648014,-5.855716,-3.875026,-2.262010,9.543348,-1.439819,1.846571,-7.284656,2.026044,1.182375,4.788319,5.647757,3.522353,2.156264,1.760800,5.431457,-2.383435,6.924248,-4.148299,3.123149,-0.002650,-5.055147,1.084503,-0.054286,-9.021225,0.139030,-9.296445,1.837244,-0.626460,4.309654,2.038530,0.935332,-4.820105,-6.103666,-4.719761,4.844823], dtype = "float64")#candidate|194|(364,)|const|float64
call_193 = func_184_call(relay.reshape(const_194.astype('float64'), [14, 13, 2]))
call_195 = func_184_call(relay.reshape(const_194.astype('float64'), [14, 13, 2]))
func_184_call = mod.get_global_var('func_184')
func_186_call = mutated_mod.get_global_var('func_186')
call_216 = func_184_call(relay.reshape(call_193.astype('float64'), [14, 13, 2]))
call_217 = func_184_call(relay.reshape(call_193.astype('float64'), [14, 13, 2]))
uop_228 = relay.log10(call_193.astype('float32')) # shape=(14, 13, 2)
uop_230 = relay.log10(call_195.astype('float32')) # shape=(14, 13, 2)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_239 = func_135_call()
call_240 = func_135_call()
output = relay.Tuple([call_191,const_194,call_216,uop_228,call_239,])
output2 = relay.Tuple([call_192,const_194,call_217,uop_230,call_240,])
func_242 = relay.Function([], output)
mod['func_242'] = func_242
mod = relay.transform.InferType()(mod)
mutated_mod['func_242'] = func_242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_242_call = mutated_mod.get_global_var('func_242')
call_243 = func_242_call()
output = call_243
func_244 = relay.Function([], output)
mutated_mod['func_244'] = func_244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_250 = func_135_call()
call_251 = func_135_call()
output = relay.Tuple([call_250,])
output2 = relay.Tuple([call_251,])
func_256 = relay.Function([], output)
mod['func_256'] = func_256
mod = relay.transform.InferType()(mod)
mutated_mod['func_256'] = func_256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_256_call = mutated_mod.get_global_var('func_256')
call_257 = func_256_call()
output = call_257
func_258 = relay.Function([], output)
mutated_mod['func_258'] = func_258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_312 = func_135_call()
call_313 = func_135_call()
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_320 = relay.TupleGetItem(func_256_call(), 0)
call_321 = relay.TupleGetItem(func_258_call(), 0)
func_184_call = mod.get_global_var('func_184')
func_186_call = mutated_mod.get_global_var('func_186')
const_326 = relay.const([-6.723892,-9.428329,7.965534,1.709929,-0.307421,-6.030305,-6.975184,-1.430686,-4.264321,5.496195,0.951779,3.970717,0.535943,-5.068418,-7.824310,-0.733976,-0.021078,-3.041896,7.198870,-5.163905,8.322080,-9.679740,9.034912,5.492288,2.522284,5.410670,-6.728429,6.774943,-4.524977,2.782808,8.633588,1.786838,-2.102554,7.254101,2.452036,-0.556329,-7.127141,9.253738,3.826163,-2.583136,5.558428,9.732094,-3.878719,2.648204,-0.892586,1.894455,9.747720,-5.478946,2.711837,3.419713,2.181863,5.340452,-7.773338,2.663289,3.667799,-0.638089,4.983320,0.078539,-2.380050,4.525699,6.115207,-1.070076,4.834674,-1.588591,3.681642,-2.483527,4.634785,-2.122497,-8.981942,-6.314541,1.683889,-1.312973,-7.503903,3.088868,8.975723,-8.496275,2.901292,3.498977,5.401801,7.895058,9.492014,5.923130,7.646462,-7.020464,1.750406,-8.387680,-2.848325,0.995343,-2.366602,7.237262,8.075527,-2.412916,2.153305,-9.411665,2.137360,6.018164,7.670195,-9.486980,-8.981785,-9.520946,6.346167,3.105127,2.387450,-2.683829,7.710658,5.339329,7.477167,0.919882,8.774290,1.065749,-2.493966,3.043832,5.846447,-8.565069,8.652946,7.617050,1.267472,-7.736356,-8.348074,-9.128643,-7.478698,-1.008320,9.317489,-6.748005,9.100989,-0.978248,-8.029672,6.186356,1.972043,-6.954956,-0.134434,3.130591,-6.309143,2.034562,-2.744654,-1.133914,4.291578,3.413216,-6.119687,-1.937944,9.985093,9.505721,-7.112732,-6.150224,2.187552,-3.223457,-4.046284,4.451681,1.943262,9.301284,7.320260,0.956108,5.651718,4.047720,-3.808094,7.505075,-8.732799,-2.036765,-0.327948,-0.227190,5.529329,9.545883,-2.784397,-0.467654,9.942359,-7.516845,0.296154,-0.308860,-0.690138,-0.533921,5.155554,-8.176247,2.313437,-0.894646,7.792568,4.614245,-3.103370,7.747635,7.695482,-2.836917,2.685167,5.073409,-3.730026,3.941927,-4.280207,-0.902878,-6.873724,7.709374,6.063265,0.635288,8.717397,6.791993,8.153322,-3.808309,-0.800126,-6.859831,7.204353,-5.087350,1.533629,-8.585565,7.867249,0.757601,-7.091834,1.849244,-7.151419,-1.711189,9.679626,8.543270,-8.338876,-0.529977,0.410237,0.163297,-1.928501,-2.891591,4.131756,8.764913,2.594266,-8.900045,-3.630939,5.316056,-9.188112,-6.345210,9.428725,6.459248,9.128098,-9.019182,-6.503379,-9.820476,1.235065,-0.354170,8.980303,-5.229913,-1.275805,-5.963950,-0.532990,1.303268,-8.976350,8.699230,-6.914726,1.290398,-0.145238,-7.878580,8.521790,6.467083,0.885003,-9.628005,-6.314650,-5.540327,6.643798,7.261819,-3.649707,5.739460,-2.362918,6.363815,6.632542,-8.231813,-2.614027,-8.964830,3.706334,8.735312,8.124103,-9.275417,-9.846354,-8.426059,0.920781,7.296946,-6.287454,-8.067420,4.303364,4.335219,5.555256,-6.176280,-9.897349,5.136341,0.680031,4.874700,-1.016988,-1.684820,-3.497318,8.585079,-7.248302,6.846536,5.638328,9.702036,9.771461,3.264933,-6.933938,9.230464,-3.100906,1.975053,6.465245,-4.850808,-6.984394,-4.611688,0.789272,-6.971409,-6.879567,-6.271348,-0.732396,5.216634,5.212538,-8.962419,-3.780754,-7.836784,-5.944539,-2.596878,-7.751883,-4.645082,5.288641,7.070765,-0.377211,-7.649451,-5.350733,-7.517366,-0.364829,-0.472527,-7.910328,-7.318322,-0.988936,2.125760,-9.494688,-4.894733,-0.783245,8.969125,8.286892,-2.509498,-5.163318,9.874690,7.425178,4.712608,2.266440,8.402748,-9.614577,-7.175367,8.745011,-5.593816,-2.410855,-4.191788,3.622198,-7.419011,7.520650,-7.599273,-0.317520,-0.895120,9.741025,4.945739,7.844598,-1.807371,-5.186745,6.568915,-6.068591,6.713093,-1.328424,5.382768,8.276731,8.235241,-0.258115,1.434206,0.052009,-9.531935,4.222908,0.227910,6.173949,3.082616], dtype = "float64")#candidate|326|(364,)|const|float64
call_325 = func_184_call(relay.reshape(const_326.astype('float64'), [14, 13, 2]))
call_327 = func_184_call(relay.reshape(const_326.astype('float64'), [14, 13, 2]))
uop_333 = relay.acosh(call_312.astype('float64')) # shape=(4, 6, 5)
uop_335 = relay.acosh(call_313.astype('float64')) # shape=(4, 6, 5)
output = relay.Tuple([call_320,call_325,const_326,uop_333,])
output2 = relay.Tuple([call_321,call_327,const_326,uop_335,])
func_336 = relay.Function([], output)
mod['func_336'] = func_336
mod = relay.transform.InferType()(mod)
mutated_mod['func_336'] = func_336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_336_call = mutated_mod.get_global_var('func_336')
call_337 = func_336_call()
output = call_337
func_338 = relay.Function([], output)
mutated_mod['func_338'] = func_338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_350 = relay.TupleGetItem(func_256_call(), 0)
call_351 = relay.TupleGetItem(func_258_call(), 0)
uop_355 = relay.log10(call_350.astype('float64')) # shape=(4, 6, 5)
uop_357 = relay.log10(call_351.astype('float64')) # shape=(4, 6, 5)
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_362 = relay.TupleGetItem(func_256_call(), 0)
call_363 = relay.TupleGetItem(func_258_call(), 0)
output = relay.Tuple([uop_355,call_362,])
output2 = relay.Tuple([uop_357,call_363,])
func_380 = relay.Function([], output)
mod['func_380'] = func_380
mod = relay.transform.InferType()(mod)
output = func_380()
func_381 = relay.Function([], output)
mutated_mod['func_381'] = func_381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_387 = func_135_call()
call_388 = func_135_call()
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_393 = relay.TupleGetItem(func_380_call(), 1)
call_394 = relay.TupleGetItem(func_381_call(), 1)
output = relay.Tuple([call_387,call_393,])
output2 = relay.Tuple([call_388,call_394,])
func_402 = relay.Function([], output)
mod['func_402'] = func_402
mod = relay.transform.InferType()(mod)
output = func_402()
func_403 = relay.Function([], output)
mutated_mod['func_403'] = func_403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_450 = relay.TupleGetItem(func_256_call(), 0)
call_451 = relay.TupleGetItem(func_258_call(), 0)
func_336_call = mod.get_global_var('func_336')
func_338_call = mutated_mod.get_global_var('func_338')
call_457 = relay.TupleGetItem(func_336_call(), 3)
call_458 = relay.TupleGetItem(func_338_call(), 3)
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_460 = relay.TupleGetItem(func_256_call(), 0)
call_461 = relay.TupleGetItem(func_258_call(), 0)
func_242_call = mod.get_global_var('func_242')
func_244_call = mutated_mod.get_global_var('func_244')
call_462 = relay.TupleGetItem(func_242_call(), 4)
call_463 = relay.TupleGetItem(func_244_call(), 4)
output = relay.Tuple([call_450,call_457,call_460,call_462,])
output2 = relay.Tuple([call_451,call_458,call_461,call_463,])
func_472 = relay.Function([], output)
mod['func_472'] = func_472
mod = relay.transform.InferType()(mod)
mutated_mod['func_472'] = func_472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_472_call = mutated_mod.get_global_var('func_472')
call_473 = func_472_call()
output = call_473
func_474 = relay.Function([], output)
mutated_mod['func_474'] = func_474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_402_call = mod.get_global_var('func_402')
func_403_call = mutated_mod.get_global_var('func_403')
call_478 = relay.TupleGetItem(func_402_call(), 1)
call_479 = relay.TupleGetItem(func_403_call(), 1)
func_184_call = mod.get_global_var('func_184')
func_186_call = mutated_mod.get_global_var('func_186')
var_516 = relay.var("var_516", dtype = "float64", shape = (364,))#candidate|516|(364,)|var|float64
call_515 = func_184_call(relay.reshape(var_516.astype('float64'), [14, 13, 2]))
call_517 = func_184_call(relay.reshape(var_516.astype('float64'), [14, 13, 2]))
var_525 = relay.var("var_525", dtype = "uint64", shape = (4, 6, 5))#candidate|525|(4, 6, 5)|var|uint64
bop_526 = relay.power(call_478.astype('float64'), relay.reshape(var_525.astype('float64'), relay.shape_of(call_478))) # shape=(4, 6, 5)
bop_529 = relay.power(call_479.astype('float64'), relay.reshape(var_525.astype('float64'), relay.shape_of(call_479))) # shape=(4, 6, 5)
func_184_call = mod.get_global_var('func_184')
func_186_call = mutated_mod.get_global_var('func_186')
call_535 = func_184_call(relay.reshape(call_515.astype('float64'), [14, 13, 2]))
call_536 = func_184_call(relay.reshape(call_515.astype('float64'), [14, 13, 2]))
output = relay.Tuple([call_515,var_516,bop_526,call_535,])
output2 = relay.Tuple([call_517,var_516,bop_529,call_536,])
func_538 = relay.Function([var_516,var_525,], output)
mod['func_538'] = func_538
mod = relay.transform.InferType()(mod)
mutated_mod['func_538'] = func_538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_538_call = mutated_mod.get_global_var('func_538')
var_540 = relay.var("var_540", dtype = "float64", shape = (364,))#candidate|540|(364,)|var|float64
var_541 = relay.var("var_541", dtype = "uint64", shape = (4, 6, 5))#candidate|541|(4, 6, 5)|var|uint64
call_539 = func_538_call(var_540,var_541,)
output = call_539
func_542 = relay.Function([var_540,var_541,], output)
mutated_mod['func_542'] = func_542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_558 = relay.TupleGetItem(func_380_call(), 1)
call_559 = relay.TupleGetItem(func_381_call(), 1)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_573 = func_135_call()
call_574 = func_135_call()
output = relay.Tuple([call_558,call_573,])
output2 = relay.Tuple([call_559,call_574,])
func_577 = relay.Function([], output)
mod['func_577'] = func_577
mod = relay.transform.InferType()(mod)
mutated_mod['func_577'] = func_577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mutated_mod.get_global_var('func_577')
call_578 = func_577_call()
output = call_578
func_579 = relay.Function([], output)
mutated_mod['func_579'] = func_579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_336_call = mod.get_global_var('func_336')
func_338_call = mutated_mod.get_global_var('func_338')
call_605 = relay.TupleGetItem(func_336_call(), 1)
call_606 = relay.TupleGetItem(func_338_call(), 1)
output = call_605
output2 = call_606
func_613 = relay.Function([], output)
mod['func_613'] = func_613
mod = relay.transform.InferType()(mod)
mutated_mod['func_613'] = func_613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_613_call = mutated_mod.get_global_var('func_613')
call_614 = func_613_call()
output = call_614
func_615 = relay.Function([], output)
mutated_mod['func_615'] = func_615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_627 = relay.TupleGetItem(func_577_call(), 1)
call_628 = relay.TupleGetItem(func_579_call(), 1)
output = relay.Tuple([call_627,])
output2 = relay.Tuple([call_628,])
func_654 = relay.Function([], output)
mod['func_654'] = func_654
mod = relay.transform.InferType()(mod)
mutated_mod['func_654'] = func_654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_654_call = mutated_mod.get_global_var('func_654')
call_655 = func_654_call()
output = call_655
func_656 = relay.Function([], output)
mutated_mod['func_656'] = func_656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_654_call = mod.get_global_var('func_654')
func_656_call = mutated_mod.get_global_var('func_656')
call_670 = relay.TupleGetItem(func_654_call(), 0)
call_671 = relay.TupleGetItem(func_656_call(), 0)
output = relay.Tuple([call_670,])
output2 = relay.Tuple([call_671,])
func_674 = relay.Function([], output)
mod['func_674'] = func_674
mod = relay.transform.InferType()(mod)
mutated_mod['func_674'] = func_674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_674_call = mutated_mod.get_global_var('func_674')
call_675 = func_674_call()
output = call_675
func_676 = relay.Function([], output)
mutated_mod['func_676'] = func_676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_689 = relay.TupleGetItem(func_380_call(), 1)
call_690 = relay.TupleGetItem(func_381_call(), 1)
func_654_call = mod.get_global_var('func_654')
func_656_call = mutated_mod.get_global_var('func_656')
call_702 = relay.TupleGetItem(func_654_call(), 0)
call_703 = relay.TupleGetItem(func_656_call(), 0)
output = relay.Tuple([call_689,call_702,])
output2 = relay.Tuple([call_690,call_703,])
func_707 = relay.Function([], output)
mod['func_707'] = func_707
mod = relay.transform.InferType()(mod)
output = func_707()
func_708 = relay.Function([], output)
mutated_mod['func_708'] = func_708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_714 = relay.var("var_714", dtype = "int64", shape = (10, 7, 8))#candidate|714|(10, 7, 8)|var|int64
var_715 = relay.var("var_715", dtype = "int64", shape = (10, 7, 8))#candidate|715|(10, 7, 8)|var|int64
bop_716 = relay.minimum(var_714.astype('int64'), relay.reshape(var_715.astype('int64'), relay.shape_of(var_714))) # shape=(10, 7, 8)
output = bop_716
output2 = bop_716
func_722 = relay.Function([var_714,var_715,], output)
mod['func_722'] = func_722
mod = relay.transform.InferType()(mod)
var_723 = relay.var("var_723", dtype = "int64", shape = (10, 7, 8))#candidate|723|(10, 7, 8)|var|int64
var_724 = relay.var("var_724", dtype = "int64", shape = (10, 7, 8))#candidate|724|(10, 7, 8)|var|int64
output = func_722(var_723,var_724,)
func_725 = relay.Function([var_723,var_724,], output)
mutated_mod['func_725'] = func_725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_472_call = mod.get_global_var('func_472')
func_474_call = mutated_mod.get_global_var('func_474')
call_737 = relay.TupleGetItem(func_472_call(), 3)
call_738 = relay.TupleGetItem(func_474_call(), 3)
func_184_call = mod.get_global_var('func_184')
func_186_call = mutated_mod.get_global_var('func_186')
const_747 = relay.const([[-2.320049,7.259646,8.186073,-0.746034,5.847304,-9.546814,-5.460557,9.731971,5.567164,6.899251,-9.846227,-3.239147,-0.672546,-5.350149,9.484493,-2.168953,4.970226,0.401323,-7.866504,-0.296548,7.508056,0.487346,-9.924439,-9.565502,4.569325,-8.168080,2.016248,-2.571727,-0.368117,-7.082935,-4.475669,8.694965,-4.261390,1.662055,-2.315516,3.373323,-6.184142,2.283562,3.491021,3.385333,1.149163,-3.957562,-1.509926,-3.907308,-9.683551,2.141506,9.340053,-2.595655,7.014952,-5.516945,4.060403,8.196048,5.301028,-3.532071,5.440543,1.912358,2.444389,4.483824,-9.752291,-2.110405,-8.986065,5.766626,1.779450,-8.108276,4.737705,-2.989355,-2.816247,1.468269,5.665593,-1.956485,0.703767,1.828865,9.450938,-2.323602,5.983098,-7.112282,-3.827156,2.674110,5.717985,-9.632300,9.610073,-9.676938,4.833725,7.972547,8.920755,7.165034,3.162688,-0.174616,2.883136,-0.616957,3.125222,-3.562604,-2.807816,7.316629,8.521500,7.968987,1.778260,-6.506838,5.685120,0.934649,9.122753,7.362820,8.694432,-9.871351,-5.321433,8.391520,9.453898,-1.303282,-2.935085,-3.083836,5.590531,-9.413612,8.347458,2.189456,-0.973734,0.281468,1.228688,-8.874500,-8.279659,3.158216,0.973933,4.214231,4.718165,-2.275750,2.714048,5.758309,-3.780539,5.920200,5.669096,-6.657924,1.418191,7.787332,-4.257340,-3.876441,-8.179781,-1.346385,-5.089909,0.341372,8.543697,4.548714,-5.030221,3.466991,-4.230236,-3.088640,-1.430863,0.422246,-9.931938,-1.461258,-0.760765,-0.185059,6.795258,-3.361810,-5.331257,0.626590,-6.037339,-0.214841,1.243392,3.538474,2.032968,2.256759,7.089460,3.318280,-5.737943,-5.955487,-5.798141,4.376364,7.280682,-9.525050,0.795701,8.434333,-9.809047,-4.736189,-9.734382,-8.866388,0.127023,9.833089,-1.328529,7.019334,-5.855790,-5.082496,-9.200077,-8.621683,1.631387,3.119137,-4.536859,-4.996313,-9.353194,6.250007,3.411131,-1.458861,3.402291,2.328199,6.966489,-2.941245,-1.753983,-6.110464,7.650749,5.016121,7.556162,7.336936,1.596575,9.150987,2.877374,-6.033229,-9.904086,0.817120,-8.996081,6.798969,8.910362,-9.336480,-1.099170,-0.818009,3.813159,2.334158,-9.492948,2.674711,-6.109408,-3.555176,8.877426,-3.686574,1.954681,4.341560,-6.201325,3.065743,3.505488,-9.602123,8.808815,1.546210,-3.509171,4.460008,2.157700,-0.017172,4.046753,6.649742,-8.790568,-2.760841,-9.790753,4.466220,3.927624,-5.132735,-6.435836,-6.287421,-5.934590,0.063112,-6.795332,7.434947,0.502725,-4.071559,-3.025371,4.968190,7.270416,0.138600,7.834429,5.895531,9.680761,9.554216,-9.271323,0.628389,6.102622,8.617668,-9.755436,-3.100754,-3.519381,-2.059957,-8.670092,5.068934,-1.019794,4.698764,-1.937143,-0.129700,0.883112,6.978158,1.293664,-0.732346,9.355025,0.056924,-5.006816,4.626453,-5.353152,-0.164995,7.303568,-1.389952,-5.326765,-1.090599,-9.294534,-8.186499,-3.169090,5.632790,4.020993,7.803887,4.507879,-6.959116,-9.490266,1.577971,2.914311,3.920798,4.645440,-0.043099,-6.074722,-1.399774,7.246197,-8.494264,7.668854,-5.804100,3.318568,0.337412,-1.381632,-6.420860,-8.225449,1.531240,0.182348,-9.081770,-3.863727,-0.072899,9.420066,-2.327918,-8.421377,6.869997,-4.173958,-7.854009,2.897204,6.515586,0.965495,-2.013886,5.547665,1.540868,-5.524686,9.066042,8.454382,7.763247,1.485804,0.720482,-8.817858,3.535656,-6.137441,-8.175729,9.982698,8.843729,-9.800065,-7.726132,8.683516,-2.602101,-2.887734,7.918924,-6.923031,-8.139713,-4.543623,8.768177,-4.575121,3.086025,-2.057114,-9.322546,3.557392,-8.335307,7.294689,3.695724,-4.141310,5.271787,-4.911221,-0.231048,2.952841,-0.306069,1.772441,0.910340]], dtype = "float64")#candidate|747|(1, 364)|const|float64
call_746 = func_184_call(relay.reshape(const_747.astype('float64'), [14, 13, 2]))
call_748 = func_184_call(relay.reshape(const_747.astype('float64'), [14, 13, 2]))
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_752 = relay.TupleGetItem(func_380_call(), 1)
call_753 = relay.TupleGetItem(func_381_call(), 1)
output = relay.Tuple([call_737,call_746,const_747,call_752,])
output2 = relay.Tuple([call_738,call_748,const_747,call_753,])
func_764 = relay.Function([], output)
mod['func_764'] = func_764
mod = relay.transform.InferType()(mod)
mutated_mod['func_764'] = func_764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_764_call = mutated_mod.get_global_var('func_764')
call_765 = func_764_call()
output = call_765
func_766 = relay.Function([], output)
mutated_mod['func_766'] = func_766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_853 = relay.TupleGetItem(func_764_call(), 2)
call_854 = relay.TupleGetItem(func_766_call(), 2)
output = call_853
output2 = call_854
func_855 = relay.Function([], output)
mod['func_855'] = func_855
mod = relay.transform.InferType()(mod)
mutated_mod['func_855'] = func_855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_855_call = mutated_mod.get_global_var('func_855')
call_856 = func_855_call()
output = call_856
func_857 = relay.Function([], output)
mutated_mod['func_857'] = func_857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
call_885 = relay.TupleGetItem(func_674_call(), 0)
call_886 = relay.TupleGetItem(func_676_call(), 0)
var_902 = relay.var("var_902", dtype = "uint64", shape = (4, 6, 5))#candidate|902|(4, 6, 5)|var|uint64
bop_903 = relay.subtract(call_885.astype('float64'), relay.reshape(var_902.astype('float64'), relay.shape_of(call_885))) # shape=(4, 6, 5)
bop_906 = relay.subtract(call_886.astype('float64'), relay.reshape(var_902.astype('float64'), relay.shape_of(call_886))) # shape=(4, 6, 5)
uop_908 = relay.cosh(call_885.astype('float32')) # shape=(4, 6, 5)
uop_910 = relay.cosh(call_886.astype('float32')) # shape=(4, 6, 5)
func_242_call = mod.get_global_var('func_242')
func_244_call = mutated_mod.get_global_var('func_244')
call_926 = relay.TupleGetItem(func_242_call(), 1)
call_927 = relay.TupleGetItem(func_244_call(), 1)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_939 = func_135_call()
call_940 = func_135_call()
var_947 = relay.var("var_947", dtype = "float64", shape = (364,))#candidate|947|(364,)|var|float64
bop_948 = relay.power(call_926.astype('float64'), relay.reshape(var_947.astype('float64'), relay.shape_of(call_926))) # shape=(364,)
bop_951 = relay.power(call_927.astype('float64'), relay.reshape(var_947.astype('float64'), relay.shape_of(call_927))) # shape=(364,)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_969 = relay.TupleGetItem(func_577_call(), 1)
call_970 = relay.TupleGetItem(func_579_call(), 1)
bop_973 = relay.right_shift(call_969.astype('int16'), relay.reshape(bop_903.astype('int16'), relay.shape_of(call_969))) # shape=(4, 6, 5)
bop_976 = relay.right_shift(call_970.astype('int16'), relay.reshape(bop_906.astype('int16'), relay.shape_of(call_970))) # shape=(4, 6, 5)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_977 = relay.TupleGetItem(func_380_call(), 0)
call_978 = relay.TupleGetItem(func_381_call(), 0)
output = relay.Tuple([uop_908,call_939,bop_948,bop_973,call_977,])
output2 = relay.Tuple([uop_910,call_940,bop_951,bop_976,call_978,])
func_985 = relay.Function([var_902,var_947,], output)
mod['func_985'] = func_985
mod = relay.transform.InferType()(mod)
mutated_mod['func_985'] = func_985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_985_call = mutated_mod.get_global_var('func_985')
var_987 = relay.var("var_987", dtype = "uint64", shape = (4, 6, 5))#candidate|987|(4, 6, 5)|var|uint64
var_988 = relay.var("var_988", dtype = "float64", shape = (364,))#candidate|988|(364,)|var|float64
call_986 = func_985_call(var_987,var_988,)
output = call_986
func_989 = relay.Function([var_987,var_988,], output)
mutated_mod['func_989'] = func_989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_336_call = mod.get_global_var('func_336')
func_338_call = mutated_mod.get_global_var('func_338')
call_1036 = relay.TupleGetItem(func_336_call(), 2)
call_1037 = relay.TupleGetItem(func_338_call(), 2)
output = relay.Tuple([call_1036,])
output2 = relay.Tuple([call_1037,])
func_1038 = relay.Function([], output)
mod['func_1038'] = func_1038
mod = relay.transform.InferType()(mod)
output = func_1038()
func_1039 = relay.Function([], output)
mutated_mod['func_1039'] = func_1039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_1040 = relay.TupleGetItem(func_764_call(), 1)
call_1041 = relay.TupleGetItem(func_766_call(), 1)
var_1043 = relay.var("var_1043", dtype = "float64", shape = (14, 13, 2))#candidate|1043|(14, 13, 2)|var|float64
bop_1044 = relay.power(call_1040.astype('float32'), relay.reshape(var_1043.astype('float32'), relay.shape_of(call_1040))) # shape=(14, 13, 2)
bop_1047 = relay.power(call_1041.astype('float32'), relay.reshape(var_1043.astype('float32'), relay.shape_of(call_1041))) # shape=(14, 13, 2)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_1053 = relay.TupleGetItem(func_764_call(), 1)
call_1054 = relay.TupleGetItem(func_766_call(), 1)
func_613_call = mod.get_global_var('func_613')
func_615_call = mutated_mod.get_global_var('func_615')
call_1056 = func_613_call()
call_1057 = func_613_call()
func_855_call = mod.get_global_var('func_855')
func_857_call = mutated_mod.get_global_var('func_857')
call_1061 = func_855_call()
call_1062 = func_855_call()
var_1066 = relay.var("var_1066", dtype = "float64", shape = (15, 364))#candidate|1066|(15, 364)|var|float64
bop_1067 = relay.not_equal(call_1061.astype('bool'), var_1066.astype('bool')) # shape=(15, 364)
bop_1070 = relay.not_equal(call_1062.astype('bool'), var_1066.astype('bool')) # shape=(15, 364)
output = relay.Tuple([bop_1044,call_1053,call_1056,bop_1067,])
output2 = relay.Tuple([bop_1047,call_1054,call_1057,bop_1070,])
func_1071 = relay.Function([var_1043,var_1066,], output)
mod['func_1071'] = func_1071
mod = relay.transform.InferType()(mod)
mutated_mod['func_1071'] = func_1071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1071_call = mutated_mod.get_global_var('func_1071')
var_1073 = relay.var("var_1073", dtype = "float64", shape = (14, 13, 2))#candidate|1073|(14, 13, 2)|var|float64
var_1074 = relay.var("var_1074", dtype = "float64", shape = (15, 364))#candidate|1074|(15, 364)|var|float64
call_1072 = func_1071_call(var_1073,var_1074,)
output = call_1072
func_1075 = relay.Function([var_1073,var_1074,], output)
mutated_mod['func_1075'] = func_1075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
call_1090 = relay.TupleGetItem(func_674_call(), 0)
call_1091 = relay.TupleGetItem(func_676_call(), 0)
output = call_1090
output2 = call_1091
func_1102 = relay.Function([], output)
mod['func_1102'] = func_1102
mod = relay.transform.InferType()(mod)
mutated_mod['func_1102'] = func_1102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1102_call = mutated_mod.get_global_var('func_1102')
call_1103 = func_1102_call()
output = call_1103
func_1104 = relay.Function([], output)
mutated_mod['func_1104'] = func_1104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_613_call = mod.get_global_var('func_613')
func_615_call = mutated_mod.get_global_var('func_615')
call_1116 = func_613_call()
call_1117 = func_613_call()
var_1120 = relay.var("var_1120", dtype = "float64", shape = (14, 13, 2))#candidate|1120|(14, 13, 2)|var|float64
bop_1121 = relay.less(call_1116.astype('bool'), relay.reshape(var_1120.astype('bool'), relay.shape_of(call_1116))) # shape=(14, 13, 2)
bop_1124 = relay.less(call_1117.astype('bool'), relay.reshape(var_1120.astype('bool'), relay.shape_of(call_1117))) # shape=(14, 13, 2)
func_538_call = mod.get_global_var('func_538')
func_542_call = mutated_mod.get_global_var('func_542')
var_1127 = relay.var("var_1127", dtype = "uint64", shape = (120,))#candidate|1127|(120,)|var|uint64
call_1126 = relay.TupleGetItem(func_538_call(relay.reshape(call_1116.astype('float64'), [364,]), relay.reshape(var_1127.astype('uint64'), [4, 6, 5]), ), 3)
call_1128 = relay.TupleGetItem(func_542_call(relay.reshape(call_1116.astype('float64'), [364,]), relay.reshape(var_1127.astype('uint64'), [4, 6, 5]), ), 3)
output = relay.Tuple([bop_1121,call_1126,var_1127,])
output2 = relay.Tuple([bop_1124,call_1128,var_1127,])
func_1130 = relay.Function([var_1120,var_1127,], output)
mod['func_1130'] = func_1130
mod = relay.transform.InferType()(mod)
var_1131 = relay.var("var_1131", dtype = "float64", shape = (14, 13, 2))#candidate|1131|(14, 13, 2)|var|float64
var_1132 = relay.var("var_1132", dtype = "uint64", shape = (120,))#candidate|1132|(120,)|var|uint64
output = func_1130(var_1131,var_1132,)
func_1133 = relay.Function([var_1131,var_1132,], output)
mutated_mod['func_1133'] = func_1133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_613_call = mod.get_global_var('func_613')
func_615_call = mutated_mod.get_global_var('func_615')
call_1135 = func_613_call()
call_1136 = func_613_call()
func_336_call = mod.get_global_var('func_336')
func_338_call = mutated_mod.get_global_var('func_338')
call_1145 = relay.TupleGetItem(func_336_call(), 3)
call_1146 = relay.TupleGetItem(func_338_call(), 3)
func_1102_call = mod.get_global_var('func_1102')
func_1104_call = mutated_mod.get_global_var('func_1104')
call_1147 = func_1102_call()
call_1148 = func_1102_call()
output = relay.Tuple([call_1135,call_1145,call_1147,])
output2 = relay.Tuple([call_1136,call_1146,call_1148,])
func_1162 = relay.Function([], output)
mod['func_1162'] = func_1162
mod = relay.transform.InferType()(mod)
mutated_mod['func_1162'] = func_1162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1162_call = mutated_mod.get_global_var('func_1162')
call_1163 = func_1162_call()
output = call_1163
func_1164 = relay.Function([], output)
mutated_mod['func_1164'] = func_1164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1206 = relay.var("var_1206", dtype = "float64", shape = (2, 1, 13))#candidate|1206|(2, 1, 13)|var|float64
uop_1207 = relay.sin(var_1206.astype('float64')) # shape=(2, 1, 13)
uop_1209 = relay.tan(uop_1207.astype('float32')) # shape=(2, 1, 13)
uop_1211 = relay.exp(uop_1209.astype('float32')) # shape=(2, 1, 13)
output = relay.Tuple([uop_1211,])
output2 = relay.Tuple([uop_1211,])
func_1219 = relay.Function([var_1206,], output)
mod['func_1219'] = func_1219
mod = relay.transform.InferType()(mod)
mutated_mod['func_1219'] = func_1219
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1220 = relay.var("var_1220", dtype = "float64", shape = (2, 1, 13))#candidate|1220|(2, 1, 13)|var|float64
func_1219_call = mutated_mod.get_global_var('func_1219')
call_1221 = func_1219_call(var_1220)
output = call_1221
func_1222 = relay.Function([var_1220], output)
mutated_mod['func_1222'] = func_1222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_613_call = mod.get_global_var('func_613')
func_615_call = mutated_mod.get_global_var('func_615')
call_1248 = func_613_call()
call_1249 = func_613_call()
output = relay.Tuple([call_1248,])
output2 = relay.Tuple([call_1249,])
func_1250 = relay.Function([], output)
mod['func_1250'] = func_1250
mod = relay.transform.InferType()(mod)
mutated_mod['func_1250'] = func_1250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1250_call = mutated_mod.get_global_var('func_1250')
call_1251 = func_1250_call()
output = call_1251
func_1252 = relay.Function([], output)
mutated_mod['func_1252'] = func_1252
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1263 = relay.var("var_1263", dtype = "float64", shape = (6, 5, 6))#candidate|1263|(6, 5, 6)|var|float64
uop_1264 = relay.rsqrt(var_1263.astype('float64')) # shape=(6, 5, 6)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_1266 = relay.TupleGetItem(func_764_call(), 2)
call_1267 = relay.TupleGetItem(func_766_call(), 2)
uop_1270 = relay.erf(uop_1264.astype('float32')) # shape=(6, 5, 6)
func_722_call = mod.get_global_var('func_722')
func_725_call = mutated_mod.get_global_var('func_725')
var_1274 = relay.var("var_1274", dtype = "int64", shape = (8, 70))#candidate|1274|(8, 70)|var|int64
call_1273 = func_722_call(relay.reshape(var_1274.astype('int64'), [10, 7, 8]), relay.reshape(var_1274.astype('int64'), [10, 7, 8]), )
call_1275 = func_722_call(relay.reshape(var_1274.astype('int64'), [10, 7, 8]), relay.reshape(var_1274.astype('int64'), [10, 7, 8]), )
output = relay.Tuple([call_1266,uop_1270,call_1273,var_1274,])
output2 = relay.Tuple([call_1267,uop_1270,call_1275,var_1274,])
func_1297 = relay.Function([var_1263,var_1274,], output)
mod['func_1297'] = func_1297
mod = relay.transform.InferType()(mod)
mutated_mod['func_1297'] = func_1297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1297_call = mutated_mod.get_global_var('func_1297')
var_1299 = relay.var("var_1299", dtype = "float64", shape = (6, 5, 6))#candidate|1299|(6, 5, 6)|var|float64
var_1300 = relay.var("var_1300", dtype = "int64", shape = (8, 70))#candidate|1300|(8, 70)|var|int64
call_1298 = func_1297_call(var_1299,var_1300,)
output = call_1298
func_1301 = relay.Function([var_1299,var_1300,], output)
mutated_mod['func_1301'] = func_1301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_336_call = mod.get_global_var('func_336')
func_338_call = mutated_mod.get_global_var('func_338')
call_1311 = relay.TupleGetItem(func_336_call(), 0)
call_1312 = relay.TupleGetItem(func_338_call(), 0)
func_1250_call = mod.get_global_var('func_1250')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_1315 = relay.TupleGetItem(func_1250_call(), 0)
call_1316 = relay.TupleGetItem(func_1252_call(), 0)
output = relay.Tuple([call_1311,call_1315,])
output2 = relay.Tuple([call_1312,call_1316,])
func_1317 = relay.Function([], output)
mod['func_1317'] = func_1317
mod = relay.transform.InferType()(mod)
mutated_mod['func_1317'] = func_1317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1317_call = mutated_mod.get_global_var('func_1317')
call_1318 = func_1317_call()
output = call_1318
func_1319 = relay.Function([], output)
mutated_mod['func_1319'] = func_1319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_472_call = mod.get_global_var('func_472')
func_474_call = mutated_mod.get_global_var('func_474')
call_1330 = relay.TupleGetItem(func_472_call(), 0)
call_1331 = relay.TupleGetItem(func_474_call(), 0)
output = relay.Tuple([call_1330,])
output2 = relay.Tuple([call_1331,])
func_1334 = relay.Function([], output)
mod['func_1334'] = func_1334
mod = relay.transform.InferType()(mod)
mutated_mod['func_1334'] = func_1334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1334_call = mutated_mod.get_global_var('func_1334')
call_1335 = func_1334_call()
output = call_1335
func_1336 = relay.Function([], output)
mutated_mod['func_1336'] = func_1336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_1345 = relay.TupleGetItem(func_256_call(), 0)
call_1346 = relay.TupleGetItem(func_258_call(), 0)
output = call_1345
output2 = call_1346
func_1358 = relay.Function([], output)
mod['func_1358'] = func_1358
mod = relay.transform.InferType()(mod)
mutated_mod['func_1358'] = func_1358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1358_call = mutated_mod.get_global_var('func_1358')
call_1359 = func_1358_call()
output = call_1359
func_1360 = relay.Function([], output)
mutated_mod['func_1360'] = func_1360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_1433 = relay.TupleGetItem(func_256_call(), 0)
call_1434 = relay.TupleGetItem(func_258_call(), 0)
func_1102_call = mod.get_global_var('func_1102')
func_1104_call = mutated_mod.get_global_var('func_1104')
call_1435 = func_1102_call()
call_1436 = func_1102_call()
bop_1437 = relay.mod(call_1435.astype('float64'), relay.reshape(call_1433.astype('float64'), relay.shape_of(call_1435))) # shape=(4, 6, 5)
bop_1440 = relay.mod(call_1436.astype('float64'), relay.reshape(call_1434.astype('float64'), relay.shape_of(call_1436))) # shape=(4, 6, 5)
func_472_call = mod.get_global_var('func_472')
func_474_call = mutated_mod.get_global_var('func_474')
call_1446 = relay.TupleGetItem(func_472_call(), 2)
call_1447 = relay.TupleGetItem(func_474_call(), 2)
output = relay.Tuple([bop_1437,call_1446,])
output2 = relay.Tuple([bop_1440,call_1447,])
func_1448 = relay.Function([], output)
mod['func_1448'] = func_1448
mod = relay.transform.InferType()(mod)
output = func_1448()
func_1449 = relay.Function([], output)
mutated_mod['func_1449'] = func_1449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_855_call = mod.get_global_var('func_855')
func_857_call = mutated_mod.get_global_var('func_857')
call_1471 = func_855_call()
call_1472 = func_855_call()
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_1473 = relay.TupleGetItem(func_380_call(), 1)
call_1474 = relay.TupleGetItem(func_381_call(), 1)
var_1476 = relay.var("var_1476", dtype = "float64", shape = (3, 364))#candidate|1476|(3, 364)|var|float64
bop_1477 = relay.greater(call_1471.astype('bool'), var_1476.astype('bool')) # shape=(3, 364)
bop_1480 = relay.greater(call_1472.astype('bool'), var_1476.astype('bool')) # shape=(3, 364)
uop_1505 = relay.rsqrt(call_1471.astype('float32')) # shape=(1, 364)
uop_1507 = relay.rsqrt(call_1472.astype('float32')) # shape=(1, 364)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_1523 = func_135_call()
call_1524 = func_135_call()
func_1317_call = mod.get_global_var('func_1317')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_1525 = relay.TupleGetItem(func_1317_call(), 1)
call_1526 = relay.TupleGetItem(func_1319_call(), 1)
output = relay.Tuple([call_1473,bop_1477,uop_1505,call_1523,call_1525,])
output2 = relay.Tuple([call_1474,bop_1480,uop_1507,call_1524,call_1526,])
func_1528 = relay.Function([var_1476,], output)
mod['func_1528'] = func_1528
mod = relay.transform.InferType()(mod)
mutated_mod['func_1528'] = func_1528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1529 = relay.var("var_1529", dtype = "float64", shape = (3, 364))#candidate|1529|(3, 364)|var|float64
func_1528_call = mutated_mod.get_global_var('func_1528')
call_1530 = func_1528_call(var_1529)
output = call_1530
func_1531 = relay.Function([var_1529], output)
mutated_mod['func_1531'] = func_1531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1038_call = mod.get_global_var('func_1038')
func_1039_call = mutated_mod.get_global_var('func_1039')
call_1552 = relay.TupleGetItem(func_1038_call(), 0)
call_1553 = relay.TupleGetItem(func_1039_call(), 0)
var_1564 = relay.var("var_1564", dtype = "float64", shape = (364,))#candidate|1564|(364,)|var|float64
bop_1565 = relay.bitwise_and(call_1552.astype('int64'), relay.reshape(var_1564.astype('int64'), relay.shape_of(call_1552))) # shape=(364,)
bop_1568 = relay.bitwise_and(call_1553.astype('int64'), relay.reshape(var_1564.astype('int64'), relay.shape_of(call_1553))) # shape=(364,)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_1571 = relay.TupleGetItem(func_380_call(), 1)
call_1572 = relay.TupleGetItem(func_381_call(), 1)
output = relay.Tuple([bop_1565,call_1571,])
output2 = relay.Tuple([bop_1568,call_1572,])
func_1582 = relay.Function([var_1564,], output)
mod['func_1582'] = func_1582
mod = relay.transform.InferType()(mod)
var_1583 = relay.var("var_1583", dtype = "float64", shape = (364,))#candidate|1583|(364,)|var|float64
output = func_1582(var_1583)
func_1584 = relay.Function([var_1583], output)
mutated_mod['func_1584'] = func_1584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1317_call = mod.get_global_var('func_1317')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_1594 = relay.TupleGetItem(func_1317_call(), 0)
call_1595 = relay.TupleGetItem(func_1319_call(), 0)
func_985_call = mod.get_global_var('func_985')
func_989_call = mutated_mod.get_global_var('func_989')
var_1600 = relay.var("var_1600", dtype = "float64", shape = (182, 2))#candidate|1600|(182, 2)|var|float64
call_1599 = relay.TupleGetItem(func_985_call(relay.reshape(call_1594.astype('uint64'), [4, 6, 5]), relay.reshape(var_1600.astype('float64'), [364,]), ), 3)
call_1601 = relay.TupleGetItem(func_989_call(relay.reshape(call_1594.astype('uint64'), [4, 6, 5]), relay.reshape(var_1600.astype('float64'), [364,]), ), 3)
output = relay.Tuple([call_1594,call_1599,var_1600,])
output2 = relay.Tuple([call_1595,call_1601,var_1600,])
func_1614 = relay.Function([var_1600,], output)
mod['func_1614'] = func_1614
mod = relay.transform.InferType()(mod)
var_1615 = relay.var("var_1615", dtype = "float64", shape = (182, 2))#candidate|1615|(182, 2)|var|float64
output = func_1614(var_1615)
func_1616 = relay.Function([var_1615], output)
mutated_mod['func_1616'] = func_1616
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1644 = relay.const(-0.007361, dtype = "float64")#candidate|1644|()|const|float64
var_1645 = relay.var("var_1645", dtype = "float64", shape = (8, 16, 4))#candidate|1645|(8, 16, 4)|var|float64
bop_1646 = relay.divide(const_1644.astype('float64'), var_1645.astype('float64')) # shape=(8, 16, 4)
func_1162_call = mod.get_global_var('func_1162')
func_1164_call = mutated_mod.get_global_var('func_1164')
call_1653 = relay.TupleGetItem(func_1162_call(), 0)
call_1654 = relay.TupleGetItem(func_1164_call(), 0)
output = relay.Tuple([bop_1646,call_1653,])
output2 = relay.Tuple([bop_1646,call_1654,])
func_1659 = relay.Function([var_1645,], output)
mod['func_1659'] = func_1659
mod = relay.transform.InferType()(mod)
var_1660 = relay.var("var_1660", dtype = "float64", shape = (8, 16, 4))#candidate|1660|(8, 16, 4)|var|float64
output = func_1659(var_1660)
func_1661 = relay.Function([var_1660], output)
mutated_mod['func_1661'] = func_1661
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1699 = relay.var("var_1699", dtype = "int32", shape = (14, 4, 1))#candidate|1699|(14, 4, 1)|var|int32
var_1700 = relay.var("var_1700", dtype = "int32", shape = (14, 4, 13))#candidate|1700|(14, 4, 13)|var|int32
bop_1701 = relay.bitwise_and(var_1699.astype('int32'), var_1700.astype('int32')) # shape=(14, 4, 13)
uop_1705 = relay.atanh(bop_1701.astype('float32')) # shape=(14, 4, 13)
uop_1714 = relay.sqrt(uop_1705.astype('float32')) # shape=(14, 4, 13)
uop_1717 = relay.cos(uop_1714.astype('float64')) # shape=(14, 4, 13)
bop_1725 = relay.bitwise_or(uop_1717.astype('int16'), relay.reshape(bop_1701.astype('int16'), relay.shape_of(uop_1717))) # shape=(14, 4, 13)
output = bop_1725
output2 = bop_1725
func_1730 = relay.Function([var_1699,var_1700,], output)
mod['func_1730'] = func_1730
mod = relay.transform.InferType()(mod)
mutated_mod['func_1730'] = func_1730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1730_call = mutated_mod.get_global_var('func_1730')
var_1732 = relay.var("var_1732", dtype = "int32", shape = (14, 4, 1))#candidate|1732|(14, 4, 1)|var|int32
var_1733 = relay.var("var_1733", dtype = "int32", shape = (14, 4, 13))#candidate|1733|(14, 4, 13)|var|int32
call_1731 = func_1730_call(var_1732,var_1733,)
output = call_1731
func_1734 = relay.Function([var_1732,var_1733,], output)
mutated_mod['func_1734'] = func_1734
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1774 = relay.const([[-2.495060,3.075609,-3.178348,3.697647,-9.658345,-5.318279,2.461350]], dtype = "float32")#candidate|1774|(1, 7)|const|float32
uop_1775 = relay.log2(const_1774.astype('float32')) # shape=(1, 7)
func_985_call = mod.get_global_var('func_985')
func_989_call = mutated_mod.get_global_var('func_989')
const_1782 = relay.const([1,-5,-6,4,3,-3,-1,7,-6,4,-4,-7,-6,-2,-10,-5,8,8,10,-7,-4,-5,-7,-6,3,-6,-2,6,3,9,4,-8,5,-6,8,2,-6,-6,7,8,9,7,-7,1,4,5,5,10,-9,-9,-2,8,5,-10,3,-4,-10,-8,-5,-6,1,7,-7,8,-5,-3,-5,4,-5,4,-2,2,1,-8,-9,5,8,-5,-1,10,-7,3,-4,-4,1,6,-8,5,8,-6,-10,6,5,10,2,3,3,-1,-5,5,-5,-1,-9,2,10,6,-1,7,-4,3,8,-5,-2,-7,3,4,5,3,-2,3], dtype = "uint64")#candidate|1782|(120,)|const|uint64
const_1783 = relay.const([1.887289,3.409830,-1.489612,8.251853,1.018826,1.131355,-5.187631,5.203657,1.917372,3.460091,5.549254,-9.494421,0.613104,-7.640421,8.831624,4.519898,8.031425,7.902409,-3.282437,4.724188,-3.191283,-4.498201,7.597127,-8.656581,-8.514016,-3.875240,4.475081,1.509864,-9.501001,8.436009,9.566523,-2.141078,6.718594,-1.126455,-5.825916,1.061673,-1.421375,6.893618,5.820236,-4.279551,8.206078,-7.249047,5.372444,1.419306,3.700712,5.730481,-7.601330,-8.957817,-4.035118,0.345765,-3.940143,2.411883,-3.765289,-7.505925,-9.494640,9.826008,3.590624,-6.486152,8.086796,-3.350273,8.681379,6.591808,2.343070,8.921657,-2.885865,-0.681032,-2.142096,6.734024,-1.870990,-0.822399,0.582135,-1.637292,9.403214,1.130263,8.866659,-2.445259,-6.495434,-9.131957,9.733972,2.285942,-0.099982,-3.197438,7.599799,8.560110,2.347775,-9.610996,1.098600,6.523225,2.865527,-3.544960,-5.759307,0.617134,-6.937504,-6.264354,-7.346782,-1.327090,9.587381,7.469872,-5.108276,-6.106481,-7.540505,-0.550360,5.242447,2.395895,0.432976,0.067542,-1.596610,-9.910626,-8.657323,-4.469083,-2.990972,3.815495,0.240629,-0.899362,8.569698,4.430449,6.737737,-8.552210,9.927311,5.599825,7.111295,-3.814943,-8.239634,-2.525022,1.721571,9.832706,4.449123,7.848727,4.002278,5.755111,-3.442069,-7.402815,-3.143444,-0.901232,-7.732509,-0.401009,3.273467,3.113457,2.610431,-2.152681,-8.902678,-5.987960,1.323753,-4.146193,4.258365,7.097214,-3.328517,7.120649,-1.809687,-4.792638,-6.959106,-3.290405,8.031755,1.017820,-8.497256,4.199166,2.274947,-2.356598,9.707111,5.631187,-4.825662,-8.636750,-6.105292,-6.266976,-8.290330,-6.910935,5.056311,-0.591493,-7.285504,-8.369152,2.131320,-0.742623,8.401442,5.453044,1.818333,-1.858502,-7.263326,2.523484,-7.001692,6.605146,-3.838781,8.898878,1.400089,6.182669,8.737663,-7.022588,5.204716,5.005885,4.500679,-9.196355,7.996747,7.109562,8.779585,6.163021,-8.268154,-1.082470,-8.579201,-2.501777,2.096969,6.126653,1.146625,-1.273065,-4.747446,-1.805484,-2.842242,0.362606,6.348907,3.796183,3.344728,-4.483841,-0.445977,-4.098577,4.160610,-4.459523,-9.028340,8.257259,8.362712,3.035299,-4.058049,5.091845,-2.591877,-0.105573,1.264522,-4.426440,-0.206421,-2.163679,-0.458918,8.630205,-9.455077,-0.968278,-2.087733,-2.528113,7.056319,2.977174,5.664811,7.871676,2.798420,3.446267,7.048477,8.268424,4.547353,-8.194557,7.518080,1.181524,5.542817,-1.400285,5.938327,2.154930,-9.438529,-5.819691,-6.758243,9.239873,-1.358580,-3.430725,4.884494,8.071160,-9.139144,-1.674657,-3.159306,2.617059,1.843350,2.086966,-6.139939,-8.289098,7.212324,1.419647,-9.409573,-1.034943,1.989596,-5.900770,-9.386159,8.790895,-7.800266,-9.237817,4.113939,-7.927761,-4.798333,-9.904708,3.843288,3.415707,9.533167,-8.721048,-8.697400,-6.340224,5.712694,-1.977185,8.311951,-5.480128,4.443056,-3.762998,-1.005406,2.954788,-1.461025,-9.521918,-0.878577,-9.607912,-2.893191,6.653627,4.634003,-9.982011,2.152615,2.344706,4.017101,-8.699183,-8.800559,6.511399,8.827546,3.518986,-6.866935,3.425170,-3.605030,7.552460,-6.222602,5.550581,-5.468286,6.133555,-6.766633,-3.558427,-7.563597,-1.131224,7.989156,-7.847840,-6.834544,-2.059301,0.330681,-1.640270,-6.626826,-6.970157,-0.167498,-3.535968,8.809306,-1.280517,-2.640637,6.869848,0.176883,-6.040483,-2.865436,-7.541273,-2.557362,9.066891,-8.886812,6.101171,6.173999,-8.051313,8.716409,2.455092,-4.510459,-0.612100,-4.494560,0.875830,2.396804,4.560117,-0.343241,3.421601,-9.586541,-4.836572,-6.212932,9.059867,6.381250,3.396406,0.774300,-7.674055,5.942783,-9.864584], dtype = "float64")#candidate|1783|(364,)|const|float64
call_1781 = relay.TupleGetItem(func_985_call(relay.reshape(const_1782.astype('uint64'), [4, 6, 5]), relay.reshape(const_1783.astype('float64'), [364,]), ), 0)
call_1784 = relay.TupleGetItem(func_989_call(relay.reshape(const_1782.astype('uint64'), [4, 6, 5]), relay.reshape(const_1783.astype('float64'), [364,]), ), 0)
func_242_call = mod.get_global_var('func_242')
func_244_call = mutated_mod.get_global_var('func_244')
call_1798 = relay.TupleGetItem(func_242_call(), 1)
call_1799 = relay.TupleGetItem(func_244_call(), 1)
func_242_call = mod.get_global_var('func_242')
func_244_call = mutated_mod.get_global_var('func_244')
call_1800 = relay.TupleGetItem(func_242_call(), 0)
call_1801 = relay.TupleGetItem(func_244_call(), 0)
func_184_call = mod.get_global_var('func_184')
func_186_call = mutated_mod.get_global_var('func_186')
call_1802 = func_184_call(relay.reshape(call_1798.astype('float64'), [14, 13, 2]))
call_1803 = func_184_call(relay.reshape(call_1798.astype('float64'), [14, 13, 2]))
func_1071_call = mod.get_global_var('func_1071')
func_1075_call = mutated_mod.get_global_var('func_1075')
var_1808 = relay.var("var_1808", dtype = "float64", shape = (5460,))#candidate|1808|(5460,)|var|float64
call_1807 = relay.TupleGetItem(func_1071_call(relay.reshape(const_1783.astype('float64'), [14, 13, 2]), relay.reshape(var_1808.astype('float64'), [15, 364]), ), 0)
call_1809 = relay.TupleGetItem(func_1075_call(relay.reshape(const_1783.astype('float64'), [14, 13, 2]), relay.reshape(var_1808.astype('float64'), [15, 364]), ), 0)
var_1840 = relay.var("var_1840", dtype = "uint64", shape = (120,))#candidate|1840|(120,)|var|uint64
bop_1841 = relay.add(const_1782.astype('uint32'), relay.reshape(var_1840.astype('uint32'), relay.shape_of(const_1782))) # shape=(120,)
output = relay.Tuple([uop_1775,call_1781,const_1783,call_1798,call_1800,call_1802,call_1807,var_1808,bop_1841,])
output2 = relay.Tuple([uop_1775,call_1784,const_1783,call_1799,call_1801,call_1803,call_1809,var_1808,bop_1841,])
func_1852 = relay.Function([var_1808,var_1840,], output)
mod['func_1852'] = func_1852
mod = relay.transform.InferType()(mod)
mutated_mod['func_1852'] = func_1852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1852_call = mutated_mod.get_global_var('func_1852')
var_1854 = relay.var("var_1854", dtype = "float64", shape = (5460,))#candidate|1854|(5460,)|var|float64
var_1855 = relay.var("var_1855", dtype = "uint64", shape = (120,))#candidate|1855|(120,)|var|uint64
call_1853 = func_1852_call(var_1854,var_1855,)
output = call_1853
func_1856 = relay.Function([var_1854,var_1855,], output)
mutated_mod['func_1856'] = func_1856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_654_call = mod.get_global_var('func_654')
func_656_call = mutated_mod.get_global_var('func_656')
call_1895 = relay.TupleGetItem(func_654_call(), 0)
call_1896 = relay.TupleGetItem(func_656_call(), 0)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_1900 = func_135_call()
call_1901 = func_135_call()
output = relay.Tuple([call_1895,call_1900,])
output2 = relay.Tuple([call_1896,call_1901,])
func_1944 = relay.Function([], output)
mod['func_1944'] = func_1944
mod = relay.transform.InferType()(mod)
mutated_mod['func_1944'] = func_1944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1944_call = mutated_mod.get_global_var('func_1944')
call_1945 = func_1944_call()
output = call_1945
func_1946 = relay.Function([], output)
mutated_mod['func_1946'] = func_1946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_654_call = mod.get_global_var('func_654')
func_656_call = mutated_mod.get_global_var('func_656')
call_2004 = relay.TupleGetItem(func_654_call(), 0)
call_2005 = relay.TupleGetItem(func_656_call(), 0)
output = relay.Tuple([call_2004,])
output2 = relay.Tuple([call_2005,])
func_2011 = relay.Function([], output)
mod['func_2011'] = func_2011
mod = relay.transform.InferType()(mod)
output = func_2011()
func_2012 = relay.Function([], output)
mutated_mod['func_2012'] = func_2012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1038_call = mod.get_global_var('func_1038')
func_1039_call = mutated_mod.get_global_var('func_1039')
call_2039 = relay.TupleGetItem(func_1038_call(), 0)
call_2040 = relay.TupleGetItem(func_1039_call(), 0)
var_2041 = relay.var("var_2041", dtype = "float64", shape = (364,))#candidate|2041|(364,)|var|float64
bop_2042 = relay.not_equal(call_2039.astype('bool'), relay.reshape(var_2041.astype('bool'), relay.shape_of(call_2039))) # shape=(364,)
bop_2045 = relay.not_equal(call_2040.astype('bool'), relay.reshape(var_2041.astype('bool'), relay.shape_of(call_2040))) # shape=(364,)
bop_2048 = relay.greater(call_2039.astype('bool'), relay.reshape(bop_2042.astype('bool'), relay.shape_of(call_2039))) # shape=(364,)
bop_2051 = relay.greater(call_2040.astype('bool'), relay.reshape(bop_2045.astype('bool'), relay.shape_of(call_2040))) # shape=(364,)
func_1528_call = mod.get_global_var('func_1528')
func_1531_call = mutated_mod.get_global_var('func_1531')
var_2062 = relay.var("var_2062", dtype = "float64", shape = (1092,))#candidate|2062|(1092,)|var|float64
call_2061 = relay.TupleGetItem(func_1528_call(relay.reshape(var_2062.astype('float64'), [3, 364])), 2)
call_2063 = relay.TupleGetItem(func_1531_call(relay.reshape(var_2062.astype('float64'), [3, 364])), 2)
output = relay.Tuple([bop_2048,call_2061,var_2062,])
output2 = relay.Tuple([bop_2051,call_2063,var_2062,])
func_2065 = relay.Function([var_2041,var_2062,], output)
mod['func_2065'] = func_2065
mod = relay.transform.InferType()(mod)
mutated_mod['func_2065'] = func_2065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2065_call = mutated_mod.get_global_var('func_2065')
var_2067 = relay.var("var_2067", dtype = "float64", shape = (364,))#candidate|2067|(364,)|var|float64
var_2068 = relay.var("var_2068", dtype = "float64", shape = (1092,))#candidate|2068|(1092,)|var|float64
call_2066 = func_2065_call(var_2067,var_2068,)
output = call_2066
func_2069 = relay.Function([var_2067,var_2068,], output)
mutated_mod['func_2069'] = func_2069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_2075 = relay.TupleGetItem(func_577_call(), 1)
call_2076 = relay.TupleGetItem(func_579_call(), 1)
output = relay.Tuple([call_2075,])
output2 = relay.Tuple([call_2076,])
func_2086 = relay.Function([], output)
mod['func_2086'] = func_2086
mod = relay.transform.InferType()(mod)
mutated_mod['func_2086'] = func_2086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2086_call = mutated_mod.get_global_var('func_2086')
call_2087 = func_2086_call()
output = call_2087
func_2088 = relay.Function([], output)
mutated_mod['func_2088'] = func_2088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_654_call = mod.get_global_var('func_654')
func_656_call = mutated_mod.get_global_var('func_656')
call_2111 = relay.TupleGetItem(func_654_call(), 0)
call_2112 = relay.TupleGetItem(func_656_call(), 0)
func_1944_call = mod.get_global_var('func_1944')
func_1946_call = mutated_mod.get_global_var('func_1946')
call_2131 = relay.TupleGetItem(func_1944_call(), 1)
call_2132 = relay.TupleGetItem(func_1946_call(), 1)
output = relay.Tuple([call_2111,call_2131,])
output2 = relay.Tuple([call_2112,call_2132,])
func_2137 = relay.Function([], output)
mod['func_2137'] = func_2137
mod = relay.transform.InferType()(mod)
output = func_2137()
func_2138 = relay.Function([], output)
mutated_mod['func_2138'] = func_2138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1944_call = mod.get_global_var('func_1944')
func_1946_call = mutated_mod.get_global_var('func_1946')
call_2139 = relay.TupleGetItem(func_1944_call(), 0)
call_2140 = relay.TupleGetItem(func_1946_call(), 0)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_2147 = relay.TupleGetItem(func_577_call(), 0)
call_2148 = relay.TupleGetItem(func_579_call(), 0)
func_1297_call = mod.get_global_var('func_1297')
func_1301_call = mutated_mod.get_global_var('func_1301')
var_2161 = relay.var("var_2161", dtype = "float64", shape = (180,))#candidate|2161|(180,)|var|float64
var_2162 = relay.var("var_2162", dtype = "int64", shape = (560,))#candidate|2162|(560,)|var|int64
call_2160 = relay.TupleGetItem(func_1297_call(relay.reshape(var_2161.astype('float64'), [6, 5, 6]), relay.reshape(var_2162.astype('int64'), [8, 70]), ), 0)
call_2163 = relay.TupleGetItem(func_1301_call(relay.reshape(var_2161.astype('float64'), [6, 5, 6]), relay.reshape(var_2162.astype('int64'), [8, 70]), ), 0)
output = relay.Tuple([call_2139,call_2147,call_2160,var_2161,var_2162,])
output2 = relay.Tuple([call_2140,call_2148,call_2163,var_2161,var_2162,])
func_2167 = relay.Function([var_2161,var_2162,], output)
mod['func_2167'] = func_2167
mod = relay.transform.InferType()(mod)
var_2168 = relay.var("var_2168", dtype = "float64", shape = (180,))#candidate|2168|(180,)|var|float64
var_2169 = relay.var("var_2169", dtype = "int64", shape = (560,))#candidate|2169|(560,)|var|int64
output = func_2167(var_2168,var_2169,)
func_2170 = relay.Function([var_2168,var_2169,], output)
mutated_mod['func_2170'] = func_2170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_2273 = relay.TupleGetItem(func_1448_call(), 0)
call_2274 = relay.TupleGetItem(func_1449_call(), 0)
uop_2288 = relay.cos(call_2273.astype('float64')) # shape=(4, 6, 5)
uop_2290 = relay.cos(call_2274.astype('float64')) # shape=(4, 6, 5)
func_1130_call = mod.get_global_var('func_1130')
func_1133_call = mutated_mod.get_global_var('func_1133')
var_2296 = relay.var("var_2296", dtype = "float64", shape = (364,))#candidate|2296|(364,)|var|float64
call_2295 = relay.TupleGetItem(func_1130_call(relay.reshape(var_2296.astype('float64'), [14, 13, 2]), relay.reshape(call_2273.astype('uint64'), [120,]), ), 0)
call_2297 = relay.TupleGetItem(func_1133_call(relay.reshape(var_2296.astype('float64'), [14, 13, 2]), relay.reshape(call_2273.astype('uint64'), [120,]), ), 0)
output = relay.Tuple([uop_2288,call_2295,var_2296,])
output2 = relay.Tuple([uop_2290,call_2297,var_2296,])
func_2309 = relay.Function([var_2296,], output)
mod['func_2309'] = func_2309
mod = relay.transform.InferType()(mod)
mutated_mod['func_2309'] = func_2309
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2310 = relay.var("var_2310", dtype = "float64", shape = (364,))#candidate|2310|(364,)|var|float64
func_2309_call = mutated_mod.get_global_var('func_2309')
call_2311 = func_2309_call(var_2310)
output = call_2311
func_2312 = relay.Function([var_2310], output)
mutated_mod['func_2312'] = func_2312
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2314 = relay.var("var_2314", dtype = "int16", shape = (5, 5, 15))#candidate|2314|(5, 5, 15)|var|int16
var_2315 = relay.var("var_2315", dtype = "int16", shape = (5, 5, 15))#candidate|2315|(5, 5, 15)|var|int16
bop_2316 = relay.bitwise_xor(var_2314.astype('int16'), relay.reshape(var_2315.astype('int16'), relay.shape_of(var_2314))) # shape=(5, 5, 15)
func_1317_call = mod.get_global_var('func_1317')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_2321 = relay.TupleGetItem(func_1317_call(), 0)
call_2322 = relay.TupleGetItem(func_1319_call(), 0)
output = relay.Tuple([bop_2316,call_2321,])
output2 = relay.Tuple([bop_2316,call_2322,])
func_2323 = relay.Function([var_2314,var_2315,], output)
mod['func_2323'] = func_2323
mod = relay.transform.InferType()(mod)
mutated_mod['func_2323'] = func_2323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2323_call = mutated_mod.get_global_var('func_2323')
var_2325 = relay.var("var_2325", dtype = "int16", shape = (5, 5, 15))#candidate|2325|(5, 5, 15)|var|int16
var_2326 = relay.var("var_2326", dtype = "int16", shape = (5, 5, 15))#candidate|2326|(5, 5, 15)|var|int16
call_2324 = func_2323_call(var_2325,var_2326,)
output = call_2324
func_2327 = relay.Function([var_2325,var_2326,], output)
mutated_mod['func_2327'] = func_2327
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2350 = relay.var("var_2350", dtype = "float32", shape = (16, 6, 1))#candidate|2350|(16, 6, 1)|var|float32
uop_2351 = relay.atanh(var_2350.astype('float32')) # shape=(16, 6, 1)
output = relay.Tuple([uop_2351,])
output2 = relay.Tuple([uop_2351,])
func_2361 = relay.Function([var_2350,], output)
mod['func_2361'] = func_2361
mod = relay.transform.InferType()(mod)
mutated_mod['func_2361'] = func_2361
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2362 = relay.var("var_2362", dtype = "float32", shape = (16, 6, 1))#candidate|2362|(16, 6, 1)|var|float32
func_2361_call = mutated_mod.get_global_var('func_2361')
call_2363 = func_2361_call(var_2362)
output = call_2363
func_2364 = relay.Function([var_2362], output)
mutated_mod['func_2364'] = func_2364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1250_call = mod.get_global_var('func_1250')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_2404 = relay.TupleGetItem(func_1250_call(), 0)
call_2405 = relay.TupleGetItem(func_1252_call(), 0)
func_2011_call = mod.get_global_var('func_2011')
func_2012_call = mutated_mod.get_global_var('func_2012')
call_2419 = relay.TupleGetItem(func_2011_call(), 0)
call_2420 = relay.TupleGetItem(func_2012_call(), 0)
output = relay.Tuple([call_2404,call_2419,])
output2 = relay.Tuple([call_2405,call_2420,])
func_2444 = relay.Function([], output)
mod['func_2444'] = func_2444
mod = relay.transform.InferType()(mod)
mutated_mod['func_2444'] = func_2444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2444_call = mutated_mod.get_global_var('func_2444')
call_2445 = func_2444_call()
output = call_2445
func_2446 = relay.Function([], output)
mutated_mod['func_2446'] = func_2446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_472_call = mod.get_global_var('func_472')
func_474_call = mutated_mod.get_global_var('func_474')
call_2508 = relay.TupleGetItem(func_472_call(), 3)
call_2509 = relay.TupleGetItem(func_474_call(), 3)
var_2515 = relay.var("var_2515", dtype = "uint64", shape = (4, 6, 5))#candidate|2515|(4, 6, 5)|var|uint64
bop_2516 = relay.not_equal(call_2508.astype('bool'), relay.reshape(var_2515.astype('bool'), relay.shape_of(call_2508))) # shape=(4, 6, 5)
bop_2519 = relay.not_equal(call_2509.astype('bool'), relay.reshape(var_2515.astype('bool'), relay.shape_of(call_2509))) # shape=(4, 6, 5)
func_2444_call = mod.get_global_var('func_2444')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_2538 = relay.TupleGetItem(func_2444_call(), 0)
call_2539 = relay.TupleGetItem(func_2446_call(), 0)
output = relay.Tuple([bop_2516,call_2538,])
output2 = relay.Tuple([bop_2519,call_2539,])
func_2550 = relay.Function([var_2515,], output)
mod['func_2550'] = func_2550
mod = relay.transform.InferType()(mod)
var_2551 = relay.var("var_2551", dtype = "uint64", shape = (4, 6, 5))#candidate|2551|(4, 6, 5)|var|uint64
output = func_2550(var_2551)
func_2552 = relay.Function([var_2551], output)
mutated_mod['func_2552'] = func_2552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2086_call = mod.get_global_var('func_2086')
func_2088_call = mutated_mod.get_global_var('func_2088')
call_2554 = relay.TupleGetItem(func_2086_call(), 0)
call_2555 = relay.TupleGetItem(func_2088_call(), 0)
func_707_call = mod.get_global_var('func_707')
func_708_call = mutated_mod.get_global_var('func_708')
call_2556 = relay.TupleGetItem(func_707_call(), 0)
call_2557 = relay.TupleGetItem(func_708_call(), 0)
output = relay.Tuple([call_2554,call_2556,])
output2 = relay.Tuple([call_2555,call_2557,])
func_2559 = relay.Function([], output)
mod['func_2559'] = func_2559
mod = relay.transform.InferType()(mod)
output = func_2559()
func_2560 = relay.Function([], output)
mutated_mod['func_2560'] = func_2560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
call_2591 = relay.TupleGetItem(func_674_call(), 0)
call_2592 = relay.TupleGetItem(func_676_call(), 0)
var_2595 = relay.var("var_2595", dtype = "uint64", shape = (4, 6, 5))#candidate|2595|(4, 6, 5)|var|uint64
bop_2596 = relay.logical_or(call_2591.astype('bool'), relay.reshape(var_2595.astype('bool'), relay.shape_of(call_2591))) # shape=(4, 6, 5)
bop_2599 = relay.logical_or(call_2592.astype('bool'), relay.reshape(var_2595.astype('bool'), relay.shape_of(call_2592))) # shape=(4, 6, 5)
const_2606 = relay.const([[[True,True,False,True,False],[False,False,True,False,True],[True,False,True,False,False],[True,False,False,False,False],[True,True,True,False,True],[True,False,True,True,True]],[[False,False,True,False,False],[True,False,False,True,True],[True,False,True,False,False],[True,False,True,True,False],[True,False,True,False,False],[False,True,True,False,False]],[[False,False,True,True,False],[True,True,False,True,False],[True,False,False,False,True],[False,True,True,True,False],[True,True,True,False,True],[True,False,True,False,False]],[[True,True,False,False,False],[False,True,True,True,False],[True,False,True,True,True],[False,False,False,True,True],[True,False,False,False,False],[False,True,False,True,False]]], dtype = "bool")#candidate|2606|(4, 6, 5)|const|bool
bop_2607 = relay.minimum(bop_2596.astype('int16'), relay.reshape(const_2606.astype('int16'), relay.shape_of(bop_2596))) # shape=(4, 6, 5)
bop_2610 = relay.minimum(bop_2599.astype('int16'), relay.reshape(const_2606.astype('int16'), relay.shape_of(bop_2599))) # shape=(4, 6, 5)
output = relay.Tuple([bop_2607,])
output2 = relay.Tuple([bop_2610,])
func_2611 = relay.Function([var_2595,], output)
mod['func_2611'] = func_2611
mod = relay.transform.InferType()(mod)
var_2612 = relay.var("var_2612", dtype = "uint64", shape = (4, 6, 5))#candidate|2612|(4, 6, 5)|var|uint64
output = func_2611(var_2612)
func_2613 = relay.Function([var_2612], output)
mutated_mod['func_2613'] = func_2613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_2619 = relay.TupleGetItem(func_764_call(), 2)
call_2620 = relay.TupleGetItem(func_766_call(), 2)
output = call_2619
output2 = call_2620
func_2626 = relay.Function([], output)
mod['func_2626'] = func_2626
mod = relay.transform.InferType()(mod)
output = func_2626()
func_2627 = relay.Function([], output)
mutated_mod['func_2627'] = func_2627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_613_call = mod.get_global_var('func_613')
func_615_call = mutated_mod.get_global_var('func_615')
call_2640 = func_613_call()
call_2641 = func_613_call()
output = call_2640
output2 = call_2641
func_2652 = relay.Function([], output)
mod['func_2652'] = func_2652
mod = relay.transform.InferType()(mod)
mutated_mod['func_2652'] = func_2652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2652_call = mutated_mod.get_global_var('func_2652')
call_2653 = func_2652_call()
output = call_2653
func_2654 = relay.Function([], output)
mutated_mod['func_2654'] = func_2654
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2666 = relay.var("var_2666", dtype = "int8", shape = ())#candidate|2666|()|var|int8
var_2667 = relay.var("var_2667", dtype = "int8", shape = (10, 14, 8))#candidate|2667|(10, 14, 8)|var|int8
bop_2668 = relay.bitwise_or(var_2666.astype('int8'), var_2667.astype('int8')) # shape=(10, 14, 8)
output = relay.Tuple([bop_2668,])
output2 = relay.Tuple([bop_2668,])
func_2677 = relay.Function([var_2666,var_2667,], output)
mod['func_2677'] = func_2677
mod = relay.transform.InferType()(mod)
mutated_mod['func_2677'] = func_2677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2677_call = mutated_mod.get_global_var('func_2677')
var_2679 = relay.var("var_2679", dtype = "int8", shape = ())#candidate|2679|()|var|int8
var_2680 = relay.var("var_2680", dtype = "int8", shape = (10, 14, 8))#candidate|2680|(10, 14, 8)|var|int8
call_2678 = func_2677_call(var_2679,var_2680,)
output = call_2678
func_2681 = relay.Function([var_2679,var_2680,], output)
mutated_mod['func_2681'] = func_2681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1334_call = mod.get_global_var('func_1334')
func_1336_call = mutated_mod.get_global_var('func_1336')
call_2696 = relay.TupleGetItem(func_1334_call(), 0)
call_2697 = relay.TupleGetItem(func_1336_call(), 0)
output = call_2696
output2 = call_2697
func_2706 = relay.Function([], output)
mod['func_2706'] = func_2706
mod = relay.transform.InferType()(mod)
mutated_mod['func_2706'] = func_2706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2706_call = mutated_mod.get_global_var('func_2706')
call_2707 = func_2706_call()
output = call_2707
func_2708 = relay.Function([], output)
mutated_mod['func_2708'] = func_2708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2711 = relay.var("var_2711", dtype = "float64", shape = (1, 4, 16))#candidate|2711|(1, 4, 16)|var|float64
var_2712 = relay.var("var_2712", dtype = "float64", shape = (5, 4, 16))#candidate|2712|(5, 4, 16)|var|float64
bop_2713 = relay.divide(var_2711.astype('float64'), var_2712.astype('float64')) # shape=(5, 4, 16)
uop_2720 = relay.erf(var_2712.astype('float64')) # shape=(5, 4, 16)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
call_2734 = relay.TupleGetItem(func_674_call(), 0)
call_2735 = relay.TupleGetItem(func_676_call(), 0)
uop_2741 = relay.exp(uop_2720.astype('float64')) # shape=(5, 4, 16)
uop_2747 = relay.atanh(uop_2741.astype('float32')) # shape=(5, 4, 16)
var_2749 = relay.var("var_2749", dtype = "float32", shape = (5, 4, 16))#candidate|2749|(5, 4, 16)|var|float32
bop_2750 = relay.multiply(uop_2747.astype('uint8'), relay.reshape(var_2749.astype('uint8'), relay.shape_of(uop_2747))) # shape=(5, 4, 16)
bop_2755 = relay.minimum(uop_2741.astype('int64'), relay.reshape(bop_2713.astype('int64'), relay.shape_of(uop_2741))) # shape=(5, 4, 16)
output = relay.Tuple([call_2734,bop_2750,bop_2755,])
output2 = relay.Tuple([call_2735,bop_2750,bop_2755,])
func_2763 = relay.Function([var_2711,var_2712,var_2749,], output)
mod['func_2763'] = func_2763
mod = relay.transform.InferType()(mod)
var_2764 = relay.var("var_2764", dtype = "float64", shape = (1, 4, 16))#candidate|2764|(1, 4, 16)|var|float64
var_2765 = relay.var("var_2765", dtype = "float64", shape = (5, 4, 16))#candidate|2765|(5, 4, 16)|var|float64
var_2766 = relay.var("var_2766", dtype = "float32", shape = (5, 4, 16))#candidate|2766|(5, 4, 16)|var|float32
output = func_2763(var_2764,var_2765,var_2766,)
func_2767 = relay.Function([var_2764,var_2765,var_2766,], output)
mutated_mod['func_2767'] = func_2767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2652_call = mod.get_global_var('func_2652')
func_2654_call = mutated_mod.get_global_var('func_2654')
call_2848 = func_2652_call()
call_2849 = func_2652_call()
output = relay.Tuple([call_2848,])
output2 = relay.Tuple([call_2849,])
func_2858 = relay.Function([], output)
mod['func_2858'] = func_2858
mod = relay.transform.InferType()(mod)
output = func_2858()
func_2859 = relay.Function([], output)
mutated_mod['func_2859'] = func_2859
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2869 = relay.const([[[8.032549,-1.582449,-9.716322,7.701875,0.135072,-2.452741,4.919050,9.620618,2.104279,-7.004953,0.157235,4.091962,4.359145,9.437084,7.078321],[-1.307733,4.518277,3.939439,-0.692693,-5.616754,2.373447,-3.324296,2.228083,-1.870790,1.455628,3.040186,2.899667,-1.006144,-1.034129,2.463025]],[[2.298668,5.792844,6.968078,-4.851094,4.704008,3.503682,5.237293,-1.006670,0.055763,2.091760,1.038917,-9.965946,-1.644328,2.781032,-0.202439],[-7.423157,5.403881,-7.564671,-6.147003,-7.054033,-9.343556,-1.496605,0.910633,-1.770655,-5.000673,-1.046462,0.214481,-9.271218,2.685250,-7.693523]],[[2.729465,6.730555,-1.109439,9.349994,2.284288,0.573435,0.955933,0.746022,-5.775986,-4.401726,-2.107059,-2.815824,4.034641,6.854646,4.548087],[-5.771763,-6.180697,4.149131,-3.897213,0.203228,-4.790971,1.681048,-1.993974,-9.935736,-4.315536,5.253773,0.681848,-4.418386,7.971171,-9.009733]],[[-5.794041,2.865914,-4.013200,0.488772,3.424205,-8.510208,9.103145,5.107040,6.221718,-0.575559,-1.248992,-5.867103,-7.019698,-4.312321,-1.976435],[-4.076912,-3.778978,2.717143,-6.347285,8.694015,5.854682,7.420648,1.864754,-0.368290,-5.206713,-4.269494,8.680613,1.684331,-5.676649,7.961396]],[[-9.647199,9.526529,9.178797,1.469562,0.698296,2.190775,2.087662,-1.733090,9.993879,6.657027,7.140394,7.472096,-4.011229,-1.342287,-1.482841],[0.903169,8.603540,9.088836,2.977418,-1.233461,5.356564,7.425851,-1.867066,8.658486,-8.117115,-6.287726,8.150061,-1.762932,-8.700003,-7.085265]],[[-8.245116,3.225283,-0.598513,-0.226481,1.718575,-4.792250,-5.211360,4.301006,1.638758,5.561916,4.286963,-3.362009,2.129196,-9.734461,9.498263],[-8.753207,-0.289854,-7.095823,2.395141,-2.128552,0.959543,1.260157,-0.521142,5.407443,-0.057050,-4.280241,-4.260429,-3.593098,1.783321,8.062828]],[[5.415640,7.033816,2.561319,-3.500643,-6.278119,3.452070,2.863900,-0.503241,-1.311169,-7.196950,-8.943578,-4.802386,8.160759,-4.671999,-3.566441],[8.551880,7.962772,8.045141,-4.300135,8.807719,2.515647,9.128588,-8.769843,-7.913012,8.361319,9.731991,0.556208,-2.802225,-5.603478,-0.788197]],[[-1.028575,-9.985826,-4.802310,-6.132093,4.225122,3.671986,-9.547953,7.242331,-6.642377,0.386267,-2.155531,1.065989,1.668072,-8.427022,-2.765193],[-4.654509,3.877769,1.065828,-1.282923,-5.940625,9.458097,-3.782369,-9.701585,-3.473303,-6.973843,-1.920220,-4.998528,-0.402465,5.486050,4.311026]],[[8.806053,-0.383889,-2.638076,-9.104953,8.807135,-7.424305,4.633342,6.953044,4.552680,-4.057407,6.070461,-5.236458,3.603015,4.356691,-0.095998],[-3.297700,-3.839711,-6.314558,-9.645395,-9.085630,0.360468,2.495383,9.227471,3.732402,-1.493157,-9.818115,-7.724092,-8.364462,-0.616505,1.554942]],[[-6.277550,-8.347203,-3.396907,-5.042039,-6.445980,4.082438,5.766063,-6.018305,4.486197,5.626580,0.986075,8.092477,4.256668,4.028434,-5.339482],[-8.261103,9.046025,1.416849,3.579541,-0.725059,-0.783557,0.995942,-7.243038,2.594168,2.078939,-4.019098,-7.714527,9.207716,6.055184,5.564118]]], dtype = "float64")#candidate|2869|(10, 2, 15)|const|float64
uop_2870 = relay.log10(const_2869.astype('float64')) # shape=(10, 2, 15)
func_2309_call = mod.get_global_var('func_2309')
func_2312_call = mutated_mod.get_global_var('func_2312')
var_2901 = relay.var("var_2901", dtype = "float64", shape = (364,))#candidate|2901|(364,)|var|float64
call_2900 = relay.TupleGetItem(func_2309_call(relay.reshape(var_2901.astype('float64'), [364,])), 2)
call_2902 = relay.TupleGetItem(func_2312_call(relay.reshape(var_2901.astype('float64'), [364,])), 2)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_2903 = func_2626_call()
call_2904 = func_2626_call()
output = relay.Tuple([uop_2870,call_2900,var_2901,call_2903,])
output2 = relay.Tuple([uop_2870,call_2902,var_2901,call_2904,])
func_2911 = relay.Function([var_2901,], output)
mod['func_2911'] = func_2911
mod = relay.transform.InferType()(mod)
mutated_mod['func_2911'] = func_2911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2912 = relay.var("var_2912", dtype = "float64", shape = (364,))#candidate|2912|(364,)|var|float64
func_2911_call = mutated_mod.get_global_var('func_2911')
call_2913 = func_2911_call(var_2912)
output = call_2913
func_2914 = relay.Function([var_2912], output)
mutated_mod['func_2914'] = func_2914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2559_call = mod.get_global_var('func_2559')
func_2560_call = mutated_mod.get_global_var('func_2560')
call_2958 = relay.TupleGetItem(func_2559_call(), 1)
call_2959 = relay.TupleGetItem(func_2560_call(), 1)
func_707_call = mod.get_global_var('func_707')
func_708_call = mutated_mod.get_global_var('func_708')
call_2960 = relay.TupleGetItem(func_707_call(), 0)
call_2961 = relay.TupleGetItem(func_708_call(), 0)
func_855_call = mod.get_global_var('func_855')
func_857_call = mutated_mod.get_global_var('func_857')
call_2978 = func_855_call()
call_2979 = func_855_call()
output = relay.Tuple([call_2958,call_2960,call_2978,])
output2 = relay.Tuple([call_2959,call_2961,call_2979,])
func_2980 = relay.Function([], output)
mod['func_2980'] = func_2980
mod = relay.transform.InferType()(mod)
mutated_mod['func_2980'] = func_2980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mutated_mod.get_global_var('func_2980')
call_2981 = func_2980_call()
output = call_2981
func_2982 = relay.Function([], output)
mutated_mod['func_2982'] = func_2982
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3027 = relay.var("var_3027", dtype = "float64", shape = (2, 1, 15))#candidate|3027|(2, 1, 15)|var|float64
var_3028 = relay.var("var_3028", dtype = "float64", shape = (2, 14, 15))#candidate|3028|(2, 14, 15)|var|float64
bop_3029 = relay.mod(var_3027.astype('float64'), var_3028.astype('float64')) # shape=(2, 14, 15)
bop_3033 = relay.logical_and(var_3028.astype('bool'), var_3027.astype('bool')) # shape=(2, 14, 15)
uop_3042 = relay.tan(var_3028.astype('float64')) # shape=(2, 14, 15)
bop_3048 = relay.less(uop_3042.astype('bool'), relay.reshape(bop_3033.astype('bool'), relay.shape_of(uop_3042))) # shape=(2, 14, 15)
output = relay.Tuple([bop_3029,bop_3048,])
output2 = relay.Tuple([bop_3029,bop_3048,])
func_3054 = relay.Function([var_3027,var_3028,], output)
mod['func_3054'] = func_3054
mod = relay.transform.InferType()(mod)
var_3055 = relay.var("var_3055", dtype = "float64", shape = (2, 1, 15))#candidate|3055|(2, 1, 15)|var|float64
var_3056 = relay.var("var_3056", dtype = "float64", shape = (2, 14, 15))#candidate|3056|(2, 14, 15)|var|float64
output = func_3054(var_3055,var_3056,)
func_3057 = relay.Function([var_3055,var_3056,], output)
mutated_mod['func_3057'] = func_3057
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3068 = relay.var("var_3068", dtype = "int64", shape = (11, 16, 16))#candidate|3068|(11, 16, 16)|var|int64
const_3069 = relay.const([[[-1,-6,-8,1,5,1,-3,6,-9,1,-9,-8,-10,4,-9,8],[1,-7,2,-1,1,10,4,-6,-9,6,5,-6,10,-9,-8,-1],[10,-8,-7,1,10,2,7,8,4,3,-9,6,-10,8,-9,5],[-8,-2,-1,-3,-4,6,4,7,-7,9,1,5,8,9,4,-7],[-8,-7,3,3,-4,9,2,-8,-10,5,2,-5,3,10,-10,10],[-9,1,7,-7,3,-1,-4,4,-5,7,8,8,6,9,-6,-5],[5,6,10,-3,1,-5,-2,-9,9,4,8,9,1,-9,8,-3],[2,3,3,4,-9,-7,10,-7,3,-8,-3,-4,-6,3,-1,-7],[6,-4,5,10,-8,4,-6,1,-2,10,-8,4,-9,10,-5,-2],[4,-7,5,10,6,-5,6,-10,5,-6,6,6,8,5,10,2],[5,-2,7,-6,-7,5,-7,4,7,-4,1,-8,6,10,-1,10],[4,-6,6,-5,-3,8,5,3,-3,5,-6,3,-6,-8,7,-1],[-1,-3,-9,4,9,3,4,-6,-2,1,3,8,6,4,-5,6],[2,-5,-8,-4,-10,8,4,1,4,1,-3,-7,-6,-4,-8,7],[10,2,10,2,4,2,-6,3,4,-1,7,-7,1,-4,-2,2],[4,9,-3,-3,-2,6,-9,-2,-4,-9,-1,6,8,4,4,1]],[[1,1,10,10,9,4,4,1,8,-1,-4,4,8,1,5,9],[9,-7,-3,3,-2,2,-4,6,-10,-5,-5,-8,9,4,-3,-8],[-2,-3,2,9,-4,2,3,-2,-4,-1,5,1,-1,6,7,-6],[8,5,7,8,6,-1,-7,-6,-9,-9,6,-8,6,-3,-9,1],[10,9,-2,1,6,-1,-5,5,1,10,-5,-6,-4,3,10,1],[2,9,9,-3,4,-10,-10,4,-1,1,-5,-7,8,10,-4,9],[-3,9,2,8,8,6,-5,9,7,1,7,-8,-10,4,-9,9],[5,3,1,-3,1,9,10,-3,-8,-6,4,3,-2,7,1,-5],[-5,-4,-2,-7,8,9,6,6,8,-10,-8,8,9,3,-1,-8],[7,-3,3,-1,8,1,-4,9,-1,-6,-3,10,10,-3,4,-7],[7,9,2,1,2,5,10,-1,4,-9,2,10,-5,-2,8,9],[9,-5,9,-2,-9,8,2,8,7,-6,9,2,1,-2,-3,-6],[10,-5,7,-10,8,-6,9,8,-3,6,10,-7,-2,-2,1,-9],[-9,-8,4,5,-9,-2,-4,4,-7,-3,-10,2,1,-9,3,-3],[-4,1,2,10,6,10,6,-1,-8,-2,7,2,-9,2,9,-4],[-10,-1,-2,4,6,-10,-9,5,-5,6,2,-10,7,3,-1,10]],[[-4,6,3,4,5,10,-4,1,-4,1,-5,7,7,9,-8,9],[-10,-8,4,-2,7,-3,9,-10,1,10,-4,-7,6,-7,4,8],[1,-7,-9,4,-1,7,-2,-2,10,-10,-9,-3,4,-1,8,-4],[-5,-3,-10,-2,-5,10,10,2,-5,4,1,1,9,-6,1,-5],[-3,-5,-5,-3,-8,10,6,-7,6,7,9,5,-1,-5,2,-3],[8,7,4,4,4,1,-5,3,10,-1,9,8,-8,4,-3,-7],[4,-4,4,2,1,-10,-4,8,-4,-4,4,2,-5,1,5,8],[-2,2,10,3,-9,-8,5,-8,4,1,4,-9,4,-8,10,10],[8,-7,6,-8,5,8,1,-9,8,2,-7,-2,2,10,3,3],[2,10,2,-4,3,8,-10,8,9,9,-10,7,-8,-4,-6,4],[7,-5,1,7,-1,-7,-4,-8,-2,10,-9,-4,1,10,4,-5],[-10,-3,2,-5,5,-6,5,-3,-3,1,-8,-1,-4,8,6,1],[8,9,4,-6,3,9,8,-7,4,4,-4,3,-7,5,6,1],[2,3,1,-6,-1,-6,-6,1,2,4,-2,5,-9,1,8,9],[-2,-5,-4,-1,5,-8,-2,-3,-6,-2,5,6,-8,1,-10,6],[-5,-7,2,-5,-3,10,-2,10,1,6,9,-9,-8,-5,-1,2]],[[-3,-6,-5,4,4,5,-6,-5,9,10,-3,7,1,2,4,-9],[-3,4,6,7,-1,-9,1,1,-7,-10,-3,-4,8,8,9,8],[2,1,-9,9,3,6,-4,-4,1,-3,-10,1,-2,9,-6,-5],[-9,8,5,10,7,-3,-5,4,-10,10,-2,7,10,9,-5,8],[-3,5,-6,-7,1,6,7,-1,4,7,2,2,-2,-10,7,2],[-4,9,2,-5,-6,-8,-8,9,2,-8,2,8,2,10,8,9],[-8,4,-4,2,7,-4,1,-6,9,-9,7,4,7,-1,7,7],[-10,-7,1,6,-1,4,4,-7,6,-6,1,-4,-6,-3,7,-2],[2,-3,1,2,10,6,-6,8,6,6,-6,8,-5,6,-3,-1],[8,-10,5,-10,6,8,-8,-3,-2,4,9,-9,2,-10,-6,2],[5,4,1,-5,-10,8,-1,2,10,-1,-7,5,8,4,6,-9],[-5,-3,6,5,10,4,6,7,2,-7,2,8,-7,3,8,6],[-4,-4,-6,-6,2,-10,-8,4,-8,-10,-3,10,3,-5,7,8],[2,-2,1,-5,-10,3,5,-9,-10,-5,9,7,1,5,-5,1],[-7,6,-3,-4,7,2,-7,-6,1,-4,-9,2,-4,9,-4,-7],[-5,10,5,10,1,3,-10,9,-2,-2,3,-10,5,-6,-2,-9]],[[-7,3,-2,1,3,-3,7,-6,6,-10,4,-6,1,-7,7,8],[-6,6,-5,3,-3,5,-10,-8,1,-5,-8,-3,5,2,7,-5],[-2,-10,8,-7,10,2,2,-8,10,5,4,-6,9,10,9,-8],[-6,8,-4,6,4,5,10,9,7,-7,-4,-2,3,1,-7,3],[-9,-9,5,-8,5,-6,-9,4,-9,-6,4,-7,2,-8,-9,4],[3,1,-1,8,-4,-1,-9,8,-6,2,4,8,9,5,-9,6],[-6,-10,9,5,10,6,-10,9,9,-7,-5,1,1,2,6,-3],[-8,-9,9,-8,-9,10,9,9,-3,4,-1,1,-10,-3,-2,1],[7,7,-4,-7,-1,6,6,-1,10,-6,10,-5,10,-1,4,4],[-1,-1,8,-10,5,-3,1,-2,9,4,-5,2,-6,-10,4,-4],[-7,-2,3,5,9,-10,2,-3,-2,-2,5,4,8,2,10,-7],[-2,-3,2,-4,-8,1,-8,10,-9,-7,-8,-6,7,-8,-7,-5],[5,-4,7,-10,-2,-4,-5,-10,-7,-1,-10,-1,6,-5,6,9],[-9,2,1,-1,-1,3,9,10,-10,1,7,-6,-5,5,-2,-5],[-9,9,9,5,4,5,1,9,8,1,4,-10,10,-10,-4,-5],[4,-5,3,2,-7,-1,6,-8,-10,2,8,-4,-9,-5,3,-6]],[[-6,-9,-10,-6,-10,3,-7,-8,2,2,4,-10,-4,8,5,-4],[4,1,4,10,4,-8,6,9,-8,8,1,-6,3,10,-9,-10],[-8,8,-8,-4,4,5,-9,-8,9,10,-3,3,-4,7,-9,-6],[-8,7,-3,-10,4,-6,2,-4,9,-1,2,-2,8,10,6,4],[-10,-2,3,-1,7,-2,1,-4,-1,5,-8,10,4,-5,7,6],[10,10,8,-2,9,8,9,-10,-6,4,2,1,-7,8,-6,1],[10,7,5,5,-3,-3,6,5,-8,5,6,-6,4,6,8,-4],[-9,6,-10,7,7,-10,-3,2,-7,-3,-5,-5,-3,-7,-8,-9],[3,10,-8,1,-5,8,-7,3,-9,4,-3,5,1,7,4,-4],[-1,10,-1,7,-1,6,-5,-9,-3,-10,-3,-6,-6,4,1,7],[-4,3,8,-1,-3,5,8,-2,-9,9,7,8,10,-3,2,3],[7,-1,-8,-1,1,-10,-2,-2,-7,4,-6,-7,-8,7,10,-8],[-8,1,-5,-6,8,7,-10,-2,-10,9,3,-4,8,-1,-3,-7],[-9,-8,1,-3,2,1,-7,-7,1,2,-3,5,8,-2,-6,-4],[7,1,8,9,2,-9,2,5,-3,-9,3,-2,9,-4,2,10],[-1,-9,5,-6,7,7,3,-5,10,7,-6,-6,2,10,9,-5]],[[-2,-7,2,5,1,9,3,4,-7,-7,-7,-10,3,5,3,-2],[4,-4,-7,6,-9,3,10,-7,8,4,7,6,-7,3,1,-4],[9,3,-5,5,5,-9,-7,4,10,-3,-3,8,10,-7,-9,9],[-9,3,3,-1,5,-5,-6,-8,-8,-1,7,-10,-1,9,-2,-7],[1,6,-5,4,8,-4,8,-9,10,9,1,8,10,3,6,-10],[7,2,-4,-6,6,7,10,2,9,-9,3,-2,5,-3,-5,-1],[-3,-8,9,-1,2,1,-5,-3,-6,-5,-2,-4,-2,1,3,2],[4,5,2,8,-4,-7,4,3,4,1,-5,-2,-3,6,4,-2],[-6,2,2,3,1,-7,9,4,-6,-7,9,9,4,-10,3,-7],[-10,8,-8,-8,-8,3,4,1,2,2,9,5,-9,2,-6,3],[-7,-8,10,6,-2,7,6,-8,6,-10,-5,8,10,6,-8,-4],[9,-10,9,-1,4,-8,8,9,-8,-10,-5,-9,-8,-1,-3,1],[-6,-3,6,-5,-1,-1,9,-4,-10,-3,1,-8,-6,-5,-5,-3],[7,5,9,6,-4,-1,-6,1,-7,10,6,-9,10,-3,2,5],[3,7,-1,4,-9,-8,1,-2,6,8,-10,4,3,-5,3,-8],[-4,-8,5,2,-10,10,2,10,4,9,9,5,1,8,-2,10]],[[-9,-10,-2,-10,-3,-2,2,4,-3,1,-6,-3,4,9,-8,-1],[7,5,4,-2,8,5,-7,6,-9,2,-1,2,-6,3,-10,-5],[8,6,5,-2,-1,3,-3,10,5,-9,6,-6,-2,8,-3,-9],[-3,4,5,1,10,-6,4,-7,5,-7,-7,5,10,-1,6,-8],[7,9,8,7,-3,-3,8,-5,-7,-6,-5,-2,-4,-2,3,1],[1,-1,9,7,3,-10,1,4,10,-10,8,-2,5,3,3,9],[4,-1,9,7,-9,3,-2,5,6,7,-9,8,-2,-5,7,-6],[-3,-3,8,-6,-7,-6,5,-1,1,5,-8,6,-4,-4,3,1],[9,-10,-6,-4,5,-1,5,1,3,-6,1,-10,2,-7,6,-3],[-3,-1,-1,-1,-9,7,8,10,6,-10,-9,-3,6,6,-9,6],[3,-3,4,-3,8,-9,-9,-6,6,-3,10,-5,-5,8,-1,-6],[-4,1,2,-3,3,7,-10,9,2,-2,-8,-9,-8,-9,-3,-3],[3,-5,7,7,9,-2,-8,-6,2,3,6,5,10,5,10,-10],[-4,-9,-10,-1,-2,-7,-3,-3,4,-7,9,-6,-7,-4,-9,-9],[7,3,6,-8,4,-3,10,-4,-3,5,-2,-2,-2,-5,9,3],[3,5,10,10,-1,-3,-8,-7,5,-2,3,-3,8,-5,3,5]],[[5,-5,-3,9,9,-5,6,-9,-4,-7,5,-1,9,10,-7,5],[-4,5,9,-1,5,-7,-6,1,7,6,-7,3,-6,-7,9,-4],[-6,10,2,-6,-7,-7,9,-2,5,6,-8,9,5,6,-10,7],[-9,1,-8,10,10,-8,-7,-5,10,-6,2,4,-3,-1,1,9],[7,-1,7,-2,-1,5,-1,-10,-2,3,4,-3,-8,-10,-6,-8],[10,-10,3,3,-2,-9,9,-6,-8,6,6,8,8,2,-8,-9],[-10,-5,-8,-4,-7,3,-4,6,10,1,5,-10,9,7,2,8],[-4,2,1,4,9,-3,-8,5,3,6,7,-1,9,8,5,-1],[10,10,-1,1,-4,3,5,2,5,-6,-5,3,-6,-5,-8,9],[-4,-9,-5,-5,7,1,-7,10,2,-6,-4,2,9,-2,-6,5],[1,-2,-6,-5,6,-5,-10,5,-2,8,-2,-7,-10,10,-1,5],[-10,-10,6,9,3,5,10,7,10,7,8,5,-4,-3,7,-1],[-6,5,-8,6,-10,-9,10,10,1,-4,-3,6,-1,4,-6,-6],[6,6,6,9,2,6,-2,-4,6,-4,4,-6,-9,-6,7,-7],[3,-9,7,7,-4,1,-3,-10,10,8,4,-2,8,7,-10,-8],[-10,-6,-5,-6,9,-8,2,-9,-4,8,-5,-2,-8,6,-5,-5]],[[-3,2,7,10,5,6,6,10,6,-9,-10,-4,9,-10,-6,7],[-7,1,7,10,1,-9,-3,8,-9,-10,5,-9,4,7,4,3],[-5,7,-8,-5,-3,8,7,5,1,7,1,-2,-5,7,5,3],[6,5,7,5,-8,3,-8,-1,6,-9,-6,-2,-10,-2,-10,-6],[-7,4,-2,-1,3,4,-4,2,-5,-7,-2,1,9,-10,10,-7],[8,10,-10,8,7,-5,-9,3,10,4,-10,-5,-8,-9,-2,5],[10,7,8,-3,7,8,-7,-9,-4,8,-6,4,-9,-4,1,-10],[-7,-1,4,2,4,-7,-2,7,-9,-1,-9,1,-7,-10,6,-1],[8,-10,8,4,-3,-2,-9,-2,-3,3,5,3,-9,-2,6,10],[7,-8,1,6,5,10,6,-2,2,-4,-9,10,-1,-5,-8,-1],[-4,-2,1,10,6,1,1,-5,-9,1,-6,-6,-5,-4,-5,-2],[5,5,-1,-3,-2,-1,8,-5,6,2,6,1,-10,-8,1,5],[1,-2,-2,9,9,-6,-7,3,8,-5,5,8,2,-2,4,-1],[-5,7,-9,-3,8,7,-2,-9,8,-3,-2,10,-6,9,10,-5],[4,-4,8,-5,-7,-2,-3,-7,6,5,2,-4,-8,10,-4,6],[-9,-2,8,-5,-8,-1,-9,3,2,-5,-3,-5,-1,-10,-10,-4]],[[-7,-7,-2,9,9,-4,-10,-4,-4,7,8,-8,-6,6,7,6],[6,10,-6,-9,-8,-1,-9,9,4,1,-7,-4,9,3,-2,1],[-2,6,-9,3,2,-4,-9,-4,-10,-8,6,-3,2,3,5,-1],[-9,5,6,3,-1,8,-3,-4,1,-1,-4,4,-10,-3,4,-2],[-3,-9,4,-8,3,5,-10,9,3,-8,6,-6,-10,-1,-2,-5],[7,-5,-10,-6,-9,-8,-1,10,-9,-4,2,-3,-8,-5,5,-5],[-6,5,-3,8,3,-3,-3,10,-5,8,2,-8,-6,-1,4,5],[-8,7,-3,-5,9,1,-5,7,-5,5,-6,10,-9,5,6,-5],[-10,8,-5,2,-3,7,5,-5,-1,-10,5,-1,10,8,-3,10],[3,-1,-1,4,5,9,7,10,4,5,7,-4,1,3,-4,9],[3,8,2,-7,5,-5,-1,10,-5,7,-2,-9,6,7,8,-9],[-8,6,-9,5,2,8,-4,-9,5,1,10,8,-3,-5,-3,-4],[3,8,-5,-8,2,-10,-4,7,6,7,-9,1,-10,-5,-3,3],[-10,-10,4,4,3,6,3,-9,3,-7,10,6,-8,-4,-1,7],[-10,8,4,-1,4,-4,-1,7,8,-4,-2,2,-1,-1,5,-6],[6,6,6,6,-5,8,-5,7,9,-4,2,-2,-2,7,-2,2]]], dtype = "int64")#candidate|3069|(11, 16, 16)|const|int64
bop_3070 = relay.greater_equal(var_3068.astype('bool'), relay.reshape(const_3069.astype('bool'), relay.shape_of(var_3068))) # shape=(11, 16, 16)
uop_3074 = relay.cosh(var_3068.astype('float32')) # shape=(11, 16, 16)
var_3085 = relay.var("var_3085", dtype = "int64", shape = (11, 16, 16))#candidate|3085|(11, 16, 16)|var|int64
bop_3086 = relay.not_equal(const_3069.astype('bool'), relay.reshape(var_3085.astype('bool'), relay.shape_of(const_3069))) # shape=(11, 16, 16)
uop_3091 = relay.exp(uop_3074.astype('float64')) # shape=(11, 16, 16)
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_3093 = relay.TupleGetItem(func_1448_call(), 1)
call_3094 = relay.TupleGetItem(func_1449_call(), 1)
output = relay.Tuple([bop_3070,bop_3086,uop_3091,call_3093,])
output2 = relay.Tuple([bop_3070,bop_3086,uop_3091,call_3094,])
func_3098 = relay.Function([var_3068,var_3085,], output)
mod['func_3098'] = func_3098
mod = relay.transform.InferType()(mod)
var_3099 = relay.var("var_3099", dtype = "int64", shape = (11, 16, 16))#candidate|3099|(11, 16, 16)|var|int64
var_3100 = relay.var("var_3100", dtype = "int64", shape = (11, 16, 16))#candidate|3100|(11, 16, 16)|var|int64
output = func_3098(var_3099,var_3100,)
func_3101 = relay.Function([var_3099,var_3100,], output)
mutated_mod['func_3101'] = func_3101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_3108 = relay.TupleGetItem(func_764_call(), 0)
call_3109 = relay.TupleGetItem(func_766_call(), 0)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_3123 = func_135_call()
call_3124 = func_135_call()
func_2309_call = mod.get_global_var('func_2309')
func_2312_call = mutated_mod.get_global_var('func_2312')
const_3126 = relay.const([-3.458512,2.299303,3.101287,1.965289,-5.690676,3.228024,-1.765328,0.547926,-2.628663,-7.821359,-0.160271,4.978677,-6.935589,-0.683958,4.287437,-1.395002,8.831385,0.076395,7.342599,0.491867,-4.654172,-4.622382,3.048838,-9.569814,-5.656550,-8.347430,-0.796820,1.227823,5.135570,-3.693438,8.128232,-2.402583,1.777254,9.534735,-9.740763,-3.814072,-1.487844,6.017778,-8.137736,7.457640,3.588913,9.088955,7.615537,-1.788710,-8.914495,5.725023,1.455740,-9.027458,3.058646,3.269238,3.954424,8.048510,1.454754,5.845645,-2.941235,-7.784105,-8.222689,9.821198,-8.759233,-8.341567,-4.753262,-2.486946,6.142694,-6.767441,-0.475749,5.494755,0.637844,7.478659,5.062709,4.964334,7.046022,6.080719,2.011116,9.091614,6.713360,2.370348,-2.275762,8.872518,-2.005360,-0.629117,-0.765497,-5.191176,-5.638549,-5.572030,2.995525,1.950330,3.334867,-2.006333,8.874645,-6.935984,-7.688438,3.902845,4.822167,-2.125281,-3.625087,-0.768732,-2.113726,2.044571,1.168709,8.757657,0.792445,9.961204,3.172296,5.128237,-6.460809,5.684013,2.171972,8.391664,-5.112342,9.216347,-1.618475,3.024707,-5.491909,-4.722791,-0.768656,-4.117160,-4.829902,-6.809239,-2.304816,7.814549,4.399512,4.291649,5.694088,3.614798,-1.708399,-0.820278,-4.034789,-3.399236,-7.933090,-0.592668,-0.286301,-1.133996,1.384583,-1.137474,7.969690,-4.763300,8.081413,6.222029,-3.131642,-8.573091,9.902553,5.490805,-6.053192,9.124055,-4.586048,8.332532,-4.641752,-8.073807,-8.860048,0.293735,-6.759281,-2.372137,1.063241,-7.833355,-7.517622,2.047314,0.816568,8.228874,-8.956071,2.304280,1.495052,3.623323,-6.368266,4.748873,-7.522153,-7.383167,-5.042431,-2.782612,1.945510,3.876874,3.396387,4.092217,1.736966,-8.314079,4.799901,4.847795,-3.753681,1.322104,-2.016942,8.305230,9.566171,5.922731,-3.448237,-3.021561,-3.638328,3.707544,-4.837146,-0.836444,-1.421890,8.590299,-7.243765,-0.285168,8.052404,-0.667021,-0.674122,-8.894228,7.415726,5.184277,-2.275803,1.067401,7.719864,-1.114642,-0.859395,1.702628,-9.552893,-6.373272,0.797508,7.875799,-5.591492,-3.662658,-4.340385,0.861807,-6.582886,0.159419,-2.089897,2.169814,-3.025022,6.484629,3.565454,2.455076,6.201645,-3.238152,-7.500371,4.408752,6.680077,0.988941,-6.465946,-2.188704,7.201784,6.193836,-4.730892,1.748905,1.986039,3.330686,1.941863,-8.308855,7.555728,-2.173415,-8.488661,-2.055406,3.428545,1.897081,-0.751130,6.611121,-3.214930,3.329933,7.061671,5.415459,1.505090,6.133561,0.819641,7.056921,2.013360,-3.862870,5.610736,2.886889,-7.507146,8.166057,-2.019991,-5.212460,6.303230,-6.899104,-0.657119,2.241361,-5.419419,-1.066820,-1.151433,-1.148227,8.824282,-7.332217,-3.169710,-5.286894,-3.887865,3.058213,-2.427296,0.779100,-2.592694,-4.789777,2.908144,-7.651304,3.341956,6.492696,9.769014,9.962983,-9.010127,2.317921,1.503194,3.274220,9.206497,2.152322,-5.223493,-5.244179,-2.686821,1.278691,-5.783954,9.254550,1.077609,-9.634845,7.905088,2.982620,1.834102,-6.642064,-4.459063,-5.165566,-0.764933,0.654392,2.863156,2.382035,8.210472,1.807685,5.771303,3.444478,-4.368591,7.685807,2.009201,3.464799,4.520612,5.935167,-6.890576,-0.200251,2.241180,3.250008,2.089371,-6.900136,-6.088204,-0.497332,8.428539,-6.262208,0.336103,1.585922,-0.731123,8.892969,-0.305161,-6.741108,0.047198,7.288139,-7.279167,9.805382,-9.992242,-5.687845,4.881598,-0.650357,-6.456408,-8.155073,-4.322914,-4.410895,6.970580,-3.916957,8.151414,-9.624305,9.115254,3.235923,-7.524735,4.003401,7.745568,3.474033,6.177885,3.288208,-4.851062,8.741742,4.657208,-1.677509,-6.710304,-5.718451], dtype = "float64")#candidate|3126|(364,)|const|float64
call_3125 = relay.TupleGetItem(func_2309_call(relay.reshape(const_3126.astype('float64'), [364,])), 2)
call_3127 = relay.TupleGetItem(func_2312_call(relay.reshape(const_3126.astype('float64'), [364,])), 2)
var_3134 = relay.var("var_3134", dtype = "float64", shape = (364,))#candidate|3134|(364,)|var|float64
bop_3135 = relay.greater_equal(call_3125.astype('bool'), relay.reshape(var_3134.astype('bool'), relay.shape_of(call_3125))) # shape=(364,)
bop_3138 = relay.greater_equal(call_3127.astype('bool'), relay.reshape(var_3134.astype('bool'), relay.shape_of(call_3127))) # shape=(364,)
var_3140 = relay.var("var_3140", dtype = "float64", shape = (364,))#candidate|3140|(364,)|var|float64
bop_3141 = relay.right_shift(var_3134.astype('uint64'), relay.reshape(var_3140.astype('uint64'), relay.shape_of(var_3134))) # shape=(364,)
func_2611_call = mod.get_global_var('func_2611')
func_2613_call = mutated_mod.get_global_var('func_2613')
call_3146 = relay.TupleGetItem(func_2611_call(relay.reshape(call_3108.astype('uint64'), [4, 6, 5])), 0)
call_3147 = relay.TupleGetItem(func_2613_call(relay.reshape(call_3108.astype('uint64'), [4, 6, 5])), 0)
uop_3154 = relay.asin(bop_3135.astype('float32')) # shape=(364,)
uop_3156 = relay.asin(bop_3138.astype('float32')) # shape=(364,)
output = relay.Tuple([call_3108,call_3123,const_3126,bop_3141,call_3146,uop_3154,])
output2 = relay.Tuple([call_3109,call_3124,const_3126,bop_3141,call_3147,uop_3156,])
func_3165 = relay.Function([var_3134,var_3140,], output)
mod['func_3165'] = func_3165
mod = relay.transform.InferType()(mod)
mutated_mod['func_3165'] = func_3165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3165_call = mutated_mod.get_global_var('func_3165')
var_3167 = relay.var("var_3167", dtype = "float64", shape = (364,))#candidate|3167|(364,)|var|float64
var_3168 = relay.var("var_3168", dtype = "float64", shape = (364,))#candidate|3168|(364,)|var|float64
call_3166 = func_3165_call(var_3167,var_3168,)
output = call_3166
func_3169 = relay.Function([var_3167,var_3168,], output)
mutated_mod['func_3169'] = func_3169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_336_call = mod.get_global_var('func_336')
func_338_call = mutated_mod.get_global_var('func_338')
call_3256 = relay.TupleGetItem(func_336_call(), 1)
call_3257 = relay.TupleGetItem(func_338_call(), 1)
func_2444_call = mod.get_global_var('func_2444')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_3259 = relay.TupleGetItem(func_2444_call(), 1)
call_3260 = relay.TupleGetItem(func_2446_call(), 1)
output = relay.Tuple([call_3256,call_3259,])
output2 = relay.Tuple([call_3257,call_3260,])
func_3276 = relay.Function([], output)
mod['func_3276'] = func_3276
mod = relay.transform.InferType()(mod)
output = func_3276()
func_3277 = relay.Function([], output)
mutated_mod['func_3277'] = func_3277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_3307 = relay.TupleGetItem(func_256_call(), 0)
call_3308 = relay.TupleGetItem(func_258_call(), 0)
uop_3309 = relay.log(call_3307.astype('float32')) # shape=(4, 6, 5)
uop_3311 = relay.log(call_3308.astype('float32')) # shape=(4, 6, 5)
uop_3316 = relay.exp(uop_3309.astype('float32')) # shape=(4, 6, 5)
uop_3318 = relay.exp(uop_3311.astype('float32')) # shape=(4, 6, 5)
output = uop_3316
output2 = uop_3318
func_3321 = relay.Function([], output)
mod['func_3321'] = func_3321
mod = relay.transform.InferType()(mod)
mutated_mod['func_3321'] = func_3321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3321_call = mutated_mod.get_global_var('func_3321')
call_3322 = func_3321_call()
output = call_3322
func_3323 = relay.Function([], output)
mutated_mod['func_3323'] = func_3323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_472_call = mod.get_global_var('func_472')
func_474_call = mutated_mod.get_global_var('func_474')
call_3327 = relay.TupleGetItem(func_472_call(), 0)
call_3328 = relay.TupleGetItem(func_474_call(), 0)
func_2065_call = mod.get_global_var('func_2065')
func_2069_call = mutated_mod.get_global_var('func_2069')
const_3344 = relay.const([7.689240,-5.136749,-3.054972,-2.971537,9.404823,-1.623310,-2.722833,6.774200,5.012576,-8.142779,-2.202654,-2.076761,-1.522630,-9.399197,-5.153557,4.961765,5.092909,9.431627,9.145096,1.926739,-7.232680,7.031150,8.655628,-2.128940,8.718049,-8.289767,4.094582,0.498571,0.831563,-1.671922,5.441106,5.900260,0.329376,7.219041,2.026488,-4.436175,-6.901089,-2.792461,-1.839599,-0.199051,5.934888,6.457394,5.514097,-3.368614,-1.189534,0.935113,3.280186,2.399937,0.564821,5.878103,9.462861,-8.551177,4.019166,-1.631388,1.288732,5.120566,1.710778,1.692708,-8.196957,9.387979,-2.596572,-6.932270,-1.163467,0.513380,-1.360829,-2.992312,-7.344043,-9.400603,6.483534,1.145268,8.247369,6.239406,1.224299,-5.171323,-2.428002,-7.408808,-6.443125,-0.544239,-5.932587,-5.434727,-6.634834,3.670462,8.801584,5.232920,-0.436986,0.539644,7.709280,-2.052205,2.018219,-6.317803,1.001327,2.313489,-4.942017,-4.767545,3.010120,1.356770,1.042456,-8.975573,-0.455968,3.300049,-6.447994,4.737901,6.624731,-0.384888,-4.406553,-1.886072,9.149852,0.876722,-9.133466,6.786204,-3.004682,5.437042,8.471525,-0.496723,6.041813,-1.360680,-0.497236,-9.082355,5.120940,-4.098740,4.784213,4.686000,-7.240454,-2.614226,-2.375769,-3.201793,7.558124,-6.292558,6.541266,-9.408918,-8.843282,-2.242091,-1.868962,-9.679907,0.626844,9.980995,-2.481709,-0.136501,6.626650,1.319425,-5.250233,-1.293294,1.719523,-6.600046,2.224500,-8.901559,0.734666,-1.034832,8.440030,0.203883,-0.623485,3.738363,-8.769167,5.704438,5.827151,2.880835,3.287382,8.105682,0.251133,9.545987,-8.744173,-5.368564,4.811969,-1.771977,-1.130157,5.466092,-1.992496,3.168124,-8.398444,2.655312,7.569516,0.229745,-8.170876,0.721864,-5.051339,3.869669,-2.895179,-2.624392,-2.647352,-4.709914,2.657542,7.015279,0.989143,-4.109156,-3.273695,9.035046,-3.529785,-8.105597,9.011279,-4.645873,-5.822689,-1.235777,-7.630890,-1.086227,4.247215,4.426413,2.849328,8.217623,5.595191,-5.141762,2.380700,8.014233,2.405840,-2.175842,6.615164,-6.495182,-4.082909,5.900432,-8.438034,-6.322979,-3.691084,-1.761944,-4.238677,-9.485541,5.865234,9.938165,-6.567399,-6.448644,-6.346585,-2.413223,-8.550725,-3.031257,-0.129151,4.154367,1.004179,-3.688201,0.188341,9.483536,-4.424221,6.839819,9.760146,-2.524914,9.585371,3.847786,-1.113454,8.634359,-4.975173,1.791313,6.516845,9.974537,-2.571218,2.515916,-8.791170,-5.728137,-7.074047,-0.978630,-2.331816,-6.681145,-1.756969,-6.418167,9.275168,2.372616,2.295704,-4.803324,0.789444,1.662194,-3.754098,3.210557,-3.385526,4.188375,4.258829,-1.750350,2.761221,7.339267,-4.728597,-8.907992,8.227758,0.336930,-7.825075,-6.164386,-5.786443,-6.413645,-9.302375,9.108548,9.946983,4.312823,3.558171,-9.031201,-4.932758,-6.983941,3.633985,4.303177,-6.618721,5.880320,-4.938473,-0.027897,-0.244562,8.463039,-9.585908,0.338326,-9.478481,-3.350683,-0.233622,-6.132065,-8.453714,4.716498,1.762340,-9.541525,3.927665,-9.395682,9.182070,-6.843586,3.156106,-4.251447,9.367791,2.565534,6.441193,1.598885,7.847604,-4.570000,-7.103208,3.175109,-4.940622,2.264016,-7.309708,-1.356429,-1.338844,8.536011,-3.878434,1.859983,8.664500,5.482394,-3.192013,-6.250590,-2.810546,9.671990,-9.431031,-7.607998,-8.305122,-2.169742,-7.985495,5.166947,-9.802593,-4.924617,-0.174588,-2.035445,5.701035,-5.029344,-8.457810,8.497547,-6.873938,9.660563,8.276566,5.246447,7.236547,-9.563418,-7.434590,-7.652310,-3.257737,-1.814795,-3.067172,-7.773087,-1.150950,5.810000,1.012730,-7.827794,8.555404,-9.346815,6.921491,-9.774653,-1.826242,-7.114557,-2.778497,0.028078], dtype = "float64")#candidate|3344|(364,)|const|float64
var_3345 = relay.var("var_3345", dtype = "float64", shape = (1092, 1))#candidate|3345|(1092, 1)|var|float64
call_3343 = relay.TupleGetItem(func_2065_call(relay.reshape(const_3344.astype('float64'), [364,]), relay.reshape(var_3345.astype('float64'), [1092,]), ), 0)
call_3346 = relay.TupleGetItem(func_2069_call(relay.reshape(const_3344.astype('float64'), [364,]), relay.reshape(var_3345.astype('float64'), [1092,]), ), 0)
func_2706_call = mod.get_global_var('func_2706')
func_2708_call = mutated_mod.get_global_var('func_2708')
call_3350 = func_2706_call()
call_3351 = func_2706_call()
bop_3368 = relay.less(var_3345.astype('bool'), const_3344.astype('bool')) # shape=(1092, 364)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_3371 = relay.TupleGetItem(func_764_call(), 3)
call_3372 = relay.TupleGetItem(func_766_call(), 3)
func_2323_call = mod.get_global_var('func_2323')
func_2327_call = mutated_mod.get_global_var('func_2327')
var_3378 = relay.var("var_3378", dtype = "int16", shape = (375,))#candidate|3378|(375,)|var|int16
call_3377 = relay.TupleGetItem(func_2323_call(relay.reshape(var_3378.astype('int16'), [5, 5, 15]), relay.reshape(var_3378.astype('int16'), [5, 5, 15]), ), 1)
call_3379 = relay.TupleGetItem(func_2327_call(relay.reshape(var_3378.astype('int16'), [5, 5, 15]), relay.reshape(var_3378.astype('int16'), [5, 5, 15]), ), 1)
bop_3390 = relay.greater_equal(var_3378.astype('bool'), var_3345.astype('bool')) # shape=(1092, 375)
uop_3400 = relay.sigmoid(bop_3368.astype('float64')) # shape=(1092, 364)
func_1038_call = mod.get_global_var('func_1038')
func_1039_call = mutated_mod.get_global_var('func_1039')
call_3402 = relay.TupleGetItem(func_1038_call(), 0)
call_3403 = relay.TupleGetItem(func_1039_call(), 0)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_3414 = relay.TupleGetItem(func_764_call(), 0)
call_3415 = relay.TupleGetItem(func_766_call(), 0)
bop_3417 = relay.greater_equal(uop_3400.astype('bool'), call_3343.astype('bool')) # shape=(1092, 364)
bop_3420 = relay.greater_equal(uop_3400.astype('bool'), call_3346.astype('bool')) # shape=(1092, 364)
output = relay.Tuple([call_3327,call_3350,call_3371,call_3377,bop_3390,call_3402,call_3414,bop_3417,])
output2 = relay.Tuple([call_3328,call_3351,call_3372,call_3379,bop_3390,call_3403,call_3415,bop_3420,])
func_3423 = relay.Function([var_3345,var_3378,], output)
mod['func_3423'] = func_3423
mod = relay.transform.InferType()(mod)
mutated_mod['func_3423'] = func_3423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3423_call = mutated_mod.get_global_var('func_3423')
var_3425 = relay.var("var_3425", dtype = "float64", shape = (1092, 1))#candidate|3425|(1092, 1)|var|float64
var_3426 = relay.var("var_3426", dtype = "int16", shape = (375,))#candidate|3426|(375,)|var|int16
call_3424 = func_3423_call(var_3425,var_3426,)
output = call_3424
func_3427 = relay.Function([var_3425,var_3426,], output)
mutated_mod['func_3427'] = func_3427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_3437 = relay.TupleGetItem(func_2980_call(), 2)
call_3438 = relay.TupleGetItem(func_2982_call(), 2)
uop_3441 = relay.acosh(call_3437.astype('float32')) # shape=(1, 364)
uop_3443 = relay.acosh(call_3438.astype('float32')) # shape=(1, 364)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
call_3446 = relay.TupleGetItem(func_674_call(), 0)
call_3447 = relay.TupleGetItem(func_676_call(), 0)
func_1659_call = mod.get_global_var('func_1659')
func_1661_call = mutated_mod.get_global_var('func_1661')
var_3450 = relay.var("var_3450", dtype = "float64", shape = (512,))#candidate|3450|(512,)|var|float64
call_3449 = relay.TupleGetItem(func_1659_call(relay.reshape(var_3450.astype('float64'), [8, 16, 4])), 0)
call_3451 = relay.TupleGetItem(func_1661_call(relay.reshape(var_3450.astype('float64'), [8, 16, 4])), 0)
uop_3456 = relay.tan(uop_3441.astype('float32')) # shape=(1, 364)
uop_3458 = relay.tan(uop_3443.astype('float32')) # shape=(1, 364)
bop_3465 = relay.add(uop_3441.astype('uint8'), relay.reshape(uop_3456.astype('uint8'), relay.shape_of(uop_3441))) # shape=(1, 364)
bop_3468 = relay.add(uop_3443.astype('uint8'), relay.reshape(uop_3458.astype('uint8'), relay.shape_of(uop_3443))) # shape=(1, 364)
output = relay.Tuple([call_3446,call_3449,var_3450,bop_3465,])
output2 = relay.Tuple([call_3447,call_3451,var_3450,bop_3468,])
func_3470 = relay.Function([var_3450,], output)
mod['func_3470'] = func_3470
mod = relay.transform.InferType()(mod)
var_3471 = relay.var("var_3471", dtype = "float64", shape = (512,))#candidate|3471|(512,)|var|float64
output = func_3470(var_3471)
func_3472 = relay.Function([var_3471], output)
mutated_mod['func_3472'] = func_3472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2011_call = mod.get_global_var('func_2011')
func_2012_call = mutated_mod.get_global_var('func_2012')
call_3477 = relay.TupleGetItem(func_2011_call(), 0)
call_3478 = relay.TupleGetItem(func_2012_call(), 0)
uop_3490 = relay.asinh(call_3477.astype('float64')) # shape=(4, 6, 5)
uop_3492 = relay.asinh(call_3478.astype('float64')) # shape=(4, 6, 5)
bop_3512 = relay.logical_and(uop_3490.astype('bool'), relay.reshape(call_3477.astype('bool'), relay.shape_of(uop_3490))) # shape=(4, 6, 5)
bop_3515 = relay.logical_and(uop_3492.astype('bool'), relay.reshape(call_3478.astype('bool'), relay.shape_of(uop_3492))) # shape=(4, 6, 5)
output = relay.Tuple([bop_3512,])
output2 = relay.Tuple([bop_3515,])
func_3529 = relay.Function([], output)
mod['func_3529'] = func_3529
mod = relay.transform.InferType()(mod)
mutated_mod['func_3529'] = func_3529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3529_call = mutated_mod.get_global_var('func_3529')
call_3530 = func_3529_call()
output = call_3530
func_3531 = relay.Function([], output)
mutated_mod['func_3531'] = func_3531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_135_call = mod.get_global_var('func_135')
func_136_call = mutated_mod.get_global_var('func_136')
call_3596 = func_135_call()
call_3597 = func_135_call()
uop_3618 = relay.erf(call_3596.astype('float64')) # shape=(4, 6, 5)
uop_3620 = relay.erf(call_3597.astype('float64')) # shape=(4, 6, 5)
func_538_call = mod.get_global_var('func_538')
func_542_call = mutated_mod.get_global_var('func_542')
const_3630 = relay.const([[3.557663],[5.393768],[-9.406678],[0.856698],[-3.399736],[-8.946220],[-2.433271],[5.615772],[6.295887],[8.438949],[3.334512],[-9.985531],[-3.471928],[-3.624322],[-0.579460],[-4.000189],[-3.002673],[4.700692],[0.668545],[6.688023],[4.794772],[-6.064525],[1.075880],[-5.469663],[-5.388088],[-3.274320],[0.520696],[0.527522],[3.378485],[-3.687482],[6.518192],[6.845323],[-2.018170],[-6.897674],[4.611765],[8.782321],[-1.493776],[2.927746],[8.686507],[-3.962052],[4.889064],[-3.913506],[1.240670],[-8.091549],[2.802652],[7.559342],[7.857766],[-4.716707],[8.239201],[-9.771556],[2.542033],[8.984105],[8.609305],[1.087136],[1.538346],[8.289218],[-2.650393],[8.712894],[0.104356],[-2.259429],[-4.938764],[-5.437126],[-9.616809],[7.894910],[3.949010],[0.246278],[-3.235261],[-9.205101],[7.510597],[-5.733206],[7.739303],[6.465807],[6.893965],[-4.125225],[-3.856965],[9.748482],[-2.965541],[0.965277],[8.531703],[-9.757874],[-6.810949],[2.043050],[-6.646338],[-3.251087],[8.770472],[-9.074202],[-5.723829],[-7.821164],[-6.631348],[3.073584],[-8.733067],[2.731787],[-0.329638],[9.017382],[-9.047697],[-2.385595],[8.519667],[9.191787],[-3.192229],[3.273984],[-1.838497],[-8.295796],[8.284302],[1.930652],[9.022736],[1.952399],[7.155341],[-3.238318],[2.100592],[5.388097],[2.048087],[-1.462705],[5.209684],[0.722915],[8.819205],[3.652285],[-7.833767],[0.135887],[1.948086],[-0.381556],[1.675274],[-8.607722],[-4.717547],[-2.405958],[-3.963544],[0.009551],[7.232078],[7.046203],[0.364737],[-2.486871],[5.945420],[6.881264],[-8.980763],[-9.882259],[0.732448],[-1.573749],[-9.749662],[2.860774],[-5.302561],[-2.880140],[-9.421302],[-7.520384],[7.960900],[-2.963163],[-2.111090],[5.301441],[3.239228],[-5.019266],[4.597506],[1.842271],[4.535376],[6.011435],[-6.578585],[-7.721495],[-8.255463],[2.049221],[3.070148],[7.239744],[0.189349],[6.130165],[-8.536231],[-4.597944],[3.994666],[3.029553],[9.430051],[2.119381],[0.042330],[-3.334131],[-4.883834],[-5.924076],[3.904125],[9.465562],[3.356133],[1.939356],[-0.870836],[1.995115],[2.152366],[-1.876845],[-4.834614],[-4.806962],[-1.647572],[-8.833354],[-8.814402],[8.004702],[9.964628],[-4.621574],[-3.136690],[7.824417],[-8.944172],[-3.348594],[-0.138363],[9.614849],[4.474185],[-8.647616],[-0.585751],[8.218784],[7.872186],[-8.070391],[-0.186045],[-1.258935],[7.007368],[-0.185320],[-6.452831],[4.646432],[-6.910567],[6.425459],[4.152516],[8.598576],[2.441657],[-8.982908],[-3.965474],[-3.124905],[0.653336],[1.764109],[9.087788],[-8.922578],[-3.047508],[-1.372361],[-7.245172],[7.754580],[2.741662],[0.533873],[-6.560688],[-8.451910],[9.590638],[8.114852],[-6.612774],[3.901489],[-4.639780],[-8.432202],[-0.678185],[-2.125014],[1.139844],[9.996539],[-3.112591],[6.342270],[7.692742],[3.129878],[0.821056],[9.029388],[-5.290837],[-7.229007],[1.997771],[4.309221],[-2.148877],[8.357433],[-4.692277],[-0.207384],[-3.967647],[3.691508],[-1.314942],[-8.405513],[-1.479405],[3.859330],[1.771952],[-9.688821],[5.961788],[6.078066],[-1.139505],[-0.104025],[-7.355217],[5.929472],[7.441528],[-3.107334],[7.927642],[8.586453],[-3.019078],[9.129704],[7.070315],[-0.380229],[-2.333838],[-2.516000],[4.889452],[-4.650340],[-9.092049],[0.808674],[-9.855582],[9.065580],[-6.253846],[1.847966],[-2.411084],[7.724068],[-2.572461],[0.568212],[-0.558247],[6.609556],[-3.494123],[-8.391019],[4.257531],[1.279460],[-9.452480],[-6.731914],[6.361990],[-4.312184],[2.240691],[5.516617],[-0.979302],[8.499858],[3.913357],[-0.827498],[-7.419971],[-4.375894],[-4.589036],[1.339323],[8.372550],[6.080833],[2.703727],[-3.578591],[-3.242125],[-7.044325],[-9.856256],[3.381283],[-2.916010],[-2.266476],[3.378001],[7.935000],[-9.129476],[-7.734466],[5.033025],[-2.857295],[-5.213543],[-8.209038],[8.276801],[-8.462467],[6.474264],[1.694948],[-8.053100],[4.311429],[2.651311],[-1.725663],[-4.886124],[1.227245],[-2.959361],[7.364875],[6.674389],[-1.626080],[-8.446169],[6.023789],[-5.051178],[9.072575],[-0.811610],[0.123534],[7.034253],[9.586461],[-9.250378],[4.247323],[-2.761217],[8.569992],[-8.877686],[-4.646871],[-1.058893],[1.884019],[3.094496],[-0.639456],[-6.936123],[0.606285],[0.335873],[8.763288],[6.105201],[4.584656],[-0.430646],[5.900260],[3.283205],[7.074141]], dtype = "float64")#candidate|3630|(364, 1)|const|float64
call_3629 = relay.TupleGetItem(func_538_call(relay.reshape(const_3630.astype('float64'), [364,]), relay.reshape(call_3596.astype('uint64'), [4, 6, 5]), ), 1)
call_3631 = relay.TupleGetItem(func_542_call(relay.reshape(const_3630.astype('float64'), [364,]), relay.reshape(call_3596.astype('uint64'), [4, 6, 5]), ), 1)
output = relay.Tuple([uop_3618,call_3629,const_3630,])
output2 = relay.Tuple([uop_3620,call_3631,const_3630,])
func_3636 = relay.Function([], output)
mod['func_3636'] = func_3636
mod = relay.transform.InferType()(mod)
output = func_3636()
func_3637 = relay.Function([], output)
mutated_mod['func_3637'] = func_3637
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3640 = relay.var("var_3640", dtype = "uint64", shape = (12, 6, 13))#candidate|3640|(12, 6, 13)|var|uint64
var_3641 = relay.var("var_3641", dtype = "uint64", shape = (12, 6, 13))#candidate|3641|(12, 6, 13)|var|uint64
bop_3642 = relay.not_equal(var_3640.astype('bool'), relay.reshape(var_3641.astype('bool'), relay.shape_of(var_3640))) # shape=(12, 6, 13)
bop_3646 = relay.power(bop_3642.astype('float64'), relay.reshape(var_3640.astype('float64'), relay.shape_of(bop_3642))) # shape=(12, 6, 13)
output = bop_3646
output2 = bop_3646
func_3657 = relay.Function([var_3640,var_3641,], output)
mod['func_3657'] = func_3657
mod = relay.transform.InferType()(mod)
mutated_mod['func_3657'] = func_3657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3657_call = mutated_mod.get_global_var('func_3657')
var_3659 = relay.var("var_3659", dtype = "uint64", shape = (12, 6, 13))#candidate|3659|(12, 6, 13)|var|uint64
var_3660 = relay.var("var_3660", dtype = "uint64", shape = (12, 6, 13))#candidate|3660|(12, 6, 13)|var|uint64
call_3658 = func_3657_call(var_3659,var_3660,)
output = call_3658
func_3661 = relay.Function([var_3659,var_3660,], output)
mutated_mod['func_3661'] = func_3661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_3726 = relay.TupleGetItem(func_380_call(), 0)
call_3727 = relay.TupleGetItem(func_381_call(), 0)
output = relay.Tuple([call_3726,])
output2 = relay.Tuple([call_3727,])
func_3738 = relay.Function([], output)
mod['func_3738'] = func_3738
mod = relay.transform.InferType()(mod)
output = func_3738()
func_3739 = relay.Function([], output)
mutated_mod['func_3739'] = func_3739
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3754 = relay.var("var_3754", dtype = "float32", shape = ())#candidate|3754|()|var|float32
var_3755 = relay.var("var_3755", dtype = "float32", shape = (3, 12, 15))#candidate|3755|(3, 12, 15)|var|float32
bop_3756 = relay.minimum(var_3754.astype('float32'), var_3755.astype('float32')) # shape=(3, 12, 15)
var_3762 = relay.var("var_3762", dtype = "float32", shape = (3, 12, 15))#candidate|3762|(3, 12, 15)|var|float32
bop_3763 = relay.add(bop_3756.astype('uint32'), relay.reshape(var_3762.astype('uint32'), relay.shape_of(bop_3756))) # shape=(3, 12, 15)
output = bop_3763
output2 = bop_3763
func_3776 = relay.Function([var_3754,var_3755,var_3762,], output)
mod['func_3776'] = func_3776
mod = relay.transform.InferType()(mod)
var_3777 = relay.var("var_3777", dtype = "float32", shape = ())#candidate|3777|()|var|float32
var_3778 = relay.var("var_3778", dtype = "float32", shape = (3, 12, 15))#candidate|3778|(3, 12, 15)|var|float32
var_3779 = relay.var("var_3779", dtype = "float32", shape = (3, 12, 15))#candidate|3779|(3, 12, 15)|var|float32
output = func_3776(var_3777,var_3778,var_3779,)
func_3780 = relay.Function([var_3777,var_3778,var_3779,], output)
mutated_mod['func_3780'] = func_3780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
call_3856 = relay.TupleGetItem(func_256_call(), 0)
call_3857 = relay.TupleGetItem(func_258_call(), 0)
var_3874 = relay.var("var_3874", dtype = "uint64", shape = (4, 6, 5))#candidate|3874|(4, 6, 5)|var|uint64
bop_3875 = relay.equal(call_3856.astype('bool'), relay.reshape(var_3874.astype('bool'), relay.shape_of(call_3856))) # shape=(4, 6, 5)
bop_3878 = relay.equal(call_3857.astype('bool'), relay.reshape(var_3874.astype('bool'), relay.shape_of(call_3857))) # shape=(4, 6, 5)
output = bop_3875
output2 = bop_3878
func_3882 = relay.Function([var_3874,], output)
mod['func_3882'] = func_3882
mod = relay.transform.InferType()(mod)
var_3883 = relay.var("var_3883", dtype = "uint64", shape = (4, 6, 5))#candidate|3883|(4, 6, 5)|var|uint64
output = func_3882(var_3883)
func_3884 = relay.Function([var_3883], output)
mutated_mod['func_3884'] = func_3884
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3886 = relay.var("var_3886", dtype = "int32", shape = (15, 16, 11))#candidate|3886|(15, 16, 11)|var|int32
var_3887 = relay.var("var_3887", dtype = "int32", shape = (15, 16, 11))#candidate|3887|(15, 16, 11)|var|int32
bop_3888 = relay.not_equal(var_3886.astype('bool'), relay.reshape(var_3887.astype('bool'), relay.shape_of(var_3886))) # shape=(15, 16, 11)
output = relay.Tuple([bop_3888,])
output2 = relay.Tuple([bop_3888,])
func_3899 = relay.Function([var_3886,var_3887,], output)
mod['func_3899'] = func_3899
mod = relay.transform.InferType()(mod)
mutated_mod['func_3899'] = func_3899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3899_call = mutated_mod.get_global_var('func_3899')
var_3901 = relay.var("var_3901", dtype = "int32", shape = (15, 16, 11))#candidate|3901|(15, 16, 11)|var|int32
var_3902 = relay.var("var_3902", dtype = "int32", shape = (15, 16, 11))#candidate|3902|(15, 16, 11)|var|int32
call_3900 = func_3899_call(var_3901,var_3902,)
output = call_3900
func_3903 = relay.Function([var_3901,var_3902,], output)
mutated_mod['func_3903'] = func_3903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2559_call = mod.get_global_var('func_2559')
func_2560_call = mutated_mod.get_global_var('func_2560')
call_3905 = relay.TupleGetItem(func_2559_call(), 0)
call_3906 = relay.TupleGetItem(func_2560_call(), 0)
output = call_3905
output2 = call_3906
func_3925 = relay.Function([], output)
mod['func_3925'] = func_3925
mod = relay.transform.InferType()(mod)
mutated_mod['func_3925'] = func_3925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3925_call = mutated_mod.get_global_var('func_3925')
call_3926 = func_3925_call()
output = call_3926
func_3927 = relay.Function([], output)
mutated_mod['func_3927'] = func_3927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2706_call = mod.get_global_var('func_2706')
func_2708_call = mutated_mod.get_global_var('func_2708')
call_3965 = func_2706_call()
call_3966 = func_2706_call()
output = relay.Tuple([call_3965,])
output2 = relay.Tuple([call_3966,])
func_3973 = relay.Function([], output)
mod['func_3973'] = func_3973
mod = relay.transform.InferType()(mod)
mutated_mod['func_3973'] = func_3973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3973_call = mutated_mod.get_global_var('func_3973')
call_3974 = func_3973_call()
output = call_3974
func_3975 = relay.Function([], output)
mutated_mod['func_3975'] = func_3975
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3988 = relay.var("var_3988", dtype = "int32", shape = ())#candidate|3988|()|var|int32
var_3989 = relay.var("var_3989", dtype = "int32", shape = (1, 6))#candidate|3989|(1, 6)|var|int32
bop_3990 = relay.add(var_3988.astype('int32'), var_3989.astype('int32')) # shape=(1, 6)
output = bop_3990
output2 = bop_3990
func_4006 = relay.Function([var_3988,var_3989,], output)
mod['func_4006'] = func_4006
mod = relay.transform.InferType()(mod)
mutated_mod['func_4006'] = func_4006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4006_call = mutated_mod.get_global_var('func_4006')
var_4008 = relay.var("var_4008", dtype = "int32", shape = ())#candidate|4008|()|var|int32
var_4009 = relay.var("var_4009", dtype = "int32", shape = (1, 6))#candidate|4009|(1, 6)|var|int32
call_4007 = func_4006_call(var_4008,var_4009,)
output = call_4007
func_4010 = relay.Function([var_4008,var_4009,], output)
mutated_mod['func_4010'] = func_4010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3321_call = mod.get_global_var('func_3321')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_4014 = func_3321_call()
call_4015 = func_3321_call()
output = relay.Tuple([call_4014,])
output2 = relay.Tuple([call_4015,])
func_4027 = relay.Function([], output)
mod['func_4027'] = func_4027
mod = relay.transform.InferType()(mod)
output = func_4027()
func_4028 = relay.Function([], output)
mutated_mod['func_4028'] = func_4028
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4054 = relay.var("var_4054", dtype = "float64", shape = (11, 8, 16))#candidate|4054|(11, 8, 16)|var|float64
var_4055 = relay.var("var_4055", dtype = "float64", shape = (11, 8, 16))#candidate|4055|(11, 8, 16)|var|float64
bop_4056 = relay.floor_mod(var_4054.astype('float64'), relay.reshape(var_4055.astype('float64'), relay.shape_of(var_4054))) # shape=(11, 8, 16)
func_654_call = mod.get_global_var('func_654')
func_656_call = mutated_mod.get_global_var('func_656')
call_4061 = relay.TupleGetItem(func_654_call(), 0)
call_4062 = relay.TupleGetItem(func_656_call(), 0)
func_402_call = mod.get_global_var('func_402')
func_403_call = mutated_mod.get_global_var('func_403')
call_4065 = relay.TupleGetItem(func_402_call(), 0)
call_4066 = relay.TupleGetItem(func_403_call(), 0)
output = relay.Tuple([bop_4056,call_4061,call_4065,])
output2 = relay.Tuple([bop_4056,call_4062,call_4066,])
func_4073 = relay.Function([var_4054,var_4055,], output)
mod['func_4073'] = func_4073
mod = relay.transform.InferType()(mod)
var_4074 = relay.var("var_4074", dtype = "float64", shape = (11, 8, 16))#candidate|4074|(11, 8, 16)|var|float64
var_4075 = relay.var("var_4075", dtype = "float64", shape = (11, 8, 16))#candidate|4075|(11, 8, 16)|var|float64
output = func_4073(var_4074,var_4075,)
func_4076 = relay.Function([var_4074,var_4075,], output)
mutated_mod['func_4076'] = func_4076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_4152 = relay.TupleGetItem(func_577_call(), 1)
call_4153 = relay.TupleGetItem(func_579_call(), 1)
output = relay.Tuple([call_4152,])
output2 = relay.Tuple([call_4153,])
func_4155 = relay.Function([], output)
mod['func_4155'] = func_4155
mod = relay.transform.InferType()(mod)
output = func_4155()
func_4156 = relay.Function([], output)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4173 = relay.const(5, dtype = "uint64")#candidate|4173|()|const|uint64
var_4174 = relay.var("var_4174", dtype = "uint64", shape = (3, 16, 4))#candidate|4174|(3, 16, 4)|var|uint64
bop_4175 = relay.maximum(const_4173.astype('uint64'), var_4174.astype('uint64')) # shape=(3, 16, 4)
func_707_call = mod.get_global_var('func_707')
func_708_call = mutated_mod.get_global_var('func_708')
call_4178 = relay.TupleGetItem(func_707_call(), 0)
call_4179 = relay.TupleGetItem(func_708_call(), 0)
uop_4184 = relay.sqrt(var_4174.astype('float32')) # shape=(3, 16, 4)
output = relay.Tuple([bop_4175,call_4178,uop_4184,])
output2 = relay.Tuple([bop_4175,call_4179,uop_4184,])
func_4186 = relay.Function([var_4174,], output)
mod['func_4186'] = func_4186
mod = relay.transform.InferType()(mod)
var_4187 = relay.var("var_4187", dtype = "uint64", shape = (3, 16, 4))#candidate|4187|(3, 16, 4)|var|uint64
output = func_4186(var_4187)
func_4188 = relay.Function([var_4187], output)
mutated_mod['func_4188'] = func_4188
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4220 = relay.var("var_4220", dtype = "uint8", shape = (8, 3, 2))#candidate|4220|(8, 3, 2)|var|uint8
const_4221 = relay.const([[[-4,3],[7,6],[-5,8]],[[6,9],[6,2],[-8,7]],[[-1,7],[-9,5],[3,-7]],[[9,10],[4,6],[-5,4]],[[5,-9],[4,-1],[6,2]],[[4,9],[7,-6],[7,2]],[[5,3],[-1,9],[3,-10]],[[-3,4],[8,-3],[3,-10]]], dtype = "uint8")#candidate|4221|(8, 3, 2)|const|uint8
bop_4222 = relay.right_shift(var_4220.astype('uint8'), relay.reshape(const_4221.astype('uint8'), relay.shape_of(var_4220))) # shape=(8, 3, 2)
output = bop_4222
output2 = bop_4222
func_4231 = relay.Function([var_4220,], output)
mod['func_4231'] = func_4231
mod = relay.transform.InferType()(mod)
mutated_mod['func_4231'] = func_4231
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4232 = relay.var("var_4232", dtype = "uint8", shape = (8, 3, 2))#candidate|4232|(8, 3, 2)|var|uint8
func_4231_call = mutated_mod.get_global_var('func_4231')
call_4233 = func_4231_call(var_4232)
output = call_4233
func_4234 = relay.Function([var_4232], output)
mutated_mod['func_4234'] = func_4234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4155_call = mod.get_global_var('func_4155')
func_4156_call = mutated_mod.get_global_var('func_4156')
call_4268 = relay.TupleGetItem(func_4155_call(), 0)
call_4269 = relay.TupleGetItem(func_4156_call(), 0)
output = relay.Tuple([call_4268,])
output2 = relay.Tuple([call_4269,])
func_4272 = relay.Function([], output)
mod['func_4272'] = func_4272
mod = relay.transform.InferType()(mod)
output = func_4272()
func_4273 = relay.Function([], output)
mutated_mod['func_4273'] = func_4273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4027_call = mod.get_global_var('func_4027')
func_4028_call = mutated_mod.get_global_var('func_4028')
call_4277 = relay.TupleGetItem(func_4027_call(), 0)
call_4278 = relay.TupleGetItem(func_4028_call(), 0)
func_2444_call = mod.get_global_var('func_2444')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_4289 = relay.TupleGetItem(func_2444_call(), 1)
call_4290 = relay.TupleGetItem(func_2446_call(), 1)
output = relay.Tuple([call_4277,call_4289,])
output2 = relay.Tuple([call_4278,call_4290,])
func_4300 = relay.Function([], output)
mod['func_4300'] = func_4300
mod = relay.transform.InferType()(mod)
mutated_mod['func_4300'] = func_4300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4300_call = mutated_mod.get_global_var('func_4300')
call_4301 = func_4300_call()
output = call_4301
func_4302 = relay.Function([], output)
mutated_mod['func_4302'] = func_4302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_4315 = func_2626_call()
call_4316 = func_2626_call()
func_985_call = mod.get_global_var('func_985')
func_989_call = mutated_mod.get_global_var('func_989')
const_4318 = relay.const([-10,1,9,-1,10,4,6,2,4,-2,-6,8,-9,-6,2,-10,-2,10,9,-4,5,2,9,-3,2,5,-6,-1,-8,5,-4,-2,-8,-8,6,-7,2,-4,5,-4,-3,-4,-10,3,-4,9,5,-4,6,1,-4,2,-10,-4,4,-2,7,-5,3,-6,-8,6,-8,10,10,5,2,7,6,6,1,6,-6,-4,10,-9,-9,-4,3,1,5,-7,-5,-10,-8,-10,6,9,-8,-4,-5,7,-6,-10,-4,2,9,8,-4,3,-7,-2,-9,-5,-4,-5,10,4,2,-6,-7,8,8,9,6,-5,-7,4,-10,4], dtype = "uint64")#candidate|4318|(120,)|const|uint64
call_4317 = relay.TupleGetItem(func_985_call(relay.reshape(const_4318.astype('uint64'), [4, 6, 5]), relay.reshape(call_4315.astype('float64'), [364,]), ), 4)
call_4319 = relay.TupleGetItem(func_989_call(relay.reshape(const_4318.astype('uint64'), [4, 6, 5]), relay.reshape(call_4315.astype('float64'), [364,]), ), 4)
func_1659_call = mod.get_global_var('func_1659')
func_1661_call = mutated_mod.get_global_var('func_1661')
const_4321 = relay.const([-7.590110,4.123148,3.840011,-4.598513,-4.813888,8.368594,2.229302,9.156028,7.577521,-0.304339,2.365275,-1.017830,-9.292463,8.172008,-6.540271,-2.926280,-8.246524,-4.502814,0.564682,8.408140,-7.317417,-8.022182,-5.619055,-7.696251,-5.597056,5.143603,-0.976497,8.496965,-0.831373,-1.265531,7.561881,-6.299200,-3.882606,-5.104395,8.008540,3.495569,-1.951925,7.119685,1.404731,8.929307,-8.017676,-5.282238,-1.894972,9.299979,-8.573264,3.700878,-7.863903,2.155904,7.220869,-0.546936,-1.208021,-4.951295,-7.460217,7.359877,1.254423,8.750282,9.615090,-3.968067,-9.358275,9.353770,-0.220831,-8.006006,-6.072611,5.799057,8.564886,-3.385017,-2.083486,1.380768,-8.415402,-2.429834,3.870510,7.774142,5.191841,-9.014881,4.184822,-7.788643,-8.444153,-1.747172,0.523714,-8.309929,0.300206,-0.316281,-7.275301,-6.946914,-4.015280,-0.647376,5.616126,3.653541,-9.642207,-5.998462,8.598556,6.724812,4.272062,-8.587284,9.659389,-2.682055,3.912309,-6.498147,-1.643941,-1.143069,-9.027526,-3.437786,-8.888906,-5.256548,8.835936,-8.624455,-1.301245,-5.523461,2.794557,-3.708506,-5.702679,3.169358,3.976767,3.693326,0.644038,-0.702494,-2.305992,9.163553,-1.696098,9.356733,-7.310422,-5.895335,4.064702,-5.659978,0.880987,-5.590820,2.172752,8.940735,3.557273,-8.289610,-8.471786,-4.780441,7.493791,2.019379,-4.066169,3.721723,-4.815741,3.706448,1.540792,-1.405837,-5.431008,-9.238206,9.755982,-0.516090,-5.293534,6.673175,9.478249,3.210410,7.814799,2.721775,-6.203813,-5.321299,-1.459158,-4.607823,7.569714,4.147699,8.607640,-8.068498,0.493806,-2.620151,2.032025,4.166352,9.441585,-3.493941,8.353122,-7.702615,-3.414151,9.247951,-2.431554,-2.176008,-5.212722,0.091651,6.308271,-8.587111,-7.249322,-1.145951,-4.542769,8.978436,9.570633,-8.825797,5.602822,-4.429877,1.983492,-1.829761,2.488902,-7.752058,-9.749392,-0.685905,7.142094,9.743790,7.926363,2.862519,6.118678,4.278290,-0.398118,5.453165,5.871510,-0.494715,4.070032,-6.351427,8.042478,7.836879,8.683111,-8.444813,-6.137116,-4.789232,0.758199,-3.466112,-6.914833,7.713888,2.929163,-6.484727,-6.133019,-9.013618,-9.766961,3.388948,3.576512,3.282258,-2.505988,2.291146,1.235976,-1.850970,5.594250,3.546292,-8.155318,2.790648,-0.020820,-4.867591,-5.000918,-8.484219,-7.997882,-0.854625,-2.969797,-1.684931,3.985631,-5.481958,9.651696,-6.015143,8.377237,7.968681,-4.150764,3.189614,-7.883968,-1.513579,-5.873602,6.377320,-4.304490,-9.883679,-3.166342,8.171157,-9.101644,-0.134762,-0.743370,2.889165,9.272626,9.232475,0.715021,-5.868861,7.777259,-8.169279,7.969136,-6.345916,3.635090,1.101724,0.728742,-5.082392,-9.167033,9.487997,5.545963,-6.397614,5.271053,-7.854376,-1.801494,2.465843,6.168311,-8.314864,6.634809,-1.825038,5.202941,-4.812476,-8.747483,5.940602,-0.881007,5.939906,9.216786,-9.378633,-7.164258,3.513384,6.630552,-8.421539,-5.361459,4.062699,4.789680,-7.871702,6.347926,9.492298,0.753271,-4.004024,7.056709,3.630697,7.337636,-7.463238,6.043905,8.063726,-1.755979,8.558395,-2.996829,-3.569962,2.904052,-8.779689,-8.057352,-9.397457,-1.149134,8.364293,0.403303,-8.097627,-1.127236,-7.481317,-1.331608,-5.596308,9.930404,8.798976,-8.552445,6.197165,2.547753,5.696703,6.029472,1.936762,-6.613186,2.873181,-1.230693,7.248299,-8.057658,-8.210175,7.338117,1.942595,-5.523098,-2.702455,0.710891,-0.841752,1.249707,-2.496776,-0.830236,7.596146,-0.615099,-4.820245,-1.507122,9.195588,1.105401,-7.803772,-4.913023,0.721529,-7.733112,2.194482,4.434811,-7.294423,4.898132,7.879553,1.985586,3.753609,5.623678,-3.286548,3.479946,8.235355,4.414631,0.573163,3.928875,-5.996198,-9.990984,4.203095,-4.895681,-2.224863,-9.597081,9.945726,-8.899286,2.649827,-7.013661,-4.049898,7.650915,-1.511227,9.548098,-5.347059,-3.142599,-6.438268,5.731138,-5.474136,-4.297880,5.586496,-7.518644,-7.141261,0.636833,-8.075278,9.020771,6.531534,-0.875152,4.703343,5.842329,7.950565,-3.175819,-7.414396,7.112791,2.643648,-6.638890,1.061819,8.068416,9.589608,7.796932,-9.213950,-8.172257,-0.226342,6.890921,-9.613557,3.307603,-7.380382,-9.435646,4.734879,5.422615,1.519362,-6.894796,-4.749471,-7.732068,-8.996826,-9.421299,-8.777005,1.962521,0.731133,-3.699764,5.552024,6.989415,0.161321,1.432417,-9.809719,-4.917678,-8.527559,-2.386177,-0.132450,-6.695533,-4.245780,-9.778690,-0.880053,3.881235,-5.594452,4.249717,-5.517083,-6.863610,-9.748857,-9.986252,-2.334093,-7.949186,1.551883,-3.717593,6.616404,5.544250,4.717523,-9.042881,7.390224,6.094159,6.329068,4.992963,-6.084344,-5.154030,5.964199,0.279297,7.572329,-1.212671,-6.542362,-3.500022,-5.534312,4.797554,0.820498,7.116337,-8.807224,5.536277,3.143855,7.624051,-8.101550,8.146188,-7.827399,0.064141,-2.515906,1.144324,-9.999308,3.030221,7.421516,-4.209715,-3.552297,9.466289,4.134428,4.411635,5.005349,-0.462290,-8.925938,-4.153085,-3.291045,-4.972089,2.322059,4.001786,3.995083,-0.494591,5.789867,-3.128180,-1.964733,-2.871628,-8.666991,4.103040,-2.113978,0.076170,9.116312,-8.443388,4.943558,-5.453877,-6.000688], dtype = "float64")#candidate|4321|(512,)|const|float64
call_4320 = relay.TupleGetItem(func_1659_call(relay.reshape(const_4321.astype('float64'), [8, 16, 4])), 1)
call_4322 = relay.TupleGetItem(func_1661_call(relay.reshape(const_4321.astype('float64'), [8, 16, 4])), 1)
func_1528_call = mod.get_global_var('func_1528')
func_1531_call = mutated_mod.get_global_var('func_1531')
var_4333 = relay.var("var_4333", dtype = "float64", shape = (1092,))#candidate|4333|(1092,)|var|float64
call_4332 = relay.TupleGetItem(func_1528_call(relay.reshape(var_4333.astype('float64'), [3, 364])), 1)
call_4334 = relay.TupleGetItem(func_1531_call(relay.reshape(var_4333.astype('float64'), [3, 364])), 1)
output = relay.Tuple([call_4315,call_4317,const_4318,call_4320,const_4321,call_4332,var_4333,])
output2 = relay.Tuple([call_4316,call_4319,const_4318,call_4322,const_4321,call_4334,var_4333,])
func_4340 = relay.Function([var_4333,], output)
mod['func_4340'] = func_4340
mod = relay.transform.InferType()(mod)
mutated_mod['func_4340'] = func_4340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4341 = relay.var("var_4341", dtype = "float64", shape = (1092,))#candidate|4341|(1092,)|var|float64
func_4340_call = mutated_mod.get_global_var('func_4340')
call_4342 = func_4340_call(var_4341)
output = call_4342
func_4343 = relay.Function([var_4341], output)
mutated_mod['func_4343'] = func_4343
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4429 = relay.const([[[-9.971927,9.013684,4.067107,-5.977406,-8.628439,0.507980,-4.808973,0.016356,6.306975],[1.000471,6.966554,6.994867,7.036048,9.588091,-8.307950,4.083929,9.809847,0.186311],[-1.289477,-6.154828,-8.841815,-3.198053,-6.914902,-0.634460,1.222149,-4.821658,5.462806],[4.315244,-2.049772,-7.458792,5.187079,9.364050,-8.460032,4.966785,-9.135999,8.283609],[3.804397,-9.060776,-2.173862,-8.010118,-3.810302,-3.936841,-9.886423,-6.827149,-6.372470],[8.927539,-4.805649,2.461502,3.156690,-4.069646,-4.955262,-7.217399,6.036612,-2.995912],[2.735956,9.942121,7.267162,-7.678687,4.124109,2.471799,1.176458,-8.636544,6.715658],[-9.705390,-7.413870,0.063075,9.439704,9.409116,-2.524857,-7.154011,-6.040759,1.494351],[9.958110,1.123752,-3.877400,-1.534219,3.663035,-2.810919,-0.237195,8.810108,2.565004],[-7.430362,-6.485562,8.271847,2.059876,0.603419,3.349365,3.531460,-5.636813,2.571342],[9.981533,-3.953983,-0.975965,-2.660933,2.584753,-0.449104,-3.367779,3.590771,-2.775958],[6.143256,-3.382360,8.348679,1.391451,-0.362415,9.524905,-9.109198,-2.314456,2.205703],[5.396261,4.077326,5.814296,0.949485,-4.217440,-3.788513,5.853223,-0.646154,-8.822322]],[[1.638155,6.882354,0.646060,-3.445753,0.871777,-8.230296,7.077159,-8.032870,7.622956],[-1.630956,1.107482,9.234532,5.231003,5.591104,0.610970,9.013170,3.078807,-2.294360],[1.618222,8.800118,6.431302,5.709704,0.919817,-7.979004,1.653025,-7.143823,6.747788],[3.430835,-1.402117,9.325162,-9.347305,2.875359,5.459433,0.223926,-3.574608,8.513157],[-3.406736,-8.579286,8.483204,-7.399925,-9.384298,2.108032,1.449812,-0.619679,-2.455275],[4.463383,9.605367,-0.115748,-7.539966,1.170744,-8.422661,5.892388,-4.613869,1.824805],[-9.172453,-5.648892,-6.685032,-1.831978,-7.110763,8.518197,-8.016580,-9.782742,9.993626],[-8.642151,-0.066173,-5.480617,6.155437,8.334593,-2.880641,2.705951,6.568712,9.324927],[0.066342,0.347705,-5.042148,-2.184123,3.169249,-7.703733,-1.494027,-5.675097,2.607230],[7.044064,-5.557556,-2.795141,8.976766,9.834750,2.755591,-9.844279,8.607141,1.804558],[8.076597,-8.198153,-2.329985,2.990890,-9.455337,4.760810,9.764762,-0.213999,4.693047],[-7.251642,-9.563287,4.142688,-2.061559,-9.213236,5.372478,9.863968,-8.479568,5.367769],[1.729454,2.712107,8.516877,8.331520,7.838155,-2.573553,-6.737004,-6.917487,5.633439]],[[-0.889335,6.216977,9.712196,-5.812672,4.046957,-5.978567,2.933713,-2.723753,5.335251],[5.643371,-0.265912,-0.054489,-9.579168,0.803195,1.622358,-0.869404,-8.207179,3.287061],[5.429438,-8.313479,-8.411901,1.110452,-8.122698,-6.233023,6.334887,-4.850467,-8.753910],[3.188966,2.118496,1.065108,2.670833,7.796101,-4.116657,3.729046,-9.097656,-4.044465],[-5.702639,7.315292,8.830325,6.247890,4.025558,-3.792256,-6.738260,-3.570202,-7.469878],[6.017719,-8.737907,7.063045,5.539776,-4.653172,9.933180,-2.813558,-8.248035,-5.738147],[1.809649,2.573821,-4.972847,-9.120134,8.150657,-5.828828,8.271770,7.395940,-6.013324],[-4.422214,9.679962,-1.032983,3.242892,-2.657722,-0.611418,-3.755388,-6.025163,-3.138070],[1.254920,-3.840346,-0.538037,8.031883,-9.222193,0.186233,1.094354,-6.839794,-6.472001],[0.856278,2.642601,7.855177,9.752614,3.633594,5.809383,-0.601819,-2.609695,6.530259],[2.893701,-1.464333,5.976688,0.181829,0.630640,6.106429,-2.983678,-3.053473,8.320407],[1.860332,2.763722,-4.094458,-0.727290,1.644128,7.882495,8.633330,6.155943,-1.196764],[6.956895,-5.771024,3.559919,-7.624410,-3.699162,5.898671,8.498487,-7.144051,7.240281]],[[4.919556,4.386086,0.647398,-1.690096,-1.819493,-5.298546,-1.754449,-1.980569,6.148634],[5.647025,1.839427,-2.370724,9.761034,3.345334,-0.546044,-4.369090,-9.296719,-9.319624],[8.951999,0.293759,6.168336,-9.067726,3.128374,-2.105369,4.461177,9.752522,5.403308],[6.803514,7.302149,7.301428,-2.599114,7.555231,0.577642,-6.549238,-5.579787,-1.545918],[6.373995,-2.988111,5.902725,2.668322,-6.991069,7.318645,-8.135336,-3.428496,8.707617],[6.889378,4.763685,7.001282,8.186697,0.139521,8.722485,8.297153,5.673499,7.001317],[-5.990548,8.821789,4.042113,-3.713823,2.974763,2.547183,-9.454417,-4.795023,-2.174925],[7.381164,8.776152,8.665839,-4.442985,-4.575835,-7.644693,3.983256,-6.481597,2.007749],[2.869727,-5.368817,-3.790437,-6.558209,-7.735846,2.151839,-6.740060,-6.792849,8.649812],[-1.120910,-8.649685,6.020363,-3.462582,7.864237,1.878175,6.697819,0.720344,-3.663442],[0.676993,-4.421862,5.444945,-3.845406,-7.360127,-9.598961,0.041439,-1.258254,5.076945],[-8.647067,-8.124062,-4.979725,9.325522,-9.154664,7.688910,-9.726829,4.158402,8.641577],[-6.559420,-6.571957,-0.215913,1.564389,8.176330,-8.749822,9.654735,0.737704,-5.138842]],[[-3.376433,2.634086,-3.001159,9.043994,3.029739,-7.638745,6.343112,2.520167,4.604550],[-1.597886,2.821443,-2.160125,-9.411319,-2.614139,4.523500,-0.685804,-4.938532,9.359053],[-1.488686,-7.211861,0.568746,-9.080458,5.202872,8.854681,-2.115674,0.829158,1.357116],[1.166654,-1.343027,1.889685,-0.153695,0.098785,0.082047,-0.207011,6.637603,-9.234559],[2.968596,2.200590,-9.320019,5.773942,7.187680,-6.158863,7.888217,-3.042631,0.704269],[8.960497,2.478087,9.469752,7.456916,5.144716,-9.863666,-7.677643,-5.329539,-0.488449],[-7.307644,5.141759,3.689822,-0.299437,3.227662,-3.631449,8.137530,6.793000,-1.097919],[2.077728,-0.791445,-2.994304,-1.292637,-0.550902,-8.821761,8.005927,-7.726361,-0.098004],[-9.801785,-9.488881,-3.131004,9.667239,5.867088,-4.292596,8.862157,7.378674,-0.628308],[-2.150958,-5.709192,-2.183169,6.854965,1.394974,-6.453102,6.262340,7.708651,9.943908],[-7.529186,3.938280,3.002761,8.664035,6.491791,-0.598634,-9.467267,3.409632,9.120532],[-3.503649,7.322842,-9.124051,7.583542,2.117438,-2.914083,-5.759617,1.703632,-6.691966],[-8.031999,0.843456,-4.158298,9.315981,-4.809321,-0.839770,-2.008327,-2.242697,-5.995170]],[[-7.786061,6.938279,-6.898357,-7.044976,-5.468498,-0.672711,-2.682540,4.849810,7.983567],[6.132349,-2.688253,9.026654,6.339459,6.839272,8.186643,-9.970110,-7.267378,9.294493],[6.730464,9.459939,3.849191,-2.852591,-8.757356,3.161245,-6.676573,4.774865,-3.175051],[6.552211,-1.136307,-0.119439,-0.402589,4.582912,-8.819874,-2.563388,-5.952940,1.503942],[5.720862,6.865318,2.805211,7.818718,0.763513,1.542901,9.219286,4.668309,8.833054],[-1.062083,2.179457,-4.877781,-5.123994,6.800757,9.734920,6.410432,9.987570,-7.726738],[9.981402,-4.203257,-1.534602,7.579128,-5.211277,-3.724226,-1.160033,7.773047,-7.933634],[0.102694,-5.555312,-5.648802,5.308396,6.225902,-1.175839,-6.292110,1.741321,9.450789],[-3.902912,-7.651970,0.086244,-1.772268,6.597818,0.642207,-9.736513,-5.451733,-9.933321],[-0.681011,-7.952378,-4.953373,4.241735,1.639975,5.467575,5.144123,0.964575,-5.931213],[-5.290891,-8.257164,-9.975414,3.436881,-9.401350,-8.988729,-4.617974,-5.262754,-6.577422],[-0.638508,0.425581,-9.667484,-8.235952,-7.235380,4.582654,-5.452539,-8.198651,2.059860],[1.313499,5.850194,0.168022,-6.791780,-1.065838,-1.354802,5.755581,-2.851914,-2.730086]],[[4.631955,-6.733023,-4.612687,-5.521129,1.403423,3.393262,0.576680,-8.169915,-3.826514],[-5.727211,5.985983,-6.916129,4.234512,-5.929803,-2.128914,2.388865,5.078940,-9.456005],[9.210890,8.134848,1.386533,-0.481059,9.646081,1.829306,-2.055388,-3.955617,-2.071251],[8.887745,-1.412864,0.017911,3.752182,-1.010708,5.032646,-2.598243,9.342410,8.972469],[7.992976,9.725853,-5.892355,-3.558709,8.626394,1.556113,8.008337,7.634388,-8.970132],[4.889855,0.538392,3.616748,-0.676509,-9.592137,2.097974,-3.972795,2.942635,7.767675],[-6.719147,-4.406024,-2.689812,9.099432,-0.196909,3.731645,5.268147,-2.847685,-7.958072],[5.623834,-2.562545,-6.998775,-9.473305,-6.989222,-7.290773,2.693895,7.189603,-5.723529],[5.009264,-8.796894,6.841898,6.442108,-5.191514,9.127315,9.635912,3.687973,-6.745654],[5.389038,-0.463684,-5.153613,9.275855,7.517029,6.596630,-9.049816,7.381375,2.982493],[-6.492134,3.084234,-6.250792,1.230195,-7.395633,0.454360,-1.677782,6.699529,-0.870253],[4.924180,4.791039,7.683507,5.423920,-0.283155,-8.036597,2.760983,-1.118062,0.378988],[7.766150,-1.624991,8.362534,0.456657,-9.498541,-1.833616,-1.834185,-4.694099,-3.594628]],[[6.306479,8.951210,-2.386787,9.581274,-4.244861,-6.641195,-2.118727,-9.496984,9.396384],[7.387498,3.276133,6.233072,-8.605217,9.883590,-9.341052,-8.567302,3.454397,2.134624],[3.261094,3.175726,-8.405214,4.763450,-9.370273,1.081409,8.320165,-0.111993,-1.907220],[-2.738495,0.515321,7.518783,1.666272,4.106246,1.542148,-3.187775,0.586830,-4.320480],[-8.225808,5.504675,1.882675,-7.145351,9.022231,4.791492,9.431933,-7.994068,0.081994],[-6.926250,-4.944861,-6.127794,-7.319843,-5.143668,-6.403646,8.265317,1.255351,1.715107],[9.758461,5.697409,-2.852217,-7.942152,5.714233,7.100827,-3.335489,2.435463,1.851769],[-9.378443,1.491201,-4.431639,5.679287,-2.732313,-8.468797,7.956112,5.362629,-8.738407],[6.875869,0.325109,9.226220,3.969119,-1.036047,-4.992883,-3.784110,6.420732,-3.567787],[-2.154128,7.264289,-3.975913,-6.924325,0.926088,-3.241594,-1.983748,-0.022463,-1.596293],[-7.542111,2.215801,8.058678,-3.891053,-3.751140,3.201290,6.627567,-5.039198,-0.647810],[-1.014732,-7.653802,-1.621945,7.936230,-4.299374,3.172098,-2.297450,8.094274,-6.666832],[1.678755,-9.601166,9.216693,-5.317261,3.814229,1.646624,3.291237,4.033993,-1.446656]],[[7.379843,-1.283908,4.707085,-1.800559,1.442198,-4.532077,-0.023870,-3.263531,9.104827],[-0.334174,9.279784,7.280667,1.297336,-8.063471,-4.945768,0.390732,0.342744,-8.414503],[8.651219,-8.902010,-7.531147,-3.956520,-1.211630,0.609192,-1.066728,-7.057933,-4.158968],[4.418958,-7.314080,-2.043743,-7.410853,-4.534935,2.295782,-4.842588,-9.573522,3.525714],[1.504575,8.500265,-1.415041,-4.528130,1.414557,-9.637156,-5.282273,5.856367,-0.817753],[4.073737,8.345186,-9.469528,-7.051536,4.660971,3.015309,9.099222,0.685229,-7.417072],[-5.728259,-5.414464,9.772515,9.220023,-5.209151,5.420195,-7.130207,4.894723,-5.466745],[-5.152224,4.248913,0.660775,-8.771806,2.169711,-4.886945,1.454335,-7.407884,-0.188789],[2.601204,3.345382,-1.419297,-6.725912,-7.393074,3.553295,8.763954,3.678981,8.717120],[6.603302,-0.652925,6.461298,-7.826151,5.730363,6.826838,8.344992,5.798469,-7.239900],[6.940203,-2.581023,4.839587,-3.387697,7.279843,6.281505,9.569976,-8.567939,1.639762],[-7.175323,-9.931735,5.506990,9.575011,-6.399593,3.649848,-9.743717,8.950737,-0.170933],[-0.378733,6.108396,0.149822,0.704430,4.572441,-7.625282,7.348764,8.312613,-2.737099]],[[3.178057,5.313678,-2.405769,6.218690,3.980014,0.259182,2.410627,-3.102938,6.957079],[6.337280,-8.750104,-7.225559,6.212909,5.028994,2.499569,8.728961,7.600401,9.367127],[-1.250186,0.213674,5.600408,9.446161,-8.895175,-1.076001,5.382127,-2.020913,-3.012759],[-9.629818,5.187180,-8.039788,6.809346,8.193771,-9.734423,-0.861397,8.753517,-7.493659],[-9.402717,5.856309,-0.975430,-2.914020,7.789931,5.577949,4.745729,-8.209608,-1.644229],[-8.192631,-0.178031,-7.721775,-2.510779,8.154184,-7.906797,-1.691272,-9.545343,-5.129693],[2.022986,-7.634118,1.159355,7.664676,-3.587935,5.964247,-3.550173,-8.884998,-1.836061],[-4.294759,-5.884587,-8.692753,1.281116,3.890925,4.960106,-7.170148,9.733855,5.483777],[6.033407,1.209866,-5.585437,-6.300449,-7.283666,-0.566340,7.350644,1.612350,-3.485413],[0.489050,0.059370,5.910217,-5.054011,8.009477,5.915444,-9.890195,7.548734,-5.086492],[4.315146,8.459606,9.621359,-8.126873,-9.229447,-5.076247,8.430067,-8.275472,2.014997],[2.052599,-6.914521,4.618075,-8.629606,-5.018700,6.417632,0.951422,4.547509,4.299481],[-8.684178,6.868901,0.123501,-4.759805,8.313247,7.838407,-9.566822,-2.610703,-2.575243]],[[-5.724469,-5.188598,-8.350572,6.272068,-5.375730,-3.834455,-3.064921,2.085711,0.757324],[8.528871,5.081728,5.071716,9.234345,-6.052845,-9.136800,9.876741,1.999425,6.851133],[-7.882454,2.936608,9.830314,-0.052551,6.758454,7.159039,-7.642478,-4.928176,-4.498333],[3.996276,7.198850,9.775325,-4.301240,1.517671,-4.128088,3.843200,9.833479,0.634020],[4.121223,-1.363010,6.930294,4.073859,8.630337,-9.970817,3.040456,5.214727,9.594312],[-2.747575,-6.470459,2.205199,-4.412212,9.492457,8.360195,-8.178871,-4.249285,9.761541],[6.269582,6.425943,-1.502653,-1.430711,9.581454,7.275900,-2.884285,-4.721895,9.000275],[-3.632583,0.981375,6.894039,-8.887841,7.839747,0.981031,1.542749,6.031005,2.080171],[-8.278876,-5.888277,1.620268,-3.656025,7.736487,-2.188680,-6.355055,7.495524,-4.103787],[-9.055730,-9.025630,6.212316,0.341291,-4.934318,-6.983314,-7.084864,8.476577,-5.146323],[-0.946629,5.771635,-4.833101,-9.064183,-7.291757,-4.432626,7.826264,7.450723,-9.256987],[2.014358,7.471098,-6.379995,7.461700,-0.815416,5.858543,2.980287,5.033969,-6.381333],[0.042274,-9.663448,-5.988999,-1.492731,-2.729485,6.657290,1.040145,-3.207772,1.130076]],[[-2.775714,7.596668,4.292497,4.556098,7.628530,1.573716,-2.390360,-1.954681,-3.409344],[7.733157,-7.763654,0.458322,-1.828390,-3.342503,1.973839,-8.582127,-4.248890,2.400057],[-6.041776,5.206509,7.692706,5.441521,9.958050,1.703313,-2.408930,-3.940904,-2.736463],[2.899170,-4.480542,9.826563,9.160088,6.102963,2.677072,1.795634,-8.308053,4.896203],[-6.915520,2.527313,2.596604,3.904101,-2.254582,-0.819988,8.294346,1.257268,-9.814535],[-8.782362,-1.934419,9.145832,-3.378434,-8.177928,1.614689,-7.240672,-4.752019,2.596142],[-7.324162,-8.889105,9.493079,7.987780,-6.124882,-9.383574,9.269834,-4.554476,6.389686],[-7.301454,-3.442827,-1.678022,-3.763113,3.278059,-2.851435,-3.581159,-1.440991,5.303182],[-8.280300,-1.565862,-9.502245,4.930239,5.059790,5.133153,0.591379,-7.654044,-1.844828],[-5.920523,-1.336288,-6.933631,-6.927078,9.811473,5.184666,-3.003705,-3.801371,-6.849724],[-7.381864,-8.577847,6.827047,-7.207217,0.377082,-4.479882,1.391563,6.533774,3.339821],[-7.491345,-5.540814,-0.433823,8.504263,8.752237,0.500145,-0.903120,6.400003,-8.641727],[-3.948807,-2.729171,3.217351,-3.982277,2.084424,-4.231572,3.221369,-2.967385,5.426013]],[[0.977862,-7.650274,-6.116595,-5.790187,6.028396,4.269910,-9.314223,-0.609015,-8.444529],[0.950300,-0.173535,-5.963260,1.783029,3.356792,7.656167,-7.791690,6.775180,-7.877202],[5.190908,-7.446594,-6.990049,-7.635094,-1.249994,0.870209,-1.261165,0.893686,0.911505],[-0.232688,5.282907,5.003499,-7.195803,2.210103,-7.849125,3.837399,-7.480033,-5.678017],[8.044412,9.139003,8.546418,-1.884010,0.101799,-2.488886,1.549628,-5.858681,-1.556169],[-4.621402,1.146168,9.395831,4.408217,6.111003,-8.428183,-5.202041,-7.144807,0.824540],[6.035439,-2.289662,9.662203,2.736660,9.995421,9.296337,5.475319,-8.409537,4.922041],[-1.598531,-9.020187,-3.635280,5.782854,-1.693256,-4.857717,1.715612,-3.105987,1.095507],[-1.206842,-1.261253,-1.411831,-6.902133,9.792313,-5.786033,-4.009709,0.905350,0.977417],[5.643809,8.162287,-5.252877,-9.953611,8.423892,9.205376,-3.716587,6.500577,0.573964],[5.133589,-9.007677,-4.118946,5.672210,0.297103,0.835228,1.161999,-0.320947,3.757830],[-0.092881,-6.873162,-3.255429,-2.205240,-5.107615,2.085993,9.259110,3.760510,-3.895532],[2.441100,-9.651808,-0.749120,0.284608,-9.360661,-9.299428,-9.713378,2.690507,-8.793342]],[[5.204465,5.244450,2.822801,2.545449,2.215264,-5.661509,9.275979,6.987311,-9.781977],[3.780287,7.070227,1.128068,6.696295,8.147346,9.125355,-8.620622,-7.494540,-5.369307],[5.824237,1.554969,-7.217533,-6.953743,5.695729,8.935901,7.142183,8.178449,-1.496793],[9.270847,-3.826140,9.803238,-0.861594,-5.038205,6.500013,-8.882772,3.391866,1.855004],[2.372569,7.150943,7.144838,4.971770,9.068684,-2.478090,5.814503,-3.613949,-3.698183],[0.683541,7.348302,5.127053,-4.022844,8.314314,2.655444,3.685582,-3.034285,6.726998],[0.673643,5.172204,9.151403,0.021730,8.603327,2.601316,5.717878,-1.654229,-9.644548],[1.953137,-4.716279,-1.328031,5.348976,-2.744501,-2.200164,3.263353,-7.404523,7.543879],[-6.067249,0.275279,-6.032790,9.717411,2.120843,-9.786471,-3.143216,7.249492,2.187611],[-4.945400,8.260398,-2.875205,0.192677,-2.702046,-9.393336,8.323698,-6.999724,-1.179550],[7.897297,-4.473564,-3.021788,7.096028,-0.882440,2.910860,-3.387991,-3.004143,-6.656343],[-4.441289,-6.813972,-4.680135,-1.912898,-2.695210,-8.987137,0.189425,-8.553574,-2.021559],[-3.776527,6.713054,-7.584624,-7.013782,6.206946,7.526373,-2.815812,4.571651,-5.331999]],[[0.274153,4.909083,4.666291,8.749856,-0.930705,-3.777858,-9.876717,-3.214185,4.224160],[-5.564876,4.942927,-6.322145,2.222502,-8.126172,3.551419,-2.391975,3.727572,-6.891286],[6.980971,8.659687,-0.591538,1.647683,4.636307,-4.860643,-5.286891,-9.074563,-0.472836],[-4.712812,6.902345,-3.500513,6.434311,-4.496920,5.878308,0.824646,-3.102019,-0.430705],[-2.913727,9.791073,2.844303,-7.124942,-4.819787,4.104089,2.888734,-9.162103,5.171104],[-7.253219,-5.838431,9.116077,9.773513,-0.814357,-1.910226,-7.091429,-1.817608,-4.223232],[-0.812031,-5.165788,9.349390,6.513058,2.400287,-2.816996,7.333951,-6.811084,6.266781],[8.483463,-6.541966,-9.761954,-3.111974,-6.679093,-5.542173,-6.992684,0.974998,4.509913],[-6.377149,-9.879237,-8.403294,-7.453536,1.042972,6.480683,6.425512,1.170326,9.705780],[-1.537507,8.819130,-4.106953,0.533101,-4.886171,8.115091,8.392725,-1.996876,-0.597455],[-6.911115,-8.948703,6.477514,-0.806551,-3.669028,-6.502055,5.122758,7.249237,7.988191],[-8.902057,-2.386175,-9.422802,-9.690821,-1.720947,3.401840,-8.799020,2.040976,5.606187],[-1.496896,7.384077,4.692457,-7.263998,-7.947110,2.221566,-2.155561,-0.869446,-5.131611]]], dtype = "float64")#candidate|4429|(15, 13, 9)|const|float64
var_4430 = relay.var("var_4430", dtype = "float64", shape = (15, 13, 9))#candidate|4430|(15, 13, 9)|var|float64
bop_4431 = relay.equal(const_4429.astype('bool'), relay.reshape(var_4430.astype('bool'), relay.shape_of(const_4429))) # shape=(15, 13, 9)
func_1659_call = mod.get_global_var('func_1659')
func_1661_call = mutated_mod.get_global_var('func_1661')
var_4447 = relay.var("var_4447", dtype = "float64", shape = (32, 16))#candidate|4447|(32, 16)|var|float64
call_4446 = relay.TupleGetItem(func_1659_call(relay.reshape(var_4447.astype('float64'), [8, 16, 4])), 1)
call_4448 = relay.TupleGetItem(func_1661_call(relay.reshape(var_4447.astype('float64'), [8, 16, 4])), 1)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_4449 = func_2626_call()
call_4450 = func_2626_call()
func_2086_call = mod.get_global_var('func_2086')
func_2088_call = mutated_mod.get_global_var('func_2088')
call_4467 = relay.TupleGetItem(func_2086_call(), 0)
call_4468 = relay.TupleGetItem(func_2088_call(), 0)
output = relay.Tuple([bop_4431,call_4446,var_4447,call_4449,call_4467,])
output2 = relay.Tuple([bop_4431,call_4448,var_4447,call_4450,call_4468,])
func_4470 = relay.Function([var_4430,var_4447,], output)
mod['func_4470'] = func_4470
mod = relay.transform.InferType()(mod)
var_4471 = relay.var("var_4471", dtype = "float64", shape = (15, 13, 9))#candidate|4471|(15, 13, 9)|var|float64
var_4472 = relay.var("var_4472", dtype = "float64", shape = (32, 16))#candidate|4472|(32, 16)|var|float64
output = func_4470(var_4471,var_4472,)
func_4473 = relay.Function([var_4471,var_4472,], output)
mutated_mod['func_4473'] = func_4473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4027_call = mod.get_global_var('func_4027')
func_4028_call = mutated_mod.get_global_var('func_4028')
call_4488 = relay.TupleGetItem(func_4027_call(), 0)
call_4489 = relay.TupleGetItem(func_4028_call(), 0)
output = call_4488
output2 = call_4489
func_4491 = relay.Function([], output)
mod['func_4491'] = func_4491
mod = relay.transform.InferType()(mod)
mutated_mod['func_4491'] = func_4491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4491_call = mutated_mod.get_global_var('func_4491')
call_4492 = func_4491_call()
output = call_4492
func_4493 = relay.Function([], output)
mutated_mod['func_4493'] = func_4493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_4504 = relay.TupleGetItem(func_2980_call(), 1)
call_4505 = relay.TupleGetItem(func_2982_call(), 1)
output = relay.Tuple([call_4504,])
output2 = relay.Tuple([call_4505,])
func_4540 = relay.Function([], output)
mod['func_4540'] = func_4540
mod = relay.transform.InferType()(mod)
mutated_mod['func_4540'] = func_4540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4540_call = mutated_mod.get_global_var('func_4540')
call_4541 = func_4540_call()
output = call_4541
func_4542 = relay.Function([], output)
mutated_mod['func_4542'] = func_4542
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4543 = relay.var("var_4543", dtype = "float64", shape = (6, 14, 8))#candidate|4543|(6, 14, 8)|var|float64
const_4544 = relay.const([[[0.291956,9.048694,-6.417334,-3.443499,-2.929675,-8.193192,-8.128965,7.959238],[-7.314177,-8.891644,6.446181,-3.708761,-5.293334,-4.817780,-0.527371,5.824018],[0.711230,-6.160555,-9.336105,9.972434,-8.320952,4.369177,0.999585,-7.958533],[8.024411,-5.594771,-2.331640,-7.325915,-1.024865,8.345716,-0.506010,-3.224051],[4.644398,-9.370476,7.330520,-8.684675,1.562525,-6.954408,-5.442921,-0.638543],[-5.684289,-0.476179,1.241214,9.328809,6.435192,-1.526120,5.187197,5.962677],[-3.410423,-2.573792,9.690457,7.438763,-3.911861,6.635593,-8.324203,-5.328555],[0.748308,2.354573,-7.030285,-1.087683,9.176321,3.201723,3.706507,8.901073],[-7.414672,-2.755559,-9.748623,-0.646649,4.920795,4.666601,1.037106,-1.451374],[-4.647707,-1.115029,6.815214,3.998525,7.194041,5.558787,2.184371,-7.965794],[5.447972,-6.328220,-0.642515,-5.284425,-0.228399,-9.469301,-9.757578,-3.647781],[-4.749735,3.587615,9.524435,9.441026,0.038419,-2.968086,8.276307,0.374048],[0.718086,5.379969,-5.073329,9.643948,3.555891,9.146851,7.540319,1.346449],[-2.819116,9.203639,2.880137,-0.038957,4.019826,8.594209,-5.156408,6.437220]],[[-5.388186,1.353574,5.334490,-6.312777,-5.434560,-2.836365,2.480991,-3.075442],[-7.135459,-6.497559,-0.011475,-0.384939,2.871387,-9.042355,-3.080459,7.242968],[-6.681676,-0.842557,6.309925,4.400061,-6.940211,0.515489,6.215617,6.556171],[2.375508,1.200589,-7.018635,-9.970878,3.706234,2.240078,-8.484670,8.144533],[-4.051391,-2.123178,-6.976748,7.382888,9.752640,-6.894500,-7.912016,-0.934274],[7.494367,9.601893,-6.565955,5.178967,7.221646,5.370105,6.570667,-9.511001],[-2.521335,-1.875262,-4.350531,4.151550,-7.078258,-6.929290,8.366438,8.626204],[-7.397594,0.259764,-9.831305,1.916629,9.489247,5.379753,4.601807,-3.456322],[1.529630,-6.292796,2.586583,5.811500,8.468268,-6.962481,9.743771,-1.260196],[9.383178,-8.402029,-1.944444,2.624370,-1.282932,7.880476,-3.593350,-8.868708],[-3.511758,-4.065917,-3.155597,6.554500,4.419520,1.900270,2.422785,9.433985],[2.198779,-2.930639,2.468321,3.202628,3.569916,3.959677,6.704446,0.759604],[-2.020688,4.523385,1.373189,-4.746538,-4.681455,9.305853,7.269595,-6.015458],[-9.068554,7.085561,-4.028412,-0.341361,1.366558,-2.284079,8.751095,-0.919403]],[[3.504254,-5.108858,-8.849669,5.366752,-7.703461,8.402105,4.670368,-4.375054],[-8.575844,7.100242,9.843565,-7.136576,1.380459,1.422702,-3.084215,-4.811337],[5.050908,5.658501,-5.348968,-6.610014,2.595084,-5.712917,-7.026222,1.545145],[-5.450571,6.196858,-1.673439,-8.363420,-8.780771,-2.334030,8.505590,-6.216493],[4.655620,3.425088,1.962316,3.683858,9.863840,4.298654,-0.272725,-3.390709],[-9.833398,-3.977379,-8.124546,-8.211670,-1.451373,1.774894,-4.885617,-3.754631],[9.705582,4.409101,-7.687562,-7.211811,-1.939150,6.599458,-9.527157,-5.457413],[4.234897,2.181323,9.528552,3.525961,-0.219728,-5.096371,-9.775470,-2.444268],[-2.803252,-3.545804,-0.636946,-9.261097,9.272961,-8.533017,2.540771,-9.862610],[2.120651,-2.815587,9.452601,2.939225,4.431605,-0.496699,-8.274756,3.453655],[-3.342441,1.581474,-2.841481,-0.892495,6.196054,9.453087,0.334303,-1.024024],[0.313572,7.844091,-4.561273,-2.494287,-4.117547,6.313470,-9.251741,8.630216],[1.551961,7.661161,-3.460175,3.770299,-3.409609,9.133653,-9.218733,4.201777],[-0.961383,-9.524845,7.244187,-1.475413,-9.971004,-8.179405,6.398335,9.388283]],[[2.255873,-5.250288,-9.550825,0.191231,2.689304,-3.001407,-7.903154,2.508141],[4.783717,5.784988,8.263241,-2.943875,-0.889398,-5.527998,0.508704,-3.305611],[-2.794832,-9.058638,-0.747254,-4.727510,-2.797020,4.285965,-8.624577,-4.712557],[-1.263830,-5.325520,1.205624,1.790665,0.568961,3.128077,-7.130253,8.358812],[4.547213,8.189527,-5.793340,4.418376,5.980799,1.891060,3.216683,3.316433],[-5.843247,2.190022,-6.449104,7.317071,-7.431756,-2.521719,-3.472917,-2.493546],[-4.381683,2.256287,8.626359,0.115498,3.051812,-2.459950,-9.351130,-1.829635],[8.367003,3.591132,9.455786,9.405264,6.309132,-4.625117,-8.736873,8.080589],[-6.963537,7.865848,4.815641,-6.744190,5.679107,-4.524251,-7.632029,-5.788681],[-7.052660,-0.637546,-7.932940,-5.303260,3.321816,7.434031,1.500544,-0.492255],[7.707270,5.370413,9.184001,8.793427,-6.245803,-6.663844,4.913743,-9.318643],[-9.660320,4.064967,-0.904816,8.701781,-7.725015,6.115526,8.530796,5.664290],[4.474591,-2.719450,7.399547,-4.459689,7.971013,-5.635044,0.733646,-9.247420],[8.478351,8.959040,9.339625,-2.904900,1.941882,9.943884,2.578696,-4.306689]],[[6.652194,2.651154,-5.767846,-3.223805,0.116789,-4.861485,8.830881,-6.331462],[-8.064193,1.367837,-6.722736,1.076047,0.009241,5.615100,-3.402821,-4.493343],[-8.771524,-8.306138,3.011635,-4.230184,6.196153,3.783907,8.652334,-6.804075],[1.189360,-7.933376,4.424071,-3.483306,-0.143388,6.448196,8.548162,5.761720],[-4.798317,-8.886413,-9.521394,-3.031248,-8.632719,3.863379,2.206577,0.929689],[2.329612,6.503781,-2.945296,7.973753,2.516310,5.203338,-9.819523,-4.659222],[-0.802705,-6.900647,0.375232,-1.867031,3.549992,4.765248,4.305491,4.470231],[-9.008342,8.687173,-5.986355,-8.196064,-8.607091,-2.066473,-4.186073,2.217459],[-9.304273,0.971867,-4.379309,0.312130,9.994129,-6.936562,3.737648,5.590146],[-6.650659,-7.702714,-3.990102,-9.185421,-7.704063,4.825418,3.371220,3.686684],[9.013393,2.524860,1.285274,2.582558,-5.046068,3.213866,0.349107,3.588343],[-5.483707,1.809831,-4.572312,9.672599,-7.373679,7.510965,1.651847,6.736135],[-5.212044,-1.111522,2.661833,-5.999378,8.022546,-4.122524,8.391369,1.358047],[9.314730,-1.124386,-4.689894,6.644555,-9.527947,3.447356,5.110579,-2.327450]],[[3.805770,8.140416,-7.496229,-9.296779,-3.113427,1.355909,4.085742,8.797466],[6.864775,-1.719260,2.687579,-5.074232,0.018893,7.149924,8.511469,-9.011262],[-4.815070,8.119036,2.553517,-4.184308,-7.731518,9.256631,-0.738553,4.193380],[-9.435711,-9.007164,2.126036,-8.537019,-1.888870,5.080228,9.228548,-0.669196],[-8.722444,3.379012,-0.511873,1.669543,0.195817,-0.128196,4.089236,8.742871],[7.514999,6.137442,-1.840542,2.468729,5.564592,-2.175136,-7.769915,-1.727377],[1.547207,4.182355,8.815734,-6.071271,6.996635,2.147336,-6.623289,5.803044],[-9.803508,-4.984837,-6.519674,2.610944,5.493008,-5.253103,-8.248856,-7.235803],[-4.570567,8.514533,-3.490149,-8.241020,-5.655026,-6.125620,-2.281726,4.285359],[-0.802689,-0.463505,6.335338,-1.336049,0.286129,0.567307,2.759573,7.870449],[9.304233,4.812734,4.399286,1.191253,4.335703,-7.531045,9.574090,-9.195330],[-3.045467,-2.182123,-1.228135,-6.951917,-0.197631,-0.575045,5.399178,0.070258],[-4.367789,-5.660738,6.443841,-1.127297,5.258148,-3.342082,-3.380898,-4.881282],[8.247299,-8.600324,4.775131,-3.445148,-5.476643,4.613593,-0.471724,-3.923088]]], dtype = "float64")#candidate|4544|(6, 14, 8)|const|float64
bop_4545 = relay.subtract(var_4543.astype('float64'), relay.reshape(const_4544.astype('float64'), relay.shape_of(var_4543))) # shape=(6, 14, 8)
uop_4555 = relay.cos(const_4544.astype('float64')) # shape=(6, 14, 8)
output = relay.Tuple([bop_4545,uop_4555,])
output2 = relay.Tuple([bop_4545,uop_4555,])
func_4566 = relay.Function([var_4543,], output)
mod['func_4566'] = func_4566
mod = relay.transform.InferType()(mod)
var_4567 = relay.var("var_4567", dtype = "float64", shape = (6, 14, 8))#candidate|4567|(6, 14, 8)|var|float64
output = func_4566(var_4567)
func_4568 = relay.Function([var_4567], output)
mutated_mod['func_4568'] = func_4568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1250_call = mod.get_global_var('func_1250')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_4577 = relay.TupleGetItem(func_1250_call(), 0)
call_4578 = relay.TupleGetItem(func_1252_call(), 0)
uop_4582 = relay.asin(call_4577.astype('float64')) # shape=(14, 13, 2)
uop_4584 = relay.asin(call_4578.astype('float64')) # shape=(14, 13, 2)
output = relay.Tuple([uop_4582,])
output2 = relay.Tuple([uop_4584,])
func_4589 = relay.Function([], output)
mod['func_4589'] = func_4589
mod = relay.transform.InferType()(mod)
mutated_mod['func_4589'] = func_4589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4589_call = mutated_mod.get_global_var('func_4589')
call_4590 = func_4589_call()
output = call_4590
func_4591 = relay.Function([], output)
mutated_mod['func_4591'] = func_4591
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4603 = relay.const(-5, dtype = "int16")#candidate|4603|()|const|int16
const_4604 = relay.const([[[8,7,1,4,-10,5]],[[-6,5,-9,4,10,-9]],[[5,-3,-3,-4,10,-2]],[[1,-1,6,-9,7,10]],[[-10,10,-4,-10,-10,7]],[[1,-8,-1,4,-8,-5]],[[2,-5,-7,-5,-9,-9]],[[-3,2,-6,-9,-10,-8]],[[9,5,6,10,-5,7]],[[9,-10,-6,-1,-2,4]],[[-2,4,2,-3,1,-8]]], dtype = "int16")#candidate|4604|(11, 1, 6)|const|int16
bop_4605 = relay.bitwise_xor(const_4603.astype('int16'), const_4604.astype('int16')) # shape=(11, 1, 6)
output = bop_4605
output2 = bop_4605
func_4615 = relay.Function([], output)
mod['func_4615'] = func_4615
mod = relay.transform.InferType()(mod)
mutated_mod['func_4615'] = func_4615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4615_call = mutated_mod.get_global_var('func_4615')
call_4616 = func_4615_call()
output = call_4616
func_4617 = relay.Function([], output)
mutated_mod['func_4617'] = func_4617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_336_call = mod.get_global_var('func_336')
func_338_call = mutated_mod.get_global_var('func_338')
call_4621 = relay.TupleGetItem(func_336_call(), 3)
call_4622 = relay.TupleGetItem(func_338_call(), 3)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_4632 = func_2626_call()
call_4633 = func_2626_call()
output = relay.Tuple([call_4621,call_4632,])
output2 = relay.Tuple([call_4622,call_4633,])
func_4634 = relay.Function([], output)
mod['func_4634'] = func_4634
mod = relay.transform.InferType()(mod)
mutated_mod['func_4634'] = func_4634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4634_call = mutated_mod.get_global_var('func_4634')
call_4635 = func_4634_call()
output = call_4635
func_4636 = relay.Function([], output)
mutated_mod['func_4636'] = func_4636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1334_call = mod.get_global_var('func_1334')
func_1336_call = mutated_mod.get_global_var('func_1336')
call_4653 = relay.TupleGetItem(func_1334_call(), 0)
call_4654 = relay.TupleGetItem(func_1336_call(), 0)
output = relay.Tuple([call_4653,])
output2 = relay.Tuple([call_4654,])
func_4685 = relay.Function([], output)
mod['func_4685'] = func_4685
mod = relay.transform.InferType()(mod)
output = func_4685()
func_4686 = relay.Function([], output)
mutated_mod['func_4686'] = func_4686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3276_call = mod.get_global_var('func_3276')
func_3277_call = mutated_mod.get_global_var('func_3277')
call_4690 = relay.TupleGetItem(func_3276_call(), 0)
call_4691 = relay.TupleGetItem(func_3277_call(), 0)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_4702 = relay.TupleGetItem(func_380_call(), 1)
call_4703 = relay.TupleGetItem(func_381_call(), 1)
output = relay.Tuple([call_4690,call_4702,])
output2 = relay.Tuple([call_4691,call_4703,])
func_4704 = relay.Function([], output)
mod['func_4704'] = func_4704
mod = relay.transform.InferType()(mod)
output = func_4704()
func_4705 = relay.Function([], output)
mutated_mod['func_4705'] = func_4705
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4712 = relay.var("var_4712", dtype = "float32", shape = (1, 6, 12))#candidate|4712|(1, 6, 12)|var|float32
uop_4713 = relay.rsqrt(var_4712.astype('float32')) # shape=(1, 6, 12)
func_3054_call = mod.get_global_var('func_3054')
func_3057_call = mutated_mod.get_global_var('func_3057')
const_4719 = relay.const([6.986566,6.273020,8.033730,-7.435950,-5.501621,6.737497,4.106128,-6.452073,-9.404000,-1.593935,-8.205960,3.123000,6.717934,-6.406604,2.361933,-3.723068,-8.029889,-8.730609,-9.074516,-6.349083,-5.279213,0.889876,-9.353958,-8.090098,8.429281,-2.200315,-2.455238,9.613592,3.620769,-3.492957], dtype = "float64")#candidate|4719|(30,)|const|float64
var_4720 = relay.var("var_4720", dtype = "float64", shape = (420,))#candidate|4720|(420,)|var|float64
call_4718 = relay.TupleGetItem(func_3054_call(relay.reshape(const_4719.astype('float64'), [2, 1, 15]), relay.reshape(var_4720.astype('float64'), [2, 14, 15]), ), 1)
call_4721 = relay.TupleGetItem(func_3057_call(relay.reshape(const_4719.astype('float64'), [2, 1, 15]), relay.reshape(var_4720.astype('float64'), [2, 14, 15]), ), 1)
func_1358_call = mod.get_global_var('func_1358')
func_1360_call = mutated_mod.get_global_var('func_1360')
call_4722 = func_1358_call()
call_4723 = func_1358_call()
output = relay.Tuple([uop_4713,call_4718,const_4719,var_4720,call_4722,])
output2 = relay.Tuple([uop_4713,call_4721,const_4719,var_4720,call_4723,])
func_4736 = relay.Function([var_4712,var_4720,], output)
mod['func_4736'] = func_4736
mod = relay.transform.InferType()(mod)
mutated_mod['func_4736'] = func_4736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4736_call = mutated_mod.get_global_var('func_4736')
var_4738 = relay.var("var_4738", dtype = "float32", shape = (1, 6, 12))#candidate|4738|(1, 6, 12)|var|float32
var_4739 = relay.var("var_4739", dtype = "float64", shape = (420,))#candidate|4739|(420,)|var|float64
call_4737 = func_4736_call(var_4738,var_4739,)
output = call_4737
func_4740 = relay.Function([var_4738,var_4739,], output)
mutated_mod['func_4740'] = func_4740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_4814 = func_2626_call()
call_4815 = func_2626_call()
output = relay.Tuple([call_4814,])
output2 = relay.Tuple([call_4815,])
func_4818 = relay.Function([], output)
mod['func_4818'] = func_4818
mod = relay.transform.InferType()(mod)
output = func_4818()
func_4819 = relay.Function([], output)
mutated_mod['func_4819'] = func_4819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4685_call = mod.get_global_var('func_4685')
func_4686_call = mutated_mod.get_global_var('func_4686')
call_4848 = relay.TupleGetItem(func_4685_call(), 0)
call_4849 = relay.TupleGetItem(func_4686_call(), 0)
func_1852_call = mod.get_global_var('func_1852')
func_1856_call = mutated_mod.get_global_var('func_1856')
var_4863 = relay.var("var_4863", dtype = "float64", shape = (5460,))#candidate|4863|(5460,)|var|float64
call_4862 = relay.TupleGetItem(func_1852_call(relay.reshape(var_4863.astype('float64'), [5460,]), relay.reshape(call_4848.astype('uint64'), [120,]), ), 2)
call_4864 = relay.TupleGetItem(func_1856_call(relay.reshape(var_4863.astype('float64'), [5460,]), relay.reshape(call_4848.astype('uint64'), [120,]), ), 2)
output = relay.Tuple([call_4848,call_4862,var_4863,])
output2 = relay.Tuple([call_4849,call_4864,var_4863,])
func_4871 = relay.Function([var_4863,], output)
mod['func_4871'] = func_4871
mod = relay.transform.InferType()(mod)
var_4872 = relay.var("var_4872", dtype = "float64", shape = (5460,))#candidate|4872|(5460,)|var|float64
output = func_4871(var_4872)
func_4873 = relay.Function([var_4872], output)
mutated_mod['func_4873'] = func_4873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1162_call = mod.get_global_var('func_1162')
func_1164_call = mutated_mod.get_global_var('func_1164')
call_4929 = relay.TupleGetItem(func_1162_call(), 2)
call_4930 = relay.TupleGetItem(func_1164_call(), 2)
output = call_4929
output2 = call_4930
func_4937 = relay.Function([], output)
mod['func_4937'] = func_4937
mod = relay.transform.InferType()(mod)
output = func_4937()
func_4938 = relay.Function([], output)
mutated_mod['func_4938'] = func_4938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2980_call = mod.get_global_var('func_2980')
func_2982_call = mutated_mod.get_global_var('func_2982')
call_4984 = relay.TupleGetItem(func_2980_call(), 2)
call_4985 = relay.TupleGetItem(func_2982_call(), 2)
func_1071_call = mod.get_global_var('func_1071')
func_1075_call = mutated_mod.get_global_var('func_1075')
var_4987 = relay.var("var_4987", dtype = "float64", shape = (5460,))#candidate|4987|(5460,)|var|float64
call_4986 = relay.TupleGetItem(func_1071_call(relay.reshape(call_4984.astype('float64'), [14, 13, 2]), relay.reshape(var_4987.astype('float64'), [15, 364]), ), 1)
call_4988 = relay.TupleGetItem(func_1075_call(relay.reshape(call_4984.astype('float64'), [14, 13, 2]), relay.reshape(var_4987.astype('float64'), [15, 364]), ), 1)
bop_4989 = relay.greater(call_4984.astype('bool'), relay.reshape(call_4986.astype('bool'), relay.shape_of(call_4984))) # shape=(1, 364)
bop_4992 = relay.greater(call_4985.astype('bool'), relay.reshape(call_4988.astype('bool'), relay.shape_of(call_4985))) # shape=(1, 364)
func_3470_call = mod.get_global_var('func_3470')
func_3472_call = mutated_mod.get_global_var('func_3472')
const_4994 = relay.const([5.258362,-4.132862,-2.764859,-3.449768,-5.366017,-2.596122,8.039064,-3.330326,2.353065,6.871849,-0.773289,-9.142636,7.669271,8.055738,-7.244856,-1.603712,-4.617388,9.988806,-0.017376,9.733412,4.707690,-1.573331,-9.698529,2.105375,0.794347,5.246163,5.182679,-3.801056,-7.154627,-5.986463,-2.983022,-2.355727,8.489281,-3.208517,3.368831,-7.083886,5.198784,4.061705,6.274525,0.212054,3.768428,-9.324635,-5.115432,-9.836430,-1.509540,6.720476,6.744571,0.809007,-2.387950,0.500153,-0.996475,-0.711452,-1.704039,2.844997,-1.355153,5.665320,-6.911000,1.169895,-0.858431,5.861869,-4.269948,7.972453,-9.107050,-5.886895,-3.257483,-3.212352,8.468619,-9.678995,0.539805,0.852540,-0.924958,0.256050,-3.613760,0.961994,-2.692925,7.260755,-0.804453,3.217232,-7.683356,5.276106,1.078385,5.450778,-9.880775,-7.204446,9.472159,-5.399103,-2.164533,-6.817133,-4.019879,5.429073,-8.529617,8.464014,-9.010256,2.855104,-1.723728,9.466320,0.820728,-1.246277,9.771076,4.173653,-2.012780,-5.408174,4.990520,3.366097,4.207492,7.200560,1.059987,-6.154123,3.793811,-9.336127,-6.279433,2.418512,-6.754529,5.999806,-4.137586,6.096887,-7.843207,-1.419790,-4.928183,0.383015,-1.646761,-3.295250,6.704918,9.515051,-4.287465,-6.230149,-9.721895,-1.594119,5.111704,-4.914709,-8.625193,-4.489914,0.753549,0.672915,-7.601859,0.403485,5.357150,1.969957,-3.055039,2.008482,-7.579419,8.652439,6.493807,-2.518091,-5.331573,-5.347623,-6.264673,1.702017,2.805913,8.871828,-0.115819,7.437087,-6.599153,-3.342708,8.604833,-2.786893,-8.128875,-8.335695,4.563131,-2.941841,6.313515,3.983241,-5.722078,-9.749297,8.771148,7.853745,-2.827674,2.778421,1.242679,-5.337891,0.244207,3.500123,-0.314506,2.468706,-5.035910,7.350222,-1.146056,2.405199,-8.559924,9.560247,5.451740,6.133921,0.670097,6.471761,-1.841110,6.556189,-6.005485,8.944805,6.048636,-9.603784,0.456188,5.893959,-5.442203,-3.452976,-6.625415,-1.208492,-4.699654,-0.884316,-0.722842,6.464067,7.587404,-4.854491,0.179635,-7.987109,-4.984709,-3.280312,9.611908,-7.382821,-0.587410,-8.708682,-5.773335,-6.624541,-0.830307,-7.969522,-5.209838,1.999641,-1.458671,9.398464,-2.040110,-3.596809,6.487834,-8.196179,6.387897,-5.693279,0.450680,-1.217367,-5.936631,-8.254920,5.491695,1.569945,-3.951747,3.917985,6.688962,-4.696861,0.281269,-3.361384,5.190821,4.605544,5.246997,-0.743565,-5.643144,-6.709042,-0.396251,1.706059,6.027659,7.875595,4.252136,2.894269,-8.447476,-7.595363,-6.662474,-4.308429,3.797064,-9.347323,9.333828,9.644749,-2.852717,-3.119969,3.974421,-3.175699,3.758201,-1.718479,2.255080,6.902523,-5.573367,2.210183,-3.810715,-0.409726,8.589610,2.568356,-8.722925,-0.310399,-7.936784,4.574040,-2.593493,7.990414,7.470160,-1.967829,4.411560,-4.209816,-9.407167,-3.281175,5.724406,-0.430785,-9.773170,-0.219685,5.399996,4.265512,5.202680,1.887901,-9.051838,6.533046,-2.721282,-7.145729,5.703416,2.280866,-7.347423,0.149033,7.573964,-9.888531,8.092127,-9.448386,3.734110,-2.466100,-1.831624,-2.466741,-9.738396,-8.114163,-6.158966,-1.226147,-0.460998,7.338178,-0.411133,-2.413424,-4.697670,2.046665,0.453737,-0.730160,2.011546,-6.427507,-0.883649,-5.433307,-3.592252,-6.123343,-0.220469,1.997243,-0.192020,2.513665,7.492475,-5.626779,9.353035,0.812121,3.068429,7.482559,-6.614633,-8.764133,6.474389,-1.861070,-5.997386,-8.068151,9.707281,3.004401,-3.307150,-1.702329,-3.870558,7.250791,-2.123870,6.026446,4.073071,-0.204273,-3.646528,-2.682761,-8.761474,0.108832,3.464652,8.248303,9.641596,2.237721,2.563882,5.960267,-1.737754,2.097659,6.823930,3.718835,-1.976599,3.714087,-8.016937,-5.662813,-6.323388,6.655482,6.623705,-2.286481,0.836167,-6.640395,-7.574063,1.475369,-1.791923,4.439676,4.763510,-9.460885,4.482304,-8.883103,-8.180661,-3.806872,-7.999019,-7.778564,-1.243838,6.997027,-4.918387,-9.160404,4.374495,-7.361121,3.519775,-2.637421,-9.109262,-3.371214,-8.173230,4.581750,1.732323,2.244859,-0.522186,6.558069,-2.830673,-3.059915,-7.531866,3.496765,-2.916770,1.810365,-2.830861,-9.798515,7.820972,-2.965087,1.362555,-3.844017,1.604508,9.893218,4.229480,-8.885680,4.554541,3.417935,0.933883,8.798087,-6.461082,8.432479,-9.892732,9.525293,-8.090587,8.144765,1.782429,-8.708046,4.363339,-5.937432,-4.587716,1.910326,-7.418429,5.412260,4.237457,9.927773,-0.240084,-6.673129,6.864339,-6.338894,6.460331,0.902755,1.132941,9.001261,8.123530,3.079825,-3.965848,1.466521,8.098211,4.122833,-7.004948,-6.437668,4.741085,8.631417,-2.483604,2.120211,-6.511009,1.020017,-3.138819,-2.544584,-2.073986,-8.296422,-7.376978,1.749767,-2.299250,0.554336,-4.453542,0.660031,-7.120013,-3.568035,-2.977237,8.783273,-1.617826,-3.748053,3.811543,1.819314,6.616062,8.504702,9.994167,4.297442,0.380424,-5.774658,7.089688,0.996737,7.499196,-0.287304,3.177220,-3.059582,-0.541696,9.464639,5.055222,-0.624917,-3.965309,6.897287,-1.471563,8.526500,8.664991,4.530424,-1.672774,-1.854526,-9.553837,9.673868,-7.471678,-0.281733,1.375512,5.491594,-2.938183,6.575019,1.221794,-9.819644], dtype = "float64")#candidate|4994|(512,)|const|float64
call_4993 = relay.TupleGetItem(func_3470_call(relay.reshape(const_4994.astype('float64'), [512,])), 0)
call_4995 = relay.TupleGetItem(func_3472_call(relay.reshape(const_4994.astype('float64'), [512,])), 0)
bop_4998 = relay.bitwise_xor(call_4986.astype('int16'), relay.reshape(call_4984.astype('int16'), relay.shape_of(call_4986))) # shape=(14, 13, 2)
bop_5001 = relay.bitwise_xor(call_4988.astype('int16'), relay.reshape(call_4985.astype('int16'), relay.shape_of(call_4988))) # shape=(14, 13, 2)
output = relay.Tuple([var_4987,bop_4989,call_4993,const_4994,bop_4998,])
output2 = relay.Tuple([var_4987,bop_4992,call_4995,const_4994,bop_5001,])
func_5011 = relay.Function([var_4987,], output)
mod['func_5011'] = func_5011
mod = relay.transform.InferType()(mod)
mutated_mod['func_5011'] = func_5011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5012 = relay.var("var_5012", dtype = "float64", shape = (5460,))#candidate|5012|(5460,)|var|float64
func_5011_call = mutated_mod.get_global_var('func_5011')
call_5013 = func_5011_call(var_5012)
output = call_5013
func_5014 = relay.Function([var_5012], output)
mutated_mod['func_5014'] = func_5014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2444_call = mod.get_global_var('func_2444')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_5083 = relay.TupleGetItem(func_2444_call(), 0)
call_5084 = relay.TupleGetItem(func_2446_call(), 0)
output = call_5083
output2 = call_5084
func_5087 = relay.Function([], output)
mod['func_5087'] = func_5087
mod = relay.transform.InferType()(mod)
mutated_mod['func_5087'] = func_5087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5087_call = mutated_mod.get_global_var('func_5087')
call_5088 = func_5087_call()
output = call_5088
func_5089 = relay.Function([], output)
mutated_mod['func_5089'] = func_5089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5095 = relay.var("var_5095", dtype = "bool", shape = (14, 1, 10))#candidate|5095|(14, 1, 10)|var|bool
var_5096 = relay.var("var_5096", dtype = "bool", shape = (14, 12, 10))#candidate|5096|(14, 12, 10)|var|bool
bop_5097 = relay.logical_or(var_5095.astype('bool'), var_5096.astype('bool')) # shape=(14, 12, 10)
uop_5105 = relay.acos(var_5095.astype('float32')) # shape=(14, 1, 10)
output = relay.Tuple([bop_5097,uop_5105,])
output2 = relay.Tuple([bop_5097,uop_5105,])
func_5112 = relay.Function([var_5095,var_5096,], output)
mod['func_5112'] = func_5112
mod = relay.transform.InferType()(mod)
mutated_mod['func_5112'] = func_5112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5112_call = mutated_mod.get_global_var('func_5112')
var_5114 = relay.var("var_5114", dtype = "bool", shape = (14, 1, 10))#candidate|5114|(14, 1, 10)|var|bool
var_5115 = relay.var("var_5115", dtype = "bool", shape = (14, 12, 10))#candidate|5115|(14, 12, 10)|var|bool
call_5113 = func_5112_call(var_5114,var_5115,)
output = call_5113
func_5116 = relay.Function([var_5114,var_5115,], output)
mutated_mod['func_5116'] = func_5116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1102_call = mod.get_global_var('func_1102')
func_1104_call = mutated_mod.get_global_var('func_1104')
call_5137 = func_1102_call()
call_5138 = func_1102_call()
output = relay.Tuple([call_5137,])
output2 = relay.Tuple([call_5138,])
func_5141 = relay.Function([], output)
mod['func_5141'] = func_5141
mod = relay.transform.InferType()(mod)
mutated_mod['func_5141'] = func_5141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5141_call = mutated_mod.get_global_var('func_5141')
call_5142 = func_5141_call()
output = call_5142
func_5143 = relay.Function([], output)
mutated_mod['func_5143'] = func_5143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4589_call = mod.get_global_var('func_4589')
func_4591_call = mutated_mod.get_global_var('func_4591')
call_5170 = relay.TupleGetItem(func_4589_call(), 0)
call_5171 = relay.TupleGetItem(func_4591_call(), 0)
func_1038_call = mod.get_global_var('func_1038')
func_1039_call = mutated_mod.get_global_var('func_1039')
call_5196 = relay.TupleGetItem(func_1038_call(), 0)
call_5197 = relay.TupleGetItem(func_1039_call(), 0)
func_4073_call = mod.get_global_var('func_4073')
func_4076_call = mutated_mod.get_global_var('func_4076')
var_5202 = relay.var("var_5202", dtype = "float64", shape = (2, 704))#candidate|5202|(2, 704)|var|float64
call_5201 = relay.TupleGetItem(func_4073_call(relay.reshape(var_5202.astype('float64'), [11, 8, 16]), relay.reshape(var_5202.astype('float64'), [11, 8, 16]), ), 2)
call_5203 = relay.TupleGetItem(func_4076_call(relay.reshape(var_5202.astype('float64'), [11, 8, 16]), relay.reshape(var_5202.astype('float64'), [11, 8, 16]), ), 2)
func_1528_call = mod.get_global_var('func_1528')
func_1531_call = mutated_mod.get_global_var('func_1531')
const_5214 = relay.const([[-9.530139,-6.783545,-5.503016,-1.375532,-3.159190,-4.240199,-4.826972,6.941286,-8.805435,5.577868,-5.594912,-6.650599,-0.368996,1.464108,8.263177,1.709744,0.636814,4.184223,3.503906,-9.185672,9.026325,-8.397432,7.584984,6.410611,7.012934,3.922872,5.826486,-3.766539,5.967390,-4.548953,0.528068,9.476321,2.049776,-1.621539,-6.030567,-5.018857,1.830971,-0.336000,-9.529330,-8.393925,-4.446872,-2.399107,-7.170323,5.479413,-3.538728,-7.622739,3.509681,-9.306759,-8.771460,-1.058080,-3.218491,-4.961250,8.341915,-2.594016,1.279630,-3.732299,-3.313363,6.519247,3.618043,-0.615340,3.371025,8.822696,-6.788419,2.586279,-1.584879,-3.730500,2.999950,-1.175482,9.678166,-0.604752,3.669825,-8.022127,2.889873,-8.807219,7.581302,-6.947082,-1.520960,3.471460,-5.038741,1.084167,-8.845542,5.181407,4.905507,3.890804,-3.265176,7.424012,-6.162035,4.938016,4.714784,-5.860411,-9.116946,1.607307,-5.000861,-8.603576,-9.680756,9.505326,3.220879,-2.472022,-0.598254,2.892849,5.046113,-0.446991,-8.843871,-7.963116,-3.115539,-6.712349,3.111066,8.755842,2.766769,-1.125303,4.936471,-9.763720,-1.905080,4.691951,-2.380112,9.887805,8.655475,1.132950,1.260861,-3.136497,-8.853120,6.798942,-6.945680,7.453457,-8.624685,0.264477,1.803559,-4.952748,-5.461376,-1.984101,-4.951064,6.190720,-5.280026,5.907053,-5.727733,1.751047,7.190928,-3.511707,0.788707,4.206922,-1.329130,3.515320,-0.430198,3.251996,-3.643367,-1.564950,-9.587142,-4.177165,-3.462764,-3.544477,7.257124,-0.415493,-3.840273,2.870031,-6.114362,9.697158],[9.955581,9.220348,-0.464769,8.996043,-3.812267,2.805849,1.693790,7.359120,-2.106403,-8.965276,3.773275,-4.335579,4.035670,5.402300,-4.499516,-9.352382,-3.529431,5.864259,9.086833,1.843466,-0.443633,-7.570497,-7.021509,-2.240885,6.552531,3.188258,3.579501,0.577662,4.151459,-8.921351,2.476547,1.466907,-4.384183,3.436158,4.640252,-8.276645,6.038863,6.195183,-4.295291,-8.055512,-1.044507,3.082410,9.018338,2.786361,7.457590,-7.043237,-8.141563,-2.604237,2.319364,-8.344179,-7.088121,-1.547971,1.016769,-9.311208,2.024974,-0.051910,-1.166726,2.773889,-7.441851,-3.952378,3.073616,-9.320621,-4.988171,-5.208025,-0.604101,4.043567,4.905651,7.063023,1.837127,2.703554,-4.930951,4.961638,2.356864,9.405416,6.507366,0.952950,-0.886292,-5.757381,5.745492,-6.414768,-0.794763,-1.381816,-8.802078,-2.473074,8.167059,-2.089729,3.383591,-6.032961,0.255630,-8.082526,2.354762,4.674532,-4.328536,3.074884,-5.921481,4.753688,8.622779,1.293792,4.880524,9.315424,9.025217,3.564595,1.694983,6.115597,1.186798,8.904429,4.540332,-6.561071,1.673227,5.781827,-7.581171,-6.441165,8.503350,0.877396,1.618064,0.108240,-1.293606,-9.925456,8.734911,-8.878449,6.716301,0.524966,-0.018916,-4.323881,4.878108,-6.846112,8.054807,1.133183,-9.514651,6.851963,-2.215712,-9.244618,3.984578,-5.018346,-0.474292,9.638868,6.631736,-0.977766,2.879519,2.602379,3.474416,-2.163214,-4.561061,0.183741,-4.162336,-6.770157,3.778840,8.086445,2.103348,1.812344,5.904234,-8.438457,-2.206662,-9.253520,0.416383,-9.543694],[9.327623,5.673829,7.655830,-0.378986,-8.728065,-5.664635,1.395178,-9.318865,7.901747,-4.963067,6.353361,8.351020,-8.765609,3.701733,6.894925,-3.585545,-9.129599,-2.257886,-5.318509,1.103001,-9.752262,-4.049596,6.395146,-9.287765,5.816497,3.334329,9.328094,-2.263624,5.918135,-5.572210,9.734990,6.195894,-9.625938,1.148440,0.968258,9.177224,-9.071443,7.535277,8.675853,0.622929,8.206601,3.358071,8.775988,-0.788549,9.273686,-4.234594,2.602207,-2.084147,8.331591,-5.924912,-7.988320,-1.840072,0.106601,-9.177666,-0.414127,3.512408,9.768484,-3.976848,-9.439460,4.753926,0.408594,0.155655,5.977857,7.850273,5.803751,3.791717,3.218838,4.856871,-1.410263,9.842371,6.957036,-7.468658,9.355857,6.602849,2.964061,7.212361,-4.457936,3.004863,-1.998418,3.375921,-7.750962,8.192613,-2.430213,-8.532153,7.686743,3.260651,1.970910,1.019032,4.402783,-6.780372,1.755116,8.334995,-1.481793,4.214434,5.507938,5.645036,-4.305220,-5.967493,4.972465,3.360081,-9.437162,6.401299,-6.052143,3.644775,2.737617,-2.219993,7.992555,0.958129,-9.121713,7.359246,6.404516,8.805771,4.737745,-8.763987,-8.104435,0.440945,5.347355,-4.034034,8.002723,9.494754,-2.142437,3.865954,3.221187,7.784333,-0.394076,-7.827447,2.257563,1.585872,2.229818,8.502775,9.224320,-2.994404,4.124013,-5.604417,-8.176354,-1.218833,7.318531,0.382153,-6.790010,-7.147457,1.137700,-3.797808,-0.931602,5.437859,3.371492,7.750448,-6.335975,4.162838,2.847427,-2.075281,8.492796,-4.102003,5.399502,-5.892890,-2.362068,-3.163960],[0.865132,7.526337,-4.676832,5.069596,9.553315,-1.954237,-7.151943,-9.204290,8.526593,-2.611759,9.874361,4.473051,-9.834193,-4.804543,-7.213376,-9.834417,7.781801,6.784618,-1.690790,1.929259,2.901343,3.394752,-4.069432,7.507551,3.569145,-5.684636,-5.229981,4.548802,6.104818,-5.966367,-9.900364,0.465207,-8.934184,2.842356,6.839836,-2.781984,-3.809681,4.420633,1.590147,-8.538835,-3.066357,8.470217,-0.687940,2.728980,-1.701069,2.758699,-2.215897,-6.505819,5.071531,8.029179,0.680875,0.124654,-7.003812,-7.722917,-0.730273,-3.359673,6.391786,3.441734,-5.491171,-2.892018,-4.637029,7.211968,-1.298286,1.832446,6.426661,1.400931,1.133254,-6.079422,1.826917,7.390551,1.744616,-9.553767,-0.930931,-6.743674,-4.600043,9.650627,-9.939694,0.007145,3.716420,-4.501426,2.744991,1.020849,-0.022645,-0.154001,-8.498553,1.460546,1.542758,-1.106389,-2.561086,-6.904261,7.605789,6.220484,-1.920749,0.799697,-8.589230,-3.467026,0.247365,-3.619581,6.576914,7.325201,-3.704947,5.655031,-8.692164,4.510955,-3.202333,6.375275,-5.791966,0.009845,2.745378,-4.818142,-9.781199,8.546649,-9.207376,-3.475393,1.119669,5.156431,-0.187668,1.859713,-7.291690,6.382240,4.278746,9.278680,-9.064370,-7.541897,3.199861,4.524980,-6.350855,1.156884,-1.274853,-3.998995,6.918162,6.383431,0.663836,-9.952718,-7.720628,-9.666981,-9.079530,6.335048,8.992112,-1.199825,-9.736633,-4.669766,-2.818427,1.214229,9.952573,-5.948800,9.174988,8.237474,6.235983,-3.059144,3.384492,9.030450,-7.668166,-1.893149,-3.087095,-5.951541],[-2.361509,3.320390,-1.500782,5.589557,2.590279,-3.429566,-0.615730,5.830467,3.474939,1.023500,-3.820962,-4.667215,6.195234,-2.538063,6.639192,-1.195297,-9.842370,2.766399,-6.176976,-5.033657,-7.977580,-8.418775,-2.643959,-2.628235,8.893013,4.140874,-4.383753,9.747635,-9.300204,-6.235579,-7.821066,-5.643666,-0.271049,-4.406282,-3.026444,-3.996945,0.667010,9.242403,-5.318462,-6.467506,7.648309,-8.288512,0.349046,6.449584,1.940034,-3.686857,-0.842255,-2.734965,-5.061949,7.959744,-3.190813,9.041257,-9.057576,3.520594,3.218974,1.755759,2.557547,-0.301649,6.513966,6.579879,5.357326,-4.929141,-5.701072,9.896769,5.732691,2.383715,-9.431396,-1.765187,-1.712901,-2.451899,4.955638,-0.130242,6.531833,8.366733,5.042048,0.765996,-4.044523,-3.121417,0.320214,9.446051,8.394435,-3.145785,-2.883482,-3.935175,-3.682235,-5.250825,-6.527097,3.172849,4.357048,-6.488741,8.206261,-5.380533,-2.712692,-2.427068,-8.335121,-4.682255,-3.799216,6.362616,7.640920,6.188390,-7.421593,0.753627,0.968230,-1.892464,-9.531994,2.178640,0.309774,2.620028,-4.186273,3.659256,-3.569614,-4.281893,-0.999767,6.956554,-8.477016,5.308099,-3.037043,3.963175,1.788198,-2.574994,2.142972,6.316258,6.382644,-0.859980,-1.680482,-9.216991,5.574974,-9.685644,7.279698,-8.239639,-3.619433,-9.323707,-2.018765,-7.626362,-5.346398,5.491517,-3.426162,-9.340822,-8.648138,-0.522689,-4.951929,8.899787,9.373850,5.156849,7.079484,-6.299957,1.443471,-0.279108,2.857951,-7.359112,2.364976,3.682153,-6.828121,-2.972948,-2.433427,-6.922258],[3.181486,-7.348683,6.217766,1.409207,7.480979,-5.639044,8.356663,0.561912,-7.547978,-5.607537,8.178962,4.869976,8.436550,-9.025065,-7.019245,-0.281378,-0.683888,2.400938,-8.646380,-5.499273,-1.581357,-8.073876,5.217469,-6.226352,5.516322,-7.010415,-4.984934,3.192654,9.233808,9.623726,-9.779293,8.979861,7.465616,-4.015301,-7.951575,6.608920,4.987557,-8.829950,5.164638,-7.732818,8.463859,-3.372949,4.730670,9.296798,1.176074,-5.399092,-2.815662,5.517428,-2.071624,2.340284,-7.072818,-4.635853,-1.604219,3.852199,4.465488,0.856203,-0.100703,0.250066,6.236124,-9.796625,1.739876,-2.051701,-3.793313,7.423194,6.522999,3.860217,-7.856863,5.270332,-5.766844,-9.773218,5.834848,-6.796454,7.920228,8.796546,-3.228315,-7.091268,-3.573031,5.021934,-0.602440,-4.709402,3.490520,7.957392,5.972406,1.273939,8.807654,2.548525,9.811952,-0.699894,0.360843,5.359975,8.214002,-9.172224,-9.606953,9.980198,-8.278142,-4.733643,2.870562,1.068220,-8.776236,5.580019,0.418495,-7.652797,-5.356042,4.219777,-7.444662,-2.472347,-1.959300,-6.580073,-8.310423,3.738888,1.154703,0.428334,-0.871220,9.792786,6.969650,-3.998792,4.416086,0.571993,-9.963531,-5.644233,0.710050,-2.774790,2.097228,-8.000452,-0.165706,-3.811134,7.294520,2.667883,9.025158,-3.381811,2.244898,6.073296,-0.406642,-9.402698,3.479046,3.378476,3.507925,4.134054,-1.830549,4.516562,4.300892,-1.416634,0.304427,-5.092437,-3.722595,9.988639,-8.640761,0.703182,0.942352,9.795265,-0.506179,6.531276,-9.893525,-8.063317,-8.331633,-2.258796],[7.911805,-2.064188,-5.374390,7.874718,6.616148,-3.154073,4.495762,-4.252178,3.502847,-4.618753,8.076677,-7.916703,-2.769233,-0.250822,-7.709746,-2.116471,-5.469169,-9.518341,-3.128970,5.798357,-2.500483,0.964696,1.790642,-1.096061,2.861718,-2.236665,-8.434332,-5.547509,7.209398,0.444515,5.608237,-9.623486,-4.125980,-7.985664,-6.245400,-8.759444,2.677375,6.518608,-4.668331,-5.366722,-4.240539,-0.275202,9.729223,0.963868,7.295023,-6.810877,-5.775810,-7.186819,6.788295,7.809366,7.836662,-8.383917,5.095453,1.542216,9.732539,8.178054,2.706129,-4.358981,8.445834,7.485593,-7.079659,4.404915,-8.316068,4.788190,4.595961,-2.483077,-4.212775,4.489152,-5.929817,7.329246,-4.497829,7.398981,-1.603752,-7.341350,6.224199,0.423988,3.520800,-3.968594,-9.246742,7.348074,2.979188,-4.210059,-7.573980,3.523850,5.861285,-6.591759,-1.047218,4.738867,5.199807,-8.235406,4.054821,-0.774131,-5.510982,0.574652,-1.352874,-3.990202,-1.618370,-5.272580,6.781260,1.841928,-9.346319,-2.287605,3.761264,-8.527480,-3.499554,6.851184,-1.407415,-6.666518,-5.981359,1.079634,7.181301,-1.722980,4.810093,-8.902855,2.092753,7.035159,-2.261866,-6.947736,7.569296,-3.434391,0.125762,1.942985,-4.747233,-8.976691,4.350299,2.067886,-4.276362,-0.599759,-9.406186,-0.943488,-2.962824,-2.664111,5.475784,-4.358562,8.683107,-4.586066,-8.243182,-0.172576,-4.650212,-0.887653,-8.748053,-3.960829,9.204420,-2.602863,6.336376,5.251964,-6.485326,-6.960486,-0.925981,-3.852256,-8.018031,-3.287076,0.500936,8.034957,-8.977423,6.474093]], dtype = "float64")#candidate|5214|(7, 156)|const|float64
call_5213 = relay.TupleGetItem(func_1528_call(relay.reshape(const_5214.astype('float64'), [3, 364])), 1)
call_5215 = relay.TupleGetItem(func_1531_call(relay.reshape(const_5214.astype('float64'), [3, 364])), 1)
func_4818_call = mod.get_global_var('func_4818')
func_4819_call = mutated_mod.get_global_var('func_4819')
call_5229 = relay.TupleGetItem(func_4818_call(), 0)
call_5230 = relay.TupleGetItem(func_4819_call(), 0)
output = relay.Tuple([call_5170,call_5196,call_5201,var_5202,call_5213,const_5214,call_5229,])
output2 = relay.Tuple([call_5171,call_5197,call_5203,var_5202,call_5215,const_5214,call_5230,])
func_5231 = relay.Function([var_5202,], output)
mod['func_5231'] = func_5231
mod = relay.transform.InferType()(mod)
var_5232 = relay.var("var_5232", dtype = "float64", shape = (2, 704))#candidate|5232|(2, 704)|var|float64
output = func_5231(var_5232)
func_5233 = relay.Function([var_5232], output)
mutated_mod['func_5233'] = func_5233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4818_call = mod.get_global_var('func_4818')
func_4819_call = mutated_mod.get_global_var('func_4819')
call_5242 = relay.TupleGetItem(func_4818_call(), 0)
call_5243 = relay.TupleGetItem(func_4819_call(), 0)
output = call_5242
output2 = call_5243
func_5260 = relay.Function([], output)
mod['func_5260'] = func_5260
mod = relay.transform.InferType()(mod)
output = func_5260()
func_5261 = relay.Function([], output)
mutated_mod['func_5261'] = func_5261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5279 = relay.var("var_5279", dtype = "float32", shape = (16, 1, 16))#candidate|5279|(16, 1, 16)|var|float32
uop_5280 = relay.sinh(var_5279.astype('float32')) # shape=(16, 1, 16)
var_5287 = relay.var("var_5287", dtype = "float32", shape = (16, 15, 16))#candidate|5287|(16, 15, 16)|var|float32
bop_5288 = relay.less_equal(var_5279.astype('bool'), var_5287.astype('bool')) # shape=(16, 15, 16)
func_1358_call = mod.get_global_var('func_1358')
func_1360_call = mutated_mod.get_global_var('func_1360')
call_5293 = func_1358_call()
call_5294 = func_1358_call()
output = relay.Tuple([uop_5280,bop_5288,call_5293,])
output2 = relay.Tuple([uop_5280,bop_5288,call_5294,])
func_5304 = relay.Function([var_5279,var_5287,], output)
mod['func_5304'] = func_5304
mod = relay.transform.InferType()(mod)
mutated_mod['func_5304'] = func_5304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5304_call = mutated_mod.get_global_var('func_5304')
var_5306 = relay.var("var_5306", dtype = "float32", shape = (16, 1, 16))#candidate|5306|(16, 1, 16)|var|float32
var_5307 = relay.var("var_5307", dtype = "float32", shape = (16, 15, 16))#candidate|5307|(16, 15, 16)|var|float32
call_5305 = func_5304_call(var_5306,var_5307,)
output = call_5305
func_5308 = relay.Function([var_5306,var_5307,], output)
mutated_mod['func_5308'] = func_5308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_5319 = relay.TupleGetItem(func_2858_call(), 0)
call_5320 = relay.TupleGetItem(func_2859_call(), 0)
output = relay.Tuple([call_5319,])
output2 = relay.Tuple([call_5320,])
func_5333 = relay.Function([], output)
mod['func_5333'] = func_5333
mod = relay.transform.InferType()(mod)
output = func_5333()
func_5334 = relay.Function([], output)
mutated_mod['func_5334'] = func_5334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2559_call = mod.get_global_var('func_2559')
func_2560_call = mutated_mod.get_global_var('func_2560')
call_5341 = relay.TupleGetItem(func_2559_call(), 0)
call_5342 = relay.TupleGetItem(func_2560_call(), 0)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_5345 = relay.TupleGetItem(func_2858_call(), 0)
call_5346 = relay.TupleGetItem(func_2859_call(), 0)
output = relay.Tuple([call_5341,call_5345,])
output2 = relay.Tuple([call_5342,call_5346,])
func_5347 = relay.Function([], output)
mod['func_5347'] = func_5347
mod = relay.transform.InferType()(mod)
mutated_mod['func_5347'] = func_5347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5347_call = mutated_mod.get_global_var('func_5347')
call_5348 = func_5347_call()
output = call_5348
func_5349 = relay.Function([], output)
mutated_mod['func_5349'] = func_5349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4615_call = mod.get_global_var('func_4615')
func_4617_call = mutated_mod.get_global_var('func_4617')
call_5364 = func_4615_call()
call_5365 = func_4615_call()
output = call_5364
output2 = call_5365
func_5368 = relay.Function([], output)
mod['func_5368'] = func_5368
mod = relay.transform.InferType()(mod)
mutated_mod['func_5368'] = func_5368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5368_call = mutated_mod.get_global_var('func_5368')
call_5369 = func_5368_call()
output = call_5369
func_5370 = relay.Function([], output)
mutated_mod['func_5370'] = func_5370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_577_call = mod.get_global_var('func_577')
func_579_call = mutated_mod.get_global_var('func_579')
call_5376 = relay.TupleGetItem(func_577_call(), 0)
call_5377 = relay.TupleGetItem(func_579_call(), 0)
func_1852_call = mod.get_global_var('func_1852')
func_1856_call = mutated_mod.get_global_var('func_1856')
const_5395 = relay.const([1.872898,-9.265198,-9.618323,0.716105,-2.718156,2.346277,-5.946730,-7.996737,-9.933917,9.634668,1.494922,-0.175879,-6.740466,5.598059,9.132364,-9.854624,-6.121816,-6.929556,2.314293,-2.119400,-2.022508,-5.519224,7.314833,9.452826,9.325823,-9.075784,-2.051086,3.240758,-9.756011,-6.063544,0.503872,-3.644811,8.043561,-6.532633,-7.530084,2.523678,-5.512614,9.772101,-9.585444,0.135605,3.333807,-6.416071,-5.570625,5.385569,-4.921156,3.687765,-2.426922,1.531665,-9.874663,-2.169466,-0.506224,3.912391,0.743866,8.450586,9.081609,2.404906,-9.234213,9.923927,9.653752,0.523073,-6.145280,9.257090,4.728064,1.455866,-2.555122,-0.996718,1.366880,4.706020,6.658884,-1.841198,2.424053,0.392390,4.539268,2.535247,0.778288,3.219528,2.258122,-5.181272,6.329210,-8.539531,0.684994,4.369355,5.882126,2.501359,0.497815,2.152569,8.825832,-5.910791,9.240346,2.434464,-1.722392,7.532205,4.789209,-3.010750,3.926610,-1.283525,-5.972607,6.934556,-7.835891,-1.290059,-4.136134,6.111264,-3.218069,-8.166831,8.605307,6.347986,-4.831449,2.341935,-7.139834,2.872618,-1.101515,3.070242,9.291842,-8.981964,2.977191,2.087237,4.231301,-4.165112,-7.135594,3.558241,-3.156591,2.413369,4.711644,0.333948,5.015724,6.732105,-5.891016,-7.034913,2.979317,-1.439660,6.010149,-7.901095,-5.975236,-5.809414,-4.548340,-8.823130,-5.500811,1.457402,-0.665390,-6.795877,5.356450,1.527188,-3.373188,3.853342,0.199828,-8.763678,1.738376,9.278046,1.552947,-0.755465,1.133005,7.307654,4.028801,-9.433858,2.031045,9.348306,-6.337428,-3.504584,-3.697728,8.068070,2.219653,-2.068908,-9.442842,-1.300131,0.601191,3.275873,9.166404,1.416309,-8.327712,-9.428728,-8.757633,-9.687620,3.142305,1.071771,3.409259,6.818277,-4.334512,2.349104,7.648181,4.169710,6.647250,9.133219,3.585618,2.666993,-4.680955,2.481929,2.966280,-0.115548,-6.899936,-4.337644,-3.322813,9.815046,1.327570,7.656471,-9.147142,3.232698,-5.064598,0.030110,4.145924,4.526551,-5.308660,-3.731860,-2.655392,-9.581176,-1.430917,-0.730551,-6.147848,-8.197652,3.598182,-1.582185,-4.737735,6.510710,6.460362,-5.139095,8.214934,-1.532108,-5.802173,6.125479,5.910358,1.016117,-9.917880,-1.342905,9.478692,-0.832888,5.458304,3.021194,-3.723462,-9.207740,2.034750,1.058990,-6.432343,-5.419471,-4.897799,1.383483,-7.740062,-0.768754,9.149416,4.547091,2.237275,8.116800,7.747904,-8.869685,3.228567,6.150999,3.161339,8.777646,-6.706041,-1.438617,5.900752,7.723981,-7.583708,-9.246824,-6.318619,5.591073,2.828301,-2.456002,1.906183,-0.719409,6.685495,9.638949,-6.829266,-5.868308,-7.592708,-4.480759,6.906247,6.874444,1.737274,4.198808,-6.449618,2.591320,6.030681,-0.547646,-3.678645,3.792448,-5.542124,-4.364827,1.555794,4.649762,4.079520,6.290569,6.756690,-8.701017,-8.699865,0.164662,-1.016071,-2.680236,-1.331686,-5.429764,3.204353,4.837718,-2.733449,5.806348,-7.034140,-1.203460,-2.036225,-4.783877,-0.673242,-8.607943,-6.679949,9.117484,-5.287958,-8.913193,-1.982365,0.610413,-7.449330,8.353238,-3.307772,-4.971535,-5.987584,-1.763522,-4.603660,-6.713491,6.018478,4.482098,-5.169457,6.369748,-6.843263,-8.261110,-6.987007,9.801356,-5.268961,-0.576653,1.464735,6.866348,6.076243,-5.889878,2.455154,-1.000573,7.002975,-4.414638,6.572602,-7.122344,-9.479747,-6.208002,-8.255934,5.143132,3.780125,1.038147,4.288349,-9.597946,-5.167797,-7.035773,5.154583,-1.024211,6.406024,7.986002,-4.266638,-8.371559,-4.206115,-4.774198,-6.558075,6.469879,7.619887,-5.127054,4.478284,9.541886,7.524085,9.049908,-0.849173,8.907022,9.635019,-3.063456,-7.572417,-5.828017,-9.017490,6.949336,-6.655881,-2.278460,4.021038,-6.423137,4.455572,-8.864251,-5.763086,6.732991,-5.802786,-7.651930,0.595423,2.436911,3.270306,-2.052036,-8.550156,8.909227,-7.590242,-4.684560,-8.495582,2.743063,-7.249835,9.867432,7.247663,-0.490860,0.823259,2.867083,9.407115,3.471035,-3.633760,-7.136204,3.514824,-8.529002,8.233779,-7.015300,8.407489,6.527120,3.317517,-4.753724,-2.154899,-2.151299,3.167775,-5.287610,9.370814,-9.377860,-1.095360,-7.279769,-6.667188,2.904276,-0.253905,2.096919,2.999306,2.301371,9.216642,-6.433758,-1.951966,-1.856697,-1.040232,7.391652,-9.755279,-8.143511,-8.910543,-2.680637,1.242265,9.989356,7.250263,1.975497,0.729068,-4.873423,3.567153,-1.020680,9.738511,3.780455,-2.249641,1.083377,-2.087504,8.897784,0.655046,3.338677,9.236124,-6.625437,-9.057634,-3.845758,-2.405816,-8.473499,7.753869,-3.375981,2.286944,-5.998747,-6.411062,-9.512945,4.735984,1.437500,-6.261814,2.864076,1.511836,-0.387665,-0.507592,-4.437226,3.511906,-5.888066,1.928434,-5.691826,-5.532537,-5.214025,-8.499144,-6.209357,-6.431879,-4.121795,-8.273374,0.023605,6.072512,7.402524,-4.204773,0.194063,1.895967,-4.895102,-4.586628,1.310408,6.080346,5.654964,6.810863,-7.093243,3.983111,-8.581543,-6.867075,-4.322471,6.279999,1.414380,0.054882,-5.074103,-5.630381,2.830923,8.428731,-6.791549,4.444506,-4.179190,4.744270,-7.725875,-5.485134,-2.198269,-6.966467,-3.715573,3.304087,6.167396,-5.835538,0.360400,-1.304878,1.603032,8.189926,3.571097,2.691821,9.637554,-0.434864,-2.251904,-7.047066,7.457151,4.603476,9.558771,-8.573636,6.068257,-6.322471,3.254756,6.779196,-4.271177,-5.899914,0.799026,9.944763,-7.158657,9.185149,-2.816910,-8.930663,-5.822939,-9.934371,-7.157160,1.688237,3.641439,-2.698190,-7.383089,-7.833730,-8.114963,-3.870794,-8.939608,0.326959,0.490640,5.627729,-3.536869,-9.465835,3.652953,-7.893314,4.247630,0.721771,8.660262,2.757549,-6.042427,-1.503381,3.932059,-7.773436,4.549527,-1.752093,-1.043999,-0.029254,4.425445,-3.170457,2.771553,-7.570247,-8.966902,-3.478555,0.299844,3.674656,5.193923,9.518030,7.741383,-6.261056,5.729303,2.218572,8.560953,-6.618529,-9.568142,8.222591,-8.154104,-3.791037,-4.690252,-8.647160,8.247289,0.820041,-9.499997,9.595161,-8.300998,-9.301839,-5.549691,-9.146790,9.172679,9.133335,2.301086,-6.879793,-0.648468,-8.067337,5.370883,4.976739,-4.469883,5.857378,3.548436,-7.664104,-4.637975,3.946291,5.525911,-6.989328,-6.297545,-2.062495,1.544218,3.923265,-1.580124,-4.668012,4.402087,-6.566452,-5.541871,-1.105904,-7.748424,1.442196,2.826390,4.165962,-7.986988,0.235823,1.422049,-2.373020,-6.876022,2.047395,4.432828,-3.441549,9.015070,5.681947,-0.259496,9.090309,-3.417236,-7.038496,8.511388,-5.230275,2.912509,-9.851623,-0.414973,7.093387,0.906924,7.649962,-4.350447,1.497209,-3.197360,4.322611,-8.343343,5.945091,-3.614118,-7.564056,6.656215,3.400361,-7.841201,-0.548197,3.568485,-7.379066,-8.400835,2.554052,0.167154,-5.950292,8.076019,4.521487,-4.694713,2.554761,-8.450427,-9.742259,-1.942938,-1.307317,3.356039,1.925163,2.196658,5.105859,4.717506,-5.830779,2.944845,-0.967768,0.427902,-9.926288,-3.788627,-0.873416,4.564839,8.446965,-4.770452,0.130667,-8.836575,-1.667130,-3.452176,8.869499,0.327649,-8.617184,-5.737051,0.736301,-8.493133,7.358207,0.940417,3.338324,-7.822573,8.473077,9.719286,-4.269061,5.261790,7.292093,7.604017,-0.051795,-4.845132,9.939560,1.655229,-2.740008,6.504754,5.348909,8.763310,0.995271,7.887101,3.236336,0.907849,-4.771155,-3.979920,-9.942458,-4.352470,-9.728952,-0.937845,7.008039,5.350088,9.640044,3.113680,6.208975,-6.152465,-8.970778,5.244966,-6.487872,8.049636,-5.624422,-8.943861,2.227733,5.766524,5.159381,-9.883046,6.323836,5.226152,-1.820278,9.029712,9.194172,-0.897771,5.871530,9.122048,4.196285,-2.301490,3.401392,-6.904209,7.594593,-7.784690,5.960939,0.277027,-4.977091,-7.368406,0.183390,0.321974,2.603753,-5.847058,3.871863,-5.158644,0.077685,-2.282919,8.723578,7.755835,-2.381941,6.522702,-0.097663,7.080471,7.819161,5.421389,1.073439,-5.488566,2.224183,-4.427544,-6.743501,7.695149,8.393096,-5.994108,-9.896635,-9.873631,-8.098554,1.014562,-2.856027,6.506315,-9.029485,3.700559,0.179349,-9.344765,-2.171323,-4.987721,9.012044,-7.972257,5.398704,1.398865,3.759985,7.568059,4.942233,-0.857540,5.522525,-3.316633,2.266311,0.953484,5.447621,4.053604,-0.786527,-3.685341,0.620193,8.030879,-5.032304,-7.755963,-4.893269,8.671278,-4.792482,8.335056,6.938249,7.187637,2.591193,-4.619978,-4.363445,4.208562,4.430266,-8.902760,-4.533699,6.493248,-8.581611,-9.037425,5.470434,8.452666,-1.883608,8.985025,-5.818906,-6.672552,-0.909097,-8.759034,-2.190689,9.542689,0.435373,-8.013788,8.560755,-7.564639,6.622435,-0.172913,-3.972472,3.455469,0.140063,2.509592,5.192202,5.167157,-3.215797,2.681227,5.004670,-0.896148,-2.563643,5.927895,-7.986129,-8.298867,-4.800547,9.925522,-4.564070,0.854386,1.487247,3.356253,-8.293287,-5.921514,-1.267990,3.646566,0.398762,-0.626178,-2.111766,4.274751,-5.395423,2.068969,3.877315,8.922047,8.730014,8.747951,6.292728,9.868749,1.226191,-2.208536,9.449287,-6.125606,5.817031,4.320232,-1.526704,7.797996,-7.217111,5.478509,8.412761,9.741799,-1.769952,8.063319,7.891459,8.513002,6.907363,-3.841021,-8.740630,5.928784,3.096223,1.484786,6.565200,-1.993318,9.615913,6.929238,4.052732,4.490893,9.450289,9.788783,-8.201369,-0.963082,7.011064,-9.693157,7.585155,3.305759,-5.794377,-7.744201,6.802553,0.626768,-0.393144,9.635441,5.622325,4.104716,-4.024594,5.396238,-7.426536,-4.157570,-2.374967,7.974441,-7.011400,2.691740,0.505185,-6.609012,-7.126166,-8.344548,4.504058,-1.319000,-7.345876,0.498129,2.699611,2.848826,-6.212083,2.711061,1.962486,-5.338966,4.751120,-0.910818,2.420280,-4.579576,4.764334,6.523549,-0.262450,5.804431,2.707556,8.964693,-9.553702,-3.168722,-8.925535,5.566020,-5.344320,1.994844,6.281334,9.068417,6.078125,0.278325,-0.435828,9.621863,-3.015069,7.658761,4.221149,-1.930515,-1.787258,1.677963,-5.505048,-0.453772,-2.969425,7.164640,8.762214,6.219142,-8.683510,4.290974,6.380357,6.878173,-4.314606,7.238687,-4.006943,8.800454,9.204077,2.181483,0.429708,-2.874853,-0.401645,-7.494948,-7.252904,-0.966369,-6.591338,8.093757,-7.179992,7.134025,-8.394728,-6.123291,2.260396,7.040456,-7.908355,-0.691577,-0.104326,-7.421104,-6.605217,-5.494010,-7.964182,9.992051,1.902922,-1.456293,-8.341113,-8.969533,-3.234656,7.387950,-5.926903,-3.291676,4.063116,-4.861473,-4.159794,-4.075694,8.465202,8.359031,6.484277,-6.430553,-9.109577,-1.015296,9.781714,3.115217,-1.010182,7.426295,5.291832,4.703573,-5.496034,-6.561621,-1.336146,-5.017936,9.289066,9.439305,-5.278545,3.234891,-0.913188,0.235310,-3.645014,-9.828817,6.614481,1.903738,3.044342,-5.245146,6.022858,-0.065798,8.414887,4.817402,0.177780,-9.448087,9.683732,-2.125892,4.875187,6.418096,-8.755005,-9.996854,6.475256,-9.096546,7.629923,-8.788206,0.213391,-1.585996,3.450729,8.100237,5.122971,4.976013,-1.394298,-4.194758,6.978835,8.067658,6.194184,-8.615109,-3.594840,-4.323120,8.599932,-0.095949,4.158860,9.965820,-1.747568,2.629956,-0.389260,-1.709418,-6.771008,7.186869,-4.792023,4.434758,-7.724678,-9.685296,-8.237639,-7.972317,-4.546778,-1.950506,-4.204556,-9.645510,3.072054,-8.949933,-2.858935,-9.815583,9.840202,5.238985,-3.335974,-2.485641,-6.438729,0.855007,2.609811,-0.941508,-4.638401,9.595492,-2.430190,-9.064529,-8.990515,-4.991015,9.376458,6.892714,-8.855735,9.054667,-0.936327,7.926608,-5.981276,2.356847,6.520882,1.776803,3.918440,-3.138210,8.994689,1.960193,2.878379,-9.593273,-7.235027,7.540002,-4.093589,9.728245,-8.016622,2.339378,-9.335417,-3.159571,-5.770558,9.052941,8.504996,-7.825618,-6.048999,-1.234324,4.270563,3.174059,-3.052902,-7.191386,4.140144,1.626000,-2.262562,-0.446832,-0.510391,-9.719889,2.543461,-8.162453,1.416287,8.546667,-4.383967,7.510760,-0.158575,6.902369,-3.519299,-5.042851,6.225839,7.696920,-3.573591,-2.027859,6.980047,-4.914063,0.195767,6.422412,1.352717,-6.874216,-0.709066,7.477191,-7.516412,6.513173,-1.140709,-0.818561,-0.824518,7.715424,-8.257013,1.812728,3.820865,-1.660125,-6.365412,9.064360,-8.461590,2.693905,-6.777857,6.719240,8.345734,3.202163,-4.758611,6.642234,8.832836,-8.731378,9.584593,6.135866,6.829895,9.234441,4.265971,2.607942,-5.358262,-8.343063,8.993425,-5.240367,9.402121,-1.926548,9.512280,-9.666975,-0.685191,-7.576473,-9.263093,-1.428671,8.562312,9.316989,8.121176,-2.312812,5.001773,-2.738475,9.327660,1.919164,-6.816853,-5.857937,5.139870,-1.830095,8.100527,8.650473,5.048666,0.600464,4.832478,7.910937,7.031773,3.026363,9.474778,0.492157,-0.511441,3.507830,-4.646560,-7.212554,-4.513786,-8.890103,-3.939470,0.089086,0.605874,-8.656688,0.185408,4.879293,-3.154471,2.401408,-1.220243,-7.200060,8.100660,8.395525,0.169835,7.572112,2.630954,-5.889652,-1.982587,6.752878,-5.056861,-6.091716,1.674310,9.052416,-0.078472,2.549652,3.955718,4.248280,6.148330,1.710627,6.938221,-7.291211,-3.820221,-6.576484,-3.284246,-8.662182,2.825481,-9.833614,8.568842,-2.970814,-9.710946,-7.923721,2.504957,-9.302375,9.702375,-7.796034,7.320892,2.853850,0.033650,-1.864149,9.833361,-1.666297,0.782005,3.228479,-0.190243,8.090768,-3.566685,5.979160,7.659369,-1.662808,0.199844,5.634559,-8.381007,-9.212147,-6.275879,7.035127,3.990970,4.448603,4.935437,3.522382,-7.481603,-9.072745,1.890325,3.914006,-3.983409,9.570761,-3.475740,-9.656336,2.148540,-9.835803,2.678356,7.154959,5.088317,1.151485,5.561943,4.804467,5.709342,-8.692357,3.123876,-9.768275,-6.399373,3.723354,-9.198485,3.103187,-8.089273,-6.745255,1.646932,-8.377725,-8.830483,4.433144,4.703070,2.268365,1.513554,0.169187,5.075446,-4.273857,9.859725,-3.718092,6.076770,0.679608,3.484101,7.221844,7.813490,-6.260670,6.497385,2.455901,-9.637231,-8.792467,8.420260,-9.398846,7.010503,-6.627752,-1.253688,-6.504666,-9.333321,2.540034,3.864641,-2.492487,-8.163094,-3.126844,1.849963,-9.148055,2.622935,7.419516,-9.065781,3.226923,-9.672939,-4.114274,9.525415,-1.380419,-1.400690,5.354096,-6.056577,-8.002007,-2.121229,-4.064983,4.452317,9.377132,9.023086,9.628135,-6.981267,8.450696,-6.036633,6.245346,6.419621,5.149173,0.006815,4.841457,-9.462295,3.508946,9.533766,-3.404352,-0.667237,4.226998,-9.515537,-7.930134,6.324857,6.585268,7.170326,3.436332,-7.102628,4.175479,-2.860486,2.004058,-9.140618,2.384445,6.096678,-8.097985,-9.928482,8.577690,-7.143338,8.465964,-5.661002,1.589901,-5.477695,-0.082414,6.611816,-5.260182,-0.512989,5.782017,-7.166918,-0.371180,-4.269430,-1.082110,-7.148838,-1.712377,2.856646,7.300858,-1.651279,7.761330,2.767921,-2.223543,8.051935,-7.227680,-4.019471,9.403405,4.635759,-0.663914,-8.900929,-6.783815,9.798891,-1.331682,-1.030062,-1.249098,-7.420119,8.381170,0.251647,9.497989,2.600212,-6.387183,1.952033,-5.687026,-1.507177,-8.884997,9.774369,5.923553,6.620322,6.642858,3.052220,3.311295,-8.048269,-1.437473,-3.050420,-1.878438,8.994483,5.591001,-2.021261,3.113960,4.274718,-9.864096,-1.932899,2.408700,5.927447,-1.130191,-0.812209,-0.205028,-6.453236,-1.543569,-5.465980,-1.933286,2.906375,-7.836799,-8.340648,-0.855339,-2.212139,-3.504810,2.054783,-9.279300,1.186881,4.903799,-7.940179,-1.521860,-0.917488,0.035694,6.776692,8.875775,-8.086965,1.656106,0.589520,-5.689285,-3.511758,7.503872,-0.974746,-4.959181,-2.020023,6.867451,3.099670,5.867015,-5.014087,0.474108,9.920770,-1.312258,-4.891446,-3.108092,-6.317733,4.694518,4.312747,-0.193368,7.434032,6.373108,-7.422861,-5.038901,-3.438824,-8.962393,6.584448,4.191971,-2.242114,-1.104920,8.674399,-2.256512,8.231602,-4.175880,-3.875713,-5.302915,8.083826,9.876604,-9.064804,5.826387,-7.114958,0.718987,2.019622,-7.346738,-5.485821,2.922924,3.534763,6.494180,3.935200,4.439080,-1.334579,3.313610,-6.572793,-0.573295,8.730291,6.482641,9.096419,8.270847,9.616102,-9.050713,-4.621944,3.188037,9.124574,-1.763975,-0.721387,8.378136,8.435072,-8.784901,4.661804,-7.887121,9.251555,-5.168887,-0.879373,5.346222,0.129305,7.057527,8.639169,9.723103,-0.904529,-6.439159,-7.160532,1.145583,-6.693337,7.030813,-9.782892,-4.732595,3.210942,-7.152476,-2.307083,-5.560106,1.807459,2.647278,-1.690428,-3.456248,-2.473465,-6.866133,-8.857415,-5.340234,0.273047,-2.514056,4.518329,6.134957,-5.683891,-4.007939,-5.862919,-6.767772,4.022967,-5.966035,4.309708,-8.365949,5.416426,-8.714499,-3.517184,5.920768,-4.139856,-3.623862,-7.518150,-1.420626,9.382058,-0.058771,0.534919,-8.176786,-9.619197,4.061629,8.748253,-5.001107,-3.516713,-9.120786,5.544229,-2.208291,7.131357,-3.576589,5.673141,-5.719260,6.674879,-8.234052,-2.397423,7.298569,3.018579,-4.004036,-9.182817,-6.889287,4.931086,-1.752152,-3.409046,-7.689454,7.422498,6.980966,6.441678,1.821692,-4.626509,-8.110907,-7.944884,-8.203501,-4.922338,-0.539868,2.499480,7.922867,2.184039,1.653014,-8.173390,-7.930687,-9.446538,-9.084374,0.435634,7.453541,3.586598,-1.023264,7.698359,-0.705603,0.996556,8.164842,6.130803,3.913514,-0.919894,-8.846670,-7.435198,-7.680986,-1.719819,8.249615,-0.184388,-8.526254,-3.576421,-8.095301,3.668758,9.458736,9.903524,3.063222,4.495687,-1.386703,6.985241,-7.031343,5.964134,3.393216,-0.932260,6.709032,1.801003,-0.021881,8.843101,0.151626,8.227547,2.884394,6.041818,3.093902,-9.304243,-8.382878,-6.590689,2.011281,3.329314,-4.078915,9.677053,6.303766,0.202407,-8.266961,-7.329733,7.545501,-8.569872,-3.254795,2.838828,-2.986593,1.073226,0.261542,-8.376175,7.654934,5.927021,1.234539,-9.337013,6.710566,-8.469804,-9.454760,-3.599775,2.513084,-3.551991,-9.419576,7.166354,5.551826,-4.424696,8.323020,-1.154459,-4.353590,-5.315635,-9.087685,-9.104266,-9.764353,-0.554013,7.686582,-6.384407,7.836253,4.933942,-5.115727,7.186159,8.843875,-8.068362,-3.306694,-1.916301,2.837517,-7.046994,3.763913,3.251750,8.674496,-2.731462,-1.313213,0.736398,0.371793,-8.513261,-1.197535,-4.298945,7.569458,-8.242019,3.722013,-9.133806,1.652433,-4.451233,-1.635331,-0.923275,1.963663,-2.573085,3.708533,-7.158154,-4.112468,-0.304339,-8.632547,1.890841,9.402664,3.647226,-2.705129,2.823787,-8.331824,-6.450596,-3.388189,-9.492058,0.012677,5.343598,3.356586,5.149777,-9.633398,-7.483568,-7.470869,-5.960677,5.428892,-6.002185,-4.137009,4.596412,-6.877174,9.559047,-6.762655,-5.526705,-3.963615,-7.451210,8.729155,-3.836913,7.120914,-2.026437,-8.494920,2.561920,-5.173570,3.229122,-0.371736,6.683196,-8.347115,0.458165,5.941533,-2.742704,2.566552,3.397064,-2.790148,8.747423,-0.848563,-3.180092,-8.677678,-5.800132,1.733878,1.192805,-8.026753,-5.522004,2.141356,9.744608,-9.095370,9.505250,-9.418838,-7.009121,-4.093283,-3.187594,-6.517987,3.892461,-8.767007,0.614791,1.685651,0.262972,-9.972742,-1.839766,4.667129,-9.164505,6.890133,-4.925502,-9.389499,-0.044162,-2.716289,1.451048,4.730838,1.809027,-9.694962,-0.446846,-7.517138,8.822608,3.542889,-5.379838,8.891283,-0.986513,-1.778086,-7.474607,-2.446905,5.649239,2.499907,0.814664,4.689636,-5.915422,9.774015,9.561335,3.150606,-6.346894,-1.066764,7.671416,2.325901,-0.477306,-8.902762,-8.503476,-7.495352,1.662887,-6.120089,-7.319591,-2.428391,8.979473,9.074216,2.014855,0.530830,-7.612238,-5.556395,4.913265,4.588689,-4.275530,-4.534101,-1.167465,-8.419580,-7.667039,-9.533668,4.868112,-5.869642,5.432325,1.282229,-5.325907,-5.927932,6.977717,-9.801040,6.719700,-6.721099,-1.269566,-2.759325,0.310552,-3.273137,-9.396613,9.125183,9.407710,-5.800506,1.863076,6.376317,5.579726,-3.339684,8.215131,5.185958,3.407698,-0.693042,4.820483,-6.156545,3.046539,-6.765495,-6.121333,7.340378,0.227430,-1.582117,-4.324475,-2.688446,4.067394,-5.206978,-4.213408,6.869129,4.910535,9.966891,7.730353,-0.665952,-9.208959,-6.757212,-5.465405,3.644037,2.274594,-5.724476,3.414332,1.142319,-7.035158,9.354539,-9.727490,-3.499894,-1.745207,-2.038536,0.744669,8.733501,1.706281,-2.016033,8.775903,-5.060719,9.747629,-0.710967,6.382229,-7.984797,9.442824,-0.472990,-6.393973,-2.919101,-0.320712,-8.979048,1.255904,-0.882020,8.710644,-4.819946,-4.820949,-2.041643,0.698906,-1.660238,-7.527081,-8.974524,3.463428,3.914208,9.637589,-5.717069,-6.168750,-5.002857,-9.432673,4.427365,7.290524,0.256391,-9.827637,-5.598189,-1.261046,-7.453253,2.490025,3.805866,-7.842930,-1.537889,-3.362801,7.066252,-2.216732,-6.085287,-9.049106,-4.596719,0.130617,0.899827,0.628908,5.778439,1.244868,2.001339,6.789933,7.885877,4.174573,8.071684,-7.569022,1.271367,-9.916847,-2.148457,0.430267,1.184882,-2.242543,-1.362741,-9.436634,3.198925,9.854265,-8.003232,6.679846,-0.854673,6.129011,-8.835477,8.239598,-8.649333,0.921308,-1.944659,-1.938156,8.236533,3.282797,-0.165285,-3.818626,2.671833,-6.649802,-2.442870,0.261091,0.695478,-9.399348,-4.792726,9.240775,-5.500234,2.669333,1.368472,-7.970846,-3.641862,-6.208782,9.908858,2.544885,-8.940704,-3.545882,8.674589,-9.928520,-1.045243,5.790858,-3.551981,-3.911615,8.607947,5.750123,7.073530,-8.526433,1.755540,-8.204326,6.399755,8.254269,-9.087268,-6.147352,4.799128,-9.850657,8.707020,2.768215,-5.632761,-1.052343,3.071005,-8.693981,9.641043,0.230700,2.997759,0.946320,1.387086,-4.839648,-6.003225,7.301845,9.181891,-7.348891,3.508742,-8.561247,2.297614,-2.122753,2.876466,3.876233,0.575158,2.739867,-2.955211,2.095656,-3.099132,3.534520,-4.539877,-1.096841,-6.801804,-3.269571,-9.163184,6.081819,-5.334907,7.172643,-8.070905,-5.329117,6.043731,-4.344780,9.949102,9.501009,-4.578315,-6.660512,2.695705,-3.585214,5.620984,-3.427558,-2.593591,9.628705,1.907620,-9.234682,4.739934,5.418082,-5.553608,4.618002,8.132516,5.328365,8.375854,-3.570294,0.567418,9.596903,7.865862,-4.438385,5.430718,-7.510591,-3.077327,3.835585,-4.403757,-8.126558,-8.440219,-7.481936,-6.154655,4.338673,3.074486,3.653150,3.668172,-3.707508,-0.969274,-7.741234,-7.956864,-6.771575,8.223437,1.015373,-2.317108,-0.665869,5.978276,-6.797612,7.267690,3.656407,3.905332,3.016822,3.538222,2.317173,-6.055316,-4.483647,5.486067,-8.786543,-3.798194,-9.288310,6.491706,1.440557,2.792056,1.154061,-4.411289,8.470436,6.239817,-9.652085,-1.828767,-3.234476,1.665948,-5.653136,9.894878,9.585675,-2.848200,-6.973945,-9.322228,-0.425162,3.237521,-7.059792,-7.461635,4.430488,-6.042194,9.313127,8.628870,-3.148067,-4.960647,4.840631,1.162788,7.688493,-0.691496,6.946877,2.256616,-2.069795,3.133410,-0.758432,8.754999,2.528833,7.906722,-8.189485,-6.797618,6.878389,8.433358,-3.125094,1.599578,-6.125433,8.698684,5.961282,1.355307,5.215557,-8.902568,1.340272,1.117531,-9.265891,9.642777,-2.267209,4.038218,-7.826775,-4.017142,4.135607,-9.588850,-0.485191,8.359904,-9.452589,9.539883,-9.562978,-1.930791,0.041247,-7.674845,-7.061962,4.354988,-4.743668,2.469589,9.100122,3.425008,8.646947,5.140097,-8.032895,7.975616,5.774293,-5.339932,6.180960,7.480663,9.223152,-2.120824,7.030855,-3.558301,-8.025812,-1.872205,4.706851,-4.411274,8.066324,-7.234175,-2.797606,5.470237,2.131404,9.872003,-6.697669,4.205121,5.446634,9.709256,4.479120,-2.281650,6.438721,-9.496442,-3.825329,-8.214449,-1.523868,7.589052,-2.696876,-5.186521,2.149269,-3.195771,2.876839,6.228743,3.944048,0.367563,-3.778783,-4.542634,4.675405,-9.714290,3.567644,2.251294,-0.853957,4.347499,9.819242,-0.562892,2.257024,-4.258378,-2.389212,6.657950,3.538395,4.521443,-4.264945,8.937911,-8.662658,-5.633956,-7.796808,4.610420,-8.423436,-6.847739,-7.288846,-1.376957,5.747021,-9.584068,-9.213283,-2.685528,1.037734,4.460120,3.117756,8.012581,1.741418,-5.257696,3.725246,-5.943850,-7.086331,-9.358667,6.653258,-5.812594,3.671902,-7.240598,3.870149,8.678760,-4.290990,-8.680238,-3.877734,3.090505,6.300927,0.955919,4.344193,7.038113,-4.320463,4.611235,-1.563956,0.808667,-0.979541,-3.290260,-7.002762,-7.148011,-1.474715,-7.000497,-7.628015,-2.737477,6.180691,8.779210,5.357062,-0.328929,-5.843770,2.295375,-7.823798,-3.709598,8.412891,-6.720240,6.159221,-2.729522,5.169604,-1.504736,0.552163,-8.628006,-4.064424,0.114796,-2.292235,-9.345164,5.882615,3.560580,-0.336310,6.564183,-0.067985,7.707602,-1.201257,-6.865650,-7.279031,-2.073720,4.286155,1.458036,-4.087387,-8.709114,-9.378257,7.895398,-5.077541,7.693232,-7.825107,-7.701408,-8.270199,-9.583997,-3.196488,7.567302,5.341087,-7.353263,-9.814659,6.495157,-7.523351,4.922946,-0.842609,0.950749,9.981413,4.119370,8.006984,3.076115,1.534508,-9.713019,-0.344234,-6.141558,4.231411,-9.668171,-7.434419,-4.439434,1.260097,-2.492377,-6.113912,3.734872,-0.036095,-9.155730,-4.619694,-7.137760,1.609455,4.079990,-0.186465,-1.149874,-7.530768,1.080735,-0.661905,-0.199630,4.350996,6.786641,-8.293032,4.883080,7.653258,-3.599060,2.181780,2.011546,6.903807,-1.910205,-3.317669,-0.518348,-0.431438,-3.336047,8.900704,-8.705472,8.062081,6.580784,-9.962147,-5.442206,-1.631934,-5.648625,7.018032,-7.100392,-5.397971,-4.306004,9.584924,-0.880559,-7.005092,-6.000231,9.687491,-5.613984,-4.999360,-7.615998,9.724665,-0.029035,4.437320,5.537949,-8.710281,8.815990,0.474161,-7.868207,-1.739868,-8.060944,5.886109,8.666968,0.296312,0.236113,3.890842,1.780055,-8.321702,-4.711532,-6.626450,4.514306,1.461006,3.100084,-6.915683,-4.370908,-8.497280,-6.157275,9.863386,-0.008249,0.392950,1.329170,9.647634,2.533414,-6.303939,2.975245,-0.379429,-6.269973,-9.292392,-1.938366,3.148955,9.504327,3.240378,6.235459,4.089125,3.489959,6.954288,7.583146,2.047399,-2.609950,-2.969452,-2.459758,-2.974095,2.282863,2.487876,-4.772842,-6.583606,-2.447010,9.657515,-6.109797,-4.618642,9.447239,-8.287870,-3.063398,-5.153580,-8.635024,4.394218,7.959001,2.065174,-4.294434,-3.489186,8.044536,-7.981639,-9.058184,3.581777,9.794958,-8.386086,6.180241,8.345530,8.642576,-7.421028,8.408522,-1.936423,-6.316749,3.575214,-5.249641,7.257640,-7.251609,-5.049581,1.871841,9.439835,9.576991,2.235223,9.699410,-7.442849,-8.379450,-8.366351,-7.828559,-7.815762,-2.591321,0.029074,8.988940,-3.991645,7.644960,-7.224584,-6.589685,1.802698,-8.845446,-3.220343,1.590277,-5.793207,7.574235,8.169290,3.897200,-0.736817,1.956596,1.589943,-8.328240,-6.803338,-7.836068,-6.330964,7.161033,-4.995966,8.661899,4.337012,5.726788,-1.488141,-4.101599,5.649762,-1.296049,6.298874,8.603093,-0.619561,-2.587862,1.098666,-8.598153,4.686470,5.503399,5.119176,-0.516520,-9.481931,-9.344060,-5.151197,-9.057953,-7.039968,-3.688754,7.735487,-7.588689,4.444043,-7.138216,0.525586,1.435398,-6.758029,-5.005968,6.112446,-8.482380,7.983920,-4.704916,8.856824,9.695052,2.428307,7.440445,5.147480,3.102873,-2.214722,-6.563951,-9.108726,-0.786164,-0.358743,-5.481770,3.983508,0.414977,1.326749,9.303210,0.085601,-2.343386,-0.443557,2.896297,-8.654459,-4.468418,-2.652635,-3.985212,-1.832555,-5.712984,-9.272691,-4.972941,4.990103,-0.660177,-2.205871,-2.148051,-7.668350,-5.664699,-2.586847,-1.841670,-5.165986,-7.970080,7.307706,5.551553,4.835403,9.047281,-0.208608,-1.255967,5.309845,-9.657553,-0.762339,6.822131,-3.267014,1.678552,5.911823,7.850791,-9.840417,6.429411,-9.802036,-1.038305,-5.388935,2.772355,4.954103,-8.075303,-9.953026,-8.206680,8.712301,1.467905,-5.588090,8.759437,8.307983,7.328797,-8.522843,8.634265,-4.951251,-0.009286,7.101351,9.176720,8.275770,-2.202240,6.695584,-0.294502,-3.035261,-7.985478,-1.632676,3.096395,-3.735379,-6.210614,1.489678,2.305640,2.567500,-6.796565,-4.614675,7.622056,0.565332,0.733354,1.232024,-8.420578,-1.942266,-2.692240,-5.364662,-1.820770,-1.046727,1.700016,-5.515965,8.216567,-5.026300,1.784719,-3.067056,1.889898,-5.780967,-9.386209,-5.843642,1.254036,8.985619,-2.801419,9.420987,-8.647349,4.947519,3.016437,-5.669207,1.109186,-3.597301,8.287980,8.671958,0.238030,-9.628899,1.213976,-6.213115,3.274889,-9.936758,6.084786,-6.671359,-2.014735,7.403972,5.138412,-2.458029,-0.145538,2.437507,9.479305,-9.439498,-8.564257,-4.101551,-9.351986,1.914919,-2.825020,2.029991,3.019554,0.966616,1.207042,-6.033450,8.197416,5.830678,5.341613,0.710102,6.512886,8.006090,-8.768043,-8.061476,-0.660437,-9.016995,7.616706,-3.026861,3.799202,-1.477589,-5.284965,-3.099797,-0.698656,-4.923430,-9.004433,-0.520987,3.084804,-3.390663,-9.480432,-5.310737,-1.826750,5.443098,-6.641283,-7.839771,-0.979976,-1.315728,3.263906,-7.955943,-2.591583,-4.996973,-5.469777,8.649300,-4.997654,-4.836044,-2.078532,-5.969395,2.732020,-1.739655,8.344896,-5.302545,-1.108240,9.133637,5.375032,7.931433,-0.913324,-0.497243,-2.751761,-5.498353,8.161498,3.681235,-4.288556,-4.487543,-6.153709,2.335447,-4.720289,0.057757,1.810313,-0.174936,-1.240680,-8.674743,9.727845,2.764582,-2.168760,3.673087,-3.934387,8.164188,-6.862246,5.881658,4.664247,-9.419662,-9.977289,-9.473623,-4.906045,-9.196051,-1.902782,7.312606,1.775052,6.008521,3.269192,-2.152620,-7.146409,-1.669671,6.989741,7.761109,-8.643847,-6.623527,4.508614,-9.711751,-6.141922,-9.936768,-1.640326,-1.169803,-4.425842,5.634551,-1.918164,-9.246692,-4.716023,8.931409,-3.261587,-9.481391,6.665596,0.079224,1.591020,-3.226755,-7.008177,-7.926907,3.853588,-8.995850,-5.083434,5.627182,0.869909,9.624872,-6.216535,-7.829989,1.679057,4.983310,2.257034,8.727156,1.954733,-2.195142,-9.396441,-4.837774,-1.794155,-3.025764,-7.016340,1.940775,7.996444,0.688522,-8.907627,-4.984403,-8.736303,-1.006613,-1.050363,-4.141252,1.738632,1.755672,6.244882,5.803726,-8.537852,4.225732,2.101751,6.894413,8.855614,-5.761162,-2.166341,-0.898607,3.889272,-5.284862,-1.170300,9.310212,-5.933652,-3.993990,-4.398501,0.628984,2.464903,2.134064,8.283716,6.287368,-0.409696,-1.640150,-5.691645,7.848298,0.446910,6.186581,8.627118,-8.262161,2.777281,9.815619,-5.291586,-8.279161,0.325311,9.624384,-0.703148,-3.876665,-7.339342,1.494668,1.965803,-4.561870,5.657909,-7.907836,-0.704654,-7.256634,9.126871,1.188078,-6.158853,5.004195,-4.241621,-7.752729,9.934655,3.464240,-9.543889,-9.434405,0.068892,-2.471482,-6.306050,9.624340,9.314863,-3.854952,-4.157067,1.088659,-3.899418,-3.373038,8.785720,7.272975,6.619149,-8.056419,-0.696982,7.531634,-5.453337,-0.226224,4.517524,1.832159,0.589409,2.492697,-7.327925,-9.608568,-7.687718,6.718510,1.132433,-6.913347,3.766815,-3.638545,-2.095589,7.713605,-5.262231,3.965669,-1.663239,-6.748113,3.288030,9.310742,-1.413906,-7.397429,-6.320679,-5.087457,-3.570066,7.203149,-4.691738,8.138553,5.579380,7.233085,-0.957190,4.969559,7.233579,-2.677593,-4.075467,-7.805260,2.033501,8.327216,-5.945103,-0.934767,-4.971144,-6.186862,0.295724,7.184554,8.352713,-3.231512,-8.033881,-7.352364,-4.803323,-7.089092,-8.297891,2.989775,1.532130,8.156608,2.411104,-4.896573,2.478075,-0.826119,8.012110,-9.637671,-4.694356,-3.401077,-7.543794,-9.287456,-2.163035,1.384015,-4.259202,-2.259257,2.913303,5.788326,4.249754,1.802563,3.595671,-4.687494,2.724060,5.495728,1.549439,-8.449851,-8.111918,-7.051799,4.768733,5.730617,1.456684,2.644732,9.540335,5.599987,4.916236,-6.879160,-0.377570,0.435084,8.497165,4.084212,-5.195084,-8.742000,-1.240818,1.618046,3.081712,2.724752,9.943389,1.150622,-9.396517,7.073181,1.456868,-2.226113,-3.364807,-3.317421,-3.588232,3.833175,7.013740,7.197055,-1.783903,-8.658315,1.359848,-0.871460,-4.104711,2.360497,-9.327725,-5.852383,-7.700217,2.497032,-7.000544,-4.507707,5.739947,-4.242015,-9.289198,7.832020,-6.654360,-7.577398,4.615886,-4.121219,-7.207347,-2.030258,3.682736,7.214585,7.480502,-9.993500,-7.105833,-2.530336,-7.394926,-4.725187,-9.912280,-1.065995,7.077805,-3.007680,4.151705,5.899445,6.697505,3.629241,-3.672468,-6.380175,7.081418,-5.110044,-6.610258,-3.038190,4.429094,4.184419,-3.303215,-8.678206,-2.806763,-9.729355,-4.005779,9.438276,-6.648616,-9.648447,5.343131,-5.476862,9.990375,-6.898162,-7.265382,6.036549,-9.580498,0.239283,-5.837468,-4.497201,2.988890,-1.344724,-4.352492,2.809186,-2.281983,-8.321327,-9.685267,1.333390,1.057583,6.973368,-0.895426,4.224188,4.972369,8.958582,-8.164141,-1.322418,-0.542676,0.821001,0.023580,9.437273,-4.055343,2.614108,5.905217,1.282523,5.658215,-2.927760,8.762214,-2.820475,-5.381144,-4.381696,3.852747,-8.406929,0.235824,4.922493,-9.395750,3.295338,-9.088920,-7.726018,8.143407,-2.938090,-3.521230,-9.100072,-0.168579,8.565493,-0.595325,5.436743,-3.171083,7.778729,-7.990560,-7.290647,-2.685378,7.823271,0.882837,-4.588635,4.020443,8.895046,6.850411,4.167012,-7.674012,-1.902284,-4.972333,-9.178596,-5.744282,8.169235,-1.551876,6.478104,7.298014,8.582818,-1.959689,5.898505,-6.958031,-7.582839,-2.634777,7.934568,-9.716812,2.818355,-4.854301,2.069130,0.775767,6.424424,0.264315,-5.522176,3.550504,3.779494,8.454748,-7.805123,4.765374,8.008804,-3.182102,-0.026677,2.942613,-5.805255,7.462988,-7.611458,-5.326548,7.018439,-8.685879,-8.677214,7.925068,-7.449720,-5.509642,2.048180,3.519297,0.546945,5.533327,-6.668195,7.096981,-0.315760,-7.241148,6.109585,-7.090319,-1.616233,3.521304,2.977585,-5.552354,4.386558,-5.422944,-5.239110,-2.921401,3.098243,8.967319,-7.566698,-3.995361,-2.286149,3.610101,3.909504,-5.293549,-0.662270,-4.740156,-9.580175,0.712917,1.093954,-6.235995,9.239059,8.239173,0.024082,-8.395587,5.342719,-8.388053,-4.955029,-0.317134,-9.975740,9.660198,-1.333309,-6.818412,6.486468,-7.490939,8.918518,-7.550614,3.253055,3.067388,6.363827,-5.678426,6.527253,-1.253130,-5.760956,6.451704,8.613166,-8.914847,0.707777,-5.605777,-3.070657,9.455541,-3.007884,9.822876,-2.099539,-7.143112,-0.448334,-4.131767,5.958095,3.530630,0.172906,-0.819715,-1.111822,-7.348670,8.356294,-9.773001,-3.027939,3.047245,6.036934,-0.562632,-2.640458,4.228257,-7.740045,-9.924206,-6.523286,9.301704,-0.992379,-4.852823,-8.562182,-5.362914,-1.272611,-7.042098,4.973658,1.338707,-8.561807,-8.753973,-2.409191,5.207419,6.866805,-1.023671,-1.361230,-8.400009,-6.672948,2.083074,4.116032,-0.276229,-4.265657,-8.747929,8.561001,-8.462024,-9.964130,-7.731594,5.482478,4.459522,4.782799,-0.774999,7.702437,-8.414102,-6.066545,7.217853,-5.691174,2.394304,-6.850840,-4.655724,3.121542,0.440498,9.137425,-7.559938,8.059396,3.061566,5.334204,-4.405608,-4.293970,-5.983663,-6.351545,5.080163,-0.450993,5.644736,-5.209431,-1.508050,4.782091,1.681941,7.618873,5.055170,7.331689,8.956688,-5.494639,-9.696824,-6.009342,8.883357,-5.220324,1.149605,2.082938,2.457121,-6.563982,3.625930,5.659964,-7.801308,-0.395187,0.586455,3.112664,5.384133,5.298797,-2.840766,-5.771570,-1.743872,-4.171973,7.443219,3.212897,-3.832557,-0.969981,7.568930,-6.735253,-3.262990,0.223043,1.254030,-2.309483,-0.936754,-1.567492,-7.288355,7.925038,5.538635,-1.012833,1.362633,6.124056,-0.500213,-4.208548,5.788719,1.688178,6.036230,2.003735,2.561030,5.897476,7.701493,4.472589,9.906468,0.889447,-1.233369,8.968784,6.513355,5.755460,4.703687,4.346536,7.894479,-8.918740,5.383865,7.564602,-2.897124,-9.701369,-3.900486,1.350603,-7.253586,-5.712366,-3.414396,9.687700,-6.749172,7.115413,-9.005703,-6.807613,-7.259128,-3.225588,-7.984936,-9.368090,9.686230,5.357130,-0.546659,8.276450,8.992649,-2.189089,6.701280,8.491635,-9.466742,5.197753,9.969892,-8.754566,9.989286,8.904620,-0.828639,-8.454793,-0.662335,8.272619,-4.848179,-4.043422,-0.378427,0.102789,-9.153777,7.233308,-2.804561,4.384148,-3.887649,5.744353,-8.224010,-9.010483,-2.227480,-0.611335,-3.150293,-3.967543,-7.174993,-1.753512,3.917007,6.213805,-7.761062,-1.186285,4.987514,-6.737477,-8.382663,9.590350,-0.908406,5.311117,-8.036728,0.505489,-6.447344,2.835125,-0.161766,3.853770,-4.356279,6.979059,-7.016283,5.382005,7.367941,4.495604,6.665897,4.783286,-2.109120,-7.589920,-5.915476,6.515168,6.513322,-9.539156,-6.489047,7.348287,-2.979281,3.482521,1.325735,-2.512573,-5.354752,-4.410052,3.274521,0.327595,-7.069885,-6.351446,-5.902909,1.191296,6.535694,0.976613,-4.690495,-5.336481,-4.926298,4.913286,-3.747230,-1.360829,7.112954,-2.865826,-5.713592,7.226479,1.217313,-7.855730,2.287792,-7.385786,6.269989,7.971724,-0.375929,-8.019692,7.083340,-5.280533,8.545528,6.093501,6.175290,2.322532,5.948602,9.414331,1.618270,-7.213435,0.463027,7.775072,8.773592,-5.207586,-0.760993,-4.472832,-8.804743,7.189903,7.089306,8.323357,-4.855731,6.198740,9.555026,-8.476047,-6.925670,9.744471,0.520386,-8.834514,8.826448,0.314077,2.282454,-6.220747,-7.540584,5.397648,-6.704904,2.413079,-6.778825,-6.910808,8.192092,-0.458686,-6.167358,7.092692,-8.606004,-0.515847,4.902775,0.621089,4.221889,-1.778044,1.098615,5.147555,-4.429465,-1.035014,4.009706,-7.078203,9.390289,-1.348144,4.113555,-5.473859,7.092778,1.501400,-4.298882,1.425489,-5.828439,0.530741,-4.375779,7.072523,8.198105,8.779818,6.433157,7.534514,-9.949166,-2.996261,-2.030794,6.553543,5.249323,-4.072380,6.740260,4.077588,8.602323,3.885385,7.871811,1.214700,-5.902975,-4.088137,-7.876062,-5.240542,5.255222,-9.468963,7.176847,-6.266565,6.881236,-4.909905,-0.151108,-6.634750,7.192604,7.630464,0.143058,0.653448,2.845355,9.003812,-8.023248,-1.849925,-5.932898,8.285277,-2.239886,-1.106114,-0.666001,-3.127738,-6.026441,-2.060286,-8.106999,-0.398870,-0.602959,5.504465,4.990907,-2.253700,1.144636,-1.803693,6.494173,2.271083,3.602941,2.877714,2.679258,-4.102905,5.773141,6.510344,1.744119,9.912613,7.331571,8.989177,7.628517,-8.133080,7.116278,-3.504167,-9.955762,-7.962911,5.053936,0.102903,-7.815252,-6.813115,4.307468,2.558326,9.216635,-8.886917,-7.895136,-7.250171,6.034613,-0.341062,2.554289,-2.935073,-0.629222,4.312991,-1.358879,-8.390308,-4.179174,-2.771552,-5.134254,-9.631644,-2.017366,5.300974,6.294323,-3.032197,-9.108693,1.027695,9.836066,-7.282710,-6.457523,7.086108,-9.684709,0.275002,-1.740776,-6.873092,-8.286443,2.589825,-9.551990,1.583657,-0.472524,-5.512989,-1.311187,-8.143071,4.407097,4.639079,-9.538203,1.831475,5.240172,0.596131,-3.312112,-8.767770,0.117412,-2.867958,-5.983021,4.553731,2.098133,-3.675435,3.444899,-3.182735,7.065143,-5.556192,-8.549245,-2.745251,5.445139,-6.733303,-1.171642,-7.281091,-1.522591,4.138589,-9.189381,3.863045,-0.612646,8.016045,-1.874510,1.394337,1.933288,5.881017,6.816041,5.209350,2.357686,-3.611706,1.609977,4.489734,7.701740,-5.287977,9.487268,-0.405775,2.688225,2.259108,7.344295,4.661911,0.799170,-6.443373,6.462583,2.032053,4.924193,-0.099124,-7.284429,-4.912044,-0.521442,8.302947,-1.388883,9.536960,2.427608,8.713469,9.087538,4.804166,6.716544,7.884761,-6.170838,-7.079775,0.687886,-5.396620,-1.318714,4.673860,1.590645,0.196721,-4.701649,-3.489003,4.990028,-1.032878,-1.184007,5.103603,-7.595083,-4.516503,4.494156,-3.236345,9.699106,-3.237813,-8.156629,-3.154915,-1.720131,2.139522,9.649080,-9.960018,-9.866281,5.636264,7.004898,-1.779260,-8.575122,-6.088632,8.189489,-4.426325,5.079412,3.987408,-3.775748,3.022776,3.156034,-7.605993,-7.602834,1.481328,1.692847,-2.484046,-7.923346,-5.016120,5.497604,-1.066711,-8.877209,-0.037352,-3.935493,8.164420,9.136462,3.841206,5.191906,5.434811,8.166131,-8.691552,-5.909861,9.358878,-3.571138,2.861353,-2.151630,-0.685446,-0.727749,-0.353166,-1.542082,0.155304,-1.026810,-7.751062,-6.746670,-5.835245,8.644342,3.730833,1.015620,-9.741255,-4.975324,1.059962,1.415523,1.551307,-9.194335,-6.384536,0.908662,0.224628,9.178572,-2.929981,9.144096,9.672695,2.756095,-9.786799,2.907705,-6.502320,-7.923100,-5.377567,-8.761558,1.844872,6.267494,7.600529,-2.773482,-5.916964,3.404059,5.901439,5.737569,3.047343,7.305003,5.230039,-1.810181,7.148270,-0.939812,-7.165508,4.946712,6.825481,-8.176016,-0.340896,4.270113,-2.714109,0.859230,-2.233722,-9.593377,4.695255,1.280382,-6.407025,4.088180,6.811430,3.170442,-5.484961,4.719467,3.550811,-6.011361,-3.133578,-1.203476,-1.142558,8.949142,4.255500,-5.013101,1.096363,8.456219,8.680883,6.344058,-3.876174,3.426938,-5.775069,5.722682,-7.494563,6.673717,3.794661,1.655728,3.795062,-7.570772,-9.751292,7.681341,9.892349,8.298514,6.650551,3.034014,1.152402,-8.745155,9.162293,1.155774,-9.787859,0.209433,-2.193947,8.570937,8.178253,-3.824426,1.292868,3.402441,9.482734,0.710722,-6.249714,-5.570613,0.051407,4.965251,-4.770843,-1.670747,3.643127,2.454244,-8.752259,5.049975,-8.932109,1.334153,5.315993,-2.697898,3.206522,-5.316615,-4.654422,3.120628,0.409592,7.166691,4.496489,-1.807439,5.550320,7.961579,7.929963,0.183388,-1.434181,2.951664,1.053890,-9.563377,7.180955,-1.883710,-0.682976,-8.629776,-4.919882,0.212886,1.643432,-0.140773,5.312005,8.689960,-6.379040,0.012285,6.670183,2.388805,-9.274616,-8.004212,-6.622183,-8.017580,-0.770309,-5.206630,-4.607719,3.538350,-3.623308,-0.238075,7.856446,-9.169675,-4.073375,-0.311378,-3.250724,-6.522462,-9.660420,-2.747843,-7.007752,2.800895,5.962477,5.289619,2.722466,-1.277665,6.175502,-2.397569,-3.681789,-0.935986,-6.663675,-3.480400,-2.726175,3.281934,9.307720,4.477765,-1.461663,8.827466,9.491145,6.237939,0.687385,-2.776529,-9.649978,2.424048,0.162301,1.619005,-0.695310,-9.209957,7.611300,8.339852,0.544131,-3.520927,5.678112,-5.465533,-1.317483,-6.040891,6.722982,-9.989237,3.022170,-9.880471,-4.495567,-7.564463,9.029059,1.353754,-1.249030,-5.794545,-0.609622,-1.527311,-1.094527,-5.335282,-2.184028,-1.537731,7.219851,-0.318551,-0.277601,1.998576,-5.187386,1.697145,-8.935952,-4.689094,-3.886377,-6.723471,2.251323,-0.308475,1.402305,4.903235,6.143667,6.048221,-5.851435,7.022001,-6.834042,6.595869,-4.881829,8.380886,-8.878787,-1.660483,-4.297706,7.741641,8.710132,6.079910,-1.449171,-3.588510,-5.082324,-7.239750,0.217200,8.683041,-9.928225,8.628612,9.978423,8.982898,-1.146804,-6.593991,-9.076225,9.881950,-7.282470,1.678322,2.047995,-6.821294,4.825917,-6.560435,5.452701,0.577170,4.305448,-5.471225,8.746810,-5.490255,2.329309,-7.197615,-8.776059,6.368548,-2.034587,5.733020,7.528703,0.427500,-2.407252,0.723676,3.361045,4.555857,0.390728,9.605120,3.069330,8.070325,1.944735,-5.287856,1.001166,-1.501416,-0.781661,3.207765,3.508007,1.199601,-4.911936,4.006538,5.792965,-0.505489,6.193824,0.811176,4.796014,6.976360,-5.415116,-2.219912,-1.695972,0.859811,-8.960910,-8.893169,1.584215,8.614310,-7.119528,3.347971,3.270910,8.680888,2.239077,6.999154,5.383366,5.255584,0.824092,8.456182,-4.758364,-8.902885,1.658688,3.702302,-1.623482,-2.654641,7.132521,-0.194265,-0.415587,0.001367,-9.453362,-9.076527,-2.935314,7.773562,-7.716054,3.134572,5.522555,8.685269,-6.118986,6.065078,-3.687941,4.014018,7.655392,-9.457410,7.412916,-9.695729,2.102956,8.487642,-5.602933,5.793864,5.402962,-8.897986,-6.171603,8.843587,-2.447166,-0.876343,0.653782,-0.238199,2.476989,-1.852240,8.753775,0.837208,8.906880,-5.359582,3.015680,-1.250956,-8.290301,-5.861193,0.371657,8.869360,-9.838574,-5.490587,2.917108,2.081393,3.689007,-5.757662,-6.505849,7.721708,-1.616097,2.043800,8.939735,2.967848,-2.331153,1.821590,3.854682,0.037316,-1.921187,6.420437,6.079895,-4.503953,-3.783321,4.554497,-5.200459,6.125754,-8.155209,9.127682,-5.074157,2.922552,-9.972870,-2.919502,2.173755,1.330141,7.904869,7.036923,9.992250,-1.246242,-3.218347,-2.581426,-7.348527,-8.503117,2.179454,1.688248,-0.951975,-8.341260,7.358916,-1.432120,3.760572,-7.617541,8.516938,0.762714,9.476685,-4.162403,7.004783,2.379274,-5.752203,-2.552462,6.664183,-1.336436,-9.641819,-1.828923,1.430891,-1.851523,-7.217239,-9.573013,-1.096109,7.716909,8.349738,-5.745249,-6.744022,-9.321274,5.113877,-6.018790,-8.173811,-6.148068,-9.807047,-8.402468,7.259619,-9.553144,1.952337,6.780718,-5.506597,-6.884732,5.383552,-0.358072,-9.103147,-5.215856,8.860263,-8.209110,1.224165,-4.229643,6.879017,-1.908199,3.829971,-1.728573,9.806887,-8.465934,-6.508618,1.442747,0.248220,-9.489711,-4.337234,9.427855,7.967304,-5.064290,-3.452959,-7.648774,4.665366,0.901658,3.906260,-7.804723,7.300453,-5.300851,7.647212,8.761364,7.665350,-6.295459,9.287595,1.604810,3.614895,3.849314,-7.090284,6.428207,-6.717210,-5.143154,-8.884596,-0.072406,-2.321691,-2.925779,-1.153213,-2.512542,3.659201,-5.865111,6.990487,5.838303,1.064267,-5.614156,6.050837,7.709458,-0.027430,8.817766,-9.232521,3.980502,9.117379,-7.324319,2.759220,4.003209,2.955382,9.269136,-5.050163,3.025672,-5.279502,1.563848,2.556098,8.909726,7.863554,9.213827,6.949799,-8.628754,-2.309892,-0.614755,2.281381,-7.748959,3.367255,8.110220,-4.322419,5.622450,8.744852,-4.341632,-2.782595,-6.673682,2.599256,4.030146,-3.201314,3.635940,8.364114,3.431627,0.051216,7.931972,3.444805,-3.327461,-5.081878,-1.159760,5.958495,-4.172334,3.203799,8.666653,-2.437244,4.179221,-7.667209,8.281743,-7.969110,-0.260276,-3.268829,1.841522,8.634646,-3.309225,9.828756,0.110407,0.878416,-2.278194,-2.550549,0.709309,6.561322,-6.114284,7.107151,7.275324,-3.563224,-3.731133,6.629635,-1.938861,6.036071,-1.672904,-5.343527,0.752985,-2.436016,-8.967713,8.937928,6.278399,-0.046974,-8.313451,-0.632612,5.729929,-3.680751,1.919016,0.596011,-2.961548,-2.239426,-6.169661,-5.416747,0.637881,1.107427,8.471823,2.621036,7.941342,-7.954664,-5.893356,4.610891,7.634166,0.649951,-8.809351,7.531534,6.166804,3.222737,-2.986798,-0.195494,-2.483566,2.597703,-5.921975,7.140932,-6.657391,-9.102395,-2.971316,-3.125343,9.285866,-2.298762,4.797614,-8.245797,-8.963646,-5.859467,0.825538,-3.943297,-6.488551,8.020443,-6.614275,0.463023,4.458927,7.219677,4.136705,9.618132,6.874258,-2.579049,1.047398,-7.641718,2.154486,-5.862016,4.967216,-0.159752,-1.340350,-0.975537,-5.320958,7.168355,0.095783,6.745020,3.026887,3.983499,1.248447,4.431742,-3.673674,-5.702253,-6.126092,-2.342609,4.737108,1.713326,3.972630,-7.642109,0.638721,0.678648,4.016066,-1.085174,6.842732,0.969823,4.958076,-5.333345,-3.736690,6.527411,6.991003,-5.179365,2.313715,5.292807,-7.739566,-5.465763,9.134892,-6.248547,2.255522,2.614036,1.326512,4.647352,5.799524,-9.286318,-0.313538,-7.615496,-1.433703,-8.021524,9.751385,-0.113206,1.970597,8.156719,-8.759855,6.621919,-5.495698,-6.289219,-5.839867,7.126259,0.673025,9.377983,4.898197,-0.744059,3.421239,0.844268,-1.209660,-7.767430,7.170285,-5.537538,6.027292,4.364449,7.440665,4.951877,3.157803,1.023050,2.855075,-9.968192,0.574698,-9.876836,4.481225,3.762262,4.406361,6.491802,8.356770,-0.767388,-3.113012,6.353051,7.832937,1.473705,9.756841,-4.955035,8.359684,1.125838,9.981363,6.757651,-3.655201,-9.642657,-0.628514,-7.519168,6.205769,3.093756,-7.593788,9.942289,2.700103,-9.969565,-6.504176,9.759428,3.711180,-5.722029,-6.913677,0.090157,-1.725499,-1.398572,6.173075,-7.213280,9.979756,-8.899610,-1.928450,-0.694806,-9.858305,-5.204503,6.246788,1.331732,4.212698,6.004346,7.762708,-3.476963,-3.469012,0.443738,7.110679,-4.362702,0.100383,-9.276492,5.611315,3.324419,9.551551,-0.643769,-5.496896,7.867503,0.141918,1.093363,0.171993,-7.965494,4.797791,8.387238,2.562698,5.226486,0.048298,4.654007,-2.850127,-0.219133,-6.645039,-8.465558,-8.366425,-1.398462,-3.895152,4.244710,4.643580,1.995427,1.059063,6.089640,6.138184,3.139645,-8.594595,0.832748,9.904745,-6.128668,-6.039978,-1.092806,-1.448943,-6.212372,7.396447,-4.726368,8.707803,4.723883,5.377409,8.524180,3.448935,5.459557,2.804535,1.423670,-3.303730,3.735361,-1.812276,-4.650989,-2.357447,-4.550398,-7.854135,5.492975,-8.382473,-4.203128,7.698466,-1.878029,-2.784633,7.549234,-3.579370,-4.629269,-0.271666,9.906815,-4.440986,-8.256446,-4.608642,-4.715748,7.688332,-0.877913,-6.320002,2.071239,7.243971,-2.779251,4.728866,2.826801,-5.596622,5.367120,4.100605,-0.572333,-7.026534,0.981131,7.116393,6.302467,8.593852,-9.704732,-9.227504,9.889281,-5.839886,8.060485,0.641118,1.777670,-7.153963,3.163013,-7.368418,3.817719,-2.614455,7.784923,-0.285646,-5.490077,4.353296,6.798658,4.546233,3.256823,8.221448,4.656359,2.383322,-6.743622,7.587621,-1.325968,7.730434,-6.952982,-4.185462,2.658553,-1.675493,-8.149859,3.552811,1.081523,-3.479682,-6.825393,6.572231,5.206641,-8.401553,3.699960,7.627738,1.294924,0.300498,-5.411364,-1.026932,0.692797,9.698562,-1.832479,2.464844,6.489808,-1.015543,1.956811,-9.231714,-2.206332,2.534419,-8.034085,7.838274,5.746828,-7.599935,-7.756263,-8.821727,1.174401,8.712857,-0.514861,-4.625676,5.833902,6.229210,-5.985107,2.610488,-4.985296,-6.755002,4.237852,5.148297,1.517779,-4.746304,-5.527290,4.090306,-3.956657,2.616198,2.703284,0.312690,-6.179356,-5.244934,-9.251522,0.227963,-0.787096,5.648133,-3.428692,-9.538972,-9.268407,6.359477,9.301801,3.091018,-8.441435,-9.991537,-2.506426,-9.492424,-1.324927,0.624141,-3.277800,-1.867701,4.623870,-5.776408,-3.250304,8.219375,2.707017,0.695476,5.311564,-1.254928,2.169447,5.908532,-1.572037,-1.189973,-1.938859,2.001210,-7.972337,7.209458,-2.704499,5.420416,2.381254,5.010596,-4.830774,6.039780,7.409472,6.656398,7.818536,-3.854293,-7.239833,-1.102901,3.491956,5.875698,1.951366,5.777662,-0.687559,-9.611626,5.574638,-2.887927,-1.204690,9.399741,3.048880,-9.578212,4.935712,7.647409,7.292514,0.280637,9.998509,2.507315,4.809773,-0.254049,8.779104,9.049799,9.637693,-9.702907,-1.115175,8.249808,-7.441692,-7.384304,6.886697,9.115378,6.583320,6.872910,2.489105,-0.395355,3.539214,-3.418607,6.730614,2.882403,8.055957,5.901701,8.559182,-0.498339,-3.091330,1.718565,-7.084544,4.001194,4.753075,-2.126710,5.950525,-6.679458,-0.562871,3.529437,-9.565878,-5.837122,6.706542,9.426449,-8.258565,-8.309637,-7.404942,-3.812551,8.625710,6.058016,-9.941769,9.228998,-0.926895,-3.172700,3.032775,-8.751342,-7.907741,5.335499,-1.736330,-2.385707,-5.576561,-9.237656,3.024276,0.549732,-3.087172,7.411813,5.818249,-9.676506,-7.730592,-1.408386,-4.600410,-6.574319,2.064640,-5.926637,-8.770442,-1.722670,-6.707152,-9.089606,-9.352472,-9.469985,-1.884034,2.223875,-3.035923,4.150497,5.376436,-4.996311,-9.635769,-6.245202,8.649755,-2.631675,-1.224943,-6.144617,5.425093,-2.901549,6.973173,-5.703356,-5.783392,1.663094,4.343906,-1.163591,-1.263187,-6.533729,7.415236,-3.948525,-1.912170,-0.943227,5.665596,3.073434,2.800079,-6.745403,-2.017551,-0.533878,6.690765,1.040576,-9.372226,4.916513,3.002299,-7.867322,-1.247697,8.278053,8.605433,1.582185,-1.319153,2.146456,-6.050799,-9.818176,-6.752718,-4.427566,-2.168437,-5.160929,3.634313,6.292088,3.620372,0.383106,-3.206895,-6.583662,-3.709103,5.518111,-7.541959,9.594101,-4.490254,0.901234,-8.518950,-2.719705,-3.085841,-6.108203,-6.190407,-5.041592,0.302494,-9.431200,-5.751473,5.016200,-5.797205,1.928752,0.240801,-5.120663,9.744849,-4.813885,0.599339,-5.007803,3.063407,8.890436,8.106765,7.373875,9.333236,-2.828036,3.599016,-6.644650,-6.652635,-8.801991,-9.754296,-2.633325,5.156479,-1.567750,9.609814,-4.600950,8.766498,8.530468,6.196119,8.265760,-1.466036,-6.280565,5.946824,5.193081,-3.724035,5.745729,-0.879683,-3.275777,-2.872037,-7.226088,-9.710871,-3.766427,-1.489948,-3.302599,-6.858208,-0.504149,0.033875,-3.895590,-4.162985,0.453127,-6.490236,3.058330,-8.359830,-5.770653,-6.616777,-6.434514,4.142441,-8.502241,-2.552578,6.276671,-8.458631,4.282880,-5.069178,-0.881482,-0.744758,9.764883,-8.982342,1.884953,9.561865,0.194706,7.917993,-1.708949,-7.198543,-7.316566,6.958296,-6.417207,-7.232609,9.685814,3.990167,8.652769,3.887335,-0.810145,8.801312,-0.968711,7.560810,6.843054,-6.657718,8.907438,-2.425098,6.679304,6.909966,-9.638859,-1.482439,-3.904181,7.155544,7.330402,8.942515,2.865315,4.360354,8.168837,7.552555,8.049491,-1.829074,3.354689,0.813617,-8.538232,-7.286727,-0.848405,-6.185810,-9.224045,-3.859062,3.802507,-4.970706,-6.620397,-6.520228,-6.916218,-0.359866,8.284079,0.754581,-9.917377,-0.536089,0.741631,1.013973,1.949903,9.697117,8.153216,9.812279,4.428997,4.357497,1.544770,3.343209,-2.540984,-9.997345,-8.872654,-1.788403,-0.947612,0.213926,2.575302,3.280379,-6.190533,-4.086389,-6.321787,-0.968626,9.609327,7.729650,-6.463229,0.801196,4.230736,-3.208382,7.376482,-4.207876,5.823122,6.829096,-2.183012,9.838095,3.566966,-5.130003,4.466370,7.986534,9.363776,-6.729845,4.992129,-2.760342,2.571308,-4.063200,6.554417,-7.121366,-2.543577,2.423653,-2.284351,-3.389601,-1.692044,8.991956,5.083960,2.618432,9.104042,-7.703706,9.900731,3.129383,-9.550473,2.656789,-2.530729,-3.893269,9.199312,2.572112,4.488552,-9.634952,2.337059,4.074112,-5.131160,5.908444,-4.638717,9.587285,-4.221607,-3.640075,-2.516439,-8.232412,5.860216,-6.586542,-2.655188,-3.862128,7.217413,5.722096,-7.889170,8.344180,8.127164,3.191228,6.088366,2.031308,2.154291,-9.884231,6.925666,9.606381,4.074705,-6.100145,7.474477,4.787420,9.544794,4.363341,-8.257980,-4.313541,6.212640,3.266863,-1.405148,-4.066588,9.308736,-6.650252,6.448185,3.140030,3.733274,-5.694718,7.305412,3.121640,8.818889,-7.478966,4.635301,7.737629,-4.784786,0.552185,-2.876539,8.393595,-3.616247,-4.721170,7.088059,3.961471,1.348171,5.282236,1.677902,1.079529,-9.703545,-5.526339,1.336645,-7.108038,4.323707,-1.318841,-1.584791,8.034255,8.262281,-9.511207,7.620339,5.750513,-0.569751,4.644755,4.105373,-8.434830,3.028489,-5.411134,-0.452527,-1.314918,-5.082299,3.216439,-3.783561,-9.693605,6.938953,-9.706718,-8.433183,7.231461,0.721202,-8.685978,-3.753152,-7.510838,-5.934027,-6.094285,3.341206,-0.888488,7.578599,-2.000587,-1.180759,-6.733075,-4.554731,-1.734009,-1.743779,1.047949,4.377362,3.283112,-0.455014,0.502136,-3.335071,4.954519,-2.794756,5.511522,-5.950226,-6.032745,-8.244193,-8.946506,5.085792,6.829622,-6.491797,5.508215,8.131063,0.277754,-7.815349,-1.590395,-8.533409,8.070317,0.229957,5.293803,-8.559836,-2.679750,-2.544148,5.459212,8.215116,4.334519,8.776421,6.980846,2.430633,-2.526370,6.549358,-2.536218,5.086371,9.981312,0.410151,-7.915207,-5.471920,-0.101145,5.559704,-6.307243,1.759166,-7.200787,6.616956,4.005758,5.921791,-7.791438,-3.097836,-4.472193,-5.275787,-8.316061,-4.744865,-8.040268,4.971395,6.675230,-3.326787,7.144717,-6.334443,9.182058,-0.286917,-0.831549,-6.356979,-5.822485,-9.530022,-3.222363,-1.263551,-2.602077,7.270611,9.891573,1.208624,8.346395,7.999449,8.043851,6.666959,4.067317,1.149676,8.157022,-8.886752], dtype = "float64")#candidate|5395|(5460,)|const|float64
call_5394 = relay.TupleGetItem(func_1852_call(relay.reshape(const_5395.astype('float64'), [5460,]), relay.reshape(call_5376.astype('uint64'), [120,]), ), 1)
call_5396 = relay.TupleGetItem(func_1856_call(relay.reshape(const_5395.astype('float64'), [5460,]), relay.reshape(call_5376.astype('uint64'), [120,]), ), 1)
output = relay.Tuple([call_5376,call_5394,const_5395,])
output2 = relay.Tuple([call_5377,call_5396,const_5395,])
func_5400 = relay.Function([], output)
mod['func_5400'] = func_5400
mod = relay.transform.InferType()(mod)
mutated_mod['func_5400'] = func_5400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5400_call = mutated_mod.get_global_var('func_5400')
call_5401 = func_5400_call()
output = call_5401
func_5402 = relay.Function([], output)
mutated_mod['func_5402'] = func_5402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4300_call = mod.get_global_var('func_4300')
func_4302_call = mutated_mod.get_global_var('func_4302')
call_5449 = relay.TupleGetItem(func_4300_call(), 0)
call_5450 = relay.TupleGetItem(func_4302_call(), 0)
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_5452 = relay.TupleGetItem(func_1448_call(), 0)
call_5453 = relay.TupleGetItem(func_1449_call(), 0)
output = relay.Tuple([call_5449,call_5452,])
output2 = relay.Tuple([call_5450,call_5453,])
func_5457 = relay.Function([], output)
mod['func_5457'] = func_5457
mod = relay.transform.InferType()(mod)
output = func_5457()
func_5458 = relay.Function([], output)
mutated_mod['func_5458'] = func_5458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_764_call = mod.get_global_var('func_764')
func_766_call = mutated_mod.get_global_var('func_766')
call_5459 = relay.TupleGetItem(func_764_call(), 2)
call_5460 = relay.TupleGetItem(func_766_call(), 2)
output = relay.Tuple([call_5459,])
output2 = relay.Tuple([call_5460,])
func_5461 = relay.Function([], output)
mod['func_5461'] = func_5461
mod = relay.transform.InferType()(mod)
mutated_mod['func_5461'] = func_5461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5461_call = mutated_mod.get_global_var('func_5461')
call_5462 = func_5461_call()
output = call_5462
func_5463 = relay.Function([], output)
mutated_mod['func_5463'] = func_5463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5516 = relay.var("var_5516", dtype = "int64", shape = (11, 4, 16))#candidate|5516|(11, 4, 16)|var|int64
var_5517 = relay.var("var_5517", dtype = "int64", shape = (11, 4, 16))#candidate|5517|(11, 4, 16)|var|int64
bop_5518 = relay.bitwise_xor(var_5516.astype('int64'), relay.reshape(var_5517.astype('int64'), relay.shape_of(var_5516))) # shape=(11, 4, 16)
uop_5522 = relay.asin(var_5516.astype('float64')) # shape=(11, 4, 16)
uop_5531 = relay.tan(bop_5518.astype('float64')) # shape=(11, 4, 16)
uop_5536 = relay.atanh(uop_5522.astype('float64')) # shape=(11, 4, 16)
func_5231_call = mod.get_global_var('func_5231')
func_5233_call = mutated_mod.get_global_var('func_5233')
const_5542 = relay.const([-3.662882,-7.791467,-5.353459,-1.690818,2.510652,1.748797,5.646060,5.390392,3.932773,-8.024802,-9.535127,-3.353183,9.272972,5.040207,9.011537,0.636180,9.949784,-7.474660,1.140517,-5.179674,-3.253817,0.142416,-0.673370,-0.561266,0.715277,-3.389111,-0.967561,-7.943125,1.501550,7.827230,-3.793443,-0.361267,-7.510141,8.258753,4.941809,-5.660910,-3.912978,4.945312,-7.889414,-9.699238,0.324776,-8.809788,-6.884037,2.030155,-3.927833,-7.461359,1.522571,-5.085600,5.746669,-3.066685,9.706003,4.868459,-6.859385,-7.784168,-3.384087,-4.257023,3.302018,5.711022,-5.846422,4.863613,4.792114,8.225172,-1.324612,-7.070079,7.135168,-9.397059,-9.791117,-4.603225,5.985023,4.739454,-0.376969,4.440510,-9.392494,8.300160,0.474430,1.041556,-9.127839,-5.577440,-0.837034,2.265403,1.396790,-6.096381,8.950120,-2.285766,7.405519,-7.193735,-3.925089,4.929264,-2.812249,2.599338,2.209881,0.008825,2.820867,-9.055253,-9.456487,5.680768,-4.968407,1.951146,2.409584,-0.414411,-4.614108,-1.584626,-2.127845,1.254756,-2.230756,-4.273702,-8.294348,4.691073,1.436218,8.513165,8.371128,9.109348,6.885050,2.560931,0.523744,5.610853,-4.297338,-9.982724,-1.059554,-6.032589,-9.195304,-7.798538,-9.107028,-5.938343,-5.324744,2.449372,-6.403984,1.759522,-7.494147,-6.977746,-4.855993,9.768105,7.514825,0.838654,5.338083,-1.632902,-7.243432,-8.766432,3.456081,6.503629,3.249057,6.985723,5.855093,9.895409,-5.577676,5.486138,0.556612,9.342237,-0.030588,-3.704724,-1.336061,9.048710,-7.103341,5.114266,-2.773818,8.248084,-6.086540,-6.549031,5.325726,6.989240,8.163040,-9.220556,5.286157,-8.899114,-8.292655,7.558670,5.410130,4.426486,0.459873,6.109523,0.596129,9.151209,-2.168502,-0.894287,2.981867,6.807543,-8.792804,8.202454,4.112490,-9.171909,4.502081,7.611735,-0.426379,-6.562273,9.168783,-7.985288,-4.022799,-3.709275,9.216591,-4.010754,-6.649680,8.815368,8.263133,-9.283100,-8.519743,-9.534103,0.686986,5.996760,-1.696852,4.676507,3.865813,4.815915,8.219710,-7.233353,-3.287663,9.239674,-5.148859,2.213093,6.006176,3.365751,-1.679605,1.235577,1.098168,-6.238588,-2.881396,4.619470,7.801189,1.205837,7.890492,2.621686,-2.303236,-4.971795,2.616610,-9.438558,-3.958852,8.439931,2.425686,-7.507712,8.092882,0.361684,-4.274744,3.081984,4.700161,-8.300691,3.679622,-2.168495,-6.364687,-2.445082,-6.904544,-5.640055,-5.519804,-5.566535,5.893169,-2.495759,6.118183,-7.207410,9.582237,1.075527,7.343529,2.301882,7.207806,-1.818401,-8.410497,6.292084,-5.983349,9.988721,2.805417,-5.267225,-7.495511,2.989845,-4.985249,2.969713,-8.946687,-2.909176,-4.578889,-2.907401,9.511726,2.835957,0.571261,8.703545,3.642182,4.284297,-6.934163,7.374262,-6.164762,-4.071100,-5.668642,-6.029989,-7.534993,-9.453551,-3.445973,-7.769235,-2.164248,-2.586040,-0.351062,4.436229,-8.898090,7.644696,-8.355470,-3.623738,1.708578,-7.128126,-7.610886,-4.448616,3.136955,-1.391222,0.995939,-0.938671,-4.240779,-8.454823,-9.594960,-7.418103,-9.911572,3.189003,-3.178739,9.421151,-5.085096,-4.203867,1.466836,4.167725,9.292182,-7.084053,-3.579091,-5.996974,8.045100,2.424932,-4.047069,9.196693,6.865392,-4.818935,-8.493078,-9.702956,1.491611,0.844533,1.183669,3.158730,-7.698204,-2.466382,-2.755814,-8.391951,7.625622,7.702882,2.983971,-0.735124,2.793637,1.536098,-5.074560,-3.275468,-5.968065,-9.836285,-4.584323,-4.317992,-1.245758,1.562945,-1.610266,-2.173160,-2.033914,8.429532,-9.370853,-0.350680,-7.543180,5.448699,9.257400,-2.921041,-9.853307,-0.261741,9.543686,8.185412,7.674958,-0.250786,-3.452807,2.092344,1.021591,7.806519,-3.904981,9.943724,7.935605,9.077536,4.740195,-4.469617,8.898814,-3.752150,5.861885,-3.106576,8.519338,-8.773922,7.829194,-5.367303,0.012420,3.148863,2.215103,-8.579242,2.291107,-9.952256,-1.691308,-9.286240,0.243010,-2.788302,2.644860,5.826818,4.299580,-8.717546,9.366366,5.253837,-1.841116,-1.573314,-9.471581,-8.049049,-1.855726,-8.003349,4.226083,-1.661852,3.032058,-1.539087,5.209659,9.413209,8.558666,-9.118930,-2.691486,1.037857,-7.035551,4.896605,5.557204,-0.484958,-5.692176,-2.532507,-5.481450,-1.946172,4.296156,-8.023352,-0.984212,9.228902,5.613893,-7.742808,-8.827413,4.990938,1.232974,1.218020,-0.463284,-4.074391,-9.530963,0.096961,-1.315355,-2.753493,-1.525979,-6.611016,2.756417,-4.801087,8.638822,-3.771942,2.227699,-7.933766,-9.971807,3.698943,-4.646865,0.434415,-7.309156,2.672498,-6.321857,-9.295143,-2.573492,2.664584,-5.764346,-8.623200,-0.084145,6.720762,-6.690755,-4.213949,1.792112,-9.543255,-1.396217,-0.797636,-8.412631,6.628904,-8.901901,3.968909,-6.878543,-1.339404,-6.909110,7.659619,8.813552,-3.391814,-9.181485,1.274788,-4.583057,0.010540,2.754422,5.367312,7.714666,5.286150,-7.545012,-6.773102,5.022919,-6.566517,-8.439794,0.496254,-2.775205,7.771647,-0.239032,1.987010,-6.605571,3.099934,-5.764952,3.057007,0.563055,2.661228,8.751592,5.706533,-2.803585,7.660305,8.800253,5.155568,-4.171874,-1.853526,5.773611,-2.796329,6.409264,2.852218,-5.628519,0.625075,7.072326,-9.710452,0.102543,-8.655971,4.783354,-9.561647,-6.917915,-4.463171,-8.362393,9.467254,-2.150049,-1.278050,-1.965895,-4.938053,-4.311770,-7.892700,-3.593720,5.493409,-5.315150,-6.088233,1.380246,-3.869001,-7.033222,-9.307875,-1.939134,-9.676822,7.582277,-8.498061,-3.968145,2.433460,-5.630446,6.613331,-0.072940,-2.791146,-6.578401,-7.098123,3.796220,7.712570,3.562113,3.459923,2.394666,7.809884,-8.803237,-1.014898,-0.952829,5.101507,-9.963478,7.497012,0.837695,5.381052,-3.721291,2.883531,4.513194,7.463003,0.046214,-4.453886,-0.976749,9.898777,2.903979,-0.179749,8.196563,-8.796783,-4.011787,-8.061628,-4.114736,7.346485,6.516584,-5.057724,5.026819,-8.509150,-5.546061,6.836537,-7.902870,5.329556,9.610874,3.677152,-0.841803,-4.053047,5.308431,-6.422588,-8.090881,3.762736,5.385539,-4.669227,3.088427,1.147628,0.697469,3.400972,5.696627,2.731812,-8.144574,-5.389890,6.586242,1.226087,2.651722,-0.609611,5.918578,-0.295327,3.028069,3.235420,8.929749,3.242870,0.977878,-9.172684,1.337135,9.959414,-2.446324,-8.577261,-4.755196,-6.597438,-3.030741,-0.364065,-4.095166,-2.632825,1.548088,5.312398,-8.467846,-2.215876,3.958712,-4.656754,-9.815526,-4.038108,0.909398,-8.544295,-0.093470,-0.392674,0.292811,-1.320783,6.821805,-5.569820,-5.831251,4.197063,-5.591147,-7.135498,-9.585822,-4.268547,8.878393,4.881578,-4.111208,-4.014313,-3.895480,1.144303,3.430169,-2.647705,-5.481415,-9.149805,-6.208860,8.045530,1.216420,-2.328964,-8.256301,-1.069161,5.513259,6.762602,-8.102194,-8.835681,-0.115026,-8.038950,4.719138,-4.623166,2.432335,-1.996131,-2.134403,-6.783396,5.265798,3.126723,-1.161463,2.593511,7.818884,3.534943,8.781663,-6.338322,8.997754,8.057133,6.553672,-6.535877,-8.751657,-1.020498,-4.884426,-2.592031,3.406577,6.067118,-7.911465,5.232931,7.391170,5.744543,-8.884084,-9.872365,-6.059723,-0.155313,8.988096,9.645880,4.333072,-2.822958,-8.651312,-2.212960,-1.798373,5.756080,-7.694383,-6.671884,6.050961,-4.993931,-6.128292,9.391646,5.581725,-9.897922,-4.346670,-2.537283,-0.090672,1.532683,-1.485595,-7.393269,-7.411509,4.807884,8.462499,-7.598215,6.158122,-4.382421,-4.800459,-2.659877,-2.990224,-4.277805,-6.439320,-8.028637,-4.189663,-0.389586,7.035503,5.751713,-3.943285,9.697110,6.206831,8.998031,-9.201418,-1.470169,0.773324,-4.692816,5.856352,3.098144,-7.237145,-2.097197,8.931925,0.174787,-8.876920,-2.761043,1.128062,-1.261231,-6.929860,9.393761,6.643704,8.830882,-7.192736,-9.746142,-9.333763,-8.965722,-9.924411,2.432051,1.200418,-3.917856,-9.352997,-9.653320,-3.842703,-0.190117,-4.605833,-7.993259,6.108582,6.113484,2.585685,9.198547,6.336235,-9.759802,3.662838,1.430342,-4.331419,-7.528574,2.456311,-6.368593,4.494759,-3.946136,-0.333954,9.600940,-0.762453,-6.979290,9.655478,3.435592,0.555854,-4.411237,-4.995006,3.299449,5.247490,3.915007,-2.152586,3.547247,-7.009612,-6.343336,-3.567421,-9.278312,-0.350315,-6.375416,-0.077688,-6.567675,-3.040228,-2.929791,-6.544075,5.768543,0.802954,-8.465423,6.616327,0.825519,5.169912,-4.602517,-7.026785,-8.634360,2.800566,-0.515779,2.713871,3.122188,9.687262,-2.100830,2.336857,9.922033,-9.465033,7.870849,9.543105,1.164421,-4.745066,-4.135463,-0.069661,9.183439,-1.867560,5.650710,-1.838270,9.452372,0.302705,3.068257,3.651482,6.781176,8.934997,1.928838,-0.380716,7.387292,9.502940,0.119352,3.179878,3.078895,-5.275223,9.005389,-6.950077,-7.629486,-9.328305,-6.927005,-7.259738,4.391780,-3.627058,5.919666,4.838930,5.975291,-4.676578,-6.949869,1.437879,9.328182,-4.528361,-5.986658,4.661079,-5.225822,4.556660,-8.349472,9.765929,3.548366,-3.833994,-1.883879,3.257832,-3.887434,-3.533935,4.726422,1.359187,7.023561,5.837090,-5.956207,-4.597578,-0.813804,4.494036,1.279481,-1.554354,6.264235,8.667686,-1.944650,6.109545,0.309198,4.059104,-8.517724,2.511631,3.755626,8.491591,-8.791558,-1.117594,8.926887,9.951234,-6.596144,0.340285,-1.409792,4.295887,-8.783571,-2.998784,-8.474917,-3.604090,-4.640272,-7.802635,9.544929,7.308614,3.631169,-2.792830,7.133666,-8.850383,-3.285314,2.014457,-7.429509,1.134951,-3.317482,-3.636277,-9.397876,8.160569,5.227517,-7.035386,1.409569,-4.865306,4.271830,-9.368739,-5.390701,5.450417,-9.195549,3.892935,5.918252,0.065345,-7.899020,0.498375,3.255225,3.834578,-6.512074,9.865619,4.894390,1.875308,-2.929599,-6.661435,-6.990410,6.042157,-2.510407,8.457787,-7.993221,3.865403,6.818222,5.975714,9.852395,9.425509,-0.416210,-6.363235,-4.261719,-8.245404,9.195348,3.489877,-1.990692,-2.606771,1.860423,8.249767,8.999131,4.244196,5.994096,9.645852,3.643596,-2.811045,7.836392,-8.704320,-3.136235,-1.130073,1.541662,8.731633,7.639900,-3.375538,-6.283514,-9.106125,8.740043,-4.734927,-0.425597,3.389097,-7.382279,7.734671,-2.947489,3.130011,-7.624965,-3.303484,5.194948,-0.215200,-8.038007,0.637945,-4.228853,-0.160559,1.253541,-5.378726,-9.708829,-4.954578,4.698245,-9.918198,3.163470,3.308986,3.341203,2.850709,3.200984,1.559416,-6.870404,-6.172984,-4.338958,-0.453067,2.973493,7.239955,6.572084,-9.543060,6.684069,-2.509634,-6.136046,5.048151,-1.705248,-1.766065,-1.451844,4.285111,5.507785,2.813633,-7.408883,8.866790,-2.076097,0.947270,-8.817827,-7.501767,-5.715650,-2.633665,-9.237177,-0.710906,-8.078831,3.771422,0.005893,-0.487563,-4.540914,-8.913706,1.678194,1.236923,1.339314,0.182091,-3.713857,2.302997,1.842041,-0.013689,8.980534,-0.808985,9.934196,-5.131872,-8.341440,3.507248,-2.877960,0.657229,-8.439274,9.403117,6.453564,1.416899,0.731117,-8.334303,6.981500,-3.824575,7.453303,-9.804319,-9.640383,2.069115,1.729102,-8.151130,8.024932,-1.317974,-4.238752,3.709292,-3.242595,0.902136,4.278248,-6.987448,-9.875308,-3.694232,5.240161,6.753317,6.130808,-0.567306,0.044939,6.888568,-3.801733,-6.936309,3.560748,-7.801465,5.324242,1.086030,1.063097,8.191874,4.645978,-0.162753,-0.014564,-7.815592,-9.600620,9.016856,4.257882,-2.888262,-6.361670,-8.348536,-8.591126,3.199565,1.907014,4.989845,2.263584,-6.822335,-6.062856,9.123845,-8.635552,-3.944664,6.703885,7.721156,-5.040675,-8.137697,-2.749497,7.166141,-9.293133,-8.396800,3.315978,-8.642264,-0.722438,1.685929,9.379879,-3.907043,6.300645,5.570974,-9.539626,5.480904,-5.294560,5.668035,6.084302,-4.909543,4.343639,7.209274,-6.105847,6.592664,-9.895924,0.682801,-7.059903,-9.968676,-5.524590,-7.819991,-6.901480,-6.983451,9.621219,7.825166,-7.260618,-7.482479,7.975532,-1.132940,-0.674683,-0.978137,3.088029,-1.006007,6.714727,6.479552,-1.055034,-5.119330,4.598853,-5.808900,-4.730275,9.066938,5.932632,2.063327,8.420111,-4.411377,1.729341,1.901224,-4.162759,-0.843824,-3.377577,3.138821,8.594511,9.964546,-7.875626,-7.072371,2.925164,0.374635,2.094825,8.654220,8.148007,-8.574857,6.276385,7.564327,-4.124954,8.908716,3.190983,2.087137,9.267758,3.098765,-8.722551,-6.728416,-1.105415,-8.362142,-5.939543,-4.940706,7.391525,9.716763,-8.481188,-1.153360,-5.642046,9.932694,9.297070,2.343013,5.980607,-3.068587,-8.128083,-4.441021,4.221329,-8.991518,-0.881713,9.615460,-7.807628,-2.591664,3.595498,0.292421,5.073047,7.878412,7.570355,0.776449,9.291642,9.715330,-2.086900,-2.942033,-0.243135,-0.648946,-0.841618,6.858044,-1.293480,9.782670,-3.428045,5.598998,-9.485816,-3.617145,5.029835,-3.239690,-5.876614,-8.219120,2.623603,-5.085189,-8.841104,7.054117,-6.450432,4.115404,-7.567160,-1.351882,7.272856,-1.248188,-4.566027,4.013569,-0.557647,-9.496066,4.282606,-4.742615,-2.710777,4.344320,1.873966,8.388829,8.597820,-9.867032,9.121505,-2.523355,-5.513735,-0.932393,-1.918546,4.090171,-0.705695,6.440149,-1.027285,-9.584409,-1.379812,3.082481,-8.462593,0.988979,3.651759,-7.675511,-1.744604,5.626800,5.520487,9.477756,-4.469803,2.861514,-2.403226,-1.390033,-6.156310,2.257144,-8.797674,-5.245142,9.102194,-1.330093,1.809110,-6.244397,-7.434122,-6.627581,4.056371,8.739343,-6.308378,-9.542446,7.448230,-8.615986,-8.611948,-0.398078,-5.000032,0.539474,-1.341343,7.642085,-6.450812,2.715779,5.516216,9.304673,7.263482,-9.604252,3.089729,-5.433185,-5.988346,-5.328446,5.555295,4.633625,8.067182,0.231909,9.441124,8.485208,-1.465404,-0.894254,-6.110069,4.709440,-0.384415,-8.943847,-5.687091,-4.404738,3.467699,3.890365,7.826095,-8.722433,-3.732063,-7.732999,-1.767895,0.394266,-9.894544,0.596220,8.726540,-7.363814,-2.891109,1.655869,7.557297,6.146808,-8.388135,4.349602,-2.505238,-9.109072,-2.379099,-2.995883,-6.432204,4.222854,9.366257,-0.837157,3.151512,-3.628088,4.360716,9.914594,4.343615,9.782110,6.947858,8.974108,-1.642189,-4.320061,-9.547799,-8.403689,9.658118,5.504106,-8.990084,4.197555,-6.291804,5.172752,-8.807095,-4.146170,-3.622205,8.879296,1.567783,0.436642,6.345344,-6.812266,-2.664278,-8.986708,-5.497766,-1.608248,8.714037,3.823984,1.643742,9.368531,2.516134,9.859086,1.228525], dtype = "float64")#candidate|5542|(1408,)|const|float64
call_5541 = relay.TupleGetItem(func_5231_call(relay.reshape(const_5542.astype('float64'), [2, 704])), 6)
call_5543 = relay.TupleGetItem(func_5233_call(relay.reshape(const_5542.astype('float64'), [2, 704])), 6)
func_3165_call = mod.get_global_var('func_3165')
func_3169_call = mutated_mod.get_global_var('func_3169')
call_5548 = relay.TupleGetItem(func_3165_call(relay.reshape(call_5541.astype('float64'), [364,]), relay.reshape(call_5541.astype('float64'), [364,]), ), 2)
call_5549 = relay.TupleGetItem(func_3169_call(relay.reshape(call_5541.astype('float64'), [364,]), relay.reshape(call_5541.astype('float64'), [364,]), ), 2)
func_3529_call = mod.get_global_var('func_3529')
func_3531_call = mutated_mod.get_global_var('func_3531')
call_5555 = relay.TupleGetItem(func_3529_call(), 0)
call_5556 = relay.TupleGetItem(func_3531_call(), 0)
bop_5562 = relay.greater_equal(uop_5536.astype('bool'), relay.reshape(uop_5531.astype('bool'), relay.shape_of(uop_5536))) # shape=(11, 4, 16)
func_1071_call = mod.get_global_var('func_1071')
func_1075_call = mutated_mod.get_global_var('func_1075')
var_5581 = relay.var("var_5581", dtype = "float64", shape = (15, 364))#candidate|5581|(15, 364)|var|float64
call_5580 = relay.TupleGetItem(func_1071_call(relay.reshape(call_5548.astype('float64'), [14, 13, 2]), relay.reshape(var_5581.astype('float64'), [15, 364]), ), 3)
call_5582 = relay.TupleGetItem(func_1075_call(relay.reshape(call_5548.astype('float64'), [14, 13, 2]), relay.reshape(var_5581.astype('float64'), [15, 364]), ), 3)
uop_5583 = relay.rsqrt(uop_5522.astype('float64')) # shape=(11, 4, 16)
output = relay.Tuple([call_5541,const_5542,call_5548,call_5555,bop_5562,call_5580,var_5581,uop_5583,])
output2 = relay.Tuple([call_5543,const_5542,call_5549,call_5556,bop_5562,call_5582,var_5581,uop_5583,])
F = relay.Function([var_5516,var_5517,var_5581,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5516,var_5517,var_5581,], output2)
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
