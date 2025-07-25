import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_0 = relay.var("var_0", dtype = "float64", shape = (5, 15, 6))#candidate|0|(5, 15, 6)|var|float64
uop_1 = relay.exp(var_0.astype('float64')) # shape=(5, 15, 6)
output = relay.Tuple([uop_1,])
output2 = relay.Tuple([uop_1,])
func_9 = relay.Function([var_0,], output)
mod['func_9'] = func_9
mod = relay.transform.InferType()(mod)
mutated_mod['func_9'] = func_9
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10 = relay.var("var_10", dtype = "float64", shape = (5, 15, 6))#candidate|10|(5, 15, 6)|var|float64
func_9_call = mutated_mod.get_global_var('func_9')
call_11 = func_9_call(var_10)
output = call_11
func_12 = relay.Function([var_10], output)
mutated_mod['func_12'] = func_12
mutated_mod = relay.transform.InferType()(mutated_mod)
var_512 = relay.var("var_512", dtype = "float64", shape = (6, 3, 3))#candidate|512|(6, 3, 3)|var|float64
const_513 = relay.const([[[-0.094461,1.318921,1.085882],[-6.560715,-7.505453,3.820286],[-8.468012,4.585571,-2.525250]],[[-2.710501,-7.766494,0.006852],[-6.221809,-1.912885,-2.613251],[-1.414310,2.847343,-1.102369]],[[-2.999936,8.263332,8.378836],[-5.054051,1.824295,-8.995279],[-3.194482,-7.069489,-3.253068]],[[-7.732463,-3.429215,5.524249],[-5.693627,-8.319963,5.685603],[-7.673092,4.850002,2.541571]],[[3.468867,-2.322323,8.502287],[-3.554085,-7.605978,-3.633423],[-6.188272,2.521081,5.204879]],[[-8.934085,-5.005188,7.035505],[7.978876,6.679222,-9.588113],[2.994695,-5.230140,-8.656868]]], dtype = "float64")#candidate|513|(6, 3, 3)|const|float64
bop_514 = relay.divide(var_512.astype('float64'), relay.reshape(const_513.astype('float64'), relay.shape_of(var_512))) # shape=(6, 3, 3)
func_9_call = mod.get_global_var('func_9')
func_12_call = mutated_mod.get_global_var('func_12')
var_520 = relay.var("var_520", dtype = "float64", shape = (50, 9))#candidate|520|(50, 9)|var|float64
call_519 = relay.TupleGetItem(func_9_call(relay.reshape(var_520.astype('float64'), [5, 15, 6])), 0)
call_521 = relay.TupleGetItem(func_12_call(relay.reshape(var_520.astype('float64'), [5, 15, 6])), 0)
uop_527 = relay.cosh(bop_514.astype('float32')) # shape=(6, 3, 3)
func_9_call = mod.get_global_var('func_9')
func_12_call = mutated_mod.get_global_var('func_12')
call_550 = relay.TupleGetItem(func_9_call(relay.reshape(call_519.astype('float64'), [5, 15, 6])), 0)
call_551 = relay.TupleGetItem(func_12_call(relay.reshape(call_519.astype('float64'), [5, 15, 6])), 0)
output = relay.Tuple([call_519,var_520,uop_527,call_550,])
output2 = relay.Tuple([call_521,var_520,uop_527,call_551,])
func_555 = relay.Function([var_512,var_520,], output)
mod['func_555'] = func_555
mod = relay.transform.InferType()(mod)
var_556 = relay.var("var_556", dtype = "float64", shape = (6, 3, 3))#candidate|556|(6, 3, 3)|var|float64
var_557 = relay.var("var_557", dtype = "float64", shape = (50, 9))#candidate|557|(50, 9)|var|float64
output = func_555(var_556,var_557,)
func_558 = relay.Function([var_556,var_557,], output)
mutated_mod['func_558'] = func_558
mutated_mod = relay.transform.InferType()(mutated_mod)
const_661 = relay.const([[-5.345281,2.761900,-7.519725],[6.023384,9.093359,-8.461420],[7.966260,7.085226,0.534918],[6.453354,-7.158952,1.268606],[-7.659101,2.519089,-4.814766],[0.176275,-5.219299,-2.665281],[3.846080,7.351260,-0.911036],[-8.471015,-9.594355,9.755433],[0.703315,9.905170,1.859427],[3.246211,6.849621,2.572088],[2.528457,-4.768223,3.080773],[3.776130,8.793229,9.692960],[-3.655854,8.078528,-9.417305]], dtype = "float64")#candidate|661|(13, 3)|const|float64
uop_662 = relay.sigmoid(const_661.astype('float64')) # shape=(13, 3)
output = relay.Tuple([uop_662,])
output2 = relay.Tuple([uop_662,])
func_665 = relay.Function([], output)
mod['func_665'] = func_665
mod = relay.transform.InferType()(mod)
output = func_665()
func_666 = relay.Function([], output)
mutated_mod['func_666'] = func_666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_703 = relay.TupleGetItem(func_665_call(), 0)
call_704 = relay.TupleGetItem(func_666_call(), 0)
output = call_703
output2 = call_704
func_736 = relay.Function([], output)
mod['func_736'] = func_736
mod = relay.transform.InferType()(mod)
output = func_736()
func_737 = relay.Function([], output)
mutated_mod['func_737'] = func_737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_747 = relay.TupleGetItem(func_665_call(), 0)
call_748 = relay.TupleGetItem(func_666_call(), 0)
output = call_747
output2 = call_748
func_753 = relay.Function([], output)
mod['func_753'] = func_753
mod = relay.transform.InferType()(mod)
output = func_753()
func_754 = relay.Function([], output)
mutated_mod['func_754'] = func_754
mutated_mod = relay.transform.InferType()(mutated_mod)
var_779 = relay.var("var_779", dtype = "uint8", shape = ())#candidate|779|()|var|uint8
var_780 = relay.var("var_780", dtype = "uint8", shape = (7, 2, 14))#candidate|780|(7, 2, 14)|var|uint8
bop_781 = relay.equal(var_779.astype('bool'), var_780.astype('bool')) # shape=(7, 2, 14)
output = bop_781
output2 = bop_781
func_784 = relay.Function([var_779,var_780,], output)
mod['func_784'] = func_784
mod = relay.transform.InferType()(mod)
mutated_mod['func_784'] = func_784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_784_call = mutated_mod.get_global_var('func_784')
var_786 = relay.var("var_786", dtype = "uint8", shape = ())#candidate|786|()|var|uint8
var_787 = relay.var("var_787", dtype = "uint8", shape = (7, 2, 14))#candidate|787|(7, 2, 14)|var|uint8
call_785 = func_784_call(var_786,var_787,)
output = call_785
func_788 = relay.Function([var_786,var_787,], output)
mutated_mod['func_788'] = func_788
mutated_mod = relay.transform.InferType()(mutated_mod)
var_793 = relay.var("var_793", dtype = "float64", shape = (10, 2, 9))#candidate|793|(10, 2, 9)|var|float64
var_794 = relay.var("var_794", dtype = "float64", shape = (10, 2, 9))#candidate|794|(10, 2, 9)|var|float64
bop_795 = relay.floor_mod(var_793.astype('float64'), relay.reshape(var_794.astype('float64'), relay.shape_of(var_793))) # shape=(10, 2, 9)
var_798 = relay.var("var_798", dtype = "float64", shape = (10, 2, 9))#candidate|798|(10, 2, 9)|var|float64
bop_799 = relay.equal(var_793.astype('bool'), relay.reshape(var_798.astype('bool'), relay.shape_of(var_793))) # shape=(10, 2, 9)
output = relay.Tuple([bop_795,bop_799,])
output2 = relay.Tuple([bop_795,bop_799,])
func_802 = relay.Function([var_793,var_794,var_798,], output)
mod['func_802'] = func_802
mod = relay.transform.InferType()(mod)
mutated_mod['func_802'] = func_802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_802_call = mutated_mod.get_global_var('func_802')
var_804 = relay.var("var_804", dtype = "float64", shape = (10, 2, 9))#candidate|804|(10, 2, 9)|var|float64
var_805 = relay.var("var_805", dtype = "float64", shape = (10, 2, 9))#candidate|805|(10, 2, 9)|var|float64
var_806 = relay.var("var_806", dtype = "float64", shape = (10, 2, 9))#candidate|806|(10, 2, 9)|var|float64
call_803 = func_802_call(var_804,var_805,var_806,)
output = call_803
func_807 = relay.Function([var_804,var_805,var_806,], output)
mutated_mod['func_807'] = func_807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_868 = relay.TupleGetItem(func_665_call(), 0)
call_869 = relay.TupleGetItem(func_666_call(), 0)
output = relay.Tuple([call_868,])
output2 = relay.Tuple([call_869,])
func_872 = relay.Function([], output)
mod['func_872'] = func_872
mod = relay.transform.InferType()(mod)
output = func_872()
func_873 = relay.Function([], output)
mutated_mod['func_873'] = func_873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_872_call = mod.get_global_var('func_872')
func_873_call = mutated_mod.get_global_var('func_873')
call_905 = relay.TupleGetItem(func_872_call(), 0)
call_906 = relay.TupleGetItem(func_873_call(), 0)
output = relay.Tuple([call_905,])
output2 = relay.Tuple([call_906,])
func_907 = relay.Function([], output)
mod['func_907'] = func_907
mod = relay.transform.InferType()(mod)
output = func_907()
func_908 = relay.Function([], output)
mutated_mod['func_908'] = func_908
mutated_mod = relay.transform.InferType()(mutated_mod)
const_960 = relay.const(3, dtype = "uint16")#candidate|960|()|const|uint16
const_961 = relay.const([[[-4,8,-6,3,-2,2],[1,-3,-9,-5,-1,6],[-5,3,-10,3,-9,-2],[-9,-7,-7,-10,10,-5],[6,-3,-4,-1,5,-4],[-10,-9,-10,-4,-7,-10],[9,-3,3,5,1,-8],[-8,-6,4,9,9,-5],[-8,7,-1,10,-5,8]],[[-4,-1,2,1,-10,-4],[-7,10,-9,-4,-5,4],[6,-5,-8,10,7,-8],[3,-8,6,-7,5,8],[4,4,-1,-7,-10,-9],[-7,-2,-2,-3,8,8],[-5,7,-4,-5,7,2],[-8,6,-3,-8,-5,7],[9,-2,3,-10,-7,-8]],[[4,-3,-5,-10,4,-2],[-4,-1,1,6,-2,-8],[10,-3,7,-10,-7,3],[-8,6,2,10,8,-4],[-3,-10,1,-8,-8,-6],[4,-7,8,2,4,7],[6,1,-1,5,-7,9],[-5,-7,-9,7,10,4],[-3,-4,-6,4,-8,-8]],[[-1,-5,9,4,-10,-6],[-7,-2,-6,-7,-3,-7],[-1,3,-7,-2,-5,7],[-8,10,6,-9,-7,-2],[-7,4,-9,1,4,-3],[6,-1,2,-6,1,-10],[-10,-1,-2,-1,-1,3],[6,2,-9,-2,10,-5],[-3,3,-7,-2,4,7]],[[6,6,-3,-9,-2,-2],[8,5,9,-10,-3,6],[-10,10,-4,9,-4,-1],[-4,7,-1,-9,3,9],[-4,-2,-6,6,1,-7],[2,8,4,3,10,-6],[-7,2,-6,1,1,-6],[6,-10,-9,-3,-6,-7],[10,8,7,1,-6,-5]],[[-5,4,-2,3,-4,6],[-10,2,-9,6,-8,9],[6,-1,-4,-9,-5,-5],[3,6,8,1,-10,-6],[2,8,4,-7,-7,5],[7,10,-6,10,2,-7],[9,-10,2,7,10,6],[-3,6,-1,3,6,-1],[-10,-4,-10,-3,-10,5]],[[-1,-8,8,-6,-6,2],[7,7,-1,-10,1,1],[6,8,9,9,-6,2],[8,-6,2,2,-3,7],[-7,-5,10,8,2,-3],[1,-10,7,-2,9,9],[-6,-3,10,-5,6,5],[-7,-1,1,7,-5,1],[-6,7,3,-9,9,-9]],[[1,-7,-3,-4,-9,7],[-10,-4,-1,7,7,5],[1,8,5,10,1,-4],[4,-5,4,3,-8,10],[-9,7,10,8,3,1],[5,-3,-1,-1,6,7],[9,7,-4,-5,2,1],[-3,3,-4,5,8,-6],[-6,5,2,-5,10,8]],[[-6,7,6,-2,-4,6],[-1,-9,-10,1,1,-9],[6,6,3,9,7,-7],[-3,-2,4,-7,1,-8],[-1,5,3,-7,-8,-6],[-8,-8,3,8,6,3],[9,7,-7,9,3,2],[-9,-6,3,-6,9,8],[1,7,7,7,3,-6]],[[-10,8,10,-9,8,-6],[7,4,9,-9,-7,10],[-10,9,-3,-4,1,-6],[2,10,1,3,-1,6],[-10,-2,3,10,-9,5],[-4,-6,-10,6,10,-4],[-5,8,5,-5,9,1],[-9,3,1,-1,8,-10],[4,2,3,2,2,-3]],[[4,-1,5,-2,4,4],[7,10,5,-6,7,2],[4,7,5,-3,8,-9],[10,7,9,9,7,3],[-1,-2,7,-6,9,6],[-3,-3,5,-6,-3,8],[4,-10,-9,4,4,-6],[-3,3,-8,-8,-8,-4],[10,7,-2,-9,-2,-9]]], dtype = "uint16")#candidate|961|(11, 9, 6)|const|uint16
bop_962 = relay.right_shift(const_960.astype('uint16'), const_961.astype('uint16')) # shape=(11, 9, 6)
func_736_call = mod.get_global_var('func_736')
func_737_call = mutated_mod.get_global_var('func_737')
call_983 = func_736_call()
call_984 = func_736_call()
output = relay.Tuple([bop_962,call_983,])
output2 = relay.Tuple([bop_962,call_984,])
func_987 = relay.Function([], output)
mod['func_987'] = func_987
mod = relay.transform.InferType()(mod)
output = func_987()
func_988 = relay.Function([], output)
mutated_mod['func_988'] = func_988
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1043 = relay.var("var_1043", dtype = "float64", shape = (6, 1, 12))#candidate|1043|(6, 1, 12)|var|float64
uop_1044 = relay.rsqrt(var_1043.astype('float64')) # shape=(6, 1, 12)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_1047 = func_753_call()
call_1048 = func_753_call()
output = relay.Tuple([uop_1044,call_1047,])
output2 = relay.Tuple([uop_1044,call_1048,])
func_1073 = relay.Function([var_1043,], output)
mod['func_1073'] = func_1073
mod = relay.transform.InferType()(mod)
var_1074 = relay.var("var_1074", dtype = "float64", shape = (6, 1, 12))#candidate|1074|(6, 1, 12)|var|float64
output = func_1073(var_1074)
func_1075 = relay.Function([var_1074], output)
mutated_mod['func_1075'] = func_1075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_872_call = mod.get_global_var('func_872')
func_873_call = mutated_mod.get_global_var('func_873')
call_1101 = relay.TupleGetItem(func_872_call(), 0)
call_1102 = relay.TupleGetItem(func_873_call(), 0)
func_1073_call = mod.get_global_var('func_1073')
func_1075_call = mutated_mod.get_global_var('func_1075')
const_1114 = relay.const([[-7.463258,0.547859,-7.426985,9.889373,9.591548,3.706162,1.733929,-1.211871,-6.523711,-5.043080,4.682225,-7.833855,8.848653,6.826698,-4.503888,0.997745,3.647093,-0.974608,6.505949,7.518362,-8.797095,2.227198,-1.458642,3.279014,-7.133240,-8.230667,-2.888821,0.944876,4.563534,5.275474,2.713962,-6.111513,5.958448,8.566592,-8.632495,0.068095,2.602603,-9.278304,5.118325,-5.039661,7.724698,1.278469,7.702114,7.416304,-8.613465,-6.508157,8.431057,-2.018868,8.960596,7.538608,-4.893937,-7.412181,7.455630,-9.775315,8.027736,0.681479,7.455717,-9.453862,5.598905,1.949173,-2.257832,-9.269914,-5.126915,-9.549922,-6.567487,3.644904,8.988134,-8.632653,-6.080736,3.968531,4.469019,-4.844548]], dtype = "float64")#candidate|1114|(1, 72)|const|float64
call_1113 = relay.TupleGetItem(func_1073_call(relay.reshape(const_1114.astype('float64'), [6, 1, 12])), 1)
call_1115 = relay.TupleGetItem(func_1075_call(relay.reshape(const_1114.astype('float64'), [6, 1, 12])), 1)
output = relay.Tuple([call_1101,call_1113,const_1114,])
output2 = relay.Tuple([call_1102,call_1115,const_1114,])
func_1127 = relay.Function([], output)
mod['func_1127'] = func_1127
mod = relay.transform.InferType()(mod)
output = func_1127()
func_1128 = relay.Function([], output)
mutated_mod['func_1128'] = func_1128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_872_call = mod.get_global_var('func_872')
func_873_call = mutated_mod.get_global_var('func_873')
call_1159 = relay.TupleGetItem(func_872_call(), 0)
call_1160 = relay.TupleGetItem(func_873_call(), 0)
output = call_1159
output2 = call_1160
func_1173 = relay.Function([], output)
mod['func_1173'] = func_1173
mod = relay.transform.InferType()(mod)
mutated_mod['func_1173'] = func_1173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1173_call = mutated_mod.get_global_var('func_1173')
call_1174 = func_1173_call()
output = call_1174
func_1175 = relay.Function([], output)
mutated_mod['func_1175'] = func_1175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1173_call = mod.get_global_var('func_1173')
func_1175_call = mutated_mod.get_global_var('func_1175')
call_1271 = func_1173_call()
call_1272 = func_1173_call()
func_9_call = mod.get_global_var('func_9')
func_12_call = mutated_mod.get_global_var('func_12')
const_1285 = relay.const([-6.989522,-9.106478,-8.314027,-4.786647,-8.282024,-3.292608,-3.520701,-8.061055,-4.332994,3.893320,6.346049,-0.317298,-6.936768,6.600097,1.069658,-4.571312,-9.824947,2.294169,-5.664636,8.781884,-6.418939,-5.288282,9.404674,1.130554,0.911788,-0.117596,8.628861,-5.049808,-1.999339,8.235270,-9.381368,7.025445,-0.123636,0.281935,-0.239325,-8.694329,-0.588504,6.938440,6.378697,0.769956,4.332796,2.067967,2.806325,-4.819366,-8.645173,3.170472,6.918027,0.727851,0.112771,-1.800404,9.912118,1.757635,9.628115,6.784007,3.230578,1.240376,7.970504,6.121832,-0.215790,-5.525085,-0.756428,5.199220,-9.731573,8.329850,1.245963,0.905429,-0.402384,1.624545,2.932708,-3.537956,6.509987,9.971030,7.956711,3.526003,2.953287,-7.128592,-4.391141,7.565492,-0.175354,-7.244680,3.221073,-6.961978,-7.393893,9.194754,-2.631690,3.613144,-6.842836,-8.303771,6.655195,3.258133,0.772005,-9.019351,-0.461982,-1.897076,2.259415,-2.203181,-1.581036,-5.998359,-7.974092,-5.534810,-0.659813,4.484955,2.736234,-3.681309,1.885186,7.039592,2.848181,-1.427701,9.080927,-3.402335,-9.226416,5.066869,5.203873,9.829669,-8.352165,-1.809977,0.762959,5.969917,-5.877729,-9.968307,2.539764,-6.174045,4.538136,-4.013533,-2.419637,0.350461,-8.271140,5.820714,1.895917,0.798006,7.854364,-4.477804,4.418661,3.608363,2.315730,-5.430691,3.318307,3.289172,2.612172,6.588598,-0.072249,-3.083575,-0.383291,-8.777013,4.359085,3.944625,3.228574,4.625967,9.728644,-8.312105,-2.683339,0.034492,-1.513785,4.256953,2.020128,2.701021,2.794088,-6.707352,7.878912,6.923215,-2.585288,8.427654,-1.299350,4.642730,2.339715,-4.422817,-4.249795,0.432512,-4.453559,-9.408393,-0.052209,6.695797,-9.323966,5.392467,-4.007774,-7.578999,1.935798,7.469594,-5.210004,2.811527,-6.659619,-6.515651,0.269083,8.434324,-5.052263,1.503393,8.264355,-5.050843,-3.876930,-1.724892,8.885149,-8.132236,-2.541498,-3.907313,-9.949272,9.565037,-6.869749,2.700037,4.593122,7.895105,-6.832457,-3.510351,-1.231132,9.781134,-5.620143,8.869771,-3.838158,-7.344800,5.056805,-4.825193,-7.833217,2.342197,7.924848,5.396906,0.803462,-4.300818,2.243030,-8.064451,8.206837,6.656090,6.920711,9.030849,-6.717432,-1.070045,8.825723,4.868103,-6.750368,-0.628042,7.264747,1.897691,-6.977650,-7.806525,-0.427914,5.130472,7.722033,-6.874994,-7.323127,-7.220244,5.512813,-0.655483,7.828386,3.775884,-4.661778,9.952211,5.800827,5.740911,-0.086426,9.965089,-0.632563,0.288024,5.485225,-6.983725,3.624308,-9.033676,1.445115,5.598576,-3.988059,4.842374,-8.147326,-7.649200,1.162741,-5.990658,-8.428391,-5.566181,-7.369562,-3.724403,4.714507,5.964679,8.402981,-2.176139,1.826564,-1.010554,-7.498764,-5.615773,-2.758225,-1.338726,-1.376949,-0.081953,-7.756966,0.719858,-9.123769,7.760215,-9.081308,-0.280265,-4.857704,6.609384,9.278169,-7.341896,2.572257,-0.510011,1.577044,5.482892,3.737235,-7.445811,-4.118557,2.034034,3.444821,8.650612,4.040976,-5.998626,-4.136232,4.763724,4.057061,6.497759,5.988203,-4.381342,-1.947017,-3.877245,9.647504,6.671197,2.079381,-9.133102,4.602660,-7.011487,-2.657904,3.192363,-1.882400,-8.961128,-8.565515,-9.866172,8.448646,-5.648902,-5.030782,-8.157812,-3.515425,-7.668537,-5.047515,-6.896886,-7.530687,-4.926575,5.046812,2.046513,2.184884,8.390451,1.083588,2.849175,6.345014,-7.485147,-1.085378,1.714756,-8.628309,-2.700942,5.380708,9.960527,-1.602619,-0.073176,5.270148,6.381338,0.483321,-8.325544,5.854424,5.047217,7.761370,-3.923580,-3.086502,-6.841697,6.702325,7.215094,-7.269610,-5.652883,1.496990,-6.692576,-9.476200,6.993386,7.521805,-8.322895,0.413396,7.304320,3.912037,-3.130585,4.974291,4.880794,-3.945311,6.285959,9.570629,2.514965,-1.451366,9.524163,9.077578,-1.343717,-1.895302,4.627719,1.733734,-4.184142,7.564210,-5.226588,-1.954909,1.375267,8.806694,7.146523,5.982977,2.297735,-5.602542,-3.883542,7.578911,-9.568103,-3.512042,1.505991,-0.059436,-0.376889,-3.879301,1.040977,-6.925990,4.458667,6.196463,-2.442457,2.454260,0.111716,-1.202878,-1.212171,-9.150652,1.448270,-7.963842,-6.691438,2.031509,-9.540382,-9.310346,-2.301583,9.564870,-4.960482,-6.693058,9.899376,-6.480593,2.817624,-0.282995,-5.030436,1.512324,7.923414,-8.391333,-7.929246,6.299856,6.650400,-2.547386,-7.037977,-7.867306,5.722036,-9.133200,-2.472668,0.682466,5.017944,5.637144,-9.088022,-5.318292,2.943183,-2.211120,-5.377609,-2.941491,4.482324,1.353492,-3.334186], dtype = "float64")#candidate|1285|(450,)|const|float64
call_1284 = relay.TupleGetItem(func_9_call(relay.reshape(const_1285.astype('float64'), [5, 15, 6])), 0)
call_1286 = relay.TupleGetItem(func_12_call(relay.reshape(const_1285.astype('float64'), [5, 15, 6])), 0)
output = relay.Tuple([call_1271,call_1284,const_1285,])
output2 = relay.Tuple([call_1272,call_1286,const_1285,])
func_1299 = relay.Function([], output)
mod['func_1299'] = func_1299
mod = relay.transform.InferType()(mod)
output = func_1299()
func_1300 = relay.Function([], output)
mutated_mod['func_1300'] = func_1300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1316 = relay.var("var_1316", dtype = "float32", shape = (3, 6, 4))#candidate|1316|(3, 6, 4)|var|float32
uop_1317 = relay.sin(var_1316.astype('float32')) # shape=(3, 6, 4)
bop_1331 = relay.floor_divide(uop_1317.astype('float32'), relay.reshape(var_1316.astype('float32'), relay.shape_of(uop_1317))) # shape=(3, 6, 4)
bop_1337 = relay.not_equal(uop_1317.astype('bool'), relay.reshape(var_1316.astype('bool'), relay.shape_of(uop_1317))) # shape=(3, 6, 4)
bop_1340 = relay.multiply(bop_1331.astype('int64'), relay.reshape(bop_1337.astype('int64'), relay.shape_of(bop_1331))) # shape=(3, 6, 4)
uop_1361 = relay.log2(bop_1340.astype('float32')) # shape=(3, 6, 4)
uop_1364 = relay.sqrt(uop_1361.astype('float32')) # shape=(3, 6, 4)
uop_1384 = relay.sinh(uop_1364.astype('float64')) # shape=(3, 6, 4)
uop_1387 = relay.atanh(uop_1364.astype('float64')) # shape=(3, 6, 4)
output = relay.Tuple([uop_1384,uop_1387,])
output2 = relay.Tuple([uop_1384,uop_1387,])
func_1395 = relay.Function([var_1316,], output)
mod['func_1395'] = func_1395
mod = relay.transform.InferType()(mod)
var_1396 = relay.var("var_1396", dtype = "float32", shape = (3, 6, 4))#candidate|1396|(3, 6, 4)|var|float32
output = func_1395(var_1396)
func_1397 = relay.Function([var_1396], output)
mutated_mod['func_1397'] = func_1397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_987_call = mod.get_global_var('func_987')
func_988_call = mutated_mod.get_global_var('func_988')
call_1414 = relay.TupleGetItem(func_987_call(), 0)
call_1415 = relay.TupleGetItem(func_988_call(), 0)
uop_1418 = relay.exp(call_1414.astype('float32')) # shape=(11, 9, 6)
uop_1420 = relay.exp(call_1415.astype('float32')) # shape=(11, 9, 6)
func_784_call = mod.get_global_var('func_784')
func_788_call = mutated_mod.get_global_var('func_788')
var_1429 = relay.var("var_1429", dtype = "uint8", shape = ())#candidate|1429|()|var|uint8
var_1430 = relay.var("var_1430", dtype = "uint8", shape = (196,))#candidate|1430|(196,)|var|uint8
call_1428 = func_784_call(relay.reshape(var_1429.astype('uint8'), []), relay.reshape(var_1430.astype('uint8'), [7, 2, 14]), )
call_1431 = func_784_call(relay.reshape(var_1429.astype('uint8'), []), relay.reshape(var_1430.astype('uint8'), [7, 2, 14]), )
func_9_call = mod.get_global_var('func_9')
func_12_call = mutated_mod.get_global_var('func_12')
const_1440 = relay.const([[3.589344,3.336189,-7.546448,-2.006145,-1.799890,-5.620126,-3.903714,4.766955,9.571364,3.647882,-6.547279,3.128194,2.850359,1.629480,6.137762,3.143010,4.875685,9.913683,-0.862993,9.498721,4.881628,-5.782833,2.906299,-3.541523,2.157259,-3.500188,8.774802,4.481918,-4.469156,-8.499350,-9.765422,0.441424,-7.231015,6.785299,-2.064479,1.937992,-4.665663,8.224398,7.579589,-6.692870,9.713757,-0.152142,-2.031477,0.059636,-8.184632,7.208126,-3.712295,-4.337077,3.197451,7.649567,9.895696,2.005208,-9.205927,0.204759,7.051408,2.952013,-6.796842,6.638414,2.222104,-2.614743,-3.067227,-3.402869,-3.528159,7.190033,-2.614797,4.460686,9.079271,3.226904,8.748641,-4.289371,-9.599297,-3.786165,1.759271,-5.958872,-5.017001,7.064014,-5.356187,6.849410,-0.691766,-9.448225,-3.262352,-6.681465,-3.134630,4.731897,0.652338,-6.294090,9.825824,-3.950781,-1.450317,-4.915509,1.869446,8.732323,0.404590,-1.443361,4.149693,0.525600,-0.346386,-4.078769,8.152456,3.929308,0.086479,5.453589,-9.139227,6.996461,-7.321223,9.827388,9.957311,4.980632,-0.405170,2.352427,-5.607110,5.814498,-8.880183,1.370122,2.110603,-0.614938,7.697746,-9.894330,-5.715257,-7.987626,2.579943,-1.721321,1.606281,1.907053,-5.751338,9.323304,9.121801,5.893214,-6.709062,-3.747218,6.936188,-2.651577,-3.093530,-5.712458,7.752738,0.789623,8.933616,8.105039,2.164262,-3.571661,9.511372,-9.920563,-8.813419,7.624492,-2.352844,-3.358318,-8.808836,-9.107729,0.397643,4.309250,-2.541904,6.008980,4.870195,-6.833763,-8.287453,-1.675228,-0.536305,-9.968244,-1.791627,-5.111015,6.885061,2.395829,3.314312,-3.328129,-6.015972,5.615137,-7.333192,-2.227240,-2.043879,-2.322233,3.478389,-6.332114,9.806426,-0.967738,-9.858286,6.363286,-0.067463,-3.170439,-7.577642,-1.639190,-4.280942,5.740320,5.768404,-6.936964,-8.953707,-7.993232,2.187608,-8.508005,9.183574,0.490695,3.869201,-2.734250,4.765309,1.958027,5.735648,-0.220829,-1.177102,0.267402,-1.110052,4.111669,-6.955499,-1.568575,-6.780427,7.159754,-8.998835,-2.671229,4.717832,2.191719,5.000455,-7.458266,-1.253664,-6.366060,7.641152,-9.990606,-8.048755,-4.798132,2.510477,-7.464272,5.754847,-5.864662,-2.417678,2.320595,5.722343,-8.338205,-3.476423,8.312861,-5.497178,4.873377,3.770579,8.220828,1.836915,7.095258,-5.308762,-1.175519,4.362287,7.064037,6.045371,8.600165,5.544033,0.725483,-3.665710,1.620233,0.646212,-2.276056,-2.838829,-9.621938,-6.825919,9.438250,8.740153,-3.171104,-9.890325,6.029144,5.456345,-3.917481,-9.159071,-0.227573,-2.077883,2.964251,-2.666365,9.566511,7.446815,-1.568721,9.360177,1.620269,6.074528,3.687028,1.827668,-5.627354,5.728728,-7.697388,-8.646924,-2.169978,-0.283690,-1.777003,-6.683915,5.344168,6.636354,7.870870,1.021421,-3.290888,-9.612341,-4.308125,-7.174626,-5.306634,0.946951,3.870404,4.733215,4.371994,-6.684450,-2.447481,4.477464,-1.850525,2.893820,7.872725,-6.250208,-8.395034,1.369444,4.994463,9.012031,7.998174,-9.988281,-4.065730,-8.076324,5.475751,-9.342751,3.796564,5.350885,-5.992348,2.997407,-0.323955,9.278593,6.208304,2.048218,-7.314748,-9.975962,-5.939284,3.771522,1.498104,-8.709396,-5.712360,-4.446012,-6.436856,5.822451,2.988277,-0.398400,5.059433,-6.396823,-3.411201,0.433494,-4.848765,-3.850260,-1.669716,1.649492,8.021587,-5.498743,-3.421566,-1.605474,-6.110911,-2.756108,-7.682996,5.735797,-3.877285,-1.918686,-9.730479,-1.210450,-7.562344,7.456373,-4.209759,-4.441759,-3.667109,6.614209,2.154776,4.343516,1.777301,0.938841,-8.120602,7.774363,-0.904335,2.757067,6.767061,5.592477,-5.813905,-4.098107,-9.736909,-9.212700,1.289543,2.776398,9.230838,3.959846,-8.433844,8.014035,8.845999,-7.269022,-7.175846,-0.529389,0.436438,7.152233,-7.352329,-1.916369,-4.406149,0.555294,-8.149654,0.975934,8.805986,-6.196017,6.137473,-1.950588,0.063995,8.713023,-9.696684,6.527507,0.182690,6.500253,0.368297,-1.655211,9.492210,8.843625,7.446706,7.140200,2.264439,-2.803635,7.613112,-0.968874,9.368564,6.991909,0.926098,0.381733,5.172658,8.851934,-4.751105,3.197857,0.426675,2.145278,4.161420,-0.591463,5.729214,7.952410,7.012782,4.959125,0.376659,1.807081,3.313679,-1.492201,1.423805,3.349655,5.210924,7.564386,-5.102806,8.167260,-3.533761,-2.841551,4.151452,-5.866751,6.645292,9.252490,-2.015680,-8.292940,-3.855242,0.083122,-3.158961,4.157368,1.914898,-1.258804,-0.429124,9.771318,5.620927,-9.449820,7.560113,-5.481169,-9.443371]], dtype = "float64")#candidate|1440|(1, 450)|const|float64
call_1439 = relay.TupleGetItem(func_9_call(relay.reshape(const_1440.astype('float64'), [5, 15, 6])), 0)
call_1441 = relay.TupleGetItem(func_12_call(relay.reshape(const_1440.astype('float64'), [5, 15, 6])), 0)
output = relay.Tuple([uop_1418,call_1428,var_1429,var_1430,call_1439,const_1440,])
output2 = relay.Tuple([uop_1420,call_1431,var_1429,var_1430,call_1441,const_1440,])
func_1452 = relay.Function([var_1429,var_1430,], output)
mod['func_1452'] = func_1452
mod = relay.transform.InferType()(mod)
var_1453 = relay.var("var_1453", dtype = "uint8", shape = ())#candidate|1453|()|var|uint8
var_1454 = relay.var("var_1454", dtype = "uint8", shape = (196,))#candidate|1454|(196,)|var|uint8
output = func_1452(var_1453,var_1454,)
func_1455 = relay.Function([var_1453,var_1454,], output)
mutated_mod['func_1455'] = func_1455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_872_call = mod.get_global_var('func_872')
func_873_call = mutated_mod.get_global_var('func_873')
call_1489 = relay.TupleGetItem(func_872_call(), 0)
call_1490 = relay.TupleGetItem(func_873_call(), 0)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_1560 = func_753_call()
call_1561 = func_753_call()
func_736_call = mod.get_global_var('func_736')
func_737_call = mutated_mod.get_global_var('func_737')
call_1562 = func_736_call()
call_1563 = func_736_call()
func_1452_call = mod.get_global_var('func_1452')
func_1455_call = mutated_mod.get_global_var('func_1455')
var_1590 = relay.var("var_1590", dtype = "uint8", shape = ())#candidate|1590|()|var|uint8
var_1591 = relay.var("var_1591", dtype = "uint8", shape = (196,))#candidate|1591|(196,)|var|uint8
call_1589 = relay.TupleGetItem(func_1452_call(relay.reshape(var_1590.astype('uint8'), []), relay.reshape(var_1591.astype('uint8'), [196,]), ), 5)
call_1592 = relay.TupleGetItem(func_1455_call(relay.reshape(var_1590.astype('uint8'), []), relay.reshape(var_1591.astype('uint8'), [196,]), ), 5)
output = relay.Tuple([call_1489,call_1560,call_1562,call_1589,var_1590,var_1591,])
output2 = relay.Tuple([call_1490,call_1561,call_1563,call_1592,var_1590,var_1591,])
func_1596 = relay.Function([var_1590,var_1591,], output)
mod['func_1596'] = func_1596
mod = relay.transform.InferType()(mod)
mutated_mod['func_1596'] = func_1596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1596_call = mutated_mod.get_global_var('func_1596')
var_1598 = relay.var("var_1598", dtype = "uint8", shape = ())#candidate|1598|()|var|uint8
var_1599 = relay.var("var_1599", dtype = "uint8", shape = (196,))#candidate|1599|(196,)|var|uint8
call_1597 = func_1596_call(var_1598,var_1599,)
output = call_1597
func_1600 = relay.Function([var_1598,var_1599,], output)
mutated_mod['func_1600'] = func_1600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_987_call = mod.get_global_var('func_987')
func_988_call = mutated_mod.get_global_var('func_988')
call_1602 = relay.TupleGetItem(func_987_call(), 1)
call_1603 = relay.TupleGetItem(func_988_call(), 1)
func_907_call = mod.get_global_var('func_907')
func_908_call = mutated_mod.get_global_var('func_908')
call_1612 = relay.TupleGetItem(func_907_call(), 0)
call_1613 = relay.TupleGetItem(func_908_call(), 0)
func_802_call = mod.get_global_var('func_802')
func_807_call = mutated_mod.get_global_var('func_807')
var_1616 = relay.var("var_1616", dtype = "float64", shape = (180,))#candidate|1616|(180,)|var|float64
call_1615 = relay.TupleGetItem(func_802_call(relay.reshape(var_1616.astype('float64'), [10, 2, 9]), relay.reshape(var_1616.astype('float64'), [10, 2, 9]), relay.reshape(var_1616.astype('float64'), [10, 2, 9]), ), 0)
call_1617 = relay.TupleGetItem(func_807_call(relay.reshape(var_1616.astype('float64'), [10, 2, 9]), relay.reshape(var_1616.astype('float64'), [10, 2, 9]), relay.reshape(var_1616.astype('float64'), [10, 2, 9]), ), 0)
output = relay.Tuple([call_1602,call_1612,call_1615,var_1616,])
output2 = relay.Tuple([call_1603,call_1613,call_1617,var_1616,])
func_1621 = relay.Function([var_1616,], output)
mod['func_1621'] = func_1621
mod = relay.transform.InferType()(mod)
var_1622 = relay.var("var_1622", dtype = "float64", shape = (180,))#candidate|1622|(180,)|var|float64
output = func_1621(var_1622)
func_1623 = relay.Function([var_1622], output)
mutated_mod['func_1623'] = func_1623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_1667 = func_753_call()
call_1668 = func_753_call()
output = relay.Tuple([call_1667,])
output2 = relay.Tuple([call_1668,])
func_1697 = relay.Function([], output)
mod['func_1697'] = func_1697
mod = relay.transform.InferType()(mod)
mutated_mod['func_1697'] = func_1697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1697_call = mutated_mod.get_global_var('func_1697')
call_1698 = func_1697_call()
output = call_1698
func_1699 = relay.Function([], output)
mutated_mod['func_1699'] = func_1699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_872_call = mod.get_global_var('func_872')
func_873_call = mutated_mod.get_global_var('func_873')
call_1728 = relay.TupleGetItem(func_872_call(), 0)
call_1729 = relay.TupleGetItem(func_873_call(), 0)
output = call_1728
output2 = call_1729
func_1749 = relay.Function([], output)
mod['func_1749'] = func_1749
mod = relay.transform.InferType()(mod)
output = func_1749()
func_1750 = relay.Function([], output)
mutated_mod['func_1750'] = func_1750
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1817 = relay.var("var_1817", dtype = "uint32", shape = (16, 7, 1))#candidate|1817|(16, 7, 1)|var|uint32
var_1818 = relay.var("var_1818", dtype = "uint32", shape = (16, 7, 3))#candidate|1818|(16, 7, 3)|var|uint32
bop_1819 = relay.right_shift(var_1817.astype('uint32'), var_1818.astype('uint32')) # shape=(16, 7, 3)
output = relay.Tuple([bop_1819,])
output2 = relay.Tuple([bop_1819,])
func_1829 = relay.Function([var_1817,var_1818,], output)
mod['func_1829'] = func_1829
mod = relay.transform.InferType()(mod)
mutated_mod['func_1829'] = func_1829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1829_call = mutated_mod.get_global_var('func_1829')
var_1831 = relay.var("var_1831", dtype = "uint32", shape = (16, 7, 1))#candidate|1831|(16, 7, 1)|var|uint32
var_1832 = relay.var("var_1832", dtype = "uint32", shape = (16, 7, 3))#candidate|1832|(16, 7, 3)|var|uint32
call_1830 = func_1829_call(var_1831,var_1832,)
output = call_1830
func_1833 = relay.Function([var_1831,var_1832,], output)
mutated_mod['func_1833'] = func_1833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_1841 = relay.TupleGetItem(func_665_call(), 0)
call_1842 = relay.TupleGetItem(func_666_call(), 0)
func_1173_call = mod.get_global_var('func_1173')
func_1175_call = mutated_mod.get_global_var('func_1175')
call_1845 = func_1173_call()
call_1846 = func_1173_call()
func_1395_call = mod.get_global_var('func_1395')
func_1397_call = mutated_mod.get_global_var('func_1397')
var_1858 = relay.var("var_1858", dtype = "float32", shape = (72,))#candidate|1858|(72,)|var|float32
call_1857 = relay.TupleGetItem(func_1395_call(relay.reshape(var_1858.astype('float32'), [3, 6, 4])), 1)
call_1859 = relay.TupleGetItem(func_1397_call(relay.reshape(var_1858.astype('float32'), [3, 6, 4])), 1)
output = relay.Tuple([call_1841,call_1845,call_1857,var_1858,])
output2 = relay.Tuple([call_1842,call_1846,call_1859,var_1858,])
func_1866 = relay.Function([var_1858,], output)
mod['func_1866'] = func_1866
mod = relay.transform.InferType()(mod)
var_1867 = relay.var("var_1867", dtype = "float32", shape = (72,))#candidate|1867|(72,)|var|float32
output = func_1866(var_1867)
func_1868 = relay.Function([var_1867], output)
mutated_mod['func_1868'] = func_1868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_1913 = relay.TupleGetItem(func_665_call(), 0)
call_1914 = relay.TupleGetItem(func_666_call(), 0)
output = relay.Tuple([call_1913,])
output2 = relay.Tuple([call_1914,])
func_1922 = relay.Function([], output)
mod['func_1922'] = func_1922
mod = relay.transform.InferType()(mod)
output = func_1922()
func_1923 = relay.Function([], output)
mutated_mod['func_1923'] = func_1923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_1924 = relay.TupleGetItem(func_665_call(), 0)
call_1925 = relay.TupleGetItem(func_666_call(), 0)
func_1829_call = mod.get_global_var('func_1829')
func_1833_call = mutated_mod.get_global_var('func_1833')
var_1927 = relay.var("var_1927", dtype = "uint32", shape = (112,))#candidate|1927|(112,)|var|uint32
var_1928 = relay.var("var_1928", dtype = "uint32", shape = (336,))#candidate|1928|(336,)|var|uint32
call_1926 = relay.TupleGetItem(func_1829_call(relay.reshape(var_1927.astype('uint32'), [16, 7, 1]), relay.reshape(var_1928.astype('uint32'), [16, 7, 3]), ), 0)
call_1929 = relay.TupleGetItem(func_1833_call(relay.reshape(var_1927.astype('uint32'), [16, 7, 1]), relay.reshape(var_1928.astype('uint32'), [16, 7, 3]), ), 0)
func_1922_call = mod.get_global_var('func_1922')
func_1923_call = mutated_mod.get_global_var('func_1923')
call_1938 = relay.TupleGetItem(func_1922_call(), 0)
call_1939 = relay.TupleGetItem(func_1923_call(), 0)
func_1697_call = mod.get_global_var('func_1697')
func_1699_call = mutated_mod.get_global_var('func_1699')
call_1944 = relay.TupleGetItem(func_1697_call(), 0)
call_1945 = relay.TupleGetItem(func_1699_call(), 0)
func_1127_call = mod.get_global_var('func_1127')
func_1128_call = mutated_mod.get_global_var('func_1128')
call_1950 = relay.TupleGetItem(func_1127_call(), 2)
call_1951 = relay.TupleGetItem(func_1128_call(), 2)
bop_1954 = relay.logical_and(var_1928.astype('bool'), relay.reshape(call_1926.astype('bool'), relay.shape_of(var_1928))) # shape=(336,)
bop_1957 = relay.logical_and(var_1928.astype('bool'), relay.reshape(call_1929.astype('bool'), relay.shape_of(var_1928))) # shape=(336,)
output = relay.Tuple([call_1924,var_1927,call_1938,call_1944,call_1950,bop_1954,])
output2 = relay.Tuple([call_1925,var_1927,call_1939,call_1945,call_1951,bop_1957,])
func_1972 = relay.Function([var_1927,var_1928,], output)
mod['func_1972'] = func_1972
mod = relay.transform.InferType()(mod)
var_1973 = relay.var("var_1973", dtype = "uint32", shape = (112,))#candidate|1973|(112,)|var|uint32
var_1974 = relay.var("var_1974", dtype = "uint32", shape = (336,))#candidate|1974|(336,)|var|uint32
output = func_1972(var_1973,var_1974,)
func_1975 = relay.Function([var_1973,var_1974,], output)
mutated_mod['func_1975'] = func_1975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mod.get_global_var('func_736')
func_737_call = mutated_mod.get_global_var('func_737')
call_2063 = func_736_call()
call_2064 = func_736_call()
func_802_call = mod.get_global_var('func_802')
func_807_call = mutated_mod.get_global_var('func_807')
const_2067 = relay.const([-1.253097,2.009049,8.313111,4.574319,-4.536666,9.023763,7.794687,9.166751,4.055149,4.947264,6.463471,0.916893,-9.630102,-0.927796,-5.560097,9.145086,9.092031,-6.546145,-1.155744,-7.681966,7.190013,4.829106,-8.474797,-2.484951,1.718182,0.973644,-1.561150,2.357519,2.117075,-3.837687,1.759068,5.879008,-5.260183,-9.700079,4.668087,-6.478412,-1.684459,7.804926,-4.633260,3.611072,7.396704,-4.007703,1.063929,7.457779,-8.569528,-1.191480,0.895285,-2.133828,-5.316397,0.868811,8.413602,-9.318644,1.364935,2.420585,2.719986,-2.552016,0.758390,-7.112246,-6.103680,-7.059379,1.412665,3.556916,-2.537965,7.730820,-7.984689,-9.563650,-0.897064,8.972997,-2.976839,3.422279,4.838807,7.183224,8.286441,9.821916,7.174379,-0.455147,7.393349,3.883108,1.989026,-6.190452,2.160971,6.813095,3.684850,-2.198763,2.233763,4.991768,2.083600,-3.362607,8.869310,-5.048261,6.055675,6.824575,-0.346545,-7.263749,7.293890,2.661941,6.117649,-5.442816,-2.552827,-0.374661,8.298208,-6.258207,-0.522180,0.137473,8.818767,-0.641459,-7.618585,3.118925,5.760910,-3.389506,-0.535960,6.552065,-9.765455,-9.988443,-6.093218,7.081373,-1.243353,-5.156243,-1.307805,-2.849051,-2.856803,-1.363912,7.603705,4.092029,0.697853,1.539194,-6.170816,4.615727,0.445949,5.577750,-4.303508,8.058640,-6.599605,-0.175669,5.659225,-9.715862,9.987365,-5.217438,-1.445815,0.763189,7.674725,7.606504,-6.138305,-7.244234,-9.008583,7.181807,-2.648221,-7.074720,5.863295,8.370350,2.432324,-6.719416,-9.533564,2.529022,-2.954475,-4.775211,-4.578305,5.888437,-2.691121,-4.163294,1.971719,-6.169524,-5.758395,6.759308,7.353101,-4.821622,-6.078932,5.488389,8.958705,-2.323043,-1.337950,0.572435,-3.111547,1.902185,-5.261162,-5.397857,0.132516,-6.360791,2.096125,3.124115], dtype = "float64")#candidate|2067|(180,)|const|float64
call_2066 = relay.TupleGetItem(func_802_call(relay.reshape(const_2067.astype('float64'), [10, 2, 9]), relay.reshape(const_2067.astype('float64'), [10, 2, 9]), relay.reshape(const_2067.astype('float64'), [10, 2, 9]), ), 0)
call_2068 = relay.TupleGetItem(func_807_call(relay.reshape(const_2067.astype('float64'), [10, 2, 9]), relay.reshape(const_2067.astype('float64'), [10, 2, 9]), relay.reshape(const_2067.astype('float64'), [10, 2, 9]), ), 0)
bop_2071 = relay.logical_xor(const_2067.astype('uint64'), relay.reshape(call_2066.astype('uint64'), relay.shape_of(const_2067))) # shape=(180,)
bop_2074 = relay.logical_xor(const_2067.astype('uint64'), relay.reshape(call_2068.astype('uint64'), relay.shape_of(const_2067))) # shape=(180,)
output = relay.Tuple([call_2063,bop_2071,])
output2 = relay.Tuple([call_2064,bop_2074,])
func_2080 = relay.Function([], output)
mod['func_2080'] = func_2080
mod = relay.transform.InferType()(mod)
output = func_2080()
func_2081 = relay.Function([], output)
mutated_mod['func_2081'] = func_2081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2082 = relay.var("var_2082", dtype = "float32", shape = (2, 13, 1))#candidate|2082|(2, 13, 1)|var|float32
uop_2083 = relay.acos(var_2082.astype('float32')) # shape=(2, 13, 1)
var_2089 = relay.var("var_2089", dtype = "float32", shape = (2, 13, 5))#candidate|2089|(2, 13, 5)|var|float32
bop_2090 = relay.less_equal(uop_2083.astype('bool'), var_2089.astype('bool')) # shape=(2, 13, 5)
bop_2094 = relay.floor_divide(var_2082.astype('float32'), var_2089.astype('float32')) # shape=(2, 13, 5)
func_1299_call = mod.get_global_var('func_1299')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_2109 = relay.TupleGetItem(func_1299_call(), 0)
call_2110 = relay.TupleGetItem(func_1300_call(), 0)
output = relay.Tuple([bop_2090,bop_2094,call_2109,])
output2 = relay.Tuple([bop_2090,bop_2094,call_2110,])
func_2119 = relay.Function([var_2082,var_2089,], output)
mod['func_2119'] = func_2119
mod = relay.transform.InferType()(mod)
var_2120 = relay.var("var_2120", dtype = "float32", shape = (2, 13, 1))#candidate|2120|(2, 13, 1)|var|float32
var_2121 = relay.var("var_2121", dtype = "float32", shape = (2, 13, 5))#candidate|2121|(2, 13, 5)|var|float32
output = func_2119(var_2120,var_2121,)
func_2122 = relay.Function([var_2120,var_2121,], output)
mutated_mod['func_2122'] = func_2122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mod.get_global_var('func_1127')
func_1128_call = mutated_mod.get_global_var('func_1128')
call_2133 = relay.TupleGetItem(func_1127_call(), 0)
call_2134 = relay.TupleGetItem(func_1128_call(), 0)
output = relay.Tuple([call_2133,])
output2 = relay.Tuple([call_2134,])
func_2165 = relay.Function([], output)
mod['func_2165'] = func_2165
mod = relay.transform.InferType()(mod)
mutated_mod['func_2165'] = func_2165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2165_call = mutated_mod.get_global_var('func_2165')
call_2166 = func_2165_call()
output = call_2166
func_2167 = relay.Function([], output)
mutated_mod['func_2167'] = func_2167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1697_call = mod.get_global_var('func_1697')
func_1699_call = mutated_mod.get_global_var('func_1699')
call_2317 = relay.TupleGetItem(func_1697_call(), 0)
call_2318 = relay.TupleGetItem(func_1699_call(), 0)
output = relay.Tuple([call_2317,])
output2 = relay.Tuple([call_2318,])
func_2319 = relay.Function([], output)
mod['func_2319'] = func_2319
mod = relay.transform.InferType()(mod)
mutated_mod['func_2319'] = func_2319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2319_call = mutated_mod.get_global_var('func_2319')
call_2320 = func_2319_call()
output = call_2320
func_2321 = relay.Function([], output)
mutated_mod['func_2321'] = func_2321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_2324 = relay.TupleGetItem(func_1299_call(), 2)
call_2325 = relay.TupleGetItem(func_1300_call(), 2)
uop_2326 = relay.acos(call_2324.astype('float32')) # shape=(450,)
uop_2328 = relay.acos(call_2325.astype('float32')) # shape=(450,)
output = uop_2326
output2 = uop_2328
func_2337 = relay.Function([], output)
mod['func_2337'] = func_2337
mod = relay.transform.InferType()(mod)
output = func_2337()
func_2338 = relay.Function([], output)
mutated_mod['func_2338'] = func_2338
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2350 = relay.var("var_2350", dtype = "int16", shape = (16, 10, 16))#candidate|2350|(16, 10, 16)|var|int16
var_2351 = relay.var("var_2351", dtype = "int16", shape = (16, 10, 16))#candidate|2351|(16, 10, 16)|var|int16
bop_2352 = relay.bitwise_and(var_2350.astype('int16'), relay.reshape(var_2351.astype('int16'), relay.shape_of(var_2350))) # shape=(16, 10, 16)
output = relay.Tuple([bop_2352,])
output2 = relay.Tuple([bop_2352,])
func_2374 = relay.Function([var_2350,var_2351,], output)
mod['func_2374'] = func_2374
mod = relay.transform.InferType()(mod)
mutated_mod['func_2374'] = func_2374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2374_call = mutated_mod.get_global_var('func_2374')
var_2376 = relay.var("var_2376", dtype = "int16", shape = (16, 10, 16))#candidate|2376|(16, 10, 16)|var|int16
var_2377 = relay.var("var_2377", dtype = "int16", shape = (16, 10, 16))#candidate|2377|(16, 10, 16)|var|int16
call_2375 = func_2374_call(var_2376,var_2377,)
output = call_2375
func_2378 = relay.Function([var_2376,var_2377,], output)
mutated_mod['func_2378'] = func_2378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2319_call = mod.get_global_var('func_2319')
func_2321_call = mutated_mod.get_global_var('func_2321')
call_2408 = relay.TupleGetItem(func_2319_call(), 0)
call_2409 = relay.TupleGetItem(func_2321_call(), 0)
output = relay.Tuple([call_2408,])
output2 = relay.Tuple([call_2409,])
func_2410 = relay.Function([], output)
mod['func_2410'] = func_2410
mod = relay.transform.InferType()(mod)
mutated_mod['func_2410'] = func_2410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mutated_mod.get_global_var('func_2410')
call_2411 = func_2410_call()
output = call_2411
func_2412 = relay.Function([], output)
mutated_mod['func_2412'] = func_2412
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2485 = relay.var("var_2485", dtype = "float64", shape = (13, 7, 14))#candidate|2485|(13, 7, 14)|var|float64
uop_2486 = relay.atanh(var_2485.astype('float64')) # shape=(13, 7, 14)
func_1697_call = mod.get_global_var('func_1697')
func_1699_call = mutated_mod.get_global_var('func_1699')
call_2490 = relay.TupleGetItem(func_1697_call(), 0)
call_2491 = relay.TupleGetItem(func_1699_call(), 0)
output = relay.Tuple([uop_2486,call_2490,])
output2 = relay.Tuple([uop_2486,call_2491,])
func_2494 = relay.Function([var_2485,], output)
mod['func_2494'] = func_2494
mod = relay.transform.InferType()(mod)
var_2495 = relay.var("var_2495", dtype = "float64", shape = (13, 7, 14))#candidate|2495|(13, 7, 14)|var|float64
output = func_2494(var_2495)
func_2496 = relay.Function([var_2495], output)
mutated_mod['func_2496'] = func_2496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mod.get_global_var('func_736')
func_737_call = mutated_mod.get_global_var('func_737')
call_2636 = func_736_call()
call_2637 = func_736_call()
func_1299_call = mod.get_global_var('func_1299')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_2654 = relay.TupleGetItem(func_1299_call(), 0)
call_2655 = relay.TupleGetItem(func_1300_call(), 0)
output = relay.Tuple([call_2636,call_2654,])
output2 = relay.Tuple([call_2637,call_2655,])
func_2658 = relay.Function([], output)
mod['func_2658'] = func_2658
mod = relay.transform.InferType()(mod)
mutated_mod['func_2658'] = func_2658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mutated_mod.get_global_var('func_2658')
call_2659 = func_2658_call()
output = call_2659
func_2660 = relay.Function([], output)
mutated_mod['func_2660'] = func_2660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2165_call = mod.get_global_var('func_2165')
func_2167_call = mutated_mod.get_global_var('func_2167')
call_2675 = relay.TupleGetItem(func_2165_call(), 0)
call_2676 = relay.TupleGetItem(func_2167_call(), 0)
func_2080_call = mod.get_global_var('func_2080')
func_2081_call = mutated_mod.get_global_var('func_2081')
call_2684 = relay.TupleGetItem(func_2080_call(), 0)
call_2685 = relay.TupleGetItem(func_2081_call(), 0)
output = relay.Tuple([call_2675,call_2684,])
output2 = relay.Tuple([call_2676,call_2685,])
func_2722 = relay.Function([], output)
mod['func_2722'] = func_2722
mod = relay.transform.InferType()(mod)
output = func_2722()
func_2723 = relay.Function([], output)
mutated_mod['func_2723'] = func_2723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mod.get_global_var('func_2410')
func_2412_call = mutated_mod.get_global_var('func_2412')
call_2731 = relay.TupleGetItem(func_2410_call(), 0)
call_2732 = relay.TupleGetItem(func_2412_call(), 0)
output = relay.Tuple([call_2731,])
output2 = relay.Tuple([call_2732,])
func_2735 = relay.Function([], output)
mod['func_2735'] = func_2735
mod = relay.transform.InferType()(mod)
output = func_2735()
func_2736 = relay.Function([], output)
mutated_mod['func_2736'] = func_2736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mod.get_global_var('func_736')
func_737_call = mutated_mod.get_global_var('func_737')
call_2742 = func_736_call()
call_2743 = func_736_call()
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_2754 = func_753_call()
call_2755 = func_753_call()
func_872_call = mod.get_global_var('func_872')
func_873_call = mutated_mod.get_global_var('func_873')
call_2764 = relay.TupleGetItem(func_872_call(), 0)
call_2765 = relay.TupleGetItem(func_873_call(), 0)
func_2374_call = mod.get_global_var('func_2374')
func_2378_call = mutated_mod.get_global_var('func_2378')
const_2776 = relay.const([4,7,1,-10,2,7,9,9,-1,-2,-1,6,5,-2,-5,-7,1,5,-2,10,-10,-7,-4,2,3,-6,6,-10,10,-9,-1,3,10,5,-4,7,-4,2,1,5,-7,-10,3,-2,-2,-7,9,6,-10,3,-7,-10,7,9,6,-3,5,6,5,-10,-10,1,-4,1,9,-10,6,-9,9,-10,4,-10,9,6,3,-1,10,6,-1,10,3,-8,7,2,7,-3,-7,7,-8,-10,-6,7,4,-10,10,-5,-9,4,2,3,1,-8,8,6,10,-6,8,-4,7,-7,5,2,7,-9,-5,8,-8,-6,-6,2,-8,-4,-2,-1,2,7,-2,-1,-6,-9,3,-9,-6,7,9,9,8,6,-10,10,-6,9,-6,8,9,5,7,-4,2,6,-1,-9,-6,10,3,-8,-6,7,-5,6,-2,-7,6,1,-3,9,2,4,4,-2,3,-8,-6,1,-9,5,-7,-10,6,-2,8,2,1,6,9,4,9,-10,-4,6,9,5,-8,2,-6,-2,6,-4,9,2,-1,9,-8,-7,-4,-6,-6,1,-7,7,-7,-8,2,-10,4,-8,-10,-5,10,1,-6,-6,-1,6,10,-9,-10,-10,9,-3,3,7,2,2,-5,3,3,4,4,9,-1,1,-7,6,-10,-10,2,-6,3,-4,2,-10,7,-8,3,-7,8,-8,6,3,-4,-8,-2,1,-2,-4,4,-1,9,4,-9,-8,8,1,1,1,-7,-4,-3,4,1,2,-3,8,2,-6,4,7,-2,-7,2,-10,5,10,8,3,-4,-5,-8,3,-7,-1,4,3,8,-1,-6,-3,-3,-10,7,-10,-6,9,10,-6,-10,-9,6,-10,-2,9,10,-10,5,5,1,2,-10,3,-5,-8,7,9,9,-10,-10,8,10,-6,6,-6,7,-8,1,1,-10,2,8,3,-3,-8,-3,-7,-4,8,4,-1,-4,-10,-10,-2,9,10,-7,5,-7,3,1,2,2,-7,6,9,-7,-4,1,-1,-1,-10,-5,8,-9,-9,10,-8,-3,-3,5,6,3,2,9,-6,4,9,-10,9,-8,2,2,-4,-4,-2,1,2,-2,-9,6,1,1,9,-7,-1,-7,-4,-2,3,-5,5,-3,-9,-1,-5,-4,-9,8,-6,-6,-1,1,-3,-4,-9,1,3,10,8,10,10,-10,9,-9,-3,2,-10,-9,-6,-9,-2,-8,4,-8,-1,6,4,-2,-5,8,8,2,-2,2,4,10,4,2,6,-2,8,-10,-5,-5,-5,-10,2,-2,-5,-2,-8,6,10,9,5,5,-9,-8,-9,-7,-8,9,9,4,-6,4,9,-5,5,7,5,-7,-6,1,2,2,-6,-9,4,10,2,-3,1,1,2,-10,-7,1,6,3,-3,5,7,4,-1,-3,-8,3,-4,9,-2,3,8,5,10,-9,4,-2,-1,-2,1,-3,-4,10,3,-6,-8,4,-4,1,8,9,-5,-3,-7,9,2,9,-10,-4,10,-8,8,6,3,-10,-7,-3,7,-1,10,-4,-1,8,4,4,1,-2,-4,-3,-8,-7,9,9,3,2,-9,-6,9,-2,6,-5,-8,8,-7,-8,-3,10,-5,9,1,3,-8,-2,5,-8,-2,9,-1,-3,-7,5,-9,3,-6,-4,-4,8,-8,-8,4,3,2,9,7,4,-4,4,-4,7,-9,-6,8,8,-4,-8,-4,-6,2,-10,7,5,-2,7,5,-5,-5,-1,5,-8,6,7,6,4,9,7,7,9,10,-5,-10,-1,-1,9,-2,3,2,5,5,5,3,-2,-3,-10,-7,-10,-5,-3,3,-2,-8,2,7,9,7,8,8,-2,2,-6,9,7,6,4,-3,-6,-1,2,-8,-2,7,-6,-1,-5,-4,-2,-6,-1,-1,4,9,-5,-10,10,10,-4,-3,9,1,-7,-7,-10,-9,7,-3,-6,-3,-5,-9,-3,-9,5,9,6,-10,-7,-1,7,-5,4,5,10,-2,-3,2,-2,-2,2,1,-3,10,-5,4,-5,-8,9,-10,3,6,4,1,8,5,7,8,8,-10,3,6,-7,8,10,-4,9,-9,5,-3,7,3,-5,-6,2,-5,-3,4,7,-3,9,2,-7,-5,4,7,5,5,-4,-2,-8,1,1,-1,-9,-7,-4,-8,-1,7,-10,-7,6,-6,5,-5,8,6,3,-8,-4,1,-6,-10,2,4,-2,9,-3,8,-7,-2,-1,2,8,8,-7,-1,-8,3,8,3,8,-10,1,10,-3,10,-3,-9,6,-4,-8,7,-5,7,-8,7,-6,-7,-7,2,-9,3,7,-2,3,8,-10,7,-7,-1,9,-1,5,2,6,9,8,-7,7,-10,5,10,-4,1,5,6,-9,1,-8,-3,6,-10,-7,-1,-8,5,-8,-1,3,-4,3,4,-1,-6,-7,1,-3,8,-2,6,-10,5,5,-10,7,1,-6,-2,2,-3,-6,-2,9,-1,-1,-1,8,-10,-10,-5,4,7,-3,-6,6,3,8,-1,7,8,-2,10,-4,5,1,-1,6,-7,-8,3,6,3,1,-1,-9,8,-7,-1,9,5,8,6,-7,-2,-8,6,-10,8,-7,8,9,7,-6,-8,-6,6,-10,-7,-5,-1,-5,9,-8,-5,-7,10,10,-3,-8,3,4,8,-10,-1,6,-2,-1,-6,-9,3,-7,3,2,6,-6,6,6,6,-10,5,-10,-9,-7,9,10,-3,7,-4,1,-9,-9,-1,-10,5,5,-8,-8,-8,-5,-2,-1,2,8,-6,-8,-9,1,-5,6,-1,-1,-10,9,3,-8,-9,-7,-6,-6,5,-7,-2,4,-9,9,-5,-2,-7,-6,-5,3,-3,4,7,-2,-6,9,-9,-7,-5,-2,-7,7,7,4,8,-5,-8,-10,1,-7,3,6,9,2,-2,-6,1,10,-9,-10,-2,7,4,-4,9,1,-7,2,2,2,10,-10,-3,7,-5,-10,1,-6,3,1,3,-4,3,-6,1,7,-6,-10,-9,3,-5,-2,10,-5,-10,-7,-10,-3,6,-8,-5,-8,-3,-2,-7,-8,-7,3,10,2,-4,-5,1,-9,-7,-4,1,-5,-2,7,-1,-4,-5,10,4,-7,3,3,10,-1,-9,9,-8,-4,-9,-2,8,-1,-2,2,4,-4,-1,-1,9,6,-8,7,7,-6,4,1,3,-9,-4,1,-10,3,4,-10,5,-10,-3,8,-10,-8,-2,10,-10,10,-10,2,-8,1,8,-4,9,7,-2,-2,9,9,-9,-5,-8,5,-8,7,-9,-9,-10,-3,8,1,-2,4,-2,-3,4,2,-2,1,1,9,8,10,-2,7,10,2,10,5,1,-5,-5,6,-1,1,-6,-3,-8,-2,-5,-2,8,10,10,-2,-3,-5,-3,8,-1,-7,9,1,6,-8,4,-7,-2,2,4,4,-2,-8,1,10,-4,8,10,9,-3,-6,-6,9,2,3,-5,3,-5,4,-4,-9,3,2,-7,1,7,-6,2,5,7,10,-3,3,2,6,-2,-6,2,-2,8,-10,-3,-10,-4,-1,-10,-6,3,-3,-5,-5,-3,5,9,-6,-3,2,3,-2,-6,9,-3,-1,2,-3,10,-7,-7,8,-2,-2,1,10,5,-2,-3,7,5,4,1,-6,5,3,8,9,8,-4,5,-2,5,1,4,-6,7,6,-9,-8,8,6,7,-5,-5,3,-2,-10,10,7,-1,-2,-6,6,-1,-8,10,-4,-9,9,5,-4,8,5,5,-1,-8,-7,-3,10,9,-4,1,-3,4,-4,7,-9,-2,-2,-8,-3,8,-3,-3,5,-10,-1,5,-9,10,-10,-1,-2,5,10,-7,-2,-5,5,7,-1,9,7,-10,4,10,-6,5,4,2,-3,-10,-5,9,4,10,-2,9,-10,8,10,-10,-10,4,2,1,6,-10,4,-1,-7,4,-7,-1,-6,2,6,4,-4,-4,-6,-2,4,-3,1,-9,-2,-8,-9,-7,7,-1,-9,2,3,10,1,-4,-3,-5,9,-3,-8,2,-9,4,-6,2,10,-9,-10,-6,10,-5,-5,5,6,-8,8,-4,9,-6,3,-10,-10,9,7,-10,-3,10,-5,3,3,-8,9,2,1,3,-4,8,4,-3,-1,10,7,-2,-4,-6,6,10,7,3,7,-4,1,-6,-7,7,-3,-4,4,-3,-10,-5,-4,-2,-6,10,3,6,-6,-10,-3,-3,-2,7,2,4,8,8,6,-4,7,8,10,3,-8,8,-9,-10,-9,-9,-4,5,-4,-5,-3,5,-4,9,8,-9,6,-10,10,8,-6,2,-9,3,10,-6,-8,4,-3,-6,-8,9,-4,-10,8,6,2,3,5,-7,-3,-7,-1,3,-5,-6,5,6,4,-6,2,8,1,7,9,-10,-4,-3,9,2,-4,6,2,9,-8,10,-6,-7,-2,-3,-6,-3,-2,-9,2,-5,-10,6,-3,-9,9,-2,-10,3,1,2,3,-2,-4,5,2,2,9,3,-4,-2,4,9,-2,7,-2,-3,-8,7,-7,6,10,-3,-6,2,9,-3,7,8,-6,-5,7,1,-4,-5,-3,-2,9,-4,2,-6,-2,-5,-3,-8,-1,9,-2,3,-1,7,-9,8,6,6,-8,8,-3,8,-9,7,1,8,-6,-9,9,-2,-7,-8,-2,1,-7,1,6,-8,-8,-5,-2,-4,5,-7,9,3,-8,1,5,10,-10,2,10,1,8,9,-10,-8,4,9,3,-1,3,2,3,10,3,-9,3,-3,5,-10,-2,-10,-4,-4,-3,9,-9,3,-3,5,-4,-8,-6,9,10,-8,8,3,-9,10,-3,7,9,4,-1,-7,7,6,-6,-5,-4,1,3,5,-2,-1,3,-9,-5,4,5,-5,-7,-6,-3,1,5,3,-7,-7,3,-6,-7,-1,-9,10,-10,-6,3,-2,-4,8,-3,5,-9,-1,-2,3,3,2,2,-3,9,9,-1,2,2,-5,1,6,-2,-6,-5,6,2,-7,-1,5,2,-4,5,-10,-4,-3,-7,-6,-8,-5,-1,1,8,8,-2,1,-8,-1,-9,-9,8,-1,-1,-3,-9,-1,7,6,2,7,8,10,-1,1,1,-6,-4,-1,-3,-5,3,5,-10,7,2,5,-10,-7,3,-4,10,3,-6,-8,-9,1,8,1,-6,7,-2,9,-7,-6,6,7,9,-7,-4,-4,-7,4,3,-1,-4,7,5,10,4,-4,-6,-4,3,-8,8,10,8,-1,1,-8,-4,-3,-2,-1,-8,7,-10,-7,-6,-9,-8,10,-5,7,-4,-3,1,-7,8,3,5,-10,-3,-7,5,-3,-5,10,-5,7,1,8,-5,-9,5,1,-2,-6,-1,5,-10,-10,1,-6,5,6,5,-2,-2,-3,2,8,6,-10,10,-2,4,-5,10,-1,-7,4,2,-4,6,-3,3,4,-7,6,-10,8,-10,8,6,-8,-10,-7,-8,-9,8,5,-3,-3,-1,-8,7,4,-10,-7,6,1,8,8,-9,-2,-9,10,-6,-2,2,-10,7,6,10,6,-1,-2,5,8,-9,4,-9,-9,9,-4,3,-10,1,10,3,9,-2,-4,-3,2,-5,9,1,1,-1,-1,-2,-7,-10,4,2,7,4,-3,-6,-10,-1,6,-9,4,-1,-6,-9,-6,1,-10,5,9,3,-10,-6,1,-9,1,-4,-2,1,10,1,7,-7,-5,8,-6,5,-9,6,10,7,-5,-8,5,-5,7,10,7,5,-4,5,4,-5,3,-3,9,6,-10,-1,4,-2,3,7,1,-2,-4,6,7,1,5,4,-5,-7,5,-1,-5,1,5,8,1,3,-4,-5,2,-2,-1,10,9,10,9,-4,-4,-4,7,5,1,5,-6,-8,-6,5,9,1,7,3,-5,-2,-1,6,-8,6,-8,5,-1,2,5,5,5,3,1,9,10,3,-10,1,-1,-7,10,-2,-9,10,-2,-8,-3,2,-7,-10,-4,10,3,2,-10,2,5,3,-8,5,-10,-10,6,-6,3,-9,10,-1,-1,-8,3,3,6,9,-10,8,1,-4,-10,-9,-8,-9,8,-1,2,1,9,-1,-1,1,-7,3,4,5,8,6,4,4,5,2,5,3,9,-1,6,-2,-8,1,10,8,3,6,1,-1,5,6,-9,4,-2,-8,6,1,3,-5,-9,-3,-9,10,-6,6,4,-3,-10,-1,-1,-1,7,10,4,-4,-10,-5,-3,7,-4,3,7,-1,3,1,10,-3,-6,8,-10,-2,7,-9,10,2,-3,4,-2,-8,6,3,3,-5,-10,-8,-5,-3,8,5,-10,-4,5,-4,2,4,-3,-7,2,7,5,2,-6,4,-7,-1,-7,1,-4,1,-6,5,-3,-8,-4,-8,-10,3,-7,9,-6,-2,-9,9,9,9,-6,-7,-9,-5,-1,4,-5,-9,-3,-8,-3,4,-5,-3,-4,10,-9,8,-3,8,5,-9,-10,1,-9,2,9,-3,-10,9,-1,3,-7,5,-1,-7,-7,-7,5,10,-6,7,10,-2,-8,-4,3,6,-8,1,4,-8,-6,-9,2,6,-2,7,-5,-2,-1,2,6,5,9,-5,-6,7,9,-3,-5,-1,6,-7,-7,5,-5,-4,-5,5,5,-10,-5,4,-2,5,8,2,-1,4,-10,-8,8,-8,-8,-8,4,-5,4,3,6,1,3,7,-4,4,4,9,-1,-4,1,-4,-9,-4,-8,-8,6,-10,5,-2,2,5,7,5,-2,-9,-10,-5,-3,3,7,-10,1,9,9,6,-9,-7,-4,6,-3,6,9,-4,2,6,7,2,5,-3,-7,6,-10,4,-7,-10,7,-4,9,1,-3,3,-4,-7,8,-5,-1,-3,-6,-4,1,-3,-2,-7,3,4,-6,6,-4,10,5], dtype = "int16")#candidate|2776|(2560,)|const|int16
call_2775 = relay.TupleGetItem(func_2374_call(relay.reshape(const_2776.astype('int16'), [16, 10, 16]), relay.reshape(const_2776.astype('int16'), [16, 10, 16]), ), 0)
call_2777 = relay.TupleGetItem(func_2378_call(relay.reshape(const_2776.astype('int16'), [16, 10, 16]), relay.reshape(const_2776.astype('int16'), [16, 10, 16]), ), 0)
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
const_2780 = relay.const([-2.455183,2.053125,-8.907954,7.207733,1.303447,-1.249444,-5.410205,5.923851,-7.003586,-9.862537,7.125967,4.897969,0.424433,-1.987886,6.957454,-8.942050,-4.626849,-2.710492,2.421145,-5.739973,-7.030573,3.759691,-6.681006,-2.097468,3.956542,4.182598,-3.928357,-7.988964,6.349125,-7.108024,-0.786119,-4.567636,3.920825,8.089886,-2.781183,0.742335,-6.710888,-9.957481,9.311284,7.655802,8.332727,1.459070,5.391808,9.586288,6.393100,8.324666,1.078235,-6.669078,7.769848,7.458064,6.339731,-1.324355,5.520207,-2.874488], dtype = "float64")#candidate|2780|(54,)|const|float64
const_2781 = relay.const([-2.501691,2.982419,-8.943229,-3.487730,-0.730922,-8.886092,-8.473760,-1.433060,-3.469416,3.647974,-7.361940,-4.077995,-3.111057,-6.992713,-3.176155,-2.012416,0.384794,4.379912,3.262188,6.665257,2.996168,1.248353,-5.660104,1.334750,4.147706,-9.265434,1.541779,4.011713,6.037885,7.782332,8.821672,-1.705653,7.624359,-9.739742,8.732676,6.239389,6.811264,-2.486554,-3.346782,0.832826,7.449904,-2.560340,-3.540362,-1.329393,1.299266,5.356565,-4.358034,3.196668,8.816731,-8.391429,0.241066,-4.806712,-3.638096,-5.279567,-9.516351,-1.117158,3.023087,-4.455654,-9.147773,7.863176,3.539426,-3.123927,-3.361673,8.224448,6.422608,0.412147,3.210434,-3.415227,-9.000299,3.154257,-0.151978,-4.117771,-3.552951,1.575864,-4.412577,-8.934916,3.231661,6.927244,8.071230,-2.187401,-7.569667,2.138261,8.954059,1.021236,0.705624,-8.896759,-2.657909,0.670212,-5.056766,8.844786,-8.074920,-2.896808,-5.934221,1.412759,-7.086830,-3.450753,9.059066,2.653269,1.572471,7.330480,1.439235,-1.105213,-0.278308,-7.314688,-8.753279,1.347532,5.240043,0.014555,7.268843,2.622152,-3.333897,-4.536776,-2.195811,-6.162027,-5.363145,-4.859896,7.066918,0.991069,-7.272950,-0.537492,4.256814,8.568930,1.316464,-9.401187,-2.803901,6.540070,-2.148793,-5.480860,3.717563,-6.847141,-5.107815,1.915115,-9.833655,-2.116386,-9.445620,1.903838,-7.942068,-5.609741,4.757031,2.667447,6.407871,-9.962785,-4.205312,-0.554082,8.099655,-9.429311,8.851626,-4.775680,-9.467821,-4.247239,1.310246,2.504752,6.041442,-5.496383,-7.272014,-6.041495,-9.459348,3.164531,2.128407,-6.624798,3.277626,0.258308,-2.391649,-1.137679,-0.008079,6.465329,-1.572374,6.806978,-6.592950,3.528981,7.513070,-7.233342,-9.972242,5.048315,1.655732,1.609548,-6.493095,1.880274,-6.842568,4.776896,8.311183,-3.401241,2.279312,1.854924,3.109524,8.350599,-3.953551,-4.528838,5.486631,-8.702584,5.885514,3.790652,-8.799865,-6.830293,-1.597468,7.178831,-3.396673,-3.571887,-3.457631,-5.522073,-6.575245,-7.973947,5.285128,7.142513,-6.168754,-6.245547,5.314157,0.120489,-0.581282,-9.463149,-1.901399,-0.228586,-2.990039,-9.876718,-4.809245,-4.583817,-8.696066,0.351960,-3.447276,6.435261,0.519812,-5.502111,1.295726,-6.108150,-0.347510,0.962666,8.865956,8.504352,-4.951075,-6.308250,-0.764904,3.023131,9.865408,4.547885,8.372091,5.072985,-3.113340,-4.131658,1.301527,5.819270,8.829447,-9.649666,3.191079,-1.369879,-2.237649,-0.811477,-1.405788,2.641569,6.343232,8.562087,4.263004,7.749273,-8.714954,-3.192842,-7.500591,7.715402,-3.953067,-0.680796,-9.672626,5.771316,3.195641,6.608019,9.102480,-1.649910,1.722095,9.942482,-3.680372,-3.098032,-9.378991,-0.119683,2.435034,6.743820,-7.078347,5.147523,-0.616580,6.367034,-9.419699,6.537404,5.837062,-7.107689,0.307395,-3.122264,-4.781729,3.364278,8.098364,-6.684255,3.676942,-1.609542,6.850116,-7.318348,-5.035402,-7.229671,2.300412,-5.327928,7.570741,0.302742,-7.818749,-9.296338,3.619709,-2.730896,1.334212,9.639059,-5.490311,-9.968084,2.233335,5.132538,-9.191302,-8.144992,-6.686555,4.204968,-6.912857,-0.760413,-7.855409,2.034484,-3.715280,-7.974138,-2.690227,7.057333,3.333445,8.213533,-4.993811,-0.770222,-4.374273,-0.815817,4.821182,-9.211043,2.416476,-1.961113,6.815037,2.673523,6.235422,8.911299,2.888091,-7.493176,1.595464,1.060191,4.617624,-9.937202,-9.378131,-6.368427,-2.440056,5.738733,5.556323,4.689528,-9.548208,6.085288,-6.066235,7.281067,8.794722,-3.820626,5.477823,-1.948245,7.063898,-7.948432,-4.229757,3.879014,2.260161,-2.628875,3.811723,0.322767,-8.668651,9.484926,-4.937409,-2.504868,8.178065,-6.156667,-8.547243,3.059903,4.517417,5.287417,-1.023776,3.484077,-7.343212,-7.501071,8.484475,5.596888,-0.288133,5.035391,4.712598,-1.635427,-1.638254,-6.192297,-2.835433,8.496327,6.971134,3.845431,8.391164,-8.768233,-4.035278,5.526214,-3.562116,3.552462,-8.690042,1.995899,-0.277156,-4.496099,-6.322488,1.076276,-7.770924,4.630446,1.998078,4.560694,4.922662,-3.474079,-3.749346,6.931202,-1.407651,-7.992749,3.086232,9.934179,9.041504,5.138349,-1.213912,-4.595665,0.747705,-7.511341,-8.903674,9.726975,8.081204,7.105740,-7.915179,7.416732,6.374948,6.319179,8.911885,-3.155082,-1.400449,9.057752,-2.281339,8.255360,6.696678,8.108901,0.717356,0.169463,-6.214536,-2.705300,9.586107,-6.580099,4.598116,-3.690118,-8.037162,-7.231220,-2.860285,6.815600,4.312580,-1.202380,-9.564872,3.002808,-9.152385,2.148506], dtype = "float64")#candidate|2781|(450,)|const|float64
call_2779 = relay.TupleGetItem(func_555_call(relay.reshape(const_2780.astype('float64'), [6, 3, 3]), relay.reshape(const_2781.astype('float64'), [50, 9]), ), 0)
call_2782 = relay.TupleGetItem(func_558_call(relay.reshape(const_2780.astype('float64'), [6, 3, 3]), relay.reshape(const_2781.astype('float64'), [50, 9]), ), 0)
bop_2783 = relay.right_shift(const_2776.astype('int16'), relay.reshape(call_2775.astype('int16'), relay.shape_of(const_2776))) # shape=(2560,)
bop_2786 = relay.right_shift(const_2776.astype('int16'), relay.reshape(call_2777.astype('int16'), relay.shape_of(const_2776))) # shape=(2560,)
output = relay.Tuple([call_2742,call_2754,call_2764,call_2779,const_2780,const_2781,bop_2783,])
output2 = relay.Tuple([call_2743,call_2755,call_2765,call_2782,const_2780,const_2781,bop_2786,])
func_2794 = relay.Function([], output)
mod['func_2794'] = func_2794
mod = relay.transform.InferType()(mod)
mutated_mod['func_2794'] = func_2794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2794_call = mutated_mod.get_global_var('func_2794')
call_2795 = func_2794_call()
output = call_2795
func_2796 = relay.Function([], output)
mutated_mod['func_2796'] = func_2796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_2817 = relay.TupleGetItem(func_1299_call(), 1)
call_2818 = relay.TupleGetItem(func_1300_call(), 1)
func_2119_call = mod.get_global_var('func_2119')
func_2122_call = mutated_mod.get_global_var('func_2122')
const_2821 = relay.const([5.929378,-7.530605,2.659661,-0.775031,-8.722125,2.158435,8.548051,2.698985,0.241936,6.631938,0.269846,-6.089946,7.030908,-2.579312,0.651780,-1.173218,-1.043761,-5.591341,9.951480,-9.346938,5.864600,-7.508724,-2.142409,4.405363,7.849426,7.064696], dtype = "float32")#candidate|2821|(26,)|const|float32
const_2822 = relay.const([0.623460,8.221100,-1.838332,2.939391,4.208876,9.114440,5.073268,-2.238768,6.494554,3.401274,7.429091,2.958007,9.705577,6.444928,-3.525739,5.236338,-1.696552,-4.105490,-1.161855,7.916331,8.260833,2.992126,-9.993175,7.441055,-7.658245,-7.168745,9.784186,-0.347751,-3.722152,6.354090,-5.803312,-8.713136,7.634705,-0.148884,0.423747,6.656843,-1.165290,2.843700,0.522855,-3.105051,9.037029,3.215511,-6.703392,4.137712,9.321531,8.404301,-9.919410,-8.474288,-7.904197,6.073152,-3.360027,-6.894523,4.412695,-9.740928,-9.829423,-0.201958,9.404233,-7.202317,-5.085809,-9.946563,-1.355002,7.094286,4.589215,-2.458692,-3.196685,4.721411,2.053650,5.156484,3.698484,8.672637,-8.947263,8.550693,8.777131,5.288182,-5.865751,9.651002,8.946987,2.211011,-6.221401,-2.475252,9.432040,1.921952,8.957033,-4.391913,-5.928353,-2.984930,4.222881,-1.024868,3.541291,-8.458361,1.281769,-6.455302,3.197209,-2.271866,-6.232180,-7.129926,-6.543568,-1.935320,5.609845,3.268232,-0.955931,-8.836230,0.195394,-8.722618,5.531666,-6.739918,-1.823704,9.402823,-8.879186,9.721453,3.269563,3.068758,1.704233,9.534118,-7.073829,4.580226,3.608454,-1.879687,-1.044308,7.480215,-5.864638,1.968933,1.336501,-9.120192,-3.149333,-3.577510,0.661121,1.450226,2.503088,5.243330], dtype = "float32")#candidate|2822|(130,)|const|float32
call_2820 = relay.TupleGetItem(func_2119_call(relay.reshape(const_2821.astype('float32'), [2, 13, 1]), relay.reshape(const_2822.astype('float32'), [2, 13, 5]), ), 0)
call_2823 = relay.TupleGetItem(func_2122_call(relay.reshape(const_2821.astype('float32'), [2, 13, 1]), relay.reshape(const_2822.astype('float32'), [2, 13, 5]), ), 0)
func_2794_call = mod.get_global_var('func_2794')
func_2796_call = mutated_mod.get_global_var('func_2796')
call_2824 = relay.TupleGetItem(func_2794_call(), 5)
call_2825 = relay.TupleGetItem(func_2796_call(), 5)
output = relay.Tuple([call_2817,call_2820,const_2821,const_2822,call_2824,])
output2 = relay.Tuple([call_2818,call_2823,const_2821,const_2822,call_2825,])
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
const_2829 = relay.const([[[9.773950,-0.224241]],[[-2.034442,-6.963421]],[[-0.648615,-7.049993]],[[7.027514,-7.319524]],[[-4.172329,-7.738664]],[[-6.165438,-2.799337]],[[6.367966,7.945876]],[[2.735266,-8.469364]],[[1.516027,7.198642]],[[-2.494709,-9.034672]],[[-6.914857,-1.811119]],[[7.389231,-7.944486]],[[-0.695432,7.391474]],[[2.275187,2.626473]],[[1.603262,-4.011283]]], dtype = "float64")#candidate|2829|(15, 1, 2)|const|float64
uop_2830 = relay.cosh(const_2829.astype('float64')) # shape=(15, 1, 2)
var_2835 = relay.var("var_2835", dtype = "float64", shape = (15, 12, 2))#candidate|2835|(15, 12, 2)|var|float64
bop_2836 = relay.minimum(const_2829.astype('float64'), var_2835.astype('float64')) # shape=(15, 12, 2)
bop_2846 = relay.logical_or(const_2829.astype('bool'), relay.reshape(uop_2830.astype('bool'), relay.shape_of(const_2829))) # shape=(15, 1, 2)
uop_2849 = relay.cos(bop_2836.astype('float32')) # shape=(15, 12, 2)
bop_2852 = relay.left_shift(const_2829.astype('uint64'), relay.reshape(uop_2830.astype('uint64'), relay.shape_of(const_2829))) # shape=(15, 1, 2)
func_2722_call = mod.get_global_var('func_2722')
func_2723_call = mutated_mod.get_global_var('func_2723')
call_2855 = relay.TupleGetItem(func_2722_call(), 0)
call_2856 = relay.TupleGetItem(func_2723_call(), 0)
uop_2865 = relay.tan(uop_2849.astype('float32')) # shape=(15, 12, 2)
func_784_call = mod.get_global_var('func_784')
func_788_call = mutated_mod.get_global_var('func_788')
const_2868 = relay.const(9, dtype = "uint8")#candidate|2868|()|const|uint8
const_2869 = relay.const([5,9,1,3,-1,-8,-2,-9,-1,-3,9,2,-8,-5,6,-5,1,4,-3,-5,8,9,8,-4,9,9,-7,7,6,6,-9,5,-5,2,-10,4,10,7,3,4,-1,2,-6,5,3,5,2,-2,1,-7,-10,-8,-6,8,-8,-3,-7,-7,4,-4,5,8,9,6,-3,8,4,6,1,-1,-6,8,-9,-6,-10,9,8,-5,-7,-5,-4,6,1,9,-5,2,5,5,-6,-7,9,-2,-3,-4,-7,-3,-5,10,10,-7,2,-6,-1,2,-10,-4,5,6,4,-8,-10,-2,9,-1,3,-6,9,-3,3,-6,4,-1,-7,-7,-8,1,-6,-5,7,6,3,-7,3,1,-3,6,10,-8,-8,-7,2,6,-1,6,8,9,3,-4,-4,-2,-5,-6,-8,9,1,-4,-3,2,-3,1,-10,3,-6,10,3,9,-10,10,-1,-6,6,-7,10,3,8,5,4,-3,-4,-10,-7,-4,4,-9,-4,9,-4,-8,-6,8,-5,-3,-10,1,3,10], dtype = "uint8")#candidate|2869|(196,)|const|uint8
call_2867 = func_784_call(relay.reshape(const_2868.astype('uint8'), []), relay.reshape(const_2869.astype('uint8'), [7, 2, 14]), )
call_2870 = func_784_call(relay.reshape(const_2868.astype('uint8'), []), relay.reshape(const_2869.astype('uint8'), [7, 2, 14]), )
bop_2884 = relay.logical_or(uop_2865.astype('bool'), relay.reshape(bop_2836.astype('bool'), relay.shape_of(uop_2865))) # shape=(15, 12, 2)
func_907_call = mod.get_global_var('func_907')
func_908_call = mutated_mod.get_global_var('func_908')
call_2897 = relay.TupleGetItem(func_907_call(), 0)
call_2898 = relay.TupleGetItem(func_908_call(), 0)
bop_2904 = relay.multiply(bop_2846.astype('float64'), relay.reshape(const_2829.astype('float64'), relay.shape_of(bop_2846))) # shape=(15, 1, 2)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_2910 = relay.TupleGetItem(func_2658_call(), 0)
call_2911 = relay.TupleGetItem(func_2660_call(), 0)
func_1073_call = mod.get_global_var('func_1073')
func_1075_call = mutated_mod.get_global_var('func_1075')
var_2915 = relay.var("var_2915", dtype = "float64", shape = (72,))#candidate|2915|(72,)|var|float64
call_2914 = relay.TupleGetItem(func_1073_call(relay.reshape(var_2915.astype('float64'), [6, 1, 12])), 1)
call_2916 = relay.TupleGetItem(func_1075_call(relay.reshape(var_2915.astype('float64'), [6, 1, 12])), 1)
uop_2918 = relay.exp(bop_2884.astype('float32')) # shape=(15, 12, 2)
uop_2939 = relay.sin(uop_2918.astype('float64')) # shape=(15, 12, 2)
uop_2942 = relay.rsqrt(uop_2939.astype('float32')) # shape=(15, 12, 2)
output = relay.Tuple([bop_2852,call_2855,call_2867,const_2868,const_2869,call_2897,bop_2904,call_2910,call_2914,var_2915,uop_2942,])
output2 = relay.Tuple([bop_2852,call_2856,call_2870,const_2868,const_2869,call_2898,bop_2904,call_2911,call_2916,var_2915,uop_2942,])
func_2945 = relay.Function([var_2835,var_2915,], output)
mod['func_2945'] = func_2945
mod = relay.transform.InferType()(mod)
mutated_mod['func_2945'] = func_2945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2945_call = mutated_mod.get_global_var('func_2945')
var_2947 = relay.var("var_2947", dtype = "float64", shape = (15, 12, 2))#candidate|2947|(15, 12, 2)|var|float64
var_2948 = relay.var("var_2948", dtype = "float64", shape = (72,))#candidate|2948|(72,)|var|float64
call_2946 = func_2945_call(var_2947,var_2948,)
output = call_2946
func_2949 = relay.Function([var_2947,var_2948,], output)
mutated_mod['func_2949'] = func_2949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_2951 = func_753_call()
call_2952 = func_753_call()
func_2337_call = mod.get_global_var('func_2337')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_2963 = func_2337_call()
call_2964 = func_2337_call()
uop_2965 = relay.log10(call_2963.astype('float32')) # shape=(450,)
uop_2967 = relay.log10(call_2964.astype('float32')) # shape=(450,)
output = relay.Tuple([call_2951,uop_2965,])
output2 = relay.Tuple([call_2952,uop_2967,])
func_2969 = relay.Function([], output)
mod['func_2969'] = func_2969
mod = relay.transform.InferType()(mod)
mutated_mod['func_2969'] = func_2969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2969_call = mutated_mod.get_global_var('func_2969')
call_2970 = func_2969_call()
output = call_2970
func_2971 = relay.Function([], output)
mutated_mod['func_2971'] = func_2971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_987_call = mod.get_global_var('func_987')
func_988_call = mutated_mod.get_global_var('func_988')
call_2972 = relay.TupleGetItem(func_987_call(), 0)
call_2973 = relay.TupleGetItem(func_988_call(), 0)
const_2976 = relay.const([[[-9,10,1,9,10,-1],[3,1,5,5,9,-6],[4,7,9,5,-8,-10],[-3,-4,-6,-5,8,-4],[-6,-8,4,-9,3,-8],[-3,-10,10,-1,10,5],[2,-3,-8,7,8,8],[-9,-2,5,7,-3,-1],[9,-5,1,5,9,-6]],[[-8,8,8,10,5,4],[-2,-9,7,9,6,-5],[3,10,1,-9,-9,-7],[-5,8,8,1,10,6],[-4,5,8,-6,-3,5],[2,-3,2,-10,6,6],[-8,6,1,-9,-9,-2],[6,2,-4,-1,10,7],[-5,-9,-5,-7,-4,-4]],[[6,-9,-8,4,8,-1],[-2,9,8,3,5,4],[-7,-4,3,5,1,-6],[4,3,5,-6,-8,-8],[1,2,1,5,-7,10],[-6,1,8,4,-9,-6],[1,-1,7,7,-1,3],[5,2,6,3,-7,-7],[4,-7,-10,-7,-4,-10]],[[-8,-8,-6,-10,10,2],[-4,-8,-1,-5,8,-8],[-4,-9,-3,-9,6,9],[8,-2,3,-4,8,9],[-9,-4,6,-7,-7,1],[7,-1,9,6,1,-6],[3,5,-4,-3,-7,-1],[-1,5,7,9,6,-9],[-2,-2,5,9,-2,9]],[[9,10,-7,10,3,5],[1,-4,-4,4,9,8],[6,10,-4,-5,-9,8],[7,-5,1,-10,3,-1],[-8,2,-1,-9,-2,6],[-8,-8,7,4,-3,-6],[-8,-9,2,-8,5,8],[-4,4,8,3,-2,-2],[8,4,-4,8,-7,-2]],[[8,-9,-2,10,6,4],[-3,-9,-8,5,8,7],[-10,-3,-3,5,-5,-8],[-1,-6,2,10,-7,-4],[3,-2,7,-4,-6,3],[2,-5,-2,5,-1,10],[-3,1,-1,-6,4,-7],[9,7,8,5,8,8],[-2,3,6,-7,6,-8]],[[2,-3,-3,-7,-2,8],[-6,10,4,6,-1,-9],[2,3,-5,7,6,-6],[-10,3,-1,10,5,-3],[-7,7,8,2,-4,-10],[-9,-10,6,-4,-1,6],[8,-9,-5,-4,-1,-8],[-6,1,-9,-1,-9,-3],[-7,9,6,9,-1,-8]],[[3,1,-2,-5,3,-10],[-8,-1,4,-1,-1,-2],[-8,-10,1,9,10,8],[-9,10,-10,4,-5,-8],[-7,1,-1,-6,4,-10],[-5,-9,-7,9,-3,-7],[1,-4,4,-5,-10,2],[1,-10,5,-2,-7,7],[1,9,5,6,7,4]],[[1,-4,-8,-2,-6,4],[10,-4,-8,-10,-9,10],[7,3,7,5,7,-8],[-8,3,-3,-7,-4,10],[6,-8,1,10,-5,1],[-10,-1,6,1,-2,-1],[-3,7,-1,-9,1,3],[-7,-9,6,6,6,3],[7,-9,-10,3,9,3]],[[9,7,9,-1,3,-1],[-1,4,-2,-3,-3,-7],[3,8,-10,-1,3,10],[-10,-10,-2,-1,-6,2],[4,-7,8,-9,6,2],[-8,-6,3,-5,-8,5],[6,4,-4,1,4,4],[6,4,9,-7,-8,-8],[-10,3,7,-7,-7,8]],[[9,-9,9,-4,7,6],[-3,4,7,-4,6,4],[-9,-8,-2,-8,-6,-4],[2,-10,8,-4,-9,4],[-2,-3,-10,-2,8,5],[-6,10,2,9,-4,3],[-6,-4,-7,1,9,-8],[8,7,-1,5,5,-1],[1,-1,10,-8,-2,1]]], dtype = "uint16")#candidate|2976|(11, 9, 6)|const|uint16
bop_2977 = relay.logical_or(call_2972.astype('bool'), relay.reshape(const_2976.astype('bool'), relay.shape_of(call_2972))) # shape=(11, 9, 6)
bop_2980 = relay.logical_or(call_2973.astype('bool'), relay.reshape(const_2976.astype('bool'), relay.shape_of(call_2973))) # shape=(11, 9, 6)
output = bop_2977
output2 = bop_2980
func_2993 = relay.Function([], output)
mod['func_2993'] = func_2993
mod = relay.transform.InferType()(mod)
output = func_2993()
func_2994 = relay.Function([], output)
mutated_mod['func_2994'] = func_2994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mod.get_global_var('func_736')
func_737_call = mutated_mod.get_global_var('func_737')
call_3012 = func_736_call()
call_3013 = func_736_call()
output = relay.Tuple([call_3012,])
output2 = relay.Tuple([call_3013,])
func_3014 = relay.Function([], output)
mod['func_3014'] = func_3014
mod = relay.transform.InferType()(mod)
output = func_3014()
func_3015 = relay.Function([], output)
mutated_mod['func_3015'] = func_3015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2794_call = mod.get_global_var('func_2794')
func_2796_call = mutated_mod.get_global_var('func_2796')
call_3016 = relay.TupleGetItem(func_2794_call(), 6)
call_3017 = relay.TupleGetItem(func_2796_call(), 6)
uop_3024 = relay.acos(call_3016.astype('float64')) # shape=(2560,)
uop_3026 = relay.acos(call_3017.astype('float64')) # shape=(2560,)
func_2319_call = mod.get_global_var('func_2319')
func_2321_call = mutated_mod.get_global_var('func_2321')
call_3029 = relay.TupleGetItem(func_2319_call(), 0)
call_3030 = relay.TupleGetItem(func_2321_call(), 0)
const_3032 = relay.const([7.192012,-9.355263,7.861617,0.217217,6.548925,0.798362,-4.139026,8.492158,9.396936,-3.654020,5.510301,-9.474872,3.735342,2.023407,6.572608,-9.770878,-2.718064,-1.722981,-3.842011,2.289557,8.136525,8.171288,-5.513043,1.107136,-7.376961,-2.086801,3.290841,-8.244123,-2.248788,9.487823,6.162449,8.169386,4.056960,0.106623,2.446241,5.496508,2.495729,-6.495947,3.102285,4.112306,9.659952,7.618882,-1.654052,6.132247,9.161087,-1.643737,-1.615128,-9.971757,-7.914580,-4.563871,8.133837,-1.180535,-7.911807,-8.146292,-4.059956,-4.502228,8.570325,2.756571,8.622855,0.610770,9.651197,7.757070,9.974880,6.229924,3.300134,6.676653,0.038130,0.634909,-3.245532,0.830718,2.187205,1.046621,3.061375,-8.987250,4.374385,-4.433243,-1.556923,3.502921,9.295490,2.597537,-6.289779,0.130162,-2.471784,5.726217,-1.966450,5.156500,-4.648138,7.135925,3.278874,7.445506,0.021806,-6.895295,6.440287,1.904563,-4.620261,-4.507065,8.642632,9.323740,-1.743294,-3.167337,5.331388,1.265546,-7.196396,-3.963306,-6.075629,4.129139,9.066161,6.237177,5.121558,7.628791,6.526667,-9.667233,-7.702520,-4.971156,-8.906486,1.118904,8.060612,-6.477695,0.272945,3.721159,-1.882619,2.103817,-9.880717,-8.731069,6.414843,-4.549224,9.991810,2.759024,-5.290134,3.631485,3.879829,-2.292976,7.038509,-4.960367,8.342873,-7.976111,-2.050104,5.183556,0.733336,-1.073108,-9.048410,6.615551,4.065204,8.503283,3.993722,7.792093,7.732367,8.681277,-0.258604,-3.072710,0.360777,0.802339,-0.460591,4.577651,-0.058481,1.027949,-7.676757,3.742744,9.662091,0.161600,3.632963,1.706123,-5.953533,5.219616,3.508850,7.122215,-8.153526,-1.576955,3.357475,-2.297678,-5.277793,-9.999594,9.230379,-3.182819,-3.986405,3.800994,-9.841388,8.924115,0.612234,8.308222,-7.014545,8.706789,0.699359,5.720522,6.010203,2.746254,2.064436,-8.159869,6.261295,-4.589065,-3.204079,5.095038,-3.579737,-9.735519,9.461219,-0.447691,-5.305357,-4.117854,-1.268716,-6.883855,-4.135955,8.291804,-1.385173,-5.994880,-8.726248,0.928054,-0.970625,-3.824158,8.166073,-4.289142,-6.120893,-8.970651,-5.525306,3.882494,6.056075,0.324908,6.360593,0.182290,-7.945026,6.919564,-6.546415,-9.996564,0.972560,-7.029919,7.825617,0.396477,3.455594,-8.853188,-3.403271,-4.790571,5.959193,8.862213,-4.830512,-2.334521,-1.690607,-4.224169,9.117671,5.869095,0.305647,3.874187,-5.631355,-3.294334,6.331274,-1.898449,-6.493138,1.435961,-1.480291,-2.041755,7.377416,0.624637,-0.975237,6.924479,-2.623666,-1.571661,-7.045147,-6.500102,-3.125449,-8.969646,9.009428,-7.837947,-1.709806,-5.796751,-1.609744,3.688251,7.209941,-2.012578,-0.448031,1.180505,-6.303793,-7.883929,-3.012160,-4.058617,-0.395644,-5.464484,4.107163,0.440225,-7.134937,-1.674727,3.793175,-6.354268,-5.104930,-2.614201,-6.328578,-8.394556,-4.017583,8.327875,8.484043,9.020794,5.898228,-6.363125,-0.724440,-5.254059,9.038296,-3.096790,-1.138197,3.197618,1.145452,-0.286826,-0.800698,-7.538045,6.604074,9.073563,9.601536,-9.924526,-8.284756,9.738806,7.663939,6.604970,-4.037419,8.959954,-1.303655,-4.396962,-6.907612,-8.227847,4.667091,7.786466,-2.829765,3.843247,-4.309984,-3.965303,-6.693135,3.684663,9.651762,-4.760672,-2.665788,7.252027,2.873108,-2.711455,-2.955418,-4.269826,-1.337842,-9.482547,-0.885933,-1.876933,-5.383249,3.705363,8.167279,-3.339495,8.976190,-3.086393,-3.903340,-7.428699,3.176445,9.995117,8.897080,8.225399,-5.112414,6.013722,-4.868925,5.323653,-7.179134,8.827116,7.067353,7.703766,2.759063,5.257876,3.362013,2.580782,-8.384894,-3.096684,-5.415681,7.970146,2.304595,3.530633,3.101878,-4.592907,4.218006,0.318650,4.874378,8.830555,-6.189873,-2.217394,-8.330088,4.866397,1.255672,0.182860,2.309169,-8.873965,3.595111,-0.218831,-6.351838,-8.048711,4.635677,-6.048106,-1.178720,3.274665,-8.587884,-1.116773,9.308741,-0.950626,1.346935,-3.142596,-7.481404,-4.359491,-8.961139,-3.667789,1.446543,-7.351819,-4.660153,-3.216470,-3.705438,-4.947109,9.306525,7.244421,-2.976006,3.414417,6.532729,-0.079615,-5.931232,3.649390,-2.579355,0.212763,2.747207,-5.102065,7.842518,-5.187008,-8.953760,-9.916287,-7.636075,-5.886237,1.916910,-1.336190,6.359466,8.652124,9.563737,-9.145898,-7.534559,-1.822577,9.897460,-8.460239,4.139886,-3.820653,1.452732,1.204616,-0.617869,-0.619622,-3.715851,9.092887,9.217262,0.540966,7.930520,-8.348616,-6.559505,9.097944,9.870135,-6.498686,9.392266,-1.283648,8.369927,-5.211624,4.468707,-8.781270,2.442197,6.878285,-4.053015,-8.061122,-1.768488,8.185530,7.673210,-7.422987,-9.059177,0.617391,6.487087,-1.344323,1.927075,4.036330,7.743923,-2.460537,2.619822,-3.394969,3.958685,7.740213,6.825755,-0.859112,-9.776475,-3.747990,8.873506,-8.243249,0.489602,0.189818,9.024255,-1.002172,-2.895406,3.818210,-8.097161,8.254306,-8.469023,-1.722933,-1.130934,-1.042870,1.533510,2.461217,-1.791826,-3.676356,5.319164,0.055719,-5.639413,5.345044,-7.729978,-0.512809,-2.685589,-4.477808,-4.464843,3.487089,3.852887,9.785851,-9.689343,4.161429,-8.893845,-9.062777,-2.471248,-3.277295,1.147810,8.976789,0.465446,2.284364,-7.946750,-7.718077,-6.397852,7.778435,-1.741837,-2.134621,7.710064,7.140850,8.623074,0.903715,1.240401,-5.873427,-8.965306,1.573898,1.971794,0.898321,-7.287363,0.069994,7.925147,9.973612,3.070910,-7.577931,2.768160,8.226409,-5.089676,-7.826003,-8.743633,-8.098267,5.168643,-3.118310,-8.115570,-4.829936,-4.070190,4.151193,-5.259362,6.491599,0.438182,-8.295233,4.817738,3.312226,6.376785,-7.377296,6.956514,-6.305914,-4.162751,5.811736,-9.891109,3.944868,6.596737,6.381691,3.868989,-4.303741,-3.469251,-6.434863,-0.233266,3.574818,2.567610,8.275331,5.834985,5.697619,0.103181,-8.958800,-0.924211,-5.103669,5.416908,4.237935,-7.020423,4.526522,7.977341,-2.033960,3.164147,7.781870,5.821541,8.124754,-4.242822,-7.518795,-4.295220,4.646326,3.088711,-2.795840,4.689479,4.761465,1.160959,6.050559,-3.717551,-1.320160,1.006691,1.586205,1.961099,4.657050,1.071357,4.357080,2.754611,3.323530,-0.397363,4.192464,9.834685,4.081304,4.864217,6.095396,-4.818012,1.723117,2.650890,1.343964,-0.307137,-2.990667,-9.976339,7.082599,6.166969,-0.554975,-7.150672,5.526727,7.013776,2.262111,0.415565,-6.679856,-6.041426,-7.405885,-1.367504,-9.816565,-5.539598,4.161928,-0.469268,-5.069753,8.593443,9.150415,-1.913749,7.567935,6.505641,-1.003012,-2.145589,1.416332,4.229618,-3.014466,9.477919,-7.701095,-2.736336,-3.166813,-2.179413,-2.924728,-1.618046,1.269814,-6.111635,-5.030086,3.558625,2.374954,0.161376,7.002048,-5.149201,8.183135,-5.376446,2.317561,7.607064,-0.900412,3.642475,1.129816,-8.554937,-7.377821,0.633190,6.884582,-2.951521,-7.931079,9.458864,-1.231960,-7.600499,8.842354,7.435883,4.587755,-1.905299,-3.993718,-4.059047,9.315284,-1.448977,1.578747,-7.812739,1.149439,7.818035,1.880346,3.757788,-1.950597,4.559222,-4.739653,2.423226,0.564055,8.294803,8.882527,6.544974,7.323870,-0.444164,1.027410,6.659394,3.284480,4.058545,6.395973,-2.865624,-4.789763,0.274744,-0.500138,-9.226042,-3.393114,1.353547,0.324841,5.000943,5.379857,6.748451,-8.101281,0.537233,-6.023411,-6.587788,4.682526,1.425405,-1.389431,-6.440911,9.363393,-3.055139,4.763088,3.838295,-8.277835,1.179557,8.122576,2.478850,9.917809,2.648601,6.961663,7.041823,0.729928,-9.297205,1.288434,-6.627140,8.610421,-2.819388,0.883021,7.171218,-7.788739,6.104029,6.172531,-0.142709,9.234359,-7.604013,5.444826,3.448536,2.418834,0.738352,-6.851301,6.014347,-0.818217,-9.153490,-8.852456,-7.187002,-3.232866,-2.528465,-3.313697,-4.850416,-0.679360,-4.988042,-4.665956,-7.572934,0.866830,-0.063683,-2.299857,6.686306,-1.694970,-1.617563,6.673019,3.200895,-4.806104,0.690301,-3.713742,-2.779107,0.479455,7.198634,-9.264689,7.282179,7.898737,2.177616,4.565959,-5.400827,4.923889,-1.811867,5.602306,-7.360948,2.036186,-6.383878,-4.333669,1.629023,2.032097,6.568619,-1.279969,9.600722,4.896754,2.038159,3.725883,-2.254413,-5.296699,6.736219,-3.110859,5.468701,-6.936667,-6.571599,-5.239193,-9.161353,-3.877373,9.359148,-3.651128,-1.086600,-5.614129,-1.462858,1.041280,-8.245003,-4.969216,-5.489941,4.336236,-5.612508,6.628010,-8.943244,-6.648468,-8.098260,8.967066,-5.067931,-9.639866,0.730828,-5.013782,4.229206,-6.492592,-9.268568,0.994877,4.236279,-3.928676,-4.899802,-2.531540,-0.914193,6.780540,9.717315,-2.079852,-0.534261,-8.153531,7.967474,-4.749144,8.779110,-5.807260,5.820336,-3.339911,5.030086,-1.666813,-4.140614,-4.146244,-3.136701,7.459179,-1.151384,3.582723,7.361171,-1.756555,-2.109913,1.300270,9.291623,5.913142,4.158882,-8.454033,3.809162,5.976444,4.620127,-0.064393,9.350440,-1.080436,2.463930,3.387458,4.783840,-5.041978,-2.129748,2.127947,9.757876,-9.829163,-1.392510,3.351541,0.548691,-4.584959,8.754811,-7.623508,-3.857824,-8.125869,-6.226991,-2.989695,-9.741102,-3.753839,-9.280704,-6.158582,-3.004963,8.057738,5.605485,-1.592212,5.130554,-7.824350,2.826187,0.090908,4.268290,-0.584465,4.918533,1.570987,5.947112,-6.973843,-3.446149,4.850992,1.802657,1.386519,-8.053598,-0.090455,-2.855728,-0.877157,1.367670,-2.139389,6.320674,9.129904,7.825119,-2.470158,-6.003912,9.165649,-6.855252,6.439593,3.245987,-1.238601,9.479547,6.073982,9.072014,3.050424,3.764123,6.259731,-9.190149,-8.181254,-3.408957,-1.613229,6.269025,2.918863,1.730785,-1.349166,6.019680,-6.261414,7.607514,1.879102,5.634894,1.384086,-7.387599,0.946658,5.679032,-2.282049,5.996064,-1.143062,-5.469596,-3.642296,6.498340,-2.504699,2.865540,0.697151,-6.192602,-3.520631,8.671154,2.191995,-9.404105,1.761304,-5.723822,4.870226,-6.064127,-3.591354,5.101420,-5.301502,5.963938,-9.512677,8.538113,0.931424,-5.856963,1.789325,-1.092134,4.123212,-9.560904,-8.384024,-9.973359,-3.910795,-9.217799,-8.868264,9.342947,-8.931543,1.091466,9.441961,-4.460445,7.537932,-7.684317,-1.116658,3.210353,-0.795577,-2.837699,-1.667614,-8.713896,-6.528787,3.002056,9.864610,5.190666,-3.459159,-4.980733,-7.363254,-9.747981,9.298178,-0.363560,2.730104,6.258941,6.649359,3.287365,-5.612319,-7.126898,-1.228212,9.532955,-9.196063,5.829197,-4.177498,1.563475,-8.144723,-2.731117,-9.476705,8.553756,-5.680355,0.172584,5.950707,2.777063,2.577564,-2.866602,4.329580,6.896764,-0.738229,-9.100036,-7.035317,0.639333,-0.013381,-5.127011,4.353819,-1.422185,-3.718449,3.978110,-4.102928,5.788999,9.864713,8.479219,-9.014640,-9.642559,5.375396,6.429711,-0.613374,-1.205177,-4.913854,-6.447510,9.751640,3.062409,-2.428057,2.218973,8.965623,-4.086752,-4.096727,0.063606,-1.864909,8.777439,5.809290,9.368028,-6.547595,-6.829863,-5.369890,-2.598748,7.695886,1.616947,-4.880823,8.033421,-9.229028,-1.442732,4.070420,5.070195,-5.675407,-9.794824,2.149805,7.610668,3.095975,-8.188345,-9.868027,3.481975,-4.298348,-8.818137,1.812085,-6.048537,1.123652,-2.527117,-1.998134,9.207039,2.968204,-4.282853,7.332468,-4.254241,7.758326,5.013347,7.772210,-8.611622,7.959837,-3.010081,-3.139939,-5.155353,-5.752293,-4.011571,-3.049594,9.067230,4.499093,-1.019528,4.913888,-5.557648,6.528972,8.873321,-8.922270,-4.121519,-0.997139,9.779260,8.999079,-1.428911,-7.847944,7.003135,-0.407278,-6.130349,-2.614638,2.710246,1.632018,9.651811,3.404930,4.757540,-7.016452,6.244138,7.498625,7.810103,5.017695,-5.980412,-3.832596,-7.388702,-0.595399,4.445736,-1.514797,-4.885715,-2.396125,-8.518740,-0.019757,4.587900,-1.156369,1.294646,6.424795,-0.267980,5.699428,9.221593,-9.455726,-7.374426,-6.802805,-9.745309,-9.988995,6.101183,-6.476013,-1.296108,2.795642,3.877336,3.517622,4.260697,8.756196,5.424839,-2.768976,-4.139558,-9.709417,4.841680,-5.052544,2.360997,5.278841,4.140388,1.811835,-6.411463,-1.578220,-8.248505,6.356435,-3.726740,1.188169,4.091079,-2.310684,4.917275,-5.722141,-3.871389,-8.076095,-5.356245,-6.881602,2.270317,3.010643,-6.273115,7.973834,6.743784,9.560004,0.554676,5.692606,-4.873520,-1.622876,8.196574,0.567032,-4.520238,2.575353,9.864248,-2.528655,4.736266,-4.976785,8.367435,-8.039513,-9.443945,8.435603,6.279926,-8.583838,-1.036277,6.104586,-9.521306,2.284423,-9.535207,5.920880,-3.004869,-3.098573,2.771096,-9.233460,-0.830250,-7.879422,-5.157805,-0.716721,-1.939486,0.833482,3.696500,-9.293502,8.825859,-3.976154,7.460511,7.906992,-3.387793,0.390842,7.916908,-1.293256,9.475578,-6.418512,-8.615798,9.508116,-2.451646,-6.453280,3.113624,6.268725,-8.089671,-2.578939,2.183314,-4.730233,3.732320,8.659988,7.530315,-2.391278,-8.313068,-4.007362,5.000245,-9.598333,-4.606337,2.075599,7.796471,4.782015,8.496644,0.965936,4.391668,-6.668569,-2.083798,4.913147,2.789003,-6.400298,0.566297,1.837785,-7.987725,-8.576029,-6.037795,-5.472743,-3.702145,1.973457,4.723726,-9.163627,-1.022038,7.536445,-2.881950,-6.742695,-3.899292,-6.854458,1.960917,-1.228503,8.448566,9.177807,-7.073259,8.289712,3.998175,-9.834614,-8.209701,0.493439,0.768506,3.171874,-5.695231,-1.650567,-4.515303,-1.019868,-3.312756,4.350967,2.657489,2.377859,-1.170768,-6.900880,6.071220,-2.578521,0.446037,9.591095,-3.789883,-9.180732,-5.767167,2.337205,0.938149,1.184632,-9.918030,8.804973,6.254905,1.832469,-9.287168,6.833866,5.132555,5.173061,5.378993,6.817743,3.913435,-6.689570,-9.829381,-9.791164,2.862526,2.390726,-4.358859,8.143832,8.200498,4.273179,-9.989789,-3.118206,-1.098511,-4.137624,-9.725974,7.966809,-6.039333,0.330236,2.491298,-2.593948,8.734776,-5.913303,7.668045,0.778489,-2.275953,-8.274896,2.601916,-2.602061,-5.161675,-6.438438,4.595294,-4.032573,6.803753,-9.033456,8.762001,-6.778579,5.021999,-1.383413,-2.169460,4.981441,-8.343581,-1.948188,-8.331237,8.758601,5.444348,7.385731,1.526165,-6.734471,-0.257956,5.234602,-3.465677,-7.808399,-7.239122,-7.182356,9.950489,2.325966,7.969050,0.342092,8.330951,-0.686154,-5.253030,1.433207,2.469108,7.624313,-9.280770,2.520588,-9.221264,-7.121062,-3.357087,4.560359,7.659480,0.964492,-2.198304,-9.886277,3.488825,2.224096,6.465924,6.657392,-9.965160,-5.185490,7.518181,7.397875,3.400030,-8.968320,-8.046279,8.428942,-1.179024,-4.219167,-4.075154,-8.647956,7.500847,2.479818,-5.645594,2.099129,6.098781,-7.196358,0.371575,-5.560807,1.375323,-8.425507,6.196240,3.739676,-7.429801,-6.697960,1.375876,-5.179807,-9.362578,8.698855,-8.347704,-1.525032,-5.142166,-8.349130,-0.443337,-7.685761,8.182617,-2.173649,0.502454,8.936037,1.934388,-9.192101,-4.087931,-6.647353,-4.882814,-3.586809,-9.960638,9.849421,1.114559,6.732743,-9.928357,9.710755,-6.083626,-2.455726,-5.250053,-7.816084,-6.414678,-1.503347,1.804783,8.962078,-1.752020,1.782136,-7.685719,2.049529,-5.496717,-8.497258,-3.786638,2.844497,8.241571,-4.400411,7.984667,8.006398,0.440295,-1.311400,-0.364760,3.236922,9.288443,-5.854283,5.512334,9.264631,-0.679197,-9.456299,-2.304332,4.692359,-5.869978,1.589751,-1.915137,6.064056,-1.155762,9.803317,4.183863,9.140715,3.033463,1.064579,2.561079,-0.936062,-1.637983,-4.005228,-5.612643,-6.569657,-2.497688,-5.195748,-6.901369,-0.338684,-3.302660,-7.784671,-4.522309,-7.149922,0.403539,-6.468800,8.966530,-6.154465,-6.694513,-4.971845,-1.187484,3.920571,-1.293467,-2.941367,5.436723,3.756318,-8.117354,7.300613,4.544678,-5.732120,8.465405,6.466020,3.754574,-8.023664,-0.614948,1.710635,8.078058,5.326634,-6.475169,3.772860,6.975931,9.780659,-5.686031,-0.457814,3.374812,-7.400520,-4.912646,9.636470,6.564852,6.614730,-0.943491,-8.311671,5.430130,0.071164,6.468312,6.237396,6.434711,-3.911199,6.549090,3.394093,9.418509,-7.708983,7.028018,-4.048854,2.954327,-4.528518,-8.370582,-2.310640,4.985834,3.290055,-8.506013,5.800642,-4.012167,1.617488,-9.796270,-1.029295,-5.812791,1.922363,-6.398020,-8.400323,8.786608,0.282085,7.773835,9.101922,0.094494,-7.549862,3.784481,8.497209,5.276406,-6.153967,6.009142,-9.825824,2.043182,8.605217,4.559876,4.468423,-5.103062,-0.105116,-4.231246,-6.114461,-2.301652,4.107628,-1.519397,5.290339,5.109860,-0.854716,-0.836356,-5.550845,-3.760568,3.025679,8.060311,9.857178,3.724058,-7.026164,8.076393,2.896824,4.647956,-4.102594,1.755426,7.225793,3.765220,0.270817,-5.501352,3.468221,1.646291,-4.130560,6.776931,1.980201,2.162773,5.886260,-2.900537,7.814555,6.807888,-7.885516,3.428361,-1.400263,0.802471,5.753374,2.290748,-0.402019,9.576686,-2.524555,-1.024142,-3.120160,0.625423,6.823458,-7.993690,7.604489,-3.622031,3.165752,7.192914,-8.709361,6.979391,5.837835,-9.193395,-6.072699,-9.462795,-0.563401,-2.555720,2.550762,-6.269343,4.906345,6.814749,9.484151,-8.703445,6.080695,-5.721781,-1.298732,2.431659,-5.690331,-4.898810,-1.777587,0.166459,6.542226,0.952759,8.877835,7.193480,-9.428904,8.961060,-0.067582,-7.432861,-9.866989,2.354697,5.164301,-7.994361,-1.151893,-2.228778,9.512648,-0.694029,7.541802,3.728925,2.729542,1.585974,3.824259,5.653160,0.804144,-2.778139,-7.881682,-9.934181,-8.719070,-8.550070,7.022048,5.435134,-1.890116,-2.913271,1.553529,7.906081,-6.753674,8.228454,1.793647,-6.911754,-2.294281,-5.630086,-7.426637,-1.717816,9.735953,-9.759111,9.968479,-2.582381,3.857734,1.929014,-5.331186,4.690318,-3.438401,9.321683,-2.240430,-7.915182,-2.763172,3.420342,2.819230,8.585579,-0.822742,-0.364848,-3.261088,-1.928828,9.023483,-2.652561,-7.693833,-4.618978,-7.205492,-7.860516,5.413032,-5.414488,-3.751931,9.052900,0.213750,-0.432324,-3.181268,-6.997865,8.418982,-1.434482,-2.709757,2.272596,-1.891034,8.344172,9.250584,2.980438,-2.735623,-1.634257,-4.944907,0.711074,-1.868631,3.257013,-8.168837,4.294198,-6.362106,-7.020568,2.930147,4.638380,5.547496,-5.835302,1.889192,-5.251028,8.954454,-9.459950,-0.400025,-3.691038,5.300213,4.107823,2.579751,-1.542878,-8.049304,-1.962086,-5.603460,0.714129,2.043029,-3.810763,-0.934203,-6.244677,1.198649,7.130762,-3.187468,-8.602408,8.860106,8.457371,8.529783,0.914859,-3.303610,9.826560,0.266930,6.581120,-1.229380,0.032231,-7.264090,9.996640,-2.552672,5.457260,-0.205984,6.259124,8.808329,-5.574673,-5.340219,-0.693927,4.733501,0.113638,-4.005780,1.081969,-2.699766,8.873695,2.959108,-1.215418,0.894856,-1.923841,5.655573,-8.902567,2.618271,2.193396,-1.657874,-3.428795,8.420429,-9.760121,-0.546981,8.373006,7.256963,7.142825,5.514230,-7.060716,0.887727,-7.146382,-9.245317,8.525924,7.965650,0.767228,-5.402896,7.638909,7.909260,-2.448690,-1.130305,-6.115146,-7.764828,-2.338015,3.515861,1.383321,3.797414,-0.988377,-1.173086,2.991695,-0.909009,9.611539,6.563680,7.034631,-8.356514,-2.272565,6.524951,-9.963583,9.206941,0.445601,-1.808051,6.610787,-5.428322,7.041490,-7.521735,-5.174806,-3.690681,5.446142,-2.601433,-4.587911,-9.193617,2.748270,-5.490404,-6.752451,-3.692882,-1.584725,-0.830563,9.711941,9.824261,8.065683,1.191849,7.266105,5.445562,8.366842,3.142190,-6.022196,8.528952,1.284887,-6.170427,4.555366,3.826182,7.706454,0.792764,-3.919265,6.872691,-7.776458,2.903426,-9.769021,5.928387,-3.642338,-3.430813,-2.605447,8.890607,3.832911,7.310785,-8.950893,-5.340340,-4.264424,-1.204101,0.359256,-9.105637,6.241040,7.313937,-0.940022,0.215682,6.536967,-4.797148,7.221480,8.713007,8.950292,8.138723,4.864527,6.159129,-3.498577,-3.904750,5.001999,8.488816,-6.016882,0.731926,4.140329,2.946956,-4.368013,2.398349,5.878920,-1.846825,0.924523,4.917957,1.150444,0.945475,-5.262652,6.209340,-8.251149,-5.278145,8.094030,-9.756261,5.342234,1.079279,6.164229,3.586250,9.508457,4.243818,-3.522288,8.494640,6.832654,6.538087,-1.980607,8.751538,5.060971,6.140669,7.819249,-2.430789,-8.490688,-6.453651,-2.708465,-9.696659,2.148446,-8.665822,-1.437420,-7.529915,-5.479498,-1.867458,-7.827169,-5.425085,7.715228,8.168461,7.038620,5.954667,0.712418,2.805832,-6.712148,-3.824065,0.617475,7.974064,-8.604911,9.196427,6.680887,-3.845409,0.994802,1.269619,-5.567419,-1.646268,-6.913147,4.281330,6.518404,4.544932,2.001058,-8.536024,7.118529,-3.905421,9.677292,-4.951468,3.201811,-6.903830,5.787052,-2.329578,-6.574317,3.658810,-0.450308,4.160286,5.759068,3.145013,-6.214594,1.960088,0.888318,2.049994,4.592429,6.879104,-8.991891,-9.326697,-5.274541,-7.314321,3.989130,5.179331,-2.473850,7.856356,-2.449630,-7.820053,-3.747311,-8.852529,-7.816981,-4.685858,8.389974,-6.193595,-7.211043,-0.183741,9.341012,8.784784,-5.847656,7.706912,8.381315,2.544909,7.572090,-2.905622,4.619573,-6.979536,1.421768,-6.114626,-1.622959,-2.051401,4.432909,0.395469,6.055478,9.178977,-5.825663,1.744154,3.713358,7.925258,-0.319843,8.704160,-4.564984,0.482936,-8.379078,-6.368133,0.779699,8.764321,8.825258,3.571864,-1.291872,1.426857,4.660903,-5.089939,6.806376,-6.545732,-1.709497,0.034009,7.152503,-8.449078,-4.093584,-1.895290,9.200379,-3.114448,2.728933,-1.776804,-8.971475,-3.450726,-6.504585,3.028125,-9.134245,7.887217,2.243810,5.310813,-7.913104,-6.699558,-0.148117,-5.722677,5.139255,7.125029,-4.630228,-0.737579,7.662922,9.719438,3.443610,2.821008,-7.902116,-1.751147,0.471630,-4.384470,7.563779,4.069445,4.097203,-8.884156,-0.937750,7.417400,8.521301,-0.343999,-6.313633,-0.118685,-2.574549,5.112651,-0.048596,-3.989717,7.685854,5.395347,9.441976,9.880331,-9.335529,6.493389,6.138809,-5.556719,-0.194925,8.007018,-4.535768,0.567588,7.772455,7.163335,-6.293196,7.942364,-8.639188,1.096640,6.040362,-2.342479,-0.015335,7.550314,2.922989,-4.577454,-2.472694,-2.929720,1.293447,1.761316,6.792379,-9.507374,-3.256322,1.183985,2.467276,-8.679826,0.864415,-9.509477,0.829628,3.596729,0.326904,-2.835381,7.351251,-4.610835,-6.175278,9.270813,-4.363484,-6.504574,-8.324419,8.132941,-1.920043,-7.239763,6.961371,7.748033,-4.754836,3.170327,-8.811267,3.928727,-5.770555,-3.181344,9.267499,-7.562682,8.041179,-3.215593,8.925327,7.788845,-3.315020,6.315302,4.488777,-0.925759,-9.626611,7.146818,6.026709,-1.921473,1.095053,0.240522,1.291417,-5.095375,-0.465981,-8.668948,0.687389,5.531591,8.567742,3.316886,2.273226,7.421595,4.112496,-0.257691,2.324410,-6.324420,3.997479,-9.361867,-5.648222,0.052729,7.296674,-1.837444,-6.054283,-7.866177,-6.587247,-0.412067,8.028135,2.842930,-7.166159,-9.277406,2.202083,-0.593809,-8.670551,2.572956,-6.336570,5.702688,-7.475374,-2.252954,8.914380,-4.535912,-7.608183,4.867247,-3.268839,-8.020165,-1.189201,5.867899,2.903992,-7.768379,-1.500595,-5.041667,-0.916677,-3.854852,2.772870,9.453569,-5.148941,4.348968,-0.670008,-4.373545,6.650783,-9.360771,5.659181,7.335342,9.094817,-6.578416,6.728455,-5.270376,-9.882490,-7.972988,3.611566,-8.029495,-1.618765,-4.175113,-0.576459,3.926337,6.413517,8.615878,3.352081,-8.608134,-0.240037,-5.603505,2.273756,-9.677737,-5.784453,-3.477487,-2.711745,5.847990,-1.553194,-8.966782,-5.848820,-8.873844,7.538444,7.449522,1.732805,5.519054,-6.422170,9.380845,2.574546,-9.803395,0.077049,8.043780,7.507488,-7.394700,1.298852,9.785890,-4.488666,5.906815,4.378184,4.418588,-5.952160,4.222473,-6.305711,0.892452,-3.150537,5.438943,-6.628939,4.987962,9.427187,4.838269,-4.573479,3.326004,-2.921029,-1.031795,6.980190,-2.677157,6.716233,-5.145103,6.746390,7.054556,8.168677,8.312112,8.610198,-1.212084,-5.880358,2.047935,-2.734207,2.578837,-7.354630,-4.616416,8.928763,4.111145,-1.027712,8.214208,2.414149,9.848826,6.494299,-4.373692,-4.821034,-5.238993,-4.391805,5.236997,-4.284609,-4.711215,0.125596,-9.154403,4.056121,8.531417,0.005550,9.461803,7.879023,-0.536314,6.017947,4.848576,2.124592,-1.750051,-4.807003,-6.015639,1.632850,7.796547,6.486267,5.184279,1.655079,0.588993,1.572370,-7.210759,3.070750,-2.754800,3.758861,-9.486355,1.483624,7.763597,4.914748,-9.706229,-8.043537,4.321996,7.686816,-6.403108,2.591583,3.296539,7.448203,1.588221,-9.512346,4.168880,7.490967,-6.550334,9.609260,-7.583109,1.246846,8.097314,-9.987626,-9.517528,2.328105,9.208891,-7.511721,-6.817715,-8.284631,-4.569426,5.412464,-1.119035,-7.914680,5.655241,-6.727410,-8.007854,-8.269332,9.907400,-6.131387,-1.670937,0.589461,-9.604995,-6.280230,5.422240,-5.927088,-3.773610,7.828133,-9.345356,9.561521,9.230838,-6.602245,-6.817811,3.964072,8.930067,9.299928,-3.010428,1.147569,-1.579800,0.852021,-1.146655,8.823506,2.804127,-7.143240,-8.893938,8.228459,0.104913,3.042549,-9.324035,-8.883815,-2.520592,7.621529,-5.336814,9.218914,-6.648009,-8.053278,-4.006388,5.373526,-0.663457,-1.116917,-8.465052,9.534103,8.672581,2.507064,4.423833,7.942756,4.805186,-3.758169,-5.214590,-3.743407,-4.210722,9.106786,-9.646619,-6.420308,-7.519864,-0.437680,-6.746759,5.757041,-1.956968,0.483754,-6.031848,-9.534709,1.833024,6.321964,-4.315909,2.756775,-1.272895,-2.665120,7.611928,3.566061,1.443678,-0.623633,6.754665,5.759591,-1.057919,-5.161815,2.757655,-4.113819,6.089613,-7.556561,9.650186,1.058582,5.193264,1.893179,-3.997144,-0.852601,-1.938413,-5.725929,-1.923966,2.250598,-2.503381,7.592289,-8.372997,9.460767,1.746653,-4.594652,3.647142,-4.727561,2.531366,8.208368,1.658837,9.865349,5.754826,4.324794,3.009033,-4.639829,-0.106060,9.099309,-8.528690,5.135732,4.024313,-5.574543,4.210217,1.325062,-4.598511,-4.010227,-8.448521,6.280694,6.825537,-6.701480,-0.586878,2.704486,-0.951697,0.960867,4.295076,9.415045,-2.627909,8.849434,-5.782529,-9.880413,9.224600,-8.940320,-2.009803], dtype = "float64")#candidate|3032|(2560,)|const|float64
bop_3033 = relay.minimum(uop_3024.astype('int64'), relay.reshape(const_3032.astype('int64'), relay.shape_of(uop_3024))) # shape=(2560,)
bop_3036 = relay.minimum(uop_3026.astype('int64'), relay.reshape(const_3032.astype('int64'), relay.shape_of(uop_3026))) # shape=(2560,)
bop_3037 = relay.logical_and(uop_3024.astype('bool'), relay.reshape(call_3016.astype('bool'), relay.shape_of(uop_3024))) # shape=(2560,)
bop_3040 = relay.logical_and(uop_3026.astype('bool'), relay.reshape(call_3017.astype('bool'), relay.shape_of(uop_3026))) # shape=(2560,)
output = relay.Tuple([call_3029,bop_3033,bop_3037,])
output2 = relay.Tuple([call_3030,bop_3036,bop_3040,])
func_3043 = relay.Function([], output)
mod['func_3043'] = func_3043
mod = relay.transform.InferType()(mod)
output = func_3043()
func_3044 = relay.Function([], output)
mutated_mod['func_3044'] = func_3044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_987_call = mod.get_global_var('func_987')
func_988_call = mutated_mod.get_global_var('func_988')
call_3048 = relay.TupleGetItem(func_987_call(), 0)
call_3049 = relay.TupleGetItem(func_988_call(), 0)
func_802_call = mod.get_global_var('func_802')
func_807_call = mutated_mod.get_global_var('func_807')
var_3057 = relay.var("var_3057", dtype = "float64", shape = (180,))#candidate|3057|(180,)|var|float64
call_3056 = relay.TupleGetItem(func_802_call(relay.reshape(var_3057.astype('float64'), [10, 2, 9]), relay.reshape(var_3057.astype('float64'), [10, 2, 9]), relay.reshape(var_3057.astype('float64'), [10, 2, 9]), ), 0)
call_3058 = relay.TupleGetItem(func_807_call(relay.reshape(var_3057.astype('float64'), [10, 2, 9]), relay.reshape(var_3057.astype('float64'), [10, 2, 9]), relay.reshape(var_3057.astype('float64'), [10, 2, 9]), ), 0)
func_9_call = mod.get_global_var('func_9')
func_12_call = mutated_mod.get_global_var('func_12')
var_3074 = relay.var("var_3074", dtype = "float64", shape = (450,))#candidate|3074|(450,)|var|float64
call_3073 = relay.TupleGetItem(func_9_call(relay.reshape(var_3074.astype('float64'), [5, 15, 6])), 0)
call_3075 = relay.TupleGetItem(func_12_call(relay.reshape(var_3074.astype('float64'), [5, 15, 6])), 0)
uop_3076 = relay.sinh(call_3056.astype('float64')) # shape=(10, 2, 9)
uop_3078 = relay.sinh(call_3058.astype('float64')) # shape=(10, 2, 9)
output = relay.Tuple([call_3048,var_3057,call_3073,var_3074,uop_3076,])
output2 = relay.Tuple([call_3049,var_3057,call_3075,var_3074,uop_3078,])
func_3079 = relay.Function([var_3057,var_3074,], output)
mod['func_3079'] = func_3079
mod = relay.transform.InferType()(mod)
var_3080 = relay.var("var_3080", dtype = "float64", shape = (180,))#candidate|3080|(180,)|var|float64
var_3081 = relay.var("var_3081", dtype = "float64", shape = (450,))#candidate|3081|(450,)|var|float64
output = func_3079(var_3080,var_3081,)
func_3082 = relay.Function([var_3080,var_3081,], output)
mutated_mod['func_3082'] = func_3082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_987_call = mod.get_global_var('func_987')
func_988_call = mutated_mod.get_global_var('func_988')
call_3097 = relay.TupleGetItem(func_987_call(), 1)
call_3098 = relay.TupleGetItem(func_988_call(), 1)
func_2410_call = mod.get_global_var('func_2410')
func_2412_call = mutated_mod.get_global_var('func_2412')
call_3120 = relay.TupleGetItem(func_2410_call(), 0)
call_3121 = relay.TupleGetItem(func_2412_call(), 0)
func_1972_call = mod.get_global_var('func_1972')
func_1975_call = mutated_mod.get_global_var('func_1975')
var_3129 = relay.var("var_3129", dtype = "uint32", shape = (112,))#candidate|3129|(112,)|var|uint32
const_3130 = relay.const([-4,4,4,-4,1,7,4,6,-1,-8,-8,4,7,4,-5,-2,-3,7,-8,8,10,-3,5,10,-2,10,3,9,-7,1,9,-2,-10,2,2,5,-5,8,-8,7,-9,9,10,-1,-2,-8,-6,5,-1,-3,-9,7,-9,-4,-5,6,-10,5,-6,7,-1,-10,7,-4,-4,-1,7,9,-5,4,7,-4,-8,7,9,1,8,8,9,-4,-1,8,-5,8,1,9,-2,3,2,-4,-3,-3,-6,-8,5,8,1,7,-4,-5,7,-2,-5,-10,4,-1,9,-10,7,10,2,-9,5,-8,-1,3,-4,-6,10,9,-10,-3,-4,-3,-2,10,-2,-6,5,5,8,-3,-3,-3,-4,6,-3,-10,3,8,8,-9,9,7,-3,1,10,-4,-2,5,9,10,2,1,-5,1,6,-6,-7,-8,-5,2,10,10,2,8,7,-5,9,-4,-2,-10,5,1,8,4,8,-1,-9,2,6,-3,9,-4,2,3,-1,2,8,9,5,-9,9,-1,1,-10,-5,-2,2,3,1,10,8,9,-5,1,-4,-3,10,-1,-9,-10,5,9,7,1,-7,-4,-3,2,-3,-10,-3,10,-6,6,4,-10,-9,6,10,-8,10,-5,-6,5,-9,-8,7,-6,9,-10,8,-1,8,5,-9,-6,-4,6,-7,-9,5,9,-5,6,-6,8,8,-1,9,4,-8,8,1,-9,-4,-7,8,-10,-2,7,-7,-2,-4,-9,8,2,-6,-7,4,-7,8,7,1,-7,8,-9,-10,-9,-3,-9,4,10,-4,6,6,-8,9,-8,-5,-1,2,-7,2,-7,4,9,-9,-5,5,3,-7,6,4,-4,1,-1,7,5,6,4,10,-8,-2,2,-6,-1,-3,9,-10,-8,10,6,-1,-7], dtype = "uint32")#candidate|3130|(336,)|const|uint32
call_3128 = relay.TupleGetItem(func_1972_call(relay.reshape(var_3129.astype('uint32'), [112,]), relay.reshape(const_3130.astype('uint32'), [336,]), ), 1)
call_3131 = relay.TupleGetItem(func_1975_call(relay.reshape(var_3129.astype('uint32'), [112,]), relay.reshape(const_3130.astype('uint32'), [336,]), ), 1)
output = relay.Tuple([call_3097,call_3120,call_3128,var_3129,const_3130,])
output2 = relay.Tuple([call_3098,call_3121,call_3131,var_3129,const_3130,])
func_3137 = relay.Function([var_3129,], output)
mod['func_3137'] = func_3137
mod = relay.transform.InferType()(mod)
var_3138 = relay.var("var_3138", dtype = "uint32", shape = (112,))#candidate|3138|(112,)|var|uint32
output = func_3137(var_3138)
func_3139 = relay.Function([var_3138], output)
mutated_mod['func_3139'] = func_3139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2735_call = mod.get_global_var('func_2735')
func_2736_call = mutated_mod.get_global_var('func_2736')
call_3180 = relay.TupleGetItem(func_2735_call(), 0)
call_3181 = relay.TupleGetItem(func_2736_call(), 0)
output = call_3180
output2 = call_3181
func_3189 = relay.Function([], output)
mod['func_3189'] = func_3189
mod = relay.transform.InferType()(mod)
output = func_3189()
func_3190 = relay.Function([], output)
mutated_mod['func_3190'] = func_3190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_3230 = func_753_call()
call_3231 = func_753_call()
func_2945_call = mod.get_global_var('func_2945')
func_2949_call = mutated_mod.get_global_var('func_2949')
var_3270 = relay.var("var_3270", dtype = "float64", shape = (360,))#candidate|3270|(360,)|var|float64
const_3271 = relay.const([8.566949,3.284943,-5.010481,-6.327501,7.128525,0.115231,6.549438,-8.906642,8.188866,-5.706512,-6.521265,1.909941,-6.108137,4.000720,-2.091803,1.510357,-9.816419,8.475607,-8.449073,-3.853690,8.966496,-3.529083,-4.442956,8.489824,7.463104,3.193841,-9.854326,1.052303,6.024947,-3.888187,6.909170,0.814026,-6.462924,-9.208906,-5.247086,9.219173,1.508214,-8.423964,-0.781038,2.287488,-0.231506,7.274740,-7.780074,1.842917,3.082810,9.614655,0.745741,-3.943174,-0.092801,8.594938,-3.985989,-0.134656,-4.301630,1.082623,1.212624,3.793583,5.188231,-1.170464,0.479713,3.588854,1.610163,1.797211,2.366770,-2.309238,7.282998,7.453237,-0.854336,5.786909,-9.892901,0.292065,1.912015,3.603948], dtype = "float64")#candidate|3271|(72,)|const|float64
call_3269 = relay.TupleGetItem(func_2945_call(relay.reshape(var_3270.astype('float64'), [15, 12, 2]), relay.reshape(const_3271.astype('float64'), [72,]), ), 5)
call_3272 = relay.TupleGetItem(func_2949_call(relay.reshape(var_3270.astype('float64'), [15, 12, 2]), relay.reshape(const_3271.astype('float64'), [72,]), ), 5)
output = relay.Tuple([call_3230,call_3269,var_3270,const_3271,])
output2 = relay.Tuple([call_3231,call_3272,var_3270,const_3271,])
func_3280 = relay.Function([var_3270,], output)
mod['func_3280'] = func_3280
mod = relay.transform.InferType()(mod)
var_3281 = relay.var("var_3281", dtype = "float64", shape = (360,))#candidate|3281|(360,)|var|float64
output = func_3280(var_3281)
func_3282 = relay.Function([var_3281], output)
mutated_mod['func_3282'] = func_3282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_907_call = mod.get_global_var('func_907')
func_908_call = mutated_mod.get_global_var('func_908')
call_3320 = relay.TupleGetItem(func_907_call(), 0)
call_3321 = relay.TupleGetItem(func_908_call(), 0)
func_784_call = mod.get_global_var('func_784')
func_788_call = mutated_mod.get_global_var('func_788')
const_3360 = relay.const(-5, dtype = "uint8")#candidate|3360|()|const|uint8
var_3361 = relay.var("var_3361", dtype = "uint8", shape = (196,))#candidate|3361|(196,)|var|uint8
call_3359 = func_784_call(relay.reshape(const_3360.astype('uint8'), []), relay.reshape(var_3361.astype('uint8'), [7, 2, 14]), )
call_3362 = func_784_call(relay.reshape(const_3360.astype('uint8'), []), relay.reshape(var_3361.astype('uint8'), [7, 2, 14]), )
func_3189_call = mod.get_global_var('func_3189')
func_3190_call = mutated_mod.get_global_var('func_3190')
call_3364 = func_3189_call()
call_3365 = func_3189_call()
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_3372 = relay.TupleGetItem(func_665_call(), 0)
call_3373 = relay.TupleGetItem(func_666_call(), 0)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
var_3375 = relay.var("var_3375", dtype = "float64", shape = (1274,))#candidate|3375|(1274,)|var|float64
call_3374 = relay.TupleGetItem(func_2494_call(relay.reshape(var_3375.astype('float64'), [13, 7, 14])), 1)
call_3376 = relay.TupleGetItem(func_2496_call(relay.reshape(var_3375.astype('float64'), [13, 7, 14])), 1)
func_987_call = mod.get_global_var('func_987')
func_988_call = mutated_mod.get_global_var('func_988')
call_3380 = relay.TupleGetItem(func_987_call(), 0)
call_3381 = relay.TupleGetItem(func_988_call(), 0)
func_1621_call = mod.get_global_var('func_1621')
func_1623_call = mutated_mod.get_global_var('func_1623')
const_3386 = relay.const([[-2.123903],[6.468720],[-8.086596],[7.677769],[-9.608325],[-0.536401],[1.554776],[-7.630880],[-1.633893],[7.660715],[-1.226430],[6.787618],[8.643090],[3.305193],[-6.561301],[0.059811],[9.651043],[0.804884],[-5.300286],[9.748520],[6.195584],[8.056547],[-6.793350],[-9.609609],[-7.690002],[1.984398],[3.778500],[4.952741],[-1.858052],[-1.607181],[-9.970076],[8.479687],[-5.453513],[-8.602117],[0.949206],[8.601943],[0.155994],[-5.448420],[3.659897],[-6.244821],[-7.402691],[-4.115649],[-4.932130],[-1.330689],[2.666480],[4.580914],[-4.691480],[1.120227],[9.027072],[0.035620],[6.908509],[9.588076],[-5.676499],[-4.384855],[2.849451],[4.297139],[1.794595],[5.041811],[9.031699],[-2.317619],[1.579784],[7.401043],[-7.946209],[-9.935896],[-6.495799],[-9.483247],[0.588238],[-8.825522],[1.437711],[3.882323],[-1.572228],[-0.070127],[-7.824066],[0.306675],[9.632964],[-1.954891],[-0.650468],[4.622149],[4.555216],[-9.848291],[8.962882],[8.634792],[6.722278],[-7.391148],[0.894025],[5.630533],[-9.830041],[3.925671],[2.735672],[6.493085],[-5.208660],[3.156046],[2.891782],[4.636816],[9.305446],[-9.967304],[-0.301962],[7.860017],[4.691022],[1.373764],[4.269843],[-1.825560],[-8.835279],[-0.240038],[5.618998],[9.934225],[-0.147199],[-0.416686],[8.087686],[-4.431561],[3.327161],[5.932509],[-8.957019],[0.704918],[9.164712],[-1.639796],[1.480625],[-7.103256],[-2.521566],[-5.400840],[-5.274714],[6.199398],[-8.182848],[-3.774637],[1.123585],[-1.453996],[3.483605],[3.892394],[-0.083665],[-7.748477],[4.027144],[-2.528677],[1.558607],[-9.170835],[-6.415835],[5.399474],[-2.860095],[6.136130],[-4.517595],[-2.034502],[-6.813033],[7.963891],[8.282251],[6.333450],[1.397268],[3.176571],[8.190255],[-7.245948],[-9.161647],[-4.531316],[5.930010],[-6.272578],[6.579046],[-6.127835],[7.423836],[4.607991],[-6.763511],[-3.638748],[2.491929],[4.434637],[9.477269],[4.175714],[9.973888],[2.417469],[6.946881],[-7.666442],[-4.740970],[-0.772940],[-2.804131],[4.493585],[-9.382567],[6.613395],[7.799798],[-0.634274],[5.741445],[-9.348865],[-9.424162],[9.683140],[1.809516],[3.404369]], dtype = "float64")#candidate|3386|(180, 1)|const|float64
call_3385 = relay.TupleGetItem(func_1621_call(relay.reshape(const_3386.astype('float64'), [180,])), 3)
call_3387 = relay.TupleGetItem(func_1623_call(relay.reshape(const_3386.astype('float64'), [180,])), 3)
func_2080_call = mod.get_global_var('func_2080')
func_2081_call = mutated_mod.get_global_var('func_2081')
call_3391 = relay.TupleGetItem(func_2080_call(), 0)
call_3392 = relay.TupleGetItem(func_2081_call(), 0)
func_2794_call = mod.get_global_var('func_2794')
func_2796_call = mutated_mod.get_global_var('func_2796')
call_3397 = relay.TupleGetItem(func_2794_call(), 6)
call_3398 = relay.TupleGetItem(func_2796_call(), 6)
func_872_call = mod.get_global_var('func_872')
func_873_call = mutated_mod.get_global_var('func_873')
call_3400 = relay.TupleGetItem(func_872_call(), 0)
call_3401 = relay.TupleGetItem(func_873_call(), 0)
output = relay.Tuple([call_3320,call_3359,const_3360,var_3361,call_3364,call_3372,call_3374,var_3375,call_3380,call_3385,const_3386,call_3391,call_3397,call_3400,])
output2 = relay.Tuple([call_3321,call_3362,const_3360,var_3361,call_3365,call_3373,call_3376,var_3375,call_3381,call_3387,const_3386,call_3392,call_3398,call_3401,])
func_3403 = relay.Function([var_3361,var_3375,], output)
mod['func_3403'] = func_3403
mod = relay.transform.InferType()(mod)
mutated_mod['func_3403'] = func_3403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3403_call = mutated_mod.get_global_var('func_3403')
var_3405 = relay.var("var_3405", dtype = "uint8", shape = (196,))#candidate|3405|(196,)|var|uint8
var_3406 = relay.var("var_3406", dtype = "float64", shape = (1274,))#candidate|3406|(1274,)|var|float64
call_3404 = func_3403_call(var_3405,var_3406,)
output = call_3404
func_3407 = relay.Function([var_3405,var_3406,], output)
mutated_mod['func_3407'] = func_3407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1127_call = mod.get_global_var('func_1127')
func_1128_call = mutated_mod.get_global_var('func_1128')
call_3439 = relay.TupleGetItem(func_1127_call(), 0)
call_3440 = relay.TupleGetItem(func_1128_call(), 0)
func_2337_call = mod.get_global_var('func_2337')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_3443 = func_2337_call()
call_3444 = func_2337_call()
output = relay.Tuple([call_3439,call_3443,])
output2 = relay.Tuple([call_3440,call_3444,])
func_3452 = relay.Function([], output)
mod['func_3452'] = func_3452
mod = relay.transform.InferType()(mod)
output = func_3452()
func_3453 = relay.Function([], output)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1697_call = mod.get_global_var('func_1697')
func_1699_call = mutated_mod.get_global_var('func_1699')
call_3469 = relay.TupleGetItem(func_1697_call(), 0)
call_3470 = relay.TupleGetItem(func_1699_call(), 0)
func_2319_call = mod.get_global_var('func_2319')
func_2321_call = mutated_mod.get_global_var('func_2321')
call_3471 = relay.TupleGetItem(func_2319_call(), 0)
call_3472 = relay.TupleGetItem(func_2321_call(), 0)
func_872_call = mod.get_global_var('func_872')
func_873_call = mutated_mod.get_global_var('func_873')
call_3482 = relay.TupleGetItem(func_872_call(), 0)
call_3483 = relay.TupleGetItem(func_873_call(), 0)
func_2165_call = mod.get_global_var('func_2165')
func_2167_call = mutated_mod.get_global_var('func_2167')
call_3488 = relay.TupleGetItem(func_2165_call(), 0)
call_3489 = relay.TupleGetItem(func_2167_call(), 0)
output = relay.Tuple([call_3469,call_3471,call_3482,call_3488,])
output2 = relay.Tuple([call_3470,call_3472,call_3483,call_3489,])
func_3495 = relay.Function([], output)
mod['func_3495'] = func_3495
mod = relay.transform.InferType()(mod)
output = func_3495()
func_3496 = relay.Function([], output)
mutated_mod['func_3496'] = func_3496
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3525 = relay.var("var_3525", dtype = "float64", shape = (13, 13, 4))#candidate|3525|(13, 13, 4)|var|float64
var_3526 = relay.var("var_3526", dtype = "float64", shape = (13, 13, 4))#candidate|3526|(13, 13, 4)|var|float64
bop_3527 = relay.less_equal(var_3525.astype('bool'), relay.reshape(var_3526.astype('bool'), relay.shape_of(var_3525))) # shape=(13, 13, 4)
output = bop_3527
output2 = bop_3527
func_3530 = relay.Function([var_3525,var_3526,], output)
mod['func_3530'] = func_3530
mod = relay.transform.InferType()(mod)
var_3531 = relay.var("var_3531", dtype = "float64", shape = (13, 13, 4))#candidate|3531|(13, 13, 4)|var|float64
var_3532 = relay.var("var_3532", dtype = "float64", shape = (13, 13, 4))#candidate|3532|(13, 13, 4)|var|float64
output = func_3530(var_3531,var_3532,)
func_3533 = relay.Function([var_3531,var_3532,], output)
mutated_mod['func_3533'] = func_3533
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3556 = relay.var("var_3556", dtype = "int64", shape = (14, 13, 1))#candidate|3556|(14, 13, 1)|var|int64
var_3557 = relay.var("var_3557", dtype = "int64", shape = (14, 13, 9))#candidate|3557|(14, 13, 9)|var|int64
bop_3558 = relay.logical_xor(var_3556.astype('int64'), var_3557.astype('int64')) # shape=(14, 13, 9)
uop_3561 = relay.cos(var_3556.astype('float64')) # shape=(14, 13, 1)
func_3280_call = mod.get_global_var('func_3280')
func_3282_call = mutated_mod.get_global_var('func_3282')
const_3564 = relay.const([-4.173295,3.305379,-3.712949,8.339108,6.612390,-9.284637,4.671734,-9.832437,6.953157,-2.578820,-2.916169,8.329061,-3.305680,5.817828,7.905320,2.357300,9.130109,5.066079,8.752763,-4.818633,-5.348256,7.683137,-2.451502,8.286062,-8.351137,3.031094,8.173338,2.127504,-2.580529,9.352049,-6.305818,1.231227,5.517946,5.725573,5.776702,2.451443,0.610254,0.060697,2.631030,9.542537,-6.804806,-7.633500,-8.928484,-8.110417,-4.497126,-4.891640,-8.848420,-4.250412,-2.409631,-0.198502,-6.331982,-7.684301,-6.253705,2.211916,-9.322740,7.888383,-2.441958,-5.288328,-4.129712,1.353500,-7.431236,0.388273,3.225750,-0.664843,2.536240,-6.445533,8.348282,9.882596,-6.049611,9.894492,-5.102461,-1.732345,-3.616347,2.138588,7.391328,9.559318,-2.587221,-9.684679,-6.601977,2.588786,6.761111,1.000288,-4.886951,9.831914,-6.032929,8.609038,3.750922,1.914096,-5.051962,-5.005688,9.740901,1.607982,-1.237863,3.711481,0.056600,6.422270,-2.725374,0.107943,2.603832,-2.392037,8.804518,-6.079351,8.054251,-0.232035,-8.137458,2.053792,-3.016792,3.892878,-4.438006,4.233820,-1.499502,-2.396519,-9.918099,6.261278,-4.031330,0.063956,-1.738388,2.859800,9.763387,8.109482,-2.347549,5.787832,-1.912981,-9.808363,5.153031,-3.440170,-3.194553,4.709420,-0.008503,-3.029988,-1.590229,-1.217802,-8.387095,-0.298137,3.932798,4.882649,-9.378761,-0.725168,-8.502965,9.197401,-0.903166,8.581223,-1.610201,5.864553,3.679409,-4.937667,6.327665,-2.697202,-3.135646,4.473961,1.337588,7.123917,5.002817,-0.881494,-6.785401,-6.349373,0.631481,7.353680,-7.182806,-1.655188,0.474091,0.831983,1.217249,-0.992586,-4.675462,0.216322,-5.403083,4.042044,-7.639676,8.274102,9.241726,6.929575,2.462651,-5.107981,-5.625142,-9.067988,7.344514,-7.628344,9.281907,-0.134047,5.483004,1.898160,2.797497,7.729792,-8.911125,-2.069616,-4.347327,-6.882924,7.194585,7.251440,8.393151,6.739157,9.832674,4.798062,-5.199378,-3.686987,1.784923,5.251597,-5.692482,-2.291020,-7.419910,-3.265788,7.759765,-4.323860,-9.575535,-2.745345,5.671484,-7.882362,2.949267,-9.742437,-3.806005,5.224201,-7.198479,-1.905079,-4.299178,-6.069830,7.145622,4.361570,6.529092,6.994459,-1.687948,-0.835569,6.258913,-4.485433,-2.487720,-5.534424,-9.997646,1.390225,1.655597,2.638477,-9.249018,-5.009999,4.930118,-0.335681,2.963063,-2.193575,5.576174,-9.478391,4.250528,-4.519781,3.311225,-0.974544,-3.834926,-0.466208,6.096997,2.905392,3.497255,-4.791504,-8.120881,-8.345653,-7.610295,1.049717,4.856000,4.661191,-3.559002,-7.496915,-5.268821,0.423057,-5.816736,-0.355995,-4.608699,-4.566931,7.080360,-8.445238,2.436389,-7.307752,5.986886,-5.606712,1.203892,6.882668,4.121988,5.725592,5.975483,-6.487833,-3.864086,7.235952,7.136197,6.462098,-6.093258,-5.856800,-5.345878,-3.709168,-2.110175,-6.761265,-8.862222,3.931215,7.629024,4.981315,-2.746974,0.486247,5.207181,3.987467,-9.238940,7.108396,-8.203359,-5.280384,-7.477647,-1.588788,5.193422,-8.689475,-7.112527,6.145199,-2.977377,-6.090854,8.880662,-2.950422,7.662921,8.394771,-8.525231,-8.981942,-2.197464,0.251844,1.376460,0.503197,-3.325246,-9.411767,9.085905,-2.949614,3.306448,-5.824897,-3.670446,4.786428,-0.787233,8.365259,1.542210,4.070811,8.152907,0.204022,-4.456777,7.028216,-1.161262,-4.527650,-5.410938,-9.170804,4.545032,-4.072406,9.196377,0.900836,-5.117337,-2.786203,8.943093,7.486696,-6.721177,2.371117,7.892536,8.841588,2.615891,6.629642,-6.844518,1.271417,7.819491,-1.969835,2.066799,-9.324850,-7.500165,7.266058,2.366658,-3.754974,9.817881,-3.914926], dtype = "float64")#candidate|3564|(360,)|const|float64
call_3563 = relay.TupleGetItem(func_3280_call(relay.reshape(const_3564.astype('float64'), [360,])), 0)
call_3565 = relay.TupleGetItem(func_3282_call(relay.reshape(const_3564.astype('float64'), [360,])), 0)
func_3189_call = mod.get_global_var('func_3189')
func_3190_call = mutated_mod.get_global_var('func_3190')
call_3566 = func_3189_call()
call_3567 = func_3189_call()
bop_3569 = relay.multiply(uop_3561.astype('float64'), relay.reshape(var_3556.astype('float64'), relay.shape_of(uop_3561))) # shape=(14, 13, 1)
output = relay.Tuple([bop_3558,call_3563,const_3564,call_3566,bop_3569,])
output2 = relay.Tuple([bop_3558,call_3565,const_3564,call_3567,bop_3569,])
func_3580 = relay.Function([var_3556,var_3557,], output)
mod['func_3580'] = func_3580
mod = relay.transform.InferType()(mod)
var_3581 = relay.var("var_3581", dtype = "int64", shape = (14, 13, 1))#candidate|3581|(14, 13, 1)|var|int64
var_3582 = relay.var("var_3582", dtype = "int64", shape = (14, 13, 9))#candidate|3582|(14, 13, 9)|var|int64
output = func_3580(var_3581,var_3582,)
func_3583 = relay.Function([var_3581,var_3582,], output)
mutated_mod['func_3583'] = func_3583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_3585 = relay.TupleGetItem(func_2658_call(), 1)
call_3586 = relay.TupleGetItem(func_2660_call(), 1)
output = relay.Tuple([call_3585,])
output2 = relay.Tuple([call_3586,])
func_3596 = relay.Function([], output)
mod['func_3596'] = func_3596
mod = relay.transform.InferType()(mod)
mutated_mod['func_3596'] = func_3596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3596_call = mutated_mod.get_global_var('func_3596')
call_3597 = func_3596_call()
output = call_3597
func_3598 = relay.Function([], output)
mutated_mod['func_3598'] = func_3598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2735_call = mod.get_global_var('func_2735')
func_2736_call = mutated_mod.get_global_var('func_2736')
call_3599 = relay.TupleGetItem(func_2735_call(), 0)
call_3600 = relay.TupleGetItem(func_2736_call(), 0)
output = call_3599
output2 = call_3600
func_3608 = relay.Function([], output)
mod['func_3608'] = func_3608
mod = relay.transform.InferType()(mod)
output = func_3608()
func_3609 = relay.Function([], output)
mutated_mod['func_3609'] = func_3609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mod.get_global_var('func_2410')
func_2412_call = mutated_mod.get_global_var('func_2412')
call_3613 = relay.TupleGetItem(func_2410_call(), 0)
call_3614 = relay.TupleGetItem(func_2412_call(), 0)
func_3079_call = mod.get_global_var('func_3079')
func_3082_call = mutated_mod.get_global_var('func_3082')
var_3645 = relay.var("var_3645", dtype = "float64", shape = (180,))#candidate|3645|(180,)|var|float64
const_3646 = relay.const([-4.441804,4.012744,-3.746964,5.815543,-0.968024,-3.199522,-6.508188,-6.525919,8.607641,5.809846,8.603910,4.984483,-9.379334,-5.276599,8.391354,2.372287,-0.089000,6.508942,4.806023,-6.262212,3.591839,2.313895,8.047449,7.878453,-5.017450,-4.499520,0.455193,1.928546,7.152330,9.496223,3.159192,3.209328,8.764763,-6.734177,8.145525,-3.423276,-6.480106,-1.157471,4.401225,-1.718225,-0.351513,-1.712968,-1.539525,-3.686138,0.177108,2.046727,-4.572170,7.503913,8.213595,5.507309,-9.247947,2.332972,1.922737,0.423197,-0.779006,-2.237564,-7.912776,-1.039622,-5.900533,-6.628602,1.389027,2.907654,-5.420126,1.614659,-5.265992,-7.412207,9.848457,5.241188,-6.842796,5.978267,-7.040003,2.592845,-9.371035,-6.331930,-4.203408,8.625717,-4.181775,-1.492157,3.059741,-5.965824,-7.930199,-5.888411,-0.523291,-6.803650,-0.313840,0.484762,-2.796967,1.021166,9.762724,1.293023,9.629160,5.558604,3.703483,-8.275043,1.438234,7.370053,-2.204625,8.788520,2.287405,4.404329,-7.809570,4.077610,2.987911,4.114050,-6.944970,1.522238,1.115716,1.063351,-7.907419,5.932964,-7.862297,2.652918,1.487273,1.953022,-8.488065,-0.341769,-9.399491,4.932284,8.612653,-6.064095,-2.587439,4.978196,-9.600143,-5.076574,-4.965596,-3.892489,-9.922608,7.920433,8.913399,6.687312,7.249240,-2.358621,4.618970,-1.738105,-0.461563,-5.572935,-4.999343,9.276465,-6.065809,4.731463,1.306429,9.695467,8.919220,5.800833,3.139668,-8.350316,4.537553,-8.241399,1.673626,4.986450,8.774218,-7.792679,8.669234,-1.066473,7.115344,-0.518574,-2.360396,8.755820,4.578575,-7.998327,6.620745,1.275523,9.932796,6.718151,-8.790270,-2.946352,-8.303229,4.524238,-0.798825,8.012648,6.909379,7.469486,7.289031,6.271060,7.106093,2.035582,3.054508,4.728185,1.373876,2.149390,7.405914,6.467688,-5.000470,0.536798,0.186729,-0.925848,9.445046,-2.066929,-9.060002,6.678873,4.031336,-2.242586,8.958968,2.489573,-7.428122,5.238584,-7.278882,0.287825,5.128811,-2.200632,3.101789,-6.839375,-3.572354,6.495887,-1.393608,-6.131338,-8.606829,-8.781004,4.962383,-9.485722,-5.548421,3.208260,-0.998852,4.129916,-8.184406,-0.666227,3.978166,-9.372306,0.146326,-4.699033,-7.833538,5.252375,-1.927248,-5.683945,6.989922,8.743723,-0.914049,8.190352,-0.289704,4.409521,-2.396296,-2.324516,-0.101544,3.079096,9.923697,0.602430,-8.477546,-8.392357,6.404981,-7.213700,2.224962,-1.404662,4.190361,-9.571328,3.847125,-8.441676,-5.001487,0.573146,1.933255,-0.685811,-0.615484,-9.057041,3.704834,4.413874,6.432444,3.650262,-1.830578,9.490550,5.668250,8.027705,2.607218,-6.576010,-8.936516,-2.277811,-2.681223,-4.539970,-4.805632,-1.153935,5.954527,-5.824195,6.752009,6.104647,-2.708568,1.356776,5.136919,-0.559970,-5.058366,-4.554373,-0.821419,-1.299543,2.196977,7.848429,0.419861,6.166102,-6.181875,-9.103152,-9.490611,1.989806,-1.671656,-3.768106,9.876212,-5.154117,-8.147418,-2.375391,3.179600,4.472496,-1.307196,-8.456974,-9.282682,-1.743987,-5.667752,2.002381,6.758705,4.105887,5.492769,4.079021,-1.292567,4.780834,-2.482236,8.519811,-7.858618,-4.520686,9.442480,7.785068,4.346019,-4.797539,-5.302008,-5.927839,-9.089507,9.280939,7.393308,-6.221030,-5.227175,-5.517169,-2.524566,-8.568446,6.254113,5.135491,3.742260,-0.039843,-3.632368,-1.482576,-0.495772,-2.282927,-5.403493,0.680304,-4.619617,0.340836,3.707298,3.675836,3.243266,-1.456499,2.718106,-0.270198,-5.133747,3.967479,6.761858,3.614127,-9.656799,7.009351,2.576653,-1.247079,-1.385852,-5.535349,-0.904771,1.731610,1.448979,-5.620977,0.161336,-2.620601,1.817204,8.856915,2.126662,2.929137,-3.151592,5.924472,7.562308,-8.747232,5.271988,0.026897,-1.769443,-1.933973,-7.397879,-4.007976,0.439943,-7.188651,-3.721910,8.577049,-5.380153,7.067486,2.560680,3.418068,0.292935,0.988806,-3.809496,-5.049095,1.110800,2.219655,0.060147,-4.621797,-7.810712,7.888850,-6.627697,-7.330974,3.678328,0.582921,-7.754401,7.836698,-6.349000,8.259786,4.358457,-3.676783,-9.155602,8.499612,0.140715,-3.552212,-3.942950,0.754915,-4.667509,8.172124,8.504146,1.775959,4.214373,7.397200,1.316156,2.779193,-5.118493,8.461221,2.426912,-3.439390,-1.594514,-2.251558,1.349071,1.635874,8.226618,1.784547,-3.490266,9.240013,-1.515273,4.876363,4.042976,-3.524361,-4.817263,-7.254723,-6.109387,2.218524,3.454390,8.924005,8.874349,-3.034807,-7.595580,4.007482,-0.566809,-6.482524,-3.667538,-3.283794,-6.463698,7.602722,8.746613,-9.038509], dtype = "float64")#candidate|3646|(450,)|const|float64
call_3644 = relay.TupleGetItem(func_3079_call(relay.reshape(var_3645.astype('float64'), [180,]), relay.reshape(const_3646.astype('float64'), [450,]), ), 0)
call_3647 = relay.TupleGetItem(func_3082_call(relay.reshape(var_3645.astype('float64'), [180,]), relay.reshape(const_3646.astype('float64'), [450,]), ), 0)
func_3079_call = mod.get_global_var('func_3079')
func_3082_call = mutated_mod.get_global_var('func_3082')
call_3657 = relay.TupleGetItem(func_3079_call(relay.reshape(var_3645.astype('float64'), [180,]), relay.reshape(const_3646.astype('float64'), [450,]), ), 1)
call_3658 = relay.TupleGetItem(func_3082_call(relay.reshape(var_3645.astype('float64'), [180,]), relay.reshape(const_3646.astype('float64'), [450,]), ), 1)
var_3678 = relay.var("var_3678", dtype = "uint16", shape = (11, 9, 6))#candidate|3678|(11, 9, 6)|var|uint16
bop_3679 = relay.add(call_3644.astype('int8'), relay.reshape(var_3678.astype('int8'), relay.shape_of(call_3644))) # shape=(11, 9, 6)
bop_3682 = relay.add(call_3647.astype('int8'), relay.reshape(var_3678.astype('int8'), relay.shape_of(call_3647))) # shape=(11, 9, 6)
func_2080_call = mod.get_global_var('func_2080')
func_2081_call = mutated_mod.get_global_var('func_2081')
call_3698 = relay.TupleGetItem(func_2080_call(), 0)
call_3699 = relay.TupleGetItem(func_2081_call(), 0)
func_3280_call = mod.get_global_var('func_3280')
func_3282_call = mutated_mod.get_global_var('func_3282')
var_3701 = relay.var("var_3701", dtype = "float64", shape = (360,))#candidate|3701|(360,)|var|float64
call_3700 = relay.TupleGetItem(func_3280_call(relay.reshape(var_3701.astype('float64'), [360,])), 1)
call_3702 = relay.TupleGetItem(func_3282_call(relay.reshape(var_3701.astype('float64'), [360,])), 1)
const_3711 = relay.const([[[-1,-7,-10,4,2,-3],[-2,-4,-5,2,7,4],[-7,6,-4,-5,5,-6],[8,1,7,5,-8,-2],[1,5,-3,-1,-9,-10],[-5,-8,5,-5,1,7],[1,-1,8,-2,-5,-6],[-5,9,-5,7,-3,8],[8,-3,9,-8,9,-9]],[[-3,7,-7,8,-1,8],[-5,-3,1,-8,-7,9],[-10,-8,8,-7,10,9],[-6,-1,-4,-10,5,1],[7,6,-10,-9,2,1],[-5,-1,2,-2,6,7],[4,3,3,9,3,3],[10,6,-1,2,-5,3],[-4,6,-10,-2,-2,-6]],[[-10,4,-10,-7,-3,4],[7,-2,-10,10,9,4],[10,-6,2,7,6,-5],[10,-1,-2,9,-3,-2],[5,7,-9,-5,-8,1],[-2,-3,-10,7,8,-5],[2,-2,6,-10,-7,4],[9,-4,10,-8,-2,1],[9,3,5,-10,3,-4]],[[7,9,10,-7,-3,-5],[-4,5,5,-9,-3,4],[4,5,-5,6,2,5],[1,10,-2,-8,9,4],[9,-2,10,10,-9,9],[5,-7,3,8,3,9],[-2,-2,10,9,-3,-2],[7,5,9,2,-1,3],[-1,9,1,-9,-5,-6]],[[-1,6,3,5,2,-6],[5,-8,-6,-4,4,-3],[3,7,-3,5,-7,-7],[1,-10,5,-5,-3,9],[-4,8,-8,2,-3,9],[2,-1,7,9,2,-10],[-5,-7,7,-10,1,-10],[1,10,1,-9,7,3],[-7,-9,-4,-6,-3,-9]],[[-9,9,9,8,-1,3],[2,-8,3,3,4,9],[-1,6,9,2,6,-7],[3,4,-8,10,10,-8],[-9,-3,3,2,-8,-7],[6,5,5,7,-9,-3],[-10,6,-9,1,5,3],[-7,-1,-3,-9,10,-1],[6,-2,-8,2,8,-8]],[[-2,6,-4,-5,-4,-3],[5,-6,-6,9,-4,8],[5,-2,10,1,8,9],[-4,2,-1,5,-8,10],[-9,-7,1,8,7,-9],[9,-9,7,10,2,-1],[6,-8,8,-10,8,-3],[3,7,1,-7,7,-7],[1,6,-1,8,-3,-4]],[[6,-10,-1,5,2,6],[-7,-4,-8,-9,-10,4],[-3,1,-1,-7,-8,3],[-9,5,-2,5,-5,-6],[-1,4,1,3,10,-10],[-8,8,-5,7,-3,5],[7,-7,-10,5,-9,3],[7,-5,-9,-10,1,4],[10,10,-8,-9,7,-7]],[[-10,-8,-1,2,-4,-7],[-10,-1,4,9,-1,-7],[5,3,-3,-1,-5,5],[-8,6,-2,7,1,-4],[-7,8,3,-6,3,-2],[-2,-1,-2,4,1,-1],[4,-6,-8,-9,7,-3],[-3,3,-8,2,8,8],[-10,-9,4,-6,10,5]],[[-6,2,-2,-6,-4,2],[-3,-2,10,10,-4,-10],[1,-7,10,8,6,9],[-7,-6,-3,-2,5,-7],[6,4,8,-6,-10,9],[-7,-7,-9,5,-3,-6],[1,3,4,10,7,9],[8,2,2,-1,10,-4],[-6,4,9,-8,-10,6]],[[-8,3,10,9,-9,9],[4,-10,8,3,2,5],[-1,-10,3,4,-2,-7],[1,4,8,-3,1,-7],[9,5,9,-1,-5,9],[8,-9,2,-5,-3,7],[2,4,-5,-2,-10,6],[-9,10,-9,-1,-6,-7],[8,3,3,-3,-2,-8]]], dtype = "uint16")#candidate|3711|(11, 9, 6)|const|uint16
bop_3712 = relay.floor_divide(call_3644.astype('float32'), relay.reshape(const_3711.astype('float32'), relay.shape_of(call_3644))) # shape=(11, 9, 6)
bop_3715 = relay.floor_divide(call_3647.astype('float32'), relay.reshape(const_3711.astype('float32'), relay.shape_of(call_3647))) # shape=(11, 9, 6)
func_3280_call = mod.get_global_var('func_3280')
func_3282_call = mutated_mod.get_global_var('func_3282')
call_3720 = relay.TupleGetItem(func_3280_call(relay.reshape(var_3701.astype('float64'), [360,])), 3)
call_3721 = relay.TupleGetItem(func_3282_call(relay.reshape(var_3701.astype('float64'), [360,])), 3)
func_3530_call = mod.get_global_var('func_3530')
func_3533_call = mutated_mod.get_global_var('func_3533')
var_3730 = relay.var("var_3730", dtype = "float64", shape = (676,))#candidate|3730|(676,)|var|float64
call_3729 = func_3530_call(relay.reshape(var_3730.astype('float64'), [13, 13, 4]), relay.reshape(var_3730.astype('float64'), [13, 13, 4]), )
call_3731 = func_3530_call(relay.reshape(var_3730.astype('float64'), [13, 13, 4]), relay.reshape(var_3730.astype('float64'), [13, 13, 4]), )
output = relay.Tuple([call_3613,var_3645,const_3646,call_3657,bop_3679,call_3698,call_3700,var_3701,bop_3712,call_3720,call_3729,var_3730,])
output2 = relay.Tuple([call_3614,var_3645,const_3646,call_3658,bop_3682,call_3699,call_3702,var_3701,bop_3715,call_3721,call_3731,var_3730,])
func_3781 = relay.Function([var_3645,var_3678,var_3701,var_3730,], output)
mod['func_3781'] = func_3781
mod = relay.transform.InferType()(mod)
var_3782 = relay.var("var_3782", dtype = "float64", shape = (180,))#candidate|3782|(180,)|var|float64
var_3783 = relay.var("var_3783", dtype = "uint16", shape = (11, 9, 6))#candidate|3783|(11, 9, 6)|var|uint16
var_3784 = relay.var("var_3784", dtype = "float64", shape = (360,))#candidate|3784|(360,)|var|float64
var_3785 = relay.var("var_3785", dtype = "float64", shape = (676,))#candidate|3785|(676,)|var|float64
output = func_3781(var_3782,var_3783,var_3784,var_3785,)
func_3786 = relay.Function([var_3782,var_3783,var_3784,var_3785,], output)
mutated_mod['func_3786'] = func_3786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_3824 = relay.TupleGetItem(func_665_call(), 0)
call_3825 = relay.TupleGetItem(func_666_call(), 0)
output = call_3824
output2 = call_3825
func_3845 = relay.Function([], output)
mod['func_3845'] = func_3845
mod = relay.transform.InferType()(mod)
output = func_3845()
func_3846 = relay.Function([], output)
mutated_mod['func_3846'] = func_3846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_3887 = relay.TupleGetItem(func_665_call(), 0)
call_3888 = relay.TupleGetItem(func_666_call(), 0)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_3912 = func_753_call()
call_3913 = func_753_call()
func_3608_call = mod.get_global_var('func_3608')
func_3609_call = mutated_mod.get_global_var('func_3609')
call_3922 = func_3608_call()
call_3923 = func_3608_call()
output = relay.Tuple([call_3887,call_3912,call_3922,])
output2 = relay.Tuple([call_3888,call_3913,call_3923,])
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
var_4028 = relay.var("var_4028", dtype = "float64", shape = ())#candidate|4028|()|var|float64
var_4029 = relay.var("var_4029", dtype = "float64", shape = (1, 4, 7))#candidate|4029|(1, 4, 7)|var|float64
bop_4030 = relay.power(var_4028.astype('float64'), var_4029.astype('float64')) # shape=(1, 4, 7)
func_3079_call = mod.get_global_var('func_3079')
func_3082_call = mutated_mod.get_global_var('func_3082')
var_4036 = relay.var("var_4036", dtype = "float64", shape = (180,))#candidate|4036|(180,)|var|float64
var_4037 = relay.var("var_4037", dtype = "float64", shape = (450,))#candidate|4037|(450,)|var|float64
call_4035 = relay.TupleGetItem(func_3079_call(relay.reshape(var_4036.astype('float64'), [180,]), relay.reshape(var_4037.astype('float64'), [450,]), ), 2)
call_4038 = relay.TupleGetItem(func_3082_call(relay.reshape(var_4036.astype('float64'), [180,]), relay.reshape(var_4037.astype('float64'), [450,]), ), 2)
func_1395_call = mod.get_global_var('func_1395')
func_1397_call = mutated_mod.get_global_var('func_1397')
const_4047 = relay.const([[-1.741565,4.026635,5.945807,-4.433301,-6.130178,-1.483954,4.277458,8.654552,9.393735,4.923719,1.142850,4.079021],[0.448682,-2.069658,3.833458,-0.399566,7.545652,-0.929679,6.156300,-8.883893,6.775632,-6.586669,-6.812158,-3.298024],[-2.606921,6.308296,-4.168014,9.436140,8.352902,5.777386,7.591381,5.704981,-8.124025,1.617913,-3.991919,0.637846],[-5.493970,-1.166053,4.305651,0.740158,-6.644553,3.629527,4.016148,-0.952027,-4.663365,7.415261,5.411079,-9.618391],[-7.829988,6.768634,3.555032,0.628543,-3.663364,-0.089271,-4.869759,-7.688916,-5.201431,-7.273423,-0.830410,9.517649],[-8.171729,-0.327623,9.389044,5.168727,-0.765583,-7.331729,3.844004,-3.677205,1.522370,3.772912,-7.667322,-2.719909]], dtype = "float32")#candidate|4047|(6, 12)|const|float32
call_4046 = relay.TupleGetItem(func_1395_call(relay.reshape(const_4047.astype('float32'), [3, 6, 4])), 0)
call_4048 = relay.TupleGetItem(func_1397_call(relay.reshape(const_4047.astype('float32'), [3, 6, 4])), 0)
output = relay.Tuple([bop_4030,call_4035,var_4036,var_4037,call_4046,const_4047,])
output2 = relay.Tuple([bop_4030,call_4038,var_4036,var_4037,call_4048,const_4047,])
func_4053 = relay.Function([var_4028,var_4029,var_4036,var_4037,], output)
mod['func_4053'] = func_4053
mod = relay.transform.InferType()(mod)
var_4054 = relay.var("var_4054", dtype = "float64", shape = ())#candidate|4054|()|var|float64
var_4055 = relay.var("var_4055", dtype = "float64", shape = (1, 4, 7))#candidate|4055|(1, 4, 7)|var|float64
var_4056 = relay.var("var_4056", dtype = "float64", shape = (180,))#candidate|4056|(180,)|var|float64
var_4057 = relay.var("var_4057", dtype = "float64", shape = (450,))#candidate|4057|(450,)|var|float64
output = func_4053(var_4054,var_4055,var_4056,var_4057,)
func_4058 = relay.Function([var_4054,var_4055,var_4056,var_4057,], output)
mutated_mod['func_4058'] = func_4058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1173_call = mod.get_global_var('func_1173')
func_1175_call = mutated_mod.get_global_var('func_1175')
call_4138 = func_1173_call()
call_4139 = func_1173_call()
output = call_4138
output2 = call_4139
func_4159 = relay.Function([], output)
mod['func_4159'] = func_4159
mod = relay.transform.InferType()(mod)
mutated_mod['func_4159'] = func_4159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4159_call = mutated_mod.get_global_var('func_4159')
call_4160 = func_4159_call()
output = call_4160
func_4161 = relay.Function([], output)
mutated_mod['func_4161'] = func_4161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2319_call = mod.get_global_var('func_2319')
func_2321_call = mutated_mod.get_global_var('func_2321')
call_4181 = relay.TupleGetItem(func_2319_call(), 0)
call_4182 = relay.TupleGetItem(func_2321_call(), 0)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_4199 = func_753_call()
call_4200 = func_753_call()
func_1866_call = mod.get_global_var('func_1866')
func_1868_call = mutated_mod.get_global_var('func_1868')
var_4204 = relay.var("var_4204", dtype = "float32", shape = (72,))#candidate|4204|(72,)|var|float32
call_4203 = relay.TupleGetItem(func_1866_call(relay.reshape(var_4204.astype('float32'), [72,])), 0)
call_4205 = relay.TupleGetItem(func_1868_call(relay.reshape(var_4204.astype('float32'), [72,])), 0)
output = relay.Tuple([call_4181,call_4199,call_4203,var_4204,])
output2 = relay.Tuple([call_4182,call_4200,call_4205,var_4204,])
func_4213 = relay.Function([var_4204,], output)
mod['func_4213'] = func_4213
mod = relay.transform.InferType()(mod)
var_4214 = relay.var("var_4214", dtype = "float32", shape = (72,))#candidate|4214|(72,)|var|float32
output = func_4213(var_4214)
func_4215 = relay.Function([var_4214], output)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3452_call = mod.get_global_var('func_3452')
func_3453_call = mutated_mod.get_global_var('func_3453')
call_4219 = relay.TupleGetItem(func_3452_call(), 1)
call_4220 = relay.TupleGetItem(func_3453_call(), 1)
func_3403_call = mod.get_global_var('func_3403')
func_3407_call = mutated_mod.get_global_var('func_3407')
var_4225 = relay.var("var_4225", dtype = "uint8", shape = (196,))#candidate|4225|(196,)|var|uint8
const_4226 = relay.const([-9.948142,3.582824,0.429079,-4.555638,3.892099,6.300324,6.295606,-6.183238,4.183984,2.234220,-5.403394,-7.259569,-2.095051,0.224460,2.328506,-3.490542,4.013533,-7.917110,-6.396020,-6.024628,3.254302,1.510933,-9.437758,-6.317333,0.339147,5.769136,7.531810,-8.821500,8.100007,3.528533,3.815475,-7.298401,8.497408,2.696278,1.604795,0.321988,2.105518,8.460672,2.187998,4.800629,0.842358,-5.896498,0.226657,-1.330296,-9.317842,1.642290,-4.121148,-6.998271,9.062547,6.197145,6.208840,0.848742,1.374008,7.122282,-9.481277,-3.024771,0.368400,-5.923892,8.662007,2.484246,-7.020643,3.260943,-0.087254,-5.886044,4.363668,-9.275149,1.250096,-4.818169,-1.247788,7.585654,-2.147773,8.970210,-2.407777,-4.992660,-8.497419,2.243807,8.502748,3.228722,-6.739114,4.003714,-0.735541,-6.438174,9.560616,-5.053597,-4.976440,-7.572912,0.093650,-4.393665,4.129214,-0.668578,-8.116338,-4.060396,-8.503620,9.081336,2.106950,4.781858,-1.148653,0.740388,-8.802517,-9.887766,5.791705,2.219784,-0.044217,-4.865881,2.216112,2.871796,-0.452063,0.435021,-1.266265,5.634560,9.440308,6.361432,4.227960,0.650198,-7.312222,-2.590046,-9.349252,8.635907,-2.893044,-6.159990,-3.712849,1.849699,1.178347,4.196956,-2.828996,1.560671,7.070251,5.783496,-0.030743,-5.362703,-9.105432,-8.990436,2.272705,5.789050,-3.164574,6.088694,-7.393810,3.525199,0.737359,1.809262,-6.236194,5.244969,3.658162,-2.091933,1.564402,-3.859912,9.763475,-0.778734,-4.925598,-7.629431,6.850377,2.962658,3.440865,3.768070,-4.621580,-1.892430,2.109782,-6.758412,-6.256491,-1.306460,-8.139956,-7.995240,-2.179800,-4.975502,-0.135522,3.229002,-9.790245,2.386596,8.563859,-5.223862,0.937450,-9.442899,-7.895570,3.254856,2.017601,-4.114935,9.393595,-3.940413,2.730664,-1.891735,0.431192,9.664298,9.468714,7.232689,4.226570,-1.351551,-1.651847,9.661153,4.549361,-1.747040,0.956962,-8.338657,8.776172,-9.004117,4.672716,-9.065096,-3.485492,-0.101839,0.982619,-4.501253,3.042770,5.247590,-2.826897,-3.958847,-1.103268,-6.839080,3.876409,-7.168082,3.742846,8.918094,4.612671,-8.482669,8.277509,2.112805,-1.252246,9.191405,-9.967704,-7.347758,-7.200988,9.106302,4.316474,-3.203322,-7.717163,6.773869,5.922515,2.208798,-2.085035,-6.102095,-7.267789,-9.063752,6.438260,8.966364,2.166194,-9.447720,-3.768064,-3.844197,-7.189461,7.887642,1.705907,-6.971032,9.671664,0.571439,1.760515,-4.939735,-4.905937,3.655503,-1.572478,1.134558,-0.693831,5.838314,2.583562,-1.338737,-5.279427,1.036064,-2.293471,-0.982467,8.317427,7.432562,7.904782,-5.441014,5.247958,-1.076532,-9.851398,2.843671,5.451756,-5.794880,-0.855479,-6.236351,-6.145331,-6.050417,-3.921181,-6.566172,-4.200430,-4.364082,8.870938,9.313318,-6.862294,3.772415,-3.159060,1.056609,3.374894,-0.417742,-1.055248,6.057728,-7.307018,7.545899,-1.534356,-5.141765,-3.616873,3.539703,-0.167977,-5.065419,-5.694906,7.709857,-5.158949,-4.021477,-0.749564,9.557591,-7.918562,0.031398,-5.979127,3.140082,5.422537,4.789548,-2.689663,1.154303,-6.632352,-1.836765,9.255222,6.189451,-5.981087,-3.822765,-8.987713,-0.841765,-0.107843,-9.187306,-5.340006,6.027930,0.092128,2.018979,3.355720,-2.297852,-3.144157,-6.298830,6.952965,3.272339,-6.418481,-1.513666,6.359810,6.365818,7.660882,-9.012862,9.093818,5.326368,7.486539,-4.302756,2.044942,-0.893078,7.412637,-7.639994,-2.197624,7.179991,4.580892,0.361965,-9.239798,-3.567057,-4.536888,2.813347,-2.912935,4.993076,-3.746539,1.644866,-0.699118,0.314862,-1.600425,-4.242292,-5.798431,3.570811,-4.142344,-9.056921,9.128118,-5.729947,-8.747018,3.006764,-7.674389,-4.585502,7.415743,-6.746844,0.007060,4.137359,6.619205,-6.048727,3.023808,9.715216,-3.260514,-6.152049,-8.963165,-4.682975,7.590134,-7.638033,-8.001667,-9.726184,-8.068850,6.769394,-9.497028,9.186253,8.368315,3.764799,-0.735216,-7.673497,9.890198,-2.437133,8.403290,-2.174997,9.708383,-3.569216,7.285764,7.041587,9.877820,0.990133,7.774932,-8.370555,-5.277527,-0.950029,-5.425764,8.007325,6.291294,-7.502675,-4.476484,7.530735,9.964585,4.023364,-2.600831,-2.134443,-4.696539,-2.741879,-7.289045,-3.715028,-1.178366,8.214192,1.820120,-5.198859,3.210457,7.705234,2.683822,2.689912,-6.551146,3.584060,0.063474,-2.807902,8.260060,6.781870,2.727648,-7.719318,-5.630164,6.313539,7.573906,4.781019,-7.824365,-3.726894,8.031703,-7.022709,9.412320,6.928501,8.690503,-3.649307,-9.796939,-2.956189,4.592587,1.241801,1.143234,6.463290,7.538282,3.249431,3.049934,1.894737,5.900044,-4.693090,-2.608206,4.938664,9.565685,-3.887272,6.747172,-9.849943,-6.988417,2.526868,-9.608295,-0.942028,4.894927,9.973298,4.951047,8.280505,-9.511582,8.054300,9.733002,-3.325743,-6.734387,-2.812164,6.794560,-2.506705,6.721907,8.821425,-0.678849,9.862930,8.242417,-3.401914,2.286491,3.953598,6.901949,-7.248220,4.906283,-2.037707,-1.641066,-3.872968,3.807205,9.355282,-5.697812,-2.548108,-0.567627,-6.797563,-8.123956,-5.959999,-1.258997,4.249189,5.530887,5.381889,-6.222591,-1.093813,-7.759465,-2.468215,-7.603217,-7.003729,8.003581,3.848944,-9.058809,6.237862,4.024481,0.367715,-1.193981,4.684252,-3.910518,-6.719253,-3.301596,3.199611,9.723397,-7.524650,0.492534,-0.591526,0.593817,-7.524363,7.369689,-6.475504,-2.284177,3.275257,-7.040681,-4.568461,4.125168,7.661946,1.870135,-3.718585,7.721672,-1.557377,-5.067416,8.955135,0.684678,5.676214,6.773775,8.752523,7.596626,-0.701428,9.847118,3.378005,-5.334864,0.983087,5.515946,-1.891253,-4.449848,-6.819898,-0.120136,5.204187,8.537372,-4.123509,-6.019032,-5.585213,-6.912084,-3.448937,3.101830,-3.940025,-4.870028,-7.605930,-6.115113,-9.716452,4.065773,9.008663,-2.208523,6.295656,2.652538,7.613699,4.486814,-9.754821,-2.960205,-2.505780,-5.726447,9.374019,-8.069726,-5.276858,0.414256,6.964933,1.692766,-6.593173,1.437140,-4.491562,6.637026,5.596811,1.594884,8.266525,-5.336226,-3.991991,-7.841243,9.408190,8.652707,3.197711,1.909932,0.246032,7.802615,-6.544247,-6.303724,-6.820261,-2.836179,-2.134198,7.654879,-7.173196,2.008915,-2.014025,-2.100731,-3.937426,9.828552,-3.399076,5.984448,-6.474397,3.553186,7.803890,4.803933,-4.808692,1.315618,7.400280,-7.868461,-6.818565,-1.826371,3.527661,0.160197,-7.986390,-3.939273,0.678594,1.444098,-8.540397,-9.010811,-5.214066,5.008607,-5.766260,0.190374,5.187111,0.042382,-5.419304,-4.461135,-2.934872,4.638141,5.970006,-7.588081,8.309610,-5.531806,-8.723144,-8.980572,-3.485682,8.397514,-2.117982,-5.342209,-9.291471,-1.420961,-9.007239,1.235288,-8.300515,2.939852,-3.122001,-1.948800,5.520669,8.484403,5.575589,-9.022814,-1.144863,-8.439850,4.019005,-8.992857,-0.091607,-6.434120,-6.094435,-7.921400,-8.253887,-4.187179,9.664229,0.917344,0.773729,-0.654360,-7.446949,-7.816343,5.885986,6.320848,9.481396,-7.622923,-7.686900,-7.630705,-7.134274,1.007624,9.819974,6.525359,-4.494004,3.283582,-2.212483,3.223840,6.854029,1.226070,-2.095549,2.230435,-7.889407,-5.866486,-1.020717,5.043253,3.828971,2.869650,-7.873152,5.192002,5.878009,-1.765028,-7.137523,-1.017124,7.126397,-2.758847,7.206951,-2.808264,-4.608022,-5.944950,2.265234,2.570521,7.496642,8.846210,-2.849147,-5.705969,-3.583516,6.302353,-6.785913,-7.789147,1.306317,-3.129447,-3.480958,-2.184835,8.571992,5.527787,0.901478,6.917289,1.556981,-5.911898,1.877708,-8.700529,-5.459202,-2.658917,7.288360,-5.850913,-3.175448,8.073024,6.328431,8.751274,2.600162,-0.297883,1.159425,6.194532,-4.328958,-5.703375,-1.242420,0.814376,-7.480548,-1.558555,-5.407973,-8.749809,8.785210,3.387449,-4.484964,4.135144,4.394254,-1.703235,9.550765,-8.112979,2.313545,4.025665,4.007974,-1.938376,-2.528644,4.350795,-7.134364,5.003009,-7.065413,-1.805651,6.713623,-2.716839,5.013172,-4.399834,-9.485660,7.784345,5.778556,1.659063,6.300043,7.163323,-9.818994,2.843406,-6.619731,-8.634873,4.971847,5.650315,-9.563691,-9.146664,-8.907375,-7.539853,0.268222,6.789023,-9.292248,2.233210,-3.427590,-8.172263,5.792724,0.644032,-1.916596,-0.151579,3.289128,6.885691,4.741015,8.307908,-4.037262,-0.776509,1.421062,-0.097936,0.098062,-4.941558,-8.105785,-1.868648,-8.757798,-7.277945,-7.272051,-8.534929,-9.468689,6.612783,8.643702,-8.968467,3.909896,9.393982,-3.162338,-7.693417,3.009521,3.282990,5.838216,-0.097250,-0.738113,9.094834,5.161797,-8.894870,3.058851,-9.462783,-2.025643,-6.790979,7.632791,8.756587,6.706489,2.898932,-7.674287,4.270294,6.394884,7.975102,-9.964249,-9.494714,-9.149055,7.874119,-5.717248,5.940942,-4.206650,-2.473389,8.683231,7.592907,-3.468695,-0.659040,-2.924581,-5.380748,8.769205,5.732982,-7.996301,9.456512,-4.217424,-2.085333,-3.345085,9.498475,1.389093,2.759018,4.102943,-1.884760,4.576157,-2.395874,-2.807765,2.810531,-1.474947,2.717983,-0.944992,-1.633515,6.682792,-3.011349,-6.968018,7.382424,4.017678,-0.966358,0.225793,-1.509414,5.103045,-8.706393,-9.421306,5.059976,-2.703626,4.153374,-5.063319,9.525069,5.507540,0.250469,-8.026537,7.294490,3.616640,-9.429018,-3.109759,-3.053662,-2.992875,6.065155,-5.528036,7.662296,0.105450,-5.460342,-8.229959,-2.280884,1.044664,7.247490,-5.870500,7.510079,1.018842,-5.706584,8.310428,1.793436,-4.302041,-2.953487,-6.556466,9.792261,-7.071225,0.030762,-7.902786,-0.690883,0.881157,1.085849,6.873243,-5.032101,-5.406772,-1.947523,8.256649,0.018249,1.451812,-9.850496,-6.137563,7.016994,5.908832,9.882842,-1.126702,0.329070,-3.444400,9.362674,-1.735039,-4.199039,1.790344,-2.228955,-4.300788,-1.706219,7.060727,5.874570,-1.683774,-9.465466,8.546178,6.396475,-8.054476,-3.149801,1.954897,-2.680966,0.170510,5.202209,7.951099,0.176416,0.179134,0.760479,-9.465831,-4.610690,-4.890648,9.621593,1.690396,2.480927,4.755194,-2.271416,-5.049505,-3.387435,1.590431,-6.831024,3.440849,-8.150395,8.834429,6.454134,4.075331,-2.715514,3.203517,0.004109,1.828272,-5.524771,-3.752513,3.522907,0.896288,-2.952735,9.158213,6.867245,-6.675629,-7.183539,-9.287175,-9.325623,3.813951,4.927514,-0.117268,3.663530,9.558947,-9.322817,-9.628475,-0.420553,-6.097852,-6.496236,7.833720,-7.830754,-8.599511,0.957921,1.338557,-6.668040,5.997887,6.001960,-0.883670,8.527001,-9.975242,-1.965882,9.781382,-8.565923,5.667842,-2.500461,-3.654930,0.676354,8.006177,4.882680,-8.869534,2.636443,7.497768,1.109682,-5.946058,-0.135404,-3.091525,8.641006,4.069214,7.070030,6.956253,-1.317953,1.784658,-9.273052,-6.299694,3.931855,9.022943,-8.820399,8.608433,-8.917881,-6.491425,-8.459791,0.609069,5.534314,8.776223,-6.739427,-6.058915,-0.706293,-5.624903,-9.668484,5.235803,1.280567,-6.235833,1.028615,5.643188,4.146064,-6.491447,-7.740246,-2.265426,0.671709,4.807000,-8.446549,-3.710602,6.679848,7.665466,3.191928,9.898267,8.054377,3.659172,3.005612,-3.352784,-3.648920,-2.234627,4.412495,-4.357755,-2.899134,-9.418573,0.393438,0.768983,0.259666,-3.535897,4.429272,4.206824,-9.916212,-4.841019,4.006696,-5.771698,3.102205,-8.510916,6.169968,1.021223,-4.570550,-1.468606,-9.998513,-8.850179,-2.127887,1.395198,-6.010253,-0.820839,7.000621,-9.279691,-5.418906,-4.062447,4.533446,-8.444494,-2.304694,-6.701605,4.858329,-1.665463,3.073140,9.204198,-6.502031,3.814164,6.771720,2.464506,-9.848000,0.378043,-9.879877,9.289281,-4.981343,8.280889,1.117393,-3.138374,-8.891549,0.249195,8.058019,-2.600958,1.933544,7.113110,6.494667,4.656509,-2.768852,-5.293992,-1.236418,6.766118,5.033736,9.536684,-9.883255,0.282999,4.848028,-3.078788,5.266522,-6.577463,7.710936,1.560594,-9.480899,-5.965308,2.895546,9.429688,-1.404922,3.965141,6.794281,5.141529,-3.487262,7.834889,7.616631,-1.027774,-3.887207,4.286474,-2.379095,-2.421950,4.129207,-7.747313,-2.509904,-6.955974,-5.329142,-7.272381,9.270334,7.821909,0.502087,6.424358,0.144318,8.524232,-9.313433,8.983328,-3.617452,2.562405,-2.362648,-7.060042,7.860705,-4.142805,-8.418873,-3.774612,-8.082762,9.514361,-1.218857,-2.502878,0.877288,2.719992,-7.258132,-9.900433,-1.603689,-7.802200,7.977004,7.252980,4.234265,-2.157733,4.488602,5.071176,5.836918,5.059976,5.605262,6.580360,5.896118,-0.044791,1.493606,-6.074832,-7.404106,-6.036065,-4.363786,4.085354,9.165290,5.370539,-1.499409,-7.448080,-2.232279,2.350893,1.673345,-5.658906,2.027882,-1.555514,8.994985,-5.328569,7.709956,-4.905327,3.992538,-9.876409,8.838340,1.265460,-5.877786,9.106047,2.467453,3.900050,7.452285,1.238879,-2.442067,5.870223,5.382309,-7.239665,1.378382,-6.174837,-2.574455,9.934200,-6.164491,6.239233,4.308698,1.430958,4.944479,1.890222,-4.524110,0.924005,3.636255,1.319621,-8.154305,2.156547], dtype = "float64")#candidate|4226|(1274,)|const|float64
call_4224 = relay.TupleGetItem(func_3403_call(relay.reshape(var_4225.astype('uint8'), [196,]), relay.reshape(const_4226.astype('float64'), [1274,]), ), 13)
call_4227 = relay.TupleGetItem(func_3407_call(relay.reshape(var_4225.astype('uint8'), [196,]), relay.reshape(const_4226.astype('float64'), [1274,]), ), 13)
uop_4259 = relay.tan(call_4219.astype('float32')) # shape=(450,)
uop_4261 = relay.tan(call_4220.astype('float32')) # shape=(450,)
output = relay.Tuple([call_4224,var_4225,const_4226,uop_4259,])
output2 = relay.Tuple([call_4227,var_4225,const_4226,uop_4261,])
func_4267 = relay.Function([var_4225,], output)
mod['func_4267'] = func_4267
mod = relay.transform.InferType()(mod)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4268 = relay.var("var_4268", dtype = "uint8", shape = (196,))#candidate|4268|(196,)|var|uint8
func_4267_call = mutated_mod.get_global_var('func_4267')
call_4269 = func_4267_call(var_4268)
output = call_4269
func_4270 = relay.Function([var_4268], output)
mutated_mod['func_4270'] = func_4270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1922_call = mod.get_global_var('func_1922')
func_1923_call = mutated_mod.get_global_var('func_1923')
call_4396 = relay.TupleGetItem(func_1922_call(), 0)
call_4397 = relay.TupleGetItem(func_1923_call(), 0)
func_1922_call = mod.get_global_var('func_1922')
func_1923_call = mutated_mod.get_global_var('func_1923')
call_4411 = relay.TupleGetItem(func_1922_call(), 0)
call_4412 = relay.TupleGetItem(func_1923_call(), 0)
func_1972_call = mod.get_global_var('func_1972')
func_1975_call = mutated_mod.get_global_var('func_1975')
var_4419 = relay.var("var_4419", dtype = "uint32", shape = (112,))#candidate|4419|(112,)|var|uint32
const_4420 = relay.const([9,1,5,-7,9,6,-7,-5,-7,2,8,10,7,-7,4,-5,7,4,-8,-8,-9,6,5,-8,6,8,1,2,-2,3,4,-2,-3,-2,-9,10,5,3,7,-4,1,-9,-10,2,-1,-9,-4,5,-9,-10,5,4,6,-2,9,10,-8,4,-1,1,3,6,-10,7,-7,-6,7,-4,9,9,-2,8,9,7,10,1,-7,-5,9,-6,8,-1,-6,-9,-1,-1,-7,-2,-4,-8,6,-10,-10,1,6,6,-1,-9,1,2,-8,6,3,-4,8,1,-3,8,7,-3,-9,7,5,9,-7,2,3,1,-8,2,8,2,6,3,1,8,-4,-2,-2,8,9,5,10,7,-10,5,-4,-9,1,4,9,-4,7,-3,4,-10,-1,-6,-10,10,3,10,-2,-8,3,5,-5,7,4,5,-3,-2,10,7,4,-2,1,-4,2,-8,-7,-7,3,-6,-3,-4,8,3,7,-9,-5,7,4,-3,-5,-1,5,7,-3,-4,6,5,7,1,5,-2,-3,-10,-10,3,-5,10,-2,7,-9,-2,-10,-8,-4,-8,1,3,1,-10,6,8,10,1,-2,7,-1,6,-9,-10,-5,4,-10,-9,10,-2,5,-10,-6,6,1,-1,6,6,4,-8,4,-5,7,-5,-3,5,-7,-4,-6,-4,6,1,-5,-7,3,-7,5,3,-4,-9,9,9,-7,-2,-1,-9,-4,-9,7,7,9,-1,4,6,-6,6,-9,1,8,-10,-10,8,-1,-2,-2,2,-2,8,7,-3,1,8,8,5,-3,-5,-5,-8,9,-7,-8,6,2,-4,-10,-1,10,-10,-1,2,-1,8,1,2,-5,-5,-8,10,7,-8,-5,-7,-10,-3,1,4,4,9,7,7,2,4,-3,1,-10,-6], dtype = "uint32")#candidate|4420|(336,)|const|uint32
call_4418 = relay.TupleGetItem(func_1972_call(relay.reshape(var_4419.astype('uint32'), [112,]), relay.reshape(const_4420.astype('uint32'), [336,]), ), 5)
call_4421 = relay.TupleGetItem(func_1975_call(relay.reshape(var_4419.astype('uint32'), [112,]), relay.reshape(const_4420.astype('uint32'), [336,]), ), 5)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
const_4424 = relay.const([-8.312910,2.090887,-3.349804,4.337417,9.071524,-9.458905,4.078180,6.600024,-8.079332,-7.288025,5.561042,6.534208,6.726920,9.850617,7.353137,-7.049404,-9.628040,3.164573,-7.814314,4.174903,-7.096121,7.762042,-6.913488,3.546483,-4.298648,9.109776,6.166023,-5.692204,6.206174,6.574474,9.758579,-5.800421,8.112768,-6.917740,-4.602972,3.674997,4.567599,6.827586,-1.707815,6.093202,-6.549907,-5.752310,8.209413,-8.329984,-5.295786,6.470772,-8.521368,2.873964,0.287065,5.754161,-9.615304,-3.961101,9.323739,3.651901,-8.553422,5.764770,4.305189,-2.998287,-8.111288,3.800159,-5.151538,-0.397155,4.953675,-8.780409,-1.606129,-0.268110,-0.665061,-2.367049,-5.553826,7.877800,-9.273979,3.463977,-9.440843,-5.217742,6.252351,-1.908296,-1.868956,-1.423406,-4.235497,-4.809696,-9.782329,5.607599,0.341173,-1.501427,-6.821977,-6.356699,-9.434745,-0.240663,8.146354,1.852571,2.033483,-1.619259,7.861387,0.938787,2.546494,-9.978957,-7.642692,3.757374,9.120617,-4.767334,2.830850,1.394778,-2.957942,6.015633,-5.347684,-7.817425,-7.149917,-9.555660,1.065710,5.194807,8.495309,-4.370618,-9.501851,-8.670932,-3.827659,8.363944,8.492097,5.480221,-8.362079,-1.264624,-8.943099,-7.792318,8.290712,-2.608582,-6.910403,-5.966585,9.922931,-0.230692,-9.826714,6.586532,1.223367,-9.180220,1.205304,-0.733457,-0.382658,3.448783,-2.957161,8.522781,-4.191750,-6.903203,-0.152962,-6.470061,-8.614869,5.345809,0.787664,1.979485,4.445216,-3.045079,4.291992,-1.813159,9.919912,-9.945249,-3.375267,9.947590,0.426434,2.632956,-0.107338,0.036495,-7.122282,3.184292,-9.202132,-4.297246,7.948685,-0.307093,-3.020751,-7.845813,-5.738047,9.609056,6.777407,9.976194,-0.520293,-5.339939,8.525514,6.681850,-2.739411,8.246770,8.797659,-9.054889,-5.105432,-3.043958,1.090854,-7.521657,5.708251,-3.988672,7.761217,-3.832615,0.851256,-5.614222,-1.498154,-0.029287,9.046326,3.602363,-8.684207,0.660777,8.309407,5.257766,-8.099115,-7.126608,8.021176,-9.718715,0.259140,-5.637173,2.326291,1.077468,6.900202,-5.449385,9.470968,4.410377,3.664498,3.134672,-0.888636,-1.835434,-6.787933,6.881460,9.120608,-6.790095,-1.682026,8.969493,-2.070696,6.672463,7.062207,-0.027925,-2.571018,-7.850334,-3.333019,-8.860513,-7.916430,4.836646,7.256485,-1.204835,1.561577,0.707763,8.201928,9.857670,3.969207,2.625687,1.515274,-6.104659,-8.135767,3.977527,-4.057026,7.088457,-6.312154,2.856347,9.397992,3.447094,5.078838,-4.251007,5.231902,-4.032911,0.976787,6.835742,5.266893,-0.424645,-2.251701,-0.735256,5.438313,7.970779,-1.212736,6.209324,-0.976107,-7.924086,-9.364868,6.939925,6.566209,-3.941882,2.942879,3.095515,7.045452,-1.026806,4.560305,-2.178698,4.083663,3.191017,9.937165,1.014930,1.430980,2.279613,5.961250,6.455075,-4.626894,7.482448,-4.597133,-8.610331,-7.566211,5.165762,9.402907,-8.273837,-1.307960,-2.458625,-3.664441,1.075837,-5.048764,8.479054,6.633981,-9.094039,9.549281,-0.532405,-0.237206,8.392291,3.052949,-5.517045,5.706641,5.425184,-5.187725,6.981630,-3.242402,-8.927590,0.270623,-0.881824,2.238926,-4.736971,-2.831721,-5.635647,8.389189,1.025663,-8.560659,8.768841,-8.707095,1.624097,-1.835352,6.927495,-1.257195,2.758181,-6.196198,-0.170466,-6.001589,-8.598117,9.632855,5.805002,-2.807493,-3.379191,4.924954,-0.235859,-9.388384,-9.449814,-0.875577,6.781108,-4.102885,-0.855076,-3.704113,-8.962892,7.715688,7.341195,7.789501,4.742205,4.696354,-1.683577,9.767325,-8.199678,1.210329,8.602497,1.833273,-4.957401,1.467782,-9.394779,7.150878,7.978744,3.088951,-9.403036,3.741524,-5.820384,1.318864,3.450009,-6.343447,-5.163829,6.004302,2.911922,8.550951,-4.538970,2.834524,-3.070223,7.808598,8.858607,0.314517,8.297031,-7.710491,8.195241,-7.201024,-9.094426,5.443629,-6.629326,-5.635309,2.649853,4.987547,3.348865,-9.182437,-1.803136,6.970651,-1.195929,1.152063,5.898434,2.429239,7.768933,-4.883529,-8.942093,-5.391028,-5.366889,3.097394,-7.369054,2.026211,9.166599,-6.505152,8.867974,5.058214,-6.950849,2.200077,-3.385163,-0.456701,-9.075757,-7.171703,-6.079428,-9.453624,0.093961,-7.009241,-3.318815,9.014567,3.561157,0.295061,1.075051,-6.506406,3.531424,-6.765819,0.857012,2.746249,1.747233,-3.851365,9.426736,-1.057757,-0.783497,-3.644533,-5.500230,-0.575234,9.861297,-4.619341,7.800300,-9.819079,-9.821137,-7.639248,-4.835280,8.042195,7.683136,6.573886,-8.400677,-9.597311,9.511585,-0.662153,-9.138948,6.670351,-5.041982,1.918308,5.929317,8.837877,-2.972254,2.717594,2.747137,-3.326819,-4.343425,4.931729,5.118463,-8.233088,9.385637,-3.599250,8.327855,6.994253,2.315047,1.953816,2.827146,-4.587733,5.677179,-6.248455,-6.538711,1.758505,-1.671164,-2.194861,-5.317571,-0.342134,7.663105,-7.986399,3.893558,-4.944954,-0.382998,5.971389,-1.531752,7.111212,1.985380,4.453863,-8.809789,-4.173986,3.991398,-2.226847,8.985409,2.534963,1.305801,-1.888257,-0.195928,3.815743,-5.876785,-4.942032,-7.858182,-2.374350,8.370837,3.265619,8.203685,-3.835425,-7.547700,-1.947852,-5.727679,-5.761134,8.845213,-3.680032,-7.784661,-6.618074,-4.016036,4.720289,-0.854867,-7.861405,7.544146,4.607889,4.139965,-9.801148,-3.717282,-9.295933,-1.057792,-9.359027,1.408183,7.819043,-1.011787,-7.864451,-2.255741,8.964344,-5.613800,-7.406952,-6.868576,-0.940506,-9.487451,2.601013,2.147059,7.026767,5.008178,-4.828895,-6.975962,-7.772060,2.814717,8.363112,-4.420434,8.280597,-1.564636,5.830869,8.340157,-1.580162,-0.752737,6.409630,0.309399,9.053947,-0.528989,4.815015,-6.389482,-4.853367,2.833073,2.138551,-6.692712,-6.593485,3.003661,9.455893,3.126685,-4.002971,-8.470954,1.945358,-9.703260,-2.152433,-0.579212,3.941542,1.465509,5.541066,4.592759,-7.389800,8.699306,-4.579128,-7.994994,1.129192,0.723287,3.176234,1.325401,-9.626619,-4.331747,3.408688,-6.927961,7.347602,-4.952958,-8.007869,1.577698,6.177939,0.261007,7.345733,-3.694634,9.207088,-2.795625,0.135684,-9.527103,6.983501,-0.600280,4.476232,9.920397,-4.150392,3.693870,9.782988,9.375650,8.570479,-6.354422,5.016950,-4.503880,9.277554,8.342860,-3.096626,-5.546212,-6.187974,-4.605228,6.708703,-6.676666,6.022264,8.065421,7.410491,-4.743519,3.432887,2.424466,3.834812,-7.120497,2.891497,7.152143,6.983173,4.451222,-0.586268,1.521500,-5.324837,4.155194,-6.175356,-4.635953,2.329658,-3.072883,-5.780598,1.974089,7.288341,-3.562039,-4.962352,5.828044,3.531123,5.181175,-8.095971,0.597561,1.825535,9.946132,7.799599,4.872515,-0.041785,-0.373334,9.091559,-7.461201,2.639283,6.717355,-0.302910,8.876862,-8.166682,3.757577,3.699014,9.302059,3.370020,-1.255934,-6.717501,8.240396,-3.861800,3.499497,-1.205167,-7.690452,-2.856112,5.998046,-3.165216,-6.855761,9.767114,-2.916969,9.234614,1.861863,-2.129739,4.414721,5.689367,7.661929,-5.240076,-3.555045,-2.403080,-0.237681,-0.445993,8.950608,-2.648954,1.624888,9.974145,4.129480,6.323391,8.442890,-0.974553,2.892519,2.772943,9.537255,7.324354,-5.127801,7.772967,1.187485,-2.713295,-9.712302,-3.503404,2.552522,5.006881,-4.125944,3.152723,-7.299369,4.059889,-0.678990,-9.799853,-2.873258,8.774640,8.858208,-1.077730,-2.489466,9.995439,7.352487,0.283036,4.147410,5.004882,8.644418,7.161020,4.922097,6.463551,-2.082853,6.438532,-9.055813,2.730593,7.652856,-6.180578,7.506852,1.889844,3.967960,5.788046,0.985118,4.846324,4.804506,0.600019,6.187984,-0.027402,-3.456121,-3.059967,-2.587692,4.963098,7.582875,-2.528730,8.718294,-9.690957,-7.608642,-8.303195,-5.756308,-8.164788,-8.998770,-2.433650,0.098430,5.985451,8.747801,-9.338259,-1.639794,2.027551,6.704501,-6.078550,7.747834,1.756932,-0.308331,-2.678019,0.268069,-6.769869,-4.302450,6.789477,-8.329640,8.343496,9.150938,1.225555,3.231197,1.400333,-5.912613,-5.735177,-6.366809,4.135048,8.255038,-5.694602,6.253072,-5.206447,3.592951,8.320922,1.458454,4.452847,-8.133357,-5.671614,-6.227709,-0.310017,4.774693,-0.830003,-7.523568,-8.535778,0.151577,8.971329,9.606536,-0.152576,5.475408,-3.040787,7.238274,7.331555,8.032994,1.677169,-8.808518,-2.309508,-3.507600,9.041959,1.271579,-6.506732,-6.694437,7.138703,-3.312678,3.880611,0.985462,-4.602814,6.472284,-3.261148,3.780329,-2.888315,4.775243,0.248011,-7.821769,-8.515264,-9.346854,-4.016113,-8.434819,-5.510228,-8.267516,5.117976,-4.940506,-9.619414,2.372325,-6.964940,-8.191417,-8.837741,3.040354,-8.919081,5.335407,5.115778,1.152235,-7.007829,5.434808,-9.692909,-4.593254,3.252589,3.782251,6.928286,-8.303707,3.109279,-1.473413,-5.335053,5.643809,6.112465,-5.427889,-3.814623,1.907557,7.469694,-0.492092,-6.851719,8.614667,8.970477,0.452880,-0.065570,-3.211529,-0.755662,6.957673,-8.801136,8.698306,7.555322,4.707230,-7.235143,3.959449,5.849597,7.030729,-9.376947,-4.309753,-8.617315,-3.477695,3.097013,-4.130835,-1.822606,0.795754,5.031748,-3.224965,-9.122741,-0.659360,-0.512432,-7.120199,3.177963,2.404066,8.870121,0.817401,4.223262,-9.993873,-6.530970,2.097560,-6.468626,-9.868206,6.598453,0.695954,-6.855713,-3.157484,5.808979,-8.920575,5.520479,-2.884307,9.038361,-2.680190,-6.252658,-8.092279,6.775998,6.716157,-7.745272,5.738662,-1.952056,5.056459,7.740239,-7.201632,-8.897656,0.737854,-1.542525,-8.100078,-4.881230,6.415104,5.634293,5.808063,8.019134,5.363010,-3.296250,3.477743,9.380058,9.754319,7.307347,3.575636,7.880436,7.855117,-8.899049,9.611489,-2.270059,3.056529,-9.391836,-7.843143,6.183252,8.229118,9.547505,5.361343,1.291869,0.621900,-0.657025,4.057753,5.078981,1.524468,-1.230910,-0.417624,2.894836,0.968953,0.604991,7.274164,6.909662,-9.675987,-6.704944,1.880035,0.359690,-0.020345,8.932030,2.743004,-1.224578,-0.678934,0.810650,9.861688,6.356745,8.341744,-2.244888,4.880064,1.546022,-1.618719,5.376406,-7.136234,-6.964833,-8.456210,-8.994632,5.929948,0.271415,4.687246,-7.731601,6.356707,2.060534,-2.044536,-8.906442,1.175138,-5.638459,8.306718,3.746729,-5.592521,-9.102560,1.199503,-0.427508,2.107488,0.647494,-2.863062,8.589062,5.796323,-0.180935,-7.354871,1.762530,0.477571,-1.608856,-4.520743,-9.341502,0.178402,0.260876,9.628500,9.765800,6.171248,9.891599,4.427149,-2.127396,-5.150379,-4.707634,6.524509,-9.870867,9.896449,6.345265,0.518808,-6.229691,-1.562988,5.860171,9.736422,-2.975848,6.186445,9.387613,-1.488827,5.910019,-5.841647,1.959501,-0.624335,-3.673711,-8.387589,2.381885,9.628157,2.917375,1.816445,3.403548,3.850290,-0.020174,-9.416989,6.017055,6.283592,1.320640,7.963411,8.582954,-5.960326,0.943016,1.660015,-7.136866,9.279565,-4.085206,5.771995,7.445988,7.510148,8.073989,6.090791,-7.171634,-8.787901,1.908573,-6.011130,2.784665,-2.566149,-0.888238,3.684749,1.466912,-9.574511,0.731811,5.265848,-2.242064,-3.070659,-7.667170,7.275182,-3.558076,-2.146586,5.278998,-5.340742,-0.399346,5.449004,-0.829211,7.354225,0.714500,1.427850,0.693671,-5.279155,1.829604,-7.323616,-0.237176,-4.177156,6.182949,-9.299871,-2.138837,1.284752,-3.575909,5.561252,8.159192,-5.581561,-4.352093,4.385947,-4.356284,0.877703,1.941226,-6.186336,8.163048,-8.182805,1.050844,1.455367,-3.509401,-8.865315,-6.207552,7.850060,2.507008,-1.139153,-3.402764,5.310432,1.437936,-7.744852,-3.670874,0.262891,-9.835744,-7.359240,-7.534154,5.472409,-4.872208,3.493071,4.592625,-7.632355,-8.013721,-7.702399,2.840014,-3.342432,-7.743613,0.383440,1.256453,5.152727,-5.495385,7.689944,4.851524,5.207767,5.753977,-1.896077,-3.419272,2.541775,-5.757023,3.199279,4.839901,-8.710260,-3.715990,3.022826,-2.977014,9.955946,-4.993021,-6.410340,1.509361,-7.715582,-8.827312,3.719598,8.593809,-7.025421,-6.034589,7.655936,5.332359,-0.391247,4.588157,9.352304,-5.537585,3.463704,1.454903,-9.769904,4.552895,4.347256,-6.721855,-7.896912,9.296791,8.203477,-5.180626,-3.448366,-6.170256,-0.259800,-7.901177,-7.611031,-1.604520,1.084890,7.688783,7.401559,-3.721873,-9.738701,3.217937,8.933975,3.339659,6.318273,8.087352,3.958216,-2.026413,-5.852424,8.546184,1.605060,-9.249606,-1.496841,-9.397237,-5.757989,-6.956268,3.594048,-6.055547,6.505111,8.560860,3.892681,-7.633953,8.290431,-5.122109,4.771768,-5.185332,-0.968123,7.304816,-7.484665,-6.347887,1.917742,2.339751,-0.441408,2.090699,-2.534942,-9.515376,0.517760,-4.107518,9.725732,-9.289242,0.684330,3.045990,7.134818,-2.941228,4.122513,2.365079,7.017231,6.950089,-1.883706,1.541105,-2.423788,-8.582557,-5.221926,-4.099999,-4.708183,-5.305706,0.527469,7.821706,2.557737,-4.575929,-9.325286,6.245664,-0.014491,0.992730,3.235544,6.903370,7.648072,7.394563,1.281065,9.303815,5.003110,9.341085,-7.960493], dtype = "float64")#candidate|4424|(1274,)|const|float64
call_4423 = relay.TupleGetItem(func_2494_call(relay.reshape(const_4424.astype('float64'), [13, 7, 14])), 0)
call_4425 = relay.TupleGetItem(func_2496_call(relay.reshape(const_4424.astype('float64'), [13, 7, 14])), 0)
output = relay.Tuple([call_4396,call_4411,call_4418,var_4419,const_4420,call_4423,const_4424,])
output2 = relay.Tuple([call_4397,call_4412,call_4421,var_4419,const_4420,call_4425,const_4424,])
func_4435 = relay.Function([var_4419,], output)
mod['func_4435'] = func_4435
mod = relay.transform.InferType()(mod)
mutated_mod['func_4435'] = func_4435
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4436 = relay.var("var_4436", dtype = "uint32", shape = (112,))#candidate|4436|(112,)|var|uint32
func_4435_call = mutated_mod.get_global_var('func_4435')
call_4437 = func_4435_call(var_4436)
output = call_4437
func_4438 = relay.Function([var_4436], output)
mutated_mod['func_4438'] = func_4438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_4463 = relay.TupleGetItem(func_1299_call(), 1)
call_4464 = relay.TupleGetItem(func_1300_call(), 1)
uop_4472 = relay.asinh(call_4463.astype('float32')) # shape=(5, 15, 6)
uop_4474 = relay.asinh(call_4464.astype('float32')) # shape=(5, 15, 6)
func_2735_call = mod.get_global_var('func_2735')
func_2736_call = mutated_mod.get_global_var('func_2736')
call_4489 = relay.TupleGetItem(func_2735_call(), 0)
call_4490 = relay.TupleGetItem(func_2736_call(), 0)
uop_4492 = relay.asin(uop_4472.astype('float32')) # shape=(5, 15, 6)
uop_4494 = relay.asin(uop_4474.astype('float32')) # shape=(5, 15, 6)
func_2319_call = mod.get_global_var('func_2319')
func_2321_call = mutated_mod.get_global_var('func_2321')
call_4502 = relay.TupleGetItem(func_2319_call(), 0)
call_4503 = relay.TupleGetItem(func_2321_call(), 0)
func_3043_call = mod.get_global_var('func_3043')
func_3044_call = mutated_mod.get_global_var('func_3044')
call_4509 = relay.TupleGetItem(func_3043_call(), 2)
call_4510 = relay.TupleGetItem(func_3044_call(), 2)
output = relay.Tuple([call_4489,uop_4492,call_4502,call_4509,])
output2 = relay.Tuple([call_4490,uop_4494,call_4503,call_4510,])
func_4515 = relay.Function([], output)
mod['func_4515'] = func_4515
mod = relay.transform.InferType()(mod)
output = func_4515()
func_4516 = relay.Function([], output)
mutated_mod['func_4516'] = func_4516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4515_call = mod.get_global_var('func_4515')
func_4516_call = mutated_mod.get_global_var('func_4516')
call_4574 = relay.TupleGetItem(func_4515_call(), 2)
call_4575 = relay.TupleGetItem(func_4516_call(), 2)
func_2735_call = mod.get_global_var('func_2735')
func_2736_call = mutated_mod.get_global_var('func_2736')
call_4586 = relay.TupleGetItem(func_2735_call(), 0)
call_4587 = relay.TupleGetItem(func_2736_call(), 0)
output = relay.Tuple([call_4574,call_4586,])
output2 = relay.Tuple([call_4575,call_4587,])
func_4591 = relay.Function([], output)
mod['func_4591'] = func_4591
mod = relay.transform.InferType()(mod)
mutated_mod['func_4591'] = func_4591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4591_call = mutated_mod.get_global_var('func_4591')
call_4592 = func_4591_call()
output = call_4592
func_4593 = relay.Function([], output)
mutated_mod['func_4593'] = func_4593
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4628 = relay.var("var_4628", dtype = "uint8", shape = (5, 15, 3))#candidate|4628|(5, 15, 3)|var|uint8
var_4629 = relay.var("var_4629", dtype = "uint8", shape = (5, 15, 3))#candidate|4629|(5, 15, 3)|var|uint8
bop_4630 = relay.left_shift(var_4628.astype('uint8'), relay.reshape(var_4629.astype('uint8'), relay.shape_of(var_4628))) # shape=(5, 15, 3)
func_1299_call = mod.get_global_var('func_1299')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_4633 = relay.TupleGetItem(func_1299_call(), 0)
call_4634 = relay.TupleGetItem(func_1300_call(), 0)
output = relay.Tuple([bop_4630,call_4633,])
output2 = relay.Tuple([bop_4630,call_4634,])
func_4639 = relay.Function([var_4628,var_4629,], output)
mod['func_4639'] = func_4639
mod = relay.transform.InferType()(mod)
var_4640 = relay.var("var_4640", dtype = "uint8", shape = (5, 15, 3))#candidate|4640|(5, 15, 3)|var|uint8
var_4641 = relay.var("var_4641", dtype = "uint8", shape = (5, 15, 3))#candidate|4641|(5, 15, 3)|var|uint8
output = func_4639(var_4640,var_4641,)
func_4642 = relay.Function([var_4640,var_4641,], output)
mutated_mod['func_4642'] = func_4642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_4644 = func_753_call()
call_4645 = func_753_call()
output = call_4644
output2 = call_4645
func_4704 = relay.Function([], output)
mod['func_4704'] = func_4704
mod = relay.transform.InferType()(mod)
output = func_4704()
func_4705 = relay.Function([], output)
mutated_mod['func_4705'] = func_4705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1749_call = mod.get_global_var('func_1749')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_4716 = func_1749_call()
call_4717 = func_1749_call()
func_1596_call = mod.get_global_var('func_1596')
func_1600_call = mutated_mod.get_global_var('func_1600')
const_4719 = relay.const(10, dtype = "uint8")#candidate|4719|()|const|uint8
const_4720 = relay.const([9,-8,10,5,6,-9,3,1,-2,10,-9,4,4,-3,1,5,-6,5,1,-6,-9,8,-8,1,9,10,8,4,-5,-8,-1,-8,-6,-4,2,-3,-4,-2,2,-2,5,-1,-9,-6,-1,1,-5,-10,-4,7,-6,-7,-3,-3,-2,-8,-9,9,3,2,-8,-8,6,6,-4,-5,7,-1,3,-7,-10,-2,-3,7,-6,10,4,9,-5,9,9,-10,-10,-7,4,9,-1,3,4,10,10,8,-5,5,3,9,-10,8,-9,-4,-1,7,6,5,-9,-1,-2,-3,7,9,2,2,9,3,-7,3,9,-1,9,4,1,-6,-6,2,-7,-1,-10,-2,-5,9,3,1,1,7,-9,7,-8,-5,-4,-6,-9,-1,-2,-10,-1,10,-10,-5,6,-2,-3,-7,3,-5,-10,-7,10,7,-4,-2,7,-6,4,9,-3,4,-1,-9,2,1,-7,-10,8,-10,6,7,3,-10,7,8,10,8,-3,-6,-2,-7,-7,5,-6,-10,-8,-4,2,-9,-3,9], dtype = "uint8")#candidate|4720|(196,)|const|uint8
call_4718 = relay.TupleGetItem(func_1596_call(relay.reshape(const_4719.astype('uint8'), []), relay.reshape(const_4720.astype('uint8'), [196,]), ), 5)
call_4721 = relay.TupleGetItem(func_1600_call(relay.reshape(const_4719.astype('uint8'), []), relay.reshape(const_4720.astype('uint8'), [196,]), ), 5)
func_3925_call = mod.get_global_var('func_3925')
func_3927_call = mutated_mod.get_global_var('func_3927')
call_4724 = relay.TupleGetItem(func_3925_call(), 2)
call_4725 = relay.TupleGetItem(func_3927_call(), 2)
func_1866_call = mod.get_global_var('func_1866')
func_1868_call = mutated_mod.get_global_var('func_1868')
const_4729 = relay.const([[8.495674,-2.899809],[6.269700,-5.050338],[-4.801630,7.079470],[-5.197095,5.490053],[-0.587306,-2.565973],[-3.628189,-8.262181],[0.493254,9.245859],[0.285032,-9.507658],[-5.210887,7.001247],[3.756588,-5.046780],[1.886828,-8.499135],[5.713082,0.129896],[-1.967268,-5.287242],[-9.714072,-1.245522],[2.707691,-9.591939],[-1.955518,8.820891],[0.984918,-5.032318],[0.120918,8.116335],[-8.462242,-4.245297],[2.970397,-7.877660],[4.515038,-8.046789],[6.885256,2.900508],[-2.281366,1.568441],[1.431996,7.550293],[1.426945,1.289630],[-4.009177,3.406054],[-6.685017,0.404181],[-9.026363,7.546599],[-7.925612,5.314493],[4.043278,-1.574290],[-9.553708,-9.505917],[9.851530,4.704145],[-0.912256,2.309869],[2.438656,1.840527],[-7.254737,0.148666],[-0.767582,5.183510]], dtype = "float32")#candidate|4729|(36, 2)|const|float32
call_4728 = relay.TupleGetItem(func_1866_call(relay.reshape(const_4729.astype('float32'), [72,])), 2)
call_4730 = relay.TupleGetItem(func_1868_call(relay.reshape(const_4729.astype('float32'), [72,])), 2)
func_1596_call = mod.get_global_var('func_1596')
func_1600_call = mutated_mod.get_global_var('func_1600')
call_4733 = relay.TupleGetItem(func_1596_call(relay.reshape(const_4719.astype('uint8'), []), relay.reshape(call_4718.astype('uint8'), [196,]), ), 3)
call_4734 = relay.TupleGetItem(func_1600_call(relay.reshape(const_4719.astype('uint8'), []), relay.reshape(call_4718.astype('uint8'), [196,]), ), 3)
output = relay.Tuple([call_4716,call_4718,const_4719,const_4720,call_4724,call_4728,const_4729,call_4733,])
output2 = relay.Tuple([call_4717,call_4721,const_4719,const_4720,call_4725,call_4730,const_4729,call_4734,])
func_4735 = relay.Function([], output)
mod['func_4735'] = func_4735
mod = relay.transform.InferType()(mod)
mutated_mod['func_4735'] = func_4735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4735_call = mutated_mod.get_global_var('func_4735')
call_4736 = func_4735_call()
output = call_4736
func_4737 = relay.Function([], output)
mutated_mod['func_4737'] = func_4737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_4741 = relay.TupleGetItem(func_1299_call(), 1)
call_4742 = relay.TupleGetItem(func_1300_call(), 1)
func_1073_call = mod.get_global_var('func_1073')
func_1075_call = mutated_mod.get_global_var('func_1075')
const_4744 = relay.const([-0.483340,1.703313,9.244455,-4.708395,7.643885,-3.859521,7.127201,-3.086100,-7.707629,2.993153,2.641862,4.993525,-8.342309,-1.402129,1.521409,0.984792,5.524836,-4.854332,3.631692,-4.008979,0.091389,5.626674,3.421969,0.517879,5.488970,-2.503953,-0.479236,-3.318698,8.909679,8.057253,2.799351,-1.616749,6.874982,3.060365,1.889426,4.105715,9.932602,7.558436,-9.267730,-5.754563,7.082949,-1.971697,-3.690163,-0.354672,-2.766709,2.904399,9.755313,-6.972228,-6.437173,7.557622,-9.405085,5.535577,5.919782,-7.403972,8.241618,9.250346,-4.395818,7.278564,-3.512594,-7.342521,5.218243,8.243377,3.249340,6.478618,2.684224,1.464331,0.747603,9.083410,-5.213635,-2.443568,-6.254177,-2.113527], dtype = "float64")#candidate|4744|(72,)|const|float64
call_4743 = relay.TupleGetItem(func_1073_call(relay.reshape(const_4744.astype('float64'), [6, 1, 12])), 0)
call_4745 = relay.TupleGetItem(func_1075_call(relay.reshape(const_4744.astype('float64'), [6, 1, 12])), 0)
output = relay.Tuple([call_4741,call_4743,const_4744,])
output2 = relay.Tuple([call_4742,call_4745,const_4744,])
func_4746 = relay.Function([], output)
mod['func_4746'] = func_4746
mod = relay.transform.InferType()(mod)
output = func_4746()
func_4747 = relay.Function([], output)
mutated_mod['func_4747'] = func_4747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3014_call = mod.get_global_var('func_3014')
func_3015_call = mutated_mod.get_global_var('func_3015')
call_4766 = relay.TupleGetItem(func_3014_call(), 0)
call_4767 = relay.TupleGetItem(func_3015_call(), 0)
func_2374_call = mod.get_global_var('func_2374')
func_2378_call = mutated_mod.get_global_var('func_2378')
const_4769 = relay.const([10,-1,-2,10,6,1,-5,-1,9,-6,5,7,-1,4,8,-2,-1,3,-5,1,7,7,8,-4,-9,5,2,9,9,-5,5,5,-2,1,3,9,6,2,4,-9,8,-9,8,-6,-1,5,-8,-4,-1,10,-9,-4,4,8,-3,3,3,-4,9,-1,8,-6,8,-1,-7,3,-9,-2,4,-5,9,8,9,4,-9,8,-10,-8,-8,-7,9,2,8,2,-4,-7,-4,-4,7,3,-2,7,-7,2,3,10,-1,9,4,1,6,-2,5,3,3,-9,-9,1,-1,-1,2,6,4,5,5,-8,6,-3,-6,-4,-4,-6,-9,-7,9,5,-9,-7,6,-1,-9,-4,-8,5,-5,3,-2,-10,-5,1,7,7,9,-1,7,-6,2,9,-10,4,-3,-5,-7,8,-4,-7,-7,8,-10,10,2,2,-9,6,7,-5,8,-9,-4,10,-6,-10,-3,10,9,1,-8,-7,-5,-4,-2,7,8,-6,3,-2,-5,3,-3,1,4,5,-6,7,-5,6,-4,9,8,-4,-3,1,1,6,-8,-7,-1,-4,-7,8,6,9,-8,-1,6,-7,-2,-7,-4,-6,-1,7,-7,9,-4,6,-3,-7,3,-7,-3,-8,-5,-9,-9,3,8,-2,-1,-9,-1,4,-9,-7,8,3,-10,-8,7,6,-4,6,9,9,2,-4,2,-9,8,5,-9,1,1,-6,9,-6,3,5,1,-3,-1,-8,-6,5,-2,-1,-1,2,-4,-10,-2,-5,10,10,-3,6,3,-8,10,2,6,-3,-8,8,-5,2,-7,-6,-7,6,-9,-6,6,-1,9,-8,-9,-1,8,-8,8,-2,-8,-9,3,7,-10,6,10,4,-1,6,5,-8,7,-6,7,-1,4,-10,-7,-1,-1,-5,-2,-10,-3,-4,4,-9,-5,7,3,-7,-7,-4,-3,3,1,4,-7,8,-1,-8,4,5,2,-3,9,2,6,-8,4,-6,-9,10,-7,8,3,-2,-3,8,10,-10,1,2,-1,-10,-4,-10,7,1,-10,-1,-4,2,1,-3,-1,-7,-9,4,1,-5,-10,-8,-8,-10,-7,-1,-3,8,-3,2,-6,-10,10,-2,-8,6,5,7,-2,-2,-8,-1,6,-5,-2,6,-8,10,-10,6,1,-8,-5,-10,3,-7,-4,2,-10,10,-5,-8,3,-10,-10,3,-10,10,5,4,3,-9,-10,7,-9,1,-5,7,-7,-9,5,10,2,-1,-3,6,-4,1,7,5,-6,2,-7,9,7,-3,-1,-6,-7,1,1,6,-4,1,-6,7,-5,5,-9,-8,-2,7,-7,6,1,4,7,-5,-6,2,5,5,-8,5,-3,-2,-5,-10,-3,8,4,-5,-3,-1,9,2,3,-7,8,-8,5,7,2,-4,-4,8,6,10,-4,-10,-4,-8,-8,10,4,-6,-10,1,-10,7,-1,1,-10,9,-4,6,9,-5,-8,-2,4,3,3,-6,-1,7,9,9,1,-3,5,2,-5,1,-3,8,-3,1,-7,6,-1,-9,-3,2,-8,-8,6,9,9,7,-4,-9,-5,10,-9,-1,-1,3,-1,-7,-1,4,-5,9,2,7,-10,-1,-7,9,7,-8,-2,-2,7,-2,6,-6,-8,6,8,3,10,-2,-5,4,-3,-2,-3,-8,6,1,-7,-3,-9,-2,-4,4,9,10,-9,5,5,6,2,2,-3,9,7,2,3,-4,9,1,-6,-1,3,6,3,-10,4,-4,5,7,-5,2,5,5,4,1,4,4,9,-7,-3,-9,1,6,-5,9,-3,8,-7,-1,6,2,3,-9,-7,5,7,7,-7,5,-7,2,7,8,-2,4,3,9,-1,8,-9,8,-9,4,-7,10,3,-3,-3,-4,-2,-4,-6,10,-3,5,-3,6,7,10,6,7,-5,10,3,-2,4,-9,8,8,-10,-1,-8,-7,-6,-1,10,-4,10,10,9,10,9,-2,1,-8,4,3,8,-9,10,1,-7,2,10,-1,-5,10,10,-1,-3,1,-10,-1,8,-7,7,-6,-4,2,-2,2,-5,9,8,8,1,-1,6,1,10,-10,-5,-3,-5,-2,-9,-4,9,-10,5,8,-7,-7,1,-5,-6,-9,-3,2,7,-7,-10,-9,-6,8,6,7,5,6,-4,6,-8,-2,7,-9,2,1,6,-3,-8,4,-6,-9,7,-8,6,10,1,5,10,4,-1,-5,4,9,-10,-8,-6,-1,2,-3,-3,4,-8,4,4,-1,-3,-2,-6,-9,-8,5,5,6,-5,-8,3,-6,1,-1,8,-10,10,-5,4,5,4,3,-7,-9,-9,3,-10,-5,9,-6,9,7,7,-6,-8,3,10,-3,7,9,10,-10,-3,3,-10,-8,-6,-10,6,4,-6,8,-2,-3,5,-5,-8,-9,-9,-2,3,9,2,2,5,4,2,-7,4,-3,6,8,-2,-4,9,-1,-3,-2,10,-4,10,8,9,4,9,-6,7,8,1,10,7,4,4,6,-10,10,-8,9,6,-3,-3,10,3,9,2,-5,3,-3,-5,-10,1,4,8,9,1,9,-2,-1,-8,8,2,-3,5,9,-4,7,-8,-5,6,-2,-5,-10,9,2,4,9,5,8,-5,10,-5,-7,7,1,5,2,-6,8,6,5,2,-3,-6,-9,-7,2,-5,8,2,-9,5,-8,-6,6,-8,9,5,-1,4,-1,8,-6,4,-4,1,3,7,-7,-10,2,-2,-10,-4,7,10,10,3,8,7,-6,-9,6,-2,6,6,10,10,4,-2,3,-8,7,-10,1,-8,8,7,3,9,-1,-9,4,4,5,-8,5,3,9,8,-3,-10,6,-8,-7,8,1,-3,-7,2,3,2,8,-2,1,9,-8,4,6,-1,-9,3,6,-7,-4,-5,-1,-7,-2,-7,8,-6,5,-8,-2,-6,-10,4,-8,9,2,-9,10,-1,4,5,6,-8,-1,-3,-7,-7,1,-3,10,1,7,-4,-7,-1,-5,-2,-8,-1,7,6,-5,1,4,-5,5,8,-7,10,7,4,8,2,-6,-8,7,7,7,-5,9,5,5,7,-6,-5,-6,7,-5,-1,2,-4,-3,10,-6,-1,7,10,-1,-6,-3,4,-8,-5,-1,-3,-6,-3,-5,-9,10,-5,-9,-10,1,-1,-5,-4,-5,-7,7,-9,-5,10,-5,-1,2,-1,1,3,-7,6,7,-8,-1,9,5,9,-10,1,1,-2,10,-3,-7,2,-1,10,10,-10,-3,9,7,-9,10,-4,-2,3,10,-4,4,-2,6,-3,-10,-9,2,-10,-7,-9,6,9,2,3,-10,10,3,-9,4,5,-4,4,2,8,2,8,3,-10,-1,-6,8,-7,9,-9,-7,-6,7,-9,-5,-10,-4,-7,-10,-1,-9,-4,-4,7,-6,-6,-1,3,2,8,-9,-6,-9,-10,-9,-9,-10,5,-3,-7,9,3,-8,9,-8,-9,3,10,8,10,2,4,-2,6,-3,6,10,3,6,8,-7,1,-2,-4,2,6,1,4,10,9,-6,-5,-6,2,10,-8,-7,-1,-1,-7,-6,4,4,-3,1,8,-8,-2,3,6,6,-4,-4,-1,-9,7,5,5,1,-6,9,-10,8,3,7,-9,-5,5,-8,-4,9,2,-5,3,-4,-10,2,-2,-1,-4,-4,1,-7,-9,-7,2,4,-9,-3,-7,-3,2,5,8,8,-6,6,-2,-6,-8,5,8,-5,8,-1,-5,-2,-10,10,2,-9,-10,8,7,-4,6,8,9,-2,1,4,6,2,2,1,10,4,6,-6,5,-2,1,4,-1,-9,-10,8,-8,1,2,5,5,-4,9,-5,-9,-5,5,2,-8,10,-3,-3,9,-2,9,3,-7,4,-6,-2,4,-7,9,-6,-10,4,-5,8,-2,-6,-10,-4,7,-4,-4,2,-6,-8,-8,-1,-1,4,3,-1,-2,7,-8,-8,-8,8,1,-4,8,-1,6,-7,-8,-4,-4,-5,4,8,-4,6,9,5,-3,6,-9,-10,-8,4,9,-6,-7,-9,4,4,4,-9,6,-4,1,10,6,8,8,-9,-4,-10,-5,-3,-4,6,-6,2,6,-1,-5,-10,-3,-4,-2,10,7,4,-6,-10,3,2,-8,-1,10,3,5,6,-4,10,3,-2,7,2,-5,8,6,-7,-4,-1,2,-2,9,-6,-10,1,-4,4,10,-9,-8,-3,8,-9,10,-9,-3,-1,10,-7,4,2,2,-1,1,7,10,-4,-10,3,4,-6,4,3,-7,-2,10,-8,1,-5,3,4,2,2,-2,5,6,6,1,3,10,6,9,-2,-5,-5,-9,-10,6,4,-6,7,-10,-3,10,6,1,-2,8,-1,3,1,-4,4,2,1,6,-1,10,-7,10,-2,9,-3,8,-10,-1,-4,4,6,-5,-6,-6,-9,-3,-1,-4,-5,-7,-10,2,7,-2,8,-10,-2,3,7,-6,-10,-3,-1,-3,9,-5,-6,-10,-10,-5,-10,5,9,-9,9,-3,4,9,-4,-4,-2,-4,7,3,-8,-8,-5,-10,2,1,9,-2,1,-10,2,9,-4,2,9,-1,-6,-7,3,-5,1,6,-1,10,-10,8,6,-5,2,-6,-3,-10,-7,9,-6,-4,-10,4,-1,-3,7,-2,-1,-5,-6,-6,7,9,-2,-5,1,-3,4,-10,2,-7,-7,3,-7,2,1,-4,1,4,10,-2,-1,-1,2,1,7,4,6,-3,-8,-8,-3,7,4,9,-5,4,-6,10,-6,-4,8,8,-5,-6,-8,-4,-7,-6,4,-4,8,4,4,-2,6,5,3,-7,6,3,-10,-6,-10,7,-10,3,-10,2,5,-4,9,5,5,-2,9,-7,-4,5,9,-8,-2,9,-9,8,6,-5,3,8,-3,-1,8,1,-2,6,8,-4,-4,-4,3,-5,6,-5,1,7,4,6,5,-5,-6,2,-2,4,-9,-9,10,3,-3,5,4,7,9,1,5,-4,-5,-2,-1,5,7,-4,7,3,6,5,7,7,7,1,-3,2,-1,9,3,4,7,6,-5,-3,4,-10,-1,-8,-6,10,-4,-1,9,7,-1,1,-6,1,6,2,-3,-3,-1,3,-10,9,7,8,-10,-7,5,9,7,-3,-4,-4,-1,-1,6,2,-7,9,-2,10,-4,-3,7,10,-1,-10,2,-2,-9,-5,-7,2,-9,7,-9,-3,6,-2,9,-10,7,-5,-3,1,-4,-8,3,-4,-2,6,-10,6,7,8,10,-4,7,7,10,2,4,4,2,2,1,-7,4,-6,1,-7,-1,9,2,-5,-2,8,-9,-5,-10,-4,2,-3,-5,7,2,-9,7,-10,2,3,4,-1,-4,3,3,9,9,2,-9,-1,5,6,6,10,1,3,7,-10,2,8,-1,1,-9,3,3,10,2,9,10,-7,7,10,-5,6,2,-5,1,4,-8,-7,-10,9,1,-1,9,5,9,-9,-4,4,-1,10,4,1,10,10,-6,-6,-7,9,-7,10,-10,10,4,-1,-2,6,-4,5,8,7,-6,-1,2,-7,-6,4,-7,-1,10,-5,-2,8,9,-3,-3,-9,3,-2,-3,5,7,7,-6,5,10,-8,-1,10,4,-7,4,-3,-7,4,-5,9,-8,8,-7,-10,2,-9,6,5,3,-6,7,7,-6,3,-2,5,-1,4,3,4,5,10,-3,3,6,-6,-1,-6,4,10,2,-5,-6,4,6,9,-1,3,4,3,-5,1,-10,5,-6,9,10,-4,5,-10,-6,-10,-7,-5,1,1,7,-4,-10,-10,-5,4,-4,-6,6,8,6,-1,3,4,-3,1,-8,6,3,-2,-6,-6,9,-9,-9,-9,7,7,-7,5,5,-2,1,1,-6,4,1,4,3,7,2,-6,5,2,-4,3,-3,2,-1,-7,8,-10,-3,-1,8,10,-1,1,-10,9,10,-5,5,6,-2,2,4,9,6,6,5,6,-4,3,9,-8,-1,9,-10,-1,-8,2,-7,-3,-8,-9,-7,-10,-1,3,-2,9,5,9,-5,-8,3,6,1,-3,8,-4,8,-4,-7,-10,-1,4,9,1,-4,-6,1,7,1,10,5,-2,8,-3,-6,-5,6,-3,3,-8,5,3,7,-5,-1,8,9,-8,-10,3,8,1,7,8,7,6,1,7,9,-8,7,8,-8,4,-9,-3,4,10,7,-9,3,6,7,4,5,8,-10,1,-3,5,1,1,-2,-7,9,5,3,10,7,6,5,-6,-10,-2,-4,-9,5,-2,-2,-7,-7,5,-4,-10,8,-2,1,10,5,-6,-3,5,4,-6,-6,-9,3,-3,-10,7,2,-3,-7,6,-8,-2,7,8,5,-10,-7,4,-5,-9,3,-3,5,-7,2,8,-6,-9,-8,-6,3,3,-9,1,7,8,-6,-4,10,5,7,-10,-6,5,9,6,-1,1,-10,-3,2,7,-4,-1,2,-4,1,-1,-6,10,2,-9,-9,-3,3,-5,7,3,3,-6,3,-6,-8,1,5,-1,-9,2,-9,6,8,8,-3,7,-6,3,-4,4,-5,-6,-6,9,-7,5,3,9,5,9,8,-4,-10,4,5,8,10,-10,2,4,-10,5,-10,-7,2,3,-3,-4,5,8,3,7,1,4,9,-3,6,-10,-4,1,2,-6,2,-7,8,-4,5,-6,1,10,-7,6,-2,-2,-5,10,9,-2,8,8,9,6,-5,8,4,5,2,-9,-2,-1,-5,4,-9,-7,-8,-2,8,8,-2,-1,-8,-10,-2,5,9,10,-6,-10,-1,-1,-3,-5,-1,-6,1,9,-8,10,-9,3,-10,4,7,1,2,-6,-5,7,4,-8,5,-6,8,2,-10,5,-7,-8,-4], dtype = "int16")#candidate|4769|(2560,)|const|int16
call_4768 = relay.TupleGetItem(func_2374_call(relay.reshape(const_4769.astype('int16'), [16, 10, 16]), relay.reshape(const_4769.astype('int16'), [16, 10, 16]), ), 0)
call_4770 = relay.TupleGetItem(func_2378_call(relay.reshape(const_4769.astype('int16'), [16, 10, 16]), relay.reshape(const_4769.astype('int16'), [16, 10, 16]), ), 0)
func_4213_call = mod.get_global_var('func_4213')
func_4215_call = mutated_mod.get_global_var('func_4215')
const_4788 = relay.const([-7.149140,-2.548180,-9.689328,-3.629457,7.503200,-1.296207,-7.707064,-8.364860,-5.349307,-3.061490,-7.646861,-9.300151,5.091991,-9.784568,3.274671,-7.715487,-8.432091,-5.515796,2.101357,3.497537,5.572382,8.371293,-1.278860,-9.111601,-8.171539,5.734221,-1.083650,-9.471674,-2.177440,-0.764702,-6.131481,7.264808,-6.997321,8.342877,0.544703,-1.019242,-7.639164,-0.055556,3.390209,5.646667,-7.826425,-1.342741,-5.347150,-5.124453,7.201455,-2.957386,1.926031,1.881533,-9.084664,7.252172,6.354231,-4.682002,-0.585850,-7.204384,6.519183,6.817690,-5.646830,6.284305,-5.408088,9.045792,-5.823772,7.066559,1.446843,1.507803,-1.540640,0.631394,-5.446646,6.412344,9.333216,4.045762,-6.492033,-7.078066], dtype = "float32")#candidate|4788|(72,)|const|float32
call_4787 = relay.TupleGetItem(func_4213_call(relay.reshape(const_4788.astype('float32'), [72,])), 1)
call_4789 = relay.TupleGetItem(func_4215_call(relay.reshape(const_4788.astype('float32'), [72,])), 1)
func_4267_call = mod.get_global_var('func_4267')
func_4270_call = mutated_mod.get_global_var('func_4270')
var_4807 = relay.var("var_4807", dtype = "uint8", shape = (196,))#candidate|4807|(196,)|var|uint8
call_4806 = relay.TupleGetItem(func_4267_call(relay.reshape(var_4807.astype('uint8'), [196,])), 2)
call_4808 = relay.TupleGetItem(func_4270_call(relay.reshape(var_4807.astype('uint8'), [196,])), 2)
output = relay.Tuple([call_4766,call_4768,const_4769,call_4787,const_4788,call_4806,var_4807,])
output2 = relay.Tuple([call_4767,call_4770,const_4769,call_4789,const_4788,call_4808,var_4807,])
func_4811 = relay.Function([var_4807,], output)
mod['func_4811'] = func_4811
mod = relay.transform.InferType()(mod)
mutated_mod['func_4811'] = func_4811
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4812 = relay.var("var_4812", dtype = "uint8", shape = (196,))#candidate|4812|(196,)|var|uint8
func_4811_call = mutated_mod.get_global_var('func_4811')
call_4813 = func_4811_call(var_4812)
output = call_4813
func_4814 = relay.Function([var_4812], output)
mutated_mod['func_4814'] = func_4814
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4850 = relay.var("var_4850", dtype = "float32", shape = (5, 2, 16))#candidate|4850|(5, 2, 16)|var|float32
uop_4851 = relay.exp(var_4850.astype('float32')) # shape=(5, 2, 16)
uop_4853 = relay.atan(uop_4851.astype('float32')) # shape=(5, 2, 16)
func_4515_call = mod.get_global_var('func_4515')
func_4516_call = mutated_mod.get_global_var('func_4516')
call_4855 = relay.TupleGetItem(func_4515_call(), 1)
call_4856 = relay.TupleGetItem(func_4516_call(), 1)
bop_4872 = relay.not_equal(uop_4851.astype('bool'), relay.reshape(uop_4853.astype('bool'), relay.shape_of(uop_4851))) # shape=(5, 2, 16)
output = relay.Tuple([call_4855,bop_4872,])
output2 = relay.Tuple([call_4856,bop_4872,])
func_4877 = relay.Function([var_4850,], output)
mod['func_4877'] = func_4877
mod = relay.transform.InferType()(mod)
var_4878 = relay.var("var_4878", dtype = "float32", shape = (5, 2, 16))#candidate|4878|(5, 2, 16)|var|float32
output = func_4877(var_4878)
func_4879 = relay.Function([var_4878], output)
mutated_mod['func_4879'] = func_4879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2337_call = mod.get_global_var('func_2337')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_4910 = func_2337_call()
call_4911 = func_2337_call()
output = relay.Tuple([call_4910,])
output2 = relay.Tuple([call_4911,])
func_4913 = relay.Function([], output)
mod['func_4913'] = func_4913
mod = relay.transform.InferType()(mod)
output = func_4913()
func_4914 = relay.Function([], output)
mutated_mod['func_4914'] = func_4914
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5031 = relay.var("var_5031", dtype = "float64", shape = (4, 15, 10))#candidate|5031|(4, 15, 10)|var|float64
uop_5032 = relay.cosh(var_5031.astype('float64')) # shape=(4, 15, 10)
output = relay.Tuple([uop_5032,])
output2 = relay.Tuple([uop_5032,])
func_5037 = relay.Function([var_5031,], output)
mod['func_5037'] = func_5037
mod = relay.transform.InferType()(mod)
mutated_mod['func_5037'] = func_5037
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5038 = relay.var("var_5038", dtype = "float64", shape = (4, 15, 10))#candidate|5038|(4, 15, 10)|var|float64
func_5037_call = mutated_mod.get_global_var('func_5037')
call_5039 = func_5037_call(var_5038)
output = call_5039
func_5040 = relay.Function([var_5038], output)
mutated_mod['func_5040'] = func_5040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_5049 = relay.TupleGetItem(func_665_call(), 0)
call_5050 = relay.TupleGetItem(func_666_call(), 0)
func_753_call = mod.get_global_var('func_753')
func_754_call = mutated_mod.get_global_var('func_754')
call_5053 = func_753_call()
call_5054 = func_753_call()
func_4515_call = mod.get_global_var('func_4515')
func_4516_call = mutated_mod.get_global_var('func_4516')
call_5057 = relay.TupleGetItem(func_4515_call(), 1)
call_5058 = relay.TupleGetItem(func_4516_call(), 1)
func_3403_call = mod.get_global_var('func_3403')
func_3407_call = mutated_mod.get_global_var('func_3407')
var_5068 = relay.var("var_5068", dtype = "uint8", shape = (196,))#candidate|5068|(196,)|var|uint8
const_5069 = relay.const([[-2.994396,-0.386598,5.512075,9.063198,-3.323202,-2.945100,-3.357726,-9.561915,-9.882077,-4.106549,6.942392,-1.977848,5.986298,-5.466763,-9.122718,-4.329710,-3.751510,2.570532,8.083036,6.761807,5.511047,-8.801609,6.934035,-5.508030,-1.575781,-3.284740,6.198263,3.674087,-7.987302,3.614450,3.318193,7.173182,-6.623408,2.380412,4.587536,-6.763847,2.399091,-3.484700,7.747924,-3.696874,0.128757,5.502862,1.933018,8.332395,-7.287546,-2.598667,1.919283,6.675745,0.701136,2.844466,4.620962,8.454775,-8.446557,1.941943,4.305730,6.185639,-9.740168,1.882402,0.737143,0.776304,9.526760,6.851704,1.773766,7.345186,-3.891856,1.665402,-2.831847,-4.853431,-5.644248,-6.509625,0.615714,-0.891198,-4.080139,4.732787,3.596925,-4.963601,0.608543,1.402220,-0.071791,3.414362,8.635254,0.869411,7.478322,-7.564531,4.230746,4.996785,-2.383827,9.557110,-3.342544,6.749491,0.446301,-3.226174,9.725572,-4.351225,-3.981974,-4.887153,-2.712368,6.631324,7.575107,-4.782069,-6.169459,6.351227,3.070085,-2.717980,-7.862194,7.902405,4.199938,-9.295844,7.632296,-4.671921,-1.801150,9.873358,-9.712807,-8.417320,-2.885978,9.748310,4.812873,-6.555516,5.297797,-5.923800,-6.185489,0.584311,4.647743,-4.500230,-2.825047,3.072900,-4.019011,-1.537073,4.043942,-8.642049,7.418447,4.294300,8.553174,7.036187,-7.357650,-9.206387,-5.607049,-4.931294,5.913937,-8.403734,1.150514,-1.698583,5.581327,1.666330,2.381552,-1.434880,3.264282,3.625106,3.362224,2.231095,-5.500749,-5.962053,5.861872,3.410484,-1.957579,5.728977,6.527898,9.857296,-0.087293,6.852479,-7.565647,-8.645329,3.400764,-4.217005,-8.786182,-3.817541,8.752465,2.617915,6.371118,0.824052,3.161280,-0.094821,-7.652112,6.644838,-2.094246,1.974744,-7.217951,-9.217299,1.305211,2.116281,-3.867128,1.323808,-6.476959,-4.343820,2.205103,5.068396,-5.859786,5.932514,6.530613,3.490438,0.236356,6.868158,-4.017727,-7.596428,-1.074382,-1.546327,7.392658,7.664142,-1.018589,-5.128500,7.947334,-3.386329,7.395755,7.885530,-5.371284,-9.263964,4.004600,-5.251230,9.564306,3.456435,-2.715924,-7.786329,1.052110,3.853630,4.794968,5.253523,-6.327172,0.369923,5.950988,-7.643133,6.749712,-5.303465,-9.746283,7.944726,9.164716,-9.551984,-1.437304,4.699254,-6.653244,2.336143,-7.606460,-2.857877,5.626404,-4.280253,-7.759054,-6.677362,5.372433,-1.954604,3.888188,5.224175,5.227595,-3.887106,-9.178217,0.329506,0.506255,6.770091,-8.586928,-3.824706,5.144290,-4.181264,6.819604,4.258364,5.826838,6.285070,6.086926,5.814361,-1.781066,-9.151371,-2.079301,7.665303,3.955485,5.191473,-4.298540,3.357409,9.792983,-4.482362,-9.530677,8.225137,9.981719,6.335248,-6.128760,5.315058,-9.298531,2.444671,-8.767396,-6.652751,0.980297,8.964463,6.539944,2.388191,-9.092357,-1.607491,-3.493408,9.510849,-1.388831,-5.554469,5.101604,5.706414,-7.617292,-6.804427,2.856225,-0.243642,5.279474,-3.289884,-7.026560,9.205262,0.272572,3.963130,6.505512,-6.079557,8.523161,-6.666680,-6.221054,1.407240,5.057011,1.560687,-2.115097,9.906427,7.934666,7.509176,-2.151049,1.822267,-1.751369,3.330747,6.707168,0.846707,-0.826297,3.483218,8.733760,5.625120,6.484027,1.015426,-2.847201,7.272742,-8.048250,9.606301,4.415630,4.300569,-0.426855,5.979902,-2.597558,-1.337337,8.019114,3.391985,-5.893678,6.420353,-0.064507,-4.652858,5.399834,-2.784029,-3.893763,-1.934534,-5.393066,5.015181,-2.960238,-3.125232,3.920886,-7.146911,1.571799,7.061376,-3.908995,0.305403,1.188915,-9.980051,9.123062,-8.485468,-8.480303,1.200111,-7.863906,1.049278,7.181794,0.647366,7.209755,0.842318,-6.297588,-7.665114,7.503496,2.548446,1.265552,-0.371351,-5.007813,-9.728464,7.563908,-5.251233,-4.520034,3.985730,4.224401,-2.423977,-1.026656,6.443193,-9.802729,1.217774,0.498708,-2.133771,-8.135147,7.084416,-0.479272,-1.426561,4.253596,7.772768,-7.036871,-8.469549,-1.425176,-3.947522,-4.264279,9.619220,-6.947338,7.382304,5.575912,-4.142996,-4.918591,-5.158112,-7.255564,-2.073163,8.686712,9.908772,-7.565532,-4.982382,2.075570,5.216649,-5.198068,-7.451293,-8.280259,1.522057,-2.320406,4.269221,3.721000,2.318517,-9.651618,-4.661943,4.016138,-2.853357,3.004704,-2.603021,2.210660,-2.385533,-6.771979,-8.910421,-3.699241,-4.609862,-9.361392,4.401626,-0.161671,8.232733,0.410237,-8.576705,5.133866,-0.105487,2.978325,3.943060,7.094769,8.063592,7.210557,-4.260598,8.005040,-6.330044,-7.428567,2.509095,-7.069792,-2.758626,-1.249932,-9.360225,2.349756,-4.848969,-7.675265,0.321394,-7.887519,8.928968,2.668163,7.945177,4.537687,-6.947921,-0.234014,-6.704791,-2.206267,-7.912713,4.419798,-8.772058,3.191154,-1.294945,4.103228,3.174143,-1.089029,4.264107,-3.453628,-8.089586,-9.833025,-7.879018,-8.433161,8.930099,4.650621,-7.365413,-1.869651,1.240823,3.032243,1.062603,1.334086,-6.852379,-6.386142,4.760779,5.480512,-0.190572,-0.919366,-1.339775,2.819136,1.938698,0.337737,7.435925,8.816325,1.238312,-7.347082,1.836343,-5.209378,3.411830,2.868581,4.364485,-1.429848,-0.015463,-1.444695,-9.037750,-0.703878,-0.717918,1.829427,0.565731,-7.959647,3.387508,-2.972663,2.991231,4.518794,2.308913,7.276666,8.646035,-5.258218,8.143703,-3.007018,-4.207441,6.463385,-6.550935,-8.599141,9.477609,-6.333663,-6.513764,5.288687,2.927269,-1.012099,1.942655,-8.505476,-0.314718,-1.480675,4.274195,9.168617,2.722501,6.292732,6.487139,-4.025392,-8.824311,9.029824,3.525445,-1.469207,0.492971,3.417269,8.684919,5.788160,-4.486303,5.246415,-8.255347,5.240646,9.392198,5.442718,-9.723832,-9.223609,0.402624,1.228578,-7.246862,1.224328,3.623537,1.639932,-0.321249,-9.449160,-0.756254,9.176808,-0.210521,1.390989,8.285710,-9.439895,-2.237808,-8.675418,-9.008231,-1.227378,-3.235951,4.169309,-6.701177,-4.936037,0.504875,3.575466,-5.989256,1.546303,9.537200,-0.846410,1.706224,-1.310121,5.601294,9.678658,8.360480,6.817119,-4.027302,2.474006,4.090422,6.435487,-9.470517,-9.015947,3.589266,0.045921,-4.925934,3.498683,-8.424009,1.305237,4.208307,5.427424,-1.845291,-0.913150,8.311878,4.923051,4.110696,-7.991024,5.800050,-7.006385,-2.912269,1.413094,9.730630,-3.009959,7.480878,-2.922564,5.029854,5.682292,-6.339297,-9.406079,4.480219,-0.353247,-5.652543,-1.144353,2.298508,0.624450,-7.983061,3.581221,6.288900,9.493597,9.144150,1.960097,8.074162,2.774729,-9.145940,-0.285155,3.299134,-6.550210,5.514862,-7.989971,7.996569,-0.960934,-1.456492,-9.679981,4.818330,-6.828963,7.605525,3.155812,-5.398127,-8.119918,-2.972952,-1.924891,8.724694,-0.230979,1.202596,6.815457,-2.132340,-6.277622,8.952579,-4.896954,-5.418868,-0.238048,5.392401,0.420212,-1.277650,-2.828880,-9.509429,-1.230538,-8.094626,-8.221854,0.624403,-8.176436,9.047446,2.871141,6.307547,6.867772,-1.794355,5.806226,-0.968598,-1.761602,-1.638973,0.978941,9.947041,-6.710746,-0.325650,-7.064525,1.258423,1.814988,4.549043,1.764044,4.183302,5.621598,-1.348889,6.627091,8.417287,7.952227,-4.157855,-5.173113,0.868018,6.100016,2.318306,3.105351,0.086041,4.947858,1.920990,8.592841,2.194380,7.671844,-7.748729,-0.843130,-4.628358,5.568814,3.089487,-5.131970,7.948312,-4.723115,2.615235,6.421828,7.234945,-4.344762,1.907028,3.634585,-4.711730,7.147674,7.237619,-9.421674,2.339980,-5.159734,6.923023,9.308493,1.429284,3.400130,-7.325282,5.720967,5.308766,-5.352730,3.697660,4.343219,-6.214377,-5.792533,8.227937,8.329134,6.869026,7.636503,3.688445,2.358910,-4.311668,2.288993,6.402581,-5.942118,-3.563437,6.796402,-6.873766,6.807356,9.200790,-4.499749,-1.389896,-3.152108,-0.645029,-7.532918,-0.690170,-1.872999,-6.296440,0.836245,-8.059930,-4.180931,0.135688,-6.180585,9.424751,-4.294499,-3.666419,8.602414,8.867712,-2.147161,1.122031,5.401757,-8.320071,-7.859010,9.358291,-8.703478,-5.520729,9.460560,-7.893500,1.940245,2.205690,9.048586,8.443794,2.479398,-9.203413,-2.203985,-9.972523,4.854821,5.644257,-6.195304,-9.523372,-3.737531,3.869843,-9.801392,2.465490,6.869236,8.855516,-1.914015,2.923262,6.417065,1.676999,7.918774,8.862338,-8.941239,3.803219,-1.120919,8.259097,-4.655002,-0.280099,9.462043,-1.341049,-7.759834,9.032092,-2.147270,-3.547099,-4.598405,5.453583,-9.970281,-7.540926,5.101162,8.669990,6.373886,-4.127662,5.201554,-1.025013,6.435389,-5.527365,6.254198,-2.600152,-1.038693,7.940694,1.490833,7.972995,-4.425876,-6.097004,9.556264,4.440392,3.187133,-8.274365,-0.807035,9.293221,5.252779,2.354583,6.424782,6.051383,9.376363,-9.331819,0.497695,-4.926331,8.065172,-5.075363,-0.716799,-9.522099,6.481247,-0.186848,0.010745,2.500876,0.580735,7.600326,1.957679,5.546550,-6.271279,5.863287,3.907404,3.660803,-2.160408,5.441961,4.222228,-9.698011,-1.127861,-1.646017,-5.424673,-7.131956,-0.704454,-7.326770,-2.143529,-9.318242,5.943102,2.316675,6.185850,-1.273958,-8.089623,-5.849999,8.138361,-1.779812,-6.251478,4.728146,5.165864,-6.650441,-3.503027,1.760349,-6.891868,6.902807,4.870631,-5.200254,7.805165,-3.974727,-3.631777,5.215349,-4.310098,4.488237,-0.237619,7.071480,3.531879,1.087831,9.204232,-9.643434,0.918444,7.527007,-6.404290,5.872480,-4.674042,0.770006,2.022295,-4.228665,3.061086,-0.252296,2.243056,7.113055,4.840774,-9.341606,6.721285,3.361696,-1.199413,6.008046,-3.027191,-5.777583,-2.028346,-5.520430,-1.156706,4.581914,-5.449622,1.836555,-0.137621,-6.041576,1.454742,-8.173096,-4.979501,8.063947,-2.888717,7.865399,-2.400924,-7.803777,-5.486810,-3.647947,4.504312,-2.024063,8.249579,3.596910,-2.195378,5.010912,-2.381634,-8.471918,6.704039,7.442080,-0.081366,9.912625,-8.148830,3.413625,-8.791777,7.266628,-8.211976,9.832303,3.278383,7.927330,1.502582,-1.100679,-2.993112,-8.884886,-6.049897,1.381067,-0.116271,4.356138,-2.602690,5.109344,-5.580541,3.054424,-6.979483,-2.474617,4.030372,7.132385,7.467237,6.439584,-7.725582,8.810303,1.759545,6.318864,8.561026,7.708632,-0.399209,-6.859764,7.136024,2.701188,7.419438,-1.961230,6.175130,2.076273,5.835665,-9.139471,-0.858989,-5.875088,-0.238559,4.482963,7.296815,-3.519419,-2.730409,-4.567768,-3.850211,7.433805,-6.885493,-2.424814,-7.471627,-4.379168,-4.913812,6.546351,-9.322832,6.474963,-7.536050,8.152439,0.894021,4.445213,-8.725573,0.839233,2.348875,-8.881101,-3.879622,0.267933,-5.394652,-5.001862,-5.480179,7.481055,-7.112984,7.970731,-8.918245,-2.596431,-4.397829,7.555481,3.146973,4.406270,3.282575,-0.282701,2.588501,-4.211799,5.139678,-9.443814,5.121892,6.501932,-2.498136,-3.280329,6.540012,-0.739924,-0.338628,-4.649113,9.642910,-0.228322,-5.561427,-8.850645,-9.090954,7.681932,-1.083265,3.664479,-6.713696,9.399380,2.472359,0.463827,-3.095494,2.485188,0.623423,-8.632069,6.612297,2.877425,-5.533989,5.438640,4.008990,-5.350109,3.613607,0.757686,-8.128567,-5.095422,-9.428602,-1.816096,-1.444614,0.602679,-7.055055,-2.660375,-3.864672,4.795382,4.932870,4.726469,3.047026,-9.210479,5.211269,-1.735815,-8.393542,8.597388,-3.648080,8.433180,2.382276,-3.124700,0.857543,-8.206974,9.040441,-9.818845,-3.672021,5.073795,6.080692,-9.278961,1.917139,7.190503,-2.167087,-6.739025,-2.546729,2.463111,-3.803329,6.929458,-3.131339,9.794124,7.103913,-6.478384,7.522405,-0.334984,-8.074486,3.451615,2.716285,7.091760,6.397953,0.449411,-3.993919,-6.530887,-1.622786,-5.163505,3.301740,-7.497826,0.903123,-6.081501,-0.206672,7.538630,-7.202079,-7.103898,7.252160,9.716177,3.567935,3.334280,0.961136,-5.397734,5.306050,-6.220029,-7.318488,-1.686624,3.752756,-1.339064,0.975734,-0.778451,-4.131982,3.084754,1.009534,6.775651,8.313755,-1.174724,-0.671176,6.513873,5.159472,-7.542852,-3.584577,6.216772,8.428960,-9.609702,9.859277,-2.573677,1.824483,-5.931209,-3.997324,-5.317038,-1.101154,-8.649860,8.262442,-9.193029,7.337104,3.382058,9.182262,-8.683852,-8.602216,9.446774,0.492687,-9.477015,-3.836364,5.317124,-5.684037,-9.284916,-9.446674,3.393827,-9.627499,-4.782374,-4.494158,-6.313116,-7.707154,-0.695725,0.939464,6.427635,-5.704503,3.233790,-7.887563,4.220030,-0.732618,9.577445,8.731037,4.548689,-5.570803,2.508063,5.827465,9.766672,-5.112902,-9.000289,0.908535,2.640523,1.349899,-1.830791,3.120861,-3.589515,-0.681561,2.789786,-9.894125,3.490103,-8.149113,0.569403,-0.673888,-4.473407,5.717981,-7.858321,-0.324433,-5.589143,0.231446,3.432630,-4.637681,-1.698202,0.471009,-4.327040,-2.347368,-5.671874,5.764583,-2.482825,-4.428874,-2.876430,-5.610134,0.291303,-5.663597,-2.614468,-8.749010,8.388597,-7.795414,2.805734,5.979179,1.915449,-3.982171,-3.486575,-6.885127,3.376506,5.324944,-0.776388,1.463339,-8.599986,6.528589,7.194075]], dtype = "float64")#candidate|5069|(1, 1274)|const|float64
call_5067 = relay.TupleGetItem(func_3403_call(relay.reshape(var_5068.astype('uint8'), [196,]), relay.reshape(const_5069.astype('float64'), [1274,]), ), 11)
call_5070 = relay.TupleGetItem(func_3407_call(relay.reshape(var_5068.astype('uint8'), [196,]), relay.reshape(const_5069.astype('float64'), [1274,]), ), 11)
func_4213_call = mod.get_global_var('func_4213')
func_4215_call = mutated_mod.get_global_var('func_4215')
const_5079 = relay.const([[-6.913215,7.191946,-0.926027,2.008789,-6.701410,6.436793,4.578252,4.438913,0.386919,3.450355,-8.814270,7.211623],[6.499794,-5.018128,-8.168805,2.899378,7.431622,7.642406,3.579957,-9.261115,3.732249,9.866583,2.279385,8.428329],[-9.902504,9.807966,6.985124,1.071805,0.752428,4.840480,-1.494210,-0.697920,8.453737,2.148895,-0.327874,-8.750728],[9.456746,2.247402,7.408982,-0.574910,0.483534,-3.212232,-5.566128,-0.809779,-5.017890,2.296876,-8.596291,-5.382005],[-3.018265,-1.641162,9.041473,-5.573397,-2.036482,6.879307,1.661984,-9.189791,-3.783733,3.270517,-9.111069,-9.274615],[0.605513,8.548726,-1.286880,-0.299785,-7.506732,5.231819,1.776751,-1.774513,6.356294,6.418862,8.163666,-6.356686]], dtype = "float32")#candidate|5079|(6, 12)|const|float32
call_5078 = relay.TupleGetItem(func_4213_call(relay.reshape(const_5079.astype('float32'), [72,])), 3)
call_5080 = relay.TupleGetItem(func_4215_call(relay.reshape(const_5079.astype('float32'), [72,])), 3)
func_1173_call = mod.get_global_var('func_1173')
func_1175_call = mutated_mod.get_global_var('func_1175')
call_5082 = func_1173_call()
call_5083 = func_1173_call()
output = relay.Tuple([call_5049,call_5053,call_5057,call_5067,var_5068,const_5069,call_5078,const_5079,call_5082,])
output2 = relay.Tuple([call_5050,call_5054,call_5058,call_5070,var_5068,const_5069,call_5080,const_5079,call_5083,])
func_5108 = relay.Function([var_5068,], output)
mod['func_5108'] = func_5108
mod = relay.transform.InferType()(mod)
mutated_mod['func_5108'] = func_5108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5109 = relay.var("var_5109", dtype = "uint8", shape = (196,))#candidate|5109|(196,)|var|uint8
func_5108_call = mutated_mod.get_global_var('func_5108')
call_5110 = func_5108_call(var_5109)
output = call_5110
func_5111 = relay.Function([var_5109], output)
mutated_mod['func_5111'] = func_5111
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5116 = relay.var("var_5116", dtype = "float32", shape = (16, 11, 8))#candidate|5116|(16, 11, 8)|var|float32
const_5117 = relay.const([[[6.587918,-1.110829,7.724776,5.278920,-7.633539,-0.379439,3.841100,6.972918],[1.064832,-4.491105,-8.085859,-3.453921,-4.132353,-4.154601,-9.694024,-3.120306],[0.008831,-1.534919,-6.043279,-1.165599,-8.285527,-5.168951,-7.291270,3.715627],[5.116198,8.442407,2.347998,-1.137063,-9.240294,-5.180234,-5.000393,5.363214],[8.037553,-6.810795,2.994634,-9.153296,-3.930831,-3.630047,-3.475760,-5.831852],[8.388463,6.912771,6.125062,0.579885,9.235230,-5.681327,-5.566809,8.203605],[-2.879863,3.236087,-7.706397,1.507436,-9.406914,5.325580,-6.086774,3.256129],[5.859536,-6.783312,-8.521843,8.896808,8.359389,7.363022,3.250724,8.477035],[8.127429,8.483679,1.903016,-5.555438,-1.730363,-7.768514,3.826421,5.161238],[3.173068,3.848448,1.891132,0.573925,3.123951,-0.160071,3.844435,-9.463521],[4.417517,6.341786,-0.890962,-4.093425,0.855790,9.233947,-3.688353,-0.416113]],[[-8.123783,5.889118,-4.687516,-8.651093,-4.890373,-8.730849,2.783071,-1.300672],[-2.417346,3.701276,2.486335,-1.039062,-6.687191,3.960470,-4.650010,-3.280489],[9.190156,-6.985894,-3.114698,6.192004,8.989934,1.254421,-1.783508,6.333853],[5.445081,-1.518600,4.180957,8.110179,-3.175101,-2.035855,-5.492548,-7.211951],[9.883550,8.987347,0.900355,-7.409462,-1.001303,0.947178,4.879207,-1.523087],[6.732043,8.814439,4.757525,4.258960,7.636774,-0.686569,-2.668276,1.066240],[7.223564,-5.092839,-0.670344,8.552363,-9.562847,0.705060,-8.280302,-5.965399],[-4.485114,-0.998734,-1.919548,-7.631187,5.372340,-7.721579,7.027607,2.779668],[-4.010861,4.871712,-4.684168,-1.697934,-1.502837,-5.772844,7.328000,-8.337285],[-4.631427,8.707233,-1.523713,-1.413547,-9.053708,-7.663267,0.262748,-6.275281],[8.821461,-7.958167,-7.723341,-1.460866,-8.115770,9.458048,4.457654,-8.060357]],[[-3.393209,-8.436177,6.676483,5.709643,9.000392,3.054336,5.328523,4.109742],[0.225176,9.610693,-2.757891,-9.896527,-3.942855,-9.900980,-7.454629,-7.373452],[-7.172128,2.639952,7.144386,1.912484,-6.343071,4.072434,-3.472876,-3.403414],[-9.737848,0.553172,8.849027,-3.484821,-1.407152,0.145979,5.367237,7.520411],[5.489774,3.174017,8.647722,3.318325,2.616496,-1.009704,7.279185,1.151362],[-5.964134,-4.423469,6.262275,8.753088,2.761106,-5.372430,-2.965377,-2.889958],[-5.586386,9.190300,-0.967313,-3.273441,0.825816,6.302311,4.958317,3.669352],[-9.416506,-1.934695,-9.059903,4.975260,-8.249899,-2.380759,5.813746,-5.138095],[-3.774032,-5.077275,8.817035,-3.303946,9.659797,6.791297,-0.497493,-3.537600],[4.262577,-9.814932,-8.778575,4.631212,8.510914,-6.027650,0.614121,2.712503],[-2.869603,-5.077886,-3.400160,-2.185139,7.629409,-0.108374,-8.670219,-1.698845]],[[5.823684,0.953936,-5.653826,1.366986,-4.629183,-1.492105,-9.315279,6.553282],[5.929703,-9.197580,-4.799788,3.917922,0.412483,-2.571434,-2.042296,9.807827],[1.138100,-7.116605,9.015947,-4.067500,5.532434,9.236626,-0.950115,-2.352228],[2.346317,7.499636,7.110364,7.384478,-9.208665,2.206324,-2.981292,4.739144],[0.190901,5.830586,3.916965,4.199784,-0.638782,-0.046593,7.391055,4.800326],[-5.317997,9.467473,0.340241,-5.275170,-9.531441,9.288090,-9.935195,-0.213329],[-4.782929,-9.868291,4.901524,-1.893020,6.023978,-4.652184,9.170297,6.375748],[-0.664696,9.432166,3.473044,-0.055424,9.671426,-5.302785,-2.753811,-2.565789],[-2.994937,-6.582892,-1.680462,3.782385,5.620469,-5.551604,6.699755,-8.671847],[-4.479232,-7.821286,4.665303,9.802616,-4.022552,-9.361646,7.766621,3.685674],[-6.352876,4.164193,-1.376791,-0.893109,5.830905,-1.669155,-4.319352,-1.663034]],[[-4.900517,-0.137833,0.817279,5.552770,5.990661,-6.586339,-5.349571,-9.866741],[5.290818,5.120900,-1.227766,-2.384818,-8.323922,3.524021,8.412639,-3.953038],[-0.500935,-3.186260,-9.136786,9.660908,4.436059,-7.007196,1.888184,-2.991432],[6.329051,-3.991226,2.119245,7.108204,8.015046,-3.411006,-1.182772,-9.094502],[8.263528,1.297376,-5.046341,2.161096,-6.131908,7.897639,-0.817496,7.217690],[0.775018,-6.224737,-2.576740,3.721595,-8.326138,-2.795573,-4.081639,7.233338],[6.098475,1.212300,8.440323,-1.268562,3.304765,6.450652,1.618988,9.526234],[-1.110961,-4.454466,3.998228,-6.875158,6.708987,-2.420245,5.031886,-9.037100],[-4.326436,5.211368,-8.216864,-1.734058,4.346543,-6.240161,-7.055930,-9.211892],[0.102914,3.415035,-2.403816,-6.522471,-1.351816,2.747630,-7.580212,0.571358],[0.004618,-6.558645,-8.247915,3.573650,-4.073616,-3.320851,9.343286,1.388895]],[[1.195722,5.306714,-8.354581,-9.301387,3.218868,-8.943081,0.544732,-3.577532],[-0.436602,-5.821226,7.740538,5.917512,4.363664,-1.314478,-5.611391,9.875997],[-9.217318,4.344518,-6.287789,-7.990838,6.576521,9.229121,-9.018730,9.598144],[-7.663158,9.264067,-1.152429,4.071309,-0.776359,-8.994216,6.249874,2.039579],[1.707763,-8.400449,-3.235996,4.917416,-7.498314,-5.547586,-8.571159,7.990265],[5.439865,4.816696,3.719243,-1.253177,-8.887347,-0.982033,-5.149011,-8.588413],[-9.524223,-5.142833,8.113552,-3.317344,-7.807798,-4.314188,2.209143,-1.002401],[-6.513080,-5.958495,-6.712950,3.798414,3.266946,8.389398,4.223017,5.450745],[-8.040671,-6.859416,5.799843,4.557629,2.409311,3.656453,-5.096094,-7.209135],[9.398651,-9.753318,1.917213,-2.821551,-8.336556,-0.241036,3.212838,7.531320],[4.874671,5.015813,9.341245,3.656919,-6.837622,5.830006,-2.589270,2.828127]],[[-7.330936,6.262774,-1.973183,-3.321934,2.546193,-3.321979,9.338462,2.950321],[-2.211570,8.781317,8.860439,-6.832808,2.047248,-8.688081,0.654738,0.808318],[-9.677898,0.728396,1.469385,5.039288,7.344081,0.666541,4.154575,2.968890],[-6.991282,2.716931,6.905937,3.358229,3.651615,-6.707673,-7.429747,-3.535947],[0.311700,8.055481,-6.838911,3.056115,-6.495364,-9.625582,2.005118,7.150772],[-8.260358,-8.156028,7.795917,2.711898,6.706887,8.474038,6.835591,-2.349037],[-6.450966,4.319000,-3.293307,-2.316804,-7.988554,1.316723,-4.230748,0.008945],[7.093802,7.598551,2.709291,-2.307298,-8.422008,-3.012737,9.490130,-1.557001],[-7.276731,-4.374611,6.873264,-1.872173,7.351838,0.141299,-0.758256,2.703141],[-1.131737,-5.443361,1.650545,2.001917,6.648227,6.860862,-9.042189,-1.567934],[-9.908447,-3.370607,0.899327,8.114674,-9.427454,-9.629205,3.047100,-5.683006]],[[-7.170133,2.597152,0.413027,-6.564450,7.889642,-4.675076,5.767633,-5.246857],[8.592192,2.349598,6.477283,-4.288618,-2.679098,5.928922,-6.552630,7.282408],[-5.264741,-0.834880,4.505797,-2.211981,-2.392568,2.106168,3.031572,4.881711],[-8.046053,2.467857,2.103257,0.150263,7.468727,9.916935,-5.321458,-6.125400],[-3.380272,7.672819,4.186902,-3.444730,-7.418724,-4.001219,4.451229,-5.720668],[-8.482062,-9.344311,7.994130,3.923009,-8.483275,-5.267714,-8.794867,8.896201],[7.367573,-3.204218,7.672615,7.820174,-0.742040,2.614235,1.779831,7.185468],[-3.373949,-4.954136,2.948527,-3.174423,-3.398049,2.944772,9.699744,3.008824],[8.126321,-7.615531,-3.213586,-2.679347,2.110668,2.780418,5.410978,-1.804403],[-6.133466,-5.613688,9.486697,7.416032,8.060291,-9.609184,7.873014,-9.733994],[6.810388,0.148582,-2.346064,0.172964,-8.915973,-8.506772,7.219825,6.154496]],[[9.239299,-5.381687,-9.699989,0.428480,-1.266917,-3.015895,4.282670,-6.096852],[1.523095,7.032063,0.608679,6.876220,4.545757,7.346123,1.925627,-2.554959],[-2.970659,0.467185,-8.959779,1.469436,-3.782047,-2.634260,-5.650141,-7.576326],[3.741874,3.703226,-1.161427,-0.965831,-0.787286,5.961989,-7.245976,8.637259],[-7.660829,3.639046,5.793328,7.668194,-7.276346,2.674275,-5.062369,8.369685],[9.076838,-0.747516,3.412718,2.485145,-1.330816,7.938363,-6.745223,-9.657734],[0.161014,7.719033,-6.130590,-4.763321,6.151273,5.911492,-3.630353,3.945089],[7.796764,9.323928,-8.026723,-6.508954,9.288524,2.791023,-9.919351,-0.850728],[6.612193,-2.691559,-7.235472,-2.967668,0.630041,7.003977,-7.838756,9.175065],[-8.455711,0.436883,-3.070709,-3.486839,4.803198,2.901247,1.796626,-8.042638],[-7.486627,-2.608532,4.975125,-1.089838,-7.689115,-2.913609,-4.909656,-6.178655]],[[6.128494,8.604190,1.842856,4.241021,2.437932,6.355228,9.257004,1.603819],[-3.591256,-7.329225,-6.979328,-6.566204,0.885565,-2.356225,6.628341,-9.672341],[-1.624361,-3.636468,3.408528,-5.542822,-9.181696,3.416501,5.761342,6.883145],[-2.785874,-5.269642,-1.658091,8.380081,4.252953,9.631654,-1.604191,1.987859],[5.889083,1.151767,-7.062151,7.139204,4.915260,-9.381488,2.430691,-1.918832],[3.642749,7.580378,-3.206303,5.584001,-9.876867,-4.675911,4.395064,5.321509],[9.855925,0.531324,-0.304598,-5.174724,-8.980692,6.222682,5.026362,7.457282],[-3.104086,-4.664050,-5.126202,-3.038860,2.562827,3.656502,7.268214,5.255925],[5.120898,-4.644381,-7.224117,2.654832,7.830008,-9.960309,3.308782,8.628166],[-4.444286,-0.979780,-2.263257,7.787996,5.746920,-5.549662,5.126932,6.923616],[-8.625703,8.995270,-0.056534,8.544998,5.380752,-6.617813,-4.743973,-4.634399]],[[-4.375472,9.713264,4.741440,-7.249620,4.010779,7.925429,-8.001102,-0.192885],[-5.931722,6.828110,-3.324599,-2.594365,9.995124,-0.043418,2.335461,-6.316945],[0.689303,-4.986687,5.451126,0.050700,1.254117,3.086134,9.395253,-0.763713],[8.213235,4.007774,1.962679,2.154188,-6.375334,-4.992708,-8.135192,6.578574],[-5.702035,4.593951,-5.099695,-2.555693,2.624354,-1.645912,9.887868,9.142308],[-6.759955,6.951465,-3.058165,-4.504440,-3.606186,-3.254890,-2.301973,6.359468],[8.987362,-5.278926,1.602175,3.759381,-9.643698,-5.326494,5.991919,2.348402],[-4.679693,6.137903,1.807237,0.027803,-3.116288,2.104197,-7.209382,7.246652],[6.623643,2.233119,-4.973080,3.580297,-2.025664,3.277426,2.412160,-1.056149],[6.382875,8.326811,1.701309,-3.708191,-7.043439,-4.577232,-1.413441,7.436112],[8.159094,6.186771,2.738318,0.147164,-0.977849,7.029620,3.762560,8.400448]],[[4.012708,6.085653,2.463416,-3.210365,1.945267,-4.890174,-9.867163,9.362905],[4.714409,-2.413889,-0.432166,-3.518594,-8.043592,-5.864987,8.778320,-3.077788],[-9.240783,-2.137826,5.593086,-8.571279,7.336664,2.463817,-2.888231,-9.960727],[9.704720,-0.473308,-9.068909,-9.950814,5.926956,-0.296436,-2.520268,9.030616],[-5.174315,-4.942310,8.672110,2.944842,-4.358276,-8.887865,9.633914,-7.632243],[6.074511,-4.877545,2.715968,-2.503987,-0.713505,-4.065157,4.952866,7.723459],[7.471624,-3.625524,-4.427847,6.691864,-2.653402,8.633233,-7.959439,-2.976621],[1.999143,8.171723,6.052800,0.612032,-9.471763,-0.623070,7.073169,-0.748160],[0.306449,2.669741,-7.493798,-4.465187,5.823436,-3.065511,9.138964,8.847620],[-8.715064,-5.585629,2.546823,2.345438,2.665809,8.753368,1.202669,2.978364],[-1.446736,0.370386,4.238386,8.908425,8.570306,5.666762,-3.893649,8.746296]],[[1.804144,-3.076069,9.766114,7.689172,3.449208,-0.740722,-0.082689,-1.535436],[-7.276125,8.797200,6.084834,-9.400071,-9.216155,-9.980946,5.554185,0.348361],[7.914473,5.993738,5.351921,8.691762,9.729493,-0.105528,0.234484,1.179408],[-9.004721,9.264643,4.429859,-7.324652,9.934372,0.087008,7.080267,-2.772025],[-6.048076,7.611152,-0.669010,1.788999,-1.427701,6.204074,-0.603182,-4.185971],[3.292167,-0.951603,0.864218,-5.139029,4.236953,0.454109,3.117989,3.509213],[3.142049,6.106338,6.067881,-4.307949,-3.536205,0.144221,-4.814148,7.982718],[-8.667668,-9.777860,9.556303,-9.937819,-2.745130,9.751734,7.551643,-5.928039],[0.950270,-3.471178,-7.502365,4.839219,-5.108088,2.967916,-3.319030,-3.445567],[-7.209310,-8.726676,-6.240691,0.491785,2.335039,-5.170502,9.998339,9.099881],[-7.306906,-2.129445,-4.215228,-6.539196,-6.864026,4.296807,-1.806424,3.646028]],[[3.797342,-6.401085,8.787169,-4.018373,-2.646439,3.768435,9.181572,1.759971],[3.436730,-5.509035,2.512931,-8.376125,-2.747102,-7.322362,-3.170185,-8.200377],[9.560799,3.710179,-2.626490,4.390929,-0.558142,-5.288775,-7.146112,9.947378],[8.472955,7.905460,-5.623474,7.574574,-2.805778,-6.889083,4.983351,-4.137493],[2.161431,6.842573,8.912540,0.399102,-5.473679,-6.800261,1.725751,-5.467477],[9.212742,9.240029,8.052062,5.843196,-8.848735,-6.147538,-3.302713,-5.256907],[-2.758243,8.160226,3.923996,0.882424,-9.973306,-4.142837,-4.229191,9.942562],[-6.159186,9.386216,8.295270,8.536086,-1.627906,7.011542,-3.642904,0.552492],[-2.102460,1.343471,3.515045,2.103190,-3.074909,9.265304,-1.267186,-1.866907],[9.168938,-9.681909,-0.129374,-9.658291,-4.438552,4.499911,0.296303,7.962714],[7.293585,7.101786,-8.210784,6.143538,-5.615652,3.042862,1.702632,-9.641577]],[[0.198966,1.346911,-8.364371,0.477706,5.516534,-6.899328,7.950255,-4.993939],[-3.444951,0.870155,-2.888160,5.604991,1.435068,7.694112,-4.288371,5.905788],[4.100488,-5.092675,-4.789315,-4.892630,-3.566254,-8.354232,-9.869189,5.751477],[7.371644,9.407894,6.513350,-7.517421,0.808863,3.948612,3.875879,-8.193740],[5.754869,2.358223,-0.833254,0.549334,-4.884859,-3.632065,9.118386,7.007056],[-4.928314,-1.582482,8.279523,-4.835648,4.783136,-5.994817,-6.277612,5.967608],[7.611183,1.561592,-6.077996,6.328522,-6.523722,2.435818,4.172186,-8.653924],[-8.727028,1.994692,-0.623971,-7.499823,0.402896,-9.953267,3.887364,3.556219],[-4.128977,-3.603952,5.982242,2.516029,0.827101,2.600092,9.177092,-4.951423],[1.714556,8.508418,0.952029,5.396783,7.211511,-3.576528,9.966927,3.224875],[-3.980630,-7.523671,6.111965,-8.177610,-7.101198,9.949976,3.510122,9.554063]],[[8.430300,-6.067610,5.034707,0.814756,-6.696478,0.311300,0.558259,9.706413],[9.959101,-1.186322,-6.461601,9.906877,-7.066846,-9.213027,9.415841,-4.622298],[6.463567,0.820246,-8.027884,6.861521,5.037214,-8.950697,3.107974,-4.492613],[6.927458,-9.699069,1.689645,5.002363,-9.676830,-6.445249,2.907303,3.911170],[9.135479,1.838471,8.267482,-2.203555,-5.345779,-8.376704,2.045103,-8.013816],[9.094134,-0.200569,-7.958124,-2.490450,2.340877,-9.463940,-8.382158,6.769388],[4.369242,7.961775,4.254119,3.817300,1.001832,-3.882567,-6.243830,6.591353],[7.586997,9.958951,0.045506,-6.463190,-1.063774,-8.439414,-3.584092,-9.870263],[-7.524046,9.071928,-1.842113,8.803095,-1.805435,-9.061995,-9.401224,-0.534445],[1.005882,-0.503857,5.998819,4.766787,7.523765,-8.496394,-7.796295,2.893861],[9.502454,-8.616340,3.833301,3.081422,1.725847,0.942756,2.538100,2.865767]]], dtype = "float32")#candidate|5117|(16, 11, 8)|const|float32
bop_5118 = relay.mod(var_5116.astype('float32'), relay.reshape(const_5117.astype('float32'), relay.shape_of(var_5116))) # shape=(16, 11, 8)
uop_5125 = relay.sqrt(var_5116.astype('float32')) # shape=(16, 11, 8)
bop_5136 = relay.maximum(uop_5125.astype('uint64'), relay.reshape(bop_5118.astype('uint64'), relay.shape_of(uop_5125))) # shape=(16, 11, 8)
uop_5142 = relay.atan(const_5117.astype('float32')) # shape=(16, 11, 8)
uop_5144 = relay.tan(bop_5136.astype('float32')) # shape=(16, 11, 8)
func_2080_call = mod.get_global_var('func_2080')
func_2081_call = mutated_mod.get_global_var('func_2081')
call_5176 = relay.TupleGetItem(func_2080_call(), 0)
call_5177 = relay.TupleGetItem(func_2081_call(), 0)
uop_5195 = relay.acos(uop_5142.astype('float32')) # shape=(16, 11, 8)
output = relay.Tuple([uop_5144,call_5176,uop_5195,])
output2 = relay.Tuple([uop_5144,call_5177,uop_5195,])
func_5197 = relay.Function([var_5116,], output)
mod['func_5197'] = func_5197
mod = relay.transform.InferType()(mod)
var_5198 = relay.var("var_5198", dtype = "float32", shape = (16, 11, 8))#candidate|5198|(16, 11, 8)|var|float32
output = func_5197(var_5198)
func_5199 = relay.Function([var_5198], output)
mutated_mod['func_5199'] = func_5199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_5201 = relay.TupleGetItem(func_665_call(), 0)
call_5202 = relay.TupleGetItem(func_666_call(), 0)
output = call_5201
output2 = call_5202
func_5206 = relay.Function([], output)
mod['func_5206'] = func_5206
mod = relay.transform.InferType()(mod)
output = func_5206()
func_5207 = relay.Function([], output)
mutated_mod['func_5207'] = func_5207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_5234 = relay.TupleGetItem(func_2658_call(), 1)
call_5235 = relay.TupleGetItem(func_2660_call(), 1)
func_3495_call = mod.get_global_var('func_3495')
func_3496_call = mutated_mod.get_global_var('func_3496')
call_5240 = relay.TupleGetItem(func_3495_call(), 2)
call_5241 = relay.TupleGetItem(func_3496_call(), 2)
output = relay.Tuple([call_5234,call_5240,])
output2 = relay.Tuple([call_5235,call_5241,])
func_5244 = relay.Function([], output)
mod['func_5244'] = func_5244
mod = relay.transform.InferType()(mod)
output = func_5244()
func_5245 = relay.Function([], output)
mutated_mod['func_5245'] = func_5245
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5413 = relay.var("var_5413", dtype = "float32", shape = (12, 11, 4))#candidate|5413|(12, 11, 4)|var|float32
uop_5414 = relay.acos(var_5413.astype('float32')) # shape=(12, 11, 4)
bop_5417 = relay.not_equal(var_5413.astype('bool'), relay.reshape(uop_5414.astype('bool'), relay.shape_of(var_5413))) # shape=(12, 11, 4)
output = relay.Tuple([bop_5417,])
output2 = relay.Tuple([bop_5417,])
func_5435 = relay.Function([var_5413,], output)
mod['func_5435'] = func_5435
mod = relay.transform.InferType()(mod)
mutated_mod['func_5435'] = func_5435
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5436 = relay.var("var_5436", dtype = "float32", shape = (12, 11, 4))#candidate|5436|(12, 11, 4)|var|float32
func_5435_call = mutated_mod.get_global_var('func_5435')
call_5437 = func_5435_call(var_5436)
output = call_5437
func_5438 = relay.Function([var_5436], output)
mutated_mod['func_5438'] = func_5438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5560 = relay.var("var_5560", dtype = "float32", shape = (11, 10, 10))#candidate|5560|(11, 10, 10)|var|float32
var_5561 = relay.var("var_5561", dtype = "float32", shape = (11, 10, 10))#candidate|5561|(11, 10, 10)|var|float32
bop_5562 = relay.power(var_5560.astype('float32'), relay.reshape(var_5561.astype('float32'), relay.shape_of(var_5560))) # shape=(11, 10, 10)
func_4735_call = mod.get_global_var('func_4735')
func_4737_call = mutated_mod.get_global_var('func_4737')
call_5567 = relay.TupleGetItem(func_4735_call(), 1)
call_5568 = relay.TupleGetItem(func_4737_call(), 1)
output = relay.Tuple([bop_5562,call_5567,])
output2 = relay.Tuple([bop_5562,call_5568,])
func_5580 = relay.Function([var_5560,var_5561,], output)
mod['func_5580'] = func_5580
mod = relay.transform.InferType()(mod)
var_5581 = relay.var("var_5581", dtype = "float32", shape = (11, 10, 10))#candidate|5581|(11, 10, 10)|var|float32
var_5582 = relay.var("var_5582", dtype = "float32", shape = (11, 10, 10))#candidate|5582|(11, 10, 10)|var|float32
output = func_5580(var_5581,var_5582,)
func_5583 = relay.Function([var_5581,var_5582,], output)
mutated_mod['func_5583'] = func_5583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2794_call = mod.get_global_var('func_2794')
func_2796_call = mutated_mod.get_global_var('func_2796')
call_5664 = relay.TupleGetItem(func_2794_call(), 2)
call_5665 = relay.TupleGetItem(func_2796_call(), 2)
func_2794_call = mod.get_global_var('func_2794')
func_2796_call = mutated_mod.get_global_var('func_2796')
call_5681 = relay.TupleGetItem(func_2794_call(), 6)
call_5682 = relay.TupleGetItem(func_2796_call(), 6)
uop_5692 = relay.log(call_5681.astype('float32')) # shape=(2560,)
uop_5694 = relay.log(call_5682.astype('float32')) # shape=(2560,)
uop_5695 = relay.sigmoid(uop_5692.astype('float32')) # shape=(2560,)
uop_5697 = relay.sigmoid(uop_5694.astype('float32')) # shape=(2560,)
uop_5712 = relay.atanh(uop_5695.astype('float32')) # shape=(2560,)
uop_5714 = relay.atanh(uop_5697.astype('float32')) # shape=(2560,)
output = relay.Tuple([call_5664,uop_5712,])
output2 = relay.Tuple([call_5665,uop_5714,])
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
func_5206_call = mod.get_global_var('func_5206')
func_5207_call = mutated_mod.get_global_var('func_5207')
call_5736 = func_5206_call()
call_5737 = func_5206_call()
output = call_5736
output2 = call_5737
func_5743 = relay.Function([], output)
mod['func_5743'] = func_5743
mod = relay.transform.InferType()(mod)
output = func_5743()
func_5744 = relay.Function([], output)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5890 = relay.const([[[-8.502945,-0.760524,-4.187694,8.093522,-7.314616,0.416153,-8.543908,-1.663243,-9.182705]],[[6.265530,-8.372737,-8.069613,2.197384,0.854967,-4.275240,-6.890680,-3.005769,-9.372667]]], dtype = "float32")#candidate|5890|(2, 1, 9)|const|float32
uop_5891 = relay.cos(const_5890.astype('float32')) # shape=(2, 1, 9)
uop_5893 = relay.sinh(uop_5891.astype('float64')) # shape=(2, 1, 9)
bop_5902 = relay.equal(uop_5891.astype('bool'), relay.reshape(const_5890.astype('bool'), relay.shape_of(uop_5891))) # shape=(2, 1, 9)
output = relay.Tuple([uop_5893,bop_5902,])
output2 = relay.Tuple([uop_5893,bop_5902,])
func_5905 = relay.Function([], output)
mod['func_5905'] = func_5905
mod = relay.transform.InferType()(mod)
mutated_mod['func_5905'] = func_5905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5905_call = mutated_mod.get_global_var('func_5905')
call_5906 = func_5905_call()
output = call_5906
func_5907 = relay.Function([], output)
mutated_mod['func_5907'] = func_5907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4515_call = mod.get_global_var('func_4515')
func_4516_call = mutated_mod.get_global_var('func_4516')
call_5917 = relay.TupleGetItem(func_4515_call(), 3)
call_5918 = relay.TupleGetItem(func_4516_call(), 3)
uop_5928 = relay.sqrt(call_5917.astype('float64')) # shape=(2560,)
uop_5930 = relay.sqrt(call_5918.astype('float64')) # shape=(2560,)
output = relay.Tuple([uop_5928,])
output2 = relay.Tuple([uop_5930,])
func_5932 = relay.Function([], output)
mod['func_5932'] = func_5932
mod = relay.transform.InferType()(mod)
output = func_5932()
func_5933 = relay.Function([], output)
mutated_mod['func_5933'] = func_5933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3596_call = mod.get_global_var('func_3596')
func_3598_call = mutated_mod.get_global_var('func_3598')
call_5936 = relay.TupleGetItem(func_3596_call(), 0)
call_5937 = relay.TupleGetItem(func_3598_call(), 0)
output = relay.Tuple([call_5936,])
output2 = relay.Tuple([call_5937,])
func_5950 = relay.Function([], output)
mod['func_5950'] = func_5950
mod = relay.transform.InferType()(mod)
mutated_mod['func_5950'] = func_5950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5950_call = mutated_mod.get_global_var('func_5950')
call_5951 = func_5950_call()
output = call_5951
func_5952 = relay.Function([], output)
mutated_mod['func_5952'] = func_5952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_5971 = relay.TupleGetItem(func_2658_call(), 0)
call_5972 = relay.TupleGetItem(func_2660_call(), 0)
func_1395_call = mod.get_global_var('func_1395')
func_1397_call = mutated_mod.get_global_var('func_1397')
const_5977 = relay.const([[-5.969148],[-9.038695],[8.963143],[-4.600070],[3.462906],[0.122712],[1.725237],[1.690939],[-9.254805],[-8.064809],[0.386387],[7.217628],[2.545432],[-0.313147],[9.667026],[-6.941763],[-3.361895],[0.500205],[2.642787],[-9.170944],[6.771868],[-0.240469],[-5.303588],[-1.311113],[-1.125953],[7.238492],[-1.914982],[-9.960228],[9.100233],[-8.296847],[2.399769],[-7.638639],[8.171380],[-3.471554],[-5.282153],[5.082890],[-3.217571],[-2.173862],[-3.201153],[-9.696647],[4.121066],[-7.669885],[-5.065664],[7.226641],[3.901701],[-0.938686],[-1.611760],[7.836439],[-2.230722],[-6.050251],[-4.623336],[-8.442207],[-5.661785],[9.473336],[-6.340331],[0.977848],[-7.854167],[3.782124],[5.788835],[-7.471758],[-0.150243],[3.373492],[-7.454690],[-3.264656],[-4.106474],[0.731058],[8.683883],[-2.841627],[-7.032330],[-0.342159],[6.062483],[-7.847325]], dtype = "float32")#candidate|5977|(72, 1)|const|float32
call_5976 = relay.TupleGetItem(func_1395_call(relay.reshape(const_5977.astype('float32'), [3, 6, 4])), 0)
call_5978 = relay.TupleGetItem(func_1397_call(relay.reshape(const_5977.astype('float32'), [3, 6, 4])), 0)
output = relay.Tuple([call_5971,call_5976,const_5977,])
output2 = relay.Tuple([call_5972,call_5978,const_5977,])
func_5995 = relay.Function([], output)
mod['func_5995'] = func_5995
mod = relay.transform.InferType()(mod)
output = func_5995()
func_5996 = relay.Function([], output)
mutated_mod['func_5996'] = func_5996
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6023 = relay.var("var_6023", dtype = "float32", shape = (2, 10, 13))#candidate|6023|(2, 10, 13)|var|float32
uop_6024 = relay.tan(var_6023.astype('float32')) # shape=(2, 10, 13)
output = relay.Tuple([uop_6024,])
output2 = relay.Tuple([uop_6024,])
func_6039 = relay.Function([var_6023,], output)
mod['func_6039'] = func_6039
mod = relay.transform.InferType()(mod)
mutated_mod['func_6039'] = func_6039
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6040 = relay.var("var_6040", dtype = "float32", shape = (2, 10, 13))#candidate|6040|(2, 10, 13)|var|float32
func_6039_call = mutated_mod.get_global_var('func_6039')
call_6041 = func_6039_call(var_6040)
output = call_6041
func_6042 = relay.Function([var_6040], output)
mutated_mod['func_6042'] = func_6042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3596_call = mod.get_global_var('func_3596')
func_3598_call = mutated_mod.get_global_var('func_3598')
call_6046 = relay.TupleGetItem(func_3596_call(), 0)
call_6047 = relay.TupleGetItem(func_3598_call(), 0)
output = call_6046
output2 = call_6047
func_6075 = relay.Function([], output)
mod['func_6075'] = func_6075
mod = relay.transform.InferType()(mod)
mutated_mod['func_6075'] = func_6075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6075_call = mutated_mod.get_global_var('func_6075')
call_6076 = func_6075_call()
output = call_6076
func_6077 = relay.Function([], output)
mutated_mod['func_6077'] = func_6077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5995_call = mod.get_global_var('func_5995')
func_5996_call = mutated_mod.get_global_var('func_5996')
call_6081 = relay.TupleGetItem(func_5995_call(), 1)
call_6082 = relay.TupleGetItem(func_5996_call(), 1)
func_4811_call = mod.get_global_var('func_4811')
func_4814_call = mutated_mod.get_global_var('func_4814')
const_6087 = relay.const([-2,3,-5,8,7,7,-7,-1,-5,-4,-4,-10,5,-10,-10,-4,-7,10,6,-2,-9,2,-6,-4,6,1,2,2,5,-8,-10,9,-3,-9,-6,-1,2,2,-4,8,6,-9,-1,4,2,-10,6,10,-8,-8,4,1,1,-1,-10,7,10,-2,7,-4,-8,1,-4,5,4,8,3,1,3,-8,-4,-8,-1,3,6,8,4,2,-4,1,2,-5,1,8,-1,8,3,8,-6,-3,8,10,3,-1,-1,-7,2,-6,10,-6,2,4,9,9,-3,-2,6,-5,4,-7,8,7,-4,10,7,-4,-1,-2,10,-10,4,8,-3,-8,-10,-3,-9,-6,-3,8,6,9,-10,-10,2,5,-1,7,-7,3,2,-4,8,3,-8,-1,2,-2,3,-3,9,3,1,3,7,-3,-6,9,9,-7,-4,1,-10,-8,-2,-8,-9,10,2,-7,-3,-7,7,3,1,-3,8,-1,-7,-1,-10,-2,9,8,-9,-10,5,-1,5,-10,-6,3,9,4,3,-6], dtype = "uint8")#candidate|6087|(196,)|const|uint8
call_6086 = relay.TupleGetItem(func_4811_call(relay.reshape(const_6087.astype('uint8'), [196,])), 2)
call_6088 = relay.TupleGetItem(func_4814_call(relay.reshape(const_6087.astype('uint8'), [196,])), 2)
func_2722_call = mod.get_global_var('func_2722')
func_2723_call = mutated_mod.get_global_var('func_2723')
call_6089 = relay.TupleGetItem(func_2722_call(), 0)
call_6090 = relay.TupleGetItem(func_2723_call(), 0)
output = relay.Tuple([call_6081,call_6086,const_6087,call_6089,])
output2 = relay.Tuple([call_6082,call_6088,const_6087,call_6090,])
func_6093 = relay.Function([], output)
mod['func_6093'] = func_6093
mod = relay.transform.InferType()(mod)
output = func_6093()
func_6094 = relay.Function([], output)
mutated_mod['func_6094'] = func_6094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_6173 = relay.TupleGetItem(func_1299_call(), 1)
call_6174 = relay.TupleGetItem(func_1300_call(), 1)
uop_6187 = relay.log(call_6173.astype('float64')) # shape=(5, 15, 6)
uop_6189 = relay.log(call_6174.astype('float64')) # shape=(5, 15, 6)
output = uop_6187
output2 = uop_6189
func_6199 = relay.Function([], output)
mod['func_6199'] = func_6199
mod = relay.transform.InferType()(mod)
output = func_6199()
func_6200 = relay.Function([], output)
mutated_mod['func_6200'] = func_6200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1173_call = mod.get_global_var('func_1173')
func_1175_call = mutated_mod.get_global_var('func_1175')
call_6214 = func_1173_call()
call_6215 = func_1173_call()
func_4515_call = mod.get_global_var('func_4515')
func_4516_call = mutated_mod.get_global_var('func_4516')
call_6224 = relay.TupleGetItem(func_4515_call(), 3)
call_6225 = relay.TupleGetItem(func_4516_call(), 3)
output = relay.Tuple([call_6214,call_6224,])
output2 = relay.Tuple([call_6215,call_6225,])
func_6242 = relay.Function([], output)
mod['func_6242'] = func_6242
mod = relay.transform.InferType()(mod)
output = func_6242()
func_6243 = relay.Function([], output)
mutated_mod['func_6243'] = func_6243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4591_call = mod.get_global_var('func_4591')
func_4593_call = mutated_mod.get_global_var('func_4593')
call_6254 = relay.TupleGetItem(func_4591_call(), 1)
call_6255 = relay.TupleGetItem(func_4593_call(), 1)
func_5743_call = mod.get_global_var('func_5743')
func_5744_call = mutated_mod.get_global_var('func_5744')
call_6256 = func_5743_call()
call_6257 = func_5743_call()
func_5580_call = mod.get_global_var('func_5580')
func_5583_call = mutated_mod.get_global_var('func_5583')
const_6262 = relay.const([[0.775486,-4.423896],[8.618030,6.154986],[-4.856774,-9.812258],[-7.354960,-0.859506],[-4.727622,-1.749860],[-0.679976,7.716072],[-7.179929,-7.348068],[3.611579,2.677474],[-2.937221,-3.723396],[9.505422,-1.283964],[-2.753024,-4.359037],[-7.737146,-8.573613],[5.219147,1.249380],[-1.850781,-3.872881],[2.988177,6.615930],[-8.234689,-1.838963],[-5.900031,-2.858429],[-4.745578,8.648194],[1.481870,8.323267],[-0.817532,-5.669653],[0.509349,-8.891566],[-0.615806,-8.112295],[6.156756,-5.031214],[-8.761183,-0.686127],[-6.681768,-9.782626],[2.168567,8.114469],[3.144459,9.948911],[-3.981164,3.186390],[1.171173,0.764307],[-0.263292,1.659533],[8.937830,-5.231651],[-4.487207,-4.141032],[4.179517,6.583716],[9.722427,-0.257455],[-3.636140,-7.697138],[4.343446,-1.463283],[5.888053,5.042791],[7.571578,9.913080],[-2.155726,-7.222168],[-7.135120,3.942669],[3.945761,4.402915],[4.558844,-6.319499],[7.569180,-5.114114],[-8.816602,9.110630],[-7.532897,-2.345794],[7.128113,-9.316321],[6.686317,8.199985],[-4.196489,2.619177],[0.992064,-5.145027],[-9.856352,-7.611840],[1.527571,9.195287],[3.291157,-4.766211],[6.485375,7.125085],[-1.484575,-4.828331],[-9.993148,-1.507206],[9.378844,7.713004],[-5.067370,9.520447],[-2.800041,-5.823246],[5.300562,7.129018],[-6.328761,-0.412767],[-7.133852,-3.292402],[-8.246631,-2.421929],[-6.920123,9.476200],[7.004901,3.696928],[-9.472140,-0.558541],[-5.325371,-2.160058],[-3.436115,8.121628],[0.207535,-3.668661],[2.817899,8.546231],[-5.803524,1.835867],[-5.156952,-9.236059],[6.766370,0.324958],[-0.889082,-9.078790],[-9.454227,-7.613274],[-9.708750,6.236688],[-3.308765,-8.044118],[-4.239010,8.580336],[5.865475,-6.549466],[1.810512,1.240235],[-1.228967,-8.938777],[1.593968,0.424698],[7.512313,-9.616175],[2.342084,-4.623660],[-7.301198,-6.657831],[-3.145486,3.583772],[-9.328495,6.231050],[-7.088273,-3.417796],[9.836988,5.185671],[2.488905,-8.304551],[8.319947,-2.906796],[-0.410480,-7.948172],[5.324761,4.055722],[-1.443127,-9.028280],[-3.976905,-0.551589],[-6.216213,5.100917],[3.679999,-8.116971],[-3.945563,6.497605],[-7.549909,-7.472807],[-5.156678,9.592907],[6.651188,1.449474],[6.841489,-2.728575],[4.825852,-4.874768],[6.690668,0.718038],[-7.216381,5.938014],[-7.835643,-2.659747],[5.170085,0.799417],[4.684393,0.691976],[-4.151348,-1.621725],[-3.146045,9.285313],[7.901086,-2.341374],[-7.281180,9.921065],[0.829360,6.835860],[-0.122589,-9.150999],[-3.197327,0.017667],[-9.774761,2.245897],[-0.808142,-1.037746],[-8.893465,-3.042393],[3.244223,7.844397],[9.421265,2.704090],[5.837440,-5.132191],[-9.693766,4.757796],[7.103746,1.360098],[-4.965735,-3.267684],[-1.735088,5.683170],[-6.527689,2.473954],[-7.934076,5.357798],[2.337713,9.505918],[1.576896,-8.015094],[-8.085967,3.737798],[0.599042,-2.946434],[0.054208,-6.283798],[1.387032,-0.635971],[3.943009,-8.495910],[-4.697973,5.344785],[-2.954350,0.618943],[5.755891,1.580657],[7.501717,6.134410],[4.523419,-1.057266],[-6.168312,6.891908],[6.073642,2.546497],[0.336371,-0.112752],[-6.539094,7.694072],[-0.346616,-9.810098],[0.563851,-3.668123],[-0.003288,4.839197],[4.905707,-5.508043],[-9.019248,4.657723],[-0.369886,-8.710050],[-3.642194,2.155711],[8.036209,8.111320],[1.175678,3.184423],[-5.566047,-0.258635],[4.667465,-1.560660],[9.792245,-4.913848],[-1.189416,6.619071],[-2.904944,-2.555138],[2.778858,4.342994],[5.499584,-0.969238],[9.068792,5.039609],[7.419029,-3.365311],[0.888789,4.274299],[-0.662837,-0.560640],[-3.270278,6.175910],[6.251129,8.013983],[7.273233,9.181826],[-4.187153,-0.163797],[1.520039,6.760991],[9.143404,0.489874],[-8.107078,2.083563],[-2.208530,-8.306419],[-9.250917,-4.613549],[5.852871,-4.811649],[-5.141675,5.043557],[2.725240,-1.520019],[3.017232,-7.775606],[-7.488907,1.133335],[-7.014575,4.641871],[-0.871197,7.782733],[8.890040,2.148573],[-1.790744,7.016634],[8.110095,8.213805],[-5.789380,-0.097210],[2.669581,-5.779121],[-9.154384,-7.944102],[5.011768,-2.540817],[1.700364,-2.944633],[5.267729,-7.271552],[4.121599,-0.371993],[-3.333112,9.966109],[-4.887780,4.526250],[-5.464657,4.265865],[0.023109,-0.974037],[9.363289,7.688110],[-3.114952,8.936956],[6.253102,6.469574],[4.784283,4.544255],[2.098125,7.391466],[-5.790895,2.837848],[-3.588176,-9.458780],[6.219758,-9.046895],[0.231428,0.641503],[4.521572,4.519215],[-1.265730,6.333004],[-8.338476,-0.624308],[-9.751476,6.127942],[-4.376920,9.061422],[3.286433,-3.304722],[-2.365737,6.100957],[-0.854662,-6.279249],[5.129403,-3.346130],[-0.117325,-8.623411],[3.303505,6.835425],[-4.660357,-5.996799],[8.839243,6.202518],[5.145064,3.599465],[4.334734,7.148543],[-3.137159,7.887072],[0.443530,7.227309],[-9.767593,3.132570],[-1.272752,6.234630],[9.939641,6.223606],[2.855888,-7.384892],[1.467640,3.466916],[-2.684708,-3.307343],[-5.521170,8.045450],[-2.383597,3.385616],[-7.003792,-1.501583],[0.622730,3.971623],[3.105241,-7.617036],[1.757962,-3.518555],[-2.326447,9.899268],[-2.674841,7.209016],[-5.133990,9.975878],[-8.461065,0.568381],[5.352520,8.093185],[1.977771,1.435915],[-3.985696,2.592803],[-4.575006,-2.313974],[3.018787,-7.402964],[9.130097,-0.684854],[-1.264123,-8.130928],[0.938071,1.176259],[7.078472,5.461514],[4.124551,-2.977850],[-2.986205,0.604760],[2.452933,-3.317487],[-6.939547,-1.878126],[-3.390702,9.687793],[-1.798859,5.957262],[2.655325,-1.305849],[-5.126060,4.570753],[5.679531,3.668593],[9.819812,-0.577481],[-7.371634,-4.878362],[4.702151,-1.810406],[5.848659,-7.101315],[-5.023679,9.819606],[-8.298138,-5.893983],[-9.322917,-2.828152],[4.459136,0.180617],[4.163135,0.265521],[-0.366186,-1.205616],[3.610550,-9.064529],[-3.499137,-9.964231],[-0.020470,-3.025813],[-6.530402,4.151580],[-7.557101,-7.968575],[8.295786,-1.627350],[9.443329,-9.818350],[6.065837,-7.199777],[-9.513985,-4.959992],[6.117586,3.111792],[-3.237332,7.936611],[-1.303643,6.292020],[-9.633992,7.832706],[-7.750415,-3.698232],[2.128109,7.690686],[5.146926,3.172793],[-5.929374,-1.654090],[3.403039,-2.771534],[5.943800,-0.265178],[-1.210250,-7.051549],[6.156207,3.321503],[-1.933533,8.747957],[-6.839061,-5.801470],[-3.354958,7.345598],[1.466794,8.401547],[1.972141,6.014632],[4.340194,7.936550],[1.292571,-9.512496],[7.883444,-6.636248],[-6.557242,0.771118],[8.798300,-2.511667],[-7.034617,-8.452984],[-1.511891,-7.307855],[0.346184,-5.927873],[4.680006,5.364339],[-6.504261,3.993963],[2.905587,3.584883],[1.738403,-6.871859],[-6.808546,8.184832],[4.456973,6.285793],[4.133362,1.767681],[6.377341,7.414072],[6.192121,4.463700],[-3.462859,1.867096],[7.081654,6.909662],[-8.476036,0.080647],[1.216187,7.106560],[-2.330804,-1.341459],[-7.231173,2.574157],[7.060900,-3.792672],[7.758724,-7.938208],[-0.345929,5.233995],[-2.812859,-2.303728],[-2.886599,-7.245666],[-1.818907,-4.102056],[-1.337229,-5.573446],[2.794910,-9.916294],[-6.951991,0.328286],[-8.668655,-2.026510],[-9.419393,-3.246187],[-1.075423,8.256149],[-8.807435,-9.571943],[4.153688,-8.550160],[3.986034,-4.138018],[-0.659134,-2.219912],[3.019720,-8.446779],[8.639821,-5.806823],[-6.925374,5.754078],[6.691489,2.759720],[-3.472729,9.070116],[4.247969,9.177577],[-7.599126,9.863667],[-3.568487,-0.145768],[3.058569,9.441094],[1.642049,-9.745644],[2.599839,-9.272320],[-1.872792,-5.613610],[-8.826833,-8.201720],[3.265835,-5.621905],[9.788332,-6.389031],[8.701469,5.907009],[2.262778,-2.288500],[-3.714282,-9.949773],[-5.130505,2.877670],[1.348989,6.747214],[2.909796,0.539964],[0.729384,-6.057119],[5.884266,-0.992347],[0.663652,4.973958],[-7.435026,2.024525],[0.490440,-3.279197],[1.369371,-4.887858],[-7.646097,-6.499568],[-8.967908,-9.401043],[9.605152,-5.484617],[-1.715490,-8.755815],[2.421130,-5.603140],[0.918052,-1.188547],[-9.176372,-9.998134],[-9.412797,-0.638946],[-5.381527,-8.664576],[-6.213845,-1.888016],[-9.756138,-5.821310],[9.452563,-9.989132],[-5.159677,-1.149276],[0.757779,-6.960107],[-6.633557,1.140852],[-9.791057,3.093067],[-8.825179,7.371738],[-7.303366,-3.284512],[-3.569195,4.541027],[3.031297,-7.769020],[8.681515,8.371409],[-9.195687,-4.692878],[-2.823798,6.114025],[4.651807,1.747586],[8.303283,-2.634575],[-1.022299,-8.170363],[6.724420,-9.780343],[3.768979,-3.862063],[-6.747534,6.119182],[-1.245326,8.442686],[2.835368,1.860240],[0.659979,-0.866648],[9.944799,-7.047738],[-0.302919,-5.217620],[7.225876,-1.016660],[-6.395700,2.818704],[1.060085,0.261266],[-7.862248,-4.042701],[0.234476,-8.973531],[6.531790,3.722935],[7.467454,-7.016690],[-3.535944,7.231320],[-3.101933,8.976258],[-1.903359,5.462575],[6.218586,5.724677],[6.002281,-7.194910],[2.506992,1.593738],[9.240549,9.885732],[-3.878211,-1.317907],[8.314685,-8.883825],[-0.268653,-9.169329],[-5.457190,-4.324918],[-3.632726,3.291238],[8.140982,-2.430544],[-9.177034,7.386922],[1.062357,-7.788576],[3.087873,-6.173064],[-2.681733,-2.395816],[-7.471262,-4.026740],[-1.238778,1.031661],[-6.680250,-1.555480],[-3.682534,8.471784],[-6.097547,-6.412588],[2.971871,6.428463],[-4.076427,8.215536],[1.722508,7.451683],[-5.295935,-7.017099],[-3.921519,8.965401],[8.325720,-2.193319],[5.586579,-6.437950],[4.259275,8.127560],[-8.315831,9.804475],[-1.422113,9.482160],[-8.443955,-5.845890],[-1.633529,5.251585],[-4.385353,-2.306530],[-5.165010,2.530574],[-7.673702,8.115544],[-6.464605,-3.388636],[8.773975,3.633449],[4.245672,2.782935],[2.050768,-5.782246],[8.132469,-0.644202],[6.476161,2.904589],[-6.836554,5.688655],[-6.102140,-4.557851],[5.055209,3.011445],[-1.510121,-2.041635],[-6.670489,3.508536],[2.078225,6.680010],[4.067859,-2.350002],[-1.184318,-2.816234],[-5.900621,3.156893],[-3.651162,-8.543840],[6.351382,-8.186546],[-1.241920,6.247704],[3.354921,8.734250],[-8.939196,8.222386],[-1.877923,-9.055353],[6.607114,7.011478],[-5.262336,-5.008647],[-8.784093,-9.456133],[3.028625,9.064996],[-1.293626,-0.857806],[2.273019,-6.926441],[-6.167323,2.724097],[-9.495176,-7.296205],[-8.092308,0.705991],[-2.823347,4.116051],[-5.626724,-0.195088],[9.129028,-8.373680],[-6.228479,9.470816],[-1.631739,-6.605356],[8.922280,4.125026],[2.804342,9.006319],[-7.501111,5.282720],[-1.285042,9.418301],[-5.504376,-1.618160],[-0.851060,5.628540],[6.297586,-2.631048],[7.660156,8.631891],[5.437742,-3.149625],[-0.258488,-8.323912],[-0.501385,6.246546],[4.430136,-3.427639],[6.156108,1.970985],[1.481790,-6.015415],[0.465713,-4.584916],[2.336051,4.372616],[-8.172287,-3.623708],[0.743367,5.047801],[-4.346144,-9.528661],[-9.009856,7.350534],[-1.015934,0.496931],[-6.835105,-0.201115],[-9.804820,-9.683241],[-1.994395,-2.112351],[9.757606,3.084179],[-8.960315,-1.135268],[-3.540973,-3.135478],[8.646495,-5.313869],[-0.124625,7.283656],[9.278896,-5.283918],[-2.716869,-1.924723],[-4.941779,-7.443123],[8.215711,-3.158239],[-1.532614,-4.728774],[9.690807,9.126423],[-6.892616,-1.131088],[2.466087,3.832811],[-0.237662,6.497335],[-1.773128,6.405207],[-8.000275,-9.388227],[-0.405155,2.659056],[-8.520338,7.522366],[-1.227530,-6.037156],[-2.148925,0.827852],[3.712827,-3.019952],[-5.330022,-2.534935],[7.753670,3.266593],[4.274702,1.182379],[-0.444450,0.236345],[-6.241743,0.633506],[1.127227,-6.344219],[-3.117060,-4.302016],[-5.376618,3.937834],[-2.246859,-3.134181],[-1.355297,2.611526],[2.457611,7.494502],[-7.748960,-5.553083],[0.299491,9.312695],[-3.118484,-0.929129],[-8.302681,-3.833513],[2.424570,6.581412],[2.281517,-3.402396],[-7.619792,-2.440545],[-7.010632,3.099224],[-0.855172,-6.412626],[0.854156,-9.634726],[4.229408,6.641171],[3.599849,-2.847083],[5.370456,-2.651025],[4.015373,-2.646796],[4.642318,-1.939560],[-9.362871,-5.242124],[6.671847,-7.742722],[-9.085540,-1.850193],[2.316994,2.794369],[0.439073,-5.038963],[-6.224843,-0.284903],[2.852647,8.128976],[3.816458,-6.253229],[5.367881,-7.171626],[5.188939,-8.262659],[0.439405,9.591658],[-0.066682,-2.430596]], dtype = "float32")#candidate|6262|(550, 2)|const|float32
call_6261 = relay.TupleGetItem(func_5580_call(relay.reshape(const_6262.astype('float32'), [11, 10, 10]), relay.reshape(const_6262.astype('float32'), [11, 10, 10]), ), 1)
call_6263 = relay.TupleGetItem(func_5583_call(relay.reshape(const_6262.astype('float32'), [11, 10, 10]), relay.reshape(const_6262.astype('float32'), [11, 10, 10]), ), 1)
var_6281 = relay.var("var_6281", dtype = "float32", shape = (550, 2))#candidate|6281|(550, 2)|var|float32
bop_6282 = relay.minimum(const_6262.astype('int8'), relay.reshape(var_6281.astype('int8'), relay.shape_of(const_6262))) # shape=(550, 2)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
const_6288 = relay.const([0.937937,4.282166,4.057028,-3.662848,-9.564648,5.456054,5.460015,-1.283428,7.762008,1.567073,7.220771,7.793901,1.087805,-0.937103,-9.116360,-2.346596,-8.964682,-8.025430,8.070762,-7.853154,5.144855,-6.838901,-9.576904,9.901552,-8.592588,-4.795980,4.899968,2.335057,-7.995136,4.663823,3.517839,-9.432049,5.993327,-4.654805,6.278292,-2.026702,-4.735615,8.417665,8.024730,-6.592902,3.725375,-0.677465,8.771096,-1.150714,9.619630,-8.808978,8.702617,-0.360232,0.195503,-6.818927,3.639328,3.576079,4.560548,2.346158,7.955737,-5.106685,-6.688437,8.069613,-3.498619,2.325321,7.112792,7.402838,-7.322293,1.851281,-8.953139,-8.836239,5.112357,1.615307,4.109383,2.891421,1.792087,9.898125,-5.434673,7.641410,-5.900939,-0.372289,-4.206442,5.958123,-8.232950,7.619278,-6.104892,-2.082755,2.593323,-6.849647,-7.339099,-6.711494,-5.769333,-8.287189,-1.958657,8.233275,-5.501657,8.075820,0.713112,-5.003823,8.989923,-7.353449,1.526790,4.602171,5.973518,9.744515,-8.352718,6.844400,-6.498024,9.116928,2.946141,2.021470,3.110598,-1.997930,8.046449,-0.677842,-3.072870,-8.882231,2.561731,3.213805,-3.449658,3.128890,-8.691766,0.457831,-8.127623,9.123258,6.374325,5.027493,4.456813,-8.248843,-8.681229,-9.665162,5.926010,3.779372,-8.027674,6.440346,9.110698,1.318815,8.074262,-0.651636,-2.408079,3.192088,8.112863,-4.131587,6.753735,6.008818,3.864958,-3.125640,8.802256,6.752894,-8.418790,-4.793368,0.524489,9.492375,-8.120936,-3.482600,-4.995219,-7.215440,8.434901,-8.219292,9.559046,-0.404217,0.464812,-6.025333,-8.586229,0.522395,-2.873773,3.750442,0.892198,8.362989,-2.893510,-0.240416,6.764419,-4.895482,9.865099,0.486614,4.442430,4.400240,4.591402,3.112694,-8.084398,-4.863718,-1.494198,-3.673010,2.065502,6.313623,-3.785711,-5.627427,-4.249436,-9.480972,3.780169,9.299517,1.004835,-6.403575,-3.792905,4.877752,-0.651588,0.951122,3.518552,-9.026914,2.589058,-8.726464,-4.414196,-8.245890,-1.764117,-3.989751,-1.497726,-7.787371,2.364403,-5.468290,-2.358067,-6.499999,-4.145852,0.709821,9.333546,-2.012373,9.711191,-5.447423,1.602391,-2.456541,9.597431,4.157332,-0.961264,-9.866806,-4.290787,9.288812,-4.727248,8.987812,-4.707510,-1.168311,1.970918,-1.455757,8.743596,-8.398322,5.744844,-1.053243,5.908147,2.189762,1.715118,3.141033,-7.990839,-6.713873,-5.679806,6.532501,-7.768681,3.031856,-1.141662,-9.375292,-2.395096,-9.898005,-3.490179,8.132707,4.172729,5.505872,-8.710466,-9.527462,-8.674953,3.122385,5.003270,4.709319,-6.842605,8.841271,-8.246680,-9.210498,-9.052710,3.654759,-1.818882,-3.373397,1.742155,-5.171193,1.271328,-5.602934,-5.610792,-0.910533,1.610799,2.744840,-6.854339,-0.516016,1.172881,-9.015760,-1.237194,-4.262182,-7.293060,-7.412974,-3.237211,8.235441,0.470060,9.092386,4.161699,0.355900,9.186794,-9.028313,6.415163,6.625955,6.895510,-6.298643,8.066205,-2.821260,-0.542511,6.098261,-5.610105,-4.020350,-4.980709,4.725433,6.612054,-3.100800,9.277163,1.523101,-3.929892,3.645970,-7.329664,9.693996,-6.676726,5.250559,-5.091661,-2.741116,4.590273,-4.229772,-5.191110,0.317448,0.212779,1.737003,-0.625034,6.184920,8.274917,-8.117996,5.863305,0.294089,-0.663569,-1.213729,3.558334,4.698036,7.161410,-1.915372,7.418029,8.002657,-5.581884,3.235432,0.571775,6.189455,-4.698872,-0.084586,9.297247,8.215159,-0.331007,-9.236612,-9.308751,-2.976661,8.896478,-4.043988,-4.421806,6.164665,-3.562899,9.772983,-3.106616,-5.940993,2.385388,-3.106569,-4.552455,-1.335730,5.847724,-4.717383,-5.224055,4.405777,8.238694,-8.758993,3.093577,-6.119231,-6.734391,-7.083920,-0.707801,6.083734,7.938823,-9.576662,-9.085483,9.591135,1.573526,4.227399,-4.976313,-7.136575,-3.276721,-6.681981,-2.447681,5.254689,-1.294645,8.952204,-7.413456,-8.171594,-1.039577,7.808141,6.650785,-9.150619,-1.898246,-4.425274,-9.263220,2.661966,6.836674,1.592392,-9.315835,5.689786,-1.489849,-9.670580,5.241127,-0.536446,2.914179,-2.477549,-0.809411,-2.132742,9.484211,-5.395037,6.406982,-3.448987,5.497409,-4.529669,8.180831,-2.775232,0.857525,-7.522330,-8.421366,-8.839535,4.352871,-0.448395,-3.598421,-6.918066,-0.265459,9.031281,-2.636823,-1.458168,1.215355,-5.214406,-5.707350,-8.727294,3.822205,2.513032,-3.123623,5.933380,-6.141631,8.114610,-3.714425,-1.650056,-8.144358,-9.279448,-4.740580,-3.204345,-7.926207,-4.437353,-2.828866,-9.130286,2.530290,8.046448,7.301422,6.778506,-0.555352,-9.478418,1.619597,5.785029,5.225727,-9.316757,9.560563,6.773169,4.990644,-9.227870,4.204859,7.927063,-3.941106,-7.019352,-5.809009,-0.702943,-3.058301,4.019847,7.485722,-4.712918,0.432623,-8.215135,3.444739,-8.931683,9.164296,-6.552053,1.287662,-8.703380,-6.741523,1.046056,-8.454881,-8.834793,1.161095,-9.292673,-4.735057,0.494923,-3.785774,-0.586951,7.938885,-2.912472,-6.627411,6.849611,8.001461,4.756930,-9.830383,-2.699245,-5.420220,-9.878764,-9.752942,2.490998,3.760622,-2.006614,-7.151587,4.202012,9.935900,9.475002,1.315531,0.375425,-3.397628,-9.779632,-8.634950,6.897959,7.486823,-5.908577,4.486876,3.955300,-1.942019,-6.780612,-4.379634,-0.652551,4.316146,9.816129,4.967028,1.651652,-4.783929,-4.326371,-0.290835,2.612407,3.928313,-8.745483,7.596151,7.506165,2.455115,0.399557,-2.115342,-2.309846,1.187879,-3.057587,-0.316745,-0.053466,6.672366,2.266142,-0.681460,-7.710595,-5.679544,-7.048194,-1.632530,8.373943,6.448373,8.984295,0.773709,-2.183338,-4.824548,6.217721,-8.580960,7.418243,-6.798479,-4.683608,0.168549,1.705553,1.102713,-5.211986,2.622141,5.570947,-0.890585,-3.687921,-4.030061,-4.316387,4.636043,-0.410953,3.121595,-4.031665,-1.947284,-0.001667,2.710113,-7.659882,-2.980989,-8.068466,-6.248286,-6.239042,-1.239460,-8.131912,9.403962,4.696125,-2.149689,6.008094,3.295375,-2.019331,-8.208520,-1.723796,-5.212934,-5.180047,2.090564,-3.405035,-7.721327,-5.884647,-9.957195,-9.533601,9.612401,-3.026890,6.563346,6.923910,6.320687,-8.592581,-7.081880,1.298582,3.722723,2.916340,-0.333693,4.816451,6.733831,-4.674992,-6.053406,4.020460,-1.025623,-9.562607,9.402291,1.721706,2.534140,-6.810976,-1.386761,-7.378417,8.125025,-5.157169,6.920016,0.688563,1.776174,-1.067228,-6.714977,1.536235,-4.441002,-2.187247,9.706443,-0.116741,0.397457,-7.459986,9.557315,-6.687845,5.583658,-1.269707,-9.147911,8.743492,6.165206,2.604093,3.774532,8.466752,-7.413712,-0.890654,0.658609,-9.018936,8.605009,-9.190375,6.548392,-4.646607,0.313727,-8.597573,-9.093439,0.754562,7.002346,5.553791,9.460744,-2.127565,-1.344104,6.962408,-6.228938,-6.452814,-4.008206,-5.796157,9.811595,-9.570666,6.525025,-6.242021,-1.417939,-3.479231,9.680548,7.908216,-2.871835,-0.188610,-7.635264,-7.001095,-0.468911,-4.552143,1.058892,-0.185727,2.795007,5.595117,1.931903,-2.965576,0.498793,-7.256592,-6.824053,8.952846,8.576550,5.225021,5.725991,-7.575325,6.889301,-4.847246,4.632142,1.618153,-3.790657,-8.452004,0.934057,2.328309,2.100811,2.424221,9.621380,-6.495802,-5.339718,-9.442554,2.489760,1.990777,-2.329972,8.421013,4.755888,-4.997304,2.487078,0.256980,-1.457554,6.480304,-1.418647,6.703432,2.897850,9.126373,-1.332415,3.426319,-2.889358,-4.436628,-1.742091,4.406670,-1.610057,3.326748,-3.769235,-7.284877,-0.280004,-7.893158,-2.796935,-9.507765,9.158727,-1.040169,-1.555163,4.570047,-7.848008,9.069032,3.207044,-7.989557,-4.825763,6.058979,9.399057,5.138427,3.607532,-4.469417,-3.908539,8.628741,-1.879250,9.666656,2.076416,-1.325411,-4.593232,-2.598020,-8.415406,1.963045,0.102837,6.127409,6.291811,-5.569375,-6.718216,-2.662931,8.849707,-6.688641,8.992895,-7.156032,-8.786483,5.701011,-2.506513,-9.974066,-4.976171,-3.584138,-1.934081,-9.823620,-0.006222,-7.043117,-7.438693,6.343938,-7.157772,2.850721,0.503813,-1.728890,-6.414406,-1.314360,6.746723,1.360258,9.262868,0.837359,5.482907,4.977290,-9.301229,-9.307320,-8.579331,9.562247,0.379686,3.343545,-2.108758,-7.069518,3.554976,-0.933651,0.483257,-9.701174,2.148451,-2.426443,-9.276356,-8.783566,6.711733,0.214629,3.881596,-6.151114,0.338962,4.669082,2.897804,6.512202,4.640594,-8.775712,3.811205,8.057633,-0.785171,-6.475348,8.742618,-4.080530,8.286191,-6.547663,-5.881175,-5.027294,-7.676740,8.505873,0.986123,-6.760374,-0.559427,-4.797630,-9.224235,-9.835195,2.607415,0.489073,-1.788991,-6.481482,5.636262,-4.745246,8.221742,8.864208,-9.956474,-1.126860,9.406702,-7.438214,5.655417,-1.891516,-5.881861,-8.662921,0.711404,-0.427926,0.543774,9.154874,-3.211738,-5.852130,-8.924343,1.637260,0.553263,6.671977,0.601035,-1.883893,-7.261166,-3.041550,-0.583462,-4.167413,-7.844293,8.899715,0.435494,-1.150140,-1.565825,-2.997994,-7.420364,5.162090,1.587103,4.750343,8.355695,5.687749,-6.275810,-9.700840,-0.635716,-2.829137,-8.746941,7.324831,-4.607084,6.739765,-1.711957,-6.228257,4.108433,-6.723234,-3.173974,7.799935,-6.056468,9.438408,-8.938067,1.498324,-4.997900,9.989572,4.566862,4.466678,-3.012638,-4.389587,-8.587963,-0.900406,-9.397286,-7.731427,-1.172597,-6.556381,-8.323239,6.754035,-9.879269,8.252572,-9.220815,3.553037,2.037870,0.519912,0.679858,8.915154,-7.362045,4.215895,-8.604126,5.519578,-0.304787,4.364250,7.440387,4.280420,4.073813,6.623247,-0.510453,4.614126,6.390765,0.431552,-2.008891,-9.987130,-6.706506,-4.806741,5.485016,3.874599,2.894284,-3.119031,2.648192,-8.903522,-6.696265,-8.087165,-0.771535,5.593146,8.860521,-1.814014,4.809890,-8.263861,4.717888,-2.425479,4.839882,-2.686331,4.225897,8.508683,-0.332946,0.356427,3.940475,5.041448,-4.467316,8.589952,-9.636923,6.509902,-6.202862,5.218879,-6.585283,-6.670957,-9.458613,7.182434,0.198721,-7.465774,-9.058841,5.611261,-0.768904,-6.973056,5.074456,-6.179686,6.788410,2.013400,8.053683,6.228247,-1.624662,0.177187,-0.599679,-1.243005,-7.957662,-1.303519,8.799992,-9.339131,-3.103719,-4.916328,9.595748,9.433458,-8.243069,-0.151847,-7.987680,-8.052232,-1.872799,1.623312,-8.773078,-4.566034,-7.435936,2.384143,-1.864805,9.342816,-4.390232,-7.227955,-0.943911,6.218682,-1.239571,5.404693,4.581127,-0.597415,1.438315,3.273066,6.699563,-3.809472,-7.561431,6.967237,-5.443019,2.809394,-0.952399,-5.735645,-4.072990,-7.651108,9.753957,8.659836,4.333686,-6.290146,6.802612,-4.855563,-9.229412,-0.458346,-9.823073,5.089423,1.396864,-3.454599,7.378272,-5.464146,-1.746281,-3.793041,-6.302473,-3.245930,7.572728,8.452851,-5.421346,-0.458071,-7.162722,0.426529,-4.524407,0.453663,-6.917845,-7.092115,-4.328451,8.730571,6.386811,4.269070,7.400139,6.464161,-5.086571,9.954109,-9.293621,6.898332,-0.247589,5.772925,-3.886107,-0.151336,-1.511309,-9.056477,-0.855318,5.265205,2.432655,9.110930,7.482245,-5.587168,9.673869,-2.280453,6.858598,3.523862,5.759098,-6.665369,8.929468,-5.455647,1.083952,4.014756,-8.421422,5.174300,0.697846,-0.503685,0.638944,-7.497829,-7.954663,-3.507505,7.055747,7.063856,4.006576,-3.679983,5.908579,-9.846665,4.713353,-7.301426,5.688305,7.637090,-1.790333,4.504464,-5.505120,7.143357,-2.430404,-5.218964,5.527040,-1.735262,-7.820442,9.720934,5.145348,-6.145065,2.566991,-5.044370,1.902612,7.541332,6.538482,2.885639,0.263004,-6.850013,2.811312,6.801860,6.333721,5.176923,-7.359615,2.163777,-1.012561,-2.193618,-9.067785,-1.801245,-1.981483,6.411992,-3.212594,-6.175499,6.244976,-5.724148,4.022389,2.682234,2.104631,-1.096648,-3.970051,-3.538455,-1.209298,-4.646463,7.233867,-6.203732,3.170895,-8.305626,-9.945208,6.466755,7.039591,-3.721068,2.347837,9.161550,-2.372407,-7.309807,6.762877,-4.625824,2.132997,-7.927959,2.488760,-1.219458,3.676172,2.032328,0.888580,8.090955,-8.280852,-3.239815,-3.183982,-6.829980,5.221407,1.930805,6.167866,-4.670886,-6.411818,-4.567835,4.386766,-8.243179,7.940891,7.798767,-5.838048,9.056051,-9.163293,-9.473898,-9.849675,-6.660058,1.578825,-3.289139,1.971084,8.256600,-0.617023,8.875103,0.358122,-4.057015,9.493051,6.930325,-7.304563,-2.750875,-5.114860,9.810233,-6.195356,6.314159,3.422235,-2.905518,-5.272171,5.693411,9.332330,3.807373,-6.525834,7.010488,6.872999,-6.050525,-8.562359,-0.095378,9.070576,1.511578,6.816085,-4.298327,-1.114908,5.670102,-9.364299,0.357121,-3.779154,-4.705452,-1.482022,-8.908079,9.812507,-1.024930,-0.293379,-7.281517,-3.334465,6.869473,-8.591563,8.955982,-0.825333,-9.753810,2.035479,8.213966,-1.730261,-8.846190,1.548352,-4.375909,2.817307,-2.659067,3.867161,-4.509566,-0.624825,-8.466251,0.046198,-4.432143,-2.087142,-5.844189,-2.536780,2.512294,-2.440662,-1.350109,1.914695,-5.690369,3.748668,-6.044366,7.800380,-3.498423,-6.006787,2.571138,-4.651686,3.499666,-9.293949,-4.069129], dtype = "float64")#candidate|6288|(1274,)|const|float64
call_6287 = relay.TupleGetItem(func_2494_call(relay.reshape(const_6288.astype('float64'), [13, 7, 14])), 1)
call_6289 = relay.TupleGetItem(func_2496_call(relay.reshape(const_6288.astype('float64'), [13, 7, 14])), 1)
func_5244_call = mod.get_global_var('func_5244')
func_5245_call = mutated_mod.get_global_var('func_5245')
call_6300 = relay.TupleGetItem(func_5244_call(), 0)
call_6301 = relay.TupleGetItem(func_5245_call(), 0)
output = relay.Tuple([call_6254,call_6256,call_6261,bop_6282,call_6287,const_6288,call_6300,])
output2 = relay.Tuple([call_6255,call_6257,call_6263,bop_6282,call_6289,const_6288,call_6301,])
func_6311 = relay.Function([var_6281,], output)
mod['func_6311'] = func_6311
mod = relay.transform.InferType()(mod)
mutated_mod['func_6311'] = func_6311
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6312 = relay.var("var_6312", dtype = "float32", shape = (550, 2))#candidate|6312|(550, 2)|var|float32
func_6311_call = mutated_mod.get_global_var('func_6311')
call_6313 = func_6311_call(var_6312)
output = call_6313
func_6314 = relay.Function([var_6312], output)
mutated_mod['func_6314'] = func_6314
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6338 = relay.var("var_6338", dtype = "float32", shape = (11, 1, 3))#candidate|6338|(11, 1, 3)|var|float32
var_6339 = relay.var("var_6339", dtype = "float32", shape = (11, 9, 3))#candidate|6339|(11, 9, 3)|var|float32
bop_6340 = relay.divide(var_6338.astype('float32'), var_6339.astype('float32')) # shape=(11, 9, 3)
func_5932_call = mod.get_global_var('func_5932')
func_5933_call = mutated_mod.get_global_var('func_5933')
call_6344 = relay.TupleGetItem(func_5932_call(), 0)
call_6345 = relay.TupleGetItem(func_5933_call(), 0)
uop_6349 = relay.rsqrt(bop_6340.astype('float64')) # shape=(11, 9, 3)
output = relay.Tuple([call_6344,uop_6349,])
output2 = relay.Tuple([call_6345,uop_6349,])
func_6351 = relay.Function([var_6338,var_6339,], output)
mod['func_6351'] = func_6351
mod = relay.transform.InferType()(mod)
mutated_mod['func_6351'] = func_6351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6351_call = mutated_mod.get_global_var('func_6351')
var_6353 = relay.var("var_6353", dtype = "float32", shape = (11, 1, 3))#candidate|6353|(11, 1, 3)|var|float32
var_6354 = relay.var("var_6354", dtype = "float32", shape = (11, 9, 3))#candidate|6354|(11, 9, 3)|var|float32
call_6352 = func_6351_call(var_6353,var_6354,)
output = call_6352
func_6355 = relay.Function([var_6353,var_6354,], output)
mutated_mod['func_6355'] = func_6355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6075_call = mod.get_global_var('func_6075')
func_6077_call = mutated_mod.get_global_var('func_6077')
call_6359 = func_6075_call()
call_6360 = func_6075_call()
func_5743_call = mod.get_global_var('func_5743')
func_5744_call = mutated_mod.get_global_var('func_5744')
call_6382 = func_5743_call()
call_6383 = func_5743_call()
output = relay.Tuple([call_6359,call_6382,])
output2 = relay.Tuple([call_6360,call_6383,])
func_6395 = relay.Function([], output)
mod['func_6395'] = func_6395
mod = relay.transform.InferType()(mod)
output = func_6395()
func_6396 = relay.Function([], output)
mutated_mod['func_6396'] = func_6396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4591_call = mod.get_global_var('func_4591')
func_4593_call = mutated_mod.get_global_var('func_4593')
call_6407 = relay.TupleGetItem(func_4591_call(), 1)
call_6408 = relay.TupleGetItem(func_4593_call(), 1)
output = relay.Tuple([call_6407,])
output2 = relay.Tuple([call_6408,])
func_6409 = relay.Function([], output)
mod['func_6409'] = func_6409
mod = relay.transform.InferType()(mod)
mutated_mod['func_6409'] = func_6409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6409_call = mutated_mod.get_global_var('func_6409')
call_6410 = func_6409_call()
output = call_6410
func_6411 = relay.Function([], output)
mutated_mod['func_6411'] = func_6411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mod.get_global_var('func_736')
func_737_call = mutated_mod.get_global_var('func_737')
call_6421 = func_736_call()
call_6422 = func_736_call()
func_2337_call = mod.get_global_var('func_2337')
func_2338_call = mutated_mod.get_global_var('func_2338')
call_6428 = func_2337_call()
call_6429 = func_2337_call()
uop_6432 = relay.asinh(call_6428.astype('float32')) # shape=(450,)
uop_6434 = relay.asinh(call_6429.astype('float32')) # shape=(450,)
uop_6436 = relay.log2(uop_6432.astype('float64')) # shape=(450,)
uop_6438 = relay.log2(uop_6434.astype('float64')) # shape=(450,)
func_3189_call = mod.get_global_var('func_3189')
func_3190_call = mutated_mod.get_global_var('func_3190')
call_6440 = func_3189_call()
call_6441 = func_3189_call()
output = relay.Tuple([call_6421,uop_6436,call_6440,])
output2 = relay.Tuple([call_6422,uop_6438,call_6441,])
func_6449 = relay.Function([], output)
mod['func_6449'] = func_6449
mod = relay.transform.InferType()(mod)
mutated_mod['func_6449'] = func_6449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6449_call = mutated_mod.get_global_var('func_6449')
call_6450 = func_6449_call()
output = call_6450
func_6451 = relay.Function([], output)
mutated_mod['func_6451'] = func_6451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3608_call = mod.get_global_var('func_3608')
func_3609_call = mutated_mod.get_global_var('func_3609')
call_6464 = func_3608_call()
call_6465 = func_3608_call()
output = relay.Tuple([call_6464,])
output2 = relay.Tuple([call_6465,])
func_6475 = relay.Function([], output)
mod['func_6475'] = func_6475
mod = relay.transform.InferType()(mod)
mutated_mod['func_6475'] = func_6475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6475_call = mutated_mod.get_global_var('func_6475')
call_6476 = func_6475_call()
output = call_6476
func_6477 = relay.Function([], output)
mutated_mod['func_6477'] = func_6477
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6492 = relay.const([[[5,-10,-9,-4,-1,4,-1,6],[7,-9,-2,-5,-1,-7,-10,-10],[10,7,-3,8,3,4,4,-8],[-7,-3,-5,5,7,-4,-6,-6],[-6,-6,4,-1,-7,-3,-4,-9],[5,1,-2,10,10,-8,8,-3],[-5,-1,4,-7,6,1,10,-4],[1,9,-4,3,-2,-10,-3,3],[3,-8,-8,7,7,-6,7,-4],[-7,-4,-1,-5,-7,3,8,-1],[-2,8,-6,-3,-3,7,-1,8],[3,9,8,7,6,9,-6,7],[-9,-7,9,5,-3,4,5,-1],[4,2,-1,1,-1,-5,1,6]],[[-8,5,4,-1,-2,2,7,-6],[3,-6,1,6,-8,-10,5,-8],[-10,10,3,-3,-6,-2,8,5],[10,-8,9,-2,6,-5,-9,-2],[6,-4,-3,3,2,4,5,-1],[-1,5,-4,-8,-8,-1,-7,-7],[5,1,-8,9,10,-2,-1,10],[-6,3,-2,10,3,9,2,-3],[7,5,6,7,-7,3,-4,1],[9,-9,4,-5,1,-9,1,-2],[-3,6,-2,9,6,7,-6,9],[4,-8,-7,9,8,3,-9,-10],[1,-4,-10,2,5,-5,2,6],[-4,-8,9,9,5,-9,-6,-7]],[[-4,1,1,2,-7,-7,-3,-6],[-9,-7,10,-6,-9,-9,5,-5],[-4,4,4,-3,7,9,-3,8],[-7,-10,3,4,-2,-1,7,-5],[4,8,9,8,-1,5,-4,-6],[8,-10,4,4,-8,-3,1,-8],[9,-3,-9,-4,2,6,4,6],[10,4,-1,1,5,4,2,-3],[10,-1,10,9,5,-5,9,-3],[-9,-2,7,-10,7,-2,-8,2],[-4,-4,6,-6,1,4,-3,9],[-5,-4,4,7,-10,2,6,5],[-5,-2,-6,-6,10,-5,4,-6],[-6,-3,6,2,1,-7,6,-6]],[[-3,-3,-9,-4,-6,3,-4,1],[1,10,6,-7,-6,3,-6,-6],[-9,8,8,4,-2,8,-8,-7],[4,8,1,-8,-10,2,10,-5],[-7,-5,-6,10,8,5,8,-6],[-1,-2,-2,1,1,-7,1,2],[-6,4,-7,-9,2,-2,-8,-3],[-3,-3,-7,-6,-8,-3,-9,-7],[-1,-7,5,7,2,10,-8,-10],[1,-7,-8,9,7,4,-7,9],[2,-8,3,-4,5,-8,-6,5],[10,6,-4,-3,-8,-7,8,5],[-3,4,-8,-5,-4,-7,9,-8],[3,-8,-10,10,-10,5,2,-7]],[[-2,-2,-1,3,-10,-6,2,10],[9,-4,3,-6,-8,8,-8,-4],[-7,-1,5,-4,6,-4,3,6],[3,10,4,8,9,-4,2,9],[6,8,6,6,1,10,5,-7],[-8,6,-4,-3,-10,-10,-7,-2],[9,-4,-3,6,-10,9,4,6],[4,5,-4,-9,-7,9,-7,5],[-10,-2,-9,8,-7,-7,-4,5],[4,-3,8,5,4,7,4,9],[3,8,10,-3,2,7,6,-3],[2,1,10,5,-9,-7,-6,-8],[6,1,1,-2,-8,10,-1,-2],[-8,2,8,-4,-2,9,-5,-7]],[[4,-8,1,-9,-9,3,-1,4],[8,7,-5,-5,2,-5,3,-10],[9,2,-10,-1,10,-10,8,10],[9,-4,-8,1,2,-7,-7,10],[6,8,-4,6,10,7,-7,-6],[4,-9,8,4,-6,-5,-9,9],[-10,3,5,-8,-5,-4,9,9],[9,-10,7,-9,5,6,-10,1],[-1,3,-6,-2,3,-3,6,-10],[9,-4,-1,1,-6,2,-3,5],[9,-1,-9,6,-7,-6,9,7],[-3,-4,3,-4,4,4,-1,3],[-7,7,-7,7,1,8,9,-8],[8,1,-9,10,-1,1,3,3]],[[10,7,-4,5,10,-3,-1,-3],[5,2,-9,9,7,3,6,2],[-8,5,-3,-7,-4,-2,-1,5],[1,2,-8,-1,1,-6,3,-4],[7,5,10,5,-10,10,-3,1],[-10,5,4,-4,-1,-1,-8,-5],[2,7,2,5,-2,-5,-10,9],[9,-2,2,-5,8,-7,-1,-3],[4,7,3,-8,-9,-10,-9,-10],[4,1,-10,1,6,-4,2,-2],[-7,-2,4,-7,-3,3,7,2],[7,-9,4,5,-8,7,-6,6],[-9,-6,-8,-8,-10,-5,-4,10],[4,10,-9,-6,-4,5,-3,3]],[[-9,4,2,8,-1,-10,-2,8],[-10,-4,3,-6,-4,-5,3,-8],[7,-10,2,-2,3,-9,2,2],[8,-1,-7,-8,-9,7,-2,-6],[5,-9,-6,-1,5,-7,-9,-1],[7,10,10,-7,2,2,-9,5],[4,2,-7,10,-4,8,-8,-2],[10,8,-1,-8,-9,9,9,-3],[-7,3,-9,-3,4,6,-10,-6],[2,10,-1,8,-1,9,10,2],[-10,-9,-10,1,4,5,-8,4],[-6,-7,5,8,-4,-5,-2,2],[-2,8,5,-7,9,-5,-4,8],[3,9,-1,-3,6,9,-7,-8]],[[4,-2,-7,8,-10,4,-1,-3],[10,-2,9,-7,-7,4,9,-10],[2,-2,10,7,-4,-3,-5,-9],[8,-7,-1,3,1,10,3,-3],[-4,6,-6,6,-5,-4,5,7],[-7,10,9,5,-3,1,7,-1],[-10,8,9,5,3,6,5,9],[8,-9,5,8,-9,3,3,-8],[10,-1,10,-1,-5,10,10,1],[1,6,4,-3,5,8,10,2],[-3,-9,7,7,6,-4,-9,6],[-7,-5,8,-3,-5,-10,-8,-7],[3,6,-5,-6,10,-9,6,-8],[-8,3,2,9,-6,4,-9,-7]],[[-4,-4,5,10,-1,4,-2,10],[5,8,-9,7,-3,-1,2,7],[-10,7,-1,3,-3,9,9,-9],[-5,4,-3,-9,-3,-9,8,-3],[6,-6,-6,-9,3,-6,9,7],[-4,6,-3,4,-5,3,8,2],[3,-3,6,-9,9,-1,3,-2],[10,-4,5,1,10,3,-7,6],[-4,10,-10,-1,4,-9,2,6],[9,9,8,2,-1,8,2,1],[-10,8,-1,10,10,4,9,8],[-10,10,4,-5,-8,6,-4,8],[9,5,2,7,3,6,3,-9],[-10,10,2,-2,6,-2,6,-6]],[[5,-6,7,3,-7,1,4,3],[-1,-9,-8,-3,10,7,-9,-2],[8,-3,3,6,-6,10,-9,5],[7,10,8,2,-3,3,-5,6],[5,8,-7,8,1,7,-2,-7],[8,-8,5,4,2,7,6,-1],[-5,7,-3,-9,-4,4,9,-8],[-1,5,8,-3,9,-8,-5,6],[-7,-6,-7,-7,-9,8,4,-7],[10,-2,-1,9,-7,7,-5,6],[5,4,-4,4,4,3,7,5],[-10,-8,-4,-3,1,6,2,-7],[1,10,4,3,5,6,-4,9],[-9,-6,-1,5,8,9,-3,-6]],[[10,2,-9,2,10,6,-2,-9],[2,-6,-4,-9,4,4,-4,2],[8,10,10,3,-1,-4,-6,3],[-8,-2,-10,9,-9,-1,-5,9],[-8,1,8,-8,3,-1,4,-6],[3,-7,1,8,8,2,-4,-7],[7,-10,1,5,9,4,10,-6],[-2,-9,-8,2,8,-9,5,5],[-3,-9,3,2,-2,3,-10,6],[-3,-4,1,7,10,-2,-2,-8],[-9,1,3,-2,-2,8,6,-2],[8,-2,-2,10,6,8,8,5],[5,9,-1,-4,10,5,-5,-6],[4,5,6,-9,-7,10,-5,3]],[[5,9,-5,-9,4,-2,10,3],[4,10,-5,-10,-8,-8,-9,2],[-4,-8,-5,-5,-10,9,5,-1],[-9,-6,-10,7,-9,10,9,-10],[6,-4,-6,9,8,-5,9,1],[-7,-4,-3,6,7,2,9,-1],[-3,-5,5,-4,-9,7,4,-7],[5,1,-2,4,2,-7,9,7],[2,10,3,2,2,1,-7,9],[10,2,7,-5,-9,4,-2,-9],[-1,4,2,8,-7,-1,9,-6],[10,-5,3,7,-4,-1,2,-1],[-8,6,10,5,-7,2,6,7],[8,-2,1,5,2,10,-8,6]],[[-5,-10,-10,-2,1,1,4,1],[9,4,-7,-5,-9,-5,-7,4],[5,7,-9,10,-3,-7,-10,-10],[6,-1,5,3,3,10,9,4],[-10,-9,1,10,2,-4,8,3],[8,-6,-10,-4,7,6,9,-1],[-2,7,2,1,7,-8,7,-6],[5,-7,-2,-9,6,4,5,2],[6,5,9,3,1,-10,1,5],[-9,-1,3,8,5,-5,-9,-2],[-8,-4,2,4,7,2,-9,5],[9,-9,-6,-4,-10,5,-5,6],[-3,2,-10,-9,-10,6,-7,-9],[7,-1,-4,-5,-1,6,7,-9]]], dtype = "uint64")#candidate|6492|(14, 14, 8)|const|uint64
var_6493 = relay.var("var_6493", dtype = "uint64", shape = (14, 14, 8))#candidate|6493|(14, 14, 8)|var|uint64
bop_6494 = relay.right_shift(const_6492.astype('uint64'), relay.reshape(var_6493.astype('uint64'), relay.shape_of(const_6492))) # shape=(14, 14, 8)
output = bop_6494
output2 = bop_6494
func_6501 = relay.Function([var_6493,], output)
mod['func_6501'] = func_6501
mod = relay.transform.InferType()(mod)
var_6502 = relay.var("var_6502", dtype = "uint64", shape = (14, 14, 8))#candidate|6502|(14, 14, 8)|var|uint64
output = func_6501(var_6502)
func_6503 = relay.Function([var_6502], output)
mutated_mod['func_6503'] = func_6503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5932_call = mod.get_global_var('func_5932')
func_5933_call = mutated_mod.get_global_var('func_5933')
call_6553 = relay.TupleGetItem(func_5932_call(), 0)
call_6554 = relay.TupleGetItem(func_5933_call(), 0)
output = call_6553
output2 = call_6554
func_6559 = relay.Function([], output)
mod['func_6559'] = func_6559
mod = relay.transform.InferType()(mod)
mutated_mod['func_6559'] = func_6559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6559_call = mutated_mod.get_global_var('func_6559')
call_6560 = func_6559_call()
output = call_6560
func_6561 = relay.Function([], output)
mutated_mod['func_6561'] = func_6561
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6591 = relay.const([[[-2,2,1,9,-4,-1,9,-6,8,7,3,4,-2,4,2,3],[-8,-3,2,5,5,9,-5,8,-8,-1,-8,-5,-5,-2,-1,-10],[-3,-10,-6,-2,-2,-4,5,8,-6,-4,-5,9,-10,-6,7,1],[-10,-4,5,-5,7,4,3,3,3,6,-6,10,7,8,4,3],[-10,8,4,-2,5,1,10,-7,-3,4,9,7,2,9,7,-9],[10,-2,-3,5,4,7,-2,-8,-1,-4,6,6,9,3,-9,4],[-10,-6,-3,-2,-7,-1,-5,-1,3,7,-1,9,-10,7,-3,-9],[-7,7,-3,7,9,-8,8,3,7,1,4,-7,2,-4,-4,9],[9,1,6,4,5,2,-3,5,6,9,7,8,1,4,6,-7],[9,7,-6,-1,-2,4,-9,-7,-4,8,-2,1,-8,-9,8,9],[3,-5,8,-10,8,-8,-3,-3,-9,10,-7,5,6,10,-1,3],[9,-3,-3,-9,-8,-9,2,-8,3,6,-9,-5,-6,-6,6,-9],[7,-1,-6,1,-9,-5,-4,-4,10,-7,1,-3,9,-4,-1,1]],[[6,8,4,5,2,4,4,-5,8,-5,-5,7,-8,-10,-3,-8],[-5,-2,8,10,-9,7,2,10,-3,-10,3,-4,-6,3,7,10],[-6,1,-2,-5,7,6,6,-9,3,7,7,-1,6,-4,-3,-5],[9,-6,-8,3,5,-3,9,9,-5,10,-8,5,-4,10,-3,10],[-10,-4,7,2,-9,2,10,2,8,7,4,1,-1,7,6,8],[4,-6,9,3,-4,-8,4,2,-3,-7,3,6,1,-9,-1,-4],[-1,7,8,-2,5,-9,-1,3,3,10,10,-1,-9,7,-9,6],[1,2,3,2,-5,9,5,7,-1,-4,-2,3,5,-1,3,6],[3,1,-3,4,-7,3,6,-10,8,-10,-8,2,-5,2,2,-1],[-8,-1,-7,-1,1,-6,4,3,-1,2,8,-5,-9,-10,-4,8],[-3,-5,7,7,-9,-2,-9,5,-10,9,1,8,8,-2,8,4],[-8,-2,-4,10,1,6,-1,-2,-10,-8,3,-10,5,-3,2,4],[8,-5,-6,6,9,9,-5,-10,10,-5,-5,7,-6,2,-10,8]],[[-4,-10,7,8,-8,-9,-8,7,8,-4,-6,2,-1,-10,9,-9],[-2,-3,-5,-9,10,5,7,-7,-3,-8,9,-10,2,-1,1,-6],[-9,2,-2,6,-8,-1,4,-2,6,-7,-9,7,-9,4,8,-3],[-3,-10,7,-8,-8,2,4,2,-3,6,8,-3,4,6,-1,1],[-5,8,9,-9,-4,3,-2,-9,4,6,1,-8,1,8,-7,6],[10,-4,-2,9,3,-6,-9,-1,-4,-6,10,-9,1,3,-6,10],[6,8,6,-6,1,5,8,-6,4,-7,-7,-5,6,4,8,-10],[7,-4,5,-3,1,8,-5,4,-6,6,-9,-2,1,-7,-10,-5],[2,2,-9,-6,5,4,8,-3,-8,8,2,-10,-5,-5,-1,4],[2,-3,-2,-3,-2,-9,2,-7,-1,-8,6,-9,5,8,6,1],[7,-9,2,-6,-7,-7,6,-9,-8,1,5,4,4,7,-5,8],[-4,-3,-6,-3,3,-4,-3,-6,-2,-4,7,-8,-2,-2,5,1],[4,-10,-2,-5,-4,-5,-2,9,-10,-10,4,9,-4,5,9,-3]],[[-7,-7,-7,-3,1,-9,9,-8,2,5,5,4,-4,-9,2,-10],[-4,-9,9,-1,9,3,9,-8,-9,-8,8,-6,-8,9,-8,2],[-4,-2,-2,3,-6,-1,10,-7,-4,-7,-5,-7,7,-7,-5,-8],[8,3,-4,1,-5,-4,-2,5,-6,-10,-3,-5,5,7,3,-10],[-7,10,9,3,6,6,8,5,2,-6,6,-9,-5,10,4,-8],[-3,2,2,4,5,-7,3,-9,-9,2,-6,6,-9,-9,8,-4],[8,5,-3,9,10,3,9,-8,4,-4,3,10,-8,-5,-8,9],[8,7,2,-1,5,-6,3,5,-4,-8,10,-8,-8,-7,5,4],[10,7,9,-4,2,-9,4,4,2,6,1,2,-9,8,7,-7],[3,-8,-10,7,4,8,-9,-7,-6,4,-7,7,-7,9,-6,10],[-8,10,-3,-1,2,-7,4,3,-5,7,5,-7,8,-6,-10,-2],[5,10,10,6,-3,-4,-7,6,7,-3,7,7,-3,8,9,6],[3,-1,7,6,2,-8,-10,-10,-10,-1,2,2,3,3,-1,6]],[[-2,8,6,-1,5,-7,6,4,-2,-2,-3,2,-6,7,-3,-3],[10,6,7,-4,9,-9,-1,-2,8,-7,-10,-8,-5,6,-8,5],[-2,7,2,-4,-5,7,-6,6,3,-4,4,9,-6,7,6,5],[-7,-9,-4,-10,-6,2,8,-5,-3,5,-2,5,1,-4,-6,-3],[1,-1,-7,-3,-10,6,-5,8,-1,-5,7,-10,4,5,3,2],[-2,-1,4,1,-1,1,-9,7,-1,-10,2,9,4,-5,-2,2],[-10,10,-9,7,9,9,6,-7,-8,-5,6,6,8,10,-10,1],[-7,3,3,7,9,-9,4,2,-2,2,-3,-2,2,8,-4,10],[-1,7,-5,7,4,9,-1,-10,9,2,10,2,6,2,10,-9],[-8,-6,-5,-9,10,-7,-10,-5,8,-1,-1,-2,5,-7,7,6],[6,-10,-7,-10,-6,10,-5,-3,2,3,8,-2,-1,-6,7,-4],[5,2,1,-1,-2,-3,3,1,-1,-3,-2,-10,4,-1,-1,3],[-9,10,-8,8,-9,6,8,-1,4,8,9,-8,5,5,4,-1]],[[-3,-2,-1,3,-3,6,-8,10,1,7,7,4,-5,-9,-6,-2],[3,-2,-8,6,3,3,-9,3,-1,7,-8,-2,-9,-3,-3,-4],[3,-1,-10,-2,-9,2,6,-7,6,6,6,-8,-1,9,-8,-2],[-10,1,2,-3,-6,10,-10,2,-10,1,-8,-10,-2,7,-6,2],[-2,8,-6,-6,5,6,-2,5,-7,-7,-7,-6,-9,-10,1,-5],[-5,-8,3,3,1,-5,-8,-4,-7,9,-1,-5,-9,-9,9,5],[4,-6,9,-5,9,-3,10,-1,2,5,7,8,-6,-8,9,-10],[-9,10,-6,-10,8,-1,5,-7,3,2,3,8,5,6,-9,6],[5,-6,4,-5,1,1,1,3,-2,-6,5,4,-9,-3,-9,6],[7,-2,-10,-3,6,-9,2,10,6,-8,-9,-10,-5,7,-2,-5],[-7,-1,-7,-1,8,7,-1,5,3,8,-8,-8,-1,-6,-10,-5],[-9,5,1,-6,-4,-9,1,2,-7,-6,1,7,-3,-9,5,9],[10,-7,-9,-8,-9,-8,2,6,2,-6,10,-7,8,3,9,7]],[[-5,10,9,-9,-6,-1,-8,-8,9,-5,9,1,9,-1,5,8],[2,5,6,10,-10,-8,7,1,2,-4,-10,-8,-10,-7,-5,-6],[1,-8,5,8,-10,6,-4,5,6,7,-6,-7,4,-1,9,7],[1,8,7,3,-4,-7,9,6,-3,3,10,8,-4,-6,-8,-4],[10,7,7,5,3,2,5,-7,-5,-10,10,10,6,-6,8,-3],[1,-4,-2,-10,4,-6,1,9,-4,10,6,-8,7,7,4,-2],[2,3,-6,10,6,8,9,-5,6,-7,-9,-7,8,10,7,-7],[9,-4,5,-6,10,-2,3,2,-5,4,-5,-10,6,-5,3,2],[3,8,2,9,-8,-10,10,-10,4,-1,-6,2,-3,5,-10,-10],[4,1,2,7,2,-10,-1,7,8,-4,1,8,-4,1,-1,1],[1,-3,-3,-4,8,-7,-8,-6,-4,-1,-6,-10,2,-8,-6,-2],[10,-9,-6,6,-9,-6,-9,1,1,-10,-3,-1,6,9,8,-9],[7,-9,-3,10,10,-8,8,-2,-3,8,-5,-10,8,-2,-3,3]],[[1,4,9,-7,-1,7,6,8,4,-5,7,-1,-5,1,6,-7],[-8,-2,-6,-5,3,6,-3,-9,10,-7,9,2,-1,-1,9,-3],[-8,3,5,1,-1,-7,1,1,-10,-10,6,-3,9,3,2,4],[-4,-6,-6,-7,5,-1,-10,10,1,-8,-4,-4,-3,-10,5,-6],[2,6,-8,6,6,10,10,-7,9,-7,-6,-5,-8,-5,6,1],[-1,7,1,5,-1,-5,-4,-3,8,6,-1,-3,4,1,7,-10],[-1,10,-2,-9,-9,-5,7,-3,-10,-6,-10,7,7,5,-9,4],[4,2,-8,-9,5,9,-4,4,-3,-4,-1,8,10,-4,10,9],[-4,2,-3,-1,6,10,-2,5,-7,8,-9,-6,10,8,-9,-6],[9,5,8,2,-5,6,-9,5,-2,-5,-1,-10,4,1,-8,-4],[-4,10,-4,7,-7,9,6,3,8,8,3,-8,-9,-8,-9,-5],[1,4,8,-5,6,10,-9,-7,2,-4,-5,-2,5,-9,-2,5],[10,9,3,-4,1,1,10,4,-3,-9,-1,3,10,-10,6,6]],[[-7,7,-2,-8,-8,10,9,10,-10,-10,-9,-9,-5,-1,-4,-9],[3,-2,-9,-5,-1,5,-7,-2,3,2,-5,8,9,2,-6,6],[-1,2,1,8,-2,-10,7,8,5,9,10,-1,9,-4,-8,-6],[-9,8,-8,1,-7,-9,-4,4,8,9,-5,6,-6,10,-3,3],[-5,-1,7,-2,-5,-1,-7,-8,10,-2,-2,10,-1,3,7,7],[7,4,1,10,-7,7,-6,1,-6,3,-1,5,-3,7,4,-1],[-1,-5,-1,10,-6,1,4,7,5,6,-3,10,-9,8,-3,6],[-4,-8,-6,2,-5,-3,5,9,-2,-5,-7,-2,6,-2,9,-2],[-9,-7,-9,8,-1,5,10,5,-10,-6,-7,-5,-8,-9,5,9],[2,-10,4,6,-6,1,-4,6,7,1,10,-9,3,7,-9,-1],[-2,-3,6,2,-10,-7,-9,8,-7,-4,-5,7,-10,3,9,-2],[4,9,-7,-1,6,-1,3,5,-10,-6,9,-10,-8,-8,-8,9],[-8,-1,1,-1,-2,-4,-2,6,7,7,-5,-4,-2,9,-5,-4]],[[-9,7,9,-9,-8,9,-3,4,-6,5,-9,-4,3,5,-4,-10],[-3,6,-3,-4,-7,5,-7,9,1,5,-5,5,4,6,6,-2],[-3,3,-3,-8,-10,-10,1,10,-3,2,-4,6,6,6,9,2],[-6,7,2,10,8,10,-1,-1,-5,-4,1,-5,-3,-10,-6,-4],[5,-4,9,-10,-3,-8,1,1,-6,3,5,6,-6,10,-9,8],[6,-3,-3,-1,5,5,1,-2,-10,-6,-2,5,-9,3,7,-3],[1,-5,-1,5,8,-2,5,-5,8,2,-4,-9,9,-10,-3,-7],[-1,1,1,-9,-7,9,6,6,5,-5,2,1,-8,-8,-6,-5],[9,10,-5,2,-2,3,3,4,-7,7,5,-1,-1,-1,-5,-5],[-6,6,-5,-1,-7,7,-4,-2,-9,10,-8,-4,9,-9,4,9],[-10,1,-5,-4,-9,-6,1,-3,6,-2,-4,5,-2,8,-8,-7],[-3,-6,1,1,-1,2,-5,-10,-8,-5,-9,-8,3,-8,-2,-9],[-3,3,5,5,-3,5,4,6,8,-6,2,-9,-9,-5,-1,-6]],[[-9,10,7,9,-4,5,-2,2,4,10,-4,-10,5,4,10,-2],[-2,-5,8,8,-2,10,6,5,-1,-6,3,8,1,-4,5,-2],[-8,6,4,-8,7,-10,9,2,10,3,-6,-1,-4,-8,3,-5],[-8,7,-3,6,-2,-2,4,8,-6,9,-3,-6,7,7,-3,-1],[5,3,-4,9,-5,-4,9,-5,5,4,4,9,6,-1,10,10],[-1,-5,-1,-8,7,7,6,-10,6,10,-6,9,-5,-8,2,10],[10,6,-10,-8,-8,3,-7,-6,-7,-10,7,4,2,7,-2,7],[4,1,-10,3,6,-4,8,-5,-10,9,-6,7,7,-2,-5,-10],[2,5,2,10,5,-10,-7,10,-10,3,2,-4,8,-7,-4,-3],[8,-8,7,8,-3,-5,-3,-8,-1,-1,-2,1,10,4,5,-2],[-3,-3,8,2,-4,-4,9,-2,-4,5,-5,-8,4,-10,-7,-2],[-3,-3,-10,4,2,-1,-1,-3,-3,1,-5,-6,8,8,10,-8],[-4,-4,5,-8,-8,-8,-9,4,-7,3,-3,-1,-7,-8,6,10]],[[6,6,-3,-8,1,-2,7,4,8,-8,-8,-1,7,-10,5,4],[-5,3,-5,1,-7,8,-8,9,-2,6,-5,3,-8,4,-4,-5],[1,8,-10,-1,3,-10,2,4,6,3,9,-3,8,2,-8,-2],[-6,-4,-1,-1,4,3,3,-1,-1,8,8,-9,-9,-2,-10,5],[-7,10,5,2,5,9,-5,6,-3,-8,-6,-1,7,-1,10,-3],[-8,-4,-6,-6,2,-10,-6,-4,9,-3,-8,1,10,4,-1,-6],[10,3,8,9,-5,-10,-3,1,6,-8,-10,4,2,-1,-7,-9],[-9,-4,-2,-9,-2,-9,3,9,-3,8,8,3,-1,1,1,6],[-4,9,5,-4,-6,4,-2,1,-3,-9,10,-1,8,1,-3,3],[9,-5,9,3,-10,-5,1,-8,-4,7,10,-6,-1,-2,-6,-6],[-5,9,-8,-1,9,-1,-3,-7,7,-2,-4,-7,-9,-3,-2,-10],[-8,2,1,-4,-9,-3,5,1,5,-9,6,-6,-5,-10,8,3],[-10,1,10,4,-2,4,-8,-7,2,4,2,-3,-10,1,6,1]],[[-2,-7,-10,4,7,-7,-4,-10,8,4,-5,-6,-1,-1,4,-3],[6,9,-3,6,-10,7,-7,8,-10,-5,9,-9,10,-9,4,1],[2,-6,2,4,-4,3,9,-7,6,-5,-5,5,-2,10,-6,6],[10,2,-3,-3,1,-6,-9,-9,-7,10,-7,-7,-9,7,-9,-3],[6,-10,-6,-3,1,5,-4,-5,-1,3,1,-8,-7,8,-1,-5],[-8,3,-10,-1,10,10,-4,-5,1,-10,-5,5,-7,-10,-3,3],[-9,-7,7,-9,8,8,-8,5,-8,4,-7,-7,-9,1,1,-5],[-4,-1,-4,5,2,2,-8,-1,-3,-2,-1,3,6,-2,-1,9],[-1,4,3,-7,-5,-6,7,-9,-10,1,10,3,-1,4,4,-5],[6,-2,1,5,-8,6,8,-6,-6,2,-2,-3,10,2,5,-10],[-9,9,10,3,-4,-5,-6,-1,-9,-10,7,-3,3,10,-5,8],[-1,-3,2,10,6,-8,-6,7,-1,-6,10,-5,5,2,4,-3],[8,7,-1,-4,4,-3,1,8,7,-10,3,2,1,-7,4,1]]], dtype = "int64")#candidate|6591|(13, 13, 16)|const|int64
var_6592 = relay.var("var_6592", dtype = "int64", shape = (13, 13, 16))#candidate|6592|(13, 13, 16)|var|int64
bop_6593 = relay.right_shift(const_6591.astype('int64'), relay.reshape(var_6592.astype('int64'), relay.shape_of(const_6591))) # shape=(13, 13, 16)
uop_6602 = relay.log10(bop_6593.astype('float32')) # shape=(13, 13, 16)
uop_6607 = relay.atan(uop_6602.astype('float32')) # shape=(13, 13, 16)
bop_6621 = relay.less(uop_6607.astype('bool'), relay.reshape(uop_6602.astype('bool'), relay.shape_of(uop_6607))) # shape=(13, 13, 16)
func_4053_call = mod.get_global_var('func_4053')
func_4058_call = mutated_mod.get_global_var('func_4058')
var_6625 = relay.var("var_6625", dtype = "float64", shape = ())#candidate|6625|()|var|float64
const_6626 = relay.const([-8.479170,-2.894884,-8.807043,6.642509,6.071377,-5.029554,0.351269,9.772897,-1.607604,5.245507,-7.205488,-0.808182,-1.860239,-3.920774,-9.301026,3.449163,3.978126,2.460829,6.816491,-8.354848,1.525181,9.611809,1.578770,-0.662172,-6.019026,-8.233247,-8.105296,-8.358012], dtype = "float64")#candidate|6626|(28,)|const|float64
var_6627 = relay.var("var_6627", dtype = "float64", shape = (180, 1))#candidate|6627|(180, 1)|var|float64
const_6628 = relay.const([[4.617612,-5.250315,3.992327,-9.995342,-3.052279,-1.548623,-6.968293,1.414032,-5.827691,5.860455,6.024348,8.072069,1.982176,8.195942,0.006947,5.090554,-9.862857,-8.442344,-0.679423,-9.138037,9.288742,5.919097,-9.609494,-8.092149,-4.389352,5.976125,9.265484,-6.087346,3.968968,-0.885750,2.433912,3.093133,8.782018,0.846111,-4.739236,-4.259714,8.386393,3.357030,6.106375,-5.779310,3.791843,4.939390,-5.880718,-3.388856,0.595524,5.910951,-3.772906,4.450108,-0.275601,3.035533,-8.413437,-7.604875,3.425313,4.192184,7.048709,3.271660,6.748336,0.574315,-5.924042,4.257226,2.246367,-1.818854,-1.890579,1.875335,-7.067847,1.542652,5.007045,-4.649637,-6.453666,1.647043,6.651971,-6.434822,6.123246,9.281529,2.865668,9.233651,2.524051,5.398537,2.252745,-7.390724,1.811874,9.997093,2.920531,-0.982599,0.368026,8.976030,-5.177193,-1.738973,5.051880,8.614287],[-0.686113,7.669450,-4.086827,6.540421,-3.895318,5.165692,-2.239181,-6.729603,3.121842,9.365657,-5.798767,9.468291,-6.611213,-4.408588,9.597587,8.735051,-8.483234,0.349131,0.854754,1.431741,-7.547544,9.147345,2.270115,-5.720205,-4.293613,5.590473,-5.056836,2.798696,-7.870873,5.435738,4.101250,-8.547662,5.140626,-3.050395,-1.830950,-1.216159,7.145402,9.217860,8.262443,0.925731,5.387880,-5.443682,8.957421,7.637302,6.440917,-1.675654,6.325926,0.731555,-6.109133,1.360665,6.636569,-4.711599,8.586447,7.288746,0.650485,6.844454,0.664203,0.299570,6.442349,7.642767,1.251521,-5.179265,-6.589509,5.817237,7.829278,8.412223,7.036607,1.909563,-6.367862,3.514078,5.087992,-0.817704,4.073671,-5.058306,-9.730879,3.024201,1.289175,-9.156608,4.171332,-7.498210,-3.682203,1.730132,0.033399,4.291922,9.178489,-2.595514,8.945922,-9.655363,-5.404735,4.693230],[-0.681967,-0.329601,-7.042454,8.073116,-9.292402,7.671521,4.824501,-1.920137,6.486867,-8.511667,2.215236,-7.791452,-8.627945,0.552493,2.147321,5.823115,6.619333,7.240427,5.128613,-0.242506,-2.213657,-0.940898,-7.293876,0.651717,-2.523854,9.805490,-4.716552,-7.960050,-9.509610,9.172409,3.847746,1.061319,-4.228739,-9.309583,7.152029,4.216653,-5.130814,2.644726,6.831425,3.321568,1.877045,7.143056,-4.131222,-2.389048,0.450251,-0.348033,-1.868645,9.099508,-5.279587,-2.158624,-5.760881,2.391377,-1.196708,-5.233473,4.728762,1.194246,-1.805352,-5.150658,2.082563,8.736484,-2.858844,8.825872,4.359216,9.778674,-4.772780,2.426897,-1.582321,-3.966949,8.401848,-7.706051,-2.080558,6.222983,-9.617844,1.828864,-6.053460,-6.870235,-2.764441,-9.343360,-7.701195,5.316901,1.527630,-0.200820,2.061315,-5.580575,8.800433,-9.721808,1.965716,-1.199705,3.188436,1.463824],[-2.399611,2.988803,3.207464,-8.756448,1.635009,-2.003385,-6.611557,-2.316483,5.592590,-7.039472,1.309833,-7.795506,1.838183,-8.849901,-2.287259,-4.875082,9.773606,8.586760,0.237503,6.268227,7.468645,-9.740762,-7.403562,-7.754163,0.838381,-9.022236,7.379833,1.484521,5.735937,7.625777,4.584042,-5.968926,2.220968,3.223378,2.218058,-0.233173,8.444349,-2.103716,0.167439,5.149414,7.739299,-9.061481,4.778196,5.067120,0.512728,-5.111203,2.253338,-7.824190,0.588346,9.496425,-6.014755,1.280465,-9.637306,2.907280,-8.542017,0.716896,-7.990506,-4.104064,2.902030,-6.805977,7.501962,-2.200184,1.003079,0.076515,-9.482288,9.243738,-8.703538,-5.227601,-1.247749,1.941445,0.114634,-7.102759,-1.085701,8.567708,8.448856,-1.002062,-0.592340,8.614827,5.071116,-7.375496,6.118956,-1.197560,5.786764,9.858655,-3.297594,-8.932405,8.933048,9.224924,-6.412357,5.079692],[-6.170353,-3.490700,-7.020962,-3.306578,-5.357720,-9.725083,-3.970758,-6.065677,0.891510,7.545254,-9.046672,6.983155,7.828274,7.779252,8.000700,0.261631,-2.675001,5.906663,6.424496,4.696727,-6.255941,0.016371,-2.819438,-4.488069,7.890255,-8.464526,-2.263695,4.594739,-3.922985,6.104260,-3.429724,-9.349838,-9.054752,2.903341,7.900130,6.796035,-2.599717,0.796517,-7.239839,9.840788,5.009445,3.927351,4.559682,2.476128,3.240297,-7.576596,7.756187,8.029969,-3.037221,1.136510,0.037824,5.149091,-3.448919,-4.999649,2.801810,-9.836605,3.716631,-3.678177,7.773056,8.578651,-3.120791,-7.753133,-3.677046,3.394072,-5.848574,-8.853920,7.519563,-4.585539,-8.003757,2.175788,-4.914895,2.509805,9.874635,-1.164056,2.345682,-0.580735,6.788701,-1.390700,-8.917600,-0.026586,-9.332587,-3.384083,1.205557,4.111201,0.917806,0.992715,9.036554,-3.050979,-9.723415,2.169536]], dtype = "float64")#candidate|6628|(5, 90)|const|float64
call_6624 = relay.TupleGetItem(func_4053_call(relay.reshape(var_6625.astype('float64'), []), relay.reshape(const_6626.astype('float64'), [1, 4, 7]), relay.reshape(var_6627.astype('float64'), [180,]), relay.reshape(const_6628.astype('float64'), [450,]), ), 4)
call_6629 = relay.TupleGetItem(func_4058_call(relay.reshape(var_6625.astype('float64'), []), relay.reshape(const_6626.astype('float64'), [1, 4, 7]), relay.reshape(var_6627.astype('float64'), [180,]), relay.reshape(const_6628.astype('float64'), [450,]), ), 4)
output = relay.Tuple([bop_6621,call_6624,var_6625,const_6626,var_6627,const_6628,])
output2 = relay.Tuple([bop_6621,call_6629,var_6625,const_6626,var_6627,const_6628,])
func_6636 = relay.Function([var_6592,var_6625,var_6627,], output)
mod['func_6636'] = func_6636
mod = relay.transform.InferType()(mod)
mutated_mod['func_6636'] = func_6636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6636_call = mutated_mod.get_global_var('func_6636')
var_6638 = relay.var("var_6638", dtype = "int64", shape = (13, 13, 16))#candidate|6638|(13, 13, 16)|var|int64
var_6639 = relay.var("var_6639", dtype = "float64", shape = ())#candidate|6639|()|var|float64
var_6640 = relay.var("var_6640", dtype = "float64", shape = (180, 1))#candidate|6640|(180, 1)|var|float64
call_6637 = func_6636_call(var_6638,var_6639,var_6640,)
output = call_6637
func_6641 = relay.Function([var_6638,var_6639,var_6640,], output)
mutated_mod['func_6641'] = func_6641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_907_call = mod.get_global_var('func_907')
func_908_call = mutated_mod.get_global_var('func_908')
call_6667 = relay.TupleGetItem(func_907_call(), 0)
call_6668 = relay.TupleGetItem(func_908_call(), 0)
output = call_6667
output2 = call_6668
func_6691 = relay.Function([], output)
mod['func_6691'] = func_6691
mod = relay.transform.InferType()(mod)
mutated_mod['func_6691'] = func_6691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6691_call = mutated_mod.get_global_var('func_6691')
call_6692 = func_6691_call()
output = call_6692
func_6693 = relay.Function([], output)
mutated_mod['func_6693'] = func_6693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6701 = relay.var("var_6701", dtype = "float32", shape = (15, 6, 1))#candidate|6701|(15, 6, 1)|var|float32
uop_6702 = relay.sigmoid(var_6701.astype('float32')) # shape=(15, 6, 1)
output = relay.Tuple([uop_6702,])
output2 = relay.Tuple([uop_6702,])
func_6706 = relay.Function([var_6701,], output)
mod['func_6706'] = func_6706
mod = relay.transform.InferType()(mod)
mutated_mod['func_6706'] = func_6706
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6707 = relay.var("var_6707", dtype = "float32", shape = (15, 6, 1))#candidate|6707|(15, 6, 1)|var|float32
func_6706_call = mutated_mod.get_global_var('func_6706')
call_6708 = func_6706_call(var_6707)
output = call_6708
func_6709 = relay.Function([var_6707], output)
mutated_mod['func_6709'] = func_6709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5905_call = mod.get_global_var('func_5905')
func_5907_call = mutated_mod.get_global_var('func_5907')
call_6736 = relay.TupleGetItem(func_5905_call(), 0)
call_6737 = relay.TupleGetItem(func_5907_call(), 0)
uop_6742 = relay.atan(call_6736.astype('float64')) # shape=(2, 1, 9)
uop_6744 = relay.atan(call_6737.astype('float64')) # shape=(2, 1, 9)
uop_6749 = relay.sqrt(uop_6742.astype('float32')) # shape=(2, 1, 9)
uop_6751 = relay.sqrt(uop_6744.astype('float32')) # shape=(2, 1, 9)
func_2119_call = mod.get_global_var('func_2119')
func_2122_call = mutated_mod.get_global_var('func_2122')
var_6757 = relay.var("var_6757", dtype = "float32", shape = (26,))#candidate|6757|(26,)|var|float32
const_6758 = relay.const([[8.409288,-1.576598,1.597212,-5.220102,6.078941,5.768477,-5.046036,-2.117174,-0.605706,-8.736334],[-4.787292,3.796290,-8.454092,6.782271,3.351468,8.058774,9.170701,2.231448,-5.675623,-8.280322],[-4.697394,-1.950573,0.882895,-7.146619,1.780011,-2.843442,5.777603,5.802008,-5.244444,8.055446],[-2.807137,-9.743611,-7.822953,4.348331,-0.731570,-2.592477,5.528838,1.827867,-8.147610,5.415546],[-6.755033,1.133376,7.582867,-3.500995,3.239829,-3.228253,-6.394832,-6.583893,-3.414536,0.283662],[9.667612,3.238483,-7.016015,3.061940,2.820821,8.910186,-3.863435,4.185539,4.106049,-2.824546],[3.524972,7.748625,0.953007,-5.463305,3.305049,-4.944851,-7.530023,0.288358,8.683310,8.515316],[7.021087,-6.691605,8.833160,-1.901215,2.920117,6.349371,5.130637,-7.370713,-3.322662,-6.119800],[-7.986411,-1.598644,3.718618,-9.546065,-4.467473,6.995157,-6.769168,-6.061251,9.366854,-5.716638],[2.427465,-1.465233,-9.980111,6.598187,1.416954,-5.747044,2.078383,-9.495817,8.955405,9.545161],[-3.163989,6.242008,-7.849980,-3.460831,-3.636467,1.283956,2.589957,-5.258402,-4.636555,-3.438686],[-2.712400,-1.603257,-9.081082,-8.229937,0.359639,8.788792,-9.523269,-5.405761,-4.598462,-3.670526],[4.144303,-8.345973,0.690003,2.502858,0.135559,-5.266647,-8.102482,6.191451,6.706517,-3.283200]], dtype = "float32")#candidate|6758|(13, 10)|const|float32
call_6756 = relay.TupleGetItem(func_2119_call(relay.reshape(var_6757.astype('float32'), [2, 13, 1]), relay.reshape(const_6758.astype('float32'), [2, 13, 5]), ), 2)
call_6759 = relay.TupleGetItem(func_2122_call(relay.reshape(var_6757.astype('float32'), [2, 13, 1]), relay.reshape(const_6758.astype('float32'), [2, 13, 5]), ), 2)
func_4704_call = mod.get_global_var('func_4704')
func_4705_call = mutated_mod.get_global_var('func_4705')
call_6761 = func_4704_call()
call_6762 = func_4704_call()
output = relay.Tuple([uop_6749,call_6756,var_6757,const_6758,call_6761,])
output2 = relay.Tuple([uop_6751,call_6759,var_6757,const_6758,call_6762,])
func_6768 = relay.Function([var_6757,], output)
mod['func_6768'] = func_6768
mod = relay.transform.InferType()(mod)
var_6769 = relay.var("var_6769", dtype = "float32", shape = (26,))#candidate|6769|(26,)|var|float32
output = func_6768(var_6769)
func_6770 = relay.Function([var_6769], output)
mutated_mod['func_6770'] = func_6770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4913_call = mod.get_global_var('func_4913')
func_4914_call = mutated_mod.get_global_var('func_4914')
call_6779 = relay.TupleGetItem(func_4913_call(), 0)
call_6780 = relay.TupleGetItem(func_4914_call(), 0)
output = call_6779
output2 = call_6780
func_6790 = relay.Function([], output)
mod['func_6790'] = func_6790
mod = relay.transform.InferType()(mod)
mutated_mod['func_6790'] = func_6790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6790_call = mutated_mod.get_global_var('func_6790')
call_6791 = func_6790_call()
output = call_6791
func_6792 = relay.Function([], output)
mutated_mod['func_6792'] = func_6792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4591_call = mod.get_global_var('func_4591')
func_4593_call = mutated_mod.get_global_var('func_4593')
call_6844 = relay.TupleGetItem(func_4591_call(), 0)
call_6845 = relay.TupleGetItem(func_4593_call(), 0)
func_4267_call = mod.get_global_var('func_4267')
func_4270_call = mutated_mod.get_global_var('func_4270')
var_6882 = relay.var("var_6882", dtype = "uint8", shape = (196,))#candidate|6882|(196,)|var|uint8
call_6881 = relay.TupleGetItem(func_4267_call(relay.reshape(var_6882.astype('uint8'), [196,])), 0)
call_6883 = relay.TupleGetItem(func_4270_call(relay.reshape(var_6882.astype('uint8'), [196,])), 0)
output = relay.Tuple([call_6844,call_6881,var_6882,])
output2 = relay.Tuple([call_6845,call_6883,var_6882,])
func_6896 = relay.Function([var_6882,], output)
mod['func_6896'] = func_6896
mod = relay.transform.InferType()(mod)
var_6897 = relay.var("var_6897", dtype = "uint8", shape = (196,))#candidate|6897|(196,)|var|uint8
output = func_6896(var_6897)
func_6898 = relay.Function([var_6897], output)
mutated_mod['func_6898'] = func_6898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6093_call = mod.get_global_var('func_6093')
func_6094_call = mutated_mod.get_global_var('func_6094')
call_6908 = relay.TupleGetItem(func_6093_call(), 1)
call_6909 = relay.TupleGetItem(func_6094_call(), 1)
output = call_6908
output2 = call_6909
func_6915 = relay.Function([], output)
mod['func_6915'] = func_6915
mod = relay.transform.InferType()(mod)
output = func_6915()
func_6916 = relay.Function([], output)
mutated_mod['func_6916'] = func_6916
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6975 = relay.var("var_6975", dtype = "float64", shape = (11, 1, 4))#candidate|6975|(11, 1, 4)|var|float64
uop_6976 = relay.atan(var_6975.astype('float64')) # shape=(11, 1, 4)
uop_6980 = relay.exp(var_6975.astype('float32')) # shape=(11, 1, 4)
output = relay.Tuple([uop_6976,uop_6980,])
output2 = relay.Tuple([uop_6976,uop_6980,])
func_6987 = relay.Function([var_6975,], output)
mod['func_6987'] = func_6987
mod = relay.transform.InferType()(mod)
var_6988 = relay.var("var_6988", dtype = "float64", shape = (11, 1, 4))#candidate|6988|(11, 1, 4)|var|float64
output = func_6987(var_6988)
func_6989 = relay.Function([var_6988], output)
mutated_mod['func_6989'] = func_6989
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6991 = relay.var("var_6991", dtype = "float32", shape = (11, 5, 14))#candidate|6991|(11, 5, 14)|var|float32
var_6992 = relay.var("var_6992", dtype = "float32", shape = (11, 5, 14))#candidate|6992|(11, 5, 14)|var|float32
bop_6993 = relay.power(var_6991.astype('float32'), relay.reshape(var_6992.astype('float32'), relay.shape_of(var_6991))) # shape=(11, 5, 14)
func_2165_call = mod.get_global_var('func_2165')
func_2167_call = mutated_mod.get_global_var('func_2167')
call_6996 = relay.TupleGetItem(func_2165_call(), 0)
call_6997 = relay.TupleGetItem(func_2167_call(), 0)
var_7033 = relay.var("var_7033", dtype = "float32", shape = (11, 5, 14))#candidate|7033|(11, 5, 14)|var|float32
bop_7034 = relay.right_shift(bop_6993.astype('int16'), relay.reshape(var_7033.astype('int16'), relay.shape_of(bop_6993))) # shape=(11, 5, 14)
uop_7045 = relay.exp(bop_6993.astype('float64')) # shape=(11, 5, 14)
output = relay.Tuple([call_6996,bop_7034,uop_7045,])
output2 = relay.Tuple([call_6997,bop_7034,uop_7045,])
func_7082 = relay.Function([var_6991,var_6992,var_7033,], output)
mod['func_7082'] = func_7082
mod = relay.transform.InferType()(mod)
var_7083 = relay.var("var_7083", dtype = "float32", shape = (11, 5, 14))#candidate|7083|(11, 5, 14)|var|float32
var_7084 = relay.var("var_7084", dtype = "float32", shape = (11, 5, 14))#candidate|7084|(11, 5, 14)|var|float32
var_7085 = relay.var("var_7085", dtype = "float32", shape = (11, 5, 14))#candidate|7085|(11, 5, 14)|var|float32
output = func_7082(var_7083,var_7084,var_7085,)
func_7086 = relay.Function([var_7083,var_7084,var_7085,], output)
mutated_mod['func_7086'] = func_7086
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7088 = relay.const(False, dtype = "bool")#candidate|7088|()|const|bool
const_7089 = relay.const([[[True,False,True,True,True,False,True,False,True,True,False]],[[False,True,True,True,False,True,True,True,False,False,False]],[[False,False,False,True,False,False,True,False,True,True,False]],[[False,False,True,True,True,True,False,True,True,True,False]],[[False,False,True,False,True,False,False,True,False,False,False]],[[False,True,False,False,True,False,True,False,False,False,False]],[[True,True,True,True,True,False,False,False,True,True,False]]], dtype = "bool")#candidate|7089|(7, 1, 11)|const|bool
bop_7090 = relay.logical_and(const_7088.astype('bool'), const_7089.astype('bool')) # shape=(7, 1, 11)
output = bop_7090
output2 = bop_7090
func_7093 = relay.Function([], output)
mod['func_7093'] = func_7093
mod = relay.transform.InferType()(mod)
mutated_mod['func_7093'] = func_7093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7093_call = mutated_mod.get_global_var('func_7093')
call_7094 = func_7093_call()
output = call_7094
func_7095 = relay.Function([], output)
mutated_mod['func_7095'] = func_7095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3043_call = mod.get_global_var('func_3043')
func_3044_call = mutated_mod.get_global_var('func_3044')
call_7260 = relay.TupleGetItem(func_3043_call(), 2)
call_7261 = relay.TupleGetItem(func_3044_call(), 2)
output = call_7260
output2 = call_7261
func_7289 = relay.Function([], output)
mod['func_7289'] = func_7289
mod = relay.transform.InferType()(mod)
mutated_mod['func_7289'] = func_7289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7289_call = mutated_mod.get_global_var('func_7289')
call_7290 = func_7289_call()
output = call_7290
func_7291 = relay.Function([], output)
mutated_mod['func_7291'] = func_7291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7334 = relay.var("var_7334", dtype = "int8", shape = (3, 2, 13))#candidate|7334|(3, 2, 13)|var|int8
var_7335 = relay.var("var_7335", dtype = "int8", shape = (3, 2, 13))#candidate|7335|(3, 2, 13)|var|int8
bop_7336 = relay.left_shift(var_7334.astype('int8'), relay.reshape(var_7335.astype('int8'), relay.shape_of(var_7334))) # shape=(3, 2, 13)
output = bop_7336
output2 = bop_7336
func_7339 = relay.Function([var_7334,var_7335,], output)
mod['func_7339'] = func_7339
mod = relay.transform.InferType()(mod)
mutated_mod['func_7339'] = func_7339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7339_call = mutated_mod.get_global_var('func_7339')
var_7341 = relay.var("var_7341", dtype = "int8", shape = (3, 2, 13))#candidate|7341|(3, 2, 13)|var|int8
var_7342 = relay.var("var_7342", dtype = "int8", shape = (3, 2, 13))#candidate|7342|(3, 2, 13)|var|int8
call_7340 = func_7339_call(var_7341,var_7342,)
output = call_7340
func_7343 = relay.Function([var_7341,var_7342,], output)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3452_call = mod.get_global_var('func_3452')
func_3453_call = mutated_mod.get_global_var('func_3453')
call_7347 = relay.TupleGetItem(func_3452_call(), 0)
call_7348 = relay.TupleGetItem(func_3453_call(), 0)
func_6915_call = mod.get_global_var('func_6915')
func_6916_call = mutated_mod.get_global_var('func_6916')
call_7359 = func_6915_call()
call_7360 = func_6915_call()
func_4746_call = mod.get_global_var('func_4746')
func_4747_call = mutated_mod.get_global_var('func_4747')
call_7380 = relay.TupleGetItem(func_4746_call(), 2)
call_7381 = relay.TupleGetItem(func_4747_call(), 2)
output = relay.Tuple([call_7347,call_7359,call_7380,])
output2 = relay.Tuple([call_7348,call_7360,call_7381,])
func_7382 = relay.Function([], output)
mod['func_7382'] = func_7382
mod = relay.transform.InferType()(mod)
output = func_7382()
func_7383 = relay.Function([], output)
mutated_mod['func_7383'] = func_7383
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7437 = relay.const([[[-5.100346,-3.527346,1.849215,6.133340,-3.987176,8.516998,-4.743068,7.108270,4.689375,0.290143,-6.774168,-4.799854,3.923207,6.943775],[-5.384160,-7.804332,-8.960240,0.680594,-3.286930,-1.439894,7.968540,-0.380133,-9.304534,-9.506898,-1.280736,-7.720804,6.291754,6.685791],[-1.584062,-1.335632,9.961854,-7.260122,4.480664,6.744417,-5.419553,-1.737802,1.797197,8.481864,-6.881085,-3.279415,2.612539,1.396179],[8.115076,-6.019927,7.624714,-9.914961,1.541337,-1.975095,8.290812,-7.545223,8.739685,3.932022,7.444189,-3.037252,-3.898202,-2.016378],[-2.703742,-1.236552,5.535526,1.365575,5.355025,0.912021,-8.610042,8.598843,-0.023238,-5.428151,-4.973216,-3.490954,-6.428443,0.072475],[9.500860,8.988257,-3.515193,8.584960,-0.405484,-5.299440,8.924537,-0.523807,-6.517905,5.263241,5.965756,-8.704061,5.244741,-2.175497],[-9.335891,-0.628860,4.777687,6.225684,6.011624,7.588257,4.514307,7.158398,-0.572850,7.233883,9.337188,5.823686,-9.150022,-4.144703],[-5.744344,3.514914,-2.383265,4.418845,2.957439,5.416288,9.345883,-0.935470,6.584934,6.267347,6.303238,-4.969500,3.386835,-3.769024],[4.278592,1.297748,6.374194,-5.627308,-0.456220,8.474132,-5.494127,-9.255014,-9.877237,6.967911,-8.471799,2.891356,2.811146,-1.060357]],[[9.498580,-8.468342,1.140562,-3.176376,-2.880050,5.325515,-0.929374,5.307563,0.837368,7.053280,-4.223830,4.096749,1.452965,9.022674],[-9.085811,-3.413371,-9.173303,4.425971,-5.092287,-0.853637,-8.367642,-2.212150,-1.567233,-5.347666,5.584992,0.309536,-1.804929,5.948516],[8.842075,-4.103103,-4.239280,8.058773,9.686552,4.791879,7.116623,-3.219788,9.220674,-9.669265,-8.346395,5.076213,-4.826004,-6.202834],[-8.471429,6.703276,-5.921430,9.426049,-7.571064,4.026539,5.015703,9.105584,-4.950758,5.787655,-1.319123,8.731041,-6.899560,3.123673],[-8.994864,4.791990,7.609965,-2.600389,-5.235995,-9.301188,5.961890,-5.575439,-2.208898,7.518379,0.166935,-3.153951,-3.869246,0.121899],[1.569304,-8.830082,-3.405582,-6.020504,-0.367316,2.858450,-3.027150,0.220400,0.017516,2.110665,6.354091,-6.434608,3.014001,3.545436],[-9.075217,-9.792221,4.152893,8.839176,-8.426407,6.106743,8.527872,5.036909,-8.673291,4.056172,-0.108524,-2.065340,3.989248,-5.738775],[2.257000,-4.011830,-1.305608,2.172948,4.480536,6.831909,-1.994475,-2.492471,1.140869,-2.270222,-4.181253,4.498695,-5.532928,8.562006],[-5.384610,-7.355543,8.212163,-6.103792,8.299554,1.450085,-5.738046,-2.261164,4.124789,-5.213756,-3.916095,-2.098919,-0.394764,3.602051]],[[4.438389,-4.747033,-5.521485,-1.983924,-4.642397,-4.352646,-5.614584,-1.507640,-0.275655,-1.677998,-1.960129,9.409007,8.362744,6.023949],[1.336723,-9.322606,0.183315,9.620761,6.579892,0.861419,-8.331911,2.824504,9.527576,4.911001,-0.007380,1.318716,2.706098,0.269658],[8.884988,-2.760449,9.302106,2.067074,-1.947783,-1.504213,-4.050949,7.982262,3.648102,-4.891437,-5.615581,0.670919,5.002656,4.959171],[0.228126,2.694634,-9.690578,8.393717,-0.138576,-2.774791,8.190018,-1.919191,4.116668,-4.826249,-4.872523,1.766692,5.396917,5.487588],[-2.363721,4.338399,7.204321,-6.949425,-1.739159,7.596569,-4.425026,3.038502,-8.124438,-5.653225,0.797626,4.018987,7.126246,6.976068],[4.755009,1.075388,0.949392,3.067039,8.373749,-9.989471,1.345323,-8.740785,-7.079433,-2.442889,3.741174,-6.163092,6.251951,-1.780083],[-7.488821,0.565694,-6.950762,6.337860,1.644821,-7.831228,-8.481630,6.314225,-4.191412,-7.190905,0.097380,2.603365,0.225290,-8.332584],[4.764591,2.799954,-9.049236,5.668456,6.723483,-4.027038,9.757558,4.550255,-1.784355,-6.040414,-7.251658,3.223553,1.944349,-8.717514],[-0.949079,2.043959,7.184969,5.264145,-5.737635,-5.624596,-9.422729,-2.767117,6.705601,7.476658,-0.937679,-5.400263,-3.645732,6.260838]],[[-5.610779,-7.056796,-8.413985,9.099400,-8.406185,8.326314,2.786748,-9.747029,-2.820536,-9.044434,-4.444322,5.981818,3.554592,5.916100],[7.164552,3.226094,-3.416463,-9.798594,1.673252,-7.585459,0.763803,-0.262002,9.681571,-0.321465,-2.695410,5.473719,-7.715023,4.260149],[-8.823822,-9.637590,5.269992,-9.172412,8.689735,-7.475391,-9.268515,1.676370,-3.700696,-6.976735,-6.469648,-6.659049,4.139873,-4.906197],[-5.629279,1.408675,-0.646727,4.449974,9.409167,-4.869948,-9.202537,-7.479474,1.603859,-1.044154,3.450894,-1.270684,7.304135,-7.208694],[-3.662224,6.789965,5.009408,-6.312426,-6.248249,3.396967,5.212881,-9.633123,9.381962,-2.971237,-0.540420,-3.803234,7.599733,-1.330049],[8.586805,-3.807748,3.101572,7.121766,-5.966974,-4.391925,1.226983,4.118146,1.225058,-8.131355,-3.855918,-0.255491,-7.617344,-3.581443],[5.396673,-0.336350,-5.982160,-7.703900,-1.563666,-2.451033,0.900808,0.342861,-8.637305,1.034127,1.386495,-2.423970,-6.709824,-1.465073],[-0.135736,7.794743,8.511319,-9.823184,-5.982754,8.326654,-8.326511,0.113085,8.343139,-5.299338,5.847843,4.133656,-4.819522,-0.027868],[-0.740168,7.066442,-9.925745,-7.708840,-4.710159,9.317397,-1.091966,-0.247693,-8.783729,-4.464378,-9.578671,4.048937,1.501760,-4.657944]]], dtype = "float64")#candidate|7437|(4, 9, 14)|const|float64
uop_7438 = relay.sin(const_7437.astype('float64')) # shape=(4, 9, 14)
output = uop_7438
output2 = uop_7438
func_7442 = relay.Function([], output)
mod['func_7442'] = func_7442
mod = relay.transform.InferType()(mod)
output = func_7442()
func_7443 = relay.Function([], output)
mutated_mod['func_7443'] = func_7443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3014_call = mod.get_global_var('func_3014')
func_3015_call = mutated_mod.get_global_var('func_3015')
call_7464 = relay.TupleGetItem(func_3014_call(), 0)
call_7465 = relay.TupleGetItem(func_3015_call(), 0)
func_1922_call = mod.get_global_var('func_1922')
func_1923_call = mutated_mod.get_global_var('func_1923')
call_7468 = relay.TupleGetItem(func_1922_call(), 0)
call_7469 = relay.TupleGetItem(func_1923_call(), 0)
func_3403_call = mod.get_global_var('func_3403')
func_3407_call = mutated_mod.get_global_var('func_3407')
const_7471 = relay.const([-3,-7,-6,6,9,9,-6,-10,-9,6,-2,4,6,-10,-7,4,10,10,-2,-7,8,2,8,7,-9,-9,-7,-2,4,7,1,-3,3,-8,-8,5,-2,10,-8,-7,3,9,6,-6,-5,4,-6,-8,8,3,10,2,4,-2,-2,-1,-3,-8,4,-9,-6,-5,-10,3,-9,-6,6,-1,-1,-3,9,1,-6,1,2,1,5,-2,8,-4,2,4,-7,10,-7,4,-9,-10,-3,-7,2,-5,-3,-5,4,6,9,-6,6,-8,-9,10,9,-4,-10,-9,8,-1,-5,-2,6,-7,-9,-5,8,-9,-8,-4,-9,-1,-1,3,-6,-2,1,-10,-3,5,-9,-10,-6,2,10,-2,6,9,-4,9,-7,1,-7,8,-5,6,5,-10,5,-6,-10,5,10,5,8,-3,7,6,2,-3,-9,2,-5,5,-6,6,-7,-6,-8,-10,7,3,7,5,5,8,-9,6,-5,-3,-1,-9,-3,-5,5,9,-1,3,2,-7,8,-1,-10,-8,-7,5,3,8], dtype = "uint8")#candidate|7471|(196,)|const|uint8
var_7472 = relay.var("var_7472", dtype = "float64", shape = (1274,))#candidate|7472|(1274,)|var|float64
call_7470 = relay.TupleGetItem(func_3403_call(relay.reshape(const_7471.astype('uint8'), [196,]), relay.reshape(var_7472.astype('float64'), [1274,]), ), 12)
call_7473 = relay.TupleGetItem(func_3407_call(relay.reshape(const_7471.astype('uint8'), [196,]), relay.reshape(var_7472.astype('float64'), [1274,]), ), 12)
output = relay.Tuple([call_7464,call_7468,call_7470,const_7471,var_7472,])
output2 = relay.Tuple([call_7465,call_7469,call_7473,const_7471,var_7472,])
func_7477 = relay.Function([var_7472,], output)
mod['func_7477'] = func_7477
mod = relay.transform.InferType()(mod)
var_7478 = relay.var("var_7478", dtype = "float64", shape = (1274,))#candidate|7478|(1274,)|var|float64
output = func_7477(var_7478)
func_7479 = relay.Function([var_7478], output)
mutated_mod['func_7479'] = func_7479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6475_call = mod.get_global_var('func_6475')
func_6477_call = mutated_mod.get_global_var('func_6477')
call_7515 = relay.TupleGetItem(func_6475_call(), 0)
call_7516 = relay.TupleGetItem(func_6477_call(), 0)
func_4811_call = mod.get_global_var('func_4811')
func_4814_call = mutated_mod.get_global_var('func_4814')
var_7526 = relay.var("var_7526", dtype = "uint8", shape = (7, 28))#candidate|7526|(7, 28)|var|uint8
call_7525 = relay.TupleGetItem(func_4811_call(relay.reshape(var_7526.astype('uint8'), [196,])), 5)
call_7527 = relay.TupleGetItem(func_4814_call(relay.reshape(var_7526.astype('uint8'), [196,])), 5)
uop_7534 = relay.asin(var_7526.astype('float32')) # shape=(7, 28)
output = relay.Tuple([call_7515,call_7525,uop_7534,])
output2 = relay.Tuple([call_7516,call_7527,uop_7534,])
F = relay.Function([var_7526,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7526,], output2)
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
