import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_9 = relay.const([[[2.416059],[-7.381802],[6.162250],[8.721513],[-4.121889],[-5.915325],[6.123298],[5.174847],[3.704718]],[[3.023993],[0.635556],[4.712174],[-5.164932],[-8.525282],[0.723308],[-0.784558],[2.899169],[9.220117]],[[-2.816439],[-0.336563],[-5.819990],[-9.765501],[9.370284],[2.873517],[-0.149590],[-8.130678],[-8.081557]],[[-5.116705],[-5.294043],[-9.950998],[-5.083035],[-4.807091],[9.041558],[-2.795874],[-9.810823],[6.388373]],[[-0.027486],[-7.263038],[8.905464],[-0.848852],[8.029863],[-3.844071],[9.332077],[-2.374745],[4.175829]],[[8.002042],[-6.592973],[1.703532],[5.232998],[5.615819],[-4.430167],[2.141113],[-9.978929],[-0.878456]],[[6.222277],[5.814370],[2.656441],[4.560422],[-6.242358],[1.084364],[-2.671702],[-7.029107],[-5.488941]],[[6.105150],[1.463579],[-3.158742],[9.266663],[-1.515986],[2.734667],[0.788524],[-3.254082],[8.114329]],[[-6.609637],[-3.485968],[5.854088],[-4.046091],[-0.297568],[-2.051005],[-7.190624],[8.713276],[-3.852186]],[[8.223217],[3.062467],[8.343556],[2.531162],[8.487260],[9.794648],[4.627314],[6.965208],[-4.090806]],[[4.799332],[3.304799],[1.645791],[7.912526],[5.815141],[-4.572451],[-8.584679],[6.710722],[4.410021]],[[-1.333840],[2.421927],[-6.472646],[0.812278],[9.206755],[6.385361],[9.980330],[-8.411508],[8.954980]],[[-8.191629],[-2.801911],[2.919289],[4.334857],[-3.312844],[4.825301],[3.636631],[-2.903310],[6.532843]]], dtype = "float64")#candidate|9|(13, 9, 1)|const|float64
uop_10 = relay.cos(const_9.astype('float64')) # shape=(13, 9, 1)
uop_16 = relay.atanh(uop_10.astype('float32')) # shape=(13, 9, 1)
output = uop_16
output2 = uop_16
func_21 = relay.Function([], output)
mod['func_21'] = func_21
mod = relay.transform.InferType()(mod)
output = func_21()
func_22 = relay.Function([], output)
mutated_mod['func_22'] = func_22
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_52 = func_21_call()
call_53 = func_21_call()
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_54 = func_21_call()
call_55 = func_21_call()
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_60 = func_21_call()
call_61 = func_21_call()
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_66 = func_21_call()
call_67 = func_21_call()
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_71 = func_21_call()
call_72 = func_21_call()
output = relay.Tuple([call_52,call_54,call_60,call_66,call_71,])
output2 = relay.Tuple([call_53,call_55,call_61,call_67,call_72,])
func_76 = relay.Function([], output)
mod['func_76'] = func_76
mod = relay.transform.InferType()(mod)
output = func_76()
func_77 = relay.Function([], output)
mutated_mod['func_77'] = func_77
mutated_mod = relay.transform.InferType()(mutated_mod)
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_101 = relay.TupleGetItem(func_76_call(), 4)
call_102 = relay.TupleGetItem(func_77_call(), 4)
output = call_101
output2 = call_102
func_122 = relay.Function([], output)
mod['func_122'] = func_122
mod = relay.transform.InferType()(mod)
output = func_122()
func_123 = relay.Function([], output)
mutated_mod['func_123'] = func_123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_136 = func_21_call()
call_137 = func_21_call()
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_143 = func_21_call()
call_144 = func_21_call()
output = relay.Tuple([call_136,call_143,])
output2 = relay.Tuple([call_137,call_144,])
func_155 = relay.Function([], output)
mod['func_155'] = func_155
mod = relay.transform.InferType()(mod)
output = func_155()
func_156 = relay.Function([], output)
mutated_mod['func_156'] = func_156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_183 = func_122_call()
call_184 = func_122_call()
output = relay.Tuple([call_183,])
output2 = relay.Tuple([call_184,])
func_185 = relay.Function([], output)
mod['func_185'] = func_185
mod = relay.transform.InferType()(mod)
mutated_mod['func_185'] = func_185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_185_call = mutated_mod.get_global_var('func_185')
call_186 = func_185_call()
output = call_186
func_187 = relay.Function([], output)
mutated_mod['func_187'] = func_187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_191 = relay.TupleGetItem(func_155_call(), 1)
call_192 = relay.TupleGetItem(func_156_call(), 1)
output = relay.Tuple([call_191,])
output2 = relay.Tuple([call_192,])
func_200 = relay.Function([], output)
mod['func_200'] = func_200
mod = relay.transform.InferType()(mod)
output = func_200()
func_201 = relay.Function([], output)
mutated_mod['func_201'] = func_201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_225 = func_21_call()
call_226 = func_21_call()
func_185_call = mod.get_global_var('func_185')
func_187_call = mutated_mod.get_global_var('func_187')
call_237 = relay.TupleGetItem(func_185_call(), 0)
call_238 = relay.TupleGetItem(func_187_call(), 0)
func_185_call = mod.get_global_var('func_185')
func_187_call = mutated_mod.get_global_var('func_187')
call_244 = relay.TupleGetItem(func_185_call(), 0)
call_245 = relay.TupleGetItem(func_187_call(), 0)
output = relay.Tuple([call_225,call_237,call_244,])
output2 = relay.Tuple([call_226,call_238,call_245,])
func_247 = relay.Function([], output)
mod['func_247'] = func_247
mod = relay.transform.InferType()(mod)
output = func_247()
func_248 = relay.Function([], output)
mutated_mod['func_248'] = func_248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_247_call = mod.get_global_var('func_247')
func_248_call = mutated_mod.get_global_var('func_248')
call_290 = relay.TupleGetItem(func_247_call(), 2)
call_291 = relay.TupleGetItem(func_248_call(), 2)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_302 = func_122_call()
call_303 = func_122_call()
output = relay.Tuple([call_290,call_302,])
output2 = relay.Tuple([call_291,call_303,])
func_308 = relay.Function([], output)
mod['func_308'] = func_308
mod = relay.transform.InferType()(mod)
mutated_mod['func_308'] = func_308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_308_call = mutated_mod.get_global_var('func_308')
call_309 = func_308_call()
output = call_309
func_310 = relay.Function([], output)
mutated_mod['func_310'] = func_310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_185_call = mod.get_global_var('func_185')
func_187_call = mutated_mod.get_global_var('func_187')
call_339 = relay.TupleGetItem(func_185_call(), 0)
call_340 = relay.TupleGetItem(func_187_call(), 0)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_353 = func_21_call()
call_354 = func_21_call()
bop_355 = relay.logical_xor(call_353.astype('uint32'), relay.reshape(call_339.astype('uint32'), relay.shape_of(call_353))) # shape=(13, 9, 1)
bop_358 = relay.logical_xor(call_354.astype('uint32'), relay.reshape(call_340.astype('uint32'), relay.shape_of(call_354))) # shape=(13, 9, 1)
output = bop_355
output2 = bop_358
func_371 = relay.Function([], output)
mod['func_371'] = func_371
mod = relay.transform.InferType()(mod)
output = func_371()
func_372 = relay.Function([], output)
mutated_mod['func_372'] = func_372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_406 = relay.TupleGetItem(func_155_call(), 1)
call_407 = relay.TupleGetItem(func_156_call(), 1)
uop_408 = relay.sinh(call_406.astype('float32')) # shape=(13, 9, 1)
uop_410 = relay.sinh(call_407.astype('float32')) # shape=(13, 9, 1)
output = relay.Tuple([uop_408,])
output2 = relay.Tuple([uop_410,])
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
const_470 = relay.const(8.959878, dtype = "float32")#candidate|470|()|const|float32
var_471 = relay.var("var_471", dtype = "float32", shape = (8, 10, 8))#candidate|471|(8, 10, 8)|var|float32
bop_472 = relay.floor_mod(const_470.astype('float32'), var_471.astype('float32')) # shape=(8, 10, 8)
output = bop_472
output2 = bop_472
func_475 = relay.Function([var_471,], output)
mod['func_475'] = func_475
mod = relay.transform.InferType()(mod)
var_476 = relay.var("var_476", dtype = "float32", shape = (8, 10, 8))#candidate|476|(8, 10, 8)|var|float32
output = func_475(var_476)
func_477 = relay.Function([var_476], output)
mutated_mod['func_477'] = func_477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_247_call = mod.get_global_var('func_247')
func_248_call = mutated_mod.get_global_var('func_248')
call_489 = relay.TupleGetItem(func_247_call(), 0)
call_490 = relay.TupleGetItem(func_248_call(), 0)
output = relay.Tuple([call_489,])
output2 = relay.Tuple([call_490,])
func_493 = relay.Function([], output)
mod['func_493'] = func_493
mod = relay.transform.InferType()(mod)
output = func_493()
func_494 = relay.Function([], output)
mutated_mod['func_494'] = func_494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_499 = func_21_call()
call_500 = func_21_call()
output = relay.Tuple([call_499,])
output2 = relay.Tuple([call_500,])
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
func_371_call = mod.get_global_var('func_371')
func_372_call = mutated_mod.get_global_var('func_372')
call_536 = func_371_call()
call_537 = func_371_call()
var_541 = relay.var("var_541", dtype = "uint32", shape = (13, 9, 9))#candidate|541|(13, 9, 9)|var|uint32
bop_542 = relay.right_shift(call_536.astype('uint16'), var_541.astype('uint16')) # shape=(13, 9, 9)
bop_545 = relay.right_shift(call_537.astype('uint16'), var_541.astype('uint16')) # shape=(13, 9, 9)
func_308_call = mod.get_global_var('func_308')
func_310_call = mutated_mod.get_global_var('func_310')
call_549 = relay.TupleGetItem(func_308_call(), 0)
call_550 = relay.TupleGetItem(func_310_call(), 0)
uop_553 = relay.exp(bop_542.astype('float32')) # shape=(13, 9, 9)
uop_555 = relay.exp(bop_545.astype('float32')) # shape=(13, 9, 9)
func_493_call = mod.get_global_var('func_493')
func_494_call = mutated_mod.get_global_var('func_494')
call_558 = relay.TupleGetItem(func_493_call(), 0)
call_559 = relay.TupleGetItem(func_494_call(), 0)
output = relay.Tuple([call_549,uop_553,call_558,])
output2 = relay.Tuple([call_550,uop_555,call_559,])
func_565 = relay.Function([var_541,], output)
mod['func_565'] = func_565
mod = relay.transform.InferType()(mod)
mutated_mod['func_565'] = func_565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_566 = relay.var("var_566", dtype = "uint32", shape = (13, 9, 9))#candidate|566|(13, 9, 9)|var|uint32
func_565_call = mutated_mod.get_global_var('func_565')
call_567 = func_565_call(var_566)
output = call_567
func_568 = relay.Function([var_566], output)
mutated_mod['func_568'] = func_568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_584 = func_122_call()
call_585 = func_122_call()
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_602 = relay.TupleGetItem(func_155_call(), 1)
call_603 = relay.TupleGetItem(func_156_call(), 1)
output = relay.Tuple([call_584,call_602,])
output2 = relay.Tuple([call_585,call_603,])
func_631 = relay.Function([], output)
mod['func_631'] = func_631
mod = relay.transform.InferType()(mod)
output = func_631()
func_632 = relay.Function([], output)
mutated_mod['func_632'] = func_632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_371_call = mod.get_global_var('func_371')
func_372_call = mutated_mod.get_global_var('func_372')
call_639 = func_371_call()
call_640 = func_371_call()
func_475_call = mod.get_global_var('func_475')
func_477_call = mutated_mod.get_global_var('func_477')
var_655 = relay.var("var_655", dtype = "float32", shape = (640,))#candidate|655|(640,)|var|float32
call_654 = func_475_call(relay.reshape(var_655.astype('float32'), [8, 10, 8]))
call_656 = func_475_call(relay.reshape(var_655.astype('float32'), [8, 10, 8]))
func_308_call = mod.get_global_var('func_308')
func_310_call = mutated_mod.get_global_var('func_310')
call_662 = relay.TupleGetItem(func_308_call(), 0)
call_663 = relay.TupleGetItem(func_310_call(), 0)
output = relay.Tuple([call_639,call_654,var_655,call_662,])
output2 = relay.Tuple([call_640,call_656,var_655,call_663,])
func_664 = relay.Function([var_655,], output)
mod['func_664'] = func_664
mod = relay.transform.InferType()(mod)
mutated_mod['func_664'] = func_664
mutated_mod = relay.transform.InferType()(mutated_mod)
var_665 = relay.var("var_665", dtype = "float32", shape = (640,))#candidate|665|(640,)|var|float32
func_664_call = mutated_mod.get_global_var('func_664')
call_666 = func_664_call(var_665)
output = call_666
func_667 = relay.Function([var_665], output)
mutated_mod['func_667'] = func_667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_493_call = mod.get_global_var('func_493')
func_494_call = mutated_mod.get_global_var('func_494')
call_838 = relay.TupleGetItem(func_493_call(), 0)
call_839 = relay.TupleGetItem(func_494_call(), 0)
func_185_call = mod.get_global_var('func_185')
func_187_call = mutated_mod.get_global_var('func_187')
call_845 = relay.TupleGetItem(func_185_call(), 0)
call_846 = relay.TupleGetItem(func_187_call(), 0)
uop_855 = relay.sin(call_845.astype('float64')) # shape=(13, 9, 1)
uop_857 = relay.sin(call_846.astype('float64')) # shape=(13, 9, 1)
func_200_call = mod.get_global_var('func_200')
func_201_call = mutated_mod.get_global_var('func_201')
call_858 = relay.TupleGetItem(func_200_call(), 0)
call_859 = relay.TupleGetItem(func_201_call(), 0)
bop_868 = relay.right_shift(call_838.astype('int16'), relay.reshape(uop_855.astype('int16'), relay.shape_of(call_838))) # shape=(13, 9, 1)
bop_871 = relay.right_shift(call_839.astype('int16'), relay.reshape(uop_857.astype('int16'), relay.shape_of(call_839))) # shape=(13, 9, 1)
output = relay.Tuple([call_858,bop_868,])
output2 = relay.Tuple([call_859,bop_871,])
func_887 = relay.Function([], output)
mod['func_887'] = func_887
mod = relay.transform.InferType()(mod)
output = func_887()
func_888 = relay.Function([], output)
mutated_mod['func_888'] = func_888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_897 = func_122_call()
call_898 = func_122_call()
uop_903 = relay.acosh(call_897.astype('float32')) # shape=(13, 9, 1)
uop_905 = relay.acosh(call_898.astype('float32')) # shape=(13, 9, 1)
func_247_call = mod.get_global_var('func_247')
func_248_call = mutated_mod.get_global_var('func_248')
call_911 = relay.TupleGetItem(func_247_call(), 2)
call_912 = relay.TupleGetItem(func_248_call(), 2)
func_664_call = mod.get_global_var('func_664')
func_667_call = mutated_mod.get_global_var('func_667')
const_917 = relay.const([-6.886112,-5.452405,3.734782,-6.564432,-5.856314,-1.894619,-6.699091,-2.787559,9.962701,-6.325819,-8.509394,-0.836924,-9.351239,-4.573417,-2.717572,8.486589,3.099503,-1.501780,9.723397,3.017376,3.115972,-8.751285,6.115922,-3.092306,8.374068,-3.831663,4.762491,3.288336,-1.527005,-7.279526,-0.873651,5.648901,0.088323,-9.917445,8.156490,-8.208843,-7.992291,-2.840197,0.191956,-3.829108,-9.915474,-9.091389,-1.238750,7.412957,8.384481,0.341759,1.401375,4.191573,-6.670404,7.486503,0.772992,9.082738,2.002821,6.050806,-5.814801,3.507893,0.866154,4.749247,8.934129,-6.869246,-1.514299,-8.294435,-0.614323,-8.658866,-2.345815,-4.066279,4.201578,9.993587,-4.005927,8.830152,-3.925265,0.353973,7.411010,9.990705,4.038378,9.124562,-3.825947,-4.131963,-5.520133,5.853877,-8.244674,-7.101183,2.570703,-5.539202,9.807050,7.414005,-5.363206,7.649200,3.940591,-1.315806,-1.455004,-8.471353,-7.715266,5.305495,3.344554,1.246674,9.411871,2.722489,1.252592,-8.498320,1.245839,-9.469897,-5.950627,9.328146,2.764678,-6.177961,-4.080901,-7.194507,5.298839,6.456009,-6.818468,9.465484,-3.273127,7.529530,-9.716894,-6.943684,9.510429,-3.360295,-0.889904,9.597551,9.785180,0.638013,-2.276802,-9.127233,-5.505879,-7.548742,-9.980552,-9.772431,-1.158227,-5.221258,5.652765,-9.702737,-8.921839,-1.001847,1.032468,-9.800180,9.395346,-0.598630,7.261449,-3.213862,-6.604997,-3.641495,-4.681333,7.019605,-5.465273,6.127204,0.950370,-5.945204,-4.480903,-3.749148,-4.439436,1.778261,9.465281,3.717271,-1.499557,-4.165871,-9.901549,-8.451306,2.327365,2.561478,0.904761,6.639469,6.412148,-4.105148,-9.714827,3.643343,6.281273,-1.844301,-2.437722,2.258376,2.534455,5.573347,2.455315,-8.765659,7.042510,-3.082204,0.645316,4.751008,-2.195259,-1.515197,7.267088,8.011170,-4.621734,3.732616,-8.455420,-1.301305,-3.390467,0.926637,4.036636,-4.803436,-2.387276,9.775068,-4.258993,-7.720866,8.044980,6.681179,-3.882828,9.418349,-8.832010,4.248136,-0.157814,8.822721,5.994585,-8.865947,-4.503922,0.302355,1.003635,-7.539311,-8.335502,-3.293941,-5.691701,-3.549445,8.568630,9.683980,-1.611583,-5.091232,-3.386711,7.915853,-9.010884,-8.900267,-0.975276,9.826776,5.807867,3.433055,-9.833625,5.303052,1.171104,4.121175,6.123465,-3.326516,8.654261,-2.992028,-0.493445,3.597092,1.624147,-7.459079,-8.512359,-1.667053,1.248548,3.949534,5.632869,-6.224182,-5.850628,1.074091,9.850489,1.699284,-0.844486,-0.528884,2.608722,-7.204165,-3.174097,-3.184148,-7.921123,-8.984850,-5.350030,-2.881915,-6.219069,-3.326048,-3.439202,-7.403468,3.213311,4.384868,-2.160452,7.232710,4.264303,-9.254380,-3.543917,-0.715466,4.945864,-7.947563,-3.034850,-9.997590,-3.060915,0.602089,-7.987595,-1.963134,8.705937,-1.787776,6.396259,3.931617,7.694685,-1.387238,-5.469238,-1.555359,4.061025,1.322684,1.501708,-2.820378,-0.901181,7.868018,-8.044403,9.464648,9.333516,2.679913,7.804073,8.706001,-8.156775,-8.907373,4.919528,1.665423,7.946100,-2.559016,-2.971367,-5.525140,0.993602,9.594598,3.098680,9.326701,-2.929764,-4.605778,-3.150516,-4.956015,3.482497,7.118987,-6.954864,-9.128944,-9.871418,-1.518484,9.400750,3.530763,-6.043829,-2.128807,6.433327,-8.083303,-3.921276,8.146256,7.050929,-5.951716,-1.111002,6.459840,-0.175195,0.422845,-3.045011,5.031291,-6.737484,-0.048092,8.864674,2.667804,2.357181,8.605465,-6.384903,-7.578661,-1.070343,-2.420442,-8.446717,5.149748,4.736037,6.174349,5.316764,-0.800501,-8.100314,-4.305075,6.726231,-1.266040,-6.442652,8.300730,1.779055,-2.679093,-3.996628,-2.596905,-7.830764,5.945529,-3.902610,3.432082,1.617350,-7.497728,6.272664,7.196741,-8.117577,3.949540,7.574094,2.919656,-7.992099,4.053323,-6.987237,9.508884,2.537063,4.006115,-1.347138,8.616307,-8.389697,9.942498,5.411858,-4.271301,-9.239514,-2.336765,-9.291346,-8.116871,4.736658,6.675733,-4.209549,-3.359055,3.097319,0.803044,-9.949963,0.461078,-6.888895,-8.995013,-9.380050,3.973137,-1.491473,-6.309949,7.629802,8.849655,-2.417050,1.835074,-9.154979,7.766208,7.629793,9.886339,1.164481,-7.960840,2.702063,2.075702,4.604046,-8.402613,-7.303328,1.600243,-0.499234,-4.157391,7.562178,4.807299,8.780950,-6.361799,0.879236,4.708842,-7.725245,7.809521,-3.324054,9.733601,5.446665,-9.182814,6.942909,-4.258093,-7.573744,-3.081248,-5.096376,9.654030,-0.748218,-8.278114,6.203310,4.946567,5.120383,2.107322,5.980213,4.127782,9.890601,4.022301,3.259491,-8.761027,-9.042733,-9.088431,-9.314969,8.107050,9.139858,-7.365707,6.378517,-7.170613,-7.569542,-0.456477,1.388031,9.542584,7.928821,0.585697,-9.762175,8.895013,-7.861120,1.209121,4.965535,-3.142066,-1.878126,-3.505947,-7.501074,-4.630990,-9.028008,-9.733569,-2.722612,-1.894469,-7.381255,7.636555,6.737984,-6.787016,-6.739536,-0.576579,-4.749903,-2.685352,-6.764052,-4.757773,2.049144,3.850315,7.121595,0.121872,5.852558,-9.419849,3.992432,-4.047220,-1.047468,0.889878,-3.141400,-8.617222,-3.410733,6.910780,2.826941,5.200796,-7.632808,8.689617,-6.742873,-3.274674,-4.513199,-5.369451,-1.453461,3.305271,8.500969,4.059443,-6.887038,-7.626723,-8.820394,3.694259,4.270386,-2.813030,-9.626755,8.590841,7.521031,-4.095851,-6.167204,6.269337,-4.084260,8.756521,1.456147,4.477153,2.080727,-7.320760,-3.884956,2.556954,-0.744787,1.004187,4.894793,-8.101364,-4.898126,4.609329,3.744671,9.522277,4.833913,5.773680,1.699238,-9.959424,-8.082699,-2.159459,9.739346,-2.705459,-3.211813,-2.751538,-9.243736,-9.299988,2.205063,-7.659744,-7.313226,-9.432099,-5.366800,5.732053,9.147815,-1.064835,-5.017013,-0.028928,6.049800,-8.385654,-1.223869,1.624064,9.819277,-5.578915,0.707247,7.017603,-5.184974,4.336443,2.114335,9.095023,6.408397,-6.410497,-8.002144,7.429419,8.822067,2.903193,-7.563190,-6.202787,-8.650655,-3.197407,7.346483,-9.843544,-1.766225,8.490041,-2.133918,-9.501999,-0.960144,0.840063,4.105288,-1.199696,-6.113343,-4.346376,5.949203,-1.144824,6.551544,9.238106,-5.779293,6.077279,-1.340716,-9.465909,4.213300,-8.420496,3.091595,-7.305241,-7.340646,8.289340,6.929908,8.619134,2.575588,-5.779709,-1.505021,1.258954,3.287061,5.643845,4.421503,-4.731948,-2.255660,0.514727,5.811063,-0.226181,-0.618750,-9.315923,-4.094497,-8.982314,-6.522423,-2.830587,2.841793,8.146147,-2.665206,-9.905013,5.009222,-2.683135,8.346582,6.857715], dtype = "float32")#candidate|917|(640,)|const|float32
call_916 = relay.TupleGetItem(func_664_call(relay.reshape(const_917.astype('float32'), [640,])), 1)
call_918 = relay.TupleGetItem(func_667_call(relay.reshape(const_917.astype('float32'), [640,])), 1)
bop_924 = relay.logical_and(uop_903.astype('bool'), relay.reshape(call_897.astype('bool'), relay.shape_of(uop_903))) # shape=(13, 9, 1)
bop_927 = relay.logical_and(uop_905.astype('bool'), relay.reshape(call_898.astype('bool'), relay.shape_of(uop_905))) # shape=(13, 9, 1)
func_185_call = mod.get_global_var('func_185')
func_187_call = mutated_mod.get_global_var('func_187')
call_935 = relay.TupleGetItem(func_185_call(), 0)
call_936 = relay.TupleGetItem(func_187_call(), 0)
output = relay.Tuple([call_911,call_916,const_917,bop_924,call_935,])
output2 = relay.Tuple([call_912,call_918,const_917,bop_927,call_936,])
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
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_969 = func_21_call()
call_970 = func_21_call()
uop_971 = relay.asin(call_969.astype('float64')) # shape=(13, 9, 1)
uop_973 = relay.asin(call_970.astype('float64')) # shape=(13, 9, 1)
output = relay.Tuple([uop_971,])
output2 = relay.Tuple([uop_973,])
func_981 = relay.Function([], output)
mod['func_981'] = func_981
mod = relay.transform.InferType()(mod)
output = func_981()
func_982 = relay.Function([], output)
mutated_mod['func_982'] = func_982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_1024 = relay.TupleGetItem(func_501_call(), 0)
call_1025 = relay.TupleGetItem(func_503_call(), 0)
uop_1034 = relay.atan(call_1024.astype('float32')) # shape=(13, 9, 1)
uop_1036 = relay.atan(call_1025.astype('float32')) # shape=(13, 9, 1)
bop_1044 = relay.power(call_1024.astype('float32'), relay.reshape(uop_1034.astype('float32'), relay.shape_of(call_1024))) # shape=(13, 9, 1)
bop_1047 = relay.power(call_1025.astype('float32'), relay.reshape(uop_1036.astype('float32'), relay.shape_of(call_1025))) # shape=(13, 9, 1)
bop_1053 = relay.bitwise_or(bop_1044.astype('uint64'), relay.reshape(uop_1034.astype('uint64'), relay.shape_of(bop_1044))) # shape=(13, 9, 1)
bop_1056 = relay.bitwise_or(bop_1047.astype('uint64'), relay.reshape(uop_1036.astype('uint64'), relay.shape_of(bop_1047))) # shape=(13, 9, 1)
output = bop_1053
output2 = bop_1056
func_1073 = relay.Function([], output)
mod['func_1073'] = func_1073
mod = relay.transform.InferType()(mod)
output = func_1073()
func_1074 = relay.Function([], output)
mutated_mod['func_1074'] = func_1074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_493_call = mod.get_global_var('func_493')
func_494_call = mutated_mod.get_global_var('func_494')
call_1123 = relay.TupleGetItem(func_493_call(), 0)
call_1124 = relay.TupleGetItem(func_494_call(), 0)
output = call_1123
output2 = call_1124
func_1128 = relay.Function([], output)
mod['func_1128'] = func_1128
mod = relay.transform.InferType()(mod)
output = func_1128()
func_1129 = relay.Function([], output)
mutated_mod['func_1129'] = func_1129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1251 = relay.var("var_1251", dtype = "int8", shape = (10, 9, 16))#candidate|1251|(10, 9, 16)|var|int8
const_1252 = relay.const([[[9,10,6,7,-2,-7,-7,10,-7,-9,4,5,-4,-4,1,2],[1,-1,-4,10,7,7,-10,-9,2,9,8,9,-2,-4,8,5],[6,6,-8,-7,4,10,-3,-2,7,-10,7,8,4,-4,-7,-2],[9,-4,6,4,5,5,1,2,-1,4,4,1,3,2,6,-3],[-4,4,8,10,-1,9,2,-1,-6,5,6,-9,1,9,5,-4],[8,-9,-5,-8,-3,8,10,2,-6,-5,-1,1,6,-1,1,10],[-3,-6,7,7,-2,-9,6,-8,6,-3,10,1,4,-6,7,-4],[4,-9,1,3,2,-6,3,9,7,-8,-7,-2,-1,6,4,-8],[-8,-1,4,-4,8,-5,6,-10,-7,2,9,7,-2,-10,2,5]],[[9,-3,-2,1,7,-10,-1,7,-3,4,-1,-4,5,-9,3,1],[2,5,10,-3,-4,-9,-5,3,-5,10,1,9,7,6,-4,2],[-10,-9,4,7,-6,3,5,1,-6,-4,-4,-4,4,9,-7,-5],[9,-7,-7,1,1,7,1,-5,-9,-3,-3,2,-6,-5,-5,10],[-4,6,-1,7,2,-9,-3,1,3,-7,-10,-4,-1,1,-9,9],[-8,-7,4,3,9,1,8,8,-6,8,3,4,2,1,6,7],[4,5,9,4,-3,3,-6,3,-3,2,4,9,3,9,9,5],[9,1,-1,-7,-1,4,-1,-1,-9,-10,9,8,9,-1,-3,-4],[-8,2,2,-2,2,-10,4,-7,4,-5,-7,5,8,6,2,-4]],[[7,-10,5,-1,9,-10,-3,-7,2,-10,-2,-7,-10,-4,5,5],[-3,-8,-8,-7,-10,-1,4,10,7,-5,6,3,-6,-10,-4,2],[1,-10,-9,-5,4,2,1,3,3,-1,1,4,-9,-10,-1,-2],[10,-3,-9,-8,4,10,-1,5,3,10,8,-3,10,3,6,8],[-7,7,-7,10,6,-7,5,10,8,3,-5,6,-10,9,-4,3],[7,-1,6,6,-3,6,6,7,-7,-1,-7,-10,-6,4,-7,3],[-9,-8,6,-5,-10,-7,9,2,6,-8,10,1,-8,-8,-4,-9],[-5,-7,3,-10,-5,1,2,-9,7,-1,-7,5,-9,-10,-5,-7],[-6,-1,-8,-3,-9,8,6,-2,-7,1,7,-9,10,1,-10,4]],[[-5,-6,6,-8,4,8,3,4,-3,6,-3,-6,6,-6,8,-2],[-7,-9,-8,9,3,5,-5,10,3,8,10,-9,-3,-3,-7,5],[-3,-6,-1,4,-2,2,7,-7,-7,-8,-1,5,2,-5,5,2],[4,1,-6,-9,-6,-8,-4,-5,2,-8,-2,4,-1,2,1,-3],[5,2,9,-10,4,-9,-2,7,-10,6,-8,-6,1,4,-4,-9],[-1,10,2,-6,-7,5,9,-5,9,-9,-2,-5,-4,9,5,9],[-8,-5,-1,7,6,-9,-5,4,-6,10,-1,-2,-5,-3,8,-8],[2,-7,6,1,5,9,-4,4,7,7,1,2,-2,-8,-6,-7],[10,1,5,8,-10,9,-9,4,-9,5,-2,-3,2,3,8,8]],[[3,1,-9,-9,5,5,-3,1,9,9,3,-4,-5,-2,-8,-8],[8,-8,-10,10,-4,-9,-3,8,-6,-5,-1,1,7,-9,-4,7],[-8,-2,3,4,-6,-6,-5,3,1,10,7,8,-7,-3,3,6],[7,2,8,7,10,3,8,-7,-5,3,-8,-8,-5,7,-10,-1],[-9,-5,8,-2,-7,-4,-2,6,-9,9,-9,2,7,3,-2,-2],[-9,9,1,8,8,-5,-4,-10,-1,8,-6,-3,2,8,-4,7],[7,1,-9,8,-10,10,5,4,-8,3,7,-7,-5,4,-5,-3],[9,2,2,7,-10,-5,-8,-10,-3,10,-2,8,-4,-7,3,1],[3,-10,-3,4,-6,10,-7,-10,-3,10,-9,-3,1,2,-9,8]],[[8,4,4,5,-8,-4,5,-7,4,6,-8,-8,8,-4,5,-6],[9,2,-9,-3,-4,-3,-1,-9,-8,2,-1,-6,10,-5,-2,-6],[2,-4,9,-7,-6,-1,-1,-4,5,-6,6,-7,-1,-1,-3,4],[7,8,9,8,-8,-4,9,-9,-6,3,6,-8,10,10,6,-1],[-5,-10,4,2,9,10,-8,4,-5,-5,5,-8,3,-10,-3,4],[2,4,2,-10,4,8,-1,5,7,5,-3,9,-10,-7,-4,2],[-6,1,-2,8,-3,9,1,9,2,-2,-8,3,1,-2,-2,10],[3,-8,4,-3,4,-10,4,7,-3,4,-1,1,6,7,-10,-8],[8,-7,1,9,2,4,-9,5,-7,5,-4,10,-2,2,5,4]],[[-5,8,-5,-3,6,-4,-6,7,7,-3,-8,5,-1,-3,-6,-10],[2,-6,4,-1,-7,-3,5,10,2,5,6,2,-4,4,4,10],[3,-10,-7,9,-7,1,-2,5,2,-6,7,-8,2,2,7,9],[-8,-8,9,3,10,9,-2,-8,2,5,-1,-2,-4,-9,4,2],[7,1,9,-4,-5,-3,-9,1,6,-1,-8,1,7,4,10,-7],[10,-6,9,10,-5,3,5,-5,2,1,1,4,4,1,-8,4],[6,6,10,-1,8,-10,10,7,3,3,-10,6,-7,-1,-5,10],[4,9,2,10,-6,7,8,-7,2,9,-9,7,1,-8,4,10],[-5,-2,8,1,4,9,1,-5,8,-6,-8,-2,2,7,-7,2]],[[5,1,7,7,-9,5,6,3,-7,-2,2,4,-3,10,8,-4],[-7,6,6,-9,-2,4,-6,2,4,8,6,-1,-5,-9,-2,-7],[9,-5,7,-9,-8,-6,10,10,2,3,2,-8,-3,-1,1,4],[-1,6,-2,-6,-10,5,-10,5,2,9,1,2,-6,9,-3,7],[1,-2,8,3,10,-9,2,-2,3,-10,-3,-6,-7,6,7,6],[7,-3,7,5,4,10,8,-4,-5,5,7,7,-6,8,6,-3],[1,10,-2,7,-8,5,9,9,4,-4,-5,6,1,5,7,10],[6,8,-6,-7,10,-4,-1,-4,9,7,6,5,7,-7,-10,4],[9,-5,9,-1,3,-9,-8,-9,-1,-1,10,-6,-6,3,2,-1]],[[3,5,-7,10,-4,4,10,-1,10,7,7,-8,8,8,-3,10],[6,-6,4,1,-5,-9,10,5,9,-1,9,9,5,7,8,-5],[-5,-7,9,6,-5,-8,-5,5,6,10,9,3,9,-3,-9,3],[-9,2,8,-9,-3,8,-9,1,10,5,3,3,-9,-10,3,2],[-4,8,-2,-5,-4,-10,5,-2,-3,4,6,9,-4,-4,4,8],[2,-2,-5,-7,7,3,9,4,-4,-9,6,6,10,-6,7,4],[10,-2,-10,-3,8,-8,-5,2,-3,-2,10,-8,7,5,-7,-1],[-5,-1,4,4,4,-3,-8,-10,6,1,-7,8,-2,8,-4,-6],[4,7,-3,-3,5,-8,1,-6,-8,-4,-6,3,-5,-7,1,-9]],[[-1,4,7,3,-3,7,-6,10,-9,-3,5,1,6,-1,1,4],[6,8,-5,-7,1,-10,-6,5,5,8,-3,-1,9,7,-4,2],[9,3,-2,-2,-4,-1,5,6,1,1,5,6,6,3,-4,-9],[-6,9,-1,-10,7,5,-5,-3,5,4,-8,3,4,3,1,-5],[2,-7,-8,10,-8,7,-6,-4,4,10,-8,7,6,-4,-2,6],[-4,9,-9,5,-3,-3,-5,-1,-6,-3,3,8,8,8,2,5],[6,6,-2,1,5,8,2,9,10,2,-1,-3,-4,-10,5,-10],[9,4,-9,9,-10,4,-6,-8,8,-8,-10,-10,1,1,-5,-7],[-7,8,-8,1,-3,10,1,-6,7,6,4,-4,-5,-1,7,7]]], dtype = "int8")#candidate|1252|(10, 9, 16)|const|int8
bop_1253 = relay.bitwise_and(var_1251.astype('int8'), relay.reshape(const_1252.astype('int8'), relay.shape_of(var_1251))) # shape=(10, 9, 16)
func_200_call = mod.get_global_var('func_200')
func_201_call = mutated_mod.get_global_var('func_201')
call_1276 = relay.TupleGetItem(func_200_call(), 0)
call_1277 = relay.TupleGetItem(func_201_call(), 0)
func_664_call = mod.get_global_var('func_664')
func_667_call = mutated_mod.get_global_var('func_667')
const_1297 = relay.const([[0.859418,2.256601,1.288938,-8.374838],[-8.792537,4.902773,8.828246,6.444751],[4.800238,-2.733149,6.072653,-5.058315],[-8.192632,-6.582304,-1.864786,5.683978],[0.356023,2.064188,-6.428116,-8.060708],[0.218309,4.758957,-1.697546,6.277706],[-9.261144,-2.352547,-6.445069,-2.944118],[-1.406750,6.773091,-2.358423,8.594257],[-4.071404,6.102262,-2.073587,0.612190],[7.100937,-7.571924,-0.563000,9.573038],[4.715237,-2.451998,-2.653665,-8.137829],[-6.235495,-6.451269,-6.090872,-9.758674],[-0.148801,1.486204,6.267471,-5.303666],[3.792609,-1.526823,-9.320370,8.252410],[1.038110,2.839475,-8.334616,8.301974],[-0.273482,1.958319,5.519036,4.001755],[2.810943,-0.474943,4.399107,0.745019],[6.005269,-8.997506,0.667581,4.123808],[-7.377006,6.337488,-9.364781,8.785374],[-5.340359,1.943562,-9.555921,0.097457],[7.724097,-0.428832,6.874352,5.080456],[6.527279,-0.539943,8.626982,2.497337],[1.255827,-0.955480,7.749940,-6.039371],[5.190624,5.631234,-0.755470,7.899227],[-7.551362,-4.498690,-0.419501,-8.944846],[-3.107170,-3.038587,-3.327085,8.080743],[-2.455223,6.065574,8.343066,8.313300],[1.541801,-3.696023,-1.952071,9.815844],[3.514687,-7.044693,-0.879148,1.423189],[0.330114,-8.048542,8.372717,0.256233],[-0.263788,-3.293589,-5.554730,-2.119616],[-4.726343,2.989535,-2.502657,-1.389032],[9.969726,7.882305,2.164251,-3.710965],[3.792317,4.206038,-2.035258,-2.227812],[8.459348,-0.518010,4.592100,-1.068844],[6.651556,-6.660422,-1.868483,8.907955],[5.422135,3.171785,0.218101,6.545796],[4.612020,1.675154,-3.710439,-9.585819],[-1.182668,7.467155,9.481309,-5.341444],[-2.667917,-2.022139,6.223280,-2.964612],[3.245816,0.089183,1.922450,7.713043],[2.899292,-1.671268,-8.008844,-3.057477],[3.754950,-8.466270,4.640582,0.101801],[8.565096,-1.253298,9.587788,2.755748],[7.626002,4.462884,-3.144644,0.557809],[4.759690,3.004003,-9.255859,4.452415],[8.427412,-1.946994,-3.985247,-5.744208],[5.347601,-8.197415,5.787972,7.729123],[-4.612708,1.414645,6.241474,0.272631],[-0.636147,4.031608,-8.547819,-3.228241],[-7.745657,-4.722768,-6.233512,1.975069],[4.563536,-0.594669,7.048443,0.454145],[-8.199788,-0.475317,2.220261,4.150771],[-1.955833,-1.675374,3.230567,9.994920],[4.805217,-6.395367,-9.870454,-8.874568],[5.653723,2.432089,-7.394112,-1.188169],[1.419490,0.296636,-3.158242,5.127159],[4.160914,1.080012,-5.381512,-3.743077],[-1.876805,-8.066896,-9.294741,9.938618],[4.126829,7.560806,5.239214,1.247802],[-6.056068,-0.479449,9.650363,-3.185029],[6.888281,5.966495,-8.718899,-7.279951],[-5.864265,6.930591,1.966231,-4.959056],[0.117901,-5.137450,7.464438,-5.685260],[-0.233326,8.372242,-0.792686,-8.504432],[7.215587,9.509794,-7.867438,6.619250],[-0.634103,8.402244,2.960916,8.738973],[8.618079,1.948621,5.636506,6.195635],[-9.339253,2.581640,-7.565201,5.349233],[0.312681,0.960353,-5.695311,-1.825580],[6.896209,-9.043895,5.772751,-2.609430],[7.988957,5.828413,3.588434,6.939539],[4.549712,-8.437875,-4.649297,-8.667651],[-9.630818,5.247710,-8.442540,-7.202358],[-7.648142,-2.275846,-7.508487,-7.288582],[-5.188358,-8.487432,-7.787364,-0.928726],[-7.769349,1.486823,-2.827607,-6.690095],[4.902564,8.776779,9.225597,-6.426386],[-1.063096,7.868624,2.866728,-3.967850],[0.632769,7.446797,-3.341300,-4.370943],[-9.287787,-1.208988,9.328767,5.648332],[-0.642667,-6.851232,-7.989197,5.170451],[3.827314,7.578987,3.384860,-7.689102],[-1.487683,-7.606163,0.380978,9.006853],[6.772690,-8.836911,-7.398320,3.377095],[-5.246616,-9.159090,-0.848159,3.856374],[-0.238906,-2.973893,4.110255,7.650592],[-0.067359,-9.551005,-1.660967,7.818092],[2.231679,-6.317151,-2.698782,7.525416],[6.827203,6.276293,6.828544,6.414229],[-8.429001,7.308498,-0.381636,8.809096],[3.136253,2.248776,-2.488498,6.502981],[-5.795927,9.491350,3.855256,-5.792710],[5.689696,7.451900,-2.715536,-3.015998],[-9.922268,-6.655381,-0.020100,-9.568108],[-2.868953,9.287180,-3.401024,-7.815618],[-8.974835,2.718670,-1.050498,-7.016103],[-8.135417,6.889837,-8.550510,2.953812],[2.444082,-1.612597,7.066250,1.719719],[-9.496842,-3.373991,0.126304,0.664607],[1.359359,-2.807680,-6.384029,8.762438],[-2.691251,-8.503905,-3.164789,8.282156],[8.749233,-3.561796,-4.505400,-1.429469],[-8.923806,-4.953480,-1.538150,-9.798041],[-2.366451,1.340440,9.132712,5.415362],[1.850623,6.512590,7.380780,-7.624836],[-0.813994,-3.594050,-3.392490,0.394904],[0.258505,2.131434,7.245501,7.158869],[-6.626718,0.867094,5.049555,2.052409],[-0.576601,6.184627,0.246823,-2.649268],[-1.408202,0.151464,-5.508020,4.971069],[-2.400623,4.021256,-1.244879,9.367957],[0.791846,5.998576,-4.746807,-5.191165],[8.040812,-0.058981,7.644899,-7.562888],[4.849416,-6.562574,-9.084651,-1.786049],[-9.709299,-3.821430,-7.582571,8.056890],[-7.597045,6.003242,4.668799,2.003816],[2.842729,-2.889741,3.454604,-6.544029],[-9.461573,-4.123088,-5.141444,7.779587],[-4.543467,-3.160914,7.723137,-6.008965],[-1.113287,-1.220166,8.874376,-2.312103],[-0.116800,0.957118,8.530935,-5.333821],[3.766699,-2.359627,6.647333,-1.377493],[0.971571,4.531112,9.497715,9.294101],[8.536869,6.272963,4.348141,8.075738],[-9.698228,3.513931,-5.958919,3.091442],[-6.054560,4.664035,9.128123,0.121877],[-9.741242,-2.471199,0.423693,0.763326],[8.283249,2.068324,-3.455846,-7.127912],[-9.003033,-9.128481,-7.501885,-1.832375],[1.829921,-3.393792,6.887133,-7.220095],[-2.440572,4.938390,-5.652657,-6.484428],[-7.584645,-5.207981,-6.578945,7.978025],[7.672525,2.690929,-1.173340,-7.147594],[-8.544047,-7.528733,8.593444,4.706083],[7.204769,5.408332,-6.549230,-7.320220],[8.280069,9.535154,7.202734,-8.188881],[5.500546,-7.409898,6.727092,8.664822],[-5.949414,-1.840173,-6.068727,6.749218],[-0.299863,5.503500,2.871585,7.312851],[3.994897,-5.406965,-4.470262,5.526320],[3.689750,6.621570,-9.636265,-4.653234],[-4.322994,-5.670005,-7.045311,5.617497],[-9.256432,9.881767,-8.398280,8.834145],[-2.479649,-4.305532,-2.903911,-9.977296],[-3.265245,3.643267,-2.169953,5.752017],[-5.469277,-9.946341,6.836322,8.018375],[-9.454106,5.710291,-6.255706,-2.664245],[1.764030,0.155035,-1.785845,7.091316],[3.993511,-1.958810,-3.220781,-4.515831],[7.300596,6.434076,-8.120505,5.224049],[-0.762118,7.041860,0.469215,5.321327],[2.314888,-7.211180,-1.715256,-7.149025],[-2.185965,6.910185,-2.624633,4.991838],[-7.087059,-1.339715,-1.458794,-0.813000],[1.044933,8.051588,3.740763,3.607789],[1.745905,2.674191,5.481205,6.033037],[-8.265413,-5.134458,-2.184853,-5.092402],[-5.995321,-2.975677,-0.391475,6.962102],[-8.342391,-9.749352,4.522321,-5.744687]], dtype = "float32")#candidate|1297|(160, 4)|const|float32
call_1296 = relay.TupleGetItem(func_664_call(relay.reshape(const_1297.astype('float32'), [640,])), 3)
call_1298 = relay.TupleGetItem(func_667_call(relay.reshape(const_1297.astype('float32'), [640,])), 3)
output = relay.Tuple([bop_1253,call_1276,call_1296,const_1297,])
output2 = relay.Tuple([bop_1253,call_1277,call_1298,const_1297,])
func_1299 = relay.Function([var_1251,], output)
mod['func_1299'] = func_1299
mod = relay.transform.InferType()(mod)
var_1300 = relay.var("var_1300", dtype = "int8", shape = (10, 9, 16))#candidate|1300|(10, 9, 16)|var|int8
output = func_1299(var_1300)
func_1301 = relay.Function([var_1300], output)
mutated_mod['func_1301'] = func_1301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_1318 = relay.TupleGetItem(func_155_call(), 1)
call_1319 = relay.TupleGetItem(func_156_call(), 1)
output = relay.Tuple([call_1318,])
output2 = relay.Tuple([call_1319,])
func_1323 = relay.Function([], output)
mod['func_1323'] = func_1323
mod = relay.transform.InferType()(mod)
output = func_1323()
func_1324 = relay.Function([], output)
mutated_mod['func_1324'] = func_1324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_308_call = mod.get_global_var('func_308')
func_310_call = mutated_mod.get_global_var('func_310')
call_1479 = relay.TupleGetItem(func_308_call(), 0)
call_1480 = relay.TupleGetItem(func_310_call(), 0)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_1494 = func_1128_call()
call_1495 = func_1128_call()
func_200_call = mod.get_global_var('func_200')
func_201_call = mutated_mod.get_global_var('func_201')
call_1506 = relay.TupleGetItem(func_200_call(), 0)
call_1507 = relay.TupleGetItem(func_201_call(), 0)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_1508 = func_122_call()
call_1509 = func_122_call()
func_371_call = mod.get_global_var('func_371')
func_372_call = mutated_mod.get_global_var('func_372')
call_1518 = func_371_call()
call_1519 = func_371_call()
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_1524 = relay.TupleGetItem(func_418_call(), 0)
call_1525 = relay.TupleGetItem(func_420_call(), 0)
output = relay.Tuple([call_1479,call_1494,call_1506,call_1508,call_1518,call_1524,])
output2 = relay.Tuple([call_1480,call_1495,call_1507,call_1509,call_1519,call_1525,])
func_1526 = relay.Function([], output)
mod['func_1526'] = func_1526
mod = relay.transform.InferType()(mod)
output = func_1526()
func_1527 = relay.Function([], output)
mutated_mod['func_1527'] = func_1527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_1534 = func_122_call()
call_1535 = func_122_call()
var_1545 = relay.var("var_1545", dtype = "float32", shape = (13, 9, 10))#candidate|1545|(13, 9, 10)|var|float32
bop_1546 = relay.greater_equal(call_1534.astype('bool'), var_1545.astype('bool')) # shape=(13, 9, 10)
bop_1549 = relay.greater_equal(call_1535.astype('bool'), var_1545.astype('bool')) # shape=(13, 9, 10)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
var_1568 = relay.var("var_1568", dtype = "int8", shape = (720, 2))#candidate|1568|(720, 2)|var|int8
call_1567 = relay.TupleGetItem(func_1299_call(relay.reshape(var_1568.astype('int8'), [10, 9, 16])), 3)
call_1569 = relay.TupleGetItem(func_1301_call(relay.reshape(var_1568.astype('int8'), [10, 9, 16])), 3)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_1570 = func_21_call()
call_1571 = func_21_call()
uop_1576 = relay.cosh(call_1534.astype('float32')) # shape=(13, 9, 1)
uop_1578 = relay.cosh(call_1535.astype('float32')) # shape=(13, 9, 1)
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_1589 = relay.TupleGetItem(func_418_call(), 0)
call_1590 = relay.TupleGetItem(func_420_call(), 0)
output = relay.Tuple([bop_1546,call_1567,var_1568,call_1570,uop_1576,call_1589,])
output2 = relay.Tuple([bop_1549,call_1569,var_1568,call_1571,uop_1578,call_1590,])
func_1595 = relay.Function([var_1545,var_1568,], output)
mod['func_1595'] = func_1595
mod = relay.transform.InferType()(mod)
var_1596 = relay.var("var_1596", dtype = "float32", shape = (13, 9, 10))#candidate|1596|(13, 9, 10)|var|float32
var_1597 = relay.var("var_1597", dtype = "int8", shape = (720, 2))#candidate|1597|(720, 2)|var|int8
output = func_1595(var_1596,var_1597,)
func_1598 = relay.Function([var_1596,var_1597,], output)
mutated_mod['func_1598'] = func_1598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_1608 = func_21_call()
call_1609 = func_21_call()
output = call_1608
output2 = call_1609
func_1614 = relay.Function([], output)
mod['func_1614'] = func_1614
mod = relay.transform.InferType()(mod)
output = func_1614()
func_1615 = relay.Function([], output)
mutated_mod['func_1615'] = func_1615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_1633 = func_1128_call()
call_1634 = func_1128_call()
func_664_call = mod.get_global_var('func_664')
func_667_call = mutated_mod.get_global_var('func_667')
var_1647 = relay.var("var_1647", dtype = "float32", shape = (640,))#candidate|1647|(640,)|var|float32
call_1646 = relay.TupleGetItem(func_664_call(relay.reshape(var_1647.astype('float32'), [640,])), 3)
call_1648 = relay.TupleGetItem(func_667_call(relay.reshape(var_1647.astype('float32'), [640,])), 3)
output = relay.Tuple([call_1633,call_1646,var_1647,])
output2 = relay.Tuple([call_1634,call_1648,var_1647,])
func_1649 = relay.Function([var_1647,], output)
mod['func_1649'] = func_1649
mod = relay.transform.InferType()(mod)
mutated_mod['func_1649'] = func_1649
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1650 = relay.var("var_1650", dtype = "float32", shape = (640,))#candidate|1650|(640,)|var|float32
func_1649_call = mutated_mod.get_global_var('func_1649')
call_1651 = func_1649_call(var_1650)
output = call_1651
func_1652 = relay.Function([var_1650], output)
mutated_mod['func_1652'] = func_1652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_371_call = mod.get_global_var('func_371')
func_372_call = mutated_mod.get_global_var('func_372')
call_1670 = func_371_call()
call_1671 = func_371_call()
output = relay.Tuple([call_1670,])
output2 = relay.Tuple([call_1671,])
func_1677 = relay.Function([], output)
mod['func_1677'] = func_1677
mod = relay.transform.InferType()(mod)
output = func_1677()
func_1678 = relay.Function([], output)
mutated_mod['func_1678'] = func_1678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_1679 = relay.TupleGetItem(func_501_call(), 0)
call_1680 = relay.TupleGetItem(func_503_call(), 0)
output = relay.Tuple([call_1679,])
output2 = relay.Tuple([call_1680,])
func_1692 = relay.Function([], output)
mod['func_1692'] = func_1692
mod = relay.transform.InferType()(mod)
output = func_1692()
func_1693 = relay.Function([], output)
mutated_mod['func_1693'] = func_1693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_1721 = relay.TupleGetItem(func_1692_call(), 0)
call_1722 = relay.TupleGetItem(func_1693_call(), 0)
func_1614_call = mod.get_global_var('func_1614')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_1747 = func_1614_call()
call_1748 = func_1614_call()
uop_1754 = relay.tan(call_1721.astype('float32')) # shape=(13, 9, 1)
uop_1756 = relay.tan(call_1722.astype('float32')) # shape=(13, 9, 1)
output = relay.Tuple([call_1747,uop_1754,])
output2 = relay.Tuple([call_1748,uop_1756,])
func_1758 = relay.Function([], output)
mod['func_1758'] = func_1758
mod = relay.transform.InferType()(mod)
output = func_1758()
func_1759 = relay.Function([], output)
mutated_mod['func_1759'] = func_1759
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1817 = relay.var("var_1817", dtype = "float64", shape = (8, 1, 12))#candidate|1817|(8, 1, 12)|var|float64
uop_1818 = relay.asinh(var_1817.astype('float64')) # shape=(8, 1, 12)
output = relay.Tuple([uop_1818,])
output2 = relay.Tuple([uop_1818,])
func_1830 = relay.Function([var_1817,], output)
mod['func_1830'] = func_1830
mod = relay.transform.InferType()(mod)
var_1831 = relay.var("var_1831", dtype = "float64", shape = (8, 1, 12))#candidate|1831|(8, 1, 12)|var|float64
output = func_1830(var_1831)
func_1832 = relay.Function([var_1831], output)
mutated_mod['func_1832'] = func_1832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_1869 = relay.TupleGetItem(func_76_call(), 3)
call_1870 = relay.TupleGetItem(func_77_call(), 3)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
var_1901 = relay.var("var_1901", dtype = "int8", shape = (1440,))#candidate|1901|(1440,)|var|int8
call_1900 = relay.TupleGetItem(func_1299_call(relay.reshape(var_1901.astype('int8'), [10, 9, 16])), 3)
call_1902 = relay.TupleGetItem(func_1301_call(relay.reshape(var_1901.astype('int8'), [10, 9, 16])), 3)
bop_1906 = relay.less_equal(var_1901.astype('bool'), call_1869.astype('bool')) # shape=(13, 9, 1440)
bop_1909 = relay.less_equal(var_1901.astype('bool'), call_1870.astype('bool')) # shape=(13, 9, 1440)
output = relay.Tuple([call_1900,bop_1906,])
output2 = relay.Tuple([call_1902,bop_1909,])
func_1915 = relay.Function([var_1901,], output)
mod['func_1915'] = func_1915
mod = relay.transform.InferType()(mod)
var_1916 = relay.var("var_1916", dtype = "int8", shape = (1440,))#candidate|1916|(1440,)|var|int8
output = func_1915(var_1916)
func_1917 = relay.Function([var_1916], output)
mutated_mod['func_1917'] = func_1917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_631_call = mod.get_global_var('func_631')
func_632_call = mutated_mod.get_global_var('func_632')
call_1927 = relay.TupleGetItem(func_631_call(), 1)
call_1928 = relay.TupleGetItem(func_632_call(), 1)
output = call_1927
output2 = call_1928
func_1972 = relay.Function([], output)
mod['func_1972'] = func_1972
mod = relay.transform.InferType()(mod)
output = func_1972()
func_1973 = relay.Function([], output)
mutated_mod['func_1973'] = func_1973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_1977 = func_1128_call()
call_1978 = func_1128_call()
const_1989 = relay.const([[[8.413491,-2.849890,-9.772366,7.189883,4.481996,6.127674,-4.762837],[-6.001998,4.452740,7.986922,1.762161,0.636290,-1.176793,0.270811],[5.311740,2.329884,-6.473700,-3.004182,-8.252913,9.659656,-6.595515],[6.587958,-8.031894,-6.568595,5.563425,5.657354,1.725566,-6.117527],[-8.540357,-9.639716,-4.132526,-5.850204,2.910385,6.048118,-1.117159],[5.151025,4.532483,5.588259,3.825575,0.437154,-1.581460,5.925031],[3.877095,3.447209,3.783186,-9.461252,1.041538,3.979271,5.651103],[-5.020454,7.305367,-5.545939,-7.103125,0.663253,-6.475359,-1.166728],[9.666164,-7.776764,-5.092607,-5.332227,3.279947,3.609439,4.720608]],[[-4.425744,-1.574597,5.985075,-8.963533,-8.182278,6.604343,-1.250482],[8.381924,-1.661445,-7.428502,8.507098,-2.926284,6.103471,-3.250088],[-5.814651,5.211314,5.383575,-3.864716,3.053868,-1.168179,0.763523],[5.034786,7.491105,6.065557,-9.344196,8.583421,-5.773807,4.145506],[2.159629,-0.488233,-3.164890,-1.447908,7.952971,-1.230220,-1.591008],[4.856892,-7.063794,3.512566,3.711179,-1.029511,7.205498,1.544035],[9.266248,9.484532,7.408210,8.915724,6.871955,0.553129,-4.367368],[1.237927,-4.108953,-8.253226,-3.698087,0.248461,-9.828497,2.658669],[1.959621,7.271284,3.141073,0.665363,8.939662,-6.737812,6.678988]],[[0.929909,7.004026,-2.832823,4.242847,2.288264,-7.510277,4.684152],[-5.404801,-7.556010,-1.979834,-1.296366,-8.721302,-6.746408,-5.743712],[-9.071653,-3.227508,0.068258,7.656874,5.691192,7.444994,-8.167614],[7.168225,-5.876079,-4.956888,3.649523,8.265863,-1.160877,-7.999312],[3.153782,-7.198220,-7.954462,4.514047,-3.535352,0.924292,-5.156671],[-9.520475,-1.493997,-1.856690,3.717051,-0.883896,5.028001,9.010341],[5.502420,-1.786438,-0.153702,6.443115,0.038329,7.345020,6.951440],[-1.338864,8.444232,-8.030267,-5.096777,-6.433339,3.140860,9.445158],[-0.011784,-6.175905,-2.916164,-4.079477,4.345637,2.545824,9.011105]],[[5.055958,5.331789,-9.616433,-0.892985,-0.928185,1.746989,6.284198],[9.730800,-9.053043,4.581788,-3.776571,0.265905,-1.497496,-4.046853],[-3.326516,-8.201191,-8.193290,9.941512,-2.506755,1.773527,-5.028445],[-0.495768,1.582561,-6.140045,5.410460,-4.221001,3.547761,8.226107],[9.047524,7.865295,5.848947,1.811259,7.031819,-8.400697,-2.931655],[3.269987,-7.017255,-2.550058,8.255052,7.196843,-8.248424,-2.839647],[-2.116976,-7.272560,7.649537,5.553878,8.488311,-6.872159,1.246368],[6.735684,-0.386237,-1.350309,-0.369562,-5.771707,-5.385874,-4.737173],[-0.968326,-6.373286,-0.644160,-9.891073,7.820337,-0.749279,-8.696522]],[[6.131441,5.014649,1.447012,6.517857,1.553697,3.814942,-2.096290],[5.383696,-6.049255,8.062311,-0.267594,6.713600,-7.463154,-9.049516],[-6.610517,8.086648,-1.245173,-9.157838,5.743325,-8.713542,3.176657],[-1.253805,7.754508,-7.884261,2.978930,-9.191723,-9.310050,-6.797321],[-4.640970,7.473795,1.814711,4.539325,-7.025221,-7.323564,0.382542],[-7.763206,-3.185979,-8.731879,-4.404312,9.653711,8.445531,-1.987320],[-3.224760,-7.928151,8.018059,2.873549,-8.667671,2.389673,-7.888717],[-2.317628,-9.264911,-6.611604,-2.583824,-0.446123,5.229348,-1.097468],[2.494875,-5.137957,-7.955122,6.948723,7.643629,-2.904690,9.499620]],[[-2.364224,7.380627,9.156879,8.559556,-7.215294,1.330666,-4.210077],[2.018580,5.193780,3.341121,-8.038897,-0.489867,-9.478341,-8.278020],[5.764987,-7.260261,8.573471,6.121601,2.468546,-6.125152,-9.397754],[-1.196366,-9.715180,2.085498,-7.136170,-5.887467,-6.307995,-1.306317],[-5.707454,-8.781442,-4.879841,9.188660,-9.145351,8.754613,7.401055],[-6.106053,6.289073,-4.055293,-1.742228,8.332762,1.699535,1.194162],[-2.990933,-3.181125,-5.585601,-4.349737,5.600518,-0.257035,-6.871229],[5.871972,3.465691,7.950409,-6.550522,-1.865919,-8.870010,1.318679],[1.763201,7.894064,9.273961,-2.365678,-0.969035,-6.961925,-3.296854]],[[-5.745924,-7.549419,-2.641689,8.647994,-5.308624,-3.394730,-7.879087],[-0.892265,-4.082382,-1.879298,8.280695,3.698103,6.058387,7.955949],[3.934664,-2.829081,-2.519691,4.930963,-4.867682,2.373350,-0.461289],[3.463803,-1.220138,-1.451053,-5.592957,-1.720338,-5.374882,9.694716],[-8.264763,-6.189728,7.393357,7.100911,1.854816,-1.748559,3.508861],[9.198724,9.294069,-3.394794,-1.460064,-5.127926,2.822766,1.341221],[-6.269575,1.819503,3.167562,-9.010435,-3.897045,-7.823090,-7.247922],[3.596070,-9.080461,0.710565,0.340142,8.742859,8.788540,-7.368370],[6.207828,-5.858157,3.525003,-8.868996,3.681385,0.490768,-3.265257]],[[-0.245797,-3.084924,-1.265261,-7.414645,4.276615,4.093611,3.746485],[-8.741600,5.816243,2.781833,-2.848112,7.637894,2.666229,4.517560],[-9.883141,5.698005,0.962889,-7.218135,-1.742997,2.695814,-2.997490],[3.015607,2.167127,-7.556209,2.631498,5.023391,-9.787198,-6.903606],[7.822823,-6.175304,5.736876,-1.396320,6.366556,-7.725132,6.846420],[9.320709,-9.915980,-3.819557,7.313417,-3.067146,-4.248715,-5.104896],[-2.545723,0.756853,-5.684159,1.602214,0.607189,-6.741072,-5.925251],[-0.987390,5.269935,1.805445,-1.632104,7.125955,-0.982589,-9.183817],[5.172153,9.330535,4.400207,-6.470910,-1.986868,1.131596,3.348262]],[[4.112691,-3.240483,-7.587682,4.992124,0.571209,6.047280,4.876393],[-9.377195,-0.876549,-3.618931,7.731994,-2.867709,-0.405568,5.735200],[-1.825811,2.962535,-1.927927,-0.505858,7.322688,8.902034,8.994466],[-9.993270,-2.595977,3.675156,-5.404259,9.370795,7.909476,0.911500],[-6.829818,-0.749975,-8.182695,-3.815578,3.806373,0.745892,1.026920],[-2.071472,7.752182,0.479682,9.763511,-7.461145,1.383562,-9.040165],[-3.804758,-1.494405,-9.755786,4.656293,-1.355317,-7.370291,-8.655266],[5.583498,-4.375042,4.546146,-4.377713,8.920470,0.794852,7.492403],[2.938078,6.135124,-9.545388,9.454998,-1.732533,2.789038,-3.104199]],[[9.775802,1.277198,-7.173522,-5.128138,9.228305,6.186261,-4.334267],[-8.882795,7.840704,3.740588,8.389111,-2.610501,9.568032,-3.605648],[6.933850,-9.286279,5.292030,0.560081,2.425009,9.334911,-0.974532],[3.317674,8.571872,4.048518,-3.441811,-2.237559,-4.117452,-9.298068],[8.718000,-7.810676,8.047762,6.356552,-5.404166,5.913818,-0.476941],[-6.559506,9.829647,-6.627666,5.910035,1.051355,-4.110313,-7.054059],[-7.892061,-1.833975,4.153767,-9.685394,2.768927,4.253235,7.579092],[5.690106,-6.797709,-0.159080,-6.131469,-5.391046,-6.673346,1.963884],[0.029757,5.184082,-7.839758,-9.815309,-3.608093,-9.449601,-8.118593]],[[4.225058,-1.694586,-8.935045,-4.814836,-8.266862,5.185665,0.588679],[-8.514550,-8.738245,-1.551620,1.308282,-0.457428,-7.556881,6.411312],[-9.186423,-5.358929,9.781092,7.402071,9.497004,-1.060504,-1.899916],[0.632520,-1.194666,-2.943680,6.211768,-7.500121,0.623249,-8.525259],[-4.700159,-7.309788,-1.452446,-6.142509,-7.835882,8.639396,-2.077902],[1.215872,4.912895,-8.610081,8.166026,-8.756076,8.203999,6.261528],[5.307698,-9.568701,2.740834,5.931695,4.069798,0.909387,8.620022],[-0.826339,0.118746,-2.897495,-2.413059,-4.755899,8.072330,-2.503201],[5.642550,1.538965,-7.977975,-4.906818,-6.748986,5.130707,-0.550265]],[[7.109381,0.298917,1.064762,-1.206949,3.665113,-1.790542,-9.618875],[-3.200209,-8.775804,-6.665521,3.964352,7.687641,5.223604,3.034386],[4.072860,6.594379,7.969036,-8.632580,9.631486,-5.194040,6.193185],[-6.884012,-1.042355,6.042008,9.974215,-9.520952,-5.565681,-0.530109],[9.834004,-4.864569,5.737804,-3.621113,-1.104030,0.591286,5.157317],[-9.425885,-0.069351,-7.877840,9.889778,9.793814,1.669526,7.202968],[9.029264,6.371616,5.589108,-3.633192,-9.976408,4.311804,6.218117],[-6.983990,-7.105640,-1.873880,-1.244426,3.709364,-8.116305,-8.188962],[-4.001009,9.577887,0.505153,7.228391,-8.032072,-9.593555,-4.275751]],[[0.252988,-0.910292,-6.616785,-9.115589,-1.675758,7.349167,-1.768900],[-2.415193,9.232808,0.035391,8.509503,-5.243680,2.424571,-1.655870],[4.090441,-7.952245,-6.968432,-3.913008,4.428258,4.912619,7.519334],[-9.629117,-2.104408,-2.347502,4.991480,-6.088448,2.435287,6.466158],[4.887784,-5.819331,-9.535276,8.674208,6.752435,5.200037,-2.843823],[-5.850939,4.471403,-6.470159,-3.736999,-4.779273,-6.397365,-0.440512],[3.026622,-9.169306,2.497283,2.668394,2.985754,-0.806292,-8.797708],[-9.667501,2.618805,9.234053,2.333062,-2.984981,-1.897221,1.666395],[-5.019626,-1.147150,-8.436473,-4.268798,2.797761,7.410375,5.434166]]], dtype = "float32")#candidate|1989|(13, 9, 7)|const|float32
bop_1990 = relay.divide(call_1977.astype('float32'), const_1989.astype('float32')) # shape=(13, 9, 7)
bop_1993 = relay.divide(call_1978.astype('float32'), const_1989.astype('float32')) # shape=(13, 9, 7)
output = bop_1990
output2 = bop_1993
func_1997 = relay.Function([], output)
mod['func_1997'] = func_1997
mod = relay.transform.InferType()(mod)
mutated_mod['func_1997'] = func_1997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1997_call = mutated_mod.get_global_var('func_1997')
call_1998 = func_1997_call()
output = call_1998
func_1999 = relay.Function([], output)
mutated_mod['func_1999'] = func_1999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_2002 = relay.TupleGetItem(func_1526_call(), 4)
call_2003 = relay.TupleGetItem(func_1527_call(), 4)
var_2019 = relay.var("var_2019", dtype = "uint32", shape = (13, 9, 14))#candidate|2019|(13, 9, 14)|var|uint32
bop_2020 = relay.add(call_2002.astype('int64'), var_2019.astype('int64')) # shape=(13, 9, 14)
bop_2023 = relay.add(call_2003.astype('int64'), var_2019.astype('int64')) # shape=(13, 9, 14)
func_1997_call = mod.get_global_var('func_1997')
func_1999_call = mutated_mod.get_global_var('func_1999')
call_2028 = func_1997_call()
call_2029 = func_1997_call()
func_887_call = mod.get_global_var('func_887')
func_888_call = mutated_mod.get_global_var('func_888')
call_2030 = relay.TupleGetItem(func_887_call(), 1)
call_2031 = relay.TupleGetItem(func_888_call(), 1)
func_475_call = mod.get_global_var('func_475')
func_477_call = mutated_mod.get_global_var('func_477')
var_2033 = relay.var("var_2033", dtype = "float32", shape = (640,))#candidate|2033|(640,)|var|float32
call_2032 = func_475_call(relay.reshape(var_2033.astype('float32'), [8, 10, 8]))
call_2034 = func_475_call(relay.reshape(var_2033.astype('float32'), [8, 10, 8]))
uop_2037 = relay.log2(call_2032.astype('float32')) # shape=(8, 10, 8)
uop_2039 = relay.log2(call_2034.astype('float32')) # shape=(8, 10, 8)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_2066 = relay.TupleGetItem(func_937_call(), 0)
call_2067 = relay.TupleGetItem(func_939_call(), 0)
func_1073_call = mod.get_global_var('func_1073')
func_1074_call = mutated_mod.get_global_var('func_1074')
call_2072 = func_1073_call()
call_2073 = func_1073_call()
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_2077 = relay.TupleGetItem(func_76_call(), 2)
call_2078 = relay.TupleGetItem(func_77_call(), 2)
bop_2111 = relay.add(call_2002.astype('int8'), var_2033.astype('int8')) # shape=(13, 9, 640)
bop_2114 = relay.add(call_2003.astype('int8'), var_2033.astype('int8')) # shape=(13, 9, 640)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_2125 = func_1972_call()
call_2126 = func_1972_call()
output = relay.Tuple([bop_2020,call_2028,call_2030,uop_2037,call_2066,call_2072,call_2077,bop_2111,call_2125,])
output2 = relay.Tuple([bop_2023,call_2029,call_2031,uop_2039,call_2067,call_2073,call_2078,bop_2114,call_2126,])
func_2127 = relay.Function([var_2019,var_2033,], output)
mod['func_2127'] = func_2127
mod = relay.transform.InferType()(mod)
mutated_mod['func_2127'] = func_2127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2127_call = mutated_mod.get_global_var('func_2127')
var_2129 = relay.var("var_2129", dtype = "uint32", shape = (13, 9, 14))#candidate|2129|(13, 9, 14)|var|uint32
var_2130 = relay.var("var_2130", dtype = "float32", shape = (640,))#candidate|2130|(640,)|var|float32
call_2128 = func_2127_call(var_2129,var_2130,)
output = call_2128
func_2131 = relay.Function([var_2129,var_2130,], output)
mutated_mod['func_2131'] = func_2131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_2147 = relay.TupleGetItem(func_1758_call(), 1)
call_2148 = relay.TupleGetItem(func_1759_call(), 1)
var_2151 = relay.var("var_2151", dtype = "float32", shape = (13, 9, 8))#candidate|2151|(13, 9, 8)|var|float32
bop_2152 = relay.equal(call_2147.astype('bool'), var_2151.astype('bool')) # shape=(13, 9, 8)
bop_2155 = relay.equal(call_2148.astype('bool'), var_2151.astype('bool')) # shape=(13, 9, 8)
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_2157 = relay.TupleGetItem(func_418_call(), 0)
call_2158 = relay.TupleGetItem(func_420_call(), 0)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_2161 = func_21_call()
call_2162 = func_21_call()
output = relay.Tuple([bop_2152,call_2157,call_2161,])
output2 = relay.Tuple([bop_2155,call_2158,call_2162,])
func_2179 = relay.Function([var_2151,], output)
mod['func_2179'] = func_2179
mod = relay.transform.InferType()(mod)
mutated_mod['func_2179'] = func_2179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2180 = relay.var("var_2180", dtype = "float32", shape = (13, 9, 8))#candidate|2180|(13, 9, 8)|var|float32
func_2179_call = mutated_mod.get_global_var('func_2179')
call_2181 = func_2179_call(var_2180)
output = call_2181
func_2182 = relay.Function([var_2180], output)
mutated_mod['func_2182'] = func_2182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_981_call = mod.get_global_var('func_981')
func_982_call = mutated_mod.get_global_var('func_982')
call_2211 = relay.TupleGetItem(func_981_call(), 0)
call_2212 = relay.TupleGetItem(func_982_call(), 0)
output = relay.Tuple([call_2211,])
output2 = relay.Tuple([call_2212,])
func_2224 = relay.Function([], output)
mod['func_2224'] = func_2224
mod = relay.transform.InferType()(mod)
mutated_mod['func_2224'] = func_2224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2224_call = mutated_mod.get_global_var('func_2224')
call_2225 = func_2224_call()
output = call_2225
func_2226 = relay.Function([], output)
mutated_mod['func_2226'] = func_2226
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2291 = relay.const([[[4,4,-1,5,-1,-5,9,-6,-1,-6,-3,-5,-10],[3,1,-7,5,8,-10,-1,5,3,-8,-8,-7,7],[9,-3,4,-9,10,-9,7,-3,10,9,-2,1,1],[-6,-4,-2,-5,-4,-1,-4,-8,7,10,-2,6,8],[-4,-5,-6,3,3,3,-10,-9,-1,-3,-7,4,-2],[8,10,5,4,-8,10,2,-9,-3,3,10,-6,3],[-5,1,-7,-5,-6,10,-10,-2,-10,-8,-1,-7,-5],[-8,-2,-6,-2,-2,7,-4,8,5,-2,2,3,-2],[1,7,-6,10,-10,5,-3,-8,4,3,8,2,5],[4,6,-10,-3,4,6,9,10,7,-1,-2,-9,-9],[-3,6,6,5,4,-8,6,10,8,7,3,9,-1],[1,6,-6,10,6,-2,8,6,-6,-10,4,8,-5]],[[-7,7,5,-7,-7,-9,-7,-2,4,6,8,4,-10],[7,2,-1,6,5,5,2,7,8,4,2,2,10],[1,1,2,9,9,1,5,7,-1,3,-10,-9,-1],[-2,6,4,-8,9,2,-4,-6,-6,-4,-5,2,1],[7,6,-9,-10,2,4,-8,10,1,-10,-10,9,9],[-6,-10,-5,-5,4,9,10,-9,-3,-7,6,6,4],[2,7,7,-4,-10,-3,-10,-10,-4,-2,5,1,-8],[-10,3,-2,9,-8,-5,-3,-1,-2,7,10,2,-4],[7,9,-2,-4,6,2,5,2,-2,7,-5,-2,8],[-6,4,-7,5,8,8,-4,8,-10,6,5,10,1],[8,8,3,-6,3,-10,1,10,10,4,2,10,-7],[-5,-6,2,10,-10,5,-2,1,-9,-9,-2,2,4]],[[-7,1,-9,10,-3,-9,-4,5,-7,8,-8,10,7],[-6,-7,3,7,9,2,-3,-2,9,-3,3,-3,2],[9,1,-4,-5,7,5,3,2,-3,-2,9,-1,8],[-6,7,4,-2,4,-10,-6,-6,-3,-7,6,-3,-5],[2,7,-1,2,-3,-8,1,-10,8,10,-9,6,-1],[5,3,-6,-7,-8,10,-10,6,7,-7,-8,4,-10],[-2,-10,9,5,-7,-10,6,7,-7,8,-3,1,-1],[-7,-7,-10,5,2,-5,-7,-9,-9,2,10,2,-3],[10,-7,2,-8,2,10,5,-1,-8,-5,3,2,9],[-5,8,6,-1,-1,-8,2,6,-9,-3,-3,9,7],[-1,1,1,-1,-5,8,-1,-9,-9,-10,2,-10,-10],[-5,3,2,1,4,-9,-10,1,10,-9,10,1,-3]],[[-9,-7,7,7,6,-2,5,10,10,-10,-9,10,1],[-6,-9,-5,-3,9,-6,8,8,-10,7,-10,-9,-7],[-1,8,8,-4,4,-7,-2,7,-3,-10,8,-7,-10],[-1,5,9,6,10,1,2,5,-4,-8,-7,-7,-5],[6,9,6,7,7,-9,-3,-8,-7,2,4,9,7],[6,-4,9,10,8,-8,-9,-10,10,1,10,2,10],[-7,9,-4,10,-3,-7,-8,3,9,3,-2,5,-4],[-9,-8,-2,7,-1,-6,10,1,-4,-4,7,9,-5],[4,4,4,4,-4,8,-8,2,-1,3,10,5,6],[-7,1,-8,1,-2,-7,10,-3,-1,-7,-2,7,-4],[-5,-3,10,-8,4,-5,7,-2,6,-4,-10,7,-1],[-10,6,-7,3,-2,2,6,-3,10,10,4,6,2]],[[-4,5,-10,4,-1,7,-1,-8,6,-6,5,-8,-10],[3,-2,-3,-6,4,3,1,8,-7,4,1,-9,8],[-5,-3,3,-4,-10,3,-5,-9,-2,-4,8,-1,-9],[2,-1,6,-1,2,4,8,3,8,-6,-8,-9,1],[6,-2,6,6,6,-3,10,10,-3,8,10,6,4],[4,-6,5,-9,-8,-10,-2,6,-5,5,10,4,6],[3,9,5,5,2,-3,4,8,6,2,7,8,-5],[-10,6,4,-7,9,8,-3,-1,-3,-10,10,-1,7],[10,-10,4,3,-5,9,9,3,-1,10,-3,-6,-4],[-8,-1,-4,2,5,5,6,-6,-3,-3,4,1,6],[5,-8,10,-5,-2,-1,5,8,5,-10,-9,6,9],[5,-2,-5,-5,-7,8,-8,-10,-5,-5,5,-9,1]],[[-9,-1,4,2,9,4,-2,-10,2,-3,7,9,2],[-3,10,8,-8,-2,7,8,-1,1,-3,6,-9,10],[-6,1,3,-9,-8,4,6,-10,-10,-10,-3,4,1],[1,-8,9,10,-10,-4,7,5,-9,7,-5,-10,-8],[5,-8,2,6,10,4,5,-2,4,-10,3,2,-9],[-7,-4,-9,-6,5,6,-8,7,8,-7,-9,-2,-9],[-8,-4,-8,5,5,10,1,-1,-7,7,2,-5,6],[9,-5,-2,7,-2,-7,8,-1,5,-6,-2,5,8],[-3,-6,9,8,2,-6,7,8,5,8,-6,9,-9],[-4,10,-2,5,3,-3,-7,-2,6,3,5,-9,5],[6,-5,6,-7,-3,1,-7,9,5,7,-9,7,6],[-1,3,-8,1,-3,-7,5,-1,6,-9,8,-3,1]],[[7,-5,8,-7,1,1,1,10,6,7,-10,-7,-10],[-4,1,4,-1,-10,4,-3,5,8,10,5,3,-5],[-5,-3,7,-5,-1,4,-9,-5,4,-9,-2,6,-6],[9,-10,-2,5,9,1,10,-4,-7,1,-9,10,5],[-6,-3,9,-2,6,-6,-7,3,-9,-3,-7,10,-4],[4,-7,-5,7,7,-2,7,-1,1,7,10,-6,3],[-5,5,1,1,-8,5,6,5,1,6,-6,1,-10],[3,6,-3,-8,10,8,1,10,5,-8,-4,4,-10],[-8,6,-4,5,-5,-10,-7,-4,4,4,3,-1,-10],[9,-6,4,2,1,-9,3,-5,6,-5,-8,8,-4],[1,-2,-10,-7,-2,8,3,7,6,-3,-6,2,1],[-2,-1,-2,2,5,6,8,-5,9,6,9,7,4]],[[4,5,-3,4,3,-6,9,7,-3,3,-1,-7,10],[2,1,3,9,9,-6,8,1,6,-5,-5,-10,-8],[3,-10,3,-10,-8,-8,-2,-9,-3,8,10,4,-9],[-4,9,9,-7,-3,-1,-3,-8,5,9,6,10,-6],[10,-6,10,7,1,-1,7,7,9,-6,-2,-6,-7],[-4,8,7,-1,8,-4,1,3,4,-6,-9,-2,1],[-7,6,9,1,10,-5,3,-4,-2,-2,7,-6,-6],[7,9,-3,-2,8,-9,-9,7,1,9,6,-10,-6],[-4,-9,5,-10,1,9,-10,-5,6,-9,-7,-2,6],[8,6,-1,6,3,-6,-6,-4,-2,-3,-5,-2,1],[-5,-6,1,-6,-9,9,7,-7,-5,-1,9,5,-10],[-1,7,2,7,4,5,6,7,9,9,8,-10,-3]],[[2,-1,2,-7,-5,2,8,-9,4,-6,3,4,1],[6,-10,-10,-10,-7,2,9,4,9,-7,-4,2,-1],[-5,-6,6,-8,2,-1,1,-3,3,-2,5,-8,8],[3,-3,-4,7,7,-4,4,-4,-8,-4,-8,5,3],[-9,-4,4,-6,10,-5,2,4,6,-3,2,3,-4],[-2,-1,1,-7,-7,-2,8,-5,-1,-3,-4,-1,-9],[-10,-1,-5,5,10,-6,-3,-6,5,7,6,-8,2],[-10,-1,-8,-5,-7,-1,-6,10,-8,6,8,-9,-1],[2,6,1,7,-6,5,5,2,4,-9,-2,7,-2],[-9,-1,-9,-2,-9,2,-7,2,-2,3,2,-3,-2],[-9,-5,6,-5,-6,4,-7,5,10,10,3,8,5],[1,-3,5,4,5,3,8,2,1,6,1,-5,7]],[[-10,-4,-7,2,-10,1,4,5,-6,9,7,-7,6],[-7,6,9,-9,10,-9,-5,9,2,-2,5,10,-3],[-5,-9,8,-2,-2,-10,-3,6,-5,1,-8,1,2],[7,-9,-10,-3,-5,-7,-7,7,1,-10,-4,-9,-10],[9,-7,7,-4,6,-1,3,2,-3,2,-8,2,1],[4,-2,-8,-6,-4,9,-1,2,-6,8,-6,8,-4],[2,-4,-3,-4,3,-10,5,3,-1,-10,6,9,-5],[6,-4,10,6,8,10,-6,2,-3,-1,-2,1,-7],[-10,-1,-1,10,7,9,2,5,-7,-9,9,7,-8],[-2,1,-4,-6,-7,1,-10,7,-4,-9,5,3,7],[3,2,3,10,3,-6,-6,6,2,8,9,10,-2],[-6,-6,7,-6,-1,-4,10,5,-8,1,-10,2,-4]]], dtype = "uint16")#candidate|2291|(10, 12, 13)|const|uint16
var_2292 = relay.var("var_2292", dtype = "uint16", shape = (10, 12, 13))#candidate|2292|(10, 12, 13)|var|uint16
bop_2293 = relay.not_equal(const_2291.astype('bool'), relay.reshape(var_2292.astype('bool'), relay.shape_of(const_2291))) # shape=(10, 12, 13)
output = relay.Tuple([bop_2293,])
output2 = relay.Tuple([bop_2293,])
func_2296 = relay.Function([var_2292,], output)
mod['func_2296'] = func_2296
mod = relay.transform.InferType()(mod)
mutated_mod['func_2296'] = func_2296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2297 = relay.var("var_2297", dtype = "uint16", shape = (10, 12, 13))#candidate|2297|(10, 12, 13)|var|uint16
func_2296_call = mutated_mod.get_global_var('func_2296')
call_2298 = func_2296_call(var_2297)
output = call_2298
func_2299 = relay.Function([var_2297], output)
mutated_mod['func_2299'] = func_2299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_2311 = relay.TupleGetItem(func_1677_call(), 0)
call_2312 = relay.TupleGetItem(func_1678_call(), 0)
func_247_call = mod.get_global_var('func_247')
func_248_call = mutated_mod.get_global_var('func_248')
call_2327 = relay.TupleGetItem(func_247_call(), 0)
call_2328 = relay.TupleGetItem(func_248_call(), 0)
bop_2342 = relay.floor_divide(call_2311.astype('float32'), relay.reshape(call_2327.astype('float32'), relay.shape_of(call_2311))) # shape=(13, 9, 1)
bop_2345 = relay.floor_divide(call_2312.astype('float32'), relay.reshape(call_2328.astype('float32'), relay.shape_of(call_2312))) # shape=(13, 9, 1)
var_2350 = relay.var("var_2350", dtype = "float32", shape = (13, 9, 8))#candidate|2350|(13, 9, 8)|var|float32
bop_2351 = relay.divide(bop_2342.astype('float64'), var_2350.astype('float64')) # shape=(13, 9, 8)
bop_2354 = relay.divide(bop_2345.astype('float64'), var_2350.astype('float64')) # shape=(13, 9, 8)
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_2359 = relay.TupleGetItem(func_76_call(), 0)
call_2360 = relay.TupleGetItem(func_77_call(), 0)
bop_2364 = relay.bitwise_and(bop_2351.astype('uint16'), bop_2342.astype('uint16')) # shape=(13, 9, 8)
bop_2367 = relay.bitwise_and(bop_2354.astype('uint16'), bop_2345.astype('uint16')) # shape=(13, 9, 8)
output = relay.Tuple([call_2359,bop_2364,])
output2 = relay.Tuple([call_2360,bop_2367,])
func_2374 = relay.Function([var_2350,], output)
mod['func_2374'] = func_2374
mod = relay.transform.InferType()(mod)
mutated_mod['func_2374'] = func_2374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2375 = relay.var("var_2375", dtype = "float32", shape = (13, 9, 8))#candidate|2375|(13, 9, 8)|var|float32
func_2374_call = mutated_mod.get_global_var('func_2374')
call_2376 = func_2374_call(var_2375)
output = call_2376
func_2377 = relay.Function([var_2375], output)
mutated_mod['func_2377'] = func_2377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_2386 = relay.TupleGetItem(func_1758_call(), 1)
call_2387 = relay.TupleGetItem(func_1759_call(), 1)
output = relay.Tuple([call_2386,])
output2 = relay.Tuple([call_2387,])
func_2389 = relay.Function([], output)
mod['func_2389'] = func_2389
mod = relay.transform.InferType()(mod)
mutated_mod['func_2389'] = func_2389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2389_call = mutated_mod.get_global_var('func_2389')
call_2390 = func_2389_call()
output = call_2390
func_2391 = relay.Function([], output)
mutated_mod['func_2391'] = func_2391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_2419 = relay.TupleGetItem(func_418_call(), 0)
call_2420 = relay.TupleGetItem(func_420_call(), 0)
output = relay.Tuple([call_2419,])
output2 = relay.Tuple([call_2420,])
func_2421 = relay.Function([], output)
mod['func_2421'] = func_2421
mod = relay.transform.InferType()(mod)
output = func_2421()
func_2422 = relay.Function([], output)
mutated_mod['func_2422'] = func_2422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_2430 = relay.TupleGetItem(func_1677_call(), 0)
call_2431 = relay.TupleGetItem(func_1678_call(), 0)
func_475_call = mod.get_global_var('func_475')
func_477_call = mutated_mod.get_global_var('func_477')
var_2439 = relay.var("var_2439", dtype = "float32", shape = (640,))#candidate|2439|(640,)|var|float32
call_2438 = func_475_call(relay.reshape(var_2439.astype('float32'), [8, 10, 8]))
call_2440 = func_475_call(relay.reshape(var_2439.astype('float32'), [8, 10, 8]))
func_664_call = mod.get_global_var('func_664')
func_667_call = mutated_mod.get_global_var('func_667')
call_2448 = relay.TupleGetItem(func_664_call(relay.reshape(var_2439.astype('float32'), [640,])), 1)
call_2449 = relay.TupleGetItem(func_667_call(relay.reshape(var_2439.astype('float32'), [640,])), 1)
output = relay.Tuple([call_2430,call_2438,var_2439,call_2448,])
output2 = relay.Tuple([call_2431,call_2440,var_2439,call_2449,])
func_2454 = relay.Function([var_2439,], output)
mod['func_2454'] = func_2454
mod = relay.transform.InferType()(mod)
var_2455 = relay.var("var_2455", dtype = "float32", shape = (640,))#candidate|2455|(640,)|var|float32
output = func_2454(var_2455)
func_2456 = relay.Function([var_2455], output)
mutated_mod['func_2456'] = func_2456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1073_call = mod.get_global_var('func_1073')
func_1074_call = mutated_mod.get_global_var('func_1074')
call_2489 = func_1073_call()
call_2490 = func_1073_call()
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_2491 = relay.TupleGetItem(func_1758_call(), 0)
call_2492 = relay.TupleGetItem(func_1759_call(), 0)
bop_2496 = relay.subtract(call_2489.astype('int32'), relay.reshape(call_2491.astype('int32'), relay.shape_of(call_2489))) # shape=(13, 9, 1)
bop_2499 = relay.subtract(call_2490.astype('int32'), relay.reshape(call_2492.astype('int32'), relay.shape_of(call_2490))) # shape=(13, 9, 1)
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_2500 = relay.TupleGetItem(func_418_call(), 0)
call_2501 = relay.TupleGetItem(func_420_call(), 0)
func_247_call = mod.get_global_var('func_247')
func_248_call = mutated_mod.get_global_var('func_248')
call_2521 = relay.TupleGetItem(func_247_call(), 1)
call_2522 = relay.TupleGetItem(func_248_call(), 1)
output = relay.Tuple([bop_2496,call_2500,call_2521,])
output2 = relay.Tuple([bop_2499,call_2501,call_2522,])
func_2527 = relay.Function([], output)
mod['func_2527'] = func_2527
mod = relay.transform.InferType()(mod)
output = func_2527()
func_2528 = relay.Function([], output)
mutated_mod['func_2528'] = func_2528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_247_call = mod.get_global_var('func_247')
func_248_call = mutated_mod.get_global_var('func_248')
call_2533 = relay.TupleGetItem(func_247_call(), 0)
call_2534 = relay.TupleGetItem(func_248_call(), 0)
output = relay.Tuple([call_2533,])
output2 = relay.Tuple([call_2534,])
func_2566 = relay.Function([], output)
mod['func_2566'] = func_2566
mod = relay.transform.InferType()(mod)
mutated_mod['func_2566'] = func_2566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2566_call = mutated_mod.get_global_var('func_2566')
call_2567 = func_2566_call()
output = call_2567
func_2568 = relay.Function([], output)
mutated_mod['func_2568'] = func_2568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_2588 = relay.TupleGetItem(func_501_call(), 0)
call_2589 = relay.TupleGetItem(func_503_call(), 0)
func_565_call = mod.get_global_var('func_565')
func_568_call = mutated_mod.get_global_var('func_568')
const_2604 = relay.const([-7,-8,9,-9,-8,-2,-4,8,2,-10,-3,-3,4,8,-5,9,-3,4,2,-8,4,-5,-5,-6,2,-1,-6,2,10,-5,10,-6,-10,-6,6,5,6,-10,6,9,10,10,6,8,-1,-10,-7,-3,-9,-9,5,-4,-7,-1,8,10,-1,6,4,3,6,-4,2,-10,-10,-7,-5,3,7,7,-3,-5,-7,10,-6,-7,-8,7,-2,-4,-8,-5,-4,-6,-2,8,10,-8,8,-10,-2,-9,10,2,-5,-2,7,-7,-6,4,6,3,-7,4,-10,-10,-1,-3,-6,-1,-9,-5,2,9,-5,-8,-3,6,2,5,-6,4,-3,8,-10,-4,4,7,-1,4,9,8,2,4,-6,6,2,-7,7,-8,-4,7,-4,-6,1,3,-3,-2,5,-9,-4,10,6,-3,-5,-9,-5,-9,-3,6,-4,-3,-9,1,2,-6,-8,-2,-6,-7,-8,-1,5,2,6,1,8,-8,9,-5,-1,7,7,-4,-4,5,-9,5,-10,-1,6,10,-6,-2,-8,-7,-8,-8,2,10,-3,6,-5,6,-7,-4,9,-8,4,1,9,-3,-2,3,-3,10,10,-7,-8,-2,2,-9,-2,7,8,-8,-7,3,-1,3,-9,-1,-10,4,3,-4,-2,9,1,9,-5,-8,7,-2,-10,-2,10,8,4,-10,9,-4,-9,6,9,1,2,6,1,-8,5,-9,-3,-4,10,6,8,-10,-4,-6,2,9,-7,3,-3,8,-1,2,8,3,-10,7,10,4,6,7,7,3,-10,-1,-7,2,8,4,-10,3,-7,-7,-10,10,-10,5,10,-9,-4,5,1,-3,-9,-6,5,10,-2,10,-7,9,7,7,3,10,-8,3,10,10,-3,2,-6,2,9,-1,4,6,-5,1,-8,-7,5,8,4,-7,-4,6,1,-9,2,7,-9,7,7,-4,-10,3,-1,-3,9,-3,-10,3,5,-2,-10,-2,5,5,-9,8,9,7,2,-6,-3,-4,-6,-6,8,9,-8,-1,2,4,-6,-3,4,7,-3,9,-2,8,-1,-8,-2,-9,9,3,7,-3,8,7,7,9,9,-5,-2,-8,9,4,-4,-2,-4,-2,-10,1,2,-1,-4,-10,-8,-3,-10,-5,-6,10,3,-2,-7,-5,1,7,6,4,-8,-4,-9,-1,7,-10,5,4,2,-3,10,7,4,5,-2,1,-3,-10,-1,5,-7,4,5,-9,3,7,2,7,8,7,2,3,2,-10,-2,-4,10,-2,3,5,3,-1,7,-10,-3,6,4,3,-1,-10,9,-4,1,5,7,-2,-3,-5,5,5,2,-5,9,2,-2,6,8,10,6,-5,-7,-3,-4,-9,4,8,5,2,-1,7,1,-3,-3,-10,8,4,-4,6,-7,-6,-10,9,-8,-3,-7,10,-4,-7,-6,8,2,-1,-10,6,-1,10,-7,-1,10,-1,2,5,4,3,-8,-4,-2,9,-2,-9,7,6,-8,8,1,-7,1,-1,3,-5,-4,5,3,-5,-1,8,4,4,1,2,-3,6,-10,-1,8,7,-2,-7,-8,-8,9,-9,-1,6,6,3,8,5,6,-2,9,-6,4,8,8,-5,3,1,-8,6,-7,-5,-10,-5,-6,1,-8,10,2,8,-5,8,-6,2,6,-7,-10,-9,5,-7,3,-8,-6,-5,-6,10,-5,-9,-7,-4,-10,-9,-5,1,4,-1,-7,-10,-7,5,7,5,4,-2,7,-6,-6,9,3,1,1,6,3,3,10,-5,3,-8,6,-10,3,3,-10,1,6,3,-6,-7,3,-8,10,-10,5,-2,8,-7,-9,-2,-5,-4,-5,-8,6,-9,-5,-3,-4,8,1,-2,1,1,10,-8,-6,-3,9,-3,7,5,-3,-7,-1,6,-2,-4,8,2,9,-2,-2,6,-8,-8,3,7,2,-2,-6,9,-5,-2,8,-10,5,2,6,-9,-8,-9,2,6,-7,-9,7,2,10,-6,9,-7,-7,-4,-8,-9,-1,9,2,7,6,-4,-5,4,2,6,-5,8,2,6,6,-6,4,8,3,-5,3,-1,-8,2,4,-3,-10,10,2,2,3,-5,-5,1,10,6,-7,-10,9,-5,1,-1,-9,-3,-9,1,4,9,10,-7,9,-4,10,3,7,4,6,-10,-8,-7,9,1,5,5,1,4,7,8,1,9,-9,-7,-8,-1,-10,-7,8,6,-7,7,-3,10,10,-7,7,-8,-1,-3,-1,-7,-3,-4,2,6,-9,1,-5,-3,-9,5,-8,-4,7,-10,-10,-9,-1,7,3,5,6,5,7,6,10,-3,4,7,-5,-10,-4,-9,4,-10,-9,8,-1,7,-2,-5,2,-1,3,10,7,-4,-10,7,1,10,4,-5,2,-4,-3,-5,7,3,-5,10,2,-4,7,8,-1,-7,-8,-2,4,-5,7,4,-7,3,-2,6,7,8,-1,3,7,-9,-4,-3,10,-7,-9,10,10,8,6,-7,3,-8,-4,-10,-3,-5,-1,7,-6,8,-3,-1,-2,4,4,3,-9,-4,2,-3,3,3,-6,-5,3,10,-2,1,-2,1,8,-3,-3,-9,3,1,8,1,-2,-8,2,5,9,-5,2,-6,10,-7,-10,-9,6,10,3,10,8,4,-6,-3,6,-5,-5,-9,2,-1,10,-5,1,-2,7,-4,10,6,-7,-8,-8,-1,3,10,-4,8,-3,2,-10,-10,6,3,-2,-9,-7,-1,-9,-10,2,10,2,-4,4,-9,-10,-1,-3,-10,5,-3,6,9,-8,-2,10,-8,1,-7,6,9,-5,2,-5,10,-2,2,8,-5,-2,-7,-8,-5,7], dtype = "uint32")#candidate|2604|(1053,)|const|uint32
call_2603 = relay.TupleGetItem(func_565_call(relay.reshape(const_2604.astype('uint32'), [13, 9, 9])), 0)
call_2605 = relay.TupleGetItem(func_568_call(relay.reshape(const_2604.astype('uint32'), [13, 9, 9])), 0)
bop_2618 = relay.left_shift(call_2603.astype('uint32'), relay.reshape(call_2588.astype('uint32'), relay.shape_of(call_2603))) # shape=(13, 9, 1)
bop_2621 = relay.left_shift(call_2605.astype('uint32'), relay.reshape(call_2589.astype('uint32'), relay.shape_of(call_2605))) # shape=(13, 9, 1)
output = relay.Tuple([const_2604,bop_2618,])
output2 = relay.Tuple([const_2604,bop_2621,])
func_2626 = relay.Function([], output)
mod['func_2626'] = func_2626
mod = relay.transform.InferType()(mod)
output = func_2626()
func_2627 = relay.Function([], output)
mutated_mod['func_2627'] = func_2627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_2639 = func_122_call()
call_2640 = func_122_call()
func_493_call = mod.get_global_var('func_493')
func_494_call = mutated_mod.get_global_var('func_494')
call_2641 = relay.TupleGetItem(func_493_call(), 0)
call_2642 = relay.TupleGetItem(func_494_call(), 0)
output = relay.Tuple([call_2639,call_2641,])
output2 = relay.Tuple([call_2640,call_2642,])
func_2643 = relay.Function([], output)
mod['func_2643'] = func_2643
mod = relay.transform.InferType()(mod)
output = func_2643()
func_2644 = relay.Function([], output)
mutated_mod['func_2644'] = func_2644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1073_call = mod.get_global_var('func_1073')
func_1074_call = mutated_mod.get_global_var('func_1074')
call_2645 = func_1073_call()
call_2646 = func_1073_call()
output = call_2645
output2 = call_2646
func_2651 = relay.Function([], output)
mod['func_2651'] = func_2651
mod = relay.transform.InferType()(mod)
output = func_2651()
func_2652 = relay.Function([], output)
mutated_mod['func_2652'] = func_2652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_2678 = relay.TupleGetItem(func_2626_call(), 1)
call_2679 = relay.TupleGetItem(func_2627_call(), 1)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_2691 = relay.TupleGetItem(func_1692_call(), 0)
call_2692 = relay.TupleGetItem(func_1693_call(), 0)
func_1649_call = mod.get_global_var('func_1649')
func_1652_call = mutated_mod.get_global_var('func_1652')
var_2718 = relay.var("var_2718", dtype = "float32", shape = (1, 640))#candidate|2718|(1, 640)|var|float32
call_2717 = relay.TupleGetItem(func_1649_call(relay.reshape(var_2718.astype('float32'), [640,])), 2)
call_2719 = relay.TupleGetItem(func_1652_call(relay.reshape(var_2718.astype('float32'), [640,])), 2)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_2720 = relay.TupleGetItem(func_937_call(), 3)
call_2721 = relay.TupleGetItem(func_939_call(), 3)
uop_2722 = relay.sigmoid(var_2718.astype('float32')) # shape=(1, 640)
output = relay.Tuple([call_2678,call_2691,call_2717,call_2720,uop_2722,])
output2 = relay.Tuple([call_2679,call_2692,call_2719,call_2721,uop_2722,])
func_2724 = relay.Function([var_2718,], output)
mod['func_2724'] = func_2724
mod = relay.transform.InferType()(mod)
var_2725 = relay.var("var_2725", dtype = "float32", shape = (1, 640))#candidate|2725|(1, 640)|var|float32
output = func_2724(var_2725)
func_2726 = relay.Function([var_2725], output)
mutated_mod['func_2726'] = func_2726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_2747 = relay.TupleGetItem(func_76_call(), 0)
call_2748 = relay.TupleGetItem(func_77_call(), 0)
func_1614_call = mod.get_global_var('func_1614')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_2794 = func_1614_call()
call_2795 = func_1614_call()
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_2809 = func_21_call()
call_2810 = func_21_call()
bop_2812 = relay.mod(call_2747.astype('float64'), relay.reshape(call_2794.astype('float64'), relay.shape_of(call_2747))) # shape=(13, 9, 1)
bop_2815 = relay.mod(call_2748.astype('float64'), relay.reshape(call_2795.astype('float64'), relay.shape_of(call_2748))) # shape=(13, 9, 1)
func_981_call = mod.get_global_var('func_981')
func_982_call = mutated_mod.get_global_var('func_982')
call_2822 = relay.TupleGetItem(func_981_call(), 0)
call_2823 = relay.TupleGetItem(func_982_call(), 0)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
var_2825 = relay.var("var_2825", dtype = "int8", shape = (20, 72))#candidate|2825|(20, 72)|var|int8
call_2824 = relay.TupleGetItem(func_1299_call(relay.reshape(var_2825.astype('int8'), [10, 9, 16])), 1)
call_2826 = relay.TupleGetItem(func_1301_call(relay.reshape(var_2825.astype('int8'), [10, 9, 16])), 1)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_2856 = func_1972_call()
call_2857 = func_1972_call()
var_2860 = relay.var("var_2860", dtype = "int8", shape = (20, 72))#candidate|2860|(20, 72)|var|int8
bop_2861 = relay.mod(var_2825.astype('float64'), relay.reshape(var_2860.astype('float64'), relay.shape_of(var_2825))) # shape=(20, 72)
bop_2889 = relay.maximum(call_2747.astype('uint16'), relay.reshape(call_2809.astype('uint16'), relay.shape_of(call_2747))) # shape=(13, 9, 1)
bop_2892 = relay.maximum(call_2748.astype('uint16'), relay.reshape(call_2810.astype('uint16'), relay.shape_of(call_2748))) # shape=(13, 9, 1)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_2896 = func_1128_call()
call_2897 = func_1128_call()
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
const_2903 = relay.const([1.203271,8.558941,-6.403513,-5.744834,9.258670,1.148800,3.993403,5.354243,8.264211,1.536040,4.027336,5.926704,-6.989986,4.875763,-3.465011,9.466350,-9.658375,8.681140,-8.328468,-4.751910,1.877951,7.120379,3.752735,-3.400978,9.935872,2.762416,4.458992,-5.365400,-6.089237,1.171885,-5.205025,-1.241749,-2.596633,7.764664,-4.144020,-4.727946,-3.241440,-2.900248,-8.777526,-5.787994,-8.977418,-0.283019,6.954497,3.832457,-8.663076,-2.034019,7.376065,0.111976,-8.848240,8.746166,-9.012642,-4.843633,1.220786,2.491024,0.078954,7.576452,0.579376,7.270593,1.273460,-6.511562,-3.212594,-1.042035,-7.515392,1.463329,-9.157927,0.130477,-2.397669,7.520483,-0.563138,6.556269,8.333414,3.707742,0.180180,1.700746,2.088664,-2.816680,-5.910642,-2.499226,0.960599,8.546025,-0.937430,-8.087621,-2.202764,-1.586326,-6.823788,-8.150504,9.371283,5.151024,-6.521205,2.073099,-6.253131,9.613301,-5.500687,4.900897,8.349851,9.557110,6.949235,-1.708072,-4.616123,-2.145543,9.462584,-1.874721,-1.219782,6.755808,-9.090017,6.209907,-9.095120,6.439412,-3.386953,-6.742912,6.966040,8.618108,-1.291638,-9.980790,-7.937028,1.027220,7.582498,-1.595417,2.178983,-0.084425,-8.275634,1.624877,6.993660,6.051771,6.660173,1.501223,-1.563407,-7.548231,5.225123,3.432520,0.809233,2.264420,-7.179656,7.169935,4.661171,9.694364,0.628800,-9.382681,6.861695,-2.038163,-1.822133,0.009490,-7.023937,6.142956,-0.862596,9.823177,2.837715,-4.367218,7.439733,-7.040170,1.174793,-6.181016,-0.247501,0.146849,7.888691,-6.044993,-1.846406,-7.479372,0.002730,-7.585861,-0.869757,-7.882120,-9.957729,7.912891,-6.934964,-3.388763,1.291016,-3.213293,4.075840,5.785063,0.813658,-8.680370,1.216481,-1.813400,-9.317950,-1.062153,-2.056349,5.699283,5.621911,-6.140805,-9.072511,8.571220,-5.194558,2.337866,-2.708541,-3.533098,-2.098606,4.662155,4.293253,7.283082,-2.873524,-3.067961,-9.110185,6.226021,-6.135514,2.628575,-1.982576,-6.894370,-7.913096,-4.997590,-4.606646,-6.120008,-3.203453,-7.549514,0.865855,9.737644,0.982718,-8.970202,8.729702,3.069357,-7.686035,-3.081181,4.269628,5.149265,-3.132151,-8.752182,-5.207926,-7.902018,-9.841010,-5.568729,-8.855613,4.921588,0.046538,8.726194,8.324545,-9.862470,2.258309,-2.914032,6.140350,-5.720353,-0.406817,-4.028825,6.883367,9.526165,1.086621,9.977076,1.088065,3.493537,-5.493108,-9.384455,9.443430,4.559935,3.763463,1.525560,0.760150,1.945394,5.172650,-9.570695,-1.873696,-8.557938,1.295868,0.338588,4.357975,8.173725,6.184243,9.006335,-0.274749,0.611261,7.750775,-6.707068,-7.687841,-5.686598,5.582714,-1.555487,-9.202430,0.968715,-0.566454,-5.610753,5.178272,6.075087,3.525416,2.370953,-5.950677,-7.058401,-6.685071,-4.452594,-2.992481,-0.481476,-7.136301,2.963720,0.668610,-0.487341,2.601728,2.704479,9.646230,8.589210,-0.846641,-8.290754,7.758083,-8.570681,-8.669110,-5.066786,6.311365,-1.831106,3.506243,-1.782870,1.827594,-3.181287,6.517013,6.278738,-1.771961,-3.651699,-7.063363,6.540880,1.608369,5.736452,6.965076,-9.835657,-7.378127,-4.634844,-4.004563,-8.174584,0.085589,-7.021937,9.646140,2.956430,-9.393267,-0.284952,0.880261,-9.700122,7.656474,-2.280831,4.363872,6.609920,6.459602,1.491165,-7.257265,1.491628,-2.843993,-1.101181,-4.105875,1.057115,1.039492,8.753557,-1.417820,5.174806,7.007562,-5.255982,-1.474271,-1.074512,4.248576,8.839968,1.076067,8.326085,-5.243065,1.251633,-9.823002,8.205106,-7.116209,-8.369648,-9.798205,-4.722799,8.414007,-7.229924,-5.976880,3.099095,-9.015183,4.695806,-0.984323,2.557526,2.372413,1.743537,-5.740273,1.939271,6.289008,0.139455,-6.299181,1.085793,-6.133714,1.351406,-3.805618,-7.272827,-1.871389,-7.515489,-4.581446,1.949593,0.069641,8.593613,-9.822634,-0.635553,-2.179987,5.833400,-3.098277,-6.220410,1.495059,4.119346,3.724067,-8.701232,-5.963084,-7.834431,9.371902,-5.637343,-8.484178,-4.297234,-3.635725,-6.490719,-2.338241,3.585855,-0.926255,7.380144,-4.857850,9.590271,-4.775735,5.640868,-7.670231,2.376779,2.095847,-5.616161,-1.419747,-5.711535,-2.326306,6.133433,8.233273,7.257100,3.802089,9.995702,3.194856,2.114865,-0.478284,-0.600994,-4.907500,-8.349269,8.024756,6.173786,5.765332,9.780036,-8.649386,-3.488506,6.015127,4.019075,-8.927479,-9.462883,6.650032,7.929915,-0.220063,-3.190670,-6.512395,6.370184,-1.571693,6.388046,-3.916818,0.091733,3.587638,-0.462162,5.028340,7.381444,-4.099126,1.330228,2.440584,-7.028233,9.409278,-0.424704,4.076120,8.762296,-3.733022,-2.475403,5.743911,8.232465,4.945970,-9.214527,2.639644,1.881747,4.886737,9.566183,2.966698,4.537023,9.140074,-2.022524,6.799838,-6.974843,-6.231587,-9.221525,-4.686995,7.921014,-8.800389,-3.879785,4.067967,2.585023,-8.930717,-6.595597,-0.134791,-3.238777,8.003338,8.842211,2.553336,3.160418,-5.766920,2.608870,6.975029,-4.231323,-1.362130,-1.986281,-4.545928,6.931072,-5.337661,2.091844,5.577829,-9.950631,-2.785729,8.958459,2.493781,-7.145812,-4.855618,-8.558259,-8.850289,1.661642,2.075383,-9.091172,-9.601878,1.675787,8.607927,0.178793,-7.492096,-2.483191,4.166502,-9.129906,-9.418146,-9.940162,5.173399,-5.521357,-3.556778,-0.931117,9.293341,1.523557,-5.012055,8.259171,4.309517,-2.089225,-1.590120,6.424924,-0.093240,3.942090,-8.522253,-0.538298,-5.149382,5.812982,-0.958373,6.724634,-5.884513,5.733938,6.782089,0.333249,-3.156266,-3.005352,-9.055601,-3.391605,-4.573528,4.940228,-5.047625,-0.302156,-3.143359,4.772048,8.797690,1.043175,5.604535,4.634752,6.269377,-7.035797,-7.144880,-2.035886,-8.366249,-3.182976,-1.609390,6.152249,9.155777,-8.637059,4.780470,-4.192914,-4.453726,-1.526507,1.821107,-8.442296,-3.604981,-1.120560,2.395354,2.224039,0.364556,-3.767836,7.440374,-4.006461,5.278341,6.956432,-4.999160,-2.684188,3.441780,9.394919,-9.068305,7.380513,-5.214946,7.324491,-6.734668,9.970252,-3.647759,-8.411069,2.680622,-6.442106,5.328149,2.353386,-1.592916,-6.127947,-8.166745,-5.837351,9.314576,-7.093788,1.638345,9.584699,-2.481386,2.510954,5.453859,1.055780,1.417941,4.093979,3.794677,-7.274078,-1.727569,7.726048,-2.669070,4.969302,6.345803,2.006628,-0.446157,-8.542206,2.895464,9.118466,4.154151,2.394525,1.921171,7.272325,2.184619,-5.214846,-1.972712,6.362740,1.520242,-6.466842,-2.231843,9.483436,8.268679,3.900056,5.816111,8.486223], dtype = "float32")#candidate|2903|(640,)|const|float32
call_2902 = relay.TupleGetItem(func_2454_call(relay.reshape(const_2903.astype('float32'), [640,])), 0)
call_2904 = relay.TupleGetItem(func_2456_call(relay.reshape(const_2903.astype('float32'), [640,])), 0)
var_2921 = relay.var("var_2921", dtype = "float32", shape = (13, 9, 15))#candidate|2921|(13, 9, 15)|var|float32
bop_2922 = relay.floor_divide(call_2794.astype('float64'), var_2921.astype('float64')) # shape=(13, 9, 15)
bop_2925 = relay.floor_divide(call_2795.astype('float64'), var_2921.astype('float64')) # shape=(13, 9, 15)
func_1595_call = mod.get_global_var('func_1595')
func_1598_call = mutated_mod.get_global_var('func_1598')
const_2944 = relay.const([8.712625,-9.205212,4.736412,-9.191248,1.121832,-0.617234,0.683447,3.130333,-2.101602,-1.708166,2.201844,-0.210216,0.535112,1.150602,0.505110,1.765305,5.377836,8.379248,3.426387,3.073605,4.104551,2.963465,0.748966,8.371604,6.515807,-8.147023,2.485513,8.218753,9.889867,5.086204,-5.747752,8.030014,-5.972349,6.567488,-1.626150,-6.343432,-6.439080,-8.878508,-8.571803,8.607926,6.441614,-3.241248,-1.939218,-5.391960,8.957777,1.465359,-5.537670,7.088017,0.542916,-0.588109,6.806448,-0.154774,-2.673427,-5.436940,-4.236439,8.191821,5.562429,-3.704452,7.203197,8.080359,-6.178845,3.225392,3.645376,1.341176,9.790498,-2.471843,-5.825277,-4.073107,-5.402568,-2.831471,-3.020321,-0.156616,1.315760,5.837825,6.056647,4.931890,2.992137,-4.123222,-9.176570,-9.556451,-3.350875,-0.023759,1.527571,6.084553,5.109247,-1.601025,3.319071,-9.451777,4.403165,-7.162124,-6.794016,-2.643332,-9.282225,0.731164,-0.690280,-9.506975,-4.202212,1.478230,8.952404,5.381877,-5.860999,-3.620231,2.220540,8.089901,-3.505366,2.049916,5.054812,6.183955,1.739397,-0.750817,-7.455992,-4.524636,-9.702925,-2.757694,-4.400949,-8.317038,8.240884,8.657921,4.119090,5.531767,-8.082474,6.691227,-1.488335,0.221724,9.560268,6.515000,-1.642552,-9.902138,4.880496,-1.019121,3.191649,5.603303,3.248252,2.575884,8.012638,-6.162541,3.028371,3.007882,-2.393731,9.756270,9.230166,2.840332,-5.200430,-4.648315,-0.621611,-7.277655,8.607504,-4.473323,-1.905694,-9.006418,-4.068288,1.325386,-9.422201,2.357668,2.599696,-7.016705,8.558430,-7.453063,2.655597,-1.414860,7.235067,7.560003,-0.454062,1.875997,6.895232,-4.853038,-7.447728,-1.259213,-5.075511,-7.060873,-1.540845,-8.472416,-0.104387,-3.227038,7.023612,-8.977246,9.206576,-5.051285,7.846797,-6.186556,4.990782,2.415162,-5.611585,-6.008618,0.093192,-3.007553,9.389930,-1.980684,8.114681,3.160849,9.425440,9.648988,-9.943513,-1.306295,3.093660,-6.529196,4.194257,-0.511518,7.858550,-7.740118,0.020225,0.042415,-2.862624,9.874627,-5.124029,-4.729553,-5.880236,-6.679562,4.162720,-4.601854,4.965365,2.868899,-5.763522,-2.743718,-1.698517,8.772888,8.208273,-0.306734,-7.604893,0.867663,0.898660,-0.312896,5.876445,-5.890246,1.986633,3.637799,8.384076,8.880497,-0.427160,-5.005244,-4.655867,7.111752,-9.827696,1.266035,2.195166,0.334652,2.555409,-2.978088,-6.379563,9.323228,4.585726,-2.395456,-0.349512,7.562179,0.237453,9.217938,6.207294,9.977670,5.155129,-5.198579,4.589295,6.433997,9.703790,6.581909,-6.506535,6.202961,8.097959,-2.214208,9.402731,-1.366742,3.927647,-6.133440,-0.102223,-8.654588,1.799379,-5.496581,-0.715480,5.818831,1.301264,9.025131,4.181292,-6.066907,-2.241553,-9.836804,-0.405805,-2.616703,0.083257,-5.288929,-2.716287,8.859182,6.684418,-3.346531,5.210602,6.354368,-3.758660,-7.302886,1.948449,-5.649983,2.345755,6.464152,-3.000183,-2.734386,-1.252432,6.895151,8.320125,-8.345403,1.975008,4.768346,-6.525138,2.276290,3.667147,5.566228,-1.350286,1.331164,-4.419835,1.490799,-6.785248,-4.344113,-7.645754,-8.444636,-8.076199,-2.357862,0.193683,-5.503188,-3.556680,0.033293,7.747193,-8.883023,-8.198855,-7.383328,-3.286056,2.940207,0.487627,-8.536782,-6.888743,0.232783,5.826291,-6.556483,4.243690,6.811762,-0.274200,-8.823137,8.896180,-7.265670,-4.793857,-8.234885,-3.418283,2.377906,-2.535613,-4.104757,-2.072303,8.101375,0.303855,8.141226,7.343424,0.309634,0.379760,0.210329,-0.125877,-3.873601,-4.423933,-7.067687,0.566728,-5.991849,2.990739,-8.155024,1.358860,5.814041,2.048761,2.994909,2.925065,-8.519015,-9.711096,4.652726,5.425265,8.585592,1.041087,5.636700,-9.662439,-4.541805,-8.393631,9.504394,-2.880963,-4.648639,2.937421,-6.156134,-4.128990,1.130633,9.898007,-6.742441,4.869561,-9.999242,0.056362,7.585953,-4.289513,2.283714,-6.535012,-7.325106,2.453117,-7.664382,-5.559732,-0.316757,0.280159,-6.252321,-0.685148,-8.385812,-4.834695,-8.825631,-6.709112,3.808699,4.366758,2.347577,-3.215910,1.858452,-1.582499,-7.363904,-1.172597,-5.525030,3.050056,-6.976881,4.907616,7.883928,-5.949796,7.948304,3.100859,3.111580,4.186653,-4.808286,-4.405636,3.777860,6.509291,1.757842,-6.292825,6.517721,-9.584619,-6.426747,-6.926914,-2.969019,8.948030,2.452644,-8.471257,-6.685639,9.033914,3.012562,-2.596572,0.530472,2.826037,8.047183,-9.869621,4.892809,7.268751,-1.501839,6.015813,-8.465990,-4.735292,0.693261,-0.983961,-7.618605,-5.450439,0.776411,-1.117457,-3.803758,5.803954,-3.513280,-0.454142,8.528452,7.173574,-4.119376,-4.697983,2.312570,-5.151154,5.752595,-6.907277,2.273538,-8.170041,1.934677,8.289849,-3.103298,-5.394786,-0.154975,-7.131509,-9.155512,9.476222,-4.396399,9.514182,-6.322281,-4.952697,-9.025005,9.490741,7.430712,-9.186751,-2.815966,-9.957759,-1.123644,9.485338,7.460967,-0.274831,4.159190,-4.407190,4.307215,-1.395305,-0.174030,-6.829254,0.639486,-2.972695,1.263113,-0.456786,-0.291574,-3.580262,1.932139,5.052060,0.437008,-1.603049,7.211278,-5.122324,-0.573581,-6.742630,8.920446,4.685311,-0.734147,7.189626,-4.856047,9.519070,-6.938840,1.656729,-6.191309,-6.770401,1.823095,-8.919963,-1.159321,0.644385,9.319301,9.948657,-0.368003,-7.632015,-0.132147,-6.143241,3.989035,0.208770,6.729201,8.281279,6.593733,8.494632,-3.464001,7.871047,-7.629346,8.053255,-2.489840,-5.343311,6.413436,5.438596,-7.161529,-1.591206,1.013608,6.280798,-4.959999,-8.228734,1.312566,-7.641067,-5.551734,-4.244051,1.176321,-7.309372,-0.037251,-0.142269,1.545305,9.687361,-8.167772,7.245309,3.343344,-1.632692,1.121959,2.891979,2.375572,-1.742097,7.879619,-4.580461,-7.454053,-0.578836,-9.881550,-5.119403,-3.630111,4.152589,0.093735,-2.077366,-2.764527,5.819857,-9.726732,-6.611007,-4.537890,1.273713,8.412525,-7.623814,-4.093944,-4.255574,-0.218929,8.952000,-6.461179,3.530291,5.077617,-6.428802,-5.974929,-1.220212,-6.641293,-6.654906,5.689173,-4.160564,-4.564269,5.378937,3.862401,5.426929,-5.754329,-2.752177,3.708475,8.993105,7.323918,-4.704658,4.193476,-7.995244,6.311760,-9.458145,-1.056844,8.687968,-2.803867,-1.562830,-0.729854,1.949835,-4.838828,6.095783,2.902131,-3.741802,-4.441826,-6.160451,9.653158,6.439089,-1.307759,-0.296814,-2.392523,3.707401,-8.553669,-4.055766,4.466512,8.822199,9.328973,4.737018,0.122291,-0.383082,9.555065,8.851262,4.541439,4.985366,4.176920,8.364764,-3.510534,-5.336810,-1.289178,1.590780,-6.517983,6.659388,-2.108818,-7.302312,-9.498535,3.520154,7.005994,7.638890,-3.153468,-8.845690,-1.957732,3.586215,-2.975258,9.993821,8.683170,-7.941685,7.738710,3.376377,4.028351,-3.289923,-9.058126,4.247151,-3.737620,5.737495,1.674158,-9.204121,9.288448,-1.556486,4.827622,-9.119287,8.392709,-4.169822,-2.260556,-6.809245,3.936620,0.097817,-3.688123,-9.823312,0.346899,9.026420,7.531205,-8.580628,-5.377209,0.123892,-6.104563,-0.668237,-9.306466,2.677669,-3.214683,-9.878417,-2.501949,-1.517398,-7.347400,9.383972,-0.362110,2.335602,4.233263,-0.606919,-0.403508,4.327455,6.474019,-4.822734,1.694006,-4.824939,5.390186,3.937055,-2.221311,4.980959,-0.653987,7.490220,7.051347,8.576131,-9.432239,-3.083275,8.440244,-3.852206,6.864387,-7.358742,-8.080104,3.666667,-8.543160,0.997977,-1.217110,8.316355,6.944932,2.132463,9.519463,2.686786,-5.818920,7.303631,-1.800729,-5.056902,-8.077262,-6.987728,0.619015,6.344491,-3.408918,-7.868177,5.233058,-7.137044,-4.274961,3.260576,-1.941082,-2.320861,4.583625,-8.315409,4.278982,6.739053,5.166199,-4.150847,3.375896,-8.728064,-8.021761,-7.412134,5.440173,-4.326205,-9.813154,8.021236,0.384525,5.893779,9.961381,-8.567082,-8.482702,7.662024,0.169853,-8.187748,9.663195,-9.886409,-4.480970,8.317268,8.763361,4.210426,2.893268,-7.934992,-4.837515,3.886766,8.467759,-9.832274,-8.083264,-1.181048,3.245577,-7.068581,4.595321,-9.901851,-5.252315,6.386311,-5.354789,5.849559,-7.122754,-7.609117,-5.483833,-2.292908,0.917891,6.984100,-2.675510,8.800104,5.154181,-8.120800,-8.451513,-9.385229,-4.234749,7.778866,-3.273995,7.431501,-4.767145,-0.286467,8.512833,9.339418,3.000794,-2.404750,-5.885294,-8.497673,-7.300037,-4.060311,6.574819,1.227669,6.261046,-9.317758,9.740385,-9.533841,2.859435,-3.352001,5.554034,3.031451,7.271249,1.223721,6.650120,6.937482,-9.254123,7.260716,-8.356069,-8.000492,6.471156,2.873767,-0.167165,-6.019326,-5.433347,-4.122050,-6.419437,5.859229,-0.952098,8.043004,-1.905334,9.786196,5.582068,-5.521631,8.298090,6.291728,-8.085281,8.448906,-4.281482,-9.992146,2.201224,-4.227903,0.369005,3.427721,-4.570402,8.387744,4.112773,-6.335829,2.423927,-4.627789,5.634841,1.941834,-8.929379,-0.279059,5.251810,-3.358292,8.438618,-4.989157,-3.176209,-7.612035,2.381154,4.816502,-2.312760,9.732064,-2.861380,-8.360995,2.368419,5.325361,2.706952,-5.840572,4.462517,0.643213,3.634879,4.997639,6.253478,1.568952,5.120140,6.441845,-5.187864,-4.838182,-2.583832,-3.110709,-1.076408,4.940372,6.300531,-0.036435,-0.322474,5.597463,-8.799724,5.366543,1.859281,-5.255684,4.603784,-6.451123,-8.230945,9.187321,-4.509717,-5.182000,5.153447,-2.119095,5.438908,2.815652,-2.932315,4.971828,2.396246,-0.069512,3.363061,-3.167404,-2.026580,-3.570825,7.641999,5.949305,7.394070,-7.699399,1.193290,0.289170,-1.313325,7.024265,-3.988182,9.017068,0.463002,-6.282418,-1.348347,-8.887424,2.698272,2.589458,-4.196948,-1.924573,-9.522789,-4.216479,5.149965,-2.658008,2.048753,-2.319751,-5.445294,3.369455,5.478532,4.497404,-4.744897,-6.465570,-0.582468,-1.856963,-4.657816,5.928718,-2.869815,5.073670,9.766561,4.292561,1.056794,-3.110010,2.226591,0.791332,5.816301,-7.744102,-4.186328,-6.622311,-9.565618,3.017903,3.010091,9.070173,7.050994,-7.285117,-0.487921,6.157335,4.295113,6.058813,1.377535,-4.489799,9.528106,5.429306,8.783260,7.362610,-4.149059,6.693375,8.115122,8.471764,0.161183,2.418476,2.843035,4.832228,9.039278,1.628045,0.718701,1.025966,-2.696341,4.202019,-3.892582,1.185436,4.869824,2.323823,7.076195,2.456972,-1.653039,-7.629697,8.077624,-1.446427,7.545124,-4.833014,6.995171,6.252176,-6.984141,-7.790487,8.037058,1.685063,-9.629803,8.907226,-5.939820,-0.816978,-9.925520,-6.126857,-6.427142,-5.696682,8.053245,-4.845560,-9.910792,-6.370288,-9.516666,-1.280247,1.420062,0.494477,-0.366589,8.664481,3.902636,7.796404,3.487792,-6.809304,-9.296337,1.374165,1.016473,2.078672,5.273285,-8.504530,-7.831774,-4.716653,-0.027284,8.280143,-9.918619,3.389753,-0.500581,2.326205,8.740701,1.853551,-3.839298,8.102090,-4.223740,-5.813430,-0.555392,-7.979819,6.129666,-8.997680,-6.473087,-7.911105,8.452344,-3.089372,-0.165438,3.832550,0.710599,5.991838,5.439829,6.575349,1.538127,0.937852,-0.972800,-7.494014,-7.047856,-0.834241,-9.866423,-1.559673,-1.389948,7.419423,-1.368380,-0.397397,2.846047,-9.436776,-6.547270,2.702294,5.352538,-0.620537,-0.497173,1.628400,1.741025,6.977664,-4.681066,1.109878,-8.006068,6.948287,7.923364,7.792499,9.371384,6.438453,5.785030,-0.604820,-2.243845,6.254865,5.582641,5.020678,-2.714064,1.770008,-8.041924,5.396734,4.248194,-7.432149,6.758994,-0.649097,6.893105,-6.542544,-1.820809,7.941760,9.593994,3.018078,2.125482,-4.906230,8.106185,-9.876036,-9.486899,-9.916142,-6.833684,0.451895,-3.062165,-8.370157,3.647567,0.132786,5.439572,-4.736740,0.933057,-6.256655,1.652069,-9.491525,-7.058835,-3.260343,-1.664808,-3.790572,6.745865,-0.837143,8.609949,9.464953,-8.974515,-0.534788,3.854486,-3.539667,-2.378244,5.338513,7.071923,-9.424219,-4.527097,7.657538,-7.429484,6.239079,5.909755,9.132656,0.249327], dtype = "float32")#candidate|2944|(1170,)|const|float32
call_2943 = relay.TupleGetItem(func_1595_call(relay.reshape(const_2944.astype('float32'), [13, 9, 10]), relay.reshape(var_2825.astype('int8'), [720, 2]), ), 2)
call_2945 = relay.TupleGetItem(func_1598_call(relay.reshape(const_2944.astype('float32'), [13, 9, 10]), relay.reshape(var_2825.astype('int8'), [720, 2]), ), 2)
uop_2949 = relay.sigmoid(var_2860.astype('float64')) # shape=(20, 72)
func_1915_call = mod.get_global_var('func_1915')
func_1917_call = mutated_mod.get_global_var('func_1917')
call_2952 = relay.TupleGetItem(func_1915_call(relay.reshape(uop_2949.astype('int8'), [1440,])), 0)
call_2953 = relay.TupleGetItem(func_1917_call(relay.reshape(uop_2949.astype('int8'), [1440,])), 0)
var_2959 = relay.var("var_2959", dtype = "float64", shape = (20, 72))#candidate|2959|(20, 72)|var|float64
bop_2960 = relay.bitwise_and(uop_2949.astype('int8'), relay.reshape(var_2959.astype('int8'), relay.shape_of(uop_2949))) # shape=(20, 72)
func_1649_call = mod.get_global_var('func_1649')
func_1652_call = mutated_mod.get_global_var('func_1652')
call_2971 = relay.TupleGetItem(func_1649_call(relay.reshape(const_2903.astype('float32'), [640,])), 2)
call_2972 = relay.TupleGetItem(func_1652_call(relay.reshape(const_2903.astype('float32'), [640,])), 2)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_2987 = relay.TupleGetItem(func_1677_call(), 0)
call_2988 = relay.TupleGetItem(func_1678_call(), 0)
output = relay.Tuple([bop_2812,call_2822,call_2824,call_2856,bop_2861,bop_2889,call_2896,call_2902,const_2903,bop_2922,call_2943,const_2944,call_2952,bop_2960,call_2971,call_2987,])
output2 = relay.Tuple([bop_2815,call_2823,call_2826,call_2857,bop_2861,bop_2892,call_2897,call_2904,const_2903,bop_2925,call_2945,const_2944,call_2953,bop_2960,call_2972,call_2988,])
func_3000 = relay.Function([var_2825,var_2860,var_2921,var_2959,], output)
mod['func_3000'] = func_3000
mod = relay.transform.InferType()(mod)
mutated_mod['func_3000'] = func_3000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3000_call = mutated_mod.get_global_var('func_3000')
var_3002 = relay.var("var_3002", dtype = "int8", shape = (20, 72))#candidate|3002|(20, 72)|var|int8
var_3003 = relay.var("var_3003", dtype = "int8", shape = (20, 72))#candidate|3003|(20, 72)|var|int8
var_3004 = relay.var("var_3004", dtype = "float32", shape = (13, 9, 15))#candidate|3004|(13, 9, 15)|var|float32
var_3005 = relay.var("var_3005", dtype = "float64", shape = (20, 72))#candidate|3005|(20, 72)|var|float64
call_3001 = func_3000_call(var_3002,var_3003,var_3004,var_3005,)
output = call_3001
func_3006 = relay.Function([var_3002,var_3003,var_3004,var_3005,], output)
mutated_mod['func_3006'] = func_3006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_3034 = func_122_call()
call_3035 = func_122_call()
output = call_3034
output2 = call_3035
func_3036 = relay.Function([], output)
mod['func_3036'] = func_3036
mod = relay.transform.InferType()(mod)
mutated_mod['func_3036'] = func_3036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mutated_mod.get_global_var('func_3036')
call_3037 = func_3036_call()
output = call_3037
func_3038 = relay.Function([], output)
mutated_mod['func_3038'] = func_3038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_200_call = mod.get_global_var('func_200')
func_201_call = mutated_mod.get_global_var('func_201')
call_3070 = relay.TupleGetItem(func_200_call(), 0)
call_3071 = relay.TupleGetItem(func_201_call(), 0)
output = relay.Tuple([call_3070,])
output2 = relay.Tuple([call_3071,])
func_3093 = relay.Function([], output)
mod['func_3093'] = func_3093
mod = relay.transform.InferType()(mod)
output = func_3093()
func_3094 = relay.Function([], output)
mutated_mod['func_3094'] = func_3094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2389_call = mod.get_global_var('func_2389')
func_2391_call = mutated_mod.get_global_var('func_2391')
call_3095 = relay.TupleGetItem(func_2389_call(), 0)
call_3096 = relay.TupleGetItem(func_2391_call(), 0)
output = relay.Tuple([call_3095,])
output2 = relay.Tuple([call_3096,])
func_3114 = relay.Function([], output)
mod['func_3114'] = func_3114
mod = relay.transform.InferType()(mod)
output = func_3114()
func_3115 = relay.Function([], output)
mutated_mod['func_3115'] = func_3115
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3125 = relay.const([[[-8.058520,0.551023,-8.088159,-9.090143],[8.844781,-5.400641,-2.476891,7.984245],[1.873656,5.722292,6.235551,-8.804831],[5.238406,-9.404880,-0.585872,2.247240],[4.547607,2.823878,8.238767,-2.427362],[5.473652,2.576400,-6.049087,-4.801404],[0.337842,-0.864255,3.435594,-0.740366],[7.249391,-5.712006,-5.752491,6.263033],[-0.388786,-3.972826,-2.498730,-1.843239],[2.166889,7.553431,-8.400920,3.744191],[2.312329,-8.971215,-1.391690,-4.164371],[9.481364,3.132943,-6.492890,6.936413],[-9.638551,-1.707300,0.310040,-1.943378],[-4.557579,-8.293658,5.103045,0.259490]],[[4.958456,0.781754,-8.970772,-2.782140],[-1.297725,6.339785,-6.695039,-8.019098],[-6.911280,3.434349,4.592069,-5.267370],[9.675850,4.831801,9.116010,8.691159],[-6.248427,-4.534679,-4.057298,8.021506],[2.587303,9.331284,6.865390,-0.328781],[4.708635,8.976423,7.412868,-6.049138],[0.005278,-0.811288,-7.533369,3.390779],[-1.033420,8.115482,-8.401990,-0.212573],[-7.586047,3.162526,7.527024,3.450556],[2.396258,4.476668,2.341276,6.052624],[7.700838,5.215960,-9.471422,4.706558],[-6.435350,0.618710,3.114520,-1.054681],[-8.601013,4.510662,0.198969,-4.766866]],[[-5.463852,-5.650533,4.306813,-8.681095],[4.719354,5.570117,-7.581250,-4.961595],[7.528012,-7.180878,9.899269,-1.162574],[-1.081641,9.794711,9.334955,0.082661],[-8.622644,0.522660,4.530794,-9.189722],[9.841182,-6.368599,-9.276783,-2.745104],[1.231515,-5.461731,-8.206125,-8.758012],[0.454069,-6.968807,1.137799,-4.289034],[1.285812,5.389573,9.478608,5.957969],[5.274944,-1.498627,4.664394,-5.596416],[4.245364,9.241407,8.140764,7.409157],[-2.230538,0.487229,6.317933,4.787697],[9.466718,4.357030,-7.871640,2.439160],[6.596733,-4.310881,7.683651,6.286970]]], dtype = "float32")#candidate|3125|(3, 14, 4)|const|float32
uop_3126 = relay.sinh(const_3125.astype('float32')) # shape=(3, 14, 4)
output = relay.Tuple([uop_3126,])
output2 = relay.Tuple([uop_3126,])
func_3133 = relay.Function([], output)
mod['func_3133'] = func_3133
mod = relay.transform.InferType()(mod)
mutated_mod['func_3133'] = func_3133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3133_call = mutated_mod.get_global_var('func_3133')
call_3134 = func_3133_call()
output = call_3134
func_3135 = relay.Function([], output)
mutated_mod['func_3135'] = func_3135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_185_call = mod.get_global_var('func_185')
func_187_call = mutated_mod.get_global_var('func_187')
call_3223 = relay.TupleGetItem(func_185_call(), 0)
call_3224 = relay.TupleGetItem(func_187_call(), 0)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_3235 = relay.TupleGetItem(func_155_call(), 1)
call_3236 = relay.TupleGetItem(func_156_call(), 1)
var_3241 = relay.var("var_3241", dtype = "float32", shape = (13, 9, 1))#candidate|3241|(13, 9, 1)|var|float32
bop_3242 = relay.bitwise_and(call_3235.astype('int64'), relay.reshape(var_3241.astype('int64'), relay.shape_of(call_3235))) # shape=(13, 9, 1)
bop_3245 = relay.bitwise_and(call_3236.astype('int64'), relay.reshape(var_3241.astype('int64'), relay.shape_of(call_3236))) # shape=(13, 9, 1)
output = relay.Tuple([call_3223,bop_3242,])
output2 = relay.Tuple([call_3224,bop_3245,])
func_3266 = relay.Function([var_3241,], output)
mod['func_3266'] = func_3266
mod = relay.transform.InferType()(mod)
mutated_mod['func_3266'] = func_3266
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3267 = relay.var("var_3267", dtype = "float32", shape = (13, 9, 1))#candidate|3267|(13, 9, 1)|var|float32
func_3266_call = mutated_mod.get_global_var('func_3266')
call_3268 = func_3266_call(var_3267)
output = call_3268
func_3269 = relay.Function([var_3267], output)
mutated_mod['func_3269'] = func_3269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_3356 = func_1972_call()
call_3357 = func_1972_call()
output = relay.Tuple([call_3356,])
output2 = relay.Tuple([call_3357,])
func_3375 = relay.Function([], output)
mod['func_3375'] = func_3375
mod = relay.transform.InferType()(mod)
output = func_3375()
func_3376 = relay.Function([], output)
mutated_mod['func_3376'] = func_3376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_3417 = relay.TupleGetItem(func_155_call(), 1)
call_3418 = relay.TupleGetItem(func_156_call(), 1)
output = call_3417
output2 = call_3418
func_3433 = relay.Function([], output)
mod['func_3433'] = func_3433
mod = relay.transform.InferType()(mod)
output = func_3433()
func_3434 = relay.Function([], output)
mutated_mod['func_3434'] = func_3434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_887_call = mod.get_global_var('func_887')
func_888_call = mutated_mod.get_global_var('func_888')
call_3435 = relay.TupleGetItem(func_887_call(), 0)
call_3436 = relay.TupleGetItem(func_888_call(), 0)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_3437 = relay.TupleGetItem(func_1526_call(), 5)
call_3438 = relay.TupleGetItem(func_1527_call(), 5)
output = relay.Tuple([call_3435,call_3437,])
output2 = relay.Tuple([call_3436,call_3438,])
func_3455 = relay.Function([], output)
mod['func_3455'] = func_3455
mod = relay.transform.InferType()(mod)
output = func_3455()
func_3456 = relay.Function([], output)
mutated_mod['func_3456'] = func_3456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_3462 = relay.TupleGetItem(func_1526_call(), 4)
call_3463 = relay.TupleGetItem(func_1527_call(), 4)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_3490 = relay.TupleGetItem(func_1758_call(), 1)
call_3491 = relay.TupleGetItem(func_1759_call(), 1)
output = relay.Tuple([call_3462,call_3490,])
output2 = relay.Tuple([call_3463,call_3491,])
func_3493 = relay.Function([], output)
mod['func_3493'] = func_3493
mod = relay.transform.InferType()(mod)
mutated_mod['func_3493'] = func_3493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3493_call = mutated_mod.get_global_var('func_3493')
call_3494 = func_3493_call()
output = call_3494
func_3495 = relay.Function([], output)
mutated_mod['func_3495'] = func_3495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_493_call = mod.get_global_var('func_493')
func_494_call = mutated_mod.get_global_var('func_494')
call_3515 = relay.TupleGetItem(func_493_call(), 0)
call_3516 = relay.TupleGetItem(func_494_call(), 0)
func_2527_call = mod.get_global_var('func_2527')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_3529 = relay.TupleGetItem(func_2527_call(), 2)
call_3530 = relay.TupleGetItem(func_2528_call(), 2)
func_981_call = mod.get_global_var('func_981')
func_982_call = mutated_mod.get_global_var('func_982')
call_3531 = relay.TupleGetItem(func_981_call(), 0)
call_3532 = relay.TupleGetItem(func_982_call(), 0)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_3557 = func_21_call()
call_3558 = func_21_call()
output = relay.Tuple([call_3515,call_3529,call_3531,call_3557,])
output2 = relay.Tuple([call_3516,call_3530,call_3532,call_3558,])
func_3564 = relay.Function([], output)
mod['func_3564'] = func_3564
mod = relay.transform.InferType()(mod)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3564_call = mutated_mod.get_global_var('func_3564')
call_3565 = func_3564_call()
output = call_3565
func_3566 = relay.Function([], output)
mutated_mod['func_3566'] = func_3566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_308_call = mod.get_global_var('func_308')
func_310_call = mutated_mod.get_global_var('func_310')
call_3643 = relay.TupleGetItem(func_308_call(), 1)
call_3644 = relay.TupleGetItem(func_310_call(), 1)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_3659 = relay.TupleGetItem(func_155_call(), 1)
call_3660 = relay.TupleGetItem(func_156_call(), 1)
func_2127_call = mod.get_global_var('func_2127')
func_2131_call = mutated_mod.get_global_var('func_2131')
var_3686 = relay.var("var_3686", dtype = "uint32", shape = (1638,))#candidate|3686|(1638,)|var|uint32
const_3687 = relay.const([-6.267926,2.179914,1.590149,5.599267,-0.072722,7.335192,9.297423,-6.932167,-1.929017,-7.169956,5.339078,9.241757,5.072607,-6.269564,2.581830,-3.809423,-3.581885,3.437781,-1.670319,5.179860,-8.104579,7.122213,5.099180,2.381168,-5.395798,9.214753,7.896578,8.118802,-8.116319,1.668774,-8.244466,1.135192,-2.034211,-6.340974,-7.430819,0.844285,-0.658630,-1.846609,-7.408775,1.032248,8.755969,-0.905008,3.658949,1.907369,1.786027,6.227131,-5.980942,-7.013795,-6.941216,6.298916,8.468511,9.234706,1.433366,9.306664,3.079682,-0.213641,9.537742,6.592022,-0.109082,-4.353482,-9.048610,8.586576,-2.686618,7.516014,-3.527146,8.353680,5.544060,8.809046,-9.924237,-3.180309,2.849321,-3.291632,-1.578723,-0.221505,-8.770048,-0.003961,-5.360645,8.391966,-4.476512,7.533109,-6.814266,-9.641353,1.198347,-1.810479,-7.092126,4.549211,-3.323698,-0.363492,-4.412984,6.368472,3.503042,8.424007,-9.952237,-6.615375,3.841925,7.335418,9.048010,7.017875,-7.530477,-7.104029,-6.748162,-9.378697,-3.192537,9.536883,1.149473,8.854908,4.028444,9.752349,-6.104518,-6.819088,6.187698,5.009601,5.093913,-9.630665,-4.897665,-0.786946,-8.040089,2.966325,2.877025,5.903827,-9.324490,7.481603,7.390193,7.119791,-7.641987,7.936840,2.923433,-3.598276,1.340232,-3.606489,-2.206646,5.144454,-7.757426,5.033603,9.031001,-0.414892,4.386985,4.938710,-7.803163,-7.818687,-4.850745,5.714013,-7.959893,-9.165831,-0.740168,-7.129721,6.863249,5.812028,-5.250887,8.501269,-3.781352,9.869356,0.887275,-2.764081,4.826054,9.334958,6.987032,-0.058581,-8.456552,6.435460,2.686201,6.578560,1.165637,-7.167310,8.573994,-7.333252,-9.635180,-0.694837,-7.219057,1.940077,2.792928,-7.168640,0.973855,1.000191,2.467351,-5.856590,-0.510660,-6.187800,5.705752,9.882627,-5.583243,-0.941705,-6.661262,0.748471,0.668216,-7.399074,0.655146,9.195870,1.331210,-0.038100,-4.624472,-9.476234,6.083840,-6.174777,6.460642,4.443002,2.110582,-4.003183,-2.631233,4.696631,9.978567,4.515736,-9.708824,7.741964,8.805589,-2.386503,2.419084,-7.877657,2.256813,8.280630,-6.265237,7.848608,-9.059423,0.428614,3.451755,-0.611169,8.037879,7.004358,8.092239,1.677040,-6.617004,-5.578693,-9.664455,-6.713901,8.973130,5.733344,8.527173,-2.035140,-4.436062,-4.470620,-5.507311,-0.410228,-4.849032,0.192150,1.907892,-4.138094,-4.907340,7.812812,5.672930,5.734129,4.192648,0.162104,9.715886,-8.192750,8.903270,5.109015,3.513118,2.155304,4.589935,0.213466,-7.581276,-7.866614,-2.975305,7.105685,-1.581911,1.668067,5.303885,-5.863397,-5.523738,1.600893,5.815115,2.988453,-6.015164,6.458152,9.886919,-7.121303,-5.249452,-9.882343,-0.938404,2.315961,-4.853127,-8.766888,0.387302,-2.619166,1.895577,6.637115,-1.954839,-5.070919,-0.495529,-9.150096,-7.717005,8.561676,-0.681056,-6.021647,8.167765,7.745077,-6.746500,-9.832763,-0.545779,7.107967,-5.299980,-3.567308,5.605100,6.378226,-9.476846,1.010405,0.554869,-5.991461,-1.121899,-8.215944,-3.573815,-2.336181,-8.230181,-9.623791,3.672234,-7.536403,-1.298057,7.248326,4.051979,1.297836,-1.759172,9.772310,9.973621,7.392418,-0.074781,-6.776684,7.448138,7.875753,6.013447,-9.001057,5.036858,-6.388622,-1.225363,0.019961,-4.555398,7.552683,0.022679,-7.377919,-2.616474,-9.049386,-5.006041,3.084696,3.238815,9.014869,-1.356982,-9.375091,-2.551892,-3.037467,-6.655252,4.076801,-5.740634,9.452657,9.970022,2.283030,-4.306775,-4.305435,-2.146474,-4.729777,-2.710582,-3.592466,-6.780388,-4.215966,7.338657,1.731331,-7.256929,-4.566142,4.641097,-4.422902,-1.111867,0.641139,6.782215,5.102288,5.183189,-2.123023,8.283539,0.842226,4.413866,-4.161673,-1.800392,-9.616895,-5.953141,1.553478,-5.492927,-0.923031,0.740108,5.920719,9.988602,-0.512191,5.423736,-8.273205,9.917245,-4.590249,0.814297,1.211851,-2.464206,-9.579747,4.245432,-2.341349,1.568983,-1.833270,-1.209566,-0.559670,-3.809312,4.019488,6.427390,-4.565325,1.313039,1.431624,0.156971,-0.898701,-4.005410,0.300713,-8.479799,9.289183,-1.964493,3.209192,-0.998437,8.533497,-5.362154,-6.363834,-3.061456,9.894728,3.021228,3.947553,3.770398,-0.706231,-7.554339,4.781578,2.109751,9.158215,-6.200637,1.191375,-3.235233,7.281304,4.924790,-1.216936,-6.338371,5.841578,-5.638017,1.643471,-1.548025,2.411532,4.528055,0.627284,8.377206,-2.520078,9.796819,-5.414438,-8.168254,5.859765,8.333842,-7.909888,7.894233,1.023574,-5.770858,7.372254,-5.748773,5.447738,-7.542547,6.193455,3.860869,1.436312,4.439955,-7.526534,-1.804718,8.766026,1.274428,5.480687,7.604873,-6.007038,1.953914,-6.499642,-0.118562,5.006657,-0.063182,2.984293,0.700727,8.817611,-9.614475,-0.054769,8.134470,1.156087,8.397038,9.830350,6.077650,-0.635267,1.997130,7.820361,2.516387,-3.914675,1.836951,5.145848,7.798190,1.911503,8.007210,-3.552217,1.446437,4.792349,-3.735657,9.229719,1.591651,0.603044,-1.761349,-5.367576,6.970381,4.701975,-1.749447,0.573251,4.459239,-2.155122,7.320673,5.529305,-0.558513,9.455025,2.197287,-9.314432,9.529397,-3.936036,-5.041851,0.738988,1.102226,-8.159093,3.398012,7.274887,-2.685277,8.816938,-2.196851,-2.529429,-7.912804,-4.651447,-2.851756,-5.213262,-0.494723,0.209627,2.245825,-0.503610,-0.702491,5.568742,9.745719,-1.418392,-0.761082,2.637691,5.775368,0.326659,6.577598,9.307416,-8.851073,4.929194,-3.797774,-0.254485,1.997076,8.269469,8.548738,-0.874632,8.789691,1.205626,-7.634863,2.583761,-3.478824,7.844440,-6.453496,-9.674484,-2.664292,9.611510,-2.057240,7.373195,-9.549727,2.255719,3.773519,-8.838177,2.512924,-6.333873,-9.316725,5.330472,-0.068314,5.086835,5.357178,9.048640,4.090022,4.860509,-7.603619,-4.924791,8.262873,7.243549,1.682500,0.479158,4.946241,-9.748624,0.783516,-2.403415,1.034208,-6.081495,7.305459,-0.749352,-3.360042,1.367259,-0.241528,-7.464862,4.589764,-8.624183,3.493923,3.783308,4.715949,5.156867,7.222531,-7.019964,4.233665,-6.769415,0.143656,1.798263,-3.504558,-0.114240,-0.205953,-3.885315,-9.312750,-2.447061,-8.680796,-5.886997,-0.864552,4.275771,-9.818938,-4.670777,-9.177502,-3.076824,8.791321,-7.682503,-3.493530,2.580022,1.803409,7.524234,-8.122399,7.971414,2.143895,6.009454,1.781281,-0.194104,-6.902846,5.269595,2.567196,-2.063652,-6.791069,-9.753684,-1.806557,4.334636,0.542854,4.954929,2.576443,-1.975024,4.118094,-6.004463], dtype = "float32")#candidate|3687|(640,)|const|float32
call_3685 = relay.TupleGetItem(func_2127_call(relay.reshape(var_3686.astype('uint32'), [13, 9, 14]), relay.reshape(const_3687.astype('float32'), [640,]), ), 3)
call_3688 = relay.TupleGetItem(func_2131_call(relay.reshape(var_3686.astype('uint32'), [13, 9, 14]), relay.reshape(const_3687.astype('float32'), [640,]), ), 3)
func_3266_call = mod.get_global_var('func_3266')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_3691 = relay.TupleGetItem(func_3266_call(relay.reshape(call_3643.astype('float32'), [13, 9, 1])), 0)
call_3692 = relay.TupleGetItem(func_3269_call(relay.reshape(call_3643.astype('float32'), [13, 9, 1])), 0)
output = relay.Tuple([call_3643,call_3659,call_3685,var_3686,const_3687,call_3691,])
output2 = relay.Tuple([call_3644,call_3660,call_3688,var_3686,const_3687,call_3692,])
func_3696 = relay.Function([var_3686,], output)
mod['func_3696'] = func_3696
mod = relay.transform.InferType()(mod)
mutated_mod['func_3696'] = func_3696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3697 = relay.var("var_3697", dtype = "uint32", shape = (1638,))#candidate|3697|(1638,)|var|uint32
func_3696_call = mutated_mod.get_global_var('func_3696')
call_3698 = func_3696_call(var_3697)
output = call_3698
func_3699 = relay.Function([var_3697], output)
mutated_mod['func_3699'] = func_3699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1997_call = mod.get_global_var('func_1997')
func_1999_call = mutated_mod.get_global_var('func_1999')
call_3744 = func_1997_call()
call_3745 = func_1997_call()
func_1915_call = mod.get_global_var('func_1915')
func_1917_call = mutated_mod.get_global_var('func_1917')
var_3778 = relay.var("var_3778", dtype = "int8", shape = (1440,))#candidate|3778|(1440,)|var|int8
call_3777 = relay.TupleGetItem(func_1915_call(relay.reshape(var_3778.astype('int8'), [1440,])), 0)
call_3779 = relay.TupleGetItem(func_1917_call(relay.reshape(var_3778.astype('int8'), [1440,])), 0)
uop_3813 = relay.sigmoid(call_3777.astype('float32')) # shape=(160, 4)
uop_3815 = relay.sigmoid(call_3779.astype('float32')) # shape=(160, 4)
output = relay.Tuple([call_3744,var_3778,uop_3813,])
output2 = relay.Tuple([call_3745,var_3778,uop_3815,])
func_3832 = relay.Function([var_3778,], output)
mod['func_3832'] = func_3832
mod = relay.transform.InferType()(mod)
var_3833 = relay.var("var_3833", dtype = "int8", shape = (1440,))#candidate|3833|(1440,)|var|int8
output = func_3832(var_3833)
func_3834 = relay.Function([var_3833], output)
mutated_mod['func_3834'] = func_3834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_3836 = relay.TupleGetItem(func_1677_call(), 0)
call_3837 = relay.TupleGetItem(func_1678_call(), 0)
output = relay.Tuple([call_3836,])
output2 = relay.Tuple([call_3837,])
func_3852 = relay.Function([], output)
mod['func_3852'] = func_3852
mod = relay.transform.InferType()(mod)
output = func_3852()
func_3853 = relay.Function([], output)
mutated_mod['func_3853'] = func_3853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_493_call = mod.get_global_var('func_493')
func_494_call = mutated_mod.get_global_var('func_494')
call_3890 = relay.TupleGetItem(func_493_call(), 0)
call_3891 = relay.TupleGetItem(func_494_call(), 0)
var_3928 = relay.var("var_3928", dtype = "float32", shape = (13, 9, 1))#candidate|3928|(13, 9, 1)|var|float32
bop_3929 = relay.divide(call_3890.astype('float32'), relay.reshape(var_3928.astype('float32'), relay.shape_of(call_3890))) # shape=(13, 9, 1)
bop_3932 = relay.divide(call_3891.astype('float32'), relay.reshape(var_3928.astype('float32'), relay.shape_of(call_3891))) # shape=(13, 9, 1)
output = relay.Tuple([bop_3929,])
output2 = relay.Tuple([bop_3932,])
func_3938 = relay.Function([var_3928,], output)
mod['func_3938'] = func_3938
mod = relay.transform.InferType()(mod)
mutated_mod['func_3938'] = func_3938
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3939 = relay.var("var_3939", dtype = "float32", shape = (13, 9, 1))#candidate|3939|(13, 9, 1)|var|float32
func_3938_call = mutated_mod.get_global_var('func_3938')
call_3940 = func_3938_call(var_3939)
output = call_3940
func_3941 = relay.Function([var_3939], output)
mutated_mod['func_3941'] = func_3941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_4025 = relay.TupleGetItem(func_1526_call(), 0)
call_4026 = relay.TupleGetItem(func_1527_call(), 0)
output = relay.Tuple([call_4025,])
output2 = relay.Tuple([call_4026,])
func_4032 = relay.Function([], output)
mod['func_4032'] = func_4032
mod = relay.transform.InferType()(mod)
output = func_4032()
func_4033 = relay.Function([], output)
mutated_mod['func_4033'] = func_4033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_4063 = func_21_call()
call_4064 = func_21_call()
output = call_4063
output2 = call_4064
func_4078 = relay.Function([], output)
mod['func_4078'] = func_4078
mod = relay.transform.InferType()(mod)
mutated_mod['func_4078'] = func_4078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4078_call = mutated_mod.get_global_var('func_4078')
call_4079 = func_4078_call()
output = call_4079
func_4080 = relay.Function([], output)
mutated_mod['func_4080'] = func_4080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_4092 = func_3036_call()
call_4093 = func_3036_call()
output = relay.Tuple([call_4092,])
output2 = relay.Tuple([call_4093,])
func_4109 = relay.Function([], output)
mod['func_4109'] = func_4109
mod = relay.transform.InferType()(mod)
output = func_4109()
func_4110 = relay.Function([], output)
mutated_mod['func_4110'] = func_4110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_4114 = relay.TupleGetItem(func_2626_call(), 0)
call_4115 = relay.TupleGetItem(func_2627_call(), 0)
const_4127 = relay.const([-5,10,6,1,-5,-9,-10,-4,4,-6,-5,-5,-4,7,6,-5,-6,5,8,4,-10,8,8,8,-7,4,-9,2,-2,1,8,10,-1,-8,2,-2,-6,4,-10,10,7,1,1,-9,6,-2,8,-10,7,-5,3,3,8,5,-10,-9,-9,2,6,4,3,-6,-5,9,-8,5,4,1,5,-3,-1,1,3,-9,-9,2,-6,-5,7,-7,10,6,-1,-9,-5,1,-5,7,10,-10,8,10,-2,-8,-9,-6,8,7,1,6,-8,-3,1,-4,5,-7,6,8,2,-7,-3,-4,-6,-8,6,-4,-3,9,8,-5,7,-7,-1,1,3,6,2,6,-2,-5,-8,-5,10,5,9,-1,1,-1,3,8,3,-3,-6,3,3,6,-8,4,-5,6,-8,2,4,-2,7,-4,-5,-5,6,-9,-7,10,-6,-3,-3,6,-5,1,-4,-8,-4,-3,-9,-10,-8,2,1,-1,6,9,5,1,4,1,6,10,2,-8,4,6,4,7,1,4,4,-9,7,-8,1,-10,9,-6,3,-3,-2,9,8,3,4,9,1,6,7,10,5,4,9,-6,5,-1,8,-3,6,8,-5,5,-6,-3,-4,2,2,3,7,8,-9,-9,9,-5,-9,-4,-9,-10,9,-9,-6,-4,6,-4,9,7,10,-4,7,5,-2,2,-7,8,6,3,-8,-10,4,-9,5,10,-1,4,4,6,8,7,8,5,3,-6,3,-5,-10,-10,2,10,-6,9,-6,6,-3,-1,-10,-5,-4,-4,-8,6,3,3,-7,9,9,-3,-3,9,6,8,-8,-9,-5,1,-1,-1,4,10,-7,5,6,-1,1,-6,-1,2,-7,-2,-3,-4,-10,9,-9,5,9,-3,10,-6,3,-7,-8,4,8,-8,10,5,8,-4,-2,-4,9,-6,1,-9,5,1,-4,9,-10,5,2,10,2,9,-2,-3,-2,1,10,-2,-7,8,-7,-3,5,-8,6,7,3,1,10,-8,2,10,1,-7,-4,-10,-2,-9,-1,-2,-7,4,-6,5,9,-10,5,1,1,-6,2,5,9,1,-3,6,3,-9,-6,-2,-10,-6,-2,2,-6,8,6,-2,-7,4,5,9,-1,4,5,-2,10,-3,-4,6,5,8,7,-6,-2,-6,10,4,6,-1,-5,7,1,-2,6,7,-3,-3,-4,5,-9,4,6,3,5,4,-4,-9,-2,-2,-10,10,-3,-2,-1,-4,9,10,-5,9,6,3,-6,-7,-5,5,-5,7,-7,6,7,10,7,3,-2,5,8,10,-2,2,-3,3,3,7,-10,-2,10,-4,2,2,-4,4,4,-5,8,-4,-6,10,-6,3,-7,-4,5,-5,-7,-2,3,-2,9,-3,-7,-7,-5,-6,1,6,2,-6,-10,-5,9,10,3,-1,1,9,-3,5,-3,-9,-10,-4,-7,-1,-3,-7,-4,-4,-9,9,-9,2,-5,9,7,6,-3,10,-3,8,-9,-8,-2,-10,-5,4,9,5,-2,4,2,-7,-10,-6,9,-9,-1,-1,-9,-5,-2,-10,5,-5,-2,8,-8,-1,-3,-3,3,3,9,8,-5,-2,-3,7,10,5,-10,-5,8,-9,3,5,4,-1,-2,-2,-3,5,7,-2,-6,8,-9,-8,-9,8,-9,-7,1,-7,-6,-1,3,4,1,-8,2,7,-9,6,2,-9,7,5,5,-2,-2,9,-10,-7,9,-8,-1,2,-9,-7,4,-1,3,10,7,8,-4,7,10,-5,-9,-9,7,8,2,7,3,-9,-2,-2,-9,-10,-7,-7,1,5,-4,-8,-8,8,-4,-7,3,-3,5,5,6,-8,-4,-2,-6,3,-5,-2,-9,-4,5,10,-9,2,10,7,5,-1,-10,-4,-1,-6,-9,-9,7,3,-7,2,8,10,-3,4,-4,-9,-9,3,-1,8,5,10,3,8,8,5,-3,-4,4,8,-4,-4,-1,4,-4,-2,10,-5,-7,2,-2,-3,-4,3,4,7,10,2,-6,1,-9,-3,9,9,-10,5,-7,-6,5,6,3,-9,5,-2,8,-5,10,-3,5,-9,2,-6,10,10,3,7,1,9,-7,-9,8,-1,1,1,7,-2,2,10,1,-9,7,-2,-2,-4,-4,4,-6,-2,1,4,1,-1,-5,-7,2,-3,-4,7,6,4,6,-3,7,3,9,7,5,-5,10,9,1,-1,4,10,-3,9,-6,-6,-8,-10,6,8,-7,6,-8,1,6,4,-2,-2,-1,-6,3,-8,9,-9,7,-10,2,-6,-10,10,9,-6,10,-9,8,8,7,4,5,-3,-3,-9,-9,-7,-1,5,-3,-4,6,4,7,7,7,2,-7,4,-9,6,9,-9,2,-2,-2,8,8,-3,-3,10,4,-1,8,2,10,7,3,10,1,-10,8,2,7,2,-8,9,-6,-2,6,6,-3,-3,-1,2,5,-5,-10,-9,-4,9,7,3,-8,10,2,8,-8,-4,6,-1,7,-5,4,-4,-7,2,10,-7,-2,-2,2,-10,5,-1,1,1,1,5,-2,-6,3,-2,5,3,8,-4,7,3,9,2,-10,-7,1,-6,4,-1,-2,-2,-2,-8,2,1,9,1,9,-9,-8,-8,10,-1,8,1,-5,-10,-8,5,2,9,-9,-1,-8,5,-7,-7,7,-1,-2,-4,5,-3,-2,-3,4,10,-6,2,-1,10,-10,-7,4,1,-2,10,10,-2,-2,1,-1,-9,-9,-1,-8,2,-7,-6,-9,-5,-3,-10,-10,7,9,10,-8,7,2,10,8,-9,-3,5,3,4,-7,-10,7,9,-5,6,-7,-1,-10], dtype = "uint32")#candidate|4127|(1053,)|const|uint32
bop_4128 = relay.floor_mod(call_4114.astype('float32'), relay.reshape(const_4127.astype('float32'), relay.shape_of(call_4114))) # shape=(1053,)
bop_4131 = relay.floor_mod(call_4115.astype('float32'), relay.reshape(const_4127.astype('float32'), relay.shape_of(call_4115))) # shape=(1053,)
output = relay.Tuple([bop_4128,])
output2 = relay.Tuple([bop_4131,])
func_4133 = relay.Function([], output)
mod['func_4133'] = func_4133
mod = relay.transform.InferType()(mod)
output = func_4133()
func_4134 = relay.Function([], output)
mutated_mod['func_4134'] = func_4134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3093_call = mod.get_global_var('func_3093')
func_3094_call = mutated_mod.get_global_var('func_3094')
call_4188 = relay.TupleGetItem(func_3093_call(), 0)
call_4189 = relay.TupleGetItem(func_3094_call(), 0)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_4196 = func_122_call()
call_4197 = func_122_call()
output = relay.Tuple([call_4188,call_4196,])
output2 = relay.Tuple([call_4189,call_4197,])
func_4202 = relay.Function([], output)
mod['func_4202'] = func_4202
mod = relay.transform.InferType()(mod)
mutated_mod['func_4202'] = func_4202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4202_call = mutated_mod.get_global_var('func_4202')
call_4203 = func_4202_call()
output = call_4203
func_4204 = relay.Function([], output)
mutated_mod['func_4204'] = func_4204
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4294 = relay.var("var_4294", dtype = "float64", shape = (5, 4, 14))#candidate|4294|(5, 4, 14)|var|float64
uop_4295 = relay.acos(var_4294.astype('float64')) # shape=(5, 4, 14)
func_3433_call = mod.get_global_var('func_3433')
func_3434_call = mutated_mod.get_global_var('func_3434')
call_4314 = func_3433_call()
call_4315 = func_3433_call()
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_4358 = relay.TupleGetItem(func_2421_call(), 0)
call_4359 = relay.TupleGetItem(func_2422_call(), 0)
output = relay.Tuple([uop_4295,call_4314,call_4358,])
output2 = relay.Tuple([uop_4295,call_4315,call_4359,])
func_4360 = relay.Function([var_4294,], output)
mod['func_4360'] = func_4360
mod = relay.transform.InferType()(mod)
mutated_mod['func_4360'] = func_4360
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4361 = relay.var("var_4361", dtype = "float64", shape = (5, 4, 14))#candidate|4361|(5, 4, 14)|var|float64
func_4360_call = mutated_mod.get_global_var('func_4360')
call_4362 = func_4360_call(var_4361)
output = call_4362
func_4363 = relay.Function([var_4361], output)
mutated_mod['func_4363'] = func_4363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_493_call = mod.get_global_var('func_493')
func_494_call = mutated_mod.get_global_var('func_494')
call_4365 = relay.TupleGetItem(func_493_call(), 0)
call_4366 = relay.TupleGetItem(func_494_call(), 0)
output = relay.Tuple([call_4365,])
output2 = relay.Tuple([call_4366,])
func_4404 = relay.Function([], output)
mod['func_4404'] = func_4404
mod = relay.transform.InferType()(mod)
output = func_4404()
func_4405 = relay.Function([], output)
mutated_mod['func_4405'] = func_4405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_4432 = relay.TupleGetItem(func_76_call(), 1)
call_4433 = relay.TupleGetItem(func_77_call(), 1)
func_3000_call = mod.get_global_var('func_3000')
func_3006_call = mutated_mod.get_global_var('func_3006')
var_4436 = relay.var("var_4436", dtype = "int8", shape = (1440,))#candidate|4436|(1440,)|var|int8
var_4437 = relay.var("var_4437", dtype = "float32", shape = (1755,))#candidate|4437|(1755,)|var|float32
call_4435 = relay.TupleGetItem(func_3000_call(relay.reshape(var_4436.astype('int8'), [20, 72]), relay.reshape(var_4436.astype('int8'), [20, 72]), relay.reshape(var_4437.astype('float32'), [13, 9, 15]), relay.reshape(var_4436.astype('float64'), [20, 72]), ), 2)
call_4438 = relay.TupleGetItem(func_3006_call(relay.reshape(var_4436.astype('int8'), [20, 72]), relay.reshape(var_4436.astype('int8'), [20, 72]), relay.reshape(var_4437.astype('float32'), [13, 9, 15]), relay.reshape(var_4436.astype('float64'), [20, 72]), ), 2)
func_2651_call = mod.get_global_var('func_2651')
func_2652_call = mutated_mod.get_global_var('func_2652')
call_4447 = func_2651_call()
call_4448 = func_2651_call()
uop_4454 = relay.erf(var_4437.astype('float32')) # shape=(1755,)
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_4457 = relay.TupleGetItem(func_76_call(), 2)
call_4458 = relay.TupleGetItem(func_77_call(), 2)
bop_4462 = relay.greater_equal(uop_4454.astype('bool'), call_4457.astype('bool')) # shape=(13, 9, 1755)
bop_4465 = relay.greater_equal(uop_4454.astype('bool'), call_4458.astype('bool')) # shape=(13, 9, 1755)
func_3493_call = mod.get_global_var('func_3493')
func_3495_call = mutated_mod.get_global_var('func_3495')
call_4470 = relay.TupleGetItem(func_3493_call(), 0)
call_4471 = relay.TupleGetItem(func_3495_call(), 0)
func_185_call = mod.get_global_var('func_185')
func_187_call = mutated_mod.get_global_var('func_187')
call_4476 = relay.TupleGetItem(func_185_call(), 0)
call_4477 = relay.TupleGetItem(func_187_call(), 0)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_4479 = func_1128_call()
call_4480 = func_1128_call()
bop_4491 = relay.logical_and(uop_4454.astype('bool'), call_4479.astype('bool')) # shape=(13, 9, 1755)
bop_4494 = relay.logical_and(uop_4454.astype('bool'), call_4480.astype('bool')) # shape=(13, 9, 1755)
func_3266_call = mod.get_global_var('func_3266')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_4509 = relay.TupleGetItem(func_3266_call(relay.reshape(call_4432.astype('float32'), [13, 9, 1])), 0)
call_4510 = relay.TupleGetItem(func_3269_call(relay.reshape(call_4432.astype('float32'), [13, 9, 1])), 0)
output = relay.Tuple([call_4432,call_4435,var_4436,call_4447,bop_4462,call_4470,call_4476,bop_4491,call_4509,])
output2 = relay.Tuple([call_4433,call_4438,var_4436,call_4448,bop_4465,call_4471,call_4477,bop_4494,call_4510,])
func_4514 = relay.Function([var_4436,var_4437,], output)
mod['func_4514'] = func_4514
mod = relay.transform.InferType()(mod)
var_4515 = relay.var("var_4515", dtype = "int8", shape = (1440,))#candidate|4515|(1440,)|var|int8
var_4516 = relay.var("var_4516", dtype = "float32", shape = (1755,))#candidate|4516|(1755,)|var|float32
output = func_4514(var_4515,var_4516,)
func_4517 = relay.Function([var_4515,var_4516,], output)
mutated_mod['func_4517'] = func_4517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_4582 = func_21_call()
call_4583 = func_21_call()
output = relay.Tuple([call_4582,])
output2 = relay.Tuple([call_4583,])
func_4589 = relay.Function([], output)
mod['func_4589'] = func_4589
mod = relay.transform.InferType()(mod)
output = func_4589()
func_4590 = relay.Function([], output)
mutated_mod['func_4590'] = func_4590
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4618 = relay.const([[[5.425701,6.666861,-3.976726,7.480527,-6.690115,2.845716,-7.951680,-9.674562,-5.340005,-8.759289],[-5.524909,-2.939924,9.985407,-3.083606,8.048607,-0.839625,4.073296,-7.097092,-5.884724,6.177532],[-1.752465,-3.738806,8.296315,-9.787058,-9.314115,-9.463426,1.270653,1.224219,4.455432,-4.897689],[-5.023321,3.782539,4.934145,8.489914,-4.190357,-5.540674,8.107391,8.512308,-2.996328,-5.944919],[-3.883728,5.398720,2.811927,8.319651,8.723400,-3.235977,-0.182318,1.079448,7.626537,3.118486],[7.536346,-8.381785,5.467281,7.142302,2.436869,-0.094452,0.477555,-4.307123,9.795863,5.925574],[9.736528,-0.333678,0.955841,6.344350,-4.056911,-9.254846,1.826310,-2.777381,2.303390,-1.007501],[1.408262,-4.856352,-9.578386,4.159930,-0.765596,-2.143330,-8.041106,2.316767,5.674946,-3.294961],[-3.390850,0.104476,-5.168077,-4.729744,-2.078861,-8.732255,6.217533,-3.895237,9.097203,2.033169],[-0.051141,-7.814419,-3.813541,-0.413292,-2.283033,8.939144,-0.062863,-1.886074,-6.074443,-4.775375],[9.390360,-4.866289,4.808263,6.135319,7.463199,3.116686,-9.031941,-1.977149,1.205768,-7.868149],[-9.023119,-1.254614,2.210321,6.765580,3.808726,-0.010746,-1.573809,-2.908498,7.017252,3.793596],[-4.800742,-0.341917,-7.927745,-0.230298,4.779407,6.824196,-0.173747,-1.354076,8.644849,-7.267176],[7.888286,9.550480,1.297239,-3.812843,5.659560,6.760931,-7.936750,0.207545,7.595443,-1.446731],[-7.831473,-5.409605,-1.841459,-6.026704,-3.219653,-4.778371,9.583757,5.950967,4.221341,2.831203]],[[5.133916,1.319948,-2.970294,-0.752149,-1.887227,4.715591,3.770724,6.341571,-3.737723,6.467981],[-8.391591,3.698017,7.373460,5.929351,-3.741155,-8.888938,7.104449,7.395606,-0.866374,1.657665],[-1.544566,3.655778,-0.425541,4.863016,1.877897,0.300568,3.622222,9.355310,-6.195762,9.270801],[-4.153405,-6.846412,4.061200,9.862227,-8.204157,-7.631322,2.629425,-5.845144,5.800603,3.091067],[-5.780985,-1.710098,4.755716,-5.699144,-8.091186,-2.277805,3.079778,2.723241,-6.404103,-7.651803],[4.575541,4.813930,6.579423,0.762536,-8.476605,2.584012,3.644331,-6.259586,5.614497,-6.219405],[-5.451304,-0.750232,-8.262223,0.245695,5.273843,4.566242,-8.297327,6.229945,-5.841331,-4.427538],[1.717354,7.901218,-6.498824,5.665599,-6.879937,1.107986,-6.851811,1.916088,7.892840,8.852803],[-3.943302,-7.204467,-4.163342,-8.543754,-2.397333,4.216858,-0.274106,-0.832583,-3.637408,1.595817],[-1.311820,0.612088,-5.849623,1.444427,8.341536,-4.016264,3.089287,3.397865,5.081883,-5.152240],[-2.220013,4.364392,-9.306655,6.544947,-4.310253,4.433990,-5.484854,4.861039,2.707240,-4.135860],[-8.112556,4.212543,9.544235,8.837759,-9.153252,-8.927289,7.982568,-2.630859,-0.442657,-5.136707],[-6.171270,2.126506,-7.197017,3.528931,2.108814,8.365921,4.356400,9.182011,0.698024,1.755442],[-4.978310,-4.906238,7.463229,6.183626,6.892338,-7.632998,8.407688,-0.434906,8.417301,-2.519475],[3.556433,-4.830821,-2.895384,-3.044260,-7.781245,1.657497,1.708821,-4.963897,-3.745452,-4.157648]],[[6.373322,4.720969,-1.818111,-5.403377,-8.589244,-5.826422,-7.169363,-4.343159,-8.448130,-4.648945],[-9.632230,9.080163,-8.834691,-3.070680,7.452450,-1.494667,-3.018587,-1.532069,5.855687,-4.414198],[1.975469,8.815181,0.239616,-8.924605,-8.333435,-0.724070,-0.088357,4.352196,3.286749,-4.944542],[-5.767506,4.543044,-8.121330,-2.213409,-3.915295,1.591314,0.671515,-7.878036,-5.283520,0.481781],[6.012382,9.049213,9.339087,-2.918636,6.643184,-4.151970,6.803108,-4.566415,7.083820,8.515961],[3.733670,0.418249,-2.752031,0.863301,-6.381662,8.768303,-7.200029,7.553111,4.310596,-6.355347],[-9.129076,2.043959,-2.821083,-3.597237,-7.907645,0.893722,-2.398551,-6.391858,-8.580144,-7.371068],[-2.749079,6.891504,-1.032129,1.313767,-5.554129,-1.059932,-7.365024,7.765693,7.024761,-9.623979],[4.682678,9.109869,-7.508976,-9.292452,1.571486,7.295347,4.358597,-3.579231,0.523277,1.697339],[5.755969,4.760495,7.440921,-1.078788,-2.159378,-3.299022,3.800045,6.512564,-6.328010,-6.623846],[-7.093534,3.757242,-7.165988,-0.543395,7.132638,-4.582839,9.949013,-2.284074,-9.270601,-7.010191],[8.230818,-6.995334,-7.306898,-3.658281,-7.757154,7.025576,-2.204256,-4.332714,-3.046455,2.831158],[-0.800376,7.082488,9.377807,5.725763,-6.422163,-7.494698,-4.925807,-8.908069,-3.109043,8.214155],[-8.334433,-7.561122,-4.354924,8.885393,1.991900,-8.908217,-4.350476,5.102193,-2.085329,6.520784],[-7.604315,-2.793303,7.712655,-3.598928,-3.571659,-2.567668,-4.877784,6.065772,2.848481,1.205188]],[[2.243602,-1.906728,5.166536,5.712041,-1.214838,1.503646,-8.756733,-8.135625,-5.929020,-2.855266],[-3.480357,3.590208,5.635894,4.741393,-3.061892,9.674437,4.766048,9.539648,3.100626,-8.978109],[-5.541714,7.597870,9.143559,-9.204253,-8.639994,-8.882774,2.067941,2.546149,5.401978,1.682251],[6.258695,0.562713,-0.257458,-4.902958,-7.000777,-4.542193,-4.806424,1.997356,7.196213,9.558673],[-9.802253,-4.665890,-8.742049,-4.202602,9.166865,6.670122,-9.805499,9.157235,7.510844,7.983585],[-4.484620,-2.507655,5.405937,-7.108393,3.316819,-5.290563,-9.822011,6.225884,-7.034358,-1.970721],[8.078637,-9.762030,-9.812289,3.528723,1.125009,5.786390,-9.778894,-9.731038,-6.533230,-9.565193],[5.088904,3.356339,7.020486,-4.892294,4.353295,7.055598,-8.317155,-1.692346,6.474723,-2.616922],[-0.140368,-8.971527,-0.363455,-6.936103,-2.761494,-2.696044,4.042635,6.697612,1.566541,-5.712741],[-7.656312,2.734204,-7.659971,7.495857,6.538529,-6.484865,-4.557689,-5.843570,-6.290313,8.493261],[6.981982,-6.561196,1.147612,-4.889076,3.956743,3.454519,-5.925419,-5.296451,3.170266,2.641769],[1.446197,-6.898627,-4.519907,-1.310154,-0.062325,2.413274,-9.388034,-2.033776,4.731867,-8.630833],[-4.655629,-8.720720,-8.718059,6.840646,9.742365,3.120605,-9.874712,-2.467218,-6.206592,0.336358],[-1.876517,6.756441,-9.918798,-8.472132,-2.483282,-5.544010,5.106038,5.681365,3.139297,5.613712],[2.859003,-2.707064,-1.322553,2.708703,8.400570,3.750665,2.892815,-4.530425,7.546784,-3.407896]],[[7.021911,-6.729643,7.394037,8.690202,-9.507318,8.627447,2.808137,7.661363,-8.005844,-8.476963],[-9.471336,3.703160,-7.326808,4.319278,3.542615,1.723577,7.768139,3.698636,-4.570862,7.185214],[8.806158,-7.317946,-3.529541,-0.131180,-2.742427,8.062201,1.552448,1.256182,-8.584594,9.821575],[-4.587468,8.076115,-8.735511,-4.878069,0.562956,9.976481,4.466701,6.956795,0.426676,-7.179187],[-9.189008,-5.300267,5.338569,-1.268644,7.262946,8.416210,-9.280025,6.757608,4.913771,7.093949],[4.099627,2.201453,8.513374,4.015138,-9.043857,-2.242566,9.180932,-7.191782,-1.922149,-2.739983],[-2.023054,8.607957,-2.687905,1.323751,1.565604,-1.970142,2.808560,7.197231,-4.158282,-4.831369],[-1.035213,-6.399684,6.795253,-6.739665,0.260615,7.581548,-2.014337,-7.774887,2.419193,-6.270408],[4.339593,-5.708842,-6.962813,9.964229,-9.908602,-4.208143,-9.741008,-3.825830,0.934414,-9.658397],[6.486243,9.662500,-5.215785,2.593662,3.333721,-8.697032,-5.461327,-3.977077,-8.771946,-1.167792],[3.759026,-7.465095,3.394433,2.696516,5.179059,0.476656,-5.288138,5.789862,-9.661342,-3.460281],[-0.893359,-2.949215,5.587396,-1.097046,-3.063455,-9.153215,4.261891,-4.980788,5.660978,8.430378],[8.113400,-9.405649,9.805220,-7.631294,-4.567030,-0.765248,-5.725784,5.648427,5.559920,8.122449],[-4.709977,7.904945,-8.412983,-2.629463,2.208496,0.218211,-0.038624,-9.744805,7.103564,-9.944130],[-5.510828,-1.223193,1.477021,-5.274722,0.871428,3.632733,-0.840847,6.458819,-7.833320,-1.326501]],[[-4.251999,-2.344952,4.582476,-5.297663,5.784509,-8.692319,4.292223,-8.014265,3.707913,2.569231],[3.473035,-9.339007,3.709626,-6.389082,-4.164792,-9.367967,-7.213543,2.390460,8.034132,-3.251906],[-9.366436,-4.339704,-5.812827,9.231715,-8.538726,-0.915187,5.083155,5.950932,5.853974,-1.169541],[-7.349056,-9.322481,6.821733,3.961801,5.327875,6.001159,-2.183600,-8.540927,0.855145,-6.065940],[-4.668889,4.108254,-7.448426,5.081875,-5.233407,5.250466,-6.802653,-6.635458,5.036664,-7.348420],[0.021929,8.894665,-0.442406,-5.820336,4.611812,7.097431,-6.138698,7.664453,1.177942,-1.992684],[-6.447603,-4.551812,0.108285,-3.226889,-5.797067,3.887640,-1.429158,-8.722877,-2.106789,-9.347081],[5.027021,-0.612301,-0.130001,-6.112088,-0.848653,-4.540503,-1.894741,6.854043,4.069086,0.534265],[-9.498344,5.750594,1.021581,8.685621,7.831806,1.328974,5.434686,-0.572691,9.468148,4.928946],[3.126955,-7.092463,8.582373,0.973467,7.889603,-3.229086,3.709985,-4.546127,6.826597,5.230394],[-4.072202,-2.854466,-0.440535,9.025497,2.453045,6.979697,-7.017146,4.326775,1.262397,-8.813372],[4.887178,-5.001897,2.482121,1.070085,3.683155,3.478866,7.738268,5.550184,-3.440803,5.027883],[-7.000113,-0.478993,-5.983949,-3.930230,-7.170810,-4.503235,8.277996,-5.087246,0.980387,-0.012617],[-4.270330,-6.583547,9.109609,4.183107,3.533202,6.128643,0.784486,-0.540763,2.364492,7.723794],[-4.476610,5.099774,4.669209,-0.029200,8.331632,8.657191,-1.931145,7.764812,5.661371,8.989491]],[[7.191321,-4.842036,-8.709108,-9.477635,9.967388,6.063600,5.220853,-2.163019,-1.674698,-1.421942],[0.326792,-2.875754,9.146530,1.140448,-7.638656,7.784987,7.757221,1.687143,2.467010,-6.875421],[6.190440,-6.545090,-0.498245,0.038228,7.552208,5.344486,7.925821,-4.551196,3.365180,-7.645736],[-3.914490,-0.490798,1.186732,5.952781,0.918467,-0.689206,4.432914,-8.624686,4.117197,-4.334968],[1.568653,1.832768,3.496778,0.276141,1.877224,7.332726,-1.117450,0.516928,4.316189,-7.093746],[-4.377642,3.427380,1.235988,-4.369761,-8.163133,4.737976,-5.089674,-7.122524,-2.118867,-8.276848],[7.037139,5.929941,4.793023,-7.450111,0.598944,-2.550874,6.296743,5.001897,5.949840,4.420082],[-3.764121,9.307230,2.533635,3.571607,2.191240,1.610246,2.903150,-3.702184,9.205516,7.444084],[6.925537,8.939977,2.515228,2.326158,-4.291580,-4.802192,6.253758,5.684087,-2.665851,-7.602819],[-8.201721,-7.553542,-8.398183,8.440422,4.697799,-8.075448,-0.333652,4.018008,-5.168378,-2.609489],[8.394313,-9.498813,-8.224845,1.345832,-9.226646,-3.067536,1.821783,-1.574861,-1.402523,-3.792601],[-4.024859,-7.544871,-1.282742,-3.133398,9.055918,1.938532,-5.407515,1.437435,5.894011,2.673494],[2.398642,-5.505015,-5.738110,-9.823570,-2.367956,4.841679,-5.798013,8.598476,0.367333,1.043125],[-3.292915,-1.936517,-9.139125,6.396824,-1.032772,4.019337,8.677637,1.044962,-1.598099,-3.190944],[-8.120179,0.150534,8.048008,8.162941,1.700749,7.879289,1.919961,-5.658059,-8.594089,8.179437]],[[-2.245984,-3.225403,-9.630687,5.579210,2.474805,-8.885558,3.744025,-2.920360,-9.142955,-0.981700],[9.002797,-8.479232,4.411967,-4.590307,-4.953100,-2.359051,3.733073,-6.820740,-1.900543,-7.623424],[1.294274,2.911129,8.266539,-4.962844,2.440465,4.558626,-5.329748,6.439026,-7.198467,7.168895],[8.249640,4.616379,-6.202343,5.197769,3.178199,4.505381,-1.237217,-1.115742,-2.594152,6.821302],[9.729316,-5.476826,-3.201266,1.984647,-0.515533,-1.654052,-8.183513,-1.983169,5.904636,-3.497746],[2.783745,-0.671425,-6.198689,6.574234,4.740737,4.821867,3.599166,-3.260218,7.371299,-3.608470],[7.120614,-0.391076,-6.156410,-7.356545,-2.120004,6.172987,-0.676694,8.361172,-8.944776,-9.689914],[9.106884,-3.999061,1.762799,7.757414,-9.455161,-7.530325,-1.332584,0.169690,1.699854,-4.962962],[-6.292677,-9.340736,1.750334,-7.882143,-7.416988,3.806788,-7.185082,2.090640,3.778126,-8.564169],[-2.562560,8.570478,7.789248,-9.074253,-9.062926,-0.036127,-9.447927,-1.161534,-6.778524,8.885994],[9.411442,4.890470,-2.515279,8.831309,0.978788,8.516324,5.401579,-2.982951,2.675066,1.525261],[7.108416,2.638670,-6.642938,-2.954278,-0.187368,-6.527127,-6.838472,8.367467,-5.310978,-8.073396],[-4.523073,5.113955,-6.417654,7.373253,-6.233233,-1.161433,-3.630572,0.191675,1.608235,-5.098101],[8.465273,1.099460,-6.693134,-8.101657,3.923738,-1.515888,-4.339369,4.169917,7.209050,5.423765],[-9.443560,8.049809,0.497717,7.319509,-5.011375,-0.993028,-6.865228,-3.584108,-6.850242,9.906310]],[[9.223322,7.131305,-2.694132,6.285667,6.453841,7.952450,-4.730646,3.524691,-2.896325,-6.047122],[-8.110187,-9.121415,-6.669265,5.333608,-6.840975,-2.407569,-5.203203,9.979763,5.529667,-8.229725],[1.490404,-0.479530,-6.114568,7.049776,-2.874109,-7.448139,-4.289763,-9.385654,8.445036,6.555924],[-6.514563,8.558507,-0.655726,8.153488,4.889510,-1.410778,-1.278882,-1.681159,-5.088520,8.632471],[7.958523,7.183471,-2.980199,-4.256170,4.132158,1.381068,-1.956493,-1.240836,-0.998684,-6.337143],[8.456517,-1.059603,9.630140,1.049298,2.693629,-1.409249,-0.424854,-4.231955,9.962266,-2.428143],[3.158877,0.044287,-4.308858,-5.518792,8.205175,3.880036,7.453025,-2.010662,-3.912465,8.179495],[-5.750613,0.096315,7.213292,-3.863527,-2.302899,-5.078812,-5.741926,6.089431,1.431132,6.428401],[-1.726847,-2.604454,8.333319,-8.529495,-9.808113,1.516416,-0.496979,7.854131,-3.092444,-4.878038],[-2.737618,-5.786697,-7.803627,7.580802,3.704780,6.559956,8.078124,-7.630417,-8.659743,2.762718],[-3.414664,-7.620784,6.501566,-8.493701,0.118143,-1.713131,1.711663,-1.097561,3.923095,-8.082538],[5.330122,-2.184908,4.597981,9.430849,-5.890662,-6.588350,4.251135,8.763005,-4.130660,-7.966923],[-7.440655,2.592767,-4.420528,-0.549553,0.683260,-7.979375,-5.620087,-3.086398,8.964294,4.811290],[-5.549059,-1.063795,-5.772293,-5.121441,-3.942233,-6.425697,5.628625,-4.814818,-4.256883,1.948700],[6.645295,-0.165159,6.528689,7.767862,-7.592599,-9.935501,-3.444174,-2.954646,-2.142119,4.780096]],[[6.973613,3.673247,2.244802,-8.009301,-3.401324,-6.128303,-4.621083,0.260036,3.094222,-3.031918],[-1.525982,-3.465866,-8.998724,4.584898,5.865589,4.922622,7.464256,3.282821,-2.271591,-7.918454],[-7.682737,4.891141,9.387799,-7.314635,3.164828,-6.438109,3.472653,3.314885,0.400831,-5.626168],[1.700403,4.601360,-9.158129,-1.264501,2.247540,-1.207495,4.570399,-4.642257,-7.816951,1.730942],[7.236281,6.186846,-9.832560,-8.236983,-9.290100,-2.131075,-6.300344,-1.700163,-2.112754,-0.142576],[5.959278,2.929999,-9.456485,9.132916,-0.219009,-3.806807,-3.864797,-2.148047,-0.537165,-7.583481],[6.270653,5.208372,-2.722504,3.067935,-9.176292,-9.903613,-1.690221,-9.785214,1.704906,3.571710],[-2.289226,-7.254161,-4.039364,8.166814,2.707193,7.274464,-1.223698,3.514383,-2.728079,5.449354],[-7.070530,-6.426825,-9.189874,1.168847,-6.072722,5.398517,-7.387763,1.222450,8.577960,-8.913350],[-0.862367,8.667526,-9.233899,8.406478,0.806250,1.229157,9.033694,-5.330156,-1.418263,4.531395],[7.103989,9.176214,-5.008794,-6.711112,8.067768,1.507964,-8.186229,-3.839735,8.566175,6.127543],[-6.943150,-7.503539,-2.290239,3.133118,-6.264345,8.750698,-5.515239,4.369042,9.789072,-6.456201],[-1.331752,-7.476287,-6.159909,6.383904,-4.163104,1.140390,4.211953,-5.302495,-3.622980,-3.511067],[1.980639,-6.260236,-1.994484,-0.314821,4.768908,-4.735164,-5.337179,-9.831685,5.061844,-9.714212],[-1.400179,5.595872,9.087454,1.870582,7.234646,-9.802713,9.916586,-4.189309,0.155265,0.619835]],[[4.769978,-4.336342,-5.313676,0.044432,4.290538,-8.603383,6.077148,5.314340,6.388015,-6.995569],[3.043319,8.004855,-1.039762,-7.499240,0.188724,-0.868133,-1.942944,-3.576478,-0.497745,-1.256539],[-2.697170,6.189417,-3.145232,-1.265403,-8.875901,9.543407,-0.561301,-1.849494,-6.847245,-3.064749],[6.244011,9.567937,2.508955,-6.662887,3.182606,1.932520,9.725709,7.622909,-4.817923,-6.460023],[-0.545444,-6.010675,-9.400901,8.161703,4.995158,-9.035703,1.775145,-6.041173,-5.088184,-6.319824],[-6.951906,1.228520,-6.789561,3.912811,-3.618618,5.483517,6.168444,3.224469,5.955275,9.168954],[-5.996920,2.126497,2.353671,9.885195,-1.668094,5.801653,5.161940,8.362321,2.857438,-3.309358],[-5.383419,-7.649749,4.536940,5.876284,5.193531,-8.002858,8.762412,4.914109,0.607996,-1.383946],[-5.051272,-5.677377,-2.351143,8.291214,2.496160,2.236156,-8.989533,0.305261,-0.635961,-3.605139],[5.868759,9.903559,-0.937320,9.906334,3.204543,2.283192,6.003982,-3.735622,0.304241,6.191824],[2.786868,-9.418664,7.918005,-7.473929,4.050461,8.051178,3.691662,6.449914,4.873856,2.174087],[-0.182786,-5.803244,3.725480,4.985738,-8.762978,5.534379,4.274367,6.577003,0.106248,-6.311137],[-8.513364,-8.177841,5.204565,2.569538,-8.979312,6.785674,-5.787105,2.843103,-1.354746,-5.410749],[0.966311,2.019116,-1.142428,4.011208,-0.133895,-5.742347,1.076752,-5.014630,-0.043471,2.313809],[-0.758966,0.557142,-4.996249,-4.957622,5.285435,-6.829075,-3.812876,9.205967,-5.856488,5.961230]],[[9.192891,-6.517689,-3.723292,5.005266,-2.288551,0.663639,2.852698,5.098725,8.107950,8.347394],[9.879351,-4.918880,9.343863,-1.375128,-6.673356,-7.627534,9.183696,6.316655,1.738454,-4.411376],[8.381951,-5.476186,-0.642234,2.341489,-9.799979,-5.993854,-9.188273,7.659895,-8.319816,3.328178],[7.309213,-4.882135,-2.123986,-3.649216,-4.916886,-6.531290,7.970584,5.998359,-4.927758,0.796779],[5.033144,-3.165834,-8.859096,0.217905,4.748559,-1.685169,-3.365297,7.974144,-3.447284,-3.787064],[-4.547026,-4.065991,2.455568,7.276809,-9.512349,-5.320963,-3.112851,1.175503,7.020589,-3.900766],[-5.481966,2.205403,3.278572,9.930389,4.665866,9.467236,-0.079750,3.898271,9.172511,-4.340391],[2.871755,9.053610,5.400388,4.184347,7.184883,-1.932480,-5.482073,-0.070435,-2.357409,4.984041],[2.317614,-3.350381,-8.895909,4.565406,-3.070451,-2.607165,8.585438,-0.382647,-1.258729,2.157178],[5.815933,4.798411,4.876614,8.242095,-5.693037,9.701579,7.885658,4.982935,2.938020,6.721648],[-1.175868,-9.835435,4.517661,3.111011,-4.105180,5.730049,-6.164183,0.125457,-1.998552,0.941747],[4.387692,-8.874392,-4.587153,-5.075870,2.230658,-6.951792,4.991372,2.366630,1.187386,2.991022],[7.327686,7.243439,1.883301,4.086494,0.397384,-4.333699,-6.584577,-1.110765,0.021869,-9.128389],[-2.602040,-1.734029,7.533987,0.856795,-0.295486,-6.891269,6.018408,8.205665,-1.701878,8.341155],[-9.934790,-6.470108,-0.564646,3.885342,-6.028780,-6.123495,-9.137246,-1.554053,-7.428670,-7.051916]],[[-7.230088,-1.766940,-8.280593,6.298856,6.959691,0.869966,-7.710268,-3.086209,-5.051495,-4.992204],[3.545284,2.514810,-6.666553,-0.938345,7.886748,2.146457,0.839531,-2.308659,-4.959889,0.476091],[-0.570224,0.898833,-6.007548,7.109878,5.512415,7.659276,1.771998,2.053856,3.099891,-2.019374],[-1.268151,-7.017256,-7.875748,-1.556414,-0.231344,-6.712246,-1.244999,-8.038129,7.663408,4.591577],[8.785077,9.905540,8.418164,-2.005648,-6.968933,-6.198419,9.534152,4.014525,9.024709,-1.785576],[7.881092,-0.615308,-9.117545,-3.216872,-3.521723,-6.219030,5.464891,-5.616582,-3.146709,8.971063],[-7.582959,-4.075621,-3.907504,8.389233,5.816073,-3.540694,-3.778984,-1.359256,4.340720,-3.738184],[-9.833741,8.742187,-3.859240,-0.655490,5.971448,-9.520798,4.081363,0.669714,-3.432496,5.217358],[-3.360017,-4.696317,-0.181041,1.565174,2.969137,-4.231135,-5.995336,8.594221,1.869820,-0.381951],[6.477228,-5.708927,0.620344,1.535466,-3.128062,8.782822,-9.410666,2.203832,-9.269815,-7.784402],[-2.804180,4.136141,-9.651637,-4.270407,-1.671787,-6.128228,7.290624,7.682474,-2.506585,-8.546714],[9.045448,3.052128,7.861388,6.331309,3.396065,4.588938,-7.482958,6.961639,-1.128698,-2.500337],[-3.334529,-1.552591,-2.486923,-7.361928,-3.296392,2.280077,-1.633949,0.813361,-2.671926,7.162840],[-3.628835,9.034599,5.862802,-6.649210,-9.228918,-3.614001,9.397432,-6.953646,-2.944106,9.147713],[7.652445,6.425602,2.611414,3.714487,3.762328,-6.639608,-7.841576,-3.555446,-3.886703,4.234963]],[[3.235786,9.583091,-9.019132,-5.209572,-2.144287,-2.847739,9.156567,1.773366,-1.434140,-3.524168],[1.007537,-6.510422,-3.151108,0.926211,8.496456,-7.374704,-8.241158,2.253390,8.555281,-3.909019],[4.104301,-8.355878,-3.725538,-7.766707,-6.000625,-1.162618,9.289077,8.883311,7.301526,-3.600427],[8.030415,9.112442,-5.138773,1.896393,5.962505,2.615487,-7.521835,2.986935,1.387434,2.296462],[-7.669362,4.552237,-6.946673,9.060796,6.853885,-9.696477,-2.457175,-8.695012,7.815650,8.747081],[4.268717,1.798118,-1.182400,-4.146852,-3.725696,1.405558,7.848408,-8.871758,-2.674894,1.630688],[4.145108,-2.430841,-9.657129,-1.695651,-7.586959,-0.588607,-6.124368,8.592053,-0.329286,-2.154204],[-7.510996,8.403048,-5.822065,5.336555,9.879381,-5.506003,4.544550,9.137339,-8.855447,0.058705],[5.855293,-4.136172,5.590707,-5.712685,-7.072827,7.140223,-2.006391,-2.917595,-6.999303,1.172245],[4.453110,2.549680,8.401650,-9.813980,-5.820197,-3.757508,0.853562,-1.235428,3.237990,-2.672273],[0.367201,-8.662282,-0.826607,7.253618,-7.069972,-3.841305,-0.060627,-7.036314,-1.828676,9.294376],[-4.077040,-6.252514,7.441178,7.325199,6.714413,-9.760671,3.480031,2.228595,2.711734,-2.132244],[2.005432,0.380350,-0.474817,6.672941,-0.371098,-1.676498,0.689247,-1.355268,1.847823,2.929971],[8.766201,7.079293,-4.026100,-4.345801,3.063812,1.394244,-8.769846,2.924729,3.906277,4.961403],[0.645276,-6.765543,5.636392,5.478197,-7.099689,2.478090,-5.621627,-2.768330,2.066937,0.868665]],[[-2.164836,-4.284297,4.706805,1.131885,-6.648721,9.472754,-5.567725,-1.487236,-4.798314,-2.497867],[-3.264376,9.503752,5.581005,9.581881,-9.602444,0.968753,-8.482793,7.186020,6.280987,-2.159892],[-3.737840,-9.618091,9.815901,-0.082186,-2.544143,2.486020,-8.637645,-6.094151,-0.274164,3.345751],[-6.183019,3.192766,-8.125981,-2.850090,-6.401640,4.722942,-0.091559,0.992616,8.189193,-1.245722],[6.009156,-1.469078,-5.340289,1.822599,4.351178,5.814530,8.866105,-7.202184,-4.883584,-8.864306],[2.779242,5.730607,8.601074,9.090380,-1.864174,-0.255041,5.786597,9.244049,7.782908,5.382300],[1.155754,-8.725739,4.185504,-6.410995,-7.261453,-4.551046,3.626401,7.531957,9.118904,9.135397],[-0.098856,8.239824,-3.914671,2.492569,9.220845,-4.923314,-9.681615,1.679771,7.137755,9.827319],[-0.713602,8.431521,3.365486,-5.320266,-1.697419,-2.480560,-4.907017,-8.998419,-2.910608,-2.423662],[-9.508246,9.974411,-8.207892,6.250525,-9.867949,6.985648,-0.548665,-8.448153,9.991186,-6.455381],[-0.338399,4.420278,-2.200473,-1.777664,0.481725,-0.512178,8.238131,-4.265169,3.261262,-9.330365],[-5.786422,-1.876081,-4.183208,-5.473793,-8.441494,6.763058,0.292416,6.013503,4.123189,2.435399],[-4.501949,-6.581008,5.044912,7.519036,-5.362477,-6.748037,1.769028,-0.584438,-7.066118,-8.955604],[7.759382,0.081079,-7.174073,5.023435,-6.493660,-9.747586,-7.323601,6.587322,-6.508942,-4.230476],[-9.550332,4.602821,-9.014125,3.839937,9.805825,8.629632,-2.235253,3.453120,2.681194,-9.626610]],[[6.896714,-4.603198,3.131123,2.834167,8.623344,7.522564,4.756270,1.977114,-2.130008,-6.645490],[-2.071324,-9.053196,-7.724546,8.760623,-5.075155,-4.810590,7.618244,-6.479803,-1.496479,-1.367564],[1.414030,2.836380,-7.497455,-9.650279,9.760007,-6.891959,-4.804744,-8.917797,7.976690,-5.795258],[3.701141,0.505635,-8.436158,-6.162112,-5.310745,-3.830342,-6.599243,-2.039008,-8.653668,2.509396],[4.475491,-4.858156,-4.962776,-8.154003,-9.987232,-6.441701,4.096127,-4.341714,4.509795,-0.933877],[0.603300,6.727936,-4.049843,3.935709,3.447838,1.541897,-3.344957,-0.292731,-5.112996,-6.494331],[-6.760451,1.727056,5.328987,5.596368,-1.038144,-4.225485,-0.747342,6.245163,5.994660,4.895879],[1.151939,6.291621,-8.278780,-6.225122,-7.466271,-4.524613,1.068515,8.020771,3.903280,8.814249],[-5.961521,-1.654795,-7.427132,-0.398431,-2.578802,-9.916859,-8.187003,6.396279,2.441992,5.233301],[1.703230,-6.630658,0.549180,8.589840,-3.432272,-3.428361,-5.377444,3.656712,-3.359624,-6.411574],[-8.246419,-6.931438,-5.731716,7.599122,-9.315967,6.025164,-6.369922,-9.071245,0.705457,5.190481],[1.760856,2.801951,-7.207586,-2.192805,-5.059505,5.272661,6.274296,5.171232,2.177629,0.608623],[8.305731,0.828935,8.742996,-2.208415,0.043195,-5.671626,0.313388,-0.471465,5.952157,4.138210],[9.646256,-4.937647,-5.992221,-5.187275,-3.847959,8.889095,7.957827,-7.447602,0.277139,9.711225],[-8.680878,2.344422,3.883315,6.401533,-6.130545,-7.583430,7.397818,-8.573231,-2.206563,5.008678]]], dtype = "float32")#candidate|4618|(16, 15, 10)|const|float32
uop_4619 = relay.acos(const_4618.astype('float32')) # shape=(16, 15, 10)
output = relay.Tuple([uop_4619,])
output2 = relay.Tuple([uop_4619,])
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
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_4646 = relay.TupleGetItem(func_501_call(), 0)
call_4647 = relay.TupleGetItem(func_503_call(), 0)
func_247_call = mod.get_global_var('func_247')
func_248_call = mutated_mod.get_global_var('func_248')
call_4648 = relay.TupleGetItem(func_247_call(), 2)
call_4649 = relay.TupleGetItem(func_248_call(), 2)
const_4652 = relay.const([[[2.514139,4.132219,4.559681,2.050321,-1.348892,-2.284374,8.072745,-8.591713],[1.768903,-9.447668,-4.663816,-7.004517,-0.291284,9.365003,-8.633771,-5.698879],[-4.121105,-0.838196,1.129132,-4.322702,-9.852407,-1.098401,-3.382610,8.698217],[-2.968577,-7.357395,-5.895280,-3.466850,-6.009309,7.050158,-3.992792,-8.852814],[9.484338,1.825635,-8.525745,-9.811893,-6.270567,1.011883,1.106982,-2.641281],[-4.102020,-5.250247,9.633142,8.218554,0.675250,-0.666989,0.491434,-2.072103],[0.693259,9.039674,-5.307039,4.354856,-3.061574,1.206096,0.541733,-4.309116],[4.309981,-7.405732,1.378755,-4.521765,-9.322939,8.157151,6.036939,-1.497598],[4.342622,-8.883754,8.505620,-4.889616,-3.304010,3.863991,4.429741,-0.184042]],[[-1.574789,3.090856,-3.906421,-9.582614,-6.122910,-1.075211,-0.414084,6.648478],[4.343440,2.457031,7.555247,-3.745973,1.343907,1.409156,0.256597,8.070496],[-4.019540,-9.912700,-1.877709,5.602910,-3.987399,-6.052514,-2.687802,-0.568496],[-2.866681,-5.347271,7.715756,4.245328,-6.092243,5.772580,-5.091493,8.493798],[4.877895,-8.166716,1.346093,-3.819581,0.511143,-0.076611,-2.917935,7.287357],[-7.641218,-9.471699,7.800043,-2.313605,-6.104076,1.180192,0.153170,8.876057],[-2.121522,-0.265622,9.551520,0.429226,-6.621118,-8.561211,-1.154015,7.130469],[5.246572,-5.994328,3.397077,-8.801670,-8.348941,4.627785,3.317218,-0.843498],[-4.475838,4.076110,-7.519551,-7.640567,-7.153844,8.523541,1.021439,3.779470]],[[7.286355,3.687818,-4.459206,-8.143015,0.927806,-4.057955,2.262651,6.399838],[-8.217557,9.052198,5.627959,7.775674,4.336154,5.595705,3.678137,3.281214],[-8.282159,8.853067,0.780239,-8.668608,9.856837,0.526486,6.784851,-3.735835],[2.558670,-3.720818,-7.590177,-5.964098,3.317542,-7.224234,-9.160784,4.173952],[-7.716049,2.023573,-9.459512,-9.802307,4.631208,-1.132802,-4.513243,-3.092630],[9.413370,7.356908,-4.463569,4.654607,9.615474,-4.904864,1.271213,-9.851756],[-4.603859,1.927244,2.087132,5.952713,1.137433,-9.309762,-1.992635,2.632815],[7.040869,4.267949,-2.236624,5.916480,-7.977929,4.036690,8.702268,5.578486],[-2.759249,9.343292,7.952689,-5.162392,-3.949201,-5.635393,4.202391,-4.501376]],[[-2.542680,-2.446157,-7.811229,-6.292655,6.591017,0.612517,-1.305010,-8.124929],[5.433168,-5.481940,-8.254160,-8.513042,5.206230,-9.372580,-8.863394,-2.740012],[-7.752982,-2.137269,-5.348014,-9.025456,-5.806766,5.398719,-0.003699,8.175800],[0.226356,-2.322997,-8.020725,-9.515763,-8.900389,-5.609230,-0.845481,7.553221],[5.025145,0.925103,2.713601,4.541896,3.590122,-3.809536,4.294464,-6.247147],[4.923801,-7.050151,7.065764,-7.973469,0.961309,-5.835791,3.749462,2.994435],[3.741419,-7.004007,-8.969919,8.529063,-0.097069,7.045000,9.275976,-2.901250],[6.291780,0.564441,-4.302856,-5.260916,-2.408179,0.659825,-0.979526,9.025751],[1.265891,-3.873637,5.152400,-0.040758,8.822007,9.523729,8.391578,-3.276660]],[[1.724876,1.393862,1.110580,2.845164,-6.324262,0.128707,1.711300,6.510764],[-5.836261,-2.996573,5.003634,-7.559584,6.071982,6.949361,5.298533,4.208325],[3.409336,-5.694488,-4.045425,2.635439,-5.125967,3.795088,3.173608,5.206250],[2.297069,3.084039,-7.625482,1.015145,-2.492577,-3.138667,-7.119549,-5.052798],[-7.995678,-7.278001,-3.781357,4.597374,-2.489048,4.617286,3.166282,-0.385597],[-2.558244,4.505927,5.854414,-2.742690,-0.845881,0.815169,-4.816810,-7.061039],[1.050274,3.941868,-6.036480,-4.782346,-6.209480,-0.484581,-3.081593,-6.683483],[8.793910,5.178055,-0.288806,-5.788901,-7.208548,-2.783170,5.447277,3.363744],[3.136848,-7.052091,-4.501263,1.724286,-2.171472,-4.304179,-6.802346,-8.983624]],[[0.115444,-5.360012,1.398094,-4.294891,-8.230309,5.452266,2.778161,-5.428939],[1.031279,6.251853,-1.127546,-4.857890,-2.237247,1.567045,7.244409,-1.240731],[-6.595976,8.094318,9.363289,0.792991,-2.281141,8.111938,-5.858693,-3.164610],[9.875879,7.581927,-0.265611,-6.776346,-3.096537,0.130866,4.173374,-4.820983],[-8.001935,-0.489338,6.741745,-8.169078,-3.826766,-6.203870,4.182210,-2.789302],[-5.346183,-2.495181,-2.514385,1.456467,4.908322,-3.289330,0.292705,-3.089317],[-6.417013,0.312940,-9.709935,4.744209,-0.748050,8.792307,5.756441,-7.506155],[5.473505,-7.817578,8.011852,6.621353,9.353926,-1.478728,-3.009468,-7.592258],[8.061615,9.676831,3.864210,-4.859048,-9.067593,-3.323549,5.121405,1.311586]],[[8.455587,-2.385028,8.529769,0.666199,-7.869687,3.038407,-1.309853,3.454835],[-3.963806,-5.884031,-3.927194,9.279381,-1.270038,-6.286772,-1.129653,8.672855],[1.384742,-2.157501,4.400404,2.352992,3.100406,-6.046758,4.291346,0.459877],[-1.470896,1.082160,-7.474021,3.268041,-2.934234,4.466329,4.845675,6.059069],[-8.909754,-4.955009,5.916672,0.515072,-9.619987,5.246707,-8.065176,8.884493],[-8.249889,4.470920,5.826150,5.367707,-1.648205,-3.291589,8.168413,-7.723394],[-3.178660,1.305113,7.100747,-6.233644,8.694793,0.891412,4.226865,-4.489127],[8.170356,-0.197531,5.713566,2.243106,-1.731662,5.740565,7.408182,-9.778121],[-1.810673,7.862850,-0.981365,-5.692033,9.526971,8.429515,-1.899468,-9.094253]],[[8.486619,0.014237,3.249536,-9.020075,-6.278427,8.055559,-9.696910,7.044412],[-5.378697,-9.669127,3.349487,-9.287246,-8.009539,9.358308,6.408570,-0.485207],[-7.052720,5.044212,-0.470387,-2.704078,-5.814055,-2.862761,0.602631,7.107153],[4.347233,-9.395067,-5.531989,0.621513,4.546585,-3.182305,4.328998,1.845084],[-2.123022,6.313874,8.001269,8.932769,7.664172,-4.489484,-0.910727,-1.012420],[6.978127,-2.109469,2.268933,-5.389489,-7.149637,-5.225195,7.860171,7.268639],[-6.881337,4.895577,-8.622754,1.994146,-4.916670,-4.612047,-8.495328,-8.878200],[-7.662286,1.842115,9.098721,-6.663509,-8.649868,2.598621,-2.795323,6.719345],[8.547612,-6.735482,-5.798435,0.117777,4.977681,0.845880,4.346516,9.388229]],[[-1.071510,0.091791,-1.514524,8.282484,-4.778074,5.513890,2.575418,-4.145953],[9.798788,7.541922,-4.016468,-2.638457,-9.994495,9.077009,-0.999961,7.654597],[-0.811882,-2.528607,-4.659338,5.861945,-6.449115,-3.692670,-9.039448,-7.248640],[6.076451,2.276444,-6.661571,-5.446841,7.508364,-0.057209,-6.365561,-2.081399],[4.338330,-9.391125,-3.184689,-1.490066,-1.909201,-5.475290,5.689832,-2.352843],[-1.450626,8.203368,9.922915,-8.077292,9.654832,-6.130173,-8.566262,-8.898160],[3.025475,-1.062510,7.845890,-3.408308,7.863008,-0.281919,3.398610,8.901150],[-2.767459,7.506029,-2.063753,-2.431675,-3.167106,-4.677615,9.205994,-9.518289],[4.820888,-8.828828,-9.736044,-3.665117,4.122814,-7.264484,3.920997,8.283320]],[[-5.371837,6.598552,-4.409866,7.512363,9.839242,1.734605,-9.489348,8.298383],[-0.833972,-3.999592,5.803009,-6.310971,9.438596,2.260340,8.584357,-5.464074],[0.699857,-6.224154,1.168816,5.479233,6.462132,3.892274,-4.833372,4.888979],[-2.521210,8.915772,-7.940834,4.903450,2.383502,-6.257751,8.803283,-7.740990],[8.388614,-5.834956,-0.200924,4.240698,-4.784298,-2.542041,7.923740,-4.858491],[1.358827,8.267785,2.050905,-0.427087,-8.278735,7.050236,4.442041,-8.093853],[7.868399,-3.868686,-9.148738,7.906853,-0.711121,-9.122062,-4.590917,-8.100101],[-0.554751,5.782657,-1.481122,-5.241302,4.323330,-7.957559,-9.663358,3.426539],[0.999713,8.622930,6.583309,-3.917970,-0.025551,1.752645,0.404482,0.936947]],[[-1.372494,-3.040712,-1.788821,8.283908,-1.091905,-0.971206,-6.374012,-5.049378],[9.252218,-9.835177,9.074907,3.683249,4.614408,-0.065261,-1.011248,-8.999876],[-7.279372,7.990555,-1.577169,-9.207230,-9.066091,6.844034,-3.335726,-4.605447],[5.485970,-3.838022,2.515687,3.754233,7.232353,-6.120941,8.986221,-6.147082],[3.777302,-3.435498,-4.752584,-5.630184,5.783136,0.276425,-1.892417,-6.448123],[-2.986839,-1.969300,-1.189009,-4.467834,7.647225,0.267189,-2.173203,-3.643712],[1.718947,8.815540,-4.804856,-9.918124,0.357800,0.017541,8.235430,6.565548],[0.985840,2.672069,3.579836,4.564921,-7.890142,7.351294,-8.599743,-0.199216],[-0.147765,8.234021,-1.599158,3.632611,4.365980,7.828274,-6.711851,2.402071]],[[-7.969928,5.993899,-1.084973,-0.884076,1.748894,7.817490,4.434795,1.683315],[3.081350,-6.148107,-9.789536,6.092591,1.083723,-6.752906,-7.413869,4.335346],[-4.308939,-9.173760,9.305045,-5.814205,5.386164,-7.536883,2.222448,-1.421567],[-1.598395,-4.829071,-2.298101,-7.733124,-8.323645,8.040919,-6.084461,7.798009],[1.057528,-1.136010,-5.177319,5.611235,-1.558597,5.758363,9.683130,8.681805],[-7.555994,-8.567678,1.329426,-9.937931,4.633304,-2.933227,-5.359152,1.261210],[-1.643562,-4.947649,-0.081219,-2.250902,5.276051,-1.808714,0.225554,-6.077749],[-4.390139,7.655231,-3.729342,6.321092,4.024510,3.120066,-0.914882,-1.200971],[-4.805633,7.495618,-0.888585,-6.888654,4.382902,5.007183,-2.913852,3.925404]],[[-3.734726,-4.085345,-5.927766,1.891428,-6.369593,-2.942690,2.388012,2.840820],[0.601410,-0.819704,-6.914531,-6.923338,1.515373,-7.418906,4.707154,-7.992810],[-5.560873,-2.764090,7.293542,5.780782,0.610846,-6.281473,-2.657753,-5.468239],[-1.914146,8.797195,8.077017,9.465020,6.754119,-8.798692,5.815360,4.795783],[-8.577011,-4.231924,2.562710,8.377857,8.602483,4.793478,4.102079,-2.859753],[-2.422808,-7.094844,1.904418,-5.915662,3.577129,8.374541,-4.228119,3.107655],[7.595791,-6.041697,6.709800,8.971513,2.560215,-8.358395,-7.674042,-4.978150],[-4.670361,3.008659,-4.014333,5.602009,-8.974387,-6.848780,8.511542,4.120021],[-2.206606,4.620782,6.186735,-7.411461,9.617358,7.593554,4.433527,-1.055018]]], dtype = "float32")#candidate|4652|(13, 9, 8)|const|float32
bop_4653 = relay.multiply(call_4646.astype('int8'), const_4652.astype('int8')) # shape=(13, 9, 8)
bop_4656 = relay.multiply(call_4647.astype('int8'), const_4652.astype('int8')) # shape=(13, 9, 8)
output = relay.Tuple([call_4648,bop_4653,])
output2 = relay.Tuple([call_4649,bop_4656,])
func_4678 = relay.Function([], output)
mod['func_4678'] = func_4678
mod = relay.transform.InferType()(mod)
mutated_mod['func_4678'] = func_4678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4678_call = mutated_mod.get_global_var('func_4678')
call_4679 = func_4678_call()
output = call_4679
func_4680 = relay.Function([], output)
mutated_mod['func_4680'] = func_4680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1073_call = mod.get_global_var('func_1073')
func_1074_call = mutated_mod.get_global_var('func_1074')
call_4691 = func_1073_call()
call_4692 = func_1073_call()
func_3375_call = mod.get_global_var('func_3375')
func_3376_call = mutated_mod.get_global_var('func_3376')
call_4696 = relay.TupleGetItem(func_3375_call(), 0)
call_4697 = relay.TupleGetItem(func_3376_call(), 0)
output = relay.Tuple([call_4691,call_4696,])
output2 = relay.Tuple([call_4692,call_4697,])
func_4700 = relay.Function([], output)
mod['func_4700'] = func_4700
mod = relay.transform.InferType()(mod)
output = func_4700()
func_4701 = relay.Function([], output)
mutated_mod['func_4701'] = func_4701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_4807 = relay.TupleGetItem(func_1526_call(), 3)
call_4808 = relay.TupleGetItem(func_1527_call(), 3)
output = relay.Tuple([call_4807,])
output2 = relay.Tuple([call_4808,])
func_4818 = relay.Function([], output)
mod['func_4818'] = func_4818
mod = relay.transform.InferType()(mod)
mutated_mod['func_4818'] = func_4818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4818_call = mutated_mod.get_global_var('func_4818')
call_4819 = func_4818_call()
output = call_4819
func_4820 = relay.Function([], output)
mutated_mod['func_4820'] = func_4820
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4856 = relay.var("var_4856", dtype = "float64", shape = (3, 3, 4))#candidate|4856|(3, 3, 4)|var|float64
var_4857 = relay.var("var_4857", dtype = "float64", shape = (3, 3, 4))#candidate|4857|(3, 3, 4)|var|float64
bop_4858 = relay.divide(var_4856.astype('float64'), relay.reshape(var_4857.astype('float64'), relay.shape_of(var_4856))) # shape=(3, 3, 4)
output = bop_4858
output2 = bop_4858
func_4863 = relay.Function([var_4856,var_4857,], output)
mod['func_4863'] = func_4863
mod = relay.transform.InferType()(mod)
mutated_mod['func_4863'] = func_4863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4863_call = mutated_mod.get_global_var('func_4863')
var_4865 = relay.var("var_4865", dtype = "float64", shape = (3, 3, 4))#candidate|4865|(3, 3, 4)|var|float64
var_4866 = relay.var("var_4866", dtype = "float64", shape = (3, 3, 4))#candidate|4866|(3, 3, 4)|var|float64
call_4864 = func_4863_call(var_4865,var_4866,)
output = call_4864
func_4867 = relay.Function([var_4865,var_4866,], output)
mutated_mod['func_4867'] = func_4867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1614_call = mod.get_global_var('func_1614')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_4871 = func_1614_call()
call_4872 = func_1614_call()
output = relay.Tuple([call_4871,])
output2 = relay.Tuple([call_4872,])
func_4883 = relay.Function([], output)
mod['func_4883'] = func_4883
mod = relay.transform.InferType()(mod)
mutated_mod['func_4883'] = func_4883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4883_call = mutated_mod.get_global_var('func_4883')
call_4884 = func_4883_call()
output = call_4884
func_4885 = relay.Function([], output)
mutated_mod['func_4885'] = func_4885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_4896 = func_122_call()
call_4897 = func_122_call()
var_4905 = relay.var("var_4905", dtype = "float32", shape = (13, 9, 6))#candidate|4905|(13, 9, 6)|var|float32
bop_4906 = relay.logical_and(call_4896.astype('bool'), var_4905.astype('bool')) # shape=(13, 9, 6)
bop_4909 = relay.logical_and(call_4897.astype('bool'), var_4905.astype('bool')) # shape=(13, 9, 6)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_4912 = relay.TupleGetItem(func_937_call(), 4)
call_4913 = relay.TupleGetItem(func_939_call(), 4)
output = relay.Tuple([bop_4906,call_4912,])
output2 = relay.Tuple([bop_4909,call_4913,])
func_4936 = relay.Function([var_4905,], output)
mod['func_4936'] = func_4936
mod = relay.transform.InferType()(mod)
var_4937 = relay.var("var_4937", dtype = "float32", shape = (13, 9, 6))#candidate|4937|(13, 9, 6)|var|float32
output = func_4936(var_4937)
func_4938 = relay.Function([var_4937], output)
mutated_mod['func_4938'] = func_4938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4629_call = mod.get_global_var('func_4629')
func_4631_call = mutated_mod.get_global_var('func_4631')
call_4959 = relay.TupleGetItem(func_4629_call(), 0)
call_4960 = relay.TupleGetItem(func_4631_call(), 0)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_4978 = func_3036_call()
call_4979 = func_3036_call()
func_664_call = mod.get_global_var('func_664')
func_667_call = mutated_mod.get_global_var('func_667')
const_4987 = relay.const([[4.115064,6.130457,8.426816,-0.020947,-6.188453,-8.133744,-5.765365,4.108398,9.958861,-5.335945,-1.961837,9.460543,-3.289978,0.060622,-5.400000,5.285799,-1.179919,-7.349792,-9.120677,-4.409661,0.262330,-2.997079,0.815881,2.345252,9.592248,-7.585255,7.387521,-4.119438,-7.672686,-9.488146,-5.577139,-1.819125,9.771520,-5.945117,6.429714,-4.502601,7.511517,-0.040360,5.740844,1.197337,2.568283,-8.949600,-4.614853,-4.160620,3.798319,6.743692,-7.892926,-7.281623,-4.078158,1.220959,7.147908,9.553546,-1.735140,-5.150460,0.857124,-4.383752,3.471960,3.502312,0.239640,-6.367656,-9.239000,-4.685782,9.875854,-2.614017,0.813154,8.997356,-8.562395,1.237981,-9.863431,-3.299178,-4.147428,-4.902627,9.830436,7.009760,3.380825,6.805120,0.209792,2.930668,9.703922,4.478490,3.159804,9.393882,1.806801,7.694468,-3.678769,6.013812,-8.476376,-5.435002,9.266569,2.182870,6.235072,-0.813394,-4.657226,8.975286,-8.092509,1.891961,8.737638,3.859247,1.346628,-8.793448,-4.354302,-1.291805,1.906611,-7.928044,-3.072552,-4.436372,2.878238,8.658300,-3.767780,0.565801,2.467778,-8.352785,1.956217,5.644682,-0.303819,3.945366,2.747382,-5.771905,-1.579681,4.683714,-3.620663,9.825757,-6.626062,8.912731,2.136929,1.752989,1.717873,-1.208603,3.648700,-5.819514,5.382005,-7.184419,1.916294,-8.709670,-6.811207,6.044748,2.926883,-9.230527,3.261663,-4.395398,-8.976302,4.671314,2.853977,-9.739804,2.593067,3.333338,-8.960536,5.959505,-9.998558,-3.372010,1.540274,6.845881,-4.911993,-4.055538,2.451249,-5.916545,9.494339,-8.975754,1.430656,0.561951,2.972576,-2.686584,8.147677,5.423103,9.497542,-8.970007,3.950568,4.280499,1.408750,9.836325,-3.368263,-6.172185,8.998636,-0.082845,2.304961,8.040583,-2.083219,7.333300,8.454000,1.318082,-5.953696,4.047071,6.950444,4.854610,9.462984,-8.929665,-1.316358,3.221505,0.004903,7.106924,8.957949,5.119557,-6.001703,4.204308,3.871771,-1.121167,-3.802069,-2.324189,-5.887110,-0.248841,-5.194083,2.022218,9.192694,7.812590,-0.738157,-5.716016,4.759651,-7.471686,-2.740961,-5.712981,-0.723013,2.113325,-9.486729,4.267231,1.776191,-1.530957,-1.459748,-1.524150,-4.035354,-7.834338,-0.534270,8.129759,-7.949975,1.174012,7.894972,-2.083494,-5.384054,4.895076,7.697821,4.940841,-1.983805,9.366363,2.005865,1.440818,5.513773,3.408719,-3.956149,0.625619,-7.633213,3.800959,-8.158884,1.636733,3.725040,-6.427830,9.578764,4.219363,4.923893,-0.344443,-0.983029,8.431568,8.135013,-2.765141,5.938364,-7.677448,-0.697731,7.641583,-9.270476,-5.510562,0.981079,-7.952022,-7.329798,7.088326,-1.463140,7.670465,3.307151,-2.943760,3.616345,-5.483779,3.270631,-7.142412,-8.735437,-8.078572,-3.148523,-4.342038,5.255809,3.212347,-9.986103,-2.175246,-5.152659,6.442717,-7.250333,7.157705,-1.765602,-3.634679,-0.712843,-7.424195,-6.256182,2.558462,6.592878,1.681603,7.443009,-7.950206,1.379960,-0.358324,-3.913179,5.263454,-7.231751,-5.549630,-6.514804,-9.592077,3.034679,5.994896,2.312006,1.401631,-5.571007,-8.761415,3.256051,0.504313,2.954053,-7.763145,3.863380,-0.217510,-9.180385,8.923939,9.530001,-0.670458,-2.486519,-2.478325,-4.381472,-2.262861],[-5.226526,-2.874510,8.126600,-1.291269,-6.035063,1.674500,-5.738085,0.492808,-9.569016,4.575878,-8.253660,4.641425,5.280169,-7.210960,2.983269,-3.851610,6.855106,4.686509,-1.102898,7.768331,-6.169802,4.901894,-7.282355,-5.729608,7.549572,-8.359984,9.299667,-5.940799,-5.658812,-1.711831,7.827333,7.008542,-5.494288,2.441757,0.937520,8.832760,4.810678,-4.893533,2.319978,5.349243,3.391349,-0.942021,8.733868,9.396723,3.185504,4.090846,1.973669,-2.494093,2.670729,-6.705488,-6.457308,-2.508259,-9.197750,-9.773496,9.032652,-5.308203,3.148879,8.020383,3.182815,-0.020625,9.544560,2.363219,7.020904,-9.514552,-7.646260,5.441241,-7.345096,-2.853030,-7.223738,-4.778396,-4.970230,-8.581612,4.409804,-5.049514,9.544921,6.502469,-6.956803,1.802882,-2.160910,-7.226878,-4.588497,-6.817971,-9.448492,-7.993867,8.467317,-6.199089,8.532612,7.013397,4.038469,-5.480253,0.860755,9.840395,-6.175701,6.325131,-3.841131,7.415825,4.531395,1.679310,5.155959,-4.738493,-0.779723,-0.437278,-0.998580,-2.731793,-8.810723,-6.764509,-4.140121,6.588576,-6.499441,-5.113056,9.512351,7.579552,4.830732,-9.656643,-6.656058,2.135351,0.610610,9.994412,0.981583,4.968266,-1.624979,1.218574,2.341503,4.320131,3.599404,-7.755563,-4.712214,5.520120,-0.881027,-1.649278,6.439828,6.785928,7.355630,-7.043403,-0.106660,-6.068628,4.546535,-3.110329,7.020738,-3.259203,1.228502,3.818127,-5.025656,4.335774,-7.693661,-8.077486,8.838116,-6.356489,-1.410902,2.200998,9.442210,6.812313,-6.148513,3.844653,8.835052,-9.907073,9.354855,-9.426557,3.584785,-8.808984,6.630207,0.623785,2.422747,-6.143724,-2.561768,-4.995906,2.851105,-5.171309,6.720345,1.224190,0.483233,6.964985,7.930402,-6.582639,1.411727,-9.296799,2.779312,8.564001,-3.221093,-9.742658,-7.408566,-9.647591,-2.872083,9.377524,-8.767316,5.396013,-0.173302,-2.436410,-8.849413,-6.761730,-7.173257,1.407961,-0.108785,-9.378247,-2.263484,0.968441,3.487833,-4.098378,-6.462803,-9.079813,8.369184,-2.755175,-4.875402,4.988139,-2.377680,7.580479,6.032441,-4.931237,9.525591,-7.718550,-7.191103,-7.200177,7.602177,7.002410,-1.419387,-5.220094,9.123737,-4.861674,-4.712342,4.846953,7.076898,5.133990,7.283650,7.319574,-5.629421,-4.933914,4.058385,-1.464967,5.359309,4.755506,6.771722,1.439400,-8.843242,0.964252,-0.568448,7.511833,3.986267,-9.889050,5.709794,6.534811,6.368168,-6.605014,3.901966,8.127405,-3.145360,-6.504304,-9.737015,5.201279,8.677803,4.278707,8.749887,-7.208692,8.487705,9.138664,-8.993531,-0.075490,-0.640541,-7.394072,-6.280855,-5.102465,-8.038063,-3.224323,3.222442,-3.880283,-4.036997,-0.045136,-7.691039,-2.739631,6.411531,-9.123216,4.904777,1.450002,0.796538,0.338994,7.565605,5.156552,-6.467185,-9.594536,2.238930,5.668416,6.260088,9.186121,-6.914640,4.395675,3.619707,4.361547,2.101223,-5.946922,-4.624255,-1.797013,5.332198,-6.471284,8.077825,5.038685,8.367124,8.329299,-7.182247,-8.826804,-8.888682,-4.221209,-9.416332,-3.798759,-3.814413,-2.105313,-8.661427,-6.590337,-6.912025,-5.996896,-6.612561,-8.614314,-7.048128,-3.047646,-9.057555,9.343332,-9.816988,-1.909760,8.626047,-6.787691,7.717460,-2.174706]], dtype = "float32")#candidate|4987|(2, 320)|const|float32
call_4986 = relay.TupleGetItem(func_664_call(relay.reshape(const_4987.astype('float32'), [640,])), 3)
call_4988 = relay.TupleGetItem(func_667_call(relay.reshape(const_4987.astype('float32'), [640,])), 3)
output = relay.Tuple([call_4959,call_4978,call_4986,const_4987,])
output2 = relay.Tuple([call_4960,call_4979,call_4988,const_4987,])
func_4999 = relay.Function([], output)
mod['func_4999'] = func_4999
mod = relay.transform.InferType()(mod)
mutated_mod['func_4999'] = func_4999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4999_call = mutated_mod.get_global_var('func_4999')
call_5000 = func_4999_call()
output = call_5000
func_5001 = relay.Function([], output)
mutated_mod['func_5001'] = func_5001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4629_call = mod.get_global_var('func_4629')
func_4631_call = mutated_mod.get_global_var('func_4631')
call_5047 = relay.TupleGetItem(func_4629_call(), 0)
call_5048 = relay.TupleGetItem(func_4631_call(), 0)
uop_5066 = relay.sigmoid(call_5047.astype('float64')) # shape=(16, 15, 10)
uop_5068 = relay.sigmoid(call_5048.astype('float64')) # shape=(16, 15, 10)
output = relay.Tuple([uop_5066,])
output2 = relay.Tuple([uop_5068,])
func_5078 = relay.Function([], output)
mod['func_5078'] = func_5078
mod = relay.transform.InferType()(mod)
mutated_mod['func_5078'] = func_5078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5078_call = mutated_mod.get_global_var('func_5078')
call_5079 = func_5078_call()
output = call_5079
func_5080 = relay.Function([], output)
mutated_mod['func_5080'] = func_5080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_5085 = relay.TupleGetItem(func_2421_call(), 0)
call_5086 = relay.TupleGetItem(func_2422_call(), 0)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_5095 = relay.TupleGetItem(func_2626_call(), 1)
call_5096 = relay.TupleGetItem(func_2627_call(), 1)
func_200_call = mod.get_global_var('func_200')
func_201_call = mutated_mod.get_global_var('func_201')
call_5112 = relay.TupleGetItem(func_200_call(), 0)
call_5113 = relay.TupleGetItem(func_201_call(), 0)
output = relay.Tuple([call_5085,call_5095,call_5112,])
output2 = relay.Tuple([call_5086,call_5096,call_5113,])
func_5115 = relay.Function([], output)
mod['func_5115'] = func_5115
mod = relay.transform.InferType()(mod)
mutated_mod['func_5115'] = func_5115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mutated_mod.get_global_var('func_5115')
call_5116 = func_5115_call()
output = call_5116
func_5117 = relay.Function([], output)
mutated_mod['func_5117'] = func_5117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_5121 = relay.TupleGetItem(func_1526_call(), 3)
call_5122 = relay.TupleGetItem(func_1527_call(), 3)
func_4360_call = mod.get_global_var('func_4360')
func_4363_call = mutated_mod.get_global_var('func_4363')
const_5156 = relay.const([[4.129005,1.430100,-6.004680,7.739516],[-7.570856,-5.883156,-6.715489,-7.202299],[7.725252,-7.696093,-4.389239,-8.057074],[2.730723,-8.724071,9.120901,2.881476],[-2.110419,7.490623,-1.823550,6.950591],[8.354817,-1.547705,-0.645948,3.006073],[-7.902132,2.797538,9.510081,3.317975],[5.420774,-0.516951,-6.739334,6.512268],[4.224427,-9.977003,9.993788,-4.659398],[2.585505,-0.294120,-7.083453,1.246710],[-9.226040,7.373450,9.006304,-2.638166],[-0.211837,4.583640,-9.309511,-7.779116],[1.721197,-1.704750,-3.953482,-1.574016],[5.983682,3.554085,-8.716631,-2.747090],[9.105453,-9.808736,-5.962812,4.343509],[-3.140583,-7.234050,-4.193226,-5.368306],[7.254211,-1.391197,2.166242,5.576248],[-1.511360,-0.513124,5.579937,8.505874],[0.024582,7.042342,-3.070305,-3.458392],[3.532559,7.642318,0.621803,-2.269248],[-7.252550,-9.642201,6.888709,7.556450],[-6.887209,-6.612851,-4.864225,-1.278471],[2.685975,-3.994682,8.888463,-8.559171],[2.331605,-2.382623,0.065707,3.755799],[3.878796,-8.817207,7.606629,-5.360136],[8.193761,9.619562,-2.336862,6.261314],[-6.068184,6.027887,2.249784,-0.101062],[-8.628769,5.939211,2.697401,7.934575],[9.327148,0.184842,6.008398,-0.396608],[-9.144677,3.416105,-7.409588,5.591362],[-6.008217,-9.265750,-1.931236,-5.986407],[1.218453,5.012579,-9.064217,4.865051],[-9.656961,-0.081474,2.910128,-5.315298],[-1.446030,-1.433461,6.445549,4.380837],[7.028753,2.929366,9.510948,-6.607083],[0.454063,0.582917,-5.352026,1.641383],[-6.440184,0.537262,4.393327,0.998273],[8.121220,-8.458928,5.344593,-2.734455],[9.695832,9.570934,1.557635,5.227747],[2.309086,-9.376515,8.768915,-7.688111],[6.707794,7.860720,0.022098,-8.842488],[2.251464,7.205850,6.068161,0.310380],[3.735774,4.304112,-6.259700,-8.965541],[4.184745,1.638545,-8.196960,-4.621495],[9.244891,-0.879046,5.773553,2.737830],[0.887699,0.403263,-3.952490,5.502347],[5.027056,-4.130655,2.039104,9.291252],[1.529352,-9.955091,-6.967675,9.738431],[-4.777941,5.512389,2.763617,-7.324340],[6.286370,8.157171,-7.101424,-1.244217],[2.453363,5.415528,7.357080,4.461676],[-8.137016,-0.117604,4.635868,-1.193675],[-9.966204,3.515988,9.466759,-0.427821],[7.928517,-7.613240,5.204784,-5.751621],[-5.410337,7.748549,-0.452927,-6.710945],[-5.834034,-9.502005,3.853579,-3.773390],[-5.205949,4.025573,9.946096,-9.452711],[1.170738,2.757246,6.826704,2.856407],[1.975591,7.345025,2.339630,-1.973427],[3.222229,2.833472,-9.331828,-1.285724],[1.274846,-7.571420,2.341536,-8.312866],[7.190059,0.127386,3.730598,-8.025243],[-0.781780,-3.886957,-8.677690,9.070959],[9.805864,-1.301093,-4.173767,-8.567780],[-7.936804,6.129844,-0.708020,-4.158588],[3.124138,-1.327648,-6.567962,0.545782],[8.160442,-7.027464,0.595981,6.351246],[8.258665,-4.287369,-1.132192,1.709799],[1.911862,-4.258630,-6.280852,8.651068],[8.997595,-6.502520,3.250243,-7.159625]], dtype = "float64")#candidate|5156|(70, 4)|const|float64
call_5155 = relay.TupleGetItem(func_4360_call(relay.reshape(const_5156.astype('float64'), [5, 4, 14])), 0)
call_5157 = relay.TupleGetItem(func_4363_call(relay.reshape(const_5156.astype('float64'), [5, 4, 14])), 0)
func_4999_call = mod.get_global_var('func_4999')
func_5001_call = mutated_mod.get_global_var('func_5001')
call_5167 = relay.TupleGetItem(func_4999_call(), 0)
call_5168 = relay.TupleGetItem(func_5001_call(), 0)
uop_5198 = relay.erf(call_5167.astype('float64')) # shape=(16, 15, 10)
uop_5200 = relay.erf(call_5168.astype('float64')) # shape=(16, 15, 10)
func_122_call = mod.get_global_var('func_122')
func_123_call = mutated_mod.get_global_var('func_123')
call_5216 = func_122_call()
call_5217 = func_122_call()
func_1073_call = mod.get_global_var('func_1073')
func_1074_call = mutated_mod.get_global_var('func_1074')
call_5236 = func_1073_call()
call_5237 = func_1073_call()
func_1323_call = mod.get_global_var('func_1323')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_5243 = relay.TupleGetItem(func_1323_call(), 0)
call_5244 = relay.TupleGetItem(func_1324_call(), 0)
func_371_call = mod.get_global_var('func_371')
func_372_call = mutated_mod.get_global_var('func_372')
call_5247 = func_371_call()
call_5248 = func_371_call()
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_5250 = func_21_call()
call_5251 = func_21_call()
output = relay.Tuple([call_5121,call_5155,const_5156,uop_5198,call_5216,call_5236,call_5243,call_5247,call_5250,])
output2 = relay.Tuple([call_5122,call_5157,const_5156,uop_5200,call_5217,call_5237,call_5244,call_5248,call_5251,])
func_5254 = relay.Function([], output)
mod['func_5254'] = func_5254
mod = relay.transform.InferType()(mod)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5254_call = mutated_mod.get_global_var('func_5254')
call_5255 = func_5254_call()
output = call_5255
func_5256 = relay.Function([], output)
mutated_mod['func_5256'] = func_5256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3455_call = mod.get_global_var('func_3455')
func_3456_call = mutated_mod.get_global_var('func_3456')
call_5262 = relay.TupleGetItem(func_3455_call(), 0)
call_5263 = relay.TupleGetItem(func_3456_call(), 0)
output = call_5262
output2 = call_5263
func_5266 = relay.Function([], output)
mod['func_5266'] = func_5266
mod = relay.transform.InferType()(mod)
output = func_5266()
func_5267 = relay.Function([], output)
mutated_mod['func_5267'] = func_5267
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5305 = relay.var("var_5305", dtype = "int16", shape = ())#candidate|5305|()|var|int16
var_5306 = relay.var("var_5306", dtype = "int16", shape = (12, 12, 14))#candidate|5306|(12, 12, 14)|var|int16
bop_5307 = relay.not_equal(var_5305.astype('bool'), var_5306.astype('bool')) # shape=(12, 12, 14)
uop_5329 = relay.atanh(bop_5307.astype('float32')) # shape=(12, 12, 14)
output = uop_5329
output2 = uop_5329
func_5351 = relay.Function([var_5305,var_5306,], output)
mod['func_5351'] = func_5351
mod = relay.transform.InferType()(mod)
mutated_mod['func_5351'] = func_5351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5351_call = mutated_mod.get_global_var('func_5351')
var_5353 = relay.var("var_5353", dtype = "int16", shape = ())#candidate|5353|()|var|int16
var_5354 = relay.var("var_5354", dtype = "int16", shape = (12, 12, 14))#candidate|5354|(12, 12, 14)|var|int16
call_5352 = func_5351_call(var_5353,var_5354,)
output = call_5352
func_5355 = relay.Function([var_5353,var_5354,], output)
mutated_mod['func_5355'] = func_5355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_371_call = mod.get_global_var('func_371')
func_372_call = mutated_mod.get_global_var('func_372')
call_5418 = func_371_call()
call_5419 = func_371_call()
output = call_5418
output2 = call_5419
func_5422 = relay.Function([], output)
mod['func_5422'] = func_5422
mod = relay.transform.InferType()(mod)
mutated_mod['func_5422'] = func_5422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5422_call = mutated_mod.get_global_var('func_5422')
call_5423 = func_5422_call()
output = call_5423
func_5424 = relay.Function([], output)
mutated_mod['func_5424'] = func_5424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_200_call = mod.get_global_var('func_200')
func_201_call = mutated_mod.get_global_var('func_201')
call_5439 = relay.TupleGetItem(func_200_call(), 0)
call_5440 = relay.TupleGetItem(func_201_call(), 0)
output = relay.Tuple([call_5439,])
output2 = relay.Tuple([call_5440,])
func_5445 = relay.Function([], output)
mod['func_5445'] = func_5445
mod = relay.transform.InferType()(mod)
mutated_mod['func_5445'] = func_5445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5445_call = mutated_mod.get_global_var('func_5445')
call_5446 = func_5445_call()
output = call_5446
func_5447 = relay.Function([], output)
mutated_mod['func_5447'] = func_5447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_308_call = mod.get_global_var('func_308')
func_310_call = mutated_mod.get_global_var('func_310')
call_5453 = relay.TupleGetItem(func_308_call(), 1)
call_5454 = relay.TupleGetItem(func_310_call(), 1)
func_493_call = mod.get_global_var('func_493')
func_494_call = mutated_mod.get_global_var('func_494')
call_5465 = relay.TupleGetItem(func_493_call(), 0)
call_5466 = relay.TupleGetItem(func_494_call(), 0)
output = relay.Tuple([call_5453,call_5465,])
output2 = relay.Tuple([call_5454,call_5466,])
func_5473 = relay.Function([], output)
mod['func_5473'] = func_5473
mod = relay.transform.InferType()(mod)
output = func_5473()
func_5474 = relay.Function([], output)
mutated_mod['func_5474'] = func_5474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2527_call = mod.get_global_var('func_2527')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_5475 = relay.TupleGetItem(func_2527_call(), 1)
call_5476 = relay.TupleGetItem(func_2528_call(), 1)
func_5254_call = mod.get_global_var('func_5254')
func_5256_call = mutated_mod.get_global_var('func_5256')
call_5482 = relay.TupleGetItem(func_5254_call(), 4)
call_5483 = relay.TupleGetItem(func_5256_call(), 4)
func_3938_call = mod.get_global_var('func_3938')
func_3941_call = mutated_mod.get_global_var('func_3941')
call_5504 = relay.TupleGetItem(func_3938_call(relay.reshape(call_5482.astype('float32'), [13, 9, 1])), 0)
call_5505 = relay.TupleGetItem(func_3941_call(relay.reshape(call_5482.astype('float32'), [13, 9, 1])), 0)
func_3493_call = mod.get_global_var('func_3493')
func_3495_call = mutated_mod.get_global_var('func_3495')
call_5524 = relay.TupleGetItem(func_3493_call(), 1)
call_5525 = relay.TupleGetItem(func_3495_call(), 1)
output = relay.Tuple([call_5475,call_5482,call_5504,call_5524,])
output2 = relay.Tuple([call_5476,call_5483,call_5505,call_5525,])
func_5540 = relay.Function([], output)
mod['func_5540'] = func_5540
mod = relay.transform.InferType()(mod)
mutated_mod['func_5540'] = func_5540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5540_call = mutated_mod.get_global_var('func_5540')
call_5541 = func_5540_call()
output = call_5541
func_5542 = relay.Function([], output)
mutated_mod['func_5542'] = func_5542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_5590 = func_1972_call()
call_5591 = func_1972_call()
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_5601 = relay.TupleGetItem(func_2626_call(), 0)
call_5602 = relay.TupleGetItem(func_2627_call(), 0)
bop_5613 = relay.greater(call_5601.astype('bool'), call_5590.astype('bool')) # shape=(13, 9, 1053)
bop_5616 = relay.greater(call_5602.astype('bool'), call_5591.astype('bool')) # shape=(13, 9, 1053)
func_418_call = mod.get_global_var('func_418')
func_420_call = mutated_mod.get_global_var('func_420')
call_5620 = relay.TupleGetItem(func_418_call(), 0)
call_5621 = relay.TupleGetItem(func_420_call(), 0)
func_4700_call = mod.get_global_var('func_4700')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_5628 = relay.TupleGetItem(func_4700_call(), 1)
call_5629 = relay.TupleGetItem(func_4701_call(), 1)
func_3564_call = mod.get_global_var('func_3564')
func_3566_call = mutated_mod.get_global_var('func_3566')
call_5638 = relay.TupleGetItem(func_3564_call(), 0)
call_5639 = relay.TupleGetItem(func_3566_call(), 0)
output = relay.Tuple([bop_5613,call_5620,call_5628,call_5638,])
output2 = relay.Tuple([bop_5616,call_5621,call_5629,call_5639,])
func_5640 = relay.Function([], output)
mod['func_5640'] = func_5640
mod = relay.transform.InferType()(mod)
mutated_mod['func_5640'] = func_5640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5640_call = mutated_mod.get_global_var('func_5640')
call_5641 = func_5640_call()
output = call_5641
func_5642 = relay.Function([], output)
mutated_mod['func_5642'] = func_5642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4202_call = mod.get_global_var('func_4202')
func_4204_call = mutated_mod.get_global_var('func_4204')
call_5725 = relay.TupleGetItem(func_4202_call(), 1)
call_5726 = relay.TupleGetItem(func_4204_call(), 1)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_5729 = relay.TupleGetItem(func_1526_call(), 2)
call_5730 = relay.TupleGetItem(func_1527_call(), 2)
output = relay.Tuple([call_5725,call_5729,])
output2 = relay.Tuple([call_5726,call_5730,])
func_5739 = relay.Function([], output)
mod['func_5739'] = func_5739
mod = relay.transform.InferType()(mod)
mutated_mod['func_5739'] = func_5739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5739_call = mutated_mod.get_global_var('func_5739')
call_5740 = func_5739_call()
output = call_5740
func_5741 = relay.Function([], output)
mutated_mod['func_5741'] = func_5741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4109_call = mod.get_global_var('func_4109')
func_4110_call = mutated_mod.get_global_var('func_4110')
call_5765 = relay.TupleGetItem(func_4109_call(), 0)
call_5766 = relay.TupleGetItem(func_4110_call(), 0)
output = relay.Tuple([call_5765,])
output2 = relay.Tuple([call_5766,])
func_5778 = relay.Function([], output)
mod['func_5778'] = func_5778
mod = relay.transform.InferType()(mod)
mutated_mod['func_5778'] = func_5778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5778_call = mutated_mod.get_global_var('func_5778')
call_5779 = func_5778_call()
output = call_5779
func_5780 = relay.Function([], output)
mutated_mod['func_5780'] = func_5780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4999_call = mod.get_global_var('func_4999')
func_5001_call = mutated_mod.get_global_var('func_5001')
call_5781 = relay.TupleGetItem(func_4999_call(), 1)
call_5782 = relay.TupleGetItem(func_5001_call(), 1)
output = relay.Tuple([call_5781,])
output2 = relay.Tuple([call_5782,])
func_5795 = relay.Function([], output)
mod['func_5795'] = func_5795
mod = relay.transform.InferType()(mod)
mutated_mod['func_5795'] = func_5795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5795_call = mutated_mod.get_global_var('func_5795')
call_5796 = func_5795_call()
output = call_5796
func_5797 = relay.Function([], output)
mutated_mod['func_5797'] = func_5797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_5817 = relay.TupleGetItem(func_1758_call(), 1)
call_5818 = relay.TupleGetItem(func_1759_call(), 1)
var_5823 = relay.var("var_5823", dtype = "float32", shape = (13, 9, 15))#candidate|5823|(13, 9, 15)|var|float32
bop_5824 = relay.multiply(call_5817.astype('uint16'), var_5823.astype('uint16')) # shape=(13, 9, 15)
bop_5827 = relay.multiply(call_5818.astype('uint16'), var_5823.astype('uint16')) # shape=(13, 9, 15)
output = relay.Tuple([bop_5824,])
output2 = relay.Tuple([bop_5827,])
func_5829 = relay.Function([var_5823,], output)
mod['func_5829'] = func_5829
mod = relay.transform.InferType()(mod)
mutated_mod['func_5829'] = func_5829
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5830 = relay.var("var_5830", dtype = "float32", shape = (13, 9, 15))#candidate|5830|(13, 9, 15)|var|float32
func_5829_call = mutated_mod.get_global_var('func_5829')
call_5831 = func_5829_call(var_5830)
output = call_5831
func_5832 = relay.Function([var_5830], output)
mutated_mod['func_5832'] = func_5832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3133_call = mod.get_global_var('func_3133')
func_3135_call = mutated_mod.get_global_var('func_3135')
call_5998 = relay.TupleGetItem(func_3133_call(), 0)
call_5999 = relay.TupleGetItem(func_3135_call(), 0)
func_5829_call = mod.get_global_var('func_5829')
func_5832_call = mutated_mod.get_global_var('func_5832')
var_6001 = relay.var("var_6001", dtype = "float32", shape = (1755,))#candidate|6001|(1755,)|var|float32
call_6000 = relay.TupleGetItem(func_5829_call(relay.reshape(var_6001.astype('float32'), [13, 9, 15])), 0)
call_6002 = relay.TupleGetItem(func_5832_call(relay.reshape(var_6001.astype('float32'), [13, 9, 15])), 0)
uop_6015 = relay.sin(call_6000.astype('float64')) # shape=(13, 9, 15)
uop_6017 = relay.sin(call_6002.astype('float64')) # shape=(13, 9, 15)
func_5540_call = mod.get_global_var('func_5540')
func_5542_call = mutated_mod.get_global_var('func_5542')
call_6033 = relay.TupleGetItem(func_5540_call(), 1)
call_6034 = relay.TupleGetItem(func_5542_call(), 1)
output = relay.Tuple([call_5998,var_6001,uop_6015,call_6033,])
output2 = relay.Tuple([call_5999,var_6001,uop_6017,call_6034,])
func_6039 = relay.Function([var_6001,], output)
mod['func_6039'] = func_6039
mod = relay.transform.InferType()(mod)
var_6040 = relay.var("var_6040", dtype = "float32", shape = (1755,))#candidate|6040|(1755,)|var|float32
output = func_6039(var_6040)
func_6041 = relay.Function([var_6040], output)
mutated_mod['func_6041'] = func_6041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5473_call = mod.get_global_var('func_5473')
func_5474_call = mutated_mod.get_global_var('func_5474')
call_6070 = relay.TupleGetItem(func_5473_call(), 0)
call_6071 = relay.TupleGetItem(func_5474_call(), 0)
func_1830_call = mod.get_global_var('func_1830')
func_1832_call = mutated_mod.get_global_var('func_1832')
var_6084 = relay.var("var_6084", dtype = "float64", shape = (96,))#candidate|6084|(96,)|var|float64
call_6083 = relay.TupleGetItem(func_1830_call(relay.reshape(var_6084.astype('float64'), [8, 1, 12])), 0)
call_6085 = relay.TupleGetItem(func_1832_call(relay.reshape(var_6084.astype('float64'), [8, 1, 12])), 0)
output = relay.Tuple([call_6070,call_6083,var_6084,])
output2 = relay.Tuple([call_6071,call_6085,var_6084,])
func_6089 = relay.Function([var_6084,], output)
mod['func_6089'] = func_6089
mod = relay.transform.InferType()(mod)
mutated_mod['func_6089'] = func_6089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6090 = relay.var("var_6090", dtype = "float64", shape = (96,))#candidate|6090|(96,)|var|float64
func_6089_call = mutated_mod.get_global_var('func_6089')
call_6091 = func_6089_call(var_6090)
output = call_6091
func_6092 = relay.Function([var_6090], output)
mutated_mod['func_6092'] = func_6092
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6190 = relay.var("var_6190", dtype = "float32", shape = (14, 6, 9))#candidate|6190|(14, 6, 9)|var|float32
const_6191 = relay.const([[[6.120254,0.362703,4.152196,-8.306403,-6.744086,4.648065,8.354193,-9.618315,5.187514],[0.150462,9.427569,1.455217,6.088807,9.914992,1.603761,7.758184,-2.424735,6.368177],[4.566951,-0.379201,-9.419862,6.938442,6.068780,-1.317771,3.666514,5.819534,2.526779],[-9.139210,9.668385,-0.382902,-3.391107,7.585134,-1.356366,-6.581771,1.257046,-7.921222],[-2.480982,5.919239,7.235098,6.167605,6.203523,9.214704,0.597149,3.528033,4.873754],[-9.062835,9.633770,-4.061192,-3.690315,-4.519329,7.419309,-5.463930,-0.097392,-7.328189]],[[7.977119,-4.266886,-2.016591,0.349386,6.469795,-3.487530,0.884058,-6.901513,6.799568],[-9.001755,-4.220658,9.451765,4.671348,5.843576,8.655525,-2.702759,7.805149,0.483226],[-1.474852,-6.880344,-3.063894,8.568278,6.502540,-2.287033,-7.265585,-4.026415,4.659476],[5.795419,7.002414,8.055617,-8.225397,9.538694,-6.771120,5.829080,-6.522971,6.637850],[-5.471214,-2.406353,-0.425892,-8.343015,4.904534,2.813045,-2.415479,-0.850931,-0.241468],[-6.503973,5.662385,-4.506120,5.644427,-3.840749,8.276736,-6.555019,-7.256295,8.715748]],[[8.797390,-3.746093,9.735820,-8.982216,-9.812252,0.116093,-8.264292,9.496181,-1.127435],[3.270029,4.158920,5.682508,8.028430,-0.198038,-5.218214,8.561638,-1.633518,-9.807653],[0.571090,5.755873,7.467826,-5.000684,8.063769,2.987034,-2.012499,0.618392,2.338532],[-3.218158,-0.046305,-7.785024,6.022945,-2.027786,9.460810,3.198611,0.731834,-7.697749],[4.653170,-5.411993,-2.927724,-1.089369,1.734535,-4.452671,-7.733064,0.212610,-3.230270],[2.582718,3.806268,1.841844,6.181609,-5.927183,5.161225,6.239259,2.859276,1.061097]],[[-9.113132,-7.605576,9.564882,-3.525269,-3.076195,-2.301021,1.513585,-3.031275,-3.769106],[-1.728101,-3.834434,-8.782223,9.044253,-6.462764,-4.261176,3.546417,-8.565938,-4.200607],[-6.497166,9.936459,-8.692258,4.724971,-6.874502,4.469803,1.588428,-9.418348,-1.079274],[-3.433988,-8.088734,-5.048419,-3.065364,0.599850,-3.929471,9.896983,-5.401333,9.650881],[-1.245963,2.700644,-3.795999,4.064961,-1.002033,3.143278,0.587243,-6.564774,-8.400824],[-0.600381,-6.887750,7.077813,0.314504,-3.582786,-6.617163,-4.383737,-0.758159,0.587479]],[[-1.306499,0.572866,-2.111696,8.404923,-3.213262,9.185419,1.737866,8.074908,-0.393688],[-9.505516,5.876769,2.566796,-4.858333,1.656373,7.146832,5.636416,0.784477,-0.906063],[4.901588,5.933122,-8.615636,-2.629977,-7.108211,0.194332,3.206649,-6.273344,-3.950245],[-8.542348,-6.974683,-4.212829,-5.272258,6.730955,-2.624300,1.737405,-2.665246,8.031376],[8.479543,-6.766744,9.594956,-0.905249,7.156679,-9.368982,0.617247,-9.345947,-3.843316],[9.730042,-3.527182,-5.211657,7.037683,-1.670208,1.488430,-7.239145,7.683233,-3.562164]],[[-6.441216,1.959878,-8.506343,-5.910532,-9.971627,8.325925,6.194601,0.228970,0.031218],[-0.170861,5.270921,-3.703583,-5.728972,-8.126403,9.963767,-2.313331,0.974065,0.420362],[9.194059,9.369779,-8.907187,-0.192790,-1.967704,8.772310,-4.448011,-2.575543,-9.653477],[-7.079524,7.476923,0.018212,3.557741,-2.960995,5.085611,-5.944607,5.409641,5.644156],[-1.002600,9.100564,6.782426,8.001300,-4.941552,-9.804771,-7.249998,2.017455,1.594477],[4.197661,7.644334,5.827259,2.346575,9.802385,-0.929658,0.254431,8.785115,0.890380]],[[8.508887,-1.232892,-3.811712,8.641749,5.581586,-5.285652,5.424218,9.313371,4.565283],[4.618243,9.443845,-0.711032,1.764698,-6.446605,-3.785634,-1.435841,-6.783032,-4.282332],[7.880862,-9.949320,-4.906224,9.837491,-4.637585,-3.592598,1.786215,-9.644026,7.311647],[-1.901717,-7.786877,8.930204,-7.589424,7.109308,-8.597857,1.868851,4.104692,-6.263632],[-3.003669,8.349766,-8.729052,0.066289,2.125406,-5.464141,-7.815403,-8.495940,-3.467932],[8.033781,3.263392,3.626897,-5.276165,3.901173,-0.628496,-3.989315,8.930122,2.156370]],[[6.424914,4.244534,9.190124,9.630173,0.771668,-5.773046,7.749008,-1.300461,-7.276938],[-6.454532,6.241411,-2.792973,7.035525,-6.975797,-8.375344,4.384230,-3.011277,4.005908],[-3.058808,3.007110,-5.957953,2.026259,-2.885674,-3.906858,-3.202552,5.913122,-9.635753],[7.934436,-4.267900,-4.602970,-1.828140,0.750835,-1.756371,-8.787337,8.574791,-7.955923],[0.768343,-3.689044,-1.086529,7.100494,6.886117,-4.749604,-7.725268,-2.953743,1.898911],[-8.060495,-5.867976,1.776865,-5.471475,4.974966,7.017088,8.741331,-4.913192,-6.459289]],[[-7.827637,6.592557,5.300882,8.319164,6.496829,-1.028143,-5.898600,-1.443827,-7.437549],[6.437943,3.287597,3.398708,2.765285,-1.603270,-6.879702,-7.367147,-9.768475,-0.138644],[2.364690,2.248247,1.296416,7.452879,-3.207329,-0.421089,0.320176,3.071157,6.089877],[-2.601933,4.531341,-9.427598,5.042126,-4.768191,-8.153419,1.004458,-6.856212,-4.336608],[8.757241,1.324287,-8.069129,-3.814697,-6.644852,-1.012505,-7.422420,-9.925080,9.546195],[2.180232,4.958787,-7.894570,9.128414,4.080874,2.573151,5.193660,4.122737,-5.257865]],[[3.456493,-2.661580,2.124124,5.620377,2.043030,7.924575,-9.448264,0.754416,4.662356],[9.579162,-7.266565,-5.872489,-3.965131,-2.482903,7.466689,0.001900,2.307918,-9.963282],[6.493471,0.938106,1.447291,7.290274,5.347679,7.828541,4.464563,0.415433,7.526278],[3.558873,-5.925866,8.757959,-5.681673,-1.293935,-6.179678,-7.221520,-5.363204,-5.858743],[5.772891,9.939289,0.889566,9.809577,2.284258,-1.515567,-6.342138,-9.541065,1.039394],[-7.752272,5.400457,1.300699,9.381269,1.254210,6.209145,9.701469,5.896523,-1.775127]],[[0.633921,8.391765,-5.364983,7.688248,1.663326,4.774075,-6.842583,2.388223,-7.569864],[8.213206,-2.907657,8.825561,6.675039,-0.203172,2.986417,3.341018,-2.299256,7.594129],[-5.960718,-5.465397,8.968838,-2.290777,9.562496,9.278303,-9.314923,-1.227105,3.920064],[5.627231,-6.543482,7.789333,-7.745377,4.603158,-5.321132,0.281022,5.608741,-3.834720],[-2.404586,-6.214966,-8.870516,0.725293,6.837920,-8.307298,-9.013845,5.894111,4.174014],[-0.387052,6.859894,2.969277,9.944753,-8.455806,-9.033463,5.365885,3.251846,-3.540835]],[[0.879351,-9.814194,2.817819,9.372140,-5.581278,8.979711,0.404016,2.021174,5.957155],[-4.662268,-6.017567,5.928088,-9.304395,8.721947,6.981431,6.227022,0.858500,0.484872],[-0.387950,-7.929252,0.781719,6.931046,-1.857250,8.515443,7.976303,-7.752150,-2.678457],[-5.804029,-8.537415,-1.854453,6.538159,-3.407492,8.692259,-8.568223,-1.715746,6.703962],[-7.178825,-9.159235,8.136439,-6.564762,-9.467275,-5.273465,-5.470580,6.612555,-9.775975],[-2.394399,1.245437,3.201969,-1.578170,8.801158,-9.522051,-4.710697,4.132085,6.937738]],[[-2.632429,5.981497,-1.617909,7.760486,-8.205541,4.256286,-3.753925,-6.001002,-5.793182],[6.883353,2.858479,7.340754,1.119562,-1.646292,6.102848,1.775366,4.846935,-0.889788],[9.560432,3.883469,-0.867329,-0.125899,-7.095906,-4.906008,-9.267680,-4.753615,-2.968815],[-9.259484,9.096069,-5.419778,-6.470959,5.683785,-9.506636,-7.177645,8.986937,1.277426],[-2.777316,0.874116,6.158457,-9.533102,9.056146,6.272630,-1.866217,4.735397,5.844105],[-0.356887,8.460641,1.962277,1.521281,3.125120,0.560479,-8.965345,4.785278,4.176693]],[[-7.127000,-1.345260,-0.412818,0.966919,5.384417,-1.213446,4.467322,9.253136,-0.045306],[-9.717069,-2.809853,7.231925,9.618835,3.785270,2.782399,6.236967,-1.035608,8.389736],[7.435555,-2.629386,1.350362,3.087874,4.121359,7.653490,-9.439615,-4.443445,-4.055403],[-8.963089,0.555001,-0.365761,-6.193258,-9.283564,7.652500,1.690908,2.329673,-4.225993],[0.973500,0.543479,-7.314986,-4.680669,-2.944024,4.280253,-2.944875,-2.983877,5.097435],[-2.515125,-3.774171,0.187445,-7.569394,6.558009,-7.872742,-1.236846,5.468983,-9.777843]]], dtype = "float32")#candidate|6191|(14, 6, 9)|const|float32
bop_6192 = relay.divide(var_6190.astype('float32'), relay.reshape(const_6191.astype('float32'), relay.shape_of(var_6190))) # shape=(14, 6, 9)
bop_6199 = relay.equal(var_6190.astype('bool'), relay.reshape(const_6191.astype('bool'), relay.shape_of(var_6190))) # shape=(14, 6, 9)
output = relay.Tuple([bop_6192,bop_6199,])
output2 = relay.Tuple([bop_6192,bop_6199,])
func_6205 = relay.Function([var_6190,], output)
mod['func_6205'] = func_6205
mod = relay.transform.InferType()(mod)
mutated_mod['func_6205'] = func_6205
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6206 = relay.var("var_6206", dtype = "float32", shape = (14, 6, 9))#candidate|6206|(14, 6, 9)|var|float32
func_6205_call = mutated_mod.get_global_var('func_6205')
call_6207 = func_6205_call(var_6206)
output = call_6207
func_6208 = relay.Function([var_6206], output)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_6258 = relay.TupleGetItem(func_1692_call(), 0)
call_6259 = relay.TupleGetItem(func_1693_call(), 0)
output = relay.Tuple([call_6258,])
output2 = relay.Tuple([call_6259,])
func_6295 = relay.Function([], output)
mod['func_6295'] = func_6295
mod = relay.transform.InferType()(mod)
output = func_6295()
func_6296 = relay.Function([], output)
mutated_mod['func_6296'] = func_6296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3375_call = mod.get_global_var('func_3375')
func_3376_call = mutated_mod.get_global_var('func_3376')
call_6302 = relay.TupleGetItem(func_3375_call(), 0)
call_6303 = relay.TupleGetItem(func_3376_call(), 0)
output = call_6302
output2 = call_6303
func_6304 = relay.Function([], output)
mod['func_6304'] = func_6304
mod = relay.transform.InferType()(mod)
output = func_6304()
func_6305 = relay.Function([], output)
mutated_mod['func_6305'] = func_6305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4202_call = mod.get_global_var('func_4202')
func_4204_call = mutated_mod.get_global_var('func_4204')
call_6319 = relay.TupleGetItem(func_4202_call(), 0)
call_6320 = relay.TupleGetItem(func_4204_call(), 0)
const_6321 = relay.const([[[4.789819,1.209449,-4.636528,-8.631471,-4.097733,-8.153113,7.912607,-7.701862,5.763614,-1.078161],[-8.883049,4.273596,-2.411019,-2.291656,-5.913217,-6.934843,-5.198994,0.239950,0.399191,-4.202578],[9.278353,2.720203,6.723772,6.312209,-7.265007,5.977531,5.782623,-5.201904,-6.716029,-2.283821],[-2.031513,-6.039454,2.200297,9.860252,1.615761,-8.200269,4.583553,9.610717,7.236699,1.210246],[9.610725,-3.789960,-2.340684,-1.662226,0.335388,8.972912,4.373035,-7.080295,-5.016851,4.612718],[-3.800651,-3.257055,9.217191,-5.688394,-0.411404,-2.321122,-4.063585,-1.792508,0.949247,0.027593],[5.817950,1.540532,-1.521961,1.467615,2.145151,5.984406,-7.740649,0.428416,9.442699,1.080797],[-4.163156,6.633735,-1.281995,4.819371,-8.803282,3.900162,1.044524,-5.105345,-0.635804,-1.320130],[7.307508,8.322805,6.685229,1.704963,-9.578156,-4.186801,5.597440,9.965819,5.915919,3.834902]],[[0.281410,-8.711735,0.638853,9.420583,-5.395241,-9.428628,1.223468,-8.658134,-0.719405,3.050282],[-5.249890,7.374142,-0.043245,1.272851,9.804060,8.894675,4.719795,-3.982066,4.908014,3.395185],[9.816532,5.023963,8.830966,-1.252512,6.456717,6.163337,3.526527,2.484140,1.886755,-8.533621],[-5.138028,-1.796516,2.219891,-5.357326,-9.579979,-7.856975,5.492983,-1.524265,6.405963,2.103715],[-1.919717,-5.732474,4.368500,7.288451,3.962542,-3.258563,-8.405599,9.216201,3.555417,-9.910264],[7.977918,6.014535,-4.850244,-2.864034,-3.882251,-1.632225,-1.901986,9.214607,0.352235,-9.382367],[-1.629049,-6.430422,9.879948,-8.272627,6.373440,-2.368064,5.666344,-0.292591,6.532871,-9.452346],[-1.678353,0.576319,8.127533,-7.378012,6.404001,9.190200,0.799803,-0.615088,-8.603828,1.756417],[7.232173,-0.097495,-8.346613,-3.257287,4.331787,2.210666,-0.405640,-9.535441,9.286268,-0.822551]],[[-9.091913,-4.641841,4.604433,-9.140653,7.267502,4.308315,-6.554664,-2.736967,-8.877538,-8.801595],[4.751466,2.960725,-6.614296,1.864962,1.097053,2.269312,-8.724459,5.616762,-9.090240,5.333339],[-5.298907,5.314960,-5.770334,1.755449,-6.518494,2.361643,0.143063,1.029442,-8.847011,-7.973190],[-7.098265,6.303347,6.986253,-8.636042,8.205838,-3.926234,5.944489,-9.525819,0.952863,-4.512664],[3.471013,0.809883,1.587942,3.550903,1.024116,9.378506,2.250202,-9.250967,0.268153,-1.960999],[-7.558929,-1.412421,-2.319491,-2.841379,-9.567385,-5.654774,-5.018194,7.753100,-4.401849,2.600881],[-9.103160,-7.550006,-3.866936,-9.738432,8.701430,-6.424478,8.601362,9.889593,1.505593,7.923919],[5.089959,9.486294,8.569453,0.834284,4.308265,-1.132802,3.906773,0.919083,0.343899,5.385234],[8.540918,0.603490,8.473716,-9.566511,-1.807234,-0.170809,9.172325,0.609038,-8.680287,1.113970]],[[1.139161,1.282561,-8.312795,-3.791996,7.806091,-0.231327,6.455421,4.076557,0.891570,6.630133],[-4.723747,7.898580,-5.922141,-1.320666,4.489549,-0.156861,3.985959,2.298126,3.591374,-4.706667],[5.981455,3.726131,-2.318334,5.661187,-1.462509,5.597478,2.967865,0.258945,6.972872,-3.525221],[3.861247,2.792134,7.373810,-1.731150,0.692441,6.441081,9.631177,9.944030,4.269875,5.036526],[-7.589464,-1.324934,0.080255,1.820816,-0.136156,6.285158,-2.407814,-4.938362,4.435203,-3.611133],[0.849611,-8.933739,-1.688294,-4.750917,-6.044661,-3.723773,-7.934036,-4.185666,-7.560018,-5.600140],[-3.970015,-5.052932,2.867504,-8.441980,8.977274,4.473516,-7.484761,1.202042,0.190648,-7.787124],[-6.304659,-4.761506,-7.700444,-6.783596,-6.445821,0.206450,0.507509,-2.212491,-7.539623,2.196968],[1.160672,2.209278,-0.114839,1.155641,-6.328067,-8.948773,-1.917481,-4.122093,4.973533,2.422474]],[[9.202844,-5.941208,-1.838538,5.495760,6.542294,-2.847947,8.927642,-6.219958,-1.948639,-8.142756],[-8.830588,0.454488,4.807240,7.733617,4.401178,6.884857,5.756006,2.222595,-7.480543,-4.843286],[3.522777,-4.617658,-7.741449,4.521453,-0.966308,-7.878333,-8.886881,9.407558,2.255673,-2.115224],[0.929342,2.264072,-3.356048,-0.975824,-3.373062,-2.248538,7.678486,-8.141829,-9.855541,5.533281],[3.638599,8.726523,9.257555,-9.270677,8.715877,7.410270,-8.680994,8.144919,0.466163,2.242523],[-7.819084,-8.324154,-8.465859,-6.808518,-5.692331,-0.115467,0.863874,0.101469,-3.391547,3.151528],[-8.851499,1.025914,4.739821,2.481363,-4.458709,-0.654849,4.327905,2.477683,-9.145339,-3.650253],[1.677172,-5.103356,-8.946634,0.411941,6.694466,-9.460349,-1.248803,-1.719480,-9.570183,-8.520864],[-5.327318,4.930828,6.759627,-2.687435,-7.773575,-5.067747,7.447692,-7.771935,-6.710624,-7.867664]],[[-6.481198,-8.831820,-7.921229,2.283881,-9.427546,-7.227103,-2.676313,-5.807768,-3.507556,0.646449],[5.215829,-7.905460,1.510345,-9.238568,-6.877458,4.671762,3.933361,7.197236,6.076815,-0.133248],[5.167093,-1.121480,6.727228,9.286056,3.265559,-9.635469,3.180090,1.126978,-6.762077,-7.604038],[8.340544,9.903118,0.093677,-2.255184,2.042742,2.480814,2.919016,0.599187,-1.608265,-8.842467],[6.881361,7.404639,0.135117,8.714540,-0.304437,7.760483,-5.439093,1.189345,5.660514,-2.672083],[-4.909996,7.205926,3.736140,-7.271488,-4.508588,-2.926076,-9.138812,-8.822248,-0.544020,1.252084],[6.593672,-6.469643,8.577172,-5.314284,-9.831211,-3.832838,-3.927595,-8.651495,-4.706991,8.769778],[-7.326350,-9.915464,0.819044,-8.953516,8.823840,2.424162,-6.927584,-0.080752,9.774942,4.454976],[1.979011,-5.735314,8.873307,3.677890,-8.752238,-7.211544,-9.693438,3.949384,8.678118,-2.807597]],[[3.608150,-7.670864,7.181642,3.538521,5.681070,-4.445277,-6.893106,-1.000755,-1.617618,2.294702],[-2.334956,1.364709,8.489491,1.942397,-1.088250,1.199575,3.366195,-2.651681,-0.204366,3.750315],[-5.703260,-9.776972,-2.103804,-7.055043,-6.149833,3.401221,-4.927533,-9.591768,0.949259,-5.190186],[6.554993,6.294688,4.920190,9.885641,-3.607812,8.984310,6.265312,4.133175,-2.292302,-1.365947],[-3.660275,-6.977940,-5.032659,-6.993786,-5.643585,6.445166,-9.969814,-8.622404,-2.622652,0.470381],[-4.411831,1.534466,-2.502146,4.004046,6.512058,8.549156,-5.938684,-6.150545,-0.632791,-4.131276],[7.438179,-8.704804,5.383045,-0.253603,9.874067,-1.236295,-0.487136,3.540814,-7.355776,-8.491622],[-7.934513,5.972898,7.328931,0.259337,-6.299783,-6.409609,7.689224,3.507988,5.354440,9.184880],[2.752531,-8.140110,0.212183,-5.620682,-2.322304,7.801429,9.510643,4.019853,-1.912375,-7.382013]],[[8.982421,7.907798,-8.051614,6.247433,-6.985777,-5.334004,-7.934011,5.959340,-3.300598,6.965055],[-6.997772,5.740954,-1.294475,-3.149266,5.817947,2.934804,2.343238,2.428099,-1.767082,5.607054],[2.880406,-4.159990,-7.673964,-1.172941,-8.514120,-9.971295,-0.349871,-5.305921,-6.852946,-0.262244],[4.911275,-0.077816,-7.651817,-1.691088,-3.448481,3.437550,4.673338,7.958571,4.221665,-4.221082],[-2.666705,5.503026,-4.787217,5.582855,-1.081149,-3.148615,7.527252,2.491239,1.376543,-2.503525],[8.493351,7.519601,-3.188464,1.368269,-8.870904,9.493593,-7.683730,-8.544951,-5.960716,3.276037],[6.517895,-4.249492,1.919898,-7.825295,-1.970508,-8.397949,-3.179236,-9.382306,4.530859,-4.067448],[-2.402216,-1.186571,-5.145604,3.760362,-3.792018,-8.532836,7.508167,-2.141617,-1.967168,8.141797],[-4.328031,-9.292744,7.557388,2.748369,-9.212438,5.863554,9.094930,2.095680,-8.430869,-0.187418]],[[-3.396123,-9.823296,9.415751,-0.761976,6.639460,-1.732101,3.381255,-4.058106,-1.969056,5.686807],[6.338750,3.218339,-8.145018,4.047873,5.753850,9.712880,-5.470702,0.989482,5.324588,0.166661],[6.007102,-1.841927,-3.626970,-7.501567,-1.927416,-4.577794,-0.843489,-9.462406,-6.934555,7.181146],[1.529562,9.199427,-0.982476,0.910293,-2.172263,-4.931827,2.347309,0.659609,2.004226,-8.008519],[2.456833,4.395466,-6.053784,7.796228,0.153737,-2.884970,3.333976,-9.600548,0.392266,1.767811],[-1.297841,0.934674,-1.223961,-1.902604,-8.832252,9.947372,3.881624,6.204489,-8.445186,-0.621231],[4.572933,-5.249934,6.054688,-1.621309,4.196328,-1.404354,9.535757,7.729420,-2.094961,4.465437],[-2.962441,7.107664,-4.394717,2.153682,6.182411,-3.183145,-0.288184,6.277622,-3.999591,-6.531015],[-9.730008,1.240086,6.507617,0.369297,-9.633032,-8.140079,-8.233381,-6.701070,0.018087,5.409241]],[[-0.169790,0.054315,2.702950,-1.884876,0.379898,9.661160,5.349793,8.668647,2.474523,3.813374],[-5.105092,-8.596038,8.252714,2.211486,-7.039577,9.679338,-2.640767,3.361367,0.838083,1.157482],[1.143947,-8.751478,-9.326890,9.189939,0.338553,3.676292,-0.092377,-2.755067,6.931385,-4.604112],[-8.511860,-0.211981,2.542981,-4.530735,5.340932,5.235948,-9.695269,2.924256,8.571795,-0.900652],[1.097098,-9.901587,9.604662,4.313594,-0.005852,-4.116104,6.002794,-0.387715,3.057939,-9.861584],[-5.472613,1.951090,6.553596,5.856297,6.222296,5.384669,-5.030401,-6.282006,-7.307954,-2.364635],[-4.426351,-8.299185,9.041633,-4.532398,2.132362,1.166788,-6.110181,6.189104,7.075236,-1.943488],[-0.977591,-7.645126,-7.218357,0.139145,-2.136160,4.443890,-9.300535,2.786281,-0.669808,-5.663414],[-2.948029,-5.858063,-7.480971,-0.118262,-3.123499,-1.379058,6.678896,3.685467,-4.720428,-8.897389]],[[-6.121298,6.447990,6.261204,-1.038176,-2.899454,-9.944940,-5.500836,1.402940,-8.581179,1.294367],[-2.538596,9.125833,-2.224573,0.506604,3.960447,7.444238,-2.752704,6.677166,2.166528,6.577969],[-1.069614,-1.486940,-0.384811,-7.260604,-7.983146,-6.599000,6.895575,-8.273727,-0.662181,-6.643810],[7.078381,-0.618999,-6.248483,-3.140807,4.758551,7.175502,4.583462,8.181773,3.913585,-9.756035],[3.812412,2.006687,-1.426169,-7.597751,8.220881,8.469011,-0.657708,-4.725558,3.903021,9.173884],[2.161700,-3.318903,-2.911056,-5.162480,8.750780,0.333708,5.930873,-2.182292,-7.795973,5.153214],[1.513282,4.324774,-9.916309,3.922883,-6.062070,-4.868358,7.637164,-9.343108,-2.364175,-3.146180],[7.409977,-5.383226,-5.606971,-6.986992,7.080944,-5.884809,-4.500957,7.488036,-3.274678,-2.265992],[9.900995,-4.984672,-5.538004,-3.995784,9.022230,-8.816571,7.087348,-5.095895,6.123277,-2.133317]],[[-0.451926,-7.440688,-5.612582,0.614235,-3.798617,0.504379,-3.088904,-3.279286,-1.725752,-0.876027],[8.747558,-3.671548,6.090734,-3.926971,-5.553395,-2.030009,-0.353903,2.476969,-6.353870,8.931558],[6.112732,-4.327483,-5.530396,-6.342364,1.442814,-0.280495,5.145655,7.070563,3.967644,-8.218162],[7.025740,-3.146891,2.176433,-7.146128,-4.328206,-3.883563,7.842392,-9.605744,8.195433,-9.891525],[4.581356,-8.848127,-4.086258,7.142354,6.280180,7.475311,-2.948213,-8.338992,9.551208,5.303461],[-4.685709,9.274517,-8.348485,0.082489,-0.376066,1.187770,0.783582,7.037651,5.306716,7.756833],[-2.109823,1.320602,9.966331,-7.678903,5.640545,-0.885226,9.282711,4.264567,6.838920,9.348115],[-2.554702,8.422139,-8.071422,7.372257,-5.856671,1.754139,9.976894,8.866847,-8.156771,-3.135418],[-8.409733,-5.500344,-8.924452,6.562634,-9.451166,-3.456403,0.585263,-8.495153,-6.302799,-6.376724]],[[1.462214,7.889094,-8.273455,8.728753,-7.966466,-3.983484,-1.038588,-4.539976,-9.378274,7.468677],[-4.377989,-9.758684,9.032184,-5.442160,-1.989527,-8.446382,-4.735837,7.754480,3.901748,8.562537],[-7.105024,-5.511000,-9.337572,1.141776,-6.060256,-6.947077,-1.385760,5.543726,1.637208,5.823363],[-0.805754,4.113675,0.478213,0.581741,6.094820,-5.222187,2.682827,8.107607,8.089596,-2.644146],[0.364566,8.678819,7.189337,1.300209,-9.143563,1.648202,7.277406,1.164318,3.964580,5.918124],[4.618164,-4.847193,-6.649989,0.796487,-5.876255,0.661724,-7.359941,-3.701360,8.756034,-6.860676],[-5.276479,-1.031991,2.226095,9.701139,3.041144,5.930025,-0.368046,2.906351,9.075395,1.866854],[-2.032057,9.256241,2.700933,4.321726,-4.485512,-9.675247,6.678843,-7.389885,-6.847895,2.125554],[-7.873422,-5.434771,-4.240690,1.790654,-8.766135,8.035508,5.170107,6.146664,-2.221711,-2.230231]]], dtype = "float32")#candidate|6321|(13, 9, 10)|const|float32
bop_6322 = relay.not_equal(call_6319.astype('bool'), const_6321.astype('bool')) # shape=(13, 9, 10)
bop_6325 = relay.not_equal(call_6320.astype('bool'), const_6321.astype('bool')) # shape=(13, 9, 10)
func_2179_call = mod.get_global_var('func_2179')
func_2182_call = mutated_mod.get_global_var('func_2182')
const_6337 = relay.const([-3.716805,-5.449465,3.636159,-3.791609,1.753777,-4.083410,-8.914940,-5.423098,-1.929774,-4.634975,9.806390,5.254148,-2.453578,0.103040,0.830568,-4.054868,-8.227140,-5.178334,7.638299,-1.772809,8.827257,-8.283430,6.324701,9.986833,-9.905799,-6.776412,-4.527122,-0.407777,7.916270,0.509986,-5.012544,-4.841469,-4.825960,-5.781703,6.955013,-4.763311,-5.342640,9.273381,-1.552964,3.510116,-3.955337,-4.944974,4.585066,-0.944020,-6.366705,4.064800,5.525017,8.229850,2.851583,-7.986367,-6.801833,5.055983,9.060518,-9.836277,9.677153,-6.463702,-6.080124,4.262753,0.934775,-0.646448,5.987960,-2.073426,3.100195,-7.153936,-4.278099,5.311600,0.724867,5.257695,1.532046,-2.222739,5.088437,9.262521,-5.541989,2.296636,-7.053838,6.396726,-7.096519,-3.280984,-7.566677,-4.481328,5.118764,9.499969,-8.295123,2.132532,1.961484,5.661860,-9.502216,-5.121819,1.256913,-7.662598,3.731448,0.804564,-1.532064,0.334500,-6.250357,8.023905,1.680380,-4.444465,4.707566,-9.624659,-8.477350,2.130115,-3.830759,1.826857,3.653330,7.881730,7.692827,-3.189146,-9.553230,-7.375116,7.640375,1.478002,2.930444,7.681285,3.119533,5.919719,7.697999,8.490395,-3.744049,9.737669,-0.701818,-5.848854,8.639132,1.589171,-4.884424,-5.219602,0.287253,-1.010798,8.952432,8.915414,1.465759,-7.840211,4.728588,-7.419592,-9.257489,-9.705411,-9.455104,5.563590,7.708654,-2.790638,-3.228381,-5.818363,-1.115059,-2.014753,-7.961893,-6.499786,-5.102616,-5.610078,-1.310265,7.389498,-9.621016,-7.848704,-1.092348,-4.197295,-5.194911,4.945047,8.671372,6.604407,8.287658,3.697495,6.868738,0.424625,3.439186,-3.969875,1.224266,-5.190973,9.911043,-1.049238,-9.522751,1.844185,4.988493,-3.156689,-4.059431,-3.328993,6.821085,1.223076,-4.108630,5.010993,-7.971718,9.153523,9.338509,9.868956,-7.890888,5.468278,-9.342026,-6.677402,0.770831,-4.562734,-8.831024,4.474653,5.679377,-2.312923,-9.701386,2.088372,2.159739,-8.042420,-7.250332,5.758246,1.679562,-9.491101,-2.793897,-5.943612,7.671784,5.204957,7.695753,5.228362,-0.829376,-4.652660,0.914768,9.943266,4.391221,-1.535087,-1.402856,-1.952145,-7.354228,5.751905,4.284827,-0.655121,3.142977,-8.820761,4.196624,4.423034,-5.590764,-8.119322,8.737668,-7.079633,9.362098,-9.453741,4.018667,5.766439,9.489997,-4.472016,-3.915988,8.838882,-9.629638,2.341540,-7.174478,7.507209,-2.960856,-1.563380,-0.292228,-9.210150,3.598784,7.495611,-1.546655,-9.442382,8.414607,-2.338424,-6.905449,0.450468,-6.533970,-7.771944,8.733161,3.192988,7.732003,7.304746,-7.900362,5.716341,6.453457,-4.873613,4.051370,6.658616,1.016944,6.697105,-1.523580,5.643349,5.147153,0.013790,5.715955,-7.156993,-9.070243,-0.458940,-3.840664,5.921358,-5.727057,7.968579,-6.823367,1.191183,-9.000917,3.406336,5.144183,3.024493,-8.547757,-5.461212,9.579227,-7.696880,-3.244915,8.849372,-2.065523,-1.998704,-9.562530,8.643694,8.055137,0.467314,2.931248,-5.593572,3.803316,6.083103,-6.476269,4.301452,-5.401250,4.874192,7.677600,8.666650,7.673497,-9.403820,7.620283,0.008449,-9.194231,0.672839,6.207516,3.418753,3.429257,2.778344,-2.701982,-9.643829,-5.673865,2.523004,-7.507662,-2.756647,1.782186,6.956267,-5.218784,4.381741,8.159952,-9.793518,-3.935185,0.419933,-8.441857,0.447982,-8.844871,9.774777,5.203156,-7.306356,-6.155364,-4.443147,2.310370,-6.246247,-3.253321,6.816484,-5.060576,-2.807783,1.086932,7.875935,-0.189972,-4.196935,-4.709660,-1.984911,-8.422229,8.376621,5.410751,-2.049638,8.933872,-7.432670,-2.098473,-6.037978,5.842391,2.312821,-0.818177,-4.940702,5.050817,7.378178,-2.734680,-0.999479,-4.225500,5.648017,1.565637,6.044842,8.183662,-5.603798,5.154673,-3.770345,5.705414,4.630613,-7.091991,5.600209,-6.411521,4.823231,-5.350499,1.874887,1.961868,-7.527773,4.428143,-7.365561,4.878844,-6.564014,9.275898,6.723475,6.825772,-4.084825,-9.458501,1.371216,8.012266,4.579539,-9.158961,-2.175644,-2.190250,-5.625561,-4.745663,-9.603109,9.275416,-8.757953,5.041373,-8.442430,-5.280003,5.878690,-3.101107,7.232241,6.247615,0.883038,-7.827137,-0.741752,-4.821899,-2.816321,8.843339,-1.749801,1.268109,2.136964,-9.303070,0.046691,-8.509804,3.527749,-4.532150,-6.132422,3.193545,6.400358,-8.390318,-2.241970,5.794360,7.162474,6.303691,7.164274,3.384865,-1.728357,-8.956550,-0.066964,-1.600949,8.221398,7.908468,-4.370631,9.114780,-6.993987,4.837694,-9.882800,6.366824,2.906459,6.964262,6.355135,3.589813,-9.528998,-7.124624,1.959605,-3.778247,3.488256,-8.011204,7.337442,0.232577,1.967519,-1.691377,5.119428,-7.307325,4.751536,-5.616055,-0.462522,-6.346649,2.286120,1.349353,1.394261,-1.383069,7.495710,-5.807459,-5.368475,-7.937417,5.842515,-3.106035,-5.239416,3.170745,-7.714574,8.369443,-9.857414,-5.941294,-4.518968,-6.993783,5.720088,-5.023925,3.130354,2.451937,-8.401208,-6.458673,5.832850,3.332718,4.421330,5.226909,-5.035637,-4.697105,-0.775451,-9.439366,-8.084950,-5.581568,1.541984,9.548463,8.121894,4.514675,-7.805817,0.575844,-1.207951,-9.274185,-3.771359,4.556929,-0.453855,9.836250,-0.340103,5.279726,-3.358170,3.250739,-4.264573,-0.662563,4.378822,6.552954,8.381850,7.845649,7.117155,0.679844,0.201371,-0.057338,-9.590392,-2.466428,-2.113068,-1.013642,4.279181,-8.080659,-3.140280,-4.322382,-9.263539,3.875620,-5.172315,1.608502,-6.487303,4.405108,-1.051328,1.565145,5.545931,5.794422,6.176828,-5.042156,3.574952,-8.751331,-1.465956,-0.258250,8.837155,-5.751721,-8.921920,9.438016,2.023055,2.116181,3.680248,-2.201812,-1.175394,-9.114454,6.281641,1.037558,5.161115,-3.452001,-1.736881,0.536482,3.228008,7.093925,1.801977,-3.286393,-8.096932,-7.062266,5.780739,-9.946434,9.960156,1.227588,-4.434110,9.557624,3.931923,9.139939,-6.942627,5.788806,-0.685054,-2.946308,5.554730,-0.333779,-1.918401,9.971644,-8.440197,9.522623,-2.408976,-3.441785,3.973729,7.987554,-4.012468,-7.318839,2.825970,-8.698798,1.181946,0.962779,1.191958,-5.762436,8.635807,2.724661,7.541433,0.115260,-7.110696,-9.941439,8.876424,-7.249216,-2.068993,0.520900,-9.164711,-4.432193,-8.470718,-8.169168,6.866393,2.626916,6.828924,-0.310246,3.947658,-8.616156,-5.067855,-4.924739,-9.263699,9.574061,3.441999,-4.660087,-0.385027,3.936599,2.424374,-3.864804,-4.370174,4.320546,2.819979,9.363306,8.311746,-3.642467,-1.808127,9.017311,6.066865,-2.543188,7.420091,-5.695256,7.331431,-0.531316,7.493131,9.872828,-0.944762,3.533057,7.589493,8.762117,1.062665,-2.982361,-8.441868,-6.451812,-1.075694,-4.016334,-0.724827,5.263015,2.357388,-7.295634,-9.964580,-3.076312,-6.411129,-0.349294,-1.650063,-8.680919,3.416092,-1.377065,-0.335721,5.190527,4.206823,6.071195,-0.897317,8.186937,-4.319715,8.225557,0.884275,-9.160224,1.667523,8.442215,-1.899984,2.716078,-2.234045,4.128834,7.336870,4.003233,-0.295736,-2.156148,3.729585,-7.970696,6.807367,9.488028,-8.792345,-0.244123,-3.884261,8.124918,6.125463,0.639187,-3.672215,-7.324549,3.031707,-9.084801,-9.417180,5.662669,-0.857378,-2.919348,1.873319,4.433414,6.560522,7.066779,5.443556,-3.954306,-9.960125,0.105757,-4.339615,-1.862357,6.689096,1.367337,4.365858,-5.431600,6.003238,7.092610,-6.595085,-2.040939,-9.836354,9.504430,-4.698473,-3.202805,2.848030,-8.245771,1.896151,-5.215099,1.137412,2.443531,-8.717910,7.987201,-5.778504,-2.121043,0.020988,-2.347312,-1.424602,6.575799,2.181909,3.304801,5.956007,-1.576550,-1.174830,-7.118505,-8.695436,-1.275927,7.805403,-8.389973,-8.966113,-7.000591,8.460306,7.908480,-3.974481,6.518990,-9.675522,9.714808,-3.705597,3.980639,-6.489062,-6.304350,6.970093,4.423411,-0.788122,-2.373074,-1.677736,-9.745884,7.429120,2.104534,8.242951,6.048557,-5.224855,2.772962,-9.922863,6.599448,-9.601751,9.747986,5.043366,-8.406169,6.219988,-1.650411,9.235308,9.662842,4.792845,6.262172,3.676898,-0.452455,6.114914,-3.075488,-3.599286,-0.169748,-4.053662,-4.587734,-9.692713,7.404347,9.117046,7.941717,0.055582,0.969755,8.667809,9.718669,2.334078,-2.558701,0.108983,-3.478997,6.011410,0.131532,1.250402,7.275452,-6.308926,8.768683,-8.900115,2.461286,6.439033,-5.270254,1.184472,-6.650014,-8.847838,0.242895,4.792820,1.245829,-5.831326,-7.601650,9.225325,2.912296,6.364385,2.882322,0.494793,4.935376,-1.644990,2.310361,7.363278,-9.865773,0.699720,1.133586,-0.507374,8.169319,5.520252,-1.711749,6.255803,1.764279,-4.648876,-6.133822,8.391841,-4.709190,-7.861368,4.224839,0.800053,6.428869,6.214169,-6.415690,5.512723,-2.488571,2.043493,2.639783,-0.176956,2.645496,-4.320757,-6.029247,9.075014,4.019058,-2.719593,2.889003,-0.592292,-2.954916,-1.951860,8.228369,-8.510098,-1.737438,-4.994356,-6.514422,-3.444949,4.312308,-6.299402,-8.427802,7.111747,4.193516,-9.877966,8.764334,1.729904,-3.190705,-5.156764,0.981181,9.019039,5.646584,-5.973061,-0.138665,0.105414,5.891816,3.187823,-4.890818,6.911050,7.174678,-3.655437,-6.265019,-9.620335,6.907656,3.022690,-9.823355,9.305007,-5.740566,6.131425,-9.519093,7.657082,-3.316848,-3.527653,3.343523,-4.276445,1.540883,7.943485,-9.537445,3.875278,4.575936,7.683206,7.698953,3.559387,-3.859819,0.741427,5.865272,-6.000594,9.747692,-5.236648,-5.834688,4.306202,-0.965454,4.247961,9.707217,-6.763697,3.078880,-8.042705,-6.199028,6.990311], dtype = "float32")#candidate|6337|(936,)|const|float32
call_6336 = relay.TupleGetItem(func_2179_call(relay.reshape(const_6337.astype('float32'), [13, 9, 8])), 0)
call_6338 = relay.TupleGetItem(func_2182_call(relay.reshape(const_6337.astype('float32'), [13, 9, 8])), 0)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_6362 = relay.TupleGetItem(func_1692_call(), 0)
call_6363 = relay.TupleGetItem(func_1693_call(), 0)
var_6368 = relay.var("var_6368", dtype = "bool", shape = (13, 9, 10))#candidate|6368|(13, 9, 10)|var|bool
bop_6369 = relay.floor_divide(bop_6322.astype('float64'), relay.reshape(var_6368.astype('float64'), relay.shape_of(bop_6322))) # shape=(13, 9, 10)
bop_6372 = relay.floor_divide(bop_6325.astype('float64'), relay.reshape(var_6368.astype('float64'), relay.shape_of(bop_6325))) # shape=(13, 9, 10)
output = relay.Tuple([call_6336,const_6337,call_6362,bop_6369,])
output2 = relay.Tuple([call_6338,const_6337,call_6363,bop_6372,])
func_6377 = relay.Function([var_6368,], output)
mod['func_6377'] = func_6377
mod = relay.transform.InferType()(mod)
var_6378 = relay.var("var_6378", dtype = "bool", shape = (13, 9, 10))#candidate|6378|(13, 9, 10)|var|bool
output = func_6377(var_6378)
func_6379 = relay.Function([var_6378], output)
mutated_mod['func_6379'] = func_6379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2389_call = mod.get_global_var('func_2389')
func_2391_call = mutated_mod.get_global_var('func_2391')
call_6416 = relay.TupleGetItem(func_2389_call(), 0)
call_6417 = relay.TupleGetItem(func_2391_call(), 0)
output = call_6416
output2 = call_6417
func_6418 = relay.Function([], output)
mod['func_6418'] = func_6418
mod = relay.transform.InferType()(mod)
mutated_mod['func_6418'] = func_6418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6418_call = mutated_mod.get_global_var('func_6418')
call_6419 = func_6418_call()
output = call_6419
func_6420 = relay.Function([], output)
mutated_mod['func_6420'] = func_6420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4133_call = mod.get_global_var('func_4133')
func_4134_call = mutated_mod.get_global_var('func_4134')
call_6450 = relay.TupleGetItem(func_4133_call(), 0)
call_6451 = relay.TupleGetItem(func_4134_call(), 0)
const_6461 = relay.const([-9.058493,3.133780,-0.737837,7.614154,-7.698732,-9.111487,-4.558282,8.073993,-2.518622,-5.844442,-3.083037,7.886074,-7.247226,3.932658,-4.773837,-6.079887,5.246923,3.359530,-0.914619,1.200928,2.161553,-9.225884,7.059173,1.055317,-7.849597,3.206982,2.292993,3.635640,-9.641225,-8.990849,3.768215,3.514191,-0.707003,-3.977615,-8.825537,-8.405150,-8.320061,1.707796,-8.266632,1.100105,4.957868,2.037943,4.701537,-3.450144,5.508376,-7.265911,1.267307,-2.042444,-7.036711,-0.185555,-6.998732,-4.948999,6.491982,-1.017741,-8.014471,-5.700741,1.018457,2.209491,-6.100256,-9.844549,-1.510677,-6.152362,3.391741,-0.084660,-9.005330,-2.622728,4.413283,6.108932,-3.158430,-9.864632,8.130607,-6.769644,6.270031,4.098352,-5.680840,6.904002,-5.261750,-7.225252,-9.746821,4.817083,-4.081378,-5.708833,-1.839880,-9.115042,6.844396,-4.656136,-7.073976,4.235785,-2.816249,3.143441,9.675404,3.949229,3.556767,4.723250,-6.677509,-7.051399,-5.071141,-0.217808,-4.408645,7.231979,-0.351477,-3.314466,8.387544,-4.956698,-9.824942,-4.155446,-2.005518,0.107019,1.585919,-7.724589,6.901421,-6.381549,8.637837,-7.544903,-5.190114,7.728196,4.354882,2.600470,-0.297490,-6.367738,5.405175,-6.207317,8.739848,0.180473,-9.097777,-2.008575,-7.393656,2.964392,-6.187512,2.162621,7.627636,8.542442,-2.612965,0.189064,-0.697196,4.673590,-3.954019,7.097292,0.163980,9.334198,-9.753138,0.269077,-1.829978,-7.526693,6.504766,8.884618,2.781845,9.871359,5.379477,-1.517329,1.033477,-8.780733,4.645673,6.977036,-2.752107,-1.035639,-4.833276,-9.289313,-2.601946,6.545009,-8.674303,-4.320897,6.785724,-2.636522,7.668342,-7.601326,-6.450076,-4.339869,7.562526,9.662833,-1.448176,-1.830757,5.065811,-3.775206,-3.392224,9.953756,-0.333435,-8.766777,-6.860673,4.133062,4.093413,-5.010915,-9.401889,2.874302,-6.362730,2.142553,-8.381005,7.821222,-2.264841,6.409493,-8.488714,-1.361362,-6.199093,-5.079589,9.032648,-3.894142,-6.005028,-2.806153,-0.473023,-0.378465,-8.161782,6.226413,2.329346,1.864324,-2.766941,-1.334893,9.653154,-1.140534,0.558981,-6.854178,-5.328888,6.535846,1.249117,4.030982,0.463760,-7.459686,6.893354,-6.428532,6.503892,7.152944,-8.085398,-0.120804,-5.235017,-0.875157,5.299671,-7.081594,2.815117,-6.122142,3.537126,-4.015696,3.924299,8.306173,9.895451,-9.391683,7.947641,-3.489821,8.173940,4.968188,8.601329,-6.892746,8.759846,-3.876787,-8.098511,7.691272,-6.106292,1.298735,8.425432,0.029895,-2.234844,9.299259,5.507073,-2.761968,-6.325297,-6.941823,8.013941,-3.020058,2.474016,6.019960,-3.298794,6.004864,7.262894,-4.709349,2.769967,2.351479,8.098749,0.305096,-0.302440,-1.086545,-1.427321,5.398804,7.259583,-7.438559,-3.427868,-0.189704,-5.016577,-1.454448,-8.769265,-7.957011,-2.496775,-7.389829,-5.611969,-4.426626,4.793347,0.562272,5.279284,5.925833,8.543972,3.287714,1.987086,-7.003914,0.599355,0.144448,4.843980,-6.615930,7.424207,-7.008521,-0.136815,7.178706,8.151066,9.240605,7.812673,3.336819,-0.304984,-5.320234,-9.025946,-6.175536,1.930490,-0.561384,8.671085,-7.319918,3.420794,8.750174,1.603844,3.392197,0.449842,7.035604,5.203761,7.658091,5.196185,4.889571,-7.989728,-8.300528,-4.104208,7.324005,7.144213,-4.064498,-4.998715,-8.704625,-5.211867,-0.759423,4.179396,-1.103674,-4.977428,-8.973353,-5.024166,0.314309,7.110503,-7.322417,-2.694623,-0.624600,-0.041789,-0.156376,-4.419444,-7.841867,-4.193127,-7.097823,6.534976,-9.466800,9.753727,7.599120,6.529259,-3.931842,-2.958771,-6.367958,-0.313020,-2.341301,8.305901,2.986644,-9.662642,6.439601,-0.630637,-4.866059,-4.966316,3.419524,2.023557,5.128875,-1.688192,-5.127747,1.425021,8.455495,9.068996,-4.438651,0.038627,-5.479971,4.053490,-2.000784,1.469025,1.629225,-6.882217,8.097449,-7.478457,-3.328669,8.652877,2.481601,9.820073,-5.681114,2.246873,3.919768,0.663848,-5.821773,4.429610,-2.967363,4.065601,2.346780,2.426668,0.152626,6.309893,-7.965212,-4.612283,7.619026,-2.830504,-2.012255,-8.570527,-7.313467,9.176861,7.449024,-1.579221,-3.779705,9.362757,3.239071,-8.735094,-2.903098,-2.797018,-0.882435,7.917729,-1.750787,-5.196410,3.973283,-3.152437,-5.550165,-3.162822,1.357694,5.526271,-6.356145,6.383393,0.032559,-0.731658,5.227500,-2.678414,-2.368349,-3.897219,-1.996176,5.759903,9.146583,0.699226,-8.736425,8.723694,-1.667073,6.431853,-5.146993,-7.595145,-1.441465,5.453630,4.036218,-4.239654,3.140491,-9.820096,5.559101,1.291205,-5.353454,-5.581785,-0.685157,-4.374389,-2.563205,0.612875,-4.115753,2.074252,0.021605,-5.513558,-8.209972,-4.071839,0.565859,4.959560,-3.121448,-2.016499,-5.210452,7.309083,-3.765962,3.304423,2.339483,1.689167,5.058582,6.696150,-8.443109,1.334470,-7.387996,-6.731914,8.413046,-0.305364,4.854454,-8.527901,2.329762,-8.734795,3.690732,-7.580187,3.021963,-0.299842,-9.611681,2.964551,8.477094,-2.790718,-0.261496,-0.337271,-1.390339,9.490917,7.540816,6.498996,-0.549770,-7.439132,-8.231148,-3.164879,5.672624,-1.895177,-1.133194,-4.045515,-5.657498,8.540011,6.881728,-4.227484,-2.149515,3.367322,1.812359,-4.558658,8.513950,8.749016,-8.275944,6.536809,-8.026531,0.253680,3.259308,0.326811,-6.376029,-4.391973,-5.312648,-3.823402,-8.723297,-1.085909,-7.428566,0.739981,4.648347,1.498604,9.166626,6.220462,-4.356461,-0.229269,-8.386395,-1.670634,3.711453,3.026148,3.467770,-2.820880,1.933221,-5.472378,-8.300217,4.539271,-7.792673,8.898265,7.257755,-5.952267,8.799126,1.744555,-9.991928,2.794076,-9.606935,4.388720,-5.693994,-5.687836,-8.710533,0.554152,-9.219371,-6.004032,-7.806834,-4.381120,0.864463,2.353580,-2.395139,-3.629555,-1.163216,-9.622402,-8.032592,6.855070,9.182216,7.834790,-8.103091,-0.178932,2.918649,9.875352,-2.858365,-4.665277,-2.445835,3.753431,-6.085988,0.101331,2.970615,-8.243002,1.412593,-7.517331,3.625569,-0.947678,-2.577055,-4.478961,-2.943668,1.784462,-0.073005,-6.567320,-7.572049,3.637216,0.550582,3.750452,-5.330449,9.655166,6.911826,-1.212797,4.280628,-8.692354,-1.407062,4.067961,0.556323,2.827901,-1.623174,-4.745538,4.920147,-6.091391,3.280371,0.977209,5.784575,6.414739,-4.519765,7.225938,2.317242,-6.462776,-2.326147,-4.348317,-9.409972,0.550695,8.521610,2.583919,0.768444,5.918593,-4.633486,-6.767223,1.848558,-3.258230,-8.657805,3.576868,-1.237372,1.717300,-8.259097,-7.900930,9.965661,9.809063,9.602110,-4.516023,-9.420756,2.532340,-1.094210,-6.863782,-9.442906,-8.444233,-8.493216,-5.642090,2.797288,-6.074906,1.119253,-9.261512,-0.586044,6.309224,8.778146,6.621157,6.446872,-3.464966,-1.524932,-2.971637,9.643011,1.223693,-0.558224,-5.559735,1.685492,1.109886,3.467719,-2.780360,-1.107150,-0.443455,7.102765,6.950919,-1.565884,-4.305886,9.889204,5.753411,2.194103,-4.361634,-2.716183,0.086808,7.114465,-8.409308,4.051697,6.812503,-0.843053,3.510737,3.375882,4.051803,-3.030548,-7.845618,-2.334999,-4.806580,6.185444,5.461124,-3.080323,9.977528,-2.748274,-9.835612,-0.031170,6.992328,2.306610,-7.742502,7.560766,5.590819,-5.631617,3.866871,4.163526,-6.941196,1.318375,5.219611,4.612399,5.278584,-3.458597,4.876455,2.673980,-7.940191,4.330822,1.634954,-3.065930,-5.628106,1.582597,1.593603,2.725925,7.131038,7.186999,-4.624150,5.727863,-9.878453,-2.825396,6.691602,-4.729174,-7.880002,-7.366876,2.450110,-6.373668,8.067788,8.949414,7.698209,3.586978,4.377957,4.736584,8.801624,-6.071412,-1.900409,5.235781,-9.760032,8.219230,3.558642,0.959311,-1.982407,-5.110456,9.645772,-1.656355,-0.144209,5.452772,1.708982,-6.499679,6.097900,-8.394128,1.366384,4.298885,-3.553553,-4.022406,3.831102,-7.464055,-2.751627,7.436086,-8.201802,-8.164953,6.476935,6.945608,-3.032098,1.133078,-6.647436,3.169253,5.255227,7.018016,-8.867869,4.279632,9.394970,1.271440,-9.901200,2.244032,5.275835,-2.056042,9.021367,1.004838,5.187700,-2.901752,-9.480690,1.257306,-8.377236,7.409420,-6.039689,-5.487816,-7.225234,5.830718,9.720182,-1.821429,-6.037689,7.140934,-7.887123,7.000258,-8.679084,3.408945,-6.454517,-8.071095,3.279953,2.345763,0.785573,-3.467563,9.122406,-6.950999,-7.832401,2.378875,0.131395,2.695940,1.620726,8.788287,-4.320205,9.606244,0.355901,7.325147,4.809903,1.688768,5.986864,5.677733,9.358009,8.611770,-7.419269,6.022753,5.979923,3.273506,3.701081,-6.189689,0.241407,-7.715004,-7.411209,1.298415,-2.336658,-5.374512,-1.053621,0.613387,5.338881,-4.377952,8.517225,-7.720314,-9.348584,-3.479949,-9.263337,0.190475,-7.822663,7.233113,8.476030,-4.022196,9.785249,6.294470,-9.027641,4.923229,4.091084,5.313084,0.770413,-7.635021,6.093141,-9.473472,2.415718,6.551964,3.751129,-5.033509,-9.630928,9.422414,1.338670,4.390686,0.509523,-0.458836,-2.753705,5.325241,0.827902,3.608563,-4.544377,-4.590622,9.940144,3.925964,-3.723692,-9.582625,5.813285,-8.856177,-7.042823,-0.473961,4.965799,7.082844,1.509875,3.039133,-3.348094,5.885648,-3.232967,-0.231670,-6.726479,1.873870,-1.436058,2.505634,3.510463,-9.518079,9.151100,0.732904,6.481765,6.379693,5.019670,9.280247,4.598175,2.739883,2.093938,-4.235186,1.218054,-1.398411,6.782493,6.484864,-4.964615,-0.589132,6.841665,-7.244351,-3.099111,4.294107,-1.199127,8.952781,5.127640,-3.937717,6.460182,-6.827765,-9.760325,-1.156602,-3.614705,-9.991040,4.662974,9.199578,-8.973178,-7.706231,6.418951,-1.705977,-3.925861,1.686730,-6.722704,-1.542251,-2.359266,1.571006,-5.784669,-6.160105,5.754151,3.674214,-4.330008,6.368121,-6.303265,1.981978,4.125852,1.372442,-0.197154,-2.274251,-4.949039,-3.552489,7.310423,5.549682,0.339387,7.534647,-4.889036,1.577250,9.932765,8.392549,-0.343813,3.826189,0.813722,-6.528001,9.571127,-1.540323,8.392200,1.055538,-5.496288,-0.007040,-2.428960,3.844734,-1.033923,8.609278,0.840863,9.626915,-1.290511,-1.375170,-5.740026,3.579882,6.559038,3.707455,-5.942047,4.260148,-3.003311,-5.630694,7.686730,1.884409,-6.162762,5.379272,-1.152011,-3.436241,0.799082,-3.662492,0.191125,-5.526794,7.595209,8.004893,-9.122360,6.156444,7.061757,6.533287,8.942002,-7.944166,-8.904202,6.698414,0.344509,6.851634,-5.187713,-2.541703,2.660093,-3.755710,-9.112474,-7.580597,6.316066,3.151272,0.366536,1.129240,-6.837722,-9.555275,-1.250516,3.071376,3.864837,-2.637856,-0.380668,1.722409,8.792188,-9.347538,-7.235223,-3.265895,-2.166460,-4.777618,7.003572,-9.656097,6.470551,-7.120314,4.767831,5.069100,-8.083165,-7.128860,-0.361002,-4.716963,-0.699410], dtype = "float32")#candidate|6461|(1053,)|const|float32
bop_6462 = relay.bitwise_or(call_6450.astype('int16'), relay.reshape(const_6461.astype('int16'), relay.shape_of(call_6450))) # shape=(1053,)
bop_6465 = relay.bitwise_or(call_6451.astype('int16'), relay.reshape(const_6461.astype('int16'), relay.shape_of(call_6451))) # shape=(1053,)
var_6477 = relay.var("var_6477", dtype = "int16", shape = (1053,))#candidate|6477|(1053,)|var|int16
bop_6478 = relay.equal(bop_6462.astype('bool'), relay.reshape(var_6477.astype('bool'), relay.shape_of(bop_6462))) # shape=(1053,)
bop_6481 = relay.equal(bop_6465.astype('bool'), relay.reshape(var_6477.astype('bool'), relay.shape_of(bop_6465))) # shape=(1053,)
func_5795_call = mod.get_global_var('func_5795')
func_5797_call = mutated_mod.get_global_var('func_5797')
call_6482 = relay.TupleGetItem(func_5795_call(), 0)
call_6483 = relay.TupleGetItem(func_5797_call(), 0)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_6498 = relay.TupleGetItem(func_1692_call(), 0)
call_6499 = relay.TupleGetItem(func_1693_call(), 0)
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_6504 = relay.TupleGetItem(func_2626_call(), 0)
call_6505 = relay.TupleGetItem(func_2627_call(), 0)
func_6304_call = mod.get_global_var('func_6304')
func_6305_call = mutated_mod.get_global_var('func_6305')
call_6509 = func_6304_call()
call_6510 = func_6304_call()
func_631_call = mod.get_global_var('func_631')
func_632_call = mutated_mod.get_global_var('func_632')
call_6515 = relay.TupleGetItem(func_631_call(), 1)
call_6516 = relay.TupleGetItem(func_632_call(), 1)
output = relay.Tuple([bop_6478,call_6482,call_6498,call_6504,call_6509,call_6515,])
output2 = relay.Tuple([bop_6481,call_6483,call_6499,call_6505,call_6510,call_6516,])
func_6530 = relay.Function([var_6477,], output)
mod['func_6530'] = func_6530
mod = relay.transform.InferType()(mod)
mutated_mod['func_6530'] = func_6530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6531 = relay.var("var_6531", dtype = "int16", shape = (1053,))#candidate|6531|(1053,)|var|int16
func_6530_call = mutated_mod.get_global_var('func_6530')
call_6532 = func_6530_call(var_6531)
output = call_6532
func_6533 = relay.Function([var_6531], output)
mutated_mod['func_6533'] = func_6533
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6553 = relay.var("var_6553", dtype = "int64", shape = (14, 13, 11))#candidate|6553|(14, 13, 11)|var|int64
var_6554 = relay.var("var_6554", dtype = "int64", shape = (14, 13, 11))#candidate|6554|(14, 13, 11)|var|int64
bop_6555 = relay.bitwise_xor(var_6553.astype('int64'), relay.reshape(var_6554.astype('int64'), relay.shape_of(var_6553))) # shape=(14, 13, 11)
output = bop_6555
output2 = bop_6555
func_6559 = relay.Function([var_6553,var_6554,], output)
mod['func_6559'] = func_6559
mod = relay.transform.InferType()(mod)
mutated_mod['func_6559'] = func_6559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6559_call = mutated_mod.get_global_var('func_6559')
var_6561 = relay.var("var_6561", dtype = "int64", shape = (14, 13, 11))#candidate|6561|(14, 13, 11)|var|int64
var_6562 = relay.var("var_6562", dtype = "int64", shape = (14, 13, 11))#candidate|6562|(14, 13, 11)|var|int64
call_6560 = func_6559_call(var_6561,var_6562,)
output = call_6560
func_6563 = relay.Function([var_6561,var_6562,], output)
mutated_mod['func_6563'] = func_6563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_6565 = relay.TupleGetItem(func_155_call(), 0)
call_6566 = relay.TupleGetItem(func_156_call(), 0)
var_6598 = relay.var("var_6598", dtype = "float32", shape = (13, 9, 9))#candidate|6598|(13, 9, 9)|var|float32
bop_6599 = relay.left_shift(call_6565.astype('uint8'), var_6598.astype('uint8')) # shape=(13, 9, 9)
bop_6602 = relay.left_shift(call_6566.astype('uint8'), var_6598.astype('uint8')) # shape=(13, 9, 9)
output = bop_6599
output2 = bop_6602
func_6606 = relay.Function([var_6598,], output)
mod['func_6606'] = func_6606
mod = relay.transform.InferType()(mod)
var_6607 = relay.var("var_6607", dtype = "float32", shape = (13, 9, 9))#candidate|6607|(13, 9, 9)|var|float32
output = func_6606(var_6607)
func_6608 = relay.Function([var_6607], output)
mutated_mod['func_6608'] = func_6608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2527_call = mod.get_global_var('func_2527')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_6627 = relay.TupleGetItem(func_2527_call(), 1)
call_6628 = relay.TupleGetItem(func_2528_call(), 1)
output = relay.Tuple([call_6627,])
output2 = relay.Tuple([call_6628,])
func_6642 = relay.Function([], output)
mod['func_6642'] = func_6642
mod = relay.transform.InferType()(mod)
output = func_6642()
func_6643 = relay.Function([], output)
mutated_mod['func_6643'] = func_6643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_6656 = func_3036_call()
call_6657 = func_3036_call()
output = call_6656
output2 = call_6657
func_6658 = relay.Function([], output)
mod['func_6658'] = func_6658
mod = relay.transform.InferType()(mod)
output = func_6658()
func_6659 = relay.Function([], output)
mutated_mod['func_6659'] = func_6659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4078_call = mod.get_global_var('func_4078')
func_4080_call = mutated_mod.get_global_var('func_4080')
call_6671 = func_4078_call()
call_6672 = func_4078_call()
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_6681 = relay.TupleGetItem(func_76_call(), 3)
call_6682 = relay.TupleGetItem(func_77_call(), 3)
func_1830_call = mod.get_global_var('func_1830')
func_1832_call = mutated_mod.get_global_var('func_1832')
var_6693 = relay.var("var_6693", dtype = "float64", shape = (96,))#candidate|6693|(96,)|var|float64
call_6692 = relay.TupleGetItem(func_1830_call(relay.reshape(var_6693.astype('float64'), [8, 1, 12])), 0)
call_6694 = relay.TupleGetItem(func_1832_call(relay.reshape(var_6693.astype('float64'), [8, 1, 12])), 0)
output = relay.Tuple([call_6671,call_6681,call_6692,var_6693,])
output2 = relay.Tuple([call_6672,call_6682,call_6694,var_6693,])
func_6697 = relay.Function([var_6693,], output)
mod['func_6697'] = func_6697
mod = relay.transform.InferType()(mod)
mutated_mod['func_6697'] = func_6697
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6698 = relay.var("var_6698", dtype = "float64", shape = (96,))#candidate|6698|(96,)|var|float64
func_6697_call = mutated_mod.get_global_var('func_6697')
call_6699 = func_6697_call(var_6698)
output = call_6699
func_6700 = relay.Function([var_6698], output)
mutated_mod['func_6700'] = func_6700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1614_call = mod.get_global_var('func_1614')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_6728 = func_1614_call()
call_6729 = func_1614_call()
output = relay.Tuple([call_6728,])
output2 = relay.Tuple([call_6729,])
func_6764 = relay.Function([], output)
mod['func_6764'] = func_6764
mod = relay.transform.InferType()(mod)
output = func_6764()
func_6765 = relay.Function([], output)
mutated_mod['func_6765'] = func_6765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2643_call = mod.get_global_var('func_2643')
func_2644_call = mutated_mod.get_global_var('func_2644')
call_6776 = relay.TupleGetItem(func_2643_call(), 1)
call_6777 = relay.TupleGetItem(func_2644_call(), 1)
func_5795_call = mod.get_global_var('func_5795')
func_5797_call = mutated_mod.get_global_var('func_5797')
call_6790 = relay.TupleGetItem(func_5795_call(), 0)
call_6791 = relay.TupleGetItem(func_5797_call(), 0)
bop_6799 = relay.bitwise_xor(call_6776.astype('uint64'), relay.reshape(call_6790.astype('uint64'), relay.shape_of(call_6776))) # shape=(13, 9, 1)
bop_6802 = relay.bitwise_xor(call_6777.astype('uint64'), relay.reshape(call_6791.astype('uint64'), relay.shape_of(call_6777))) # shape=(13, 9, 1)
func_4514_call = mod.get_global_var('func_4514')
func_4517_call = mutated_mod.get_global_var('func_4517')
var_6847 = relay.var("var_6847", dtype = "int8", shape = (10, 144))#candidate|6847|(10, 144)|var|int8
var_6848 = relay.var("var_6848", dtype = "float32", shape = (15, 117))#candidate|6848|(15, 117)|var|float32
call_6846 = relay.TupleGetItem(func_4514_call(relay.reshape(var_6847.astype('int8'), [1440,]), relay.reshape(var_6848.astype('float32'), [1755,]), ), 3)
call_6849 = relay.TupleGetItem(func_4517_call(relay.reshape(var_6847.astype('int8'), [1440,]), relay.reshape(var_6848.astype('float32'), [1755,]), ), 3)
var_6866 = relay.var("var_6866", dtype = "int8", shape = (10, 144))#candidate|6866|(10, 144)|var|int8
bop_6867 = relay.subtract(var_6847.astype('uint16'), relay.reshape(var_6866.astype('uint16'), relay.shape_of(var_6847))) # shape=(10, 144)
func_2127_call = mod.get_global_var('func_2127')
func_2131_call = mutated_mod.get_global_var('func_2131')
const_6871 = relay.const([5,-10,4,4,-1,-7,3,-3,-1,-4,-1,3,5,6,-6,-2,-6,-7,-6,-2,-4,-6,-3,9,4,-6,-6,-8,-7,-9,-7,3,-5,-6,1,-8,6,-2,-2,4,4,-3,-1,1,5,-10,-3,8,7,-1,-3,-5,-2,8,6,2,-6,-2,7,-4,5,7,-10,10,-2,-6,-7,-3,-8,4,5,-5,4,7,-3,6,-6,8,1,-3,-8,-7,2,3,-1,3,7,-6,-5,2,3,-6,2,-4,3,-3,10,5,10,-1,6,-4,2,-4,2,-5,-4,5,-6,-9,8,-9,2,2,3,-2,7,-4,7,-6,-5,-5,1,-5,8,-7,5,-7,-1,10,2,4,9,6,7,-6,-2,-3,2,-1,1,-9,5,7,4,-1,1,-4,5,-10,-4,7,9,3,8,-2,-4,-9,-6,7,6,-6,7,-9,2,7,6,-5,3,-6,2,10,-10,6,-5,-6,3,8,-2,2,-6,1,2,9,-6,4,5,-3,-5,1,-2,-9,-6,4,-3,3,3,3,2,1,-9,5,3,10,-6,5,7,2,-2,3,-3,9,10,3,4,-7,1,10,9,1,1,5,4,3,-6,-3,3,-4,4,5,3,2,6,-9,1,2,6,2,-9,-5,-1,3,-10,9,6,3,-9,-3,-4,2,2,7,-3,9,-4,-4,-3,-3,6,9,7,1,-7,-1,-9,-6,6,9,4,1,2,-7,4,2,-1,2,-4,-5,9,2,8,-9,5,6,-7,9,4,-6,7,10,8,-7,-7,1,-8,-6,-3,1,-4,-7,-3,10,-4,8,4,-9,-10,-5,9,-6,1,3,6,1,-10,1,-7,-1,-7,4,4,4,-2,-4,-6,-9,-2,-4,6,-10,-6,-10,-2,-5,9,-10,5,-1,-4,-1,5,1,2,-8,1,-5,-9,-3,7,1,9,8,-9,2,-6,-6,-3,-10,4,-3,6,-3,4,-7,4,-4,-3,-9,-3,-6,4,-10,10,-9,-8,1,-2,-10,-2,7,8,1,6,-2,10,10,9,-10,9,-5,-4,2,3,-2,2,-3,1,-10,5,-7,-9,9,-6,10,10,4,-4,-10,10,-1,3,3,-9,2,6,-7,8,-6,6,-10,1,-10,2,-3,-4,-7,10,1,-4,1,4,-8,5,7,-9,-10,2,-7,-8,9,5,-8,-5,-2,2,2,3,-6,-1,2,9,2,1,-6,-2,-2,-10,-1,9,-5,-9,5,-6,-10,6,-8,-5,-8,2,7,10,10,-8,-4,-4,-8,-7,-5,-5,-1,1,6,2,2,10,7,-9,-8,7,3,-5,4,-3,-7,6,-9,-7,-2,-1,-2,-4,-10,5,-9,2,-4,3,10,-9,-4,3,9,-2,-9,-5,-5,8,-1,3,-5,-4,-3,9,2,-8,-2,-4,1,1,-1,10,5,-9,-1,10,9,-9,10,-6,5,-1,-7,7,10,-9,-4,7,5,8,10,5,2,4,1,4,-5,4,-1,1,1,-2,-7,4,5,-1,2,6,2,-3,3,-3,-4,10,10,-7,-1,5,8,-3,3,-9,2,6,7,-6,-9,-9,-6,8,-2,6,-2,3,-2,2,-2,8,-6,5,6,-6,-10,7,5,3,-10,3,2,3,-4,-7,6,10,2,7,-9,-2,-7,-5,6,-2,-9,-10,2,-2,8,5,-7,-8,-2,-6,8,-10,-6,-9,-4,-1,-5,1,4,-6,-5,8,7,10,1,-8,1,-5,-4,-1,3,-9,-3,-8,8,-9,4,-4,1,10,-7,10,6,-8,10,-7,1,3,-10,9,4,10,5,-1,-7,8,-9,3,4,6,-1,6,10,-8,-10,-8,-6,4,-2,8,6,-3,-4,10,8,-3,8,-4,1,-1,-8,-7,7,4,8,9,7,1,-8,1,-7,-8,-4,-5,2,-5,-5,5,-6,3,2,-8,-4,2,1,10,8,5,10,-8,-6,-3,7,-4,8,7,-1,-10,-5,9,-6,4,-8,-7,-8,3,7,-4,-5,-7,8,-6,8,-4,-6,9,-5,-5,3,-3,6,5,-1,10,-9,-2,1,-6,4,4,-4,-2,-7,3,-1,-10,-2,2,4,-1,9,10,3,-10,7,-7,-6,-1,7,4,-8,-7,-9,-6,-3,8,2,3,-3,10,-7,-2,-5,-10,4,-4,-6,5,-2,-8,7,6,-3,5,-1,7,-2,-5,-9,3,6,-10,-8,8,5,2,2,-1,6,3,1,-9,9,1,-8,-5,-10,9,-7,8,4,4,-10,3,3,5,-5,8,-10,-4,-3,-5,2,-3,-10,3,-10,10,-5,8,-8,-1,-9,9,-8,-8,-1,-4,-6,6,-7,-7,-7,9,-7,-10,-9,-10,-2,8,3,2,10,9,-4,-9,5,2,-3,5,-9,7,-8,8,5,3,-3,-1,1,-8,-6,-6,5,4,8,-7,6,4,-10,-5,8,2,3,6,-7,6,3,6,-9,-3,-2,3,4,-2,-10,1,7,3,9,1,-6,-9,1,5,8,9,10,-7,-1,-1,8,-1,5,4,-5,-10,-5,8,-8,8,-2,-5,-10,9,1,-4,-9,-3,-1,10,3,-5,-3,-4,7,-5,10,-3,2,2,9,-10,1,5,-2,7,7,4,6,-8,-2,2,-5,-2,5,10,-10,-4,-4,2,-6,-1,-1,-2,3,-8,5,6,-6,-8,-2,7,-7,-2,2,8,3,2,4,-10,5,3,9,1,10,6,-6,-4,4,5,-10,-3,-2,-6,8,-5,-4,-5,8,10,-5,-9,-1,-5,7,-10,-3,-9,-7,-3,-10,10,-5,-9,-10,2,-7,-6,2,-3,1,7,6,1,2,10,2,-6,-6,-3,-7,-2,6,3,9,-8,-9,6,-2,1,-3,-5,-3,-4,-7,-5,-2,9,5,5,-7,-6,-1,-4,-3,6,-7,3,-4,-9,5,-5,9,6,-5,-9,5,3,-2,-8,1,1,7,-8,-2,-1,-8,-6,2,2,5,4,-9,-6,3,5,10,-9,-9,-9,3,10,10,-10,-9,2,4,-4,2,-3,3,-6,-4,-3,4,-6,4,8,-3,8,1,-6,5,-7,9,9,-9,-9,2,6,4,4,-7,3,3,3,-1,-8,-10,-3,-6,-3,9,-8,3,-8,-5,6,7,3,3,3,-7,-10,5,-6,-8,-5,-2,-8,6,-2,2,-4,-9,10,-5,8,1,8,3,-8,4,8,6,-1,-3,3,2,6,-4,-5,-7,-8,-3,6,-2,-7,-8,4,-10,-4,9,10,-5,-5,3,6,5,2,-2,-3,3,-3,-6,4,-4,-1,-8,-6,-9,1,-3,4,3,-7,4,-9,4,9,1,-6,-4,7,7,-6,-6,-8,4,-8,-8,1,-7,-1,4,-10,3,-9,-10,10,2,4,3,-7,-4,1,2,-5,2,-9,-6,-3,-3,-8,1,-2,4,-10,-10,3,4,7,7,4,-6,8,-1,10,5,1,-8,10,-9,-10,-7,-2,-6,-6,10,2,2,9,3,9,9,-4,1,10,4,10,10,4,-2,1,-10,-10,-5,4,-2,5,-3,8,-5,-5,-8,-2,-6,4,-7,-1,-10,-7,-2,2,-6,-5,8,-2,-4,1,9,-8,-10,-4,-9,-5,-6,3,-5,-9,-4,9,-10,4,-5,3,10,10,8,-8,9,-8,-6,-2,-8,4,-7,-3,-2,-8,3,1,-7,-3,7,1,-5,-10,2,3,-4,9,10,6,-8,-6,-10,-4,2,-9,9,4,1,-8,-5,-2,-10,10,-4,9,-3,-4,-6,9,6,-6,9,2,3,4,10,6,-8,9,5,5,5,-2,-8,8,8,-10,1,7,-9,-1,-7,-9,5,9,6,-9,-3,-3,-1,-4,6,-4,-5,2,-1,5,1,-7,3,-10,9,-1,2,3,8,2,3,-10,8,4,-6,1,2,6,1,-6,5,5,3,1,-7,-5,1,-1,-9,2,2,3,-1,-1,6,5,7,1,7,-3,-6,-7,4,-10,2,8,-5,-2,-3,1,10,-3,5,7,5,-10,-8,10,4,-7,-3,-2,10,-7,7,-2,-3,6,-6,-3,4,-4,10,-6,-5,5,-10,6,-3,10,-10,-8,5,4,8,-4,1,-5,-5,9,4,8,1,1,-9,-3,-3,-6,7,-2,9,7,8,-3,5,-1,-6,-2,-6,-2,-5,-6,9,1,-1,-1,10,2,-2,-1,9,-5,-2,3,-1,3,-3,6,-2,-8,-9,5,8,9,2,-6,-1,-5,7,3,4,-6,6,1,-9,2,7,-9,-3,-5,-6,6,-10,-2,-9,-7,-2,2,-4,-5,1,1,5,4,-6,-2,10,4,9,8,-3,-10,7,1,6,-2,-5,6,-3,-7,9,-3,-9,8,-5,5,1,-10,-1,8,1,4,-3,6,-3], dtype = "uint32")#candidate|6871|(1638,)|const|uint32
var_6872 = relay.var("var_6872", dtype = "float32", shape = (640,))#candidate|6872|(640,)|var|float32
call_6870 = relay.TupleGetItem(func_2127_call(relay.reshape(const_6871.astype('uint32'), [13, 9, 14]), relay.reshape(var_6872.astype('float32'), [640,]), ), 3)
call_6873 = relay.TupleGetItem(func_2131_call(relay.reshape(const_6871.astype('uint32'), [13, 9, 14]), relay.reshape(var_6872.astype('float32'), [640,]), ), 3)
func_3696_call = mod.get_global_var('func_3696')
func_3699_call = mutated_mod.get_global_var('func_3699')
call_6880 = relay.TupleGetItem(func_3696_call(relay.reshape(const_6871.astype('uint32'), [1638,])), 5)
call_6881 = relay.TupleGetItem(func_3699_call(relay.reshape(const_6871.astype('uint32'), [1638,])), 5)
func_2527_call = mod.get_global_var('func_2527')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_6884 = relay.TupleGetItem(func_2527_call(), 1)
call_6885 = relay.TupleGetItem(func_2528_call(), 1)
bop_6888 = relay.power(const_6871.astype('float64'), bop_6799.astype('float64')) # shape=(13, 9, 1638)
bop_6891 = relay.power(const_6871.astype('float64'), bop_6802.astype('float64')) # shape=(13, 9, 1638)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_6898 = func_1128_call()
call_6899 = func_1128_call()
output = relay.Tuple([call_6846,var_6848,bop_6867,call_6870,var_6872,call_6880,call_6884,bop_6888,call_6898,])
output2 = relay.Tuple([call_6849,var_6848,bop_6867,call_6873,var_6872,call_6881,call_6885,bop_6891,call_6899,])
func_6902 = relay.Function([var_6847,var_6848,var_6866,var_6872,], output)
mod['func_6902'] = func_6902
mod = relay.transform.InferType()(mod)
mutated_mod['func_6902'] = func_6902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6902_call = mutated_mod.get_global_var('func_6902')
var_6904 = relay.var("var_6904", dtype = "int8", shape = (10, 144))#candidate|6904|(10, 144)|var|int8
var_6905 = relay.var("var_6905", dtype = "float32", shape = (15, 117))#candidate|6905|(15, 117)|var|float32
var_6906 = relay.var("var_6906", dtype = "int8", shape = (10, 144))#candidate|6906|(10, 144)|var|int8
var_6907 = relay.var("var_6907", dtype = "float32", shape = (640,))#candidate|6907|(640,)|var|float32
call_6903 = func_6902_call(var_6904,var_6905,var_6906,var_6907,)
output = call_6903
func_6908 = relay.Function([var_6904,var_6905,var_6906,var_6907,], output)
mutated_mod['func_6908'] = func_6908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3433_call = mod.get_global_var('func_3433')
func_3434_call = mutated_mod.get_global_var('func_3434')
call_6995 = func_3433_call()
call_6996 = func_3433_call()
output = call_6995
output2 = call_6996
func_6999 = relay.Function([], output)
mod['func_6999'] = func_6999
mod = relay.transform.InferType()(mod)
output = func_6999()
func_7000 = relay.Function([], output)
mutated_mod['func_7000'] = func_7000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5640_call = mod.get_global_var('func_5640')
func_5642_call = mutated_mod.get_global_var('func_5642')
call_7004 = relay.TupleGetItem(func_5640_call(), 2)
call_7005 = relay.TupleGetItem(func_5642_call(), 2)
func_6559_call = mod.get_global_var('func_6559')
func_6563_call = mutated_mod.get_global_var('func_6563')
const_7036 = relay.const([[1,3,-3,10,7,1,-3,-1,-7,-7,1,-4,-10,-3,-9,9,-9,9,-3,4,-2,-3,-7,3,9,5,-10,5,2,-5,4,-2,-6,9,-9,1,-7,8,7,1,3,-7,7,-5,9,9,-3,8,-1,1,9,3,4,-9,-3,10,6,-1,1,-1,7,6,10,-3,3,1,6,8,-5,3,-7,6,-2,8,4,-6,7,2,7,8,-9,-10,3,5,6,6,2,-9,-8,2,4,2,9,1,-1,-6,10,-5,5,-10,7,4,-9,-8,10,8,7,9,6,-3,-1,-7,-4,-3,-2,10,3,3,-7,-9,-2,-2,9,-6,-1,3,-6,2,-5,-1,-8,-8,-4,-2,-3,-7,10,-3,-3,3,8,6,10,-5,1,-2,6,-1,-1,1,-6,9,10,-2,-1,-4,4,-2,-8,-7,-3,-9,1,9,-2,5,9,-1,-6,-1,-9,5,-7,-8,-3,1,6,-5,9,-8,-2,-9,9,-9,7,3,7,1,-4,-6,-4,5,8,-6,1,9,8,-6,10,-3,7,2,1,-7,-2,4,-3,-5,-8,-7,-4,-4,-6,1,-10,-4,-8,3,10,8,7,8,-10,1,4,7,-6,-2,5,-10,-8,4,-1,-9,8,-4,9,7,7,-9,7,2,-9,8,10,1,-4,-7,-1,-9,6,-6,-7,6,10,-8,-3,2,7,-8,-10,6,-3,3,1,-4,5,-2,4,10,-3,-3,-1,10,7,-6,6,-4,-6,2,-7,2,8,-6,-4,-8,-7,3,8,-5,-1,3,-2,4,-4,-5,5,-4,-3,-5,9,2,-4,3,10,8,-6,9,-8,5,-1,2,8,-9,6,-8,7,10,-6,-5,10,8,-4,5,-1,-5,-3,-8,-3,-1,-1,4,10,-9,-9,-5,-8,7,1,4,-4,-4,-8,-7,-9,9,-9,8,-1,6,-1,-8,-3,9,-7,-5,3,-8,-2,-1,-5,-1,-5,4,5,-5,10,-3,10,-6,-8,10,8,2,2,3,6,-2,2,-9,5,-3,-1,7,-10,-10,3,10,7,5,9,-7,-1,-8,-4,-2,-4,3,5,7,-4,-4,7,2,9,-3,3,-5,-8,7,-1,10,-6,-1,2,6,4,-3,-7,-5,2,7,8,10,-5,10,10,3,3,-6,-3,1,6,8,-10,-10,-3,-10,8,-8,10,1,10,-5,10,-9,8,2,-7,7,-5,2,5,8,-3,-8,-8,1,5,-2,9,-9,5,-1,2,-2,7,5,-5,5,3,10,-2,-9,1,3,-7,9,2,2,9,10,-7,8,-2,-1,8,-6,6,-9,-9,7,3,-5,5,10,3,-10,7,-6,10,-3,1,-1,5,2,-2,-9,2,-3,-3,-10,5,1,-7,2,-4,-8,-2,-2,10,-10,-4,9,-3,4,5,4,-4,-3,-2,8,10,1,-6,-1,-10,9,2,-9,-2,2,-6,9,-3,-3,-9,-1,9,-1,8,3,4,9,2,2,-2,3,-3,10,-7,3,5,5,7,-1,9,-2,-6,9,-8,3,-5,7,-3,6,-1,-7,2,-10,-7,3,-7,-9,5,-2,-8,2,-3,1,-8,-7,-3,-7,4,5,10,-9,2,-9,-5,9,-8,-7,4,7,3,2,6,-3,7,-6,-6,6,-3,5,8,1,9,-6,-6,-4,5,-4,-7,5,-5,-3,-4,-8,-3,-6,9,6,-7,-10,5,1,3,-5,4,-4,-9,-9,5,-1,-10,-3,6,8,4,-8,3,-1,7,-7,-3,2,-8,-6,-10,-5,-6,1,8,7,7,-10,-5,9,6,4,8,3,9,-1,10,9,-4,2,-2,-3,6,-1,4,-4,-7,2,-4,-3,8,-2,-2,6,5,-8,-7,-6,-4,-4,1,1,-4,-5,-9,3,-4,6,8,-2,8,-10,10,-7,-4,-3,7,-3,6,-1,-6,-2,1,-6,10,2,7,6,-7,-2,-4,-6,-8,5,-8,-10,-3,7,-2,3,-9,3,-8,-3,-2,7,-7,-8,-5,10,-1,10,-5,-8,-7,1,9,-4,-1,-3,2,-8,5,8,8,3,-10,-1,-7,-2,-1,4,4,-6,-7,-7,-9,9,-10,-5,-5,-8,-9,-10,10,-5,-4,3,-1,5,8,-8,-9,-4,-6,-7,-5,-7,-4,5,10,6,-2,-4,-10,10,2,-6,7,-8,-8,3,10,2,-7,-1,-8,3,-8,1,-7,-5,-9,10,2,8,-4,5,-2,-1,3,-8,-9,-1,9,4,-2,-4,1,-10,3,4,10,-3,-8,5,-6,-4,-5,3,-6,-9,7,1,9,-2,-9,2,-10,6,-1,1,4,-4,10,-3,6,5,7,-1,9,-1,-2,10,7,-9,-6,6,4,9,7,8,-5,-7,1,1,3,-8,6,-6,5,1,-4,1,7,1,3,-1,4,-1,6,-7,-5,-4,5,3,-5,-3,-1,6,6,6,-9,-8,-5,-10,-10,-1,-1,5,7,10,-2,9,-9,5,-2,-7,-8,-4,3,-5,10,-1,3,9,-3,9,1,-3,3,-10,-9,-6,3,1,3,-2,-3,1,8,-3,-8,10,-10,-2,1,10,10,-6,-3,10,4,-8,-4,1,1,-6,-8,-8,9,3,-1,-7,-8,-5,-1,-8,6,10,-5,5,6,-4,-6,-5,2,3,3,-8,5,4,8,-1,-8,-6,3,-8,1,-5,6,-3,10,-4,8,-5,-5,2,-1,-8,5,3,-7,9,4,-6,4,9,-7,-8,-4,9,4,-3,-4,5,6,9,8,1,2,10,-7,1,-3,9,5,-7,1,3,2,7,3,-1,-6,3,-10,-5,4,-10,-8,-4,-1,10,-4,9,1,4,-4,7,7,-5,4,3,7,-7,-4,-7,-4,7,10,-4,2,6,-2,3,4,-4,1,10,-3,-2,-8,4,-6,9,-8,8,10,-5,9,-2,7,3,5,5,-10,7,-6,9,-3,-9,-1,1,4,-6,4,-8,-3,-9,4,-8,-1,-2,7,10,-10,-1,9,-4,5,-6,7,-10,-4,-1,-2,-3,-4,-1,-4,9,3,7,-1,3,-1,5,-2,10,-5,-4,-10,2,-10,4,-6,-2,-4,-1,9,1,2,10,4,-9,3,-7,-8,6,4,6,5,-8,-6,-4,-4,7,-4,1,-10,-6,-2,3,-2,2,1,5,-5,-2,4,5,2,6,-10,-3,-7,-3,-4,1,-7,1,8,-1,2,3,3,6,2,1,-8,4,7,-6,-4,-6,-7,-1,6,-9,7,-4,2,6,-1,7,3,-7,-9,-1,8,-5,8,-4,-8,-1,-7,-5,-3,2,-10,-3,10,-5,-3,-1,-6,5,-4,6,-2,-9,10,-7,-5,-8,9,9,-1,8,3,-4,8,4,-10,4,-7,-10,-6,-3,9,-7,-3,8,5,10,5,-8,5,5,-10,7,3,-8,8,10,-1,6,7,9,-7,-9,-3,5,7,-3,-2,-6,-10,2,4,-3,-2,8,-2,1,-6,-2,-5,6,1,-1,-10,6,1,-5,-3,-9,-9,4,6,1,-8,-10,1,7,7,-5,-2,6,10,-8,2,-9,6,2,-1,-5,-5,-1,3,10,-5,7,-7,-3,-4,9,-10,-9,-4,-10,2,-3,10,-5,2,-5,10,6,-4,-4,10,6,-4,6,-6,2,-4,6,8,9,9,-9,-5,-8,-6,9,8,5,10,1,-10,3,7,-7,3,9,9,10,-4,1,3,-5,-5,4,-4,1,-9,9,6,-4,-4,-10,10,-5,10,-4,7,-3,-10,10,-5,1,9,-1,7,-5,-6,-4,-9,-1,-6,-2,-4,7,-4,-1,2,-3,1,-6,-9,1,-10,-4,-5,-5,-9,6,-4,1,-4,6,-4,6,5,6,-5,-1,-4,-3,9,-2,7,-4,-2,8,5,3,7,7,-1,5,-1,-2,-1,-6,3,9,-5,-2,7,-5,5,2,-5,-3,-1,6,-9,9,-3,2,-10,-7,-5,-1,10,5,-2,-9,-5,5,5,1,10,-5,4,1,8,10,9,-6,-9,-4,5,10,-8,-9,8,6,-10,1,6,-10,9,10,3,-7,-4,-3,-4,10,-10,4,8,6,-1,-2,8,-5,-1,-7,8,5,2,-2,1,-10,-2,-8,6,-6,10,6,-9,-7,6,5,5,-8,9,5,6,2,-2,8,-6,-5,-4,4,-3,-6,-4,-5,-10,-8,-6,1,-10,10,5,8,-4,-8,7,4,5,-1,10,10,10,10,-10,-10,4,-2,9,10,4,-4,10,-1,9,-5,-7,-10,2,-6,1,-5,-5,-5,9,-10,3,-6,-5,1,-8,-2,9,5,-3,4,-5,10,5,4,3,9,-9,3,1,-7,-10,5,2,1,-8,-1,5,3,-9,6,-3,7,9,8,-4,8,-4,3,10,3,-10,-1,6,-7,-2,-4,-7,9,-5,-5,-1,-2,3,-3,3,10,-8,10,-6,-6,9,5,5,3,10,8,10,-6,-7,-7,5,-6,10,-7,-3,5,7,10,-4,1,-1,-5,8,4,-2,-8,10,-2,-9,7,3,2,1,-3,4,-1,10,-4,9,6,10,-10,7,1,10,6,1,5,-1,-9,10,-10,5,-1,-3,-8,2,-1,8,4,1,3,-1,4,-7,-1,-2,-1,6,-5,-10,1,-1,-10,-6,8,8,9,-10,-5,7,-5,-4,10,-8,-8,6,-10,-4,7,-7,-7,-6,4,1,-4,3,9,-8,9,2,6,-1,-8,-7,4,9,6,-10,-5,2,-9,-3,-6,7,-8,-7,10,1,10,2,9,-7,-1,9,-8,-7,8,7,-10,-1,7,3,3,-5,9,9,1,4,3,-9,-4,1,-4,-6,-5,3,3,9,-7,1,4,-5,-5,8,-2,-2,3,8,2,-2,-9,10,10,-9,6,6,-7,-6,9,2,-2,8,8,5,-8,-8,3,-2,-9,-3,-1,8,9,10,-9,1,-7,-9,5,-4,10,-3,-1,-7,3,9,8,-2,1,-6,6,-2,-8,-7,-4,7,4,6,-2,10,-2,1,-4,10,7,-6,5,8,-10,6,8,5,-1,1,-5,-1,8,8,5,9,-3,-4,4,2,9,-5,1,-2,2,-10,-2,3,-2,-6,-8,8,-10,10,6,-8,-1,-5,3,-9,-3,-2,-9,-7,-4,8,7,-3,-10,-3,-6,5,-3,2,-10,-3,-7,9,7,-6,10,5,2,4,-3,-10,7,-8,8,6,-10,-4,-1,-4,-9,-1,6,6,-6,-2,9,-9,1,-5,-5,8,8,-2,-5,9,-9,-2,-6,3,-3,10,10,6,-7,8,-2,7,10,-10,8,-10,-10,1,3,10,2,-5,1,2,4,10,-10,-9,8,7,1,-6,10,-8,3,8,-10,-8,8,-7,-1]], dtype = "int64")#candidate|7036|(1, 2002)|const|int64
call_7035 = func_6559_call(relay.reshape(const_7036.astype('int64'), [14, 13, 11]), relay.reshape(const_7036.astype('int64'), [14, 13, 11]), )
call_7037 = func_6559_call(relay.reshape(const_7036.astype('int64'), [14, 13, 11]), relay.reshape(const_7036.astype('int64'), [14, 13, 11]), )
func_2626_call = mod.get_global_var('func_2626')
func_2627_call = mutated_mod.get_global_var('func_2627')
call_7038 = relay.TupleGetItem(func_2626_call(), 0)
call_7039 = relay.TupleGetItem(func_2627_call(), 0)
output = relay.Tuple([call_7004,call_7035,const_7036,call_7038,])
output2 = relay.Tuple([call_7005,call_7037,const_7036,call_7039,])
func_7043 = relay.Function([], output)
mod['func_7043'] = func_7043
mod = relay.transform.InferType()(mod)
mutated_mod['func_7043'] = func_7043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7043_call = mutated_mod.get_global_var('func_7043')
call_7044 = func_7043_call()
output = call_7044
func_7045 = relay.Function([], output)
mutated_mod['func_7045'] = func_7045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4700_call = mod.get_global_var('func_4700')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_7078 = relay.TupleGetItem(func_4700_call(), 0)
call_7079 = relay.TupleGetItem(func_4701_call(), 0)
output = relay.Tuple([call_7078,])
output2 = relay.Tuple([call_7079,])
func_7084 = relay.Function([], output)
mod['func_7084'] = func_7084
mod = relay.transform.InferType()(mod)
mutated_mod['func_7084'] = func_7084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mutated_mod.get_global_var('func_7084')
call_7085 = func_7084_call()
output = call_7085
func_7086 = relay.Function([], output)
mutated_mod['func_7086'] = func_7086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_7110 = relay.TupleGetItem(func_2421_call(), 0)
call_7111 = relay.TupleGetItem(func_2422_call(), 0)
func_6304_call = mod.get_global_var('func_6304')
func_6305_call = mutated_mod.get_global_var('func_6305')
call_7127 = func_6304_call()
call_7128 = func_6304_call()
func_3832_call = mod.get_global_var('func_3832')
func_3834_call = mutated_mod.get_global_var('func_3834')
const_7136 = relay.const([9,7,9,-8,6,-2,-5,4,-4,2,-7,3,5,-2,2,-6,-3,-6,-2,3,-10,8,1,-7,5,9,2,-1,9,-5,-9,10,3,-6,2,-3,-6,10,-3,6,-8,9,5,9,5,5,-5,8,2,-3,5,9,-6,-1,-7,6,-10,-7,5,10,-10,-6,9,4,-1,-6,-4,-8,-5,9,5,-1,-10,-9,6,9,-4,2,-10,-3,-3,7,-7,8,-5,-7,-4,-5,-7,-1,6,9,-6,3,7,-9,8,-10,3,8,8,-10,4,-7,10,3,10,5,-5,4,-6,-4,10,-7,5,3,-1,-4,-6,5,2,3,-2,-10,9,-10,-8,7,-10,1,2,-7,-6,-9,5,-10,3,-1,-4,-3,6,9,-8,9,3,-1,3,9,10,-10,1,2,-5,-1,5,-3,-9,-2,-9,5,1,10,-6,1,-6,-3,-3,2,-9,9,9,4,6,-3,6,-8,5,-9,6,9,3,10,-8,-5,5,2,8,10,-1,-9,-2,-4,-5,-10,-6,-3,-10,6,5,-4,7,-4,1,9,8,10,4,-7,-8,-10,-5,-3,5,-2,1,1,-3,3,9,-7,-9,-7,1,-2,2,-1,-4,-3,-4,-9,4,-2,-5,2,-8,-2,-7,10,6,7,5,-6,-4,9,-7,-2,-10,-9,-1,10,-1,-4,3,6,-7,9,1,-2,6,3,-2,4,9,-7,-4,10,9,-4,10,-2,-3,3,-6,-8,-6,8,6,-10,-5,5,-1,-5,-1,-3,-10,-9,5,6,-7,-6,5,-3,-5,-6,-9,10,-8,-10,-5,-9,7,-10,2,-6,2,3,3,10,10,-8,9,-1,-4,-3,6,-6,3,-7,-3,3,-2,-7,-6,-5,-3,5,1,-6,-9,-4,4,-7,-7,2,-5,9,3,4,-3,6,-10,-5,-7,5,-3,-10,-10,-3,-1,-9,2,-4,4,-2,7,-10,-1,9,9,5,-5,-10,-1,-2,-8,7,-10,4,-10,-8,6,-3,6,-4,-6,-8,1,-5,-1,-5,9,10,4,3,10,-1,1,3,6,4,-6,10,-2,-10,-4,-1,-8,4,3,-7,1,1,-2,1,10,7,-2,3,-3,-5,1,-4,7,10,5,6,5,-8,-10,2,-8,7,-7,-2,-7,-1,-2,-5,1,10,-5,4,4,5,-2,-5,8,-8,4,7,-6,-8,-3,9,2,-2,8,5,9,-5,10,1,1,5,1,5,-2,8,-7,9,-8,6,-8,-7,2,-8,-1,-10,-8,8,-9,-7,-7,6,1,5,10,-5,-4,-5,-4,9,-2,2,6,-9,4,-9,10,8,3,-9,5,-3,-8,-5,1,-10,5,-1,1,-9,8,7,-3,7,8,-3,2,4,-4,2,5,6,-5,4,-9,-2,-10,4,2,3,9,-5,-2,3,-7,9,1,3,-4,-4,9,9,5,-7,5,8,-8,9,1,-3,-8,-10,10,5,-2,9,4,-3,1,7,9,-4,-8,6,2,8,4,9,5,9,4,7,6,-9,9,7,-1,5,-3,-9,-10,6,-8,9,-10,9,4,4,-7,1,6,5,8,-9,3,-5,-6,7,6,7,2,-2,5,10,-8,1,-8,3,6,-6,-9,-2,-2,1,6,-5,-8,-9,-4,7,8,6,-4,-2,1,1,-9,-5,3,10,-5,-8,-4,6,-5,-10,10,-1,-4,-7,2,-7,1,3,-9,3,-8,7,-9,-9,-7,-7,4,-3,2,-5,6,-7,-3,10,1,-6,-4,10,7,8,-10,-2,5,-5,7,-3,-4,-9,1,1,-5,-3,-1,2,4,-3,-5,1,2,8,7,-2,2,-10,-3,4,-9,8,-2,7,2,-2,-4,-8,-10,6,6,10,1,10,2,-3,3,-10,-2,2,-6,-1,-9,7,-5,-9,-10,8,3,-5,-4,-8,2,1,-5,-7,9,-1,9,2,-10,-7,-1,2,-5,-1,-7,-5,6,-2,2,2,-9,4,1,-4,-6,-9,-5,3,10,-10,-4,4,2,-3,-5,-8,9,4,5,-1,8,9,3,-3,7,-7,-10,-3,9,9,-10,-10,-8,-9,2,-5,1,4,-8,-4,2,-6,-4,-7,4,7,-2,4,-1,2,-4,6,10,7,8,-3,-5,-3,7,-2,-5,-8,7,-4,7,-4,2,6,9,-10,-7,7,1,10,9,10,10,10,9,6,9,-7,-9,5,-8,-2,7,6,-1,-7,-6,-6,-6,-2,10,3,7,4,-2,-1,-3,5,6,7,8,8,2,10,2,-3,9,4,5,-9,7,9,-7,-10,-8,10,1,-9,4,1,1,-8,9,6,2,-2,7,8,10,7,-5,3,5,-10,-3,-4,-4,-5,-8,10,-6,10,-6,9,8,-3,5,8,-9,-10,9,7,10,-10,-4,-10,-3,-6,-9,-6,-5,10,6,-1,-8,7,6,-1,-7,7,-1,2,5,6,4,-3,-2,8,-10,-3,9,6,-8,-4,-9,-6,5,-8,-7,6,-6,-10,-1,6,-7,-10,3,-2,4,-5,4,-5,1,-9,8,10,4,2,-8,7,-9,2,4,2,7,-2,1,1,-1,-8,8,2,-8,7,3,1,-10,4,4,-1,5,5,-1,8,7,-2,4,6,8,-7,-5,3,-9,9,-4,6,4,-7,-8,-8,1,-9,-3,6,-6,2,-1,-9,3,6,8,9,5,-8,3,7,3,-10,1,-8,8,10,-5,10,7,-5,7,-7,-4,-5,-9,10,10,-10,5,-2,8,-10,3,8,5,-4,-9,-5,6,-9,-4,-10,-8,-7,-8,6,1,8,-8,-3,-4,-5,6,8,-2,8,8,8,6,-1,-4,-4,-4,8,-3,-7,8,9,-4,5,-4,9,8,-9,5,-3,-6,-6,1,4,-7,-8,3,-8,-4,2,-5,-3,-2,-1,2,-8,1,1,-9,4,6,-10,1,7,-2,-7,-1,4,-1,-10,9,3,1,-1,-7,-8,-9,1,8,-7,-6,-9,-3,10,-8,-8,10,6,-3,4,4,-4,-10,-4,2,9,4,-7,-1,-10,9,3,-7,-3,-7,-2,-6,-5,1,3,1,-3,9,9,-9,8,-6,9,1,-6,6,-3,-4,9,8,-1,5,3,4,-4,2,2,5,3,-3,8,9,-2,-10,2,-4,-6,-5,-4,2,1,-2,-1,-4,4,-5,7,-4,1,-1,-1,-4,-5,-7,-9,7,-10,-4,-5,-7,-6,-1,-10,-3,8,-4,10,-7,10,-1,10,10,6,-3,2,10,-4,-10,-8,5,-8,7,8,10,6,8,9,10,-2,4,2,-2,9,-9,7,-4,-3,-1,-3,-1,-2,8,7,-7,-8,-2,7,7,8,-2,1,9,7,7,3,-10,8,-8,-4,5,6,-4,-1,-10,8,5,-9,3,4,-3,-9,4,1,-4,7,-6,-7,9,-3,9,2,-9,8,-7,4,-1,-3,2,-7,8,8,-8,-6,2,-5,-1,5,-7,3,-5,-4,-2,3,2,4,3,-3,6,-7,9,1,6,9,9,5,-1,-10,7,-8,-3,-6,4,-9,-3,9,8,-1,4,-8,-3,6,-4,-8,-2,-10,9,-3,-9,1,9,-3,10,1,-5,-8,6,4,-4,2,9,1,8,-10,6,-9,5,-2,-6,-10,4,1,6,9,-2,-6,-3,-10,2,-7,5,-5,-8,5,2,6,7,-5,7,-1,-4,-9,-5,-7,-10,5,-2,6,-7,-5,8,4,-1,6,-2,-6,-5,3,-3,-5,9,-8,10,3,5,-6,-1,6,-9,9,-1,-10,-9,6,-5,5,-3,-7,7,10,-7,-2,-9,2,5,1,-8,4,-6,-1,3,7,1,9,-1,7,-9,8,-1,8,-2,2,10,7], dtype = "int8")#candidate|7136|(1440,)|const|int8
call_7135 = relay.TupleGetItem(func_3832_call(relay.reshape(const_7136.astype('int8'), [1440,])), 1)
call_7137 = relay.TupleGetItem(func_3834_call(relay.reshape(const_7136.astype('int8'), [1440,])), 1)
bop_7148 = relay.greater_equal(const_7136.astype('bool'), call_7127.astype('bool')) # shape=(13, 9, 1440)
bop_7151 = relay.greater_equal(const_7136.astype('bool'), call_7128.astype('bool')) # shape=(13, 9, 1440)
output = relay.Tuple([call_7110,call_7135,bop_7148,])
output2 = relay.Tuple([call_7111,call_7137,bop_7151,])
func_7155 = relay.Function([], output)
mod['func_7155'] = func_7155
mod = relay.transform.InferType()(mod)
output = func_7155()
func_7156 = relay.Function([], output)
mutated_mod['func_7156'] = func_7156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4078_call = mod.get_global_var('func_4078')
func_4080_call = mutated_mod.get_global_var('func_4080')
call_7160 = func_4078_call()
call_7161 = func_4078_call()
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_7162 = func_3036_call()
call_7163 = func_3036_call()
bop_7168 = relay.floor_mod(call_7160.astype('float32'), relay.reshape(call_7162.astype('float32'), relay.shape_of(call_7160))) # shape=(13, 9, 1)
bop_7171 = relay.floor_mod(call_7161.astype('float32'), relay.reshape(call_7163.astype('float32'), relay.shape_of(call_7161))) # shape=(13, 9, 1)
func_1649_call = mod.get_global_var('func_1649')
func_1652_call = mutated_mod.get_global_var('func_1652')
var_7174 = relay.var("var_7174", dtype = "float32", shape = (640,))#candidate|7174|(640,)|var|float32
call_7173 = relay.TupleGetItem(func_1649_call(relay.reshape(var_7174.astype('float32'), [640,])), 1)
call_7175 = relay.TupleGetItem(func_1652_call(relay.reshape(var_7174.astype('float32'), [640,])), 1)
func_5829_call = mod.get_global_var('func_5829')
func_5832_call = mutated_mod.get_global_var('func_5832')
const_7178 = relay.const([-6.019191,0.570156,-8.431521,4.650425,1.618866,-4.168514,-0.925945,5.923594,5.200384,-1.208344,6.893726,-9.777144,-0.336167,1.139888,-2.937090,-1.686750,-2.652009,0.473095,-9.399213,1.095800,2.392810,2.882907,7.214971,-9.264017,7.146869,3.991219,3.049159,-5.704168,2.830648,1.598135,-7.402362,-3.081921,6.656549,4.086170,4.844576,-6.211845,-4.605644,-6.621677,-2.758415,-8.393254,4.061868,9.948767,-1.247831,-4.801041,1.658832,0.644498,2.191525,-6.966256,9.769447,-5.214924,-9.419116,9.933746,-8.410467,7.141603,-0.959833,-9.384027,4.700425,-1.963325,9.878226,6.959832,-4.707674,-8.241850,-1.264080,8.434047,1.848735,-6.096085,-9.516585,-3.751760,1.498544,3.385840,-9.764374,0.101749,0.429946,2.294776,2.150151,-2.111811,7.098461,5.011632,4.152527,6.018574,7.354504,1.089908,-1.504318,-3.532236,6.814608,5.682823,-7.216782,9.959640,3.117287,-8.414774,9.903804,-8.442137,-2.403848,-7.335547,-4.782719,-7.378821,-4.345235,8.637077,8.336990,-0.978025,-2.330395,-3.641751,4.651733,-1.973307,-2.011061,9.017211,4.148032,-3.463536,4.547434,-2.040023,5.314379,0.143185,-4.433417,-9.654802,4.939868,-1.239315,-1.445424,-0.035670,-3.363022,-3.977791,4.792337,-1.671709,-3.257756,-2.555076,1.598868,6.844386,6.956643,-3.676697,-7.809847,-9.937117,-5.615802,5.539864,4.311056,-1.844592,-4.143905,4.215167,-6.835252,4.583952,-7.961583,-2.048159,-2.388713,-2.399526,6.621052,5.847203,2.941806,7.982645,-2.608040,6.788306,-8.078728,4.493114,-8.228492,-3.435031,-0.771631,4.264400,-8.534865,-5.253940,-7.248179,-3.321493,-1.186398,5.049146,9.384532,3.431377,0.508221,-0.533602,-4.115935,-5.824363,-6.660882,9.529365,-9.476119,4.537579,-7.490425,5.113083,0.474008,-8.847988,6.628769,4.684075,-3.266817,-0.197668,9.759654,0.106769,-1.485461,2.951335,2.966304,5.720410,0.358245,-3.068396,2.164387,-9.561095,4.332141,-3.509878,-8.481343,-9.233703,-2.776841,-6.223344,7.750886,2.636255,-3.103636,-4.257014,5.370600,9.162560,-1.821951,-6.349789,-0.978021,-0.842049,-3.130687,-8.902148,4.701119,4.117393,-0.683669,0.643651,-3.328751,2.855505,5.923135,-4.724308,-6.327364,-5.919450,7.922338,-8.818024,8.060808,8.665092,2.216303,7.016729,-2.183404,-6.632253,-6.001098,-6.545841,-6.774552,2.185218,1.972932,-8.869661,-4.550105,3.476534,5.336909,6.025083,-1.462195,-7.524716,-8.169134,-4.233358,0.468337,3.253122,8.263130,-1.850775,-9.879922,0.715426,7.781529,9.995308,-5.546240,4.200801,-6.971047,4.691009,5.644215,-2.749932,0.477589,4.991300,9.300009,-7.233841,-2.124092,-6.368391,2.745714,2.414788,4.585342,-6.720013,9.541525,8.234175,-8.284529,-9.875370,4.511450,1.289032,-7.335023,9.855970,-2.996073,-1.382972,-9.742108,7.521907,-5.969827,-1.006468,5.423540,-8.943588,-7.460676,-1.089916,-8.073611,-4.655679,0.100138,-3.196238,-3.824314,4.504076,4.087750,-0.885231,-3.324397,4.838658,-8.451517,-2.092845,-1.893489,-0.393231,-5.908239,2.998988,6.396720,-5.940938,-7.595344,-6.566816,-5.281905,5.998263,7.454733,1.902819,3.136630,7.124849,-2.466170,7.362409,-7.513000,9.193333,-2.213966,9.190410,4.095772,-9.015754,-5.097552,-5.146766,-2.645177,-1.373535,9.049591,2.991700,0.021646,-4.158652,-9.155121,-8.507623,7.791875,3.995006,5.190286,-4.605647,0.283356,-0.598556,6.605561,-0.271400,-7.359467,-8.640411,0.485564,-7.464872,-3.786346,-3.911089,-4.102546,4.876064,7.647113,0.889724,0.322313,1.537342,-2.454517,-4.417170,-9.731974,6.806882,7.507355,0.252440,2.636529,4.193846,-6.082805,-8.198898,8.353701,6.222564,-7.823930,2.901357,-9.897138,-1.353478,-1.392930,-2.723911,-1.022074,4.552687,5.419269,-7.615711,-3.478925,-5.779100,6.082487,7.316685,-0.078306,2.706475,0.867338,-9.321796,1.811511,-5.263301,6.817795,1.835062,-1.114782,-1.947515,8.769031,-9.146320,-1.931317,-6.414486,3.677884,-4.123234,-8.174688,-4.039745,-3.924798,5.388329,-6.974624,1.946376,0.090921,2.750509,9.072053,5.612871,-5.891955,-7.764384,9.582514,-9.884897,-0.952492,-9.003766,7.891318,-8.042067,-6.502674,3.565502,0.255826,-3.654929,7.881008,-5.294342,0.837141,3.628220,1.288361,1.038738,6.309492,8.632600,-5.993023,-8.511146,2.755728,-4.126564,9.404267,-5.814541,-9.634007,0.667399,-4.829342,0.447300,0.903808,6.656987,-1.974582,3.258824,-4.601088,-0.314730,5.511967,-5.047550,0.903819,-6.257395,8.159336,-7.156259,3.820701,2.834190,2.171320,-6.543656,-1.206790,-4.387501,-6.062875,-9.699012,-6.598466,1.455006,1.870512,-2.047930,-2.225098,7.051521,5.844829,-3.251882,3.904764,-3.277016,-4.684687,-2.934376,-7.902890,2.153670,-7.515330,-4.183930,-3.664057,-3.343507,5.178173,6.972634,8.625554,2.987531,-1.937698,-1.798065,-2.237203,-1.628994,6.521093,7.656275,3.729913,-7.983523,-2.339141,5.327560,-6.562392,-0.333403,-2.680715,-0.387820,1.927843,5.241005,6.996475,9.397032,-3.651691,-9.742527,-2.505078,-2.690191,-8.041171,-4.471601,0.532211,-8.679596,4.830484,0.390344,-2.630794,-2.784341,-4.009408,4.731044,7.249747,2.021355,-6.226862,6.810125,8.906562,1.088833,-4.654376,-2.826168,6.035200,6.378563,0.826907,-1.666952,-6.082080,9.501330,-6.092086,-6.845880,-2.360461,-5.734472,6.384045,1.410238,8.959727,3.486584,-1.231646,7.917809,-1.611669,4.163947,8.786861,5.324696,-3.119844,-0.496283,2.909668,-5.557924,-5.217802,-4.005700,-1.023900,-3.442335,-9.033575,3.429948,0.788295,-3.264532,0.443158,-4.156616,-2.720750,7.593971,-1.299285,2.728961,-3.078239,0.566350,-0.113263,9.776678,-9.730223,-0.283447,6.638289,9.978606,-4.888405,-8.056502,6.658753,6.443970,-5.394006,-0.313118,-9.438229,-1.993682,5.497676,-2.404675,0.755235,-4.866275,9.790446,5.080567,-0.509749,-3.524729,-5.638726,1.650557,1.262076,1.637457,2.519555,-5.496743,-8.618325,-8.810772,3.935244,1.763556,-7.529651,-4.468584,6.616224,-9.840937,-1.730401,-0.525348,6.727243,0.639379,-7.953469,-9.267654,-8.387497,-1.197625,4.089078,2.112564,3.709079,-6.494337,-0.442529,2.674962,-1.271394,-7.150311,-5.727056,9.572407,-7.176652,-7.625824,-6.395396,-8.291932,-1.270403,0.481434,9.490458,-9.634515,9.761513,0.292755,5.614172,8.288909,-3.579588,-4.153484,3.140343,8.303172,-2.486175,-7.251860,-4.597988,-9.877549,8.331833,0.137014,-0.531199,9.033700,-5.439960,9.976052,-3.001812,5.045353,-4.209074,0.215785,1.950797,2.265274,6.586558,-8.705362,-0.311617,-3.116715,-8.146168,4.517571,6.469150,8.101698,5.837957,0.771909,0.176850,-1.840768,-5.773103,5.062486,-5.860976,-3.234604,1.971156,-8.569698,1.667219,8.317495,-6.040186,-0.993805,-4.845377,5.835829,-1.607674,7.860038,3.345070,-0.591513,8.009697,3.369324,-2.165898,7.307870,2.881251,-0.522846,-4.956819,-7.263254,-8.786886,-5.221975,-0.926957,-5.578751,-5.775011,2.629642,5.279191,-4.446081,0.309436,3.365894,7.834834,7.058584,-8.359718,7.367040,-5.776887,7.814099,-5.338329,0.238268,9.946896,0.705735,5.326292,4.067953,-5.138933,6.731800,8.628458,-5.041603,-6.513363,5.655880,2.296071,8.332356,3.040834,-2.464741,6.348528,-5.565812,2.166182,-0.456993,-8.923362,7.909874,8.432998,0.032435,5.865608,1.067265,5.492754,-8.493987,4.401142,-1.756090,-1.210726,-3.807174,-9.629312,-7.189117,0.276340,-5.370895,-8.641662,-4.422729,8.840797,0.340425,0.114293,-7.358611,3.856025,7.878578,-0.471829,0.911934,-5.230174,-8.937119,4.687011,-2.269227,-4.975551,-1.510654,6.680331,-0.865088,-0.562546,4.955493,6.295786,0.579885,0.322440,5.010420,-3.676848,-8.258755,2.492678,-5.504850,-8.609665,0.794905,6.516812,1.621594,-5.649391,1.059656,3.978318,4.165547,-3.520272,-1.960276,8.712775,-0.680488,-7.239249,5.480426,1.311952,-5.438173,-4.955920,-2.192514,-3.406560,-2.772295,-7.550080,0.253762,2.644946,-7.960571,7.740992,2.191201,-7.954488,8.782877,-6.278307,-2.120510,-5.098485,2.450810,-2.080617,-7.228806,-7.289868,-3.472714,3.016553,-6.255317,-4.296320,-9.283837,6.690313,-0.597442,0.359154,1.733517,-7.518573,-5.255748,-5.463961,-4.918756,2.927330,1.517591,9.436411,-6.946068,-7.199327,3.498968,6.085174,-9.759714,3.806840,3.821066,-8.680597,3.648106,-7.754121,6.559201,6.619201,-8.394035,6.237518,-1.018302,1.979884,1.371902,-0.443016,-6.036619,-4.516225,-9.678703,5.555681,9.730944,-5.865105,8.037957,-6.826665,-9.517346,-7.731824,-4.931073,-8.030621,-3.391471,-1.386204,0.547274,6.042235,-2.483370,5.403359,2.118453,-4.981946,-5.200862,9.386874,-8.472754,2.474442,-1.490147,1.141455,8.614519,4.831949,5.288629,1.822250,-8.759224,-0.289861,-7.850215,-7.623204,-9.835063,-0.914932,4.510603,-9.905904,4.605769,-0.130529,4.358109,2.067255,-4.936603,3.727882,-6.274752,-6.837353,1.302359,0.198234,-9.880806,3.848722,6.464275,-2.640776,-2.397090,-1.729090,-3.499969,0.812652,-6.633018,-8.166222,4.692885,-7.425568,-3.850850,7.366903,4.857958,7.225255,-9.938346,-1.769058,2.152670,-8.464136,-5.546766,0.427479,-6.269514,-2.867041,5.138027,2.499763,-0.674033,-6.213818,-8.299607,-4.809804,4.271620,-8.685490,5.375625,2.082396,0.957359,-4.208554,-7.725810,-4.262476,-7.645967,7.967951,2.602616,-2.835098,-4.593922,-4.876764,-2.166414,-6.604155,-4.037003,6.010680,8.065672,-9.875303,9.845642,-9.486433,8.597191,-3.219594,-5.195791,1.043870,-2.035817,4.152147,2.533675,5.575975,4.164685,7.193231,-7.795168,3.929997,4.540572,-9.621290,-2.319496,-3.736503,7.352937,1.285552,-0.128353,6.985315,-2.505294,0.071413,-7.891543,-3.942113,-2.282721,-2.381923,-0.948186,-1.368093,4.058879,-6.766493,-0.928738,3.405853,3.174074,9.131678,-0.956299,-0.690335,0.277036,-6.664123,6.197167,5.079166,-3.478365,-4.636225,8.540364,-0.531605,-9.705708,-1.049834,5.706507,-2.482068,-5.839947,-5.719509,2.888159,-9.781406,-2.462084,-4.062920,6.626658,1.603023,9.484868,-7.776487,-4.959081,-6.381571,-0.106066,6.687753,-7.107894,-7.811903,2.616176,5.391801,-3.488520,-7.402749,-4.870830,-3.999564,-7.046946,4.837096,5.603973,7.370905,-9.522660,-5.334723,-4.902590,-3.923764,-7.376351,-1.775288,1.005075,-7.572004,3.784424,-0.396904,1.743874,1.431565,-3.338432,-2.869665,-3.750620,-0.625434,7.807976,2.357299,-0.120061,-7.139725,1.691501,0.380432,3.669011,-8.696216,-4.950423,-2.571921,9.281189,3.031591,1.161220,1.211853,3.692502,-8.183325,9.431432,4.083757,-9.322589,-3.970602,-8.935994,-7.749527,8.453642,-9.870566,-6.646849,3.964221,-4.070366,2.569637,-1.489615,0.003412,-7.039167,-0.475556,-1.872345,-8.546332,-0.156186,-6.154292,-0.535333,-4.713245,7.410394,7.694029,4.602246,3.702625,3.774536,1.697975,0.576619,-9.588643,4.917146,3.550573,-5.304532,-4.077831,-3.453215,4.330794,6.332389,-6.039772,-8.368366,-3.042399,8.710582,7.561956,2.256728,-5.160933,9.085267,-5.348097,-9.237196,-8.751988,4.408946,4.875671,2.533017,-6.065197,-8.686655,2.996226,-1.217485,-5.434567,0.721924,3.846523,0.309931,-5.401318,-7.314152,0.577769,-6.856485,5.751295,-4.770653,-8.494329,9.493534,-5.822316,7.888590,-7.400713,-2.593917,8.840594,-5.338902,-2.798724,0.203083,-0.394748,5.890799,-5.407107,-3.902402,-2.596810,-2.528375,-2.574537,2.299434,5.349598,9.612812,9.847215,-7.378782,4.003630,1.530698,-6.200499,-7.991517,-7.465714,-7.687269,-9.803396,-6.947596,8.338405,6.056766,-8.151796,5.862861,3.287493,8.936689,-2.611490,-6.633283,-6.941982,2.823362,-4.305577,2.760830,7.255546,5.892163,-3.865894,-0.199535,-3.161762,-5.159275,7.731889,-4.079938,-7.286772,7.329212,7.675452,-4.470176,3.983525,8.821995,-7.673833,-8.448521,-3.528253,1.261623,6.130611,5.388153,4.061909,-8.739116,2.622345,8.639637,-0.696324,-6.519809,-6.405777,0.676728,-4.531404,8.537783,1.933118,-6.068150,6.353836,4.366158,-8.389492,-2.134983,-8.654259,-7.191528,6.184207,7.567495,-2.549461,-9.593872,-9.681750,-5.820551,-6.113609,7.397946,4.435837,0.929058,9.741878,2.850143,9.194508,6.593291,-8.811639,9.633283,-3.856703,9.839831,-4.191721,2.398348,9.940851,3.497726,-7.525539,7.587772,9.320734,-2.729011,4.420785,-0.737295,-3.693157,-4.196673,5.157493,-7.575474,-1.742872,-2.000147,4.900078,-9.048104,2.641172,-0.383806,-1.354801,6.924960,1.127838,4.732213,9.653023,2.010204,6.657366,-8.685047,-1.343275,-2.859983,-6.740263,4.154089,0.911317,-0.819279,-3.315584,-4.152555,-9.479145,-8.759855,3.291667,3.432464,1.099701,-9.123955,-4.314913,3.968929,-7.089629,-8.636228,-3.793767,-4.268581,3.329328,-2.545768,-9.323310,-9.573943,-8.647849,-7.936156,-2.286372,-8.318850,-6.100682,2.036649,7.325930,4.423426,-3.690057,-0.849242,-8.812498,-1.308571,7.759295,3.070735,5.983079,-2.908693,-3.955265,-3.491966,-2.269514,-2.112800,6.965498,-4.409699,-8.526821,-2.657817,9.091589,8.338330,-7.722390,7.463813,-2.208015,2.640589,-1.893107,0.983195,-0.779070,-9.913799,-1.169280,3.602942,-1.839566,-3.272078,-1.044564,7.165802,4.471728,8.919110,1.589766,4.567947,2.705032,5.985903,-6.362085,-1.597390,-6.533554,-5.394699,8.112863,5.623931,5.306803,-7.001506,-0.443756,6.988913,-3.823951,4.800744,7.969687,8.796545,9.077412,-8.209090,5.203023,-9.236541,2.581239,-8.806014,3.259734,-8.349940,9.650921,-6.785277,5.183996,5.883231,-6.668979,9.221155,6.067181,-4.232257,4.018983,-9.946779,7.359415,1.101150,9.495113,9.024393,8.960460,7.788716,-5.050553,-6.501559,8.548592,8.133217,9.649666,0.502048,0.496822,7.299993,8.421603,7.712429,8.800299,6.227805,-4.907302,2.394548,2.947855,-9.639276,-9.010258,9.890774,-6.009890,5.561179,0.947616,-4.442424,-2.478210,7.006396,6.306718,-0.822878,4.620722,-1.389010,-5.982545,3.228242,-6.272127,6.984671,6.368174,0.588247,6.617797,6.631272,3.023419,6.898168,8.885245,1.023890,2.443979,3.080205,-3.459513,-1.566809,0.288413,-9.709452,5.467858,-0.724437,-2.691525,-6.479638,-0.408827,-8.542378,1.076070,3.999484,-0.439730,3.364954,-0.438009,5.783084,-0.861552,0.037614,1.703719,-3.056851,9.231214,5.311103,-5.823487,4.618598,0.390537,-3.562958,5.435989,-5.121302,3.130789,8.144680,-1.097221,-0.976114,-0.151358,8.508002,7.552554,-1.649196,-1.017076,-3.402321,5.880830,-2.522404,0.304944,4.760917,-3.245213,-9.908550,-6.769686,-1.295297,-9.179295,7.928794,-5.356399,4.281147,-3.109344,5.015268,9.751568,3.381998,9.345721,-0.737901,8.649850,-7.574606,3.034521,7.682911,-7.048240,-8.818476,-0.413702,-8.171639,-6.314478,-6.568851,9.967379,-7.696693,6.140232,-3.281401,8.845473,5.166159,-2.409375,-9.749799,-3.237079,4.700370,8.543000,-3.755975,-7.038142,1.899585,-6.427301,7.515339,6.762947,-4.877404,-8.570907,0.005068,9.123810,-8.466779,-1.893609,8.173216,-9.101147,-7.232744,5.474737,3.630535,2.703893,-7.057665,-2.680516,0.220016,0.035605,-5.873336,-3.289258,8.757423,-2.344011,-9.268350,2.096253,9.747765,-6.361352,4.698110,-1.612018,4.563831,9.892948,3.006978,-2.521928,3.302362,8.267938,9.763099,-9.763861,3.850808,-5.659958,2.044978,-3.801405,3.491890,-2.295633,-9.818022,0.240792,-0.609312,7.457097,-4.858793,7.430672,-3.677200,1.055642,-5.999895,-9.013032,-7.105503,1.463399,-3.343542,-9.723539,5.566802,1.512351,-4.814576,3.461681,4.432112,-3.180440,-9.804600,-3.216798,-2.421822,-0.230019,2.055551,4.404454,1.465853,4.286636,-1.730467,5.141725,5.299173,2.201388,9.099270,-3.449215,2.884785,-9.148824,-2.026535,-6.880145,-8.828128,-9.449104,-1.630309,4.581907,-6.370855,1.135708,3.394170,-6.527334,6.572469,-0.405971,9.254956,-3.298698,7.675450,-9.514955,5.566549,8.955107,-5.312427,7.277501,0.023242,-3.283452,2.402933,-8.940802,6.958509,6.747397,-4.654823,8.604631,9.873573,-9.145738,2.915738,-8.946404,-2.960458,-5.373860,4.801789,3.258687,9.891514,5.543660,0.087076,7.916416,-6.166491,-6.963507,-0.514405,-6.568028,9.752735,-5.591193,-3.936026,0.151655,-6.060796,4.799591,9.763244,-2.808549,-5.721696,8.722394,6.823312,-9.806301,-8.854489,-5.478661,0.216846,-5.140507,-5.360761,6.735856,0.060160,7.212498,-7.354348,-9.609507,0.364170,-0.172967,-4.470586,5.848145,-9.282318,9.817956,-2.024822,7.141779,0.499984,-4.113941,5.948713,-6.884170,-7.667962,-4.112587,-1.267026,-3.013623,-4.197214,8.953116,5.754777,-9.519648,6.621418,-3.230638,-9.729039,4.158541,9.651618,6.450175,0.929463,1.799754,2.644946,-6.133165,-4.118418,9.955337,-5.214322,5.444633,3.923019,6.641844,-6.353300,7.876573,-9.504996,-8.350921,-7.288808,-4.341660,5.721101,-6.037374,9.311327,-6.304801,0.752991,-2.215499,-5.642398,3.399673,-2.979094,-2.581458,-2.857260,4.871705,-8.726982,-0.647715,4.450517,-6.309608,5.636907,4.380101,-9.421571,-5.762917,3.016358,8.932131,6.513378,0.975848,0.455696,-1.807840,7.367963,-5.924678,8.962185,4.979487,4.717617,9.044692,-7.998462,-4.205925,-2.746930,-2.615527,6.073448,3.053630,5.151475,-0.085001,1.327630,-7.034739,-8.494621,-5.029264,-8.016245,-4.894788,-8.664692,-8.109913,-5.552843,5.767812,8.636607,-2.073463,6.359459,1.711629,1.556954,3.864578,-0.106160,2.197303,8.262663,-1.683823,3.685896,6.420986,-1.840293,-4.192683,-6.620840,2.503593,-7.616629,6.362663,-9.842069,-2.655749,-8.694352,-9.558581,7.568669,-6.106279,7.254082,-6.615023,1.161565,-2.411294,7.931192,3.782488,-2.032823,-6.307768,-4.373030,-7.425234,-5.340856,-6.536495,3.708498,-7.362658,3.615153,1.517199,7.472007,3.201617,1.066878,7.020234,4.079062,8.558673,9.172899,-2.843513,9.776126,-8.526878,3.586356,-7.555495,6.753999,1.667391,9.557817,-8.505707,1.052923,-9.804578,8.324126,4.695880,-3.743812,2.533908,-8.704448,6.574208,-4.580055,-6.942632,2.612387,-8.746151,6.851026,9.995749,-9.481856,9.835328], dtype = "float32")#candidate|7178|(1755,)|const|float32
call_7177 = relay.TupleGetItem(func_5829_call(relay.reshape(const_7178.astype('float32'), [13, 9, 15])), 0)
call_7179 = relay.TupleGetItem(func_5832_call(relay.reshape(const_7178.astype('float32'), [13, 9, 15])), 0)
output = relay.Tuple([bop_7168,call_7173,var_7174,call_7177,const_7178,])
output2 = relay.Tuple([bop_7171,call_7175,var_7174,call_7179,const_7178,])
func_7180 = relay.Function([var_7174,], output)
mod['func_7180'] = func_7180
mod = relay.transform.InferType()(mod)
mutated_mod['func_7180'] = func_7180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7181 = relay.var("var_7181", dtype = "float32", shape = (640,))#candidate|7181|(640,)|var|float32
func_7180_call = mutated_mod.get_global_var('func_7180')
call_7182 = func_7180_call(var_7181)
output = call_7182
func_7183 = relay.Function([var_7181], output)
mutated_mod['func_7183'] = func_7183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_501_call = mod.get_global_var('func_501')
func_503_call = mutated_mod.get_global_var('func_503')
call_7187 = relay.TupleGetItem(func_501_call(), 0)
call_7188 = relay.TupleGetItem(func_503_call(), 0)
output = relay.Tuple([call_7187,])
output2 = relay.Tuple([call_7188,])
func_7196 = relay.Function([], output)
mod['func_7196'] = func_7196
mod = relay.transform.InferType()(mod)
output = func_7196()
func_7197 = relay.Function([], output)
mutated_mod['func_7197'] = func_7197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5078_call = mod.get_global_var('func_5078')
func_5080_call = mutated_mod.get_global_var('func_5080')
call_7238 = relay.TupleGetItem(func_5078_call(), 0)
call_7239 = relay.TupleGetItem(func_5080_call(), 0)
var_7274 = relay.var("var_7274", dtype = "float64", shape = (16, 15, 10))#candidate|7274|(16, 15, 10)|var|float64
bop_7275 = relay.not_equal(call_7238.astype('bool'), relay.reshape(var_7274.astype('bool'), relay.shape_of(call_7238))) # shape=(16, 15, 10)
bop_7278 = relay.not_equal(call_7239.astype('bool'), relay.reshape(var_7274.astype('bool'), relay.shape_of(call_7239))) # shape=(16, 15, 10)
output = bop_7275
output2 = bop_7278
func_7307 = relay.Function([var_7274,], output)
mod['func_7307'] = func_7307
mod = relay.transform.InferType()(mod)
mutated_mod['func_7307'] = func_7307
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7308 = relay.var("var_7308", dtype = "float64", shape = (16, 15, 10))#candidate|7308|(16, 15, 10)|var|float64
func_7307_call = mutated_mod.get_global_var('func_7307')
call_7309 = func_7307_call(var_7308)
output = call_7309
func_7310 = relay.Function([var_7308], output)
mutated_mod['func_7310'] = func_7310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
call_7380 = relay.TupleGetItem(func_5115_call(), 1)
call_7381 = relay.TupleGetItem(func_5117_call(), 1)
output = relay.Tuple([call_7380,])
output2 = relay.Tuple([call_7381,])
func_7413 = relay.Function([], output)
mod['func_7413'] = func_7413
mod = relay.transform.InferType()(mod)
mutated_mod['func_7413'] = func_7413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mutated_mod.get_global_var('func_7413')
call_7414 = func_7413_call()
output = call_7414
func_7415 = relay.Function([], output)
mutated_mod['func_7415'] = func_7415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1073_call = mod.get_global_var('func_1073')
func_1074_call = mutated_mod.get_global_var('func_1074')
call_7416 = func_1073_call()
call_7417 = func_1073_call()
func_2643_call = mod.get_global_var('func_2643')
func_2644_call = mutated_mod.get_global_var('func_2644')
call_7423 = relay.TupleGetItem(func_2643_call(), 1)
call_7424 = relay.TupleGetItem(func_2644_call(), 1)
func_2389_call = mod.get_global_var('func_2389')
func_2391_call = mutated_mod.get_global_var('func_2391')
call_7425 = relay.TupleGetItem(func_2389_call(), 0)
call_7426 = relay.TupleGetItem(func_2391_call(), 0)
output = relay.Tuple([call_7416,call_7423,call_7425,])
output2 = relay.Tuple([call_7417,call_7424,call_7426,])
func_7430 = relay.Function([], output)
mod['func_7430'] = func_7430
mod = relay.transform.InferType()(mod)
output = func_7430()
func_7431 = relay.Function([], output)
mutated_mod['func_7431'] = func_7431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7086_call = mutated_mod.get_global_var('func_7086')
call_7432 = relay.TupleGetItem(func_7084_call(), 0)
call_7433 = relay.TupleGetItem(func_7086_call(), 0)
output = relay.Tuple([call_7432,])
output2 = relay.Tuple([call_7433,])
func_7446 = relay.Function([], output)
mod['func_7446'] = func_7446
mod = relay.transform.InferType()(mod)
output = func_7446()
func_7447 = relay.Function([], output)
mutated_mod['func_7447'] = func_7447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4078_call = mod.get_global_var('func_4078')
func_4080_call = mutated_mod.get_global_var('func_4080')
call_7490 = func_4078_call()
call_7491 = func_4078_call()
output = relay.Tuple([call_7490,])
output2 = relay.Tuple([call_7491,])
func_7502 = relay.Function([], output)
mod['func_7502'] = func_7502
mod = relay.transform.InferType()(mod)
mutated_mod['func_7502'] = func_7502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7502_call = mutated_mod.get_global_var('func_7502')
call_7503 = func_7502_call()
output = call_7503
func_7504 = relay.Function([], output)
mutated_mod['func_7504'] = func_7504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7502_call = mod.get_global_var('func_7502')
func_7504_call = mutated_mod.get_global_var('func_7504')
call_7531 = relay.TupleGetItem(func_7502_call(), 0)
call_7532 = relay.TupleGetItem(func_7504_call(), 0)
output = call_7531
output2 = call_7532
func_7581 = relay.Function([], output)
mod['func_7581'] = func_7581
mod = relay.transform.InferType()(mod)
mutated_mod['func_7581'] = func_7581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7581_call = mutated_mod.get_global_var('func_7581')
call_7582 = func_7581_call()
output = call_7582
func_7583 = relay.Function([], output)
mutated_mod['func_7583'] = func_7583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4629_call = mod.get_global_var('func_4629')
func_4631_call = mutated_mod.get_global_var('func_4631')
call_7586 = relay.TupleGetItem(func_4629_call(), 0)
call_7587 = relay.TupleGetItem(func_4631_call(), 0)
output = call_7586
output2 = call_7587
func_7606 = relay.Function([], output)
mod['func_7606'] = func_7606
mod = relay.transform.InferType()(mod)
output = func_7606()
func_7607 = relay.Function([], output)
mutated_mod['func_7607'] = func_7607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4629_call = mod.get_global_var('func_4629')
func_4631_call = mutated_mod.get_global_var('func_4631')
call_7734 = relay.TupleGetItem(func_4629_call(), 0)
call_7735 = relay.TupleGetItem(func_4631_call(), 0)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_7746 = relay.TupleGetItem(func_1758_call(), 1)
call_7747 = relay.TupleGetItem(func_1759_call(), 1)
output = relay.Tuple([call_7734,call_7746,])
output2 = relay.Tuple([call_7735,call_7747,])
func_7750 = relay.Function([], output)
mod['func_7750'] = func_7750
mod = relay.transform.InferType()(mod)
mutated_mod['func_7750'] = func_7750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7750_call = mutated_mod.get_global_var('func_7750')
call_7751 = func_7750_call()
output = call_7751
func_7752 = relay.Function([], output)
mutated_mod['func_7752'] = func_7752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mod.get_global_var('func_1677')
func_1678_call = mutated_mod.get_global_var('func_1678')
call_7814 = relay.TupleGetItem(func_1677_call(), 0)
call_7815 = relay.TupleGetItem(func_1678_call(), 0)
func_4514_call = mod.get_global_var('func_4514')
func_4517_call = mutated_mod.get_global_var('func_4517')
const_7821 = relay.const([5,-9,10,-3,-4,9,5,9,10,1,-9,-7,-4,-2,8,4,-1,-2,-8,3,8,-3,5,9,10,-1,10,6,6,-1,-3,8,8,6,5,-10,-3,-5,3,-4,-4,5,-6,-8,-1,7,-5,-10,4,-1,-5,-1,-3,7,-2,10,7,-10,6,-5,8,-3,-6,-8,-8,1,-9,4,-1,-8,3,9,-3,4,10,8,-1,10,5,8,-6,-9,-1,7,-5,5,4,9,-6,9,-2,1,-10,-9,-1,-8,-5,-4,-3,8,-7,-5,8,10,-7,-7,8,2,-3,2,-9,-10,9,-3,-4,-10,8,4,1,10,-3,-9,-9,8,4,-5,-10,9,9,-4,7,-4,3,-10,1,4,-9,4,6,9,10,2,6,-1,-7,8,3,8,-1,8,-10,-6,7,-6,-2,10,-8,-3,-8,-9,-1,1,-10,-8,9,3,-2,8,-8,10,-9,1,-7,-2,-9,1,8,6,1,9,3,9,10,5,-4,-8,-7,2,3,8,5,-6,1,2,-7,2,-2,5,10,8,5,9,-6,6,5,3,-5,-4,2,-8,7,-9,3,-9,-2,-9,4,8,8,-9,-2,-2,3,3,2,-4,-5,7,5,-3,4,5,-9,-8,-9,-10,1,-7,-8,10,4,-8,-7,7,1,-10,-1,3,-9,8,1,-8,8,9,-6,5,-4,-10,-7,2,6,-5,8,8,-2,-3,2,5,7,-7,4,-4,6,7,1,-3,1,4,5,-7,8,-10,-3,2,9,-2,3,1,-10,-5,8,-7,-6,-10,-5,-10,7,3,4,-2,5,8,-2,9,9,-4,-2,8,4,-8,7,1,-7,5,-10,-4,1,-4,1,4,7,-9,-10,6,-6,-4,4,6,2,1,-6,-8,9,9,-5,-1,2,-1,6,-6,-2,5,8,7,1,-1,-5,6,-10,3,8,10,-4,2,-10,4,1,-8,-9,8,-5,8,7,-3,9,-4,1,-6,-9,-7,-1,1,-10,-2,5,8,-8,-9,10,-1,7,-5,1,5,2,-9,5,-6,10,-4,7,-7,2,-9,8,-1,-5,-5,-10,8,-6,-6,8,8,1,5,5,4,-7,-2,-2,4,-1,-6,1,4,3,-10,5,9,9,-5,-7,4,3,1,-8,3,-3,-2,-6,-4,8,10,-2,-9,-4,-7,-5,-4,-6,-4,-9,-4,7,-1,-2,-2,8,4,-2,1,9,-6,9,-3,-5,1,-3,10,-1,-4,5,5,-9,-5,6,-6,6,-1,2,-1,-10,-2,-7,4,-3,-5,6,4,-1,-6,-7,-1,-2,9,6,-2,-2,9,9,1,2,2,8,-1,5,7,10,4,-10,-8,4,-3,6,-10,-5,-7,-9,-3,5,7,5,-1,-1,9,-9,-8,-8,-9,-2,7,10,-4,-3,5,3,7,3,3,2,-5,-10,3,-3,10,9,-3,-3,7,4,-3,1,4,-7,-8,-10,1,-6,-8,5,4,-7,-7,4,6,6,-6,1,-1,-9,-9,-1,-9,-5,6,4,7,9,-2,8,2,9,-10,-9,3,9,-9,4,-9,-4,10,7,1,-3,-8,1,4,-9,4,-3,-8,-9,-7,4,4,1,7,-3,-1,-1,7,2,-6,6,-10,7,3,4,10,4,-7,-10,-10,-3,3,-1,-6,2,5,-1,6,3,-5,9,-7,3,-9,-8,-10,-1,5,-3,-6,-4,-2,-6,-5,2,-7,7,-6,-8,3,-4,-9,6,-9,-6,4,6,6,-8,4,-1,9,-5,-10,9,-8,-8,10,-2,1,-3,-9,2,-4,6,-8,-7,7,-3,-4,2,-5,-1,-2,-3,-1,7,7,5,8,7,10,-5,7,-6,10,7,8,-2,10,-3,-2,-3,2,8,1,7,9,-10,8,9,6,5,3,4,1,-6,-2,9,1,3,3,5,2,8,3,-9,-3,-1,-10,-10,4,3,7,9,1,1,-4,6,2,-9,1,-4,-2,9,-3,4,-6,-3,-9,2,6,4,10,7,1,-8,4,9,8,8,8,9,7,7,-6,-7,-4,2,10,5,5,-6,-7,3,-4,7,2,-3,9,8,3,-6,8,-1,9,-2,1,-1,4,6,-6,-7,8,-7,4,-2,1,-3,8,-7,-2,-1,-6,3,-6,-5,1,-1,4,8,1,4,-8,1,3,-4,5,-1,-6,1,3,-6,-10,5,-3,1,-3,-8,-1,8,4,-10,5,-2,-6,-7,-8,5,-10,-9,5,8,4,8,2,-3,10,-7,-5,-8,-9,1,-7,-3,-9,9,4,-2,1,8,-10,2,-4,-6,6,-9,-10,2,9,6,10,3,-3,4,9,-9,-3,-10,10,6,-2,10,-5,9,10,3,-1,5,5,9,-3,4,9,-3,-10,4,-3,-3,-7,-4,8,-8,-8,-4,-4,7,-3,-3,5,-1,4,6,-10,-6,1,-7,-9,-9,-7,10,-8,-1,5,3,-10,4,10,9,-9,8,-7,9,9,5,-5,-9,9,1,-4,6,9,-7,-10,-10,3,8,-4,-6,-7,10,5,4,-9,-9,-1,8,7,-8,2,-7,-7,-5,-4,-1,3,4,1,1,2,7,-7,3,8,2,-9,-5,3,-5,-2,-7,-10,-10,-8,-2,-10,-4,-4,2,8,4,-2,6,-10,2,1,-4,2,-1,6,3,-4,5,-3,2,1,-1,-6,8,-1,-7,-2,1,-6,6,-8,7,5,-2,9,2,-9,-10,-3,10,-1,-4,7,-8,-10,4,-7,-1,-3,3,-6,-9,-9,9,-9,5,7,4,-5,-8,9,4,-3,8,-10,7,7,1,6,7,-3,5,2,-6,2,-3,-8,-8,-3,-6,-9,-9,8,4,1,9,-6,4,6,6,-5,-2,7,1,-8,5,9,-6,7,1,1,-2,8,4,7,1,-10,-5,3,-9,5,10,1,3,8,-5,-5,6,6,-7,-2,7,3,9,7,7,-3,8,-5,-3,4,-1,-7,-4,1,-6,-4,-4,-4,-3,2,-7,-8,-10,-5,-7,-1,1,9,8,9,-2,-8,9,1,7,1,8,-8,-2,1,3,10,-9,1,7,-3,4,7,-7,5,-10,7,-6,8,9,7,-3,-10,-6,-10,-3,-3,-8,10,9,-9,-10,8,-3,-3,-8,-8,9,-3,-7,7,-8,6,-9,1,-2,6,7,7,2,4,-4,1,10,-8,9,-8,-6,-4,3,-4,4,-6,-5,10,-6,-9,9,-2,6,-6,7,-3,-10,-7,-2,5,-2,6,-5,5,3,2,4,10,5,-6,-2,3,-7,5,3,5,3,1,10,-1,-1,-6,6,6,4,4,-4,9,9,-9,4,-6,-5,-4,6,-9,-6,-2,5,-4,4,6,-4,9,9,-6,4,-7,-10,6,-6,-2,2,-7,-6,5,-10,7,-7,7,-6,6,-6,9,-4,3,9,-2,-1,-9,9,-6,8,3,2,9,5,-6,-8,9,9,10,7,-3,1,5,8,7,7,-1,-1,6,8,9,8,-8,9,-7,9,7,1,-10,-3,7,8,-10,-10,3,10,-4,9,7,9,8,-3,-10,7,7,6,4,4,2,-10,-2,8,-1,5,7,-2,-1,-2,-1,-10,10,2,1,8,10,10,-10,-7,7,1,-7,9,-7,-1,-9,-5,-9,5,-3,-5,4,-6,-4,-7,6,-5,8,2,-6,-4,-4,-7,7,4,8,-4,5,-5,4,1,10,2,-1,-3,-7,-5,-9,-5,6,-8,-9,5,4,-4,-3,-8,-3,1,7,3,3,7,10,-8,-1,1,3,-3,-7,7,2,-3,8,-10,-7,8,-1,-2,7,1,10,-6,-9,2,-6,6,-6,4,2,-6,-9,7,-1,4,10], dtype = "int8")#candidate|7821|(1440,)|const|int8
var_7822 = relay.var("var_7822", dtype = "float32", shape = (1, 1755))#candidate|7822|(1, 1755)|var|float32
call_7820 = relay.TupleGetItem(func_4514_call(relay.reshape(const_7821.astype('int8'), [1440,]), relay.reshape(var_7822.astype('float32'), [1755,]), ), 8)
call_7823 = relay.TupleGetItem(func_4517_call(relay.reshape(const_7821.astype('int8'), [1440,]), relay.reshape(var_7822.astype('float32'), [1755,]), ), 8)
func_4032_call = mod.get_global_var('func_4032')
func_4033_call = mutated_mod.get_global_var('func_4033')
call_7830 = relay.TupleGetItem(func_4032_call(), 0)
call_7831 = relay.TupleGetItem(func_4033_call(), 0)
bop_7833 = relay.multiply(call_7814.astype('int32'), var_7822.astype('int32')) # shape=(13, 9, 1755)
bop_7836 = relay.multiply(call_7815.astype('int32'), var_7822.astype('int32')) # shape=(13, 9, 1755)
uop_7845 = relay.sinh(bop_7833.astype('float32')) # shape=(13, 9, 1755)
uop_7847 = relay.sinh(bop_7836.astype('float32')) # shape=(13, 9, 1755)
bop_7852 = relay.mod(call_7814.astype('float64'), const_7821.astype('float64')) # shape=(13, 9, 1440)
bop_7855 = relay.mod(call_7815.astype('float64'), const_7821.astype('float64')) # shape=(13, 9, 1440)
output = relay.Tuple([call_7820,call_7830,uop_7845,bop_7852,])
output2 = relay.Tuple([call_7823,call_7831,uop_7847,bop_7855,])
func_7856 = relay.Function([var_7822,], output)
mod['func_7856'] = func_7856
mod = relay.transform.InferType()(mod)
var_7857 = relay.var("var_7857", dtype = "float32", shape = (1, 1755))#candidate|7857|(1, 1755)|var|float32
output = func_7856(var_7857)
func_7858 = relay.Function([var_7857], output)
mutated_mod['func_7858'] = func_7858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7446_call = mod.get_global_var('func_7446')
func_7447_call = mutated_mod.get_global_var('func_7447')
call_7909 = relay.TupleGetItem(func_7446_call(), 0)
call_7910 = relay.TupleGetItem(func_7447_call(), 0)
func_6642_call = mod.get_global_var('func_6642')
func_6643_call = mutated_mod.get_global_var('func_6643')
call_7924 = relay.TupleGetItem(func_6642_call(), 0)
call_7925 = relay.TupleGetItem(func_6643_call(), 0)
func_4404_call = mod.get_global_var('func_4404')
func_4405_call = mutated_mod.get_global_var('func_4405')
call_7939 = relay.TupleGetItem(func_4404_call(), 0)
call_7940 = relay.TupleGetItem(func_4405_call(), 0)
output = relay.Tuple([call_7909,call_7924,call_7939,])
output2 = relay.Tuple([call_7910,call_7925,call_7940,])
func_7951 = relay.Function([], output)
mod['func_7951'] = func_7951
mod = relay.transform.InferType()(mod)
mutated_mod['func_7951'] = func_7951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7951_call = mutated_mod.get_global_var('func_7951')
call_7952 = func_7951_call()
output = call_7952
func_7953 = relay.Function([], output)
mutated_mod['func_7953'] = func_7953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7974 = relay.var("var_7974", dtype = "float64", shape = (4, 11, 8))#candidate|7974|(4, 11, 8)|var|float64
uop_7975 = relay.cos(var_7974.astype('float64')) # shape=(4, 11, 8)
uop_7996 = relay.asinh(uop_7975.astype('float64')) # shape=(4, 11, 8)
output = uop_7996
output2 = uop_7996
func_7999 = relay.Function([var_7974,], output)
mod['func_7999'] = func_7999
mod = relay.transform.InferType()(mod)
var_8000 = relay.var("var_8000", dtype = "float64", shape = (4, 11, 8))#candidate|8000|(4, 11, 8)|var|float64
output = func_7999(var_8000)
func_8001 = relay.Function([var_8000], output)
mutated_mod['func_8001'] = func_8001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7430_call = mod.get_global_var('func_7430')
func_7431_call = mutated_mod.get_global_var('func_7431')
call_8005 = relay.TupleGetItem(func_7430_call(), 2)
call_8006 = relay.TupleGetItem(func_7431_call(), 2)
var_8008 = relay.var("var_8008", dtype = "float32", shape = (13, 9, 5))#candidate|8008|(13, 9, 5)|var|float32
bop_8009 = relay.logical_and(call_8005.astype('bool'), var_8008.astype('bool')) # shape=(13, 9, 5)
bop_8012 = relay.logical_and(call_8006.astype('bool'), var_8008.astype('bool')) # shape=(13, 9, 5)
func_4629_call = mod.get_global_var('func_4629')
func_4631_call = mutated_mod.get_global_var('func_4631')
call_8024 = relay.TupleGetItem(func_4629_call(), 0)
call_8025 = relay.TupleGetItem(func_4631_call(), 0)
output = relay.Tuple([bop_8009,call_8024,])
output2 = relay.Tuple([bop_8012,call_8025,])
func_8028 = relay.Function([var_8008,], output)
mod['func_8028'] = func_8028
mod = relay.transform.InferType()(mod)
mutated_mod['func_8028'] = func_8028
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8029 = relay.var("var_8029", dtype = "float32", shape = (13, 9, 5))#candidate|8029|(13, 9, 5)|var|float32
func_8028_call = mutated_mod.get_global_var('func_8028')
call_8030 = func_8028_call(var_8029)
output = call_8030
func_8031 = relay.Function([var_8029], output)
mutated_mod['func_8031'] = func_8031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5422_call = mod.get_global_var('func_5422')
func_5424_call = mutated_mod.get_global_var('func_5424')
call_8183 = func_5422_call()
call_8184 = func_5422_call()
output = relay.Tuple([call_8183,])
output2 = relay.Tuple([call_8184,])
func_8187 = relay.Function([], output)
mod['func_8187'] = func_8187
mod = relay.transform.InferType()(mod)
output = func_8187()
func_8188 = relay.Function([], output)
mutated_mod['func_8188'] = func_8188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_371_call = mod.get_global_var('func_371')
func_372_call = mutated_mod.get_global_var('func_372')
call_8202 = func_371_call()
call_8203 = func_371_call()
output = relay.Tuple([call_8202,])
output2 = relay.Tuple([call_8203,])
func_8224 = relay.Function([], output)
mod['func_8224'] = func_8224
mod = relay.transform.InferType()(mod)
output = func_8224()
func_8225 = relay.Function([], output)
mutated_mod['func_8225'] = func_8225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4883_call = mod.get_global_var('func_4883')
func_4885_call = mutated_mod.get_global_var('func_4885')
call_8252 = relay.TupleGetItem(func_4883_call(), 0)
call_8253 = relay.TupleGetItem(func_4885_call(), 0)
var_8270 = relay.var("var_8270", dtype = "float32", shape = (13, 9, 9))#candidate|8270|(13, 9, 9)|var|float32
bop_8271 = relay.minimum(call_8252.astype('uint32'), var_8270.astype('uint32')) # shape=(13, 9, 9)
bop_8274 = relay.minimum(call_8253.astype('uint32'), var_8270.astype('uint32')) # shape=(13, 9, 9)
func_7606_call = mod.get_global_var('func_7606')
func_7607_call = mutated_mod.get_global_var('func_7607')
call_8277 = func_7606_call()
call_8278 = func_7606_call()
func_5640_call = mod.get_global_var('func_5640')
func_5642_call = mutated_mod.get_global_var('func_5642')
call_8284 = relay.TupleGetItem(func_5640_call(), 2)
call_8285 = relay.TupleGetItem(func_5642_call(), 2)
uop_8288 = relay.atan(bop_8271.astype('float32')) # shape=(13, 9, 9)
uop_8290 = relay.atan(bop_8274.astype('float32')) # shape=(13, 9, 9)
output = relay.Tuple([call_8277,call_8284,uop_8288,])
output2 = relay.Tuple([call_8278,call_8285,uop_8290,])
func_8346 = relay.Function([var_8270,], output)
mod['func_8346'] = func_8346
mod = relay.transform.InferType()(mod)
var_8347 = relay.var("var_8347", dtype = "float32", shape = (13, 9, 9))#candidate|8347|(13, 9, 9)|var|float32
output = func_8346(var_8347)
func_8348 = relay.Function([var_8347], output)
mutated_mod['func_8348'] = func_8348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_8453 = relay.TupleGetItem(func_1526_call(), 2)
call_8454 = relay.TupleGetItem(func_1527_call(), 2)
func_3938_call = mod.get_global_var('func_3938')
func_3941_call = mutated_mod.get_global_var('func_3941')
call_8482 = relay.TupleGetItem(func_3938_call(relay.reshape(call_8453.astype('float32'), [13, 9, 1])), 0)
call_8483 = relay.TupleGetItem(func_3941_call(relay.reshape(call_8453.astype('float32'), [13, 9, 1])), 0)
func_2643_call = mod.get_global_var('func_2643')
func_2644_call = mutated_mod.get_global_var('func_2644')
call_8494 = relay.TupleGetItem(func_2643_call(), 1)
call_8495 = relay.TupleGetItem(func_2644_call(), 1)
func_5778_call = mod.get_global_var('func_5778')
func_5780_call = mutated_mod.get_global_var('func_5780')
call_8524 = relay.TupleGetItem(func_5778_call(), 0)
call_8525 = relay.TupleGetItem(func_5780_call(), 0)
bop_8534 = relay.greater(call_8494.astype('bool'), relay.reshape(call_8524.astype('bool'), relay.shape_of(call_8494))) # shape=(13, 9, 1)
bop_8537 = relay.greater(call_8495.astype('bool'), relay.reshape(call_8525.astype('bool'), relay.shape_of(call_8495))) # shape=(13, 9, 1)
output = relay.Tuple([call_8453,call_8482,bop_8534,])
output2 = relay.Tuple([call_8454,call_8483,bop_8537,])
func_8545 = relay.Function([], output)
mod['func_8545'] = func_8545
mod = relay.transform.InferType()(mod)
output = func_8545()
func_8546 = relay.Function([], output)
mutated_mod['func_8546'] = func_8546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3433_call = mod.get_global_var('func_3433')
func_3434_call = mutated_mod.get_global_var('func_3434')
call_8599 = func_3433_call()
call_8600 = func_3433_call()
func_1323_call = mod.get_global_var('func_1323')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_8603 = relay.TupleGetItem(func_1323_call(), 0)
call_8604 = relay.TupleGetItem(func_1324_call(), 0)
func_185_call = mod.get_global_var('func_185')
func_187_call = mutated_mod.get_global_var('func_187')
call_8608 = relay.TupleGetItem(func_185_call(), 0)
call_8609 = relay.TupleGetItem(func_187_call(), 0)
func_3093_call = mod.get_global_var('func_3093')
func_3094_call = mutated_mod.get_global_var('func_3094')
call_8612 = relay.TupleGetItem(func_3093_call(), 0)
call_8613 = relay.TupleGetItem(func_3094_call(), 0)
func_2127_call = mod.get_global_var('func_2127')
func_2131_call = mutated_mod.get_global_var('func_2131')
var_8621 = relay.var("var_8621", dtype = "uint32", shape = (1638,))#candidate|8621|(1638,)|var|uint32
const_8622 = relay.const([-9.029371,-5.968480,1.604601,2.433947,0.035805,3.098814,-5.304402,-0.915852,-2.492506,6.533957,-4.982950,-1.823209,8.621669,-6.126393,8.731484,-8.349634,5.853604,5.373293,6.943812,-8.772659,-8.430414,2.393488,5.781142,6.651084,8.702730,2.382433,-0.987221,8.740256,5.605472,-4.328810,0.201276,-8.767518,7.869098,7.051735,-2.507599,6.049953,7.685707,5.948345,9.306111,2.531461,-1.084728,-6.950589,-8.529171,-9.936737,7.014602,-1.192386,1.866750,5.030262,4.824305,-9.584768,-0.402944,-4.315576,-6.115021,9.841980,-8.500527,9.326545,4.465805,1.052701,9.224384,8.021095,-7.731483,8.801865,8.189479,2.839403,9.734002,-9.161435,8.265558,-0.835546,3.214047,2.737631,-2.297924,-8.603325,-6.618808,5.861845,1.777304,4.372524,-9.096123,-0.415188,8.105796,-8.369796,2.600711,5.242988,-9.316182,-3.814475,9.863413,3.145607,-9.527273,0.034122,-8.743687,-4.803079,0.823992,8.646897,-5.196895,9.760811,3.928572,8.320005,5.229811,-7.170951,-7.229225,3.808256,-2.835347,7.988234,-2.038060,-9.476265,8.311331,-5.383942,-0.449098,-1.912935,8.676320,-4.386521,-7.907231,8.192574,-3.238341,7.775818,1.943230,-5.193101,1.685143,-3.663927,-7.695326,-6.119572,-1.800191,7.289613,6.578102,8.396351,7.692822,0.547351,4.678303,6.870374,-5.591516,-9.171127,0.942847,-5.081412,-4.012208,-6.407504,6.596235,-0.009838,-3.930823,-0.589345,-5.334641,-7.368247,9.320611,3.335130,9.463011,1.088127,7.693571,9.052035,-7.541035,9.653554,-3.338873,-5.490502,9.735802,5.836760,-8.620075,1.674028,-9.011837,-1.059589,8.785879,-4.110787,7.212418,7.958895,-7.354156,0.014004,-3.983129,7.505986,7.245591,-2.804532,5.384877,-8.089831,3.585362,-6.444311,3.768727,2.377739,-8.158189,8.293053,2.924332,-2.779198,2.713721,8.830897,-3.410696,8.403185,-5.592802,-6.378101,3.687107,5.811047,-2.716417,-3.590352,-0.752173,7.946386,-1.709349,-1.817040,5.622520,3.582777,7.173255,-0.656449,8.577834,8.942270,4.062705,0.178776,-0.416426,5.268499,-4.831723,-6.390578,5.920638,4.354851,2.417920,-1.673935,-1.388618,9.153817,-5.394457,-4.634392,5.056048,4.072707,2.815886,-8.500969,8.198674,5.108766,1.329132,-7.869709,7.127254,-9.916340,-8.207888,2.776771,-3.365709,-5.427967,-9.003978,2.958978,-5.016526,-6.835294,0.144647,5.572323,-4.714743,8.737103,-4.940491,-1.817776,5.420394,-2.710142,4.327249,3.210751,5.632591,-8.073757,-9.403414,4.770000,-3.081044,-8.208096,-2.587182,-4.860307,-1.264581,4.704647,-6.197893,-3.029042,-5.305735,8.604774,-5.342509,-6.061511,-0.747059,6.476750,-0.006271,3.048300,-1.693485,-8.009967,4.770335,6.720785,-4.150720,-5.477386,1.516609,8.692565,-1.669205,1.823818,3.479476,-8.941522,8.624205,-3.148662,-3.942674,-4.658736,3.877650,-4.502948,-1.242902,6.355266,-0.560528,7.649597,-1.163224,8.849739,1.762468,-6.807881,-9.758282,-7.253854,-9.953514,9.899956,-9.853913,-0.637939,0.729856,-8.773779,-6.803565,-8.969779,8.615148,-2.602430,-7.960720,-1.674449,7.666917,-5.680026,3.645447,0.205059,5.593736,9.783076,-6.453521,-2.788920,-2.936516,1.413574,-6.568206,5.337687,4.863239,1.500932,2.646904,9.791080,-0.774281,9.627548,-8.091957,-4.165510,7.598610,9.245985,1.397733,8.771836,-6.606125,-0.449536,1.261460,5.541515,-0.232849,-0.195518,-1.939526,-2.173199,-8.969119,7.603402,-2.380554,-6.793374,2.454063,5.910211,1.075379,-6.342380,-9.186795,-6.287025,-9.004572,-8.076686,9.621786,-2.806646,4.108630,-3.427200,-6.767552,-8.340578,5.929697,1.297465,1.508720,1.695264,5.621011,-1.212353,5.735757,2.149058,-4.971766,-6.589114,9.874795,-5.322269,1.996302,-5.367742,-2.263578,-1.286233,1.914567,-8.075158,-8.517840,-8.223609,2.816390,6.254437,3.776132,-6.291761,4.615112,0.685910,5.058808,6.423702,2.108911,4.715988,-1.181156,6.097304,3.370091,-8.925549,-2.037880,2.616229,-8.974482,-9.723233,-1.750871,0.826730,6.412937,-7.457050,-4.668406,2.937654,3.655544,6.670950,-1.468701,1.936533,-2.791138,3.375049,-4.323790,-7.458354,-9.483843,2.012866,0.558420,-4.493084,5.166325,-8.373934,-0.021846,2.414467,-5.074959,1.577016,-3.163762,-3.605158,6.375849,7.029550,-4.672904,-0.633934,-5.448823,4.590733,-2.732672,-0.607449,-6.988761,-0.694936,-0.426431,-3.872806,-6.544966,1.519632,4.472460,-4.039057,7.198071,-5.536166,1.015821,-3.698898,-3.274744,-7.781546,6.707143,1.511253,5.766570,-7.516022,6.274536,-6.420080,9.836142,-4.093602,4.231621,2.055297,-9.158547,-5.826401,-1.051214,2.988155,0.211341,4.592244,-5.407788,-4.748231,-0.119097,4.260193,-9.836270,-8.229021,5.353634,-4.567271,6.982338,-4.658520,9.600270,3.008654,3.520689,0.909767,-9.930247,-4.151028,8.284252,-0.523060,8.066630,7.181058,6.925042,8.377335,4.168520,4.439633,3.116355,-1.945723,6.164348,-0.181594,2.216211,6.981133,7.142293,-1.448986,-2.092261,-1.064035,4.587333,0.817899,8.459338,8.160403,-4.959238,7.069714,-8.549628,8.256307,-2.162719,9.443256,9.790287,9.138985,-6.199574,3.743787,1.752825,-1.263908,0.642949,1.096507,0.631688,8.536063,-6.152330,7.288047,1.395346,-0.031486,5.243586,2.668189,-6.136533,1.227807,-7.773178,7.765873,-8.707375,-7.708242,-7.939561,1.349223,0.933571,0.688285,8.042162,-7.679722,3.217787,-4.495272,-0.701758,5.541864,6.512800,6.441568,2.373584,0.612906,8.692762,-0.215524,4.700677,7.103775,-2.002473,-2.221856,6.565398,-1.269604,4.272061,9.352523,-2.312745,-9.570064,4.997349,-6.153850,0.264003,1.620344,9.951609,-0.948994,2.532364,1.590641,-2.662220,0.580132,3.198978,3.275983,7.199472,-5.258740,3.824588,6.624279,7.655980,-0.927837,2.821795,6.102133,5.933173,4.462887,1.205516,-0.811886,0.137270,6.517017,-4.024291,0.148528,-5.711496,2.027434,1.689356,-5.909598,-4.487911,4.107577,-9.773299,9.815483,-1.531705,-4.074840,6.582306,5.517800,2.395679,0.378613,2.476395,7.329647,9.962781,-3.086821,7.742989,9.685845,4.425032,6.158373,2.459747,0.998838,1.053027,0.260371,-5.412083,4.644806,2.024167,7.037044,-9.308221,-6.712166,-7.910315,-0.842078,-8.066509,0.384626,-2.214929,2.823298,4.018846,3.650733,4.654849,-5.542782,0.147032,4.143278,-1.431667,-0.450158,0.943191,-4.474447,7.407836,9.005232,-2.041771,9.386086,2.049726,-3.474009,0.888030,7.257358,-6.648084,-2.680800,-4.414920,3.071461,4.533456,9.756826,-1.530993,-9.805260,-0.523627,4.377829,-4.229157,0.873510,-4.534591,6.018590], dtype = "float32")#candidate|8622|(640,)|const|float32
call_8620 = relay.TupleGetItem(func_2127_call(relay.reshape(var_8621.astype('uint32'), [13, 9, 14]), relay.reshape(const_8622.astype('float32'), [640,]), ), 7)
call_8623 = relay.TupleGetItem(func_2131_call(relay.reshape(var_8621.astype('uint32'), [13, 9, 14]), relay.reshape(const_8622.astype('float32'), [640,]), ), 7)
bop_8626 = relay.equal(call_8608.astype('bool'), call_8620.astype('bool')) # shape=(13, 9, 640)
bop_8629 = relay.equal(call_8609.astype('bool'), call_8623.astype('bool')) # shape=(13, 9, 640)
bop_8630 = relay.floor_divide(bop_8626.astype('float32'), const_8622.astype('float32')) # shape=(13, 9, 640)
bop_8633 = relay.floor_divide(bop_8629.astype('float32'), const_8622.astype('float32')) # shape=(13, 9, 640)
uop_8636 = relay.erf(var_8621.astype('float64')) # shape=(1638,)
output = relay.Tuple([call_8599,call_8603,call_8612,bop_8630,uop_8636,])
output2 = relay.Tuple([call_8600,call_8604,call_8613,bop_8633,uop_8636,])
func_8643 = relay.Function([var_8621,], output)
mod['func_8643'] = func_8643
mod = relay.transform.InferType()(mod)
mutated_mod['func_8643'] = func_8643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8644 = relay.var("var_8644", dtype = "uint32", shape = (1638,))#candidate|8644|(1638,)|var|uint32
func_8643_call = mutated_mod.get_global_var('func_8643')
call_8645 = func_8643_call(var_8644)
output = call_8645
func_8646 = relay.Function([var_8644], output)
mutated_mod['func_8646'] = func_8646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7155_call = mod.get_global_var('func_7155')
func_7156_call = mutated_mod.get_global_var('func_7156')
call_8657 = relay.TupleGetItem(func_7155_call(), 2)
call_8658 = relay.TupleGetItem(func_7156_call(), 2)
var_8664 = relay.var("var_8664", dtype = "bool", shape = (13, 9, 1440))#candidate|8664|(13, 9, 1440)|var|bool
bop_8665 = relay.divide(call_8657.astype('float32'), relay.reshape(var_8664.astype('float32'), relay.shape_of(call_8657))) # shape=(13, 9, 1440)
bop_8668 = relay.divide(call_8658.astype('float32'), relay.reshape(var_8664.astype('float32'), relay.shape_of(call_8658))) # shape=(13, 9, 1440)
uop_8671 = relay.log2(var_8664.astype('float32')) # shape=(13, 9, 1440)
func_631_call = mod.get_global_var('func_631')
func_632_call = mutated_mod.get_global_var('func_632')
call_8675 = relay.TupleGetItem(func_631_call(), 1)
call_8676 = relay.TupleGetItem(func_632_call(), 1)
bop_8683 = relay.power(call_8657.astype('float64'), relay.reshape(var_8664.astype('float64'), relay.shape_of(call_8657))) # shape=(13, 9, 1440)
bop_8686 = relay.power(call_8658.astype('float64'), relay.reshape(var_8664.astype('float64'), relay.shape_of(call_8658))) # shape=(13, 9, 1440)
var_8691 = relay.var("var_8691", dtype = "float32", shape = (13, 9, 1440))#candidate|8691|(13, 9, 1440)|var|float32
bop_8692 = relay.bitwise_or(bop_8665.astype('uint8'), relay.reshape(var_8691.astype('uint8'), relay.shape_of(bop_8665))) # shape=(13, 9, 1440)
bop_8695 = relay.bitwise_or(bop_8668.astype('uint8'), relay.reshape(var_8691.astype('uint8'), relay.shape_of(bop_8668))) # shape=(13, 9, 1440)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_8707 = func_1972_call()
call_8708 = func_1972_call()
output = relay.Tuple([uop_8671,call_8675,bop_8683,bop_8692,call_8707,])
output2 = relay.Tuple([uop_8671,call_8676,bop_8686,bop_8695,call_8708,])
func_8709 = relay.Function([var_8664,var_8691,], output)
mod['func_8709'] = func_8709
mod = relay.transform.InferType()(mod)
mutated_mod['func_8709'] = func_8709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8709_call = mutated_mod.get_global_var('func_8709')
var_8711 = relay.var("var_8711", dtype = "bool", shape = (13, 9, 1440))#candidate|8711|(13, 9, 1440)|var|bool
var_8712 = relay.var("var_8712", dtype = "float32", shape = (13, 9, 1440))#candidate|8712|(13, 9, 1440)|var|float32
call_8710 = func_8709_call(var_8711,var_8712,)
output = call_8710
func_8713 = relay.Function([var_8711,var_8712,], output)
mutated_mod['func_8713'] = func_8713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4589_call = mod.get_global_var('func_4589')
func_4590_call = mutated_mod.get_global_var('func_4590')
call_8861 = relay.TupleGetItem(func_4589_call(), 0)
call_8862 = relay.TupleGetItem(func_4590_call(), 0)
output = relay.Tuple([call_8861,])
output2 = relay.Tuple([call_8862,])
func_8871 = relay.Function([], output)
mod['func_8871'] = func_8871
mod = relay.transform.InferType()(mod)
mutated_mod['func_8871'] = func_8871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8871_call = mutated_mod.get_global_var('func_8871')
call_8872 = func_8871_call()
output = call_8872
func_8873 = relay.Function([], output)
mutated_mod['func_8873'] = func_8873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3455_call = mod.get_global_var('func_3455')
func_3456_call = mutated_mod.get_global_var('func_3456')
call_8892 = relay.TupleGetItem(func_3455_call(), 0)
call_8893 = relay.TupleGetItem(func_3456_call(), 0)
func_8028_call = mod.get_global_var('func_8028')
func_8031_call = mutated_mod.get_global_var('func_8031')
var_8909 = relay.var("var_8909", dtype = "float32", shape = (585,))#candidate|8909|(585,)|var|float32
call_8908 = relay.TupleGetItem(func_8028_call(relay.reshape(var_8909.astype('float32'), [13, 9, 5])), 1)
call_8910 = relay.TupleGetItem(func_8031_call(relay.reshape(var_8909.astype('float32'), [13, 9, 5])), 1)
func_7043_call = mod.get_global_var('func_7043')
func_7045_call = mutated_mod.get_global_var('func_7045')
call_8917 = relay.TupleGetItem(func_7043_call(), 3)
call_8918 = relay.TupleGetItem(func_7045_call(), 3)
func_5829_call = mod.get_global_var('func_5829')
func_5832_call = mutated_mod.get_global_var('func_5832')
const_8935 = relay.const([-1.563220,6.799597,1.826576,-1.547460,7.015421,-6.824746,-8.035516,2.210943,-6.728806,9.173552,9.097575,4.619443,-5.602790,-0.187612,-4.472283,-0.386947,3.752504,-2.457763,3.604269,-3.295859,1.987818,-2.846309,-9.160104,-9.729923,-9.617869,5.886368,3.566474,2.490865,3.239194,2.649934,3.750196,2.689540,6.752604,2.762534,-1.126579,7.277773,1.769072,-5.595909,8.067638,-4.860315,-9.104207,-3.828515,-0.972921,9.409956,1.994962,4.392493,5.180103,-4.058959,-6.244211,4.276096,5.570411,-1.795775,4.384022,-0.774138,-8.108278,-1.296977,0.311276,-8.916617,-1.501398,2.588389,-1.429205,-0.122229,2.210395,-6.989470,5.770720,2.459255,-6.264327,9.979327,-8.241826,9.424000,-3.243908,1.590850,-5.294720,6.394326,5.747992,-7.031850,9.586148,1.112102,8.912928,2.251931,-7.649148,2.017961,-2.530041,-7.755555,7.129121,5.993282,8.740338,0.952923,-0.979219,-3.690830,2.476296,7.880437,9.325356,-1.514092,-6.706640,1.570120,-4.247285,-8.213951,7.625082,3.492876,-6.201699,-0.167934,3.301233,8.459874,-5.823151,0.900671,-4.106665,7.335895,-3.645627,2.862887,2.048188,4.556364,0.290967,-8.134789,-1.870740,6.547420,7.182690,-9.356070,3.618495,-6.068861,3.561234,-6.526111,0.185703,9.272863,8.183793,-8.221164,-8.122602,-6.732495,3.194549,-5.460883,-7.837536,-3.162709,-6.608134,-2.382037,-7.125322,5.044795,-3.508562,-2.637137,7.081954,8.485402,-1.326830,6.099891,3.028511,-3.710678,1.218053,-4.204896,6.178483,7.882899,4.867288,7.939169,-5.046258,8.845846,-0.369587,-0.517197,-3.373859,-9.839875,-2.304293,5.628195,1.972843,-6.123352,-0.845732,-5.874826,-7.116499,2.374934,6.216784,0.427966,-4.504954,5.899810,-0.885856,-4.999961,8.326572,9.375029,0.081227,-8.587977,2.005467,7.745046,6.764286,1.699136,0.287113,-3.921847,0.239181,-0.817803,-6.906068,3.748391,-6.230419,5.137815,-6.807830,6.601546,0.105135,7.111263,-3.158097,1.916207,-8.701089,4.418769,5.102913,0.817304,-4.460407,-4.056737,4.331631,3.156915,-7.012215,7.249414,-7.478107,-0.198739,-3.472502,-6.279450,-2.168482,9.296223,-6.313021,-6.951531,-8.840228,-8.517461,1.118820,1.884431,-5.288975,-3.103491,-1.778345,-6.605021,-3.648285,-7.579569,-4.086926,-5.241417,-2.907173,6.027766,-4.074106,5.007388,6.320196,8.140991,-3.166882,2.081718,-0.320948,3.881205,-4.179434,5.112475,-9.758072,0.868537,-9.391385,8.868110,2.579570,8.709600,-4.929796,-1.303450,-2.146145,2.882006,9.779465,-0.867874,-6.010859,-1.645673,1.325463,-0.811353,1.409899,-6.590714,3.792955,6.570037,-3.554118,-9.146146,8.797612,4.810804,8.362296,-2.324911,0.958847,-7.421055,4.104488,-8.729857,-7.616467,-4.434321,6.943772,0.999813,5.120217,5.541865,1.492259,-5.608383,4.899374,-7.779719,-4.314541,9.134989,7.445180,-6.569967,-4.616258,5.071090,7.134637,-1.883585,-1.857296,7.206364,-6.717894,-5.082286,-1.471715,-7.786560,-1.134331,-7.981237,-7.599946,-2.938325,5.116224,-4.113287,-7.003610,-1.101475,4.748499,-2.627100,-2.590887,1.198188,-9.082387,-0.089542,6.077912,-7.502179,-0.016479,-9.683169,-4.299935,-1.032655,0.888320,2.692337,8.030703,4.036010,6.382044,-4.419298,3.152283,-8.231157,2.108828,5.941433,-8.070231,-9.682000,-5.661356,0.007620,-0.069064,6.224063,-5.471685,1.720363,-9.559127,-1.131248,-3.352352,-3.309059,6.798180,3.240428,5.007573,2.359602,9.529216,-9.005160,-0.439360,-4.051716,-8.096552,5.829829,8.259483,-3.896710,4.576976,3.257389,5.179741,-0.206052,-7.137252,-4.417417,-7.891088,2.837369,8.112460,0.109975,3.684018,-6.978162,5.963877,-5.347996,-6.325758,3.618181,-1.651076,5.780864,-2.540587,-2.256019,-6.434975,-2.492408,-0.949616,-9.871037,-5.814980,5.662217,9.759070,7.136026,0.606001,6.064608,-2.191689,-9.904427,8.115969,-3.115664,1.778070,5.838991,1.558589,-3.761855,2.377627,-8.644497,-3.862434,-2.574680,8.501294,8.665203,4.029319,1.180657,7.355935,-0.466210,9.850177,-7.773948,8.619163,-4.707580,4.937841,-7.858760,5.494512,-4.717656,6.583156,-5.663916,-3.956669,5.421700,-2.789784,5.932801,-7.269202,1.260534,3.724130,-1.050050,9.000622,5.504945,8.769732,5.534561,-2.425501,9.733344,-5.309323,4.753911,4.838840,8.619324,3.920383,7.840435,-2.792958,7.034901,-9.012830,4.026202,1.335840,-4.462697,-0.484229,7.142356,-4.201914,-4.292176,-7.862124,8.253909,9.175420,-2.184155,-4.115603,-2.605258,-5.145545,-0.813200,-3.480517,-1.995982,-6.061712,-6.349762,-6.628309,-5.662227,-5.857620,-1.251586,-5.742407,-3.554343,-3.224338,-2.239705,-1.457796,9.994026,-3.206131,7.027557,3.662962,-7.617806,4.624843,3.071207,7.389331,-3.926621,-1.546904,-0.616832,-4.405460,-7.070972,2.761747,9.159781,-3.783162,-1.394612,-7.484643,0.203998,8.590987,-2.426896,-0.763327,0.475798,8.750068,-8.289904,-9.132756,-2.411948,9.322637,4.169985,3.595068,6.299262,2.038096,-3.621784,0.989849,-3.866181,-8.501074,3.366738,-7.559556,-1.434144,-0.628112,9.208892,5.391197,-7.868337,7.482164,-7.246181,-2.814187,-4.968174,2.451109,-5.450445,-8.916772,-4.967858,0.446849,2.745328,-5.004505,9.558248,-3.876048,5.361576,-3.603761,2.363278,6.602005,-7.394994,6.559768,5.150306,8.374116,6.455320,-7.202860,-6.521607,-7.261689,9.413070,7.888383,1.832624,-9.966567,-2.482550,-5.130342,-0.119400,5.593852,-1.685554,3.165778,5.816783,7.033990,-1.337904,-2.867044,6.512812,-1.789729,5.347896,4.890107,-2.317467,5.943490,-8.104234,-7.699243,7.809713,4.351642,-6.340210,-3.198247,6.533909,-1.150980,8.627113,2.366893,7.307644,-3.190289,6.717938,-2.275582,7.094611,-2.354457,6.649987,-5.948661,-4.910745,-8.248744,-7.864789,7.080695,-3.100629,4.572832,-2.587327,-5.486884,-0.162129,0.195193,-3.138802,1.408558,9.380120,0.290943,-0.402398,-9.502838,7.748815,3.538796,9.303227,-1.128982,0.832589,3.263152,-7.639535,2.458598,-1.229323,-3.669131,-7.737824,-5.346221,-3.502802,0.893631,5.551818,8.069236,-0.686592,-1.753236,6.473195,-3.795526,-9.150459,5.883068,4.131519,-6.011021,1.469826,5.792315,-0.867289,5.101072,9.029778,-5.461152,-1.047866,-1.879504,-5.072117,-0.028263,6.514694,-4.176962,3.630664,-1.756847,1.680565,-9.224662,8.827881,-7.290491,-7.836314,-1.011759,-4.002663,-9.902138,4.617659,-2.349312,-0.055223,6.841491,1.635879,0.331349,7.531895,1.192604,-7.684399,0.916220,3.620473,-5.821315,-0.450388,-7.579688,3.146579,6.295124,7.633962,-6.057441,8.759703,5.714843,-2.097175,0.777816,-7.090921,-2.222343,-3.402009,-6.360019,2.931130,7.415498,-1.598901,3.083633,5.494322,-5.482019,-6.573895,-8.892788,-1.309988,-8.853046,-3.106175,0.491729,-8.298997,-7.701067,2.351555,7.828804,5.673336,-0.876704,-3.753770,9.756532,3.770316,-3.476539,-8.782151,2.952140,-7.711912,6.028035,1.605529,7.455189,-6.180114,-7.531177,-2.328870,0.089678,1.332669,8.131120,0.093852,5.276482,-5.451253,-9.513466,-7.870940,-9.194126,8.731556,0.897924,-3.101492,-5.047250,-1.325891,-6.543949,-4.953008,-5.398932,-5.536900,4.560885,-2.826346,-5.847102,-5.683500,-5.488245,-4.711503,5.484426,-3.125527,-4.548447,9.682022,-1.952845,5.020470,9.000348,-5.429858,5.549346,0.553736,-8.791846,5.496600,7.721258,3.458481,-4.333260,-4.679409,2.093763,9.793475,8.899999,-8.039980,-8.097841,-7.318700,-0.392569,-9.840925,4.204899,-4.810842,6.797719,-2.625569,-1.701851,-9.901852,8.055958,-7.027037,-4.372253,-5.621809,1.175093,6.775568,5.758789,6.807921,-3.414415,9.629294,4.284524,1.600038,-1.947303,1.348801,5.109512,9.954952,-4.195504,7.593910,6.702297,-3.911613,-9.678970,2.914342,-9.938711,3.815491,-1.932640,-0.205303,7.990919,-1.317764,-7.525469,-9.434828,-8.969684,-1.590280,5.510624,5.379882,-3.399346,9.244008,0.328450,-3.893196,6.164881,-2.220150,-3.040519,-9.128620,-3.821202,0.698683,-3.585774,-2.117534,-3.391076,-6.923776,-9.447565,-5.386412,7.702880,2.451829,-1.965380,-0.087759,-7.022665,9.632647,-9.540010,-4.773363,3.234777,8.970536,8.124874,-3.412806,-6.978530,9.333265,-2.046281,6.770390,-3.637444,-5.404414,-5.457394,-8.335242,2.568856,-0.132352,3.139185,-2.984533,-5.871496,8.785428,4.009683,3.386431,-1.065579,-6.265616,2.742050,-7.482283,-3.579230,-7.349589,-7.878765,2.974838,8.284662,4.944135,-9.730889,7.896999,6.221495,-8.385496,-1.405532,-1.475676,5.145456,0.438611,9.826894,-7.431380,-9.885102,-6.213230,5.545023,-7.615230,6.100932,-2.135812,3.154948,6.795221,-3.016160,8.348256,6.042793,6.426704,-2.988907,2.348551,-8.773824,7.608851,0.432230,8.574717,-2.655875,0.410142,8.773158,2.306523,2.976752,0.876521,1.440246,-1.433591,0.975585,0.892829,-7.502361,8.299750,-8.669657,3.456030,-6.502229,-5.561800,-6.794429,2.100907,9.394914,-9.197263,1.507895,-7.155220,-8.233504,7.448028,-4.167392,4.001815,-4.491727,-0.770737,2.187458,-4.036938,-8.959275,-2.178201,-0.108633,7.745941,8.237751,-7.673772,6.298790,7.905382,3.043678,1.430951,0.466808,-1.305016,9.989184,-7.584097,-3.569325,8.718862,1.745185,8.140437,7.674803,-5.875086,-9.298722,9.444118,5.243019,6.276964,9.365162,3.070578,5.100893,-2.958998,-3.121000,8.552309,2.381839,2.826168,8.923790,-9.635710,3.619414,7.590567,5.992325,-1.805742,4.049016,4.660228,-2.522201,5.517473,-5.310843,5.022247,-2.524756,2.306076,3.127487,-1.389978,6.970693,9.944719,6.550865,-4.282835,0.830914,-2.526239,-5.024539,1.320504,-1.434132,-0.608310,6.248869,0.205382,9.557517,8.134553,1.817283,2.504870,3.773886,-1.001224,6.808484,8.582523,0.478459,3.658221,-2.015926,-3.784123,2.162291,3.582464,-9.171464,-5.018329,-5.018411,-7.451982,6.717552,-4.050690,-6.388539,-1.893827,-9.748667,-8.322115,7.223355,9.482573,2.473872,-8.352473,1.675695,7.651007,-8.415939,8.641802,9.450213,-2.908591,1.639752,7.104059,4.842346,3.882540,-7.199727,1.227637,1.118719,3.273317,3.675209,6.923886,5.199493,-4.502656,-4.296620,-6.506793,-5.666576,-7.113295,-6.335257,7.748508,0.349614,6.831925,9.335441,4.636771,9.668173,6.145724,-1.008545,6.259455,9.814364,2.649770,6.571050,1.329084,1.985116,9.342182,-7.489921,6.874668,0.350224,5.704558,-2.547603,5.290931,2.800772,-1.147967,3.837280,2.965721,1.399927,-9.812045,9.743681,-8.625366,-6.312611,-0.984927,2.197045,-9.221915,-2.540205,5.676385,6.494021,-5.349973,6.437245,-6.187301,3.865303,1.494717,7.172692,1.677343,3.131402,2.131269,-1.499233,-1.484287,9.188458,-2.217949,-8.777087,-5.661421,6.099484,-1.391861,3.908675,8.254754,0.888451,-2.306149,0.929250,4.323987,1.922160,-9.617569,-4.833942,5.050732,4.078194,8.264773,6.842262,6.193624,-2.991359,9.215475,6.766529,-2.409042,7.499079,3.091640,1.528858,-2.527797,9.789509,-7.413337,4.661677,4.682025,4.512283,8.622409,5.860600,9.301804,-5.885034,3.583082,-5.079785,-6.677760,-9.196957,-6.402127,-4.167700,1.670467,0.953625,3.895854,2.339630,8.475820,3.670249,-0.138175,-7.500377,8.663557,-4.377361,-6.461615,-5.010630,5.215861,-8.529049,-0.935637,-3.041236,-5.736705,1.235948,-7.629923,-4.021330,-2.457506,-1.711079,-4.463358,-9.402896,-3.204936,4.662531,6.323088,3.413394,-2.255469,-5.871245,9.554180,-2.332556,-7.203479,2.805685,9.785172,0.431910,-2.216150,-6.358200,-5.890852,-5.974094,3.012436,7.106313,5.026155,9.082877,-4.773722,9.678834,-8.076078,1.125552,5.700225,-6.325796,-2.184412,-1.506861,3.431447,-9.395645,-8.852219,-9.177526,-0.167536,-2.051902,9.176391,9.397885,-1.027612,2.160284,5.236028,1.452191,6.026407,0.848596,7.781297,-4.825391,-0.533125,-6.080542,9.381454,-2.960292,-8.706816,-1.991143,2.397504,4.454616,-1.105716,-0.351091,8.907402,-2.745153,4.349792,5.123482,-5.231972,-5.073058,-1.005908,5.062363,5.791598,5.800514,-3.975174,6.994762,7.941323,8.485787,1.954176,3.396898,-7.893028,-0.877526,5.096073,-4.614401,2.732075,-7.527064,-6.823691,-4.309331,-5.791362,1.344614,8.965685,-1.047622,-8.051244,-3.910729,5.611983,-4.061540,0.902061,-6.470745,-8.044631,-3.822761,4.076111,6.878319,-4.659906,0.517080,6.947190,-7.371982,-7.337642,-7.140159,-0.983094,-9.585771,-2.919733,1.123293,1.684988,4.248887,6.296291,-1.950017,-9.350380,-6.550506,3.052950,3.210599,-5.930078,9.261035,-1.544702,0.111496,-3.483425,9.075429,3.999286,-4.777016,-0.602146,-8.436436,-5.201675,-6.000315,0.496569,7.589665,-2.560750,4.067830,-4.289450,5.869571,-6.428470,-5.949162,4.398050,-6.063581,-9.033236,2.118670,-1.823624,-4.177170,-0.108683,0.227825,2.894763,-6.059429,-7.889509,1.809658,-1.062274,4.188290,5.860881,0.831546,5.877294,4.814682,4.056049,-4.073162,7.376249,-8.127511,3.347182,5.426883,-6.016798,1.844102,5.028417,-3.261945,7.296916,3.783013,1.027548,1.714986,-4.671259,-7.683854,-8.476683,0.322840,-0.990736,6.160495,2.760245,-9.894811,8.820344,-7.477344,-7.639852,-0.725701,0.856800,9.888611,3.699262,9.935514,3.764839,3.102869,0.391784,8.439530,-8.574015,5.883710,7.987368,9.952185,9.295054,-4.294921,-8.309344,-0.337051,-0.641247,-0.392586,-7.842984,2.977970,-2.898918,3.458419,4.303783,8.511717,-7.100856,8.454001,-6.563116,-2.072689,8.825929,-8.956340,4.033940,3.703760,-9.621065,6.914544,9.913539,-8.373873,3.907856,6.883920,7.186431,-3.358650,-5.101988,3.555535,1.476533,-1.189648,-6.658256,-0.203119,1.001226,7.090600,-0.774697,1.898070,7.655778,5.260982,0.625012,6.044469,1.903676,-7.733349,-3.674980,-4.644919,2.092738,-5.364925,8.267731,-1.794148,-0.613488,-6.049095,-3.877766,-3.670404,-5.611501,4.969462,8.815619,-0.584523,-4.679314,-1.747899,-8.971758,-5.346041,1.441338,-7.109537,-0.634471,-4.241332,-8.354996,9.941194,-4.551567,0.389215,1.331829,-1.451713,5.477853,5.408997,-0.599457,-6.556001,-5.470898,-9.462562,6.357483,0.684976,4.172955,-7.692610,-0.340544,7.957895,-3.324246,0.451102,7.875009,-6.255043,-5.765744,-1.008811,9.399318,-2.166402,-7.625493,5.443449,2.711016,2.551132,-0.691732,-6.830094,6.000467,2.522554,-4.565252,1.836390,9.843834,4.364178,6.900159,-8.576727,-5.468669,-2.256160,2.661540,9.264137,-7.632873,-5.958839,-3.465921,-2.264341,-4.320931,8.581799,-9.119045,-2.286335,-5.292222,-8.368420,0.298778,-0.705494,1.809248,-4.972741,9.843994,4.604580,-1.338912,-7.541178,-9.168710,-5.381620,6.795010,-8.605948,-4.088255,8.383622,-0.265693,-9.585257,-4.920541,9.618739,-1.655024,-2.543626,3.226108,1.501518,2.489424,7.331249,-1.529675,-9.168435,3.821024,-4.410121,1.426717,0.672685,7.532683,-8.032953,-5.875541,7.384851,9.313421,-1.756738,6.882912,6.504073,-4.931155,-3.498436,-6.242007,-1.698500,1.767189,-7.433606,-3.484154,-1.825876,0.821000,1.749845,4.633107,-8.505067,-1.218119,5.442384,5.968518,6.200997,2.316665,-8.419632,-4.893263,-1.814721,4.142547,0.886908,-1.717489,8.207761,-0.255675,8.385984,1.390490,-4.766131,6.292425,3.092656,-6.206062,-9.821947,2.393432,-3.031223,2.532836,4.407846,9.933292,-1.687817,0.279777,4.069153,-2.179806,2.282717,9.209344,7.626405,2.486156,4.990189,2.281620,-5.474721,-3.800614,1.439967,2.693913,6.270599,0.585520,-1.380003,4.886460,-3.644647,-9.198136,-7.230574,8.425083,-2.584008,-8.308785,5.088572,6.523652,-9.047290,-8.233490,5.561312,3.620568,-4.099287,-9.320558,1.976837,-7.836192,4.445418,4.755121,-2.525279,-3.139088,7.797506,-1.286909,-9.653571,-7.787374,-9.803540,-2.200867,-1.188301,-2.834163,-9.902521,9.346045,-4.439796,6.503675,0.054935,4.475300,-5.238350,-5.108340,5.811405,-9.734202,5.147594,-0.686600,8.832267,1.948243,-0.138430,-4.126805,6.775028,-1.154779,8.222096,3.685318,-5.608606,3.330723,-2.614499,2.126033,-1.038164,-3.426182,-3.873324,5.507974,7.506037,-1.386225,-7.944214,8.054881,-4.161432,-5.100472,5.505141,-7.206711,-8.495635,-2.015460,-6.220175,-9.575607,8.878401,-0.042622,-0.280899,3.273132,-1.491033,1.811220,-4.001732,-8.714267,9.929367,1.898014,4.927511,-1.973004,8.836515,-3.882848,-5.255786,-8.952956,6.477324,-2.916276,2.609942,-9.427783,6.907839,-8.607603,-6.121136,-4.828056,3.164312,-6.391288,-8.445363,1.697211,-5.007396,8.230119,-4.370193,-3.798566,-0.096630,4.926301,2.112470,0.935248,-6.584748,-4.389224,8.212843,-7.375239,-2.502427,8.531867,5.199761,-8.263719,-6.800769,6.372102,-7.350246,5.587489,-7.719325,-7.652995,-2.562898,-6.493737,3.743053,7.132746,3.827043,-1.002537,-7.110212,-2.076488,-4.436105,5.284467,-8.173469,2.607013,1.554467,0.561308,-6.774415,3.113194,-2.467160,2.189688,-2.260016,-7.986810,-8.442848,-9.735604,-7.895761,-0.490309,0.196086,9.901892,-5.904059,-4.883556,6.450634,4.848808,3.599499,-2.898060,-7.499679,-0.286801,-9.851050,3.619169,3.562663,-2.861405,-6.118357,-2.270338,-2.174626,-7.537565,-9.404253,-4.708944,-7.365626,4.194395,-7.827385,0.905325,9.607817,-1.903588,-3.706069,-5.461613,6.255089,5.802143,-8.835281,6.962907,-5.413003,4.519087,1.065663,-0.016846,-7.127502,0.181534,-5.369378,0.753127,-0.836819,2.272515,0.720896,-1.291437,-3.449001,9.046443,6.237153,-7.995521,-4.649204,1.708540,2.350025,7.483003,1.363735,9.180730,-9.472446,-3.060980,-3.945743,1.973812,5.416662,-2.357823,-7.120251,-4.609187,-3.222863,5.796624,1.626440,-6.294783,-0.326539,-2.264128,3.492710,6.427921,-5.472572,-2.689427,-5.854825,3.085285,-2.238428,3.764815,5.213393,-8.024755,-2.062192,-8.955266,-1.646730,8.634571,-7.774899,4.774573,8.676309,3.457391,-8.231151,-4.325909,-3.247474,-0.370965,0.257365,4.608248,-9.461000,-8.380558,5.959240,-8.411137,-4.847390,-6.890700,8.956868,-4.810681,6.278186,-3.673946,7.740061,-7.761665,-2.408320,-0.931853,-5.659751,-6.993660,-9.423141,-9.473457,1.843583,5.813731,-7.501322], dtype = "float32")#candidate|8935|(1755,)|const|float32
call_8934 = relay.TupleGetItem(func_5829_call(relay.reshape(const_8935.astype('float32'), [13, 9, 15])), 0)
call_8936 = relay.TupleGetItem(func_5832_call(relay.reshape(const_8935.astype('float32'), [13, 9, 15])), 0)
func_6205_call = mod.get_global_var('func_6205')
func_6208_call = mutated_mod.get_global_var('func_6208')
const_8944 = relay.const([-7.416947,3.528287,8.560520,7.853088,4.213383,-9.690623,0.039382,0.770623,-3.196516,-6.727778,9.073601,8.236336,5.566649,8.308581,-0.274847,4.779268,7.947511,-5.943646,6.798644,-3.002542,9.158488,9.451646,1.464548,-1.421898,7.212743,-0.498426,3.862286,8.733956,3.130373,-6.212197,9.242022,-6.497620,-0.456236,2.500727,-9.784628,6.020695,3.964609,-9.116255,2.739729,-4.535757,7.417890,3.606586,-1.811283,8.316605,2.011304,1.327412,-2.847176,3.437873,-6.724781,-9.893067,4.487462,-7.325041,-6.374046,8.331606,7.317979,-3.578151,-3.405302,-6.330214,-7.764176,-6.068053,3.136092,2.955009,-7.130914,-3.040038,1.880132,3.682339,-0.454025,6.213158,3.798702,-7.936450,-5.681281,9.403149,5.263597,6.679059,-4.086249,5.334621,6.095045,4.050771,-3.483845,-1.514421,-1.978557,-9.519266,-4.705961,-3.667603,-1.387548,-3.483710,6.639399,1.337082,5.854334,3.517121,-6.132243,6.925837,2.980230,7.530373,0.627141,8.841872,-0.116470,-7.713965,-5.395645,-6.221263,-9.023208,0.128857,-2.196644,-5.565011,-8.621878,2.896655,-0.963598,-0.428942,5.517417,4.270149,-6.839998,4.801035,-4.832762,8.687933,-9.219496,4.638059,-3.068324,-6.942148,9.704247,7.495089,-3.617570,2.347432,6.611601,-5.298057,5.614387,3.359213,0.030647,-3.867864,5.515351,-2.505521,2.470095,-3.687606,-4.063902,1.215628,3.201901,1.885755,9.183507,-3.129944,8.724958,-3.086622,1.617008,-3.186296,-4.599496,-7.324017,-4.575410,0.693100,1.203154,0.011630,-6.018086,1.168791,6.260469,-0.565994,4.181609,-4.334394,7.763279,-9.261321,-1.479343,5.902538,0.351451,-9.108124,-6.979217,-9.032729,8.522754,-8.312980,-2.839007,3.643545,-3.224467,-5.133987,2.173888,-7.846147,2.739868,5.092146,5.307017,-3.807413,-4.482874,-8.130435,-6.052833,-7.400854,7.291423,-7.139325,6.762699,7.255127,0.923172,7.253938,-9.521699,5.320175,-3.879251,-9.950771,-8.513257,4.416461,4.459574,0.986259,-0.680757,-3.048645,-8.818430,7.847510,-0.402830,-5.739950,-4.632129,-6.448838,8.415042,0.460162,-2.761081,-0.094417,-3.784451,-6.837087,9.576049,-1.672240,6.650543,1.526344,7.926014,1.565009,-0.192477,8.066777,-4.263587,6.668796,4.847119,8.441349,-4.075253,-2.282105,9.072261,0.450422,8.584135,-1.247859,-5.671044,-2.407245,-4.071917,3.392491,3.656701,-3.458094,6.017483,-1.727297,-0.850737,-8.384987,5.384516,3.990025,5.201584,8.230295,-0.561898,-8.910254,-2.274968,-7.013967,-1.254481,3.885018,-2.779706,2.550566,0.567380,6.072823,-5.821273,0.871258,-8.111319,-0.196080,0.056716,-0.956222,-6.199454,-2.801694,-8.778303,6.299027,-7.402402,-1.990624,-8.501434,-3.987195,2.303147,6.351166,-7.545488,7.426073,-7.608548,-6.000190,-1.431954,5.659966,1.782956,2.300168,1.614347,5.579055,9.830519,-5.121962,1.710897,5.032567,-7.216481,-5.334450,5.731954,-0.891551,-8.512463,6.886205,4.411291,3.956279,-7.270458,-3.302026,6.920987,-6.577179,-8.369328,4.031326,3.631323,-1.737952,3.337706,-2.737303,5.278565,-9.335792,-2.932899,-1.789259,1.892608,-2.625171,-6.100412,7.176777,-7.041321,-6.528860,-5.215068,8.472850,-2.582496,-4.638604,-1.741659,6.328333,4.685036,5.002521,1.896539,1.277518,6.942829,2.243477,1.025278,-2.887008,-3.389841,-7.573313,-4.403231,-3.956169,4.944237,-5.506397,-8.519470,3.376995,-6.221636,8.207886,-5.593863,-1.141941,-1.919207,4.534069,-0.694232,-5.654331,-8.494854,4.242926,-6.554841,-8.672468,-0.651352,3.286581,-2.403060,-1.242628,-3.902429,-1.504973,1.499593,-0.085066,-8.429741,1.549346,1.752983,8.227472,-5.288776,-5.318176,6.821256,-2.840405,-4.173646,-2.223036,8.339822,0.113250,-3.136624,-1.023963,-8.985866,1.751139,4.515054,1.524917,-6.458969,-6.161668,2.319776,8.919672,7.494363,1.355351,-4.993086,-3.419812,-4.553494,5.651423,-9.424075,-4.809719,-0.348853,1.582336,-9.924314,8.646192,-5.566509,6.126980,-7.159467,-1.880196,7.270018,2.363949,9.118502,6.296867,1.336275,-7.051132,-9.467768,-7.745530,-2.799594,-9.108462,-5.981551,-6.524185,-0.778960,1.179829,-6.950018,-5.309196,6.514890,6.371472,-6.868022,-5.274720,9.168067,9.348740,-9.648483,2.023701,4.739311,2.836092,2.234191,-9.022862,-3.201261,-2.657623,0.122348,-8.361130,4.033772,2.767440,-9.339251,9.064490,-9.893716,0.830760,5.433688,-7.208783,6.658191,-7.371282,9.113038,-1.400031,-8.259983,-3.712744,3.392288,-6.535208,2.076391,-3.331538,-6.755926,4.449845,-3.627650,4.745178,3.234164,3.606171,5.641119,3.662861,-8.543682,-5.698952,6.138762,4.732132,4.960288,8.790461,3.986541,-3.407517,6.024970,7.437295,9.988559,1.880197,-5.440568,1.188711,9.555868,-6.323689,-6.407875,-5.903772,6.461651,-3.640729,-9.914949,0.097312,-6.133449,3.695839,-1.376932,4.061228,2.072637,-9.435225,4.405026,6.061770,0.868545,4.450397,3.793402,8.494779,4.808877,2.817983,1.526635,1.183057,5.431775,5.394198,2.392629,5.629673,-0.217323,-8.777651,1.002398,-4.857363,5.389348,-1.053716,0.194310,-8.191115,8.387840,-7.730241,-5.366287,-2.821974,-5.837268,3.060996,6.110842,-1.683572,8.218437,4.720251,3.941348,1.094889,7.601361,6.891184,6.633494,6.911770,5.564791,3.757668,-0.645550,5.010771,1.009823,-2.006058,9.811414,-1.987963,-9.765182,3.186395,7.939163,-0.789154,-2.787349,-8.851987,8.864084,5.863966,3.711522,7.961890,-3.416997,5.115604,6.343948,-8.347922,-7.769309,0.749836,0.577083,-0.555162,8.383836,1.807382,-2.718204,5.636432,-3.606819,1.155971,8.472109,2.799028,4.406538,-3.302098,-5.536752,-6.948127,7.417001,6.234632,-0.509419,-1.797354,8.403443,-6.816959,2.513271,4.977013,-4.562596,2.725571,8.495777,7.376075,4.923006,-0.726116,0.153944,2.036235,-2.606363,9.747390,-0.669017,7.548792,8.844185,-0.930097,6.872365,-8.486751,-0.372420,-1.050108,-6.363266,-4.324175,1.305258,-9.501029,5.776528,4.524763,-2.130091,4.902622,-4.916254,-1.400215,-8.162123,-9.429939,3.075848,4.486509,4.073911,2.309747,3.560821,1.087899,-7.982330,3.880060,3.830543,-3.221765,6.815632,3.497511,-1.738841,-8.422891,-0.608125,-9.091041,9.500022,7.564525,1.660089,8.868065,-6.390626,8.380108,-6.651809,7.453118,-4.506630,3.525038,4.095749,2.181306,0.569643,-3.706180,0.898633,0.285612,-3.206410,2.018146,0.037879,-1.998319,5.526794,1.994750,1.413257,-3.251134,-0.901515,0.236905,-0.897952,6.840104,-4.933217,0.436640,-0.836004,7.792535,8.966642,1.727611,9.887696,-8.074336,5.128295,-6.857350,-4.476758,-0.915753,-7.037743,-6.949251,4.972780,-5.918348,3.420978,1.386354,-6.981410,-7.430438,2.305533,2.457272,-0.564851,1.480202,0.544375,-4.257605,-8.131025,-0.482736,-3.297887,9.419949,-3.692319,-8.329350,0.848421,5.107452,-1.962574,1.167531,4.322045,-1.181763,5.231116,-3.424916,5.288165,-2.965390,3.434101,-4.111556,-6.389742,4.370064,-8.146026,-0.009751,5.264242,4.149349,-0.056058,7.849731,9.813837,6.383350,-2.289221,2.030415,-6.899543,5.435767,-4.938890,6.723131,-7.185793,6.356362,-2.904182,-6.947392,-8.149013,9.340684,3.799632,-1.694512,-2.700962,8.856188,4.840481,-1.662347,-0.749381,-8.321356,-8.895636,3.411517,-5.448976,3.200591,5.820209,3.692236,3.162735,-1.380749,5.506943,-4.774522,-7.287235,-1.163378,-7.810312,0.791177,8.803325,-3.772315,5.969175,-4.632960,-9.682234,5.795185,6.377421,7.637175,8.814492,6.654560,8.021964,4.157256,9.912429,1.446013,-3.005305,4.250375,-3.569461,1.290573,7.978858,-6.297636,0.798993,5.785031,-7.902330,-7.254552,-1.362128,-8.060243,6.540849,7.501678,-3.824569,-1.592375,5.958115,-7.022483,3.422363,-2.199152,8.780572,5.860722,-0.758634,7.523502], dtype = "float32")#candidate|8944|(756,)|const|float32
call_8943 = relay.TupleGetItem(func_6205_call(relay.reshape(const_8944.astype('float32'), [14, 6, 9])), 1)
call_8945 = relay.TupleGetItem(func_6208_call(relay.reshape(const_8944.astype('float32'), [14, 6, 9])), 1)
output = relay.Tuple([call_8892,call_8908,var_8909,call_8917,call_8934,const_8935,call_8943,const_8944,])
output2 = relay.Tuple([call_8893,call_8910,var_8909,call_8918,call_8936,const_8935,call_8945,const_8944,])
func_8970 = relay.Function([var_8909,], output)
mod['func_8970'] = func_8970
mod = relay.transform.InferType()(mod)
mutated_mod['func_8970'] = func_8970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8971 = relay.var("var_8971", dtype = "float32", shape = (585,))#candidate|8971|(585,)|var|float32
func_8970_call = mutated_mod.get_global_var('func_8970')
call_8972 = func_8970_call(var_8971)
output = call_8972
func_8973 = relay.Function([var_8971], output)
mutated_mod['func_8973'] = func_8973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5640_call = mod.get_global_var('func_5640')
func_5642_call = mutated_mod.get_global_var('func_5642')
call_9010 = relay.TupleGetItem(func_5640_call(), 3)
call_9011 = relay.TupleGetItem(func_5642_call(), 3)
output = relay.Tuple([call_9010,])
output2 = relay.Tuple([call_9011,])
func_9012 = relay.Function([], output)
mod['func_9012'] = func_9012
mod = relay.transform.InferType()(mod)
output = func_9012()
func_9013 = relay.Function([], output)
mutated_mod['func_9013'] = func_9013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_9018 = func_1972_call()
call_9019 = func_1972_call()
output = relay.Tuple([call_9018,])
output2 = relay.Tuple([call_9019,])
func_9039 = relay.Function([], output)
mod['func_9039'] = func_9039
mod = relay.transform.InferType()(mod)
mutated_mod['func_9039'] = func_9039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9039_call = mutated_mod.get_global_var('func_9039')
call_9040 = func_9039_call()
output = call_9040
func_9041 = relay.Function([], output)
mutated_mod['func_9041'] = func_9041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21_call = mod.get_global_var('func_21')
func_22_call = mutated_mod.get_global_var('func_22')
call_9115 = func_21_call()
call_9116 = func_21_call()
func_1595_call = mod.get_global_var('func_1595')
func_1598_call = mutated_mod.get_global_var('func_1598')
var_9119 = relay.var("var_9119", dtype = "float32", shape = (10, 117))#candidate|9119|(10, 117)|var|float32
const_9120 = relay.const([[-3,-5,-5,-5,4,1,3,-6,2,-7,-1,7,4,-10,-7,8,-5,9,7,-7,9,-2,-9,-7,6,-3,-10,-6,-4,-7,-7,1,8,-4,-5,10,10,6,2,4,7,5,-10,2,-9,4,-4,10,6,-8,6,7,-10,9,6,10,-1,-1,-5,-2,1,-2,5,-8,-5,-4,-4,1,3,8,1,3,2,-2,6,-3,2,-4,7,-7,-6,-5,1,-6,6,-4,-9,-9,-2,10,-5,-6,8,5,2,10,-5,10,-3,-10,8,5,2,10,5,3,5,-8,-1,-8,4,-1,-5,5,-5,4,-9,-5,-3,5,7,7,-7,-4,-7,-9,10,-2,-1,2,1,1,5,1,1,3,3,-7,-4,-9,3,3,-10,-10],[-3,-6,8,-6,-1,10,-2,9,4,6,-9,10,6,9,10,6,-4,10,2,-7,-3,-7,2,2,4,-4,4,-6,9,6,-5,-5,-7,-2,-2,-1,8,2,4,5,-2,10,5,6,-3,5,7,8,-6,-2,-9,-3,-3,-6,9,-6,2,-4,-3,-1,3,4,-8,5,-5,2,1,3,-10,-2,10,-9,5,-9,6,-5,-6,10,-3,7,1,2,-5,-8,3,6,-8,-8,-10,1,7,-4,5,6,-8,-6,4,-3,-2,-6,10,10,6,-1,5,10,-10,-4,10,-4,4,-9,9,-7,-2,-8,4,-10,-8,-7,-5,-4,5,1,-9,-6,-5,3,-9,-7,-5,3,6,2,-6,-8,9,-7,1,10,3,5,2,-3],[2,2,-6,-9,-10,-8,-3,9,-10,6,4,-3,1,6,8,4,1,9,3,-2,2,-9,-8,-7,-5,-2,-7,10,3,-3,5,-2,7,6,1,3,9,8,-10,-6,6,-8,2,-4,3,-7,9,7,-3,6,-10,-9,10,-6,2,9,-1,4,-4,10,6,-6,-9,10,3,-9,-4,-1,6,7,1,-8,3,-8,10,4,5,2,-2,-9,-10,-9,-7,-1,2,-2,5,7,-4,5,-3,2,1,-4,-8,-10,-9,5,1,-8,-3,6,-10,6,-8,-10,3,8,7,7,-3,6,-7,-8,4,-3,-4,-6,4,10,4,10,3,-1,10,-8,8,4,4,6,-6,8,10,6,-6,5,-10,9,-4,4,10,-4,-7,-4],[8,10,10,6,1,-3,10,-9,4,-4,8,-2,-3,7,-7,-10,2,1,-7,2,-10,-5,5,-1,-1,9,4,-10,-10,-6,9,-3,5,2,10,-9,1,1,7,-6,8,10,9,-10,8,-5,1,9,-2,7,7,4,-10,-3,-8,7,-6,-9,-8,5,4,-6,-8,8,-6,-3,3,-10,-2,-1,-3,6,5,6,4,-1,1,-3,2,2,8,-10,3,-5,-2,7,5,9,-3,-3,-6,7,-2,10,-2,10,8,-3,2,9,-6,-1,2,-1,5,-1,-8,2,-9,-2,5,-2,-3,-5,5,-1,10,10,-2,-8,4,-9,8,-2,4,-7,-7,-1,6,-7,9,9,-10,5,1,10,-3,-10,2,9,8,-6,-6,9],[-2,2,4,5,4,9,-1,3,-2,4,-6,2,10,-1,5,-10,-8,-10,-6,8,3,5,8,8,2,-4,7,-4,-3,5,7,-5,-10,7,8,-3,-5,-4,8,-3,-6,-1,-4,-1,-4,-5,4,7,-4,9,2,-4,-10,-1,2,1,2,2,8,5,10,2,1,-9,4,9,-9,4,-3,10,-1,-7,2,3,1,-2,7,8,-1,-2,-2,-10,4,-2,1,6,2,6,-3,6,4,-8,9,-10,-10,5,3,-4,-1,8,8,-3,9,4,6,-5,-7,-3,8,7,6,-1,9,-6,10,4,9,-8,-5,-8,4,3,-8,-8,-10,4,8,4,1,-10,5,-10,-9,1,-3,-7,4,-8,8,9,-2,-5,8,-8],[1,-1,1,-3,10,-6,-4,-9,5,-5,5,1,8,-8,5,-7,-3,5,8,4,-1,-10,-3,7,10,1,5,5,-9,-10,-8,-3,5,-4,-5,2,7,2,3,-8,-9,-10,-2,-6,5,-5,4,3,5,4,-6,-5,10,-4,7,8,2,10,3,5,5,1,8,-1,-3,-3,3,3,5,10,1,10,6,-9,8,-6,-8,2,-5,10,-10,-1,1,10,-3,-10,8,10,-1,-4,-7,-2,1,10,7,-6,-3,1,10,1,-2,8,2,6,6,-2,4,7,-8,-1,-7,1,3,5,3,-7,-1,-5,-2,6,-4,-1,4,4,-5,6,-4,-5,1,2,-7,1,3,-1,-8,5,7,10,3,3,1,-3,8,-1],[7,-5,2,2,-1,-2,-10,-2,-2,2,8,-7,-5,-3,-8,2,-8,10,10,-7,5,-1,-8,-5,7,10,-1,6,7,10,4,1,-8,1,-4,-10,-2,5,-6,-10,6,-10,-7,4,8,9,6,5,2,-4,6,5,-5,-8,9,-3,10,-5,-4,10,4,5,1,6,5,10,-1,9,-5,6,7,-2,-5,-3,-5,2,-4,1,-6,-1,-4,2,7,-1,10,-10,-9,5,9,-4,3,-6,-4,2,-2,10,-3,-3,-6,5,-4,-5,7,-8,10,-3,-9,-9,3,-2,6,1,4,2,-10,8,-3,-6,4,7,7,8,8,-10,3,-6,-4,10,2,-8,10,4,-8,6,-6,8,2,3,3,10,7,-5,-2,-9],[-9,-7,-2,4,3,3,-2,5,7,5,3,-8,-1,9,9,10,-4,9,-7,-5,-3,-10,-1,3,4,2,5,-6,-4,-2,5,-1,8,-5,4,-5,-10,6,-1,1,-8,1,-2,10,3,7,7,-9,9,-1,-5,2,3,-9,6,8,-3,-7,-5,9,10,-10,-7,3,-2,-10,1,6,-9,-8,5,1,2,-10,-5,-9,-8,-4,-7,-10,-1,7,4,8,8,-10,-10,8,-9,3,1,8,8,-4,-9,5,7,-4,5,4,-5,-6,-7,1,5,9,3,-5,1,9,4,-2,3,-1,7,4,4,-9,2,-9,3,5,7,-10,-9,-10,10,-5,-7,3,-4,6,-5,-10,-6,-6,-9,6,10,6,-2,2,10,6],[6,1,-6,-9,-5,-10,8,-9,-6,2,-10,5,7,-5,9,-6,1,-4,-6,8,1,-4,5,-7,10,-8,10,-2,5,5,9,6,9,-6,2,-8,-3,4,-8,10,-10,8,-4,-8,10,-10,5,8,7,-8,-10,-3,-1,-1,-6,4,-9,-6,5,-1,-7,3,-6,-5,8,3,-2,-1,1,-1,-4,5,-9,8,6,8,-10,-5,-5,1,-4,9,1,8,-5,3,5,-7,-10,6,-4,-1,-7,-3,7,-4,-8,-6,7,3,4,-3,3,-3,3,-10,6,-1,8,-5,-8,5,-6,-7,6,4,7,10,5,6,1,-7,7,-9,-2,9,5,-7,4,3,7,1,3,5,-3,8,-7,10,-2,1,7,-3,-4,3],[-6,8,-4,-7,-8,-6,3,4,8,-8,-7,4,8,6,8,2,6,7,-8,-8,7,7,8,2,9,6,-8,10,8,10,5,-1,-1,-2,5,7,-2,3,-10,-5,4,5,-2,10,2,9,3,10,-10,-6,2,8,10,3,-6,-8,-2,4,9,7,7,9,-5,5,1,2,-5,-7,-2,4,1,-8,-5,10,-8,5,2,-7,-3,4,-6,-7,-7,-7,-7,6,-4,-2,9,-5,10,4,4,-8,-6,10,1,2,-4,-4,1,-8,6,-4,-1,-4,8,2,9,-8,-6,-6,8,2,8,-10,8,4,7,9,-6,10,10,6,5,4,-2,6,-10,-1,-6,5,-10,-8,-6,6,9,-8,9,-8,-5,6,3,-9]], dtype = "int8")#candidate|9120|(10, 144)|const|int8
call_9118 = relay.TupleGetItem(func_1595_call(relay.reshape(var_9119.astype('float32'), [13, 9, 10]), relay.reshape(const_9120.astype('int8'), [720, 2]), ), 0)
call_9121 = relay.TupleGetItem(func_1598_call(relay.reshape(var_9119.astype('float32'), [13, 9, 10]), relay.reshape(const_9120.astype('int8'), [720, 2]), ), 0)
output = relay.Tuple([call_9115,call_9118,var_9119,const_9120,])
output2 = relay.Tuple([call_9116,call_9121,var_9119,const_9120,])
func_9122 = relay.Function([var_9119,], output)
mod['func_9122'] = func_9122
mod = relay.transform.InferType()(mod)
var_9123 = relay.var("var_9123", dtype = "float32", shape = (10, 117))#candidate|9123|(10, 117)|var|float32
output = func_9122(var_9123)
func_9124 = relay.Function([var_9123], output)
mutated_mod['func_9124'] = func_9124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2566_call = mod.get_global_var('func_2566')
func_2568_call = mutated_mod.get_global_var('func_2568')
call_9145 = relay.TupleGetItem(func_2566_call(), 0)
call_9146 = relay.TupleGetItem(func_2568_call(), 0)
output = call_9145
output2 = call_9146
func_9154 = relay.Function([], output)
mod['func_9154'] = func_9154
mod = relay.transform.InferType()(mod)
output = func_9154()
func_9155 = relay.Function([], output)
mutated_mod['func_9155'] = func_9155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3375_call = mod.get_global_var('func_3375')
func_3376_call = mutated_mod.get_global_var('func_3376')
call_9212 = relay.TupleGetItem(func_3375_call(), 0)
call_9213 = relay.TupleGetItem(func_3376_call(), 0)
output = call_9212
output2 = call_9213
func_9215 = relay.Function([], output)
mod['func_9215'] = func_9215
mod = relay.transform.InferType()(mod)
output = func_9215()
func_9216 = relay.Function([], output)
mutated_mod['func_9216'] = func_9216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6658_call = mod.get_global_var('func_6658')
func_6659_call = mutated_mod.get_global_var('func_6659')
call_9265 = func_6658_call()
call_9266 = func_6658_call()
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
call_9271 = relay.TupleGetItem(func_5115_call(), 1)
call_9272 = relay.TupleGetItem(func_5117_call(), 1)
output = relay.Tuple([call_9265,call_9271,])
output2 = relay.Tuple([call_9266,call_9272,])
func_9273 = relay.Function([], output)
mod['func_9273'] = func_9273
mod = relay.transform.InferType()(mod)
mutated_mod['func_9273'] = func_9273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9273_call = mutated_mod.get_global_var('func_9273')
call_9274 = func_9273_call()
output = call_9274
func_9275 = relay.Function([], output)
mutated_mod['func_9275'] = func_9275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6642_call = mod.get_global_var('func_6642')
func_6643_call = mutated_mod.get_global_var('func_6643')
call_9300 = relay.TupleGetItem(func_6642_call(), 0)
call_9301 = relay.TupleGetItem(func_6643_call(), 0)
var_9326 = relay.var("var_9326", dtype = "float32", shape = (13, 9, 9))#candidate|9326|(13, 9, 9)|var|float32
bop_9327 = relay.mod(call_9300.astype('float32'), var_9326.astype('float32')) # shape=(13, 9, 9)
bop_9330 = relay.mod(call_9301.astype('float32'), var_9326.astype('float32')) # shape=(13, 9, 9)
output = bop_9327
output2 = bop_9330
func_9336 = relay.Function([var_9326,], output)
mod['func_9336'] = func_9336
mod = relay.transform.InferType()(mod)
var_9337 = relay.var("var_9337", dtype = "float32", shape = (13, 9, 9))#candidate|9337|(13, 9, 9)|var|float32
output = func_9336(var_9337)
func_9338 = relay.Function([var_9337], output)
mutated_mod['func_9338'] = func_9338
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9363 = relay.var("var_9363", dtype = "int16", shape = ())#candidate|9363|()|var|int16
var_9364 = relay.var("var_9364", dtype = "int16", shape = (16, 3, 9))#candidate|9364|(16, 3, 9)|var|int16
bop_9365 = relay.logical_xor(var_9363.astype('int16'), var_9364.astype('int16')) # shape=(16, 3, 9)
var_9369 = relay.var("var_9369", dtype = "int16", shape = (16, 3, 9))#candidate|9369|(16, 3, 9)|var|int16
bop_9370 = relay.less_equal(bop_9365.astype('bool'), relay.reshape(var_9369.astype('bool'), relay.shape_of(bop_9365))) # shape=(16, 3, 9)
output = bop_9370
output2 = bop_9370
func_9414 = relay.Function([var_9363,var_9364,var_9369,], output)
mod['func_9414'] = func_9414
mod = relay.transform.InferType()(mod)
var_9415 = relay.var("var_9415", dtype = "int16", shape = ())#candidate|9415|()|var|int16
var_9416 = relay.var("var_9416", dtype = "int16", shape = (16, 3, 9))#candidate|9416|(16, 3, 9)|var|int16
var_9417 = relay.var("var_9417", dtype = "int16", shape = (16, 3, 9))#candidate|9417|(16, 3, 9)|var|int16
output = func_9414(var_9415,var_9416,var_9417,)
func_9418 = relay.Function([var_9415,var_9416,var_9417,], output)
mutated_mod['func_9418'] = func_9418
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9488 = relay.var("var_9488", dtype = "float64", shape = (8, 12, 16))#candidate|9488|(8, 12, 16)|var|float64
uop_9489 = relay.rsqrt(var_9488.astype('float64')) # shape=(8, 12, 16)
output = relay.Tuple([uop_9489,])
output2 = relay.Tuple([uop_9489,])
func_9492 = relay.Function([var_9488,], output)
mod['func_9492'] = func_9492
mod = relay.transform.InferType()(mod)
mutated_mod['func_9492'] = func_9492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9493 = relay.var("var_9493", dtype = "float64", shape = (8, 12, 16))#candidate|9493|(8, 12, 16)|var|float64
func_9492_call = mutated_mod.get_global_var('func_9492')
call_9494 = func_9492_call(var_9493)
output = call_9494
func_9495 = relay.Function([var_9493], output)
mutated_mod['func_9495'] = func_9495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7155_call = mod.get_global_var('func_7155')
func_7156_call = mutated_mod.get_global_var('func_7156')
call_9556 = relay.TupleGetItem(func_7155_call(), 1)
call_9557 = relay.TupleGetItem(func_7156_call(), 1)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_9565 = func_3036_call()
call_9566 = func_3036_call()
func_4133_call = mod.get_global_var('func_4133')
func_4134_call = mutated_mod.get_global_var('func_4134')
call_9578 = relay.TupleGetItem(func_4133_call(), 0)
call_9579 = relay.TupleGetItem(func_4134_call(), 0)
bop_9610 = relay.right_shift(call_9556.astype('int8'), call_9565.astype('int8')) # shape=(13, 9, 1440)
bop_9613 = relay.right_shift(call_9557.astype('int8'), call_9566.astype('int8')) # shape=(13, 9, 1440)
output = relay.Tuple([call_9578,bop_9610,])
output2 = relay.Tuple([call_9579,bop_9613,])
func_9617 = relay.Function([], output)
mod['func_9617'] = func_9617
mod = relay.transform.InferType()(mod)
output = func_9617()
func_9618 = relay.Function([], output)
mutated_mod['func_9618'] = func_9618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3455_call = mod.get_global_var('func_3455')
func_3456_call = mutated_mod.get_global_var('func_3456')
call_9644 = relay.TupleGetItem(func_3455_call(), 1)
call_9645 = relay.TupleGetItem(func_3456_call(), 1)
var_9649 = relay.var("var_9649", dtype = "float32", shape = (13, 9, 15))#candidate|9649|(13, 9, 15)|var|float32
bop_9650 = relay.greater(call_9644.astype('bool'), var_9649.astype('bool')) # shape=(13, 9, 15)
bop_9653 = relay.greater(call_9645.astype('bool'), var_9649.astype('bool')) # shape=(13, 9, 15)
func_7430_call = mod.get_global_var('func_7430')
func_7431_call = mutated_mod.get_global_var('func_7431')
call_9677 = relay.TupleGetItem(func_7430_call(), 1)
call_9678 = relay.TupleGetItem(func_7431_call(), 1)
output = relay.Tuple([bop_9650,call_9677,])
output2 = relay.Tuple([bop_9653,call_9678,])
func_9696 = relay.Function([var_9649,], output)
mod['func_9696'] = func_9696
mod = relay.transform.InferType()(mod)
var_9697 = relay.var("var_9697", dtype = "float32", shape = (13, 9, 15))#candidate|9697|(13, 9, 15)|var|float32
output = func_9696(var_9697)
func_9698 = relay.Function([var_9697], output)
mutated_mod['func_9698'] = func_9698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_9787 = relay.TupleGetItem(func_155_call(), 0)
call_9788 = relay.TupleGetItem(func_156_call(), 0)
output = relay.Tuple([call_9787,])
output2 = relay.Tuple([call_9788,])
func_9793 = relay.Function([], output)
mod['func_9793'] = func_9793
mod = relay.transform.InferType()(mod)
mutated_mod['func_9793'] = func_9793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9793_call = mutated_mod.get_global_var('func_9793')
call_9794 = func_9793_call()
output = call_9794
func_9795 = relay.Function([], output)
mutated_mod['func_9795'] = func_9795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_9839 = relay.TupleGetItem(func_1758_call(), 1)
call_9840 = relay.TupleGetItem(func_1759_call(), 1)
func_4883_call = mod.get_global_var('func_4883')
func_4885_call = mutated_mod.get_global_var('func_4885')
call_9841 = relay.TupleGetItem(func_4883_call(), 0)
call_9842 = relay.TupleGetItem(func_4885_call(), 0)
output = relay.Tuple([call_9839,call_9841,])
output2 = relay.Tuple([call_9840,call_9842,])
func_9850 = relay.Function([], output)
mod['func_9850'] = func_9850
mod = relay.transform.InferType()(mod)
mutated_mod['func_9850'] = func_9850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9850_call = mutated_mod.get_global_var('func_9850')
call_9851 = func_9850_call()
output = call_9851
func_9852 = relay.Function([], output)
mutated_mod['func_9852'] = func_9852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_887_call = mod.get_global_var('func_887')
func_888_call = mutated_mod.get_global_var('func_888')
call_9866 = relay.TupleGetItem(func_887_call(), 0)
call_9867 = relay.TupleGetItem(func_888_call(), 0)
func_76_call = mod.get_global_var('func_76')
func_77_call = mutated_mod.get_global_var('func_77')
call_9922 = relay.TupleGetItem(func_76_call(), 2)
call_9923 = relay.TupleGetItem(func_77_call(), 2)
func_7606_call = mod.get_global_var('func_7606')
func_7607_call = mutated_mod.get_global_var('func_7607')
call_9927 = func_7606_call()
call_9928 = func_7606_call()
output = relay.Tuple([call_9866,call_9922,call_9927,])
output2 = relay.Tuple([call_9867,call_9923,call_9928,])
func_9936 = relay.Function([], output)
mod['func_9936'] = func_9936
mod = relay.transform.InferType()(mod)
output = func_9936()
func_9937 = relay.Function([], output)
mutated_mod['func_9937'] = func_9937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7086_call = mutated_mod.get_global_var('func_7086')
call_9938 = relay.TupleGetItem(func_7084_call(), 0)
call_9939 = relay.TupleGetItem(func_7086_call(), 0)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_9952 = relay.TupleGetItem(func_1758_call(), 1)
call_9953 = relay.TupleGetItem(func_1759_call(), 1)
func_6039_call = mod.get_global_var('func_6039')
func_6041_call = mutated_mod.get_global_var('func_6041')
const_9955 = relay.const([[-6.810065,9.136504,3.230624],[6.558177,6.562037,5.069429],[3.690743,-1.842851,6.198022],[6.386873,4.937220,8.094849],[6.729039,-8.304330,-2.334309],[-8.130935,-9.956154,7.101852],[-7.682571,7.776237,5.178265],[-6.397771,4.557475,5.115190],[4.206017,-5.418121,1.527166],[-5.305542,4.751437,-9.375551],[-5.312581,-5.656399,-8.049458],[-2.576851,-6.813858,-4.592106],[-5.817912,-2.559747,3.580131],[-5.424814,-8.358781,-3.222756],[2.742188,8.650771,9.559020],[-8.972986,-0.272646,-6.127726],[-1.221554,2.496173,-9.734335],[5.190611,-7.703959,-7.840212],[2.598632,1.985712,-1.711921],[6.098154,-9.817754,-1.902538],[-0.827501,2.721458,1.862633],[-0.571720,-4.653914,-8.043949],[3.360599,-7.889660,6.170984],[-8.837929,7.309954,6.477953],[6.324121,5.711666,6.963078],[9.889909,2.003293,-5.929747],[-7.485595,-3.923445,4.267955],[6.600184,-8.734238,-0.091075],[-2.797112,9.436381,-1.768398],[6.094831,3.148598,2.605306],[-6.160100,5.831801,1.469121],[-5.910484,-2.008746,9.483852],[2.388093,-3.334479,-2.581408],[-9.940095,1.742038,-7.078777],[-8.027647,0.995041,1.974158],[-5.409455,2.820420,1.873225],[1.003694,-3.570947,-5.194083],[1.542105,-8.885191,-2.143390],[8.082648,-2.895802,-8.819824],[-6.594187,-4.086360,-3.459743],[5.394164,-6.664986,-1.655076],[3.940617,3.015234,6.596768],[4.466430,-1.507962,3.987126],[-6.933548,5.315220,4.361660],[-7.231171,-7.732694,-9.010574],[-4.519873,9.197886,-1.332302],[-4.814049,3.313173,-3.628746],[2.113274,-6.233416,0.198585],[-2.465758,-4.066628,-0.190287],[9.145588,9.312817,-6.154958],[1.087518,7.906691,1.935065],[-0.854658,-6.631275,9.163481],[1.244094,-0.059069,-0.108880],[3.257756,-2.789422,-6.689864],[8.132722,8.816636,9.228142],[-9.302824,-7.554548,4.575112],[-4.666382,1.828395,-5.344356],[6.890603,5.783671,0.312222],[0.603430,7.450355,-4.939290],[7.702181,8.209184,-3.557800],[-9.085196,0.453220,4.674237],[-9.969893,1.554200,-3.851615],[-9.471464,3.887943,6.655494],[-7.711862,9.733832,-6.793722],[7.610032,1.740966,-5.011182],[-0.794751,8.419103,4.745676],[-8.422878,-3.757594,5.479202],[5.217246,-9.111252,-5.321438],[2.026807,-5.983934,-0.069584],[-6.590000,-0.962299,-3.485115],[-1.117639,2.082892,2.740443],[-1.614921,-3.273372,1.819586],[5.524931,-7.879012,6.997409],[6.371306,3.351357,4.182337],[9.954359,3.527113,9.279778],[-8.757399,-3.099312,2.122175],[8.526499,-3.139135,-0.811462],[1.306347,-0.397486,7.399040],[-7.902118,1.287886,0.197191],[7.162384,-3.716158,-1.682667],[7.193456,6.251566,3.949655],[9.167580,-9.881650,-0.185037],[1.192756,-1.083330,0.480281],[4.884470,1.354894,8.524733],[2.966033,6.959764,-8.606903],[3.188513,-9.962648,6.573975],[-0.266221,-8.190520,-3.232862],[5.509054,2.896555,-6.585771],[-3.809628,-8.188564,-5.511757],[-1.513444,8.186411,8.939395],[8.426671,1.202468,-5.117708],[4.432702,8.879262,4.952370],[9.926243,0.573641,7.926635],[3.434041,1.371016,9.718793],[-1.768132,8.230524,2.241890],[2.969349,0.910642,-4.688357],[4.721883,-7.672205,-2.397709],[0.191503,9.994924,-8.706136],[-7.284065,-0.968528,9.327995],[8.542849,9.889747,4.471950],[9.069891,8.341855,2.595381],[-8.842285,-3.972253,4.798362],[5.534435,-9.821758,7.630575],[2.336667,-8.190191,4.497565],[7.211339,7.853246,9.504529],[3.047403,3.989855,-0.017102],[-1.049746,-3.951613,3.512429],[8.688665,-3.330904,4.198390],[-4.401970,5.495175,-9.110535],[8.943093,0.428194,-9.339777],[8.983742,0.890138,7.484608],[-2.206760,4.584503,-4.770524],[-7.905797,7.168583,2.872316],[1.279655,4.999268,-2.525464],[5.754337,7.620059,4.076605],[-8.544743,2.303057,6.672239],[3.623800,-4.823008,-9.123115],[9.417450,6.988865,0.684698],[-9.632326,-4.164459,6.338458],[8.268927,-7.094989,3.395851],[3.360924,6.952505,-7.431034],[3.374280,-4.761291,-4.136360],[-7.570904,6.358902,-3.525059],[-1.591929,2.793052,-1.086042],[3.769559,-7.380818,-7.737621],[3.657536,9.479486,-2.757885],[-1.444860,8.637847,8.200499],[0.179659,6.748718,9.300876],[-0.572415,-3.978102,1.367180],[-7.690950,5.900909,-2.113003],[9.176189,7.020082,-3.756396],[-1.956785,2.147281,1.883972],[6.281825,-9.941028,-8.932976],[-6.727691,5.922426,-2.605566],[4.223364,0.724784,8.574027],[-3.857680,-9.228219,4.476753],[8.490688,6.517696,9.098170],[8.015392,4.998505,-3.239443],[-4.570810,-5.391987,2.323737],[-5.133011,-4.358633,8.461360],[4.514756,-5.236235,4.245421],[3.021051,2.174145,7.757512],[6.161661,5.508331,-7.128248],[-0.419007,-7.991517,-0.357955],[-6.185816,-4.124174,9.923347],[-6.313222,5.329505,-2.504300],[9.070402,1.005416,-3.424384],[4.924246,1.151772,-5.724875],[-4.152467,-5.096614,-2.040971],[9.855794,9.930388,7.889191],[6.082166,-9.515587,-5.008437],[-0.768304,-8.013081,-6.195029],[-9.932371,-6.707077,-3.405463],[-1.182737,-4.096297,7.624313],[4.401648,7.357536,-3.598292],[5.456827,-9.498118,-5.510508],[-4.535029,-4.108459,-8.794976],[2.392133,6.192088,-3.486707],[4.282337,-3.401432,-7.024575],[-8.927475,-2.270994,-6.417948],[-6.691880,7.852149,9.616451],[4.781149,-6.921071,-2.836116],[-0.901692,5.890132,-4.469976],[1.879494,-9.161824,1.146658],[2.847714,6.461204,6.889041],[-4.158839,7.946039,-9.034488],[0.256730,4.372070,-7.916324],[-0.668435,7.057928,-3.424205],[1.049792,9.763943,2.895980],[-6.782215,-9.001565,9.089113],[-1.923782,5.832647,5.600510],[-4.161462,8.341942,-8.627034],[-2.414420,-5.285008,-7.267121],[9.163391,-9.124313,-5.171788],[7.238506,-1.389146,-6.325063],[6.677069,8.174357,-7.941808],[-5.810300,5.820732,-4.039456],[1.343476,-0.794895,8.855768],[-2.754296,8.900701,3.561702],[9.401943,-3.373932,3.248315],[9.613425,8.542523,7.721978],[0.803250,8.928606,-7.373006],[-8.152231,-6.355525,3.713681],[2.849257,-2.478808,0.326073],[-7.021884,-5.438874,-8.696876],[5.198542,-9.750030,0.180354],[7.697411,7.335145,6.228339],[-7.692695,-9.611897,7.863220],[-3.313330,1.297720,6.816869],[7.149934,2.871425,-0.848720],[7.714277,5.857883,5.616832],[3.972733,7.263024,3.226143],[-7.839281,-2.098578,-9.842745],[5.342768,5.843050,5.576619],[4.382968,-3.973676,-0.584754],[-6.989966,9.959748,4.689874],[-9.975618,0.102222,7.346070],[6.304624,-0.135617,-7.194561],[3.787878,-3.583882,7.770475],[4.539684,-3.690162,6.222169],[-9.288112,-7.305345,-8.663066],[-6.855658,-8.887396,-0.782319],[-8.457705,-1.504844,-8.458081],[9.894501,-1.759468,-5.546385],[4.839205,-9.489875,6.930007],[-4.179733,4.549015,5.156288],[-4.217204,3.527719,0.100705],[9.082198,2.206152,2.073417],[-3.173790,9.255090,-6.248765],[-0.900657,0.708525,9.905567],[1.318604,-7.711243,-3.113913],[-7.381038,-3.209926,6.476677],[3.591854,5.608148,-3.702507],[-9.424136,-3.000536,5.303888],[9.495540,-6.584786,-6.420136],[-9.464501,-7.526691,4.971490],[-9.239171,2.477363,4.649893],[7.300712,5.236059,7.672684],[2.564829,3.884679,0.796160],[-3.567982,-6.458553,8.851375],[-8.021503,-5.408208,-3.161146],[9.641137,4.983312,2.111264],[2.045658,-1.123233,-5.926649],[1.415030,1.564242,6.554321],[4.738102,-1.820800,-9.248183],[4.399241,1.601660,7.831642],[9.039935,-2.458919,-0.246277],[3.590889,-6.466668,-0.397806],[8.637629,-2.435731,-9.449694],[9.062530,3.703972,-5.036942],[7.217437,-3.384595,6.457952],[-5.590486,-9.751313,-0.240279],[5.963901,7.357716,5.588117],[-5.567039,9.529580,3.820640],[-1.581717,5.919097,-1.297516],[8.583574,6.685782,-0.749172],[-0.913140,2.661595,-9.043608],[4.295387,3.817049,9.130123],[-2.974848,9.164186,1.808217],[-7.726044,7.988096,4.108311],[9.646634,1.790040,4.054606],[6.555416,3.125922,-1.938889],[-6.649254,3.426203,-7.805054],[-8.859555,-9.869823,-8.852309],[8.177065,9.331034,7.690564],[-4.419675,1.362345,5.820957],[-4.073760,-9.747252,-8.521980],[5.010715,-1.136822,-9.392183],[1.013812,-7.088274,7.082632],[2.776489,8.080936,4.688524],[-3.691597,0.202919,-6.920652],[-0.342081,2.424696,-8.515590],[0.134485,0.397183,-4.265356],[0.135345,-9.122169,5.893909],[-6.679227,-2.585795,4.570621],[-7.554615,-2.465106,2.217973],[7.018978,6.400536,9.234769],[-1.241553,2.788580,-5.423804],[2.526469,1.270922,6.602669],[6.450125,-8.099692,5.120567],[-0.713540,6.519666,4.698175],[5.766443,-8.741938,-1.511605],[-9.290359,-7.181214,-3.135931],[7.571262,-8.339032,2.559372],[6.771688,-8.833109,9.445641],[4.957330,3.632573,-6.954734],[6.768856,3.789298,-2.973114],[2.134920,-1.938822,-4.329182],[0.478031,3.216425,-2.296196],[4.372165,1.649232,9.389722],[-2.713328,-2.780887,9.193964],[-3.409315,-0.509570,-2.361871],[1.757896,7.272027,-0.948767],[-1.984738,7.607836,7.708451],[6.877375,0.313716,-8.005311],[3.070513,6.169687,7.013086],[-4.782559,-3.905122,6.428928],[5.393965,-4.594543,6.119288],[-6.606375,-7.741923,9.253602],[4.859652,2.375011,0.545731],[-2.642363,-6.605452,8.386901],[-4.267031,6.271191,-2.613619],[-4.504697,-4.813470,2.684468],[8.451569,0.259819,4.950676],[8.681862,8.143759,-2.985067],[7.269012,3.507408,-0.167130],[0.125586,-2.215130,6.645367],[7.253457,-7.996976,7.658094],[1.752278,5.015142,-1.873686],[4.198122,-8.400683,-7.730109],[-6.931240,8.304077,6.267271],[-7.565539,-9.313952,-4.024413],[0.845249,8.706223,6.208897],[1.830823,1.633003,9.664697],[-6.864738,-0.086432,-0.100066],[4.808754,-9.917215,-5.829587],[-0.530451,-9.514628,-4.842020],[5.069764,-3.510847,9.670750],[8.521584,1.128322,-3.807934],[-9.323896,6.514125,3.882318],[-0.837508,-2.648364,7.900151],[-0.461938,5.102717,-5.629490],[5.080826,-6.623480,2.607296],[4.030761,-0.353925,2.840547],[-1.324113,9.153719,-5.881365],[2.193837,2.698593,5.389407],[-5.686344,8.470503,-2.776514],[1.151676,8.755972,-0.846672],[-3.511992,4.959755,-0.112748],[4.022158,-0.841701,-7.205750],[3.676124,5.951265,-5.577343],[9.324761,7.808058,-9.226797],[-1.842754,8.337551,5.757683],[-7.133279,-1.339331,2.349837],[9.786635,0.111574,8.394448],[-6.134828,5.264445,-6.216726],[8.990961,-3.970224,-6.741443],[-7.265035,2.713447,-8.560117],[1.569375,-6.407307,-4.929826],[-0.152277,-6.143350,8.305964],[-6.910214,-7.427550,-6.914779],[6.209502,-0.048655,-6.771761],[-7.928732,6.865021,-9.607848],[6.610879,1.099972,5.048644],[3.325331,6.713968,5.970611],[2.245346,-4.996360,5.870927],[-3.472715,-7.941942,5.744745],[3.721324,-4.517257,5.493667],[-7.650169,-1.689709,-0.917843],[0.590157,-0.457110,2.359183],[-1.863502,2.301672,-8.849471],[7.010365,8.699768,6.565475],[-7.740701,-4.485004,5.349855],[3.841632,-3.622986,0.789414],[-8.388007,-3.959115,2.850747],[-1.242080,3.944814,7.718958],[0.825623,-4.848934,-4.179146],[8.968658,9.675107,5.527285],[2.745543,-5.935789,1.486287],[-3.494180,9.872519,-3.351405],[-4.365718,-5.143124,-8.692387],[0.683728,-4.005629,-4.045357],[0.126795,2.359916,8.066421],[9.638023,6.403290,1.359090],[-4.667493,-4.971279,-8.394168],[-5.027141,-1.390447,-3.902132],[-9.522151,-2.695979,-7.905989],[-5.831199,-1.410210,-5.279508],[-7.810289,-5.613615,3.926916],[-1.151102,4.532044,8.739801],[7.647231,-2.977459,-5.865490],[-3.561413,-9.512511,3.739164],[7.182131,-7.803237,4.527201],[-2.540315,-2.932299,-4.060109],[-2.547239,4.384211,1.452186],[8.841863,0.683493,-4.693233],[7.636076,-5.661312,3.035849],[-2.720506,6.920834,-0.656411],[2.444575,3.896910,4.043831],[6.381739,-3.240289,1.990125],[-8.767029,9.749333,-6.957069],[2.839050,-4.168284,1.332875],[-0.804569,5.651943,-0.335988],[-6.040179,-5.882291,-3.734886],[3.856866,1.544377,-6.786529],[-4.829579,9.763853,-5.961052],[3.093951,5.063637,-3.998166],[-6.994094,-7.653777,-5.188193],[3.792441,-9.207708,-8.984235],[-0.500954,1.922761,-3.536740],[-8.235371,-8.207374,-5.693342],[-3.472209,-1.404427,8.301409],[-7.374881,9.426771,0.009351],[-5.868599,8.552630,-4.349310],[0.951057,1.456397,-6.773330],[-4.821549,-5.992616,5.424255],[-7.963869,4.780838,3.093927],[0.884913,-5.055071,7.647213],[-3.814992,-0.401336,-3.750648],[-9.998782,6.414871,-6.914844],[1.752499,6.839032,5.621603],[-8.803724,-2.246818,2.373485],[-9.911337,3.959829,0.493065],[2.979122,-1.520486,0.643591],[-7.462666,-3.118407,-0.315423],[-6.138235,-1.718307,9.037533],[-8.325567,0.518354,9.035028],[-0.640486,6.175020,-8.843976],[-8.219597,-9.658905,-7.746182],[-9.388649,6.170965,-6.300698],[2.057602,4.205715,-2.738534],[-8.110070,-5.448830,4.258850],[-9.846326,-9.470596,-7.396107],[-0.520376,-9.570974,8.310391],[9.608651,1.578298,4.990440],[-6.190436,-3.538678,-1.687481],[-3.805933,6.030984,-7.239551],[2.301495,0.063654,-9.075362],[-9.844173,-4.116744,0.318029],[6.340989,9.920106,-5.363592],[3.457103,-9.326435,-8.224756],[-9.980780,4.896234,-0.251689],[3.053199,-1.772061,8.959875],[-1.097055,5.156758,-6.545251],[-6.583030,5.941531,-2.330185],[-7.978223,-2.471825,-3.863832],[4.221832,-8.763862,-1.819819],[-7.406067,-1.469345,-5.028689],[1.163115,3.075910,-2.995195],[-6.273153,-0.795367,-8.954960],[3.169106,-6.018673,2.097546],[-5.710852,4.657541,0.352022],[0.937106,7.917670,-8.144488],[7.878266,-9.589254,2.349251],[-0.886866,-7.766307,6.819387],[-3.765704,8.298867,4.507100],[7.410997,-2.032460,-1.355031],[-1.521979,5.136793,6.774027],[-4.449591,-6.576192,1.297910],[9.808716,4.032612,-4.449362],[-3.882484,1.807926,2.550182],[8.291070,-8.954522,-8.463770],[0.059747,5.567325,-3.277139],[2.542130,8.910170,-6.981358],[0.300546,1.349075,0.964738],[4.248587,-4.713172,9.214479],[1.942461,-3.575142,-0.444257],[-3.756750,8.991605,0.836882],[-2.128892,-4.876314,-9.292013],[0.153850,-6.614098,-3.087382],[-2.435443,-2.876718,-1.981020],[2.307271,-2.115783,0.054936],[-8.096809,-1.741040,5.452374],[5.391707,-6.518656,-2.402459],[-1.556204,-3.033493,-7.086364],[-0.652492,6.540478,8.929413],[4.107766,8.015179,-1.039273],[-5.364656,8.971887,-9.172914],[-9.743864,-9.788655,-5.773044],[6.235789,-3.049126,8.048545],[-0.722746,-4.378407,-3.745029],[8.486077,-6.327210,5.677222],[-4.633512,7.678953,7.561310],[-5.772747,4.062193,-4.690652],[7.059963,2.694566,-9.162700],[-8.698902,-5.653662,-0.197409],[-5.936983,-0.778367,-2.418808],[2.225340,-7.741976,-4.268078],[7.381881,3.150804,-3.472001],[-8.423356,-8.059267,4.647711],[-7.016925,9.409450,-4.683593],[-5.695071,-6.630074,3.557046],[-7.793000,1.557357,9.057123],[-1.626640,-8.978288,-2.378688],[-9.270206,6.481187,-9.958474],[5.239941,-6.811769,2.651193],[-5.246208,-3.837398,0.613991],[5.501771,-7.212065,-2.940969],[4.889535,-9.953477,-4.757592],[-4.558343,5.081618,7.117272],[-0.664154,6.211049,-2.362093],[-4.707485,-4.336421,4.059924],[-8.913713,3.213067,5.530222],[8.770578,2.790190,-8.557264],[-8.301866,-1.026678,-0.538148],[0.394296,-2.433240,-9.359012],[9.543249,0.385543,9.298265],[7.203328,9.513821,-9.416697],[-9.011049,0.715835,-7.884846],[-9.000504,-9.441206,-7.410816],[-0.734007,-8.947976,-2.787138],[4.463842,5.014345,5.273274],[2.169934,-7.569415,-0.950376],[2.669594,-8.099706,-8.740615],[0.116145,3.823438,7.273072],[-8.747648,9.594440,-3.086219],[6.669084,-4.666433,-8.192486],[3.950993,-2.096306,-3.854196],[4.036737,-7.854489,2.862624],[-3.332299,2.050018,-5.918786],[2.372181,-5.113732,8.825834],[8.544635,8.101143,8.115301],[6.541828,8.833713,5.972595],[-8.238723,-6.666038,-2.397798],[5.433708,-5.508610,1.749696],[6.971845,2.032557,9.849528],[-8.592709,-0.601835,-1.395632],[4.906359,-1.180785,-3.898291],[4.344356,-9.897388,8.401080],[0.092107,9.736806,7.280416],[-5.100531,-9.644728,-5.726848],[1.411415,-7.578936,-0.821438],[9.719119,-7.050491,2.824663],[0.502488,-5.235326,-1.204554],[7.511707,-8.610029,9.307045],[4.111753,5.455398,3.039401],[3.774569,-7.585374,-7.359781],[0.701190,8.346784,-9.319852],[-9.449322,6.605517,0.227216],[-1.504908,6.268988,-2.750352],[-3.108840,-6.995251,2.567600],[6.391715,-4.057982,-8.962770],[6.093892,8.632010,4.139691],[6.064807,9.694408,-7.174467],[-1.904266,2.523898,-2.451410],[-5.659266,1.325004,-0.219973],[-2.290877,-7.748752,2.896007],[-8.316632,-0.600240,1.661866],[4.374231,4.550993,1.081928],[6.199483,-8.624407,8.010308],[-8.241447,2.039458,5.387031],[-2.280274,7.489909,-8.245345],[5.213908,1.256896,-0.257603],[-4.313133,6.451487,5.326120],[8.772411,-0.043226,3.839852],[-0.190276,4.910320,-4.183149],[1.249210,9.576778,2.334661],[-4.677393,-3.459660,-3.588531],[-4.500800,-5.178642,-1.804141],[0.540753,-5.476704,5.689977],[1.455092,-8.177883,5.796766],[5.363351,5.503058,0.924913],[7.558120,-5.688586,-4.360933],[-7.843985,2.848093,-6.955715],[-9.840888,7.319279,-2.810333],[4.951109,2.690819,-9.395866],[-2.898645,3.622797,-6.589230],[-0.408465,-1.569545,3.542496],[2.224519,-7.925962,-0.526068],[-4.472566,-9.497770,-2.179772],[-5.564443,-7.223869,4.621344],[-4.625859,1.092770,5.825018],[-8.243573,5.757581,-5.979985],[3.274994,-7.340813,-3.915937],[9.191071,-5.194204,0.539748],[-9.520820,-1.573303,5.374870],[4.059743,3.099701,3.364933],[8.582221,-9.777219,1.737311],[7.303629,-4.639327,-1.595689],[4.409704,3.628889,7.834054],[-3.839736,-5.198005,-4.896966],[-3.899122,5.923532,-1.598937],[-9.462211,-6.480859,-1.972937],[-1.151493,0.796053,-5.242455],[5.124492,3.309076,1.341340],[5.965063,-1.498274,-0.847073],[2.837071,-7.390522,-4.735027],[-2.797108,-5.406925,3.635145],[-0.981755,8.707136,-6.751328],[2.605521,5.981477,-9.754866],[6.718841,-9.315466,3.096658],[-8.432806,2.555975,0.906228],[-6.724333,-3.616104,-0.134001],[5.781199,6.293519,-1.380282],[-1.086366,-5.785807,-7.850374],[-3.713887,-3.764228,8.040060],[7.654167,6.130512,2.837946],[-0.292977,-7.675678,-0.605814],[-1.533226,4.003173,-2.425215],[5.469177,9.161150,-7.732308],[-8.555211,2.090570,5.687056],[-4.228410,-1.000062,7.394636],[-6.710317,7.295395,8.029477],[-7.108891,-2.477632,8.359469],[2.550730,5.210907,-9.837837],[9.406114,3.913656,-5.903332],[0.097963,9.707024,-5.890400],[4.064681,3.580976,7.504360],[6.788877,-8.708010,2.950619],[-0.235835,0.916713,3.682468],[-2.064132,-8.914475,3.282895],[-4.118417,-4.991600,-1.459410],[1.586729,7.130806,5.314995],[9.417816,-4.545806,-2.753286],[4.953880,1.805753,-9.530508],[8.656802,1.531370,-6.457870],[-4.166936,9.472404,6.712505],[3.827291,-8.869525,2.215023],[5.425070,-9.525114,-7.351012],[6.455513,2.365528,-5.380280],[1.503323,-5.060865,-1.603979],[3.304132,-2.954663,1.879253],[-1.896089,-1.932947,8.551246],[-1.337587,-8.305067,5.985854],[5.255912,-0.588514,8.524607]], dtype = "float32")#candidate|9955|(585, 3)|const|float32
call_9954 = relay.TupleGetItem(func_6039_call(relay.reshape(const_9955.astype('float32'), [1755,])), 0)
call_9956 = relay.TupleGetItem(func_6041_call(relay.reshape(const_9955.astype('float32'), [1755,])), 0)
output = relay.Tuple([call_9938,call_9952,call_9954,const_9955,])
output2 = relay.Tuple([call_9939,call_9953,call_9956,const_9955,])
func_9959 = relay.Function([], output)
mod['func_9959'] = func_9959
mod = relay.transform.InferType()(mod)
mutated_mod['func_9959'] = func_9959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9959_call = mutated_mod.get_global_var('func_9959')
call_9960 = func_9959_call()
output = call_9960
func_9961 = relay.Function([], output)
mutated_mod['func_9961'] = func_9961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9273_call = mod.get_global_var('func_9273')
func_9275_call = mutated_mod.get_global_var('func_9275')
call_10035 = relay.TupleGetItem(func_9273_call(), 1)
call_10036 = relay.TupleGetItem(func_9275_call(), 1)
func_5778_call = mod.get_global_var('func_5778')
func_5780_call = mutated_mod.get_global_var('func_5780')
call_10052 = relay.TupleGetItem(func_5778_call(), 0)
call_10053 = relay.TupleGetItem(func_5780_call(), 0)
output = relay.Tuple([call_10035,call_10052,])
output2 = relay.Tuple([call_10036,call_10053,])
func_10065 = relay.Function([], output)
mod['func_10065'] = func_10065
mod = relay.transform.InferType()(mod)
output = func_10065()
func_10066 = relay.Function([], output)
mutated_mod['func_10066'] = func_10066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_10067 = relay.TupleGetItem(func_7413_call(), 0)
call_10068 = relay.TupleGetItem(func_7415_call(), 0)
output = call_10067
output2 = call_10068
func_10087 = relay.Function([], output)
mod['func_10087'] = func_10087
mod = relay.transform.InferType()(mod)
mutated_mod['func_10087'] = func_10087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10087_call = mutated_mod.get_global_var('func_10087')
call_10088 = func_10087_call()
output = call_10088
func_10089 = relay.Function([], output)
mutated_mod['func_10089'] = func_10089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6764_call = mod.get_global_var('func_6764')
func_6765_call = mutated_mod.get_global_var('func_6765')
call_10115 = relay.TupleGetItem(func_6764_call(), 0)
call_10116 = relay.TupleGetItem(func_6765_call(), 0)
var_10135 = relay.var("var_10135", dtype = "float32", shape = (13, 9, 8))#candidate|10135|(13, 9, 8)|var|float32
bop_10136 = relay.less_equal(call_10115.astype('bool'), var_10135.astype('bool')) # shape=(13, 9, 8)
bop_10139 = relay.less_equal(call_10116.astype('bool'), var_10135.astype('bool')) # shape=(13, 9, 8)
output = relay.Tuple([bop_10136,])
output2 = relay.Tuple([bop_10139,])
func_10142 = relay.Function([var_10135,], output)
mod['func_10142'] = func_10142
mod = relay.transform.InferType()(mod)
mutated_mod['func_10142'] = func_10142
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10143 = relay.var("var_10143", dtype = "float32", shape = (13, 9, 8))#candidate|10143|(13, 9, 8)|var|float32
func_10142_call = mutated_mod.get_global_var('func_10142')
call_10144 = func_10142_call(var_10143)
output = call_10144
func_10145 = relay.Function([var_10143], output)
mutated_mod['func_10145'] = func_10145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5540_call = mod.get_global_var('func_5540')
func_5542_call = mutated_mod.get_global_var('func_5542')
call_10205 = relay.TupleGetItem(func_5540_call(), 0)
call_10206 = relay.TupleGetItem(func_5542_call(), 0)
func_9617_call = mod.get_global_var('func_9617')
func_9618_call = mutated_mod.get_global_var('func_9618')
call_10223 = relay.TupleGetItem(func_9617_call(), 1)
call_10224 = relay.TupleGetItem(func_9618_call(), 1)
func_5795_call = mod.get_global_var('func_5795')
func_5797_call = mutated_mod.get_global_var('func_5797')
call_10227 = relay.TupleGetItem(func_5795_call(), 0)
call_10228 = relay.TupleGetItem(func_5797_call(), 0)
output = relay.Tuple([call_10205,call_10223,call_10227,])
output2 = relay.Tuple([call_10206,call_10224,call_10228,])
func_10277 = relay.Function([], output)
mod['func_10277'] = func_10277
mod = relay.transform.InferType()(mod)
mutated_mod['func_10277'] = func_10277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10277_call = mutated_mod.get_global_var('func_10277')
call_10278 = func_10277_call()
output = call_10278
func_10279 = relay.Function([], output)
mutated_mod['func_10279'] = func_10279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_155_call = mod.get_global_var('func_155')
func_156_call = mutated_mod.get_global_var('func_156')
call_10387 = relay.TupleGetItem(func_155_call(), 1)
call_10388 = relay.TupleGetItem(func_156_call(), 1)
func_5422_call = mod.get_global_var('func_5422')
func_5424_call = mutated_mod.get_global_var('func_5424')
call_10395 = func_5422_call()
call_10396 = func_5422_call()
func_3133_call = mod.get_global_var('func_3133')
func_3135_call = mutated_mod.get_global_var('func_3135')
call_10398 = relay.TupleGetItem(func_3133_call(), 0)
call_10399 = relay.TupleGetItem(func_3135_call(), 0)
var_10403 = relay.var("var_10403", dtype = "float32", shape = (3, 14, 4))#candidate|10403|(3, 14, 4)|var|float32
bop_10404 = relay.power(call_10398.astype('float32'), relay.reshape(var_10403.astype('float32'), relay.shape_of(call_10398))) # shape=(3, 14, 4)
bop_10407 = relay.power(call_10399.astype('float32'), relay.reshape(var_10403.astype('float32'), relay.shape_of(call_10399))) # shape=(3, 14, 4)
output = relay.Tuple([call_10387,call_10395,bop_10404,])
output2 = relay.Tuple([call_10388,call_10396,bop_10407,])
func_10419 = relay.Function([var_10403,], output)
mod['func_10419'] = func_10419
mod = relay.transform.InferType()(mod)
mutated_mod['func_10419'] = func_10419
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10420 = relay.var("var_10420", dtype = "float32", shape = (3, 14, 4))#candidate|10420|(3, 14, 4)|var|float32
func_10419_call = mutated_mod.get_global_var('func_10419')
call_10421 = func_10419_call(var_10420)
output = call_10421
func_10422 = relay.Function([var_10420], output)
mutated_mod['func_10422'] = func_10422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7750_call = mod.get_global_var('func_7750')
func_7752_call = mutated_mod.get_global_var('func_7752')
call_10484 = relay.TupleGetItem(func_7750_call(), 1)
call_10485 = relay.TupleGetItem(func_7752_call(), 1)
func_7043_call = mod.get_global_var('func_7043')
func_7045_call = mutated_mod.get_global_var('func_7045')
call_10486 = relay.TupleGetItem(func_7043_call(), 2)
call_10487 = relay.TupleGetItem(func_7045_call(), 2)
bop_10489 = relay.less(call_10484.astype('bool'), call_10486.astype('bool')) # shape=(13, 9, 2002)
bop_10492 = relay.less(call_10485.astype('bool'), call_10487.astype('bool')) # shape=(13, 9, 2002)
uop_10493 = relay.log10(call_10486.astype('float32')) # shape=(1, 2002)
uop_10495 = relay.log10(call_10487.astype('float32')) # shape=(1, 2002)
bop_10496 = relay.equal(bop_10489.astype('bool'), uop_10493.astype('bool')) # shape=(13, 9, 2002)
bop_10499 = relay.equal(bop_10492.astype('bool'), uop_10495.astype('bool')) # shape=(13, 9, 2002)
output = bop_10496
output2 = bop_10499
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
