import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_74 = relay.var("var_74", dtype = "float64", shape = (10, 5, 12))#candidate|74|(10, 5, 12)|var|float64
uop_75 = relay.acosh(var_74.astype('float64')) # shape=(10, 5, 12)
output = relay.Tuple([uop_75,])
output2 = relay.Tuple([uop_75,])
func_88 = relay.Function([var_74,], output)
mod['func_88'] = func_88
mod = relay.transform.InferType()(mod)
var_89 = relay.var("var_89", dtype = "float64", shape = (10, 5, 12))#candidate|89|(10, 5, 12)|var|float64
output = func_88(var_89)
func_90 = relay.Function([var_89], output)
mutated_mod['func_90'] = func_90
mutated_mod = relay.transform.InferType()(mutated_mod)
var_210 = relay.var("var_210", dtype = "float64", shape = (2, 2, 3))#candidate|210|(2, 2, 3)|var|float64
const_211 = relay.const([[[8.673883,0.330609,-3.054156],[-7.453589,9.822424,1.136451]],[[-8.386672,-0.012640,-8.917751],[-9.500323,2.945579,5.177872]]], dtype = "float64")#candidate|211|(2, 2, 3)|const|float64
bop_212 = relay.mod(var_210.astype('float64'), relay.reshape(const_211.astype('float64'), relay.shape_of(var_210))) # shape=(2, 2, 3)
var_234 = relay.var("var_234", dtype = "float64", shape = (2, 2, 3))#candidate|234|(2, 2, 3)|var|float64
bop_235 = relay.power(const_211.astype('float32'), relay.reshape(var_234.astype('float32'), relay.shape_of(const_211))) # shape=(2, 2, 3)
func_88_call = mod.get_global_var('func_88')
func_90_call = mutated_mod.get_global_var('func_90')
const_239 = relay.const([1.230560,1.727871,1.579200,-4.441586,-3.706331,-1.204099,3.795566,-6.414698,8.121039,-2.238675,5.987851,5.172053,-8.015263,4.691388,4.995072,0.302759,-2.430559,1.091668,-8.602697,3.952010,1.429368,1.032537,-9.732545,5.759911,-0.629646,6.236708,-4.268197,9.145734,2.565182,-7.050644,4.026856,-1.269634,9.544446,9.028020,4.764970,-8.261185,-0.011824,6.893409,1.098216,0.374913,8.775235,3.051690,2.196354,-7.702807,8.712158,6.904236,2.543953,8.458659,5.523996,-5.538496,6.716242,7.316127,-0.446293,-7.984243,-8.283866,5.989994,-2.321214,1.631972,4.262190,-7.080340,-3.698797,6.917690,5.044028,-8.186402,1.731499,3.933048,8.741027,2.496630,-4.285053,-9.040661,4.924732,-5.278062,-8.870538,8.163167,5.033560,6.097381,9.483530,2.179475,7.052442,0.873481,5.833711,5.395842,-6.652706,-7.519912,-2.389160,1.768815,5.573639,8.889677,0.101316,6.165100,-2.597386,-3.453980,-0.031017,3.021488,-7.856925,-8.084631,8.780272,-7.072313,-2.749254,-8.587714,8.678804,-5.596851,4.954989,7.686866,-4.934880,-2.807509,5.414610,-0.191364,-0.622551,1.218600,0.812564,-3.228448,5.641918,-0.693335,-2.014517,-0.973998,-4.386164,-7.479811,-8.781730,-0.497311,-4.924415,0.689647,3.171363,5.290384,4.381600,-8.106011,6.199177,-6.589377,-8.860878,-2.670626,2.456658,-1.811410,-4.539403,-0.065083,-0.757862,3.260401,4.005575,-6.923365,8.852023,-0.029400,-7.320905,0.370286,-9.021384,-0.350000,-7.720890,8.663934,6.054309,4.081276,-7.529558,-6.795967,-8.469790,3.101225,0.155997,-1.841712,-1.745995,3.692751,-0.070101,-3.448831,-6.978159,2.510657,2.077957,0.465096,-9.757697,-0.306434,-5.185507,-7.335222,2.130907,-7.825686,4.444347,3.720565,1.237738,8.902991,1.412715,-6.968467,-0.587273,-4.296209,-3.298198,2.632101,-9.641440,3.799109,-9.528720,0.934846,-5.181817,-4.385343,-5.835461,3.782736,9.681216,3.015377,-7.174664,-2.942616,9.276543,-0.700949,-7.806552,7.448097,-3.000477,6.088465,-4.961589,-9.181191,-8.429893,-5.940261,-5.718714,5.864334,-3.869315,-5.247175,-0.192735,-8.766706,3.730450,-3.783473,-2.806376,-1.955499,-9.257367,9.959098,-9.598249,3.200948,6.434946,9.298804,9.538720,5.965135,-6.357254,-2.104811,-9.259707,-5.414695,-1.607623,-9.350830,-5.723939,1.775591,-9.985391,8.513734,-7.208266,-3.203617,6.018656,0.297278,-6.203666,-1.287347,-9.072417,6.099746,6.502263,-6.879066,-2.870997,-4.458473,5.717128,-5.676477,5.028179,-5.744406,-1.537786,6.373043,-7.915453,8.746032,5.430190,7.048450,-1.398195,-3.987297,3.116467,3.822787,8.660010,-6.758708,3.392141,6.696842,1.578709,-5.209836,-0.926688,6.612456,-6.462780,2.444377,-7.578646,6.512128,2.953450,3.585111,-6.022280,0.308225,-3.997150,-0.911536,-9.228312,-5.264720,0.897262,6.220832,-1.230881,9.565681,5.252281,-1.000763,9.271593,0.013261,-2.930747,1.871884,7.947409,-3.744225,4.391654,-5.850779,-9.218116,9.072478,7.823908,4.030274,2.039902,6.450545,9.187898,-8.569596,7.780441,-5.171286,-5.197946,0.764768,-1.071166,-2.878158,-9.337718,7.603290,8.088728,4.796659,2.474705,4.172872,4.565864,-7.944935,-7.060503,0.441766,-7.782553,7.636990,-8.732923,-5.853420,2.264465,-8.768529,5.929532,-4.809821,-3.090914,-2.078266,2.547756,-4.004591,-6.576963,7.562403,1.532502,-5.894782,-3.950559,8.525469,-8.329973,5.014180,-5.222572,-9.542619,3.445257,-6.121470,-8.365155,-6.734687,-3.455108,-9.216745,9.938062,-7.818289,-2.316753,-4.269620,-9.391613,1.802371,1.318084,-3.705204,-9.346033,-7.676569,-9.459942,1.347662,8.466841,-0.318693,-7.837412,-6.989626,-5.317875,0.739474,8.622304,-3.004083,6.859344,2.384210,-7.378427,-7.589681,-7.258463,2.067803,7.642874,4.468585,-0.442616,4.321050,-1.914933,-0.504659,-2.071433,8.384882,5.477151,7.201321,-7.961538,1.795438,4.351658,2.229482,-1.870869,-2.092659,-2.440733,-0.742150,2.765639,1.018494,6.071380,-0.488480,6.374012,-1.521682,5.277778,1.824031,-7.824992,2.191473,-7.738959,6.345281,4.134370,9.870355,9.952004,-5.105545,0.314863,-0.037428,8.938749,-3.451809,-7.223206,7.598599,-0.846064,1.396734,2.169910,-0.972570,-5.279207,7.084646,7.769586,5.289035,-6.773433,3.437131,5.521093,2.143648,1.870155,-4.502033,-9.226729,0.917778,-5.436502,5.158685,2.914658,-8.408694,5.041224,7.252146,-3.691730,4.208741,-2.356863,-4.506083,-7.423500,-0.011926,2.716515,7.590347,-7.860786,-6.994917,-5.392015,6.862112,-4.981071,3.101416,9.525428,-3.335632,9.815055,-4.127513,1.411435,9.383038,-2.761910,0.406869,-1.059994,1.216770,5.445166,-1.953213,7.958255,-2.830761,1.513514,8.625981,-8.040702,-1.464596,0.539603,-2.644854,7.180119,-7.634651,9.977544,1.193765,5.255666,5.157438,-4.322175,-2.238258,1.810955,9.239821,-8.916695,6.606664,4.338774,-4.414590,-5.617030,3.321450,-6.945698,-9.854073,8.238456,-8.740989,-3.898744,3.316708,8.531127,4.383106,-7.094664,0.841480,5.408305,-6.243361,-5.225691,-5.752857,8.828494,-7.247725,9.339699,5.541513,-3.611507,4.208849,7.399080,7.615986,-5.237553,3.625846,-0.064417,6.191696,3.932985,-3.334521,-8.404682,4.990272,-1.580897,-1.679667,-4.514350,-2.044059,4.316128,6.938852,-0.196912,6.321797,6.957444,-5.468266,6.833201,-0.445628,3.134571,-5.759252,5.608311,5.603967,2.024297,1.949891,1.182436,-7.166077,-4.485679,-2.456047,-2.694427,5.981031,-8.903345,4.890273,-2.851047,5.577660,-3.190455,7.522833,2.482628,9.287191,-0.632561,-3.168414,-5.822135,-2.955215,-4.554072,-9.898477,-7.126600,1.898237,7.647520,-4.535323,-4.363950,3.992441,5.216231,-7.744440,2.533818,6.076094,-0.633515,9.944087,-8.332454,3.175297,-9.952881,-6.884625,-2.218674,-5.759027,-5.820929,2.288245,-6.699473,-7.914267,3.686255,-3.478035,-5.073766,6.968098,7.475439,-8.475207,-1.631192,-3.642805,4.658627,-5.995450,-3.489045,6.075381,9.785279,0.087458,9.446958,-2.598749,-9.357367,8.306436,-9.722432,-6.453818,9.261763,-7.885065,-5.765436,0.221902,7.207349,0.963956,-0.231867,-4.993665,1.173277,8.937132,1.366653,-2.029109], dtype = "float64")#candidate|239|(600,)|const|float64
call_238 = relay.TupleGetItem(func_88_call(relay.reshape(const_239.astype('float64'), [10, 5, 12])), 0)
call_240 = relay.TupleGetItem(func_90_call(relay.reshape(const_239.astype('float64'), [10, 5, 12])), 0)
func_88_call = mod.get_global_var('func_88')
func_90_call = mutated_mod.get_global_var('func_90')
call_248 = relay.TupleGetItem(func_88_call(relay.reshape(call_238.astype('float64'), [10, 5, 12])), 0)
call_249 = relay.TupleGetItem(func_90_call(relay.reshape(call_238.astype('float64'), [10, 5, 12])), 0)
output = relay.Tuple([bop_212,bop_235,call_238,const_239,call_248,])
output2 = relay.Tuple([bop_212,bop_235,call_240,const_239,call_249,])
func_256 = relay.Function([var_210,var_234,], output)
mod['func_256'] = func_256
mod = relay.transform.InferType()(mod)
var_257 = relay.var("var_257", dtype = "float64", shape = (2, 2, 3))#candidate|257|(2, 2, 3)|var|float64
var_258 = relay.var("var_258", dtype = "float64", shape = (2, 2, 3))#candidate|258|(2, 2, 3)|var|float64
output = func_256(var_257,var_258,)
func_259 = relay.Function([var_257,var_258,], output)
mutated_mod['func_259'] = func_259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_474 = relay.var("var_474", dtype = "float32", shape = (10, 5, 16))#candidate|474|(10, 5, 16)|var|float32
uop_475 = relay.rsqrt(var_474.astype('float32')) # shape=(10, 5, 16)
output = uop_475
output2 = uop_475
func_489 = relay.Function([var_474,], output)
mod['func_489'] = func_489
mod = relay.transform.InferType()(mod)
mutated_mod['func_489'] = func_489
mutated_mod = relay.transform.InferType()(mutated_mod)
var_490 = relay.var("var_490", dtype = "float32", shape = (10, 5, 16))#candidate|490|(10, 5, 16)|var|float32
func_489_call = mutated_mod.get_global_var('func_489')
call_491 = func_489_call(var_490)
output = call_491
func_492 = relay.Function([var_490], output)
mutated_mod['func_492'] = func_492
mutated_mod = relay.transform.InferType()(mutated_mod)
const_494 = relay.const(-9.912255, dtype = "float32")#candidate|494|()|const|float32
var_495 = relay.var("var_495", dtype = "float32", shape = (1, 8, 11))#candidate|495|(1, 8, 11)|var|float32
bop_496 = relay.power(const_494.astype('float32'), var_495.astype('float32')) # shape=(1, 8, 11)
uop_500 = relay.asin(var_495.astype('float64')) # shape=(1, 8, 11)
func_256_call = mod.get_global_var('func_256')
func_259_call = mutated_mod.get_global_var('func_259')
var_509 = relay.var("var_509", dtype = "float64", shape = (12,))#candidate|509|(12,)|var|float64
call_508 = relay.TupleGetItem(func_256_call(relay.reshape(var_509.astype('float64'), [2, 2, 3]), relay.reshape(var_509.astype('float64'), [2, 2, 3]), ), 0)
call_510 = relay.TupleGetItem(func_259_call(relay.reshape(var_509.astype('float64'), [2, 2, 3]), relay.reshape(var_509.astype('float64'), [2, 2, 3]), ), 0)
func_256_call = mod.get_global_var('func_256')
func_259_call = mutated_mod.get_global_var('func_259')
call_540 = relay.TupleGetItem(func_256_call(relay.reshape(call_508.astype('float64'), [2, 2, 3]), relay.reshape(call_508.astype('float64'), [2, 2, 3]), ), 3)
call_541 = relay.TupleGetItem(func_259_call(relay.reshape(call_508.astype('float64'), [2, 2, 3]), relay.reshape(call_508.astype('float64'), [2, 2, 3]), ), 3)
bop_544 = relay.not_equal(uop_500.astype('bool'), relay.reshape(var_495.astype('bool'), relay.shape_of(uop_500))) # shape=(1, 8, 11)
uop_548 = relay.log2(call_540.astype('float64')) # shape=(600,)
uop_550 = relay.log2(call_541.astype('float64')) # shape=(600,)
output = relay.Tuple([bop_496,call_508,var_509,bop_544,uop_548,])
output2 = relay.Tuple([bop_496,call_510,var_509,bop_544,uop_550,])
func_567 = relay.Function([var_495,var_509,], output)
mod['func_567'] = func_567
mod = relay.transform.InferType()(mod)
mutated_mod['func_567'] = func_567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_567_call = mutated_mod.get_global_var('func_567')
var_569 = relay.var("var_569", dtype = "float32", shape = (1, 8, 11))#candidate|569|(1, 8, 11)|var|float32
var_570 = relay.var("var_570", dtype = "float64", shape = (12,))#candidate|570|(12,)|var|float64
call_568 = func_567_call(var_569,var_570,)
output = call_568
func_571 = relay.Function([var_569,var_570,], output)
mutated_mod['func_571'] = func_571
mutated_mod = relay.transform.InferType()(mutated_mod)
const_806 = relay.const([[[-0.932725,9.406311,6.459311,1.291276],[2.046208,8.794100,-5.018048,8.149666],[-8.943156,-0.322410,9.256838,3.163431],[-3.409033,-0.153000,9.459526,6.374154],[9.352040,-7.562896,2.201587,-9.729146]]], dtype = "float32")#candidate|806|(1, 5, 4)|const|float32
uop_807 = relay.acosh(const_806.astype('float32')) # shape=(1, 5, 4)
output = uop_807
output2 = uop_807
func_811 = relay.Function([], output)
mod['func_811'] = func_811
mod = relay.transform.InferType()(mod)
output = func_811()
func_812 = relay.Function([], output)
mutated_mod['func_812'] = func_812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mod.get_global_var('func_811')
func_812_call = mutated_mod.get_global_var('func_812')
call_824 = func_811_call()
call_825 = func_811_call()
uop_839 = relay.rsqrt(call_824.astype('float32')) # shape=(1, 5, 4)
uop_841 = relay.rsqrt(call_825.astype('float32')) # shape=(1, 5, 4)
bop_842 = relay.bitwise_or(uop_839.astype('int8'), relay.reshape(call_824.astype('int8'), relay.shape_of(uop_839))) # shape=(1, 5, 4)
bop_845 = relay.bitwise_or(uop_841.astype('int8'), relay.reshape(call_825.astype('int8'), relay.shape_of(uop_841))) # shape=(1, 5, 4)
output = relay.Tuple([bop_842,])
output2 = relay.Tuple([bop_845,])
func_849 = relay.Function([], output)
mod['func_849'] = func_849
mod = relay.transform.InferType()(mod)
mutated_mod['func_849'] = func_849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_849_call = mutated_mod.get_global_var('func_849')
call_850 = func_849_call()
output = call_850
func_851 = relay.Function([], output)
mutated_mod['func_851'] = func_851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mod.get_global_var('func_811')
func_812_call = mutated_mod.get_global_var('func_812')
call_852 = func_811_call()
call_853 = func_811_call()
func_811_call = mod.get_global_var('func_811')
func_812_call = mutated_mod.get_global_var('func_812')
call_860 = func_811_call()
call_861 = func_811_call()
uop_863 = relay.sinh(call_852.astype('float64')) # shape=(1, 5, 4)
uop_865 = relay.sinh(call_853.astype('float64')) # shape=(1, 5, 4)
uop_879 = relay.cosh(uop_863.astype('float32')) # shape=(1, 5, 4)
uop_881 = relay.cosh(uop_865.astype('float32')) # shape=(1, 5, 4)
func_256_call = mod.get_global_var('func_256')
func_259_call = mutated_mod.get_global_var('func_259')
var_883 = relay.var("var_883", dtype = "float64", shape = (12,))#candidate|883|(12,)|var|float64
call_882 = relay.TupleGetItem(func_256_call(relay.reshape(var_883.astype('float64'), [2, 2, 3]), relay.reshape(var_883.astype('float64'), [2, 2, 3]), ), 4)
call_884 = relay.TupleGetItem(func_259_call(relay.reshape(var_883.astype('float64'), [2, 2, 3]), relay.reshape(var_883.astype('float64'), [2, 2, 3]), ), 4)
output = relay.Tuple([call_860,uop_879,call_882,var_883,])
output2 = relay.Tuple([call_861,uop_881,call_884,var_883,])
func_887 = relay.Function([var_883,], output)
mod['func_887'] = func_887
mod = relay.transform.InferType()(mod)
mutated_mod['func_887'] = func_887
mutated_mod = relay.transform.InferType()(mutated_mod)
var_888 = relay.var("var_888", dtype = "float64", shape = (12,))#candidate|888|(12,)|var|float64
func_887_call = mutated_mod.get_global_var('func_887')
call_889 = func_887_call(var_888)
output = call_889
func_890 = relay.Function([var_888], output)
mutated_mod['func_890'] = func_890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_921 = relay.TupleGetItem(func_849_call(), 0)
call_922 = relay.TupleGetItem(func_851_call(), 0)
output = relay.Tuple([call_921,])
output2 = relay.Tuple([call_922,])
func_928 = relay.Function([], output)
mod['func_928'] = func_928
mod = relay.transform.InferType()(mod)
output = func_928()
func_929 = relay.Function([], output)
mutated_mod['func_929'] = func_929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_988 = relay.TupleGetItem(func_849_call(), 0)
call_989 = relay.TupleGetItem(func_851_call(), 0)
var_991 = relay.var("var_991", dtype = "int8", shape = (10, 5, 4))#candidate|991|(10, 5, 4)|var|int8
bop_992 = relay.multiply(call_988.astype('int64'), var_991.astype('int64')) # shape=(10, 5, 4)
bop_995 = relay.multiply(call_989.astype('int64'), var_991.astype('int64')) # shape=(10, 5, 4)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_1005 = relay.TupleGetItem(func_928_call(), 0)
call_1006 = relay.TupleGetItem(func_929_call(), 0)
uop_1037 = relay.log2(call_1005.astype('float32')) # shape=(1, 5, 4)
uop_1039 = relay.log2(call_1006.astype('float32')) # shape=(1, 5, 4)
func_489_call = mod.get_global_var('func_489')
func_492_call = mutated_mod.get_global_var('func_492')
var_1046 = relay.var("var_1046", dtype = "float32", shape = (800,))#candidate|1046|(800,)|var|float32
call_1045 = func_489_call(relay.reshape(var_1046.astype('float32'), [10, 5, 16]))
call_1047 = func_489_call(relay.reshape(var_1046.astype('float32'), [10, 5, 16]))
bop_1050 = relay.bitwise_and(uop_1037.astype('int32'), relay.reshape(call_988.astype('int32'), relay.shape_of(uop_1037))) # shape=(1, 5, 4)
bop_1053 = relay.bitwise_and(uop_1039.astype('int32'), relay.reshape(call_989.astype('int32'), relay.shape_of(uop_1039))) # shape=(1, 5, 4)
output = relay.Tuple([bop_992,call_1045,var_1046,bop_1050,])
output2 = relay.Tuple([bop_995,call_1047,var_1046,bop_1053,])
func_1056 = relay.Function([var_991,var_1046,], output)
mod['func_1056'] = func_1056
mod = relay.transform.InferType()(mod)
var_1057 = relay.var("var_1057", dtype = "int8", shape = (10, 5, 4))#candidate|1057|(10, 5, 4)|var|int8
var_1058 = relay.var("var_1058", dtype = "float32", shape = (800,))#candidate|1058|(800,)|var|float32
output = func_1056(var_1057,var_1058,)
func_1059 = relay.Function([var_1057,var_1058,], output)
mutated_mod['func_1059'] = func_1059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mod.get_global_var('func_811')
func_812_call = mutated_mod.get_global_var('func_812')
call_1124 = func_811_call()
call_1125 = func_811_call()
output = call_1124
output2 = call_1125
func_1126 = relay.Function([], output)
mod['func_1126'] = func_1126
mod = relay.transform.InferType()(mod)
output = func_1126()
func_1127 = relay.Function([], output)
mutated_mod['func_1127'] = func_1127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_1191 = func_1126_call()
call_1192 = func_1126_call()
uop_1210 = relay.exp(call_1191.astype('float32')) # shape=(1, 5, 4)
uop_1212 = relay.exp(call_1192.astype('float32')) # shape=(1, 5, 4)
output = relay.Tuple([uop_1210,])
output2 = relay.Tuple([uop_1212,])
func_1213 = relay.Function([], output)
mod['func_1213'] = func_1213
mod = relay.transform.InferType()(mod)
mutated_mod['func_1213'] = func_1213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1213_call = mutated_mod.get_global_var('func_1213')
call_1214 = func_1213_call()
output = call_1214
func_1215 = relay.Function([], output)
mutated_mod['func_1215'] = func_1215
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1218 = relay.var("var_1218", dtype = "float64", shape = (8, 16, 1))#candidate|1218|(8, 16, 1)|var|float64
uop_1219 = relay.exp(var_1218.astype('float64')) # shape=(8, 16, 1)
bop_1231 = relay.mod(uop_1219.astype('float64'), relay.reshape(var_1218.astype('float64'), relay.shape_of(uop_1219))) # shape=(8, 16, 1)
bop_1241 = relay.logical_or(bop_1231.astype('bool'), relay.reshape(uop_1219.astype('bool'), relay.shape_of(bop_1231))) # shape=(8, 16, 1)
output = relay.Tuple([bop_1241,])
output2 = relay.Tuple([bop_1241,])
func_1246 = relay.Function([var_1218,], output)
mod['func_1246'] = func_1246
mod = relay.transform.InferType()(mod)
var_1247 = relay.var("var_1247", dtype = "float64", shape = (8, 16, 1))#candidate|1247|(8, 16, 1)|var|float64
output = func_1246(var_1247)
func_1248 = relay.Function([var_1247], output)
mutated_mod['func_1248'] = func_1248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mod.get_global_var('func_811')
func_812_call = mutated_mod.get_global_var('func_812')
call_1263 = func_811_call()
call_1264 = func_811_call()
output = call_1263
output2 = call_1264
func_1270 = relay.Function([], output)
mod['func_1270'] = func_1270
mod = relay.transform.InferType()(mod)
mutated_mod['func_1270'] = func_1270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mutated_mod.get_global_var('func_1270')
call_1271 = func_1270_call()
output = call_1271
func_1272 = relay.Function([], output)
mutated_mod['func_1272'] = func_1272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_1329 = func_1270_call()
call_1330 = func_1270_call()
uop_1337 = relay.asin(call_1329.astype('float32')) # shape=(1, 5, 4)
uop_1339 = relay.asin(call_1330.astype('float32')) # shape=(1, 5, 4)
func_887_call = mod.get_global_var('func_887')
func_890_call = mutated_mod.get_global_var('func_890')
const_1343 = relay.const([4.215405,-1.399853,-0.461243,-2.049186,-9.817533,-1.543204,-2.973976,-7.920354,-2.531206,-5.128897,2.537110,-5.099341], dtype = "float64")#candidate|1343|(12,)|const|float64
call_1342 = relay.TupleGetItem(func_887_call(relay.reshape(const_1343.astype('float64'), [12,])), 2)
call_1344 = relay.TupleGetItem(func_890_call(relay.reshape(const_1343.astype('float64'), [12,])), 2)
bop_1358 = relay.floor_mod(uop_1337.astype('float32'), relay.reshape(call_1329.astype('float32'), relay.shape_of(uop_1337))) # shape=(1, 5, 4)
bop_1361 = relay.floor_mod(uop_1339.astype('float32'), relay.reshape(call_1330.astype('float32'), relay.shape_of(uop_1339))) # shape=(1, 5, 4)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_1368 = func_1126_call()
call_1369 = func_1126_call()
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_1378 = func_1126_call()
call_1379 = func_1126_call()
uop_1385 = relay.rsqrt(call_1342.astype('float32')) # shape=(10, 5, 12)
uop_1387 = relay.rsqrt(call_1344.astype('float32')) # shape=(10, 5, 12)
output = relay.Tuple([const_1343,bop_1358,call_1368,call_1378,uop_1385,])
output2 = relay.Tuple([const_1343,bop_1361,call_1369,call_1379,uop_1387,])
func_1397 = relay.Function([], output)
mod['func_1397'] = func_1397
mod = relay.transform.InferType()(mod)
mutated_mod['func_1397'] = func_1397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1397_call = mutated_mod.get_global_var('func_1397')
call_1398 = func_1397_call()
output = call_1398
func_1399 = relay.Function([], output)
mutated_mod['func_1399'] = func_1399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_1408 = relay.TupleGetItem(func_1397_call(), 0)
call_1409 = relay.TupleGetItem(func_1399_call(), 0)
output = relay.Tuple([call_1408,])
output2 = relay.Tuple([call_1409,])
func_1431 = relay.Function([], output)
mod['func_1431'] = func_1431
mod = relay.transform.InferType()(mod)
mutated_mod['func_1431'] = func_1431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1431_call = mutated_mod.get_global_var('func_1431')
call_1432 = func_1431_call()
output = call_1432
func_1433 = relay.Function([], output)
mutated_mod['func_1433'] = func_1433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_1538 = func_1126_call()
call_1539 = func_1126_call()
const_1567 = relay.const([[[-1.682852,8.788138,0.507163,0.930644],[-5.591658,-1.342529,-6.273198,-1.954049],[5.964206,5.764701,3.953576,0.988416],[9.158879,-5.152242,-3.100782,9.328842],[2.266594,9.708684,3.979131,9.465105]],[[9.364127,7.475590,3.488157,-2.567548],[6.592659,-0.389911,6.952184,5.378979],[8.253454,-2.957087,-3.714751,8.439441],[-2.453322,-4.418175,8.144310,7.139020],[6.615946,-5.621354,-6.394567,0.676888]],[[9.563830,4.524894,4.464893,4.071795],[-4.446335,0.955926,-1.596534,5.293025],[8.747533,-5.256458,4.311991,8.146944],[-5.527781,3.732297,-0.334349,-2.221980],[-1.210867,-3.327168,0.688809,7.270827]],[[6.307847,-2.507110,2.151300,-6.613511],[9.326381,1.775458,-8.941430,7.094312],[-0.045891,-1.401323,-8.719070,-5.493116],[-7.392467,-5.421842,4.512602,1.889137],[-5.374327,-9.653746,7.622230,8.960853]],[[4.477502,-9.537805,8.157668,-3.407369],[-5.389432,6.918417,9.496858,-4.660109],[-7.426241,0.694123,-9.743684,7.216326],[-6.773823,-9.508754,-6.764052,-8.970989],[-4.538173,-6.028119,0.491057,3.904709]],[[9.303419,-2.491377,0.849211,-9.156613],[0.944619,8.689040,-9.615255,9.041380],[-0.650075,3.073225,4.383318,-0.598131],[-2.325278,5.058724,4.045872,2.546996],[0.146696,9.231649,-8.185602,1.771236]]], dtype = "float32")#candidate|1567|(6, 5, 4)|const|float32
bop_1568 = relay.logical_xor(call_1538.astype('uint16'), const_1567.astype('uint16')) # shape=(6, 5, 4)
bop_1571 = relay.logical_xor(call_1539.astype('uint16'), const_1567.astype('uint16')) # shape=(6, 5, 4)
uop_1581 = relay.log(call_1538.astype('float64')) # shape=(1, 5, 4)
uop_1583 = relay.log(call_1539.astype('float64')) # shape=(1, 5, 4)
output = relay.Tuple([bop_1568,uop_1581,])
output2 = relay.Tuple([bop_1571,uop_1583,])
func_1586 = relay.Function([], output)
mod['func_1586'] = func_1586
mod = relay.transform.InferType()(mod)
mutated_mod['func_1586'] = func_1586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1586_call = mutated_mod.get_global_var('func_1586')
call_1587 = func_1586_call()
output = call_1587
func_1588 = relay.Function([], output)
mutated_mod['func_1588'] = func_1588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_1595 = relay.TupleGetItem(func_1397_call(), 0)
call_1596 = relay.TupleGetItem(func_1399_call(), 0)
output = relay.Tuple([call_1595,])
output2 = relay.Tuple([call_1596,])
func_1597 = relay.Function([], output)
mod['func_1597'] = func_1597
mod = relay.transform.InferType()(mod)
mutated_mod['func_1597'] = func_1597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mutated_mod.get_global_var('func_1597')
call_1598 = func_1597_call()
output = call_1598
func_1599 = relay.Function([], output)
mutated_mod['func_1599'] = func_1599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_1684 = relay.TupleGetItem(func_928_call(), 0)
call_1685 = relay.TupleGetItem(func_929_call(), 0)
uop_1689 = relay.sin(call_1684.astype('float64')) # shape=(1, 5, 4)
uop_1691 = relay.sin(call_1685.astype('float64')) # shape=(1, 5, 4)
bop_1692 = relay.minimum(uop_1689.astype('uint64'), relay.reshape(call_1684.astype('uint64'), relay.shape_of(uop_1689))) # shape=(1, 5, 4)
bop_1695 = relay.minimum(uop_1691.astype('uint64'), relay.reshape(call_1685.astype('uint64'), relay.shape_of(uop_1691))) # shape=(1, 5, 4)
uop_1702 = relay.erf(uop_1689.astype('float32')) # shape=(1, 5, 4)
uop_1704 = relay.erf(uop_1691.astype('float32')) # shape=(1, 5, 4)
output = relay.Tuple([bop_1692,uop_1702,])
output2 = relay.Tuple([bop_1695,uop_1704,])
func_1716 = relay.Function([], output)
mod['func_1716'] = func_1716
mod = relay.transform.InferType()(mod)
output = func_1716()
func_1717 = relay.Function([], output)
mutated_mod['func_1717'] = func_1717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_1751 = func_1270_call()
call_1752 = func_1270_call()
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_1753 = relay.TupleGetItem(func_849_call(), 0)
call_1754 = relay.TupleGetItem(func_851_call(), 0)
uop_1760 = relay.atan(call_1751.astype('float32')) # shape=(1, 5, 4)
uop_1762 = relay.atan(call_1752.astype('float32')) # shape=(1, 5, 4)
func_88_call = mod.get_global_var('func_88')
func_90_call = mutated_mod.get_global_var('func_90')
var_1765 = relay.var("var_1765", dtype = "float64", shape = (600,))#candidate|1765|(600,)|var|float64
call_1764 = relay.TupleGetItem(func_88_call(relay.reshape(var_1765.astype('float64'), [10, 5, 12])), 0)
call_1766 = relay.TupleGetItem(func_90_call(relay.reshape(var_1765.astype('float64'), [10, 5, 12])), 0)
var_1767 = relay.var("var_1767", dtype = "float32", shape = (10, 5, 4))#candidate|1767|(10, 5, 4)|var|float32
bop_1768 = relay.power(uop_1760.astype('float64'), var_1767.astype('float64')) # shape=(10, 5, 4)
bop_1771 = relay.power(uop_1762.astype('float64'), var_1767.astype('float64')) # shape=(10, 5, 4)
bop_1778 = relay.greater_equal(uop_1760.astype('bool'), bop_1768.astype('bool')) # shape=(10, 5, 4)
bop_1781 = relay.greater_equal(uop_1762.astype('bool'), bop_1771.astype('bool')) # shape=(10, 5, 4)
const_1785 = relay.const([[[-8.115641,2.576410,-2.212309,5.047973],[1.849890,7.222322,8.600749,-0.474571],[3.026317,3.090907,-3.254758,-6.972891],[3.625434,9.491853,-9.532528,-0.555289],[-1.755240,6.186869,-5.659044,9.861349]],[[-5.086941,-5.157051,5.803559,-3.784976],[0.850243,-0.442750,-0.541360,-0.182706],[1.672919,3.793488,-7.868349,6.227122],[7.521799,8.692280,6.450950,-7.062685],[4.883902,-3.254509,3.471078,-5.206530]],[[-5.874649,-8.894343,8.218839,-0.450966],[5.657785,-6.130946,7.540728,-1.646900],[-3.907066,-2.559917,-0.373458,8.588842],[9.731890,-6.107121,-8.393783,5.644797],[-0.119736,2.888800,-1.777516,-5.737482]],[[-7.187935,9.968073,-4.301661,-3.754154],[-3.638613,3.930689,6.074062,-9.234564],[-4.921797,8.128639,5.784456,4.177668],[6.421270,0.458866,-3.899703,7.076402],[-1.040583,-8.443001,-6.969698,6.246505]],[[6.655098,8.431760,6.670623,1.386093],[2.519188,8.927713,-0.262436,-5.805458],[3.096074,0.018598,0.520264,-2.748490],[-0.165122,4.641845,-9.551257,2.415570],[0.784324,-0.084697,-7.944491,-7.117306]],[[4.003600,0.456385,-6.332179,0.416104],[9.831598,8.439035,7.823943,6.975825],[-2.962786,-6.128262,0.931819,-7.529952],[-8.869438,-7.049285,-0.502028,-1.722788],[-2.910421,4.148717,2.526392,-7.929212]],[[-5.844362,-6.267700,-2.305362,7.866117],[-3.580823,7.925673,6.380629,-0.460851],[-5.077899,-3.184179,4.276157,-8.432471],[-7.775817,-4.989772,-5.182207,2.967821],[-3.677893,-5.998180,8.212775,2.669258]],[[3.276094,9.432109,-7.248312,5.764643],[-4.027858,1.182344,-2.383843,5.699017],[-7.973001,4.354541,5.612521,6.264801],[-7.703499,-4.902042,9.852349,0.079987],[-2.099387,0.661493,-2.521978,8.526679]],[[-3.559521,-2.825363,5.581125,-9.854925],[9.815392,-6.238235,-3.604842,-2.936694],[-6.944751,-1.658287,-1.522286,-6.691561],[-8.400890,6.954421,-7.614973,-6.872934],[0.489686,-1.890226,-4.202146,-6.366415]],[[-8.502380,-3.541526,-3.890734,1.092388],[5.907353,-2.818782,5.682566,-4.330597],[-5.170631,-2.133982,0.443221,-9.691428],[4.218974,6.532926,4.082797,1.323467],[-3.369541,-9.721620,-3.004354,5.238057]],[[6.232437,2.985946,4.044221,-5.754467],[9.124535,-1.595989,5.836924,1.531705],[2.086641,1.308664,6.205219,-7.667555],[-5.409676,-9.192885,-4.135406,3.123837],[-3.098117,-2.618568,-1.144414,3.944221]],[[2.936827,-4.332736,-1.380672,1.954049],[-7.392160,-5.084826,3.055875,-1.800951],[1.067354,-3.414781,-8.087341,8.412292],[-5.361354,-8.820640,0.936485,-6.632434],[-7.101049,4.824930,3.873658,-4.266082]]], dtype = "float32")#candidate|1785|(12, 5, 4)|const|float32
bop_1786 = relay.maximum(uop_1760.astype('uint16'), const_1785.astype('uint16')) # shape=(12, 5, 4)
bop_1789 = relay.maximum(uop_1762.astype('uint16'), const_1785.astype('uint16')) # shape=(12, 5, 4)
uop_1791 = relay.sqrt(call_1753.astype('float64')) # shape=(1, 5, 4)
uop_1793 = relay.sqrt(call_1754.astype('float64')) # shape=(1, 5, 4)
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_1795 = relay.TupleGetItem(func_849_call(), 0)
call_1796 = relay.TupleGetItem(func_851_call(), 0)
bop_1800 = relay.not_equal(call_1795.astype('bool'), bop_1778.astype('bool')) # shape=(10, 5, 4)
bop_1803 = relay.not_equal(call_1796.astype('bool'), bop_1781.astype('bool')) # shape=(10, 5, 4)
uop_1807 = relay.log(const_1785.astype('float32')) # shape=(12, 5, 4)
output = relay.Tuple([call_1764,var_1765,bop_1786,uop_1791,bop_1800,uop_1807,])
output2 = relay.Tuple([call_1766,var_1765,bop_1789,uop_1793,bop_1803,uop_1807,])
func_1814 = relay.Function([var_1765,var_1767,], output)
mod['func_1814'] = func_1814
mod = relay.transform.InferType()(mod)
var_1815 = relay.var("var_1815", dtype = "float64", shape = (600,))#candidate|1815|(600,)|var|float64
var_1816 = relay.var("var_1816", dtype = "float32", shape = (10, 5, 4))#candidate|1816|(10, 5, 4)|var|float32
output = func_1814(var_1815,var_1816,)
func_1817 = relay.Function([var_1815,var_1816,], output)
mutated_mod['func_1817'] = func_1817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1586_call = mod.get_global_var('func_1586')
func_1588_call = mutated_mod.get_global_var('func_1588')
call_1849 = relay.TupleGetItem(func_1586_call(), 0)
call_1850 = relay.TupleGetItem(func_1588_call(), 0)
output = relay.Tuple([call_1849,])
output2 = relay.Tuple([call_1850,])
func_1851 = relay.Function([], output)
mod['func_1851'] = func_1851
mod = relay.transform.InferType()(mod)
output = func_1851()
func_1852 = relay.Function([], output)
mutated_mod['func_1852'] = func_1852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1858 = relay.TupleGetItem(func_1716_call(), 0)
call_1859 = relay.TupleGetItem(func_1717_call(), 0)
var_1867 = relay.var("var_1867", dtype = "uint64", shape = (12, 5, 4))#candidate|1867|(12, 5, 4)|var|uint64
bop_1868 = relay.left_shift(call_1858.astype('int16'), var_1867.astype('int16')) # shape=(12, 5, 4)
bop_1871 = relay.left_shift(call_1859.astype('int16'), var_1867.astype('int16')) # shape=(12, 5, 4)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1876 = relay.TupleGetItem(func_1716_call(), 0)
call_1877 = relay.TupleGetItem(func_1717_call(), 0)
uop_1885 = relay.atan(bop_1868.astype('float32')) # shape=(12, 5, 4)
uop_1887 = relay.atan(bop_1871.astype('float32')) # shape=(12, 5, 4)
output = relay.Tuple([call_1876,uop_1885,])
output2 = relay.Tuple([call_1877,uop_1887,])
func_1888 = relay.Function([var_1867,], output)
mod['func_1888'] = func_1888
mod = relay.transform.InferType()(mod)
mutated_mod['func_1888'] = func_1888
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1889 = relay.var("var_1889", dtype = "uint64", shape = (12, 5, 4))#candidate|1889|(12, 5, 4)|var|uint64
func_1888_call = mutated_mod.get_global_var('func_1888')
call_1890 = func_1888_call(var_1889)
output = call_1890
func_1891 = relay.Function([var_1889], output)
mutated_mod['func_1891'] = func_1891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mod.get_global_var('func_811')
func_812_call = mutated_mod.get_global_var('func_812')
call_1902 = func_811_call()
call_1903 = func_811_call()
uop_1906 = relay.acos(call_1902.astype('float64')) # shape=(1, 5, 4)
uop_1908 = relay.acos(call_1903.astype('float64')) # shape=(1, 5, 4)
bop_1910 = relay.bitwise_xor(uop_1906.astype('uint16'), relay.reshape(call_1902.astype('uint16'), relay.shape_of(uop_1906))) # shape=(1, 5, 4)
bop_1913 = relay.bitwise_xor(uop_1908.astype('uint16'), relay.reshape(call_1903.astype('uint16'), relay.shape_of(uop_1908))) # shape=(1, 5, 4)
output = bop_1910
output2 = bop_1913
func_1921 = relay.Function([], output)
mod['func_1921'] = func_1921
mod = relay.transform.InferType()(mod)
output = func_1921()
func_1922 = relay.Function([], output)
mutated_mod['func_1922'] = func_1922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1944 = relay.TupleGetItem(func_1716_call(), 1)
call_1945 = relay.TupleGetItem(func_1717_call(), 1)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1952 = relay.TupleGetItem(func_1716_call(), 1)
call_1953 = relay.TupleGetItem(func_1717_call(), 1)
output = relay.Tuple([call_1944,call_1952,])
output2 = relay.Tuple([call_1945,call_1953,])
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
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_2003 = func_1270_call()
call_2004 = func_1270_call()
func_1213_call = mod.get_global_var('func_1213')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_2010 = relay.TupleGetItem(func_1213_call(), 0)
call_2011 = relay.TupleGetItem(func_1215_call(), 0)
output = relay.Tuple([call_2003,call_2010,])
output2 = relay.Tuple([call_2004,call_2011,])
func_2031 = relay.Function([], output)
mod['func_2031'] = func_2031
mod = relay.transform.InferType()(mod)
mutated_mod['func_2031'] = func_2031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mutated_mod.get_global_var('func_2031')
call_2032 = func_2031_call()
output = call_2032
func_2033 = relay.Function([], output)
mutated_mod['func_2033'] = func_2033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_2034 = relay.TupleGetItem(func_928_call(), 0)
call_2035 = relay.TupleGetItem(func_929_call(), 0)
output = relay.Tuple([call_2034,])
output2 = relay.Tuple([call_2035,])
func_2037 = relay.Function([], output)
mod['func_2037'] = func_2037
mod = relay.transform.InferType()(mod)
output = func_2037()
func_2038 = relay.Function([], output)
mutated_mod['func_2038'] = func_2038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_2054 = relay.TupleGetItem(func_928_call(), 0)
call_2055 = relay.TupleGetItem(func_929_call(), 0)
output = call_2054
output2 = call_2055
func_2065 = relay.Function([], output)
mod['func_2065'] = func_2065
mod = relay.transform.InferType()(mod)
output = func_2065()
func_2066 = relay.Function([], output)
mutated_mod['func_2066'] = func_2066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_2079 = relay.TupleGetItem(func_1957_call(), 0)
call_2080 = relay.TupleGetItem(func_1959_call(), 0)
output = relay.Tuple([call_2079,])
output2 = relay.Tuple([call_2080,])
func_2085 = relay.Function([], output)
mod['func_2085'] = func_2085
mod = relay.transform.InferType()(mod)
output = func_2085()
func_2086 = relay.Function([], output)
mutated_mod['func_2086'] = func_2086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_2169 = relay.TupleGetItem(func_1597_call(), 0)
call_2170 = relay.TupleGetItem(func_1599_call(), 0)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_2190 = relay.TupleGetItem(func_1597_call(), 0)
call_2191 = relay.TupleGetItem(func_1599_call(), 0)
output = relay.Tuple([call_2169,call_2190,])
output2 = relay.Tuple([call_2170,call_2191,])
func_2197 = relay.Function([], output)
mod['func_2197'] = func_2197
mod = relay.transform.InferType()(mod)
output = func_2197()
func_2198 = relay.Function([], output)
mutated_mod['func_2198'] = func_2198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_2268 = relay.TupleGetItem(func_928_call(), 0)
call_2269 = relay.TupleGetItem(func_929_call(), 0)
var_2277 = relay.var("var_2277", dtype = "int8", shape = (4, 5, 4))#candidate|2277|(4, 5, 4)|var|int8
bop_2278 = relay.floor_divide(call_2268.astype('float32'), var_2277.astype('float32')) # shape=(4, 5, 4)
bop_2281 = relay.floor_divide(call_2269.astype('float32'), var_2277.astype('float32')) # shape=(4, 5, 4)
const_2287 = relay.const([[[-6,1,-3,4],[-5,-8,-3,5],[-6,10,-5,-9],[-1,8,-4,3],[-5,8,9,3]]], dtype = "int8")#candidate|2287|(1, 5, 4)|const|int8
bop_2288 = relay.less(call_2268.astype('bool'), relay.reshape(const_2287.astype('bool'), relay.shape_of(call_2268))) # shape=(1, 5, 4)
bop_2291 = relay.less(call_2269.astype('bool'), relay.reshape(const_2287.astype('bool'), relay.shape_of(call_2269))) # shape=(1, 5, 4)
output = relay.Tuple([bop_2278,bop_2288,])
output2 = relay.Tuple([bop_2281,bop_2291,])
func_2295 = relay.Function([var_2277,], output)
mod['func_2295'] = func_2295
mod = relay.transform.InferType()(mod)
var_2296 = relay.var("var_2296", dtype = "int8", shape = (4, 5, 4))#candidate|2296|(4, 5, 4)|var|int8
output = func_2295(var_2296)
func_2297 = relay.Function([var_2296], output)
mutated_mod['func_2297'] = func_2297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_2306 = relay.TupleGetItem(func_849_call(), 0)
call_2307 = relay.TupleGetItem(func_851_call(), 0)
output = relay.Tuple([call_2306,])
output2 = relay.Tuple([call_2307,])
func_2312 = relay.Function([], output)
mod['func_2312'] = func_2312
mod = relay.transform.InferType()(mod)
output = func_2312()
func_2313 = relay.Function([], output)
mutated_mod['func_2313'] = func_2313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_2322 = func_1126_call()
call_2323 = func_1126_call()
output = relay.Tuple([call_2322,])
output2 = relay.Tuple([call_2323,])
func_2336 = relay.Function([], output)
mod['func_2336'] = func_2336
mod = relay.transform.InferType()(mod)
mutated_mod['func_2336'] = func_2336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mutated_mod.get_global_var('func_2336')
call_2337 = func_2336_call()
output = call_2337
func_2338 = relay.Function([], output)
mutated_mod['func_2338'] = func_2338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1851_call = mod.get_global_var('func_1851')
func_1852_call = mutated_mod.get_global_var('func_1852')
call_2347 = relay.TupleGetItem(func_1851_call(), 0)
call_2348 = relay.TupleGetItem(func_1852_call(), 0)
output = call_2347
output2 = call_2348
func_2359 = relay.Function([], output)
mod['func_2359'] = func_2359
mod = relay.transform.InferType()(mod)
output = func_2359()
func_2360 = relay.Function([], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2402 = relay.var("var_2402", dtype = "float32", shape = (7, 7, 16))#candidate|2402|(7, 7, 16)|var|float32
uop_2403 = relay.sigmoid(var_2402.astype('float32')) # shape=(7, 7, 16)
output = relay.Tuple([uop_2403,])
output2 = relay.Tuple([uop_2403,])
func_2406 = relay.Function([var_2402,], output)
mod['func_2406'] = func_2406
mod = relay.transform.InferType()(mod)
var_2407 = relay.var("var_2407", dtype = "float32", shape = (7, 7, 16))#candidate|2407|(7, 7, 16)|var|float32
output = func_2406(var_2407)
func_2408 = relay.Function([var_2407], output)
mutated_mod['func_2408'] = func_2408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_2410 = relay.TupleGetItem(func_2031_call(), 1)
call_2411 = relay.TupleGetItem(func_2033_call(), 1)
func_2312_call = mod.get_global_var('func_2312')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_2416 = relay.TupleGetItem(func_2312_call(), 0)
call_2417 = relay.TupleGetItem(func_2313_call(), 0)
func_88_call = mod.get_global_var('func_88')
func_90_call = mutated_mod.get_global_var('func_90')
var_2423 = relay.var("var_2423", dtype = "float64", shape = (600,))#candidate|2423|(600,)|var|float64
call_2422 = relay.TupleGetItem(func_88_call(relay.reshape(var_2423.astype('float64'), [10, 5, 12])), 0)
call_2424 = relay.TupleGetItem(func_90_call(relay.reshape(var_2423.astype('float64'), [10, 5, 12])), 0)
output = relay.Tuple([call_2410,call_2416,call_2422,var_2423,])
output2 = relay.Tuple([call_2411,call_2417,call_2424,var_2423,])
func_2427 = relay.Function([var_2423,], output)
mod['func_2427'] = func_2427
mod = relay.transform.InferType()(mod)
mutated_mod['func_2427'] = func_2427
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2428 = relay.var("var_2428", dtype = "float64", shape = (600,))#candidate|2428|(600,)|var|float64
func_2427_call = mutated_mod.get_global_var('func_2427')
call_2429 = func_2427_call(var_2428)
output = call_2429
func_2430 = relay.Function([var_2428], output)
mutated_mod['func_2430'] = func_2430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1213_call = mod.get_global_var('func_1213')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_2432 = relay.TupleGetItem(func_1213_call(), 0)
call_2433 = relay.TupleGetItem(func_1215_call(), 0)
const_2453 = relay.const([[[7.366142,-9.191232,-6.668955,-9.268923],[6.365249,3.693492,1.780459,3.696643],[7.143634,0.760265,-0.054237,-4.566679],[6.545146,4.687159,9.633950,0.710298],[8.091319,7.178992,-8.068020,-6.443090]],[[-4.431600,3.630259,-6.706812,9.699488],[-0.088816,2.931379,1.652656,-1.847872],[1.415612,-4.887187,-8.497049,1.309711],[3.755420,0.120363,7.280390,9.789298],[2.827159,2.356723,6.513573,3.992143]],[[-0.478596,0.793455,1.324326,-0.737923],[1.863816,2.763303,-0.441661,4.796412],[-3.621222,6.371102,5.947333,5.121491],[3.040288,-1.287635,6.266311,-8.906263],[-1.369585,8.450293,-5.005455,-2.926192]],[[-4.558615,8.983166,-3.525331,-5.417186],[-7.959209,-7.029125,-9.581617,-5.278238],[5.735937,2.964423,3.636348,-9.384428],[2.862075,9.421439,0.738367,0.763930],[0.047608,-4.012291,2.713087,-0.615699]],[[-6.841231,9.190327,-8.801151,-8.245992],[-1.138238,-4.224523,3.478410,0.958576],[-1.965887,-2.154733,-0.175700,9.827058],[4.046045,-1.391237,-7.804577,-4.985733],[0.087960,-6.011286,0.846942,3.445878]],[[-5.887490,0.170140,-9.515719,-9.061719],[3.960645,-5.020544,-2.673733,-5.221038],[8.185455,-6.349219,0.222910,-9.616892],[9.878791,2.992625,0.437949,-9.963033],[-7.108471,-0.059424,6.887724,-6.761142]],[[8.128891,-9.520988,-8.995925,9.142361],[6.057288,-6.338671,-6.124544,-0.486159],[3.436555,7.597654,-2.007856,-4.635234],[6.961682,-0.666236,9.972522,-3.581042],[9.771025,-9.687004,5.223318,-4.047777]],[[9.978587,4.571490,3.458652,4.747522],[9.103103,-3.596303,7.998078,3.719667],[5.609744,2.748219,-8.389034,0.090078],[-4.488301,8.090789,-5.375282,4.549225],[-5.524916,0.986148,-0.185979,-7.134962]],[[8.292897,6.117691,6.927822,-3.791877],[-4.538154,5.558800,7.818781,7.152376],[-9.355930,0.722056,-0.100079,3.748755],[6.499615,-5.371503,8.913186,-2.554017],[3.604306,6.728321,-7.411701,5.160083]],[[6.818903,3.839037,-0.056503,3.764683],[0.510133,5.792237,5.464726,6.924098],[7.719361,-5.887432,-7.711581,-6.425904],[-5.450821,3.049146,9.629086,-7.963572],[8.449152,3.093858,-4.262591,5.029452]],[[6.620246,4.027916,4.170862,7.573133],[-7.489460,0.327617,-1.779024,7.228292],[-9.596503,9.427800,2.361676,-2.153858],[3.235144,-4.275286,-4.477839,-6.226423],[-8.956358,-3.905997,-2.702341,0.674426]],[[5.002660,3.265625,-0.020337,9.534372],[9.610874,-9.222869,-0.704930,-1.491008],[-1.116613,1.240354,-7.116319,-9.069637],[0.735555,-1.687034,-8.218125,-4.380714],[-3.648822,-3.129251,-3.425833,6.625583]],[[-5.903977,8.907301,5.884743,9.061222],[-5.090022,-4.194858,-1.208818,-3.653914],[-4.671059,3.974672,-4.042772,-4.990341],[1.797005,7.973083,-1.498446,-0.859091],[-2.145421,9.889456,4.090698,1.788041]],[[5.949850,-7.647866,-6.065587,5.077003],[2.363208,4.472101,6.301062,-0.940102],[-3.949950,-9.052814,9.284756,-0.180405],[-3.487294,4.043200,-9.910786,-9.991645],[-1.165792,5.396690,3.208570,3.660722]],[[4.380526,-0.361734,7.793756,9.350066],[-8.047508,-8.625251,-2.484890,4.189319],[1.474935,-3.889935,8.304858,6.711974],[2.203972,-5.231653,-6.022757,7.376606],[-4.527854,-0.642384,4.319104,-2.024973]],[[4.730821,7.872718,3.412864,8.707405],[8.432141,-4.639762,-1.176095,-7.521813],[-8.783512,-7.509940,9.100101,-6.637939],[9.562843,6.109452,-2.170735,-0.508562],[-9.252182,-6.650031,-5.536184,-8.896990]]], dtype = "float32")#candidate|2453|(16, 5, 4)|const|float32
bop_2454 = relay.left_shift(call_2432.astype('uint16'), const_2453.astype('uint16')) # shape=(16, 5, 4)
bop_2457 = relay.left_shift(call_2433.astype('uint16'), const_2453.astype('uint16')) # shape=(16, 5, 4)
bop_2459 = relay.mod(const_2453.astype('float32'), call_2432.astype('float32')) # shape=(16, 5, 4)
bop_2462 = relay.mod(const_2453.astype('float32'), call_2433.astype('float32')) # shape=(16, 5, 4)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
const_2468 = relay.const([8.646961,-1.072185,-6.551666,-6.706358,-0.016069,-3.269917,-6.922498,1.828400,-9.083742,-8.278779,9.464971,7.139548,7.537040,-7.705969,-0.622574,-8.502273,2.754537,8.781385,5.048315,-5.307887,-3.010119,2.192509,9.802845,2.103898,5.047741,-6.679314,8.426298,1.893604,-4.382610,-6.539366,2.513043,-6.442192,4.585864,-5.614220,3.198182,-3.758484,9.515080,-8.160827,8.011159,7.033219,1.519352,1.036050,8.930097,3.597915,-2.516684,-0.877591,0.783033,5.183632,-3.141971,0.244891,-9.348520,-9.933003,6.386275,0.880840,-3.838383,1.449138,-0.876466,0.194267,-4.009121,7.799150,-9.663439,-8.035852,-8.876171,-1.416948,7.068677,-3.205061,-1.693194,-2.503958,4.963437,-5.294246,-4.371093,2.977687,-6.007831,-2.419345,-2.167939,9.342664,1.998620,-2.101922,6.968137,5.468714,-2.836565,3.833452,-4.897169,-5.154166,9.120838,0.988057,6.855669,-4.114366,5.521071,-5.551522,-0.676992,-6.824300,0.020262,4.181871,-2.030618,3.650142,-3.283716,9.837177,-3.930749,-1.039850,-7.612991,8.979617,-3.587755,8.820412,-9.674769,2.624908,8.675757,4.074855,-4.971529,-6.317908,9.625501,6.432589,-0.052968,-2.597150,4.400651,-8.609710,-0.815757,3.707740,5.842905,4.260613,-7.008317,-7.483374,-6.377549,-5.282060,-4.854744,3.393506,-6.835092,0.643750,5.670648,-8.299167,-0.893765,-2.997340,-7.789660,2.789419,-2.033291,-3.631281,-3.775851,4.467923,-6.869410,5.208027,-2.373767,-6.284114,-0.797104,8.483260,2.365009,-9.233861,-3.609298,-6.198312,-9.144963,-6.172089,-4.745189,6.177018,7.754011,-3.123471,-8.552678,-3.721645,-3.553556,3.451973,-4.477853,3.046365,-4.016458,9.280374,-5.057959,-9.007433,3.316032,-1.375163,5.014817,-4.401228,-1.404495,-4.227547,8.454946,5.186855,8.298418,-1.922997,5.531367,6.589746,7.657894,-8.209574,-2.837814,-7.981157,8.327631,-5.527288,-0.681275,4.102080,7.915166,5.525272,-1.109184,-3.659788,1.785468,3.975105,-6.092554,2.105979,2.811384,-1.867438,-5.629351,3.893818,4.901512,-7.186618,5.570356,-4.672700,8.969132,3.042666,-4.495451,5.371944,-7.313186,-2.867400,1.984087,-0.403652,3.293837,-0.218407,5.452873,4.664249,9.292728,-9.126500,3.667604,4.936904,-3.078322,-6.349300,9.698546,-6.765020,-6.538898,-5.895603,-2.473010,-1.040620,5.897183,3.033642,-0.666352,5.826141,-4.313352,-9.952432,-4.689954,-9.240020,-3.637566,5.426177,-7.897010,9.276496,-0.034519,-8.735151,-7.136906,-7.692291,-6.643884,-6.080874,-8.013739,-1.112446,0.403678,-4.925377,4.184196,-7.894827,3.226349,3.591190,-3.524170,-8.039755,-0.959248,6.035378,6.993250,0.372202,-4.959483,3.928406,5.926975,5.985134,-3.293097,0.648310,7.662464,-9.305619,6.779797,-6.044320,-7.979290,5.955152,-1.997827,-7.317927,-5.849910,0.014674,4.197349,-8.926971,-5.619813,-1.470136,9.835320,-7.205090,0.211740,-6.394842,-6.582352,-8.100665,4.006125,-2.757539,3.925177,-6.910035,-4.780624,-3.328523,-4.227800,-4.952529,-0.650379,3.581883,-2.974947,-7.297109,-6.385160,8.783826,-9.065886,-8.912429,5.853891,5.701852,3.899687,-7.266133,5.546122,1.821048,5.311233,-7.555104,-3.880163,-6.732240,-4.989784,8.444154,4.412207,0.721464,-9.450782,0.597157,-2.225937,-4.040269,-6.903883,0.135338,3.048297,9.536841,0.207094,6.348564,-4.935187,-9.276174,-0.940936,0.482256,-7.327481,9.079111,-5.522611,-0.970115,0.132358,-5.193821,-1.137568,2.708065,2.218913,-3.605233,6.240478,-3.602622,2.168136,-7.587837,-3.767811,5.499886,-8.120159,-6.183218,-8.215356,-7.909210,9.675733,4.190664,-2.502680,-0.490383,-3.230557,-0.888076,-7.251922,4.336059,-8.148209,6.948617,1.250777,6.187157,-4.685711,4.888836,6.550730,-7.758188,-0.639576,-1.468551,6.127436,-8.402641,0.965503,6.247613,-8.474462,-3.526290,-1.245492,1.616270,-8.659587,4.657174,-9.137782,2.137542,-8.821712,8.436307,-4.142143,-1.511800,-1.339021,4.282387,9.967645,8.716380,2.278020,-0.105043,4.025803,1.445525,4.761483,-5.812043,2.493753,9.429693,-4.729463,4.298474,-1.580502,-7.492108,-8.930452,-1.869020,-2.446982,5.697608,4.157360,6.468733,-3.428234,0.194899,2.503819,9.341053,6.122282,6.718916,2.971098,-8.048892,-8.231705,-9.626192,-2.348520,-5.327043,-6.648346,-6.656940,-1.450761,7.968901,9.045737,-4.578749,-7.454126,3.345263,-3.774540,2.670395,2.244004,8.187770,-0.835258,3.427563,-8.078216,6.042353,1.052292,5.073710,9.848652,-6.408601,2.671652,-9.529183,8.145930,9.798188,-9.663877,7.111814,5.640074,0.320379,2.081843,-8.268235,-9.921203,-3.868214,-4.768327,7.839837,-6.326952,-0.288736,-1.546736,-1.099621,-5.770130,3.915851,-9.981244,0.900144,0.571484,-9.439837,6.262075,8.997971,-4.893208,9.600297,2.051270,7.735025,9.887167,3.012418,-4.737136,0.338718,9.709749,5.363176,2.792650,8.638879,8.755337,0.167938,8.086951,-6.032640,5.871260,-0.820633,9.554594,-0.052307,1.808953,-4.815705,7.373424,-8.055255,2.022680,2.395548,-9.626940,0.151668,-1.225993,-6.813316,7.238280,1.292945,0.414351,6.839196,1.565955,8.406469,1.964210,-6.013428,2.400950,-9.231903,-8.211030,1.433693,-3.045031,-0.660368,-9.326277,-2.998111,-9.913386,-3.543328,8.314733,-7.015189,3.953022,7.896729,6.264481,-5.126231,3.160339,8.781224,-5.132764,-9.802253,-3.231713,8.118814,-1.898495,-5.566162,1.661999,-7.534441,1.748976,-6.262861,-4.344591,5.638719,8.435905,-6.866878,-8.808944,1.120709,-0.313451,-5.007336,-4.398466,6.286381,9.666604,8.816872,-7.201205,-0.539121,-9.491024,0.701718,-2.313647,0.118438,-8.665428,-9.020277,3.648916,7.617366,-5.312822,-2.208561,9.759070,1.851969,-5.421764,8.330826,-6.033324,-4.674343,-5.652415,9.757227,-0.855984,1.021537,-7.393151,-2.019893,7.205058,3.168386,4.841719,-8.382572,-5.181544,6.188321,6.853051,2.780845,-3.203969,-2.652254,4.331488,-7.511390,-6.003899,-4.943375,3.873286,8.814678,-6.499786,-0.678823,-8.464599,-1.910461,-7.135997,4.755000,2.420513,2.882883,-6.080197,-5.540412,6.499582,-3.883486,-8.712776,-5.429521,7.364202,-9.469810,3.247832,4.372757,-7.629794,-7.755493,4.220842,-4.159613,-4.190774,6.802393,3.729897,9.204364,-3.353396,3.307188,-1.992426,-9.894142,2.577944,-0.209510,-9.697535,-7.736995,7.602339,8.584254,5.877179,4.432334,-4.897929,-6.907627,2.021037,-8.117106,4.875287,-5.164766,-6.692296,1.054378,-7.404288,-6.218355,9.299329,5.857876,1.870937,-7.632985,-7.939727,-0.838272,-6.876771,-7.782146,-2.270016,6.473584,-2.141583,-8.939028,-0.216127,-8.993240,8.069803,8.300645,-7.005301,8.914268,-6.499567,-1.189406,-9.736245,1.874869,5.042296,-9.558189,-9.665153,-6.024543,2.681888,3.532324,-4.947606,-3.960818,-1.924479,1.264943,-4.981820,-1.348427,-4.554609,8.913117,-5.569999,7.566941,0.319380,8.482313,1.929152,-5.036518,-9.049705,-9.594536,-1.626297,-0.569138,0.428201,7.748668,8.669453,-4.766253,-3.525420,-2.311243,-2.645409,-6.977901,1.558671,4.694424,8.030841,1.186483,-8.567191,1.098640,0.661454,0.127332,8.783946,-8.829443,8.180523,-0.082014,0.554098,-2.302104,-5.198593,7.362320,-1.383919,-4.897725,-4.777313,-4.167453,9.565295,8.989896,2.150941,9.904856,6.742086,0.951637,-4.969344,-1.087859,-6.613096,6.722379,-3.387609,-9.114727,-7.538576,-8.606059,8.957156,9.899184,-7.073137,0.767923,1.973940,-4.704784,-4.765114,2.461844,9.704150,-6.353360,-4.268561,-9.184755,-9.074327,-2.528665,3.534202,-9.969023,2.692594,-0.196512,-8.884328,4.649255,-1.083981,4.278998,-7.653153,-5.465417,-6.076219,7.844439,-2.340966,7.739808,6.437286,4.115495,0.305571,7.855924,4.282365,-5.383235,2.186828,-7.441392,-2.155944,-2.276728,-3.589361,-3.477723,-3.749033,-5.530920,-5.037246,9.925314,0.469080,-9.746144,-1.341343,6.552941,9.488764,-0.612934,2.088228,3.183639,-5.059898,-2.586005,-1.254177,2.738922,2.682206,2.922128,-1.352380,9.433169,-4.765113,-1.689791,5.218678,-7.735952,3.762507,3.942163,2.555321,-0.585342,-9.026837,0.289667], dtype = "float32")#candidate|2468|(784,)|const|float32
call_2467 = relay.TupleGetItem(func_2406_call(relay.reshape(const_2468.astype('float32'), [7, 7, 16])), 0)
call_2469 = relay.TupleGetItem(func_2408_call(relay.reshape(const_2468.astype('float32'), [7, 7, 16])), 0)
bop_2486 = relay.not_equal(bop_2454.astype('bool'), call_2432.astype('bool')) # shape=(16, 5, 4)
bop_2489 = relay.not_equal(bop_2457.astype('bool'), call_2433.astype('bool')) # shape=(16, 5, 4)
output = relay.Tuple([bop_2459,call_2467,const_2468,bop_2486,])
output2 = relay.Tuple([bop_2462,call_2469,const_2468,bop_2489,])
func_2494 = relay.Function([], output)
mod['func_2494'] = func_2494
mod = relay.transform.InferType()(mod)
output = func_2494()
func_2495 = relay.Function([], output)
mutated_mod['func_2495'] = func_2495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_2522 = relay.TupleGetItem(func_1716_call(), 0)
call_2523 = relay.TupleGetItem(func_1717_call(), 0)
output = call_2522
output2 = call_2523
func_2524 = relay.Function([], output)
mod['func_2524'] = func_2524
mod = relay.transform.InferType()(mod)
output = func_2524()
func_2525 = relay.Function([], output)
mutated_mod['func_2525'] = func_2525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_2537 = relay.TupleGetItem(func_849_call(), 0)
call_2538 = relay.TupleGetItem(func_851_call(), 0)
var_2541 = relay.var("var_2541", dtype = "int8", shape = (13, 5, 4))#candidate|2541|(13, 5, 4)|var|int8
bop_2542 = relay.equal(call_2537.astype('bool'), var_2541.astype('bool')) # shape=(13, 5, 4)
bop_2545 = relay.equal(call_2538.astype('bool'), var_2541.astype('bool')) # shape=(13, 5, 4)
func_567_call = mod.get_global_var('func_567')
func_571_call = mutated_mod.get_global_var('func_571')
const_2550 = relay.const([[2.165072,2.717374,-6.835761,-4.226482,-4.988684,2.317725,2.340029,1.454228,-2.259262,7.704095,-0.527153,-4.730167,-1.690897,-5.450107,6.342976,-0.201401,-1.473239,7.976320,-0.636105,-4.222030,-0.357102,7.081600,0.941048,-9.566204,-8.412989,-7.877739,3.631712,6.353298,-7.481768,-1.507839,7.147869,-3.867410,0.506781,3.637207,-2.962175,-0.682089,0.502376,-2.441818,9.946135,0.827532,7.232644,-0.506550,-6.570143,-8.627579,3.200392,-4.287081,-4.738856,2.138516,-4.905975,3.895513,-8.442696,-2.269247,3.911361,5.311103,3.386380,5.417149,-3.427184,-4.667314,2.289386,3.678896,8.737924,0.631615,3.557346,9.705569,4.665254,-9.269571,7.792468,-5.641509,7.006619,5.760725,-8.438097,0.527094,-5.908778,4.486139,3.167447,-9.015040,-5.191684,-2.035691,-8.048400,-3.329028,-6.203382,-3.140194,2.634942,-3.640879,-2.677089,5.909491,-5.771206,9.714156]], dtype = "float32")#candidate|2550|(1, 88)|const|float32
var_2551 = relay.var("var_2551", dtype = "float64", shape = (12,))#candidate|2551|(12,)|var|float64
call_2549 = relay.TupleGetItem(func_567_call(relay.reshape(const_2550.astype('float32'), [1, 8, 11]), relay.reshape(var_2551.astype('float64'), [12,]), ), 0)
call_2552 = relay.TupleGetItem(func_571_call(relay.reshape(const_2550.astype('float32'), [1, 8, 11]), relay.reshape(var_2551.astype('float64'), [12,]), ), 0)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_2554 = relay.TupleGetItem(func_1716_call(), 0)
call_2555 = relay.TupleGetItem(func_1717_call(), 0)
uop_2561 = relay.cosh(call_2549.astype('float32')) # shape=(1, 8, 11)
uop_2563 = relay.cosh(call_2552.astype('float32')) # shape=(1, 8, 11)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_2564 = relay.TupleGetItem(func_1431_call(), 0)
call_2565 = relay.TupleGetItem(func_1433_call(), 0)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_2582 = relay.TupleGetItem(func_1957_call(), 0)
call_2583 = relay.TupleGetItem(func_1959_call(), 0)
output = relay.Tuple([bop_2542,const_2550,var_2551,call_2554,uop_2561,call_2564,call_2582,])
output2 = relay.Tuple([bop_2545,const_2550,var_2551,call_2555,uop_2563,call_2565,call_2583,])
func_2605 = relay.Function([var_2541,var_2551,], output)
mod['func_2605'] = func_2605
mod = relay.transform.InferType()(mod)
var_2606 = relay.var("var_2606", dtype = "int8", shape = (13, 5, 4))#candidate|2606|(13, 5, 4)|var|int8
var_2607 = relay.var("var_2607", dtype = "float64", shape = (12,))#candidate|2607|(12,)|var|float64
output = func_2605(var_2606,var_2607,)
func_2608 = relay.Function([var_2606,var_2607,], output)
mutated_mod['func_2608'] = func_2608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1851_call = mod.get_global_var('func_1851')
func_1852_call = mutated_mod.get_global_var('func_1852')
call_2623 = relay.TupleGetItem(func_1851_call(), 0)
call_2624 = relay.TupleGetItem(func_1852_call(), 0)
output = call_2623
output2 = call_2624
func_2635 = relay.Function([], output)
mod['func_2635'] = func_2635
mod = relay.transform.InferType()(mod)
mutated_mod['func_2635'] = func_2635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2635_call = mutated_mod.get_global_var('func_2635')
call_2636 = func_2635_call()
output = call_2636
func_2637 = relay.Function([], output)
mutated_mod['func_2637'] = func_2637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2336_call = mod.get_global_var('func_2336')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_2671 = relay.TupleGetItem(func_2336_call(), 0)
call_2672 = relay.TupleGetItem(func_2338_call(), 0)
output = relay.Tuple([call_2671,])
output2 = relay.Tuple([call_2672,])
func_2682 = relay.Function([], output)
mod['func_2682'] = func_2682
mod = relay.transform.InferType()(mod)
mutated_mod['func_2682'] = func_2682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2682_call = mutated_mod.get_global_var('func_2682')
call_2683 = func_2682_call()
output = call_2683
func_2684 = relay.Function([], output)
mutated_mod['func_2684'] = func_2684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2085_call = mod.get_global_var('func_2085')
func_2086_call = mutated_mod.get_global_var('func_2086')
call_2746 = relay.TupleGetItem(func_2085_call(), 0)
call_2747 = relay.TupleGetItem(func_2086_call(), 0)
output = relay.Tuple([call_2746,])
output2 = relay.Tuple([call_2747,])
func_2757 = relay.Function([], output)
mod['func_2757'] = func_2757
mod = relay.transform.InferType()(mod)
output = func_2757()
func_2758 = relay.Function([], output)
mutated_mod['func_2758'] = func_2758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_2782 = relay.TupleGetItem(func_928_call(), 0)
call_2783 = relay.TupleGetItem(func_929_call(), 0)
func_2295_call = mod.get_global_var('func_2295')
func_2297_call = mutated_mod.get_global_var('func_2297')
const_2799 = relay.const([-6,-9,-5,3,-8,4,5,10,3,-2,10,7,4,-6,-6,3,-3,3,7,-9,-10,-8,5,10,-5,-8,10,7,-9,-6,-1,-7,1,2,7,-6,6,-3,-3,-8,-7,-1,2,-10,2,3,7,6,1,10,9,4,-10,-6,-2,-1,-1,-8,10,-1,6,-6,4,-2,1,-3,-8,8,6,10,8,-8,4,9,6,8,4,4,7,-4], dtype = "int8")#candidate|2799|(80,)|const|int8
call_2798 = relay.TupleGetItem(func_2295_call(relay.reshape(const_2799.astype('int8'), [4, 5, 4])), 1)
call_2800 = relay.TupleGetItem(func_2297_call(relay.reshape(const_2799.astype('int8'), [4, 5, 4])), 1)
output = relay.Tuple([call_2782,call_2798,const_2799,])
output2 = relay.Tuple([call_2783,call_2800,const_2799,])
func_2808 = relay.Function([], output)
mod['func_2808'] = func_2808
mod = relay.transform.InferType()(mod)
mutated_mod['func_2808'] = func_2808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2808_call = mutated_mod.get_global_var('func_2808')
call_2809 = func_2808_call()
output = call_2809
func_2810 = relay.Function([], output)
mutated_mod['func_2810'] = func_2810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_2831 = relay.TupleGetItem(func_1397_call(), 1)
call_2832 = relay.TupleGetItem(func_1399_call(), 1)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_2846 = relay.TupleGetItem(func_1716_call(), 0)
call_2847 = relay.TupleGetItem(func_1717_call(), 0)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_2857 = relay.TupleGetItem(func_1597_call(), 0)
call_2858 = relay.TupleGetItem(func_1599_call(), 0)
func_1126_call = mod.get_global_var('func_1126')
func_1127_call = mutated_mod.get_global_var('func_1127')
call_2875 = func_1126_call()
call_2876 = func_1126_call()
output = relay.Tuple([call_2831,call_2846,call_2857,call_2875,])
output2 = relay.Tuple([call_2832,call_2847,call_2858,call_2876,])
func_2885 = relay.Function([], output)
mod['func_2885'] = func_2885
mod = relay.transform.InferType()(mod)
mutated_mod['func_2885'] = func_2885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2885_call = mutated_mod.get_global_var('func_2885')
call_2886 = func_2885_call()
output = call_2886
func_2887 = relay.Function([], output)
mutated_mod['func_2887'] = func_2887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_2902 = relay.TupleGetItem(func_849_call(), 0)
call_2903 = relay.TupleGetItem(func_851_call(), 0)
func_2494_call = mod.get_global_var('func_2494')
func_2495_call = mutated_mod.get_global_var('func_2495')
call_2906 = relay.TupleGetItem(func_2494_call(), 0)
call_2907 = relay.TupleGetItem(func_2495_call(), 0)
output = relay.Tuple([call_2902,call_2906,])
output2 = relay.Tuple([call_2903,call_2907,])
func_2921 = relay.Function([], output)
mod['func_2921'] = func_2921
mod = relay.transform.InferType()(mod)
output = func_2921()
func_2922 = relay.Function([], output)
mutated_mod['func_2922'] = func_2922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1851_call = mod.get_global_var('func_1851')
func_1852_call = mutated_mod.get_global_var('func_1852')
call_2937 = relay.TupleGetItem(func_1851_call(), 0)
call_2938 = relay.TupleGetItem(func_1852_call(), 0)
output = relay.Tuple([call_2937,])
output2 = relay.Tuple([call_2938,])
func_2944 = relay.Function([], output)
mod['func_2944'] = func_2944
mod = relay.transform.InferType()(mod)
output = func_2944()
func_2945 = relay.Function([], output)
mutated_mod['func_2945'] = func_2945
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2954 = relay.var("var_2954", dtype = "float64", shape = (13, 5, 2))#candidate|2954|(13, 5, 2)|var|float64
var_2955 = relay.var("var_2955", dtype = "float64", shape = (13, 5, 2))#candidate|2955|(13, 5, 2)|var|float64
bop_2956 = relay.maximum(var_2954.astype('float64'), relay.reshape(var_2955.astype('float64'), relay.shape_of(var_2954))) # shape=(13, 5, 2)
bop_2960 = relay.less(var_2955.astype('bool'), relay.reshape(bop_2956.astype('bool'), relay.shape_of(var_2955))) # shape=(13, 5, 2)
output = relay.Tuple([bop_2960,])
output2 = relay.Tuple([bop_2960,])
func_2966 = relay.Function([var_2954,var_2955,], output)
mod['func_2966'] = func_2966
mod = relay.transform.InferType()(mod)
mutated_mod['func_2966'] = func_2966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2966_call = mutated_mod.get_global_var('func_2966')
var_2968 = relay.var("var_2968", dtype = "float64", shape = (13, 5, 2))#candidate|2968|(13, 5, 2)|var|float64
var_2969 = relay.var("var_2969", dtype = "float64", shape = (13, 5, 2))#candidate|2969|(13, 5, 2)|var|float64
call_2967 = func_2966_call(var_2968,var_2969,)
output = call_2967
func_2970 = relay.Function([var_2968,var_2969,], output)
mutated_mod['func_2970'] = func_2970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_3017 = relay.TupleGetItem(func_1716_call(), 1)
call_3018 = relay.TupleGetItem(func_1717_call(), 1)
output = relay.Tuple([call_3017,])
output2 = relay.Tuple([call_3018,])
func_3037 = relay.Function([], output)
mod['func_3037'] = func_3037
mod = relay.transform.InferType()(mod)
output = func_3037()
func_3038 = relay.Function([], output)
mutated_mod['func_3038'] = func_3038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mod.get_global_var('func_2494')
func_2495_call = mutated_mod.get_global_var('func_2495')
call_3065 = relay.TupleGetItem(func_2494_call(), 3)
call_3066 = relay.TupleGetItem(func_2495_call(), 3)
func_88_call = mod.get_global_var('func_88')
func_90_call = mutated_mod.get_global_var('func_90')
const_3088 = relay.const([[8.581913,-8.059460],[-5.151850,7.947803],[-4.330304,-4.387963],[-1.317936,5.150641],[6.914119,-1.392965],[-8.912890,5.477937],[-4.039960,5.119214],[1.209742,-5.156865],[-7.238779,7.553203],[2.655390,-6.254604],[-7.335283,-7.242066],[7.165801,3.702463],[0.073888,-4.740775],[4.097727,6.631725],[-1.301131,2.006981],[-6.564005,-8.193969],[-9.206416,6.342512],[-1.913898,6.238461],[-0.904798,5.276552],[-7.324499,1.979274],[-8.909136,6.906808],[4.107395,1.793843],[9.586905,9.895045],[-8.881628,6.054926],[4.636837,3.886740],[-2.016534,8.240784],[-3.777327,-2.301602],[3.627195,-0.189055],[1.769729,7.991890],[-0.664791,-8.069029],[8.186754,6.021656],[8.484481,-6.505452],[-0.539723,-0.322453],[9.078310,7.812725],[-6.809259,-2.234567],[4.396619,1.145584],[-7.787844,-4.895746],[6.116285,-3.836266],[-7.867385,-3.888801],[-8.735036,2.909656],[-7.939033,3.952535],[3.694149,9.696283],[-3.197122,2.214888],[1.436923,-2.292611],[6.559885,-9.399189],[9.772693,-7.169213],[6.457983,8.928127],[2.876065,-2.180844],[-0.460110,7.088681],[-6.525768,2.457490],[-6.181801,8.048751],[3.488076,4.984227],[-6.854519,0.852781],[8.989567,0.308699],[3.198464,-2.553828],[2.863061,-7.810010],[0.311483,1.649269],[3.263672,-0.540237],[5.384416,8.853923],[-9.664370,-4.745310],[-2.315773,-9.384891],[1.211965,-0.211735],[2.589236,8.465950],[8.742832,-4.024639],[-1.593407,0.619830],[6.109772,1.347847],[8.256857,0.616608],[-0.383402,-7.941658],[-4.584363,-9.778823],[-1.607553,-4.954488],[5.470567,9.542387],[0.761115,3.437630],[1.141980,4.430231],[4.476442,-8.039157],[1.070299,-0.825920],[1.086056,9.050443],[4.463756,0.161245],[-8.421219,4.058296],[9.574353,2.359724],[4.056263,-6.840537],[6.776318,8.341876],[7.203744,1.398962],[0.776365,-8.969542],[-6.854184,-3.353966],[7.757179,1.386173],[1.535761,8.345507],[1.939724,-8.907802],[-1.980725,-8.052714],[-3.985573,-2.319002],[9.039474,6.033158],[8.528429,9.104635],[9.479361,7.481127],[6.477661,-4.163649],[-6.806827,4.440429],[-7.006096,-7.632945],[4.783103,-0.138005],[-0.348029,2.257921],[-6.356061,-2.614760],[-7.151948,7.684688],[-6.866510,-4.357400],[-1.316620,-3.258329],[-5.693968,-0.283407],[9.758212,0.320815],[7.697203,6.102459],[-2.868017,6.657403],[7.652309,-8.704747],[7.486903,8.325652],[0.277054,5.710041],[-6.464985,-2.527457],[-1.953505,-7.488566],[7.669335,-8.302461],[0.491949,-3.509913],[-3.133387,1.683172],[8.048457,7.731714],[7.252074,-0.828382],[-7.016510,-0.337905],[-8.554835,4.419977],[-0.053802,-2.368599],[-5.668771,-8.668353],[-1.458053,8.700854],[8.238786,-9.125465],[4.325550,6.833364],[-7.284374,0.954993],[-6.424981,-8.469203],[-6.659674,6.052360],[6.856068,-3.680249],[-7.123064,1.855197],[3.817144,1.704497],[6.386956,6.725618],[6.465908,-0.525567],[1.028609,-1.556333],[4.729613,-4.897280],[-1.582697,-7.721505],[4.640212,4.676414],[-4.209556,1.690714],[-6.379579,-6.000637],[-9.040260,-0.807583],[-8.784833,-0.478947],[-2.588012,8.111796],[0.007530,2.649104],[7.900047,1.760003],[-7.358425,-9.574453],[8.727079,-5.006618],[-3.983117,-3.273064],[-5.301733,-8.725365],[2.395444,-1.671381],[0.865184,0.369069],[2.887103,1.097215],[2.511622,-0.555235],[3.948824,-5.044767],[-7.905907,-6.520296],[4.186149,2.062363],[6.423380,-4.147617],[-2.052837,-2.662166],[2.073089,-1.045342],[-5.137273,5.326587],[-9.966752,0.093071],[0.984631,5.168862],[-2.517014,-8.139097],[-1.051565,-3.578439],[-6.398934,-0.327670],[6.421660,-3.671653],[-0.719341,-7.075423],[-3.873254,-0.358363],[9.668981,4.972777],[8.489179,-7.816795],[-6.396908,3.523042],[-3.611696,4.285471],[5.980830,-7.374934],[-4.749993,2.978195],[5.655709,-6.545475],[0.004347,5.281363],[-2.959968,8.518896],[1.263518,-7.810448],[4.077348,-3.037860],[7.689512,-3.612088],[4.466526,0.244265],[0.460610,-0.471303],[-7.394822,8.160908],[-9.021103,-0.252962],[2.437475,-3.006598],[4.490812,-0.685960],[2.423710,7.478105],[-7.873310,7.928840],[-5.601961,-9.069494],[1.102940,-5.754961],[3.824589,2.602755],[-4.509401,-4.995163],[-8.347475,-9.252282],[0.724895,-4.759279],[3.882753,9.151490],[0.721703,5.851776],[-4.464131,8.151581],[5.562372,1.850627],[7.339780,-0.585558],[6.583125,3.629847],[2.012248,1.477494],[1.102031,3.950856],[4.968168,-1.995683],[3.643555,-1.077422],[0.132912,5.745980],[-7.745993,0.211815],[-4.958523,0.954491],[4.378266,0.786376],[1.648328,5.368631],[-3.604579,9.378435],[-8.944585,-6.791396],[-6.281182,4.493854],[-6.611305,-6.361619],[0.883038,9.675837],[0.861330,4.313224],[8.541928,8.103424],[-6.012421,5.220518],[-0.186869,-8.531508],[6.109506,-5.185343],[-8.612044,0.404132],[6.095329,1.798562],[-0.264945,-2.422881],[1.381778,-0.198325],[-7.232068,3.078741],[-9.765328,9.741387],[-5.476721,0.143200],[-0.347999,3.931637],[3.825066,0.765235],[-4.101601,-6.613987],[8.332809,-5.486422],[-5.013561,-6.073424],[-5.225743,1.313388],[-9.084689,3.774974],[7.208097,-3.910600],[5.121695,-4.918266],[2.853060,4.471809],[-2.628579,-8.027642],[-1.604355,-4.088526],[3.371759,4.399944],[3.651111,-1.485005],[4.852377,-2.206776],[7.936208,-4.639245],[-5.924635,0.556130],[-1.350879,4.157842],[-7.898778,5.730532],[-7.596958,-4.841469],[-9.639901,1.385187],[-4.305731,2.234116],[-6.588474,-7.225402],[0.751308,-0.932852],[7.092511,5.199526],[-1.706422,-0.468164],[-9.174266,7.463458],[-4.878663,-3.957925],[1.692263,-7.933783],[2.114949,6.357991],[1.539317,5.205490],[-8.875536,-3.058589],[-5.819849,7.568368],[-9.060434,7.053567],[2.562916,3.571178],[-1.908188,-7.823090],[7.135943,-5.547574],[3.431376,-0.263666],[2.440877,2.667107],[3.011996,-5.070435],[8.440792,-1.043257],[1.018631,-4.728454],[-7.597464,-5.380631],[1.604978,-6.541276],[6.110670,7.609367],[-3.230623,8.301212],[-3.249515,7.031206],[-9.481076,8.927418],[-9.712406,5.486303],[7.409712,-1.025499],[7.285079,1.599610],[-3.844691,-1.166651],[-6.996670,-2.135867],[3.460552,-0.496330],[-4.666756,-2.190088],[8.992341,-6.730498],[0.969450,-9.806250],[9.545843,0.355532],[1.099117,6.104846],[-4.122781,-3.650192],[6.612183,-6.693147],[-4.061934,-4.857029],[-7.794824,-0.782964],[-7.824299,2.601037],[-3.365543,1.687667],[3.847417,4.935903],[9.013198,-5.550215],[-5.070923,-6.688030],[5.619999,-1.610580],[2.497101,-8.840331],[1.202816,-8.904725],[3.554291,-6.703228],[7.712166,0.668102],[-4.808588,5.532512],[8.093664,0.130275],[-8.661127,1.128141],[-3.548958,-1.102375],[7.440935,-3.976663]], dtype = "float64")#candidate|3088|(300, 2)|const|float64
call_3087 = relay.TupleGetItem(func_88_call(relay.reshape(const_3088.astype('float64'), [10, 5, 12])), 0)
call_3089 = relay.TupleGetItem(func_90_call(relay.reshape(const_3088.astype('float64'), [10, 5, 12])), 0)
func_2312_call = mod.get_global_var('func_2312')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_3090 = relay.TupleGetItem(func_2312_call(), 0)
call_3091 = relay.TupleGetItem(func_2313_call(), 0)
output = relay.Tuple([call_3065,call_3087,const_3088,call_3090,])
output2 = relay.Tuple([call_3066,call_3089,const_3088,call_3091,])
func_3099 = relay.Function([], output)
mod['func_3099'] = func_3099
mod = relay.transform.InferType()(mod)
mutated_mod['func_3099'] = func_3099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3099_call = mutated_mod.get_global_var('func_3099')
call_3100 = func_3099_call()
output = call_3100
func_3101 = relay.Function([], output)
mutated_mod['func_3101'] = func_3101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_3181 = relay.TupleGetItem(func_1957_call(), 1)
call_3182 = relay.TupleGetItem(func_1959_call(), 1)
const_3189 = relay.const([[[-6.156908,7.199753,0.646705,-6.582335],[8.005373,0.857595,-3.623795,-0.318044],[-6.362829,7.047063,-5.557423,-7.804283],[9.674753,1.120595,5.703050,-8.450533],[-6.890724,7.809176,0.375117,-5.135429]],[[7.428518,7.701339,9.498245,9.440225],[1.150531,1.482300,7.390097,7.940417],[6.806739,8.385236,8.084866,-6.959215],[4.862826,9.796513,5.852084,-2.732920],[4.426139,-9.830850,3.518264,-0.313885]],[[6.593802,-2.866860,-6.376436,8.001354],[-2.097297,-5.574321,-5.604798,-9.229199],[-5.393676,1.387482,1.259254,-1.662400],[8.475988,5.188473,-3.256389,4.819735],[2.258931,2.081474,4.266362,1.080283]],[[8.549908,-4.468906,-7.991968,0.074494],[-9.119626,-2.257795,-9.544106,4.332378],[1.911252,7.690545,-1.066328,2.425850],[-1.069340,4.234424,9.495270,-6.181877],[-6.535856,9.448411,2.350959,5.515561]],[[0.712042,9.369629,3.056246,0.223072],[7.451578,-9.316940,-4.793793,1.110134],[-5.510485,-2.953542,5.526181,-6.337478],[4.334509,-1.237131,7.990253,2.737907],[4.508628,-4.721325,8.562291,2.394716]],[[-6.453318,-6.324002,-3.213941,-9.952256],[5.925278,-2.330460,4.029533,-4.119743],[-3.926671,3.121689,6.036601,-2.765018],[5.921858,6.733298,8.664040,8.691467],[-4.941268,-5.524213,3.645537,-7.413611]],[[3.936297,6.028242,7.300390,-6.099592],[-8.459261,6.138747,-5.790812,-0.817873],[2.851083,-4.583716,-0.869827,-8.840625],[6.818967,4.703512,9.243200,3.116223],[4.786314,3.716052,4.104684,-5.411020]],[[3.195953,1.836777,-7.168018,1.430261],[8.004975,-7.027820,9.997972,-4.706203],[8.860051,5.735063,9.945804,6.453902],[2.893930,-9.121814,-4.843290,-3.955451],[-8.461747,7.712640,1.773134,-0.882893]]], dtype = "float32")#candidate|3189|(8, 5, 4)|const|float32
bop_3190 = relay.mod(call_3181.astype('float64'), const_3189.astype('float64')) # shape=(8, 5, 4)
bop_3193 = relay.mod(call_3182.astype('float64'), const_3189.astype('float64')) # shape=(8, 5, 4)
func_256_call = mod.get_global_var('func_256')
func_259_call = mutated_mod.get_global_var('func_259')
const_3195 = relay.const([[8.988159,4.349396],[4.963397,1.954530],[4.274197,5.538490],[-6.856161,-1.677248],[1.027590,7.052427],[-2.591988,1.639889]], dtype = "float64")#candidate|3195|(6, 2)|const|float64
call_3194 = relay.TupleGetItem(func_256_call(relay.reshape(const_3195.astype('float64'), [2, 2, 3]), relay.reshape(const_3195.astype('float64'), [2, 2, 3]), ), 2)
call_3196 = relay.TupleGetItem(func_259_call(relay.reshape(const_3195.astype('float64'), [2, 2, 3]), relay.reshape(const_3195.astype('float64'), [2, 2, 3]), ), 2)
output = relay.Tuple([bop_3190,call_3194,const_3195,])
output2 = relay.Tuple([bop_3193,call_3196,const_3195,])
func_3197 = relay.Function([], output)
mod['func_3197'] = func_3197
mod = relay.transform.InferType()(mod)
mutated_mod['func_3197'] = func_3197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3197_call = mutated_mod.get_global_var('func_3197')
call_3198 = func_3197_call()
output = call_3198
func_3199 = relay.Function([], output)
mutated_mod['func_3199'] = func_3199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1586_call = mod.get_global_var('func_1586')
func_1588_call = mutated_mod.get_global_var('func_1588')
call_3205 = relay.TupleGetItem(func_1586_call(), 1)
call_3206 = relay.TupleGetItem(func_1588_call(), 1)
var_3209 = relay.var("var_3209", dtype = "float64", shape = (7, 5, 4))#candidate|3209|(7, 5, 4)|var|float64
bop_3210 = relay.subtract(call_3205.astype('uint32'), var_3209.astype('uint32')) # shape=(7, 5, 4)
bop_3213 = relay.subtract(call_3206.astype('uint32'), var_3209.astype('uint32')) # shape=(7, 5, 4)
output = relay.Tuple([bop_3210,])
output2 = relay.Tuple([bop_3213,])
func_3216 = relay.Function([var_3209,], output)
mod['func_3216'] = func_3216
mod = relay.transform.InferType()(mod)
var_3217 = relay.var("var_3217", dtype = "float64", shape = (7, 5, 4))#candidate|3217|(7, 5, 4)|var|float64
output = func_3216(var_3217)
func_3218 = relay.Function([var_3217], output)
mutated_mod['func_3218'] = func_3218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_3228 = relay.TupleGetItem(func_928_call(), 0)
call_3229 = relay.TupleGetItem(func_929_call(), 0)
var_3230 = relay.var("var_3230", dtype = "int8", shape = (5, 5, 4))#candidate|3230|(5, 5, 4)|var|int8
bop_3231 = relay.bitwise_or(call_3228.astype('uint32'), var_3230.astype('uint32')) # shape=(5, 5, 4)
bop_3234 = relay.bitwise_or(call_3229.astype('uint32'), var_3230.astype('uint32')) # shape=(5, 5, 4)
func_1814_call = mod.get_global_var('func_1814')
func_1817_call = mutated_mod.get_global_var('func_1817')
const_3236 = relay.const([[-1.678852,-0.189646],[-4.297915,-8.960927],[-3.225116,7.372806],[6.222483,-9.582600],[-2.091327,-9.923811],[-1.777744,-9.145803],[-1.782100,6.742408],[-6.840942,-9.202504],[-3.330328,-1.248857],[-1.165030,-3.087279],[8.355901,-5.445409],[-5.457143,8.392966],[8.249183,-9.312736],[0.375700,5.875510],[0.416084,-3.359404],[-4.072773,-6.906895],[6.615349,2.407152],[-5.671662,4.622494],[8.412480,-4.646591],[-2.493194,-5.938321],[0.444727,-6.167846],[-9.200462,4.941627],[-3.190232,7.108181],[-7.534053,7.866204],[-5.283533,4.905668],[-9.686257,3.580531],[7.945999,-1.013379],[1.043220,3.754276],[2.429059,8.491269],[-0.293631,5.938268],[0.342869,1.365261],[3.326914,3.299291],[-4.320638,-2.246093],[9.854241,-8.772767],[0.674273,7.135870],[-1.704111,-2.850693],[-3.708033,4.117255],[-5.641075,3.594107],[0.383648,2.707761],[8.770718,-2.793387],[-0.537620,-4.776330],[-4.691504,-5.414672],[8.049331,2.669008],[-6.006929,-6.870068],[2.198420,9.932404],[-3.067196,9.828517],[-1.591283,-9.531748],[-5.351861,6.498601],[2.873799,-9.028864],[-2.015655,-6.192915],[-0.364180,6.515880],[3.491591,7.806872],[2.421496,-7.331544],[4.996003,6.313027],[-1.174032,9.746131],[9.556360,2.549186],[5.163009,-1.676967],[-4.832931,4.758708],[-8.210289,-5.287345],[-1.348066,4.822570],[-6.191167,-5.870100],[7.014152,3.378013],[0.941500,-2.263591],[3.950736,-6.053528],[-0.976502,3.323885],[8.656792,1.748801],[9.006743,2.212264],[-9.372273,-1.873563],[-5.023381,-0.975628],[-5.280698,1.616630],[3.069120,-8.067940],[-0.370924,8.606434],[-0.468239,5.297176],[8.863398,1.916151],[-4.412334,9.385639],[4.826800,-5.957357],[-0.383037,-8.315572],[-6.139834,-8.156129],[8.730444,7.732538],[3.077454,-5.828286],[9.671356,6.709734],[4.827672,4.100547],[6.575900,-7.092654],[-1.482323,-2.108693],[9.990771,-4.004915],[7.311028,8.641787],[0.157316,-9.582244],[5.493464,-4.997478],[-1.824783,-7.190994],[9.296123,-6.181162],[-8.073497,7.540463],[0.815981,9.328590],[-8.407561,-9.847750],[-7.825213,3.535277],[-0.921572,7.673826],[-7.455140,-2.642420],[1.609646,-1.521231],[9.763877,-5.046072],[8.038131,-7.925933],[9.990897,-6.162675],[6.501010,4.394093],[-5.201316,-5.566720],[-2.551955,8.346950],[1.522487,-5.186022],[-5.218861,8.947175],[9.064247,2.076334],[-5.467665,4.216058],[8.740172,7.324830],[-6.286454,-7.048742],[9.392381,-5.827217],[-9.531680,1.208820],[0.348398,5.458987],[-9.728620,5.275269],[-7.420470,3.468859],[1.065754,-4.317320],[-6.921898,0.342871],[2.126880,8.621136],[-8.359722,-9.122810],[0.677378,8.396998],[7.916173,-7.113685],[1.540806,4.499837],[-9.792935,-1.335538],[2.295802,-7.478187],[2.588720,0.816410],[-7.864784,6.176010],[-1.852411,9.709819],[0.168826,-1.631965],[8.582047,6.823879],[8.037116,-4.599176],[7.392921,2.757642],[-0.091517,-8.226829],[2.896411,-5.933042],[-4.178580,6.039333],[9.748453,2.650770],[3.702970,-4.359205],[-2.674065,3.229109],[-4.958473,-2.589564],[7.367786,7.467334],[1.655884,5.798133],[5.539176,-2.104199],[9.575728,-0.969392],[8.314151,-4.209149],[1.143545,8.669316],[-1.703436,8.548508],[1.780922,-2.640156],[4.656720,-4.464183],[4.330852,-9.311494],[2.178543,-7.577077],[-5.395311,8.641183],[-8.737387,-8.529886],[-0.132023,-5.889524],[-5.654610,-7.790537],[0.006455,-9.265048],[-7.984827,8.564104],[-2.544643,-0.900453],[5.466856,9.019097],[9.664769,5.111860],[-3.464473,5.489178],[1.104692,0.130137],[-5.426635,3.448103],[-7.492052,-7.977293],[-1.165512,-0.090650],[4.725478,-5.173415],[1.937630,-5.585677],[4.609197,6.489428],[4.749702,-2.515993],[-6.233896,4.630187],[1.707835,-9.687016],[-3.938072,-8.017625],[-8.594501,-9.468931],[8.560034,-4.996726],[-3.441707,4.077210],[-8.373185,9.064419],[-0.558552,2.000183],[1.538520,1.173710],[7.537001,-4.545692],[-1.703101,7.536065],[6.673356,2.241274],[-9.777839,9.321942],[-6.733065,-2.783397],[2.585925,6.983286],[-4.447418,-8.402750],[0.786352,-3.883304],[1.454759,-1.126844],[-5.479024,9.213779],[0.199060,-3.306966],[-1.522022,-7.052256],[8.122769,-4.195303],[-2.486010,-4.595287],[-8.870497,-9.888176],[-5.767117,-6.206880],[2.919438,3.248040],[-1.242401,6.328972],[0.473428,-9.271854],[-7.126971,7.843403],[7.829081,-9.711961],[5.282349,-1.347079],[-7.500677,4.033940],[-7.224549,-1.108797],[-8.895521,6.693841],[-6.343922,2.251480],[-0.194149,-7.183131],[-9.074011,-5.830654],[2.761434,-4.384933],[3.433154,-5.266756],[8.898741,-3.978134],[3.126531,-1.345554],[7.235490,8.043801],[-8.884826,6.089581],[-8.322319,9.496613],[6.857972,-2.483090],[8.905456,1.552886],[-4.642905,-7.141787],[3.424567,3.920500],[1.345749,2.617012],[6.295090,2.313542],[8.358620,-3.614502],[-2.265755,-0.535416],[-8.067276,-8.217227],[9.425369,-8.096602],[6.084666,-6.914680],[-1.091237,2.297451],[8.185104,-5.470762],[9.154450,-0.188343],[-3.089979,-1.421682],[7.981653,2.848870],[-9.085012,8.882739],[5.829577,7.565782],[-4.560136,-8.177497],[2.676175,-1.730048],[-4.485048,0.246098],[-0.358138,-8.094349],[-8.803486,5.937420],[5.182567,6.855264],[-1.023830,-2.798506],[2.410449,-3.362392],[3.931298,-7.213781],[3.101856,9.952746],[1.146061,9.681139],[-7.943772,-3.376455],[3.276802,-6.810201],[-9.423317,-3.944484],[-7.722074,3.075429],[-5.940747,6.539634],[-4.388640,-6.530311],[8.045414,9.026141],[-8.425155,-5.884414],[-4.777605,6.814852],[2.203068,-6.001822],[-0.682469,-9.979050],[4.210534,-7.461140],[-6.070127,8.664332],[0.256594,-3.419194],[5.859794,9.035741],[-0.030703,2.786216],[-9.456597,-7.060929],[-9.695616,-9.712300],[3.741865,-5.978752],[-4.692046,-7.095446],[-0.970781,9.060508],[3.423962,-6.208306],[8.135702,-8.234753],[-0.768092,-5.308752],[7.380782,-8.683929],[1.870116,-4.629456],[3.727403,-3.283245],[1.275370,-5.512734],[-8.226611,9.296145],[4.513027,8.791195],[2.918900,8.762627],[4.206162,-7.597360],[-5.221197,-8.370796],[4.796919,1.069333],[6.445861,-9.233794],[-1.506287,4.799954],[-6.376054,5.901272],[-5.698764,-5.657095],[-2.525908,9.631513],[4.393454,-3.802774],[-3.574100,-4.499447],[1.263373,5.212601],[6.047589,7.559197],[-3.603728,-6.754264],[4.031987,1.396239],[-2.993446,6.877179],[3.423092,-0.467200],[0.928568,-4.552848],[-0.409129,6.287628],[-3.676398,-2.095365],[6.141027,-7.242397],[-9.575426,-1.610838],[-1.000818,-4.953242],[-1.114620,9.974482],[-8.881643,-5.739744],[4.452986,-1.427506],[3.344270,8.470476],[-5.753340,9.610084],[-5.290119,3.454516],[4.279899,-3.410398],[3.013380,-3.727783]], dtype = "float64")#candidate|3236|(300, 2)|const|float64
const_3237 = relay.const([-4.284050,6.987942,3.066022,7.086123,6.646087,-0.922173,-0.322156,4.542254,9.322796,-0.563481,3.116153,-7.548475,6.172953,-3.034300,7.504596,-6.463158,6.392776,5.683020,9.714422,-4.421160,9.655666,-9.999876,-7.886286,-6.891523,7.989328,-1.370620,-7.955189,0.003190,-1.636056,-8.562428,-0.751005,8.202626,-3.956475,-5.348786,8.990058,-8.668678,4.033591,-3.901307,0.884019,-6.466917,0.269285,9.380553,8.864265,8.948684,-7.817547,9.664559,2.133562,-8.898731,0.483683,7.593935,0.548205,-2.014176,4.538569,8.306881,9.787117,5.370113,-1.189886,-7.543057,2.122307,7.618265,1.796896,-8.301088,8.394294,-9.976172,3.107393,5.717263,-4.698217,-5.306211,8.199690,-8.111322,3.853043,4.119804,-5.677035,1.493127,-5.308161,8.912151,-2.645151,-6.663121,-1.151264,-8.488632,-2.039104,9.454943,9.637636,-8.703334,8.878125,-5.301895,-9.236725,-8.889146,7.851918,7.748961,0.672273,-1.150842,-8.404912,3.108354,3.969849,0.713335,-8.534583,-3.342793,-6.101534,-0.045296,5.493085,-6.424726,-0.525944,-7.017305,-8.052050,4.622126,-4.216462,1.932899,-3.356270,-5.720501,4.247109,-6.940751,-8.882952,2.835177,4.486673,-7.223670,-6.840959,8.588838,2.041851,3.096531,1.094524,5.348310,-5.117600,-6.983837,-0.524734,-2.009654,-7.034468,5.890415,-3.108184,9.159964,-1.642028,-3.342537,-4.124689,1.833269,-6.519990,-0.396516,-1.444660,0.455382,-6.625009,3.532866,-8.828674,-6.634223,-1.634003,9.658632,6.592698,0.042218,-0.375783,-8.241915,2.342716,5.485249,-5.770727,2.984773,7.908479,6.394125,-0.889434,-3.879932,2.402412,-5.399531,-7.408623,-7.348383,-2.001074,3.767508,6.038556,-2.156257,-1.892208,-2.808733,2.928994,9.724488,1.061780,-1.595027,0.530268,-4.642631,-2.545310,7.128083,3.508441,-8.735355,4.868977,-8.097098,7.625142,8.012841,-8.895225,6.669017,9.006022,8.142881,5.443889,-7.525136,-9.704544,7.262526,0.690144,-3.919988,-9.238525,3.186904,-9.427212,7.370904,-7.648676,8.324790,-6.625592,-1.307389,6.482923,-9.142018], dtype = "float32")#candidate|3237|(200,)|const|float32
call_3235 = relay.TupleGetItem(func_1814_call(relay.reshape(const_3236.astype('float64'), [600,]), relay.reshape(const_3237.astype('float32'), [10, 5, 4]), ), 0)
call_3238 = relay.TupleGetItem(func_1817_call(relay.reshape(const_3236.astype('float64'), [600,]), relay.reshape(const_3237.astype('float32'), [10, 5, 4]), ), 0)
output = relay.Tuple([bop_3231,call_3235,const_3236,const_3237,])
output2 = relay.Tuple([bop_3234,call_3238,const_3236,const_3237,])
func_3253 = relay.Function([var_3230,], output)
mod['func_3253'] = func_3253
mod = relay.transform.InferType()(mod)
var_3254 = relay.var("var_3254", dtype = "int8", shape = (5, 5, 4))#candidate|3254|(5, 5, 4)|var|int8
output = func_3253(var_3254)
func_3255 = relay.Function([var_3254], output)
mutated_mod['func_3255'] = func_3255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_3269 = relay.TupleGetItem(func_1397_call(), 0)
call_3270 = relay.TupleGetItem(func_1399_call(), 0)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_3277 = relay.TupleGetItem(func_2031_call(), 1)
call_3278 = relay.TupleGetItem(func_2033_call(), 1)
output = relay.Tuple([call_3269,call_3277,])
output2 = relay.Tuple([call_3270,call_3278,])
func_3295 = relay.Function([], output)
mod['func_3295'] = func_3295
mod = relay.transform.InferType()(mod)
output = func_3295()
func_3296 = relay.Function([], output)
mutated_mod['func_3296'] = func_3296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3330 = relay.var("var_3330", dtype = "int32", shape = (7, 10, 11))#candidate|3330|(7, 10, 11)|var|int32
var_3331 = relay.var("var_3331", dtype = "int32", shape = (7, 10, 11))#candidate|3331|(7, 10, 11)|var|int32
bop_3332 = relay.bitwise_or(var_3330.astype('int32'), relay.reshape(var_3331.astype('int32'), relay.shape_of(var_3330))) # shape=(7, 10, 11)
output = bop_3332
output2 = bop_3332
func_3337 = relay.Function([var_3330,var_3331,], output)
mod['func_3337'] = func_3337
mod = relay.transform.InferType()(mod)
var_3338 = relay.var("var_3338", dtype = "int32", shape = (7, 10, 11))#candidate|3338|(7, 10, 11)|var|int32
var_3339 = relay.var("var_3339", dtype = "int32", shape = (7, 10, 11))#candidate|3339|(7, 10, 11)|var|int32
output = func_3337(var_3338,var_3339,)
func_3340 = relay.Function([var_3338,var_3339,], output)
mutated_mod['func_3340'] = func_3340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3295_call = mod.get_global_var('func_3295')
func_3296_call = mutated_mod.get_global_var('func_3296')
call_3356 = relay.TupleGetItem(func_3295_call(), 0)
call_3357 = relay.TupleGetItem(func_3296_call(), 0)
func_2037_call = mod.get_global_var('func_2037')
func_2038_call = mutated_mod.get_global_var('func_2038')
call_3393 = relay.TupleGetItem(func_2037_call(), 0)
call_3394 = relay.TupleGetItem(func_2038_call(), 0)
func_3253_call = mod.get_global_var('func_3253')
func_3255_call = mutated_mod.get_global_var('func_3255')
var_3403 = relay.var("var_3403", dtype = "int8", shape = (100,))#candidate|3403|(100,)|var|int8
call_3402 = relay.TupleGetItem(func_3253_call(relay.reshape(var_3403.astype('int8'), [5, 5, 4])), 3)
call_3404 = relay.TupleGetItem(func_3255_call(relay.reshape(var_3403.astype('int8'), [5, 5, 4])), 3)
output = relay.Tuple([call_3356,call_3393,call_3402,var_3403,])
output2 = relay.Tuple([call_3357,call_3394,call_3404,var_3403,])
func_3418 = relay.Function([var_3403,], output)
mod['func_3418'] = func_3418
mod = relay.transform.InferType()(mod)
var_3419 = relay.var("var_3419", dtype = "int8", shape = (100,))#candidate|3419|(100,)|var|int8
output = func_3418(var_3419)
func_3420 = relay.Function([var_3419], output)
mutated_mod['func_3420'] = func_3420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1213_call = mod.get_global_var('func_1213')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_3435 = relay.TupleGetItem(func_1213_call(), 0)
call_3436 = relay.TupleGetItem(func_1215_call(), 0)
output = call_3435
output2 = call_3436
func_3438 = relay.Function([], output)
mod['func_3438'] = func_3438
mod = relay.transform.InferType()(mod)
output = func_3438()
func_3439 = relay.Function([], output)
mutated_mod['func_3439'] = func_3439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3295_call = mod.get_global_var('func_3295')
func_3296_call = mutated_mod.get_global_var('func_3296')
call_3447 = relay.TupleGetItem(func_3295_call(), 0)
call_3448 = relay.TupleGetItem(func_3296_call(), 0)
func_3037_call = mod.get_global_var('func_3037')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_3457 = relay.TupleGetItem(func_3037_call(), 0)
call_3458 = relay.TupleGetItem(func_3038_call(), 0)
func_1213_call = mod.get_global_var('func_1213')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_3459 = relay.TupleGetItem(func_1213_call(), 0)
call_3460 = relay.TupleGetItem(func_1215_call(), 0)
output = relay.Tuple([call_3447,call_3457,call_3459,])
output2 = relay.Tuple([call_3448,call_3458,call_3460,])
func_3464 = relay.Function([], output)
mod['func_3464'] = func_3464
mod = relay.transform.InferType()(mod)
mutated_mod['func_3464'] = func_3464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3464_call = mutated_mod.get_global_var('func_3464')
call_3465 = func_3464_call()
output = call_3465
func_3466 = relay.Function([], output)
mutated_mod['func_3466'] = func_3466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2635_call = mod.get_global_var('func_2635')
func_2637_call = mutated_mod.get_global_var('func_2637')
call_3485 = func_2635_call()
call_3486 = func_2635_call()
uop_3490 = relay.asinh(call_3485.astype('float32')) # shape=(6, 5, 4)
uop_3492 = relay.asinh(call_3486.astype('float32')) # shape=(6, 5, 4)
func_3295_call = mod.get_global_var('func_3295')
func_3296_call = mutated_mod.get_global_var('func_3296')
call_3497 = relay.TupleGetItem(func_3295_call(), 1)
call_3498 = relay.TupleGetItem(func_3296_call(), 1)
output = relay.Tuple([uop_3490,call_3497,])
output2 = relay.Tuple([uop_3492,call_3498,])
func_3507 = relay.Function([], output)
mod['func_3507'] = func_3507
mod = relay.transform.InferType()(mod)
mutated_mod['func_3507'] = func_3507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mutated_mod.get_global_var('func_3507')
call_3508 = func_3507_call()
output = call_3508
func_3509 = relay.Function([], output)
mutated_mod['func_3509'] = func_3509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1921_call = mod.get_global_var('func_1921')
func_1922_call = mutated_mod.get_global_var('func_1922')
call_3515 = func_1921_call()
call_3516 = func_1921_call()
var_3553 = relay.var("var_3553", dtype = "uint16", shape = (14, 5, 4))#candidate|3553|(14, 5, 4)|var|uint16
bop_3554 = relay.multiply(call_3515.astype('uint32'), var_3553.astype('uint32')) # shape=(14, 5, 4)
bop_3557 = relay.multiply(call_3516.astype('uint32'), var_3553.astype('uint32')) # shape=(14, 5, 4)
bop_3559 = relay.mod(var_3553.astype('float64'), call_3515.astype('float64')) # shape=(14, 5, 4)
bop_3562 = relay.mod(var_3553.astype('float64'), call_3516.astype('float64')) # shape=(14, 5, 4)
uop_3570 = relay.rsqrt(bop_3559.astype('float64')) # shape=(14, 5, 4)
uop_3572 = relay.rsqrt(bop_3562.astype('float64')) # shape=(14, 5, 4)
uop_3575 = relay.cos(uop_3570.astype('float64')) # shape=(14, 5, 4)
uop_3577 = relay.cos(uop_3572.astype('float64')) # shape=(14, 5, 4)
func_88_call = mod.get_global_var('func_88')
func_90_call = mutated_mod.get_global_var('func_90')
var_3604 = relay.var("var_3604", dtype = "float64", shape = (600,))#candidate|3604|(600,)|var|float64
call_3603 = relay.TupleGetItem(func_88_call(relay.reshape(var_3604.astype('float64'), [10, 5, 12])), 0)
call_3605 = relay.TupleGetItem(func_90_call(relay.reshape(var_3604.astype('float64'), [10, 5, 12])), 0)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_3607 = relay.TupleGetItem(func_2808_call(), 0)
call_3608 = relay.TupleGetItem(func_2810_call(), 0)
func_2295_call = mod.get_global_var('func_2295')
func_2297_call = mutated_mod.get_global_var('func_2297')
const_3612 = relay.const([[4,3],[6,2],[4,7],[7,-10],[-8,-1],[-8,-5],[-4,-4],[9,-2],[-3,-10],[10,-9],[6,-2],[7,-9],[-9,-9],[-7,5],[1,2],[5,-7],[-10,7],[9,-4],[-5,9],[-10,-8],[1,8],[-4,-9],[-4,9],[6,8],[-10,-8],[5,5],[-10,-2],[3,1],[-7,-1],[-2,8],[-1,7],[-2,5],[-2,-3],[9,-6],[10,-9],[-8,-8],[9,-6],[8,-9],[2,8],[1,-5]], dtype = "int8")#candidate|3612|(40, 2)|const|int8
call_3611 = relay.TupleGetItem(func_2295_call(relay.reshape(const_3612.astype('int8'), [4, 5, 4])), 1)
call_3613 = relay.TupleGetItem(func_2297_call(relay.reshape(const_3612.astype('int8'), [4, 5, 4])), 1)
output = relay.Tuple([bop_3554,uop_3575,call_3603,var_3604,call_3607,call_3611,const_3612,])
output2 = relay.Tuple([bop_3557,uop_3577,call_3605,var_3604,call_3608,call_3613,const_3612,])
func_3618 = relay.Function([var_3553,var_3604,], output)
mod['func_3618'] = func_3618
mod = relay.transform.InferType()(mod)
var_3619 = relay.var("var_3619", dtype = "uint16", shape = (14, 5, 4))#candidate|3619|(14, 5, 4)|var|uint16
var_3620 = relay.var("var_3620", dtype = "float64", shape = (600,))#candidate|3620|(600,)|var|float64
output = func_3618(var_3619,var_3620,)
func_3621 = relay.Function([var_3619,var_3620,], output)
mutated_mod['func_3621'] = func_3621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3037_call = mod.get_global_var('func_3037')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_3673 = relay.TupleGetItem(func_3037_call(), 0)
call_3674 = relay.TupleGetItem(func_3038_call(), 0)
func_2605_call = mod.get_global_var('func_2605')
func_2608_call = mutated_mod.get_global_var('func_2608')
const_3679 = relay.const([[8,-5,2,8,-5,-3,9,-2,7,-3,-7,-6,4,6,-7,7,8,2,1,1,-10,5,-8,-2,9,3,6,3,-1,-1,9,-6,1,-4,7,10,-10,7,-4,-4,-8,10,-8,5,2,-8,3,-8,1,9,-7,-5],[6,6,5,-2,1,-9,5,-10,10,-7,-3,9,7,4,-9,-3,-3,2,3,2,-5,4,-5,-8,4,9,-10,-1,-10,-5,6,-3,-8,-8,10,6,-1,9,5,-4,-3,-6,3,2,-4,2,4,6,2,-7,-4,-10],[-3,2,6,-9,-8,2,2,-5,-10,6,-2,-9,8,9,-9,8,7,2,-5,2,5,7,7,-6,8,-4,4,-7,9,4,-4,-2,2,4,-6,-3,8,2,3,-6,-10,3,4,-6,-5,-3,-5,-10,2,6,-8,-2],[-10,-6,2,4,-2,6,7,1,2,-9,-2,4,10,-3,-1,-9,-9,4,6,-3,-2,-4,-1,-1,8,2,8,5,7,10,-3,1,-1,7,-10,6,1,3,5,-9,-3,-7,8,-10,-8,-5,7,-6,10,8,6,-3],[5,9,9,7,8,2,-3,-2,-1,5,2,8,7,-3,-1,-7,2,8,-5,-3,8,8,-8,-6,9,8,-3,5,-4,10,-5,-4,7,8,9,-5,-1,-2,-5,-9,-10,-8,-7,2,1,9,-10,-3,-6,-9,6,-4]], dtype = "int8")#candidate|3679|(5, 52)|const|int8
var_3680 = relay.var("var_3680", dtype = "float64", shape = (12,))#candidate|3680|(12,)|var|float64
call_3678 = relay.TupleGetItem(func_2605_call(relay.reshape(const_3679.astype('int8'), [13, 5, 4]), relay.reshape(var_3680.astype('float64'), [12,]), ), 1)
call_3681 = relay.TupleGetItem(func_2608_call(relay.reshape(const_3679.astype('int8'), [13, 5, 4]), relay.reshape(var_3680.astype('float64'), [12,]), ), 1)
output = relay.Tuple([call_3673,call_3678,const_3679,var_3680,])
output2 = relay.Tuple([call_3674,call_3681,const_3679,var_3680,])
func_3705 = relay.Function([var_3680,], output)
mod['func_3705'] = func_3705
mod = relay.transform.InferType()(mod)
var_3706 = relay.var("var_3706", dtype = "float64", shape = (12,))#candidate|3706|(12,)|var|float64
output = func_3705(var_3706)
func_3707 = relay.Function([var_3706], output)
mutated_mod['func_3707'] = func_3707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1851_call = mod.get_global_var('func_1851')
func_1852_call = mutated_mod.get_global_var('func_1852')
call_3725 = relay.TupleGetItem(func_1851_call(), 0)
call_3726 = relay.TupleGetItem(func_1852_call(), 0)
func_2197_call = mod.get_global_var('func_2197')
func_2198_call = mutated_mod.get_global_var('func_2198')
call_3737 = relay.TupleGetItem(func_2197_call(), 1)
call_3738 = relay.TupleGetItem(func_2198_call(), 1)
output = relay.Tuple([call_3725,call_3737,])
output2 = relay.Tuple([call_3726,call_3738,])
func_3746 = relay.Function([], output)
mod['func_3746'] = func_3746
mod = relay.transform.InferType()(mod)
output = func_3746()
func_3747 = relay.Function([], output)
mutated_mod['func_3747'] = func_3747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_3758 = func_1270_call()
call_3759 = func_1270_call()
func_1814_call = mod.get_global_var('func_1814')
func_1817_call = mutated_mod.get_global_var('func_1817')
const_3767 = relay.const([-8.291203,-1.352753,8.571353,8.707494,-6.332385,1.407546,4.739668,-7.308612,-3.215164,3.263051,0.873506,3.572035,-7.849490,-5.118094,3.882307,4.137152,4.895035,-6.774574,-1.189165,-9.558957,-7.699018,8.599578,-2.566923,0.506268,8.448898,5.403107,-1.434833,-3.905923,-5.504351,2.529804,-4.510556,6.664072,-2.084854,-1.390149,1.733799,-0.601615,-3.559710,-1.023152,6.896964,5.735683,-6.195788,5.046408,3.441536,9.021834,-2.777501,-7.630065,0.799992,7.669266,1.717558,6.562032,-9.486038,-9.423748,6.649601,5.805595,5.533843,2.028898,9.125749,-4.639802,-9.682159,-6.919379,-5.822470,8.191386,-0.867946,-9.130339,0.578701,0.853481,8.814032,-2.679960,-3.756074,5.126994,1.969103,5.937883,-5.560153,5.130782,5.135592,1.867426,-8.232786,3.126270,6.820004,5.059639,6.375020,-5.801953,-0.410469,-1.411454,-2.009230,-8.739176,-5.228237,8.733524,-8.988909,-8.285538,-4.635580,9.518952,-9.865953,-5.492407,-7.421371,-3.711521,-6.011003,-0.422037,-7.265982,4.245821,8.845375,-1.752761,8.407230,-6.424448,-1.955968,0.548859,-0.252345,-5.792284,5.063702,2.951421,-2.899236,-8.914101,-5.737661,6.753917,5.917090,-1.723486,4.095110,-3.276211,-2.415018,-6.652522,0.541895,0.772394,-7.803511,0.859964,-0.336013,-5.909718,-8.167401,2.532728,4.383286,2.805919,9.472613,6.954219,-4.680578,0.636711,-0.776719,-4.495493,2.776406,-2.527555,4.464984,-3.646188,-4.123396,-5.619492,6.407609,8.020106,-9.741516,1.427394,-1.670318,-8.457019,-4.308451,0.037698,6.611066,8.335347,-6.430993,9.191255,9.833039,0.861066,-0.870888,-1.361305,-5.498340,-6.311731,7.852994,-4.673330,3.986828,-4.664985,0.217065,-3.658528,0.099115,6.928825,6.054206,7.548920,-8.820255,-6.699516,-4.776530,-1.054469,3.305211,-9.251995,-5.309885,-4.900268,7.177695,-3.622471,9.532209,-4.115836,-1.228132,-3.994702,-4.282503,-9.049197,-3.472824,9.084543,0.373356,0.097838,-1.237185,9.638588,9.728232,-2.541943,8.743409,9.661618,-7.114938,5.239314,7.718459,-0.298551,-3.203292,0.120105,-3.423407,7.385742,-9.744364,-5.262217,-8.537774,-6.159106,0.924388,1.943633,7.583152,3.006959,-6.923954,-1.708315,-2.153011,4.278848,1.771097,-2.138625,3.536671,0.707464,-9.670897,-9.487869,-0.424952,-6.455022,-9.928530,-4.414011,-9.660540,7.587869,-0.600280,9.463283,-6.429429,6.749350,2.243680,0.718513,-1.976155,-4.464406,-6.165348,0.691971,3.573144,2.064944,7.651806,2.495620,8.786189,-1.435331,-1.529378,2.754948,-1.342491,-9.915117,-8.203866,-1.185900,1.629988,4.886221,-6.566567,-8.527624,9.594397,1.442926,1.920606,-0.923096,6.817494,-3.620992,-3.160870,-5.687510,1.692136,-3.563011,1.352680,-2.070035,-5.878838,-9.006431,-2.090563,-5.966883,-7.386270,2.439762,4.495817,1.333197,-7.487108,-4.200729,4.586844,-4.248739,-6.336761,-1.442735,8.870445,-1.034321,-0.010828,-2.518818,8.073101,-2.379579,-5.877959,4.182034,-2.218927,-0.287594,-8.467352,1.631489,-6.788055,-0.988142,3.730824,-6.691416,9.426095,-2.075173,3.349266,4.855460,8.993598,0.225107,5.437537,8.232448,7.097812,-2.437024,1.695727,5.704551,5.688046,-9.022316,-5.694437,-4.211480,4.241559,7.181557,0.696797,9.987912,3.181460,9.739520,2.162346,-3.857608,-0.713909,-2.133386,-5.007566,8.317310,-7.942213,-5.798437,-1.394720,-9.310607,6.144723,2.533780,-0.867339,-3.934431,2.162704,-0.106452,-8.562258,7.750066,-8.729573,-0.527316,6.070947,-0.695408,1.781918,-9.735372,3.592879,1.835673,-1.323684,-5.878825,6.694720,-9.040533,-9.428749,1.532643,8.651546,1.411488,0.052297,8.107970,-0.771154,-7.102560,-1.886198,7.355818,0.078653,1.830415,1.950369,1.042902,-9.221772,6.343212,-4.970284,1.208269,1.341947,2.696481,1.273970,2.938094,6.792039,1.621604,-4.468116,7.596350,-0.790828,-5.320076,-2.514774,-5.870760,2.727492,4.975788,5.303758,-5.100975,-8.414761,1.655983,-5.539151,5.464765,-2.885867,0.198076,7.957334,-6.530586,1.101059,-6.022573,-9.900059,-8.336586,-6.307391,-1.665090,8.980980,0.413055,-4.606953,5.376568,0.003251,-0.698220,4.815471,8.404773,6.748825,-5.872099,-4.962736,-5.374708,-0.934448,-7.542228,1.410275,-6.518160,6.538989,-8.482136,-0.250212,-1.075126,-0.475878,4.221984,0.411579,-9.467506,-8.857746,9.687725,9.225913,-2.257058,1.327975,3.770405,9.919655,3.611599,6.869180,-3.567500,3.552103,0.257075,-1.251873,2.621574,3.861111,-1.854767,1.274773,-2.701358,8.365147,-2.264038,-4.536514,1.244669,9.277884,-5.060093,-4.129324,-9.941531,-3.557959,1.546200,-9.849035,-5.137248,8.812666,4.892688,-5.128650,0.561971,-4.599442,-0.927780,0.696605,-1.439908,-1.928387,8.523249,-0.341147,-5.063651,-8.350307,5.168384,8.461203,-4.146833,-9.850231,0.954139,-8.400147,-9.410423,-2.974739,2.303136,3.372740,-4.260890,-4.838530,-3.584953,9.971129,3.715142,7.903233,-1.396050,-2.974898,2.551616,-6.695081,-6.626399,9.818598,-5.732570,9.298578,-7.468305,0.789379,1.483809,-7.917039,-6.173226,-1.720307,1.392408,-9.579865,-2.775377,9.254285,0.398635,-7.338371,-2.697390,4.777416,7.762670,-4.224409,7.860448,-2.061564,2.164721,-1.281183,-1.267694,-1.989911,-8.553567,1.126933,9.505136,-2.548030,9.936720,-0.981573,8.479367,-8.554893,4.805008,-6.242936,-6.431391,0.007796,2.185933,-5.062228,-4.724734,-9.086748,6.054856,-7.935342,-9.580909,-6.031645,6.307858,9.428277,-6.949393,-0.564291,-8.752311,-1.943109,5.797578,-4.833706,3.589920,9.202681,3.961948,4.683984,4.278973,-0.306043,-4.626326,3.563168,0.320475,-6.776566,-8.042779,7.700795,6.865876,-5.280124,4.984792,-0.183085,5.993309,1.459019,8.194396,4.509478,-6.601558,-0.678062,-1.252703,-8.090695,-1.664895,7.865981,6.083489,2.848841,-9.781379,-4.585098,-5.985387,3.074735,-8.376568,2.858210,4.707967,-0.149077,-6.943611,-6.697201,8.905168,-6.413623,-3.862452,-5.785100,6.641694,-8.360854,0.062703,7.950441,3.045875,3.187709,9.209318,7.871221,-6.052663,-7.015953,-1.048216,3.069488,-9.625446,1.661660,-0.511532,-3.020210,3.481742,8.333090,2.733767,3.033030,9.885779], dtype = "float64")#candidate|3767|(600,)|const|float64
var_3768 = relay.var("var_3768", dtype = "float32", shape = (200,))#candidate|3768|(200,)|var|float32
call_3766 = relay.TupleGetItem(func_1814_call(relay.reshape(const_3767.astype('float64'), [600,]), relay.reshape(var_3768.astype('float32'), [10, 5, 4]), ), 4)
call_3769 = relay.TupleGetItem(func_1817_call(relay.reshape(const_3767.astype('float64'), [600,]), relay.reshape(var_3768.astype('float32'), [10, 5, 4]), ), 4)
func_3253_call = mod.get_global_var('func_3253')
func_3255_call = mutated_mod.get_global_var('func_3255')
var_3777 = relay.var("var_3777", dtype = "int8", shape = (100,))#candidate|3777|(100,)|var|int8
call_3776 = relay.TupleGetItem(func_3253_call(relay.reshape(var_3777.astype('int8'), [5, 5, 4])), 2)
call_3778 = relay.TupleGetItem(func_3255_call(relay.reshape(var_3777.astype('int8'), [5, 5, 4])), 2)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_3780 = relay.TupleGetItem(func_1431_call(), 0)
call_3781 = relay.TupleGetItem(func_1433_call(), 0)
output = relay.Tuple([call_3758,call_3766,const_3767,var_3768,call_3776,var_3777,call_3780,])
output2 = relay.Tuple([call_3759,call_3769,const_3767,var_3768,call_3778,var_3777,call_3781,])
func_3789 = relay.Function([var_3768,var_3777,], output)
mod['func_3789'] = func_3789
mod = relay.transform.InferType()(mod)
mutated_mod['func_3789'] = func_3789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mutated_mod.get_global_var('func_3789')
var_3791 = relay.var("var_3791", dtype = "float32", shape = (200,))#candidate|3791|(200,)|var|float32
var_3792 = relay.var("var_3792", dtype = "int8", shape = (100,))#candidate|3792|(100,)|var|int8
call_3790 = func_3789_call(var_3791,var_3792,)
output = call_3790
func_3793 = relay.Function([var_3791,var_3792,], output)
mutated_mod['func_3793'] = func_3793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_3797 = relay.TupleGetItem(func_1597_call(), 0)
call_3798 = relay.TupleGetItem(func_1599_call(), 0)
output = relay.Tuple([call_3797,])
output2 = relay.Tuple([call_3798,])
func_3806 = relay.Function([], output)
mod['func_3806'] = func_3806
mod = relay.transform.InferType()(mod)
output = func_3806()
func_3807 = relay.Function([], output)
mutated_mod['func_3807'] = func_3807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3037_call = mod.get_global_var('func_3037')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_3808 = relay.TupleGetItem(func_3037_call(), 0)
call_3809 = relay.TupleGetItem(func_3038_call(), 0)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
var_3837 = relay.var("var_3837", dtype = "float32", shape = (784,))#candidate|3837|(784,)|var|float32
call_3836 = relay.TupleGetItem(func_2406_call(relay.reshape(var_3837.astype('float32'), [7, 7, 16])), 0)
call_3838 = relay.TupleGetItem(func_2408_call(relay.reshape(var_3837.astype('float32'), [7, 7, 16])), 0)
output = relay.Tuple([call_3808,call_3836,var_3837,])
output2 = relay.Tuple([call_3809,call_3838,var_3837,])
func_3850 = relay.Function([var_3837,], output)
mod['func_3850'] = func_3850
mod = relay.transform.InferType()(mod)
mutated_mod['func_3850'] = func_3850
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3851 = relay.var("var_3851", dtype = "float32", shape = (784,))#candidate|3851|(784,)|var|float32
func_3850_call = mutated_mod.get_global_var('func_3850')
call_3852 = func_3850_call(var_3851)
output = call_3852
func_3853 = relay.Function([var_3851], output)
mutated_mod['func_3853'] = func_3853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2312_call = mod.get_global_var('func_2312')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_3858 = relay.TupleGetItem(func_2312_call(), 0)
call_3859 = relay.TupleGetItem(func_2313_call(), 0)
output = call_3858
output2 = call_3859
func_3879 = relay.Function([], output)
mod['func_3879'] = func_3879
mod = relay.transform.InferType()(mod)
mutated_mod['func_3879'] = func_3879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3879_call = mutated_mod.get_global_var('func_3879')
call_3880 = func_3879_call()
output = call_3880
func_3881 = relay.Function([], output)
mutated_mod['func_3881'] = func_3881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2757_call = mod.get_global_var('func_2757')
func_2758_call = mutated_mod.get_global_var('func_2758')
call_3899 = relay.TupleGetItem(func_2757_call(), 0)
call_3900 = relay.TupleGetItem(func_2758_call(), 0)
output = call_3899
output2 = call_3900
func_3904 = relay.Function([], output)
mod['func_3904'] = func_3904
mod = relay.transform.InferType()(mod)
mutated_mod['func_3904'] = func_3904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3904_call = mutated_mod.get_global_var('func_3904')
call_3905 = func_3904_call()
output = call_3905
func_3906 = relay.Function([], output)
mutated_mod['func_3906'] = func_3906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mod.get_global_var('func_2921')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_3929 = relay.TupleGetItem(func_2921_call(), 0)
call_3930 = relay.TupleGetItem(func_2922_call(), 0)
output = relay.Tuple([call_3929,])
output2 = relay.Tuple([call_3930,])
func_3934 = relay.Function([], output)
mod['func_3934'] = func_3934
mod = relay.transform.InferType()(mod)
output = func_3934()
func_3935 = relay.Function([], output)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3746_call = mod.get_global_var('func_3746')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_3945 = relay.TupleGetItem(func_3746_call(), 0)
call_3946 = relay.TupleGetItem(func_3747_call(), 0)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_3973 = relay.TupleGetItem(func_1716_call(), 1)
call_3974 = relay.TupleGetItem(func_1717_call(), 1)
output = relay.Tuple([call_3945,call_3973,])
output2 = relay.Tuple([call_3946,call_3974,])
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
func_2944_call = mod.get_global_var('func_2944')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_4009 = relay.TupleGetItem(func_2944_call(), 0)
call_4010 = relay.TupleGetItem(func_2945_call(), 0)
output = relay.Tuple([call_4009,])
output2 = relay.Tuple([call_4010,])
func_4011 = relay.Function([], output)
mod['func_4011'] = func_4011
mod = relay.transform.InferType()(mod)
mutated_mod['func_4011'] = func_4011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4011_call = mutated_mod.get_global_var('func_4011')
call_4012 = func_4011_call()
output = call_4012
func_4013 = relay.Function([], output)
mutated_mod['func_4013'] = func_4013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_4042 = relay.TupleGetItem(func_928_call(), 0)
call_4043 = relay.TupleGetItem(func_929_call(), 0)
func_2197_call = mod.get_global_var('func_2197')
func_2198_call = mutated_mod.get_global_var('func_2198')
call_4044 = relay.TupleGetItem(func_2197_call(), 0)
call_4045 = relay.TupleGetItem(func_2198_call(), 0)
func_3438_call = mod.get_global_var('func_3438')
func_3439_call = mutated_mod.get_global_var('func_3439')
call_4058 = func_3438_call()
call_4059 = func_3438_call()
func_2427_call = mod.get_global_var('func_2427')
func_2430_call = mutated_mod.get_global_var('func_2430')
var_4063 = relay.var("var_4063", dtype = "float64", shape = (600,))#candidate|4063|(600,)|var|float64
call_4062 = relay.TupleGetItem(func_2427_call(relay.reshape(var_4063.astype('float64'), [600,])), 2)
call_4064 = relay.TupleGetItem(func_2430_call(relay.reshape(var_4063.astype('float64'), [600,])), 2)
output = relay.Tuple([call_4042,call_4044,call_4058,call_4062,var_4063,])
output2 = relay.Tuple([call_4043,call_4045,call_4059,call_4064,var_4063,])
func_4066 = relay.Function([var_4063,], output)
mod['func_4066'] = func_4066
mod = relay.transform.InferType()(mod)
mutated_mod['func_4066'] = func_4066
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4067 = relay.var("var_4067", dtype = "float64", shape = (600,))#candidate|4067|(600,)|var|float64
func_4066_call = mutated_mod.get_global_var('func_4066')
call_4068 = func_4066_call(var_4067)
output = call_4068
func_4069 = relay.Function([var_4067], output)
mutated_mod['func_4069'] = func_4069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3464_call = mod.get_global_var('func_3464')
func_3466_call = mutated_mod.get_global_var('func_3466')
call_4153 = relay.TupleGetItem(func_3464_call(), 2)
call_4154 = relay.TupleGetItem(func_3466_call(), 2)
func_3981_call = mod.get_global_var('func_3981')
func_3983_call = mutated_mod.get_global_var('func_3983')
call_4161 = relay.TupleGetItem(func_3981_call(), 0)
call_4162 = relay.TupleGetItem(func_3983_call(), 0)
func_3934_call = mod.get_global_var('func_3934')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_4165 = relay.TupleGetItem(func_3934_call(), 0)
call_4166 = relay.TupleGetItem(func_3935_call(), 0)
func_2605_call = mod.get_global_var('func_2605')
func_2608_call = mutated_mod.get_global_var('func_2608')
var_4169 = relay.var("var_4169", dtype = "int8", shape = (260, 1))#candidate|4169|(260, 1)|var|int8
const_4170 = relay.const([[-3.354896,-2.535254,7.577831,7.376763],[1.707259,7.079199,-0.055702,-6.130409],[9.975149,7.913170,-2.558330,-2.632137]], dtype = "float64")#candidate|4170|(3, 4)|const|float64
call_4168 = relay.TupleGetItem(func_2605_call(relay.reshape(var_4169.astype('int8'), [13, 5, 4]), relay.reshape(const_4170.astype('float64'), [12,]), ), 0)
call_4171 = relay.TupleGetItem(func_2608_call(relay.reshape(var_4169.astype('int8'), [13, 5, 4]), relay.reshape(const_4170.astype('float64'), [12,]), ), 0)
uop_4205 = relay.acosh(call_4168.astype('float64')) # shape=(13, 5, 4)
uop_4207 = relay.acosh(call_4171.astype('float64')) # shape=(13, 5, 4)
uop_4211 = relay.atanh(uop_4205.astype('float32')) # shape=(13, 5, 4)
uop_4213 = relay.atanh(uop_4207.astype('float32')) # shape=(13, 5, 4)
uop_4222 = relay.log2(uop_4211.astype('float32')) # shape=(13, 5, 4)
uop_4224 = relay.log2(uop_4213.astype('float32')) # shape=(13, 5, 4)
bop_4228 = relay.mod(uop_4211.astype('float64'), relay.reshape(call_4168.astype('float64'), relay.shape_of(uop_4211))) # shape=(13, 5, 4)
bop_4231 = relay.mod(uop_4213.astype('float64'), relay.reshape(call_4171.astype('float64'), relay.shape_of(uop_4213))) # shape=(13, 5, 4)
output = relay.Tuple([call_4153,call_4161,call_4165,var_4169,const_4170,uop_4222,bop_4228,])
output2 = relay.Tuple([call_4154,call_4162,call_4166,var_4169,const_4170,uop_4224,bop_4231,])
func_4250 = relay.Function([var_4169,], output)
mod['func_4250'] = func_4250
mod = relay.transform.InferType()(mod)
mutated_mod['func_4250'] = func_4250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4251 = relay.var("var_4251", dtype = "int8", shape = (260, 1))#candidate|4251|(260, 1)|var|int8
func_4250_call = mutated_mod.get_global_var('func_4250')
call_4252 = func_4250_call(var_4251)
output = call_4252
func_4253 = relay.Function([var_4251], output)
mutated_mod['func_4253'] = func_4253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2757_call = mod.get_global_var('func_2757')
func_2758_call = mutated_mod.get_global_var('func_2758')
call_4255 = relay.TupleGetItem(func_2757_call(), 0)
call_4256 = relay.TupleGetItem(func_2758_call(), 0)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_4269 = relay.TupleGetItem(func_2808_call(), 2)
call_4270 = relay.TupleGetItem(func_2810_call(), 2)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_4271 = relay.TupleGetItem(func_1597_call(), 0)
call_4272 = relay.TupleGetItem(func_1599_call(), 0)
func_3197_call = mod.get_global_var('func_3197')
func_3199_call = mutated_mod.get_global_var('func_3199')
call_4273 = relay.TupleGetItem(func_3197_call(), 0)
call_4274 = relay.TupleGetItem(func_3199_call(), 0)
output = relay.Tuple([call_4255,call_4269,call_4271,call_4273,])
output2 = relay.Tuple([call_4256,call_4270,call_4272,call_4274,])
func_4275 = relay.Function([], output)
mod['func_4275'] = func_4275
mod = relay.transform.InferType()(mod)
output = func_4275()
func_4276 = relay.Function([], output)
mutated_mod['func_4276'] = func_4276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1921_call = mod.get_global_var('func_1921')
func_1922_call = mutated_mod.get_global_var('func_1922')
call_4286 = func_1921_call()
call_4287 = func_1921_call()
const_4307 = relay.const([[[-9,-9,-8,6],[5,-9,5,10],[1,-6,-6,8],[-8,-6,-8,-8],[-1,-2,5,9]],[[8,-6,-7,-2],[-8,3,-1,-8],[7,7,-6,-6],[3,10,-6,7],[6,4,-10,4]],[[-7,2,7,1],[5,-3,5,9],[-5,-8,-7,4],[-6,7,-9,6],[7,5,9,1]],[[-4,-4,-2,-8],[2,-8,9,-2],[-2,-3,-7,6],[8,-1,-9,-10],[5,-3,8,5]],[[-7,1,-7,-3],[2,-2,6,5],[1,-2,8,-3],[-7,-1,-10,-9],[1,3,4,9]],[[-1,-5,10,10],[7,4,-3,10],[5,-6,-10,-10],[-4,-9,8,-4],[-8,5,-10,1]],[[-6,-5,-2,-8],[8,2,9,-9],[6,3,5,-4],[-6,-4,3,-8],[-8,9,-9,7]],[[-2,-7,2,6],[-5,1,-4,-4],[-3,1,-4,6],[-1,4,-3,-1],[-1,-8,6,10]],[[-10,-1,5,7],[6,5,-6,-1],[-7,8,5,6],[8,8,5,5],[-8,-2,-2,2]],[[-8,5,9,10],[1,7,7,-10],[9,-9,6,2],[10,7,-4,9],[8,-5,-10,-3]],[[2,6,5,-2],[-4,9,-7,-3],[6,7,1,-3],[10,5,4,2],[2,-3,4,3]],[[8,-9,4,2],[-6,-3,6,7],[5,-7,-2,5],[7,-2,5,10],[-7,10,2,3]],[[-2,-6,-4,4],[7,-10,-2,-2],[5,1,-9,-5],[1,10,-9,5],[1,10,4,-9]],[[-5,9,-6,-8],[5,2,2,2],[5,9,5,5],[-5,3,9,10],[3,-1,10,-1]],[[-9,-1,-10,-6],[-5,9,9,7],[-9,5,4,-1],[-5,-5,4,-2],[-9,-3,7,4]]], dtype = "uint16")#candidate|4307|(15, 5, 4)|const|uint16
bop_4308 = relay.divide(call_4286.astype('float64'), const_4307.astype('float64')) # shape=(15, 5, 4)
bop_4311 = relay.divide(call_4287.astype('float64'), const_4307.astype('float64')) # shape=(15, 5, 4)
bop_4326 = relay.left_shift(bop_4308.astype('int64'), call_4286.astype('int64')) # shape=(15, 5, 4)
bop_4329 = relay.left_shift(bop_4311.astype('int64'), call_4287.astype('int64')) # shape=(15, 5, 4)
func_4275_call = mod.get_global_var('func_4275')
func_4276_call = mutated_mod.get_global_var('func_4276')
call_4330 = relay.TupleGetItem(func_4275_call(), 2)
call_4331 = relay.TupleGetItem(func_4276_call(), 2)
output = relay.Tuple([bop_4326,call_4330,])
output2 = relay.Tuple([bop_4329,call_4331,])
func_4344 = relay.Function([], output)
mod['func_4344'] = func_4344
mod = relay.transform.InferType()(mod)
output = func_4344()
func_4345 = relay.Function([], output)
mutated_mod['func_4345'] = func_4345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3904_call = mod.get_global_var('func_3904')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_4346 = func_3904_call()
call_4347 = func_3904_call()
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_4349 = relay.TupleGetItem(func_1716_call(), 1)
call_4350 = relay.TupleGetItem(func_1717_call(), 1)
func_3806_call = mod.get_global_var('func_3806')
func_3807_call = mutated_mod.get_global_var('func_3807')
call_4357 = relay.TupleGetItem(func_3806_call(), 0)
call_4358 = relay.TupleGetItem(func_3807_call(), 0)
output = relay.Tuple([call_4346,call_4349,call_4357,])
output2 = relay.Tuple([call_4347,call_4350,call_4358,])
func_4364 = relay.Function([], output)
mod['func_4364'] = func_4364
mod = relay.transform.InferType()(mod)
mutated_mod['func_4364'] = func_4364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mutated_mod.get_global_var('func_4364')
call_4365 = func_4364_call()
output = call_4365
func_4366 = relay.Function([], output)
mutated_mod['func_4366'] = func_4366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_929_call = mutated_mod.get_global_var('func_929')
call_4425 = relay.TupleGetItem(func_928_call(), 0)
call_4426 = relay.TupleGetItem(func_929_call(), 0)
output = relay.Tuple([call_4425,])
output2 = relay.Tuple([call_4426,])
func_4438 = relay.Function([], output)
mod['func_4438'] = func_4438
mod = relay.transform.InferType()(mod)
mutated_mod['func_4438'] = func_4438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mutated_mod.get_global_var('func_4438')
call_4439 = func_4438_call()
output = call_4439
func_4440 = relay.Function([], output)
mutated_mod['func_4440'] = func_4440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_4452 = relay.TupleGetItem(func_1597_call(), 0)
call_4453 = relay.TupleGetItem(func_1599_call(), 0)
func_4066_call = mod.get_global_var('func_4066')
func_4069_call = mutated_mod.get_global_var('func_4069')
var_4460 = relay.var("var_4460", dtype = "float64", shape = (600,))#candidate|4460|(600,)|var|float64
call_4459 = relay.TupleGetItem(func_4066_call(relay.reshape(var_4460.astype('float64'), [600,])), 3)
call_4461 = relay.TupleGetItem(func_4069_call(relay.reshape(var_4460.astype('float64'), [600,])), 3)
func_2885_call = mod.get_global_var('func_2885')
func_2887_call = mutated_mod.get_global_var('func_2887')
call_4468 = relay.TupleGetItem(func_2885_call(), 1)
call_4469 = relay.TupleGetItem(func_2887_call(), 1)
output = relay.Tuple([call_4452,call_4459,var_4460,call_4468,])
output2 = relay.Tuple([call_4453,call_4461,var_4460,call_4469,])
func_4475 = relay.Function([var_4460,], output)
mod['func_4475'] = func_4475
mod = relay.transform.InferType()(mod)
mutated_mod['func_4475'] = func_4475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4476 = relay.var("var_4476", dtype = "float64", shape = (600,))#candidate|4476|(600,)|var|float64
func_4475_call = mutated_mod.get_global_var('func_4475')
call_4477 = func_4475_call(var_4476)
output = call_4477
func_4478 = relay.Function([var_4476], output)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_4520 = relay.TupleGetItem(func_3507_call(), 0)
call_4521 = relay.TupleGetItem(func_3509_call(), 0)
func_2944_call = mod.get_global_var('func_2944')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_4528 = relay.TupleGetItem(func_2944_call(), 0)
call_4529 = relay.TupleGetItem(func_2945_call(), 0)
output = relay.Tuple([call_4520,call_4528,])
output2 = relay.Tuple([call_4521,call_4529,])
func_4543 = relay.Function([], output)
mod['func_4543'] = func_4543
mod = relay.transform.InferType()(mod)
mutated_mod['func_4543'] = func_4543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4543_call = mutated_mod.get_global_var('func_4543')
call_4544 = func_4543_call()
output = call_4544
func_4545 = relay.Function([], output)
mutated_mod['func_4545'] = func_4545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4543_call = mod.get_global_var('func_4543')
func_4545_call = mutated_mod.get_global_var('func_4545')
call_4570 = relay.TupleGetItem(func_4543_call(), 0)
call_4571 = relay.TupleGetItem(func_4545_call(), 0)
output = relay.Tuple([call_4570,])
output2 = relay.Tuple([call_4571,])
func_4572 = relay.Function([], output)
mod['func_4572'] = func_4572
mod = relay.transform.InferType()(mod)
output = func_4572()
func_4573 = relay.Function([], output)
mutated_mod['func_4573'] = func_4573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2682_call = mod.get_global_var('func_2682')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_4609 = relay.TupleGetItem(func_2682_call(), 0)
call_4610 = relay.TupleGetItem(func_2684_call(), 0)
const_4611 = relay.const([[[3.150525,-9.334933,1.471626,-9.273106],[-5.222357,-4.805645,-9.272855,2.618505],[-3.579313,2.184684,-7.646778,-7.447417],[-2.517521,4.187350,0.981108,8.161086],[6.936702,-6.558085,1.029303,-2.574563]],[[-7.817886,-6.253823,-6.850306,-4.363818],[-5.956860,-6.179910,-6.492300,2.457357],[-9.533292,-4.760806,6.705856,1.432180],[4.230980,0.101118,-6.086920,-0.875223],[8.557929,4.631610,4.319006,-6.887289]],[[3.228073,-9.378601,0.328058,7.476678],[-3.049153,-9.636402,6.129066,-0.514128],[1.851682,-1.241962,2.967112,-3.862314],[7.846446,-2.426618,5.795886,-1.868521],[4.224345,-4.765285,-3.391024,8.520511]],[[2.004066,-3.232446,6.145700,-0.692031],[9.008797,-7.504939,8.346016,2.519966],[-0.497508,8.855554,-1.204979,2.475026],[-9.085844,8.305280,3.253785,6.114335],[-5.377222,8.767644,-8.590749,-2.606267]],[[-7.054962,-2.369958,3.037366,-8.737336],[-7.358571,7.555993,-3.564347,-2.915664],[1.056882,1.520890,-3.725450,9.928589],[1.298712,-3.315061,-2.904602,0.242962],[4.883230,2.727718,2.178678,3.147686]],[[3.449841,-0.651073,5.174745,0.820799],[-7.171745,4.833323,5.678075,0.420014],[7.907104,7.967591,-7.521424,2.015550],[-2.296460,-2.568957,-5.539627,4.797805],[6.726096,6.494477,0.802038,0.479160]],[[-7.093218,-6.920567,3.227710,-0.489280],[-1.505942,2.910824,-1.256710,-8.497148],[5.178659,-5.932665,-0.365792,6.190547],[6.439751,-5.920438,2.386259,2.749622],[-5.489510,-2.348931,9.239523,6.356403]]], dtype = "float32")#candidate|4611|(7, 5, 4)|const|float32
bop_4612 = relay.minimum(call_4609.astype('uint64'), const_4611.astype('uint64')) # shape=(7, 5, 4)
bop_4615 = relay.minimum(call_4610.astype('uint64'), const_4611.astype('uint64')) # shape=(7, 5, 4)
output = relay.Tuple([bop_4612,])
output2 = relay.Tuple([bop_4615,])
func_4617 = relay.Function([], output)
mod['func_4617'] = func_4617
mod = relay.transform.InferType()(mod)
output = func_4617()
func_4618 = relay.Function([], output)
mutated_mod['func_4618'] = func_4618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mod.get_global_var('func_4438')
func_4440_call = mutated_mod.get_global_var('func_4440')
call_4643 = relay.TupleGetItem(func_4438_call(), 0)
call_4644 = relay.TupleGetItem(func_4440_call(), 0)
func_3806_call = mod.get_global_var('func_3806')
func_3807_call = mutated_mod.get_global_var('func_3807')
call_4646 = relay.TupleGetItem(func_3806_call(), 0)
call_4647 = relay.TupleGetItem(func_3807_call(), 0)
func_3438_call = mod.get_global_var('func_3438')
func_3439_call = mutated_mod.get_global_var('func_3439')
call_4669 = func_3438_call()
call_4670 = func_3438_call()
func_4066_call = mod.get_global_var('func_4066')
func_4069_call = mutated_mod.get_global_var('func_4069')
const_4683 = relay.const([9.016460,-6.966263,-3.569753,1.194467,8.638720,-4.382850,6.871746,-1.705692,6.415765,6.671491,-7.289034,5.323589,4.290739,-1.749308,6.108773,-1.427618,-4.023356,-4.527263,-0.078627,-0.437034,-7.403573,-8.298375,5.044471,4.990722,-8.585835,5.464986,9.604885,-5.564904,8.001266,0.215167,-2.665503,2.405258,0.636444,6.251221,9.301867,1.093144,-8.859095,0.216791,-7.374054,2.639222,8.934927,2.244085,4.396143,7.704444,-8.324864,7.620254,-4.552868,-7.485522,-8.510288,9.719468,1.633478,2.888758,-5.078726,7.988166,-0.148891,-5.840470,-0.848331,-6.485745,9.485313,-7.473256,-4.840519,-2.652346,-7.948734,-3.824404,9.142668,-6.058073,-0.292552,-5.713248,-1.651147,5.675733,-0.047568,-3.135071,-1.445974,-1.696198,-4.968614,8.914088,4.173861,1.333566,-8.241460,-5.578863,-4.190164,-2.126134,9.602537,8.214223,8.070451,-8.599030,-1.295152,-2.556771,9.432165,6.158231,1.728828,-3.539505,-8.967510,-5.911527,-2.031752,-6.226406,3.612358,9.042187,-7.282779,-6.981681,-6.909955,8.364224,0.704244,3.128494,7.629838,-7.692198,7.317702,5.027456,-1.674529,7.610881,-1.975681,0.388321,-9.785925,-2.582035,-8.951794,-4.199590,5.038890,7.712905,6.840763,8.895001,8.118002,5.776352,4.062851,5.826574,-4.084579,-6.852262,-6.175501,-8.918026,-0.013892,4.767167,0.580312,8.863921,-9.853575,1.070496,6.310215,-7.247024,-3.946605,-9.554810,-6.536604,-6.824718,-9.576650,2.013291,-0.573334,8.012655,0.454753,8.173267,9.915776,9.672016,-9.108401,3.440291,-4.156058,-1.919919,-2.949119,-7.230038,-8.333278,8.694755,0.487398,-8.285266,8.723380,-0.618313,-1.968378,9.133316,7.940761,3.281991,-0.235158,0.039315,-1.602415,1.650030,-3.220460,4.160004,-2.884895,4.744886,-9.265915,-7.990594,-9.261816,-2.524597,-9.639312,-5.850248,-5.572236,0.701450,-2.654584,5.782213,6.214071,7.888007,-0.283491,-3.253428,-6.352169,-6.626778,7.333944,-5.617426,-7.316650,5.682673,-9.355162,-0.869605,9.133885,5.514130,-7.051709,3.420663,-6.859414,-1.403729,2.524125,3.545147,-3.752758,-4.296446,-9.469414,6.234384,5.157753,-7.532187,-5.046437,8.728055,-2.203635,-8.815053,6.534075,-0.536567,-1.601206,3.570429,-0.665078,7.985149,-0.954077,-9.232416,-1.842211,2.327191,-0.351563,-3.966333,-0.338985,9.330930,-8.730201,-9.552281,6.282787,8.903543,3.973227,3.109847,-7.126483,-8.311110,6.375665,1.291809,3.971842,1.977213,-5.504585,-9.456693,2.306250,-3.156580,1.530893,-4.584540,4.287996,1.830529,-1.992440,-3.200852,6.341051,1.495003,-7.742211,1.052974,-7.679982,1.388790,-1.667726,7.351993,9.631400,5.637459,-7.372004,0.472611,-1.711460,-0.498065,-1.354645,3.394383,-9.368295,-7.475198,8.870173,-4.637206,-3.615881,6.715444,2.414382,9.568774,-8.614324,-2.617352,-9.641956,-8.464144,-4.214111,6.038627,-4.541475,-5.664200,6.836187,0.226112,-6.227844,-0.980806,7.617738,7.280486,1.347219,-1.522725,-1.408964,-4.905271,-6.595446,6.524645,-5.280775,9.822233,4.551159,9.563409,-4.771853,7.199489,-8.789187,-6.214706,6.077219,-6.761761,-6.726943,-9.086715,6.029118,4.133164,-5.371660,-1.561565,4.950762,2.554917,-5.487788,9.664202,5.973126,0.487913,2.266327,8.530879,-8.420726,8.550010,-8.495793,5.314290,-9.548887,-9.680623,6.864401,3.949353,-1.193718,4.474784,3.757279,-6.214471,1.584504,-6.178745,3.111035,-2.029311,-1.889993,-8.998948,0.854892,-1.540945,-2.174096,-4.257465,-7.681975,-9.070628,-9.843096,9.293700,-1.929204,-1.020921,4.233758,-8.980339,3.825308,-5.523391,-7.131772,-3.383611,-6.972182,-0.354188,3.613911,-5.399511,-1.044084,2.303841,-5.567525,0.935055,-5.443843,6.726941,-6.703108,-7.269086,-3.584943,2.196579,4.361169,-3.691874,2.731692,-5.985031,-7.865721,-1.478283,9.263720,9.238671,-8.262353,-4.198371,1.341741,-5.047209,-9.276875,5.095536,-4.483531,0.633977,-8.511636,1.376304,-7.033368,1.456652,8.010091,-8.698884,1.102930,-7.074817,-9.548023,-2.887009,-9.590698,3.912204,1.329491,3.403753,-3.575546,9.448551,9.264985,-4.761106,-9.648763,-0.520817,3.712674,-3.011575,-3.427690,-5.008930,3.562076,-7.690492,5.506805,-9.499146,-0.421914,-9.996106,0.968732,-5.787352,5.969283,-1.579688,-2.670473,7.797439,3.520615,-7.611678,-4.560799,-5.221013,1.823014,-3.765556,0.806945,7.103371,-8.219699,-9.580446,3.810116,-5.209543,6.719140,-8.666400,6.906909,4.905586,7.939956,6.129635,-9.990763,1.408076,-2.226127,-1.815581,3.317103,-4.139008,-8.678433,9.965903,8.921137,-9.571857,-0.912709,-4.489569,-9.122411,6.973283,1.432201,7.170591,-5.442503,4.452864,-0.070988,-9.830006,6.125268,-5.292917,3.619636,3.885664,4.981995,9.710368,-3.518931,-6.266100,6.827411,-3.212704,-8.803318,-3.164699,-8.323498,2.578028,-5.171631,-9.277141,-3.314463,0.002952,-1.819541,-8.586599,-5.715400,-6.341871,5.972440,0.398110,-0.078326,5.605324,8.559408,5.342838,1.245584,4.168806,5.160362,1.268871,-0.605480,7.582506,7.849548,-5.256365,-8.008368,-1.564769,4.814854,-5.674584,0.489567,-9.560464,-0.797516,5.307796,0.594586,6.955795,-1.954575,-0.691256,0.315738,-4.206692,-9.131572,-7.670862,1.210360,-2.639248,-8.631729,-1.859400,1.247214,-0.029677,-1.408933,6.338942,-5.226127,-3.846754,-5.880812,9.242236,3.588832,-1.637724,0.259622,-2.426183,-8.462623,6.748525,6.305628,-0.469481,5.377508,-3.107385,-4.844877,8.147697,-9.381618,-6.622532,-5.015070,-1.306082,7.768862,2.927569,6.458616,7.658876,6.551261,-3.670729,-3.059536,2.190312,-3.515321,9.148478,3.593141,2.089174,0.247527,-4.180366,-4.287888,9.455453,-6.988462,-6.095377,-4.256687,3.612733,-8.227345,-9.573632,-6.401698,-3.049437,-9.573382,-2.023621,-1.127645,3.841203,1.248609,-8.033312,5.644297,3.061131,-6.341897,1.443852,2.818432,-3.398765,0.814524,-6.469883,-8.791754,-5.862050,-1.028708,3.542141,-4.364818,-3.757926,-2.983572,6.551908,-6.478482,2.618238,-3.849467,6.577028,7.657953,-2.830346,9.380517,5.015746,6.611918,-5.054569,-9.054461,6.776531,-3.909604,-2.060578,-6.733840,-9.799534,-9.422167,0.749960,8.310015,-2.324778], dtype = "float64")#candidate|4683|(600,)|const|float64
call_4682 = relay.TupleGetItem(func_4066_call(relay.reshape(const_4683.astype('float64'), [600,])), 4)
call_4684 = relay.TupleGetItem(func_4069_call(relay.reshape(const_4683.astype('float64'), [600,])), 4)
var_4687 = relay.var("var_4687", dtype = "int8", shape = (7, 5, 4))#candidate|4687|(7, 5, 4)|var|int8
bop_4688 = relay.logical_xor(call_4643.astype('uint64'), var_4687.astype('uint64')) # shape=(7, 5, 4)
bop_4691 = relay.logical_xor(call_4644.astype('uint64'), var_4687.astype('uint64')) # shape=(7, 5, 4)
output = relay.Tuple([call_4646,call_4669,call_4682,const_4683,bop_4688,])
output2 = relay.Tuple([call_4647,call_4670,call_4684,const_4683,bop_4691,])
func_4694 = relay.Function([var_4687,], output)
mod['func_4694'] = func_4694
mod = relay.transform.InferType()(mod)
mutated_mod['func_4694'] = func_4694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4695 = relay.var("var_4695", dtype = "int8", shape = (7, 5, 4))#candidate|4695|(7, 5, 4)|var|int8
func_4694_call = mutated_mod.get_global_var('func_4694')
call_4696 = func_4694_call(var_4695)
output = call_4696
func_4697 = relay.Function([var_4695], output)
mutated_mod['func_4697'] = func_4697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mod.get_global_var('func_4438')
func_4440_call = mutated_mod.get_global_var('func_4440')
call_4705 = relay.TupleGetItem(func_4438_call(), 0)
call_4706 = relay.TupleGetItem(func_4440_call(), 0)
output = relay.Tuple([call_4705,])
output2 = relay.Tuple([call_4706,])
func_4716 = relay.Function([], output)
mod['func_4716'] = func_4716
mod = relay.transform.InferType()(mod)
mutated_mod['func_4716'] = func_4716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4716_call = mutated_mod.get_global_var('func_4716')
call_4717 = func_4716_call()
output = call_4717
func_4718 = relay.Function([], output)
mutated_mod['func_4718'] = func_4718
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4743 = relay.var("var_4743", dtype = "uint32", shape = (4, 15, 6))#candidate|4743|(4, 15, 6)|var|uint32
const_4744 = relay.const([[[-3,2,-2,-6,-7,-3],[5,-8,-10,10,3,8],[3,10,-6,2,10,5],[9,4,4,9,-3,-4],[7,-10,2,-6,7,9],[-8,5,6,-2,3,1],[5,7,-8,2,4,8],[1,-3,1,-6,-2,9],[-2,5,6,1,7,-9],[6,10,5,-8,-3,7],[-10,3,3,-1,2,8],[-3,9,-6,3,-2,-6],[3,5,2,10,-4,-7],[2,10,6,-3,-9,-7],[3,-9,-4,-5,-8,5]],[[-2,-3,7,-1,-7,-2],[-3,10,-7,6,-8,8],[1,-3,2,8,-4,-10],[8,9,-4,-8,5,-8],[-8,6,-1,-10,-8,1],[2,5,10,-6,-7,-6],[5,10,4,6,-4,8],[5,-8,-2,4,-8,-9],[-2,-7,-1,4,6,7],[1,2,4,-9,-7,-3],[-7,10,-5,4,-7,8],[3,-3,5,-9,-3,-2],[-8,-9,9,1,-10,1],[-3,3,-7,5,5,9],[9,-6,8,3,-8,-2]],[[-4,-5,5,10,-3,7],[5,10,-1,2,8,4],[6,3,-10,3,7,10],[5,1,4,8,1,3],[-8,3,3,-3,7,-6],[-10,-4,-8,10,-6,-1],[-10,-2,-8,6,-10,-3],[8,-3,-3,-3,10,9],[-2,1,-1,-10,3,3],[-7,-9,-8,9,10,1],[2,6,3,-2,-6,5],[-7,-8,7,4,-8,8],[-7,10,-10,3,-6,8],[8,-4,-4,2,4,-4],[9,4,10,1,-10,7]],[[5,3,-10,-1,-10,-3],[-6,6,2,10,7,-9],[7,-6,-5,8,-4,-9],[4,3,7,-8,8,2],[5,1,7,3,-2,-10],[4,4,10,4,-7,8],[10,6,2,-10,-1,3],[3,-1,-6,1,-8,-10],[2,2,9,-3,6,1],[-9,-6,-3,8,4,-2],[-10,-2,10,9,-6,-3],[-9,-7,8,-4,8,9],[9,-9,9,-7,4,9],[1,-8,-9,3,-7,-4],[10,-2,-7,2,-8,-1]]], dtype = "uint32")#candidate|4744|(4, 15, 6)|const|uint32
bop_4745 = relay.multiply(var_4743.astype('uint32'), relay.reshape(const_4744.astype('uint32'), relay.shape_of(var_4743))) # shape=(4, 15, 6)
func_887_call = mod.get_global_var('func_887')
func_890_call = mutated_mod.get_global_var('func_890')
const_4752 = relay.const([[-3.136510,-6.558622],[-3.374215,7.675101],[-5.761914,2.657720],[-7.841788,1.640605],[2.963020,-7.710767],[4.403423,-0.063878]], dtype = "float64")#candidate|4752|(6, 2)|const|float64
call_4751 = relay.TupleGetItem(func_887_call(relay.reshape(const_4752.astype('float64'), [12,])), 2)
call_4753 = relay.TupleGetItem(func_890_call(relay.reshape(const_4752.astype('float64'), [12,])), 2)
uop_4767 = relay.acos(bop_4745.astype('float32')) # shape=(4, 15, 6)
output = relay.Tuple([call_4751,const_4752,uop_4767,])
output2 = relay.Tuple([call_4753,const_4752,uop_4767,])
func_4776 = relay.Function([var_4743,], output)
mod['func_4776'] = func_4776
mod = relay.transform.InferType()(mod)
mutated_mod['func_4776'] = func_4776
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4777 = relay.var("var_4777", dtype = "uint32", shape = (4, 15, 6))#candidate|4777|(4, 15, 6)|var|uint32
func_4776_call = mutated_mod.get_global_var('func_4776')
call_4778 = func_4776_call(var_4777)
output = call_4778
func_4779 = relay.Function([var_4777], output)
mutated_mod['func_4779'] = func_4779
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4788 = relay.var("var_4788", dtype = "int16", shape = (1, 2, 1))#candidate|4788|(1, 2, 1)|var|int16
var_4789 = relay.var("var_4789", dtype = "int16", shape = (7, 2, 16))#candidate|4789|(7, 2, 16)|var|int16
bop_4790 = relay.maximum(var_4788.astype('int16'), var_4789.astype('int16')) # shape=(7, 2, 16)
bop_4806 = relay.multiply(bop_4790.astype('int64'), var_4788.astype('int64')) # shape=(7, 2, 16)
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_4810 = relay.TupleGetItem(func_849_call(), 0)
call_4811 = relay.TupleGetItem(func_851_call(), 0)
bop_4813 = relay.right_shift(bop_4790.astype('int8'), var_4788.astype('int8')) # shape=(7, 2, 16)
uop_4818 = relay.acosh(var_4788.astype('float64')) # shape=(1, 2, 1)
output = relay.Tuple([bop_4806,call_4810,bop_4813,uop_4818,])
output2 = relay.Tuple([bop_4806,call_4811,bop_4813,uop_4818,])
func_4826 = relay.Function([var_4788,var_4789,], output)
mod['func_4826'] = func_4826
mod = relay.transform.InferType()(mod)
mutated_mod['func_4826'] = func_4826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4826_call = mutated_mod.get_global_var('func_4826')
var_4828 = relay.var("var_4828", dtype = "int16", shape = (1, 2, 1))#candidate|4828|(1, 2, 1)|var|int16
var_4829 = relay.var("var_4829", dtype = "int16", shape = (7, 2, 16))#candidate|4829|(7, 2, 16)|var|int16
call_4827 = func_4826_call(var_4828,var_4829,)
output = call_4827
func_4830 = relay.Function([var_4828,var_4829,], output)
mutated_mod['func_4830'] = func_4830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4716_call = mod.get_global_var('func_4716')
func_4718_call = mutated_mod.get_global_var('func_4718')
call_4840 = relay.TupleGetItem(func_4716_call(), 0)
call_4841 = relay.TupleGetItem(func_4718_call(), 0)
func_1213_call = mod.get_global_var('func_1213')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_4873 = relay.TupleGetItem(func_1213_call(), 0)
call_4874 = relay.TupleGetItem(func_1215_call(), 0)
var_4878 = relay.var("var_4878", dtype = "float32", shape = (2, 5, 4))#candidate|4878|(2, 5, 4)|var|float32
bop_4879 = relay.right_shift(call_4873.astype('uint16'), var_4878.astype('uint16')) # shape=(2, 5, 4)
bop_4882 = relay.right_shift(call_4874.astype('uint16'), var_4878.astype('uint16')) # shape=(2, 5, 4)
output = relay.Tuple([call_4840,bop_4879,])
output2 = relay.Tuple([call_4841,bop_4882,])
func_4885 = relay.Function([var_4878,], output)
mod['func_4885'] = func_4885
mod = relay.transform.InferType()(mod)
var_4886 = relay.var("var_4886", dtype = "float32", shape = (2, 5, 4))#candidate|4886|(2, 5, 4)|var|float32
output = func_4885(var_4886)
func_4887 = relay.Function([var_4886], output)
mutated_mod['func_4887'] = func_4887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3904_call = mod.get_global_var('func_3904')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_4892 = func_3904_call()
call_4893 = func_3904_call()
func_4475_call = mod.get_global_var('func_4475')
func_4478_call = mutated_mod.get_global_var('func_4478')
var_4900 = relay.var("var_4900", dtype = "float64", shape = (600,))#candidate|4900|(600,)|var|float64
call_4899 = relay.TupleGetItem(func_4475_call(relay.reshape(var_4900.astype('float64'), [600,])), 2)
call_4901 = relay.TupleGetItem(func_4478_call(relay.reshape(var_4900.astype('float64'), [600,])), 2)
output = relay.Tuple([call_4892,call_4899,var_4900,])
output2 = relay.Tuple([call_4893,call_4901,var_4900,])
func_4905 = relay.Function([var_4900,], output)
mod['func_4905'] = func_4905
mod = relay.transform.InferType()(mod)
var_4906 = relay.var("var_4906", dtype = "float64", shape = (600,))#candidate|4906|(600,)|var|float64
output = func_4905(var_4906)
func_4907 = relay.Function([var_4906], output)
mutated_mod['func_4907'] = func_4907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mod.get_global_var('func_4438')
func_4440_call = mutated_mod.get_global_var('func_4440')
call_4918 = relay.TupleGetItem(func_4438_call(), 0)
call_4919 = relay.TupleGetItem(func_4440_call(), 0)
func_3099_call = mod.get_global_var('func_3099')
func_3101_call = mutated_mod.get_global_var('func_3101')
call_4926 = relay.TupleGetItem(func_3099_call(), 2)
call_4927 = relay.TupleGetItem(func_3101_call(), 2)
func_1888_call = mod.get_global_var('func_1888')
func_1891_call = mutated_mod.get_global_var('func_1891')
var_4929 = relay.var("var_4929", dtype = "uint64", shape = (1, 240))#candidate|4929|(1, 240)|var|uint64
call_4928 = relay.TupleGetItem(func_1888_call(relay.reshape(var_4929.astype('uint64'), [12, 5, 4])), 1)
call_4930 = relay.TupleGetItem(func_1891_call(relay.reshape(var_4929.astype('uint64'), [12, 5, 4])), 1)
func_3705_call = mod.get_global_var('func_3705')
func_3707_call = mutated_mod.get_global_var('func_3707')
var_4937 = relay.var("var_4937", dtype = "float64", shape = (12,))#candidate|4937|(12,)|var|float64
call_4936 = relay.TupleGetItem(func_3705_call(relay.reshape(var_4937.astype('float64'), [12,])), 0)
call_4938 = relay.TupleGetItem(func_3707_call(relay.reshape(var_4937.astype('float64'), [12,])), 0)
func_4344_call = mod.get_global_var('func_4344')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_4939 = relay.TupleGetItem(func_4344_call(), 0)
call_4940 = relay.TupleGetItem(func_4345_call(), 0)
output = relay.Tuple([call_4918,call_4926,call_4928,var_4929,call_4936,var_4937,call_4939,])
output2 = relay.Tuple([call_4919,call_4927,call_4930,var_4929,call_4938,var_4937,call_4940,])
func_4941 = relay.Function([var_4929,var_4937,], output)
mod['func_4941'] = func_4941
mod = relay.transform.InferType()(mod)
var_4942 = relay.var("var_4942", dtype = "uint64", shape = (1, 240))#candidate|4942|(1, 240)|var|uint64
var_4943 = relay.var("var_4943", dtype = "float64", shape = (12,))#candidate|4943|(12,)|var|float64
output = func_4941(var_4942,var_4943,)
func_4944 = relay.Function([var_4942,var_4943,], output)
mutated_mod['func_4944'] = func_4944
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5001 = relay.var("var_5001", dtype = "float32", shape = (16, 12, 4))#candidate|5001|(16, 12, 4)|var|float32
uop_5002 = relay.exp(var_5001.astype('float32')) # shape=(16, 12, 4)
uop_5023 = relay.acosh(var_5001.astype('float32')) # shape=(16, 12, 4)
output = relay.Tuple([uop_5002,uop_5023,])
output2 = relay.Tuple([uop_5002,uop_5023,])
func_5025 = relay.Function([var_5001,], output)
mod['func_5025'] = func_5025
mod = relay.transform.InferType()(mod)
var_5026 = relay.var("var_5026", dtype = "float32", shape = (16, 12, 4))#candidate|5026|(16, 12, 4)|var|float32
output = func_5025(var_5026)
func_5027 = relay.Function([var_5026], output)
mutated_mod['func_5027'] = func_5027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3934_call = mod.get_global_var('func_3934')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_5046 = relay.TupleGetItem(func_3934_call(), 0)
call_5047 = relay.TupleGetItem(func_3935_call(), 0)
output = relay.Tuple([call_5046,])
output2 = relay.Tuple([call_5047,])
func_5048 = relay.Function([], output)
mod['func_5048'] = func_5048
mod = relay.transform.InferType()(mod)
output = func_5048()
func_5049 = relay.Function([], output)
mutated_mod['func_5049'] = func_5049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mod.get_global_var('func_4364')
func_4366_call = mutated_mod.get_global_var('func_4366')
call_5050 = relay.TupleGetItem(func_4364_call(), 1)
call_5051 = relay.TupleGetItem(func_4366_call(), 1)
output = relay.Tuple([call_5050,])
output2 = relay.Tuple([call_5051,])
func_5055 = relay.Function([], output)
mod['func_5055'] = func_5055
mod = relay.transform.InferType()(mod)
output = func_5055()
func_5056 = relay.Function([], output)
mutated_mod['func_5056'] = func_5056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5095 = relay.var("var_5095", dtype = "float32", shape = (13, 1, 3))#candidate|5095|(13, 1, 3)|var|float32
var_5096 = relay.var("var_5096", dtype = "float32", shape = (13, 6, 3))#candidate|5096|(13, 6, 3)|var|float32
bop_5097 = relay.floor_divide(var_5095.astype('float32'), var_5096.astype('float32')) # shape=(13, 6, 3)
output = relay.Tuple([bop_5097,])
output2 = relay.Tuple([bop_5097,])
func_5102 = relay.Function([var_5095,var_5096,], output)
mod['func_5102'] = func_5102
mod = relay.transform.InferType()(mod)
mutated_mod['func_5102'] = func_5102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5102_call = mutated_mod.get_global_var('func_5102')
var_5104 = relay.var("var_5104", dtype = "float32", shape = (13, 1, 3))#candidate|5104|(13, 1, 3)|var|float32
var_5105 = relay.var("var_5105", dtype = "float32", shape = (13, 6, 3))#candidate|5105|(13, 6, 3)|var|float32
call_5103 = func_5102_call(var_5104,var_5105,)
output = call_5103
func_5106 = relay.Function([var_5104,var_5105,], output)
mutated_mod['func_5106'] = func_5106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4543_call = mod.get_global_var('func_4543')
func_4545_call = mutated_mod.get_global_var('func_4545')
call_5117 = relay.TupleGetItem(func_4543_call(), 1)
call_5118 = relay.TupleGetItem(func_4545_call(), 1)
uop_5124 = relay.sqrt(call_5117.astype('float64')) # shape=(6, 5, 4)
uop_5126 = relay.sqrt(call_5118.astype('float64')) # shape=(6, 5, 4)
func_887_call = mod.get_global_var('func_887')
func_890_call = mutated_mod.get_global_var('func_890')
const_5128 = relay.const([[6.914543,-2.754799,3.577346,-2.175135],[-1.282168,8.634717,6.606179,1.711165],[-6.398510,-1.584680,9.740801,7.072428]], dtype = "float64")#candidate|5128|(3, 4)|const|float64
call_5127 = relay.TupleGetItem(func_887_call(relay.reshape(const_5128.astype('float64'), [12,])), 1)
call_5129 = relay.TupleGetItem(func_890_call(relay.reshape(const_5128.astype('float64'), [12,])), 1)
output = relay.Tuple([uop_5124,call_5127,const_5128,])
output2 = relay.Tuple([uop_5126,call_5129,const_5128,])
func_5131 = relay.Function([], output)
mod['func_5131'] = func_5131
mod = relay.transform.InferType()(mod)
mutated_mod['func_5131'] = func_5131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5131_call = mutated_mod.get_global_var('func_5131')
call_5132 = func_5131_call()
output = call_5132
func_5133 = relay.Function([], output)
mutated_mod['func_5133'] = func_5133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2524_call = mod.get_global_var('func_2524')
func_2525_call = mutated_mod.get_global_var('func_2525')
call_5172 = func_2524_call()
call_5173 = func_2524_call()
output = relay.Tuple([call_5172,])
output2 = relay.Tuple([call_5173,])
func_5177 = relay.Function([], output)
mod['func_5177'] = func_5177
mod = relay.transform.InferType()(mod)
mutated_mod['func_5177'] = func_5177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5177_call = mutated_mod.get_global_var('func_5177')
call_5178 = func_5177_call()
output = call_5178
func_5179 = relay.Function([], output)
mutated_mod['func_5179'] = func_5179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1921_call = mod.get_global_var('func_1921')
func_1922_call = mutated_mod.get_global_var('func_1922')
call_5209 = func_1921_call()
call_5210 = func_1921_call()
func_4344_call = mod.get_global_var('func_4344')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_5225 = relay.TupleGetItem(func_4344_call(), 0)
call_5226 = relay.TupleGetItem(func_4345_call(), 0)
func_3037_call = mod.get_global_var('func_3037')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_5228 = relay.TupleGetItem(func_3037_call(), 0)
call_5229 = relay.TupleGetItem(func_3038_call(), 0)
func_1213_call = mod.get_global_var('func_1213')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_5231 = relay.TupleGetItem(func_1213_call(), 0)
call_5232 = relay.TupleGetItem(func_1215_call(), 0)
output = relay.Tuple([call_5209,call_5225,call_5228,call_5231,])
output2 = relay.Tuple([call_5210,call_5226,call_5229,call_5232,])
func_5239 = relay.Function([], output)
mod['func_5239'] = func_5239
mod = relay.transform.InferType()(mod)
mutated_mod['func_5239'] = func_5239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5239_call = mutated_mod.get_global_var('func_5239')
call_5240 = func_5239_call()
output = call_5240
func_5241 = relay.Function([], output)
mutated_mod['func_5241'] = func_5241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_5247 = relay.TupleGetItem(func_1397_call(), 1)
call_5248 = relay.TupleGetItem(func_1399_call(), 1)
output = call_5247
output2 = call_5248
func_5287 = relay.Function([], output)
mod['func_5287'] = func_5287
mod = relay.transform.InferType()(mod)
mutated_mod['func_5287'] = func_5287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5287_call = mutated_mod.get_global_var('func_5287')
call_5288 = func_5287_call()
output = call_5288
func_5289 = relay.Function([], output)
mutated_mod['func_5289'] = func_5289
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5308 = relay.var("var_5308", dtype = "float32", shape = (3, 14, 2))#candidate|5308|(3, 14, 2)|var|float32
uop_5309 = relay.log10(var_5308.astype('float32')) # shape=(3, 14, 2)
output = uop_5309
output2 = uop_5309
func_5316 = relay.Function([var_5308,], output)
mod['func_5316'] = func_5316
mod = relay.transform.InferType()(mod)
var_5317 = relay.var("var_5317", dtype = "float32", shape = (3, 14, 2))#candidate|5317|(3, 14, 2)|var|float32
output = func_5316(var_5317)
func_5318 = relay.Function([var_5317], output)
mutated_mod['func_5318'] = func_5318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3806_call = mod.get_global_var('func_3806')
func_3807_call = mutated_mod.get_global_var('func_3807')
call_5327 = relay.TupleGetItem(func_3806_call(), 0)
call_5328 = relay.TupleGetItem(func_3807_call(), 0)
output = call_5327
output2 = call_5328
func_5341 = relay.Function([], output)
mod['func_5341'] = func_5341
mod = relay.transform.InferType()(mod)
mutated_mod['func_5341'] = func_5341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5341_call = mutated_mod.get_global_var('func_5341')
call_5342 = func_5341_call()
output = call_5342
func_5343 = relay.Function([], output)
mutated_mod['func_5343'] = func_5343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mod.get_global_var('func_2921')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_5368 = relay.TupleGetItem(func_2921_call(), 0)
call_5369 = relay.TupleGetItem(func_2922_call(), 0)
func_3418_call = mod.get_global_var('func_3418')
func_3420_call = mutated_mod.get_global_var('func_3420')
const_5376 = relay.const([-4,1,-4,8,-3,3,7,3,2,-3,6,-10,-2,-2,-4,3,-10,9,1,3,8,-9,8,10,-9,4,-9,-4,5,-7,3,-8,8,-8,-3,-3,9,-5,2,-6,8,-6,-6,1,6,-2,-10,3,-6,-7,2,-1,1,-7,-3,6,4,-10,4,-2,9,-1,-4,9,5,-10,-7,7,5,3,-6,-9,2,-1,-3,9,8,-3,6,2,-9,8,1,5,9,6,-8,-6,-8,-9,1,-3,9,9,7,5,-4,-3,8,5], dtype = "int8")#candidate|5376|(100,)|const|int8
call_5375 = relay.TupleGetItem(func_3418_call(relay.reshape(const_5376.astype('int8'), [100,])), 3)
call_5377 = relay.TupleGetItem(func_3420_call(relay.reshape(const_5376.astype('int8'), [100,])), 3)
output = relay.Tuple([call_5368,call_5375,const_5376,])
output2 = relay.Tuple([call_5369,call_5377,const_5376,])
func_5396 = relay.Function([], output)
mod['func_5396'] = func_5396
mod = relay.transform.InferType()(mod)
mutated_mod['func_5396'] = func_5396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5396_call = mutated_mod.get_global_var('func_5396')
call_5397 = func_5396_call()
output = call_5397
func_5398 = relay.Function([], output)
mutated_mod['func_5398'] = func_5398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4275_call = mod.get_global_var('func_4275')
func_4276_call = mutated_mod.get_global_var('func_4276')
call_5403 = relay.TupleGetItem(func_4275_call(), 2)
call_5404 = relay.TupleGetItem(func_4276_call(), 2)
func_4572_call = mod.get_global_var('func_4572')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_5413 = relay.TupleGetItem(func_4572_call(), 0)
call_5414 = relay.TupleGetItem(func_4573_call(), 0)
output = relay.Tuple([call_5403,call_5413,])
output2 = relay.Tuple([call_5404,call_5414,])
func_5426 = relay.Function([], output)
mod['func_5426'] = func_5426
mod = relay.transform.InferType()(mod)
mutated_mod['func_5426'] = func_5426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5426_call = mutated_mod.get_global_var('func_5426')
call_5427 = func_5426_call()
output = call_5427
func_5428 = relay.Function([], output)
mutated_mod['func_5428'] = func_5428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_811_call = mod.get_global_var('func_811')
func_812_call = mutated_mod.get_global_var('func_812')
call_5455 = func_811_call()
call_5456 = func_811_call()
output = relay.Tuple([call_5455,])
output2 = relay.Tuple([call_5456,])
func_5508 = relay.Function([], output)
mod['func_5508'] = func_5508
mod = relay.transform.InferType()(mod)
output = func_5508()
func_5509 = relay.Function([], output)
mutated_mod['func_5509'] = func_5509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2312_call = mod.get_global_var('func_2312')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_5576 = relay.TupleGetItem(func_2312_call(), 0)
call_5577 = relay.TupleGetItem(func_2313_call(), 0)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_5583 = func_1270_call()
call_5584 = func_1270_call()
output = relay.Tuple([call_5576,call_5583,])
output2 = relay.Tuple([call_5577,call_5584,])
func_5585 = relay.Function([], output)
mod['func_5585'] = func_5585
mod = relay.transform.InferType()(mod)
mutated_mod['func_5585'] = func_5585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5585_call = mutated_mod.get_global_var('func_5585')
call_5586 = func_5585_call()
output = call_5586
func_5587 = relay.Function([], output)
mutated_mod['func_5587'] = func_5587
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5608 = relay.var("var_5608", dtype = "float32", shape = (13, 10, 8))#candidate|5608|(13, 10, 8)|var|float32
uop_5609 = relay.log(var_5608.astype('float32')) # shape=(13, 10, 8)
var_5620 = relay.var("var_5620", dtype = "float32", shape = (13, 10, 8))#candidate|5620|(13, 10, 8)|var|float32
bop_5621 = relay.minimum(uop_5609.astype('int64'), relay.reshape(var_5620.astype('int64'), relay.shape_of(uop_5609))) # shape=(13, 10, 8)
func_3037_call = mod.get_global_var('func_3037')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_5645 = relay.TupleGetItem(func_3037_call(), 0)
call_5646 = relay.TupleGetItem(func_3038_call(), 0)
bop_5658 = relay.power(uop_5609.astype('float64'), relay.reshape(var_5620.astype('float64'), relay.shape_of(uop_5609))) # shape=(13, 10, 8)
func_3789_call = mod.get_global_var('func_3789')
func_3793_call = mutated_mod.get_global_var('func_3793')
const_5670 = relay.const([-5.188909,2.701217,-0.246212,9.894724,-1.720036,-4.004761,7.073288,-7.704476,5.801022,2.188903,-9.500006,-9.800609,8.338358,7.315777,-4.613221,-3.258703,3.195346,-4.426944,-8.354557,-6.269732,8.991009,2.282596,-4.263380,-9.782804,2.323145,7.857395,-5.944049,-4.231669,2.137465,-6.059238,6.040450,6.727904,-5.858108,-5.719125,4.800891,9.699828,5.095061,3.233537,-7.387726,-0.008609,-9.961361,5.591609,7.455555,-4.035926,0.956110,-2.897395,0.899190,6.357498,1.087210,7.377299,8.752095,-6.945795,2.396460,-0.295322,3.423653,6.590999,0.372887,-2.678577,2.502194,6.261280,6.653818,4.387024,6.909488,6.033805,4.965518,-1.189618,4.756242,8.287494,-6.734823,4.901300,-8.732610,5.005645,0.072448,-9.094091,0.747103,-3.550832,1.681371,1.638463,-4.771128,-7.906596,5.244502,-0.048235,1.006696,-2.988513,-2.236638,4.130983,-6.796178,-5.152120,7.692498,-1.848385,-7.172045,7.076603,0.003885,8.085567,0.821221,4.169263,-7.997002,-5.528143,1.671156,3.653907,-3.382200,7.052145,-7.885118,-6.644194,-5.859212,-1.476051,2.194431,9.431026,-8.467837,1.967570,-0.530250,2.182300,-2.940275,-3.856180,-7.855779,6.399423,-6.733176,6.787403,-8.367385,-9.890186,5.266400,-0.512495,2.194652,1.972673,-4.766337,0.683402,2.663329,9.080603,-4.651611,4.104923,1.181328,5.110265,7.449895,-9.886192,6.058067,8.712883,5.963215,3.515239,7.737035,7.193481,5.849200,-1.425848,9.056497,2.380438,8.361580,-3.187541,2.574044,-8.664777,-5.905556,3.042931,-1.787836,-4.817507,-9.501206,-7.796763,-4.748961,8.310009,-5.244053,-9.837641,8.266900,-1.573645,2.076158,8.882336,-6.225017,1.610490,3.127668,-8.562532,9.924970,1.608163,3.560699,0.564717,8.093986,5.360434,-7.854265,6.265864,1.611660,-8.869159,-8.713379,-9.579379,-1.489741,-6.249822,-2.895209,9.947886,0.422033,6.396479,-4.326897,7.414822,5.322449,9.030946,-5.700359,7.618357,-8.507779,-3.265757,6.224143,-4.739318,8.982190,1.928450,3.001308,5.398704,-6.270429,7.465596], dtype = "float32")#candidate|5670|(200,)|const|float32
var_5671 = relay.var("var_5671", dtype = "int8", shape = (100,))#candidate|5671|(100,)|var|int8
call_5669 = relay.TupleGetItem(func_3789_call(relay.reshape(const_5670.astype('float32'), [200,]), relay.reshape(var_5671.astype('int8'), [100,]), ), 6)
call_5672 = relay.TupleGetItem(func_3793_call(relay.reshape(const_5670.astype('float32'), [200,]), relay.reshape(var_5671.astype('int8'), [100,]), ), 6)
func_1921_call = mod.get_global_var('func_1921')
func_1922_call = mutated_mod.get_global_var('func_1922')
call_5677 = func_1921_call()
call_5678 = func_1921_call()
output = relay.Tuple([bop_5621,call_5645,bop_5658,call_5669,const_5670,var_5671,call_5677,])
output2 = relay.Tuple([bop_5621,call_5646,bop_5658,call_5672,const_5670,var_5671,call_5678,])
func_5679 = relay.Function([var_5608,var_5620,var_5671,], output)
mod['func_5679'] = func_5679
mod = relay.transform.InferType()(mod)
mutated_mod['func_5679'] = func_5679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5679_call = mutated_mod.get_global_var('func_5679')
var_5681 = relay.var("var_5681", dtype = "float32", shape = (13, 10, 8))#candidate|5681|(13, 10, 8)|var|float32
var_5682 = relay.var("var_5682", dtype = "float32", shape = (13, 10, 8))#candidate|5682|(13, 10, 8)|var|float32
var_5683 = relay.var("var_5683", dtype = "int8", shape = (100,))#candidate|5683|(100,)|var|int8
call_5680 = func_5679_call(var_5681,var_5682,var_5683,)
output = call_5680
func_5684 = relay.Function([var_5681,var_5682,var_5683,], output)
mutated_mod['func_5684'] = func_5684
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5718 = relay.var("var_5718", dtype = "int16", shape = (8, 3, 16))#candidate|5718|(8, 3, 16)|var|int16
const_5719 = relay.const([[[-9,-5,-8,3,-5,-3,-2,4,6,-8,10,7,-1,-6,3,4],[8,10,-4,-10,-7,1,7,-9,-5,-1,2,2,6,-2,9,-9],[-5,5,-2,-8,7,-10,7,5,-8,-8,8,-4,9,-1,1,-5]],[[9,-6,2,3,5,4,-5,-5,-9,3,-2,10,-2,10,-3,10],[5,-4,-1,-8,10,-10,3,10,-10,-9,-10,6,2,-5,-10,-8],[10,2,8,-10,4,-5,-9,10,8,4,2,9,-3,-10,7,8]],[[9,1,-3,-8,-2,3,8,1,-7,-5,4,-5,-8,1,-3,5],[2,9,-8,2,2,3,1,7,8,8,-7,10,8,-1,4,-4],[3,-10,2,10,7,5,7,9,5,-9,10,6,-5,-2,-4,-3]],[[-10,9,-7,8,-2,6,-7,9,2,-6,1,2,-10,3,1,-2],[-1,4,10,5,-9,5,6,9,4,-2,-9,9,9,5,9,10],[8,9,-10,-4,-5,-6,-5,-1,-2,3,5,1,5,-5,-3,6]],[[3,-3,-2,-3,-10,-10,-7,5,1,-3,2,-4,9,-5,4,-8],[-7,-9,10,5,-2,4,-5,-9,6,7,-5,9,10,-10,5,1],[-9,-10,4,-8,2,6,-10,8,-8,-8,-7,8,-2,4,-6,-9]],[[7,5,-7,-10,6,8,10,6,2,10,2,7,-8,-1,-5,-3],[-2,-4,5,9,9,-9,-3,8,10,5,7,8,-10,-4,-3,-5],[-7,-3,-4,-4,-10,-3,-2,10,-8,6,4,3,-4,9,5,-2]],[[7,-3,-8,4,-3,-4,-8,7,-9,3,6,9,4,9,4,-10],[-7,-3,-3,6,6,9,4,9,-8,9,8,-5,-8,10,6,-4],[-6,-9,-4,4,-2,-3,10,10,-2,-3,-6,1,-3,-7,-4,1]],[[10,10,6,5,9,-4,7,9,4,-10,-10,-6,3,-1,6,8],[5,-9,1,9,-1,-3,9,-10,3,3,10,-8,5,-3,-3,-7],[8,-7,2,-3,9,3,-7,10,10,5,5,6,-5,10,-9,-6]]], dtype = "int16")#candidate|5719|(8, 3, 16)|const|int16
bop_5720 = relay.multiply(var_5718.astype('int16'), relay.reshape(const_5719.astype('int16'), relay.shape_of(var_5718))) # shape=(8, 3, 16)
var_5724 = relay.var("var_5724", dtype = "int16", shape = (8, 3, 16))#candidate|5724|(8, 3, 16)|var|int16
bop_5725 = relay.equal(bop_5720.astype('bool'), relay.reshape(var_5724.astype('bool'), relay.shape_of(bop_5720))) # shape=(8, 3, 16)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_5729 = relay.TupleGetItem(func_3507_call(), 0)
call_5730 = relay.TupleGetItem(func_3509_call(), 0)
func_4438_call = mod.get_global_var('func_4438')
func_4440_call = mutated_mod.get_global_var('func_4440')
call_5739 = relay.TupleGetItem(func_4438_call(), 0)
call_5740 = relay.TupleGetItem(func_4440_call(), 0)
func_3037_call = mod.get_global_var('func_3037')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_5754 = relay.TupleGetItem(func_3037_call(), 0)
call_5755 = relay.TupleGetItem(func_3038_call(), 0)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_5756 = relay.TupleGetItem(func_2808_call(), 0)
call_5757 = relay.TupleGetItem(func_2810_call(), 0)
func_5341_call = mod.get_global_var('func_5341')
func_5343_call = mutated_mod.get_global_var('func_5343')
call_5758 = func_5341_call()
call_5759 = func_5341_call()
bop_5772 = relay.divide(var_5718.astype('float64'), relay.reshape(bop_5725.astype('float64'), relay.shape_of(var_5718))) # shape=(8, 3, 16)
func_3934_call = mod.get_global_var('func_3934')
func_3935_call = mutated_mod.get_global_var('func_3935')
call_5791 = relay.TupleGetItem(func_3934_call(), 0)
call_5792 = relay.TupleGetItem(func_3935_call(), 0)
output = relay.Tuple([call_5729,call_5739,call_5754,call_5756,call_5758,bop_5772,call_5791,])
output2 = relay.Tuple([call_5730,call_5740,call_5755,call_5757,call_5759,bop_5772,call_5792,])
func_5797 = relay.Function([var_5718,var_5724,], output)
mod['func_5797'] = func_5797
mod = relay.transform.InferType()(mod)
var_5798 = relay.var("var_5798", dtype = "int16", shape = (8, 3, 16))#candidate|5798|(8, 3, 16)|var|int16
var_5799 = relay.var("var_5799", dtype = "int16", shape = (8, 3, 16))#candidate|5799|(8, 3, 16)|var|int16
output = func_5797(var_5798,var_5799,)
func_5800 = relay.Function([var_5798,var_5799,], output)
mutated_mod['func_5800'] = func_5800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1213_call = mod.get_global_var('func_1213')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_5820 = relay.TupleGetItem(func_1213_call(), 0)
call_5821 = relay.TupleGetItem(func_1215_call(), 0)
func_5287_call = mod.get_global_var('func_5287')
func_5289_call = mutated_mod.get_global_var('func_5289')
call_5826 = func_5287_call()
call_5827 = func_5287_call()
uop_5830 = relay.tan(call_5820.astype('float32')) # shape=(1, 5, 4)
uop_5832 = relay.tan(call_5821.astype('float32')) # shape=(1, 5, 4)
func_2757_call = mod.get_global_var('func_2757')
func_2758_call = mutated_mod.get_global_var('func_2758')
call_5833 = relay.TupleGetItem(func_2757_call(), 0)
call_5834 = relay.TupleGetItem(func_2758_call(), 0)
func_5239_call = mod.get_global_var('func_5239')
func_5241_call = mutated_mod.get_global_var('func_5241')
call_5849 = relay.TupleGetItem(func_5239_call(), 3)
call_5850 = relay.TupleGetItem(func_5241_call(), 3)
output = relay.Tuple([call_5826,uop_5830,call_5833,call_5849,])
output2 = relay.Tuple([call_5827,uop_5832,call_5834,call_5850,])
func_5854 = relay.Function([], output)
mod['func_5854'] = func_5854
mod = relay.transform.InferType()(mod)
output = func_5854()
func_5855 = relay.Function([], output)
mutated_mod['func_5855'] = func_5855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1586_call = mod.get_global_var('func_1586')
func_1588_call = mutated_mod.get_global_var('func_1588')
call_5856 = relay.TupleGetItem(func_1586_call(), 1)
call_5857 = relay.TupleGetItem(func_1588_call(), 1)
output = call_5856
output2 = call_5857
func_5873 = relay.Function([], output)
mod['func_5873'] = func_5873
mod = relay.transform.InferType()(mod)
mutated_mod['func_5873'] = func_5873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5873_call = mutated_mod.get_global_var('func_5873')
call_5874 = func_5873_call()
output = call_5874
func_5875 = relay.Function([], output)
mutated_mod['func_5875'] = func_5875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5177_call = mod.get_global_var('func_5177')
func_5179_call = mutated_mod.get_global_var('func_5179')
call_5903 = relay.TupleGetItem(func_5177_call(), 0)
call_5904 = relay.TupleGetItem(func_5179_call(), 0)
func_5585_call = mod.get_global_var('func_5585')
func_5587_call = mutated_mod.get_global_var('func_5587')
call_5913 = relay.TupleGetItem(func_5585_call(), 1)
call_5914 = relay.TupleGetItem(func_5587_call(), 1)
func_1814_call = mod.get_global_var('func_1814')
func_1817_call = mutated_mod.get_global_var('func_1817')
const_5925 = relay.const([[5.668571,-2.998999,9.454081,9.626522,1.086861,-5.695361,-2.492700,-5.991046,-2.009945,-1.651967],[7.906651,-6.573768,2.039494,7.590938,-0.473890,-9.748788,3.889221,8.096979,-4.111270,-7.900516],[-7.381570,-3.073236,5.505296,-2.032932,2.623913,9.532643,6.117540,7.154614,9.783068,-5.419517],[9.367860,9.051581,7.757265,6.052655,-6.016202,-5.380923,-1.929051,4.207606,0.152545,9.444492],[-0.760444,5.969039,7.265037,8.968292,-8.739725,-1.116948,-3.896838,-3.461056,-4.523796,-2.242973],[-2.928490,-6.831156,1.035337,-3.680193,8.730864,8.077833,-4.435680,4.099120,2.383009,-1.565524],[-5.662876,-3.703539,5.290523,2.230103,-7.416913,-5.053121,-3.708331,-8.088665,-3.308510,-4.147595],[-5.370255,9.386266,-5.096475,-4.007577,2.187475,3.738788,1.653542,0.951884,2.151261,5.585071],[-6.314045,-1.417235,-2.030559,-1.899942,8.243974,-3.779087,0.733174,0.715305,6.045978,2.751936],[-6.373385,-9.314271,-7.586477,-8.706137,-6.680013,-0.290889,9.880031,1.640338,1.604358,-9.459666],[-5.039797,-7.514606,2.579893,-4.344607,-3.677760,2.785724,-6.481203,-2.049679,9.058789,-0.222976],[-1.139740,-6.022896,5.898081,2.550436,-1.908234,-4.453224,1.630958,-6.371311,-4.031195,8.108022],[-6.742415,0.661559,-9.409040,-7.650735,2.336294,-5.950743,0.889594,8.063974,-7.816698,8.821809],[5.908411,-7.451759,-0.612548,1.408023,5.497780,5.152335,2.019881,-3.094015,8.568276,-8.908294],[-3.228022,-4.365737,4.362248,-6.380529,0.764921,-9.712557,4.986218,4.259291,2.791925,-1.052963],[9.837678,5.075398,7.613820,-9.968469,-1.549942,3.865233,9.634639,-3.444497,4.974369,2.090666],[-5.683373,8.159897,-4.420893,3.191597,0.536787,-2.189283,-5.208609,-3.934774,4.460046,-8.957056],[9.277519,-2.800612,8.740234,7.779665,-0.231162,5.449230,6.826761,-9.767842,7.026654,3.813784],[-9.630099,6.903263,6.410927,-6.732791,2.500337,-8.528614,-9.242472,9.564250,0.484721,-7.111283],[8.326079,-5.439028,4.043540,-0.625345,7.232875,9.999117,5.528624,-2.424417,-1.713061,-1.752154],[5.252118,-7.122057,7.538193,0.460139,6.667315,-6.652283,-4.848312,8.500124,-4.703328,-4.252048],[8.704975,4.069086,4.713947,-0.068950,-9.197145,6.887467,1.880707,1.099808,8.023393,-7.623242],[-0.191532,-4.183584,7.957370,-0.945623,4.148033,7.663500,6.380620,-0.393489,-0.618551,-8.167463],[5.116286,-2.743497,-2.545346,8.704440,4.979432,-4.973655,4.070862,-7.179112,-2.530548,-7.587791],[2.001652,-2.751047,-6.468205,9.753791,7.982390,3.440843,3.445557,-5.636874,3.664860,-6.836792],[3.093748,-7.285515,3.702632,5.392903,-3.897063,1.840923,-6.218147,-6.527791,-6.100004,1.603125],[8.049615,-1.372581,1.476069,-2.862137,3.104789,7.265854,3.461959,3.696848,-9.822856,-9.666081],[-0.671958,-7.933417,-3.706329,1.962622,3.806812,-4.961906,0.401487,3.845214,8.351984,0.895618],[-6.943927,3.540392,-8.929591,-5.839222,-2.697604,5.665438,2.464327,0.029653,-4.855710,-9.754366],[6.780070,7.969809,-1.107386,2.551586,-7.334476,-5.548586,9.121305,0.667843,-7.183307,-3.431463],[-2.821636,2.114456,-8.552655,3.460852,6.668395,-8.299005,4.161786,0.569020,-7.720453,3.499308],[3.095091,-7.253763,-2.680784,-9.453821,4.130165,9.760750,8.191549,2.827026,4.624616,-7.581493],[1.367129,0.665646,-9.685057,-0.849142,-6.505678,-5.229684,0.816509,-2.692740,-7.218377,-5.295236],[-0.402365,6.876745,-6.367401,3.115846,-3.032025,-5.877361,-5.754093,-0.022456,-7.969149,5.721926],[-2.082303,-8.611923,-3.647301,7.291288,3.761265,4.331500,6.390209,5.318222,1.089409,5.996882],[3.042652,4.366966,-4.589998,-2.362156,-6.532737,4.023337,2.269336,-6.600031,-8.793606,-8.690877],[1.159273,1.593292,7.742684,-1.217832,0.273577,-1.685930,3.286374,-0.152879,4.011533,-4.251328],[3.682095,-7.429217,5.544942,-2.029121,2.600390,-2.927832,-9.852874,1.476960,-8.872395,4.466282],[-6.350399,-2.566499,3.982469,4.815390,-3.305183,6.398327,9.062128,-8.929882,-4.070899,-9.341028],[-3.881723,6.501011,5.348403,-7.815291,-5.366406,4.049835,8.539067,3.256781,1.793852,9.696462],[-1.756704,3.212273,-2.375296,8.012622,-5.006545,-8.629394,-5.909142,-6.130067,2.725561,7.040129],[-7.430835,-6.800823,5.708961,-5.639043,-0.702053,-4.270551,-1.325790,-0.398211,6.834177,-2.507936],[4.623785,-3.460885,-9.614741,5.919653,2.690612,5.371785,-1.767737,7.168017,2.165621,-2.122684],[0.306102,5.760333,-9.064648,4.071123,0.012069,0.992588,-6.282444,-4.585514,-2.354229,-6.229938],[-9.981203,3.651621,7.530867,-5.199357,5.393295,-8.381033,0.358987,-4.656632,5.434120,-5.594866],[8.969303,-5.015921,3.933333,-0.701399,-7.697486,-9.497677,0.299775,4.462583,-4.352312,4.457960],[-3.550495,3.875933,0.352822,4.586426,3.507805,8.715029,-7.014575,-9.109085,-4.111112,0.789310],[-7.466389,-1.398318,-3.405487,-3.503047,8.873892,-4.272391,-2.560524,-1.556725,1.266915,-7.959760],[7.677909,-8.645940,6.936118,8.292252,2.021068,5.505178,-6.115613,4.786780,7.933170,-0.059131],[-3.331109,2.159693,-8.700703,-6.452377,8.705658,-8.086449,8.194345,-6.253147,9.355057,-8.943354],[8.619288,-3.757739,3.638264,-1.670023,-8.676082,-9.831055,2.715002,8.452938,6.516037,4.286829],[-5.808011,2.173848,-6.117875,0.408011,5.753372,7.712075,5.265149,6.981544,1.974811,2.602749],[-6.072191,-7.024185,8.754971,6.874837,-0.740552,-3.389901,-1.516440,-4.863693,8.154575,-6.135127],[1.035127,5.376181,-8.602632,-7.083569,-1.566393,8.434986,5.256273,-2.014243,3.854604,9.074577],[9.170550,-6.268439,1.482300,-8.276009,-6.364839,7.130089,-8.463594,-2.628398,3.496730,9.222835],[6.584814,-5.849228,-1.464006,8.690664,-9.385008,7.106274,-7.645358,8.599558,-6.166010,3.642958],[4.894917,4.077046,5.910310,-5.750229,-0.651603,1.584859,-0.166230,-2.035208,-1.079465,-6.684107],[-6.298196,-6.562106,7.393250,-9.348382,-1.992609,6.897953,-3.729536,3.231068,-4.546309,8.169669],[1.013744,-3.888340,-0.888712,5.135822,0.014553,-7.953556,5.336597,-2.779874,-0.967500,5.772087],[-9.004468,-6.473019,8.102567,8.576053,8.848551,-7.197745,0.041837,-2.886444,5.784380,-8.845072]], dtype = "float64")#candidate|5925|(60, 10)|const|float64
const_5926 = relay.const([[-5.901536],[2.006498],[8.301069],[-2.106604],[-4.163999],[9.657441],[8.213228],[-9.978018],[-2.194962],[7.863260],[-6.131033],[-7.233864],[9.252635],[8.090022],[-3.995631],[-7.094976],[-4.286953],[-5.618884],[-8.061196],[-1.663332],[-9.544070],[-2.869872],[-9.328983],[2.190350],[-8.177885],[-2.517697],[0.612391],[0.635988],[-2.364488],[-2.477837],[-4.639782],[4.258174],[-6.973145],[-9.300305],[-2.509429],[-2.161805],[3.357794],[6.263859],[4.037317],[-5.812424],[7.274087],[-5.087835],[5.397396],[6.998810],[-3.043937],[-6.152781],[-0.603319],[-7.397112],[-9.791873],[6.448366],[0.546892],[4.755190],[-0.854655],[-4.953318],[-3.686892],[4.266444],[4.613956],[-9.884794],[-8.899676],[7.330704],[-9.120982],[6.044773],[2.003919],[5.621860],[2.764170],[3.824172],[-3.290979],[3.315987],[4.297259],[6.256553],[-1.174483],[7.673587],[-4.835581],[-2.151081],[9.600892],[-2.684259],[4.675550],[-5.966562],[9.448720],[-7.564044],[9.561248],[8.117333],[1.469069],[-1.324358],[-1.553964],[-4.581101],[4.807613],[4.433328],[4.103715],[-5.056204],[0.564793],[-3.410035],[-3.296331],[8.947980],[9.251803],[-7.371942],[2.590670],[-0.500372],[-9.455625],[5.525209],[-2.571931],[7.532741],[3.386803],[-5.064168],[-2.395467],[8.283564],[8.729067],[2.306592],[0.732858],[8.677876],[-0.098703],[6.724160],[6.266063],[-0.031145],[-1.709152],[-4.986537],[2.842993],[-0.061486],[-6.593766],[-9.213366],[1.409261],[-5.776568],[6.373611],[6.830949],[8.786423],[3.135937],[-9.856300],[5.155591],[0.335489],[-2.276141],[-4.852912],[-4.373033],[-5.309688],[-6.917916],[3.512709],[-1.226868],[2.460833],[5.584739],[-9.265690],[8.064987],[3.845542],[5.593840],[2.167959],[0.326676],[4.393447],[-7.785605],[3.809154],[5.156179],[-1.333043],[-8.865063],[-1.453163],[-8.308172],[-4.410587],[8.245281],[-9.189378],[-7.079359],[5.670933],[-0.218984],[-8.031181],[1.045948],[1.541802],[5.799516],[1.604523],[-2.000233],[3.825835],[8.517449],[1.745083],[0.182523],[-1.633822],[-0.531191],[8.986056],[-6.472660],[8.845812],[8.880740],[7.308293],[2.941030],[-3.899741],[5.217607],[7.436448],[6.318586],[-6.094724],[2.334519],[9.088605],[7.234688],[5.806301],[-4.486157],[-3.832246],[6.189416],[5.748257],[-6.727132],[-4.382027],[6.280988],[-7.860889],[-8.642660],[8.285923],[-7.463841],[-0.412968],[2.943005],[-9.438668],[1.920212]], dtype = "float32")#candidate|5926|(200, 1)|const|float32
call_5924 = relay.TupleGetItem(func_1814_call(relay.reshape(const_5925.astype('float64'), [600,]), relay.reshape(const_5926.astype('float32'), [10, 5, 4]), ), 0)
call_5927 = relay.TupleGetItem(func_1817_call(relay.reshape(const_5925.astype('float64'), [600,]), relay.reshape(const_5926.astype('float32'), [10, 5, 4]), ), 0)
output = relay.Tuple([call_5903,call_5913,call_5924,const_5925,const_5926,])
output2 = relay.Tuple([call_5904,call_5914,call_5927,const_5925,const_5926,])
func_5933 = relay.Function([], output)
mod['func_5933'] = func_5933
mod = relay.transform.InferType()(mod)
mutated_mod['func_5933'] = func_5933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5933_call = mutated_mod.get_global_var('func_5933')
call_5934 = func_5933_call()
output = call_5934
func_5935 = relay.Function([], output)
mutated_mod['func_5935'] = func_5935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5959 = relay.var("var_5959", dtype = "float32", shape = (1, 7, 10))#candidate|5959|(1, 7, 10)|var|float32
uop_5960 = relay.cos(var_5959.astype('float32')) # shape=(1, 7, 10)
output = uop_5960
output2 = uop_5960
func_5969 = relay.Function([var_5959,], output)
mod['func_5969'] = func_5969
mod = relay.transform.InferType()(mod)
mutated_mod['func_5969'] = func_5969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5970 = relay.var("var_5970", dtype = "float32", shape = (1, 7, 10))#candidate|5970|(1, 7, 10)|var|float32
func_5969_call = mutated_mod.get_global_var('func_5969')
call_5971 = func_5969_call(var_5970)
output = call_5971
func_5972 = relay.Function([var_5970], output)
mutated_mod['func_5972'] = func_5972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5873_call = mod.get_global_var('func_5873')
func_5875_call = mutated_mod.get_global_var('func_5875')
call_6021 = func_5873_call()
call_6022 = func_5873_call()
func_3705_call = mod.get_global_var('func_3705')
func_3707_call = mutated_mod.get_global_var('func_3707')
var_6032 = relay.var("var_6032", dtype = "float64", shape = (12,))#candidate|6032|(12,)|var|float64
call_6031 = relay.TupleGetItem(func_3705_call(relay.reshape(var_6032.astype('float64'), [12,])), 3)
call_6033 = relay.TupleGetItem(func_3707_call(relay.reshape(var_6032.astype('float64'), [12,])), 3)
output = relay.Tuple([call_6021,call_6031,var_6032,])
output2 = relay.Tuple([call_6022,call_6033,var_6032,])
func_6035 = relay.Function([var_6032,], output)
mod['func_6035'] = func_6035
mod = relay.transform.InferType()(mod)
mutated_mod['func_6035'] = func_6035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6036 = relay.var("var_6036", dtype = "float64", shape = (12,))#candidate|6036|(12,)|var|float64
func_6035_call = mutated_mod.get_global_var('func_6035')
call_6037 = func_6035_call(var_6036)
output = call_6037
func_6038 = relay.Function([var_6036], output)
mutated_mod['func_6038'] = func_6038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4275_call = mod.get_global_var('func_4275')
func_4276_call = mutated_mod.get_global_var('func_4276')
call_6090 = relay.TupleGetItem(func_4275_call(), 3)
call_6091 = relay.TupleGetItem(func_4276_call(), 3)
output = relay.Tuple([call_6090,])
output2 = relay.Tuple([call_6091,])
func_6100 = relay.Function([], output)
mod['func_6100'] = func_6100
mod = relay.transform.InferType()(mod)
output = func_6100()
func_6101 = relay.Function([], output)
mutated_mod['func_6101'] = func_6101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4011_call = mod.get_global_var('func_4011')
func_4013_call = mutated_mod.get_global_var('func_4013')
call_6146 = relay.TupleGetItem(func_4011_call(), 0)
call_6147 = relay.TupleGetItem(func_4013_call(), 0)
func_5055_call = mod.get_global_var('func_5055')
func_5056_call = mutated_mod.get_global_var('func_5056')
call_6158 = relay.TupleGetItem(func_5055_call(), 0)
call_6159 = relay.TupleGetItem(func_5056_call(), 0)
uop_6168 = relay.acosh(call_6146.astype('float64')) # shape=(6, 5, 4)
uop_6170 = relay.acosh(call_6147.astype('float64')) # shape=(6, 5, 4)
output = relay.Tuple([call_6158,uop_6168,])
output2 = relay.Tuple([call_6159,uop_6170,])
func_6171 = relay.Function([], output)
mod['func_6171'] = func_6171
mod = relay.transform.InferType()(mod)
output = func_6171()
func_6172 = relay.Function([], output)
mutated_mod['func_6172'] = func_6172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5396_call = mod.get_global_var('func_5396')
func_5398_call = mutated_mod.get_global_var('func_5398')
call_6200 = relay.TupleGetItem(func_5396_call(), 1)
call_6201 = relay.TupleGetItem(func_5398_call(), 1)
func_5341_call = mod.get_global_var('func_5341')
func_5343_call = mutated_mod.get_global_var('func_5343')
call_6213 = func_5341_call()
call_6214 = func_5341_call()
output = relay.Tuple([call_6200,call_6213,])
output2 = relay.Tuple([call_6201,call_6214,])
func_6223 = relay.Function([], output)
mod['func_6223'] = func_6223
mod = relay.transform.InferType()(mod)
output = func_6223()
func_6224 = relay.Function([], output)
mutated_mod['func_6224'] = func_6224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2944_call = mod.get_global_var('func_2944')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_6227 = relay.TupleGetItem(func_2944_call(), 0)
call_6228 = relay.TupleGetItem(func_2945_call(), 0)
output = relay.Tuple([call_6227,])
output2 = relay.Tuple([call_6228,])
func_6285 = relay.Function([], output)
mod['func_6285'] = func_6285
mod = relay.transform.InferType()(mod)
mutated_mod['func_6285'] = func_6285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6285_call = mutated_mod.get_global_var('func_6285')
call_6286 = func_6285_call()
output = call_6286
func_6287 = relay.Function([], output)
mutated_mod['func_6287'] = func_6287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3879_call = mod.get_global_var('func_3879')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_6318 = func_3879_call()
call_6319 = func_3879_call()
func_1056_call = mod.get_global_var('func_1056')
func_1059_call = mutated_mod.get_global_var('func_1059')
const_6327 = relay.const([4,-4,-6,-9,-7,8,-6,-5,-5,7,3,4,-6,-6,-10,-3,-5,-3,4,-1,10,4,-10,-2,-5,-6,2,-4,8,3,3,4,-3,-10,-10,9,-10,3,-1,-6,5,5,-3,-4,-7,1,-5,9,-2,6,-1,2,-7,3,2,-4,-1,-4,8,-7,7,6,-5,-1,-3,10,1,7,-7,-5,10,-5,8,5,-9,10,2,-7,8,-5,4,-7,5,4,4,10,9,-5,7,1,-2,-2,-7,-3,-9,-8,-4,-10,10,-3,-3,10,-10,-9,5,-3,-10,-3,-7,4,5,-1,-8,7,6,4,-5,-1,9,4,-9,1,3,8,2,-6,-5,-5,-9,-3,-4,-4,3,-6,5,-6,-8,-6,3,-2,8,-4,-6,-6,-3,8,7,-10,7,-5,-5,-9,-10,-5,10,9,-7,3,-4,-6,9,6,-6,-8,-2,5,4,2,10,-6,-7,10,-8,5,1,10,-5,-6,3,-6,-7,-4,-7,-4,6,-7,4,4,10,5,3,1,-4,-3,-1,1,9,10,2,5], dtype = "int8")#candidate|6327|(200,)|const|int8
const_6328 = relay.const([-5.558582,-2.982524,2.558170,8.195789,7.934539,8.055615,9.120788,3.820330,1.324618,1.972366,5.243763,2.435845,-2.338756,-0.071858,7.381273,-3.103323,5.833040,6.702835,6.649045,-0.935091,0.045012,5.673846,-9.087851,-0.104728,-5.623333,8.910368,-0.634816,-9.643994,7.141795,-4.950615,-3.385756,-4.518002,5.245705,0.716637,-4.318218,1.991492,3.857042,8.503437,-2.594634,8.907919,1.862233,-7.146458,8.362481,-9.151651,-3.812878,5.679615,6.354038,-2.262889,4.777138,5.353554,0.819283,3.274472,-2.092896,-5.757326,-6.220132,5.527316,-0.735293,2.901233,-7.547701,-2.148257,-9.063127,3.276627,9.409552,4.953896,9.950590,9.994807,4.560719,2.973339,2.072193,-1.394556,1.342081,1.504801,-0.600402,-1.957661,3.762789,8.371133,-4.915599,2.454401,-4.191133,1.431345,-3.798965,5.033854,4.564100,9.539507,-4.424262,6.337969,9.340713,-1.633128,1.741954,-9.970864,3.540718,9.348954,-7.234542,-2.002168,7.285894,9.442130,-5.484173,2.276451,8.620125,-3.705852,8.391693,-8.413486,-4.054142,-8.906269,2.201355,-1.240509,-7.378898,-2.276372,1.699484,5.852239,-1.070702,-7.793523,2.905815,8.642006,-9.299851,4.821901,2.029095,-9.738074,-9.345680,2.514312,1.259771,-9.368503,4.258908,-3.497419,7.356855,3.561457,-4.426193,-6.572629,-9.158592,2.043610,8.734424,-4.912281,-0.240650,0.960572,4.866820,-7.793245,-1.588090,-1.594368,9.080052,-5.973107,-7.559552,6.116506,7.651047,7.660818,7.904694,-3.596275,4.424715,4.768577,3.572470,-1.065685,5.136679,4.282961,1.727933,-1.200386,2.923430,-3.328489,-1.002324,-4.835866,3.912123,9.229266,-3.798365,-8.502633,-1.822632,7.365696,-2.131325,-9.117961,-8.341335,8.039666,2.742439,8.147694,4.261686,1.636805,0.129808,5.100336,8.985593,9.788349,3.594344,2.746675,6.009359,4.989691,-8.114482,2.763960,-7.591673,-2.527572,-4.087857,-0.599960,2.158119,-2.030746,2.050387,-4.843804,-8.740483,3.059915,5.604735,-4.902334,2.664646,-0.138032,7.116229,0.915367,-5.411254,-4.701740,9.141167,-8.159101,-4.071806,5.801320,8.105416,-0.056270,3.093883,6.316150,-0.055888,9.189372,7.569322,6.574592,2.919922,-7.086603,-4.480893,5.507062,2.911635,4.987270,-7.655695,-2.629814,-6.061950,0.467972,-2.993166,-5.360414,-4.520193,-5.448900,9.493349,7.760962,-3.290560,-4.218544,-1.848577,-8.043788,-2.417647,6.020166,-7.297757,-9.706047,-6.661364,-1.529423,-8.827165,1.141096,-5.707289,-3.765937,4.708823,7.983308,-1.037127,-3.941712,5.625465,-1.098237,-6.524319,-3.140660,9.983922,9.514143,-7.966925,-8.433407,-5.351609,-2.210923,-7.598564,-0.407924,-6.328093,3.414493,-3.208927,7.177510,2.091314,0.835535,8.248102,-1.103360,-9.728264,-8.132291,-9.209771,5.506987,-1.049607,2.970136,-9.163669,-0.245863,2.175646,7.489012,6.738449,3.382661,1.002154,8.352056,-4.858822,5.718462,5.619289,-0.595882,3.286752,0.442248,8.406990,-2.102767,-4.873677,-8.669786,-6.705475,1.559592,-7.952480,-7.497464,7.614352,-2.149412,-3.504950,-3.588667,6.096920,2.470178,-2.293343,-3.951783,4.797460,-4.802230,9.026262,-2.258570,-7.512662,7.663699,-9.387952,-4.497621,5.508211,-5.192291,9.467015,-6.759489,3.362815,9.925401,-5.569693,3.930449,-3.235689,6.837134,-8.171674,4.915011,-3.572065,3.685229,4.431805,-3.981812,-1.078208,-8.978883,-4.007599,-3.080901,-9.193191,5.140792,0.220226,-0.973240,-4.237860,5.455171,3.777263,-0.391340,5.246114,5.703107,7.494527,-9.699382,-5.162805,9.926646,4.466451,-2.818051,8.323554,-5.679830,-8.302974,-1.122688,-0.748411,1.756327,7.126120,8.475882,8.864862,4.758326,5.092864,-5.189519,-6.778611,-6.961812,9.943840,7.878335,-0.388449,0.282136,-5.689740,-4.112260,1.783635,0.946578,0.127175,5.057373,9.617003,4.810144,-6.142004,-6.398673,-1.077723,-8.603229,9.056278,-5.416178,2.267682,-1.849257,-8.063790,5.702070,-4.320142,-4.173819,8.156601,-6.527035,-1.314411,8.213156,1.962655,2.127548,-8.924363,8.805337,1.088617,-6.760823,0.540757,-4.347558,6.173063,7.397768,-2.280786,4.517515,5.630352,-0.862865,9.282757,4.036076,6.180643,-7.574743,-9.879778,8.558054,-5.291071,0.220233,-0.915509,8.994195,3.519000,6.855590,-9.025216,6.772366,-8.345954,6.971965,-7.810027,-8.542228,8.287115,2.754686,-4.140219,5.222998,-9.895099,-8.687091,-3.969818,-7.023696,-9.151625,-4.906483,-6.852882,6.670809,2.928987,6.271930,9.560508,-7.471851,-3.864293,-4.748930,-9.154504,2.552554,-5.593407,-5.399809,9.548983,-5.582692,-6.908522,-4.530428,4.368625,-3.118328,-5.783937,-2.983960,5.969646,-9.543222,-2.022112,0.600760,-8.004480,-9.875813,-5.221013,-8.794086,3.007558,-9.314273,2.688928,2.786078,-6.265254,4.804478,2.206101,-2.798435,-5.251119,-4.652024,5.323942,-7.220908,1.297181,8.561177,7.316411,9.330367,-5.373320,-3.005798,8.913755,-7.664211,4.148838,-5.709967,2.699122,-0.102223,-9.724489,5.680723,-5.780412,9.042329,-9.451494,5.988243,-6.044249,-5.495364,-8.976746,-1.869449,-3.287279,7.443722,7.072741,-1.356724,-3.104953,-9.032091,-5.039801,1.195303,1.897086,-8.804158,2.130710,3.441636,-6.099244,-1.358301,0.878379,-9.234841,-4.076603,6.489238,-1.056939,-3.008966,-9.007556,9.442640,-1.461996,8.276313,0.187265,5.030214,-2.172065,9.568170,4.907666,4.496862,-4.986146,-5.576967,-0.554183,-1.612136,-0.845710,1.237058,-1.025151,9.166425,1.851897,-4.423824,-7.142980,9.247495,8.621778,6.897435,3.239647,6.479416,6.455353,-9.409008,3.011659,-4.218853,4.153873,5.716992,-9.253845,1.589439,3.105931,-7.588170,5.160674,-4.496506,-1.520337,7.450002,6.755458,-9.965376,7.799619,-2.740281,0.620464,-9.476899,-3.003492,-0.296232,-6.820096,5.275702,-9.211875,9.071867,2.498469,-5.832005,0.986440,7.217875,-0.928596,6.763850,-4.561529,-2.855046,-2.494659,9.623029,-4.690411,9.940721,4.548698,1.287890,7.946549,8.555420,-9.607685,-9.227311,-8.496967,-3.481386,8.183801,-3.716607,9.265936,-6.969683,9.821289,2.048453,9.698655,-7.840782,7.393437,-3.207916,-7.311100,5.190101,4.241445,-9.462245,-7.537628,-1.681230,5.071979,0.904869,-8.953612,-6.173637,6.283913,0.069693,9.083129,1.866539,6.311604,4.762540,-5.409852,0.168500,-3.741694,6.749147,-7.396717,9.725378,-1.785637,4.526758,-6.483870,-1.791828,1.035067,-3.079696,7.979725,8.595675,-3.864248,-4.587258,6.411026,-3.296209,0.589252,-7.311364,-1.903424,9.976140,4.147931,0.112436,5.447589,8.640396,3.341753,0.323698,-2.274018,-3.599339,1.384185,8.735215,-6.141899,-3.803279,2.446323,0.015828,-3.087830,-9.982179,3.408129,5.543181,5.054300,4.231053,8.525153,4.289104,3.573366,-0.223720,-7.233029,-6.296174,1.125756,-0.217052,5.157278,-6.877217,4.862665,1.588999,-6.606011,8.360397,-8.725472,4.758764,2.919493,8.418504,-9.650757,9.565782,5.265815,6.143834,-0.085094,8.162062,4.136349,-9.473808,-0.314055,-4.452038,-0.072194,-9.506481,-3.109532,-7.034561,-0.676476,8.151499,6.480414,8.160606,-0.492930,-1.139048,-5.131906,-8.640758,8.253895,-3.827074,9.222040,4.504662,-7.819594,-4.242282,8.035441,-0.589390,-5.771398,-5.503575,-7.203019,-1.821075,-6.283145,-1.755024,-2.778557,-8.423818,2.893387,7.575548,0.278576,-9.556661,-7.522996,7.477658,-4.950511,1.765168,6.191401,-6.925087,0.706914,-0.584417,1.647155,-2.952707,5.186622,-3.289798,-2.561984,9.364775,-8.331826,3.104622,-4.986409,-4.802652,6.074561,5.253636,4.777145,-9.074448,-9.837904,-9.653449,7.237741,6.224126,7.762820,2.065433,8.998614,-3.205679,5.578972,-5.002191,-0.487408,-1.185746,-3.135343,-5.832211,0.162000,-4.983783,2.784327,-7.083135,-8.724812,0.198229,9.462913,9.791908,-6.442882,-3.754240,7.846251,9.696705,5.860423,2.317869,-0.485498,9.007406,5.525573,7.341591,-2.620646,4.236314,-8.026534,-1.289189,-3.706082,-5.239316,5.748537,-5.561211,-4.604212,-4.205307,1.430152,2.716854,6.700460,5.819059,3.958712,9.982135,-7.165871,-2.064648,-8.929095,-2.873104,-2.377711,4.468244,0.548513,-1.567332,0.707526,2.321875,1.916406,-3.645684,0.302051,5.330816,4.384014,-7.009897,7.326418,-8.816961], dtype = "float32")#candidate|6328|(800,)|const|float32
call_6326 = relay.TupleGetItem(func_1056_call(relay.reshape(const_6327.astype('int8'), [10, 5, 4]), relay.reshape(const_6328.astype('float32'), [800,]), ), 2)
call_6329 = relay.TupleGetItem(func_1059_call(relay.reshape(const_6327.astype('int8'), [10, 5, 4]), relay.reshape(const_6328.astype('float32'), [800,]), ), 2)
output = relay.Tuple([call_6318,call_6326,const_6327,const_6328,])
output2 = relay.Tuple([call_6319,call_6329,const_6327,const_6328,])
func_6330 = relay.Function([], output)
mod['func_6330'] = func_6330
mod = relay.transform.InferType()(mod)
output = func_6330()
func_6331 = relay.Function([], output)
mutated_mod['func_6331'] = func_6331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2085_call = mod.get_global_var('func_2085')
func_2086_call = mutated_mod.get_global_var('func_2086')
call_6337 = relay.TupleGetItem(func_2085_call(), 0)
call_6338 = relay.TupleGetItem(func_2086_call(), 0)
func_4941_call = mod.get_global_var('func_4941')
func_4944_call = mutated_mod.get_global_var('func_4944')
var_6342 = relay.var("var_6342", dtype = "uint64", shape = (24, 10))#candidate|6342|(24, 10)|var|uint64
const_6343 = relay.const([-0.578354,9.938051,-1.872157,9.177634,7.246739,4.820165,2.438386,3.476515,7.839731,-9.301394,1.099773,0.852307], dtype = "float64")#candidate|6343|(12,)|const|float64
call_6341 = relay.TupleGetItem(func_4941_call(relay.reshape(var_6342.astype('uint64'), [1, 240]), relay.reshape(const_6343.astype('float64'), [12,]), ), 3)
call_6344 = relay.TupleGetItem(func_4944_call(relay.reshape(var_6342.astype('uint64'), [1, 240]), relay.reshape(const_6343.astype('float64'), [12,]), ), 3)
func_811_call = mod.get_global_var('func_811')
func_812_call = mutated_mod.get_global_var('func_812')
call_6358 = func_811_call()
call_6359 = func_811_call()
output = relay.Tuple([call_6337,call_6341,var_6342,const_6343,call_6358,])
output2 = relay.Tuple([call_6338,call_6344,var_6342,const_6343,call_6359,])
func_6370 = relay.Function([var_6342,], output)
mod['func_6370'] = func_6370
mod = relay.transform.InferType()(mod)
mutated_mod['func_6370'] = func_6370
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6371 = relay.var("var_6371", dtype = "uint64", shape = (24, 10))#candidate|6371|(24, 10)|var|uint64
func_6370_call = mutated_mod.get_global_var('func_6370')
call_6372 = func_6370_call(var_6371)
output = call_6372
func_6373 = relay.Function([var_6371], output)
mutated_mod['func_6373'] = func_6373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3879_call = mod.get_global_var('func_3879')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_6387 = func_3879_call()
call_6388 = func_3879_call()
func_2921_call = mod.get_global_var('func_2921')
func_2922_call = mutated_mod.get_global_var('func_2922')
call_6391 = relay.TupleGetItem(func_2921_call(), 0)
call_6392 = relay.TupleGetItem(func_2922_call(), 0)
bop_6399 = relay.logical_or(call_6387.astype('bool'), relay.reshape(call_6391.astype('bool'), relay.shape_of(call_6387))) # shape=(1, 5, 4)
bop_6402 = relay.logical_or(call_6388.astype('bool'), relay.reshape(call_6392.astype('bool'), relay.shape_of(call_6388))) # shape=(1, 5, 4)
bop_6403 = relay.left_shift(call_6387.astype('int32'), relay.reshape(call_6391.astype('int32'), relay.shape_of(call_6387))) # shape=(1, 5, 4)
bop_6406 = relay.left_shift(call_6388.astype('int32'), relay.reshape(call_6392.astype('int32'), relay.shape_of(call_6388))) # shape=(1, 5, 4)
func_4905_call = mod.get_global_var('func_4905')
func_4907_call = mutated_mod.get_global_var('func_4907')
var_6412 = relay.var("var_6412", dtype = "float64", shape = (600,))#candidate|6412|(600,)|var|float64
call_6411 = relay.TupleGetItem(func_4905_call(relay.reshape(var_6412.astype('float64'), [600,])), 2)
call_6413 = relay.TupleGetItem(func_4907_call(relay.reshape(var_6412.astype('float64'), [600,])), 2)
bop_6414 = relay.maximum(var_6412.astype('int32'), relay.reshape(call_6411.astype('int32'), relay.shape_of(var_6412))) # shape=(600,)
bop_6417 = relay.maximum(var_6412.astype('int32'), relay.reshape(call_6413.astype('int32'), relay.shape_of(var_6412))) # shape=(600,)
func_5585_call = mod.get_global_var('func_5585')
func_5587_call = mutated_mod.get_global_var('func_5587')
call_6432 = relay.TupleGetItem(func_5585_call(), 0)
call_6433 = relay.TupleGetItem(func_5587_call(), 0)
bop_6439 = relay.mod(call_6387.astype('float64'), relay.reshape(call_6432.astype('float64'), relay.shape_of(call_6387))) # shape=(1, 5, 4)
bop_6442 = relay.mod(call_6388.astype('float64'), relay.reshape(call_6433.astype('float64'), relay.shape_of(call_6388))) # shape=(1, 5, 4)
output = relay.Tuple([bop_6399,bop_6403,bop_6414,bop_6439,])
output2 = relay.Tuple([bop_6402,bop_6406,bop_6417,bop_6442,])
func_6453 = relay.Function([var_6412,], output)
mod['func_6453'] = func_6453
mod = relay.transform.InferType()(mod)
var_6454 = relay.var("var_6454", dtype = "float64", shape = (600,))#candidate|6454|(600,)|var|float64
output = func_6453(var_6454)
func_6455 = relay.Function([var_6454], output)
mutated_mod['func_6455'] = func_6455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5131_call = mod.get_global_var('func_5131')
func_5133_call = mutated_mod.get_global_var('func_5133')
call_6474 = relay.TupleGetItem(func_5131_call(), 1)
call_6475 = relay.TupleGetItem(func_5133_call(), 1)
func_2808_call = mod.get_global_var('func_2808')
func_2810_call = mutated_mod.get_global_var('func_2810')
call_6495 = relay.TupleGetItem(func_2808_call(), 0)
call_6496 = relay.TupleGetItem(func_2810_call(), 0)
func_3464_call = mod.get_global_var('func_3464')
func_3466_call = mutated_mod.get_global_var('func_3466')
call_6500 = relay.TupleGetItem(func_3464_call(), 2)
call_6501 = relay.TupleGetItem(func_3466_call(), 2)
uop_6504 = relay.cos(call_6495.astype('float32')) # shape=(1, 5, 4)
uop_6506 = relay.cos(call_6496.astype('float32')) # shape=(1, 5, 4)
func_5055_call = mod.get_global_var('func_5055')
func_5056_call = mutated_mod.get_global_var('func_5056')
call_6515 = relay.TupleGetItem(func_5055_call(), 0)
call_6516 = relay.TupleGetItem(func_5056_call(), 0)
output = relay.Tuple([call_6474,call_6500,uop_6504,call_6515,])
output2 = relay.Tuple([call_6475,call_6501,uop_6506,call_6516,])
func_6529 = relay.Function([], output)
mod['func_6529'] = func_6529
mod = relay.transform.InferType()(mod)
output = func_6529()
func_6530 = relay.Function([], output)
mutated_mod['func_6530'] = func_6530
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6544 = relay.const([[[1.593211],[-6.707009],[7.830005],[-7.728160],[6.105728],[-8.234730],[-9.582035]],[[6.951813],[-1.195953],[4.296780],[-7.339418],[3.879281],[2.012432],[5.592492]],[[8.473782],[0.783611],[-4.995259],[-7.687526],[-8.967955],[-7.556313],[-3.885098]],[[9.100242],[-1.925350],[-2.899348],[-9.371904],[-9.740316],[2.642168],[-0.308302]],[[-8.628948],[-6.315260],[-7.666214],[1.143715],[6.240381],[0.821565],[-1.892627]],[[8.851789],[-9.469667],[1.401693],[4.782639],[6.511569],[7.537592],[2.537911]],[[-9.356712],[-6.666384],[6.798077],[-4.043508],[-3.058687],[-0.934500],[2.226552]],[[5.888501],[-6.614025],[-0.308775],[3.205242],[2.593443],[2.017159],[6.092829]],[[-7.846191],[-1.255079],[-8.614688],[-3.186918],[6.883239],[-4.819228],[-7.358013]],[[5.315020],[-9.538179],[6.934551],[-8.158938],[8.258767],[-0.765882],[-6.128353]],[[-0.203353],[-2.669927],[-8.978912],[0.487215],[0.911300],[-4.870560],[-4.349555]],[[-0.680698],[-2.444135],[-4.309446],[3.317457],[5.442873],[5.847487],[7.318743]],[[3.301993],[-7.403554],[1.069422],[4.847941],[0.418360],[0.490171],[-1.177406]],[[6.182716],[-7.342469],[4.881212],[0.761293],[0.301103],[7.777127],[-2.735059]],[[8.502556],[-5.889227],[-1.387711],[-4.939091],[-2.181463],[5.680103],[-4.337761]]], dtype = "float32")#candidate|6544|(15, 7, 1)|const|float32
uop_6545 = relay.log(const_6544.astype('float32')) # shape=(15, 7, 1)
output = relay.Tuple([uop_6545,])
output2 = relay.Tuple([uop_6545,])
func_6548 = relay.Function([], output)
mod['func_6548'] = func_6548
mod = relay.transform.InferType()(mod)
mutated_mod['func_6548'] = func_6548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6548_call = mutated_mod.get_global_var('func_6548')
call_6549 = func_6548_call()
output = call_6549
func_6550 = relay.Function([], output)
mutated_mod['func_6550'] = func_6550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3981_call = mod.get_global_var('func_3981')
func_3983_call = mutated_mod.get_global_var('func_3983')
call_6554 = relay.TupleGetItem(func_3981_call(), 0)
call_6555 = relay.TupleGetItem(func_3983_call(), 0)
func_3464_call = mod.get_global_var('func_3464')
func_3466_call = mutated_mod.get_global_var('func_3466')
call_6559 = relay.TupleGetItem(func_3464_call(), 2)
call_6560 = relay.TupleGetItem(func_3466_call(), 2)
func_2494_call = mod.get_global_var('func_2494')
func_2495_call = mutated_mod.get_global_var('func_2495')
call_6561 = relay.TupleGetItem(func_2494_call(), 0)
call_6562 = relay.TupleGetItem(func_2495_call(), 0)
func_3850_call = mod.get_global_var('func_3850')
func_3853_call = mutated_mod.get_global_var('func_3853')
const_6593 = relay.const([-5.125915,1.881387,0.301098,7.914355,-2.974221,-4.005606,-7.754679,-2.778285,2.611572,-2.145455,-0.098924,9.984376,2.651954,4.100394,-5.693955,5.055677,5.242739,4.156171,5.893282,7.761915,-4.131371,-4.327049,1.018728,-1.332980,6.670034,-5.899332,9.091349,2.967942,-2.333229,-4.526907,5.015365,-4.109618,-5.683825,4.467741,-0.108973,-8.508081,4.439209,2.183456,3.025070,7.445037,-0.083695,-1.443626,-5.048088,-4.700301,-3.446446,5.917627,-4.075276,7.142418,5.882663,-9.702161,0.829099,2.394481,9.430272,1.171179,-2.614456,-6.687070,-2.644729,-3.231023,-2.882877,-0.214429,1.336150,-8.118625,2.777082,8.584550,-2.159100,-3.440742,-8.092104,-1.854558,-7.807635,-5.073606,1.353056,1.538270,-4.844959,-7.550153,-7.557775,2.723311,-4.161692,-6.109673,7.089425,1.594157,3.365394,-0.505159,5.018038,-9.459282,-8.657924,-3.681744,0.561319,-1.846643,4.494813,-3.374754,9.149721,-7.790961,1.627853,4.351374,-3.164671,-0.533676,-6.349924,2.910059,-2.753079,1.680669,-5.071512,-6.359072,6.035229,3.203727,6.249771,-0.930398,-7.505305,-8.703832,5.004687,-0.732479,-5.873453,-5.907715,7.918771,-6.716297,9.527257,0.729672,9.821157,8.592380,-5.912468,-2.337961,-8.475365,-9.849681,6.573728,-5.757884,-8.529035,-5.418952,8.009064,0.578661,-9.468850,-0.824003,6.798059,5.536977,3.586277,7.065158,-0.582109,6.278641,-0.861345,4.454090,3.146160,1.287325,-9.459291,-0.213355,-9.509030,1.383295,-1.887071,-6.574898,1.352453,-5.084446,-3.759261,-8.693172,0.209345,3.048669,0.699103,2.009722,-7.385485,-8.959100,-0.053364,-2.176095,-1.629216,6.449916,-7.990452,-6.839970,-9.885128,-8.650344,-6.110732,2.838727,5.851217,8.979221,9.396477,9.251598,2.371792,-9.482018,-4.422720,-7.444450,-7.259676,2.004159,5.654614,-2.816999,8.039685,-7.696146,1.128625,0.557709,-1.375881,5.046103,-8.781002,7.169149,-3.993605,3.471599,4.688060,8.685117,-3.687984,-8.631757,-1.840281,5.360056,4.146081,9.810536,2.764799,2.672560,-1.876013,7.111026,2.859239,-5.668065,-4.557749,8.276226,-9.260868,-0.341082,6.686090,-3.648560,2.682417,6.542940,-7.480541,-2.578927,-0.456409,4.835866,-1.973351,9.176482,-6.599111,-4.833242,6.889241,-3.818141,-1.788197,-4.062554,6.592395,-7.052311,-5.010809,9.468146,-0.822274,-0.389056,-5.902672,3.691910,-3.942663,-0.558076,3.043710,-0.619781,-5.448237,-3.090956,2.163616,3.553534,8.462922,8.404767,1.405323,-4.873959,-5.696146,-1.603054,4.437299,-3.337415,-2.660679,-1.769491,2.833569,1.987022,3.779698,-2.949132,-6.835021,3.476414,2.830890,-8.030546,6.664324,2.008345,7.937395,-5.996325,4.485312,0.100011,-2.049805,7.324476,-9.532943,2.651259,-4.695738,-2.645545,9.427510,6.492431,-8.704785,-6.835189,-9.040944,-2.069846,8.480784,-8.368464,3.000271,4.271986,4.612753,1.301166,0.044677,4.000289,-2.879138,-9.905580,9.803567,9.887963,0.161796,-9.862218,4.593851,-6.394285,3.306132,6.809920,-1.379965,-2.973436,-0.273659,0.499797,2.563933,8.300438,-6.408306,9.734339,3.912843,3.988243,-2.504993,8.490584,-9.049237,5.972789,-0.817525,-1.049476,0.092415,8.772784,-6.502048,0.809107,3.263592,-6.531695,-5.511046,-3.137148,-8.096679,1.428651,6.950403,-8.214869,-9.141168,8.083041,-7.169255,9.816514,5.575651,8.111066,8.542643,3.324306,-9.684849,-5.937315,5.689599,-8.317757,-7.054931,0.959370,-1.960634,-0.119294,0.819815,-2.245396,4.332923,6.469061,-9.658047,9.191047,6.591882,-7.802149,-9.063338,-5.398842,0.889845,9.992171,-0.565100,6.967507,-0.317299,1.977284,-9.499048,7.128368,2.350919,-5.883791,-2.228990,9.293678,-6.207199,6.875771,-5.557821,-9.629907,-4.953829,-9.892960,-7.520321,-7.914436,0.023880,-9.238583,1.452456,9.227577,-4.645487,-3.532564,1.232718,-2.936150,3.371773,-0.398035,-5.221704,-0.083586,-6.219221,0.016871,-1.441843,6.192572,-5.020721,2.765952,-5.355902,-6.611850,-4.821455,5.161386,8.885797,6.585604,8.638927,-9.766670,8.834685,-1.732304,2.122224,-6.431633,3.553067,9.675996,-2.674655,9.600164,-5.709065,9.354141,-7.860745,-8.990893,4.708997,0.697663,-5.579450,-7.184513,-4.888143,4.517387,-1.085076,2.883426,-2.441138,2.344228,-6.041374,2.570255,4.220835,4.227904,4.680961,1.583657,-4.162190,8.365453,-8.979796,-8.420611,-2.512358,3.575654,2.735422,0.464945,1.138830,-4.105089,8.729493,-5.674867,3.493440,5.040911,-4.894482,6.754105,6.818113,3.911150,-9.531111,-8.570151,5.120289,7.200053,-1.920961,-2.016300,-3.846922,5.704019,-9.565661,-2.344340,-5.237639,-2.405097,-8.114026,3.757306,-8.485225,7.503263,-2.167275,-7.371343,4.665763,-6.035482,-0.285720,-9.467919,-5.789698,-9.678543,1.423967,-0.822335,-9.755756,-4.731835,-0.727471,-3.298697,-1.084526,6.319440,8.266501,7.213298,3.327932,1.557672,-6.142910,-8.745767,8.027619,-5.987621,0.890282,-9.027558,5.838427,-4.840246,-1.849551,7.817736,6.394247,2.537088,-2.035529,7.576420,7.238194,0.475201,-5.160076,-0.886733,-0.137920,7.331264,4.856504,-0.761103,-0.913946,-7.752781,4.516361,-0.562194,-9.126052,-1.073705,-5.297414,-3.420560,-4.277512,2.550901,-4.035760,-3.352529,-5.636772,-7.130118,-1.330462,0.657095,-8.480482,2.134098,9.126870,-7.788628,-0.866437,-7.511634,-7.597656,-9.012053,-1.585392,-1.866154,7.620104,8.415603,-3.977322,3.273856,-4.737552,4.726180,-9.536234,9.903412,-0.312988,1.601790,-0.067961,7.014614,-3.202775,0.577028,-8.518806,8.125838,-4.571210,5.907380,2.213663,3.057202,1.256089,-9.104774,-8.563319,3.498685,5.855039,2.956173,-5.600770,-6.002752,-1.125107,3.619467,9.731412,-6.945315,-3.924736,-8.262926,-2.195323,5.179303,7.015719,2.703385,6.537609,-0.262238,0.842629,-5.040471,6.996250,-1.399933,-3.511028,-6.968997,8.640869,-5.577227,-2.153848,5.582443,-5.251122,6.989462,-7.363707,1.488968,9.380492,-0.519669,0.712597,2.761696,4.996277,-8.929346,5.667167,-1.850916,2.026888,-6.474211,5.660572,-3.394460,0.190116,5.418610,-0.242955,6.563527,0.233616,-5.478813,5.674881,4.715364,-7.909856,-5.201162,-5.895295,-4.528769,3.424578,7.943374,-0.722813,9.861281,7.739901,7.328720,6.332383,-6.733788,-1.189731,-6.449006,-9.103714,-3.291063,6.125382,-2.885802,2.006257,-7.208307,-2.617153,-8.552928,3.169809,-9.010780,-6.861485,2.282237,-0.208512,-3.341763,-4.105538,-0.367389,-3.581096,0.054140,-9.835535,4.216637,-3.998606,-0.337333,-8.672348,1.597965,-7.844009,-4.522711,2.802179,6.905727,1.138848,-9.180683,-7.127951,-9.909979,-0.170250,-6.703708,-9.588915,-5.708990,2.912259,9.841347,1.080729,-9.278463,-2.930320,6.596661,-7.385065,6.229759,-1.869902,2.595821,6.885627,-9.601343,-8.297041,-1.684710,-1.603626,3.447024,2.744177,5.642576,-7.761689,8.676755,7.051928,-0.950762,6.767037,9.206893,-7.602671,-1.076817,5.272637,0.066179,2.230613,-1.622685,-6.549933,-2.268242,-4.538704,5.488948,7.663742,6.419978,5.766373,-0.109084,0.652561,-7.390626,-7.006463,7.575846,3.599396,2.131150,-3.852961,3.930254,-5.951167,3.769835,9.380288,9.417090,2.327436,7.314323,-5.711113,7.813330,-4.727785,6.988499,-4.576318,-0.753889,9.912026,-2.494615,3.014949,5.704840,9.794777,-9.401322,9.563480,6.097887,-4.047946,6.468765,-7.057281,-1.712913,-4.958285,-6.129328,7.597103,2.751902,-2.316039,-5.479404,0.138873,2.874524,-9.856996,4.763763,7.657922,-5.054123,-4.728069,5.159478,-1.005762,2.511609,9.915585,4.116704,-7.320124,-5.962599,0.732472,-8.167009,-0.816844,6.299002,3.559381,-5.706136,-5.936871,-4.920941,-3.402841,2.058099,0.664214,3.270778,-4.148811,0.486185,4.654946,-0.583973,8.791005,6.233316,-9.721448,-2.562017,-3.214597,2.356051,-4.778192,7.152491,9.176157,2.496260,8.904473,7.897155,-6.267336,-2.320858,-0.925462,-0.633295,9.225826,6.675083,-8.772844,8.388633,-8.541160,5.798205,-2.099164,0.883724,-4.161555,-9.222910,-2.003742,2.542286,9.660309,-7.700428,-2.832194,5.593274], dtype = "float32")#candidate|6593|(784,)|const|float32
call_6592 = relay.TupleGetItem(func_3850_call(relay.reshape(const_6593.astype('float32'), [784,])), 0)
call_6594 = relay.TupleGetItem(func_3853_call(relay.reshape(const_6593.astype('float32'), [784,])), 0)
func_3037_call = mod.get_global_var('func_3037')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_6597 = relay.TupleGetItem(func_3037_call(), 0)
call_6598 = relay.TupleGetItem(func_3038_call(), 0)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_6606 = relay.TupleGetItem(func_1716_call(), 0)
call_6607 = relay.TupleGetItem(func_1717_call(), 0)
output = relay.Tuple([call_6554,call_6559,call_6561,call_6592,const_6593,call_6597,call_6606,])
output2 = relay.Tuple([call_6555,call_6560,call_6562,call_6594,const_6593,call_6598,call_6607,])
func_6616 = relay.Function([], output)
mod['func_6616'] = func_6616
mod = relay.transform.InferType()(mod)
mutated_mod['func_6616'] = func_6616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6616_call = mutated_mod.get_global_var('func_6616')
call_6617 = func_6616_call()
output = call_6617
func_6618 = relay.Function([], output)
mutated_mod['func_6618'] = func_6618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4344_call = mod.get_global_var('func_4344')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_6621 = relay.TupleGetItem(func_4344_call(), 0)
call_6622 = relay.TupleGetItem(func_4345_call(), 0)
func_4344_call = mod.get_global_var('func_4344')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_6624 = relay.TupleGetItem(func_4344_call(), 1)
call_6625 = relay.TupleGetItem(func_4345_call(), 1)
output = relay.Tuple([call_6621,call_6624,])
output2 = relay.Tuple([call_6622,call_6625,])
func_6628 = relay.Function([], output)
mod['func_6628'] = func_6628
mod = relay.transform.InferType()(mod)
output = func_6628()
func_6629 = relay.Function([], output)
mutated_mod['func_6629'] = func_6629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3295_call = mod.get_global_var('func_3295')
func_3296_call = mutated_mod.get_global_var('func_3296')
call_6635 = relay.TupleGetItem(func_3295_call(), 0)
call_6636 = relay.TupleGetItem(func_3296_call(), 0)
func_5131_call = mod.get_global_var('func_5131')
func_5133_call = mutated_mod.get_global_var('func_5133')
call_6649 = relay.TupleGetItem(func_5131_call(), 2)
call_6650 = relay.TupleGetItem(func_5133_call(), 2)
output = relay.Tuple([call_6635,call_6649,])
output2 = relay.Tuple([call_6636,call_6650,])
func_6662 = relay.Function([], output)
mod['func_6662'] = func_6662
mod = relay.transform.InferType()(mod)
mutated_mod['func_6662'] = func_6662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6662_call = mutated_mod.get_global_var('func_6662')
call_6663 = func_6662_call()
output = call_6663
func_6664 = relay.Function([], output)
mutated_mod['func_6664'] = func_6664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2944_call = mod.get_global_var('func_2944')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_6668 = relay.TupleGetItem(func_2944_call(), 0)
call_6669 = relay.TupleGetItem(func_2945_call(), 0)
var_6671 = relay.var("var_6671", dtype = "uint16", shape = (6, 5, 4))#candidate|6671|(6, 5, 4)|var|uint16
bop_6672 = relay.equal(call_6668.astype('bool'), relay.reshape(var_6671.astype('bool'), relay.shape_of(call_6668))) # shape=(6, 5, 4)
bop_6675 = relay.equal(call_6669.astype('bool'), relay.reshape(var_6671.astype('bool'), relay.shape_of(call_6669))) # shape=(6, 5, 4)
output = bop_6672
output2 = bop_6675
func_6679 = relay.Function([var_6671,], output)
mod['func_6679'] = func_6679
mod = relay.transform.InferType()(mod)
var_6680 = relay.var("var_6680", dtype = "uint16", shape = (6, 5, 4))#candidate|6680|(6, 5, 4)|var|uint16
output = func_6679(var_6680)
func_6681 = relay.Function([var_6680], output)
mutated_mod['func_6681'] = func_6681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_6697 = relay.TupleGetItem(func_1397_call(), 0)
call_6698 = relay.TupleGetItem(func_1399_call(), 0)
output = call_6697
output2 = call_6698
func_6699 = relay.Function([], output)
mod['func_6699'] = func_6699
mod = relay.transform.InferType()(mod)
mutated_mod['func_6699'] = func_6699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6699_call = mutated_mod.get_global_var('func_6699')
call_6700 = func_6699_call()
output = call_6700
func_6701 = relay.Function([], output)
mutated_mod['func_6701'] = func_6701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_6757 = relay.TupleGetItem(func_1431_call(), 0)
call_6758 = relay.TupleGetItem(func_1433_call(), 0)
output = call_6757
output2 = call_6758
func_6784 = relay.Function([], output)
mod['func_6784'] = func_6784
mod = relay.transform.InferType()(mod)
mutated_mod['func_6784'] = func_6784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6784_call = mutated_mod.get_global_var('func_6784')
call_6785 = func_6784_call()
output = call_6785
func_6786 = relay.Function([], output)
mutated_mod['func_6786'] = func_6786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6171_call = mod.get_global_var('func_6171')
func_6172_call = mutated_mod.get_global_var('func_6172')
call_6792 = relay.TupleGetItem(func_6171_call(), 1)
call_6793 = relay.TupleGetItem(func_6172_call(), 1)
func_3904_call = mod.get_global_var('func_3904')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_6795 = func_3904_call()
call_6796 = func_3904_call()
func_3981_call = mod.get_global_var('func_3981')
func_3983_call = mutated_mod.get_global_var('func_3983')
call_6820 = relay.TupleGetItem(func_3981_call(), 1)
call_6821 = relay.TupleGetItem(func_3983_call(), 1)
func_3197_call = mod.get_global_var('func_3197')
func_3199_call = mutated_mod.get_global_var('func_3199')
call_6824 = relay.TupleGetItem(func_3197_call(), 2)
call_6825 = relay.TupleGetItem(func_3199_call(), 2)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_6830 = func_1270_call()
call_6831 = func_1270_call()
func_6100_call = mod.get_global_var('func_6100')
func_6101_call = mutated_mod.get_global_var('func_6101')
call_6843 = relay.TupleGetItem(func_6100_call(), 0)
call_6844 = relay.TupleGetItem(func_6101_call(), 0)
output = relay.Tuple([call_6792,call_6795,call_6820,call_6824,call_6830,call_6843,])
output2 = relay.Tuple([call_6793,call_6796,call_6821,call_6825,call_6831,call_6844,])
func_6857 = relay.Function([], output)
mod['func_6857'] = func_6857
mod = relay.transform.InferType()(mod)
mutated_mod['func_6857'] = func_6857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6857_call = mutated_mod.get_global_var('func_6857')
call_6858 = func_6857_call()
output = call_6858
func_6859 = relay.Function([], output)
mutated_mod['func_6859'] = func_6859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5131_call = mod.get_global_var('func_5131')
func_5133_call = mutated_mod.get_global_var('func_5133')
call_6887 = relay.TupleGetItem(func_5131_call(), 1)
call_6888 = relay.TupleGetItem(func_5133_call(), 1)
var_6889 = relay.var("var_6889", dtype = "float32", shape = (14, 5, 4))#candidate|6889|(14, 5, 4)|var|float32
bop_6890 = relay.floor_mod(call_6887.astype('float32'), var_6889.astype('float32')) # shape=(14, 5, 4)
bop_6893 = relay.floor_mod(call_6888.astype('float32'), var_6889.astype('float32')) # shape=(14, 5, 4)
func_4905_call = mod.get_global_var('func_4905')
func_4907_call = mutated_mod.get_global_var('func_4907')
var_6896 = relay.var("var_6896", dtype = "float64", shape = (600,))#candidate|6896|(600,)|var|float64
call_6895 = relay.TupleGetItem(func_4905_call(relay.reshape(var_6896.astype('float64'), [600,])), 1)
call_6897 = relay.TupleGetItem(func_4907_call(relay.reshape(var_6896.astype('float64'), [600,])), 1)
func_2682_call = mod.get_global_var('func_2682')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_6905 = relay.TupleGetItem(func_2682_call(), 0)
call_6906 = relay.TupleGetItem(func_2684_call(), 0)
output = relay.Tuple([bop_6890,call_6895,var_6896,call_6905,])
output2 = relay.Tuple([bop_6893,call_6897,var_6896,call_6906,])
func_6923 = relay.Function([var_6889,var_6896,], output)
mod['func_6923'] = func_6923
mod = relay.transform.InferType()(mod)
mutated_mod['func_6923'] = func_6923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6923_call = mutated_mod.get_global_var('func_6923')
var_6925 = relay.var("var_6925", dtype = "float32", shape = (14, 5, 4))#candidate|6925|(14, 5, 4)|var|float32
var_6926 = relay.var("var_6926", dtype = "float64", shape = (600,))#candidate|6926|(600,)|var|float64
call_6924 = func_6923_call(var_6925,var_6926,)
output = call_6924
func_6927 = relay.Function([var_6925,var_6926,], output)
mutated_mod['func_6927'] = func_6927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6953 = relay.var("var_6953", dtype = "float64", shape = (1, 3, 3))#candidate|6953|(1, 3, 3)|var|float64
uop_6954 = relay.sin(var_6953.astype('float64')) # shape=(1, 3, 3)
output = relay.Tuple([uop_6954,])
output2 = relay.Tuple([uop_6954,])
func_6962 = relay.Function([var_6953,], output)
mod['func_6962'] = func_6962
mod = relay.transform.InferType()(mod)
mutated_mod['func_6962'] = func_6962
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6963 = relay.var("var_6963", dtype = "float64", shape = (1, 3, 3))#candidate|6963|(1, 3, 3)|var|float64
func_6962_call = mutated_mod.get_global_var('func_6962')
call_6964 = func_6962_call(var_6963)
output = call_6964
func_6965 = relay.Function([var_6963], output)
mutated_mod['func_6965'] = func_6965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_7082 = relay.TupleGetItem(func_1597_call(), 0)
call_7083 = relay.TupleGetItem(func_1599_call(), 0)
func_4475_call = mod.get_global_var('func_4475')
func_4478_call = mutated_mod.get_global_var('func_4478')
const_7088 = relay.const([-9.194525,-1.603268,1.004640,-4.174343,-9.628757,1.083164,-1.039957,5.603176,1.948939,-8.550734,7.433275,9.489099,-2.001266,-2.715846,-8.975468,-0.425606,5.958557,3.300007,6.833256,2.095846,4.749314,-8.856623,-9.934678,-7.203610,0.916358,-4.423750,-6.968982,-9.103294,-0.814657,-2.860547,-2.250233,1.356071,-5.156831,-3.010373,-1.467577,7.310624,-0.236032,-3.253680,1.564209,3.157066,0.862936,0.828883,3.753500,4.289534,-1.769986,-4.133460,-4.796071,-0.773886,7.017210,7.771646,-0.815393,3.613136,-6.235839,-9.481786,-6.015696,-1.609448,0.534161,8.505783,1.036617,-5.391588,-4.376765,7.460204,-0.617193,5.932527,-4.444223,-3.256252,-2.071618,-4.895524,6.017821,-5.050218,-6.909705,2.755061,0.009348,-3.075064,1.699506,-3.815007,3.863705,5.206272,-5.570869,7.198700,5.817241,7.058861,0.810896,-0.857664,-7.837507,-6.979295,-2.525597,-8.257111,-8.746517,-0.027123,4.390845,-9.670488,-9.662982,0.631537,-8.947178,-9.149339,-4.911428,0.695203,7.669799,-0.634334,0.801536,-4.300764,-7.622669,1.603647,2.736085,4.274327,-3.867723,2.177664,1.744639,4.603381,-8.707618,8.899873,-5.504129,-7.818536,-7.774182,0.534057,-9.799469,2.228358,9.645839,7.387075,8.291589,3.295886,-1.476979,-8.641424,5.409984,-5.521546,4.492507,-7.076643,-3.097752,3.453019,6.925781,-9.063604,-1.020581,2.882112,-9.258729,-5.296613,9.520301,-9.685465,2.506547,8.772979,-2.101289,-0.065766,1.509815,2.804521,2.455985,-6.709157,-2.495241,-3.485688,2.068080,-5.109102,0.523207,7.403854,-8.867674,-1.201973,-7.964281,3.186957,9.206144,3.497208,-7.165229,1.320736,3.800490,0.686935,-3.347209,0.898620,2.897649,-9.862706,-1.601922,0.864966,2.916747,-7.226283,3.419221,-2.850582,1.923824,3.871440,4.800138,-6.727801,-5.570108,-9.840861,7.115498,-7.592102,4.438914,7.119789,-2.853518,-6.811152,4.900273,-3.237368,-4.781925,3.010609,-3.449962,-2.744537,6.784287,-3.085870,-1.161842,1.398524,-1.532003,-8.660764,-9.130358,-8.956733,-8.394536,-0.980438,8.694178,-2.431924,9.294877,-6.296658,-5.720510,6.187974,9.683350,2.171057,-6.389593,9.942197,6.253932,-5.472638,-1.533008,-4.255735,-3.617586,-5.671453,7.698093,5.013309,-8.659211,-5.617316,-7.070418,4.975574,-2.261989,4.761001,0.968933,1.016930,-4.701435,-8.345590,-8.132943,4.028471,9.268694,2.758968,-0.918890,8.212193,-5.072123,7.188421,-1.062376,-7.739230,-8.126775,5.166397,-6.902337,-4.112624,4.229879,5.117941,4.300479,-6.472654,-9.326676,-3.863550,-6.918936,-2.610803,8.218914,-3.006885,-5.170268,-4.603858,-2.898145,-2.928094,4.659283,-5.513175,2.305091,-2.199703,-1.842525,2.891111,-2.340441,-3.601980,3.774133,3.613710,-3.759388,-4.968021,-1.984579,8.473791,7.505748,-9.148430,-2.870523,3.792483,-2.781667,8.350555,-8.426204,-2.796009,-3.150430,4.785567,7.709474,-8.027451,-8.599381,-3.209276,-6.021357,-7.761541,9.825123,-1.440448,4.016596,6.931986,3.855735,-6.843539,7.740607,5.859635,2.991830,1.100590,6.829110,4.079075,8.817309,4.976039,9.967301,0.994958,-0.316899,0.717671,3.035097,6.673539,9.177882,-2.861917,-3.969373,-6.969109,-6.751120,-6.098605,3.531104,-7.270981,0.381609,-1.273028,1.876435,8.783760,8.751573,2.528677,4.713976,-5.932943,-8.896456,4.538992,-2.534096,3.556968,-6.665377,-1.610138,9.016853,-7.205808,-1.576210,9.960211,-1.274584,5.795874,1.795080,-6.436608,-1.386362,7.435069,7.151115,6.513027,-3.263934,-8.674864,3.738124,0.870516,9.180115,9.286148,-7.354989,7.561438,-6.898796,4.001082,1.157689,-8.104532,-9.435563,3.316776,3.822142,5.922398,1.812234,-2.995361,-2.474731,6.534798,7.582417,-9.042537,0.817266,-6.363520,-8.422174,-0.790470,2.125504,2.681120,-9.397456,1.282234,-8.342480,-2.934981,-8.779661,-8.365368,-6.489532,2.491127,-5.558756,4.799495,8.367054,7.841270,8.177848,-3.489052,1.346743,-5.337594,-4.268818,9.449252,-5.501754,-2.876066,-9.544039,-5.102325,-4.351040,-7.124680,4.835684,-9.591725,5.201173,-0.112986,3.283787,9.613988,4.846971,4.850370,7.886839,-5.342871,-5.840824,-3.577857,8.725614,2.302778,-6.271217,-8.089730,0.315076,8.256393,3.155183,-3.601993,-4.228889,0.215043,5.371865,2.055100,8.594727,1.458858,-0.091993,-3.305673,-2.109771,5.521978,7.656936,-7.533898,-9.158354,5.987484,9.377778,6.144183,6.482505,0.011769,5.804382,5.883612,-1.995879,-3.872618,-5.231343,-6.187620,-9.426445,-4.974388,-3.070750,-4.547228,-8.758074,-4.942349,8.600287,1.226237,-8.130465,-5.969748,4.418754,-8.001835,-2.562198,-0.891289,0.398875,4.783721,-9.999940,2.178500,-0.672292,2.491799,6.108407,-0.579825,8.877039,3.458692,2.137920,7.353766,3.019172,-5.189833,-6.011037,-3.780310,-9.716292,1.504471,4.504306,8.225017,1.480231,-3.486000,-9.757740,9.547255,-2.769768,5.628626,-9.372101,-3.750371,-0.976763,5.431611,5.883989,-2.241475,8.155387,-3.425981,-7.047587,-3.952299,6.202875,-5.551183,-8.772987,2.297936,-3.403455,-4.480463,-8.496297,-7.464579,4.986147,8.346432,8.724243,-4.682180,-8.901794,-3.433757,-6.325086,-4.140864,8.091491,7.524404,-8.347245,9.896482,2.174602,-2.168300,-3.938427,-1.168045,-1.634683,6.771602,4.627116,3.035349,-5.388232,-1.522286,-7.130934,-5.290993,1.715092,9.796298,3.096707,-0.864774,-3.569498,-5.357790,1.981146,8.591336,-7.478587,-0.553383,-1.652529,1.493866,4.107956,-4.057610,-3.687389,4.505431,-8.846931,-8.379392,7.930659,2.347990,4.183084,1.824317,-0.536445,-0.508075,7.946425,4.825968,-4.417801,-2.201798,-0.645072,-2.040535,-8.277197,4.405346,-1.712559,-0.640402,-2.188627,-2.113043,3.099839,6.296764,-4.684873,-0.718204,-7.624707,6.052639,9.811450,-8.148429,-0.348874,-9.480219,-1.409847,-7.670882,8.309738,0.853821,-6.232798,0.191530,7.677872,8.869779,5.999736,4.893692,2.191902,-3.489576,-0.519268,3.070485,6.881881,7.362011,8.073498,8.173294,-2.848978,-6.614793,-4.272605,-4.646682,-3.249015,2.357059,-1.732650,4.023243,6.399688,-2.432443,-9.778529,3.583902,4.943728,-4.943841,-4.401039,-1.407276,-2.368780,0.585122], dtype = "float64")#candidate|7088|(600,)|const|float64
call_7087 = relay.TupleGetItem(func_4475_call(relay.reshape(const_7088.astype('float64'), [600,])), 0)
call_7089 = relay.TupleGetItem(func_4478_call(relay.reshape(const_7088.astype('float64'), [600,])), 0)
func_5048_call = mod.get_global_var('func_5048')
func_5049_call = mutated_mod.get_global_var('func_5049')
call_7119 = relay.TupleGetItem(func_5048_call(), 0)
call_7120 = relay.TupleGetItem(func_5049_call(), 0)
var_7122 = relay.var("var_7122", dtype = "int8", shape = (14, 5, 4))#candidate|7122|(14, 5, 4)|var|int8
bop_7123 = relay.bitwise_xor(call_7119.astype('int8'), var_7122.astype('int8')) # shape=(14, 5, 4)
bop_7126 = relay.bitwise_xor(call_7120.astype('int8'), var_7122.astype('int8')) # shape=(14, 5, 4)
func_4543_call = mod.get_global_var('func_4543')
func_4545_call = mutated_mod.get_global_var('func_4545')
call_7142 = relay.TupleGetItem(func_4543_call(), 1)
call_7143 = relay.TupleGetItem(func_4545_call(), 1)
bop_7177 = relay.subtract(call_7142.astype('int64'), call_7119.astype('int64')) # shape=(6, 5, 4)
bop_7180 = relay.subtract(call_7143.astype('int64'), call_7120.astype('int64')) # shape=(6, 5, 4)
output = relay.Tuple([call_7082,call_7087,const_7088,bop_7123,bop_7177,])
output2 = relay.Tuple([call_7083,call_7089,const_7088,bop_7126,bop_7180,])
func_7181 = relay.Function([var_7122,], output)
mod['func_7181'] = func_7181
mod = relay.transform.InferType()(mod)
var_7182 = relay.var("var_7182", dtype = "int8", shape = (14, 5, 4))#candidate|7182|(14, 5, 4)|var|int8
output = func_7181(var_7182)
func_7183 = relay.Function([var_7182], output)
mutated_mod['func_7183'] = func_7183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5239_call = mod.get_global_var('func_5239')
func_5241_call = mutated_mod.get_global_var('func_5241')
call_7203 = relay.TupleGetItem(func_5239_call(), 1)
call_7204 = relay.TupleGetItem(func_5241_call(), 1)
func_6548_call = mod.get_global_var('func_6548')
func_6550_call = mutated_mod.get_global_var('func_6550')
call_7215 = relay.TupleGetItem(func_6548_call(), 0)
call_7216 = relay.TupleGetItem(func_6550_call(), 0)
output = relay.Tuple([call_7203,call_7215,])
output2 = relay.Tuple([call_7204,call_7216,])
func_7223 = relay.Function([], output)
mod['func_7223'] = func_7223
mod = relay.transform.InferType()(mod)
mutated_mod['func_7223'] = func_7223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7223_call = mutated_mod.get_global_var('func_7223')
call_7224 = func_7223_call()
output = call_7224
func_7225 = relay.Function([], output)
mutated_mod['func_7225'] = func_7225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_849_call = mod.get_global_var('func_849')
func_851_call = mutated_mod.get_global_var('func_851')
call_7262 = relay.TupleGetItem(func_849_call(), 0)
call_7263 = relay.TupleGetItem(func_851_call(), 0)
output = relay.Tuple([call_7262,])
output2 = relay.Tuple([call_7263,])
func_7266 = relay.Function([], output)
mod['func_7266'] = func_7266
mod = relay.transform.InferType()(mod)
output = func_7266()
func_7267 = relay.Function([], output)
mutated_mod['func_7267'] = func_7267
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7302 = relay.var("var_7302", dtype = "float32", shape = (4, 1, 12))#candidate|7302|(4, 1, 12)|var|float32
uop_7303 = relay.atanh(var_7302.astype('float32')) # shape=(4, 1, 12)
func_5055_call = mod.get_global_var('func_5055')
func_5056_call = mutated_mod.get_global_var('func_5056')
call_7316 = relay.TupleGetItem(func_5055_call(), 0)
call_7317 = relay.TupleGetItem(func_5056_call(), 0)
uop_7321 = relay.atan(uop_7303.astype('float32')) # shape=(4, 1, 12)
output = relay.Tuple([call_7316,uop_7321,])
output2 = relay.Tuple([call_7317,uop_7321,])
F = relay.Function([var_7302,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7302,], output2)
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
