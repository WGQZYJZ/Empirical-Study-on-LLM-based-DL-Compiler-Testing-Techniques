import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_505 = relay.const([[[9,-9,-7],[1,3,8],[6,-1,3],[7,-6,8],[-5,10,2],[-9,-7,5],[7,8,3],[-8,-5,-4],[-8,-2,9],[4,-4,1],[-6,-8,-1],[8,10,-6],[5,-1,-2],[-9,-5,5],[-10,1,-3]],[[-1,-3,3],[1,-1,-9],[-1,2,-5],[7,7,4],[8,-10,9],[1,4,6],[-9,-9,7],[9,2,-9],[6,-10,10],[4,9,6],[9,9,-3],[-3,3,3],[9,7,-1],[-8,-2,3],[-2,9,3]],[[1,-5,7],[5,-10,-1],[-8,3,4],[2,5,2],[-8,-5,8],[-4,-1,-9],[-7,-8,5],[-8,-2,6],[6,-9,4],[9,6,8],[-3,2,3],[2,-8,-7],[-2,5,7],[-9,9,-6],[-1,-4,-10]],[[-10,-7,6],[-8,10,-9],[-10,-3,2],[-6,2,2],[8,-2,10],[-7,4,-7],[-3,-9,2],[1,6,4],[-1,10,6],[3,5,10],[-9,8,-2],[4,-9,-10],[10,10,5],[-3,-4,2],[-6,8,10]],[[9,-5,-5],[-1,2,-1],[-8,4,-6],[-3,5,-3],[-9,-2,4],[-5,3,1],[6,-6,-1],[-3,-9,-8],[5,-5,1],[7,-1,-9],[3,10,-5],[-4,1,1],[9,3,-10],[5,4,-6],[-8,-5,4]]], dtype = "int8")#candidate|505|(5, 15, 3)|const|int8
var_506 = relay.var("var_506", dtype = "int8", shape = (5, 15, 3))#candidate|506|(5, 15, 3)|var|int8
bop_507 = relay.right_shift(const_505.astype('int8'), relay.reshape(var_506.astype('int8'), relay.shape_of(const_505))) # shape=(5, 15, 3)
output = bop_507
output2 = bop_507
func_517 = relay.Function([var_506,], output)
mod['func_517'] = func_517
mod = relay.transform.InferType()(mod)
mutated_mod['func_517'] = func_517
mutated_mod = relay.transform.InferType()(mutated_mod)
var_518 = relay.var("var_518", dtype = "int8", shape = (5, 15, 3))#candidate|518|(5, 15, 3)|var|int8
func_517_call = mutated_mod.get_global_var('func_517')
call_519 = func_517_call(var_518)
output = call_519
func_520 = relay.Function([var_518], output)
mutated_mod['func_520'] = func_520
mutated_mod = relay.transform.InferType()(mutated_mod)
const_554 = relay.const([[[0.068267,-3.317222],[-9.664475,-6.278885],[2.131514,-7.241374],[-1.650289,7.661148],[4.081407,3.969934],[-3.896322,3.705441],[2.336945,-9.506352],[9.734265,8.192919],[0.993408,-8.841871],[3.225962,-7.855456],[6.029905,9.150256],[9.320870,-8.768111],[5.755297,3.770370],[6.839402,6.444191],[-1.210271,5.546602]],[[1.915353,-4.367901],[-2.612714,0.228901],[-4.802846,-3.733719],[-4.363731,5.460258],[9.945785,9.952683],[-9.152097,-4.380753],[5.999384,-9.023443],[6.343575,2.962270],[-4.012378,6.082178],[-1.881165,5.546994],[3.102509,5.258525],[7.899612,4.024220],[-2.629572,1.957933],[-3.510032,-4.365931],[-9.482645,2.609730]],[[-8.570343,-1.502813],[-5.131567,7.541818],[-2.606853,4.464988],[9.095386,-7.741333],[-0.697085,5.933821],[-2.854891,4.458963],[-6.837400,-9.419998],[-0.634842,-6.738560],[-2.229627,8.484084],[6.094358,0.447086],[4.156404,1.193354],[4.638895,0.895192],[3.687783,-3.268040],[-3.828588,-2.550034],[-1.669374,9.689868]],[[-7.375564,4.220988],[-8.899368,-3.281229],[-0.555509,-3.128765],[-0.210919,-8.123243],[9.866371,0.634794],[-4.430230,-4.468759],[2.371053,9.880230],[5.378712,-8.219435],[-9.583757,-7.701922],[3.459140,-4.602676],[-3.786839,6.638363],[-8.333248,3.713475],[-9.169042,8.032331],[-7.882150,5.634264],[-7.515609,9.343063]],[[5.115664,-8.845590],[-2.852047,-7.637992],[9.529059,4.198283],[1.996767,-9.213434],[-7.883452,8.670749],[8.797432,2.268969],[-1.564667,8.867417],[9.460026,-0.100295],[1.384154,-0.244301],[4.740988,6.200157],[-4.851220,0.130860],[9.361165,1.718596],[0.644307,-2.118244],[5.733799,-4.634988],[-8.675939,6.985733]],[[5.054332,-0.898688],[-9.081297,-2.578956],[-9.551371,-0.784572],[-5.993234,-4.217713],[0.930190,3.734809],[7.155543,8.008343],[1.840292,-1.105183],[-4.183436,2.495959],[-7.204895,-0.031822],[-1.026236,-3.327433],[-3.049229,0.113077],[-4.153600,-5.463322],[-0.854312,-1.022132],[-8.765585,-8.121212],[-0.379930,8.756046]],[[-3.310764,-7.266913],[8.538050,1.770944],[9.755187,-2.430407],[-1.015085,-4.137738],[7.303843,9.831147],[-9.359978,2.765086],[1.022621,-3.577836],[7.843309,-6.488628],[-3.079635,-8.742493],[1.203476,4.571182],[8.998223,-0.579982],[-4.883534,3.816076],[-2.323027,1.423031],[-2.038848,9.517330],[-8.091277,4.674311]],[[9.518001,-5.128819],[-1.819330,6.741620],[-2.607614,-6.950799],[-4.554802,-8.148706],[2.593818,1.572939],[-8.189036,-7.821058],[0.205710,-5.582446],[4.696255,7.110430],[-2.179798,-6.673146],[-3.918182,-1.079797],[0.669743,0.819356],[-6.669308,-2.553839],[6.120765,8.714135],[-3.788725,-5.107764],[7.898579,0.302905]],[[4.167347,9.725384],[-3.751474,-8.493925],[-6.978898,-1.976719],[-4.743197,8.548645],[6.451483,-0.351296],[8.446135,-1.274838],[-3.188592,-7.753734],[3.292778,-6.105737],[-9.229375,-1.526979],[-0.977414,-4.899487],[-3.128829,-5.528237],[-3.364981,9.270482],[4.503788,-5.177639],[9.679340,-4.573780],[4.305570,8.155606]],[[-9.253989,5.344621],[5.338217,-5.574766],[3.164153,-3.455752],[3.724427,-1.595255],[8.929736,7.635919],[6.189849,1.727444],[-3.657101,-5.178500],[-8.379510,-8.195949],[-9.086085,-6.784092],[-5.842268,9.772893],[0.488437,7.263857],[-2.483142,-1.301796],[2.546806,-3.484921],[6.019873,4.691621],[3.343180,6.711905]],[[1.306645,-8.160651],[-1.248145,4.589276],[8.369499,-5.037034],[5.086444,8.229324],[5.374885,4.937844],[8.616473,1.967603],[8.373847,-1.191743],[1.042407,7.978786],[-7.968876,-0.139320],[-1.914690,2.672405],[-5.250972,-2.318578],[1.412896,0.223116],[6.981194,1.510512],[-7.650857,6.780102],[4.621876,-3.374554]],[[5.683229,9.450798],[1.656477,-1.100309],[3.683165,-2.809588],[2.100791,3.551706],[-4.613171,8.669931],[6.355999,5.903580],[-0.331246,-1.278947],[-0.282300,-6.233599],[-6.132344,4.030950],[3.692568,8.164523],[1.966615,-4.553129],[-8.688463,2.933782],[-6.762234,-7.099651],[9.958115,6.344735],[-9.688206,3.467402]],[[-8.312422,-0.019216],[2.671272,-6.099744],[-6.307226,-1.674217],[5.917640,-4.365246],[-4.461915,1.316103],[2.127221,5.660560],[1.727513,-1.335051],[-7.915311,-6.325997],[9.828434,5.063237],[1.324228,4.072062],[3.528441,0.224051],[-1.600928,-1.206521],[-5.441010,9.481967],[1.043626,-6.621462],[1.657333,-5.736450]],[[6.228708,-5.437012],[8.663090,7.484385],[3.139483,-1.565186],[-5.981724,-3.768945],[-2.170874,-7.953022],[-1.555862,-0.600084],[-9.781692,-2.317416],[4.494557,4.292521],[2.089788,9.832937],[7.696696,4.391237],[4.558193,7.077966],[-8.479024,-0.405171],[-1.872118,0.584265],[-4.096388,-7.301912],[-0.559537,-2.219661]],[[1.251369,-4.546306],[5.645393,4.910580],[0.071308,0.773355],[3.099619,-0.462273],[-0.167484,-8.123090],[7.562457,6.364729],[6.730375,-8.350582],[-4.118463,8.014941],[-6.177795,4.157785],[8.056259,-3.769874],[2.781424,8.132433],[-2.458699,-0.481801],[-5.056981,1.785934],[-1.838758,8.409660],[-4.680421,-2.025968]]], dtype = "float64")#candidate|554|(15, 15, 2)|const|float64
uop_555 = relay.acosh(const_554.astype('float64')) # shape=(15, 15, 2)
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
var_558 = relay.var("var_558", dtype = "int8", shape = (225,))#candidate|558|(225,)|var|int8
call_557 = func_517_call(relay.reshape(var_558.astype('int8'), [5, 15, 3]))
call_559 = func_517_call(relay.reshape(var_558.astype('int8'), [5, 15, 3]))
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
call_560 = func_517_call(relay.reshape(var_558.astype('int8'), [5, 15, 3]))
call_561 = func_517_call(relay.reshape(var_558.astype('int8'), [5, 15, 3]))
uop_579 = relay.asinh(uop_555.astype('float32')) # shape=(15, 15, 2)
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
call_581 = func_517_call(relay.reshape(call_560.astype('int8'), [5, 15, 3]))
call_582 = func_517_call(relay.reshape(call_560.astype('int8'), [5, 15, 3]))
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
call_587 = func_517_call(relay.reshape(call_581.astype('int8'), [5, 15, 3]))
call_588 = func_517_call(relay.reshape(call_581.astype('int8'), [5, 15, 3]))
bop_594 = relay.floor_divide(uop_579.astype('float64'), relay.reshape(const_554.astype('float64'), relay.shape_of(uop_579))) # shape=(15, 15, 2)
output = relay.Tuple([call_557,var_558,call_560,call_581,call_587,bop_594,])
output2 = relay.Tuple([call_559,var_558,call_561,call_582,call_588,bop_594,])
func_598 = relay.Function([var_558,], output)
mod['func_598'] = func_598
mod = relay.transform.InferType()(mod)
var_599 = relay.var("var_599", dtype = "int8", shape = (225,))#candidate|599|(225,)|var|int8
output = func_598(var_599)
func_600 = relay.Function([var_599], output)
mutated_mod['func_600'] = func_600
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1119 = relay.var("var_1119", dtype = "float64", shape = (4, 5, 11))#candidate|1119|(4, 5, 11)|var|float64
uop_1120 = relay.atan(var_1119.astype('float64')) # shape=(4, 5, 11)
output = relay.Tuple([uop_1120,])
output2 = relay.Tuple([uop_1120,])
func_1137 = relay.Function([var_1119,], output)
mod['func_1137'] = func_1137
mod = relay.transform.InferType()(mod)
var_1138 = relay.var("var_1138", dtype = "float64", shape = (4, 5, 11))#candidate|1138|(4, 5, 11)|var|float64
output = func_1137(var_1138)
func_1139 = relay.Function([var_1138], output)
mutated_mod['func_1139'] = func_1139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1383 = relay.var("var_1383", dtype = "bool", shape = (14, 7, 9))#candidate|1383|(14, 7, 9)|var|bool
const_1384 = relay.const([[[True,True,False,True,True,True,False,False,False],[False,False,False,True,False,True,False,True,True],[False,True,True,False,True,True,False,False,False],[False,False,True,False,True,False,False,False,True],[True,False,False,False,False,False,False,False,True],[True,False,False,False,True,True,False,True,False],[True,True,False,True,True,False,False,False,True]],[[False,False,True,False,False,False,False,False,False],[False,False,False,True,True,True,True,True,False],[True,True,True,True,False,False,False,True,True],[False,True,True,False,False,False,True,False,False],[True,False,False,False,False,False,False,False,True],[True,True,False,True,False,False,False,False,False],[False,False,False,False,False,True,True,False,True]],[[True,False,True,True,True,True,True,True,False],[True,False,False,False,True,True,True,True,False],[True,True,False,True,False,False,True,False,False],[True,True,True,False,True,True,False,False,False],[True,False,False,True,True,False,True,False,True],[True,True,False,True,False,False,True,True,False],[True,True,False,True,False,True,False,False,False]],[[True,False,True,False,False,True,False,True,False],[False,True,False,True,False,True,False,True,True],[False,False,True,False,True,False,False,False,False],[True,True,False,False,False,True,True,False,True],[False,False,False,False,False,True,True,False,True],[False,False,False,False,False,False,True,False,True],[True,False,False,True,True,True,True,True,True]],[[False,False,False,True,False,False,False,True,True],[True,False,True,True,False,True,True,False,True],[False,True,True,True,False,True,True,True,False],[False,True,False,False,True,False,False,True,True],[False,True,False,True,False,False,False,True,False],[True,True,True,False,True,False,True,False,True],[False,False,False,True,False,True,True,False,True]],[[True,False,False,False,True,True,False,False,True],[False,True,True,True,False,False,False,True,True],[False,False,True,True,True,True,False,False,False],[True,True,False,False,False,True,False,True,False],[True,True,False,True,False,True,False,True,False],[False,True,True,True,True,True,False,True,False],[False,True,False,False,False,True,False,True,False]],[[True,True,True,True,True,False,False,False,False],[True,False,True,True,False,False,False,True,False],[False,True,True,False,True,False,True,True,False],[False,False,True,False,True,True,True,True,False],[False,True,False,False,False,False,False,False,False],[False,False,True,False,False,False,True,True,False],[True,False,True,False,False,True,True,True,True]],[[False,False,False,False,False,True,False,True,True],[False,True,True,False,True,False,True,False,False],[False,True,True,False,True,True,True,True,False],[True,False,True,False,True,True,False,True,False],[True,False,True,False,False,False,False,True,True],[False,False,True,False,False,True,False,False,False],[True,False,True,True,True,True,False,True,False]],[[False,True,False,False,False,False,True,False,False],[True,False,True,False,False,False,False,True,False],[True,True,True,True,False,True,False,False,False],[True,False,True,False,False,False,False,False,False],[False,True,False,False,False,True,False,True,True],[False,True,False,False,False,True,True,True,False],[False,True,False,False,False,False,True,False,True]],[[True,False,True,True,False,True,False,True,True],[True,True,False,False,True,True,True,True,True],[False,True,False,False,True,True,False,False,False],[True,True,False,False,True,True,True,False,True],[False,False,False,False,True,True,False,False,False],[False,True,False,True,True,True,False,False,False],[True,False,False,True,True,False,False,True,True]],[[True,True,True,False,True,False,True,True,True],[False,False,True,True,False,False,True,True,False],[False,True,False,False,True,False,True,False,False],[True,False,True,False,True,False,True,False,False],[True,True,True,True,True,True,False,False,True],[True,True,True,True,True,False,True,False,True],[True,True,False,True,False,False,True,False,False]],[[True,True,False,True,True,True,True,False,False],[False,False,True,False,True,False,True,False,False],[True,True,False,True,True,True,True,False,True],[True,True,True,True,True,False,True,False,True],[False,True,True,True,False,False,False,False,True],[False,True,False,False,False,True,False,True,False],[True,False,True,False,False,False,True,True,True]],[[False,True,False,True,True,True,True,False,True],[True,False,True,False,True,False,False,True,True],[False,False,False,False,True,True,True,False,True],[False,True,False,True,True,True,True,True,True],[True,False,True,False,True,False,False,True,True],[False,False,False,True,False,False,False,False,False],[True,False,False,False,False,True,False,True,True]],[[False,True,False,True,False,False,False,False,True],[False,False,False,True,True,False,False,False,False],[False,False,True,False,True,True,False,True,True],[False,False,False,True,False,True,True,True,True],[True,True,False,False,False,False,False,True,True],[True,True,False,True,False,False,False,False,False],[True,True,True,False,True,True,True,False,True]]], dtype = "bool")#candidate|1384|(14, 7, 9)|const|bool
bop_1385 = relay.logical_and(var_1383.astype('bool'), relay.reshape(const_1384.astype('bool'), relay.shape_of(var_1383))) # shape=(14, 7, 9)
output = relay.Tuple([bop_1385,])
output2 = relay.Tuple([bop_1385,])
func_1401 = relay.Function([var_1383,], output)
mod['func_1401'] = func_1401
mod = relay.transform.InferType()(mod)
var_1402 = relay.var("var_1402", dtype = "bool", shape = (14, 7, 9))#candidate|1402|(14, 7, 9)|var|bool
output = func_1401(var_1402)
func_1403 = relay.Function([var_1402], output)
mutated_mod['func_1403'] = func_1403
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1448 = relay.const([[[2.275895],[2.527673],[4.324650],[1.667282],[0.585258],[5.069317],[2.365756],[3.063775],[8.926849],[-1.807699],[2.097067],[5.614372],[-7.035441],[9.319624],[-1.631433]],[[-6.435267],[-8.893833],[-4.145183],[6.351255],[6.016105],[7.064034],[8.507448],[-4.270712],[-3.792435],[-6.561490],[9.190982],[4.421553],[-2.765869],[5.733676],[0.028205]]], dtype = "float32")#candidate|1448|(2, 15, 1)|const|float32
uop_1449 = relay.cos(const_1448.astype('float32')) # shape=(2, 15, 1)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
var_1455 = relay.var("var_1455", dtype = "bool", shape = (882,))#candidate|1455|(882,)|var|bool
call_1454 = relay.TupleGetItem(func_1401_call(relay.reshape(var_1455.astype('bool'), [14, 7, 9])), 0)
call_1456 = relay.TupleGetItem(func_1403_call(relay.reshape(var_1455.astype('bool'), [14, 7, 9])), 0)
output = relay.Tuple([uop_1449,call_1454,var_1455,])
output2 = relay.Tuple([uop_1449,call_1456,var_1455,])
func_1460 = relay.Function([var_1455,], output)
mod['func_1460'] = func_1460
mod = relay.transform.InferType()(mod)
mutated_mod['func_1460'] = func_1460
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1461 = relay.var("var_1461", dtype = "bool", shape = (882,))#candidate|1461|(882,)|var|bool
func_1460_call = mutated_mod.get_global_var('func_1460')
call_1462 = func_1460_call(var_1461)
output = call_1462
func_1463 = relay.Function([var_1461], output)
mutated_mod['func_1463'] = func_1463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2140 = relay.var("var_2140", dtype = "float64", shape = (1, 8, 12))#candidate|2140|(1, 8, 12)|var|float64
uop_2141 = relay.acosh(var_2140.astype('float64')) # shape=(1, 8, 12)
output = uop_2141
output2 = uop_2141
func_2145 = relay.Function([var_2140,], output)
mod['func_2145'] = func_2145
mod = relay.transform.InferType()(mod)
var_2146 = relay.var("var_2146", dtype = "float64", shape = (1, 8, 12))#candidate|2146|(1, 8, 12)|var|float64
output = func_2145(var_2146)
func_2147 = relay.Function([var_2146], output)
mutated_mod['func_2147'] = func_2147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2362 = relay.var("var_2362", dtype = "float64", shape = (13, 8, 7))#candidate|2362|(13, 8, 7)|var|float64
const_2363 = relay.const([[[-1.892242,3.167339,-3.885567,-3.749677,-8.345238,-8.947723,-2.918239],[-7.373617,-1.114122,-4.708163,6.750450,-3.255646,3.947910,2.577871],[-2.241246,8.354936,9.901935,9.264479,3.399292,4.979614,-3.920296],[7.156910,-6.100686,-2.950406,7.234842,1.304035,-9.524810,8.687002],[-2.010452,6.677971,7.911182,5.565694,-0.403816,-3.552868,-6.019549],[7.251787,-9.300664,6.775842,-3.013597,5.595840,-9.255578,-3.138644],[-9.807180,-6.650668,7.084085,1.109555,-7.082004,4.483370,3.613064],[-5.392832,2.519481,-3.125907,-4.980345,-2.965461,4.555759,9.579269]],[[-7.881221,-8.523949,0.089946,9.539865,0.869110,7.094021,0.340288],[-7.260569,3.823281,-9.749958,-5.999774,-7.814004,-4.045650,7.932988],[-7.816433,9.144326,0.466151,-0.782319,-7.524458,2.018411,-1.200412],[9.904167,1.789883,7.758445,-0.366436,2.254836,-9.663867,-5.132637],[-7.009980,5.658633,-1.148741,4.961674,-8.033232,-0.963375,-8.070333],[-3.132104,-1.300209,-5.765434,7.944018,-6.621070,-0.329096,-4.305127],[2.668836,0.735904,1.066631,4.913734,-7.508242,4.893414,-7.581561],[1.595679,4.945382,9.208256,-0.661240,9.934120,1.756895,7.400289]],[[1.910020,0.943819,-3.334889,-8.805858,4.238414,2.633576,-7.372739],[-0.415936,-6.363176,9.551561,-7.036040,-0.670754,7.496783,-0.113956],[7.319056,-3.205686,-1.459085,-7.332264,-3.882505,-8.226055,-0.371091],[6.314423,-5.470398,4.515946,-9.281656,-0.100793,6.508692,1.799623],[-4.452551,-3.120364,9.325172,-5.104359,-2.354830,2.209104,9.160998],[-4.077275,5.354402,-1.755586,1.240459,4.718601,8.712876,-9.885141],[-9.700451,8.635077,-5.759728,-2.727490,-8.730395,5.674891,5.387309],[8.487636,-1.460270,-7.035862,-1.778784,9.941404,-3.376890,7.592029]],[[-0.978915,7.489878,3.226706,5.346237,-5.460489,1.761845,-0.380761],[5.236228,5.896385,-3.069718,-7.805352,-2.885746,8.512020,-8.837846],[-3.685628,0.755769,-3.643198,1.934714,9.492263,7.041195,-1.099447],[-5.493897,0.566139,4.991736,6.272814,-3.219328,-5.227074,-6.900876],[-9.547517,-7.196424,-1.215200,1.743354,-4.482941,-7.682095,9.072065],[4.779726,-6.812935,-2.508725,1.176843,1.615420,9.509673,-6.881650],[-0.332969,5.047119,1.720466,6.939026,-5.952786,-9.029101,8.468912],[-8.039096,-3.195526,-3.475167,-5.336169,-2.291573,-7.533365,-2.936826]],[[3.487256,-0.357049,7.173480,-5.076619,8.724451,-6.572832,-5.617195],[-5.175739,0.611719,-6.224547,-0.669281,-9.108114,4.659150,-8.677082],[-9.488910,7.090601,6.082263,8.148439,-3.481131,9.448161,8.438058],[2.597275,8.813129,4.221325,-5.599280,-2.345071,7.928855,2.589485],[-9.290576,-2.142021,-7.359795,-4.343166,6.086250,-9.793828,-0.414241],[9.805025,5.003486,9.314699,-4.688656,9.015616,3.687386,0.104512],[4.656067,8.242819,-2.410614,-4.875898,-5.252892,-3.690251,9.991630],[8.658317,3.502505,4.489789,9.618095,8.718131,-2.066109,-0.717388]],[[-0.905920,-1.819826,1.209427,8.227006,5.728914,-2.987799,9.537351],[-9.071090,-4.352835,-7.793300,-6.869700,-7.453075,-4.553210,-5.526748],[0.790393,-0.612469,-9.276266,5.988924,9.338009,-7.540959,-7.326091],[-2.592013,7.709234,-4.604572,-1.415254,1.367340,5.769496,-4.990201],[2.475226,-1.525281,8.315750,7.535295,7.973188,4.294975,3.053920],[6.074208,3.864297,0.131856,-3.906172,-1.911611,-1.477088,-8.775550],[5.574287,-7.387377,2.645130,3.087460,4.691117,-3.606334,7.874910],[3.416584,0.676930,1.487202,-9.279621,-2.353166,-7.198842,7.264567]],[[-3.021464,-0.868912,-8.240916,7.752807,7.077364,3.444963,6.931104],[6.667484,1.233985,0.038647,-7.507736,7.550898,-1.163159,2.042537],[-0.015968,0.746297,-9.397495,0.817872,-8.952308,-2.193143,7.611710],[0.465147,-4.457548,-8.748181,2.005475,-6.339025,-9.934640,0.985105],[2.318279,3.980999,8.841551,8.230571,7.521147,2.566583,7.978487],[0.058152,3.662931,2.755624,-0.220722,4.908490,5.111628,8.875418],[-6.734254,-7.692636,5.830867,0.512628,2.315628,5.082363,2.086097],[-5.649103,-0.760131,-6.993450,-6.368827,0.596639,2.367493,9.066160]],[[9.509897,-7.814607,3.576344,0.239123,-3.721103,1.403951,6.006707],[-0.588924,7.809235,1.774707,5.063124,7.996776,4.633965,-0.988004],[-7.617713,-4.537978,-2.495957,5.677884,9.007189,-3.458992,8.190434],[6.571794,-5.790740,-2.939718,3.732238,-1.457817,2.674964,-6.779893],[-6.579968,8.892975,-1.866663,-9.881888,-8.164036,-0.822601,1.278137],[4.637213,3.461115,7.147296,6.389505,5.421676,-8.862690,2.834441],[-6.760153,-6.452301,-9.677630,8.733594,0.920785,9.713379,1.253150],[-5.664959,-2.238253,8.455127,-7.909609,-2.046248,-6.392275,-8.173008]],[[8.096349,-6.149251,-5.454672,-7.474839,-6.360978,7.866888,-1.371085],[6.667027,7.932458,-9.470263,-6.605360,7.254436,-4.252720,-4.455616],[1.942424,7.083151,-8.821216,-5.526516,2.315682,5.207851,-5.356603],[1.221184,8.527205,-4.971087,-7.017394,-7.812995,5.504002,-9.077917],[6.204059,-8.065466,0.722425,0.815281,-2.857001,-5.619433,1.314026],[2.904669,4.631379,-7.646595,-5.000293,5.782493,5.789233,6.322891],[7.031566,-7.614784,-8.153664,7.830920,2.108308,5.556747,7.731141],[8.046317,9.172470,-8.000334,0.516934,3.781029,-6.823031,5.643885]],[[-9.707446,-5.739266,-3.065789,2.754261,2.061558,-5.442681,5.301350],[-5.391711,-0.085900,3.280623,7.165036,-2.592115,-3.611654,-2.118449],[-4.474354,-5.640806,-9.200179,-4.607984,-1.380863,8.503356,-6.419090],[-2.343534,8.119457,-2.434236,-3.081710,2.689638,-7.127437,-7.799152],[7.408515,8.277624,-6.447504,-5.116262,-8.441328,6.218438,-9.810413],[-2.811165,6.285815,2.300043,-1.239540,-0.149276,4.140057,-7.955961],[6.548414,0.935223,6.432114,-8.618577,-5.722443,-5.475638,9.979461],[2.086331,-1.418096,-2.874692,-2.441618,-5.632054,-5.382839,4.932534]],[[-6.926799,8.241845,3.857494,-4.362120,3.117923,-3.680953,6.053795],[-0.778684,1.312158,5.407352,9.156440,1.169623,4.645923,-7.460999],[-9.442639,4.927469,5.367891,-9.901266,7.205416,8.943398,8.007068],[1.386433,-7.848649,7.226420,2.054494,9.446312,-0.660721,1.273403],[-3.089290,6.910101,0.721041,5.618412,3.764955,6.148887,-7.682427],[3.964592,4.593031,0.996094,-6.090739,7.523533,0.665351,1.392461],[8.752431,7.418757,-5.565778,-6.661870,3.387456,9.852294,4.164101],[-2.942141,0.747173,6.441760,-1.350725,3.886573,6.537523,-2.363063]],[[1.131676,-2.348472,-4.102052,4.175643,7.385263,1.259730,6.768378],[0.209679,2.615668,4.713800,-8.318535,4.245207,7.091624,2.643325],[8.922596,3.350458,3.362561,8.097749,7.247336,2.483445,-7.784551],[2.413537,2.088355,-9.368970,-1.748230,2.211492,-4.885014,7.800201],[8.614760,-1.935501,8.683302,-8.280978,-9.646888,-7.451949,-0.823070],[-1.212959,-0.423179,-5.533710,-0.708496,7.527374,-2.954671,4.639311],[6.746096,-9.581041,-4.077534,-8.894123,-4.190147,-5.032232,-4.205459],[-6.380890,-0.746971,-9.872095,2.556277,-7.461769,4.082464,-9.226293]],[[1.634104,0.222165,2.404775,3.137915,-6.196166,1.686070,-0.892456],[8.190643,-5.262316,0.752335,-1.066469,-2.822589,6.914530,-9.029298],[-4.242003,-0.057206,-1.222040,-6.744382,-2.380907,4.684349,6.834935],[9.907662,5.002179,1.378630,6.701901,-3.020733,-0.888460,3.684275],[-5.419323,-7.119612,-4.132494,-2.142091,-1.649860,-8.617201,-3.153133],[-4.710390,-4.740705,-9.895587,-2.337727,-9.348893,-9.231099,-4.439968],[2.974074,-8.611104,0.792665,-3.337743,-4.967405,-0.142671,6.166750],[3.021331,6.027771,-8.527338,1.569380,2.399411,-2.417432,0.136630]]], dtype = "float64")#candidate|2363|(13, 8, 7)|const|float64
bop_2364 = relay.subtract(var_2362.astype('float64'), relay.reshape(const_2363.astype('float64'), relay.shape_of(var_2362))) # shape=(13, 8, 7)
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
var_2370 = relay.var("var_2370", dtype = "int8", shape = (225,))#candidate|2370|(225,)|var|int8
call_2369 = func_517_call(relay.reshape(var_2370.astype('int8'), [5, 15, 3]))
call_2371 = func_517_call(relay.reshape(var_2370.astype('int8'), [5, 15, 3]))
output = relay.Tuple([bop_2364,call_2369,var_2370,])
output2 = relay.Tuple([bop_2364,call_2371,var_2370,])
func_2380 = relay.Function([var_2362,var_2370,], output)
mod['func_2380'] = func_2380
mod = relay.transform.InferType()(mod)
var_2381 = relay.var("var_2381", dtype = "float64", shape = (13, 8, 7))#candidate|2381|(13, 8, 7)|var|float64
var_2382 = relay.var("var_2382", dtype = "int8", shape = (225,))#candidate|2382|(225,)|var|int8
output = func_2380(var_2381,var_2382,)
func_2383 = relay.Function([var_2381,var_2382,], output)
mutated_mod['func_2383'] = func_2383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2426 = relay.var("var_2426", dtype = "int64", shape = (13, 3, 13))#candidate|2426|(13, 3, 13)|var|int64
var_2427 = relay.var("var_2427", dtype = "int64", shape = (13, 3, 13))#candidate|2427|(13, 3, 13)|var|int64
bop_2428 = relay.less_equal(var_2426.astype('bool'), relay.reshape(var_2427.astype('bool'), relay.shape_of(var_2426))) # shape=(13, 3, 13)
bop_2435 = relay.greater(bop_2428.astype('bool'), relay.reshape(var_2426.astype('bool'), relay.shape_of(bop_2428))) # shape=(13, 3, 13)
func_1460_call = mod.get_global_var('func_1460')
func_1463_call = mutated_mod.get_global_var('func_1463')
const_2439 = relay.const([True,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True], dtype = "bool")#candidate|2439|(882,)|const|bool
call_2438 = relay.TupleGetItem(func_1460_call(relay.reshape(const_2439.astype('bool'), [882,])), 2)
call_2440 = relay.TupleGetItem(func_1463_call(relay.reshape(const_2439.astype('bool'), [882,])), 2)
var_2446 = relay.var("var_2446", dtype = "bool", shape = (13, 3, 13))#candidate|2446|(13, 3, 13)|var|bool
bop_2447 = relay.left_shift(bop_2435.astype('int8'), relay.reshape(var_2446.astype('int8'), relay.shape_of(bop_2435))) # shape=(13, 3, 13)
bop_2452 = relay.add(const_2439.astype('int16'), relay.reshape(call_2438.astype('int16'), relay.shape_of(const_2439))) # shape=(882,)
bop_2455 = relay.add(const_2439.astype('int16'), relay.reshape(call_2440.astype('int16'), relay.shape_of(const_2439))) # shape=(882,)
func_2145_call = mod.get_global_var('func_2145')
func_2147_call = mutated_mod.get_global_var('func_2147')
const_2458 = relay.const([[-2.014458,-4.905310],[9.540120,-8.363410],[-4.502467,1.869093],[-7.485187,4.831910],[4.481350,9.076442],[6.305788,-8.677019],[-5.936971,6.665276],[-4.213311,-7.731975],[9.454637,8.090497],[6.079231,3.548205],[-1.084035,1.179069],[-8.124912,9.819756],[-0.084631,-3.886676],[4.964456,-7.905079],[3.327980,-2.603847],[-1.753438,-8.675082],[9.332829,-7.922669],[3.784586,-9.830934],[-7.799613,-0.681422],[-9.537127,-3.757999],[-3.650968,-2.957003],[8.884725,5.189616],[7.929567,7.392360],[-9.334417,2.945169],[9.760172,-2.260761],[2.379486,-4.884276],[9.348348,-2.682151],[3.575705,-9.708670],[-6.462992,2.988749],[-6.946236,-4.684086],[-1.010925,0.702543],[7.782917,-0.083598],[-5.391295,6.977481],[0.581848,-3.920266],[5.117602,-1.234581],[9.535641,-3.052077],[-0.426605,-1.021376],[4.089572,-4.973536],[-2.967461,-2.385954],[-2.635483,-3.781481],[-8.641310,3.164845],[7.241003,-7.001585],[-4.503659,6.283629],[1.845410,3.071199],[6.006009,-5.072753],[-1.684955,-8.177919],[-3.050122,-1.814952],[7.789370,-7.259689]], dtype = "float64")#candidate|2458|(48, 2)|const|float64
call_2457 = func_2145_call(relay.reshape(const_2458.astype('float64'), [1, 8, 12]))
call_2459 = func_2145_call(relay.reshape(const_2458.astype('float64'), [1, 8, 12]))
uop_2480 = relay.erf(const_2439.astype('float32')) # shape=(882,)
bop_2482 = relay.greater_equal(uop_2480.astype('bool'), relay.reshape(call_2438.astype('bool'), relay.shape_of(uop_2480))) # shape=(882,)
bop_2485 = relay.greater_equal(uop_2480.astype('bool'), relay.reshape(call_2440.astype('bool'), relay.shape_of(uop_2480))) # shape=(882,)
output = relay.Tuple([bop_2447,bop_2452,call_2457,const_2458,bop_2482,])
output2 = relay.Tuple([bop_2447,bop_2455,call_2459,const_2458,bop_2485,])
func_2491 = relay.Function([var_2426,var_2427,var_2446,], output)
mod['func_2491'] = func_2491
mod = relay.transform.InferType()(mod)
var_2492 = relay.var("var_2492", dtype = "int64", shape = (13, 3, 13))#candidate|2492|(13, 3, 13)|var|int64
var_2493 = relay.var("var_2493", dtype = "int64", shape = (13, 3, 13))#candidate|2493|(13, 3, 13)|var|int64
var_2494 = relay.var("var_2494", dtype = "bool", shape = (13, 3, 13))#candidate|2494|(13, 3, 13)|var|bool
output = func_2491(var_2492,var_2493,var_2494,)
func_2495 = relay.Function([var_2492,var_2493,var_2494,], output)
mutated_mod['func_2495'] = func_2495
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2561 = relay.var("var_2561", dtype = "float64", shape = (7, 12, 8))#candidate|2561|(7, 12, 8)|var|float64
uop_2562 = relay.atan(var_2561.astype('float64')) # shape=(7, 12, 8)
var_2571 = relay.var("var_2571", dtype = "float64", shape = (7, 12, 8))#candidate|2571|(7, 12, 8)|var|float64
bop_2572 = relay.equal(var_2561.astype('bool'), relay.reshape(var_2571.astype('bool'), relay.shape_of(var_2561))) # shape=(7, 12, 8)
bop_2591 = relay.maximum(uop_2562.astype('float64'), relay.reshape(bop_2572.astype('float64'), relay.shape_of(uop_2562))) # shape=(7, 12, 8)
output = bop_2591
output2 = bop_2591
func_2596 = relay.Function([var_2561,var_2571,], output)
mod['func_2596'] = func_2596
mod = relay.transform.InferType()(mod)
mutated_mod['func_2596'] = func_2596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2596_call = mutated_mod.get_global_var('func_2596')
var_2598 = relay.var("var_2598", dtype = "float64", shape = (7, 12, 8))#candidate|2598|(7, 12, 8)|var|float64
var_2599 = relay.var("var_2599", dtype = "float64", shape = (7, 12, 8))#candidate|2599|(7, 12, 8)|var|float64
call_2597 = func_2596_call(var_2598,var_2599,)
output = call_2597
func_2600 = relay.Function([var_2598,var_2599,], output)
mutated_mod['func_2600'] = func_2600
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2762 = relay.var("var_2762", dtype = "float32", shape = (5, 14, 10))#candidate|2762|(5, 14, 10)|var|float32
uop_2763 = relay.cos(var_2762.astype('float32')) # shape=(5, 14, 10)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
var_2776 = relay.var("var_2776", dtype = "bool", shape = (882,))#candidate|2776|(882,)|var|bool
call_2775 = relay.TupleGetItem(func_1401_call(relay.reshape(var_2776.astype('bool'), [14, 7, 9])), 0)
call_2777 = relay.TupleGetItem(func_1403_call(relay.reshape(var_2776.astype('bool'), [14, 7, 9])), 0)
output = relay.Tuple([uop_2763,call_2775,var_2776,])
output2 = relay.Tuple([uop_2763,call_2777,var_2776,])
func_2780 = relay.Function([var_2762,var_2776,], output)
mod['func_2780'] = func_2780
mod = relay.transform.InferType()(mod)
mutated_mod['func_2780'] = func_2780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2780_call = mutated_mod.get_global_var('func_2780')
var_2782 = relay.var("var_2782", dtype = "float32", shape = (5, 14, 10))#candidate|2782|(5, 14, 10)|var|float32
var_2783 = relay.var("var_2783", dtype = "bool", shape = (882,))#candidate|2783|(882,)|var|bool
call_2781 = func_2780_call(var_2782,var_2783,)
output = call_2781
func_2784 = relay.Function([var_2782,var_2783,], output)
mutated_mod['func_2784'] = func_2784
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2820 = relay.const([[[-8,9,-1,7,-4,8,-5,3,-2,3,-8,9,-7,-3],[-10,6,-1,6,-5,-2,3,3,8,10,-10,9,7,4],[-3,-2,3,2,2,-7,-5,10,-10,6,6,10,-6,7],[-9,1,5,4,1,3,-8,-2,1,10,4,3,-1,7],[-4,-5,3,-4,9,-8,5,-6,4,-7,2,10,5,-6],[-6,8,-7,-2,10,1,-5,-10,10,7,-3,-1,-2,-1],[-4,-5,-1,-2,-7,9,2,5,-8,-10,-2,-4,-1,-2],[-6,10,-1,2,-8,-2,-1,-10,-10,-2,1,-7,-9,8]],[[6,3,-2,-3,7,-6,-2,-10,9,5,9,8,-9,3],[-7,-10,-2,4,7,8,3,-1,-4,7,2,-3,-9,-3],[7,8,8,7,-2,-5,-8,-3,10,-7,6,6,-8,-1],[1,5,9,-1,1,10,-1,-2,-9,-4,-10,3,-7,-6],[-9,1,-10,-9,-10,-7,-10,-4,-1,2,3,2,6,-1],[-6,7,-3,-7,-5,-3,1,-5,8,-2,8,-10,-9,-8],[8,8,-6,1,-5,4,9,2,7,10,9,-6,-5,1],[1,-1,-9,-4,5,-4,-6,-8,-6,-2,10,-10,-4,-9]],[[5,5,9,4,4,-3,-3,-7,5,-1,-8,4,5,-8],[-10,-9,6,8,9,-3,10,-4,-3,10,-8,7,-4,-5],[-4,-7,1,9,2,-3,9,-6,2,-10,2,-2,-10,6],[9,4,-8,8,-9,-7,4,3,-7,-2,8,-3,1,1],[-4,9,10,-9,-6,-8,-3,5,-4,-1,-7,2,-7,6],[-2,-1,-5,2,-4,6,9,5,8,9,8,4,5,3],[-3,-9,-7,1,-3,-7,-5,4,-4,6,-9,-7,9,6],[-7,7,7,5,8,-6,-1,7,4,2,10,-4,-6,-8]],[[10,10,-3,9,3,-6,10,-4,-4,8,2,-10,9,3],[-2,-10,-7,2,-5,3,-5,-3,-2,-7,-7,6,5,4],[-7,1,2,-4,2,-10,-6,-7,4,7,4,-4,-7,2],[6,9,-5,-3,-10,5,-2,8,-9,-1,4,3,-2,-1],[-7,4,-1,7,1,-2,-8,4,-3,9,9,9,10,3],[6,2,9,7,6,5,-3,-2,-3,10,-9,9,1,-1],[-7,4,8,-9,1,-4,-9,6,-5,4,3,3,-4,-9],[-10,7,-5,-3,4,-10,9,2,5,1,-6,-8,-8,4]],[[3,7,4,-1,5,-3,-7,4,9,3,5,3,-6,4],[-2,-5,2,6,-8,-6,-2,-1,-2,-4,-2,4,-10,1],[-6,1,-3,-2,-10,2,5,2,9,-8,-8,-1,-9,10],[-1,-5,-7,-6,-5,-7,7,5,-9,1,10,-10,-2,-1],[-5,-10,3,3,4,-10,8,-5,9,8,7,-8,1,-7],[9,3,10,-10,1,-3,-5,-5,2,-9,-10,-9,-10,-3],[-4,-3,-10,-5,-2,-3,10,-1,1,-7,7,-4,-5,-5],[-9,-4,-9,-6,-5,-9,-7,1,8,-2,7,-2,7,1]],[[-8,-5,-5,1,-9,-4,9,-1,-8,6,4,7,-7,-6],[-4,6,-5,10,-3,-7,10,-5,7,-7,-10,-10,-1,4],[3,-4,-8,10,3,-5,-5,-9,4,-5,-1,5,-5,4],[10,-8,9,-2,4,2,4,-6,-2,3,10,-6,-2,2],[5,-5,-7,8,5,-5,-1,-6,6,3,6,5,-6,9],[-3,-7,-9,1,-5,4,-10,9,-9,6,7,-5,-9,-1],[1,-5,10,-3,4,9,-5,-7,3,6,-1,7,-6,-2],[-1,10,-2,-6,-8,-5,5,10,-6,-4,-5,1,5,-5]]], dtype = "int32")#candidate|2820|(6, 8, 14)|const|int32
var_2821 = relay.var("var_2821", dtype = "int32", shape = (6, 8, 14))#candidate|2821|(6, 8, 14)|var|int32
bop_2822 = relay.less_equal(const_2820.astype('bool'), relay.reshape(var_2821.astype('bool'), relay.shape_of(const_2820))) # shape=(6, 8, 14)
output = bop_2822
output2 = bop_2822
func_2832 = relay.Function([var_2821,], output)
mod['func_2832'] = func_2832
mod = relay.transform.InferType()(mod)
mutated_mod['func_2832'] = func_2832
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2833 = relay.var("var_2833", dtype = "int32", shape = (6, 8, 14))#candidate|2833|(6, 8, 14)|var|int32
func_2832_call = mutated_mod.get_global_var('func_2832')
call_2834 = func_2832_call(var_2833)
output = call_2834
func_2835 = relay.Function([var_2833], output)
mutated_mod['func_2835'] = func_2835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3479 = relay.var("var_3479", dtype = "float32", shape = (14, 7, 15))#candidate|3479|(14, 7, 15)|var|float32
uop_3480 = relay.log(var_3479.astype('float32')) # shape=(14, 7, 15)
output = uop_3480
output2 = uop_3480
func_3486 = relay.Function([var_3479,], output)
mod['func_3486'] = func_3486
mod = relay.transform.InferType()(mod)
mutated_mod['func_3486'] = func_3486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3487 = relay.var("var_3487", dtype = "float32", shape = (14, 7, 15))#candidate|3487|(14, 7, 15)|var|float32
func_3486_call = mutated_mod.get_global_var('func_3486')
call_3488 = func_3486_call(var_3487)
output = call_3488
func_3489 = relay.Function([var_3487], output)
mutated_mod['func_3489'] = func_3489
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3665 = relay.var("var_3665", dtype = "float64", shape = (8, 8, 12))#candidate|3665|(8, 8, 12)|var|float64
uop_3666 = relay.log(var_3665.astype('float64')) # shape=(8, 8, 12)
output = relay.Tuple([uop_3666,])
output2 = relay.Tuple([uop_3666,])
func_3675 = relay.Function([var_3665,], output)
mod['func_3675'] = func_3675
mod = relay.transform.InferType()(mod)
var_3676 = relay.var("var_3676", dtype = "float64", shape = (8, 8, 12))#candidate|3676|(8, 8, 12)|var|float64
output = func_3675(var_3676)
func_3677 = relay.Function([var_3676], output)
mutated_mod['func_3677'] = func_3677
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3917 = relay.const([[[8,8,-6,-4,10,9,3,-1,5,5,8,-7,-1],[-7,-5,8,8,5,-2,-6,4,10,-1,4,-4,2],[-4,-3,4,-1,-10,6,-6,-3,10,1,-5,3,-1],[-6,9,-6,-6,9,1,-1,-10,-9,6,5,9,9],[-8,-4,1,-3,-7,-5,-8,-5,4,-9,10,3,8],[-1,-5,-5,-3,9,8,-6,10,1,4,8,9,4],[-5,-7,-4,-4,-9,9,7,-7,1,1,3,-9,8],[-6,-5,8,9,5,-4,-2,7,6,-1,-10,-6,-4],[-4,7,2,-1,-8,-9,6,10,-4,-6,6,-8,5],[-1,-10,2,-10,10,-4,1,3,9,-5,-3,3,-1],[-9,8,-6,7,-4,3,-1,5,5,-9,7,10,-9],[2,-10,1,-3,-5,7,-8,4,6,6,1,9,-2]],[[10,-8,-4,-10,-3,-4,-1,-5,5,-1,5,-4,-1],[4,7,-4,-5,5,-3,4,6,-2,10,-7,-3,4],[8,-8,-5,6,-6,10,-3,3,-9,-1,8,4,-1],[3,-9,-1,-6,-5,3,2,4,-3,6,2,-6,2],[6,-3,7,2,-4,-5,4,-1,3,-8,-5,3,-8],[9,-10,9,-7,7,-10,-1,4,5,8,-6,-7,-10],[-5,6,-10,9,-7,7,3,-9,-5,-7,8,6,6],[-1,-6,9,-3,-5,1,-4,4,-2,7,2,-2,10],[3,-10,-10,5,-1,7,9,-7,-6,7,-4,9,-10],[5,1,4,3,-4,4,-9,2,-10,-8,9,10,3],[7,-5,-2,7,-6,-9,6,4,-1,-6,8,3,-3],[-9,-10,-6,6,-4,-4,4,-3,-8,4,-8,4,-9]],[[-9,10,7,-4,-6,6,4,10,10,-5,-5,-1,-7],[-8,-6,-7,9,9,-9,-5,-5,-4,-8,4,-8,-2],[-6,-4,5,-5,-8,5,10,-5,7,3,-8,1,-3],[7,-6,4,1,4,-1,6,1,-9,5,9,4,6],[-3,10,-9,-5,6,-6,1,-5,-9,4,-2,1,8],[9,-4,-4,1,-2,10,7,9,5,3,4,8,-2],[-2,-8,-2,2,2,-2,-1,3,-2,-9,4,-2,-1],[9,-4,-10,1,-7,-4,1,-5,9,7,-9,-4,3],[2,7,2,3,-4,-2,-10,9,8,-10,-5,8,4],[-3,6,8,-3,-9,10,3,-6,10,4,2,3,2],[4,10,-7,-6,-10,1,1,8,-4,7,6,10,9],[9,-5,-10,4,6,-2,6,-1,5,9,-3,-4,4]],[[8,-9,5,10,10,-8,-9,-6,9,7,9,1,-7],[10,5,-3,-10,-1,-2,-7,-3,9,-1,5,8,-9],[-3,-4,3,4,-10,10,-1,6,-3,6,-8,-8,-9],[-9,4,-4,8,-9,-2,8,2,-3,-10,4,10,1],[-4,-8,-1,-10,7,-4,-9,-6,8,4,-4,2,-4],[9,-8,-3,-9,-5,-10,-9,-8,1,-8,10,-1,-5],[-1,-8,3,10,-10,-4,-8,1,-6,4,-3,-3,2],[-6,-10,-5,-10,-8,2,6,3,-3,1,-10,4,2],[10,8,-9,-2,-7,-9,-2,2,5,6,-10,-10,2],[-9,-3,-4,4,-3,-10,1,-4,6,5,7,-6,7],[-3,6,-6,-4,5,2,-3,4,3,-1,-6,-10,5],[-1,4,8,5,-5,-10,-2,6,-8,-10,-2,-8,10]]], dtype = "uint64")#candidate|3917|(4, 12, 13)|const|uint64
var_3918 = relay.var("var_3918", dtype = "uint64", shape = (4, 12, 13))#candidate|3918|(4, 12, 13)|var|uint64
bop_3919 = relay.logical_xor(const_3917.astype('uint64'), relay.reshape(var_3918.astype('uint64'), relay.shape_of(const_3917))) # shape=(4, 12, 13)
uop_3938 = relay.sqrt(bop_3919.astype('float64')) # shape=(4, 12, 13)
func_3486_call = mod.get_global_var('func_3486')
func_3489_call = mutated_mod.get_global_var('func_3489')
var_3956 = relay.var("var_3956", dtype = "float32", shape = (7, 210))#candidate|3956|(7, 210)|var|float32
call_3955 = func_3486_call(relay.reshape(var_3956.astype('float32'), [14, 7, 15]))
call_3957 = func_3486_call(relay.reshape(var_3956.astype('float32'), [14, 7, 15]))
func_2596_call = mod.get_global_var('func_2596')
func_2600_call = mutated_mod.get_global_var('func_2600')
var_3960 = relay.var("var_3960", dtype = "float64", shape = (168, 4))#candidate|3960|(168, 4)|var|float64
call_3959 = func_2596_call(relay.reshape(var_3960.astype('float64'), [7, 12, 8]), relay.reshape(var_3960.astype('float64'), [7, 12, 8]), )
call_3961 = func_2596_call(relay.reshape(var_3960.astype('float64'), [7, 12, 8]), relay.reshape(var_3960.astype('float64'), [7, 12, 8]), )
output = relay.Tuple([uop_3938,call_3955,var_3956,call_3959,var_3960,])
output2 = relay.Tuple([uop_3938,call_3957,var_3956,call_3961,var_3960,])
func_3994 = relay.Function([var_3918,var_3956,var_3960,], output)
mod['func_3994'] = func_3994
mod = relay.transform.InferType()(mod)
mutated_mod['func_3994'] = func_3994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3994_call = mutated_mod.get_global_var('func_3994')
var_3996 = relay.var("var_3996", dtype = "uint64", shape = (4, 12, 13))#candidate|3996|(4, 12, 13)|var|uint64
var_3997 = relay.var("var_3997", dtype = "float32", shape = (7, 210))#candidate|3997|(7, 210)|var|float32
var_3998 = relay.var("var_3998", dtype = "float64", shape = (168, 4))#candidate|3998|(168, 4)|var|float64
call_3995 = func_3994_call(var_3996,var_3997,var_3998,)
output = call_3995
func_3999 = relay.Function([var_3996,var_3997,var_3998,], output)
mutated_mod['func_3999'] = func_3999
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4355 = relay.const([[[8.876346,-8.967740,-4.379402,-4.798923],[-1.722970,-2.951949,4.849112,0.823855],[-2.325582,-9.726826,5.327940,-2.191729],[8.579261,-6.779125,-1.842250,-3.370880],[4.397757,7.916259,-2.717206,-4.292149],[0.311052,-5.239971,4.533982,-8.924820],[-0.626729,-8.620255,-5.450611,-6.257337],[-8.179504,8.818488,-3.721250,-4.270867],[-4.459881,2.246403,-2.943652,4.748825],[-7.227032,-5.850422,0.846916,-1.717403],[7.383141,6.472628,7.947684,0.102738],[7.704549,-8.781129,-7.190471,0.678852]],[[-6.670086,-1.867194,-2.204433,9.726947],[0.372055,0.388516,-3.243984,-4.023205],[-4.857438,3.434759,9.606979,3.138706],[2.820038,4.667220,3.570608,-8.199494],[1.220609,-3.713188,6.115986,2.590824],[3.694815,4.584255,-8.638256,5.103101],[-5.189791,-1.687853,4.148076,-1.544575],[0.255866,-4.543343,-4.065478,5.828334],[7.909595,-7.818054,4.185542,8.289707],[-5.094490,-5.584870,-4.889314,6.023041],[0.917712,8.786318,-8.898623,7.495659],[2.377031,-3.508700,3.613164,6.471234]],[[4.988863,0.796983,1.761984,8.414302],[2.646329,-7.484879,4.331827,-3.191146],[2.406287,0.669897,2.200488,-4.653838],[-4.266351,0.866626,-8.626444,3.423343],[-7.152596,-9.975424,8.450062,3.645875],[0.621642,5.901040,1.931213,0.989294],[1.358124,-2.304809,-5.827716,8.560422],[4.301641,-7.306041,9.523655,8.800097],[-8.507859,-3.003737,8.087269,-0.882596],[0.217559,5.153675,-0.943603,-5.890072],[7.391397,-2.589939,5.085899,4.213201],[-9.027885,-7.510844,7.765636,0.616873]],[[6.733121,8.918127,0.114747,1.350050],[1.051165,-5.299206,-4.773858,6.069735],[3.759952,7.111317,9.490700,-5.061712],[-5.787829,-4.571242,-9.245302,9.766683],[4.548641,6.151831,-4.203649,9.741431],[9.954404,7.312737,-7.387462,-4.198414],[7.989683,-7.914873,-6.659137,-9.185718],[3.658398,-7.991922,9.659960,1.968774],[-1.983552,9.358423,-3.630898,1.895234],[-9.162609,6.755371,6.320227,6.251554],[3.654369,-1.687362,-1.019866,-9.595283],[2.107145,2.312352,-3.731453,4.437761]],[[0.892433,8.235229,1.090872,-5.528068],[-1.916139,1.354790,6.498743,-2.574928],[-4.094474,-4.022760,7.656277,5.462126],[5.580619,1.318352,9.408888,-3.928403],[-9.906515,-9.967295,-3.597084,6.284112],[-2.264192,4.321869,6.442112,-5.791584],[-4.328663,-4.183166,2.171636,-6.426236],[6.200314,-3.673703,-2.713011,6.491184],[4.926036,-7.784286,-4.019577,-9.136388],[-9.657176,-5.692253,0.768059,-4.240566],[4.011617,5.573933,-5.934269,1.920155],[-5.564210,-9.176053,6.145805,0.815120]],[[-2.888700,-6.776496,4.016034,7.589836],[-3.978894,-6.712146,0.507088,7.596087],[4.933695,7.920296,-4.655272,5.551111],[3.639921,2.470308,-3.872194,3.770111],[0.379495,0.389987,-3.672456,-9.341559],[7.739635,-9.301997,6.118163,5.957568],[-4.250761,-9.254599,-2.817529,5.979558],[-9.460081,-3.664699,0.752038,5.815944],[0.510851,-0.790841,1.271190,5.034046],[2.690999,1.139888,2.337277,3.796411],[-2.821893,9.941250,-6.707471,-2.772164],[3.348043,4.487361,-8.140934,1.282692]],[[2.522593,9.262725,6.003820,1.171947],[-8.162045,8.511978,-1.179652,1.876019],[1.004973,9.951378,-5.315659,-3.202352],[-9.629493,-7.556682,-2.854261,-4.189842],[5.421628,-5.669733,-7.176740,6.577169],[9.500933,0.373695,-1.116824,-8.952334],[9.360358,7.434203,9.844943,8.400047],[5.409391,-5.661579,-8.767418,6.076943],[-7.929769,-0.162938,-8.463830,5.398650],[-3.533090,2.712451,1.668236,-2.186982],[4.205198,-4.114122,8.375976,-2.262842],[-5.450112,-5.768781,5.173533,-1.669881]],[[-9.472942,6.088767,6.087828,-6.907023],[0.450475,-4.679975,2.754050,8.378144],[-2.281117,1.087887,6.721390,-7.559024],[-1.230352,-2.557215,-1.592236,9.421382],[0.843032,2.665100,3.295980,2.910140],[4.827887,8.321868,-2.604523,2.107028],[4.944511,2.914899,-9.254285,-1.857162],[-7.981599,0.186845,8.321642,7.078868],[7.433580,3.232801,-1.838606,1.012190],[-3.343941,-6.043991,1.766976,9.067095],[-9.621719,6.629979,-0.241989,0.278615],[7.353403,-4.698954,7.768752,4.493184]],[[-3.004675,4.247832,5.266645,3.425339],[-9.641970,6.206782,1.163841,-8.044393],[3.325055,6.272447,9.119289,-3.672288],[3.039725,5.982409,5.622124,4.541248],[-1.026422,-7.988894,2.843466,5.836370],[-5.826368,6.581446,-5.082892,0.397513],[2.985225,2.337754,-6.909574,9.115555],[-1.445435,-1.399417,-4.073897,-4.403274],[3.428067,-1.442167,-4.208803,-2.482146],[-1.995731,-8.958954,1.983896,-5.581996],[-2.498419,0.618843,-9.604597,-1.432584],[8.282554,-5.975882,-9.970421,-4.092154]],[[6.260390,-7.589994,9.026738,-9.098945],[-4.883050,-6.881115,4.366430,1.519236],[-6.992851,-2.194931,8.539075,-3.786167],[3.275816,-7.502337,6.349304,0.536003],[-4.349552,-2.330945,-4.078632,5.199479],[3.963927,-9.161528,0.674450,7.369948],[-1.847363,-8.313308,-6.417127,1.647762],[7.384571,-3.575343,-1.882444,2.484394],[3.441144,-2.627297,6.653514,7.365494],[8.383772,1.454667,2.617509,7.404426],[-7.295671,0.615898,-1.762960,-4.979386],[9.849514,-4.042707,6.935139,-9.901442]],[[3.207821,-2.432011,-4.235686,5.080071],[-7.930343,-7.662340,7.330353,8.676089],[3.653448,6.494549,9.463812,5.468529],[-9.469174,9.266282,-1.840524,-4.476032],[-2.343378,-6.282615,-6.478157,4.023943],[-5.547307,-6.350040,9.413953,1.367326],[1.185872,-2.321430,-8.799392,7.121077],[2.929820,-0.614214,-5.198630,7.294668],[-7.852398,9.152576,7.130602,3.502233],[3.065009,-0.259481,1.641733,0.059491],[-5.816236,-5.900837,-3.576453,5.862751],[-7.822204,7.849050,-8.987958,9.101636]]], dtype = "float32")#candidate|4355|(11, 12, 4)|const|float32
uop_4356 = relay.log10(const_4355.astype('float32')) # shape=(11, 12, 4)
output = uop_4356
output2 = uop_4356
func_4372 = relay.Function([], output)
mod['func_4372'] = func_4372
mod = relay.transform.InferType()(mod)
mutated_mod['func_4372'] = func_4372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mutated_mod.get_global_var('func_4372')
call_4373 = func_4372_call()
output = call_4373
func_4374 = relay.Function([], output)
mutated_mod['func_4374'] = func_4374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4446 = func_4372_call()
call_4447 = func_4372_call()
func_2380_call = mod.get_global_var('func_2380')
func_2383_call = mutated_mod.get_global_var('func_2383')
var_4449 = relay.var("var_4449", dtype = "float64", shape = (728,))#candidate|4449|(728,)|var|float64
const_4450 = relay.const([5,5,-2,-6,8,-8,6,-1,-3,2,-4,3,-6,8,-7,1,2,4,2,2,-8,4,10,-8,2,6,10,1,-4,-1,9,-5,-10,4,-8,4,7,-4,3,-1,-2,1,8,-8,-3,5,3,-3,-10,-6,5,8,10,-8,-4,6,-8,9,-8,-8,6,-3,5,3,-6,4,1,-3,6,3,-2,7,5,4,3,-6,-7,-9,8,-6,10,-4,-5,-1,-10,-8,-3,-10,1,6,8,-4,-3,-5,-4,3,-4,5,8,8,-2,8,-3,6,6,9,-3,9,5,-7,9,-3,9,-2,-7,4,-9,5,-5,-10,-4,-5,2,-3,9,6,-9,1,-8,-6,-3,4,-3,6,1,-6,-4,2,-6,3,-4,-5,9,-3,-9,1,7,6,6,7,9,-2,8,-9,8,2,-2,-5,3,7,6,3,-3,5,-2,-7,-10,4,-3,-2,4,3,1,6,-7,-5,10,8,9,-5,10,4,2,-9,2,8,-7,1,-2,-1,9,-1,6,-4,-7,-9,-10,-8,-2,9,-8,9,9,-5,-8,-9,-2,8,4,-4,9,-7,-6,-3,-1,2,1,-5,3,3,-6,-10,5,-8,-10], dtype = "int8")#candidate|4450|(225,)|const|int8
call_4448 = relay.TupleGetItem(func_2380_call(relay.reshape(var_4449.astype('float64'), [13, 8, 7]), relay.reshape(const_4450.astype('int8'), [225,]), ), 2)
call_4451 = relay.TupleGetItem(func_2383_call(relay.reshape(var_4449.astype('float64'), [13, 8, 7]), relay.reshape(const_4450.astype('int8'), [225,]), ), 2)
func_1460_call = mod.get_global_var('func_1460')
func_1463_call = mutated_mod.get_global_var('func_1463')
var_4458 = relay.var("var_4458", dtype = "bool", shape = (882,))#candidate|4458|(882,)|var|bool
call_4457 = relay.TupleGetItem(func_1460_call(relay.reshape(var_4458.astype('bool'), [882,])), 0)
call_4459 = relay.TupleGetItem(func_1463_call(relay.reshape(var_4458.astype('bool'), [882,])), 0)
bop_4466 = relay.floor_divide(call_4457.astype('float32'), call_4448.astype('float32')) # shape=(2, 15, 225)
bop_4469 = relay.floor_divide(call_4459.astype('float32'), call_4451.astype('float32')) # shape=(2, 15, 225)
bop_4517 = relay.floor_mod(call_4457.astype('float64'), const_4450.astype('float64')) # shape=(2, 15, 225)
bop_4520 = relay.floor_mod(call_4459.astype('float64'), const_4450.astype('float64')) # shape=(2, 15, 225)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4521 = func_4372_call()
call_4522 = func_4372_call()
func_2780_call = mod.get_global_var('func_2780')
func_2784_call = mutated_mod.get_global_var('func_2784')
const_4527 = relay.const([-5.392727,-7.196699,7.818566,-5.309093,-7.434333,6.672808,8.001531,-4.842851,3.849315,0.571217,-5.959804,4.858519,4.712679,8.306475,-5.082564,5.400928,-0.922125,8.814463,9.534451,-9.895829,-4.742502,-8.977823,2.427564,-2.095042,7.356759,7.125256,7.993139,5.669723,-9.682918,0.802033,3.979845,0.377721,-8.793489,-6.487025,-9.234653,-3.774667,-3.351685,5.603670,6.195981,0.395123,5.411956,-4.490919,4.749683,1.567222,-6.183952,2.288228,6.810029,8.316011,5.039807,6.491200,0.766117,-1.103359,0.566471,2.498130,4.883231,3.174318,-9.121598,7.050055,8.598637,9.726600,-1.189376,-9.391295,-1.002808,4.238321,8.835297,4.921994,-9.819962,-0.442247,4.995050,-6.606215,-8.069463,3.378296,7.781052,3.980310,-3.624971,3.686660,2.903081,-5.558256,8.828145,2.133267,4.963978,1.672181,-5.424158,1.742976,-4.653226,-5.931319,8.228325,7.590600,1.778018,-4.676896,2.648829,-2.037717,7.394976,-7.294498,-6.972583,6.448635,1.077602,-5.792871,-4.001008,4.638889,4.278894,-7.348803,-8.079955,-4.840383,-1.131100,9.866800,-7.185075,-6.554815,-5.006861,-0.741666,-0.743547,-5.245656,0.673608,4.243948,-8.044599,-6.334932,-3.732449,6.528345,-4.042770,-9.571380,-7.559609,-1.999404,3.433097,-3.528620,-7.483507,6.251642,-9.701342,-6.330604,-6.204562,2.656416,-9.564636,-2.891390,-2.396218,8.686625,0.104387,4.250263,7.284968,-4.645290,-9.047767,5.707651,-7.686336,1.547886,-4.782421,-8.736933,1.491101,-7.656010,8.895349,5.441617,-6.526055,-1.120995,-4.468541,1.359411,8.964869,7.590038,-4.228483,-4.233814,2.675646,3.551250,5.151925,-0.642875,8.938671,8.321128,3.787224,2.819550,0.488637,-3.462123,5.796244,-3.397708,0.908398,3.769624,-2.179712,-2.860140,0.436801,8.513196,7.544426,-8.264642,-9.552830,8.124855,-5.414780,6.314180,-8.136498,2.919336,2.313573,5.249761,1.290869,-6.769096,-3.590010,6.952409,-5.672489,0.736704,-9.635464,0.821665,5.771835,6.463983,7.802612,1.659491,-8.590337,6.104494,-8.863495,-2.745447,2.832583,9.760940,-7.357952,-4.807520,-0.929252,-2.010638,7.598351,9.266832,5.232072,-8.372738,-2.038853,-1.834402,-3.789800,-7.309025,-3.575632,6.022738,-1.281882,-3.241797,4.014443,6.942168,-4.686765,2.815718,1.842796,-5.780775,4.071749,2.912291,-1.013109,-6.095280,-0.365415,-5.358796,4.126337,-7.887259,-7.224100,-8.021226,2.045404,0.052641,-3.212627,8.788541,-0.167606,-5.850018,-1.991642,0.279916,2.570770,-5.960495,-2.126609,3.941902,-6.030621,1.930459,-0.712405,-6.820528,-8.297107,3.928917,-6.625484,-0.267534,-3.730643,-0.592981,8.869209,5.142580,3.857335,-1.786433,-6.820577,-9.278038,8.170348,-6.145272,9.701939,-8.712556,-6.688403,-8.396143,-7.658443,3.342833,9.671758,-2.674532,7.425441,-1.780317,8.670091,0.546272,-7.136526,-8.262281,4.278054,6.502507,9.967185,-8.716037,2.393039,6.999408,-7.200665,-7.661333,-2.095384,-4.362101,-1.073324,8.292484,7.168692,-0.551412,-5.912234,5.909717,8.676795,-4.307500,-5.120116,-9.124809,-7.701154,-0.473420,4.763068,-7.838021,8.679606,1.962499,2.573590,5.801032,3.763749,-1.211852,-6.013100,-2.893350,-4.064431,-8.954762,2.406674,-7.378438,-1.164056,-5.612175,7.596371,-5.611822,5.827492,0.139456,-7.132521,9.164005,-9.405613,9.418799,-0.563972,-6.876702,-4.271571,0.383967,4.014575,4.789822,-5.360908,2.314732,8.963219,-7.672559,-7.999518,3.106383,-6.426300,-7.510754,0.293167,3.766321,1.050223,-0.250325,4.222313,-0.562723,-0.163492,-3.180532,3.852389,-2.909732,7.038740,-6.939443,-3.999559,-8.500817,-9.386234,7.066108,-1.361038,4.487118,-4.209752,-1.492856,-8.675933,8.348640,-1.423873,4.647730,8.209514,-1.081436,6.992498,-1.104347,8.149844,-1.693536,-5.565896,7.014776,8.390877,-5.331669,-4.661407,9.911867,8.637594,5.206669,-8.820478,-7.484448,6.748224,2.312177,7.350255,-1.417799,-4.998144,-7.945439,4.597310,-9.393459,2.468790,-2.433789,0.031325,-2.134869,-7.619718,-5.034928,-4.826987,6.559490,-4.479661,-2.228839,-1.014050,-1.833701,-7.150124,6.062148,-1.197228,-5.785757,8.238536,6.844837,-5.969120,1.372733,-1.758293,3.031970,-0.572342,-1.600155,0.996300,-1.665297,3.555316,6.252094,-0.876008,9.350648,-1.596502,-5.298580,6.101818,-8.619045,0.820365,-3.783400,2.605947,-4.205481,-6.483558,-1.185959,-1.582289,-5.448169,0.544805,6.508452,-5.875153,-7.416523,-8.856149,-6.837052,7.379398,6.166799,1.771930,-9.435147,4.003840,-6.598465,8.200976,-9.185005,-3.665090,0.954235,-7.840179,6.480843,-9.255378,7.478411,-4.167281,-2.916485,-6.227970,-4.823627,2.413432,-7.939147,8.933678,2.061705,-2.548384,-0.628762,-6.659794,-4.620331,-7.026609,2.830913,-3.160228,3.476316,4.094889,-5.490331,3.394996,9.342329,1.252220,-5.618959,-8.564531,0.522331,0.891628,2.654472,1.425979,-3.988288,1.916444,-3.042271,-9.647388,-6.502556,1.615278,5.507291,4.704188,-7.436120,-6.525870,-7.529218,-9.656503,5.492797,4.111828,2.416606,2.988334,4.391396,1.695280,-9.326887,4.991828,9.287365,4.962986,-4.444251,9.974579,1.363022,9.021861,2.949140,1.469946,0.275140,1.587262,3.706110,-3.632616,-2.221110,4.309789,5.448558,1.748590,4.544546,1.132436,-6.141075,-1.532723,-6.019911,2.566829,2.884795,1.201145,9.224836,0.398241,5.021727,8.540683,-0.219092,-0.254842,-3.617144,-3.370184,-2.048794,4.723695,3.512475,-5.543420,5.065033,9.035092,-2.325466,4.886955,9.074123,-0.103201,-7.809123,-3.038770,-4.057988,-6.329790,2.192520,8.501251,-8.673757,-4.563270,-2.002122,2.994534,-7.635924,5.716089,8.497960,-4.378332,5.280326,2.174720,5.925575,-0.936034,-5.760021,-0.720204,-8.768293,4.138712,-1.264203,-1.635781,-6.750412,-3.222077,-2.801231,8.726558,-9.114566,-1.571097,9.820937,7.755947,-7.022029,-0.982209,-4.551131,-1.885430,-8.808885,7.333199,3.974953,-9.187925,6.234209,-8.660654,-4.295654,-6.800200,1.426192,-0.315089,-5.246978,9.059368,-6.676593,-8.310214,-4.030524,9.787606,-8.703435,1.678239,-0.232399,-9.539679,-6.146916,6.662623,-8.576956,3.063497,-3.321105,-7.566998,5.593417,5.767674,-6.059137,-2.823906,-7.804065,8.029129,-4.691881,-5.025968,-8.900163,9.079380,6.358835,2.942691,-0.806631,-0.101781,3.026419,7.257262,-3.166508,-5.742750,-5.220443,-1.010111,-0.459913,-2.031886,-6.514868,7.321242,9.818176,-2.819139,2.101529,-8.743396,-7.914756,-0.132879,-3.531260,5.426222,7.990068,8.344722,-2.432427,-0.222123,0.550466,-7.626690,-9.296626,1.426757,-7.343491,-2.520896,1.752286,1.733121,9.921761,6.968032,6.501909,4.115317,-7.722162,7.452526,-5.119245,7.528393,-4.760932,6.684781,4.451623,-5.648017,-4.357745,7.866955,6.410379,-8.616137,0.436388,-1.871780,-5.793112,2.118421,-9.421726,6.283307,-8.647563,4.751830,-8.927807,6.801630,9.050746,7.763721,6.074186,5.593953,7.387115,9.283874,-7.405377,-3.401620,4.490306,6.581956,-7.451467,-4.739353,-4.617605,4.357952,8.186272,-8.240556,-0.088170,-9.541973,3.367387,-2.650187,0.513698,8.005243,-9.239444,-9.993881,1.140610,0.039551,5.429877,-8.923902,9.728332,-3.136403,3.007834], dtype = "float32")#candidate|4527|(700,)|const|float32
call_4526 = relay.TupleGetItem(func_2780_call(relay.reshape(const_4527.astype('float32'), [5, 14, 10]), relay.reshape(var_4458.astype('bool'), [882,]), ), 0)
call_4528 = relay.TupleGetItem(func_2784_call(relay.reshape(const_4527.astype('float32'), [5, 14, 10]), relay.reshape(var_4458.astype('bool'), [882,]), ), 0)
bop_4529 = relay.less_equal(bop_4517.astype('bool'), call_4457.astype('bool')) # shape=(2, 15, 225)
bop_4532 = relay.less_equal(bop_4520.astype('bool'), call_4459.astype('bool')) # shape=(2, 15, 225)
output = relay.Tuple([call_4446,var_4449,var_4458,bop_4466,call_4521,call_4526,const_4527,bop_4529,])
output2 = relay.Tuple([call_4447,var_4449,var_4458,bop_4469,call_4522,call_4528,const_4527,bop_4532,])
func_4535 = relay.Function([var_4449,var_4458,], output)
mod['func_4535'] = func_4535
mod = relay.transform.InferType()(mod)
mutated_mod['func_4535'] = func_4535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4535_call = mutated_mod.get_global_var('func_4535')
var_4537 = relay.var("var_4537", dtype = "float64", shape = (728,))#candidate|4537|(728,)|var|float64
var_4538 = relay.var("var_4538", dtype = "bool", shape = (882,))#candidate|4538|(882,)|var|bool
call_4536 = func_4535_call(var_4537,var_4538,)
output = call_4536
func_4539 = relay.Function([var_4537,var_4538,], output)
mutated_mod['func_4539'] = func_4539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4610 = func_4372_call()
call_4611 = func_4372_call()
func_2596_call = mod.get_global_var('func_2596')
func_2600_call = mutated_mod.get_global_var('func_2600')
var_4614 = relay.var("var_4614", dtype = "float64", shape = (2, 336))#candidate|4614|(2, 336)|var|float64
call_4613 = func_2596_call(relay.reshape(var_4614.astype('float64'), [7, 12, 8]), relay.reshape(var_4614.astype('float64'), [7, 12, 8]), )
call_4615 = func_2596_call(relay.reshape(var_4614.astype('float64'), [7, 12, 8]), relay.reshape(var_4614.astype('float64'), [7, 12, 8]), )
uop_4616 = relay.log(call_4613.astype('float64')) # shape=(7, 12, 8)
uop_4618 = relay.log(call_4615.astype('float64')) # shape=(7, 12, 8)
output = relay.Tuple([call_4610,var_4614,uop_4616,])
output2 = relay.Tuple([call_4611,var_4614,uop_4618,])
func_4622 = relay.Function([var_4614,], output)
mod['func_4622'] = func_4622
mod = relay.transform.InferType()(mod)
mutated_mod['func_4622'] = func_4622
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4623 = relay.var("var_4623", dtype = "float64", shape = (2, 336))#candidate|4623|(2, 336)|var|float64
func_4622_call = mutated_mod.get_global_var('func_4622')
call_4624 = func_4622_call(var_4623)
output = call_4624
func_4625 = relay.Function([var_4623], output)
mutated_mod['func_4625'] = func_4625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4720 = func_4372_call()
call_4721 = func_4372_call()
output = call_4720
output2 = call_4721
func_4727 = relay.Function([], output)
mod['func_4727'] = func_4727
mod = relay.transform.InferType()(mod)
mutated_mod['func_4727'] = func_4727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mutated_mod.get_global_var('func_4727')
call_4728 = func_4727_call()
output = call_4728
func_4729 = relay.Function([], output)
mutated_mod['func_4729'] = func_4729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4763 = func_4372_call()
call_4764 = func_4372_call()
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
const_4767 = relay.const([True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True], dtype = "bool")#candidate|4767|(882,)|const|bool
call_4766 = relay.TupleGetItem(func_1401_call(relay.reshape(const_4767.astype('bool'), [14, 7, 9])), 0)
call_4768 = relay.TupleGetItem(func_1403_call(relay.reshape(const_4767.astype('bool'), [14, 7, 9])), 0)
func_1460_call = mod.get_global_var('func_1460')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_4772 = relay.TupleGetItem(func_1460_call(relay.reshape(call_4766.astype('bool'), [882,])), 1)
call_4773 = relay.TupleGetItem(func_1463_call(relay.reshape(call_4766.astype('bool'), [882,])), 1)
output = relay.Tuple([call_4763,call_4766,const_4767,call_4772,])
output2 = relay.Tuple([call_4764,call_4768,const_4767,call_4773,])
func_4774 = relay.Function([], output)
mod['func_4774'] = func_4774
mod = relay.transform.InferType()(mod)
mutated_mod['func_4774'] = func_4774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mutated_mod.get_global_var('func_4774')
call_4775 = func_4774_call()
output = call_4775
func_4776 = relay.Function([], output)
mutated_mod['func_4776'] = func_4776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_4829 = relay.TupleGetItem(func_4774_call(), 2)
call_4830 = relay.TupleGetItem(func_4776_call(), 2)
output = relay.Tuple([call_4829,])
output2 = relay.Tuple([call_4830,])
func_4850 = relay.Function([], output)
mod['func_4850'] = func_4850
mod = relay.transform.InferType()(mod)
mutated_mod['func_4850'] = func_4850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4850_call = mutated_mod.get_global_var('func_4850')
call_4851 = func_4850_call()
output = call_4851
func_4852 = relay.Function([], output)
mutated_mod['func_4852'] = func_4852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_4871 = relay.TupleGetItem(func_4774_call(), 3)
call_4872 = relay.TupleGetItem(func_4776_call(), 3)
output = relay.Tuple([call_4871,])
output2 = relay.Tuple([call_4872,])
func_4873 = relay.Function([], output)
mod['func_4873'] = func_4873
mod = relay.transform.InferType()(mod)
output = func_4873()
func_4874 = relay.Function([], output)
mutated_mod['func_4874'] = func_4874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4886 = func_4372_call()
call_4887 = func_4372_call()
var_4897 = relay.var("var_4897", dtype = "float32", shape = (11, 12, 4))#candidate|4897|(11, 12, 4)|var|float32
bop_4898 = relay.mod(call_4886.astype('float64'), relay.reshape(var_4897.astype('float64'), relay.shape_of(call_4886))) # shape=(11, 12, 4)
bop_4901 = relay.mod(call_4887.astype('float64'), relay.reshape(var_4897.astype('float64'), relay.shape_of(call_4887))) # shape=(11, 12, 4)
uop_4916 = relay.sin(var_4897.astype('float64')) # shape=(11, 12, 4)
output = relay.Tuple([bop_4898,uop_4916,])
output2 = relay.Tuple([bop_4901,uop_4916,])
func_4924 = relay.Function([var_4897,], output)
mod['func_4924'] = func_4924
mod = relay.transform.InferType()(mod)
var_4925 = relay.var("var_4925", dtype = "float32", shape = (11, 12, 4))#candidate|4925|(11, 12, 4)|var|float32
output = func_4924(var_4925)
func_4926 = relay.Function([var_4925], output)
mutated_mod['func_4926'] = func_4926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_4954 = func_4727_call()
call_4955 = func_4727_call()
output = relay.Tuple([call_4954,])
output2 = relay.Tuple([call_4955,])
func_4961 = relay.Function([], output)
mod['func_4961'] = func_4961
mod = relay.transform.InferType()(mod)
mutated_mod['func_4961'] = func_4961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4961_call = mutated_mod.get_global_var('func_4961')
call_4962 = func_4961_call()
output = call_4962
func_4963 = relay.Function([], output)
mutated_mod['func_4963'] = func_4963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4873_call = mod.get_global_var('func_4873')
func_4874_call = mutated_mod.get_global_var('func_4874')
call_5005 = relay.TupleGetItem(func_4873_call(), 0)
call_5006 = relay.TupleGetItem(func_4874_call(), 0)
uop_5018 = relay.tan(call_5005.astype('float64')) # shape=(14, 7, 9)
uop_5020 = relay.tan(call_5006.astype('float64')) # shape=(14, 7, 9)
func_2491_call = mod.get_global_var('func_2491')
func_2495_call = mutated_mod.get_global_var('func_2495')
const_5032 = relay.const([[-8,-5,3,-2,10,-1,3,6,5,-9,-1,9,9],[-6,9,-6,-8,-1,-6,2,-7,7,-5,8,-8,-6],[-7,2,2,-8,-1,10,-5,2,4,-7,9,2,9],[-3,-6,-10,5,6,-8,-10,9,10,-1,-5,-8,-5],[-8,-8,-7,-8,1,-6,7,-6,8,-6,8,-1,8],[-3,8,-1,6,-5,-4,8,8,4,5,2,5,-10],[-2,3,7,-6,5,3,-1,-4,9,10,3,-5,-3],[-4,3,-3,-7,6,-10,10,4,-7,-2,-7,1,8],[-9,-6,8,-3,6,-7,-10,-10,7,-8,-3,-5,-5],[6,10,-4,5,-3,10,5,2,2,6,4,1,-6],[6,1,-4,9,-1,4,3,-10,-3,-2,10,7,-5],[1,3,-4,1,-4,2,-8,8,-10,9,-5,-8,9],[10,-4,-9,5,-4,-2,-4,-9,-2,1,9,1,3],[4,1,-7,-9,10,-8,1,3,7,2,8,-3,3],[2,1,8,-7,1,3,-7,-10,-7,-8,-4,10,1],[9,-8,-7,4,8,-5,2,8,-8,8,1,6,-6],[4,-8,7,-8,-10,5,-5,8,7,8,7,2,1],[-1,-3,-9,4,-2,5,-5,-7,8,5,-3,-6,-10],[4,-8,-5,4,-5,-5,-10,-9,-6,-7,7,4,1],[-6,6,-10,8,-9,-7,3,6,9,6,1,4,-5],[-5,-3,-6,-3,-5,-5,3,5,7,-1,7,-10,-10],[5,1,5,8,-2,8,-9,10,-5,-9,4,10,10],[-5,-10,-1,7,6,-6,9,-1,3,10,-5,8,-7],[10,6,-7,-8,6,-4,1,-4,-4,-5,1,-4,-1],[6,-1,-4,10,-10,-10,6,10,-8,7,8,-4,6],[-10,6,9,3,-7,-2,-6,6,3,-4,9,3,-6],[9,3,7,8,-5,7,9,-4,3,-3,7,-10,-8],[5,-6,4,2,5,-1,3,1,5,-4,-1,2,-5],[-10,2,-3,-1,9,-8,-3,8,-7,-3,1,-8,-8],[1,3,-8,10,-10,8,-3,7,8,2,7,9,8],[7,-6,-5,6,4,10,6,6,-3,1,-8,-3,2],[-2,9,2,7,2,6,1,-2,3,-3,9,8,8],[-6,-10,1,3,3,-6,3,4,6,7,-8,-3,9],[-9,-4,3,-7,2,7,10,1,2,-3,-1,-4,4],[-7,5,3,-3,2,-8,-10,-9,-8,-7,-4,-10,5],[-6,8,-3,9,2,-3,-10,2,-3,10,9,10,4],[-5,1,-4,1,6,-8,3,8,7,-2,-6,1,-7],[-4,4,-1,2,1,6,9,-7,7,-9,7,-3,-4],[3,6,6,7,8,9,9,-6,-3,6,-2,-1,10]], dtype = "int64")#candidate|5032|(39, 13)|const|int64
call_5031 = relay.TupleGetItem(func_2491_call(relay.reshape(const_5032.astype('int64'), [13, 3, 13]), relay.reshape(const_5032.astype('int64'), [13, 3, 13]), relay.reshape(const_5032.astype('bool'), [13, 3, 13]), ), 3)
call_5033 = relay.TupleGetItem(func_2495_call(relay.reshape(const_5032.astype('int64'), [13, 3, 13]), relay.reshape(const_5032.astype('int64'), [13, 3, 13]), relay.reshape(const_5032.astype('bool'), [13, 3, 13]), ), 3)
const_5038 = relay.const([[5,6,3,2,2,-8,9,-1,-1,8,4,-5,3],[10,-8,7,-8,-5,-10,2,2,-5,2,-1,8,-1],[7,9,6,4,-4,-1,6,1,4,8,-7,-8,10],[10,-3,10,6,2,1,-10,-8,5,-9,-10,2,-1],[-4,8,2,-1,8,7,-3,10,4,6,2,-6,8],[6,-5,-10,7,2,-5,-4,-4,-7,-9,-10,-8,5],[-8,1,-6,-9,-3,7,-7,9,1,5,6,2,-10],[10,-1,-5,5,-6,-4,-9,3,9,4,4,-5,3],[-10,7,-9,7,4,-6,10,8,-6,3,5,-9,-1],[-6,-1,-6,-4,-10,-3,-1,-9,-4,1,-2,-2,-4],[6,8,8,2,5,-10,-4,-1,7,4,1,6,-1],[-6,-5,10,8,9,-1,3,10,4,4,-2,9,9],[-1,1,3,-5,-10,10,-10,-3,-9,-9,-10,4,8],[6,-2,-5,-10,-7,6,1,-6,3,9,8,-4,8],[10,9,10,3,-2,4,-7,-5,2,8,-7,5,8],[-6,2,8,8,10,-7,-7,-5,9,4,4,9,4],[-4,-2,4,-7,-1,-10,4,-4,-5,8,-6,4,2],[-5,-10,7,-10,8,-8,-2,-10,8,4,-5,-5,-1],[-1,-10,-2,3,6,8,8,1,9,-5,-8,2,-4],[-3,9,1,-8,2,8,2,5,1,3,1,5,-2],[-8,-7,1,-3,-3,-2,-7,-8,2,-10,-9,-2,1],[4,-9,3,1,10,-9,4,-7,-2,3,-1,10,-5],[10,-1,1,1,4,-7,-3,6,-8,-3,-9,9,-6],[8,-10,7,10,-5,5,-3,9,3,5,-3,2,-7],[-2,2,7,-6,-4,-10,-10,7,10,-4,8,-2,-7],[-7,4,7,-2,-6,2,7,6,10,4,-1,7,-5],[3,1,4,-8,-4,6,5,-7,5,-10,-3,7,10],[-4,-5,6,-6,-7,-5,-1,-1,8,-1,10,-1,9],[5,-3,-5,-3,-6,8,8,-4,-4,3,-6,-9,8],[-4,-4,-4,8,3,6,4,9,-4,1,9,5,-9],[4,7,-9,-10,-4,1,4,5,-2,-2,1,7,5],[5,9,-2,-4,-7,-10,6,-3,-5,-1,-9,-9,3],[8,-2,-5,3,-5,-8,-4,1,-4,-9,4,-6,-6],[7,7,-5,-9,7,8,-9,-7,-1,4,6,-1,-4],[10,-1,6,-2,-9,7,-8,3,6,-10,-10,3,-4],[-9,5,1,3,10,1,2,10,7,6,3,-3,5],[3,7,-9,4,2,-9,-9,-6,-2,-10,10,8,9],[-5,2,8,-10,-5,-3,-2,6,2,2,-8,8,5],[-7,-3,-4,-1,-10,4,-5,-8,-9,3,-2,3,-3]], dtype = "int64")#candidate|5038|(39, 13)|const|int64
bop_5039 = relay.subtract(const_5032.astype('float64'), relay.reshape(const_5038.astype('float64'), relay.shape_of(const_5032))) # shape=(39, 13)
output = relay.Tuple([uop_5018,call_5031,bop_5039,])
output2 = relay.Tuple([uop_5020,call_5033,bop_5039,])
func_5054 = relay.Function([], output)
mod['func_5054'] = func_5054
mod = relay.transform.InferType()(mod)
output = func_5054()
func_5055 = relay.Function([], output)
mutated_mod['func_5055'] = func_5055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_5126 = relay.TupleGetItem(func_5054_call(), 1)
call_5127 = relay.TupleGetItem(func_5055_call(), 1)
func_4535_call = mod.get_global_var('func_4535')
func_4539_call = mutated_mod.get_global_var('func_4539')
var_5134 = relay.var("var_5134", dtype = "float64", shape = (728,))#candidate|5134|(728,)|var|float64
var_5135 = relay.var("var_5135", dtype = "bool", shape = (14, 63))#candidate|5135|(14, 63)|var|bool
call_5133 = relay.TupleGetItem(func_4535_call(relay.reshape(var_5134.astype('float64'), [728,]), relay.reshape(var_5135.astype('bool'), [882,]), ), 5)
call_5136 = relay.TupleGetItem(func_4539_call(relay.reshape(var_5134.astype('float64'), [728,]), relay.reshape(var_5135.astype('bool'), [882,]), ), 5)
output = relay.Tuple([call_5126,call_5133,var_5134,var_5135,])
output2 = relay.Tuple([call_5127,call_5136,var_5134,var_5135,])
func_5139 = relay.Function([var_5134,var_5135,], output)
mod['func_5139'] = func_5139
mod = relay.transform.InferType()(mod)
mutated_mod['func_5139'] = func_5139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5139_call = mutated_mod.get_global_var('func_5139')
var_5141 = relay.var("var_5141", dtype = "float64", shape = (728,))#candidate|5141|(728,)|var|float64
var_5142 = relay.var("var_5142", dtype = "bool", shape = (14, 63))#candidate|5142|(14, 63)|var|bool
call_5140 = func_5139_call(var_5141,var_5142,)
output = call_5140
func_5143 = relay.Function([var_5141,var_5142,], output)
mutated_mod['func_5143'] = func_5143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_5188 = func_4372_call()
call_5189 = func_4372_call()
func_1137_call = mod.get_global_var('func_1137')
func_1139_call = mutated_mod.get_global_var('func_1139')
const_5205 = relay.const([-9.186132,-6.416730,-9.949568,-0.954184,1.006077,3.096364,-5.499658,-6.387804,-9.327859,-3.622048,5.058110,-1.936307,-7.164990,6.428103,0.798735,3.933781,3.408164,-6.324807,-1.737768,2.344290,-7.369074,5.584201,1.976032,-7.048928,-6.534926,2.047504,2.526406,-7.138141,4.217065,9.632189,-5.986647,-2.222561,-3.832090,4.604526,7.420671,-3.652052,3.860022,-1.084195,-7.899033,-4.005387,5.781439,-4.449137,-6.139929,-3.802950,-6.518289,-2.626834,5.699741,-0.166004,7.069605,-1.579242,5.481267,-6.067868,7.613050,2.604185,-7.538734,-5.336436,-5.704728,-5.210954,0.874712,-1.044963,-3.887238,-4.176444,-2.591732,-9.358058,-9.678547,-5.313041,8.912632,-3.621298,-1.248583,-8.840299,-9.915258,-3.384369,-6.977561,2.103862,-5.295341,9.688706,-6.922667,-8.856384,3.827173,-1.172721,3.910002,6.613025,5.211429,3.626294,4.066604,-3.454853,-9.278148,-1.232053,4.817048,-7.606883,-0.298031,1.168488,4.977031,1.991068,-5.770055,-6.581498,-6.794383,-8.320035,-7.021430,8.607893,-4.487797,9.448304,7.822134,2.438451,9.883080,-5.414301,4.906446,-9.173531,8.388854,5.637682,6.452819,0.173337,2.721351,2.681173,-6.578160,-6.714683,6.188555,6.452580,1.227567,3.262515,8.611018,-1.002922,4.778905,2.425175,-3.468456,-0.601879,8.543077,-2.198569,-3.677866,-1.822803,-5.459979,8.232815,-5.633014,-4.710750,4.965999,-9.625140,4.789224,2.662749,1.801826,6.603116,-6.073969,4.921043,-8.505023,-2.442998,0.596027,6.287928,0.439560,3.744809,6.822349,-0.032252,-3.723031,2.683870,4.580919,-4.269989,-1.072284,0.500529,-0.813060,-2.805332,-2.088806,0.187130,7.908377,2.043545,0.578794,-5.772801,4.909499,2.439799,1.651635,9.292331,6.964938,6.114770,-4.315575,-3.133989,5.184983,4.267745,-9.194602,4.204340,8.324434,-6.704780,-6.067981,8.568674,0.105155,5.948102,-1.975676,-6.502353,-5.822383,5.118819,-2.316356,5.819311,-7.768627,8.311681,4.555409,-2.952644,9.982109,0.679013,4.583827,6.097285,8.276843,9.430483,-1.617894,-4.866755,8.346874,7.116528,9.335075,9.771331,2.624219,-2.615074,3.076814,9.055641,-8.146922,-0.840382,2.194131,-6.375265,-0.478681,-9.519320,7.678226,-0.184758,-4.015925,-1.280150,-8.206256,1.082197], dtype = "float64")#candidate|5205|(220,)|const|float64
call_5204 = relay.TupleGetItem(func_1137_call(relay.reshape(const_5205.astype('float64'), [4, 5, 11])), 0)
call_5206 = relay.TupleGetItem(func_1139_call(relay.reshape(const_5205.astype('float64'), [4, 5, 11])), 0)
func_2780_call = mod.get_global_var('func_2780')
func_2784_call = mutated_mod.get_global_var('func_2784')
const_5208 = relay.const([-4.877783,6.489931,-1.623650,-9.061495,-6.888946,0.991694,-9.714782,-0.374294,3.411711,-8.144067,-5.370953,5.022229,4.896395,-4.108016,-5.533335,-7.548182,0.284727,2.285128,-3.016459,-6.847794,-9.271576,1.705666,-7.281746,9.345614,-1.038394,-6.479122,6.918163,-0.559022,-4.336137,9.288561,4.406901,7.588010,1.047939,-6.673428,6.847434,0.837999,-5.752002,-2.440100,-9.167283,-5.517193,-3.660324,-3.752565,-9.392442,-9.017124,5.777714,6.649406,8.455614,9.319767,-1.639142,-9.215586,8.481482,4.129730,-4.500469,-1.479612,2.468766,-0.400698,4.631904,3.706163,9.846571,-1.805542,4.049206,8.271516,8.884074,-5.709153,-1.313739,0.501196,-8.673907,5.893097,-0.965996,8.507893,8.509855,0.403708,-7.878500,-2.418956,-0.233099,3.941190,4.931081,0.703259,0.153512,-1.746541,-3.547668,1.333698,-5.282044,-7.695049,-1.064535,-1.091287,5.393350,5.698750,3.713736,3.482376,-7.282480,1.114138,-6.254863,-6.352900,-5.353784,0.261171,-7.146334,2.638655,-9.409976,-5.820813,-0.906418,-0.261954,-3.049887,0.402875,7.660700,-2.360937,3.672850,8.855402,-3.608831,-9.938434,-0.369401,2.407606,-8.691041,2.863558,-9.292073,-5.413643,3.958468,-7.825825,-8.172424,4.510402,0.904223,0.862404,7.345729,-0.102693,3.387372,4.033790,-9.846641,-1.702288,1.355211,6.623087,9.904644,-1.312643,-0.893595,0.296754,4.855390,9.829289,-6.394508,5.387610,7.257239,7.161389,-5.057089,1.522229,3.968718,-6.041664,9.300625,0.148571,9.541389,9.727683,-1.913568,-2.504448,9.762656,-4.633064,-7.183887,-9.019598,7.721669,-4.225218,-1.218087,0.854855,-9.119841,-6.743804,0.775582,-6.139061,-4.746617,3.158108,-2.145699,-0.255401,0.218271,3.390895,-2.205614,8.325041,6.791581,-1.187772,1.075460,-4.436376,9.978471,-4.449564,-8.168953,1.838648,-2.238940,7.450085,-0.072620,7.074674,1.546637,2.497797,-8.160674,8.990498,4.731600,4.311012,9.000164,-9.295502,-1.829974,-4.708458,0.932730,2.348512,-1.831979,6.300482,-6.047268,-6.753149,4.731237,-0.264397,-2.176220,-0.910817,2.540108,1.910120,0.491307,5.408147,-4.153674,-9.020491,3.782109,9.453853,-0.922471,-1.626303,0.161560,-5.794867,-4.347083,-7.682478,3.865914,-4.303487,-1.209134,3.592643,6.667451,-2.752212,-7.721843,-4.687351,-0.765731,1.965492,-6.248613,-5.641418,-9.112388,-2.975399,2.125538,-3.497603,7.822369,6.676930,-3.569523,8.997489,9.581655,1.485774,-9.217841,7.495836,5.908934,-8.937728,-2.676112,-0.801528,0.512010,3.285496,4.862259,9.243025,9.532205,0.196728,-8.979770,2.390899,-3.503976,3.652670,-0.264517,8.772677,-9.267271,3.792793,-8.706597,4.257474,7.232949,-8.702017,-7.900724,9.283317,-1.553842,3.956156,-5.825575,-5.713440,3.747151,1.062355,-0.851841,-4.255098,-1.228068,1.989590,1.781141,4.604272,-4.011951,1.989045,9.884262,-9.218298,7.353410,-7.150495,-5.704501,-1.594589,0.344030,-3.975584,0.672919,-5.394608,-2.208323,-4.775233,-0.515639,-5.333705,-3.180624,-2.050525,1.806861,8.137732,-0.658956,-8.284052,3.738616,7.265212,-3.548411,-3.505971,-7.435101,-4.470213,2.147419,-2.941782,-6.594746,-7.823347,-5.293289,-2.742377,9.275124,4.649676,-2.593249,-5.847310,-6.874319,-8.956489,4.810966,-5.740161,2.925525,1.023125,-0.057486,-0.187197,-2.116709,2.837204,9.869447,-3.399342,5.669800,0.055627,2.705765,6.503686,2.166431,5.487240,1.183994,-0.004246,-7.932636,7.946129,1.932650,0.770297,-6.377454,-0.737762,-9.551584,-8.343555,-5.717089,9.447707,3.796274,-6.572850,-9.396638,-9.950851,7.442950,-4.203469,-0.846546,-7.747454,-7.563095,9.926393,-9.224233,-1.967128,8.290318,6.489729,-1.529965,9.180625,1.345358,-7.498168,6.329719,0.175074,4.490941,-9.701394,1.796752,6.928660,-9.685265,-0.296611,4.923923,-8.881990,4.322076,-5.251342,-6.346200,-1.392257,7.408614,-6.898428,7.850678,-1.939571,2.086847,-7.485394,6.144212,-6.626707,-2.840369,3.147790,-7.152173,-3.002571,9.866699,6.384755,0.117447,3.567330,6.709541,9.478032,-0.079131,0.379337,3.067966,-4.623702,-4.405069,-5.735297,-6.757065,-4.222645,9.373121,-7.019127,6.126985,8.917449,1.419460,-4.356427,-1.660032,7.869299,2.925134,-3.339742,-9.207640,8.967710,-5.390778,-0.843929,6.361886,1.486670,4.029763,9.945075,9.229994,3.089416,-6.609075,0.873243,-8.889359,5.139344,-6.742156,-2.827654,-8.206331,4.134279,5.685751,0.778936,-5.434549,-4.516161,3.043399,-9.338333,-3.284460,5.409578,6.404731,2.737118,-1.837469,8.130806,-8.807456,1.020553,-1.114586,4.177499,-8.825793,-3.529365,1.787983,7.393851,3.022967,-4.235145,9.332961,-3.663888,-2.715460,-6.927333,-2.769917,9.930008,2.503377,1.328229,0.895934,-3.766805,-7.902283,-1.792141,6.501353,-8.823762,-4.456644,-5.582324,-1.805788,-3.725200,-3.345956,4.809194,6.514710,9.624939,-1.955017,-3.952765,-0.431706,3.300688,2.194000,-3.901477,8.066285,2.001190,4.094269,-1.438852,-6.707921,1.376938,3.846614,2.072254,0.206350,-1.578231,-4.643532,-5.904266,2.425886,5.391886,1.440946,6.969698,-8.288582,-6.810921,-1.439730,0.623992,-8.105354,3.012295,-1.045261,-7.980941,1.706670,6.562794,6.605713,-4.581449,2.255936,7.605131,-7.414639,-3.936701,-8.506599,-4.559742,5.709550,2.000370,-9.071142,5.578133,-7.194457,1.129707,-3.574072,1.739047,-8.703698,-3.771937,3.711091,-0.415870,-5.188951,-3.486422,-8.553842,0.802525,-0.144122,8.378970,3.403927,8.967408,-5.109919,-3.557752,3.581643,-6.156698,2.853479,-8.695287,-9.109943,-7.933999,0.729675,5.245024,-9.403586,4.535066,-9.496161,1.876359,8.680494,5.024499,1.096748,2.509894,6.962692,-4.166254,-2.848339,2.809697,-7.933818,-8.339999,-5.187476,8.736486,-2.557642,1.824124,6.525170,8.921416,-0.849220,-1.686836,-3.684376,-2.777099,9.529402,-8.861555,8.721064,-4.478419,-1.423207,1.965335,7.966134,5.678003,5.278641,-3.380349,8.592400,-7.672261,-5.111682,-8.539434,-6.783031,-8.324035,6.844979,3.741550,-0.945889,-0.457421,-8.182143,2.032183,-6.190612,-7.111653,5.270712,-1.066568,-6.717079,-1.549039,3.577019,2.559073,-0.767922,4.919064,-6.877312,-8.430398,7.881690,3.734771,3.717890,8.762505,8.739919,3.931175,-2.121375,-1.752406,-5.172364,3.107662,2.737219,8.138624,-3.104095,6.961275,-0.410573,8.788451,4.198675,9.242618,6.750691,-4.478366,-9.952436,2.080458,-7.229341,5.395064,7.898770,-8.592606,4.841733,-5.676812,9.642248,6.594236,6.043648,1.965905,3.845155,3.243644,2.832686,-0.047734,-9.287737,-2.714108,1.465326,9.470161,-3.825773,8.193929,-6.706995,0.438707,4.237037,1.041505,8.371397,6.868474,4.972113,1.888303,6.035295,0.628429,3.688218,-9.708140,0.177762,7.696928,7.450351,-2.111198,-3.457046,0.922601,-2.961357,1.622994,2.074837,-4.365805,2.474110,8.757808,3.315029,-9.698358,-9.676760,4.957005,5.434612,5.025848,8.841500,-0.488451,9.925482,-8.425476,-9.580609,9.181313,-3.380818,-6.964635,3.653797,-1.411522,-0.727510,-4.497904,8.970519,4.132198,-7.022732,-5.372825,-4.081613,-3.566700,-4.017774,0.774513,-5.105684,0.836657,-9.207293,-6.473342,0.088850,9.497782], dtype = "float32")#candidate|5208|(700,)|const|float32
var_5209 = relay.var("var_5209", dtype = "bool", shape = (882,))#candidate|5209|(882,)|var|bool
call_5207 = relay.TupleGetItem(func_2780_call(relay.reshape(const_5208.astype('float32'), [5, 14, 10]), relay.reshape(var_5209.astype('bool'), [882,]), ), 0)
call_5210 = relay.TupleGetItem(func_2784_call(relay.reshape(const_5208.astype('float32'), [5, 14, 10]), relay.reshape(var_5209.astype('bool'), [882,]), ), 0)
output = relay.Tuple([call_5188,call_5204,const_5205,call_5207,const_5208,var_5209,])
output2 = relay.Tuple([call_5189,call_5206,const_5205,call_5210,const_5208,var_5209,])
func_5215 = relay.Function([var_5209,], output)
mod['func_5215'] = func_5215
mod = relay.transform.InferType()(mod)
var_5216 = relay.var("var_5216", dtype = "bool", shape = (882,))#candidate|5216|(882,)|var|bool
output = func_5215(var_5216)
func_5217 = relay.Function([var_5216], output)
mutated_mod['func_5217'] = func_5217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_5229 = func_4727_call()
call_5230 = func_4727_call()
output = call_5229
output2 = call_5230
func_5245 = relay.Function([], output)
mod['func_5245'] = func_5245
mod = relay.transform.InferType()(mod)
output = func_5245()
func_5246 = relay.Function([], output)
mutated_mod['func_5246'] = func_5246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4873_call = mod.get_global_var('func_4873')
func_4874_call = mutated_mod.get_global_var('func_4874')
call_5260 = relay.TupleGetItem(func_4873_call(), 0)
call_5261 = relay.TupleGetItem(func_4874_call(), 0)
output = relay.Tuple([call_5260,])
output2 = relay.Tuple([call_5261,])
func_5273 = relay.Function([], output)
mod['func_5273'] = func_5273
mod = relay.transform.InferType()(mod)
output = func_5273()
func_5274 = relay.Function([], output)
mutated_mod['func_5274'] = func_5274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5245_call = mod.get_global_var('func_5245')
func_5246_call = mutated_mod.get_global_var('func_5246')
call_5299 = func_5245_call()
call_5300 = func_5245_call()
output = call_5299
output2 = call_5300
func_5303 = relay.Function([], output)
mod['func_5303'] = func_5303
mod = relay.transform.InferType()(mod)
mutated_mod['func_5303'] = func_5303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5303_call = mutated_mod.get_global_var('func_5303')
call_5304 = func_5303_call()
output = call_5304
func_5305 = relay.Function([], output)
mutated_mod['func_5305'] = func_5305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4961_call = mod.get_global_var('func_4961')
func_4963_call = mutated_mod.get_global_var('func_4963')
call_5314 = relay.TupleGetItem(func_4961_call(), 0)
call_5315 = relay.TupleGetItem(func_4963_call(), 0)
output = relay.Tuple([call_5314,])
output2 = relay.Tuple([call_5315,])
func_5321 = relay.Function([], output)
mod['func_5321'] = func_5321
mod = relay.transform.InferType()(mod)
output = func_5321()
func_5322 = relay.Function([], output)
mutated_mod['func_5322'] = func_5322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5245_call = mod.get_global_var('func_5245')
func_5246_call = mutated_mod.get_global_var('func_5246')
call_5370 = func_5245_call()
call_5371 = func_5245_call()
func_2380_call = mod.get_global_var('func_2380')
func_2383_call = mutated_mod.get_global_var('func_2383')
const_5382 = relay.const([[4.535789,-1.119832,-6.620801,9.588845,-3.788826,-7.772782,8.044045,-7.001062,0.940264,-7.042238,2.792053,0.129472,-9.091302,8.719228,-0.786612,-6.193863,3.649195,-5.830321,-7.744162,0.015208,6.856730,0.713440,9.920752,-2.394542,9.534614,-0.767637,0.728535,-5.641258,-6.176033,-9.481073,5.157554,-3.271387,4.678731,5.859106,-3.880641,-5.638592,-1.797614,-5.993172,-9.622128,3.183225,-3.421781,-3.246463,8.937529,4.363720,-1.768794,-9.656477,-0.293326,-6.970712,1.163202,-7.859337,-3.922495,6.885309,-8.093413,-9.495300,-1.756766,-9.493393,9.388932,-1.091528,4.838813,-3.147373,2.236055,-8.967422,7.407824,-3.974129,-7.805855,4.542945,1.502415,9.567640,-8.958091,-0.705236,4.710433,4.453773,-6.062074,9.540259,0.430598,1.453011,-6.865795,5.289449,0.807218,-2.511426,-5.027209,-4.758350,-7.539275,7.619580,-5.095728,-0.579702,-2.960491,-8.006685,6.702146,-4.432938,-7.288468,-6.597096,4.802888,-4.330484,5.595550,-4.128720,-1.960238,5.427553,5.872760,-3.653684,9.286664,4.092522,-0.829551,-6.720132],[-1.488444,8.355332,-9.270446,3.493735,2.026437,-4.579760,6.123913,-6.765297,-3.415709,-6.308162,-7.310051,7.988192,2.308071,4.970736,-2.233166,-3.014634,-1.991012,8.239001,9.379966,9.731304,9.313423,8.527772,-8.038342,-2.568335,4.666895,-3.484829,8.424567,1.631257,4.905292,9.770119,-9.360837,-1.613811,2.550535,-3.310367,-7.458955,9.637566,8.220205,-1.904830,-5.235550,-0.455649,-9.339543,1.965684,-8.589973,-9.152472,5.822141,-1.676948,1.526860,-1.359424,-4.161769,2.443104,-0.360987,-4.153207,2.359553,-0.112006,-1.603186,-4.285086,3.399240,-9.842360,-3.056006,4.582811,-2.392884,-9.337645,-3.003714,-6.573477,6.094090,-1.114940,-0.505894,2.773100,4.861195,0.522974,2.328866,-0.613632,7.503101,-5.474347,-6.032968,4.900616,2.859792,-3.292327,6.220320,3.236985,5.244867,-3.632709,-1.303351,8.868207,4.474607,3.846617,-1.139400,-2.145510,4.961583,-3.948805,-9.303911,-0.361369,3.347773,-0.130488,-1.963169,0.711680,8.498703,9.221030,3.871879,5.109081,-7.895783,2.783096,1.705331,-1.285625],[0.281063,-0.961398,3.016194,4.593628,1.695150,6.659794,8.676041,3.065029,-5.363489,1.471787,-0.049405,8.260175,2.099849,2.468690,-3.026923,5.352214,-4.952647,6.975666,6.078803,-4.349607,-7.260580,-8.940222,-7.805507,-9.673039,-5.221367,7.670113,3.373724,0.566677,7.621774,5.312583,7.433296,4.850841,-6.312464,3.476283,-3.392936,-9.319542,9.117799,-3.012837,2.918977,-5.790522,-4.974999,-1.185204,-3.781711,4.524164,-5.902681,4.049343,2.889401,-4.437756,-3.439449,0.528151,5.819729,1.858518,-6.920184,8.352185,4.130681,-1.635965,3.599148,3.503642,-8.207750,2.157337,4.350297,-1.256843,-1.914573,-9.747917,-9.714519,6.828055,6.430124,-8.266433,-1.522614,9.170654,-3.236455,-5.859578,-0.864103,2.077001,-3.531577,-8.381912,-3.025174,-0.878865,1.235423,6.019155,1.480833,1.611379,7.714910,-3.261173,7.940659,2.378415,4.369401,7.689164,6.323653,2.301982,-2.083668,9.100797,-7.420109,3.276078,-2.085662,-4.666578,4.062253,5.858254,9.818768,-6.910114,6.743934,-4.927844,5.602224,9.041696],[2.119955,-4.033531,-8.776111,-8.119790,-9.731615,-5.906644,-4.976341,-8.065265,-3.819310,-9.342995,7.590453,3.218144,7.580516,-2.080103,2.593356,9.878861,-5.774151,-4.918077,-2.876758,4.853542,-4.320286,7.833261,-5.689401,-0.741501,2.237455,9.542329,-2.909375,-4.332396,-0.757201,-3.688375,-3.755221,-3.978349,-4.847392,9.610193,9.786333,8.101577,-6.497198,-8.922929,-0.356049,1.999234,-9.852738,-1.577179,6.595765,-6.039113,4.529777,-2.215377,-9.995373,-2.887337,6.941761,7.291721,7.305812,9.702754,-3.049797,-8.179011,-4.358733,-5.409902,-2.027767,4.070346,3.238217,-5.845374,3.891961,-2.753359,0.253324,-6.302385,-8.533923,-4.429295,-5.641312,6.917632,8.545417,5.911525,-0.564276,-5.530895,-8.674351,-7.636051,5.884332,6.336740,4.427493,6.103911,-9.899820,-3.538682,5.728324,-5.167006,-9.109486,-0.473323,-4.442060,9.538951,-5.416560,4.053569,-7.193527,-9.767179,-6.667366,-4.798451,-7.971715,7.467238,1.633929,5.691594,-5.473588,-2.787021,-7.847812,-3.228178,-0.111474,0.524182,-2.630110,5.683760],[-6.374737,-3.108197,6.496619,8.748469,-1.653556,8.933328,-6.858377,1.730179,-0.775200,6.301162,-4.476457,4.810546,2.154065,5.998290,-2.425638,-7.223520,6.951585,3.159681,8.740299,-0.149527,4.194308,3.295672,-8.885695,-0.726296,-9.330021,9.463022,-3.294325,9.308237,6.283943,8.821953,-0.601004,8.591538,-0.872088,-9.475650,7.253612,-3.770137,-8.069064,-8.740802,-3.968293,-6.854807,-8.106541,7.510888,-4.262397,-8.965789,-6.821124,0.216195,-2.478388,-2.716158,-2.567237,-2.265900,6.487715,-9.339737,5.126556,-5.492688,-6.180131,-2.596504,5.106783,4.445488,9.007238,4.533871,4.730111,-2.582420,7.580114,-5.933988,2.803815,8.642259,1.414702,7.243462,-9.439234,-8.566863,-1.082199,0.628252,0.274351,3.882125,4.613846,-8.929096,-8.529232,-8.853711,5.974557,3.882778,8.587984,4.542045,-6.052539,4.255596,-2.083762,4.286820,6.268222,-7.336626,8.853286,8.999295,2.952747,7.136048,-0.812451,9.258178,6.023394,-0.811575,-4.758292,1.800219,-2.724775,8.211326,9.215842,9.339089,-2.474604,0.585094],[-8.002515,-9.461551,-6.160844,8.524136,7.521803,-0.109000,8.744381,3.982856,-4.121004,-0.499335,-6.849745,7.567467,1.897426,-2.777333,7.862202,5.185107,-1.007152,2.151682,-0.917210,9.975143,6.946525,-9.886124,-4.173410,-5.422173,-7.204282,-7.588840,4.071510,-2.257532,-7.431605,-8.632002,-0.299126,6.952033,3.485512,9.000423,3.300661,6.271227,-7.997323,3.058859,5.708800,8.147750,1.470987,-3.380686,-4.311482,9.807284,7.350119,-6.478596,4.171320,-0.376824,-1.344392,-0.269656,-7.072643,-1.337014,1.980141,-5.182196,-3.098577,9.230900,8.538041,-2.789550,-5.894589,-3.068561,7.820931,-2.615368,7.953043,6.431328,-3.790150,4.375318,8.270603,-1.088344,-3.412619,7.605625,-1.172225,-9.619881,7.900911,9.254773,-7.362678,7.981139,-4.501783,-3.029339,1.636016,1.467650,-3.995714,-9.922509,5.247632,-1.785635,5.756257,-3.731200,-4.856670,3.152316,1.763939,-8.849096,3.998112,9.710289,5.142051,7.875257,9.747949,-1.519234,8.482186,7.146777,8.555308,-0.984804,5.019793,8.147863,7.090935,5.198085],[3.515731,-1.983848,-1.937968,9.157837,-1.509713,-1.870950,8.668260,7.135687,1.360613,2.962035,-7.750097,-3.222393,-2.155459,-7.763643,-8.960470,-6.200104,6.229005,-7.724756,-6.651693,9.575794,-3.507054,-6.146749,-6.957066,1.518453,-1.716699,8.220157,-7.772849,4.851059,3.762288,7.024665,5.287472,9.930057,-7.585324,-6.964545,1.615512,4.907404,0.846587,-0.557093,8.110140,-1.120138,-5.187261,0.828964,6.455266,-4.061629,-4.263785,-4.085313,4.227179,-6.367494,-7.193614,8.194322,-8.490789,6.545529,-6.102441,9.679475,6.305735,-6.339580,1.979034,4.156076,-9.020165,8.376410,5.803109,-9.463579,-2.316326,-2.403928,-0.327360,-8.738321,5.426958,-5.223657,3.206804,5.540529,4.469787,4.223501,6.229406,7.484626,-4.026087,-9.607132,1.964380,-9.716036,6.051940,-2.972885,-1.308397,-6.894847,-6.746085,-0.468200,6.358514,2.108259,2.769581,7.207484,4.283483,-6.375243,-9.381950,6.262549,4.626202,0.861986,-5.090780,-9.113124,-8.721732,-0.040412,-9.347139,4.800565,6.619493,-2.144000,3.129825,7.333818]], dtype = "float64")#candidate|5382|(7, 104)|const|float64
const_5383 = relay.const([7,7,10,9,10,-7,9,-7,3,2,-3,-8,-6,-3,7,3,5,-3,7,-3,3,-1,6,-1,4,-10,-6,7,1,2,-2,-5,-4,4,-2,8,8,6,-7,-5,-2,7,3,-9,-4,6,5,2,2,1,-4,-7,-10,6,-2,6,6,-4,-7,-7,4,-6,-7,-8,-6,-2,10,3,-4,7,10,2,9,6,8,7,-9,1,-1,4,10,10,-7,1,-1,-9,-2,-6,-10,-6,-8,-10,-6,-2,2,6,3,-3,6,4,-2,8,-8,6,-1,-4,-5,-5,-7,-10,2,-10,-10,5,-7,-5,4,3,-2,-9,1,-1,10,-9,-2,8,5,-8,1,2,4,6,-5,-1,-10,-9,6,9,-5,-4,9,10,10,-8,-3,10,10,-7,-9,-1,9,-9,-7,10,9,8,4,2,5,-6,10,6,-3,6,-1,10,6,-4,10,-6,8,6,3,-9,-8,7,-10,-2,3,-7,-7,-4,-6,8,4,2,-2,-7,8,1,10,6,8,5,5,8,6,-7,-4,-6,-10,4,1,-5,7,5,-6,7,10,-7,-3,9,1,-2,10,3,10,-4,-9,10,-6,5,-7,-6,-4], dtype = "int8")#candidate|5383|(225,)|const|int8
call_5381 = relay.TupleGetItem(func_2380_call(relay.reshape(const_5382.astype('float64'), [13, 8, 7]), relay.reshape(const_5383.astype('int8'), [225,]), ), 1)
call_5384 = relay.TupleGetItem(func_2383_call(relay.reshape(const_5382.astype('float64'), [13, 8, 7]), relay.reshape(const_5383.astype('int8'), [225,]), ), 1)
func_5321_call = mod.get_global_var('func_5321')
func_5322_call = mutated_mod.get_global_var('func_5322')
call_5395 = relay.TupleGetItem(func_5321_call(), 0)
call_5396 = relay.TupleGetItem(func_5322_call(), 0)
output = relay.Tuple([call_5370,call_5381,const_5382,const_5383,call_5395,])
output2 = relay.Tuple([call_5371,call_5384,const_5382,const_5383,call_5396,])
func_5398 = relay.Function([], output)
mod['func_5398'] = func_5398
mod = relay.transform.InferType()(mod)
mutated_mod['func_5398'] = func_5398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5398_call = mutated_mod.get_global_var('func_5398')
call_5399 = func_5398_call()
output = call_5399
func_5400 = relay.Function([], output)
mutated_mod['func_5400'] = func_5400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5245_call = mod.get_global_var('func_5245')
func_5246_call = mutated_mod.get_global_var('func_5246')
call_5519 = func_5245_call()
call_5520 = func_5245_call()
output = relay.Tuple([call_5519,])
output2 = relay.Tuple([call_5520,])
func_5524 = relay.Function([], output)
mod['func_5524'] = func_5524
mod = relay.transform.InferType()(mod)
mutated_mod['func_5524'] = func_5524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5524_call = mutated_mod.get_global_var('func_5524')
call_5525 = func_5524_call()
output = call_5525
func_5526 = relay.Function([], output)
mutated_mod['func_5526'] = func_5526
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5547 = relay.var("var_5547", dtype = "float64", shape = (1, 1, 13))#candidate|5547|(1, 1, 13)|var|float64
uop_5548 = relay.asin(var_5547.astype('float64')) # shape=(1, 1, 13)
bop_5550 = relay.right_shift(var_5547.astype('int8'), relay.reshape(uop_5548.astype('int8'), relay.shape_of(var_5547))) # shape=(1, 1, 13)
bop_5557 = relay.not_equal(uop_5548.astype('bool'), relay.reshape(bop_5550.astype('bool'), relay.shape_of(uop_5548))) # shape=(1, 1, 13)
func_4535_call = mod.get_global_var('func_4535')
func_4539_call = mutated_mod.get_global_var('func_4539')
var_5563 = relay.var("var_5563", dtype = "float64", shape = (728,))#candidate|5563|(728,)|var|float64
var_5564 = relay.var("var_5564", dtype = "bool", shape = (882,))#candidate|5564|(882,)|var|bool
call_5562 = relay.TupleGetItem(func_4535_call(relay.reshape(var_5563.astype('float64'), [728,]), relay.reshape(var_5564.astype('bool'), [882,]), ), 1)
call_5565 = relay.TupleGetItem(func_4539_call(relay.reshape(var_5563.astype('float64'), [728,]), relay.reshape(var_5564.astype('bool'), [882,]), ), 1)
output = relay.Tuple([bop_5557,call_5562,var_5563,var_5564,])
output2 = relay.Tuple([bop_5557,call_5565,var_5563,var_5564,])
func_5566 = relay.Function([var_5547,var_5563,var_5564,], output)
mod['func_5566'] = func_5566
mod = relay.transform.InferType()(mod)
mutated_mod['func_5566'] = func_5566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5566_call = mutated_mod.get_global_var('func_5566')
var_5568 = relay.var("var_5568", dtype = "float64", shape = (1, 1, 13))#candidate|5568|(1, 1, 13)|var|float64
var_5569 = relay.var("var_5569", dtype = "float64", shape = (728,))#candidate|5569|(728,)|var|float64
var_5570 = relay.var("var_5570", dtype = "bool", shape = (882,))#candidate|5570|(882,)|var|bool
call_5567 = func_5566_call(var_5568,var_5569,var_5570,)
output = call_5567
func_5571 = relay.Function([var_5568,var_5569,var_5570,], output)
mutated_mod['func_5571'] = func_5571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4873_call = mod.get_global_var('func_4873')
func_4874_call = mutated_mod.get_global_var('func_4874')
call_5615 = relay.TupleGetItem(func_4873_call(), 0)
call_5616 = relay.TupleGetItem(func_4874_call(), 0)
func_5524_call = mod.get_global_var('func_5524')
func_5526_call = mutated_mod.get_global_var('func_5526')
call_5617 = relay.TupleGetItem(func_5524_call(), 0)
call_5618 = relay.TupleGetItem(func_5526_call(), 0)
func_2596_call = mod.get_global_var('func_2596')
func_2600_call = mutated_mod.get_global_var('func_2600')
var_5636 = relay.var("var_5636", dtype = "float64", shape = (672,))#candidate|5636|(672,)|var|float64
call_5635 = func_2596_call(relay.reshape(var_5636.astype('float64'), [7, 12, 8]), relay.reshape(var_5636.astype('float64'), [7, 12, 8]), )
call_5637 = func_2596_call(relay.reshape(var_5636.astype('float64'), [7, 12, 8]), relay.reshape(var_5636.astype('float64'), [7, 12, 8]), )
func_5273_call = mod.get_global_var('func_5273')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_5644 = relay.TupleGetItem(func_5273_call(), 0)
call_5645 = relay.TupleGetItem(func_5274_call(), 0)
output = relay.Tuple([call_5615,call_5617,call_5635,var_5636,call_5644,])
output2 = relay.Tuple([call_5616,call_5618,call_5637,var_5636,call_5645,])
func_5676 = relay.Function([var_5636,], output)
mod['func_5676'] = func_5676
mod = relay.transform.InferType()(mod)
mutated_mod['func_5676'] = func_5676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5677 = relay.var("var_5677", dtype = "float64", shape = (672,))#candidate|5677|(672,)|var|float64
func_5676_call = mutated_mod.get_global_var('func_5676')
call_5678 = func_5676_call(var_5677)
output = call_5678
func_5679 = relay.Function([var_5677], output)
mutated_mod['func_5679'] = func_5679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4873_call = mod.get_global_var('func_4873')
func_4874_call = mutated_mod.get_global_var('func_4874')
call_5686 = relay.TupleGetItem(func_4873_call(), 0)
call_5687 = relay.TupleGetItem(func_4874_call(), 0)
output = relay.Tuple([call_5686,])
output2 = relay.Tuple([call_5687,])
func_5711 = relay.Function([], output)
mod['func_5711'] = func_5711
mod = relay.transform.InferType()(mod)
mutated_mod['func_5711'] = func_5711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5711_call = mutated_mod.get_global_var('func_5711')
call_5712 = func_5711_call()
output = call_5712
func_5713 = relay.Function([], output)
mutated_mod['func_5713'] = func_5713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_5819 = func_4727_call()
call_5820 = func_4727_call()
output = call_5819
output2 = call_5820
func_5847 = relay.Function([], output)
mod['func_5847'] = func_5847
mod = relay.transform.InferType()(mod)
output = func_5847()
func_5848 = relay.Function([], output)
mutated_mod['func_5848'] = func_5848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5524_call = mod.get_global_var('func_5524')
func_5526_call = mutated_mod.get_global_var('func_5526')
call_5854 = relay.TupleGetItem(func_5524_call(), 0)
call_5855 = relay.TupleGetItem(func_5526_call(), 0)
output = relay.Tuple([call_5854,])
output2 = relay.Tuple([call_5855,])
func_5861 = relay.Function([], output)
mod['func_5861'] = func_5861
mod = relay.transform.InferType()(mod)
output = func_5861()
func_5862 = relay.Function([], output)
mutated_mod['func_5862'] = func_5862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_5973 = relay.TupleGetItem(func_5054_call(), 0)
call_5974 = relay.TupleGetItem(func_5055_call(), 0)
var_6002 = relay.var("var_6002", dtype = "float64", shape = (14, 7, 9))#candidate|6002|(14, 7, 9)|var|float64
bop_6003 = relay.right_shift(call_5973.astype('uint32'), relay.reshape(var_6002.astype('uint32'), relay.shape_of(call_5973))) # shape=(14, 7, 9)
bop_6006 = relay.right_shift(call_5974.astype('uint32'), relay.reshape(var_6002.astype('uint32'), relay.shape_of(call_5974))) # shape=(14, 7, 9)
uop_6018 = relay.sqrt(bop_6003.astype('float32')) # shape=(14, 7, 9)
uop_6020 = relay.sqrt(bop_6006.astype('float32')) # shape=(14, 7, 9)
func_1460_call = mod.get_global_var('func_1460')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_6022 = relay.TupleGetItem(func_1460_call(relay.reshape(call_5973.astype('bool'), [882,])), 1)
call_6023 = relay.TupleGetItem(func_1463_call(relay.reshape(call_5973.astype('bool'), [882,])), 1)
output = relay.Tuple([uop_6018,call_6022,])
output2 = relay.Tuple([uop_6020,call_6023,])
func_6038 = relay.Function([var_6002,], output)
mod['func_6038'] = func_6038
mod = relay.transform.InferType()(mod)
mutated_mod['func_6038'] = func_6038
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6039 = relay.var("var_6039", dtype = "float64", shape = (14, 7, 9))#candidate|6039|(14, 7, 9)|var|float64
func_6038_call = mutated_mod.get_global_var('func_6038')
call_6040 = func_6038_call(var_6039)
output = call_6040
func_6041 = relay.Function([var_6039], output)
mutated_mod['func_6041'] = func_6041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_6091 = func_5303_call()
call_6092 = func_5303_call()
var_6115 = relay.var("var_6115", dtype = "float32", shape = (11, 12, 4))#candidate|6115|(11, 12, 4)|var|float32
bop_6116 = relay.greater(call_6091.astype('bool'), relay.reshape(var_6115.astype('bool'), relay.shape_of(call_6091))) # shape=(11, 12, 4)
bop_6119 = relay.greater(call_6092.astype('bool'), relay.reshape(var_6115.astype('bool'), relay.shape_of(call_6092))) # shape=(11, 12, 4)
output = relay.Tuple([bop_6116,])
output2 = relay.Tuple([bop_6119,])
func_6123 = relay.Function([var_6115,], output)
mod['func_6123'] = func_6123
mod = relay.transform.InferType()(mod)
mutated_mod['func_6123'] = func_6123
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6124 = relay.var("var_6124", dtype = "float32", shape = (11, 12, 4))#candidate|6124|(11, 12, 4)|var|float32
func_6123_call = mutated_mod.get_global_var('func_6123')
call_6125 = func_6123_call(var_6124)
output = call_6125
func_6126 = relay.Function([var_6124], output)
mutated_mod['func_6126'] = func_6126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_6128 = func_4727_call()
call_6129 = func_4727_call()
func_5847_call = mod.get_global_var('func_5847')
func_5848_call = mutated_mod.get_global_var('func_5848')
call_6133 = func_5847_call()
call_6134 = func_5847_call()
func_6123_call = mod.get_global_var('func_6123')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_6135 = relay.TupleGetItem(func_6123_call(relay.reshape(call_6128.astype('float32'), [11, 12, 4])), 0)
call_6136 = relay.TupleGetItem(func_6126_call(relay.reshape(call_6128.astype('float32'), [11, 12, 4])), 0)
func_5711_call = mod.get_global_var('func_5711')
func_5713_call = mutated_mod.get_global_var('func_5713')
call_6141 = relay.TupleGetItem(func_5711_call(), 0)
call_6142 = relay.TupleGetItem(func_5713_call(), 0)
output = relay.Tuple([call_6128,call_6133,call_6135,call_6141,])
output2 = relay.Tuple([call_6129,call_6134,call_6136,call_6142,])
func_6158 = relay.Function([], output)
mod['func_6158'] = func_6158
mod = relay.transform.InferType()(mod)
output = func_6158()
func_6159 = relay.Function([], output)
mutated_mod['func_6159'] = func_6159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5273_call = mod.get_global_var('func_5273')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_6182 = relay.TupleGetItem(func_5273_call(), 0)
call_6183 = relay.TupleGetItem(func_5274_call(), 0)
var_6184 = relay.var("var_6184", dtype = "bool", shape = (14, 7, 9))#candidate|6184|(14, 7, 9)|var|bool
bop_6185 = relay.subtract(call_6182.astype('uint16'), relay.reshape(var_6184.astype('uint16'), relay.shape_of(call_6182))) # shape=(14, 7, 9)
bop_6188 = relay.subtract(call_6183.astype('uint16'), relay.reshape(var_6184.astype('uint16'), relay.shape_of(call_6183))) # shape=(14, 7, 9)
func_3994_call = mod.get_global_var('func_3994')
func_3999_call = mutated_mod.get_global_var('func_3999')
const_6190 = relay.const([[-3,-6,7,-4,4,5,-3,-4,10,1,-4,-3,-6,1,-4,-2,7,9,-9,-2,5,6,6,1,6,4],[-6,8,9,5,-2,10,4,5,2,-6,-9,-7,10,9,-9,-9,1,8,-9,-5,9,-10,7,-8,-7,8],[-7,-8,-2,-7,1,9,-1,2,-9,1,-4,-2,-10,-10,5,10,-4,10,-9,-10,-3,2,3,6,-3,-1],[-9,8,3,4,-7,-1,5,8,10,-4,-4,-7,-4,-10,-9,6,3,-7,1,6,6,-10,3,-6,-5,-6],[-9,-9,-5,10,1,3,-9,10,-10,9,-6,-10,8,-1,-4,-5,9,8,4,-1,-3,8,-3,-3,5,-10],[2,9,3,4,-7,4,4,4,-7,2,7,3,8,-2,9,-5,3,-2,6,-6,6,2,10,-7,-1,1],[9,-8,2,-2,-6,-4,5,-3,-2,5,-9,-8,-3,7,4,-3,-2,1,-5,-6,4,-7,-6,9,1,5],[-10,-2,8,8,7,-6,-2,-6,-2,7,-2,2,-7,5,-4,10,3,-7,-1,-4,6,-1,9,-7,-10,4],[9,8,-8,3,-3,-5,5,9,7,-8,5,3,-5,-2,5,6,3,-7,7,2,3,8,9,5,3,1],[3,10,4,-2,10,-2,-2,-6,1,10,-5,-1,6,-2,-1,6,7,-9,-10,4,1,-4,7,3,-10,-9],[1,-9,7,-5,4,-2,7,-6,4,-6,-5,9,2,9,5,5,9,-1,7,7,-7,-6,10,-9,3,-1],[-8,10,2,-10,-7,-3,10,5,1,-1,-10,-3,1,5,9,-2,-6,-5,-2,-5,9,-5,3,-6,-1,3],[6,-2,-7,-10,-2,-1,5,-7,10,-7,-2,-8,4,7,3,-7,-5,-7,-7,-9,1,9,6,4,8,5],[-4,4,8,-3,1,-1,2,-9,9,8,-9,-8,3,-3,5,-2,2,7,7,-1,4,7,2,-3,-5,10],[9,1,2,-4,1,-6,-2,-2,-4,9,5,-2,-1,7,-9,10,-5,-2,4,-3,-2,9,-3,4,4,-5],[-9,-7,3,8,10,-2,10,3,-9,-10,-7,-6,-10,8,-4,-6,-10,-5,6,7,-1,3,4,-5,4,4],[4,10,10,1,-10,9,9,-5,7,-3,2,10,-3,8,10,-7,-4,10,6,10,-8,6,-2,4,-4,10],[4,1,-6,-3,3,-3,-10,2,6,-1,-2,-4,7,-6,5,-6,-7,-4,-10,-1,10,1,-1,-3,-5,-1],[-3,-3,-3,3,4,-6,-8,4,-1,2,-3,9,-8,-10,9,1,-8,-6,1,8,-9,-8,9,9,-9,9],[-4,5,-3,6,-8,-5,9,-7,1,8,2,-10,-8,-8,10,10,-8,-7,-1,2,-7,-6,-10,-1,-8,2],[-4,10,-9,-10,8,2,-6,6,1,-9,-6,-7,7,9,8,5,2,-6,4,2,8,5,-5,3,10,4],[-6,4,10,9,3,-10,9,-7,-3,-2,-3,7,9,-3,4,7,-2,-3,2,-10,6,-9,-9,-8,5,5],[9,5,-4,9,8,7,-4,-2,-4,1,-6,7,-7,10,-4,-10,-9,-5,7,-2,-9,-7,-1,3,-5,7],[5,7,-8,-3,-1,7,2,-2,5,6,-5,1,1,-3,-8,-8,-6,-6,1,7,6,4,8,-7,-2,-1]], dtype = "uint64")#candidate|6190|(24, 26)|const|uint64
const_6191 = relay.const([-1.676514,9.781796,7.584729,1.574734,-8.140857,6.733730,-9.878154,0.538011,-1.035512,9.065388,-4.309903,-4.160646,-9.287796,-0.808363,-8.642580,-4.098326,8.934721,2.740866,1.228508,-2.542275,-8.716910,-0.726463,-6.987691,-3.774341,5.207778,5.226276,8.450410,9.980765,-8.749835,7.600932,9.361739,-6.222939,8.435142,-7.791293,-9.688493,4.742436,-7.452668,7.351124,0.873902,1.813107,0.651075,9.444812,-8.138045,2.856289,-2.238551,6.933737,-9.058524,-4.747206,-0.591962,-7.669758,4.761604,8.111373,5.862647,5.745506,-8.290805,-7.653586,2.912413,-6.089772,-1.358213,4.215301,-9.173215,0.693664,-4.992299,-8.485263,-1.074131,0.135116,-7.563640,9.661094,1.338582,6.311268,7.078844,9.720295,4.197658,0.449526,5.740233,-1.427913,9.211839,6.268004,-9.670466,-4.341929,-6.228563,-9.953251,-8.059183,1.887490,-3.349531,4.729702,-0.866692,2.232817,-1.575701,6.890991,3.706290,0.821793,2.659005,-5.222901,5.532188,-5.527703,-5.639086,-2.054937,-4.861639,-4.547429,-0.509137,6.251979,-6.422789,-9.030535,0.879957,4.054512,-5.054388,7.689601,0.061361,2.058425,7.182061,-4.009367,-3.754973,-3.929825,-6.759831,-2.886891,1.017231,3.453410,-6.768806,-2.541595,-9.523393,-6.182494,9.725281,-0.042774,3.617345,2.117566,-0.129774,-7.472952,-0.153699,6.965645,2.179643,-7.837095,0.153195,-5.127707,7.558628,4.941738,-3.896939,-3.808005,-7.586736,-4.611803,-3.320228,-2.070527,-4.961996,-5.489804,5.825583,5.888451,4.171999,2.092983,-3.370231,-7.894798,9.280335,6.064465,4.928418,8.365443,-2.868731,0.140468,2.716196,3.167036,-4.394020,-4.223825,-6.537806,-3.413927,3.016107,-3.744491,1.179420,-1.304462,0.671519,4.218451,0.848530,-2.374271,-1.977716,8.675427,7.204940,4.864400,-7.590532,7.629525,-1.290200,-7.812835,-4.214258,0.740855,4.421697,-2.915343,3.949828,8.080195,-0.619928,-5.679470,6.361842,-5.973149,9.466765,-3.414984,5.756119,-1.831270,5.703834,-8.804314,0.498826,5.105636,6.736512,4.565366,5.165113,9.913364,-0.625394,6.981786,7.033215,-6.873454,0.135503,-5.302857,8.349042,-3.150564,9.861093,-1.004900,-7.631896,7.084171,0.852300,-7.237188,3.250889,-3.052033,-0.995401,2.181700,6.231920,-7.238669,-2.309605,7.688771,5.577802,-9.758099,-3.857283,9.497000,9.233799,-0.692117,-9.406436,4.878782,5.148753,1.407087,7.398578,9.696850,5.513428,-5.138051,1.144423,8.047965,0.511308,4.224911,-8.463091,0.300562,-3.801725,-3.909324,-9.167403,-2.635724,8.874467,2.855746,2.880467,5.282792,-2.773582,-6.293960,5.832824,-9.096474,-7.824588,6.223697,9.705821,-2.666039,-5.297470,-4.770668,-2.726376,-9.706383,-9.998108,4.553520,1.039263,-8.345999,-2.166310,9.743573,-3.560349,-4.043501,5.026076,8.444289,-9.072500,-3.448889,-1.987632,-7.692939,-6.380738,-6.497566,-0.789312,-5.893459,-2.833319,-2.044678,4.498247,3.015212,1.489169,-1.776750,3.521765,8.535883,2.514012,-0.821174,-8.079932,0.254755,-3.026462,-9.196685,2.082646,-3.100109,1.646742,-2.874755,-1.642122,5.287720,9.301872,-4.577726,2.177951,5.125215,-6.425488,8.072003,-6.077294,0.131419,-4.578385,9.827774,-3.840104,-7.671066,-7.666713,-6.640170,-1.020491,3.275610,-3.776426,-8.556132,2.121338,-4.892262,5.458832,6.047882,-0.369035,-0.944931,-2.585484,-2.146201,2.715082,-4.202252,0.100442,-8.541210,-5.011406,-2.970622,-9.153877,2.899305,-9.509678,6.899576,8.804690,1.457454,0.043513,-2.605449,4.958095,-0.800857,2.008294,3.051190,1.520593,-8.835550,2.457958,-4.502865,2.381147,4.778704,-1.246921,-0.521563,4.625463,6.565884,1.526936,-2.704318,3.656969,-8.880929,-4.846067,7.592997,7.887799,4.918065,-7.865260,-1.154649,1.582740,2.034607,-6.602871,2.825876,3.377853,-8.743059,3.908075,-2.453579,8.106555,1.253514,-6.513446,-6.869748,4.577170,-6.240800,4.191518,1.919518,-0.542435,-9.769351,-7.977549,4.290363,3.093138,1.485795,-0.093091,5.541270,-2.615017,4.982537,3.862500,-5.441169,-9.022505,8.989750,-7.067759,-6.556583,6.220276,5.633368,8.881810,-2.936992,9.860293,5.844501,9.991147,3.930261,9.846957,-5.503557,-7.073017,2.101640,8.507800,2.767750,-2.225349,-1.728579,-5.637868,4.338550,-7.761270,-8.428146,6.458906,-8.371458,-8.361911,-7.905360,-3.233685,0.241734,-0.439832,9.478947,1.753933,3.673693,7.536894,2.220913,3.188663,0.801987,-1.501285,8.065752,1.312236,-8.279606,-2.029473,1.758538,0.323853,1.253013,-7.689058,6.893690,7.275278,3.273758,0.633797,1.465041,9.039328,-8.499436,-3.977544,-9.642110,7.719659,-1.705951,1.701145,7.126375,-4.212839,-6.389908,8.799162,-9.212884,-9.827295,5.880288,-8.016899,3.649879,8.628665,-8.485778,4.587586,7.837649,5.912086,-5.960666,-1.451364,-8.288245,2.402211,0.555350,-9.949799,9.719754,4.206698,-0.612244,8.281160,5.254059,-4.833703,6.444280,-8.595541,-3.833831,-0.935012,2.523455,-7.258448,7.865167,-8.276003,8.024618,-9.899049,-6.598252,4.774300,2.008333,-5.126605,-2.473804,-3.395496,-4.378990,-1.740041,8.273395,-0.884775,6.632681,-3.537573,-2.934639,3.864562,0.119274,-4.948589,0.334674,5.505608,6.112572,-3.338493,-4.243569,0.263171,3.464773,6.934170,-7.954676,3.483828,5.314701,-8.342160,5.763814,7.945583,4.756121,-0.646844,3.207400,3.171133,9.831635,-8.403101,9.744209,-5.216641,-0.300899,5.274358,9.626013,-1.008273,-6.216590,-1.660125,1.698498,-7.111338,-3.505769,0.570376,-1.917737,-7.230207,-5.716939,7.480892,-1.273259,7.691562,-9.964558,3.887693,9.409564,-8.790952,-0.120438,9.169280,-6.009233,-7.640901,-4.209835,-1.235423,-0.332185,-9.729999,-9.868775,-5.252625,-4.786231,7.158522,-6.832882,-3.679056,-8.660995,9.923464,-8.723450,-3.402404,8.613875,4.850261,7.362009,-0.167216,-7.042979,-9.139571,9.378395,9.851147,-3.394365,-5.881019,4.739719,7.051177,2.741857,-3.528620,5.785623,-0.536353,3.686456,5.352816,1.034446,-0.143698,-5.987316,-5.260400,-5.748312,8.768963,-9.687258,4.631406,1.708812,-2.022845,-0.034899,-9.452079,0.104610,-5.913085,-8.119400,3.753658,1.883985,5.209084,0.678402,8.239728,5.702977,-7.693083,-0.126968,2.616169,-4.017290,-8.196216,-1.383651,3.368826,2.168667,-0.965990,6.010920,-4.663654,2.937707,-2.302130,3.111095,-4.543073,9.662453,0.781973,0.307919,6.890888,-4.884032,-5.089659,-0.122185,-4.442589,4.845704,9.818377,1.300412,1.705628,6.675615,8.991434,-4.316433,1.875245,-5.325050,0.855306,0.648673,-1.188070,9.257218,-8.081477,-2.086682,3.700726,7.147657,-9.070443,-1.593465,4.946399,5.113138,3.185673,7.961425,9.636891,4.433317,7.523086,8.513999,-4.229888,-9.995341,-5.974494,7.687469,-0.223432,-9.174673,0.806768,-7.165189,-2.056460,9.354796,0.544576,-2.009777,4.778395,-2.834111,-0.269782,-8.825545,-4.662331,5.535683,6.604878,-6.056758,0.228952,-7.426189,-6.099832,-6.430409,-1.490524,-1.277399,-2.091909,1.082367,-2.106944,-9.067107,6.441217,6.234895,5.743119,9.816176,7.618720,-9.977369,-7.124952,-8.145552,8.783177,-6.689060,-2.368048,-5.704950,6.797664,-7.845597,8.877851,3.755179,5.635089,-1.324197,0.563964,0.666503,8.461240,-2.414000,-5.850540,-1.995753,3.465110,-5.050986,3.172197,-3.307410,-9.722510,-5.838732,5.370705,-0.454487,-6.820230,3.329494,-2.914724,8.997947,-1.091529,-1.383950,-8.064868,-3.672838,9.521813,6.825129,4.388202,4.632070,9.015849,9.980167,9.288137,2.980629,-7.235961,-6.932396,-3.816366,5.356248,4.712406,6.164054,-4.378540,1.909944,-2.988593,5.180884,-5.081700,2.797648,-1.501471,-7.181620,8.478239,-3.549988,-3.887411,-2.908113,-3.509472,6.301493,2.914838,6.370092,-9.894864,4.407365,4.727274,4.942336,-1.551530,2.147385,9.122424,-2.913183,-2.564182,8.947499,5.631768,4.809451,8.844487,7.362656,6.612586,-9.612066,8.301116,8.167312,-4.823168,-5.118602,7.721757,-5.822902,9.170766,3.296613,9.913629,-4.111437,3.243304,-0.634898,-6.401435,3.508980,-2.283842,-2.478784,-5.781019,-6.272496,-4.371527,4.946739,0.705527,-2.503804,-6.255991,-9.555278,-8.860928,9.519137,-4.318947,-2.251045,9.510080,-2.489610,-7.366847,-0.695603,-5.006085,8.264443,8.155637,1.057147,-9.351531,-5.044822,5.693508,-6.376639,3.333055,4.371058,5.094662,2.077815,-9.171951,-1.324223,-9.190217,1.155750,-1.474086,6.264774,5.998386,-6.311913,-7.188900,-6.297571,7.689608,-1.238020,-2.371975,-5.369981,5.715596,0.179574,4.269022,-7.267199,-8.321913,5.933620,4.454671,-2.502553,0.050362,-7.495770,6.180593,3.400800,-4.133362,-4.871718,-3.804674,-6.270044,-2.627135,4.545315,-3.556796,9.540674,0.889460,1.427306,8.331471,4.721925,-0.766426,-5.264529,-8.957005,-3.812356,7.859281,-3.651809,4.205616,-5.564108,-3.870993,3.156405,2.983553,3.078454,7.971828,0.760742,-1.312725,1.770676,3.304095,0.843310,-9.595840,-8.866820,-8.359227,8.021786,4.211478,2.073684,8.823678,-3.787555,9.723920,0.360284,-8.576563,4.076282,6.805682,5.214613,-6.551155,-1.794568,-7.633086,0.985860,1.886189,-3.411563,-0.771200,-5.768305,6.496016,-5.798224,-4.550316,1.452668,3.510284,-6.496013,-1.407166,2.273479,-8.840836,1.027090,-0.562576,1.287319,9.296199,-8.168321,0.508291,5.432972,-3.845277,0.708285,6.798927,0.381865,6.386307,6.160633,-7.332741,-3.203569,-7.863786,2.599621,-4.386473,7.469750,5.236611,6.605190,-9.823567,9.497010,4.001517,-6.227768,6.604944,9.357962,3.355650,-4.093257,3.540710,-0.409673,-0.718326,-8.258203,-8.418073,-0.608547,6.033150,-0.479658,-8.244621,-6.254908,-6.689836,-3.933373,9.458934,-5.582102,-7.898968,-3.471129,7.290668,-7.164176,-2.072059,9.514364,-8.151573,-7.479957,1.102408,2.483671,-3.778851,4.281208,-0.377045,0.644889,3.976034,-4.569238,-3.661208,2.564618,6.153743,-7.164897,-4.018704,-1.725539,0.809071,2.999140,8.397846,8.915898,-5.428624,-7.019611,-3.559544,-8.344415,7.965323,-6.398653,5.594120,-8.061716,2.232967,9.203896,-0.005370,-7.712065,-4.181329,-6.557134,-3.585120,-8.939735,1.662684,-7.905703,-2.755431,4.990218,4.153786,0.148364,-9.726377,-9.664949,-6.060446,6.017348,6.286718,6.189899,1.914530,-1.970791,2.923363,2.777708,5.077517,-5.432782,-4.766341,-2.971821,0.207261,9.311715,7.012600,0.109693,2.595200,-2.672757,-3.744304,-5.427402,5.933410,-0.037828,4.670199,8.133937,9.215225,-7.456392,-0.888664,6.152832,7.236546,5.392769,-6.733281,-6.124594,3.805383,8.382199,-3.179440,-2.632366,-2.872751,-4.524839,-5.473542,-3.373614,-6.813756,4.037845,1.774566,-6.050790,9.865299,1.647091,1.096981,2.284131,-7.698149,-4.158771,2.594512,4.676813,2.815454,2.061907,4.419193,7.710684,6.599734,-9.439762,-6.990217,4.032777,-4.341569,5.585840,-8.243271,1.398622,9.392229,-0.169882,-2.132827,-4.282103,7.936859,1.294349,-6.120385,-1.355472,3.134437,-5.257164,-8.641223,-4.115653,0.711450,-8.126195,-4.063377,-4.241067,0.178627,-0.823073,-3.512025,-3.057410,7.908129,4.542842,-3.068545,7.533737,-2.670843,7.664812,8.408050,-2.758295,-0.156866,-9.508206,-8.744201,-3.031012,4.837372,5.497063,-9.470874,-3.113943,8.569654,6.106782,0.239448,2.395276,-5.329353,-7.077092,-3.562688,-1.758832,0.959327,-4.632583,-8.071384,-2.560228,7.475373,3.192164,8.441490,2.538041,6.406759,-5.753904,5.707292,5.313706,9.122605,3.292582,-3.589071,-0.428379,4.603488,4.372020,0.162302,0.239713,5.839741,-9.704123,-7.390951,8.346467,-9.315004,5.650597,1.516227,-6.658037,-4.201090,2.443300,5.065430,2.614283,-4.416193,-5.650965,-3.706331,-4.114285,4.050355,-0.918457,3.466329,4.483367,8.329774,5.073518,2.343659,3.215264,-3.570550,-3.850172,-9.557414,-0.312438,-4.205763,3.155966,-7.855674,-3.371632,-0.784708,-7.854496,-6.566609,-7.668872,-4.394792,9.775343,8.536726,4.934683,2.172633,0.395316,0.094927,-4.068285,9.682785,-1.770688,6.814144,0.102723,1.583849,3.140671,9.580762,-6.492243,-2.518568,-5.166695,-2.172928,6.187309,0.853648,-7.454455,-6.823584,8.322212,-1.359213,2.074692,-7.405990,8.305690,-7.765886,-0.586848,-9.463044,3.537753,-5.520954,-7.676806,-5.710116,-6.992854,6.402585,-8.885128,3.346358,1.092085,-3.929455,1.030342,8.812524,-7.109146,-5.489383,8.316041,3.658874,0.333632,-1.962774,9.948534,8.098581,5.263139,-9.351898,-0.719379,3.684945,8.709719,-4.846826,-3.120347,5.452696,-1.639887,4.012807,5.536542,-8.554997,-3.673209,-1.117252,3.297222,1.780057,-2.533492,0.681785,5.376472,-8.775761,-8.151813,-9.596437,-4.771286,7.751003,6.454647,0.626016,-7.805526,5.852391,-3.487822,-1.706752,4.344535,-1.678630,1.858526,-7.472630,-1.859540,2.969756,8.117097,-3.133393,6.039781,-6.393138,-2.837595,8.633972,-9.308330,-3.702854,5.220989,-5.027613,-0.167122,-6.051000,-1.639193,9.918115,-8.326158,0.281488,-0.318870,7.295596,-6.543379,-1.129837,7.394095,1.351521,-4.367118,1.081017,-0.276190,-9.074010,-6.854055,-2.124730,0.111896,-8.350430,-8.817783,5.125460,5.098228,-7.238493,1.378700,-2.477797,3.960277,-9.954968,2.725356,5.154848,9.806321,7.700912,-3.783009,4.153969,1.844609,5.739821,5.541751,-6.633159,-1.902998,-7.678993,6.497039,-8.154761,-3.819137,-9.882653,-4.810619,1.570900,6.901662,-6.912976,-9.568165,1.230860,9.610672,7.526463,7.893913,5.458030,2.928059,2.685934,-1.136469,0.222194,-0.167070,7.134787,7.385892,8.619738,7.371248,-9.581452,2.538653,9.488509,6.175966,1.585692,-0.504978,-1.611750,1.870721,-5.417390,0.777588,-2.409906,5.840356,4.256803,8.405637,5.506795,-4.322692,-6.479699,8.871394,-7.866584,2.296209,7.347448,-0.630014,7.311494,-2.808977,7.458131,1.080938,8.746970,9.412524,8.030445,8.962544,4.420597,-5.572444,8.207435,8.503004,-5.950096,-4.394673,-1.332656,4.853680,-4.018709,9.671468,-8.732102,3.839240,3.392322,-4.750380,5.622751,8.469088,2.633635,9.084032,3.752015,-9.605233,5.661891,-0.641936,0.797206,0.849315,8.137712,5.438744,6.453228,6.923919,-5.602914,2.842402,-5.154782,-1.115856,-9.410650,-5.535750,1.826896,-9.553519,6.889663,-3.098288,-5.765069,-6.002590,1.748094,1.763914,0.117241,1.074540,-3.750179,8.314555,-9.820802,-9.836153,8.422916,-6.160724,0.386846,8.123495,2.713434,8.712515,8.154674,7.407033,-3.656594,5.317386,-1.171713,1.751101,5.169858,0.594142,-8.349026,6.908898,-3.453587,-1.389339,-6.365305,5.250097,-7.884796,9.808762,-3.485192,-3.080601,-0.616412,-3.451598,-5.688707,9.157576,0.386702,9.446707,8.431103,2.324847,1.903409,0.067888,-7.618944,5.938689,-2.819680,-8.760411,-7.064701,0.291808,1.205237,6.747654,4.373485,4.906054,5.092935,-3.260094,1.255508,-5.764639,-9.141686,-4.836613,-8.528409,5.147623,3.143311,-8.653863,-4.174047,-9.367757,3.125266,7.177065,-1.714686,1.922034,-8.875899,-8.964799,-4.916553,-5.923011,6.497851,1.063634,-6.787936,-2.090071,-2.099238,8.945306,-1.571836,-2.925093,5.033357,-5.002431,8.180419,2.236208], dtype = "float32")#candidate|6191|(1470,)|const|float32
const_6192 = relay.const([3.829982,-7.945978,7.258657,-7.662307,-3.031440,2.513865,7.690733,6.729336,-4.568182,-5.656640,-0.193013,3.761220,-6.014095,5.511566,0.465765,9.239950,-2.846078,9.792113,6.979263,7.584986,-5.864212,2.003408,-2.066021,4.262627,-2.289977,-3.546273,-5.002421,-1.550304,8.613702,-4.765267,3.873115,7.687495,-1.395920,3.457561,-0.249184,3.446006,4.123293,2.448639,-0.925896,-2.712560,-2.407779,3.475965,-1.849712,3.436285,6.154525,-2.508548,-7.827567,-7.615076,-5.896021,-1.629112,-4.443250,9.347376,-0.260065,0.683782,5.485553,-8.633217,5.074265,-8.826810,4.520473,5.648133,-3.436623,1.847612,2.361169,6.498479,5.985213,-8.445181,7.403328,0.849084,-7.442575,-2.504956,-4.313184,7.819725,-0.613229,-8.061481,-7.595835,-4.103301,0.624768,0.756963,1.896217,2.132557,-3.258782,7.166973,3.837803,-7.952371,5.813298,-5.312903,4.496094,0.895642,7.090236,0.296930,6.568166,-9.421472,-2.798145,7.098773,-3.813563,-0.485993,2.040977,1.914474,8.917177,-0.690550,-3.982968,-8.155352,5.254896,-9.594402,2.967299,-1.734129,0.549459,-0.495906,-4.203133,-0.194794,-2.248900,7.296151,-3.797098,-1.277547,-6.607373,-7.766804,9.550581,-6.183203,4.029547,-3.890278,0.949744,4.702640,8.835518,-6.060136,-8.542967,3.105915,4.792328,-0.852936,2.597252,3.576235,9.509679,-7.305551,9.635550,1.675800,4.589494,5.427484,-6.839038,-8.215858,-6.720701,4.000341,0.139073,7.002084,-6.004000,-4.675090,4.463123,8.534700,1.498887,3.735892,1.506894,7.130540,-6.350642,1.169348,-3.460447,0.583335,-9.617777,3.607778,7.997032,-2.736225,-4.899411,4.546895,0.136528,-0.307466,-5.734703,0.002477,6.176145,7.221407,7.831242,-1.479199,-0.626916,9.669333,4.454541,-4.994361,0.270413,-4.774002,5.420552,5.451960,-5.935344,3.690991,-7.779863,-1.978610,-8.751447,8.493106,-4.483760,1.009286,1.123669,3.785126,6.412315,5.855077,0.979307,-2.290939,2.555303,9.056535,5.945459,2.161897,7.318828,7.866388,0.245923,6.200065,5.977599,-4.149201,0.732331,9.311405,3.284290,-1.549445,-4.953140,2.332599,-6.102814,8.218052,4.274963,6.203515,9.852379,-5.072294,-4.231156,-6.610147,-2.919276,-3.240716,4.275332,-3.212516,6.659667,2.413726,0.208085,6.120112,8.986255,-7.060918,7.521980,2.864901,-7.594498,3.402396,6.103682,-7.380491,-1.757770,-3.350964,-1.563395,-4.100035,8.409289,3.149924,-1.696247,-5.929097,-4.163504,3.221458,3.255574,-4.366930,-3.018918,-5.956080,7.911270,-1.877581,3.953795,8.090476,3.685776,1.301530,0.367199,-0.938815,-9.079746,1.941643,0.848051,-1.315701,2.780216,-2.650079,1.697986,-2.871114,-2.392747,-6.793681,2.967955,1.258473,-0.081454,1.303780,-8.664521,1.101435,-4.682813,2.159571,5.350255,-6.805744,-8.838008,8.233610,4.269692,-7.079474,-7.701842,-3.280120,7.407690,-4.456644,-2.720324,6.658468,4.165970,9.923122,-3.218249,7.346743,1.420045,-9.883942,3.722849,3.817900,9.590566,-9.019630,-3.222792,9.880167,-5.212976,6.031073,3.917849,0.216966,-4.843002,0.048576,0.426100,-5.814931,-2.182177,-4.407725,-0.089086,6.788067,-8.466192,2.707127,-2.887745,-2.679587,7.816025,6.352646,-2.421530,1.781703,-3.639700,2.134595,-5.522266,-5.514668,1.926331,-4.023679,-1.726480,5.798801,2.045181,6.701452,-8.835571,-7.832569,-0.970720,-9.717324,8.114187,7.108684,-6.915596,6.616791,-7.165655,-5.490152,9.607162,-3.374835,-4.644310,-0.996285,-4.823865,3.814008,4.330980,-4.192834,0.837597,-6.669252,2.929507,-6.908998,5.287108,-9.414137,4.872034,3.437378,5.801862,-0.205004,7.096877,5.784268,4.291679,-8.028587,-1.272307,-2.395135,-9.615164,-0.212793,-1.727044,4.657068,4.343803,6.694697,-7.288477,2.369920,-6.391082,7.368057,-7.588212,-0.349567,4.795171,-3.579152,2.547153,-8.786214,6.693693,2.176586,9.709772,6.088577,-2.794493,-5.964290,8.877842,-0.615109,4.694108,-7.565748,-4.913788,7.141799,3.466400,-6.466608,-4.316571,-3.020807,8.523796,3.584306,9.986280,1.984383,-9.216054,-4.114015,3.172458,9.161603,9.592588,-0.802343,-3.940627,5.213170,3.483038,2.403901,-9.140751,-8.462358,0.031124,2.129863,-6.751210,9.870429,-0.352943,7.675453,-5.295243,-3.292630,-1.637278,-2.305100,9.293079,-9.119848,2.279352,-4.242083,-9.827401,3.613057,3.683504,-3.524536,-6.954392,-4.979417,2.743411,-4.539803,-7.729927,7.713121,-8.244143,-0.541471,-2.269312,-7.735420,-5.873124,8.806671,9.879960,-1.482276,7.726405,4.453529,-5.919335,-9.100647,0.312522,-3.373238,-3.972727,-8.210085,7.311905,-1.720282,0.894306,9.447123,9.658919,-1.058863,1.049053,4.042610,2.969252,-6.540186,-7.684256,-4.606174,-5.960757,-4.492637,-6.697476,7.509178,1.142816,0.961746,-0.952049,-2.684884,-0.752702,3.784075,7.402615,-1.572288,6.524824,9.191180,-2.482311,8.061088,-0.938344,3.103419,-1.597448,-4.750236,-0.743653,-3.842719,-8.427071,-9.936394,-8.843144,-9.463389,1.566482,-3.534429,-5.663586,-8.330996,9.871761,1.930391,2.099670,0.192319,0.470741,8.389396,0.966296,-7.586170,-5.586762,-4.336307,-2.654392,4.455470,-7.352282,-1.944888,6.496163,2.339614,-8.874294,-2.746633,7.598793,6.860938,9.458696,-1.815162,4.969576,-3.484602,6.887613,-6.662300,1.838259,6.251794,5.950624,-4.129456,8.467498,-1.984634,-1.901003,5.218796,-6.797127,-9.426214,-6.747681,-4.683127,-3.811553,8.074947,-0.948428,0.627790,3.044452,3.986510,4.665809,2.916927,4.062761,-2.469922,-7.404897,3.835294,2.412823,-6.281278,-6.806049,7.932318,2.086821,-9.674744,-5.965499,-3.055634,6.510173,-7.106253,0.069184,1.968164,6.050286,4.034596,8.883508,-3.601929,-4.096660,-5.365571,-1.284066,4.379065,6.496519,9.460132,-6.352852,1.809794,0.251038,-9.603502,-7.228542,3.878464,1.620157,5.290404,7.177538,0.976849,3.412875,-8.028046,1.975070,7.146769,8.626343,-5.673331,-2.966810,5.558291,-2.590058,2.076017,0.801052,-4.429710,4.356339,-8.409421,-4.016227,-2.671629,9.254302,3.032912,6.726169,1.733725,3.097740,-2.517362,-6.996900,6.788130,3.199184,7.641158,0.643378,1.678088,4.928639,2.293190,-2.710613,2.920845,-0.749851,-1.892052,-9.301931,-5.865060,-4.395645,1.324385,0.396343,1.844314,1.777393,2.998038,-9.992228,1.158865,-6.116389,6.243947,8.337266,2.281793,3.765589,0.012309,7.808429,5.037762,-7.686620,-3.582347,2.358352,-8.362765,-3.363073,2.630565,-9.657269,3.895305,9.882950,6.490876,2.157280,-7.846150,4.675318,-7.962947,-5.186316,-3.513727,6.767230,-0.770224,-7.864766,2.726905,-0.239594,9.838491,-8.466653,-5.530677,-5.774044,-8.047906,-1.828290,-5.512056,-1.159542,-3.653461,3.366968,1.561811,-8.059347,0.381821,-7.790491,9.839455,-6.506170,2.891812,4.408915,-9.963677,-2.875293,-4.249570,-8.728986,-2.632108,1.059402,8.098291,1.653873,0.174572,-6.721193,-9.540763], dtype = "float64")#candidate|6192|(672,)|const|float64
call_6189 = relay.TupleGetItem(func_3994_call(relay.reshape(const_6190.astype('uint64'), [4, 12, 13]), relay.reshape(const_6191.astype('float32'), [7, 210]), relay.reshape(const_6192.astype('float64'), [168, 4]), ), 2)
call_6193 = relay.TupleGetItem(func_3999_call(relay.reshape(const_6190.astype('uint64'), [4, 12, 13]), relay.reshape(const_6191.astype('float32'), [7, 210]), relay.reshape(const_6192.astype('float64'), [168, 4]), ), 2)
func_5398_call = mod.get_global_var('func_5398')
func_5400_call = mutated_mod.get_global_var('func_5400')
call_6196 = relay.TupleGetItem(func_5398_call(), 1)
call_6197 = relay.TupleGetItem(func_5400_call(), 1)
func_4622_call = mod.get_global_var('func_4622')
func_4625_call = mutated_mod.get_global_var('func_4625')
call_6217 = relay.TupleGetItem(func_4622_call(relay.reshape(const_6192.astype('float64'), [2, 336])), 1)
call_6218 = relay.TupleGetItem(func_4625_call(relay.reshape(const_6192.astype('float64'), [2, 336])), 1)
uop_6255 = relay.asin(const_6190.astype('float32')) # shape=(24, 26)
func_3675_call = mod.get_global_var('func_3675')
func_3677_call = mutated_mod.get_global_var('func_3677')
var_6273 = relay.var("var_6273", dtype = "float64", shape = (64, 12))#candidate|6273|(64, 12)|var|float64
call_6272 = relay.TupleGetItem(func_3675_call(relay.reshape(var_6273.astype('float64'), [8, 8, 12])), 0)
call_6274 = relay.TupleGetItem(func_3677_call(relay.reshape(var_6273.astype('float64'), [8, 8, 12])), 0)
uop_6290 = relay.erf(uop_6255.astype('float32')) # shape=(24, 26)
uop_6310 = relay.tan(call_6196.astype('float32')) # shape=(5, 15, 3)
uop_6312 = relay.tan(call_6197.astype('float32')) # shape=(5, 15, 3)
output = relay.Tuple([bop_6185,call_6189,const_6191,const_6192,call_6217,call_6272,var_6273,uop_6290,uop_6310,])
output2 = relay.Tuple([bop_6188,call_6193,const_6191,const_6192,call_6218,call_6274,var_6273,uop_6290,uop_6312,])
func_6313 = relay.Function([var_6184,var_6273,], output)
mod['func_6313'] = func_6313
mod = relay.transform.InferType()(mod)
mutated_mod['func_6313'] = func_6313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6313_call = mutated_mod.get_global_var('func_6313')
var_6315 = relay.var("var_6315", dtype = "bool", shape = (14, 7, 9))#candidate|6315|(14, 7, 9)|var|bool
var_6316 = relay.var("var_6316", dtype = "float64", shape = (64, 12))#candidate|6316|(64, 12)|var|float64
call_6314 = func_6313_call(var_6315,var_6316,)
output = call_6314
func_6317 = relay.Function([var_6315,var_6316,], output)
mutated_mod['func_6317'] = func_6317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5711_call = mod.get_global_var('func_5711')
func_5713_call = mutated_mod.get_global_var('func_5713')
call_6367 = relay.TupleGetItem(func_5711_call(), 0)
call_6368 = relay.TupleGetItem(func_5713_call(), 0)
func_6313_call = mod.get_global_var('func_6313')
func_6317_call = mutated_mod.get_global_var('func_6317')
var_6379 = relay.var("var_6379", dtype = "float64", shape = (768,))#candidate|6379|(768,)|var|float64
call_6378 = relay.TupleGetItem(func_6313_call(relay.reshape(call_6367.astype('bool'), [14, 7, 9]), relay.reshape(var_6379.astype('float64'), [64, 12]), ), 3)
call_6380 = relay.TupleGetItem(func_6317_call(relay.reshape(call_6367.astype('bool'), [14, 7, 9]), relay.reshape(var_6379.astype('float64'), [64, 12]), ), 3)
output = relay.Tuple([call_6367,call_6378,var_6379,])
output2 = relay.Tuple([call_6368,call_6380,var_6379,])
func_6387 = relay.Function([var_6379,], output)
mod['func_6387'] = func_6387
mod = relay.transform.InferType()(mod)
var_6388 = relay.var("var_6388", dtype = "float64", shape = (768,))#candidate|6388|(768,)|var|float64
output = func_6387(var_6388)
func_6389 = relay.Function([var_6388], output)
mutated_mod['func_6389'] = func_6389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5711_call = mod.get_global_var('func_5711')
func_5713_call = mutated_mod.get_global_var('func_5713')
call_6395 = relay.TupleGetItem(func_5711_call(), 0)
call_6396 = relay.TupleGetItem(func_5713_call(), 0)
output = relay.Tuple([call_6395,])
output2 = relay.Tuple([call_6396,])
func_6407 = relay.Function([], output)
mod['func_6407'] = func_6407
mod = relay.transform.InferType()(mod)
output = func_6407()
func_6408 = relay.Function([], output)
mutated_mod['func_6408'] = func_6408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_6430 = func_4727_call()
call_6431 = func_4727_call()
output = relay.Tuple([call_6430,])
output2 = relay.Tuple([call_6431,])
func_6436 = relay.Function([], output)
mod['func_6436'] = func_6436
mod = relay.transform.InferType()(mod)
mutated_mod['func_6436'] = func_6436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6436_call = mutated_mod.get_global_var('func_6436')
call_6437 = func_6436_call()
output = call_6437
func_6438 = relay.Function([], output)
mutated_mod['func_6438'] = func_6438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_6452 = relay.TupleGetItem(func_4774_call(), 0)
call_6453 = relay.TupleGetItem(func_4776_call(), 0)
func_6123_call = mod.get_global_var('func_6123')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_6457 = relay.TupleGetItem(func_6123_call(relay.reshape(call_6452.astype('float32'), [11, 12, 4])), 0)
call_6458 = relay.TupleGetItem(func_6126_call(relay.reshape(call_6452.astype('float32'), [11, 12, 4])), 0)
uop_6468 = relay.exp(call_6457.astype('float32')) # shape=(11, 12, 4)
uop_6470 = relay.exp(call_6458.astype('float32')) # shape=(11, 12, 4)
func_5847_call = mod.get_global_var('func_5847')
func_5848_call = mutated_mod.get_global_var('func_5848')
call_6471 = func_5847_call()
call_6472 = func_5847_call()
output = relay.Tuple([call_6452,uop_6468,call_6471,])
output2 = relay.Tuple([call_6453,uop_6470,call_6472,])
func_6473 = relay.Function([], output)
mod['func_6473'] = func_6473
mod = relay.transform.InferType()(mod)
output = func_6473()
func_6474 = relay.Function([], output)
mutated_mod['func_6474'] = func_6474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4873_call = mod.get_global_var('func_4873')
func_4874_call = mutated_mod.get_global_var('func_4874')
call_6475 = relay.TupleGetItem(func_4873_call(), 0)
call_6476 = relay.TupleGetItem(func_4874_call(), 0)
var_6477 = relay.var("var_6477", dtype = "bool", shape = (14, 7, 9))#candidate|6477|(14, 7, 9)|var|bool
bop_6478 = relay.bitwise_and(call_6475.astype('int8'), relay.reshape(var_6477.astype('int8'), relay.shape_of(call_6475))) # shape=(14, 7, 9)
bop_6481 = relay.bitwise_and(call_6476.astype('int8'), relay.reshape(var_6477.astype('int8'), relay.shape_of(call_6476))) # shape=(14, 7, 9)
func_5676_call = mod.get_global_var('func_5676')
func_5679_call = mutated_mod.get_global_var('func_5679')
const_6486 = relay.const([4.658115,6.229413,0.436775,-5.884481,-2.376829,-2.121616,6.085425,6.791242,-8.138550,8.582427,2.332041,5.467509,6.854457,-9.366135,-3.989907,-9.764937,-7.491145,-9.534476,-1.740404,-6.551187,-8.952711,8.107736,-9.393058,3.880075,0.015372,7.701845,2.341598,-5.743324,9.615564,9.434590,6.712872,5.530141,1.240849,-6.769600,-0.997352,-7.236899,8.228535,-6.141897,3.757589,-5.215379,-3.940255,1.725627,-6.837798,-7.878086,-0.569401,-8.717608,-8.957045,-4.721139,5.033957,8.771259,1.210433,-6.869535,-5.386902,-6.483954,7.856017,-1.347132,-1.366360,0.525980,8.796013,-1.581844,3.059345,-6.103478,-2.584546,-6.271137,1.102916,-1.104451,0.551415,9.816704,6.946837,6.384028,-2.066345,8.794007,-7.344707,-5.500417,-8.759156,0.029663,4.762318,3.360069,-8.062079,4.249557,-7.859487,-7.389948,8.849873,6.147695,-2.399157,2.094594,-4.774591,7.715718,2.507569,2.012848,6.958676,7.781849,-9.129992,-2.781675,-9.358160,-3.709437,0.713016,6.864399,-6.470606,-1.553199,5.586306,7.850144,-5.939168,-2.731181,-9.151637,5.922117,8.687527,-4.930057,-0.640399,-6.999107,5.885851,4.576211,-1.000730,1.188025,4.076499,3.656125,3.672118,-1.939566,4.327327,3.172987,-2.858644,3.538431,6.429402,5.340560,2.383594,7.977594,-2.081677,4.616486,8.660992,6.977455,-9.555668,0.700695,-7.678179,1.436324,4.706263,4.006344,-5.662423,0.062073,4.344770,6.727527,-5.774372,9.617358,0.406601,3.168163,8.554535,0.814232,5.844858,9.875843,-2.575836,-8.124812,5.124534,-1.400479,-7.866809,1.462567,-1.597965,-3.459739,5.315764,-9.539600,4.911450,5.007305,-9.685228,-1.310796,-7.582835,4.763681,7.122857,-7.002377,-3.685010,-6.730498,-7.466248,-4.192093,-8.206897,3.548412,-3.877330,-3.542494,-2.279346,-4.941310,-5.597565,-0.858972,-2.282314,4.890914,2.879693,-7.990973,-2.966050,3.332560,-0.518887,-0.661797,-9.044742,7.276693,6.400156,-6.463903,1.548731,-5.250620,-0.779765,-3.030206,3.978232,-8.879439,6.004104,-3.865736,2.601417,-6.797349,4.911491,-0.742808,5.073773,-3.023970,0.908732,-8.054843,7.970150,-2.252533,7.360404,-9.631504,-1.659997,-3.117861,2.070346,-4.321381,-3.923810,-5.694048,6.681340,9.273465,-7.913952,1.389388,3.903723,0.895536,-4.558526,-0.644076,-4.921722,-4.645270,2.840286,7.122155,1.477470,4.595361,-7.928851,8.306433,-7.467411,-1.488868,-9.540308,-8.646362,1.815418,-7.432513,0.168872,-9.407084,3.685818,-3.147814,2.077752,9.562239,1.589459,-1.451160,0.024168,4.683337,-6.718938,-1.962474,8.514074,-4.834740,-0.664923,8.411327,2.512903,-0.036331,-1.705126,5.373015,-9.198073,6.447695,5.810597,7.179861,7.376667,-0.596741,2.142302,1.776435,0.025322,8.527460,-0.017583,3.151357,-2.336612,8.950646,5.887651,-2.031261,6.290998,9.924281,7.692944,8.352442,-8.170842,1.808209,0.099053,-5.226122,-2.515665,-6.630523,-1.749985,2.909599,8.053423,-0.256042,0.670936,-2.579058,-9.590365,-5.811445,1.229871,-6.781083,4.004452,3.068071,-7.477103,-7.753339,2.818874,-9.854622,-0.061607,1.244740,-9.399962,-3.624375,-5.879161,-9.135289,3.163916,7.276557,7.823937,-5.113649,6.842784,9.984349,2.831000,-4.683638,-6.205166,4.965570,-7.572865,9.189161,-0.432151,3.505483,-2.421314,0.692298,-2.529202,-9.593257,-8.006751,-1.004466,-9.852162,-6.038271,9.480929,1.716681,3.653041,6.871464,5.304230,-7.584916,-1.181787,-5.368954,6.495755,-9.837007,-5.854714,1.969777,7.690058,-8.613621,2.859963,-2.686991,-9.056458,0.143691,-6.457808,2.973440,4.251240,1.388884,7.345550,-4.874140,6.759110,-6.463728,-4.607952,-5.496661,-1.148872,2.500372,6.159661,-8.561103,9.148323,0.010805,-7.642306,5.293015,-7.441477,-2.231243,1.350083,6.717090,4.648679,-2.631959,8.296589,-8.394898,-0.931957,-7.022679,9.343065,6.845123,-5.564159,-7.810223,4.181080,-3.962149,-6.896451,-6.809387,6.241493,-3.640045,5.441390,-3.240706,9.286941,-1.341075,6.343981,-1.366989,-9.214503,9.334004,-1.016334,5.314531,-3.643075,-5.329375,-7.353501,-7.697794,-3.096187,9.237152,0.663347,-3.410022,-0.774826,-0.099409,2.371490,-8.066186,-7.207600,-2.304950,7.567850,6.692098,3.877847,-6.928187,-0.976049,-3.154108,9.246679,-7.076984,4.269623,8.124917,-4.653771,8.597849,-6.441150,1.127523,-2.700101,-3.931321,3.389311,7.812108,4.905925,7.956409,-7.528700,-5.294769,8.202420,-4.554394,1.057890,-0.365028,-9.264946,-7.678774,4.709596,8.851783,6.159842,1.553637,9.171272,-5.294764,-0.964108,-0.539894,5.625220,-8.904899,-1.759455,8.924242,-8.514832,5.869812,-2.031145,-6.891425,6.425848,1.757793,3.955669,2.656767,4.142832,0.515071,0.968162,-7.628713,-2.804311,6.277513,6.885478,-7.565821,-5.082136,-2.543654,9.635556,-1.903130,0.141318,-6.292201,-7.507395,3.829350,6.473495,4.594705,0.842417,5.077852,-9.618109,-5.350150,2.462645,-8.436567,-9.907646,-4.562716,5.424279,-8.548128,-8.265228,4.351989,-3.901798,-6.916537,9.456903,4.988568,8.638548,-8.100808,9.758188,-8.763733,8.877289,7.974817,4.128893,-2.265805,-2.463341,9.295783,9.436906,-9.147979,-4.625438,4.932107,-4.481734,-0.309559,1.005430,-3.675464,6.496951,1.038553,9.828810,-1.195276,3.459854,1.029101,5.382227,-0.101927,1.884401,-4.813572,-4.395769,8.203597,-5.125408,-4.665929,-1.714674,3.022806,5.266306,-2.109265,2.480757,-8.396294,8.432343,-2.018730,-0.523158,4.308918,2.313744,4.615357,3.789254,1.012522,-2.138741,1.824992,-3.046906,-3.415516,-2.344815,-2.044452,0.691534,-5.035818,-1.932545,1.271040,1.538970,-5.082773,0.709706,-2.866925,-7.498015,-2.052221,-1.961382,1.547056,-8.238641,-5.663984,-1.561798,-8.632472,2.045105,8.442917,-4.607316,2.067595,6.981548,-9.262742,9.065062,-7.192822,-2.189688,5.228001,-9.275549,5.741326,-4.063186,2.207387,-1.252899,5.212328,-6.524387,0.758084,6.816742,0.027140,-5.162740,1.323848,-1.311042,1.078660,1.030897,9.307198,2.305449,-6.895124,1.801549,7.510453,-7.219777,6.671843,5.216427,7.028400,8.866129,2.244460,-3.129495,-7.719699,-2.907611,-8.255293,-9.253331,-8.954571,-7.994939,7.952861,-0.345404,-8.083728,0.024148,-0.517062,-7.371495,-1.685086,-6.748737,-6.312643,-1.713936,1.624964,-9.406571,-1.643465,-8.588043,0.997767,-9.734696,-5.842543,7.647980,6.391572,-7.252435,3.150500,6.734042,7.049612,8.903749,-5.870361,-2.562433,1.536608,6.427086,9.228067,-1.402088,6.354838,8.971116,8.767468,-4.379031,-9.611153,-6.686672,0.309728,7.510244,3.601220,-0.767213,-9.371905,-0.553859,-6.612284,-0.088663,1.489303,-1.991075,6.975142,-6.008810,-7.343258,4.191818,1.769371,-0.555939,6.691017,4.156875,-7.146700,-2.846315,-8.897042,-7.953420,3.034545,-7.137802,5.327799,9.987578,8.243858,-1.877707,-6.281592,-9.595779,1.717365,-7.190236,-7.831886,-0.935845,-3.674087], dtype = "float64")#candidate|6486|(672,)|const|float64
call_6485 = relay.TupleGetItem(func_5676_call(relay.reshape(const_6486.astype('float64'), [672,])), 1)
call_6487 = relay.TupleGetItem(func_5679_call(relay.reshape(const_6486.astype('float64'), [672,])), 1)
output = relay.Tuple([bop_6478,call_6485,const_6486,])
output2 = relay.Tuple([bop_6481,call_6487,const_6486,])
func_6488 = relay.Function([var_6477,], output)
mod['func_6488'] = func_6488
mod = relay.transform.InferType()(mod)
mutated_mod['func_6488'] = func_6488
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6489 = relay.var("var_6489", dtype = "bool", shape = (14, 7, 9))#candidate|6489|(14, 7, 9)|var|bool
func_6488_call = mutated_mod.get_global_var('func_6488')
call_6490 = func_6488_call(var_6489)
output = call_6490
func_6491 = relay.Function([var_6489], output)
mutated_mod['func_6491'] = func_6491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5847_call = mod.get_global_var('func_5847')
func_5848_call = mutated_mod.get_global_var('func_5848')
call_6584 = func_5847_call()
call_6585 = func_5847_call()
func_2380_call = mod.get_global_var('func_2380')
func_2383_call = mutated_mod.get_global_var('func_2383')
const_6595 = relay.const([5.786749,-4.861163,-2.948888,6.565251,7.052597,8.391043,0.438976,2.654328,-8.107028,9.054218,7.426454,1.122477,-9.575559,-1.821880,4.495204,6.107532,4.812967,1.176427,-3.348084,-9.349163,8.745362,-4.060643,-6.030680,-7.570200,-5.132182,1.838593,-5.209622,-2.882330,-5.854729,-4.190043,-4.366219,-4.570448,7.969088,1.381851,-1.606105,-8.050384,6.057111,-7.509573,-3.915351,-5.818512,0.880415,-7.393405,3.371105,-7.444773,-5.789315,7.412920,-8.885719,-0.494588,8.923840,-0.919422,-3.139340,-0.257136,9.374378,7.228641,5.738824,2.780319,5.123166,-2.185046,-8.864886,-5.509375,-3.390475,8.496734,6.314807,-0.126469,-2.899110,-8.518263,7.034914,-0.691647,-6.570676,7.716552,-5.652919,-6.606463,-9.663955,-6.050731,5.196491,9.281048,-0.045861,-4.578226,6.264977,-7.677645,8.515291,-3.150621,6.808696,-0.784399,-5.573783,2.059555,-4.364084,0.575472,6.880786,7.815216,-8.407372,-2.056822,-8.293837,4.090912,7.229097,8.068866,-1.786779,-1.418922,-1.537136,7.409974,-8.777216,9.905483,-9.036314,3.444428,-1.119310,-3.800912,-1.068877,0.800859,-9.630884,-7.626000,6.219181,-0.594859,2.459584,8.343964,9.378372,-7.700122,-6.047374,-5.545443,-1.772626,-2.172066,8.565310,-2.176237,5.170247,-2.611359,-1.098058,8.113255,-1.757158,9.805134,-8.345044,1.734611,-7.855951,4.709272,-7.341341,5.989247,-9.970716,7.328322,8.189563,5.539985,-2.654135,-3.536455,-9.212195,-0.585821,7.480287,-8.352816,-3.395485,-8.053552,8.648415,0.584253,6.265286,9.057023,-9.232362,4.957996,-3.196036,-6.594676,-7.637732,1.926839,2.018887,9.419053,9.919824,-4.528515,-8.358828,-8.814719,4.005599,6.730838,2.588447,-0.899679,3.345497,7.352180,-0.391986,-2.497172,-0.970587,0.941007,1.094697,-8.815781,-0.391238,4.852693,5.341610,-6.534327,7.304668,-3.304518,-6.843441,4.516119,-3.176782,3.221094,-9.717995,-8.200179,7.667101,-5.782317,-6.944713,-1.900976,-8.473541,0.829056,4.579341,-1.010043,7.346541,7.506030,1.058643,-3.553574,8.481641,-1.118706,7.740611,-5.843609,-0.567071,-5.671948,-5.824485,3.755878,-0.351199,-0.002937,-3.542783,-4.435881,9.860895,-1.084408,-7.815787,1.001907,-2.674297,-9.809878,-5.118261,7.035904,6.542364,1.476686,-5.843359,-3.492156,-0.135620,-3.179488,6.222291,-9.512098,3.756313,4.906474,2.332561,5.350827,-1.522607,-4.900832,3.462416,5.552653,4.875523,-7.997978,2.406568,-6.595789,9.931502,5.023620,1.454053,-2.770423,-9.970039,4.828606,-6.603662,4.905749,-7.883093,8.557563,5.561139,-5.069938,4.915093,-9.345425,-8.787075,-2.827524,-7.754323,-4.036748,-8.510943,-2.463828,1.960117,-9.027166,-2.814137,-2.350248,8.785403,-9.045972,4.743564,7.664880,7.241705,5.805813,-5.991796,-0.147252,6.201142,4.714940,1.578450,-1.251130,7.908000,-4.067424,9.713414,-4.165938,-8.366987,9.574269,9.394474,-5.563458,9.137354,-6.147345,-0.434739,-6.862046,-2.374008,0.098099,1.546559,-6.493790,-0.990496,-5.764090,1.075581,4.303526,-4.419766,5.814705,5.277730,-6.861892,-7.261449,0.597442,2.522110,-5.302867,0.984674,3.401326,-4.812480,8.087404,-9.249939,-8.115087,-3.884440,4.727787,-2.362357,-4.458399,3.892556,-6.099292,-5.742679,-8.010784,2.340963,9.588945,-5.321933,2.015991,-4.509452,4.285639,2.716909,-2.641357,9.926496,-5.623151,9.210746,-1.479491,1.050321,-1.730125,-5.752966,-3.562980,3.333208,-4.688492,-1.018361,-0.281282,-5.255858,-9.515581,4.633047,8.835556,-2.904686,4.763477,-5.932534,-1.546786,-0.225548,0.607506,3.717015,7.785840,7.577722,-2.377347,3.873433,-5.748186,8.911966,8.854202,-7.739509,0.607181,-2.610206,-8.790906,-9.762250,0.888332,7.308037,5.855605,-0.673483,7.906120,-1.323661,0.366183,6.897641,9.722285,-5.318523,6.330074,4.715027,-9.581405,1.254154,9.805234,9.301847,3.990600,7.166587,-7.685632,4.169251,-3.299007,4.617268,3.063467,7.896312,1.100393,-0.637934,-5.100779,-5.262803,7.154605,0.295307,6.198776,5.471872,9.462863,-6.877401,-4.670895,-7.090588,8.232877,6.860480,-7.048345,-8.424968,-7.707267,-6.550345,-9.006430,8.369776,2.385992,-4.593581,-5.927422,2.921308,2.523529,0.902107,6.250784,-8.865364,8.226029,9.664284,-7.752769,-5.182962,-2.856082,-8.445686,8.957186,6.432532,-9.646870,5.822546,8.161829,2.657918,-4.457129,3.691264,-7.675792,7.635642,4.774204,7.551250,-6.665602,-2.694565,-3.515856,7.169146,0.805061,-3.492812,3.070237,-5.179263,-0.588277,2.655500,-2.225645,-7.629870,-4.773065,-4.726322,7.164853,6.274029,7.052490,-9.143196,-3.246593,2.813362,-6.551258,-8.954570,-1.385551,6.252655,-0.037628,4.408934,4.725841,5.524940,8.215693,1.289445,8.244549,-1.447992,-2.942351,-4.514789,5.933965,-3.113862,-4.941752,3.689097,7.542250,8.639721,1.564269,-2.409669,5.362389,-5.907796,-7.888998,8.561780,-0.671780,-5.664930,-2.018786,-4.566534,1.122627,-7.496279,4.204595,-7.578544,-8.391523,-1.267220,-3.221121,-6.927254,-4.485447,4.277641,-7.795893,-3.817061,-1.914797,2.639854,0.148387,-5.638065,3.810167,-5.673577,-0.382916,1.242767,1.960663,-3.847986,1.106926,8.068789,3.609930,-6.956756,7.752640,3.247819,3.534585,-1.696641,-9.958747,7.372794,8.579275,-8.607352,-5.979119,-2.740357,2.251851,-0.611336,9.244785,-2.835298,-6.802755,-5.561133,0.559424,0.499151,0.805122,0.131960,8.956715,8.732615,9.737150,-4.547869,7.672596,4.862858,-5.743693,9.317119,0.311876,-1.288060,-2.127075,9.563665,-9.641953,8.370032,-0.683579,5.869822,8.640193,5.185593,-1.381680,6.845477,-4.685796,-7.426540,-1.533645,6.492608,1.153365,1.305083,-9.171275,4.071713,3.598269,-4.017586,-8.393448,8.307250,-9.732834,-8.168448,2.360997,8.034970,-4.953570,-9.501141,9.878956,-0.451238,8.997766,7.788920,-1.027494,7.867835,8.429328,1.223755,4.429402,4.005166,0.504667,3.886151,4.380441,1.629594,-2.004005,-5.850177,6.075003,0.068486,-1.747306,-8.059431,3.450572,7.776066,-8.963577,-4.093130,6.231496,6.444172,5.834896,8.816543,7.812220,-6.918403,-4.253951,-1.544756,9.596247,2.836239,-6.586751,-7.858337,3.865112,-2.063320,4.904122,0.831663,-5.498533,3.377476,5.895136,8.538764,5.749734,2.931877,-3.087413,5.695731,0.550357,-1.123234,1.690575,7.320634,-0.981138,-8.844910,0.126254,-7.098504,-7.691568,2.940928,3.852121,7.448421,2.573944,-7.049903,-5.056075,7.859938,-7.241236,9.832648,3.047901,-5.445662,-3.649814,6.240215,4.234930,5.383419,5.331506,1.304947,5.269048,-9.362299,5.815230,2.430377,-0.951031,6.537938,-7.068635,-9.747206,-2.489302,2.692998,7.713540,-1.806977,-5.711745,3.144072,-0.179652,-7.747809,2.499106,-3.681600,-7.051373,-9.723720,6.458701,0.053258,-7.221796,6.526339,6.373109,1.359657,1.573753,7.746754,6.746227,4.432345,2.192353,-2.062762,-6.176174,-9.683186,-1.309672,-2.249908,-7.997559,5.278974,4.405539,8.663342,7.276277,-2.416009,-2.801308,-8.760602,-3.320877,-3.046683,-7.723251,-3.097244,0.766955,2.887488,5.242259,2.532752,7.870414,-9.037416,0.184705,2.665524,-0.117145,3.839093,1.406590,-9.290010,-0.030321,-0.638805,9.371266,4.305427,1.737539,-2.155104,-4.128671,-6.636404,-5.566109,0.385682,5.308245,-9.899840,-3.566946,-3.788747,-5.291383,4.074273,2.478643,8.364359,-2.980232,-7.597660,7.370232,-9.013091,-0.241420,4.547172,6.271804,1.931736,-6.585916,-4.520037,5.706193,-3.692352,6.330639], dtype = "float64")#candidate|6595|(728,)|const|float64
var_6596 = relay.var("var_6596", dtype = "int8", shape = (225,))#candidate|6596|(225,)|var|int8
call_6594 = relay.TupleGetItem(func_2380_call(relay.reshape(const_6595.astype('float64'), [13, 8, 7]), relay.reshape(var_6596.astype('int8'), [225,]), ), 0)
call_6597 = relay.TupleGetItem(func_2383_call(relay.reshape(const_6595.astype('float64'), [13, 8, 7]), relay.reshape(var_6596.astype('int8'), [225,]), ), 0)
output = relay.Tuple([call_6584,call_6594,const_6595,var_6596,])
output2 = relay.Tuple([call_6585,call_6597,const_6595,var_6596,])
func_6606 = relay.Function([var_6596,], output)
mod['func_6606'] = func_6606
mod = relay.transform.InferType()(mod)
mutated_mod['func_6606'] = func_6606
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6607 = relay.var("var_6607", dtype = "int8", shape = (225,))#candidate|6607|(225,)|var|int8
func_6606_call = mutated_mod.get_global_var('func_6606')
call_6608 = func_6606_call(var_6607)
output = call_6608
func_6609 = relay.Function([var_6607], output)
mutated_mod['func_6609'] = func_6609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4850_call = mod.get_global_var('func_4850')
func_4852_call = mutated_mod.get_global_var('func_4852')
call_6675 = relay.TupleGetItem(func_4850_call(), 0)
call_6676 = relay.TupleGetItem(func_4852_call(), 0)
output = relay.Tuple([call_6675,])
output2 = relay.Tuple([call_6676,])
func_6704 = relay.Function([], output)
mod['func_6704'] = func_6704
mod = relay.transform.InferType()(mod)
mutated_mod['func_6704'] = func_6704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6704_call = mutated_mod.get_global_var('func_6704')
call_6705 = func_6704_call()
output = call_6705
func_6706 = relay.Function([], output)
mutated_mod['func_6706'] = func_6706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5273_call = mod.get_global_var('func_5273')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_6710 = relay.TupleGetItem(func_5273_call(), 0)
call_6711 = relay.TupleGetItem(func_5274_call(), 0)
output = relay.Tuple([call_6710,])
output2 = relay.Tuple([call_6711,])
func_6712 = relay.Function([], output)
mod['func_6712'] = func_6712
mod = relay.transform.InferType()(mod)
mutated_mod['func_6712'] = func_6712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6712_call = mutated_mod.get_global_var('func_6712')
call_6713 = func_6712_call()
output = call_6713
func_6714 = relay.Function([], output)
mutated_mod['func_6714'] = func_6714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6704_call = mod.get_global_var('func_6704')
func_6706_call = mutated_mod.get_global_var('func_6706')
call_6740 = relay.TupleGetItem(func_6704_call(), 0)
call_6741 = relay.TupleGetItem(func_6706_call(), 0)
uop_6754 = relay.rsqrt(call_6740.astype('float64')) # shape=(882,)
uop_6756 = relay.rsqrt(call_6741.astype('float64')) # shape=(882,)
bop_6761 = relay.less_equal(uop_6754.astype('bool'), relay.reshape(call_6740.astype('bool'), relay.shape_of(uop_6754))) # shape=(882,)
bop_6764 = relay.less_equal(uop_6756.astype('bool'), relay.reshape(call_6741.astype('bool'), relay.shape_of(uop_6756))) # shape=(882,)
output = bop_6761
output2 = bop_6764
func_6771 = relay.Function([], output)
mod['func_6771'] = func_6771
mod = relay.transform.InferType()(mod)
output = func_6771()
func_6772 = relay.Function([], output)
mutated_mod['func_6772'] = func_6772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_6861 = relay.TupleGetItem(func_5054_call(), 2)
call_6862 = relay.TupleGetItem(func_5055_call(), 2)
output = call_6861
output2 = call_6862
func_6865 = relay.Function([], output)
mod['func_6865'] = func_6865
mod = relay.transform.InferType()(mod)
mutated_mod['func_6865'] = func_6865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6865_call = mutated_mod.get_global_var('func_6865')
call_6866 = func_6865_call()
output = call_6866
func_6867 = relay.Function([], output)
mutated_mod['func_6867'] = func_6867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6704_call = mod.get_global_var('func_6704')
func_6706_call = mutated_mod.get_global_var('func_6706')
call_6932 = relay.TupleGetItem(func_6704_call(), 0)
call_6933 = relay.TupleGetItem(func_6706_call(), 0)
func_5321_call = mod.get_global_var('func_5321')
func_5322_call = mutated_mod.get_global_var('func_5322')
call_6944 = relay.TupleGetItem(func_5321_call(), 0)
call_6945 = relay.TupleGetItem(func_5322_call(), 0)
uop_6956 = relay.exp(call_6932.astype('float32')) # shape=(882,)
uop_6958 = relay.exp(call_6933.astype('float32')) # shape=(882,)
func_6123_call = mod.get_global_var('func_6123')
func_6126_call = mutated_mod.get_global_var('func_6126')
call_6959 = relay.TupleGetItem(func_6123_call(relay.reshape(call_6944.astype('float32'), [11, 12, 4])), 0)
call_6960 = relay.TupleGetItem(func_6126_call(relay.reshape(call_6944.astype('float32'), [11, 12, 4])), 0)
output = relay.Tuple([call_6944,uop_6956,call_6959,])
output2 = relay.Tuple([call_6945,uop_6958,call_6960,])
func_6964 = relay.Function([], output)
mod['func_6964'] = func_6964
mod = relay.transform.InferType()(mod)
mutated_mod['func_6964'] = func_6964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6964_call = mutated_mod.get_global_var('func_6964')
call_6965 = func_6964_call()
output = call_6965
func_6966 = relay.Function([], output)
mutated_mod['func_6966'] = func_6966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5245_call = mod.get_global_var('func_5245')
func_5246_call = mutated_mod.get_global_var('func_5246')
call_6979 = func_5245_call()
call_6980 = func_5245_call()
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
var_7007 = relay.var("var_7007", dtype = "bool", shape = (882,))#candidate|7007|(882,)|var|bool
call_7006 = relay.TupleGetItem(func_1401_call(relay.reshape(var_7007.astype('bool'), [14, 7, 9])), 0)
call_7008 = relay.TupleGetItem(func_1403_call(relay.reshape(var_7007.astype('bool'), [14, 7, 9])), 0)
output = relay.Tuple([call_6979,call_7006,var_7007,])
output2 = relay.Tuple([call_6980,call_7008,var_7007,])
func_7013 = relay.Function([var_7007,], output)
mod['func_7013'] = func_7013
mod = relay.transform.InferType()(mod)
mutated_mod['func_7013'] = func_7013
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7014 = relay.var("var_7014", dtype = "bool", shape = (882,))#candidate|7014|(882,)|var|bool
func_7013_call = mutated_mod.get_global_var('func_7013')
call_7015 = func_7013_call(var_7014)
output = call_7015
func_7016 = relay.Function([var_7014], output)
mutated_mod['func_7016'] = func_7016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_7041 = relay.TupleGetItem(func_4774_call(), 2)
call_7042 = relay.TupleGetItem(func_4776_call(), 2)
output = call_7041
output2 = call_7042
func_7044 = relay.Function([], output)
mod['func_7044'] = func_7044
mod = relay.transform.InferType()(mod)
output = func_7044()
func_7045 = relay.Function([], output)
mutated_mod['func_7045'] = func_7045
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7070 = relay.var("var_7070", dtype = "float64", shape = (3, 5, 6))#candidate|7070|(3, 5, 6)|var|float64
uop_7071 = relay.atanh(var_7070.astype('float64')) # shape=(3, 5, 6)
func_2491_call = mod.get_global_var('func_2491')
func_2495_call = mutated_mod.get_global_var('func_2495')
var_7076 = relay.var("var_7076", dtype = "int64", shape = (507,))#candidate|7076|(507,)|var|int64
call_7075 = relay.TupleGetItem(func_2491_call(relay.reshape(var_7076.astype('int64'), [13, 3, 13]), relay.reshape(var_7076.astype('int64'), [13, 3, 13]), relay.reshape(var_7076.astype('bool'), [13, 3, 13]), ), 1)
call_7077 = relay.TupleGetItem(func_2495_call(relay.reshape(var_7076.astype('int64'), [13, 3, 13]), relay.reshape(var_7076.astype('int64'), [13, 3, 13]), relay.reshape(var_7076.astype('bool'), [13, 3, 13]), ), 1)
output = relay.Tuple([uop_7071,call_7075,var_7076,])
output2 = relay.Tuple([uop_7071,call_7077,var_7076,])
func_7088 = relay.Function([var_7070,var_7076,], output)
mod['func_7088'] = func_7088
mod = relay.transform.InferType()(mod)
var_7089 = relay.var("var_7089", dtype = "float64", shape = (3, 5, 6))#candidate|7089|(3, 5, 6)|var|float64
var_7090 = relay.var("var_7090", dtype = "int64", shape = (507,))#candidate|7090|(507,)|var|int64
output = func_7088(var_7089,var_7090,)
func_7091 = relay.Function([var_7089,var_7090,], output)
mutated_mod['func_7091'] = func_7091
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7128 = relay.const([[[2.547086,-8.340273,0.087191,-7.776709,-3.271426],[9.436876,8.256380,-8.216454,0.338298,7.227833],[-5.483990,5.151394,6.933101,-8.577568,7.087704],[-8.333210,-2.207266,-6.853979,-2.159203,7.616467],[-9.307240,-4.153961,-5.195582,-7.023206,1.989540],[2.859950,2.035350,3.520498,-0.717535,-2.705329]],[[3.445265,-0.255036,3.580540,2.284959,9.263986],[-1.576405,8.596836,5.375758,3.788020,7.985230],[-4.352222,-4.624828,3.282561,-1.949974,3.904681],[5.972461,3.410814,2.831017,7.849558,-2.234735],[4.764302,-9.656503,1.637079,-7.968712,5.337227],[-2.334086,-6.155170,4.672998,-2.350387,-5.528027]],[[-8.739719,-1.991873,0.353970,2.985489,-8.983692],[-9.760164,-5.191865,-0.027260,-7.737190,9.093062],[-6.811680,8.798228,-0.015504,-9.431300,-7.116820],[8.357177,3.260102,-7.273338,1.856720,1.444841],[0.136097,5.892562,-4.516005,-7.343819,-4.059517],[-6.982830,2.250125,8.353703,-1.513004,-7.970958]],[[-8.156363,-6.263795,1.830896,3.315639,-5.710976],[-9.009423,-1.543528,4.064806,3.350489,5.371992],[1.728897,-1.596660,-7.251947,5.230371,1.400045],[0.684300,1.590804,6.124363,0.592840,5.855509],[0.402242,6.463565,4.554851,-1.181068,-8.065315],[-0.313577,4.191619,-9.159511,-3.606280,2.600091]],[[7.466945,-6.900865,-5.061287,3.362736,-2.335807],[4.134977,-1.974996,2.233997,7.744088,-1.681544],[2.056752,-6.992024,8.030536,-4.605614,-8.414333],[-1.876228,8.505514,-4.504159,-5.782963,2.928701],[-1.532408,7.917391,7.225417,-0.071704,-3.399193],[9.969975,4.815961,5.072513,-0.706407,-1.668460]],[[3.293394,2.525359,8.603431,-5.460559,5.411095],[-3.504394,-1.853795,4.014408,-2.930876,-8.238932],[-2.466443,8.201756,6.551935,1.364729,-7.578886],[-1.172475,-9.144648,-2.465136,1.846755,9.642422],[-1.028825,-6.811239,3.176093,0.550920,7.921718],[9.252004,2.892847,8.005712,6.262746,-1.129202]],[[4.157547,4.994583,-3.431066,6.098824,-3.031620],[3.614600,8.688775,3.664124,4.904418,-9.062405],[-2.860010,-6.913448,-2.954921,4.522225,-5.897420],[-8.603290,-2.725746,2.720953,2.429842,7.435559],[-4.168845,8.804271,-1.783879,-7.435467,5.953552],[2.879939,-9.347389,0.176659,5.463858,-5.973594]],[[-3.632605,5.349990,-1.241546,-8.411110,-3.712741],[6.454915,-6.154165,-4.178723,6.802577,-0.958162],[4.759034,6.587627,2.724295,0.245126,1.346576],[7.688701,-0.290291,-5.714834,7.034742,-9.820211],[-4.211631,-5.169136,-4.922184,-4.533540,-0.395723],[-3.542225,-8.190347,9.545757,-0.953836,-6.220081]],[[5.069242,-1.960550,7.839042,-5.115144,3.521490],[-0.270529,2.728098,-8.422327,9.949058,0.127629],[1.557143,4.218926,4.351527,9.479638,8.300930],[3.778775,5.384629,-1.750418,2.320581,-9.812403],[-4.186548,-6.620912,1.126801,3.776705,0.448826],[-4.959715,1.986110,-2.278568,7.728830,-6.506638]],[[-9.656721,3.530005,4.978760,-9.668310,-0.055974],[7.242006,3.914168,-8.269848,-2.592547,8.081052],[0.295600,-9.879293,1.247584,8.395120,4.174082],[-1.562477,-1.239461,5.620435,0.781740,-8.647727],[-5.558466,-3.508439,7.667621,2.416604,0.596396],[-9.449888,-2.835377,9.735647,4.552134,-5.909013]]], dtype = "float32")#candidate|7128|(10, 6, 5)|const|float32
uop_7129 = relay.tan(const_7128.astype('float32')) # shape=(10, 6, 5)
uop_7132 = relay.sin(const_7128.astype('float64')) # shape=(10, 6, 5)
uop_7141 = relay.log10(const_7128.astype('float32')) # shape=(10, 6, 5)
func_2832_call = mod.get_global_var('func_2832')
func_2835_call = mutated_mod.get_global_var('func_2835')
var_7149 = relay.var("var_7149", dtype = "int32", shape = (672,))#candidate|7149|(672,)|var|int32
call_7148 = func_2832_call(relay.reshape(var_7149.astype('int32'), [6, 8, 14]))
call_7150 = func_2832_call(relay.reshape(var_7149.astype('int32'), [6, 8, 14]))
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_7156 = relay.TupleGetItem(func_5054_call(), 0)
call_7157 = relay.TupleGetItem(func_5055_call(), 0)
output = relay.Tuple([uop_7129,uop_7132,uop_7141,call_7148,var_7149,call_7156,])
output2 = relay.Tuple([uop_7129,uop_7132,uop_7141,call_7150,var_7149,call_7157,])
func_7182 = relay.Function([var_7149,], output)
mod['func_7182'] = func_7182
mod = relay.transform.InferType()(mod)
var_7183 = relay.var("var_7183", dtype = "int32", shape = (672,))#candidate|7183|(672,)|var|int32
output = func_7182(var_7183)
func_7184 = relay.Function([var_7183], output)
mutated_mod['func_7184'] = func_7184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_7245 = relay.TupleGetItem(func_4774_call(), 2)
call_7246 = relay.TupleGetItem(func_4776_call(), 2)
uop_7272 = relay.sqrt(call_7245.astype('float64')) # shape=(882,)
uop_7274 = relay.sqrt(call_7246.astype('float64')) # shape=(882,)
output = relay.Tuple([uop_7272,])
output2 = relay.Tuple([uop_7274,])
func_7287 = relay.Function([], output)
mod['func_7287'] = func_7287
mod = relay.transform.InferType()(mod)
output = func_7287()
func_7288 = relay.Function([], output)
mutated_mod['func_7288'] = func_7288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6436_call = mod.get_global_var('func_6436')
func_6438_call = mutated_mod.get_global_var('func_6438')
call_7335 = relay.TupleGetItem(func_6436_call(), 0)
call_7336 = relay.TupleGetItem(func_6438_call(), 0)
func_6407_call = mod.get_global_var('func_6407')
func_6408_call = mutated_mod.get_global_var('func_6408')
call_7337 = relay.TupleGetItem(func_6407_call(), 0)
call_7338 = relay.TupleGetItem(func_6408_call(), 0)
func_6158_call = mod.get_global_var('func_6158')
func_6159_call = mutated_mod.get_global_var('func_6159')
call_7339 = relay.TupleGetItem(func_6158_call(), 2)
call_7340 = relay.TupleGetItem(func_6159_call(), 2)
func_6704_call = mod.get_global_var('func_6704')
func_6706_call = mutated_mod.get_global_var('func_6706')
call_7349 = relay.TupleGetItem(func_6704_call(), 0)
call_7350 = relay.TupleGetItem(func_6706_call(), 0)
func_2596_call = mod.get_global_var('func_2596')
func_2600_call = mutated_mod.get_global_var('func_2600')
var_7358 = relay.var("var_7358", dtype = "float64", shape = (336, 2))#candidate|7358|(336, 2)|var|float64
call_7357 = func_2596_call(relay.reshape(var_7358.astype('float64'), [7, 12, 8]), relay.reshape(var_7358.astype('float64'), [7, 12, 8]), )
call_7359 = func_2596_call(relay.reshape(var_7358.astype('float64'), [7, 12, 8]), relay.reshape(var_7358.astype('float64'), [7, 12, 8]), )
output = relay.Tuple([call_7335,call_7337,call_7339,call_7349,call_7357,var_7358,])
output2 = relay.Tuple([call_7336,call_7338,call_7340,call_7350,call_7359,var_7358,])
func_7364 = relay.Function([var_7358,], output)
mod['func_7364'] = func_7364
mod = relay.transform.InferType()(mod)
mutated_mod['func_7364'] = func_7364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7365 = relay.var("var_7365", dtype = "float64", shape = (336, 2))#candidate|7365|(336, 2)|var|float64
func_7364_call = mutated_mod.get_global_var('func_7364')
call_7366 = func_7364_call(var_7365)
output = call_7366
func_7367 = relay.Function([var_7365], output)
mutated_mod['func_7367'] = func_7367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6704_call = mod.get_global_var('func_6704')
func_6706_call = mutated_mod.get_global_var('func_6706')
call_7451 = relay.TupleGetItem(func_6704_call(), 0)
call_7452 = relay.TupleGetItem(func_6706_call(), 0)
output = call_7451
output2 = call_7452
func_7475 = relay.Function([], output)
mod['func_7475'] = func_7475
mod = relay.transform.InferType()(mod)
mutated_mod['func_7475'] = func_7475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7475_call = mutated_mod.get_global_var('func_7475')
call_7476 = func_7475_call()
output = call_7476
func_7477 = relay.Function([], output)
mutated_mod['func_7477'] = func_7477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5524_call = mod.get_global_var('func_5524')
func_5526_call = mutated_mod.get_global_var('func_5526')
call_7489 = relay.TupleGetItem(func_5524_call(), 0)
call_7490 = relay.TupleGetItem(func_5526_call(), 0)
output = call_7489
output2 = call_7490
func_7496 = relay.Function([], output)
mod['func_7496'] = func_7496
mod = relay.transform.InferType()(mod)
mutated_mod['func_7496'] = func_7496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7496_call = mutated_mod.get_global_var('func_7496')
call_7497 = func_7496_call()
output = call_7497
func_7498 = relay.Function([], output)
mutated_mod['func_7498'] = func_7498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_7507 = relay.TupleGetItem(func_4774_call(), 1)
call_7508 = relay.TupleGetItem(func_4776_call(), 1)
output = call_7507
output2 = call_7508
func_7518 = relay.Function([], output)
mod['func_7518'] = func_7518
mod = relay.transform.InferType()(mod)
output = func_7518()
func_7519 = relay.Function([], output)
mutated_mod['func_7519'] = func_7519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7496_call = mod.get_global_var('func_7496')
func_7498_call = mutated_mod.get_global_var('func_7498')
call_7565 = func_7496_call()
call_7566 = func_7496_call()
uop_7569 = relay.erf(call_7565.astype('float32')) # shape=(11, 12, 4)
uop_7571 = relay.erf(call_7566.astype('float32')) # shape=(11, 12, 4)
func_3675_call = mod.get_global_var('func_3675')
func_3677_call = mutated_mod.get_global_var('func_3677')
const_7574 = relay.const([7.695379,-9.657379,-1.012657,-2.641690,-8.681349,-2.555518,7.462332,-3.885637,-8.472600,0.189009,-4.938319,-2.983838,-3.530583,-1.629764,5.198382,2.336948,-7.897144,-2.735510,-3.897839,-0.012934,2.171645,-2.584356,4.529988,-1.613938,-7.560308,-5.790991,1.946534,6.611330,-7.340679,6.698430,-9.520861,-5.021574,-6.739437,-7.887226,-8.141912,9.700860,5.439752,-4.927507,7.107686,-8.015457,-6.790183,-0.687232,-6.523883,-0.182633,-9.111663,-9.956889,-0.651459,1.913399,6.088737,-1.239645,-6.963362,6.562151,4.543062,-3.443359,-5.250689,-5.691067,5.344637,-8.850351,-3.170105,5.047040,1.711031,5.301926,-2.921334,-5.026857,-4.894790,3.511272,7.196883,-6.462273,-7.054166,4.849286,-1.198659,-1.488338,-3.569176,4.700622,7.551402,5.364726,-4.428994,-0.259202,5.431446,8.951473,9.407644,9.391810,5.522830,5.773777,-4.217356,1.888531,-3.980709,9.078304,-1.796468,6.284307,6.732962,-3.678296,-4.446635,-1.625142,-2.200464,1.543289,3.007069,-7.042717,3.953231,-6.839502,-2.061906,-7.114251,6.010072,3.492562,-9.757506,6.166269,-3.697212,1.081181,5.407680,-9.939793,2.745237,0.806852,-3.585434,-3.729518,-2.027464,-3.806434,-5.511151,6.527597,-6.431873,7.519810,-0.092752,-1.047811,9.890160,7.100942,0.389417,-0.687995,8.075871,8.799836,2.812171,2.512377,5.329106,-3.436018,-6.617547,8.162765,-8.298629,2.816878,-0.739614,0.602393,-9.735342,-6.832144,6.159254,-3.670097,-3.046658,-3.416442,9.328711,6.965996,8.481742,-8.125239,-6.415027,-3.021564,5.326777,5.951232,1.703788,0.453720,5.347775,-8.621072,-6.766425,8.044550,-3.252183,-6.072650,-1.881698,-7.108980,5.810861,5.651530,5.419467,-5.280305,-3.366927,-1.005759,2.229592,8.243225,4.062556,8.238544,-2.431067,-8.362068,-7.429250,4.495477,6.871955,4.611192,-4.270093,-3.946448,-6.005365,-8.332446,-7.113337,5.313596,-7.923781,-3.576597,-3.988326,3.370378,-2.427943,3.726354,-9.792275,5.147986,4.814148,-0.612466,-1.281136,0.851934,-6.122889,2.023056,-7.390542,-1.694870,8.758997,-1.695052,-9.900637,-9.891122,5.880606,8.572759,-2.515059,1.884889,4.715532,-3.949506,-4.250029,6.606237,2.953005,7.282208,4.826084,3.404922,-2.008969,-1.497115,6.551174,-6.324774,-7.235219,3.205970,-0.111441,-5.155008,-9.655260,5.322070,-1.797329,8.638881,3.045015,1.526281,-1.387734,2.196466,-7.654150,7.204244,6.067194,3.711660,-5.457469,-2.754284,8.577038,-0.242425,0.266057,6.363416,-7.927275,-4.550447,5.745611,-5.394501,-0.621610,4.185709,5.599102,-0.612950,-8.299305,7.393226,-9.362934,4.020358,-1.838407,-2.418000,-1.568757,-8.265056,-3.936027,-3.813663,-6.740177,-5.386381,3.508646,-4.913089,-0.829393,5.463781,-8.290552,9.886069,-8.419459,-3.820983,1.645926,2.739032,-4.986663,-5.896501,-9.180639,4.303402,-3.847351,5.876476,1.968640,-6.834767,-1.231113,-4.293702,-8.368640,-1.143242,-8.029880,-3.542844,3.600784,7.645328,7.221626,-4.178894,1.290934,-2.574144,3.490911,7.300151,2.539155,7.271885,4.979108,-5.091773,3.035978,-3.898316,-5.518539,7.710927,-1.685428,4.385545,4.815101,0.592634,0.196330,-8.595357,6.063655,9.507540,0.243070,7.626471,-5.889987,9.726628,-1.014758,-3.067743,-5.365039,-2.639949,-6.842996,-4.038040,2.099953,-5.110148,6.909695,-6.497484,-3.679316,-9.630868,-7.161712,-2.043694,8.686871,-7.132777,-7.777762,-7.630305,0.404063,2.842124,0.897420,8.357249,-9.335204,8.923005,-4.550360,-7.708302,-9.694989,-0.099459,-5.451215,5.302720,-6.397240,3.760832,-9.932566,9.377428,-3.352743,-4.534257,-4.187696,4.023375,4.578825,2.232415,-4.261710,0.710222,-3.555599,4.214949,-8.818646,-3.714642,-3.058642,6.912136,-1.582157,-3.796580,-1.898262,-0.527362,-6.448018,1.862682,-7.405499,8.578208,-3.211480,0.228112,3.562077,-8.597909,-5.031194,-9.380513,-3.228786,5.209780,4.607757,-1.285146,-7.031189,-3.209439,-0.428048,9.315353,-8.926964,6.752242,2.568535,1.924425,1.363660,-6.275814,5.122030,-5.121308,4.598689,-2.405320,-4.102749,-7.593052,5.352291,2.248197,-5.755172,-2.325431,-5.442847,5.243762,2.527367,-9.634686,-4.164117,-9.084025,9.560055,-3.092194,-6.092841,0.492874,9.922346,-4.455923,5.139685,-3.069813,-9.063487,-3.527640,-3.763438,-3.046417,3.335355,-3.557490,2.762578,1.207233,1.833503,4.312746,-3.344290,-9.100019,-2.464665,-5.648643,7.095061,1.772165,8.474660,-1.426129,-5.365242,0.629518,0.726008,3.559959,-0.263803,5.093951,-2.115867,-5.789543,-0.566336,-1.771661,0.141706,-6.469983,1.685909,-4.246147,4.434109,-5.880613,4.212240,3.622096,1.393672,5.458596,5.808957,-7.437677,-8.448045,-4.813326,5.034734,8.397555,8.022892,1.217441,-3.115733,-0.818954,-0.468667,7.340617,-9.079555,-4.417728,5.518312,-0.258737,6.287129,4.592759,2.459841,-0.389492,-5.571151,0.158948,6.649944,6.438825,-8.059719,7.198375,-8.746818,-7.942045,-9.025310,5.550813,-3.690898,-9.708233,-9.466119,7.347949,-1.800091,-6.783163,-1.182154,-2.758332,6.179626,1.873716,3.578351,-1.089517,1.824970,2.664234,-9.183169,2.894126,-8.121543,-2.836518,5.780057,-6.478451,3.491862,2.775575,-6.005702,8.059611,8.285223,7.235446,4.973552,-3.335249,-1.055972,-2.859902,-8.016170,5.856354,-3.530647,8.756634,-5.298927,9.206414,2.642411,6.456952,-7.734349,7.458472,3.634183,9.761881,-1.883743,4.813023,6.422449,3.029615,7.788428,-1.308214,-2.811557,-3.065060,7.039896,-5.025256,-6.967972,-1.593109,-2.043356,-7.123548,-4.057253,8.510152,0.833249,3.877068,-5.256955,0.826903,3.719483,6.885457,3.271662,-9.491908,3.595697,4.976196,-4.312162,5.542729,4.011851,-5.700581,8.183918,3.559780,-5.038733,2.958051,1.697815,1.143703,-0.210831,5.128938,-9.518380,-7.588929,-0.627227,7.660821,8.598639,-3.901735,-3.929694,-6.723447,-9.833364,-7.226946,-0.888029,3.895612,-3.635198,-9.071627,-1.470396,4.679404,-6.717430,-2.496531,5.700617,7.213256,-9.392595,-0.995507,0.049618,-1.208806,-7.078661,-6.582043,-3.456944,-6.121723,-0.268224,4.862841,-8.659370,8.139263,-8.160630,-1.667125,6.324365,-9.416455,8.463859,-5.969234,1.088919,-4.737872,-8.497504,-3.047453,-9.478434,3.386302,-9.698821,5.461172,8.573171,7.192909,9.936056,-6.462047,8.971248,-2.212554,2.497525,3.947181,-6.000793,-0.719872,5.097277,6.891836,2.438693,-8.823971,-6.760428,4.254441,8.917118,8.404545,-5.646424,2.904544,2.983252,-0.322862,8.139870,6.759236,6.743492,-2.383272,1.841795,-1.186579,-5.694685,-0.163000,7.473067,6.074475,-4.133894,9.186908,-3.418435,-9.800863,-5.107665,-9.400345,6.928462,9.993095,2.184194,2.108353,-7.646270,1.232141,-9.126672,3.717126,4.121452,-3.981968,9.388565,-9.887642,3.536647,6.754810,0.706866,7.001890,-2.273763,7.133204,-0.836034,-7.373461,5.469256,0.094200,1.221730,3.407123,8.820976,-5.547756,7.174253,-8.869441,2.809809,-7.522783,6.582021,3.349726,4.650683,4.159597,0.492738,-8.037906,-2.997138,9.826872,-9.344185,-3.925510,-7.394052,-1.973082,-3.499323,-0.421077,2.948441,-5.486212,-1.063513,-5.583764,7.082345,0.739329,2.844911,1.063100,-4.514079,5.784990,1.073286,-7.346034,-5.204436,6.494520,-8.843424,-4.927890,-9.486747,-3.275125,6.448798,-8.593266,6.680222,1.945369,3.132469,-0.455084,4.630012,-1.371678,1.822837,2.463338,-3.102270,-1.986240,-8.278208,-5.173716,-5.499543,-6.026682,8.505518,-6.408756,-4.932068,2.462591,-7.087311,6.693031,5.934778,-7.086166,9.537426,-3.819791,-0.811630,-3.767982,1.766221,1.775681,8.727369,8.530158,6.237214,0.392856,-8.752840,0.332499,-5.103610,-6.198021,5.930478,1.023884,-0.671954,-5.374467,-3.753728,-2.211946,8.178708,7.193006,9.376750,0.084702,-9.417115,-4.735562,7.447669,8.830908,2.237978,8.774470,-0.585667,2.896489,-6.172145,8.751795,-7.296646,-5.507554], dtype = "float64")#candidate|7574|(768,)|const|float64
call_7573 = relay.TupleGetItem(func_3675_call(relay.reshape(const_7574.astype('float64'), [8, 8, 12])), 0)
call_7575 = relay.TupleGetItem(func_3677_call(relay.reshape(const_7574.astype('float64'), [8, 8, 12])), 0)
func_6704_call = mod.get_global_var('func_6704')
func_6706_call = mutated_mod.get_global_var('func_6706')
call_7576 = relay.TupleGetItem(func_6704_call(), 0)
call_7577 = relay.TupleGetItem(func_6706_call(), 0)
func_7182_call = mod.get_global_var('func_7182')
func_7184_call = mutated_mod.get_global_var('func_7184')
var_7583 = relay.var("var_7583", dtype = "int32", shape = (672,))#candidate|7583|(672,)|var|int32
call_7582 = relay.TupleGetItem(func_7182_call(relay.reshape(var_7583.astype('int32'), [672,])), 2)
call_7584 = relay.TupleGetItem(func_7184_call(relay.reshape(var_7583.astype('int32'), [672,])), 2)
uop_7589 = relay.acos(uop_7569.astype('float32')) # shape=(11, 12, 4)
uop_7591 = relay.acos(uop_7571.astype('float32')) # shape=(11, 12, 4)
output = relay.Tuple([call_7573,const_7574,call_7576,call_7582,var_7583,uop_7589,])
output2 = relay.Tuple([call_7575,const_7574,call_7577,call_7584,var_7583,uop_7591,])
func_7592 = relay.Function([var_7583,], output)
mod['func_7592'] = func_7592
mod = relay.transform.InferType()(mod)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7593 = relay.var("var_7593", dtype = "int32", shape = (672,))#candidate|7593|(672,)|var|int32
func_7592_call = mutated_mod.get_global_var('func_7592')
call_7594 = func_7592_call(var_7593)
output = call_7594
func_7595 = relay.Function([var_7593], output)
mutated_mod['func_7595'] = func_7595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5273_call = mod.get_global_var('func_5273')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_7600 = relay.TupleGetItem(func_5273_call(), 0)
call_7601 = relay.TupleGetItem(func_5274_call(), 0)
output = relay.Tuple([call_7600,])
output2 = relay.Tuple([call_7601,])
func_7606 = relay.Function([], output)
mod['func_7606'] = func_7606
mod = relay.transform.InferType()(mod)
mutated_mod['func_7606'] = func_7606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7606_call = mutated_mod.get_global_var('func_7606')
call_7607 = func_7606_call()
output = call_7607
func_7608 = relay.Function([], output)
mutated_mod['func_7608'] = func_7608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5861_call = mod.get_global_var('func_5861')
func_5862_call = mutated_mod.get_global_var('func_5862')
call_7619 = relay.TupleGetItem(func_5861_call(), 0)
call_7620 = relay.TupleGetItem(func_5862_call(), 0)
var_7628 = relay.var("var_7628", dtype = "float32", shape = (11, 12, 4))#candidate|7628|(11, 12, 4)|var|float32
bop_7629 = relay.less(call_7619.astype('bool'), relay.reshape(var_7628.astype('bool'), relay.shape_of(call_7619))) # shape=(11, 12, 4)
bop_7632 = relay.less(call_7620.astype('bool'), relay.reshape(var_7628.astype('bool'), relay.shape_of(call_7620))) # shape=(11, 12, 4)
func_7606_call = mod.get_global_var('func_7606')
func_7608_call = mutated_mod.get_global_var('func_7608')
call_7634 = relay.TupleGetItem(func_7606_call(), 0)
call_7635 = relay.TupleGetItem(func_7608_call(), 0)
func_5566_call = mod.get_global_var('func_5566')
func_5571_call = mutated_mod.get_global_var('func_5571')
const_7655 = relay.const([1.755211,-4.749558,-1.293164,-6.243665,7.175580,9.968476,2.617794,-8.614432,7.021668,-3.281259,0.213918,6.019567,-4.984441], dtype = "float64")#candidate|7655|(13,)|const|float64
const_7656 = relay.const([4.189215,-0.561454,-4.284141,5.540926,1.144458,8.564170,-7.748704,-6.140813,-1.857541,0.707971,5.025892,8.370346,-3.754007,-6.544341,4.555604,9.692754,-8.675262,-3.703631,-1.657400,-5.315393,-0.415547,-9.661027,-2.052680,-9.631309,0.260324,9.079201,-2.811900,1.057026,-2.529198,8.784945,9.761484,-7.427365,-4.180008,-4.855187,-6.295203,3.725513,-8.369537,-7.775037,-8.908215,4.079619,-0.731584,-1.808692,6.647792,5.733846,6.825722,0.423881,0.080342,-3.466200,8.656290,-7.245121,4.335509,-5.107561,-2.370510,-8.217225,2.431008,-7.498718,8.818946,0.470335,-8.108427,-1.983910,8.931926,4.705572,-9.322609,-5.943076,-6.024965,7.288064,-1.346070,-0.195856,-4.016907,9.251290,-1.320467,-9.862139,-2.445102,0.906083,-5.395162,-1.060157,4.339222,2.789632,-9.159687,0.977019,-7.213320,-5.704163,6.468805,4.002212,-6.743562,7.954596,-6.950258,-0.400576,0.301647,-7.161989,1.154978,8.222530,-4.055791,-7.232881,7.549718,6.053297,8.414103,-4.090707,-4.463308,-4.979815,1.304821,-9.266701,8.850002,-6.675939,-4.622761,5.826821,-5.493892,-6.851183,2.494469,2.906778,4.114963,-4.155924,-6.552541,9.115346,0.724841,7.156670,8.776845,-8.078428,-3.410362,-0.201411,2.115799,7.293291,-5.809801,-3.394532,-3.947948,-4.244182,2.592431,-7.399790,-5.723222,-6.431296,-6.016336,-5.609087,3.813893,-9.312029,0.162193,-3.146379,-0.621356,-9.871818,-0.770238,-0.620424,-6.410625,-9.831508,-4.029579,-6.385126,-8.407149,-2.671363,-8.454077,-5.185649,3.936441,-6.290786,1.334356,-1.191716,-1.742550,0.983881,3.718902,4.386245,-1.408671,5.353693,0.371667,2.903554,7.926635,-6.743584,-6.754185,7.584104,0.307118,7.330360,1.498089,1.912028,-1.505831,-5.115276,-2.183541,-1.605330,0.957458,3.891342,6.055194,-0.846428,-1.577670,-2.952090,5.516174,1.720286,4.098279,-6.889162,-8.114715,-0.518849,-0.126353,-5.686718,4.165698,3.652065,8.506042,2.727917,-6.282486,6.608901,-9.472469,3.092019,9.690248,-7.425840,8.944240,3.313858,-9.565632,8.310921,-2.492325,-6.535229,-3.038893,-0.765971,-9.067680,-8.146290,3.797911,-8.309008,0.745177,-8.961950,-3.717597,-5.722383,7.983129,6.921832,1.958377,-1.562683,-6.318040,5.426504,-5.769080,-8.382202,0.773273,2.615081,-9.847951,-7.391325,-8.257922,5.099398,-6.661871,-9.452328,0.177050,7.091315,-5.754590,0.476973,-9.841468,8.376514,-2.491378,-3.872265,-2.386962,9.276628,1.135384,5.249537,-9.885302,-5.926336,-1.225413,-0.382850,-4.675289,-5.422015,6.328193,8.521030,6.428680,-4.706986,0.568556,6.938088,0.689838,-5.620340,9.543195,-8.576799,-1.447847,-7.332722,6.821386,0.925686,-3.026295,3.884256,3.204103,-6.011608,2.441405,-9.723817,7.667491,0.816218,-5.052777,0.706711,2.106616,4.618983,-5.826341,-2.283800,-3.217614,8.890179,2.754977,-5.552175,3.173003,5.171254,-9.882215,9.192235,-4.496124,-5.758707,9.711819,-3.397216,9.632306,-6.064331,2.092345,2.152350,-4.482096,-6.007314,7.216502,-9.461351,9.424071,-3.489710,-6.147343,1.803851,-5.203924,2.883668,6.455312,-4.575730,-5.140688,-3.810799,5.038195,8.142975,-7.192174,5.516795,7.364825,7.555394,-8.029043,-9.136205,6.679342,7.292945,1.365110,6.756770,-7.543870,4.434362,4.721877,-2.714857,3.356957,-8.271765,5.113650,-4.259812,-9.207961,-2.957534,9.023263,5.780046,-6.082545,-6.945637,2.616651,4.474425,0.472262,-1.529103,-6.356367,9.303845,9.445899,-1.344168,5.263516,9.975231,-9.754431,-2.973673,-4.582426,-5.399454,-7.992548,-4.268390,8.324264,5.972481,-9.999710,4.239264,-0.323286,-3.514126,-9.610932,3.880016,1.241286,7.210006,-5.051307,7.556193,6.531801,7.904615,-3.034672,-9.501552,3.150866,-5.915136,2.559250,7.367052,-6.966608,3.864855,-0.039321,6.165718,4.700286,3.566579,-4.477926,-8.935575,-1.543892,-0.255845,8.839333,-7.440926,-5.071320,-9.124714,-2.868628,-9.704804,-8.667628,-9.810523,-9.253377,-8.066843,-3.248339,0.949700,8.339606,9.070610,5.884543,-6.928567,-4.526470,-2.679536,-3.241221,-1.938123,-2.348938,1.705517,6.721409,0.391200,0.389305,8.622313,3.081669,5.895249,0.073616,-8.816793,-3.664715,4.329190,-0.322314,3.277613,8.582682,6.336480,-3.087854,-0.904766,-3.270854,2.421115,1.941238,-2.819305,5.644560,4.963302,-7.680626,-6.128860,9.634744,7.766974,9.159252,-0.181611,-7.013749,-9.308507,-9.408266,-8.309845,-4.394345,6.903445,9.208294,-4.099230,0.976541,4.216956,0.311158,-4.152111,7.534319,-5.032525,-7.671600,6.094869,9.386218,-6.862448,-1.137570,-1.737194,-4.701038,2.315682,5.927753,3.957597,2.891853,-3.833440,-2.120747,7.004607,-8.467545,-8.962364,-9.667949,-5.817117,9.787800,-2.198724,2.853209,-5.962846,-1.840209,2.999598,1.211713,-8.569497,1.683874,4.133532,0.871033,-2.573503,8.471670,-7.391636,-8.945302,5.799214,9.133156,-9.389902,-6.591684,9.574753,-7.867462,1.340831,2.217696,-3.337881,-0.509201,-5.205757,4.061196,-5.197697,6.315827,-1.159316,2.991262,6.638661,7.399035,3.688961,-3.066663,-6.784639,-8.463652,-9.431727,6.987495,-9.163572,-8.035699,2.205331,4.683733,-4.000878,3.819097,1.325233,-7.465441,6.455954,-7.485505,-5.754241,4.077286,4.979953,-2.773118,6.849596,-0.453278,3.779344,-1.983017,-2.334290,-2.474418,-4.497902,-4.031353,-3.476314,-1.010677,-5.503533,4.516950,3.673520,-2.005116,-2.097761,-5.412107,-7.519827,2.782226,-9.359117,7.724979,-8.954776,0.547692,5.251365,-3.299447,5.399341,5.526232,2.086660,-5.023717,-4.081739,0.141806,0.636470,-4.275087,-5.147870,2.787469,-8.029056,-7.515088,5.056449,5.966567,8.976429,-2.567711,2.861537,-4.073192,-5.202076,7.381603,0.364802,4.219736,6.783918,4.824452,-3.002264,-0.645100,1.395032,4.835161,-9.451433,6.851812,-2.525861,-2.789700,4.788070,-9.774777,5.223407,-4.952080,-8.529221,4.041400,-3.902156,0.721931,-2.599416,3.833628,-6.187203,-3.464845,0.931536,-1.939816,6.146048,7.288112,-6.981025,3.873770,-9.569410,-1.403687,1.113738,-7.719936,-2.035992,-2.812382,8.389999,-0.667850,-3.246714,-5.635797,-8.299440,2.793874,-4.599614,2.302750,-9.730435,-6.216575,-9.941485,4.196154,8.367409,7.680815,-5.658416,-8.401995,1.001811,7.609842,4.421637,-2.847724,7.560705,9.682035,-9.591631,-6.893961,5.658999,8.096620,1.816984,-6.415197,-3.938602,6.468850,1.515524,-3.395013,-2.273843,9.784373,-4.416950,-5.955915,8.751668,7.626312,-4.612923,3.679799,-4.288913,8.298702,4.001772,-3.960699,-9.820038,-3.884263,1.543120,-8.175649,3.000830,9.303202,3.498903,6.074268,-0.089492,0.311769,-6.130790,-8.598396,1.728547,-7.378226,3.298288,3.896730,-1.781318,-6.299971,-7.060507,-7.443125,-9.245957,2.903965,7.125261,-7.687358,1.731827,-8.111487,-7.533005,7.798878,-0.054611,3.813202,-0.174524,3.775904,-0.316026,8.722940,7.042644,-9.306110,6.036252,9.077636,-4.222114,-9.537338,0.190608,3.184820,-0.342729,-7.691383,8.819694,-4.436873,-1.668948,-1.861987,5.180582,0.295753,5.957234,-5.469763,-6.433003,6.399758,-3.962088,-3.307043,-0.907841,9.196977,-6.242155,-4.459331,8.514807,-3.316157,-3.995487,4.760247,-1.562921,-8.509936,-0.576620,-8.465720,1.097823,-0.496315,-8.011089,0.659589,-0.403615,5.741487,-5.837317,-2.847432,-7.797358,1.182390,-2.505906,5.544889,-0.806840,-9.598462,-8.002763,8.403238,8.130243,5.393194,-6.644508,-4.648933,-9.684733,-9.663779,6.108322,-4.806592,6.377922], dtype = "float64")#candidate|7656|(728,)|const|float64
call_7654 = relay.TupleGetItem(func_5566_call(relay.reshape(const_7655.astype('float64'), [1, 1, 13]), relay.reshape(const_7656.astype('float64'), [728,]), relay.reshape(call_7634.astype('bool'), [882,]), ), 1)
call_7657 = relay.TupleGetItem(func_5571_call(relay.reshape(const_7655.astype('float64'), [1, 1, 13]), relay.reshape(const_7656.astype('float64'), [728,]), relay.reshape(call_7634.astype('bool'), [882,]), ), 1)
output = relay.Tuple([bop_7629,call_7634,call_7654,const_7655,const_7656,])
output2 = relay.Tuple([bop_7632,call_7635,call_7657,const_7655,const_7656,])
func_7660 = relay.Function([var_7628,], output)
mod['func_7660'] = func_7660
mod = relay.transform.InferType()(mod)
var_7661 = relay.var("var_7661", dtype = "float32", shape = (11, 12, 4))#candidate|7661|(11, 12, 4)|var|float32
output = func_7660(var_7661)
func_7662 = relay.Function([var_7661], output)
mutated_mod['func_7662'] = func_7662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5273_call = mod.get_global_var('func_5273')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_7899 = relay.TupleGetItem(func_5273_call(), 0)
call_7900 = relay.TupleGetItem(func_5274_call(), 0)
output = relay.Tuple([call_7899,])
output2 = relay.Tuple([call_7900,])
func_7906 = relay.Function([], output)
mod['func_7906'] = func_7906
mod = relay.transform.InferType()(mod)
mutated_mod['func_7906'] = func_7906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7906_call = mutated_mod.get_global_var('func_7906')
call_7907 = func_7906_call()
output = call_7907
func_7908 = relay.Function([], output)
mutated_mod['func_7908'] = func_7908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7906_call = mod.get_global_var('func_7906')
func_7908_call = mutated_mod.get_global_var('func_7908')
call_7961 = relay.TupleGetItem(func_7906_call(), 0)
call_7962 = relay.TupleGetItem(func_7908_call(), 0)
func_1137_call = mod.get_global_var('func_1137')
func_1139_call = mutated_mod.get_global_var('func_1139')
const_8005 = relay.const([-4.327332,2.325727,-0.747652,-6.897882,4.107042,-6.778811,-9.317545,6.333671,-5.197861,5.690727,5.142126,4.811318,6.351620,-8.276321,-3.967002,-6.789954,8.991877,-4.478747,-3.638037,-7.728382,3.402000,6.730144,0.822654,-9.823549,0.196713,-1.396455,4.321547,8.924663,-3.596239,1.257906,-7.212767,5.534146,7.925601,6.226162,1.668754,7.930714,5.380423,-9.909019,-9.483693,-5.907190,-4.694657,-9.761558,-8.812186,-0.716886,8.688008,5.759780,6.184604,2.992104,-1.066103,0.406905,-7.778204,-5.010728,2.739193,-0.314086,-5.562168,8.319716,1.158068,-5.155465,0.898297,3.382814,-0.869392,-1.482988,0.587681,1.993207,6.128790,5.234264,9.753772,1.691652,-1.583547,-5.850187,-3.298937,2.602407,-0.930762,9.518147,-9.404538,-3.074041,5.989200,1.279951,8.230098,6.885162,5.173045,-2.348408,-8.051613,9.586994,-6.327086,8.878553,6.221000,-6.057219,-4.329739,7.847628,-2.969172,-0.814326,9.942549,5.705266,-4.116798,6.246822,8.695169,-7.137064,2.466492,2.913531,-0.047106,-0.653660,9.353627,2.612764,-0.593765,7.791632,-4.288961,-2.408088,3.608595,-2.747233,-0.438077,2.960503,-9.878904,-7.413419,3.519977,7.858243,-2.518463,3.598966,-0.331544,-3.530486,3.406653,-7.227411,0.948524,9.578995,-2.615007,-3.417648,0.953229,-3.689363,4.268543,4.583217,-8.402220,-3.311408,-3.360814,1.365132,-4.000159,9.495473,4.438714,-5.385831,3.536092,7.039986,8.348821,-9.828901,6.806646,-9.100992,9.353179,8.250431,-0.665116,9.522585,6.549815,-0.242553,-2.492245,2.174454,4.987543,-0.315094,-9.574141,-6.478670,9.499031,-9.349422,7.099333,8.944968,6.018956,3.080193,4.028196,-4.055401,4.152176,-9.756794,7.274117,9.687931,0.946141,4.673710,1.901391,-4.234819,-5.730971,7.945173,6.241076,0.371808,1.560287,1.978335,9.031819,8.732588,-3.289265,-7.251579,0.852505,-7.596204,5.546685,-0.873417,2.465036,2.092529,-3.462844,6.863162,4.755542,-5.678947,8.706008,3.544073,0.781490,0.274258,7.266164,0.331150,3.251223,9.277365,1.085984,8.108263,-0.891910,5.704231,2.679447,0.485022,7.229009,8.668211,4.511819,7.899864,0.256363,-9.669651,-1.749624,-5.091582,5.983822,-2.268841,4.308857,5.574174,-7.607032,-5.568388], dtype = "float64")#candidate|8005|(220,)|const|float64
call_8004 = relay.TupleGetItem(func_1137_call(relay.reshape(const_8005.astype('float64'), [4, 5, 11])), 0)
call_8006 = relay.TupleGetItem(func_1139_call(relay.reshape(const_8005.astype('float64'), [4, 5, 11])), 0)
func_3486_call = mod.get_global_var('func_3486')
func_3489_call = mutated_mod.get_global_var('func_3489')
const_8018 = relay.const([0.867136,-6.493423,9.154146,1.388115,5.532544,-4.157512,3.474166,8.938339,-0.105827,-0.562911,6.940852,7.715544,9.965609,7.112102,-0.158342,8.362450,1.855316,-6.928863,0.889239,4.876113,4.806665,-4.509635,-4.062890,2.708802,-5.542694,5.944168,5.717715,-3.616798,8.611907,9.199963,-7.852780,7.118267,-4.093172,-8.665117,1.557542,4.285013,-7.936025,2.683532,2.297303,1.738699,5.329543,6.973454,6.166488,3.123504,-6.727117,-8.376525,7.304373,-1.883156,-0.204419,-2.979302,-5.973998,-9.940457,7.416688,1.733403,-9.608505,6.261363,2.449589,6.699663,-7.150935,9.013649,0.660425,2.336955,-3.553924,9.740287,-0.466621,-0.394869,6.317743,5.927332,6.340311,6.618373,-3.734543,2.012907,5.952612,-7.326651,7.848281,-7.103369,-8.144610,1.738364,3.398048,5.159931,-2.970763,4.844188,-2.174008,8.147774,4.649912,4.179998,1.541859,-9.851048,6.595286,-0.042115,-5.540168,-8.360429,-1.575721,7.783490,-2.856788,6.925259,7.089489,-6.973807,-1.743218,5.349404,-2.725763,1.228865,5.982040,-2.993844,-3.750867,3.276553,-9.741375,6.772838,7.998317,-7.973491,0.722099,6.688647,-2.052041,-6.013775,3.142076,0.979209,4.581688,6.119642,-9.662347,0.404244,-9.203033,1.351573,-2.122063,3.612313,-8.239879,0.579395,6.690853,-2.695458,-2.977949,-0.820974,-5.331805,3.298608,-4.401602,-6.747431,5.890154,-6.477031,-0.113050,-8.915516,-1.680504,-8.608112,3.836022,5.903652,-3.581321,1.319213,-7.140704,-1.794474,2.240827,-0.504276,-2.248468,-2.178326,9.647352,7.494343,-2.669202,-7.660552,9.813970,4.579325,4.013901,-2.172973,-9.410996,-2.419026,7.762868,1.379331,8.350788,4.129077,-8.611344,0.039628,-1.912225,5.169536,-5.249994,9.725601,7.896693,-3.751667,1.750396,-1.817031,-5.360291,6.036283,-7.425214,-9.767475,-3.000085,6.960188,2.749305,-6.284569,-6.679040,4.577017,-4.937958,-6.636335,8.381897,-4.255293,7.684165,2.354115,7.895289,-4.703416,0.981152,1.463035,-8.202895,3.253971,0.316640,6.668314,2.122480,-9.226150,2.350904,0.942240,-5.404397,-6.703185,6.713001,1.269026,-1.326231,-5.205839,4.077147,4.309338,-4.305723,4.008543,5.071416,0.328764,3.988820,-3.432828,7.320593,-9.253961,8.502774,7.890640,-3.350513,7.503695,-3.733629,-7.384664,-9.467603,8.198889,-9.634695,-1.471414,4.427396,4.727255,-7.394772,-1.392690,8.240401,3.312264,4.266080,9.601658,4.734142,-1.929776,-2.668456,3.627386,-9.149459,-3.822091,-5.586774,-8.995832,-8.187244,-2.420399,0.831305,-0.524865,7.365082,1.278827,3.712761,-7.820442,-9.318033,-0.481232,-0.626638,0.751943,8.564335,2.106226,-0.861964,1.190470,2.314049,1.050047,-4.019604,-2.037108,1.919006,-2.835951,-2.710702,-3.044739,3.835900,-1.110535,-4.932533,7.195609,9.538884,3.788664,-5.006377,-5.504171,2.361457,9.402064,-8.226579,0.612908,0.892401,-9.568618,3.495889,-8.737160,7.694201,-0.207604,-4.495918,6.621938,-2.751756,-3.050623,-9.344682,8.271941,-3.909617,4.320853,-2.052184,2.555861,8.964480,2.359437,-0.416463,3.408159,-8.795635,1.420105,4.551624,-6.333709,-9.398386,9.130930,-7.442190,-0.911120,1.983543,8.492607,-9.540584,3.105482,-7.791412,-6.939700,5.504706,-3.464243,2.190022,-2.596449,5.432215,0.450160,4.969024,-1.984121,6.039498,1.056765,-8.915202,-3.755208,1.784423,-9.890204,-2.241404,-2.432972,8.956346,-8.827070,-1.578612,4.219594,0.819045,9.862789,2.847600,-4.944412,-3.629117,6.835890,-0.206055,-6.332028,-0.749411,4.663981,4.711580,-6.253042,0.353297,-0.200229,3.014005,5.446119,-8.232764,-8.370727,-0.479307,-7.121801,-2.190640,3.743893,4.388056,-0.500513,9.435704,-3.401818,1.469706,2.361625,6.922465,-2.795311,8.234633,-5.257473,4.063424,-7.675730,1.845605,-1.678063,-1.441927,1.968369,4.645152,1.835341,6.686269,-2.200418,-9.942742,4.969942,5.502502,1.002463,0.637673,-8.014903,-9.403940,-5.578612,7.540964,4.540091,3.347873,8.430079,-3.895558,0.749463,-1.629569,-9.688517,3.469079,0.325896,9.421421,9.674042,-7.617365,7.450069,-9.500041,-5.680601,6.645421,-7.797587,-9.925913,5.339942,-6.745500,9.046638,-1.677561,-7.122895,4.754796,-9.596712,-7.607698,-4.392825,1.878913,3.251066,0.924254,8.543123,6.247902,9.360104,2.364876,-1.691570,9.205052,3.296951,8.911047,3.179151,9.301730,2.573567,-1.723916,-8.850266,-5.143031,4.076306,3.764796,-3.854937,-2.988560,2.519261,-6.262718,-7.912155,0.931238,-5.366364,5.113742,9.726321,1.244124,-4.650566,-2.618745,-7.712125,-1.988934,4.718962,-0.352059,-5.297241,1.558062,5.581380,2.919726,-3.699451,1.443676,7.567549,-3.125151,1.967191,3.565699,4.936709,-8.567722,-4.545817,-3.124663,-8.539170,0.330988,5.930419,-1.429022,0.848310,-0.501360,-6.245195,-6.182423,-2.636563,5.405321,-7.794528,6.045689,-4.090326,6.524582,-6.295857,-6.181503,5.943199,7.549127,9.187687,1.210619,0.969196,-6.802200,1.897419,7.604631,0.902332,1.413257,-8.133546,-1.762505,-2.212045,9.960444,7.775579,4.326085,-1.400896,3.166537,7.549117,-7.115613,7.991755,-6.198542,8.793797,-6.046249,-1.531829,-3.461384,9.322884,-9.575535,5.872623,-0.617019,5.936640,1.745421,3.902935,7.477004,1.020641,4.268778,-6.390172,8.553451,-2.807994,4.623835,2.212785,8.744739,-3.201518,-6.427403,3.516819,-0.865403,-1.830215,-4.835692,-3.754964,-8.551271,1.621001,-6.780521,-6.333693,3.970076,-1.028580,6.778508,1.449480,-3.701091,-6.172419,1.840655,3.065090,6.731077,8.686701,8.444498,7.905479,6.196560,-2.536902,3.640585,3.971001,2.284925,9.188328,1.140006,0.545118,-0.937598,-7.828465,7.334719,5.545886,6.350038,6.340764,-4.548326,5.798583,3.565737,-9.964502,-9.802756,-7.029641,5.554647,-1.578772,-7.398896,-9.194785,-9.600404,-1.707277,-9.704507,-4.886270,-1.796865,6.469008,-1.608453,-6.220479,-4.226034,-2.732034,-4.358864,-4.188334,-4.320121,-5.989582,-7.414675,9.525020,6.597385,-5.160365,3.893506,7.673611,-2.189019,1.586777,8.834240,8.312322,-4.086789,-3.181943,-9.496811,-7.874402,-0.235541,8.050536,7.090344,5.582305,-2.056180,-3.206354,-6.356038,3.651787,-5.553717,5.596790,-6.476884,8.341034,7.481384,6.974766,-9.841274,-3.720701,-1.661314,2.619094,5.386627,-2.970159,8.645250,4.420960,-2.127145,-7.361430,3.788398,7.585450,-6.227295,-1.731759,-6.474967,2.112622,7.158458,8.571667,1.088689,7.183672,2.228285,-5.699343,3.781106,-6.172951,-2.800094,-4.698267,2.787066,8.256414,8.535795,5.892058,3.741429,-6.787951,-1.047887,-6.182952,2.665751,-2.963193,9.363364,2.061876,6.298029,8.148115,-0.478314,6.290728,5.172535,-7.699181,4.983487,-7.077323,-0.473526,6.957282,3.192986,7.415359,-3.578879,9.182787,-2.691771,-7.136217,1.779391,-4.524387,8.641620,2.401762,-0.304060,5.809496,5.185293,4.950646,4.836761,-8.599986,-0.959053,2.293636,-0.256357,2.393628,7.315711,-7.873338,4.408168,-4.743837,-7.441927,4.890158,1.261256,-6.626935,-6.356220,5.831709,2.269919,-6.125904,4.424287,-4.263576,2.664963,-1.486232,1.862452,2.051572,2.894380,0.276663,8.704246,5.984825,-2.028647,2.610386,5.040817,-4.272027,-5.763408,-7.318994,-2.330884,5.618624,-0.040739,-2.499237,-3.056035,-7.133377,7.720306,-4.212268,-3.154626,-9.216601,9.132128,-5.194411,-0.506940,5.764900,2.433839,-9.453479,-9.759063,6.508025,4.257905,-5.623714,7.063129,-7.723005,4.835692,4.146494,-4.892569,-0.974823,6.793279,-7.736972,6.007233,3.329631,2.565728,-9.216088,5.815546,4.311062,4.502894,3.550004,-2.753695,3.361042,-2.892939,-7.106523,-2.790691,-1.220495,0.095220,6.570625,2.319737,9.043979,-6.479071,-7.819770,-4.561797,7.226002,-6.895607,-4.107671,-1.888338,-4.349330,9.704166,3.511825,0.467314,1.485414,-3.971159,6.522249,0.673913,-0.118291,-2.805474,-7.004009,-9.059303,-9.835164,-0.058094,-5.025824,-5.485669,3.137790,3.135500,-0.892115,-8.752026,9.197930,-7.415804,-2.139369,5.966170,-5.815028,-1.198933,-3.675895,-2.571254,2.090373,-7.223905,6.898523,-7.552724,-5.632953,9.646732,-7.641082,-8.182466,-6.009879,-7.035028,0.877365,2.004156,8.601795,-4.789810,0.552519,-6.644331,7.866261,-4.661208,9.032450,0.907203,-3.126579,-5.432629,-8.366472,-6.300253,-8.710592,-4.184275,-3.502446,5.534134,1.770430,-0.284890,-4.884574,0.516858,5.461208,-1.922739,-4.723510,-0.608343,-3.231227,1.931522,4.425400,6.574267,-9.020820,1.726807,2.579542,-3.407322,-8.432584,2.683066,9.802573,-7.566572,-7.715276,6.473441,-3.252906,3.642336,4.575458,-0.676567,-9.826273,-3.098698,1.424933,-2.482730,-1.367725,6.807291,6.351852,7.664313,2.755783,8.392364,-9.450979,-9.981822,-8.448804,2.268224,-2.781795,-8.701029,1.875976,7.300562,6.941325,9.153320,-6.530545,-4.397190,-6.304303,-4.239191,-9.081585,8.964241,-8.823467,9.264103,-7.313993,-1.850640,-6.156646,2.616617,0.078793,-8.651409,-0.090361,-7.014358,-8.789455,-7.129074,-9.709147,-3.026802,-3.944070,0.502927,3.486137,9.474236,0.921767,-9.709093,9.505824,9.925512,-3.899358,1.933616,-3.663505,6.722075,-2.726392,5.455577,-5.417532,9.820460,7.526679,-8.244444,-9.535631,-9.234779,6.297838,8.603211,0.340335,-3.140667,7.975535,-5.424705,2.833372,-0.159000,-5.740895,4.917040,-1.694122,8.914268,7.603261,-4.055003,-3.118123,-1.815934,-7.605556,-5.045574,-5.282597,5.319675,-4.350812,3.942764,-7.424612,5.666853,3.755639,1.969452,-4.484659,-8.332682,-4.142041,2.234888,8.314561,0.976449,6.747955,5.295280,-8.661066,3.001166,2.729136,-9.994374,2.135410,-9.583841,-8.576417,-1.706161,-5.059116,8.296110,1.211433,2.050416,-4.749927,-8.371677,-0.498427,6.649648,6.319206,4.340340,-3.256417,-7.657475,-3.391455,-5.051342,-8.233678,1.889239,6.359004,-1.599852,2.851763,-1.934755,-0.081505,1.071925,-6.949830,4.952984,-3.238477,-6.081171,-9.287389,-5.456822,7.315375,-2.690379,8.579261,7.443496,-8.704996,2.132848,2.195568,9.526617,2.614083,7.040397,3.113497,8.556024,8.943050,-5.652043,-0.733765,-8.827352,-4.576703,6.629353,-7.739039,-0.028145,-5.002851,-9.127676,3.099075,6.233426,2.001100,5.403695,0.753174,-7.007775,-0.048444,4.697675,1.301453,1.271872,-4.830964,5.664744,6.376250,6.710653,7.211056,8.365300,8.042667,8.072985,2.126347,5.220368,9.677903,-1.880855,2.799429,-5.601706,4.972871,-9.979240,7.958908,2.587311,3.246793,-1.531514,-8.734688,-3.544720,0.941739,-1.962461,-8.658051,2.556755,5.918741,2.132195,7.643061,3.417440,3.646188,-7.621420,0.708631,0.488614,-7.201487,-3.204741,-9.726733,-8.529027,-9.698422,-9.559473,8.380190,8.292262,7.377295,0.333982,-4.033369,-0.864421,-9.423416,-0.461192,-2.517163,-3.520332,-9.602668,6.902414,1.349099,-6.388104,0.535370,-2.061150,-8.018241,1.247876,3.190310,4.155171,-6.861357,4.555587,-3.288899,-4.492821,-5.626519,-5.000053,0.955668,8.254740,0.219164,1.198552,-4.811211,8.715988,3.036522,3.427871,9.013392,-2.663189,-9.397647,-6.702576,-8.333451,5.187620,-9.337115,8.671606,8.876894,-4.304848,-1.416930,8.646635,-6.268798,8.458148,-6.491728,-1.792395,0.420634,1.276718,-9.046746,2.786504,-0.220905,4.843357,-2.246091,1.673158,2.819124,-0.843247,0.075990,9.499256,2.752100,8.267947,5.927494,1.655003,-9.317671,-2.719410,1.122851,9.922993,-0.449467,-4.937428,0.347533,-1.273700,7.100064,-7.811989,3.915182,-1.586261,8.714105,-1.035499,1.722522,6.571868,-4.973589,2.963079,9.701070,8.540722,1.668159,-0.930343,0.433121,-8.322495,-3.858144,0.305715,-2.546350,-0.681465,3.391031,-4.793132,-7.310516,5.456585,6.756582,-7.228088,9.417258,-7.405462,5.573872,-9.469533,5.657717,-8.141691,5.039063,6.713865,6.286138,4.948433,-3.590375,-1.202569,-3.573145,8.579922,-4.906652,-7.074327,-1.728804,-3.163115,-5.641701,-8.973910,6.379447,6.549939,8.290355,-2.852339,-6.848179,0.142458,1.585417,0.905771,1.505673,1.387771,2.330889,-3.608273,-3.227434,7.598082,7.944595,1.397631,-1.562555,3.223993,1.263619,7.370029,-2.223454,7.531164,-7.652688,6.273971,2.870267,9.630528,-3.794172,-4.411914,-0.636838,8.826185,-0.870238,2.093639,1.678720,-8.093625,-1.707706,-1.712417,-5.074484,2.176971,2.035114,0.039802,6.350021,5.444786,-9.052046,9.313332,7.954512,-1.464689,5.488600,3.237586,-9.223908,8.550727,7.841651,9.679361,9.177984,-5.559080,3.014152,-7.989110,-4.738013,2.055888,2.659126,3.081950,0.985902,-7.701064,0.972843,-9.970161,6.670049,2.642408,4.098196,1.230307,8.394547,2.633702,8.158469,3.707973,4.794739,-5.397813,9.700817,-9.478414,1.777286,2.128624,-0.731389,-0.200048,-5.420449,-5.323096,2.640956,-3.504862,8.822513,0.507352,3.302232,-6.161445,0.067389,-8.817888,-6.079483,-2.008234,9.551458,0.870802,8.752901,-1.811246,8.517132,6.318088,-8.540387,2.245258,-0.710989,-0.577221,9.014580,-1.093181,9.129252,-1.748496,1.974283,5.594287,-0.479621,-7.434085,-1.628306,8.927081,1.796112,-6.814918,0.887218,7.479802,8.231491,8.881163,-2.904768,9.569826,-3.584390,-7.205354,-1.730978,7.067255,-8.078497,-4.628423,-6.783470,-1.017937,4.864832,7.619938,-9.878921,-4.364467,-8.201213,-4.896632,8.036801,-3.650729,0.466755,-0.316828,-4.589003,9.983996,1.423699,1.278239,1.106490,-6.542522,1.145539,3.648468,-1.462101,9.908453,-7.166244,-5.877499,8.302030,1.263356,6.363266,5.364611,1.703175,-0.556017,-1.987242,-3.962108,0.182852,-1.133719,-2.728398,-8.057872,9.624247,7.110270,9.744857,-8.920537,-1.114070,-6.171854,6.728683,9.207964,-2.761048,1.378470,-2.104441,-1.667898,-8.154908,-8.405587,4.706091,-5.690755,-0.769932,-9.086551,6.672304,-6.644933,-2.689670,1.805294,-9.113954,4.795775,-7.363335,-2.698732,-2.908735,-6.950029,3.744589,-6.789581,2.645966,-1.475725,-6.538367,8.486276,6.983556,-9.136746,-1.228602,5.010832,-4.378871,2.571873,0.247721,6.911369,5.838721,9.996084,-5.448534,4.616301,-4.245645,0.422830,-2.092673,-6.855408,2.565255,5.968102,-2.123018,-1.480733,0.522706,7.545698,5.420185,9.695170,-4.948998,-2.529649,-7.698045,-1.054634,3.790479,2.220217,-1.958609,2.669552,-7.418767,-5.283260,1.121528,-4.090671,-0.276889,8.170827,-2.843544,-8.243124,0.493224,-6.475398,-1.099905,-5.258149,-5.673000,1.367151,9.311450,-4.924635,-7.811352,-4.330443,-3.921813,-0.051625,-0.109493,-1.453995,-1.787882,5.682475,5.224902,7.254976,-2.749439,9.501113,-4.547798,-0.491448,7.079937,9.274851,5.775731,5.146605,-9.964769,-7.208632,-6.516991,-3.817926,-6.126811,-3.094413,9.023701,3.092732,-5.223847,-6.069233,-3.617074,-2.494614,-7.379681,9.598143,-1.174128,6.046006,-3.854619,1.613579,-5.151030,-3.239924,-1.932234,6.962114,-2.353371,1.779051,4.475470,2.476444,-5.218869,-1.683043,-4.424660,-5.881875,-2.892146,6.470928,-3.467340,0.135558,-8.487775,4.526999,8.965996,-6.234493,5.123101,-5.051451,-5.204273,-8.053087,6.258428,9.048739,-6.784560,-9.105757,2.844088], dtype = "float32")#candidate|8018|(1470,)|const|float32
call_8017 = func_3486_call(relay.reshape(const_8018.astype('float32'), [14, 7, 15]))
call_8019 = func_3486_call(relay.reshape(const_8018.astype('float32'), [14, 7, 15]))
func_6313_call = mod.get_global_var('func_6313')
func_6317_call = mutated_mod.get_global_var('func_6317')
var_8021 = relay.var("var_8021", dtype = "float64", shape = (2, 384))#candidate|8021|(2, 384)|var|float64
call_8020 = relay.TupleGetItem(func_6313_call(relay.reshape(call_7961.astype('bool'), [14, 7, 9]), relay.reshape(var_8021.astype('float64'), [64, 12]), ), 4)
call_8022 = relay.TupleGetItem(func_6317_call(relay.reshape(call_7961.astype('bool'), [14, 7, 9]), relay.reshape(var_8021.astype('float64'), [64, 12]), ), 4)
uop_8029 = relay.tan(const_8005.astype('float32')) # shape=(220,)
output = relay.Tuple([call_7961,call_8004,call_8017,const_8018,call_8020,var_8021,uop_8029,])
output2 = relay.Tuple([call_7962,call_8006,call_8019,const_8018,call_8022,var_8021,uop_8029,])
func_8050 = relay.Function([var_8021,], output)
mod['func_8050'] = func_8050
mod = relay.transform.InferType()(mod)
mutated_mod['func_8050'] = func_8050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8051 = relay.var("var_8051", dtype = "float64", shape = (2, 384))#candidate|8051|(2, 384)|var|float64
func_8050_call = mutated_mod.get_global_var('func_8050')
call_8052 = func_8050_call(var_8051)
output = call_8052
func_8053 = relay.Function([var_8051], output)
mutated_mod['func_8053'] = func_8053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6865_call = mod.get_global_var('func_6865')
func_6867_call = mutated_mod.get_global_var('func_6867')
call_8055 = func_6865_call()
call_8056 = func_6865_call()
output = relay.Tuple([call_8055,])
output2 = relay.Tuple([call_8056,])
func_8058 = relay.Function([], output)
mod['func_8058'] = func_8058
mod = relay.transform.InferType()(mod)
mutated_mod['func_8058'] = func_8058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8058_call = mutated_mod.get_global_var('func_8058')
call_8059 = func_8058_call()
output = call_8059
func_8060 = relay.Function([], output)
mutated_mod['func_8060'] = func_8060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_8123 = func_4372_call()
call_8124 = func_4372_call()
func_6038_call = mod.get_global_var('func_6038')
func_6041_call = mutated_mod.get_global_var('func_6041')
var_8138 = relay.var("var_8138", dtype = "float64", shape = (882,))#candidate|8138|(882,)|var|float64
call_8137 = relay.TupleGetItem(func_6038_call(relay.reshape(var_8138.astype('float64'), [14, 7, 9])), 1)
call_8139 = relay.TupleGetItem(func_6041_call(relay.reshape(var_8138.astype('float64'), [14, 7, 9])), 1)
output = relay.Tuple([call_8123,call_8137,var_8138,])
output2 = relay.Tuple([call_8124,call_8139,var_8138,])
func_8140 = relay.Function([var_8138,], output)
mod['func_8140'] = func_8140
mod = relay.transform.InferType()(mod)
mutated_mod['func_8140'] = func_8140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8141 = relay.var("var_8141", dtype = "float64", shape = (882,))#candidate|8141|(882,)|var|float64
func_8140_call = mutated_mod.get_global_var('func_8140')
call_8142 = func_8140_call(var_8141)
output = call_8142
func_8143 = relay.Function([var_8141], output)
mutated_mod['func_8143'] = func_8143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6771_call = mod.get_global_var('func_6771')
func_6772_call = mutated_mod.get_global_var('func_6772')
call_8178 = func_6771_call()
call_8179 = func_6771_call()
output = call_8178
output2 = call_8179
func_8186 = relay.Function([], output)
mod['func_8186'] = func_8186
mod = relay.transform.InferType()(mod)
mutated_mod['func_8186'] = func_8186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8186_call = mutated_mod.get_global_var('func_8186')
call_8187 = func_8186_call()
output = call_8187
func_8188 = relay.Function([], output)
mutated_mod['func_8188'] = func_8188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7475_call = mod.get_global_var('func_7475')
func_7477_call = mutated_mod.get_global_var('func_7477')
call_8264 = func_7475_call()
call_8265 = func_7475_call()
uop_8272 = relay.acos(call_8264.astype('float64')) # shape=(882,)
uop_8274 = relay.acos(call_8265.astype('float64')) # shape=(882,)
bop_8281 = relay.floor_divide(uop_8272.astype('float32'), relay.reshape(call_8264.astype('float32'), relay.shape_of(uop_8272))) # shape=(882,)
bop_8284 = relay.floor_divide(uop_8274.astype('float32'), relay.reshape(call_8265.astype('float32'), relay.shape_of(uop_8274))) # shape=(882,)
func_6488_call = mod.get_global_var('func_6488')
func_6491_call = mutated_mod.get_global_var('func_6491')
call_8291 = relay.TupleGetItem(func_6488_call(relay.reshape(uop_8272.astype('bool'), [14, 7, 9])), 1)
call_8292 = relay.TupleGetItem(func_6491_call(relay.reshape(uop_8272.astype('bool'), [14, 7, 9])), 1)
uop_8297 = relay.tan(uop_8272.astype('float32')) # shape=(882,)
uop_8299 = relay.tan(uop_8274.astype('float32')) # shape=(882,)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_8303 = relay.TupleGetItem(func_5215_call(relay.reshape(uop_8297.astype('bool'), [882,])), 3)
call_8304 = relay.TupleGetItem(func_5217_call(relay.reshape(uop_8297.astype('bool'), [882,])), 3)
output = relay.Tuple([bop_8281,call_8291,uop_8297,call_8303,])
output2 = relay.Tuple([bop_8284,call_8292,uop_8299,call_8304,])
func_8313 = relay.Function([], output)
mod['func_8313'] = func_8313
mod = relay.transform.InferType()(mod)
mutated_mod['func_8313'] = func_8313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8313_call = mutated_mod.get_global_var('func_8313')
call_8314 = func_8313_call()
output = call_8314
func_8315 = relay.Function([], output)
mutated_mod['func_8315'] = func_8315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4873_call = mod.get_global_var('func_4873')
func_4874_call = mutated_mod.get_global_var('func_4874')
call_8324 = relay.TupleGetItem(func_4873_call(), 0)
call_8325 = relay.TupleGetItem(func_4874_call(), 0)
uop_8330 = relay.acosh(call_8324.astype('float32')) # shape=(14, 7, 9)
uop_8332 = relay.acosh(call_8325.astype('float32')) # shape=(14, 7, 9)
output = uop_8330
output2 = uop_8332
func_8363 = relay.Function([], output)
mod['func_8363'] = func_8363
mod = relay.transform.InferType()(mod)
mutated_mod['func_8363'] = func_8363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8363_call = mutated_mod.get_global_var('func_8363')
call_8364 = func_8363_call()
output = call_8364
func_8365 = relay.Function([], output)
mutated_mod['func_8365'] = func_8365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_8438 = relay.TupleGetItem(func_4774_call(), 3)
call_8439 = relay.TupleGetItem(func_4776_call(), 3)
func_6704_call = mod.get_global_var('func_6704')
func_6706_call = mutated_mod.get_global_var('func_6706')
call_8443 = relay.TupleGetItem(func_6704_call(), 0)
call_8444 = relay.TupleGetItem(func_6706_call(), 0)
func_6123_call = mod.get_global_var('func_6123')
func_6126_call = mutated_mod.get_global_var('func_6126')
const_8451 = relay.const([-7.601062,-0.963923,-7.216204,0.643902,-2.536569,1.011268,-4.553372,0.417846,7.168459,5.670435,7.710579,-8.915691,-4.533176,-1.452532,5.385416,8.960420,5.950907,4.787760,4.292114,-5.775909,7.855963,5.240339,-5.530095,-3.567649,-2.135412,-7.233008,-0.821095,-7.967441,-0.090463,-8.496808,5.537861,-4.382480,5.025596,1.189998,-5.295598,2.976866,2.499128,6.961101,3.210517,9.698702,-0.747031,-2.754889,9.647693,8.965345,2.373685,3.257611,-2.404932,1.302415,-9.023459,-6.152894,-4.245546,-5.693219,8.736988,9.174225,7.548288,-2.492411,0.831630,7.721211,3.371152,-1.440772,-9.140750,-8.253423,2.183318,1.179856,-6.518813,4.632866,4.766958,-1.668710,1.340466,0.046875,-3.269588,-4.945095,-1.384774,-5.337066,8.773841,-9.094463,2.545979,-5.313632,8.099260,-2.369644,5.124395,-4.042670,8.924692,5.361928,6.318485,5.190409,-7.980858,8.907080,4.736834,3.195303,-0.286242,4.267576,-4.175532,2.899357,4.227555,0.950596,9.314666,5.309114,-9.697122,0.908833,7.359679,2.681298,0.437668,4.058997,7.093148,6.558472,-1.737085,5.421992,-7.298216,-6.559726,-4.973892,-3.636383,-5.589760,-7.768418,1.639931,-9.508100,-4.172076,-0.707437,-7.444357,4.877261,-5.913628,8.897990,7.408836,3.524304,8.142548,2.446709,8.801314,1.759314,6.418700,-6.052661,-0.907749,4.451781,0.936579,-6.111093,0.707246,7.811107,-7.255326,3.890168,4.574494,8.702916,-6.869630,-7.319143,-7.261453,0.414487,0.589248,-6.370390,-1.146232,-7.335066,-4.856949,9.521258,-1.262483,6.441968,-1.386632,-2.740661,-7.001626,-1.470820,-2.887406,-7.779211,6.484872,-2.294490,-1.008783,-9.074927,8.231420,-6.874534,4.518840,9.232723,-7.262778,-8.768618,9.406744,-3.860902,-7.866512,9.212447,7.786015,3.789330,4.842335,2.044672,0.467593,2.400557,-0.899446,-1.053304,2.405511,-8.175140,-5.389369,-0.436467,1.779389,8.683093,-9.839353,0.930521,4.205337,-3.122179,-5.737561,-8.984344,9.409719,-7.464073,7.449808,7.129031,6.694788,-4.595923,-3.921659,0.902496,4.627834,0.441738,3.179146,9.790762,7.884641,-0.710046,2.329183,3.592488,-7.342233,-3.981648,-4.859213,-6.376771,3.639318,-9.954498,-2.375307,-3.572016,-4.361934,3.585577,-6.156917,-3.492039,-3.410767,1.781043,8.834792,-1.274441,9.987007,2.278977,-4.616774,1.963674,-5.971850,6.830393,0.127335,-6.605910,5.125259,-6.981808,-2.378292,2.122165,2.346660,-4.852416,-7.297565,-1.833068,-9.249224,2.046065,9.918061,-5.085886,-2.390697,-0.548704,4.368669,-9.191022,-0.557119,-6.395489,8.242829,6.221563,9.247970,-2.148171,-0.627612,1.106420,-8.866176,5.053551,6.234138,-5.778511,5.557558,4.758818,1.135589,1.810539,-9.732519,7.653802,-5.956440,-7.632459,-2.536957,1.255584,8.070613,6.768365,0.232828,-2.826164,6.800097,7.954050,3.940722,7.495215,-2.180775,2.487537,4.551865,-4.559967,1.491317,7.323796,2.660243,9.639729,7.696962,6.267096,8.810887,9.649279,-0.113218,-6.159309,6.094815,-6.506635,-6.095109,4.736495,-8.620868,8.694680,-9.513683,-6.804403,4.755956,6.085750,-8.109861,-8.702886,-8.331849,-2.717112,-6.552697,-7.630117,9.780739,8.505124,-2.343596,0.630294,-0.316155,0.666846,5.679353,8.924217,5.396345,4.058043,1.562657,6.889293,2.479575,-2.642021,-1.408009,3.751193,2.859495,-8.114317,5.150379,9.352560,-0.812504,9.192529,-6.774657,8.433550,3.785915,7.787909,-1.432380,-3.567681,2.531002,4.076892,9.731304,9.769855,0.261009,7.709139,3.748593,-1.901730,0.098457,5.471707,-5.514526,0.255013,6.231178,-5.279959,1.326871,4.581201,6.436246,6.562112,1.448825,-7.829437,-1.237967,-5.959654,-1.554047,3.374213,-4.526012,2.340360,6.537295,-7.680234,9.400872,-0.791000,1.615538,0.105791,-3.152752,9.505202,6.092507,-2.499748,9.230581,7.712454,-6.279640,4.728306,7.776467,7.421546,1.989101,4.566604,5.993127,-3.743769,1.109124,0.027056,-3.027607,-2.233923,-3.164767,0.196490,0.519912,1.927122,0.780682,-6.668274,0.351713,-6.947698,8.247054,-5.694549,8.350684,6.019912,-6.182455,4.606230,9.586448,4.689875,-1.891793,-8.308621,0.849741,4.396842,-1.177362,-2.311279,-3.781384,0.912272,-1.779727,-4.372527,-3.571402,5.860062,-6.790425,4.105904,-3.608920,-3.191762,5.223440,-3.465835,-8.113130,0.681736,7.120381,0.943174,-9.326525,8.493917,-0.690400,7.406722,6.898842,2.962115,4.229020,1.791985,8.784627,-3.391553,-1.672823,-0.302729,9.035854,-2.966351,9.232677,-7.599624,-9.126463,-6.643207,2.297418,7.460252,-1.689662,-1.879017,7.291228,9.924120,9.663438,6.288055,-1.975091,9.509832,7.532577,-4.523069,2.165177,1.106465,-5.525188,-3.127405,4.532044,-0.033389,-3.756307,2.071978,5.198793,8.286996,-4.622840,-1.544338,-9.593047,-3.506415,0.867201,-1.629507,1.210643,-9.906197,2.749466,9.530444,-6.345348,4.691214,8.752224,-4.810256,5.596021,3.374242,-7.024477,6.212939,6.267544,1.878503,-3.007472,6.018272,9.752215,-6.886636,-4.362959,1.830377,4.018200,-4.679049,4.418159,6.302394,-0.242056,-6.229040,0.289787,8.522088,-0.062261,4.618491,-2.081712,-8.294138,8.240008,-5.434462,3.320866,-1.924147,-2.532781,8.195594,-4.106444,1.832469,9.935879,2.600865,0.212504,-5.291154,9.022769,-9.875311,-9.173980,1.868955,2.827024,-6.636997,7.904559,-9.861915,2.873180,4.495667,-1.349930,-3.539630,8.837429,-9.470653], dtype = "float32")#candidate|8451|(528,)|const|float32
call_8450 = relay.TupleGetItem(func_6123_call(relay.reshape(const_8451.astype('float32'), [11, 12, 4])), 0)
call_8452 = relay.TupleGetItem(func_6126_call(relay.reshape(const_8451.astype('float32'), [11, 12, 4])), 0)
output = relay.Tuple([call_8438,call_8443,call_8450,const_8451,])
output2 = relay.Tuple([call_8439,call_8444,call_8452,const_8451,])
func_8454 = relay.Function([], output)
mod['func_8454'] = func_8454
mod = relay.transform.InferType()(mod)
mutated_mod['func_8454'] = func_8454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8454_call = mutated_mod.get_global_var('func_8454')
call_8455 = func_8454_call()
output = call_8455
func_8456 = relay.Function([], output)
mutated_mod['func_8456'] = func_8456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8186_call = mod.get_global_var('func_8186')
func_8188_call = mutated_mod.get_global_var('func_8188')
call_8526 = func_8186_call()
call_8527 = func_8186_call()
uop_8529 = relay.sinh(call_8526.astype('float64')) # shape=(882,)
uop_8531 = relay.sinh(call_8527.astype('float64')) # shape=(882,)
func_5245_call = mod.get_global_var('func_5245')
func_5246_call = mutated_mod.get_global_var('func_5246')
call_8537 = func_5245_call()
call_8538 = func_5245_call()
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_8549 = func_4372_call()
call_8550 = func_4372_call()
output = relay.Tuple([uop_8529,call_8537,call_8549,])
output2 = relay.Tuple([uop_8531,call_8538,call_8550,])
func_8552 = relay.Function([], output)
mod['func_8552'] = func_8552
mod = relay.transform.InferType()(mod)
output = func_8552()
func_8553 = relay.Function([], output)
mutated_mod['func_8553'] = func_8553
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8672 = relay.var("var_8672", dtype = "float32", shape = (14, 7, 13))#candidate|8672|(14, 7, 13)|var|float32
uop_8673 = relay.asin(var_8672.astype('float32')) # shape=(14, 7, 13)
func_2145_call = mod.get_global_var('func_2145')
func_2147_call = mutated_mod.get_global_var('func_2147')
const_8683 = relay.const([[7.375235,-0.315991,2.782448,2.390276,8.745691,7.873219,3.500260,0.687086,6.351426,4.021882,-6.616372,-8.606072,-3.463491,-6.818583,8.375313,9.038227,-6.576614,-0.460968,0.667405,1.649265,-7.639385,-3.711250,8.677414,-4.036975],[-9.044373,2.034827,-0.398882,-2.980362,1.235934,2.436456,7.698354,-8.379464,-8.266810,5.892065,-0.964662,0.205068,5.975874,-0.620200,9.702382,1.025734,-0.122662,-9.181381,3.320446,8.043242,5.902306,0.095658,5.831814,-8.008298],[9.223423,6.802020,-7.496579,-5.679258,1.475225,-4.554531,9.270164,-6.846448,9.164255,-3.792300,9.520011,8.227127,-5.951820,8.202549,-0.253525,-8.169766,3.685612,6.358126,-9.155187,3.721539,-0.389335,-2.345885,1.243219,3.946937],[-5.277537,6.179196,-7.731929,-6.645989,-7.996852,-7.067359,-3.433934,-3.031573,8.005542,5.340151,4.324954,5.932407,4.905595,7.719699,-4.706098,7.427472,3.921806,-2.961156,4.900024,-5.819933,-7.337576,9.486259,5.047906,-7.849134]], dtype = "float64")#candidate|8683|(4, 24)|const|float64
call_8682 = func_2145_call(relay.reshape(const_8683.astype('float64'), [1, 8, 12]))
call_8684 = func_2145_call(relay.reshape(const_8683.astype('float64'), [1, 8, 12]))
output = relay.Tuple([uop_8673,call_8682,const_8683,])
output2 = relay.Tuple([uop_8673,call_8684,const_8683,])
func_8687 = relay.Function([var_8672,], output)
mod['func_8687'] = func_8687
mod = relay.transform.InferType()(mod)
mutated_mod['func_8687'] = func_8687
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8688 = relay.var("var_8688", dtype = "float32", shape = (14, 7, 13))#candidate|8688|(14, 7, 13)|var|float32
func_8687_call = mutated_mod.get_global_var('func_8687')
call_8689 = func_8687_call(var_8688)
output = call_8689
func_8690 = relay.Function([var_8688], output)
mutated_mod['func_8690'] = func_8690
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8692 = relay.var("var_8692", dtype = "float32", shape = (11, 10, 14))#candidate|8692|(11, 10, 14)|var|float32
uop_8693 = relay.tan(var_8692.astype('float32')) # shape=(11, 10, 14)
output = uop_8693
output2 = uop_8693
func_8703 = relay.Function([var_8692,], output)
mod['func_8703'] = func_8703
mod = relay.transform.InferType()(mod)
var_8704 = relay.var("var_8704", dtype = "float32", shape = (11, 10, 14))#candidate|8704|(11, 10, 14)|var|float32
output = func_8703(var_8704)
func_8705 = relay.Function([var_8704], output)
mutated_mod['func_8705'] = func_8705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4850_call = mod.get_global_var('func_4850')
func_4852_call = mutated_mod.get_global_var('func_4852')
call_8710 = relay.TupleGetItem(func_4850_call(), 0)
call_8711 = relay.TupleGetItem(func_4852_call(), 0)
func_6407_call = mod.get_global_var('func_6407')
func_6408_call = mutated_mod.get_global_var('func_6408')
call_8712 = relay.TupleGetItem(func_6407_call(), 0)
call_8713 = relay.TupleGetItem(func_6408_call(), 0)
func_8454_call = mod.get_global_var('func_8454')
func_8456_call = mutated_mod.get_global_var('func_8456')
call_8721 = relay.TupleGetItem(func_8454_call(), 2)
call_8722 = relay.TupleGetItem(func_8456_call(), 2)
output = relay.Tuple([call_8710,call_8712,call_8721,])
output2 = relay.Tuple([call_8711,call_8713,call_8722,])
func_8735 = relay.Function([], output)
mod['func_8735'] = func_8735
mod = relay.transform.InferType()(mod)
mutated_mod['func_8735'] = func_8735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8735_call = mutated_mod.get_global_var('func_8735')
call_8736 = func_8735_call()
output = call_8736
func_8737 = relay.Function([], output)
mutated_mod['func_8737'] = func_8737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5398_call = mod.get_global_var('func_5398')
func_5400_call = mutated_mod.get_global_var('func_5400')
call_8738 = relay.TupleGetItem(func_5398_call(), 3)
call_8739 = relay.TupleGetItem(func_5400_call(), 3)
output = relay.Tuple([call_8738,])
output2 = relay.Tuple([call_8739,])
func_8745 = relay.Function([], output)
mod['func_8745'] = func_8745
mod = relay.transform.InferType()(mod)
mutated_mod['func_8745'] = func_8745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8745_call = mutated_mod.get_global_var('func_8745')
call_8746 = func_8745_call()
output = call_8746
func_8747 = relay.Function([], output)
mutated_mod['func_8747'] = func_8747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8058_call = mod.get_global_var('func_8058')
func_8060_call = mutated_mod.get_global_var('func_8060')
call_8760 = relay.TupleGetItem(func_8058_call(), 0)
call_8761 = relay.TupleGetItem(func_8060_call(), 0)
const_8762 = relay.const([[0.991531,4.311084,6.507047,4.561447,1.621409,-8.673976,-2.355403,-0.118813,0.782594,-3.748261,0.419192,9.347263,-4.456741],[-9.681013,-0.869110,5.607132,6.953118,7.161635,8.873574,-9.742291,-3.752698,-0.190483,-6.962982,-4.678137,5.053657,-2.290385],[9.583596,8.619691,-1.673268,-1.026164,-7.226728,-9.167600,-0.795387,-0.891527,-8.337551,-7.175141,-0.264527,2.739857,-0.145571],[-9.299558,-0.333773,-5.628237,-6.162652,-1.384962,1.983354,0.250477,-7.331082,-3.585785,-7.791209,-4.190989,7.827612,6.193463],[2.305392,8.326384,3.606839,-9.696171,-8.897598,1.105095,-9.057653,5.000505,-7.433197,4.594997,-8.549918,0.375582,5.175056],[2.795651,8.452520,-3.623551,-1.759305,-4.624156,1.839632,2.461345,6.492501,-9.955869,-1.768522,-8.933798,5.626046,-6.997027],[4.669336,-4.043379,7.043114,1.059107,-1.545217,-1.957406,8.551805,-6.783198,3.862592,-1.556677,3.421327,-9.190787,-7.345257],[-6.571806,4.016506,6.888181,0.971904,5.470142,-3.857864,7.262552,-8.503700,3.712011,-8.522643,-0.241787,9.981343,-5.481129],[7.507270,2.161134,2.916708,1.589662,-0.697018,0.522978,-7.183762,-4.010646,-1.853425,-2.449839,5.660556,-1.653374,3.743007],[9.224258,-7.841662,9.191691,5.385037,2.888464,0.952098,8.398452,-7.820096,4.874429,1.966503,0.758235,2.401563,-9.426703],[4.780241,-6.267014,0.291359,3.189508,0.079962,9.852136,2.848914,-2.452966,-4.544151,-2.299808,-4.468515,7.604969,-9.750006],[5.134253,-2.097045,-1.519669,4.469439,0.002446,1.997377,-7.265864,8.685367,4.645556,-9.008549,3.184191,1.859088,7.809575],[2.560255,7.715765,9.022853,0.399153,-6.603799,3.780495,-6.204032,-7.011263,-5.764136,5.663031,-9.286041,-3.105542,-3.358905],[9.999329,-4.773677,1.489719,-7.570866,7.761847,-7.538477,9.414829,-0.562790,-4.487913,2.103533,-3.523509,2.630381,-0.576114],[-4.996440,-0.517143,-6.163070,-6.965564,5.397069,5.702452,-4.862602,6.286876,3.713458,7.660576,-5.017322,7.828690,-9.603284],[6.641316,5.900725,-8.719678,-5.974907,-1.448705,-7.099532,3.720204,-1.534541,3.462191,7.437659,2.632750,-9.726071,5.722409],[-6.629875,-1.144797,-5.046508,-3.461309,1.273181,-5.599216,-3.503937,9.757759,6.868502,-7.539857,3.651046,4.142502,-3.305218],[6.765343,0.045039,1.401234,9.306429,2.349528,9.842684,5.603406,-6.216621,7.514029,-8.925855,3.185136,0.564974,-3.454730],[-5.691619,-6.680841,-8.449967,0.979597,-1.752161,-8.634684,-8.416810,5.305727,9.852020,5.928658,-3.876853,-2.783611,5.964059],[6.279271,5.162895,4.953674,7.629184,2.675445,8.272579,3.012815,6.449639,-2.575021,0.701311,-2.006908,-5.545388,-5.630759],[-1.387432,-6.953987,0.864687,-9.349838,7.306106,-4.207353,3.669523,-5.575491,-3.347491,-3.205938,7.108184,6.735344,9.274492],[-1.389974,8.821791,-5.519980,5.985894,8.750468,-8.673236,-8.806789,6.133679,-8.632987,-1.898648,-8.963121,4.367795,-5.063157],[6.132770,2.891175,7.154102,-9.759185,9.823545,-6.171136,5.005978,1.996513,-9.555558,1.356404,-8.935216,-7.595592,5.568770],[5.221260,-4.571485,4.007720,4.597467,-9.475598,-5.533964,-2.744203,9.069747,1.665603,-0.093075,4.378888,-2.686721,3.749595],[-1.033739,9.658856,-3.095216,-5.386257,-6.581867,-3.054515,9.385441,7.837227,4.123655,3.485857,-8.185202,-1.373024,6.975001],[3.362307,-8.872417,-2.022844,0.005670,-3.037647,-3.607714,-0.915513,2.331662,-5.475755,7.563257,-4.186621,3.782968,1.286617],[-7.351875,0.249486,8.882109,1.419697,5.661403,5.822703,4.372867,-3.644808,-2.253780,4.896913,3.020311,-7.620035,7.411958],[4.361835,-9.845612,-7.590571,-8.619490,-5.974596,5.495580,-7.572814,2.126251,3.754470,8.253140,-8.720606,-3.387188,4.737969],[-6.298524,-1.508796,3.946811,-2.821434,-4.397565,-6.537006,-9.357059,7.320924,9.576976,-0.265101,8.760529,7.674455,2.031013],[-3.166966,7.979128,7.279614,-7.937505,1.622047,-8.407077,2.067751,2.203361,8.397184,5.977810,6.144290,-6.926877,8.813321],[5.467649,3.564019,1.917274,-5.018945,7.707711,-9.374101,6.094677,8.723803,1.554520,-9.170555,5.722608,9.599781,-6.509400],[9.288749,-6.001459,-7.290774,0.972582,4.281805,-4.580131,-2.591282,7.342751,5.312392,-7.813930,-4.954007,0.650236,-0.771554],[0.798147,3.418054,-9.706335,-9.008886,-1.971396,-5.369909,-7.623109,-0.138438,8.067000,3.722859,2.919491,7.954085,1.415488],[1.978635,0.440177,1.288952,9.607351,-3.902729,4.317503,2.067791,-1.823316,-9.855246,6.621864,9.012312,4.707535,6.692493],[4.893248,-0.235469,0.191777,7.051969,-2.756607,2.676906,-7.237595,2.920616,-7.045315,2.196919,5.704992,-1.419253,-1.663605],[9.608549,-1.817221,-4.052278,-0.331811,-8.125438,-1.346777,-9.022496,6.668877,1.313741,0.955911,4.579443,5.247605,-0.051995],[-3.597987,2.158338,-2.964217,-4.715518,9.702335,-6.144517,-3.871056,1.385058,8.800209,9.891666,4.666654,-9.467128,2.563852],[5.925829,-5.827237,8.089665,-0.005456,9.218988,-8.691725,4.066045,-3.081295,7.982669,-8.405401,0.163453,-2.971481,-0.952195],[7.187863,-8.584579,8.069927,6.535688,-2.810461,-4.635368,9.794849,3.651507,-3.330173,-9.642706,4.968172,2.986114,-4.445763]], dtype = "float64")#candidate|8762|(39, 13)|const|float64
bop_8763 = relay.greater(call_8760.astype('bool'), relay.reshape(const_8762.astype('bool'), relay.shape_of(call_8760))) # shape=(39, 13)
bop_8766 = relay.greater(call_8761.astype('bool'), relay.reshape(const_8762.astype('bool'), relay.shape_of(call_8761))) # shape=(39, 13)
uop_8783 = relay.erf(const_8762.astype('float64')) # shape=(39, 13)
bop_8788 = relay.logical_or(uop_8783.astype('bool'), relay.reshape(bop_8763.astype('bool'), relay.shape_of(uop_8783))) # shape=(39, 13)
bop_8791 = relay.logical_or(uop_8783.astype('bool'), relay.reshape(bop_8766.astype('bool'), relay.shape_of(uop_8783))) # shape=(39, 13)
func_3486_call = mod.get_global_var('func_3486')
func_3489_call = mutated_mod.get_global_var('func_3489')
var_8797 = relay.var("var_8797", dtype = "float32", shape = (1470,))#candidate|8797|(1470,)|var|float32
call_8796 = func_3486_call(relay.reshape(var_8797.astype('float32'), [14, 7, 15]))
call_8798 = func_3486_call(relay.reshape(var_8797.astype('float32'), [14, 7, 15]))
output = relay.Tuple([bop_8788,call_8796,var_8797,])
output2 = relay.Tuple([bop_8791,call_8798,var_8797,])
func_8809 = relay.Function([var_8797,], output)
mod['func_8809'] = func_8809
mod = relay.transform.InferType()(mod)
mutated_mod['func_8809'] = func_8809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8810 = relay.var("var_8810", dtype = "float32", shape = (1470,))#candidate|8810|(1470,)|var|float32
func_8809_call = mutated_mod.get_global_var('func_8809')
call_8811 = func_8809_call(var_8810)
output = call_8811
func_8812 = relay.Function([var_8810], output)
mutated_mod['func_8812'] = func_8812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7906_call = mod.get_global_var('func_7906')
func_7908_call = mutated_mod.get_global_var('func_7908')
call_8849 = relay.TupleGetItem(func_7906_call(), 0)
call_8850 = relay.TupleGetItem(func_7908_call(), 0)
func_3486_call = mod.get_global_var('func_3486')
func_3489_call = mutated_mod.get_global_var('func_3489')
const_8859 = relay.const([1.271819,-6.272982,6.334582,8.975510,-6.096795,-2.002329,9.993682,-6.184036,3.608109,5.532053,7.488674,9.180812,4.980224,-8.461103,-3.303383,9.069795,7.016192,9.880491,2.685617,8.411690,-0.629860,-8.535626,-1.910142,7.655902,-2.249354,4.092926,5.016163,-9.510298,-1.065185,0.451670,6.440089,-5.341637,2.159990,6.408810,-5.826878,-6.123801,-5.146759,-3.532552,3.267803,-8.674923,9.947507,8.707939,-0.792836,9.490504,-1.024239,8.253869,3.248837,-8.119908,2.038503,-1.069419,-1.955737,1.264850,3.159298,8.733194,2.162468,4.265857,4.812490,6.161895,-6.911314,-0.191452,-7.188253,-7.141497,7.986319,-5.918609,-9.915613,4.783596,4.986640,1.287368,-1.270496,5.215751,-1.152555,-5.267321,7.723223,-3.470827,9.648884,-4.370891,-2.384269,1.574002,4.610590,7.681082,-3.546726,-2.638919,5.004542,4.386795,3.539058,4.469925,2.688266,7.237439,1.588911,-6.810143,0.900790,-2.309818,8.654777,2.322179,4.153783,-4.658243,5.844671,5.630211,-7.230797,5.119430,8.071813,3.111902,-4.686868,0.782900,-7.298403,-8.865917,-3.698255,-4.129906,0.737803,-7.079931,-6.288810,-2.188989,-9.840768,-9.401160,-8.928358,-5.063808,-8.747622,-0.942300,-7.371926,-3.198362,0.875655,-2.919885,-7.715479,3.617768,5.318797,-6.344649,-9.519971,5.252997,2.020292,7.849388,4.033717,1.350763,-3.555084,2.986271,-2.663896,4.883334,-5.000265,6.749729,-3.039255,-6.812548,9.725954,2.777758,-3.888707,-6.662993,-7.351016,6.285922,1.923840,9.920456,2.045406,-9.318697,0.869490,4.979535,-9.940613,-7.211146,-4.013326,-2.274855,4.526914,7.880737,-9.437076,8.221805,-6.966571,4.311305,-1.670108,4.504679,1.388255,3.401653,7.963468,-6.585309,2.868855,7.282891,-1.602330,3.683399,2.693375,1.922549,-0.992567,7.546229,4.345393,-8.584194,6.430146,5.450742,-5.860125,2.175975,-0.340928,5.507728,-7.342573,2.355328,-0.822216,6.798593,0.337539,7.450833,5.020625,-8.369731,1.442807,-9.434979,-8.228809,9.537262,-5.689554,3.196068,3.597955,2.656353,7.722833,-7.787351,5.194441,3.210707,-1.586563,2.035159,5.347593,-2.345125,-1.171266,-6.127115,6.329475,1.621587,-1.917264,-3.421475,1.873583,-1.716291,-2.257311,-5.732549,-1.551492,-0.038162,0.884286,-3.497460,-0.393128,9.274940,-0.587431,7.795257,-6.166990,5.177264,2.953963,-1.587402,2.378405,4.812773,2.331960,-3.857669,-7.623388,-5.941886,-5.847664,-2.870296,8.948894,2.403467,2.028027,9.836011,-5.881167,3.540074,-6.652130,-1.649502,-0.757267,7.951149,-2.725715,5.456480,7.408138,-7.685186,-8.422872,-4.538078,-0.194833,1.196834,-9.496470,9.224914,-2.505174,4.272116,-2.695642,-1.495540,8.793052,-7.277285,0.462858,-0.326301,0.670736,-0.135893,-1.023417,-1.581722,6.197303,-6.847748,-0.920819,-5.843555,-3.864502,-5.147898,8.861721,5.249569,-9.509574,-8.158181,2.563964,-8.936361,0.854688,6.017600,2.826372,2.286725,5.086806,3.649123,0.210750,-5.821387,7.019911,7.545583,-9.652518,3.478983,-7.547226,-9.733987,4.915673,7.200504,-8.791962,-8.624561,-4.788168,-6.839322,5.457886,7.154103,1.438317,0.617087,-1.763027,4.375233,8.868942,-0.556958,5.220254,-9.382985,0.908508,2.393400,-6.861683,-7.389477,6.706001,-3.812500,-1.239437,-6.135983,-0.523337,-2.776171,-8.630986,5.550040,-8.709268,9.244751,-5.387851,-1.278442,6.739052,8.375388,2.274893,-6.814724,-5.603676,-7.673607,4.897393,-5.721803,-9.293873,-9.265280,6.081210,-6.872363,4.147006,4.858861,2.855557,-6.604226,0.203651,-8.265670,2.974690,-6.375192,-0.594426,-7.507716,3.823322,4.952849,3.554460,-6.629726,7.637257,-3.224137,-2.401730,-0.030743,-0.448718,7.873577,4.013362,-9.240111,-9.740842,-0.732418,5.177700,-4.438811,-8.779055,-1.847026,-7.020315,-2.461796,-1.135507,-3.764524,-7.299078,-5.917224,1.016382,-2.796921,-6.560745,4.041061,1.504359,1.339715,-0.917290,5.958895,7.519418,-2.220711,-1.431690,7.308822,-4.498825,-1.381199,-9.229642,6.693687,-6.957791,-0.904735,-9.357656,4.116246,-6.608206,4.960094,2.949495,7.161118,-0.374629,-6.341144,-3.423239,2.318218,2.366670,4.722172,8.862086,-2.958212,-6.541607,-7.605362,-1.466236,7.559461,-2.085761,-1.592545,5.384711,-3.626375,3.119365,5.980039,-3.942549,-3.163832,-0.556435,1.589875,-7.925940,1.444615,1.204404,-3.821819,7.836155,-0.540736,-0.663515,3.200869,-2.305571,0.493845,-9.021308,2.740720,-8.490740,4.635577,2.039113,-5.992805,-7.749513,-6.124758,2.095537,4.175926,-6.115297,-3.236605,-5.372873,1.937985,2.765842,5.085716,7.262131,-4.043222,-0.096308,-7.045093,-2.671711,-7.532376,-2.564853,-1.006250,8.460832,-9.226931,2.685969,-5.698963,9.083915,-2.272361,-4.548727,-5.192285,-8.660606,3.706614,-4.847287,-8.490023,-2.525122,8.147154,-1.729118,-0.958720,-5.204331,4.889082,2.036508,5.670286,5.220401,5.416045,2.945012,9.472338,-8.144805,5.373923,-1.656130,-4.319736,-9.900989,3.998958,4.994762,-5.442513,3.858636,-0.042888,6.178948,1.918010,5.409814,-6.966299,-8.656987,0.820538,8.920175,-2.046900,-9.929787,-9.034477,-6.978617,3.648449,-7.436213,1.930311,-0.816955,-1.746137,-5.840040,-5.217469,1.790394,-9.964832,7.656810,-5.706032,-9.118885,-5.454535,1.558865,6.561458,2.491209,-4.312171,-4.016054,8.395738,7.716092,-4.142584,0.440972,9.458457,-4.701919,-4.851375,3.859072,-5.399387,0.445103,2.060785,1.099346,2.299238,5.761505,-3.768865,0.580009,-7.021834,-3.516990,-6.359592,-1.580766,-8.127208,-2.989159,-1.773581,8.934904,8.642083,3.671977,-4.213934,-3.429528,4.679344,8.711939,0.960335,6.081402,6.551838,5.977188,1.054322,0.512057,-2.470107,1.974845,-1.241965,9.269528,3.063553,-5.584655,9.148905,6.426438,-0.274408,2.839679,-6.246338,-2.995927,-4.791138,7.150440,9.049477,1.119949,-3.713840,-8.528881,2.723141,1.048810,-7.389321,-8.523341,-9.036123,3.656415,-7.657950,-4.601303,3.130933,-3.854844,-8.346682,-6.161011,4.985954,6.674928,-3.809952,-9.188046,7.146339,-0.972889,4.781278,-6.142302,7.795475,-9.128365,-6.036098,-3.145080,7.973894,4.164270,-4.346320,5.504108,5.467988,-6.057501,-5.902379,3.583600,-4.506624,-7.585289,5.819147,3.898751,-6.328261,-1.445560,-8.466654,-1.007825,-4.944461,-2.861975,9.760356,-0.869735,-7.766018,-8.799922,0.850783,5.255109,-8.443887,8.084731,-7.638362,-5.996606,-8.391648,7.857779,5.674085,3.716521,7.568110,-2.198663,1.023639,5.712756,2.738348,3.951157,2.747671,-4.452483,-2.639082,9.183879,-0.832239,5.586950,5.474888,-1.925664,-4.483762,-0.326827,6.720423,8.623046,5.599699,-4.864493,-8.924651,8.347361,-9.280109,8.601921,4.264247,9.966882,-1.377755,-0.459980,7.497845,-3.941824,-2.299380,7.961588,-3.663715,2.311880,2.833546,-4.786259,1.283939,-7.142668,-6.287016,-3.926474,-6.598101,6.490818,-9.175973,-1.659805,-7.047295,1.198035,0.893263,-6.505702,0.450854,3.794748,-6.117422,8.934385,1.210504,2.969546,6.149219,4.086354,-2.887884,3.809968,6.371787,-2.196816,-0.838823,-4.191144,9.324041,7.198975,-2.514081,6.716604,5.711133,-0.164060,-4.023246,-1.774509,8.314252,-2.366773,-8.048844,-3.964748,3.619530,-7.592568,9.106701,-4.746194,0.202502,6.848403,-5.607824,-2.638770,2.475933,0.503455,3.471668,-5.357068,1.685219,-3.561802,-0.341146,1.723453,4.918587,6.641308,4.745476,9.014396,-8.468076,-4.448249,-0.780409,-5.235068,-0.986318,2.140233,7.899586,-0.531937,-4.053198,-0.449798,-5.678137,6.489061,1.433760,-2.379866,-4.071161,-9.741396,-9.022980,1.127200,5.775365,9.759911,7.533115,9.354915,-8.021006,-4.151155,-1.708430,6.243167,-1.034886,9.089058,5.155448,-9.908355,5.134039,-7.978292,-0.232448,-0.107305,8.900291,7.086050,7.342916,0.010579,-5.717584,-6.633317,6.434360,3.803418,-5.059992,3.950427,-5.807610,1.328145,-8.753017,-7.407273,-9.288920,9.854245,-7.670857,-0.194257,8.919781,5.739191,6.751966,9.883956,3.451881,5.595808,9.759946,3.970944,-6.295055,1.750590,5.117374,8.252881,9.086075,0.758975,9.061794,3.071843,-6.549981,5.574646,-2.066137,-2.945926,9.949100,-0.223247,-2.835750,9.697145,-2.591861,-9.371501,-5.862075,0.393198,-6.957687,1.497899,1.550981,-3.151522,7.169452,7.795174,-0.317373,9.374841,8.448039,-3.994186,7.378547,9.758147,8.804095,6.006676,0.225489,2.110627,-7.065367,-0.751323,4.229689,8.269456,-5.564893,-4.195723,-3.074453,-3.279481,7.871150,9.354039,-7.804126,2.628713,-4.621688,9.154793,8.608350,7.653044,7.484239,0.483787,7.190708,1.349421,-3.019130,-3.621069,2.608201,-1.343224,-1.514249,-4.219589,-1.417687,-8.878894,-2.626287,6.747838,-3.780435,4.494001,-9.159111,-2.810117,2.379038,1.156822,4.606115,-8.424032,-3.952018,-0.978439,5.758783,-3.381508,-7.494504,-0.478035,-2.732641,-7.951381,1.768550,8.311594,6.413533,8.352591,1.533012,-9.334479,-3.923127,-7.093979,3.891306,1.671533,8.457101,0.649986,-9.301617,-1.083785,4.120257,6.696837,3.909153,-0.329566,-5.714943,2.106157,-9.676045,2.565266,7.190719,2.547870,-2.113911,3.597588,-0.306117,5.575376,-4.865675,-6.739734,-3.595978,-7.541007,-5.004294,-1.206699,-8.532189,-9.637741,0.598441,-6.813349,7.761837,-3.584603,-6.917839,7.994515,-3.110327,-2.075952,0.551130,-1.943485,-5.435864,5.969679,9.465059,-8.577319,1.321953,-4.514771,-4.293985,5.202407,-9.211128,8.495761,8.638545,-1.939657,0.539408,1.399429,9.827743,-6.952731,-0.861969,-7.625537,-0.105203,-1.010255,7.922533,-4.361927,9.948652,-4.635094,4.031979,-2.615140,-7.869882,-2.790584,6.176861,-5.281913,3.047772,5.939675,-3.195801,7.478079,-7.908504,9.268132,-8.152930,1.738102,4.930294,-6.035600,2.216473,-7.925230,5.919662,2.594255,-3.977941,5.719952,-6.859041,2.216438,-1.241643,0.043922,-3.476404,-2.867132,8.054128,-7.899883,6.924548,0.321795,-1.021668,4.155536,1.118032,-8.984484,-7.192395,2.896961,-5.441032,-9.008078,-9.503672,7.001719,-7.300794,0.943068,6.793678,-5.106654,-2.852066,2.408438,2.390420,-7.188891,8.782847,-0.684088,-2.833057,9.712845,3.233144,7.835488,4.530461,-2.473248,9.402519,1.434068,-6.746043,6.941070,-4.503749,8.538672,4.989176,-0.096544,-0.851713,4.133132,-1.858473,-0.352141,-7.779833,6.670648,-9.272610,0.568901,-0.641251,5.360932,-8.541363,5.398696,6.239326,4.826099,1.785604,-8.974957,-5.682992,-8.145434,-8.089743,-6.291914,8.367381,-6.487052,-6.556293,0.749031,9.711623,0.266675,1.456321,-0.424828,1.230526,-3.999384,5.858459,-2.478875,-4.546254,-1.316889,3.792484,3.610840,6.633652,7.191863,6.394986,-4.333272,7.215270,-0.915323,-8.169938,8.266007,-6.834923,-8.971368,-6.541593,-8.519156,-1.160396,4.943575,1.108095,-2.347689,4.147064,-8.457607,-0.573891,2.980317,-2.700849,-2.704506,-9.078393,-0.299185,2.902307,-3.939829,-9.686785,-2.404716,9.394094,-4.990344,-4.441538,0.296268,-2.512465,-3.631424,-9.085481,-1.898410,-5.609943,-5.517046,2.348239,6.631184,2.621961,-7.805466,-1.346434,-5.224670,9.407555,2.953681,6.528020,3.945348,-2.991028,-6.305980,7.531979,-3.578416,-4.647851,-8.912375,6.255816,-3.786652,2.943327,-8.954680,-0.337136,0.321347,-2.930554,4.311695,-7.078887,2.483930,0.064241,8.622072,5.860657,-5.353601,-8.209332,8.333275,-3.217211,3.202059,-7.692058,-6.490788,-6.233122,-8.587313,-0.955504,0.536194,-8.561167,7.178622,-9.746921,-3.505880,-6.963555,2.521937,3.912994,6.253336,0.956911,2.084916,-4.722354,-8.824993,-4.405711,3.310573,-1.536228,9.553339,-5.854512,-1.598227,3.143115,-7.160802,5.833749,8.977410,-2.602765,8.644354,1.579123,3.459753,-0.312420,-0.621181,2.602108,3.420787,-9.404038,-7.165791,5.668737,-7.987192,-1.347147,8.996153,-8.298532,-9.375755,4.701776,-1.276728,0.849368,-8.298835,1.185423,-4.955261,4.291099,9.084437,-8.683738,-8.936176,-5.879521,-8.556999,0.874514,0.203460,-2.371274,-3.220374,9.409581,-2.906986,-7.800493,-5.910696,-1.214375,-8.727160,-1.802302,7.124555,-1.219645,-4.614053,-4.929506,3.924377,-2.035030,-2.876088,-1.885355,-1.574775,2.141616,-3.036536,-1.974541,-3.940438,3.561168,-5.237586,-9.130431,-1.547600,4.376263,3.469232,-0.575386,1.764712,6.312059,3.709138,-6.001134,4.039420,4.356465,2.020397,-4.693271,-6.611148,0.242692,8.668855,-5.275658,-0.622423,5.875112,-4.808834,-1.086695,-4.190559,3.729312,6.895588,-4.121516,3.849685,7.147740,4.135445,-2.112949,8.888477,-7.905010,6.309644,7.478135,-2.164386,-3.404762,-9.408421,-9.429780,-1.032631,-1.802691,5.622278,2.131819,-7.952178,9.887432,-0.082462,7.324245,7.495114,5.000455,1.972462,-0.304527,8.130647,-8.012191,0.880349,-8.599674,-1.653316,-4.776523,4.266765,-8.536384,-4.308336,5.814336,-8.924429,-9.084757,-2.999531,-3.783190,-8.453899,2.414032,0.328414,9.756731,-3.353209,4.411196,0.018549,-5.133848,7.675920,-4.334910,3.546429,-9.751130,0.362490,4.421826,-8.034844,3.808888,1.949850,-1.104052,-9.880124,8.575951,-6.037956,5.243661,-7.327650,-7.461247,-3.578568,1.041437,7.162108,0.552640,2.197773,-3.773649,2.209271,-9.809353,4.471312,0.009383,5.593621,-1.770840,5.571979,9.385385,-3.586963,7.038703,-0.305789,-1.117005,2.864294,-4.408962,-6.612500,-4.160894,-8.763583,-9.321033,-8.274147,0.223021,0.176855,1.099708,3.869965,-1.294108,-3.817112,3.179717,4.278651,-8.089952,3.875434,2.174631,-7.721364,0.116503,-2.579531,-3.154954,-0.234064,-0.559450,1.411722,-9.170726,-2.323726,-6.039741,8.578819,-2.527990,8.770165,0.470294,8.881672,0.730096,-4.975439,6.351370,-2.286372,4.057078,0.055032,-7.700039,8.879900,-7.066564,-2.782842,0.412197,-2.711471,-2.055600,-6.246144,-7.109915,-5.120414,7.669055,7.698417,3.370699,-1.798834,-3.243934,0.796951,0.607537,7.657022,-7.125894,-8.913907,3.580678,9.293178,6.024988,4.891809,-5.984864,4.296630,9.047077,-7.287065,-7.241892,0.352411,-2.774064,-9.023993,-2.189809,5.532071,0.747389,-2.677344,-5.024270,-0.455091,1.180794,-0.700984,7.348444,-4.214650,-7.406565,0.188059,3.852949,6.229632,2.653643,8.301957,8.962775,4.122768,2.880695,-9.948289,0.858820,2.189174,-1.270455,-5.160547,5.148646,-9.116819,5.749736,-4.767319,6.156930,9.051654,4.148270,-6.827620,8.037381,1.318909,9.503868,3.087364,-6.679167,7.287215,-9.241226,-4.841675,-1.635102,9.924584,3.517804,1.153979,7.091225,9.488610,0.459389,0.605844,7.801084,7.393980,-5.419837,-4.587530,3.226677,-3.868233,9.144221,8.793250,8.665114,-6.762270,6.664707,8.097979,-1.463472,8.540289,-7.443919,-0.146585,-3.694746,-6.186910,-4.794098,1.923649,0.269313,6.558578,5.920395,-1.343543,4.805479,3.055700,-7.893977,6.421537,2.414378,3.415339,-1.739690,-6.183694,9.221397,4.833357,3.323796,-4.542485,-7.162163,4.982193,-8.783784,5.482897,-8.257910,-7.560890,5.486176,6.845302,7.658535,1.027097,8.713809,-1.085474,-7.686656,-9.597976,-9.820492,-3.314716,6.138763,-0.861989,-9.730848,3.895608,-2.384285], dtype = "float32")#candidate|8859|(1470,)|const|float32
call_8858 = func_3486_call(relay.reshape(const_8859.astype('float32'), [14, 7, 15]))
call_8860 = func_3486_call(relay.reshape(const_8859.astype('float32'), [14, 7, 15]))
output = relay.Tuple([call_8849,call_8858,const_8859,])
output2 = relay.Tuple([call_8850,call_8860,const_8859,])
func_8863 = relay.Function([], output)
mod['func_8863'] = func_8863
mod = relay.transform.InferType()(mod)
mutated_mod['func_8863'] = func_8863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8863_call = mutated_mod.get_global_var('func_8863')
call_8864 = func_8863_call()
output = call_8864
func_8865 = relay.Function([], output)
mutated_mod['func_8865'] = func_8865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_8894 = func_4372_call()
call_8895 = func_4372_call()
func_8454_call = mod.get_global_var('func_8454')
func_8456_call = mutated_mod.get_global_var('func_8456')
call_8899 = relay.TupleGetItem(func_8454_call(), 0)
call_8900 = relay.TupleGetItem(func_8456_call(), 0)
func_2780_call = mod.get_global_var('func_2780')
func_2784_call = mutated_mod.get_global_var('func_2784')
const_8913 = relay.const([6.014797,2.660222,-5.066460,0.179419,-9.007824,-3.010570,-5.751154,-7.465559,7.800396,-6.814635,-6.152750,2.896601,3.563922,-0.980918,-4.557002,-5.047915,3.361991,6.401910,-6.785075,0.260145,7.586119,-8.447718,-1.522691,7.580655,-8.251242,-8.086180,0.595353,6.431048,-3.346099,-0.331163,1.709378,-9.637656,-6.861503,3.982959,-2.025797,8.094298,-8.594560,7.357905,-5.714334,-6.249925,-4.112872,5.213475,6.375801,9.735752,2.742798,-1.846643,-0.905905,4.646955,9.024672,-8.043419,-4.363305,4.304383,7.360005,8.132832,-7.283601,-4.799664,-2.740199,-6.526413,-6.837041,6.879430,8.687977,-6.434854,-3.402314,-2.017170,-1.461252,0.753199,-4.015969,-6.902443,7.377368,2.185354,7.863886,4.253160,-6.501626,0.835696,1.027980,-8.400384,1.226402,-1.111247,-1.082026,8.728596,7.847933,0.843374,3.920984,0.014397,6.066626,-1.354650,-8.929824,4.743182,-0.102038,1.166177,6.284973,-6.268896,2.816062,8.397647,-5.371914,-8.944143,1.695582,2.494001,5.185769,-6.409146,-9.855337,-3.425249,-4.326211,4.995453,-4.446849,-9.459133,-3.539709,-7.705083,0.903374,4.279027,-7.220939,-6.947739,-6.591902,8.734014,-3.440088,-7.338345,-0.804561,-7.535811,-8.355789,8.817680,-4.691528,9.591828,2.236372,-1.765988,7.122199,-5.207327,-8.877277,4.087888,-1.353529,-6.215988,-3.567807,5.357412,5.900552,7.633302,2.500566,3.977036,-9.844247,-5.225022,-4.901288,3.820004,5.049196,-4.356845,-4.947861,-6.459155,-8.838033,0.277553,5.362952,4.233192,-9.572151,4.915556,-8.697682,-0.058157,3.541183,-4.068059,0.534864,9.474558,2.736784,-7.445738,9.555134,-1.131627,-5.548121,9.597457,7.714465,-2.886397,5.687617,8.090473,-7.472999,2.948919,0.878603,-3.473182,4.808959,1.377740,9.726763,-8.724173,-8.815244,-6.369334,-3.037133,-0.515449,-1.531194,-4.790970,-1.951377,1.678359,6.131946,-8.241199,-3.064528,3.228487,-9.862372,-9.764461,7.042769,5.252005,-4.879835,-5.530331,3.557944,-9.198172,5.777434,9.593950,-2.525254,2.554481,6.855936,-8.898516,-0.718153,3.401312,-1.749306,-7.877889,-3.882418,8.770899,8.759569,-1.703838,7.719527,-1.156916,6.381678,-2.774731,4.956232,7.483985,-4.575656,-8.032099,9.662381,7.022396,-4.589106,9.059282,9.537901,0.881083,-8.994613,7.261883,-9.354702,9.504703,-8.196081,9.830879,2.762917,-9.806771,8.865559,-1.058061,1.083596,-6.666911,1.200186,-2.589315,3.815804,4.138178,5.506772,0.040708,-4.075645,1.012946,-9.471187,-8.347385,4.766854,0.003714,-1.892822,-1.424752,-9.344995,4.519787,-2.313692,-0.420803,6.393995,-9.360101,2.136373,-5.731532,-4.147878,-3.540641,-2.219252,-3.292436,0.608882,-3.156720,5.576724,1.998335,-1.910263,2.610009,9.416943,-3.470704,5.398276,3.563642,-0.441267,-0.164684,-5.851374,1.512803,-9.646700,-6.700926,-0.327302,0.376467,3.435043,7.320696,7.470150,3.267697,-0.270075,9.231732,-4.858273,-8.462560,-7.903777,0.180554,0.663840,3.750234,-1.052136,-0.437250,7.469304,-3.376861,-5.064431,-8.953410,-0.628477,-4.513674,1.138291,-4.047547,8.775820,-6.304552,2.057023,-9.543774,-2.963031,-8.233414,4.607809,0.553083,-0.917103,-9.434227,7.058114,-9.300256,-6.563752,4.942159,-4.394139,1.904223,-8.884826,8.169021,3.996687,1.402576,-8.821362,-2.835060,-3.758021,-8.724113,5.889893,8.836684,5.877757,-4.036180,2.057184,4.140447,8.361673,2.330766,-4.692028,5.827550,-6.755981,8.257026,9.734864,-8.760154,-2.929124,-2.476096,9.669738,-1.327628,-9.934424,-8.170804,-5.664796,0.389857,-7.037303,-3.392411,-6.313001,-5.627076,-1.638149,6.236178,3.720501,7.790010,-1.084261,5.837062,5.657436,-4.157200,-9.916502,0.144828,-9.852501,-7.031743,2.729521,3.413554,5.688111,-6.115223,5.800691,2.738703,-6.231130,-5.243660,-9.654003,-5.412803,-2.314332,5.928537,-0.644020,3.708332,-7.516391,5.057204,-7.784053,8.258675,4.944231,0.580610,1.150861,7.643252,9.805033,-3.302653,-3.890929,-4.521827,4.445173,6.693933,-3.688153,-4.924138,9.751530,3.801511,-4.602322,4.248144,-9.692720,-9.154923,8.678219,3.442948,-0.427744,-6.147146,3.215645,1.738493,4.463976,-5.378200,4.888572,-3.693548,-5.410561,4.956149,-1.605453,-2.345515,4.643385,-7.197304,3.283044,-3.067834,4.205381,-9.352417,7.096096,2.502581,-1.259613,-9.347269,-8.526341,-7.890932,-4.137807,2.768709,-3.419100,-4.969715,-0.724072,-0.752576,-9.839140,2.644099,-8.038189,-3.859855,9.604389,-8.243321,7.762517,-4.801144,7.024981,5.448530,-6.673071,-1.230544,-6.440641,-0.404102,3.707835,-4.477149,5.377831,5.534314,0.309882,6.273979,0.908331,1.180449,0.407804,-1.865817,-8.192362,-6.415705,-0.969316,-8.602583,8.430004,3.923106,1.363209,9.585122,-1.223019,-6.953257,-4.052651,-8.112381,7.257699,5.212248,5.081151,9.264685,9.013084,-9.173352,-4.013613,-5.312358,-0.726843,-7.744390,-0.797015,-8.533623,-9.011403,-8.727974,8.512048,-9.148980,-4.877124,8.345629,8.497869,-9.542895,-6.586157,-8.306220,7.021586,0.609792,2.092972,6.202942,6.552924,-7.628334,9.156383,-9.724559,6.752368,7.495446,-9.287447,-7.300152,-0.738645,-1.981448,4.705354,5.408753,-6.765315,-4.942589,9.941279,9.520032,-6.567414,-5.629775,-9.293043,-4.249094,-4.817176,-3.746369,-8.801641,-7.100187,1.196841,1.455315,-8.160174,1.826012,0.998949,-2.706618,5.634670,8.884487,5.142508,3.115894,1.603472,1.624603,-3.854507,-8.919729,-3.247205,0.764987,-6.117996,0.882476,2.848907,9.513476,-3.058829,4.406226,1.497548,4.135029,5.643952,-9.294837,-2.027179,-9.865716,7.523208,7.555175,5.573250,2.977164,-7.289665,-2.246087,8.560265,-5.295568,6.099078,-5.867046,0.095571,9.813651,-4.249202,2.178106,-5.455111,4.207821,-6.514836,4.339433,5.440991,9.197691,9.436431,-7.480325,1.056462,7.148896,-0.966574,4.579391,7.433850,-9.901351,5.052236,2.009929,9.682561,7.300486,3.958979,-8.536431,-5.364431,-8.533798,9.144045,-3.067984,-7.130395,-4.166147,8.504460,-4.572995,-9.601393,6.104566,-1.333450,9.350804,1.300786,4.451401,-9.301650,-8.420741,-0.333172,-7.399474,0.979494,-8.351435,-3.441953,-1.229590,3.575446,6.193846,-0.087132,3.069219,9.395180,-1.504560,1.795861,4.855975,3.362566,-7.056686,4.699066,-6.356598,-0.489292,-5.502640,1.603722,-5.479328,5.514677,-4.027239,-5.606378,-1.842445,8.835013,6.176333,-1.001534,-2.151408,-8.797201,1.127582,0.419580,-0.028468,0.792395,4.744179,7.248382,3.826837,9.212248,-2.759678,0.351845,1.297589,-4.832769,0.252914,9.544132,-6.786120,1.585108,1.617070,7.496706,-1.766909,-0.870058,6.035474,6.221569,-2.208630,5.760217,8.861013,6.305441,1.619692,5.827986,4.752712,-8.841083,-0.456094,6.425554,-1.318156,3.860773,4.939563,-2.024393,1.705910,3.539232,-8.708593,7.306913,6.279626,-6.715570,-0.924725,-6.955760,3.152899,1.480713,-9.343785,7.438812,-7.296488,4.192444,7.196561,-7.760420,6.656932,-4.459009,-3.857953,1.931739,6.511260,-2.451685,3.888851,1.053959,9.914864,-4.477097,0.420132,6.332528,-7.572596,-3.565465,-9.755456,3.173085,-6.728841,-4.034873,2.436166,9.593193,2.338915,-0.451002,-7.414216], dtype = "float32")#candidate|8913|(700,)|const|float32
call_8912 = relay.TupleGetItem(func_2780_call(relay.reshape(const_8913.astype('float32'), [5, 14, 10]), relay.reshape(call_8899.astype('bool'), [882,]), ), 0)
call_8914 = relay.TupleGetItem(func_2784_call(relay.reshape(const_8913.astype('float32'), [5, 14, 10]), relay.reshape(call_8899.astype('bool'), [882,]), ), 0)
func_5524_call = mod.get_global_var('func_5524')
func_5526_call = mutated_mod.get_global_var('func_5526')
call_8951 = relay.TupleGetItem(func_5524_call(), 0)
call_8952 = relay.TupleGetItem(func_5526_call(), 0)
output = relay.Tuple([call_8894,call_8899,call_8912,const_8913,call_8951,])
output2 = relay.Tuple([call_8895,call_8900,call_8914,const_8913,call_8952,])
func_8980 = relay.Function([], output)
mod['func_8980'] = func_8980
mod = relay.transform.InferType()(mod)
mutated_mod['func_8980'] = func_8980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8980_call = mutated_mod.get_global_var('func_8980')
call_8981 = func_8980_call()
output = call_8981
func_8982 = relay.Function([], output)
mutated_mod['func_8982'] = func_8982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6436_call = mod.get_global_var('func_6436')
func_6438_call = mutated_mod.get_global_var('func_6438')
call_9161 = relay.TupleGetItem(func_6436_call(), 0)
call_9162 = relay.TupleGetItem(func_6438_call(), 0)
output = relay.Tuple([call_9161,])
output2 = relay.Tuple([call_9162,])
func_9169 = relay.Function([], output)
mod['func_9169'] = func_9169
mod = relay.transform.InferType()(mod)
output = func_9169()
func_9170 = relay.Function([], output)
mutated_mod['func_9170'] = func_9170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5273_call = mod.get_global_var('func_5273')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_9226 = relay.TupleGetItem(func_5273_call(), 0)
call_9227 = relay.TupleGetItem(func_5274_call(), 0)
func_6964_call = mod.get_global_var('func_6964')
func_6966_call = mutated_mod.get_global_var('func_6966')
call_9231 = relay.TupleGetItem(func_6964_call(), 2)
call_9232 = relay.TupleGetItem(func_6966_call(), 2)
func_6407_call = mod.get_global_var('func_6407')
func_6408_call = mutated_mod.get_global_var('func_6408')
call_9241 = relay.TupleGetItem(func_6407_call(), 0)
call_9242 = relay.TupleGetItem(func_6408_call(), 0)
uop_9257 = relay.cosh(call_9241.astype('float32')) # shape=(14, 7, 9)
uop_9259 = relay.cosh(call_9242.astype('float32')) # shape=(14, 7, 9)
output = relay.Tuple([call_9226,call_9231,uop_9257,])
output2 = relay.Tuple([call_9227,call_9232,uop_9259,])
func_9260 = relay.Function([], output)
mod['func_9260'] = func_9260
mod = relay.transform.InferType()(mod)
mutated_mod['func_9260'] = func_9260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9260_call = mutated_mod.get_global_var('func_9260')
call_9261 = func_9260_call()
output = call_9261
func_9262 = relay.Function([], output)
mutated_mod['func_9262'] = func_9262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_9287 = relay.TupleGetItem(func_5054_call(), 2)
call_9288 = relay.TupleGetItem(func_5055_call(), 2)
var_9293 = relay.var("var_9293", dtype = "float64", shape = (39, 13))#candidate|9293|(39, 13)|var|float64
bop_9294 = relay.mod(call_9287.astype('float64'), relay.reshape(var_9293.astype('float64'), relay.shape_of(call_9287))) # shape=(39, 13)
bop_9297 = relay.mod(call_9288.astype('float64'), relay.reshape(var_9293.astype('float64'), relay.shape_of(call_9288))) # shape=(39, 13)
bop_9300 = relay.multiply(var_9293.astype('float64'), relay.reshape(call_9287.astype('float64'), relay.shape_of(var_9293))) # shape=(39, 13)
bop_9303 = relay.multiply(var_9293.astype('float64'), relay.reshape(call_9288.astype('float64'), relay.shape_of(var_9293))) # shape=(39, 13)
uop_9312 = relay.rsqrt(bop_9300.astype('float32')) # shape=(39, 13)
uop_9314 = relay.rsqrt(bop_9303.astype('float32')) # shape=(39, 13)
uop_9332 = relay.acosh(uop_9312.astype('float64')) # shape=(39, 13)
uop_9334 = relay.acosh(uop_9314.astype('float64')) # shape=(39, 13)
var_9335 = relay.var("var_9335", dtype = "float64", shape = (39, 13))#candidate|9335|(39, 13)|var|float64
bop_9336 = relay.maximum(uop_9332.astype('uint64'), relay.reshape(var_9335.astype('uint64'), relay.shape_of(uop_9332))) # shape=(39, 13)
bop_9339 = relay.maximum(uop_9334.astype('uint64'), relay.reshape(var_9335.astype('uint64'), relay.shape_of(uop_9334))) # shape=(39, 13)
func_8863_call = mod.get_global_var('func_8863')
func_8865_call = mutated_mod.get_global_var('func_8865')
call_9344 = relay.TupleGetItem(func_8863_call(), 2)
call_9345 = relay.TupleGetItem(func_8865_call(), 2)
output = relay.Tuple([bop_9294,bop_9336,call_9344,])
output2 = relay.Tuple([bop_9297,bop_9339,call_9345,])
func_9355 = relay.Function([var_9293,var_9335,], output)
mod['func_9355'] = func_9355
mod = relay.transform.InferType()(mod)
var_9356 = relay.var("var_9356", dtype = "float64", shape = (39, 13))#candidate|9356|(39, 13)|var|float64
var_9357 = relay.var("var_9357", dtype = "float64", shape = (39, 13))#candidate|9357|(39, 13)|var|float64
output = func_9355(var_9356,var_9357,)
func_9358 = relay.Function([var_9356,var_9357,], output)
mutated_mod['func_9358'] = func_9358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8058_call = mod.get_global_var('func_8058')
func_8060_call = mutated_mod.get_global_var('func_8060')
call_9384 = relay.TupleGetItem(func_8058_call(), 0)
call_9385 = relay.TupleGetItem(func_8060_call(), 0)
func_4535_call = mod.get_global_var('func_4535')
func_4539_call = mutated_mod.get_global_var('func_4539')
const_9389 = relay.const([[-3.593175,-7.951546,-2.606404,-9.765650,-9.850737,-0.302365,-6.552728,6.953682,-3.572201,-3.129766,7.652136,-7.526712,-6.112762,1.335572,7.686089,8.463525,5.214998,-3.627997,-9.728444,9.095983,-5.253051,2.430058,-1.226383,-4.878807,-0.168406,2.626528,1.181692,8.794152,2.756315,1.073554,7.074345,-5.744682,-8.208406,-0.504649,4.488886,-3.156135,5.819748,0.419469,-2.681116,-3.836789,-7.914845,7.271214,2.148557,4.980918,6.238191,6.226961,-5.322057,6.365536,-9.462501,5.470447,1.048263,5.162298,1.905250,-3.080380,-4.555287,-8.615203,6.491451,7.302425,-0.873748,6.147575,1.872092,-3.000155,6.854161,-9.333068,6.168105,4.539798,6.552044,1.380427,6.013823,4.027625,-8.745291,-2.628067,3.847186,-6.230275,7.459724,9.734023,-9.114367,-3.420889,7.580189,8.907426,-2.317396,2.755300,-3.827082,-5.308949,-8.423819,9.352695,7.760392,-4.169068,2.411964,2.600488,1.319004,4.296061,-4.711863,0.832472,2.128925,0.971386,1.142159,5.239952,0.651636,-5.287400,2.712549,2.930018,2.796307,0.319703,-6.574451,7.441225,2.425420,-4.132313,-3.852580,7.773407,-5.899907,0.979094,3.384155,1.596245,-5.657369,7.152215,-2.680926,5.883732,-1.879286,-5.351400,1.634908,-3.857859,2.056292,-5.012941,-5.491505,9.385613,-1.858299,4.662526,9.198241,7.246679,-0.241098,-1.397818,4.255837,-3.059937,-0.646812,-5.065216,3.425640,3.654955,3.481880,-8.199084,9.197440,1.421039,5.894279,-3.594924,4.506675,-4.121622,-7.644808,-1.654930,-1.501258,1.783669,-7.913084,-6.769209,5.700944,-1.603220,-1.577390,-9.954128,-2.491411,3.323385,-4.122677,-0.542980,3.937677,3.923484,6.749752,3.030953,8.618386,5.513992,3.259674,6.883937,2.010284,1.084885,-9.438480,9.559660,3.129463,-4.390982,-2.223206,-8.884232,-7.856550,6.662138,6.710079,4.361545,-2.044804,-7.205238,3.638604,-5.358525,5.454873,-2.076849,2.261415,-1.531762,-7.508773,5.826003,-7.491205,7.207355,1.528374,-0.392491,3.903739,0.239387,-0.840296,6.856729,4.548419,-9.536020,-0.867630,0.661141,7.312231,-8.814455,-1.671799,-3.611042,4.167418,9.378756,6.957817,-3.711293,-8.013562,-6.380308,3.124587,-7.090527,0.239786,-3.114091,4.689985,7.316288,4.902692,-4.296869,1.902669,-7.917297,-0.123269,-2.905539,-0.670472,9.279184,-0.676105,1.590799,3.808849,6.518449,4.146077,-3.950953,8.532447,2.685716,-4.551136,-4.736270,-6.411460,-7.462036,6.825997,-3.777789,6.396830,-4.174200,6.437645,-4.507456,2.480607,7.663078,8.439599,6.088949,-2.115884,3.225374,-8.933404,-2.745823,2.925202,-1.771360,9.337257,-9.081587,-5.679535,5.231016,-9.895349,-9.228441,5.594170,-9.362318,-7.757601,3.594309,-0.309695,6.215684,-6.810181,-8.828496,-7.255925,-0.605405,4.124823,0.488665,5.011884,-2.477130,-5.111263,2.006757,-7.919346,-4.686447,3.003115,3.225451,-5.853628,2.930311,9.097581,-6.210743,-2.577693,5.656036,1.455827,6.464426,8.562951,7.657323,-8.998701,5.074388,-3.159048,9.761310,3.609698,-5.951708,1.443887,1.444192,5.798030,6.916277,-0.024233,9.012897,1.164372,0.896283,-5.556822,-2.018947,4.532279,-3.425062,8.784454,-4.417000,-3.849020,-3.545829,-1.806453,-3.374998,-3.919941,6.571816,5.878815,-5.091337,2.047919,5.689321,-0.632294,-3.458300,-8.051992,-6.759992,2.080146,-4.611004,4.074163,5.779770,-9.234033,1.985053,1.121911,-2.740088,8.893994,6.192249,-0.470317,8.136986,-5.312405,-1.796832,-2.638265,-7.984303,1.612748,5.402398,-2.627421,-3.302930,8.308557,0.754489,-0.200104,3.745527,-6.886574,-5.642430,1.237069,-5.110778,-7.217785,-6.137739,0.047307,-2.357809,-0.498553,5.969966,-9.902093,5.945742,0.931976,0.499636,-5.999156,1.425878,3.254996,7.736093,1.462248,6.897741,1.467857,-6.922064,-6.473330,9.574422,2.601182,9.126443,2.090467,5.912743,7.160960,-7.307811,4.162068,7.441107,-0.042458,4.825405,-4.366497,1.387578,6.531057,-1.687834,-5.078497,-4.497662,-7.001722,7.461733,-6.475966,-2.116982,0.218539,-9.456860,-2.606453,-0.120275,-7.073790,4.011230,-0.597246,-8.026152,-4.576245,4.793954,9.611011,-9.950905,-0.470848,1.270273,-2.946641,-9.545042,-3.013158,-1.802838,-8.133637,2.307599,3.485921,1.144150,3.587862,3.449074,-6.546983,-3.404272,-3.519871,4.843886,6.358948,7.369557,-0.365830,3.678386,-3.315614,-2.958401,-3.924690,-9.295875,-7.572449,8.667573,7.457657,3.630157,-0.336513,6.013428,5.038523,7.172926,7.274616,-8.879680,-0.499767,1.330534,-9.382807,-6.886322,1.885552,-8.905152,-8.834672,-8.163185,-8.354982,-7.372940,6.324079,0.568838,-7.158003,9.648412,3.198684,-6.905423,-5.557514,8.804060,8.808038,4.109373,-2.363867,-8.294992,-7.524177,-0.155967,-1.536445,3.776982,1.196588,-0.994688,0.828391,5.344585,-4.839870,-7.465767,2.210962,8.198845,9.415556,-9.637054,-6.914315,9.828544,4.102579,7.905651,-9.684209,2.413016,9.121223,3.094317,-7.388479,6.094787,-8.134782,6.846648,7.340121,-2.246529,6.016021,-8.982322,7.244115,-4.114820,-7.725985,9.456627,-6.398108,-1.110035,-3.358834,-4.051960,-7.976404,9.222708,-5.720301,7.758404,9.478284,-6.996466,-3.108426,-6.118465,-4.632880,-2.497420,-3.048809,7.431979,-2.604679,-0.239500,-3.178398,4.216732,8.462420,5.913151,0.577279,2.659040,2.446888,-2.194174,8.002939,3.620802,6.984374,-3.566838,1.811467,6.088153,1.707692,6.926519,-2.789337,-9.988170,9.710795,9.837302,-3.456631,-2.524021,3.785437,5.168843,2.854194,-9.333069,-7.935560,0.815417,3.732799,-9.039506,-9.945396,-5.928981,-9.950240,-5.028093,-7.485251,3.045054,6.982979,-9.238987,-2.344563,1.660932,6.527198,-5.910640,-3.888841,3.148902,-8.991758,-4.993661,2.686277,-1.880665,8.565171,-6.518691,-4.784359,6.926264,3.901215,-5.172336,1.059611,8.950898,-1.218119,7.770987,1.960898,-4.732654,-5.376003,7.503027,1.677170,0.078212,-5.453294,-2.890470,6.718361,-9.371736,-1.205158,-3.069122,-2.982431,-7.114124,-1.933265,4.318490,-6.419603,5.134690,-0.647442,6.200937,-2.088822,8.655516,-6.998758,-2.641559,3.968268,-0.380908,7.456476,4.721094,-7.793695,-8.074244,2.059832,7.767045,6.929642,-4.849196,3.510315,8.991084,6.127841,-8.918873,4.210074,2.147105,-0.428050,-9.257142,9.686632,2.772160,3.028194,-5.388867,-6.197721,-0.858510,-3.309615,8.099005,-7.415111,-9.628341,4.300145,1.830127,0.133751,7.108441,-2.129726,3.958710,-6.936856,-2.036210,5.058129,-7.176382,-5.291066,7.526882,-4.505156,-6.645648,-1.068132,-7.393213,7.375301,-8.326522,-9.232585,-9.867240,4.073157,-4.172184,4.187048,2.447166,0.064848,-4.670971,-3.932941,1.741055,-0.437019,-5.110482,-3.533277,2.627155,-8.354152,-9.265375,5.453432,-4.484502,-2.886514,-0.183137,5.348901,-5.907178,-1.242689,-8.491477,2.652165,2.739077,8.063431,-5.173814,-4.120570,8.085359,2.241527,5.071311,0.849922,8.297074,7.632541,2.263275,3.959716,7.448538,-6.011056,-9.420805,0.597514,1.867874,2.576592,-0.155196,6.657839,7.578221,0.806858,-7.729195,-8.956949,8.215233,8.721096,-6.602610,-2.913929,-2.228055,2.738294,-0.754248,-8.666882,6.473294,9.661747,2.265613,4.107999,4.795544,-3.427685,8.927984,6.677237,-2.090102,3.738310,7.251903,-6.403070,-9.107495,7.619632,5.961345,7.959837,6.925697,-7.712991,9.428947,8.546370,2.458921,-5.841059,-6.373649,2.808077,8.887551,6.171063,-4.706330,-6.441396,6.009396,-2.879461,-2.580684]], dtype = "float64")#candidate|9389|(1, 728)|const|float64
const_9390 = relay.const([True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True], dtype = "bool")#candidate|9390|(882,)|const|bool
call_9388 = relay.TupleGetItem(func_4535_call(relay.reshape(const_9389.astype('float64'), [728,]), relay.reshape(const_9390.astype('bool'), [882,]), ), 6)
call_9391 = relay.TupleGetItem(func_4539_call(relay.reshape(const_9389.astype('float64'), [728,]), relay.reshape(const_9390.astype('bool'), [882,]), ), 6)
func_8454_call = mod.get_global_var('func_8454')
func_8456_call = mutated_mod.get_global_var('func_8456')
call_9397 = relay.TupleGetItem(func_8454_call(), 0)
call_9398 = relay.TupleGetItem(func_8456_call(), 0)
uop_9402 = relay.log(call_9384.astype('float32')) # shape=(39, 13)
uop_9404 = relay.log(call_9385.astype('float32')) # shape=(39, 13)
uop_9405 = relay.log2(call_9384.astype('float64')) # shape=(39, 13)
uop_9407 = relay.log2(call_9385.astype('float64')) # shape=(39, 13)
output = relay.Tuple([call_9388,const_9389,const_9390,call_9397,uop_9402,uop_9405,])
output2 = relay.Tuple([call_9391,const_9389,const_9390,call_9398,uop_9404,uop_9407,])
func_9408 = relay.Function([], output)
mod['func_9408'] = func_9408
mod = relay.transform.InferType()(mod)
mutated_mod['func_9408'] = func_9408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9408_call = mutated_mod.get_global_var('func_9408')
call_9409 = func_9408_call()
output = call_9409
func_9410 = relay.Function([], output)
mutated_mod['func_9410'] = func_9410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_9530 = func_5303_call()
call_9531 = func_5303_call()
func_2780_call = mod.get_global_var('func_2780')
func_2784_call = mutated_mod.get_global_var('func_2784')
var_9536 = relay.var("var_9536", dtype = "float32", shape = (700,))#candidate|9536|(700,)|var|float32
var_9537 = relay.var("var_9537", dtype = "bool", shape = (882,))#candidate|9537|(882,)|var|bool
call_9535 = relay.TupleGetItem(func_2780_call(relay.reshape(var_9536.astype('float32'), [5, 14, 10]), relay.reshape(var_9537.astype('bool'), [882,]), ), 0)
call_9538 = relay.TupleGetItem(func_2784_call(relay.reshape(var_9536.astype('float32'), [5, 14, 10]), relay.reshape(var_9537.astype('bool'), [882,]), ), 0)
uop_9544 = relay.sin(var_9536.astype('float32')) # shape=(700,)
func_7364_call = mod.get_global_var('func_7364')
func_7367_call = mutated_mod.get_global_var('func_7367')
const_9548 = relay.const([[6.327526],[1.702629],[-0.509671],[-7.476816],[-6.083929],[-3.798386],[3.591677],[7.636003],[0.741958],[-0.440766],[-3.757474],[5.063673],[6.435353],[9.635686],[-9.102727],[-3.607417],[9.415128],[6.198598],[4.672871],[-1.597217],[-7.916179],[-0.255548],[5.140459],[-8.706146],[8.901138],[2.753621],[-7.483731],[0.665516],[0.450668],[5.977916],[4.587330],[8.142627],[8.935572],[-7.212586],[2.365118],[-8.463593],[5.023502],[5.298327],[-9.381723],[2.097789],[-7.954692],[-1.217762],[-4.968723],[-7.026380],[-7.366283],[2.350958],[8.147487],[-7.007564],[-2.441489],[7.018192],[6.859739],[9.125588],[-8.969040],[-2.412857],[-2.617019],[-8.906286],[-0.375597],[7.276251],[7.521441],[4.681768],[7.438312],[6.878583],[4.461467],[-5.785429],[-4.032396],[9.984869],[4.413312],[8.881832],[9.610780],[3.693305],[1.194865],[-4.668656],[-3.820179],[-7.873688],[8.309456],[5.527927],[6.771759],[7.005238],[-7.438439],[-8.798271],[3.343976],[-3.104654],[-3.312827],[8.962779],[8.543046],[9.507562],[-2.132551],[5.011220],[-2.307542],[-3.672698],[4.931227],[-5.590120],[-1.386885],[8.600681],[7.796673],[-3.430406],[-2.158315],[-8.036966],[-1.364390],[-3.370904],[-9.349949],[-9.833221],[-6.439660],[6.858062],[-5.050020],[-9.438873],[3.158281],[-4.024401],[0.070527],[-2.641686],[0.581906],[3.306131],[2.964372],[-8.035455],[7.213498],[-6.110292],[-2.010451],[7.702950],[-8.571340],[1.301560],[-3.329934],[-2.814431],[5.482344],[-3.765943],[-5.847533],[6.393801],[6.692618],[8.545352],[-9.809738],[-3.479533],[6.636129],[7.034770],[6.511418],[-9.492806],[7.189706],[-9.475780],[1.507872],[1.648116],[9.926349],[5.765278],[-5.262102],[9.776533],[-5.799557],[9.737886],[-5.718526],[-7.900634],[-2.532819],[-2.527192],[-0.938247],[7.364982],[-6.809413],[-7.063974],[-0.322048],[-9.256132],[1.226531],[7.394240],[9.035844],[3.588371],[-1.839311],[-3.268684],[-5.312089],[-7.755945],[7.959098],[-7.130057],[9.625733],[0.424486],[-2.930352],[2.698878],[-4.961891],[-5.678070],[-0.212339],[0.096726],[7.161919],[6.438330],[3.663665],[-8.353534],[-5.196381],[-7.694091],[8.073991],[-3.181484],[-8.417360],[3.398880],[2.476667],[3.695816],[-8.523198],[6.338320],[-9.641738],[-5.147629],[4.870935],[8.430463],[-6.790942],[-9.556963],[-3.901933],[-9.349594],[4.347849],[-6.676742],[-7.302989],[-4.236909],[-5.764326],[2.545825],[-9.623360],[3.995334],[-5.137112],[-5.977089],[4.199324],[-1.712249],[8.937018],[2.520976],[-3.657598],[-2.863123],[-9.685902],[8.048278],[-1.070672],[-0.991594],[-5.432844],[5.705279],[-7.331346],[1.369085],[1.555731],[-7.291098],[6.578736],[-2.830721],[3.386313],[-0.866197],[3.571688],[9.673961],[3.463301],[-1.176977],[1.320980],[-9.782804],[5.208856],[-0.285924],[5.698277],[-6.351623],[7.658992],[8.043534],[8.529172],[6.890919],[6.518328],[-6.784280],[-9.646833],[-3.176923],[5.566626],[5.597429],[1.147230],[-8.853018],[-9.125911],[-4.792575],[-1.015025],[-9.027919],[7.778055],[-7.310723],[8.056280],[4.967543],[0.674937],[0.268608],[-5.752756],[8.692098],[-7.921696],[-1.566637],[-3.512866],[-6.221399],[2.460540],[-4.549799],[8.517621],[1.264480],[6.025549],[-4.512856],[1.055796],[5.310113],[8.955802],[9.644142],[5.022232],[6.390834],[6.405795],[4.643171],[-5.889736],[-0.337813],[1.949420],[8.821433],[3.624696],[8.084295],[-3.289265],[6.394010],[-0.193097],[-3.706510],[7.383440],[5.695808],[-0.530659],[3.227229],[-3.330923],[-3.314548],[-3.950580],[-4.552109],[8.904581],[8.256010],[-2.099179],[1.639249],[-4.526887],[-9.631637],[-3.838658],[-6.676289],[-6.420652],[-6.320556],[2.592007],[2.472001],[-8.729100],[-3.970808],[-8.252195],[-7.003110],[0.040859],[9.686049],[1.087133],[-8.088403],[9.637577],[-7.040113],[-3.898219],[-1.994288],[-4.709827],[0.429651],[-1.433500],[5.085455],[-4.368628],[3.998799],[-0.626093],[2.225954],[2.760064],[6.964792],[0.141039],[-9.778489],[-6.650101],[-1.806350],[-3.719284],[-6.927802],[4.636549],[-6.898944],[-2.391237],[9.109290],[2.403086],[2.405978],[-7.489921],[3.330410],[9.218782],[-6.599152],[3.981305],[-0.675260],[1.754218],[-5.137368],[9.168772],[-3.250865],[-0.969762],[-3.031846],[-9.700018],[-5.444737],[-1.471404],[8.240082],[-8.344512],[3.114421],[3.265688],[-1.416563],[-9.192323],[3.110240],[-3.288739],[7.990012],[-5.306447],[-1.791317],[-7.775745],[5.500521],[-2.349528],[3.485221],[5.230827],[-8.194504],[5.959639],[-4.409540],[3.313282],[3.209807],[8.798170],[-0.255281],[-7.156877],[5.376882],[2.933288],[-8.374342],[-3.396199],[0.671582],[7.320100],[5.772089],[4.064799],[-6.002198],[5.355580],[-6.880387],[2.695672],[4.315108],[-3.480982],[-5.532145],[7.020788],[0.847418],[-1.271520],[3.574324],[9.605955],[9.478652],[0.349433],[2.011927],[-1.411008],[8.501455],[-7.048642],[8.839897],[-1.131505],[-5.592714],[-8.951801],[9.507791],[-2.810319],[-1.557758],[-2.578360],[0.537168],[-2.976659],[-5.064552],[-7.072272],[1.642688],[2.258495],[-0.287549],[-5.972896],[-6.687968],[-8.463408],[3.998205],[9.288576],[7.882190],[9.718248],[-4.978868],[1.245434],[6.388861],[7.771713],[2.154670],[8.520675],[-6.576321],[5.613793],[5.405101],[-2.948649],[-4.206765],[-9.978684],[1.794769],[5.765921],[-1.138109],[3.086067],[-8.759414],[-8.209484],[-8.205843],[-6.948769],[6.423917],[-0.082526],[-5.115646],[2.795238],[2.609467],[3.001776],[-8.609794],[9.736603],[-2.555461],[-0.871094],[4.479893],[7.075786],[-0.018484],[5.540506],[4.924039],[-2.875246],[-5.746301],[8.056069],[8.111542],[-4.357101],[-5.726369],[-1.418864],[4.868269],[2.623055],[-3.885035],[-9.457803],[7.069947],[-7.325611],[-7.911071],[-5.875510],[1.602389],[-5.205471],[-5.663829],[-4.967820],[-7.022822],[-3.961904],[7.681022],[-8.432316],[4.408479],[-6.985026],[4.684630],[1.181219],[-4.178615],[6.287329],[-9.453906],[4.598164],[-5.630222],[5.648096],[2.804337],[-0.521197],[-4.351941],[-2.528214],[-0.516135],[-7.399122],[-7.470322],[8.739483],[-4.366733],[-2.361274],[-8.586027],[8.700119],[-5.300473],[-2.088566],[-0.666395],[0.444908],[-6.414539],[-7.269847],[-8.014458],[-9.248659],[3.610529],[-6.385429],[4.238583],[9.067330],[2.717876],[-6.815582],[1.220059],[-6.953415],[-3.975712],[4.824184],[-2.680175],[-1.349343],[-4.394608],[8.822617],[-2.125865],[5.074486],[-3.230254],[5.012730],[-5.127136],[7.643317],[5.598651],[4.705342],[7.210932],[-3.897961],[6.028778],[9.671561],[-2.871181],[-7.534005],[-3.691786],[5.107779],[0.352131],[-8.270739],[3.720876],[2.872877],[-8.925040],[0.320196],[-2.196861],[4.428438],[-4.562010],[-8.742009],[8.745464],[4.158727],[9.077018],[-3.385993],[8.842023],[-4.389589],[5.612088],[-2.355398],[7.185200],[-9.945348],[9.054324],[2.272226],[-9.794882],[1.064841],[-8.090058],[-3.929339],[9.101431],[7.299990],[6.609662],[-8.262983],[6.941743],[8.498211],[2.812490],[8.071601],[2.107365],[2.991293],[4.644806],[5.702477],[8.009892],[-8.978150],[-5.037047],[0.523590],[-8.198230],[-4.122917],[-7.373250],[-8.234527],[-9.349635],[-8.711077],[-4.284701],[-0.651600],[8.235016],[-5.942987],[-6.724717],[6.285414],[-5.978095],[6.650462],[-6.093852],[2.204371],[0.844483],[9.237698],[-8.273689],[2.873551],[3.386050],[7.615711],[-6.425606],[-0.998232],[2.808919],[-3.394073],[-3.752401],[4.636977],[-0.805837],[6.536689],[3.699486],[9.531666],[-9.212011],[-8.094445],[6.839119],[1.472150],[-0.749472],[-0.954170],[-9.072422],[-0.562259],[1.103857],[1.177036],[-2.163252],[-1.099738],[0.721712],[-2.581004],[-6.494063],[7.370642],[-2.740765],[-0.168647],[-3.981866],[-8.422010],[-8.745935],[1.100425],[8.798155],[-7.673703],[-9.974450],[-5.459362],[-2.906522],[1.545427],[-7.656423],[-6.924656],[-5.284713],[-4.314519],[5.859834],[-8.343644],[-9.684206],[-4.074451],[8.560654],[-9.101160],[-7.076919],[3.680368],[-1.001408],[9.429137],[-7.924367],[0.394697],[-8.978574],[-9.451375],[5.051678],[2.604876],[8.296650],[-1.509110],[5.656424],[-9.773143],[-1.406505]], dtype = "float64")#candidate|9548|(672, 1)|const|float64
call_9547 = relay.TupleGetItem(func_7364_call(relay.reshape(const_9548.astype('float64'), [336, 2])), 4)
call_9549 = relay.TupleGetItem(func_7367_call(relay.reshape(const_9548.astype('float64'), [336, 2])), 4)
bop_9562 = relay.add(uop_9544.astype('float32'), const_9548.astype('float32')) # shape=(672, 700)
bop_9567 = relay.logical_and(const_9548.astype('bool'), uop_9544.astype('bool')) # shape=(672, 700)
output = relay.Tuple([call_9530,call_9535,var_9537,call_9547,bop_9562,bop_9567,])
output2 = relay.Tuple([call_9531,call_9538,var_9537,call_9549,bop_9562,bop_9567,])
func_9580 = relay.Function([var_9536,var_9537,], output)
mod['func_9580'] = func_9580
mod = relay.transform.InferType()(mod)
var_9581 = relay.var("var_9581", dtype = "float32", shape = (700,))#candidate|9581|(700,)|var|float32
var_9582 = relay.var("var_9582", dtype = "bool", shape = (882,))#candidate|9582|(882,)|var|bool
output = func_9580(var_9581,var_9582,)
func_9583 = relay.Function([var_9581,var_9582,], output)
mutated_mod['func_9583'] = func_9583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8363_call = mod.get_global_var('func_8363')
func_8365_call = mutated_mod.get_global_var('func_8365')
call_9609 = func_8363_call()
call_9610 = func_8363_call()
func_6436_call = mod.get_global_var('func_6436')
func_6438_call = mutated_mod.get_global_var('func_6438')
call_9624 = relay.TupleGetItem(func_6436_call(), 0)
call_9625 = relay.TupleGetItem(func_6438_call(), 0)
uop_9630 = relay.asinh(call_9609.astype('float32')) # shape=(14, 7, 9)
uop_9632 = relay.asinh(call_9610.astype('float32')) # shape=(14, 7, 9)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_9635 = func_4372_call()
call_9636 = func_4372_call()
output = relay.Tuple([call_9624,uop_9630,call_9635,])
output2 = relay.Tuple([call_9625,uop_9632,call_9636,])
func_9662 = relay.Function([], output)
mod['func_9662'] = func_9662
mod = relay.transform.InferType()(mod)
output = func_9662()
func_9663 = relay.Function([], output)
mutated_mod['func_9663'] = func_9663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5245_call = mod.get_global_var('func_5245')
func_5246_call = mutated_mod.get_global_var('func_5246')
call_9669 = func_5245_call()
call_9670 = func_5245_call()
func_3994_call = mod.get_global_var('func_3994')
func_3999_call = mutated_mod.get_global_var('func_3999')
const_9680 = relay.const([[8,10],[-3,7],[7,-10],[10,-8],[-4,4],[9,5],[-4,2],[-8,6],[10,-10],[-5,4],[-4,-2],[6,9],[-3,1],[2,-3],[4,10],[8,10],[1,3],[-6,-9],[-1,-3],[5,8],[5,-7],[-7,3],[-8,7],[-8,5],[6,-5],[-7,5],[9,7],[-9,1],[-8,1],[1,-9],[5,-6],[-3,-2],[1,3],[6,-7],[5,-9],[1,-8],[-10,-4],[-3,1],[-9,2],[-10,-2],[4,10],[-5,-6],[-3,5],[-7,-2],[-6,-6],[-1,8],[4,5],[4,6],[5,9],[6,-10],[-10,-2],[-2,2],[1,4],[4,6],[-1,3],[-6,-5],[-6,-1],[-8,1],[6,3],[-8,-3],[-2,2],[10,-6],[-7,-8],[8,6],[-6,8],[7,-3],[3,-10],[-10,9],[-3,-10],[9,4],[4,10],[5,-10],[2,8],[9,4],[-5,2],[-9,-1],[-2,-5],[-8,-8],[5,8],[4,3],[-8,-7],[10,9],[-8,-5],[4,9],[-7,-8],[7,9],[1,-2],[-5,-3],[5,2],[-1,-3],[3,-6],[-5,2],[1,-9],[5,-10],[5,-3],[6,5],[-6,-7],[7,-6],[1,7],[6,8],[-1,-8],[6,3],[8,4],[-2,5],[6,-4],[3,3],[-1,8],[2,-7],[-4,9],[10,1],[-8,2],[-6,5],[-9,4],[9,6],[10,7],[1,-4],[8,-4],[3,-6],[2,10],[-7,7],[6,-9],[-1,-4],[8,-10],[7,3],[7,-4],[3,-3],[10,-3],[10,4],[-3,10],[-8,2],[8,-5],[8,-10],[7,7],[-4,7],[6,2],[1,-4],[10,8],[-10,4],[-6,3],[-10,1],[7,-7],[8,8],[5,-2],[7,-1],[-9,5],[-1,7],[1,-1],[5,8],[10,6],[1,-4],[3,1],[1,6],[-10,9],[-1,1],[10,-3],[-6,8],[6,3],[-7,2],[-4,-9],[6,5],[6,9],[4,-9],[2,9],[3,-3],[3,-6],[5,-10],[2,6],[-7,-6],[-8,-10],[5,-5],[3,6],[-3,-7],[-6,-7],[-3,-2],[8,-5],[-10,8],[5,8],[-9,-8],[9,10],[-4,-8],[-2,-3],[-4,1],[4,7],[-8,4],[4,5],[7,8],[1,9],[7,-6],[-4,5],[8,10],[-4,8],[3,-7],[-3,10],[8,-7],[-8,-4],[4,5],[3,-6],[5,-2],[4,-1],[3,-1],[2,8],[1,-1],[-2,5],[7,5],[-9,-8],[8,3],[4,-8],[4,5],[3,8],[-1,-3],[1,10],[-10,-7],[-8,3],[-7,-8],[10,7],[-5,10],[8,-2],[-4,-1],[-6,5],[7,-3],[7,1],[-2,-4],[-2,6],[5,-7],[-3,-1],[5,6],[-6,5],[4,-10],[-6,6],[9,10],[-3,1],[2,3],[7,6],[10,3],[-4,-1],[10,9],[2,4],[7,5],[10,-8],[-5,10],[6,4],[-8,2],[-7,10],[4,-5],[-7,2],[-5,-2],[4,-9],[-4,1],[-7,-6],[3,-6],[-2,-2],[-6,-7],[-6,-6],[5,-7],[-1,-9],[7,3],[-8,2],[-8,6],[7,-6],[-4,5],[-1,2],[1,6],[8,-5],[9,1],[-8,9],[-1,5],[2,10],[-6,8],[8,-3],[9,-10],[-9,2],[-2,3],[7,-7],[-8,8],[-6,6],[5,-9],[-3,-3],[6,-9],[-6,-10],[5,-2],[7,3],[-4,7],[-1,-1],[-8,3],[-7,-6],[-8,5],[-8,-6],[-8,7],[8,3],[5,1],[3,-2],[6,-4],[2,3],[5,-7],[3,-7],[-4,8],[-8,-3],[1,7],[-9,6],[-6,8],[10,-9],[-1,7],[-10,7],[-1,-5],[6,-10],[-3,2],[7,7],[10,-3],[-9,3],[-9,-2],[-7,4],[-3,-6]], dtype = "uint64")#candidate|9680|(312, 2)|const|uint64
var_9681 = relay.var("var_9681", dtype = "float32", shape = (1470,))#candidate|9681|(1470,)|var|float32
const_9682 = relay.const([[-2.813508,-6.713586,6.495236,6.547034,4.852731,5.247666,-8.911030,7.103296,4.671208,9.872324,5.524475,-0.550145,-5.293662,5.696181,-2.166807,5.485964,-5.379325,3.535081,6.117357,5.213825,-6.211533,9.313217,-8.192120,8.656992,-3.422075,3.827539,-0.430749,1.890527,-6.806411,9.323326,-8.933484,5.387619,3.802352,-2.127187,7.966041,7.566288,-7.386349,1.818604,6.959816,4.416982,4.292863,9.751978,-2.853663,-9.648010,9.247418,-1.974900,-5.948763,3.851054,-7.197402,-4.246490,3.690528,-9.149807,-4.687397,-1.699599,-6.668126,-9.892613,4.281625,-9.742205,-9.190001,-7.492480,-1.810705,5.094315,-9.444773,-4.160500,3.196211,2.250834,-7.868277,-3.485023,2.740927,-2.766871,-3.168218,9.487499,-5.806264,-5.574317,1.842423,2.030665,0.356477,-1.011257,8.449536,-5.375833,-8.919691,8.716373,2.947676,3.920980,7.084707,8.310414,-7.051230,3.206711,-5.496146,0.556674,-0.696652,8.067748,-4.684053,8.853047,1.702321,-9.796022,7.978745,-3.621330,7.317972,3.511766,-8.771171,3.435220,-0.827236,9.461825,-5.836774,-5.982037,3.553834,-7.775461,9.419598,1.682654,3.933114,-0.549428,-4.202477,-7.932301,8.793988,-9.105387,-8.250094,-6.136758,-3.716020,7.933183,4.783358,2.078357,4.323351,-4.283196,6.153288,1.383512,3.739755,-7.448720,1.603750,5.706024,-0.176653,-8.282922,7.312784,7.095959,-1.655582,-1.277104,-4.461955,7.585453,7.896160,9.362594,7.827495,-6.922334,-9.074326,-8.518927,0.514717,-7.530729,5.084402,-2.082958,-0.701254,-5.977611,-5.035832,-6.700476,-0.887347,-5.505246,4.410286,4.471596,7.356677,8.462806,-8.555156,4.170990,4.555598,9.507086,-7.512836,-6.410519,-3.890985,3.338547,7.201338,2.376426,6.497680,-9.112859,4.587377,-7.837095,6.321339,3.201754,0.631630,2.511615,-5.657849,-8.739810,-4.110618,1.869012,2.117369,8.729699,-0.509421,8.680854,-2.733705,-8.245865,4.573046,-4.820720,-0.742280,-9.636430,-3.712107,5.697739,-6.105209,6.975608,-2.194280,2.159229,-3.765132,-8.950191,-6.277724,-9.533506,6.414756,-4.011987,1.729990,8.522187,-3.260709,-6.632901,2.914519,-1.085348,1.946994,-2.717056,-4.910926,8.966084,-4.826468,-1.972788,5.610588,-3.269068,9.878858,3.521747,0.970647,8.256816,-7.659515,4.500919,6.834787,-4.280576,7.748807,-4.750507,-8.564767,-2.516775,5.925582,9.611942,-7.606804,-4.464686,8.361317,-4.971190,-1.364348,-8.421123,3.081523,8.234819,6.876284,1.613106,-7.269449,0.665587,-0.549393,-3.136918,-0.734532,-5.319236,8.079189,-6.543131,7.948689,9.494759,-6.844340,-9.250176,4.673908,-6.973132,3.316641,-8.891047,8.757756,9.056783,7.460196,-8.683985,4.217390,-5.404819,0.268021,4.489086,-5.534595,-6.313779,4.641486,-2.796792,-2.450400,9.139527,4.182537,-8.551987,7.599628,-1.910586,2.160301,-9.707388,8.842502,3.143781,-0.632510,4.511002,1.559357,7.596450,5.640975,-8.641849,2.790380,1.738169,6.989642,8.877654,3.536629,5.204675,-5.275615,-6.026917,5.732219,-8.735689,-2.162411,-7.864415,-8.659678,-9.493022,4.548038,9.204934,3.688666,8.807186,-1.694665,6.290203,-1.814012,-3.863030,0.847699,6.852061,-9.587545,-3.999804,0.018338,1.978223,-8.142392,6.958049,-9.812971,-2.480059,-2.981651,-3.256726,8.207392,-9.893806,-9.820990,-6.224194,6.842273,-1.408034,-6.004847,6.967746,8.941919,4.198541,-1.326755,-0.747135,0.714656,-5.062317,-7.167421,3.129639,1.361168,-2.958795],[-8.314398,2.423987,-7.562710,-6.525237,-9.596419,-1.925409,-8.638580,5.779229,7.651519,8.267225,4.335107,-2.649990,-4.525370,0.540696,8.041298,2.496324,-2.341686,-9.134031,2.036986,9.134655,-5.217253,8.626369,6.912587,7.035941,-9.249334,-4.494437,8.213127,-0.251694,-1.893390,3.499691,8.448091,2.237630,3.142126,-2.963135,-9.413763,-2.935619,1.781795,5.075085,-5.933037,0.976355,0.997329,-3.973978,-1.394513,-6.495389,-2.245056,6.207926,9.731705,-8.354604,-9.180102,9.006565,-1.234885,1.497188,0.946287,3.858037,7.946106,7.012424,-0.446392,6.525557,-0.224972,6.967908,4.256766,-3.289717,7.730761,9.523428,8.108268,1.829837,-1.841577,2.738375,8.017194,-5.842435,-4.341079,-5.984147,3.560010,6.704867,2.844250,0.180350,0.255847,3.720537,-0.003273,-7.086913,3.631926,9.294849,-3.394223,-3.772536,4.980856,1.607219,-9.344361,-8.145619,6.262009,6.712877,-1.721864,-4.693461,-5.761607,0.414440,-8.645038,-8.807929,5.141793,-2.397193,-7.386754,9.762925,2.254097,3.092376,-6.734677,2.876945,-2.814664,1.710634,5.062969,-6.872104,6.304565,-7.855871,-3.962290,-0.012427,4.371156,0.634447,8.996305,3.779109,1.979997,-6.172138,4.114452,-9.990882,-0.999554,-2.410554,0.113561,3.344347,-8.131214,-9.639742,-9.580474,-3.462249,1.198915,0.006191,5.269569,4.138130,-5.002749,-6.587098,-2.939838,7.857355,-9.065642,-5.763692,-4.169571,8.790510,-5.854869,1.295550,-4.744336,-5.385799,-6.002704,-1.549569,-2.725652,-1.091762,3.220417,-3.122262,2.723147,-5.452758,-0.874195,8.318304,-4.591407,0.608848,8.032151,6.533205,0.031911,6.004608,7.156698,2.711927,-3.786081,-0.254092,-0.074399,7.245296,-0.275154,-8.178948,-5.295323,-3.519106,-3.846185,0.326873,-7.380798,0.584309,-9.816375,8.892924,-2.178408,-3.355468,1.939865,-7.771049,0.842584,7.909666,0.962533,-2.509197,-0.705490,-3.622403,7.881019,-7.367576,-1.558096,4.747367,-3.016247,-7.388299,6.226430,9.211815,-1.441046,-5.612083,8.524384,1.397710,8.629247,5.247203,-5.354813,-8.601220,9.449447,-1.994591,-3.666405,1.566567,-4.530630,8.482548,-4.569183,-7.443705,-1.784813,-0.433195,1.508140,-8.717572,-3.752166,-7.350112,6.260694,-1.525348,4.272785,-0.765508,-9.130026,-0.383450,-9.512970,-1.974884,1.608818,9.450351,6.428561,7.067860,5.305054,-9.484133,4.365068,2.546552,1.093011,-1.526949,-2.404311,5.595278,-1.108498,6.753377,3.836180,4.367411,6.037346,6.292738,-2.796332,3.715035,-9.659367,3.440068,-3.955066,7.087611,-5.563876,-1.655820,-3.098987,1.831968,3.525435,3.022955,-2.075027,7.302477,2.607128,2.082280,-0.915843,-5.162755,-1.060811,-5.598193,-7.213519,-2.307274,3.563049,2.984337,-0.561294,-7.320818,5.301010,8.981713,-8.475232,8.861523,5.236257,-2.432232,5.049534,-7.758625,-6.281897,-5.261904,-4.497131,-7.943612,1.926508,-8.260914,-1.097517,-7.944392,-2.465243,-5.733179,-8.635076,7.723327,-8.930780,3.888170,-1.296257,5.627840,3.840507,2.587508,-0.081279,8.968057,7.661753,-4.371633,9.432640,2.348784,-8.991865,-5.596676,-7.128484,-4.301352,7.131937,-2.898462,0.902805,4.090883,-4.860709,0.760506,-9.506727,-3.284156,-5.876462,8.793684,2.682526,3.235276,-0.467000,9.511102,0.643393,7.383450,9.972685,-6.755051,7.817035,9.419163,-4.306211,1.191292,-2.210468,-6.726606,-7.018073,-1.278113,6.692559,4.103377,7.088725,-1.528928,-0.462562,-2.977886]], dtype = "float64")#candidate|9682|(2, 336)|const|float64
call_9679 = relay.TupleGetItem(func_3994_call(relay.reshape(const_9680.astype('uint64'), [4, 12, 13]), relay.reshape(var_9681.astype('float32'), [7, 210]), relay.reshape(const_9682.astype('float64'), [168, 4]), ), 3)
call_9683 = relay.TupleGetItem(func_3999_call(relay.reshape(const_9680.astype('uint64'), [4, 12, 13]), relay.reshape(var_9681.astype('float32'), [7, 210]), relay.reshape(const_9682.astype('float64'), [168, 4]), ), 3)
output = relay.Tuple([call_9669,call_9679,const_9680,var_9681,const_9682,])
output2 = relay.Tuple([call_9670,call_9683,const_9680,var_9681,const_9682,])
func_9693 = relay.Function([var_9681,], output)
mod['func_9693'] = func_9693
mod = relay.transform.InferType()(mod)
mutated_mod['func_9693'] = func_9693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9694 = relay.var("var_9694", dtype = "float32", shape = (1470,))#candidate|9694|(1470,)|var|float32
func_9693_call = mutated_mod.get_global_var('func_9693')
call_9695 = func_9693_call(var_9694)
output = call_9695
func_9696 = relay.Function([var_9694], output)
mutated_mod['func_9696'] = func_9696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9713 = relay.var("var_9713", dtype = "float64", shape = (7, 2, 6))#candidate|9713|(7, 2, 6)|var|float64
uop_9714 = relay.log2(var_9713.astype('float64')) # shape=(7, 2, 6)
output = uop_9714
output2 = uop_9714
func_9736 = relay.Function([var_9713,], output)
mod['func_9736'] = func_9736
mod = relay.transform.InferType()(mod)
var_9737 = relay.var("var_9737", dtype = "float64", shape = (7, 2, 6))#candidate|9737|(7, 2, 6)|var|float64
output = func_9736(var_9737)
func_9738 = relay.Function([var_9737], output)
mutated_mod['func_9738'] = func_9738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5861_call = mod.get_global_var('func_5861')
func_5862_call = mutated_mod.get_global_var('func_5862')
call_9752 = relay.TupleGetItem(func_5861_call(), 0)
call_9753 = relay.TupleGetItem(func_5862_call(), 0)
func_7182_call = mod.get_global_var('func_7182')
func_7184_call = mutated_mod.get_global_var('func_7184')
var_9755 = relay.var("var_9755", dtype = "int32", shape = (672,))#candidate|9755|(672,)|var|int32
call_9754 = relay.TupleGetItem(func_7182_call(relay.reshape(var_9755.astype('int32'), [672,])), 4)
call_9756 = relay.TupleGetItem(func_7184_call(relay.reshape(var_9755.astype('int32'), [672,])), 4)
func_5711_call = mod.get_global_var('func_5711')
func_5713_call = mutated_mod.get_global_var('func_5713')
call_9763 = relay.TupleGetItem(func_5711_call(), 0)
call_9764 = relay.TupleGetItem(func_5713_call(), 0)
output = relay.Tuple([call_9752,call_9754,var_9755,call_9763,])
output2 = relay.Tuple([call_9753,call_9756,var_9755,call_9764,])
func_9772 = relay.Function([var_9755,], output)
mod['func_9772'] = func_9772
mod = relay.transform.InferType()(mod)
mutated_mod['func_9772'] = func_9772
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9773 = relay.var("var_9773", dtype = "int32", shape = (672,))#candidate|9773|(672,)|var|int32
func_9772_call = mutated_mod.get_global_var('func_9772')
call_9774 = func_9772_call(var_9773)
output = call_9774
func_9775 = relay.Function([var_9773], output)
mutated_mod['func_9775'] = func_9775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7606_call = mod.get_global_var('func_7606')
func_7608_call = mutated_mod.get_global_var('func_7608')
call_9781 = relay.TupleGetItem(func_7606_call(), 0)
call_9782 = relay.TupleGetItem(func_7608_call(), 0)
func_4622_call = mod.get_global_var('func_4622')
func_4625_call = mutated_mod.get_global_var('func_4625')
const_9794 = relay.const([[-7.289917,-8.338609,5.801747,6.174521,-7.798427,-3.734601,7.945679,9.925065,-2.486212,5.449811,-0.910984,-5.300411,9.952528,0.773619,8.636262,-7.785833,1.273153,0.096169,1.143602,5.337555,-7.967427,5.805911,-8.880906,-0.645229,-1.254169,7.529887,8.557989,6.076154,8.933777,-1.331935,5.335869,2.727680,-7.426475,2.912168,0.072759,0.952834,-4.442497,0.365466,-6.222971,-0.502082,-4.775215,8.240950,3.788860,-0.406582,-5.608575,-1.910408,7.875888,-1.955796,-6.558426,7.435261,-9.581126,-1.653305,-6.262384,4.859195,6.426815,7.279012,0.952620,-6.035081,-3.079732,-0.834319,1.026441,-4.588482,-2.426055,-6.952519,-1.930071,-6.332588,5.378833,-0.777127,-0.558474,-5.327664,9.156695,7.279673,-9.679319,4.647285,0.926489,8.727136,-9.032191,8.596721,-8.637321,-6.928587,-7.199227,9.825220,1.881351,8.486197],[-4.386018,7.058606,1.842462,-2.598384,-7.907904,-2.465296,1.847160,0.370216,0.259591,-5.607015,-9.135790,3.639598,3.157787,-1.673049,-6.869517,6.003060,1.085319,-8.735750,3.005250,2.586151,-8.071416,8.011673,6.083259,-4.723050,-4.887742,7.451325,3.420161,9.651514,5.400551,3.379183,0.442936,-2.532110,5.926585,9.021929,-9.392665,9.069098,7.475845,-1.063914,2.089231,7.159019,-2.014976,-3.912989,7.941827,-0.582155,-4.950484,-3.642368,-3.346374,-2.615989,3.327177,9.886635,-0.384796,8.091572,6.285488,4.407516,-0.071045,-0.976827,1.415683,-5.451359,-0.804186,6.299273,-5.897220,-7.253121,9.932698,-1.740688,9.486244,-9.573247,-6.820026,0.290547,4.952129,-8.941332,6.431687,-5.385294,-6.525299,-0.539446,-6.006406,5.902864,0.003242,2.117833,-4.220122,-6.353160,9.184533,-6.419651,-4.673291,-1.688802],[-4.883962,5.562317,5.336118,-4.105149,-5.703954,2.466536,-2.271849,0.257324,-5.181350,-0.009232,-3.198599,-2.644800,9.312886,-4.671712,-9.696506,-6.168448,7.559691,5.460569,9.134507,-7.617197,-0.184493,-4.529420,-6.790028,-8.988897,4.596534,-5.875494,0.500219,1.761416,5.392685,-9.125324,-2.235654,-3.522123,-9.367086,0.272851,3.840969,3.098707,4.283435,-2.732024,9.834076,-8.037665,-9.769826,7.051429,-0.259951,-2.488105,-5.254338,3.172847,9.352340,-0.449646,0.696171,-3.306234,-9.473439,-8.175619,9.794186,8.695624,-7.970252,8.859279,-9.824580,-7.326821,-5.583030,-4.141515,-5.897364,0.632919,4.900348,0.668726,0.506132,3.754951,-5.164542,2.487194,7.761593,-6.339764,2.421263,-5.350554,-3.054984,-8.908077,6.955721,3.508076,-6.487889,-4.572234,0.553097,8.253345,7.186522,-8.649114,-9.908525,4.393943],[-3.515805,6.293699,-3.777202,-4.606050,7.591289,6.837013,6.042124,-3.444462,0.134659,-7.325208,-1.393004,-2.622419,-9.623926,6.119409,-6.474649,-6.992785,6.830307,-6.801672,2.871807,-0.936049,3.760609,-5.065786,4.920059,1.589242,8.505486,7.391595,9.561977,4.517894,-9.280458,-4.298960,4.228831,2.798413,2.781749,-2.889191,-7.054483,6.094286,-5.779351,4.644220,-8.318952,5.143788,-9.490811,6.383796,-2.945763,7.950611,-2.155236,9.807263,6.663080,-7.439768,4.417674,8.909244,7.813358,5.959087,-0.372584,5.268889,0.288499,-7.315611,0.140390,7.836666,-2.419456,-7.085906,5.429080,9.295207,8.126977,6.817412,-3.885156,-9.159837,8.321355,-1.533019,-3.344996,-8.791253,-8.409589,0.932155,-3.937007,2.322377,-1.796019,0.777036,5.332708,-0.115732,-5.964503,8.276464,-2.724398,5.897846,-6.550170,-4.055713],[1.675086,-9.838168,0.884444,-0.120439,4.213425,3.409049,2.977147,5.053608,1.004289,7.766910,5.795826,-3.509134,3.445405,6.788383,1.676941,-4.793540,-2.346731,-6.940318,3.213085,0.172664,-7.460375,-7.896293,-1.167920,4.677616,0.087082,1.617344,8.045291,-3.028187,6.065280,-1.922983,1.724534,-2.440246,-9.484658,-6.386230,7.092753,-8.172597,-5.977867,4.935419,-0.989254,-0.047358,-8.006068,-2.680413,8.500095,-2.638161,-1.201192,-8.419762,7.642534,9.743944,8.258779,7.683453,5.954930,0.780910,-3.122970,-9.645337,8.167529,-1.048131,5.179730,2.929160,-8.086149,0.077141,1.610375,-7.636498,-1.797278,-6.897596,5.323133,-5.804994,0.056013,-0.392596,3.759199,-3.125039,2.929928,-0.913673,2.528790,-2.416564,2.469634,-4.766209,6.434647,2.441007,-8.241417,7.912211,-0.922909,-1.593866,4.416155,6.941256],[-2.176497,3.881506,7.762369,-2.589470,-9.259377,-7.217792,-2.687932,-9.631913,3.483602,-0.376322,5.724344,-7.917643,5.396771,4.519870,9.074162,2.096884,-7.152335,-5.893579,-7.937005,-1.735224,8.417527,-3.056964,1.340423,4.025833,0.592914,-2.720121,9.477476,-6.746263,8.614294,-8.459907,-0.087815,-0.287995,-5.420310,-3.787668,6.356905,2.238533,1.599113,3.967713,-9.701867,-1.566512,-3.154410,-5.966339,5.901859,-1.403682,-2.844796,9.050954,7.481038,3.220320,-5.044575,-5.131469,-8.741077,-6.984848,-4.275772,-1.625226,-9.858523,-9.763043,2.661880,9.076246,1.219675,-7.451348,-5.847635,-8.949852,5.311176,6.626130,-1.381002,-8.883358,-6.141691,-4.404079,-0.123093,5.197149,1.529013,9.318910,8.373832,9.384763,-3.453223,-5.279781,-1.846041,-1.576700,3.725545,6.757579,-0.292790,-8.716688,1.698638,6.628311],[-5.437754,-5.761081,-5.227840,-5.182766,-6.480781,-3.144132,4.274951,9.501386,1.723761,-7.288376,-0.251058,-5.805270,3.075480,6.475180,-8.596081,-2.777152,7.252270,-6.502246,-0.860702,7.829900,6.245125,8.074143,8.524306,-1.279027,5.244276,3.471541,-1.373422,-9.533940,-1.885345,-2.176625,-1.074908,1.653365,-9.242298,6.953882,5.303869,2.863230,-2.264627,8.938146,-3.444350,-7.149883,-3.645088,8.229936,-8.814381,-6.639810,6.677175,5.945585,5.402006,9.839355,-9.522647,-2.304871,-0.955322,-3.415237,8.343670,-1.672722,2.687993,0.854977,-7.075635,2.852553,-8.624010,7.339550,-3.705660,1.588219,-4.208231,6.182307,9.767580,-1.572165,-2.119814,-8.296896,-2.194049,2.249381,0.585710,-5.220060,5.613777,-3.761629,9.856227,6.044899,-1.834493,-4.917537,1.546594,-7.426203,8.857201,-5.418993,8.035085,2.394473],[3.370138,-9.152769,3.702028,-7.488667,-9.194227,-9.125200,0.558007,6.722846,-5.269035,-2.235821,-9.663675,-5.426083,0.934846,1.315686,7.715976,-6.505154,4.566008,-1.584496,3.370221,7.128188,4.191794,-6.272465,1.955894,8.516718,6.286108,7.876701,-5.118759,8.349719,8.108661,-5.307264,-4.896907,4.110832,5.744669,-9.223050,3.469429,-7.963126,-3.023093,4.612153,5.693576,5.993474,-7.463105,-2.779327,5.696612,-0.207603,-0.935167,2.819247,5.220851,-4.943191,-1.894326,-7.965398,-4.234734,7.863442,4.911307,-3.745558,9.339594,3.931305,-3.308571,-1.368758,2.273006,-7.018328,4.512403,-4.887357,9.464838,-9.919245,-5.174916,6.079187,1.156160,0.366397,8.293684,9.335400,2.767118,-1.032785,-0.322551,5.039295,1.265439,3.094430,-5.594408,9.171868,-5.691201,6.247275,-6.863929,0.167656,8.691438,-8.513270]], dtype = "float64")#candidate|9794|(8, 84)|const|float64
call_9793 = relay.TupleGetItem(func_4622_call(relay.reshape(const_9794.astype('float64'), [2, 336])), 0)
call_9795 = relay.TupleGetItem(func_4625_call(relay.reshape(const_9794.astype('float64'), [2, 336])), 0)
var_9797 = relay.var("var_9797", dtype = "float64", shape = (8, 84))#candidate|9797|(8, 84)|var|float64
bop_9798 = relay.left_shift(const_9794.astype('int32'), relay.reshape(var_9797.astype('int32'), relay.shape_of(const_9794))) # shape=(8, 84)
output = relay.Tuple([call_9781,call_9793,bop_9798,])
output2 = relay.Tuple([call_9782,call_9795,bop_9798,])
func_9805 = relay.Function([var_9797,], output)
mod['func_9805'] = func_9805
mod = relay.transform.InferType()(mod)
mutated_mod['func_9805'] = func_9805
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9806 = relay.var("var_9806", dtype = "float64", shape = (8, 84))#candidate|9806|(8, 84)|var|float64
func_9805_call = mutated_mod.get_global_var('func_9805')
call_9807 = func_9805_call(var_9806)
output = call_9807
func_9808 = relay.Function([var_9806], output)
mutated_mod['func_9808'] = func_9808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7287_call = mod.get_global_var('func_7287')
func_7288_call = mutated_mod.get_global_var('func_7288')
call_9872 = relay.TupleGetItem(func_7287_call(), 0)
call_9873 = relay.TupleGetItem(func_7288_call(), 0)
const_9877 = relay.const([1.298519,6.618077,8.525426,8.646367,3.662432,4.257172,7.530596,2.516440,7.317379,-2.545751,-1.124330,-6.028456,-4.421315,-2.174178,2.585882,9.975626,-8.216046,2.724269,-4.605990,5.545779,-5.452161,-8.367168,1.347889,-1.200743,-4.468171,4.898740,-4.825128,-1.492426,-1.258963,-1.251349,-5.900017,-2.858889,-4.954002,0.626361,0.788582,-8.316206,8.500745,4.305432,-0.590642,-5.752037,-9.928871,7.170327,4.667845,6.761111,-0.412569,-9.220536,-2.291015,6.046363,-3.569673,5.168976,8.269973,5.213036,-5.383872,-7.645751,-1.101213,-0.217762,-8.851001,-2.930731,0.447210,5.726294,3.801564,-5.773071,0.528773,2.027069,-4.288281,6.416565,-8.079488,4.436728,4.084924,-9.581511,-9.304486,-6.887754,-6.533319,-9.445637,-6.461006,-6.582954,9.853321,3.194660,-3.249094,-6.680697,-8.294519,4.554065,4.591830,0.331540,-7.738809,-6.373674,-8.310480,5.074435,9.246152,-1.232420,0.834600,-1.088442,-2.588505,3.184438,-9.407076,0.192020,0.700598,3.298640,4.352118,4.259763,-7.747926,-7.097368,-1.103510,-6.503399,-0.332865,-3.896189,4.910132,-0.814536,-7.457066,-4.326713,-7.786922,5.611207,-4.762607,-8.196164,-0.063641,0.280384,5.491253,7.964201,2.157453,-8.093570,5.665400,-3.849122,3.804006,-1.709909,-6.181921,-7.352471,-6.378836,5.880130,-4.754000,7.758281,3.552294,-0.329092,-0.797140,1.896451,9.182224,7.291229,-2.456581,3.639938,3.830193,2.257434,-6.057822,-2.754763,-7.915574,-9.022749,7.010830,3.655251,-9.374432,1.936129,6.705334,1.355770,-9.087420,7.131487,-9.041533,-4.023298,-5.186464,1.074518,4.628295,-1.294815,3.740742,6.937746,-2.860006,-5.364843,-7.416937,2.664721,-0.055333,-5.598816,-2.509250,9.834718,-6.410579,-5.725456,9.468382,9.435494,5.272068,-5.568150,-3.185799,2.147842,-3.485910,-8.568159,8.770199,6.506496,-2.258529,7.381068,1.840542,7.009742,-8.259146,7.510004,6.213567,0.365440,-1.160840,-3.804209,6.998749,1.459416,0.488671,-8.658949,0.882597,-0.501378,2.573904,-1.938101,-6.696922,-3.183407,6.616756,-4.415223,-8.836890,6.970963,-3.375537,-1.913379,1.418076,4.312765,0.462955,-7.505296,5.134373,-0.101571,-0.348251,-1.392366,-3.093321,7.115503,-0.473692,-8.828334,6.443348,4.904298,1.818154,4.031157,1.723507,0.477452,-7.479034,1.794433,-7.012772,-1.459746,1.445605,0.246709,5.707928,8.341411,9.669847,8.566721,-2.716526,-7.657904,-2.392231,-9.207607,-2.200879,-6.192875,9.885662,3.381941,4.690296,-2.393383,-4.136140,-1.704990,2.966334,1.591422,8.914899,7.011264,5.600143,-7.128582,-4.323122,8.501258,-9.267070,6.305963,6.884662,-8.529500,4.315592,5.738455,-6.670282,2.097599,-1.386358,-1.561611,1.226887,3.821863,8.188682,-9.334610,-7.070369,3.718097,2.986937,4.978948,9.292599,8.565653,-8.496318,-3.965503,-1.924853,-0.508107,-6.773406,2.346371,9.106326,-2.695638,-5.801667,-3.193034,-6.713932,2.676966,-0.232615,-9.884678,-1.690523,-7.348262,9.589303,-2.583318,6.317926,-0.324970,2.852283,8.771859,-7.905672,-5.138816,5.852998,4.871777,-8.201438,9.933048,1.961936,-3.714778,-6.559984,5.272690,9.254719,0.517549,-0.564840,-0.882651,4.195071,-2.623706,5.123540,-5.483076,6.283008,-9.298581,9.324162,5.759121,7.523304,-3.378292,-4.179298,8.070209,5.297634,-6.025902,-4.717525,-3.169618,7.687629,9.133367,6.435905,1.976460,-7.917722,-1.870272,2.604471,-3.658004,4.153926,-5.846184,-3.467712,5.481174,0.968110,-3.050793,-5.044574,5.238004,3.827813,-9.525033,2.852056,-7.934901,5.736951,1.132799,-8.763404,0.208254,-0.279330,0.932104,-9.710744,0.723777,1.737832,4.563885,-3.827801,3.100614,-4.742437,-2.561605,4.276612,4.072551,5.360508,8.793846,-0.636422,7.714954,6.479035,-0.386494,9.150544,1.070549,8.777184,-2.323979,8.135998,5.587454,7.290329,7.567268,-6.037760,6.846265,9.357032,4.113208,8.795197,4.885785,-6.677926,-8.642825,4.112743,-8.116730,0.146270,-5.307633,-7.255960,-2.448680,6.404429,-9.406414,-5.674733,0.823659,-8.748874,2.318576,4.115217,-7.025970,-1.500420,2.936903,-2.117455,-7.378936,-3.211650,8.409981,1.250123,-0.106576,5.478131,-3.092917,-5.630712,-3.640697,1.429543,-0.168250,-4.431564,-0.332121,-6.347330,-1.106655,6.115126,-5.746732,6.710773,-9.610622,7.255795,9.462880,6.609286,-0.542837,1.205014,-0.122831,-5.810792,5.929474,-1.558730,-9.585378,3.680902,8.635924,1.797951,-4.486610,9.050636,4.161616,9.784172,-5.219963,1.852918,-8.467930,2.680923,4.552291,6.934561,-9.987751,-3.789015,-2.370237,8.177113,-9.883228,4.453025,8.291650,1.741245,4.902993,6.618676,5.532946,-3.971198,0.477401,-1.119387,-7.166663,9.116380,5.339711,5.781972,9.912171,-4.743456,3.063819,-7.973097,-7.079235,-1.371944,-3.018623,2.049800,-4.951858,4.046638,0.050491,-8.569941,3.092817,-3.082155,7.451363,0.373224,-2.637228,-5.816328,1.251049,-0.373059,-7.442902,-4.472583,-0.184470,-5.282597,0.779011,-8.983876,6.005133,-3.798072,-9.233990,-0.739121,-1.801989,-5.136648,9.177641,0.216758,6.116128,-2.585011,-7.169355,-2.353723,1.280159,3.406489,-8.219038,0.826164,-5.837832,3.197687,1.980699,-9.399486,5.360031,-3.071632,6.908886,9.439414,-0.137378,-2.913698,-4.193941,2.210953,1.113423,9.615100,7.845654,0.642653,-0.714545,-5.118625,-2.697380,-1.630601,-9.412571,-0.025734,-0.679599,-6.211990,-6.735743,9.959943,-9.731513,-6.848730,8.936987,4.975554,-8.691741,-8.482863,5.702265,-2.674681,6.960732,1.311438,-0.073787,6.275883,-5.334465,8.603310,-1.690674,6.604229,9.616879,-0.342880,2.981841,7.139208,-4.388755,5.609713,6.789840,-7.017515,-8.849459,-5.681807,5.691571,0.547212,8.296430,-1.659436,9.253996,-5.429393,0.474571,9.761645,6.176704,9.933126,-8.892831,6.946262,-1.995098,-4.632259,-5.126076,7.242145,-7.209741,0.491478,6.026816,2.522973,4.746002,-5.299293,-4.602641,-1.301592,-0.014723,7.988346,-0.939514,-7.421113,-7.892292,2.355600,1.691809,5.245064,5.480189,-8.886514,-4.585821,3.348115,4.084018,5.195484,3.494343,9.448707,4.293931,-8.897131,-3.479126,-0.319247,8.190368,2.492697,3.019874,-4.946926,6.124195,2.748429,-1.319674,2.686469,-6.416439,5.030464,-8.311058,-1.088102,8.639048,5.775014,7.534212,7.874981,2.964173,-8.568742,2.034790,5.219653,2.278356,-0.440883,7.254532,3.929754,-1.466236,3.457897,-5.209287,-7.903086,-4.475731,3.040415,-9.539534,-1.140679,9.885499,-9.916002,8.833456,1.445931,-1.858813,-5.750025,8.026981,-2.385519,-0.706882,3.970772,3.220945,9.729939,8.720267,4.674648,4.583819,-0.310854,-0.913530,5.776625,-3.319234,-0.686778,-9.766317,4.776903,7.571934,-7.880228,6.847175,-3.223430,4.451191,6.541475,-1.727785,-9.710128,-3.859749,-1.922991,5.200050,5.537277,-0.111052,3.137080,-7.096794,-3.862593,-3.743452,-6.703431,-0.196172,-5.506936,-2.726916,5.998116,-7.935482,-4.686356,-5.597150,-5.230572,-5.702298,5.246562,2.966331,5.448094,6.602547,1.578360,-5.445746,-7.204284,-6.416978,5.447152,-8.368652,7.650537,-2.442363,0.679002,-2.659064,3.996494,2.159692,5.080859,6.495567,8.635596,2.004966,-3.281942,-8.934348,-8.183438,8.477195,4.721100,-3.336688,-4.171055,-1.291643,4.441134,4.514126,7.885942,-3.242069,-9.949480,2.338251,-1.148613,-1.438862,7.295211,6.603802,-5.945467,3.555461,-8.872126,-4.275066,-3.934088,7.474137,-3.427885,-2.447564,3.753138,-6.185125,-5.970360,2.563043,-0.213509,2.674820,-8.513088,-1.350185,1.362116,-8.747112,5.003588,9.265164,4.914456,-0.887737,6.520999,9.881135,1.430797,-1.276179,-9.273633,-8.844732,-6.363874,-0.412931,6.364798,3.967104,-2.861667,-1.291268,-1.871455,5.139548,-3.943515,8.111266,0.612076,6.121879,8.534551,-6.730779,5.442352,-0.130005,3.729548,1.603654,6.769819,1.319201,-8.959027,-7.586253,5.254122,7.236803,7.581108,-8.591283,4.123585,8.114572,3.258038,-7.168007,-7.159365,-7.885114,7.163906,-6.574386,-3.494492,-7.908180,-1.012562,-7.672518,4.061914,1.279856,-7.526630,4.020212,2.955615,-1.755172,-6.352936,-6.978103,-3.226893,-0.648129,-3.504303,-7.510503,6.119093,3.303261,0.668030,9.518883,7.556214,2.506340,-0.425245,-5.986148,4.484821,4.131891,8.966607,0.240782,-9.656362,-3.973177,-2.796234,-8.976319,2.889554,2.104874,6.655156,5.532165,-7.252109,-2.532126,2.611534,-6.236908,-4.092931,7.603457,5.063327,9.458167,-8.364574,-7.981772,-1.385900,-3.665006,6.080741,4.539689,0.665586,5.096357,3.222124,-7.072021,-8.150856,-1.919241,-6.265299,3.372929,-1.305023,-3.592615,-8.959216,8.139172,8.325767,-8.692624,-2.816021,9.459921,2.261920,2.167781,-8.369051,7.090648,-8.486964,3.632349,0.285425,7.050886,4.891557,8.265029,-4.461398,0.004383,-4.883130,-2.136757,2.563538,-5.254150,9.402818,0.010466,-9.991394,-3.117615,-5.188603,1.100676,-6.378461,0.775095,-4.657297,8.543693,-8.918554,-2.693577,5.135419,1.048585,-6.592377,9.392573,0.460691,-4.461312,2.397128,-8.346315], dtype = "float64")#candidate|9877|(882,)|const|float64
bop_9878 = relay.logical_xor(call_9872.astype('int16'), relay.reshape(const_9877.astype('int16'), relay.shape_of(call_9872))) # shape=(882,)
bop_9881 = relay.logical_xor(call_9873.astype('int16'), relay.reshape(const_9877.astype('int16'), relay.shape_of(call_9873))) # shape=(882,)
bop_9885 = relay.floor_mod(bop_9878.astype('float32'), relay.reshape(const_9877.astype('float32'), relay.shape_of(bop_9878))) # shape=(882,)
bop_9888 = relay.floor_mod(bop_9881.astype('float32'), relay.reshape(const_9877.astype('float32'), relay.shape_of(bop_9881))) # shape=(882,)
func_2145_call = mod.get_global_var('func_2145')
func_2147_call = mutated_mod.get_global_var('func_2147')
const_9906 = relay.const([[-9.420221,-7.384720],[3.728519,-0.536200],[-2.519013,7.034042],[-2.638389,-9.116355],[0.925769,5.981891],[-5.222009,3.239444],[-8.410368,-5.882758],[-9.606385,3.259915],[-0.182614,4.233526],[2.705263,-1.429266],[3.556242,-7.604785],[7.574483,7.993513],[-2.493679,-7.342284],[4.288357,-6.689879],[-6.385715,1.663072],[4.061734,2.939675],[-3.391927,-9.474333],[8.109991,0.877325],[-1.194894,-4.483177],[-6.777638,-2.797991],[-2.154976,8.222205],[2.501971,-3.258287],[-6.566151,-4.618529],[-6.222623,5.288557],[9.926478,-1.930505],[-9.008277,9.099467],[-5.766811,-1.720932],[6.761084,0.987755],[9.774423,-0.265588],[-2.879258,5.321695],[-3.981117,7.765303],[1.211588,9.586556],[-6.784209,4.063377],[0.798805,4.799407],[4.704450,-9.288831],[4.770476,-1.095800],[-5.794643,2.329504],[1.687031,2.651708],[-5.940443,-1.503564],[7.688507,-7.900955],[-9.781291,-2.381490],[2.618223,3.160342],[-2.320678,7.440653],[6.097485,-1.920525],[-9.678408,5.567017],[-7.368436,1.032784],[1.810503,2.253430],[6.350859,-1.625065]], dtype = "float64")#candidate|9906|(48, 2)|const|float64
call_9905 = func_2145_call(relay.reshape(const_9906.astype('float64'), [1, 8, 12]))
call_9907 = func_2145_call(relay.reshape(const_9906.astype('float64'), [1, 8, 12]))
func_6771_call = mod.get_global_var('func_6771')
func_6772_call = mutated_mod.get_global_var('func_6772')
call_9909 = func_6771_call()
call_9910 = func_6771_call()
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_9913 = relay.TupleGetItem(func_5054_call(), 1)
call_9914 = relay.TupleGetItem(func_5055_call(), 1)
func_9408_call = mod.get_global_var('func_9408')
func_9410_call = mutated_mod.get_global_var('func_9410')
call_9918 = relay.TupleGetItem(func_9408_call(), 2)
call_9919 = relay.TupleGetItem(func_9410_call(), 2)
output = relay.Tuple([bop_9885,call_9905,const_9906,call_9909,call_9913,call_9918,])
output2 = relay.Tuple([bop_9888,call_9907,const_9906,call_9910,call_9914,call_9919,])
func_9920 = relay.Function([], output)
mod['func_9920'] = func_9920
mod = relay.transform.InferType()(mod)
output = func_9920()
func_9921 = relay.Function([], output)
mutated_mod['func_9921'] = func_9921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5398_call = mod.get_global_var('func_5398')
func_5400_call = mutated_mod.get_global_var('func_5400')
call_9947 = relay.TupleGetItem(func_5398_call(), 4)
call_9948 = relay.TupleGetItem(func_5400_call(), 4)
output = relay.Tuple([call_9947,])
output2 = relay.Tuple([call_9948,])
func_9957 = relay.Function([], output)
mod['func_9957'] = func_9957
mod = relay.transform.InferType()(mod)
mutated_mod['func_9957'] = func_9957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9957_call = mutated_mod.get_global_var('func_9957')
call_9958 = func_9957_call()
output = call_9958
func_9959 = relay.Function([], output)
mutated_mod['func_9959'] = func_9959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4873_call = mod.get_global_var('func_4873')
func_4874_call = mutated_mod.get_global_var('func_4874')
call_9972 = relay.TupleGetItem(func_4873_call(), 0)
call_9973 = relay.TupleGetItem(func_4874_call(), 0)
func_8454_call = mod.get_global_var('func_8454')
func_8456_call = mutated_mod.get_global_var('func_8456')
call_9977 = relay.TupleGetItem(func_8454_call(), 1)
call_9978 = relay.TupleGetItem(func_8456_call(), 1)
output = relay.Tuple([call_9972,call_9977,])
output2 = relay.Tuple([call_9973,call_9978,])
func_9986 = relay.Function([], output)
mod['func_9986'] = func_9986
mod = relay.transform.InferType()(mod)
mutated_mod['func_9986'] = func_9986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9986_call = mutated_mod.get_global_var('func_9986')
call_9987 = func_9986_call()
output = call_9987
func_9988 = relay.Function([], output)
mutated_mod['func_9988'] = func_9988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9986_call = mod.get_global_var('func_9986')
func_9988_call = mutated_mod.get_global_var('func_9988')
call_9991 = relay.TupleGetItem(func_9986_call(), 1)
call_9992 = relay.TupleGetItem(func_9988_call(), 1)
const_10002 = relay.const([False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,True,True,False], dtype = "bool")#candidate|10002|(882,)|const|bool
bop_10003 = relay.logical_or(call_9991.astype('bool'), relay.reshape(const_10002.astype('bool'), relay.shape_of(call_9991))) # shape=(882,)
bop_10006 = relay.logical_or(call_9992.astype('bool'), relay.reshape(const_10002.astype('bool'), relay.shape_of(call_9992))) # shape=(882,)
output = relay.Tuple([bop_10003,])
output2 = relay.Tuple([bop_10006,])
func_10018 = relay.Function([], output)
mod['func_10018'] = func_10018
mod = relay.transform.InferType()(mod)
mutated_mod['func_10018'] = func_10018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10018_call = mutated_mod.get_global_var('func_10018')
call_10019 = func_10018_call()
output = call_10019
func_10020 = relay.Function([], output)
mutated_mod['func_10020'] = func_10020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5321_call = mod.get_global_var('func_5321')
func_5322_call = mutated_mod.get_global_var('func_5322')
call_10023 = relay.TupleGetItem(func_5321_call(), 0)
call_10024 = relay.TupleGetItem(func_5322_call(), 0)
func_598_call = mod.get_global_var('func_598')
func_600_call = mutated_mod.get_global_var('func_600')
const_10028 = relay.const([9,-10,-7,8,-8,7,7,1,-3,-5,7,-8,-7,-1,6,9,-2,-2,-9,10,-5,-5,-4,-10,7,-4,9,3,-8,9,4,1,8,-4,-6,-4,1,5,6,-4,3,7,-1,-7,7,-5,5,-7,-9,-10,7,-8,-5,-6,10,-6,-10,-4,3,2,-1,-3,2,1,-2,8,7,10,1,-5,-7,-6,3,-10,5,-8,-8,5,10,-9,9,4,3,9,1,7,-6,5,-4,10,6,6,-9,-1,-6,-3,-10,-10,10,-9,5,9,8,3,-8,9,-10,-7,5,10,-10,4,-8,5,6,-9,7,-4,-1,-6,1,4,-2,2,8,-9,-3,-10,-9,-10,-8,-4,8,-1,7,7,-5,-9,1,6,-1,2,10,-8,-7,-2,9,10,-5,6,10,-10,-6,4,8,9,-7,-5,2,-5,-2,-6,6,8,-8,-3,-8,3,-2,1,9,1,-10,-4,-10,3,-8,2,-4,-5,-5,-9,3,-4,1,7,5,7,-6,10,-1,-7,10,1,2,-6,-4,9,-9,4,-8,1,1,-1,-8,-1,1,-8,-1,-7,-4,-9,8,-8,1,-8,-5,6,-4,10,-7,-2,1,1,8], dtype = "int8")#candidate|10028|(225,)|const|int8
call_10027 = relay.TupleGetItem(func_598_call(relay.reshape(const_10028.astype('int8'), [225,])), 2)
call_10029 = relay.TupleGetItem(func_600_call(relay.reshape(const_10028.astype('int8'), [225,])), 2)
func_9772_call = mod.get_global_var('func_9772')
func_9775_call = mutated_mod.get_global_var('func_9775')
const_10060 = relay.const([-6,-1,2,4,-9,7,2,-6,4,-2,-5,2,-10,-5,4,1,6,9,-3,10,-8,3,6,4,1,7,-8,7,8,9,5,1,5,9,-3,-2,-7,10,4,3,1,1,-1,-7,10,10,-7,5,3,10,5,8,4,-3,-1,6,-8,-1,-5,7,-4,1,2,-1,-1,10,2,-8,-7,7,-9,9,-7,-6,9,-8,-2,4,4,-8,8,-9,-7,9,7,-1,-6,-4,3,7,-5,6,-1,-3,8,10,-1,-6,-5,4,10,10,8,-1,4,-4,3,6,10,1,-1,4,9,4,-7,-5,6,3,9,-6,3,2,1,10,-9,1,-1,6,7,1,8,10,-3,-7,-6,5,-6,5,-9,3,7,10,1,7,5,3,-6,-5,-6,3,-7,1,-7,3,3,-6,9,8,3,9,5,-1,-5,-2,-1,4,5,-3,4,-10,3,-7,5,4,5,8,-7,3,-5,4,-1,-6,-4,9,-7,2,7,4,-9,10,6,-3,6,7,-10,7,-9,-6,-4,-8,-5,2,-4,-6,9,-6,-5,-7,3,-2,5,4,4,7,-6,10,-7,-3,-1,3,-6,-6,-6,-10,9,1,3,7,7,5,9,5,10,-9,9,-2,9,-4,10,-5,7,-4,3,-6,-7,2,-8,4,-6,-8,2,-8,9,9,7,10,-2,-2,6,-5,-1,-9,-5,5,-5,-6,7,2,-5,5,7,-6,10,5,-6,-10,-9,-5,3,8,7,9,-8,-7,-1,7,-10,8,10,9,-4,-4,10,-1,-1,5,3,-9,-4,-7,3,-5,-8,-4,-4,8,-3,-3,2,-8,-3,1,6,10,-8,-6,-3,-3,-4,1,1,-10,-2,9,-6,-8,-9,-8,9,-6,-5,6,-5,-6,8,-1,-9,-5,-3,-4,1,-2,1,7,6,-6,6,-6,5,-10,-3,1,-1,2,1,4,10,-4,4,2,5,-2,2,-1,-1,-9,1,6,-8,-5,4,3,-3,-6,10,-8,6,5,-7,-4,-9,-5,-4,-2,9,1,7,9,3,-1,-3,-8,-1,6,1,-8,-4,-1,-6,-1,10,-2,10,-9,9,5,-10,-1,-8,-9,-9,-9,2,3,3,-4,-8,2,-8,-10,-10,8,-2,1,6,-8,6,9,-7,5,8,3,-6,5,-5,-10,4,6,-7,-3,-6,-9,10,10,2,-9,5,-8,6,-4,10,7,9,7,10,-8,-5,-9,-5,-4,2,-7,7,7,-9,-6,2,3,9,-7,2,-5,2,-1,1,-4,-9,2,-4,-1,10,2,-1,5,-2,10,10,10,1,1,-7,7,-3,3,-9,-10,2,-1,4,-4,10,10,-1,-4,-2,-4,-7,6,-9,-7,3,-7,7,7,-8,8,5,10,10,6,-6,-2,1,-4,7,1,7,5,10,5,-3,5,-1,-3,6,3,-2,-8,-3,3,2,-1,4,4,10,-1,2,-10,-1,-4,-6,1,-3,9,1,-7,-8,1,6,7,5,-8,3,10,3,-1,4,-7,10,5,9,-4,2,-10,-3,6,-4,4,2,-1,7,-6,-5,8,-10,-9,-6,-8,10,-9,-7,-10,-9,10,6,8,5,-6,8,6,-8,-9,-7,5,6,-10,-8,8,5,-9,-3,-8,-3,-9,-10,-1,1,5,6,7,3,-9,-10,-8,-6,7,4,-6,-8,1,1,8,-1,-9,-2,-1,4,6,6,8,-1,-1,-8,3,3,8,6,-5,-9,-6,-1,-4,6,10,3,5,-2,-8,-5,-10,7,-4,4,-9,-6,-3,-1,-5,-6,10,2,1], dtype = "int32")#candidate|10060|(672,)|const|int32
call_10059 = relay.TupleGetItem(func_9772_call(relay.reshape(const_10060.astype('int32'), [672,])), 1)
call_10061 = relay.TupleGetItem(func_9775_call(relay.reshape(const_10060.astype('int32'), [672,])), 1)
func_8863_call = mod.get_global_var('func_8863')
func_8865_call = mutated_mod.get_global_var('func_8865')
call_10078 = relay.TupleGetItem(func_8863_call(), 1)
call_10079 = relay.TupleGetItem(func_8865_call(), 1)
uop_10082 = relay.erf(call_10027.astype('float32')) # shape=(5, 15, 3)
uop_10084 = relay.erf(call_10029.astype('float32')) # shape=(5, 15, 3)
output = relay.Tuple([call_10023,const_10028,call_10059,const_10060,call_10078,uop_10082,])
output2 = relay.Tuple([call_10024,const_10028,call_10061,const_10060,call_10079,uop_10084,])
func_10089 = relay.Function([], output)
mod['func_10089'] = func_10089
mod = relay.transform.InferType()(mod)
mutated_mod['func_10089'] = func_10089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10089_call = mutated_mod.get_global_var('func_10089')
call_10090 = func_10089_call()
output = call_10090
func_10091 = relay.Function([], output)
mutated_mod['func_10091'] = func_10091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5847_call = mod.get_global_var('func_5847')
func_5848_call = mutated_mod.get_global_var('func_5848')
call_10152 = func_5847_call()
call_10153 = func_5847_call()
func_8552_call = mod.get_global_var('func_8552')
func_8553_call = mutated_mod.get_global_var('func_8553')
call_10156 = relay.TupleGetItem(func_8552_call(), 0)
call_10157 = relay.TupleGetItem(func_8553_call(), 0)
func_2832_call = mod.get_global_var('func_2832')
func_2835_call = mutated_mod.get_global_var('func_2835')
var_10162 = relay.var("var_10162", dtype = "int32", shape = (672,))#candidate|10162|(672,)|var|int32
call_10161 = func_2832_call(relay.reshape(var_10162.astype('int32'), [6, 8, 14]))
call_10163 = func_2832_call(relay.reshape(var_10162.astype('int32'), [6, 8, 14]))
output = relay.Tuple([call_10152,call_10156,call_10161,var_10162,])
output2 = relay.Tuple([call_10153,call_10157,call_10163,var_10162,])
func_10181 = relay.Function([var_10162,], output)
mod['func_10181'] = func_10181
mod = relay.transform.InferType()(mod)
mutated_mod['func_10181'] = func_10181
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10182 = relay.var("var_10182", dtype = "int32", shape = (672,))#candidate|10182|(672,)|var|int32
func_10181_call = mutated_mod.get_global_var('func_10181')
call_10183 = func_10181_call(var_10182)
output = call_10183
func_10184 = relay.Function([var_10182], output)
mutated_mod['func_10184'] = func_10184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9920_call = mod.get_global_var('func_9920')
func_9921_call = mutated_mod.get_global_var('func_9921')
call_10217 = relay.TupleGetItem(func_9920_call(), 2)
call_10218 = relay.TupleGetItem(func_9921_call(), 2)
var_10225 = relay.var("var_10225", dtype = "float64", shape = (48, 2))#candidate|10225|(48, 2)|var|float64
bop_10226 = relay.not_equal(call_10217.astype('bool'), relay.reshape(var_10225.astype('bool'), relay.shape_of(call_10217))) # shape=(48, 2)
bop_10229 = relay.not_equal(call_10218.astype('bool'), relay.reshape(var_10225.astype('bool'), relay.shape_of(call_10218))) # shape=(48, 2)
output = bop_10226
output2 = bop_10229
func_10241 = relay.Function([var_10225,], output)
mod['func_10241'] = func_10241
mod = relay.transform.InferType()(mod)
mutated_mod['func_10241'] = func_10241
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10242 = relay.var("var_10242", dtype = "float64", shape = (48, 2))#candidate|10242|(48, 2)|var|float64
func_10241_call = mutated_mod.get_global_var('func_10241')
call_10243 = func_10241_call(var_10242)
output = call_10243
func_10244 = relay.Function([var_10242], output)
mutated_mod['func_10244'] = func_10244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_10274 = func_4727_call()
call_10275 = func_4727_call()
output = call_10274
output2 = call_10275
func_10278 = relay.Function([], output)
mod['func_10278'] = func_10278
mod = relay.transform.InferType()(mod)
mutated_mod['func_10278'] = func_10278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10278_call = mutated_mod.get_global_var('func_10278')
call_10279 = func_10278_call()
output = call_10279
func_10280 = relay.Function([], output)
mutated_mod['func_10280'] = func_10280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8363_call = mod.get_global_var('func_8363')
func_8365_call = mutated_mod.get_global_var('func_8365')
call_10281 = func_8363_call()
call_10282 = func_8363_call()
output = relay.Tuple([call_10281,])
output2 = relay.Tuple([call_10282,])
func_10318 = relay.Function([], output)
mod['func_10318'] = func_10318
mod = relay.transform.InferType()(mod)
mutated_mod['func_10318'] = func_10318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10318_call = mutated_mod.get_global_var('func_10318')
call_10319 = func_10318_call()
output = call_10319
func_10320 = relay.Function([], output)
mutated_mod['func_10320'] = func_10320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9662_call = mod.get_global_var('func_9662')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_10334 = relay.TupleGetItem(func_9662_call(), 1)
call_10335 = relay.TupleGetItem(func_9663_call(), 1)
func_9805_call = mod.get_global_var('func_9805')
func_9808_call = mutated_mod.get_global_var('func_9808')
const_10346 = relay.const([9.748715,-6.296720,-7.457409,-0.523451,3.977383,-7.144845,-1.260265,-9.281956,0.397826,9.050951,-8.290963,7.221014,4.063496,8.456842,4.131919,-6.819757,2.028253,3.646895,7.949928,1.009013,9.800542,1.731702,-2.513529,8.661062,7.688607,9.573718,6.688590,-7.223918,7.788652,6.244069,6.692408,6.481867,-1.276193,-2.217044,2.641523,-4.624081,9.687284,-5.048139,-4.082729,1.245230,8.390799,8.814446,5.224332,2.396852,1.057749,5.219200,4.208107,3.970031,5.384659,9.995124,-3.970914,6.140437,6.577459,4.511987,3.167173,4.031007,7.091937,6.203495,-3.436980,2.605232,-8.201061,-7.396148,-0.908145,8.535865,4.124626,-4.619442,6.092474,1.773272,8.898887,-0.205961,4.914725,8.460129,-7.746406,4.510283,-8.889133,-9.553989,-3.562571,-2.656532,8.078307,-1.306365,-1.814172,-8.582043,8.610914,9.836841,-4.637913,9.333896,9.257890,-7.162522,-6.247546,5.292294,2.005127,2.108388,-8.251361,-0.477879,7.700190,3.469340,8.866714,0.135233,4.212281,6.767724,-7.979760,-7.090994,-6.315705,0.204040,-6.226542,3.457393,8.443486,5.749573,-6.497995,0.032390,6.974089,4.765704,-9.142568,6.692335,1.623040,0.360245,2.333595,-0.539949,-2.083427,-1.152890,-3.622569,-2.534592,-2.164540,5.302628,2.841403,0.931639,1.590039,7.949605,8.295590,-6.175374,-4.994174,1.943634,5.306195,4.686660,7.767288,-2.483168,3.206985,4.376687,4.400817,-6.629186,3.535658,5.956943,-9.197651,-0.492571,8.622213,6.822831,-4.861824,7.539623,-0.259519,-2.252128,4.667212,0.625248,9.657049,-3.767355,9.923464,-4.605588,-0.656277,-0.465474,-1.368240,5.261988,2.773920,5.923891,5.592118,4.688973,7.445554,3.187916,-5.301405,8.676863,-0.016263,-6.022412,-8.325958,-4.623583,-4.611846,-4.331197,-1.787151,-9.899270,-8.699346,5.901712,3.076669,4.435885,-7.698628,5.200466,1.139985,2.907784,-8.864851,7.514235,-7.169994,-7.472820,-4.726088,7.161694,-3.518773,-5.595377,-1.578444,-8.427991,-7.744657,-9.572113,-6.950104,-8.461963,9.826770,7.622132,0.323305,-6.415535,3.835825,4.967287,7.638922,-0.231312,-4.260705,-1.792229,-2.567794,-5.242239,-3.068813,-2.766864,-7.478355,-0.651501,-2.675015,-9.984873,5.330615,2.005415,6.225863,-6.865313,2.025756,-6.566851,-3.839362,-3.619123,3.300150,6.697833,-9.503363,-5.173614,-4.299180,-6.106156,8.291564,7.240156,8.656335,6.877701,2.931324,-4.450969,-9.147171,-8.683876,6.090204,6.365961,-6.263458,8.523400,-6.779390,1.660510,-7.836093,4.481566,-4.940816,-9.731920,1.172304,-4.708280,-2.020701,-4.169891,9.652334,7.845733,0.595052,5.742333,0.854171,-4.815604,8.320826,8.737715,3.966118,0.207069,2.942820,-5.036977,4.995235,5.038096,4.157046,-0.625184,-2.810096,8.561242,-7.245940,3.030252,1.844971,-1.897348,-3.095492,4.712787,-8.930314,3.459803,-8.620490,9.474749,3.083620,9.461510,-0.446453,0.544066,5.128132,-8.270902,-4.851467,-4.652490,-8.764588,-5.476794,-0.212704,-4.912986,-0.908409,-4.064156,6.856413,-3.376284,-1.129116,2.654112,5.871381,6.012274,-2.632892,-7.441513,-8.579624,-5.397082,2.216354,2.313533,-6.311284,1.753626,6.321514,-1.532163,2.894231,8.209811,-2.070134,-9.045560,-3.305791,0.417466,3.175714,3.046282,-5.104817,-0.427826,-8.135063,2.199965,-1.089716,5.820492,-6.799258,-5.259990,-6.754493,4.715128,0.361485,-2.175568,6.139391,-2.733288,2.425011,-7.990825,5.112283,-6.787212,-3.173228,2.097613,-1.429236,7.573488,-3.612468,-1.044366,5.026282,9.873981,0.985848,-2.845467,7.683894,4.404190,-5.346702,-9.536138,4.522794,2.597551,-6.049778,-7.995783,1.478545,1.812639,6.877098,-2.790275,8.240825,8.137930,9.558248,-6.209285,-2.159285,-0.824163,0.582797,7.923669,3.416370,2.230940,4.118683,-2.729096,2.528432,-6.853195,0.077547,7.678383,-8.373026,9.426432,8.234426,4.046444,7.360375,-3.206378,-8.490631,6.942359,9.586140,-1.914339,-9.133885,8.389650,-7.437617,1.777635,3.191465,4.801418,4.741295,3.206391,-2.501218,5.690973,-6.630020,-8.252285,9.224681,-0.659759,-7.718722,0.092245,0.069096,-1.312161,-6.358957,4.992848,3.367114,8.032805,1.342154,0.780368,4.425011,-7.368637,-7.975639,3.777334,-4.492241,-3.843242,-9.455281,-1.415346,8.350848,0.237517,-9.747798,7.272437,8.399711,-8.594209,8.786377,-0.185346,-7.486661,3.045027,-8.161081,-0.963491,-9.035430,7.753544,-2.759487,0.412209,8.847682,0.155013,6.380810,9.361945,-0.152984,-8.314763,8.422835,-2.992116,0.777249,-7.564533,-9.863573,-1.018487,-9.614377,3.677792,4.366392,-5.472615,-0.575340,-1.189823,-9.037761,-3.476433,-6.809253,-4.799849,-9.177396,3.219925,-0.067726,6.258232,4.886527,-5.757692,5.926652,-8.093637,-1.369793,4.798135,5.395887,-1.341741,6.523150,-0.895621,3.245653,4.776215,2.903583,7.431223,3.807821,1.047117,2.575906,-8.771789,4.930680,3.623722,8.086372,-8.357439,0.397251,-5.703997,-6.026451,-9.811547,4.296903,9.103511,-2.159282,2.527038,6.753031,-3.815340,-5.768238,9.404335,-1.858512,1.148139,-7.756329,-4.866224,-1.274459,-7.043353,1.537473,1.458680,1.206874,1.020066,9.918842,4.455352,9.087233,3.759942,-5.981434,-8.254924,-2.804794,-1.547879,3.035774,-1.447909,3.694247,-0.202536,4.655763,6.920474,-7.809294,-3.613070,4.203259,-9.994321,-0.784443,-2.574886,0.767352,8.689716,-4.203666,-6.531132,-8.070791,-8.554525,6.538512,-3.715445,-4.524524,1.567231,-4.743450,-2.673713,8.855316,0.638685,8.594686,-1.747524,-0.812070,-8.602657,1.700297,-5.519828,0.744657,6.366971,-3.820779,2.809346,-3.550923,4.266558,-7.362216,-1.865397,6.454058,5.704050,-9.479899,8.829221,4.906792,5.662934,-4.016960,-9.238062,-5.085321,-3.468500,9.764389,3.741788,3.829463,7.528345,4.418006,1.667132,8.752868,1.467961,6.575740,-0.427376,-6.793901,6.170480,3.202366,-4.067811,-2.416964,-8.634672,-5.464158,6.733859,5.016554,0.327894,-6.514376,2.892925,-9.900763,0.740035,9.780807,-2.820609,-3.749314,-1.320999,-3.908852,7.043241,2.828551,-6.552789,-0.641690,8.286228,-8.311260,-1.925660,-1.571723,-8.482883,-8.890536,-0.564797,8.314024,1.736136,-3.322757,-3.904325,-8.756575,7.104744,9.046758,8.634583,5.707711,5.273720,8.242408,2.764660,3.241855,-7.325246,8.346578,5.529612,-5.174383,-1.411383,-3.518140,3.404740,7.056808,9.140047,-5.926228,-2.169230,3.444589,-7.200814,4.366494,-6.559270,3.454285,-6.650141,8.026639,-3.742470,-4.323973,2.228495,3.418566,9.960492,3.782478,6.324768,0.526606,-0.060975,-4.347556,7.449929,-3.180951,-8.548233,6.190940,-6.267338,1.369967,-6.306075,-2.476506,-3.449269,-5.391269,-3.495956,-6.804258,4.487084,2.550199,5.106013,-4.032298,5.405093,-8.177754,4.130063,-7.811343,0.571078,-0.120142,0.683505,1.647799,-2.933171,9.944886,4.888539,-3.593802,5.851142,-3.709420,2.364908], dtype = "float64")#candidate|10346|(672,)|const|float64
call_10345 = relay.TupleGetItem(func_9805_call(relay.reshape(const_10346.astype('float64'), [8, 84])), 1)
call_10347 = relay.TupleGetItem(func_9808_call(relay.reshape(const_10346.astype('float64'), [8, 84])), 1)
output = relay.Tuple([call_10334,call_10345,const_10346,])
output2 = relay.Tuple([call_10335,call_10347,const_10346,])
func_10349 = relay.Function([], output)
mod['func_10349'] = func_10349
mod = relay.transform.InferType()(mod)
output = func_10349()
func_10350 = relay.Function([], output)
mutated_mod['func_10350'] = func_10350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6473_call = mod.get_global_var('func_6473')
func_6474_call = mutated_mod.get_global_var('func_6474')
call_10351 = relay.TupleGetItem(func_6473_call(), 0)
call_10352 = relay.TupleGetItem(func_6474_call(), 0)
output = relay.Tuple([call_10351,])
output2 = relay.Tuple([call_10352,])
func_10373 = relay.Function([], output)
mod['func_10373'] = func_10373
mod = relay.transform.InferType()(mod)
output = func_10373()
func_10374 = relay.Function([], output)
mutated_mod['func_10374'] = func_10374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_10386 = func_5303_call()
call_10387 = func_5303_call()
output = call_10386
output2 = call_10387
func_10392 = relay.Function([], output)
mod['func_10392'] = func_10392
mod = relay.transform.InferType()(mod)
mutated_mod['func_10392'] = func_10392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10392_call = mutated_mod.get_global_var('func_10392')
call_10393 = func_10392_call()
output = call_10393
func_10394 = relay.Function([], output)
mutated_mod['func_10394'] = func_10394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7906_call = mod.get_global_var('func_7906')
func_7908_call = mutated_mod.get_global_var('func_7908')
call_10416 = relay.TupleGetItem(func_7906_call(), 0)
call_10417 = relay.TupleGetItem(func_7908_call(), 0)
output = relay.Tuple([call_10416,])
output2 = relay.Tuple([call_10417,])
func_10434 = relay.Function([], output)
mod['func_10434'] = func_10434
mod = relay.transform.InferType()(mod)
mutated_mod['func_10434'] = func_10434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10434_call = mutated_mod.get_global_var('func_10434')
call_10435 = func_10434_call()
output = call_10435
func_10436 = relay.Function([], output)
mutated_mod['func_10436'] = func_10436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9986_call = mod.get_global_var('func_9986')
func_9988_call = mutated_mod.get_global_var('func_9988')
call_10466 = relay.TupleGetItem(func_9986_call(), 1)
call_10467 = relay.TupleGetItem(func_9988_call(), 1)
output = call_10466
output2 = call_10467
func_10471 = relay.Function([], output)
mod['func_10471'] = func_10471
mod = relay.transform.InferType()(mod)
output = func_10471()
func_10472 = relay.Function([], output)
mutated_mod['func_10472'] = func_10472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9662_call = mod.get_global_var('func_9662')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_10484 = relay.TupleGetItem(func_9662_call(), 0)
call_10485 = relay.TupleGetItem(func_9663_call(), 0)
func_8050_call = mod.get_global_var('func_8050')
func_8053_call = mutated_mod.get_global_var('func_8053')
const_10490 = relay.const([8.718684,-1.335250,-8.067446,9.952574,0.866531,-1.815310,-4.134197,-9.024244,9.914041,-2.611097,2.190734,5.406159,7.646978,7.824533,-7.086868,4.351546,-6.878169,5.531171,-1.738282,-2.151430,9.110512,3.666709,-6.986705,8.681209,8.636341,-5.878828,-4.812100,-8.485112,6.485467,7.138345,-5.602378,9.158028,-3.664243,6.328795,-8.417668,-3.755286,-1.068968,0.790708,7.144151,4.078177,-9.075412,1.953028,7.963185,-2.394233,7.981948,-9.863757,-4.019119,-1.360472,-9.653592,4.768123,3.753293,-7.808632,5.914404,6.174751,3.297669,-0.803092,-5.482430,-9.718486,4.443409,-2.401695,-9.528241,-2.549957,2.951149,9.443525,-4.776173,-4.435737,-6.756304,-2.918796,-8.715642,-1.930555,-1.926030,4.649322,-9.869513,-1.498531,-4.722692,-6.196698,8.370481,1.524840,-9.372806,-5.409094,-7.094292,-6.358235,-2.693628,-0.537735,-9.207517,-4.481452,3.382194,-9.239188,6.568847,-4.391096,4.114996,6.856559,6.886086,5.229311,1.382868,9.791999,-1.872763,1.849949,-3.147327,6.871845,-5.879322,8.550813,3.556862,-4.958474,-4.221832,-1.485145,4.846489,-5.887779,6.539402,-7.732174,0.798747,-0.818419,-3.402208,-7.469644,0.760687,8.759324,8.236189,-5.814934,-0.344285,-5.398055,0.015810,8.906917,-6.582872,0.748072,0.349091,-6.028243,0.292317,9.362705,-2.553386,-9.232700,2.044564,-8.114231,-0.909094,-8.151008,2.878922,6.654147,6.118168,7.925061,-2.991485,5.395081,1.344279,8.878206,-3.058046,-3.746462,-1.561715,6.522671,-9.578670,6.175401,-7.164817,-2.739179,-9.622026,-3.247694,-0.251709,6.444964,-3.600842,-1.446077,-9.208384,0.153427,-5.230203,-0.233195,-1.647905,1.541235,3.975039,-2.632854,-4.590258,5.502091,-8.734676,-0.082390,6.865764,-0.623811,7.085041,2.093072,-0.151379,-5.280272,-4.828420,9.561139,-7.894944,-2.202382,2.561140,6.633260,4.134116,-8.812627,-0.492988,-1.701283,-5.324046,-4.983436,9.057413,-9.658231,-4.150264,0.794267,8.793508,6.564427,5.618657,8.015000,-3.728980,-8.870067,4.972867,-5.902568,0.231325,1.257000,2.254996,9.183908,-4.244302,-5.519015,2.868444,0.813092,-6.217816,-4.976890,-5.791217,8.095488,4.446533,-1.834635,-7.178417,-7.237492,4.555263,-1.212510,5.366551,-9.122496,7.612541,-1.775247,-5.974192,8.962889,9.862808,-7.724158,4.846312,-2.404989,3.749552,6.741139,3.029497,5.736993,6.154020,1.031586,-9.418860,-3.001205,-2.908385,-1.964460,4.990650,-5.502964,6.228256,-5.877161,-4.339486,6.164793,-0.100999,1.780238,6.542226,-5.805056,-8.928005,1.238953,0.128071,-4.164064,6.862494,-4.636614,-1.604352,9.765408,0.434575,-1.607987,-9.535837,1.385139,-9.776385,6.922226,-8.344237,5.219450,3.081061,5.584205,-5.166920,2.555507,-0.454384,-8.958111,-0.598351,-4.150275,-2.881250,7.483390,6.768063,7.407143,0.456362,0.197353,-9.196718,8.146231,5.214508,2.914256,-7.347131,4.822064,-3.400405,-6.038246,2.758381,9.345125,0.111869,2.090786,3.965111,9.415620,8.100751,-5.976750,0.387228,5.114950,-4.326329,-0.040885,6.209013,4.636719,-2.943650,-1.466337,0.065951,7.842964,-5.812372,8.392564,7.936597,6.998806,8.548783,-8.696231,8.250710,8.470731,-7.159043,-6.044525,-5.157457,-3.514250,3.314826,-6.089887,-2.803120,-1.893676,-1.139772,-0.369234,-2.064184,-9.891990,-3.385104,-0.141567,0.360787,0.417759,5.438971,3.286779,-7.672234,-2.539248,7.307005,-5.835665,-8.774175,-0.406369,-8.628026,-7.398998,-9.734752,-1.967608,-9.112800,-5.943951,-9.673393,1.972023,-5.873491,6.480987,-5.719303,-2.453975,0.913870,6.679128,1.260159,-3.502312,7.919687,-3.632714,-9.095656,-9.805827,3.689800,-9.046534,-9.438093,-5.316294,-9.327480,9.066509,0.962460,-4.291547,-7.792606,7.306238,-0.310701,7.332130,-9.712797,2.762516,-8.251573,0.276240,6.075044,-1.098229,-8.939065,-8.839723,-0.075399,5.646152,4.051066,-2.632480,-1.104951,-8.832341,-5.276491,-5.239164,4.024645,4.526018,5.065801,-0.144798,-7.267567,-0.071779,7.512744,2.056431,3.120005,3.224112,0.301327,-8.336914,5.718016,-0.768069,2.570535,5.104704,-2.868077,-3.087286,3.283894,-1.882141,3.085612,-0.346428,9.347009,8.031574,7.475495,-1.699205,-6.785795,-6.226717,3.791786,6.900335,8.659895,3.961098,9.636222,6.829664,-7.204766,-1.263891,-0.535013,-3.952144,6.285062,-9.295576,8.317988,3.119697,-8.902094,0.563549,-6.783608,-2.280236,9.149336,0.016907,6.956741,-3.218491,7.743021,-9.541933,6.587884,7.427530,-0.082660,9.057854,-7.462195,3.021256,-4.013573,-6.043316,-6.854986,-6.423879,8.266672,-8.593341,-8.102426,-1.056012,-3.874946,-3.956543,-1.021693,-3.730972,1.125208,-3.956380,-7.166934,-9.089116,-5.172205,6.550212,2.769871,3.842190,8.239101,-3.747295,-9.041816,6.104290,8.285807,-1.495558,-1.009936,-3.053048,2.802402,5.919006,-0.291635,-7.938824,8.994398,8.270501,-1.348356,3.449050,1.708174,3.046081,-4.852831,-6.761315,-9.083749,8.677432,2.065955,1.955729,-2.096007,-3.641891,-3.464388,-7.592105,-7.460528,2.965923,-1.064192,-5.188702,-7.615623,7.276744,7.896363,-0.603429,-6.470062,-3.409068,2.580532,-3.340246,-0.350612,-6.359852,-3.623276,-4.660460,9.161328,6.471446,-5.382744,0.971975,1.537552,-0.256915,-7.407801,4.911103,-9.944595,-5.481085,4.505738,-6.032045,5.706313,-7.504582,3.482078,-7.323305,-0.503141,-1.412345,0.076263,8.796907,-5.607865,2.058303,-9.076096,9.359381,-6.002846,-3.355366,8.884496,-9.648950,-7.460642,-3.875825,5.314198,-0.966522,-6.862496,4.288662,-5.635793,-7.345584,-1.988025,4.188164,-7.100120,1.368831,-0.433513,-8.811591,-5.546061,-0.577451,-8.368200,-8.451717,3.093952,6.153611,2.094917,5.819103,-9.706307,-3.281035,-1.760366,7.462570,1.529524,7.497016,6.954219,4.022780,-2.001273,-4.963980,-5.347695,3.179946,7.100119,9.462710,2.137661,-4.550085,-8.938943,-6.942801,-4.403078,-6.028349,-6.713368,8.809946,6.740693,-0.877401,-5.122019,-8.113687,9.382245,-8.928507,2.602584,-9.740705,-8.935750,-6.907525,0.042973,4.759737,-6.807095,4.014622,-2.001610,-8.606087,1.569230,0.938665,2.094486,-6.052768,9.696234,6.132562,-6.388590,8.855782,-9.575373,-1.487556,-5.769226,0.354077,0.919756,-7.085027,4.600853,1.286410,5.738967,-2.785995,1.893082,9.370449,3.379541,1.926323,-7.795622,0.431470,-6.858123,7.353893,2.148673,2.110882,7.943400,-5.016069,9.733932,-5.200694,9.485169,3.173700,6.949285,9.359109,-6.154134,7.592204,-3.937698,6.598482,-8.569097,7.005276,-0.458595,-8.759680,-1.545254,-0.907015,-4.301435,-8.387814,-9.783251,-7.146429,6.846573,-3.148582,-3.748418,-8.099348,-7.435131,7.611159,-8.730295,8.536226,-1.281525,6.662413,-3.048155,-1.715605,-8.706324,-3.875564,-4.145553,-9.712844,1.603492,6.284873,-8.410113,-0.961514,-5.397894,3.082479,-1.888095,0.308183,-4.729373,-4.928797,-7.016020,-5.257222,6.376110,4.922136,4.105900,0.858500,4.331335,9.099751,2.387965,-6.891498,3.047499,-0.880613,-9.503037,-3.935626,-3.116811,-3.093428,8.357471,1.357435,6.023647,8.924089,1.393575,1.536054,9.162674,-7.246971,-9.937275,-0.256551,6.098415,-7.836763,-3.444799,-5.771554,4.759223,-4.767130,4.594194,5.568855,-4.643884,-6.515489,-4.671026,-5.104260,-5.157924,-5.782447,-3.686595,-1.053823,6.349495,6.236525,-3.138423,4.887112,-6.478140,-8.382377,9.603345,7.178230,-4.560074,7.500328,5.826599,2.876227,2.918770,6.346597,-6.346051,4.938598,-3.501272,-6.693446,-3.901732,-5.066464,0.903279,9.789886,-4.617082,-0.455476,-3.884553,1.149530,-1.664377,1.041423,-2.080619,4.463224,-8.599377,3.617210,0.395500,6.560073,1.946076,1.833042,3.010602,9.112131,4.056910,-8.141753,-4.438954,9.365326,-8.506979,-1.368839,1.695926,-6.279346,-5.999201,-2.211684,3.246392,9.242664,3.449708,5.241645,3.225633,3.259941,-5.595176,-0.309328,4.317589,8.230327], dtype = "float64")#candidate|10490|(768,)|const|float64
call_10489 = relay.TupleGetItem(func_8050_call(relay.reshape(const_10490.astype('float64'), [2, 384])), 3)
call_10491 = relay.TupleGetItem(func_8053_call(relay.reshape(const_10490.astype('float64'), [2, 384])), 3)
func_6158_call = mod.get_global_var('func_6158')
func_6159_call = mutated_mod.get_global_var('func_6159')
call_10514 = relay.TupleGetItem(func_6158_call(), 0)
call_10515 = relay.TupleGetItem(func_6159_call(), 0)
func_8363_call = mod.get_global_var('func_8363')
func_8365_call = mutated_mod.get_global_var('func_8365')
call_10528 = func_8363_call()
call_10529 = func_8363_call()
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_10530 = func_5303_call()
call_10531 = func_5303_call()
func_9957_call = mod.get_global_var('func_9957')
func_9959_call = mutated_mod.get_global_var('func_9959')
call_10536 = relay.TupleGetItem(func_9957_call(), 0)
call_10537 = relay.TupleGetItem(func_9959_call(), 0)
output = relay.Tuple([call_10484,call_10489,const_10490,call_10514,call_10528,call_10530,call_10536,])
output2 = relay.Tuple([call_10485,call_10491,const_10490,call_10515,call_10529,call_10531,call_10537,])
func_10551 = relay.Function([], output)
mod['func_10551'] = func_10551
mod = relay.transform.InferType()(mod)
mutated_mod['func_10551'] = func_10551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10551_call = mutated_mod.get_global_var('func_10551')
call_10552 = func_10551_call()
output = call_10552
func_10553 = relay.Function([], output)
mutated_mod['func_10553'] = func_10553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7475_call = mod.get_global_var('func_7475')
func_7477_call = mutated_mod.get_global_var('func_7477')
call_10560 = func_7475_call()
call_10561 = func_7475_call()
output = relay.Tuple([call_10560,])
output2 = relay.Tuple([call_10561,])
func_10567 = relay.Function([], output)
mod['func_10567'] = func_10567
mod = relay.transform.InferType()(mod)
mutated_mod['func_10567'] = func_10567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10567_call = mutated_mod.get_global_var('func_10567')
call_10568 = func_10567_call()
output = call_10568
func_10569 = relay.Function([], output)
mutated_mod['func_10569'] = func_10569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_10601 = relay.TupleGetItem(func_5054_call(), 0)
call_10602 = relay.TupleGetItem(func_5055_call(), 0)
func_4535_call = mod.get_global_var('func_4535')
func_4539_call = mutated_mod.get_global_var('func_4539')
const_10604 = relay.const([[8.252486,8.933583],[-2.678779,-7.265967],[-0.287875,-1.121705],[5.314131,7.446827],[7.868943,9.050772],[6.462675,-2.361989],[2.102814,-6.745873],[4.193167,-1.054222],[8.648811,6.935385],[6.887235,-0.412235],[1.094041,-1.333701],[-2.980419,9.516632],[8.047349,-7.144207],[-0.886809,-3.513721],[-0.708549,-7.584842],[-5.962023,-4.404141],[-2.385378,0.210206],[3.699615,-5.646624],[6.754997,2.052848],[-8.811192,9.917966],[5.506786,-7.084232],[-2.446574,-0.286359],[4.672109,-6.902263],[2.839018,6.412199],[-6.387560,-1.914042],[-5.369680,-9.986080],[7.491219,9.399810],[1.833769,-2.638419],[-7.221818,-3.865548],[2.959781,3.771430],[0.614350,-0.404220],[-4.628298,0.346434],[-2.247170,-2.610956],[-9.250748,-8.542526],[-5.520327,8.028983],[-0.142741,4.074437],[-1.528163,-5.778386],[-1.381275,-2.727249],[4.234350,-6.841751],[-0.883971,1.598037],[3.445803,0.292604],[-0.539108,-4.531102],[5.688614,-8.577720],[9.497405,-7.456326],[-3.598065,3.834812],[-8.499205,-2.610660],[-8.407866,3.496752],[-7.543095,4.045413],[-7.305975,7.311036],[2.764885,0.234419],[8.688792,-6.723621],[2.078342,-0.128063],[1.922084,-2.073208],[9.706067,-0.144057],[-2.511818,-3.900744],[-8.100358,-1.182817],[-1.450626,0.471442],[1.527690,-4.452732],[7.956623,1.652234],[5.300485,-9.275473],[0.441787,-7.868094],[0.181901,-7.108038],[-7.979075,6.559850],[0.718770,4.140166],[7.372035,1.847794],[-1.321834,-3.691236],[-5.406090,-1.575776],[8.765633,7.581833],[-8.733453,-4.405668],[-0.693793,5.590439],[0.921839,6.590754],[-6.730580,7.024176],[0.942541,0.810382],[-6.268545,2.381316],[8.355445,3.664845],[-8.775564,-6.848965],[-0.229254,6.868761],[0.145693,-8.764387],[9.264139,2.610424],[-3.410093,0.453059],[7.305152,9.951881],[-3.590245,1.352236],[8.405537,0.695304],[7.033310,-7.331574],[-9.933257,-5.076804],[-2.951074,-4.817915],[-3.323916,7.675025],[-0.029684,-8.981292],[4.692228,-3.326570],[4.832933,-5.966663],[-1.636940,-7.907298],[4.861374,1.093966],[-4.081715,8.599801],[-6.077763,-1.019714],[-3.299437,-4.914452],[9.446925,-8.962706],[-5.228221,-0.581631],[-3.957687,-0.401295],[-5.615860,-6.043640],[5.577363,1.343364],[5.206139,-7.196234],[5.035120,-6.064738],[6.085819,-9.366820],[-7.099135,5.654467],[1.309393,-3.171501],[-6.912725,-6.921466],[6.897189,-4.880931],[4.064203,8.850511],[1.783542,-0.611221],[-8.900006,-0.138730],[0.532969,-3.951726],[0.209159,1.203170],[-7.011755,1.070828],[-6.606615,8.440970],[-9.766461,6.536253],[-8.028637,3.516679],[-9.254181,-2.565120],[-0.267493,-1.081722],[5.511473,2.838962],[8.068734,-9.016689],[-1.369529,-0.143171],[4.517494,3.839287],[-6.811087,0.900413],[4.215119,-1.357185],[4.633814,-3.902200],[0.575397,2.962108],[-0.423891,1.442303],[3.899310,7.698465],[9.655870,1.716254],[5.110692,3.043655],[7.448948,-6.036144],[4.667213,-7.416157],[6.709510,-3.112352],[-1.304423,-8.106699],[1.014336,-9.978775],[3.726541,-2.549119],[9.944444,4.563123],[-8.315035,-0.850683],[-1.067397,-3.210999],[2.045707,-3.360152],[-7.998558,1.663449],[-4.998898,5.702235],[-6.290527,0.195234],[7.170689,-4.010507],[6.192752,8.403661],[-6.108573,9.926737],[9.945878,-7.565667],[-5.594024,6.430449],[-0.911920,5.677520],[-0.065005,-6.366690],[-1.994486,-2.835948],[1.511625,1.015717],[0.790507,8.372761],[-2.813601,-3.061527],[-2.965650,4.936883],[6.742048,5.107931],[6.709258,-5.207059],[6.206041,-0.867335],[-6.887412,0.772181],[-7.411973,-0.217471],[-1.725162,0.815952],[-0.952749,-8.641349],[3.243244,-6.050133],[-1.236105,-1.298431],[-7.636227,-6.041926],[1.605212,-3.579927],[3.419074,5.496421],[-5.503589,5.667525],[3.715964,5.964487],[-3.011140,8.848354],[8.737230,-6.021002],[1.405320,-8.334230],[-5.598688,-7.775939],[7.227464,9.084264],[-7.911892,-8.043781],[8.376526,6.796350],[5.030613,-8.600855],[-8.626404,7.289235],[5.671978,-7.096603],[-0.763299,5.691549],[8.719122,-8.184190],[-5.742930,3.001430],[-5.190795,8.511993],[-5.960573,9.173869],[1.419762,4.802449],[0.244762,-7.390115],[6.067703,7.010778],[9.180245,-3.254962],[-8.011166,0.128624],[-3.723670,-3.143786],[9.803365,-9.005175],[-1.206276,0.795368],[-5.919597,-0.547725],[9.913015,-8.768358],[9.808725,-6.305197],[-9.843167,2.265977],[7.381474,0.332783],[0.377477,-2.038724],[1.529799,-8.743302],[-4.262509,-8.011022],[9.043450,-7.726534],[8.034422,0.897177],[8.587639,0.539109],[-1.769459,-2.124461],[3.528318,4.899098],[8.255237,6.141775],[5.267364,5.395754],[8.274808,-2.363663],[-3.268494,4.772991],[3.965234,-7.327286],[-4.197159,3.930225],[-5.292575,-9.749126],[6.318107,-4.896409],[-1.657941,-1.685655],[-0.616007,4.122237],[2.629641,-2.726290],[6.715770,3.660813],[-2.230742,0.748562],[0.610978,0.349589],[-5.138078,9.573060],[4.076041,4.961685],[-4.509922,2.889955],[9.768403,-0.773097],[-3.385237,-3.204956],[3.564897,2.312323],[1.059346,-6.502319],[9.988393,-4.129425],[-5.102628,4.348172],[5.826634,4.768632],[-3.341626,-0.992297],[4.214654,-1.936706],[3.661237,5.880225],[-2.748971,-5.999342],[8.887814,-9.493449],[-2.964015,8.332430],[3.168377,4.368730],[2.864071,-2.260879],[6.322724,8.781950],[3.211263,9.942969],[-9.373067,2.431863],[6.038923,-3.869036],[0.242364,6.724172],[9.141044,-9.813780],[3.165472,8.439109],[-7.495261,3.122058],[6.487282,-9.426118],[-3.198914,3.243686],[1.950551,-0.525750],[2.302905,0.986411],[3.085568,-6.748380],[7.463476,0.610005],[-3.144513,6.328509],[-8.537220,4.921951],[0.355528,7.113750],[1.008492,-9.728402],[7.369528,9.515754],[5.145368,0.199776],[7.723985,0.993616],[-9.662547,7.205592],[-9.225537,5.175460],[5.674755,-9.050041],[9.061413,7.052104],[-4.320177,6.262682],[-7.770942,-9.702906],[9.882300,-7.431324],[-0.630768,-0.005062],[5.466844,7.851030],[-7.751398,-2.115143],[8.068709,9.328475],[-4.308190,3.230774],[-6.939933,6.147396],[6.728285,1.620613],[3.085956,4.824944],[5.324834,4.642994],[-1.005983,-4.195123],[9.175129,-8.878694],[2.113179,4.884324],[-7.049126,7.151632],[7.589332,9.470941],[-5.716391,-1.761230],[4.402909,1.582172],[1.312409,7.477692],[-6.933358,-4.430900],[-7.420702,-5.505864],[-3.980386,-7.156135],[0.694139,-2.182203],[-9.416390,9.756271],[-0.456627,-4.973038],[-3.022428,-0.984255],[-8.896597,4.334616],[-5.814673,5.533795],[-3.726221,-0.262729],[7.984351,-5.568143],[-4.198079,-2.759844],[-9.749509,-4.828004],[7.232823,-0.430035],[-2.288436,4.095311],[-7.588599,9.932659],[-2.464819,-0.984688],[6.710390,-8.543649],[8.588499,5.744893],[7.746351,-2.521229],[1.362291,-1.728358],[8.810724,-8.288013],[7.161527,9.456897],[-0.881738,-3.238840],[1.345115,-6.247648],[-7.378908,5.178174],[2.622939,8.529032],[-1.732340,-4.633542],[-2.415271,-1.771236],[-6.257496,-4.786042],[-7.077635,0.261519],[-2.573045,-7.242867],[-3.683845,-1.825024],[2.329869,-7.390517],[-7.551371,1.981860],[2.099020,9.159925],[-8.962601,-6.694845],[-8.931476,-1.987856],[-7.705607,-1.799486],[-8.926376,-5.339315],[4.205982,4.335418],[-1.437235,7.894825],[6.374896,-0.026022],[-7.402180,5.128699],[9.552084,9.643667],[-7.318691,5.436984],[-4.836695,3.922158],[-7.130708,6.330340],[2.419610,-7.454676],[4.445913,-3.553599],[-5.790627,9.128347],[-4.771189,7.116157],[-8.277604,-0.787829],[-0.308261,2.302665],[2.029907,3.853214],[-4.402745,9.863903],[3.937220,-4.364699],[1.358700,-7.600594],[2.232866,-4.379230],[-1.169959,2.783259],[8.597290,0.885522],[2.014478,-9.797897],[1.876559,-3.490457],[-6.791583,3.486676],[7.798340,-5.434272],[3.815538,-4.930047],[6.298326,-1.906851],[-8.404514,-0.911044],[8.831291,-7.741377],[6.639962,5.047450],[-2.348231,-9.550811],[7.516586,8.439164],[2.749709,0.644426],[-6.043959,4.216183],[9.632890,8.603372],[-2.304986,5.238174],[5.325820,-0.787302],[-2.341143,0.960910],[-7.904655,0.711739],[-1.567718,-3.003218],[9.254354,-3.225764],[-8.992894,4.493991]], dtype = "float64")#candidate|10604|(364, 2)|const|float64
call_10603 = relay.TupleGetItem(func_4535_call(relay.reshape(const_10604.astype('float64'), [728,]), relay.reshape(call_10601.astype('bool'), [882,]), ), 6)
call_10605 = relay.TupleGetItem(func_4539_call(relay.reshape(const_10604.astype('float64'), [728,]), relay.reshape(call_10601.astype('bool'), [882,]), ), 6)
output = relay.Tuple([call_10601,call_10603,const_10604,])
output2 = relay.Tuple([call_10602,call_10605,const_10604,])
func_10613 = relay.Function([], output)
mod['func_10613'] = func_10613
mod = relay.transform.InferType()(mod)
mutated_mod['func_10613'] = func_10613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10613_call = mutated_mod.get_global_var('func_10613')
call_10614 = func_10613_call()
output = call_10614
func_10615 = relay.Function([], output)
mutated_mod['func_10615'] = func_10615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6407_call = mod.get_global_var('func_6407')
func_6408_call = mutated_mod.get_global_var('func_6408')
call_10620 = relay.TupleGetItem(func_6407_call(), 0)
call_10621 = relay.TupleGetItem(func_6408_call(), 0)
output = call_10620
output2 = call_10621
func_10624 = relay.Function([], output)
mod['func_10624'] = func_10624
mod = relay.transform.InferType()(mod)
mutated_mod['func_10624'] = func_10624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10624_call = mutated_mod.get_global_var('func_10624')
call_10625 = func_10624_call()
output = call_10625
func_10626 = relay.Function([], output)
mutated_mod['func_10626'] = func_10626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9662_call = mod.get_global_var('func_9662')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_10647 = relay.TupleGetItem(func_9662_call(), 0)
call_10648 = relay.TupleGetItem(func_9663_call(), 0)
func_7182_call = mod.get_global_var('func_7182')
func_7184_call = mutated_mod.get_global_var('func_7184')
const_10670 = relay.const([[-8,-6,-9,-8,-4,4,-6,6,-1,-1,-4,-1,9,-7,-8,10,-8,-2,3,-6,6,-10,-4,-4,-1,-3,-5,3,-2,7,-7,-5,-5,-6,9,-7,1,5,-4,-10,7,-1,8,8,-4,10,-4,-8,4,-9,-5,-5,-4,2,1,-2,-7,-3,-4,-7,-6,2,1,-8,4,-7,-4,5,-3,5,-1,4,-9,-5,8,3,-8,-3,-5,-6,-10,5,-5,1,7,4,4,-6,-7,-8,-2,8,-8,-2,3,9,3,7,-6,8,6,-3,-1,5,-1,-4,6,4,-2,4,-6,-9,10,-5,-6,-10,-4,-7,4,-5,-5,-8,1,-4,10,-10,-2,3,7,-8,10,9,3,-1,8,-1,-4,-3,-1,-10,4,5,-1,9,6,-4,7,2,-1,-6,10,-3,6,-3,-4,8,-5,5,-3,7,-4,-8,6,9,-7,-8,2,-3],[-7,5,-9,1,-8,-1,1,-2,7,-5,4,-2,-1,-7,-2,-1,-9,2,9,-2,-10,-8,9,7,2,10,-6,-6,-5,-9,-5,9,7,10,7,-3,-4,-9,2,10,-7,-1,-7,1,-10,-2,-3,7,-4,-7,10,7,4,-9,-3,-2,3,7,-10,3,-1,3,6,5,8,1,4,1,6,-4,-1,9,-10,4,-7,8,-2,3,2,7,9,-7,4,9,-10,-8,9,-6,6,-9,-9,-10,-1,-8,-10,-2,-1,-2,-6,6,3,-6,-3,-3,2,-1,-2,-1,-5,-5,-4,-4,5,1,-6,-9,10,3,-10,2,2,-5,8,7,-7,-10,1,-7,9,-2,-4,4,-8,9,5,2,-9,-2,-4,-2,-3,-3,6,5,-7,-10,7,9,3,5,-1,5,-3,7,-8,-10,1,9,3,-3,-10,3,7,5,10,-7,-7,1],[1,-9,8,2,-3,9,5,-8,4,-2,-5,-2,7,8,-4,-3,-8,6,2,-7,8,-2,-7,8,4,-4,-7,6,6,5,2,8,8,7,-1,4,-2,4,9,-1,-10,-1,-1,-8,-10,10,-10,-1,-10,8,-5,-3,-1,8,-9,-2,-6,-5,-10,6,7,-4,-2,-7,5,8,-2,-9,-9,2,6,4,-6,8,3,10,2,9,8,8,5,-3,8,7,-9,-3,4,-6,8,8,10,5,9,7,2,-1,3,2,-10,-7,2,3,-9,4,-4,1,2,7,-2,1,10,-10,9,-2,-5,-5,1,10,-8,-1,1,-8,10,4,-10,5,-6,2,-9,2,5,10,9,10,-8,-10,3,-2,5,-4,-1,-6,-3,2,-3,7,-6,-8,9,-10,8,-8,2,-3,-5,4,3,-5,-8,-10,3,-3,-4,-2,8,4,6,7],[1,6,7,6,-10,8,-7,-1,4,9,-4,5,-7,-7,10,-10,6,-8,6,4,-4,3,9,-10,-5,-4,-2,-10,5,-1,-5,-7,6,5,9,7,-10,-5,-2,5,-5,-8,-8,-5,8,-8,-6,-6,-2,6,10,5,2,2,-6,-3,4,8,-10,4,1,-2,9,-1,3,-2,-9,-5,-8,6,4,5,-9,-9,-7,8,9,5,2,-10,-3,7,1,4,-1,-3,10,-2,-8,9,-5,3,10,3,6,-8,6,-3,-9,4,9,-4,5,9,6,9,6,-7,-10,10,-4,4,-4,-6,-6,-3,-10,-4,-3,-8,-1,-4,9,-5,4,4,2,7,-7,-10,-5,-7,-10,-8,4,-5,3,3,-1,-10,4,4,-3,3,-5,-10,6,5,-10,10,-9,10,2,-3,-2,1,-10,-3,7,-3,-8,5,2,-9,-3,6,-4,3]], dtype = "int32")#candidate|10670|(4, 168)|const|int32
call_10669 = relay.TupleGetItem(func_7182_call(relay.reshape(const_10670.astype('int32'), [672,])), 1)
call_10671 = relay.TupleGetItem(func_7184_call(relay.reshape(const_10670.astype('int32'), [672,])), 1)
var_10677 = relay.var("var_10677", dtype = "int32", shape = (4, 168))#candidate|10677|(4, 168)|var|int32
bop_10678 = relay.bitwise_and(const_10670.astype('int16'), relay.reshape(var_10677.astype('int16'), relay.shape_of(const_10670))) # shape=(4, 168)
func_10318_call = mod.get_global_var('func_10318')
func_10320_call = mutated_mod.get_global_var('func_10320')
call_10689 = relay.TupleGetItem(func_10318_call(), 0)
call_10690 = relay.TupleGetItem(func_10320_call(), 0)
func_2832_call = mod.get_global_var('func_2832')
func_2835_call = mutated_mod.get_global_var('func_2835')
call_10699 = func_2832_call(relay.reshape(const_10670.astype('int32'), [6, 8, 14]))
call_10700 = func_2832_call(relay.reshape(const_10670.astype('int32'), [6, 8, 14]))
bop_10719 = relay.minimum(var_10677.astype('uint32'), relay.reshape(const_10670.astype('uint32'), relay.shape_of(var_10677))) # shape=(4, 168)
output = relay.Tuple([call_10647,call_10669,bop_10678,call_10689,call_10699,bop_10719,])
output2 = relay.Tuple([call_10648,call_10671,bop_10678,call_10690,call_10700,bop_10719,])
func_10733 = relay.Function([var_10677,], output)
mod['func_10733'] = func_10733
mod = relay.transform.InferType()(mod)
var_10734 = relay.var("var_10734", dtype = "int32", shape = (4, 168))#candidate|10734|(4, 168)|var|int32
output = func_10733(var_10734)
func_10735 = relay.Function([var_10734], output)
mutated_mod['func_10735'] = func_10735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4372_call = mod.get_global_var('func_4372')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_10765 = func_4372_call()
call_10766 = func_4372_call()
output = relay.Tuple([call_10765,])
output2 = relay.Tuple([call_10766,])
func_10782 = relay.Function([], output)
mod['func_10782'] = func_10782
mod = relay.transform.InferType()(mod)
output = func_10782()
func_10783 = relay.Function([], output)
mutated_mod['func_10783'] = func_10783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5847_call = mod.get_global_var('func_5847')
func_5848_call = mutated_mod.get_global_var('func_5848')
call_10830 = func_5847_call()
call_10831 = func_5847_call()
func_7013_call = mod.get_global_var('func_7013')
func_7016_call = mutated_mod.get_global_var('func_7016')
const_10838 = relay.const([[True,False,True,False,False,True,False,False,True],[False,True,False,True,True,True,True,False,True],[True,True,True,False,True,True,True,True,True],[True,True,False,False,False,False,False,False,False],[True,False,True,False,True,False,False,False,True],[False,True,True,True,False,False,False,False,True],[True,True,False,True,False,True,True,True,True],[False,True,True,False,False,False,True,True,True],[True,True,True,False,True,False,True,False,False],[True,False,False,True,False,True,True,True,True],[True,False,False,False,False,True,False,True,False],[False,False,True,True,False,False,False,False,False],[False,False,False,False,True,True,False,False,True],[True,False,False,False,True,False,True,True,True],[False,True,False,False,True,False,True,False,False],[False,False,True,False,False,True,False,False,False],[True,False,True,False,True,True,False,False,False],[True,True,True,False,True,True,False,False,False],[False,True,True,True,True,True,False,True,False],[True,False,False,True,True,True,False,False,False],[True,False,False,True,True,True,True,True,True],[False,True,True,False,False,False,True,True,False],[True,True,True,True,False,True,True,True,True],[False,False,True,True,True,True,True,True,True],[True,False,False,False,False,False,True,False,False],[True,False,True,True,True,False,True,False,False],[False,True,True,True,False,True,False,True,True],[False,False,False,True,True,False,True,True,False],[True,False,False,True,False,False,False,True,True],[False,False,True,False,True,True,False,False,True],[True,True,False,False,True,False,False,False,False],[False,True,True,False,True,False,True,False,False],[True,True,True,True,True,False,False,False,True],[True,False,True,False,True,False,False,False,True],[True,False,True,True,True,True,False,True,False],[False,False,False,False,False,True,False,True,True],[False,True,True,True,True,True,False,True,False],[True,False,False,False,True,True,False,False,False],[True,False,True,True,True,False,True,True,False],[True,True,True,False,True,False,True,False,True],[False,True,True,False,False,True,True,False,False],[False,False,False,False,True,False,True,False,True],[True,False,True,True,True,False,False,True,False],[True,False,False,False,False,True,True,False,True],[False,True,False,False,True,False,False,True,False],[True,True,False,False,False,False,True,False,True],[False,False,False,False,True,False,False,False,False],[False,True,True,True,False,False,True,False,False],[False,True,True,False,False,False,False,False,True],[True,False,True,False,False,True,True,False,True],[True,False,True,False,False,False,True,False,False],[True,True,True,True,True,False,True,True,False],[True,False,False,False,True,False,True,True,False],[True,False,False,False,False,True,True,False,True],[True,True,True,False,False,True,True,False,False],[True,True,False,True,False,False,True,True,True],[False,False,False,False,True,True,True,True,True],[False,False,True,True,False,False,True,False,False],[False,True,False,False,False,True,False,True,False],[False,False,True,True,False,True,False,True,True],[True,False,False,False,False,True,True,True,True],[True,False,True,True,False,False,False,True,False],[True,True,True,True,False,True,False,True,False],[False,True,True,True,False,True,True,False,True],[False,True,False,True,False,True,False,False,True],[False,False,False,False,True,False,True,True,False],[True,True,True,True,True,True,False,False,True],[True,False,False,False,False,True,False,False,False],[True,False,False,True,True,False,True,True,True],[True,True,False,True,False,False,True,True,True],[False,True,False,True,False,False,True,False,False],[True,False,False,True,False,True,True,True,False],[True,False,True,False,False,False,True,True,False],[True,False,True,False,False,False,False,False,False],[False,True,False,True,False,True,True,True,True],[False,False,False,False,True,False,False,False,False],[False,True,False,True,False,False,False,False,True],[True,True,True,True,True,False,False,False,True],[True,False,False,False,False,True,False,True,False],[False,True,False,True,True,True,True,False,True],[True,True,False,False,False,True,True,True,False],[False,True,True,True,False,True,True,False,True],[False,False,False,True,True,True,True,False,True],[True,True,True,False,False,False,False,True,False],[True,False,False,False,False,True,True,True,False],[False,True,False,True,True,True,False,False,False],[True,False,False,False,True,True,False,True,True],[False,False,False,True,True,True,True,True,True],[False,False,True,False,False,False,True,False,True],[False,False,False,False,True,False,False,False,True],[True,False,False,False,False,False,True,True,False],[False,False,True,True,True,False,False,True,False],[False,False,False,False,False,False,False,False,False],[False,False,False,True,True,False,True,False,False],[False,True,False,False,True,False,True,False,True],[True,True,True,False,True,True,False,True,False],[True,True,False,True,True,True,True,False,False],[True,False,False,True,False,True,True,False,False]], dtype = "bool")#candidate|10838|(98, 9)|const|bool
call_10837 = relay.TupleGetItem(func_7013_call(relay.reshape(const_10838.astype('bool'), [882,])), 0)
call_10839 = relay.TupleGetItem(func_7016_call(relay.reshape(const_10838.astype('bool'), [882,])), 0)
func_6473_call = mod.get_global_var('func_6473')
func_6474_call = mutated_mod.get_global_var('func_6474')
call_10848 = relay.TupleGetItem(func_6473_call(), 2)
call_10849 = relay.TupleGetItem(func_6474_call(), 2)
output = relay.Tuple([call_10830,call_10837,const_10838,call_10848,])
output2 = relay.Tuple([call_10831,call_10839,const_10838,call_10849,])
func_10850 = relay.Function([], output)
mod['func_10850'] = func_10850
mod = relay.transform.InferType()(mod)
mutated_mod['func_10850'] = func_10850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10850_call = mutated_mod.get_global_var('func_10850')
call_10851 = func_10850_call()
output = call_10851
func_10852 = relay.Function([], output)
mutated_mod['func_10852'] = func_10852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6771_call = mod.get_global_var('func_6771')
func_6772_call = mutated_mod.get_global_var('func_6772')
call_10853 = func_6771_call()
call_10854 = func_6771_call()
output = call_10853
output2 = call_10854
func_10855 = relay.Function([], output)
mod['func_10855'] = func_10855
mod = relay.transform.InferType()(mod)
mutated_mod['func_10855'] = func_10855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10855_call = mutated_mod.get_global_var('func_10855')
call_10856 = func_10855_call()
output = call_10856
func_10857 = relay.Function([], output)
mutated_mod['func_10857'] = func_10857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10318_call = mod.get_global_var('func_10318')
func_10320_call = mutated_mod.get_global_var('func_10320')
call_10904 = relay.TupleGetItem(func_10318_call(), 0)
call_10905 = relay.TupleGetItem(func_10320_call(), 0)
func_8050_call = mod.get_global_var('func_8050')
func_8053_call = mutated_mod.get_global_var('func_8053')
const_10911 = relay.const([-4.764422,-8.504170,-8.449793,-6.676285,-2.338148,-0.202455,-0.889254,6.729634,-3.150210,-3.677728,-2.146138,-2.014061,7.409669,2.167060,3.227750,-5.056487,-3.355062,9.429212,-4.380707,-4.013683,8.386756,1.375333,-5.655690,2.223311,8.518379,2.779061,-5.943520,-4.445938,6.892979,-5.768104,6.132530,-3.147699,8.184189,-5.303844,3.385288,-2.675320,1.207867,-0.733267,-5.270926,-4.363188,2.407480,-8.357849,8.709634,9.133242,-7.465418,5.649579,-1.805588,9.320436,7.068999,6.815995,-6.379781,4.124410,2.268265,0.093101,5.917164,3.798549,2.569273,-4.407578,6.772819,7.806735,2.208758,1.008671,-8.010612,7.055009,-6.133351,-5.107473,-9.681778,-8.130748,1.124539,-1.646152,6.738567,4.635986,1.126880,8.078337,2.442266,-5.577089,7.425468,1.136513,-6.297695,0.601364,3.788856,9.053627,2.903825,-5.699207,3.677143,9.782937,-6.018745,-5.532027,1.578050,-8.137037,-2.811532,6.924604,-9.612069,-5.030465,-6.426266,0.064064,9.449102,9.849186,-4.371838,-4.348144,-8.303561,-8.118296,-7.853466,-9.777474,-5.583036,6.659922,5.144240,-7.511089,2.747799,-2.114387,-1.284025,9.602388,-6.347783,-5.516393,-0.520972,5.266969,5.785318,-9.341961,-9.538770,1.776601,8.516456,5.900864,7.086065,1.101538,-3.244317,-8.176735,4.930016,3.135935,6.525368,0.529408,-6.690316,-4.592894,-4.018683,8.144000,-3.723191,-2.081060,4.582379,-7.462855,2.199611,1.918085,-4.794780,2.892593,-0.355038,9.005022,-4.250677,2.701271,7.386767,-3.919438,-6.357654,-6.270387,-0.631329,5.777700,9.576813,0.018664,3.238541,-1.057869,-1.767745,5.978426,-1.746951,-7.565761,3.533824,2.653269,-6.684471,5.211130,-6.564303,4.354823,-8.005968,-2.981380,-6.460467,-1.782542,0.950204,5.808602,-7.268721,-2.235794,-0.155236,-7.693528,-1.399018,-1.438873,5.144160,-6.176531,-6.984321,1.614645,-0.326679,-0.990523,2.332758,-7.149821,9.231076,-1.194606,-2.545232,7.237329,-0.076320,3.082419,2.316606,4.121487,6.813342,-1.256385,0.682196,-4.125141,-2.855556,-4.838238,8.983698,-9.321245,2.514482,9.849227,5.654755,-1.408015,-0.878215,-4.499552,5.647057,-4.213540,2.123317,-7.210890,-5.323204,-8.182814,4.604377,-7.904251,4.461375,-1.469585,-1.732337,4.151419,-6.809569,7.922501,9.551368,-1.254219,1.773992,0.408975,-0.245550,3.313086,-6.885205,1.940516,-8.991135,-1.378733,-8.025210,-9.251183,-3.588589,-9.426801,5.567701,3.332352,2.340225,-3.460103,3.756569,-5.006561,7.495752,-1.247451,0.677343,-6.046523,-7.227303,-8.839667,2.271746,3.089064,-3.453216,-6.476734,0.373707,-6.259461,2.679369,8.776994,-9.350910,-0.671113,4.564413,4.285498,-3.800203,-0.804732,-3.619778,1.895391,-2.222728,-2.230616,-9.666897,-4.498454,-8.057891,5.899723,3.343558,-2.353535,-0.860765,-9.260706,-1.549757,-6.743877,2.354858,5.750663,0.484971,1.002533,6.362739,-6.096665,-0.926061,1.877461,2.122031,-4.487217,2.011504,-6.079740,-4.778278,7.706805,-4.614702,7.881484,-6.913736,-7.966234,-1.893048,9.637975,2.080879,4.575712,4.805565,-3.311291,7.051104,2.930432,-2.259819,-1.195866,-4.349959,2.729229,-5.527157,-6.088799,4.456982,-0.965200,-4.214262,6.384472,-5.699359,4.400786,3.878053,-1.078378,2.914550,0.558550,-2.751298,-1.836434,2.333449,4.110460,-5.864567,-5.909120,-8.755987,8.874506,6.225792,-1.869263,-3.169756,8.401839,-6.166785,-7.460727,1.424657,4.230227,-7.042705,9.067856,9.425980,4.970129,-6.431437,4.672609,-4.845805,-8.926957,4.737544,1.536884,-1.799921,9.635996,6.089666,-4.388567,0.925414,-7.960443,0.237265,2.516609,-5.082485,8.315899,-2.435741,-1.751280,3.427635,-3.922262,7.640945,-4.683867,-2.429100,-0.736158,-7.604539,3.671516,-6.766884,2.165956,8.396544,-7.919378,9.287480,-2.562218,-0.627235,-0.672545,3.997992,-3.473367,2.794611,9.438866,-6.423084,0.887327,-9.349611,-9.056782,-0.892194,8.277031,-6.921343,6.984067,6.220123,-5.609150,-9.874493,9.592675,8.749679,9.854355,6.015650,6.146875,-9.096113,-0.697913,2.724931,-2.087541,-4.484355,6.691146,2.936362,-8.140604,-6.558436,1.067356,5.918150,0.671654,-1.110565,8.479505,9.072735,-0.956853,5.189679,-0.843439,5.892283,-2.091131,-7.572673,9.794145,6.572570,-4.161836,-8.475719,-1.804121,4.102888,-1.050157,-7.136620,5.449093,-2.768953,-2.922808,-5.654201,-6.090356,4.206330,6.742091,-2.072925,6.815233,-6.164812,-4.539079,5.819366,-9.721929,-0.620416,7.605209,5.286183,-8.097814,-8.807042,7.154313,4.943217,-6.506181,2.514146,6.772891,-1.318357,5.238035,-1.430805,6.038735,-4.624904,-0.048229,6.903462,-4.249106,-7.630750,-1.046178,6.795941,4.289519,-0.230909,2.671264,3.429503,4.384654,8.747500,-1.139231,-0.890294,-0.170952,-5.055390,4.532242,-6.771022,-5.874255,-6.283342,6.298993,-9.953463,5.637454,-4.417275,-7.799255,4.796701,-9.243870,-3.949459,-7.938516,-9.121346,-5.108681,-6.767516,-6.794710,4.228536,9.326724,-0.997642,4.319063,-9.318137,8.906846,8.420305,-0.419118,5.065007,1.620695,-0.632757,5.771831,-5.758302,9.024535,8.554279,5.576425,-4.012480,8.929967,5.792011,8.775163,0.381375,5.189297,1.035814,4.089027,-5.701163,-2.723417,-4.376264,7.166198,0.614043,4.325592,5.557230,7.203905,-1.523094,-4.077276,3.019840,4.055661,-4.295484,1.391942,-2.554778,-0.790269,-2.674853,7.998891,-5.471184,8.127846,3.398729,6.284169,-6.134473,-1.734813,5.891337,-8.290001,3.230620,2.647443,-0.242337,9.214653,3.581511,4.780527,-1.591802,-9.475446,-1.299458,0.737579,4.318908,-3.426770,0.893570,-1.046393,8.442088,-4.313353,-7.403009,-1.159343,-3.732492,0.814988,3.585664,7.456532,-2.751442,5.508944,-5.366130,-5.205197,5.225311,8.043897,-5.028896,1.799843,-8.489927,-2.656445,9.827912,-9.744244,-3.589890,7.068600,-8.116094,8.183968,-9.187822,1.584035,7.593294,-6.621758,-9.218528,-2.825605,1.125477,-5.969611,0.546356,-6.724994,4.117227,-3.442942,8.346134,-0.743499,5.975607,-7.217213,-0.849618,-7.449794,2.972432,-1.174770,-3.395058,-4.848073,-1.201869,8.432364,0.890433,-2.268522,-6.667913,-1.658567,-0.047136,-6.502675,9.620393,6.290580,-0.757678,0.486136,4.709028,-8.595920,-6.455758,3.861926,6.011865,-1.310306,9.098380,-2.058172,-1.700108,7.576618,3.976501,-0.923980,-9.717560,-1.910814,9.968204,-0.059981,9.640054,-5.654463,-2.511376,-6.349312,-6.965118,-8.792539,4.865620,-3.441621,-0.551783,-1.847730,2.811881,-1.840282,-4.206797,-9.854791,-0.066746,-1.089523,7.853069,-3.658862,6.762620,-0.961773,6.969311,9.308125,8.977812,-0.880826,3.562977,3.779823,4.882843,-2.921284,-0.444982,1.532154,3.292041,-2.777196,-7.820892,-6.512013,7.015888,-6.239824,-1.613574,9.852929,0.068040,4.760053,-1.751374,3.422019,-0.461445,0.198448,-3.988773,7.290786,6.258049,2.602303,-5.248062,7.139472,-6.049922,4.702002,6.714439,-6.957763,-6.022355,3.485265,-1.515597,3.589483,-7.712091,2.419415,3.039463,-9.895181,-2.097748,7.071704,-3.119072,-2.339139,-2.034996,4.966096,-4.489764,-5.237077,7.442211,8.366671,-3.289345,-9.547967,2.443042,4.715666,-3.120046,7.933430,6.166671,-4.161548,4.286888,-8.274226,-0.584139,9.637089,8.602712,9.786123,7.841477,-4.516086,6.783004,-8.422323,-1.022561,-9.044387,-9.950734,6.331735,-6.529278,1.743041,-6.660895,2.146493,7.757128,6.749459,-8.989776,1.862529,9.683771,8.203155,-9.640526,-2.346270,4.545526,4.031324,-6.718902,-7.103693,-9.750222,0.322974,2.968821,9.360890,9.622687,-5.000303,-4.872179,-5.344096,1.429914,-6.066503,8.385353,2.850020,4.145135,-1.321920,7.740677,-2.695742,-4.485310,9.246947,-8.767709,-0.651783,8.555162,3.180463,-6.719800,-8.488688,0.377114,7.668571,7.296443,-9.062597,-2.978801,-8.329279,9.696684,7.280441,-7.410434,9.024996,-9.588983,4.910153,-6.167070,6.390874], dtype = "float64")#candidate|10911|(768,)|const|float64
call_10910 = relay.TupleGetItem(func_8050_call(relay.reshape(const_10911.astype('float64'), [2, 384])), 6)
call_10912 = relay.TupleGetItem(func_8053_call(relay.reshape(const_10911.astype('float64'), [2, 384])), 6)
output = relay.Tuple([call_10904,call_10910,const_10911,])
output2 = relay.Tuple([call_10905,call_10912,const_10911,])
func_10933 = relay.Function([], output)
mod['func_10933'] = func_10933
mod = relay.transform.InferType()(mod)
mutated_mod['func_10933'] = func_10933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10933_call = mutated_mod.get_global_var('func_10933')
call_10934 = func_10933_call()
output = call_10934
func_10935 = relay.Function([], output)
mutated_mod['func_10935'] = func_10935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10278_call = mod.get_global_var('func_10278')
func_10280_call = mutated_mod.get_global_var('func_10280')
call_10957 = func_10278_call()
call_10958 = func_10278_call()
output = call_10957
output2 = call_10958
func_10966 = relay.Function([], output)
mod['func_10966'] = func_10966
mod = relay.transform.InferType()(mod)
mutated_mod['func_10966'] = func_10966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10966_call = mutated_mod.get_global_var('func_10966')
call_10967 = func_10966_call()
output = call_10967
func_10968 = relay.Function([], output)
mutated_mod['func_10968'] = func_10968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5861_call = mod.get_global_var('func_5861')
func_5862_call = mutated_mod.get_global_var('func_5862')
call_11014 = relay.TupleGetItem(func_5861_call(), 0)
call_11015 = relay.TupleGetItem(func_5862_call(), 0)
var_11018 = relay.var("var_11018", dtype = "float32", shape = (11, 12, 4))#candidate|11018|(11, 12, 4)|var|float32
bop_11019 = relay.not_equal(call_11014.astype('bool'), relay.reshape(var_11018.astype('bool'), relay.shape_of(call_11014))) # shape=(11, 12, 4)
bop_11022 = relay.not_equal(call_11015.astype('bool'), relay.reshape(var_11018.astype('bool'), relay.shape_of(call_11015))) # shape=(11, 12, 4)
output = bop_11019
output2 = bop_11022
func_11042 = relay.Function([var_11018,], output)
mod['func_11042'] = func_11042
mod = relay.transform.InferType()(mod)
mutated_mod['func_11042'] = func_11042
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11043 = relay.var("var_11043", dtype = "float32", shape = (11, 12, 4))#candidate|11043|(11, 12, 4)|var|float32
func_11042_call = mutated_mod.get_global_var('func_11042')
call_11044 = func_11042_call(var_11043)
output = call_11044
func_11045 = relay.Function([var_11043], output)
mutated_mod['func_11045'] = func_11045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7606_call = mod.get_global_var('func_7606')
func_7608_call = mutated_mod.get_global_var('func_7608')
call_11082 = relay.TupleGetItem(func_7606_call(), 0)
call_11083 = relay.TupleGetItem(func_7608_call(), 0)
output = call_11082
output2 = call_11083
func_11086 = relay.Function([], output)
mod['func_11086'] = func_11086
mod = relay.transform.InferType()(mod)
output = func_11086()
func_11087 = relay.Function([], output)
mutated_mod['func_11087'] = func_11087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8745_call = mod.get_global_var('func_8745')
func_8747_call = mutated_mod.get_global_var('func_8747')
call_11094 = relay.TupleGetItem(func_8745_call(), 0)
call_11095 = relay.TupleGetItem(func_8747_call(), 0)
output = relay.Tuple([call_11094,])
output2 = relay.Tuple([call_11095,])
func_11097 = relay.Function([], output)
mod['func_11097'] = func_11097
mod = relay.transform.InferType()(mod)
output = func_11097()
func_11098 = relay.Function([], output)
mutated_mod['func_11098'] = func_11098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_11235 = relay.TupleGetItem(func_5054_call(), 0)
call_11236 = relay.TupleGetItem(func_5055_call(), 0)
uop_11250 = relay.sinh(call_11235.astype('float64')) # shape=(14, 7, 9)
uop_11252 = relay.sinh(call_11236.astype('float64')) # shape=(14, 7, 9)
output = uop_11250
output2 = uop_11252
func_11261 = relay.Function([], output)
mod['func_11261'] = func_11261
mod = relay.transform.InferType()(mod)
output = func_11261()
func_11262 = relay.Function([], output)
mutated_mod['func_11262'] = func_11262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4774_call = mod.get_global_var('func_4774')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_11302 = relay.TupleGetItem(func_4774_call(), 2)
call_11303 = relay.TupleGetItem(func_4776_call(), 2)
uop_11311 = relay.asin(call_11302.astype('float64')) # shape=(882,)
uop_11313 = relay.asin(call_11303.astype('float64')) # shape=(882,)
output = relay.Tuple([uop_11311,])
output2 = relay.Tuple([uop_11313,])
func_11322 = relay.Function([], output)
mod['func_11322'] = func_11322
mod = relay.transform.InferType()(mod)
mutated_mod['func_11322'] = func_11322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11322_call = mutated_mod.get_global_var('func_11322')
call_11323 = func_11322_call()
output = call_11323
func_11324 = relay.Function([], output)
mutated_mod['func_11324'] = func_11324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10782_call = mod.get_global_var('func_10782')
func_10783_call = mutated_mod.get_global_var('func_10783')
call_11340 = relay.TupleGetItem(func_10782_call(), 0)
call_11341 = relay.TupleGetItem(func_10783_call(), 0)
uop_11342 = relay.acosh(call_11340.astype('float64')) # shape=(11, 12, 4)
uop_11344 = relay.acosh(call_11341.astype('float64')) # shape=(11, 12, 4)
output = relay.Tuple([uop_11342,])
output2 = relay.Tuple([uop_11344,])
func_11369 = relay.Function([], output)
mod['func_11369'] = func_11369
mod = relay.transform.InferType()(mod)
mutated_mod['func_11369'] = func_11369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11369_call = mutated_mod.get_global_var('func_11369')
call_11370 = func_11369_call()
output = call_11370
func_11371 = relay.Function([], output)
mutated_mod['func_11371'] = func_11371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10373_call = mod.get_global_var('func_10373')
func_10374_call = mutated_mod.get_global_var('func_10374')
call_11405 = relay.TupleGetItem(func_10373_call(), 0)
call_11406 = relay.TupleGetItem(func_10374_call(), 0)
output = relay.Tuple([call_11405,])
output2 = relay.Tuple([call_11406,])
func_11409 = relay.Function([], output)
mod['func_11409'] = func_11409
mod = relay.transform.InferType()(mod)
mutated_mod['func_11409'] = func_11409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11409_call = mutated_mod.get_global_var('func_11409')
call_11410 = func_11409_call()
output = call_11410
func_11411 = relay.Function([], output)
mutated_mod['func_11411'] = func_11411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8363_call = mod.get_global_var('func_8363')
func_8365_call = mutated_mod.get_global_var('func_8365')
call_11417 = func_8363_call()
call_11418 = func_8363_call()
func_7906_call = mod.get_global_var('func_7906')
func_7908_call = mutated_mod.get_global_var('func_7908')
call_11441 = relay.TupleGetItem(func_7906_call(), 0)
call_11442 = relay.TupleGetItem(func_7908_call(), 0)
func_6038_call = mod.get_global_var('func_6038')
func_6041_call = mutated_mod.get_global_var('func_6041')
call_11448 = relay.TupleGetItem(func_6038_call(relay.reshape(call_11417.astype('float64'), [14, 7, 9])), 1)
call_11449 = relay.TupleGetItem(func_6041_call(relay.reshape(call_11417.astype('float64'), [14, 7, 9])), 1)
output = relay.Tuple([call_11417,call_11441,call_11448,])
output2 = relay.Tuple([call_11418,call_11442,call_11449,])
func_11454 = relay.Function([], output)
mod['func_11454'] = func_11454
mod = relay.transform.InferType()(mod)
output = func_11454()
func_11455 = relay.Function([], output)
mutated_mod['func_11455'] = func_11455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10471_call = mod.get_global_var('func_10471')
func_10472_call = mutated_mod.get_global_var('func_10472')
call_11480 = func_10471_call()
call_11481 = func_10471_call()
var_11485 = relay.var("var_11485", dtype = "bool", shape = (882,))#candidate|11485|(882,)|var|bool
bop_11486 = relay.bitwise_and(call_11480.astype('int32'), relay.reshape(var_11485.astype('int32'), relay.shape_of(call_11480))) # shape=(882,)
bop_11489 = relay.bitwise_and(call_11481.astype('int32'), relay.reshape(var_11485.astype('int32'), relay.shape_of(call_11481))) # shape=(882,)
output = relay.Tuple([bop_11486,])
output2 = relay.Tuple([bop_11489,])
func_11492 = relay.Function([var_11485,], output)
mod['func_11492'] = func_11492
mod = relay.transform.InferType()(mod)
mutated_mod['func_11492'] = func_11492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11493 = relay.var("var_11493", dtype = "bool", shape = (882,))#candidate|11493|(882,)|var|bool
func_11492_call = mutated_mod.get_global_var('func_11492')
call_11494 = func_11492_call(var_11493)
output = call_11494
func_11495 = relay.Function([var_11493], output)
mutated_mod['func_11495'] = func_11495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7287_call = mod.get_global_var('func_7287')
func_7288_call = mutated_mod.get_global_var('func_7288')
call_11506 = relay.TupleGetItem(func_7287_call(), 0)
call_11507 = relay.TupleGetItem(func_7288_call(), 0)
func_10782_call = mod.get_global_var('func_10782')
func_10783_call = mutated_mod.get_global_var('func_10783')
call_11515 = relay.TupleGetItem(func_10782_call(), 0)
call_11516 = relay.TupleGetItem(func_10783_call(), 0)
func_8058_call = mod.get_global_var('func_8058')
func_8060_call = mutated_mod.get_global_var('func_8060')
call_11517 = relay.TupleGetItem(func_8058_call(), 0)
call_11518 = relay.TupleGetItem(func_8060_call(), 0)
func_6038_call = mod.get_global_var('func_6038')
func_6041_call = mutated_mod.get_global_var('func_6041')
call_11521 = relay.TupleGetItem(func_6038_call(relay.reshape(call_11506.astype('float64'), [14, 7, 9])), 0)
call_11522 = relay.TupleGetItem(func_6041_call(relay.reshape(call_11506.astype('float64'), [14, 7, 9])), 0)
output = relay.Tuple([call_11506,call_11515,call_11517,call_11521,])
output2 = relay.Tuple([call_11507,call_11516,call_11518,call_11522,])
func_11532 = relay.Function([], output)
mod['func_11532'] = func_11532
mod = relay.transform.InferType()(mod)
mutated_mod['func_11532'] = func_11532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11532_call = mutated_mod.get_global_var('func_11532')
call_11533 = func_11532_call()
output = call_11533
func_11534 = relay.Function([], output)
mutated_mod['func_11534'] = func_11534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4850_call = mod.get_global_var('func_4850')
func_4852_call = mutated_mod.get_global_var('func_4852')
call_11574 = relay.TupleGetItem(func_4850_call(), 0)
call_11575 = relay.TupleGetItem(func_4852_call(), 0)
var_11576 = relay.var("var_11576", dtype = "bool", shape = (882,))#candidate|11576|(882,)|var|bool
bop_11577 = relay.bitwise_xor(call_11574.astype('int64'), relay.reshape(var_11576.astype('int64'), relay.shape_of(call_11574))) # shape=(882,)
bop_11580 = relay.bitwise_xor(call_11575.astype('int64'), relay.reshape(var_11576.astype('int64'), relay.shape_of(call_11575))) # shape=(882,)
func_7906_call = mod.get_global_var('func_7906')
func_7908_call = mutated_mod.get_global_var('func_7908')
call_11591 = relay.TupleGetItem(func_7906_call(), 0)
call_11592 = relay.TupleGetItem(func_7908_call(), 0)
output = relay.Tuple([bop_11577,call_11591,])
output2 = relay.Tuple([bop_11580,call_11592,])
func_11595 = relay.Function([var_11576,], output)
mod['func_11595'] = func_11595
mod = relay.transform.InferType()(mod)
var_11596 = relay.var("var_11596", dtype = "bool", shape = (882,))#candidate|11596|(882,)|var|bool
output = func_11595(var_11596)
func_11597 = relay.Function([var_11596], output)
mutated_mod['func_11597'] = func_11597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mod.get_global_var('func_5054')
func_5055_call = mutated_mod.get_global_var('func_5055')
call_11618 = relay.TupleGetItem(func_5054_call(), 2)
call_11619 = relay.TupleGetItem(func_5055_call(), 2)
output = relay.Tuple([call_11618,])
output2 = relay.Tuple([call_11619,])
func_11629 = relay.Function([], output)
mod['func_11629'] = func_11629
mod = relay.transform.InferType()(mod)
output = func_11629()
func_11630 = relay.Function([], output)
mutated_mod['func_11630'] = func_11630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8980_call = mod.get_global_var('func_8980')
func_8982_call = mutated_mod.get_global_var('func_8982')
call_11647 = relay.TupleGetItem(func_8980_call(), 4)
call_11648 = relay.TupleGetItem(func_8982_call(), 4)
output = relay.Tuple([call_11647,])
output2 = relay.Tuple([call_11648,])
func_11652 = relay.Function([], output)
mod['func_11652'] = func_11652
mod = relay.transform.InferType()(mod)
output = func_11652()
func_11653 = relay.Function([], output)
mutated_mod['func_11653'] = func_11653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_11740 = func_5303_call()
call_11741 = func_5303_call()
output = relay.Tuple([call_11740,])
output2 = relay.Tuple([call_11741,])
func_11752 = relay.Function([], output)
mod['func_11752'] = func_11752
mod = relay.transform.InferType()(mod)
output = func_11752()
func_11753 = relay.Function([], output)
mutated_mod['func_11753'] = func_11753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9662_call = mod.get_global_var('func_9662')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_11756 = relay.TupleGetItem(func_9662_call(), 1)
call_11757 = relay.TupleGetItem(func_9663_call(), 1)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_11758 = relay.TupleGetItem(func_5215_call(relay.reshape(call_11756.astype('bool'), [882,])), 5)
call_11759 = relay.TupleGetItem(func_5217_call(relay.reshape(call_11756.astype('bool'), [882,])), 5)
output = relay.Tuple([call_11756,call_11758,])
output2 = relay.Tuple([call_11757,call_11759,])
func_11760 = relay.Function([], output)
mod['func_11760'] = func_11760
mod = relay.transform.InferType()(mod)
mutated_mod['func_11760'] = func_11760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11760_call = mutated_mod.get_global_var('func_11760')
call_11761 = func_11760_call()
output = call_11761
func_11762 = relay.Function([], output)
mutated_mod['func_11762'] = func_11762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_11785 = func_4727_call()
call_11786 = func_4727_call()
func_11760_call = mod.get_global_var('func_11760')
func_11762_call = mutated_mod.get_global_var('func_11762')
call_11800 = relay.TupleGetItem(func_11760_call(), 1)
call_11801 = relay.TupleGetItem(func_11762_call(), 1)
func_4961_call = mod.get_global_var('func_4961')
func_4963_call = mutated_mod.get_global_var('func_4963')
call_11802 = relay.TupleGetItem(func_4961_call(), 0)
call_11803 = relay.TupleGetItem(func_4963_call(), 0)
output = relay.Tuple([call_11785,call_11800,call_11802,])
output2 = relay.Tuple([call_11786,call_11801,call_11803,])
func_11813 = relay.Function([], output)
mod['func_11813'] = func_11813
mod = relay.transform.InferType()(mod)
mutated_mod['func_11813'] = func_11813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11813_call = mutated_mod.get_global_var('func_11813')
call_11814 = func_11813_call()
output = call_11814
func_11815 = relay.Function([], output)
mutated_mod['func_11815'] = func_11815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6771_call = mod.get_global_var('func_6771')
func_6772_call = mutated_mod.get_global_var('func_6772')
call_11838 = func_6771_call()
call_11839 = func_6771_call()
func_598_call = mod.get_global_var('func_598')
func_600_call = mutated_mod.get_global_var('func_600')
var_11848 = relay.var("var_11848", dtype = "int8", shape = (225,))#candidate|11848|(225,)|var|int8
call_11847 = relay.TupleGetItem(func_598_call(relay.reshape(var_11848.astype('int8'), [225,])), 5)
call_11849 = relay.TupleGetItem(func_600_call(relay.reshape(var_11848.astype('int8'), [225,])), 5)
output = relay.Tuple([call_11838,call_11847,var_11848,])
output2 = relay.Tuple([call_11839,call_11849,var_11848,])
func_11850 = relay.Function([var_11848,], output)
mod['func_11850'] = func_11850
mod = relay.transform.InferType()(mod)
var_11851 = relay.var("var_11851", dtype = "int8", shape = (225,))#candidate|11851|(225,)|var|int8
output = func_11850(var_11851)
func_11852 = relay.Function([var_11851], output)
mutated_mod['func_11852'] = func_11852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9986_call = mod.get_global_var('func_9986')
func_9988_call = mutated_mod.get_global_var('func_9988')
call_11903 = relay.TupleGetItem(func_9986_call(), 1)
call_11904 = relay.TupleGetItem(func_9988_call(), 1)
output = relay.Tuple([call_11903,])
output2 = relay.Tuple([call_11904,])
func_11914 = relay.Function([], output)
mod['func_11914'] = func_11914
mod = relay.transform.InferType()(mod)
mutated_mod['func_11914'] = func_11914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11914_call = mutated_mod.get_global_var('func_11914')
call_11915 = func_11914_call()
output = call_11915
func_11916 = relay.Function([], output)
mutated_mod['func_11916'] = func_11916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_11966 = func_4727_call()
call_11967 = func_4727_call()
output = call_11966
output2 = call_11967
func_11982 = relay.Function([], output)
mod['func_11982'] = func_11982
mod = relay.transform.InferType()(mod)
output = func_11982()
func_11983 = relay.Function([], output)
mutated_mod['func_11983'] = func_11983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10318_call = mod.get_global_var('func_10318')
func_10320_call = mutated_mod.get_global_var('func_10320')
call_12037 = relay.TupleGetItem(func_10318_call(), 0)
call_12038 = relay.TupleGetItem(func_10320_call(), 0)
output = relay.Tuple([call_12037,])
output2 = relay.Tuple([call_12038,])
func_12039 = relay.Function([], output)
mod['func_12039'] = func_12039
mod = relay.transform.InferType()(mod)
mutated_mod['func_12039'] = func_12039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12039_call = mutated_mod.get_global_var('func_12039')
call_12040 = func_12039_call()
output = call_12040
func_12041 = relay.Function([], output)
mutated_mod['func_12041'] = func_12041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11409_call = mod.get_global_var('func_11409')
func_11411_call = mutated_mod.get_global_var('func_11411')
call_12044 = relay.TupleGetItem(func_11409_call(), 0)
call_12045 = relay.TupleGetItem(func_11411_call(), 0)
output = relay.Tuple([call_12044,])
output2 = relay.Tuple([call_12045,])
func_12065 = relay.Function([], output)
mod['func_12065'] = func_12065
mod = relay.transform.InferType()(mod)
mutated_mod['func_12065'] = func_12065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12065_call = mutated_mod.get_global_var('func_12065')
call_12066 = func_12065_call()
output = call_12066
func_12067 = relay.Function([], output)
mutated_mod['func_12067'] = func_12067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10373_call = mod.get_global_var('func_10373')
func_10374_call = mutated_mod.get_global_var('func_10374')
call_12114 = relay.TupleGetItem(func_10373_call(), 0)
call_12115 = relay.TupleGetItem(func_10374_call(), 0)
uop_12122 = relay.log2(call_12114.astype('float32')) # shape=(11, 12, 4)
uop_12124 = relay.log2(call_12115.astype('float32')) # shape=(11, 12, 4)
output = relay.Tuple([uop_12122,])
output2 = relay.Tuple([uop_12124,])
func_12128 = relay.Function([], output)
mod['func_12128'] = func_12128
mod = relay.transform.InferType()(mod)
mutated_mod['func_12128'] = func_12128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12128_call = mutated_mod.get_global_var('func_12128')
call_12129 = func_12128_call()
output = call_12129
func_12130 = relay.Function([], output)
mutated_mod['func_12130'] = func_12130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9408_call = mod.get_global_var('func_9408')
func_9410_call = mutated_mod.get_global_var('func_9410')
call_12139 = relay.TupleGetItem(func_9408_call(), 0)
call_12140 = relay.TupleGetItem(func_9410_call(), 0)
output = call_12139
output2 = call_12140
func_12145 = relay.Function([], output)
mod['func_12145'] = func_12145
mod = relay.transform.InferType()(mod)
output = func_12145()
func_12146 = relay.Function([], output)
mutated_mod['func_12146'] = func_12146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12039_call = mod.get_global_var('func_12039')
func_12041_call = mutated_mod.get_global_var('func_12041')
call_12163 = relay.TupleGetItem(func_12039_call(), 0)
call_12164 = relay.TupleGetItem(func_12041_call(), 0)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_12167 = relay.TupleGetItem(func_1401_call(relay.reshape(call_12163.astype('bool'), [14, 7, 9])), 0)
call_12168 = relay.TupleGetItem(func_1403_call(relay.reshape(call_12163.astype('bool'), [14, 7, 9])), 0)
func_11760_call = mod.get_global_var('func_11760')
func_11762_call = mutated_mod.get_global_var('func_11762')
call_12185 = relay.TupleGetItem(func_11760_call(), 0)
call_12186 = relay.TupleGetItem(func_11762_call(), 0)
output = relay.Tuple([call_12163,call_12167,call_12185,])
output2 = relay.Tuple([call_12164,call_12168,call_12186,])
func_12190 = relay.Function([], output)
mod['func_12190'] = func_12190
mod = relay.transform.InferType()(mod)
output = func_12190()
func_12191 = relay.Function([], output)
mutated_mod['func_12191'] = func_12191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7518_call = mod.get_global_var('func_7518')
func_7519_call = mutated_mod.get_global_var('func_7519')
call_12253 = func_7518_call()
call_12254 = func_7518_call()
output = relay.Tuple([call_12253,])
output2 = relay.Tuple([call_12254,])
func_12277 = relay.Function([], output)
mod['func_12277'] = func_12277
mod = relay.transform.InferType()(mod)
output = func_12277()
func_12278 = relay.Function([], output)
mutated_mod['func_12278'] = func_12278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11652_call = mod.get_global_var('func_11652')
func_11653_call = mutated_mod.get_global_var('func_11653')
call_12315 = relay.TupleGetItem(func_11652_call(), 0)
call_12316 = relay.TupleGetItem(func_11653_call(), 0)
output = relay.Tuple([call_12315,])
output2 = relay.Tuple([call_12316,])
func_12319 = relay.Function([], output)
mod['func_12319'] = func_12319
mod = relay.transform.InferType()(mod)
output = func_12319()
func_12320 = relay.Function([], output)
mutated_mod['func_12320'] = func_12320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8058_call = mod.get_global_var('func_8058')
func_8060_call = mutated_mod.get_global_var('func_8060')
call_12396 = relay.TupleGetItem(func_8058_call(), 0)
call_12397 = relay.TupleGetItem(func_8060_call(), 0)
const_12401 = relay.const([[-5.290993,-7.054022,-0.624563,9.232377,-9.418104,1.531993,-7.159432,-3.128729,-3.996801,4.211454,2.221374,4.636644,4.433731],[-4.757758,-6.487785,5.506692,1.238115,-3.117127,9.190449,-5.030797,-2.274533,-2.769738,9.939098,7.154725,-4.066799,7.297255],[-0.596569,-7.967995,2.690501,-1.125358,-0.569389,-2.115731,9.308248,-1.785394,-9.882009,3.270506,-4.000423,2.566540,-7.324582],[6.663034,-5.829804,-3.797347,4.470968,-7.375421,7.765450,1.567735,-4.027736,3.059186,-8.134001,-2.483880,0.406868,-9.205555],[1.462769,4.005083,-1.662611,-0.967803,-3.023509,8.934351,1.948985,-7.454015,-7.586660,7.290193,3.738502,-5.396551,-5.521570],[-0.242685,-9.870809,2.427200,-1.526354,5.255605,-5.300517,7.355338,9.076858,-0.334104,-5.689725,5.758782,-5.840282,2.550132],[-1.259619,-7.991363,-7.133064,-6.146432,1.812721,-0.105325,-7.359432,-3.352070,-9.695681,9.510173,-0.586282,-9.779157,-5.895350],[4.130263,-5.312755,-4.171028,-6.999075,2.917617,2.220502,-4.592999,-5.589581,7.534214,-5.283014,3.984701,4.511734,-3.167344],[-8.881128,5.506209,2.839410,-1.484416,6.073402,-4.900875,8.596967,4.964302,4.056764,9.712927,-2.809358,-8.501173,-3.523716],[3.617893,8.730992,3.054611,1.202219,-4.695527,0.247695,-9.177404,-4.672524,-9.221486,8.866470,-9.663902,0.929076,-1.398998],[-3.024728,6.952411,-6.423791,6.041685,-2.198571,0.988727,0.310751,-0.141329,-9.238402,7.397980,7.572154,-4.469019,9.663375],[4.342000,-9.095610,9.904443,7.977250,1.764906,1.900547,7.822741,7.562211,5.154441,-3.858335,9.215727,2.265795,9.444650],[7.226932,6.979980,1.570506,8.387609,-3.055548,-5.589330,2.513552,5.751121,-6.811447,8.741969,0.716297,-0.104639,-0.559250],[1.496178,8.778133,3.936597,-8.504680,2.648847,6.650191,-6.478611,0.357716,0.960373,-9.851369,-3.870914,7.256547,7.573508],[-8.941920,2.325335,3.126884,-4.204168,0.926348,6.074190,-9.072214,6.395552,-8.782061,9.031772,4.447245,-6.477507,0.643162],[-9.029014,-7.323467,-4.729336,-1.298645,-9.327575,-6.109420,-8.218627,-9.795885,7.045152,-1.924851,-5.695250,-9.072787,3.889251],[1.494191,-4.270637,-2.515207,4.700646,-2.039340,4.614107,2.660857,-0.026594,6.152650,-5.119349,9.538102,-9.266614,-1.358779],[-1.065375,9.442739,-2.906839,9.184389,5.796524,-1.643018,1.380193,-6.236201,9.046403,-2.504391,9.156175,-5.383321,6.204590],[-5.663655,6.531120,-4.187691,6.395207,7.239325,-0.037066,-2.709970,-9.397339,6.514402,7.970839,5.091399,6.435898,2.743589],[0.601921,-0.270534,9.902078,-2.958917,-8.271336,-1.982285,-2.443772,1.668855,-0.173458,8.357561,-9.558993,-0.994113,-2.065895],[-1.259083,5.457048,5.283301,9.490109,8.748681,-7.886349,-0.958498,1.862140,-2.625394,-4.708105,-9.910942,-5.194587,-0.010903],[-7.331202,-4.062717,-2.925570,9.695670,-3.635121,-7.397561,-6.045424,-4.028607,6.897351,3.179176,3.626725,2.026657,-0.643560],[0.842003,3.209408,4.921109,-1.288791,-7.108008,2.187394,4.880558,-4.529249,3.392677,6.239888,1.329834,-6.478064,6.441578],[4.637137,-0.689560,4.132819,-6.728255,3.851190,-5.890343,8.777191,-3.045936,-6.993199,0.020274,4.293583,-8.248722,-7.440494],[6.439210,-0.986541,9.390891,7.719813,5.495181,8.973475,8.928853,-5.325867,-9.710608,8.663178,-4.656108,-2.385607,-2.081092],[-6.954046,9.172405,3.374700,-7.565767,8.677900,6.541989,1.602769,8.399868,-5.267966,9.648333,7.408641,-5.821188,-2.467177],[-1.823617,-9.479106,-0.191850,1.811663,-4.902516,-1.702256,1.246807,-0.673881,0.792138,5.319254,-9.326435,6.642915,-4.662326],[5.455781,0.191142,5.115396,1.592457,1.742629,3.682739,5.331183,1.182458,-5.311974,0.863755,9.794663,-2.844006,-3.771618],[-5.337463,-0.398603,-6.059519,9.610063,7.128420,6.435528,7.921349,-5.717875,-2.746640,-8.384477,4.915451,-2.047338,8.320213],[1.546887,-3.908944,-4.732813,-7.400584,-7.444316,-8.289485,-8.301558,-5.790943,-5.472780,-8.015262,-4.188577,-0.136288,-8.633509],[9.699871,8.061922,-9.606634,-1.702815,-4.417624,8.662352,3.960687,8.927537,-8.431971,9.515162,3.806110,-1.335476,-0.135797],[-5.159920,2.025482,7.706682,2.676305,7.733339,1.635236,2.106077,-8.261908,-7.364388,-8.686239,4.380036,-3.677376,3.263893],[9.698534,8.398666,4.816643,-3.705855,2.010918,7.327636,-5.545309,-5.488326,0.182916,8.366683,8.167820,3.865578,8.016690],[-5.706557,-7.978832,-4.767116,9.162365,4.623323,7.297027,7.987078,9.152378,-4.985982,7.300240,-1.605241,-3.041700,-8.137540],[1.705334,2.383667,-7.127045,-7.969240,3.721421,-2.617248,8.225403,1.689213,-4.401112,6.143064,-2.591042,7.332967,-6.163380],[-9.672599,-9.229934,-2.629822,-0.913993,-8.560109,8.109291,8.970279,8.019053,0.298697,-9.382992,-3.747417,2.566594,-7.055756],[8.688323,2.801885,5.450727,-3.061118,-2.767259,-3.597719,-3.813327,-9.648831,4.327844,-7.767904,0.437935,0.494506,7.910231],[-6.819467,7.057520,-2.188952,4.263125,1.886084,6.313100,-2.259161,-2.672135,-7.554522,1.594682,5.895678,9.225584,-6.066334],[1.658427,-2.109413,2.956123,-3.524347,8.333361,8.526026,-4.631532,-7.821612,-2.878063,-4.291126,7.515293,7.409402,5.609016]], dtype = "float64")#candidate|12401|(39, 13)|const|float64
bop_12402 = relay.bitwise_or(call_12396.astype('uint16'), relay.reshape(const_12401.astype('uint16'), relay.shape_of(call_12396))) # shape=(39, 13)
bop_12405 = relay.bitwise_or(call_12397.astype('uint16'), relay.reshape(const_12401.astype('uint16'), relay.shape_of(call_12397))) # shape=(39, 13)
output = bop_12402
output2 = bop_12405
func_12408 = relay.Function([], output)
mod['func_12408'] = func_12408
mod = relay.transform.InferType()(mod)
mutated_mod['func_12408'] = func_12408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12408_call = mutated_mod.get_global_var('func_12408')
call_12409 = func_12408_call()
output = call_12409
func_12410 = relay.Function([], output)
mutated_mod['func_12410'] = func_12410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9662_call = mod.get_global_var('func_9662')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_12411 = relay.TupleGetItem(func_9662_call(), 2)
call_12412 = relay.TupleGetItem(func_9663_call(), 2)
output = call_12411
output2 = call_12412
func_12420 = relay.Function([], output)
mod['func_12420'] = func_12420
mod = relay.transform.InferType()(mod)
output = func_12420()
func_12421 = relay.Function([], output)
mutated_mod['func_12421'] = func_12421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10850_call = mod.get_global_var('func_10850')
func_10852_call = mutated_mod.get_global_var('func_10852')
call_12468 = relay.TupleGetItem(func_10850_call(), 2)
call_12469 = relay.TupleGetItem(func_10852_call(), 2)
uop_12470 = relay.cos(call_12468.astype('float64')) # shape=(98, 9)
uop_12472 = relay.cos(call_12469.astype('float64')) # shape=(98, 9)
func_2491_call = mod.get_global_var('func_2491')
func_2495_call = mutated_mod.get_global_var('func_2495')
const_12474 = relay.const([4,-6,2,5,10,3,-1,1,-7,6,10,1,10,-4,-3,-8,10,-9,3,-8,-5,2,2,-5,2,8,5,3,-9,6,3,-10,-9,7,10,-7,-8,2,-4,10,-8,7,8,-1,-4,-10,2,-2,-6,4,-4,-2,2,4,-10,-2,-1,-2,-9,-5,-1,-2,4,3,-2,-7,-10,1,-2,9,-7,10,2,-6,-6,-5,-7,-9,10,-2,-1,-1,9,-4,-6,5,-8,3,7,-10,-2,10,-4,2,-1,8,-3,-4,10,-3,2,10,-3,9,-2,-2,6,4,1,3,10,5,-10,-6,-6,7,-9,10,-1,3,-10,8,9,5,9,1,3,3,-4,4,-1,9,-1,1,8,7,-1,3,8,9,9,-9,5,-6,2,-10,-2,-3,8,6,10,-1,8,-2,-3,6,-10,-4,6,5,-9,-10,-3,-5,1,-6,-5,-3,-2,-9,-5,-9,-9,-1,3,2,-2,-5,7,6,3,10,-9,-1,7,10,-7,4,-3,1,-2,10,-7,-7,-6,2,-4,-9,5,-8,4,-2,-6,-8,-3,5,-4,-7,1,-3,8,-8,8,-9,-9,-5,4,5,6,-9,4,6,8,-9,9,7,9,-4,-5,2,-10,9,4,6,-1,1,-8,5,2,4,-6,-1,-8,-4,9,-7,2,-5,-3,-10,-5,-10,-10,6,9,-3,2,-9,-10,3,10,-10,-7,-1,-5,3,-4,10,7,3,-9,10,10,-4,-6,-10,7,9,5,4,-2,10,1,-9,-8,-6,-1,-10,8,3,-1,10,-3,3,10,-9,-4,10,9,-6,6,-7,8,7,-1,2,3,1,-1,-3,-2,5,1,1,-7,-10,9,-9,3,5,-6,10,-8,-7,-5,-10,-5,3,10,-6,3,1,3,10,-6,2,3,3,-2,10,1,6,-5,-1,-5,4,-5,9,-3,-4,4,-2,9,-8,-8,-10,-8,-4,-9,8,4,-1,6,-6,7,-1,7,7,1,-9,-2,9,-7,-3,-9,-10,6,3,1,3,3,-8,7,8,-9,-6,-6,-2,-7,-9,9,-1,-1,7,8,-10,1,-1,3,6,-4,6,-9,-3,5,-5,3,1,2,6,7,-1,3,-7,-1,10,-7,-7,5,3,4,-8,5,3,-7,-7,6,-3,2,-7,4,10,6,-8,-9,-2,-8,-2,-10,-2,3,-1,9,-7,-3,4,4,9,-1,-10,9,-3,-4,1,9,1,3,10,6,-3,-4,8,-2,5,-5,6,-8,-10,6,-8,-5,7,-3,-1,6,9,2,-5,6,10,6,-3,6,7,-5,7,4,-7,2,-5,4,10,1,2,7,9,9,8,-5,9,9,-1,1,9,8,4,8], dtype = "int64")#candidate|12474|(507,)|const|int64
call_12473 = relay.TupleGetItem(func_2491_call(relay.reshape(const_12474.astype('int64'), [13, 3, 13]), relay.reshape(const_12474.astype('int64'), [13, 3, 13]), relay.reshape(const_12474.astype('bool'), [13, 3, 13]), ), 2)
call_12475 = relay.TupleGetItem(func_2495_call(relay.reshape(const_12474.astype('int64'), [13, 3, 13]), relay.reshape(const_12474.astype('int64'), [13, 3, 13]), relay.reshape(const_12474.astype('bool'), [13, 3, 13]), ), 2)
func_2380_call = mod.get_global_var('func_2380')
func_2383_call = mutated_mod.get_global_var('func_2383')
const_12490 = relay.const([[7.618285,4.905044],[0.234051,-3.833789],[-4.816327,7.697715],[2.513409,0.444020],[3.692148,0.777136],[-5.936656,-3.630615],[-7.962036,-7.708926],[-0.890780,-1.013737],[2.443570,-7.685374],[7.765207,-7.013560],[3.768942,3.308364],[-8.055312,-1.739085],[1.043824,-3.230551],[-3.397205,6.455848],[-9.426505,-0.550861],[8.269783,0.352378],[-4.321684,6.465010],[-1.139866,-1.790606],[2.499773,3.697817],[-7.513683,3.332399],[5.435861,1.363750],[-3.180060,-3.982140],[0.575224,-4.204470],[6.508694,8.706645],[9.617097,-7.714851],[-5.786925,9.086537],[-4.055094,0.931982],[-6.848828,2.730068],[3.084632,5.771640],[7.232602,-7.063629],[-7.072566,7.791786],[-0.664794,-5.125620],[1.760197,-8.291124],[9.791507,-9.168877],[-0.242963,-2.514813],[-1.900080,-1.218960],[-4.257443,-0.381400],[6.736141,-8.239416],[7.577144,2.038300],[4.043545,3.169788],[-4.999660,-8.111376],[6.817074,-3.836762],[6.816427,-3.084448],[-4.403629,9.956834],[-2.166087,-6.857025],[-1.881585,-7.986181],[-5.109189,-5.403228],[0.584222,-1.834201],[7.337628,1.013058],[6.519278,-9.943840],[-3.412045,1.255821],[6.654650,6.554321],[-8.475766,1.151753],[4.702533,-2.663575],[3.639196,1.088914],[-3.788164,9.715181],[-9.179445,-2.504918],[-0.210633,-4.958405],[9.650528,9.103176],[-1.901878,-8.939245],[-3.212784,-4.085308],[5.127501,9.819469],[3.672172,5.332506],[-1.975968,3.008681],[8.859069,4.474639],[-5.301025,-4.966078],[3.894944,-9.867087],[5.485640,-2.396210],[-3.641408,1.188640],[2.745930,-6.357532],[8.051452,-7.126679],[-3.395013,-7.684732],[2.311206,8.764529],[-9.072120,6.876475],[2.306156,9.197730],[-8.741330,-5.189234],[-3.236856,9.237869],[-0.255040,-4.092705],[4.547619,-6.940139],[-9.582305,-5.452216],[-1.807090,4.575119],[8.271214,-5.178249],[-8.051562,3.094437],[0.471683,6.719183],[3.720952,6.975899],[1.208440,1.844342],[-0.453348,-8.079911],[8.566056,-8.283120],[6.864090,-6.162423],[-7.055738,0.042743],[-7.001772,4.214779],[3.496817,-4.067575],[0.852817,-5.568163],[7.628566,-1.136706],[1.547634,3.564823],[9.021555,-3.987483],[0.516919,3.524716],[5.346424,1.081824],[-2.257468,6.116595],[0.785480,-9.999719],[7.631435,5.011074],[0.817628,-6.813329],[4.312667,3.410293],[0.680365,1.257937],[-4.195365,-3.171436],[3.309053,0.251728],[1.639308,8.406423],[-1.014131,4.371436],[2.038062,5.239480],[-9.335947,0.101804],[7.636093,-5.109709],[6.221488,8.155697],[2.858173,3.665292],[4.652659,-4.768553],[-1.316992,-8.546042],[5.465186,-5.673939],[-4.192285,9.704789],[-6.470248,-3.651950],[7.135581,-0.104096],[-1.644726,-3.713838],[-0.091974,9.826580],[0.265843,-8.770128],[5.835511,-0.017685],[-8.737686,8.102844],[-3.039133,-2.888708],[-8.828086,-6.544180],[4.676191,-8.232097],[8.076227,4.809929],[-1.134271,4.175638],[-3.057612,0.870707],[-1.448765,3.150048],[8.136854,-3.107649],[3.248253,-4.322877],[4.112549,-7.257601],[1.058191,1.035255],[8.250511,-7.418368],[1.887009,9.670970],[7.554994,5.388168],[2.646067,7.124311],[-8.791795,-4.794128],[-0.087733,6.785196],[-1.052216,-0.990510],[-8.501336,-1.134455],[9.550592,7.212315],[-0.708766,-6.875183],[-5.909174,-4.988850],[-4.242994,-6.687394],[0.786374,1.823903],[0.860895,4.519999],[-5.369568,1.184879],[3.803724,-1.100653],[0.139406,2.864170],[8.080311,3.312518],[-2.548062,2.900009],[1.263775,0.421664],[-4.169846,-3.693802],[9.772890,9.413167],[-1.110100,-5.588928],[-2.801633,-7.358414],[-5.421957,-8.265545],[6.860449,3.934439],[7.751664,4.650569],[-3.825339,9.399781],[6.904999,-4.099335],[1.709878,-7.005135],[3.618120,-1.461145],[0.853504,5.475109],[-3.733150,8.228602],[2.095682,4.642414],[6.851373,-6.954843],[5.843524,1.285661],[6.186631,5.583412],[9.182476,-7.454284],[-1.187634,8.988176],[0.918229,-8.707902],[-3.464659,-1.999038],[-0.253963,-1.700040],[-3.035204,-3.327544],[-8.403215,-4.150694],[5.094724,-8.090722],[6.110589,5.498070],[8.437749,1.409317],[3.252246,4.926031],[-3.320973,-9.381545],[5.613207,-7.702530],[0.811600,-1.471492],[-5.572625,9.513177],[-8.967770,0.276002],[7.819539,-3.781152],[8.011767,1.621830],[5.667703,-1.597848],[-7.368937,-3.282189],[7.067483,3.678122],[9.069098,-4.565165],[-7.903110,-0.369505],[3.980727,-3.248843],[-7.815142,-5.854945],[8.944245,7.260589],[-5.781102,-3.385107],[-0.723993,-7.492717],[6.425902,-2.527111],[5.592980,2.754863],[-8.390815,5.760554],[8.726193,-6.387200],[-8.378869,4.963616],[3.157292,-3.076626],[-1.783068,-5.474689],[4.918416,-7.897299],[6.133652,-9.013211],[4.843196,-5.528293],[6.358496,1.492179],[-5.003953,-7.944880],[-0.963658,-0.037522],[-0.147653,7.529780],[2.536243,9.014579],[8.854264,9.770508],[-0.677416,1.533666],[6.447363,-9.795032],[6.728315,8.344833],[9.154314,-3.055573],[1.096745,8.692858],[8.213119,-4.884301],[8.185016,-8.802678],[0.928316,9.628600],[2.999822,6.215253],[-9.460347,5.374424],[-4.624448,9.906332],[-3.639950,6.636644],[-8.564467,-5.716225],[-7.840930,-4.319337],[-0.644776,-8.929531],[5.250334,-8.477039],[-0.464200,3.426748],[9.176565,3.240142],[-1.860241,8.452783],[-8.089557,-2.505886],[-6.908984,1.199609],[-2.612266,-4.240269],[-6.252529,-0.931394],[-8.094816,-2.993834],[7.235802,1.444659],[-3.883962,-6.087747],[-0.233608,0.167768],[-7.017979,7.683472],[-4.028562,3.621098],[5.324172,-9.976165],[-6.585130,2.024484],[8.563093,-0.763929],[5.068567,6.909584],[-5.768798,-3.785079],[2.696789,0.643902],[-0.287659,-7.353441],[0.193281,1.656826],[4.209825,-0.641687],[-6.752797,-4.963480],[2.133134,-0.802212],[8.010452,-4.699963],[5.315844,-5.056204],[7.730462,2.854905],[-9.454284,-5.138415],[0.251200,-2.549329],[5.503633,7.677661],[-7.936542,8.410231],[-7.925144,8.402799],[9.841899,6.630252],[-6.653939,-2.915263],[3.802776,9.289346],[0.014839,-4.948694],[0.423838,-2.224149],[1.193056,1.854979],[4.929511,-3.557070],[-3.444073,3.617196],[8.921768,0.283325],[-2.214914,4.808096],[5.520042,-3.634143],[4.349909,3.540811],[7.640416,6.598837],[9.897065,5.898024],[-9.952244,-2.529746],[0.508576,-3.256767],[-7.959004,-0.928238],[2.781167,4.270337],[9.690901,-0.985637],[-3.027649,7.169810],[0.028641,-4.398781],[6.877977,4.400599],[6.440310,8.737226],[-1.404836,-3.789781],[3.747050,0.390210],[-2.316837,7.523529],[-8.509040,-9.498019],[7.228661,0.124662],[3.615903,-5.036846],[4.852510,-4.479016],[3.099345,2.525210],[0.021430,5.456087],[-1.093813,-3.318645],[2.485659,-2.069798],[9.222743,-0.955969],[5.587892,3.838349],[2.150019,3.021319],[9.211258,-2.513464],[2.262149,-2.540455],[2.999429,1.905335],[2.269003,-9.999901],[2.954493,-2.761727],[-7.408311,-8.177655],[-0.619630,-7.443451],[7.575381,-7.607617],[0.732432,9.973615],[-2.050091,9.130386],[7.799295,-5.973767],[-0.371215,9.748052],[8.024062,-3.813123],[-6.185523,0.202078],[-5.072604,0.909538],[-3.357030,3.057612],[-3.225729,-1.322766],[-5.710571,-3.615884],[7.235385,-7.453032],[6.942370,0.896867],[-8.382142,-4.292042],[-9.014236,6.829069],[4.145568,-7.132339],[7.079738,9.247912],[9.494163,-0.301572],[-8.915273,6.164286],[1.586997,6.676997],[-4.136802,-6.953865],[8.275192,3.911368],[-7.750745,-6.336038],[1.243527,3.905440],[-0.434776,-5.053766],[8.214419,-9.539147],[5.300176,5.717459],[8.272348,-7.553976],[2.720171,-8.980307],[6.925547,5.392077],[3.478435,-3.651998],[-3.863984,9.873480],[-5.838029,-1.499252],[-5.141555,4.228533],[2.656512,6.110130],[-0.362430,-5.190572],[-1.480179,-6.105893],[-6.514790,5.535664],[4.937884,7.854204],[-4.446715,9.502784],[-1.556693,-6.289885],[-2.789917,5.789634],[-9.612925,-0.805671],[-8.419460,-1.391241],[-9.349447,-1.639155],[-2.507416,-2.772650],[1.726182,-3.064246],[-8.567928,9.001208],[0.276193,2.244811],[0.886370,8.849102],[8.930116,-3.426808],[-1.324179,-3.974564],[4.194243,-9.009008],[4.127475,-2.333182],[-4.568818,-8.781073],[-4.378085,5.255248]], dtype = "float64")#candidate|12490|(364, 2)|const|float64
const_12491 = relay.const([-3,-10,1,10,-2,4,-10,6,-9,-8,4,-7,-6,9,3,9,-8,-3,-9,-2,7,5,-7,1,-9,-2,2,5,2,-1,3,-3,1,8,2,-8,-8,-6,-7,-10,8,9,-3,8,-8,2,-1,2,2,9,-10,3,-2,-2,8,5,-3,-5,-3,-2,2,-2,-9,-4,-4,7,1,-1,-8,4,-4,1,-7,6,7,-9,-3,1,-7,5,7,-5,-1,-1,-1,5,6,-3,-10,3,6,-8,4,1,4,1,7,2,-4,6,-10,9,5,-8,-10,4,-2,-4,-2,8,-2,-9,-6,-6,-4,6,-5,9,-6,7,-8,3,-3,-8,6,1,4,-7,-1,-1,-9,-6,-1,-4,-1,-4,-10,-1,-7,-8,-3,-9,8,-9,10,1,-6,-4,3,-3,-7,-5,7,-1,-5,7,9,6,3,6,5,5,-8,6,4,-8,-10,9,-9,2,-1,-1,-5,8,2,3,3,9,-6,-3,-6,-3,-5,6,5,7,8,-8,9,-3,2,-8,-4,8,-4,10,3,-8,6,-2,3,8,-1,8,-4,1,-7,-5,-8,2,-6,-1,6,9,5,-4,3,2,10,-4,-1,2,-5,-10,2], dtype = "int8")#candidate|12491|(225,)|const|int8
call_12489 = relay.TupleGetItem(func_2380_call(relay.reshape(const_12490.astype('float64'), [13, 8, 7]), relay.reshape(const_12491.astype('int8'), [225,]), ), 1)
call_12492 = relay.TupleGetItem(func_2383_call(relay.reshape(const_12490.astype('float64'), [13, 8, 7]), relay.reshape(const_12491.astype('int8'), [225,]), ), 1)
uop_12500 = relay.log10(const_12490.astype('float64')) # shape=(364, 2)
bop_12504 = relay.greater_equal(uop_12500.astype('bool'), relay.reshape(const_12490.astype('bool'), relay.shape_of(uop_12500))) # shape=(364, 2)
output = relay.Tuple([uop_12470,call_12473,const_12474,call_12489,const_12491,bop_12504,])
output2 = relay.Tuple([uop_12472,call_12475,const_12474,call_12492,const_12491,bop_12504,])
func_12516 = relay.Function([], output)
mod['func_12516'] = func_12516
mod = relay.transform.InferType()(mod)
mutated_mod['func_12516'] = func_12516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12516_call = mutated_mod.get_global_var('func_12516')
call_12517 = func_12516_call()
output = call_12517
func_12518 = relay.Function([], output)
mutated_mod['func_12518'] = func_12518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8735_call = mod.get_global_var('func_8735')
func_8737_call = mutated_mod.get_global_var('func_8737')
call_12547 = relay.TupleGetItem(func_8735_call(), 2)
call_12548 = relay.TupleGetItem(func_8737_call(), 2)
output = relay.Tuple([call_12547,])
output2 = relay.Tuple([call_12548,])
func_12555 = relay.Function([], output)
mod['func_12555'] = func_12555
mod = relay.transform.InferType()(mod)
output = func_12555()
func_12556 = relay.Function([], output)
mutated_mod['func_12556'] = func_12556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5273_call = mod.get_global_var('func_5273')
func_5274_call = mutated_mod.get_global_var('func_5274')
call_12577 = relay.TupleGetItem(func_5273_call(), 0)
call_12578 = relay.TupleGetItem(func_5274_call(), 0)
func_11454_call = mod.get_global_var('func_11454')
func_11455_call = mutated_mod.get_global_var('func_11455')
call_12612 = relay.TupleGetItem(func_11454_call(), 2)
call_12613 = relay.TupleGetItem(func_11455_call(), 2)
func_8980_call = mod.get_global_var('func_8980')
func_8982_call = mutated_mod.get_global_var('func_8982')
call_12614 = relay.TupleGetItem(func_8980_call(), 0)
call_12615 = relay.TupleGetItem(func_8982_call(), 0)
output = relay.Tuple([call_12577,call_12612,call_12614,])
output2 = relay.Tuple([call_12578,call_12613,call_12615,])
func_12636 = relay.Function([], output)
mod['func_12636'] = func_12636
mod = relay.transform.InferType()(mod)
mutated_mod['func_12636'] = func_12636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12636_call = mutated_mod.get_global_var('func_12636')
call_12637 = func_12636_call()
output = call_12637
func_12638 = relay.Function([], output)
mutated_mod['func_12638'] = func_12638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6771_call = mod.get_global_var('func_6771')
func_6772_call = mutated_mod.get_global_var('func_6772')
call_12660 = func_6771_call()
call_12661 = func_6771_call()
output = call_12660
output2 = call_12661
func_12672 = relay.Function([], output)
mod['func_12672'] = func_12672
mod = relay.transform.InferType()(mod)
mutated_mod['func_12672'] = func_12672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12672_call = mutated_mod.get_global_var('func_12672')
call_12673 = func_12672_call()
output = call_12673
func_12674 = relay.Function([], output)
mutated_mod['func_12674'] = func_12674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11652_call = mod.get_global_var('func_11652')
func_11653_call = mutated_mod.get_global_var('func_11653')
call_12739 = relay.TupleGetItem(func_11652_call(), 0)
call_12740 = relay.TupleGetItem(func_11653_call(), 0)
func_6436_call = mod.get_global_var('func_6436')
func_6438_call = mutated_mod.get_global_var('func_6438')
call_12765 = relay.TupleGetItem(func_6436_call(), 0)
call_12766 = relay.TupleGetItem(func_6438_call(), 0)
uop_12769 = relay.sqrt(call_12739.astype('float32')) # shape=(11, 12, 4)
uop_12771 = relay.sqrt(call_12740.astype('float32')) # shape=(11, 12, 4)
output = relay.Tuple([call_12765,uop_12769,])
output2 = relay.Tuple([call_12766,uop_12771,])
F = relay.Function([], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([], output2)
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
