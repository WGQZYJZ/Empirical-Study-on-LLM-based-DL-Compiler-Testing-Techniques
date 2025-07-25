import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_6 = relay.const([[[5.800993,5.332889,5.968585,6.908051,-8.088154,-2.621221,1.162595,-0.429671],[1.080332,9.382120,-1.992487,1.049276,-1.526979,-5.629038,-9.231706,-0.486534],[-4.013871,-9.127754,1.109032,0.622509,5.013132,-8.706219,-5.523603,0.306745],[5.850151,-6.902565,7.140313,7.516890,0.860415,-3.231372,3.613162,4.582606],[-0.099614,4.759994,7.354877,-9.315807,-5.528728,-7.474247,8.436455,-7.259722],[-0.141553,-4.019182,-9.709215,3.321321,3.616827,3.718967,-8.498983,9.382042],[0.183516,3.897171,4.702638,1.135579,-5.426549,-2.428521,3.580293,-2.341997],[-0.715845,1.109012,-4.685164,-0.052804,2.794469,-6.324493,-9.436703,-6.633256],[-8.284081,5.134273,6.713829,1.518159,-7.157533,9.583800,-2.928283,3.664175],[-9.206136,-9.770172,4.936607,5.145485,-1.511046,-0.786755,9.258432,-9.348103],[-6.549516,7.749065,-3.538950,-8.147869,-4.074577,2.666861,2.274791,9.477310]],[[1.873366,4.625951,-0.003611,5.883053,-7.790716,-7.437952,7.398947,-8.211629],[-1.605275,4.028905,-6.025121,9.022924,-8.655305,-4.962301,2.454353,0.923249],[3.022917,2.857114,7.451435,-3.884355,-7.091610,9.653820,-2.435904,-4.552548],[6.996883,2.866839,1.944357,0.892180,0.865766,8.021077,0.394152,-3.862671],[9.507562,5.131304,-8.319235,0.212548,-2.406800,-9.534268,-6.323489,0.731759],[6.672834,9.958235,1.871683,-1.194762,-5.784462,0.679778,-4.753740,-3.167419],[0.318128,4.878765,-0.949549,-5.469876,5.163710,2.633981,7.617999,-1.350892],[6.578916,7.661294,-5.887229,-3.832672,-3.126215,-8.960218,4.841815,-4.054525],[-1.836641,-7.226236,-1.001629,8.576487,-5.306915,2.938244,4.105935,-1.618294],[-8.597266,8.531121,8.819334,5.115624,8.052428,-5.881991,7.264928,9.204304],[-2.740445,-9.418163,3.684503,7.758690,-5.340266,9.818302,-9.966822,-0.558762]],[[-5.924830,4.062435,2.181913,5.351233,-2.914916,5.628478,-4.371559,-8.876007],[7.561399,-6.502113,-8.680456,-0.932817,-8.959971,4.480372,5.113339,7.375823],[5.922262,2.871707,-2.069686,-7.742786,-4.936521,-8.494887,-4.130259,-2.481648],[7.764371,-2.984403,-3.142718,-5.696338,2.121740,4.617452,3.678636,-3.078233],[0.151646,-4.230445,-2.342327,-5.644583,-3.945687,0.305696,2.197687,-1.070059],[-2.637294,7.672437,3.405264,-8.031002,8.222390,5.072605,-6.741888,7.040678],[7.364327,8.934388,-0.109592,4.575430,-9.211191,-0.691689,-4.493754,-0.816378],[8.828757,4.980122,8.677511,0.148229,6.525750,-4.623213,-4.346791,9.805636],[7.439888,9.815651,-3.375204,-0.537907,-0.038109,9.994629,-8.918387,4.706652],[1.080169,-3.233033,-4.600269,9.640788,7.910854,-3.393402,8.314813,0.664092],[-1.145013,8.808084,5.652166,-3.791564,-7.738106,-1.670546,4.490305,-2.135478]],[[-7.692376,-4.494590,3.767163,-9.344441,9.790199,-2.908402,-0.548532,8.506728],[7.690470,-3.742091,-6.093166,-1.259340,-3.044418,1.579621,-8.728989,-5.753844],[1.019566,-3.156120,-4.774049,2.225261,0.236660,-7.762970,3.848491,-0.263311],[-6.838663,-6.871966,0.701467,0.080956,4.306287,-9.066072,0.538670,3.994958],[3.344156,4.869025,-3.014744,6.575861,-8.552449,-0.630349,7.369588,-8.398646],[4.610402,-5.171525,4.923804,-3.391477,9.555733,5.702183,0.506628,7.626781],[-7.117065,-0.098931,3.552974,-4.339561,5.200758,4.915122,0.530799,2.643253],[-0.771336,-0.211482,2.175499,5.324701,5.815465,1.715873,5.674854,4.546061],[5.213172,-5.874642,9.284555,3.085617,4.308427,9.518798,-1.115582,6.369663],[-5.532857,1.543497,-9.517557,-4.630855,1.756739,-0.054793,-9.474694,-1.787101],[9.919335,-7.156106,3.796952,-3.018468,0.964732,3.175610,-1.123065,-5.701809]],[[-5.045458,-6.345033,-6.355861,-4.417143,3.199958,-1.432760,-5.011861,6.011936],[-1.584159,-3.138548,6.032093,-6.657513,-0.659581,9.333264,1.693781,-1.488974],[2.782321,-5.680038,2.906228,7.882439,-7.853492,0.330374,-8.661150,-7.113246],[-1.101627,-6.570731,7.355756,-3.400809,-2.618244,-4.320366,-0.894238,-0.907087],[-1.414700,3.708515,3.322254,-2.770380,8.486617,9.036777,-3.792748,-5.552739],[-2.113290,6.313633,6.869761,-7.770267,5.418497,5.379606,9.678078,5.624482],[1.653302,5.501840,0.844471,-9.650105,2.016890,-0.413058,1.955650,6.201357],[0.707319,-7.767751,-1.323452,-9.077205,1.342290,2.336341,9.074129,-1.091433],[-6.527043,-7.586670,5.532234,-3.965020,-8.821244,1.127845,3.371842,3.271504],[1.106599,7.463917,-9.010810,2.363880,-9.308124,-5.118973,1.974007,-9.216473],[5.030138,7.982446,7.443877,3.342986,-7.925265,0.408060,9.573702,-7.328616]]], dtype = "float64")#candidate|6|(5, 11, 8)|const|float64
uop_7 = relay.sqrt(const_6.astype('float64')) # shape=(5, 11, 8)
uop_9 = relay.sigmoid(const_6.astype('float64')) # shape=(5, 11, 8)
output = relay.Tuple([uop_7,uop_9,])
output2 = relay.Tuple([uop_7,uop_9,])
func_12 = relay.Function([], output)
mod['func_12'] = func_12
mod = relay.transform.InferType()(mod)
mutated_mod['func_12'] = func_12
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12_call = mutated_mod.get_global_var('func_12')
call_13 = func_12_call()
output = call_13
func_14 = relay.Function([], output)
mutated_mod['func_14'] = func_14
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_22 = relay.TupleGetItem(func_12_call(), 1)
call_23 = relay.TupleGetItem(func_14_call(), 1)
var_24 = relay.var("var_24", dtype = "float64", shape = (5, 11, 8))#candidate|24|(5, 11, 8)|var|float64
bop_25 = relay.maximum(call_22.astype('int8'), relay.reshape(var_24.astype('int8'), relay.shape_of(call_22))) # shape=(5, 11, 8)
bop_28 = relay.maximum(call_23.astype('int8'), relay.reshape(var_24.astype('int8'), relay.shape_of(call_23))) # shape=(5, 11, 8)
uop_30 = relay.exp(call_22.astype('float64')) # shape=(5, 11, 8)
uop_32 = relay.exp(call_23.astype('float64')) # shape=(5, 11, 8)
bop_56 = relay.greater(uop_30.astype('bool'), relay.reshape(var_24.astype('bool'), relay.shape_of(uop_30))) # shape=(5, 11, 8)
bop_59 = relay.greater(uop_32.astype('bool'), relay.reshape(var_24.astype('bool'), relay.shape_of(uop_32))) # shape=(5, 11, 8)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_72 = relay.TupleGetItem(func_12_call(), 0)
call_73 = relay.TupleGetItem(func_14_call(), 0)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_76 = relay.TupleGetItem(func_12_call(), 0)
call_77 = relay.TupleGetItem(func_14_call(), 0)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_85 = relay.TupleGetItem(func_12_call(), 1)
call_86 = relay.TupleGetItem(func_14_call(), 1)
output = relay.Tuple([bop_25,bop_56,call_72,call_76,call_85,])
output2 = relay.Tuple([bop_28,bop_59,call_73,call_77,call_86,])
func_89 = relay.Function([var_24,], output)
mod['func_89'] = func_89
mod = relay.transform.InferType()(mod)
mutated_mod['func_89'] = func_89
mutated_mod = relay.transform.InferType()(mutated_mod)
var_90 = relay.var("var_90", dtype = "float64", shape = (5, 11, 8))#candidate|90|(5, 11, 8)|var|float64
func_89_call = mutated_mod.get_global_var('func_89')
call_91 = func_89_call(var_90)
output = call_91
func_92 = relay.Function([var_90], output)
mutated_mod['func_92'] = func_92
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_195 = relay.TupleGetItem(func_12_call(), 1)
call_196 = relay.TupleGetItem(func_14_call(), 1)
output = relay.Tuple([call_195,])
output2 = relay.Tuple([call_196,])
func_206 = relay.Function([], output)
mod['func_206'] = func_206
mod = relay.transform.InferType()(mod)
output = func_206()
func_207 = relay.Function([], output)
mutated_mod['func_207'] = func_207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_230 = relay.TupleGetItem(func_206_call(), 0)
call_231 = relay.TupleGetItem(func_207_call(), 0)
var_240 = relay.var("var_240", dtype = "float64", shape = (5, 11, 8))#candidate|240|(5, 11, 8)|var|float64
bop_241 = relay.add(call_230.astype('float32'), relay.reshape(var_240.astype('float32'), relay.shape_of(call_230))) # shape=(5, 11, 8)
bop_244 = relay.add(call_231.astype('float32'), relay.reshape(var_240.astype('float32'), relay.shape_of(call_231))) # shape=(5, 11, 8)
func_89_call = mod.get_global_var('func_89')
func_92_call = mutated_mod.get_global_var('func_92')
call_245 = relay.TupleGetItem(func_89_call(relay.reshape(bop_241.astype('float64'), [5, 11, 8])), 2)
call_246 = relay.TupleGetItem(func_92_call(relay.reshape(bop_241.astype('float64'), [5, 11, 8])), 2)
output = relay.Tuple([bop_241,call_245,])
output2 = relay.Tuple([bop_244,call_246,])
func_251 = relay.Function([var_240,], output)
mod['func_251'] = func_251
mod = relay.transform.InferType()(mod)
var_252 = relay.var("var_252", dtype = "float64", shape = (5, 11, 8))#candidate|252|(5, 11, 8)|var|float64
output = func_251(var_252)
func_253 = relay.Function([var_252], output)
mutated_mod['func_253'] = func_253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_302 = relay.TupleGetItem(func_206_call(), 0)
call_303 = relay.TupleGetItem(func_207_call(), 0)
func_251_call = mod.get_global_var('func_251')
func_253_call = mutated_mod.get_global_var('func_253')
call_314 = relay.TupleGetItem(func_251_call(relay.reshape(call_302.astype('float64'), [5, 11, 8])), 1)
call_315 = relay.TupleGetItem(func_253_call(relay.reshape(call_302.astype('float64'), [5, 11, 8])), 1)
func_251_call = mod.get_global_var('func_251')
func_253_call = mutated_mod.get_global_var('func_253')
call_316 = relay.TupleGetItem(func_251_call(relay.reshape(call_302.astype('float64'), [5, 11, 8])), 0)
call_317 = relay.TupleGetItem(func_253_call(relay.reshape(call_302.astype('float64'), [5, 11, 8])), 0)
output = relay.Tuple([call_302,call_314,call_316,])
output2 = relay.Tuple([call_303,call_315,call_317,])
func_319 = relay.Function([], output)
mod['func_319'] = func_319
mod = relay.transform.InferType()(mod)
mutated_mod['func_319'] = func_319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mutated_mod.get_global_var('func_319')
call_320 = func_319_call()
output = call_320
func_321 = relay.Function([], output)
mutated_mod['func_321'] = func_321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_331 = relay.TupleGetItem(func_12_call(), 0)
call_332 = relay.TupleGetItem(func_14_call(), 0)
output = call_331
output2 = call_332
func_340 = relay.Function([], output)
mod['func_340'] = func_340
mod = relay.transform.InferType()(mod)
mutated_mod['func_340'] = func_340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_340_call = mutated_mod.get_global_var('func_340')
call_341 = func_340_call()
output = call_341
func_342 = relay.Function([], output)
mutated_mod['func_342'] = func_342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_343 = func_340_call()
call_344 = func_340_call()
var_349 = relay.var("var_349", dtype = "float64", shape = (5, 11, 8))#candidate|349|(5, 11, 8)|var|float64
bop_350 = relay.logical_xor(call_343.astype('int32'), relay.reshape(var_349.astype('int32'), relay.shape_of(call_343))) # shape=(5, 11, 8)
bop_353 = relay.logical_xor(call_344.astype('int32'), relay.reshape(var_349.astype('int32'), relay.shape_of(call_344))) # shape=(5, 11, 8)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_366 = relay.TupleGetItem(func_206_call(), 0)
call_367 = relay.TupleGetItem(func_207_call(), 0)
const_368 = relay.const([[[-5,-10,-3,-8,3,-1,6,-4],[-10,-2,-1,2,-9,1,9,7],[-5,4,-10,-8,-8,1,6,-6],[2,-9,-3,8,-4,-3,9,6],[1,-1,10,3,-10,-4,10,1],[10,-4,2,4,1,6,9,3],[2,10,3,2,6,10,-5,-9],[-10,9,2,-8,1,4,-8,2],[1,1,-3,-9,-10,6,-9,-2],[5,3,-5,4,-4,7,-5,9],[-9,4,-7,3,-2,-1,-4,-2]],[[-4,-10,-5,-4,3,1,8,-6],[4,9,4,7,2,9,-2,-7],[-7,3,1,2,-9,-2,5,-4],[-7,-8,-6,9,4,-4,-10,-1],[7,-10,3,10,5,7,-1,8],[-5,-1,3,10,7,-2,-4,3],[-8,2,6,-1,6,-2,-10,-5],[9,9,3,7,-3,6,-1,1],[-3,-1,4,10,2,7,4,-1],[5,3,9,-9,-9,2,-5,1],[5,-8,6,1,2,9,9,9]],[[10,-3,1,1,-8,-4,-5,4],[9,-1,2,2,-1,9,1,-3],[9,-9,-7,-4,1,-9,-5,8],[-2,10,2,-9,-2,-2,-8,5],[-8,-10,5,9,2,-4,-10,-2],[9,8,3,-4,-8,10,-1,3],[-9,4,7,-2,5,9,-6,8],[2,-9,-5,-9,-1,-7,4,-2],[5,7,-3,-2,-4,-2,1,-8],[-7,-7,3,-5,3,-7,-4,-9],[4,2,6,-6,4,-3,-9,9]],[[9,10,9,4,-1,-10,9,3],[-7,3,-8,6,-8,-10,-7,4],[-4,7,4,-7,4,8,-9,9],[8,9,-2,10,3,8,7,-7],[-8,6,8,5,-1,5,5,-5],[-9,-9,-1,-2,6,-4,2,6],[6,2,-5,5,-1,7,-8,9],[9,10,-6,4,-2,9,-2,6],[6,3,4,-7,-10,-10,-7,8],[8,7,2,-10,-2,2,1,-5],[3,-8,7,1,10,-8,4,-4]],[[-5,8,2,6,6,-9,4,-6],[1,-6,-9,-8,2,-7,-3,1],[-10,9,-9,-6,-3,-4,1,5],[-3,-2,2,3,-7,10,-1,-2],[-10,-5,-6,-3,-9,7,6,2],[7,-2,-6,-2,-7,-3,-5,-1],[5,-5,-8,1,7,7,-2,-3],[-5,-7,-9,-3,3,-5,2,7],[-4,2,3,9,-3,-3,7,3],[10,2,1,8,-1,4,10,3],[-4,-8,-8,6,5,-6,5,4]]], dtype = "int32")#candidate|368|(5, 11, 8)|const|int32
bop_369 = relay.bitwise_and(bop_350.astype('uint16'), relay.reshape(const_368.astype('uint16'), relay.shape_of(bop_350))) # shape=(5, 11, 8)
bop_372 = relay.bitwise_and(bop_353.astype('uint16'), relay.reshape(const_368.astype('uint16'), relay.shape_of(bop_353))) # shape=(5, 11, 8)
output = relay.Tuple([call_366,bop_369,])
output2 = relay.Tuple([call_367,bop_372,])
func_385 = relay.Function([var_349,], output)
mod['func_385'] = func_385
mod = relay.transform.InferType()(mod)
var_386 = relay.var("var_386", dtype = "float64", shape = (5, 11, 8))#candidate|386|(5, 11, 8)|var|float64
output = func_385(var_386)
func_387 = relay.Function([var_386], output)
mutated_mod['func_387'] = func_387
mutated_mod = relay.transform.InferType()(mutated_mod)
var_413 = relay.var("var_413", dtype = "uint32", shape = (1, 7, 6))#candidate|413|(1, 7, 6)|var|uint32
var_414 = relay.var("var_414", dtype = "uint32", shape = (7, 7, 6))#candidate|414|(7, 7, 6)|var|uint32
bop_415 = relay.greater(var_413.astype('bool'), var_414.astype('bool')) # shape=(7, 7, 6)
output = bop_415
output2 = bop_415
func_419 = relay.Function([var_413,var_414,], output)
mod['func_419'] = func_419
mod = relay.transform.InferType()(mod)
var_420 = relay.var("var_420", dtype = "uint32", shape = (1, 7, 6))#candidate|420|(1, 7, 6)|var|uint32
var_421 = relay.var("var_421", dtype = "uint32", shape = (7, 7, 6))#candidate|421|(7, 7, 6)|var|uint32
output = func_419(var_420,var_421,)
func_422 = relay.Function([var_420,var_421,], output)
mutated_mod['func_422'] = func_422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_447 = func_340_call()
call_448 = func_340_call()
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_449 = relay.TupleGetItem(func_12_call(), 1)
call_450 = relay.TupleGetItem(func_14_call(), 1)
bop_456 = relay.mod(call_447.astype('float32'), relay.reshape(call_449.astype('float32'), relay.shape_of(call_447))) # shape=(5, 11, 8)
bop_459 = relay.mod(call_448.astype('float32'), relay.reshape(call_450.astype('float32'), relay.shape_of(call_448))) # shape=(5, 11, 8)
output = bop_456
output2 = bop_459
func_471 = relay.Function([], output)
mod['func_471'] = func_471
mod = relay.transform.InferType()(mod)
output = func_471()
func_472 = relay.Function([], output)
mutated_mod['func_472'] = func_472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_597 = relay.TupleGetItem(func_206_call(), 0)
call_598 = relay.TupleGetItem(func_207_call(), 0)
output = call_597
output2 = call_598
func_610 = relay.Function([], output)
mod['func_610'] = func_610
mod = relay.transform.InferType()(mod)
output = func_610()
func_611 = relay.Function([], output)
mutated_mod['func_611'] = func_611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_645 = relay.TupleGetItem(func_319_call(), 0)
call_646 = relay.TupleGetItem(func_321_call(), 0)
output = call_645
output2 = call_646
func_655 = relay.Function([], output)
mod['func_655'] = func_655
mod = relay.transform.InferType()(mod)
mutated_mod['func_655'] = func_655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_655_call = mutated_mod.get_global_var('func_655')
call_656 = func_655_call()
output = call_656
func_657 = relay.Function([], output)
mutated_mod['func_657'] = func_657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_471_call = mod.get_global_var('func_471')
func_472_call = mutated_mod.get_global_var('func_472')
call_713 = func_471_call()
call_714 = func_471_call()
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_716 = relay.TupleGetItem(func_12_call(), 1)
call_717 = relay.TupleGetItem(func_14_call(), 1)
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_720 = func_340_call()
call_721 = func_340_call()
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_724 = func_340_call()
call_725 = func_340_call()
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_732 = relay.TupleGetItem(func_206_call(), 0)
call_733 = relay.TupleGetItem(func_207_call(), 0)
output = relay.Tuple([call_713,call_716,call_720,call_724,call_732,])
output2 = relay.Tuple([call_714,call_717,call_721,call_725,call_733,])
func_734 = relay.Function([], output)
mod['func_734'] = func_734
mod = relay.transform.InferType()(mod)
mutated_mod['func_734'] = func_734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_734_call = mutated_mod.get_global_var('func_734')
call_735 = func_734_call()
output = call_735
func_736 = relay.Function([], output)
mutated_mod['func_736'] = func_736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_787 = relay.TupleGetItem(func_319_call(), 0)
call_788 = relay.TupleGetItem(func_321_call(), 0)
output = call_787
output2 = call_788
func_815 = relay.Function([], output)
mod['func_815'] = func_815
mod = relay.transform.InferType()(mod)
mutated_mod['func_815'] = func_815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mutated_mod.get_global_var('func_815')
call_816 = func_815_call()
output = call_816
func_817 = relay.Function([], output)
mutated_mod['func_817'] = func_817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_655_call = mod.get_global_var('func_655')
func_657_call = mutated_mod.get_global_var('func_657')
call_821 = func_655_call()
call_822 = func_655_call()
output = call_821
output2 = call_822
func_853 = relay.Function([], output)
mod['func_853'] = func_853
mod = relay.transform.InferType()(mod)
output = func_853()
func_854 = relay.Function([], output)
mutated_mod['func_854'] = func_854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_874 = relay.TupleGetItem(func_206_call(), 0)
call_875 = relay.TupleGetItem(func_207_call(), 0)
output = call_874
output2 = call_875
func_876 = relay.Function([], output)
mod['func_876'] = func_876
mod = relay.transform.InferType()(mod)
mutated_mod['func_876'] = func_876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mutated_mod.get_global_var('func_876')
call_877 = func_876_call()
output = call_877
func_878 = relay.Function([], output)
mutated_mod['func_878'] = func_878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_916 = func_876_call()
call_917 = func_876_call()
output = relay.Tuple([call_916,])
output2 = relay.Tuple([call_917,])
func_923 = relay.Function([], output)
mod['func_923'] = func_923
mod = relay.transform.InferType()(mod)
mutated_mod['func_923'] = func_923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_923_call = mutated_mod.get_global_var('func_923')
call_924 = func_923_call()
output = call_924
func_925 = relay.Function([], output)
mutated_mod['func_925'] = func_925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_934 = func_815_call()
call_935 = func_815_call()
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_936 = relay.TupleGetItem(func_206_call(), 0)
call_937 = relay.TupleGetItem(func_207_call(), 0)
output = relay.Tuple([call_934,call_936,])
output2 = relay.Tuple([call_935,call_937,])
func_942 = relay.Function([], output)
mod['func_942'] = func_942
mod = relay.transform.InferType()(mod)
mutated_mod['func_942'] = func_942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_942_call = mutated_mod.get_global_var('func_942')
call_943 = func_942_call()
output = call_943
func_944 = relay.Function([], output)
mutated_mod['func_944'] = func_944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_1069 = relay.TupleGetItem(func_12_call(), 1)
call_1070 = relay.TupleGetItem(func_14_call(), 1)
output = call_1069
output2 = call_1070
func_1080 = relay.Function([], output)
mod['func_1080'] = func_1080
mod = relay.transform.InferType()(mod)
output = func_1080()
func_1081 = relay.Function([], output)
mutated_mod['func_1081'] = func_1081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_1087 = relay.TupleGetItem(func_206_call(), 0)
call_1088 = relay.TupleGetItem(func_207_call(), 0)
func_471_call = mod.get_global_var('func_471')
func_472_call = mutated_mod.get_global_var('func_472')
call_1094 = func_471_call()
call_1095 = func_471_call()
uop_1099 = relay.asin(call_1087.astype('float32')) # shape=(5, 11, 8)
uop_1101 = relay.asin(call_1088.astype('float32')) # shape=(5, 11, 8)
bop_1102 = relay.greater_equal(uop_1099.astype('bool'), relay.reshape(call_1094.astype('bool'), relay.shape_of(uop_1099))) # shape=(5, 11, 8)
bop_1105 = relay.greater_equal(uop_1101.astype('bool'), relay.reshape(call_1095.astype('bool'), relay.shape_of(uop_1101))) # shape=(5, 11, 8)
output = relay.Tuple([bop_1102,])
output2 = relay.Tuple([bop_1105,])
func_1117 = relay.Function([], output)
mod['func_1117'] = func_1117
mod = relay.transform.InferType()(mod)
output = func_1117()
func_1118 = relay.Function([], output)
mutated_mod['func_1118'] = func_1118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_853_call = mod.get_global_var('func_853')
func_854_call = mutated_mod.get_global_var('func_854')
call_1181 = func_853_call()
call_1182 = func_853_call()
func_734_call = mod.get_global_var('func_734')
func_736_call = mutated_mod.get_global_var('func_736')
call_1201 = relay.TupleGetItem(func_734_call(), 4)
call_1202 = relay.TupleGetItem(func_736_call(), 4)
output = relay.Tuple([call_1181,call_1201,])
output2 = relay.Tuple([call_1182,call_1202,])
func_1205 = relay.Function([], output)
mod['func_1205'] = func_1205
mod = relay.transform.InferType()(mod)
output = func_1205()
func_1206 = relay.Function([], output)
mutated_mod['func_1206'] = func_1206
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1207 = relay.var("var_1207", dtype = "float64", shape = (6, 1, 5))#candidate|1207|(6, 1, 5)|var|float64
var_1208 = relay.var("var_1208", dtype = "float64", shape = (6, 1, 5))#candidate|1208|(6, 1, 5)|var|float64
bop_1209 = relay.minimum(var_1207.astype('float64'), relay.reshape(var_1208.astype('float64'), relay.shape_of(var_1207))) # shape=(6, 1, 5)
uop_1216 = relay.acos(var_1207.astype('float64')) # shape=(6, 1, 5)
bop_1224 = relay.add(var_1207.astype('float64'), relay.reshape(var_1208.astype('float64'), relay.shape_of(var_1207))) # shape=(6, 1, 5)
func_655_call = mod.get_global_var('func_655')
func_657_call = mutated_mod.get_global_var('func_657')
call_1236 = func_655_call()
call_1237 = func_655_call()
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_1242 = relay.TupleGetItem(func_319_call(), 2)
call_1243 = relay.TupleGetItem(func_321_call(), 2)
output = relay.Tuple([bop_1209,uop_1216,bop_1224,call_1236,call_1242,])
output2 = relay.Tuple([bop_1209,uop_1216,bop_1224,call_1237,call_1243,])
func_1247 = relay.Function([var_1207,var_1208,], output)
mod['func_1247'] = func_1247
mod = relay.transform.InferType()(mod)
var_1248 = relay.var("var_1248", dtype = "float64", shape = (6, 1, 5))#candidate|1248|(6, 1, 5)|var|float64
var_1249 = relay.var("var_1249", dtype = "float64", shape = (6, 1, 5))#candidate|1249|(6, 1, 5)|var|float64
output = func_1247(var_1248,var_1249,)
func_1250 = relay.Function([var_1248,var_1249,], output)
mutated_mod['func_1250'] = func_1250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_1276 = func_815_call()
call_1277 = func_815_call()
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_1279 = func_340_call()
call_1280 = func_340_call()
func_1247_call = mod.get_global_var('func_1247')
func_1250_call = mutated_mod.get_global_var('func_1250')
var_1283 = relay.var("var_1283", dtype = "float64", shape = (5, 6))#candidate|1283|(5, 6)|var|float64
call_1282 = relay.TupleGetItem(func_1247_call(relay.reshape(var_1283.astype('float64'), [6, 1, 5]), relay.reshape(var_1283.astype('float64'), [6, 1, 5]), ), 1)
call_1284 = relay.TupleGetItem(func_1250_call(relay.reshape(var_1283.astype('float64'), [6, 1, 5]), relay.reshape(var_1283.astype('float64'), [6, 1, 5]), ), 1)
func_734_call = mod.get_global_var('func_734')
func_736_call = mutated_mod.get_global_var('func_736')
call_1288 = relay.TupleGetItem(func_734_call(), 0)
call_1289 = relay.TupleGetItem(func_736_call(), 0)
uop_1290 = relay.sigmoid(call_1282.astype('float64')) # shape=(6, 1, 5)
uop_1292 = relay.sigmoid(call_1284.astype('float64')) # shape=(6, 1, 5)
func_923_call = mod.get_global_var('func_923')
func_925_call = mutated_mod.get_global_var('func_925')
call_1322 = relay.TupleGetItem(func_923_call(), 0)
call_1323 = relay.TupleGetItem(func_925_call(), 0)
func_251_call = mod.get_global_var('func_251')
func_253_call = mutated_mod.get_global_var('func_253')
call_1327 = relay.TupleGetItem(func_251_call(relay.reshape(call_1276.astype('float64'), [5, 11, 8])), 1)
call_1328 = relay.TupleGetItem(func_253_call(relay.reshape(call_1276.astype('float64'), [5, 11, 8])), 1)
bop_1333 = relay.right_shift(uop_1290.astype('int16'), relay.reshape(var_1283.astype('int16'), relay.shape_of(uop_1290))) # shape=(6, 1, 5)
bop_1336 = relay.right_shift(uop_1292.astype('int16'), relay.reshape(var_1283.astype('int16'), relay.shape_of(uop_1292))) # shape=(6, 1, 5)
uop_1337 = relay.erf(bop_1333.astype('float32')) # shape=(6, 1, 5)
uop_1339 = relay.erf(bop_1336.astype('float32')) # shape=(6, 1, 5)
bop_1343 = relay.right_shift(call_1279.astype('int16'), relay.reshape(call_1288.astype('int16'), relay.shape_of(call_1279))) # shape=(5, 11, 8)
bop_1346 = relay.right_shift(call_1280.astype('int16'), relay.reshape(call_1289.astype('int16'), relay.shape_of(call_1280))) # shape=(5, 11, 8)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_1348 = relay.TupleGetItem(func_12_call(), 1)
call_1349 = relay.TupleGetItem(func_14_call(), 1)
uop_1350 = relay.atan(uop_1290.astype('float32')) # shape=(6, 1, 5)
uop_1352 = relay.atan(uop_1292.astype('float32')) # shape=(6, 1, 5)
const_1362 = relay.const([[[9.578934,-6.311287,3.525761,-9.613294,-9.561722],[-9.771882,-2.421557,6.215391,-2.578180,-5.274616],[7.194521,-6.815378,-6.737265,8.128036,-7.573674],[2.721167,1.746564,1.523922,-3.089991,0.783232],[6.492074,-0.804824,8.493327,9.630870,-2.777042],[8.519409,-8.169464,-3.901878,2.775620,4.667753],[-0.046343,8.891315,-1.410093,-0.650962,-5.598011],[1.963211,8.249308,0.015780,-5.854501,-5.948202],[4.818045,-5.937005,-1.968278,-9.161429,-7.259142],[5.909824,-3.007953,-2.158657,-3.339926,7.217918],[-0.590853,-2.302438,-2.525478,-7.554253,-4.760469],[5.728048,-8.185523,-3.922390,-2.076429,-6.743060],[-3.046491,5.641306,6.524856,2.919254,-1.333502]],[[-8.224865,3.909195,-2.720122,5.192317,-0.996605],[-6.801759,9.020720,-4.359826,8.577914,-5.270884],[6.424762,6.770549,9.573567,1.363715,-2.195099],[8.365838,-5.350176,9.557022,-4.150706,-5.452527],[1.816984,-0.131109,0.736986,-4.870506,3.584056],[7.657125,6.828009,4.953133,4.253766,0.092191],[-5.791873,-5.159195,6.133511,2.755444,-4.059238],[2.563231,-8.801492,-6.183975,-6.932621,-3.477713],[0.955760,-8.920329,6.242673,5.365315,-2.684018],[-4.558812,2.113876,-5.904508,1.174800,-4.693797],[3.806959,6.814800,5.822233,5.242299,-7.551099],[9.924802,6.131147,-7.953147,6.876922,3.838886],[-5.174556,-9.953020,4.071275,-9.865468,6.394894]],[[-1.393659,-9.162564,-7.401910,-9.518330,6.687112],[-2.066056,-9.473392,1.225184,-9.909891,7.838740],[-8.111371,0.986741,0.819411,6.766846,9.614115],[3.846975,3.135582,3.363799,1.219964,-0.998362],[-7.868319,-2.925163,-7.352063,0.727983,-6.229924],[0.554124,-4.306438,-9.394927,5.330172,-6.033139],[-2.761767,-2.126165,3.908635,1.525717,2.082574],[-3.868265,-4.077641,6.632447,-5.787170,9.527178],[1.196319,2.597536,-4.480649,1.461650,-7.316434],[-7.058212,5.574321,-8.177470,1.351608,-2.479675],[0.531065,-8.943160,0.442140,6.183425,7.010472],[-9.461138,8.133804,-6.374405,4.672467,0.371103],[5.745239,-3.168690,-4.520604,-4.304419,9.853036]],[[2.130090,1.325956,-1.556083,6.945265,-1.961061],[9.894911,2.463381,-6.482601,-1.944263,9.809208],[5.042006,7.759506,-2.438320,5.591529,4.764755],[1.513400,4.516827,4.979952,5.948781,2.266067],[6.092800,-4.505930,7.203149,-9.175873,9.998461],[5.962829,6.287659,-1.154493,3.674673,-7.775268],[-0.393964,6.027692,-9.133266,-4.337285,7.249842],[9.036599,-5.100688,1.173784,-4.088156,3.475763],[5.588402,6.484245,5.951212,-7.657337,5.470902],[-0.330587,-2.197831,6.719169,-0.994916,-5.071416],[-4.497821,-1.090820,-8.810810,-8.606128,4.359939],[-6.840966,7.153144,0.051105,2.912029,0.060934],[-9.929405,2.132549,3.967108,2.405343,-7.274056]],[[4.176462,0.425137,4.853388,2.314092,4.021714],[5.540275,9.383832,3.807001,7.168094,8.360581],[0.965070,-4.491171,-3.532990,5.769174,5.298339],[-5.852561,-0.262094,-7.940217,8.630101,-5.258720],[5.393489,-0.391362,-3.862851,8.207473,-7.274666],[-4.442433,0.183483,-4.736810,-3.474628,7.342728],[7.777127,-1.072920,-3.682032,1.147647,-6.598959],[-3.990640,9.654369,-5.482918,-0.205563,-9.587375],[-4.947538,-0.879665,9.566911,-2.505533,-2.188479],[-9.999215,2.053368,-6.164556,8.906040,4.496771],[5.026989,9.947935,-9.489387,-4.689032,-6.666755],[6.880575,7.036502,-3.660735,0.179829,-8.351068],[-3.300677,7.805817,5.609404,3.168186,-3.516007]],[[-6.898459,-5.219201,-6.138073,0.761137,7.037011],[6.878069,1.744468,-0.866302,-5.775735,-7.860883],[-1.483625,2.885058,-3.508936,8.881561,1.571210],[-2.267541,1.335123,-8.241129,4.328750,-4.040403],[0.250686,7.882950,-7.856572,-1.340648,5.097945],[0.642444,8.331984,-5.450820,8.487419,-2.333571],[5.493756,-5.549805,6.429229,-0.757040,-2.745617],[-6.567522,3.546525,-7.012687,7.987610,-9.439380],[4.866301,-7.762593,-2.750962,-0.340483,-8.908965],[-2.761080,5.011887,-4.455913,8.677916,2.086393],[6.562632,4.396114,-4.825956,-0.989362,-7.666670],[-6.631773,-0.817416,5.194262,2.270982,-2.151375],[-2.498063,9.232398,1.318948,-1.765468,7.786693]]], dtype = "float32")#candidate|1362|(6, 13, 5)|const|float32
bop_1363 = relay.multiply(uop_1337.astype('int16'), const_1362.astype('int16')) # shape=(6, 13, 5)
bop_1366 = relay.multiply(uop_1339.astype('int16'), const_1362.astype('int16')) # shape=(6, 13, 5)
var_1371 = relay.var("var_1371", dtype = "float32", shape = (6, 4, 5))#candidate|1371|(6, 4, 5)|var|float32
bop_1372 = relay.right_shift(uop_1350.astype('uint16'), var_1371.astype('uint16')) # shape=(6, 4, 5)
bop_1375 = relay.right_shift(uop_1352.astype('uint16'), var_1371.astype('uint16')) # shape=(6, 4, 5)
output = relay.Tuple([call_1276,call_1322,call_1327,bop_1343,call_1348,bop_1363,bop_1372,])
output2 = relay.Tuple([call_1277,call_1323,call_1328,bop_1346,call_1349,bop_1366,bop_1375,])
func_1377 = relay.Function([var_1283,var_1371,], output)
mod['func_1377'] = func_1377
mod = relay.transform.InferType()(mod)
mutated_mod['func_1377'] = func_1377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1377_call = mutated_mod.get_global_var('func_1377')
var_1379 = relay.var("var_1379", dtype = "float64", shape = (5, 6))#candidate|1379|(5, 6)|var|float64
var_1380 = relay.var("var_1380", dtype = "float32", shape = (6, 4, 5))#candidate|1380|(6, 4, 5)|var|float32
call_1378 = func_1377_call(var_1379,var_1380,)
output = call_1378
func_1381 = relay.Function([var_1379,var_1380,], output)
mutated_mod['func_1381'] = func_1381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_923_call = mod.get_global_var('func_923')
func_925_call = mutated_mod.get_global_var('func_925')
call_1386 = relay.TupleGetItem(func_923_call(), 0)
call_1387 = relay.TupleGetItem(func_925_call(), 0)
func_1247_call = mod.get_global_var('func_1247')
func_1250_call = mutated_mod.get_global_var('func_1250')
const_1398 = relay.const([-5.773897,-3.486398,4.319154,3.483880,1.453315,-8.510498,-0.294877,-7.725699,-0.647821,3.693507,2.725318,7.250448,7.652540,-9.424317,-7.490297,4.641795,-7.236336,3.769553,7.979327,-2.194948,7.159418,9.724426,-4.620104,-8.877424,-6.812439,-5.035792,-6.762369,-3.159925,-8.586256,6.026391], dtype = "float64")#candidate|1398|(30,)|const|float64
call_1397 = relay.TupleGetItem(func_1247_call(relay.reshape(const_1398.astype('float64'), [6, 1, 5]), relay.reshape(const_1398.astype('float64'), [6, 1, 5]), ), 1)
call_1399 = relay.TupleGetItem(func_1250_call(relay.reshape(const_1398.astype('float64'), [6, 1, 5]), relay.reshape(const_1398.astype('float64'), [6, 1, 5]), ), 1)
func_1247_call = mod.get_global_var('func_1247')
func_1250_call = mutated_mod.get_global_var('func_1250')
call_1408 = relay.TupleGetItem(func_1247_call(relay.reshape(const_1398.astype('float64'), [6, 1, 5]), relay.reshape(call_1397.astype('float64'), [6, 1, 5]), ), 0)
call_1409 = relay.TupleGetItem(func_1250_call(relay.reshape(const_1398.astype('float64'), [6, 1, 5]), relay.reshape(call_1397.astype('float64'), [6, 1, 5]), ), 0)
func_1247_call = mod.get_global_var('func_1247')
func_1250_call = mutated_mod.get_global_var('func_1250')
call_1414 = relay.TupleGetItem(func_1247_call(relay.reshape(call_1408.astype('float64'), [6, 1, 5]), relay.reshape(const_1398.astype('float64'), [6, 1, 5]), ), 1)
call_1415 = relay.TupleGetItem(func_1250_call(relay.reshape(call_1408.astype('float64'), [6, 1, 5]), relay.reshape(const_1398.astype('float64'), [6, 1, 5]), ), 1)
output = relay.Tuple([call_1386,call_1397,const_1398,call_1408,call_1414,])
output2 = relay.Tuple([call_1387,call_1399,const_1398,call_1409,call_1415,])
func_1416 = relay.Function([], output)
mod['func_1416'] = func_1416
mod = relay.transform.InferType()(mod)
output = func_1416()
func_1417 = relay.Function([], output)
mutated_mod['func_1417'] = func_1417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_1424 = relay.TupleGetItem(func_12_call(), 0)
call_1425 = relay.TupleGetItem(func_14_call(), 0)
var_1426 = relay.var("var_1426", dtype = "float64", shape = (5, 11, 8))#candidate|1426|(5, 11, 8)|var|float64
bop_1427 = relay.power(call_1424.astype('float64'), relay.reshape(var_1426.astype('float64'), relay.shape_of(call_1424))) # shape=(5, 11, 8)
bop_1430 = relay.power(call_1425.astype('float64'), relay.reshape(var_1426.astype('float64'), relay.shape_of(call_1425))) # shape=(5, 11, 8)
output = bop_1427
output2 = bop_1430
func_1431 = relay.Function([var_1426,], output)
mod['func_1431'] = func_1431
mod = relay.transform.InferType()(mod)
var_1432 = relay.var("var_1432", dtype = "float64", shape = (5, 11, 8))#candidate|1432|(5, 11, 8)|var|float64
output = func_1431(var_1432)
func_1433 = relay.Function([var_1432], output)
mutated_mod['func_1433'] = func_1433
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1440 = relay.const([[[10,7,-1,1,7,10,2,-1],[5,10,-9,9,-5,10,2,4],[-7,3,7,2,5,-10,-1,1],[8,4,-2,1,-2,1,-10,-5],[6,-6,10,-9,-4,-6,-1,-1],[-8,-10,-9,-10,-3,-2,-6,1],[3,-8,-9,-1,-7,8,-4,9],[-5,4,10,-3,-5,-8,-2,-4]],[[8,9,9,10,7,-4,-6,-2],[-3,-5,10,-6,2,5,-2,-10],[-1,8,9,5,-6,6,3,-5],[6,-9,-5,-1,-10,-1,-5,3],[-10,-5,-8,6,1,-6,-1,1],[10,-4,-5,-3,1,-7,7,-2],[2,-7,-10,-4,6,-5,10,6],[6,-4,7,7,-3,4,-6,-6]],[[-4,7,-7,-4,1,-4,5,-1],[-2,-1,-4,8,-3,-9,9,-7],[10,8,5,2,5,-8,-8,3],[-8,10,5,1,-10,-6,6,3],[-7,5,7,1,5,-2,2,2],[2,-2,-2,2,5,-3,3,-9],[9,4,1,-9,7,-1,9,-9],[-7,-5,-5,-1,6,3,9,10]],[[6,-5,-3,5,-6,-9,10,-3],[8,-6,-4,5,-8,-1,-10,5],[7,5,4,10,-6,2,-4,3],[-4,6,5,-10,-10,1,2,-6],[-8,8,10,-2,6,2,-1,-1],[5,5,-9,-4,5,-6,5,-7],[2,-7,-3,9,-4,-9,-8,-2],[-10,-3,-1,7,-6,5,7,-6]],[[-7,-3,1,2,-3,-2,5,-3],[8,-3,5,-9,3,2,-5,-8],[3,-7,-5,2,9,-8,6,9],[-7,7,2,-1,-7,4,-3,-6],[-6,-3,-1,-9,-8,7,8,10],[-10,-7,10,-7,3,10,-8,4],[-1,-4,-1,5,2,3,-7,7],[-9,-10,-2,-7,10,3,-6,-3]],[[4,-9,2,4,5,-6,-10,2],[9,10,10,-8,-5,-10,8,7],[-1,-4,-10,9,-6,10,9,-7],[5,-10,5,7,1,-10,-1,8],[5,6,-2,3,-1,-6,-6,-9],[-10,-7,-8,-4,2,-7,-3,6],[9,-5,5,1,-4,6,-9,2],[5,4,-4,2,4,-8,6,-5]],[[3,8,-10,6,5,4,9,5],[3,-9,10,2,3,-1,3,-4],[5,-6,10,-7,-6,-10,6,8],[7,-6,-9,10,-10,10,6,2],[3,-6,-2,7,3,2,5,9],[-9,10,5,9,3,-1,-3,-10],[-2,1,-1,-3,-8,-4,-7,4],[9,-4,-5,2,-4,7,-7,-6]],[[-5,-3,7,-1,-1,7,-7,3],[-4,2,10,7,8,-3,-3,4],[-8,-6,-10,-8,-3,8,6,8],[8,9,-8,4,-2,-3,-6,7],[-3,-6,2,-4,9,-5,-3,4],[4,9,-2,10,-10,3,9,9],[-2,4,9,9,2,-2,6,6],[9,-2,10,9,4,-5,1,-2]],[[9,9,4,5,-9,-10,-2,4],[4,4,-7,-2,-4,-1,-1,10],[-9,-7,6,-6,8,1,-2,1],[3,10,8,-1,2,-7,-7,2],[-7,-8,10,1,1,10,-9,3],[-8,-1,8,-9,6,-1,5,8],[10,-7,1,10,10,-9,-5,-10],[-5,9,5,-2,-6,-3,-6,-4]],[[-8,-9,-9,-4,3,9,-4,-8],[3,2,7,-8,-9,-5,3,-3],[10,-3,3,9,9,-1,-8,5],[10,9,3,10,10,7,5,-8],[2,-6,-9,2,-3,-4,-5,4],[6,1,-3,-1,8,-10,-10,10],[10,-8,8,-6,4,-6,6,-2],[-3,4,-8,1,-5,-1,-7,-8]],[[6,5,-7,-9,-10,-9,4,1],[-8,5,1,2,-7,2,7,-3],[7,8,-1,-4,1,9,7,-7],[6,1,-10,-5,7,2,-9,-6],[5,10,-1,6,10,-9,5,1],[8,1,6,-6,5,-8,5,1],[-8,-5,-7,-2,6,5,-9,-5],[8,-6,1,-9,10,-1,1,-4]],[[-2,9,1,6,5,3,8,3],[-3,2,9,-10,-9,3,-2,-9],[9,6,1,9,3,-2,-9,1],[-1,8,4,-10,-1,-3,1,9],[-1,-10,-7,10,3,5,8,6],[8,-1,3,5,6,7,9,-9],[-1,5,-10,-1,9,-6,9,6],[5,-10,-9,-2,-3,4,5,4]],[[-4,7,6,-6,-2,-1,4,10],[5,8,5,10,-9,3,10,1],[8,8,5,-8,8,-8,7,4],[8,-7,-1,2,-5,-5,2,-9],[-5,-4,-4,-7,-4,-7,-5,-2],[-4,-7,-7,-7,3,7,2,-8],[4,-7,-6,3,1,8,2,10],[-10,2,-5,-10,-5,-4,3,-3]]], dtype = "uint16")#candidate|1440|(13, 8, 8)|const|uint16
const_1441 = relay.const([[[10,9,9,7,-7,4,-3,7],[4,3,-4,9,-5,3,9,-2],[-7,-6,-8,-8,-5,-3,3,-10],[-5,-3,6,-8,9,1,-1,8],[3,-6,-4,8,-7,2,2,-7],[6,5,-1,5,4,-7,-8,-7],[-6,-1,-9,4,9,-6,-7,-7],[4,-5,9,-7,7,-2,-9,-5]],[[1,-7,-3,6,6,-3,6,6],[-6,-7,2,-9,-7,3,7,-9],[1,9,-7,-8,-7,-6,2,7],[10,4,7,10,-4,10,-10,-10],[-6,-7,-3,6,5,-7,3,-9],[-7,6,6,-7,-10,10,7,10],[-10,-6,1,5,5,7,5,2],[6,-5,5,-1,-1,2,-4,1]],[[1,-8,-1,-10,-4,-6,-2,-10],[-6,1,7,4,-6,5,-3,5],[-4,-8,-8,3,7,3,-6,8],[-6,-3,2,2,-8,-7,5,-4],[-4,6,-1,4,-6,7,-7,-6],[-3,-9,-8,4,-2,-6,-2,-6],[3,8,8,-3,-8,10,5,-2],[7,-5,4,3,-10,-3,-9,9]],[[-10,7,-9,-6,-1,4,-2,-6],[8,4,-3,-8,-5,-5,9,-6],[1,8,-4,-6,-9,-2,-7,-10],[2,-8,10,-7,-6,-7,6,-5],[9,-4,-8,-9,-1,9,-1,-4],[2,7,-8,5,9,-3,7,10],[3,-8,-6,-9,-10,-8,7,4],[-4,1,7,9,10,-9,-2,-5]],[[-6,-6,-2,3,3,-2,1,-10],[-7,8,9,-10,-1,-7,1,-6],[7,-1,-8,2,4,-2,10,-2],[4,-2,9,-3,-2,-3,-2,-10],[-2,-7,-5,-10,3,-6,7,-1],[-9,-4,-7,-1,7,2,3,-8],[2,3,-4,-8,8,-1,3,-6],[7,3,8,2,7,5,-5,5]],[[8,-9,-3,-1,-1,4,4,-6],[-1,-4,-2,4,-10,9,2,7],[2,-2,2,-3,-8,5,-8,-3],[-10,8,5,1,-1,-5,2,10],[-9,-8,10,2,-2,-9,9,-1],[-1,9,1,3,10,-2,1,8],[-8,9,-10,5,-1,4,6,-7],[6,-7,7,8,10,-10,4,1]],[[6,2,-4,-2,1,2,-1,8],[-8,4,-5,-3,-2,5,2,-10],[5,-8,10,3,4,-1,-6,-4],[-4,-2,-1,-3,9,-1,-4,-1],[4,10,-7,-7,8,-10,9,-3],[-4,-3,9,10,-5,-8,5,-2],[9,2,2,-1,-9,9,4,-10],[-4,-5,-10,8,7,8,7,10]],[[-9,4,-4,-6,-5,-9,-6,7],[-4,2,9,-3,7,-8,-1,-2],[1,-6,10,-7,6,6,-7,-1],[-7,-8,2,-1,-3,5,7,6],[5,4,3,-2,7,10,-1,6],[-3,-4,-6,-6,-6,-6,-10,3],[-6,3,-10,10,-3,5,1,-3],[8,9,-2,4,8,3,4,-5]],[[6,-2,3,6,-2,3,2,6],[-3,3,-10,5,9,-5,-5,3],[-8,-6,7,-8,-2,-10,5,4],[3,-3,-6,-2,-6,8,-7,1],[-6,-6,-2,1,5,8,-9,10],[-2,6,3,1,-5,9,9,-9],[10,9,-2,-5,10,-1,-8,3],[-5,-7,9,6,-6,9,-8,4]],[[6,9,2,8,-7,-2,-9,-4],[8,-1,-9,2,-5,-5,-9,-10],[-10,4,-2,5,1,-6,-4,5],[4,-10,4,-2,-5,1,-6,1],[-1,-10,-7,-4,-4,-9,3,-2],[-1,-9,6,-5,10,7,8,-4],[2,1,10,-8,-6,-5,-10,-5],[3,5,7,2,-7,-3,-4,-5]],[[10,-6,3,-7,8,7,2,8],[-8,-7,-4,-10,6,7,10,-8],[7,-5,5,-9,-5,-2,10,4],[-6,3,-8,2,-8,-5,8,1],[5,-6,-7,5,5,10,-1,5],[3,-7,3,-4,6,-1,5,2],[5,2,4,3,7,5,6,-5],[-10,-10,10,5,-7,4,6,2]],[[3,1,-3,7,8,8,-1,-2],[5,-3,-8,-5,-5,-7,-5,10],[4,5,8,7,-3,-7,-10,-5],[-3,-2,-9,7,5,2,-4,-8],[-6,6,-7,9,8,6,6,-4],[2,-3,-2,4,6,-9,-10,9],[-2,-1,7,-10,-7,4,-10,4],[6,-2,8,8,-3,6,-6,9]],[[-1,-6,10,3,2,1,-8,1],[-2,4,2,6,9,-7,7,2],[8,-6,3,6,-9,-5,-3,2],[-3,7,-10,-9,5,3,-3,1],[2,2,9,1,6,-6,2,6],[8,-9,6,-7,-7,6,7,3],[-5,5,4,1,-1,1,-8,-9],[10,-3,9,1,10,5,-3,7]]], dtype = "uint16")#candidate|1441|(13, 8, 8)|const|uint16
bop_1442 = relay.subtract(const_1440.astype('uint16'), relay.reshape(const_1441.astype('uint16'), relay.shape_of(const_1440))) # shape=(13, 8, 8)
bop_1447 = relay.floor_divide(const_1441.astype('float64'), relay.reshape(bop_1442.astype('float64'), relay.shape_of(const_1441))) # shape=(13, 8, 8)
output = relay.Tuple([bop_1447,])
output2 = relay.Tuple([bop_1447,])
func_1451 = relay.Function([], output)
mod['func_1451'] = func_1451
mod = relay.transform.InferType()(mod)
output = func_1451()
func_1452 = relay.Function([], output)
mutated_mod['func_1452'] = func_1452
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1471 = relay.const([[[-8.690591,-5.692539,7.048025,3.896661,-1.180102,6.900956,3.985238,-7.135246,-5.455305,3.907470],[-8.646912,-1.862862,1.565431,-1.214602,9.298361,-7.513417,-5.344214,-3.693495,5.021800,7.253856],[1.478362,-5.111052,0.191260,-0.775316,4.265417,6.305711,5.171139,7.972999,6.600045,-5.375200],[7.499783,-7.611704,-3.389932,3.022585,-2.300369,3.597407,8.449659,-5.679381,-0.050442,9.320882],[9.053084,3.196437,-8.282391,9.720094,4.734786,-4.447343,-5.537756,-9.181837,-0.212144,-6.022005],[-5.033842,-4.029271,5.569805,0.125523,6.395108,6.154892,7.284500,-7.050939,2.045083,7.451405],[9.648752,2.985076,-7.259430,-7.514351,-7.344731,9.132520,-4.512776,-9.219881,9.469411,-1.824592],[-1.994417,2.915359,-3.418987,-5.065586,4.434614,-8.860296,0.920705,-0.740488,7.135179,-4.021778],[8.905126,4.023032,-2.793149,4.577716,5.151629,-0.217654,-9.166618,3.112666,6.584806,-4.560374],[-5.266596,-9.019220,7.985107,0.737204,0.178349,-0.733084,-6.901699,9.557791,1.526837,-4.958553],[-9.790918,7.780448,-5.911775,7.975079,-2.223926,-7.132849,1.747197,-4.300929,0.758496,5.959590],[-7.243416,5.128847,7.275847,0.494726,6.856732,3.700512,-5.191028,-4.781449,-0.771295,6.470573],[-7.323341,7.763247,-7.015413,-9.277351,9.236254,-3.641421,4.951410,-1.616058,-3.359074,2.756346],[3.204901,3.895499,7.449025,-1.934167,-2.781573,-0.208013,9.660079,-4.525693,-6.021124,0.866426],[-4.296366,3.180478,8.888935,2.895633,9.244057,-5.166345,0.693598,-0.412247,7.143125,-7.619183],[-3.399026,-7.374159,-7.936788,3.727351,9.517342,5.347347,8.768979,8.397963,-2.212206,-1.482650]],[[-6.089499,0.924672,0.943180,-2.646138,-5.296882,-2.833652,-5.185183,6.997244,9.546771,3.488746],[8.009176,-9.273218,5.621281,-6.179146,-5.069478,3.234265,7.874515,3.596166,-7.234453,5.577237],[-8.230148,-9.522243,8.591349,-2.537595,-1.120281,8.673617,-4.272645,-6.532866,-3.575109,2.262485],[-4.749196,8.346883,2.746223,-1.912812,-8.171665,9.063813,4.256107,4.014305,0.304662,0.391192],[7.207888,3.019614,-6.144839,7.052006,-2.633058,-7.830002,3.000079,-7.575941,-2.668919,2.522803],[8.964959,2.948925,-2.000803,2.282178,-8.058736,9.484630,9.633839,9.638442,0.098294,-3.311326],[-2.348850,-9.846978,-6.811158,-4.029543,2.343333,-8.969459,-9.681434,5.640121,-3.659810,-3.006396],[3.280643,1.617856,4.032449,-6.767922,7.622765,-3.260915,9.516286,-7.057971,-4.072075,-2.738081],[-8.037617,-2.149361,0.450719,2.231694,-8.816465,-3.564839,5.013105,-7.759946,1.199526,9.197242],[-5.042516,-5.090042,-0.161413,0.032638,6.269812,-6.602982,-1.350178,0.258062,-1.837953,-8.304701],[-5.970178,-2.085873,-5.762437,-0.589855,-1.891525,-9.943253,-2.016368,-3.123807,6.875627,4.545743],[-5.168784,-7.730014,-6.978107,-7.274766,-3.922141,1.922320,6.327851,3.295044,-8.110889,7.419237],[8.911881,2.226034,-9.818992,1.935106,-1.108439,4.384202,-0.617915,5.638486,3.492134,-3.897625],[-1.518372,-4.860139,5.792068,6.468816,-1.054685,-7.592567,4.286801,9.190923,-0.031215,5.061451],[2.338033,0.207030,1.778951,-6.718999,-1.982493,-9.785772,-8.617721,-0.062129,-9.806752,1.486886],[5.812708,8.252743,-9.404640,-7.823268,5.589045,7.689758,-2.610170,-1.972592,6.970055,-3.248656]],[[6.977227,8.736228,-3.407063,-1.227611,9.966326,6.925880,7.204321,7.850498,6.652739,-5.971430],[-5.455125,2.203176,-9.301330,-5.716855,-3.068517,4.209852,7.599192,3.551463,5.868953,5.308231],[9.496792,1.286371,8.198729,-8.402697,-1.824262,1.051203,-9.770110,-3.106606,-0.980501,9.085854],[9.201336,4.396038,6.723616,-8.390949,-0.520485,8.369428,-9.888654,-2.362824,-1.719531,-4.995188],[-3.415079,0.948247,-4.860615,8.515335,-6.817952,1.361322,-3.803995,-3.334963,1.594617,-8.502519],[-3.633091,-7.575308,-7.680301,-8.548080,1.855603,4.490247,-8.062511,5.086852,-3.365090,-7.594602],[6.526351,7.544286,-9.798607,9.326243,-3.342366,2.095068,2.390209,-3.295213,-0.189489,-2.731704],[6.055450,4.449488,-1.039624,5.483782,-7.285254,6.805787,8.526783,4.751477,8.689394,-2.016053],[-1.876665,-7.663599,8.423010,7.826934,-5.499305,5.133490,9.053944,0.371551,3.764317,6.391640],[-2.798511,2.326724,8.387162,8.409909,1.304132,-0.655839,6.225047,-7.825956,9.264120,2.268053],[2.008093,-7.599050,9.343139,3.441233,-9.371556,-7.804795,3.762317,-6.066331,-5.536553,2.717789],[5.297862,3.557841,7.673241,5.782837,5.501176,-0.608573,-1.001786,-1.327553,-3.006934,-0.503127],[-6.548601,-2.899679,6.168325,-4.063295,-4.323126,2.355243,4.760230,0.041709,-6.195844,-3.865411],[8.763027,2.269492,4.139838,2.634571,7.113943,-7.790861,7.128966,8.992845,8.799633,-0.536738],[-3.371566,-0.801815,2.297000,-4.699902,-3.272663,4.663774,0.627024,1.058697,-8.724024,-8.932692],[5.290186,0.166217,9.912482,8.475252,-2.238619,5.919259,3.849488,6.942644,8.417693,0.646767]],[[-6.363591,6.646455,7.145146,-2.967408,0.965902,9.484609,5.007489,7.734418,1.011135,1.234493],[4.451338,-3.430296,-6.970731,2.834963,9.506125,-5.133225,4.338575,6.406452,-9.499533,7.418572],[1.973752,-0.126283,3.163509,7.463632,-1.088412,1.866590,5.754668,8.923905,9.530597,8.711001],[2.580147,-8.479709,4.369652,7.098272,6.786105,-3.632925,8.271535,3.802027,-2.728964,8.370554],[6.466559,-8.618765,1.810320,5.246737,-4.019562,9.816913,-1.915258,3.126539,-8.013620,9.855261],[6.528093,-9.105074,8.866192,0.925729,-8.852355,-3.060393,7.308964,2.278579,-9.949865,0.667990],[5.622966,-6.202924,-9.366485,-3.173488,-3.154061,-4.845195,5.945418,-8.544900,-2.199704,-4.734150],[6.737949,4.708887,-6.132589,0.461252,5.777257,5.066254,0.271192,-8.471743,1.806167,-4.535311],[-9.214270,7.477722,7.950709,-3.053988,-8.532873,4.307723,-7.640690,-9.212709,3.879637,5.069340],[9.500226,3.726382,3.123310,-2.117122,-3.994703,-5.802806,-9.623561,-5.715462,-6.210552,9.019553],[-4.289601,-5.151829,8.613578,2.673775,-2.552319,6.275611,3.409341,-2.716480,-5.945565,-5.566168],[-1.088047,-7.240678,-9.880968,-6.250403,4.913965,6.507874,-2.316637,-1.928816,6.549730,-8.683307],[8.608864,5.218411,9.817893,1.605446,-8.810028,-3.744420,-2.382035,2.598297,-7.448559,5.684161],[-5.906644,7.374109,-7.245859,-7.716779,8.837649,2.982890,2.532452,2.260647,0.017257,-4.947277],[-1.322899,-0.073691,9.403888,-2.085467,6.687051,-2.614320,-0.810672,5.556773,4.436280,-6.376107],[-2.735261,2.710239,-2.662398,-2.504404,9.056783,-9.937813,-1.372508,8.739582,-3.482004,0.657514]],[[3.522580,4.236303,5.396189,0.199211,2.472276,3.500769,8.832393,6.815994,7.286348,2.856883],[-0.040397,0.707047,-2.474845,6.363660,-4.606326,4.774287,-5.543576,1.799516,1.658374,-0.716506],[2.912967,-2.621111,5.357843,-8.467315,-3.889821,4.468819,3.479295,4.448521,0.603226,3.399160],[0.035436,-7.459887,9.639415,0.347520,-4.724978,0.497800,4.606736,-7.371442,9.669601,0.002907],[2.681415,5.758066,1.240030,-2.461593,7.350390,-6.866001,-2.840674,-4.149004,1.633641,-2.873662],[4.779360,3.768931,-6.933081,0.614227,-1.491361,2.602214,-8.415342,5.162731,7.712327,-0.386356],[7.861905,1.838113,9.316734,5.412081,3.226518,-1.909890,-6.606032,0.606395,-4.176332,-3.565800],[5.343922,-0.370210,-3.096219,-3.503249,5.372704,-2.358635,3.246588,3.646219,1.890029,6.185258],[-2.455127,-4.886560,0.452901,8.622596,-0.266540,4.734526,5.496833,2.377809,7.977178,3.932649],[6.253303,0.654853,9.874803,3.540908,1.823397,7.928385,0.151756,-8.685900,4.193385,-9.716935],[-8.552901,-9.807766,8.121347,1.102289,8.680768,5.732902,3.985337,8.573440,1.326267,8.845342],[-4.808273,2.769272,-0.843570,-5.149553,6.516835,-0.790840,-5.292816,-3.676587,-7.679739,-6.689324],[-7.913234,-8.027672,-0.725250,6.854792,7.408573,0.706613,2.853779,4.007324,-6.959605,-3.469381],[-2.790005,7.736458,9.825108,-5.296563,-3.829311,7.664604,-5.497095,-8.109281,2.724317,7.249075],[-5.453723,-3.846067,1.573503,-1.912902,-2.634055,8.057908,0.650277,3.573734,-6.551376,-4.024345],[7.483389,-6.255779,-8.284571,-2.101124,-4.131056,-6.184163,-5.002038,-4.914299,-1.238986,-8.940922]],[[1.839492,6.510474,-1.890610,8.802731,-4.809569,4.559062,1.883925,4.349581,-6.848961,-0.217902],[7.144971,-7.382982,0.950354,5.149615,0.336308,-4.505023,-8.281475,6.517338,4.465336,7.729865],[-6.456887,3.342570,-5.747662,2.325290,-7.927835,8.330773,-9.770797,-1.271812,0.553206,6.971868],[8.909290,2.242870,5.832692,-7.430516,-7.662548,-4.019772,8.496527,-0.270683,4.449623,-9.159455],[3.006497,8.157304,6.003597,-6.461455,-6.345669,7.743428,3.967437,2.983260,5.803245,4.694198],[0.288746,3.265190,6.159295,3.085225,6.857758,3.478206,2.425015,3.333587,-7.496436,5.454281],[9.487887,-6.619372,-0.735608,-8.957242,7.845080,4.413083,5.670128,8.106294,-7.876556,1.335000],[1.230386,1.403129,-3.600179,6.590601,-9.613478,8.873294,-1.044080,-4.165742,2.656340,-0.246048],[3.569710,8.925147,-4.592869,5.680005,8.339492,2.710725,6.549995,-2.500963,3.790103,-3.394347],[-0.711992,8.137043,1.326504,8.916376,-1.882710,-5.234250,9.540826,1.947134,-1.946257,9.762825],[4.513312,-3.292744,0.267749,-4.558892,7.553443,-3.700193,-0.169339,-9.461644,0.909446,-8.024732],[7.291218,2.615645,2.885608,1.226610,-8.893069,1.739600,4.348845,-3.093413,-8.426075,8.303324],[-7.575433,-9.667327,2.788991,-5.436915,-6.263829,6.092142,4.552554,8.773543,0.923417,9.835941],[0.094680,7.363457,-7.372499,0.277550,2.653636,-0.520427,-7.085722,-9.932243,0.956396,-2.163486],[-7.628404,-1.983522,4.562356,-2.037964,-0.317320,-4.270620,-0.136048,-5.789784,5.429691,-6.734720],[-8.120486,-3.930175,1.734463,-1.897205,-7.274176,-2.354952,-1.034026,-9.908130,-7.247791,-0.444978]],[[-0.255813,-1.329775,8.133120,-5.710635,-2.153848,8.343239,6.369353,6.650546,-4.707701,-4.898885],[1.006570,7.856529,5.831416,5.407878,-7.460766,-6.342462,-7.630017,-9.592992,4.036507,-7.229007],[1.298713,-7.681509,-3.046786,0.638842,2.134825,1.063378,-0.634541,3.089731,-1.536744,-8.472064],[-6.361548,-4.254421,6.460134,-1.113806,9.106297,3.211559,-8.007563,5.276833,7.178719,-2.272448],[-7.174219,2.438776,-5.128732,-9.582781,9.172516,-3.636275,1.818298,-2.234847,6.409174,4.435683],[-3.101050,4.414417,-3.076395,8.020037,6.286899,0.808171,9.327791,-3.618639,1.867411,-2.534367],[4.207552,-6.673313,3.362723,-1.467930,-1.784379,3.641663,-6.766192,6.142891,-8.044437,-3.522504],[-2.905371,8.056997,3.804644,-9.029005,4.280255,2.319953,3.507784,0.652274,9.119950,8.116068],[-2.298587,-5.824802,2.435938,8.848080,-3.121595,4.383563,2.069210,-7.555653,-4.880793,9.520491],[9.778552,9.072940,0.292241,-3.862471,-7.220932,-2.532724,-2.195616,1.412986,-1.105592,7.109517],[-3.426186,-4.954595,-8.104965,-3.119703,3.995844,-4.522942,0.374195,5.004009,-6.111222,8.738683],[1.211026,0.167776,-0.509953,0.057253,-8.052939,9.571780,9.506064,-2.752741,-9.307061,-1.593556],[3.017291,-7.728671,-4.481281,6.801398,6.566132,0.288106,-9.699502,1.291069,0.167816,6.314664],[8.212616,5.840210,-5.918828,-0.083629,-4.208361,-7.330585,3.312056,-3.130309,-7.362539,4.978363],[-7.855068,-4.149514,1.453700,4.411900,-5.400754,-8.923981,5.751143,-0.095179,-4.258260,-3.530993],[-6.423222,-0.471704,-5.514606,7.039737,-0.014236,-5.475472,-5.769255,9.143660,-1.538244,-2.534121]],[[4.139175,9.264998,-5.927915,7.183091,-8.003938,-7.981194,-7.472053,3.284414,1.675110,-7.611762],[5.168422,1.545946,6.832729,9.971749,9.199364,3.976874,1.206880,-5.089590,-8.559418,-2.631895],[8.185465,7.973267,5.789215,-1.703877,-8.302890,-6.133220,-6.862481,4.686273,-0.403481,0.996561],[-3.014221,-9.302607,2.873193,-6.093022,-0.010373,1.171534,6.485797,-8.325492,1.498417,7.544651],[3.511699,4.683464,3.855762,6.395019,4.115829,-3.864489,2.023815,1.811759,7.507997,5.530934],[-3.976080,9.893358,0.373481,-4.755503,7.164360,-1.849028,0.521443,-7.617559,-0.986184,-1.420891],[-7.472314,-4.880451,-6.756559,2.453098,4.379109,8.410927,5.115398,4.499195,-3.195515,5.441774],[6.414901,-2.218144,8.690439,-3.466326,3.264204,2.154889,0.566300,2.913658,-5.500731,7.097365],[9.107553,6.147728,6.692138,-1.070624,0.932516,7.475400,5.275880,2.429946,-2.893930,2.606348],[6.055581,-2.626640,-0.581451,-4.350793,-2.447107,-5.455560,-5.045378,-9.704431,-9.997653,-7.000754],[-3.526977,-5.590568,5.581571,-5.170146,3.003697,4.337076,-9.173578,1.517319,-7.360057,1.653595],[4.075031,-1.476054,-7.472805,-6.322065,1.407652,-9.621884,-1.093442,-6.333412,-4.467894,-2.819152],[-6.735665,-0.894522,4.367564,6.555483,3.259222,-3.718262,-1.588401,1.549427,0.322318,5.912349],[-2.045338,-5.339798,-9.478009,-9.111482,1.035022,0.572527,6.221168,-0.721636,1.863333,-4.420530],[1.532678,-9.124373,8.784530,-8.466441,7.662241,-0.092611,7.452770,-3.455195,8.765960,-3.526156],[7.587916,-4.722283,-8.165380,7.401421,-8.360560,-6.622712,-2.721042,7.917323,-0.362084,-3.168832]],[[9.793576,3.769834,0.013546,-3.912352,6.748661,3.360915,-9.048032,7.880000,5.999246,2.743007],[-0.394762,1.988353,-1.759072,-0.479135,-0.762928,-6.425355,0.246174,-2.109706,8.505014,6.600789],[1.541926,-0.871461,-9.646714,-5.028303,-2.320202,6.901698,-5.098889,-5.222983,8.734878,0.750018],[2.301273,3.836464,-0.505494,-8.310141,8.158986,-2.585094,-7.218772,-8.931428,-2.756314,-9.437850],[-5.940245,4.271787,-0.802045,4.219368,-7.025679,8.945232,-2.261535,1.057566,-8.185793,7.924468],[3.829261,1.575610,-5.564782,1.351821,-6.153885,7.762262,1.836148,2.287570,-9.177907,-8.566055],[-9.506584,1.527681,-9.980892,8.350685,-6.719867,-5.139318,-8.453564,6.531920,-6.137697,9.940609],[0.694328,0.492541,1.186332,-2.392665,-3.258881,-6.812587,5.767859,3.448152,-9.288211,-9.791323],[4.212638,7.726128,-3.412074,-2.920301,7.393574,-3.872146,8.298633,1.754154,-7.576035,-5.487611],[-6.615072,0.361507,-7.927679,-0.620266,7.733755,5.234420,3.256534,-4.986535,-5.649816,-7.568829],[-2.047809,-3.769091,1.714065,-1.253675,7.896759,-5.999991,-1.024830,3.434703,-2.429847,3.063752],[5.627288,8.397225,8.795021,-9.357985,-4.230851,9.858233,8.486491,-7.000568,-8.843775,9.232628],[-9.834640,7.320075,5.049429,1.353613,-7.686439,-3.180750,-9.055635,3.103434,2.480376,4.698525],[-6.924708,7.874477,-8.684552,-2.040418,-2.801646,-0.942094,9.140473,4.266700,4.241713,9.046964],[-4.281345,8.808059,0.846432,-5.919036,-6.087273,-9.776983,0.841439,9.230011,-5.520626,-9.634921],[4.675287,0.634020,-9.877381,6.532544,7.104812,-6.865296,-3.071084,-4.075413,-9.607297,5.945993]],[[-6.412841,7.303176,9.734972,4.685153,0.294176,-0.398949,3.046458,0.847681,0.235716,2.380473],[0.174528,-5.606259,0.847346,9.929620,1.202808,-9.051122,7.976992,6.162868,-6.860875,-2.016882],[-8.620195,-3.216513,-8.475240,-3.555982,8.845023,-7.888638,8.100740,-9.824323,-0.731021,-3.992752],[-4.039870,8.909996,-5.180443,-3.430083,-3.918946,-9.431645,-0.126505,-5.515811,6.296249,-0.370475],[-0.513603,9.767993,1.705559,-4.686549,-3.258554,2.749819,8.047733,-7.224980,-4.112316,3.617175],[8.057557,0.287850,-0.628778,-7.984195,-6.592004,-2.421989,3.659044,-6.240480,-2.034873,-2.047008],[6.411117,7.564480,3.123573,1.488414,9.952216,-2.532951,-7.021219,-2.253960,3.368920,-6.713148],[2.147698,-4.062612,7.494577,2.069902,5.878164,-1.858098,1.629535,0.448349,6.084712,-9.865375],[9.340890,7.052909,3.668503,0.326286,-8.442646,-2.544823,-3.751124,-9.225704,-1.970478,0.692408],[-8.116537,-9.840677,-5.773858,-1.413164,-3.043028,-5.947508,4.412729,-0.361690,8.495066,4.435738],[4.820993,0.627031,-6.093222,8.484380,4.864065,-6.961610,-5.104570,9.870206,-5.560828,-3.444132],[3.107332,2.075542,-7.571663,4.783996,2.866337,1.220513,-4.711554,-2.331890,9.639585,5.318267],[6.871752,-2.707402,3.135072,-1.969277,2.844366,-7.528027,1.285422,2.519653,1.455364,5.320067],[9.073957,-2.303608,7.471317,-7.893334,-2.509891,2.337250,7.508750,-6.304278,5.071275,-5.989045],[5.177037,2.355302,-9.322681,1.636730,2.609012,-2.640740,1.554927,3.341213,-8.512637,1.549219],[8.298361,-3.406368,-7.241027,7.661835,6.773949,-4.083394,0.196852,3.531445,-6.451374,3.947357]],[[3.790079,-5.982749,-1.040497,4.786254,0.809101,-1.272558,3.236420,8.285334,1.947418,8.442733],[2.389443,0.117502,-0.882611,-8.316029,2.914233,-6.716608,-3.738064,-9.825372,-4.163888,7.663504],[-2.173908,6.483350,-9.358792,-3.412289,0.939474,-3.269230,6.438965,7.612780,-3.361804,9.169305],[-6.955766,-0.327888,-0.875543,7.977975,-7.464434,4.750235,-1.679749,-9.422710,1.209454,-7.815511],[-3.617495,4.495497,1.307861,3.301994,9.983576,5.295132,9.712510,-9.460804,-4.181029,-9.151358],[-5.815750,-4.021959,-1.645855,1.479757,9.355075,0.667750,-9.547341,4.688948,2.105375,7.221113],[1.472833,-8.246975,-0.725699,0.965692,3.890316,5.562044,4.418535,-5.236946,-0.768777,9.286135],[-8.541355,8.791602,-4.735156,-4.824088,-9.874973,-4.840221,-8.374403,-5.105295,0.565588,-3.513285],[3.405443,-1.751463,6.243774,1.655653,-2.409928,2.179900,0.166119,8.955022,6.828484,1.508746],[2.132230,-3.863410,2.663223,-8.692145,-7.969746,7.592549,-5.867637,-2.067331,-3.051997,5.543753],[-4.071247,2.913173,4.866544,8.334798,-8.479379,-4.081900,-1.279129,-5.782905,9.058305,-3.163845],[3.244477,-9.730796,6.067092,9.084011,-1.274617,-0.831611,5.750784,-1.678596,-1.621491,7.344198],[-1.246299,-4.270463,-0.077453,-8.550484,2.763541,1.582037,-2.989072,-6.673642,-7.525984,-1.951652],[-0.173842,-6.416425,-0.366954,4.234263,-0.766433,-5.045813,-1.848749,-3.350254,7.404299,0.276887],[1.210935,3.692214,-2.075089,-1.314596,2.200869,9.576607,3.197980,8.298333,-5.770253,4.599445],[1.972097,2.529230,-1.451877,6.732857,0.438749,8.281494,2.966076,-5.171194,-2.450152,4.742604]],[[2.363593,-6.524531,-1.104365,7.172604,-4.081568,3.103059,-3.215623,3.409637,-5.921276,-7.517041],[0.317275,3.142858,-8.158439,-7.613056,-9.973417,-6.248178,-2.122756,-3.228622,-3.651473,1.345181],[-5.921034,-3.497105,-2.605315,-7.153647,-8.044583,-3.769892,-5.539495,4.000010,4.666668,0.478900],[2.929077,-1.191174,-3.400379,-0.370417,-6.231531,9.732658,-3.477506,4.890956,-6.349133,-7.899103],[-4.982897,-7.233912,-7.055620,6.910354,-2.764776,9.000018,-4.750839,9.853591,-6.379346,2.562344],[-5.128481,-4.605622,-3.708469,2.482239,4.995737,-8.709008,-0.882126,-9.924841,-3.719146,-8.390695],[-2.349176,-8.647482,5.277978,-4.941651,1.498635,-4.529280,-6.879779,-0.002078,-3.888532,6.820729],[2.475482,5.524519,5.966672,-3.547518,6.646739,-1.810114,-3.158048,-9.291566,-8.009651,-8.775970],[-3.780748,8.047298,2.035391,-8.537653,7.766530,5.693940,7.342207,-2.231212,-5.331820,-4.031126],[-7.117401,6.786623,8.037976,-0.057414,-8.282764,4.941466,-6.347894,-4.535087,-9.893559,8.202213],[-2.754181,8.876403,-5.264013,-6.647862,-1.301479,-7.059656,7.217770,-7.891205,-8.690540,2.955783],[7.413564,9.456067,2.278266,9.588015,-4.825177,-0.794476,6.185776,-5.185818,7.641675,-8.660075],[6.022217,-2.040860,-6.902799,4.810279,-9.386213,-7.362065,8.716341,1.725059,6.160342,7.343920],[1.227274,-1.844369,1.875948,-7.186548,-2.478408,-3.636196,-2.904563,-3.700904,0.374382,7.979635],[-2.951002,4.436408,3.373432,7.305685,8.564260,7.243574,-4.145807,2.406243,-0.813627,-4.999950],[-0.136672,0.938962,-7.927778,-6.460711,2.956666,0.273800,0.282967,-4.618872,9.867332,3.720557]],[[-9.067712,9.674012,-2.716372,-5.064255,2.727913,5.826025,5.297467,-1.930744,4.885076,-2.946485],[-1.163425,-2.986738,-2.401770,-4.295164,-3.224444,2.395868,-0.887757,1.471331,5.366756,-2.713952],[3.372103,6.326211,-2.845621,-0.278979,-0.814948,-6.741949,-5.910134,-5.148233,4.874703,-1.527837],[-4.993245,-1.269014,-2.411828,4.664588,9.387315,-7.456334,-8.629599,-1.298463,7.272352,-7.804792],[8.730179,-3.504669,7.721627,-9.641566,-7.616287,7.601847,-4.180361,7.217297,2.393454,6.307234],[-6.048610,9.368472,3.132211,4.802189,-3.938088,-5.409886,9.290125,3.627425,5.020780,5.930630],[-0.522691,-5.536494,0.352197,-9.505648,-0.596509,1.023819,1.159045,8.184781,-2.839022,-4.427500],[-6.721219,-4.839688,8.730547,9.230640,-5.918767,-5.718129,6.462289,8.440991,9.216218,2.440939],[3.449404,-0.982646,-2.689488,8.237709,1.241831,6.952952,-2.094849,6.274473,-1.779295,-1.149725],[4.584138,0.330413,0.910398,1.221493,-5.180542,3.357097,-6.284032,5.703664,9.244222,6.833480],[-6.412335,8.896023,9.076954,-0.210550,9.449971,-3.684646,-7.267176,6.446496,-0.746305,-4.189972],[6.991710,1.828869,1.387177,-3.715652,0.303201,6.210832,6.640110,8.429705,9.426804,-3.232770],[-7.327838,-0.043178,-9.431584,1.463887,-3.120436,-4.293708,5.629230,9.070120,-2.612138,1.065288],[-9.218680,7.148727,2.592182,-9.965906,-4.720422,3.591995,7.652302,7.282564,1.478879,-0.770123],[-9.977197,-6.650696,-2.422696,6.824395,2.299600,8.306575,5.281822,8.770233,7.130115,-5.998842],[-0.320632,-7.230980,2.928705,-8.915109,-7.147679,-5.786878,8.037681,-6.783494,4.135853,-4.682038]],[[5.792795,-9.799570,-1.164452,4.479606,9.182086,1.263094,-7.058707,7.897745,-7.449968,-6.097111],[-7.730193,7.898849,3.026105,-4.933909,9.643748,-6.931972,-8.971194,-9.379496,-5.373677,-8.131395],[5.346200,-2.418089,8.057124,9.883799,1.912679,5.939264,-6.694544,6.989149,-7.883505,-3.129482],[-5.611444,-4.962724,6.055405,5.826338,3.250274,2.606269,7.533802,-5.413646,3.434416,-7.918539],[3.846814,8.466456,1.051118,-8.301994,-0.786037,5.955377,0.445715,2.887026,-3.719302,-9.990315],[-9.378002,-9.163612,1.719233,-4.300892,-8.950805,2.040827,-5.890076,-7.057383,0.847684,-2.467511],[4.450318,-4.282067,2.725191,-7.122558,-6.907044,7.943856,-4.462588,9.665173,-1.945084,0.623045],[-9.043769,7.850174,3.496181,-0.909710,-5.786442,-2.442498,7.328825,-0.779806,-5.784303,-2.444426],[4.298256,5.296473,-3.092731,-9.771791,-4.259311,3.451473,-3.736859,-0.067472,-3.881941,6.828563],[8.110474,1.712544,-4.996667,8.504016,-7.443257,-0.354695,-7.831022,0.442416,-5.579405,9.051264],[7.342558,3.170922,8.306579,9.996702,3.819283,-2.274033,-8.680899,1.252855,5.085528,4.920651],[-7.855665,-0.592722,4.287747,6.283560,0.964635,5.432680,-6.977486,-5.144233,-0.317858,6.343790],[-2.124080,-8.982750,1.562610,-8.422813,-9.592308,-9.410805,7.765075,9.894350,2.390104,-8.094217],[-0.501755,6.758924,-4.526971,-1.826243,-7.264078,-9.154850,-0.371234,2.920303,-5.819519,-1.297898],[-5.122045,-6.209276,1.884559,-9.867378,-1.209965,7.783656,-0.777426,4.817482,7.087131,1.755000],[-1.800464,-6.834336,-5.662037,-4.256309,6.193886,-9.875937,-6.349550,0.815424,-6.136774,-0.027339]],[[-8.300713,3.614108,-8.683079,-8.946273,3.021140,0.336190,3.160566,-5.562099,-4.999749,4.561284],[1.784652,2.670829,-1.879373,-6.099227,-0.381127,7.437354,-0.046705,-9.656687,-8.559694,-9.091911],[-1.410237,4.517401,-8.508926,-5.326539,-4.431593,-9.102877,2.663514,8.378068,3.131788,-9.622955],[-1.771476,-0.593350,6.918209,-2.445124,3.876998,6.575334,-9.173128,-5.185716,-8.454824,8.574888],[-6.650362,-0.049377,2.905332,9.069464,9.831974,4.681155,4.567981,2.625297,-3.774034,-7.189068],[-5.377462,6.551134,-3.609031,8.906326,-3.926034,-1.373776,7.467452,-0.763157,-7.212957,6.493976],[-2.660054,-1.797216,-9.363927,-0.190028,9.782765,7.680268,-1.842132,-9.190448,-6.808709,3.520384],[4.219465,9.075380,-9.768794,5.478643,3.152587,0.737585,1.896420,3.728311,6.990145,-6.774280],[1.960508,-2.421449,3.289997,-1.089283,7.204299,-3.076596,6.139557,1.426607,-0.931845,6.369666],[1.042643,1.980732,-0.115371,-3.119120,-4.829526,-8.400765,-4.330880,8.282677,0.986779,0.617896],[9.797980,4.235032,6.232226,-9.981548,-0.013383,1.073357,-2.769179,-4.535802,-3.957605,-3.701965],[-3.947729,-3.815079,-7.731147,-3.915300,0.425214,-7.320365,7.723581,-2.697733,-8.420729,-5.429940],[-0.455557,-9.001478,-9.022459,9.134472,3.716996,6.283439,-7.085814,3.102842,9.887440,-6.850706],[4.313400,4.918894,2.061822,-6.485833,2.663372,-7.049808,-0.849640,-1.152422,4.624044,8.725915],[-1.070721,-3.263540,-0.838422,8.796909,8.215979,3.250644,-8.410603,-6.158858,-0.332036,3.708508],[3.024097,2.954536,-2.584733,1.663792,4.424328,-5.479286,8.033031,-9.484024,-6.645835,-1.129548]]], dtype = "float64")#candidate|1471|(15, 16, 10)|const|float64
uop_1472 = relay.rsqrt(const_1471.astype('float64')) # shape=(15, 16, 10)
output = uop_1472
output2 = uop_1472
func_1483 = relay.Function([], output)
mod['func_1483'] = func_1483
mod = relay.transform.InferType()(mod)
output = func_1483()
func_1484 = relay.Function([], output)
mutated_mod['func_1484'] = func_1484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_471_call = mod.get_global_var('func_471')
func_472_call = mutated_mod.get_global_var('func_472')
call_1507 = func_471_call()
call_1508 = func_471_call()
output = call_1507
output2 = call_1508
func_1512 = relay.Function([], output)
mod['func_1512'] = func_1512
mod = relay.transform.InferType()(mod)
output = func_1512()
func_1513 = relay.Function([], output)
mutated_mod['func_1513'] = func_1513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_1539 = relay.TupleGetItem(func_206_call(), 0)
call_1540 = relay.TupleGetItem(func_207_call(), 0)
output = call_1539
output2 = call_1540
func_1544 = relay.Function([], output)
mod['func_1544'] = func_1544
mod = relay.transform.InferType()(mod)
output = func_1544()
func_1545 = relay.Function([], output)
mutated_mod['func_1545'] = func_1545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_942_call = mod.get_global_var('func_942')
func_944_call = mutated_mod.get_global_var('func_944')
call_1558 = relay.TupleGetItem(func_942_call(), 0)
call_1559 = relay.TupleGetItem(func_944_call(), 0)
func_610_call = mod.get_global_var('func_610')
func_611_call = mutated_mod.get_global_var('func_611')
call_1565 = func_610_call()
call_1566 = func_610_call()
var_1570 = relay.var("var_1570", dtype = "float64", shape = (5, 11, 8))#candidate|1570|(5, 11, 8)|var|float64
bop_1571 = relay.bitwise_xor(call_1565.astype('int64'), relay.reshape(var_1570.astype('int64'), relay.shape_of(call_1565))) # shape=(5, 11, 8)
bop_1574 = relay.bitwise_xor(call_1566.astype('int64'), relay.reshape(var_1570.astype('int64'), relay.shape_of(call_1566))) # shape=(5, 11, 8)
const_1576 = relay.const([[[-1,6,-5,-7,9,-5,-5,8],[-3,10,-6,5,6,-1,-4,-6],[-5,-9,1,3,10,-4,-2,10],[9,-3,8,-8,3,-3,8,-10],[-4,-5,-6,2,-6,-10,9,6],[-2,3,-10,-6,2,7,-1,-3],[9,7,-8,-3,7,5,-3,-4],[-9,-7,-9,9,2,-1,5,7],[4,1,-7,8,-8,-8,1,8],[-2,-10,-7,2,7,4,9,-7],[-9,7,-3,-8,8,-5,-1,-3]],[[-9,-3,2,-8,1,2,-7,-7],[9,2,10,6,9,9,4,2],[4,10,3,6,1,-5,1,5],[-7,4,9,7,1,8,9,1],[-5,1,10,-1,-7,9,10,8],[1,7,3,-7,-10,-2,-5,2],[3,-8,-1,3,-9,4,6,-7],[5,8,7,-2,10,-6,6,-5],[-1,3,-3,-10,9,-2,-7,4],[4,-9,9,8,5,4,-5,-2],[3,-10,4,-1,-5,9,-1,-3]],[[-7,5,-6,-5,8,4,-10,2],[4,2,-10,-10,-5,9,4,-10],[-6,8,10,1,-5,-3,-3,-8],[7,-4,2,-3,5,-4,4,1],[-1,-10,-2,-10,7,-2,8,-7],[10,1,-7,1,-4,2,-9,8],[4,10,8,-3,-3,5,-4,8],[6,-8,-4,7,-3,8,4,3],[-1,-3,5,5,-10,-1,5,-8],[9,-5,6,2,3,-3,-3,4],[-1,4,3,-6,-2,-7,8,-1]],[[1,9,8,-7,1,-9,-6,10],[-1,1,-6,7,6,6,-9,-1],[2,8,-1,-4,-4,-7,-7,-6],[-1,-2,-6,4,7,5,8,-6],[4,-2,-10,-7,9,-5,-9,5],[-1,-7,-10,-8,5,-2,-9,-5],[4,-10,-6,-1,1,3,8,-1],[7,-6,9,5,-7,-8,7,1],[-1,-8,-8,-1,-4,10,-2,-10],[7,9,10,-3,-3,5,-2,-3],[-7,-9,-1,-3,-3,-8,-4,-6]],[[-4,10,-9,1,1,1,-4,6],[7,-6,6,-3,4,5,-10,10],[8,-8,-10,10,-6,-5,-7,-2],[8,1,1,2,7,-5,8,1],[-7,4,9,-1,7,7,-8,-8],[-9,8,-5,9,-8,1,2,-4],[2,-6,-4,-5,-4,-6,-1,1],[-5,4,-1,-4,-7,-7,-8,8],[10,10,-3,-8,-9,-3,9,4],[3,6,1,3,6,9,-2,5],[-2,-8,1,-6,-10,-1,-1,3]]], dtype = "int64")#candidate|1576|(5, 11, 8)|const|int64
bop_1577 = relay.divide(bop_1571.astype('float64'), relay.reshape(const_1576.astype('float64'), relay.shape_of(bop_1571))) # shape=(5, 11, 8)
bop_1580 = relay.divide(bop_1574.astype('float64'), relay.reshape(const_1576.astype('float64'), relay.shape_of(bop_1574))) # shape=(5, 11, 8)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_1586 = relay.TupleGetItem(func_1416_call(), 2)
call_1587 = relay.TupleGetItem(func_1417_call(), 2)
func_853_call = mod.get_global_var('func_853')
func_854_call = mutated_mod.get_global_var('func_854')
call_1591 = func_853_call()
call_1592 = func_853_call()
func_251_call = mod.get_global_var('func_251')
func_253_call = mutated_mod.get_global_var('func_253')
call_1598 = relay.TupleGetItem(func_251_call(relay.reshape(const_1576.astype('float64'), [5, 11, 8])), 1)
call_1599 = relay.TupleGetItem(func_253_call(relay.reshape(const_1576.astype('float64'), [5, 11, 8])), 1)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_1604 = relay.TupleGetItem(func_1416_call(), 4)
call_1605 = relay.TupleGetItem(func_1417_call(), 4)
func_610_call = mod.get_global_var('func_610')
func_611_call = mutated_mod.get_global_var('func_611')
call_1606 = func_610_call()
call_1607 = func_610_call()
const_1609 = relay.const([[[5,-1,-3,-3,-4,-4,1,3],[-8,-2,7,7,-4,-3,-1,6],[-9,6,-7,4,9,2,7,9],[6,-8,-3,-8,-1,9,-1,10],[3,-1,-5,4,4,6,-5,-7],[-6,-1,-10,-6,-1,-5,-4,-2],[2,-9,-10,-1,-3,8,-1,7],[1,-6,9,4,-1,-4,-7,-3],[-2,6,-9,8,5,8,-2,3],[6,-4,5,7,-8,-2,7,-6],[10,-1,-8,-1,-7,-8,5,-2]],[[-3,6,-6,-6,3,-1,-5,-1],[8,6,-3,10,-5,8,-10,-2],[9,-4,2,3,-10,-8,-3,4],[1,9,6,-5,-6,4,5,2],[4,3,6,9,-2,2,6,-9],[5,-2,-5,-5,-9,-10,3,-10],[-8,10,9,-7,-8,8,-5,2],[3,3,10,1,-5,6,3,-4],[9,4,-5,10,-1,9,5,6],[-7,6,-6,-7,-1,8,8,-6],[6,-6,-10,4,7,5,-5,10]],[[9,9,6,-6,-10,-1,-8,7],[7,-5,-4,-6,2,-2,4,1],[9,-1,-8,2,-3,6,1,5],[9,-5,-1,-3,-4,-2,-9,6],[-4,5,-5,-8,1,2,-9,10],[-9,2,-5,6,2,-10,2,-10],[-4,-6,1,9,-10,-4,10,-9],[-8,-2,6,2,6,2,9,-2],[-7,2,-4,2,6,3,1,-6],[10,1,5,-7,-7,-9,-1,9],[-3,7,-6,9,8,-7,-3,9]],[[-2,-1,-6,-8,-9,1,-9,-9],[-5,-10,-7,2,-1,6,3,-7],[-6,10,9,8,6,-8,-2,-9],[-3,-10,10,-8,3,4,9,-9],[-2,-8,-10,8,6,2,3,6],[2,8,8,-2,-2,-6,-2,6],[7,-6,10,2,-10,-5,8,8],[-7,-4,4,5,6,5,-8,1],[-6,-10,-1,-2,9,-3,-9,10],[9,9,2,9,7,4,-6,-1],[-2,-7,-5,5,6,-2,-8,9]],[[6,1,5,-4,4,10,-4,2],[-1,-8,-10,2,-10,-1,7,-8],[-1,1,-10,10,4,6,10,4],[7,-10,7,-4,-6,-7,-6,-8],[-5,3,-7,-1,-3,-8,7,4],[8,-2,6,1,-1,-5,-3,-4],[-3,4,-1,10,4,-7,-4,6],[3,-4,-3,10,-3,-1,-9,5],[-5,3,-5,-10,-3,-1,-7,6],[4,10,-6,1,9,-6,-6,-2],[9,9,-8,-5,5,5,-3,-4]]], dtype = "int64")#candidate|1609|(5, 11, 8)|const|int64
bop_1610 = relay.less(const_1576.astype('bool'), relay.reshape(const_1609.astype('bool'), relay.shape_of(const_1576))) # shape=(5, 11, 8)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_1622 = relay.TupleGetItem(func_1416_call(), 4)
call_1623 = relay.TupleGetItem(func_1417_call(), 4)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_1627 = func_1431_call(relay.reshape(call_1558.astype('float64'), [5, 11, 8]))
call_1628 = func_1431_call(relay.reshape(call_1558.astype('float64'), [5, 11, 8]))
output = relay.Tuple([call_1558,bop_1577,call_1586,call_1591,call_1598,call_1604,call_1606,bop_1610,call_1622,call_1627,])
output2 = relay.Tuple([call_1559,bop_1580,call_1587,call_1592,call_1599,call_1605,call_1607,bop_1610,call_1623,call_1628,])
func_1633 = relay.Function([var_1570,], output)
mod['func_1633'] = func_1633
mod = relay.transform.InferType()(mod)
var_1634 = relay.var("var_1634", dtype = "float64", shape = (5, 11, 8))#candidate|1634|(5, 11, 8)|var|float64
output = func_1633(var_1634)
func_1635 = relay.Function([var_1634], output)
mutated_mod['func_1635'] = func_1635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mod.get_global_var('func_1483')
func_1484_call = mutated_mod.get_global_var('func_1484')
call_1653 = func_1483_call()
call_1654 = func_1483_call()
uop_1661 = relay.sinh(call_1653.astype('float64')) # shape=(15, 16, 10)
uop_1663 = relay.sinh(call_1654.astype('float64')) # shape=(15, 16, 10)
uop_1664 = relay.atan(uop_1661.astype('float32')) # shape=(15, 16, 10)
uop_1666 = relay.atan(uop_1663.astype('float32')) # shape=(15, 16, 10)
func_853_call = mod.get_global_var('func_853')
func_854_call = mutated_mod.get_global_var('func_854')
call_1684 = func_853_call()
call_1685 = func_853_call()
func_89_call = mod.get_global_var('func_89')
func_92_call = mutated_mod.get_global_var('func_92')
call_1686 = relay.TupleGetItem(func_89_call(relay.reshape(call_1684.astype('float64'), [5, 11, 8])), 3)
call_1687 = relay.TupleGetItem(func_92_call(relay.reshape(call_1684.astype('float64'), [5, 11, 8])), 3)
output = relay.Tuple([uop_1664,call_1684,call_1686,])
output2 = relay.Tuple([uop_1666,call_1685,call_1687,])
func_1688 = relay.Function([], output)
mod['func_1688'] = func_1688
mod = relay.transform.InferType()(mod)
mutated_mod['func_1688'] = func_1688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1688_call = mutated_mod.get_global_var('func_1688')
call_1689 = func_1688_call()
output = call_1689
func_1690 = relay.Function([], output)
mutated_mod['func_1690'] = func_1690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_1698 = func_1544_call()
call_1699 = func_1544_call()
output = relay.Tuple([call_1698,])
output2 = relay.Tuple([call_1699,])
func_1713 = relay.Function([], output)
mod['func_1713'] = func_1713
mod = relay.transform.InferType()(mod)
output = func_1713()
func_1714 = relay.Function([], output)
mutated_mod['func_1714'] = func_1714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1732 = func_1080_call()
call_1733 = func_1080_call()
func_471_call = mod.get_global_var('func_471')
func_472_call = mutated_mod.get_global_var('func_472')
call_1743 = func_471_call()
call_1744 = func_471_call()
output = relay.Tuple([call_1732,call_1743,])
output2 = relay.Tuple([call_1733,call_1744,])
func_1753 = relay.Function([], output)
mod['func_1753'] = func_1753
mod = relay.transform.InferType()(mod)
output = func_1753()
func_1754 = relay.Function([], output)
mutated_mod['func_1754'] = func_1754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_1760 = func_1544_call()
call_1761 = func_1544_call()
func_89_call = mod.get_global_var('func_89')
func_92_call = mutated_mod.get_global_var('func_92')
call_1764 = relay.TupleGetItem(func_89_call(relay.reshape(call_1760.astype('float64'), [5, 11, 8])), 1)
call_1765 = relay.TupleGetItem(func_92_call(relay.reshape(call_1760.astype('float64'), [5, 11, 8])), 1)
bop_1780 = relay.equal(call_1760.astype('bool'), relay.reshape(call_1764.astype('bool'), relay.shape_of(call_1760))) # shape=(5, 11, 8)
bop_1783 = relay.equal(call_1761.astype('bool'), relay.reshape(call_1765.astype('bool'), relay.shape_of(call_1761))) # shape=(5, 11, 8)
uop_1784 = relay.tan(bop_1780.astype('float32')) # shape=(5, 11, 8)
uop_1786 = relay.tan(bop_1783.astype('float32')) # shape=(5, 11, 8)
output = relay.Tuple([uop_1784,])
output2 = relay.Tuple([uop_1786,])
func_1822 = relay.Function([], output)
mod['func_1822'] = func_1822
mod = relay.transform.InferType()(mod)
mutated_mod['func_1822'] = func_1822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1822_call = mutated_mod.get_global_var('func_1822')
call_1823 = func_1822_call()
output = call_1823
func_1824 = relay.Function([], output)
mutated_mod['func_1824'] = func_1824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_1847 = relay.TupleGetItem(func_1753_call(), 0)
call_1848 = relay.TupleGetItem(func_1754_call(), 0)
output = relay.Tuple([call_1847,])
output2 = relay.Tuple([call_1848,])
func_1913 = relay.Function([], output)
mod['func_1913'] = func_1913
mod = relay.transform.InferType()(mod)
output = func_1913()
func_1914 = relay.Function([], output)
mutated_mod['func_1914'] = func_1914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_1915 = func_340_call()
call_1916 = func_340_call()
output = call_1915
output2 = call_1916
func_1937 = relay.Function([], output)
mod['func_1937'] = func_1937
mod = relay.transform.InferType()(mod)
mutated_mod['func_1937'] = func_1937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1937_call = mutated_mod.get_global_var('func_1937')
call_1938 = func_1937_call()
output = call_1938
func_1939 = relay.Function([], output)
mutated_mod['func_1939'] = func_1939
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1977 = relay.var("var_1977", dtype = "float64", shape = ())#candidate|1977|()|var|float64
var_1978 = relay.var("var_1978", dtype = "float64", shape = (15, 11, 14))#candidate|1978|(15, 11, 14)|var|float64
bop_1979 = relay.floor_mod(var_1977.astype('float64'), var_1978.astype('float64')) # shape=(15, 11, 14)
output = relay.Tuple([bop_1979,])
output2 = relay.Tuple([bop_1979,])
func_1985 = relay.Function([var_1977,var_1978,], output)
mod['func_1985'] = func_1985
mod = relay.transform.InferType()(mod)
var_1986 = relay.var("var_1986", dtype = "float64", shape = ())#candidate|1986|()|var|float64
var_1987 = relay.var("var_1987", dtype = "float64", shape = (15, 11, 14))#candidate|1987|(15, 11, 14)|var|float64
output = func_1985(var_1986,var_1987,)
func_1988 = relay.Function([var_1986,var_1987,], output)
mutated_mod['func_1988'] = func_1988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1451_call = mod.get_global_var('func_1451')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_2010 = relay.TupleGetItem(func_1451_call(), 0)
call_2011 = relay.TupleGetItem(func_1452_call(), 0)
func_610_call = mod.get_global_var('func_610')
func_611_call = mutated_mod.get_global_var('func_611')
call_2017 = func_610_call()
call_2018 = func_610_call()
func_1688_call = mod.get_global_var('func_1688')
func_1690_call = mutated_mod.get_global_var('func_1690')
call_2031 = relay.TupleGetItem(func_1688_call(), 1)
call_2032 = relay.TupleGetItem(func_1690_call(), 1)
output = relay.Tuple([call_2010,call_2017,call_2031,])
output2 = relay.Tuple([call_2011,call_2018,call_2032,])
func_2043 = relay.Function([], output)
mod['func_2043'] = func_2043
mod = relay.transform.InferType()(mod)
output = func_2043()
func_2044 = relay.Function([], output)
mutated_mod['func_2044'] = func_2044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1451_call = mod.get_global_var('func_1451')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_2054 = relay.TupleGetItem(func_1451_call(), 0)
call_2055 = relay.TupleGetItem(func_1452_call(), 0)
output = call_2054
output2 = call_2055
func_2061 = relay.Function([], output)
mod['func_2061'] = func_2061
mod = relay.transform.InferType()(mod)
mutated_mod['func_2061'] = func_2061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2062 = func_2061_call()
output = call_2062
func_2063 = relay.Function([], output)
mutated_mod['func_2063'] = func_2063
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2066 = relay.var("var_2066", dtype = "uint64", shape = (3, 7, 5))#candidate|2066|(3, 7, 5)|var|uint64
const_2067 = relay.const([[[8,-8,-9,-7,-6],[-7,-9,-9,3,9],[-1,6,-3,7,-6],[-8,3,9,-10,6],[-5,-9,8,-9,7],[-10,1,2,-2,-2],[2,-5,7,-4,10]],[[6,-2,2,-3,10],[10,-8,8,3,-1],[-10,-8,-7,-9,-3],[-2,4,4,-6,8],[-8,-6,9,10,-3],[8,3,10,-2,-2],[6,6,2,8,10]],[[1,-4,6,-10,5],[7,-9,-1,10,-8],[8,8,5,-3,-7],[-1,-1,-5,6,5],[-1,7,1,-10,1],[3,1,-3,-3,-3],[1,9,7,-1,9]]], dtype = "uint64")#candidate|2067|(3, 7, 5)|const|uint64
bop_2068 = relay.subtract(var_2066.astype('uint64'), relay.reshape(const_2067.astype('uint64'), relay.shape_of(var_2066))) # shape=(3, 7, 5)
output = bop_2068
output2 = bop_2068
func_2072 = relay.Function([var_2066,], output)
mod['func_2072'] = func_2072
mod = relay.transform.InferType()(mod)
mutated_mod['func_2072'] = func_2072
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2073 = relay.var("var_2073", dtype = "uint64", shape = (3, 7, 5))#candidate|2073|(3, 7, 5)|var|uint64
func_2072_call = mutated_mod.get_global_var('func_2072')
call_2074 = func_2072_call(var_2073)
output = call_2074
func_2075 = relay.Function([var_2073], output)
mutated_mod['func_2075'] = func_2075
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2081 = relay.var("var_2081", dtype = "float32", shape = (8, 1, 9))#candidate|2081|(8, 1, 9)|var|float32
uop_2082 = relay.cosh(var_2081.astype('float32')) # shape=(8, 1, 9)
output = uop_2082
output2 = uop_2082
func_2085 = relay.Function([var_2081,], output)
mod['func_2085'] = func_2085
mod = relay.transform.InferType()(mod)
mutated_mod['func_2085'] = func_2085
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2086 = relay.var("var_2086", dtype = "float32", shape = (8, 1, 9))#candidate|2086|(8, 1, 9)|var|float32
func_2085_call = mutated_mod.get_global_var('func_2085')
call_2087 = func_2085_call(var_2086)
output = call_2087
func_2088 = relay.Function([var_2086], output)
mutated_mod['func_2088'] = func_2088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_2090 = func_1080_call()
call_2091 = func_1080_call()
output = relay.Tuple([call_2090,])
output2 = relay.Tuple([call_2091,])
func_2128 = relay.Function([], output)
mod['func_2128'] = func_2128
mod = relay.transform.InferType()(mod)
mutated_mod['func_2128'] = func_2128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2128_call = mutated_mod.get_global_var('func_2128')
call_2129 = func_2128_call()
output = call_2129
func_2130 = relay.Function([], output)
mutated_mod['func_2130'] = func_2130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_2136 = relay.TupleGetItem(func_1822_call(), 0)
call_2137 = relay.TupleGetItem(func_1824_call(), 0)
func_1913_call = mod.get_global_var('func_1913')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_2172 = relay.TupleGetItem(func_1913_call(), 0)
call_2173 = relay.TupleGetItem(func_1914_call(), 0)
output = relay.Tuple([call_2136,call_2172,])
output2 = relay.Tuple([call_2137,call_2173,])
func_2187 = relay.Function([], output)
mod['func_2187'] = func_2187
mod = relay.transform.InferType()(mod)
mutated_mod['func_2187'] = func_2187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2187_call = mutated_mod.get_global_var('func_2187')
call_2188 = func_2187_call()
output = call_2188
func_2189 = relay.Function([], output)
mutated_mod['func_2189'] = func_2189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_2195 = relay.TupleGetItem(func_12_call(), 1)
call_2196 = relay.TupleGetItem(func_14_call(), 1)
var_2201 = relay.var("var_2201", dtype = "float64", shape = (5, 11, 8))#candidate|2201|(5, 11, 8)|var|float64
bop_2202 = relay.multiply(call_2195.astype('uint64'), relay.reshape(var_2201.astype('uint64'), relay.shape_of(call_2195))) # shape=(5, 11, 8)
bop_2205 = relay.multiply(call_2196.astype('uint64'), relay.reshape(var_2201.astype('uint64'), relay.shape_of(call_2196))) # shape=(5, 11, 8)
output = relay.Tuple([bop_2202,])
output2 = relay.Tuple([bop_2205,])
func_2217 = relay.Function([var_2201,], output)
mod['func_2217'] = func_2217
mod = relay.transform.InferType()(mod)
var_2218 = relay.var("var_2218", dtype = "float64", shape = (5, 11, 8))#candidate|2218|(5, 11, 8)|var|float64
output = func_2217(var_2218)
func_2219 = relay.Function([var_2218], output)
mutated_mod['func_2219'] = func_2219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_734_call = mod.get_global_var('func_734')
func_736_call = mutated_mod.get_global_var('func_736')
call_2232 = relay.TupleGetItem(func_734_call(), 4)
call_2233 = relay.TupleGetItem(func_736_call(), 4)
func_2061_call = mod.get_global_var('func_2061')
func_2063_call = mutated_mod.get_global_var('func_2063')
call_2240 = func_2061_call()
call_2241 = func_2061_call()
var_2256 = relay.var("var_2256", dtype = "float64", shape = (5, 11, 8))#candidate|2256|(5, 11, 8)|var|float64
bop_2257 = relay.logical_and(call_2232.astype('bool'), relay.reshape(var_2256.astype('bool'), relay.shape_of(call_2232))) # shape=(5, 11, 8)
bop_2260 = relay.logical_and(call_2233.astype('bool'), relay.reshape(var_2256.astype('bool'), relay.shape_of(call_2233))) # shape=(5, 11, 8)
func_2217_call = mod.get_global_var('func_2217')
func_2219_call = mutated_mod.get_global_var('func_2219')
call_2262 = relay.TupleGetItem(func_2217_call(relay.reshape(call_2232.astype('float64'), [5, 11, 8])), 0)
call_2263 = relay.TupleGetItem(func_2219_call(relay.reshape(call_2232.astype('float64'), [5, 11, 8])), 0)
func_1377_call = mod.get_global_var('func_1377')
func_1381_call = mutated_mod.get_global_var('func_1381')
const_2313 = relay.const([7.697873,-1.110202,-9.837639,0.028065,-0.126422,-6.045865,-6.840055,8.490807,-2.518436,0.034895,-1.302264,6.143165,0.269553,6.547885,-1.156301,4.589681,3.931661,5.928363,-9.545626,-4.968743,-1.573400,7.071552,5.952867,8.890578,-2.992996,8.945883,9.120473,-1.395350,-2.555461,3.490688], dtype = "float64")#candidate|2313|(30,)|const|float64
var_2314 = relay.var("var_2314", dtype = "float32", shape = (120,))#candidate|2314|(120,)|var|float32
call_2312 = relay.TupleGetItem(func_1377_call(relay.reshape(const_2313.astype('float64'), [5, 6]), relay.reshape(var_2314.astype('float32'), [6, 4, 5]), ), 0)
call_2315 = relay.TupleGetItem(func_1381_call(relay.reshape(const_2313.astype('float64'), [5, 6]), relay.reshape(var_2314.astype('float32'), [6, 4, 5]), ), 0)
output = relay.Tuple([call_2240,bop_2257,call_2262,call_2312,const_2313,var_2314,])
output2 = relay.Tuple([call_2241,bop_2260,call_2263,call_2315,const_2313,var_2314,])
func_2319 = relay.Function([var_2256,var_2314,], output)
mod['func_2319'] = func_2319
mod = relay.transform.InferType()(mod)
mutated_mod['func_2319'] = func_2319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2319_call = mutated_mod.get_global_var('func_2319')
var_2321 = relay.var("var_2321", dtype = "float64", shape = (5, 11, 8))#candidate|2321|(5, 11, 8)|var|float64
var_2322 = relay.var("var_2322", dtype = "float32", shape = (120,))#candidate|2322|(120,)|var|float32
call_2320 = func_2319_call(var_2321,var_2322,)
output = call_2320
func_2323 = relay.Function([var_2321,var_2322,], output)
mutated_mod['func_2323'] = func_2323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_2327 = func_1544_call()
call_2328 = func_1544_call()
func_419_call = mod.get_global_var('func_419')
func_422_call = mutated_mod.get_global_var('func_422')
const_2334 = relay.const([-10,4,-5,-3,3,2,-9,-5,-2,-8,8,-9,-3,5,7,3,-4,-7,10,-9,4,-4,-2,9,-4,9,8,-5,2,9,7,-5,3,-2,-3,-5,-2,1,8,8,-6,3], dtype = "uint32")#candidate|2334|(42,)|const|uint32
var_2335 = relay.var("var_2335", dtype = "uint32", shape = (294,))#candidate|2335|(294,)|var|uint32
call_2333 = func_419_call(relay.reshape(const_2334.astype('uint32'), [1, 7, 6]), relay.reshape(var_2335.astype('uint32'), [7, 7, 6]), )
call_2336 = func_419_call(relay.reshape(const_2334.astype('uint32'), [1, 7, 6]), relay.reshape(var_2335.astype('uint32'), [7, 7, 6]), )
bop_2353 = relay.floor_mod(var_2335.astype('float32'), relay.reshape(call_2333.astype('float32'), relay.shape_of(var_2335))) # shape=(294,)
bop_2356 = relay.floor_mod(var_2335.astype('float32'), relay.reshape(call_2336.astype('float32'), relay.shape_of(var_2335))) # shape=(294,)
var_2359 = relay.var("var_2359", dtype = "float32", shape = (294,))#candidate|2359|(294,)|var|float32
bop_2360 = relay.logical_xor(bop_2353.astype('uint32'), relay.reshape(var_2359.astype('uint32'), relay.shape_of(bop_2353))) # shape=(294,)
bop_2363 = relay.logical_xor(bop_2356.astype('uint32'), relay.reshape(var_2359.astype('uint32'), relay.shape_of(bop_2356))) # shape=(294,)
output = relay.Tuple([call_2327,const_2334,bop_2360,])
output2 = relay.Tuple([call_2328,const_2334,bop_2363,])
func_2369 = relay.Function([var_2335,var_2359,], output)
mod['func_2369'] = func_2369
mod = relay.transform.InferType()(mod)
mutated_mod['func_2369'] = func_2369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2369_call = mutated_mod.get_global_var('func_2369')
var_2371 = relay.var("var_2371", dtype = "uint32", shape = (294,))#candidate|2371|(294,)|var|uint32
var_2372 = relay.var("var_2372", dtype = "float32", shape = (294,))#candidate|2372|(294,)|var|float32
call_2370 = func_2369_call(var_2371,var_2372,)
output = call_2370
func_2373 = relay.Function([var_2371,var_2372,], output)
mutated_mod['func_2373'] = func_2373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1688_call = mod.get_global_var('func_1688')
func_1690_call = mutated_mod.get_global_var('func_1690')
call_2382 = relay.TupleGetItem(func_1688_call(), 1)
call_2383 = relay.TupleGetItem(func_1690_call(), 1)
output = call_2382
output2 = call_2383
func_2396 = relay.Function([], output)
mod['func_2396'] = func_2396
mod = relay.transform.InferType()(mod)
mutated_mod['func_2396'] = func_2396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2396_call = mutated_mod.get_global_var('func_2396')
call_2397 = func_2396_call()
output = call_2397
func_2398 = relay.Function([], output)
mutated_mod['func_2398'] = func_2398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_2399 = relay.TupleGetItem(func_1205_call(), 0)
call_2400 = relay.TupleGetItem(func_1206_call(), 0)
func_1483_call = mod.get_global_var('func_1483')
func_1484_call = mutated_mod.get_global_var('func_1484')
call_2405 = func_1483_call()
call_2406 = func_1483_call()
func_2085_call = mod.get_global_var('func_2085')
func_2088_call = mutated_mod.get_global_var('func_2088')
var_2408 = relay.var("var_2408", dtype = "float32", shape = (72,))#candidate|2408|(72,)|var|float32
call_2407 = func_2085_call(relay.reshape(var_2408.astype('float32'), [8, 1, 9]))
call_2409 = func_2085_call(relay.reshape(var_2408.astype('float32'), [8, 1, 9]))
uop_2411 = relay.log10(call_2405.astype('float32')) # shape=(15, 16, 10)
uop_2413 = relay.log10(call_2406.astype('float32')) # shape=(15, 16, 10)
func_1713_call = mod.get_global_var('func_1713')
func_1714_call = mutated_mod.get_global_var('func_1714')
call_2416 = relay.TupleGetItem(func_1713_call(), 0)
call_2417 = relay.TupleGetItem(func_1714_call(), 0)
output = relay.Tuple([call_2399,call_2407,var_2408,uop_2411,call_2416,])
output2 = relay.Tuple([call_2400,call_2409,var_2408,uop_2413,call_2417,])
func_2422 = relay.Function([var_2408,], output)
mod['func_2422'] = func_2422
mod = relay.transform.InferType()(mod)
mutated_mod['func_2422'] = func_2422
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2423 = relay.var("var_2423", dtype = "float32", shape = (72,))#candidate|2423|(72,)|var|float32
func_2422_call = mutated_mod.get_global_var('func_2422')
call_2424 = func_2422_call(var_2423)
output = call_2424
func_2425 = relay.Function([var_2423], output)
mutated_mod['func_2425'] = func_2425
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2467 = relay.var("var_2467", dtype = "float32", shape = (2, 2, 3))#candidate|2467|(2, 2, 3)|var|float32
uop_2468 = relay.exp(var_2467.astype('float32')) # shape=(2, 2, 3)
func_853_call = mod.get_global_var('func_853')
func_854_call = mutated_mod.get_global_var('func_854')
call_2474 = func_853_call()
call_2475 = func_853_call()
output = relay.Tuple([uop_2468,call_2474,])
output2 = relay.Tuple([uop_2468,call_2475,])
func_2478 = relay.Function([var_2467,], output)
mod['func_2478'] = func_2478
mod = relay.transform.InferType()(mod)
var_2479 = relay.var("var_2479", dtype = "float32", shape = (2, 2, 3))#candidate|2479|(2, 2, 3)|var|float32
output = func_2478(var_2479)
func_2480 = relay.Function([var_2479], output)
mutated_mod['func_2480'] = func_2480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_2482 = func_815_call()
call_2483 = func_815_call()
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_2491 = func_1544_call()
call_2492 = func_1544_call()
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_2494 = func_1080_call()
call_2495 = func_1080_call()
output = relay.Tuple([call_2482,call_2491,call_2494,])
output2 = relay.Tuple([call_2483,call_2492,call_2495,])
func_2499 = relay.Function([], output)
mod['func_2499'] = func_2499
mod = relay.transform.InferType()(mod)
output = func_2499()
func_2500 = relay.Function([], output)
mutated_mod['func_2500'] = func_2500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2061_call = mod.get_global_var('func_2061')
func_2063_call = mutated_mod.get_global_var('func_2063')
call_2509 = func_2061_call()
call_2510 = func_2061_call()
output = call_2509
output2 = call_2510
func_2525 = relay.Function([], output)
mod['func_2525'] = func_2525
mod = relay.transform.InferType()(mod)
mutated_mod['func_2525'] = func_2525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2525_call = mutated_mod.get_global_var('func_2525')
call_2526 = func_2525_call()
output = call_2526
func_2527 = relay.Function([], output)
mutated_mod['func_2527'] = func_2527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2535 = relay.var("var_2535", dtype = "float64", shape = (3, 16, 7))#candidate|2535|(3, 16, 7)|var|float64
uop_2536 = relay.log(var_2535.astype('float64')) # shape=(3, 16, 7)
output = relay.Tuple([uop_2536,])
output2 = relay.Tuple([uop_2536,])
func_2538 = relay.Function([var_2535,], output)
mod['func_2538'] = func_2538
mod = relay.transform.InferType()(mod)
mutated_mod['func_2538'] = func_2538
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2539 = relay.var("var_2539", dtype = "float64", shape = (3, 16, 7))#candidate|2539|(3, 16, 7)|var|float64
func_2538_call = mutated_mod.get_global_var('func_2538')
call_2540 = func_2538_call(var_2539)
output = call_2540
func_2541 = relay.Function([var_2539], output)
mutated_mod['func_2541'] = func_2541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_2594 = func_340_call()
call_2595 = func_340_call()
output = relay.Tuple([call_2594,])
output2 = relay.Tuple([call_2595,])
func_2638 = relay.Function([], output)
mod['func_2638'] = func_2638
mod = relay.transform.InferType()(mod)
mutated_mod['func_2638'] = func_2638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2638_call = mutated_mod.get_global_var('func_2638')
call_2639 = func_2638_call()
output = call_2639
func_2640 = relay.Function([], output)
mutated_mod['func_2640'] = func_2640
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2641 = relay.var("var_2641", dtype = "uint8", shape = (11, 7, 5))#candidate|2641|(11, 7, 5)|var|uint8
const_2642 = relay.const([[[9,10,-9,1,2],[1,8,-1,9,-1],[2,10,2,-5,1],[-9,-9,-10,-2,6],[9,-9,1,5,-9],[-2,6,9,3,2],[-4,-4,2,5,5]],[[9,-1,2,10,9],[-4,2,-4,-9,-3],[-10,-4,1,-8,-1],[8,-10,-10,-10,-10],[2,1,-3,5,1],[-2,6,-7,3,5],[-10,-6,1,-3,-10]],[[1,4,-6,-6,-8],[10,10,-10,-4,2],[-9,-2,5,2,-4],[8,4,7,8,2],[2,9,-9,9,-2],[-3,-7,5,-8,-7],[-1,10,-6,5,10]],[[-3,-1,-6,-9,-6],[-8,-3,3,5,7],[6,9,-3,-2,-1],[8,-7,-6,9,-10],[8,3,-4,-9,10],[3,4,-3,-6,-5],[-9,1,-2,-1,-2]],[[-6,-10,2,-7,-3],[9,-6,-7,-9,-4],[-10,-7,-1,7,2],[4,10,8,7,4],[-4,-7,3,-9,-9],[-7,8,-9,5,-2],[5,-4,1,8,-7]],[[10,-3,-4,-5,9],[6,4,-1,2,10],[10,1,2,-6,-9],[-1,6,6,-2,-3],[-4,8,2,10,7],[1,5,3,-3,6],[-2,1,-2,-8,-9]],[[-5,9,-10,7,8],[-1,-1,-10,-4,3],[-4,-10,5,-1,8],[5,2,9,6,3],[-9,-4,3,-7,8],[10,7,5,3,6],[-6,5,4,2,-9]],[[7,-1,10,-6,4],[7,3,3,-5,-6],[6,-3,-1,-4,-8],[-8,-2,-7,-7,-7],[6,-3,7,9,-2],[6,-8,-6,5,-2],[4,-9,2,-7,8]],[[10,-10,-5,8,-3],[-10,8,-6,-10,6],[-4,-3,7,9,-6],[9,-3,8,-8,-3],[-9,-9,-2,3,6],[4,-2,-2,-6,-4],[-10,-8,-4,10,-3]],[[2,-7,-10,6,2],[5,-1,-7,-7,-6],[3,5,-10,8,-10],[4,-4,3,-1,-7],[10,-9,2,-5,-8],[1,-8,5,-5,9],[-3,-9,3,10,10]],[[7,3,4,3,-4],[2,-4,-4,-8,9],[6,2,10,-7,1],[10,-9,7,8,-3],[-3,-10,5,4,-2],[-5,-7,-2,-4,7],[-6,5,-2,1,4]]], dtype = "uint8")#candidate|2642|(11, 7, 5)|const|uint8
bop_2643 = relay.right_shift(var_2641.astype('uint8'), relay.reshape(const_2642.astype('uint8'), relay.shape_of(var_2641))) # shape=(11, 7, 5)
uop_2653 = relay.asinh(var_2641.astype('float64')) # shape=(11, 7, 5)
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_2661 = func_340_call()
call_2662 = func_340_call()
output = relay.Tuple([bop_2643,uop_2653,call_2661,])
output2 = relay.Tuple([bop_2643,uop_2653,call_2662,])
func_2670 = relay.Function([var_2641,], output)
mod['func_2670'] = func_2670
mod = relay.transform.InferType()(mod)
mutated_mod['func_2670'] = func_2670
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2671 = relay.var("var_2671", dtype = "uint8", shape = (11, 7, 5))#candidate|2671|(11, 7, 5)|var|uint8
func_2670_call = mutated_mod.get_global_var('func_2670')
call_2672 = func_2670_call(var_2671)
output = call_2672
func_2673 = relay.Function([var_2671], output)
mutated_mod['func_2673'] = func_2673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_2705 = relay.TupleGetItem(func_206_call(), 0)
call_2706 = relay.TupleGetItem(func_207_call(), 0)
output = relay.Tuple([call_2705,])
output2 = relay.Tuple([call_2706,])
func_2710 = relay.Function([], output)
mod['func_2710'] = func_2710
mod = relay.transform.InferType()(mod)
mutated_mod['func_2710'] = func_2710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2710_call = mutated_mod.get_global_var('func_2710')
call_2711 = func_2710_call()
output = call_2711
func_2712 = relay.Function([], output)
mutated_mod['func_2712'] = func_2712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2747 = relay.TupleGetItem(func_2043_call(), 0)
call_2748 = relay.TupleGetItem(func_2044_call(), 0)
var_2751 = relay.var("var_2751", dtype = "float64", shape = (13, 8, 8))#candidate|2751|(13, 8, 8)|var|float64
bop_2752 = relay.bitwise_and(call_2747.astype('int16'), relay.reshape(var_2751.astype('int16'), relay.shape_of(call_2747))) # shape=(13, 8, 8)
bop_2755 = relay.bitwise_and(call_2748.astype('int16'), relay.reshape(var_2751.astype('int16'), relay.shape_of(call_2748))) # shape=(13, 8, 8)
func_655_call = mod.get_global_var('func_655')
func_657_call = mutated_mod.get_global_var('func_657')
call_2765 = func_655_call()
call_2766 = func_655_call()
output = relay.Tuple([bop_2752,call_2765,])
output2 = relay.Tuple([bop_2755,call_2766,])
func_2783 = relay.Function([var_2751,], output)
mod['func_2783'] = func_2783
mod = relay.transform.InferType()(mod)
mutated_mod['func_2783'] = func_2783
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2784 = relay.var("var_2784", dtype = "float64", shape = (13, 8, 8))#candidate|2784|(13, 8, 8)|var|float64
func_2783_call = mutated_mod.get_global_var('func_2783')
call_2785 = func_2783_call(var_2784)
output = call_2785
func_2786 = relay.Function([var_2784], output)
mutated_mod['func_2786'] = func_2786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1512_call = mod.get_global_var('func_1512')
func_1513_call = mutated_mod.get_global_var('func_1513')
call_2815 = func_1512_call()
call_2816 = func_1512_call()
output = call_2815
output2 = call_2816
func_2823 = relay.Function([], output)
mod['func_2823'] = func_2823
mod = relay.transform.InferType()(mod)
mutated_mod['func_2823'] = func_2823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2823_call = mutated_mod.get_global_var('func_2823')
call_2824 = func_2823_call()
output = call_2824
func_2825 = relay.Function([], output)
mutated_mod['func_2825'] = func_2825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2710_call = mod.get_global_var('func_2710')
func_2712_call = mutated_mod.get_global_var('func_2712')
call_2858 = relay.TupleGetItem(func_2710_call(), 0)
call_2859 = relay.TupleGetItem(func_2712_call(), 0)
func_419_call = mod.get_global_var('func_419')
func_422_call = mutated_mod.get_global_var('func_422')
var_2866 = relay.var("var_2866", dtype = "uint32", shape = (1, 42))#candidate|2866|(1, 42)|var|uint32
const_2867 = relay.const([6,-2,6,8,-10,-8,6,-7,10,-2,1,5,-3,-9,2,-7,-6,7,-5,-9,-3,-3,4,5,-4,-4,-1,5,4,6,9,-6,-6,-6,-10,-7,4,2,-10,4,4,-10,-7,-8,10,10,-9,6,-1,-6,9,-4,3,-3,-2,8,-4,-2,5,5,6,-9,-2,-8,-7,-6,8,-1,5,-6,10,-5,-4,5,-9,-7,6,7,10,2,10,6,-9,8,1,-3,8,5,-8,-1,3,-1,-3,6,6,1,-10,-1,-3,3,3,-5,5,-10,2,-10,-9,-3,-1,-4,-9,-2,-1,7,4,-8,-7,7,-4,-7,-8,1,-9,-10,3,9,8,-2,6,10,1,-8,-2,-10,-2,3,5,-7,-10,7,10,9,7,6,-3,5,6,-2,-6,5,1,-8,-5,3,2,1,5,-10,1,10,-4,-8,8,-1,4,4,5,2,-9,-5,6,-10,6,-5,-8,1,-2,4,-8,-6,-2,-8,6,-7,6,3,10,2,7,-4,-4,9,-5,6,8,6,6,-7,5,-5,-9,-2,6,-6,-3,8,-7,-3,-9,-6,5,-9,9,3,-3,6,1,-3,-3,-7,-1,-6,-1,-3,-10,-9,2,-5,-5,4,1,10,-9,6,-1,-8,2,-3,3,-5,-4,7,4,6,4,-7,-1,4,9,-3,7,-3,7,1,-1,-4,-1,-10,5,-4,9,4,8,1,2,-8,-7,-5,8,-4,-2,-3,-9,8,10,-5,-5,10,-8,3,-4,8,-3,-6,1,-9,8,8,4,3,9,-2,8,-10], dtype = "uint32")#candidate|2867|(294,)|const|uint32
call_2865 = func_419_call(relay.reshape(var_2866.astype('uint32'), [1, 7, 6]), relay.reshape(const_2867.astype('uint32'), [7, 7, 6]), )
call_2868 = func_419_call(relay.reshape(var_2866.astype('uint32'), [1, 7, 6]), relay.reshape(const_2867.astype('uint32'), [7, 7, 6]), )
func_1913_call = mod.get_global_var('func_1913')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_2870 = relay.TupleGetItem(func_1913_call(), 0)
call_2871 = relay.TupleGetItem(func_1914_call(), 0)
func_2217_call = mod.get_global_var('func_2217')
func_2219_call = mutated_mod.get_global_var('func_2219')
call_2873 = relay.TupleGetItem(func_2217_call(relay.reshape(call_2858.astype('float64'), [5, 11, 8])), 0)
call_2874 = relay.TupleGetItem(func_2219_call(relay.reshape(call_2858.astype('float64'), [5, 11, 8])), 0)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_2876 = relay.TupleGetItem(func_1416_call(), 1)
call_2877 = relay.TupleGetItem(func_1417_call(), 1)
output = relay.Tuple([call_2858,call_2865,var_2866,const_2867,call_2870,call_2873,call_2876,])
output2 = relay.Tuple([call_2859,call_2868,var_2866,const_2867,call_2871,call_2874,call_2877,])
func_2882 = relay.Function([var_2866,], output)
mod['func_2882'] = func_2882
mod = relay.transform.InferType()(mod)
mutated_mod['func_2882'] = func_2882
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2883 = relay.var("var_2883", dtype = "uint32", shape = (1, 42))#candidate|2883|(1, 42)|var|uint32
func_2882_call = mutated_mod.get_global_var('func_2882')
call_2884 = func_2882_call(var_2883)
output = call_2884
func_2885 = relay.Function([var_2883], output)
mutated_mod['func_2885'] = func_2885
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2915 = relay.var("var_2915", dtype = "uint32", shape = (4, 12, 3))#candidate|2915|(4, 12, 3)|var|uint32
const_2916 = relay.const([[[3,6,1],[-2,-6,-4],[-1,-10,-7],[1,9,-3],[-4,5,-9],[2,6,-9],[4,10,4],[-5,-10,-1],[-7,4,-10],[4,8,-6],[6,10,7],[-8,3,-1]],[[4,4,-8],[-3,-7,2],[4,1,-7],[-2,6,2],[-3,2,-10],[5,-8,10],[-5,-2,7],[-10,-8,-4],[8,8,8],[-5,2,-9],[2,-6,4],[-6,-8,1]],[[-2,8,-2],[7,-8,3],[-4,-1,8],[7,-3,-2],[-1,-3,-7],[-4,-5,-9],[3,-6,10],[1,10,10],[-9,1,2],[-8,-2,-9],[7,-7,4],[-1,1,-1]],[[9,-5,-1],[8,-2,3],[-2,6,-6],[-2,10,7],[-5,-2,6],[-9,5,-3],[-9,-10,9],[6,6,5],[8,-7,7],[2,-2,2],[10,-4,-7],[5,9,-8]]], dtype = "uint32")#candidate|2916|(4, 12, 3)|const|uint32
bop_2917 = relay.greater_equal(var_2915.astype('bool'), relay.reshape(const_2916.astype('bool'), relay.shape_of(var_2915))) # shape=(4, 12, 3)
bop_2922 = relay.floor_mod(var_2915.astype('float64'), relay.reshape(const_2916.astype('float64'), relay.shape_of(var_2915))) # shape=(4, 12, 3)
func_2525_call = mod.get_global_var('func_2525')
func_2527_call = mutated_mod.get_global_var('func_2527')
call_2925 = func_2525_call()
call_2926 = func_2525_call()
func_1117_call = mod.get_global_var('func_1117')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_2930 = relay.TupleGetItem(func_1117_call(), 0)
call_2931 = relay.TupleGetItem(func_1118_call(), 0)
output = relay.Tuple([bop_2917,bop_2922,call_2925,call_2930,])
output2 = relay.Tuple([bop_2917,bop_2922,call_2926,call_2931,])
func_2936 = relay.Function([var_2915,], output)
mod['func_2936'] = func_2936
mod = relay.transform.InferType()(mod)
mutated_mod['func_2936'] = func_2936
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2937 = relay.var("var_2937", dtype = "uint32", shape = (4, 12, 3))#candidate|2937|(4, 12, 3)|var|uint32
func_2936_call = mutated_mod.get_global_var('func_2936')
call_2938 = func_2936_call(var_2937)
output = call_2938
func_2939 = relay.Function([var_2937], output)
mutated_mod['func_2939'] = func_2939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1451_call = mod.get_global_var('func_1451')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_2982 = relay.TupleGetItem(func_1451_call(), 0)
call_2983 = relay.TupleGetItem(func_1452_call(), 0)
func_1713_call = mod.get_global_var('func_1713')
func_1714_call = mutated_mod.get_global_var('func_1714')
call_2988 = relay.TupleGetItem(func_1713_call(), 0)
call_2989 = relay.TupleGetItem(func_1714_call(), 0)
func_1913_call = mod.get_global_var('func_1913')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_3020 = relay.TupleGetItem(func_1913_call(), 0)
call_3021 = relay.TupleGetItem(func_1914_call(), 0)
func_1633_call = mod.get_global_var('func_1633')
func_1635_call = mutated_mod.get_global_var('func_1635')
call_3044 = relay.TupleGetItem(func_1633_call(relay.reshape(call_3020.astype('float64'), [5, 11, 8])), 6)
call_3045 = relay.TupleGetItem(func_1635_call(relay.reshape(call_3020.astype('float64'), [5, 11, 8])), 6)
output = relay.Tuple([call_2982,call_2988,call_3020,call_3044,])
output2 = relay.Tuple([call_2983,call_2989,call_3021,call_3045,])
func_3047 = relay.Function([], output)
mod['func_3047'] = func_3047
mod = relay.transform.InferType()(mod)
output = func_3047()
func_3048 = relay.Function([], output)
mutated_mod['func_3048'] = func_3048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3068 = relay.var("var_3068", dtype = "int64", shape = ())#candidate|3068|()|var|int64
var_3069 = relay.var("var_3069", dtype = "int64", shape = (3, 14, 16))#candidate|3069|(3, 14, 16)|var|int64
bop_3070 = relay.logical_xor(var_3068.astype('int64'), var_3069.astype('int64')) # shape=(3, 14, 16)
func_251_call = mod.get_global_var('func_251')
func_253_call = mutated_mod.get_global_var('func_253')
const_3074 = relay.const([5.530434,1.780967,-1.806484,-1.435316,-5.307731,4.306310,-9.019997,5.242013,-8.031541,-9.051566,-1.702708,7.210596,1.461617,8.008765,9.724391,-6.649876,-1.970602,3.694756,1.995675,9.882511,8.033566,2.240599,-5.336331,-1.182508,1.368790,-0.910919,9.640676,-5.789535,4.953141,6.255442,-8.428974,8.942619,8.594057,0.086132,-0.597083,-3.363301,-6.776534,-5.263170,3.558356,4.434951,5.019124,-6.898312,4.439456,2.907032,-5.883021,-0.599701,5.865766,-4.069820,-8.336611,0.685751,-1.355041,-4.824475,6.206938,5.971168,-8.262107,-0.190307,7.877177,-2.550295,2.993813,5.984477,-9.795015,7.113704,-8.066412,-5.489736,3.618424,1.368217,-9.582370,-3.617361,-8.811307,-6.148135,-1.920029,-2.412343,6.311450,8.369153,2.011147,-0.105770,-3.203878,0.756051,2.202591,2.366034,1.384635,-1.558961,4.801867,3.076051,9.236226,-1.018920,-9.156964,2.924940,0.880599,2.921194,1.646723,-5.580125,0.060217,-3.831340,4.785448,1.932696,8.767945,-6.335415,1.268909,-6.910595,5.703802,-3.665372,-2.283124,6.752463,-2.216756,-5.752779,8.973457,0.346638,-3.366091,6.870113,-6.543105,-9.990579,8.601558,-3.458849,-7.306442,2.477271,9.600321,-5.817851,2.184314,3.696673,-4.440771,2.021248,-8.239378,-6.455656,0.024625,-2.132400,-4.326653,7.521803,-9.113830,-9.196733,-9.677535,-1.900073,-1.987705,1.387620,1.528171,9.487012,-3.297083,4.505825,-1.786945,6.072525,5.156567,3.389630,-4.037261,7.921590,-5.733786,-0.499932,6.722774,-8.562722,2.163721,6.403023,-6.700876,-1.898497,-5.015860,5.758014,7.594822,-9.336144,-8.544183,-1.772911,-8.578508,4.009513,-7.946166,6.044701,5.092384,0.659781,-4.332371,3.322086,7.752570,6.397348,8.329771,-0.962097,-3.847446,4.082917,-2.479306,0.506132,-6.933279,7.387186,-7.829422,-4.583983,-9.668352,-3.738658,3.836802,1.556042,3.072201,-5.357530,2.817502,1.906090,3.338577,3.927881,7.218817,-4.542871,3.760061,-2.344861,-9.603143,9.980859,-2.994282,7.515780,1.697595,-2.793731,-4.747069,1.638063,-7.970717,4.890026,-1.053647,9.763118,0.066659,3.592192,-9.880929,1.395634,-5.500351,5.999229,-5.924244,-6.386591,-0.159318,0.020929,8.093215,-2.882298,3.894919,4.989346,-8.684210,7.756156,-7.680457,7.629852,-4.252898,-2.930072,9.498561,5.253247,-9.673365,-5.018173,6.905641,8.040782,-2.628281,-5.859873,9.665941,0.892271,-8.475064,-7.997016,0.905067,5.322047,-5.512659,0.064457,-9.905147,5.728542,-0.015789,3.122811,0.172703,4.575592,-1.541260,-2.974471,4.561024,-7.630812,-0.451161,1.910498,-7.924156,-4.854362,-8.753578,-6.439497,-9.743590,1.812249,3.863371,-2.545992,-2.974470,2.087156,4.901067,-3.684586,4.392685,3.082579,4.830854,-0.183078,7.454143,-6.477082,-2.091883,-8.095343,6.875503,6.710422,-7.594333,0.471227,8.324302,-5.560290,-5.640783,-3.362463,4.067014,-5.297802,-7.953143,-8.910905,1.659916,0.736285,3.058620,-5.909441,7.784559,-8.081834,-2.227306,-1.901735,-4.969278,-4.770726,-7.367327,-5.183517,-1.630586,-8.240375,5.142072,5.588422,-0.255809,-9.543008,-6.357348,-5.114839,3.374324,-0.972219,-8.296100,2.366275,7.048470,-4.759899,-2.534758,1.525272,4.595114,8.357804,-2.622425,8.050358,6.330154,-0.578001,-7.676205,-5.720366,5.543427,3.164551,5.620448,-6.969319,0.167584,-1.702913,-0.324405,-0.054268,-2.154170,-9.800986,-8.389589,3.176353,-2.957821,-0.318474,-0.124738,-6.037761,2.700523,5.414321,-6.479103,2.902819,-5.629868,-5.678286,3.254398,-7.746133,-3.384190,-6.090221,-1.872268,8.101803,1.460085,-9.948632,-9.980648,-0.774125,-9.780968,-5.767963,3.311287,-1.135755,-2.947024,-1.654829,-1.123139,4.654766,-0.478519,3.799904,1.642251,2.538380,-0.124148,-5.182791,-0.169147,-6.206636,-5.308778,0.581400,-1.447321,-2.305451,-5.485133,-0.953208,5.179829,-7.292101,4.407983,7.780189,-0.785063,-0.870563,-1.095652,5.525947,6.700563,9.604232,-9.447626,0.859220,6.600264,7.990237,8.911826,-6.191790,1.636081,-2.277358,-2.255565,2.552513,-8.575386,-3.926458,-7.477501,6.606952,4.745792,-3.175228,6.322314,6.188274,6.983960,6.590840,-7.789606,7.232094,-4.403238,3.155807,6.975189,8.488090,-3.683484,-4.736316,3.406143,-8.563532,0.196675,-9.620997,-0.175677,0.778638,0.125130,-5.767756,-3.747848,5.992264,4.501669,4.929000,-5.308457,-5.594657,-3.104208,0.621427,-2.659095,7.126436,-1.488524,3.806295,6.104639,-7.168063,0.945473,-4.387804,3.550404,-1.034792,-8.680964,2.319454], dtype = "float64")#candidate|3074|(440,)|const|float64
call_3073 = relay.TupleGetItem(func_251_call(relay.reshape(const_3074.astype('float64'), [5, 11, 8])), 1)
call_3075 = relay.TupleGetItem(func_253_call(relay.reshape(const_3074.astype('float64'), [5, 11, 8])), 1)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_3076 = func_1544_call()
call_3077 = func_1544_call()
output = relay.Tuple([bop_3070,call_3073,const_3074,call_3076,])
output2 = relay.Tuple([bop_3070,call_3075,const_3074,call_3077,])
func_3084 = relay.Function([var_3068,var_3069,], output)
mod['func_3084'] = func_3084
mod = relay.transform.InferType()(mod)
mutated_mod['func_3084'] = func_3084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3084_call = mutated_mod.get_global_var('func_3084')
var_3086 = relay.var("var_3086", dtype = "int64", shape = ())#candidate|3086|()|var|int64
var_3087 = relay.var("var_3087", dtype = "int64", shape = (3, 14, 16))#candidate|3087|(3, 14, 16)|var|int64
call_3085 = func_3084_call(var_3086,var_3087,)
output = call_3085
func_3088 = relay.Function([var_3086,var_3087,], output)
mutated_mod['func_3088'] = func_3088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2638_call = mod.get_global_var('func_2638')
func_2640_call = mutated_mod.get_global_var('func_2640')
call_3107 = relay.TupleGetItem(func_2638_call(), 0)
call_3108 = relay.TupleGetItem(func_2640_call(), 0)
func_1633_call = mod.get_global_var('func_1633')
func_1635_call = mutated_mod.get_global_var('func_1635')
call_3111 = relay.TupleGetItem(func_1633_call(relay.reshape(call_3107.astype('float64'), [5, 11, 8])), 7)
call_3112 = relay.TupleGetItem(func_1635_call(relay.reshape(call_3107.astype('float64'), [5, 11, 8])), 7)
func_1377_call = mod.get_global_var('func_1377')
func_1381_call = mutated_mod.get_global_var('func_1381')
var_3114 = relay.var("var_3114", dtype = "float64", shape = (30,))#candidate|3114|(30,)|var|float64
const_3115 = relay.const([0.853909,5.998508,0.367386,-6.692933,4.024918,-3.906668,-5.390084,-9.603549,8.467915,-3.575936,5.499333,9.177455,-0.365072,-7.723772,2.567846,-9.808251,5.037684,0.403549,-0.646698,-2.857700,-8.861990,-6.765556,7.176096,-1.863305,9.767512,7.859303,8.832679,6.522782,-4.685880,7.093914,4.464308,4.674890,-2.488626,8.976058,-1.486323,-0.624058,-8.257862,0.191847,0.319307,7.026120,-1.169223,7.462635,2.235923,-5.900516,-9.285053,5.241315,8.545288,4.811977,9.651407,-8.265295,-8.246120,5.966491,-3.844804,-3.813551,-7.937733,-2.535359,-5.697277,-8.248710,-3.709869,-4.092896,3.348771,-6.615498,-9.291713,-6.274850,1.204962,1.421475,4.131130,-1.383971,1.792071,4.613766,-9.251497,4.833040,5.451977,2.415010,-0.694050,0.329243,5.682118,-4.891722,8.738040,-5.609446,-4.708952,-4.480629,-5.684506,9.016576,9.597188,2.616837,-1.453197,1.442749,-6.859622,-8.852269,-1.307080,-7.585387,3.957843,6.013045,9.019406,3.061609,3.950603,1.833777,3.187674,1.038737,6.124519,-4.342067,1.352795,-0.765230,-9.564231,-0.272259,-7.207192,1.801744,-9.747246,-0.143680,-0.162732,6.679502,4.367296,4.843073,5.075830,5.731331,4.403048,-9.109851,6.473674,-9.735760], dtype = "float32")#candidate|3115|(120,)|const|float32
call_3113 = relay.TupleGetItem(func_1377_call(relay.reshape(var_3114.astype('float64'), [5, 6]), relay.reshape(const_3115.astype('float32'), [6, 4, 5]), ), 0)
call_3116 = relay.TupleGetItem(func_1381_call(relay.reshape(var_3114.astype('float64'), [5, 6]), relay.reshape(const_3115.astype('float32'), [6, 4, 5]), ), 0)
output = relay.Tuple([call_3107,call_3111,call_3113,var_3114,const_3115,])
output2 = relay.Tuple([call_3108,call_3112,call_3116,var_3114,const_3115,])
func_3117 = relay.Function([var_3114,], output)
mod['func_3117'] = func_3117
mod = relay.transform.InferType()(mod)
var_3118 = relay.var("var_3118", dtype = "float64", shape = (30,))#candidate|3118|(30,)|var|float64
output = func_3117(var_3118)
func_3119 = relay.Function([var_3118], output)
mutated_mod['func_3119'] = func_3119
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3146 = relay.var("var_3146", dtype = "float64", shape = (2, 16, 14))#candidate|3146|(2, 16, 14)|var|float64
var_3147 = relay.var("var_3147", dtype = "float64", shape = (2, 16, 14))#candidate|3147|(2, 16, 14)|var|float64
bop_3148 = relay.floor_mod(var_3146.astype('float64'), relay.reshape(var_3147.astype('float64'), relay.shape_of(var_3146))) # shape=(2, 16, 14)
output = bop_3148
output2 = bop_3148
func_3152 = relay.Function([var_3146,var_3147,], output)
mod['func_3152'] = func_3152
mod = relay.transform.InferType()(mod)
var_3153 = relay.var("var_3153", dtype = "float64", shape = (2, 16, 14))#candidate|3153|(2, 16, 14)|var|float64
var_3154 = relay.var("var_3154", dtype = "float64", shape = (2, 16, 14))#candidate|3154|(2, 16, 14)|var|float64
output = func_3152(var_3153,var_3154,)
func_3155 = relay.Function([var_3153,var_3154,], output)
mutated_mod['func_3155'] = func_3155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_3261 = relay.TupleGetItem(func_1205_call(), 0)
call_3262 = relay.TupleGetItem(func_1206_call(), 0)
func_12_call = mod.get_global_var('func_12')
func_14_call = mutated_mod.get_global_var('func_14')
call_3266 = relay.TupleGetItem(func_12_call(), 1)
call_3267 = relay.TupleGetItem(func_14_call(), 1)
func_251_call = mod.get_global_var('func_251')
func_253_call = mutated_mod.get_global_var('func_253')
call_3274 = relay.TupleGetItem(func_251_call(relay.reshape(call_3261.astype('float64'), [5, 11, 8])), 1)
call_3275 = relay.TupleGetItem(func_253_call(relay.reshape(call_3261.astype('float64'), [5, 11, 8])), 1)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_3282 = relay.TupleGetItem(func_1822_call(), 0)
call_3283 = relay.TupleGetItem(func_1824_call(), 0)
func_1377_call = mod.get_global_var('func_1377')
func_1381_call = mutated_mod.get_global_var('func_1381')
const_3285 = relay.const([[-3.032910],[-3.591050],[-4.495507],[-0.261548],[-1.205979],[-4.454098],[-7.491136],[-3.192353],[-7.037246],[-4.717450],[6.114083],[7.772195],[-0.734255],[3.010348],[4.720121],[-8.692177],[-2.437355],[-8.829626],[8.946992],[-1.659657],[7.497648],[-5.134610],[-3.682119],[-3.583818],[5.809051],[4.581502],[9.142047],[2.316378],[0.499278],[-8.751339]], dtype = "float64")#candidate|3285|(30, 1)|const|float64
var_3286 = relay.var("var_3286", dtype = "float32", shape = (120,))#candidate|3286|(120,)|var|float32
call_3284 = relay.TupleGetItem(func_1377_call(relay.reshape(const_3285.astype('float64'), [5, 6]), relay.reshape(var_3286.astype('float32'), [6, 4, 5]), ), 2)
call_3287 = relay.TupleGetItem(func_1381_call(relay.reshape(const_3285.astype('float64'), [5, 6]), relay.reshape(var_3286.astype('float32'), [6, 4, 5]), ), 2)
output = relay.Tuple([call_3261,call_3266,call_3274,call_3282,call_3284,const_3285,var_3286,])
output2 = relay.Tuple([call_3262,call_3267,call_3275,call_3283,call_3287,const_3285,var_3286,])
func_3308 = relay.Function([var_3286,], output)
mod['func_3308'] = func_3308
mod = relay.transform.InferType()(mod)
mutated_mod['func_3308'] = func_3308
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3309 = relay.var("var_3309", dtype = "float32", shape = (120,))#candidate|3309|(120,)|var|float32
func_3308_call = mutated_mod.get_global_var('func_3308')
call_3310 = func_3308_call(var_3309)
output = call_3310
func_3311 = relay.Function([var_3309], output)
mutated_mod['func_3311'] = func_3311
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3347 = relay.var("var_3347", dtype = "float32", shape = (13, 10, 6))#candidate|3347|(13, 10, 6)|var|float32
uop_3348 = relay.asin(var_3347.astype('float32')) # shape=(13, 10, 6)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_3350 = func_1080_call()
call_3351 = func_1080_call()
output = relay.Tuple([uop_3348,call_3350,])
output2 = relay.Tuple([uop_3348,call_3351,])
func_3363 = relay.Function([var_3347,], output)
mod['func_3363'] = func_3363
mod = relay.transform.InferType()(mod)
var_3364 = relay.var("var_3364", dtype = "float32", shape = (13, 10, 6))#candidate|3364|(13, 10, 6)|var|float32
output = func_3363(var_3364)
func_3365 = relay.Function([var_3364], output)
mutated_mod['func_3365'] = func_3365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mod.get_global_var('func_1913')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_3574 = relay.TupleGetItem(func_1913_call(), 0)
call_3575 = relay.TupleGetItem(func_1914_call(), 0)
output = call_3574
output2 = call_3575
func_3587 = relay.Function([], output)
mod['func_3587'] = func_3587
mod = relay.transform.InferType()(mod)
output = func_3587()
func_3588 = relay.Function([], output)
mutated_mod['func_3588'] = func_3588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2061_call = mod.get_global_var('func_2061')
func_2063_call = mutated_mod.get_global_var('func_2063')
call_3613 = func_2061_call()
call_3614 = func_2061_call()
func_2061_call = mod.get_global_var('func_2061')
func_2063_call = mutated_mod.get_global_var('func_2063')
call_3620 = func_2061_call()
call_3621 = func_2061_call()
var_3623 = relay.var("var_3623", dtype = "float64", shape = (13, 8, 8))#candidate|3623|(13, 8, 8)|var|float64
bop_3624 = relay.less(call_3613.astype('bool'), relay.reshape(var_3623.astype('bool'), relay.shape_of(call_3613))) # shape=(13, 8, 8)
bop_3627 = relay.less(call_3614.astype('bool'), relay.reshape(var_3623.astype('bool'), relay.shape_of(call_3614))) # shape=(13, 8, 8)
func_2538_call = mod.get_global_var('func_2538')
func_2541_call = mutated_mod.get_global_var('func_2541')
const_3629 = relay.const([-6.888840,-0.885215,7.617478,-7.390733,-0.254321,0.591471,5.667714,-4.910787,1.562587,1.984910,-6.438619,-9.468169,6.634561,7.880186,-9.034616,-5.590202,6.314995,-3.344970,5.897318,-4.898894,-2.337304,9.125214,-1.596342,7.657732,3.618672,0.530667,8.867463,-6.927219,1.856042,1.166560,-8.615554,-9.472788,-7.201089,8.906921,3.910470,-9.605322,4.127470,-2.259577,1.011313,-1.833727,-2.519887,-8.157180,7.714423,-5.098131,-3.607185,-0.200954,-9.330766,9.046213,-2.228858,-1.803056,-6.440640,2.573557,-3.120069,7.534953,5.866136,8.364980,-0.360713,-9.049910,-0.168558,-8.198750,-4.390382,9.656161,6.663662,-9.468088,9.181955,-4.148847,7.024474,-3.588745,0.427138,3.986513,0.719431,-4.635641,-0.593682,2.901075,-2.221799,-9.542611,4.490126,5.689926,-0.326030,-8.872366,-9.951842,1.861218,-2.548607,-3.744957,8.222895,3.680852,-8.552375,-5.973807,-3.812706,1.234146,1.535743,8.702141,3.235186,-6.375157,-6.296587,-6.303716,3.962183,-9.961934,9.562360,5.278048,-5.664773,6.758382,-0.967716,-8.066292,8.654599,1.101642,1.827862,9.668650,1.498704,-1.892125,-3.455120,0.049993,-3.995086,-8.881732,-1.949750,-8.484115,-5.516027,6.409483,-7.055799,3.268246,1.042775,-9.604936,2.647832,7.097635,2.294615,3.409870,-1.384181,5.244634,-4.607162,-7.789476,7.232577,-3.352743,-3.302796,7.809118,9.551781,8.984072,4.947645,9.934071,1.160109,-6.777583,-2.554238,1.908773,-9.364203,0.443554,-1.440590,7.843118,-0.578072,6.407399,6.245297,3.229973,6.269814,1.841162,9.267930,8.229488,8.260527,5.778067,7.489080,2.445031,-5.779643,7.393144,-1.439832,-0.471232,-4.703655,-0.947805,-0.449188,-1.933030,-6.661741,1.701282,-6.463740,-5.517266,-6.922745,1.234705,-4.529359,1.927479,2.887761,1.604790,0.821509,-6.951174,8.283133,3.549652,3.373546,7.911068,8.590542,6.758430,-7.559520,2.734638,9.214412,-5.391082,9.568117,-8.365659,-6.088637,2.334212,-3.629638,8.289122,-9.400709,3.146419,-2.521580,6.833898,8.391023,2.977152,-4.448681,-9.855865,0.478502,-4.760401,-1.590113,1.806569,-5.627263,-1.330910,6.209642,1.995045,-4.082520,7.271054,8.447507,-7.527124,9.616377,-3.819598,6.181363,6.579776,-0.405117,7.502631,9.041797,4.590348,5.670954,-8.877999,-6.139231,-0.485784,-6.858866,6.026625,-7.770084,6.824928,-9.114994,-9.806206,-3.019520,-9.920207,4.077772,-1.697313,0.027872,-8.379695,2.357452,3.829045,-4.660250,3.096107,3.305305,2.372524,-7.867889,4.835636,-7.147425,-4.975622,1.721688,3.518121,8.339639,7.147926,-7.509477,4.310588,-1.025841,4.867437,5.644198,-7.832361,0.390729,-1.202839,-9.614394,-2.620972,7.254244,7.454161,-9.558877,1.232411,-1.120686,-4.799346,0.731335,4.767911,-3.759598,-1.019675,9.335402,-5.903830,-8.547922,-2.173838,-9.153898,-0.574588,-1.265882,-0.118415,-8.245742,-6.665504,9.625099,6.000012,-8.651109,-1.028094,8.272804,-9.945868,2.770273,-6.422767,-0.563864,-7.959597,6.784508,-5.304849,0.438658,-9.569177,8.653965,-7.441926,5.781499,0.501895,-6.979468,-1.753854,-3.092353,-6.566775,4.947178,-1.951894,-8.285410,-5.060599,9.144938,9.336379,-1.741173,-4.041757,-4.351915,-7.055504,9.686803,7.866964,6.601763,2.207048,1.015399,-1.498826,-3.422808,-5.329160,8.773769,7.460652,8.374238,6.015503,-3.955407,1.475106,9.569437,9.866103,2.056325,-8.558069,-1.361870,7.484979,-6.252034,8.682067], dtype = "float64")#candidate|3629|(336,)|const|float64
call_3628 = relay.TupleGetItem(func_2538_call(relay.reshape(const_3629.astype('float64'), [3, 16, 7])), 0)
call_3630 = relay.TupleGetItem(func_2541_call(relay.reshape(const_3629.astype('float64'), [3, 16, 7])), 0)
uop_3635 = relay.sinh(call_3613.astype('float32')) # shape=(13, 8, 8)
uop_3637 = relay.sinh(call_3614.astype('float32')) # shape=(13, 8, 8)
uop_3650 = relay.sin(call_3613.astype('float32')) # shape=(13, 8, 8)
uop_3652 = relay.sin(call_3614.astype('float32')) # shape=(13, 8, 8)
output = relay.Tuple([call_3620,bop_3624,call_3628,const_3629,uop_3635,uop_3650,])
output2 = relay.Tuple([call_3621,bop_3627,call_3630,const_3629,uop_3637,uop_3652,])
func_3667 = relay.Function([var_3623,], output)
mod['func_3667'] = func_3667
mod = relay.transform.InferType()(mod)
mutated_mod['func_3667'] = func_3667
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3668 = relay.var("var_3668", dtype = "float64", shape = (13, 8, 8))#candidate|3668|(13, 8, 8)|var|float64
func_3667_call = mutated_mod.get_global_var('func_3667')
call_3669 = func_3667_call(var_3668)
output = call_3669
func_3670 = relay.Function([var_3668], output)
mutated_mod['func_3670'] = func_3670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_3713 = relay.TupleGetItem(func_1205_call(), 1)
call_3714 = relay.TupleGetItem(func_1206_call(), 1)
output = relay.Tuple([call_3713,])
output2 = relay.Tuple([call_3714,])
func_3724 = relay.Function([], output)
mod['func_3724'] = func_3724
mod = relay.transform.InferType()(mod)
mutated_mod['func_3724'] = func_3724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3724_call = mutated_mod.get_global_var('func_3724')
call_3725 = func_3724_call()
output = call_3725
func_3726 = relay.Function([], output)
mutated_mod['func_3726'] = func_3726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_3798 = relay.TupleGetItem(func_2499_call(), 2)
call_3799 = relay.TupleGetItem(func_2500_call(), 2)
output = relay.Tuple([call_3798,])
output2 = relay.Tuple([call_3799,])
func_3835 = relay.Function([], output)
mod['func_3835'] = func_3835
mod = relay.transform.InferType()(mod)
output = func_3835()
func_3836 = relay.Function([], output)
mutated_mod['func_3836'] = func_3836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_655_call = mod.get_global_var('func_655')
func_657_call = mutated_mod.get_global_var('func_657')
call_3857 = func_655_call()
call_3858 = func_655_call()
uop_3875 = relay.atanh(call_3857.astype('float32')) # shape=(5, 11, 8)
uop_3877 = relay.atanh(call_3858.astype('float32')) # shape=(5, 11, 8)
output = uop_3875
output2 = uop_3877
func_3879 = relay.Function([], output)
mod['func_3879'] = func_3879
mod = relay.transform.InferType()(mod)
output = func_3879()
func_3880 = relay.Function([], output)
mutated_mod['func_3880'] = func_3880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_3908 = relay.TupleGetItem(func_1416_call(), 0)
call_3909 = relay.TupleGetItem(func_1417_call(), 0)
output = relay.Tuple([call_3908,])
output2 = relay.Tuple([call_3909,])
func_3933 = relay.Function([], output)
mod['func_3933'] = func_3933
mod = relay.transform.InferType()(mod)
mutated_mod['func_3933'] = func_3933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3933_call = mutated_mod.get_global_var('func_3933')
call_3934 = func_3933_call()
output = call_3934
func_3935 = relay.Function([], output)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_3964 = relay.TupleGetItem(func_319_call(), 1)
call_3965 = relay.TupleGetItem(func_321_call(), 1)
func_2369_call = mod.get_global_var('func_2369')
func_2373_call = mutated_mod.get_global_var('func_2373')
const_3975 = relay.const([10,3,7,-5,-4,6,10,10,1,10,3,9,-1,1,-4,8,-10,7,2,-2,-4,6,2,2,1,-9,6,-6,10,2,8,7,2,-5,7,3,-6,7,-7,5,9,-2,-1,3,-6,5,-6,3,-10,4,-8,1,8,-3,-5,4,-2,10,-7,-7,9,-8,-6,-6,-9,-4,-9,-2,2,-3,2,2,6,-7,8,-5,-6,3,1,-8,2,-9,6,-8,-7,-7,10,2,3,8,-3,-10,3,-1,-5,-9,1,-7,-1,7,-8,6,-4,-2,8,-10,-1,10,-4,-2,-9,5,9,9,7,-8,10,10,4,5,-2,-5,-3,-10,-9,7,3,10,-4,-2,6,-5,-7,2,-9,-5,2,-5,-8,-4,-9,-5,-3,-4,3,-7,9,-5,8,-8,-6,9,5,-5,-1,8,-1,2,-7,2,-2,10,2,-6,5,-7,-6,-1,10,-4,6,-1,-4,-3,-9,2,4,3,-7,8,4,5,2,3,-1,-5,6,3,10,2,1,-3,5,-2,-6,4,-6,1,6,-1,8,5,-5,5,-6,-5,10,1,3,-8,4,8,-3,-7,3,-6,-4,-5,1,4,-9,-4,8,-4,1,-9,-2,-2,-6,-3,-6,9,2,-1,-6,-2,-4,3,6,-3,7,-1,-9,-5,-3,-5,9,-9,10,6,4,2,-6,10,-2,8,-4,-10,1,9,6,-3,8,8,1,-3,-3,5,-9,3,9,-3,-10,8,-10,7,9,-3,-3,4,-6,-1,1,2,2,-3,9,-3,-1,-2,8,-1,9,-5], dtype = "uint32")#candidate|3975|(294,)|const|uint32
call_3974 = relay.TupleGetItem(func_2369_call(relay.reshape(const_3975.astype('uint32'), [294,]), relay.reshape(const_3975.astype('float32'), [294,]), ), 2)
call_3976 = relay.TupleGetItem(func_2373_call(relay.reshape(const_3975.astype('uint32'), [294,]), relay.reshape(const_3975.astype('float32'), [294,]), ), 2)
output = relay.Tuple([call_3964,call_3974,const_3975,])
output2 = relay.Tuple([call_3965,call_3976,const_3975,])
func_3981 = relay.Function([], output)
mod['func_3981'] = func_3981
mod = relay.transform.InferType()(mod)
mutated_mod['func_3981'] = func_3981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3981_call = mutated_mod.get_global_var('func_3981')
call_3982 = func_3981_call()
output = call_3982
func_3983 = relay.Function([], output)
mutated_mod['func_3983'] = func_3983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3587_call = mod.get_global_var('func_3587')
func_3588_call = mutated_mod.get_global_var('func_3588')
call_4009 = func_3587_call()
call_4010 = func_3587_call()
func_1937_call = mod.get_global_var('func_1937')
func_1939_call = mutated_mod.get_global_var('func_1939')
call_4022 = func_1937_call()
call_4023 = func_1937_call()
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_4024 = relay.TupleGetItem(func_1753_call(), 0)
call_4025 = relay.TupleGetItem(func_1754_call(), 0)
func_3047_call = mod.get_global_var('func_3047')
func_3048_call = mutated_mod.get_global_var('func_3048')
call_4026 = relay.TupleGetItem(func_3047_call(), 2)
call_4027 = relay.TupleGetItem(func_3048_call(), 2)
output = relay.Tuple([call_4009,call_4022,call_4024,call_4026,])
output2 = relay.Tuple([call_4010,call_4023,call_4025,call_4027,])
func_4041 = relay.Function([], output)
mod['func_4041'] = func_4041
mod = relay.transform.InferType()(mod)
mutated_mod['func_4041'] = func_4041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4041_call = mutated_mod.get_global_var('func_4041')
call_4042 = func_4041_call()
output = call_4042
func_4043 = relay.Function([], output)
mutated_mod['func_4043'] = func_4043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_4081 = relay.TupleGetItem(func_1753_call(), 0)
call_4082 = relay.TupleGetItem(func_1754_call(), 0)
output = relay.Tuple([call_4081,])
output2 = relay.Tuple([call_4082,])
func_4086 = relay.Function([], output)
mod['func_4086'] = func_4086
mod = relay.transform.InferType()(mod)
output = func_4086()
func_4087 = relay.Function([], output)
mutated_mod['func_4087'] = func_4087
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4098 = relay.const([[-7.427473,4.490069,5.295550,-4.525590,7.833328,3.267474,-7.294733,-0.957737,-3.703220,4.635733,3.899587,1.065136,-2.947069,8.324808,7.305296],[6.080983,3.635065,-4.353783,-0.716225,-1.947507,-3.386754,-7.135751,0.197801,6.136246,-7.347880,-1.908773,9.063712,-3.784304,6.733193,0.536165],[-8.528595,-1.954399,9.290924,9.166226,5.531681,8.782914,7.029258,-2.119816,-9.112371,-5.124896,3.505324,4.169470,0.083312,-1.665233,5.769270],[9.894055,-2.674838,6.212923,-4.319804,-8.881142,-0.182319,-2.744044,4.658945,5.685591,-7.645013,-5.196834,-6.101079,6.267216,4.950832,-5.253522],[6.849041,0.790515,-6.696782,-6.490308,5.041997,-1.305007,-5.457652,5.879900,-6.452459,-8.202433,-1.841940,-0.122184,-0.147268,-7.391395,6.320564],[-3.443166,0.100953,7.540631,-5.821243,-1.394072,-8.119313,2.951322,9.449071,-5.205626,7.946412,0.680985,-2.505964,8.122702,5.130057,-5.550556],[-1.758025,3.130997,-8.907347,4.360308,-8.588096,-9.103750,3.122164,-5.844626,-6.335077,-7.438286,1.849333,-4.119389,3.824182,-1.200470,9.758047],[9.048730,1.170681,8.677764,1.679233,-5.874644,3.227639,-8.716173,-4.387394,2.781613,-5.348006,8.171249,6.990400,8.908178,5.206658,3.662281],[-1.963000,-2.150584,-2.018718,-8.451863,0.147746,0.138567,9.442446,4.224589,-0.590611,0.079762,-6.780230,-7.027955,-8.980964,-5.659112,9.908072],[-7.311208,-3.296225,9.922543,2.193001,2.072561,-7.813335,1.823373,-0.968265,-9.808216,6.724764,2.609437,-3.509387,-1.670203,9.985297,-1.757882],[-3.117485,5.554901,3.371639,9.629706,-0.797168,0.383331,-4.158139,-5.831750,0.015245,2.552858,-7.995859,-5.433920,7.714868,3.406186,4.171054]], dtype = "float64")#candidate|4098|(11, 15)|const|float64
uop_4099 = relay.sigmoid(const_4098.astype('float64')) # shape=(11, 15)
func_1377_call = mod.get_global_var('func_1377')
func_1381_call = mutated_mod.get_global_var('func_1381')
var_4110 = relay.var("var_4110", dtype = "float64", shape = (30,))#candidate|4110|(30,)|var|float64
var_4111 = relay.var("var_4111", dtype = "float32", shape = (120,))#candidate|4111|(120,)|var|float32
call_4109 = relay.TupleGetItem(func_1377_call(relay.reshape(var_4110.astype('float64'), [5, 6]), relay.reshape(var_4111.astype('float32'), [6, 4, 5]), ), 6)
call_4112 = relay.TupleGetItem(func_1381_call(relay.reshape(var_4110.astype('float64'), [5, 6]), relay.reshape(var_4111.astype('float32'), [6, 4, 5]), ), 6)
output = relay.Tuple([uop_4099,call_4109,var_4110,var_4111,])
output2 = relay.Tuple([uop_4099,call_4112,var_4110,var_4111,])
func_4121 = relay.Function([var_4110,var_4111,], output)
mod['func_4121'] = func_4121
mod = relay.transform.InferType()(mod)
mutated_mod['func_4121'] = func_4121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4121_call = mutated_mod.get_global_var('func_4121')
var_4123 = relay.var("var_4123", dtype = "float64", shape = (30,))#candidate|4123|(30,)|var|float64
var_4124 = relay.var("var_4124", dtype = "float32", shape = (120,))#candidate|4124|(120,)|var|float32
call_4122 = func_4121_call(var_4123,var_4124,)
output = call_4122
func_4125 = relay.Function([var_4123,var_4124,], output)
mutated_mod['func_4125'] = func_4125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3047_call = mod.get_global_var('func_3047')
func_3048_call = mutated_mod.get_global_var('func_3048')
call_4195 = relay.TupleGetItem(func_3047_call(), 0)
call_4196 = relay.TupleGetItem(func_3048_call(), 0)
func_2187_call = mod.get_global_var('func_2187')
func_2189_call = mutated_mod.get_global_var('func_2189')
call_4212 = relay.TupleGetItem(func_2187_call(), 1)
call_4213 = relay.TupleGetItem(func_2189_call(), 1)
output = relay.Tuple([call_4195,call_4212,])
output2 = relay.Tuple([call_4196,call_4213,])
func_4231 = relay.Function([], output)
mod['func_4231'] = func_4231
mod = relay.transform.InferType()(mod)
output = func_4231()
func_4232 = relay.Function([], output)
mutated_mod['func_4232'] = func_4232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_4245 = relay.TupleGetItem(func_319_call(), 0)
call_4246 = relay.TupleGetItem(func_321_call(), 0)
func_3152_call = mod.get_global_var('func_3152')
func_3155_call = mutated_mod.get_global_var('func_3155')
const_4256 = relay.const([-9.243904,-6.848559,-3.013845,-5.417421,1.467238,1.960822,-0.110599,0.180048,-8.618077,-5.248039,2.901803,-3.840033,-6.689825,3.834704,9.161927,-0.213096,-9.527076,-9.665702,0.452589,-1.068542,-0.283889,-5.143608,-7.264761,9.839702,3.687612,-5.465083,-2.765977,-7.584714,-9.980810,1.332659,-0.913455,-6.982868,-2.585384,3.577529,2.292515,9.505024,9.290839,-6.190988,4.221950,-3.015941,9.727129,4.178046,-7.165637,0.052476,-7.573064,-0.178095,-5.219047,9.288671,4.057061,-3.383398,-4.038546,-5.940988,9.916408,2.161400,-2.566561,-8.269345,-9.336226,-1.880959,3.219368,-4.921781,-3.063245,-0.186129,8.924293,3.358746,-1.057730,5.854875,9.448144,0.749090,6.998027,3.271122,-6.971414,9.202627,-1.538757,0.244386,4.067925,2.861925,-8.533476,-3.764774,7.616187,6.747511,-1.573432,7.955134,-1.758654,-8.961330,5.645406,-0.933895,3.618028,2.504572,6.096647,5.194657,-9.722597,-2.489801,-9.682307,-0.315678,-0.406774,-4.604513,-9.717057,7.699864,-0.557841,-0.707450,9.027082,5.533914,9.055793,-3.324174,-4.712142,1.484292,-4.933337,4.345741,4.602930,0.424668,5.813656,-2.307996,1.042456,1.907103,8.251629,9.803410,-9.352502,-1.584361,7.331594,-5.284096,-8.485296,-6.561650,1.644678,-6.290320,5.982251,-1.046252,5.315695,4.629491,-4.779695,-7.467650,-7.569530,1.607556,-1.056642,-0.483371,-4.958182,1.639797,6.358839,-8.909295,-9.411237,0.636020,-4.582083,-2.067469,-1.924466,-1.583521,-7.037831,-2.681611,-2.936763,6.809980,5.238117,7.345236,-8.255268,9.111460,-7.754503,-5.331755,-4.192383,8.575673,-9.530297,-7.170827,1.012389,6.435830,6.417431,-3.147983,4.437693,-5.121044,-8.243889,2.980964,0.531457,-0.137870,-8.309820,-3.210508,-5.933138,6.786578,5.851209,4.463191,-1.582393,1.599459,-4.310159,5.851591,8.965181,9.233636,7.830056,1.261533,4.602760,4.597817,-4.682445,-5.749682,6.549970,6.982459,4.700534,4.424638,-7.752563,0.022119,-6.257450,-1.376570,-8.086101,2.420153,-0.538658,-7.384088,-1.893398,6.184928,9.561695,7.486787,9.847327,-3.380741,7.820169,-7.939684,-1.833695,1.891021,8.109875,-6.392263,3.769890,3.441557,-2.471813,4.932654,8.851569,-1.032007,-4.643394,3.818577,-9.012281,-9.321656,8.418720,2.194382,-4.421798,4.411928,9.685087,8.689461,9.026484,-4.774655,7.772322,4.142698,0.273371,3.589260,7.875587,2.821275,-8.753069,-0.571649,4.953450,3.980524,-2.528111,5.218146,1.133188,-9.811646,4.828888,-0.088721,-7.737035,-9.228918,2.429630,0.795818,-8.098191,5.797014,-4.004001,4.670510,1.775572,1.416400,4.457217,8.640135,1.672179,9.295788,5.536788,5.022607,8.070277,7.745052,-6.091797,-2.601740,7.984672,5.583987,7.594237,9.582127,-4.075737,-3.646101,7.290056,-6.033642,1.954724,-1.808698,0.536942,-8.423915,5.448068,-8.651220,-6.286695,-3.904778,-5.951199,7.969101,-4.585484,-0.923975,7.415819,-7.876522,3.794963,2.711028,0.209495,7.457710,-6.498935,8.253069,8.077774,3.083968,-6.317288,1.774321,0.502724,-2.694555,-4.746393,-2.415287,8.033867,-1.983366,3.456052,8.698145,9.719240,-1.747540,-6.742003,3.648841,8.238323,6.323081,2.495747,-5.297620,4.193548,-6.728836,5.739097,3.122740,-1.983560,4.074774,-9.108999,-4.214934,4.044875,6.232507,-1.746755,8.699213,3.946793,-9.721582,-8.031391,7.034015,1.591271,6.059033,7.813438,-4.778803,-1.719105,7.811724,-4.429207,9.907288,-3.619242,-8.040193,6.269056,-2.513375,-0.229923,4.235594,1.576579,6.632752,6.599626,-3.410699,4.271852,-4.794444,-7.770133,-8.402186,9.490767,6.123325,-5.124573,-1.581257,0.611014,-8.174378,4.899185,-4.732656,2.039524,-9.652504,-6.504540,9.073350,8.010624,-2.942941,7.719589,-6.939606,-7.946108,0.003497,5.589316,-4.931128,-2.109238,4.803637,9.648681,7.855141,4.476984,1.054869,-2.366544,5.810018,-0.764748,5.194845,5.902657,-0.473403,8.508956,-9.937595,3.067118,-5.541244,-9.505551,-2.501975,0.515401,-2.175477,4.208131,0.063013,-7.936165,8.000624,-6.265664,-1.847677,-3.747474,0.284786,-8.837714,1.556109,-6.476364,-4.225524,9.815810,-6.542515,-4.340477,0.703743,-3.259325,0.453165,2.581344,9.630990,4.963630,5.855169,-9.652518,-0.461080,3.437318,3.083534,1.847616,-2.845236,-9.150413,7.160260,4.727688,-4.175270,2.693087,-9.564066,-6.915811,-6.657542,0.352387,4.716809,-5.421235,4.616550,4.085144,-7.309081,-3.047413,5.882594,7.339038,5.926601,1.504325,4.066117,9.276029,-1.884904,3.977660,2.933880,-8.340430,7.559111,-2.080098,-2.796121,2.156079,-0.086593], dtype = "float64")#candidate|4256|(448,)|const|float64
call_4255 = func_3152_call(relay.reshape(const_4256.astype('float64'), [2, 16, 14]), relay.reshape(const_4256.astype('float64'), [2, 16, 14]), )
call_4257 = func_3152_call(relay.reshape(const_4256.astype('float64'), [2, 16, 14]), relay.reshape(const_4256.astype('float64'), [2, 16, 14]), )
output = relay.Tuple([call_4245,call_4255,const_4256,])
output2 = relay.Tuple([call_4246,call_4257,const_4256,])
func_4261 = relay.Function([], output)
mod['func_4261'] = func_4261
mod = relay.transform.InferType()(mod)
output = func_4261()
func_4262 = relay.Function([], output)
mutated_mod['func_4262'] = func_4262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3835_call = mod.get_global_var('func_3835')
func_3836_call = mutated_mod.get_global_var('func_3836')
call_4286 = relay.TupleGetItem(func_3835_call(), 0)
call_4287 = relay.TupleGetItem(func_3836_call(), 0)
func_1713_call = mod.get_global_var('func_1713')
func_1714_call = mutated_mod.get_global_var('func_1714')
call_4297 = relay.TupleGetItem(func_1713_call(), 0)
call_4298 = relay.TupleGetItem(func_1714_call(), 0)
output = relay.Tuple([call_4286,call_4297,])
output2 = relay.Tuple([call_4287,call_4298,])
func_4317 = relay.Function([], output)
mod['func_4317'] = func_4317
mod = relay.transform.InferType()(mod)
output = func_4317()
func_4318 = relay.Function([], output)
mutated_mod['func_4318'] = func_4318
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4322 = relay.var("var_4322", dtype = "float64", shape = (13, 6, 12))#candidate|4322|(13, 6, 12)|var|float64
const_4323 = relay.const([[[-9.506904,7.561514,-5.147519,-5.601054,-5.884652,2.862624,-9.167076,3.151444,-3.281508,3.658986,0.668291,-4.956255],[-2.730218,-3.810800,0.076908,-2.386726,8.820208,-8.760452,-3.868683,5.458746,-6.988221,9.100770,0.225238,7.743063],[-1.610139,-3.179049,4.108071,8.632491,3.098970,-8.575098,-0.394857,-6.548377,-0.665293,5.630213,-7.193691,-8.381450],[1.364652,9.913161,-5.642880,-4.719077,-0.302840,-6.257241,1.044495,2.039539,-5.213973,-7.538730,-6.421111,-7.553663],[3.089141,3.226624,-8.092083,-8.519021,-2.346978,-2.512016,-9.837844,9.233575,4.248591,6.446360,8.114411,4.162677],[-9.384339,-5.280162,0.964813,-0.395388,8.540316,-6.761527,4.211185,5.139937,-1.135104,-6.029046,5.739579,6.239365]],[[3.749286,8.405177,-9.217550,-3.187148,-7.827783,0.407359,7.389275,2.586671,-9.800888,9.843461,-3.993120,2.033419],[-9.127346,-4.309770,9.083505,3.438008,-0.438725,7.393520,7.503040,1.462679,0.444513,4.087604,-9.249718,3.487142],[-5.975766,-8.709191,5.611786,-3.140203,4.871212,8.132834,-2.641831,-2.300678,-1.696074,1.238910,0.122857,8.736446],[-4.846928,-3.925902,6.843911,8.678504,-4.337922,2.765812,1.703080,9.880878,-5.002368,8.051562,9.253300,6.940746],[0.570527,-9.446939,3.177720,1.841729,-7.658524,8.854119,7.488094,-6.980684,-3.845048,-2.159211,7.622904,7.576536],[-5.817083,-9.627152,-4.939392,3.696669,6.715418,-0.419746,-4.428193,-7.059455,5.231133,-0.188015,-6.917432,-3.064979]],[[-4.584390,-9.821079,4.595498,6.046024,-9.435736,3.345334,7.456264,-3.406931,-3.617248,-8.065645,7.867310,-9.362882],[-9.299472,1.022294,2.412879,5.514234,-1.290807,6.297588,8.875271,-2.411123,-1.606755,-1.846798,-5.750629,-2.067379],[-7.389491,5.577240,4.939155,-1.859038,7.683064,-1.383984,-4.638859,-3.589676,7.163543,-0.503388,3.684966,-8.907847],[-3.527269,1.686270,-7.999414,-8.155062,-7.081872,-5.277416,1.749132,2.555213,-4.119772,3.420816,-3.469477,-2.102222],[1.430907,-1.980588,1.224499,-2.677741,-3.026500,-8.503226,-3.454970,3.513346,1.490798,-7.156344,-9.107884,9.322518],[-2.762291,7.110054,-8.454509,-9.832137,-3.892742,-4.453741,-4.008493,-4.044216,2.615968,7.012015,4.817677,-7.869610]],[[-7.693770,5.400036,3.005173,9.598123,4.805014,-5.703440,-4.795864,3.925888,5.270404,-1.019344,-6.661106,-2.966514],[-3.741932,2.413873,-5.776191,-8.705608,4.562692,-4.199225,-6.362393,-3.421951,-6.289910,8.181936,0.748044,-6.779829],[0.831826,-1.152186,7.577632,6.172001,-9.702536,3.615088,-0.589532,7.253004,5.393007,-3.145292,-6.692059,0.325302],[3.831176,7.032948,3.081008,-1.942514,8.416759,-4.088584,6.013823,-8.674543,1.514510,4.753605,9.771491,1.775379],[-4.375782,-2.303968,-8.897143,7.120361,-0.036775,-8.248891,-6.261251,-0.042086,-1.183757,-7.779188,-3.881599,9.286118],[-2.073435,-2.093784,-1.784491,-8.498029,7.182800,4.704252,-1.850738,-9.704438,6.564990,-7.522931,8.683724,4.671410]],[[-3.396710,8.198904,-7.889564,-6.171191,7.937842,-1.835333,-0.096029,-9.529373,4.544356,6.190016,1.981762,1.818345],[-3.127230,-8.913757,-0.871140,7.626835,-3.191220,-3.819112,-3.759847,2.900598,8.240572,1.590521,9.706861,8.467619],[6.280822,-9.199438,-1.450812,4.525328,-3.790692,-8.470850,-9.343003,7.571241,1.283885,1.335736,-7.237286,9.770293],[5.447731,3.264331,0.737180,2.194519,1.822458,4.379092,0.602744,-3.527637,-1.070625,7.742694,3.927604,6.044942],[-2.545356,-2.812315,-2.780574,-1.247717,-0.425569,-6.330477,-4.661545,-6.472325,9.492727,-1.020625,-0.531829,-2.321057],[5.894232,6.716462,-8.781027,3.795818,-2.790712,0.653940,-7.978586,-5.592090,3.367299,-6.449280,-9.181987,5.372422]],[[-2.105873,0.208276,1.298008,6.506128,3.549930,5.165091,-0.671146,-8.157322,-5.968455,7.283868,6.898561,1.813231],[-0.526518,-3.543184,-6.699555,-7.539779,4.238435,4.518544,-4.165285,-6.902214,-1.197025,4.064716,-3.426215,3.600801],[-5.732444,7.276599,-8.604916,-3.122764,-8.112825,1.966313,5.861103,4.639721,7.334626,6.925324,-6.187362,9.163384],[0.439565,2.654259,-2.774410,-4.571792,5.971438,-9.509519,-9.604764,-3.880345,-5.964874,6.998772,4.107440,-9.942945],[5.971683,-4.736169,0.080453,-8.920456,8.261802,6.600524,-5.180768,-9.887136,0.249423,7.481410,6.553971,2.467220],[-1.202337,8.475852,3.789553,-0.922561,0.329019,-1.382727,9.184387,1.211812,-0.658334,-9.933845,-0.411448,-6.698991]],[[-9.683988,4.611581,9.027418,5.102896,3.227887,-3.838799,-1.439757,-2.724322,6.206750,5.677343,1.141870,3.732918],[9.133161,1.761736,-7.199363,1.384842,7.348786,0.254566,3.759458,-9.585462,5.322354,-9.240070,-6.760393,-2.103100],[6.250469,-1.493371,-1.554658,0.269037,4.639826,-8.480507,-1.820590,-4.983914,-1.388464,9.234984,-3.995595,6.936236],[-8.489092,-9.582443,-1.812395,-1.774075,-7.048310,-3.427934,2.924411,-2.218786,-4.055225,-7.613748,-7.937809,8.850112],[-5.532113,8.871135,-1.942267,7.461634,-3.116425,2.001620,-1.892938,-3.966265,-6.973406,2.366597,-7.656361,4.959856],[-0.226712,-9.919237,-7.829214,-5.712004,-9.334078,-7.322858,-1.015476,1.045764,8.176051,4.990852,-1.108525,-1.009088]],[[-3.242377,-8.906642,7.232149,-4.334072,-8.341341,-0.957563,-3.119849,7.469566,-9.486600,2.817386,9.042803,9.067636],[-3.630729,-6.234675,0.798623,2.881130,2.679047,-1.927541,9.873120,-9.271950,6.572453,7.059222,4.411572,-3.199377],[-0.563335,-1.874320,-3.869885,-8.441478,-6.566247,-2.567849,7.875860,-1.518193,6.800685,2.867289,6.855539,-8.408868],[-1.182593,-5.726715,4.620652,-3.396351,-4.190027,5.830834,-6.492299,3.465252,5.016667,-9.771414,-4.299724,7.843212],[-9.836410,-6.981480,-7.619502,-9.214695,-9.011470,5.558853,-6.035999,2.218359,-4.910117,1.703248,-6.763346,-0.855925],[-9.181035,-3.381271,5.420643,8.571393,-7.077383,4.174460,-3.517404,-2.440430,-4.801905,-8.061475,3.470471,2.177658]],[[3.027821,-5.079451,-8.823985,4.537138,-5.017617,8.385076,3.711318,5.751937,-4.679139,-7.940732,-4.455367,-0.477964],[-1.167074,9.323162,-1.515029,-1.671095,-4.322196,-4.248589,1.692181,7.066015,3.474597,9.626941,3.677482,3.579457],[1.838502,1.740461,-8.799172,-9.415735,-9.680852,-7.463551,-3.338584,-4.701951,6.900321,4.816464,-8.721598,-5.721390],[0.376394,-5.114118,-8.874335,8.643395,-1.140228,-2.783513,-0.777572,8.603554,-7.776530,0.754324,-7.066144,4.253748],[-4.366582,-2.071378,-6.711582,6.912330,-5.151353,-9.713847,8.356569,-3.598529,-3.635911,-6.035075,4.439853,-8.316499],[5.238417,1.388352,0.618505,6.364569,0.967649,8.333611,1.985220,-4.238271,-3.992397,-0.331147,-9.045173,0.656333]],[[5.589031,2.816912,-1.502365,6.845108,5.247277,4.893162,3.964486,4.051784,3.052796,-5.887353,0.436308,-8.172869],[-1.657089,9.546955,-9.516607,7.860696,-5.469163,-1.456602,-6.634170,-2.276670,-7.096867,7.663020,-8.657410,8.519329],[0.599008,-9.585487,-2.849108,-4.327309,-8.920052,6.927287,0.346771,-6.183587,7.520321,-9.014372,-7.700321,1.268259],[-5.438002,2.437629,5.073862,-0.525256,-4.152063,1.540839,-0.657952,4.918191,1.076584,0.357104,-4.127211,-4.281200],[-5.819720,3.339899,1.378810,-3.223022,6.717721,5.133980,-5.588673,2.145979,-9.522882,3.443722,2.119918,6.098095],[8.424281,7.106248,9.607585,0.152570,-1.488091,-5.885780,6.760229,3.194051,-0.884731,-2.927906,2.657240,-1.255305]],[[-7.822923,-9.099219,-3.796823,9.905935,-4.467006,7.168705,-4.591915,6.509745,-5.355618,1.823287,-7.364049,-9.658149],[5.202994,5.512638,4.394485,-2.599045,2.470644,6.857493,4.591614,9.515305,9.311090,7.860477,4.867668,-8.743072],[-4.431977,-5.736440,-6.913460,-0.772214,7.460313,-3.478484,5.788070,-5.675438,4.856367,-2.348388,-0.359196,-7.782921],[3.177497,-7.335156,2.620796,-0.817026,-7.498731,-8.733221,6.015491,-3.050554,6.510859,8.006089,8.950714,9.716571],[9.044754,1.909126,-0.931032,7.446397,1.981656,-4.208722,-8.424611,6.275786,3.756721,-8.201951,-1.450417,2.315268],[6.192766,-6.063478,4.671037,-3.045881,7.984051,-7.181235,0.180857,1.205786,8.492651,3.620991,-9.886809,-1.787201]],[[4.304745,1.212123,7.578119,3.313669,0.065517,-5.190706,6.507238,-1.051749,-2.731212,-3.382677,-6.065037,4.420280],[-9.472087,-7.433480,2.822973,-2.131686,5.866505,-7.262705,0.346673,2.517097,8.007483,3.016715,-6.297107,4.268513],[-4.541455,4.753624,-5.078299,2.431299,6.965130,9.229189,-5.037183,4.616561,3.253883,9.752336,3.227399,-4.721378],[-1.093307,-6.951227,9.352667,3.397182,7.464864,-6.217583,8.162072,-0.197343,7.598722,7.749766,-8.608723,6.404041],[-8.717903,-8.249455,-4.529791,-4.067832,-4.534129,9.120171,2.893037,7.347217,3.582142,-9.308126,6.122475,-0.820835],[-2.300728,4.982399,-1.853426,5.313264,3.170022,8.796979,-4.080333,-7.004553,-8.186318,-1.750890,-1.387851,-4.331238]],[[3.712656,6.100603,-2.566165,-9.216284,0.013699,0.167955,-7.956724,3.826460,-2.669150,3.017496,-3.690300,0.467252],[-3.992581,-3.683569,2.138450,-2.083586,1.331468,-9.725967,1.734438,2.864360,-9.027072,0.490946,1.666516,-4.733060],[4.885836,-3.553010,8.481066,-6.201735,5.752791,-7.893151,2.581517,3.282974,-6.422999,-2.213207,-7.316540,1.670229],[-0.022575,-0.852637,3.851118,2.061177,-5.778048,-0.917487,9.584547,8.069164,-0.368720,-4.962645,4.642857,-0.892652],[4.359292,1.522557,-4.044493,-9.509367,1.275387,-4.708226,3.758877,4.448076,5.532419,9.768522,-1.927073,1.629109],[-6.744876,6.204108,-8.398133,-3.006042,-6.918867,2.940858,-3.954454,-6.069052,-5.734648,-3.038088,-9.838939,-7.344543]]], dtype = "float64")#candidate|4323|(13, 6, 12)|const|float64
bop_4324 = relay.mod(var_4322.astype('float64'), relay.reshape(const_4323.astype('float64'), relay.shape_of(var_4322))) # shape=(13, 6, 12)
func_3724_call = mod.get_global_var('func_3724')
func_3726_call = mutated_mod.get_global_var('func_3726')
call_4329 = relay.TupleGetItem(func_3724_call(), 0)
call_4330 = relay.TupleGetItem(func_3726_call(), 0)
output = relay.Tuple([bop_4324,call_4329,])
output2 = relay.Tuple([bop_4324,call_4330,])
func_4346 = relay.Function([var_4322,], output)
mod['func_4346'] = func_4346
mod = relay.transform.InferType()(mod)
mutated_mod['func_4346'] = func_4346
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4347 = relay.var("var_4347", dtype = "float64", shape = (13, 6, 12))#candidate|4347|(13, 6, 12)|var|float64
func_4346_call = mutated_mod.get_global_var('func_4346')
call_4348 = func_4346_call(var_4347)
output = call_4348
func_4349 = relay.Function([var_4347], output)
mutated_mod['func_4349'] = func_4349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1451_call = mod.get_global_var('func_1451')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_4448 = relay.TupleGetItem(func_1451_call(), 0)
call_4449 = relay.TupleGetItem(func_1452_call(), 0)
uop_4464 = relay.cos(call_4448.astype('float32')) # shape=(13, 8, 8)
uop_4466 = relay.cos(call_4449.astype('float32')) # shape=(13, 8, 8)
output = uop_4464
output2 = uop_4466
func_4467 = relay.Function([], output)
mod['func_4467'] = func_4467
mod = relay.transform.InferType()(mod)
mutated_mod['func_4467'] = func_4467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4467_call = mutated_mod.get_global_var('func_4467')
call_4468 = func_4467_call()
output = call_4468
func_4469 = relay.Function([], output)
mutated_mod['func_4469'] = func_4469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_4531 = relay.TupleGetItem(func_319_call(), 0)
call_4532 = relay.TupleGetItem(func_321_call(), 0)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_4535 = func_876_call()
call_4536 = func_876_call()
func_2670_call = mod.get_global_var('func_2670')
func_2673_call = mutated_mod.get_global_var('func_2673')
const_4541 = relay.const([[-9,-4,-4,2,8,-8,-1,2,-10,-4,4,-6,5,-6,-4,-9,-3,-3,-1,2,-2,-4,3,-8,-2,9,-10,-1,-9,-9,-9,-5,9,-9,4],[-10,2,-9,9,-9,2,9,5,8,8,6,-6,-10,-8,7,-10,10,10,-8,-9,-4,-7,2,2,5,-7,-7,-1,-10,-8,2,-4,2,4,-5],[-9,3,-1,-5,6,2,10,-8,8,1,-3,-6,7,-2,-9,5,7,1,6,-10,-5,-8,2,7,4,-6,1,5,-1,3,4,-8,-10,9,-5],[8,9,-7,2,1,-2,-4,-10,-4,-5,-10,7,-10,-5,10,-7,-1,4,9,4,1,-6,2,3,-6,-3,7,-4,-6,7,-10,4,-3,3,-4],[10,4,10,4,4,-2,-8,-8,8,-3,7,1,7,10,4,7,-9,3,-7,-5,-1,-9,-5,-3,-10,-8,-10,-8,1,-4,-4,-2,-2,-4,-4],[-1,5,-3,-6,1,-1,-2,-8,-7,-2,7,-2,9,-3,-2,-4,-1,-4,7,-9,7,-9,-2,-1,9,7,-9,4,2,3,-6,8,5,-2,-1],[5,2,9,5,2,-3,-10,10,2,-3,8,3,-7,-8,-5,9,-9,5,6,7,-4,8,5,-9,-2,4,-2,-5,-7,7,10,-3,-8,6,-10],[1,-3,9,-9,-5,-9,-2,-5,-1,8,6,3,-8,10,4,-6,6,-5,9,3,6,2,4,-3,-2,2,-10,9,-5,-1,-3,-3,-6,3,-4],[-9,8,-8,-1,-9,3,-2,6,10,-2,-2,8,3,-6,1,-3,-10,-2,-7,-3,-5,-8,1,8,-7,4,7,-5,-8,-7,10,-7,-4,3,1],[6,2,3,-7,-7,-3,-4,-3,-1,9,-9,-9,-3,7,-4,2,6,-3,-9,2,-5,-7,7,7,2,-7,8,7,-1,-7,-5,-5,5,2,10],[-10,-10,5,6,7,-9,8,2,-9,2,-8,-5,7,-2,-3,-4,-9,-9,-4,-6,2,-9,5,6,6,9,4,-6,-5,-2,1,1,-4,4,-5]], dtype = "uint8")#candidate|4541|(11, 35)|const|uint8
call_4540 = relay.TupleGetItem(func_2670_call(relay.reshape(const_4541.astype('uint8'), [11, 7, 5])), 1)
call_4542 = relay.TupleGetItem(func_2673_call(relay.reshape(const_4541.astype('uint8'), [11, 7, 5])), 1)
output = relay.Tuple([call_4531,call_4535,call_4540,const_4541,])
output2 = relay.Tuple([call_4532,call_4536,call_4542,const_4541,])
func_4548 = relay.Function([], output)
mod['func_4548'] = func_4548
mod = relay.transform.InferType()(mod)
output = func_4548()
func_4549 = relay.Function([], output)
mutated_mod['func_4549'] = func_4549
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4582 = relay.var("var_4582", dtype = "float32", shape = (5, 6, 6))#candidate|4582|(5, 6, 6)|var|float32
uop_4583 = relay.sigmoid(var_4582.astype('float32')) # shape=(5, 6, 6)
var_4588 = relay.var("var_4588", dtype = "float32", shape = (5, 6, 6))#candidate|4588|(5, 6, 6)|var|float32
bop_4589 = relay.floor_divide(var_4582.astype('float64'), relay.reshape(var_4588.astype('float64'), relay.shape_of(var_4582))) # shape=(5, 6, 6)
func_2085_call = mod.get_global_var('func_2085')
func_2088_call = mutated_mod.get_global_var('func_2088')
var_4597 = relay.var("var_4597", dtype = "float32", shape = (72,))#candidate|4597|(72,)|var|float32
call_4596 = func_2085_call(relay.reshape(var_4597.astype('float32'), [8, 1, 9]))
call_4598 = func_2085_call(relay.reshape(var_4597.astype('float32'), [8, 1, 9]))
uop_4610 = relay.sqrt(uop_4583.astype('float32')) # shape=(5, 6, 6)
output = relay.Tuple([bop_4589,call_4596,var_4597,uop_4610,])
output2 = relay.Tuple([bop_4589,call_4598,var_4597,uop_4610,])
func_4612 = relay.Function([var_4582,var_4588,var_4597,], output)
mod['func_4612'] = func_4612
mod = relay.transform.InferType()(mod)
mutated_mod['func_4612'] = func_4612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4612_call = mutated_mod.get_global_var('func_4612')
var_4614 = relay.var("var_4614", dtype = "float32", shape = (5, 6, 6))#candidate|4614|(5, 6, 6)|var|float32
var_4615 = relay.var("var_4615", dtype = "float32", shape = (5, 6, 6))#candidate|4615|(5, 6, 6)|var|float32
var_4616 = relay.var("var_4616", dtype = "float32", shape = (72,))#candidate|4616|(72,)|var|float32
call_4613 = func_4612_call(var_4614,var_4615,var_4616,)
output = call_4613
func_4617 = relay.Function([var_4614,var_4615,var_4616,], output)
mutated_mod['func_4617'] = func_4617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_610_call = mod.get_global_var('func_610')
func_611_call = mutated_mod.get_global_var('func_611')
call_4662 = func_610_call()
call_4663 = func_610_call()
func_3981_call = mod.get_global_var('func_3981')
func_3983_call = mutated_mod.get_global_var('func_3983')
call_4686 = relay.TupleGetItem(func_3981_call(), 0)
call_4687 = relay.TupleGetItem(func_3983_call(), 0)
output = relay.Tuple([call_4662,call_4686,])
output2 = relay.Tuple([call_4663,call_4687,])
func_4690 = relay.Function([], output)
mod['func_4690'] = func_4690
mod = relay.transform.InferType()(mod)
mutated_mod['func_4690'] = func_4690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4690_call = mutated_mod.get_global_var('func_4690')
call_4691 = func_4690_call()
output = call_4691
func_4692 = relay.Function([], output)
mutated_mod['func_4692'] = func_4692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4548_call = mod.get_global_var('func_4548')
func_4549_call = mutated_mod.get_global_var('func_4549')
call_4717 = relay.TupleGetItem(func_4548_call(), 2)
call_4718 = relay.TupleGetItem(func_4549_call(), 2)
func_2217_call = mod.get_global_var('func_2217')
func_2219_call = mutated_mod.get_global_var('func_2219')
var_4728 = relay.var("var_4728", dtype = "float64", shape = (1, 440))#candidate|4728|(1, 440)|var|float64
call_4727 = relay.TupleGetItem(func_2217_call(relay.reshape(var_4728.astype('float64'), [5, 11, 8])), 0)
call_4729 = relay.TupleGetItem(func_2219_call(relay.reshape(var_4728.astype('float64'), [5, 11, 8])), 0)
func_2783_call = mod.get_global_var('func_2783')
func_2786_call = mutated_mod.get_global_var('func_2786')
var_4745 = relay.var("var_4745", dtype = "float64", shape = (832,))#candidate|4745|(832,)|var|float64
call_4744 = relay.TupleGetItem(func_2783_call(relay.reshape(var_4745.astype('float64'), [13, 8, 8])), 0)
call_4746 = relay.TupleGetItem(func_2786_call(relay.reshape(var_4745.astype('float64'), [13, 8, 8])), 0)
uop_4749 = relay.log(var_4745.astype('float32')) # shape=(832,)
uop_4768 = relay.rsqrt(uop_4749.astype('float32')) # shape=(832,)
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_4771 = func_340_call()
call_4772 = func_340_call()
output = relay.Tuple([call_4717,call_4727,var_4728,call_4744,uop_4768,call_4771,])
output2 = relay.Tuple([call_4718,call_4729,var_4728,call_4746,uop_4768,call_4772,])
func_4775 = relay.Function([var_4728,var_4745,], output)
mod['func_4775'] = func_4775
mod = relay.transform.InferType()(mod)
mutated_mod['func_4775'] = func_4775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4775_call = mutated_mod.get_global_var('func_4775')
var_4777 = relay.var("var_4777", dtype = "float64", shape = (1, 440))#candidate|4777|(1, 440)|var|float64
var_4778 = relay.var("var_4778", dtype = "float64", shape = (832,))#candidate|4778|(832,)|var|float64
call_4776 = func_4775_call(var_4777,var_4778,)
output = call_4776
func_4779 = relay.Function([var_4777,var_4778,], output)
mutated_mod['func_4779'] = func_4779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_4803 = relay.TupleGetItem(func_319_call(), 1)
call_4804 = relay.TupleGetItem(func_321_call(), 1)
output = call_4803
output2 = call_4804
func_4813 = relay.Function([], output)
mod['func_4813'] = func_4813
mod = relay.transform.InferType()(mod)
output = func_4813()
func_4814 = relay.Function([], output)
mutated_mod['func_4814'] = func_4814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4231_call = mod.get_global_var('func_4231')
func_4232_call = mutated_mod.get_global_var('func_4232')
call_4818 = relay.TupleGetItem(func_4231_call(), 0)
call_4819 = relay.TupleGetItem(func_4232_call(), 0)
output = call_4818
output2 = call_4819
func_4822 = relay.Function([], output)
mod['func_4822'] = func_4822
mod = relay.transform.InferType()(mod)
mutated_mod['func_4822'] = func_4822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4822_call = mutated_mod.get_global_var('func_4822')
call_4823 = func_4822_call()
output = call_4823
func_4824 = relay.Function([], output)
mutated_mod['func_4824'] = func_4824
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4828 = relay.var("var_4828", dtype = "float64", shape = (16, 3, 12))#candidate|4828|(16, 3, 12)|var|float64
uop_4829 = relay.asinh(var_4828.astype('float64')) # shape=(16, 3, 12)
output = uop_4829
output2 = uop_4829
func_4832 = relay.Function([var_4828,], output)
mod['func_4832'] = func_4832
mod = relay.transform.InferType()(mod)
var_4833 = relay.var("var_4833", dtype = "float64", shape = (16, 3, 12))#candidate|4833|(16, 3, 12)|var|float64
output = func_4832(var_4833)
func_4834 = relay.Function([var_4833], output)
mutated_mod['func_4834'] = func_4834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_4844 = relay.TupleGetItem(func_319_call(), 1)
call_4845 = relay.TupleGetItem(func_321_call(), 1)
func_942_call = mod.get_global_var('func_942')
func_944_call = mutated_mod.get_global_var('func_944')
call_4863 = relay.TupleGetItem(func_942_call(), 1)
call_4864 = relay.TupleGetItem(func_944_call(), 1)
output = relay.Tuple([call_4844,call_4863,])
output2 = relay.Tuple([call_4845,call_4864,])
func_4872 = relay.Function([], output)
mod['func_4872'] = func_4872
mod = relay.transform.InferType()(mod)
output = func_4872()
func_4873 = relay.Function([], output)
mutated_mod['func_4873'] = func_4873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1512_call = mod.get_global_var('func_1512')
func_1513_call = mutated_mod.get_global_var('func_1513')
call_4892 = func_1512_call()
call_4893 = func_1512_call()
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_4904 = relay.TupleGetItem(func_1753_call(), 0)
call_4905 = relay.TupleGetItem(func_1754_call(), 0)
output = relay.Tuple([call_4892,call_4904,])
output2 = relay.Tuple([call_4893,call_4905,])
func_4912 = relay.Function([], output)
mod['func_4912'] = func_4912
mod = relay.transform.InferType()(mod)
mutated_mod['func_4912'] = func_4912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4912_call = mutated_mod.get_global_var('func_4912')
call_4913 = func_4912_call()
output = call_4913
func_4914 = relay.Function([], output)
mutated_mod['func_4914'] = func_4914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1512_call = mod.get_global_var('func_1512')
func_1513_call = mutated_mod.get_global_var('func_1513')
call_4925 = func_1512_call()
call_4926 = func_1512_call()
func_1688_call = mod.get_global_var('func_1688')
func_1690_call = mutated_mod.get_global_var('func_1690')
call_4945 = relay.TupleGetItem(func_1688_call(), 1)
call_4946 = relay.TupleGetItem(func_1690_call(), 1)
output = relay.Tuple([call_4925,call_4945,])
output2 = relay.Tuple([call_4926,call_4946,])
func_4947 = relay.Function([], output)
mod['func_4947'] = func_4947
mod = relay.transform.InferType()(mod)
output = func_4947()
func_4948 = relay.Function([], output)
mutated_mod['func_4948'] = func_4948
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5087 = relay.var("var_5087", dtype = "float64", shape = (10, 2, 7))#candidate|5087|(10, 2, 7)|var|float64
const_5088 = relay.const([[[4.700814,-7.832675,2.255036,0.526589,2.464819,-9.747122,3.939260],[-6.361619,-9.903873,-0.138499,-2.273694,9.503412,-4.260748,7.474406]],[[8.150814,8.254202,-4.416840,9.042033,0.108419,-0.470037,5.863432],[-1.499933,1.920583,-5.940773,-1.694014,-1.061696,2.331390,-6.353263]],[[-0.449742,8.204534,-2.004119,2.007451,-2.138071,6.949552,2.453749],[9.317583,-0.188019,1.688002,-7.364318,7.514779,-5.471185,1.162938]],[[-8.547097,4.808465,5.717893,-7.426225,0.799100,-2.731876,-9.228315],[1.148318,4.760918,6.675996,-4.652264,-5.032509,-8.102390,-0.903391]],[[0.655550,-5.067125,5.156921,8.728841,-8.260212,-2.940692,6.846443],[-9.634756,-2.570127,7.357679,-4.948195,3.216478,8.987616,5.599682]],[[-2.581417,-0.636382,0.469496,0.645039,3.252084,0.808620,-6.631571],[6.744454,-0.378668,-9.836593,-7.532006,-8.341958,-8.580918,9.725924]],[[4.236726,9.253980,-2.425475,-5.468495,-3.546118,-3.083940,-5.655400],[-0.324104,-4.844015,-5.582031,2.605481,7.952653,-3.474489,-3.280812]],[[-6.456361,-6.362245,-9.307540,2.713107,1.001798,-9.229529,2.078854],[7.918992,-4.022938,-7.468902,-0.515440,5.799098,5.463040,6.275463]],[[-5.517246,-9.527340,7.936648,0.144538,-8.154198,6.946760,-9.665310],[-1.962792,-6.150565,9.412167,7.172076,9.539606,-6.057829,0.211694]],[[-1.673924,4.441269,-1.563728,2.361128,-5.544221,6.309900,2.184351],[-5.297305,-0.496988,8.239748,7.721273,5.091078,-9.955056,-4.569511]]], dtype = "float64")#candidate|5088|(10, 2, 7)|const|float64
bop_5089 = relay.divide(var_5087.astype('float64'), relay.reshape(const_5088.astype('float64'), relay.shape_of(var_5087))) # shape=(10, 2, 7)
func_1451_call = mod.get_global_var('func_1451')
func_1452_call = mutated_mod.get_global_var('func_1452')
call_5096 = relay.TupleGetItem(func_1451_call(), 0)
call_5097 = relay.TupleGetItem(func_1452_call(), 0)
uop_5098 = relay.sqrt(const_5088.astype('float64')) # shape=(10, 2, 7)
output = relay.Tuple([bop_5089,call_5096,uop_5098,])
output2 = relay.Tuple([bop_5089,call_5097,uop_5098,])
func_5100 = relay.Function([var_5087,], output)
mod['func_5100'] = func_5100
mod = relay.transform.InferType()(mod)
mutated_mod['func_5100'] = func_5100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5101 = relay.var("var_5101", dtype = "float64", shape = (10, 2, 7))#candidate|5101|(10, 2, 7)|var|float64
func_5100_call = mutated_mod.get_global_var('func_5100')
call_5102 = func_5100_call(var_5101)
output = call_5102
func_5103 = relay.Function([var_5101], output)
mutated_mod['func_5103'] = func_5103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2525_call = mod.get_global_var('func_2525')
func_2527_call = mutated_mod.get_global_var('func_2527')
call_5111 = func_2525_call()
call_5112 = func_2525_call()
func_2710_call = mod.get_global_var('func_2710')
func_2712_call = mutated_mod.get_global_var('func_2712')
call_5133 = relay.TupleGetItem(func_2710_call(), 0)
call_5134 = relay.TupleGetItem(func_2712_call(), 0)
output = relay.Tuple([call_5111,call_5133,])
output2 = relay.Tuple([call_5112,call_5134,])
func_5142 = relay.Function([], output)
mod['func_5142'] = func_5142
mod = relay.transform.InferType()(mod)
mutated_mod['func_5142'] = func_5142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5142_call = mutated_mod.get_global_var('func_5142')
call_5143 = func_5142_call()
output = call_5143
func_5144 = relay.Function([], output)
mutated_mod['func_5144'] = func_5144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1937_call = mod.get_global_var('func_1937')
func_1939_call = mutated_mod.get_global_var('func_1939')
call_5174 = func_1937_call()
call_5175 = func_1937_call()
uop_5180 = relay.atan(call_5174.astype('float32')) # shape=(5, 11, 8)
uop_5182 = relay.atan(call_5175.astype('float32')) # shape=(5, 11, 8)
func_2422_call = mod.get_global_var('func_2422')
func_2425_call = mutated_mod.get_global_var('func_2425')
const_5190 = relay.const([-1.930594,-2.324285,-7.796984,7.450208,1.308623,-2.379845,-3.473997,4.030477,-1.345986,-4.885058,8.114834,-5.885202,-5.551584,9.406764,0.253725,9.519174,6.135205,8.933257,-1.870215,8.212440,-9.171906,0.305764,-6.668891,-4.204926,2.572576,5.381122,2.180201,-4.096551,-4.264358,4.488654,-4.027056,3.671232,-8.224567,-5.870999,4.352095,2.307278,8.573593,7.889238,3.915511,6.448798,-6.863314,6.870896,-5.280022,6.067606,-6.305352,7.388307,-0.818117,-8.349013,4.528073,1.088691,-3.659278,1.851822,3.886387,4.055947,-9.675760,4.158602,2.158755,-6.116664,7.665598,-4.321696,-2.019511,-6.082334,-3.579091,-4.286762,2.385257,1.484410,-2.995646,-1.354208,9.587587,-0.875058,-1.930713,-8.247476], dtype = "float32")#candidate|5190|(72,)|const|float32
call_5189 = relay.TupleGetItem(func_2422_call(relay.reshape(const_5190.astype('float32'), [72,])), 2)
call_5191 = relay.TupleGetItem(func_2425_call(relay.reshape(const_5190.astype('float32'), [72,])), 2)
output = relay.Tuple([uop_5180,call_5189,const_5190,])
output2 = relay.Tuple([uop_5182,call_5191,const_5190,])
func_5193 = relay.Function([], output)
mod['func_5193'] = func_5193
mod = relay.transform.InferType()(mod)
output = func_5193()
func_5194 = relay.Function([], output)
mutated_mod['func_5194'] = func_5194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4317_call = mod.get_global_var('func_4317')
func_4318_call = mutated_mod.get_global_var('func_4318')
call_5208 = relay.TupleGetItem(func_4317_call(), 1)
call_5209 = relay.TupleGetItem(func_4318_call(), 1)
output = relay.Tuple([call_5208,])
output2 = relay.Tuple([call_5209,])
func_5210 = relay.Function([], output)
mod['func_5210'] = func_5210
mod = relay.transform.InferType()(mod)
output = func_5210()
func_5211 = relay.Function([], output)
mutated_mod['func_5211'] = func_5211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4086_call = mod.get_global_var('func_4086')
func_4087_call = mutated_mod.get_global_var('func_4087')
call_5237 = relay.TupleGetItem(func_4086_call(), 0)
call_5238 = relay.TupleGetItem(func_4087_call(), 0)
func_3587_call = mod.get_global_var('func_3587')
func_3588_call = mutated_mod.get_global_var('func_3588')
call_5245 = func_3587_call()
call_5246 = func_3587_call()
func_2670_call = mod.get_global_var('func_2670')
func_2673_call = mutated_mod.get_global_var('func_2673')
var_5250 = relay.var("var_5250", dtype = "uint8", shape = (385,))#candidate|5250|(385,)|var|uint8
call_5249 = relay.TupleGetItem(func_2670_call(relay.reshape(var_5250.astype('uint8'), [11, 7, 5])), 0)
call_5251 = relay.TupleGetItem(func_2673_call(relay.reshape(var_5250.astype('uint8'), [11, 7, 5])), 0)
output = relay.Tuple([call_5237,call_5245,call_5249,var_5250,])
output2 = relay.Tuple([call_5238,call_5246,call_5251,var_5250,])
func_5261 = relay.Function([var_5250,], output)
mod['func_5261'] = func_5261
mod = relay.transform.InferType()(mod)
mutated_mod['func_5261'] = func_5261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5262 = relay.var("var_5262", dtype = "uint8", shape = (385,))#candidate|5262|(385,)|var|uint8
func_5261_call = mutated_mod.get_global_var('func_5261')
call_5263 = func_5261_call(var_5262)
output = call_5263
func_5264 = relay.Function([var_5262], output)
mutated_mod['func_5264'] = func_5264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_655_call = mod.get_global_var('func_655')
func_657_call = mutated_mod.get_global_var('func_657')
call_5289 = func_655_call()
call_5290 = func_655_call()
output = relay.Tuple([call_5289,])
output2 = relay.Tuple([call_5290,])
func_5316 = relay.Function([], output)
mod['func_5316'] = func_5316
mod = relay.transform.InferType()(mod)
mutated_mod['func_5316'] = func_5316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5316_call = mutated_mod.get_global_var('func_5316')
call_5317 = func_5316_call()
output = call_5317
func_5318 = relay.Function([], output)
mutated_mod['func_5318'] = func_5318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2396_call = mod.get_global_var('func_2396')
func_2398_call = mutated_mod.get_global_var('func_2398')
call_5334 = func_2396_call()
call_5335 = func_2396_call()
func_1913_call = mod.get_global_var('func_1913')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_5338 = relay.TupleGetItem(func_1913_call(), 0)
call_5339 = relay.TupleGetItem(func_1914_call(), 0)
output = relay.Tuple([call_5334,call_5338,])
output2 = relay.Tuple([call_5335,call_5339,])
func_5351 = relay.Function([], output)
mod['func_5351'] = func_5351
mod = relay.transform.InferType()(mod)
mutated_mod['func_5351'] = func_5351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5351_call = mutated_mod.get_global_var('func_5351')
call_5352 = func_5351_call()
output = call_5352
func_5353 = relay.Function([], output)
mutated_mod['func_5353'] = func_5353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5351_call = mod.get_global_var('func_5351')
func_5353_call = mutated_mod.get_global_var('func_5353')
call_5358 = relay.TupleGetItem(func_5351_call(), 1)
call_5359 = relay.TupleGetItem(func_5353_call(), 1)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_5374 = func_815_call()
call_5375 = func_815_call()
output = relay.Tuple([call_5358,call_5374,])
output2 = relay.Tuple([call_5359,call_5375,])
func_5378 = relay.Function([], output)
mod['func_5378'] = func_5378
mod = relay.transform.InferType()(mod)
mutated_mod['func_5378'] = func_5378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5378_call = mutated_mod.get_global_var('func_5378')
call_5379 = func_5378_call()
output = call_5379
func_5380 = relay.Function([], output)
mutated_mod['func_5380'] = func_5380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3587_call = mod.get_global_var('func_3587')
func_3588_call = mutated_mod.get_global_var('func_3588')
call_5453 = func_3587_call()
call_5454 = func_3587_call()
output = relay.Tuple([call_5453,])
output2 = relay.Tuple([call_5454,])
func_5495 = relay.Function([], output)
mod['func_5495'] = func_5495
mod = relay.transform.InferType()(mod)
output = func_5495()
func_5496 = relay.Function([], output)
mutated_mod['func_5496'] = func_5496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_5499 = relay.TupleGetItem(func_206_call(), 0)
call_5500 = relay.TupleGetItem(func_207_call(), 0)
func_1247_call = mod.get_global_var('func_1247')
func_1250_call = mutated_mod.get_global_var('func_1250')
var_5515 = relay.var("var_5515", dtype = "float64", shape = (30,))#candidate|5515|(30,)|var|float64
call_5514 = relay.TupleGetItem(func_1247_call(relay.reshape(var_5515.astype('float64'), [6, 1, 5]), relay.reshape(var_5515.astype('float64'), [6, 1, 5]), ), 3)
call_5516 = relay.TupleGetItem(func_1250_call(relay.reshape(var_5515.astype('float64'), [6, 1, 5]), relay.reshape(var_5515.astype('float64'), [6, 1, 5]), ), 3)
output = relay.Tuple([call_5499,call_5514,var_5515,])
output2 = relay.Tuple([call_5500,call_5516,var_5515,])
func_5519 = relay.Function([var_5515,], output)
mod['func_5519'] = func_5519
mod = relay.transform.InferType()(mod)
mutated_mod['func_5519'] = func_5519
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5520 = relay.var("var_5520", dtype = "float64", shape = (30,))#candidate|5520|(30,)|var|float64
func_5519_call = mutated_mod.get_global_var('func_5519')
call_5521 = func_5519_call(var_5520)
output = call_5521
func_5522 = relay.Function([var_5520], output)
mutated_mod['func_5522'] = func_5522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_5548 = relay.TupleGetItem(func_319_call(), 1)
call_5549 = relay.TupleGetItem(func_321_call(), 1)
output = relay.Tuple([call_5548,])
output2 = relay.Tuple([call_5549,])
func_5561 = relay.Function([], output)
mod['func_5561'] = func_5561
mod = relay.transform.InferType()(mod)
mutated_mod['func_5561'] = func_5561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5561_call = mutated_mod.get_global_var('func_5561')
call_5562 = func_5561_call()
output = call_5562
func_5563 = relay.Function([], output)
mutated_mod['func_5563'] = func_5563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_5595 = relay.TupleGetItem(func_1416_call(), 0)
call_5596 = relay.TupleGetItem(func_1417_call(), 0)
output = relay.Tuple([call_5595,])
output2 = relay.Tuple([call_5596,])
func_5602 = relay.Function([], output)
mod['func_5602'] = func_5602
mod = relay.transform.InferType()(mod)
mutated_mod['func_5602'] = func_5602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5602_call = mutated_mod.get_global_var('func_5602')
call_5603 = func_5602_call()
output = call_5603
func_5604 = relay.Function([], output)
mutated_mod['func_5604'] = func_5604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3835_call = mod.get_global_var('func_3835')
func_3836_call = mutated_mod.get_global_var('func_3836')
call_5635 = relay.TupleGetItem(func_3835_call(), 0)
call_5636 = relay.TupleGetItem(func_3836_call(), 0)
func_2217_call = mod.get_global_var('func_2217')
func_2219_call = mutated_mod.get_global_var('func_2219')
call_5639 = relay.TupleGetItem(func_2217_call(relay.reshape(call_5635.astype('float64'), [5, 11, 8])), 0)
call_5640 = relay.TupleGetItem(func_2219_call(relay.reshape(call_5635.astype('float64'), [5, 11, 8])), 0)
output = relay.Tuple([call_5635,call_5639,])
output2 = relay.Tuple([call_5636,call_5640,])
func_5643 = relay.Function([], output)
mod['func_5643'] = func_5643
mod = relay.transform.InferType()(mod)
mutated_mod['func_5643'] = func_5643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5643_call = mutated_mod.get_global_var('func_5643')
call_5644 = func_5643_call()
output = call_5644
func_5645 = relay.Function([], output)
mutated_mod['func_5645'] = func_5645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_5656 = func_815_call()
call_5657 = func_815_call()
output = call_5656
output2 = call_5657
func_5662 = relay.Function([], output)
mod['func_5662'] = func_5662
mod = relay.transform.InferType()(mod)
mutated_mod['func_5662'] = func_5662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5662_call = mutated_mod.get_global_var('func_5662')
call_5663 = func_5662_call()
output = call_5663
func_5664 = relay.Function([], output)
mutated_mod['func_5664'] = func_5664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mod.get_global_var('func_1483')
func_1484_call = mutated_mod.get_global_var('func_1484')
call_5700 = func_1483_call()
call_5701 = func_1483_call()
uop_5708 = relay.asinh(call_5700.astype('float32')) # shape=(15, 16, 10)
uop_5710 = relay.asinh(call_5701.astype('float32')) # shape=(15, 16, 10)
func_655_call = mod.get_global_var('func_655')
func_657_call = mutated_mod.get_global_var('func_657')
call_5715 = func_655_call()
call_5716 = func_655_call()
uop_5735 = relay.acosh(call_5700.astype('float64')) # shape=(15, 16, 10)
uop_5737 = relay.acosh(call_5701.astype('float64')) # shape=(15, 16, 10)
output = relay.Tuple([uop_5708,call_5715,uop_5735,])
output2 = relay.Tuple([uop_5710,call_5716,uop_5737,])
func_5741 = relay.Function([], output)
mod['func_5741'] = func_5741
mod = relay.transform.InferType()(mod)
mutated_mod['func_5741'] = func_5741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5741_call = mutated_mod.get_global_var('func_5741')
call_5742 = func_5741_call()
output = call_5742
func_5743 = relay.Function([], output)
mutated_mod['func_5743'] = func_5743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_5744 = relay.TupleGetItem(func_1753_call(), 1)
call_5745 = relay.TupleGetItem(func_1754_call(), 1)
output = relay.Tuple([call_5744,])
output2 = relay.Tuple([call_5745,])
func_5750 = relay.Function([], output)
mod['func_5750'] = func_5750
mod = relay.transform.InferType()(mod)
mutated_mod['func_5750'] = func_5750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5750_call = mutated_mod.get_global_var('func_5750')
call_5751 = func_5750_call()
output = call_5751
func_5752 = relay.Function([], output)
mutated_mod['func_5752'] = func_5752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4317_call = mod.get_global_var('func_4317')
func_4318_call = mutated_mod.get_global_var('func_4318')
call_5770 = relay.TupleGetItem(func_4317_call(), 1)
call_5771 = relay.TupleGetItem(func_4318_call(), 1)
func_5750_call = mod.get_global_var('func_5750')
func_5752_call = mutated_mod.get_global_var('func_5752')
call_5772 = relay.TupleGetItem(func_5750_call(), 0)
call_5773 = relay.TupleGetItem(func_5752_call(), 0)
func_655_call = mod.get_global_var('func_655')
func_657_call = mutated_mod.get_global_var('func_657')
call_5776 = func_655_call()
call_5777 = func_655_call()
func_2369_call = mod.get_global_var('func_2369')
func_2373_call = mutated_mod.get_global_var('func_2373')
var_5783 = relay.var("var_5783", dtype = "uint32", shape = (7, 42))#candidate|5783|(7, 42)|var|uint32
call_5782 = relay.TupleGetItem(func_2369_call(relay.reshape(var_5783.astype('uint32'), [294,]), relay.reshape(var_5783.astype('float32'), [294,]), ), 1)
call_5784 = relay.TupleGetItem(func_2373_call(relay.reshape(var_5783.astype('uint32'), [294,]), relay.reshape(var_5783.astype('float32'), [294,]), ), 1)
var_5785 = relay.var("var_5785", dtype = "float64", shape = (5, 11, 8))#candidate|5785|(5, 11, 8)|var|float64
bop_5786 = relay.logical_or(call_5770.astype('bool'), relay.reshape(var_5785.astype('bool'), relay.shape_of(call_5770))) # shape=(5, 11, 8)
bop_5789 = relay.logical_or(call_5771.astype('bool'), relay.reshape(var_5785.astype('bool'), relay.shape_of(call_5771))) # shape=(5, 11, 8)
func_2396_call = mod.get_global_var('func_2396')
func_2398_call = mutated_mod.get_global_var('func_2398')
call_5804 = func_2396_call()
call_5805 = func_2396_call()
var_5821 = relay.var("var_5821", dtype = "uint32", shape = (7, 42))#candidate|5821|(7, 42)|var|uint32
bop_5822 = relay.multiply(var_5783.astype('int32'), relay.reshape(var_5821.astype('int32'), relay.shape_of(var_5783))) # shape=(7, 42)
output = relay.Tuple([call_5772,call_5776,call_5782,bop_5786,call_5804,bop_5822,])
output2 = relay.Tuple([call_5773,call_5777,call_5784,bop_5789,call_5805,bop_5822,])
func_5828 = relay.Function([var_5783,var_5785,var_5821,], output)
mod['func_5828'] = func_5828
mod = relay.transform.InferType()(mod)
var_5829 = relay.var("var_5829", dtype = "uint32", shape = (7, 42))#candidate|5829|(7, 42)|var|uint32
var_5830 = relay.var("var_5830", dtype = "float64", shape = (5, 11, 8))#candidate|5830|(5, 11, 8)|var|float64
var_5831 = relay.var("var_5831", dtype = "uint32", shape = (7, 42))#candidate|5831|(7, 42)|var|uint32
output = func_5828(var_5829,var_5830,var_5831,)
func_5832 = relay.Function([var_5829,var_5830,var_5831,], output)
mutated_mod['func_5832'] = func_5832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2710_call = mod.get_global_var('func_2710')
func_2712_call = mutated_mod.get_global_var('func_2712')
call_5870 = relay.TupleGetItem(func_2710_call(), 0)
call_5871 = relay.TupleGetItem(func_2712_call(), 0)
output = relay.Tuple([call_5870,])
output2 = relay.Tuple([call_5871,])
func_5876 = relay.Function([], output)
mod['func_5876'] = func_5876
mod = relay.transform.InferType()(mod)
mutated_mod['func_5876'] = func_5876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5876_call = mutated_mod.get_global_var('func_5876')
call_5877 = func_5876_call()
output = call_5877
func_5878 = relay.Function([], output)
mutated_mod['func_5878'] = func_5878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4041_call = mod.get_global_var('func_4041')
func_4043_call = mutated_mod.get_global_var('func_4043')
call_5935 = relay.TupleGetItem(func_4041_call(), 2)
call_5936 = relay.TupleGetItem(func_4043_call(), 2)
output = call_5935
output2 = call_5936
func_5959 = relay.Function([], output)
mod['func_5959'] = func_5959
mod = relay.transform.InferType()(mod)
mutated_mod['func_5959'] = func_5959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5959_call = mutated_mod.get_global_var('func_5959')
call_5960 = func_5959_call()
output = call_5960
func_5961 = relay.Function([], output)
mutated_mod['func_5961'] = func_5961
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6005 = relay.const([[[4.175629,6.015930,5.834830,-1.364616,0.183139,8.440578,-6.561196,6.397659,0.502385,2.221115,-0.824892,-9.871121,4.769917,8.301771,8.264744],[-9.726663,-3.146153,-5.599475,1.408867,-1.401027,-5.001268,0.811487,-3.799134,-2.204336,4.636437,-6.400299,-7.605689,4.606854,-9.058561,-5.856071],[0.787687,7.100327,-2.540741,4.128352,-5.057684,-8.882585,-9.535373,6.108217,-6.099719,-5.175299,1.303165,5.925096,-7.122937,-6.133944,-5.861721],[-8.116175,8.142047,2.696016,4.567610,0.402011,-9.993322,-3.347659,-9.419427,-5.751151,-0.430140,-1.996025,6.797177,0.207984,-0.238793,-2.872353],[-0.713566,0.263024,-3.905662,1.774953,6.677746,-4.024617,-7.054581,-4.170005,-0.105922,9.610230,-2.212412,1.227270,-7.808514,9.005173,-4.457318],[2.527287,-5.572049,-3.123131,7.871690,6.975443,-1.642802,-5.971526,-3.596179,6.103657,5.319837,1.463293,-9.904484,1.398207,9.465440,-3.744977],[4.196620,-6.122447,-6.158584,-2.788490,-0.832312,-7.438679,5.228757,8.395713,-3.975662,5.224187,-4.017528,2.363591,7.022678,2.395149,6.867488],[-5.459669,9.253759,-9.348535,6.398493,1.309330,-9.140397,-9.336963,-4.281910,-7.347144,7.781214,3.212843,-9.317300,-3.533399,8.083323,4.533230],[6.058554,2.699119,-4.305858,-7.509238,5.667671,-0.898093,-0.343445,0.008094,-8.381840,9.670720,5.060950,1.672176,5.749898,4.189698,9.144843],[3.113737,-8.458090,6.104611,-6.184500,-4.341214,1.106816,-3.811479,-3.619396,0.008478,4.454015,-9.947395,5.309348,-2.707928,1.040552,2.421504],[-9.625157,-5.479299,-4.418114,-1.740560,6.655198,-8.888148,3.270923,-5.187924,-5.049887,-6.411675,-8.583505,6.507976,1.672148,-3.002056,1.255053],[2.418313,-0.555501,1.184804,-0.704813,-7.847919,-8.091756,-6.110888,9.847709,0.892702,-2.243295,9.835476,-7.239708,-7.170883,-1.178101,9.165367],[8.535812,-2.328231,-0.020954,-5.049582,1.220642,-6.003324,6.983706,9.259557,-8.171373,-7.403189,-2.234652,7.040185,-4.620505,-1.160971,9.297994],[1.422906,0.195487,-1.272176,4.660366,-2.818679,9.027706,-4.525665,3.005480,0.449148,3.395334,8.788411,2.678543,-8.815033,-4.307889,8.236003],[-7.854446,-5.838763,-1.630730,3.384950,1.001217,-9.022304,2.474038,7.351811,-1.911801,-1.268142,8.234915,3.483312,-7.927595,-4.151194,9.342673]],[[-1.615683,-8.957486,7.607877,-3.667240,-3.310864,-7.402399,-9.451523,-5.001123,-9.204126,1.608466,-2.379371,-9.472465,4.847650,1.370610,-2.814103],[9.157628,1.348850,1.634661,-8.804546,3.164408,-8.140336,4.475235,3.581218,-1.664754,-7.114762,-5.891631,-2.526011,9.092781,-1.260008,-6.328748],[4.036731,7.940462,2.989411,7.117824,-7.491984,8.671163,-2.435101,-2.915277,-0.309473,9.132752,-8.994888,3.345691,7.955123,-4.965219,3.641062],[-2.237128,9.222116,7.954871,-4.701010,-7.903678,-0.750765,6.237895,1.191760,-4.959105,7.604481,-0.940919,-2.580385,-6.918313,-1.243962,0.897135],[6.365087,-8.655550,2.270192,-2.409560,-1.827689,5.483642,-4.979252,0.046699,-2.821336,2.776205,-2.697401,5.793909,0.971101,-0.528623,-3.452381],[6.442345,4.695566,-7.692012,-9.190108,-1.516588,-1.802283,0.403854,4.206240,-5.307104,-9.396117,9.264145,8.658602,9.735936,-3.349730,4.127468],[2.298748,3.030442,-6.107492,-7.663341,-2.977611,-1.535167,-3.200657,4.962404,-2.358541,3.379759,7.870743,2.489586,4.474619,5.372241,-9.842287],[-2.015349,7.352002,-2.490555,-7.657347,-4.469758,-0.954930,0.737780,-2.818654,-3.281186,-6.853507,-3.424123,-8.523052,-7.354298,-5.603615,5.055770],[-8.367757,2.483476,1.833531,-7.612580,-9.552475,-8.545695,6.860745,7.622485,-1.515049,-5.287234,6.794327,-5.106246,9.529154,3.476967,-5.361795],[-4.454919,-1.367966,9.076462,-6.144925,9.751188,-8.506160,3.686044,6.961989,-6.835349,-8.144342,-0.814579,4.446402,0.573215,-0.328755,-6.824616],[3.271536,0.918592,-9.709660,-1.996536,-5.808619,6.967282,1.287273,-8.876853,8.893200,0.410370,-9.821377,7.266217,-0.967030,-9.240521,5.906468],[-4.778225,0.650942,7.127866,-7.745694,-3.434499,9.200012,5.932289,-8.743199,-8.836259,-1.472978,3.713409,4.235299,-8.194032,0.848195,-7.778292],[-5.048052,-2.562088,8.738596,4.901683,6.519191,-9.218966,-4.680895,5.741249,-5.824448,-4.984755,8.445649,6.755933,2.495277,0.943693,-2.411088],[5.727773,-1.479523,-1.933918,7.994138,9.324215,-5.268095,-2.306910,6.515060,4.176158,1.258102,8.010263,-9.063685,9.235306,-5.395264,-2.788668],[1.649951,9.652983,0.621779,3.093114,-5.272465,3.318839,-8.169239,0.554688,-4.961548,1.308932,-7.310869,-9.232546,7.798690,-6.700217,-2.459276]],[[-6.901482,4.627398,7.452638,-3.145770,0.349423,9.011253,3.144685,-6.681568,-3.060545,6.863493,-7.116104,-4.558056,-3.765882,2.433551,4.414013],[-0.938573,5.855344,-6.542154,-9.179664,0.920827,7.629032,9.696780,-2.152050,7.425815,-4.498959,1.104221,-8.243084,0.415564,5.423452,-9.883865],[9.937815,7.253851,-8.288158,5.350605,-5.170579,-5.325264,-1.656251,-9.044782,-6.598458,2.017451,-3.074945,5.592938,-0.397913,-6.825406,4.612564],[-3.002314,2.022836,9.283114,0.293498,-8.391106,9.701849,2.529747,-4.559327,7.733938,9.684547,3.740242,6.846907,1.763565,-4.527474,1.695923],[-9.203118,-3.068953,0.214597,8.649248,-5.485405,-9.635348,-1.484045,4.767013,4.419018,0.671226,1.594626,9.250153,-9.235540,-7.139521,-5.448187],[-8.313336,-9.215990,-2.279985,3.077501,-6.896950,8.675531,7.599558,1.067743,8.478043,4.683954,5.801279,5.680193,2.782176,2.248866,-5.284698],[-3.278867,-1.946551,5.792031,-5.797939,-0.863627,3.505975,-6.966121,-5.641835,2.660951,-5.490237,-7.193224,-7.285154,-8.288683,4.597364,4.275880],[9.149869,9.570948,-8.083265,-4.189523,9.746638,-1.228639,3.359689,3.298369,-5.289992,7.073345,-1.068200,-9.132756,2.796242,-4.953797,8.155893],[1.260344,0.205396,-3.403819,7.305968,4.662612,-4.524801,6.804891,-7.195099,8.143163,-5.910176,0.641285,-4.351416,3.337624,6.722625,3.509385],[9.114932,1.682153,8.598239,2.530131,7.722959,9.011671,-0.879508,6.605320,5.469189,2.077573,9.376617,-2.031929,-6.510175,8.124849,-5.272445],[-9.592319,2.028304,-0.460364,-8.375253,-0.618728,-2.540445,2.587361,-7.851136,8.527073,1.995026,8.934778,-8.790720,-0.943574,2.432720,-3.469738],[-0.340517,-8.159514,-3.902099,-6.086258,-7.654276,-2.567945,-2.544354,3.198889,-1.065406,2.133607,0.033961,-3.219377,-3.165691,-4.960484,6.238358],[1.391572,-1.376225,3.251711,4.678484,5.341792,-8.015374,-1.441802,8.541816,-5.956057,6.210015,1.540183,-6.519712,-5.115210,-7.927336,9.278368],[1.521488,-7.309236,-0.959442,-4.778611,6.674098,0.670004,-0.326684,1.208034,7.673053,9.557906,8.297588,3.380743,6.563880,-1.995348,-8.156132],[1.072936,5.515125,4.341756,2.737571,9.400472,4.984233,6.636789,-6.790884,5.492214,-8.681176,-5.886607,0.500051,5.731934,3.421158,9.777896]],[[4.238539,2.804973,-8.502884,-4.513994,0.530736,-2.619982,-0.714904,-7.850862,-9.003106,-1.105929,-0.365594,-9.453006,-8.427550,-0.586466,-0.165010],[-0.931281,-5.435650,-2.783168,-8.086473,9.105174,-9.465750,1.700200,0.865913,8.718648,7.411739,-6.215084,0.061443,-4.715139,-9.967548,4.205460],[-7.611457,5.431740,-5.898701,0.249337,-5.042893,-4.411484,-6.842519,-3.183143,3.586620,-9.330085,7.223071,-6.959345,7.573062,8.055270,-8.594836],[-2.262233,-8.788622,2.343266,7.557823,2.628801,3.438064,-7.527103,5.604659,3.742187,7.270557,-5.360286,-8.634044,4.742749,3.615672,-4.946244],[5.995597,-9.699184,-9.242877,-8.190832,-0.547236,2.965799,1.046961,7.251543,-2.464069,1.838492,-8.599221,3.836229,6.007257,4.619699,4.896507],[-9.995360,-5.964240,-7.816778,-8.195786,7.634285,-1.523249,1.386502,-2.605212,9.597200,3.409075,-6.589696,-7.079665,5.800593,-0.411402,-9.079566],[-4.040377,8.790738,1.090024,4.649266,-5.403330,-2.122429,9.120173,2.123691,-5.942487,8.227974,3.835233,-6.090261,5.433787,2.544021,-3.574972],[9.596768,-0.741131,7.907486,-8.327453,-9.143818,1.151222,8.156495,-5.304789,6.775228,5.203878,-7.392787,-4.005434,-0.115923,-7.793694,-8.507211],[2.795947,1.564231,-0.650120,9.643408,4.613726,8.788830,-2.582556,-3.798159,3.019845,-7.595397,-3.417888,-9.852705,3.134778,-6.670620,-6.281888],[-5.443885,-6.019613,-4.366341,-3.214947,0.876795,7.175821,3.803164,1.630566,-1.199019,5.345450,-4.692482,7.271694,-7.403569,9.489904,4.331461],[5.467259,-9.400432,2.085947,-9.924821,-4.070032,-5.027099,5.613682,-2.593722,2.748208,1.580849,4.574177,-6.323983,-1.206912,3.096039,1.045634],[-2.703743,-9.852602,-7.813165,2.363375,5.644916,-7.173116,8.717714,4.250124,-6.489670,-5.602140,9.360859,1.514495,-3.153618,8.683558,-2.152422],[-7.700336,7.098436,0.295603,0.229084,4.980973,-0.580097,-0.012722,6.877542,9.776694,-9.197981,0.202101,4.020298,3.932888,1.504929,2.840617],[9.156595,-5.728669,-4.479817,-1.490098,-8.873062,7.203071,3.265489,-8.145524,1.197802,-6.082534,1.930465,-1.765420,7.523394,-9.092368,-0.795601],[-6.894124,-9.015222,-7.787152,-5.912977,-6.359972,-7.732058,8.976949,2.541972,-5.949018,-5.105787,-4.196707,4.315245,-4.590608,-2.858417,7.785497]],[[7.382429,-4.158719,-8.451624,-1.175755,8.753191,6.319675,-5.474875,7.112162,-2.362616,1.389941,-5.338989,-0.606378,-0.556708,-7.694945,7.222557],[5.181729,0.213163,-8.655931,-8.522409,-6.727122,0.279205,-2.754150,2.814376,3.496913,7.622718,-4.056550,-3.609486,0.918954,7.384036,4.311325],[6.499127,1.572608,-2.228517,-9.614381,2.419607,-6.528468,-1.012436,-1.227175,-7.886806,0.872700,-7.483165,-1.744821,-9.868813,4.053065,2.891696],[3.828093,6.408040,-0.182170,-1.564780,1.720471,5.454265,8.993680,-0.094999,1.074181,7.357777,-9.252125,-8.730944,1.053205,7.018988,3.650243],[9.452388,6.810930,1.115584,3.095774,5.008941,9.562265,-8.304017,-4.257818,6.019631,-3.049556,6.193058,-9.401158,5.428532,-9.534185,4.335970],[4.873711,-0.389539,8.497750,-3.573155,-9.972409,8.028079,8.820661,-9.823498,-4.727522,4.988364,-0.869799,-4.005132,1.676904,-0.424016,-7.436764],[5.437375,3.341725,-5.722460,2.596021,9.995921,-8.692058,-3.472879,-2.501229,-2.536714,-6.241782,5.461973,-0.731167,4.396111,5.392504,1.818789],[9.090419,-9.755918,0.028731,-7.201452,4.447361,-5.846982,-2.081710,5.195689,7.905360,-8.331877,-2.139193,-4.747602,9.679137,-9.351954,-7.279770],[-4.935016,-2.710917,-3.795999,3.904141,-6.401420,-6.583467,1.617797,4.409113,2.149953,-5.891608,-1.471280,-3.635824,1.031943,8.908849,-1.868968],[1.532681,8.762848,6.205181,2.228527,-9.026639,-8.558257,-2.635668,-8.182777,-6.206208,-5.502597,9.169338,5.850418,-3.784882,7.020674,-0.679165],[9.392700,-9.682862,6.613717,-4.939831,-5.437504,8.026500,1.647579,-5.133870,5.050532,7.862025,9.825788,7.049822,-2.347247,4.662242,3.638878],[-5.794848,-2.367392,2.152281,-7.950500,-7.333944,1.982809,7.148197,-8.412224,-4.092085,1.986801,4.051376,-2.433296,7.828463,-8.260423,-6.743488],[8.899150,-6.651635,4.496661,8.822054,2.303925,-4.534380,6.817704,0.192478,-1.140451,-2.884574,-3.817342,-7.828266,-7.273518,0.457712,5.430685],[-9.001063,-1.354070,-4.151415,-5.558949,-5.655576,5.074812,-1.623899,-1.808364,-4.957090,6.461866,-5.758478,2.438774,-1.129050,8.352728,-2.676316],[7.633505,5.157083,-6.094426,3.016819,3.826856,-3.914359,7.934845,-6.669874,3.781309,-5.909039,3.317650,-5.044364,6.981644,-5.286912,-9.359331]],[[0.648557,1.962386,-6.803419,-5.482869,-7.764992,0.723848,7.550881,-7.053412,-5.449027,-3.132953,-8.265766,-7.747494,-0.909703,-0.672565,-1.302005],[-4.707841,-0.894157,-9.184541,0.517484,9.643506,-2.659183,-7.646060,7.538337,6.446867,-2.998919,-9.292068,8.337679,5.471706,-9.045368,-6.863004],[8.729786,3.389539,-8.083383,-1.181240,-7.910737,-4.608168,-3.183391,-4.846576,1.010582,5.176156,-6.363208,-3.197317,-6.229467,5.388925,6.234483],[8.249206,-6.800215,1.318037,-4.440605,-9.222385,9.174741,-0.436583,-9.637279,2.211743,-5.818145,6.136567,-3.308219,0.954081,-6.773950,7.225772],[-7.893715,-1.181633,1.594027,-0.549137,1.959855,4.635904,4.346793,-5.257759,-2.866478,8.174084,-3.307789,9.958964,-5.140220,-0.380997,-7.463260],[0.106502,-6.953119,7.470847,3.265455,-7.715609,0.945979,2.590804,8.179562,-0.708764,8.233051,-8.274856,-2.466481,-5.719476,-5.433091,3.985686],[-7.362319,-4.643317,-8.275800,0.484894,9.387903,-1.165213,4.726684,3.697691,9.958853,-3.160114,0.519231,6.158192,5.126723,-2.009198,-0.289334],[-0.534350,-2.138899,6.057971,-2.442418,-2.832258,-1.978887,-8.884791,-9.775794,-3.662747,0.977134,-9.149336,-5.033661,7.779333,8.825922,6.441264],[5.381454,9.339593,-9.991841,4.070778,8.359241,-5.663466,-5.876946,7.423582,-6.677421,7.121005,-2.284500,-7.818753,2.488962,-1.948273,-6.795323],[-8.401708,8.637540,4.314468,-5.916976,8.250477,6.224338,-4.090417,-0.679453,-0.848760,2.319400,5.548966,-7.186851,-1.496703,0.765389,-3.544935],[1.594004,7.497083,-2.796763,-0.449749,6.845491,-1.328230,-0.115172,2.583392,-0.994553,1.836837,4.388542,-8.847988,5.895497,3.392820,5.579991],[-7.918090,-5.556204,-4.481042,-8.241401,5.249826,-2.979130,-6.879160,-1.082965,8.907532,-4.179097,2.606508,2.135151,7.261390,-8.521105,0.976595],[-8.611718,-0.737063,-4.580055,-0.124980,-0.984036,-3.777890,9.803669,2.055737,-7.909008,3.232416,5.950037,-2.143852,-3.533934,6.866782,-2.621796],[-1.683755,-2.370302,7.287245,2.151901,-5.982855,-9.913575,-9.600782,8.795644,3.112561,6.019519,-8.916883,6.416207,1.656934,-3.984087,8.377355],[-1.162438,-0.885184,-5.889321,3.730991,8.253381,2.938241,-4.721611,3.766173,9.392182,-2.779568,8.867962,-0.010047,5.482730,-3.050569,-3.369559]],[[7.426690,-9.349269,-4.919510,6.007364,-3.798526,7.467667,-4.792955,-1.503257,3.887744,4.480068,-6.840264,1.362839,3.882774,-7.008552,-2.569411],[6.785106,3.694640,9.730309,2.676183,8.191432,7.231842,6.547500,0.933038,-5.828334,-3.572214,-0.942520,-5.661028,7.551800,-7.696404,-3.239571],[-9.109431,-6.496909,1.554087,4.166766,2.968070,-9.378895,1.472188,-7.361476,9.085072,-4.377367,-1.574311,-1.670498,-5.894683,9.975159,-6.991499],[1.651145,7.718123,-2.189163,-4.406765,2.547922,7.538541,-4.131132,-9.491185,5.086826,7.034536,8.339929,-2.190013,7.847565,9.480569,1.604927],[-6.132396,-2.849828,4.026922,-1.081495,3.301891,3.452919,6.399984,3.704079,-5.466436,-1.219156,-7.779797,-8.271491,0.313626,3.757677,-7.525607],[-2.712663,-6.259409,-7.081088,-7.265629,0.983381,0.475759,-6.929980,-4.261064,-8.950143,-2.559971,7.085646,-8.403537,0.763773,1.647369,-9.748118],[7.667292,-2.105541,9.588360,1.656545,7.136677,7.064083,7.104117,6.052805,-1.507224,6.370058,-1.835352,8.603394,-4.068147,0.269415,-8.507539],[2.571931,-2.997580,6.156866,-9.882542,0.733676,4.042691,-2.246763,-0.775391,-2.615893,8.357211,6.110892,-2.395991,-3.115932,7.121966,-6.302769],[3.504087,-5.471302,7.220564,-6.762712,-8.081227,7.615417,-0.730344,7.523524,-7.426427,5.902861,3.829455,3.279379,-0.363179,-4.338301,2.265943],[8.677519,-3.107106,0.874186,6.289155,9.066707,8.431985,8.849819,2.377191,1.521988,-3.308215,3.412027,3.256424,-4.101716,6.519632,-2.155258],[5.401670,3.456665,2.919871,-7.136651,-9.389268,-0.914104,-3.319079,-9.984185,-7.219506,2.732923,-0.235951,-2.892495,-4.185739,2.841530,7.029094],[-2.483466,6.085946,-2.970136,-1.645934,7.952663,7.276427,3.640409,9.442000,6.536133,9.893967,2.057672,2.327693,8.034743,-0.315949,1.768245],[-8.579820,-3.835150,-0.840479,-3.099431,9.874669,5.786551,-6.146741,5.952383,-2.728490,3.228640,6.827538,-1.427821,6.917214,-7.599366,-2.612815],[9.304379,-7.056540,7.657326,2.779512,2.450283,8.377799,5.529463,4.908822,-5.325068,8.700978,4.977729,-6.856858,2.310151,-3.743197,4.420666],[-8.282615,4.027377,-2.492246,6.731835,0.019877,6.869933,8.903659,-2.971758,4.027662,1.620625,-1.423237,3.749442,-6.344478,-4.863093,7.092438]]], dtype = "float32")#candidate|6005|(7, 15, 15)|const|float32
uop_6006 = relay.acosh(const_6005.astype('float32')) # shape=(7, 15, 15)
func_2525_call = mod.get_global_var('func_2525')
func_2527_call = mutated_mod.get_global_var('func_2527')
call_6011 = func_2525_call()
call_6012 = func_2525_call()
output = relay.Tuple([uop_6006,call_6011,])
output2 = relay.Tuple([uop_6006,call_6012,])
func_6017 = relay.Function([], output)
mod['func_6017'] = func_6017
mod = relay.transform.InferType()(mod)
output = func_6017()
func_6018 = relay.Function([], output)
mutated_mod['func_6018'] = func_6018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mod.get_global_var('func_1913')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_6044 = relay.TupleGetItem(func_1913_call(), 0)
call_6045 = relay.TupleGetItem(func_1914_call(), 0)
output = call_6044
output2 = call_6045
func_6047 = relay.Function([], output)
mod['func_6047'] = func_6047
mod = relay.transform.InferType()(mod)
mutated_mod['func_6047'] = func_6047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6047_call = mutated_mod.get_global_var('func_6047')
call_6048 = func_6047_call()
output = call_6048
func_6049 = relay.Function([], output)
mutated_mod['func_6049'] = func_6049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1080_call = mod.get_global_var('func_1080')
func_1081_call = mutated_mod.get_global_var('func_1081')
call_6055 = func_1080_call()
call_6056 = func_1080_call()
func_2061_call = mod.get_global_var('func_2061')
func_2063_call = mutated_mod.get_global_var('func_2063')
call_6057 = func_2061_call()
call_6058 = func_2061_call()
output = relay.Tuple([call_6055,call_6057,])
output2 = relay.Tuple([call_6056,call_6058,])
func_6060 = relay.Function([], output)
mod['func_6060'] = func_6060
mod = relay.transform.InferType()(mod)
mutated_mod['func_6060'] = func_6060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6060_call = mutated_mod.get_global_var('func_6060')
call_6061 = func_6060_call()
output = call_6061
func_6062 = relay.Function([], output)
mutated_mod['func_6062'] = func_6062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3879_call = mod.get_global_var('func_3879')
func_3880_call = mutated_mod.get_global_var('func_3880')
call_6063 = func_3879_call()
call_6064 = func_3879_call()
func_2525_call = mod.get_global_var('func_2525')
func_2527_call = mutated_mod.get_global_var('func_2527')
call_6070 = func_2525_call()
call_6071 = func_2525_call()
func_4346_call = mod.get_global_var('func_4346')
func_4349_call = mutated_mod.get_global_var('func_4349')
const_6073 = relay.const([[7.029928,-9.188562],[-1.292699,4.736035],[-0.449910,-8.967232],[-6.769517,2.862314],[4.224010,0.197315],[6.368386,8.408306],[0.103584,4.957627],[-3.045183,6.491064],[-4.078692,-1.855457],[-4.621704,1.121992],[-9.927930,3.572991],[1.763978,8.843817],[5.323625,-4.212441],[6.110826,7.883146],[-6.321477,-4.522815],[5.773099,-2.467169],[1.125404,7.711803],[-4.892093,-8.611315],[-3.318280,1.940451],[4.985517,9.320748],[4.394552,7.909452],[5.667629,-4.949113],[-9.031469,-0.001926],[-9.854347,5.566839],[9.687455,-3.676459],[-6.560729,-2.713148],[-4.294319,-2.235386],[-4.452795,-2.391329],[7.081980,8.042056],[-4.668502,-1.070071],[-8.266889,2.589368],[-7.955250,5.011823],[8.855766,5.499998],[-1.121628,-9.399445],[-5.643817,-8.317094],[-7.176780,-7.041618],[1.397701,-2.079783],[2.239551,-1.682065],[3.225233,6.632426],[-0.315300,7.476822],[-6.880764,2.838648],[-6.233891,4.507424],[-0.767642,-9.378136],[0.991753,-3.854449],[-8.408589,-1.132536],[-7.956164,2.591042],[-9.187350,3.709794],[2.776238,-4.296346],[8.074966,9.017094],[-1.525092,-5.335879],[-0.232726,2.904713],[-0.681954,-4.037406],[0.662785,-4.276460],[0.043190,8.121061],[-5.290981,7.764431],[-5.357364,8.184964],[5.544396,5.314181],[-7.232689,4.565611],[-9.297313,-6.878696],[-9.393889,6.015978],[1.641573,7.934438],[-6.703552,9.138863],[4.401493,-2.209622],[-7.224866,-8.633507],[-5.485414,7.923812],[1.354276,-5.975439],[-8.821018,-4.674956],[6.539105,-7.322166],[-2.730893,-2.121727],[-0.901257,3.334546],[-8.304749,4.312048],[-8.829571,-0.808598],[-5.450691,1.919814],[-5.364268,2.529439],[-0.992180,-2.014779],[-2.312327,-9.911204],[-3.719750,1.877814],[-9.548681,0.858529],[-7.744032,-6.271274],[-4.437015,-1.840948],[-5.248205,-0.527110],[8.235358,2.264548],[-5.614132,1.394860],[-3.127155,4.903951],[-5.088616,-2.455134],[1.163394,0.713533],[-9.478043,-5.457425],[5.981136,1.934791],[-8.841265,-2.433269],[-3.895170,5.141466],[9.291126,7.726617],[0.132645,6.071724],[8.850786,-3.408159],[6.941089,-5.891596],[3.132120,-7.200317],[8.756986,6.660552],[9.205665,4.558788],[9.716212,-7.953505],[-0.438805,0.128636],[-7.900896,9.734573],[-9.306346,2.273690],[-9.193266,1.673439],[-9.405656,-5.010482],[-6.647457,-8.440038],[0.966381,8.085842],[-1.164428,-7.800726],[7.579256,-1.121141],[-7.062601,5.720927],[-2.041659,-9.725104],[-0.421672,-2.713892],[6.964335,0.915003],[-2.375217,9.041113],[9.342411,8.874841],[2.106081,-3.896706],[6.911207,-1.151974],[5.236630,-9.668344],[-2.252436,-2.330145],[-9.592996,-9.521008],[1.389628,2.290340],[5.041265,5.738174],[2.437399,-8.710182],[-1.796259,6.961475],[-9.994990,7.958084],[6.128790,9.816555],[-0.384812,6.140386],[-4.528666,-6.053044],[2.042319,-4.983845],[9.118555,2.230774],[-6.208380,8.434961],[2.635958,-6.869217],[-8.716472,5.767918],[1.315896,-0.345870],[-3.198029,-9.171993],[1.475590,-0.625632],[4.473131,2.509624],[-5.752674,0.596055],[-5.150334,-7.944569],[-8.832833,8.533768],[-8.424939,-8.507576],[7.785213,-2.629724],[-4.199456,2.458613],[5.118750,-7.073235],[-4.858883,6.269054],[1.620661,7.035766],[8.874903,2.079452],[-2.226998,1.228832],[6.194542,-4.904090],[-3.938265,-5.720646],[3.573427,-2.099721],[8.573949,7.516397],[-1.883000,-6.031354],[-5.070537,0.804590],[7.416641,3.086224],[-1.747199,3.279827],[-1.284004,-3.581987],[-1.840251,-1.834792],[-9.965641,-7.444728],[6.330639,5.403095],[9.361715,5.803183],[3.929162,9.213688],[9.046870,-8.631602],[8.422389,7.660128],[9.337103,-6.669408],[-1.887238,-7.466433],[5.305458,-4.871470],[-9.386794,-8.453902],[-4.345725,8.187023],[4.201966,-5.602236],[1.351215,-8.702885],[-2.351570,9.746731],[6.836253,2.515898],[-3.876691,9.345402],[6.312112,-2.533307],[0.696008,4.296405],[8.797304,-6.857077],[3.849340,8.351721],[3.625147,-2.333453],[-6.904804,-4.112030],[9.985022,9.402057],[2.012485,-7.374053],[4.436676,-2.140907],[8.884046,-6.578001],[0.121213,7.991237],[0.995965,1.354538],[-3.860419,4.767401],[9.337663,8.693922],[1.140672,-9.546025],[5.291792,6.790284],[-5.431636,0.178633],[4.483570,-3.146914],[-8.488697,-0.400738],[-1.192134,0.648878],[7.629302,3.655382],[-9.375899,1.806733],[-4.838357,-9.381353],[-8.624189,-2.078899],[3.927416,2.758049],[2.255685,2.888095],[1.317516,9.356562],[-9.771762,6.136008],[3.961612,-6.213628],[9.766013,-4.900842],[-8.507976,4.263323],[-3.674626,5.565838],[8.053248,8.277043],[-3.366272,5.170893],[-1.534873,5.108407],[3.407681,-6.156729],[-8.297671,-6.813217],[-7.968991,3.479627],[9.089709,-3.744208],[-4.063410,8.892721],[-7.150171,-6.219672],[-7.426747,-2.832935],[-9.347578,4.192296],[-0.780641,0.915698],[-5.572378,-8.114439],[-9.469452,4.513553],[-7.954372,2.906735],[3.550208,8.363802],[0.418528,-9.600040],[4.659955,-6.178414],[9.327023,1.163618],[2.404384,-3.289922],[-8.547674,4.299097],[-0.088792,-9.625527],[-7.275616,0.424770],[-0.883705,5.457551],[-4.920656,7.106928],[-6.878992,2.393361],[1.224683,-2.347202],[1.412392,0.806820],[7.197322,-8.712265],[1.534477,5.671164],[6.996076,-8.925476],[9.758331,4.239902],[2.068608,8.308434],[3.835462,9.405263],[0.887264,7.053713],[-7.287578,-2.011922],[5.376725,3.769086],[7.719197,-5.096515],[2.159200,-5.799177],[-2.519641,-0.800511],[9.252139,-9.413676],[5.150661,8.236225],[2.962977,4.387822],[4.111941,9.526244],[0.584900,-7.452197],[0.098954,0.978706],[9.220423,9.505070],[7.113272,7.708575],[7.049441,5.321717],[-8.451227,0.701115],[-1.442462,6.319317],[-4.658267,-2.932335],[-5.852157,-1.232979],[-3.815079,-7.446714],[-6.725007,2.538887],[-8.199911,-3.071331],[-8.297609,-1.951646],[-2.202251,-6.444936],[-3.261245,0.226598],[7.437116,-6.493296],[-2.405983,8.347392],[-7.617869,-9.384514],[-4.089622,0.095364],[-4.295812,-2.234252],[5.827012,1.421655],[3.471871,-4.109224],[-8.517263,-9.829071],[-7.448719,6.533527],[-7.223681,9.301481],[-7.373236,4.385417],[2.018304,1.478772],[-9.691728,8.280483],[-6.598752,5.193204],[-1.612774,-4.600195],[2.045381,-1.065300],[5.232565,-1.889544],[0.524458,4.612798],[2.002642,-7.054790],[6.043821,2.902826],[4.416333,2.393489],[2.750479,6.687238],[2.186080,-2.311971],[5.363137,-6.903810],[-9.971325,-4.318630],[-1.326625,-4.706540],[-0.784219,-7.649728],[-5.973611,0.986285],[-5.833627,-1.205681],[9.600873,-9.873553],[3.661906,-0.815986],[5.792854,8.053464],[9.982473,3.610885],[9.115080,-2.348175],[-0.838652,4.293415],[-5.038885,6.038071],[-9.129126,-5.806989],[6.702682,-5.569799],[-3.622512,5.674966],[8.988488,9.033851],[-3.133055,-8.587850],[-3.457286,2.206165],[6.685018,-0.672860],[7.622834,7.700488],[5.800299,-7.286017],[-4.996448,7.257745],[8.410401,-6.013760],[1.640370,8.549674],[1.086069,-4.250062],[-8.921204,-7.178602],[-4.345797,1.165300],[-3.125843,1.284897],[1.818172,1.179721],[-7.484792,-8.232921],[4.900263,-3.043085],[-6.329153,8.557325],[3.283320,-4.804615],[3.295411,-4.578762],[3.134438,-1.749545],[-4.795096,9.375802],[8.814509,8.087717],[1.357853,7.383088],[-4.265408,3.315670],[2.033140,-4.123442],[-6.575630,3.638104],[-0.258936,-8.197040],[4.144658,5.096473],[-0.066980,0.377802],[4.856321,-8.568586],[-3.816417,-1.848110],[5.775859,-8.310243],[-5.346657,-4.455676],[8.223771,-7.584527],[6.143003,6.644737],[5.190772,-3.866238],[8.511560,5.017371],[-2.527413,4.726410],[1.172784,0.113555],[0.742110,-4.902500],[6.342818,1.735891],[-0.948807,-2.088497],[-6.620926,-8.454582],[-6.939680,6.423328],[9.781678,2.578673],[-3.203785,-1.508571],[-6.638665,1.029942],[5.411181,8.618126],[-2.992327,2.193279],[-6.866970,-7.715287],[1.236785,0.460177],[9.991455,5.229481],[7.229205,-3.278527],[2.210585,-3.802926],[-1.351688,-9.999461],[2.644313,-6.577028],[-1.978953,-7.137084],[7.057927,1.822842],[6.707821,1.449446],[4.969027,7.507440],[0.757733,7.960617],[1.874363,-1.385549],[7.479522,8.933589],[-4.035092,-5.786911],[-7.593487,8.329182],[8.537470,-4.192060],[1.658232,4.034420],[7.001868,-6.861281],[-8.235889,4.436418],[4.211391,8.685853],[-0.066696,0.854640],[2.662620,4.479981],[-8.180238,9.371028],[1.822322,-4.552211],[6.500609,-7.438869],[4.319198,2.789236],[-1.931575,0.222040],[-0.961375,-7.880540],[0.475916,8.699167],[4.846722,-2.155235],[-9.670170,5.186566],[-4.644533,-1.319646],[2.602400,-7.681790],[5.651716,-7.031065],[-1.759945,7.432174],[-6.305233,-9.615651],[7.481921,-8.355243],[-9.774476,-9.977611],[7.330839,4.056012],[-7.051005,5.895495],[-5.121363,-7.981689],[-4.070715,3.444741],[-0.790487,6.783386],[-7.160442,-8.073182],[-5.118574,-9.052497],[-5.875352,2.941508],[-5.890778,3.092183],[-7.685317,-1.908122],[-6.996218,6.189726],[5.916959,1.806412],[3.471759,-4.592540],[-4.235015,-1.114140],[-7.348243,-3.915667],[3.269113,-4.361950],[-3.171438,-7.699979],[-7.255240,2.751951],[0.954298,1.925755],[0.795483,-7.800239],[-2.997299,-5.072017],[-1.991454,5.021035],[8.405004,5.502698],[5.250626,-5.308256],[2.508001,-1.276484],[8.240521,-2.215228],[-4.021107,0.553486],[-8.778017,9.896890],[-6.121981,-1.856673],[-3.591582,4.096124],[8.869135,-1.549091],[-7.584092,-2.709624],[-9.737916,-7.240956],[-4.354830,-1.332553],[-5.983511,-6.326907],[-2.449794,8.456189],[5.631021,3.754102],[3.903191,6.238118],[5.801567,3.219558],[-9.376142,8.654880],[5.051728,-0.619642],[-6.373070,-2.291317],[-4.706743,0.875110],[-7.175680,1.265589],[-1.010460,9.587931],[-6.157210,-4.571777],[4.408880,4.370205],[1.531864,-4.804720],[-6.207029,-2.317933],[1.826016,-3.560057],[3.107896,-4.366731],[-2.627301,6.190150],[-6.679430,6.909564],[8.580037,-7.763203],[2.837462,-1.496917],[-6.896566,4.308522],[9.431583,9.111549],[2.704874,-1.714535],[-0.234407,-6.960151],[7.044183,5.986156],[8.075652,-0.345798],[8.009503,9.585224],[-4.224884,0.875694],[-8.508480,-8.711766],[2.987593,-6.574535],[2.331340,1.378411],[-5.093494,-6.587830],[-0.004393,5.637965],[-6.071874,-8.364205],[5.091726,1.006300],[-0.523702,-5.601005],[0.124943,-0.375606],[0.841837,7.095208],[-6.126972,-3.006315],[0.570533,-5.616135],[-3.105855,7.045936],[5.447719,-0.388268],[5.165611,-1.955111]], dtype = "float64")#candidate|6073|(468, 2)|const|float64
call_6072 = relay.TupleGetItem(func_4346_call(relay.reshape(const_6073.astype('float64'), [13, 6, 12])), 0)
call_6074 = relay.TupleGetItem(func_4349_call(relay.reshape(const_6073.astype('float64'), [13, 6, 12])), 0)
output = relay.Tuple([call_6063,call_6070,call_6072,const_6073,])
output2 = relay.Tuple([call_6064,call_6071,call_6074,const_6073,])
func_6077 = relay.Function([], output)
mod['func_6077'] = func_6077
mod = relay.transform.InferType()(mod)
mutated_mod['func_6077'] = func_6077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6077_call = mutated_mod.get_global_var('func_6077')
call_6078 = func_6077_call()
output = call_6078
func_6079 = relay.Function([], output)
mutated_mod['func_6079'] = func_6079
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6107 = relay.var("var_6107", dtype = "float64", shape = (5, 8, 4))#candidate|6107|(5, 8, 4)|var|float64
uop_6108 = relay.tan(var_6107.astype('float64')) # shape=(5, 8, 4)
output = relay.Tuple([uop_6108,])
output2 = relay.Tuple([uop_6108,])
func_6120 = relay.Function([var_6107,], output)
mod['func_6120'] = func_6120
mod = relay.transform.InferType()(mod)
mutated_mod['func_6120'] = func_6120
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6121 = relay.var("var_6121", dtype = "float64", shape = (5, 8, 4))#candidate|6121|(5, 8, 4)|var|float64
func_6120_call = mutated_mod.get_global_var('func_6120')
call_6122 = func_6120_call(var_6121)
output = call_6122
func_6123 = relay.Function([var_6121], output)
mutated_mod['func_6123'] = func_6123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5959_call = mod.get_global_var('func_5959')
func_5961_call = mutated_mod.get_global_var('func_5961')
call_6144 = func_5959_call()
call_6145 = func_5959_call()
output = call_6144
output2 = call_6145
func_6155 = relay.Function([], output)
mod['func_6155'] = func_6155
mod = relay.transform.InferType()(mod)
output = func_6155()
func_6156 = relay.Function([], output)
mutated_mod['func_6156'] = func_6156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_6238 = relay.TupleGetItem(func_206_call(), 0)
call_6239 = relay.TupleGetItem(func_207_call(), 0)
output = relay.Tuple([call_6238,])
output2 = relay.Tuple([call_6239,])
func_6246 = relay.Function([], output)
mod['func_6246'] = func_6246
mod = relay.transform.InferType()(mod)
mutated_mod['func_6246'] = func_6246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6246_call = mutated_mod.get_global_var('func_6246')
call_6247 = func_6246_call()
output = call_6247
func_6248 = relay.Function([], output)
mutated_mod['func_6248'] = func_6248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1117_call = mod.get_global_var('func_1117')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_6252 = relay.TupleGetItem(func_1117_call(), 0)
call_6253 = relay.TupleGetItem(func_1118_call(), 0)
var_6287 = relay.var("var_6287", dtype = "bool", shape = (5, 11, 8))#candidate|6287|(5, 11, 8)|var|bool
bop_6288 = relay.floor_mod(call_6252.astype('float64'), relay.reshape(var_6287.astype('float64'), relay.shape_of(call_6252))) # shape=(5, 11, 8)
bop_6291 = relay.floor_mod(call_6253.astype('float64'), relay.reshape(var_6287.astype('float64'), relay.shape_of(call_6253))) # shape=(5, 11, 8)
output = relay.Tuple([bop_6288,])
output2 = relay.Tuple([bop_6291,])
func_6297 = relay.Function([var_6287,], output)
mod['func_6297'] = func_6297
mod = relay.transform.InferType()(mod)
mutated_mod['func_6297'] = func_6297
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6298 = relay.var("var_6298", dtype = "bool", shape = (5, 11, 8))#candidate|6298|(5, 11, 8)|var|bool
func_6297_call = mutated_mod.get_global_var('func_6297')
call_6299 = func_6297_call(var_6298)
output = call_6299
func_6300 = relay.Function([var_6298], output)
mutated_mod['func_6300'] = func_6300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_6306 = func_815_call()
call_6307 = func_815_call()
output = call_6306
output2 = call_6307
func_6315 = relay.Function([], output)
mod['func_6315'] = func_6315
mod = relay.transform.InferType()(mod)
mutated_mod['func_6315'] = func_6315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6315_call = mutated_mod.get_global_var('func_6315')
call_6316 = func_6315_call()
output = call_6316
func_6317 = relay.Function([], output)
mutated_mod['func_6317'] = func_6317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5316_call = mod.get_global_var('func_5316')
func_5318_call = mutated_mod.get_global_var('func_5318')
call_6318 = relay.TupleGetItem(func_5316_call(), 0)
call_6319 = relay.TupleGetItem(func_5318_call(), 0)
output = call_6318
output2 = call_6319
func_6346 = relay.Function([], output)
mod['func_6346'] = func_6346
mod = relay.transform.InferType()(mod)
output = func_6346()
func_6347 = relay.Function([], output)
mutated_mod['func_6347'] = func_6347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5662_call = mod.get_global_var('func_5662')
func_5664_call = mutated_mod.get_global_var('func_5664')
call_6418 = func_5662_call()
call_6419 = func_5662_call()
func_1985_call = mod.get_global_var('func_1985')
func_1988_call = mutated_mod.get_global_var('func_1988')
const_6424 = relay.const(4.639647, dtype = "float64")#candidate|6424|()|const|float64
var_6425 = relay.var("var_6425", dtype = "float64", shape = (2310,))#candidate|6425|(2310,)|var|float64
call_6423 = relay.TupleGetItem(func_1985_call(relay.reshape(const_6424.astype('float64'), []), relay.reshape(var_6425.astype('float64'), [15, 11, 14]), ), 0)
call_6426 = relay.TupleGetItem(func_1988_call(relay.reshape(const_6424.astype('float64'), []), relay.reshape(var_6425.astype('float64'), [15, 11, 14]), ), 0)
uop_6449 = relay.log2(call_6423.astype('float64')) # shape=(15, 11, 14)
uop_6451 = relay.log2(call_6426.astype('float64')) # shape=(15, 11, 14)
func_2128_call = mod.get_global_var('func_2128')
func_2130_call = mutated_mod.get_global_var('func_2130')
call_6454 = relay.TupleGetItem(func_2128_call(), 0)
call_6455 = relay.TupleGetItem(func_2130_call(), 0)
uop_6456 = relay.sin(uop_6449.astype('float32')) # shape=(15, 11, 14)
uop_6458 = relay.sin(uop_6451.astype('float32')) # shape=(15, 11, 14)
output = relay.Tuple([call_6418,const_6424,var_6425,call_6454,uop_6456,])
output2 = relay.Tuple([call_6419,const_6424,var_6425,call_6455,uop_6458,])
func_6480 = relay.Function([var_6425,], output)
mod['func_6480'] = func_6480
mod = relay.transform.InferType()(mod)
mutated_mod['func_6480'] = func_6480
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6481 = relay.var("var_6481", dtype = "float64", shape = (2310,))#candidate|6481|(2310,)|var|float64
func_6480_call = mutated_mod.get_global_var('func_6480')
call_6482 = func_6480_call(var_6481)
output = call_6482
func_6483 = relay.Function([var_6481], output)
mutated_mod['func_6483'] = func_6483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4041_call = mod.get_global_var('func_4041')
func_4043_call = mutated_mod.get_global_var('func_4043')
call_6491 = relay.TupleGetItem(func_4041_call(), 0)
call_6492 = relay.TupleGetItem(func_4043_call(), 0)
output = call_6491
output2 = call_6492
func_6499 = relay.Function([], output)
mod['func_6499'] = func_6499
mod = relay.transform.InferType()(mod)
mutated_mod['func_6499'] = func_6499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6499_call = mutated_mod.get_global_var('func_6499')
call_6500 = func_6499_call()
output = call_6500
func_6501 = relay.Function([], output)
mutated_mod['func_6501'] = func_6501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_853_call = mod.get_global_var('func_853')
func_854_call = mutated_mod.get_global_var('func_854')
call_6519 = func_853_call()
call_6520 = func_853_call()
output = relay.Tuple([call_6519,])
output2 = relay.Tuple([call_6520,])
func_6523 = relay.Function([], output)
mod['func_6523'] = func_6523
mod = relay.transform.InferType()(mod)
mutated_mod['func_6523'] = func_6523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6523_call = mutated_mod.get_global_var('func_6523')
call_6524 = func_6523_call()
output = call_6524
func_6525 = relay.Function([], output)
mutated_mod['func_6525'] = func_6525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_6590 = relay.TupleGetItem(func_2499_call(), 0)
call_6591 = relay.TupleGetItem(func_2500_call(), 0)
func_6523_call = mod.get_global_var('func_6523')
func_6525_call = mutated_mod.get_global_var('func_6525')
call_6601 = relay.TupleGetItem(func_6523_call(), 0)
call_6602 = relay.TupleGetItem(func_6525_call(), 0)
output = relay.Tuple([call_6590,call_6601,])
output2 = relay.Tuple([call_6591,call_6602,])
func_6604 = relay.Function([], output)
mod['func_6604'] = func_6604
mod = relay.transform.InferType()(mod)
output = func_6604()
func_6605 = relay.Function([], output)
mutated_mod['func_6605'] = func_6605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_340_call = mod.get_global_var('func_340')
func_342_call = mutated_mod.get_global_var('func_342')
call_6619 = func_340_call()
call_6620 = func_340_call()
func_5741_call = mod.get_global_var('func_5741')
func_5743_call = mutated_mod.get_global_var('func_5743')
call_6629 = relay.TupleGetItem(func_5741_call(), 2)
call_6630 = relay.TupleGetItem(func_5743_call(), 2)
output = relay.Tuple([call_6619,call_6629,])
output2 = relay.Tuple([call_6620,call_6630,])
func_6651 = relay.Function([], output)
mod['func_6651'] = func_6651
mod = relay.transform.InferType()(mod)
output = func_6651()
func_6652 = relay.Function([], output)
mutated_mod['func_6652'] = func_6652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mod.get_global_var('func_206')
func_207_call = mutated_mod.get_global_var('func_207')
call_6656 = relay.TupleGetItem(func_206_call(), 0)
call_6657 = relay.TupleGetItem(func_207_call(), 0)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_6676 = relay.TupleGetItem(func_1416_call(), 1)
call_6677 = relay.TupleGetItem(func_1417_call(), 1)
func_815_call = mod.get_global_var('func_815')
func_817_call = mutated_mod.get_global_var('func_817')
call_6685 = func_815_call()
call_6686 = func_815_call()
func_3363_call = mod.get_global_var('func_3363')
func_3365_call = mutated_mod.get_global_var('func_3365')
var_6698 = relay.var("var_6698", dtype = "float32", shape = (780,))#candidate|6698|(780,)|var|float32
call_6697 = relay.TupleGetItem(func_3363_call(relay.reshape(var_6698.astype('float32'), [13, 10, 6])), 1)
call_6699 = relay.TupleGetItem(func_3365_call(relay.reshape(var_6698.astype('float32'), [13, 10, 6])), 1)
output = relay.Tuple([call_6656,call_6676,call_6685,call_6697,var_6698,])
output2 = relay.Tuple([call_6657,call_6677,call_6686,call_6699,var_6698,])
func_6706 = relay.Function([var_6698,], output)
mod['func_6706'] = func_6706
mod = relay.transform.InferType()(mod)
var_6707 = relay.var("var_6707", dtype = "float32", shape = (780,))#candidate|6707|(780,)|var|float32
output = func_6706(var_6707)
func_6708 = relay.Function([var_6707], output)
mutated_mod['func_6708'] = func_6708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mod.get_global_var('func_1913')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_6719 = relay.TupleGetItem(func_1913_call(), 0)
call_6720 = relay.TupleGetItem(func_1914_call(), 0)
output = call_6719
output2 = call_6720
func_6721 = relay.Function([], output)
mod['func_6721'] = func_6721
mod = relay.transform.InferType()(mod)
mutated_mod['func_6721'] = func_6721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6721_call = mutated_mod.get_global_var('func_6721')
call_6722 = func_6721_call()
output = call_6722
func_6723 = relay.Function([], output)
mutated_mod['func_6723'] = func_6723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6077_call = mod.get_global_var('func_6077')
func_6079_call = mutated_mod.get_global_var('func_6079')
call_6780 = relay.TupleGetItem(func_6077_call(), 1)
call_6781 = relay.TupleGetItem(func_6079_call(), 1)
output = relay.Tuple([call_6780,])
output2 = relay.Tuple([call_6781,])
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
func_2525_call = mod.get_global_var('func_2525')
func_2527_call = mutated_mod.get_global_var('func_2527')
call_6878 = func_2525_call()
call_6879 = func_2525_call()
uop_6886 = relay.tan(call_6878.astype('float32')) # shape=(13, 8, 8)
uop_6888 = relay.tan(call_6879.astype('float32')) # shape=(13, 8, 8)
func_655_call = mod.get_global_var('func_655')
func_657_call = mutated_mod.get_global_var('func_657')
call_6893 = func_655_call()
call_6894 = func_655_call()
bop_6895 = relay.less_equal(uop_6886.astype('bool'), relay.reshape(call_6878.astype('bool'), relay.shape_of(uop_6886))) # shape=(13, 8, 8)
bop_6898 = relay.less_equal(uop_6888.astype('bool'), relay.reshape(call_6879.astype('bool'), relay.shape_of(uop_6888))) # shape=(13, 8, 8)
func_1117_call = mod.get_global_var('func_1117')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_6904 = relay.TupleGetItem(func_1117_call(), 0)
call_6905 = relay.TupleGetItem(func_1118_call(), 0)
output = relay.Tuple([call_6893,bop_6895,call_6904,])
output2 = relay.Tuple([call_6894,bop_6898,call_6905,])
func_6924 = relay.Function([], output)
mod['func_6924'] = func_6924
mod = relay.transform.InferType()(mod)
mutated_mod['func_6924'] = func_6924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6924_call = mutated_mod.get_global_var('func_6924')
call_6925 = func_6924_call()
output = call_6925
func_6926 = relay.Function([], output)
mutated_mod['func_6926'] = func_6926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_942_call = mod.get_global_var('func_942')
func_944_call = mutated_mod.get_global_var('func_944')
call_6984 = relay.TupleGetItem(func_942_call(), 1)
call_6985 = relay.TupleGetItem(func_944_call(), 1)
func_923_call = mod.get_global_var('func_923')
func_925_call = mutated_mod.get_global_var('func_925')
call_6990 = relay.TupleGetItem(func_923_call(), 0)
call_6991 = relay.TupleGetItem(func_925_call(), 0)
func_4231_call = mod.get_global_var('func_4231')
func_4232_call = mutated_mod.get_global_var('func_4232')
call_6997 = relay.TupleGetItem(func_4231_call(), 0)
call_6998 = relay.TupleGetItem(func_4232_call(), 0)
output = relay.Tuple([call_6984,call_6990,call_6997,])
output2 = relay.Tuple([call_6985,call_6991,call_6998,])
func_7002 = relay.Function([], output)
mod['func_7002'] = func_7002
mod = relay.transform.InferType()(mod)
mutated_mod['func_7002'] = func_7002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7002_call = mutated_mod.get_global_var('func_7002')
call_7003 = func_7002_call()
output = call_7003
func_7004 = relay.Function([], output)
mutated_mod['func_7004'] = func_7004
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7026 = relay.const([[[2,-2,2,7,5,-7,-4,-3,-8,8,-6,-1,-10,7,-4,1],[6,2,3,-10,-1,-7,3,5,6,7,6,8,-3,-5,8,5],[-9,-2,4,-3,10,-4,-9,-6,-2,6,3,5,2,2,-4,-4],[4,7,7,-5,-7,1,7,10,10,-9,-3,8,-2,5,-9,-1],[4,-1,8,-7,-6,-1,-6,6,1,1,-8,9,-1,-10,-3,3],[8,8,1,-3,6,4,6,-9,3,-3,9,5,-6,8,5,-7],[-5,-1,2,7,-9,-9,-1,4,-8,-7,8,-5,-6,-4,-6,5]],[[5,2,-1,5,-8,-5,-3,-4,-5,-8,-4,7,-9,4,1,-1],[-7,-6,-9,-10,-5,7,5,1,-4,-3,3,10,-9,1,4,-8],[2,3,5,2,8,8,-3,-3,9,7,6,-5,-2,6,-8,-10],[8,-4,7,-5,-7,10,3,7,1,-3,3,-3,6,-4,-6,5],[-8,-9,4,3,6,-1,9,10,-4,-1,2,-2,5,-3,10,5],[6,6,7,-1,-3,1,-10,5,3,-9,-10,-5,8,-6,-7,-8],[-6,-3,4,-5,4,-2,-6,-8,-1,-5,-7,7,-10,4,7,-10]],[[-8,5,9,-10,7,-9,7,3,-4,2,-1,-9,-4,-10,-6,-2],[-7,6,-1,9,8,-3,5,6,6,-3,7,-2,4,9,-4,4],[-2,-7,9,-10,-6,-6,1,-10,-10,-6,4,7,9,8,1,-5],[4,-5,-8,2,8,-4,-9,-7,-9,7,10,1,-2,-5,1,-5],[1,-8,4,4,-5,2,5,5,2,-9,-6,6,-9,2,-10,-5],[-8,2,2,-6,4,-2,-7,7,9,-6,6,4,2,7,4,4],[6,5,-2,6,-9,7,7,9,-7,10,6,9,9,-1,10,6]],[[9,-4,2,-7,10,9,7,1,3,-7,7,-7,4,1,1,-7],[-9,-3,1,-4,-5,8,10,-4,-1,2,-1,-4,6,6,-5,10],[-6,-6,7,9,4,-2,7,7,-10,-7,5,3,-9,1,-6,9],[-7,2,-9,-4,8,-5,-5,-4,1,-4,-3,10,-8,7,3,7],[-4,-2,9,4,-3,2,-3,-10,8,-1,-3,-4,-1,8,-8,3],[-3,3,-10,-9,7,-10,-10,5,6,-10,8,-3,-8,4,-5,7],[10,8,-8,5,-10,6,-7,9,-8,6,4,4,10,7,-4,1]],[[-6,-6,-8,2,5,-10,-10,8,8,3,-3,4,-4,9,7,2],[3,-8,8,-10,7,-9,-7,-4,-3,6,3,-1,3,4,2,-3],[-5,-5,-8,-8,-5,3,-6,-8,5,6,6,-4,-9,-10,6,7],[2,-4,9,9,-9,-7,-1,-3,-10,4,-8,6,-9,-10,10,4],[-1,6,10,-7,8,-5,8,-7,9,-6,-2,-4,-1,-5,4,-4],[-10,9,6,1,10,4,6,-8,-3,-1,9,5,4,2,9,-4],[-8,9,9,-9,5,-8,-5,5,-1,2,-6,9,-6,7,-6,-6]],[[-6,-10,4,5,-3,10,9,7,-6,1,7,-1,2,-10,-2,5],[-1,4,-2,-7,-2,-6,-4,3,3,1,6,5,-1,8,-3,-1],[6,2,-4,7,-7,7,6,-3,-5,-1,8,1,-2,3,2,4],[9,7,4,-9,7,-4,7,-3,2,5,9,1,5,-1,-8,-4],[-10,2,7,6,-9,-8,-8,3,5,1,-6,-7,8,7,-2,5],[-3,7,8,5,-4,6,-6,-1,6,2,6,-2,-9,2,-1,-5],[-4,8,6,1,-8,9,7,2,-5,5,6,-6,10,8,5,-8]],[[4,2,1,9,4,1,9,5,10,5,-9,4,-1,1,-4,6],[8,9,5,7,5,9,5,-7,-3,-4,-3,2,-9,-1,-5,-2],[-7,10,-8,-1,9,4,-3,-9,-3,-9,-1,2,3,4,10,-10],[-8,1,9,8,2,-10,-5,1,3,-6,-10,-6,-4,2,-8,-3],[3,4,-5,-10,4,-2,-10,-7,-3,-1,3,-6,8,3,8,-4],[-1,3,-1,-5,-4,4,-9,8,7,-5,-7,-7,6,-2,-7,9],[7,4,-6,4,7,3,10,8,-1,8,-3,-4,7,5,-4,-2]],[[8,-10,-6,-2,2,-6,9,10,8,-9,-4,-10,-8,-7,-1,7],[4,4,2,10,5,8,4,3,9,3,-4,-6,-9,-9,9,-2],[3,-2,3,-3,-2,2,1,5,9,5,10,8,-2,2,4,6],[-9,4,-2,2,-10,-7,-10,-2,10,-4,7,-2,10,-2,-5,2],[7,-7,3,-1,4,3,-2,-4,-2,-5,-10,-10,10,-5,-10,-10],[-4,-8,-8,9,8,-5,1,-5,8,4,8,2,-5,4,5,6],[2,-6,10,-10,1,9,7,-3,-3,-6,-10,-8,5,-4,-5,-10]],[[2,-7,3,-3,7,4,-7,10,5,-2,4,2,1,10,6,-4],[7,-1,3,7,-5,3,-2,-3,-8,-4,4,-4,1,2,5,6],[-1,6,-10,-1,4,8,-6,-2,3,-9,-1,-1,-6,-10,2,4],[-2,5,-3,-6,8,-2,-4,-1,10,5,2,4,2,10,1,-5],[-4,2,7,-4,-3,-1,1,-5,1,-2,7,-10,1,2,2,2],[8,-5,5,9,-8,-4,-2,9,10,-4,-7,-7,2,8,-7,-4],[-6,1,10,9,10,-4,4,-4,5,3,-2,-8,-2,-2,9,-5]],[[5,-8,5,1,-3,-6,2,-3,-9,9,-9,-8,5,1,6,-1],[-3,5,6,-1,-5,-6,-8,4,-5,1,-1,-4,-8,2,-2,-6],[4,1,9,9,-1,-3,-3,-8,-9,2,-7,8,-3,3,5,-10],[-1,9,3,6,-2,-6,-5,5,5,-5,6,-10,-6,-4,-2,-2],[-5,5,-10,5,9,8,8,-7,1,-5,-5,-5,10,4,6,-7],[6,1,4,-7,-7,-8,-8,-6,-6,3,-6,4,10,7,3,-8],[-5,-4,-5,3,-8,9,-5,3,7,-5,-6,10,9,3,3,-3]]], dtype = "uint16")#candidate|7026|(10, 7, 16)|const|uint16
var_7027 = relay.var("var_7027", dtype = "uint16", shape = (10, 7, 16))#candidate|7027|(10, 7, 16)|var|uint16
bop_7028 = relay.bitwise_xor(const_7026.astype('uint16'), relay.reshape(var_7027.astype('uint16'), relay.shape_of(const_7026))) # shape=(10, 7, 16)
func_5100_call = mod.get_global_var('func_5100')
func_5103_call = mutated_mod.get_global_var('func_5103')
var_7032 = relay.var("var_7032", dtype = "float64", shape = (140,))#candidate|7032|(140,)|var|float64
call_7031 = relay.TupleGetItem(func_5100_call(relay.reshape(var_7032.astype('float64'), [10, 2, 7])), 0)
call_7033 = relay.TupleGetItem(func_5103_call(relay.reshape(var_7032.astype('float64'), [10, 2, 7])), 0)
output = relay.Tuple([bop_7028,call_7031,var_7032,])
output2 = relay.Tuple([bop_7028,call_7033,var_7032,])
func_7042 = relay.Function([var_7027,var_7032,], output)
mod['func_7042'] = func_7042
mod = relay.transform.InferType()(mod)
mutated_mod['func_7042'] = func_7042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7042_call = mutated_mod.get_global_var('func_7042')
var_7044 = relay.var("var_7044", dtype = "uint16", shape = (10, 7, 16))#candidate|7044|(10, 7, 16)|var|uint16
var_7045 = relay.var("var_7045", dtype = "float64", shape = (140,))#candidate|7045|(140,)|var|float64
call_7043 = func_7042_call(var_7044,var_7045,)
output = call_7043
func_7046 = relay.Function([var_7044,var_7045,], output)
mutated_mod['func_7046'] = func_7046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_942_call = mod.get_global_var('func_942')
func_944_call = mutated_mod.get_global_var('func_944')
call_7077 = relay.TupleGetItem(func_942_call(), 1)
call_7078 = relay.TupleGetItem(func_944_call(), 1)
output = call_7077
output2 = call_7078
func_7107 = relay.Function([], output)
mod['func_7107'] = func_7107
mod = relay.transform.InferType()(mod)
mutated_mod['func_7107'] = func_7107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7107_call = mutated_mod.get_global_var('func_7107')
call_7108 = func_7107_call()
output = call_7108
func_7109 = relay.Function([], output)
mutated_mod['func_7109'] = func_7109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4086_call = mod.get_global_var('func_4086')
func_4087_call = mutated_mod.get_global_var('func_4087')
call_7129 = relay.TupleGetItem(func_4086_call(), 0)
call_7130 = relay.TupleGetItem(func_4087_call(), 0)
output = call_7129
output2 = call_7130
func_7132 = relay.Function([], output)
mod['func_7132'] = func_7132
mod = relay.transform.InferType()(mod)
mutated_mod['func_7132'] = func_7132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7132_call = mutated_mod.get_global_var('func_7132')
call_7133 = func_7132_call()
output = call_7133
func_7134 = relay.Function([], output)
mutated_mod['func_7134'] = func_7134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5959_call = mod.get_global_var('func_5959')
func_5961_call = mutated_mod.get_global_var('func_5961')
call_7147 = func_5959_call()
call_7148 = func_5959_call()
output = relay.Tuple([call_7147,])
output2 = relay.Tuple([call_7148,])
func_7149 = relay.Function([], output)
mod['func_7149'] = func_7149
mod = relay.transform.InferType()(mod)
output = func_7149()
func_7150 = relay.Function([], output)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4041_call = mod.get_global_var('func_4041')
func_4043_call = mutated_mod.get_global_var('func_4043')
call_7162 = relay.TupleGetItem(func_4041_call(), 1)
call_7163 = relay.TupleGetItem(func_4043_call(), 1)
func_4121_call = mod.get_global_var('func_4121')
func_4125_call = mutated_mod.get_global_var('func_4125')
const_7184 = relay.const([-9.884707,-2.342523,0.797748,-4.992614,-0.222845,-5.535528,8.746112,6.944362,7.730288,-4.352077,-5.326508,5.779496,-2.094439,-9.153049,6.689560,-0.867218,0.507429,-2.088072,8.454754,0.594311,-0.762103,2.367783,8.847821,0.129210,8.946938,6.971000,-9.119390,9.449882,5.075103,-6.897516], dtype = "float64")#candidate|7184|(30,)|const|float64
const_7185 = relay.const([9.766423,-6.859137,-4.488446,-1.283426,7.094718,-8.810560,2.712847,5.131808,-4.625594,-9.173465,-5.317342,0.337235,8.049611,-7.611151,-9.978921,6.576601,8.245924,-5.339070,0.875222,-9.132835,8.443860,-2.817910,-3.985644,2.249610,-8.054714,1.733391,1.493151,-6.421363,-7.629171,-1.935992,-1.584867,-6.452629,7.945492,-2.533462,4.086291,4.767956,1.260502,6.338935,-4.441192,-1.860515,-1.493822,5.425905,0.496904,9.675890,-8.817539,-8.223104,1.578668,-4.140959,-2.536207,-8.804462,9.022139,-8.129740,8.571390,-5.316658,-6.877629,-4.347624,-4.917266,3.258084,4.891830,0.033686,-1.680627,8.678302,-5.133363,-5.086308,-0.822736,-3.667546,-4.342208,-9.050826,1.339332,5.126953,-3.471368,-4.073517,8.909480,-8.842948,-1.580053,-5.593157,6.932238,6.409700,9.693627,-1.779247,-1.978146,0.413682,0.926048,-5.838291,-1.181301,5.962841,1.024974,3.298303,8.260983,3.710030,6.092801,-0.196480,4.675935,-2.733109,2.134846,-4.744276,-8.158460,-4.007537,-5.066501,-3.782054,6.078316,1.633227,4.741197,8.709727,-4.512031,1.632034,6.628013,-2.682220,6.895936,5.422466,-1.117174,-0.076763,-8.588552,-4.551747,4.558140,5.542599,-7.907733,1.133317,-5.420621,-7.168684], dtype = "float32")#candidate|7185|(120,)|const|float32
call_7183 = relay.TupleGetItem(func_4121_call(relay.reshape(const_7184.astype('float64'), [30,]), relay.reshape(const_7185.astype('float32'), [120,]), ), 2)
call_7186 = relay.TupleGetItem(func_4125_call(relay.reshape(const_7184.astype('float64'), [30,]), relay.reshape(const_7185.astype('float32'), [120,]), ), 2)
func_6924_call = mod.get_global_var('func_6924')
func_6926_call = mutated_mod.get_global_var('func_6926')
call_7204 = relay.TupleGetItem(func_6924_call(), 1)
call_7205 = relay.TupleGetItem(func_6926_call(), 1)
const_7212 = relay.const([[[-3.120191,-2.116023,-6.550938,-7.201661,4.450040,-3.590587,-7.519216,4.261531],[-9.191689,6.691887,6.102592,-2.101532,-5.703955,2.872244,-5.837801,-9.504545],[-1.827358,2.548237,5.152786,-7.121185,-9.531988,4.340506,4.158150,9.267518],[3.532476,8.698532,-9.650478,3.816947,6.090618,-4.599053,8.532874,-2.700809],[0.669180,6.562188,7.264076,5.162507,-8.676697,0.838283,-2.552443,7.543771],[7.008033,-6.347314,-2.954038,-9.841049,-3.881979,4.456535,7.757284,1.631425],[2.251296,-4.539945,-0.950192,2.726568,-4.777449,-2.666835,0.313192,7.603071],[8.040754,-3.296274,8.437603,5.478998,9.225414,-7.948019,-5.713797,-7.238566],[-2.337532,5.530682,-6.627001,3.656489,2.248462,4.988259,3.601273,1.489833],[-8.776715,-6.903618,-4.885566,4.682728,-5.324487,7.012826,9.271576,9.333076],[-9.874392,6.170736,9.029989,8.009154,-0.925803,1.306071,3.672346,-3.682435]],[[-4.023089,-0.256282,-1.295514,-5.501788,1.436596,-9.112409,8.487739,-9.032838],[-8.075352,1.073906,-8.471627,-6.069785,9.276568,-5.261837,-9.984338,0.783089],[6.310363,0.409019,0.290751,-1.804172,5.863261,-4.100610,-7.837137,-3.563522],[-7.057414,-7.186731,6.256930,7.915086,-8.523937,8.394207,0.981427,0.847659],[-0.959690,-4.574362,7.820346,-1.800966,3.615725,4.734139,8.607973,-3.836954],[8.751407,-7.391294,5.842820,-7.527414,7.343603,-8.479117,-8.253231,7.533821],[5.088837,-8.801756,6.825266,6.411006,9.165807,-1.288287,9.233498,-6.870530],[-6.809977,7.784979,8.309291,1.318781,0.743173,0.564415,-7.565568,2.048234],[-4.782229,-0.760313,-2.252888,1.681058,-8.311719,3.630630,-5.144857,5.768896],[-7.397576,7.028740,-6.502172,3.395904,-6.485999,5.474137,3.058346,-4.964331],[-3.025575,7.043834,9.506287,0.768190,0.102098,2.033701,-7.360648,-2.997830]],[[4.452895,-3.475829,-0.845250,7.374196,-1.335704,8.398785,1.065058,-1.230331],[-4.290341,7.442536,-5.427094,-7.877454,3.093935,1.255241,-7.765061,-1.872547],[1.597327,7.925110,-4.695573,0.232774,7.999394,1.083941,-7.709588,-0.704343],[6.592779,-2.780270,-4.748562,8.706125,-0.252382,-4.156367,-4.697349,-6.118437],[1.197861,-5.785414,2.000146,4.161895,-1.721267,5.075119,-1.092144,-8.824084],[8.222740,5.460535,1.171738,0.554960,2.596744,-0.337338,8.305983,-5.119107],[-2.638610,-0.134180,-4.206692,-9.954424,-4.516518,8.553717,3.240814,7.288196],[9.575392,6.463067,9.182425,-8.709572,-2.639567,0.352062,-6.638247,-2.380060],[-4.054847,-0.858883,-7.247045,4.453542,-4.001744,2.729101,-0.907951,5.824582],[2.841858,-8.464512,2.738809,-2.089952,3.451395,0.587669,4.951599,-0.766848],[1.484280,-7.791873,5.359466,-2.739878,-6.630546,-0.744246,-4.760578,-5.527965]],[[-7.280543,0.857058,-0.508235,1.045966,7.541845,5.755394,-7.288228,-4.234182],[-6.189449,-3.588739,-8.257355,4.017942,-7.986907,-2.566692,1.518050,3.977736],[3.580018,-0.132812,-9.509348,-8.363692,-5.529543,-2.802839,3.178339,-3.780235],[8.539909,-6.625994,-0.776486,-0.302315,0.633823,3.577626,-6.967144,-1.704198],[3.296034,1.537938,-8.614678,3.533626,8.472330,9.812623,-6.214953,-8.282074],[-4.852129,-8.441247,-3.673365,-3.858297,2.890936,1.996010,-2.063476,4.300768],[-7.558020,1.862246,-0.979334,7.314117,-6.181844,1.826159,7.482804,-1.127506],[-2.515046,-1.600409,9.821232,-1.556823,-3.597442,-8.002481,3.584404,1.204146],[-2.373748,-6.465596,8.145987,-6.617988,-1.102771,0.806830,0.200529,-1.057308],[-1.318149,5.009714,2.625995,-4.846921,6.254433,-5.485737,-4.172319,-7.728544],[-6.774796,-0.481968,-7.138351,2.263648,-1.694012,-1.326853,-3.713351,9.861059]],[[9.179514,-7.466086,-6.186059,6.469018,-6.705279,-3.616305,7.184207,1.123251],[1.638550,0.670407,9.454854,-4.393534,6.355444,2.135286,1.270816,-7.178155],[3.934463,5.599915,9.863194,5.736468,-0.147436,3.350803,-3.093706,9.612064],[-9.065399,-8.315811,8.413811,3.501406,5.615520,-2.295447,2.756083,-9.827223],[-1.827291,-3.296157,-0.156546,5.656838,8.880771,-0.526486,6.834311,5.512682],[-0.768180,7.136736,-0.461760,9.633733,-5.056370,4.746532,-9.235707,-6.837968],[6.362288,8.875035,4.228565,1.734856,5.198899,-7.516207,6.535426,-7.484037],[3.101108,-3.005017,-4.467270,-6.071568,0.611874,-7.535359,3.595427,-5.715537],[3.524426,-4.563990,-4.774815,6.461792,9.480787,9.251235,2.508920,-8.663936],[0.867859,-9.731830,-6.512346,-8.247064,-5.980007,-9.985453,-9.155121,8.847689],[-4.728192,-4.220247,3.671760,-0.177434,1.828241,2.190089,9.432901,-6.172769]]], dtype = "float64")#candidate|7212|(5, 11, 8)|const|float64
bop_7213 = relay.not_equal(call_7162.astype('bool'), relay.reshape(const_7212.astype('bool'), relay.shape_of(call_7162))) # shape=(5, 11, 8)
bop_7216 = relay.not_equal(call_7163.astype('bool'), relay.reshape(const_7212.astype('bool'), relay.shape_of(call_7163))) # shape=(5, 11, 8)
output = relay.Tuple([call_7183,const_7184,const_7185,call_7204,bop_7213,])
output2 = relay.Tuple([call_7186,const_7184,const_7185,call_7205,bop_7216,])
func_7217 = relay.Function([], output)
mod['func_7217'] = func_7217
mod = relay.transform.InferType()(mod)
mutated_mod['func_7217'] = func_7217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7217_call = mutated_mod.get_global_var('func_7217')
call_7218 = func_7217_call()
output = call_7218
func_7219 = relay.Function([], output)
mutated_mod['func_7219'] = func_7219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7217_call = mod.get_global_var('func_7217')
func_7219_call = mutated_mod.get_global_var('func_7219')
call_7226 = relay.TupleGetItem(func_7217_call(), 2)
call_7227 = relay.TupleGetItem(func_7219_call(), 2)
func_4813_call = mod.get_global_var('func_4813')
func_4814_call = mutated_mod.get_global_var('func_4814')
call_7231 = func_4813_call()
call_7232 = func_4813_call()
func_5378_call = mod.get_global_var('func_5378')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_7233 = relay.TupleGetItem(func_5378_call(), 0)
call_7234 = relay.TupleGetItem(func_5380_call(), 0)
func_2085_call = mod.get_global_var('func_2085')
func_2088_call = mutated_mod.get_global_var('func_2088')
var_7249 = relay.var("var_7249", dtype = "float32", shape = (3, 24))#candidate|7249|(3, 24)|var|float32
call_7248 = func_2085_call(relay.reshape(var_7249.astype('float32'), [8, 1, 9]))
call_7250 = func_2085_call(relay.reshape(var_7249.astype('float32'), [8, 1, 9]))
func_2396_call = mod.get_global_var('func_2396')
func_2398_call = mutated_mod.get_global_var('func_2398')
call_7253 = func_2396_call()
call_7254 = func_2396_call()
func_1512_call = mod.get_global_var('func_1512')
func_1513_call = mutated_mod.get_global_var('func_1513')
call_7259 = func_1512_call()
call_7260 = func_1512_call()
uop_7269 = relay.asinh(var_7249.astype('float32')) # shape=(3, 24)
func_2783_call = mod.get_global_var('func_2783')
func_2786_call = mutated_mod.get_global_var('func_2786')
var_7273 = relay.var("var_7273", dtype = "float64", shape = (8, 104))#candidate|7273|(8, 104)|var|float64
call_7272 = relay.TupleGetItem(func_2783_call(relay.reshape(var_7273.astype('float64'), [13, 8, 8])), 1)
call_7274 = relay.TupleGetItem(func_2786_call(relay.reshape(var_7273.astype('float64'), [13, 8, 8])), 1)
bop_7280 = relay.logical_xor(var_7249.astype('int16'), relay.reshape(call_7248.astype('int16'), relay.shape_of(var_7249))) # shape=(3, 24)
bop_7283 = relay.logical_xor(var_7249.astype('int16'), relay.reshape(call_7250.astype('int16'), relay.shape_of(var_7249))) # shape=(3, 24)
uop_7287 = relay.rsqrt(uop_7269.astype('float32')) # shape=(3, 24)
func_471_call = mod.get_global_var('func_471')
func_472_call = mutated_mod.get_global_var('func_472')
call_7290 = func_471_call()
call_7291 = func_471_call()
func_7217_call = mod.get_global_var('func_7217')
func_7219_call = mutated_mod.get_global_var('func_7219')
call_7311 = relay.TupleGetItem(func_7217_call(), 1)
call_7312 = relay.TupleGetItem(func_7219_call(), 1)
bop_7313 = relay.add(uop_7287.astype('float64'), relay.reshape(bop_7280.astype('float64'), relay.shape_of(uop_7287))) # shape=(3, 24)
bop_7316 = relay.add(uop_7287.astype('float64'), relay.reshape(bop_7283.astype('float64'), relay.shape_of(uop_7287))) # shape=(3, 24)
bop_7323 = relay.bitwise_or(uop_7287.astype('int32'), relay.reshape(bop_7313.astype('int32'), relay.shape_of(uop_7287))) # shape=(3, 24)
bop_7326 = relay.bitwise_or(uop_7287.astype('int32'), relay.reshape(bop_7316.astype('int32'), relay.shape_of(uop_7287))) # shape=(3, 24)
var_7333 = relay.var("var_7333", dtype = "float32", shape = (3, 24))#candidate|7333|(3, 24)|var|float32
bop_7334 = relay.maximum(uop_7269.astype('int64'), relay.reshape(var_7333.astype('int64'), relay.shape_of(uop_7269))) # shape=(3, 24)
uop_7337 = relay.sigmoid(bop_7313.astype('float64')) # shape=(3, 24)
uop_7339 = relay.sigmoid(bop_7316.astype('float64')) # shape=(3, 24)
output = relay.Tuple([call_7226,call_7231,call_7233,call_7253,call_7259,call_7272,var_7273,call_7290,call_7311,bop_7323,bop_7334,uop_7337,])
output2 = relay.Tuple([call_7227,call_7232,call_7234,call_7254,call_7260,call_7274,var_7273,call_7291,call_7312,bop_7326,bop_7334,uop_7339,])
func_7352 = relay.Function([var_7249,var_7273,var_7333,], output)
mod['func_7352'] = func_7352
mod = relay.transform.InferType()(mod)
mutated_mod['func_7352'] = func_7352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7352_call = mutated_mod.get_global_var('func_7352')
var_7354 = relay.var("var_7354", dtype = "float32", shape = (3, 24))#candidate|7354|(3, 24)|var|float32
var_7355 = relay.var("var_7355", dtype = "float64", shape = (8, 104))#candidate|7355|(8, 104)|var|float64
var_7356 = relay.var("var_7356", dtype = "float32", shape = (3, 24))#candidate|7356|(3, 24)|var|float32
call_7353 = func_7352_call(var_7354,var_7355,var_7356,)
output = call_7353
func_7357 = relay.Function([var_7354,var_7355,var_7356,], output)
mutated_mod['func_7357'] = func_7357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6499_call = mod.get_global_var('func_6499')
func_6501_call = mutated_mod.get_global_var('func_6501')
call_7370 = func_6499_call()
call_7371 = func_6499_call()
func_2823_call = mod.get_global_var('func_2823')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_7372 = func_2823_call()
call_7373 = func_2823_call()
output = relay.Tuple([call_7370,call_7372,])
output2 = relay.Tuple([call_7371,call_7373,])
func_7376 = relay.Function([], output)
mod['func_7376'] = func_7376
mod = relay.transform.InferType()(mod)
output = func_7376()
func_7377 = relay.Function([], output)
mutated_mod['func_7377'] = func_7377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_7383 = relay.TupleGetItem(func_1822_call(), 0)
call_7384 = relay.TupleGetItem(func_1824_call(), 0)
output = call_7383
output2 = call_7384
func_7405 = relay.Function([], output)
mod['func_7405'] = func_7405
mod = relay.transform.InferType()(mod)
mutated_mod['func_7405'] = func_7405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7405_call = mutated_mod.get_global_var('func_7405')
call_7406 = func_7405_call()
output = call_7406
func_7407 = relay.Function([], output)
mutated_mod['func_7407'] = func_7407
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7495 = relay.var("var_7495", dtype = "float32", shape = (13, 5, 13))#candidate|7495|(13, 5, 13)|var|float32
uop_7496 = relay.asin(var_7495.astype('float32')) # shape=(13, 5, 13)
output = relay.Tuple([uop_7496,])
output2 = relay.Tuple([uop_7496,])
func_7499 = relay.Function([var_7495,], output)
mod['func_7499'] = func_7499
mod = relay.transform.InferType()(mod)
var_7500 = relay.var("var_7500", dtype = "float32", shape = (13, 5, 13))#candidate|7500|(13, 5, 13)|var|float32
output = func_7499(var_7500)
func_7501 = relay.Function([var_7500], output)
mutated_mod['func_7501'] = func_7501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6924_call = mod.get_global_var('func_6924')
func_6926_call = mutated_mod.get_global_var('func_6926')
call_7508 = relay.TupleGetItem(func_6924_call(), 2)
call_7509 = relay.TupleGetItem(func_6926_call(), 2)
func_6060_call = mod.get_global_var('func_6060')
func_6062_call = mutated_mod.get_global_var('func_6062')
call_7530 = relay.TupleGetItem(func_6060_call(), 0)
call_7531 = relay.TupleGetItem(func_6062_call(), 0)
output = relay.Tuple([call_7508,call_7530,])
output2 = relay.Tuple([call_7509,call_7531,])
func_7536 = relay.Function([], output)
mod['func_7536'] = func_7536
mod = relay.transform.InferType()(mod)
mutated_mod['func_7536'] = func_7536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7536_call = mutated_mod.get_global_var('func_7536')
call_7537 = func_7536_call()
output = call_7537
func_7538 = relay.Function([], output)
mutated_mod['func_7538'] = func_7538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4086_call = mod.get_global_var('func_4086')
func_4087_call = mutated_mod.get_global_var('func_4087')
call_7586 = relay.TupleGetItem(func_4086_call(), 0)
call_7587 = relay.TupleGetItem(func_4087_call(), 0)
func_5561_call = mod.get_global_var('func_5561')
func_5563_call = mutated_mod.get_global_var('func_5563')
call_7598 = relay.TupleGetItem(func_5561_call(), 0)
call_7599 = relay.TupleGetItem(func_5563_call(), 0)
func_6721_call = mod.get_global_var('func_6721')
func_6723_call = mutated_mod.get_global_var('func_6723')
call_7612 = func_6721_call()
call_7613 = func_6721_call()
output = relay.Tuple([call_7586,call_7598,call_7612,])
output2 = relay.Tuple([call_7587,call_7599,call_7613,])
func_7627 = relay.Function([], output)
mod['func_7627'] = func_7627
mod = relay.transform.InferType()(mod)
output = func_7627()
func_7628 = relay.Function([], output)
mutated_mod['func_7628'] = func_7628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1753_call = mod.get_global_var('func_1753')
func_1754_call = mutated_mod.get_global_var('func_1754')
call_7640 = relay.TupleGetItem(func_1753_call(), 1)
call_7641 = relay.TupleGetItem(func_1754_call(), 1)
func_6017_call = mod.get_global_var('func_6017')
func_6018_call = mutated_mod.get_global_var('func_6018')
call_7662 = relay.TupleGetItem(func_6017_call(), 1)
call_7663 = relay.TupleGetItem(func_6018_call(), 1)
uop_7665 = relay.atanh(call_7662.astype('float32')) # shape=(13, 8, 8)
uop_7667 = relay.atanh(call_7663.astype('float32')) # shape=(13, 8, 8)
func_734_call = mod.get_global_var('func_734')
func_736_call = mutated_mod.get_global_var('func_736')
call_7701 = relay.TupleGetItem(func_734_call(), 0)
call_7702 = relay.TupleGetItem(func_736_call(), 0)
uop_7704 = relay.log(uop_7665.astype('float64')) # shape=(13, 8, 8)
uop_7706 = relay.log(uop_7667.astype('float64')) # shape=(13, 8, 8)
func_385_call = mod.get_global_var('func_385')
func_387_call = mutated_mod.get_global_var('func_387')
call_7714 = relay.TupleGetItem(func_385_call(relay.reshape(call_7640.astype('float64'), [5, 11, 8])), 1)
call_7715 = relay.TupleGetItem(func_387_call(relay.reshape(call_7640.astype('float64'), [5, 11, 8])), 1)
func_6120_call = mod.get_global_var('func_6120')
func_6123_call = mutated_mod.get_global_var('func_6123')
var_7725 = relay.var("var_7725", dtype = "float64", shape = (160,))#candidate|7725|(160,)|var|float64
call_7724 = relay.TupleGetItem(func_6120_call(relay.reshape(var_7725.astype('float64'), [5, 8, 4])), 0)
call_7726 = relay.TupleGetItem(func_6123_call(relay.reshape(var_7725.astype('float64'), [5, 8, 4])), 0)
output = relay.Tuple([call_7640,call_7701,uop_7704,call_7714,call_7724,var_7725,])
output2 = relay.Tuple([call_7641,call_7702,uop_7706,call_7715,call_7726,var_7725,])
func_7728 = relay.Function([var_7725,], output)
mod['func_7728'] = func_7728
mod = relay.transform.InferType()(mod)
var_7729 = relay.var("var_7729", dtype = "float64", shape = (160,))#candidate|7729|(160,)|var|float64
output = func_7728(var_7729)
func_7730 = relay.Function([var_7729], output)
mutated_mod['func_7730'] = func_7730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5378_call = mod.get_global_var('func_5378')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_7843 = relay.TupleGetItem(func_5378_call(), 1)
call_7844 = relay.TupleGetItem(func_5380_call(), 1)
func_2538_call = mod.get_global_var('func_2538')
func_2541_call = mutated_mod.get_global_var('func_2541')
const_7885 = relay.const([2.785262,-6.286744,-4.204577,2.397852,-6.947123,7.651978,1.241274,3.600221,-7.455492,-1.001606,-3.611730,5.080431,6.018739,1.084949,2.406567,-8.994844,8.331937,1.253218,8.602822,-2.898055,1.011250,-2.717298,-2.682205,-8.875037,8.605412,6.981966,5.423756,2.288665,5.978861,-9.060844,5.746143,-6.885430,0.715230,-8.540483,-5.559374,9.466795,-7.138074,6.217831,1.209489,-7.312155,-8.822442,-6.358576,-9.477033,-7.867703,-8.621003,8.144547,4.736495,3.145177,0.743237,-3.000489,-9.414288,2.699557,4.196658,0.903920,2.112594,2.565999,3.091707,9.955332,-5.790373,4.915036,-0.734140,-7.565920,-2.338682,4.100528,-0.727177,-8.637291,8.198214,0.754440,-6.728334,5.253155,-2.282710,8.462001,-3.024239,-8.377859,8.825728,7.528424,-4.633794,6.015242,1.891303,-3.366427,-5.606469,-7.152480,6.968695,8.821350,-5.757707,1.600146,6.674844,-8.424420,8.317576,-0.115084,9.498753,4.666676,-9.136675,-2.478986,2.027576,3.232579,3.333559,3.662015,2.146231,-0.182926,2.233996,0.633937,4.727788,-8.988121,-8.836428,4.385975,-9.641231,8.107896,0.066448,2.984095,-4.321486,6.248124,-4.550940,-1.406689,3.294771,-2.120022,-4.906178,4.166221,1.865824,9.856688,8.242143,6.072403,2.346029,-8.796457,0.299956,2.592182,-0.446673,5.094681,3.535146,-4.095386,2.660647,8.630764,-2.101887,4.011572,-6.235051,3.559746,7.029179,2.739800,2.642969,4.331767,6.628569,9.140174,4.413996,7.074634,-2.146919,1.400601,-3.595946,-7.326344,-9.718964,-1.795923,-6.215875,-4.228368,5.908987,-9.365131,2.183213,4.326200,-3.421461,-8.746543,1.611417,-8.068882,0.864580,2.068923,-7.296459,0.311587,4.783401,8.233487,7.859566,0.933320,5.292630,-4.269166,-2.472418,-6.439677,-8.624542,-3.484004,-4.064615,2.451900,4.466386,6.275875,-6.271402,-1.506789,-5.440641,2.266219,6.282409,-4.061951,-8.713099,2.278953,-5.536612,5.476365,-1.506220,5.819528,-4.092419,-3.447267,2.169933,7.193823,-2.269988,-2.215162,4.413540,3.883731,-6.460869,-2.612242,-3.608961,2.647662,7.959708,7.546796,1.566463,-8.043286,0.688341,7.678092,-8.400190,3.602894,-5.228440,3.263253,5.687318,-3.672041,1.350982,1.036408,-1.139942,-3.258431,1.487792,0.273941,-0.938192,3.316981,-8.100594,7.647768,4.771978,-1.995042,-2.488020,-7.068206,-5.095733,0.756345,2.576814,6.360143,-0.985403,1.064983,1.955983,-7.014843,-9.412392,7.041656,-0.500977,5.336960,0.583691,9.950621,9.551415,-2.140565,-1.370870,1.535935,-9.054611,4.797532,8.334555,-0.372066,9.282176,-3.496822,-6.533891,-8.603631,-0.139440,1.382575,9.224927,7.664485,-6.114645,-9.853651,-6.886301,-6.297729,-1.799408,2.927580,-7.876849,-4.744650,-6.287209,6.061437,1.387881,2.240233,6.968846,5.795005,8.529837,5.205671,-3.516695,-7.515589,-1.434272,2.667057,-6.551262,-2.831588,4.033024,-9.938680,8.555884,-6.663137,0.932590,0.934304,-6.772630,-6.596968,6.739800,0.823737,1.702994,-1.237930,-0.148507,5.611936,-3.067203,8.413127,-4.005666,4.313204,4.629664,-8.312949,7.764566,1.796079,8.762272,1.892680,-2.688644,-4.395391,-6.507116,1.219983,7.960912,3.464421,-0.445233,9.082549,-8.292981,-7.728744,-7.020871,9.543178,-7.138259,-6.165690,-6.885485,4.606230,-3.418897,-6.725935,-0.648609,-1.734837,-2.890875,-0.608404,-7.195318,-1.745774,-9.817584,1.457738,3.124640,9.187788,0.507191,2.099281,8.782646,-1.250972], dtype = "float64")#candidate|7885|(336,)|const|float64
call_7884 = relay.TupleGetItem(func_2538_call(relay.reshape(const_7885.astype('float64'), [3, 16, 7])), 0)
call_7886 = relay.TupleGetItem(func_2541_call(relay.reshape(const_7885.astype('float64'), [3, 16, 7])), 0)
output = relay.Tuple([call_7843,call_7884,const_7885,])
output2 = relay.Tuple([call_7844,call_7886,const_7885,])
func_7923 = relay.Function([], output)
mod['func_7923'] = func_7923
mod = relay.transform.InferType()(mod)
output = func_7923()
func_7924 = relay.Function([], output)
mutated_mod['func_7924'] = func_7924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3879_call = mod.get_global_var('func_3879')
func_3880_call = mutated_mod.get_global_var('func_3880')
call_7934 = func_3879_call()
call_7935 = func_3879_call()
output = call_7934
output2 = call_7935
func_7942 = relay.Function([], output)
mod['func_7942'] = func_7942
mod = relay.transform.InferType()(mod)
mutated_mod['func_7942'] = func_7942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7942_call = mutated_mod.get_global_var('func_7942')
call_7943 = func_7942_call()
output = call_7943
func_7944 = relay.Function([], output)
mutated_mod['func_7944'] = func_7944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4261_call = mod.get_global_var('func_4261')
func_4262_call = mutated_mod.get_global_var('func_4262')
call_7989 = relay.TupleGetItem(func_4261_call(), 2)
call_7990 = relay.TupleGetItem(func_4262_call(), 2)
uop_8001 = relay.log2(call_7989.astype('float64')) # shape=(448,)
uop_8003 = relay.log2(call_7990.astype('float64')) # shape=(448,)
output = uop_8001
output2 = uop_8003
func_8013 = relay.Function([], output)
mod['func_8013'] = func_8013
mod = relay.transform.InferType()(mod)
mutated_mod['func_8013'] = func_8013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8013_call = mutated_mod.get_global_var('func_8013')
call_8014 = func_8013_call()
output = call_8014
func_8015 = relay.Function([], output)
mutated_mod['func_8015'] = func_8015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1512_call = mod.get_global_var('func_1512')
func_1513_call = mutated_mod.get_global_var('func_1513')
call_8030 = func_1512_call()
call_8031 = func_1512_call()
output = relay.Tuple([call_8030,])
output2 = relay.Tuple([call_8031,])
func_8032 = relay.Function([], output)
mod['func_8032'] = func_8032
mod = relay.transform.InferType()(mod)
output = func_8032()
func_8033 = relay.Function([], output)
mutated_mod['func_8033'] = func_8033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4872_call = mod.get_global_var('func_4872')
func_4873_call = mutated_mod.get_global_var('func_4873')
call_8042 = relay.TupleGetItem(func_4872_call(), 0)
call_8043 = relay.TupleGetItem(func_4873_call(), 0)
output = call_8042
output2 = call_8043
func_8055 = relay.Function([], output)
mod['func_8055'] = func_8055
mod = relay.transform.InferType()(mod)
output = func_8055()
func_8056 = relay.Function([], output)
mutated_mod['func_8056'] = func_8056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6060_call = mod.get_global_var('func_6060')
func_6062_call = mutated_mod.get_global_var('func_6062')
call_8060 = relay.TupleGetItem(func_6060_call(), 0)
call_8061 = relay.TupleGetItem(func_6062_call(), 0)
output = relay.Tuple([call_8060,])
output2 = relay.Tuple([call_8061,])
func_8067 = relay.Function([], output)
mod['func_8067'] = func_8067
mod = relay.transform.InferType()(mod)
output = func_8067()
func_8068 = relay.Function([], output)
mutated_mod['func_8068'] = func_8068
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8088 = relay.var("var_8088", dtype = "uint32", shape = (15, 10, 11))#candidate|8088|(15, 10, 11)|var|uint32
var_8089 = relay.var("var_8089", dtype = "uint32", shape = (15, 10, 11))#candidate|8089|(15, 10, 11)|var|uint32
bop_8090 = relay.bitwise_or(var_8088.astype('uint32'), relay.reshape(var_8089.astype('uint32'), relay.shape_of(var_8088))) # shape=(15, 10, 11)
func_1633_call = mod.get_global_var('func_1633')
func_1635_call = mutated_mod.get_global_var('func_1635')
const_8095 = relay.const([[5.851263,5.195008,4.863777,-3.884523],[-9.903144,-7.015608,-2.353431,3.413735],[1.726953,1.885752,2.306383,8.048623],[2.430806,-0.067542,0.664655,-1.677326],[-6.738520,-5.999547,1.709566,-9.096870],[1.424244,9.903537,9.726865,2.503546],[2.640229,-0.420944,8.799135,4.677807],[-6.174518,1.419073,-5.773781,-7.746073],[1.246549,9.158292,-4.112876,-3.123735],[-7.299259,1.943035,5.401631,3.973631],[-0.452879,3.787700,1.562018,-6.080143],[-1.138542,4.158591,2.249611,-0.976239],[-8.538399,-2.155648,2.973400,-2.793675],[-2.066149,-7.411955,-0.346324,-8.148942],[1.328671,-0.529137,-5.123684,1.177234],[-3.957445,-3.641113,-1.712749,-9.236481],[-7.603446,7.005208,-4.419100,0.852096],[-1.282302,-4.003616,3.298297,1.531366],[-6.564265,7.343541,-3.611618,1.081055],[4.988006,-4.558578,-5.640274,-6.118715],[2.300123,9.732544,3.616797,-3.415160],[-9.830714,-6.959953,-8.783657,-7.415866],[-7.925844,8.693794,-1.744750,8.754479],[-4.632837,-8.260367,5.747408,7.683183],[-6.860597,-5.257407,-1.437036,0.224232],[9.871921,-8.771567,1.209560,-2.550970],[8.805560,-2.304055,-3.259100,4.043914],[-9.048261,-1.988192,3.504572,-4.698913],[-5.133638,6.187184,-6.289747,3.780777],[0.878997,0.427046,-0.807269,-9.362750],[4.407872,-0.627640,-2.957033,2.922284],[4.576785,-6.210057,1.045630,-1.984334],[2.197626,-2.321496,6.117171,1.691059],[-5.627029,8.454265,-7.271501,-8.649227],[7.790683,-6.861797,-3.445330,-4.681003],[4.022576,-7.357981,7.973257,-4.350476],[9.164373,-7.249102,-6.570124,8.670678],[-4.642371,3.745469,-0.543532,3.780159],[-7.588507,5.966426,0.308765,-0.039909],[8.413965,5.302307,-3.960522,9.877736],[8.245106,-7.250031,-0.504234,-2.637936],[-6.586527,3.272749,8.917676,-2.719912],[-0.877934,-3.715767,2.867754,-8.316329],[-8.647369,-2.328204,7.280573,-8.698131],[6.563509,-3.880044,-6.467520,5.589338],[9.006678,5.441640,7.478176,-7.076054],[1.997086,6.451531,-6.314408,5.709408],[0.681606,1.247334,-4.919084,6.379088],[-3.930472,6.571270,-7.397584,2.608928],[4.458792,-2.668278,3.130359,4.433060],[-7.528814,4.360887,-5.474944,1.452299],[-3.333387,9.336193,-4.863924,3.129449],[-2.376230,9.081908,4.994857,-3.021674],[9.493724,7.435812,-8.664796,7.281342],[7.008231,5.711277,-1.262997,6.910271],[5.207961,2.284629,-3.960463,-4.991498],[9.839670,6.167511,-9.234334,2.061726],[9.350729,-5.430880,4.867030,-8.722056],[0.635806,2.904821,-0.938996,-8.864231],[1.565892,3.076726,-7.028745,-4.748600],[3.220281,-6.361727,-0.052923,9.348657],[-2.472520,8.817855,7.520339,-1.720829],[2.600710,-5.781794,8.118998,8.805666],[-4.990284,-7.285995,-6.331385,-9.646694],[-4.389441,7.230757,2.553638,-8.741650],[8.063680,1.948960,9.530325,7.049228],[4.057368,-7.995041,-6.393222,7.976945],[-1.002208,-9.374309,5.232095,-5.899326],[1.550267,-2.163594,-1.374761,3.409689],[-2.251514,5.523384,-1.515984,-6.388831],[-7.586502,-1.219692,-0.140187,-0.049372],[6.122058,7.574137,5.622949,5.668362],[5.919810,0.876135,-7.013376,0.935081],[-3.190106,7.305911,9.513270,-1.876130],[-5.771243,1.631683,2.666971,-1.284531],[-6.340697,1.442247,5.875995,-5.605318],[-7.058566,3.601643,-8.405452,7.728353],[1.722605,-8.440470,-7.581326,-7.733328],[3.743996,3.643053,1.404517,-9.593421],[7.461669,-5.157690,-2.112076,9.412495],[-5.760371,8.836068,-9.695004,6.740447],[5.642274,-4.092613,0.156689,3.557377],[-9.494793,3.502514,-0.932796,5.702962],[1.030521,-7.999901,6.238630,-3.526828],[-7.571610,-6.844790,-6.364321,-8.871131],[8.217759,1.248035,-3.745464,-2.293632],[1.514889,-2.199086,5.011637,6.319071],[0.092793,-4.618793,1.337792,7.129934],[-2.183077,-3.041668,0.680448,3.888451],[-1.962292,6.688755,9.820029,4.203263],[2.049830,-6.644117,-3.438505,5.434471],[3.790677,-1.033045,-4.558138,6.686376],[6.209612,9.396263,-6.128429,-1.185651],[7.407025,6.358593,9.053667,1.674181],[9.970435,1.385268,9.475889,9.965043],[-1.770810,-7.480198,7.712430,1.290860],[8.148399,-2.570908,7.975023,-4.226212],[-5.996600,2.310250,9.967620,8.128719],[-2.926497,-4.516230,4.457213,5.625301],[6.770795,7.602868,1.801964,5.377611],[3.984239,-8.784980,-7.928723,-4.588766],[2.785160,-5.597306,-3.217293,5.369373],[-1.336220,4.614884,7.062423,9.244235],[-0.483465,-3.824941,-2.109266,-9.893892],[8.572322,-8.898939,-1.158861,-7.128596],[6.314019,-3.675374,-7.332813,-9.270983],[4.658156,1.935662,-2.124198,2.454830],[6.367301,-6.580280,6.757531,5.184622],[-1.867469,3.597599,-7.461531,-1.203007],[-0.860006,-4.539175,-8.569956,-0.375721]], dtype = "float64")#candidate|8095|(110, 4)|const|float64
call_8094 = relay.TupleGetItem(func_1633_call(relay.reshape(const_8095.astype('float64'), [5, 11, 8])), 1)
call_8096 = relay.TupleGetItem(func_1635_call(relay.reshape(const_8095.astype('float64'), [5, 11, 8])), 1)
bop_8098 = relay.bitwise_or(const_8095.astype('int64'), relay.reshape(call_8094.astype('int64'), relay.shape_of(const_8095))) # shape=(110, 4)
bop_8101 = relay.bitwise_or(const_8095.astype('int64'), relay.reshape(call_8096.astype('int64'), relay.shape_of(const_8095))) # shape=(110, 4)
func_5351_call = mod.get_global_var('func_5351')
func_5353_call = mutated_mod.get_global_var('func_5353')
call_8107 = relay.TupleGetItem(func_5351_call(), 0)
call_8108 = relay.TupleGetItem(func_5353_call(), 0)
func_5495_call = mod.get_global_var('func_5495')
func_5496_call = mutated_mod.get_global_var('func_5496')
call_8115 = relay.TupleGetItem(func_5495_call(), 0)
call_8116 = relay.TupleGetItem(func_5496_call(), 0)
uop_8117 = relay.rsqrt(const_8095.astype('float32')) # shape=(110, 4)
bop_8122 = relay.divide(uop_8117.astype('float32'), relay.reshape(call_8115.astype('float32'), relay.shape_of(uop_8117))) # shape=(110, 4)
bop_8125 = relay.divide(uop_8117.astype('float32'), relay.reshape(call_8116.astype('float32'), relay.shape_of(uop_8117))) # shape=(110, 4)
uop_8126 = relay.acos(uop_8117.astype('float64')) # shape=(110, 4)
uop_8132 = relay.log(bop_8090.astype('float64')) # shape=(15, 10, 11)
func_4346_call = mod.get_global_var('func_4346')
func_4349_call = mutated_mod.get_global_var('func_4349')
var_8137 = relay.var("var_8137", dtype = "float64", shape = (936,))#candidate|8137|(936,)|var|float64
call_8136 = relay.TupleGetItem(func_4346_call(relay.reshape(var_8137.astype('float64'), [13, 6, 12])), 1)
call_8138 = relay.TupleGetItem(func_4349_call(relay.reshape(var_8137.astype('float64'), [13, 6, 12])), 1)
func_5378_call = mod.get_global_var('func_5378')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_8141 = relay.TupleGetItem(func_5378_call(), 1)
call_8142 = relay.TupleGetItem(func_5380_call(), 1)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_8143 = func_1544_call()
call_8144 = func_1544_call()
func_319_call = mod.get_global_var('func_319')
func_321_call = mutated_mod.get_global_var('func_321')
call_8148 = relay.TupleGetItem(func_319_call(), 0)
call_8149 = relay.TupleGetItem(func_321_call(), 0)
uop_8154 = relay.atanh(const_8095.astype('float64')) # shape=(110, 4)
var_8159 = relay.var("var_8159", dtype = "float64", shape = (110, 4))#candidate|8159|(110, 4)|var|float64
bop_8160 = relay.add(uop_8126.astype('uint16'), relay.reshape(var_8159.astype('uint16'), relay.shape_of(uop_8126))) # shape=(110, 4)
bop_8165 = relay.divide(var_8088.astype('float64'), relay.reshape(bop_8090.astype('float64'), relay.shape_of(var_8088))) # shape=(15, 10, 11)
output = relay.Tuple([bop_8098,call_8107,bop_8122,uop_8132,call_8136,var_8137,call_8141,call_8143,call_8148,uop_8154,bop_8160,bop_8165,])
output2 = relay.Tuple([bop_8101,call_8108,bop_8125,uop_8132,call_8138,var_8137,call_8142,call_8144,call_8149,uop_8154,bop_8160,bop_8165,])
F = relay.Function([var_8088,var_8089,var_8137,var_8159,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8088,var_8089,var_8137,var_8159,], output2)
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
