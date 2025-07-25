import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_88 = relay.var("var_88", dtype = "float32", shape = (15, 9, 3))#candidate|88|(15, 9, 3)|var|float32
uop_89 = relay.tan(var_88.astype('float32')) # shape=(15, 9, 3)
bop_119 = relay.bitwise_and(uop_89.astype('uint32'), relay.reshape(var_88.astype('uint32'), relay.shape_of(uop_89))) # shape=(15, 9, 3)
uop_138 = relay.acosh(uop_89.astype('float32')) # shape=(15, 9, 3)
output = relay.Tuple([bop_119,uop_138,])
output2 = relay.Tuple([bop_119,uop_138,])
func_140 = relay.Function([var_88,], output)
mod['func_140'] = func_140
mod = relay.transform.InferType()(mod)
var_141 = relay.var("var_141", dtype = "float32", shape = (15, 9, 3))#candidate|141|(15, 9, 3)|var|float32
output = func_140(var_141)
func_142 = relay.Function([var_141], output)
mutated_mod['func_142'] = func_142
mutated_mod = relay.transform.InferType()(mutated_mod)
const_285 = relay.const([[[-1.763230,-3.631516],[7.554839,4.681204],[-4.639150,5.914401],[-0.557264,5.049897],[-1.431662,-1.740911],[-8.689392,7.420033],[-6.855648,-5.209086],[-2.744201,-0.485518]],[[-3.268992,-2.501677],[4.182133,9.239373],[0.906565,4.719616],[8.036743,3.519121],[7.038906,3.046266],[-3.613168,-4.746795],[-7.858764,-0.371845],[-7.546878,-7.449491]],[[5.041489,-3.019974],[-4.298870,4.836626],[-4.814831,2.597824],[2.902189,-4.322410],[2.490420,-5.637068],[-9.799785,-9.371286],[1.763096,0.706289],[5.842211,-7.304981]],[[2.950992,4.511860],[0.714389,2.109451],[5.856579,3.271034],[-4.081713,-4.175279],[0.003140,0.139640],[5.589562,-9.721582],[-1.445691,3.601992],[8.593572,8.080410]],[[-6.213400,-1.680318],[4.771407,-7.068040],[6.852315,2.158288],[1.218637,1.580868],[-2.140800,-3.389848],[-4.050708,-7.062663],[9.341340,-2.369875],[-2.013887,8.189737]],[[-1.575251,-5.421554],[9.300498,4.402143],[-6.956415,-8.777517],[-6.751622,-1.440862],[0.177570,-3.357841],[2.259578,-3.791870],[-1.728657,-8.779556],[-5.634613,-4.715829]],[[0.377572,-4.569420],[5.020234,8.498561],[-0.431103,4.592622],[3.729664,0.221992],[-3.783775,-2.552968],[6.773658,-6.792168],[7.030013,-6.324948],[-5.758604,5.251805]],[[0.016521,9.849757],[5.872927,-3.751264],[-1.952238,-7.221183],[8.246913,-7.711268],[6.576771,0.960848],[-1.935009,8.894243],[-0.652497,9.268937],[-5.036469,1.517701]],[[7.064475,-3.139491],[2.082398,-7.959123],[-4.836853,-1.669884],[0.057682,9.332221],[5.065869,3.241442],[6.334263,-0.629878],[-0.156240,-0.218845],[-0.083964,-7.406248]],[[-6.137794,-0.372466],[2.428876,-5.732465],[4.715363,5.718328],[4.016750,2.991856],[4.521949,-3.871944],[4.193883,0.540705],[3.186865,-2.512773],[7.085010,9.025786]],[[2.948489,4.310717],[-6.352628,-2.551972],[-3.881102,-0.726232],[4.396686,8.665076],[-0.916167,7.037474],[-6.662108,2.910748],[-5.150151,2.349398],[-5.517572,-0.765468]],[[-2.415772,-0.100499],[6.002897,-2.145423],[-8.845170,2.795730],[-0.606967,3.815011],[2.381005,4.997373],[0.686460,8.652199],[-6.101327,1.011273],[7.496629,5.033264]],[[9.039079,-7.840365],[-9.547366,9.181408],[-8.798009,-5.970100],[8.379443,7.150040],[-2.424375,-5.252934],[-5.976703,-1.677930],[-9.778081,2.847294],[9.237124,6.551540]],[[2.982301,2.968845],[-0.802137,-8.077481],[2.200329,5.693982],[-4.643170,5.394802],[9.628220,-2.374865],[5.043042,2.782207],[-5.307588,7.499393],[1.329380,0.843083]],[[4.017268,-2.753676],[3.148237,-3.042377],[-8.762959,4.253458],[-1.437598,6.498401],[-9.803609,7.722516],[-1.017851,9.249550],[-3.286899,-0.926605],[5.706570,-7.164234]],[[-5.790476,-9.544304],[4.834294,0.017671],[-9.321043,7.395113],[6.386018,8.061600],[-1.955639,-7.909128],[3.417548,-5.804549],[-9.270760,5.853723],[-6.343155,-0.735632]]], dtype = "float64")#candidate|285|(16, 8, 2)|const|float64
uop_286 = relay.asinh(const_285.astype('float64')) # shape=(16, 8, 2)
uop_288 = relay.rsqrt(const_285.astype('float64')) # shape=(16, 8, 2)
bop_296 = relay.power(uop_286.astype('float32'), relay.reshape(const_285.astype('float32'), relay.shape_of(uop_286))) # shape=(16, 8, 2)
bop_299 = relay.less(bop_296.astype('bool'), relay.reshape(uop_288.astype('bool'), relay.shape_of(bop_296))) # shape=(16, 8, 2)
output = bop_299
output2 = bop_299
func_316 = relay.Function([], output)
mod['func_316'] = func_316
mod = relay.transform.InferType()(mod)
output = func_316()
func_317 = relay.Function([], output)
mutated_mod['func_317'] = func_317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_339 = func_316_call()
call_340 = func_316_call()
func_140_call = mod.get_global_var('func_140')
func_142_call = mutated_mod.get_global_var('func_142')
var_345 = relay.var("var_345", dtype = "float32", shape = (3, 135))#candidate|345|(3, 135)|var|float32
call_344 = relay.TupleGetItem(func_140_call(relay.reshape(var_345.astype('float32'), [15, 9, 3])), 1)
call_346 = relay.TupleGetItem(func_142_call(relay.reshape(var_345.astype('float32'), [15, 9, 3])), 1)
output = relay.Tuple([call_339,call_344,var_345,])
output2 = relay.Tuple([call_340,call_346,var_345,])
func_347 = relay.Function([var_345,], output)
mod['func_347'] = func_347
mod = relay.transform.InferType()(mod)
mutated_mod['func_347'] = func_347
mutated_mod = relay.transform.InferType()(mutated_mod)
var_348 = relay.var("var_348", dtype = "float32", shape = (3, 135))#candidate|348|(3, 135)|var|float32
func_347_call = mutated_mod.get_global_var('func_347')
call_349 = func_347_call(var_348)
output = call_349
func_350 = relay.Function([var_348], output)
mutated_mod['func_350'] = func_350
mutated_mod = relay.transform.InferType()(mutated_mod)
var_363 = relay.var("var_363", dtype = "float64", shape = (11, 1, 7))#candidate|363|(11, 1, 7)|var|float64
const_364 = relay.const([[[-5.789306,8.361320,1.201529,-3.652794,-0.732084,1.025064,7.305648],[-1.168366,5.774584,-7.892434,6.256758,-5.161095,2.780887,-3.577277]],[[3.807644,9.065682,-6.553389,9.868712,5.701023,4.675803,-1.552701],[-4.230883,-5.502694,7.499948,6.395557,5.034844,6.242072,-7.004448]],[[-0.893115,-9.022728,-2.416733,-6.148492,7.142081,-4.766506,2.171037],[-5.336798,-2.263508,-4.043228,8.347274,3.339530,5.289803,2.019902]],[[-5.020400,0.462242,-8.764026,-5.354178,4.181094,-1.535640,-5.215338],[7.921983,-5.546153,-8.140136,-4.906741,6.517503,-8.777706,1.985518]],[[9.388090,-4.144273,-2.204012,3.752845,1.745022,0.823070,-4.397308],[6.351426,5.889695,-3.276923,-7.707748,-9.272279,3.684350,2.445478]],[[-6.247547,2.964238,6.672660,-0.154136,7.727308,8.419201,6.346067],[5.312692,-5.699177,7.387830,-7.566206,1.569753,-3.257944,6.864950]],[[3.856241,5.451328,5.947747,-8.763430,-4.919307,-1.444408,-2.616863],[-0.208423,0.248305,1.199373,6.890209,9.128131,-3.047797,-6.340275]],[[-1.131420,0.065226,-5.150480,-2.651214,1.305736,7.987615,4.284089],[-7.619172,5.994654,1.273548,-8.200706,-4.912267,1.925031,7.319311]],[[-9.781038,-1.683916,-7.692434,-0.982190,-8.965008,-4.624623,7.853823],[1.658702,-7.559371,-0.668395,4.955007,-0.709374,-3.234285,3.708257]],[[-4.763411,-7.148109,-5.746515,5.119790,-2.535785,-0.721729,-8.560084],[-0.897597,-3.566689,-5.949339,7.993737,-7.002133,2.751295,5.622101]],[[0.938137,5.986261,2.634434,-5.452306,9.819640,-5.256142,0.059794],[-3.306974,-2.797438,-3.126973,7.280377,8.992051,9.004344,6.198182]]], dtype = "float64")#candidate|364|(11, 2, 7)|const|float64
bop_365 = relay.divide(var_363.astype('float64'), const_364.astype('float64')) # shape=(11, 2, 7)
output = relay.Tuple([bop_365,])
output2 = relay.Tuple([bop_365,])
func_377 = relay.Function([var_363,], output)
mod['func_377'] = func_377
mod = relay.transform.InferType()(mod)
mutated_mod['func_377'] = func_377
mutated_mod = relay.transform.InferType()(mutated_mod)
var_378 = relay.var("var_378", dtype = "float64", shape = (11, 1, 7))#candidate|378|(11, 1, 7)|var|float64
func_377_call = mutated_mod.get_global_var('func_377')
call_379 = func_377_call(var_378)
output = call_379
func_380 = relay.Function([var_378], output)
mutated_mod['func_380'] = func_380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_416 = func_316_call()
call_417 = func_316_call()
var_428 = relay.var("var_428", dtype = "bool", shape = (16, 8, 2))#candidate|428|(16, 8, 2)|var|bool
bop_429 = relay.bitwise_or(call_416.astype('uint32'), relay.reshape(var_428.astype('uint32'), relay.shape_of(call_416))) # shape=(16, 8, 2)
bop_432 = relay.bitwise_or(call_417.astype('uint32'), relay.reshape(var_428.astype('uint32'), relay.shape_of(call_417))) # shape=(16, 8, 2)
func_140_call = mod.get_global_var('func_140')
func_142_call = mutated_mod.get_global_var('func_142')
var_446 = relay.var("var_446", dtype = "float32", shape = (405, 1))#candidate|446|(405, 1)|var|float32
call_445 = relay.TupleGetItem(func_140_call(relay.reshape(var_446.astype('float32'), [15, 9, 3])), 1)
call_447 = relay.TupleGetItem(func_142_call(relay.reshape(var_446.astype('float32'), [15, 9, 3])), 1)
uop_463 = relay.erf(var_428.astype('float32')) # shape=(16, 8, 2)
func_140_call = mod.get_global_var('func_140')
func_142_call = mutated_mod.get_global_var('func_142')
call_468 = relay.TupleGetItem(func_140_call(relay.reshape(call_445.astype('float32'), [15, 9, 3])), 0)
call_469 = relay.TupleGetItem(func_142_call(relay.reshape(call_445.astype('float32'), [15, 9, 3])), 0)
output = relay.Tuple([bop_429,call_445,var_446,uop_463,call_468,])
output2 = relay.Tuple([bop_432,call_447,var_446,uop_463,call_469,])
func_471 = relay.Function([var_428,var_446,], output)
mod['func_471'] = func_471
mod = relay.transform.InferType()(mod)
mutated_mod['func_471'] = func_471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_471_call = mutated_mod.get_global_var('func_471')
var_473 = relay.var("var_473", dtype = "bool", shape = (16, 8, 2))#candidate|473|(16, 8, 2)|var|bool
var_474 = relay.var("var_474", dtype = "float32", shape = (405, 1))#candidate|474|(405, 1)|var|float32
call_472 = func_471_call(var_473,var_474,)
output = call_472
func_475 = relay.Function([var_473,var_474,], output)
mutated_mod['func_475'] = func_475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_543 = func_316_call()
call_544 = func_316_call()
func_347_call = mod.get_global_var('func_347')
func_350_call = mutated_mod.get_global_var('func_350')
var_550 = relay.var("var_550", dtype = "float32", shape = (405,))#candidate|550|(405,)|var|float32
call_549 = relay.TupleGetItem(func_347_call(relay.reshape(var_550.astype('float32'), [3, 135])), 1)
call_551 = relay.TupleGetItem(func_350_call(relay.reshape(var_550.astype('float32'), [3, 135])), 1)
output = relay.Tuple([call_543,call_549,var_550,])
output2 = relay.Tuple([call_544,call_551,var_550,])
func_555 = relay.Function([var_550,], output)
mod['func_555'] = func_555
mod = relay.transform.InferType()(mod)
mutated_mod['func_555'] = func_555
mutated_mod = relay.transform.InferType()(mutated_mod)
var_556 = relay.var("var_556", dtype = "float32", shape = (405,))#candidate|556|(405,)|var|float32
func_555_call = mutated_mod.get_global_var('func_555')
call_557 = func_555_call(var_556)
output = call_557
func_558 = relay.Function([var_556], output)
mutated_mod['func_558'] = func_558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_562 = func_316_call()
call_563 = func_316_call()
output = relay.Tuple([call_562,])
output2 = relay.Tuple([call_563,])
func_569 = relay.Function([], output)
mod['func_569'] = func_569
mod = relay.transform.InferType()(mod)
mutated_mod['func_569'] = func_569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_569_call = mutated_mod.get_global_var('func_569')
call_570 = func_569_call()
output = call_570
func_571 = relay.Function([], output)
mutated_mod['func_571'] = func_571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_569_call = mod.get_global_var('func_569')
func_571_call = mutated_mod.get_global_var('func_571')
call_577 = relay.TupleGetItem(func_569_call(), 0)
call_578 = relay.TupleGetItem(func_571_call(), 0)
output = relay.Tuple([call_577,])
output2 = relay.Tuple([call_578,])
func_586 = relay.Function([], output)
mod['func_586'] = func_586
mod = relay.transform.InferType()(mod)
mutated_mod['func_586'] = func_586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mutated_mod.get_global_var('func_586')
call_587 = func_586_call()
output = call_587
func_588 = relay.Function([], output)
mutated_mod['func_588'] = func_588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_569_call = mod.get_global_var('func_569')
func_571_call = mutated_mod.get_global_var('func_571')
call_661 = relay.TupleGetItem(func_569_call(), 0)
call_662 = relay.TupleGetItem(func_571_call(), 0)
output = call_661
output2 = call_662
func_666 = relay.Function([], output)
mod['func_666'] = func_666
mod = relay.transform.InferType()(mod)
output = func_666()
func_667 = relay.Function([], output)
mutated_mod['func_667'] = func_667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_666_call = mod.get_global_var('func_666')
func_667_call = mutated_mod.get_global_var('func_667')
call_723 = func_666_call()
call_724 = func_666_call()
var_756 = relay.var("var_756", dtype = "bool", shape = (16, 8, 2))#candidate|756|(16, 8, 2)|var|bool
bop_757 = relay.right_shift(call_723.astype('int64'), relay.reshape(var_756.astype('int64'), relay.shape_of(call_723))) # shape=(16, 8, 2)
bop_760 = relay.right_shift(call_724.astype('int64'), relay.reshape(var_756.astype('int64'), relay.shape_of(call_724))) # shape=(16, 8, 2)
uop_762 = relay.exp(var_756.astype('float64')) # shape=(16, 8, 2)
output = relay.Tuple([bop_757,uop_762,])
output2 = relay.Tuple([bop_760,uop_762,])
func_764 = relay.Function([var_756,], output)
mod['func_764'] = func_764
mod = relay.transform.InferType()(mod)
mutated_mod['func_764'] = func_764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_765 = relay.var("var_765", dtype = "bool", shape = (16, 8, 2))#candidate|765|(16, 8, 2)|var|bool
func_764_call = mutated_mod.get_global_var('func_764')
call_766 = func_764_call(var_765)
output = call_766
func_767 = relay.Function([var_765], output)
mutated_mod['func_767'] = func_767
mutated_mod = relay.transform.InferType()(mutated_mod)
var_881 = relay.var("var_881", dtype = "uint8", shape = (9, 8, 2))#candidate|881|(9, 8, 2)|var|uint8
const_882 = relay.const([[[6,-9],[4,9],[-8,-8],[-5,7],[7,-8],[10,5],[3,-9],[-10,-2]],[[10,9],[5,-3],[-8,-7],[-7,-9],[-10,7],[7,1],[-5,6],[1,-2]],[[-9,7],[6,-8],[1,9],[4,2],[-7,5],[1,5],[-8,-1],[-8,2]],[[-1,3],[6,-6],[-1,-5],[-5,8],[-6,-5],[10,-2],[10,7],[-4,5]],[[-7,7],[-2,-2],[-7,7],[-6,5],[9,-10],[9,-7],[-5,7],[3,-7]],[[2,6],[6,-8],[-9,-9],[9,10],[4,-7],[1,-4],[-8,8],[-4,-4]],[[10,2],[-1,10],[-5,-6],[3,-2],[-5,-1],[-1,-5],[-7,2],[9,-8]],[[7,-6],[10,8],[-7,10],[10,8],[-1,4],[-6,-2],[-1,4],[10,10]],[[4,8],[3,9],[-2,-3],[-1,2],[2,7],[-4,-2],[-3,6],[10,3]]], dtype = "uint8")#candidate|882|(9, 8, 2)|const|uint8
bop_883 = relay.right_shift(var_881.astype('uint8'), relay.reshape(const_882.astype('uint8'), relay.shape_of(var_881))) # shape=(9, 8, 2)
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
const_892 = relay.const([True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True], dtype = "bool")#candidate|892|(256,)|const|bool
call_891 = relay.TupleGetItem(func_764_call(relay.reshape(const_892.astype('bool'), [16, 8, 2])), 0)
call_893 = relay.TupleGetItem(func_767_call(relay.reshape(const_892.astype('bool'), [16, 8, 2])), 0)
func_666_call = mod.get_global_var('func_666')
func_667_call = mutated_mod.get_global_var('func_667')
call_895 = func_666_call()
call_896 = func_666_call()
output = relay.Tuple([bop_883,call_891,const_892,call_895,])
output2 = relay.Tuple([bop_883,call_893,const_892,call_896,])
func_897 = relay.Function([var_881,], output)
mod['func_897'] = func_897
mod = relay.transform.InferType()(mod)
mutated_mod['func_897'] = func_897
mutated_mod = relay.transform.InferType()(mutated_mod)
var_898 = relay.var("var_898", dtype = "uint8", shape = (9, 8, 2))#candidate|898|(9, 8, 2)|var|uint8
func_897_call = mutated_mod.get_global_var('func_897')
call_899 = func_897_call(var_898)
output = call_899
func_900 = relay.Function([var_898], output)
mutated_mod['func_900'] = func_900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_666_call = mod.get_global_var('func_666')
func_667_call = mutated_mod.get_global_var('func_667')
call_913 = func_666_call()
call_914 = func_666_call()
output = call_913
output2 = call_914
func_922 = relay.Function([], output)
mod['func_922'] = func_922
mod = relay.transform.InferType()(mod)
output = func_922()
func_923 = relay.Function([], output)
mutated_mod['func_923'] = func_923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1010 = relay.var("var_1010", dtype = "bool", shape = ())#candidate|1010|()|var|bool
var_1011 = relay.var("var_1011", dtype = "bool", shape = (12, 1))#candidate|1011|(12, 1)|var|bool
bop_1012 = relay.logical_or(var_1010.astype('bool'), var_1011.astype('bool')) # shape=(12, 1)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1046 = relay.TupleGetItem(func_586_call(), 0)
call_1047 = relay.TupleGetItem(func_588_call(), 0)
func_569_call = mod.get_global_var('func_569')
func_571_call = mutated_mod.get_global_var('func_571')
call_1049 = relay.TupleGetItem(func_569_call(), 0)
call_1050 = relay.TupleGetItem(func_571_call(), 0)
func_922_call = mod.get_global_var('func_922')
func_923_call = mutated_mod.get_global_var('func_923')
call_1052 = func_922_call()
call_1053 = func_922_call()
func_569_call = mod.get_global_var('func_569')
func_571_call = mutated_mod.get_global_var('func_571')
call_1065 = relay.TupleGetItem(func_569_call(), 0)
call_1066 = relay.TupleGetItem(func_571_call(), 0)
uop_1078 = relay.acos(call_1052.astype('float32')) # shape=(16, 8, 2)
uop_1080 = relay.acos(call_1053.astype('float32')) # shape=(16, 8, 2)
uop_1087 = relay.acosh(uop_1078.astype('float64')) # shape=(16, 8, 2)
uop_1089 = relay.acosh(uop_1080.astype('float64')) # shape=(16, 8, 2)
func_377_call = mod.get_global_var('func_377')
func_380_call = mutated_mod.get_global_var('func_380')
const_1105 = relay.const([[8.603267,9.573446,-9.950957,4.464293,9.705746,5.571376,-2.177449,-0.648302,-4.870755,-4.339056,-3.539657,-4.680751,0.541996,1.644633,9.290048,-0.145890,0.056699,7.030785,-8.153503,3.479414,-2.072926,0.726550,9.528352,1.733981,-7.415624,8.364962,-2.670074,7.886723,3.057383,5.689222,-0.967395,0.600619,-8.760813,-4.996107,1.176076,-5.521378,-3.228398,-2.716494,-1.274369,-7.050497,-0.825390,1.921331,3.907873,-7.366080,5.080655,-6.990724,4.138903,6.323494,-8.477218,-3.689946,5.308262,5.850533,5.437675,1.361770,7.546054,-9.783897,3.937263,-1.344152,1.772283,2.341196,-8.006340,-7.960593,0.750104,7.361864,7.046105,-2.011948,0.670368,3.526930,4.280380,-3.891570,-1.854683,-8.047372,-0.298686,-8.575909,7.476849,-0.168369,5.672486]], dtype = "float64")#candidate|1105|(1, 77)|const|float64
call_1104 = relay.TupleGetItem(func_377_call(relay.reshape(const_1105.astype('float64'), [11, 1, 7])), 0)
call_1106 = relay.TupleGetItem(func_380_call(relay.reshape(const_1105.astype('float64'), [11, 1, 7])), 0)
output = relay.Tuple([bop_1012,call_1046,call_1049,call_1065,uop_1087,call_1104,const_1105,])
output2 = relay.Tuple([bop_1012,call_1047,call_1050,call_1066,uop_1089,call_1106,const_1105,])
func_1110 = relay.Function([var_1010,var_1011,], output)
mod['func_1110'] = func_1110
mod = relay.transform.InferType()(mod)
mutated_mod['func_1110'] = func_1110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1110_call = mutated_mod.get_global_var('func_1110')
var_1112 = relay.var("var_1112", dtype = "bool", shape = ())#candidate|1112|()|var|bool
var_1113 = relay.var("var_1113", dtype = "bool", shape = (12, 1))#candidate|1113|(12, 1)|var|bool
call_1111 = func_1110_call(var_1112,var_1113,)
output = call_1111
func_1114 = relay.Function([var_1112,var_1113,], output)
mutated_mod['func_1114'] = func_1114
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1184 = relay.const([[[-3,9,9,-9,-7,8,-8,-10,10],[-4,-8,-6,8,5,-4,-9,9,6],[-9,-6,-1,2,-5,-10,8,5,-4],[10,8,9,-4,-9,-8,3,-8,-4],[5,10,10,5,4,3,1,-10,-9],[-3,9,5,6,7,-1,7,-8,-6],[-9,-8,2,-10,5,4,-1,6,-10],[7,3,2,-4,-9,-7,3,-5,8],[-2,-10,10,-10,2,1,1,8,4],[7,10,-2,-1,1,-4,5,7,3],[-1,8,-1,3,-9,-5,10,10,-7],[7,7,-6,-8,9,6,5,-6,-1]],[[2,-10,-5,-3,-8,5,7,-3,-1],[-7,10,4,-9,5,2,4,-8,-6],[-1,7,3,-5,5,5,9,-3,-10],[-8,6,6,-7,-3,-9,9,-1,9],[2,4,-4,-1,5,-3,-3,-5,2],[10,-6,-8,3,4,8,7,5,-5],[-4,-1,4,-3,-5,-7,-2,8,-1],[2,6,7,-7,-3,-8,3,-7,-1],[10,-8,-4,10,4,-5,-6,9,5],[7,-2,6,9,4,-6,6,10,-1],[-1,-2,10,-9,6,-2,4,3,-8],[-8,10,2,6,4,-2,-10,-7,-7]],[[10,5,2,7,5,-3,-8,-1,-2],[8,8,4,6,-2,-6,10,-3,-4],[-2,-4,-10,1,8,10,-4,-8,10],[-2,-5,9,-3,9,-6,2,3,-7],[3,-3,-2,8,9,8,-7,-8,-7],[4,-8,6,6,-1,6,-2,-8,7],[-9,-5,1,10,8,-10,4,4,7],[-5,-2,1,-6,4,-1,-3,-5,9],[-6,6,4,8,8,-10,-4,9,3],[3,-5,5,-7,4,-1,-10,9,-8],[1,-3,-9,-5,9,-10,-4,-4,-9],[4,-1,10,3,-6,7,7,1,-9]],[[4,5,10,8,6,6,4,3,-10],[7,2,-6,-9,-9,7,-3,3,-4],[1,10,5,5,6,5,1,-1,-7],[-4,-2,-9,2,-9,7,-10,7,-6],[-6,4,-10,-9,-2,4,7,-6,-2],[7,-4,-8,2,-9,-10,1,-7,7],[5,8,4,7,-1,-10,7,-6,-6],[3,-4,6,7,-7,4,4,10,9],[8,-7,10,-4,9,-7,4,-4,2],[2,9,6,5,-7,5,-3,3,-2],[1,9,5,4,5,10,10,-9,-3],[-4,-6,-7,6,-4,10,-9,1,1]],[[-3,-7,-5,-8,-1,3,3,-4,6],[-1,-1,-1,-10,-4,-10,9,1,4],[3,10,2,-7,1,-5,3,1,-3],[-7,-5,-6,-5,8,10,-2,5,-6],[5,1,7,3,4,-5,6,-9,-2],[-6,1,3,-6,-4,-6,8,-6,-5],[5,-4,-2,3,1,-9,-1,2,-8],[3,1,-5,-2,8,1,10,5,-2],[-2,-5,9,8,10,1,-6,-4,-6],[5,3,5,-9,8,10,1,7,7],[-3,-5,6,2,2,10,-6,-5,8],[-3,-4,3,2,-6,-1,4,-9,-6]],[[7,-8,6,7,2,-3,2,1,6],[10,7,7,-8,-1,-10,-3,-7,-7],[10,6,-8,6,2,5,-1,-8,-10],[6,7,-6,-6,-5,-1,-5,8,5],[-8,-5,-8,10,5,8,4,3,1],[10,8,10,8,2,-7,-2,-10,7],[7,-7,-9,8,-1,7,-10,-9,2],[10,7,6,9,-10,4,6,9,4],[10,-1,10,-3,5,-9,-5,7,-10],[-7,10,7,7,5,-9,-3,-8,-2],[-4,-1,8,6,-8,5,-5,-7,2],[-10,9,4,-4,-1,-5,5,9,-10]],[[5,-10,6,-2,-10,7,5,10,5],[-4,-4,5,7,1,-5,2,-5,-4],[-2,6,-5,5,-2,-6,10,10,-8],[-3,5,10,5,8,8,2,8,3],[3,-7,-2,2,4,4,-6,-6,3],[9,-2,9,-10,-2,-9,4,-3,-6],[4,7,-1,2,1,8,-8,1,5],[1,-1,6,8,-3,-10,7,9,6],[6,7,7,-1,-4,4,2,-7,-8],[6,-2,8,8,-8,1,8,3,3],[3,-5,-8,-6,-6,-5,5,-4,-10],[9,-10,-6,-4,-8,-10,-6,-7,-7]],[[2,5,-6,6,-2,8,-5,-2,7],[-5,2,7,6,-4,4,8,-7,-8],[3,-6,-4,-9,-3,-3,-10,-1,-2],[8,-10,3,-6,-4,3,-9,5,3],[2,-6,6,-7,-8,1,-5,-9,1],[-2,2,3,-7,-4,-10,10,1,-6],[7,-3,2,-8,5,5,-9,7,3],[7,-4,10,9,5,10,-9,7,-4],[8,-7,9,-10,-8,-10,-7,-1,-9],[5,5,-8,-3,1,-8,8,-9,10],[-4,-6,7,5,2,-3,9,9,-7],[-6,-5,-10,-6,-1,-3,2,-1,-2]],[[-4,-2,-3,9,2,3,-6,-2,7],[-6,-10,7,7,-1,-8,9,-9,2],[6,1,1,9,-4,10,5,-4,10],[8,-1,-10,-1,-10,-7,-2,4,-3],[7,4,-5,3,-8,-4,-8,-10,3],[-7,8,-5,-2,10,-10,2,-6,-1],[1,-10,-2,-9,-1,9,-10,8,-6],[5,-2,5,-9,-1,3,6,7,5],[4,-10,-5,-7,-7,-3,10,2,-2],[-5,-4,-5,-10,5,9,-7,-3,6],[-9,-5,9,-1,5,-2,2,9,4],[5,7,3,9,8,8,2,-8,4]],[[-4,-8,-10,-7,6,10,-1,3,-6],[-3,6,-7,-5,2,7,-1,-2,-9],[9,-5,-1,4,10,10,-6,1,2],[8,8,-3,5,5,2,10,-9,6],[-9,-3,-10,7,6,9,5,-7,5],[-7,3,10,7,9,-6,-5,7,-8],[-1,-4,2,-4,1,1,1,-8,1],[10,-9,-3,5,-4,7,1,6,4],[-9,4,-2,-5,4,-5,-5,-2,-5],[-1,-2,-3,6,7,-9,7,-9,-7],[-9,-4,-8,-7,-6,-9,-5,-3,5],[8,-8,-1,-7,-7,3,-7,-8,5]],[[-2,1,3,-10,10,7,-9,-7,1],[-6,-8,5,8,-6,-5,-4,-3,-6],[5,-7,9,-10,-9,7,-5,-8,-7],[8,5,4,3,6,5,4,-7,-6],[-5,7,5,5,9,5,-6,-3,-5],[8,7,5,5,-3,-10,-9,7,-2],[1,2,-3,-10,-2,-8,2,-6,-2],[-10,-2,-9,3,-1,5,-3,-1,10],[4,2,5,-4,6,7,-4,-4,1],[1,1,-4,-5,5,-2,1,7,3],[-3,-10,-10,6,-5,10,-2,-1,5],[1,2,8,-1,1,2,9,-2,4]],[[-3,6,3,-5,7,9,-1,1,-4],[-9,-10,2,-6,-9,7,2,6,-9],[6,-3,10,-6,-2,-6,8,3,8],[9,-6,4,-4,5,-6,10,-10,6],[6,-3,-9,-7,4,4,-5,6,3],[-7,8,-8,10,-8,-2,-2,-8,-7],[4,5,-3,-2,4,-4,-9,8,4],[-4,6,5,-10,-4,-2,5,-4,5],[-9,-10,4,2,4,1,-5,-4,-10],[-7,-6,9,4,5,4,7,-5,-8],[8,2,-9,-2,9,3,5,-2,-3],[-10,-6,-6,2,-6,10,-8,4,-10]],[[5,5,-8,-5,-2,-5,-9,3,9],[-6,1,-10,3,-9,7,8,-3,-8],[-5,5,10,-2,4,-4,3,4,9],[-6,1,1,-7,10,4,-3,10,4],[-10,1,-10,-7,-3,8,6,-6,1],[4,6,8,-3,9,-8,5,9,-2],[-1,3,-3,-7,7,5,-1,-6,5],[7,4,1,-8,10,4,-6,4,-2],[4,-5,5,9,-8,-4,-8,1,6],[-3,-2,-2,8,5,1,10,-7,6],[-4,-9,-9,-7,4,8,4,8,6],[-4,10,-6,-7,6,-1,7,7,-2]],[[-10,3,1,-8,3,-2,-6,3,8],[-6,-6,-10,-5,4,6,10,5,10],[7,10,1,-10,8,2,-3,-10,1],[5,8,1,7,10,7,9,-7,5],[-1,-7,-6,-5,-7,7,-7,-7,-4],[-9,-10,-5,8,-10,-3,4,-9,2],[-10,-4,2,-5,6,3,10,4,-2],[6,1,6,-2,7,-1,-7,-6,8],[-6,8,-6,-3,5,-6,-6,-9,-10],[-10,-5,-2,-6,9,-3,1,-9,1],[-9,2,4,3,2,-7,-6,5,-6],[2,-7,3,6,-7,-2,-10,3,-5]]], dtype = "uint32")#candidate|1184|(14, 12, 9)|const|uint32
var_1185 = relay.var("var_1185", dtype = "uint32", shape = (14, 12, 9))#candidate|1185|(14, 12, 9)|var|uint32
bop_1186 = relay.bitwise_or(const_1184.astype('uint32'), relay.reshape(var_1185.astype('uint32'), relay.shape_of(const_1184))) # shape=(14, 12, 9)
uop_1202 = relay.tan(var_1185.astype('float32')) # shape=(14, 12, 9)
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
const_1205 = relay.const([[-7.709673,-3.304544,-9.000480,5.737445,-4.623538,-8.903153,-4.453387,8.749892,-7.341505,-9.185554,3.252963,-2.529846,-3.246227,-2.493625,7.998584,-1.811383,6.799617,-6.258667,6.209752,-7.392782,9.941386,0.874961,1.925528,-3.636069,3.301124,-1.452160,-2.968500,-5.289424,-1.640050,4.832320,-4.370523,4.740035,-1.948569,6.035617,-0.846005,1.299764,-7.015764,7.056855,9.276124,5.058889,-5.363260,-0.057524,-8.239297,-9.324467,6.390863,4.138143,5.128672,9.604916,-8.540884,8.554207,-6.030874,-8.621710,5.471255,-2.234929,7.681499,3.756776,0.822646,-6.197213,-9.740488,-6.827710,-4.305181,8.191857,1.720596,-0.819962,-1.957120,-6.612259,-1.573610,5.796548,-9.600611,5.541485,-3.797856,9.929148,-6.850059,9.961935,-0.981191,-7.837168,5.504286,-3.488122,-2.513684,5.969402,9.584534,5.405487,-5.896675,6.521860,2.569655,1.801222,-4.296702,9.224142,-7.229066,9.823693,4.752297,-4.757353,-9.152219,2.571991,2.699914,5.746546,-0.266332,-5.409407,7.741556,3.458792,-4.062408,-5.219161,4.386646,0.766807,1.922613,4.567278,-3.412727,0.056485,-5.885440,5.551843,8.744734,-7.310302,-8.845246,7.012849,6.265462,-0.556524,4.893412,-3.432450,-9.047718,-7.894052,-2.763165,-9.686984,7.249145,5.882457,-0.702692,6.443707,4.539712,7.000768,1.067650,-7.835220,3.406885,-8.819860,6.135198,-1.829407,0.229146,9.487912,-7.296967,-3.339507,-7.425196,0.690905,1.506581,-4.973931,7.579851,-2.495639,-9.639730,0.562697,4.427986,-1.232327,-1.144489,-7.783374,-7.526485,3.397447,-9.999734,-4.974941,-6.025139,4.391070,2.152541,-7.457233,-1.531965,5.317805,2.622273,-6.088836,-5.655626,-6.409996,2.811333,-6.758923,-9.175914,-1.584270,-9.850351,4.359703,7.780335,-6.358947,5.161992,2.479883,8.916753,-8.000731,6.228843,6.151847,-8.025330,-9.620730,-4.818811,7.303948,-6.003913,5.768227,-3.801021,1.735695,-3.013183,-8.064032,8.936092,3.288736,-8.871031,6.029431,-7.866490,-5.836179,-0.075777,2.880424,7.951763,-9.260018,-1.453558,-5.663784,-2.552242,-0.733094,6.794182,-3.619459,-1.760924,1.387019,-4.374827,-8.930187,3.590546,2.864516,6.502206,6.436147,7.338682,2.659720,0.456774,-0.926830,1.277277,-1.540640,-5.078198,7.174459,-2.314616,5.590173,-4.567008,-1.669088,-2.052024,7.459967,-0.958208,0.220871,-6.763188,7.267572,-1.428975,-1.106563,9.146274,1.303166,7.012340,-9.666193,9.494236,-2.170269,-6.449175,-3.164548,-4.048082,-9.185943,-3.016752,-3.315737,-2.260767,-3.151549,-6.902096,2.472149,-0.920712,6.987531,0.909815,8.795210,6.952943,-0.771343,-0.960359,4.350259,5.449308,6.696229,7.661437,-8.280701,-9.958699,-1.043381,8.909815,-0.939267,-5.465436,-8.845948,6.505300,8.946876,7.391597,-8.131242,-6.330214,6.731486,-6.976700,1.292378,-9.884324,5.325120,-5.737423,5.116260,5.815398,1.343088,2.842557,-8.686246,-2.486664,-6.075016,1.704264,9.030912,-7.233166,7.134008,-5.961672,-0.972797,3.553083,9.603714,0.585835,8.339752,-2.941857,5.128877,-4.269734,-3.039534,3.628594,0.150808,-8.635399,-4.064933,6.496002,8.328266,-9.435886,-5.018174,3.225816,5.092926,4.346576,-0.422442,-0.125765,0.302966,9.404442,5.270282,-0.468166,0.586348,6.600545,5.145815,-5.602838,-0.662497,-6.621204,-6.525191,-3.560406,6.319632,-0.768402,9.361490,3.225044,-0.603679,0.089599,4.604328,-8.561586,-3.383718,-9.457313,-3.876183,-9.032384,4.900826,9.166390,-9.450787,9.727447,2.205777,1.396780,-6.599761,-1.854599,3.051402,-1.325141,5.811677,-9.855868,1.656854,-5.822336,6.589038,-5.820228,7.586546,-0.845635,-1.402835,7.758542,3.048079,-8.478768,7.218301,-2.930435,-3.898174,2.796390,4.779384,7.203813,-0.549546,-7.104120,-2.684134,-1.770056,7.905345,-8.299374,0.146418,4.560628,-5.714304,-6.464917,-6.741215,6.699187,-0.971640,6.006823,-6.181051,-1.071900,-3.683984,-4.513067,6.654385,-5.789427,2.291181,-1.172935,3.235680,0.052981,-3.501519,9.937893,8.590382,0.413995,-8.922753,1.422073,-3.448650,4.541423,6.306840,8.531362,6.508630,5.229975,-3.959567,2.566093,4.327180,-6.099346,-8.618716,4.970046]], dtype = "float32")#candidate|1205|(1, 405)|const|float32
call_1204 = relay.TupleGetItem(func_555_call(relay.reshape(const_1205.astype('float32'), [405,])), 1)
call_1206 = relay.TupleGetItem(func_558_call(relay.reshape(const_1205.astype('float32'), [405,])), 1)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1216 = relay.TupleGetItem(func_586_call(), 0)
call_1217 = relay.TupleGetItem(func_588_call(), 0)
output = relay.Tuple([bop_1186,uop_1202,call_1204,const_1205,call_1216,])
output2 = relay.Tuple([bop_1186,uop_1202,call_1206,const_1205,call_1217,])
func_1219 = relay.Function([var_1185,], output)
mod['func_1219'] = func_1219
mod = relay.transform.InferType()(mod)
var_1220 = relay.var("var_1220", dtype = "uint32", shape = (14, 12, 9))#candidate|1220|(14, 12, 9)|var|uint32
output = func_1219(var_1220)
func_1221 = relay.Function([var_1220], output)
mutated_mod['func_1221'] = func_1221
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1305 = relay.const([[[3.556025,2.609826],[-1.567350,-0.772484],[-1.939716,6.236963],[-3.391401,-8.003389],[-7.728090,-6.095741],[0.119450,-2.876767],[2.899826,-2.784299],[-7.100622,-5.606895],[5.438229,-3.415819],[-6.318119,-3.111579]],[[-2.100032,3.197269],[-2.597545,6.676867],[9.433314,3.580733],[-7.277551,7.190611],[-5.274913,5.423524],[9.858324,-6.334735],[2.350636,-9.185376],[-0.903072,-8.381207],[5.341519,7.505439],[4.622666,-6.118661]],[[-0.120376,6.281434],[2.149352,-1.927931],[-7.288886,4.943397],[4.160665,-6.568345],[-1.473291,7.909280],[9.322708,-3.643389],[8.500980,-9.932833],[-1.242395,7.430607],[-2.567430,3.814676],[6.171034,-9.124654]],[[8.265331,9.191577],[3.239281,9.823368],[4.316698,-5.865568],[-1.425663,9.033107],[9.728653,-0.448317],[-5.740428,-8.590871],[-0.960255,-8.147277],[-1.388885,9.512412],[-7.623901,-9.411997],[-9.484008,-3.219349]],[[-4.535339,7.174270],[1.202277,-6.549320],[-3.952901,-2.716275],[7.203985,-3.759913],[-9.052999,7.929765],[0.717677,-2.971899],[-9.913539,6.458904],[-6.889043,-9.500365],[4.802324,5.335172],[-6.644056,6.512773]],[[-2.403612,9.166482],[-8.015610,2.480172],[-9.345476,1.259226],[9.150513,-6.779657],[9.048498,-6.208299],[3.300287,-5.684558],[-8.690417,7.682080],[-9.475419,-8.106534],[-8.065856,-7.574083],[2.181745,2.892104]],[[-4.944836,1.538041],[-5.375232,0.481048],[7.826604,6.591446],[-1.482546,5.806777],[6.925288,8.337523],[7.430094,-2.360050],[7.164237,7.964219],[-7.660365,3.411028],[9.229231,-1.034972],[-7.829026,9.888322]],[[1.101369,-2.569891],[2.224555,2.008861],[-3.115782,-4.654057],[-7.319240,3.613077],[8.820990,-3.072449],[5.031221,-0.268342],[-4.193460,-0.285736],[7.490983,-1.740798],[-1.540987,-7.657961],[1.832731,-7.453685]],[[6.473921,8.965606],[6.324502,6.023028],[0.008435,-0.597577],[3.210193,-4.925762],[1.074852,-4.095185],[-2.668993,5.290871],[4.690555,-2.843122],[0.746815,-4.834903],[7.471722,-1.720615],[-2.279998,5.135632]],[[3.687200,-8.685243],[6.481018,-0.524413],[3.410315,1.424264],[-0.699334,-4.061770],[-7.203629,-5.668433],[0.876190,-3.793970],[-8.643822,6.475411],[1.544820,3.514781],[-2.885396,7.701529],[-9.395524,-8.139145]],[[1.364088,9.806069],[2.031735,4.567451],[8.504357,8.044878],[5.566660,6.152305],[2.116105,-5.988801],[-4.900406,8.411164],[-2.160880,-1.611917],[5.399379,-5.727277],[-9.656629,-2.091243],[-5.480039,8.622805]],[[6.240500,-7.775300],[5.596536,-2.837942],[5.436229,1.668199],[-2.324376,-7.465171],[5.061613,0.300390],[-3.174904,1.677723],[-4.133662,-2.753354],[-0.808361,-7.695459],[-9.938343,-0.552993],[-0.727385,-2.617686]]], dtype = "float32")#candidate|1305|(12, 10, 2)|const|float32
uop_1306 = relay.cosh(const_1305.astype('float32')) # shape=(12, 10, 2)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
const_1316 = relay.const([True,False,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False], dtype = "bool")#candidate|1316|(256,)|const|bool
var_1317 = relay.var("var_1317", dtype = "float32", shape = (405,))#candidate|1317|(405,)|var|float32
call_1315 = relay.TupleGetItem(func_471_call(relay.reshape(const_1316.astype('bool'), [16, 8, 2]), relay.reshape(var_1317.astype('float32'), [405, 1]), ), 1)
call_1318 = relay.TupleGetItem(func_475_call(relay.reshape(const_1316.astype('bool'), [16, 8, 2]), relay.reshape(var_1317.astype('float32'), [405, 1]), ), 1)
output = relay.Tuple([uop_1306,call_1315,const_1316,var_1317,])
output2 = relay.Tuple([uop_1306,call_1318,const_1316,var_1317,])
func_1321 = relay.Function([var_1317,], output)
mod['func_1321'] = func_1321
mod = relay.transform.InferType()(mod)
var_1322 = relay.var("var_1322", dtype = "float32", shape = (405,))#candidate|1322|(405,)|var|float32
output = func_1321(var_1322)
func_1323 = relay.Function([var_1322], output)
mutated_mod['func_1323'] = func_1323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1325 = relay.var("var_1325", dtype = "bool", shape = (13, 4, 11))#candidate|1325|(13, 4, 11)|var|bool
const_1326 = relay.const([[[False,False,False,True,True,False,False,True,False,True,False],[True,False,True,True,True,True,True,False,False,True,True],[True,False,False,False,False,False,True,True,False,True,True],[False,True,True,True,True,False,True,True,True,True,True]],[[False,False,False,True,True,False,True,False,False,True,False],[False,True,False,False,False,True,True,False,True,True,True],[False,False,False,False,False,True,True,True,True,False,True],[True,True,False,False,True,True,False,False,True,False,True]],[[False,True,False,True,False,False,False,True,True,False,False],[True,True,False,True,False,True,False,False,False,True,False],[False,True,True,True,True,True,True,False,False,True,True],[False,False,True,False,True,False,True,True,False,True,False]],[[False,False,True,True,False,True,True,True,True,False,True],[False,True,False,True,False,False,False,True,True,False,False],[False,True,True,True,False,False,True,True,True,False,True],[False,True,True,True,True,True,True,True,False,True,False]],[[False,True,True,True,True,False,False,True,False,True,False],[True,False,True,False,True,False,True,True,False,True,True],[True,False,False,False,True,True,False,True,True,True,False],[False,False,True,True,False,False,True,True,True,True,True]],[[False,True,True,False,False,False,False,True,True,False,True],[True,False,True,False,True,False,False,False,False,False,False],[True,True,False,True,True,False,False,False,True,False,True],[False,True,True,True,True,False,False,True,True,False,False]],[[False,False,True,False,False,True,False,True,True,True,False],[True,True,True,True,True,True,True,False,False,True,True],[True,False,False,True,True,False,True,True,False,True,True],[True,False,False,False,False,True,True,False,True,False,True]],[[True,False,False,False,True,False,True,False,True,False,True],[False,False,False,False,True,True,False,False,False,True,False],[False,True,True,True,False,True,True,False,False,False,False],[False,False,True,True,True,False,False,False,True,False,False]],[[True,False,True,False,False,True,False,True,False,True,False],[True,False,False,False,True,True,False,True,True,False,False],[True,True,True,True,False,True,False,False,True,True,True],[False,True,True,False,True,True,False,False,True,True,True]],[[False,True,False,True,True,False,False,True,False,True,True],[True,False,True,True,False,True,False,True,False,True,False],[False,True,False,True,True,False,False,False,True,False,True],[False,True,False,False,False,True,False,True,False,True,False]],[[True,False,False,True,True,False,True,False,False,True,True],[False,False,False,True,True,False,False,True,True,False,True],[True,False,True,False,False,False,True,False,False,False,False],[True,True,True,True,True,True,True,False,False,False,True]],[[False,True,False,False,True,True,True,False,False,False,False],[True,True,True,False,False,True,False,False,True,True,False],[True,False,True,False,False,True,True,False,False,True,True],[False,False,False,False,True,False,False,False,True,False,True]],[[False,False,True,True,False,True,False,False,True,True,False],[False,False,False,False,True,False,False,False,True,True,False],[False,True,False,False,True,False,True,True,True,True,True],[False,False,False,True,True,False,True,False,False,True,False]]], dtype = "bool")#candidate|1326|(13, 4, 11)|const|bool
bop_1327 = relay.logical_or(var_1325.astype('bool'), relay.reshape(const_1326.astype('bool'), relay.shape_of(var_1325))) # shape=(13, 4, 11)
func_897_call = mod.get_global_var('func_897')
func_900_call = mutated_mod.get_global_var('func_900')
const_1334 = relay.const([-6,-7,9,5,-10,6,6,-8,5,-7,4,-2,8,3,2,-10,-4,-9,5,-7,-10,4,4,2,-6,6,6,-10,-1,10,1,-2,-5,6,-6,6,3,-2,3,-8,3,-9,-6,-5,2,-8,7,7,-4,3,-5,6,2,9,-3,6,-5,-7,6,5,9,-2,-7,8,4,-1,-2,-9,6,2,6,-5,3,-1,-4,-6,2,-1,6,10,3,-9,8,-1,-7,-4,-9,4,-9,-10,1,-7,-3,-4,8,-1,7,7,-9,2,9,8,2,-9,-9,5,-4,-7,-3,-8,-6,3,8,-1,-8,2,6,5,-6,-1,5,6,-2,-6,1,7,10,1,10,4,4,5,-8,9,9,8,10,1,5,7,1,7,6,9], dtype = "uint8")#candidate|1334|(144,)|const|uint8
call_1333 = relay.TupleGetItem(func_897_call(relay.reshape(const_1334.astype('uint8'), [9, 8, 2])), 3)
call_1335 = relay.TupleGetItem(func_900_call(relay.reshape(const_1334.astype('uint8'), [9, 8, 2])), 3)
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
call_1336 = relay.TupleGetItem(func_764_call(relay.reshape(call_1333.astype('bool'), [16, 8, 2])), 0)
call_1337 = relay.TupleGetItem(func_767_call(relay.reshape(call_1333.astype('bool'), [16, 8, 2])), 0)
output = relay.Tuple([bop_1327,call_1333,const_1334,call_1336,])
output2 = relay.Tuple([bop_1327,call_1335,const_1334,call_1337,])
func_1339 = relay.Function([var_1325,], output)
mod['func_1339'] = func_1339
mod = relay.transform.InferType()(mod)
mutated_mod['func_1339'] = func_1339
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1340 = relay.var("var_1340", dtype = "bool", shape = (13, 4, 11))#candidate|1340|(13, 4, 11)|var|bool
func_1339_call = mutated_mod.get_global_var('func_1339')
call_1341 = func_1339_call(var_1340)
output = call_1341
func_1342 = relay.Function([var_1340], output)
mutated_mod['func_1342'] = func_1342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_666_call = mod.get_global_var('func_666')
func_667_call = mutated_mod.get_global_var('func_667')
call_1348 = func_666_call()
call_1349 = func_666_call()
output = call_1348
output2 = call_1349
func_1354 = relay.Function([], output)
mod['func_1354'] = func_1354
mod = relay.transform.InferType()(mod)
output = func_1354()
func_1355 = relay.Function([], output)
mutated_mod['func_1355'] = func_1355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1419 = relay.TupleGetItem(func_586_call(), 0)
call_1420 = relay.TupleGetItem(func_588_call(), 0)
output = relay.Tuple([call_1419,])
output2 = relay.Tuple([call_1420,])
func_1423 = relay.Function([], output)
mod['func_1423'] = func_1423
mod = relay.transform.InferType()(mod)
mutated_mod['func_1423'] = func_1423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1423_call = mutated_mod.get_global_var('func_1423')
call_1424 = func_1423_call()
output = call_1424
func_1425 = relay.Function([], output)
mutated_mod['func_1425'] = func_1425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1511 = relay.TupleGetItem(func_586_call(), 0)
call_1512 = relay.TupleGetItem(func_588_call(), 0)
output = relay.Tuple([call_1511,])
output2 = relay.Tuple([call_1512,])
func_1528 = relay.Function([], output)
mod['func_1528'] = func_1528
mod = relay.transform.InferType()(mod)
mutated_mod['func_1528'] = func_1528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1528_call = mutated_mod.get_global_var('func_1528')
call_1529 = func_1528_call()
output = call_1529
func_1530 = relay.Function([], output)
mutated_mod['func_1530'] = func_1530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_923_call = mutated_mod.get_global_var('func_923')
call_1545 = func_922_call()
call_1546 = func_922_call()
func_140_call = mod.get_global_var('func_140')
func_142_call = mutated_mod.get_global_var('func_142')
const_1556 = relay.const([-6.285172,8.612141,6.869453,-2.928223,9.602991,8.492666,3.223624,-9.424260,-5.513492,-5.416923,-7.937951,9.988527,1.424605,-2.212909,-7.123072,7.783110,0.630308,-5.747896,-4.520486,4.757403,-3.525867,4.302504,-0.217439,-1.752157,6.755537,1.909918,-1.309907,-6.745298,-3.782307,-2.958714,-4.731715,-3.000506,1.816947,-4.804676,7.225942,4.290528,-0.638380,-6.044955,-9.429150,-9.157783,1.290735,2.730195,-4.824774,7.129229,-2.497787,3.034804,6.016237,-2.655842,-9.538792,-1.440663,-8.279273,9.559302,9.015176,4.312453,0.652025,1.828603,9.738856,-4.496697,-6.348774,9.048198,-7.137361,-3.284291,-1.735761,-7.643883,8.798647,-5.523784,-2.512239,4.180780,8.784266,1.394999,-1.354434,1.193824,3.596595,5.055471,5.439928,-2.342815,2.091884,-7.361618,0.118751,-2.968136,9.064705,-7.129332,4.820605,2.102566,-8.078758,0.514034,-9.241129,2.582396,-8.171043,2.020468,5.671485,6.813300,-9.467397,-1.134535,-2.871366,2.253336,5.085031,0.704864,7.911849,-7.651561,1.648610,-6.580909,-7.324773,1.168924,-9.649851,0.288293,-7.495931,-8.468915,-1.636466,-0.965159,7.913635,-6.106683,3.321142,9.779842,9.455422,2.441914,5.982549,-8.008022,2.429725,7.587213,-6.224557,8.238092,6.172120,-9.155910,-9.041966,4.044644,-9.725292,-3.791322,3.987344,-2.585303,4.123121,-2.459892,3.838303,3.306470,-3.851984,-9.015582,3.158984,-9.642608,7.352559,-0.008162,3.668059,9.865706,0.211184,-2.361238,-2.672066,2.093965,-7.752185,-7.344994,-5.784715,-3.047358,-9.444134,-5.845150,-2.749555,3.701106,6.006702,7.065061,5.996150,-3.006026,-9.258223,9.030473,2.193799,0.604592,-8.397368,4.543751,2.444190,-4.069981,-3.229035,0.950427,1.289677,-0.630814,-3.981511,8.752756,-0.776500,-8.240822,-2.216946,9.606304,5.191856,3.448347,5.310333,-3.487402,-5.461539,-5.746970,6.855000,4.635970,-3.522995,3.502190,7.368420,-9.269564,-0.881688,1.505750,5.282871,-8.649809,2.948131,-7.936625,-4.637024,3.651058,8.705165,0.271961,0.831296,0.131036,-3.067702,-7.476412,-3.783296,-4.663888,9.748738,1.757584,-0.779498,1.543972,-7.457047,-1.247525,1.386640,7.407429,-9.824053,3.817340,-2.038739,4.298311,-6.343160,-2.924621,7.567805,1.604400,-0.476613,7.668174,7.929030,-8.401415,-0.951932,-3.057586,-0.065164,1.193711,3.078109,-9.617432,5.361696,-6.662571,2.997513,-7.815053,1.741770,-9.441492,5.730449,5.662813,-3.324821,-4.954343,-9.265687,-7.776161,-8.459211,2.247841,8.321873,0.965461,-7.399079,-5.774644,4.508100,-7.513491,-9.264520,-5.069435,-4.820883,-9.835736,-4.875809,2.467292,-9.597376,8.545650,9.875229,-0.397387,6.000194,-4.011693,9.492500,0.844000,3.241597,-9.768713,-2.281816,7.426546,-7.934302,-2.470782,-2.073684,9.061194,9.830658,-8.665508,-1.679285,6.053314,-0.716058,6.298878,-0.734429,-2.233878,-9.273767,-5.158286,-0.832045,4.742261,0.535217,8.087091,2.065833,-1.459389,3.268714,-0.705512,6.286029,7.799361,3.525048,-8.946819,-3.669032,8.515505,6.346304,8.257157,-4.255292,-1.663996,-2.508779,2.128723,-4.550603,0.950678,-8.735399,3.144638,4.373235,-3.726954,4.283860,6.856984,4.072953,-7.237115,-4.323573,-8.150084,-8.014043,-9.132926,-8.599131,0.329536,-0.253490,9.003291,-1.724533,-4.014912,5.260634,-0.997370,6.047694,-5.147868,-8.225931,4.656688,3.871582,5.910535,-0.431728,-3.480345,-3.612427,-6.076705,-8.042714,2.077576,-6.554507,4.770433,-2.410499,2.490212,2.033154,4.875120,-6.497540,-6.013169,-4.394566,-2.091004,6.746687,-0.989648,-7.382575,-5.241560,-7.883428,2.928484,-9.488085,-9.253778,-0.733091,-3.380322,-7.431620,9.475594,8.054929,-4.010395,-9.813551,-3.110882,9.318568,7.768754,3.647301,0.074891,5.760981,0.733170,9.193334,9.377162,1.740591,9.024686,5.676809,-4.432633,-8.050958,-7.838967,5.050748,-5.537264,2.050236,-1.194528,-6.736585,-0.804024,-1.223634,3.139294,-4.880909,7.139455,-4.337613,0.798259,-3.279342,-5.477447,-9.700664,3.897657,-0.341035,-6.722114,1.881845,-9.295352,-8.118677,9.555748,-4.801633,-7.318067,8.204999,-9.947319,-4.588942,7.997476,-2.514070], dtype = "float32")#candidate|1556|(405,)|const|float32
call_1555 = relay.TupleGetItem(func_140_call(relay.reshape(const_1556.astype('float32'), [15, 9, 3])), 1)
call_1557 = relay.TupleGetItem(func_142_call(relay.reshape(const_1556.astype('float32'), [15, 9, 3])), 1)
uop_1571 = relay.sigmoid(call_1545.astype('float64')) # shape=(16, 8, 2)
uop_1573 = relay.sigmoid(call_1546.astype('float64')) # shape=(16, 8, 2)
output = relay.Tuple([call_1555,const_1556,uop_1571,])
output2 = relay.Tuple([call_1557,const_1556,uop_1573,])
func_1575 = relay.Function([], output)
mod['func_1575'] = func_1575
mod = relay.transform.InferType()(mod)
output = func_1575()
func_1576 = relay.Function([], output)
mutated_mod['func_1576'] = func_1576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_1586 = func_316_call()
call_1587 = func_316_call()
output = call_1586
output2 = call_1587
func_1592 = relay.Function([], output)
mod['func_1592'] = func_1592
mod = relay.transform.InferType()(mod)
mutated_mod['func_1592'] = func_1592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mutated_mod.get_global_var('func_1592')
call_1593 = func_1592_call()
output = call_1593
func_1594 = relay.Function([], output)
mutated_mod['func_1594'] = func_1594
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1607 = relay.const([[[2.294430,-0.333296,-5.888488,-0.657151,-9.413352,-7.366841,-7.443011,6.969173,-3.183890,6.891036],[4.164181,-1.415546,-5.869021,4.544466,-0.954158,6.613158,-9.791558,9.193931,2.244735,-8.775916],[-5.796104,-9.802140,8.447882,-2.846560,8.308160,9.546525,4.400066,-4.830039,0.320320,0.914904],[-8.916145,5.233710,-6.112437,-0.669318,2.556970,-3.347082,8.353022,-4.775002,-2.477509,-3.739089],[-2.988879,-2.627855,9.580932,9.642947,-1.778413,0.622188,-5.057196,-3.195226,1.687050,-6.117526],[3.704818,5.188565,1.665252,3.809044,-8.270018,2.706112,7.266738,-1.944121,7.079740,8.511932],[-9.314917,-3.564529,-0.491613,-4.594328,2.296413,-1.040360,4.103604,8.514965,5.374060,-8.424137],[-6.055827,-7.385504,9.094579,7.876963,-6.070388,-5.739490,3.868278,3.926474,6.894753,9.521544],[-5.837441,3.222078,7.093050,-8.908197,2.268116,-7.989443,5.881205,-4.426582,-1.266725,8.975019],[-2.499825,4.220102,-9.099036,9.145551,-9.102373,0.665939,-5.462354,-4.897974,8.500484,-2.546187],[1.894809,2.823460,5.495643,4.891246,9.150197,4.226163,9.137548,0.485638,4.310975,2.619657],[2.273883,8.696461,-1.799644,-2.601814,-5.209424,-3.865195,4.552897,-1.213885,9.550670,-7.395812]],[[-1.663854,9.876015,2.269920,-4.221036,5.304431,-1.872647,-2.749244,8.225714,-1.594108,-7.220133],[-5.653290,-5.067343,-2.237168,4.398552,9.982603,-3.396760,5.386149,8.068794,-5.507731,5.908338],[2.647654,1.378810,7.500595,-1.090962,-2.373327,1.000664,-6.196193,-9.780486,-6.987282,-4.405933],[-1.604074,-7.534543,-4.419024,-7.184911,8.194386,3.462992,4.092122,-0.661689,2.337998,-1.155242],[8.900224,-0.148010,-8.247789,9.390679,-2.190910,-5.590783,-6.654263,-5.280538,-7.325835,-4.394553],[3.954940,-0.206379,-2.128570,6.363704,-4.972972,7.426917,5.558425,7.182916,-5.806934,2.972139],[-7.583007,5.432244,-2.393932,-4.394278,-5.901622,-7.765436,-6.304664,5.415566,9.408061,-7.770484],[-7.155523,2.940974,5.184730,9.165116,7.512218,1.179424,-0.070976,2.975297,-6.122049,0.581866],[-1.530171,-3.818710,0.034906,3.806629,1.115625,-4.379947,9.975699,4.945710,-8.023138,-2.164469],[8.428117,3.711303,0.097592,-0.611781,-4.223083,-7.640313,6.659996,7.652651,-4.729558,5.174861],[-9.639605,-8.133280,-4.251750,6.359972,-7.968137,-1.565433,9.459194,-8.938340,-3.478061,-3.417130],[-1.874545,6.489725,-5.392487,-8.835474,9.833440,-2.244946,5.748303,4.736812,-7.492260,-3.780223]]], dtype = "float64")#candidate|1607|(2, 12, 10)|const|float64
uop_1608 = relay.atanh(const_1607.astype('float64')) # shape=(2, 12, 10)
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
var_1611 = relay.var("var_1611", dtype = "bool", shape = (32, 8))#candidate|1611|(32, 8)|var|bool
call_1610 = relay.TupleGetItem(func_764_call(relay.reshape(var_1611.astype('bool'), [16, 8, 2])), 0)
call_1612 = relay.TupleGetItem(func_767_call(relay.reshape(var_1611.astype('bool'), [16, 8, 2])), 0)
uop_1616 = relay.log10(uop_1608.astype('float32')) # shape=(2, 12, 10)
output = relay.Tuple([call_1610,var_1611,uop_1616,])
output2 = relay.Tuple([call_1612,var_1611,uop_1616,])
func_1618 = relay.Function([var_1611,], output)
mod['func_1618'] = func_1618
mod = relay.transform.InferType()(mod)
mutated_mod['func_1618'] = func_1618
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1619 = relay.var("var_1619", dtype = "bool", shape = (32, 8))#candidate|1619|(32, 8)|var|bool
func_1618_call = mutated_mod.get_global_var('func_1618')
call_1620 = func_1618_call(var_1619)
output = call_1620
func_1621 = relay.Function([var_1619], output)
mutated_mod['func_1621'] = func_1621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_923_call = mutated_mod.get_global_var('func_923')
call_1661 = func_922_call()
call_1662 = func_922_call()
output = call_1661
output2 = call_1662
func_1663 = relay.Function([], output)
mod['func_1663'] = func_1663
mod = relay.transform.InferType()(mod)
mutated_mod['func_1663'] = func_1663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1663_call = mutated_mod.get_global_var('func_1663')
call_1664 = func_1663_call()
output = call_1664
func_1665 = relay.Function([], output)
mutated_mod['func_1665'] = func_1665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_1674 = relay.TupleGetItem(func_586_call(), 0)
call_1675 = relay.TupleGetItem(func_588_call(), 0)
func_1618_call = mod.get_global_var('func_1618')
func_1621_call = mutated_mod.get_global_var('func_1621')
call_1693 = relay.TupleGetItem(func_1618_call(relay.reshape(call_1674.astype('bool'), [32, 8])), 1)
call_1694 = relay.TupleGetItem(func_1621_call(relay.reshape(call_1674.astype('bool'), [32, 8])), 1)
bop_1699 = relay.logical_or(call_1693.astype('bool'), relay.reshape(call_1674.astype('bool'), relay.shape_of(call_1693))) # shape=(32, 8)
bop_1702 = relay.logical_or(call_1694.astype('bool'), relay.reshape(call_1675.astype('bool'), relay.shape_of(call_1694))) # shape=(32, 8)
bop_1704 = relay.logical_and(call_1693.astype('bool'), relay.reshape(call_1674.astype('bool'), relay.shape_of(call_1693))) # shape=(32, 8)
bop_1707 = relay.logical_and(call_1694.astype('bool'), relay.reshape(call_1675.astype('bool'), relay.shape_of(call_1694))) # shape=(32, 8)
bop_1709 = relay.bitwise_or(bop_1699.astype('int32'), relay.reshape(bop_1704.astype('int32'), relay.shape_of(bop_1699))) # shape=(32, 8)
bop_1712 = relay.bitwise_or(bop_1702.astype('int32'), relay.reshape(bop_1707.astype('int32'), relay.shape_of(bop_1702))) # shape=(32, 8)
func_1110_call = mod.get_global_var('func_1110')
func_1114_call = mutated_mod.get_global_var('func_1114')
const_1716 = relay.const(False, dtype = "bool")#candidate|1716|()|const|bool
const_1717 = relay.const([[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False]], dtype = "bool")#candidate|1717|(12, 1)|const|bool
call_1715 = relay.TupleGetItem(func_1110_call(relay.reshape(const_1716.astype('bool'), []), relay.reshape(const_1717.astype('bool'), [12, 1]), ), 3)
call_1718 = relay.TupleGetItem(func_1114_call(relay.reshape(const_1716.astype('bool'), []), relay.reshape(const_1717.astype('bool'), [12, 1]), ), 3)
func_1528_call = mod.get_global_var('func_1528')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_1719 = relay.TupleGetItem(func_1528_call(), 0)
call_1720 = relay.TupleGetItem(func_1530_call(), 0)
output = relay.Tuple([bop_1709,call_1715,const_1716,const_1717,call_1719,])
output2 = relay.Tuple([bop_1712,call_1718,const_1716,const_1717,call_1720,])
func_1725 = relay.Function([], output)
mod['func_1725'] = func_1725
mod = relay.transform.InferType()(mod)
mutated_mod['func_1725'] = func_1725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1725_call = mutated_mod.get_global_var('func_1725')
call_1726 = func_1725_call()
output = call_1726
func_1727 = relay.Function([], output)
mutated_mod['func_1727'] = func_1727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_1789 = func_1354_call()
call_1790 = func_1354_call()
func_140_call = mod.get_global_var('func_140')
func_142_call = mutated_mod.get_global_var('func_142')
const_1802 = relay.const([[-9.703249,5.585643,0.955858,-9.816405,5.460317,-6.143459,8.693575,3.973436,-8.423511,8.743214,4.145999,-6.603229,-8.119226,-7.782775,-7.406672,-5.735659,-1.458653,-5.147109,-6.443273,-5.898279,-9.060337,-2.891962,4.311229,4.703371,1.830346,7.497791,-3.866188,9.058761,9.448193,9.027388,1.768730,9.241606,1.292725,3.968603,-5.177924,8.561424,-0.676597,-1.463493,7.741833,2.513655,-7.585541,-8.650648,2.043188,9.998371,3.482379,-3.571392,-3.311634,-4.518718,8.535006,-1.231922,9.630047,-3.102910,3.573217,8.752920,-4.934327,8.420471,-3.360225,7.212887,8.448589,-8.004152,0.233990,3.739645,-6.871011,8.797779,9.991097,8.387245,-5.810928,2.440273,8.877054,-8.072056,6.867156,-1.033292,3.400035,6.421273,9.197269,-7.533683,-4.850212,-6.507255,7.411062,-0.065017,5.909652,-5.580432,4.123365,-4.107402,-4.154781,9.332886,-9.900666,1.846393,3.418731,2.313934,0.653432,-3.087732,1.340591,-0.747329,-7.635229,-1.946396,9.501874,9.657312,-7.746995,0.933221,0.222091,-9.880055,-8.370208,4.911829,4.173787,-4.190023,-2.408013,-3.676076,-3.159806,9.819729,-0.274484,-2.708373,-9.146955,-4.249637,3.179076,6.577266,-6.894146,4.373776,-5.575055,3.905499,1.173052,-0.092060,-8.439921,1.847499,2.112544,9.680074,-5.936656,9.162950,-6.884747,0.754328,8.736266,-6.785368,6.234597,7.187058,-4.570633,9.365814,-7.914103,-0.933603,-1.010049,2.770565,-7.132219,5.344648,3.208101,9.990755,7.842235,5.548947,2.624699,-8.334823,7.075425,-3.649611,-6.360057,6.442766,0.470643,9.824563,-0.031932,-7.262477,-4.041708,6.320462,-7.518006,4.046599,-6.883435,2.037941,-2.894073,-9.756256,2.314568,0.116962,-3.541935,-2.546449,-5.565689,9.582176,5.036363,7.530816,-3.246767,7.327851,2.593764,-5.493890,1.331932,-4.964182,1.987450,-3.701362,6.378317,1.335628,-2.189816,-1.513165,9.192015,4.448562,0.336387,-5.139523,-1.566891,-4.815775,-5.655236,1.206593,-9.369824,5.459924,-3.938667,-4.850715,-4.942232,6.670592,-6.864769,9.977011,2.282937,-2.742573,-3.350607,-4.078269,-6.470290,-0.017075,1.129860,-3.807270,2.414257,-5.839689,0.943075,-7.484984,-9.736808,3.180993,9.280297,-9.461834,8.431561,1.929169,-0.281046,-1.071093,-7.577088,8.339301,-6.242804,-3.397685,-5.901493,6.648109,3.744527,1.789245,0.074887,-9.819237,9.470053,-6.939755,1.594326,-1.386134,5.927836,-7.975755,-7.231814,-5.690233,-4.436928,-2.946311,4.457604,-3.034806,3.274243,-1.553405,-9.147262,4.120573,1.216938,4.653791,4.686309,-1.724941,-3.042954,7.772634,1.215991,-3.478401,-4.438800,-2.733370,-7.691703,-8.156908,-5.234726,6.991107,-3.965322,-6.725214,-7.376635,-3.895705,-1.963406,-6.897597,-0.216389,7.776878,0.671783,5.899142,-0.783152,4.915836,-5.050700,0.707537,-8.766085,-4.647296,7.384335,5.429529,-6.430416,-1.987579,-7.706368,7.009762,-9.232624,-3.661664,-2.073856,9.636954,8.434436,-2.472231,-3.840429,-5.396033,-8.489994,8.150500,-0.947896,1.716597,7.270678,1.146499,-8.852413,-0.755351,5.208102,4.860930,-5.633368,-6.827816,5.568644,9.713023,-2.094989,9.391098,-8.205966,7.097741,6.297905,9.465080,-8.732058,-3.635137,-8.086550,6.465759,-2.362266,0.703100,0.458243,-9.770145,-2.635782,-2.385335,-5.406561,0.046924,6.870095,7.561396,8.460458,4.372880,4.788054,0.196497,-9.908297,3.927198,7.628423,6.192850,-9.501401,3.873791,5.389527,-1.681751,7.109781,8.366789,-1.146415,5.470896,3.610361,4.382957,2.836269,-2.768991,0.791831,-5.615167,8.066349,0.795867,9.691900,-7.194932,-1.500534,-8.579567,0.393288,-6.227708,-6.825318,4.221059,-6.703483,-2.539379,8.630656,2.117747,-5.057425,6.608320,4.668227,-0.456434,-5.018246,-4.405996,3.923843,-8.343984,-7.044149,-0.050872,3.783163,-1.925165,-3.726609,1.121724,-8.703930,-1.409901,-7.683151,-6.111579,-5.717652,-6.251772,4.600122,5.011582,-2.477176,9.249465,1.448832,2.032599,-9.016610,-8.812521,3.188569,-5.880641,4.807223,-4.017952,7.457022,9.562572,8.357352,-2.916395,-3.800550,9.971038,3.969748,2.940218,-6.538386,1.194118,8.447396,4.620712,3.808017]], dtype = "float32")#candidate|1802|(1, 405)|const|float32
call_1801 = relay.TupleGetItem(func_140_call(relay.reshape(const_1802.astype('float32'), [15, 9, 3])), 0)
call_1803 = relay.TupleGetItem(func_142_call(relay.reshape(const_1802.astype('float32'), [15, 9, 3])), 0)
func_922_call = mod.get_global_var('func_922')
func_923_call = mutated_mod.get_global_var('func_923')
call_1806 = func_922_call()
call_1807 = func_922_call()
bop_1809 = relay.bitwise_xor(call_1806.astype('int32'), relay.reshape(call_1789.astype('int32'), relay.shape_of(call_1806))) # shape=(16, 8, 2)
bop_1812 = relay.bitwise_xor(call_1807.astype('int32'), relay.reshape(call_1790.astype('int32'), relay.shape_of(call_1807))) # shape=(16, 8, 2)
output = relay.Tuple([call_1801,const_1802,bop_1809,])
output2 = relay.Tuple([call_1803,const_1802,bop_1812,])
func_1825 = relay.Function([], output)
mod['func_1825'] = func_1825
mod = relay.transform.InferType()(mod)
output = func_1825()
func_1826 = relay.Function([], output)
mutated_mod['func_1826'] = func_1826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_569_call = mod.get_global_var('func_569')
func_571_call = mutated_mod.get_global_var('func_571')
call_1856 = relay.TupleGetItem(func_569_call(), 0)
call_1857 = relay.TupleGetItem(func_571_call(), 0)
output = call_1856
output2 = call_1857
func_1884 = relay.Function([], output)
mod['func_1884'] = func_1884
mod = relay.transform.InferType()(mod)
mutated_mod['func_1884'] = func_1884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1884_call = mutated_mod.get_global_var('func_1884')
call_1885 = func_1884_call()
output = call_1885
func_1886 = relay.Function([], output)
mutated_mod['func_1886'] = func_1886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1884_call = mod.get_global_var('func_1884')
func_1886_call = mutated_mod.get_global_var('func_1886')
call_1906 = func_1884_call()
call_1907 = func_1884_call()
output = relay.Tuple([call_1906,])
output2 = relay.Tuple([call_1907,])
func_1915 = relay.Function([], output)
mod['func_1915'] = func_1915
mod = relay.transform.InferType()(mod)
mutated_mod['func_1915'] = func_1915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1915_call = mutated_mod.get_global_var('func_1915')
call_1916 = func_1915_call()
output = call_1916
func_1917 = relay.Function([], output)
mutated_mod['func_1917'] = func_1917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_1936 = relay.TupleGetItem(func_1575_call(), 0)
call_1937 = relay.TupleGetItem(func_1576_call(), 0)
var_1941 = relay.var("var_1941", dtype = "float32", shape = (15, 9, 3))#candidate|1941|(15, 9, 3)|var|float32
bop_1942 = relay.divide(call_1936.astype('float64'), relay.reshape(var_1941.astype('float64'), relay.shape_of(call_1936))) # shape=(15, 9, 3)
bop_1945 = relay.divide(call_1937.astype('float64'), relay.reshape(var_1941.astype('float64'), relay.shape_of(call_1937))) # shape=(15, 9, 3)
output = relay.Tuple([bop_1942,])
output2 = relay.Tuple([bop_1945,])
func_1949 = relay.Function([var_1941,], output)
mod['func_1949'] = func_1949
mod = relay.transform.InferType()(mod)
mutated_mod['func_1949'] = func_1949
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1950 = relay.var("var_1950", dtype = "float32", shape = (15, 9, 3))#candidate|1950|(15, 9, 3)|var|float32
func_1949_call = mutated_mod.get_global_var('func_1949')
call_1951 = func_1949_call(var_1950)
output = call_1951
func_1952 = relay.Function([var_1950], output)
mutated_mod['func_1952'] = func_1952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1528_call = mod.get_global_var('func_1528')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_2026 = relay.TupleGetItem(func_1528_call(), 0)
call_2027 = relay.TupleGetItem(func_1530_call(), 0)
func_764_call = mod.get_global_var('func_764')
func_767_call = mutated_mod.get_global_var('func_767')
call_2031 = relay.TupleGetItem(func_764_call(relay.reshape(call_2026.astype('bool'), [16, 8, 2])), 1)
call_2032 = relay.TupleGetItem(func_767_call(relay.reshape(call_2026.astype('bool'), [16, 8, 2])), 1)
output = relay.Tuple([call_2026,call_2031,])
output2 = relay.Tuple([call_2027,call_2032,])
func_2033 = relay.Function([], output)
mod['func_2033'] = func_2033
mod = relay.transform.InferType()(mod)
mutated_mod['func_2033'] = func_2033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2033_call = mutated_mod.get_global_var('func_2033')
call_2034 = func_2033_call()
output = call_2034
func_2035 = relay.Function([], output)
mutated_mod['func_2035'] = func_2035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1663_call = mod.get_global_var('func_1663')
func_1665_call = mutated_mod.get_global_var('func_1665')
call_2046 = func_1663_call()
call_2047 = func_1663_call()
output = call_2046
output2 = call_2047
func_2048 = relay.Function([], output)
mod['func_2048'] = func_2048
mod = relay.transform.InferType()(mod)
output = func_2048()
func_2049 = relay.Function([], output)
mutated_mod['func_2049'] = func_2049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_2080 = func_1592_call()
call_2081 = func_1592_call()
var_2085 = relay.var("var_2085", dtype = "bool", shape = (16, 8, 2))#candidate|2085|(16, 8, 2)|var|bool
bop_2086 = relay.logical_or(call_2080.astype('bool'), relay.reshape(var_2085.astype('bool'), relay.shape_of(call_2080))) # shape=(16, 8, 2)
bop_2089 = relay.logical_or(call_2081.astype('bool'), relay.reshape(var_2085.astype('bool'), relay.shape_of(call_2081))) # shape=(16, 8, 2)
func_377_call = mod.get_global_var('func_377')
func_380_call = mutated_mod.get_global_var('func_380')
var_2091 = relay.var("var_2091", dtype = "float64", shape = (77,))#candidate|2091|(77,)|var|float64
call_2090 = relay.TupleGetItem(func_377_call(relay.reshape(var_2091.astype('float64'), [11, 1, 7])), 0)
call_2092 = relay.TupleGetItem(func_380_call(relay.reshape(var_2091.astype('float64'), [11, 1, 7])), 0)
func_1339_call = mod.get_global_var('func_1339')
func_1342_call = mutated_mod.get_global_var('func_1342')
const_2095 = relay.const([False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True], dtype = "bool")#candidate|2095|(572,)|const|bool
call_2094 = relay.TupleGetItem(func_1339_call(relay.reshape(const_2095.astype('bool'), [13, 4, 11])), 2)
call_2096 = relay.TupleGetItem(func_1342_call(relay.reshape(const_2095.astype('bool'), [13, 4, 11])), 2)
var_2105 = relay.var("var_2105", dtype = "float64", shape = (77,))#candidate|2105|(77,)|var|float64
bop_2106 = relay.greater_equal(var_2091.astype('bool'), relay.reshape(var_2105.astype('bool'), relay.shape_of(var_2091))) # shape=(77,)
const_2116 = relay.const([-4.529099,-2.957590,7.946803,-5.946030,1.812208,4.724103,-7.034344,0.104730,-3.119009,5.295528,7.370384,6.594801,0.353094,6.909749,9.111810,-9.946017,-4.271721,-7.943223,4.315921,1.462494,7.343552,1.723915,-4.101323,7.014450,0.473599,-7.915173,-8.708585,-2.151180,-2.605365,-1.930915,-5.356230,-9.284879,6.183248,-3.894104,4.126574,-6.584085,-8.917598,-1.642235,-5.986582,-5.914121,-8.143044,2.678735,-8.303994,-8.352011,2.996040,8.864658,-0.380513,7.787146,-1.812054,-4.032091,4.459809,6.889409,-4.758794,3.702934,7.160258,0.198695,-5.233369,3.992330,-4.435964,-3.523033,-1.492494,5.894299,9.834817,2.304637,-0.946118,1.123963,-6.683440,2.963984,0.672877,4.507837,-2.022422,-6.242266,4.006454,-1.999119,-2.419325,-8.963674,-1.922759], dtype = "float64")#candidate|2116|(77,)|const|float64
bop_2117 = relay.less_equal(var_2105.astype('bool'), relay.reshape(const_2116.astype('bool'), relay.shape_of(var_2105))) # shape=(77,)
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_2132 = func_1354_call()
call_2133 = func_1354_call()
output = relay.Tuple([bop_2086,call_2090,call_2094,const_2095,bop_2106,bop_2117,call_2132,])
output2 = relay.Tuple([bop_2089,call_2092,call_2096,const_2095,bop_2106,bop_2117,call_2133,])
func_2134 = relay.Function([var_2085,var_2091,var_2105,], output)
mod['func_2134'] = func_2134
mod = relay.transform.InferType()(mod)
mutated_mod['func_2134'] = func_2134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2134_call = mutated_mod.get_global_var('func_2134')
var_2136 = relay.var("var_2136", dtype = "bool", shape = (16, 8, 2))#candidate|2136|(16, 8, 2)|var|bool
var_2137 = relay.var("var_2137", dtype = "float64", shape = (77,))#candidate|2137|(77,)|var|float64
var_2138 = relay.var("var_2138", dtype = "float64", shape = (77,))#candidate|2138|(77,)|var|float64
call_2135 = func_2134_call(var_2136,var_2137,var_2138,)
output = call_2135
func_2139 = relay.Function([var_2136,var_2137,var_2138,], output)
mutated_mod['func_2139'] = func_2139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_2156 = func_1592_call()
call_2157 = func_1592_call()
func_1663_call = mod.get_global_var('func_1663')
func_1665_call = mutated_mod.get_global_var('func_1665')
call_2160 = func_1663_call()
call_2161 = func_1663_call()
output = relay.Tuple([call_2156,call_2160,])
output2 = relay.Tuple([call_2157,call_2161,])
func_2168 = relay.Function([], output)
mod['func_2168'] = func_2168
mod = relay.transform.InferType()(mod)
output = func_2168()
func_2169 = relay.Function([], output)
mutated_mod['func_2169'] = func_2169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1915_call = mod.get_global_var('func_1915')
func_1917_call = mutated_mod.get_global_var('func_1917')
call_2239 = relay.TupleGetItem(func_1915_call(), 0)
call_2240 = relay.TupleGetItem(func_1917_call(), 0)
var_2265 = relay.var("var_2265", dtype = "bool", shape = (16, 8, 2))#candidate|2265|(16, 8, 2)|var|bool
bop_2266 = relay.left_shift(call_2239.astype('int32'), relay.reshape(var_2265.astype('int32'), relay.shape_of(call_2239))) # shape=(16, 8, 2)
bop_2269 = relay.left_shift(call_2240.astype('int32'), relay.reshape(var_2265.astype('int32'), relay.shape_of(call_2240))) # shape=(16, 8, 2)
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_2271 = func_1354_call()
call_2272 = func_1354_call()
uop_2273 = relay.sqrt(call_2271.astype('float32')) # shape=(16, 8, 2)
uop_2275 = relay.sqrt(call_2272.astype('float32')) # shape=(16, 8, 2)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_2283 = func_1592_call()
call_2284 = func_1592_call()
output = relay.Tuple([bop_2266,uop_2273,call_2283,])
output2 = relay.Tuple([bop_2269,uop_2275,call_2284,])
func_2291 = relay.Function([var_2265,], output)
mod['func_2291'] = func_2291
mod = relay.transform.InferType()(mod)
mutated_mod['func_2291'] = func_2291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2292 = relay.var("var_2292", dtype = "bool", shape = (16, 8, 2))#candidate|2292|(16, 8, 2)|var|bool
func_2291_call = mutated_mod.get_global_var('func_2291')
call_2293 = func_2291_call(var_2292)
output = call_2293
func_2294 = relay.Function([var_2292], output)
mutated_mod['func_2294'] = func_2294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_586_call = mod.get_global_var('func_586')
func_588_call = mutated_mod.get_global_var('func_588')
call_2374 = relay.TupleGetItem(func_586_call(), 0)
call_2375 = relay.TupleGetItem(func_588_call(), 0)
func_1663_call = mod.get_global_var('func_1663')
func_1665_call = mutated_mod.get_global_var('func_1665')
call_2382 = func_1663_call()
call_2383 = func_1663_call()
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_2403 = func_316_call()
call_2404 = func_316_call()
output = relay.Tuple([call_2374,call_2382,call_2403,])
output2 = relay.Tuple([call_2375,call_2383,call_2404,])
func_2406 = relay.Function([], output)
mod['func_2406'] = func_2406
mod = relay.transform.InferType()(mod)
output = func_2406()
func_2407 = relay.Function([], output)
mutated_mod['func_2407'] = func_2407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_2413 = func_1354_call()
call_2414 = func_1354_call()
func_897_call = mod.get_global_var('func_897')
func_900_call = mutated_mod.get_global_var('func_900')
var_2427 = relay.var("var_2427", dtype = "uint8", shape = (8, 18))#candidate|2427|(8, 18)|var|uint8
call_2426 = relay.TupleGetItem(func_897_call(relay.reshape(var_2427.astype('uint8'), [9, 8, 2])), 1)
call_2428 = relay.TupleGetItem(func_900_call(relay.reshape(var_2427.astype('uint8'), [9, 8, 2])), 1)
uop_2435 = relay.erf(var_2427.astype('float32')) # shape=(8, 18)
uop_2444 = relay.rsqrt(uop_2435.astype('float32')) # shape=(8, 18)
output = relay.Tuple([call_2413,call_2426,uop_2444,])
output2 = relay.Tuple([call_2414,call_2428,uop_2444,])
func_2460 = relay.Function([var_2427,], output)
mod['func_2460'] = func_2460
mod = relay.transform.InferType()(mod)
var_2461 = relay.var("var_2461", dtype = "uint8", shape = (8, 18))#candidate|2461|(8, 18)|var|uint8
output = func_2460(var_2461)
func_2462 = relay.Function([var_2461], output)
mutated_mod['func_2462'] = func_2462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_923_call = mutated_mod.get_global_var('func_923')
call_2481 = func_922_call()
call_2482 = func_922_call()
output = relay.Tuple([call_2481,])
output2 = relay.Tuple([call_2482,])
func_2486 = relay.Function([], output)
mod['func_2486'] = func_2486
mod = relay.transform.InferType()(mod)
mutated_mod['func_2486'] = func_2486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mutated_mod.get_global_var('func_2486')
call_2487 = func_2486_call()
output = call_2487
func_2488 = relay.Function([], output)
mutated_mod['func_2488'] = func_2488
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2499 = relay.var("var_2499", dtype = "float32", shape = (6, 3, 1))#candidate|2499|(6, 3, 1)|var|float32
uop_2500 = relay.sinh(var_2499.astype('float32')) # shape=(6, 3, 1)
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
const_2513 = relay.const([5,-6,-1,8,-7,-9,2,10,8,-7,-8,-1,-6,2,-7,8,10,10,5,1,7,-1,-7,-6,-4,-2,-10,9,-7,-5,6,8,-7,9,10,-6,-2,-5,1,-6,6,7,-10,2,-7,-6,2,1,4,-3,-10,3,-9,10,2,3,3,6,6,3,-6,-6,-2,-8,-5,-3,10,-6,8,9,2,-10,1,8,-5,-1,-1,9,-4,-2,-8,5,-4,-8,-8,4,8,3,-9,9,6,-5,6,10,1,-2,-8,-8,9,5,-3,-5,5,2,-3,-10,-10,-3,8,-10,-7,1,-9,-10,-5,6,-5,2,-3,6,5,2,-10,6,2,1,8,7,-1,8,5,5,-6,-2,1,-2,3,-4,3,-2,-7,4,-5,5], dtype = "uint8")#candidate|2513|(144,)|const|uint8
call_2512 = relay.TupleGetItem(func_2460_call(relay.reshape(const_2513.astype('uint8'), [8, 18])), 0)
call_2514 = relay.TupleGetItem(func_2462_call(relay.reshape(const_2513.astype('uint8'), [8, 18])), 0)
func_316_call = mod.get_global_var('func_316')
func_317_call = mutated_mod.get_global_var('func_317')
call_2515 = func_316_call()
call_2516 = func_316_call()
uop_2517 = relay.cosh(uop_2500.astype('float64')) # shape=(6, 3, 1)
uop_2523 = relay.erf(uop_2500.astype('float64')) # shape=(6, 3, 1)
uop_2526 = relay.rsqrt(uop_2500.astype('float32')) # shape=(6, 3, 1)
output = relay.Tuple([call_2512,const_2513,call_2515,uop_2517,uop_2523,uop_2526,])
output2 = relay.Tuple([call_2514,const_2513,call_2516,uop_2517,uop_2523,uop_2526,])
func_2542 = relay.Function([var_2499,], output)
mod['func_2542'] = func_2542
mod = relay.transform.InferType()(mod)
var_2543 = relay.var("var_2543", dtype = "float32", shape = (6, 3, 1))#candidate|2543|(6, 3, 1)|var|float32
output = func_2542(var_2543)
func_2544 = relay.Function([var_2543], output)
mutated_mod['func_2544'] = func_2544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mod.get_global_var('func_2486')
func_2488_call = mutated_mod.get_global_var('func_2488')
call_2562 = relay.TupleGetItem(func_2486_call(), 0)
call_2563 = relay.TupleGetItem(func_2488_call(), 0)
func_1321_call = mod.get_global_var('func_1321')
func_1323_call = mutated_mod.get_global_var('func_1323')
var_2590 = relay.var("var_2590", dtype = "float32", shape = (405,))#candidate|2590|(405,)|var|float32
call_2589 = relay.TupleGetItem(func_1321_call(relay.reshape(var_2590.astype('float32'), [405,])), 3)
call_2591 = relay.TupleGetItem(func_1323_call(relay.reshape(var_2590.astype('float32'), [405,])), 3)
func_2486_call = mod.get_global_var('func_2486')
func_2488_call = mutated_mod.get_global_var('func_2488')
call_2597 = relay.TupleGetItem(func_2486_call(), 0)
call_2598 = relay.TupleGetItem(func_2488_call(), 0)
output = relay.Tuple([call_2562,call_2589,var_2590,call_2597,])
output2 = relay.Tuple([call_2563,call_2591,var_2590,call_2598,])
func_2605 = relay.Function([var_2590,], output)
mod['func_2605'] = func_2605
mod = relay.transform.InferType()(mod)
var_2606 = relay.var("var_2606", dtype = "float32", shape = (405,))#candidate|2606|(405,)|var|float32
output = func_2605(var_2606)
func_2607 = relay.Function([var_2606], output)
mutated_mod['func_2607'] = func_2607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_2668 = relay.TupleGetItem(func_2168_call(), 1)
call_2669 = relay.TupleGetItem(func_2169_call(), 1)
output = relay.Tuple([call_2668,])
output2 = relay.Tuple([call_2669,])
func_2686 = relay.Function([], output)
mod['func_2686'] = func_2686
mod = relay.transform.InferType()(mod)
output = func_2686()
func_2687 = relay.Function([], output)
mutated_mod['func_2687'] = func_2687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1528_call = mod.get_global_var('func_1528')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_2700 = relay.TupleGetItem(func_1528_call(), 0)
call_2701 = relay.TupleGetItem(func_1530_call(), 0)
func_2134_call = mod.get_global_var('func_2134')
func_2139_call = mutated_mod.get_global_var('func_2139')
var_2705 = relay.var("var_2705", dtype = "float64", shape = (77,))#candidate|2705|(77,)|var|float64
call_2704 = relay.TupleGetItem(func_2134_call(relay.reshape(call_2700.astype('bool'), [16, 8, 2]), relay.reshape(var_2705.astype('float64'), [77,]), relay.reshape(var_2705.astype('float64'), [77,]), ), 5)
call_2706 = relay.TupleGetItem(func_2139_call(relay.reshape(call_2700.astype('bool'), [16, 8, 2]), relay.reshape(var_2705.astype('float64'), [77,]), relay.reshape(var_2705.astype('float64'), [77,]), ), 5)
bop_2712 = relay.power(var_2705.astype('float32'), relay.reshape(call_2704.astype('float32'), relay.shape_of(var_2705))) # shape=(77,)
bop_2715 = relay.power(var_2705.astype('float32'), relay.reshape(call_2706.astype('float32'), relay.shape_of(var_2705))) # shape=(77,)
uop_2725 = relay.atanh(call_2700.astype('float32')) # shape=(16, 8, 2)
uop_2727 = relay.atanh(call_2701.astype('float32')) # shape=(16, 8, 2)
uop_2728 = relay.sinh(call_2704.astype('float32')) # shape=(77,)
uop_2730 = relay.sinh(call_2706.astype('float32')) # shape=(77,)
uop_2736 = relay.cos(uop_2725.astype('float32')) # shape=(16, 8, 2)
uop_2738 = relay.cos(uop_2727.astype('float32')) # shape=(16, 8, 2)
uop_2742 = relay.atanh(var_2705.astype('float32')) # shape=(77,)
output = relay.Tuple([bop_2712,uop_2728,uop_2736,uop_2742,])
output2 = relay.Tuple([bop_2715,uop_2730,uop_2738,uop_2742,])
func_2744 = relay.Function([var_2705,], output)
mod['func_2744'] = func_2744
mod = relay.transform.InferType()(mod)
var_2745 = relay.var("var_2745", dtype = "float64", shape = (77,))#candidate|2745|(77,)|var|float64
output = func_2744(var_2745)
func_2746 = relay.Function([var_2745], output)
mutated_mod['func_2746'] = func_2746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1528_call = mod.get_global_var('func_1528')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_2765 = relay.TupleGetItem(func_1528_call(), 0)
call_2766 = relay.TupleGetItem(func_1530_call(), 0)
var_2771 = relay.var("var_2771", dtype = "bool", shape = (16, 8, 2))#candidate|2771|(16, 8, 2)|var|bool
bop_2772 = relay.logical_xor(call_2765.astype('uint16'), relay.reshape(var_2771.astype('uint16'), relay.shape_of(call_2765))) # shape=(16, 8, 2)
bop_2775 = relay.logical_xor(call_2766.astype('uint16'), relay.reshape(var_2771.astype('uint16'), relay.shape_of(call_2766))) # shape=(16, 8, 2)
output = relay.Tuple([bop_2772,])
output2 = relay.Tuple([bop_2775,])
func_2777 = relay.Function([var_2771,], output)
mod['func_2777'] = func_2777
mod = relay.transform.InferType()(mod)
mutated_mod['func_2777'] = func_2777
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2778 = relay.var("var_2778", dtype = "bool", shape = (16, 8, 2))#candidate|2778|(16, 8, 2)|var|bool
func_2777_call = mutated_mod.get_global_var('func_2777')
call_2779 = func_2777_call(var_2778)
output = call_2779
func_2780 = relay.Function([var_2778], output)
mutated_mod['func_2780'] = func_2780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1725_call = mod.get_global_var('func_1725')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_2797 = relay.TupleGetItem(func_1725_call(), 2)
call_2798 = relay.TupleGetItem(func_1727_call(), 2)
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_2810 = func_1354_call()
call_2811 = func_1354_call()
bop_2815 = relay.maximum(call_2797.astype('float64'), call_2810.astype('float64')) # shape=(16, 8, 2)
bop_2818 = relay.maximum(call_2798.astype('float64'), call_2811.astype('float64')) # shape=(16, 8, 2)
func_2134_call = mod.get_global_var('func_2134')
func_2139_call = mutated_mod.get_global_var('func_2139')
const_2822 = relay.const([[4.602236],[-0.054612],[-0.774422],[9.553160],[-2.285880],[4.052156],[2.587615],[-6.122038],[5.633836],[9.233319],[4.603243],[9.074463],[-5.316209],[0.069385],[-5.549468],[-6.571310],[4.703378],[-1.886835],[4.403511],[-8.425896],[-1.345375],[6.050817],[1.768733],[5.289149],[0.572483],[-6.863179],[5.166432],[-7.053132],[-6.722736],[1.846117],[5.344614],[-4.670290],[-9.680147],[-9.512782],[5.874316],[-7.919085],[-6.054648],[7.264437],[6.094962],[-1.750574],[-1.677580],[9.592978],[9.313863],[4.775308],[5.605487],[-1.408968],[-0.102874],[4.222181],[5.202005],[-1.668204],[2.406549],[0.258086],[5.259929],[9.722701],[5.508213],[6.521846],[-4.538023],[-7.029020],[-3.154980],[0.669366],[-4.045927],[-5.422807],[0.250783],[1.369715],[-1.458911],[3.482972],[-4.882868],[6.813698],[9.289116],[3.190822],[1.543028],[-9.850861],[0.547785],[1.783584],[-9.266656],[-1.223830],[-7.745513]], dtype = "float64")#candidate|2822|(77, 1)|const|float64
call_2821 = relay.TupleGetItem(func_2134_call(relay.reshape(call_2810.astype('bool'), [16, 8, 2]), relay.reshape(const_2822.astype('float64'), [77,]), relay.reshape(const_2822.astype('float64'), [77,]), ), 1)
call_2823 = relay.TupleGetItem(func_2139_call(relay.reshape(call_2810.astype('bool'), [16, 8, 2]), relay.reshape(const_2822.astype('float64'), [77,]), relay.reshape(const_2822.astype('float64'), [77,]), ), 1)
func_1528_call = mod.get_global_var('func_1528')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_2826 = relay.TupleGetItem(func_1528_call(), 0)
call_2827 = relay.TupleGetItem(func_1530_call(), 0)
output = relay.Tuple([bop_2815,call_2821,const_2822,call_2826,])
output2 = relay.Tuple([bop_2818,call_2823,const_2822,call_2827,])
func_2828 = relay.Function([], output)
mod['func_2828'] = func_2828
mod = relay.transform.InferType()(mod)
output = func_2828()
func_2829 = relay.Function([], output)
mutated_mod['func_2829'] = func_2829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_2838 = relay.TupleGetItem(func_1575_call(), 0)
call_2839 = relay.TupleGetItem(func_1576_call(), 0)
uop_2844 = relay.sigmoid(call_2838.astype('float32')) # shape=(15, 9, 3)
uop_2846 = relay.sigmoid(call_2839.astype('float32')) # shape=(15, 9, 3)
output = relay.Tuple([uop_2844,])
output2 = relay.Tuple([uop_2846,])
func_2859 = relay.Function([], output)
mod['func_2859'] = func_2859
mod = relay.transform.InferType()(mod)
output = func_2859()
func_2860 = relay.Function([], output)
mutated_mod['func_2860'] = func_2860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2869 = relay.var("var_2869", dtype = "float32", shape = (2, 15, 8))#candidate|2869|(2, 15, 8)|var|float32
const_2870 = relay.const([[[5.160934,3.993582,-2.046194,-9.967562,4.984533,1.191537,-4.769418,4.205681],[-9.617916,-4.414072,3.547189,-3.152714,7.398027,2.857637,-8.866169,-9.373377],[-2.390877,9.144509,3.929764,2.494678,4.990932,6.806406,-2.181760,5.171829],[-2.345247,1.160209,-9.833312,-1.673913,-6.435898,8.192577,-9.390392,1.034197],[0.591682,6.251204,-8.376302,7.242166,-4.001866,-6.265973,6.351110,9.068422],[0.495251,0.263297,-1.176941,3.975604,1.817052,-6.278988,8.128026,-9.265810],[-4.428880,7.701567,-6.902707,-9.267748,6.786759,7.789142,3.973986,4.998226],[-3.598620,-1.990185,-9.816224,4.458432,-4.041297,-6.004550,5.846526,-6.987269],[-7.259999,8.346719,-3.721820,0.177419,-8.404403,-6.697092,4.979542,-9.679391],[-8.302788,8.642220,-0.532291,2.744749,-8.592385,-2.001056,-7.861193,7.869287],[-4.114466,-8.786446,3.193269,7.036308,-9.987608,5.494063,3.764045,7.117874],[-5.632254,-6.451535,-8.147744,-8.752559,1.463919,-8.045485,4.922878,8.771590],[-9.096354,3.599811,0.195162,9.992325,-6.744718,-2.624628,-6.798552,-1.258900],[-3.373136,-0.137113,-4.535222,2.963154,8.246998,7.510854,4.905249,9.518209],[-7.334133,9.829543,4.735097,-1.277122,1.933395,3.178964,-6.908488,7.629772]],[[-5.384424,9.120904,-3.677808,3.208594,3.550762,-6.523756,7.613679,-6.617630],[-0.558043,7.450130,9.391575,-2.334424,-6.813301,-9.723261,5.248282,3.205927],[0.777042,-3.956961,8.224799,-9.588810,-2.980717,-0.935623,-3.972907,-9.669329],[-2.130495,-3.637130,8.720465,5.167060,-6.382069,-1.729334,8.049689,1.000467],[1.913365,-1.701401,5.309667,5.874768,0.072144,0.173843,-0.024115,6.737521],[-7.953879,-9.108169,-3.250485,8.290326,-7.276881,-9.991873,-7.738855,-4.418880],[2.997802,-1.380725,9.600805,-9.373347,9.715214,-9.267350,0.277161,4.111588],[4.788792,3.995837,7.226384,-1.185955,3.265382,9.644082,5.963477,0.917215],[-3.538801,3.858729,0.095691,-4.554285,-4.758159,-6.237522,-4.636996,6.508008],[-3.647904,4.272900,1.389726,7.202491,-7.153276,-9.273553,-1.262759,-3.140308],[-8.708712,2.000942,-3.332503,-6.878403,-3.489497,-1.003707,-1.268647,1.068460],[1.477865,-2.406590,-9.262619,9.451645,-9.100990,-4.499629,8.691679,8.061953],[0.815347,2.371016,7.947512,-4.886053,-3.529882,-3.650877,-9.726791,2.985845],[5.600402,-7.441524,5.065598,-0.102723,-0.988838,4.957254,-9.243926,9.542331],[0.162894,8.478077,-1.277514,-0.493535,-8.291757,-9.804343,-2.834133,-9.448356]]], dtype = "float32")#candidate|2870|(2, 15, 8)|const|float32
bop_2871 = relay.power(var_2869.astype('float32'), relay.reshape(const_2870.astype('float32'), relay.shape_of(var_2869))) # shape=(2, 15, 8)
output = bop_2871
output2 = bop_2871
func_2875 = relay.Function([var_2869,], output)
mod['func_2875'] = func_2875
mod = relay.transform.InferType()(mod)
var_2876 = relay.var("var_2876", dtype = "float32", shape = (2, 15, 8))#candidate|2876|(2, 15, 8)|var|float32
output = func_2875(var_2876)
func_2877 = relay.Function([var_2876], output)
mutated_mod['func_2877'] = func_2877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2828_call = mod.get_global_var('func_2828')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_2884 = relay.TupleGetItem(func_2828_call(), 2)
call_2885 = relay.TupleGetItem(func_2829_call(), 2)
func_2033_call = mod.get_global_var('func_2033')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_2887 = relay.TupleGetItem(func_2033_call(), 0)
call_2888 = relay.TupleGetItem(func_2035_call(), 0)
output = relay.Tuple([call_2884,call_2887,])
output2 = relay.Tuple([call_2885,call_2888,])
func_2895 = relay.Function([], output)
mod['func_2895'] = func_2895
mod = relay.transform.InferType()(mod)
output = func_2895()
func_2896 = relay.Function([], output)
mutated_mod['func_2896'] = func_2896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_923_call = mutated_mod.get_global_var('func_923')
call_2911 = func_922_call()
call_2912 = func_922_call()
output = call_2911
output2 = call_2912
func_2916 = relay.Function([], output)
mod['func_2916'] = func_2916
mod = relay.transform.InferType()(mod)
output = func_2916()
func_2917 = relay.Function([], output)
mutated_mod['func_2917'] = func_2917
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2923 = relay.const(8, dtype = "uint64")#candidate|2923|()|const|uint64
var_2924 = relay.var("var_2924", dtype = "uint64", shape = (2, 2, 6))#candidate|2924|(2, 2, 6)|var|uint64
bop_2925 = relay.less_equal(const_2923.astype('bool'), var_2924.astype('bool')) # shape=(2, 2, 6)
uop_2936 = relay.sigmoid(var_2924.astype('float64')) # shape=(2, 2, 6)
output = relay.Tuple([bop_2925,uop_2936,])
output2 = relay.Tuple([bop_2925,uop_2936,])
func_2946 = relay.Function([var_2924,], output)
mod['func_2946'] = func_2946
mod = relay.transform.InferType()(mod)
var_2947 = relay.var("var_2947", dtype = "uint64", shape = (2, 2, 6))#candidate|2947|(2, 2, 6)|var|uint64
output = func_2946(var_2947)
func_2948 = relay.Function([var_2947], output)
mutated_mod['func_2948'] = func_2948
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2957 = relay.var("var_2957", dtype = "uint8", shape = (3, 2, 7))#candidate|2957|(3, 2, 7)|var|uint8
var_2958 = relay.var("var_2958", dtype = "uint8", shape = (3, 2, 7))#candidate|2958|(3, 2, 7)|var|uint8
bop_2959 = relay.less(var_2957.astype('bool'), relay.reshape(var_2958.astype('bool'), relay.shape_of(var_2957))) # shape=(3, 2, 7)
uop_2967 = relay.sqrt(var_2957.astype('float64')) # shape=(3, 2, 7)
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_2975 = relay.TupleGetItem(func_1575_call(), 0)
call_2976 = relay.TupleGetItem(func_1576_call(), 0)
output = relay.Tuple([bop_2959,uop_2967,call_2975,])
output2 = relay.Tuple([bop_2959,uop_2967,call_2976,])
func_2984 = relay.Function([var_2957,var_2958,], output)
mod['func_2984'] = func_2984
mod = relay.transform.InferType()(mod)
mutated_mod['func_2984'] = func_2984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2984_call = mutated_mod.get_global_var('func_2984')
var_2986 = relay.var("var_2986", dtype = "uint8", shape = (3, 2, 7))#candidate|2986|(3, 2, 7)|var|uint8
var_2987 = relay.var("var_2987", dtype = "uint8", shape = (3, 2, 7))#candidate|2987|(3, 2, 7)|var|uint8
call_2985 = func_2984_call(var_2986,var_2987,)
output = call_2985
func_2988 = relay.Function([var_2986,var_2987,], output)
mutated_mod['func_2988'] = func_2988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2048_call = mod.get_global_var('func_2048')
func_2049_call = mutated_mod.get_global_var('func_2049')
call_2993 = func_2048_call()
call_2994 = func_2048_call()
output = call_2993
output2 = call_2994
func_3001 = relay.Function([], output)
mod['func_3001'] = func_3001
mod = relay.transform.InferType()(mod)
output = func_3001()
func_3002 = relay.Function([], output)
mutated_mod['func_3002'] = func_3002
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3065 = relay.var("var_3065", dtype = "int8", shape = (15, 1, 15))#candidate|3065|(15, 1, 15)|var|int8
var_3066 = relay.var("var_3066", dtype = "int8", shape = (15, 12, 15))#candidate|3066|(15, 12, 15)|var|int8
bop_3067 = relay.bitwise_xor(var_3065.astype('int8'), var_3066.astype('int8')) # shape=(15, 12, 15)
uop_3071 = relay.sin(var_3066.astype('float32')) # shape=(15, 12, 15)
func_2291_call = mod.get_global_var('func_2291')
func_2294_call = mutated_mod.get_global_var('func_2294')
var_3074 = relay.var("var_3074", dtype = "bool", shape = (256,))#candidate|3074|(256,)|var|bool
call_3073 = relay.TupleGetItem(func_2291_call(relay.reshape(var_3074.astype('bool'), [16, 8, 2])), 0)
call_3075 = relay.TupleGetItem(func_2294_call(relay.reshape(var_3074.astype('bool'), [16, 8, 2])), 0)
output = relay.Tuple([bop_3067,uop_3071,call_3073,var_3074,])
output2 = relay.Tuple([bop_3067,uop_3071,call_3075,var_3074,])
func_3076 = relay.Function([var_3065,var_3066,var_3074,], output)
mod['func_3076'] = func_3076
mod = relay.transform.InferType()(mod)
mutated_mod['func_3076'] = func_3076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3076_call = mutated_mod.get_global_var('func_3076')
var_3078 = relay.var("var_3078", dtype = "int8", shape = (15, 1, 15))#candidate|3078|(15, 1, 15)|var|int8
var_3079 = relay.var("var_3079", dtype = "int8", shape = (15, 12, 15))#candidate|3079|(15, 12, 15)|var|int8
var_3080 = relay.var("var_3080", dtype = "bool", shape = (256,))#candidate|3080|(256,)|var|bool
call_3077 = func_3076_call(var_3078,var_3079,var_3080,)
output = call_3077
func_3081 = relay.Function([var_3078,var_3079,var_3080,], output)
mutated_mod['func_3081'] = func_3081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1528_call = mod.get_global_var('func_1528')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_3096 = relay.TupleGetItem(func_1528_call(), 0)
call_3097 = relay.TupleGetItem(func_1530_call(), 0)
uop_3098 = relay.atan(call_3096.astype('float64')) # shape=(16, 8, 2)
uop_3100 = relay.atan(call_3097.astype('float64')) # shape=(16, 8, 2)
bop_3102 = relay.logical_and(uop_3098.astype('bool'), relay.reshape(call_3096.astype('bool'), relay.shape_of(uop_3098))) # shape=(16, 8, 2)
bop_3105 = relay.logical_and(uop_3100.astype('bool'), relay.reshape(call_3097.astype('bool'), relay.shape_of(uop_3100))) # shape=(16, 8, 2)
output = bop_3102
output2 = bop_3105
func_3112 = relay.Function([], output)
mod['func_3112'] = func_3112
mod = relay.transform.InferType()(mod)
output = func_3112()
func_3113 = relay.Function([], output)
mutated_mod['func_3113'] = func_3113
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3145 = relay.var("var_3145", dtype = "float64", shape = (9, 10, 2))#candidate|3145|(9, 10, 2)|var|float64
uop_3146 = relay.acos(var_3145.astype('float64')) # shape=(9, 10, 2)
func_1219_call = mod.get_global_var('func_1219')
func_1221_call = mutated_mod.get_global_var('func_1221')
var_3150 = relay.var("var_3150", dtype = "uint32", shape = (1512,))#candidate|3150|(1512,)|var|uint32
call_3149 = relay.TupleGetItem(func_1219_call(relay.reshape(var_3150.astype('uint32'), [14, 12, 9])), 4)
call_3151 = relay.TupleGetItem(func_1221_call(relay.reshape(var_3150.astype('uint32'), [14, 12, 9])), 4)
output = relay.Tuple([uop_3146,call_3149,var_3150,])
output2 = relay.Tuple([uop_3146,call_3151,var_3150,])
func_3156 = relay.Function([var_3145,var_3150,], output)
mod['func_3156'] = func_3156
mod = relay.transform.InferType()(mod)
var_3157 = relay.var("var_3157", dtype = "float64", shape = (9, 10, 2))#candidate|3157|(9, 10, 2)|var|float64
var_3158 = relay.var("var_3158", dtype = "uint32", shape = (1512,))#candidate|3158|(1512,)|var|uint32
output = func_3156(var_3157,var_3158,)
func_3159 = relay.Function([var_3157,var_3158,], output)
mutated_mod['func_3159'] = func_3159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2033_call = mod.get_global_var('func_2033')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_3191 = relay.TupleGetItem(func_2033_call(), 1)
call_3192 = relay.TupleGetItem(func_2035_call(), 1)
func_3156_call = mod.get_global_var('func_3156')
func_3159_call = mutated_mod.get_global_var('func_3159')
const_3204 = relay.const([[-1.245007],[0.912710],[2.903824],[5.775607],[-7.256083],[-8.200504],[-0.504550],[-9.713264],[8.828665],[-2.180342],[-5.053625],[-0.064749],[7.749242],[0.822168],[-6.634004],[-0.706039],[4.330781],[7.090545],[5.525062],[8.195035],[-9.399554],[1.387143],[4.255842],[-7.111244],[-9.380382],[-1.440050],[-5.564083],[-1.234027],[-4.490315],[3.523060],[8.379660],[3.507105],[8.319176],[7.887103],[9.817959],[3.135633],[-0.670615],[7.141328],[-0.964656],[-5.159370],[-0.688007],[-9.298293],[7.216222],[-9.144159],[-6.147637],[3.191575],[7.358382],[9.928647],[1.062543],[-4.857143],[8.030007],[-9.947359],[-1.545454],[1.069379],[-5.080548],[-7.292146],[4.434955],[2.747048],[8.745544],[-3.789987],[7.725642],[8.475309],[2.323720],[0.968394],[5.847828],[1.440748],[2.612684],[-1.868246],[2.450355],[3.135511],[5.200126],[8.738104],[-7.457260],[-9.470777],[-7.681538],[8.166564],[-0.135767],[2.245076],[3.706305],[-2.297627],[-7.353440],[9.620961],[-1.589967],[6.022939],[-3.157405],[6.114249],[-5.502769],[-0.609102],[2.832405],[-7.591517],[2.188643],[7.250008],[-5.317768],[5.822252],[1.885403],[-0.355519],[-5.121802],[-7.172920],[5.124057],[-2.954961],[-9.291731],[-0.985056],[-3.063658],[3.349598],[4.052472],[-8.212074],[6.673946],[-1.930359],[-9.522978],[-5.869936],[0.442784],[9.198083],[-5.299591],[-5.372599],[0.157531],[2.738276],[-6.860233],[2.289404],[-5.511935],[-7.513054],[-2.684579],[0.940411],[-5.277218],[-9.121409],[7.027968],[9.105598],[3.105787],[-5.798974],[-2.718024],[-7.838939],[-6.827480],[7.964582],[2.189283],[8.547731],[7.942591],[7.876720],[-0.066323],[0.303729],[-3.886757],[6.941978],[-9.895964],[-1.420374],[0.385009],[-1.545950],[-0.540225],[-6.591722],[-9.266250],[6.835319],[-1.243611],[-8.461852],[2.336966],[6.435533],[-0.061354],[-3.669771],[-6.409070],[-4.693864],[-2.351906],[9.512056],[-5.487838],[8.849565],[-9.035366],[8.850518],[4.765995],[-4.020192],[5.191663],[7.060708],[-6.844973],[4.914806],[-0.786078],[9.071417],[2.953306],[2.032921],[-6.893348],[-6.787932],[-1.834826],[1.400265],[7.543801],[-1.844285],[-2.399695],[-4.199315]], dtype = "float64")#candidate|3204|(180, 1)|const|float64
const_3205 = relay.const([[4],[6],[-1],[8],[-1],[-8],[-5],[7],[9],[-1],[-8],[5],[-2],[4],[6],[5],[-7],[2],[7],[6],[3],[4],[-2],[1],[8],[6],[-1],[-7],[-4],[1],[4],[10],[8],[-1],[-9],[2],[2],[-1],[8],[8],[6],[-3],[-4],[9],[3],[8],[9],[-1],[9],[1],[-1],[-2],[-10],[9],[-7],[-3],[-2],[-1],[9],[6],[4],[-9],[3],[10],[-4],[-2],[6],[9],[-6],[-4],[-7],[9],[7],[8],[10],[8],[-8],[-6],[9],[-5],[-7],[-9],[8],[8],[10],[1],[1],[9],[-10],[4],[10],[5],[-2],[-1],[7],[5],[2],[4],[6],[5],[4],[-3],[6],[2],[10],[-7],[9],[10],[-10],[-2],[8],[10],[3],[-9],[-6],[5],[2],[6],[2],[3],[6],[-2],[-1],[8],[-5],[8],[-10],[-5],[-2],[4],[-1],[-9],[-6],[1],[3],[-10],[4],[-5],[6],[6],[-6],[7],[5],[-10],[6],[-5],[10],[-10],[-9],[4],[4],[10],[-8],[5],[-10],[7],[7],[1],[8],[9],[3],[3],[-9],[2],[3],[-9],[-2],[7],[8],[5],[-4],[4],[-8],[3],[6],[10],[-7],[-5],[-5],[6],[4],[2],[-6],[9],[-2],[-2],[7],[-8],[-2],[-9],[-5],[8],[-1],[10],[-3],[-3],[-2],[7],[6],[4],[8],[-4],[3],[-10],[-5],[1],[-9],[1],[5],[7],[8],[7],[4],[7],[-7],[10],[6],[-2],[8],[-2],[-2],[-10],[-4],[-4],[-4],[9],[10],[-1],[-7],[6],[9],[1],[10],[6],[5],[10],[3],[-2],[-2],[-9],[7],[6],[1],[6],[6],[-2],[-8],[2],[-6],[7],[-8],[-3],[-6],[9],[-1],[-2],[-6],[8],[8],[5],[-5],[-10],[-2],[4],[-3],[-9],[7],[-4],[-7],[1],[-1],[6],[3],[-5],[9],[-6],[-9],[-9],[9],[6],[6],[2],[9],[6],[-9],[4],[2],[-9],[6],[-8],[4],[-1],[-8],[-1],[-6],[10],[-4],[3],[10],[-9],[-8],[1],[3],[-5],[-6],[5],[-6],[-2],[-7],[-3],[1],[4],[8],[1],[9],[-9],[5],[5],[1],[-8],[-2],[6],[1],[4],[2],[2],[-1],[-1],[4],[-8],[-5],[9],[8],[9],[-5],[-8],[-2],[-7],[-2],[-1],[-8],[-10],[-9],[-9],[4],[-7],[-6],[-9],[2],[6],[7],[-6],[-8],[-1],[6],[7],[-7],[3],[9],[-9],[1],[3],[4],[-2],[10],[-4],[3],[7],[7],[-4],[-2],[-6],[-9],[2],[-5],[10],[-9],[-3],[-5],[-9],[-4],[3],[5],[9],[-5],[-6],[5],[5],[3],[9],[-10],[-3],[-1],[2],[-3],[10],[-4],[-7],[10],[2],[8],[-4],[1],[4],[-7],[-3],[-3],[8],[5],[10],[2],[7],[3],[-6],[9],[-10],[-7],[-1],[-4],[-4],[9],[9],[-6],[-6],[8],[-10],[3],[6],[-1],[-9],[-2],[9],[-5],[-8],[5],[-1],[-1],[-8],[9],[5],[7],[-6],[3],[8],[-4],[-8],[10],[-6],[10],[-4],[-9],[-1],[7],[-5],[-3],[-4],[8],[-3],[-3],[8],[-2],[6],[4],[4],[9],[8],[5],[6],[9],[10],[4],[2],[-5],[-4],[10],[8],[6],[1],[-7],[5],[7],[3],[3],[5],[3],[-5],[1],[-10],[6],[5],[-3],[7],[6],[-3],[-7],[8],[-2],[-5],[10],[-8],[-7],[-1],[-2],[-5],[2],[4],[2],[9],[9],[8],[10],[9],[6],[-6],[6],[-9],[-7],[-3],[9],[7],[7],[-1],[3],[6],[1],[8],[-1],[1],[3],[-4],[-1],[3],[-3],[-7],[6],[8],[-5],[4],[-8],[-2],[4],[10],[8],[-3],[-9],[9],[-9],[-8],[-9],[-9],[-10],[10],[-5],[-5],[-5],[-1],[8],[-4],[-5],[5],[-5],[-5],[-7],[9],[9],[2],[-6],[-7],[7],[5],[9],[-2],[-9],[3],[-5],[-9],[-3],[5],[7],[-5],[-5],[-4],[-9],[1],[2],[-1],[1],[-8],[-10],[-4],[9],[5],[8],[-1],[7],[9],[-3],[10],[-5],[10],[-6],[10],[4],[8],[1],[1],[7],[-2],[-8],[-8],[-9],[7],[-2],[-3],[-10],[4],[-6],[3],[-4],[-4],[-5],[5],[-2],[5],[-9],[5],[9],[-9],[-10],[8],[9],[-6],[-8],[-5],[-2],[-5],[5],[-8],[-6],[7],[5],[-5],[-5],[-5],[-9],[7],[-7],[-3],[3],[-5],[-8],[-3],[10],[-1],[4],[4],[-1],[6],[-3],[5],[6],[-10],[-4],[-5],[-10],[4],[-1],[-10],[-8],[-9],[-9],[4],[2],[-10],[-10],[9],[-4],[6],[1],[-8],[2],[-8],[1],[-5],[-10],[-1],[-9],[-1],[-2],[-10],[-3],[-8],[-9],[8],[6],[10],[8],[-4],[-5],[-7],[-5],[-4],[-3],[9],[-5],[10],[9],[8],[2],[7],[-9],[-9],[-4],[-7],[-2],[-6],[3],[5],[-6],[-3],[-3],[-10],[1],[-10],[3],[5],[4],[-1],[5],[-7],[-2],[-5],[-4],[1],[5],[10],[7],[10],[-9],[2],[-8],[4],[-1],[8],[2],[-4],[-10],[-9],[9],[4],[-2],[-2],[6],[6],[2],[5],[-5],[2],[3],[1],[-9],[2],[-1],[-6],[9],[-4],[4],[-9],[-10],[6],[-2],[-4],[2],[-2],[-7],[-2],[5],[-8],[5],[9],[-1],[4],[-1],[-8],[7],[-2],[6],[6],[3],[-7],[-1],[7],[-3],[4],[-6],[-1],[-8],[-4],[7],[1],[-7],[4],[9],[3],[8],[-2],[-1],[6],[-3],[-1],[5],[-8],[8],[-3],[4],[-10],[7],[6],[4],[9],[1],[2],[2],[5],[10],[6],[9],[-8],[8],[3],[-5],[2],[-5],[-7],[-10],[-10],[10],[1],[1],[7],[4],[-7],[-7],[-10],[-6],[6],[-6],[-3],[-9],[-9],[-9],[-9],[2],[-8],[8],[6],[-9],[2],[8],[3],[-7],[-5],[-9],[3],[1],[10],[10],[6],[1],[-8],[-9],[8],[-5],[-6],[-6],[-9],[7],[-5],[4],[-8],[-9],[-4],[8],[-2],[-4],[-6],[5],[1],[-6],[-5],[3],[5],[-9],[10],[-8],[8],[-7],[-8],[-2],[3],[-3],[7],[3],[-7],[2],[-3],[-7],[-8],[-1],[-8],[5],[8],[-10],[-6],[-9],[6],[-8],[-9],[8],[3],[-2],[-8],[-5],[3],[-5],[4],[-9],[-3],[-9],[9],[7],[-1],[8],[-9],[-9],[-10],[-7],[10],[-5],[7],[-6],[-9],[3],[3],[-10],[-3],[2],[4],[-5],[-8],[-5],[7],[-7],[5],[10],[1],[3],[10],[-1],[-2],[-9],[-9],[-9],[9],[-8],[-10],[5],[7],[4],[1],[2],[-7],[-1],[2],[2],[-4],[9],[10],[-8],[3],[7],[-1],[1],[-2],[7],[-9],[7],[-5],[3],[-10],[-3],[3],[-8],[9],[-5],[-4],[-6],[-3],[-2],[-3],[10],[8],[-8],[-6],[4],[5],[10],[9],[-5],[4],[3],[-10],[-2],[9],[2],[2],[4],[9],[-5],[-4],[-3],[-6],[10],[-9],[-6],[-3],[-2],[9],[10],[7],[-9],[-3],[-9],[6],[9],[2],[-10],[-5],[4],[3],[8],[2],[-3],[-1],[10],[-2],[-4],[-4],[9],[-6],[-2],[2],[-9],[-2],[10],[4],[3],[5],[6],[6],[5],[4],[5],[4],[-10],[4],[-1],[3],[3],[2],[1],[1],[-1],[-10],[6],[4],[6],[-3],[-6],[6],[-9],[7],[9],[1],[-3],[5],[-10],[-8],[5],[-1],[-3],[-4],[-1],[-9],[6],[-4],[-6],[-9],[8],[6],[5],[-7],[-10],[-8],[-2],[7],[2],[-2],[10],[1],[-9],[-3],[5],[-1],[-1],[6],[8],[1],[-8],[-4],[5],[-4],[7],[-3],[1],[5],[8],[-4],[-9],[6],[2],[4],[-7],[10],[3],[4],[9],[9],[5],[-5],[4],[6],[-7],[7],[-5],[-3],[-6],[9],[-3],[9],[-4],[6],[-2],[-1],[6],[3],[3],[4],[-10],[-5],[-3],[-4],[-9],[-4],[-1],[-10],[5],[-8],[2],[-4],[-5],[-8],[8],[10],[2],[-5],[-4],[-6],[1],[7],[3],[4],[-3],[5],[-4],[-4],[5],[1],[4],[3],[7],[-1],[-8],[-5],[-8],[-10],[-10],[-9],[9],[-10],[2],[-5],[-6],[2],[6],[-3],[5],[5],[2],[-4],[-10],[1],[1],[3],[-3],[-4],[-7],[-2],[5],[-2],[-9],[-3],[3],[-2],[8],[5],[-10],[-8],[-8],[2],[5],[6],[5],[6],[2],[-1],[7],[7],[-2],[6],[7],[-9],[-10],[10],[9],[-9],[8],[-8],[-1],[-2],[-6],[-6],[-9],[-4],[-4],[-2],[-2],[9],[-8],[-7],[-1],[-5],[2],[-1],[-10],[8],[10],[-3],[-8],[9],[-7],[-2],[3],[-10],[10],[-10],[-6],[1],[10],[10],[7],[-8],[-1],[5],[7],[-1],[6],[-3],[9],[-10],[3],[-2],[-6],[-6],[5],[6],[4],[-8],[-4],[6],[8],[6],[-5],[2],[4],[-2],[3],[3],[-5],[6],[5],[-1],[-6],[5],[3],[-5],[-1],[4],[2],[7],[-8],[-1],[3],[10],[3],[7],[8],[8],[-8],[-7],[-6],[-1],[-3],[-2],[-2],[9],[10],[-3],[-5],[10],[-1],[-7],[-6],[4],[-10],[6],[-5],[-1],[-3],[-3],[2],[7],[1],[-6],[4],[-4],[4],[3],[-6],[5],[-2],[-2],[-9],[3],[-5],[-8],[-8],[2],[6],[-8],[3],[-5],[-3],[10],[-9],[-7],[-5],[6],[-1],[-7],[7],[5],[10],[-9],[-5],[-9],[6],[7],[4],[1],[4],[4],[7],[5],[-1],[6],[8],[7],[1],[6],[-10],[-6],[9],[-8],[-3],[-6],[-8],[-6],[10],[-5],[-4],[1],[6],[-9],[4],[5],[-10],[-10],[6],[-4],[4],[-6],[10],[-7],[3],[-3],[7],[-8],[2],[10],[-5],[-9],[5],[6],[5],[10],[9],[4],[-8],[-10],[-5],[8],[7],[-4],[3],[6],[-8],[5],[-2],[5],[-2],[-7],[-1],[-2],[3],[9],[-7],[9],[3],[4],[5],[6],[-4],[-7],[3],[-6],[-10],[-7],[5],[1],[-3],[4],[-9],[3],[-6],[10],[8],[-7],[10],[-9],[-9],[-9],[7],[10],[-5],[-9],[-3],[-8],[8],[4],[8],[-7],[3],[-7],[1],[5],[2],[-9],[-2],[-2],[-9],[-5],[4],[3],[-5],[-5],[-5],[7],[8],[1],[3],[-7]], dtype = "uint32")#candidate|3205|(1512, 1)|const|uint32
call_3203 = relay.TupleGetItem(func_3156_call(relay.reshape(const_3204.astype('float64'), [9, 10, 2]), relay.reshape(const_3205.astype('uint32'), [1512,]), ), 1)
call_3206 = relay.TupleGetItem(func_3159_call(relay.reshape(const_3204.astype('float64'), [9, 10, 2]), relay.reshape(const_3205.astype('uint32'), [1512,]), ), 1)
output = relay.Tuple([call_3191,call_3203,const_3204,const_3205,])
output2 = relay.Tuple([call_3192,call_3206,const_3204,const_3205,])
func_3214 = relay.Function([], output)
mod['func_3214'] = func_3214
mod = relay.transform.InferType()(mod)
mutated_mod['func_3214'] = func_3214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3214_call = mutated_mod.get_global_var('func_3214')
call_3215 = func_3214_call()
output = call_3215
func_3216 = relay.Function([], output)
mutated_mod['func_3216'] = func_3216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_3259 = func_1354_call()
call_3260 = func_1354_call()
output = call_3259
output2 = call_3260
func_3282 = relay.Function([], output)
mod['func_3282'] = func_3282
mod = relay.transform.InferType()(mod)
output = func_3282()
func_3283 = relay.Function([], output)
mutated_mod['func_3283'] = func_3283
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3315 = relay.var("var_3315", dtype = "float32", shape = (7, 1, 12))#candidate|3315|(7, 1, 12)|var|float32
uop_3316 = relay.log10(var_3315.astype('float32')) # shape=(7, 1, 12)
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_3335 = func_1354_call()
call_3336 = func_1354_call()
output = relay.Tuple([uop_3316,call_3335,])
output2 = relay.Tuple([uop_3316,call_3336,])
func_3340 = relay.Function([var_3315,], output)
mod['func_3340'] = func_3340
mod = relay.transform.InferType()(mod)
var_3341 = relay.var("var_3341", dtype = "float32", shape = (7, 1, 12))#candidate|3341|(7, 1, 12)|var|float32
output = func_3340(var_3341)
func_3342 = relay.Function([var_3341], output)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3112_call = mod.get_global_var('func_3112')
func_3113_call = mutated_mod.get_global_var('func_3113')
call_3364 = func_3112_call()
call_3365 = func_3112_call()
func_2406_call = mod.get_global_var('func_2406')
func_2407_call = mutated_mod.get_global_var('func_2407')
call_3370 = relay.TupleGetItem(func_2406_call(), 2)
call_3371 = relay.TupleGetItem(func_2407_call(), 2)
func_2916_call = mod.get_global_var('func_2916')
func_2917_call = mutated_mod.get_global_var('func_2917')
call_3385 = func_2916_call()
call_3386 = func_2916_call()
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
const_3390 = relay.const([7.207579,4.857093,1.207321,-4.170742,6.318777,-2.148028,5.630645,4.992407,-9.869450,-9.759805,7.114647,8.644532,-8.664333,-9.126059,-5.253834,4.140703,8.542084,-3.617434,1.794861,4.440660,0.933661,5.174411,0.089466,5.643142,9.794226,4.161997,0.629995,-5.254287,8.887783,-1.945540,-8.249391,-9.472915,-3.851942,-1.028471,3.005415,-4.780488,3.385184,-8.317058,4.586864,-7.973856,1.899049,9.459774,7.187790,2.031849,-6.266569,-3.079374,8.700445,5.922547,7.270359,-8.942417,9.192970,0.487223,-2.638455,9.071239,1.333119,3.706448,8.118254,-4.603258,-2.475956,4.474069,7.713978,8.259014,-9.334128,-2.358439,-8.885419,0.525693,2.209604,9.617821,-1.505022,8.440665,-7.659292,-4.025289,-0.501286,-4.816915,-6.838384,0.010026,-5.376812,1.719339,0.784673,-0.434318,-0.794832,0.724783,8.598540,0.729956,2.264042,9.360358,7.534319,3.957835,-4.443895,-8.254182,-3.078962,-4.819079,-4.853700,8.190227,5.622306,-5.664240,6.376686,-8.576991,-3.139624,-1.482605,-4.467703,7.709305,-4.260494,2.175697,9.137116,6.986090,-9.692709,-3.806613,4.632955,-4.173347,3.347464,-4.958870,7.495885,1.001875,4.909158,5.319285,-1.010309,8.286043,-0.592969,9.609325,3.143054,2.927812,2.946382,-8.485389,9.109128,5.313971,5.581616,-3.448871,-9.708291,-2.224498,9.442309,-9.281666,8.212089,-6.702468,-1.146641,0.219625,4.706003,5.931583,-6.194799,1.721265,4.159502,-0.814623,9.819096,5.754189,6.150688,1.261199,5.776734,-6.302049,8.324367,-7.703869,-3.183785,2.130961,-6.263618,-2.048580,2.602986,9.845958,2.782618,2.353037,-3.595905,-0.499090,1.384007,-5.419966,5.257877,7.801313,-2.861329,7.607930,1.910143,-0.815692,7.609399,-0.144757,-1.670899,0.341069,1.347146,-3.027610,8.947068,3.432557,-5.378772,-3.878488,-9.262308,5.286456,0.369301,-1.433522,1.606643,8.330343,2.368232,2.519238,2.973688,9.749851,-6.593856,-5.853989,9.812765,-9.543468,6.088925,0.028016,-6.051304,-5.815295,4.684321,-6.800524,3.711239,-9.308197,1.372654,9.454414,-0.713178,1.639048,-8.456646,0.660672,-8.441654,-5.972089,-4.984813,5.060057,-4.180094,-1.035267,-0.588008,-4.928193,-4.768506,2.684083,4.105570,-1.733380,4.991291,-5.629413,4.422670,8.633576,8.335308,-9.601444,-0.016528,-6.649573,9.567067,-2.294245,7.300062,-5.344939,4.271181,5.277940,-4.509005,0.957009,9.992164,1.216296,3.753437,-4.955217,-1.944821,-6.591109,9.507012,5.675565,0.627284,-3.456858,9.258606,8.716463,-5.435610,5.995272,-2.584452,5.785505,-3.633746,4.756783,8.715591,-1.368583,-2.527197,-8.888583,2.887938,-6.314557,-5.097361,0.230022,0.014227,-6.540943,6.677613,-1.359918,-8.627523,9.148508,4.591437,-8.019865,6.768932,-5.108766,8.172149,6.264351,9.000572,-6.521027,-6.728620,8.765694,-3.192871,-7.274465,4.368214,9.164614,-1.619817,-6.116731,9.861930,-5.052248,7.790459,-4.433808,-7.504999,3.058075,-0.788206,5.760385,6.628446,-9.872284,-0.389506,1.714014,-4.580859,-4.779021,5.673089,-7.611094,7.074974,2.569910,1.136815,-5.594052,9.111030,0.235532,1.207357,8.924924,1.150253,-8.795526,-4.849451,2.448272,-0.777515,0.621050,-6.086244,8.692472,-5.155281,-3.879661,-7.183402,7.450863,-6.243474,7.681749,3.977936,-0.078774,8.846664,6.269619,-8.346333,-4.118455,-3.255999,5.875931,2.955315,-3.627373,3.423306,8.912271,0.868359,-8.779723,-3.960266,9.664149,-4.515127,-9.879689,-2.177470,0.108691,0.998041,-3.149409,0.711913,-6.888153,-1.234950,-9.059943,-7.407745,6.722718,6.464242,1.160777,-9.049276,1.519077,9.001902,-2.553208,0.195697,-2.771786,8.105335,-9.663151,-2.591335,2.820646,-5.209344,4.756312,6.207829,-0.646294,-8.578090,-2.584267,9.176418,6.692445,-9.586610,-6.070941,5.233754,-5.172233,5.090681,7.136330,7.773081,-6.034559,-3.254359,-1.270189,7.383161,-0.972344,2.462510,-2.528110,8.877632,1.988841,5.971660,6.683871,-8.909757,6.243456,3.479876,-4.999988,9.861442,-7.253790,-5.794286,8.131968,8.502659,9.325395,5.193042,8.070530,9.042954,-4.339337,7.096487,3.536093,1.203696,6.871307,2.724605], dtype = "float32")#candidate|3390|(405,)|const|float32
call_3389 = relay.TupleGetItem(func_555_call(relay.reshape(const_3390.astype('float32'), [405,])), 1)
call_3391 = relay.TupleGetItem(func_558_call(relay.reshape(const_3390.astype('float32'), [405,])), 1)
uop_3395 = relay.rsqrt(const_3390.astype('float64')) # shape=(405,)
uop_3397 = relay.atanh(uop_3395.astype('float32')) # shape=(405,)
output = relay.Tuple([call_3364,call_3370,call_3385,call_3389,uop_3397,])
output2 = relay.Tuple([call_3365,call_3371,call_3386,call_3391,uop_3397,])
func_3406 = relay.Function([], output)
mod['func_3406'] = func_3406
mod = relay.transform.InferType()(mod)
mutated_mod['func_3406'] = func_3406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3406_call = mutated_mod.get_global_var('func_3406')
call_3407 = func_3406_call()
output = call_3407
func_3408 = relay.Function([], output)
mutated_mod['func_3408'] = func_3408
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3446 = relay.var("var_3446", dtype = "float64", shape = (9, 6, 10))#candidate|3446|(9, 6, 10)|var|float64
uop_3447 = relay.sinh(var_3446.astype('float64')) # shape=(9, 6, 10)
output = uop_3447
output2 = uop_3447
func_3451 = relay.Function([var_3446,], output)
mod['func_3451'] = func_3451
mod = relay.transform.InferType()(mod)
var_3452 = relay.var("var_3452", dtype = "float64", shape = (9, 6, 10))#candidate|3452|(9, 6, 10)|var|float64
output = func_3451(var_3452)
func_3453 = relay.Function([var_3452], output)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_923_call = mutated_mod.get_global_var('func_923')
call_3473 = func_922_call()
call_3474 = func_922_call()
func_1915_call = mod.get_global_var('func_1915')
func_1917_call = mutated_mod.get_global_var('func_1917')
call_3475 = relay.TupleGetItem(func_1915_call(), 0)
call_3476 = relay.TupleGetItem(func_1917_call(), 0)
output = relay.Tuple([call_3473,call_3475,])
output2 = relay.Tuple([call_3474,call_3476,])
func_3478 = relay.Function([], output)
mod['func_3478'] = func_3478
mod = relay.transform.InferType()(mod)
mutated_mod['func_3478'] = func_3478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3478_call = mutated_mod.get_global_var('func_3478')
call_3479 = func_3478_call()
output = call_3479
func_3480 = relay.Function([], output)
mutated_mod['func_3480'] = func_3480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3001_call = mod.get_global_var('func_3001')
func_3002_call = mutated_mod.get_global_var('func_3002')
call_3483 = func_3001_call()
call_3484 = func_3001_call()
var_3491 = relay.var("var_3491", dtype = "bool", shape = (16, 8, 2))#candidate|3491|(16, 8, 2)|var|bool
bop_3492 = relay.equal(call_3483.astype('bool'), relay.reshape(var_3491.astype('bool'), relay.shape_of(call_3483))) # shape=(16, 8, 2)
bop_3495 = relay.equal(call_3484.astype('bool'), relay.reshape(var_3491.astype('bool'), relay.shape_of(call_3484))) # shape=(16, 8, 2)
output = relay.Tuple([bop_3492,])
output2 = relay.Tuple([bop_3495,])
func_3503 = relay.Function([var_3491,], output)
mod['func_3503'] = func_3503
mod = relay.transform.InferType()(mod)
var_3504 = relay.var("var_3504", dtype = "bool", shape = (16, 8, 2))#candidate|3504|(16, 8, 2)|var|bool
output = func_3503(var_3504)
func_3505 = relay.Function([var_3504], output)
mutated_mod['func_3505'] = func_3505
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3594 = relay.const([[[2.148789,0.287825,-9.523837,0.770844,5.466099,3.102478,-9.357329,2.975217,8.404131],[-0.735156,-3.746162,2.481247,-3.910339,-4.745813,5.233323,8.212272,-9.368931,-7.484897],[-1.738174,-2.750274,0.561816,3.260393,-4.346378,4.836332,9.046630,-7.233456,-1.943023],[-1.727722,4.740770,-2.014781,2.441909,3.649196,7.895154,-7.183011,-9.402234,2.897609],[6.064944,4.810619,4.993880,0.566715,-4.755791,3.751758,9.383343,-8.811189,-3.123876],[6.030901,-1.321660,-8.887526,-2.654189,-6.526459,2.787244,-6.632443,-7.000717,5.328307],[-4.406404,-2.837390,-6.049842,-6.651652,-9.725902,7.628044,1.996696,-9.809421,2.307331],[4.399321,7.858730,-1.450954,7.309563,2.432214,0.098436,-7.183207,-4.465392,-4.433219],[-9.280770,-0.406520,9.626877,9.368843,7.547458,6.770222,-6.834692,-6.456332,-4.143505],[9.742956,-2.644151,7.007175,9.721537,1.305790,8.267447,-5.307238,-5.428931,-8.389205],[-8.787928,8.331917,3.504074,4.514046,0.474856,0.946995,-3.859700,-9.710466,-5.998478],[-8.976789,3.969705,1.537401,-9.394857,-7.774336,-8.188023,-1.083272,-8.198273,-1.787314]],[[-5.228947,-4.828884,-3.493862,7.773193,-6.402185,1.800674,-1.086445,-0.418843,2.495357],[-0.723583,5.814523,7.483565,2.033414,3.025328,1.640973,3.197185,0.074565,8.923847],[7.238110,-7.970452,-6.860986,-1.896110,-3.833453,-9.040318,-5.185368,9.600412,1.987191],[-4.217737,-7.713030,1.521158,7.243268,-6.663731,-8.643913,-7.376406,-6.131103,0.837774],[-8.787316,6.060707,-9.794188,8.936427,-0.635135,-8.618255,5.940764,-3.814206,-2.118447],[8.993746,-5.252307,-8.675171,6.292876,2.870095,-8.517783,8.739286,-0.275429,9.777120],[-3.915179,-3.428798,3.904525,4.242712,9.256881,-1.322374,1.497009,7.058651,2.327076],[-6.359809,5.416340,8.216152,-1.431525,-8.339954,9.107263,0.125498,-0.259584,2.140420],[-8.503475,-2.322264,-0.623466,-3.829783,-9.763880,-3.577357,2.327625,8.661374,-8.410773],[-8.411751,8.852878,7.221729,-5.445477,-5.856834,-7.255083,-2.816470,-6.922856,-1.109606],[-8.049140,-0.397992,5.432910,-6.653541,5.525842,3.871287,-6.883934,-7.916344,-2.407387],[7.918634,-5.522021,-5.304481,5.247571,-7.694360,2.998605,-7.333766,8.339987,6.550568]],[[7.309050,7.324260,2.900482,-2.311681,6.739675,0.936819,9.771902,-5.663638,-8.060071],[-6.726137,-1.166785,-8.975881,-4.174307,2.868627,9.309922,-5.166132,-6.370863,-3.037468],[-1.048302,-5.551083,8.842867,7.601095,-5.800763,4.050435,-1.859522,-0.593778,-1.381213],[2.622961,8.181475,-6.895037,8.747371,-3.171587,-0.822541,2.760264,7.448537,-7.529653],[1.538057,0.732893,-1.673523,-4.925566,8.289775,9.961645,4.420191,-7.754380,1.704907],[-4.413539,0.531813,-1.406058,1.287698,-1.612637,0.939739,0.684907,-7.922248,-1.777274],[5.205225,-4.464111,7.806981,-5.058904,-6.892937,-3.564879,9.011688,-3.700280,8.276909],[4.123785,-7.549231,0.208488,-6.995900,-6.465857,-9.220020,9.332226,6.080016,-9.136337],[2.020564,-6.516070,1.800587,8.769338,7.364140,2.939447,7.278592,3.196903,-1.971671],[7.113493,2.383822,2.627821,8.651876,-2.146811,-8.863487,4.749653,0.786078,6.489202],[-4.308964,-8.730928,-6.133868,-0.279914,-7.396326,0.926565,4.994309,4.425785,-1.375097],[-1.562627,-7.705060,6.455445,4.755863,-3.237664,-8.860824,9.621091,4.491566,-5.161813]],[[2.227787,6.123183,-3.333422,-6.037156,9.282350,-3.506920,-8.136300,1.114135,7.650503],[-1.009520,-4.513477,-0.139266,-1.132749,8.063302,0.704409,-1.107499,9.133896,-3.578547],[-3.124127,3.615493,-5.219165,-6.645176,-1.007525,7.563672,-5.530760,-7.332966,8.702386],[8.268932,-2.111989,0.271222,-5.921949,-6.880887,1.807053,9.749697,3.732646,8.122292],[-3.602250,-0.700126,-8.648406,4.126002,3.285981,9.581066,-6.972156,6.907488,3.598814],[-8.748156,-9.603392,8.275132,1.453896,7.834514,8.779989,-0.306643,-1.478955,-4.681075],[4.861292,2.145679,7.240440,5.248268,7.143481,-9.143045,2.530386,-0.217592,2.878834],[3.146902,-7.983600,3.330695,1.082105,-4.876224,4.474027,-7.600620,-5.954043,4.136449],[-3.922820,4.176870,7.475383,5.690796,-4.725819,-5.833875,8.810189,-4.928850,0.890848],[-6.068556,9.765509,-9.650823,4.119348,7.264879,3.623534,-5.386937,0.064190,8.674568],[0.708930,8.006849,1.093957,-1.727021,3.922475,-2.133771,-8.184980,-2.766162,7.115257],[-2.549642,2.778871,-4.285931,1.293718,0.174624,-8.246445,8.612964,8.923771,1.194986]]], dtype = "float64")#candidate|3594|(4, 12, 9)|const|float64
var_3595 = relay.var("var_3595", dtype = "float64", shape = (4, 12, 9))#candidate|3595|(4, 12, 9)|var|float64
bop_3596 = relay.multiply(const_3594.astype('float64'), relay.reshape(var_3595.astype('float64'), relay.shape_of(const_3594))) # shape=(4, 12, 9)
func_897_call = mod.get_global_var('func_897')
func_900_call = mutated_mod.get_global_var('func_900')
var_3607 = relay.var("var_3607", dtype = "uint8", shape = (144, 1))#candidate|3607|(144, 1)|var|uint8
call_3606 = relay.TupleGetItem(func_897_call(relay.reshape(var_3607.astype('uint8'), [9, 8, 2])), 3)
call_3608 = relay.TupleGetItem(func_900_call(relay.reshape(var_3607.astype('uint8'), [9, 8, 2])), 3)
output = relay.Tuple([bop_3596,call_3606,var_3607,])
output2 = relay.Tuple([bop_3596,call_3608,var_3607,])
func_3611 = relay.Function([var_3595,var_3607,], output)
mod['func_3611'] = func_3611
mod = relay.transform.InferType()(mod)
var_3612 = relay.var("var_3612", dtype = "float64", shape = (4, 12, 9))#candidate|3612|(4, 12, 9)|var|float64
var_3613 = relay.var("var_3613", dtype = "uint8", shape = (144, 1))#candidate|3613|(144, 1)|var|uint8
output = func_3611(var_3612,var_3613,)
func_3614 = relay.Function([var_3612,var_3613,], output)
mutated_mod['func_3614'] = func_3614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_3633 = func_1592_call()
call_3634 = func_1592_call()
output = call_3633
output2 = call_3634
func_3643 = relay.Function([], output)
mod['func_3643'] = func_3643
mod = relay.transform.InferType()(mod)
output = func_3643()
func_3644 = relay.Function([], output)
mutated_mod['func_3644'] = func_3644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3214_call = mod.get_global_var('func_3214')
func_3216_call = mutated_mod.get_global_var('func_3216')
call_3658 = relay.TupleGetItem(func_3214_call(), 1)
call_3659 = relay.TupleGetItem(func_3216_call(), 1)
output = relay.Tuple([call_3658,])
output2 = relay.Tuple([call_3659,])
func_3660 = relay.Function([], output)
mod['func_3660'] = func_3660
mod = relay.transform.InferType()(mod)
mutated_mod['func_3660'] = func_3660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3660_call = mutated_mod.get_global_var('func_3660')
call_3661 = func_3660_call()
output = call_3661
func_3662 = relay.Function([], output)
mutated_mod['func_3662'] = func_3662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1915_call = mod.get_global_var('func_1915')
func_1917_call = mutated_mod.get_global_var('func_1917')
call_3693 = relay.TupleGetItem(func_1915_call(), 0)
call_3694 = relay.TupleGetItem(func_1917_call(), 0)
func_2916_call = mod.get_global_var('func_2916')
func_2917_call = mutated_mod.get_global_var('func_2917')
call_3729 = func_2916_call()
call_3730 = func_2916_call()
const_3733 = relay.const([[[True,False],[True,False],[True,True],[True,False],[False,True],[False,False],[False,True],[False,False]],[[True,False],[True,False],[True,True],[True,True],[False,False],[True,True],[False,False],[True,False]],[[False,False],[False,False],[True,True],[False,False],[False,False],[False,False],[True,True],[True,False]],[[True,False],[True,False],[False,False],[True,False],[False,False],[True,True],[False,True],[True,True]],[[True,True],[True,True],[False,True],[True,False],[True,True],[False,False],[False,True],[True,False]],[[False,False],[False,False],[False,False],[False,False],[False,False],[True,True],[True,False],[False,False]],[[True,True],[True,True],[False,False],[True,True],[False,False],[True,False],[True,False],[False,True]],[[False,True],[True,False],[True,False],[True,True],[False,False],[False,True],[True,False],[True,False]],[[True,True],[False,True],[True,True],[False,True],[True,False],[False,True],[False,False],[False,True]],[[True,False],[True,False],[False,False],[False,False],[True,False],[True,False],[True,False],[False,False]],[[True,False],[False,True],[False,False],[False,True],[False,False],[False,True],[True,True],[False,False]],[[True,True],[True,True],[False,True],[True,True],[True,False],[True,False],[False,True],[True,False]],[[False,True],[True,False],[True,True],[True,False],[False,False],[True,True],[True,True],[True,False]],[[False,False],[True,False],[True,False],[True,True],[False,False],[True,False],[False,False],[False,False]],[[True,True],[False,True],[True,True],[True,True],[True,False],[False,False],[True,True],[False,True]],[[False,True],[False,True],[True,True],[False,True],[False,False],[False,False],[False,False],[False,False]]], dtype = "bool")#candidate|3733|(16, 8, 2)|const|bool
bop_3734 = relay.not_equal(call_3693.astype('bool'), relay.reshape(const_3733.astype('bool'), relay.shape_of(call_3693))) # shape=(16, 8, 2)
bop_3737 = relay.not_equal(call_3694.astype('bool'), relay.reshape(const_3733.astype('bool'), relay.shape_of(call_3694))) # shape=(16, 8, 2)
func_1725_call = mod.get_global_var('func_1725')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_3742 = relay.TupleGetItem(func_1725_call(), 4)
call_3743 = relay.TupleGetItem(func_1727_call(), 4)
bop_3749 = relay.floor_mod(call_3693.astype('float32'), relay.reshape(const_3733.astype('float32'), relay.shape_of(call_3693))) # shape=(16, 8, 2)
bop_3752 = relay.floor_mod(call_3694.astype('float32'), relay.reshape(const_3733.astype('float32'), relay.shape_of(call_3694))) # shape=(16, 8, 2)
bop_3753 = relay.less_equal(call_3693.astype('bool'), relay.reshape(call_3742.astype('bool'), relay.shape_of(call_3693))) # shape=(16, 8, 2)
bop_3756 = relay.less_equal(call_3694.astype('bool'), relay.reshape(call_3743.astype('bool'), relay.shape_of(call_3694))) # shape=(16, 8, 2)
func_2542_call = mod.get_global_var('func_2542')
func_2544_call = mutated_mod.get_global_var('func_2544')
const_3763 = relay.const([[9.702908,9.140003,5.405705,2.753204,7.373229,7.044571,-2.552110,-8.717743,9.560806,6.126280,-2.021214,-7.680885,6.841559,-8.095703,3.672922,2.137252,-6.348455,0.142756]], dtype = "float32")#candidate|3763|(1, 18)|const|float32
call_3762 = relay.TupleGetItem(func_2542_call(relay.reshape(const_3763.astype('float32'), [6, 3, 1])), 0)
call_3764 = relay.TupleGetItem(func_2544_call(relay.reshape(const_3763.astype('float32'), [6, 3, 1])), 0)
output = relay.Tuple([call_3729,bop_3734,bop_3749,bop_3753,call_3762,const_3763,])
output2 = relay.Tuple([call_3730,bop_3737,bop_3752,bop_3756,call_3764,const_3763,])
func_3765 = relay.Function([], output)
mod['func_3765'] = func_3765
mod = relay.transform.InferType()(mod)
output = func_3765()
func_3766 = relay.Function([], output)
mutated_mod['func_3766'] = func_3766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3478_call = mod.get_global_var('func_3478')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_3797 = relay.TupleGetItem(func_3478_call(), 0)
call_3798 = relay.TupleGetItem(func_3480_call(), 0)
output = call_3797
output2 = call_3798
func_3808 = relay.Function([], output)
mod['func_3808'] = func_3808
mod = relay.transform.InferType()(mod)
output = func_3808()
func_3809 = relay.Function([], output)
mutated_mod['func_3809'] = func_3809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3849 = relay.var("var_3849", dtype = "int32", shape = (4, 2, 5))#candidate|3849|(4, 2, 5)|var|int32
var_3850 = relay.var("var_3850", dtype = "int32", shape = (4, 2, 5))#candidate|3850|(4, 2, 5)|var|int32
bop_3851 = relay.minimum(var_3849.astype('int32'), relay.reshape(var_3850.astype('int32'), relay.shape_of(var_3849))) # shape=(4, 2, 5)
bop_3855 = relay.greater_equal(bop_3851.astype('bool'), relay.reshape(var_3849.astype('bool'), relay.shape_of(bop_3851))) # shape=(4, 2, 5)
func_1725_call = mod.get_global_var('func_1725')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_3863 = relay.TupleGetItem(func_1725_call(), 1)
call_3864 = relay.TupleGetItem(func_1727_call(), 1)
output = relay.Tuple([bop_3855,call_3863,])
output2 = relay.Tuple([bop_3855,call_3864,])
func_3867 = relay.Function([var_3849,var_3850,], output)
mod['func_3867'] = func_3867
mod = relay.transform.InferType()(mod)
mutated_mod['func_3867'] = func_3867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3867_call = mutated_mod.get_global_var('func_3867')
var_3869 = relay.var("var_3869", dtype = "int32", shape = (4, 2, 5))#candidate|3869|(4, 2, 5)|var|int32
var_3870 = relay.var("var_3870", dtype = "int32", shape = (4, 2, 5))#candidate|3870|(4, 2, 5)|var|int32
call_3868 = func_3867_call(var_3869,var_3870,)
output = call_3868
func_3871 = relay.Function([var_3869,var_3870,], output)
mutated_mod['func_3871'] = func_3871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3406_call = mod.get_global_var('func_3406')
func_3408_call = mutated_mod.get_global_var('func_3408')
call_3884 = relay.TupleGetItem(func_3406_call(), 0)
call_3885 = relay.TupleGetItem(func_3408_call(), 0)
uop_3899 = relay.log2(call_3884.astype('float64')) # shape=(16, 8, 2)
uop_3901 = relay.log2(call_3885.astype('float64')) # shape=(16, 8, 2)
output = uop_3899
output2 = uop_3901
func_3910 = relay.Function([], output)
mod['func_3910'] = func_3910
mod = relay.transform.InferType()(mod)
output = func_3910()
func_3911 = relay.Function([], output)
mutated_mod['func_3911'] = func_3911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2828_call = mod.get_global_var('func_2828')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_3917 = relay.TupleGetItem(func_2828_call(), 2)
call_3918 = relay.TupleGetItem(func_2829_call(), 2)
output = call_3917
output2 = call_3918
func_3927 = relay.Function([], output)
mod['func_3927'] = func_3927
mod = relay.transform.InferType()(mod)
mutated_mod['func_3927'] = func_3927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3927_call = mutated_mod.get_global_var('func_3927')
call_3928 = func_3927_call()
output = call_3928
func_3929 = relay.Function([], output)
mutated_mod['func_3929'] = func_3929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_3948 = func_1592_call()
call_3949 = func_1592_call()
func_3112_call = mod.get_global_var('func_3112')
func_3113_call = mutated_mod.get_global_var('func_3113')
call_3953 = func_3112_call()
call_3954 = func_3112_call()
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
const_3961 = relay.const([3.377566,-5.231931,4.944569,9.918447,-1.932579,-4.339831,-1.843206,0.465142,8.653323,-5.591623,8.382942,5.121591,-7.502991,-0.198006,9.375636,1.085735,-1.033466,-9.895439,-4.392962,-0.172377,-0.054855,8.204035,2.893015,0.603845,-5.718727,-4.632353,-4.800379,-8.462685,0.436645,-2.117633,-6.528347,9.911305,3.954620,-5.930259,8.536774,-1.764577,3.674046,8.409382,-4.959628,9.140436,-8.753984,-8.563955,2.931043,3.273725,-6.581574,1.907560,7.406274,1.735778,0.987715,1.189757,3.516634,-8.191983,2.386608,0.592770,-8.632983,-5.348385,-1.480159,-0.925948,2.299531,-9.633829,3.968925,9.954185,-7.265216,-7.469233,-7.471650,9.236885,1.973813,8.146792,7.880856,2.129724,5.706947,-9.966409,-3.506021,-4.866875,-9.341660,2.349542,-4.396202,-3.142874,-0.970117,-7.653098,-3.810938,-8.920560,-4.970192,-0.358837,-4.457494,9.923666,-9.718723,-2.646643,-4.907607,-7.762920,4.889190,4.465157,-2.834788,0.391922,-6.054868,-8.231184,2.040960,-4.155052,-3.338027,0.929711,-8.908331,-3.867302,-8.242368,-6.389096,6.766900,8.153702,-8.959638,9.116597,-9.946375,5.016838,-4.496701,-8.964831,-4.559393,5.797686,4.369296,-6.344868,-4.086928,-6.264563,5.034732,0.255135,-0.712818,6.959006,6.259046,7.519797,7.269930,-6.775270,-4.298251,6.906938,-8.406817,7.519447,0.726637,7.898244,6.156037,-7.015086,-6.340289,5.679509,-4.642901,-4.803249,7.508228,-4.305060,-7.246759,0.079837,6.134412,-9.205365,4.080373,9.547449,9.882788,-7.399356,8.487177,2.607078,9.296879,-7.037946,8.842590,9.482859,-4.725026,-3.008999,2.810474,-2.536371,-2.307094,-4.334132,-9.912869,7.839376,-9.932895,-9.107943,-5.222270,-9.117005,0.353789,-3.103948,7.987309,6.036098,7.374901,-7.731028,9.376537,6.901064,9.447108,-9.730082,2.502123,1.643279,3.567056,7.461866,5.010501,4.700680,-2.555501,-1.004322,-9.555243,-2.465866,8.088771,-6.838986,5.698762,-9.204163,6.097674,-1.488666,-6.178442,-4.203860,-2.169895,-0.058220,0.080078,-8.540261,4.742236,0.926309,-9.806783,7.592134,4.640594,7.624073,7.625518,5.740824,-5.053331,9.432263,-2.186885,-7.075843,-4.178967,-3.081921,1.574050,6.420786,6.590650,-6.908059,-3.060876,8.160416,4.030633,-6.063612,6.064146,3.490996,-2.446811,-8.728213,-1.336322,5.231950,6.312675,5.535050,-2.104565,6.013324,5.390268,7.392651,4.697416,8.566389,7.997153,4.607601,-6.269037,-1.508848,-8.757319,0.623216,-5.205515,5.841348,-5.116117,-6.122994,2.312634,0.904667,8.096454,8.689892,4.130393,8.107664,-0.578575,4.867037,8.058666,3.979389,3.873191,-0.086384,9.857549,8.008755,-6.108248,-3.342920,-2.802997,2.026177,4.379022,-1.249350,4.103143,3.715511,7.413135,-7.124637,9.984735,-9.062676,-6.421446,-0.109048,-7.660549,-1.286254,7.920203,-9.687050,-5.036783,2.815807,-5.309043,-4.021942,5.057309,-4.268615,4.204028,0.379173,-2.071893,6.167694,-0.231208,1.104222,4.034016,-4.952290,-2.119817,-9.912938,-5.069544,-3.197837,-7.324035,-8.264463,9.665624,-0.297850,-7.138687,9.320906,4.292760,2.348748,-8.626145,-7.171615,-6.005642,-5.569175,2.508486,6.953837,-4.601907,0.405262,5.671367,-8.631588,-4.293976,7.179403,-2.837084,6.023348,2.598237,3.684494,0.243950,6.362064,-1.111145,8.667169,1.929421,1.375222,-4.809443,-7.704454,3.520179,-7.392232,1.548224,-0.543141,-1.132950,3.287486,-9.794452,8.420580,-8.169682,-6.606924,-9.136879,-8.271684,-5.565126,3.220841,-2.885125,-1.167760,-2.000634,6.644967,-7.635682,0.663157,-4.920247,-2.080722,-1.542622,-6.747173,7.244561,8.338260,-4.865768,1.626281,-3.319267,-9.269949,-3.939659,-3.192723,6.674464,-5.113185,8.700716,6.816581,-6.042801,-3.194918,2.251242,5.708664,9.697001,8.737039,-3.377709,3.682473,7.430672,-0.866992,-7.679615,0.222338,-2.652230,-7.626659,0.919933,1.996637,3.171025,-5.529207,7.106169,5.920478,3.050118,-2.943068,4.924235,-3.579553,6.112662,-5.576247,1.693970,-0.226427,2.303821,9.904642,-5.422772,-5.660090,-6.223950,-1.421398,-1.411865,5.218353,-9.825843,-0.534675,6.961752,8.822171,6.534480,-2.012053,5.022901], dtype = "float32")#candidate|3961|(405,)|const|float32
call_3960 = relay.TupleGetItem(func_471_call(relay.reshape(call_3953.astype('bool'), [16, 8, 2]), relay.reshape(const_3961.astype('float32'), [405, 1]), ), 3)
call_3962 = relay.TupleGetItem(func_475_call(relay.reshape(call_3953.astype('bool'), [16, 8, 2]), relay.reshape(const_3961.astype('float32'), [405, 1]), ), 3)
func_2744_call = mod.get_global_var('func_2744')
func_2746_call = mutated_mod.get_global_var('func_2746')
const_3964 = relay.const([0.173754,1.415350,-7.398722,6.867968,-5.905131,1.541439,-9.809313,6.815863,-6.153910,-8.664216,-9.822112,1.187165,-5.374081,7.671646,-0.112100,2.209720,-4.041788,-5.896631,9.476347,-8.578619,4.050696,2.319255,-0.280792,8.666720,5.737253,-6.619092,-3.239028,6.927316,-9.112730,-6.785673,-9.449783,-5.296168,-9.617309,-8.299282,-3.060871,-9.357048,-2.357893,1.290533,-0.963979,8.457475,-2.497146,5.888450,0.241827,1.432641,8.873054,5.842725,-7.358479,-4.084853,-9.203216,-1.541713,0.958671,-9.631328,8.337891,-5.304739,-0.226630,9.013995,9.482416,3.729002,1.400762,3.354225,6.010464,1.397815,-6.385677,-8.043390,-4.153271,-0.989141,2.098174,7.373729,-7.255490,-5.526246,2.821943,-6.847729,-5.491295,-7.367206,-9.626595,-3.244205,-6.669344], dtype = "float64")#candidate|3964|(77,)|const|float64
call_3963 = relay.TupleGetItem(func_2744_call(relay.reshape(const_3964.astype('float64'), [77,])), 0)
call_3965 = relay.TupleGetItem(func_2746_call(relay.reshape(const_3964.astype('float64'), [77,])), 0)
uop_3976 = relay.sin(const_3964.astype('float64')) # shape=(77,)
output = relay.Tuple([call_3948,call_3953,call_3960,const_3961,call_3963,uop_3976,])
output2 = relay.Tuple([call_3949,call_3954,call_3962,const_3961,call_3965,uop_3976,])
func_4000 = relay.Function([], output)
mod['func_4000'] = func_4000
mod = relay.transform.InferType()(mod)
output = func_4000()
func_4001 = relay.Function([], output)
mutated_mod['func_4001'] = func_4001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2828_call = mod.get_global_var('func_2828')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_4067 = relay.TupleGetItem(func_2828_call(), 1)
call_4068 = relay.TupleGetItem(func_2829_call(), 1)
uop_4071 = relay.log10(call_4067.astype('float32')) # shape=(11, 2, 7)
uop_4073 = relay.log10(call_4068.astype('float32')) # shape=(11, 2, 7)
output = uop_4071
output2 = uop_4073
func_4075 = relay.Function([], output)
mod['func_4075'] = func_4075
mod = relay.transform.InferType()(mod)
mutated_mod['func_4075'] = func_4075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4075_call = mutated_mod.get_global_var('func_4075')
call_4076 = func_4075_call()
output = call_4076
func_4077 = relay.Function([], output)
mutated_mod['func_4077'] = func_4077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3478_call = mod.get_global_var('func_3478')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_4084 = relay.TupleGetItem(func_3478_call(), 1)
call_4085 = relay.TupleGetItem(func_3480_call(), 1)
output = relay.Tuple([call_4084,])
output2 = relay.Tuple([call_4085,])
func_4086 = relay.Function([], output)
mod['func_4086'] = func_4086
mod = relay.transform.InferType()(mod)
output = func_4086()
func_4087 = relay.Function([], output)
mutated_mod['func_4087'] = func_4087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3214_call = mod.get_global_var('func_3214')
func_3216_call = mutated_mod.get_global_var('func_3216')
call_4098 = relay.TupleGetItem(func_3214_call(), 1)
call_4099 = relay.TupleGetItem(func_3216_call(), 1)
output = call_4098
output2 = call_4099
func_4108 = relay.Function([], output)
mod['func_4108'] = func_4108
mod = relay.transform.InferType()(mod)
output = func_4108()
func_4109 = relay.Function([], output)
mutated_mod['func_4109'] = func_4109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3001_call = mod.get_global_var('func_3001')
func_3002_call = mutated_mod.get_global_var('func_3002')
call_4138 = func_3001_call()
call_4139 = func_3001_call()
func_2828_call = mod.get_global_var('func_2828')
func_2829_call = mutated_mod.get_global_var('func_2829')
call_4149 = relay.TupleGetItem(func_2828_call(), 3)
call_4150 = relay.TupleGetItem(func_2829_call(), 3)
func_3927_call = mod.get_global_var('func_3927')
func_3929_call = mutated_mod.get_global_var('func_3929')
call_4152 = func_3927_call()
call_4153 = func_3927_call()
bop_4155 = relay.minimum(call_4149.astype('uint64'), relay.reshape(call_4138.astype('uint64'), relay.shape_of(call_4149))) # shape=(16, 8, 2)
bop_4158 = relay.minimum(call_4150.astype('uint64'), relay.reshape(call_4139.astype('uint64'), relay.shape_of(call_4150))) # shape=(16, 8, 2)
output = relay.Tuple([call_4152,bop_4155,])
output2 = relay.Tuple([call_4153,bop_4158,])
func_4159 = relay.Function([], output)
mod['func_4159'] = func_4159
mod = relay.transform.InferType()(mod)
output = func_4159()
func_4160 = relay.Function([], output)
mutated_mod['func_4160'] = func_4160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3927_call = mod.get_global_var('func_3927')
func_3929_call = mutated_mod.get_global_var('func_3929')
call_4169 = func_3927_call()
call_4170 = func_3927_call()
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_4175 = func_1354_call()
call_4176 = func_1354_call()
output = relay.Tuple([call_4169,call_4175,])
output2 = relay.Tuple([call_4170,call_4176,])
func_4178 = relay.Function([], output)
mod['func_4178'] = func_4178
mod = relay.transform.InferType()(mod)
mutated_mod['func_4178'] = func_4178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4178_call = mutated_mod.get_global_var('func_4178')
call_4179 = func_4178_call()
output = call_4179
func_4180 = relay.Function([], output)
mutated_mod['func_4180'] = func_4180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1423_call = mod.get_global_var('func_1423')
func_1425_call = mutated_mod.get_global_var('func_1425')
call_4246 = relay.TupleGetItem(func_1423_call(), 0)
call_4247 = relay.TupleGetItem(func_1425_call(), 0)
func_1725_call = mod.get_global_var('func_1725')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_4252 = relay.TupleGetItem(func_1725_call(), 0)
call_4253 = relay.TupleGetItem(func_1727_call(), 0)
var_4264 = relay.var("var_4264", dtype = "bool", shape = (16, 8, 2))#candidate|4264|(16, 8, 2)|var|bool
bop_4265 = relay.subtract(call_4246.astype('uint8'), relay.reshape(var_4264.astype('uint8'), relay.shape_of(call_4246))) # shape=(16, 8, 2)
bop_4268 = relay.subtract(call_4247.astype('uint8'), relay.reshape(var_4264.astype('uint8'), relay.shape_of(call_4247))) # shape=(16, 8, 2)
output = relay.Tuple([call_4252,bop_4265,])
output2 = relay.Tuple([call_4253,bop_4268,])
func_4269 = relay.Function([var_4264,], output)
mod['func_4269'] = func_4269
mod = relay.transform.InferType()(mod)
mutated_mod['func_4269'] = func_4269
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4270 = relay.var("var_4270", dtype = "bool", shape = (16, 8, 2))#candidate|4270|(16, 8, 2)|var|bool
func_4269_call = mutated_mod.get_global_var('func_4269')
call_4271 = func_4269_call(var_4270)
output = call_4271
func_4272 = relay.Function([var_4270], output)
mutated_mod['func_4272'] = func_4272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1725_call = mod.get_global_var('func_1725')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_4395 = relay.TupleGetItem(func_1725_call(), 4)
call_4396 = relay.TupleGetItem(func_1727_call(), 4)
output = call_4395
output2 = call_4396
func_4405 = relay.Function([], output)
mod['func_4405'] = func_4405
mod = relay.transform.InferType()(mod)
output = func_4405()
func_4406 = relay.Function([], output)
mutated_mod['func_4406'] = func_4406
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4429 = relay.var("var_4429", dtype = "float64", shape = (11, 5, 9))#candidate|4429|(11, 5, 9)|var|float64
uop_4430 = relay.log(var_4429.astype('float64')) # shape=(11, 5, 9)
output = uop_4430
output2 = uop_4430
func_4441 = relay.Function([var_4429,], output)
mod['func_4441'] = func_4441
mod = relay.transform.InferType()(mod)
var_4442 = relay.var("var_4442", dtype = "float64", shape = (11, 5, 9))#candidate|4442|(11, 5, 9)|var|float64
output = func_4441(var_4442)
func_4443 = relay.Function([var_4442], output)
mutated_mod['func_4443'] = func_4443
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4465 = relay.const([[[-0.251387,5.450995,-5.437899,-9.730692,-5.300313],[0.473246,-8.791755,6.423258,5.903208,-0.604015],[-8.381631,8.127987,3.144082,0.980351,8.195837],[2.759709,5.320437,0.658387,-5.874812,7.926230],[6.850789,-5.203669,3.079890,-4.816009,-4.537320],[-9.831315,3.651965,-1.480247,5.442921,8.437316]],[[1.548901,-1.780936,0.365556,-0.882096,-9.136809],[-8.170776,-8.837257,2.586825,-2.401431,-3.666673],[-6.626653,-0.692100,-1.520522,1.149230,-5.241291],[9.414338,2.474822,-9.350715,9.352998,-3.199589],[-0.558615,0.975848,-9.146444,-4.995048,-8.768559],[4.994286,3.810760,-6.503307,0.525266,-2.546579]],[[-2.124064,7.556866,6.022025,-8.682428,-2.784767],[-6.358130,6.802159,7.085351,2.244173,-7.339953],[-1.802502,-8.683759,3.016551,-4.509267,-6.640027],[-5.620764,-8.113604,8.445671,-5.071682,-9.278463],[-0.909072,8.737205,-3.211002,0.159339,0.612547],[9.461153,-0.804598,6.721839,-0.561641,-6.813336]],[[-0.029568,0.972329,-4.301455,3.876901,-0.109223],[7.279422,-5.859843,-6.366532,8.950918,-7.973328],[3.307676,-9.489837,-0.785219,-1.108178,2.325485],[8.767774,5.753926,-7.687651,5.408955,-9.888600],[9.608748,2.560490,4.979447,-4.750331,5.961092],[0.814040,-8.563565,-3.621031,6.597095,5.275066]],[[9.161355,5.245125,3.440281,-3.071045,3.187436],[-5.441118,-8.596142,-1.418997,2.660372,-5.673105],[-1.224877,-4.767142,-5.229631,1.856895,0.573232],[-9.238756,5.368317,2.139892,-2.738930,-7.315877],[3.556394,-8.026215,-8.231132,9.083836,-7.599102],[-4.370342,3.717308,3.191826,-9.173441,6.431177]]], dtype = "float32")#candidate|4465|(5, 6, 5)|const|float32
uop_4466 = relay.sinh(const_4465.astype('float32')) # shape=(5, 6, 5)
output = uop_4466
output2 = uop_4466
func_4475 = relay.Function([], output)
mod['func_4475'] = func_4475
mod = relay.transform.InferType()(mod)
output = func_4475()
func_4476 = relay.Function([], output)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2406_call = mod.get_global_var('func_2406')
func_2407_call = mutated_mod.get_global_var('func_2407')
call_4477 = relay.TupleGetItem(func_2406_call(), 0)
call_4478 = relay.TupleGetItem(func_2407_call(), 0)
output = call_4477
output2 = call_4478
func_4481 = relay.Function([], output)
mod['func_4481'] = func_4481
mod = relay.transform.InferType()(mod)
mutated_mod['func_4481'] = func_4481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4481_call = mutated_mod.get_global_var('func_4481')
call_4482 = func_4481_call()
output = call_4482
func_4483 = relay.Function([], output)
mutated_mod['func_4483'] = func_4483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4475_call = mod.get_global_var('func_4475')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_4484 = func_4475_call()
call_4485 = func_4475_call()
output = relay.Tuple([call_4484,])
output2 = relay.Tuple([call_4485,])
func_4492 = relay.Function([], output)
mod['func_4492'] = func_4492
mod = relay.transform.InferType()(mod)
output = func_4492()
func_4493 = relay.Function([], output)
mutated_mod['func_4493'] = func_4493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3766_call = mutated_mod.get_global_var('func_3766')
call_4497 = relay.TupleGetItem(func_3765_call(), 2)
call_4498 = relay.TupleGetItem(func_3766_call(), 2)
output = relay.Tuple([call_4497,])
output2 = relay.Tuple([call_4498,])
func_4500 = relay.Function([], output)
mod['func_4500'] = func_4500
mod = relay.transform.InferType()(mod)
mutated_mod['func_4500'] = func_4500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4500_call = mutated_mod.get_global_var('func_4500')
call_4501 = func_4500_call()
output = call_4501
func_4502 = relay.Function([], output)
mutated_mod['func_4502'] = func_4502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3660_call = mod.get_global_var('func_3660')
func_3662_call = mutated_mod.get_global_var('func_3662')
call_4546 = relay.TupleGetItem(func_3660_call(), 0)
call_4547 = relay.TupleGetItem(func_3662_call(), 0)
func_3001_call = mod.get_global_var('func_3001')
func_3002_call = mutated_mod.get_global_var('func_3002')
call_4591 = func_3001_call()
call_4592 = func_3001_call()
output = relay.Tuple([call_4546,call_4591,])
output2 = relay.Tuple([call_4547,call_4592,])
func_4622 = relay.Function([], output)
mod['func_4622'] = func_4622
mod = relay.transform.InferType()(mod)
mutated_mod['func_4622'] = func_4622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4622_call = mutated_mod.get_global_var('func_4622')
call_4623 = func_4622_call()
output = call_4623
func_4624 = relay.Function([], output)
mutated_mod['func_4624'] = func_4624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4500_call = mod.get_global_var('func_4500')
func_4502_call = mutated_mod.get_global_var('func_4502')
call_4632 = relay.TupleGetItem(func_4500_call(), 0)
call_4633 = relay.TupleGetItem(func_4502_call(), 0)
func_3282_call = mod.get_global_var('func_3282')
func_3283_call = mutated_mod.get_global_var('func_3283')
call_4669 = func_3282_call()
call_4670 = func_3282_call()
output = relay.Tuple([call_4632,call_4669,])
output2 = relay.Tuple([call_4633,call_4670,])
func_4677 = relay.Function([], output)
mod['func_4677'] = func_4677
mod = relay.transform.InferType()(mod)
output = func_4677()
func_4678 = relay.Function([], output)
mutated_mod['func_4678'] = func_4678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4709 = relay.var("var_4709", dtype = "float32", shape = (2, 4, 15))#candidate|4709|(2, 4, 15)|var|float32
uop_4710 = relay.tan(var_4709.astype('float32')) # shape=(2, 4, 15)
bop_4712 = relay.minimum(var_4709.astype('uint16'), relay.reshape(uop_4710.astype('uint16'), relay.shape_of(var_4709))) # shape=(2, 4, 15)
uop_4721 = relay.erf(uop_4710.astype('float64')) # shape=(2, 4, 15)
func_3214_call = mod.get_global_var('func_3214')
func_3216_call = mutated_mod.get_global_var('func_3216')
call_4724 = relay.TupleGetItem(func_3214_call(), 2)
call_4725 = relay.TupleGetItem(func_3216_call(), 2)
bop_4728 = relay.floor_mod(uop_4721.astype('float32'), relay.reshape(bop_4712.astype('float32'), relay.shape_of(uop_4721))) # shape=(2, 4, 15)
output = relay.Tuple([call_4724,bop_4728,])
output2 = relay.Tuple([call_4725,bop_4728,])
func_4733 = relay.Function([var_4709,], output)
mod['func_4733'] = func_4733
mod = relay.transform.InferType()(mod)
var_4734 = relay.var("var_4734", dtype = "float32", shape = (2, 4, 15))#candidate|4734|(2, 4, 15)|var|float32
output = func_4733(var_4734)
func_4735 = relay.Function([var_4734], output)
mutated_mod['func_4735'] = func_4735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4481_call = mod.get_global_var('func_4481')
func_4483_call = mutated_mod.get_global_var('func_4483')
call_4783 = func_4481_call()
call_4784 = func_4481_call()
output = relay.Tuple([call_4783,])
output2 = relay.Tuple([call_4784,])
func_4791 = relay.Function([], output)
mod['func_4791'] = func_4791
mod = relay.transform.InferType()(mod)
output = func_4791()
func_4792 = relay.Function([], output)
mutated_mod['func_4792'] = func_4792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1825_call = mod.get_global_var('func_1825')
func_1826_call = mutated_mod.get_global_var('func_1826')
call_4793 = relay.TupleGetItem(func_1825_call(), 2)
call_4794 = relay.TupleGetItem(func_1826_call(), 2)
var_4798 = relay.var("var_4798", dtype = "int32", shape = (16, 8, 2))#candidate|4798|(16, 8, 2)|var|int32
bop_4799 = relay.mod(call_4793.astype('float64'), relay.reshape(var_4798.astype('float64'), relay.shape_of(call_4793))) # shape=(16, 8, 2)
bop_4802 = relay.mod(call_4794.astype('float64'), relay.reshape(var_4798.astype('float64'), relay.shape_of(call_4794))) # shape=(16, 8, 2)
func_4269_call = mod.get_global_var('func_4269')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_4803 = relay.TupleGetItem(func_4269_call(relay.reshape(bop_4799.astype('bool'), [16, 8, 2])), 1)
call_4804 = relay.TupleGetItem(func_4272_call(relay.reshape(bop_4799.astype('bool'), [16, 8, 2])), 1)
output = relay.Tuple([bop_4799,call_4803,])
output2 = relay.Tuple([bop_4802,call_4804,])
func_4813 = relay.Function([var_4798,], output)
mod['func_4813'] = func_4813
mod = relay.transform.InferType()(mod)
var_4814 = relay.var("var_4814", dtype = "int32", shape = (16, 8, 2))#candidate|4814|(16, 8, 2)|var|int32
output = func_4813(var_4814)
func_4815 = relay.Function([var_4814], output)
mutated_mod['func_4815'] = func_4815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3927_call = mod.get_global_var('func_3927')
func_3929_call = mutated_mod.get_global_var('func_3929')
call_4885 = func_3927_call()
call_4886 = func_3927_call()
func_2916_call = mod.get_global_var('func_2916')
func_2917_call = mutated_mod.get_global_var('func_2917')
call_4896 = func_2916_call()
call_4897 = func_2916_call()
var_4898 = relay.var("var_4898", dtype = "float64", shape = (77, 13))#candidate|4898|(77, 13)|var|float64
bop_4899 = relay.less_equal(call_4885.astype('bool'), var_4898.astype('bool')) # shape=(77, 13)
bop_4902 = relay.less_equal(call_4886.astype('bool'), var_4898.astype('bool')) # shape=(77, 13)
bop_4917 = relay.power(call_4885.astype('float32'), var_4898.astype('float32')) # shape=(77, 13)
bop_4920 = relay.power(call_4886.astype('float32'), var_4898.astype('float32')) # shape=(77, 13)
bop_4925 = relay.subtract(bop_4917.astype('uint16'), relay.reshape(bop_4899.astype('uint16'), relay.shape_of(bop_4917))) # shape=(77, 13)
bop_4928 = relay.subtract(bop_4920.astype('uint16'), relay.reshape(bop_4902.astype('uint16'), relay.shape_of(bop_4920))) # shape=(77, 13)
output = relay.Tuple([call_4896,bop_4925,])
output2 = relay.Tuple([call_4897,bop_4928,])
func_4929 = relay.Function([var_4898,], output)
mod['func_4929'] = func_4929
mod = relay.transform.InferType()(mod)
mutated_mod['func_4929'] = func_4929
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4930 = relay.var("var_4930", dtype = "float64", shape = (77, 13))#candidate|4930|(77, 13)|var|float64
func_4929_call = mutated_mod.get_global_var('func_4929')
call_4931 = func_4929_call(var_4930)
output = call_4931
func_4932 = relay.Function([var_4930], output)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3406_call = mod.get_global_var('func_3406')
func_3408_call = mutated_mod.get_global_var('func_3408')
call_4947 = relay.TupleGetItem(func_3406_call(), 1)
call_4948 = relay.TupleGetItem(func_3408_call(), 1)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_4955 = relay.TupleGetItem(func_2168_call(), 1)
call_4956 = relay.TupleGetItem(func_2169_call(), 1)
output = relay.Tuple([call_4947,call_4955,])
output2 = relay.Tuple([call_4948,call_4956,])
func_4959 = relay.Function([], output)
mod['func_4959'] = func_4959
mod = relay.transform.InferType()(mod)
output = func_4959()
func_4960 = relay.Function([], output)
mutated_mod['func_4960'] = func_4960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3478_call = mod.get_global_var('func_3478')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_4961 = relay.TupleGetItem(func_3478_call(), 1)
call_4962 = relay.TupleGetItem(func_3480_call(), 1)
output = relay.Tuple([call_4961,])
output2 = relay.Tuple([call_4962,])
func_4976 = relay.Function([], output)
mod['func_4976'] = func_4976
mod = relay.transform.InferType()(mod)
mutated_mod['func_4976'] = func_4976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4976_call = mutated_mod.get_global_var('func_4976')
call_4977 = func_4976_call()
output = call_4977
func_4978 = relay.Function([], output)
mutated_mod['func_4978'] = func_4978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1663_call = mod.get_global_var('func_1663')
func_1665_call = mutated_mod.get_global_var('func_1665')
call_4979 = func_1663_call()
call_4980 = func_1663_call()
output = call_4979
output2 = call_4980
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
func_1354_call = mod.get_global_var('func_1354')
func_1355_call = mutated_mod.get_global_var('func_1355')
call_4986 = func_1354_call()
call_4987 = func_1354_call()
func_4269_call = mod.get_global_var('func_4269')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_4992 = relay.TupleGetItem(func_4269_call(relay.reshape(call_4986.astype('bool'), [16, 8, 2])), 1)
call_4993 = relay.TupleGetItem(func_4272_call(relay.reshape(call_4986.astype('bool'), [16, 8, 2])), 1)
output = relay.Tuple([call_4986,call_4992,])
output2 = relay.Tuple([call_4987,call_4993,])
func_5006 = relay.Function([], output)
mod['func_5006'] = func_5006
mod = relay.transform.InferType()(mod)
mutated_mod['func_5006'] = func_5006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5006_call = mutated_mod.get_global_var('func_5006')
call_5007 = func_5006_call()
output = call_5007
func_5008 = relay.Function([], output)
mutated_mod['func_5008'] = func_5008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_922_call = mod.get_global_var('func_922')
func_923_call = mutated_mod.get_global_var('func_923')
call_5022 = func_922_call()
call_5023 = func_922_call()
output = call_5022
output2 = call_5023
func_5038 = relay.Function([], output)
mod['func_5038'] = func_5038
mod = relay.transform.InferType()(mod)
output = func_5038()
func_5039 = relay.Function([], output)
mutated_mod['func_5039'] = func_5039
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5040 = relay.var("var_5040", dtype = "int64", shape = (5, 7, 4))#candidate|5040|(5, 7, 4)|var|int64
var_5041 = relay.var("var_5041", dtype = "int64", shape = (5, 7, 4))#candidate|5041|(5, 7, 4)|var|int64
bop_5042 = relay.logical_xor(var_5040.astype('int64'), relay.reshape(var_5041.astype('int64'), relay.shape_of(var_5040))) # shape=(5, 7, 4)
output = bop_5042
output2 = bop_5042
func_5046 = relay.Function([var_5040,var_5041,], output)
mod['func_5046'] = func_5046
mod = relay.transform.InferType()(mod)
mutated_mod['func_5046'] = func_5046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5046_call = mutated_mod.get_global_var('func_5046')
var_5048 = relay.var("var_5048", dtype = "int64", shape = (5, 7, 4))#candidate|5048|(5, 7, 4)|var|int64
var_5049 = relay.var("var_5049", dtype = "int64", shape = (5, 7, 4))#candidate|5049|(5, 7, 4)|var|int64
call_5047 = func_5046_call(var_5048,var_5049,)
output = call_5047
func_5050 = relay.Function([var_5048,var_5049,], output)
mutated_mod['func_5050'] = func_5050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5092 = relay.var("var_5092", dtype = "float32", shape = (10, 4, 14))#candidate|5092|(10, 4, 14)|var|float32
uop_5093 = relay.log(var_5092.astype('float32')) # shape=(10, 4, 14)
output = uop_5093
output2 = uop_5093
func_5096 = relay.Function([var_5092,], output)
mod['func_5096'] = func_5096
mod = relay.transform.InferType()(mod)
mutated_mod['func_5096'] = func_5096
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5097 = relay.var("var_5097", dtype = "float32", shape = (10, 4, 14))#candidate|5097|(10, 4, 14)|var|float32
func_5096_call = mutated_mod.get_global_var('func_5096')
call_5098 = func_5096_call(var_5097)
output = call_5098
func_5099 = relay.Function([var_5097], output)
mutated_mod['func_5099'] = func_5099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3910_call = mod.get_global_var('func_3910')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_5147 = func_3910_call()
call_5148 = func_3910_call()
output = relay.Tuple([call_5147,])
output2 = relay.Tuple([call_5148,])
func_5155 = relay.Function([], output)
mod['func_5155'] = func_5155
mod = relay.transform.InferType()(mod)
output = func_5155()
func_5156 = relay.Function([], output)
mutated_mod['func_5156'] = func_5156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_666_call = mod.get_global_var('func_666')
func_667_call = mutated_mod.get_global_var('func_667')
call_5159 = func_666_call()
call_5160 = func_666_call()
output = relay.Tuple([call_5159,])
output2 = relay.Tuple([call_5160,])
func_5183 = relay.Function([], output)
mod['func_5183'] = func_5183
mod = relay.transform.InferType()(mod)
output = func_5183()
func_5184 = relay.Function([], output)
mutated_mod['func_5184'] = func_5184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5198 = relay.var("var_5198", dtype = "float64", shape = (11, 8, 10))#candidate|5198|(11, 8, 10)|var|float64
var_5199 = relay.var("var_5199", dtype = "float64", shape = (11, 8, 10))#candidate|5199|(11, 8, 10)|var|float64
bop_5200 = relay.divide(var_5198.astype('float64'), relay.reshape(var_5199.astype('float64'), relay.shape_of(var_5198))) # shape=(11, 8, 10)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
var_5205 = relay.var("var_5205", dtype = "bool", shape = (8, 32))#candidate|5205|(8, 32)|var|bool
var_5206 = relay.var("var_5206", dtype = "float32", shape = (405,))#candidate|5206|(405,)|var|float32
call_5204 = relay.TupleGetItem(func_471_call(relay.reshape(var_5205.astype('bool'), [16, 8, 2]), relay.reshape(var_5206.astype('float32'), [405, 1]), ), 3)
call_5207 = relay.TupleGetItem(func_475_call(relay.reshape(var_5205.astype('bool'), [16, 8, 2]), relay.reshape(var_5206.astype('float32'), [405, 1]), ), 3)
func_4791_call = mod.get_global_var('func_4791')
func_4792_call = mutated_mod.get_global_var('func_4792')
call_5209 = relay.TupleGetItem(func_4791_call(), 0)
call_5210 = relay.TupleGetItem(func_4792_call(), 0)
const_5216 = relay.const([[[-9.596920,9.446858,-3.143041,-3.484305,1.045486,-3.166659,-9.631385,7.899240,7.433067,7.589015],[-0.033784,5.497255,5.792909,-8.369452,-9.532896,1.421460,-6.634552,3.715891,6.907876,-4.028335],[-9.089335,9.339815,5.864082,5.289910,-0.766411,-4.067633,-1.580619,0.262838,-4.204176,5.820232],[7.840080,3.621272,4.281736,-7.483997,-0.601113,-9.603723,2.553107,-7.370510,-0.204687,-1.629127],[-9.707146,-5.736491,-6.655426,3.067146,9.601957,8.070864,6.661445,-7.203280,-4.578011,7.408595],[3.132529,0.571895,8.334830,-1.409060,5.508386,5.092829,4.293468,7.472477,4.159112,8.234225],[0.330979,6.209614,6.238779,-8.341357,-5.381025,1.644826,7.810181,-3.974643,-9.642475,-9.723713],[8.449114,0.779899,4.216538,-0.483104,2.584470,-2.203703,9.514823,3.366067,1.092098,-7.980214]],[[7.289707,-3.156715,-6.388367,-0.457046,7.081633,-0.929360,-2.127961,6.042378,-3.713579,-2.763064],[8.949570,6.267426,-8.790433,-2.287221,-0.621073,9.739145,-5.533464,-3.448869,-8.174489,8.188724],[8.010998,5.620240,9.525561,-4.022239,-8.776402,-2.595076,8.658969,-6.169450,-9.263274,8.157159],[8.998570,4.141112,-3.594903,-3.822065,-1.659965,-2.174683,-7.863650,6.973754,6.802978,2.738838],[-2.686491,5.644820,8.328107,7.181081,-0.881317,-7.385449,0.586446,6.139259,0.722303,-1.020691],[4.447597,-2.483999,-2.543580,-9.920665,5.802342,-0.824609,8.706686,1.377061,7.465554,-5.401943],[5.961314,-5.945438,-2.196192,8.130575,8.494015,8.437368,-5.806783,-9.025243,9.204715,-3.188976],[4.108609,-8.469417,5.701598,0.828270,-1.786085,-0.323824,4.415818,-8.325238,6.495364,5.339901]],[[-8.297391,6.497467,-4.802920,6.942588,-2.941816,-4.666716,-5.401381,-3.212320,-1.233234,9.882683],[-9.363704,8.932090,-5.855842,8.758455,3.552288,-1.092147,-7.395471,-8.579837,-8.093515,-5.161911],[-5.269608,-6.634282,-0.298059,-2.075334,-8.690492,8.549563,4.984042,-3.424497,8.337244,0.366267],[2.263337,-4.419160,-1.036349,-5.889980,-8.422799,6.419296,-3.280441,-2.058395,0.870440,7.521004],[-1.710063,-8.603471,7.288843,6.374471,-4.136644,9.324057,-9.284815,3.054666,0.919229,0.521349],[4.695826,-7.879180,-0.029598,-2.564004,6.189533,-2.764438,-7.254975,6.403352,4.360816,-9.008771],[-3.684575,1.396221,0.669646,2.665027,6.299470,4.767850,6.988896,-3.870538,-1.694496,3.388453],[-0.863934,9.121122,-7.049328,7.900816,6.540287,-1.225475,0.158431,-7.450278,-2.224916,2.515610]],[[4.539771,-9.143456,-4.379148,-8.312627,6.542723,-8.886672,5.642744,2.289043,1.657363,-6.303617],[-0.056557,-0.998418,-9.039341,5.988887,-0.818405,-3.167522,6.968863,-9.747865,0.431984,-9.438437],[5.319619,1.723356,-9.122071,-4.101957,9.723050,-1.081392,4.590510,1.889259,1.892487,5.394264],[-0.312259,1.933747,-7.618073,4.882129,6.843999,1.986938,0.127600,0.580897,9.641009,3.005108],[-9.577459,-2.318684,-5.670981,-7.758343,-6.755662,5.045560,0.532268,-8.659444,-9.913053,-8.108503],[6.265590,-9.284673,-6.391787,-8.609003,-7.682799,-0.737912,1.788026,-2.910908,-4.588419,-9.895909],[-0.600630,9.277970,-1.963145,-2.593011,-3.044695,-4.643591,-2.351788,-5.149765,0.539277,-5.222515],[-5.328092,-8.690362,0.015471,9.844791,5.875518,4.321634,5.306436,-4.217256,-1.128798,-2.959008]],[[7.331399,4.729034,-7.387789,-3.669774,-7.779711,9.797409,3.887755,0.397408,-4.979018,-3.894900],[-6.437270,-6.982002,0.791310,8.526076,8.369026,-2.676146,1.062952,-5.738878,8.294178,3.500260],[1.492606,-1.419817,-1.840230,4.518089,-9.627029,6.133366,3.204662,-2.937682,-9.476892,4.240414],[3.177302,-8.054681,8.050340,-0.261802,0.901045,-6.001251,-8.495428,3.143678,-1.911290,-8.090354],[-7.619736,5.678238,1.909059,-9.641210,-9.729459,4.870321,4.810162,-1.291448,-8.394381,5.602059],[-2.121094,-0.262695,-7.705756,0.016486,-6.097604,3.230389,5.001860,8.180439,-3.665445,-7.013801],[0.690453,1.830810,0.642322,4.804600,-8.451793,8.596900,-9.380107,-1.419991,1.277743,-9.665493],[9.995150,6.894099,-0.236015,1.548038,-2.929736,9.047074,5.455174,4.999932,-0.255908,-0.880722]],[[5.604702,7.235348,0.101926,2.768186,-9.262251,-5.564858,1.160468,-5.090635,-5.307312,0.323040],[-7.117678,-2.460642,4.504505,-3.180088,-7.051727,-4.384557,3.069111,-9.519121,2.183597,1.244096],[3.212984,4.175511,4.991759,-5.670245,6.922656,8.336682,1.888452,5.748619,7.315488,-5.375856],[-8.409923,8.921497,3.109214,-9.888767,4.113209,-6.146475,-9.102378,-9.387230,3.482528,9.546215],[-1.103012,-7.540152,7.846521,-7.760150,-8.680849,-9.065435,6.543579,-8.778265,8.230222,-7.053600],[-5.708693,0.588254,-1.183902,8.535496,5.154472,2.878535,0.971938,9.253081,1.606153,0.627509],[-1.164171,9.049601,3.641768,-0.160908,-4.689074,-3.419808,1.347965,4.608102,5.297058,-3.608139],[-4.199269,-2.245531,2.947231,-9.733413,4.738965,-2.304568,6.697689,9.457204,2.529408,-0.341669]],[[-7.837272,7.946898,-2.388196,-9.917036,6.727330,-0.951262,-3.290556,4.542679,-4.644095,-5.569579],[5.812151,-6.941994,-5.063860,7.245227,7.675512,-1.349656,-9.400572,-1.366581,-1.559958,-5.727540],[9.784500,9.227983,1.824558,0.985822,-7.221945,6.537009,3.882130,5.204158,-5.345543,5.985051],[-5.599783,1.864696,8.586147,3.574077,-3.446141,1.846031,6.087928,7.496384,6.262831,-3.794693],[7.566243,7.254097,7.228857,-8.295182,-2.843565,-1.808320,7.837048,8.714086,2.087948,4.522313],[8.846381,7.787179,7.631113,5.312196,7.842324,3.605311,-2.255878,2.399852,4.546206,3.724647],[-0.293445,-9.251623,5.068691,-8.039085,-9.016586,7.136975,8.941902,-4.514192,8.238813,0.247803],[-0.105652,9.488733,-6.115423,-3.179239,5.074094,8.204466,9.956706,2.045163,6.124117,3.225121]],[[5.531208,5.492619,0.316013,-2.820784,-8.908737,-7.875342,-1.641551,7.150931,-5.361683,-8.964731],[5.329262,0.891507,7.971722,0.971190,0.761051,-5.394350,7.284219,4.378347,-5.958144,-9.698437],[0.900554,4.625914,-9.410392,-7.455401,-4.941900,-3.860707,-1.521321,9.519066,6.514471,3.587622],[8.482716,2.787477,5.198632,-7.556243,-6.756079,-6.963973,5.661187,1.404490,-8.740293,-3.417764],[-6.381327,-5.861080,8.511556,-1.296153,9.402637,2.594445,-0.133992,8.168963,0.011787,9.323320],[-1.883203,1.110281,1.719034,-6.457782,6.504057,-0.345389,7.649676,-5.165270,-9.121214,0.742108],[-3.870086,8.224746,-8.895125,6.421086,-7.127508,8.153989,-6.413587,-5.348615,-7.204955,-8.326187],[2.032828,6.872136,3.558306,5.242285,7.813939,0.678869,2.691715,-6.879781,-2.889250,5.485457]],[[-7.442354,2.700177,-3.803979,-0.084670,-3.602739,-5.847855,6.914159,4.427758,2.455550,0.749015],[2.564860,8.546226,0.456658,-6.221842,1.004619,-1.623293,4.124723,-9.823959,6.996595,-7.208344],[2.327714,2.802612,-8.870585,-3.704660,-8.826857,-0.496969,-9.928936,-4.353287,7.887037,0.599151],[9.572509,-0.284847,-1.173762,-6.199634,6.758035,4.377825,7.554102,-3.236628,0.170104,9.303347],[-4.361142,-2.181930,0.939202,-9.009678,1.657712,2.927255,4.110684,6.201321,0.035658,0.974005],[-9.635947,7.355797,0.186284,-6.081253,-7.610584,-6.388003,6.037250,-6.344835,-4.844524,-2.045376],[-7.096683,-1.151024,4.384206,3.818520,4.286485,-7.009489,-4.883493,3.696463,7.262357,-5.436608],[9.062743,-8.370492,1.365584,-7.516551,4.203209,-6.135785,-5.245081,2.385478,-8.265360,-1.818014]],[[6.627577,-0.326267,5.247945,2.529073,0.978954,-3.653859,6.518902,7.334492,0.568412,-1.537684],[-0.170991,6.690491,6.071740,5.322665,0.307606,3.950948,-3.851115,-8.188326,3.373689,-1.148007],[-7.091457,6.548083,4.510898,-2.815816,-1.410376,8.503306,9.651216,-6.408169,6.373620,1.210394],[2.506276,5.629440,-3.972571,8.935012,9.718879,-9.001483,6.525892,4.658527,-0.301660,0.865685],[-9.916090,-4.838206,3.671297,-2.921566,-6.127055,-4.772858,-0.840406,0.642195,4.214753,-1.889149],[-4.502348,-9.076635,0.355544,-2.661346,-5.062754,-3.955658,-0.913001,-1.634099,6.176673,-5.540809],[-7.353935,-7.958871,-7.524472,0.389558,-6.825240,-2.412717,-3.878971,-3.506329,4.420113,-4.736569],[4.548535,-7.146288,1.502746,3.553212,-0.898828,-6.938424,-8.127981,6.051233,-8.853394,4.581125]],[[1.064425,1.276487,-9.434001,0.829911,-4.686385,7.669368,-4.837818,4.980397,4.889926,7.075159],[-0.956777,-5.401092,-9.491893,4.546728,7.545870,8.314842,-4.512722,-3.823449,7.997322,-7.629982],[8.739150,1.144373,-5.309576,2.159013,8.176669,5.233229,-5.100518,4.085722,1.688023,0.866958],[2.128142,5.316452,4.014672,-9.706470,6.553110,-1.603098,6.673756,7.274893,-5.847565,0.472017],[3.307302,8.228122,-9.354406,-2.450107,0.392287,-5.726683,-5.842183,8.972612,-7.768523,-7.033195],[-0.206331,-2.410647,-7.308347,0.429002,8.749525,1.157711,1.209735,-0.934999,5.542042,-5.507713],[9.386591,5.390320,-0.550155,2.153854,-6.749521,8.325511,8.766546,-9.344593,9.046671,-0.627147],[-5.906060,9.362452,4.460179,-1.174463,-9.686089,2.959238,4.057093,0.289750,1.651411,-2.035033]]], dtype = "float64")#candidate|5216|(11, 8, 10)|const|float64
bop_5217 = relay.bitwise_or(var_5199.astype('uint32'), relay.reshape(const_5216.astype('uint32'), relay.shape_of(var_5199))) # shape=(11, 8, 10)
output = relay.Tuple([bop_5200,call_5204,var_5205,var_5206,call_5209,bop_5217,])
output2 = relay.Tuple([bop_5200,call_5207,var_5205,var_5206,call_5210,bop_5217,])
func_5221 = relay.Function([var_5198,var_5199,var_5205,var_5206,], output)
mod['func_5221'] = func_5221
mod = relay.transform.InferType()(mod)
var_5222 = relay.var("var_5222", dtype = "float64", shape = (11, 8, 10))#candidate|5222|(11, 8, 10)|var|float64
var_5223 = relay.var("var_5223", dtype = "float64", shape = (11, 8, 10))#candidate|5223|(11, 8, 10)|var|float64
var_5224 = relay.var("var_5224", dtype = "bool", shape = (8, 32))#candidate|5224|(8, 32)|var|bool
var_5225 = relay.var("var_5225", dtype = "float32", shape = (405,))#candidate|5225|(405,)|var|float32
output = func_5221(var_5222,var_5223,var_5224,var_5225,)
func_5226 = relay.Function([var_5222,var_5223,var_5224,var_5225,], output)
mutated_mod['func_5226'] = func_5226
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5264 = relay.const([[[-9.829939,9.414950,5.991716,0.672573,2.707227,9.582936,6.229329,2.485013,-8.176093,-7.137767,3.650445,3.415113,8.270598,-5.230243],[0.267310,-0.127643,-4.309170,5.671847,9.335589,1.117254,-5.609418,0.584975,4.346592,-0.179919,-8.308713,3.596959,4.797236,3.869389],[-3.607198,-4.967885,5.289656,8.823904,-9.648692,7.473555,9.007307,2.547273,4.656813,7.468246,8.357467,-7.159455,-1.306054,4.095165]],[[-1.703058,-1.598145,2.199898,8.795846,3.070482,-4.978200,6.340918,-4.332619,-6.355419,-2.344336,-2.024741,-3.769674,0.525458,4.732742],[7.246885,-8.237253,7.294644,-1.065868,9.588143,2.720999,-2.264895,5.858561,2.580411,3.586915,7.460580,-9.195002,0.291374,7.225662],[9.632830,9.526977,1.283046,5.403122,-3.865202,4.077613,4.580759,6.809762,-7.961837,1.125652,-6.704820,6.906141,4.449216,1.950295]],[[7.412045,9.246929,-2.263402,2.018837,-3.925400,-8.555959,-9.054029,3.709600,9.135894,7.850993,1.559594,8.886939,8.407537,5.788363],[-0.713105,-2.313133,9.723936,5.092986,-0.096576,8.812961,5.707085,1.769377,-7.304401,6.803523,1.129426,7.873977,1.538786,-7.784215],[-9.191158,5.578820,0.589140,-0.737017,-9.297778,-8.291478,-6.939878,1.102325,9.982017,3.890570,7.525748,6.349902,2.132199,7.296716]],[[-3.823650,-1.135188,3.399314,0.182086,7.180059,2.598935,0.533444,-9.346005,-3.604495,5.240880,-1.191068,0.571164,0.078884,0.498211],[3.475838,-7.747445,-4.002045,-5.233463,-2.031783,-6.698828,4.829071,0.468368,0.005338,-0.233938,-1.911483,-8.631474,-0.198027,-2.162161],[-3.978862,2.357510,0.063850,3.233346,-3.585301,5.004636,-9.052478,-5.403508,-0.455795,-8.693882,1.675403,6.892678,0.348523,-8.209511]],[[5.734757,4.081704,-4.203301,5.049331,-6.273396,-6.837264,1.887095,-0.208204,2.315314,1.415128,-8.580931,-1.531755,8.808766,4.315675],[0.912610,-7.589390,1.283950,-0.527212,-3.782944,4.711244,1.750916,9.907676,6.500937,-5.460486,-6.475925,-0.165795,5.219817,-0.521490],[-5.341505,2.142695,-8.896526,-5.316996,-1.958838,8.796624,8.704275,7.305045,-3.315944,4.242927,-0.513917,8.196375,1.327339,-8.820127]],[[-1.673310,4.294570,-3.065273,-7.520724,7.995481,-0.681270,8.244307,-8.380248,-3.842713,1.736819,3.708519,1.808545,-1.376304,-8.609089],[-5.856349,3.731366,-5.244703,-5.460553,7.695432,6.301901,4.983878,-0.940441,8.678454,5.369153,5.925664,6.306504,1.300290,-9.067343],[6.313800,-4.000264,2.574529,-2.314380,-4.417120,1.696478,6.197408,-9.041629,-2.234425,4.403998,-4.450695,-6.702110,-0.011853,-8.307800]]], dtype = "float64")#candidate|5264|(6, 3, 14)|const|float64
var_5265 = relay.var("var_5265", dtype = "float64", shape = (6, 3, 14))#candidate|5265|(6, 3, 14)|var|float64
bop_5266 = relay.equal(const_5264.astype('bool'), relay.reshape(var_5265.astype('bool'), relay.shape_of(const_5264))) # shape=(6, 3, 14)
func_377_call = mod.get_global_var('func_377')
func_380_call = mutated_mod.get_global_var('func_380')
const_5278 = relay.const([7.206690,8.708740,-7.837831,3.705914,0.651151,-1.829772,1.259029,-0.291098,-8.309831,1.898769,-7.748018,5.937051,-6.852926,-7.772411,0.878226,9.922271,1.481770,2.106131,6.759243,2.188914,-1.947522,3.606430,-3.730307,-1.984357,-1.343641,1.040781,2.440618,-7.477600,-5.644981,3.185069,-3.292604,9.598508,0.609640,4.407708,4.649429,4.663961,6.287832,-5.337730,6.115380,-1.272925,-3.109233,-6.747243,-3.084239,-8.479515,5.078850,7.533128,-2.892926,5.842578,4.443050,-2.500819,3.997799,6.051286,2.207986,-6.394150,-7.958547,-1.598263,0.993047,-9.158595,3.620392,-6.297756,-6.739697,9.540314,-1.300314,-6.976957,1.000152,3.168146,2.273020,9.884541,-6.622483,8.857449,2.948526,7.477855,-9.100682,-6.414870,-0.892504,3.081217,-3.001986], dtype = "float64")#candidate|5278|(77,)|const|float64
call_5277 = relay.TupleGetItem(func_377_call(relay.reshape(const_5278.astype('float64'), [11, 1, 7])), 0)
call_5279 = relay.TupleGetItem(func_380_call(relay.reshape(const_5278.astype('float64'), [11, 1, 7])), 0)
output = relay.Tuple([bop_5266,call_5277,const_5278,])
output2 = relay.Tuple([bop_5266,call_5279,const_5278,])
func_5283 = relay.Function([var_5265,], output)
mod['func_5283'] = func_5283
mod = relay.transform.InferType()(mod)
var_5284 = relay.var("var_5284", dtype = "float64", shape = (6, 3, 14))#candidate|5284|(6, 3, 14)|var|float64
output = func_5283(var_5284)
func_5285 = relay.Function([var_5284], output)
mutated_mod['func_5285'] = func_5285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5388 = relay.var("var_5388", dtype = "float64", shape = (1, 15, 8))#candidate|5388|(1, 15, 8)|var|float64
uop_5389 = relay.sinh(var_5388.astype('float64')) # shape=(1, 15, 8)
func_4000_call = mod.get_global_var('func_4000')
func_4001_call = mutated_mod.get_global_var('func_4001')
call_5391 = relay.TupleGetItem(func_4000_call(), 0)
call_5392 = relay.TupleGetItem(func_4001_call(), 0)
func_4976_call = mod.get_global_var('func_4976')
func_4978_call = mutated_mod.get_global_var('func_4978')
call_5394 = relay.TupleGetItem(func_4976_call(), 0)
call_5395 = relay.TupleGetItem(func_4978_call(), 0)
func_2984_call = mod.get_global_var('func_2984')
func_2988_call = mutated_mod.get_global_var('func_2988')
const_5407 = relay.const([[-10,4,10,1,6,3],[-1,8,10,7,-8,-4],[9,-6,4,3,-4,-6],[-4,-6,-1,4,7,-5],[1,4,-1,4,8,4],[-5,-6,5,5,-10,-10],[1,5,5,-4,-2,-8]], dtype = "uint8")#candidate|5407|(7, 6)|const|uint8
call_5406 = relay.TupleGetItem(func_2984_call(relay.reshape(const_5407.astype('uint8'), [3, 2, 7]), relay.reshape(const_5407.astype('uint8'), [3, 2, 7]), ), 1)
call_5408 = relay.TupleGetItem(func_2988_call(relay.reshape(const_5407.astype('uint8'), [3, 2, 7]), relay.reshape(const_5407.astype('uint8'), [3, 2, 7]), ), 1)
output = relay.Tuple([uop_5389,call_5391,call_5394,call_5406,const_5407,])
output2 = relay.Tuple([uop_5389,call_5392,call_5395,call_5408,const_5407,])
func_5420 = relay.Function([var_5388,], output)
mod['func_5420'] = func_5420
mod = relay.transform.InferType()(mod)
var_5421 = relay.var("var_5421", dtype = "float64", shape = (1, 15, 8))#candidate|5421|(1, 15, 8)|var|float64
output = func_5420(var_5421)
func_5422 = relay.Function([var_5421], output)
mutated_mod['func_5422'] = func_5422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1884_call = mod.get_global_var('func_1884')
func_1886_call = mutated_mod.get_global_var('func_1886')
call_5437 = func_1884_call()
call_5438 = func_1884_call()
uop_5462 = relay.asin(call_5437.astype('float32')) # shape=(16, 8, 2)
uop_5464 = relay.asin(call_5438.astype('float32')) # shape=(16, 8, 2)
output = uop_5462
output2 = uop_5464
func_5465 = relay.Function([], output)
mod['func_5465'] = func_5465
mod = relay.transform.InferType()(mod)
output = func_5465()
func_5466 = relay.Function([], output)
mutated_mod['func_5466'] = func_5466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4159_call = mod.get_global_var('func_4159')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_5498 = relay.TupleGetItem(func_4159_call(), 1)
call_5499 = relay.TupleGetItem(func_4160_call(), 1)
output = call_5498
output2 = call_5499
func_5510 = relay.Function([], output)
mod['func_5510'] = func_5510
mod = relay.transform.InferType()(mod)
output = func_5510()
func_5511 = relay.Function([], output)
mutated_mod['func_5511'] = func_5511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1915_call = mod.get_global_var('func_1915')
func_1917_call = mutated_mod.get_global_var('func_1917')
call_5532 = relay.TupleGetItem(func_1915_call(), 0)
call_5533 = relay.TupleGetItem(func_1917_call(), 0)
output = relay.Tuple([call_5532,])
output2 = relay.Tuple([call_5533,])
func_5534 = relay.Function([], output)
mod['func_5534'] = func_5534
mod = relay.transform.InferType()(mod)
output = func_5534()
func_5535 = relay.Function([], output)
mutated_mod['func_5535'] = func_5535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2895_call = mod.get_global_var('func_2895')
func_2896_call = mutated_mod.get_global_var('func_2896')
call_5536 = relay.TupleGetItem(func_2895_call(), 0)
call_5537 = relay.TupleGetItem(func_2896_call(), 0)
uop_5547 = relay.acos(call_5536.astype('float64')) # shape=(77, 1)
uop_5549 = relay.acos(call_5537.astype('float64')) # shape=(77, 1)
func_3451_call = mod.get_global_var('func_3451')
func_3453_call = mutated_mod.get_global_var('func_3453')
var_5551 = relay.var("var_5551", dtype = "float64", shape = (540,))#candidate|5551|(540,)|var|float64
call_5550 = func_3451_call(relay.reshape(var_5551.astype('float64'), [9, 6, 10]))
call_5552 = func_3451_call(relay.reshape(var_5551.astype('float64'), [9, 6, 10]))
output = relay.Tuple([uop_5547,call_5550,var_5551,])
output2 = relay.Tuple([uop_5549,call_5552,var_5551,])
func_5554 = relay.Function([var_5551,], output)
mod['func_5554'] = func_5554
mod = relay.transform.InferType()(mod)
mutated_mod['func_5554'] = func_5554
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5555 = relay.var("var_5555", dtype = "float64", shape = (540,))#candidate|5555|(540,)|var|float64
func_5554_call = mutated_mod.get_global_var('func_5554')
call_5556 = func_5554_call(var_5555)
output = call_5556
func_5557 = relay.Function([var_5555], output)
mutated_mod['func_5557'] = func_5557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2168_call = mod.get_global_var('func_2168')
func_2169_call = mutated_mod.get_global_var('func_2169')
call_5579 = relay.TupleGetItem(func_2168_call(), 1)
call_5580 = relay.TupleGetItem(func_2169_call(), 1)
func_5534_call = mod.get_global_var('func_5534')
func_5535_call = mutated_mod.get_global_var('func_5535')
call_5587 = relay.TupleGetItem(func_5534_call(), 0)
call_5588 = relay.TupleGetItem(func_5535_call(), 0)
func_2542_call = mod.get_global_var('func_2542')
func_2544_call = mutated_mod.get_global_var('func_2544')
const_5601 = relay.const([-5.465884,-4.423078,-5.963663,3.673683,7.720899,-0.617464,3.592717,-2.732661,9.906814,-1.679901,-4.168935,4.742446,-3.748715,1.155461,-1.078638,1.126786,-1.978396,-8.333087], dtype = "float32")#candidate|5601|(18,)|const|float32
call_5600 = relay.TupleGetItem(func_2542_call(relay.reshape(const_5601.astype('float32'), [6, 3, 1])), 2)
call_5602 = relay.TupleGetItem(func_2544_call(relay.reshape(const_5601.astype('float32'), [6, 3, 1])), 2)
output = relay.Tuple([call_5579,call_5587,call_5600,const_5601,])
output2 = relay.Tuple([call_5580,call_5588,call_5602,const_5601,])
func_5603 = relay.Function([], output)
mod['func_5603'] = func_5603
mod = relay.transform.InferType()(mod)
mutated_mod['func_5603'] = func_5603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5603_call = mutated_mod.get_global_var('func_5603')
call_5604 = func_5603_call()
output = call_5604
func_5605 = relay.Function([], output)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_5606 = relay.TupleGetItem(func_2859_call(), 0)
call_5607 = relay.TupleGetItem(func_2860_call(), 0)
output = relay.Tuple([call_5606,])
output2 = relay.Tuple([call_5607,])
func_5626 = relay.Function([], output)
mod['func_5626'] = func_5626
mod = relay.transform.InferType()(mod)
output = func_5626()
func_5627 = relay.Function([], output)
mutated_mod['func_5627'] = func_5627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5638 = relay.var("var_5638", dtype = "int16", shape = ())#candidate|5638|()|var|int16
var_5639 = relay.var("var_5639", dtype = "int16", shape = (12, 5, 11))#candidate|5639|(12, 5, 11)|var|int16
bop_5640 = relay.not_equal(var_5638.astype('bool'), var_5639.astype('bool')) # shape=(12, 5, 11)
output = relay.Tuple([bop_5640,])
output2 = relay.Tuple([bop_5640,])
func_5644 = relay.Function([var_5638,var_5639,], output)
mod['func_5644'] = func_5644
mod = relay.transform.InferType()(mod)
mutated_mod['func_5644'] = func_5644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5644_call = mutated_mod.get_global_var('func_5644')
var_5646 = relay.var("var_5646", dtype = "int16", shape = ())#candidate|5646|()|var|int16
var_5647 = relay.var("var_5647", dtype = "int16", shape = (12, 5, 11))#candidate|5647|(12, 5, 11)|var|int16
call_5645 = func_5644_call(var_5646,var_5647,)
output = call_5645
func_5648 = relay.Function([var_5646,var_5647,], output)
mutated_mod['func_5648'] = func_5648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_5707 = relay.TupleGetItem(func_2859_call(), 0)
call_5708 = relay.TupleGetItem(func_2860_call(), 0)
const_5742 = relay.const([[[8.742616,-1.846801,-5.280826],[1.681779,8.718076,-9.741649],[3.425847,6.135811,-9.509046],[-8.310899,-8.539601,-5.503581],[-5.853694,-1.631213,4.307554],[-5.968570,-1.639244,-4.925244],[5.493325,7.210556,-8.546979],[8.159676,7.472503,0.374833],[8.891289,6.883539,-9.883275]],[[-0.758435,-0.236541,-3.463946],[-0.804651,-9.626331,3.364946],[7.095835,-2.271251,-1.913843],[2.443349,4.929509,-7.716777],[-1.291633,-1.293359,1.213648],[0.543015,2.670284,6.898865],[-3.201275,7.330878,-4.372795],[7.025768,3.484438,5.481017],[-9.221929,2.002620,0.830048]],[[-3.354815,6.151259,-8.671794],[-8.722979,-9.781776,7.938061],[4.973526,-8.787111,-5.015671],[-4.052069,-3.197673,-0.169320],[0.649904,-0.011149,-3.225783],[-6.473282,-2.011598,5.817281],[-5.863814,-7.627482,8.819168],[-9.581698,5.846855,6.112908],[-4.528794,7.844199,-4.394750]],[[-3.276908,-8.054617,-1.738622],[-8.224972,-6.208888,0.061095],[5.010746,8.656918,-1.246029],[4.403410,2.960465,0.260532],[1.828650,-0.617966,4.709241],[-5.177620,-4.634768,-4.862415],[2.192842,7.467031,5.129863],[2.291634,1.134888,4.120064],[3.929783,-0.763046,0.242449]],[[-0.883146,9.496478,-3.397606],[3.241591,-1.299014,4.310312],[-0.472741,-3.188655,-7.165309],[-3.915691,-2.874402,-4.891869],[-5.798659,1.878120,8.971399],[-0.529588,3.148972,-3.761622],[-3.445116,-2.450549,-6.648676],[-2.273526,-7.764275,-8.950786],[-7.155634,-3.558507,-0.852910]],[[-8.224627,-3.654214,-3.747812],[7.758095,0.033215,-2.191326],[-0.489626,7.809081,-1.314407],[-2.100922,7.223715,9.197214],[-6.336723,-2.259802,-9.980193],[9.165549,9.287819,-0.996725],[8.547814,6.746168,-4.889229],[2.037528,-0.526590,5.372643],[-5.374473,6.373784,-1.795992]],[[5.186721,4.445892,0.266717],[3.434243,-0.998832,7.538713],[-4.887261,-5.070333,0.468435],[0.932619,8.350456,-1.061568],[-7.832810,1.382375,-3.951479],[-7.193835,-5.641135,4.094672],[-0.718328,-5.859861,-8.767317],[7.822527,7.746416,-3.840556],[9.330876,8.721004,4.921553]],[[5.914780,-2.047057,-1.103917],[5.197543,-5.475059,-0.968148],[7.041029,-7.976681,8.070450],[8.264706,9.817509,0.458307],[-0.115679,-2.853045,9.649547],[4.220069,6.987077,8.298452],[-2.843859,2.766305,-8.589067],[-7.980842,-6.399846,-6.606817],[8.271951,-0.311989,-4.773316]],[[-4.748246,-4.963642,-4.839690],[7.160560,8.065056,6.450722],[-7.969765,2.222350,-5.561860],[0.528533,0.732046,-9.128337],[9.629604,-7.784292,-5.928383],[9.849077,2.737345,4.646120],[-7.383650,0.163290,-2.258174],[-7.903424,-0.488702,-6.859430],[-1.061060,3.261859,8.025410]],[[8.751537,-2.832326,-2.981393],[-2.900036,8.010540,-8.530079],[1.883750,5.943176,-6.287954],[0.442761,-0.337274,-1.064307],[-7.863060,-6.965128,-0.450001],[8.661648,1.682559,9.568465],[3.585615,1.349645,3.511472],[3.701658,-8.403027,4.134382],[-0.619555,-7.799306,-0.705193]],[[6.552032,3.370518,6.456041],[1.896909,3.167329,-6.426408],[2.164806,-6.044983,-3.897675],[-2.105047,-1.395237,4.889606],[9.239500,-1.894079,-7.364557],[-4.944520,4.970253,-4.025554],[0.032473,-9.143727,-1.174482],[-6.862630,-3.855280,-9.134071],[-0.272214,-0.425704,-9.201629]],[[5.239560,-2.943624,6.265085],[-4.225932,-0.855886,3.837378],[-8.378599,5.554538,0.132766],[5.692804,5.739514,-3.838628],[1.847219,-6.941809,6.530091],[6.699111,-8.390207,-8.319914],[-7.585507,8.086041,-2.044060],[2.636316,5.623919,8.307568],[-1.262723,-2.537811,-5.543755]],[[-2.870551,-4.358742,-3.773497],[5.122037,-2.692922,0.209505],[0.255569,4.511673,-7.684873],[5.049336,1.168382,-0.738048],[6.014093,9.992631,-3.345276],[-7.165931,0.784352,6.102695],[-5.422445,1.962188,-9.945362],[4.239689,9.354610,-8.768594],[-9.549998,2.766860,3.714693]],[[3.264320,3.161162,-1.369203],[-9.388284,-5.159967,2.713322],[5.620739,-3.500788,-9.245200],[3.411081,-8.102156,0.288970],[7.002445,-6.680699,6.639145],[-4.635310,-7.839443,7.863015],[-2.721646,8.454728,-7.386154],[-7.601038,-0.186517,-3.440463],[-7.216367,-3.139802,-1.342635]],[[6.889787,3.026456,1.116273],[5.766745,1.514072,8.198726],[9.347946,2.736786,-1.353519],[2.540697,6.509983,2.420484],[8.587175,-6.470656,-6.338154],[7.252119,-1.360191,0.500623],[6.821225,2.979847,-1.892132],[0.925990,-8.133270,-9.989043],[-9.694947,-4.949651,2.079381]]], dtype = "float32")#candidate|5742|(15, 9, 3)|const|float32
bop_5743 = relay.not_equal(call_5707.astype('bool'), relay.reshape(const_5742.astype('bool'), relay.shape_of(call_5707))) # shape=(15, 9, 3)
bop_5746 = relay.not_equal(call_5708.astype('bool'), relay.reshape(const_5742.astype('bool'), relay.shape_of(call_5708))) # shape=(15, 9, 3)
output = bop_5743
output2 = bop_5746
func_5765 = relay.Function([], output)
mod['func_5765'] = func_5765
mod = relay.transform.InferType()(mod)
output = func_5765()
func_5766 = relay.Function([], output)
mutated_mod['func_5766'] = func_5766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4075_call = mod.get_global_var('func_4075')
func_4077_call = mutated_mod.get_global_var('func_4077')
call_5793 = func_4075_call()
call_5794 = func_4075_call()
func_377_call = mod.get_global_var('func_377')
func_380_call = mutated_mod.get_global_var('func_380')
var_5805 = relay.var("var_5805", dtype = "float64", shape = (77, 1))#candidate|5805|(77, 1)|var|float64
call_5804 = relay.TupleGetItem(func_377_call(relay.reshape(var_5805.astype('float64'), [11, 1, 7])), 0)
call_5806 = relay.TupleGetItem(func_380_call(relay.reshape(var_5805.astype('float64'), [11, 1, 7])), 0)
output = relay.Tuple([call_5793,call_5804,var_5805,])
output2 = relay.Tuple([call_5794,call_5806,var_5805,])
func_5809 = relay.Function([var_5805,], output)
mod['func_5809'] = func_5809
mod = relay.transform.InferType()(mod)
mutated_mod['func_5809'] = func_5809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5810 = relay.var("var_5810", dtype = "float64", shape = (77, 1))#candidate|5810|(77, 1)|var|float64
func_5809_call = mutated_mod.get_global_var('func_5809')
call_5811 = func_5809_call(var_5810)
output = call_5811
func_5812 = relay.Function([var_5810], output)
mutated_mod['func_5812'] = func_5812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3406_call = mod.get_global_var('func_3406')
func_3408_call = mutated_mod.get_global_var('func_3408')
call_5823 = relay.TupleGetItem(func_3406_call(), 0)
call_5824 = relay.TupleGetItem(func_3408_call(), 0)
func_3214_call = mod.get_global_var('func_3214')
func_3216_call = mutated_mod.get_global_var('func_3216')
call_5826 = relay.TupleGetItem(func_3214_call(), 1)
call_5827 = relay.TupleGetItem(func_3216_call(), 1)
output = relay.Tuple([call_5823,call_5826,])
output2 = relay.Tuple([call_5824,call_5827,])
func_5839 = relay.Function([], output)
mod['func_5839'] = func_5839
mod = relay.transform.InferType()(mod)
mutated_mod['func_5839'] = func_5839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5839_call = mutated_mod.get_global_var('func_5839')
call_5840 = func_5839_call()
output = call_5840
func_5841 = relay.Function([], output)
mutated_mod['func_5841'] = func_5841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_5842 = relay.TupleGetItem(func_2859_call(), 0)
call_5843 = relay.TupleGetItem(func_2860_call(), 0)
output = relay.Tuple([call_5842,])
output2 = relay.Tuple([call_5843,])
func_5851 = relay.Function([], output)
mod['func_5851'] = func_5851
mod = relay.transform.InferType()(mod)
output = func_5851()
func_5852 = relay.Function([], output)
mutated_mod['func_5852'] = func_5852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4677_call = mod.get_global_var('func_4677')
func_4678_call = mutated_mod.get_global_var('func_4678')
call_5891 = relay.TupleGetItem(func_4677_call(), 1)
call_5892 = relay.TupleGetItem(func_4678_call(), 1)
func_2859_call = mod.get_global_var('func_2859')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_5899 = relay.TupleGetItem(func_2859_call(), 0)
call_5900 = relay.TupleGetItem(func_2860_call(), 0)
output = relay.Tuple([call_5891,call_5899,])
output2 = relay.Tuple([call_5892,call_5900,])
func_5912 = relay.Function([], output)
mod['func_5912'] = func_5912
mod = relay.transform.InferType()(mod)
output = func_5912()
func_5913 = relay.Function([], output)
mutated_mod['func_5913'] = func_5913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5765_call = mod.get_global_var('func_5765')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_5920 = func_5765_call()
call_5921 = func_5765_call()
var_5922 = relay.var("var_5922", dtype = "bool", shape = (15, 9, 3))#candidate|5922|(15, 9, 3)|var|bool
bop_5923 = relay.greater_equal(call_5920.astype('bool'), relay.reshape(var_5922.astype('bool'), relay.shape_of(call_5920))) # shape=(15, 9, 3)
bop_5926 = relay.greater_equal(call_5921.astype('bool'), relay.reshape(var_5922.astype('bool'), relay.shape_of(call_5921))) # shape=(15, 9, 3)
func_3214_call = mod.get_global_var('func_3214')
func_3216_call = mutated_mod.get_global_var('func_3216')
call_5944 = relay.TupleGetItem(func_3214_call(), 3)
call_5945 = relay.TupleGetItem(func_3216_call(), 3)
func_5183_call = mod.get_global_var('func_5183')
func_5184_call = mutated_mod.get_global_var('func_5184')
call_5952 = relay.TupleGetItem(func_5183_call(), 0)
call_5953 = relay.TupleGetItem(func_5184_call(), 0)
var_5963 = relay.var("var_5963", dtype = "bool", shape = (15, 9, 3))#candidate|5963|(15, 9, 3)|var|bool
bop_5964 = relay.logical_or(call_5920.astype('bool'), relay.reshape(var_5963.astype('bool'), relay.shape_of(call_5920))) # shape=(15, 9, 3)
bop_5967 = relay.logical_or(call_5921.astype('bool'), relay.reshape(var_5963.astype('bool'), relay.shape_of(call_5921))) # shape=(15, 9, 3)
func_1592_call = mod.get_global_var('func_1592')
func_1594_call = mutated_mod.get_global_var('func_1594')
call_5970 = func_1592_call()
call_5971 = func_1592_call()
uop_5980 = relay.asinh(var_5922.astype('float32')) # shape=(15, 9, 3)
uop_5991 = relay.exp(uop_5980.astype('float32')) # shape=(15, 9, 3)
func_3910_call = mod.get_global_var('func_3910')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_5995 = func_3910_call()
call_5996 = func_3910_call()
bop_6002 = relay.right_shift(uop_5991.astype('uint64'), relay.reshape(bop_5964.astype('uint64'), relay.shape_of(uop_5991))) # shape=(15, 9, 3)
bop_6005 = relay.right_shift(uop_5991.astype('uint64'), relay.reshape(bop_5967.astype('uint64'), relay.shape_of(uop_5991))) # shape=(15, 9, 3)
func_3503_call = mod.get_global_var('func_3503')
func_3505_call = mutated_mod.get_global_var('func_3505')
call_6015 = relay.TupleGetItem(func_3503_call(relay.reshape(call_5952.astype('bool'), [16, 8, 2])), 0)
call_6016 = relay.TupleGetItem(func_3505_call(relay.reshape(call_5952.astype('bool'), [16, 8, 2])), 0)
bop_6018 = relay.subtract(uop_5980.astype('int8'), relay.reshape(uop_5991.astype('int8'), relay.shape_of(uop_5980))) # shape=(15, 9, 3)
var_6024 = relay.var("var_6024", dtype = "float32", shape = (15, 9, 3))#candidate|6024|(15, 9, 3)|var|float32
bop_6025 = relay.left_shift(uop_5980.astype('int32'), relay.reshape(var_6024.astype('int32'), relay.shape_of(uop_5980))) # shape=(15, 9, 3)
output = relay.Tuple([bop_5923,call_5944,call_5952,call_5970,call_5995,bop_6002,call_6015,bop_6018,bop_6025,])
output2 = relay.Tuple([bop_5926,call_5945,call_5953,call_5971,call_5996,bop_6005,call_6016,bop_6018,bop_6025,])
F = relay.Function([var_5922,var_5963,var_6024,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5922,var_5963,var_6024,], output2)
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
