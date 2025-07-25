import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_3 = relay.const(1.934834, dtype = "float64")#candidate|3|()|const|float64
var_4 = relay.var("var_4", dtype = "float64", shape = (1, 2, 16))#candidate|4|(1, 2, 16)|var|float64
bop_5 = relay.divide(const_3.astype('float64'), var_4.astype('float64')) # shape=(1, 2, 16)
bop_19 = relay.bitwise_and(bop_5.astype('uint8'), const_3.astype('uint8')) # shape=(1, 2, 16)
bop_36 = relay.equal(const_3.astype('bool'), var_4.astype('bool')) # shape=(1, 2, 16)
output = relay.Tuple([bop_19,bop_36,])
output2 = relay.Tuple([bop_19,bop_36,])
func_57 = relay.Function([var_4,], output)
mod['func_57'] = func_57
mod = relay.transform.InferType()(mod)
var_58 = relay.var("var_58", dtype = "float64", shape = (1, 2, 16))#candidate|58|(1, 2, 16)|var|float64
output = func_57(var_58)
func_59 = relay.Function([var_58], output)
mutated_mod['func_59'] = func_59
mutated_mod = relay.transform.InferType()(mutated_mod)
var_235 = relay.var("var_235", dtype = "float64", shape = (14, 7, 16))#candidate|235|(14, 7, 16)|var|float64
uop_236 = relay.sin(var_235.astype('float64')) # shape=(14, 7, 16)
func_57_call = mod.get_global_var('func_57')
func_59_call = mutated_mod.get_global_var('func_59')
var_239 = relay.var("var_239", dtype = "float64", shape = (32,))#candidate|239|(32,)|var|float64
call_238 = relay.TupleGetItem(func_57_call(relay.reshape(var_239.astype('float64'), [1, 2, 16])), 0)
call_240 = relay.TupleGetItem(func_59_call(relay.reshape(var_239.astype('float64'), [1, 2, 16])), 0)
output = relay.Tuple([uop_236,call_238,var_239,])
output2 = relay.Tuple([uop_236,call_240,var_239,])
func_256 = relay.Function([var_235,var_239,], output)
mod['func_256'] = func_256
mod = relay.transform.InferType()(mod)
mutated_mod['func_256'] = func_256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_256_call = mutated_mod.get_global_var('func_256')
var_258 = relay.var("var_258", dtype = "float64", shape = (14, 7, 16))#candidate|258|(14, 7, 16)|var|float64
var_259 = relay.var("var_259", dtype = "float64", shape = (32,))#candidate|259|(32,)|var|float64
call_257 = func_256_call(var_258,var_259,)
output = call_257
func_260 = relay.Function([var_258,var_259,], output)
mutated_mod['func_260'] = func_260
mutated_mod = relay.transform.InferType()(mutated_mod)
const_266 = relay.const([[[8,9,-3,8,-10,5,7,8,-10,-1,2,-6,-9,1,-3,-9],[-6,-1,-7,-9,1,8,5,-4,-9,-7,-3,7,-7,-5,-9,3],[3,6,-1,8,-1,10,2,-9,8,-1,-9,3,7,8,10,-5],[3,2,-6,-8,7,-3,1,-10,-7,10,-1,4,10,-8,-3,-3]],[[4,-2,6,-7,9,3,-1,-1,-6,-6,5,-7,-2,-5,-5,1],[6,10,-5,-6,-9,4,-2,8,-9,4,-4,9,3,-1,4,8],[5,-3,-4,-5,-8,5,-6,-9,-9,9,4,-9,3,5,-2,-9],[-10,-9,3,-9,3,-2,-7,5,4,9,-1,-4,10,4,-4,-3]],[[7,-9,4,-5,4,-7,10,6,4,-1,6,1,-7,-2,-8,-5],[4,7,-4,6,-2,8,3,-6,-1,-5,-4,-5,-1,-2,-1,-6],[-1,-5,-7,-2,4,-1,-5,-7,5,3,8,2,6,-10,3,2],[-9,10,9,-5,5,1,2,-6,10,8,-9,9,8,-2,5,6]],[[10,10,-9,2,10,4,1,-10,-9,-1,9,-4,9,-8,10,6],[10,-1,2,5,-9,3,8,3,2,-6,3,-9,-7,-7,-1,-1],[1,-1,9,5,4,-10,-3,-10,6,-7,-9,3,3,5,3,6],[9,-6,-5,6,9,4,8,7,1,7,10,5,8,-5,7,-4]]], dtype = "int8")#candidate|266|(4, 4, 16)|const|int8
const_267 = relay.const([[[1,5,4,1,8,-10,1,-4,-1,5,1,8,4,-10,6,6],[-5,-9,7,-10,-5,-8,6,-3,7,6,-6,1,-8,-6,10,-10],[-2,-8,10,-4,6,1,5,8,-4,1,-3,-1,-5,3,-10,4],[3,-3,-8,6,-10,-8,1,-7,2,-6,-2,6,-3,-5,-4,-6]],[[-9,-8,5,-2,10,-10,-6,9,-8,-5,-9,8,-9,-6,-9,8],[3,-6,-1,-5,-8,6,-5,4,-8,-4,9,3,-4,-1,-3,-5],[-6,-5,9,9,-9,5,-8,7,-9,6,-4,6,-6,-5,5,-5],[10,7,4,-1,1,-6,7,6,4,-6,9,-8,-8,-5,-2,-3]],[[2,4,-7,8,-10,-6,8,5,-4,-2,-2,9,5,2,-6,-2],[6,-6,-10,1,-9,-1,9,-8,-8,7,1,9,-1,5,-7,-8],[10,7,10,-2,-3,3,8,4,-2,-5,6,-10,6,-6,10,-7],[10,2,10,-9,6,6,3,-1,10,7,9,-4,-3,-7,4,5]],[[8,4,-1,2,4,3,-9,-2,10,8,9,4,2,-4,7,-2],[7,4,10,-7,-7,2,5,-6,5,6,-4,5,4,-4,-1,10],[4,-7,-2,-9,-7,5,-8,8,-3,-7,-5,-6,-4,-1,-9,-4],[-5,-7,5,7,10,-5,3,2,-6,-6,3,-9,2,-3,-3,2]]], dtype = "int8")#candidate|267|(4, 4, 16)|const|int8
bop_268 = relay.maximum(const_266.astype('int8'), relay.reshape(const_267.astype('int8'), relay.shape_of(const_266))) # shape=(4, 4, 16)
func_57_call = mod.get_global_var('func_57')
func_59_call = mutated_mod.get_global_var('func_59')
const_280 = relay.const([7.682186,-8.747904,-0.338517,-0.995763,9.335866,-5.063869,3.423910,2.503702,3.571888,7.512542,3.112250,-8.317602,-8.760554,-4.075875,-1.963536,-5.786348,-6.574148,2.149073,3.974440,1.197332,-8.402542,4.267535,6.272529,3.290327,0.562700,1.860454,-2.551496,1.729849,-7.510906,-7.064035,-0.195527,-5.278860], dtype = "float64")#candidate|280|(32,)|const|float64
call_279 = relay.TupleGetItem(func_57_call(relay.reshape(const_280.astype('float64'), [1, 2, 16])), 1)
call_281 = relay.TupleGetItem(func_59_call(relay.reshape(const_280.astype('float64'), [1, 2, 16])), 1)
uop_282 = relay.acosh(const_266.astype('float32')) # shape=(4, 4, 16)
output = relay.Tuple([bop_268,call_279,const_280,uop_282,])
output2 = relay.Tuple([bop_268,call_281,const_280,uop_282,])
func_284 = relay.Function([], output)
mod['func_284'] = func_284
mod = relay.transform.InferType()(mod)
mutated_mod['func_284'] = func_284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_284_call = mutated_mod.get_global_var('func_284')
call_285 = func_284_call()
output = call_285
func_286 = relay.Function([], output)
mutated_mod['func_286'] = func_286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_284_call = mod.get_global_var('func_284')
func_286_call = mutated_mod.get_global_var('func_286')
call_310 = relay.TupleGetItem(func_284_call(), 0)
call_311 = relay.TupleGetItem(func_286_call(), 0)
output = relay.Tuple([call_310,])
output2 = relay.Tuple([call_311,])
func_312 = relay.Function([], output)
mod['func_312'] = func_312
mod = relay.transform.InferType()(mod)
output = func_312()
func_313 = relay.Function([], output)
mutated_mod['func_313'] = func_313
mutated_mod = relay.transform.InferType()(mutated_mod)
const_319 = relay.const([[[-5.384417,-9.738903,-4.848633,-7.429785,5.049567,-7.906423,-7.912196,-4.622804,-4.750240,-5.214077,7.156685,-3.474056,7.367364,6.843787],[-4.091227,-5.979710,8.302547,-9.220208,-1.610906,-1.053121,-5.681082,9.164031,-2.267563,-2.497684,0.559439,-3.259630,7.643312,-2.161256]],[[-8.765119,-6.725375,-9.985425,4.016743,-8.691227,-4.513744,0.885013,-3.801194,9.412223,-2.820503,7.047531,-9.116032,3.758843,0.438831],[8.256822,5.329085,-0.189932,-4.281044,-7.028926,-8.840238,3.482888,-3.615974,-5.219985,-2.915715,-5.082525,0.304770,5.345641,-3.465099]]], dtype = "float64")#candidate|319|(2, 2, 14)|const|float64
uop_320 = relay.log10(const_319.astype('float64')) # shape=(2, 2, 14)
output = uop_320
output2 = uop_320
func_322 = relay.Function([], output)
mod['func_322'] = func_322
mod = relay.transform.InferType()(mod)
output = func_322()
func_323 = relay.Function([], output)
mutated_mod['func_323'] = func_323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_284_call = mod.get_global_var('func_284')
func_286_call = mutated_mod.get_global_var('func_286')
call_443 = relay.TupleGetItem(func_284_call(), 2)
call_444 = relay.TupleGetItem(func_286_call(), 2)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_451 = func_322_call()
call_452 = func_322_call()
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_464 = func_322_call()
call_465 = func_322_call()
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_477 = func_322_call()
call_478 = func_322_call()
output = relay.Tuple([call_443,call_451,call_464,call_477,])
output2 = relay.Tuple([call_444,call_452,call_465,call_478,])
func_482 = relay.Function([], output)
mod['func_482'] = func_482
mod = relay.transform.InferType()(mod)
mutated_mod['func_482'] = func_482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_482_call = mutated_mod.get_global_var('func_482')
call_483 = func_482_call()
output = call_483
func_484 = relay.Function([], output)
mutated_mod['func_484'] = func_484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_496 = relay.TupleGetItem(func_312_call(), 0)
call_497 = relay.TupleGetItem(func_313_call(), 0)
uop_498 = relay.sinh(call_496.astype('float32')) # shape=(4, 4, 16)
uop_500 = relay.sinh(call_497.astype('float32')) # shape=(4, 4, 16)
const_506 = relay.const([[[3.888434,-8.298384,4.636727,3.694448,-0.427493,-3.303300,0.033537,5.875908,-3.086407,-8.050425,-9.027755,-0.302987,1.953723,2.119570,9.400283,-0.797274],[7.504118,4.153947,-8.590017,1.364738,0.332789,-6.762359,-2.761808,7.591372,-1.585526,0.322917,4.095656,6.334608,-2.357891,6.443091,5.281790,-9.959528],[-9.449371,4.099364,-7.173599,-9.111161,7.935702,-9.847951,-7.695113,-3.756166,-3.067145,-2.973601,5.948840,-4.654902,-6.995945,5.492372,-0.468485,2.265255],[-9.421298,1.084054,3.652728,-0.222353,-7.472655,8.226273,-2.393541,-2.405755,8.090959,-6.283196,-6.973052,-7.793092,-5.698019,-8.401434,6.355404,-3.606275]],[[9.982860,-0.086094,1.959051,8.054017,-5.187504,-5.065436,-9.940493,5.160158,8.296632,4.627064,-8.342070,2.655324,1.895271,9.067746,5.799530,-6.732111],[2.659111,3.976460,1.680377,3.660275,5.459033,-1.316612,-3.627369,6.473747,-8.887783,4.032856,-4.446095,9.191040,-8.811314,-8.665073,-9.126306,-9.545529],[-7.953802,-5.131991,-2.603653,5.970436,-0.347589,-2.344571,3.584506,-3.839302,-7.647541,-8.350212,-7.671557,-3.636336,4.106556,-0.357808,-0.431434,2.641393],[6.667376,-7.298443,1.534855,2.146747,-3.182348,-8.698029,-4.449064,2.108079,-5.893676,9.950185,7.467897,-6.735285,7.266200,1.692966,3.480629,-2.308378]],[[-5.893195,9.590590,-8.801337,1.409025,-6.628113,-6.619571,5.810260,7.924233,2.886613,-9.809286,-3.488713,6.839014,-3.440329,1.406087,-0.626175,-2.612086],[5.917726,-3.791592,-0.947723,-4.867501,-1.508880,9.387921,-1.512161,4.698419,-4.478064,-4.808243,-6.242808,-8.882514,-9.820022,8.452818,1.135790,-9.463653],[9.857269,-3.211319,-7.093646,-7.198026,8.629546,-6.533613,-4.211528,0.728710,-6.263363,9.077612,-2.026662,2.558178,-3.384561,9.963335,-1.753397,-6.412845],[-7.729595,1.509651,2.941908,5.389967,-2.695761,-7.781750,-3.395952,0.924923,6.865619,2.094447,-3.358474,8.433291,5.094630,-3.886823,-0.593249,8.927234]],[[9.310151,0.003629,-2.494869,5.892274,1.515746,4.530076,2.167594,-6.182439,-8.231535,-2.457189,-5.010488,9.056987,-5.241580,9.687516,-6.194202,-0.010236],[5.368236,-2.553751,-5.144184,-8.822180,6.070514,0.924491,-5.032188,0.872494,-9.019840,5.749615,6.810383,-1.389389,-5.477059,-1.470975,8.059945,-6.473158],[9.417383,-3.257520,-3.592317,8.174016,7.560263,2.982293,-2.610014,-0.449247,-0.540631,3.995582,-9.400985,-6.559390,3.339955,5.079370,7.295856,7.526763],[-2.942405,-4.963311,1.192735,-0.358347,0.979505,-0.344786,-0.588179,-3.985412,8.631100,0.670875,5.292426,-5.825848,-6.394787,3.338361,-8.305446,-0.729485]]], dtype = "float32")#candidate|506|(4, 4, 16)|const|float32
bop_507 = relay.logical_and(uop_498.astype('bool'), relay.reshape(const_506.astype('bool'), relay.shape_of(uop_498))) # shape=(4, 4, 16)
bop_510 = relay.logical_and(uop_500.astype('bool'), relay.reshape(const_506.astype('bool'), relay.shape_of(uop_500))) # shape=(4, 4, 16)
output = relay.Tuple([bop_507,])
output2 = relay.Tuple([bop_510,])
func_513 = relay.Function([], output)
mod['func_513'] = func_513
mod = relay.transform.InferType()(mod)
output = func_513()
func_514 = relay.Function([], output)
mutated_mod['func_514'] = func_514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_482_call = mod.get_global_var('func_482')
func_484_call = mutated_mod.get_global_var('func_484')
call_542 = relay.TupleGetItem(func_482_call(), 0)
call_543 = relay.TupleGetItem(func_484_call(), 0)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_550 = relay.TupleGetItem(func_312_call(), 0)
call_551 = relay.TupleGetItem(func_313_call(), 0)
func_256_call = mod.get_global_var('func_256')
func_260_call = mutated_mod.get_global_var('func_260')
var_554 = relay.var("var_554", dtype = "float64", shape = (1568,))#candidate|554|(1568,)|var|float64
call_553 = relay.TupleGetItem(func_256_call(relay.reshape(var_554.astype('float64'), [14, 7, 16]), relay.reshape(call_542.astype('float64'), [32,]), ), 0)
call_555 = relay.TupleGetItem(func_260_call(relay.reshape(var_554.astype('float64'), [14, 7, 16]), relay.reshape(call_542.astype('float64'), [32,]), ), 0)
output = relay.Tuple([call_542,call_550,call_553,var_554,])
output2 = relay.Tuple([call_543,call_551,call_555,var_554,])
func_556 = relay.Function([var_554,], output)
mod['func_556'] = func_556
mod = relay.transform.InferType()(mod)
mutated_mod['func_556'] = func_556
mutated_mod = relay.transform.InferType()(mutated_mod)
var_557 = relay.var("var_557", dtype = "float64", shape = (1568,))#candidate|557|(1568,)|var|float64
func_556_call = mutated_mod.get_global_var('func_556')
call_558 = func_556_call(var_557)
output = call_558
func_559 = relay.Function([var_557], output)
mutated_mod['func_559'] = func_559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_513_call = mod.get_global_var('func_513')
func_514_call = mutated_mod.get_global_var('func_514')
call_573 = relay.TupleGetItem(func_513_call(), 0)
call_574 = relay.TupleGetItem(func_514_call(), 0)
output = call_573
output2 = call_574
func_575 = relay.Function([], output)
mod['func_575'] = func_575
mod = relay.transform.InferType()(mod)
output = func_575()
func_576 = relay.Function([], output)
mutated_mod['func_576'] = func_576
mutated_mod = relay.transform.InferType()(mutated_mod)
var_661 = relay.var("var_661", dtype = "float64", shape = ())#candidate|661|()|var|float64
var_662 = relay.var("var_662", dtype = "float64", shape = (16, 15, 14))#candidate|662|(16, 15, 14)|var|float64
bop_663 = relay.less(var_661.astype('bool'), var_662.astype('bool')) # shape=(16, 15, 14)
const_667 = relay.const([[[False,False,False,False,False,False,True,False,False,False,False,True,True,True],[True,False,False,False,True,True,True,False,True,False,False,False,True,False],[False,False,False,False,True,True,False,True,True,True,True,False,True,True],[True,True,False,False,True,False,False,False,False,False,True,True,False,True],[True,True,True,True,False,True,True,True,False,True,False,False,False,False],[False,False,True,True,True,False,True,False,False,False,True,False,False,False],[True,False,True,False,True,False,True,True,True,False,False,False,True,True],[False,False,True,False,False,False,True,True,False,False,True,True,False,False],[True,False,False,True,False,True,True,False,True,True,True,True,True,False],[True,True,True,True,True,False,True,True,False,False,False,True,False,True],[False,True,False,True,True,False,False,False,False,False,False,True,True,True],[False,False,True,True,True,False,False,False,False,True,True,True,True,True],[False,False,True,False,True,True,True,False,True,False,False,True,False,False],[True,True,False,True,True,True,True,True,False,True,True,False,True,True],[True,False,False,True,False,True,True,True,False,True,False,False,True,False]],[[True,True,True,False,False,True,False,True,False,True,False,False,False,False],[True,True,True,False,False,True,False,False,True,True,False,True,False,False],[True,True,False,True,False,True,True,False,False,True,False,True,False,False],[True,True,False,False,False,True,True,False,True,True,True,False,False,True],[True,True,True,True,False,True,False,True,True,True,True,True,True,True],[False,True,False,False,False,False,False,True,False,True,True,True,False,False],[True,True,True,False,False,False,True,False,False,True,True,True,True,True],[False,False,False,True,True,False,True,False,True,True,True,True,True,False],[False,True,True,True,False,False,True,False,True,True,True,True,False,False],[False,True,True,False,True,False,True,True,False,False,True,True,False,False],[False,True,False,False,False,True,True,True,False,True,True,True,False,False],[False,False,True,False,False,False,False,True,False,False,False,True,False,True],[False,False,True,True,True,False,True,False,True,True,True,True,False,False],[False,False,True,False,False,False,False,False,False,True,False,True,True,False],[False,True,False,False,False,True,True,True,True,True,True,True,False,False]],[[False,False,True,True,False,False,True,False,False,False,True,False,True,True],[True,False,True,True,True,True,False,True,True,True,True,False,False,False],[True,False,True,False,False,False,True,False,False,False,True,False,False,False],[False,True,True,False,True,False,True,True,False,True,False,True,True,True],[True,True,False,True,False,True,True,False,True,False,True,True,False,False],[True,True,False,True,False,True,True,False,True,True,True,True,False,True],[False,True,True,False,True,True,True,True,False,False,True,True,False,False],[False,False,False,True,True,False,False,False,True,False,False,True,True,True],[False,True,False,True,True,True,True,False,False,False,True,False,False,False],[True,False,True,True,False,True,False,False,False,True,False,True,True,False],[False,False,True,True,True,True,False,False,True,True,False,True,True,True],[False,True,False,True,True,True,True,True,False,True,True,False,False,True],[False,True,True,False,True,False,True,True,False,True,True,True,False,False],[False,True,True,False,False,True,False,True,False,True,True,True,False,False],[True,True,False,True,False,True,False,False,False,True,True,False,True,False]],[[True,True,False,True,True,False,False,True,True,False,True,False,True,False],[True,True,False,False,False,False,False,True,False,False,True,False,True,False],[False,False,False,True,False,True,False,True,True,False,False,False,False,True],[False,True,True,True,True,False,False,True,False,False,False,False,False,True],[False,True,True,False,False,False,True,False,True,False,True,False,False,True],[False,True,True,True,False,False,False,True,False,False,True,True,False,True],[True,False,True,False,False,False,False,False,False,False,False,True,False,True],[True,False,False,False,True,True,True,False,False,True,True,False,False,False],[True,False,False,True,True,True,True,True,True,True,True,False,True,True],[True,True,False,True,False,False,True,True,False,False,True,False,True,True],[False,True,True,False,False,True,True,True,False,False,False,False,True,True],[False,True,False,True,False,False,False,False,False,True,False,False,True,True],[False,True,False,True,False,False,True,False,True,False,True,False,False,True],[False,True,False,False,False,False,True,True,False,False,True,True,True,True],[True,True,True,False,False,True,True,False,True,False,True,True,False,False]],[[True,False,False,True,True,False,True,False,True,False,True,True,False,False],[False,False,False,False,True,True,False,True,False,True,True,False,True,False],[True,True,True,False,True,True,True,False,True,False,False,False,False,True],[False,True,False,False,True,False,False,False,True,False,True,True,True,False],[True,False,True,False,True,False,False,False,True,True,True,False,True,True],[True,False,True,True,True,True,True,False,True,False,False,False,False,True],[True,False,True,True,False,False,True,False,False,False,False,True,True,True],[False,True,True,True,True,False,False,False,True,True,False,False,True,False],[False,False,True,True,False,False,False,False,True,False,False,True,False,True],[True,True,False,True,False,True,False,True,True,False,True,False,True,True],[False,True,True,False,True,False,False,True,True,False,True,False,False,False],[True,False,True,False,False,True,True,False,True,True,False,False,True,True],[True,True,True,True,False,False,False,True,True,False,False,False,False,True],[False,True,True,True,True,False,False,True,False,True,False,True,True,False],[True,False,True,False,True,False,False,True,True,False,False,False,False,False]],[[False,False,False,False,True,True,True,True,False,True,False,False,True,False],[True,False,False,False,False,False,True,False,False,True,True,True,True,False],[True,True,False,True,True,False,True,True,False,True,False,False,False,False],[False,True,True,True,True,True,True,False,True,False,False,False,True,True],[True,False,True,True,True,False,False,True,False,False,False,False,True,False],[False,True,False,False,True,True,True,False,True,True,False,False,True,False],[False,True,False,False,True,True,True,True,True,True,False,False,True,False],[False,False,False,True,False,False,True,True,False,True,True,True,False,False],[True,True,False,False,False,False,False,False,False,True,True,True,False,True],[True,False,True,False,False,True,True,False,True,False,True,True,True,True],[False,True,True,False,True,True,False,True,False,False,True,False,True,False],[True,True,True,True,True,False,True,False,True,False,False,True,False,False],[False,False,True,True,True,False,True,False,True,True,False,True,True,True],[True,False,False,True,True,True,False,True,False,True,True,True,True,True],[False,True,True,True,True,False,False,True,False,True,True,False,False,True]],[[True,True,True,True,True,True,False,False,False,False,True,False,True,False],[False,False,False,False,True,True,True,True,False,True,False,False,False,True],[False,False,True,False,True,False,True,False,True,True,True,True,True,False],[False,False,True,False,False,True,False,True,False,False,False,False,True,False],[True,False,False,True,False,True,True,False,True,False,False,False,True,True],[True,False,False,True,False,True,True,False,False,False,False,False,False,False],[True,True,True,False,True,True,True,False,False,True,False,True,True,False],[True,True,False,False,True,False,False,False,True,True,False,True,True,False],[True,True,True,False,True,False,False,False,True,False,False,True,True,False],[False,False,True,True,True,True,True,True,True,True,True,False,True,True],[True,False,False,False,False,True,True,True,True,True,True,False,True,False],[True,False,False,True,True,True,False,False,False,True,True,True,True,False],[True,False,False,False,False,False,True,False,True,False,True,False,True,True],[False,True,True,True,True,True,False,False,True,False,True,True,True,False],[True,False,True,False,False,True,True,True,True,False,True,False,False,True]],[[False,True,False,False,False,True,True,False,False,True,False,True,True,True],[True,False,False,False,True,True,False,True,False,True,False,True,True,False],[True,True,True,True,True,True,True,True,False,False,True,False,True,False],[False,False,True,True,False,True,True,True,False,True,True,False,True,True],[True,False,True,False,False,False,True,True,True,False,False,True,False,False],[False,True,False,False,True,True,True,False,True,False,True,True,True,False],[False,False,False,True,True,True,False,True,False,True,False,True,False,False],[True,False,False,True,False,False,True,True,False,False,True,True,False,True],[False,True,True,False,False,True,False,True,True,False,False,True,True,False],[False,True,False,True,False,True,False,False,True,True,True,True,True,True],[False,True,False,True,True,True,True,True,True,True,False,False,True,False],[True,True,False,True,False,False,True,False,True,True,False,True,True,False],[False,False,True,True,False,True,False,True,False,True,False,True,True,False],[True,False,False,False,True,False,False,False,False,True,False,False,False,True],[True,True,True,True,False,False,False,False,True,False,True,True,False,True]],[[True,True,True,False,True,True,True,True,True,True,True,True,False,True],[True,False,False,False,False,True,False,False,True,False,False,False,True,True],[False,True,False,True,False,True,True,True,False,False,False,True,True,True],[False,True,True,False,False,True,False,False,True,False,False,False,True,False],[True,False,True,True,True,True,False,True,False,True,False,False,False,True],[True,True,False,True,True,True,True,True,True,False,True,False,False,True],[False,True,True,True,True,False,False,False,True,False,True,True,False,False],[True,False,True,False,True,True,True,False,True,True,True,False,True,False],[False,True,True,False,True,False,False,False,False,False,True,True,True,False],[False,True,False,True,True,True,True,False,True,True,True,False,False,False],[False,True,True,False,False,False,False,True,True,False,False,True,True,True],[True,False,True,True,True,False,True,False,True,False,False,False,True,True],[False,True,False,False,False,True,False,True,True,True,False,False,True,False],[False,False,True,True,False,True,False,True,True,True,True,False,False,False],[True,True,True,True,True,True,False,True,False,False,False,False,True,True]],[[False,True,True,False,True,True,True,False,False,False,True,True,True,True],[True,True,True,False,True,False,False,False,False,False,True,False,False,False],[False,False,True,True,True,False,True,False,True,True,False,True,True,False],[False,False,True,False,False,False,False,True,False,False,True,False,False,False],[True,True,False,True,True,True,False,False,False,False,False,True,True,True],[True,False,True,True,False,False,True,False,False,False,True,False,False,False],[True,True,True,False,False,True,True,True,True,False,True,True,False,True],[False,True,False,True,True,True,True,True,True,False,False,True,False,True],[False,True,False,True,False,True,True,False,False,False,True,True,False,False],[False,False,True,True,True,False,False,False,True,True,False,True,False,False],[False,False,True,False,True,True,True,True,False,False,True,True,True,False],[False,True,False,True,False,False,False,True,False,False,False,True,False,False],[False,False,False,True,False,True,True,False,True,True,True,True,True,True],[False,False,True,True,False,False,False,False,False,False,True,False,False,True],[True,False,True,False,False,True,True,True,True,False,True,False,True,False]],[[True,True,True,False,True,True,True,True,True,True,True,True,True,True],[True,True,False,False,False,False,False,False,True,True,True,False,False,False],[False,True,True,False,False,False,False,False,True,True,True,False,False,True],[True,True,False,False,False,False,True,False,False,True,True,False,True,False],[False,True,True,True,False,False,True,True,False,True,True,False,False,False],[False,False,True,False,True,True,False,True,False,True,False,False,True,True],[False,False,True,True,True,False,False,True,False,True,False,True,False,True],[True,False,False,True,False,True,True,True,True,False,False,True,True,False],[True,False,True,False,False,True,True,True,True,True,True,False,False,True],[True,False,True,False,False,True,True,False,False,True,True,True,True,True],[False,False,False,False,True,True,False,True,False,True,True,False,False,False],[False,False,True,True,False,False,True,False,True,False,False,False,True,True],[True,False,False,False,True,False,False,False,False,False,True,False,True,False],[False,True,False,False,True,False,True,True,False,False,True,False,True,True],[False,False,False,True,True,False,True,False,True,True,False,True,True,True]],[[True,False,False,False,True,False,False,False,False,False,True,True,False,False],[True,True,True,True,False,True,False,True,False,False,True,True,True,True],[False,True,False,True,True,False,True,True,True,False,True,True,False,True],[False,False,True,True,False,True,False,False,False,True,True,False,True,False],[True,False,True,True,True,True,True,True,False,False,False,True,False,True],[False,False,False,True,True,False,False,True,True,True,True,True,False,False],[False,True,False,True,True,True,True,True,False,False,False,False,False,False],[True,True,True,False,True,False,True,False,False,True,True,True,False,False],[False,False,False,False,True,False,False,True,True,True,False,False,True,False],[False,True,False,False,False,True,False,False,True,True,False,True,False,False],[False,True,False,True,True,True,True,True,True,True,False,True,False,False],[True,True,False,True,True,False,True,True,True,True,True,True,False,False],[False,True,False,True,False,False,False,True,True,True,False,True,True,False],[False,True,False,True,True,False,False,False,False,False,True,False,True,True],[True,False,True,True,True,True,False,True,True,False,False,True,False,True]],[[False,True,True,False,False,False,True,True,False,True,True,True,True,True],[True,True,False,False,True,True,True,False,False,False,True,True,False,True],[False,False,False,False,True,False,False,False,False,True,True,False,True,True],[True,False,False,False,True,False,False,False,True,False,False,True,False,True],[False,False,True,True,True,True,True,False,True,False,False,True,True,False],[False,False,True,True,True,True,False,False,True,False,True,False,False,True],[True,False,True,True,True,False,False,False,True,False,False,True,False,True],[False,True,True,False,False,False,False,True,True,False,True,False,False,False],[False,True,False,True,True,True,False,False,True,True,False,False,True,True],[True,True,False,False,False,True,False,False,True,False,True,False,False,True],[False,True,True,False,False,True,True,True,False,True,False,True,False,False],[False,True,True,True,False,True,True,True,False,False,True,True,False,True],[True,True,False,True,False,True,True,False,True,False,True,True,False,True],[True,False,False,True,False,True,False,False,True,False,True,True,False,True],[True,False,False,False,True,False,False,True,True,True,True,False,False,True]],[[False,False,False,True,False,False,False,False,False,False,True,True,False,False],[False,False,True,True,True,True,False,False,True,False,False,True,True,True],[True,True,False,True,True,True,False,False,True,False,False,True,True,True],[False,True,False,True,False,True,False,True,True,False,True,False,False,True],[True,False,True,True,True,True,False,True,False,True,True,False,True,True],[True,False,True,False,False,True,True,False,False,True,True,True,False,False],[False,False,False,True,False,True,False,False,False,True,True,True,False,False],[True,True,True,False,False,False,False,False,True,True,False,False,True,True],[True,True,True,True,True,True,True,False,False,True,False,True,False,True],[False,False,True,True,False,False,True,False,True,False,False,False,True,False],[False,False,True,False,True,False,True,True,False,False,True,False,False,True],[True,False,False,True,True,True,False,True,True,False,True,False,False,True],[True,True,True,True,False,False,True,True,False,True,False,False,True,True],[True,True,False,False,False,False,False,True,True,False,False,True,False,True],[True,False,False,False,False,True,False,False,True,True,True,True,False,False]],[[False,False,True,True,True,False,True,True,False,True,False,False,False,False],[True,False,True,False,True,True,True,True,False,True,True,True,False,False],[True,True,False,True,True,False,False,False,False,True,False,False,True,False],[False,True,True,True,True,False,False,False,False,True,True,False,False,False],[False,False,True,True,True,True,False,False,True,False,True,True,True,True],[False,False,True,False,True,False,False,True,True,False,True,True,True,True],[True,True,True,True,True,False,False,True,False,False,True,True,False,False],[True,False,True,True,False,True,True,False,True,True,True,False,True,False],[True,False,True,True,True,True,False,True,True,True,False,True,True,True],[True,False,False,False,False,True,True,False,False,False,False,False,False,True],[False,True,False,False,False,True,True,True,False,True,False,False,False,False],[True,False,False,False,False,False,False,False,True,True,False,False,False,True],[False,False,False,False,True,False,False,True,False,True,True,False,True,True],[False,True,False,False,True,False,False,True,False,True,True,True,False,False],[True,False,True,True,False,True,False,False,False,False,True,False,False,False]],[[False,True,False,True,False,False,True,False,False,True,True,False,False,True],[True,True,True,True,True,False,False,False,True,False,False,True,True,True],[True,True,False,False,False,False,True,False,False,False,False,False,True,False],[False,False,True,True,True,False,False,False,False,True,False,True,True,False],[True,False,False,False,True,False,False,True,False,True,False,False,True,False],[False,True,False,False,True,True,True,False,True,False,False,True,True,True],[True,False,True,False,True,True,False,False,True,True,False,True,False,False],[True,False,False,True,True,True,True,False,False,True,False,False,True,False],[True,False,True,False,False,True,False,True,False,True,False,False,False,False],[True,False,False,True,False,False,False,True,True,False,True,False,True,True],[False,False,False,True,False,True,False,False,False,False,False,True,True,False],[True,True,False,False,False,False,True,False,False,False,False,False,False,True],[False,True,True,False,True,True,True,True,False,True,True,True,False,True],[False,True,True,True,True,True,True,True,True,True,True,False,True,True],[False,True,True,False,False,False,False,True,True,True,False,True,True,True]]], dtype = "bool")#candidate|667|(16, 15, 14)|const|bool
bop_668 = relay.minimum(bop_663.astype('int32'), relay.reshape(const_667.astype('int32'), relay.shape_of(bop_663))) # shape=(16, 15, 14)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_679 = relay.TupleGetItem(func_312_call(), 0)
call_680 = relay.TupleGetItem(func_313_call(), 0)
bop_689 = relay.logical_xor(const_667.astype('int64'), relay.reshape(bop_663.astype('int64'), relay.shape_of(const_667))) # shape=(16, 15, 14)
output = relay.Tuple([bop_668,call_679,bop_689,])
output2 = relay.Tuple([bop_668,call_680,bop_689,])
func_697 = relay.Function([var_661,var_662,], output)
mod['func_697'] = func_697
mod = relay.transform.InferType()(mod)
mutated_mod['func_697'] = func_697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_697_call = mutated_mod.get_global_var('func_697')
var_699 = relay.var("var_699", dtype = "float64", shape = ())#candidate|699|()|var|float64
var_700 = relay.var("var_700", dtype = "float64", shape = (16, 15, 14))#candidate|700|(16, 15, 14)|var|float64
call_698 = func_697_call(var_699,var_700,)
output = call_698
func_701 = relay.Function([var_699,var_700,], output)
mutated_mod['func_701'] = func_701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_715 = relay.TupleGetItem(func_312_call(), 0)
call_716 = relay.TupleGetItem(func_313_call(), 0)
output = call_715
output2 = call_716
func_720 = relay.Function([], output)
mod['func_720'] = func_720
mod = relay.transform.InferType()(mod)
output = func_720()
func_721 = relay.Function([], output)
mutated_mod['func_721'] = func_721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_735 = func_720_call()
call_736 = func_720_call()
output = call_735
output2 = call_736
func_742 = relay.Function([], output)
mod['func_742'] = func_742
mod = relay.transform.InferType()(mod)
output = func_742()
func_743 = relay.Function([], output)
mutated_mod['func_743'] = func_743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_757 = func_720_call()
call_758 = func_720_call()
uop_773 = relay.asinh(call_757.astype('float32')) # shape=(4, 4, 16)
uop_775 = relay.asinh(call_758.astype('float32')) # shape=(4, 4, 16)
bop_785 = relay.logical_or(uop_773.astype('bool'), relay.reshape(call_757.astype('bool'), relay.shape_of(uop_773))) # shape=(4, 4, 16)
bop_788 = relay.logical_or(uop_775.astype('bool'), relay.reshape(call_758.astype('bool'), relay.shape_of(uop_775))) # shape=(4, 4, 16)
func_256_call = mod.get_global_var('func_256')
func_260_call = mutated_mod.get_global_var('func_260')
const_790 = relay.const([0.600741,-5.432292,2.304359,-0.218091,-0.649122,-4.990151,9.275003,-2.071068,2.234853,-1.438226,-3.174999,9.215478,4.949179,5.521182,6.810083,8.370037,-9.603018,-5.011118,0.005487,-5.004405,7.653083,4.946579,-0.876330,1.176314,8.734020,9.387819,7.564031,3.460298,0.138290,6.420025,-3.127120,-8.206032,-2.755699,-6.222791,7.985221,1.443781,1.698078,-3.865976,-5.229166,6.835378,1.097077,9.189671,4.694717,-2.105812,-5.202503,3.930082,-1.266762,6.188544,-5.246717,-3.968645,-7.070643,-1.009078,-5.083570,1.208395,2.535019,1.570484,-5.254776,6.343035,8.328187,-9.971054,9.744174,-9.530335,3.352807,-7.210084,0.156671,-2.051497,-4.025551,1.361390,2.001091,-2.660071,6.920097,9.184631,-5.957432,6.986504,-6.767841,0.750335,8.984370,3.824877,4.889490,2.042687,-7.822521,-5.267532,-5.025483,-0.355208,6.049767,-8.843307,-2.574055,-9.843703,-8.375823,-5.587438,4.227617,-1.849157,3.456929,-6.333855,8.512792,8.862037,1.763024,7.225876,3.734246,1.666477,-3.395244,2.487523,9.767638,6.013452,7.849501,1.066716,-9.754811,0.057585,7.631530,-6.946265,7.027981,5.488015,-7.674363,2.091130,-0.350417,-4.823633,-3.731988,1.348263,8.376947,-7.971228,-3.128825,0.330804,8.155165,-6.806698,-2.673417,-5.005872,-5.629958,-6.616156,-5.767617,-1.035903,-2.350326,0.505564,-1.506758,3.375308,7.110607,-6.492401,4.799026,-0.936644,-6.984462,5.324040,-7.712569,7.492853,3.182478,6.347215,8.704281,-6.320196,-8.244724,-6.666926,-5.272808,-3.912861,8.645754,0.785726,-5.232914,-7.237118,-8.356324,-0.033503,4.199778,9.146985,3.678894,-2.409919,-5.469167,0.940161,-1.921941,4.626947,7.826934,-9.141792,-4.154989,3.594083,-9.952427,-6.375354,2.046198,4.478578,-8.837491,-9.718102,1.105497,-7.240028,8.774523,-2.825770,1.703579,7.579559,3.511534,-4.802407,3.071045,-5.287128,8.760066,9.172209,7.719600,5.491256,0.953924,-7.385484,-9.508550,5.840503,-0.434937,6.638258,8.253461,-6.931876,-7.575748,3.398951,-8.091666,2.188694,-1.703415,-2.350826,4.282295,6.370231,0.617975,9.075733,-1.505096,-0.469978,-4.598929,-8.109410,-6.507429,-8.731841,1.743141,-0.793621,-6.064946,8.082151,-5.798124,-7.897982,2.382825,6.171903,6.261381,-7.530476,5.563754,-6.737926,-5.754161,2.206977,6.732607,-6.336572,4.458476,-3.436851,-3.948498,-7.031046,-5.111125,9.248849,-2.315975,-6.254465,6.751851,1.560395,0.699297,2.997538,4.910249,-4.301881,-5.020867,7.916458,-8.156545,1.406447,-0.670329,2.782368,3.006304,-7.119910,8.835511,4.306789,-6.333232,9.346523,0.947128,4.199846,-9.541683,0.436566,-0.129703,-7.360147,0.194105,-2.941086,-3.787131,-1.696036,-4.645012,0.524789,5.933761,-8.116394,-3.224791,-1.471012,-6.865770,-7.749319,8.900970,-7.150199,-8.135620,-8.103238,-7.387861,3.532917,9.601227,-9.262498,3.907648,6.603509,8.048321,-9.773544,-6.129018,6.734229,-5.897472,0.485922,4.537174,-5.432424,-0.160104,8.407913,7.877340,2.192419,-1.010645,-7.352498,-1.997755,8.912864,6.879998,1.271041,-8.250253,0.165170,-3.714588,-5.694856,-8.431672,8.891857,-7.822797,8.822864,-4.784216,-6.841046,5.271910,-5.345541,-4.490885,8.006787,1.411264,1.549334,5.103795,-0.465884,3.199939,3.582839,7.858265,9.880163,-5.591249,8.896911,5.465309,2.962643,-0.102974,-3.812064,4.000205,5.064627,-6.186218,-7.895085,7.508783,0.681788,-4.402934,-6.920628,-3.954477,2.112868,-2.872623,2.245597,-3.653265,-7.373573,-6.904514,8.377171,-4.557094,-5.770645,-1.152880,-9.302888,7.799643,-6.609859,0.825553,-1.606020,-6.479898,-5.984004,-5.581390,7.073359,-6.491843,-0.388299,-2.985983,3.385760,-1.264024,-0.729589,-9.923033,-7.888015,-5.361540,7.211565,6.334417,6.030421,6.290940,-6.595697,6.090300,-6.355607,-1.977264,-4.134878,3.867282,2.393790,6.707054,-6.728067,5.172321,-7.302467,4.649753,0.812272,7.473844,5.809544,-7.955943,-5.571312,0.837461,4.161425,1.562392,-3.708081,4.522627,-1.060628,8.117837,9.337297,7.632348,2.509049,4.088793,1.178324,4.767228,-9.505681,0.163605,-2.417734,2.650178,-4.941965,3.242535,2.990646,-2.149448,-0.254922,-4.016549,-2.351671,1.941758,2.568986,-5.228784,4.152456,3.558087,5.497637,-9.887421,1.870472,-5.757298,1.775542,-1.635201,-3.225885,-8.852932,8.579467,-7.502576,1.345236,1.311570,9.846528,9.127877,0.124185,-5.672790,3.202941,-8.503063,-9.317001,-9.072706,9.209058,5.114100,-2.991406,-4.921378,-5.393365,8.604985,-9.522803,-8.921339,9.689071,-7.821089,-6.946478,6.557672,3.613696,-3.856282,-1.433964,6.898865,-6.213487,-5.529260,0.796379,-2.859659,3.929371,5.076079,-4.123759,6.717186,5.161173,-0.179002,-7.079998,-6.343507,-2.335170,-0.102447,6.590324,-4.560786,-7.791241,-9.987855,9.110264,0.324889,4.482814,-2.899953,3.767116,7.080256,6.768484,-1.662992,4.296080,7.434573,-8.131600,8.298127,-7.088565,0.393558,-6.761445,-2.393192,-1.522630,-6.344793,-9.102477,3.941820,0.171437,-7.650259,-7.199693,-1.753783,4.228158,1.743174,4.861396,-9.625141,-7.552546,-0.168934,6.120362,-6.646192,2.193166,6.803935,1.095758,9.471655,5.129506,4.738268,-8.471501,-4.111143,-7.422727,3.946654,-6.050778,9.134046,8.978811,7.549731,-6.280027,-5.895297,-4.760996,0.564610,-9.785927,-2.447905,-9.732003,-2.964536,-3.123688,3.013269,-7.923291,-4.481359,-1.172352,-2.230862,-3.105562,-9.566214,9.200079,-0.932137,3.269959,-6.406539,-5.253753,1.803403,-8.897355,1.945354,-6.812593,4.333656,-4.701955,0.153959,9.161970,-2.362270,5.050153,-5.898390,-9.379186,0.800453,-7.807594,9.256679,-7.941817,-8.616197,-1.640168,6.596379,-9.103580,-9.709790,6.302260,0.219388,9.053317,-1.632531,-9.421800,0.090526,4.465617,-6.054391,-6.862573,-3.549389,4.666514,-9.977661,-5.541078,-0.084419,-5.450071,8.565421,8.738218,0.489448,3.411414,7.276850,-3.526017,-7.483774,4.381217,-3.447204,-7.248088,6.274045,9.826346,-0.699964,7.434912,-5.241117,8.462403,1.064967,-0.573718,8.698885,-5.384655,2.532169,7.811663,-3.490723,5.588378,3.121175,5.512540,6.240348,-3.989397,8.373136,-6.886318,6.496748,0.243908,-4.339380,0.417635,3.972396,0.770985,8.148054,-9.670662,2.430977,-1.693619,-8.045481,9.736377,-1.778548,4.276127,-4.857241,0.827397,9.327809,-9.050314,-2.558519,9.097212,-1.157422,-1.946031,4.416384,9.184058,-2.287935,3.735571,-6.891494,-1.200616,-1.340198,-1.795478,-0.737535,0.357411,-6.895878,6.725030,4.031264,9.217495,2.042714,1.938172,-3.434744,-9.701577,-3.875493,6.605088,-5.575040,7.435035,3.315676,8.421547,7.950523,7.154978,7.236374,-5.944186,5.819348,-6.908141,-2.566319,-8.036569,-2.636230,3.133489,-7.848542,6.648880,6.964424,-4.406616,-2.976159,-4.888896,-9.863447,-8.811862,-1.600763,-0.323970,-8.464564,8.822835,7.799702,8.527146,-9.450470,-2.862098,-4.535951,9.665887,4.358268,-7.187754,-0.833016,6.653824,6.278844,-4.818770,2.502441,0.406035,2.569821,-3.343458,-4.333800,-1.968920,-3.209651,-3.529792,7.236468,-6.553014,6.285806,-1.102402,8.654550,-0.857133,6.692399,1.953809,7.350667,-4.130774,9.418480,5.966500,6.982725,-1.530625,0.636424,-2.230594,-1.292100,5.229262,3.152428,5.927127,9.640183,4.572003,-1.677243,7.968129,-8.917474,-0.913532,-8.482336,8.627742,-0.596747,-8.038434,-2.727175,-6.855491,6.303889,-8.164246,6.773563,-8.791609,0.314166,-7.423492,-7.936549,-8.106229,1.824273,-1.131430,-8.646056,8.376010,0.554337,-1.674920,-1.492666,-4.283334,-2.454134,4.221966,1.835245,0.032900,4.640789,-6.963704,9.375394,-5.068046,-3.457496,9.159070,4.403051,6.583221,-7.156283,-4.114788,-8.243374,-6.703406,-6.339322,-2.608485,3.278402,-6.479875,2.344232,-9.849013,2.665900,-6.511277,8.938390,1.300969,-4.173579,4.819399,-3.264306,-5.964345,1.904021,-5.344269,-8.409010,1.783130,-0.757347,-6.039064,-6.143964,-7.134654,-9.517470,4.487840,-4.389026,-0.940716,0.178249,3.989992,0.527132,-9.272126,2.769488,-9.976423,-3.361473,0.457878,-1.391821,-4.592776,0.196138,-6.544060,9.876121,3.412429,-1.404025,8.139134,-5.042883,-5.034502,-6.151858,-8.179431,1.419892,6.032890,-3.588715,-6.589190,-7.806083,2.577729,1.680898,2.894127,-8.953709,4.681170,-1.040345,-7.112624,8.112765,1.720726,-4.618468,7.348302,-7.759562,3.540503,-2.576916,7.425364,-4.984957,-9.273294,6.978604,2.244527,-9.232726,-1.410342,1.392999,0.854271,2.542659,-6.288879,-6.441285,0.835893,-5.563570,1.893945,-9.695955,3.104783,-2.489589,9.787604,-2.043055,3.972203,7.435822,6.323681,-1.658613,2.206011,3.865125,4.701361,-3.912146,7.664858,5.906148,3.898685,2.887141,2.599520,-7.307376,0.455676,2.031501,0.048084,1.169837,7.162430,-2.086117,0.127660,-0.221278,7.895473,-7.595018,4.540856,-5.300629,0.946115,4.626125,2.200325,3.437658,-3.451133,0.354910,8.693675,2.657601,-9.754139,-5.750147,1.884815,3.648301,5.518661,2.113169,7.912992,0.024910,-7.078313,7.838065,-7.444665,-5.994315,2.677834,-9.991699,-9.737447,7.941208,5.371149,5.963456,-6.299470,-8.717467,-5.270975,-2.375517,1.374002,-9.425707,1.320630,5.206260,1.547230,-9.083428,6.518924,0.623802,-7.510330,-3.495368,-6.987685,7.615004,-9.352268,-5.796760,4.586314,4.558653,-3.934054,-7.921910,0.093992,9.086802,-6.528904,-8.084986,1.463395,7.906540,-7.025514,3.921101,7.911321,-9.987119,-9.942982,-1.332492,1.716093,-6.747267,-3.510841,1.410030,-7.801239,-8.372171,1.947802,-1.590167,-8.381489,-9.087868,-0.414987,-3.153762,-9.012110,7.827579,2.345927,8.208645,8.532043,3.957221,-0.509881,-5.983294,4.421464,0.245823,5.572890,0.913570,-7.013279,-1.375875,-2.163376,-2.422907,7.311434,1.657351,-3.152528,-4.784482,5.858473,6.354987,-3.404474,-3.208578,-6.884263,-4.625628,-8.996473,7.883960,-9.807999,9.514659,-2.032077,7.712300,6.170091,9.242607,3.150361,-3.542221,0.121575,9.993554,9.251317,1.990144,3.635913,9.797256,-2.495269,-9.129453,-6.578714,5.312736,-8.394252,0.709673,5.394229,4.573968,-3.450861,9.855148,2.350982,6.298942,1.242864,-6.243641,7.262858,-4.758778,-9.149564,-2.055867,-8.092150,-3.135522,-8.666611,-7.448436,-2.245922,8.416710,2.534095,-9.192418,3.082703,7.212991,-8.275302,6.744874,9.406216,2.117987,5.845904,3.679450,9.937638,-5.750340,2.485336,-1.251135,-3.886856,-3.425798,-6.252131,-7.629576,-4.623463,-4.244504,6.833547,-7.330923,6.775648,-2.378234,9.869025,-1.361698,3.236739,8.613020,-3.457399,-3.484211,6.548430,-7.327648,8.672840,3.939620,0.414657,0.944884,4.528543,5.431725,7.949989,9.162388,6.010475,-6.147963,-8.991984,7.307183,0.404819,3.022205,-3.478808,-6.556015,-9.295313,-9.887187,-0.830018,-9.566654,5.146249,-2.260548,-8.522489,-8.416609,-3.430163,-9.857038,-8.188313,0.357487,-5.578470,-6.623765,-6.230503,-3.734744,-1.943981,-1.445281,-7.316490,-8.179746,4.627608,5.106574,1.031080,6.674389,-2.549345,-0.603591,-4.033690,-3.471128,4.449355,1.722135,4.510186,-7.721831,-4.041059,-4.284540,-9.162870,7.139220,-1.557597,5.740157,-2.627145,8.280701,-6.852382,7.138319,9.708397,4.319935,-0.906657,-8.807191,9.243319,5.249012,-3.421420,-9.142867,-5.062245,-1.676211,-5.723028,-3.323165,-9.549276,2.488573,-5.307704,9.915434,-9.950073,-6.280576,-8.638524,5.887964,1.277460,4.524318,-6.465912,-2.925368,1.423219,9.918268,-9.394992,-6.024744,8.364848,-2.069043,-4.932457,4.906109,-7.692224,6.911870,2.433691,-9.128355,9.235573,-2.688149,-2.365645,4.271411,2.243168,8.422137,-7.051850,-4.982603,-1.338299,7.398282,2.114282,6.255937,-5.556914,-8.306550,4.523950,8.501831,-2.374116,5.384364,-3.066416,0.199046,3.344209,-2.511205,-5.623484,-7.169737,9.294402,-0.899769,-0.103353,-8.749705,-1.936513,-6.824933,-1.852925,3.434555,5.069715,1.215896,7.160828,9.595635,0.674096,-7.595251,8.581084,-3.608490,3.858820,0.420772,4.554541,-5.201258,-4.288548,6.739514,-1.588847,1.000549,1.225606,-7.598515,5.670831,-9.229531,9.004126,0.046654,2.274888,9.837655,-9.350073,-8.939562,-1.199116,5.562167,-3.164851,8.947084,8.133177,-2.513088,9.073750,0.337156,9.619063,-6.641661,5.183123,8.847517,5.154917,5.634204,3.981800,8.118880,-4.905315,-2.184620,-8.315955,-4.530304,-4.917391,-3.153411,3.670697,5.270807,0.214379,5.156082,2.221669,8.988095,9.048397,-0.518161,8.777046,-5.423773,-0.653196,-5.026869,0.883833,5.552524,2.786241,2.556539,7.106487,3.896452,-7.824704,1.996542,8.966535,4.584388,2.715921,9.485904,4.799202,9.010872,-1.082466,-5.198967,-0.074353,-6.791564,-3.162843,-9.649246,-0.533256,-2.838277,-6.007289,-5.681956,1.860653,-8.305479,1.928813,5.457759,0.295441,-0.591695,-1.760245,3.754069,-0.554545,-2.602307,-0.249589,2.680145,5.096780,2.988946,2.827491,9.889472,1.676506,-7.961428,-4.289771,-9.269851,-1.806037,2.671283,7.694227,8.848961,-1.592337,-1.483606,-1.569369,0.067339,-5.193260,7.192824,-4.684482,-3.981625,-8.581513,-8.289184,-6.198107,-8.652704,-1.381696,3.541596,6.726013,6.892999,-8.909018,-8.592835,8.146572,-8.976187,-0.573795,-4.678241,0.858215,2.558498,8.216641,-5.932501,-6.490987,-7.690630,-8.584135,-9.734185,-1.913135,-2.654937,-6.940004,4.441169,-9.507530,8.455072,9.697229,-2.943836,-2.900734,-8.130705,0.548287,5.862274,5.401067,-9.071235,3.099068,9.973454,0.264123,-1.410797,-2.916729,8.245927,-5.787190,-6.317102,-8.337920,-2.020235,-1.848796,-5.574652,6.651992,8.649894,0.309385,-5.796934,-0.092410,-3.209223,6.901962,5.043272,-7.059336,2.043113,1.705915,-6.624714,-3.627093,-7.105687,3.135246,-4.978227,-9.482870,-5.681558,-2.481545,-1.599553,-7.768246,-0.175198,-9.946851,-9.163534,-3.102770,5.205359,0.180498,-4.030889,-7.906079,-7.730901,4.971503,-6.076485,-8.923779,-2.793770,0.831050,8.504129,4.551878,-0.165259,-9.017131,8.653115,-1.641224,-3.431283,-7.672634,1.478900,-2.970968,3.034532,-2.520011,5.532516,-9.210038,6.263993,7.237465,7.228011,-2.060310,-8.558610,-8.391257,-1.763959,-1.119300,-3.289518,8.868015,6.482087,8.176732,0.752925,-3.974154,-9.855883,-7.097700,-1.953815,6.068023,7.331681,6.153189,-4.479733,9.762781,-0.333864,0.475844,-1.256495,-6.613063,-9.094256,-5.305911,-8.269457,8.392821,6.906811,-8.116283,2.359296,-6.397496,-9.238274,-8.590674,6.297212,7.142282,7.821921,2.283281,2.376523,1.295053,0.406767,0.540738,-3.919586,7.156729,3.786966,8.300893,8.003225,7.112839,-6.478462,-0.821318,8.405638,4.124603,-8.982509,-8.847897,5.696464,-5.661986,-2.514433,-5.339413,-9.084317,-1.219784,7.426237,-0.955747,2.380310,-1.822609,2.793529,-9.865544,-1.581486,9.016417,-9.462539,-6.235954,6.856031,-3.605910,6.782332,-3.638880,-3.559912,8.610771,-0.739042,-0.736661,1.216124,7.822467,8.222426,6.131454,-0.848129,7.570879,-6.837812,-7.916014,-9.131689,8.977953,3.915847,8.036041,3.259296,0.178190,-1.198139,5.983041,1.794290,-1.084909,-9.809018,-2.801287,-0.731470,0.019290,-2.821438,-9.952918,7.226654,-7.786562,2.549362,-9.371336,-5.591071,-7.170160,-9.675992,-5.019062,5.609917,-7.090133,-2.248045,-1.345485,-7.019034,1.622379,4.767295,5.125302,-7.916250,3.189989,1.004832,-4.654204,6.391380,-2.373596,-3.250179,4.298385,7.157562,-2.016573,1.091350,-6.315407,-3.118428,-9.270667,7.951636,-9.911092,6.023325,7.862282,-6.841917,-2.196998,8.484717,5.956626,5.047151,0.126959,-5.174703,-6.248133,-7.912206,-4.721973,-2.627597,-7.288681,-2.635855,5.543289,-4.964613,0.593982,-9.579380,-4.411543,-3.904619,-1.627186,2.708666,2.596047,5.376817,2.833265,-6.686467,-7.339012,-5.885048,5.592735,-1.485871,-8.037073,4.563569,8.036281,3.740654,3.181911,0.793048,8.153871,9.977669,-1.052046,-7.251728,-3.812459,2.885704,5.551108,6.716484,9.789401,-9.065711,-1.702425,9.196970,9.189836,-0.678641,-0.702605,-2.184265,-3.704483,-7.968080,-9.792406,-7.956605,-0.223020], dtype = "float64")#candidate|790|(1568,)|const|float64
var_791 = relay.var("var_791", dtype = "float64", shape = (32,))#candidate|791|(32,)|var|float64
call_789 = relay.TupleGetItem(func_256_call(relay.reshape(const_790.astype('float64'), [14, 7, 16]), relay.reshape(var_791.astype('float64'), [32,]), ), 1)
call_792 = relay.TupleGetItem(func_260_call(relay.reshape(const_790.astype('float64'), [14, 7, 16]), relay.reshape(var_791.astype('float64'), [32,]), ), 1)
output = relay.Tuple([bop_785,call_789,const_790,var_791,])
output2 = relay.Tuple([bop_788,call_792,const_790,var_791,])
func_794 = relay.Function([var_791,], output)
mod['func_794'] = func_794
mod = relay.transform.InferType()(mod)
var_795 = relay.var("var_795", dtype = "float64", shape = (32,))#candidate|795|(32,)|var|float64
output = func_794(var_795)
func_796 = relay.Function([var_795], output)
mutated_mod['func_796'] = func_796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_982 = relay.TupleGetItem(func_312_call(), 0)
call_983 = relay.TupleGetItem(func_313_call(), 0)
uop_984 = relay.exp(call_982.astype('float64')) # shape=(4, 4, 16)
uop_986 = relay.exp(call_983.astype('float64')) # shape=(4, 4, 16)
output = uop_984
output2 = uop_986
func_989 = relay.Function([], output)
mod['func_989'] = func_989
mod = relay.transform.InferType()(mod)
output = func_989()
func_990 = relay.Function([], output)
mutated_mod['func_990'] = func_990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_482_call = mod.get_global_var('func_482')
func_484_call = mutated_mod.get_global_var('func_484')
call_1003 = relay.TupleGetItem(func_482_call(), 3)
call_1004 = relay.TupleGetItem(func_484_call(), 3)
func_256_call = mod.get_global_var('func_256')
func_260_call = mutated_mod.get_global_var('func_260')
var_1013 = relay.var("var_1013", dtype = "float64", shape = (1568,))#candidate|1013|(1568,)|var|float64
var_1014 = relay.var("var_1014", dtype = "float64", shape = (16, 2))#candidate|1014|(16, 2)|var|float64
call_1012 = relay.TupleGetItem(func_256_call(relay.reshape(var_1013.astype('float64'), [14, 7, 16]), relay.reshape(var_1014.astype('float64'), [32,]), ), 2)
call_1015 = relay.TupleGetItem(func_260_call(relay.reshape(var_1013.astype('float64'), [14, 7, 16]), relay.reshape(var_1014.astype('float64'), [32,]), ), 2)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_1016 = func_720_call()
call_1017 = func_720_call()
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_1019 = relay.TupleGetItem(func_312_call(), 0)
call_1020 = relay.TupleGetItem(func_313_call(), 0)
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
const_1026 = relay.const(-5.468117, dtype = "float64")#candidate|1026|()|const|float64
const_1027 = relay.const([[5.737211,6.143845,-2.201406,0.744298],[9.086428,7.554822,8.970621,7.024787],[-6.080419,-2.464504,0.941877,-9.425803],[6.575286,0.014636,-6.025691,-4.637251],[-2.204232,2.441528,5.410532,-2.037190],[-6.649171,-7.596824,4.493945,-5.645765],[-7.775508,-8.414865,4.018426,7.533297],[-5.650364,-2.203382,0.144048,-3.501043],[-9.945449,-5.078886,-6.661012,-0.272760],[-6.421650,8.087439,-3.988517,-4.007203],[-3.936996,-4.563190,3.422998,3.447225],[-1.332898,-6.374041,-8.816142,1.466761],[2.945505,-1.531769,8.019799,-7.448009],[-7.256091,1.959676,9.022675,5.492977],[-8.522754,1.745405,9.114046,4.062609],[-3.439262,9.219527,3.545745,1.612158],[1.777117,-6.915665,-1.343735,-0.534129],[-7.474696,2.372008,1.908471,-6.786200],[8.758421,6.281453,-2.032243,-2.606115],[6.946286,0.027943,4.079534,0.716347],[3.389341,8.149749,-2.349257,-3.023233],[8.060403,-3.907691,-4.079117,2.263831],[4.185161,-2.712990,9.644782,-5.223657],[1.824281,0.171008,9.811241,3.601784],[4.677466,-1.503911,-6.767490,-4.879110],[1.013086,7.020616,5.588318,6.432659],[7.745570,-2.342083,-1.245990,8.713050],[4.394392,-2.104908,6.693767,8.267801],[-8.850120,-8.253000,-4.842339,7.919188],[-7.794550,7.167518,4.288900,-8.172045],[-2.358487,7.259751,3.302984,-8.794587],[-9.653065,2.342332,-2.704914,-1.501508],[5.336413,-2.490382,5.851632,4.136946],[-9.735075,-0.695302,7.757786,-6.676096],[9.295139,-8.605384,1.941236,2.389903],[-9.294562,8.582174,4.149674,0.440946],[1.165811,-6.927483,4.309877,-2.688302],[-9.260952,8.483715,6.630224,-2.005969],[-5.667783,0.429009,1.512600,3.139705],[-2.569917,1.564865,-6.824102,-6.097400],[-2.799442,-9.790931,-2.634306,1.737712],[5.656488,-7.965592,-8.613665,-1.025281],[3.529971,-0.402145,-4.618722,-0.809073],[6.065310,2.240955,0.946280,6.801482],[-1.072765,8.401507,-1.657839,-7.502685],[-8.579655,-3.857096,6.524083,2.687580],[-2.214165,1.618936,0.366806,7.567990],[1.095568,-9.475801,-4.512643,-2.253665],[3.347793,6.747851,-3.223830,-0.741530],[-5.189993,-0.363129,3.990882,4.613448],[1.634507,-8.349414,-8.541976,8.688991],[-7.143491,-6.943031,8.910908,-9.989794],[7.329646,-2.381140,1.311763,-0.691465],[7.309787,1.468885,-5.479737,5.255472],[7.588944,-7.914864,2.258828,-1.200172],[0.043140,7.888442,1.887362,6.925045],[9.212561,9.432792,-4.016829,7.596175],[-4.374776,-7.572941,2.520018,-3.768571],[-4.823492,-4.654092,8.242967,5.884951],[-7.050146,7.249634,-4.696608,-2.741685],[9.431023,-3.046230,1.532227,0.299274],[-4.218412,-7.594548,9.484465,5.587040],[1.726291,-0.111641,-7.447694,9.717485],[-5.036868,-4.832285,9.293333,-4.180540],[-7.638850,8.640083,-1.750592,8.068017],[-4.826612,-8.311052,1.720152,7.029016],[-1.770189,0.471398,-0.639491,5.408115],[1.089850,5.858136,-8.467021,8.963724],[4.297759,-7.120487,-9.006496,-8.495444],[9.298964,-7.676492,-6.188936,7.230720],[1.487425,4.132097,7.137952,-4.367564],[7.325010,2.080962,-1.562445,-8.468361],[4.795349,0.724507,4.980932,8.056872],[9.297520,2.169733,7.300411,-4.458184],[1.849883,-5.094229,-0.410594,8.174682],[4.724974,0.244989,-3.656713,8.095237],[-0.499506,9.297559,-3.262164,-1.018768],[-2.980842,-1.244270,-5.493106,5.892329],[-2.985167,-9.788347,-1.089735,-6.737162],[-6.619304,2.348962,-3.669185,2.020740],[-1.205832,-2.233065,2.043474,-5.434458],[-2.158915,7.516504,6.665669,-0.848796],[7.541423,-6.619315,-8.577101,1.633396],[-1.339564,5.218250,1.098093,5.562809],[7.899481,-4.117421,-5.214541,3.934858],[3.133441,3.213937,1.816217,9.040778],[-8.389658,-0.596994,-6.138389,7.512698],[3.816333,6.002199,4.388656,-2.928566],[-5.052172,6.714451,2.562085,8.543829],[-9.453393,2.996012,-8.365136,-0.845984],[-6.191847,-4.280097,-5.457122,3.480496],[-3.992367,-4.919977,2.482606,7.479817],[3.199295,-3.278591,1.363932,-1.614377],[-0.218423,7.211522,-9.941011,1.924187],[-0.752384,4.099204,8.821456,-1.104435],[-8.530294,-8.133738,2.618305,0.415129],[-9.063480,4.749584,-8.243351,2.797171],[0.158507,7.361749,-4.930823,-9.092230],[-7.456480,1.899735,-4.606932,-7.788495],[-7.522743,-7.782758,-4.088162,3.137447],[8.180220,-9.277976,-4.261815,-9.263963],[-3.643583,7.782036,-9.704491,1.322143],[0.809620,0.179973,4.802231,-6.337906],[-6.173025,8.880339,0.078465,0.382766],[-3.497398,-1.197039,-2.807438,-2.749006],[-4.780410,5.044510,-1.440162,-6.061041],[-9.932549,9.437062,9.079478,4.528410],[5.004810,-5.195145,2.132023,1.334451],[6.940693,-4.805904,2.188717,-4.924730],[-6.114510,-3.510297,-2.438423,5.005186],[-8.319608,-9.935324,-0.987988,2.837541],[4.577515,-2.408555,-5.212487,-4.723192],[9.400110,4.266109,7.012152,3.192850],[7.504006,-1.042539,-0.897839,-7.878437],[5.830997,-5.443844,8.440985,0.727530],[0.767739,4.844498,9.024855,4.619215],[4.419092,5.777161,-8.821649,-6.189206],[4.473286,3.289864,-6.393124,-8.889541],[2.421109,-0.686173,3.911147,6.112785],[0.196452,-0.974906,-3.812466,-3.538095],[-8.244030,-0.726282,-7.788596,-4.911068],[-1.554509,7.359276,-5.743887,-6.616940],[-6.570943,-3.096647,-2.451880,-9.163014],[-4.222408,-1.504552,-8.710265,-4.371170],[1.589303,9.360285,-6.242333,0.276689],[0.990691,3.184800,-6.254485,9.376165],[-0.075487,-4.601746,3.506394,0.541589],[7.236986,-6.412731,-6.930647,-1.088910],[-5.668313,0.651474,-5.813834,1.351408],[2.572585,4.665879,-5.291174,-7.005358],[-8.150145,7.710943,8.522499,5.241301],[-1.425277,-2.227673,6.018262,-7.560628],[-0.473616,-8.328020,-7.402333,-4.900932],[-3.142608,-8.643193,2.886621,-5.860443],[0.119833,0.210674,-1.982848,-6.101534],[0.181410,2.545950,3.147805,-5.143092],[6.267252,-5.378724,-8.632652,4.356881],[-4.747664,7.469703,-3.367057,6.452428],[3.050767,-7.284847,-4.581113,-1.005491],[9.734552,-0.293335,-1.542638,-8.462927],[1.286874,1.125454,8.642620,-4.739219],[-4.443785,2.747080,0.871427,2.376619],[-2.164761,-6.911485,-0.521470,-1.679709],[-4.945731,-7.897775,7.528061,-2.433766],[-0.420446,-6.647251,-0.102972,8.455983],[-6.574739,2.571530,-3.437705,-9.365519],[-3.310107,3.277303,9.390467,-9.483371],[-5.747165,-4.830544,5.017875,-5.546366],[9.038756,-1.893805,8.952550,-0.220087],[-7.772324,-4.573202,-5.467186,7.544735],[5.188747,8.924088,-4.111777,3.814303],[4.688612,-3.352372,-9.451249,-7.633123],[8.922693,-3.326634,-0.213025,-9.921246],[-4.064959,2.297540,7.479837,-2.510565],[8.457099,-0.137687,2.702961,-3.785166],[8.880047,-5.180362,8.897450,3.962278],[7.748563,-8.821176,7.123291,-9.138149],[9.607441,-1.731389,9.200104,5.536831],[5.457578,-4.320534,3.138709,1.403671],[-5.103750,1.736949,-6.561315,-0.331509],[-3.573522,9.997847,-2.053261,5.068454],[-5.410048,-3.049608,-6.854406,-7.645224],[6.420011,3.756134,-3.665338,-6.052426],[-6.589422,-7.803299,-2.418977,-9.471929],[5.481742,-0.224836,6.690658,5.083519],[-7.597817,3.336259,-8.152270,-5.753517],[7.020315,-2.960328,-0.650170,-4.715323],[-7.173625,8.885813,7.851961,7.485718],[8.713145,-1.047108,-8.436497,-0.732368],[-5.924470,1.215816,-2.631609,-3.772167],[0.445061,7.722852,5.359773,-8.664642],[-0.655797,7.273279,6.980102,4.487400],[-8.856380,-0.752570,3.373261,2.691657],[-5.892771,-0.377905,-0.472479,-1.432229],[-7.481187,7.165616,6.928128,5.083691],[6.816815,-4.383898,-5.962764,-4.945900],[5.447088,6.889392,0.191951,-9.155121],[6.576554,-5.548711,-7.554358,-2.244052],[-0.577992,-3.691905,0.151986,-2.014949],[-3.186249,-7.516001,-3.284945,-6.899918],[7.493645,-7.434965,-3.846596,-3.827367],[-8.966030,-8.732899,-5.926737,0.958758],[-9.865243,-4.175485,1.793826,2.798692],[6.923666,-3.754120,-1.340917,-2.110762],[-4.806440,-3.559544,6.805547,9.235381],[-4.691287,-2.863371,-7.520894,4.647043],[-7.975570,-3.273262,-9.409975,5.574342],[9.541892,1.794143,-4.583622,9.660131],[3.641681,-9.168139,9.864261,-2.669719],[0.633104,-7.150196,-6.701527,-9.919084],[6.240138,-7.581647,-7.543732,-2.346371],[-5.081190,2.834401,4.515323,9.573724],[4.071492,1.855619,0.863067,-9.911344],[0.956152,-2.966550,-2.100325,-8.296189],[-1.279916,-4.078594,-2.383936,-1.065201],[-4.755209,-5.032020,4.754645,-3.500054],[2.683582,0.428442,5.420959,9.746313],[-3.958147,-5.680717,-5.318109,-2.620133],[-8.374426,-4.970794,3.448516,4.592594],[-2.437001,1.238354,3.750860,-5.905114],[-0.341667,-7.958273,4.441768,-3.332759],[3.606625,2.461707,4.866582,-1.611472],[-8.683562,-7.725768,-2.030787,2.102688],[2.395409,-1.841073,6.674023,7.630095],[-1.053440,6.035114,1.380193,3.829882],[4.088988,6.714944,-3.077072,-2.991908],[-9.737778,6.134092,-3.857672,5.105709],[0.785290,-3.712772,5.344031,-5.378187],[7.440781,3.872488,2.817159,-9.928364],[9.441219,2.481203,3.263475,-8.105147],[5.405832,-1.051396,3.600101,0.002092],[8.221807,5.441775,-8.459515,-2.596319],[8.305400,-8.269102,-2.558430,2.829694],[-1.891236,-1.937955,-6.887841,8.818452],[-0.601210,7.070643,-8.385876,-2.849842],[1.974653,-0.190628,-3.864192,6.141724],[-8.120542,-3.188004,-5.047258,4.032613],[7.464550,4.786578,-2.693562,1.646535],[-1.120957,-8.084475,2.987600,2.587661],[-1.684867,-2.428581,-7.694304,0.162755],[-1.065615,-1.409144,1.951582,0.860331],[9.871722,1.574601,-3.498961,-1.156260],[3.518054,9.908069,6.491139,5.917622],[-9.744201,-5.276480,-0.544281,0.233734],[-5.221148,8.268113,9.429610,-5.622601],[1.459911,9.878663,-3.374643,4.815946],[-7.523496,-7.188716,0.104005,-5.414120],[-7.184043,-3.865918,-4.328567,1.885141],[9.094140,-5.007264,4.274629,1.307852],[-8.604707,-5.845468,-9.108024,1.892782],[-3.338315,3.993327,4.219764,5.949338],[-8.859924,-1.055786,-7.909736,2.273319],[4.166199,-7.158396,-8.869742,2.055258],[-9.177510,0.053697,7.968901,-2.670955],[0.802988,6.097313,6.658964,-6.049093],[0.192628,-6.565000,-0.814603,5.382930],[7.455931,-5.043695,-0.386029,2.691078],[-6.144369,9.408373,3.384711,8.433248],[9.063152,4.693951,-0.509449,5.494602],[5.214182,7.353060,9.151281,7.142072],[-0.358250,2.431426,8.685617,-1.552126],[1.547926,-8.306580,1.183296,8.925048],[-4.177185,5.114393,-6.486378,-9.791997],[-3.090544,2.453529,5.131645,-5.009316],[0.901225,-8.045678,-5.752964,-4.605743],[-1.199722,-6.545216,-5.468601,5.822948],[2.434306,5.874103,3.739102,7.349250],[2.073378,9.898891,1.573882,3.146892],[4.529523,7.512827,-9.813470,-7.607679],[-2.307485,-1.710065,-8.382819,-3.144966],[-1.354240,-9.064400,9.470371,1.986639],[-2.777381,8.392916,-4.523527,-6.190297],[-4.152353,-9.396976,8.750499,-6.370313],[0.797263,2.127190,-3.769815,5.998251],[2.729758,-8.996141,4.546131,-3.496677],[-9.391129,8.711697,-4.749169,5.707767],[-5.202770,8.759985,-9.932113,2.875731],[-4.686863,6.184815,-3.533187,6.615263],[-9.679471,5.822812,5.446732,-6.652563],[9.782578,-0.204216,6.664338,2.956023],[4.886296,-5.866614,-0.602699,-2.327239],[-3.525818,8.276371,-1.884445,-9.300645],[-7.608135,5.521673,2.487768,2.320268],[7.578674,-2.286508,7.500496,-9.644132],[-7.150979,-6.097461,5.412469,5.206802],[2.056472,-4.503065,0.637395,-9.886125],[-1.909961,4.611743,5.139237,6.379854],[3.406804,-2.557624,6.066002,8.470589],[3.401181,-9.177835,-4.765261,-4.946672],[-1.692545,-4.603845,4.062874,8.854897],[-8.338444,-9.504377,0.157467,-0.727043],[5.411103,-1.719777,-6.964486,6.277220],[3.828543,-5.661123,9.595921,6.141425],[6.157657,-1.369495,1.541990,3.029919],[-6.834419,4.913470,5.721409,-6.539047],[-7.385888,6.767689,5.513543,-0.272598],[-5.554578,-0.480193,3.242285,4.319229],[0.843716,-8.433849,4.849443,-7.373640],[3.539223,7.081652,-2.032208,1.689415],[-6.362332,0.533674,7.781392,5.429751],[-7.719455,-3.435813,1.278770,-2.160419],[9.402668,2.081225,-7.921478,-1.002265],[-4.425342,-3.801233,-9.321179,5.515946],[-4.659024,-7.486357,3.319962,2.618405],[2.575251,2.641046,3.577374,-2.470787],[-1.807478,3.896496,3.865928,-3.626227],[-0.551326,-2.289391,7.602978,2.385993],[-7.866503,4.138360,1.393115,8.498849],[-0.870890,-8.784789,4.395631,-2.143545],[-0.456296,-4.430755,-8.291740,8.579025],[-5.685487,3.297800,-4.157365,1.405043],[-2.827270,-0.114838,-0.439300,-9.525294],[-4.670747,-8.348666,9.072339,-2.291771],[8.525462,-1.948739,4.531482,-0.174918],[1.438011,0.962750,-6.120077,2.899032],[-6.593725,7.747542,9.927558,8.060378],[-3.972385,6.383091,3.657876,5.881368],[5.341022,-6.781351,-8.269855,-2.752898],[-0.572339,8.117934,-3.651374,6.061668],[-8.367013,9.525856,-7.686033,4.977179],[8.684668,9.699037,-2.253469,6.294964],[-2.453460,1.793763,-0.457249,-5.161527],[9.870849,9.261751,-2.125698,-4.266058],[7.490399,5.962726,2.844817,-7.147953],[3.782609,3.434365,0.499758,9.286586],[-0.631451,-2.802026,-2.480827,7.933033],[-4.452982,-2.257572,4.131285,4.560532],[-7.157852,-7.787767,1.140497,-0.347967],[-6.473694,3.268826,-8.210633,8.884517],[2.470498,5.010417,1.594411,7.316473],[-4.978798,-0.607744,4.330743,-9.430811],[-5.407287,1.246841,-2.566341,4.684175],[9.391458,-2.045551,6.133830,-5.492988],[6.820595,3.307548,-8.966340,-6.917353],[-3.820615,-6.952003,-7.446425,5.418788],[9.773756,-7.688103,1.838952,0.595993],[-9.070058,-6.456077,6.804070,-6.397987],[3.918869,9.307913,5.821340,-2.782050],[2.517117,2.969909,6.229109,-8.046310],[0.121073,-9.744395,-7.485072,7.104076],[7.562981,9.601527,-4.154315,3.186719],[9.105827,7.846979,-7.165013,-8.207612],[-3.682114,8.989105,-5.596758,-2.859288],[5.510302,-2.815422,-3.550505,-2.107461],[-2.245619,9.642405,-5.382592,-7.457352],[8.951169,-3.501207,7.515107,1.287898],[-9.908519,6.140667,9.126046,-3.671769],[5.473568,-0.405764,-6.176608,5.795022],[-8.035959,8.798818,-6.277566,-9.466046],[4.748979,4.141791,1.461967,-2.692135],[-3.691908,7.095225,1.467267,-8.800835],[-2.006464,2.272687,3.423937,7.491204],[0.071892,-6.804339,-4.156869,7.119880],[9.575910,-8.382456,-1.412609,-9.134765],[9.564387,-5.308547,5.594772,2.154032],[6.475839,-0.930700,3.274441,8.030778],[-4.551374,-5.743102,-4.727146,-7.503110],[1.784020,4.021498,6.988087,-7.861860],[4.201857,-4.400566,4.326163,-0.133800],[-7.101573,9.212128,9.767075,-3.503412],[7.678279,-4.482570,-1.173323,1.059410],[-7.574121,4.227134,2.265245,-8.191111],[-1.551058,2.279425,-6.127211,7.780929],[3.031480,-8.533053,0.351360,-8.816298],[-6.047491,-4.959707,-2.459494,-4.653497],[-5.191912,-7.581680,0.242875,-3.089597],[0.694907,5.029697,-6.845925,-6.734391],[6.812481,-2.647037,5.570057,8.354657],[1.830825,7.044395,-8.116337,-9.436314],[7.015175,-2.028835,0.324257,7.418091],[-7.576069,-5.914521,3.210837,-5.800392],[-3.674277,1.891402,-6.086665,0.895873],[-7.653722,2.359254,-0.050480,-9.034761],[-9.041952,-6.418890,0.633720,8.407227],[-7.306508,-1.091794,-8.333889,-2.621987],[3.838286,9.837869,3.350215,-2.484417],[7.318365,-0.483252,5.020436,3.200909],[0.667722,-1.017154,4.499597,-0.863825],[4.897937,9.154116,-0.530933,-7.419898],[1.969237,6.609797,-4.559119,5.993221],[8.421432,3.848226,-4.144102,-1.473346],[-2.872733,-7.917362,-5.582629,3.286760],[-9.871246,-2.539425,4.401856,-0.388151],[-8.924856,2.955254,3.123171,-0.673164],[-3.608174,-6.977404,-8.675109,-6.289685],[1.766605,7.916564,7.202857,6.959522],[9.718518,-3.582076,5.458514,-4.485307],[-4.665450,-6.973870,-5.961053,-6.091661],[6.743195,9.801392,-6.616681,-9.633514],[-8.238327,5.199937,1.368661,1.955978],[-7.330676,0.646133,5.627516,2.207785],[4.489229,6.189621,-9.280618,-5.098895],[-1.395500,-5.934995,4.306255,-2.161353],[-0.508702,6.482352,6.038372,-8.066874],[6.360342,3.591739,0.538918,-4.661108],[-1.947070,-4.503329,-8.122973,-1.914821],[-5.293471,9.980804,-5.284427,-4.693893],[8.262834,-6.307581,-3.379144,9.104350],[-0.201894,-9.570837,4.332157,-6.744417],[4.477993,6.554331,3.655273,-2.351089],[-2.820297,6.610560,-0.826203,7.971130],[8.710017,-6.390888,-3.039643,5.859217],[-6.539473,9.386550,9.747891,5.712783],[-4.115896,-7.216431,4.409047,-1.628549],[-3.359924,-4.879428,6.651998,-0.360520],[1.958565,-0.916646,-4.531898,-3.345782],[-9.938202,5.888261,4.592822,-8.518437],[2.136325,9.497982,7.043830,-9.165921],[5.054184,-8.386971,-2.885891,6.755554],[7.468619,4.095896,-2.980414,-0.526212],[4.235585,-4.236427,9.204480,1.584114],[1.487277,6.772827,-1.971317,-3.871552],[-6.261405,-2.562082,4.148866,-8.971534],[6.599445,7.088204,9.515585,-7.994177],[7.851224,1.090896,1.977167,1.279387],[2.484314,-1.950645,-6.873293,9.505140],[6.587881,7.569593,6.799170,-6.688642],[9.218575,-4.136395,5.190320,-0.692755],[3.791973,9.288005,-7.418792,5.558359],[5.881539,2.022225,-2.332606,-2.175287],[-0.447384,7.407583,5.235829,-6.621949],[3.030765,0.592204,-7.964131,5.213935],[1.500789,-4.983235,8.745237,2.725043],[2.620095,-7.701404,2.895228,-2.782348],[-7.167394,-1.485546,7.202999,-3.614204],[6.765708,0.488352,2.605316,-1.091034],[-9.149875,-6.262479,-3.689348,-9.384715],[-1.252737,-9.726461,-1.966263,3.083342],[-2.718471,-3.394068,4.190678,-9.457990],[6.845289,-1.135210,-4.216106,3.982925],[1.280309,-6.753678,-4.818987,-2.761171],[9.277639,-7.725163,1.094823,-6.367403],[3.905232,8.568269,3.024851,-7.623357],[6.658891,-8.375935,6.015216,-6.542667],[2.253601,-5.151950,-6.571199,5.286340],[6.949528,0.983579,0.755151,-7.137814],[-9.384372,9.064145,4.765063,-9.425482],[-5.961445,-4.994649,4.320955,4.678561],[2.506299,-3.889785,-7.705081,0.576539],[3.141992,-9.880768,-8.049433,-5.402275],[-0.213741,6.353678,2.584675,-9.666762],[-5.668179,8.464499,-5.024867,-6.390266],[-6.760696,0.579682,-3.953231,3.505023],[0.062863,9.621863,-9.056914,-4.864439],[2.860352,1.967730,-1.167523,5.518319],[-5.016941,-0.182585,1.766881,2.584847],[1.405748,-1.264112,2.884070,9.174451],[3.550259,6.850039,-0.290030,-4.990820],[5.018311,-6.497474,5.959153,-6.051253],[-7.590310,-5.912203,4.834955,-0.952740],[-8.150050,2.081787,-2.238745,-4.385982],[4.377606,6.787008,-3.593188,3.096483],[8.739580,9.996542,0.863123,7.492922],[-3.560670,8.206657,1.503229,-3.361364],[-3.333763,3.183114,-7.197812,-1.316331],[1.368047,-5.028404,5.785396,7.521709],[4.243778,-9.968566,-8.615618,1.456939],[6.612820,2.762218,-0.618468,8.368409],[6.719407,7.398239,-6.145531,4.618174],[0.222006,4.352906,4.402990,-0.948006],[1.821690,-7.776028,-0.618067,-3.226000],[-0.039015,-3.846432,3.392871,-8.019466],[-9.576752,2.294958,0.176175,5.691833],[-6.279016,-2.720508,3.729279,-3.164392],[3.952479,4.389443,-6.705481,5.497907],[2.695121,8.909139,1.508727,6.790493],[4.047741,2.859970,2.568473,-0.224172],[0.365844,5.096174,6.153778,-5.532913],[-1.979933,-4.935381,2.284779,-9.290357],[1.323951,-5.380263,5.079545,-3.091157],[-1.932339,8.419516,-1.570708,5.475516],[-1.729379,2.340655,-0.686932,-1.171417],[0.887916,-6.230240,5.337302,9.099468],[-2.463785,2.980293,0.452156,1.818081],[1.966502,7.685247,-6.430256,-6.224383],[6.831521,-5.838745,9.359202,7.209206],[0.902409,9.821660,-3.785927,7.710866],[-5.339849,-1.419814,-2.125872,5.516020],[-7.941167,-4.339667,5.329731,-7.221539],[-5.212781,7.198828,8.254938,-4.903931],[-8.666757,5.931553,-1.168381,2.867498],[-4.167992,-1.771353,0.491843,-4.649951],[-5.413681,-2.500266,6.139822,-2.468962],[4.542903,5.858839,-9.228661,0.905643],[-5.835570,7.518021,1.484469,4.469298],[-0.440210,7.741669,-6.823415,-9.635015],[-4.413289,-3.430156,0.268600,4.168310],[-3.071770,0.773818,-0.273097,9.478863],[-1.443534,1.576840,-8.364146,6.986079],[-9.529773,-1.123817,-0.683651,0.551885],[-2.099938,4.051195,-2.813212,-2.066734],[5.192265,-2.333802,7.348522,-0.271684],[-0.144380,5.930868,0.907798,-7.060614],[0.190123,-1.287319,1.808240,-8.828971],[5.115835,7.803392,-5.686560,3.132503],[0.536757,2.446482,0.579814,-5.047835],[6.068350,-1.540177,-5.704321,-7.688026],[-6.575624,-8.359428,-7.669960,0.926677],[-2.569213,-4.683898,-1.855547,-7.431166],[6.189506,-4.344431,-4.039047,-6.212509],[8.810243,-9.844381,0.908579,7.532348],[1.847040,9.055595,8.436248,8.819062],[8.424996,-2.358776,3.644018,-1.952790],[6.288824,-1.337698,3.017332,8.075422],[1.782650,8.052362,9.171849,-9.243243],[-6.503176,-7.894151,-5.837524,9.204269],[6.402291,-6.670929,-4.348823,4.852335],[9.151575,2.592962,4.598031,8.910579],[-0.692076,3.508212,-7.844902,-8.039841],[-4.294003,-5.693683,9.351118,-2.934434],[3.931394,4.888013,0.320618,9.336508],[-9.947405,-5.349406,-0.478696,9.388676],[-8.801365,-3.727795,-7.025198,2.728017],[7.127826,-9.258078,9.264912,-9.194702],[3.167964,-4.601459,-6.784173,8.934719],[4.295486,-1.093482,-7.901912,-1.779242],[2.438216,1.256062,-4.826829,-2.766134],[-7.169742,-5.071078,3.601033,-6.699956],[-3.012887,-4.005661,6.043438,-4.890905],[5.367147,-6.435886,-6.375510,-7.167685],[2.955471,9.128700,-2.592560,4.655196],[-4.261082,-3.135645,-9.173453,-4.165226],[6.694537,-6.541443,5.433324,6.145569],[8.013380,-3.178379,1.886278,6.673242],[-8.975899,-9.908563,-8.325023,5.123215],[5.790131,0.910749,-2.658219,-9.169430],[-9.513238,-0.631746,8.941030,-6.264588],[3.006197,-1.342426,9.214840,9.943463],[4.359891,-2.638210,-4.989319,-9.829115],[2.676775,3.432266,-9.921930,2.929084],[-4.710843,-9.969959,-0.659506,4.193885],[8.925318,-4.598079,4.798019,-3.611739],[3.768549,6.698516,-8.694104,0.169860],[3.019976,7.121783,-7.523664,-7.955370],[1.197330,6.155502,1.291618,4.569446],[-3.603944,8.298571,-5.346462,-4.768711],[-5.610134,4.404359,-4.211236,-9.935195],[4.933861,4.308434,-8.677474,7.443166],[-3.557961,2.342186,7.063831,-4.351547],[-7.890799,1.992291,6.065390,-6.399941],[6.316453,-1.654494,-2.362526,6.831571],[-8.498505,-7.706238,-3.092388,-2.549828],[-4.251944,-3.752325,2.194167,2.306266],[-0.606133,-0.552645,9.304198,4.409624],[-0.013786,-7.671278,-2.530241,-0.594805],[-7.761914,-4.613879,-5.747456,8.912817],[-8.366245,-8.903741,-1.152183,-3.944930],[3.136999,-3.729199,3.921824,9.269986],[7.450122,9.572159,-5.372337,-3.603070],[-4.685604,3.738710,-9.823848,9.518115],[4.390805,-9.790212,0.198517,-2.488652],[4.416697,0.088941,1.354603,-8.871055],[-4.810057,-3.300189,0.106382,7.118060],[5.425215,0.346045,6.373979,6.291213],[-7.398322,-0.726462,-4.524257,-8.776111],[4.639935,-2.215677,2.670179,0.521177],[-8.447421,-0.141106,8.168020,7.424717],[-7.845612,-0.208097,6.897041,-7.119468],[7.247830,-5.264916,-3.335243,7.892182],[-2.743147,-3.051875,-7.515469,-4.221260],[0.858566,-1.876893,-6.764190,-3.913352],[-1.781342,2.316302,-5.953674,-9.608217],[-8.723010,3.593445,3.171677,0.704803],[-4.937467,3.523492,5.126212,-2.225802],[-0.799544,1.818202,-0.619178,-0.650516],[-6.324888,8.127181,4.787363,-3.508282],[-3.393791,-8.140153,-3.437873,4.671818],[7.638987,8.730280,-8.819052,-4.952082],[5.721498,-1.085864,6.718353,-3.872352],[-3.516245,-3.692965,8.061796,0.705549],[-6.637798,-1.829490,0.276071,0.539270],[-4.250348,-4.677345,-4.067119,-3.301311],[-3.800418,-7.367904,2.286145,-8.278858],[-3.080781,7.766883,9.286887,3.028686],[1.035831,1.926668,9.823896,0.418852],[6.067636,8.885799,-8.542802,0.460739],[-9.127850,-0.017367,2.898809,7.786965],[8.031315,5.742582,5.087014,-2.790441],[-8.299938,-5.849262,4.837011,-5.508521],[7.083227,-0.265933,3.718947,-5.310927],[1.849882,2.837470,7.625263,-0.347722],[1.112602,-8.023005,-4.162368,9.815662],[-1.564851,1.319104,-3.279364,-4.721054],[5.304212,1.655126,8.943777,-6.775548],[8.473376,6.741000,-4.289240,2.426315],[1.299263,-1.308596,7.604196,6.046759],[3.985179,0.657412,-6.166164,8.435358],[-5.670076,-8.357882,4.445317,6.307004],[-0.912839,2.544496,-8.198319,-1.954281],[-6.582514,-1.626462,8.088258,2.822248],[-7.663671,-3.561693,2.311368,-1.869147],[-7.340521,3.706652,5.965057,-7.106746],[0.486710,-2.725429,4.554859,0.074601],[5.379994,4.887867,9.586627,-9.443064],[2.289506,-6.049495,-4.964301,-3.274231],[6.620763,-4.312005,-8.977958,-3.417526],[0.540262,-7.796976,-9.958090,-0.556716],[3.231633,-5.603060,2.218835,-6.566116],[6.855242,5.317630,2.772919,-4.652844],[1.611355,7.651185,-8.516026,1.625601],[-7.222279,-0.200684,3.086452,-3.735862],[-2.382684,-0.438991,4.780289,-2.591529],[0.618607,3.474209,1.611191,-3.369208],[-7.924283,8.139620,3.124653,-6.980622],[-8.745708,-2.349589,-9.219823,-2.030667],[5.412361,-4.002302,3.356286,3.599322],[-2.040810,5.800123,9.395015,-7.841798],[0.341284,-1.601310,-1.140068,-3.605035],[1.234437,-9.839080,2.592800,-7.067163],[4.836931,-8.489610,0.574601,-8.129895],[-2.178848,1.149973,2.428493,2.066364],[9.095005,3.050675,4.137622,-6.648277],[7.296983,-0.850612,3.739891,9.339787],[9.623791,4.877920,-8.655773,-2.742310],[1.481266,-6.016667,3.403437,8.809988],[9.476858,-6.118434,-1.620165,0.968033],[8.960402,8.117665,-8.847247,-6.098514],[-8.378693,-6.321793,5.665461,2.312001],[-5.680402,3.348688,3.959550,1.595315],[8.663430,8.108685,-7.686869,0.379645],[-2.008057,2.684449,-6.502533,-9.000478],[2.196267,3.376267,2.588378,-6.867979],[-6.067803,7.742056,-4.048344,-1.405312],[-3.401855,-8.592644,-2.117932,2.362138],[-9.451645,3.369200,-1.662901,8.735493],[-4.146472,-4.060301,1.035642,0.976385],[-5.226799,2.274668,0.020201,-5.413163],[-7.006920,4.651568,0.817362,7.095573],[1.603516,-8.192354,7.520058,6.237756],[-7.107341,2.504858,-5.407161,5.936485],[-6.024379,-2.751439,-0.874036,5.727301],[3.036335,4.896593,8.032746,-1.816870],[4.650555,-5.250695,-5.114995,-8.852907],[6.372468,-0.023752,-2.611367,-5.125616],[-6.368421,6.348056,-4.734283,5.730171],[4.169219,-9.850260,-4.782643,0.683767],[7.174805,-6.062441,7.856350,-0.828927],[-0.869400,9.497683,-1.952807,8.044913],[-4.780116,6.306019,-7.021727,-0.012761],[2.701122,-5.851998,8.486900,7.866642],[-9.548172,-9.422782,-9.488002,-5.035132],[0.108478,3.335090,-7.893241,-2.782726],[3.455043,6.500507,0.803269,7.978369],[-8.766755,-7.378921,7.270837,-6.153980],[0.868452,-0.262084,8.780624,-8.815303],[-3.254233,-4.248844,0.599970,4.662242],[-1.438928,-5.956950,-2.927426,-2.449135],[2.124656,-2.292830,-6.160502,-2.363876],[9.551609,9.876721,-7.989949,6.281994],[3.454257,6.917080,-3.053056,-7.254812],[8.131296,-2.868244,-4.808129,-9.509725],[7.092094,3.836133,3.636731,1.065732],[-8.330144,8.525632,3.589622,8.322535],[-4.438263,7.880852,7.710288,0.077087],[-1.372568,-7.289340,-5.102682,-2.891870],[8.727214,4.355103,-9.154166,8.173937],[6.345282,4.130316,4.130042,4.402001],[0.870483,-8.638657,-0.276250,0.362300],[-7.039121,-3.223929,-1.783623,-0.711164],[-2.699204,-3.625035,7.741793,4.150315],[-7.438105,3.388546,4.562249,0.945799],[9.993300,8.759436,1.917516,-6.234232],[-9.160922,-8.885636,3.956698,-3.897228],[-1.546293,-7.772967,-6.531225,-5.414323],[-4.350142,-4.656960,-7.145832,-6.150382],[3.687020,-2.602774,-4.965365,-3.575696],[8.977035,8.173842,-7.504629,-5.105551],[-0.786781,-4.375848,-9.099754,9.585550],[-5.060615,-2.361938,2.922282,-8.038874],[-7.885000,1.452659,5.229564,9.369389],[-3.604290,4.903150,-3.558294,2.645454],[2.589275,7.979376,-0.015405,-9.175827],[-0.020274,-9.681327,-0.322926,-1.340235],[8.383363,4.425359,-5.465364,6.830295],[-1.152365,4.308428,-8.325004,9.635378],[-9.916711,9.371415,-1.711984,7.197074],[-1.486567,-8.718601,-3.295575,7.818771],[4.997878,-8.533739,2.491389,-7.511480],[-7.331833,-2.843513,0.487719,-2.562013],[-8.383047,-1.788778,-9.093454,3.539503],[6.545790,2.612611,-3.665078,2.271756],[9.282876,5.318824,7.475877,-5.821766],[6.581279,-9.260121,0.262705,-5.159767],[-9.677772,-9.578054,-4.933961,1.299930],[6.773018,3.738097,3.051055,7.552965],[-6.691259,1.219336,3.268510,-7.935345],[-0.195480,8.033942,7.381452,3.187798],[-6.105994,-8.089049,2.266632,8.103374],[-0.947364,2.711058,9.095354,4.071980],[7.966003,-2.048670,-2.422628,-9.577776],[1.719304,-1.850054,7.426504,0.894464],[8.153514,1.477171,1.242032,-6.597593],[9.040364,-0.245921,-0.872242,8.381025],[-6.189720,-4.548243,-2.706844,-9.900214],[-5.633612,-8.746952,-7.290311,-2.893808],[-5.214834,9.490066,-8.857275,1.529621],[3.690250,-7.128881,1.787560,5.022814],[7.471859,2.939556,-1.698054,-2.387753],[-5.009401,5.069929,-8.822607,1.368401],[6.767558,-0.467984,-6.271926,6.326176],[9.791118,7.857701,2.207385,2.166201],[9.188476,-6.821793,-3.128963,-5.972547],[-9.749596,0.897146,4.567670,8.469032],[3.894961,-7.818163,8.329294,1.381171],[-5.046950,-8.222468,-6.500557,-4.567684],[-1.877796,5.178060,5.013005,9.930035],[1.171864,-7.708481,9.302724,5.903119],[-0.127814,-8.019937,-4.046151,-4.352014],[3.425647,-0.642290,-9.006639,1.682182],[-6.087169,2.197235,-5.435551,5.804662],[-9.622307,5.418298,7.095462,-9.374107],[-2.754265,6.424980,5.428470,4.581569],[-2.465234,-0.124822,5.979170,1.622879],[-2.426161,5.753680,-4.969784,8.345211],[8.097628,-0.688412,7.430475,-1.058852],[-5.260888,-2.331952,2.917868,-4.624234],[-4.990687,4.746150,-0.676268,4.124208],[7.359664,9.972048,4.026492,-6.081173],[9.698089,4.978854,-4.376758,3.587198],[4.492870,-9.653082,8.550598,6.488281],[8.590841,5.910835,6.926401,-2.626754],[-5.866289,-9.086383,-4.333927,-4.668903],[-0.792159,0.399953,5.516100,8.469850],[-7.033619,7.047531,-5.659888,6.307670],[9.001909,3.722233,8.935961,-9.690445],[7.893389,5.865439,5.168195,-0.986406],[4.677148,-8.067665,-4.715027,-4.224631],[6.771273,-2.701520,-7.542689,9.537850],[2.759059,-8.044702,1.928859,-8.632845],[-9.329652,-5.067063,9.699610,3.168969],[-6.399562,2.665401,4.714281,-6.948255],[4.628792,-1.092753,-4.373971,-2.181689],[-5.658544,9.817007,3.102480,-4.507970],[6.004865,7.905479,7.072678,-9.692785],[5.257717,-3.459861,6.643937,1.131758],[-1.968169,-5.768465,-1.416061,-8.355828],[9.400744,-0.762570,1.880332,-7.019842],[3.119695,5.138335,-2.241421,0.146812],[5.747887,-0.195664,-4.595311,7.443759],[4.447543,3.948477,-2.468615,-3.115348],[5.554594,-2.286718,-4.475126,-5.587749],[7.071441,-3.359517,1.125512,4.619428],[-8.325855,1.089134,7.199817,7.476648],[-2.897698,-0.503038,-6.269070,-3.519620],[5.707604,-1.002491,-7.285823,-5.883053],[-6.499989,0.107162,-9.593126,-2.078611],[0.210509,2.096042,-0.325174,2.491639],[5.102408,-5.885377,8.374504,-4.933290],[8.783533,-2.543419,7.594416,2.714954],[8.565126,3.857219,1.213480,-1.199395],[9.556810,-4.661228,-5.438805,-2.993267],[3.839307,1.848278,8.772437,-6.437008],[-4.052037,-0.317947,7.162195,1.271339],[7.116461,-0.776011,-7.001749,5.644245],[-6.915464,-2.293841,0.124897,-9.728951],[6.641954,5.100022,9.221153,1.402394],[-1.988539,0.064040,-9.596695,8.602615],[8.265814,-7.758794,-4.584149,4.488243],[6.535967,-4.075418,-0.683627,-7.908552],[-4.554010,5.632646,2.016651,-8.713135],[-6.557100,7.492451,-1.028313,-4.775548],[-9.112607,-8.336320,-5.876636,8.948916],[7.424966,1.697477,-5.848109,5.467149],[6.704985,9.512048,1.581586,2.539534],[9.364907,-1.160671,3.478060,-2.082788],[-5.994542,-9.663316,-6.120945,-7.144818],[1.323845,-0.865977,1.203780,4.552205],[-1.832309,5.453935,-1.025458,5.945742],[5.547361,4.149806,1.288983,-4.159291],[-0.399939,-5.296296,-6.056573,-4.563607],[-1.904673,-1.858454,-7.644326,8.282939],[-2.819253,8.526080,0.070826,-0.819749],[-9.857625,9.093499,9.242978,5.493506],[-7.277230,4.456749,1.147894,5.667682],[-1.196943,6.239317,2.226121,3.786835],[-3.307508,-8.601261,1.527496,-2.248694],[-4.582443,2.843101,-1.900072,-1.409201],[1.785867,0.487857,2.562008,-7.773584],[-6.996921,4.093034,-8.370975,3.217481],[8.405604,-1.895493,9.139372,-2.512286],[-9.464693,7.352128,0.898596,-8.207923],[0.122630,4.531684,-9.110281,-3.588576],[6.643355,-0.207843,-7.806857,-1.535225],[0.037988,5.509867,-5.784559,-5.000076],[9.974721,0.694858,1.775934,5.862214],[4.008397,-5.526237,7.274360,9.996274],[-3.207673,-2.538319,5.215369,-3.101484],[-5.637650,2.771901,3.967531,3.908401],[-5.191996,8.464179,-5.243967,-9.473381],[9.406950,1.656481,-5.426283,-9.348431],[-6.451441,6.448421,3.221460,-6.305777],[5.464056,-4.536606,-2.851969,-4.887026],[-5.877094,-8.361354,-5.121417,6.449841],[6.648221,-3.067844,0.137069,-4.861330],[-3.554563,3.762634,8.773823,7.693352],[-0.217796,-7.008457,1.214478,8.206787],[-3.020238,3.471961,-9.375172,0.265931],[4.946957,1.584214,-6.403359,7.500716],[-2.789122,-3.101838,-7.726991,-5.115389],[-2.315980,1.109702,9.479886,3.159385],[3.851498,7.991116,4.547667,7.461934],[-8.744841,8.700810,1.244871,3.929626],[-3.030038,5.495241,7.347324,3.812372],[-7.819951,-6.616971,8.870689,-0.110407],[-9.378014,-1.789642,-0.063885,-3.316891],[6.138122,7.663665,-3.367721,-0.266893],[-6.587171,-4.630066,3.051476,9.903226],[-8.197246,-1.510963,-0.939710,-7.845589],[-2.818752,-5.021603,8.460614,4.704416],[8.415497,2.539486,-4.909338,-6.308528],[5.530972,-5.437153,-3.660027,0.864639],[6.807002,-7.726150,-0.366906,-6.692967],[9.955322,5.910861,-5.433823,0.196285],[1.083514,5.808248,-0.665697,-1.442043],[-1.324085,3.588243,6.652668,-2.821623],[-9.072048,-6.218643,7.868566,3.097109],[8.169637,1.670912,3.227710,2.387113],[3.130393,-7.247643,-2.247243,-4.236152],[-0.488964,0.653881,-1.784970,-5.906496],[-4.329719,4.836732,-4.273636,9.518925],[3.438785,4.744275,5.894854,4.843337],[7.945830,6.181504,-8.203427,0.726273],[4.929878,-6.749409,-5.176029,-0.726531],[4.288710,-5.612824,-1.991693,-8.264109],[5.901756,-0.037119,-3.936860,8.978426],[-6.883380,-1.501544,-4.866374,4.248522],[-5.089611,6.203813,-0.680826,-6.157244],[7.021735,8.343304,-3.448225,4.103439],[3.865825,-2.707516,8.297870,-2.102538],[-6.574015,8.473776,-6.211338,-1.069112],[-2.559078,6.695188,8.897389,2.652878],[-8.932185,-3.967429,-6.530245,-2.459742],[-7.863694,0.716309,2.964186,2.895251],[-1.787999,-4.920483,1.684066,-5.186437],[8.034355,-1.618075,5.635481,8.404191],[4.752670,-8.545107,-4.393575,5.806404],[8.881228,-0.857688,-5.370011,4.748901],[-7.659243,1.243600,-9.402732,-4.772063],[3.497247,5.299821,-9.573951,1.891933],[-1.250178,6.040109,-5.157330,7.113877],[6.407800,-2.318069,9.140102,7.935690],[-6.748619,9.309003,-5.038102,-7.338829],[1.836109,-6.396498,-9.199424,5.275916],[6.282476,5.347112,6.818405,8.837643],[3.455622,1.045977,4.169061,-3.147933],[1.665338,0.715699,8.249810,-7.930747],[7.516022,-4.948422,-8.895132,-5.945067],[-3.779768,0.214498,9.404547,7.156750],[0.088146,2.703087,3.498185,-5.233958],[-0.002486,-3.715441,9.179877,-2.430258],[1.817395,-2.621052,-0.945151,7.803372],[7.847171,-1.488825,5.249484,3.955164],[-4.890268,-9.099201,-9.246645,9.730842],[-3.631578,5.956987,-5.286166,-0.099431],[-8.390292,4.110474,2.998532,-7.666285],[7.846617,9.929665,-7.438759,7.146484],[-1.295571,-8.894032,-1.841746,3.414632],[3.351355,-8.603994,-1.430982,6.831135],[-7.629090,3.867673,9.695451,-5.147706],[-9.378754,6.504846,-5.690157,-5.181186]], dtype = "float64")#candidate|1027|(840, 4)|const|float64
call_1025 = relay.TupleGetItem(func_697_call(relay.reshape(const_1026.astype('float64'), []), relay.reshape(const_1027.astype('float64'), [16, 15, 14]), ), 2)
call_1028 = relay.TupleGetItem(func_701_call(relay.reshape(const_1026.astype('float64'), []), relay.reshape(const_1027.astype('float64'), [16, 15, 14]), ), 2)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_1035 = relay.TupleGetItem(func_312_call(), 0)
call_1036 = relay.TupleGetItem(func_313_call(), 0)
func_482_call = mod.get_global_var('func_482')
func_484_call = mutated_mod.get_global_var('func_484')
call_1041 = relay.TupleGetItem(func_482_call(), 3)
call_1042 = relay.TupleGetItem(func_484_call(), 3)
func_513_call = mod.get_global_var('func_513')
func_514_call = mutated_mod.get_global_var('func_514')
call_1052 = relay.TupleGetItem(func_513_call(), 0)
call_1053 = relay.TupleGetItem(func_514_call(), 0)
output = relay.Tuple([call_1003,call_1012,var_1013,var_1014,call_1016,call_1019,call_1025,const_1026,const_1027,call_1035,call_1041,call_1052,])
output2 = relay.Tuple([call_1004,call_1015,var_1013,var_1014,call_1017,call_1020,call_1028,const_1026,const_1027,call_1036,call_1042,call_1053,])
func_1058 = relay.Function([var_1013,var_1014,], output)
mod['func_1058'] = func_1058
mod = relay.transform.InferType()(mod)
mutated_mod['func_1058'] = func_1058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1058_call = mutated_mod.get_global_var('func_1058')
var_1060 = relay.var("var_1060", dtype = "float64", shape = (1568,))#candidate|1060|(1568,)|var|float64
var_1061 = relay.var("var_1061", dtype = "float64", shape = (16, 2))#candidate|1061|(16, 2)|var|float64
call_1059 = func_1058_call(var_1060,var_1061,)
output = call_1059
func_1062 = relay.Function([var_1060,var_1061,], output)
mutated_mod['func_1062'] = func_1062
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1140 = relay.const([[[-4.688974,-9.604103,0.130780,6.060206,8.870886,7.916013,8.130701,9.104145,-1.379254,7.683113],[-6.170151,-3.941620,1.836734,-9.288821,0.545740,-4.177417,-0.050777,6.690682,-1.232870,0.148977],[-6.587865,5.971386,0.025672,2.291339,-5.681009,6.705849,-9.498369,-6.088809,-3.405849,-3.671904],[-3.403088,-3.760348,5.719123,-1.381540,-4.378032,6.884675,-8.391179,-7.440113,5.425957,-0.948935],[5.374967,-6.871660,7.897770,8.707277,-4.702230,-7.757758,-0.506230,6.993340,-4.397510,-8.113387],[6.786077,4.289046,-4.845236,-9.755472,1.595838,2.611312,-9.685155,4.953841,2.342694,3.583735],[-6.860942,-3.793401,-1.054288,-8.052183,-1.683821,9.290179,-8.270930,7.388375,7.068260,6.007219],[-6.048867,9.879981,-8.490933,5.265088,0.250156,8.985264,-1.310091,-5.969896,4.746993,0.109581],[1.992043,-6.348415,9.359304,5.722332,6.415655,2.227966,3.868482,-2.659217,2.195617,7.843700],[-9.797875,-5.870651,8.487539,-5.885638,8.350235,-2.427994,-4.736983,8.808531,-7.859259,-6.818057]]], dtype = "float32")#candidate|1140|(1, 10, 10)|const|float32
uop_1141 = relay.sinh(const_1140.astype('float32')) # shape=(1, 10, 10)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_1143 = func_720_call()
call_1144 = func_720_call()
uop_1145 = relay.log10(uop_1141.astype('float32')) # shape=(1, 10, 10)
uop_1147 = relay.cosh(uop_1145.astype('float64')) # shape=(1, 10, 10)
bop_1159 = relay.floor_divide(uop_1145.astype('float32'), relay.reshape(uop_1147.astype('float32'), relay.shape_of(uop_1145))) # shape=(1, 10, 10)
output = relay.Tuple([call_1143,bop_1159,])
output2 = relay.Tuple([call_1144,bop_1159,])
func_1170 = relay.Function([], output)
mod['func_1170'] = func_1170
mod = relay.transform.InferType()(mod)
mutated_mod['func_1170'] = func_1170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mutated_mod.get_global_var('func_1170')
call_1171 = func_1170_call()
output = call_1171
func_1172 = relay.Function([], output)
mutated_mod['func_1172'] = func_1172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_482_call = mod.get_global_var('func_482')
func_484_call = mutated_mod.get_global_var('func_484')
call_1200 = relay.TupleGetItem(func_482_call(), 1)
call_1201 = relay.TupleGetItem(func_484_call(), 1)
output = relay.Tuple([call_1200,])
output2 = relay.Tuple([call_1201,])
func_1222 = relay.Function([], output)
mod['func_1222'] = func_1222
mod = relay.transform.InferType()(mod)
output = func_1222()
func_1223 = relay.Function([], output)
mutated_mod['func_1223'] = func_1223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_482_call = mod.get_global_var('func_482')
func_484_call = mutated_mod.get_global_var('func_484')
call_1367 = relay.TupleGetItem(func_482_call(), 0)
call_1368 = relay.TupleGetItem(func_484_call(), 0)
func_284_call = mod.get_global_var('func_284')
func_286_call = mutated_mod.get_global_var('func_286')
call_1388 = relay.TupleGetItem(func_284_call(), 3)
call_1389 = relay.TupleGetItem(func_286_call(), 3)
output = relay.Tuple([call_1367,call_1388,])
output2 = relay.Tuple([call_1368,call_1389,])
func_1401 = relay.Function([], output)
mod['func_1401'] = func_1401
mod = relay.transform.InferType()(mod)
mutated_mod['func_1401'] = func_1401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1401_call = mutated_mod.get_global_var('func_1401')
call_1402 = func_1401_call()
output = call_1402
func_1403 = relay.Function([], output)
mutated_mod['func_1403'] = func_1403
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1404 = relay.var("var_1404", dtype = "int32", shape = ())#candidate|1404|()|var|int32
var_1405 = relay.var("var_1405", dtype = "int32", shape = (8, 1, 16))#candidate|1405|(8, 1, 16)|var|int32
bop_1406 = relay.equal(var_1404.astype('bool'), var_1405.astype('bool')) # shape=(8, 1, 16)
func_482_call = mod.get_global_var('func_482')
func_484_call = mutated_mod.get_global_var('func_484')
call_1415 = relay.TupleGetItem(func_482_call(), 3)
call_1416 = relay.TupleGetItem(func_484_call(), 3)
func_256_call = mod.get_global_var('func_256')
func_260_call = mutated_mod.get_global_var('func_260')
var_1423 = relay.var("var_1423", dtype = "float64", shape = (1568,))#candidate|1423|(1568,)|var|float64
var_1424 = relay.var("var_1424", dtype = "float64", shape = (32,))#candidate|1424|(32,)|var|float64
call_1422 = relay.TupleGetItem(func_256_call(relay.reshape(var_1423.astype('float64'), [14, 7, 16]), relay.reshape(var_1424.astype('float64'), [32,]), ), 2)
call_1425 = relay.TupleGetItem(func_260_call(relay.reshape(var_1423.astype('float64'), [14, 7, 16]), relay.reshape(var_1424.astype('float64'), [32,]), ), 2)
output = relay.Tuple([bop_1406,call_1415,call_1422,var_1423,var_1424,])
output2 = relay.Tuple([bop_1406,call_1416,call_1425,var_1423,var_1424,])
func_1442 = relay.Function([var_1404,var_1405,var_1423,var_1424,], output)
mod['func_1442'] = func_1442
mod = relay.transform.InferType()(mod)
var_1443 = relay.var("var_1443", dtype = "int32", shape = ())#candidate|1443|()|var|int32
var_1444 = relay.var("var_1444", dtype = "int32", shape = (8, 1, 16))#candidate|1444|(8, 1, 16)|var|int32
var_1445 = relay.var("var_1445", dtype = "float64", shape = (1568,))#candidate|1445|(1568,)|var|float64
var_1446 = relay.var("var_1446", dtype = "float64", shape = (32,))#candidate|1446|(32,)|var|float64
output = func_1442(var_1443,var_1444,var_1445,var_1446,)
func_1447 = relay.Function([var_1443,var_1444,var_1445,var_1446,], output)
mutated_mod['func_1447'] = func_1447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1222_call = mod.get_global_var('func_1222')
func_1223_call = mutated_mod.get_global_var('func_1223')
call_1462 = relay.TupleGetItem(func_1222_call(), 0)
call_1463 = relay.TupleGetItem(func_1223_call(), 0)
output = relay.Tuple([call_1462,])
output2 = relay.Tuple([call_1463,])
func_1466 = relay.Function([], output)
mod['func_1466'] = func_1466
mod = relay.transform.InferType()(mod)
output = func_1466()
func_1467 = relay.Function([], output)
mutated_mod['func_1467'] = func_1467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_284_call = mod.get_global_var('func_284')
func_286_call = mutated_mod.get_global_var('func_286')
call_1471 = relay.TupleGetItem(func_284_call(), 1)
call_1472 = relay.TupleGetItem(func_286_call(), 1)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_1477 = relay.TupleGetItem(func_1401_call(), 0)
call_1478 = relay.TupleGetItem(func_1403_call(), 0)
output = relay.Tuple([call_1471,call_1477,])
output2 = relay.Tuple([call_1472,call_1478,])
func_1483 = relay.Function([], output)
mod['func_1483'] = func_1483
mod = relay.transform.InferType()(mod)
mutated_mod['func_1483'] = func_1483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mutated_mod.get_global_var('func_1483')
call_1484 = func_1483_call()
output = call_1484
func_1485 = relay.Function([], output)
mutated_mod['func_1485'] = func_1485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1222_call = mod.get_global_var('func_1222')
func_1223_call = mutated_mod.get_global_var('func_1223')
call_1489 = relay.TupleGetItem(func_1222_call(), 0)
call_1490 = relay.TupleGetItem(func_1223_call(), 0)
output = call_1489
output2 = call_1490
func_1503 = relay.Function([], output)
mod['func_1503'] = func_1503
mod = relay.transform.InferType()(mod)
output = func_1503()
func_1504 = relay.Function([], output)
mutated_mod['func_1504'] = func_1504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_1537 = relay.TupleGetItem(func_1401_call(), 0)
call_1538 = relay.TupleGetItem(func_1403_call(), 0)
output = relay.Tuple([call_1537,])
output2 = relay.Tuple([call_1538,])
func_1545 = relay.Function([], output)
mod['func_1545'] = func_1545
mod = relay.transform.InferType()(mod)
output = func_1545()
func_1546 = relay.Function([], output)
mutated_mod['func_1546'] = func_1546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_284_call = mod.get_global_var('func_284')
func_286_call = mutated_mod.get_global_var('func_286')
call_1606 = relay.TupleGetItem(func_284_call(), 1)
call_1607 = relay.TupleGetItem(func_286_call(), 1)
output = relay.Tuple([call_1606,])
output2 = relay.Tuple([call_1607,])
func_1611 = relay.Function([], output)
mod['func_1611'] = func_1611
mod = relay.transform.InferType()(mod)
mutated_mod['func_1611'] = func_1611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mutated_mod.get_global_var('func_1611')
call_1612 = func_1611_call()
output = call_1612
func_1613 = relay.Function([], output)
mutated_mod['func_1613'] = func_1613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1655 = relay.var("var_1655", dtype = "float32", shape = (9, 15, 2))#candidate|1655|(9, 15, 2)|var|float32
uop_1656 = relay.atan(var_1655.astype('float32')) # shape=(9, 15, 2)
output = uop_1656
output2 = uop_1656
func_1663 = relay.Function([var_1655,], output)
mod['func_1663'] = func_1663
mod = relay.transform.InferType()(mod)
mutated_mod['func_1663'] = func_1663
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1664 = relay.var("var_1664", dtype = "float32", shape = (9, 15, 2))#candidate|1664|(9, 15, 2)|var|float32
func_1663_call = mutated_mod.get_global_var('func_1663')
call_1665 = func_1663_call(var_1664)
output = call_1665
func_1666 = relay.Function([var_1664], output)
mutated_mod['func_1666'] = func_1666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1466_call = mod.get_global_var('func_1466')
func_1467_call = mutated_mod.get_global_var('func_1467')
call_1675 = relay.TupleGetItem(func_1466_call(), 0)
call_1676 = relay.TupleGetItem(func_1467_call(), 0)
func_556_call = mod.get_global_var('func_556')
func_559_call = mutated_mod.get_global_var('func_559')
var_1678 = relay.var("var_1678", dtype = "float64", shape = (1568,))#candidate|1678|(1568,)|var|float64
call_1677 = relay.TupleGetItem(func_556_call(relay.reshape(var_1678.astype('float64'), [1568,])), 1)
call_1679 = relay.TupleGetItem(func_559_call(relay.reshape(var_1678.astype('float64'), [1568,])), 1)
output = relay.Tuple([call_1675,call_1677,var_1678,])
output2 = relay.Tuple([call_1676,call_1679,var_1678,])
func_1680 = relay.Function([var_1678,], output)
mod['func_1680'] = func_1680
mod = relay.transform.InferType()(mod)
mutated_mod['func_1680'] = func_1680
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1681 = relay.var("var_1681", dtype = "float64", shape = (1568,))#candidate|1681|(1568,)|var|float64
func_1680_call = mutated_mod.get_global_var('func_1680')
call_1682 = func_1680_call(var_1681)
output = call_1682
func_1683 = relay.Function([var_1681], output)
mutated_mod['func_1683'] = func_1683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_1756 = relay.TupleGetItem(func_1611_call(), 0)
call_1757 = relay.TupleGetItem(func_1613_call(), 0)
uop_1778 = relay.asinh(call_1756.astype('float64')) # shape=(1, 2, 16)
uop_1780 = relay.asinh(call_1757.astype('float64')) # shape=(1, 2, 16)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_1785 = relay.TupleGetItem(func_312_call(), 0)
call_1786 = relay.TupleGetItem(func_313_call(), 0)
output = relay.Tuple([uop_1778,call_1785,])
output2 = relay.Tuple([uop_1780,call_1786,])
func_1792 = relay.Function([], output)
mod['func_1792'] = func_1792
mod = relay.transform.InferType()(mod)
mutated_mod['func_1792'] = func_1792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1792_call = mutated_mod.get_global_var('func_1792')
call_1793 = func_1792_call()
output = call_1793
func_1794 = relay.Function([], output)
mutated_mod['func_1794'] = func_1794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_1795 = func_575_call()
call_1796 = func_575_call()
output = call_1795
output2 = call_1796
func_1815 = relay.Function([], output)
mod['func_1815'] = func_1815
mod = relay.transform.InferType()(mod)
output = func_1815()
func_1816 = relay.Function([], output)
mutated_mod['func_1816'] = func_1816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_1817 = func_720_call()
call_1818 = func_720_call()
output = relay.Tuple([call_1817,])
output2 = relay.Tuple([call_1818,])
func_1819 = relay.Function([], output)
mod['func_1819'] = func_1819
mod = relay.transform.InferType()(mod)
output = func_1819()
func_1820 = relay.Function([], output)
mutated_mod['func_1820'] = func_1820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_513_call = mod.get_global_var('func_513')
func_514_call = mutated_mod.get_global_var('func_514')
call_1835 = relay.TupleGetItem(func_513_call(), 0)
call_1836 = relay.TupleGetItem(func_514_call(), 0)
output = call_1835
output2 = call_1836
func_1843 = relay.Function([], output)
mod['func_1843'] = func_1843
mod = relay.transform.InferType()(mod)
output = func_1843()
func_1844 = relay.Function([], output)
mutated_mod['func_1844'] = func_1844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_1876 = relay.TupleGetItem(func_1170_call(), 1)
call_1877 = relay.TupleGetItem(func_1172_call(), 1)
func_1545_call = mod.get_global_var('func_1545')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_1878 = relay.TupleGetItem(func_1545_call(), 0)
call_1879 = relay.TupleGetItem(func_1546_call(), 0)
output = relay.Tuple([call_1876,call_1878,])
output2 = relay.Tuple([call_1877,call_1879,])
func_1895 = relay.Function([], output)
mod['func_1895'] = func_1895
mod = relay.transform.InferType()(mod)
output = func_1895()
func_1896 = relay.Function([], output)
mutated_mod['func_1896'] = func_1896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1815_call = mod.get_global_var('func_1815')
func_1816_call = mutated_mod.get_global_var('func_1816')
call_1909 = func_1815_call()
call_1910 = func_1815_call()
output = relay.Tuple([call_1909,])
output2 = relay.Tuple([call_1910,])
func_1915 = relay.Function([], output)
mod['func_1915'] = func_1915
mod = relay.transform.InferType()(mod)
output = func_1915()
func_1916 = relay.Function([], output)
mutated_mod['func_1916'] = func_1916
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1917 = relay.var("var_1917", dtype = "float32", shape = (9, 15, 14))#candidate|1917|(9, 15, 14)|var|float32
uop_1918 = relay.atanh(var_1917.astype('float32')) # shape=(9, 15, 14)
uop_1935 = relay.asin(var_1917.astype('float32')) # shape=(9, 15, 14)
output = relay.Tuple([uop_1918,uop_1935,])
output2 = relay.Tuple([uop_1918,uop_1935,])
func_1939 = relay.Function([var_1917,], output)
mod['func_1939'] = func_1939
mod = relay.transform.InferType()(mod)
mutated_mod['func_1939'] = func_1939
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1940 = relay.var("var_1940", dtype = "float32", shape = (9, 15, 14))#candidate|1940|(9, 15, 14)|var|float32
func_1939_call = mutated_mod.get_global_var('func_1939')
call_1941 = func_1939_call(var_1940)
output = call_1941
func_1942 = relay.Function([var_1940], output)
mutated_mod['func_1942'] = func_1942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_1949 = func_720_call()
call_1950 = func_720_call()
var_1961 = relay.var("var_1961", dtype = "int8", shape = (4, 4, 16))#candidate|1961|(4, 4, 16)|var|int8
bop_1962 = relay.less_equal(call_1949.astype('bool'), relay.reshape(var_1961.astype('bool'), relay.shape_of(call_1949))) # shape=(4, 4, 16)
bop_1965 = relay.less_equal(call_1950.astype('bool'), relay.reshape(var_1961.astype('bool'), relay.shape_of(call_1950))) # shape=(4, 4, 16)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_1981 = relay.TupleGetItem(func_1401_call(), 0)
call_1982 = relay.TupleGetItem(func_1403_call(), 0)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_1998 = relay.TupleGetItem(func_312_call(), 0)
call_1999 = relay.TupleGetItem(func_313_call(), 0)
output = relay.Tuple([bop_1962,call_1981,call_1998,])
output2 = relay.Tuple([bop_1965,call_1982,call_1999,])
func_2000 = relay.Function([var_1961,], output)
mod['func_2000'] = func_2000
mod = relay.transform.InferType()(mod)
var_2001 = relay.var("var_2001", dtype = "int8", shape = (4, 4, 16))#candidate|2001|(4, 4, 16)|var|int8
output = func_2000(var_2001)
func_2002 = relay.Function([var_2001], output)
mutated_mod['func_2002'] = func_2002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_2011 = relay.TupleGetItem(func_1611_call(), 0)
call_2012 = relay.TupleGetItem(func_1613_call(), 0)
func_1663_call = mod.get_global_var('func_1663')
func_1666_call = mutated_mod.get_global_var('func_1666')
const_2018 = relay.const([9.628555,-6.362762,-4.413445,-3.321054,8.310137,-6.942133,-7.357427,7.765440,-6.243689,0.412354,5.321941,8.676289,-6.250143,-7.238738,-2.476383,-9.265370,-1.891423,-5.376624,-6.726118,-2.313502,-6.384459,7.036016,6.401606,-2.855178,-1.780149,-6.797737,-2.701899,8.233889,-6.586930,-8.653995,5.867067,-9.795507,8.416297,-7.623925,3.732434,9.083967,6.380371,-8.194716,9.727745,-4.901649,-8.595686,2.601544,-3.302063,-7.065242,9.992811,-5.032200,8.199144,-0.054008,5.599303,0.066765,0.560739,1.425980,4.797830,4.991347,-3.337805,-2.511617,8.343508,5.459689,-7.049070,-2.147399,-1.720192,6.651091,-1.077528,-9.913425,-2.701825,-2.250834,2.233701,3.055983,-2.722392,5.768833,-6.652361,6.671584,-9.766277,-9.211613,-7.004649,-4.892707,5.300562,8.678965,8.419298,8.247614,6.956520,6.258869,8.879388,3.742879,2.243864,0.746197,8.237526,2.497599,5.287370,-8.216364,5.327189,2.358468,-5.952148,-0.023361,-2.398469,-7.919313,9.464349,-3.984856,-8.789593,-8.092190,6.263182,2.249818,5.684872,-3.325505,-3.069231,-1.562654,0.009267,-4.769398,-4.939247,0.194745,3.252594,-6.657039,7.811869,7.549405,0.258587,9.030057,3.732645,5.593742,-1.469986,-3.424129,-6.709436,-2.316593,-6.832046,-8.342492,9.024795,4.166575,3.780312,1.072032,7.601893,-5.847985,7.655714,2.593408,-4.405620,6.184674,-0.017292,-4.475187,-0.899778,-2.681963,6.001604,-6.484993,-8.576941,5.538925,2.694812,-8.613230,-0.480908,5.676835,-3.039719,-3.905171,4.094928,3.408221,3.385446,9.696348,-3.583635,-5.928917,-6.194688,-6.400900,1.797223,-0.887162,1.354252,6.367585,9.922111,6.587167,6.539032,-3.016862,3.685408,-0.022508,6.899625,-5.158557,4.436924,-7.369904,0.068006,-3.524765,-8.030937,-4.339367,8.348393,1.382234,-6.188765,-9.678226,9.173653,4.217847,1.681549,6.949891,0.117338,-9.809603,6.008160,-9.367142,-4.306412,7.776184,6.199334,-1.907731,0.138671,4.538374,-4.508458,3.413240,-8.956417,-4.154370,-0.615776,2.493177,1.562720,-1.078435,-9.137439,-6.281141,0.994845,6.045355,7.575624,9.638298,-6.053185,-3.491153,-9.106440,-7.144639,-8.974787,-5.771935,-7.582318,-4.424377,-9.024287,-4.128520,7.259903,9.194279,-0.451948,7.220359,-9.071043,-9.410547,0.428098,1.812381,-8.452589,9.925493,-5.855951,5.666483,9.379054,-6.945962,-0.431606,-0.713297,7.244699,-4.071016,-3.554358,1.382491,-2.851919,0.685236,3.691247,-9.187403,-7.115393,-9.118788,5.889272,-8.803362,-5.665449,-7.077279,9.458963,-2.465869,-6.462067,1.609962,7.788494,7.062832,-0.386692,7.126900,3.426717,-9.667237,0.158353,-1.188700,-8.997990,3.752385,-8.998120,-4.197766,-2.951230,-7.801816,4.297585,-8.798715,1.818412,0.380115,-8.938312,1.304986], dtype = "float32")#candidate|2018|(270,)|const|float32
call_2017 = func_1663_call(relay.reshape(const_2018.astype('float32'), [9, 15, 2]))
call_2019 = func_1663_call(relay.reshape(const_2018.astype('float32'), [9, 15, 2]))
func_1058_call = mod.get_global_var('func_1058')
func_1062_call = mutated_mod.get_global_var('func_1062')
const_2022 = relay.const([6.190977,6.965708,5.989988,-5.548526,9.372544,3.877983,-7.432209,-2.654770,-3.492748,-5.453017,6.704716,-5.835422,3.926488,-4.118602,-0.704582,-7.130364,9.942934,8.532801,-6.065820,3.212396,-3.476812,-4.762771,-2.403515,6.085575,-1.884539,1.057740,7.709546,-5.508403,-3.848333,-6.405832,-9.489420,0.554754,-9.105821,-2.665885,-9.737204,-4.970634,3.095332,3.701510,5.845742,-5.446052,-7.605845,-7.327949,1.137518,-7.615747,9.972382,-4.729508,-8.704419,7.984145,-9.621677,8.182348,0.950114,-5.011160,2.127851,-8.822713,-5.970536,-8.930547,4.150960,6.536290,6.634059,-4.324557,-1.339231,2.720184,-4.858206,1.098245,-6.028582,6.695068,5.352037,-9.348704,-1.625913,8.207450,5.371764,1.623538,-9.092204,-1.502083,8.672982,5.115799,2.754478,-1.265102,7.314151,4.145163,-2.407518,-1.933707,-6.831109,-7.722290,7.399068,9.829096,3.464086,7.355943,2.771506,-7.643774,2.482181,-2.513514,-7.683749,-6.135129,5.197813,3.254065,6.424584,4.941581,0.952585,-1.608485,5.793912,5.633897,-9.123875,1.949670,-0.755782,-4.997513,6.848481,7.647666,6.825189,1.200038,8.992740,2.858768,-0.154007,-7.281153,-1.884339,2.853367,-1.576475,2.011685,0.922943,3.001083,-6.073794,7.755431,-4.088453,9.862077,9.750234,-3.237385,9.843470,4.010132,-1.390819,1.172110,-1.984358,2.841489,-4.762574,5.052955,2.390009,6.357569,0.554203,4.880637,1.972315,7.721521,2.200593,8.582957,4.397051,3.283107,-5.283552,9.242398,1.332544,-8.698945,2.300734,7.069594,-9.376744,-4.530931,-7.231987,1.777163,-1.432023,-1.807430,3.374716,-8.826481,-5.740113,-1.914402,4.521552,2.960296,-5.325414,-8.020647,3.342177,-9.708572,-2.052090,3.203283,-0.785704,4.820819,-5.363124,4.776347,4.463223,-8.234307,5.076090,8.105072,-1.689294,4.056217,-4.245550,-5.118172,8.697764,3.113736,5.203323,-6.733947,5.053470,-4.940732,9.768948,5.880806,-6.186819,-7.855683,1.230132,-2.078597,-4.010795,-9.135979,2.120766,5.621455,-7.972037,-0.331919,3.458238,0.760285,-5.037605,-2.576818,7.374431,0.053639,-1.165111,0.044663,1.956845,5.421502,6.649772,-4.532544,1.459373,-2.267729,-4.964172,3.749417,7.808014,-3.951444,4.819677,-8.180564,8.294204,-5.985234,0.420494,4.506530,2.329369,8.009355,-9.231432,9.253825,5.304910,0.038495,-0.006747,1.150684,-7.329607,-4.445223,4.000254,-8.562334,-4.757432,-8.020896,1.657598,-0.658812,-3.618631,8.109626,0.667522,-5.911962,-1.335070,-2.689428,6.962484,8.367687,5.724801,5.224858,-4.317692,4.612861,-8.053514,-2.408413,7.213147,-3.420831,-7.095021,7.861689,-7.160908,-2.802752,6.627411,6.178403,2.056950,-0.672186,-3.460446,6.521188,-6.113133,8.619812,-0.837861,-3.240268,-5.399275,7.858982,-1.037271,-2.748310,7.184240,-7.633126,2.731928,5.044524,-8.410777,-0.374343,6.459054,2.462377,-3.018520,-6.271156,-5.503084,5.763545,8.161487,-0.366412,6.431716,-6.712287,7.195744,1.371429,-6.969330,5.265933,5.015235,-5.335144,0.030442,-1.132596,-0.347914,-6.221028,9.991515,-1.172773,3.737198,-8.270161,1.560011,4.110084,7.280033,-3.268879,2.071117,-5.538486,4.953912,5.948346,-3.096374,-4.074394,-2.674305,-3.494826,-0.705882,-8.318143,9.924662,-0.378648,3.866012,6.385518,3.125058,-9.687820,-0.512667,1.538608,6.701831,-0.636396,-7.172913,8.528287,-9.050516,-9.054553,-3.886393,-0.909088,9.326529,-6.324132,-7.739808,-7.695393,6.490827,-9.921167,6.721457,0.613937,-1.672932,1.944494,8.670369,9.326376,-9.784729,-9.634562,-6.132020,-4.084167,-1.443232,-7.517950,-3.005952,-2.579011,9.721053,6.458516,-0.868656,-4.847393,1.431934,5.540073,-6.625118,-7.097053,-1.922378,8.206017,5.505191,-7.244711,-8.536034,-5.079839,8.416844,7.481019,6.084274,-5.387619,3.923906,-5.985727,-5.474657,8.163329,-1.258034,9.309898,6.399069,8.748471,-2.820246,-3.421999,-2.589003,7.980943,4.838118,-0.039614,-2.237100,-8.947692,0.818167,-5.029261,-4.064499,-0.610769,1.473330,6.370827,-1.893857,3.669708,-1.348173,-1.412030,-1.554527,2.304738,-5.948636,-0.303887,-6.448939,-6.524088,4.454875,6.165423,1.255074,-1.543284,5.246990,3.392820,-0.065922,-9.708122,-9.521014,3.059075,-3.313122,-1.102302,-5.027576,3.986214,7.098759,8.894504,-6.982330,-6.585094,-7.147719,-7.774176,-3.587724,-1.343905,-0.223894,8.985827,7.684001,6.544001,4.974145,-8.500307,-5.237763,-0.221696,2.994922,-6.685046,-4.180657,3.048544,2.096934,-7.958933,1.998369,-6.454067,7.790237,-0.394335,-2.487189,5.357307,1.580388,-7.540519,3.830182,0.844952,-1.467666,9.884646,-3.275215,2.668063,-6.871763,4.168587,-3.193367,-3.389928,-5.679896,-9.229133,-7.267849,-2.247924,5.498748,-4.956354,-4.143012,-9.339787,8.161783,3.512945,-2.134521,-2.622626,6.750917,7.087241,3.168138,3.733201,-8.674762,2.287208,8.524039,8.622073,-5.147656,-0.762145,7.771592,0.665768,-1.042108,7.137258,4.418590,7.353781,7.190195,3.762704,-3.948310,-0.634043,-0.986386,-1.485359,-5.810993,3.393987,6.364485,9.387028,-3.129602,6.469550,5.865270,4.821816,-9.822922,1.681270,0.297861,8.138806,-2.919280,4.528512,4.130089,-4.779210,6.330411,-7.397918,9.781240,6.739936,-1.941726,-7.500749,0.667899,-0.133322,7.312999,-9.634364,-0.944096,-5.849280,1.306550,-5.684265,8.322814,-8.949285,-5.696335,1.516511,-6.768377,9.658420,-6.899989,6.159855,7.564288,0.279178,6.563774,-9.198342,3.401772,-1.786552,-3.979791,0.296542,-1.612427,-5.899157,-6.049457,-0.951904,-4.858296,9.758366,-3.524600,3.692553,2.707709,-4.443412,-2.360348,-1.334459,0.438287,-8.594031,3.278019,-1.176293,-5.155056,-9.780513,-7.726047,4.320212,-2.816852,0.311016,9.358924,5.664908,-8.149080,-2.595182,-5.059352,-0.363265,6.280633,2.417426,7.532985,-2.428079,-4.912298,-0.787337,-8.085869,9.870780,1.502782,4.460526,1.330746,7.520828,-1.697179,-5.107201,-9.108972,-3.902091,-0.982665,7.800478,8.981555,4.012568,-7.644720,0.734853,8.715767,-3.960005,5.598761,-6.319061,-3.908515,-1.752549,6.250550,7.331236,-9.858521,8.640279,7.001952,-7.509605,9.732234,-9.278543,4.538242,-2.509891,-3.195759,4.128911,-7.354489,7.800629,6.038739,7.117443,-1.928062,3.838966,-7.839308,0.865971,9.595555,0.487660,3.582299,-4.133928,8.329797,-8.010925,6.918509,3.323711,1.534144,-5.857575,0.210850,8.990303,-4.917348,-9.808278,7.113774,-8.877697,5.698537,2.414643,8.324950,5.626046,-4.590712,9.966908,-8.566903,7.090481,4.703538,-1.783222,1.912719,-3.777601,-5.902762,2.392939,2.912096,-2.070936,7.917323,2.609578,-8.509682,1.483624,-6.725764,-2.447711,9.472467,-2.303801,-3.504459,0.845064,-8.532817,0.037229,-9.135029,1.340405,0.192244,-6.953002,7.951284,3.873163,0.464583,9.012448,0.194145,-4.330147,7.265361,6.362201,5.446514,-7.978354,6.395788,9.613005,-8.054609,4.508590,-0.903889,-3.294019,7.725062,3.674671,-0.802047,5.043681,4.773062,-9.167682,-1.907749,-5.413469,1.960817,-8.454915,-4.480108,-0.012419,-4.574926,-2.312700,-4.134270,-1.871953,6.718775,-5.927926,-6.449053,7.276998,1.786764,9.413234,-8.372103,7.870830,-2.386101,-1.078425,3.690878,1.911944,-8.551528,4.502446,-0.985631,-0.469433,8.854609,7.556075,-1.333678,6.622464,-6.618146,-0.904817,-4.531301,-2.810593,0.522474,-6.607297,-6.951712,-1.415501,0.463410,8.848916,2.879399,1.738555,-9.828678,6.981268,-8.516056,-7.179042,3.424807,4.345354,-1.283558,-7.276777,-8.001866,3.478948,-5.202936,0.632275,5.706670,8.029485,-0.880555,9.746473,2.316067,-2.985766,-2.506987,-7.412366,7.158545,9.110796,-4.209905,1.808385,-2.959670,4.934195,-9.575985,3.583388,9.856932,-2.374162,1.789493,-1.664756,-2.407509,-2.017573,2.347204,-4.626518,-7.677095,-7.160151,4.240213,4.762127,-2.311601,-8.628109,2.890374,-2.816923,-4.828836,6.333120,7.765879,-2.125932,-1.398120,-8.739131,-5.487304,-1.025259,-2.921307,0.830565,-9.106234,-5.120745,7.660446,5.724721,-2.193511,8.064359,-4.606773,-1.360733,-6.410388,-6.193239,-8.576057,-5.836837,0.619474,9.346720,8.851821,-3.972109,-3.351525,7.121075,9.478049,-6.976968,-3.676548,7.634248,-9.061886,-1.759526,-1.749739,8.701051,7.975346,5.741664,-0.001364,9.839953,7.635776,2.426260,-0.639870,9.372593,2.625587,5.196810,3.393955,2.187777,-3.283189,-6.843532,-2.003255,3.217332,0.623323,-3.587183,-7.319519,-8.491876,0.136760,6.370303,-4.964458,-9.363855,-6.783797,4.281718,-9.042574,-0.779234,3.077406,7.529826,-6.494471,5.791227,-2.691002,-7.573207,0.496151,-2.049889,-8.051493,-5.821252,7.393602,6.398101,-5.435133,2.548979,3.615410,-9.718612,6.183653,-7.554220,-0.305074,9.510432,8.223442,8.745494,-2.572853,-2.344830,2.192471,0.303537,1.803090,9.298818,-4.868184,-2.323902,-1.269302,-6.252065,-0.982956,4.436699,-6.621291,3.027773,-8.831229,7.261806,1.991069,-5.342909,-4.099685,1.134153,-3.062641,-3.192502,9.455677,-4.396110,2.504477,9.448341,2.793415,-2.815295,-9.494924,2.092523,0.017792,9.146517,-5.771871,4.705389,-0.335854,-8.021037,8.166333,3.261021,8.787239,-0.838470,-8.201250,7.289415,1.799597,1.354780,2.749370,-7.326210,9.196908,8.449189,7.839543,5.551871,3.289257,-2.048333,-5.999592,-6.060343,3.196698,-5.639044,-8.794786,5.272052,3.802472,6.652737,-8.170826,6.391017,-2.281431,2.360463,-8.234716,4.764661,5.367591,-3.284920,9.396169,1.183070,-2.060011,-7.322746,2.431732,-4.753002,-1.435420,-7.411512,0.176629,1.868517,-6.718566,-6.183411,4.985488,3.813599,0.191528,-4.219541,-6.078873,-1.457060,3.116640,1.023627,-6.569569,7.243371,-2.287002,9.360338,-4.134783,1.201837,-8.599098,3.914235,4.503466,-7.940114,-9.944399,5.727928,-1.145090,2.594419,-9.740125,3.000516,-9.177604,8.336272,-4.103992,5.623379,6.392131,0.091335,-6.615546,3.252152,7.729228,-9.854801,-7.756145,-4.400350,8.425236,-6.695296,7.545689,0.653983,7.987449,-3.735813,8.165799,-0.037030,-9.610504,-6.477243,-1.753310,-4.519890,8.084569,9.813547,-3.987012,3.104848,-8.727442,2.532523,9.976803,8.989523,8.785260,-4.845550,5.021396,-0.615376,-6.446793,-0.889712,-3.925179,8.223764,-0.399313,-7.653813,-6.384393,-7.922131,6.058914,-4.861254,-3.719269,8.492355,4.459452,7.097622,-9.494678,-3.882959,-1.876543,6.226667,8.627927,0.476713,-5.593598,-5.130057,0.922576,7.680316,-4.729546,1.882519,7.988407,7.045583,-9.312844,-8.564855,-9.893821,1.082605,8.490476,7.766541,4.467879,-5.793305,-5.762883,3.022918,-5.282548,2.003596,-8.712581,2.931124,8.037972,0.185462,4.512881,8.955220,-2.190473,3.692949,6.535093,6.005756,7.952505,-8.707049,-4.243028,9.041822,-1.497376,-3.075658,2.697268,4.723424,-1.467144,-5.672300,-0.339845,4.842585,-5.375591,-6.160249,5.420873,7.316580,-7.040246,2.324247,7.310560,0.006583,5.793859,-6.058738,1.444285,4.260967,-5.678677,-6.276830,2.300960,-3.431218,-8.961481,-9.632915,-4.945471,-9.786130,4.846855,3.687050,-4.468183,9.039895,-9.452406,-7.822688,6.974200,8.607540,5.708046,-9.895306,0.580900,-5.219314,9.215398,-8.628350,-8.005197,-4.341812,-7.894659,-2.736980,-8.751804,-0.497212,-0.739193,6.252077,-2.742080,2.276182,-9.752721,6.058782,-8.189142,0.624285,-1.227623,7.321725,-6.143100,-2.285714,-8.693116,9.698221,-8.986400,1.383517,-1.245763,-6.740535,-0.328392,-1.657416,3.395890,-1.181660,4.901301,-5.190163,3.726787,7.312930,7.108380,-4.146295,-7.910828,1.480487,2.661459,7.207892,2.253498,6.690362,-4.754290,-1.322191,8.478855,6.780343,-1.532602,-9.411276,-9.543909,7.056957,3.491487,7.055498,7.411181,8.938399,7.753919,-8.009738,-6.356439,-2.003753,8.563258,4.178301,-0.693572,0.753007,-2.020874,-7.306747,7.469536,-8.980994,-0.671100,2.749450,-7.051991,-0.893537,1.399324,-4.676624,-7.579957,-1.948502,9.119521,-2.098719,8.721903,-8.296870,9.581228,-1.066531,-2.471367,-8.409388,-7.762513,-4.419634,-8.053567,-8.956267,5.792783,0.369119,-9.337476,8.267869,4.155201,7.305601,-1.291926,-1.722804,-9.685165,-4.925122,-9.728479,1.179387,-0.957964,6.232471,5.117518,4.580676,1.730286,-2.932037,-8.796778,3.129555,-3.623260,-3.326527,0.577386,-2.079538,5.144825,-2.139813,2.542000,-7.596472,-5.048003,-9.870922,-3.756618,-7.175325,2.208602,4.497731,8.008955,1.181036,1.844868,-2.558650,0.029314,-3.120861,0.358861,-9.284617,8.862281,3.639713,-0.826759,4.225026,5.471453,-7.919441,-9.346786,-7.054431,0.516497,9.906962,-5.216263,3.621508,8.779810,-5.083889,-1.236454,0.048920,-2.946528,2.029649,1.387881,4.625310,4.203599,4.944193,2.186096,4.258256,3.065115,1.440228,-3.742345,5.048551,-9.709108,-8.773086,-8.612465,-6.213129,-2.349539,-2.473028,-8.446018,-0.219478,5.375839,-8.045944,-6.659880,3.070812,-3.321614,7.981666,6.745723,-5.803035,-8.811024,5.519580,1.926970,6.387316,3.307797,0.546626,9.125652,6.334360,3.360553,1.085392,8.781959,6.561237,7.578039,-8.999870,-7.952133,9.537768,-9.440212,0.638174,-9.531270,2.869682,-5.667026,-4.031651,4.887059,1.481127,5.948217,-9.685642,6.410657,-1.346907,-8.033262,-9.040822,-3.075545,8.664780,-6.932048,-1.815496,-6.492883,-1.387506,-6.683933,-2.046458,6.631636,-3.204073,0.760592,1.098990,-0.732413,4.011717,3.987558,0.257709,9.182299,-4.879655,-4.876374,1.015283,-1.905771,1.536887,-8.950428,-8.014751,2.958168,-9.524677,1.044317,-3.654874,3.777266,-1.591729,7.906757,-3.398835,2.912127,-7.709075,7.140946,-8.372664,7.641165,-5.730316,0.317133,6.433024,0.893956,9.240466,-8.160399,0.995294,-2.966117,-5.592052,9.817625,-9.677919,3.101800,-5.207711,-7.270932,-1.093031,4.706105,7.380752,-2.682089,3.331655,-7.407907,-5.997401,-5.931391,4.041942,-0.014335,-9.760819,-5.872003,-5.037402,9.180343,0.273506,6.764076,-5.460968,-4.682061,3.774602,-2.533584,4.162067,-6.894210,7.583232,7.455597,7.318538,-3.168357,0.289468,-6.641024,-3.870162,9.302399,-6.616673,-3.930511,7.450163,-7.849880,1.164267,6.009844,-6.849310,-8.938980,6.119915,-0.296595,2.636962,-3.049641,6.847303,-6.977738,6.769240,6.451987,-3.470694,-4.704881,4.586816,5.565594,1.731334,7.237189,-5.869763,-2.930041,2.770942,-6.629058,1.650216,6.118241,2.937307,0.626440,5.456163,-3.934967,-6.511139,2.471134,-8.797789,-0.702098,-8.200458,6.897227,5.312226,-8.261739,-4.076824,-3.271483,7.744835,-9.833083,9.452944,0.104717,2.305698,1.737417,-2.869602,1.021959,4.735156,2.283220,5.454514,-5.261176,-8.889533,5.512941,9.915263,-9.963025,6.828552,6.441568,-6.714238,-8.210461,8.368383,6.685414,-5.559951,-2.120792,-5.514016,3.040472,-8.978680,1.297327,-7.191518,9.148094,-2.760272,9.710561,-1.327522,-9.406399,5.550928,-6.281421,-3.446656,1.573624,-2.444274,-0.378084,5.433391,-8.483132,4.917261,-2.337398,-0.841795,2.637975,9.136246,2.616435,-8.693438,5.125794,-1.993530,-5.883829,3.074579,5.707977,6.675255,5.740547,-0.865694,-4.615220,5.840176,1.100135,-5.748584,-8.600465,3.207974,4.047322,4.684259,-9.790575,4.702319,1.960770,-1.148437,-3.589809,-4.801893,-8.612177,-7.473030,7.662756,0.556145,0.232464,8.871412,2.063314,6.456533,-2.568739,5.879395,-2.550922,2.082409,-5.789890,1.880211,4.765674,-3.248775,-2.728305,-9.450718,-7.278229,-4.246520,3.429278,3.572016,3.257036,-3.482859,2.768020,-9.163623,-9.085986,6.562089,3.467835,6.553390,1.606484,-3.247940,-9.685503,7.866754,-8.589858,5.041259,4.290202,-5.123526,5.258871,4.704787,4.209247,6.200184,5.643392,-7.954230,8.872140,-6.456187,6.120424,-4.255813,9.231147,-1.694448,9.753635,-4.033265,-1.846534,9.202132,4.469356,-6.577265,-4.693837,-7.579601,6.792653,-6.598527,-8.282393,1.033127,7.511987,-6.398144,4.803145,-4.198250,-3.053693,7.538404,-2.714611,-5.275750,7.761036,-3.790451,-4.139699,-9.653455,5.403185,-1.965017,7.339200,8.307492,8.677081,5.374830,-3.531519,-5.137812,-9.796935,7.915823], dtype = "float64")#candidate|2022|(1568,)|const|float64
call_2021 = relay.TupleGetItem(func_1058_call(relay.reshape(const_2022.astype('float64'), [1568,]), relay.reshape(call_2011.astype('float64'), [16, 2]), ), 5)
call_2023 = relay.TupleGetItem(func_1062_call(relay.reshape(const_2022.astype('float64'), [1568,]), relay.reshape(call_2011.astype('float64'), [16, 2]), ), 5)
func_1792_call = mod.get_global_var('func_1792')
func_1794_call = mutated_mod.get_global_var('func_1794')
call_2034 = relay.TupleGetItem(func_1792_call(), 0)
call_2035 = relay.TupleGetItem(func_1794_call(), 0)
func_2000_call = mod.get_global_var('func_2000')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_2041 = relay.TupleGetItem(func_2000_call(relay.reshape(call_2021.astype('int8'), [4, 4, 16])), 2)
call_2042 = relay.TupleGetItem(func_2002_call(relay.reshape(call_2021.astype('int8'), [4, 4, 16])), 2)
output = relay.Tuple([call_2011,call_2017,const_2018,call_2021,const_2022,call_2034,call_2041,])
output2 = relay.Tuple([call_2012,call_2019,const_2018,call_2023,const_2022,call_2035,call_2042,])
func_2052 = relay.Function([], output)
mod['func_2052'] = func_2052
mod = relay.transform.InferType()(mod)
mutated_mod['func_2052'] = func_2052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2052_call = mutated_mod.get_global_var('func_2052')
call_2053 = func_2052_call()
output = call_2053
func_2054 = relay.Function([], output)
mutated_mod['func_2054'] = func_2054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2052_call = mod.get_global_var('func_2052')
func_2054_call = mutated_mod.get_global_var('func_2054')
call_2055 = relay.TupleGetItem(func_2052_call(), 2)
call_2056 = relay.TupleGetItem(func_2054_call(), 2)
func_1895_call = mod.get_global_var('func_1895')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_2079 = relay.TupleGetItem(func_1895_call(), 1)
call_2080 = relay.TupleGetItem(func_1896_call(), 1)
func_284_call = mod.get_global_var('func_284')
func_286_call = mutated_mod.get_global_var('func_286')
call_2081 = relay.TupleGetItem(func_284_call(), 3)
call_2082 = relay.TupleGetItem(func_286_call(), 3)
func_1815_call = mod.get_global_var('func_1815')
func_1816_call = mutated_mod.get_global_var('func_1816')
call_2092 = func_1815_call()
call_2093 = func_1815_call()
func_1442_call = mod.get_global_var('func_1442')
func_1447_call = mutated_mod.get_global_var('func_1447')
const_2095 = relay.const(-4, dtype = "int32")#candidate|2095|()|const|int32
const_2096 = relay.const([-1,6,3,3,-6,-8,-9,-4,-4,2,7,9,4,5,8,10,4,-7,7,2,-5,6,7,-5,-5,3,4,7,1,7,-9,-7,2,10,6,-3,-2,8,-7,2,-7,-5,-8,10,6,9,4,-8,1,-8,-10,9,7,1,10,7,-10,-10,-9,-10,-10,10,-6,-2,4,8,-10,6,-4,-1,-2,-4,5,3,-4,6,-3,-10,5,-9,-4,5,-2,1,-7,2,5,2,-10,3,-9,10,7,4,-1,-3,8,9,6,-9,4,-2,9,-8,-10,-5,-2,-4,2,-1,1,-2,-1,-2,-2,-1,4,5,9,4,-6,2,-1,-7,6,-8,3,7], dtype = "int32")#candidate|2096|(128,)|const|int32
var_2097 = relay.var("var_2097", dtype = "float64", shape = (1568,))#candidate|2097|(1568,)|var|float64
call_2094 = relay.TupleGetItem(func_1442_call(relay.reshape(const_2095.astype('int32'), []), relay.reshape(const_2096.astype('int32'), [8, 1, 16]), relay.reshape(var_2097.astype('float64'), [1568,]), relay.reshape(call_2079.astype('float64'), [32,]), ), 3)
call_2098 = relay.TupleGetItem(func_1447_call(relay.reshape(const_2095.astype('int32'), []), relay.reshape(const_2096.astype('int32'), [8, 1, 16]), relay.reshape(var_2097.astype('float64'), [1568,]), relay.reshape(call_2079.astype('float64'), [32,]), ), 3)
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
const_2107 = relay.const([-1.463881,-2.267974,-3.044233,-6.930733,3.935009,4.311984,-5.091367,-0.021444,2.786502,-0.383941,-7.120333,-6.515524,-3.123756,-5.134259,-6.238391,-8.744592,-5.148690,5.797779,5.592751,-3.881133,-0.031477,5.700151,2.200763,-3.739379,8.110333,8.275531,8.252432,-6.328917,0.447165,8.625851,4.595006,-4.661384,1.090448,-0.968502,-0.483913,6.037575,-8.497679,7.587092,-4.038733,-7.979931,4.184337,9.526849,-8.589484,-2.701466,-1.423040,7.027386,-7.627625,3.614883,-3.080812,-8.504037,-7.971090,2.163909,-6.311379,-7.269014,-6.803904,-1.991515,-3.650380,-4.123502,-5.745611,0.407047,-4.795385,-9.277455,-7.499784,-5.234861,3.496227,9.237355,-4.081553,-8.967720,-6.594797,5.831436,8.990743,-6.714388,8.234526,-0.540628,3.340683,2.019748,7.790918,-0.326341,1.899591,-1.927955,5.045392,6.303329,-5.433157,-0.285310,-4.012522,1.784066,-0.684148,-9.989097,-4.911981,3.699450,-5.044116,7.354619,-9.718572,7.139555,0.378103,-2.272180,-9.231184,-0.795185,8.380785,5.941161,0.436751,6.155903,-8.316550,1.430644,0.375574,-6.297124,0.858151,6.818034,-6.916918,-2.625653,-1.322706,-6.809563,-6.111963,4.072493,-0.608515,2.332240,3.454930,0.093901,-4.105158,-2.964077,2.108576,5.907326,-8.711894,-7.676841,-3.122343,-5.728542,5.970884,6.721815,-0.855938,9.382545,0.771064,-0.830868,5.620664,-9.753996,-4.007545,0.185321,3.644549,5.693933,3.234669,-2.999032,-4.219963,-4.238713,-0.615505,2.410498,-5.061707,6.028106,5.459038,-3.463170,0.047277,6.880487,8.614039,5.609511,5.083310,9.489381,-7.431294,-4.122219,-0.392239,-2.111894,-4.570310,6.784985,-3.412256,-5.890323,-0.673442,-1.760619,8.972372,-8.402159,9.409842,-8.218134,-8.990302,7.801877,1.384104,8.181956,3.020427,-9.834043,0.268970,-4.435194,-5.850933,8.409831,-7.903185,-1.712684,1.306125,-8.693397,-4.943248,-9.270186,-7.027291,2.826005,6.454053,-5.912781,-9.536586,1.321005,-5.834140,8.895790,-3.483927,-3.945870,2.860681,4.130972,6.472857,6.697614,-0.783800,-4.670685,1.948057,-5.689396,-2.516708,9.362106,-9.572973,-2.002586,1.941373,1.100025,-1.335813,-4.755838,8.828470,2.749131,0.514252,-7.607139,-0.548711,7.776533,7.673662,-3.072091,-2.514468,-7.879086,-7.855835,0.327766,1.336222,-8.138081,-0.700214,6.937663,-2.348519,-5.527412,9.222479,1.483378,3.728406,3.630359,-7.547548,-4.976415,-3.887576,8.651367,8.618548,-6.941547,-1.372423,7.346373,4.834818,-0.457512,1.648059,8.664118,5.663729,-0.306774,1.607027,4.020343,5.030430,-3.680811,4.135862,1.497162,3.833516,3.440993,-1.978209,-8.489510,0.742238,6.940610,-4.262799,0.988865,2.471216,-0.667150,6.034505,-7.856373,-1.177131,-5.517434,9.763675,-4.036248,6.159305,-6.096375,-1.189024,8.070947,2.775647,-2.437792,-4.934683,2.010198,4.435116,-3.413133,-5.759669,-6.085604,-1.227851,-3.150987,-1.517094,-7.208516,-3.782680,3.877292,3.360370,-1.646824,8.495868,-5.554221,-1.953922,3.137795,-6.642011,-3.531420,-1.514495,1.842479,-5.897080,-1.336415,-3.614489,-0.601267,4.969571,-1.160745,7.378373,5.150897,4.239694,-7.898910,-0.959318,-9.609394,8.431965,1.994114,3.793781,-4.697217,-7.866809,-5.188042,7.689002,5.606907,-3.669217,-5.792452,-9.977132,-0.869697,9.418127,7.046858,-7.537974,-7.184863,-4.893936,4.785062,-1.062838,5.744663,5.755413,-4.052375,4.340428,9.439041,7.404321,8.983748,-5.867473,4.047320,-7.436900,9.869215,-2.630231,-2.977427,8.753318,-8.726619,-6.807950,-5.621803,9.374315,-0.432148,-8.652519,-8.239788,6.808857,8.388045,2.301406,-4.042008,4.239161,-8.832709,3.880399,-7.468795,8.027388,7.565766,7.138785,1.549797,-3.467610,9.210302,0.846727,-6.313632,3.396539,-3.798793,-3.973031,-1.007475,-6.164049,-9.017677,2.842865,-7.694496,4.254824,-7.920520,7.072489,-6.481714,-8.441186,-4.004277,1.482239,-1.500555,-6.424184,-4.988529,0.793971,-0.908471,0.828812,-0.387754,-4.191534,9.536779,-2.761922,-1.942682,2.708542,5.849867,-5.340647,-0.014385,-6.655673,-1.563801,0.097230,4.392464,3.425952,3.131126,-8.758731,9.111487,-1.344587,6.588467,2.861210,9.016922,-3.074926,-7.067669,-6.709506,-1.735180,8.554255,-8.233987,9.496395,-0.106098,2.338642,-8.981483,0.673929,-1.296653,-0.519789,-3.709299,5.564673,8.620229,-3.247528,-0.598432,-2.391717,7.383363,2.102459,-3.574794,2.981682,0.523020,-3.140517,7.270239,-4.483724,-4.284459,0.199705,-8.462412,-8.484108,-7.192963,7.606938,2.425946,4.755006,0.853464,-9.329227,-3.024780,-4.607327,0.396595,2.471969,-9.098957,-6.072069,-3.507894,9.007551,3.045094,-6.451890,-4.883208,-7.830518,7.097341,-3.395707,3.982056,0.059392,5.759272,3.926729,-9.268550,0.157165,-9.211842,2.913717,1.404147,6.852724,-6.446107,-0.015809,3.157489,9.562804,-1.274972,-3.218840,-7.395840,4.226565,6.162989,-6.042685,9.828488,5.208817,-2.819511,8.841864,2.551271,-6.692133,-2.436933,1.514689,3.169114,5.852370,-9.816387,6.643280,7.122522,-9.637573,-4.194073,-4.682133,-1.780913,7.219332,1.632005,-4.099317,-8.479511,-3.847309,1.405222,-6.225887,-6.227989,2.556820,0.460691,-3.236730,0.549796,-2.915936,2.890294,-5.834495,-4.645521,-6.799467,-7.437293,-1.984084,4.931177,8.642096,-5.286976,-7.556018,6.201350,-3.254320,-4.969348,2.931702,7.005614,1.754992,2.480391,0.166899,-0.860652,3.745189,-3.519393,1.892372,-1.772655,6.779183,-3.643547,-2.292780,0.984867,5.900982,3.856549,4.078061,-9.354969,8.811045,-6.748922,1.405225,0.613302,1.144226,-3.487405,4.849233,-4.642057,-2.994295,-8.106444,-9.947356,5.969136,-0.021080,2.355806,1.153466,-8.127121,1.058184,5.405227,5.329338,0.981192,2.905266,6.917602,-4.213175,0.839340,7.850269,2.205511,2.071688,5.987546,0.410193,7.459624,-2.978306,-4.904804,8.331548,-2.285494,-6.756826,5.814703,3.912867,-6.826934,-0.887892,-5.754547,-5.898095,-6.750958,-5.682266,5.519739,-1.297314,5.792620,-9.188422,-3.919270,3.510376,9.561520,-6.160936,3.200406,5.230485,4.903446,8.051634,3.082635,-4.947456,2.263957,1.124251,-1.660021,-7.765326,-9.683087,5.486219,-6.542283,1.513459,-4.801473,-3.693141,-1.222474,-9.850367,-5.390426,6.451890,9.673175,3.850058,2.792909,8.523327,-2.676145,0.383769,-1.825199,4.556689,8.995547,-5.010746,-6.528580,-0.470678,4.439294,-0.018837,-6.771316,0.397896,8.488631,2.261965,-2.372688,7.250629,-6.031761,7.791396,4.901664,8.304597,-6.353827,4.051024,-9.617478,7.260517,-7.113973,0.968755,4.194506,-3.484990,7.917178,7.556232,-9.531069,-2.762428,1.781795,1.584227,-7.645003,-7.837460,5.065784,0.862580,7.079787,1.114888,2.266573,-1.876496,5.564969,4.409563,-8.434564,-6.718017,7.628645,9.381091,1.140573,-0.525544,6.353019,-7.870128,-4.158161,6.071638,-1.757851,7.795313,0.880058,-6.040136,-1.123752,-8.670450,1.545530,5.099367,5.142515,8.529615,5.230855,9.981491,-9.334248,4.552597,2.688178,-3.272561,4.840103,0.325922,-6.891318,-9.814394,-2.855306,1.607937,2.782971,-1.180696,-8.097318,7.219254,4.874602,-4.015200,-1.393205,-9.933309,-4.803885,6.461721,-5.746599,0.525436,5.591721,1.033807,-9.973565,8.105055,1.745441,-9.525817,7.239595,-6.419882,-9.798031,1.983155,-0.341525,4.435988,-9.395347,4.521081,7.163688,4.236723,-7.570573,-3.633937,-2.343603,-0.469878,-4.423593,8.081762,0.790086,-3.297759,-8.522900,-7.573994,-2.389029,-7.017037,4.973950,9.982883,-1.450152,5.791023,-8.447710,0.759444,5.030122,-0.108447,-7.659567,4.864372,2.097589,-2.090627,0.634905,3.054732,-0.073348,9.622030,2.197277,-6.626075,0.121509,-4.074788,-0.016409,-3.152197,8.414764,0.926903,-1.054572,8.221352,-5.162432,-9.025567,2.140053,9.530696,7.536242,1.778061,-2.350130,-7.147558,3.995957,5.193547,-7.218513,3.800754,-9.246980,7.911312,8.948066,7.782477,-7.842802,-0.410773,0.746116,6.039731,-4.209292,4.013152,5.087559,-7.314374,-0.092312,-4.875936,-8.701786,-0.119582,-3.883243,4.905400,1.661672,9.010117,-1.540806,1.436159,-4.209533,-3.017029,4.630069,2.862354,4.847060,7.225655,0.605888,-3.927255,5.554934,-2.594924,1.562883,3.649368,-7.453530,-0.365764,-6.071530,-1.347570,0.222107,8.289136,-0.055378,8.418776,7.644742,4.595876,-6.810964,-5.737830,1.413020,9.235523,-0.510341,7.765753,0.431351,-3.712567,0.433543,-8.041093,2.792828,9.809874,-9.762270,-3.589460,5.275682,-2.412253,6.041388,5.513423,-5.426036,1.696671,8.236539,0.277252,1.321688,2.094062,8.409746,8.848617,7.770565,-7.814912,4.758245,5.696977,4.267238,-8.661809,-2.764759,1.453518,-7.423128,-2.642361,0.402231,-7.263802,7.906141,7.746856,-8.567620,5.688931,2.081798,4.894831,-4.357042,2.185359,4.615669,1.346489,2.481060,-9.082175,9.369291,1.358778,-6.986341,4.396869,5.577552,-5.156354,3.666483,-0.994588,-9.791553,6.851806,-1.385638,-4.808106,-7.316215,-1.793098,-6.515734,2.083867,6.835964,-9.497794,9.749095,8.286541,-8.822098,-1.008772,3.775884,-7.826029,-0.708565,0.938404,-0.821984,-2.379533,0.447038,-3.494111,8.753013,8.144982,-1.950289,5.606784,-1.112567,1.203931,-1.142208,-6.416693,-3.878434,6.069168,7.189849,8.014418,-9.479405,-5.631382,-8.275650,0.025437,9.601291,-5.096760,-4.000876,1.436989,-3.716021,3.662622,-9.368405,7.657882,-0.656948,2.184655,1.616957,0.811257,9.212632,5.199464,-1.920022,8.388143,8.522011,-2.520064,6.471288,-3.396323,-7.560698,3.984323,-9.761595,0.630636,6.060311,-4.797548,4.816687,9.838394,2.326484,9.383793,9.652229,2.282671,-4.850932,3.765503,2.411249,-8.965819,5.165501,-1.284361,-8.852102,4.584351,5.422749,-8.278415,6.342982,3.892390,-1.667901,1.461889,0.214273,-1.419415,-9.490455,-9.311235,-1.240261,4.283362,-0.668705,9.067894,2.662485,-1.501237,-2.127799,6.697589,-5.151390,-7.184808,2.853964,1.957849,0.821488,1.012417,9.458642,7.355467,-2.109135,2.843061,4.310292,9.755331,9.767027,9.854584,-8.642823,-5.849010,0.382871,5.593356,-8.670864,1.566891,-2.002327,7.484674,-5.722202,4.046076,3.612448,6.239374,5.712751,6.605438,0.715809,-2.890879,5.741450,-1.401574,-4.247807,-0.874440,-1.917770,-5.699794,-6.335856,-6.627918,-6.153270,6.177540,4.101169,-4.578431,9.259156,9.966239,-8.894515,-1.758544,-8.551810,-2.053389,-5.299599,4.086173,4.340927,3.619090,2.248603,-4.262025,-9.049983,0.500259,9.646670,-8.208807,3.757260,7.360457,-2.506186,-4.855353,-4.010373,7.437598,5.993228,-0.467871,-6.211976,-3.296127,7.777860,3.562500,-5.434286,8.874769,8.319977,-1.358826,-9.056327,-2.468825,8.268992,3.434588,-0.447907,-7.412970,-6.816281,-3.881866,-1.742936,-0.328070,6.925324,6.894419,2.345434,8.063185,5.868322,2.169622,4.456212,-9.367372,-8.760013,0.449345,-4.072274,-4.099424,-0.214635,1.628167,2.028512,-8.149294,1.445869,-6.149067,4.548764,6.753845,2.419967,-4.482200,7.375647,9.739721,-1.418025,-0.890829,-7.089507,9.354126,8.606067,-6.974326,1.812999,0.641351,-9.160941,9.932733,-8.536577,-3.813171,4.190097,-3.291065,0.566561,7.158951,-6.082771,-7.238415,-5.241031,8.476167,-7.886666,0.546917,1.654531,8.685876,-4.002242,4.818298,1.502748,0.872591,-6.240156,1.379390,7.317116,1.545572,-6.033070,8.123784,-2.530966,-0.627838,-8.275764,-7.999558,1.651776,0.787115,-3.573266,-8.177555,5.719809,-8.464130,7.277577,1.776371,-4.431030,1.389485,3.650041,-0.004149,7.560664,-1.208500,-6.118793,8.225976,-1.556192,2.944471,4.532696,1.785346,6.388503,-4.899783,8.257630,-0.344061,0.266692,5.274393,-1.795685,-4.742334,-4.170907,6.778356,9.269510,-9.290658,2.519768,-2.866693,3.591904,2.890133,4.943816,-3.262856,-8.497428,2.163972,-4.655532,-4.334905,-4.887359,-7.278265,0.495385,8.008150,7.708854,3.684409,1.587167,6.869583,4.362006,-8.159270,5.926149,0.855822,0.750640,3.345183,0.390031,-5.661752,-4.927752,6.055493,-3.877684,-0.216762,-9.578892,-8.293880,1.618093,0.977222,2.929980,9.805300,-1.071743,-8.794607,8.722383,7.185674,1.737293,-7.676526,-1.015666,7.113295,-2.614483,-6.555367,8.876218,0.112596,4.350368,7.364654,-4.414574,1.434758,-7.625610,-6.068587,2.939088,-2.451240,4.630925,-8.518672,-0.784781,-3.423975,2.421313,-4.961607,7.165389,3.417921,-2.118832,6.214045,1.429853,9.318042,-7.149792,-1.879842,6.452286,-0.597840,2.072013,-8.537271,8.576168,1.669198,-3.047629,6.050864,3.020728,-0.528596,-7.473916,-9.306033,-7.311014,7.575818,2.058912,-5.343232,-8.129350,2.448480,1.945069,-6.841210,-8.201718,7.840092,5.303763,-4.482139,7.732972,-5.802357,9.410867,7.610755,-6.547258,-0.738679,-2.829393,-9.345234,-6.883941,0.878690,5.787555,-5.469835,4.133615,-5.236198,-5.219400,5.083802,6.617964,4.956127,-0.795159,-7.604889,8.997876,-8.237832,8.969214,4.269981,-4.904379,4.377375,-9.636230,6.083806,0.932074,-2.543227,-3.617700,2.859773,7.902841,-8.433543,-4.360639,-3.197195,-9.232216,1.989870,7.425730,8.740460,7.577145,8.584841,-5.368824,8.839299,9.058978,4.690354,9.240849,3.347471,-9.037450,-7.638143,8.031464,-2.631923,2.240091,7.640599,-6.746127,-9.687227,-5.413276,2.748750,-7.358152,-9.918418,-7.363651,-2.398299,4.992036,-6.295783,7.259810,-8.832889,6.730489,-6.754921,-8.313767,4.026203,-0.021994,1.682748,-6.525435,5.712484,1.950046,-3.408553,-5.380613,-1.491677,-3.650392,1.427494,1.736381,-7.419770,-2.261230,-7.247038,2.162514,-9.751827,5.540438,-8.015826,-8.147907,7.968048,0.821881,-1.851266,-3.306315,4.953700,8.719829,-9.392677,-6.176963,-8.392868,-7.028588,-0.948361,-0.143344,2.571337,-6.767428,8.190631,-8.551461,-9.846222,-5.436732,4.329031,3.077643,-7.341675,6.089885,-0.698456,1.787382,-8.235564,1.828996,9.404121,1.256722,1.065035,-9.574875,3.115943,5.967597,2.865196,-8.013546,-3.546693,7.438203,-8.848515,-5.919033,4.922034,1.577868,7.784216,-9.402826,9.091180,1.255291,8.524819,7.573498,-4.823409,-1.507043,6.704402,-7.464172,1.369024,-9.729091,-0.489457,-4.021546,-1.486636,-6.808150,-4.939667,9.559640,-9.444896,-6.695613,-9.919027,-8.648885,3.342390,-9.562846,0.516773,-4.155469,8.386670,8.242414,6.728662,7.047921,7.944540,6.918905,-7.866764,6.210465,-3.038697,-5.471044,-7.623570,3.341626,6.227616,-8.737952,4.443466,5.890902,6.818288,-1.801936,-2.499874,-9.419188,1.072199,6.955083,-3.818402,0.846825,4.802928,-5.157684,-6.450023,0.963224,9.643915,4.942265,-4.998434,3.589105,1.186632,7.828604,2.355840,8.030142,5.460828,-7.305071,-5.224471,-1.042837,4.451495,6.121904,4.840085,-2.938111,-4.609950,2.778141,-6.008781,-3.519035,-3.877163,-3.197020,3.522207,8.047194,-9.878011,2.128465,1.754416,-6.791518,-5.842477,-3.867319,-9.330522,-0.412285,-5.662537,-4.130348,7.529640,-5.117403,-7.667957,6.882505,5.914764,-1.805993,6.122436,-1.630049,-4.044283,0.611109,-3.995872,-3.803537,-5.655325,2.841062,-3.027189,-3.103137,-1.050070,0.618222,4.493284,-5.119772,4.417066,-5.022494,-2.041689,3.357091,-8.825360,1.889449,9.971470,2.204133,7.524944,-8.634842,-0.364710,7.824485,-2.261827,8.391087,4.192515,-2.585846,6.523647,3.228458,2.591134,-2.752697,-5.024666,-6.521063,0.792388,5.550613,-2.166635,-1.565633,-1.216945,2.540009,-7.239887,-4.939054,-5.615330,1.009443,-2.746720,-0.506941,4.099603,1.622201,-2.694313,8.352160,3.439245,-5.561150,5.655379,7.084212,-6.468619,-2.370607,3.132404,2.126167,6.486237,7.517315,4.649512,4.712729,-7.054960,-4.008376,-2.249180,-1.112410,9.224824,3.036287,7.258325,-9.103452,9.108758,7.636637,-7.738652,-3.704211,6.012198,9.488080,6.066002,4.074530,7.817502,1.193067,-5.077236,3.797306,-4.295318,-8.118929,7.220700,-2.844111,1.273857,-0.671522,-9.634249,7.540907,-2.472260,-0.158801,9.654698,-9.905484,-7.240972,-8.363660,2.158808,-4.184660,-9.351010,-1.717432,0.008101,-2.683262,-2.962473,-1.031132,6.701492,-8.584457,-6.814145,-4.160257,-3.560153,-9.568249,-5.015286,4.909695,8.439418,3.970964,-2.000601,7.781237,-2.697717,-7.606044,-4.026206,8.291757,-9.126565,-7.327137,5.967425,-4.948763,4.152277,-9.774828,4.218273,0.414412,1.607903,-7.152744,-3.026282,2.488748,7.885067,4.676973,8.365751,-2.400090,-0.338008,-4.594153,3.048588,-5.023268,-9.996604,-5.703306,-8.700701,-6.487177,-9.204208,-7.185380,-9.098939,-1.585646,5.905019,-6.134247,-4.584856,3.275611,3.032125,-1.239215,-1.293968,1.257550,4.011475,2.284384,3.701124,5.398210,-1.464766,7.112242,-8.792690,2.897594,5.511000,-9.707130,-2.883513,0.616708,8.721139,-6.201636,-7.820435,-0.705378,7.380205,4.129232,5.650508,-3.543571,-5.524524,1.968718,2.484770,3.821026,-7.916274,8.791447,2.319217,-3.266397,-6.968029,-8.860355,-1.757089,8.570434,-6.127172,-9.138976,8.419136,-2.565160,-1.096384,-8.714517,-2.795737,7.132387,5.075243,8.227963,3.107913,-7.865380,-4.010100,-3.706266,8.434293,-7.112200,-5.056865,-0.463188,8.117169,-8.870325,-1.274308,-3.924717,-1.962065,7.537217,-8.028814,-1.390595,-0.133279,4.234185,2.550145,1.217648,0.712431,6.387121,-1.776249,-6.286879,-0.255581,-0.007605,0.459845,4.415164,-3.148897,-5.226816,1.241089,-7.422159,0.372407,-7.787209,4.983175,1.804042,2.758525,-0.474442,-0.595650,4.195949,6.904222,6.043452,-7.864066,-4.924470,7.334882,6.819059,1.886875,-2.925764,-9.150675,-5.132755,-1.911299,-1.630820,-2.540449,-1.769136,5.579813,3.189889,3.334461,-3.300054,0.418000,-3.814743,8.761631,1.623690,8.535290,1.094016,-4.636151,0.358292,2.823415,-4.332405,-3.746916,3.676911,-6.889397,6.911880,9.145462,-3.064998,-4.476565,-7.956152,-7.177500,5.780757,5.072057,2.919523,-3.232842,4.379033,6.708143,1.889437,-1.687825,1.410841,1.061410,-4.027709,-3.715288,0.519199,3.501909,-0.341608,7.392073,8.757147,-4.325095,-4.284850,7.382420,2.137474,7.276656,-8.623142,3.767569,-9.500099,-9.001102,1.802894,5.016215,-1.068444,-1.053699,9.073003,-4.047257,0.526014,2.204960,3.296262,6.899738,9.382529,9.329209,-1.331655,-3.084633,7.595080,6.777150,9.082268,7.769846,1.459405,5.045275,8.714660,8.280139,-3.993866,-8.322487,3.868007,-0.126356,-2.868005,-9.451225,-1.988852,5.402535,-5.893680,7.713302,-3.050232,9.918847,-5.931172,-9.801233,-5.255150,-1.303876,-6.188926,-2.167495,-6.738519,6.368871,-6.468642,0.295734,-8.000216,-4.324573,0.285305,-0.281371,-7.956028,1.798293,-4.320444,-8.240439,3.891270,-3.608305,5.123516,3.675875,3.690427,-7.716442,1.367035,0.513007,-5.561521,-9.278141,5.670502,2.457918,-1.912702,-2.393614,-7.759626,1.789591,-3.991145,-7.961240,-5.461618,6.242280,-0.082250,0.134850,-6.391999,7.081590,-0.141347,-5.410985,-9.178340,6.610490,2.019458,-3.751704,-2.960051,7.584235,4.285289,-1.969232,-6.649510,6.651845,8.158581,-3.680453,7.453924,-3.477310,8.015553,4.895796,3.053455,-9.406622,2.307293,-3.441217,-5.670822,-8.615036,6.928651,3.946289,-9.428998,-2.782910,3.201270,6.711242,-0.932894,-3.522970,9.214020,-1.003421,-5.275875,6.860794,4.248050,0.592118,3.264636,5.637539,-1.732482,-9.302686,6.978484,-9.797639,5.325027,-3.627623,2.602336,5.688841,-5.448363,7.190879,-3.105667,-4.623966,6.873707,9.288922,1.456444,1.019829,8.521616,7.414939,0.015542,5.350856,6.466744,-6.083728,-2.256196,8.397925,8.903812,8.943385,0.678293,0.432214,8.495484,-7.553346,2.244771,-6.341409,7.576179,-9.625456,0.010713,-0.828061,9.987833,-0.081522,-7.482656,-7.306623,-7.916392,-7.614426,-6.921731,-9.273117,-9.090598,-2.894944,4.717676,7.716763,-8.976087,7.516892,4.816660,8.828891,-1.501112,9.393852,8.530346,2.907541,5.339705,-6.005086,5.098345,-7.421575,9.144897,-3.941487,0.944200,3.264612,1.830501,-2.452079,-8.379812,7.302922,7.127790,-4.088041,-3.238158,-6.929808,5.124329,8.966066,-6.017921,-8.052958,4.058505,-6.027147,-6.839554,-4.516972,-6.239793,3.321108,-8.922925,3.426233,0.933678,2.677304,6.575452,8.044334,-7.665652,-5.846426,-2.703743,-1.481231,7.545815,6.874001,-6.281194,3.108647,-4.675342,-2.472284,4.311514,-2.832454,0.743427,-6.310348,7.555031,8.454140,1.239192,-2.352617,-3.362480,0.044943,8.500722,-7.832433,-9.052268,-6.138891,-2.430411,-0.425429,9.065273,-4.227632,-6.135223,0.320215,-3.746240,0.273244,-6.247682,-7.344989,-1.644312,-7.078776,-2.365177,0.432846,-3.261588,8.709693,-2.567290,-6.150065,-9.844809,-7.518932,-9.215400,-6.576720,-5.075998,-5.825178,-3.390847,-9.307621,-0.248708,-2.932164,5.602627,9.155645,-2.249440,-0.103765,-2.340537,-9.492958,7.694247,4.717102,-8.485133,-6.949654,3.152762,-0.024441,4.996557,-5.470755,8.877559,-1.349786,7.668080,4.361647,-9.955067,-3.661355,-8.001513,5.720382,-4.584015,9.821630,2.988820,0.436943,-7.287954,-9.167379,-2.752282,5.965888,5.310971,-7.212509,-1.241296,-2.826254,2.798900,5.076829,1.581751,0.728868,-4.565052,9.902269,6.730476,-2.352197,-8.218432,2.340559,-9.675292,-8.125614,2.940719,-7.005208,-4.255709,-4.546962,2.555944,-7.296262,9.419589,-7.428234,-5.846846,7.009521,0.011170,-5.191277,-5.761027,-4.105896,-9.667529,-7.010049,-3.631414,6.337283,-6.414364,-3.464296,-3.406078,-0.067744,6.721220,8.912783,-0.652482,9.653904,-1.259679,8.779062,5.216618,4.308829,3.300676,1.411541,-8.771012,-7.780069,5.779397,6.972612,2.430818,2.256302,-8.280207,2.235976,3.739177,-1.025617,-3.113525,-9.502662,-8.137524,5.795093,1.849725,1.465038,-7.584293,-0.426505,-6.905935,7.336091,-3.420577,-8.187443,1.429038,4.996050,-8.491166,-7.981603,-6.267529,1.381574,6.204335,-0.889174,6.883761,-0.350486,9.852196,9.569561,-7.025307,-3.334093,0.055254,-8.186479,-4.403469,6.581790,8.443114,6.318106,-3.779711,-9.528769,4.573737,1.614688,-9.847486,-2.198926,-3.109760,-9.170774,-7.743012,7.457366,0.269275,-8.870658,-4.026586,6.557059,-8.032682,5.029060,0.878847,-2.026147,-8.172042,4.207746,5.278715,-7.997216,-2.516798,5.680412,6.435785,-3.327133,-5.056314,-8.577112,9.092022,-7.730923,-4.266530,-1.084869,-9.963507,4.112811,-0.863604,3.634747,-9.464124,-6.629712,-1.323492,-0.040334,-8.982174,0.018020,1.751843,1.501648,7.759879,-5.416984,1.867174,9.002989,4.468038,-8.456986,9.632734,-4.249282,-1.710995,-2.253532,-1.016641,-1.468083,-6.299681,4.074355,-7.304946,-8.910086,-3.771917,3.075434,3.313616,3.862860,6.382640,6.378590,-8.328723,9.787135,-3.668983,5.223944,-8.793365,4.430048,1.327010,-6.503235,-6.165038,2.906094,-8.381661,-4.960646,2.121554,-7.806299,-0.095949,-4.524686,9.420814,2.743009,6.457908,-5.835024,-9.974711,-8.709327,-1.857901,5.346919,7.833084,-6.663305,-5.698925,-9.986265,-1.483049,-6.696580,-0.616122,6.690215,-9.159311,4.688557,-1.839172,5.005192,8.545310,-6.222048,4.966764,-6.836348,3.492249,-0.669753,-2.428996,5.679493,7.574419,1.237192,-3.013101,-8.983241,5.957118,4.208876,5.518674,-1.405282,-9.623035,0.700757,7.257365,9.101967,-9.081805,-0.888303,-5.665417,1.748238,8.755893,7.667596,-2.959003,9.522574,6.745033,8.323211,5.966565,0.416549,-4.088822,5.551749,2.169526,-4.428559,-7.048070,-7.484822,1.350085,6.420996,-8.168108,-8.426238,-6.797434,-9.086464,-3.823036,-7.768227,5.064597,-2.722940,-6.281769,4.446023,-4.681269,4.388889,-3.122889,3.735330,-2.951834,6.860602,4.522714,6.698199,3.253283,9.320566,9.388481,1.242862,7.462860,-7.808296,-6.899535,3.273302,-2.026775,0.766881,-0.865238,-0.602487,7.826834,2.636583,3.732010,-8.811366,-1.475567,8.766955,-6.939774,6.245494,-2.717628,9.340388,5.798863,2.844985,-2.395436,7.534801,2.267028,8.132354,7.709326,7.132367,4.780660,0.698965,4.846075,8.947927,1.012492,9.216503,-4.815906,-7.657761,-7.208920,1.748808,8.758129,7.544143,-4.610131,5.182559,-3.671587,2.537428,3.305322,8.061638,2.592963,-9.438192,2.740673,-7.381142,-3.162043,-4.086836,-0.942027,2.890880,-7.668390,-3.289953,3.313186,-7.908205,-1.982413,5.300631,-7.216415,-3.361944,1.994650,-4.489485,-0.086146,2.505757,-5.993006,7.839989,7.560371,-2.363394,-2.076126,4.071181,-7.418777,9.129538,5.652880,-2.868823,1.594929,1.510509,7.188620,-0.224902,-1.185689,0.070673,6.462838,8.367142,0.971163,-0.635192,-8.700751,-5.400434,5.758230,3.437826,-2.250976,-3.190535,-2.115998,9.390439,1.049552,3.652229,4.080177,-4.436836,-7.407680,2.286724,9.064001,0.288925,8.474586,9.624971,6.523739,4.959628,-2.850996,9.363705,5.344156,1.659167,-9.311329,-3.918497,4.784059,-3.553785,-8.019412,8.670283,3.994141,2.568333,-6.481333,8.172173,1.434149,-3.827975,-6.208862,-3.970939,-9.439767,0.489145,2.511782,-3.946889,-5.278735,-7.495767,-3.367055,6.727052,-8.986225,0.526693,7.941375,-7.520334,2.605809,-5.777911,-4.310335,-7.060948,-9.531334,-2.678823,7.627189,-0.874607,1.763803,2.021883,5.945191,-5.349278,6.796463,-0.817679,-2.301535,-7.855142,1.212927,-7.907258,2.408447,-4.484846,-0.056331,8.529399,8.319903,2.468139,-0.270577,8.065292,1.821432,0.286164,7.196705,0.954385,-3.564322,4.641776,2.922942,-7.391581,-4.684751,-0.047403,6.052081,0.686920,-7.743135,3.762342,7.262604,-9.332774,-0.393229,1.271877,7.171651,-1.635340,-2.327035,-9.814320,2.012270,4.670754,8.402842,-6.031356,3.956433,-7.602489,-4.140941,6.862203,-8.868301,9.321148,0.334965,-2.576176,6.898914,1.516492,-2.015351,9.687108,-5.953354,-4.718955,4.251787,-7.108293,-0.591141,-9.769878,-6.858859,-8.495475,4.302254,-6.429469,-3.181288,0.738710,2.548631,-1.337013,-4.997599,5.892505,-9.763317,5.938704,-5.982185,-4.748503,-8.019967,2.143692,-1.703022,7.468950,9.261151,6.992355,-9.962153,-6.054190,3.982284,2.107441,-1.687017,-2.039882,-6.759406,-3.716078,0.410633,8.853762,7.102318,-6.197052,-7.926405,2.254875,4.167053,-1.721466,-6.978486,2.185158,7.173835,4.087868,4.004997,-9.625976,8.576546,-9.175077,0.393236,-6.991413,4.029404,0.412909,-7.775145,5.792832,6.873951,2.863341,-2.270094,9.780091,-1.582430,-0.597411,-8.946697,0.200847,1.544278,-2.399069,-5.325143,-2.276595,7.854167,3.283468,-1.311274,-8.952981,-9.822871,6.920291,-1.616645,-3.693090,-5.792339,8.172932,7.090657,-4.441757,-9.823650,-9.963015,-6.710483,-6.916655,-7.736476,2.716781,1.707297,-3.567000,-0.973338,-2.053322,-2.320076,6.932593,0.458864,9.612166,2.568264,-2.016378,-3.208061,-0.370114,5.236951,-5.882620,3.011903,-2.789170,8.273585,-6.104361,9.929474,9.938123,-7.436004,-5.175634,1.394189,-1.558568,0.456545,-4.534098,0.176629,-4.444849,-3.822218,-7.934754,1.471791,-1.479234,9.927343,-0.787282,5.209761,-1.391296,-4.882244,-4.166014,-0.257949,-2.888989,9.876846,1.644537,-3.412905,9.341777,1.506147,-1.985909,-5.281225,4.445854,4.562872,-2.564645,7.383198,-5.666159,4.955646,3.292088,-5.252832,-2.002730,5.869590,-9.257453,5.771305,-0.204022,-1.429625,6.467896,6.583396,-7.545223,-4.321532,1.337526,-6.375240,5.796882,-9.067768,5.363048,0.877430,-6.819495,-8.724322,-9.426879,-2.530021,-2.811314,1.592907,-0.564783,-6.103572,2.822475,1.559394,0.153721,3.241279,-9.447860,0.240539,-1.326234,9.951898,3.897552,0.330989,3.921556,-1.087858,-4.190075,-5.862278,-3.384446,-2.917958,4.227969,6.444114,4.751623,-0.584888,-3.006274,3.315488,-1.444611,-7.812763,-5.651224,1.618941,9.921769,4.619322,3.527556,-2.701945,8.834846,7.070982,8.154321,3.852520,5.552600,-5.025878,2.952626,-9.290841,-6.086325,-5.778531,1.357188,-3.857174,8.394946,-9.483872,4.705050,8.883259,2.763836,-0.675107,3.718480,3.633103,0.240448,-4.511390,-0.870692,-5.918136,6.935386,8.642673,-9.859557,-6.636829,-1.550824,-7.839626,5.201837,-5.250603,-3.955778,6.909757,-3.602961,6.562622,-2.011115,-5.005389,-1.642205,5.845294,3.950036,-2.968729,8.783769,-0.128763,-4.227224,7.626049,-7.245383,-9.843615,-8.851893,-0.372265,2.685825,-1.498348,2.767855,-5.564608,4.843107,-3.095859,-5.378945,-8.377978,0.543373,6.564574,1.745947,0.216258,-4.365621,9.304856,-7.724718,3.101094,3.220074,9.705284,4.790941,-4.470200,-4.475877,3.665415,-2.498405,-9.708446,-0.042687,8.341432,-0.766604,1.721354,-3.671142,-6.794780,-4.741407,-1.376166,1.380302,5.386952,6.198982,-2.369129,-1.841019,2.899769,8.839843,-1.595073,4.332822,-4.593272,-8.429488,5.295349,-2.447016,1.581327,8.482664,-4.232310,-4.143122,4.645834,9.603340,0.588509,-6.497685,-5.868299,-4.386062,9.066464,-8.698470,3.072182,-2.921724,-6.369521,-2.522676,2.865223,5.674591,4.496734,1.891559,-8.148015,-2.883969,-2.774913,-1.877734,-0.136309,8.629788,-1.677260,5.497957,4.120888,-7.913748,-2.930360,2.493033,7.302942,2.342546,-3.061825,8.124723,-7.616023,-3.175483,-7.543886,1.754285,5.553101,6.556065,2.893041,-7.882222,-1.144475,-8.812858,3.191976,-3.561452,-5.455020,7.350777,5.197065,2.270422,-7.419355,-8.064692,-8.843036,-7.196921,7.896458,-9.551047,-4.577597,3.179234,7.780320,-5.985940,5.550250,1.656363,-1.027379,3.411736,-1.564373,6.571446,-7.396245,2.028380,-6.720505,8.626236,9.977231,-1.031134,-3.668389,-3.600723,9.036454,-5.250621,-4.221003,-6.399493,9.122104,-4.261689,2.204628,-5.207810,3.437683,-2.631387,5.045243,9.182860,2.323399,9.348607,2.178834,-5.975872,-4.105656,-9.701496,-4.684995,0.637014,-3.885888,8.927002,-9.565735,0.741444,-9.939636,8.177643,4.258406,-2.071663,-1.791700,-3.221100,-0.299534,-7.060887,-7.000456,9.203122,2.334755,-4.689582,-7.646268,2.470669,4.617873,-3.071439,0.918153,-0.454992,0.360755,1.291614,-9.937874,4.445005,-9.466080,1.085316,-3.202691,-9.804823,1.725971,2.440434,-6.537281,-9.594095,-6.082071,7.815069,-2.127759,-5.010179,2.637333,5.261121,-1.830625,-4.293750,-1.823797,2.673565,-2.775065,4.498821,-9.012635,9.735944,2.642200,-6.410974,-5.123362,1.141229,1.805449,-4.859547,-8.756641,-7.746877,3.525389,0.385003,-0.460837,-5.998245,-4.749404,9.983656,2.364947,-0.859747,-8.496114,-6.112816,-1.934343,-4.790029,7.142595,-0.673623,-2.480844,-6.446365,8.407252,-0.618281,-3.732327,-0.118654,-3.877082,2.393856,-2.569028,-8.148249,6.280722,-5.825671,8.995191,2.900898,3.478186,-1.736439,8.457633,3.668760,-1.822301,-0.576502,0.496825,-8.629374,-5.793596,2.956153,0.490427,-9.058446,-5.159047,-3.582748,0.616246,-9.484248,-7.365777,-3.712582,-9.188690,-7.196052,1.445017,6.914117,-4.952264,-9.244905,-4.486820,3.615481,-9.085058,-9.785221,-4.215339,-5.273309,-1.964698,4.512235,1.844473,-3.980669,1.514397,-0.607451,-3.971148,0.736521,4.300524,3.715727,8.994232,0.848491,-0.407602,-4.408042,0.980163,-8.533627,-4.404225,-3.863437,-0.242423,0.789825,3.297735,-2.457202,6.487725,-2.592229,-0.617737,-7.451307,1.156429,4.558213,7.572898,-6.279260,-4.697873,5.191826,-7.502375,-8.041981,-3.391762,5.518841,2.498153,4.673545,6.816912,-4.355549,-3.294186,-4.126551,-4.771904,2.876147,8.319954,-4.931494,9.265696,-6.827569,1.444138,-1.191962,-6.944765,-3.680822,4.506323,1.006942,2.974458,-4.609481,-2.285848,5.392360,-3.540820,5.439946,9.487808,1.160742,7.952862,-5.090707,-3.381178,-7.622248,-9.149652,3.700090,1.142995,8.223331,-8.656351,-1.416750,-2.435895,3.993289,-1.525742,-9.163402,8.690550,-3.668076,-2.162712,9.468417,9.885582,9.365361,-1.447760,-7.554387,5.882029,0.104002,0.458713,5.850864,6.876756,7.979088,0.850688,9.614835,6.582146,2.989280,8.624027,4.350718,-6.665566,-9.142337,4.988974,-1.949511,-9.811118,-4.616184,5.220505,0.290907,-9.321278,5.752020,5.631478,-4.249295,-0.126402,-1.618695,2.767448,9.395369,-7.730197,-7.784682,-6.848999,0.910236,-0.517037,-5.318380,0.932864,5.327203,-1.315664,1.769388,6.243649,4.668982,3.397977,1.963104,7.586097,-6.093208,0.778892,1.410998,-7.529682,-6.603472,-2.558924,-6.747310,5.053166,2.846308,-6.043522,9.473581,3.821294,-7.756574,-4.004558,2.808517,-3.656031,2.973113,-8.711789,1.616043,6.826949,-4.202550,-8.524969,2.189651,-0.996278,-2.070234,3.060828,-1.754552,-7.513941,1.904139,2.438871,-1.081858,3.779104,0.529610,-7.173097,-4.631720,-5.768355,7.940921,7.332305,-6.175258,5.264465,7.338814,-7.984701,6.509109,-2.710943,3.717233,0.218434,1.543861,-6.840596,9.714152,0.336463,-9.863306,-7.391734,-7.977629,5.056187,0.095778,6.969044,6.940794,-6.078334,-8.628690,-1.491284,-5.909407,0.902653,-6.996564,-7.783065,-4.667997,1.550353,-7.140336,-7.837541,7.169837,1.695500,3.342557,9.673005,6.543040,8.382186,-2.480191,7.550526,-1.143867,-0.395319,-6.344283,-3.517783,-6.345758,-1.325063,5.564012,-9.380833,-7.075121,7.683525,-1.467881,-4.842058,-6.854013,-7.443328,8.808543,-5.179470,-6.963024,-0.994869,1.521354,-3.776949,-9.686639,-4.102930,5.185235,7.348948,6.363318,2.527830,4.156375,8.637446,-3.475673,8.498758,9.779304,2.881955,-2.629087,0.923584,-4.078928,-3.553211,-0.429737,-5.353579,5.291210,8.670845,-2.014501,-6.690447,-6.889068,4.297488,1.117569,5.120197,-5.289076,1.187085,-1.105277,1.239673,-9.381612,-9.979233,-4.064077,-0.323610,-0.671399,-7.548183,0.196203,-2.112700,-1.879365,-3.078804,-7.904109,1.062906,-1.901695,-0.918563,1.036324,7.649035,6.857070,-9.865333,-5.875319,0.583452,-5.688043,6.684490,-5.003026,0.968493,5.290814,7.899247,9.447550,0.991580,5.381744,3.455614,5.558847,-5.070200,-6.361674,-1.576785,5.611673,0.012556,-7.057926,6.489571,-3.828257,1.563940,-9.645160,-4.919397,9.585305,7.314705,2.372709,7.986986,1.416373,6.487601,-4.368103,-9.045568,0.302204,9.348480,-2.519561,-4.646282,-1.473094,8.010574,-4.984106,-1.377916,4.628068,-4.234135,-9.296454,6.608809,7.142096,7.889887,-2.539846,-4.256783,2.922801,1.751696,-2.970466,5.584287,-5.262070,-8.855499,-5.360979,-8.490679,-0.257945,-8.055280,0.883519,4.989642,-2.452084,-4.201691,-4.098633,-8.745761,4.794876,-9.367751,2.572225,-1.262551,-3.157040,8.324145,3.375652,-9.828325,-8.899670,1.853385,-8.491867,1.023075,2.513817,4.930893,-4.374958,-6.809400,-0.087050,0.473387,-0.306575,0.945452,-6.548976,5.331009,-7.216834,-8.290075], dtype = "float64")#candidate|2107|(3360,)|const|float64
call_2106 = relay.TupleGetItem(func_697_call(relay.reshape(const_2095.astype('float64'), []), relay.reshape(const_2107.astype('float64'), [16, 15, 14]), ), 0)
call_2108 = relay.TupleGetItem(func_701_call(relay.reshape(const_2095.astype('float64'), []), relay.reshape(const_2107.astype('float64'), [16, 15, 14]), ), 0)
output = relay.Tuple([call_2055,call_2079,call_2081,call_2092,call_2094,const_2095,const_2096,var_2097,call_2106,const_2107,])
output2 = relay.Tuple([call_2056,call_2080,call_2082,call_2093,call_2098,const_2095,const_2096,var_2097,call_2108,const_2107,])
func_2109 = relay.Function([var_2097,], output)
mod['func_2109'] = func_2109
mod = relay.transform.InferType()(mod)
var_2110 = relay.var("var_2110", dtype = "float64", shape = (1568,))#candidate|2110|(1568,)|var|float64
output = func_2109(var_2110)
func_2111 = relay.Function([var_2110], output)
mutated_mod['func_2111'] = func_2111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_2113 = func_720_call()
call_2114 = func_720_call()
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_2115 = func_322_call()
call_2116 = func_322_call()
func_2109_call = mod.get_global_var('func_2109')
func_2111_call = mutated_mod.get_global_var('func_2111')
var_2130 = relay.var("var_2130", dtype = "float64", shape = (1568,))#candidate|2130|(1568,)|var|float64
call_2129 = relay.TupleGetItem(func_2109_call(relay.reshape(var_2130.astype('float64'), [1568,])), 2)
call_2131 = relay.TupleGetItem(func_2111_call(relay.reshape(var_2130.astype('float64'), [1568,])), 2)
func_1819_call = mod.get_global_var('func_1819')
func_1820_call = mutated_mod.get_global_var('func_1820')
call_2132 = relay.TupleGetItem(func_1819_call(), 0)
call_2133 = relay.TupleGetItem(func_1820_call(), 0)
func_742_call = mod.get_global_var('func_742')
func_743_call = mutated_mod.get_global_var('func_743')
call_2141 = func_742_call()
call_2142 = func_742_call()
output = relay.Tuple([call_2113,call_2115,call_2129,var_2130,call_2132,call_2141,])
output2 = relay.Tuple([call_2114,call_2116,call_2131,var_2130,call_2133,call_2142,])
func_2147 = relay.Function([var_2130,], output)
mod['func_2147'] = func_2147
mod = relay.transform.InferType()(mod)
mutated_mod['func_2147'] = func_2147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2148 = relay.var("var_2148", dtype = "float64", shape = (1568,))#candidate|2148|(1568,)|var|float64
func_2147_call = mutated_mod.get_global_var('func_2147')
call_2149 = func_2147_call(var_2148)
output = call_2149
func_2150 = relay.Function([var_2148], output)
mutated_mod['func_2150'] = func_2150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_2254 = relay.TupleGetItem(func_1401_call(), 0)
call_2255 = relay.TupleGetItem(func_1403_call(), 0)
output = relay.Tuple([call_2254,])
output2 = relay.Tuple([call_2255,])
func_2259 = relay.Function([], output)
mod['func_2259'] = func_2259
mod = relay.transform.InferType()(mod)
mutated_mod['func_2259'] = func_2259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mutated_mod.get_global_var('func_2259')
call_2260 = func_2259_call()
output = call_2260
func_2261 = relay.Function([], output)
mutated_mod['func_2261'] = func_2261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2267 = relay.var("var_2267", dtype = "float64", shape = (10, 15, 11))#candidate|2267|(10, 15, 11)|var|float64
uop_2268 = relay.atanh(var_2267.astype('float64')) # shape=(10, 15, 11)
func_1466_call = mod.get_global_var('func_1466')
func_1467_call = mutated_mod.get_global_var('func_1467')
call_2276 = relay.TupleGetItem(func_1466_call(), 0)
call_2277 = relay.TupleGetItem(func_1467_call(), 0)
output = relay.Tuple([uop_2268,call_2276,])
output2 = relay.Tuple([uop_2268,call_2277,])
func_2284 = relay.Function([var_2267,], output)
mod['func_2284'] = func_2284
mod = relay.transform.InferType()(mod)
mutated_mod['func_2284'] = func_2284
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2285 = relay.var("var_2285", dtype = "float64", shape = (10, 15, 11))#candidate|2285|(10, 15, 11)|var|float64
func_2284_call = mutated_mod.get_global_var('func_2284')
call_2286 = func_2284_call(var_2285)
output = call_2286
func_2287 = relay.Function([var_2285], output)
mutated_mod['func_2287'] = func_2287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1222_call = mod.get_global_var('func_1222')
func_1223_call = mutated_mod.get_global_var('func_1223')
call_2412 = relay.TupleGetItem(func_1222_call(), 0)
call_2413 = relay.TupleGetItem(func_1223_call(), 0)
func_2000_call = mod.get_global_var('func_2000')
func_2002_call = mutated_mod.get_global_var('func_2002')
var_2415 = relay.var("var_2415", dtype = "int8", shape = (256,))#candidate|2415|(256,)|var|int8
call_2414 = relay.TupleGetItem(func_2000_call(relay.reshape(var_2415.astype('int8'), [4, 4, 16])), 1)
call_2416 = relay.TupleGetItem(func_2002_call(relay.reshape(var_2415.astype('int8'), [4, 4, 16])), 1)
func_2109_call = mod.get_global_var('func_2109')
func_2111_call = mutated_mod.get_global_var('func_2111')
const_2448 = relay.const([-1.404417,2.307927,-8.819009,7.689585,5.245580,-3.818806,-0.714381,4.183746,4.485518,5.637140,-9.786128,0.061163,6.965771,-8.724517,-5.128894,3.596930,0.765487,5.937147,-1.431976,-7.597575,-8.184886,-8.256936,-6.943911,5.873531,5.953056,-1.740427,2.198118,-9.102178,-8.416298,1.986644,-7.371067,6.348036,8.744950,-7.378620,7.190750,8.138172,6.640008,0.933372,8.502885,5.784287,6.239601,-5.853574,4.829742,-5.329564,-3.865256,-8.084603,-4.418406,-4.066545,-7.159494,7.614063,5.831733,9.158472,-7.530644,6.015254,1.205008,-3.975626,-5.019093,2.107149,4.522906,0.898386,1.106014,4.465618,5.440031,8.203756,-5.806455,0.813253,3.189385,-1.043201,9.637875,1.026135,6.228547,-8.308684,6.566868,3.777192,4.628165,-7.188889,1.137384,-0.894375,7.261976,-3.235056,-1.493773,4.968784,2.842581,9.172296,9.088487,2.728302,-3.760051,-9.325853,-3.276507,2.101300,-6.169754,-5.379438,6.187515,-6.843358,5.861268,-3.802952,6.356985,9.952943,3.838489,1.746508,-2.297312,2.282231,-5.344223,-0.151380,-4.036538,-9.265065,5.206670,-9.138697,7.210084,6.192389,2.646209,-9.500109,6.180096,9.888494,-3.855937,-9.098185,-5.399161,-3.202791,7.997311,3.844598,-3.307240,3.246852,-3.230834,-4.957734,-6.426272,-3.198156,9.501559,-8.551281,9.374630,7.292920,8.347610,-5.649134,-8.171280,-4.726623,9.899408,7.861397,-8.781309,4.577626,-9.612926,-9.790331,2.901155,-3.786424,-1.835614,9.367412,1.913170,1.012100,-8.559992,-7.316558,-9.005443,4.128135,-7.227282,3.948576,1.890248,1.474448,-6.875707,-2.242080,7.690329,-2.469839,-0.489404,9.886289,3.441990,-3.215539,-4.579807,-7.306078,2.262204,-1.845807,-5.219351,-8.082914,-4.450161,7.484951,-5.295962,-0.807775,-8.164418,7.699218,-2.038756,-8.234993,7.356063,-4.812071,0.715711,5.515602,-4.264063,-5.841101,7.316693,-2.212956,3.076920,8.207298,3.243639,1.245172,-7.877843,-9.896423,9.689508,-9.912144,0.588208,-5.930473,3.662846,-1.968049,4.619060,-9.663484,8.337504,-1.987304,-2.023573,-3.788969,7.252133,-0.032717,-2.686599,-5.309237,4.217433,4.553390,0.708711,-7.287104,7.903033,-9.046050,3.214882,1.625549,8.020759,4.549152,8.216160,-3.722238,1.388894,0.907468,1.083393,0.741505,-7.271556,-4.108140,-4.511223,0.343892,0.034261,-3.064185,-0.763732,2.235046,6.086254,-5.099759,1.925809,6.741307,1.639929,-1.804497,2.660572,4.919148,-6.173507,8.480412,-7.531114,-1.132697,5.901757,8.259510,2.291709,3.657065,3.675923,6.340373,-7.236435,-1.089674,6.648749,8.169736,-2.813259,4.617517,-4.519114,-4.794908,8.571967,-2.183952,5.273738,-3.245876,-2.847749,-3.902145,0.687012,-3.457075,-3.527245,0.705595,-6.962362,-5.670377,-0.300004,0.916791,5.513327,9.557628,5.383960,5.885249,5.971016,0.614369,8.518231,-8.150694,5.153302,3.346052,0.186016,-1.781946,8.749014,-0.855497,-5.377465,-9.956453,8.602377,-1.591374,7.682809,-4.367589,2.257225,-2.499865,4.159767,-9.414154,-1.287376,-7.622875,-7.528342,5.616021,-0.756038,3.397634,4.711539,-9.252907,-8.875067,3.770167,-9.523071,-2.105787,2.750008,-7.128346,3.170712,-6.518538,-3.172276,9.590203,3.689769,-6.981023,8.507864,-0.070421,1.998854,3.782022,6.937435,0.397295,-4.944460,0.316501,9.347948,-2.627792,-6.580482,-1.987824,-5.475642,-4.133029,-7.714796,4.786353,-7.612943,-0.438131,-5.554648,2.709156,5.850795,9.991690,7.155313,8.184256,-6.786505,3.499742,-7.804217,-9.908461,-8.264595,-7.053686,0.358229,-6.709779,8.676776,-6.877752,-6.712091,1.521790,-0.670548,-7.151097,-7.940976,-4.292546,5.830648,2.253487,4.994832,-5.511505,-6.092210,-4.145997,-4.915598,-2.105612,-6.581462,9.104309,-0.134005,-0.249007,1.759017,-2.908094,-9.618522,3.743361,8.130323,-9.108658,-3.065416,-8.619559,4.984708,-4.096470,8.337732,-8.591186,0.758133,-1.667353,-1.737081,2.573109,2.372161,3.226870,-6.696778,-8.035182,-0.776268,7.619527,2.412764,5.837604,-8.913391,4.013911,-2.622851,7.990629,7.643275,-3.013155,-4.223619,-0.158465,6.463892,-3.487415,-3.453349,7.727262,4.398535,8.965333,-4.609477,2.959581,-9.562024,-4.180295,-4.383969,6.031290,-3.876406,-0.660855,8.974968,-5.135463,-4.349250,-5.653194,4.335352,9.938469,-9.080928,-2.576388,-6.376028,-1.854114,-3.613793,8.459317,-9.731294,-4.188466,-2.361154,-0.657576,7.167890,7.233319,0.742872,-6.577282,2.009575,1.276637,-5.746526,8.629460,9.320889,-1.316571,-5.167667,0.009942,-7.049746,6.710404,-8.315970,-7.242443,8.241467,2.619148,7.131696,6.868271,-6.134849,0.236276,-8.838775,3.933066,-8.343246,8.106927,6.300004,9.586734,8.578192,6.616534,-2.751143,7.171604,2.125658,-4.261962,2.121084,2.530367,-1.615732,-5.906698,6.803498,6.341607,5.632172,8.050410,1.055525,-9.403473,1.153523,-9.321279,2.774077,1.364421,-5.851780,-9.276921,-0.949214,5.403895,-5.745455,3.509771,5.415278,1.921218,-3.893685,-0.845446,8.220508,-7.633516,-9.559411,2.538722,-2.814447,-4.232352,-0.368091,-5.984776,-5.281053,-2.643295,-4.578555,7.281596,-4.227222,-4.653304,8.394452,-9.944489,-5.447810,4.699762,1.914900,-1.773464,-0.421417,-9.589708,9.079390,7.168270,5.631633,-6.076310,6.825563,5.997369,-5.074758,-4.718432,-1.506105,0.585245,4.938508,3.568395,4.786737,5.395943,-9.779107,-6.983724,-5.504541,-4.572514,6.496107,2.773319,-2.822082,-3.560068,3.026360,-6.058265,3.618821,-8.215503,-6.176864,3.138108,1.105218,4.526284,0.225452,-6.309949,2.577948,9.502925,6.077895,-9.931055,2.470989,9.969037,0.319649,5.528719,6.845628,-1.319519,7.822124,6.285905,-6.553146,2.772692,-2.586884,9.928215,-6.537143,8.396830,-8.308348,3.471004,-3.128042,-2.004971,-9.373702,7.798253,1.037099,2.641602,6.071487,4.624344,-3.807228,4.658784,-1.300266,-3.595118,5.433757,3.989931,5.759506,-3.246187,1.003630,-9.799297,-3.454094,9.284402,8.115972,-8.372689,0.009731,-4.053082,-4.899500,-4.960162,-6.405627,8.718279,-6.479289,2.290195,0.385715,-2.433639,-2.832117,-9.405401,-8.373092,-6.933029,6.175653,-4.054218,5.293501,-1.606985,7.803174,-5.406201,8.124950,6.626509,-8.158813,-4.479156,-6.781061,-3.973883,7.202796,6.810934,-7.561223,1.062110,6.972852,-7.004912,-8.943821,-3.956396,-5.390412,7.504822,9.601355,5.130592,-9.936494,4.227348,-4.918072,3.588263,9.756701,1.244188,7.975565,2.857846,7.905011,4.931735,-4.790813,0.715174,-5.663244,-9.028768,6.603113,-5.043847,2.897472,7.298403,1.858853,8.479575,8.267337,4.736290,9.209744,2.826474,-3.495399,-1.836495,8.017385,7.397177,2.908372,3.250251,-0.085068,-3.205342,1.897579,0.199617,-2.508695,6.179047,-2.433697,-5.078745,2.784814,-2.484175,-9.615780,-5.886647,-5.644182,-5.735648,-1.677131,-5.730981,4.000190,-3.539070,-7.004969,4.199084,7.920949,1.986748,8.925846,7.353577,4.474521,5.040800,0.392612,1.736842,7.739382,8.559391,7.916261,-5.121618,-2.811393,-7.213447,9.433316,6.390104,-6.914204,-0.400199,5.390700,9.324628,8.439172,-4.819072,-9.368402,-8.557357,1.885633,7.530463,2.992440,6.999324,3.702165,2.172237,-7.060001,7.163554,7.719938,-5.516129,3.542319,4.909783,-7.745634,1.496235,-1.136668,2.280043,8.059803,-0.105475,-6.929005,-5.660560,1.576839,-3.192616,7.852025,9.410793,6.025977,1.574256,5.102919,4.048707,-7.027468,-1.633667,-1.149601,0.029542,4.657624,6.820352,0.088306,9.360280,7.010127,-1.168233,9.349418,7.746464,-3.170594,0.373544,2.055109,8.468998,-3.178644,-1.013055,8.834612,-5.737775,-7.926180,7.102751,-3.891834,-8.384737,-3.582410,-6.811908,-6.841477,7.427832,-5.065512,-1.762587,5.758079,9.415186,-1.611470,9.030958,8.822484,-9.249598,9.094497,-3.071801,-0.510444,7.690078,2.200803,-8.795350,2.697983,-1.648082,-3.934693,9.608534,1.517885,2.580227,4.735969,8.633253,2.287944,-8.400570,0.374068,-2.034799,3.874411,7.675565,6.997930,6.067017,8.274782,-0.942710,-5.693314,8.981023,-7.667151,3.491315,3.060360,5.412557,-1.693879,1.521028,-4.226023,8.608541,7.943255,-4.535246,-5.048846,4.875270,-0.424191,-7.272805,-3.782753,-0.702106,-2.323692,-3.491285,-0.884106,-0.828503,9.265385,4.195069,1.182266,9.485630,9.442516,6.289040,9.944574,0.308745,-1.973156,5.580950,6.896881,-8.050929,2.648096,-1.634389,-7.496267,8.712181,-7.878956,8.561095,2.158840,3.695245,-1.368860,7.704029,6.462804,9.759747,-8.198402,-4.659240,-5.578340,6.047846,2.854656,-2.005752,2.940953,0.981839,-2.852217,2.946601,-6.611163,-4.083410,-1.647617,-2.690770,-6.442738,5.047361,-4.773863,-8.035858,-2.487474,3.712951,3.783953,6.112610,5.944436,9.182837,8.109508,4.291239,6.191402,0.327633,9.746909,2.607134,9.203257,-8.643021,1.308389,0.249288,5.031426,9.791929,-8.701855,3.198003,-6.639612,4.966058,4.601771,8.300102,-9.292434,-0.322784,-4.459576,3.331313,5.805431,-2.882271,-3.972824,-3.645075,-2.303445,1.055869,8.008061,-7.613013,7.583617,6.915214,-3.415800,4.851606,2.330837,3.365345,0.845100,-5.732606,-3.243302,1.052661,-2.438762,-3.181272,-4.344890,1.707971,-4.817120,1.589864,4.369714,4.648902,1.172517,-3.668983,-9.138296,-7.441530,-3.230351,-6.771378,2.321077,5.905942,-4.967670,-2.457830,7.850028,-1.742082,0.698315,8.772005,-6.211510,9.643777,8.003654,4.241794,1.909249,-5.294266,-4.270320,-8.049773,-4.254716,1.620046,-8.619243,8.986518,2.498524,2.796373,2.085453,6.885132,5.881702,0.851155,-5.418615,9.403867,2.908318,3.929490,-1.388571,2.048782,7.291445,9.481035,7.451692,-4.732670,-0.375537,1.089907,-3.751173,-7.926631,0.176140,3.680078,-6.371752,5.930003,-9.568249,3.473968,9.570515,1.411431,3.706499,-8.429950,-8.504143,7.060874,-7.820161,-1.864621,1.489898,9.114953,9.205827,-0.453500,8.624301,8.773557,-0.177841,-3.035669,9.653041,-2.600802,0.083993,8.976031,3.499790,-1.572772,-7.503104,7.022402,0.524579,-3.425251,4.496235,-4.794305,4.629590,-4.908718,-7.047034,4.209268,-5.928890,-8.372125,-7.693701,5.224781,-7.355672,0.150311,8.256152,-1.993856,5.321372,3.736743,6.933753,0.196966,9.593003,-5.968678,2.948712,7.447322,-3.912156,4.484946,-0.159880,-6.339076,-6.123168,7.246762,-0.703253,6.735846,-5.257315,-0.738731,-2.707239,-3.650209,7.196456,-5.407490,-6.432633,8.076402,9.394324,4.937957,7.207245,5.126190,-3.531740,9.730818,-1.563323,-0.776152,8.436155,5.862106,9.949916,0.439941,-9.725959,6.415611,-3.061252,4.805817,2.063475,7.710805,0.759999,-3.301779,7.938478,-0.292995,-5.090517,-0.998513,-1.916606,-4.468208,-0.941919,-4.616796,4.777779,8.817264,-1.242542,8.586504,-9.585062,5.049840,9.252365,8.514655,4.024171,3.183735,-6.928996,-2.493495,3.255329,-0.007909,-6.783345,-6.683658,-2.671792,0.067820,8.037131,-5.083672,4.225544,3.193600,-6.654566,8.299368,-2.224581,5.889959,1.384047,2.570027,-6.107482,-7.364689,7.041696,-0.778729,-1.733320,-0.738542,8.278662,4.613775,-4.554870,2.123389,7.773969,4.661242,6.853235,1.426481,-2.137317,0.271465,-8.913993,2.230528,0.146999,-7.850869,-2.657171,7.531102,2.718828,-9.395796,3.348884,-2.857818,6.801594,-9.800191,4.021560,1.470476,3.197738,-4.557504,-5.686875,7.967699,-5.487148,5.849219,-3.375936,-0.146182,-8.546565,-4.845810,-2.500238,-8.545352,-4.919335,2.176225,-4.256993,4.513099,8.758641,-5.553415,2.552445,9.945580,0.480865,-6.659703,5.790644,4.417473,-5.880522,4.418771,8.474874,-6.092665,6.363655,2.647936,-5.375280,1.110537,-6.999472,4.482449,2.955456,3.305487,8.612385,-3.451358,-0.901955,-8.430965,2.327131,-7.825960,-9.796721,-4.536481,-7.089669,0.137268,-2.668378,-3.477094,-0.323393,1.479893,1.343973,-2.575032,-4.891581,0.097122,2.249851,3.861845,-5.100715,2.483264,-3.357117,-4.427103,1.787313,5.128265,-9.622235,-1.783484,7.217654,-5.068177,6.782782,-9.279987,3.177119,-5.236658,5.611576,-9.175875,7.716068,-9.268958,5.192728,-6.982829,6.435533,1.762074,-3.252110,-3.371174,5.961096,-4.663882,-8.963445,-9.323586,-5.963009,-4.653864,2.921579,7.396154,-6.628097,-5.520899,-0.211178,-1.627265,0.148462,5.299015,2.297021,4.286240,-0.618042,2.243229,-3.835709,0.489336,3.803904,1.216479,-4.230456,4.706523,-9.146553,-1.816792,9.535259,-4.192505,-7.926192,-6.320567,-9.082576,-7.994308,7.269293,2.301924,-5.068238,-3.202070,-6.110044,-5.235903,2.089511,5.959917,7.485876,-4.447821,-2.868025,5.480067,9.076434,-0.987147,-1.201572,-5.781386,9.760453,4.347023,-3.984376,0.357192,5.150035,9.871153,1.298983,8.234414,7.842845,5.504688,-6.062187,-6.377500,-5.247401,8.650274,-7.843365,-0.588137,4.430116,4.438983,-2.679229,-5.269167,-9.582079,-2.170713,-5.105980,-9.094191,8.343602,0.678535,6.415215,2.802608,1.231411,-2.077448,6.538346,2.072623,-9.799587,-8.005288,3.220626,5.474118,1.313887,3.992322,6.415052,2.606207,-6.566213,-2.630224,-7.881866,1.279138,6.559291,8.427887,4.086069,0.972532,4.167876,-3.287476,3.009254,-1.249044,8.228714,-1.119697,-7.019197,4.462311,3.158185,-1.149179,-8.955757,5.220606,3.951779,-3.108806,9.450364,-6.016266,9.824704,0.721982,-6.901100,5.444996,4.381201,-7.013730,6.899046,-2.987891,-7.439565,7.731746,4.660169,-3.286202,9.743131,0.484242,-4.239286,-2.518641,-1.889355,-7.750388,9.909469,-6.478171,-1.740080,-9.767228,-7.463880,-1.599305,9.215995,3.269228,-6.181983,1.573906,-7.086615,-5.571352,7.049258,8.311329,-4.915333,-9.116164,6.598939,-7.540073,-5.211282,-9.280973,-6.844119,8.411382,-2.647091,-8.171722,-5.353247,-4.173151,-9.825336,2.144825,9.108318,4.132990,0.993867,-9.323825,-8.008862,-2.981645,7.645510,5.195647,3.697005,-2.564478,-0.349087,-0.321737,-9.832761,1.865494,2.351375,-6.001389,5.233008,-7.830692,-2.000639,-7.001973,7.596901,1.825185,0.990811,-1.842683,6.646062,-4.350479,8.037036,-6.208377,0.904477,-2.968085,-9.371152,-6.749171,-6.826055,-4.336590,1.688463,1.075117,0.356888,4.987787,-8.392433,2.192595,-0.953288,6.629506,-0.670241,-7.978041,8.655441,-9.878828,7.561555,-3.353622,9.094873,-4.007983,2.407961,-2.951859,-4.211914,3.882638,9.857847,-9.824199,-7.364141,-3.564521,8.071886,-9.236007,8.126436,9.332578,0.824026,6.698629,-5.622008,9.191057,2.022209,9.922232,-1.384961,-5.790156,8.167932,9.453200,-1.649825,0.250464,-8.694108,8.289169,-3.118082,3.629275,-7.583528,9.806137,-1.312375,-2.126411,-8.491877,-5.539449,-7.358411,-7.921971,8.141610,2.877218,6.496439,-6.694465,-3.824841,-6.614523,-8.439820,7.494971,-6.012007,3.046929,5.868012,-7.400307,8.370319,-6.432151,-1.568463,-4.124794,7.002607,3.652460,-8.510051,-9.595123,1.052023,8.816195,-1.484118,-4.480262,6.315287,-1.102084,3.152374,-0.492848,5.589996,-7.366771,-8.684261,2.691987,-7.294967,-1.554268,-4.465449,-4.661285,7.919480,3.839111,-9.456251,-7.509213,-1.007830,-0.796865,-3.510791,-7.275219,-9.468692,4.986958,9.046491,-6.827082,1.663692,-2.038220,1.907218,-6.972972,1.762994,2.329675,4.236916,2.997805,-8.013203,-2.105546,8.585032,-6.454703,8.322098,-4.617655,-4.091605,0.541302,0.268480,-4.190618,-5.632780,-4.788856,-1.455083,9.993251,8.390936,2.356836,-8.484333,-9.268108,3.398231,1.869473,-0.646307,8.464608,-6.050549,7.347525,6.131186,3.896139,-0.880492,4.642875,0.876844,-5.483023,4.055950,-3.387620,4.883025,2.373648,2.375400,-9.756735,-2.693867,-9.830056,-9.579393,2.509280,3.315191,3.867734,-5.614753,9.706421,0.728334,-3.013733,0.721389,-0.347913,-6.335572,7.081876,9.490137,8.354429,-8.793860,-2.993009,9.968331,-1.782011,-7.616063,-0.374899,-6.150487,-4.732025,-9.851647,-4.579632,1.936453,-7.092419,1.362798,6.178520,2.452135,-8.119363,7.111621,-1.431183,-5.191971,3.109287,-5.666002,6.598703,7.790841,-8.928520,2.805892,-7.784533,-4.617778,-2.651449,-1.092430,-2.277235,-1.585867,7.511892,5.828136,1.587064], dtype = "float64")#candidate|2448|(1568,)|const|float64
call_2447 = relay.TupleGetItem(func_2109_call(relay.reshape(const_2448.astype('float64'), [1568,])), 8)
call_2449 = relay.TupleGetItem(func_2111_call(relay.reshape(const_2448.astype('float64'), [1568,])), 8)
output = relay.Tuple([call_2412,call_2414,var_2415,call_2447,const_2448,])
output2 = relay.Tuple([call_2413,call_2416,var_2415,call_2449,const_2448,])
func_2458 = relay.Function([var_2415,], output)
mod['func_2458'] = func_2458
mod = relay.transform.InferType()(mod)
var_2459 = relay.var("var_2459", dtype = "int8", shape = (256,))#candidate|2459|(256,)|var|int8
output = func_2458(var_2459)
func_2460 = relay.Function([var_2459], output)
mutated_mod['func_2460'] = func_2460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mod.get_global_var('func_989')
func_990_call = mutated_mod.get_global_var('func_990')
call_2494 = func_989_call()
call_2495 = func_989_call()
output = relay.Tuple([call_2494,])
output2 = relay.Tuple([call_2495,])
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
func_1915_call = mod.get_global_var('func_1915')
func_1916_call = mutated_mod.get_global_var('func_1916')
call_2630 = relay.TupleGetItem(func_1915_call(), 0)
call_2631 = relay.TupleGetItem(func_1916_call(), 0)
output = call_2630
output2 = call_2631
func_2638 = relay.Function([], output)
mod['func_2638'] = func_2638
mod = relay.transform.InferType()(mod)
output = func_2638()
func_2639 = relay.Function([], output)
mutated_mod['func_2639'] = func_2639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_2661 = func_322_call()
call_2662 = func_322_call()
output = relay.Tuple([call_2661,])
output2 = relay.Tuple([call_2662,])
func_2686 = relay.Function([], output)
mod['func_2686'] = func_2686
mod = relay.transform.InferType()(mod)
output = func_2686()
func_2687 = relay.Function([], output)
mutated_mod['func_2687'] = func_2687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_482_call = mod.get_global_var('func_482')
func_484_call = mutated_mod.get_global_var('func_484')
call_2691 = relay.TupleGetItem(func_482_call(), 1)
call_2692 = relay.TupleGetItem(func_484_call(), 1)
output = relay.Tuple([call_2691,])
output2 = relay.Tuple([call_2692,])
func_2702 = relay.Function([], output)
mod['func_2702'] = func_2702
mod = relay.transform.InferType()(mod)
mutated_mod['func_2702'] = func_2702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2702_call = mutated_mod.get_global_var('func_2702')
call_2703 = func_2702_call()
output = call_2703
func_2704 = relay.Function([], output)
mutated_mod['func_2704'] = func_2704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mod.get_global_var('func_1483')
func_1485_call = mutated_mod.get_global_var('func_1485')
call_2790 = relay.TupleGetItem(func_1483_call(), 0)
call_2791 = relay.TupleGetItem(func_1485_call(), 0)
output = call_2790
output2 = call_2791
func_2792 = relay.Function([], output)
mod['func_2792'] = func_2792
mod = relay.transform.InferType()(mod)
output = func_2792()
func_2793 = relay.Function([], output)
mutated_mod['func_2793'] = func_2793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2792_call = mod.get_global_var('func_2792')
func_2793_call = mutated_mod.get_global_var('func_2793')
call_2899 = func_2792_call()
call_2900 = func_2792_call()
uop_2902 = relay.acos(call_2899.astype('float32')) # shape=(1, 2, 16)
uop_2904 = relay.acos(call_2900.astype('float32')) # shape=(1, 2, 16)
func_1815_call = mod.get_global_var('func_1815')
func_1816_call = mutated_mod.get_global_var('func_1816')
call_2905 = func_1815_call()
call_2906 = func_1815_call()
func_2497_call = mod.get_global_var('func_2497')
func_2499_call = mutated_mod.get_global_var('func_2499')
call_2916 = relay.TupleGetItem(func_2497_call(), 0)
call_2917 = relay.TupleGetItem(func_2499_call(), 0)
output = relay.Tuple([uop_2902,call_2905,call_2916,])
output2 = relay.Tuple([uop_2904,call_2906,call_2917,])
func_2924 = relay.Function([], output)
mod['func_2924'] = func_2924
mod = relay.transform.InferType()(mod)
mutated_mod['func_2924'] = func_2924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2924_call = mutated_mod.get_global_var('func_2924')
call_2925 = func_2924_call()
output = call_2925
func_2926 = relay.Function([], output)
mutated_mod['func_2926'] = func_2926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2792_call = mod.get_global_var('func_2792')
func_2793_call = mutated_mod.get_global_var('func_2793')
call_2997 = func_2792_call()
call_2998 = func_2792_call()
output = relay.Tuple([call_2997,])
output2 = relay.Tuple([call_2998,])
func_3003 = relay.Function([], output)
mod['func_3003'] = func_3003
mod = relay.transform.InferType()(mod)
mutated_mod['func_3003'] = func_3003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3003_call = mutated_mod.get_global_var('func_3003')
call_3004 = func_3003_call()
output = call_3004
func_3005 = relay.Function([], output)
mutated_mod['func_3005'] = func_3005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1545_call = mod.get_global_var('func_1545')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_3021 = relay.TupleGetItem(func_1545_call(), 0)
call_3022 = relay.TupleGetItem(func_1546_call(), 0)
func_742_call = mod.get_global_var('func_742')
func_743_call = mutated_mod.get_global_var('func_743')
call_3023 = func_742_call()
call_3024 = func_742_call()
var_3028 = relay.var("var_3028", dtype = "int8", shape = (4, 4, 16))#candidate|3028|(4, 4, 16)|var|int8
bop_3029 = relay.greater(call_3023.astype('bool'), relay.reshape(var_3028.astype('bool'), relay.shape_of(call_3023))) # shape=(4, 4, 16)
bop_3032 = relay.greater(call_3024.astype('bool'), relay.reshape(var_3028.astype('bool'), relay.shape_of(call_3024))) # shape=(4, 4, 16)
output = relay.Tuple([call_3021,bop_3029,])
output2 = relay.Tuple([call_3022,bop_3032,])
func_3033 = relay.Function([var_3028,], output)
mod['func_3033'] = func_3033
mod = relay.transform.InferType()(mod)
var_3034 = relay.var("var_3034", dtype = "int8", shape = (4, 4, 16))#candidate|3034|(4, 4, 16)|var|int8
output = func_3033(var_3034)
func_3035 = relay.Function([var_3034], output)
mutated_mod['func_3035'] = func_3035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_3037 = func_322_call()
call_3038 = func_322_call()
var_3041 = relay.var("var_3041", dtype = "float64", shape = (2, 2, 14))#candidate|3041|(2, 2, 14)|var|float64
bop_3042 = relay.mod(call_3037.astype('float32'), relay.reshape(var_3041.astype('float32'), relay.shape_of(call_3037))) # shape=(2, 2, 14)
bop_3045 = relay.mod(call_3038.astype('float32'), relay.reshape(var_3041.astype('float32'), relay.shape_of(call_3038))) # shape=(2, 2, 14)
output = relay.Tuple([bop_3042,])
output2 = relay.Tuple([bop_3045,])
func_3051 = relay.Function([var_3041,], output)
mod['func_3051'] = func_3051
mod = relay.transform.InferType()(mod)
mutated_mod['func_3051'] = func_3051
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3052 = relay.var("var_3052", dtype = "float64", shape = (2, 2, 14))#candidate|3052|(2, 2, 14)|var|float64
func_3051_call = mutated_mod.get_global_var('func_3051')
call_3053 = func_3051_call(var_3052)
output = call_3053
func_3054 = relay.Function([var_3052], output)
mutated_mod['func_3054'] = func_3054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mod.get_global_var('func_2259')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_3107 = relay.TupleGetItem(func_2259_call(), 0)
call_3108 = relay.TupleGetItem(func_2261_call(), 0)
output = relay.Tuple([call_3107,])
output2 = relay.Tuple([call_3108,])
func_3120 = relay.Function([], output)
mod['func_3120'] = func_3120
mod = relay.transform.InferType()(mod)
output = func_3120()
func_3121 = relay.Function([], output)
mutated_mod['func_3121'] = func_3121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1819_call = mod.get_global_var('func_1819')
func_1820_call = mutated_mod.get_global_var('func_1820')
call_3174 = relay.TupleGetItem(func_1819_call(), 0)
call_3175 = relay.TupleGetItem(func_1820_call(), 0)
func_2497_call = mod.get_global_var('func_2497')
func_2499_call = mutated_mod.get_global_var('func_2499')
call_3209 = relay.TupleGetItem(func_2497_call(), 0)
call_3210 = relay.TupleGetItem(func_2499_call(), 0)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_3223 = func_720_call()
call_3224 = func_720_call()
output = relay.Tuple([call_3174,call_3209,call_3223,])
output2 = relay.Tuple([call_3175,call_3210,call_3224,])
func_3262 = relay.Function([], output)
mod['func_3262'] = func_3262
mod = relay.transform.InferType()(mod)
output = func_3262()
func_3263 = relay.Function([], output)
mutated_mod['func_3263'] = func_3263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mod.get_global_var('func_1483')
func_1485_call = mutated_mod.get_global_var('func_1485')
call_3300 = relay.TupleGetItem(func_1483_call(), 1)
call_3301 = relay.TupleGetItem(func_1485_call(), 1)
output = relay.Tuple([call_3300,])
output2 = relay.Tuple([call_3301,])
func_3324 = relay.Function([], output)
mod['func_3324'] = func_3324
mod = relay.transform.InferType()(mod)
output = func_3324()
func_3325 = relay.Function([], output)
mutated_mod['func_3325'] = func_3325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mod.get_global_var('func_2259')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_3344 = relay.TupleGetItem(func_2259_call(), 0)
call_3345 = relay.TupleGetItem(func_2261_call(), 0)
output = call_3344
output2 = call_3345
func_3358 = relay.Function([], output)
mod['func_3358'] = func_3358
mod = relay.transform.InferType()(mod)
mutated_mod['func_3358'] = func_3358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3358_call = mutated_mod.get_global_var('func_3358')
call_3359 = func_3358_call()
output = call_3359
func_3360 = relay.Function([], output)
mutated_mod['func_3360'] = func_3360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_3361 = relay.TupleGetItem(func_1401_call(), 1)
call_3362 = relay.TupleGetItem(func_1403_call(), 1)
func_2259_call = mod.get_global_var('func_2259')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_3371 = relay.TupleGetItem(func_2259_call(), 0)
call_3372 = relay.TupleGetItem(func_2261_call(), 0)
uop_3391 = relay.acos(call_3361.astype('float64')) # shape=(4, 4, 16)
uop_3393 = relay.acos(call_3362.astype('float64')) # shape=(4, 4, 16)
output = relay.Tuple([call_3371,uop_3391,])
output2 = relay.Tuple([call_3372,uop_3393,])
func_3395 = relay.Function([], output)
mod['func_3395'] = func_3395
mod = relay.transform.InferType()(mod)
mutated_mod['func_3395'] = func_3395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3395_call = mutated_mod.get_global_var('func_3395')
call_3396 = func_3395_call()
output = call_3396
func_3397 = relay.Function([], output)
mutated_mod['func_3397'] = func_3397
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3456 = relay.var("var_3456", dtype = "uint8", shape = ())#candidate|3456|()|var|uint8
const_3457 = relay.const([[[1,9,2,5,-1,-10,-1,8,7,1,3],[-2,7,8,-10,-5,4,3,8,-3,2,8],[10,-5,10,-2,9,-3,-9,-8,7,2,-9],[-9,-4,-8,6,2,-9,-4,-2,3,-2,10],[9,-2,1,-8,-8,-9,-1,-3,-2,4,-1],[-2,7,-4,4,-2,-2,-1,-8,-3,-8,-1],[9,6,6,-3,-10,-9,2,8,9,-1,6],[-6,-1,-9,3,-7,-3,-4,-3,-7,5,10],[1,-5,7,3,-10,-8,-8,-1,8,-5,-1],[9,7,-6,1,-10,-3,-3,3,-4,5,-5],[8,5,-5,6,-9,-7,8,-9,-9,-1,5],[3,-10,-2,-10,1,4,5,-8,3,-3,-6],[-6,-1,-5,9,6,8,10,2,-7,-9,1],[-10,4,-6,8,9,-8,-2,3,-3,-3,7],[-2,-3,-4,-2,8,-3,9,-9,-3,2,-9],[4,-4,-10,-9,2,6,2,10,4,-6,-10]],[[8,2,8,-3,-8,8,6,-1,-5,-8,-10],[2,2,10,2,-5,-9,-2,-2,-3,-5,-4],[-3,8,10,10,6,-2,7,-10,-1,-9,-3],[7,-9,-6,3,5,-5,-5,-9,-6,6,-5],[1,-2,-10,3,6,-9,-10,7,-2,-1,-5],[5,1,1,1,-10,3,7,5,-9,9,5],[-10,7,7,3,6,8,-9,-5,-8,7,9],[9,3,6,-5,-5,7,8,-10,8,9,3],[6,2,-5,7,2,-9,-3,9,7,-4,-4],[8,5,1,-3,-6,2,-5,7,-10,-10,-4],[-3,-3,-4,7,-9,-3,-3,10,9,-5,4],[-8,5,-9,-7,10,-5,4,-9,-1,-8,-5],[-1,8,-3,-2,6,9,8,-6,5,6,-8],[1,-1,-6,-9,3,9,9,-6,-10,-1,-4],[1,3,-6,5,-9,-9,-1,3,-9,-9,8],[10,-8,-8,1,9,2,7,-3,1,-9,4]],[[9,-9,4,9,-7,-7,1,-6,-9,-4,7],[10,4,-3,4,-4,-7,-3,4,-4,-1,5],[-8,4,-4,-8,-2,2,-2,10,4,-10,10],[1,-5,2,-6,8,8,1,4,6,10,1],[-2,-9,-6,7,-2,7,-5,-3,-6,7,5],[-7,-9,-5,10,2,-7,-10,8,9,8,-7],[-5,-6,-3,6,-2,9,7,-10,-1,10,-1],[-1,8,1,5,8,10,2,8,-3,4,-2],[7,-9,6,6,-10,8,-8,3,-7,-3,7],[-2,5,5,-9,-2,1,-5,-1,-4,-10,10],[-1,1,-5,7,-2,-9,4,10,-1,10,-2],[-6,-7,-5,-3,5,7,4,-2,6,-7,5],[-8,-5,-5,-2,-1,1,9,7,10,-7,-7],[9,-1,-7,9,-2,-7,6,1,1,6,-9],[10,10,7,-7,10,6,-10,-2,5,5,-10],[-3,9,-2,-8,4,7,7,3,10,9,-7]],[[-1,7,-4,5,3,4,2,1,-8,-9,10],[9,-2,-7,5,2,-4,1,1,-3,-5,-8],[-4,8,-5,5,3,-7,4,-7,-1,-6,-8],[-4,-2,7,3,-6,-6,6,-1,5,6,-10],[9,1,6,4,2,-5,4,-4,7,5,-2],[5,4,9,3,2,7,-1,-9,-7,2,7],[-5,-4,-9,-8,-9,-6,4,-5,-3,10,-10],[-2,-5,-2,-2,2,2,-2,2,-1,4,6],[-3,4,7,7,-2,-10,8,3,-3,-7,-10],[5,10,4,5,9,-8,5,6,7,-9,-4],[-9,8,1,-8,-6,-2,-8,10,4,-1,-2],[-10,-6,-8,-3,3,9,-7,-7,-1,7,9],[2,9,1,-10,8,-3,8,1,-4,-5,-8],[-5,-7,-9,-2,10,-10,-9,10,-5,-1,3],[10,1,2,8,10,4,2,10,2,7,8],[2,-7,-6,-5,-8,-7,-8,-6,-9,-10,2]],[[4,5,1,-9,-9,-8,-6,-5,-5,6,1],[-3,10,3,-2,-1,10,-4,7,-1,4,3],[6,-3,-10,-5,2,-9,-7,-4,9,7,1],[-2,5,-5,3,-1,7,-1,10,9,3,8],[-10,1,8,-1,-1,7,4,-7,3,7,-9],[-8,-4,4,-7,-7,5,-8,-10,-1,-10,9],[4,5,5,9,10,-4,6,-2,-10,-10,9],[-7,-5,-1,7,-2,-7,8,1,-3,-7,-3],[-7,-4,6,-2,-1,5,5,4,-4,-5,-5],[3,2,-5,5,2,5,-10,1,5,1,10],[5,-10,-10,10,-9,9,10,-2,6,-6,-3],[1,8,-6,5,7,-7,9,-3,5,3,-7],[10,8,5,-6,-2,-2,2,-1,3,-8,-4],[-10,-9,1,8,5,-9,-3,-8,-3,-5,-3],[3,5,4,6,2,7,10,-3,5,-8,2],[-9,2,3,6,-6,1,-3,-7,-3,5,-10]],[[7,3,3,8,-5,-6,-8,-4,-6,-1,4],[-10,-5,1,2,-4,9,2,-1,7,-5,10],[-3,-8,-7,-4,7,3,8,9,-9,10,2],[-10,-2,6,-2,-3,-3,6,1,2,-5,-9],[2,6,3,-1,-7,8,10,7,2,-10,10],[-6,5,1,4,-4,8,-10,-5,-5,-2,2],[-7,-7,-6,4,1,8,-8,6,7,-10,2],[-5,1,-1,-1,8,-9,-6,9,10,-8,6],[7,7,3,-8,-7,4,-1,2,6,-1,-2],[10,5,-1,-10,8,-8,1,10,10,2,-7],[9,-6,-7,1,-4,-3,5,-1,-9,-2,1],[2,-5,-1,6,-2,7,-1,-7,-6,-3,7],[2,-3,-6,-10,2,-10,-4,-8,9,3,-9],[2,7,6,-6,-10,-2,9,-1,5,-1,-2],[6,-5,-1,-2,-5,8,-2,-3,-9,5,7],[-1,5,4,9,-10,8,-1,-4,-1,7,10]],[[-4,-8,-6,-8,8,-5,-3,8,-7,-8,-6],[3,-4,-8,4,10,2,4,-10,-5,10,-9],[7,9,-8,8,-8,3,-7,-2,-2,8,-8],[-4,-5,-7,6,-9,5,-8,5,-6,-9,2],[1,-5,-6,-5,-5,3,7,-4,5,-6,1],[3,10,-6,8,4,-4,10,-4,-4,-5,9],[-6,3,-8,2,-4,3,4,-4,-1,-10,9],[-7,-5,2,-6,10,-5,3,-5,-3,10,7],[-7,-4,1,-5,4,-3,-3,-8,5,-2,4],[-4,-10,10,-2,6,9,-2,-4,3,9,6],[1,2,4,6,9,7,-8,-1,-3,2,7],[-4,-10,-8,3,2,7,-9,8,-7,7,6],[10,-6,6,-6,-1,-3,-7,10,4,1,-6],[2,-6,-10,-4,10,6,6,-3,3,3,5],[-7,-8,-6,2,-1,-7,3,2,4,1,8],[-9,2,-5,8,-6,4,5,5,6,-2,-3]],[[-10,2,8,1,-3,-9,2,1,-5,-4,1],[2,7,-1,1,-3,2,-3,1,8,-4,-10],[-2,-6,-7,7,10,-5,-7,5,4,-9,3],[7,-7,9,-4,8,9,-5,2,6,3,-8],[-8,2,-1,8,-4,10,-2,3,-8,-1,4],[-3,2,-10,-1,-7,3,2,-10,-10,7,-8],[-8,2,3,-3,1,-5,5,8,-6,-6,-6],[-3,-1,3,-2,5,-3,4,-2,2,2,6],[1,-5,1,-7,2,-3,2,10,-8,-4,4],[4,-4,7,2,-3,-9,1,2,7,8,8],[8,6,5,-5,-7,-4,7,-8,7,5,2],[6,-6,7,-4,5,-4,-6,-10,-9,1,-1],[7,9,-1,-1,-10,4,-1,9,-9,-5,-7],[4,-3,-6,8,-5,7,10,8,-8,8,4],[6,-3,10,-9,-3,4,-8,2,-10,-3,-3],[-4,2,-9,5,-10,-9,-7,4,-5,1,-3]],[[-2,6,-2,-8,2,5,-5,6,2,-2,-10],[-9,6,-9,5,-5,5,-8,2,3,9,10],[6,3,-2,6,-5,6,3,6,7,5,-5],[-10,-1,3,-3,-4,-10,7,-4,-6,10,-8],[-9,-10,-8,-8,-8,-1,5,8,8,-7,9],[-4,6,1,4,-10,-6,9,5,-6,-8,-9],[3,-1,9,3,3,-2,7,-9,-3,-6,-9],[-2,2,7,-4,-5,2,-10,-7,1,-10,10],[-6,-10,10,-7,-9,-3,-6,-3,7,-9,-5],[1,4,1,-3,-1,2,8,-5,10,6,7],[6,-4,9,3,4,7,6,-2,-10,7,-6],[3,2,7,1,-1,5,1,1,-1,5,-5],[-3,9,-3,5,-5,-9,6,-6,2,-3,3],[3,7,10,-10,-5,5,-8,2,6,-6,4],[-2,8,-10,-3,4,-8,9,-2,-5,6,3],[-6,9,-2,-8,-6,1,-4,-4,3,-2,8]],[[-8,-4,9,1,-4,-7,-1,-10,7,9,10],[8,-10,-2,9,6,10,10,-10,1,10,-8],[9,9,-6,6,2,9,-3,8,9,-1,6],[2,2,9,-3,4,9,-8,2,10,-7,9],[10,-4,-3,-1,6,-2,-7,4,-2,-2,2],[7,-5,1,5,-2,7,-5,-2,-9,10,-9],[-4,6,1,-8,-9,8,-3,-6,9,5,-5],[-6,7,-7,9,-5,-1,1,-1,7,-6,-6],[4,-7,-9,10,-3,2,4,-8,-7,5,3],[2,-7,-6,5,-1,-1,5,3,7,-2,7],[-10,6,-7,7,-7,6,1,-8,-1,9,-9],[5,8,9,10,-5,-10,-10,-1,7,-10,-5],[-4,-9,-4,-8,-3,-7,4,10,-2,4,5],[1,3,-8,-2,3,-6,10,1,4,-10,4],[7,-7,10,-2,-7,4,2,4,5,-7,-2],[-10,4,8,7,7,-7,-4,6,-3,-1,-5]],[[-7,7,6,2,3,-10,7,3,1,7,-4],[4,-9,5,4,-4,-10,-4,9,4,-9,2],[-2,8,-5,-1,6,-3,4,6,9,-10,5],[5,9,7,-4,2,4,-1,-6,9,10,8],[9,2,6,-7,6,-6,-9,-3,-1,-1,6],[3,-4,4,4,8,6,1,1,-4,10,-10],[-2,-4,-9,-8,-6,-4,3,6,10,1,3],[-9,-10,9,-2,10,3,8,8,-6,-7,7],[-10,9,7,7,2,4,10,3,-4,7,9],[-9,1,3,8,10,-5,8,-9,-1,5,-6],[-9,-7,3,2,9,-1,9,-8,4,-2,7],[2,-9,8,10,-6,-4,-4,7,1,7,6],[-5,-2,-2,-9,-6,-6,4,6,-9,-3,-5],[2,-2,10,6,-7,2,-10,-4,5,10,3],[-5,-7,1,-9,-8,-2,7,-2,-10,2,8],[8,10,2,-3,3,-3,-4,2,-3,-6,3]],[[-9,-4,3,2,-9,3,-2,-9,-9,-6,-5],[-9,4,9,8,-5,6,5,7,-1,8,6],[-1,8,9,4,-2,1,8,-10,-10,3,-4],[5,8,10,2,-7,-2,4,-6,-3,5,8],[6,8,-3,-3,-3,-10,6,8,-5,2,-9],[9,7,8,8,5,-4,-9,6,-5,10,-2],[5,-4,-7,8,-5,3,-10,5,-5,-1,3],[-7,2,10,5,-8,-3,1,-1,6,-7,-9],[8,-7,4,3,8,6,9,-5,9,-7,8],[-2,8,-4,-7,-5,6,-7,8,6,9,9],[2,-4,-7,-5,8,3,-7,4,9,8,-9],[-4,6,-6,-3,-5,-9,8,-10,1,2,6],[1,5,7,-3,-8,-7,6,1,8,-8,7],[-3,1,-4,7,4,8,-8,-1,-5,-8,7],[-4,7,6,-9,1,9,5,5,-3,-10,6],[-10,-10,10,-5,-4,-5,1,8,6,9,1]],[[3,5,-5,-9,-4,-10,1,-4,4,5,1],[-3,-3,8,8,-7,-7,7,1,3,-2,-2],[10,9,-4,-5,10,5,9,-9,-5,8,-1],[2,-10,7,-7,-6,5,-10,2,3,5,7],[-3,3,-3,10,7,-3,-8,-2,9,9,-5],[-2,-6,1,5,5,4,-6,10,-8,9,-5],[-4,-9,5,7,-8,-9,4,-6,-7,6,1],[-8,-9,10,-2,4,-2,-8,-4,-8,-2,9],[-6,4,5,7,-4,-7,-3,-3,-1,-10,-2],[1,1,-8,-8,-10,3,-8,-8,6,-9,-6],[-9,-9,6,5,-8,-3,8,4,2,8,2],[4,2,1,-3,6,-4,2,4,9,4,1],[-5,5,2,3,-1,3,4,-7,-1,-9,-5],[6,-8,1,6,5,-8,-1,6,-4,8,2],[-1,1,9,-6,10,-8,-6,-2,1,-4,-10],[3,8,4,-7,9,5,-10,1,3,-8,2]]], dtype = "uint8")#candidate|3457|(13, 16, 11)|const|uint8
bop_3458 = relay.bitwise_and(var_3456.astype('uint8'), const_3457.astype('uint8')) # shape=(13, 16, 11)
func_1843_call = mod.get_global_var('func_1843')
func_1844_call = mutated_mod.get_global_var('func_1844')
call_3471 = func_1843_call()
call_3472 = func_1843_call()
uop_3475 = relay.rsqrt(bop_3458.astype('float32')) # shape=(13, 16, 11)
output = relay.Tuple([call_3471,uop_3475,])
output2 = relay.Tuple([call_3472,uop_3475,])
func_3483 = relay.Function([var_3456,], output)
mod['func_3483'] = func_3483
mod = relay.transform.InferType()(mod)
mutated_mod['func_3483'] = func_3483
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3484 = relay.var("var_3484", dtype = "uint8", shape = ())#candidate|3484|()|var|uint8
func_3483_call = mutated_mod.get_global_var('func_3483')
call_3485 = func_3483_call(var_3484)
output = call_3485
func_3486 = relay.Function([var_3484], output)
mutated_mod['func_3486'] = func_3486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3488 = relay.var("var_3488", dtype = "float32", shape = ())#candidate|3488|()|var|float32
const_3489 = relay.const([[[-0.875809,9.200896],[5.706290,4.131125],[-1.339475,8.480309],[4.183989,0.865534]],[[-6.227179,-9.605871],[2.279388,0.082886],[-1.135371,2.177976],[-4.807690,0.522078]],[[4.070249,0.870425],[5.598828,0.666852],[7.255938,8.612558],[6.625580,-8.389187]],[[-9.368524,3.396806],[3.148964,3.334215],[6.975206,-1.732639],[6.570243,-2.248691]]], dtype = "float32")#candidate|3489|(4, 4, 2)|const|float32
bop_3490 = relay.greater_equal(var_3488.astype('bool'), const_3489.astype('bool')) # shape=(4, 4, 2)
uop_3493 = relay.sin(const_3489.astype('float32')) # shape=(4, 4, 2)
output = relay.Tuple([bop_3490,uop_3493,])
output2 = relay.Tuple([bop_3490,uop_3493,])
func_3504 = relay.Function([var_3488,], output)
mod['func_3504'] = func_3504
mod = relay.transform.InferType()(mod)
mutated_mod['func_3504'] = func_3504
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3505 = relay.var("var_3505", dtype = "float32", shape = ())#candidate|3505|()|var|float32
func_3504_call = mutated_mod.get_global_var('func_3504')
call_3506 = func_3504_call(var_3505)
output = call_3506
func_3507 = relay.Function([var_3505], output)
mutated_mod['func_3507'] = func_3507
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3559 = relay.var("var_3559", dtype = "float32", shape = (4, 5, 8))#candidate|3559|(4, 5, 8)|var|float32
uop_3560 = relay.sinh(var_3559.astype('float32')) # shape=(4, 5, 8)
func_2000_call = mod.get_global_var('func_2000')
func_2002_call = mutated_mod.get_global_var('func_2002')
const_3565 = relay.const([10,8,-1,-1,-1,-7,-9,4,4,-10,-7,2,-10,-4,2,4,5,2,-3,10,-8,-2,8,1,-2,-2,2,2,-5,-6,-4,-9,-2,-4,-3,-8,-3,-10,-10,4,-3,-10,-4,-7,-1,-4,-5,3,-3,4,-3,-9,-7,-1,1,9,-2,1,3,3,-2,8,-1,7,-10,-9,5,3,-10,-9,10,7,8,7,5,-7,8,-4,-8,4,4,-5,3,3,4,6,-9,-5,-8,-2,4,-2,7,-3,9,-7,1,3,1,9,7,1,-8,-7,-9,-1,-10,-7,-1,4,-8,-4,-2,-6,5,10,1,-10,-8,-7,-5,1,-3,2,9,-5,-6,7,-10,-5,-8,-6,8,10,-2,4,7,-3,-4,-6,1,-1,4,9,2,-10,-10,-1,-2,-4,-10,-10,-6,1,7,4,-3,-7,6,3,-7,-8,7,5,2,4,10,3,8,-5,-1,3,5,-1,3,6,-6,8,6,5,-3,-4,-4,8,-10,4,-1,7,4,-6,1,8,-8,1,10,-4,4,7,-4,9,-9,7,-10,5,-2,1,-4,-3,5,-6,9,-7,9,-2,-10,-9,3,-8,-10,-7,5,8,-8,10,2,-8,8,-7,-1,2,-1,8,-6,-9,1,-9,-5,-6,5,-6,-3,-1,10,-8,8,-10,-10,4,-9,10,-10,-6,5,8,7,-8], dtype = "int8")#candidate|3565|(256,)|const|int8
call_3564 = relay.TupleGetItem(func_2000_call(relay.reshape(const_3565.astype('int8'), [4, 4, 16])), 0)
call_3566 = relay.TupleGetItem(func_2002_call(relay.reshape(const_3565.astype('int8'), [4, 4, 16])), 0)
output = relay.Tuple([uop_3560,call_3564,const_3565,])
output2 = relay.Tuple([uop_3560,call_3566,const_3565,])
func_3570 = relay.Function([var_3559,], output)
mod['func_3570'] = func_3570
mod = relay.transform.InferType()(mod)
mutated_mod['func_3570'] = func_3570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3571 = relay.var("var_3571", dtype = "float32", shape = (4, 5, 8))#candidate|3571|(4, 5, 8)|var|float32
func_3570_call = mutated_mod.get_global_var('func_3570')
call_3572 = func_3570_call(var_3571)
output = call_3572
func_3573 = relay.Function([var_3571], output)
mutated_mod['func_3573'] = func_3573
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3597 = relay.var("var_3597", dtype = "float64", shape = (15, 5, 9))#candidate|3597|(15, 5, 9)|var|float64
uop_3598 = relay.atanh(var_3597.astype('float64')) # shape=(15, 5, 9)
uop_3605 = relay.sigmoid(var_3597.astype('float32')) # shape=(15, 5, 9)
output = relay.Tuple([uop_3598,uop_3605,])
output2 = relay.Tuple([uop_3598,uop_3605,])
func_3611 = relay.Function([var_3597,], output)
mod['func_3611'] = func_3611
mod = relay.transform.InferType()(mod)
mutated_mod['func_3611'] = func_3611
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3612 = relay.var("var_3612", dtype = "float64", shape = (15, 5, 9))#candidate|3612|(15, 5, 9)|var|float64
func_3611_call = mutated_mod.get_global_var('func_3611')
call_3613 = func_3611_call(var_3612)
output = call_3613
func_3614 = relay.Function([var_3612], output)
mutated_mod['func_3614'] = func_3614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_284_call = mod.get_global_var('func_284')
func_286_call = mutated_mod.get_global_var('func_286')
call_3616 = relay.TupleGetItem(func_284_call(), 0)
call_3617 = relay.TupleGetItem(func_286_call(), 0)
output = relay.Tuple([call_3616,])
output2 = relay.Tuple([call_3617,])
func_3620 = relay.Function([], output)
mod['func_3620'] = func_3620
mod = relay.transform.InferType()(mod)
output = func_3620()
func_3621 = relay.Function([], output)
mutated_mod['func_3621'] = func_3621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_3637 = relay.TupleGetItem(func_1611_call(), 0)
call_3638 = relay.TupleGetItem(func_1613_call(), 0)
uop_3656 = relay.rsqrt(call_3637.astype('float64')) # shape=(1, 2, 16)
uop_3658 = relay.rsqrt(call_3638.astype('float64')) # shape=(1, 2, 16)
var_3684 = relay.var("var_3684", dtype = "float64", shape = (16, 2, 16))#candidate|3684|(16, 2, 16)|var|float64
bop_3685 = relay.maximum(uop_3656.astype('int16'), var_3684.astype('int16')) # shape=(16, 2, 16)
bop_3688 = relay.maximum(uop_3658.astype('int16'), var_3684.astype('int16')) # shape=(16, 2, 16)
func_3395_call = mod.get_global_var('func_3395')
func_3397_call = mutated_mod.get_global_var('func_3397')
call_3700 = relay.TupleGetItem(func_3395_call(), 0)
call_3701 = relay.TupleGetItem(func_3397_call(), 0)
bop_3710 = relay.maximum(uop_3656.astype('int8'), relay.reshape(call_3637.astype('int8'), relay.shape_of(uop_3656))) # shape=(1, 2, 16)
bop_3713 = relay.maximum(uop_3658.astype('int8'), relay.reshape(call_3638.astype('int8'), relay.shape_of(uop_3658))) # shape=(1, 2, 16)
bop_3719 = relay.multiply(bop_3685.astype('float64'), bop_3710.astype('float64')) # shape=(16, 2, 16)
bop_3722 = relay.multiply(bop_3688.astype('float64'), bop_3713.astype('float64')) # shape=(16, 2, 16)
uop_3723 = relay.tan(bop_3685.astype('float32')) # shape=(16, 2, 16)
uop_3725 = relay.tan(bop_3688.astype('float32')) # shape=(16, 2, 16)
output = relay.Tuple([call_3700,bop_3719,uop_3723,])
output2 = relay.Tuple([call_3701,bop_3722,uop_3725,])
func_3732 = relay.Function([var_3684,], output)
mod['func_3732'] = func_3732
mod = relay.transform.InferType()(mod)
var_3733 = relay.var("var_3733", dtype = "float64", shape = (16, 2, 16))#candidate|3733|(16, 2, 16)|var|float64
output = func_3732(var_3733)
func_3734 = relay.Function([var_3733], output)
mutated_mod['func_3734'] = func_3734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2638_call = mod.get_global_var('func_2638')
func_2639_call = mutated_mod.get_global_var('func_2639')
call_3738 = func_2638_call()
call_3739 = func_2638_call()
func_1915_call = mod.get_global_var('func_1915')
func_1916_call = mutated_mod.get_global_var('func_1916')
call_3745 = relay.TupleGetItem(func_1915_call(), 0)
call_3746 = relay.TupleGetItem(func_1916_call(), 0)
func_3003_call = mod.get_global_var('func_3003')
func_3005_call = mutated_mod.get_global_var('func_3005')
call_3777 = relay.TupleGetItem(func_3003_call(), 0)
call_3778 = relay.TupleGetItem(func_3005_call(), 0)
uop_3794 = relay.acosh(call_3777.astype('float64')) # shape=(1, 2, 16)
uop_3796 = relay.acosh(call_3778.astype('float64')) # shape=(1, 2, 16)
output = relay.Tuple([call_3738,call_3745,uop_3794,])
output2 = relay.Tuple([call_3739,call_3746,uop_3796,])
func_3798 = relay.Function([], output)
mod['func_3798'] = func_3798
mod = relay.transform.InferType()(mod)
mutated_mod['func_3798'] = func_3798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3798_call = mutated_mod.get_global_var('func_3798')
call_3799 = func_3798_call()
output = call_3799
func_3800 = relay.Function([], output)
mutated_mod['func_3800'] = func_3800
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3825 = relay.var("var_3825", dtype = "float64", shape = (12, 10, 13))#candidate|3825|(12, 10, 13)|var|float64
uop_3826 = relay.sigmoid(var_3825.astype('float64')) # shape=(12, 10, 13)
uop_3828 = relay.atanh(uop_3826.astype('float64')) # shape=(12, 10, 13)
func_2702_call = mod.get_global_var('func_2702')
func_2704_call = mutated_mod.get_global_var('func_2704')
call_3837 = relay.TupleGetItem(func_2702_call(), 0)
call_3838 = relay.TupleGetItem(func_2704_call(), 0)
bop_3872 = relay.logical_or(uop_3828.astype('bool'), relay.reshape(uop_3826.astype('bool'), relay.shape_of(uop_3828))) # shape=(12, 10, 13)
var_3879 = relay.var("var_3879", dtype = "float64", shape = (2, 2, 14))#candidate|3879|(2, 2, 14)|var|float64
bop_3880 = relay.add(call_3837.astype('float64'), relay.reshape(var_3879.astype('float64'), relay.shape_of(call_3837))) # shape=(2, 2, 14)
bop_3883 = relay.add(call_3838.astype('float64'), relay.reshape(var_3879.astype('float64'), relay.shape_of(call_3838))) # shape=(2, 2, 14)
func_2109_call = mod.get_global_var('func_2109')
func_2111_call = mutated_mod.get_global_var('func_2111')
var_3895 = relay.var("var_3895", dtype = "float64", shape = (1568,))#candidate|3895|(1568,)|var|float64
call_3894 = relay.TupleGetItem(func_2109_call(relay.reshape(var_3895.astype('float64'), [1568,])), 2)
call_3896 = relay.TupleGetItem(func_2111_call(relay.reshape(var_3895.astype('float64'), [1568,])), 2)
output = relay.Tuple([bop_3872,bop_3880,call_3894,var_3895,])
output2 = relay.Tuple([bop_3872,bop_3883,call_3896,var_3895,])
func_3897 = relay.Function([var_3825,var_3879,var_3895,], output)
mod['func_3897'] = func_3897
mod = relay.transform.InferType()(mod)
mutated_mod['func_3897'] = func_3897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3897_call = mutated_mod.get_global_var('func_3897')
var_3899 = relay.var("var_3899", dtype = "float64", shape = (12, 10, 13))#candidate|3899|(12, 10, 13)|var|float64
var_3900 = relay.var("var_3900", dtype = "float64", shape = (2, 2, 14))#candidate|3900|(2, 2, 14)|var|float64
var_3901 = relay.var("var_3901", dtype = "float64", shape = (1568,))#candidate|3901|(1568,)|var|float64
call_3898 = func_3897_call(var_3899,var_3900,var_3901,)
output = call_3898
func_3902 = relay.Function([var_3899,var_3900,var_3901,], output)
mutated_mod['func_3902'] = func_3902
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3909 = relay.const([[[4,-9,6,-9,4,9,-2,3,-6,2,4,7,5,1,-7,-2],[-5,-6,-2,7,-8,7,-7,-1,-3,-6,10,-1,7,1,-4,-5],[-3,-9,-7,-2,-5,6,-7,-6,-1,-1,6,-3,1,7,6,-4],[4,-3,-2,-9,-2,-10,1,3,-8,2,-6,7,9,-3,-7,-4],[-2,5,2,2,6,-4,8,8,4,8,-6,-7,8,-2,9,-7],[2,7,-3,-7,1,-5,-3,-2,4,6,6,5,-5,8,-2,7],[4,-8,-4,-7,10,-3,6,7,7,10,-7,7,3,-8,-10,-8],[10,3,-3,-1,2,-4,-1,-8,6,-2,-6,-5,-4,-5,7,-9],[1,10,-2,-9,-7,5,-5,4,3,-4,-5,-10,-1,1,8,4],[-6,5,7,4,-8,10,2,-5,-2,-7,-8,-5,-2,5,-10,1]],[[-5,-4,2,-6,5,-4,-2,5,9,-10,-7,-6,-3,2,3,-7],[-2,9,-9,6,1,-2,-2,6,6,-8,2,3,8,9,1,-10],[-7,8,-3,9,-6,-8,7,-10,9,8,-6,7,8,-5,-9,1],[3,-1,4,2,-2,-8,4,2,8,5,10,-5,-5,7,-5,-2],[-6,7,-5,-1,1,6,7,-1,5,-6,7,5,-6,-7,-9,-9],[6,-6,-7,9,-6,5,2,-10,-1,4,-2,1,-1,8,1,-8],[5,9,-1,-2,-3,4,-3,2,3,-4,-7,2,5,-2,7,-3],[-2,-4,9,3,3,7,2,-1,-7,9,-2,-4,10,3,-5,-10],[9,1,-10,-9,-4,10,-6,-2,-10,9,-3,-10,8,-10,10,-10],[-4,6,-9,-10,3,-8,4,2,-2,-5,3,-8,9,-5,-8,9]],[[-8,-7,-1,-8,8,3,-8,4,-7,7,-2,-2,2,9,2,1],[2,7,-6,10,-2,4,10,-2,-6,-9,-3,-1,-10,-5,8,-2],[-4,8,3,4,10,7,-5,-1,7,1,-2,-5,3,-5,-5,-5],[-8,-1,-8,-8,2,-2,-6,9,-2,-5,3,7,9,-8,2,3],[4,-1,-8,5,-6,-8,10,10,-10,-6,-7,8,8,-10,9,8],[-9,10,-8,9,1,-8,7,-3,-3,9,-4,5,4,10,-1,1],[-7,-9,-5,9,-6,-7,5,7,8,5,4,4,7,3,10,8],[-4,-2,-3,-5,10,-1,1,-10,-5,-3,-6,9,8,-1,-8,8],[6,-9,3,-10,-5,7,-3,6,-3,-1,5,4,3,-4,6,1],[3,5,-5,10,-7,7,-5,10,-2,-9,-10,-10,2,-4,-7,-2]]], dtype = "int16")#candidate|3909|(3, 10, 16)|const|int16
var_3910 = relay.var("var_3910", dtype = "int16", shape = (3, 10, 16))#candidate|3910|(3, 10, 16)|var|int16
bop_3911 = relay.add(const_3909.astype('int16'), relay.reshape(var_3910.astype('int16'), relay.shape_of(const_3909))) # shape=(3, 10, 16)
output = relay.Tuple([bop_3911,])
output2 = relay.Tuple([bop_3911,])
func_3923 = relay.Function([var_3910,], output)
mod['func_3923'] = func_3923
mod = relay.transform.InferType()(mod)
mutated_mod['func_3923'] = func_3923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3924 = relay.var("var_3924", dtype = "int16", shape = (3, 10, 16))#candidate|3924|(3, 10, 16)|var|int16
func_3923_call = mutated_mod.get_global_var('func_3923')
call_3925 = func_3923_call(var_3924)
output = call_3925
func_3926 = relay.Function([var_3924], output)
mutated_mod['func_3926'] = func_3926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mod.get_global_var('func_2259')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_3933 = relay.TupleGetItem(func_2259_call(), 0)
call_3934 = relay.TupleGetItem(func_2261_call(), 0)
output = call_3933
output2 = call_3934
func_3936 = relay.Function([], output)
mod['func_3936'] = func_3936
mod = relay.transform.InferType()(mod)
output = func_3936()
func_3937 = relay.Function([], output)
mutated_mod['func_3937'] = func_3937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2924_call = mod.get_global_var('func_2924')
func_2926_call = mutated_mod.get_global_var('func_2926')
call_3940 = relay.TupleGetItem(func_2924_call(), 0)
call_3941 = relay.TupleGetItem(func_2926_call(), 0)
var_3953 = relay.var("var_3953", dtype = "float32", shape = (3, 2, 16))#candidate|3953|(3, 2, 16)|var|float32
bop_3954 = relay.logical_or(call_3940.astype('bool'), var_3953.astype('bool')) # shape=(3, 2, 16)
bop_3957 = relay.logical_or(call_3941.astype('bool'), var_3953.astype('bool')) # shape=(3, 2, 16)
output = relay.Tuple([bop_3954,])
output2 = relay.Tuple([bop_3957,])
func_3969 = relay.Function([var_3953,], output)
mod['func_3969'] = func_3969
mod = relay.transform.InferType()(mod)
mutated_mod['func_3969'] = func_3969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3970 = relay.var("var_3970", dtype = "float32", shape = (3, 2, 16))#candidate|3970|(3, 2, 16)|var|float32
func_3969_call = mutated_mod.get_global_var('func_3969')
call_3971 = func_3969_call(var_3970)
output = call_3971
func_3972 = relay.Function([var_3970], output)
mutated_mod['func_3972'] = func_3972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3620_call = mod.get_global_var('func_3620')
func_3621_call = mutated_mod.get_global_var('func_3621')
call_3985 = relay.TupleGetItem(func_3620_call(), 0)
call_3986 = relay.TupleGetItem(func_3621_call(), 0)
func_3798_call = mod.get_global_var('func_3798')
func_3800_call = mutated_mod.get_global_var('func_3800')
call_4010 = relay.TupleGetItem(func_3798_call(), 0)
call_4011 = relay.TupleGetItem(func_3800_call(), 0)
output = relay.Tuple([call_3985,call_4010,])
output2 = relay.Tuple([call_3986,call_4011,])
func_4013 = relay.Function([], output)
mod['func_4013'] = func_4013
mod = relay.transform.InferType()(mod)
mutated_mod['func_4013'] = func_4013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4013_call = mutated_mod.get_global_var('func_4013')
call_4014 = func_4013_call()
output = call_4014
func_4015 = relay.Function([], output)
mutated_mod['func_4015'] = func_4015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3120_call = mod.get_global_var('func_3120')
func_3121_call = mutated_mod.get_global_var('func_3121')
call_4031 = relay.TupleGetItem(func_3120_call(), 0)
call_4032 = relay.TupleGetItem(func_3121_call(), 0)
output = relay.Tuple([call_4031,])
output2 = relay.Tuple([call_4032,])
func_4062 = relay.Function([], output)
mod['func_4062'] = func_4062
mod = relay.transform.InferType()(mod)
output = func_4062()
func_4063 = relay.Function([], output)
mutated_mod['func_4063'] = func_4063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1466_call = mod.get_global_var('func_1466')
func_1467_call = mutated_mod.get_global_var('func_1467')
call_4118 = relay.TupleGetItem(func_1466_call(), 0)
call_4119 = relay.TupleGetItem(func_1467_call(), 0)
uop_4128 = relay.tan(call_4118.astype('float32')) # shape=(2, 2, 14)
uop_4130 = relay.tan(call_4119.astype('float32')) # shape=(2, 2, 14)
output = relay.Tuple([uop_4128,])
output2 = relay.Tuple([uop_4130,])
func_4149 = relay.Function([], output)
mod['func_4149'] = func_4149
mod = relay.transform.InferType()(mod)
mutated_mod['func_4149'] = func_4149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mutated_mod.get_global_var('func_4149')
call_4150 = func_4149_call()
output = call_4150
func_4151 = relay.Function([], output)
mutated_mod['func_4151'] = func_4151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_4208 = relay.TupleGetItem(func_1401_call(), 1)
call_4209 = relay.TupleGetItem(func_1403_call(), 1)
output = call_4208
output2 = call_4209
func_4223 = relay.Function([], output)
mod['func_4223'] = func_4223
mod = relay.transform.InferType()(mod)
output = func_4223()
func_4224 = relay.Function([], output)
mutated_mod['func_4224'] = func_4224
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4251 = relay.var("var_4251", dtype = "float32", shape = (3, 13, 2))#candidate|4251|(3, 13, 2)|var|float32
var_4252 = relay.var("var_4252", dtype = "float32", shape = (3, 13, 2))#candidate|4252|(3, 13, 2)|var|float32
bop_4253 = relay.floor_divide(var_4251.astype('float32'), relay.reshape(var_4252.astype('float32'), relay.shape_of(var_4251))) # shape=(3, 13, 2)
func_3120_call = mod.get_global_var('func_3120')
func_3121_call = mutated_mod.get_global_var('func_3121')
call_4256 = relay.TupleGetItem(func_3120_call(), 0)
call_4257 = relay.TupleGetItem(func_3121_call(), 0)
output = relay.Tuple([bop_4253,call_4256,])
output2 = relay.Tuple([bop_4253,call_4257,])
func_4280 = relay.Function([var_4251,var_4252,], output)
mod['func_4280'] = func_4280
mod = relay.transform.InferType()(mod)
mutated_mod['func_4280'] = func_4280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mutated_mod.get_global_var('func_4280')
var_4282 = relay.var("var_4282", dtype = "float32", shape = (3, 13, 2))#candidate|4282|(3, 13, 2)|var|float32
var_4283 = relay.var("var_4283", dtype = "float32", shape = (3, 13, 2))#candidate|4283|(3, 13, 2)|var|float32
call_4281 = func_4280_call(var_4282,var_4283,)
output = call_4281
func_4284 = relay.Function([var_4282,var_4283,], output)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1222_call = mod.get_global_var('func_1222')
func_1223_call = mutated_mod.get_global_var('func_1223')
call_4296 = relay.TupleGetItem(func_1222_call(), 0)
call_4297 = relay.TupleGetItem(func_1223_call(), 0)
uop_4298 = relay.log2(call_4296.astype('float32')) # shape=(2, 2, 14)
uop_4300 = relay.log2(call_4297.astype('float32')) # shape=(2, 2, 14)
output = relay.Tuple([uop_4298,])
output2 = relay.Tuple([uop_4300,])
func_4317 = relay.Function([], output)
mod['func_4317'] = func_4317
mod = relay.transform.InferType()(mod)
mutated_mod['func_4317'] = func_4317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4317_call = mutated_mod.get_global_var('func_4317')
call_4318 = func_4317_call()
output = call_4318
func_4319 = relay.Function([], output)
mutated_mod['func_4319'] = func_4319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2924_call = mod.get_global_var('func_2924')
func_2926_call = mutated_mod.get_global_var('func_2926')
call_4398 = relay.TupleGetItem(func_2924_call(), 2)
call_4399 = relay.TupleGetItem(func_2926_call(), 2)
var_4421 = relay.var("var_4421", dtype = "float64", shape = (4, 4, 16))#candidate|4421|(4, 4, 16)|var|float64
bop_4422 = relay.floor_mod(call_4398.astype('float64'), relay.reshape(var_4421.astype('float64'), relay.shape_of(call_4398))) # shape=(4, 4, 16)
bop_4425 = relay.floor_mod(call_4399.astype('float64'), relay.reshape(var_4421.astype('float64'), relay.shape_of(call_4399))) # shape=(4, 4, 16)
func_4223_call = mod.get_global_var('func_4223')
func_4224_call = mutated_mod.get_global_var('func_4224')
call_4427 = func_4223_call()
call_4428 = func_4223_call()
output = relay.Tuple([bop_4422,call_4427,])
output2 = relay.Tuple([bop_4425,call_4428,])
func_4429 = relay.Function([var_4421,], output)
mod['func_4429'] = func_4429
mod = relay.transform.InferType()(mod)
var_4430 = relay.var("var_4430", dtype = "float64", shape = (4, 4, 16))#candidate|4430|(4, 4, 16)|var|float64
output = func_4429(var_4430)
func_4431 = relay.Function([var_4430], output)
mutated_mod['func_4431'] = func_4431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_4468 = relay.TupleGetItem(func_312_call(), 0)
call_4469 = relay.TupleGetItem(func_313_call(), 0)
func_794_call = mod.get_global_var('func_794')
func_796_call = mutated_mod.get_global_var('func_796')
var_4479 = relay.var("var_4479", dtype = "float64", shape = (32,))#candidate|4479|(32,)|var|float64
call_4478 = relay.TupleGetItem(func_794_call(relay.reshape(var_4479.astype('float64'), [32,])), 3)
call_4480 = relay.TupleGetItem(func_796_call(relay.reshape(var_4479.astype('float64'), [32,])), 3)
var_4481 = relay.var("var_4481", dtype = "float64", shape = (32,))#candidate|4481|(32,)|var|float64
bop_4482 = relay.greater_equal(call_4478.astype('bool'), relay.reshape(var_4481.astype('bool'), relay.shape_of(call_4478))) # shape=(32,)
bop_4485 = relay.greater_equal(call_4480.astype('bool'), relay.reshape(var_4481.astype('bool'), relay.shape_of(call_4480))) # shape=(32,)
uop_4495 = relay.cos(var_4479.astype('float64')) # shape=(32,)
output = relay.Tuple([call_4468,bop_4482,uop_4495,])
output2 = relay.Tuple([call_4469,bop_4485,uop_4495,])
func_4502 = relay.Function([var_4479,var_4481,], output)
mod['func_4502'] = func_4502
mod = relay.transform.InferType()(mod)
mutated_mod['func_4502'] = func_4502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4502_call = mutated_mod.get_global_var('func_4502')
var_4504 = relay.var("var_4504", dtype = "float64", shape = (32,))#candidate|4504|(32,)|var|float64
var_4505 = relay.var("var_4505", dtype = "float64", shape = (32,))#candidate|4505|(32,)|var|float64
call_4503 = func_4502_call(var_4504,var_4505,)
output = call_4503
func_4506 = relay.Function([var_4504,var_4505,], output)
mutated_mod['func_4506'] = func_4506
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4539 = relay.var("var_4539", dtype = "float32", shape = (16, 1, 13))#candidate|4539|(16, 1, 13)|var|float32
var_4540 = relay.var("var_4540", dtype = "float32", shape = (16, 3, 13))#candidate|4540|(16, 3, 13)|var|float32
bop_4541 = relay.power(var_4539.astype('float32'), var_4540.astype('float32')) # shape=(16, 3, 13)
func_3969_call = mod.get_global_var('func_3969')
func_3972_call = mutated_mod.get_global_var('func_3972')
const_4545 = relay.const([[-2.492745],[1.742778],[8.739990],[0.636018],[5.266634],[7.487312],[-7.210617],[-2.378915],[-5.294935],[3.228725],[-5.295114],[-2.630205],[6.027562],[-0.611579],[-6.486567],[7.077619],[2.100486],[0.607533],[-3.845558],[6.910321],[4.557997],[3.523238],[8.550048],[2.681660],[-0.511062],[8.701776],[7.360660],[-4.311298],[3.617052],[8.615110],[3.274389],[-3.661963],[1.869217],[8.550708],[-5.441055],[1.863735],[-4.811248],[-6.290396],[-8.217374],[5.892694],[-5.224228],[-4.558330],[-5.673813],[-1.238442],[9.898946],[6.248091],[-4.143158],[8.784501],[-0.272273],[2.779755],[9.641055],[-5.916517],[-2.626991],[-9.408193],[1.542778],[5.460680],[-5.631420],[8.443350],[-3.739221],[-3.618754],[1.054458],[2.047354],[0.603363],[-0.619726],[3.669137],[1.197962],[-8.258939],[-3.073415],[-8.989780],[-0.885482],[2.723700],[7.905195],[2.925798],[-8.929618],[8.051317],[9.866602],[3.100132],[-2.880988],[9.286316],[-5.748532],[1.905552],[1.326594],[8.422774],[-1.708371],[-5.583935],[0.685593],[-7.483946],[4.288686],[-5.663663],[8.380309],[-9.332990],[-9.998769],[6.550271],[0.867038],[5.031282],[-5.228868]], dtype = "float32")#candidate|4545|(96, 1)|const|float32
call_4544 = relay.TupleGetItem(func_3969_call(relay.reshape(const_4545.astype('float32'), [3, 2, 16])), 0)
call_4546 = relay.TupleGetItem(func_3972_call(relay.reshape(const_4545.astype('float32'), [3, 2, 16])), 0)
bop_4547 = relay.right_shift(bop_4541.astype('int32'), var_4539.astype('int32')) # shape=(16, 3, 13)
func_3003_call = mod.get_global_var('func_3003')
func_3005_call = mutated_mod.get_global_var('func_3005')
call_4552 = relay.TupleGetItem(func_3003_call(), 0)
call_4553 = relay.TupleGetItem(func_3005_call(), 0)
output = relay.Tuple([call_4544,const_4545,bop_4547,call_4552,])
output2 = relay.Tuple([call_4546,const_4545,bop_4547,call_4553,])
func_4558 = relay.Function([var_4539,var_4540,], output)
mod['func_4558'] = func_4558
mod = relay.transform.InferType()(mod)
mutated_mod['func_4558'] = func_4558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4558_call = mutated_mod.get_global_var('func_4558')
var_4560 = relay.var("var_4560", dtype = "float32", shape = (16, 1, 13))#candidate|4560|(16, 1, 13)|var|float32
var_4561 = relay.var("var_4561", dtype = "float32", shape = (16, 3, 13))#candidate|4561|(16, 3, 13)|var|float32
call_4559 = func_4558_call(var_4560,var_4561,)
output = call_4559
func_4562 = relay.Function([var_4560,var_4561,], output)
mutated_mod['func_4562'] = func_4562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_4567 = relay.TupleGetItem(func_1611_call(), 0)
call_4568 = relay.TupleGetItem(func_1613_call(), 0)
const_4582 = relay.const([[[True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True],[False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True]],[[True,False,False,False,True,True,False,False,False,True,False,False,True,True,True,True],[True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False]],[[False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True],[False,True,True,True,False,False,False,True,False,False,False,False,True,True,False,True]],[[False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True],[False,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True]],[[True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False],[True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False]],[[False,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True],[False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True]],[[True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False],[True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True]],[[True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True],[True,False,True,True,True,True,False,True,False,False,False,True,True,False,False,False]],[[False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True],[False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True]],[[False,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True],[True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True]]], dtype = "bool")#candidate|4582|(10, 2, 16)|const|bool
bop_4583 = relay.less_equal(call_4567.astype('bool'), const_4582.astype('bool')) # shape=(10, 2, 16)
bop_4586 = relay.less_equal(call_4568.astype('bool'), const_4582.astype('bool')) # shape=(10, 2, 16)
output = bop_4583
output2 = bop_4586
func_4595 = relay.Function([], output)
mod['func_4595'] = func_4595
mod = relay.transform.InferType()(mod)
mutated_mod['func_4595'] = func_4595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4595_call = mutated_mod.get_global_var('func_4595')
call_4596 = func_4595_call()
output = call_4596
func_4597 = relay.Function([], output)
mutated_mod['func_4597'] = func_4597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2792_call = mod.get_global_var('func_2792')
func_2793_call = mutated_mod.get_global_var('func_2793')
call_4609 = func_2792_call()
call_4610 = func_2792_call()
func_3570_call = mod.get_global_var('func_3570')
func_3573_call = mutated_mod.get_global_var('func_3573')
var_4624 = relay.var("var_4624", dtype = "float32", shape = (160,))#candidate|4624|(160,)|var|float32
call_4623 = relay.TupleGetItem(func_3570_call(relay.reshape(var_4624.astype('float32'), [4, 5, 8])), 2)
call_4625 = relay.TupleGetItem(func_3573_call(relay.reshape(var_4624.astype('float32'), [4, 5, 8])), 2)
func_4429_call = mod.get_global_var('func_4429')
func_4431_call = mutated_mod.get_global_var('func_4431')
call_4670 = relay.TupleGetItem(func_4429_call(relay.reshape(call_4623.astype('float64'), [4, 4, 16])), 1)
call_4671 = relay.TupleGetItem(func_4431_call(relay.reshape(call_4623.astype('float64'), [4, 4, 16])), 1)
output = relay.Tuple([call_4609,call_4623,var_4624,call_4670,])
output2 = relay.Tuple([call_4610,call_4625,var_4624,call_4671,])
func_4679 = relay.Function([var_4624,], output)
mod['func_4679'] = func_4679
mod = relay.transform.InferType()(mod)
var_4680 = relay.var("var_4680", dtype = "float32", shape = (160,))#candidate|4680|(160,)|var|float32
output = func_4679(var_4680)
func_4681 = relay.Function([var_4680], output)
mutated_mod['func_4681'] = func_4681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2702_call = mod.get_global_var('func_2702')
func_2704_call = mutated_mod.get_global_var('func_2704')
call_4691 = relay.TupleGetItem(func_2702_call(), 0)
call_4692 = relay.TupleGetItem(func_2704_call(), 0)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_4703 = relay.TupleGetItem(func_1170_call(), 1)
call_4704 = relay.TupleGetItem(func_1172_call(), 1)
output = relay.Tuple([call_4691,call_4703,])
output2 = relay.Tuple([call_4692,call_4704,])
func_4705 = relay.Function([], output)
mod['func_4705'] = func_4705
mod = relay.transform.InferType()(mod)
mutated_mod['func_4705'] = func_4705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4705_call = mutated_mod.get_global_var('func_4705')
call_4706 = func_4705_call()
output = call_4706
func_4707 = relay.Function([], output)
mutated_mod['func_4707'] = func_4707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mod.get_global_var('func_4149')
func_4151_call = mutated_mod.get_global_var('func_4151')
call_4799 = relay.TupleGetItem(func_4149_call(), 0)
call_4800 = relay.TupleGetItem(func_4151_call(), 0)
func_1680_call = mod.get_global_var('func_1680')
func_1683_call = mutated_mod.get_global_var('func_1683')
var_4802 = relay.var("var_4802", dtype = "float64", shape = (1568,))#candidate|4802|(1568,)|var|float64
call_4801 = relay.TupleGetItem(func_1680_call(relay.reshape(var_4802.astype('float64'), [1568,])), 2)
call_4803 = relay.TupleGetItem(func_1683_call(relay.reshape(var_4802.astype('float64'), [1568,])), 2)
func_4502_call = mod.get_global_var('func_4502')
func_4506_call = mutated_mod.get_global_var('func_4506')
var_4805 = relay.var("var_4805", dtype = "float64", shape = (8, 4))#candidate|4805|(8, 4)|var|float64
call_4804 = relay.TupleGetItem(func_4502_call(relay.reshape(var_4805.astype('float64'), [32,]), relay.reshape(var_4805.astype('float64'), [32,]), ), 2)
call_4806 = relay.TupleGetItem(func_4506_call(relay.reshape(var_4805.astype('float64'), [32,]), relay.reshape(var_4805.astype('float64'), [32,]), ), 2)
func_794_call = mod.get_global_var('func_794')
func_796_call = mutated_mod.get_global_var('func_796')
call_4809 = relay.TupleGetItem(func_794_call(relay.reshape(var_4805.astype('float64'), [32,])), 2)
call_4810 = relay.TupleGetItem(func_796_call(relay.reshape(var_4805.astype('float64'), [32,])), 2)
output = relay.Tuple([call_4799,call_4801,var_4802,call_4804,var_4805,call_4809,])
output2 = relay.Tuple([call_4800,call_4803,var_4802,call_4806,var_4805,call_4810,])
func_4816 = relay.Function([var_4802,var_4805,], output)
mod['func_4816'] = func_4816
mod = relay.transform.InferType()(mod)
mutated_mod['func_4816'] = func_4816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4816_call = mutated_mod.get_global_var('func_4816')
var_4818 = relay.var("var_4818", dtype = "float64", shape = (1568,))#candidate|4818|(1568,)|var|float64
var_4819 = relay.var("var_4819", dtype = "float64", shape = (8, 4))#candidate|4819|(8, 4)|var|float64
call_4817 = func_4816_call(var_4818,var_4819,)
output = call_4817
func_4820 = relay.Function([var_4818,var_4819,], output)
mutated_mod['func_4820'] = func_4820
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4830 = relay.var("var_4830", dtype = "int64", shape = (8, 9, 7))#candidate|4830|(8, 9, 7)|var|int64
var_4831 = relay.var("var_4831", dtype = "int64", shape = (8, 9, 7))#candidate|4831|(8, 9, 7)|var|int64
bop_4832 = relay.minimum(var_4830.astype('int64'), relay.reshape(var_4831.astype('int64'), relay.shape_of(var_4830))) # shape=(8, 9, 7)
uop_4846 = relay.asinh(var_4830.astype('float64')) # shape=(8, 9, 7)
bop_4851 = relay.greater(bop_4832.astype('bool'), relay.reshape(var_4830.astype('bool'), relay.shape_of(bop_4832))) # shape=(8, 9, 7)
output = relay.Tuple([uop_4846,bop_4851,])
output2 = relay.Tuple([uop_4846,bop_4851,])
func_4859 = relay.Function([var_4830,var_4831,], output)
mod['func_4859'] = func_4859
mod = relay.transform.InferType()(mod)
mutated_mod['func_4859'] = func_4859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4859_call = mutated_mod.get_global_var('func_4859')
var_4861 = relay.var("var_4861", dtype = "int64", shape = (8, 9, 7))#candidate|4861|(8, 9, 7)|var|int64
var_4862 = relay.var("var_4862", dtype = "int64", shape = (8, 9, 7))#candidate|4862|(8, 9, 7)|var|int64
call_4860 = func_4859_call(var_4861,var_4862,)
output = call_4860
func_4863 = relay.Function([var_4861,var_4862,], output)
mutated_mod['func_4863'] = func_4863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mod.get_global_var('func_1483')
func_1485_call = mutated_mod.get_global_var('func_1485')
call_4910 = relay.TupleGetItem(func_1483_call(), 0)
call_4911 = relay.TupleGetItem(func_1485_call(), 0)
output = call_4910
output2 = call_4911
func_4917 = relay.Function([], output)
mod['func_4917'] = func_4917
mod = relay.transform.InferType()(mod)
output = func_4917()
func_4918 = relay.Function([], output)
mutated_mod['func_4918'] = func_4918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1895_call = mod.get_global_var('func_1895')
func_1896_call = mutated_mod.get_global_var('func_1896')
call_5009 = relay.TupleGetItem(func_1895_call(), 0)
call_5010 = relay.TupleGetItem(func_1896_call(), 0)
var_5011 = relay.var("var_5011", dtype = "float32", shape = (9, 10, 10))#candidate|5011|(9, 10, 10)|var|float32
bop_5012 = relay.maximum(call_5009.astype('float32'), var_5011.astype('float32')) # shape=(9, 10, 10)
bop_5015 = relay.maximum(call_5010.astype('float32'), var_5011.astype('float32')) # shape=(9, 10, 10)
func_4223_call = mod.get_global_var('func_4223')
func_4224_call = mutated_mod.get_global_var('func_4224')
call_5016 = func_4223_call()
call_5017 = func_4223_call()
output = relay.Tuple([bop_5012,call_5016,])
output2 = relay.Tuple([bop_5015,call_5017,])
func_5018 = relay.Function([var_5011,], output)
mod['func_5018'] = func_5018
mod = relay.transform.InferType()(mod)
var_5019 = relay.var("var_5019", dtype = "float32", shape = (9, 10, 10))#candidate|5019|(9, 10, 10)|var|float32
output = func_5018(var_5019)
func_5020 = relay.Function([var_5019], output)
mutated_mod['func_5020'] = func_5020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1792_call = mod.get_global_var('func_1792')
func_1794_call = mutated_mod.get_global_var('func_1794')
call_5031 = relay.TupleGetItem(func_1792_call(), 0)
call_5032 = relay.TupleGetItem(func_1794_call(), 0)
output = relay.Tuple([call_5031,])
output2 = relay.Tuple([call_5032,])
func_5033 = relay.Function([], output)
mod['func_5033'] = func_5033
mod = relay.transform.InferType()(mod)
output = func_5033()
func_5034 = relay.Function([], output)
mutated_mod['func_5034'] = func_5034
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5116 = relay.const(9, dtype = "int64")#candidate|5116|()|const|int64
var_5117 = relay.var("var_5117", dtype = "int64", shape = (6, 7, 12))#candidate|5117|(6, 7, 12)|var|int64
bop_5118 = relay.greater_equal(const_5116.astype('bool'), var_5117.astype('bool')) # shape=(6, 7, 12)
output = bop_5118
output2 = bop_5118
func_5122 = relay.Function([var_5117,], output)
mod['func_5122'] = func_5122
mod = relay.transform.InferType()(mod)
mutated_mod['func_5122'] = func_5122
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5123 = relay.var("var_5123", dtype = "int64", shape = (6, 7, 12))#candidate|5123|(6, 7, 12)|var|int64
func_5122_call = mutated_mod.get_global_var('func_5122')
call_5124 = func_5122_call(var_5123)
output = call_5124
func_5125 = relay.Function([var_5123], output)
mutated_mod['func_5125'] = func_5125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1843_call = mod.get_global_var('func_1843')
func_1844_call = mutated_mod.get_global_var('func_1844')
call_5142 = func_1843_call()
call_5143 = func_1843_call()
output = call_5142
output2 = call_5143
func_5147 = relay.Function([], output)
mod['func_5147'] = func_5147
mod = relay.transform.InferType()(mod)
mutated_mod['func_5147'] = func_5147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5147_call = mutated_mod.get_global_var('func_5147')
call_5148 = func_5147_call()
output = call_5148
func_5149 = relay.Function([], output)
mutated_mod['func_5149'] = func_5149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2702_call = mod.get_global_var('func_2702')
func_2704_call = mutated_mod.get_global_var('func_2704')
call_5308 = relay.TupleGetItem(func_2702_call(), 0)
call_5309 = relay.TupleGetItem(func_2704_call(), 0)
output = relay.Tuple([call_5308,])
output2 = relay.Tuple([call_5309,])
func_5332 = relay.Function([], output)
mod['func_5332'] = func_5332
mod = relay.transform.InferType()(mod)
output = func_5332()
func_5333 = relay.Function([], output)
mutated_mod['func_5333'] = func_5333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_5336 = relay.TupleGetItem(func_1170_call(), 0)
call_5337 = relay.TupleGetItem(func_1172_call(), 0)
var_5370 = relay.var("var_5370", dtype = "int8", shape = (4, 4, 16))#candidate|5370|(4, 4, 16)|var|int8
bop_5371 = relay.multiply(call_5336.astype('int16'), relay.reshape(var_5370.astype('int16'), relay.shape_of(call_5336))) # shape=(4, 4, 16)
bop_5374 = relay.multiply(call_5337.astype('int16'), relay.reshape(var_5370.astype('int16'), relay.shape_of(call_5337))) # shape=(4, 4, 16)
func_3033_call = mod.get_global_var('func_3033')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_5383 = relay.TupleGetItem(func_3033_call(relay.reshape(call_5336.astype('int8'), [4, 4, 16])), 1)
call_5384 = relay.TupleGetItem(func_3035_call(relay.reshape(call_5336.astype('int8'), [4, 4, 16])), 1)
output = relay.Tuple([bop_5371,call_5383,])
output2 = relay.Tuple([bop_5374,call_5384,])
func_5386 = relay.Function([var_5370,], output)
mod['func_5386'] = func_5386
mod = relay.transform.InferType()(mod)
mutated_mod['func_5386'] = func_5386
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5387 = relay.var("var_5387", dtype = "int8", shape = (4, 4, 16))#candidate|5387|(4, 4, 16)|var|int8
func_5386_call = mutated_mod.get_global_var('func_5386')
call_5388 = func_5386_call(var_5387)
output = call_5388
func_5389 = relay.Function([var_5387], output)
mutated_mod['func_5389'] = func_5389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2924_call = mod.get_global_var('func_2924')
func_2926_call = mutated_mod.get_global_var('func_2926')
call_5423 = relay.TupleGetItem(func_2924_call(), 1)
call_5424 = relay.TupleGetItem(func_2926_call(), 1)
output = call_5423
output2 = call_5424
func_5429 = relay.Function([], output)
mod['func_5429'] = func_5429
mod = relay.transform.InferType()(mod)
mutated_mod['func_5429'] = func_5429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5429_call = mutated_mod.get_global_var('func_5429')
call_5430 = func_5429_call()
output = call_5430
func_5431 = relay.Function([], output)
mutated_mod['func_5431'] = func_5431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_5465 = relay.TupleGetItem(func_1401_call(), 1)
call_5466 = relay.TupleGetItem(func_1403_call(), 1)
const_5479 = relay.const([[[-8.887135,2.588869,9.845948,-2.389059,3.633588,1.836634,7.025057,0.182154,1.617494,-6.810395,5.182457,6.711774,-5.181564,7.812457,9.267160,-2.780063],[6.339138,-1.357911,8.770749,8.945271,-7.349659,-2.925672,7.667059,-1.842877,4.818653,-7.972209,8.287272,8.294906,9.179985,-6.100731,2.234823,-4.682627],[1.023522,-7.545791,7.708769,6.731517,-5.880675,-4.366324,7.354820,-6.703293,7.529741,4.955461,8.728884,-3.847406,9.778530,0.183972,-0.463525,4.345659],[-1.707030,-8.705969,0.627333,2.973969,9.166751,7.449351,-3.636015,2.690602,-7.879760,-8.649362,3.785760,5.939071,-2.554972,-8.303394,-3.330212,-8.483448]],[[8.631380,3.109355,-0.257300,-3.888503,-8.572764,2.706944,-9.410722,-2.737869,3.960005,-9.588769,9.070491,-2.765794,-8.784290,-9.264421,-5.466243,0.398116],[7.410697,5.078196,0.353826,3.772083,0.607347,-6.517151,-6.027064,9.455603,-4.918762,-0.687046,6.029504,4.027497,7.390856,-2.312312,-8.260571,7.255490],[-1.136544,6.605210,2.654003,0.515407,1.722788,-9.205330,-6.516137,-1.384202,2.457030,7.545397,6.137111,-4.364272,-0.508108,-9.241678,-5.447936,3.919335],[-7.372127,-5.568599,6.352023,8.629723,0.553267,-5.227159,5.719768,-4.188938,-9.200314,0.255367,-6.442567,-0.360966,-9.571997,4.276051,1.439751,-2.784579]],[[-2.933655,9.891823,-5.171455,-6.762803,-3.097780,-5.455730,4.061314,-4.146400,-1.978479,3.638754,7.319076,2.406667,6.131337,-6.373141,8.579355,-5.125972],[1.905155,-2.883273,-2.611049,0.475527,9.896077,-3.114560,0.817907,-7.332728,-1.203493,-6.724722,-7.009828,-2.696275,5.512910,-4.680296,7.873632,-4.000803],[-3.491175,-9.304365,0.228604,3.173812,7.849136,-3.163891,-1.845623,-6.388385,-0.653376,-4.619046,5.981765,-1.242575,3.207362,0.729508,-1.360409,8.119833],[-6.858660,4.429893,3.301190,8.249745,8.458683,9.907105,-5.394230,-6.432995,9.204407,8.175774,3.466693,3.558572,-7.445155,8.210144,-4.413164,6.410422]],[[0.181508,-1.327577,2.220595,4.654316,0.071750,-9.516738,8.623649,5.473949,6.697356,7.262730,-9.048500,9.761060,1.257854,1.952269,0.664225,9.340196],[-8.753243,-3.225539,6.850538,-0.069207,-9.441088,-9.111636,1.817242,-2.275618,3.625185,-5.090019,-1.343298,-7.929780,-7.591814,5.739330,4.755172,-9.703959],[5.302105,5.893539,6.197046,7.076167,8.433013,1.981649,3.595633,5.672108,0.081038,9.026609,-4.120218,8.780101,2.964976,-8.703641,9.448744,-1.700195],[8.704163,4.202830,2.298124,5.304986,6.396366,-1.137827,-4.532763,8.091409,2.079587,-8.472702,-3.966584,-4.246865,-2.870904,-2.465574,-8.230057,-2.594163]]], dtype = "float32")#candidate|5479|(4, 4, 16)|const|float32
bop_5480 = relay.left_shift(call_5465.astype('int16'), relay.reshape(const_5479.astype('int16'), relay.shape_of(call_5465))) # shape=(4, 4, 16)
bop_5483 = relay.left_shift(call_5466.astype('int16'), relay.reshape(const_5479.astype('int16'), relay.shape_of(call_5466))) # shape=(4, 4, 16)
output = bop_5480
output2 = bop_5483
func_5492 = relay.Function([], output)
mod['func_5492'] = func_5492
mod = relay.transform.InferType()(mod)
mutated_mod['func_5492'] = func_5492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5492_call = mutated_mod.get_global_var('func_5492')
call_5493 = func_5492_call()
output = call_5493
func_5494 = relay.Function([], output)
mutated_mod['func_5494'] = func_5494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3120_call = mod.get_global_var('func_3120')
func_3121_call = mutated_mod.get_global_var('func_3121')
call_5495 = relay.TupleGetItem(func_3120_call(), 0)
call_5496 = relay.TupleGetItem(func_3121_call(), 0)
func_4595_call = mod.get_global_var('func_4595')
func_4597_call = mutated_mod.get_global_var('func_4597')
call_5507 = func_4595_call()
call_5508 = func_4595_call()
output = relay.Tuple([call_5495,call_5507,])
output2 = relay.Tuple([call_5496,call_5508,])
func_5516 = relay.Function([], output)
mod['func_5516'] = func_5516
mod = relay.transform.InferType()(mod)
mutated_mod['func_5516'] = func_5516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5516_call = mutated_mod.get_global_var('func_5516')
call_5517 = func_5516_call()
output = call_5517
func_5518 = relay.Function([], output)
mutated_mod['func_5518'] = func_5518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_742_call = mod.get_global_var('func_742')
func_743_call = mutated_mod.get_global_var('func_743')
call_5562 = func_742_call()
call_5563 = func_742_call()
output = relay.Tuple([call_5562,])
output2 = relay.Tuple([call_5563,])
func_5590 = relay.Function([], output)
mod['func_5590'] = func_5590
mod = relay.transform.InferType()(mod)
mutated_mod['func_5590'] = func_5590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5590_call = mutated_mod.get_global_var('func_5590')
call_5591 = func_5590_call()
output = call_5591
func_5592 = relay.Function([], output)
mutated_mod['func_5592'] = func_5592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5429_call = mod.get_global_var('func_5429')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_5608 = func_5429_call()
call_5609 = func_5429_call()
output = relay.Tuple([call_5608,])
output2 = relay.Tuple([call_5609,])
func_5612 = relay.Function([], output)
mod['func_5612'] = func_5612
mod = relay.transform.InferType()(mod)
output = func_5612()
func_5613 = relay.Function([], output)
mutated_mod['func_5613'] = func_5613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1819_call = mod.get_global_var('func_1819')
func_1820_call = mutated_mod.get_global_var('func_1820')
call_5624 = relay.TupleGetItem(func_1819_call(), 0)
call_5625 = relay.TupleGetItem(func_1820_call(), 0)
uop_5636 = relay.atanh(call_5624.astype('float64')) # shape=(4, 4, 16)
uop_5638 = relay.atanh(call_5625.astype('float64')) # shape=(4, 4, 16)
func_3358_call = mod.get_global_var('func_3358')
func_3360_call = mutated_mod.get_global_var('func_3360')
call_5641 = func_3358_call()
call_5642 = func_3358_call()
func_3483_call = mod.get_global_var('func_3483')
func_3486_call = mutated_mod.get_global_var('func_3486')
const_5647 = relay.const(-3, dtype = "uint8")#candidate|5647|()|const|uint8
call_5646 = relay.TupleGetItem(func_3483_call(relay.reshape(const_5647.astype('uint8'), [])), 0)
call_5648 = relay.TupleGetItem(func_3486_call(relay.reshape(const_5647.astype('uint8'), [])), 0)
func_2638_call = mod.get_global_var('func_2638')
func_2639_call = mutated_mod.get_global_var('func_2639')
call_5654 = func_2638_call()
call_5655 = func_2638_call()
output = relay.Tuple([uop_5636,call_5641,call_5646,const_5647,call_5654,])
output2 = relay.Tuple([uop_5638,call_5642,call_5648,const_5647,call_5655,])
func_5656 = relay.Function([], output)
mod['func_5656'] = func_5656
mod = relay.transform.InferType()(mod)
mutated_mod['func_5656'] = func_5656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5656_call = mutated_mod.get_global_var('func_5656')
call_5657 = func_5656_call()
output = call_5657
func_5658 = relay.Function([], output)
mutated_mod['func_5658'] = func_5658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1819_call = mod.get_global_var('func_1819')
func_1820_call = mutated_mod.get_global_var('func_1820')
call_5758 = relay.TupleGetItem(func_1819_call(), 0)
call_5759 = relay.TupleGetItem(func_1820_call(), 0)
var_5760 = relay.var("var_5760", dtype = "int8", shape = (4, 4, 16))#candidate|5760|(4, 4, 16)|var|int8
bop_5761 = relay.divide(call_5758.astype('float32'), relay.reshape(var_5760.astype('float32'), relay.shape_of(call_5758))) # shape=(4, 4, 16)
bop_5764 = relay.divide(call_5759.astype('float32'), relay.reshape(var_5760.astype('float32'), relay.shape_of(call_5759))) # shape=(4, 4, 16)
output = relay.Tuple([bop_5761,])
output2 = relay.Tuple([bop_5764,])
func_5772 = relay.Function([var_5760,], output)
mod['func_5772'] = func_5772
mod = relay.transform.InferType()(mod)
mutated_mod['func_5772'] = func_5772
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5773 = relay.var("var_5773", dtype = "int8", shape = (4, 4, 16))#candidate|5773|(4, 4, 16)|var|int8
func_5772_call = mutated_mod.get_global_var('func_5772')
call_5774 = func_5772_call(var_5773)
output = call_5774
func_5775 = relay.Function([var_5773], output)
mutated_mod['func_5775'] = func_5775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2924_call = mod.get_global_var('func_2924')
func_2926_call = mutated_mod.get_global_var('func_2926')
call_5791 = relay.TupleGetItem(func_2924_call(), 0)
call_5792 = relay.TupleGetItem(func_2926_call(), 0)
output = call_5791
output2 = call_5792
func_5807 = relay.Function([], output)
mod['func_5807'] = func_5807
mod = relay.transform.InferType()(mod)
mutated_mod['func_5807'] = func_5807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mutated_mod.get_global_var('func_5807')
call_5808 = func_5807_call()
output = call_5808
func_5809 = relay.Function([], output)
mutated_mod['func_5809'] = func_5809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5813 = relay.var("var_5813", dtype = "float32", shape = (2, 7, 6))#candidate|5813|(2, 7, 6)|var|float32
uop_5814 = relay.sigmoid(var_5813.astype('float32')) # shape=(2, 7, 6)
func_513_call = mod.get_global_var('func_513')
func_514_call = mutated_mod.get_global_var('func_514')
call_5816 = relay.TupleGetItem(func_513_call(), 0)
call_5817 = relay.TupleGetItem(func_514_call(), 0)
func_1792_call = mod.get_global_var('func_1792')
func_1794_call = mutated_mod.get_global_var('func_1794')
call_5821 = relay.TupleGetItem(func_1792_call(), 1)
call_5822 = relay.TupleGetItem(func_1794_call(), 1)
output = relay.Tuple([uop_5814,call_5816,call_5821,])
output2 = relay.Tuple([uop_5814,call_5817,call_5822,])
func_5825 = relay.Function([var_5813,], output)
mod['func_5825'] = func_5825
mod = relay.transform.InferType()(mod)
var_5826 = relay.var("var_5826", dtype = "float32", shape = (2, 7, 6))#candidate|5826|(2, 7, 6)|var|float32
output = func_5825(var_5826)
func_5827 = relay.Function([var_5826], output)
mutated_mod['func_5827'] = func_5827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5656_call = mod.get_global_var('func_5656')
func_5658_call = mutated_mod.get_global_var('func_5658')
call_5917 = relay.TupleGetItem(func_5656_call(), 0)
call_5918 = relay.TupleGetItem(func_5658_call(), 0)
output = call_5917
output2 = call_5918
func_5928 = relay.Function([], output)
mod['func_5928'] = func_5928
mod = relay.transform.InferType()(mod)
mutated_mod['func_5928'] = func_5928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5928_call = mutated_mod.get_global_var('func_5928')
call_5929 = func_5928_call()
output = call_5929
func_5930 = relay.Function([], output)
mutated_mod['func_5930'] = func_5930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4917_call = mod.get_global_var('func_4917')
func_4918_call = mutated_mod.get_global_var('func_4918')
call_5986 = func_4917_call()
call_5987 = func_4917_call()
output = call_5986
output2 = call_5987
func_6002 = relay.Function([], output)
mod['func_6002'] = func_6002
mod = relay.transform.InferType()(mod)
mutated_mod['func_6002'] = func_6002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6002_call = mutated_mod.get_global_var('func_6002')
call_6003 = func_6002_call()
output = call_6003
func_6004 = relay.Function([], output)
mutated_mod['func_6004'] = func_6004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3798_call = mod.get_global_var('func_3798')
func_3800_call = mutated_mod.get_global_var('func_3800')
call_6103 = relay.TupleGetItem(func_3798_call(), 2)
call_6104 = relay.TupleGetItem(func_3800_call(), 2)
func_312_call = mod.get_global_var('func_312')
func_313_call = mutated_mod.get_global_var('func_313')
call_6108 = relay.TupleGetItem(func_312_call(), 0)
call_6109 = relay.TupleGetItem(func_313_call(), 0)
output = relay.Tuple([call_6103,call_6108,])
output2 = relay.Tuple([call_6104,call_6109,])
func_6124 = relay.Function([], output)
mod['func_6124'] = func_6124
mod = relay.transform.InferType()(mod)
output = func_6124()
func_6125 = relay.Function([], output)
mutated_mod['func_6125'] = func_6125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_6239 = func_575_call()
call_6240 = func_575_call()
func_5147_call = mod.get_global_var('func_5147')
func_5149_call = mutated_mod.get_global_var('func_5149')
call_6250 = func_5147_call()
call_6251 = func_5147_call()
func_3033_call = mod.get_global_var('func_3033')
func_3035_call = mutated_mod.get_global_var('func_3035')
call_6253 = relay.TupleGetItem(func_3033_call(relay.reshape(call_6250.astype('int8'), [4, 4, 16])), 0)
call_6254 = relay.TupleGetItem(func_3035_call(relay.reshape(call_6250.astype('int8'), [4, 4, 16])), 0)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
call_6257 = relay.TupleGetItem(func_1401_call(), 1)
call_6258 = relay.TupleGetItem(func_1403_call(), 1)
func_513_call = mod.get_global_var('func_513')
func_514_call = mutated_mod.get_global_var('func_514')
call_6269 = relay.TupleGetItem(func_513_call(), 0)
call_6270 = relay.TupleGetItem(func_514_call(), 0)
output = relay.Tuple([call_6239,call_6250,call_6253,call_6257,call_6269,])
output2 = relay.Tuple([call_6240,call_6251,call_6254,call_6258,call_6270,])
func_6277 = relay.Function([], output)
mod['func_6277'] = func_6277
mod = relay.transform.InferType()(mod)
output = func_6277()
func_6278 = relay.Function([], output)
mutated_mod['func_6278'] = func_6278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5429_call = mod.get_global_var('func_5429')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_6306 = func_5429_call()
call_6307 = func_5429_call()
func_4502_call = mod.get_global_var('func_4502')
func_4506_call = mutated_mod.get_global_var('func_4506')
const_6313 = relay.const([0.912453,0.442553,-1.094552,-3.851571,9.182974,0.684641,6.740715,4.641259,6.543537,6.121582,-2.007986,-6.079960,-0.520779,6.007412,1.205307,5.887345,9.146603,-6.555999,-2.846914,-7.131645,-7.426357,4.725126,4.511893,4.688974,3.911019,-3.153584,-4.485162,2.860312,-8.850849,8.425634,4.352101,2.040934], dtype = "float64")#candidate|6313|(32,)|const|float64
call_6312 = relay.TupleGetItem(func_4502_call(relay.reshape(const_6313.astype('float64'), [32,]), relay.reshape(const_6313.astype('float64'), [32,]), ), 2)
call_6314 = relay.TupleGetItem(func_4506_call(relay.reshape(const_6313.astype('float64'), [32,]), relay.reshape(const_6313.astype('float64'), [32,]), ), 2)
func_3923_call = mod.get_global_var('func_3923')
func_3926_call = mutated_mod.get_global_var('func_3926')
const_6331 = relay.const([-5,8,1,3,-8,10,-5,1,-8,-7,2,3,3,5,2,-9,-10,3,9,-3,6,-10,8,8,-8,10,8,-1,9,-9,9,-10,-9,8,8,4,9,-4,-7,-4,5,4,-9,-4,-8,-9,-5,6,1,-1,-9,2,-10,4,9,4,-4,-7,3,1,-8,-10,3,-8,-2,-3,3,7,-4,-3,-3,-6,5,-1,-9,-2,7,2,8,4,7,8,-5,-5,10,-1,-7,1,2,-2,6,-6,6,1,-7,3,-2,-6,-10,5,3,2,-3,-3,4,-6,9,-3,1,10,-9,-2,6,8,-10,-5,-1,4,1,-10,3,5,-9,9,-2,-6,2,2,7,-1,4,-4,4,-2,-5,7,-8,2,-1,-7,-9,-4,2,-6,-7,-8,4,10,9,-10,4,-2,2,-2,-2,9,-2,2,-10,-5,-7,10,4,-9,9,7,9,-8,1,5,8,7,-7,-6,-7,-4,3,-6,-1,9,-4,-5,-6,-5,4,-2,-6,-6,8,-9,-2,-9,-6,-3,-10,9,1,-9,1,-3,4,9,4,2,-7,7,6,6,1,-1,4,-6,-5,1,9,-3,1,2,9,-9,6,8,2,-4,-3,-3,-4,-9,4,-7,6,-7,-3,-6,4,9,-1,-4,8,7,2,8,1,-8,-9,-9,6,6,4,2,-5,-9,-7,-3,-10,8,-10,-9,6,-7,4,-2,1,-2,7,-4,4,-3,6,-7,4,-8,2,7,-7,-2,10,1,-1,-8,-6,3,6,2,1,8,-5,-2,-6,-4,3,3,-8,-3,-7,7,3,-5,7,-3,-9,6,9,-2,8,7,-9,-3,5,8,-8,7,-7,2,-10,-4,8,-4,9,4,-9,9,3,9,-7,-2,-3,6,-1,-6,5,-9,-4,-2,8,-2,-10,7,10,-3,-2,-4,4,-5,-10,6,-2,10,2,9,-7,7,10,1,1,-1,-1,-9,6,-1,-4,-4,6,4,-6,-5,4,2,-9,7,9,6,2,-6,-9,9,-6,2,6,7,9,-7,-8,-8,-4,-9,-3,-2,10,7,4,3,-8,-1,2,-10,-10,3,-8,4,-8,-4,8,7,-5,-7,8,-1,4,-5,-8,7,-2,7,-5,-9,-4,3,-2,-1,-3,-7,8,-1,8,9,9,-7,8,8,-4,6,3,-1,-8,-1,3,-3,-6,3,8,-1,10,7,-1,-3,5,3,9,-2,-8,-9,1,-10,-6,-10,-7,-3,-8,-6,9,-3,9,2,-2,4,-7,1,-4,-4,5,7,6,8,-2,2,4,-6,1,-10], dtype = "int16")#candidate|6331|(480,)|const|int16
call_6330 = relay.TupleGetItem(func_3923_call(relay.reshape(const_6331.astype('int16'), [3, 10, 16])), 0)
call_6332 = relay.TupleGetItem(func_3926_call(relay.reshape(const_6331.astype('int16'), [3, 10, 16])), 0)
output = relay.Tuple([call_6306,call_6312,const_6313,call_6330,const_6331,])
output2 = relay.Tuple([call_6307,call_6314,const_6313,call_6332,const_6331,])
func_6340 = relay.Function([], output)
mod['func_6340'] = func_6340
mod = relay.transform.InferType()(mod)
output = func_6340()
func_6341 = relay.Function([], output)
mutated_mod['func_6341'] = func_6341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2497_call = mod.get_global_var('func_2497')
func_2499_call = mutated_mod.get_global_var('func_2499')
call_6442 = relay.TupleGetItem(func_2497_call(), 0)
call_6443 = relay.TupleGetItem(func_2499_call(), 0)
output = call_6442
output2 = call_6443
func_6448 = relay.Function([], output)
mod['func_6448'] = func_6448
mod = relay.transform.InferType()(mod)
output = func_6448()
func_6449 = relay.Function([], output)
mutated_mod['func_6449'] = func_6449
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6542 = relay.const([[[-3,-5,1],[-7,-1,1],[2,5,-5],[6,-2,4],[-10,3,4],[5,-2,2],[-8,-10,-7],[2,8,-3],[2,8,-2],[8,-1,-6],[-4,2,-1]],[[-1,5,-7],[10,-4,-9],[-3,8,6],[6,-4,4],[1,8,6],[-10,-10,8],[-7,-9,1],[8,10,7],[-8,10,9],[-1,-4,6],[10,-6,-8]],[[10,-7,6],[8,1,-2],[1,-1,-1],[7,-1,-10],[-10,2,3],[-2,-5,5],[-4,5,-8],[-6,-6,-2],[-5,8,-1],[-4,1,6],[-6,-8,-7]],[[2,3,-9],[-4,-3,-1],[-5,5,4],[-2,-4,-6],[8,1,3],[-8,-9,2],[-3,4,5],[3,2,5],[-4,8,-1],[-10,-4,-4],[9,4,2]],[[-8,2,-3],[7,-9,3],[-9,-1,7],[-1,1,-10],[-4,7,-6],[2,4,-8],[-1,2,-6],[-3,2,-1],[-8,-5,-8],[5,3,10],[1,-5,-7]],[[3,-8,7],[-7,-10,-6],[7,-5,-6],[9,-7,-5],[4,-10,-2],[-2,3,7],[-7,-2,-5],[-9,-6,-9],[1,6,-10],[4,7,-5],[-9,4,-8]],[[-5,7,-1],[10,7,8],[8,3,7],[3,9,7],[10,10,1],[-5,2,-6],[6,-7,-9],[10,4,1],[1,5,5],[4,10,-9],[4,7,-8]],[[1,6,1],[-2,-7,6],[-10,-4,-7],[-8,4,6],[9,9,-8],[-9,-5,6],[4,-8,-6],[9,-1,2],[-1,10,-10],[-1,8,7],[1,4,2]]], dtype = "uint32")#candidate|6542|(8, 11, 3)|const|uint32
var_6543 = relay.var("var_6543", dtype = "uint32", shape = (8, 11, 3))#candidate|6543|(8, 11, 3)|var|uint32
bop_6544 = relay.bitwise_xor(const_6542.astype('uint32'), relay.reshape(var_6543.astype('uint32'), relay.shape_of(const_6542))) # shape=(8, 11, 3)
output = relay.Tuple([bop_6544,])
output2 = relay.Tuple([bop_6544,])
func_6548 = relay.Function([var_6543,], output)
mod['func_6548'] = func_6548
mod = relay.transform.InferType()(mod)
var_6549 = relay.var("var_6549", dtype = "uint32", shape = (8, 11, 3))#candidate|6549|(8, 11, 3)|var|uint32
output = func_6548(var_6549)
func_6550 = relay.Function([var_6549], output)
mutated_mod['func_6550'] = func_6550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1466_call = mod.get_global_var('func_1466')
func_1467_call = mutated_mod.get_global_var('func_1467')
call_6574 = relay.TupleGetItem(func_1466_call(), 0)
call_6575 = relay.TupleGetItem(func_1467_call(), 0)
const_6597 = relay.const([[[-1.166240,-8.808257,7.772626,2.182486,7.166330,0.512745,0.170289,-6.390443,-1.686472,-6.790793,3.585341,-4.735090,-7.618203,-8.887298],[-3.448909,7.975433,-3.148449,-0.103732,9.590883,3.781321,-5.300832,-9.521766,-8.665555,-7.172061,-1.240638,1.806111,0.249132,6.605939]],[[2.038670,7.342562,0.421034,-4.108024,-5.878844,-5.579824,4.901730,-1.726342,-5.487837,1.770349,8.957873,9.039976,-1.098242,-6.540774],[-5.022992,8.278081,1.222091,-5.204806,1.923281,-4.355607,1.989177,-4.468479,-5.591944,-1.605932,4.745559,5.509953,-4.532716,3.092164]]], dtype = "float64")#candidate|6597|(2, 2, 14)|const|float64
bop_6598 = relay.not_equal(call_6574.astype('bool'), relay.reshape(const_6597.astype('bool'), relay.shape_of(call_6574))) # shape=(2, 2, 14)
bop_6601 = relay.not_equal(call_6575.astype('bool'), relay.reshape(const_6597.astype('bool'), relay.shape_of(call_6575))) # shape=(2, 2, 14)
var_6611 = relay.var("var_6611", dtype = "float64", shape = (2, 2, 14))#candidate|6611|(2, 2, 14)|var|float64
bop_6612 = relay.floor_divide(const_6597.astype('float32'), relay.reshape(var_6611.astype('float32'), relay.shape_of(const_6597))) # shape=(2, 2, 14)
output = relay.Tuple([bop_6598,bop_6612,])
output2 = relay.Tuple([bop_6601,bop_6612,])
func_6615 = relay.Function([var_6611,], output)
mod['func_6615'] = func_6615
mod = relay.transform.InferType()(mod)
mutated_mod['func_6615'] = func_6615
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6616 = relay.var("var_6616", dtype = "float64", shape = (2, 2, 14))#candidate|6616|(2, 2, 14)|var|float64
func_6615_call = mutated_mod.get_global_var('func_6615')
call_6617 = func_6615_call(var_6616)
output = call_6617
func_6618 = relay.Function([var_6616], output)
mutated_mod['func_6618'] = func_6618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4223_call = mod.get_global_var('func_4223')
func_4224_call = mutated_mod.get_global_var('func_4224')
call_6628 = func_4223_call()
call_6629 = func_4223_call()
uop_6630 = relay.log2(call_6628.astype('float32')) # shape=(4, 4, 16)
uop_6632 = relay.log2(call_6629.astype('float32')) # shape=(4, 4, 16)
func_5825_call = mod.get_global_var('func_5825')
func_5827_call = mutated_mod.get_global_var('func_5827')
const_6663 = relay.const([-0.302621,4.612633,9.415900,-8.198403,1.343393,-9.109897,-9.396208,2.913424,-6.170415,-7.049626,7.073624,-0.482452,3.439435,4.461091,6.329557,3.209632,-7.249540,-2.600115,-0.497953,1.219436,3.113377,8.229333,-8.173522,1.113713,2.283432,0.657279,-9.417570,7.886806,5.144235,-4.075237,-5.128759,-3.807062,0.684889,-9.886646,-5.792416,8.532477,2.721039,2.884834,1.270322,-6.525252,3.026574,7.502340,6.174916,8.457438,2.827802,7.303615,-0.166242,-1.670684,-2.964666,5.029106,3.425968,4.556839,2.275525,-0.004598,2.077481,1.029226,0.937703,-4.401484,4.861410,3.237849,-6.293596,-0.639907,-4.504923,-1.272598,1.106397,7.674579,-9.683126,9.156047,-1.351566,-0.762748,-1.441713,-2.430608,1.543983,-5.651138,-5.722646,6.242095,-2.847676,4.988405,8.671491,-8.750094,8.957480,0.586643,-9.241152,6.976085], dtype = "float32")#candidate|6663|(84,)|const|float32
call_6662 = relay.TupleGetItem(func_5825_call(relay.reshape(const_6663.astype('float32'), [2, 7, 6])), 2)
call_6664 = relay.TupleGetItem(func_5827_call(relay.reshape(const_6663.astype('float32'), [2, 7, 6])), 2)
func_1545_call = mod.get_global_var('func_1545')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_6670 = relay.TupleGetItem(func_1545_call(), 0)
call_6671 = relay.TupleGetItem(func_1546_call(), 0)
output = relay.Tuple([uop_6630,call_6662,const_6663,call_6670,])
output2 = relay.Tuple([uop_6632,call_6664,const_6663,call_6671,])
func_6684 = relay.Function([], output)
mod['func_6684'] = func_6684
mod = relay.transform.InferType()(mod)
mutated_mod['func_6684'] = func_6684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6684_call = mutated_mod.get_global_var('func_6684')
call_6685 = func_6684_call()
output = call_6685
func_6686 = relay.Function([], output)
mutated_mod['func_6686'] = func_6686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5516_call = mod.get_global_var('func_5516')
func_5518_call = mutated_mod.get_global_var('func_5518')
call_6778 = relay.TupleGetItem(func_5516_call(), 1)
call_6779 = relay.TupleGetItem(func_5518_call(), 1)
output = call_6778
output2 = call_6779
func_6791 = relay.Function([], output)
mod['func_6791'] = func_6791
mod = relay.transform.InferType()(mod)
output = func_6791()
func_6792 = relay.Function([], output)
mutated_mod['func_6792'] = func_6792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3936_call = mod.get_global_var('func_3936')
func_3937_call = mutated_mod.get_global_var('func_3937')
call_6839 = func_3936_call()
call_6840 = func_3936_call()
output = call_6839
output2 = call_6840
func_6864 = relay.Function([], output)
mod['func_6864'] = func_6864
mod = relay.transform.InferType()(mod)
mutated_mod['func_6864'] = func_6864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6864_call = mutated_mod.get_global_var('func_6864')
call_6865 = func_6864_call()
output = call_6865
func_6866 = relay.Function([], output)
mutated_mod['func_6866'] = func_6866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3358_call = mod.get_global_var('func_3358')
func_3360_call = mutated_mod.get_global_var('func_3360')
call_6938 = func_3358_call()
call_6939 = func_3358_call()
func_742_call = mod.get_global_var('func_742')
func_743_call = mutated_mod.get_global_var('func_743')
call_6952 = func_742_call()
call_6953 = func_742_call()
func_5122_call = mod.get_global_var('func_5122')
func_5125_call = mutated_mod.get_global_var('func_5125')
const_6976 = relay.const([[-9,-5,6,-9,1,3,6,10,7,2,-9,-5,-10,-8],[1,10,6,-2,-9,3,10,2,5,6,6,-1,4,6],[3,10,3,-3,-5,1,5,-4,1,1,-1,-8,-4,4],[7,5,-1,3,4,4,2,-5,-1,-1,8,8,8,6],[7,3,9,1,10,-5,1,-8,-7,9,2,2,-2,9],[8,-2,-5,-8,-1,-6,4,-9,-3,7,8,9,8,1],[-2,9,-8,-5,-6,-9,2,1,-9,3,5,-3,8,6],[1,-5,10,5,5,-10,4,9,5,4,-10,7,6,10],[-1,-1,4,7,2,-9,-3,9,8,-5,-9,6,-5,7],[-2,5,-3,-6,-4,10,-7,2,-10,9,-10,1,-5,-9],[10,2,-2,5,-5,4,-4,-5,5,-2,8,-3,8,-8],[-10,1,-4,4,-2,-3,8,6,2,-2,9,-4,-5,-5],[-2,6,-1,-6,10,1,6,8,-1,-5,-6,-4,3,9],[-6,3,-7,-3,-5,-3,8,-6,-8,-8,9,-6,2,-7],[7,-5,10,2,-6,-8,-6,6,5,-8,-6,-3,-10,9],[6,-9,4,5,-1,-3,-6,7,-2,-5,5,-9,10,10],[-1,-3,5,-10,-3,2,6,10,6,3,10,-2,-1,-8],[3,2,6,-2,7,-9,9,-4,-9,-8,-2,3,-8,7],[-8,-2,-2,6,10,-9,10,-7,1,7,-8,3,5,-1],[10,2,-2,8,9,-4,-2,5,-2,4,-6,3,3,3],[1,10,-2,1,9,8,5,-6,-4,10,5,-9,-4,-2],[-8,4,-9,-5,9,2,7,-5,-3,-3,3,-5,9,7],[6,-10,-4,-6,-9,1,8,5,7,-10,-10,-1,6,1],[-10,7,-8,2,1,5,10,-9,3,-4,3,-3,6,-6],[-10,10,-5,-7,5,-5,9,8,5,-8,1,-9,5,-7],[-5,-5,-2,-4,1,-10,-3,3,-2,-1,-8,5,10,-4],[-5,-6,-8,5,4,-6,1,1,10,5,-5,-1,7,10],[2,-2,7,-7,-1,-4,2,-1,-6,8,-6,-10,-1,-2],[8,8,8,-9,10,-9,-8,5,2,4,8,-4,5,3],[-6,6,9,-6,-4,9,8,-4,-10,8,-6,-10,6,-9],[9,-9,-9,10,9,-2,-8,-8,10,7,-4,3,-9,4],[-6,-6,-7,1,2,-3,-5,5,-7,-2,-8,10,-3,-1],[4,10,8,-7,3,-10,-9,-5,7,10,6,2,2,-3],[5,-9,-9,10,-5,2,-7,2,-3,-2,8,4,-5,-7],[10,-2,-5,-5,10,-2,4,-4,4,7,-2,8,3,5],[10,-5,-1,7,-9,-10,8,7,-6,5,6,9,-2,-9]], dtype = "int64")#candidate|6976|(36, 14)|const|int64
call_6975 = func_5122_call(relay.reshape(const_6976.astype('int64'), [6, 7, 12]))
call_6977 = func_5122_call(relay.reshape(const_6976.astype('int64'), [6, 7, 12]))
output = relay.Tuple([call_6938,call_6952,call_6975,const_6976,])
output2 = relay.Tuple([call_6939,call_6953,call_6977,const_6976,])
func_6978 = relay.Function([], output)
mod['func_6978'] = func_6978
mod = relay.transform.InferType()(mod)
mutated_mod['func_6978'] = func_6978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6978_call = mutated_mod.get_global_var('func_6978')
call_6979 = func_6978_call()
output = call_6979
func_6980 = relay.Function([], output)
mutated_mod['func_6980'] = func_6980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3003_call = mod.get_global_var('func_3003')
func_3005_call = mutated_mod.get_global_var('func_3005')
call_6989 = relay.TupleGetItem(func_3003_call(), 0)
call_6990 = relay.TupleGetItem(func_3005_call(), 0)
output = relay.Tuple([call_6989,])
output2 = relay.Tuple([call_6990,])
func_7009 = relay.Function([], output)
mod['func_7009'] = func_7009
mod = relay.transform.InferType()(mod)
mutated_mod['func_7009'] = func_7009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7009_call = mutated_mod.get_global_var('func_7009')
call_7010 = func_7009_call()
output = call_7010
func_7011 = relay.Function([], output)
mutated_mod['func_7011'] = func_7011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1792_call = mod.get_global_var('func_1792')
func_1794_call = mutated_mod.get_global_var('func_1794')
call_7042 = relay.TupleGetItem(func_1792_call(), 1)
call_7043 = relay.TupleGetItem(func_1794_call(), 1)
const_7072 = relay.const([[[2,-10,6,1,-7,6,9,9,1,-7,1,-1,-2,10,6,3],[-4,2,6,7,-6,-7,4,-6,-7,-10,-10,1,-7,-1,-5,-10],[1,8,-5,-5,5,6,5,4,5,-2,-6,-7,6,-7,-4,9],[-9,5,9,5,-9,3,4,-7,3,4,-4,6,10,-2,-10,-2]],[[-7,5,6,-2,-10,10,-4,3,-6,-9,-1,-2,-8,-7,-5,-9],[7,-10,3,-9,-9,-1,6,2,-2,-4,-6,5,-1,6,3,-6],[-1,-1,-8,-9,9,-2,3,-1,-5,-1,-3,8,-9,8,10,-10],[2,-5,-2,-9,-6,8,-7,8,5,-4,4,-10,6,4,-6,5]],[[6,10,6,-2,2,-2,10,2,9,-2,8,5,4,8,-6,7],[4,-1,-9,-3,-5,-10,6,8,8,8,6,1,-5,-9,3,2],[-3,8,-7,1,-5,-7,-4,4,-7,-9,-8,-2,-9,-3,-6,10],[9,1,8,-8,-4,-3,9,10,2,10,8,-2,-4,-1,-1,10]],[[-10,7,-3,-10,1,-7,3,-10,-7,-2,4,-3,-10,-1,-5,2],[-3,5,6,-7,1,7,1,6,8,2,3,-4,-2,-5,-7,-4],[5,-8,-5,6,-9,7,-2,8,2,-6,7,-9,5,6,8,-2],[-9,2,7,9,4,-4,10,8,3,-6,-4,-9,-8,8,-7,9]]], dtype = "int8")#candidate|7072|(4, 4, 16)|const|int8
bop_7073 = relay.right_shift(call_7042.astype('int64'), relay.reshape(const_7072.astype('int64'), relay.shape_of(call_7042))) # shape=(4, 4, 16)
bop_7076 = relay.right_shift(call_7043.astype('int64'), relay.reshape(const_7072.astype('int64'), relay.shape_of(call_7043))) # shape=(4, 4, 16)
func_3051_call = mod.get_global_var('func_3051')
func_3054_call = mutated_mod.get_global_var('func_3054')
const_7086 = relay.const([[-0.881158],[-0.303442],[4.146305],[-7.071307],[-9.729156],[9.685477],[-8.457000],[2.086877],[5.740428],[9.060877],[-8.152527],[-4.623640],[-0.063373],[9.964665],[7.567630],[-1.400048],[-6.510724],[-1.053166],[-7.018896],[0.556455],[1.809098],[6.881759],[8.815690],[-9.724262],[7.342440],[6.908272],[-6.018039],[-5.750911],[-7.669793],[2.337204],[5.060172],[8.127478],[-9.221783],[4.217454],[5.123227],[7.035197],[3.471195],[-8.832614],[9.436108],[9.503327],[-9.243740],[8.898139],[8.146843],[-2.728350],[7.764754],[7.495803],[9.511416],[-9.089397],[-3.299604],[-5.415304],[3.636907],[-8.213023],[9.290424],[4.400646],[1.269042],[8.584713]], dtype = "float64")#candidate|7086|(56, 1)|const|float64
call_7085 = relay.TupleGetItem(func_3051_call(relay.reshape(const_7086.astype('float64'), [2, 2, 14])), 0)
call_7087 = relay.TupleGetItem(func_3054_call(relay.reshape(const_7086.astype('float64'), [2, 2, 14])), 0)
output = relay.Tuple([bop_7073,call_7085,const_7086,])
output2 = relay.Tuple([bop_7076,call_7087,const_7086,])
func_7088 = relay.Function([], output)
mod['func_7088'] = func_7088
mod = relay.transform.InferType()(mod)
output = func_7088()
func_7089 = relay.Function([], output)
mutated_mod['func_7089'] = func_7089
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7129 = relay.const(6, dtype = "int32")#candidate|7129|()|const|int32
const_7130 = relay.const([[[-8,-3,6,8,8,1,8,6,-1,1,1,10,-3,4,-2,-8],[-7,-1,-10,8,10,6,1,10,-10,5,-8,-5,9,9,-10,-4],[-7,-1,5,-7,-9,2,4,3,4,-9,-5,3,6,7,-8,-4],[-7,2,-4,-6,-3,-4,-10,-2,7,5,8,7,-10,9,-7,-5],[-7,6,-7,6,-9,-6,7,3,1,-5,-8,2,-7,7,3,-10]],[[-8,-4,9,4,10,8,2,-9,-9,-4,7,6,7,7,5,2],[4,-8,-6,2,4,3,-3,-1,-9,1,10,-9,9,7,-5,-9],[7,-1,-2,10,5,4,-6,-10,1,-10,-9,6,-4,3,-3,8],[10,4,-6,-1,-8,1,-1,8,4,-1,-6,10,1,1,6,6],[1,-1,4,10,-7,5,-3,10,-10,10,-1,6,-6,7,-4,-1]],[[5,-4,1,3,6,-8,1,-6,-10,-5,-1,-2,-5,10,-4,-8],[2,-9,7,-3,-10,-2,10,9,8,-2,6,5,-4,3,-5,-6],[5,2,-5,-5,-9,-5,-8,-10,10,-3,-5,-10,-3,-5,-5,7],[-6,2,-7,8,7,-4,10,1,-3,8,3,5,10,6,2,-5],[-4,2,7,7,5,-1,5,-7,-6,-6,-3,-5,-2,-8,4,-3]],[[-4,4,-6,9,4,6,-2,6,8,-5,3,-3,10,-9,9,-5],[-8,-8,9,8,7,-3,-9,-5,10,-9,1,-10,-7,5,1,-1],[-10,5,-6,5,7,2,-6,4,-8,-1,-6,10,-9,9,7,-9],[1,-8,-5,10,-10,9,-9,4,-5,-6,5,4,3,4,-5,8],[-6,-5,-1,6,-7,-7,-7,6,5,5,-10,-4,4,6,2,9]],[[2,1,-7,5,2,-2,3,3,10,10,8,-4,1,-6,-3,2],[-7,1,10,7,1,2,-7,-4,4,-6,7,7,-1,-2,7,2],[-7,-7,-2,-2,6,-9,-1,-10,4,-1,8,-8,2,3,-3,1],[-1,-8,3,-8,-6,-1,-9,-3,-7,-3,-4,-3,-2,-4,-5,-7],[-3,3,-7,-4,7,9,6,-10,-8,-7,-7,-9,-9,6,-9,-2]],[[9,10,-4,8,-2,9,1,-9,4,5,6,-10,8,9,-8,2],[4,-3,6,4,-10,-6,-4,-4,-2,-2,3,-5,8,10,7,-3],[-4,1,-2,10,10,3,-10,6,5,2,8,9,-3,3,-1,-1],[5,-4,9,-8,-9,-6,-9,-3,-8,2,-2,3,-2,-5,3,5],[-8,-6,3,7,-5,3,3,10,-10,-7,-7,-10,-7,9,1,-7]],[[-5,5,6,-1,4,7,-9,9,1,-6,8,-7,-10,-2,-2,-1],[3,8,9,10,-5,-1,6,-6,7,7,-7,-10,-1,-10,-3,-2],[9,6,1,-1,5,-3,-3,-9,-10,-6,9,5,-8,4,8,-10],[8,-4,1,7,7,-8,8,1,-4,-6,10,-2,8,10,4,10],[-5,10,10,-4,7,7,9,-7,2,-5,-7,-1,-5,-1,-10,-10]],[[5,-2,7,-2,-8,-4,-7,-10,-6,-3,4,-6,-4,7,-7,-2],[-6,9,-10,2,2,-5,-6,-9,-1,-5,-4,-5,9,-6,-10,-1],[3,-2,3,-9,1,-5,10,-9,-6,-8,-7,-3,-7,-3,7,3],[-5,1,10,-6,-5,-8,-7,-7,-5,-3,10,-9,5,1,-7,4],[-3,2,8,-4,1,9,3,10,5,-10,-9,9,10,-10,8,9]],[[-10,3,-10,-2,-3,8,-8,-3,2,-7,2,-9,-8,9,2,5],[2,-1,-9,5,3,-9,2,4,-7,6,-7,-2,-1,-2,3,-6],[-7,5,-9,9,4,3,-10,-1,-9,8,2,-2,-3,8,2,-8],[1,9,8,2,-6,9,3,4,-6,10,4,-1,-6,2,-2,-1],[8,7,-7,-7,5,2,-5,-1,-9,-9,3,-10,8,9,4,7]],[[9,9,2,-1,-1,4,-9,9,4,-1,-7,-5,4,-8,-3,2],[6,10,-7,-4,3,-8,-3,-10,-4,-5,5,7,6,-8,10,-3],[-5,-6,-1,3,-10,-8,-8,3,1,-3,10,6,7,6,-7,-6],[9,5,4,-6,8,9,-2,8,-2,2,2,9,3,9,-4,10],[-8,-5,-4,-9,5,-8,2,-2,8,-6,1,2,-3,-2,3,-2]],[[9,-3,10,-5,2,4,1,8,-2,-2,2,-7,-2,-3,4,-7],[-5,-6,-4,10,6,10,3,-9,-2,8,-4,10,5,-2,-1,2],[3,10,10,-3,-5,-8,-9,-3,-9,-5,-7,10,10,-1,-2,6],[-2,3,6,10,9,2,-4,-10,-8,-5,-4,5,6,-5,-8,4],[-5,1,4,-5,-7,4,-5,-4,3,-6,-4,-9,8,9,-2,7]],[[3,-1,9,-2,6,-8,2,2,1,10,-10,4,-4,-5,9,6],[-9,-10,6,7,-10,2,6,7,3,-1,-8,-4,-1,9,-10,3],[-3,-10,-5,-10,1,-8,6,-6,-3,-6,3,3,7,-5,8,-10],[1,9,-8,-2,1,-8,3,9,-1,9,3,10,-4,10,-3,5],[10,-1,-5,9,-2,4,-1,1,8,-9,-2,2,6,-9,10,-4]],[[-8,-1,7,-10,9,4,8,5,7,-6,3,-6,10,7,-9,-2],[-5,3,-5,10,-6,-3,2,-2,-1,10,8,10,-1,-8,9,1],[-5,5,5,3,4,10,5,6,2,-8,2,-8,9,7,-6,-2],[-1,10,-4,1,-8,-5,3,-8,9,-5,6,-6,-9,-10,9,7],[-9,-10,-9,-3,4,-1,1,-1,-5,-9,-2,-5,8,-8,-7,1]],[[-4,-1,3,-2,-3,-3,-2,3,3,-8,1,-5,-9,7,8,2],[-10,4,10,-10,3,-7,8,-4,-4,-5,6,-3,1,-10,10,10],[8,3,4,-1,5,-1,8,5,8,6,-9,10,10,10,6,10],[-6,2,-6,-6,-8,5,2,7,-9,-3,-1,10,-5,-3,-10,4],[6,7,-6,-5,2,10,2,-4,-10,1,2,-5,2,9,-1,-10]],[[-7,-10,-2,9,7,-7,-7,-1,-10,10,-6,10,-5,1,-9,4],[2,3,1,9,1,6,-7,-7,-3,-10,6,-8,8,-8,4,5],[7,9,9,-3,-6,-8,-8,-1,-4,2,10,10,1,4,-1,1],[-6,4,-10,6,8,8,-1,-6,1,-4,8,-8,-1,4,1,9],[-8,5,-10,4,8,-3,-5,3,-7,-7,-2,-3,5,-6,5,-6]]], dtype = "int32")#candidate|7130|(15, 5, 16)|const|int32
bop_7131 = relay.left_shift(const_7129.astype('int32'), const_7130.astype('int32')) # shape=(15, 5, 16)
output = relay.Tuple([bop_7131,])
output2 = relay.Tuple([bop_7131,])
func_7134 = relay.Function([], output)
mod['func_7134'] = func_7134
mod = relay.transform.InferType()(mod)
mutated_mod['func_7134'] = func_7134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7134_call = mutated_mod.get_global_var('func_7134')
call_7135 = func_7134_call()
output = call_7135
func_7136 = relay.Function([], output)
mutated_mod['func_7136'] = func_7136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2686_call = mod.get_global_var('func_2686')
func_2687_call = mutated_mod.get_global_var('func_2687')
call_7153 = relay.TupleGetItem(func_2686_call(), 0)
call_7154 = relay.TupleGetItem(func_2687_call(), 0)
func_4859_call = mod.get_global_var('func_4859')
func_4863_call = mutated_mod.get_global_var('func_4863')
var_7160 = relay.var("var_7160", dtype = "int64", shape = (504,))#candidate|7160|(504,)|var|int64
call_7159 = relay.TupleGetItem(func_4859_call(relay.reshape(var_7160.astype('int64'), [8, 9, 7]), relay.reshape(var_7160.astype('int64'), [8, 9, 7]), ), 0)
call_7161 = relay.TupleGetItem(func_4863_call(relay.reshape(var_7160.astype('int64'), [8, 9, 7]), relay.reshape(var_7160.astype('int64'), [8, 9, 7]), ), 0)
output = relay.Tuple([call_7153,call_7159,var_7160,])
output2 = relay.Tuple([call_7154,call_7161,var_7160,])
func_7165 = relay.Function([var_7160,], output)
mod['func_7165'] = func_7165
mod = relay.transform.InferType()(mod)
var_7166 = relay.var("var_7166", dtype = "int64", shape = (504,))#candidate|7166|(504,)|var|int64
output = func_7165(var_7166)
func_7167 = relay.Function([var_7166], output)
mutated_mod['func_7167'] = func_7167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4595_call = mod.get_global_var('func_4595')
func_4597_call = mutated_mod.get_global_var('func_4597')
call_7283 = func_4595_call()
call_7284 = func_4595_call()
func_1792_call = mod.get_global_var('func_1792')
func_1794_call = mutated_mod.get_global_var('func_1794')
call_7287 = relay.TupleGetItem(func_1792_call(), 1)
call_7288 = relay.TupleGetItem(func_1794_call(), 1)
output = relay.Tuple([call_7283,call_7287,])
output2 = relay.Tuple([call_7284,call_7288,])
func_7314 = relay.Function([], output)
mod['func_7314'] = func_7314
mod = relay.transform.InferType()(mod)
output = func_7314()
func_7315 = relay.Function([], output)
mutated_mod['func_7315'] = func_7315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3936_call = mod.get_global_var('func_3936')
func_3937_call = mutated_mod.get_global_var('func_3937')
call_7329 = func_3936_call()
call_7330 = func_3936_call()
output = relay.Tuple([call_7329,])
output2 = relay.Tuple([call_7330,])
func_7333 = relay.Function([], output)
mod['func_7333'] = func_7333
mod = relay.transform.InferType()(mod)
mutated_mod['func_7333'] = func_7333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7333_call = mutated_mod.get_global_var('func_7333')
call_7334 = func_7333_call()
output = call_7334
func_7335 = relay.Function([], output)
mutated_mod['func_7335'] = func_7335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_7346 = func_5807_call()
call_7347 = func_5807_call()
uop_7355 = relay.cos(call_7346.astype('float64')) # shape=(1, 2, 16)
uop_7357 = relay.cos(call_7347.astype('float64')) # shape=(1, 2, 16)
output = relay.Tuple([uop_7355,])
output2 = relay.Tuple([uop_7357,])
func_7363 = relay.Function([], output)
mod['func_7363'] = func_7363
mod = relay.transform.InferType()(mod)
output = func_7363()
func_7364 = relay.Function([], output)
mutated_mod['func_7364'] = func_7364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7464 = relay.var("var_7464", dtype = "int32", shape = (5, 15, 16))#candidate|7464|(5, 15, 16)|var|int32
var_7465 = relay.var("var_7465", dtype = "int32", shape = (5, 15, 16))#candidate|7465|(5, 15, 16)|var|int32
bop_7466 = relay.maximum(var_7464.astype('int32'), relay.reshape(var_7465.astype('int32'), relay.shape_of(var_7464))) # shape=(5, 15, 16)
func_7314_call = mod.get_global_var('func_7314')
func_7315_call = mutated_mod.get_global_var('func_7315')
call_7480 = relay.TupleGetItem(func_7314_call(), 0)
call_7481 = relay.TupleGetItem(func_7315_call(), 0)
output = relay.Tuple([bop_7466,call_7480,])
output2 = relay.Tuple([bop_7466,call_7481,])
func_7484 = relay.Function([var_7464,var_7465,], output)
mod['func_7484'] = func_7484
mod = relay.transform.InferType()(mod)
var_7485 = relay.var("var_7485", dtype = "int32", shape = (5, 15, 16))#candidate|7485|(5, 15, 16)|var|int32
var_7486 = relay.var("var_7486", dtype = "int32", shape = (5, 15, 16))#candidate|7486|(5, 15, 16)|var|int32
output = func_7484(var_7485,var_7486,)
func_7487 = relay.Function([var_7485,var_7486,], output)
mutated_mod['func_7487'] = func_7487
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7534 = relay.var("var_7534", dtype = "float32", shape = (1, 7, 2))#candidate|7534|(1, 7, 2)|var|float32
uop_7535 = relay.exp(var_7534.astype('float32')) # shape=(1, 7, 2)
func_556_call = mod.get_global_var('func_556')
func_559_call = mutated_mod.get_global_var('func_559')
var_7539 = relay.var("var_7539", dtype = "float64", shape = (1568,))#candidate|7539|(1568,)|var|float64
call_7538 = relay.TupleGetItem(func_556_call(relay.reshape(var_7539.astype('float64'), [1568,])), 2)
call_7540 = relay.TupleGetItem(func_559_call(relay.reshape(var_7539.astype('float64'), [1568,])), 2)
func_2686_call = mod.get_global_var('func_2686')
func_2687_call = mutated_mod.get_global_var('func_2687')
call_7547 = relay.TupleGetItem(func_2686_call(), 0)
call_7548 = relay.TupleGetItem(func_2687_call(), 0)
func_5590_call = mod.get_global_var('func_5590')
func_5592_call = mutated_mod.get_global_var('func_5592')
call_7559 = relay.TupleGetItem(func_5590_call(), 0)
call_7560 = relay.TupleGetItem(func_5592_call(), 0)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_7567 = func_5807_call()
call_7568 = func_5807_call()
output = relay.Tuple([uop_7535,call_7538,var_7539,call_7547,call_7559,call_7567,])
output2 = relay.Tuple([uop_7535,call_7540,var_7539,call_7548,call_7560,call_7568,])
func_7581 = relay.Function([var_7534,var_7539,], output)
mod['func_7581'] = func_7581
mod = relay.transform.InferType()(mod)
var_7582 = relay.var("var_7582", dtype = "float32", shape = (1, 7, 2))#candidate|7582|(1, 7, 2)|var|float32
var_7583 = relay.var("var_7583", dtype = "float64", shape = (1568,))#candidate|7583|(1568,)|var|float64
output = func_7581(var_7582,var_7583,)
func_7584 = relay.Function([var_7582,var_7583,], output)
mutated_mod['func_7584'] = func_7584
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7595 = relay.var("var_7595", dtype = "float64", shape = (12, 6, 11))#candidate|7595|(12, 6, 11)|var|float64
uop_7596 = relay.log2(var_7595.astype('float64')) # shape=(12, 6, 11)
func_2497_call = mod.get_global_var('func_2497')
func_2499_call = mutated_mod.get_global_var('func_2499')
call_7602 = relay.TupleGetItem(func_2497_call(), 0)
call_7603 = relay.TupleGetItem(func_2499_call(), 0)
uop_7613 = relay.log(var_7595.astype('float32')) # shape=(12, 6, 11)
output = relay.Tuple([uop_7596,call_7602,uop_7613,])
output2 = relay.Tuple([uop_7596,call_7603,uop_7613,])
func_7624 = relay.Function([var_7595,], output)
mod['func_7624'] = func_7624
mod = relay.transform.InferType()(mod)
var_7625 = relay.var("var_7625", dtype = "float64", shape = (12, 6, 11))#candidate|7625|(12, 6, 11)|var|float64
output = func_7624(var_7625)
func_7626 = relay.Function([var_7625], output)
mutated_mod['func_7626'] = func_7626
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7634 = relay.var("var_7634", dtype = "int16", shape = ())#candidate|7634|()|var|int16
const_7635 = relay.const([[[-8,-4,-7,1,-1,-5,-10,-3,8,6],[8,-4,-9,10,10,9,-8,6,-1,5]]], dtype = "int16")#candidate|7635|(1, 2, 10)|const|int16
bop_7636 = relay.greater_equal(var_7634.astype('bool'), const_7635.astype('bool')) # shape=(1, 2, 10)
bop_7643 = relay.mod(var_7634.astype('float64'), bop_7636.astype('float64')) # shape=(1, 2, 10)
func_7088_call = mod.get_global_var('func_7088')
func_7089_call = mutated_mod.get_global_var('func_7089')
call_7651 = relay.TupleGetItem(func_7088_call(), 0)
call_7652 = relay.TupleGetItem(func_7089_call(), 0)
func_3732_call = mod.get_global_var('func_3732')
func_3734_call = mutated_mod.get_global_var('func_3734')
const_7659 = relay.const([-5.178112,0.257346,4.222094,4.104431,4.430252,0.060475,-9.573768,-2.976475,-7.724269,-0.050904,8.700845,-7.913740,-2.415304,-3.256171,-8.122736,-3.956659,2.833681,0.865480,7.543358,8.448910,6.670295,8.242560,5.499928,-2.520530,4.624234,-8.873452,6.971672,-7.361040,-0.861160,7.088637,-0.101115,4.234785,-4.360958,7.964832,9.070731,-0.800773,2.408215,-9.156873,-2.973230,-3.890747,-0.561852,-1.859504,3.839249,6.472234,8.600986,-0.668528,-8.916389,0.034887,4.979667,-5.234171,2.242536,8.552797,6.690105,9.672313,-1.374550,9.227001,7.469318,3.796762,-3.120364,-4.849457,8.654375,-7.094278,-5.590257,-0.616911,-1.557168,6.524256,-6.909971,-1.788944,-4.721501,7.988375,3.218322,4.076829,-7.043657,7.514809,-9.046360,-7.716337,0.489504,3.796616,-6.937871,6.481689,2.411459,9.232696,2.380200,3.678968,6.731148,-5.014012,3.984775,9.997622,-8.680105,0.555080,-0.476828,0.815529,-0.882864,-8.886714,-1.392548,6.456317,-2.618053,6.004714,-8.266438,6.348686,1.837014,-1.543157,-4.354152,-2.769916,-0.700226,3.426617,1.823106,-6.508649,3.852330,6.104584,-5.054672,3.770923,2.225115,-2.279816,7.609806,8.889316,-1.154490,-7.925464,-6.198192,9.896023,-1.251376,6.489606,3.825796,2.828619,-8.197880,6.947552,6.455801,4.904048,0.954476,-3.615671,-3.922811,-1.981739,6.182403,3.336076,5.247542,-3.739570,9.294311,-9.538658,-7.593961,3.958256,-0.750250,9.061768,-3.012784,-1.428247,4.917673,-7.155580,-4.120993,-8.936038,6.409106,6.053249,-8.340260,-2.792459,-8.127036,6.262618,-6.536115,7.114233,2.382706,-5.763831,-9.415683,7.957561,2.221289,3.297144,-9.614258,0.143779,4.310226,8.956479,4.372375,3.021650,-7.463020,-5.586693,7.854465,1.170073,-7.566131,-8.945082,-4.988933,-4.332078,-7.840310,8.882048,0.363145,-7.923016,-9.798694,8.852921,-5.894363,0.216599,9.410278,3.630367,8.654478,7.726193,1.284603,-9.415076,7.445042,4.755804,-8.898583,5.918012,-0.888531,-3.727669,0.780668,-1.949612,-7.817559,-5.488414,5.565956,4.776015,-5.513857,-7.801996,-7.513512,6.262166,-2.608017,9.025442,3.380117,-2.821760,5.500696,-0.268296,-6.189762,-4.921291,-7.683169,-3.177194,-3.950323,7.627749,-6.289149,-8.382438,-0.679228,5.943804,2.019879,-2.386373,0.528418,-2.511101,9.278429,9.125989,0.586501,5.221281,-2.342626,9.709300,8.306635,2.168037,-3.607176,-9.831730,6.191825,5.284121,9.367330,7.176314,9.206330,9.791257,5.540308,-0.415747,-2.630155,-4.777746,-3.481429,8.190224,-6.832771,3.913409,0.120209,-5.732181,1.916226,3.240762,0.113410,5.227709,-5.125012,5.332618,6.428965,-0.510378,0.314368,-1.386932,-9.679203,8.441262,-4.025984,2.450267,6.453307,-2.447491,-6.746526,0.539890,2.546850,-0.941364,9.838330,8.813555,5.916161,-1.749795,-3.201974,-9.350759,-5.102097,-0.138064,8.206999,-3.657744,7.205093,8.520471,-3.345995,9.085945,-1.144543,9.054643,4.847632,-6.288972,-2.337720,-4.835131,-5.447075,0.039704,-0.234024,9.184873,-0.958141,-9.545319,8.343704,8.852857,-3.688799,8.940152,-8.389439,-3.467233,3.336913,-1.893712,7.362923,-6.497835,-6.531728,2.184056,7.672135,-8.499729,-2.215301,5.237780,-6.094203,-4.512828,6.525933,7.022031,-0.050116,-7.824839,0.246879,-8.521252,2.352552,-4.771134,-6.104276,-5.236793,-6.027259,9.399726,-6.048207,-1.263084,2.318888,0.927490,-8.431923,-0.156877,5.628020,-1.696086,-7.840415,9.367521,-1.371801,5.994103,7.952149,-0.719824,-6.320476,3.387298,6.341045,7.462907,-9.899972,7.121794,-9.000208,8.268774,-3.803178,-1.591875,-4.175664,-5.220204,4.570911,-0.417636,-4.751867,-9.021741,-4.679671,4.104059,-2.477571,2.497161,4.507794,3.335635,-4.094061,6.647004,9.730317,9.232508,-0.363392,-3.178220,2.858501,-4.012103,0.187490,-1.290759,-2.158611,7.581974,1.783298,4.372420,-9.265610,-4.116867,-2.165239,4.418352,2.726318,8.983575,5.504626,5.015273,-0.856140,-5.460954,-6.722257,-9.137008,-8.027193,6.680041,-6.809675,-0.806113,-5.776696,6.384209,5.387394,-6.647075,-4.454441,-3.229891,0.890431,-6.632951,8.988753,3.464371,-9.816363,2.352892,-9.981234,-0.833887,1.737661,7.387887,1.855855,-8.101818,2.909742,3.183775,5.566560,3.103952,6.723513,-4.420427,-6.807160,-1.497242,9.415017,9.058301,6.008975,-0.550169,3.671021,-7.824499,8.436714,1.200089,1.098391,-8.838722,-8.346393,2.372374,1.051915,-5.942504,9.333359,-0.678993,-0.409855,-7.616444,2.476177,1.198580,-7.920506,8.564006,-1.834227,9.637455,4.312124,-7.731959,9.595934,2.987722,-2.222654,4.284959,5.986206,-4.869708,5.170754,3.497654,-6.828928,3.477250,-7.278024,-8.611815,9.708012,-8.642002,1.674777,-9.089590,-1.046173,9.679066,-0.992735,-7.154914,6.362893,3.439730,-9.790769,8.465744,2.361844,1.889096,-6.174590,4.204110,4.539263,-8.807582,-3.451450,-2.389476,3.713791,3.723951,-5.812953,5.888230,8.950734,-2.731443,8.768625,-9.429395,9.404726,-4.921379,3.897224,1.549772,6.222296,2.541977,4.147045,-9.741040,9.619652,-6.868961,8.782418,2.869207,-3.406301,-8.752839,-3.303154,9.576848,1.759312,0.037577,1.889988,1.849408,-7.796951,-6.040876,-2.959842,-6.428861,1.204190,4.878126], dtype = "float64")#candidate|7659|(512,)|const|float64
call_7658 = relay.TupleGetItem(func_3732_call(relay.reshape(const_7659.astype('float64'), [16, 2, 16])), 1)
call_7660 = relay.TupleGetItem(func_3734_call(relay.reshape(const_7659.astype('float64'), [16, 2, 16])), 1)
uop_7663 = relay.log2(bop_7636.astype('float32')) # shape=(1, 2, 10)
func_4917_call = mod.get_global_var('func_4917')
func_4918_call = mutated_mod.get_global_var('func_4918')
call_7668 = func_4917_call()
call_7669 = func_4917_call()
output = relay.Tuple([bop_7643,call_7651,call_7658,const_7659,uop_7663,call_7668,])
output2 = relay.Tuple([bop_7643,call_7652,call_7660,const_7659,uop_7663,call_7669,])
func_7672 = relay.Function([var_7634,], output)
mod['func_7672'] = func_7672
mod = relay.transform.InferType()(mod)
var_7673 = relay.var("var_7673", dtype = "int16", shape = ())#candidate|7673|()|var|int16
output = func_7672(var_7673)
func_7674 = relay.Function([var_7673], output)
mutated_mod['func_7674'] = func_7674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4595_call = mod.get_global_var('func_4595')
func_4597_call = mutated_mod.get_global_var('func_4597')
call_7681 = func_4595_call()
call_7682 = func_4595_call()
output = relay.Tuple([call_7681,])
output2 = relay.Tuple([call_7682,])
func_7693 = relay.Function([], output)
mod['func_7693'] = func_7693
mod = relay.transform.InferType()(mod)
output = func_7693()
func_7694 = relay.Function([], output)
mutated_mod['func_7694'] = func_7694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5033_call = mod.get_global_var('func_5033')
func_5034_call = mutated_mod.get_global_var('func_5034')
call_7707 = relay.TupleGetItem(func_5033_call(), 0)
call_7708 = relay.TupleGetItem(func_5034_call(), 0)
func_5590_call = mod.get_global_var('func_5590')
func_5592_call = mutated_mod.get_global_var('func_5592')
call_7731 = relay.TupleGetItem(func_5590_call(), 0)
call_7732 = relay.TupleGetItem(func_5592_call(), 0)
func_556_call = mod.get_global_var('func_556')
func_559_call = mutated_mod.get_global_var('func_559')
var_7734 = relay.var("var_7734", dtype = "float64", shape = (1568,))#candidate|7734|(1568,)|var|float64
call_7733 = relay.TupleGetItem(func_556_call(relay.reshape(var_7734.astype('float64'), [1568,])), 1)
call_7735 = relay.TupleGetItem(func_559_call(relay.reshape(var_7734.astype('float64'), [1568,])), 1)
uop_7745 = relay.log10(call_7733.astype('float64')) # shape=(4, 4, 16)
uop_7747 = relay.log10(call_7735.astype('float64')) # shape=(4, 4, 16)
output = relay.Tuple([call_7707,call_7731,var_7734,uop_7745,])
output2 = relay.Tuple([call_7708,call_7732,var_7734,uop_7747,])
func_7761 = relay.Function([var_7734,], output)
mod['func_7761'] = func_7761
mod = relay.transform.InferType()(mod)
var_7762 = relay.var("var_7762", dtype = "float64", shape = (1568,))#candidate|7762|(1568,)|var|float64
output = func_7761(var_7762)
func_7763 = relay.Function([var_7762], output)
mutated_mod['func_7763'] = func_7763
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7783 = relay.var("var_7783", dtype = "uint8", shape = (16, 7, 10))#candidate|7783|(16, 7, 10)|var|uint8
var_7784 = relay.var("var_7784", dtype = "uint8", shape = (16, 7, 10))#candidate|7784|(16, 7, 10)|var|uint8
bop_7785 = relay.bitwise_xor(var_7783.astype('uint8'), relay.reshape(var_7784.astype('uint8'), relay.shape_of(var_7783))) # shape=(16, 7, 10)
func_7693_call = mod.get_global_var('func_7693')
func_7694_call = mutated_mod.get_global_var('func_7694')
call_7791 = relay.TupleGetItem(func_7693_call(), 0)
call_7792 = relay.TupleGetItem(func_7694_call(), 0)
func_4859_call = mod.get_global_var('func_4859')
func_4863_call = mutated_mod.get_global_var('func_4863')
var_7814 = relay.var("var_7814", dtype = "int64", shape = (504,))#candidate|7814|(504,)|var|int64
call_7813 = relay.TupleGetItem(func_4859_call(relay.reshape(var_7814.astype('int64'), [8, 9, 7]), relay.reshape(var_7814.astype('int64'), [8, 9, 7]), ), 1)
call_7815 = relay.TupleGetItem(func_4863_call(relay.reshape(var_7814.astype('int64'), [8, 9, 7]), relay.reshape(var_7814.astype('int64'), [8, 9, 7]), ), 1)
var_7828 = relay.var("var_7828", dtype = "bool", shape = (8, 9, 7))#candidate|7828|(8, 9, 7)|var|bool
bop_7829 = relay.mod(call_7813.astype('float32'), relay.reshape(var_7828.astype('float32'), relay.shape_of(call_7813))) # shape=(8, 9, 7)
bop_7832 = relay.mod(call_7815.astype('float32'), relay.reshape(var_7828.astype('float32'), relay.shape_of(call_7815))) # shape=(8, 9, 7)
output = relay.Tuple([bop_7785,call_7791,var_7814,bop_7829,])
output2 = relay.Tuple([bop_7785,call_7792,var_7814,bop_7832,])
func_7841 = relay.Function([var_7783,var_7784,var_7814,var_7828,], output)
mod['func_7841'] = func_7841
mod = relay.transform.InferType()(mod)
var_7842 = relay.var("var_7842", dtype = "uint8", shape = (16, 7, 10))#candidate|7842|(16, 7, 10)|var|uint8
var_7843 = relay.var("var_7843", dtype = "uint8", shape = (16, 7, 10))#candidate|7843|(16, 7, 10)|var|uint8
var_7844 = relay.var("var_7844", dtype = "int64", shape = (504,))#candidate|7844|(504,)|var|int64
var_7845 = relay.var("var_7845", dtype = "bool", shape = (8, 9, 7))#candidate|7845|(8, 9, 7)|var|bool
output = func_7841(var_7842,var_7843,var_7844,var_7845,)
func_7846 = relay.Function([var_7842,var_7843,var_7844,var_7845,], output)
mutated_mod['func_7846'] = func_7846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_720_call = mod.get_global_var('func_720')
func_721_call = mutated_mod.get_global_var('func_721')
call_7883 = func_720_call()
call_7884 = func_720_call()
func_794_call = mod.get_global_var('func_794')
func_796_call = mutated_mod.get_global_var('func_796')
const_7891 = relay.const([-2.200954,-1.595258,4.401886,8.711773,-9.340080,-2.900805,-5.968886,9.095826,-5.631203,9.929962,1.708266,1.986410,8.672015,9.501554,1.326430,-8.577922,1.399579,2.882946,2.804988,4.200617,-7.628609,1.827732,9.676989,-0.001919,-5.925224,4.850587,-1.521436,4.959574,-0.717007,-9.598941,-0.007895,9.212696], dtype = "float64")#candidate|7891|(32,)|const|float64
call_7890 = relay.TupleGetItem(func_794_call(relay.reshape(const_7891.astype('float64'), [32,])), 2)
call_7892 = relay.TupleGetItem(func_796_call(relay.reshape(const_7891.astype('float64'), [32,])), 2)
var_7904 = relay.var("var_7904", dtype = "float64", shape = (1568,))#candidate|7904|(1568,)|var|float64
bop_7905 = relay.floor_divide(call_7890.astype('float64'), relay.reshape(var_7904.astype('float64'), relay.shape_of(call_7890))) # shape=(1568,)
bop_7908 = relay.floor_divide(call_7892.astype('float64'), relay.reshape(var_7904.astype('float64'), relay.shape_of(call_7892))) # shape=(1568,)
uop_7910 = relay.sin(bop_7905.astype('float32')) # shape=(1568,)
uop_7912 = relay.sin(bop_7908.astype('float32')) # shape=(1568,)
uop_7914 = relay.asin(uop_7910.astype('float64')) # shape=(1568,)
uop_7916 = relay.asin(uop_7912.astype('float64')) # shape=(1568,)
bop_7922 = relay.power(uop_7910.astype('float32'), relay.reshape(uop_7914.astype('float32'), relay.shape_of(uop_7910))) # shape=(1568,)
bop_7925 = relay.power(uop_7912.astype('float32'), relay.reshape(uop_7916.astype('float32'), relay.shape_of(uop_7912))) # shape=(1568,)
output = relay.Tuple([call_7883,const_7891,bop_7922,])
output2 = relay.Tuple([call_7884,const_7891,bop_7925,])
func_7951 = relay.Function([var_7904,], output)
mod['func_7951'] = func_7951
mod = relay.transform.InferType()(mod)
mutated_mod['func_7951'] = func_7951
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7952 = relay.var("var_7952", dtype = "float64", shape = (1568,))#candidate|7952|(1568,)|var|float64
func_7951_call = mutated_mod.get_global_var('func_7951')
call_7953 = func_7951_call(var_7952)
output = call_7953
func_7954 = relay.Function([var_7952], output)
mutated_mod['func_7954'] = func_7954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_7986 = func_5807_call()
call_7987 = func_5807_call()
func_6791_call = mod.get_global_var('func_6791')
func_6792_call = mutated_mod.get_global_var('func_6792')
call_7988 = func_6791_call()
call_7989 = func_6791_call()
func_482_call = mod.get_global_var('func_482')
func_484_call = mutated_mod.get_global_var('func_484')
call_7991 = relay.TupleGetItem(func_482_call(), 0)
call_7992 = relay.TupleGetItem(func_484_call(), 0)
uop_7995 = relay.sqrt(call_7988.astype('float64')) # shape=(10, 2, 16)
uop_7997 = relay.sqrt(call_7989.astype('float64')) # shape=(10, 2, 16)
output = relay.Tuple([call_7986,call_7991,uop_7995,])
output2 = relay.Tuple([call_7987,call_7992,uop_7997,])
func_8009 = relay.Function([], output)
mod['func_8009'] = func_8009
mod = relay.transform.InferType()(mod)
mutated_mod['func_8009'] = func_8009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8009_call = mutated_mod.get_global_var('func_8009')
call_8010 = func_8009_call()
output = call_8010
func_8011 = relay.Function([], output)
mutated_mod['func_8011'] = func_8011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4062_call = mod.get_global_var('func_4062')
func_4063_call = mutated_mod.get_global_var('func_4063')
call_8012 = relay.TupleGetItem(func_4062_call(), 0)
call_8013 = relay.TupleGetItem(func_4063_call(), 0)
func_6791_call = mod.get_global_var('func_6791')
func_6792_call = mutated_mod.get_global_var('func_6792')
call_8027 = func_6791_call()
call_8028 = func_6791_call()
var_8053 = relay.var("var_8053", dtype = "bool", shape = (10, 2, 16))#candidate|8053|(10, 2, 16)|var|bool
bop_8054 = relay.minimum(call_8027.astype('int64'), relay.reshape(var_8053.astype('int64'), relay.shape_of(call_8027))) # shape=(10, 2, 16)
bop_8057 = relay.minimum(call_8028.astype('int64'), relay.reshape(var_8053.astype('int64'), relay.shape_of(call_8028))) # shape=(10, 2, 16)
func_7484_call = mod.get_global_var('func_7484')
func_7487_call = mutated_mod.get_global_var('func_7487')
var_8059 = relay.var("var_8059", dtype = "int32", shape = (1200,))#candidate|8059|(1200,)|var|int32
call_8058 = relay.TupleGetItem(func_7484_call(relay.reshape(var_8059.astype('int32'), [5, 15, 16]), relay.reshape(var_8059.astype('int32'), [5, 15, 16]), ), 1)
call_8060 = relay.TupleGetItem(func_7487_call(relay.reshape(var_8059.astype('int32'), [5, 15, 16]), relay.reshape(var_8059.astype('int32'), [5, 15, 16]), ), 1)
output = relay.Tuple([call_8012,bop_8054,call_8058,var_8059,])
output2 = relay.Tuple([call_8013,bop_8057,call_8060,var_8059,])
func_8073 = relay.Function([var_8053,var_8059,], output)
mod['func_8073'] = func_8073
mod = relay.transform.InferType()(mod)
mutated_mod['func_8073'] = func_8073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8073_call = mutated_mod.get_global_var('func_8073')
var_8075 = relay.var("var_8075", dtype = "bool", shape = (10, 2, 16))#candidate|8075|(10, 2, 16)|var|bool
var_8076 = relay.var("var_8076", dtype = "int32", shape = (1200,))#candidate|8076|(1200,)|var|int32
call_8074 = func_8073_call(var_8075,var_8076,)
output = call_8074
func_8077 = relay.Function([var_8075,var_8076,], output)
mutated_mod['func_8077'] = func_8077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1466_call = mod.get_global_var('func_1466')
func_1467_call = mutated_mod.get_global_var('func_1467')
call_8103 = relay.TupleGetItem(func_1466_call(), 0)
call_8104 = relay.TupleGetItem(func_1467_call(), 0)
uop_8112 = relay.sqrt(call_8103.astype('float64')) # shape=(2, 2, 14)
uop_8114 = relay.sqrt(call_8104.astype('float64')) # shape=(2, 2, 14)
output = relay.Tuple([uop_8112,])
output2 = relay.Tuple([uop_8114,])
func_8138 = relay.Function([], output)
mod['func_8138'] = func_8138
mod = relay.transform.InferType()(mod)
output = func_8138()
func_8139 = relay.Function([], output)
mutated_mod['func_8139'] = func_8139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8142 = relay.var("var_8142", dtype = "float64", shape = (3, 15, 5))#candidate|8142|(3, 15, 5)|var|float64
uop_8143 = relay.rsqrt(var_8142.astype('float64')) # shape=(3, 15, 5)
uop_8147 = relay.asinh(uop_8143.astype('float64')) # shape=(3, 15, 5)
bop_8153 = relay.equal(uop_8147.astype('bool'), relay.reshape(uop_8143.astype('bool'), relay.shape_of(uop_8147))) # shape=(3, 15, 5)
func_5928_call = mod.get_global_var('func_5928')
func_5930_call = mutated_mod.get_global_var('func_5930')
call_8172 = func_5928_call()
call_8173 = func_5928_call()
func_4679_call = mod.get_global_var('func_4679')
func_4681_call = mutated_mod.get_global_var('func_4681')
const_8175 = relay.const([-8.699082,4.587927,-8.531086,7.469344,5.216792,2.124938,5.453787,6.856874,-2.231394,-0.017067,2.048597,-7.358919,-4.844873,-3.523451,-1.200403,8.418963,-4.525498,-6.222241,-1.382381,-3.157801,-0.741239,8.330973,1.198234,-8.061007,1.008154,-2.342463,-3.506900,1.704963,1.503055,-3.190243,6.479119,-1.778537,-1.946889,3.876133,3.614883,-4.224477,1.989211,3.524523,-9.172254,-7.879886,-3.450075,-6.615683,-8.369144,7.893798,3.100172,7.633823,1.255097,5.322857,-4.798144,6.162784,-5.028452,9.823657,7.939106,-6.751442,-8.897049,0.542948,7.027390,1.364617,8.878241,9.940354,-8.238671,-0.059930,0.757790,3.739395,-9.473855,7.814410,3.157413,-9.081069,2.044152,-0.234833,-9.281182,2.136756,-8.249979,2.016403,7.304834,-6.927780,4.139021,-0.148658,-8.819762,-7.598872,-2.317507,3.842953,-6.362551,-3.208978,-4.850141,8.956657,4.761875,3.298527,5.461226,3.721594,3.493670,-4.290706,-2.774703,1.077222,-2.090628,1.280591,9.805544,-2.425402,1.994386,-1.771230,-3.421018,-5.521833,-9.066187,2.637939,-3.835222,-2.409202,-0.898051,-9.045998,3.137113,-0.071316,7.293123,-5.928445,-0.343341,-8.047628,-7.773532,-0.422999,-1.531233,-5.851124,-3.285943,-2.589040,-8.451126,-1.428983,7.015712,-6.376837,3.423465,-8.150863,-2.267885,4.882314,-3.218833,-5.240388,-8.961709,8.557515,1.475644,2.006253,8.954806,-9.279136,5.379639,-1.189071,6.967771,3.979346,9.573876,7.396653,0.121760,7.290647,-4.707990,-9.756635,-2.897846,9.945750,2.233016,6.554939,-7.229067,-5.922525,-2.040888,-1.187727,8.495758,-7.838477,-7.125620,3.510183,2.481845,6.893934], dtype = "float32")#candidate|8175|(160,)|const|float32
call_8174 = relay.TupleGetItem(func_4679_call(relay.reshape(const_8175.astype('float32'), [160,])), 2)
call_8176 = relay.TupleGetItem(func_4681_call(relay.reshape(const_8175.astype('float32'), [160,])), 2)
func_1545_call = mod.get_global_var('func_1545')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_8178 = relay.TupleGetItem(func_1545_call(), 0)
call_8179 = relay.TupleGetItem(func_1546_call(), 0)
func_3732_call = mod.get_global_var('func_3732')
func_3734_call = mutated_mod.get_global_var('func_3734')
var_8182 = relay.var("var_8182", dtype = "float64", shape = (512,))#candidate|8182|(512,)|var|float64
call_8181 = relay.TupleGetItem(func_3732_call(relay.reshape(var_8182.astype('float64'), [16, 2, 16])), 1)
call_8183 = relay.TupleGetItem(func_3734_call(relay.reshape(var_8182.astype('float64'), [16, 2, 16])), 1)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_8184 = func_5807_call()
call_8185 = func_5807_call()
output = relay.Tuple([bop_8153,call_8172,call_8174,const_8175,call_8178,call_8181,var_8182,call_8184,])
output2 = relay.Tuple([bop_8153,call_8173,call_8176,const_8175,call_8179,call_8183,var_8182,call_8185,])
func_8186 = relay.Function([var_8142,var_8182,], output)
mod['func_8186'] = func_8186
mod = relay.transform.InferType()(mod)
var_8187 = relay.var("var_8187", dtype = "float64", shape = (3, 15, 5))#candidate|8187|(3, 15, 5)|var|float64
var_8188 = relay.var("var_8188", dtype = "float64", shape = (512,))#candidate|8188|(512,)|var|float64
output = func_8186(var_8187,var_8188,)
func_8189 = relay.Function([var_8187,var_8188,], output)
mutated_mod['func_8189'] = func_8189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8138_call = mod.get_global_var('func_8138')
func_8139_call = mutated_mod.get_global_var('func_8139')
call_8204 = relay.TupleGetItem(func_8138_call(), 0)
call_8205 = relay.TupleGetItem(func_8139_call(), 0)
func_697_call = mod.get_global_var('func_697')
func_701_call = mutated_mod.get_global_var('func_701')
const_8209 = relay.const(3.491403, dtype = "float64")#candidate|8209|()|const|float64
var_8210 = relay.var("var_8210", dtype = "float64", shape = (3360,))#candidate|8210|(3360,)|var|float64
call_8208 = relay.TupleGetItem(func_697_call(relay.reshape(const_8209.astype('float64'), []), relay.reshape(var_8210.astype('float64'), [16, 15, 14]), ), 0)
call_8211 = relay.TupleGetItem(func_701_call(relay.reshape(const_8209.astype('float64'), []), relay.reshape(var_8210.astype('float64'), [16, 15, 14]), ), 0)
func_4502_call = mod.get_global_var('func_4502')
func_4506_call = mutated_mod.get_global_var('func_4506')
const_8224 = relay.const([-8.735924,5.419299,9.891637,4.329417,5.671784,7.369278,-7.818616,-4.974327,9.186045,-5.950163,5.221447,-9.842638,-0.665064,-9.197972,-7.247957,9.459918,5.955839,-5.893452,2.437855,6.366147,-7.201776,-9.079454,3.260831,4.628201,-2.171433,4.431998,2.319157,-8.650012,-6.940174,2.674543,8.716375,6.741084], dtype = "float64")#candidate|8224|(32,)|const|float64
call_8223 = relay.TupleGetItem(func_4502_call(relay.reshape(const_8224.astype('float64'), [32,]), relay.reshape(const_8224.astype('float64'), [32,]), ), 0)
call_8225 = relay.TupleGetItem(func_4506_call(relay.reshape(const_8224.astype('float64'), [32,]), relay.reshape(const_8224.astype('float64'), [32,]), ), 0)
bop_8233 = relay.logical_and(const_8224.astype('bool'), const_8209.astype('bool')) # shape=(32,)
output = relay.Tuple([call_8204,call_8208,var_8210,call_8223,bop_8233,])
output2 = relay.Tuple([call_8205,call_8211,var_8210,call_8225,bop_8233,])
func_8249 = relay.Function([var_8210,], output)
mod['func_8249'] = func_8249
mod = relay.transform.InferType()(mod)
var_8250 = relay.var("var_8250", dtype = "float64", shape = (3360,))#candidate|8250|(3360,)|var|float64
output = func_8249(var_8250)
func_8251 = relay.Function([var_8250], output)
mutated_mod['func_8251'] = func_8251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3798_call = mod.get_global_var('func_3798')
func_3800_call = mutated_mod.get_global_var('func_3800')
call_8273 = relay.TupleGetItem(func_3798_call(), 0)
call_8274 = relay.TupleGetItem(func_3800_call(), 0)
output = call_8273
output2 = call_8274
func_8284 = relay.Function([], output)
mod['func_8284'] = func_8284
mod = relay.transform.InferType()(mod)
mutated_mod['func_8284'] = func_8284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8284_call = mutated_mod.get_global_var('func_8284')
call_8285 = func_8284_call()
output = call_8285
func_8286 = relay.Function([], output)
mutated_mod['func_8286'] = func_8286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2924_call = mod.get_global_var('func_2924')
func_2926_call = mutated_mod.get_global_var('func_2926')
call_8329 = relay.TupleGetItem(func_2924_call(), 0)
call_8330 = relay.TupleGetItem(func_2926_call(), 0)
var_8332 = relay.var("var_8332", dtype = "float32", shape = (8, 2, 16))#candidate|8332|(8, 2, 16)|var|float32
bop_8333 = relay.maximum(call_8329.astype('int16'), var_8332.astype('int16')) # shape=(8, 2, 16)
bop_8336 = relay.maximum(call_8330.astype('int16'), var_8332.astype('int16')) # shape=(8, 2, 16)
var_8355 = relay.var("var_8355", dtype = "float32", shape = (8, 2, 16))#candidate|8355|(8, 2, 16)|var|float32
bop_8356 = relay.power(var_8332.astype('float32'), relay.reshape(var_8355.astype('float32'), relay.shape_of(var_8332))) # shape=(8, 2, 16)
output = relay.Tuple([bop_8333,bop_8356,])
output2 = relay.Tuple([bop_8336,bop_8356,])
func_8364 = relay.Function([var_8332,var_8355,], output)
mod['func_8364'] = func_8364
mod = relay.transform.InferType()(mod)
mutated_mod['func_8364'] = func_8364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8364_call = mutated_mod.get_global_var('func_8364')
var_8366 = relay.var("var_8366", dtype = "float32", shape = (8, 2, 16))#candidate|8366|(8, 2, 16)|var|float32
var_8367 = relay.var("var_8367", dtype = "float32", shape = (8, 2, 16))#candidate|8367|(8, 2, 16)|var|float32
call_8365 = func_8364_call(var_8366,var_8367,)
output = call_8365
func_8368 = relay.Function([var_8366,var_8367,], output)
mutated_mod['func_8368'] = func_8368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6684_call = mod.get_global_var('func_6684')
func_6686_call = mutated_mod.get_global_var('func_6686')
call_8382 = relay.TupleGetItem(func_6684_call(), 2)
call_8383 = relay.TupleGetItem(func_6686_call(), 2)
output = relay.Tuple([call_8382,])
output2 = relay.Tuple([call_8383,])
func_8400 = relay.Function([], output)
mod['func_8400'] = func_8400
mod = relay.transform.InferType()(mod)
mutated_mod['func_8400'] = func_8400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8400_call = mutated_mod.get_global_var('func_8400')
call_8401 = func_8400_call()
output = call_8401
func_8402 = relay.Function([], output)
mutated_mod['func_8402'] = func_8402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2052_call = mod.get_global_var('func_2052')
func_2054_call = mutated_mod.get_global_var('func_2054')
call_8487 = relay.TupleGetItem(func_2052_call(), 0)
call_8488 = relay.TupleGetItem(func_2054_call(), 0)
const_8500 = relay.const([[[False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True],[False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False]],[[False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False],[True,True,True,False,False,False,False,False,True,False,False,True,False,True,True,True]]], dtype = "bool")#candidate|8500|(2, 2, 16)|const|bool
bop_8501 = relay.right_shift(call_8487.astype('int64'), const_8500.astype('int64')) # shape=(2, 2, 16)
bop_8504 = relay.right_shift(call_8488.astype('int64'), const_8500.astype('int64')) # shape=(2, 2, 16)
output = relay.Tuple([bop_8501,])
output2 = relay.Tuple([bop_8504,])
func_8505 = relay.Function([], output)
mod['func_8505'] = func_8505
mod = relay.transform.InferType()(mod)
mutated_mod['func_8505'] = func_8505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8505_call = mutated_mod.get_global_var('func_8505')
call_8506 = func_8505_call()
output = call_8506
func_8507 = relay.Function([], output)
mutated_mod['func_8507'] = func_8507
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8518 = relay.const([[[4.923869,0.115777,-8.373153,1.829093,0.239113,9.244411,6.188618],[-4.769577,-1.043389,-4.970787,7.395459,3.198695,2.604590,0.720006]],[[-3.973403,9.219986,4.448250,6.587396,-8.704540,-1.439015,0.738477],[-5.292530,7.907559,5.651965,-6.271802,-7.764620,-1.991428,-8.683707]],[[7.406336,-0.106185,-9.139947,4.737447,-6.906299,8.900314,7.914834],[7.770239,-1.543092,-3.808474,-7.382838,3.225162,5.857796,-7.574596]]], dtype = "float64")#candidate|8518|(3, 2, 7)|const|float64
uop_8519 = relay.atanh(const_8518.astype('float64')) # shape=(3, 2, 7)
output = uop_8519
output2 = uop_8519
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
	relay.transform.LazyGradientInit(),
	relay.transform.PartialEvaluate(),
	relay.transform.Legalize(),
	relay.transform.FoldConstant(),
	relay.transform.ToANormalForm(),
	relay.transform.ToGraphNormalForm(),
	relay.transform.SimplifyInference(),
	relay.transform.ToBasicBlockNormalForm(),
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
