import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_10 = relay.var("var_10", dtype = "float64", shape = (1, 1, 9))#candidate|10|(1, 1, 9)|var|float64
uop_11 = relay.log10(var_10.astype('float64')) # shape=(1, 1, 9)
uop_18 = relay.log2(uop_11.astype('float32')) # shape=(1, 1, 9)
output = relay.Tuple([uop_18,])
output2 = relay.Tuple([uop_18,])
func_20 = relay.Function([var_10,], output)
mod['func_20'] = func_20
mod = relay.transform.InferType()(mod)
var_21 = relay.var("var_21", dtype = "float64", shape = (1, 1, 9))#candidate|21|(1, 1, 9)|var|float64
output = func_20(var_21)
func_22 = relay.Function([var_21], output)
mutated_mod['func_22'] = func_22
mutated_mod = relay.transform.InferType()(mutated_mod)
const_374 = relay.const([[[-4.643529,-2.105452,0.100014,-4.572385,1.257536,5.575362,-8.766343],[-9.122879,2.531819,3.979434,-8.099594,9.949755,9.063685,-7.266842]],[[-6.789030,-8.403099,1.058911,-1.951395,7.720586,9.848764,-7.426464],[-5.407919,7.250121,-2.656776,0.427351,2.011879,5.770711,4.394800]],[[-5.007303,4.262397,9.915630,-0.797926,-7.697050,5.518444,8.334495],[-9.607531,5.153326,-5.438030,8.020122,4.084921,9.691868,-5.748192]],[[7.302967,4.174487,3.556367,5.290064,6.905549,-4.611538,-6.424287],[3.035117,-2.827665,-6.002219,-6.041934,-3.606842,5.221940,-1.769780]],[[-1.097540,0.459409,-2.149646,9.625088,3.108226,-9.459850,-2.946302],[-6.038362,-0.461447,-5.273015,1.437426,-7.717788,-4.167248,-9.633137]],[[2.947875,-8.021862,3.026103,9.719240,-0.099933,-9.841862,1.860938],[-7.167295,2.746884,8.561697,9.763880,-8.118920,-0.815473,-6.153823]],[[5.838467,-4.918427,-1.117246,-5.610975,-3.521960,9.410830,-0.577937],[-8.388836,4.385979,-1.041270,7.810890,-0.045602,7.156901,1.289825]],[[-4.958595,-8.857234,-8.433369,-4.649371,0.159027,5.378945,-4.082428],[7.044764,-5.570190,9.037527,-3.964367,-0.218818,1.794594,-9.131861]],[[8.905727,-0.756210,-6.034804,7.784067,8.070287,9.644178,-1.380527],[-6.918352,5.647254,9.604918,2.334039,3.343036,-2.952658,5.697419]],[[6.051719,3.822117,6.103201,-8.537292,-2.591122,9.036786,4.417053],[5.454256,2.627757,-0.136827,2.194317,-9.545241,-8.429448,-6.382092]],[[4.199970,-7.559386,-0.493450,3.938818,6.426129,3.094283,4.238512],[0.606248,7.127903,-8.429858,-2.412439,8.412836,-6.833179,-0.886594]],[[-2.089995,-2.455988,-5.050453,-6.435208,-5.629538,2.514920,8.215609],[8.018369,6.246203,2.355480,7.726947,1.514484,-8.798329,8.845835]],[[-8.853278,-9.670441,9.497005,-6.305393,7.655859,-0.054142,-3.323718],[-1.571267,-3.034272,-9.238616,-2.204723,-5.306467,6.926318,-2.143221]]], dtype = "float64")#candidate|374|(13, 2, 7)|const|float64
uop_375 = relay.sinh(const_374.astype('float64')) # shape=(13, 2, 7)
bop_378 = relay.power(uop_375.astype('float32'), relay.reshape(const_374.astype('float32'), relay.shape_of(uop_375))) # shape=(13, 2, 7)
func_20_call = mod.get_global_var('func_20')
func_22_call = mutated_mod.get_global_var('func_22')
const_383 = relay.const([-3.043715,-5.257384,-8.927846,0.241202,-2.968143,0.443601,4.061304,2.940879,-5.119442], dtype = "float64")#candidate|383|(9,)|const|float64
call_382 = relay.TupleGetItem(func_20_call(relay.reshape(const_383.astype('float64'), [1, 1, 9])), 0)
call_384 = relay.TupleGetItem(func_22_call(relay.reshape(const_383.astype('float64'), [1, 1, 9])), 0)
output = relay.Tuple([bop_378,call_382,const_383,])
output2 = relay.Tuple([bop_378,call_384,const_383,])
func_411 = relay.Function([], output)
mod['func_411'] = func_411
mod = relay.transform.InferType()(mod)
mutated_mod['func_411'] = func_411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_411_call = mutated_mod.get_global_var('func_411')
call_412 = func_411_call()
output = call_412
func_413 = relay.Function([], output)
mutated_mod['func_413'] = func_413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_449 = relay.var("var_449", dtype = "bool", shape = ())#candidate|449|()|var|bool
var_450 = relay.var("var_450", dtype = "bool", shape = (2, 13, 11))#candidate|450|(2, 13, 11)|var|bool
bop_451 = relay.logical_or(var_449.astype('bool'), var_450.astype('bool')) # shape=(2, 13, 11)
bop_459 = relay.not_equal(bop_451.astype('bool'), relay.reshape(var_450.astype('bool'), relay.shape_of(bop_451))) # shape=(2, 13, 11)
output = relay.Tuple([bop_459,])
output2 = relay.Tuple([bop_459,])
func_477 = relay.Function([var_449,var_450,], output)
mod['func_477'] = func_477
mod = relay.transform.InferType()(mod)
var_478 = relay.var("var_478", dtype = "bool", shape = ())#candidate|478|()|var|bool
var_479 = relay.var("var_479", dtype = "bool", shape = (2, 13, 11))#candidate|479|(2, 13, 11)|var|bool
output = func_477(var_478,var_479,)
func_480 = relay.Function([var_478,var_479,], output)
mutated_mod['func_480'] = func_480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_488 = relay.TupleGetItem(func_411_call(), 2)
call_489 = relay.TupleGetItem(func_413_call(), 2)
func_20_call = mod.get_global_var('func_20')
func_22_call = mutated_mod.get_global_var('func_22')
call_505 = relay.TupleGetItem(func_20_call(relay.reshape(call_488.astype('float64'), [1, 1, 9])), 0)
call_506 = relay.TupleGetItem(func_22_call(relay.reshape(call_488.astype('float64'), [1, 1, 9])), 0)
func_477_call = mod.get_global_var('func_477')
func_480_call = mutated_mod.get_global_var('func_480')
var_518 = relay.var("var_518", dtype = "bool", shape = ())#candidate|518|()|var|bool
const_519 = relay.const([True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True], dtype = "bool")#candidate|519|(286,)|const|bool
call_517 = relay.TupleGetItem(func_477_call(relay.reshape(var_518.astype('bool'), []), relay.reshape(const_519.astype('bool'), [2, 13, 11]), ), 0)
call_520 = relay.TupleGetItem(func_480_call(relay.reshape(var_518.astype('bool'), []), relay.reshape(const_519.astype('bool'), [2, 13, 11]), ), 0)
func_477_call = mod.get_global_var('func_477')
func_480_call = mutated_mod.get_global_var('func_480')
call_521 = relay.TupleGetItem(func_477_call(relay.reshape(var_518.astype('bool'), []), relay.reshape(call_517.astype('bool'), [2, 13, 11]), ), 0)
call_522 = relay.TupleGetItem(func_480_call(relay.reshape(var_518.astype('bool'), []), relay.reshape(call_517.astype('bool'), [2, 13, 11]), ), 0)
output = relay.Tuple([call_488,call_505,call_517,var_518,const_519,call_521,])
output2 = relay.Tuple([call_489,call_506,call_520,var_518,const_519,call_522,])
func_523 = relay.Function([var_518,], output)
mod['func_523'] = func_523
mod = relay.transform.InferType()(mod)
var_524 = relay.var("var_524", dtype = "bool", shape = ())#candidate|524|()|var|bool
output = func_523(var_524)
func_525 = relay.Function([var_524], output)
mutated_mod['func_525'] = func_525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_530 = relay.TupleGetItem(func_411_call(), 1)
call_531 = relay.TupleGetItem(func_413_call(), 1)
output = relay.Tuple([call_530,])
output2 = relay.Tuple([call_531,])
func_557 = relay.Function([], output)
mod['func_557'] = func_557
mod = relay.transform.InferType()(mod)
mutated_mod['func_557'] = func_557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_557_call = mutated_mod.get_global_var('func_557')
call_558 = func_557_call()
output = call_558
func_559 = relay.Function([], output)
mutated_mod['func_559'] = func_559
mutated_mod = relay.transform.InferType()(mutated_mod)
const_560 = relay.const([[[9.663117,-4.958879,-5.111802,-9.283924,-1.645492,7.310829,-3.996744,5.179505,0.549314,-7.530041,2.803737,-2.736183,9.573348,-6.748880],[0.923202,-8.440901,-5.217314,-8.179563,-3.558087,0.016566,4.885500,7.804076,-7.337803,5.789605,2.866756,-4.547949,-1.862551,8.701813],[-8.383044,-4.405043,9.403838,-7.344014,0.462416,0.151363,4.162658,-1.350345,1.899123,-8.736663,-4.785800,3.506710,-1.648727,-9.982693]],[[-2.330014,-5.485497,0.456669,4.393384,-4.804045,-0.212362,-0.686852,0.546651,-7.345487,-6.578462,8.826932,-4.708108,-4.764252,3.748309],[5.085882,-5.428301,-3.464587,-5.630098,9.715950,-3.336151,1.925381,0.663254,-2.177008,9.089574,-9.149686,-3.406720,0.940713,3.419345],[-5.986619,-4.370373,-1.785599,-9.254522,8.411995,8.723630,-2.660817,-6.909550,-1.699352,8.528625,6.991063,-1.835466,5.684417,6.382568]],[[7.119378,-1.090614,-1.896638,7.896933,2.608426,0.442897,-3.243452,2.225091,-4.747129,-4.480669,9.905046,-3.958613,-3.089399,-0.592535],[3.584097,-2.682015,-7.410919,6.413736,8.394900,-2.285000,-7.644417,-9.157652,-5.151178,8.184044,3.305160,8.469341,3.056914,0.636657],[-9.124025,4.250072,-9.917367,-5.731026,7.931649,2.345772,-3.744200,4.868119,6.872280,3.385439,-2.660318,-2.393132,-9.911741,-2.699477]],[[0.393054,-3.111584,-1.671676,-8.035524,7.441156,1.067776,-2.513490,-8.193888,-0.580510,0.740402,7.704802,3.854665,0.385817,1.177402],[-8.663027,0.652561,-0.459729,0.849559,-5.456147,6.087106,0.399049,-7.310785,1.370592,-0.423312,-3.989558,7.807150,6.400676,1.491426],[-7.273197,-6.190954,9.006595,8.112279,9.751719,-2.933927,-8.931965,-3.442589,-7.117281,8.628564,7.799056,-6.549675,6.568324,9.489354]],[[-4.567602,3.732055,8.627652,7.667331,5.869993,-2.430455,-7.833011,-5.844424,-6.672831,-5.479131,7.121249,-3.484748,2.077500,1.113139],[-9.969062,3.320742,5.471194,-6.620876,9.269503,1.466771,-2.308180,9.719162,-4.231133,1.573643,-7.977937,-7.787958,4.159432,-9.467977],[4.271081,4.792368,-5.718863,-5.875963,0.791015,1.971204,0.832290,4.005984,-4.391237,-0.524158,7.845799,-1.461959,7.152312,2.738811]]], dtype = "float32")#candidate|560|(5, 3, 14)|const|float32
uop_561 = relay.cos(const_560.astype('float32')) # shape=(5, 3, 14)
uop_566 = relay.atanh(uop_561.astype('float64')) # shape=(5, 3, 14)
func_523_call = mod.get_global_var('func_523')
func_525_call = mutated_mod.get_global_var('func_525')
const_572 = relay.const(False, dtype = "bool")#candidate|572|()|const|bool
call_571 = relay.TupleGetItem(func_523_call(relay.reshape(const_572.astype('bool'), [])), 5)
call_573 = relay.TupleGetItem(func_525_call(relay.reshape(const_572.astype('bool'), [])), 5)
output = relay.Tuple([uop_566,call_571,const_572,])
output2 = relay.Tuple([uop_566,call_573,const_572,])
func_574 = relay.Function([], output)
mod['func_574'] = func_574
mod = relay.transform.InferType()(mod)
output = func_574()
func_575 = relay.Function([], output)
mutated_mod['func_575'] = func_575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_590 = relay.TupleGetItem(func_557_call(), 0)
call_591 = relay.TupleGetItem(func_559_call(), 0)
output = relay.Tuple([call_590,])
output2 = relay.Tuple([call_591,])
func_602 = relay.Function([], output)
mod['func_602'] = func_602
mod = relay.transform.InferType()(mod)
output = func_602()
func_603 = relay.Function([], output)
mutated_mod['func_603'] = func_603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_632 = relay.TupleGetItem(func_574_call(), 2)
call_633 = relay.TupleGetItem(func_575_call(), 2)
output = call_632
output2 = call_633
func_663 = relay.Function([], output)
mod['func_663'] = func_663
mod = relay.transform.InferType()(mod)
output = func_663()
func_664 = relay.Function([], output)
mutated_mod['func_664'] = func_664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_722 = relay.TupleGetItem(func_411_call(), 0)
call_723 = relay.TupleGetItem(func_413_call(), 0)
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_728 = relay.TupleGetItem(func_557_call(), 0)
call_729 = relay.TupleGetItem(func_559_call(), 0)
output = relay.Tuple([call_722,call_728,])
output2 = relay.Tuple([call_723,call_729,])
func_745 = relay.Function([], output)
mod['func_745'] = func_745
mod = relay.transform.InferType()(mod)
output = func_745()
func_746 = relay.Function([], output)
mutated_mod['func_746'] = func_746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_602_call = mod.get_global_var('func_602')
func_603_call = mutated_mod.get_global_var('func_603')
call_788 = relay.TupleGetItem(func_602_call(), 0)
call_789 = relay.TupleGetItem(func_603_call(), 0)
output = relay.Tuple([call_788,])
output2 = relay.Tuple([call_789,])
func_802 = relay.Function([], output)
mod['func_802'] = func_802
mod = relay.transform.InferType()(mod)
output = func_802()
func_803 = relay.Function([], output)
mutated_mod['func_803'] = func_803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_832 = relay.TupleGetItem(func_557_call(), 0)
call_833 = relay.TupleGetItem(func_559_call(), 0)
func_802_call = mod.get_global_var('func_802')
func_803_call = mutated_mod.get_global_var('func_803')
call_838 = relay.TupleGetItem(func_802_call(), 0)
call_839 = relay.TupleGetItem(func_803_call(), 0)
func_20_call = mod.get_global_var('func_20')
func_22_call = mutated_mod.get_global_var('func_22')
call_846 = relay.TupleGetItem(func_20_call(relay.reshape(call_838.astype('float64'), [1, 1, 9])), 0)
call_847 = relay.TupleGetItem(func_22_call(relay.reshape(call_838.astype('float64'), [1, 1, 9])), 0)
var_854 = relay.var("var_854", dtype = "float32", shape = (1, 5, 9))#candidate|854|(1, 5, 9)|var|float32
bop_855 = relay.bitwise_and(call_838.astype('int32'), var_854.astype('int32')) # shape=(1, 5, 9)
bop_858 = relay.bitwise_and(call_839.astype('int32'), var_854.astype('int32')) # shape=(1, 5, 9)
uop_868 = relay.acos(call_838.astype('float64')) # shape=(1, 1, 9)
uop_870 = relay.acos(call_839.astype('float64')) # shape=(1, 1, 9)
func_663_call = mod.get_global_var('func_663')
func_664_call = mutated_mod.get_global_var('func_664')
call_874 = func_663_call()
call_875 = func_663_call()
bop_884 = relay.divide(call_874.astype('float64'), bop_855.astype('float64')) # shape=(1, 5, 9)
bop_887 = relay.divide(call_875.astype('float64'), bop_858.astype('float64')) # shape=(1, 5, 9)
func_802_call = mod.get_global_var('func_802')
func_803_call = mutated_mod.get_global_var('func_803')
call_889 = relay.TupleGetItem(func_802_call(), 0)
call_890 = relay.TupleGetItem(func_803_call(), 0)
bop_895 = relay.logical_or(uop_868.astype('bool'), bop_884.astype('bool')) # shape=(1, 5, 9)
bop_898 = relay.logical_or(uop_870.astype('bool'), bop_887.astype('bool')) # shape=(1, 5, 9)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_899 = relay.TupleGetItem(func_574_call(), 2)
call_900 = relay.TupleGetItem(func_575_call(), 2)
bop_901 = relay.greater(bop_895.astype('bool'), relay.reshape(bop_855.astype('bool'), relay.shape_of(bop_895))) # shape=(1, 5, 9)
bop_904 = relay.greater(bop_898.astype('bool'), relay.reshape(bop_858.astype('bool'), relay.shape_of(bop_898))) # shape=(1, 5, 9)
output = relay.Tuple([call_832,call_846,call_889,call_899,bop_901,])
output2 = relay.Tuple([call_833,call_847,call_890,call_900,bop_904,])
func_906 = relay.Function([var_854,], output)
mod['func_906'] = func_906
mod = relay.transform.InferType()(mod)
var_907 = relay.var("var_907", dtype = "float32", shape = (1, 5, 9))#candidate|907|(1, 5, 9)|var|float32
output = func_906(var_907)
func_908 = relay.Function([var_907], output)
mutated_mod['func_908'] = func_908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_910 = relay.TupleGetItem(func_574_call(), 2)
call_911 = relay.TupleGetItem(func_575_call(), 2)
output = call_910
output2 = call_911
func_912 = relay.Function([], output)
mod['func_912'] = func_912
mod = relay.transform.InferType()(mod)
output = func_912()
func_913 = relay.Function([], output)
mutated_mod['func_913'] = func_913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_745_call = mod.get_global_var('func_745')
func_746_call = mutated_mod.get_global_var('func_746')
call_968 = relay.TupleGetItem(func_745_call(), 0)
call_969 = relay.TupleGetItem(func_746_call(), 0)
const_970 = relay.const([[[3.970735,-9.892877,6.495254,7.221438,5.558380,-5.407673,-0.193767],[0.876406,4.943521,4.851348,-7.418188,4.434632,7.470944,8.213457]],[[-5.606324,7.060052,-0.338190,9.629953,7.538681,9.143455,2.075314],[-9.697443,-7.965126,-4.366395,9.569259,-8.263024,0.315006,-7.146522]],[[-8.089989,-5.364741,-3.570128,-4.287517,7.873188,4.537283,-0.986709],[8.029945,-2.699752,0.142807,5.926057,-9.421258,4.165442,-0.009545]],[[-7.792314,-0.345778,-7.679895,8.329213,-8.247694,-6.713088,1.419866],[-9.091567,-0.337173,3.911972,-2.833523,2.665895,-2.968533,-5.161473]],[[-6.776159,-2.057819,2.487349,3.553096,3.367507,4.850072,-9.637553],[2.467925,1.541189,4.800479,-3.029301,-2.813116,3.033806,-1.673349]],[[6.278447,-4.165621,-6.545948,-0.014432,0.825981,2.025833,-2.140284],[-8.140911,-7.902108,-7.682237,4.273672,1.218140,-2.737288,-3.011528]],[[6.505861,1.289116,-5.084166,5.551415,-8.915522,-4.331698,6.421025],[-8.044109,-1.578706,6.775075,-0.967020,-4.078308,5.075094,0.819238]],[[5.327981,-7.370576,3.096967,4.606898,2.688090,-3.484725,-4.675796],[8.797975,-4.261600,0.092069,-9.661757,-7.937433,-8.128341,-8.898025]],[[-5.431496,6.303765,-3.124564,3.982163,8.601678,7.824181,7.188231],[-5.834016,-8.843269,8.081218,0.212149,-2.525078,4.841142,8.033358]],[[2.783539,-4.554013,0.509835,-8.744939,0.018253,5.207673,-7.377080],[7.989243,-4.197598,-9.805270,4.214867,-5.476705,-8.483106,-8.052224]],[[9.530530,-6.706705,5.210466,-2.977431,-4.185556,-7.406265,-9.729974],[0.157546,-8.129995,-2.432607,-7.919513,-0.279961,3.952864,7.945445]],[[8.604840,7.495584,6.698744,9.065766,-9.145649,3.315433,-2.091414],[-9.840301,-5.378226,-3.200434,-5.206369,5.508345,2.714585,-0.467857]],[[-5.004222,-4.767298,8.603713,-3.858824,0.099109,-9.648906,-6.205567],[4.561371,2.031261,5.393221,5.445990,8.037094,1.574922,-5.373676]]], dtype = "float32")#candidate|970|(13, 2, 7)|const|float32
bop_971 = relay.logical_or(call_968.astype('bool'), relay.reshape(const_970.astype('bool'), relay.shape_of(call_968))) # shape=(13, 2, 7)
bop_974 = relay.logical_or(call_969.astype('bool'), relay.reshape(const_970.astype('bool'), relay.shape_of(call_969))) # shape=(13, 2, 7)
output = relay.Tuple([bop_971,])
output2 = relay.Tuple([bop_974,])
func_975 = relay.Function([], output)
mod['func_975'] = func_975
mod = relay.transform.InferType()(mod)
output = func_975()
func_976 = relay.Function([], output)
mutated_mod['func_976'] = func_976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_981 = relay.TupleGetItem(func_975_call(), 0)
call_982 = relay.TupleGetItem(func_976_call(), 0)
output = call_981
output2 = call_982
func_983 = relay.Function([], output)
mod['func_983'] = func_983
mod = relay.transform.InferType()(mod)
mutated_mod['func_983'] = func_983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_983_call = mutated_mod.get_global_var('func_983')
call_984 = func_983_call()
output = call_984
func_985 = relay.Function([], output)
mutated_mod['func_985'] = func_985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_992 = relay.TupleGetItem(func_574_call(), 1)
call_993 = relay.TupleGetItem(func_575_call(), 1)
func_20_call = mod.get_global_var('func_20')
func_22_call = mutated_mod.get_global_var('func_22')
const_996 = relay.const([[-5.969809,7.531118,-1.657831],[-4.247395,-8.393190,-4.226790],[2.643110,6.606606,-1.974909]], dtype = "float64")#candidate|996|(3, 3)|const|float64
call_995 = relay.TupleGetItem(func_20_call(relay.reshape(const_996.astype('float64'), [1, 1, 9])), 0)
call_997 = relay.TupleGetItem(func_22_call(relay.reshape(const_996.astype('float64'), [1, 1, 9])), 0)
output = relay.Tuple([call_992,call_995,const_996,])
output2 = relay.Tuple([call_993,call_997,const_996,])
func_1004 = relay.Function([], output)
mod['func_1004'] = func_1004
mod = relay.transform.InferType()(mod)
output = func_1004()
func_1005 = relay.Function([], output)
mutated_mod['func_1005'] = func_1005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_745_call = mod.get_global_var('func_745')
func_746_call = mutated_mod.get_global_var('func_746')
call_1113 = relay.TupleGetItem(func_745_call(), 0)
call_1114 = relay.TupleGetItem(func_746_call(), 0)
func_602_call = mod.get_global_var('func_602')
func_603_call = mutated_mod.get_global_var('func_603')
call_1115 = relay.TupleGetItem(func_602_call(), 0)
call_1116 = relay.TupleGetItem(func_603_call(), 0)
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_1125 = relay.TupleGetItem(func_557_call(), 0)
call_1126 = relay.TupleGetItem(func_559_call(), 0)
func_906_call = mod.get_global_var('func_906')
func_908_call = mutated_mod.get_global_var('func_908')
var_1131 = relay.var("var_1131", dtype = "float32", shape = (1, 45))#candidate|1131|(1, 45)|var|float32
call_1130 = relay.TupleGetItem(func_906_call(relay.reshape(var_1131.astype('float32'), [1, 5, 9])), 3)
call_1132 = relay.TupleGetItem(func_908_call(relay.reshape(var_1131.astype('float32'), [1, 5, 9])), 3)
output = relay.Tuple([call_1113,call_1115,call_1125,call_1130,var_1131,])
output2 = relay.Tuple([call_1114,call_1116,call_1126,call_1132,var_1131,])
func_1133 = relay.Function([var_1131,], output)
mod['func_1133'] = func_1133
mod = relay.transform.InferType()(mod)
mutated_mod['func_1133'] = func_1133
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1134 = relay.var("var_1134", dtype = "float32", shape = (1, 45))#candidate|1134|(1, 45)|var|float32
func_1133_call = mutated_mod.get_global_var('func_1133')
call_1135 = func_1133_call(var_1134)
output = call_1135
func_1136 = relay.Function([var_1134], output)
mutated_mod['func_1136'] = func_1136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_1141 = relay.TupleGetItem(func_411_call(), 2)
call_1142 = relay.TupleGetItem(func_413_call(), 2)
output = relay.Tuple([call_1141,])
output2 = relay.Tuple([call_1142,])
func_1167 = relay.Function([], output)
mod['func_1167'] = func_1167
mod = relay.transform.InferType()(mod)
mutated_mod['func_1167'] = func_1167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mutated_mod.get_global_var('func_1167')
call_1168 = func_1167_call()
output = call_1168
func_1169 = relay.Function([], output)
mutated_mod['func_1169'] = func_1169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_1180 = relay.TupleGetItem(func_411_call(), 2)
call_1181 = relay.TupleGetItem(func_413_call(), 2)
output = call_1180
output2 = call_1181
func_1186 = relay.Function([], output)
mod['func_1186'] = func_1186
mod = relay.transform.InferType()(mod)
output = func_1186()
func_1187 = relay.Function([], output)
mutated_mod['func_1187'] = func_1187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_745_call = mod.get_global_var('func_745')
func_746_call = mutated_mod.get_global_var('func_746')
call_1338 = relay.TupleGetItem(func_745_call(), 0)
call_1339 = relay.TupleGetItem(func_746_call(), 0)
const_1346 = relay.const([[[-4.870144,-3.548302,3.027754,-3.349179,-0.314500,-1.312775,6.775571],[7.553552,-9.905266,-5.682237,1.721418,5.415772,5.538030,3.990796]],[[-8.018178,-2.937986,-5.802054,4.983590,6.754729,1.162531,-4.187572],[-9.135992,-6.185996,6.177225,1.342885,-9.234846,8.497869,6.278689]],[[-7.951502,-4.188766,-7.739512,5.009760,8.004753,-0.264996,9.444704],[-2.751038,3.224905,6.677633,1.945273,-0.613084,-1.294636,5.743023]],[[-7.728460,-4.578801,-4.445953,5.063802,-8.433257,6.380971,-6.051798],[-5.725254,3.001664,1.089891,-1.099060,-4.111603,1.606727,-3.220852]],[[7.893188,8.254693,-9.310411,4.181912,-7.537042,6.469095,7.821269],[-4.513936,6.773058,1.235010,-8.522366,3.428609,-1.868724,-6.158175]],[[4.077463,4.550440,-6.906602,-7.064667,1.504217,6.924470,5.349329],[-2.722609,5.440344,-7.392402,7.183009,3.676766,-8.873117,-5.885375]],[[-7.470308,-9.723583,1.568657,0.304793,-7.431732,4.312468,0.417667],[-3.005791,0.165028,4.976501,9.315603,7.975051,-0.722917,-5.365289]],[[-8.520630,0.775457,6.852339,-8.888234,5.905340,2.026714,5.647904],[9.082267,5.628617,6.131881,-8.243235,-7.320901,-7.475356,7.099944]],[[-2.455326,6.869963,-6.432520,-6.994131,-7.024190,7.160216,-3.177809],[-8.755616,5.578691,-4.680863,1.538249,1.919103,-7.055460,3.876242]],[[-4.537195,3.233750,8.796780,4.958899,4.886935,8.500617,-1.839633],[-1.207501,6.279552,-3.776676,-1.320107,-0.406321,5.400818,-9.418376]],[[5.313512,-7.562018,-0.524663,-6.486020,4.129033,6.365325,9.058657],[-3.207375,5.098742,-1.932625,3.461353,1.649813,1.825553,1.550600]],[[-2.677138,5.578990,-6.095429,4.123089,3.578968,-3.637113,3.780518],[-6.505981,-2.511171,-1.812125,2.346099,7.505608,0.390056,-6.538241]],[[-8.936723,7.124239,9.558685,-1.255134,3.699488,-0.260797,1.436141],[4.316719,4.247549,-8.916111,-2.763028,9.001037,3.851974,0.775870]]], dtype = "float32")#candidate|1346|(13, 2, 7)|const|float32
bop_1347 = relay.logical_and(call_1338.astype('bool'), relay.reshape(const_1346.astype('bool'), relay.shape_of(call_1338))) # shape=(13, 2, 7)
bop_1350 = relay.logical_and(call_1339.astype('bool'), relay.reshape(const_1346.astype('bool'), relay.shape_of(call_1339))) # shape=(13, 2, 7)
uop_1357 = relay.rsqrt(const_1346.astype('float32')) # shape=(13, 2, 7)
func_602_call = mod.get_global_var('func_602')
func_603_call = mutated_mod.get_global_var('func_603')
call_1367 = relay.TupleGetItem(func_602_call(), 0)
call_1368 = relay.TupleGetItem(func_603_call(), 0)
func_802_call = mod.get_global_var('func_802')
func_803_call = mutated_mod.get_global_var('func_803')
call_1375 = relay.TupleGetItem(func_802_call(), 0)
call_1376 = relay.TupleGetItem(func_803_call(), 0)
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_1378 = relay.TupleGetItem(func_557_call(), 0)
call_1379 = relay.TupleGetItem(func_559_call(), 0)
bop_1393 = relay.bitwise_or(call_1367.astype('int64'), relay.reshape(call_1378.astype('int64'), relay.shape_of(call_1367))) # shape=(1, 1, 9)
bop_1396 = relay.bitwise_or(call_1368.astype('int64'), relay.reshape(call_1379.astype('int64'), relay.shape_of(call_1368))) # shape=(1, 1, 9)
bop_1409 = relay.mod(uop_1357.astype('float32'), relay.reshape(bop_1347.astype('float32'), relay.shape_of(uop_1357))) # shape=(13, 2, 7)
bop_1412 = relay.mod(uop_1357.astype('float32'), relay.reshape(bop_1350.astype('float32'), relay.shape_of(uop_1357))) # shape=(13, 2, 7)
output = relay.Tuple([call_1375,bop_1393,bop_1409,])
output2 = relay.Tuple([call_1376,bop_1396,bop_1412,])
func_1415 = relay.Function([], output)
mod['func_1415'] = func_1415
mod = relay.transform.InferType()(mod)
mutated_mod['func_1415'] = func_1415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1415_call = mutated_mod.get_global_var('func_1415')
call_1416 = func_1415_call()
output = call_1416
func_1417 = relay.Function([], output)
mutated_mod['func_1417'] = func_1417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_663_call = mod.get_global_var('func_663')
func_664_call = mutated_mod.get_global_var('func_664')
call_1440 = func_663_call()
call_1441 = func_663_call()
func_20_call = mod.get_global_var('func_20')
func_22_call = mutated_mod.get_global_var('func_22')
const_1446 = relay.const([4.508762,9.205771,-9.593575,7.733453,0.920714,-7.352239,-8.482313,5.093955,7.578764], dtype = "float64")#candidate|1446|(9,)|const|float64
call_1445 = relay.TupleGetItem(func_20_call(relay.reshape(const_1446.astype('float64'), [1, 1, 9])), 0)
call_1447 = relay.TupleGetItem(func_22_call(relay.reshape(const_1446.astype('float64'), [1, 1, 9])), 0)
bop_1461 = relay.floor_mod(call_1445.astype('float32'), relay.reshape(const_1446.astype('float32'), relay.shape_of(call_1445))) # shape=(1, 1, 9)
bop_1464 = relay.floor_mod(call_1447.astype('float32'), relay.reshape(const_1446.astype('float32'), relay.shape_of(call_1447))) # shape=(1, 1, 9)
uop_1472 = relay.sin(bop_1461.astype('float64')) # shape=(1, 1, 9)
uop_1474 = relay.sin(bop_1464.astype('float64')) # shape=(1, 1, 9)
output = relay.Tuple([call_1440,uop_1472,])
output2 = relay.Tuple([call_1441,uop_1474,])
func_1480 = relay.Function([], output)
mod['func_1480'] = func_1480
mod = relay.transform.InferType()(mod)
mutated_mod['func_1480'] = func_1480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1480_call = mutated_mod.get_global_var('func_1480')
call_1481 = func_1480_call()
output = call_1481
func_1482 = relay.Function([], output)
mutated_mod['func_1482'] = func_1482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1562 = relay.var("var_1562", dtype = "float32", shape = (13, 14, 15))#candidate|1562|(13, 14, 15)|var|float32
var_1563 = relay.var("var_1563", dtype = "float32", shape = (13, 14, 15))#candidate|1563|(13, 14, 15)|var|float32
bop_1564 = relay.floor_divide(var_1562.astype('float32'), relay.reshape(var_1563.astype('float32'), relay.shape_of(var_1562))) # shape=(13, 14, 15)
uop_1570 = relay.tan(var_1562.astype('float64')) # shape=(13, 14, 15)
uop_1585 = relay.asinh(var_1562.astype('float32')) # shape=(13, 14, 15)
func_745_call = mod.get_global_var('func_745')
func_746_call = mutated_mod.get_global_var('func_746')
call_1588 = relay.TupleGetItem(func_745_call(), 0)
call_1589 = relay.TupleGetItem(func_746_call(), 0)
output = relay.Tuple([bop_1564,uop_1570,uop_1585,call_1588,])
output2 = relay.Tuple([bop_1564,uop_1570,uop_1585,call_1589,])
func_1590 = relay.Function([var_1562,var_1563,], output)
mod['func_1590'] = func_1590
mod = relay.transform.InferType()(mod)
mutated_mod['func_1590'] = func_1590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mutated_mod.get_global_var('func_1590')
var_1592 = relay.var("var_1592", dtype = "float32", shape = (13, 14, 15))#candidate|1592|(13, 14, 15)|var|float32
var_1593 = relay.var("var_1593", dtype = "float32", shape = (13, 14, 15))#candidate|1593|(13, 14, 15)|var|float32
call_1591 = func_1590_call(var_1592,var_1593,)
output = call_1591
func_1594 = relay.Function([var_1592,var_1593,], output)
mutated_mod['func_1594'] = func_1594
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1609 = relay.var("var_1609", dtype = "float64", shape = (10, 5, 9))#candidate|1609|(10, 5, 9)|var|float64
uop_1610 = relay.sinh(var_1609.astype('float64')) # shape=(10, 5, 9)
bop_1614 = relay.floor_mod(uop_1610.astype('float64'), relay.reshape(var_1609.astype('float64'), relay.shape_of(uop_1610))) # shape=(10, 5, 9)
uop_1617 = relay.sin(bop_1614.astype('float32')) # shape=(10, 5, 9)
output = relay.Tuple([uop_1617,])
output2 = relay.Tuple([uop_1617,])
func_1620 = relay.Function([var_1609,], output)
mod['func_1620'] = func_1620
mod = relay.transform.InferType()(mod)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1621 = relay.var("var_1621", dtype = "float64", shape = (10, 5, 9))#candidate|1621|(10, 5, 9)|var|float64
func_1620_call = mutated_mod.get_global_var('func_1620')
call_1622 = func_1620_call(var_1621)
output = call_1622
func_1623 = relay.Function([var_1621], output)
mutated_mod['func_1623'] = func_1623
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1680 = relay.const([[[-2.186439,4.169238,7.672093,2.892855,4.825209,-5.342410,3.010163,-6.976039,-7.322737],[4.077855,-4.446634,3.698689,3.663599,3.238608,6.409500,1.623383,-2.322541,-4.239327],[-4.868133,-9.737266,0.868885,-7.530397,-3.388452,-6.538068,7.843609,8.737964,4.154410]],[[-9.105971,6.004119,3.720086,-4.985286,-5.178428,9.965025,3.440435,-5.134625,5.936483],[-3.535668,-2.557964,7.461557,-5.528140,-3.782624,-2.427861,-0.040271,2.108363,-3.297847],[-4.605332,7.051087,4.098661,-3.637631,-1.147940,-0.077072,-0.334539,8.935360,-4.952461]],[[1.330372,-1.564139,-5.277127,4.876071,9.690052,-3.975536,0.676287,-2.211702,9.860813],[-3.359726,-8.460034,-3.689522,-8.601747,-3.125074,9.231902,-9.651542,1.519554,6.280645],[9.776489,-4.392492,8.844256,4.950277,-6.560941,5.712070,9.168528,0.916353,-4.327588]],[[7.069165,-7.871140,-1.228711,-8.790852,-2.947977,9.348721,7.752702,-9.097948,2.234082],[-1.547952,-9.995482,7.398950,-0.591680,0.060675,-5.775021,9.941022,6.652676,5.539237],[1.536817,-8.199647,1.741040,1.888015,4.946067,7.332287,4.831079,4.690012,-0.856788]],[[5.154108,3.426357,-1.707374,-7.264165,4.687015,1.978822,-3.863194,-9.112954,-1.222766],[-0.463323,-7.032919,5.621429,4.316636,3.209559,-3.123211,4.531554,-6.466363,9.003423],[-8.670589,-1.688327,1.148120,9.742154,3.576492,-4.577093,1.024683,2.559947,-6.496338]],[[7.711014,-8.214223,-0.454719,-0.896590,-9.092601,8.491870,9.605829,-0.111092,9.878913],[4.056897,5.581817,1.793118,-6.607174,-9.759048,-7.136453,-1.786850,-1.149792,1.979127],[-1.762631,-3.608038,-7.626458,-9.901370,-4.111960,-3.534126,-2.994145,-8.407306,-7.365312]],[[9.516635,-2.818136,-6.897910,0.624509,7.283147,8.818870,-7.728028,-7.334366,0.671524],[-4.065813,0.684978,-9.782576,8.518299,5.198222,-3.120477,1.753298,5.602425,8.715950],[-3.154310,-2.115109,6.098607,-3.536962,0.445831,-8.663402,-7.469589,-2.123485,2.071092]],[[4.435747,6.353825,-2.380079,-8.063834,-0.281923,-2.861000,1.401886,-2.128957,-8.362290],[-3.559315,7.607711,0.699081,-4.278285,8.558898,8.171175,6.725067,7.232720,-1.632426],[-7.271730,5.313007,-6.373499,-7.399221,-7.445828,0.426501,-1.555802,-3.796409,-0.174732]],[[-3.931210,9.550391,5.967983,-9.139699,6.158483,-2.034966,-4.419562,-8.067259,4.813730],[0.884308,-5.799438,-2.839752,-3.476899,1.006861,-3.750015,-8.542315,-3.336496,-6.104986],[3.694010,-5.563665,-5.581831,-0.186593,7.426964,-7.592014,8.049241,9.264507,-0.804983]],[[9.600008,-8.463962,1.123140,-3.368252,1.531637,3.182729,7.204886,6.080112,8.827080],[-3.139451,-7.088790,-0.962545,-3.262596,-5.954647,5.165152,7.540555,4.670366,-0.742954],[-6.818578,-6.397944,6.761225,-5.539761,-1.934212,7.467949,2.035631,5.042164,4.860835]],[[5.340025,4.000214,6.095373,-7.116117,-7.311570,7.194349,-9.446182,8.465448,0.669583],[-5.908126,2.423281,6.137417,-6.908512,-5.254681,-6.753854,7.508949,2.777975,9.551802],[8.913784,5.770603,9.774268,-2.744738,3.442110,5.105200,0.851910,-3.439396,-1.239182]]], dtype = "float64")#candidate|1680|(11, 3, 9)|const|float64
uop_1681 = relay.exp(const_1680.astype('float64')) # shape=(11, 3, 9)
output = uop_1681
output2 = uop_1681
func_1690 = relay.Function([], output)
mod['func_1690'] = func_1690
mod = relay.transform.InferType()(mod)
mutated_mod['func_1690'] = func_1690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1690_call = mutated_mod.get_global_var('func_1690')
call_1691 = func_1690_call()
output = call_1691
func_1692 = relay.Function([], output)
mutated_mod['func_1692'] = func_1692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_663_call = mod.get_global_var('func_663')
func_664_call = mutated_mod.get_global_var('func_664')
call_1697 = func_663_call()
call_1698 = func_663_call()
output = call_1697
output2 = call_1698
func_1700 = relay.Function([], output)
mod['func_1700'] = func_1700
mod = relay.transform.InferType()(mod)
output = func_1700()
func_1701 = relay.Function([], output)
mutated_mod['func_1701'] = func_1701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_1713 = relay.TupleGetItem(func_975_call(), 0)
call_1714 = relay.TupleGetItem(func_976_call(), 0)
const_1754 = relay.const([[[False,False,False,False,True,False,True],[False,False,True,False,True,False,False]],[[True,False,True,True,True,True,True],[True,False,False,True,False,True,False]],[[False,False,True,False,False,True,False],[False,True,True,False,False,True,True]],[[True,True,True,False,True,True,False],[False,False,True,True,True,False,False]],[[True,True,True,True,True,False,True],[False,True,True,False,True,True,False]],[[True,False,True,False,True,True,False],[True,False,False,True,False,False,True]],[[True,False,True,False,True,False,True],[False,False,False,False,False,False,False]],[[True,True,True,False,True,False,False],[False,True,False,True,True,True,True]],[[False,True,False,True,True,True,False],[False,False,True,False,False,False,True]],[[False,False,True,True,True,False,True],[False,True,True,False,False,False,False]],[[False,True,True,False,False,True,True],[True,False,True,True,False,True,True]],[[True,True,False,True,True,False,True],[False,False,False,False,True,False,False]],[[False,False,False,False,True,True,False],[True,False,True,False,True,True,True]]], dtype = "bool")#candidate|1754|(13, 2, 7)|const|bool
bop_1755 = relay.greater_equal(call_1713.astype('bool'), relay.reshape(const_1754.astype('bool'), relay.shape_of(call_1713))) # shape=(13, 2, 7)
bop_1758 = relay.greater_equal(call_1714.astype('bool'), relay.reshape(const_1754.astype('bool'), relay.shape_of(call_1714))) # shape=(13, 2, 7)
output = relay.Tuple([bop_1755,])
output2 = relay.Tuple([bop_1758,])
func_1760 = relay.Function([], output)
mod['func_1760'] = func_1760
mod = relay.transform.InferType()(mod)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1761 = func_1760_call()
output = call_1761
func_1762 = relay.Function([], output)
mutated_mod['func_1762'] = func_1762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1480_call = mod.get_global_var('func_1480')
func_1482_call = mutated_mod.get_global_var('func_1482')
call_1783 = relay.TupleGetItem(func_1480_call(), 1)
call_1784 = relay.TupleGetItem(func_1482_call(), 1)
output = call_1783
output2 = call_1784
func_1785 = relay.Function([], output)
mod['func_1785'] = func_1785
mod = relay.transform.InferType()(mod)
mutated_mod['func_1785'] = func_1785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1785_call = mutated_mod.get_global_var('func_1785')
call_1786 = func_1785_call()
output = call_1786
func_1787 = relay.Function([], output)
mutated_mod['func_1787'] = func_1787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_1806 = relay.TupleGetItem(func_1167_call(), 0)
call_1807 = relay.TupleGetItem(func_1169_call(), 0)
output = relay.Tuple([call_1806,])
output2 = relay.Tuple([call_1807,])
func_1829 = relay.Function([], output)
mod['func_1829'] = func_1829
mod = relay.transform.InferType()(mod)
mutated_mod['func_1829'] = func_1829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1829_call = mutated_mod.get_global_var('func_1829')
call_1830 = func_1829_call()
output = call_1830
func_1831 = relay.Function([], output)
mutated_mod['func_1831'] = func_1831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_1838 = relay.TupleGetItem(func_1167_call(), 0)
call_1839 = relay.TupleGetItem(func_1169_call(), 0)
output = relay.Tuple([call_1838,])
output2 = relay.Tuple([call_1839,])
func_1846 = relay.Function([], output)
mod['func_1846'] = func_1846
mod = relay.transform.InferType()(mod)
output = func_1846()
func_1847 = relay.Function([], output)
mutated_mod['func_1847'] = func_1847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_983_call = mod.get_global_var('func_983')
func_985_call = mutated_mod.get_global_var('func_985')
call_1971 = func_983_call()
call_1972 = func_983_call()
func_477_call = mod.get_global_var('func_477')
func_480_call = mutated_mod.get_global_var('func_480')
const_2017 = relay.const(True, dtype = "bool")#candidate|2017|()|const|bool
const_2018 = relay.const([True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True], dtype = "bool")#candidate|2018|(286,)|const|bool
call_2016 = relay.TupleGetItem(func_477_call(relay.reshape(const_2017.astype('bool'), []), relay.reshape(const_2018.astype('bool'), [2, 13, 11]), ), 0)
call_2019 = relay.TupleGetItem(func_480_call(relay.reshape(const_2017.astype('bool'), []), relay.reshape(const_2018.astype('bool'), [2, 13, 11]), ), 0)
const_2021 = relay.const([[[True,True,False,True,False,False,False,True,True,True,False],[False,True,True,False,True,False,True,True,True,False,True],[False,True,False,False,True,False,True,False,False,True,True],[True,False,True,True,False,True,False,False,True,True,True],[False,True,True,False,False,False,False,False,True,False,False],[True,True,True,False,False,True,False,True,False,True,True],[False,False,False,True,True,False,False,False,True,True,True],[False,True,True,True,True,False,False,False,False,False,True],[True,False,True,False,False,True,False,False,False,False,False],[False,True,True,False,False,True,False,True,False,False,False],[False,True,False,False,False,False,False,False,True,True,False],[False,True,False,True,True,False,False,False,True,False,True],[False,True,True,False,True,False,False,True,True,False,True]],[[True,False,True,True,False,True,False,True,True,False,False],[True,False,False,False,False,False,True,False,True,True,True],[True,True,False,True,False,False,False,False,True,True,True],[False,False,True,True,False,True,False,True,True,True,True],[True,True,True,True,False,True,True,False,True,False,True],[True,True,True,True,False,False,False,True,True,False,False],[False,True,False,True,True,True,True,True,False,False,False],[True,False,True,True,True,True,False,True,False,True,False],[False,True,False,False,True,False,True,False,False,True,True],[False,True,True,False,False,False,False,False,False,False,False],[True,True,True,False,True,False,True,False,True,True,True],[True,True,True,True,False,True,True,True,False,False,False],[True,False,False,True,False,True,False,False,True,True,True]]], dtype = "bool")#candidate|2021|(2, 13, 11)|const|bool
bop_2022 = relay.greater(call_2016.astype('bool'), relay.reshape(const_2021.astype('bool'), relay.shape_of(call_2016))) # shape=(2, 13, 11)
bop_2025 = relay.greater(call_2019.astype('bool'), relay.reshape(const_2021.astype('bool'), relay.shape_of(call_2019))) # shape=(2, 13, 11)
uop_2026 = relay.cosh(call_2016.astype('float64')) # shape=(2, 13, 11)
uop_2028 = relay.cosh(call_2019.astype('float64')) # shape=(2, 13, 11)
func_912_call = mod.get_global_var('func_912')
func_913_call = mutated_mod.get_global_var('func_913')
call_2031 = func_912_call()
call_2032 = func_912_call()
func_602_call = mod.get_global_var('func_602')
func_603_call = mutated_mod.get_global_var('func_603')
call_2034 = relay.TupleGetItem(func_602_call(), 0)
call_2035 = relay.TupleGetItem(func_603_call(), 0)
var_2039 = relay.var("var_2039", dtype = "bool", shape = (286,))#candidate|2039|(286,)|var|bool
bop_2040 = relay.logical_and(const_2018.astype('bool'), relay.reshape(var_2039.astype('bool'), relay.shape_of(const_2018))) # shape=(286,)
output = relay.Tuple([call_1971,const_2017,bop_2022,uop_2026,call_2031,call_2034,bop_2040,])
output2 = relay.Tuple([call_1972,const_2017,bop_2025,uop_2028,call_2032,call_2035,bop_2040,])
func_2044 = relay.Function([var_2039,], output)
mod['func_2044'] = func_2044
mod = relay.transform.InferType()(mod)
mutated_mod['func_2044'] = func_2044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2045 = relay.var("var_2045", dtype = "bool", shape = (286,))#candidate|2045|(286,)|var|bool
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2046 = func_2044_call(var_2045)
output = call_2046
func_2047 = relay.Function([var_2045], output)
mutated_mod['func_2047'] = func_2047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_745_call = mod.get_global_var('func_745')
func_746_call = mutated_mod.get_global_var('func_746')
call_2087 = relay.TupleGetItem(func_745_call(), 1)
call_2088 = relay.TupleGetItem(func_746_call(), 1)
var_2099 = relay.var("var_2099", dtype = "float32", shape = (15, 9, 9))#candidate|2099|(15, 9, 9)|var|float32
bop_2100 = relay.greater_equal(call_2087.astype('bool'), var_2099.astype('bool')) # shape=(15, 9, 9)
bop_2103 = relay.greater_equal(call_2088.astype('bool'), var_2099.astype('bool')) # shape=(15, 9, 9)
output = bop_2100
output2 = bop_2103
func_2104 = relay.Function([var_2099,], output)
mod['func_2104'] = func_2104
mod = relay.transform.InferType()(mod)
var_2105 = relay.var("var_2105", dtype = "float32", shape = (15, 9, 9))#candidate|2105|(15, 9, 9)|var|float32
output = func_2104(var_2105)
func_2106 = relay.Function([var_2105], output)
mutated_mod['func_2106'] = func_2106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1700_call = mod.get_global_var('func_1700')
func_1701_call = mutated_mod.get_global_var('func_1701')
call_2143 = func_1700_call()
call_2144 = func_1700_call()
func_1760_call = mod.get_global_var('func_1760')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_2153 = relay.TupleGetItem(func_1760_call(), 0)
call_2154 = relay.TupleGetItem(func_1762_call(), 0)
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_2156 = relay.TupleGetItem(func_557_call(), 0)
call_2157 = relay.TupleGetItem(func_559_call(), 0)
var_2162 = relay.var("var_2162", dtype = "float32", shape = (10, 14, 9))#candidate|2162|(10, 14, 9)|var|float32
bop_2163 = relay.add(call_2156.astype('float64'), var_2162.astype('float64')) # shape=(10, 14, 9)
bop_2166 = relay.add(call_2157.astype('float64'), var_2162.astype('float64')) # shape=(10, 14, 9)
bop_2170 = relay.greater_equal(var_2162.astype('bool'), relay.reshape(bop_2163.astype('bool'), relay.shape_of(var_2162))) # shape=(10, 14, 9)
bop_2173 = relay.greater_equal(var_2162.astype('bool'), relay.reshape(bop_2166.astype('bool'), relay.shape_of(var_2162))) # shape=(10, 14, 9)
bop_2176 = relay.multiply(call_2143.astype('uint32'), bop_2163.astype('uint32')) # shape=(10, 14, 9)
bop_2179 = relay.multiply(call_2144.astype('uint32'), bop_2166.astype('uint32')) # shape=(10, 14, 9)
output = relay.Tuple([call_2153,bop_2170,bop_2176,])
output2 = relay.Tuple([call_2154,bop_2173,bop_2179,])
func_2180 = relay.Function([var_2162,], output)
mod['func_2180'] = func_2180
mod = relay.transform.InferType()(mod)
mutated_mod['func_2180'] = func_2180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2181 = relay.var("var_2181", dtype = "float32", shape = (10, 14, 9))#candidate|2181|(10, 14, 9)|var|float32
func_2180_call = mutated_mod.get_global_var('func_2180')
call_2182 = func_2180_call(var_2181)
output = call_2182
func_2183 = relay.Function([var_2181], output)
mutated_mod['func_2183'] = func_2183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_2195 = func_1690_call()
call_2196 = func_1690_call()
uop_2197 = relay.acos(call_2195.astype('float64')) # shape=(11, 3, 9)
uop_2199 = relay.acos(call_2196.astype('float64')) # shape=(11, 3, 9)
var_2204 = relay.var("var_2204", dtype = "float64", shape = (11, 3, 9))#candidate|2204|(11, 3, 9)|var|float64
bop_2205 = relay.power(uop_2197.astype('float32'), relay.reshape(var_2204.astype('float32'), relay.shape_of(uop_2197))) # shape=(11, 3, 9)
bop_2208 = relay.power(uop_2199.astype('float32'), relay.reshape(var_2204.astype('float32'), relay.shape_of(uop_2199))) # shape=(11, 3, 9)
func_1133_call = mod.get_global_var('func_1133')
func_1136_call = mutated_mod.get_global_var('func_1136')
var_2210 = relay.var("var_2210", dtype = "float32", shape = (45,))#candidate|2210|(45,)|var|float32
call_2209 = relay.TupleGetItem(func_1133_call(relay.reshape(var_2210.astype('float32'), [1, 45])), 3)
call_2211 = relay.TupleGetItem(func_1136_call(relay.reshape(var_2210.astype('float32'), [1, 45])), 3)
func_1760_call = mod.get_global_var('func_1760')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_2216 = relay.TupleGetItem(func_1760_call(), 0)
call_2217 = relay.TupleGetItem(func_1762_call(), 0)
uop_2223 = relay.atanh(call_2195.astype('float64')) # shape=(11, 3, 9)
uop_2225 = relay.atanh(call_2196.astype('float64')) # shape=(11, 3, 9)
output = relay.Tuple([bop_2205,call_2209,var_2210,call_2216,uop_2223,])
output2 = relay.Tuple([bop_2208,call_2211,var_2210,call_2217,uop_2225,])
func_2230 = relay.Function([var_2204,var_2210,], output)
mod['func_2230'] = func_2230
mod = relay.transform.InferType()(mod)
var_2231 = relay.var("var_2231", dtype = "float64", shape = (11, 3, 9))#candidate|2231|(11, 3, 9)|var|float64
var_2232 = relay.var("var_2232", dtype = "float32", shape = (45,))#candidate|2232|(45,)|var|float32
output = func_2230(var_2231,var_2232,)
func_2233 = relay.Function([var_2231,var_2232,], output)
mutated_mod['func_2233'] = func_2233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2241 = relay.var("var_2241", dtype = "uint64", shape = (1, 7, 15))#candidate|2241|(1, 7, 15)|var|uint64
var_2242 = relay.var("var_2242", dtype = "uint64", shape = (2, 7, 15))#candidate|2242|(2, 7, 15)|var|uint64
bop_2243 = relay.right_shift(var_2241.astype('uint64'), var_2242.astype('uint64')) # shape=(2, 7, 15)
output = relay.Tuple([bop_2243,])
output2 = relay.Tuple([bop_2243,])
func_2256 = relay.Function([var_2241,var_2242,], output)
mod['func_2256'] = func_2256
mod = relay.transform.InferType()(mod)
var_2257 = relay.var("var_2257", dtype = "uint64", shape = (1, 7, 15))#candidate|2257|(1, 7, 15)|var|uint64
var_2258 = relay.var("var_2258", dtype = "uint64", shape = (2, 7, 15))#candidate|2258|(2, 7, 15)|var|uint64
output = func_2256(var_2257,var_2258,)
func_2259 = relay.Function([var_2257,var_2258,], output)
mutated_mod['func_2259'] = func_2259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1760_call = mod.get_global_var('func_1760')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_2263 = relay.TupleGetItem(func_1760_call(), 0)
call_2264 = relay.TupleGetItem(func_1762_call(), 0)
uop_2267 = relay.acos(call_2263.astype('float64')) # shape=(13, 2, 7)
uop_2269 = relay.acos(call_2264.astype('float64')) # shape=(13, 2, 7)
output = relay.Tuple([uop_2267,])
output2 = relay.Tuple([uop_2269,])
func_2292 = relay.Function([], output)
mod['func_2292'] = func_2292
mod = relay.transform.InferType()(mod)
output = func_2292()
func_2293 = relay.Function([], output)
mutated_mod['func_2293'] = func_2293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_802_call = mod.get_global_var('func_802')
func_803_call = mutated_mod.get_global_var('func_803')
call_2318 = relay.TupleGetItem(func_802_call(), 0)
call_2319 = relay.TupleGetItem(func_803_call(), 0)
func_1480_call = mod.get_global_var('func_1480')
func_1482_call = mutated_mod.get_global_var('func_1482')
call_2320 = relay.TupleGetItem(func_1480_call(), 0)
call_2321 = relay.TupleGetItem(func_1482_call(), 0)
func_975_call = mod.get_global_var('func_975')
func_976_call = mutated_mod.get_global_var('func_976')
call_2327 = relay.TupleGetItem(func_975_call(), 0)
call_2328 = relay.TupleGetItem(func_976_call(), 0)
func_2292_call = mod.get_global_var('func_2292')
func_2293_call = mutated_mod.get_global_var('func_2293')
call_2329 = relay.TupleGetItem(func_2292_call(), 0)
call_2330 = relay.TupleGetItem(func_2293_call(), 0)
output = relay.Tuple([call_2318,call_2320,call_2327,call_2329,])
output2 = relay.Tuple([call_2319,call_2321,call_2328,call_2330,])
func_2332 = relay.Function([], output)
mod['func_2332'] = func_2332
mod = relay.transform.InferType()(mod)
output = func_2332()
func_2333 = relay.Function([], output)
mutated_mod['func_2333'] = func_2333
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2334 = relay.const([[[1,-5,5,-3,6],[-5,8,5,-6,8],[9,2,7,6,-8],[3,-5,8,-2,10],[-2,2,-6,5,-9],[-8,8,10,7,9],[7,7,-10,-3,-3],[-2,-1,-6,-3,-9],[-5,3,-6,-9,10],[-8,-1,8,-9,6],[7,8,4,3,4],[2,-8,3,9,-4],[-9,6,9,-1,-7],[10,-5,-10,-2,-8],[6,8,-6,-5,-2],[-4,5,-10,3,1]],[[-6,-4,1,2,8],[4,2,7,2,3],[-4,4,6,-2,-5],[9,-7,-4,8,4],[8,1,9,-9,1],[-4,10,4,1,-5],[10,10,6,8,2],[1,9,1,9,8],[6,6,-9,2,-6],[-8,2,6,4,3],[3,7,5,9,-1],[-5,-8,-3,-1,6],[-3,-6,4,2,-3],[5,8,-9,3,-6],[-6,9,3,-8,6],[-4,10,-3,-9,4]],[[9,-9,3,-7,-5],[-1,5,-2,2,5],[-7,7,8,-4,5],[8,-9,-9,4,-1],[3,9,-1,-8,-4],[-1,1,-10,9,5],[-4,-8,-1,-7,4],[-3,1,-5,-4,5],[6,-1,-5,-8,-5],[-8,10,-1,-2,-8],[-6,1,5,-10,-1],[-9,3,5,-8,-4],[-10,1,-6,-2,1],[-5,1,4,4,-4],[-1,3,2,-3,3],[-5,-10,4,7,6]],[[-6,-6,-9,-2,6],[-9,1,-4,9,5],[-7,-6,5,4,-8],[1,-3,2,7,4],[-9,2,-2,5,4],[-5,10,-7,-3,-8],[-3,-6,4,-6,-1],[-4,-3,2,-3,-9],[9,-5,7,-2,4],[3,9,-2,9,-3],[10,3,-6,-1,4],[-3,5,-9,-3,-3],[3,4,7,-4,-4],[7,6,9,6,8],[-1,-2,2,-7,4],[-10,5,-8,10,1]],[[1,-9,-9,-9,-10],[5,-10,8,-8,-7],[-6,-9,10,5,1],[3,-3,9,3,-7],[6,4,8,-10,-8],[9,1,-5,5,-1],[8,-8,-10,-3,4],[-6,1,-6,4,3],[2,-4,-10,-4,-10],[1,10,-9,6,-3],[-3,3,-1,-2,7],[-6,9,-2,10,-4],[-2,10,-8,-4,2],[-7,8,-10,-10,-3],[8,-4,1,6,1],[-4,8,-6,-5,-1]],[[8,4,9,-5,6],[4,9,-3,-5,2],[10,10,1,6,-6],[3,-6,-8,-10,-2],[2,2,-7,2,3],[-9,-1,3,-6,-6],[-8,6,7,-9,-8],[-3,8,-4,8,8],[-1,6,-7,-1,-2],[9,7,3,1,1],[2,2,9,6,1],[1,-10,-3,10,4],[-3,1,8,2,-6],[3,-6,10,2,-3],[10,6,-2,1,-2],[-5,9,3,-10,9]],[[9,-3,-6,10,-1],[-10,10,-2,-4,6],[9,-1,7,-6,-2],[-2,6,7,10,-9],[-4,-1,6,7,-8],[7,6,4,3,-8],[-4,5,-6,1,10],[7,10,8,-3,7],[8,9,-2,-7,4],[10,-8,7,7,-1],[7,-1,-8,-2,-4],[4,-2,7,-7,-1],[-2,10,-3,-3,4],[-7,2,7,-9,-2],[-9,6,-9,-9,9],[-1,8,8,-8,-2]],[[-7,-3,-9,8,1],[-10,6,4,-10,4],[-3,-10,-6,-2,1],[5,5,6,8,1],[-6,2,10,7,-8],[-1,6,2,10,-6],[-10,-9,-9,-8,-3],[-8,3,-10,5,4],[10,4,5,-10,10],[7,7,4,5,4],[-2,-6,2,7,-3],[9,-6,-1,-9,-7],[-7,8,4,-9,-3],[-4,5,7,6,-5],[4,-4,8,-1,-8],[-7,-5,-10,-8,-8]],[[4,-5,4,8,-7],[10,-6,-4,-4,3],[-7,9,-5,1,-8],[4,2,2,-3,-5],[3,4,2,6,-4],[7,9,-3,5,-10],[4,-6,5,-2,10],[9,-5,-7,-10,4],[-1,-5,-7,5,-4],[-6,8,5,-1,2],[-6,-9,3,-1,-8],[-8,6,-7,4,6],[6,-6,-3,8,10],[7,2,-9,1,-9],[-5,-6,-10,3,-7],[-2,10,-7,-9,-8]],[[6,6,-3,-2,-7],[3,-8,2,-4,-4],[5,-3,-3,9,-7],[2,-2,1,5,10],[-6,3,-4,4,3],[10,-3,4,-5,-10],[10,6,-10,7,-4],[-7,-2,2,7,-5],[-3,8,-9,-2,5],[-7,-5,9,3,3],[5,-6,10,4,-4],[-8,5,3,-8,10],[-10,-10,-1,-10,-5],[10,5,-6,5,-2],[10,-8,-8,10,-9],[-1,9,-1,2,-5]],[[-8,-6,2,-8,3],[-8,2,7,6,-5],[-10,-1,8,7,7],[7,-8,6,7,7],[-6,3,10,5,9],[-10,-6,6,-6,6],[-7,-9,-7,5,1],[-4,-8,4,-8,3],[-10,-6,5,-2,7],[4,-2,8,-8,-1],[-8,5,-3,1,7],[-9,-8,-3,7,4],[5,7,-9,-5,10],[7,5,4,-10,-9],[1,-5,-7,10,6],[-9,1,6,-2,10]],[[-1,10,8,3,-10],[-6,2,-8,10,2],[-3,4,-6,-6,5],[10,1,-9,-5,9],[-5,-4,6,8,1],[1,3,-8,8,-7],[7,9,9,-9,2],[-8,4,-8,6,-6],[7,1,-3,-1,2],[-5,7,-9,4,1],[-5,-7,-2,9,10],[-5,1,9,2,6],[-5,-2,-5,-9,8],[-8,-10,4,-9,-8],[-8,-6,-8,4,2],[-5,-1,1,8,6]],[[1,-3,-7,3,-9],[5,-5,-8,-7,-2],[-4,-7,-5,-10,2],[1,10,-4,-10,-4],[-7,8,-1,4,1],[-6,4,10,4,2],[-6,9,6,4,10],[5,-7,9,1,4],[1,9,-3,-5,-8],[3,2,1,-5,4],[-3,3,3,-7,-7],[-8,-3,6,-5,5],[7,-9,-9,-7,-5],[10,-1,9,-6,8],[-1,2,3,-2,-8],[-2,-6,-4,-1,-1]],[[-3,8,3,5,6],[-3,-10,-1,-2,9],[-9,-4,2,-9,-10],[-3,1,-4,9,-6],[-5,-9,3,-7,-4],[-6,9,-7,-10,6],[-9,3,-8,-6,10],[-1,-10,-9,-2,-1],[-3,9,-7,-3,-7],[6,-7,5,10,4],[5,5,6,10,8],[-4,8,-3,2,-1],[6,-2,-10,2,-10],[2,-2,1,-8,-7],[4,-7,5,-7,-7],[-3,-8,10,5,10]]], dtype = "uint16")#candidate|2334|(14, 16, 5)|const|uint16
var_2335 = relay.var("var_2335", dtype = "uint16", shape = (14, 16, 5))#candidate|2335|(14, 16, 5)|var|uint16
bop_2336 = relay.bitwise_or(const_2334.astype('uint16'), relay.reshape(var_2335.astype('uint16'), relay.shape_of(const_2334))) # shape=(14, 16, 5)
bop_2339 = relay.floor_mod(bop_2336.astype('float64'), relay.reshape(const_2334.astype('float64'), relay.shape_of(bop_2336))) # shape=(14, 16, 5)
output = bop_2339
output2 = bop_2339
func_2343 = relay.Function([var_2335,], output)
mod['func_2343'] = func_2343
mod = relay.transform.InferType()(mod)
mutated_mod['func_2343'] = func_2343
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2344 = relay.var("var_2344", dtype = "uint16", shape = (14, 16, 5))#candidate|2344|(14, 16, 5)|var|uint16
func_2343_call = mutated_mod.get_global_var('func_2343')
call_2345 = func_2343_call(var_2344)
output = call_2345
func_2346 = relay.Function([var_2344], output)
mutated_mod['func_2346'] = func_2346
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2371 = relay.var("var_2371", dtype = "float32", shape = (15, 8, 10))#candidate|2371|(15, 8, 10)|var|float32
uop_2372 = relay.log(var_2371.astype('float32')) # shape=(15, 8, 10)
func_2180_call = mod.get_global_var('func_2180')
func_2183_call = mutated_mod.get_global_var('func_2183')
var_2377 = relay.var("var_2377", dtype = "float32", shape = (9, 140))#candidate|2377|(9, 140)|var|float32
call_2376 = relay.TupleGetItem(func_2180_call(relay.reshape(var_2377.astype('float32'), [10, 14, 9])), 1)
call_2378 = relay.TupleGetItem(func_2183_call(relay.reshape(var_2377.astype('float32'), [10, 14, 9])), 1)
output = relay.Tuple([uop_2372,call_2376,var_2377,])
output2 = relay.Tuple([uop_2372,call_2378,var_2377,])
func_2383 = relay.Function([var_2371,var_2377,], output)
mod['func_2383'] = func_2383
mod = relay.transform.InferType()(mod)
var_2384 = relay.var("var_2384", dtype = "float32", shape = (15, 8, 10))#candidate|2384|(15, 8, 10)|var|float32
var_2385 = relay.var("var_2385", dtype = "float32", shape = (9, 140))#candidate|2385|(9, 140)|var|float32
output = func_2383(var_2384,var_2385,)
func_2386 = relay.Function([var_2384,var_2385,], output)
mutated_mod['func_2386'] = func_2386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_602_call = mod.get_global_var('func_602')
func_603_call = mutated_mod.get_global_var('func_603')
call_2397 = relay.TupleGetItem(func_602_call(), 0)
call_2398 = relay.TupleGetItem(func_603_call(), 0)
output = relay.Tuple([call_2397,])
output2 = relay.Tuple([call_2398,])
func_2408 = relay.Function([], output)
mod['func_2408'] = func_2408
mod = relay.transform.InferType()(mod)
output = func_2408()
func_2409 = relay.Function([], output)
mutated_mod['func_2409'] = func_2409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1846_call = mod.get_global_var('func_1846')
func_1847_call = mutated_mod.get_global_var('func_1847')
call_2416 = relay.TupleGetItem(func_1846_call(), 0)
call_2417 = relay.TupleGetItem(func_1847_call(), 0)
output = call_2416
output2 = call_2417
func_2425 = relay.Function([], output)
mod['func_2425'] = func_2425
mod = relay.transform.InferType()(mod)
output = func_2425()
func_2426 = relay.Function([], output)
mutated_mod['func_2426'] = func_2426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2425_call = mod.get_global_var('func_2425')
func_2426_call = mutated_mod.get_global_var('func_2426')
call_2436 = func_2425_call()
call_2437 = func_2425_call()
func_1004_call = mod.get_global_var('func_1004')
func_1005_call = mutated_mod.get_global_var('func_1005')
call_2443 = relay.TupleGetItem(func_1004_call(), 1)
call_2444 = relay.TupleGetItem(func_1005_call(), 1)
output = relay.Tuple([call_2436,call_2443,])
output2 = relay.Tuple([call_2437,call_2444,])
func_2448 = relay.Function([], output)
mod['func_2448'] = func_2448
mod = relay.transform.InferType()(mod)
mutated_mod['func_2448'] = func_2448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2448_call = mutated_mod.get_global_var('func_2448')
call_2449 = func_2448_call()
output = call_2449
func_2450 = relay.Function([], output)
mutated_mod['func_2450'] = func_2450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1480_call = mod.get_global_var('func_1480')
func_1482_call = mutated_mod.get_global_var('func_1482')
call_2465 = relay.TupleGetItem(func_1480_call(), 0)
call_2466 = relay.TupleGetItem(func_1482_call(), 0)
output = relay.Tuple([call_2465,])
output2 = relay.Tuple([call_2466,])
func_2474 = relay.Function([], output)
mod['func_2474'] = func_2474
mod = relay.transform.InferType()(mod)
mutated_mod['func_2474'] = func_2474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2474_call = mutated_mod.get_global_var('func_2474')
call_2475 = func_2474_call()
output = call_2475
func_2476 = relay.Function([], output)
mutated_mod['func_2476'] = func_2476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_2487 = relay.TupleGetItem(func_411_call(), 1)
call_2488 = relay.TupleGetItem(func_413_call(), 1)
func_2104_call = mod.get_global_var('func_2104')
func_2106_call = mutated_mod.get_global_var('func_2106')
const_2491 = relay.const([7.268557,9.009710,8.047322,2.684938,-7.327492,-9.246438,0.395884,-1.309446,-2.067749,-5.398269,4.844370,7.531134,0.080286,-5.023645,-1.377982,-0.364429,-0.658188,-2.714932,-2.305635,5.164071,-9.313789,3.956823,8.971659,0.309590,8.867981,-9.655455,-7.324888,1.507169,-0.521322,-1.023643,3.422465,-4.535021,-2.081633,-5.745044,-1.567357,1.621264,0.095694,-5.293240,-2.603796,4.379585,-0.527409,6.164114,0.030554,-6.423389,-6.442413,-1.479898,-9.945731,7.464855,-2.058983,2.608501,-6.534435,0.458015,2.900179,-7.092022,1.569614,-1.005415,0.411955,-3.352750,-7.620820,1.364747,9.374178,4.242842,-5.437004,-8.549447,-7.777426,-5.755660,-8.686105,-6.681836,8.797906,-5.991516,-4.300550,-2.491405,-3.800378,-2.789996,-7.226858,9.235648,-8.500299,7.545196,-5.839485,8.543905,9.783834,6.465436,4.558246,5.262166,-9.741738,5.331412,-5.518151,-7.915655,-9.594033,-3.765271,-5.302730,-6.732438,-6.884911,-2.357107,2.554933,1.645178,4.157236,-0.413584,-9.481352,6.039377,9.151222,-4.425155,8.354316,-3.535014,2.819537,-7.507012,5.988100,-5.259393,-3.426579,-5.535568,-2.190265,-9.805150,-8.900478,-2.311843,-7.790673,6.082049,-4.020971,-6.073668,-0.839167,7.122658,1.731568,-0.541356,-5.488629,-1.887915,3.457822,-9.645022,-3.887457,7.703066,-1.061837,4.091139,0.519295,-7.189197,-4.748047,5.525399,-3.839244,7.801658,-7.695447,-0.714993,-2.656770,5.421132,8.271306,-9.231498,-8.397233,-0.113341,8.713180,-3.940342,-0.802536,4.060726,9.106440,2.155622,4.136835,6.479621,-0.023774,2.073203,-9.634562,-6.443770,-3.445806,3.571617,-3.391950,4.762033,5.630870,0.019085,6.126203,6.142724,8.079514,-5.707055,0.246010,2.896915,6.487623,-2.480767,8.209973,0.329428,4.846992,0.156527,-3.076852,-0.722007,-1.699757,9.777736,-5.169710,-2.531941,5.500832,-2.592934,-1.279942,1.691797,-7.096887,3.410187,-5.494249,-2.887359,1.838247,-6.870841,-4.366438,0.122121,-1.871353,-5.004607,3.413242,-0.431804,3.015761,7.364579,-3.782516,8.989845,1.560022,0.593127,5.689483,0.765426,7.588740,-5.994216,-9.627868,-0.052310,-1.327240,7.841089,7.991833,5.502528,0.921558,-4.310410,7.461679,-1.340728,-5.297474,-6.299707,8.681411,-5.460470,2.747142,3.952916,-8.685675,-8.666911,-1.891103,4.701022,-4.865518,4.149551,9.936876,4.804470,8.568942,9.312277,1.194585,-0.907510,-3.218628,8.651477,7.475316,7.154145,-5.428714,3.183021,-6.102668,-8.464813,9.027869,-4.754614,3.690856,9.383643,8.262930,-0.925008,-2.130260,-8.876613,7.393186,4.257578,-9.661097,0.624558,-3.712337,3.250350,1.973587,3.246312,7.674681,8.500591,-0.100654,-7.212835,-9.865294,-0.703610,1.572901,2.943425,2.939801,0.860744,0.679613,-2.853041,6.089955,-4.522810,-3.138721,5.932956,1.482387,-3.579878,8.298172,-9.108191,-3.296006,5.150178,7.585475,-9.008777,9.742397,-0.544801,-0.949774,-2.990006,-8.066673,-1.520762,2.482833,8.150494,9.822990,-3.364677,-0.724688,-2.611752,4.309880,-4.502080,-0.667638,8.291704,-8.363588,-0.658026,9.740635,0.249424,-5.435268,-6.171033,9.288014,-5.708276,7.990198,-7.999379,1.735597,-3.725253,-2.704272,2.647398,-3.307425,-2.039770,-2.865989,9.563977,4.572570,-5.025047,8.127712,9.895697,-1.481076,8.845839,-1.091957,8.228762,-8.822834,7.098599,-1.060868,5.715758,9.260188,7.829776,-5.101426,0.554586,2.241844,1.088914,-6.887897,-9.814052,6.272396,1.150008,2.145271,4.702298,-5.843432,-0.509826,-4.556031,6.738002,6.474984,5.191685,-9.166150,1.852202,-9.294291,-6.957495,-2.040573,2.070326,-2.833850,9.588931,1.481878,5.417896,7.377624,-5.489290,2.366216,-7.016592,8.809364,-8.325046,-9.153948,9.931500,4.826101,-6.599092,-7.145800,7.534315,-6.922194,-5.225391,5.794999,4.298096,0.805578,-1.061346,-3.037341,0.386897,5.202653,5.150275,-2.388591,-0.102951,-7.076949,5.525126,6.227984,3.694737,2.129120,2.676222,9.289710,-4.292924,6.492919,8.363400,6.284926,1.115403,-2.000257,-1.779131,2.201395,-8.469373,0.761555,8.568631,-8.301289,-7.532709,-1.892496,6.646388,4.377729,4.118957,-2.875175,-8.254568,6.146614,-7.321267,-7.711656,-6.860362,-3.631523,4.720467,-5.346177,-2.353054,7.218378,8.926271,-7.619631,6.592901,-0.180326,-0.849122,0.024145,-4.874087,-4.574265,-6.518791,7.644706,6.290978,-1.873947,-2.689122,7.649341,0.825423,9.019864,-9.223118,8.946164,8.417749,-1.335898,5.758809,-3.105801,7.987268,-9.627507,8.077212,-6.861759,1.564644,1.774352,-0.362590,-5.692388,3.367251,-1.344683,-4.729025,9.916818,4.298972,5.996071,7.930086,-9.564612,4.117114,2.281590,-2.527982,8.925255,-5.080459,4.797187,2.365404,-3.258135,-3.176613,-8.388890,5.461819,-4.036926,-1.476590,4.742824,-7.606230,-5.977333,-9.873331,-7.692411,1.872547,2.165349,1.170467,-7.796708,-5.579000,5.305336,5.635389,0.644695,-4.477507,5.329730,-3.734927,-6.631645,-9.950750,-1.031112,-6.966071,-3.686841,-2.961578,1.962118,-9.842510,-5.474601,6.551398,3.526393,1.305328,5.848096,3.437992,-8.994113,3.926109,-5.638587,1.353955,-3.796674,6.655637,-2.536038,-5.579566,8.948513,9.451241,-2.387149,-7.269465,-4.183610,-7.169657,4.828815,-1.878085,9.091967,-6.909325,-0.883722,-6.438085,-3.142074,2.348316,4.104901,-4.582721,-9.436424,-7.212522,-4.703850,8.804804,0.499552,-7.291536,3.542972,-8.246919,-0.815592,-2.497273,2.610502,-1.790661,-9.057469,-7.787975,3.284112,3.362717,-4.295791,-8.423791,-6.921621,5.496351,-1.330507,-7.340362,2.665890,-7.059734,4.165259,-9.021698,-0.850102,-6.946968,-9.152284,-3.349338,-9.099562,1.560722,-9.704498,3.829939,0.564556,-2.317829,6.185126,9.046271,5.191985,-4.998062,-2.398774,1.953994,7.279834,-4.319074,-2.060188,-8.915773,-0.531902,-8.714127,2.525612,3.863221,-7.281253,-8.661285,-2.570555,-0.005298,-0.808130,-3.056699,6.453572,9.676689,-5.240689,-2.478155,-3.259225,1.518056,9.054546,2.525294,6.125668,3.147919,-0.803899,8.372857,-7.354008,7.266599,5.345675,1.059292,3.229306,6.388927,-7.966946,6.140614,-6.492952,6.255731,-4.278002,5.945753,9.461911,7.030356,-0.666746,-7.925080,0.117451,1.725249,-3.962624,5.842372,3.134285,4.897184,5.053879,3.616542,9.911990,2.523992,5.336101,8.547863,5.233839,9.872367,-4.208757,-0.796128,4.183308,-3.165082,2.973103,3.737528,-5.993756,-2.844115,3.746092,-1.163867,6.069623,-9.858815,-3.311615,7.634334,9.480139,2.619245,2.788059,4.956644,-8.568249,-3.178969,0.018556,-4.870361,-2.714342,9.074290,-0.317595,-5.316823,3.957818,6.994992,-6.360397,-5.816096,7.246333,0.247473,5.048164,6.592826,-2.697371,7.197755,0.698795,-1.689535,9.933894,-1.850590,5.969454,9.117853,8.539810,-9.797217,1.542905,2.565316,-0.691445,4.615420,4.790579,5.828070,-1.020403,-9.855595,6.877291,2.957194,-6.206316,-8.996264,-3.950957,6.606673,-8.306786,-9.671506,-4.003635,-7.172996,-7.934715,-0.093272,-1.597450,-2.590679,3.379119,3.317300,5.150050,7.230211,-1.682943,7.272537,2.614993,-2.403382,-3.619057,8.165365,9.660952,9.341186,-9.153103,3.411498,-6.351571,1.878532,-0.820395,-0.591761,-1.285789,-0.361891,1.147255,8.027317,-6.977685,2.261638,-7.225926,8.830810,-4.336624,-8.986332,-9.798813,-4.066849,0.998256,-5.719640,-2.886574,8.084187,-7.426192,8.840573,4.344288,-6.086386,-3.291150,-5.086226,5.949244,-8.943433,-2.851996,-6.232388,8.460684,7.659245,-6.603804,-3.526087,-6.874221,3.835661,1.883571,7.878997,-0.444698,-3.062708,4.072158,5.245288,-5.734700,-3.468407,-8.188875,-2.936486,3.240160,-3.385572,0.511668,-1.262916,-0.552548,3.814798,-3.297186,-0.084553,-3.344242,-3.793038,4.370419,-5.677284,1.011635,1.183890,2.098584,4.257380,1.632815,8.311363,4.380063,2.774318,5.076197,0.090102,5.887816,-7.511285,9.759959,6.104316,5.382656,-6.605176,-4.379044,-8.137369,9.341678,0.372860,-6.083720,-1.429320,-5.278495,7.996003,-0.622655,-6.815360,3.716209,8.820238,9.290022,7.976545,8.956052,1.616627,5.219726,6.604281,-9.410327,-0.664170,8.425426,-4.322414,-5.521350,-7.764461,-4.022064,-2.737993,4.218633,-7.240941,-9.831589,8.775542,-0.359833,8.189048,9.168118,-4.093328,8.809096,-7.725790,0.315599,2.805901,-7.626373,-8.665169,-2.939811,-6.280683,7.993616,-6.188668,8.004684,0.889100,-3.868512,9.943816,8.344546,9.600013,-3.026636,-0.229130,-1.881284,1.350631,5.638984,-5.450944,-6.586847,3.768056,2.222092,9.909729,-8.996336,-2.892257,-2.649833,-3.075472,-3.388912,-6.693482,4.541193,-5.899146,-5.829044,-7.862313,-6.144886,7.129806,-5.163464,-7.413328,-6.938662,-0.639929,-9.555163,-2.145971,-9.574231,-2.823611,-8.101304,-9.631703,4.724915,-2.453077,-1.014842,2.162859,0.175122,-6.637278,-1.051545,5.208122,-3.527564,9.348984,4.703392,9.496554,-1.395624,-7.659290,7.430603,-2.767125,7.660972,-5.614347,0.346530,-9.288519,8.075049,-7.251515,6.430626,-1.534033,4.203581,-9.104119,8.644622,5.111239,-5.872598,5.947913,-9.142149,-7.246019,-1.995221,3.237881,2.842854,-5.386841,-1.284295,-3.147085,-0.027744,-2.534699,-9.651871,-0.361639,-9.245404,8.372329,4.436821,-2.003123,-8.173947,-3.057355,-2.609398,-3.144210,7.796407,-9.357122,-1.441535,-5.883129,0.012167,-4.990654,7.472741,-5.017789,-3.832322,-9.689105,-6.823991,2.414940,-4.200396,0.075250,-8.019327,-8.504460,-2.425958,4.001049,3.799414,4.596077,-1.762685,-1.396007,1.173390,-1.312228,-6.248160,1.771309,7.789274,9.180907,-3.623045,-0.684564,-7.682076,0.494274,3.258904,6.171219,-7.427167,-0.269126,9.425815,-7.339038,1.871983,-3.035999,-8.691985,-9.026092,0.482132,7.245383,-5.659222,-9.361131,-3.954841,9.491767,-9.727053,-8.573344,7.346530,-7.818620,7.959395,5.826265,1.493801,-7.421296,-2.484434,8.411430,-6.847413,8.816178,9.511023,4.798415,4.802275,7.601580,-8.150443,-5.591200,-5.388115,-3.044320,-4.816388,-8.201069,1.863801,9.962615,3.507167,5.868813,9.053888,-8.454914,-6.145063,-4.595997,-9.535847,-3.023824,0.497046,7.539444,1.920014,0.609390,3.538459,6.116035,-8.610736,-8.634091,4.801212,2.652082,3.398704,2.741454,0.386126,0.418767,-3.516409,-3.983136,0.340399,1.074875,2.901709,-3.948347,2.983438,-7.449227,-4.083232,2.730998,-5.693520,-5.807659,4.021926,-8.181442,5.520963,-9.320620,8.357924,0.818020,-5.779947,2.512360,0.458662,6.755281,4.507746,-4.660921,-6.951999,9.228017,-7.630361,-6.699383,-0.012157,-6.206410,5.544010,0.954933,-7.588793,9.333721,0.653732,-0.936011,-6.339885,8.243103,1.499937,0.552831,-0.072629,8.871467,-5.407373,-1.291059,-8.282068,-8.343398,3.200978,-2.616554,-5.703256,7.342106,-6.775732,-8.377053,3.213792,-2.332780,0.192264,-6.091459,-8.362446,-1.281134,-3.188081,8.137987,2.902508,-4.037053,4.395291,-4.258865,-4.717831,-8.284871,-4.467705,2.003899,-8.430494,-9.992382,9.635883,7.308025,-5.459596,-9.797310,-1.252447,7.328524,0.114648,3.099999,-3.109719,-3.192892,0.788476,0.265473,3.913900,3.153569,-4.557972,7.498722,-4.045457,-4.030960,-1.159101,9.485150,-1.825643,-8.756608,-2.378137,8.054294,-7.193266,4.137172,-7.377480,4.398917,2.587519,4.044748,-1.326782,4.112796,-8.524171,-0.783202,-4.756398,9.927301,-0.713424,-0.340576,4.106018,-6.939283,0.666508,7.106333,-0.074000,7.743076,8.072660,-0.397013,4.558629,6.158538,3.923360,-8.340941,3.538649,-3.168147,-7.666785,0.114268,-2.469252,9.707955,7.557087,9.781871,3.850466,-2.019164,-3.471113,-9.307743,-2.082546,5.793740,8.052735,-8.265404,2.213287,2.331567,7.156044,-8.066493,-6.124554,-0.022610,-7.440481,8.440709,-8.396504,1.175028,-7.204276,0.169649,1.551126,-2.444415,-3.881791,2.903350,-3.550184,8.022085,8.847510,1.423568,8.604149,-7.375217,-8.116569,8.943070,7.424889,5.622074,0.705320,-1.127889,2.049954,3.987951,5.945564,0.736081,5.838167,-9.453628,-0.520304,-3.993171,4.636072,-0.350812,3.881156,-3.340000,-1.215797,-8.782423,-8.290241,-1.049995,-6.229162,-5.679434,-5.474900,8.942017,-4.139332,8.667655,1.516137,0.017301,-9.517532,-4.923168,8.015584,-0.333572,-0.388782,7.575686,2.422493,-0.851980,-3.904509,-5.434178,3.333419,-7.288636,4.205426,-7.709609,-7.406982,6.260756,3.038923,-8.004420,-8.620603,-1.494729,4.584981,-3.232774,1.971340,-6.783442,7.583255,1.007644,-7.500634,-7.990225,2.554662], dtype = "float32")#candidate|2491|(1215,)|const|float32
call_2490 = func_2104_call(relay.reshape(const_2491.astype('float32'), [15, 9, 9]))
call_2492 = func_2104_call(relay.reshape(const_2491.astype('float32'), [15, 9, 9]))
output = relay.Tuple([call_2487,call_2490,const_2491,])
output2 = relay.Tuple([call_2488,call_2492,const_2491,])
func_2497 = relay.Function([], output)
mod['func_2497'] = func_2497
mod = relay.transform.InferType()(mod)
mutated_mod['func_2497'] = func_2497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2497_call = mutated_mod.get_global_var('func_2497')
call_2498 = func_2497_call()
output = call_2498
func_2499 = relay.Function([], output)
mutated_mod['func_2499'] = func_2499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1480_call = mod.get_global_var('func_1480')
func_1482_call = mutated_mod.get_global_var('func_1482')
call_2563 = relay.TupleGetItem(func_1480_call(), 0)
call_2564 = relay.TupleGetItem(func_1482_call(), 0)
func_2332_call = mod.get_global_var('func_2332')
func_2333_call = mutated_mod.get_global_var('func_2333')
call_2598 = relay.TupleGetItem(func_2332_call(), 3)
call_2599 = relay.TupleGetItem(func_2333_call(), 3)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_2605 = func_1690_call()
call_2606 = func_1690_call()
bop_2616 = relay.divide(call_2563.astype('float64'), call_2605.astype('float64')) # shape=(11, 3, 9)
bop_2619 = relay.divide(call_2564.astype('float64'), call_2606.astype('float64')) # shape=(11, 3, 9)
output = relay.Tuple([call_2598,bop_2616,])
output2 = relay.Tuple([call_2599,bop_2619,])
func_2627 = relay.Function([], output)
mod['func_2627'] = func_2627
mod = relay.transform.InferType()(mod)
output = func_2627()
func_2628 = relay.Function([], output)
mutated_mod['func_2628'] = func_2628
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2654 = relay.var("var_2654", dtype = "int64", shape = (13, 5, 3))#candidate|2654|(13, 5, 3)|var|int64
var_2655 = relay.var("var_2655", dtype = "int64", shape = (13, 5, 3))#candidate|2655|(13, 5, 3)|var|int64
bop_2656 = relay.bitwise_and(var_2654.astype('int64'), relay.reshape(var_2655.astype('int64'), relay.shape_of(var_2654))) # shape=(13, 5, 3)
func_2627_call = mod.get_global_var('func_2627')
func_2628_call = mutated_mod.get_global_var('func_2628')
call_2668 = relay.TupleGetItem(func_2627_call(), 0)
call_2669 = relay.TupleGetItem(func_2628_call(), 0)
func_1846_call = mod.get_global_var('func_1846')
func_1847_call = mutated_mod.get_global_var('func_1847')
call_2674 = relay.TupleGetItem(func_1846_call(), 0)
call_2675 = relay.TupleGetItem(func_1847_call(), 0)
var_2683 = relay.var("var_2683", dtype = "float64", shape = (13, 2, 7))#candidate|2683|(13, 2, 7)|var|float64
bop_2684 = relay.less_equal(call_2668.astype('bool'), relay.reshape(var_2683.astype('bool'), relay.shape_of(call_2668))) # shape=(13, 2, 7)
bop_2687 = relay.less_equal(call_2669.astype('bool'), relay.reshape(var_2683.astype('bool'), relay.shape_of(call_2669))) # shape=(13, 2, 7)
uop_2695 = relay.tan(call_2668.astype('float64')) # shape=(13, 2, 7)
uop_2697 = relay.tan(call_2669.astype('float64')) # shape=(13, 2, 7)
output = relay.Tuple([bop_2656,call_2674,bop_2684,uop_2695,])
output2 = relay.Tuple([bop_2656,call_2675,bop_2687,uop_2697,])
func_2713 = relay.Function([var_2654,var_2655,var_2683,], output)
mod['func_2713'] = func_2713
mod = relay.transform.InferType()(mod)
mutated_mod['func_2713'] = func_2713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2713_call = mutated_mod.get_global_var('func_2713')
var_2715 = relay.var("var_2715", dtype = "int64", shape = (13, 5, 3))#candidate|2715|(13, 5, 3)|var|int64
var_2716 = relay.var("var_2716", dtype = "int64", shape = (13, 5, 3))#candidate|2716|(13, 5, 3)|var|int64
var_2717 = relay.var("var_2717", dtype = "float64", shape = (13, 2, 7))#candidate|2717|(13, 2, 7)|var|float64
call_2714 = func_2713_call(var_2715,var_2716,var_2717,)
output = call_2714
func_2718 = relay.Function([var_2715,var_2716,var_2717,], output)
mutated_mod['func_2718'] = func_2718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1700_call = mod.get_global_var('func_1700')
func_1701_call = mutated_mod.get_global_var('func_1701')
call_2769 = func_1700_call()
call_2770 = func_1700_call()
var_2771 = relay.var("var_2771", dtype = "bool", shape = (1, 13, 14))#candidate|2771|(1, 13, 14)|var|bool
bop_2772 = relay.floor_mod(call_2769.astype('float64'), var_2771.astype('float64')) # shape=(1, 13, 14)
bop_2775 = relay.floor_mod(call_2770.astype('float64'), var_2771.astype('float64')) # shape=(1, 13, 14)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_2778 = func_1690_call()
call_2779 = func_1690_call()
output = relay.Tuple([bop_2772,call_2778,])
output2 = relay.Tuple([bop_2775,call_2779,])
func_2780 = relay.Function([var_2771,], output)
mod['func_2780'] = func_2780
mod = relay.transform.InferType()(mod)
mutated_mod['func_2780'] = func_2780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2781 = relay.var("var_2781", dtype = "bool", shape = (1, 13, 14))#candidate|2781|(1, 13, 14)|var|bool
func_2780_call = mutated_mod.get_global_var('func_2780')
call_2782 = func_2780_call(var_2781)
output = call_2782
func_2783 = relay.Function([var_2781], output)
mutated_mod['func_2783'] = func_2783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_663_call = mod.get_global_var('func_663')
func_664_call = mutated_mod.get_global_var('func_664')
call_2794 = func_663_call()
call_2795 = func_663_call()
output = call_2794
output2 = call_2795
func_2817 = relay.Function([], output)
mod['func_2817'] = func_2817
mod = relay.transform.InferType()(mod)
mutated_mod['func_2817'] = func_2817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2817_call = mutated_mod.get_global_var('func_2817')
call_2818 = func_2817_call()
output = call_2818
func_2819 = relay.Function([], output)
mutated_mod['func_2819'] = func_2819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_663_call = mod.get_global_var('func_663')
func_664_call = mutated_mod.get_global_var('func_664')
call_2866 = func_663_call()
call_2867 = func_663_call()
func_523_call = mod.get_global_var('func_523')
func_525_call = mutated_mod.get_global_var('func_525')
call_2900 = relay.TupleGetItem(func_523_call(relay.reshape(call_2866.astype('bool'), [])), 2)
call_2901 = relay.TupleGetItem(func_525_call(relay.reshape(call_2866.astype('bool'), [])), 2)
bop_2906 = relay.add(call_2900.astype('uint16'), call_2866.astype('uint16')) # shape=(2, 13, 11)
bop_2909 = relay.add(call_2901.astype('uint16'), call_2867.astype('uint16')) # shape=(2, 13, 11)
output = relay.Tuple([bop_2906,])
output2 = relay.Tuple([bop_2909,])
func_2923 = relay.Function([], output)
mod['func_2923'] = func_2923
mod = relay.transform.InferType()(mod)
output = func_2923()
func_2924 = relay.Function([], output)
mutated_mod['func_2924'] = func_2924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_745_call = mod.get_global_var('func_745')
func_746_call = mutated_mod.get_global_var('func_746')
call_2955 = relay.TupleGetItem(func_745_call(), 1)
call_2956 = relay.TupleGetItem(func_746_call(), 1)
func_602_call = mod.get_global_var('func_602')
func_603_call = mutated_mod.get_global_var('func_603')
call_2959 = relay.TupleGetItem(func_602_call(), 0)
call_2960 = relay.TupleGetItem(func_603_call(), 0)
bop_2963 = relay.logical_and(call_2955.astype('bool'), relay.reshape(call_2959.astype('bool'), relay.shape_of(call_2955))) # shape=(1, 1, 9)
bop_2966 = relay.logical_and(call_2956.astype('bool'), relay.reshape(call_2960.astype('bool'), relay.shape_of(call_2956))) # shape=(1, 1, 9)
output = bop_2963
output2 = bop_2966
func_2967 = relay.Function([], output)
mod['func_2967'] = func_2967
mod = relay.transform.InferType()(mod)
output = func_2967()
func_2968 = relay.Function([], output)
mutated_mod['func_2968'] = func_2968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_802_call = mod.get_global_var('func_802')
func_803_call = mutated_mod.get_global_var('func_803')
call_3031 = relay.TupleGetItem(func_802_call(), 0)
call_3032 = relay.TupleGetItem(func_803_call(), 0)
output = call_3031
output2 = call_3032
func_3033 = relay.Function([], output)
mod['func_3033'] = func_3033
mod = relay.transform.InferType()(mod)
mutated_mod['func_3033'] = func_3033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3033_call = mutated_mod.get_global_var('func_3033')
call_3034 = func_3033_call()
output = call_3034
func_3035 = relay.Function([], output)
mutated_mod['func_3035'] = func_3035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2332_call = mod.get_global_var('func_2332')
func_2333_call = mutated_mod.get_global_var('func_2333')
call_3043 = relay.TupleGetItem(func_2332_call(), 2)
call_3044 = relay.TupleGetItem(func_2333_call(), 2)
output = call_3043
output2 = call_3044
func_3064 = relay.Function([], output)
mod['func_3064'] = func_3064
mod = relay.transform.InferType()(mod)
output = func_3064()
func_3065 = relay.Function([], output)
mutated_mod['func_3065'] = func_3065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1785_call = mod.get_global_var('func_1785')
func_1787_call = mutated_mod.get_global_var('func_1787')
call_3142 = func_1785_call()
call_3143 = func_1785_call()
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_3149 = relay.TupleGetItem(func_1167_call(), 0)
call_3150 = relay.TupleGetItem(func_1169_call(), 0)
func_2044_call = mod.get_global_var('func_2044')
func_2047_call = mutated_mod.get_global_var('func_2047')
var_3154 = relay.var("var_3154", dtype = "bool", shape = (286, 1))#candidate|3154|(286, 1)|var|bool
call_3153 = relay.TupleGetItem(func_2044_call(relay.reshape(var_3154.astype('bool'), [286,])), 1)
call_3155 = relay.TupleGetItem(func_2047_call(relay.reshape(var_3154.astype('bool'), [286,])), 1)
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_3156 = relay.TupleGetItem(func_557_call(), 0)
call_3157 = relay.TupleGetItem(func_559_call(), 0)
bop_3169 = relay.left_shift(call_3142.astype('int64'), relay.reshape(call_3149.astype('int64'), relay.shape_of(call_3142))) # shape=(1, 1, 9)
bop_3172 = relay.left_shift(call_3143.astype('int64'), relay.reshape(call_3150.astype('int64'), relay.shape_of(call_3143))) # shape=(1, 1, 9)
bop_3173 = relay.minimum(call_3153.astype('uint8'), var_3154.astype('uint8')) # shape=(286, 1)
bop_3176 = relay.minimum(call_3155.astype('uint8'), var_3154.astype('uint8')) # shape=(286, 1)
uop_3179 = relay.cos(call_3142.astype('float64')) # shape=(1, 1, 9)
uop_3181 = relay.cos(call_3143.astype('float64')) # shape=(1, 1, 9)
uop_3184 = relay.cosh(call_3156.astype('float64')) # shape=(1, 1, 9)
uop_3186 = relay.cosh(call_3157.astype('float64')) # shape=(1, 1, 9)
uop_3194 = relay.log(var_3154.astype('float64')) # shape=(286, 1)
func_2104_call = mod.get_global_var('func_2104')
func_2106_call = mutated_mod.get_global_var('func_2106')
const_3199 = relay.const([5.900506,-0.271478,6.538465,4.087268,8.706017,4.347522,8.283732,1.526320,-6.425483,-4.058880,-3.582643,1.166797,-7.879231,-5.847847,5.454066,-4.668948,-8.694514,-8.797754,-3.107114,2.279673,-1.251300,-4.696482,-1.212166,-7.468143,-5.709461,7.518841,-6.571540,-0.126780,-4.900161,7.084777,1.631750,-9.359192,-2.839203,8.700699,6.787546,-1.361142,6.519660,4.173643,5.697247,3.666356,-0.688377,-9.905719,9.449712,-1.296890,7.669615,1.097654,4.498589,-9.619434,-5.901826,-7.371032,3.510380,3.618737,9.822544,-0.793454,3.351378,0.521570,-9.617305,-6.411199,-2.114454,-8.419914,-2.722031,-8.884871,7.848128,8.105307,-5.325233,1.886914,7.497291,7.970482,7.518722,6.402812,9.378434,2.485975,-3.867797,3.408656,-2.247219,-2.200826,4.174662,-3.577482,-0.063596,-5.835135,7.249597,-4.061226,4.883309,3.730436,9.894196,1.670667,2.150850,-1.778906,-2.880937,0.555115,9.954022,-5.731111,-5.549383,-2.670804,-2.445265,-0.142366,-8.993710,-3.697725,-0.889444,7.393097,-0.586596,-0.841174,3.815093,1.950159,-5.163202,-8.218315,6.480595,-6.079538,8.244749,-7.090391,0.875403,1.037451,0.962244,1.829151,5.713110,1.228665,1.644145,-0.423216,-9.955585,1.962694,-5.164924,5.458009,-6.107808,1.126888,-3.481728,1.773182,-4.378500,6.671803,7.881919,3.718945,0.833800,-6.197219,-1.916294,9.012407,9.321984,8.631193,-3.477609,6.817822,-0.744932,-3.681210,-1.818781,5.075103,-1.693677,-7.569575,4.968794,5.039685,-2.414266,-2.684448,-1.774856,0.675738,-6.657130,0.349962,8.526210,1.349955,8.716405,-2.096744,4.051470,7.744485,4.358231,1.199223,2.075309,9.515728,9.182077,0.888358,-9.772559,2.033078,2.056118,8.137104,5.201770,7.497067,9.550493,-8.503274,0.627024,-3.144230,5.861790,2.751431,-9.066206,-8.372463,-2.784629,7.198969,-8.148423,0.097460,2.250169,1.781016,8.145113,-9.740763,-5.475770,-3.926145,-8.349669,-0.203969,-8.428456,-5.710054,5.516180,-1.588572,-0.695922,-4.573397,-7.705928,1.933900,-6.768426,-1.919996,3.156004,-9.258235,0.925896,7.959270,-4.824776,2.520539,9.084034,6.767423,-1.004330,3.836971,-2.311058,-2.305030,6.637795,-8.560198,-6.127508,-3.536208,6.170078,4.870014,4.653403,-0.956361,3.513239,-6.271536,-5.808581,4.499317,-2.697132,7.788536,-9.273260,5.096585,8.741526,8.265492,4.031897,2.798737,5.347528,0.908256,5.920232,-4.716416,-9.982966,-8.644286,-3.081033,7.325607,-8.405194,8.023902,-9.812437,-5.974248,8.542505,2.298978,0.190777,1.097919,-3.548186,5.549064,0.233311,-0.816806,3.256486,-9.577072,-5.638003,-0.996695,-6.356942,5.127589,-7.805593,3.031640,8.488654,-6.157764,8.391207,5.068565,7.573473,-9.428890,-4.843163,-8.549273,0.516327,-4.708851,-0.435456,-0.063231,-2.828108,-5.386160,5.991867,-7.021696,-1.400211,-1.657499,7.835369,8.973848,-1.506510,0.241529,-6.240447,-5.153567,-4.694086,0.208319,0.773320,8.943103,5.910605,9.823647,3.298353,-2.286329,-8.811292,-8.036878,-9.344724,-2.129752,1.118608,-7.972442,7.808868,2.151249,5.036936,2.438739,-1.296627,-4.012761,-7.232126,-6.153001,-5.502338,8.116924,6.443980,-6.425315,-2.106452,7.984279,-3.916489,5.048510,-6.974700,5.306851,-4.979986,6.664129,4.301026,-7.995326,0.130812,-3.883527,0.689012,-4.414973,1.967407,2.366691,-0.375906,9.839060,-8.192970,-0.012221,4.923759,-7.577257,-8.574501,-6.469113,3.911464,0.919144,2.852305,-7.627272,-1.835935,-4.261284,0.001668,0.137863,-7.407382,-8.459100,1.036341,8.285922,-1.606319,-6.612761,1.616989,8.755846,-6.601458,9.980217,-4.589554,-0.309452,1.982248,-4.550694,-8.648595,-6.375053,-4.545457,9.538862,9.788353,-5.211377,-9.124408,1.122523,3.979407,5.042601,1.019860,5.854876,-6.883709,-3.853521,-7.091445,9.896436,-2.288881,1.787256,-9.249864,3.709318,-5.029146,-9.785221,-3.002266,-2.109783,-2.042912,4.329337,7.305361,5.963859,2.500751,0.017712,-8.888219,-5.326181,-6.230773,1.697077,0.788162,-6.389159,-6.514425,-1.795266,-2.136180,-5.707016,-6.039153,6.537380,-9.536868,-9.308690,-8.482764,-6.912440,-3.206524,-1.247769,-9.330361,8.163362,-6.370886,8.592348,-4.107608,6.017274,7.554477,0.566222,-8.887708,6.640764,6.395598,-0.525005,2.908428,-5.088513,2.569561,-0.422627,-7.892806,4.319279,4.654209,3.466939,1.765194,5.590880,-8.366915,-3.782928,7.633968,-8.563115,7.216589,-4.722638,1.422559,-3.597852,2.070759,-3.202375,7.688773,-1.263481,4.646328,-4.224534,4.616934,3.779521,0.258756,-0.605028,8.948941,4.435919,8.796346,8.517892,7.276001,6.984976,-0.751677,-9.243501,-3.656347,-8.333327,7.847157,-2.162733,-4.706721,-4.654483,1.783785,-4.495505,4.564614,-9.993067,-6.014209,2.580401,5.418596,-5.632925,1.774781,9.249613,-5.778648,9.207157,3.459267,-2.020253,9.877462,7.190112,3.437955,1.810031,2.333547,5.035765,7.305959,1.898765,6.751600,-5.996549,5.814838,-0.114418,7.625922,5.146382,3.842326,3.855397,-3.943483,-2.890490,-8.169645,8.310653,5.292404,8.592710,3.642751,5.987685,1.267655,1.757578,-4.855745,-5.823460,7.371880,-5.221128,7.079091,3.586345,-0.594478,0.386371,7.365660,-3.809063,5.850203,0.918523,2.744603,2.459945,-3.803538,5.228795,4.247098,7.968737,9.797142,6.255276,8.521522,-4.407329,-7.289105,-5.995998,-0.565940,-6.416601,7.749208,0.043635,3.267281,3.086646,9.608360,-8.555930,-3.726350,-8.265609,6.207520,-4.640750,-9.373128,-0.027555,-1.941439,8.759500,4.355658,-3.209754,9.394596,1.991304,-7.380443,4.609015,4.115575,-2.378173,6.963818,9.459766,6.466621,2.457456,4.414329,-7.883575,-6.774023,-0.270926,-0.416605,-6.602726,-9.693293,-1.839374,-3.925384,0.892997,5.499197,1.473771,-3.905089,7.079641,-4.336601,4.523380,-2.227494,0.025232,8.919217,-0.218605,-9.930757,-7.180778,5.239098,-5.784529,-5.426938,4.207987,9.553570,-4.532228,-4.008272,6.108400,-5.887274,-9.797571,0.062015,7.184597,1.490300,-6.193282,5.752045,7.268522,2.856272,-3.826599,4.749954,7.113840,2.726076,-9.869003,6.876845,-5.998856,-0.703555,-3.630639,8.515615,0.153902,6.860181,-9.724071,-7.557134,0.560278,1.748922,3.100612,-4.744776,-5.022224,-1.697699,3.754056,-3.433136,2.326663,-8.121750,-0.628182,6.565931,-0.707892,0.907663,9.939174,-9.200537,2.050699,6.306042,-5.212433,2.281683,3.972092,4.030796,1.218422,-6.590830,3.408958,-4.189353,-9.890727,2.471840,3.923201,-8.755669,-8.663176,8.916195,-4.719459,-3.925948,-3.376118,4.942171,9.255538,-9.139015,5.644419,0.384603,7.835685,-1.204165,3.658947,3.921413,0.351296,-4.258979,-0.045630,0.817313,-0.878024,-2.177245,-7.054180,-4.857145,-1.737717,-2.419419,1.696408,-2.069843,-7.865079,4.151575,-6.357114,-7.945388,-2.986936,7.900903,-0.824212,2.502884,-1.168879,-2.088036,-3.216569,-4.604128,9.263615,-7.480730,-2.154381,-3.029627,3.464349,4.614585,-9.924831,0.083181,-0.783668,9.000668,-2.897540,3.088419,-9.411358,5.029304,-5.492961,-9.149334,-6.474252,-7.920866,0.504013,4.080681,-1.434954,6.494722,-8.870310,6.214626,7.047909,-5.802405,-4.581366,1.206176,1.929684,0.197960,-9.503180,8.524196,-4.028371,-4.981412,-2.318840,-3.110507,-5.733336,1.623845,7.852712,0.739206,-6.771396,-5.580747,1.916432,2.225529,-2.528184,-4.961190,-0.871500,6.178412,2.072429,4.332061,-6.222425,5.119264,1.930858,5.574816,6.928630,2.606268,-2.705615,-3.372997,8.317162,-9.451399,-3.825597,5.028851,0.483542,7.674996,-2.550448,-1.887274,3.499451,6.233032,2.240790,9.361764,4.477878,-5.402386,-0.079175,6.975301,-6.514792,3.468015,-7.745676,-1.823658,2.216618,-4.235404,-9.133373,-5.921717,-3.646208,-4.941483,2.213609,0.143073,-4.890988,-0.113369,-1.932933,6.929713,-5.477274,-2.614590,1.476387,-0.695762,-2.561604,-3.432722,3.204137,-1.253412,-9.299473,2.548755,-5.929823,-4.771248,-0.577268,9.572605,-0.841443,-1.961613,4.936011,7.403793,1.896118,-0.582468,-2.694352,-0.557055,4.434995,-0.373380,0.447074,4.631623,-1.994639,-1.902314,3.005497,8.884361,-6.777693,-1.262005,-7.736875,-7.406936,1.753037,-2.475777,3.389447,5.121836,4.455547,-5.778108,-6.745179,2.240993,4.820682,5.600845,8.878381,-4.563032,-9.077997,-7.401201,-1.659252,-9.917933,4.236661,-4.849908,2.693217,4.567445,7.141990,9.936739,-6.249126,-9.877009,4.501309,-2.897772,-9.292536,-5.638626,5.610969,-6.631580,-5.559903,0.957983,0.476929,-0.703471,7.762946,1.539720,-2.467420,-6.919238,0.926223,-7.327894,9.148685,-9.383300,-9.780755,-2.979297,7.117346,2.532282,-5.879167,8.470730,-4.301241,-6.124938,6.537100,-0.233378,0.483287,-6.773196,3.878823,4.141364,4.647331,2.982678,-9.286267,3.808280,-8.480199,3.894699,9.546693,-9.676250,2.343015,-0.351980,-0.560713,-8.286553,3.292266,2.890753,4.560615,0.593214,-1.999026,-3.512115,1.283448,-9.073049,0.177652,-4.527759,-6.363484,-2.152072,4.322431,-2.483239,-0.810407,4.787365,-1.664249,-2.272710,8.219045,-5.889126,-3.774949,5.930871,2.054382,5.465511,7.240211,3.779399,-8.416459,6.462217,-4.338591,-8.888925,-6.988394,4.375628,-4.302369,2.395448,2.285014,8.418025,-4.710904,0.773789,-3.593376,-2.444023,-6.842439,3.910594,-7.708261,6.091198,-7.767785,0.015600,1.131863,5.770209,-0.730727,-7.443584,1.866737,-0.609988,-3.906098,6.928118,-1.251588,-4.584212,9.330967,-3.708450,9.518764,9.439535,6.536042,-8.601352,2.925940,-4.103029,-2.475314,3.004494,-5.218289,-7.462105,-9.609349,2.971386,1.629103,8.132721,8.485703,-6.006006,3.325159,-9.467136,-9.776400,-8.734629,3.758121,-6.363971,0.601316,8.000263,8.608365,-5.626342,4.115907,-1.367037,8.029653,3.835665,0.385016,0.266112,1.241639,3.484011,5.246074,8.760390,-7.781466,-3.902649,-3.390498,4.146007,0.509104,4.502616,6.804793,-2.815606,2.263410,4.891759,4.449710,-3.112173,7.826207,9.132996,7.423363,3.638963,-5.918179,2.065694,9.209029,-2.771134,-6.790348,8.055541,3.261893,-0.497661,5.876184,-4.450570,4.025724,-2.233452,-2.592852,3.240547,-8.709401,-1.315567,-4.658114,1.985939,-6.107335,3.441285,3.208052,3.884391,-4.544075,-4.297504,3.143615,-9.944131,3.947776,2.540339,-8.266866,0.531304,8.628473,0.817055,5.460067,7.485966,-0.381136,-4.083614,5.484730,7.030852,8.516444,-8.348367,-3.712800,9.620111,4.993407,7.932374,5.934734,-7.600996,-4.952234,7.525312,6.860870,-3.953224,2.366077,1.999962,-3.160998,-4.197657,-2.316843,-4.330280,5.690804,-2.322029,0.528397,6.868683,-4.787844,2.848342,0.890509,-9.370970,-5.829013,3.410544,2.380820,-6.801224,3.244690,-2.859102,4.575410,-9.775745,-0.198844,7.751456,-3.358622,0.096172,2.875868,-2.516913,4.021560,5.061459,6.508887,9.876417,3.187581,-0.389785,-2.963878,9.227966,0.611739,-2.673129,-6.968352,8.665313,-4.317813,-8.702751,-0.439676,4.999691,1.285703,4.160371,2.889770,-5.118708,-0.993163,1.581732,6.176057,1.341479,-1.372322,-5.258973,5.288377,8.431748,-9.951604,5.904745,-4.894593,-3.486669,8.643137,-2.964343,-9.429294,-0.344861,5.342340,7.561692,-3.853331,-8.560670,3.127570,6.968263,-9.846305,-8.420219,-7.418699,6.113061,-7.442205,7.527925,5.010443,-8.652786,-7.168222,6.545543,-3.970310,-9.907762,2.490078,2.570077,0.109084,6.998276,-1.286608,9.151689,-3.112233,1.561494,-2.862585,-2.538830,2.976331,-7.526477,9.258968,6.451000,-8.853320,-8.996528,-0.947724,-3.707718,5.399049,-5.375382,-7.450866,-5.753594,-2.853694,1.667110,-7.894349,0.632026,6.795715,4.257046,3.316388,-4.548639,-9.272518,4.442475,0.607101,3.058898,0.233706,-6.149992,8.204776,-1.157184,-3.745217,-8.877614,-0.698353,-0.057443,0.783039,-5.125387,8.066097,3.025911,-4.431603,-8.305320,-4.553812,-7.921398,4.554345,5.177779,6.070431,1.544763,-8.295619,3.782390,6.141375,-6.233781,5.684691,2.495844,1.493254,4.103226,0.121087,6.992802,0.502060,4.525709,-9.803039,4.675498,8.959975,-4.754195,-5.847163,-1.003568,0.925608,7.358350,8.937010,0.067670,6.262855,-5.514333,0.066041,-1.715770,4.646793,1.032946,1.272719,-8.141177,0.333993,-0.294444,-9.869796,4.457673,6.046123,-8.525553,2.013431,9.554453,-1.118696,9.775328,-3.635681,-1.320573,-0.481594,8.006998,-4.147855,-9.946289,-8.632558,-1.979898,7.719526,3.333442,-8.454123,5.645209,7.094794,-8.414684,0.468488,4.070346], dtype = "float32")#candidate|3199|(1215,)|const|float32
call_3198 = func_2104_call(relay.reshape(const_3199.astype('float32'), [15, 9, 9]))
call_3200 = func_2104_call(relay.reshape(const_3199.astype('float32'), [15, 9, 9]))
output = relay.Tuple([bop_3169,bop_3173,uop_3179,uop_3184,uop_3194,call_3198,const_3199,])
output2 = relay.Tuple([bop_3172,bop_3176,uop_3181,uop_3186,uop_3194,call_3200,const_3199,])
func_3202 = relay.Function([var_3154,], output)
mod['func_3202'] = func_3202
mod = relay.transform.InferType()(mod)
mutated_mod['func_3202'] = func_3202
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3203 = relay.var("var_3203", dtype = "bool", shape = (286, 1))#candidate|3203|(286, 1)|var|bool
func_3202_call = mutated_mod.get_global_var('func_3202')
call_3204 = func_3202_call(var_3203)
output = call_3204
func_3205 = relay.Function([var_3203], output)
mutated_mod['func_3205'] = func_3205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3033_call = mod.get_global_var('func_3033')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_3240 = func_3033_call()
call_3241 = func_3033_call()
output = call_3240
output2 = call_3241
func_3244 = relay.Function([], output)
mod['func_3244'] = func_3244
mod = relay.transform.InferType()(mod)
mutated_mod['func_3244'] = func_3244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mutated_mod.get_global_var('func_3244')
call_3245 = func_3244_call()
output = call_3245
func_3246 = relay.Function([], output)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1785_call = mod.get_global_var('func_1785')
func_1787_call = mutated_mod.get_global_var('func_1787')
call_3334 = func_1785_call()
call_3335 = func_1785_call()
uop_3339 = relay.sigmoid(call_3334.astype('float32')) # shape=(1, 1, 9)
uop_3341 = relay.sigmoid(call_3335.astype('float32')) # shape=(1, 1, 9)
func_2817_call = mod.get_global_var('func_2817')
func_2819_call = mutated_mod.get_global_var('func_2819')
call_3353 = func_2817_call()
call_3354 = func_2817_call()
bop_3357 = relay.logical_or(call_3334.astype('bool'), call_3353.astype('bool')) # shape=(1, 1, 9)
bop_3360 = relay.logical_or(call_3335.astype('bool'), call_3354.astype('bool')) # shape=(1, 1, 9)
const_3364 = relay.const([[[3.900065,6.900296,-7.330920,1.936341,8.446349,9.501524,9.360364,2.811084,-9.143310],[3.341739,-3.340495,1.146677,9.332715,-8.928923,5.998515,-5.612827,-3.021035,-2.823126],[3.789283,-6.603767,-4.295628,-9.181036,-5.942105,-0.843039,0.114879,-8.508702,6.331763],[-7.018624,-1.233163,-2.394519,0.398977,-7.045374,5.035680,-7.369222,-8.924735,5.650459],[-2.407800,9.562996,0.321130,1.620266,6.478365,7.476645,1.158278,4.156608,-7.889191],[4.008119,5.468312,6.366305,6.305937,2.251938,5.566228,-7.429452,-8.482768,-1.149090],[8.776525,-3.929562,2.637258,1.911422,9.731432,-8.544274,6.727133,7.957562,9.463139],[0.036989,-0.294648,-5.852925,5.583327,8.226382,-0.939182,9.299642,2.971995,-7.648700],[1.300705,-6.779202,5.033455,6.185154,-8.279995,9.562429,2.419809,-6.964445,6.131067],[3.186580,7.342185,-4.151913,-7.481680,3.276831,8.801186,-6.329152,-6.570124,2.433121],[4.849985,-2.909904,-7.393118,7.884655,-7.196163,3.612957,5.958863,-2.186943,-3.127830],[-4.326002,-9.361711,-3.144864,-5.738923,8.623850,6.121141,-3.230172,8.817419,8.182700],[-1.259769,6.798338,-5.443403,-3.875474,-3.523466,0.021152,5.216066,5.132161,1.886062],[8.241208,8.826766,-7.316263,2.446778,3.879231,7.609584,-9.855044,-1.819684,-2.879695]]], dtype = "float32")#candidate|3364|(1, 14, 9)|const|float32
bop_3365 = relay.logical_xor(uop_3339.astype('uint64'), const_3364.astype('uint64')) # shape=(1, 14, 9)
bop_3368 = relay.logical_xor(uop_3341.astype('uint64'), const_3364.astype('uint64')) # shape=(1, 14, 9)
output = relay.Tuple([bop_3357,bop_3365,])
output2 = relay.Tuple([bop_3360,bop_3368,])
func_3379 = relay.Function([], output)
mod['func_3379'] = func_3379
mod = relay.transform.InferType()(mod)
mutated_mod['func_3379'] = func_3379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3379_call = mutated_mod.get_global_var('func_3379')
call_3380 = func_3379_call()
output = call_3380
func_3381 = relay.Function([], output)
mutated_mod['func_3381'] = func_3381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1480_call = mod.get_global_var('func_1480')
func_1482_call = mutated_mod.get_global_var('func_1482')
call_3401 = relay.TupleGetItem(func_1480_call(), 1)
call_3402 = relay.TupleGetItem(func_1482_call(), 1)
var_3405 = relay.var("var_3405", dtype = "float64", shape = (8, 10, 9))#candidate|3405|(8, 10, 9)|var|float64
bop_3406 = relay.not_equal(call_3401.astype('bool'), var_3405.astype('bool')) # shape=(8, 10, 9)
bop_3409 = relay.not_equal(call_3402.astype('bool'), var_3405.astype('bool')) # shape=(8, 10, 9)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_3410 = relay.TupleGetItem(func_574_call(), 1)
call_3411 = relay.TupleGetItem(func_575_call(), 1)
func_1829_call = mod.get_global_var('func_1829')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_3412 = relay.TupleGetItem(func_1829_call(), 0)
call_3413 = relay.TupleGetItem(func_1831_call(), 0)
uop_3458 = relay.acosh(call_3410.astype('float64')) # shape=(2, 13, 11)
uop_3460 = relay.acosh(call_3411.astype('float64')) # shape=(2, 13, 11)
output = relay.Tuple([bop_3406,call_3412,uop_3458,])
output2 = relay.Tuple([bop_3409,call_3413,uop_3460,])
func_3467 = relay.Function([var_3405,], output)
mod['func_3467'] = func_3467
mod = relay.transform.InferType()(mod)
mutated_mod['func_3467'] = func_3467
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3468 = relay.var("var_3468", dtype = "float64", shape = (8, 10, 9))#candidate|3468|(8, 10, 9)|var|float64
func_3467_call = mutated_mod.get_global_var('func_3467')
call_3469 = func_3467_call(var_3468)
output = call_3469
func_3470 = relay.Function([var_3468], output)
mutated_mod['func_3470'] = func_3470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1480_call = mod.get_global_var('func_1480')
func_1482_call = mutated_mod.get_global_var('func_1482')
call_3508 = relay.TupleGetItem(func_1480_call(), 0)
call_3509 = relay.TupleGetItem(func_1482_call(), 0)
func_3467_call = mod.get_global_var('func_3467')
func_3470_call = mutated_mod.get_global_var('func_3470')
var_3515 = relay.var("var_3515", dtype = "float64", shape = (720,))#candidate|3515|(720,)|var|float64
call_3514 = relay.TupleGetItem(func_3467_call(relay.reshape(var_3515.astype('float64'), [8, 10, 9])), 1)
call_3516 = relay.TupleGetItem(func_3470_call(relay.reshape(var_3515.astype('float64'), [8, 10, 9])), 1)
func_2256_call = mod.get_global_var('func_2256')
func_2259_call = mutated_mod.get_global_var('func_2259')
var_3533 = relay.var("var_3533", dtype = "uint64", shape = (105,))#candidate|3533|(105,)|var|uint64
var_3534 = relay.var("var_3534", dtype = "uint64", shape = (210,))#candidate|3534|(210,)|var|uint64
call_3532 = relay.TupleGetItem(func_2256_call(relay.reshape(var_3533.astype('uint64'), [1, 7, 15]), relay.reshape(var_3534.astype('uint64'), [2, 7, 15]), ), 0)
call_3535 = relay.TupleGetItem(func_2259_call(relay.reshape(var_3533.astype('uint64'), [1, 7, 15]), relay.reshape(var_3534.astype('uint64'), [2, 7, 15]), ), 0)
output = relay.Tuple([call_3508,call_3514,var_3515,call_3532,var_3533,var_3534,])
output2 = relay.Tuple([call_3509,call_3516,var_3515,call_3535,var_3533,var_3534,])
func_3543 = relay.Function([var_3515,var_3533,var_3534,], output)
mod['func_3543'] = func_3543
mod = relay.transform.InferType()(mod)
var_3544 = relay.var("var_3544", dtype = "float64", shape = (720,))#candidate|3544|(720,)|var|float64
var_3545 = relay.var("var_3545", dtype = "uint64", shape = (105,))#candidate|3545|(105,)|var|uint64
var_3546 = relay.var("var_3546", dtype = "uint64", shape = (210,))#candidate|3546|(210,)|var|uint64
output = func_3543(var_3544,var_3545,var_3546,)
func_3547 = relay.Function([var_3544,var_3545,var_3546,], output)
mutated_mod['func_3547'] = func_3547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_663_call = mod.get_global_var('func_663')
func_664_call = mutated_mod.get_global_var('func_664')
call_3703 = func_663_call()
call_3704 = func_663_call()
output = relay.Tuple([call_3703,])
output2 = relay.Tuple([call_3704,])
func_3713 = relay.Function([], output)
mod['func_3713'] = func_3713
mod = relay.transform.InferType()(mod)
output = func_3713()
func_3714 = relay.Function([], output)
mutated_mod['func_3714'] = func_3714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1785_call = mod.get_global_var('func_1785')
func_1787_call = mutated_mod.get_global_var('func_1787')
call_3849 = func_1785_call()
call_3850 = func_1785_call()
output = relay.Tuple([call_3849,])
output2 = relay.Tuple([call_3850,])
func_3852 = relay.Function([], output)
mod['func_3852'] = func_3852
mod = relay.transform.InferType()(mod)
output = func_3852()
func_3853 = relay.Function([], output)
mutated_mod['func_3853'] = func_3853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3852_call = mod.get_global_var('func_3852')
func_3853_call = mutated_mod.get_global_var('func_3853')
call_3854 = relay.TupleGetItem(func_3852_call(), 0)
call_3855 = relay.TupleGetItem(func_3853_call(), 0)
output = relay.Tuple([call_3854,])
output2 = relay.Tuple([call_3855,])
func_3863 = relay.Function([], output)
mod['func_3863'] = func_3863
mod = relay.transform.InferType()(mod)
output = func_3863()
func_3864 = relay.Function([], output)
mutated_mod['func_3864'] = func_3864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1480_call = mod.get_global_var('func_1480')
func_1482_call = mutated_mod.get_global_var('func_1482')
call_3872 = relay.TupleGetItem(func_1480_call(), 1)
call_3873 = relay.TupleGetItem(func_1482_call(), 1)
output = call_3872
output2 = call_3873
func_3893 = relay.Function([], output)
mod['func_3893'] = func_3893
mod = relay.transform.InferType()(mod)
mutated_mod['func_3893'] = func_3893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3893_call = mutated_mod.get_global_var('func_3893')
call_3894 = func_3893_call()
output = call_3894
func_3895 = relay.Function([], output)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3916 = func_2967_call()
call_3917 = func_2967_call()
uop_3939 = relay.tan(call_3916.astype('float64')) # shape=(1, 1, 9)
uop_3941 = relay.tan(call_3917.astype('float64')) # shape=(1, 1, 9)
output = relay.Tuple([uop_3939,])
output2 = relay.Tuple([uop_3941,])
func_3966 = relay.Function([], output)
mod['func_3966'] = func_3966
mod = relay.transform.InferType()(mod)
output = func_3966()
func_3967 = relay.Function([], output)
mutated_mod['func_3967'] = func_3967
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3972 = relay.var("var_3972", dtype = "float32", shape = (12, 13, 1))#candidate|3972|(12, 13, 1)|var|float32
uop_3973 = relay.erf(var_3972.astype('float32')) # shape=(12, 13, 1)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_3975 = func_3064_call()
call_3976 = func_3064_call()
func_2780_call = mod.get_global_var('func_2780')
func_2783_call = mutated_mod.get_global_var('func_2783')
call_3977 = relay.TupleGetItem(func_2780_call(relay.reshape(call_3975.astype('bool'), [1, 13, 14])), 1)
call_3978 = relay.TupleGetItem(func_2783_call(relay.reshape(call_3975.astype('bool'), [1, 13, 14])), 1)
uop_3980 = relay.atanh(uop_3973.astype('float32')) # shape=(12, 13, 1)
bop_3982 = relay.bitwise_xor(uop_3980.astype('int8'), relay.reshape(uop_3973.astype('int8'), relay.shape_of(uop_3980))) # shape=(12, 13, 1)
uop_3988 = relay.sin(bop_3982.astype('float32')) # shape=(12, 13, 1)
func_3966_call = mod.get_global_var('func_3966')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_3994 = relay.TupleGetItem(func_3966_call(), 0)
call_3995 = relay.TupleGetItem(func_3967_call(), 0)
output = relay.Tuple([call_3975,call_3977,uop_3988,call_3994,])
output2 = relay.Tuple([call_3976,call_3978,uop_3988,call_3995,])
func_3998 = relay.Function([var_3972,], output)
mod['func_3998'] = func_3998
mod = relay.transform.InferType()(mod)
var_3999 = relay.var("var_3999", dtype = "float32", shape = (12, 13, 1))#candidate|3999|(12, 13, 1)|var|float32
output = func_3998(var_3999)
func_4000 = relay.Function([var_3999], output)
mutated_mod['func_4000'] = func_4000
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4013 = relay.var("var_4013", dtype = "float64", shape = (12, 14, 12))#candidate|4013|(12, 14, 12)|var|float64
uop_4014 = relay.log(var_4013.astype('float64')) # shape=(12, 14, 12)
func_3064_call = mod.get_global_var('func_3064')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_4028 = func_3064_call()
call_4029 = func_3064_call()
output = relay.Tuple([uop_4014,call_4028,])
output2 = relay.Tuple([uop_4014,call_4029,])
func_4041 = relay.Function([var_4013,], output)
mod['func_4041'] = func_4041
mod = relay.transform.InferType()(mod)
var_4042 = relay.var("var_4042", dtype = "float64", shape = (12, 14, 12))#candidate|4042|(12, 14, 12)|var|float64
output = func_4041(var_4042)
func_4043 = relay.Function([var_4042], output)
mutated_mod['func_4043'] = func_4043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_983_call = mod.get_global_var('func_983')
func_985_call = mutated_mod.get_global_var('func_985')
call_4084 = func_983_call()
call_4085 = func_983_call()
output = relay.Tuple([call_4084,])
output2 = relay.Tuple([call_4085,])
func_4091 = relay.Function([], output)
mod['func_4091'] = func_4091
mod = relay.transform.InferType()(mod)
output = func_4091()
func_4092 = relay.Function([], output)
mutated_mod['func_4092'] = func_4092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_802_call = mod.get_global_var('func_802')
func_803_call = mutated_mod.get_global_var('func_803')
call_4107 = relay.TupleGetItem(func_802_call(), 0)
call_4108 = relay.TupleGetItem(func_803_call(), 0)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_4111 = relay.TupleGetItem(func_411_call(), 0)
call_4112 = relay.TupleGetItem(func_413_call(), 0)
output = relay.Tuple([call_4107,call_4111,])
output2 = relay.Tuple([call_4108,call_4112,])
func_4126 = relay.Function([], output)
mod['func_4126'] = func_4126
mod = relay.transform.InferType()(mod)
mutated_mod['func_4126'] = func_4126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4126_call = mutated_mod.get_global_var('func_4126')
call_4127 = func_4126_call()
output = call_4127
func_4128 = relay.Function([], output)
mutated_mod['func_4128'] = func_4128
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4148 = relay.var("var_4148", dtype = "float32", shape = (11, 16, 2))#candidate|4148|(11, 16, 2)|var|float32
var_4149 = relay.var("var_4149", dtype = "float32", shape = (11, 16, 2))#candidate|4149|(11, 16, 2)|var|float32
bop_4150 = relay.minimum(var_4148.astype('float32'), relay.reshape(var_4149.astype('float32'), relay.shape_of(var_4148))) # shape=(11, 16, 2)
func_1846_call = mod.get_global_var('func_1846')
func_1847_call = mutated_mod.get_global_var('func_1847')
call_4158 = relay.TupleGetItem(func_1846_call(), 0)
call_4159 = relay.TupleGetItem(func_1847_call(), 0)
func_2408_call = mod.get_global_var('func_2408')
func_2409_call = mutated_mod.get_global_var('func_2409')
call_4173 = relay.TupleGetItem(func_2408_call(), 0)
call_4174 = relay.TupleGetItem(func_2409_call(), 0)
bop_4177 = relay.maximum(call_4173.astype('float32'), relay.reshape(call_4158.astype('float32'), relay.shape_of(call_4173))) # shape=(1, 1, 9)
bop_4180 = relay.maximum(call_4174.astype('float32'), relay.reshape(call_4159.astype('float32'), relay.shape_of(call_4174))) # shape=(1, 1, 9)
func_2383_call = mod.get_global_var('func_2383')
func_2386_call = mutated_mod.get_global_var('func_2386')
var_4187 = relay.var("var_4187", dtype = "float32", shape = (1200,))#candidate|4187|(1200,)|var|float32
const_4188 = relay.const([6.732314,6.170306,3.118764,-0.495124,0.447490,-5.895839,-9.497956,-4.605576,0.759271,-6.735591,4.705133,3.387461,-1.431823,5.508671,0.993935,-1.872098,6.536952,9.402382,7.592223,0.838502,2.257453,8.734261,-1.077278,9.315446,-1.733123,1.826651,1.774171,9.721612,3.088780,6.475990,5.861998,8.210627,6.186119,5.863224,-9.513303,6.697981,6.157832,6.735924,2.817377,0.067709,-2.473913,1.283051,-3.625347,-1.463600,1.591476,-1.951241,9.994098,5.339598,-0.127120,8.462757,-5.661441,-9.074545,-6.873104,4.595056,-2.747865,9.385232,3.091319,-3.008047,3.036841,4.045456,2.849998,5.995174,0.550467,8.506710,-3.672612,2.458911,-8.993717,-3.718683,6.916450,-0.089052,-7.777671,2.034966,-5.623270,7.440910,-8.637248,-1.723611,-7.869031,-1.707353,7.652555,4.740377,-7.755432,-8.295409,3.375559,0.236070,-9.352793,-0.278087,6.397275,5.461163,-3.615143,-7.892810,6.170509,-2.672002,-1.818567,-2.743735,-6.688159,2.149783,-0.105861,5.815648,-0.485046,-4.622800,-3.402724,-5.234263,-8.849910,0.198109,-2.122778,2.437015,3.876161,-4.883127,-6.328265,5.428329,-3.571537,-1.272165,-7.839737,-8.076932,-0.522357,7.901102,-0.979507,7.988922,1.450328,3.979581,-6.632018,-3.654695,-2.157201,7.753265,1.581524,9.850894,-3.016142,-2.853251,-9.712819,3.340116,4.026019,0.978302,-2.216348,8.103534,-2.976515,-1.913037,7.726051,-5.116449,2.657585,3.253410,-2.448813,-1.586873,-1.975295,0.340167,-2.607468,3.167710,3.705467,3.834846,8.046523,-9.720091,4.328748,-1.459090,1.564842,-8.354158,2.217083,1.126497,-6.217955,-1.452449,-4.457556,2.145473,-9.013492,-5.293740,-1.170881,-8.740768,-9.316552,7.141201,6.620821,6.552060,-6.856626,8.183533,5.795051,9.946514,-7.708845,-0.372699,9.744630,9.097133,-6.894368,5.143343,0.698754,3.509396,-4.216216,8.576974,-7.486195,-5.701630,-8.659004,-0.815889,-9.010193,-8.037053,1.736808,3.504610,-6.564656,0.981221,9.834469,4.517001,-2.999494,-0.147742,3.391572,-0.487517,-5.803384,-7.447462,-2.526602,-2.529734,-5.035011,5.705032,0.162873,-4.879833,-1.233090,9.005772,6.948661,-4.787240,0.946031,-3.254518,6.557893,-1.164687,-2.842386,-1.786155,-0.310059,7.338290,6.194314,-1.018427,-5.658584,5.003165,-5.708911,-0.718451,6.586552,2.104025,0.399990,-7.411185,-1.159616,0.758130,2.555788,3.696271,-7.314607,6.724835,-9.506054,6.676454,-0.971016,2.186726,3.997865,-7.800870,-6.344483,3.706789,-0.034388,-9.112027,-4.263223,1.623617,-9.355429,0.917058,2.535028,-3.108723,6.824900,-1.001970,-8.938371,-8.724157,3.293576,9.949855,6.024045,-9.286991,-1.679075,-7.545799,-0.284798,-6.391330,4.738446,9.065061,-6.657982,-3.356866,6.513362,-1.749677,-0.291619,2.797083,1.285008,8.589629,8.019704,-7.991494,4.242379,1.087059,-8.644748,-6.984508,4.872099,2.254474,0.836292,3.869224,-8.605353,9.661202,2.617791,9.482137,5.310145,0.062142,-6.788557,-0.681938,-6.860255,6.202618,1.095597,-4.513057,5.050665,2.178002,0.354375,-2.159188,-2.830936,-4.717928,-3.252045,-9.712191,1.616302,2.529789,-8.284797,1.810438,2.988076,8.226523,-2.631265,7.300900,9.486523,-0.755510,-9.705564,2.754331,-6.050369,-3.559441,2.747299,-5.345544,-7.833254,-8.634181,1.990568,2.536698,-9.102089,-1.881481,0.159325,-1.652420,-4.174085,4.297665,9.648588,3.796253,3.065522,4.142614,-0.079676,3.124922,8.327367,0.925140,0.789600,4.181517,-6.116162,-4.296775,2.897581,-0.865263,5.042544,-4.460738,-1.166797,7.142437,5.611364,-4.640910,-2.453824,-8.062003,9.313135,6.915429,5.333282,-0.482058,-9.761673,8.728176,-7.474469,5.126841,0.080013,-5.215751,2.607832,5.563277,-9.401865,-6.803432,5.893669,-9.656943,7.151306,5.247272,-5.592628,-2.671483,-6.104943,0.491208,7.077307,6.211590,-1.942434,4.736554,1.852283,8.081274,-0.778151,-1.454989,-1.233265,1.769992,-3.786629,-8.809656,-2.187546,0.118754,-9.052232,7.875469,0.365303,1.400690,7.899074,4.520320,8.288661,-1.547209,3.548484,-4.088792,-4.731833,9.590636,-4.176347,4.212389,-1.569097,-8.893294,7.725174,-0.093263,-1.262849,1.102845,-9.260468,-8.059828,8.105569,-6.205383,6.884452,-6.638197,-9.124317,6.975632,-5.514655,7.801874,7.978823,5.458681,-6.807348,-7.164860,9.252241,-1.874476,-6.323847,-4.128750,5.365526,-1.780124,0.022124,-6.091529,-0.376388,-2.494929,0.072450,7.226820,1.230542,9.918983,9.667402,-9.654789,9.101875,-8.788206,6.652137,2.953807,2.508311,-7.969849,9.102802,-2.593606,-6.046597,-0.213665,6.537110,-0.197433,-1.047857,-7.259188,6.528470,0.975870,3.684710,5.796755,-8.099010,3.459955,-8.296786,-7.192902,1.653232,-0.722219,8.960001,7.151043,-2.956810,-3.891389,2.101765,-0.041700,7.264686,-6.502535,-1.496071,-0.544801,-7.395393,-6.585219,7.093334,-5.081773,-1.056451,-5.766622,4.452504,-6.970622,1.200991,9.868251,1.488660,-7.084145,0.780561,9.807281,-1.636902,-3.307846,9.743409,1.820361,6.648326,4.831790,-0.457911,4.359827,3.907488,-9.101970,-4.314855,-3.688860,1.181730,4.537213,7.758506,-4.218838,-6.672143,-0.003826,-7.818778,-4.287640,-4.447840,5.971564,9.816710,-0.971501,-2.241886,2.299750,-0.614168,-6.133349,-7.371357,-4.300565,-9.245030,4.439437,8.237998,-8.608620,-4.378154,9.543875,3.162842,5.595452,-7.484565,7.337263,-6.064881,6.583916,-5.248111,9.353425,0.230876,-4.096516,-4.316637,-3.283054,-4.600469,7.975864,6.635737,2.843860,4.982339,0.516419,-3.528541,-4.801742,-9.672897,-4.090507,9.644667,9.011600,1.141839,-7.651378,-2.798976,-9.987858,-0.827623,2.265749,-5.439383,-7.752045,6.383974,8.699199,-6.450415,8.841252,-5.564970,-9.710785,4.947778,-9.797212,2.499189,-1.519642,-7.383429,-0.958221,2.073825,-3.260163,-5.905593,8.836234,0.941900,-2.234773,2.508264,-9.614033,6.136553,1.336325,-9.194352,7.234582,9.105979,9.107188,-1.327356,-3.782849,6.979570,-6.590369,0.449946,-2.373460,-3.894309,-7.023930,-8.837233,7.375978,7.697950,-8.570549,8.520682,-6.757662,8.962592,-0.670270,8.303674,2.041023,0.068960,6.982915,-7.848287,0.399739,-3.657007,-8.300379,-9.880166,-7.989942,-9.988884,-9.464545,-6.136326,-3.018850,-7.920154,-9.253226,7.404867,8.443156,4.903889,5.344536,-6.879404,-2.401310,3.345384,1.302557,3.234760,0.032632,-0.125577,6.227309,-2.798395,-8.303723,-1.793655,9.344073,0.154858,-2.413987,1.362477,-3.761618,1.966004,-5.473818,7.037263,-7.285927,9.151940,-1.138155,2.323835,-2.969532,-9.413684,9.801340,9.764946,-5.037178,8.624093,7.486837,9.131898,-9.900228,6.998868,1.268307,-8.066830,3.410152,7.344096,6.074827,3.890186,5.781361,-2.331415,-4.390395,5.898734,-6.540171,0.740906,7.594882,7.219011,1.541647,-9.720809,4.836101,9.477862,-1.382456,2.167839,3.085280,9.445260,-6.616877,7.216345,-9.851261,2.648237,4.686467,-9.136138,0.087302,-6.644851,-8.033473,9.288390,9.696891,-1.328862,-6.882965,2.233376,-8.212109,-0.112094,3.243200,4.890373,-6.524881,-7.530564,-5.313590,-6.997859,6.194184,-1.228597,9.876138,1.236056,-2.109329,-8.657066,7.414212,9.696944,-4.082953,-5.470136,6.565460,9.793117,2.614059,-4.795514,8.249893,4.754071,7.698185,-5.996124,-2.067474,-9.856830,-2.546714,5.981147,-9.692741,6.065720,-6.395343,-8.350814,-9.963259,6.876937,-2.429624,2.053795,-0.927749,-2.083808,-0.242945,-4.623134,-1.195714,-9.902398,6.980129,9.804877,-4.627517,-4.224879,-2.698754,-3.123462,4.989139,-9.222673,5.781479,8.597254,6.522135,-3.547292,-7.898646,-4.545793,3.676994,6.227446,-6.882197,-2.122823,-4.851648,8.786881,-6.049690,3.280120,1.872389,6.664909,0.448594,-2.018835,-9.563213,-6.578418,6.410216,6.636217,4.221386,4.414269,3.317004,-7.445531,-4.307422,9.547022,-4.471041,-3.990070,-1.318723,-1.599963,-5.591038,-4.243641,3.944082,-4.568052,4.268306,4.125332,-7.925058,-9.886782,9.893239,7.478824,-8.882232,-7.283482,0.705125,-4.869903,-8.419045,6.272993,0.119382,3.540784,6.099448,7.424768,9.663408,8.116505,6.079906,-0.020114,8.855107,7.021385,-9.459537,-6.593223,-4.362158,7.607305,9.065355,-5.905669,8.909256,-3.086094,9.225087,1.024640,-5.370024,-1.779162,4.179603,-7.695987,9.482963,-0.384293,3.433782,7.674077,-0.317332,-5.200803,-6.615527,-0.704524,-6.395843,-3.602381,2.707626,6.123215,-2.226429,5.483539,-8.582695,-7.255717,1.492626,1.262629,7.341763,9.037464,4.910570,-6.745747,-2.537509,0.789467,4.468936,-5.171851,-6.828121,-2.392392,1.844058,-4.902869,-6.625986,3.908318,8.976383,-9.687252,-4.455095,-1.373622,-5.397390,1.607621,-4.932641,9.849520,-5.410236,-2.594453,6.083132,9.994661,-0.387542,-5.318014,5.993444,7.807873,-8.059034,4.700434,8.198174,4.816473,-0.760361,-2.048088,7.879108,-7.426805,5.070634,-9.841717,-9.737370,4.140298,6.228784,0.109191,-5.612040,-1.067961,-2.849608,1.069322,8.804602,8.474586,4.244025,-3.739709,-1.754862,-7.557484,1.407161,-3.397267,-3.799212,1.115319,-9.017227,-2.433256,1.429430,8.433303,1.337812,3.318517,6.986296,-6.131630,-1.532072,-3.263671,-6.129955,-0.401760,5.120729,6.189209,-7.782647,-7.497825,4.613635,2.270334,4.331297,-6.040504,8.474050,2.177700,5.164850,0.535784,5.364573,-4.149036,-6.356362,1.657481,0.902647,-8.018741,8.228166,-5.278515,1.308517,4.349723,6.291768,3.378905,0.246970,1.086755,0.515106,-2.882330,-6.788918,-2.713334,9.958642,7.803452,-4.499124,5.783553,-5.358454,-3.923160,7.248883,-4.937847,4.447582,-2.280091,-4.858933,9.383344,-9.495788,-2.998610,-0.295088,-5.954604,4.795799,5.742795,7.292584,7.015544,-3.822389,6.330221,-8.322283,-2.957161,-7.419927,-9.796637,7.168397,-9.521959,-3.752577,-6.819553,8.778029,-9.224478,-0.020010,-0.954907,-7.674479,2.710525,6.537562,9.607359,-9.781931,8.040887,-4.366130,-8.972848,-9.469529,8.487371,6.960324,4.487949,-6.385136,6.660621,0.629566,-9.856450,-6.160003,6.934644,3.358914,3.902584,-9.994282,-8.385191,-5.105103,-3.134157,3.468660,2.435816,-8.654888,8.271581,2.226612,8.920210,-0.014743,-8.118747,-5.940665,-4.915033,-9.446678,0.489394,-5.722087,3.199205,-2.407761,8.816547,-0.521353,1.504855,-3.197994,4.779667,0.225952,-7.377319,3.219783,-1.494698,-0.082721,3.324349,-9.886972,-9.270205,-9.017691,-8.748700,2.565136,-3.413646,-6.846712,-8.755834,-9.857112,-2.158813,1.978092,7.563067,-6.291006,-2.342690,-6.897079,7.689092,-0.302588,1.646961,-3.626332,-3.714508,-9.839349,0.560335,-8.015789,4.538726,7.178248,-5.885502,-2.153809,5.836560,-9.687390,-3.957713,1.612523,1.219716,2.817922,-7.535194,-7.254169,4.391428,2.083480,-3.889964,9.771058,-9.247032,0.495034,6.270860,-8.271868,-6.478534,-1.174956,9.988375,9.694900,4.509668,-3.841853,-2.413314,-8.926326,1.162276,-2.226124,4.415783,6.082294,-7.566046,6.381573,-7.206954,9.243391,-8.786554,2.336161,3.747951,-8.400950,6.427672,4.549979,-5.982584,-3.917138,2.064862,1.036856,-4.308302,6.368203,6.897945,-3.074475,-1.187749,4.830820,9.457030,0.873019,5.882466,3.430463,-4.667532,-6.827912,9.349695,-6.429636,9.752871,2.693336,-0.514097,-1.888953,8.227852,2.013931,-0.620702,-0.575781,-7.240527,4.427172,-1.342967,-3.609471,5.149099,5.401440,7.717172,9.775645,9.415366,-3.629919,6.918514,1.139170,4.868948,8.583581,6.379243,3.570921,7.996860,9.148657,-9.593894,-3.458836,-9.708197,-2.320631,9.779032,-5.079439,-0.421582,-5.317737,-5.818444,3.935156,-1.191604,4.078927,-8.487010,1.681865,8.721946,2.292602,6.236657,3.739256,4.696888,1.462513,-0.188373,9.886556,2.431813,-3.787389,-8.029917,5.804655,-1.275945,-7.847977,-9.419409,-4.885060,3.180517,2.822271,6.256594,-6.838736,-8.851152,6.590295,-3.983093,0.566883,-8.913693,9.059612,5.321112,-2.363668,7.310599,1.227774,-5.456240,-1.737590,1.807008,-2.728172,-5.673724,-9.464746,3.906890,8.636044,-8.699216,9.553716,7.729174,3.253606,3.803324,-7.309547,7.540803,-2.043717,-7.329454,1.120903,-3.465981,-5.872428,-2.492393,9.695395,3.765801,4.260783,-7.034498,-7.110561,3.153719,-7.400197,3.625331,-6.359055,-1.422062,6.743189,4.689719,3.930905,-5.575457,-6.749408,-6.998160,-4.563361,6.762332,3.121547,-5.519236,9.076003,-5.350756,5.782483,-5.820263,-4.386654,-0.645674,1.145592,-8.018626,-0.852653,3.085533,1.827960,-8.498149,5.354085,-2.180620,5.494664,-3.434051,-5.002465,9.591643,3.276195,4.663448,-6.517249,5.538276,9.781613,-6.559499,-9.540999,8.903069,0.431782,-0.617360,6.410930,-8.366503,6.007106,5.962297,2.072365,6.317424,-9.288548,-5.381670,2.949674,5.114608,2.056263,-5.628996,8.170574,4.913608,9.006462,6.242893,-9.147732,-6.997525,-8.270613,-6.537858,-1.417300,-2.461619,-6.626022,3.391097,-7.444864,3.937478,2.085181,-5.285673,2.703359], dtype = "float32")#candidate|4188|(1260,)|const|float32
call_4186 = relay.TupleGetItem(func_2383_call(relay.reshape(var_4187.astype('float32'), [15, 8, 10]), relay.reshape(const_4188.astype('float32'), [9, 140]), ), 1)
call_4189 = relay.TupleGetItem(func_2386_call(relay.reshape(var_4187.astype('float32'), [15, 8, 10]), relay.reshape(const_4188.astype('float32'), [9, 140]), ), 1)
func_2230_call = mod.get_global_var('func_2230')
func_2233_call = mutated_mod.get_global_var('func_2233')
var_4192 = relay.var("var_4192", dtype = "float64", shape = (297,))#candidate|4192|(297,)|var|float64
var_4193 = relay.var("var_4193", dtype = "float32", shape = (45,))#candidate|4193|(45,)|var|float32
call_4191 = relay.TupleGetItem(func_2230_call(relay.reshape(var_4192.astype('float64'), [11, 3, 9]), relay.reshape(var_4193.astype('float32'), [45,]), ), 0)
call_4194 = relay.TupleGetItem(func_2233_call(relay.reshape(var_4192.astype('float64'), [11, 3, 9]), relay.reshape(var_4193.astype('float32'), [45,]), ), 0)
output = relay.Tuple([bop_4150,bop_4177,call_4186,var_4187,const_4188,call_4191,var_4192,var_4193,])
output2 = relay.Tuple([bop_4150,bop_4180,call_4189,var_4187,const_4188,call_4194,var_4192,var_4193,])
func_4203 = relay.Function([var_4148,var_4149,var_4187,var_4192,var_4193,], output)
mod['func_4203'] = func_4203
mod = relay.transform.InferType()(mod)
var_4204 = relay.var("var_4204", dtype = "float32", shape = (11, 16, 2))#candidate|4204|(11, 16, 2)|var|float32
var_4205 = relay.var("var_4205", dtype = "float32", shape = (11, 16, 2))#candidate|4205|(11, 16, 2)|var|float32
var_4206 = relay.var("var_4206", dtype = "float32", shape = (1200,))#candidate|4206|(1200,)|var|float32
var_4207 = relay.var("var_4207", dtype = "float64", shape = (297,))#candidate|4207|(297,)|var|float64
var_4208 = relay.var("var_4208", dtype = "float32", shape = (45,))#candidate|4208|(45,)|var|float32
output = func_4203(var_4204,var_4205,var_4206,var_4207,var_4208,)
func_4209 = relay.Function([var_4204,var_4205,var_4206,var_4207,var_4208,], output)
mutated_mod['func_4209'] = func_4209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1415_call = mod.get_global_var('func_1415')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_4215 = relay.TupleGetItem(func_1415_call(), 1)
call_4216 = relay.TupleGetItem(func_1417_call(), 1)
uop_4235 = relay.acosh(call_4215.astype('float64')) # shape=(1, 1, 9)
uop_4237 = relay.acosh(call_4216.astype('float64')) # shape=(1, 1, 9)
const_4251 = relay.const([[[-2,9,-4,-2,-3,3,9,-10,1],[-10,9,9,-9,3,-10,2,-6,1],[-5,6,9,-5,-1,9,4,-1,1],[2,-4,9,-2,7,-2,-7,-3,-7],[4,3,7,-1,1,4,3,-3,-3],[-10,5,-2,-8,-6,-3,5,4,-7],[10,-10,10,-1,1,10,8,8,9],[-2,10,10,-2,-5,5,-7,-7,-3],[2,10,10,9,9,-3,9,5,-5],[5,2,-6,-9,1,2,3,-10,9],[-2,-1,-6,-7,-2,-4,-9,-6,10],[-7,5,-7,4,2,4,5,10,6],[10,10,-8,-1,-5,8,-9,4,-3],[-2,10,10,-5,-1,10,-8,-3,-4]],[[-5,9,-2,-5,2,-6,2,-3,-1],[-8,9,-9,7,9,8,-10,-8,2],[6,2,9,-4,-5,-3,9,3,1],[6,9,-7,-1,-7,7,-1,-9,10],[1,8,10,-2,-5,6,-7,3,10],[-5,6,-1,3,6,5,9,10,3],[9,9,-10,-9,9,-7,9,-1,-3],[-9,-4,-8,1,-4,3,2,-3,-7],[8,-2,-5,10,-8,-10,-3,9,4],[-4,-5,7,-6,-1,2,1,-3,10],[1,-3,-1,2,-3,-1,8,-3,6],[2,-1,-8,-2,-4,4,-2,-2,-4],[9,-6,8,-9,-3,-1,2,-10,6],[-7,-8,3,5,-5,-2,9,-8,4]],[[-2,-4,5,5,-7,-2,2,-1,-8],[-2,-10,9,9,-3,-3,-3,-2,-2],[-10,-4,-2,2,-4,4,-9,-5,5],[-3,4,-9,3,-3,-9,-1,4,8],[2,9,4,9,2,-4,-8,1,-3],[10,-2,-2,-10,10,8,7,9,-5],[-9,-8,-8,8,-1,9,-9,1,-2],[4,6,3,3,4,-5,-5,-5,7],[-5,-9,-2,-10,9,-4,-6,2,-4],[6,6,7,10,8,-5,9,8,6],[-10,2,-10,8,-7,-6,5,8,3],[-3,-7,10,-3,-2,1,-2,-4,8],[-3,8,7,2,-7,3,6,-6,-8],[7,-7,4,-6,-7,-3,4,3,7]],[[-7,2,-9,-5,5,-2,-10,-4,-5],[-5,5,3,8,3,1,-1,-10,4],[10,-8,3,-7,6,-9,8,-6,-7],[10,-6,5,4,8,9,-7,3,5],[5,8,5,-6,3,-7,-1,-4,-9],[-6,6,-9,4,-5,3,-5,-6,-10],[10,4,-8,-4,8,-5,8,2,-5],[-1,8,8,-10,8,3,6,5,-1],[-1,-3,-2,5,-2,-5,7,6,4],[7,-6,-9,-6,-4,-5,6,-9,-4],[-9,-4,6,-8,7,-10,-7,-4,-5],[-1,8,-4,2,10,10,6,-10,2],[10,-1,-3,8,8,-4,7,-4,5],[-9,-9,-10,-10,8,-7,-8,-10,3]],[[-9,-7,5,2,9,6,-5,2,-5],[-2,-1,6,3,-4,-2,10,10,-8],[9,6,5,1,-10,-3,7,9,-8],[-5,-9,-5,8,2,-3,2,10,9],[1,-7,-4,5,8,7,-8,-6,-1],[-8,6,-6,10,-10,-7,8,-8,-10],[-5,-6,-8,-8,7,-3,-7,-7,1],[-2,3,-1,-9,-8,-4,-3,-3,4],[2,-8,-6,-7,-2,-5,-10,-3,-7],[1,5,-6,8,-10,6,2,5,-7],[1,-5,-10,3,7,3,2,1,5],[-6,7,-4,9,-3,8,-7,-7,9],[3,7,9,4,-6,-9,-4,-4,3],[6,-5,-10,2,-9,10,-6,1,-10]],[[5,-2,-3,-2,7,10,3,6,6],[1,3,-6,-10,-3,8,-3,-1,4],[5,-1,-1,4,6,1,4,-1,-4],[10,-9,-6,8,2,4,1,3,2],[2,7,6,1,2,8,7,9,-9],[-7,-6,-6,6,-10,1,4,-7,-1],[-10,4,-2,-5,8,-9,3,-6,4],[9,-1,-2,10,4,-6,2,-5,8],[-7,-8,-1,4,2,10,1,-9,-8],[-5,-6,8,3,-10,6,-8,2,-10],[5,-6,-3,7,6,8,-5,-2,9],[-5,-10,3,-2,1,-8,-7,-4,-2],[-9,-2,-2,-9,-3,-10,-3,-7,7],[-10,-2,2,-3,-3,-2,-5,1,-8]],[[-10,-2,9,7,8,-6,-5,-5,-9],[-5,8,9,-2,-2,2,7,-6,4],[4,9,5,-6,-4,-7,10,5,-9],[-7,-1,-5,-1,-6,3,4,3,-9],[1,-9,8,9,-8,-5,1,2,-3],[6,9,-10,-3,-2,-10,-5,8,-7],[1,-4,2,-8,3,4,6,1,3],[-10,6,3,4,-8,-3,1,-10,-3],[-6,5,10,7,-3,-3,-10,3,8],[-3,-3,5,5,-9,2,-9,-2,10],[-6,-2,-5,-5,10,2,-3,10,-7],[3,-2,-1,4,-3,-4,2,1,-9],[9,-3,2,-6,-2,5,1,3,10],[-10,-4,3,-7,10,-9,6,2,6]],[[7,-1,10,10,3,7,-7,-8,-1],[1,-5,5,9,-3,-1,5,3,-6],[-3,4,-2,-1,-7,2,-1,-5,-3],[2,10,-10,-4,-8,4,-10,2,5],[5,7,-7,2,-1,6,-7,-5,-4],[7,-2,5,-1,-5,8,-9,7,9],[-4,-10,7,-10,-4,1,-9,-6,-5],[9,9,-9,5,2,-3,-4,1,5],[-1,4,7,3,-6,-9,3,7,3],[9,-3,1,-3,6,-10,5,5,7],[7,-9,1,3,7,6,-5,9,-9],[7,-5,7,3,9,1,1,-7,10],[10,4,3,-9,-6,-6,9,8,-6],[1,6,7,-5,-7,9,-2,1,6]],[[5,-2,-4,-7,-10,6,7,5,-9],[-5,1,7,-1,8,-5,6,2,1],[6,8,1,4,-3,-5,1,7,4],[-1,4,-7,-6,7,10,-1,-7,4],[4,10,-7,10,-5,-8,-2,3,10],[5,2,-3,1,1,-4,-8,1,8],[2,-5,-6,5,-4,3,8,-10,-1],[3,7,-2,6,-1,-7,-6,6,6],[-6,9,-9,6,2,8,-8,-7,-2],[10,-8,-9,-10,4,6,-8,-2,4],[9,1,-5,5,9,-2,1,-10,-3],[-6,4,8,1,-4,-1,6,-8,3],[5,1,-10,-4,-7,9,-1,-2,4],[-5,-4,-6,9,6,9,3,7,-8]],[[8,-7,-6,6,1,4,-8,10,10],[-8,10,-6,-5,-4,4,-1,-4,7],[5,9,1,-3,2,10,9,-1,-4],[-7,6,1,-3,-2,1,9,3,3],[-1,5,-10,-5,3,-8,-3,-5,-8],[6,-9,8,-8,-5,5,6,-4,1],[-6,-3,-2,-7,9,1,8,-9,-6],[6,-6,-6,9,-8,3,-9,6,9],[6,-3,7,2,-5,-4,-8,6,1],[6,6,-5,3,-9,7,-9,3,5],[9,-9,8,5,4,-1,-5,-5,1],[9,3,5,5,2,-7,2,-6,-10],[4,2,1,1,8,-5,5,5,2],[-9,-3,7,-1,7,9,6,5,9]],[[1,1,5,10,-10,9,2,-10,-2],[6,5,-5,-3,6,-8,5,5,9],[-2,2,-2,5,-3,-3,-4,-10,-4],[-3,-5,4,-6,-1,5,-2,8,10],[-5,4,-1,-2,-5,2,-9,-6,-6],[8,-1,2,10,2,8,-8,6,2],[10,-10,8,6,-9,-4,5,6,2],[4,3,-1,-8,5,-2,1,1,-7],[-7,10,7,2,5,-10,9,-2,9],[-3,-2,-3,3,4,-7,-7,-6,-2],[-1,7,-6,7,-10,-8,-10,-8,-9],[-7,-6,8,-4,10,4,-4,-8,-2],[-7,-10,6,8,8,10,-8,10,8],[5,-7,-3,-7,-7,-8,-1,-8,6]],[[10,-3,1,-8,10,10,7,1,2],[-6,-3,-6,-2,7,-10,7,6,-8],[3,5,3,-3,-1,-6,-8,-2,5],[-3,-6,8,-3,6,5,8,2,-3],[-7,7,1,-10,6,-2,-1,8,5],[-5,-1,2,7,-5,-3,3,-7,9],[4,8,5,-8,7,6,-4,-4,4],[-2,-6,-9,7,9,10,1,1,-3],[3,3,-9,-4,1,-7,-4,5,6],[-6,-4,7,7,2,-7,-4,-8,2],[7,-10,6,5,-6,7,-4,5,2],[-6,9,-6,-10,-9,-7,-6,7,-7],[3,2,-2,-9,3,-4,5,-5,7],[3,2,-8,2,-7,9,-3,-4,10]],[[-3,-2,-5,3,-8,8,-10,5,-2],[-2,4,-5,-1,-5,-1,-1,-6,-1],[1,4,-2,5,1,3,2,8,-3],[10,9,-9,10,7,2,6,-1,3],[3,7,-9,-9,-4,-8,2,-10,-1],[3,8,-7,7,-2,-6,-6,-4,-4],[1,-5,-4,3,8,9,2,-3,2],[-1,-3,-9,-9,-9,8,-7,9,-6],[-6,9,4,-5,9,-7,6,-2,-2],[-10,-8,5,2,-4,5,-6,-9,-4],[2,-9,7,-4,5,-4,8,7,2],[-1,5,5,-5,10,-5,-7,6,-10],[4,-8,1,-8,-7,-7,9,1,-3],[-4,9,-6,-2,5,-1,-3,-8,-7]]], dtype = "int64")#candidate|4251|(13, 14, 9)|const|int64
bop_4252 = relay.bitwise_xor(call_4215.astype('int8'), const_4251.astype('int8')) # shape=(13, 14, 9)
bop_4255 = relay.bitwise_xor(call_4216.astype('int8'), const_4251.astype('int8')) # shape=(13, 14, 9)
output = relay.Tuple([uop_4235,bop_4252,])
output2 = relay.Tuple([uop_4237,bop_4255,])
func_4283 = relay.Function([], output)
mod['func_4283'] = func_4283
mod = relay.transform.InferType()(mod)
mutated_mod['func_4283'] = func_4283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4283_call = mutated_mod.get_global_var('func_4283')
call_4284 = func_4283_call()
output = call_4284
func_4285 = relay.Function([], output)
mutated_mod['func_4285'] = func_4285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4377 = relay.var("var_4377", dtype = "float64", shape = (10, 15, 2))#candidate|4377|(10, 15, 2)|var|float64
uop_4378 = relay.log10(var_4377.astype('float64')) # shape=(10, 15, 2)
func_4126_call = mod.get_global_var('func_4126')
func_4128_call = mutated_mod.get_global_var('func_4128')
call_4384 = relay.TupleGetItem(func_4126_call(), 0)
call_4385 = relay.TupleGetItem(func_4128_call(), 0)
output = relay.Tuple([uop_4378,call_4384,])
output2 = relay.Tuple([uop_4378,call_4385,])
func_4397 = relay.Function([var_4377,], output)
mod['func_4397'] = func_4397
mod = relay.transform.InferType()(mod)
mutated_mod['func_4397'] = func_4397
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4398 = relay.var("var_4398", dtype = "float64", shape = (10, 15, 2))#candidate|4398|(10, 15, 2)|var|float64
func_4397_call = mutated_mod.get_global_var('func_4397')
call_4399 = func_4397_call(var_4398)
output = call_4399
func_4400 = relay.Function([var_4398], output)
mutated_mod['func_4400'] = func_4400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3893_call = mod.get_global_var('func_3893')
func_3895_call = mutated_mod.get_global_var('func_3895')
call_4474 = func_3893_call()
call_4475 = func_3893_call()
var_4479 = relay.var("var_4479", dtype = "float64", shape = (6, 1, 9))#candidate|4479|(6, 1, 9)|var|float64
bop_4480 = relay.power(call_4474.astype('float64'), var_4479.astype('float64')) # shape=(6, 1, 9)
bop_4483 = relay.power(call_4475.astype('float64'), var_4479.astype('float64')) # shape=(6, 1, 9)
var_4484 = relay.var("var_4484", dtype = "float64", shape = (14, 15, 9))#candidate|4484|(14, 15, 9)|var|float64
bop_4485 = relay.subtract(call_4474.astype('int8'), var_4484.astype('int8')) # shape=(14, 15, 9)
bop_4488 = relay.subtract(call_4475.astype('int8'), var_4484.astype('int8')) # shape=(14, 15, 9)
var_4515 = relay.var("var_4515", dtype = "int8", shape = (14, 15, 9))#candidate|4515|(14, 15, 9)|var|int8
bop_4516 = relay.equal(bop_4485.astype('bool'), relay.reshape(var_4515.astype('bool'), relay.shape_of(bop_4485))) # shape=(14, 15, 9)
bop_4519 = relay.equal(bop_4488.astype('bool'), relay.reshape(var_4515.astype('bool'), relay.shape_of(bop_4488))) # shape=(14, 15, 9)
bop_4524 = relay.logical_or(bop_4516.astype('bool'), call_4474.astype('bool')) # shape=(14, 15, 9)
bop_4527 = relay.logical_or(bop_4519.astype('bool'), call_4475.astype('bool')) # shape=(14, 15, 9)
output = relay.Tuple([bop_4480,bop_4524,])
output2 = relay.Tuple([bop_4483,bop_4527,])
func_4533 = relay.Function([var_4479,var_4484,var_4515,], output)
mod['func_4533'] = func_4533
mod = relay.transform.InferType()(mod)
var_4534 = relay.var("var_4534", dtype = "float64", shape = (6, 1, 9))#candidate|4534|(6, 1, 9)|var|float64
var_4535 = relay.var("var_4535", dtype = "float64", shape = (14, 15, 9))#candidate|4535|(14, 15, 9)|var|float64
var_4536 = relay.var("var_4536", dtype = "int8", shape = (14, 15, 9))#candidate|4536|(14, 15, 9)|var|int8
output = func_4533(var_4534,var_4535,var_4536,)
func_4537 = relay.Function([var_4534,var_4535,var_4536,], output)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_4574 = relay.TupleGetItem(func_557_call(), 0)
call_4575 = relay.TupleGetItem(func_559_call(), 0)
output = call_4574
output2 = call_4575
func_4604 = relay.Function([], output)
mod['func_4604'] = func_4604
mod = relay.transform.InferType()(mod)
mutated_mod['func_4604'] = func_4604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4604_call = mutated_mod.get_global_var('func_4604')
call_4605 = func_4604_call()
output = call_4605
func_4606 = relay.Function([], output)
mutated_mod['func_4606'] = func_4606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_983_call = mod.get_global_var('func_983')
func_985_call = mutated_mod.get_global_var('func_985')
call_4624 = func_983_call()
call_4625 = func_983_call()
output = relay.Tuple([call_4624,])
output2 = relay.Tuple([call_4625,])
func_4629 = relay.Function([], output)
mod['func_4629'] = func_4629
mod = relay.transform.InferType()(mod)
mutated_mod['func_4629'] = func_4629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4629_call = mutated_mod.get_global_var('func_4629')
call_4630 = func_4629_call()
output = call_4630
func_4631 = relay.Function([], output)
mutated_mod['func_4631'] = func_4631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4283_call = mod.get_global_var('func_4283')
func_4285_call = mutated_mod.get_global_var('func_4285')
call_4632 = relay.TupleGetItem(func_4283_call(), 1)
call_4633 = relay.TupleGetItem(func_4285_call(), 1)
func_4397_call = mod.get_global_var('func_4397')
func_4400_call = mutated_mod.get_global_var('func_4400')
var_4637 = relay.var("var_4637", dtype = "float64", shape = (300,))#candidate|4637|(300,)|var|float64
call_4636 = relay.TupleGetItem(func_4397_call(relay.reshape(var_4637.astype('float64'), [10, 15, 2])), 1)
call_4638 = relay.TupleGetItem(func_4400_call(relay.reshape(var_4637.astype('float64'), [10, 15, 2])), 1)
func_3379_call = mod.get_global_var('func_3379')
func_3381_call = mutated_mod.get_global_var('func_3381')
call_4639 = relay.TupleGetItem(func_3379_call(), 1)
call_4640 = relay.TupleGetItem(func_3381_call(), 1)
func_1415_call = mod.get_global_var('func_1415')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_4669 = relay.TupleGetItem(func_1415_call(), 2)
call_4670 = relay.TupleGetItem(func_1417_call(), 2)
output = relay.Tuple([call_4632,call_4636,var_4637,call_4639,call_4669,])
output2 = relay.Tuple([call_4633,call_4638,var_4637,call_4640,call_4670,])
func_4675 = relay.Function([var_4637,], output)
mod['func_4675'] = func_4675
mod = relay.transform.InferType()(mod)
mutated_mod['func_4675'] = func_4675
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4676 = relay.var("var_4676", dtype = "float64", shape = (300,))#candidate|4676|(300,)|var|float64
func_4675_call = mutated_mod.get_global_var('func_4675')
call_4677 = func_4675_call(var_4676)
output = call_4677
func_4678 = relay.Function([var_4676], output)
mutated_mod['func_4678'] = func_4678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4748 = relay.var("var_4748", dtype = "uint64", shape = ())#candidate|4748|()|var|uint64
var_4749 = relay.var("var_4749", dtype = "uint64", shape = (1, 15, 15))#candidate|4749|(1, 15, 15)|var|uint64
bop_4750 = relay.right_shift(var_4748.astype('uint64'), var_4749.astype('uint64')) # shape=(1, 15, 15)
output = bop_4750
output2 = bop_4750
func_4753 = relay.Function([var_4748,var_4749,], output)
mod['func_4753'] = func_4753
mod = relay.transform.InferType()(mod)
var_4754 = relay.var("var_4754", dtype = "uint64", shape = ())#candidate|4754|()|var|uint64
var_4755 = relay.var("var_4755", dtype = "uint64", shape = (1, 15, 15))#candidate|4755|(1, 15, 15)|var|uint64
output = func_4753(var_4754,var_4755,)
func_4756 = relay.Function([var_4754,var_4755,], output)
mutated_mod['func_4756'] = func_4756
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4789 = relay.var("var_4789", dtype = "uint32", shape = (11, 6, 14))#candidate|4789|(11, 6, 14)|var|uint32
var_4790 = relay.var("var_4790", dtype = "uint32", shape = (11, 6, 14))#candidate|4790|(11, 6, 14)|var|uint32
bop_4791 = relay.bitwise_xor(var_4789.astype('uint32'), relay.reshape(var_4790.astype('uint32'), relay.shape_of(var_4789))) # shape=(11, 6, 14)
output = bop_4791
output2 = bop_4791
func_4794 = relay.Function([var_4789,var_4790,], output)
mod['func_4794'] = func_4794
mod = relay.transform.InferType()(mod)
mutated_mod['func_4794'] = func_4794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4794_call = mutated_mod.get_global_var('func_4794')
var_4796 = relay.var("var_4796", dtype = "uint32", shape = (11, 6, 14))#candidate|4796|(11, 6, 14)|var|uint32
var_4797 = relay.var("var_4797", dtype = "uint32", shape = (11, 6, 14))#candidate|4797|(11, 6, 14)|var|uint32
call_4795 = func_4794_call(var_4796,var_4797,)
output = call_4795
func_4798 = relay.Function([var_4796,var_4797,], output)
mutated_mod['func_4798'] = func_4798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2817_call = mod.get_global_var('func_2817')
func_2819_call = mutated_mod.get_global_var('func_2819')
call_4808 = func_2817_call()
call_4809 = func_2817_call()
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_4819 = relay.TupleGetItem(func_1167_call(), 0)
call_4820 = relay.TupleGetItem(func_1169_call(), 0)
func_4794_call = mod.get_global_var('func_4794')
func_4798_call = mutated_mod.get_global_var('func_4798')
const_4831 = relay.const([7,2,-10,4,-9,-3,7,-6,-10,-7,8,-7,6,-1,8,-6,-1,2,-1,9,7,6,-3,10,-7,-8,-7,-2,-4,5,10,6,-2,-3,7,5,-3,-7,-3,2,4,-5,-7,-5,-9,-3,-4,2,-9,2,-6,9,6,-6,5,-9,9,9,10,-9,6,7,2,7,4,-7,-4,2,4,-1,7,5,5,-4,-8,3,8,4,-9,9,-10,-6,3,-6,-7,6,-10,-1,-5,-7,1,-4,2,-7,1,-6,4,-5,1,4,2,-3,-10,-5,-1,-7,4,9,1,7,-4,1,5,5,-9,6,-10,4,-3,-5,5,7,3,-5,2,4,-7,3,5,9,-10,7,-4,-8,-2,-1,4,8,4,2,7,3,3,7,-6,1,-3,-4,9,-4,-6,10,5,-7,-1,-4,-5,2,2,7,8,-4,8,8,3,-10,10,-8,8,-3,-2,-7,3,6,-1,-5,-1,-9,-8,-8,-2,-9,8,5,-1,-5,7,-2,1,6,-1,2,2,10,-10,-3,7,-3,9,3,8,5,-9,-6,4,-4,-4,4,-10,8,-5,2,-2,10,-5,-3,10,10,4,-10,1,1,2,3,-4,-2,3,2,9,9,5,-10,-10,4,8,2,10,5,9,-4,3,3,-7,1,8,-1,2,10,2,5,10,9,1,5,-4,-4,-4,2,3,-7,-5,-6,10,10,1,-1,-5,4,4,9,-8,-6,-1,4,-4,-6,1,-8,9,-2,7,3,4,9,7,-8,10,-7,-4,4,-2,-9,-2,4,4,2,-9,-5,-4,-3,-2,-8,-6,-3,6,8,-10,10,3,3,-10,-1,4,2,-10,-3,-5,-3,7,-3,5,-2,-10,7,4,3,9,-3,-9,2,-1,2,-7,-8,2,9,5,-2,-2,8,-3,2,-4,6,1,5,-5,9,-1,-8,8,-10,-1,-6,5,10,5,-1,-10,-6,-7,4,-7,5,10,3,-5,1,-7,-8,2,-10,4,10,6,-7,-7,6,4,4,-9,3,9,-9,-10,-7,-6,3,-6,-4,-9,9,1,-1,-9,10,9,-3,7,5,8,2,-8,-4,8,-1,8,-2,-5,6,8,-3,9,-7,7,-4,3,9,-10,8,-10,6,8,8,3,-7,-10,-9,-6,3,-8,8,-2,-7,-9,-4,-5,-8,-8,-6,8,9,-6,7,5,-5,7,-8,-10,5,9,8,-8,7,-1,-7,8,9,6,-6,-5,6,6,-5,7,4,7,-2,-8,-3,3,10,-5,5,-6,-4,4,5,4,-4,9,-8,10,3,10,7,-5,-3,7,-4,9,-3,8,2,-9,-4,4,5,4,4,-4,-5,9,9,-6,-8,-1,-9,-1,10,7,8,-7,-7,-1,-3,3,1,-8,1,-3,10,-2,-2,1,-2,-7,-10,-5,5,10,-10,8,9,4,-9,-9,-9,-1,5,-5,10,9,-6,9,-10,-1,-3,4,4,-4,-2,-3,5,4,-6,6,10,-6,-10,10,-3,2,8,10,3,7,8,-8,4,2,2,-5,-5,-1,-5,7,-1,-6,5,1,1,-3,7,-1,-7,2,10,4,-6,10,-7,1,-8,-7,4,-10,7,5,7,7,-8,-3,-6,-4,3,6,-5,-10,-4,5,-6,-5,8,-8,-4,7,4,10,7,4,2,-4,7,-7,10,8,-6,-10,3,-7,3,-8,-4,-6,-4,4,10,-2,-1,-7,10,-10,8,-1,6,-7,4,5,-6,2,1,8,4,-8,9,-10,1,-5,8,10,-6,2,-4,9,-7,-10,4,4,7,7,-7,3,6,7,-6,7,-5,1,7,-9,-8,7,-8,4,-10,9,5,-7,4,5,2,3,3,7,3,-4,-5,-6,1,8,8,-1,1,-6,-10,4,-2,-9,10,-7,-2,-5,2,-9,1,4,-5,4,3,-1,-10,-6,2,9,1,-5,9,-9,-3,-5,6,-4,4,-6,-10,1,2,4,3,5,1,9,10,-10,8,7,-5,-6,-1,-8,-1,-10,-6,-8,8,-7,3,-7,-7,6,-2,-1,6,-8,4,-9,-6,-10,1,-3,1,-8,-7,-7,-3,10,-8,4,2,2,-9,1,-9,-8,-2,1,-3,10,-5,-6,10,8,9,-3,-6,-7,5,10,10,4,1,5,-4,7,2,8,9,3,7,-9,10,-8,3,-6,-6,-6,6,2,-8,9,-2,3,4,1,1,-4,5,5,2,2,-4,6,10,9,-8,-8,-7,2,-7,3,-5,9,3,-10,5,-4,10,10,9,-8,8,-7,-6,-6,-4,-3,10,-8,7,-7,-8,3,10,-8,1,-3,-1,-5,1,-2,-4,3,8,-4,-7,-7,-1,-5,-2,-9,-10,-5,5,7,-3,1,3,-1,3,-6,-8,9,3,-10,8,9,2,-6,4,-4,-2,6,9,6,5,-4,5,4,-9,1,6,3,4,6,5,-4,-3,2,-8,-5,10,-5,3], dtype = "uint32")#candidate|4831|(924,)|const|uint32
call_4830 = func_4794_call(relay.reshape(const_4831.astype('uint32'), [11, 6, 14]), relay.reshape(const_4831.astype('uint32'), [11, 6, 14]), )
call_4832 = func_4794_call(relay.reshape(const_4831.astype('uint32'), [11, 6, 14]), relay.reshape(const_4831.astype('uint32'), [11, 6, 14]), )
bop_4842 = relay.multiply(call_4830.astype('int16'), call_4808.astype('int16')) # shape=(11, 6, 14)
bop_4845 = relay.multiply(call_4832.astype('int16'), call_4809.astype('int16')) # shape=(11, 6, 14)
output = relay.Tuple([call_4819,const_4831,bop_4842,])
output2 = relay.Tuple([call_4820,const_4831,bop_4845,])
func_4849 = relay.Function([], output)
mod['func_4849'] = func_4849
mod = relay.transform.InferType()(mod)
mutated_mod['func_4849'] = func_4849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4849_call = mutated_mod.get_global_var('func_4849')
call_4850 = func_4849_call()
output = call_4850
func_4851 = relay.Function([], output)
mutated_mod['func_4851'] = func_4851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3713_call = mod.get_global_var('func_3713')
func_3714_call = mutated_mod.get_global_var('func_3714')
call_4924 = relay.TupleGetItem(func_3713_call(), 0)
call_4925 = relay.TupleGetItem(func_3714_call(), 0)
output = call_4924
output2 = call_4925
func_4931 = relay.Function([], output)
mod['func_4931'] = func_4931
mod = relay.transform.InferType()(mod)
mutated_mod['func_4931'] = func_4931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4931_call = mutated_mod.get_global_var('func_4931')
call_4932 = func_4931_call()
output = call_4932
func_4933 = relay.Function([], output)
mutated_mod['func_4933'] = func_4933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4283_call = mod.get_global_var('func_4283')
func_4285_call = mutated_mod.get_global_var('func_4285')
call_4949 = relay.TupleGetItem(func_4283_call(), 0)
call_4950 = relay.TupleGetItem(func_4285_call(), 0)
func_1004_call = mod.get_global_var('func_1004')
func_1005_call = mutated_mod.get_global_var('func_1005')
call_4972 = relay.TupleGetItem(func_1004_call(), 1)
call_4973 = relay.TupleGetItem(func_1005_call(), 1)
output = relay.Tuple([call_4949,call_4972,])
output2 = relay.Tuple([call_4950,call_4973,])
func_4974 = relay.Function([], output)
mod['func_4974'] = func_4974
mod = relay.transform.InferType()(mod)
output = func_4974()
func_4975 = relay.Function([], output)
mutated_mod['func_4975'] = func_4975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_5023 = func_1186_call()
call_5024 = func_1186_call()
func_557_call = mod.get_global_var('func_557')
func_559_call = mutated_mod.get_global_var('func_559')
call_5044 = relay.TupleGetItem(func_557_call(), 0)
call_5045 = relay.TupleGetItem(func_559_call(), 0)
output = relay.Tuple([call_5023,call_5044,])
output2 = relay.Tuple([call_5024,call_5045,])
func_5052 = relay.Function([], output)
mod['func_5052'] = func_5052
mod = relay.transform.InferType()(mod)
mutated_mod['func_5052'] = func_5052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5052_call = mutated_mod.get_global_var('func_5052')
call_5053 = func_5052_call()
output = call_5053
func_5054 = relay.Function([], output)
mutated_mod['func_5054'] = func_5054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_5079 = func_1690_call()
call_5080 = func_1690_call()
uop_5108 = relay.atan(call_5079.astype('float64')) # shape=(11, 3, 9)
uop_5110 = relay.atan(call_5080.astype('float64')) # shape=(11, 3, 9)
bop_5122 = relay.right_shift(uop_5108.astype('uint8'), relay.reshape(call_5079.astype('uint8'), relay.shape_of(uop_5108))) # shape=(11, 3, 9)
bop_5125 = relay.right_shift(uop_5110.astype('uint8'), relay.reshape(call_5080.astype('uint8'), relay.shape_of(uop_5110))) # shape=(11, 3, 9)
output = relay.Tuple([bop_5122,])
output2 = relay.Tuple([bop_5125,])
func_5132 = relay.Function([], output)
mod['func_5132'] = func_5132
mod = relay.transform.InferType()(mod)
output = func_5132()
func_5133 = relay.Function([], output)
mutated_mod['func_5133'] = func_5133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_5152 = func_3244_call()
call_5153 = func_3244_call()
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_5156 = func_3244_call()
call_5157 = func_3244_call()
output = relay.Tuple([call_5152,call_5156,])
output2 = relay.Tuple([call_5153,call_5157,])
func_5164 = relay.Function([], output)
mod['func_5164'] = func_5164
mod = relay.transform.InferType()(mod)
output = func_5164()
func_5165 = relay.Function([], output)
mutated_mod['func_5165'] = func_5165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2448_call = mod.get_global_var('func_2448')
func_2450_call = mutated_mod.get_global_var('func_2450')
call_5178 = relay.TupleGetItem(func_2448_call(), 0)
call_5179 = relay.TupleGetItem(func_2450_call(), 0)
func_4604_call = mod.get_global_var('func_4604')
func_4606_call = mutated_mod.get_global_var('func_4606')
call_5187 = func_4604_call()
call_5188 = func_4604_call()
func_2627_call = mod.get_global_var('func_2627')
func_2628_call = mutated_mod.get_global_var('func_2628')
call_5196 = relay.TupleGetItem(func_2627_call(), 0)
call_5197 = relay.TupleGetItem(func_2628_call(), 0)
func_2497_call = mod.get_global_var('func_2497')
func_2499_call = mutated_mod.get_global_var('func_2499')
call_5206 = relay.TupleGetItem(func_2497_call(), 2)
call_5207 = relay.TupleGetItem(func_2499_call(), 2)
uop_5211 = relay.atan(call_5196.astype('float32')) # shape=(13, 2, 7)
uop_5213 = relay.atan(call_5197.astype('float32')) # shape=(13, 2, 7)
func_2780_call = mod.get_global_var('func_2780')
func_2783_call = mutated_mod.get_global_var('func_2783')
call_5216 = relay.TupleGetItem(func_2780_call(relay.reshape(uop_5211.astype('bool'), [1, 13, 14])), 1)
call_5217 = relay.TupleGetItem(func_2783_call(relay.reshape(uop_5211.astype('bool'), [1, 13, 14])), 1)
output = relay.Tuple([call_5178,call_5187,call_5206,uop_5211,call_5216,])
output2 = relay.Tuple([call_5179,call_5188,call_5207,uop_5213,call_5217,])
func_5218 = relay.Function([], output)
mod['func_5218'] = func_5218
mod = relay.transform.InferType()(mod)
output = func_5218()
func_5219 = relay.Function([], output)
mutated_mod['func_5219'] = func_5219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4604_call = mod.get_global_var('func_4604')
func_4606_call = mutated_mod.get_global_var('func_4606')
call_5258 = func_4604_call()
call_5259 = func_4604_call()
output = relay.Tuple([call_5258,])
output2 = relay.Tuple([call_5259,])
func_5260 = relay.Function([], output)
mod['func_5260'] = func_5260
mod = relay.transform.InferType()(mod)
output = func_5260()
func_5261 = relay.Function([], output)
mutated_mod['func_5261'] = func_5261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5281 = relay.var("var_5281", dtype = "float32", shape = (11, 15, 1))#candidate|5281|(11, 15, 1)|var|float32
uop_5282 = relay.atan(var_5281.astype('float32')) # shape=(11, 15, 1)
output = relay.Tuple([uop_5282,])
output2 = relay.Tuple([uop_5282,])
func_5285 = relay.Function([var_5281,], output)
mod['func_5285'] = func_5285
mod = relay.transform.InferType()(mod)
var_5286 = relay.var("var_5286", dtype = "float32", shape = (11, 15, 1))#candidate|5286|(11, 15, 1)|var|float32
output = func_5285(var_5286)
func_5287 = relay.Function([var_5286], output)
mutated_mod['func_5287'] = func_5287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2448_call = mod.get_global_var('func_2448')
func_2450_call = mutated_mod.get_global_var('func_2450')
call_5328 = relay.TupleGetItem(func_2448_call(), 0)
call_5329 = relay.TupleGetItem(func_2450_call(), 0)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_5370 = func_3244_call()
call_5371 = func_3244_call()
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_5373 = func_1690_call()
call_5374 = func_1690_call()
bop_5400 = relay.bitwise_or(call_5373.astype('int16'), call_5370.astype('int16')) # shape=(11, 3, 9)
bop_5403 = relay.bitwise_or(call_5374.astype('int16'), call_5371.astype('int16')) # shape=(11, 3, 9)
func_906_call = mod.get_global_var('func_906')
func_908_call = mutated_mod.get_global_var('func_908')
var_5414 = relay.var("var_5414", dtype = "float32", shape = (45,))#candidate|5414|(45,)|var|float32
call_5413 = relay.TupleGetItem(func_906_call(relay.reshape(var_5414.astype('float32'), [1, 5, 9])), 0)
call_5415 = relay.TupleGetItem(func_908_call(relay.reshape(var_5414.astype('float32'), [1, 5, 9])), 0)
func_3467_call = mod.get_global_var('func_3467')
func_3470_call = mutated_mod.get_global_var('func_3470')
var_5417 = relay.var("var_5417", dtype = "float64", shape = (720,))#candidate|5417|(720,)|var|float64
call_5416 = relay.TupleGetItem(func_3467_call(relay.reshape(var_5417.astype('float64'), [8, 10, 9])), 0)
call_5418 = relay.TupleGetItem(func_3470_call(relay.reshape(var_5417.astype('float64'), [8, 10, 9])), 0)
output = relay.Tuple([call_5328,bop_5400,call_5413,var_5414,call_5416,var_5417,])
output2 = relay.Tuple([call_5329,bop_5403,call_5415,var_5414,call_5418,var_5417,])
func_5429 = relay.Function([var_5414,var_5417,], output)
mod['func_5429'] = func_5429
mod = relay.transform.InferType()(mod)
mutated_mod['func_5429'] = func_5429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5429_call = mutated_mod.get_global_var('func_5429')
var_5431 = relay.var("var_5431", dtype = "float32", shape = (45,))#candidate|5431|(45,)|var|float32
var_5432 = relay.var("var_5432", dtype = "float64", shape = (720,))#candidate|5432|(720,)|var|float64
call_5430 = func_5429_call(var_5431,var_5432,)
output = call_5430
func_5433 = relay.Function([var_5431,var_5432,], output)
mutated_mod['func_5433'] = func_5433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_5473 = relay.TupleGetItem(func_1167_call(), 0)
call_5474 = relay.TupleGetItem(func_1169_call(), 0)
output = call_5473
output2 = call_5474
func_5498 = relay.Function([], output)
mod['func_5498'] = func_5498
mod = relay.transform.InferType()(mod)
output = func_5498()
func_5499 = relay.Function([], output)
mutated_mod['func_5499'] = func_5499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_574_call = mod.get_global_var('func_574')
func_575_call = mutated_mod.get_global_var('func_575')
call_5534 = relay.TupleGetItem(func_574_call(), 2)
call_5535 = relay.TupleGetItem(func_575_call(), 2)
output = call_5534
output2 = call_5535
func_5538 = relay.Function([], output)
mod['func_5538'] = func_5538
mod = relay.transform.InferType()(mod)
mutated_mod['func_5538'] = func_5538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5538_call = mutated_mod.get_global_var('func_5538')
call_5539 = func_5538_call()
output = call_5539
func_5540 = relay.Function([], output)
mutated_mod['func_5540'] = func_5540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1846_call = mod.get_global_var('func_1846')
func_1847_call = mutated_mod.get_global_var('func_1847')
call_5581 = relay.TupleGetItem(func_1846_call(), 0)
call_5582 = relay.TupleGetItem(func_1847_call(), 0)
output = relay.Tuple([call_5581,])
output2 = relay.Tuple([call_5582,])
func_5590 = relay.Function([], output)
mod['func_5590'] = func_5590
mod = relay.transform.InferType()(mod)
output = func_5590()
func_5591 = relay.Function([], output)
mutated_mod['func_5591'] = func_5591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1846_call = mod.get_global_var('func_1846')
func_1847_call = mutated_mod.get_global_var('func_1847')
call_5604 = relay.TupleGetItem(func_1846_call(), 0)
call_5605 = relay.TupleGetItem(func_1847_call(), 0)
func_1133_call = mod.get_global_var('func_1133')
func_1136_call = mutated_mod.get_global_var('func_1136')
const_5611 = relay.const([-1.599001,6.507541,5.060034,-7.132221,2.532029,-0.971736,5.904429,-1.655192,-9.582732,-8.349712,-7.877355,4.571249,-8.949108,1.551614,1.310704,3.549491,-0.062703,5.313794,3.584138,6.544693,-3.241605,4.833277,-0.676131,-6.514133,-2.976577,-9.639871,5.427391,9.054967,-1.899962,8.031524,-0.146955,8.012246,1.334256,2.490280,5.639254,8.601379,-4.636025,0.635470,-2.056700,8.143628,-5.188857,5.046509,-3.562175,-8.420035,-8.263507], dtype = "float32")#candidate|5611|(45,)|const|float32
call_5610 = relay.TupleGetItem(func_1133_call(relay.reshape(const_5611.astype('float32'), [1, 45])), 2)
call_5612 = relay.TupleGetItem(func_1136_call(relay.reshape(const_5611.astype('float32'), [1, 45])), 2)
var_5633 = relay.var("var_5633", dtype = "float32", shape = (45,))#candidate|5633|(45,)|var|float32
bop_5634 = relay.left_shift(const_5611.astype('uint64'), relay.reshape(var_5633.astype('uint64'), relay.shape_of(const_5611))) # shape=(45,)
output = relay.Tuple([call_5604,call_5610,bop_5634,])
output2 = relay.Tuple([call_5605,call_5612,bop_5634,])
func_5641 = relay.Function([var_5633,], output)
mod['func_5641'] = func_5641
mod = relay.transform.InferType()(mod)
var_5642 = relay.var("var_5642", dtype = "float32", shape = (45,))#candidate|5642|(45,)|var|float32
output = func_5641(var_5642)
func_5643 = relay.Function([var_5642], output)
mutated_mod['func_5643'] = func_5643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5708 = relay.var("var_5708", dtype = "uint16", shape = (14, 14, 12))#candidate|5708|(14, 14, 12)|var|uint16
var_5709 = relay.var("var_5709", dtype = "uint16", shape = (14, 14, 12))#candidate|5709|(14, 14, 12)|var|uint16
bop_5710 = relay.left_shift(var_5708.astype('uint16'), relay.reshape(var_5709.astype('uint16'), relay.shape_of(var_5708))) # shape=(14, 14, 12)
output = relay.Tuple([bop_5710,])
output2 = relay.Tuple([bop_5710,])
func_5717 = relay.Function([var_5708,var_5709,], output)
mod['func_5717'] = func_5717
mod = relay.transform.InferType()(mod)
var_5718 = relay.var("var_5718", dtype = "uint16", shape = (14, 14, 12))#candidate|5718|(14, 14, 12)|var|uint16
var_5719 = relay.var("var_5719", dtype = "uint16", shape = (14, 14, 12))#candidate|5719|(14, 14, 12)|var|uint16
output = func_5717(var_5718,var_5719,)
func_5720 = relay.Function([var_5718,var_5719,], output)
mutated_mod['func_5720'] = func_5720
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5747 = relay.var("var_5747", dtype = "float64", shape = (11, 5, 9))#candidate|5747|(11, 5, 9)|var|float64
uop_5748 = relay.cosh(var_5747.astype('float64')) # shape=(11, 5, 9)
output = relay.Tuple([uop_5748,])
output2 = relay.Tuple([uop_5748,])
func_5750 = relay.Function([var_5747,], output)
mod['func_5750'] = func_5750
mod = relay.transform.InferType()(mod)
var_5751 = relay.var("var_5751", dtype = "float64", shape = (11, 5, 9))#candidate|5751|(11, 5, 9)|var|float64
output = func_5750(var_5751)
func_5752 = relay.Function([var_5751], output)
mutated_mod['func_5752'] = func_5752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5538_call = mod.get_global_var('func_5538')
func_5540_call = mutated_mod.get_global_var('func_5540')
call_5791 = func_5538_call()
call_5792 = func_5538_call()
output = call_5791
output2 = call_5792
func_5798 = relay.Function([], output)
mod['func_5798'] = func_5798
mod = relay.transform.InferType()(mod)
mutated_mod['func_5798'] = func_5798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5798_call = mutated_mod.get_global_var('func_5798')
call_5799 = func_5798_call()
output = call_5799
func_5800 = relay.Function([], output)
mutated_mod['func_5800'] = func_5800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_912_call = mod.get_global_var('func_912')
func_913_call = mutated_mod.get_global_var('func_913')
call_5801 = func_912_call()
call_5802 = func_912_call()
func_2332_call = mod.get_global_var('func_2332')
func_2333_call = mutated_mod.get_global_var('func_2333')
call_5803 = relay.TupleGetItem(func_2332_call(), 0)
call_5804 = relay.TupleGetItem(func_2333_call(), 0)
output = relay.Tuple([call_5801,call_5803,])
output2 = relay.Tuple([call_5802,call_5804,])
func_5806 = relay.Function([], output)
mod['func_5806'] = func_5806
mod = relay.transform.InferType()(mod)
output = func_5806()
func_5807 = relay.Function([], output)
mutated_mod['func_5807'] = func_5807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2627_call = mod.get_global_var('func_2627')
func_2628_call = mutated_mod.get_global_var('func_2628')
call_5829 = relay.TupleGetItem(func_2627_call(), 0)
call_5830 = relay.TupleGetItem(func_2628_call(), 0)
func_5750_call = mod.get_global_var('func_5750')
func_5752_call = mutated_mod.get_global_var('func_5752')
const_5836 = relay.const([-0.423056,-4.562520,-6.763484,5.793665,-9.324744,7.712629,8.195534,5.887834,4.578750,0.571497,6.778854,-7.770996,6.100684,-9.434175,6.327762,2.395846,2.657260,4.706140,-9.374994,-2.162678,-8.438027,1.211606,9.974401,1.660600,2.875326,-3.825373,7.220196,6.468541,-2.324131,9.742833,7.630869,3.600476,0.139306,-5.964969,-0.206932,-6.821022,-0.654134,-7.959146,-9.906820,-1.668357,-4.922947,3.032957,-8.283280,-4.837394,-6.443671,-5.050880,4.967866,-8.258933,-4.603853,-5.365840,-3.923839,-5.396852,-8.849982,-4.130004,-8.769180,-6.460769,-2.840272,-9.340173,-9.145761,3.081033,-8.193975,-2.204136,0.635438,-3.795942,2.922866,-6.008345,2.562280,9.750594,4.935348,0.574871,-8.622176,-2.797055,3.279611,3.726683,-6.251584,-8.440824,-9.485337,-9.887154,-0.615099,-7.485330,8.888696,6.866584,0.370223,-5.155547,-2.324754,-3.824775,6.601739,0.870937,9.015114,8.077016,3.873339,-1.226803,-6.691011,-8.894127,-1.257885,0.148418,4.061570,-2.676759,9.905051,-8.098573,-3.049406,-3.601965,0.981450,-0.881633,4.588449,-9.277022,-0.913264,-1.155866,3.349752,1.111142,6.016400,9.570014,0.376993,3.989003,-2.584638,-6.833318,-1.061911,7.603085,1.398473,-8.623515,4.379829,2.425731,-3.382068,-0.310249,-5.318286,3.926811,-2.934837,4.878143,-0.847249,-8.537931,-4.286744,-7.918647,-3.526667,-2.673671,7.567622,-4.457265,-2.047321,-4.004070,8.653127,-6.640419,-9.656650,-3.158978,4.307783,-0.811077,-1.763070,-0.908388,-7.735234,-5.024390,-0.720392,-7.991954,7.084216,-3.727043,-5.451428,-3.978055,-4.554880,-5.057083,-6.107741,8.155042,-3.042532,-8.447861,2.564980,5.629266,2.462115,-2.574318,-9.849502,7.566705,7.105494,2.414516,7.800382,5.806982,2.004588,-6.748216,-6.349700,9.029707,-7.239239,-7.162835,-8.118229,8.326186,7.793012,-3.084020,-2.608962,4.204375,1.405559,5.887314,3.319955,-9.992879,-0.033361,-1.462174,0.240394,9.813837,4.292883,9.894446,0.122494,3.525952,-4.379373,9.387066,-6.931269,-7.336698,1.732636,-3.148577,-7.674197,5.460436,2.749872,-8.971919,4.520804,-7.325302,7.937608,7.493731,-1.490722,6.061127,-1.590466,2.567428,5.856121,-9.744373,-7.617049,1.749290,-4.336873,4.458432,4.961264,-2.711900,-6.568519,0.606152,-1.302582,-4.422874,-9.887646,8.341606,-3.348805,5.888970,-3.175161,2.724952,-2.447314,5.125398,2.291017,-3.863169,-8.836899,-8.257899,-4.752080,-3.759536,-7.899501,6.675798,-0.235614,2.954294,-7.118862,7.814446,-6.831346,8.574699,0.127325,5.185230,8.123312,0.163529,-2.461749,-3.807626,-5.521022,7.198134,-5.189244,5.959720,4.142196,8.097646,9.789559,-8.486902,8.617706,-3.511819,8.772848,-8.144249,2.955245,-6.098154,5.596298,-1.161105,-1.362298,-1.810724,7.974069,2.461657,-3.813134,-5.637749,6.365150,7.553846,-0.381890,-2.229559,-2.365666,-9.752816,-7.370361,2.100046,-9.536351,7.001120,-9.231443,1.581499,2.873616,-2.181625,1.071443,8.746918,-3.069891,-3.700707,-9.307119,-5.188937,0.034660,8.892629,1.622590,2.173257,-1.081517,-4.542954,-6.299873,-6.757678,4.972429,9.596558,9.980623,9.796529,6.827610,-2.980420,-8.921101,-7.313596,-9.365001,-8.317939,1.623254,8.234132,-9.673585,-7.375241,9.966757,7.614399,4.624908,4.143405,6.307911,-0.952167,-6.997132,8.543045,1.889639,-3.005295,8.408844,-2.626535,-7.284319,-3.366439,2.618166,4.814162,-7.912906,3.473888,3.232015,-9.744695,-0.797017,-6.359535,-3.249801,7.028245,2.181747,0.876876,-4.455286,5.980322,9.584972,-5.495244,-1.149854,7.811047,-4.393231,5.246084,9.442223,-7.963276,-1.004902,3.487647,-3.189761,1.268969,-6.489532,-6.422443,-5.719284,-2.926007,-3.013462,-9.463337,-7.188628,3.690212,5.489856,2.106853,-0.365887,-4.706669,-8.914853,5.225960,-8.708524,-4.207910,3.465579,-3.691052,4.937815,8.619302,5.377136,-8.235407,4.761846,-5.033182,-7.125305,-7.139688,1.849740,-3.376304,-5.124757,6.703243,-7.628926,2.230162,-9.702935,5.065761,-2.025090,4.483946,-4.796112,-9.291559,8.652643,-6.758502,-9.836904,3.872293,1.731555,0.460820,5.086885,4.181691,-6.743424,-0.830399,-8.679571,-8.020999,-7.440334,-3.613834,-2.805307,8.319086,6.422400,0.146543,-6.990398,7.133019,-2.254828,9.038446,8.599551,1.326131,5.094776,8.925108,8.551761,2.996442,2.035683,7.663564,-0.797348,-8.560904,-8.478118,5.808992,-3.396496,0.096742,6.702193,-6.401290,2.115669,-1.034574,4.122666,-7.401217,-2.512304,7.519479,1.825267,5.324571,1.522016,5.780734,8.237474,-9.051098,4.232584,1.685704,-2.068481,-0.016123,2.476661,-1.178212,-0.378545,-4.290577,-7.023182,-3.131602,-1.970301,3.168148,0.253781,6.473124,7.490493,-8.336438,3.122005,1.524166,-9.367070,1.998900,4.224634,-3.821467,-7.344696,-0.661893,-9.057401,-1.517332,-0.529885,-9.956017,-8.730295,-2.825858,6.328901,5.798159,-9.113741,-7.177288,-3.790827,6.204994,-1.781849,3.435297,-9.515654,2.748976,-4.687053,4.875896,-4.633738,3.985247,8.179575,-8.656176,-1.404566,-4.602146,8.452249,3.580840,-7.974339], dtype = "float64")#candidate|5836|(495,)|const|float64
call_5835 = relay.TupleGetItem(func_5750_call(relay.reshape(const_5836.astype('float64'), [11, 5, 9])), 0)
call_5837 = relay.TupleGetItem(func_5752_call(relay.reshape(const_5836.astype('float64'), [11, 5, 9])), 0)
output = relay.Tuple([call_5829,call_5835,const_5836,])
output2 = relay.Tuple([call_5830,call_5837,const_5836,])
func_5842 = relay.Function([], output)
mod['func_5842'] = func_5842
mod = relay.transform.InferType()(mod)
output = func_5842()
func_5843 = relay.Function([], output)
mutated_mod['func_5843'] = func_5843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4604_call = mod.get_global_var('func_4604')
func_4606_call = mutated_mod.get_global_var('func_4606')
call_5889 = func_4604_call()
call_5890 = func_4604_call()
func_2180_call = mod.get_global_var('func_2180')
func_2183_call = mutated_mod.get_global_var('func_2183')
var_5898 = relay.var("var_5898", dtype = "float32", shape = (630, 2))#candidate|5898|(630, 2)|var|float32
call_5897 = relay.TupleGetItem(func_2180_call(relay.reshape(var_5898.astype('float32'), [10, 14, 9])), 0)
call_5899 = relay.TupleGetItem(func_2183_call(relay.reshape(var_5898.astype('float32'), [10, 14, 9])), 0)
var_5923 = relay.var("var_5923", dtype = "float32", shape = (630, 2))#candidate|5923|(630, 2)|var|float32
bop_5924 = relay.logical_xor(var_5898.astype('int32'), relay.reshape(var_5923.astype('int32'), relay.shape_of(var_5898))) # shape=(630, 2)
uop_5932 = relay.acos(var_5898.astype('float64')) # shape=(630, 2)
func_5260_call = mod.get_global_var('func_5260')
func_5261_call = mutated_mod.get_global_var('func_5261')
call_5935 = relay.TupleGetItem(func_5260_call(), 0)
call_5936 = relay.TupleGetItem(func_5261_call(), 0)
output = relay.Tuple([call_5889,call_5897,bop_5924,uop_5932,call_5935,])
output2 = relay.Tuple([call_5890,call_5899,bop_5924,uop_5932,call_5936,])
func_5941 = relay.Function([var_5898,var_5923,], output)
mod['func_5941'] = func_5941
mod = relay.transform.InferType()(mod)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5941_call = mutated_mod.get_global_var('func_5941')
var_5943 = relay.var("var_5943", dtype = "float32", shape = (630, 2))#candidate|5943|(630, 2)|var|float32
var_5944 = relay.var("var_5944", dtype = "float32", shape = (630, 2))#candidate|5944|(630, 2)|var|float32
call_5942 = func_5941_call(var_5943,var_5944,)
output = call_5942
func_5945 = relay.Function([var_5943,var_5944,], output)
mutated_mod['func_5945'] = func_5945
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5947 = relay.var("var_5947", dtype = "int64", shape = ())#candidate|5947|()|var|int64
const_5948 = relay.const([[[5,4,-4],[-3,8,-10],[-9,-9,-5],[-5,9,8],[2,10,-4],[9,-4,5],[8,4,-3],[8,7,9]],[[2,-1,-8],[1,-6,-3],[6,2,-7],[-10,4,10],[-6,7,6],[5,10,8],[-4,-7,2],[3,-3,7]]], dtype = "int64")#candidate|5948|(2, 8, 3)|const|int64
bop_5949 = relay.equal(var_5947.astype('bool'), const_5948.astype('bool')) # shape=(2, 8, 3)
func_2497_call = mod.get_global_var('func_2497')
func_2499_call = mutated_mod.get_global_var('func_2499')
call_5956 = relay.TupleGetItem(func_2497_call(), 0)
call_5957 = relay.TupleGetItem(func_2499_call(), 0)
func_1700_call = mod.get_global_var('func_1700')
func_1701_call = mutated_mod.get_global_var('func_1701')
call_5960 = func_1700_call()
call_5961 = func_1700_call()
output = relay.Tuple([bop_5949,call_5956,call_5960,])
output2 = relay.Tuple([bop_5949,call_5957,call_5961,])
func_5976 = relay.Function([var_5947,], output)
mod['func_5976'] = func_5976
mod = relay.transform.InferType()(mod)
var_5977 = relay.var("var_5977", dtype = "int64", shape = ())#candidate|5977|()|var|int64
output = func_5976(var_5977)
func_5978 = relay.Function([var_5977], output)
mutated_mod['func_5978'] = func_5978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2474_call = mod.get_global_var('func_2474')
func_2476_call = mutated_mod.get_global_var('func_2476')
call_6010 = relay.TupleGetItem(func_2474_call(), 0)
call_6011 = relay.TupleGetItem(func_2476_call(), 0)
output = call_6010
output2 = call_6011
func_6041 = relay.Function([], output)
mod['func_6041'] = func_6041
mod = relay.transform.InferType()(mod)
output = func_6041()
func_6042 = relay.Function([], output)
mutated_mod['func_6042'] = func_6042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1415_call = mod.get_global_var('func_1415')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_6122 = relay.TupleGetItem(func_1415_call(), 1)
call_6123 = relay.TupleGetItem(func_1417_call(), 1)
output = call_6122
output2 = call_6123
func_6144 = relay.Function([], output)
mod['func_6144'] = func_6144
mod = relay.transform.InferType()(mod)
mutated_mod['func_6144'] = func_6144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6144_call = mutated_mod.get_global_var('func_6144')
call_6145 = func_6144_call()
output = call_6145
func_6146 = relay.Function([], output)
mutated_mod['func_6146'] = func_6146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_802_call = mod.get_global_var('func_802')
func_803_call = mutated_mod.get_global_var('func_803')
call_6207 = relay.TupleGetItem(func_802_call(), 0)
call_6208 = relay.TupleGetItem(func_803_call(), 0)
func_6144_call = mod.get_global_var('func_6144')
func_6146_call = mutated_mod.get_global_var('func_6146')
call_6231 = func_6144_call()
call_6232 = func_6144_call()
output = relay.Tuple([call_6207,call_6231,])
output2 = relay.Tuple([call_6208,call_6232,])
func_6237 = relay.Function([], output)
mod['func_6237'] = func_6237
mod = relay.transform.InferType()(mod)
mutated_mod['func_6237'] = func_6237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6237_call = mutated_mod.get_global_var('func_6237')
call_6238 = func_6237_call()
output = call_6238
func_6239 = relay.Function([], output)
mutated_mod['func_6239'] = func_6239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_6242 = func_1690_call()
call_6243 = func_1690_call()
func_20_call = mod.get_global_var('func_20')
func_22_call = mutated_mod.get_global_var('func_22')
var_6256 = relay.var("var_6256", dtype = "float64", shape = (1, 9))#candidate|6256|(1, 9)|var|float64
call_6255 = relay.TupleGetItem(func_20_call(relay.reshape(var_6256.astype('float64'), [1, 1, 9])), 0)
call_6257 = relay.TupleGetItem(func_22_call(relay.reshape(var_6256.astype('float64'), [1, 1, 9])), 0)
bop_6267 = relay.bitwise_xor(call_6255.astype('int8'), call_6242.astype('int8')) # shape=(11, 3, 9)
bop_6270 = relay.bitwise_xor(call_6257.astype('int8'), call_6243.astype('int8')) # shape=(11, 3, 9)
func_477_call = mod.get_global_var('func_477')
func_480_call = mutated_mod.get_global_var('func_480')
const_6302 = relay.const(False, dtype = "bool")#candidate|6302|()|const|bool
const_6303 = relay.const([True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False], dtype = "bool")#candidate|6303|(286,)|const|bool
call_6301 = relay.TupleGetItem(func_477_call(relay.reshape(const_6302.astype('bool'), []), relay.reshape(const_6303.astype('bool'), [2, 13, 11]), ), 0)
call_6304 = relay.TupleGetItem(func_480_call(relay.reshape(const_6302.astype('bool'), []), relay.reshape(const_6303.astype('bool'), [2, 13, 11]), ), 0)
bop_6309 = relay.logical_and(call_6242.astype('bool'), relay.reshape(bop_6267.astype('bool'), relay.shape_of(call_6242))) # shape=(11, 3, 9)
bop_6312 = relay.logical_and(call_6243.astype('bool'), relay.reshape(bop_6270.astype('bool'), relay.shape_of(call_6243))) # shape=(11, 3, 9)
output = relay.Tuple([var_6256,call_6301,const_6302,const_6303,bop_6309,])
output2 = relay.Tuple([var_6256,call_6304,const_6302,const_6303,bop_6312,])
func_6313 = relay.Function([var_6256,], output)
mod['func_6313'] = func_6313
mod = relay.transform.InferType()(mod)
var_6314 = relay.var("var_6314", dtype = "float64", shape = (1, 9))#candidate|6314|(1, 9)|var|float64
output = func_6313(var_6314)
func_6315 = relay.Function([var_6314], output)
mutated_mod['func_6315'] = func_6315
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6341 = relay.var("var_6341", dtype = "float32", shape = (10, 14, 8))#candidate|6341|(10, 14, 8)|var|float32
uop_6342 = relay.sin(var_6341.astype('float32')) # shape=(10, 14, 8)
const_6346 = relay.const([[[3.258529,4.688772,3.841519,-4.894884,-6.043751,6.386338,0.880092,4.281646],[0.245941,4.724644,-2.882267,1.706569,-1.676238,-2.881919,6.559192,-7.827332],[0.974168,-8.635454,0.418385,-2.454503,-3.881261,-3.261849,-4.128352,-2.221302],[5.635909,8.329402,-3.546643,-9.325241,-7.265639,5.609113,4.171659,-2.732485],[-5.732309,2.189213,-1.553702,6.155865,4.206842,-5.773400,9.141943,-0.535733],[6.320685,5.072451,-0.368368,-8.622555,-7.985575,-0.456669,8.832356,-7.612789],[-4.868789,1.389459,-5.384180,9.883764,0.461026,6.352918,-8.353217,4.996261],[8.427644,-1.222449,2.483659,-4.284481,-3.502734,3.431132,-4.188189,6.842200],[7.559651,4.234296,4.039365,2.003371,-1.642328,-1.055861,-8.964176,-4.383958],[-3.473187,-5.588841,-2.117133,1.035369,2.245436,-8.666194,3.635545,-7.554779],[6.656518,-1.885051,3.599350,3.787231,-7.751269,-1.272907,6.432066,-4.559040],[2.753869,3.986518,-4.725549,3.217151,8.440558,2.134157,9.198453,0.160415],[0.235818,-4.716682,-5.308859,-4.580378,4.321972,0.776421,-0.393629,-6.809329],[-9.331426,8.353487,-2.538922,2.224217,-1.666146,-4.851315,-6.741940,-6.563955]],[[3.186825,-7.182914,-7.681212,-6.663908,-1.233715,8.946362,-4.566534,-3.185989],[3.652704,1.302231,-7.259235,-2.836982,2.219137,6.700970,-1.693587,0.118935],[-2.066424,7.354079,-7.812731,-0.676590,-6.885033,7.659140,6.834568,2.415260],[5.488625,-0.216441,4.020125,7.185613,-4.115059,3.708359,-3.733271,-2.065354],[-1.742744,-6.956025,-7.585985,8.194044,-5.604589,7.139362,2.943419,-0.134562],[7.580984,-2.671487,5.657271,6.885618,-6.823220,5.798786,4.281571,7.058369],[2.793181,-7.891913,-3.525232,-0.010275,8.868735,-9.294784,9.892790,9.062758],[-6.429921,9.856644,9.712567,1.277983,8.673623,9.431512,-6.137268,4.109005],[-9.605287,4.368688,5.385101,0.604258,0.239624,7.069024,-4.368154,4.405891],[5.290426,6.657356,6.814918,-7.507618,3.945145,3.171892,6.484095,7.192668],[8.172219,-2.180769,6.367103,1.742901,-3.033731,3.966610,2.419458,0.548211],[5.803658,-4.791154,9.748860,-2.772089,-6.247629,-1.151606,-6.468210,1.535926],[8.491719,-7.430455,8.588527,9.239090,9.697310,-7.529824,-1.217025,6.259100],[-1.745072,-0.372367,-0.417013,-0.587356,6.860613,-8.480246,7.112828,4.645293]],[[-7.193670,3.628383,4.258130,7.095917,9.748625,6.685578,8.042380,0.372748],[-9.717138,7.252871,-7.679064,8.790495,-2.483236,1.894011,9.934683,-9.911328],[9.922414,8.725297,6.669806,6.306898,2.483322,-9.853554,9.997080,-6.564953],[0.991369,-6.912884,-5.698930,2.257972,-6.458752,-8.575381,3.001726,8.851656],[-4.868073,8.417958,3.500832,-4.930465,-0.499453,2.552814,-5.602389,6.131651],[4.715382,-3.861047,-6.581068,-7.329772,-7.715003,-9.452052,-9.302635,-5.746313],[0.821615,-3.339400,-2.787024,1.691148,9.450299,-4.469762,-4.777973,7.130552],[-5.413935,6.110434,-9.135094,0.881458,-5.995157,-0.895990,7.671510,7.543886],[1.985533,4.394074,-3.483018,-7.605778,7.258568,-6.679696,-6.654098,3.269646],[7.416889,0.114513,-7.099685,-7.321398,9.857389,4.359617,-3.940970,6.103750],[-5.377670,2.024479,3.238754,-8.395473,2.351975,-1.770272,5.379459,-9.480436],[2.495459,-7.614771,-9.232696,-3.188266,0.540040,-1.921547,6.584064,4.642625],[-0.556530,-7.449406,-2.513434,-5.091706,9.903331,-4.632972,-6.507833,6.119218],[-3.884907,7.808896,7.025015,-9.539961,-7.227178,-9.138331,-6.240116,6.087183]],[[-0.846364,-7.587757,5.724888,-6.383399,-5.685774,5.857432,4.683684,-0.607061],[-0.478516,-7.632869,7.741119,-5.297514,0.904041,0.205067,0.883562,-0.410895],[9.105745,-7.395185,6.773413,7.345217,6.582961,-3.032563,-8.812548,4.544651],[3.310158,-9.763427,-8.554429,-8.586084,2.261839,-5.181793,-1.716978,-5.966955],[9.373494,-1.478283,-0.037969,-0.732980,-2.155115,-9.309556,3.732416,4.441755],[-4.669369,-7.462693,1.045279,-9.233688,-1.467723,3.399441,-8.512219,-7.384183],[-9.492038,-2.491139,7.462430,7.800907,-9.459303,-6.440638,2.568585,-8.707677],[7.886528,-6.074415,0.849843,9.688089,4.034167,-3.165382,-8.932001,-1.859651],[-6.529986,1.331366,2.704324,0.877242,2.659823,-1.459267,-9.808832,-4.240050],[7.144718,-1.662786,9.541224,-3.571266,-0.708910,-3.618294,-4.080073,8.874121],[-1.589608,-0.684049,5.064244,7.272061,4.701286,9.076618,-6.022723,9.288382],[0.363970,-8.174595,0.823120,2.625544,9.648950,-8.551026,-6.653625,-5.257960],[3.795699,0.071089,1.722337,9.216312,-9.998227,-6.033746,-4.691246,-5.117169],[8.717246,-3.789846,8.191918,-0.645623,-7.027979,-1.652819,-8.660101,6.032427]],[[0.310245,5.586936,8.055632,9.370191,1.414125,-2.756326,8.838944,7.595152],[3.416262,9.642919,-5.690339,1.870967,0.472101,2.944515,4.237323,8.092084],[7.866125,0.690227,5.818280,-5.019918,-4.214740,-2.655282,7.777444,-5.074547],[9.358712,-5.293138,5.746177,-9.119072,4.125497,-6.726826,-5.455944,-5.972163],[-6.450611,-9.639206,-6.913078,7.408392,8.231683,5.327290,4.916191,2.979049],[2.830388,-8.529559,-3.325159,6.551951,1.630220,-4.896500,0.076605,6.190408],[-6.243188,8.306541,8.249730,0.982869,-6.216342,1.936509,-0.754185,5.541167],[-0.167702,-2.484419,-7.193588,6.466783,1.508760,-5.498268,-7.068774,7.999991],[3.888128,1.258915,5.548311,-2.006745,4.041449,4.632374,-8.575253,-9.253775],[8.266196,9.605353,-5.678328,0.714386,-3.616821,1.571014,0.915898,1.261952],[1.596362,1.101081,8.398587,0.144536,-0.296955,-8.878455,6.036364,2.811510],[4.002203,-8.075665,4.899965,-0.524293,3.648837,-3.786389,-9.847597,-6.996186],[4.539736,-9.491749,3.644707,5.493100,-0.188618,-3.811055,-8.461410,-3.870559],[3.108528,-5.217557,-6.978626,-8.586372,-3.024134,1.369058,3.442463,-9.993695]],[[3.756791,2.562123,-0.244646,-2.207330,1.075669,-4.567473,9.670368,7.138016],[-1.004729,1.849843,-9.535533,-0.159497,4.228919,0.177631,1.563961,2.058111],[-2.379813,2.134490,5.299234,-5.652390,1.490055,1.141911,9.844715,6.331219],[-1.403131,5.891239,-2.392788,5.896969,6.986974,-1.030370,-9.790588,4.998465],[9.796930,-4.265545,3.624037,3.233579,7.152113,7.677320,2.197183,-9.288889],[0.575743,7.613939,-0.231500,5.382101,4.588850,-5.971772,6.060940,6.082740],[8.950026,-7.394626,-5.470149,8.463141,-1.209661,-7.626440,2.444327,1.502303],[-8.361692,-8.878855,5.112060,-8.351032,-6.505536,-0.924534,5.674450,-8.866718],[1.744236,4.445933,-1.577330,-0.494491,8.653086,-9.550218,4.861667,3.301918],[-6.756169,-7.982605,-0.558231,4.552939,-2.935783,-3.397971,3.539719,-3.721952],[1.017414,-6.038436,-6.577615,-9.771082,6.096465,-6.647235,-4.626717,5.375924],[5.624597,-1.769230,-9.491250,-6.655634,-8.163824,-6.843029,3.735109,-5.778698],[-7.590938,-5.086339,9.196706,-5.901884,-3.860436,-7.132928,5.870017,4.406436],[0.184752,-4.073343,2.305978,-1.798327,7.009598,9.558062,0.317653,-0.253763]],[[-3.958837,-3.080385,3.954110,4.700238,8.356632,2.049643,2.835475,-2.928024],[-5.263959,-6.193456,1.649777,7.455968,-6.492946,-5.630294,0.915499,5.781298],[8.479918,9.858868,5.254452,-1.958416,-4.435392,8.616651,0.143665,4.230879],[-8.377697,3.507206,-6.356781,-1.025271,-7.695533,9.376314,6.099515,2.886890],[-5.755876,-3.230689,7.624496,4.801413,-1.976695,4.740342,-6.245379,5.630578],[0.012361,-7.995592,-1.930351,-9.732633,2.761406,-8.760642,-2.697090,-5.147491],[-7.778814,-4.481732,8.008276,-0.094664,-6.606124,2.106549,-4.882680,0.102622],[-7.460104,7.401293,0.141596,6.110971,3.119722,6.439315,6.549499,6.146331],[-9.576208,-5.360527,3.771464,9.031142,-7.490958,-9.820719,-4.514914,-9.360952],[5.049507,9.686690,1.414555,-4.674108,-4.183661,2.735899,6.898700,5.370111],[-6.200488,9.101678,-1.968009,-4.852977,-5.280417,0.466925,-2.912285,2.762378],[-6.646448,-5.305543,3.254873,-1.940380,4.248553,1.933717,-6.833455,-5.477421],[-3.247241,-3.877341,4.814474,-1.577786,3.792230,-5.118188,0.671078,-5.262672],[-5.835551,-8.800115,1.178077,9.467906,-2.492086,6.005136,1.905569,5.551342]],[[1.919980,0.571827,-7.899496,-4.754275,8.954457,-3.936605,-3.284824,-4.574265],[7.072086,-3.531859,-2.876103,7.253119,5.258252,0.916646,5.625240,-7.148014],[5.397111,4.933425,5.457773,6.765712,-0.948551,-5.739105,-2.837780,6.420730],[6.383404,-9.729299,5.281174,-9.677197,-9.929217,8.173844,-0.674647,6.904785],[8.476419,-8.724568,-1.249945,-9.490225,4.434772,-2.458579,0.736941,8.989738],[7.861324,-6.297102,-4.744602,4.334361,0.035300,-4.926032,2.901452,0.137303],[-3.745918,6.083655,4.458566,2.555058,-0.147230,4.421511,1.516600,-7.336009],[-2.085019,9.436171,0.591943,-9.955064,4.195369,4.134527,-2.461014,-9.528023],[-7.818175,7.407521,4.403598,-7.692354,-3.445308,8.401401,-2.882297,4.714231],[7.558309,2.435357,1.770205,8.939747,-6.678489,0.380082,2.113204,9.490247],[-6.704723,2.216314,6.982934,9.884204,5.580736,8.690022,5.714102,3.536286],[1.390425,2.290857,-9.732762,-8.042508,2.351692,5.646645,7.357957,-9.325515],[4.299414,3.921649,8.590557,3.817622,7.861822,7.659254,2.968321,9.203341],[0.820905,1.142878,4.605695,0.327808,-5.192691,3.227001,7.630289,6.067139]],[[-2.527097,-3.036512,6.808167,-6.901423,-1.999132,2.144111,-0.653954,0.382606],[-2.867835,8.044089,-6.701951,-7.862378,7.587110,-7.440066,-8.394035,-2.423069],[-4.054761,-2.026692,-8.579398,-3.185817,-4.723228,-2.753045,3.206766,9.889035],[-1.722094,6.623316,5.036679,8.485076,-7.379589,7.183112,4.187169,4.397812],[-0.886260,-1.676064,-1.723466,-7.108125,-1.359863,-6.497184,-2.417810,3.428257],[-8.266531,0.271709,8.086452,8.741885,-5.109566,-6.142619,-6.192882,6.424131],[0.606353,7.549716,-4.915265,2.646969,-4.700912,-7.790201,7.528747,6.637349],[9.985396,1.177334,-7.371797,-0.107026,2.066505,-3.620262,-1.756893,8.307143],[9.406745,5.058645,-7.049039,7.886096,-9.851572,2.693497,1.391112,-6.868951],[4.202161,8.683168,-5.057329,-2.079727,-1.149888,9.867964,-2.366656,8.655863],[1.546815,6.212487,3.088193,-6.260616,2.197735,4.705195,-2.647247,7.664751],[4.857759,1.053708,-1.811760,7.979135,2.533692,1.002273,2.729108,0.622017],[2.618670,-9.334856,9.201528,3.313989,-3.523163,-3.735358,-1.970110,-3.449526],[-0.927553,2.349587,1.091633,-5.618656,0.927066,-6.243536,-0.274478,9.230289]],[[3.093187,-0.447634,-8.557831,9.280872,-0.743737,2.227290,9.390492,-6.600371],[-4.997907,-9.631351,-2.289074,-8.291096,-4.899520,5.682794,-9.353506,-9.005358],[-4.700378,8.921344,-1.998154,-8.065499,-4.983449,1.672043,2.303803,6.017329],[0.856495,-4.459505,-7.816493,9.506382,1.252704,3.310094,4.070461,8.024836],[-0.014399,-5.247051,3.700479,8.584420,8.521320,0.873424,-1.647266,-2.883282],[-6.204219,-9.918699,8.015441,2.078539,-2.699499,-1.776128,7.424667,7.687113],[-6.441004,-4.501346,-7.854318,0.798991,8.559553,4.734886,-9.790576,2.367420],[-1.058527,5.784683,-3.542697,-0.460651,-5.462068,-0.470820,7.389495,9.621284],[-3.090447,2.307721,-7.449095,-6.162859,-7.741768,8.525823,8.876728,7.387134],[-7.096871,1.329274,-0.018735,1.766805,-2.982111,-0.298284,-1.063323,-2.588643],[8.265999,7.669730,-8.953680,0.387830,9.576118,5.061785,-1.072044,-0.348539],[-8.371577,7.751615,-1.128355,9.980870,-3.683681,-0.652410,7.105864,5.558083],[-0.871157,-0.884675,-7.189968,2.579554,0.322964,-6.884638,-9.034486,-6.010978],[-6.084873,3.325710,3.602645,-8.489759,-0.532696,-1.580971,9.890527,-0.573268]]], dtype = "float32")#candidate|6346|(10, 14, 8)|const|float32
bop_6347 = relay.greater(var_6341.astype('bool'), relay.reshape(const_6346.astype('bool'), relay.shape_of(var_6341))) # shape=(10, 14, 8)
var_6355 = relay.var("var_6355", dtype = "float32", shape = (10, 14, 8))#candidate|6355|(10, 14, 8)|var|float32
bop_6356 = relay.logical_or(uop_6342.astype('bool'), relay.reshape(var_6355.astype('bool'), relay.shape_of(uop_6342))) # shape=(10, 14, 8)
uop_6360 = relay.log2(var_6341.astype('float64')) # shape=(10, 14, 8)
func_5218_call = mod.get_global_var('func_5218')
func_5219_call = mutated_mod.get_global_var('func_5219')
call_6364 = relay.TupleGetItem(func_5218_call(), 3)
call_6365 = relay.TupleGetItem(func_5219_call(), 3)
bop_6366 = relay.logical_and(uop_6360.astype('bool'), relay.reshape(bop_6356.astype('bool'), relay.shape_of(uop_6360))) # shape=(10, 14, 8)
uop_6381 = relay.asinh(uop_6360.astype('float64')) # shape=(10, 14, 8)
bop_6387 = relay.equal(uop_6381.astype('bool'), relay.reshape(bop_6347.astype('bool'), relay.shape_of(uop_6381))) # shape=(10, 14, 8)
func_2474_call = mod.get_global_var('func_2474')
func_2476_call = mutated_mod.get_global_var('func_2476')
call_6390 = relay.TupleGetItem(func_2474_call(), 0)
call_6391 = relay.TupleGetItem(func_2476_call(), 0)
uop_6400 = relay.rsqrt(bop_6387.astype('float64')) # shape=(10, 14, 8)
func_602_call = mod.get_global_var('func_602')
func_603_call = mutated_mod.get_global_var('func_603')
call_6402 = relay.TupleGetItem(func_602_call(), 0)
call_6403 = relay.TupleGetItem(func_603_call(), 0)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_6405 = func_2967_call()
call_6406 = func_2967_call()
output = relay.Tuple([call_6364,bop_6366,call_6390,uop_6400,call_6402,call_6405,])
output2 = relay.Tuple([call_6365,bop_6366,call_6391,uop_6400,call_6403,call_6406,])
func_6413 = relay.Function([var_6341,var_6355,], output)
mod['func_6413'] = func_6413
mod = relay.transform.InferType()(mod)
mutated_mod['func_6413'] = func_6413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6413_call = mutated_mod.get_global_var('func_6413')
var_6415 = relay.var("var_6415", dtype = "float32", shape = (10, 14, 8))#candidate|6415|(10, 14, 8)|var|float32
var_6416 = relay.var("var_6416", dtype = "float32", shape = (10, 14, 8))#candidate|6416|(10, 14, 8)|var|float32
call_6414 = func_6413_call(var_6415,var_6416,)
output = call_6414
func_6417 = relay.Function([var_6415,var_6416,], output)
mutated_mod['func_6417'] = func_6417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5218_call = mod.get_global_var('func_5218')
func_5219_call = mutated_mod.get_global_var('func_5219')
call_6419 = relay.TupleGetItem(func_5218_call(), 1)
call_6420 = relay.TupleGetItem(func_5219_call(), 1)
output = call_6419
output2 = call_6420
func_6425 = relay.Function([], output)
mod['func_6425'] = func_6425
mod = relay.transform.InferType()(mod)
output = func_6425()
func_6426 = relay.Function([], output)
mutated_mod['func_6426'] = func_6426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6554 = relay.var("var_6554", dtype = "int64", shape = (15, 4, 2))#candidate|6554|(15, 4, 2)|var|int64
const_6555 = relay.const([[[5,-9],[7,10],[-7,3],[-3,-6]],[[1,9],[6,2],[-3,-4],[5,6]],[[8,-8],[-5,1],[7,4],[6,6]],[[-8,5],[-7,8],[9,1],[-1,-1]],[[2,-4],[-10,-1],[-8,8],[-6,1]],[[1,10],[3,10],[-9,4],[-7,9]],[[-6,6],[-9,-2],[-3,8],[7,5]],[[-5,6],[2,-10],[6,-3],[10,-2]],[[-6,-2],[-9,-9],[-7,4],[-8,1]],[[-4,3],[-2,9],[10,-3],[-3,-7]],[[-7,-3],[3,9],[-10,-3],[-1,-4]],[[-3,1],[4,5],[1,4],[-5,2]],[[-10,-8],[-6,5],[1,-6],[4,9]],[[9,-5],[1,4],[-10,-5],[-9,-10]],[[-1,-2],[-7,-5],[-4,-5],[1,8]]], dtype = "int64")#candidate|6555|(15, 4, 2)|const|int64
bop_6556 = relay.add(var_6554.astype('int64'), relay.reshape(const_6555.astype('int64'), relay.shape_of(var_6554))) # shape=(15, 4, 2)
output = relay.Tuple([bop_6556,])
output2 = relay.Tuple([bop_6556,])
F = relay.Function([var_6554,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6554,], output2)
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
