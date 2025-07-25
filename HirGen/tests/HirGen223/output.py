import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_224 = relay.const([[[-8.433188,-9.534578,-2.506446],[-9.722130,-9.899712,0.746946],[-0.466511,-5.966147,1.303537],[-2.122351,-1.190066,4.155217],[-6.371629,5.298627,3.537788],[4.747671,5.581013,-6.909149],[-1.423879,5.748013,4.527284]]], dtype = "float32")#candidate|224|(1, 7, 3)|const|float32
const_225 = relay.const([[[8.963076,-1.942844,-7.794624],[-4.235286,-8.137717,-0.623061],[-9.408038,-8.045944,6.550436],[3.225939,-7.332290,-8.627483],[-8.729238,-5.755382,-2.417399],[-0.083125,-1.464776,3.652922],[5.535740,-6.288352,1.700413]],[[7.789812,-9.284501,0.409568],[-6.489597,-3.677450,-2.673115],[-8.651149,-6.971816,3.023923],[-9.540737,-9.252037,-9.006598],[0.877641,2.356299,6.874970],[-0.394632,-9.754811,1.699133],[-6.945256,-8.328779,-9.735885]],[[-7.932146,9.678891,6.214148],[3.081089,-4.440031,-1.474816],[1.860413,-4.912712,9.465606],[6.914868,8.505284,0.476531],[-0.099257,-5.866495,-3.421538],[8.298319,6.660547,2.628951],[-7.974586,9.910367,-1.015442]],[[1.759407,1.507484,-7.152009],[-6.601937,4.355553,6.452912],[-2.114556,-4.029303,-8.119683],[3.954639,7.136983,-1.613583],[3.339651,1.883333,-9.241343],[-3.377387,-1.463896,0.421758],[-0.268740,-7.524730,2.067073]],[[-1.275328,3.377801,-6.634910],[5.320154,-6.100823,8.916787],[7.761647,9.128109,9.053777],[-7.144652,9.089503,3.150707],[0.721464,-4.255901,9.990028],[6.679684,9.323457,9.746757],[-9.436099,2.296278,4.306235]],[[-3.150849,6.761182,-9.935575],[7.077597,-7.241034,6.658359],[1.865179,-1.196324,-7.387921],[-4.721082,3.855851,2.945490],[3.429182,-1.054115,-0.192565],[3.167576,-1.098372,-9.995605],[3.713171,-2.769682,-1.212002]],[[-0.218184,-7.993413,-4.750668],[-8.844464,5.533150,-5.921755],[-4.189082,-4.158448,1.210981],[3.956207,4.736280,6.547927],[-1.653316,5.566802,4.050912],[-8.644520,-9.496507,-8.291605],[5.568267,6.383195,-2.070024]],[[5.975656,1.815174,4.762950],[-7.967384,-1.762037,9.959008],[0.127059,-9.916012,-0.029701],[2.876884,9.144863,4.573303],[-4.902837,8.158126,0.313674],[6.283437,-5.408449,8.357501],[3.190053,-2.425943,5.784909]]], dtype = "float32")#candidate|225|(8, 7, 3)|const|float32
bop_226 = relay.floor_mod(const_224.astype('float32'), const_225.astype('float32')) # shape=(8, 7, 3)
bop_255 = relay.bitwise_or(const_224.astype('int32'), const_225.astype('int32')) # shape=(8, 7, 3)
output = relay.Tuple([bop_226,bop_255,])
output2 = relay.Tuple([bop_226,bop_255,])
func_273 = relay.Function([], output)
mod['func_273'] = func_273
mod = relay.transform.InferType()(mod)
mutated_mod['func_273'] = func_273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_273_call = mutated_mod.get_global_var('func_273')
call_274 = func_273_call()
output = call_274
func_275 = relay.Function([], output)
mutated_mod['func_275'] = func_275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_315 = relay.TupleGetItem(func_273_call(), 1)
call_316 = relay.TupleGetItem(func_275_call(), 1)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_319 = relay.TupleGetItem(func_273_call(), 1)
call_320 = relay.TupleGetItem(func_275_call(), 1)
output = relay.Tuple([call_315,call_319,])
output2 = relay.Tuple([call_316,call_320,])
func_329 = relay.Function([], output)
mod['func_329'] = func_329
mod = relay.transform.InferType()(mod)
output = func_329()
func_330 = relay.Function([], output)
mutated_mod['func_330'] = func_330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_331 = relay.TupleGetItem(func_273_call(), 0)
call_332 = relay.TupleGetItem(func_275_call(), 0)
const_344 = relay.const([[[6.247124,-8.240173,-0.915224],[-2.360272,2.446449,0.214481],[-6.470068,9.872539,-7.293389],[-1.310917,-6.481783,2.000526],[-2.894382,-9.910221,-5.991661],[4.660661,2.918587,4.256630],[9.254444,2.416454,-0.556699]],[[-7.836058,-6.228556,-4.497752],[1.530802,-3.457443,5.863434],[2.020462,-0.296740,3.634846],[6.583025,-1.791437,7.246099],[9.148475,5.353989,9.722074],[8.829660,-7.986272,5.297042],[-9.899895,5.029230,-3.009729]],[[-6.924494,-5.132148,4.202678],[3.921364,5.795213,-7.794084],[7.344483,2.724044,-2.525517],[7.560679,-5.824246,-4.250886],[-9.757810,-7.980608,9.977521],[-1.622392,5.730755,-2.030145],[1.897285,4.828583,2.894307]],[[0.452701,0.842980,0.933684],[2.789333,3.660845,1.248040],[-6.446795,-7.257000,7.046648],[0.624421,8.079847,6.125227],[-1.175491,5.072361,6.636781],[8.848395,-1.014347,1.842247],[-2.122264,-0.463981,9.425819]],[[9.192067,0.012355,-6.728893],[5.198663,-3.994940,-9.809552],[-3.639050,-8.993569,0.938885],[-0.071533,-2.560079,1.174900],[8.658713,4.518356,-8.236826],[4.780798,-5.032121,4.475838],[3.833888,-2.272594,-0.914946]],[[2.875148,8.313890,-9.105583],[8.140910,7.295683,8.083100],[-7.625291,8.508235,-2.616332],[-1.121300,1.452371,-1.340001],[1.885793,-7.077614,-8.113932],[6.889330,7.545239,1.753177],[7.859531,9.951362,4.919819]],[[0.767567,1.995306,4.649453],[-4.693850,1.376859,-4.369091],[4.066175,9.375688,9.937586],[-9.282799,-4.188608,-1.743836],[5.396823,-9.392259,-5.003963],[-4.578919,7.165980,-2.658008],[9.424976,-3.653586,4.077348]],[[7.018223,2.391534,-2.211588],[-5.974487,8.096270,-6.324165],[-8.430758,2.056716,-4.067525],[-2.931931,4.668176,-2.048405],[-4.753652,6.632979,-7.162167],[9.340565,9.973977,5.832337],[-5.089455,-6.047022,-4.479281]]], dtype = "float32")#candidate|344|(8, 7, 3)|const|float32
bop_345 = relay.logical_or(call_331.astype('bool'), relay.reshape(const_344.astype('bool'), relay.shape_of(call_331))) # shape=(8, 7, 3)
bop_348 = relay.logical_or(call_332.astype('bool'), relay.reshape(const_344.astype('bool'), relay.shape_of(call_332))) # shape=(8, 7, 3)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_358 = relay.TupleGetItem(func_329_call(), 1)
call_359 = relay.TupleGetItem(func_330_call(), 1)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_360 = relay.TupleGetItem(func_273_call(), 1)
call_361 = relay.TupleGetItem(func_275_call(), 1)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_367 = relay.TupleGetItem(func_273_call(), 0)
call_368 = relay.TupleGetItem(func_275_call(), 0)
output = relay.Tuple([bop_345,call_358,call_360,call_367,])
output2 = relay.Tuple([bop_348,call_359,call_361,call_368,])
func_377 = relay.Function([], output)
mod['func_377'] = func_377
mod = relay.transform.InferType()(mod)
mutated_mod['func_377'] = func_377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_377_call = mutated_mod.get_global_var('func_377')
call_378 = func_377_call()
output = call_378
func_379 = relay.Function([], output)
mutated_mod['func_379'] = func_379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_382 = relay.var("var_382", dtype = "float32", shape = (8, 11, 7))#candidate|382|(8, 11, 7)|var|float32
uop_383 = relay.cos(var_382.astype('float32')) # shape=(8, 11, 7)
output = relay.Tuple([uop_383,])
output2 = relay.Tuple([uop_383,])
func_385 = relay.Function([var_382,], output)
mod['func_385'] = func_385
mod = relay.transform.InferType()(mod)
var_386 = relay.var("var_386", dtype = "float32", shape = (8, 11, 7))#candidate|386|(8, 11, 7)|var|float32
output = func_385(var_386)
func_387 = relay.Function([var_386], output)
mutated_mod['func_387'] = func_387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_445 = relay.TupleGetItem(func_273_call(), 0)
call_446 = relay.TupleGetItem(func_275_call(), 0)
output = call_445
output2 = call_446
func_449 = relay.Function([], output)
mod['func_449'] = func_449
mod = relay.transform.InferType()(mod)
output = func_449()
func_450 = relay.Function([], output)
mutated_mod['func_450'] = func_450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_471 = relay.var("var_471", dtype = "uint8", shape = ())#candidate|471|()|var|uint8
var_472 = relay.var("var_472", dtype = "uint8", shape = (2, 15, 9))#candidate|472|(2, 15, 9)|var|uint8
bop_473 = relay.maximum(var_471.astype('uint8'), var_472.astype('uint8')) # shape=(2, 15, 9)
output = relay.Tuple([bop_473,])
output2 = relay.Tuple([bop_473,])
func_486 = relay.Function([var_471,var_472,], output)
mod['func_486'] = func_486
mod = relay.transform.InferType()(mod)
mutated_mod['func_486'] = func_486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_486_call = mutated_mod.get_global_var('func_486')
var_488 = relay.var("var_488", dtype = "uint8", shape = ())#candidate|488|()|var|uint8
var_489 = relay.var("var_489", dtype = "uint8", shape = (2, 15, 9))#candidate|489|(2, 15, 9)|var|uint8
call_487 = func_486_call(var_488,var_489,)
output = call_487
func_490 = relay.Function([var_488,var_489,], output)
mutated_mod['func_490'] = func_490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_450_call = mutated_mod.get_global_var('func_450')
call_492 = func_449_call()
call_493 = func_449_call()
output = relay.Tuple([call_492,])
output2 = relay.Tuple([call_493,])
func_505 = relay.Function([], output)
mod['func_505'] = func_505
mod = relay.transform.InferType()(mod)
mutated_mod['func_505'] = func_505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_505_call = mutated_mod.get_global_var('func_505')
call_506 = func_505_call()
output = call_506
func_507 = relay.Function([], output)
mutated_mod['func_507'] = func_507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_585 = relay.TupleGetItem(func_329_call(), 0)
call_586 = relay.TupleGetItem(func_330_call(), 0)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_587 = relay.TupleGetItem(func_329_call(), 1)
call_588 = relay.TupleGetItem(func_330_call(), 1)
bop_594 = relay.right_shift(call_587.astype('uint8'), relay.reshape(call_585.astype('uint8'), relay.shape_of(call_587))) # shape=(8, 7, 3)
bop_597 = relay.right_shift(call_588.astype('uint8'), relay.reshape(call_586.astype('uint8'), relay.shape_of(call_588))) # shape=(8, 7, 3)
uop_616 = relay.sinh(call_587.astype('float32')) # shape=(8, 7, 3)
uop_618 = relay.sinh(call_588.astype('float32')) # shape=(8, 7, 3)
output = relay.Tuple([bop_594,uop_616,])
output2 = relay.Tuple([bop_597,uop_618,])
func_621 = relay.Function([], output)
mod['func_621'] = func_621
mod = relay.transform.InferType()(mod)
output = func_621()
func_622 = relay.Function([], output)
mutated_mod['func_622'] = func_622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_450_call = mutated_mod.get_global_var('func_450')
call_631 = func_449_call()
call_632 = func_449_call()
uop_644 = relay.atan(call_631.astype('float64')) # shape=(8, 7, 3)
uop_646 = relay.atan(call_632.astype('float64')) # shape=(8, 7, 3)
output = relay.Tuple([uop_644,])
output2 = relay.Tuple([uop_646,])
func_656 = relay.Function([], output)
mod['func_656'] = func_656
mod = relay.transform.InferType()(mod)
output = func_656()
func_657 = relay.Function([], output)
mutated_mod['func_657'] = func_657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_450_call = mutated_mod.get_global_var('func_450')
call_709 = func_449_call()
call_710 = func_449_call()
func_621_call = mod.get_global_var('func_621')
func_622_call = mutated_mod.get_global_var('func_622')
call_721 = relay.TupleGetItem(func_621_call(), 1)
call_722 = relay.TupleGetItem(func_622_call(), 1)
bop_723 = relay.logical_xor(call_721.astype('uint16'), relay.reshape(call_709.astype('uint16'), relay.shape_of(call_721))) # shape=(8, 7, 3)
bop_726 = relay.logical_xor(call_722.astype('uint16'), relay.reshape(call_710.astype('uint16'), relay.shape_of(call_722))) # shape=(8, 7, 3)
uop_727 = relay.sigmoid(call_709.astype('float64')) # shape=(8, 7, 3)
uop_729 = relay.sigmoid(call_710.astype('float64')) # shape=(8, 7, 3)
uop_737 = relay.tan(uop_727.astype('float32')) # shape=(8, 7, 3)
uop_739 = relay.tan(uop_729.astype('float32')) # shape=(8, 7, 3)
output = relay.Tuple([bop_723,uop_737,])
output2 = relay.Tuple([bop_726,uop_739,])
func_740 = relay.Function([], output)
mod['func_740'] = func_740
mod = relay.transform.InferType()(mod)
mutated_mod['func_740'] = func_740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_740_call = mutated_mod.get_global_var('func_740')
call_741 = func_740_call()
output = call_741
func_742 = relay.Function([], output)
mutated_mod['func_742'] = func_742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_774 = relay.TupleGetItem(func_273_call(), 1)
call_775 = relay.TupleGetItem(func_275_call(), 1)
output = relay.Tuple([call_774,])
output2 = relay.Tuple([call_775,])
func_776 = relay.Function([], output)
mod['func_776'] = func_776
mod = relay.transform.InferType()(mod)
mutated_mod['func_776'] = func_776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mutated_mod.get_global_var('func_776')
call_777 = func_776_call()
output = call_777
func_778 = relay.Function([], output)
mutated_mod['func_778'] = func_778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_818 = relay.TupleGetItem(func_776_call(), 0)
call_819 = relay.TupleGetItem(func_778_call(), 0)
uop_825 = relay.rsqrt(call_818.astype('float64')) # shape=(8, 7, 3)
uop_827 = relay.rsqrt(call_819.astype('float64')) # shape=(8, 7, 3)
func_656_call = mod.get_global_var('func_656')
func_657_call = mutated_mod.get_global_var('func_657')
call_854 = relay.TupleGetItem(func_656_call(), 0)
call_855 = relay.TupleGetItem(func_657_call(), 0)
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_862 = relay.TupleGetItem(func_377_call(), 3)
call_863 = relay.TupleGetItem(func_379_call(), 3)
output = relay.Tuple([uop_825,call_854,call_862,])
output2 = relay.Tuple([uop_827,call_855,call_863,])
func_869 = relay.Function([], output)
mod['func_869'] = func_869
mod = relay.transform.InferType()(mod)
mutated_mod['func_869'] = func_869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_869_call = mutated_mod.get_global_var('func_869')
call_870 = func_869_call()
output = call_870
func_871 = relay.Function([], output)
mutated_mod['func_871'] = func_871
mutated_mod = relay.transform.InferType()(mutated_mod)
const_914 = relay.const([[[7.343899,1.465472,6.464311,-6.661192,-5.152216,6.026701,5.017060,3.164766],[0.847724,8.093903,-5.365423,-4.080739,7.969031,-1.791207,8.887898,-3.952213],[6.599965,-3.821204,2.775709,-7.002426,8.651386,-3.355076,-1.601693,3.242780],[-7.165825,-9.088318,9.625885,1.566232,5.355422,-1.306307,-1.224979,2.699207],[-9.305841,-2.792026,7.460014,-7.966923,-9.207777,5.766120,-5.709161,-0.594800],[0.388218,9.998839,3.512194,2.095416,-4.323023,-8.848141,-3.273095,-7.425626],[1.233313,-7.403208,-1.942074,8.503871,-2.706415,0.046289,-9.297342,6.879448],[-8.257759,-2.305832,-5.454010,7.706085,7.562887,0.558498,9.648756,-8.920585],[-6.819356,3.046262,7.341543,-1.785795,-9.463733,-4.329517,5.205578,-0.529495],[-3.810856,-9.347647,5.122763,8.839067,1.609093,-4.332283,8.565734,6.605965]],[[-8.672099,-6.141793,-4.534272,9.607945,-5.790180,7.982197,1.981504,-1.872968],[-9.872529,-5.764039,-8.756904,-5.346981,-4.534578,-9.406086,5.643154,-6.437796],[0.209261,-0.266837,6.866668,-5.106788,5.154304,0.120213,2.912104,9.352833],[-5.171476,7.317575,6.946767,-5.432793,2.090284,9.916143,1.411199,-9.136053],[-3.340542,-3.597248,-0.111168,-0.427503,-1.133557,-4.797995,4.772148,6.777907],[-3.000979,-6.217929,-4.259839,9.737510,2.645466,-0.677630,-2.420768,6.298358],[4.455060,-1.651752,-9.443508,-1.778530,8.915665,7.999219,-2.885893,-8.600068],[5.883619,-2.701321,-2.487690,4.861852,5.503181,-7.754309,-1.148676,-3.761687],[5.059830,0.453590,1.546188,-1.298626,6.486387,7.230650,-8.454695,-6.603267],[-1.275530,6.593106,-4.548155,8.355219,-4.840979,-8.358736,4.683721,4.731270]],[[4.711410,9.082326,-3.715919,8.422371,8.525466,6.169524,5.644789,4.669637],[-9.872972,-0.111189,-1.136599,-9.790951,3.801061,9.023132,-7.084917,4.715331],[-3.869416,-6.474947,-2.255358,-2.974634,4.667784,1.797918,7.898349,-2.350654],[9.559164,-9.560133,-5.563228,-9.524104,0.879203,2.364642,-5.898834,-9.118931],[7.926793,6.733127,-4.255450,1.058564,6.788609,-2.792266,2.614539,7.323297],[3.755473,-9.636665,-1.644612,3.881797,8.318025,6.826751,6.713282,-1.806769],[5.077437,-6.198314,4.860237,0.753395,-5.385126,5.225921,-9.133835,-9.354748],[-6.218248,-6.797173,-4.608160,4.231268,-9.310290,0.653330,-7.619925,-7.659841],[-8.952218,0.169502,-9.483848,-7.939435,9.545932,-1.457365,-8.008897,8.187272],[-0.553913,-3.053059,-7.158780,-3.317605,-3.965533,-3.262742,0.434218,-0.098369]],[[-2.473811,5.361667,-5.953596,6.408312,1.208037,-2.723274,6.680001,-6.336023],[3.217575,-1.663268,-2.107147,-2.834936,-3.797081,7.634505,9.497838,2.040970],[-1.723223,-4.304243,0.911061,-0.863372,8.731854,-5.887892,-1.116072,-1.813795],[9.644382,4.915979,5.489431,6.921346,6.869597,3.093318,-2.718040,-3.203583],[5.341463,-1.138155,-4.461016,8.869782,4.774729,-7.978143,0.265423,2.364445],[0.560250,-7.912716,-9.702932,4.161738,4.577647,-1.940889,3.168325,-3.563122],[3.998481,5.307794,7.013821,5.142397,1.030975,-6.194386,6.844005,2.197498],[9.392726,3.632570,5.745935,6.783637,-0.897477,1.639253,-5.791850,-5.235242],[-3.530661,8.265547,1.477458,-6.438068,6.376195,5.094715,-7.711619,7.201161],[-7.599126,4.179601,2.304126,-7.517956,-1.841122,-6.813850,8.066008,-1.951019]],[[-6.629600,7.567929,-9.586600,-0.947684,5.621524,-0.673432,5.090821,4.003840],[4.104344,6.381037,3.208104,-3.848911,6.521086,-8.068303,9.931405,-7.543385],[-6.171216,9.468719,0.953793,-0.275096,6.758858,-6.227659,9.566589,4.142691],[-6.930637,4.642886,-2.428239,1.872322,-6.866224,6.121852,-3.492372,-1.151622],[2.880564,-4.687614,7.109020,4.607052,9.063600,6.294135,3.800251,0.696940],[-2.152483,2.081715,-6.319722,-5.848908,-5.326694,4.194129,-9.976909,-1.613971],[2.432688,-2.912510,3.565202,-3.294290,-4.295761,4.318596,-1.905318,1.569162],[-6.611315,3.574678,-7.192492,7.437957,6.726527,1.742097,-0.983848,-0.822461],[-7.703790,4.856889,-4.131453,8.517093,4.900611,2.586004,1.776460,-2.267916],[0.286475,6.397180,-5.097865,8.306557,1.244106,6.733423,-5.895243,1.077845]],[[-2.860340,-9.026183,-7.642495,1.704137,3.133728,0.185594,-7.220683,-4.166095],[-8.928335,5.027761,-1.392950,-6.511502,7.949217,-6.836187,0.757509,2.506117],[-6.781027,1.680399,8.346892,-3.037252,4.430659,2.083587,-9.275445,8.699421],[8.803567,6.493463,0.595099,2.702081,5.770768,-9.329175,-8.081239,-9.000573],[-1.532111,1.361727,3.064912,-4.975149,-8.630081,-6.209298,1.681149,4.749207],[-3.932816,-7.630373,-8.819361,-6.977893,5.846586,4.659113,-2.393238,-6.850729],[5.025663,-5.610997,-3.409251,7.410390,8.956628,6.999262,4.247129,9.243557],[4.292396,-3.787684,-7.337422,2.289330,4.748551,2.472930,-3.932234,-3.659106],[1.587911,-7.774744,7.601828,-8.382565,8.932375,3.573691,-0.527901,-3.643450],[1.571264,-9.369220,-8.957948,2.391012,-9.170342,8.595515,9.855290,-2.774902]],[[5.286704,-9.636421,-1.883519,3.738811,-6.943244,-9.173334,4.907066,-5.316826],[2.716216,-5.247252,-2.893678,-9.936392,-8.036569,2.332756,9.226862,2.457693],[9.306481,-1.485896,-4.965882,4.917285,-6.351835,-6.354419,7.964685,-9.605357],[5.738473,-2.483105,8.775003,-4.847374,-1.876286,0.839612,3.555543,-8.220229],[-8.272156,-8.951163,-4.933965,6.746065,4.511465,1.619626,-8.583515,-2.375013],[-7.146149,9.758014,5.063693,-8.178099,5.124698,5.283812,-3.629568,1.289624],[-5.851728,4.560279,-7.129326,-1.482033,-2.623130,-1.234038,4.281851,-8.698848],[9.338948,4.003300,5.479636,-6.208826,9.101010,1.446873,-5.668850,-5.258789],[-9.531654,7.633077,-6.629080,0.837857,1.862864,3.699064,-8.851619,1.723630],[9.310973,-9.461032,-8.631019,-4.406479,-9.893671,4.718089,-3.300442,-9.991261]],[[3.361568,5.291231,2.597273,5.294432,-6.167798,7.140437,-0.205850,-8.224338],[-3.721103,1.925095,-3.232793,-2.792697,9.387027,7.296143,-8.645712,0.855632],[1.156485,4.216762,6.464089,-1.211912,-5.654437,-6.926307,-2.626990,-5.465534],[4.956238,4.339303,1.492099,-8.893355,7.839504,0.379066,3.872630,8.669234],[6.768182,9.013981,9.654948,7.887316,-0.545222,0.423226,-4.909720,7.831728],[7.177750,0.810810,-6.212782,4.681611,6.989332,9.259814,9.063134,-5.474208],[-7.025557,8.258632,9.628345,6.792904,-9.287651,-3.869792,-8.911052,-3.192184],[-7.767934,0.012782,-0.473772,-8.095265,2.221694,-9.908694,-6.334331,6.279268],[7.265725,5.038478,5.588208,-0.848599,7.893297,7.871174,-2.192483,1.003783],[0.546563,7.213172,7.642790,-6.815006,-0.100759,-9.313274,3.642307,7.179746]],[[-5.508402,8.008763,7.576954,-5.180742,-9.138532,-1.250881,5.204206,4.761047],[-5.084678,-5.186288,-4.790947,-6.500189,-3.615415,9.000287,8.842397,-6.615575],[1.988570,3.974438,1.252882,1.852121,5.147920,-1.184673,5.613962,-8.381761],[-6.497965,-3.425950,6.023827,8.497628,8.097118,0.727288,5.140682,-2.167972],[4.840349,2.805411,4.280976,-3.017116,3.908571,-9.651508,-7.415089,-8.147912],[8.943005,6.963173,-4.292796,-2.190401,0.352253,-1.644402,4.660480,-4.770156],[-4.286048,9.885157,-0.612539,8.837971,-8.892780,5.331476,-3.207191,-0.599609],[-2.969647,-7.558752,-7.707681,-3.931506,-7.936703,5.591924,8.444914,-1.316851],[0.491474,-8.663552,7.422095,4.748265,9.674273,-1.051055,3.732273,4.202900],[-2.033943,-1.109794,7.006963,-3.444007,1.507143,8.321402,9.809390,-9.859735]],[[-9.576040,8.864376,-5.893104,8.579929,1.320220,1.272463,-4.253973,-6.463115],[-6.107160,-7.831261,9.456454,1.036713,-0.995627,2.436826,-8.695991,-3.520490],[-9.339561,-2.139527,0.992423,-4.173011,6.683790,4.781411,1.103657,-7.318346],[-1.506224,0.883008,-6.974394,-9.541156,4.441196,-6.514372,5.687973,-9.614986],[-2.603685,9.507838,3.635631,-6.178722,0.529521,-7.890496,6.924839,4.958841],[1.340564,5.818580,7.851361,-4.687583,-9.638584,1.939208,-3.250604,6.158248],[-9.911644,-1.963077,1.615477,1.109328,-3.952190,1.916215,-7.890078,0.574337],[7.471483,5.352586,-4.546579,0.646908,7.111949,-1.050942,8.985553,-5.317566],[-7.116058,1.914167,-2.572276,3.196805,-4.256043,-7.238865,1.355094,0.416997],[3.507954,7.732344,-9.244207,-1.339040,3.814992,0.502872,-3.416566,2.831203]],[[-3.502460,-3.136288,0.460933,2.690056,-1.872738,-6.814998,9.245676,-1.450460],[0.770333,-4.425676,9.302973,8.975983,-1.290604,9.547339,-5.742656,4.683220],[3.833171,4.473018,0.954447,-4.849402,2.564606,7.342802,-8.192596,4.137498],[-1.696240,-4.195110,-1.883112,-4.517185,-7.017330,5.042121,-4.164755,-6.051601],[6.228948,-9.753770,-2.199803,-5.607994,-2.402536,2.572648,-6.828627,-5.776723],[-6.104630,-5.547414,-5.695352,8.602116,-1.326444,8.567302,-0.302503,-3.603803],[-7.023339,-8.615419,7.631436,-6.363798,0.555832,0.574742,-3.080088,-1.418307],[-4.051492,1.044285,1.459970,3.169669,1.798265,5.254870,-9.847817,3.691406],[-6.282715,-3.188043,5.605994,7.707016,-6.502476,-3.572726,-4.238286,5.540885],[0.083709,6.839677,-1.666207,-9.563875,-7.056876,3.845282,4.292110,7.318936]],[[-0.726956,5.746550,-2.601763,-1.258289,2.364254,0.949480,4.171339,-4.601814],[4.963362,-3.508875,1.577444,7.460348,-7.708872,-0.351455,-4.523987,4.700403],[7.534488,-2.235355,-8.038541,-2.919751,9.951774,2.174478,9.131976,8.694321],[-7.163004,-6.400617,-9.004234,6.458508,-0.047872,-2.492558,6.847186,8.071581],[-9.477161,-5.087103,4.233681,3.372553,-2.962987,0.939545,-7.554574,-9.496522],[-5.762612,-4.909176,-3.885137,2.346926,-2.751061,5.766222,-8.857842,-8.526983],[-1.874380,6.657616,-7.533351,-7.715394,5.771790,-8.437206,-1.158206,-7.961682],[5.842466,4.635190,-1.593837,-1.377473,-4.634940,-7.682619,-6.204594,-0.319595],[1.551119,-8.668921,-8.942471,-8.782786,7.261148,8.266267,0.554576,-8.404540],[3.321723,3.465153,8.740695,-9.935527,9.543650,-7.639777,2.732774,4.822424]],[[-7.266003,-7.454220,-9.491728,-9.009692,2.330788,-0.830706,-5.464826,4.367235],[-1.795141,2.935219,-0.448707,-6.590897,2.310154,-7.262731,8.417159,8.891860],[6.462237,-3.576662,8.804087,2.214378,-5.785505,4.612650,4.785343,-8.195500],[0.959277,3.545553,2.481696,-2.280916,-4.931854,-5.563806,-0.059892,2.516805],[6.422807,8.241280,-4.978048,-6.151572,-1.114078,6.290653,-1.624818,-4.126006],[-8.844770,-7.713457,4.906338,-3.544371,0.251062,3.635097,-9.970754,9.646359],[-5.385984,-8.847726,-5.227157,4.796935,1.443545,-2.073075,1.908167,6.947490],[-9.164893,8.256965,-4.487705,8.614580,-4.815389,5.413248,8.771506,5.924877],[-4.047987,-7.810681,-7.596807,9.038813,9.692942,8.213774,-1.502343,-7.358575],[-3.007538,-9.413657,3.876217,-7.020283,-6.525849,-8.469349,0.432025,8.824009]],[[-2.726468,-9.374738,-5.567165,-9.146033,0.918268,-1.733393,-3.287714,-4.812238],[-4.226090,-9.761153,-4.980668,-8.032212,-3.222646,-9.435846,-8.428300,5.255285],[6.463444,4.937418,-9.285662,9.957479,9.911105,9.814662,-0.471242,1.180664],[1.730351,-2.399537,-6.684554,-6.472199,-1.518992,-8.914475,2.783248,4.039712],[4.019132,-3.125500,-5.099621,3.906678,1.221858,3.566672,-5.597371,-0.731542],[-2.424075,1.077427,1.707976,-8.881610,-5.474042,-4.948574,-8.939895,3.932799],[-8.074311,7.953577,5.809143,0.238133,-6.316660,4.330307,0.666104,-9.529546],[-1.466857,-3.699502,8.821970,6.636571,-8.438627,1.915641,8.113034,-2.407104],[-9.977095,-7.484625,1.482472,-4.203536,7.230067,-8.374937,-2.949777,-5.778041],[4.382079,-0.525308,5.264600,-5.056318,-1.037645,5.964338,-6.215089,3.423498]],[[4.168424,7.451236,1.893436,-9.115227,3.655847,0.471818,2.859470,-9.305915],[8.094877,-9.041111,5.864703,-5.705744,-0.896341,8.516698,5.472754,-7.865971],[9.901648,3.013993,6.713306,1.405877,6.458680,-4.464695,-4.493980,9.529135],[-6.024022,4.787736,-0.204875,6.674756,2.196048,-6.557534,6.663073,6.454800],[-2.466316,-1.350875,5.763158,-0.720804,-1.237540,9.315327,5.122166,-2.616593],[-0.309635,4.867859,4.816319,-3.898770,-5.989575,-3.445277,1.844065,-8.729688],[-7.454362,8.536234,-2.952592,-0.137055,9.589464,9.568347,-1.395214,-7.522077],[2.604883,-1.364197,-3.827294,3.770742,7.053584,-6.374258,-9.775498,-3.804401],[7.609280,-4.535511,8.364582,5.562262,-4.834005,3.375163,-5.634595,-7.733608],[-7.054309,5.947793,7.760745,3.456138,-6.728238,4.543677,-4.191109,0.997154]],[[5.027322,3.701375,0.467686,4.425135,1.733290,-7.394928,-9.777577,-8.782710],[6.506485,9.121145,-8.565074,8.777180,8.729219,1.394300,-7.681341,0.914010],[-2.167039,-4.853581,6.403621,-9.132927,2.206072,4.214655,8.079846,-2.596467],[8.330122,4.226882,-3.538110,-0.112828,9.226314,6.038783,-8.532630,3.862582],[7.897189,-4.223962,-6.007554,8.773150,-5.207703,0.487392,-0.608897,-4.712094],[-2.758932,-6.781244,1.962487,-6.661873,-0.774331,-8.054963,-7.173168,-2.966800],[-0.407864,1.166896,8.584095,-1.296533,3.808625,7.966802,5.465321,4.830141],[0.389410,-9.974554,-4.345448,5.152440,-4.325910,7.087487,0.810588,-6.035602],[2.051438,-3.602356,-4.034760,-0.566647,3.510780,-6.212200,8.516453,-8.103733],[9.949512,2.938527,2.947125,-5.178872,6.145007,-6.120091,7.453611,-8.491973]]], dtype = "float32")#candidate|914|(16, 10, 8)|const|float32
uop_915 = relay.atan(const_914.astype('float32')) # shape=(16, 10, 8)
uop_922 = relay.atanh(uop_915.astype('float32')) # shape=(16, 10, 8)
func_740_call = mod.get_global_var('func_740')
func_742_call = mutated_mod.get_global_var('func_742')
call_926 = relay.TupleGetItem(func_740_call(), 0)
call_927 = relay.TupleGetItem(func_742_call(), 0)
bop_931 = relay.right_shift(uop_915.astype('uint16'), relay.reshape(const_914.astype('uint16'), relay.shape_of(uop_915))) # shape=(16, 10, 8)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_954 = relay.TupleGetItem(func_329_call(), 1)
call_955 = relay.TupleGetItem(func_330_call(), 1)
uop_958 = relay.exp(uop_922.astype('float64')) # shape=(16, 10, 8)
output = relay.Tuple([call_926,bop_931,call_954,uop_958,])
output2 = relay.Tuple([call_927,bop_931,call_955,uop_958,])
func_976 = relay.Function([], output)
mod['func_976'] = func_976
mod = relay.transform.InferType()(mod)
output = func_976()
func_977 = relay.Function([], output)
mutated_mod['func_977'] = func_977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_976_call = mod.get_global_var('func_976')
func_977_call = mutated_mod.get_global_var('func_977')
call_978 = relay.TupleGetItem(func_976_call(), 2)
call_979 = relay.TupleGetItem(func_977_call(), 2)
var_989 = relay.var("var_989", dtype = "int32", shape = (8, 7, 3))#candidate|989|(8, 7, 3)|var|int32
bop_990 = relay.left_shift(call_978.astype('int8'), relay.reshape(var_989.astype('int8'), relay.shape_of(call_978))) # shape=(8, 7, 3)
bop_993 = relay.left_shift(call_979.astype('int8'), relay.reshape(var_989.astype('int8'), relay.shape_of(call_979))) # shape=(8, 7, 3)
output = relay.Tuple([bop_990,])
output2 = relay.Tuple([bop_993,])
func_995 = relay.Function([var_989,], output)
mod['func_995'] = func_995
mod = relay.transform.InferType()(mod)
var_996 = relay.var("var_996", dtype = "int32", shape = (8, 7, 3))#candidate|996|(8, 7, 3)|var|int32
output = func_995(var_996)
func_997 = relay.Function([var_996], output)
mutated_mod['func_997'] = func_997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_656_call = mod.get_global_var('func_656')
func_657_call = mutated_mod.get_global_var('func_657')
call_1031 = relay.TupleGetItem(func_656_call(), 0)
call_1032 = relay.TupleGetItem(func_657_call(), 0)
func_995_call = mod.get_global_var('func_995')
func_997_call = mutated_mod.get_global_var('func_997')
call_1049 = relay.TupleGetItem(func_995_call(relay.reshape(call_1031.astype('int32'), [8, 7, 3])), 0)
call_1050 = relay.TupleGetItem(func_997_call(relay.reshape(call_1031.astype('int32'), [8, 7, 3])), 0)
var_1058 = relay.var("var_1058", dtype = "int8", shape = (8, 7, 3))#candidate|1058|(8, 7, 3)|var|int8
bop_1059 = relay.power(call_1049.astype('float64'), relay.reshape(var_1058.astype('float64'), relay.shape_of(call_1049))) # shape=(8, 7, 3)
bop_1062 = relay.power(call_1050.astype('float64'), relay.reshape(var_1058.astype('float64'), relay.shape_of(call_1050))) # shape=(8, 7, 3)
func_995_call = mod.get_global_var('func_995')
func_997_call = mutated_mod.get_global_var('func_997')
call_1066 = relay.TupleGetItem(func_995_call(relay.reshape(var_1058.astype('int32'), [8, 7, 3])), 0)
call_1067 = relay.TupleGetItem(func_997_call(relay.reshape(var_1058.astype('int32'), [8, 7, 3])), 0)
func_656_call = mod.get_global_var('func_656')
func_657_call = mutated_mod.get_global_var('func_657')
call_1071 = relay.TupleGetItem(func_656_call(), 0)
call_1072 = relay.TupleGetItem(func_657_call(), 0)
output = relay.Tuple([call_1031,bop_1059,call_1066,call_1071,])
output2 = relay.Tuple([call_1032,bop_1062,call_1067,call_1072,])
func_1080 = relay.Function([var_1058,], output)
mod['func_1080'] = func_1080
mod = relay.transform.InferType()(mod)
var_1081 = relay.var("var_1081", dtype = "int8", shape = (8, 7, 3))#candidate|1081|(8, 7, 3)|var|int8
output = func_1080(var_1081)
func_1082 = relay.Function([var_1081], output)
mutated_mod['func_1082'] = func_1082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1151 = relay.var("var_1151", dtype = "uint32", shape = ())#candidate|1151|()|var|uint32
var_1152 = relay.var("var_1152", dtype = "uint32", shape = (12, 3, 10))#candidate|1152|(12, 3, 10)|var|uint32
bop_1153 = relay.add(var_1151.astype('uint32'), var_1152.astype('uint32')) # shape=(12, 3, 10)
const_1163 = relay.const([[[-7,4,-10,-10,-10,-9,3,-8,-5,9],[-9,3,-2,10,-4,-8,7,9,-2,-10],[-4,-5,7,1,2,-5,6,-10,8,-8]],[[2,1,7,9,-1,-4,-10,-5,-2,10],[-8,-4,5,-3,-4,3,-7,7,8,-5],[-5,-5,-10,3,-7,-8,9,9,6,5]],[[3,7,-6,-5,-10,-3,-3,-1,1,7],[-6,4,6,9,5,1,-4,1,-3,-2],[1,10,-6,-7,3,-6,8,4,3,-6]],[[-9,-10,7,1,-8,-3,-10,2,-3,4],[4,7,-8,-8,6,1,4,6,-3,-1],[4,9,-6,2,2,5,4,10,3,-4]],[[5,-4,-7,8,9,-10,-3,5,-1,-9],[2,3,-8,-9,2,-9,3,5,4,-9],[-5,4,-9,9,7,-7,4,7,2,10]],[[-1,10,-4,3,10,-1,-4,-5,5,5],[2,10,-1,-5,-5,8,5,10,-4,-7],[9,-1,2,-6,-10,8,-4,-5,7,9]],[[-4,-8,6,10,4,-6,5,4,3,-6],[-10,2,-5,10,-6,4,7,-1,-1,-4],[-8,6,8,-3,-9,-4,3,4,5,-10]],[[4,-1,5,5,-2,-10,7,-4,-7,6],[5,-6,5,6,3,-1,1,9,5,-1],[3,7,-7,-7,-7,-10,-2,-3,-6,9]],[[9,8,3,4,-3,4,8,6,-2,10],[5,-4,-6,-5,9,2,5,6,7,-7],[6,-6,5,-10,6,-6,1,7,-8,10]],[[10,3,-9,-5,-10,-9,-6,-3,-7,-5],[2,-4,-3,10,5,9,9,-1,3,-9],[10,1,10,-6,6,10,5,3,-4,1]],[[3,7,4,-4,-5,1,-10,-1,8,-9],[-1,6,-2,-5,-4,-10,-6,10,-6,-6],[9,8,2,2,-9,6,-2,7,1,-4]],[[6,-1,2,2,-8,-1,-8,6,10,-9],[1,-8,-10,-6,-5,-6,-4,-5,8,4],[-8,3,-4,5,7,1,-1,-8,4,-2]]], dtype = "uint32")#candidate|1163|(12, 3, 10)|const|uint32
bop_1164 = relay.bitwise_xor(bop_1153.astype('uint16'), relay.reshape(const_1163.astype('uint16'), relay.shape_of(bop_1153))) # shape=(12, 3, 10)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_1170 = relay.TupleGetItem(func_273_call(), 1)
call_1171 = relay.TupleGetItem(func_275_call(), 1)
output = relay.Tuple([bop_1164,call_1170,])
output2 = relay.Tuple([bop_1164,call_1171,])
func_1189 = relay.Function([var_1151,var_1152,], output)
mod['func_1189'] = func_1189
mod = relay.transform.InferType()(mod)
var_1190 = relay.var("var_1190", dtype = "uint32", shape = ())#candidate|1190|()|var|uint32
var_1191 = relay.var("var_1191", dtype = "uint32", shape = (12, 3, 10))#candidate|1191|(12, 3, 10)|var|uint32
output = func_1189(var_1190,var_1191,)
func_1192 = relay.Function([var_1190,var_1191,], output)
mutated_mod['func_1192'] = func_1192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_450_call = mutated_mod.get_global_var('func_450')
call_1235 = func_449_call()
call_1236 = func_449_call()
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_1242 = relay.TupleGetItem(func_377_call(), 1)
call_1243 = relay.TupleGetItem(func_379_call(), 1)
output = relay.Tuple([call_1235,call_1242,])
output2 = relay.Tuple([call_1236,call_1243,])
func_1244 = relay.Function([], output)
mod['func_1244'] = func_1244
mod = relay.transform.InferType()(mod)
output = func_1244()
func_1245 = relay.Function([], output)
mutated_mod['func_1245'] = func_1245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_1280 = relay.TupleGetItem(func_776_call(), 0)
call_1281 = relay.TupleGetItem(func_778_call(), 0)
func_621_call = mod.get_global_var('func_621')
func_622_call = mutated_mod.get_global_var('func_622')
call_1282 = relay.TupleGetItem(func_621_call(), 1)
call_1283 = relay.TupleGetItem(func_622_call(), 1)
func_1189_call = mod.get_global_var('func_1189')
func_1192_call = mutated_mod.get_global_var('func_1192')
var_1289 = relay.var("var_1289", dtype = "uint32", shape = ())#candidate|1289|()|var|uint32
const_1290 = relay.const([-6,3,8,4,-5,6,5,1,1,4,6,7,-7,7,7,-7,2,-10,-8,-8,7,2,-4,-3,-6,10,-9,4,-7,3,-9,-5,-2,1,9,4,7,-7,-8,8,5,8,5,4,-4,-4,-9,6,-5,-5,8,10,3,6,8,-5,-4,-9,-4,-10,9,-3,-4,4,-6,4,6,9,3,-1,1,-4,-7,-3,7,9,-7,6,1,-1,-7,-1,10,4,-5,-4,9,1,-2,-8,6,-5,-2,-4,-1,8,-9,2,-8,5,-1,10,-9,-7,5,-10,-3,-6,5,7,-5,5,3,7,6,-7,-1,7,9,-10,9,9,-6,8,5,9,-10,7,-4,9,6,-8,-2,-8,-1,7,-10,-4,1,10,-9,9,-5,-7,3,-2,-9,-6,5,3,-2,-6,9,1,-3,-10,-1,-2,-5,9,4,-7,-10,-5,6,-1,-2,-5,6,-3,-6,-1,-9,-5,-3,-4,-6,9,5,10,-4,2,-7,-9,2,2,-4,-6,6,-9,6,6,-6,9,-9,-3,-10,-10,-3,-10,10,2,4,9,9,-1,-3,8,-1,1,6,4,-10,-4,5,5,-5,1,6,9,8,-2,-6,10,-9,-7,4,2,-8,-4,-10,2,9,3,3,-1,-4,4,5,-9,-7,-9,10,5,-8,4,-2,-1,10,-6,-10,6,8,-5,-3,7,-3,-3,8,2,8,3,-2,3,-10,3,-4,5,-8,-6,7,3,10,6,3,-5,5,5,4,-7,4,6,10,9,4,-1,9,-4,9,8,-7,6,-2,-7,-6,-1,-6,-8,8,6,-5,4,10,-4,5,2,-6,4,-7,4,-5,4,2,10,9,4,3,-7,-8,-2,4,5,-2,8,9,-3,-7,-8,8,2,5,1,-6,1,-9,6,-8,-3,-1,-10,-3,7,-1,-10,6,-8,8,1,6,-7,-6,8,8,-4,2,-1,10,-4,6,2], dtype = "uint32")#candidate|1290|(360,)|const|uint32
call_1288 = relay.TupleGetItem(func_1189_call(relay.reshape(var_1289.astype('uint32'), []), relay.reshape(const_1290.astype('uint32'), [12, 3, 10]), ), 1)
call_1291 = relay.TupleGetItem(func_1192_call(relay.reshape(var_1289.astype('uint32'), []), relay.reshape(const_1290.astype('uint32'), [12, 3, 10]), ), 1)
func_656_call = mod.get_global_var('func_656')
func_657_call = mutated_mod.get_global_var('func_657')
call_1293 = relay.TupleGetItem(func_656_call(), 0)
call_1294 = relay.TupleGetItem(func_657_call(), 0)
func_1244_call = mod.get_global_var('func_1244')
func_1245_call = mutated_mod.get_global_var('func_1245')
call_1313 = relay.TupleGetItem(func_1244_call(), 0)
call_1314 = relay.TupleGetItem(func_1245_call(), 0)
uop_1324 = relay.acosh(call_1293.astype('float64')) # shape=(8, 7, 3)
uop_1326 = relay.acosh(call_1294.astype('float64')) # shape=(8, 7, 3)
output = relay.Tuple([call_1280,call_1282,call_1288,var_1289,const_1290,call_1313,uop_1324,])
output2 = relay.Tuple([call_1281,call_1283,call_1291,var_1289,const_1290,call_1314,uop_1326,])
func_1329 = relay.Function([var_1289,], output)
mod['func_1329'] = func_1329
mod = relay.transform.InferType()(mod)
mutated_mod['func_1329'] = func_1329
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1330 = relay.var("var_1330", dtype = "uint32", shape = ())#candidate|1330|()|var|uint32
func_1329_call = mutated_mod.get_global_var('func_1329')
call_1331 = func_1329_call(var_1330)
output = call_1331
func_1332 = relay.Function([var_1330], output)
mutated_mod['func_1332'] = func_1332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1383 = relay.var("var_1383", dtype = "float32", shape = (8, 12))#candidate|1383|(8, 12)|var|float32
uop_1384 = relay.atanh(var_1383.astype('float32')) # shape=(8, 12)
output = uop_1384
output2 = uop_1384
func_1394 = relay.Function([var_1383,], output)
mod['func_1394'] = func_1394
mod = relay.transform.InferType()(mod)
mutated_mod['func_1394'] = func_1394
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1395 = relay.var("var_1395", dtype = "float32", shape = (8, 12))#candidate|1395|(8, 12)|var|float32
func_1394_call = mutated_mod.get_global_var('func_1394')
call_1396 = func_1394_call(var_1395)
output = call_1396
func_1397 = relay.Function([var_1395], output)
mutated_mod['func_1397'] = func_1397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_505_call = mod.get_global_var('func_505')
func_507_call = mutated_mod.get_global_var('func_507')
call_1419 = relay.TupleGetItem(func_505_call(), 0)
call_1420 = relay.TupleGetItem(func_507_call(), 0)
output = relay.Tuple([call_1419,])
output2 = relay.Tuple([call_1420,])
func_1428 = relay.Function([], output)
mod['func_1428'] = func_1428
mod = relay.transform.InferType()(mod)
output = func_1428()
func_1429 = relay.Function([], output)
mutated_mod['func_1429'] = func_1429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_1475 = relay.TupleGetItem(func_273_call(), 0)
call_1476 = relay.TupleGetItem(func_275_call(), 0)
func_740_call = mod.get_global_var('func_740')
func_742_call = mutated_mod.get_global_var('func_742')
call_1477 = relay.TupleGetItem(func_740_call(), 1)
call_1478 = relay.TupleGetItem(func_742_call(), 1)
func_1329_call = mod.get_global_var('func_1329')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_1485 = relay.const(8, dtype = "uint32")#candidate|1485|()|const|uint32
call_1484 = relay.TupleGetItem(func_1329_call(relay.reshape(const_1485.astype('uint32'), [])), 5)
call_1486 = relay.TupleGetItem(func_1332_call(relay.reshape(const_1485.astype('uint32'), [])), 5)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_1491 = relay.TupleGetItem(func_329_call(), 0)
call_1492 = relay.TupleGetItem(func_330_call(), 0)
uop_1495 = relay.sin(call_1477.astype('float64')) # shape=(8, 7, 3)
uop_1497 = relay.sin(call_1478.astype('float64')) # shape=(8, 7, 3)
output = relay.Tuple([call_1475,call_1484,const_1485,call_1491,uop_1495,])
output2 = relay.Tuple([call_1476,call_1486,const_1485,call_1492,uop_1497,])
func_1504 = relay.Function([], output)
mod['func_1504'] = func_1504
mod = relay.transform.InferType()(mod)
mutated_mod['func_1504'] = func_1504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1504_call = mutated_mod.get_global_var('func_1504')
call_1505 = func_1504_call()
output = call_1505
func_1506 = relay.Function([], output)
mutated_mod['func_1506'] = func_1506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1428_call = mod.get_global_var('func_1428')
func_1429_call = mutated_mod.get_global_var('func_1429')
call_1567 = relay.TupleGetItem(func_1428_call(), 0)
call_1568 = relay.TupleGetItem(func_1429_call(), 0)
output = relay.Tuple([call_1567,])
output2 = relay.Tuple([call_1568,])
func_1570 = relay.Function([], output)
mod['func_1570'] = func_1570
mod = relay.transform.InferType()(mod)
output = func_1570()
func_1571 = relay.Function([], output)
mutated_mod['func_1571'] = func_1571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_1612 = relay.TupleGetItem(func_329_call(), 1)
call_1613 = relay.TupleGetItem(func_330_call(), 1)
output = call_1612
output2 = call_1613
func_1620 = relay.Function([], output)
mod['func_1620'] = func_1620
mod = relay.transform.InferType()(mod)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mutated_mod.get_global_var('func_1620')
call_1621 = func_1620_call()
output = call_1621
func_1622 = relay.Function([], output)
mutated_mod['func_1622'] = func_1622
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1633 = relay.var("var_1633", dtype = "float32", shape = (4, 9, 13))#candidate|1633|(4, 9, 13)|var|float32
var_1634 = relay.var("var_1634", dtype = "float32", shape = (4, 9, 13))#candidate|1634|(4, 9, 13)|var|float32
bop_1635 = relay.not_equal(var_1633.astype('bool'), relay.reshape(var_1634.astype('bool'), relay.shape_of(var_1633))) # shape=(4, 9, 13)
output = relay.Tuple([bop_1635,])
output2 = relay.Tuple([bop_1635,])
func_1639 = relay.Function([var_1633,var_1634,], output)
mod['func_1639'] = func_1639
mod = relay.transform.InferType()(mod)
var_1640 = relay.var("var_1640", dtype = "float32", shape = (4, 9, 13))#candidate|1640|(4, 9, 13)|var|float32
var_1641 = relay.var("var_1641", dtype = "float32", shape = (4, 9, 13))#candidate|1641|(4, 9, 13)|var|float32
output = func_1639(var_1640,var_1641,)
func_1642 = relay.Function([var_1640,var_1641,], output)
mutated_mod['func_1642'] = func_1642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_1651 = relay.TupleGetItem(func_776_call(), 0)
call_1652 = relay.TupleGetItem(func_778_call(), 0)
var_1654 = relay.var("var_1654", dtype = "int32", shape = (8, 7, 3))#candidate|1654|(8, 7, 3)|var|int32
bop_1655 = relay.floor_divide(call_1651.astype('float32'), relay.reshape(var_1654.astype('float32'), relay.shape_of(call_1651))) # shape=(8, 7, 3)
bop_1658 = relay.floor_divide(call_1652.astype('float32'), relay.reshape(var_1654.astype('float32'), relay.shape_of(call_1652))) # shape=(8, 7, 3)
output = relay.Tuple([bop_1655,])
output2 = relay.Tuple([bop_1658,])
func_1659 = relay.Function([var_1654,], output)
mod['func_1659'] = func_1659
mod = relay.transform.InferType()(mod)
var_1660 = relay.var("var_1660", dtype = "int32", shape = (8, 7, 3))#candidate|1660|(8, 7, 3)|var|int32
output = func_1659(var_1660)
func_1661 = relay.Function([var_1660], output)
mutated_mod['func_1661'] = func_1661
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1686 = relay.var("var_1686", dtype = "float32", shape = (10, 4, 13))#candidate|1686|(10, 4, 13)|var|float32
uop_1687 = relay.sinh(var_1686.astype('float32')) # shape=(10, 4, 13)
output = uop_1687
output2 = uop_1687
func_1690 = relay.Function([var_1686,], output)
mod['func_1690'] = func_1690
mod = relay.transform.InferType()(mod)
var_1691 = relay.var("var_1691", dtype = "float32", shape = (10, 4, 13))#candidate|1691|(10, 4, 13)|var|float32
output = func_1690(var_1691)
func_1692 = relay.Function([var_1691], output)
mutated_mod['func_1692'] = func_1692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_450_call = mutated_mod.get_global_var('func_450')
call_1728 = func_449_call()
call_1729 = func_449_call()
output = relay.Tuple([call_1728,])
output2 = relay.Tuple([call_1729,])
func_1730 = relay.Function([], output)
mod['func_1730'] = func_1730
mod = relay.transform.InferType()(mod)
output = func_1730()
func_1731 = relay.Function([], output)
mutated_mod['func_1731'] = func_1731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1730_call = mod.get_global_var('func_1730')
func_1731_call = mutated_mod.get_global_var('func_1731')
call_1769 = relay.TupleGetItem(func_1730_call(), 0)
call_1770 = relay.TupleGetItem(func_1731_call(), 0)
output = call_1769
output2 = call_1770
func_1781 = relay.Function([], output)
mod['func_1781'] = func_1781
mod = relay.transform.InferType()(mod)
mutated_mod['func_1781'] = func_1781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1781_call = mutated_mod.get_global_var('func_1781')
call_1782 = func_1781_call()
output = call_1782
func_1783 = relay.Function([], output)
mutated_mod['func_1783'] = func_1783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_621_call = mod.get_global_var('func_621')
func_622_call = mutated_mod.get_global_var('func_622')
call_1807 = relay.TupleGetItem(func_621_call(), 0)
call_1808 = relay.TupleGetItem(func_622_call(), 0)
output = call_1807
output2 = call_1808
func_1833 = relay.Function([], output)
mod['func_1833'] = func_1833
mod = relay.transform.InferType()(mod)
mutated_mod['func_1833'] = func_1833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1833_call = mutated_mod.get_global_var('func_1833')
call_1834 = func_1833_call()
output = call_1834
func_1835 = relay.Function([], output)
mutated_mod['func_1835'] = func_1835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_1929 = relay.TupleGetItem(func_776_call(), 0)
call_1930 = relay.TupleGetItem(func_778_call(), 0)
func_1329_call = mod.get_global_var('func_1329')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_1934 = relay.const(8, dtype = "uint32")#candidate|1934|()|const|uint32
call_1933 = relay.TupleGetItem(func_1329_call(relay.reshape(const_1934.astype('uint32'), [])), 5)
call_1935 = relay.TupleGetItem(func_1332_call(relay.reshape(const_1934.astype('uint32'), [])), 5)
func_1329_call = mod.get_global_var('func_1329')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_1937 = relay.TupleGetItem(func_1329_call(relay.reshape(const_1934.astype('uint32'), [])), 0)
call_1938 = relay.TupleGetItem(func_1332_call(relay.reshape(const_1934.astype('uint32'), [])), 0)
output = relay.Tuple([call_1929,call_1933,const_1934,call_1937,])
output2 = relay.Tuple([call_1930,call_1935,const_1934,call_1938,])
func_1942 = relay.Function([], output)
mod['func_1942'] = func_1942
mod = relay.transform.InferType()(mod)
mutated_mod['func_1942'] = func_1942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1942_call = mutated_mod.get_global_var('func_1942')
call_1943 = func_1942_call()
output = call_1943
func_1944 = relay.Function([], output)
mutated_mod['func_1944'] = func_1944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_450_call = mutated_mod.get_global_var('func_450')
call_1953 = func_449_call()
call_1954 = func_449_call()
output = relay.Tuple([call_1953,])
output2 = relay.Tuple([call_1954,])
func_1956 = relay.Function([], output)
mod['func_1956'] = func_1956
mod = relay.transform.InferType()(mod)
output = func_1956()
func_1957 = relay.Function([], output)
mutated_mod['func_1957'] = func_1957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_505_call = mod.get_global_var('func_505')
func_507_call = mutated_mod.get_global_var('func_507')
call_1973 = relay.TupleGetItem(func_505_call(), 0)
call_1974 = relay.TupleGetItem(func_507_call(), 0)
output = relay.Tuple([call_1973,])
output2 = relay.Tuple([call_1974,])
func_1987 = relay.Function([], output)
mod['func_1987'] = func_1987
mod = relay.transform.InferType()(mod)
mutated_mod['func_1987'] = func_1987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1987_call = mutated_mod.get_global_var('func_1987')
call_1988 = func_1987_call()
output = call_1988
func_1989 = relay.Function([], output)
mutated_mod['func_1989'] = func_1989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_740_call = mod.get_global_var('func_740')
func_742_call = mutated_mod.get_global_var('func_742')
call_2051 = relay.TupleGetItem(func_740_call(), 1)
call_2052 = relay.TupleGetItem(func_742_call(), 1)
func_1942_call = mod.get_global_var('func_1942')
func_1944_call = mutated_mod.get_global_var('func_1944')
call_2063 = relay.TupleGetItem(func_1942_call(), 0)
call_2064 = relay.TupleGetItem(func_1944_call(), 0)
bop_2066 = relay.bitwise_and(call_2051.astype('int32'), relay.reshape(call_2063.astype('int32'), relay.shape_of(call_2051))) # shape=(8, 7, 3)
bop_2069 = relay.bitwise_and(call_2052.astype('int32'), relay.reshape(call_2064.astype('int32'), relay.shape_of(call_2052))) # shape=(8, 7, 3)
output = bop_2066
output2 = bop_2069
func_2072 = relay.Function([], output)
mod['func_2072'] = func_2072
mod = relay.transform.InferType()(mod)
mutated_mod['func_2072'] = func_2072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mutated_mod.get_global_var('func_2072')
call_2073 = func_2072_call()
output = call_2073
func_2074 = relay.Function([], output)
mutated_mod['func_2074'] = func_2074
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2120 = relay.var("var_2120", dtype = "float32", shape = (9, 5, 5))#candidate|2120|(9, 5, 5)|var|float32
uop_2121 = relay.erf(var_2120.astype('float32')) # shape=(9, 5, 5)
output = uop_2121
output2 = uop_2121
func_2128 = relay.Function([var_2120,], output)
mod['func_2128'] = func_2128
mod = relay.transform.InferType()(mod)
mutated_mod['func_2128'] = func_2128
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2129 = relay.var("var_2129", dtype = "float32", shape = (9, 5, 5))#candidate|2129|(9, 5, 5)|var|float32
func_2128_call = mutated_mod.get_global_var('func_2128')
call_2130 = func_2128_call(var_2129)
output = call_2130
func_2131 = relay.Function([var_2129], output)
mutated_mod['func_2131'] = func_2131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1781_call = mod.get_global_var('func_1781')
func_1783_call = mutated_mod.get_global_var('func_1783')
call_2201 = func_1781_call()
call_2202 = func_1781_call()
func_1987_call = mod.get_global_var('func_1987')
func_1989_call = mutated_mod.get_global_var('func_1989')
call_2203 = relay.TupleGetItem(func_1987_call(), 0)
call_2204 = relay.TupleGetItem(func_1989_call(), 0)
output = relay.Tuple([call_2201,call_2203,])
output2 = relay.Tuple([call_2202,call_2204,])
func_2220 = relay.Function([], output)
mod['func_2220'] = func_2220
mod = relay.transform.InferType()(mod)
mutated_mod['func_2220'] = func_2220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mutated_mod.get_global_var('func_2220')
call_2221 = func_2220_call()
output = call_2221
func_2222 = relay.Function([], output)
mutated_mod['func_2222'] = func_2222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_2226 = func_1620_call()
call_2227 = func_1620_call()
output = call_2226
output2 = call_2227
func_2231 = relay.Function([], output)
mod['func_2231'] = func_2231
mod = relay.transform.InferType()(mod)
output = func_2231()
func_2232 = relay.Function([], output)
mutated_mod['func_2232'] = func_2232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_656_call = mod.get_global_var('func_656')
func_657_call = mutated_mod.get_global_var('func_657')
call_2370 = relay.TupleGetItem(func_656_call(), 0)
call_2371 = relay.TupleGetItem(func_657_call(), 0)
func_2231_call = mod.get_global_var('func_2231')
func_2232_call = mutated_mod.get_global_var('func_2232')
call_2383 = func_2231_call()
call_2384 = func_2231_call()
output = relay.Tuple([call_2370,call_2383,])
output2 = relay.Tuple([call_2371,call_2384,])
func_2385 = relay.Function([], output)
mod['func_2385'] = func_2385
mod = relay.transform.InferType()(mod)
mutated_mod['func_2385'] = func_2385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2385_call = mutated_mod.get_global_var('func_2385')
call_2386 = func_2385_call()
output = call_2386
func_2387 = relay.Function([], output)
mutated_mod['func_2387'] = func_2387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_2391 = relay.TupleGetItem(func_2385_call(), 1)
call_2392 = relay.TupleGetItem(func_2387_call(), 1)
output = call_2391
output2 = call_2392
func_2394 = relay.Function([], output)
mod['func_2394'] = func_2394
mod = relay.transform.InferType()(mod)
output = func_2394()
func_2395 = relay.Function([], output)
mutated_mod['func_2395'] = func_2395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_2396 = relay.TupleGetItem(func_2385_call(), 1)
call_2397 = relay.TupleGetItem(func_2387_call(), 1)
func_1504_call = mod.get_global_var('func_1504')
func_1506_call = mutated_mod.get_global_var('func_1506')
call_2406 = relay.TupleGetItem(func_1504_call(), 1)
call_2407 = relay.TupleGetItem(func_1506_call(), 1)
func_656_call = mod.get_global_var('func_656')
func_657_call = mutated_mod.get_global_var('func_657')
call_2431 = relay.TupleGetItem(func_656_call(), 0)
call_2432 = relay.TupleGetItem(func_657_call(), 0)
output = relay.Tuple([call_2396,call_2406,call_2431,])
output2 = relay.Tuple([call_2397,call_2407,call_2432,])
func_2436 = relay.Function([], output)
mod['func_2436'] = func_2436
mod = relay.transform.InferType()(mod)
mutated_mod['func_2436'] = func_2436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2436_call = mutated_mod.get_global_var('func_2436')
call_2437 = func_2436_call()
output = call_2437
func_2438 = relay.Function([], output)
mutated_mod['func_2438'] = func_2438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1504_call = mod.get_global_var('func_1504')
func_1506_call = mutated_mod.get_global_var('func_1506')
call_2439 = relay.TupleGetItem(func_1504_call(), 4)
call_2440 = relay.TupleGetItem(func_1506_call(), 4)
output = call_2439
output2 = call_2440
func_2441 = relay.Function([], output)
mod['func_2441'] = func_2441
mod = relay.transform.InferType()(mod)
mutated_mod['func_2441'] = func_2441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2441_call = mutated_mod.get_global_var('func_2441')
call_2442 = func_2441_call()
output = call_2442
func_2443 = relay.Function([], output)
mutated_mod['func_2443'] = func_2443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_976_call = mod.get_global_var('func_976')
func_977_call = mutated_mod.get_global_var('func_977')
call_2468 = relay.TupleGetItem(func_976_call(), 2)
call_2469 = relay.TupleGetItem(func_977_call(), 2)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_2476 = relay.TupleGetItem(func_329_call(), 0)
call_2477 = relay.TupleGetItem(func_330_call(), 0)
func_1504_call = mod.get_global_var('func_1504')
func_1506_call = mutated_mod.get_global_var('func_1506')
call_2481 = relay.TupleGetItem(func_1504_call(), 1)
call_2482 = relay.TupleGetItem(func_1506_call(), 1)
bop_2500 = relay.bitwise_xor(call_2481.astype('int8'), relay.reshape(call_2468.astype('int8'), relay.shape_of(call_2481))) # shape=(8, 7, 3)
bop_2503 = relay.bitwise_xor(call_2482.astype('int8'), relay.reshape(call_2469.astype('int8'), relay.shape_of(call_2482))) # shape=(8, 7, 3)
output = relay.Tuple([call_2476,bop_2500,])
output2 = relay.Tuple([call_2477,bop_2503,])
func_2513 = relay.Function([], output)
mod['func_2513'] = func_2513
mod = relay.transform.InferType()(mod)
mutated_mod['func_2513'] = func_2513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mutated_mod.get_global_var('func_2513')
call_2514 = func_2513_call()
output = call_2514
func_2515 = relay.Function([], output)
mutated_mod['func_2515'] = func_2515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1956_call = mod.get_global_var('func_1956')
func_1957_call = mutated_mod.get_global_var('func_1957')
call_2522 = relay.TupleGetItem(func_1956_call(), 0)
call_2523 = relay.TupleGetItem(func_1957_call(), 0)
output = call_2522
output2 = call_2523
func_2526 = relay.Function([], output)
mod['func_2526'] = func_2526
mod = relay.transform.InferType()(mod)
mutated_mod['func_2526'] = func_2526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mutated_mod.get_global_var('func_2526')
call_2527 = func_2526_call()
output = call_2527
func_2528 = relay.Function([], output)
mutated_mod['func_2528'] = func_2528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2436_call = mod.get_global_var('func_2436')
func_2438_call = mutated_mod.get_global_var('func_2438')
call_2553 = relay.TupleGetItem(func_2436_call(), 2)
call_2554 = relay.TupleGetItem(func_2438_call(), 2)
func_1781_call = mod.get_global_var('func_1781')
func_1783_call = mutated_mod.get_global_var('func_1783')
call_2562 = func_1781_call()
call_2563 = func_1781_call()
uop_2570 = relay.asinh(call_2553.astype('float64')) # shape=(8, 7, 3)
uop_2572 = relay.asinh(call_2554.astype('float64')) # shape=(8, 7, 3)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_2595 = relay.TupleGetItem(func_329_call(), 1)
call_2596 = relay.TupleGetItem(func_330_call(), 1)
uop_2600 = relay.cosh(uop_2570.astype('float32')) # shape=(8, 7, 3)
uop_2602 = relay.cosh(uop_2572.astype('float32')) # shape=(8, 7, 3)
const_2603 = relay.const([[[3.944143,-8.801897,-0.326947],[1.636092,6.361143,0.187955],[4.683076,-1.829105,-4.600702],[-6.976163,-4.394302,-1.766706],[2.762482,-2.477228,-0.047640],[9.492318,4.492523,-1.206223],[-9.693470,-4.734694,3.653113]],[[1.088387,9.570146,-8.883977],[-8.842320,4.349734,5.932362],[-6.388242,-6.229429,5.150490],[8.491010,8.260274,-1.461664],[-9.042663,8.900189,5.544331],[-6.501545,4.713539,-4.951212],[4.184580,9.318686,2.754890]],[[-0.176005,4.653180,-6.321899],[-7.648697,1.730150,4.152367],[3.910090,-8.830646,-8.714996],[3.236983,-7.973057,-6.683957],[-8.381434,8.574253,4.675403],[-1.762717,-2.213194,-3.693108],[-3.419310,-9.263808,-2.714195]],[[-5.979154,2.923832,2.363123],[-6.180032,1.757446,5.127506],[9.792863,8.338306,7.777050],[-0.453406,2.575793,8.968555],[1.352898,-6.098099,1.238224],[3.273224,-7.998446,-4.480161],[3.602394,-6.320658,1.888776]],[[-1.938794,6.867620,9.583155],[-9.441891,7.820379,0.610340],[-0.342884,-8.878980,-3.593390],[5.824289,8.637048,3.067759],[9.010823,-0.753525,2.771885],[-8.500377,6.406760,7.576274],[-6.059478,-4.878635,4.099335]],[[1.640425,-9.290908,-1.140095],[5.617364,9.134895,6.171757],[1.102831,3.412533,-7.808228],[3.964918,-7.720107,0.890671],[-4.443417,-0.394218,7.224994],[-0.814292,3.553807,-3.262054],[2.336394,3.209591,9.958508]],[[7.250848,-2.034664,-6.347796],[4.463373,6.366626,-4.024110],[-4.046761,-3.214239,8.402405],[-6.780251,-8.905399,5.547616],[-9.493812,2.988970,5.859355],[-6.868975,1.474862,2.638300],[-1.348878,0.300056,-3.067097]],[[-8.897031,-0.853002,9.969945],[-0.172928,8.214913,7.380222],[2.936674,-4.829465,-7.742687],[7.436551,-8.138203,6.793196],[8.868495,0.467309,4.575373],[-1.426594,-2.793738,-8.197103],[0.071854,5.586905,-2.952663]]], dtype = "float32")#candidate|2603|(8, 7, 3)|const|float32
bop_2604 = relay.equal(uop_2600.astype('bool'), relay.reshape(const_2603.astype('bool'), relay.shape_of(uop_2600))) # shape=(8, 7, 3)
bop_2607 = relay.equal(uop_2602.astype('bool'), relay.reshape(const_2603.astype('bool'), relay.shape_of(uop_2602))) # shape=(8, 7, 3)
output = relay.Tuple([call_2562,call_2595,bop_2604,])
output2 = relay.Tuple([call_2563,call_2596,bop_2607,])
func_2631 = relay.Function([], output)
mod['func_2631'] = func_2631
mod = relay.transform.InferType()(mod)
mutated_mod['func_2631'] = func_2631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2631_call = mutated_mod.get_global_var('func_2631')
call_2632 = func_2631_call()
output = call_2632
func_2633 = relay.Function([], output)
mutated_mod['func_2633'] = func_2633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1570_call = mod.get_global_var('func_1570')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_2690 = relay.TupleGetItem(func_1570_call(), 0)
call_2691 = relay.TupleGetItem(func_1571_call(), 0)
output = call_2690
output2 = call_2691
func_2704 = relay.Function([], output)
mod['func_2704'] = func_2704
mod = relay.transform.InferType()(mod)
mutated_mod['func_2704'] = func_2704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2704_call = mutated_mod.get_global_var('func_2704')
call_2705 = func_2704_call()
output = call_2705
func_2706 = relay.Function([], output)
mutated_mod['func_2706'] = func_2706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1987_call = mod.get_global_var('func_1987')
func_1989_call = mutated_mod.get_global_var('func_1989')
call_2716 = relay.TupleGetItem(func_1987_call(), 0)
call_2717 = relay.TupleGetItem(func_1989_call(), 0)
output = relay.Tuple([call_2716,])
output2 = relay.Tuple([call_2717,])
func_2732 = relay.Function([], output)
mod['func_2732'] = func_2732
mod = relay.transform.InferType()(mod)
output = func_2732()
func_2733 = relay.Function([], output)
mutated_mod['func_2733'] = func_2733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_505_call = mod.get_global_var('func_505')
func_507_call = mutated_mod.get_global_var('func_507')
call_2745 = relay.TupleGetItem(func_505_call(), 0)
call_2746 = relay.TupleGetItem(func_507_call(), 0)
func_1833_call = mod.get_global_var('func_1833')
func_1835_call = mutated_mod.get_global_var('func_1835')
call_2749 = func_1833_call()
call_2750 = func_1833_call()
uop_2751 = relay.log10(call_2749.astype('float32')) # shape=(8, 7, 3)
uop_2753 = relay.log10(call_2750.astype('float32')) # shape=(8, 7, 3)
func_869_call = mod.get_global_var('func_869')
func_871_call = mutated_mod.get_global_var('func_871')
call_2763 = relay.TupleGetItem(func_869_call(), 1)
call_2764 = relay.TupleGetItem(func_871_call(), 1)
output = relay.Tuple([call_2745,uop_2751,call_2763,])
output2 = relay.Tuple([call_2746,uop_2753,call_2764,])
func_2786 = relay.Function([], output)
mod['func_2786'] = func_2786
mod = relay.transform.InferType()(mod)
output = func_2786()
func_2787 = relay.Function([], output)
mutated_mod['func_2787'] = func_2787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_2806 = relay.TupleGetItem(func_377_call(), 1)
call_2807 = relay.TupleGetItem(func_379_call(), 1)
output = relay.Tuple([call_2806,])
output2 = relay.Tuple([call_2807,])
func_2876 = relay.Function([], output)
mod['func_2876'] = func_2876
mod = relay.transform.InferType()(mod)
output = func_2876()
func_2877 = relay.Function([], output)
mutated_mod['func_2877'] = func_2877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2394_call = mod.get_global_var('func_2394')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_2878 = func_2394_call()
call_2879 = func_2394_call()
func_2231_call = mod.get_global_var('func_2231')
func_2232_call = mutated_mod.get_global_var('func_2232')
call_2884 = func_2231_call()
call_2885 = func_2231_call()
func_1659_call = mod.get_global_var('func_1659')
func_1661_call = mutated_mod.get_global_var('func_1661')
call_2890 = relay.TupleGetItem(func_1659_call(relay.reshape(call_2878.astype('int32'), [8, 7, 3])), 0)
call_2891 = relay.TupleGetItem(func_1661_call(relay.reshape(call_2878.astype('int32'), [8, 7, 3])), 0)
uop_2896 = relay.asin(call_2878.astype('float32')) # shape=(8, 7, 3)
uop_2898 = relay.asin(call_2879.astype('float32')) # shape=(8, 7, 3)
output = relay.Tuple([call_2884,call_2890,uop_2896,])
output2 = relay.Tuple([call_2885,call_2891,uop_2898,])
func_2911 = relay.Function([], output)
mod['func_2911'] = func_2911
mod = relay.transform.InferType()(mod)
mutated_mod['func_2911'] = func_2911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2911_call = mutated_mod.get_global_var('func_2911')
call_2912 = func_2911_call()
output = call_2912
func_2913 = relay.Function([], output)
mutated_mod['func_2913'] = func_2913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_2944 = relay.TupleGetItem(func_776_call(), 0)
call_2945 = relay.TupleGetItem(func_778_call(), 0)
func_1987_call = mod.get_global_var('func_1987')
func_1989_call = mutated_mod.get_global_var('func_1989')
call_2978 = relay.TupleGetItem(func_1987_call(), 0)
call_2979 = relay.TupleGetItem(func_1989_call(), 0)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
var_2993 = relay.var("var_2993", dtype = "float32", shape = (520,))#candidate|2993|(520,)|var|float32
call_2992 = func_1690_call(relay.reshape(var_2993.astype('float32'), [10, 4, 13]))
call_2994 = func_1690_call(relay.reshape(var_2993.astype('float32'), [10, 4, 13]))
output = relay.Tuple([call_2944,call_2978,call_2992,var_2993,])
output2 = relay.Tuple([call_2945,call_2979,call_2994,var_2993,])
func_2999 = relay.Function([var_2993,], output)
mod['func_2999'] = func_2999
mod = relay.transform.InferType()(mod)
var_3000 = relay.var("var_3000", dtype = "float32", shape = (520,))#candidate|3000|(520,)|var|float32
output = func_2999(var_3000)
func_3001 = relay.Function([var_3000], output)
mutated_mod['func_3001'] = func_3001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1428_call = mod.get_global_var('func_1428')
func_1429_call = mutated_mod.get_global_var('func_1429')
call_3003 = relay.TupleGetItem(func_1428_call(), 0)
call_3004 = relay.TupleGetItem(func_1429_call(), 0)
func_2436_call = mod.get_global_var('func_2436')
func_2438_call = mutated_mod.get_global_var('func_2438')
call_3018 = relay.TupleGetItem(func_2436_call(), 1)
call_3019 = relay.TupleGetItem(func_2438_call(), 1)
output = relay.Tuple([call_3003,call_3018,])
output2 = relay.Tuple([call_3004,call_3019,])
func_3021 = relay.Function([], output)
mod['func_3021'] = func_3021
mod = relay.transform.InferType()(mod)
output = func_3021()
func_3022 = relay.Function([], output)
mutated_mod['func_3022'] = func_3022
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3055 = relay.var("var_3055", dtype = "float64", shape = (12, 6, 15))#candidate|3055|(12, 6, 15)|var|float64
uop_3056 = relay.log(var_3055.astype('float64')) # shape=(12, 6, 15)
func_2231_call = mod.get_global_var('func_2231')
func_2232_call = mutated_mod.get_global_var('func_2232')
call_3066 = func_2231_call()
call_3067 = func_2231_call()
func_1504_call = mod.get_global_var('func_1504')
func_1506_call = mutated_mod.get_global_var('func_1506')
call_3080 = relay.TupleGetItem(func_1504_call(), 1)
call_3081 = relay.TupleGetItem(func_1506_call(), 1)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_3086 = func_2526_call()
call_3087 = func_2526_call()
uop_3097 = relay.sinh(var_3055.astype('float32')) # shape=(12, 6, 15)
func_1956_call = mod.get_global_var('func_1956')
func_1957_call = mutated_mod.get_global_var('func_1957')
call_3112 = relay.TupleGetItem(func_1956_call(), 0)
call_3113 = relay.TupleGetItem(func_1957_call(), 0)
func_1639_call = mod.get_global_var('func_1639')
func_1642_call = mutated_mod.get_global_var('func_1642')
const_3124 = relay.const([3.052542,9.681805,3.450033,-3.750141,-1.931168,9.378287,7.118899,7.770142,2.031729,-3.711360,-3.501477,9.975892,8.064288,-0.516772,2.472267,-5.285010,-3.248623,2.868226,-6.946809,3.895824,5.651993,1.282957,-0.368246,-6.609139,-6.656092,-4.362295,-2.755488,-0.742037,-5.267851,-0.337228,-3.095236,2.916440,-7.659526,-8.673912,-6.314705,3.787039,7.510769,-4.052603,1.566252,9.981238,1.532023,-8.091345,8.404335,4.292844,4.668723,-4.442321,0.414686,-4.509927,-0.407394,-1.730051,-6.307923,-7.992845,-5.693037,7.855099,-6.544554,-6.469535,-3.932613,1.330329,4.129086,-0.662600,-6.689300,-6.374528,-3.640977,3.924426,5.650819,6.933140,5.514107,6.533410,-4.225722,5.091710,9.478436,-3.504867,-1.976456,-9.238690,8.747480,9.862766,2.289952,0.655509,-8.697301,-9.246493,-8.394032,-2.649785,-8.692141,9.312201,-2.374542,7.531287,-1.328276,-1.220660,3.259002,-5.906338,9.681864,-2.361304,8.393092,-8.269232,-6.956879,-3.847156,-4.101327,-3.539348,-2.299665,0.891822,-8.754305,1.160051,-7.480639,6.303048,-6.382401,-1.990060,0.526316,-9.159811,-8.775621,4.430790,8.456089,4.530111,-6.894268,-5.135504,-6.425059,1.995314,-7.225925,1.438389,-0.823909,-5.356451,8.957347,-6.771155,4.577428,2.696636,3.533379,-9.507789,-2.866639,-4.698036,9.538341,-3.700124,-5.025462,-7.282009,-5.428582,-8.280837,4.170540,6.117461,2.693153,3.507393,-7.025923,1.037492,7.164407,-0.945556,0.016962,-2.229885,-5.063638,-8.774278,1.497572,5.112179,4.017104,-9.548802,8.709692,6.588041,-7.107539,9.223320,4.566172,-5.361893,4.895299,6.307447,-6.602301,9.289114,-4.795074,8.690593,5.921139,1.815050,-3.372138,3.974050,5.748741,2.703089,4.599605,-6.425701,8.987423,-8.385386,2.229237,2.631256,2.947275,-8.145524,7.847835,1.745686,4.631478,8.979614,1.357835,0.810713,2.757373,-2.634202,2.540513,8.554545,6.713358,5.322544,8.101622,-0.308566,-9.998950,-9.271575,3.137044,-7.098287,-8.419058,-0.667821,-6.347370,-7.008582,-7.969276,-8.736600,2.739615,-7.187738,1.253754,-0.352489,5.732380,-9.080808,0.023565,8.800197,-1.937617,4.058893,5.981222,-3.144265,5.160938,5.499927,7.389378,-3.130414,7.490129,-9.440008,-9.775758,-1.158647,1.369186,7.671855,0.805552,5.426681,-3.467007,0.258640,0.719325,7.604777,-9.367954,-2.049493,3.211277,9.697443,-0.171226,1.698560,-2.711138,-8.807609,-4.173401,-2.608844,-9.047300,-1.135947,7.279561,-8.424060,3.596778,8.794226,-4.881946,-1.146438,-4.720751,-1.112298,8.371136,-6.575262,7.395402,9.336220,-5.537470,-0.458354,-5.290399,-5.687416,-2.115576,-0.458831,-3.438044,4.967193,4.975451,-9.453013,7.564916,-9.162230,3.373564,-9.132022,3.896973,-0.053546,-7.531377,-1.933553,3.236565,-8.029978,0.908614,-1.191638,-4.390195,-4.007955,9.124095,-6.972358,-9.969048,4.973985,4.169695,-0.984473,7.019805,-5.764888,7.037907,-9.765298,8.535405,-4.777599,1.267698,7.681648,0.853921,-6.464469,-4.019491,4.339142,3.552553,-0.756078,9.801135,-5.780287,-8.931746,-3.454071,5.984293,-8.221486,0.241680,-9.497677,0.410394,-9.190280,3.306505,3.179174,1.260225,-7.277632,7.095289,9.184613,-2.968523,-9.977804,4.863757,-8.465875,8.806023,9.379867,-3.361196,-9.096620,8.438343,-2.977290,7.411323,1.318679,-6.350340,8.057248,-9.607510,-5.412338,-4.357999,2.169428,0.303656,0.083731,1.875920,7.156963,-7.346823,8.594658,1.465306,-6.276796,-3.968455,6.591411,-7.836598,-6.369044,-7.863042,9.332942,8.414933,-0.896252,-3.565693,-5.421597,-7.287060,3.573146,1.958716,7.073651,-4.572145,6.838266,8.399665,-7.852240,6.796997,-8.846509,9.131028,0.697338,2.965307,-0.870669,0.266547,4.061534,-3.234455,-1.520613,0.729535,-7.676128,5.461763,-5.556063,7.724408,-6.619879,-7.976354,-1.323336,-9.960615,-6.072203,1.466467,-6.340013,5.996147,-8.386704,-7.844981,0.731269,-0.687556,-8.742451,1.457485,-2.858531,2.317602,-0.386436,-0.195655,5.068143,-4.214035,-1.153899,-0.887825,-6.918936,-4.549513,-5.075919,0.428081,-9.266055,3.006117,5.971437,-4.522469,5.230157,7.697916,6.385763,-4.953457,-3.348800,-0.252642,-4.964893,7.578763,7.654227,-8.063425,8.128003,9.010126,1.977480,-7.491129,-1.223165,2.549373,-9.094657,9.610014,-4.801470,-1.458225,-0.728787,4.335381,-5.842758,2.371354,-9.795042,5.355491,7.428546,6.778100,5.525287,2.063236,-4.191046,-5.276003,9.651602,-1.065313,5.404064,4.284448,-2.200449,8.670890,6.912098,-0.847920,-2.213630,5.426186,-8.674230,-4.882809,-8.270086,8.481122,-2.807012,5.318239,9.428304,2.686370,1.972016,-2.009227,6.845224,-0.172898,-5.285441,-7.473798,-1.159064,-7.251598,6.304713,-1.126799,6.414118,-4.640566,2.607963,6.792017,-3.924845,-3.871265,1.846472], dtype = "float32")#candidate|3124|(468,)|const|float32
call_3123 = relay.TupleGetItem(func_1639_call(relay.reshape(const_3124.astype('float32'), [4, 9, 13]), relay.reshape(const_3124.astype('float32'), [4, 9, 13]), ), 0)
call_3125 = relay.TupleGetItem(func_1642_call(relay.reshape(const_3124.astype('float32'), [4, 9, 13]), relay.reshape(const_3124.astype('float32'), [4, 9, 13]), ), 0)
output = relay.Tuple([uop_3056,call_3066,call_3080,call_3086,uop_3097,call_3112,call_3123,const_3124,])
output2 = relay.Tuple([uop_3056,call_3067,call_3081,call_3087,uop_3097,call_3113,call_3125,const_3124,])
func_3131 = relay.Function([var_3055,], output)
mod['func_3131'] = func_3131
mod = relay.transform.InferType()(mod)
mutated_mod['func_3131'] = func_3131
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3132 = relay.var("var_3132", dtype = "float64", shape = (12, 6, 15))#candidate|3132|(12, 6, 15)|var|float64
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3133 = func_3131_call(var_3132)
output = call_3133
func_3134 = relay.Function([var_3132], output)
mutated_mod['func_3134'] = func_3134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_3157 = relay.TupleGetItem(func_329_call(), 1)
call_3158 = relay.TupleGetItem(func_330_call(), 1)
func_1639_call = mod.get_global_var('func_1639')
func_1642_call = mutated_mod.get_global_var('func_1642')
var_3164 = relay.var("var_3164", dtype = "float32", shape = (468,))#candidate|3164|(468,)|var|float32
call_3163 = relay.TupleGetItem(func_1639_call(relay.reshape(var_3164.astype('float32'), [4, 9, 13]), relay.reshape(var_3164.astype('float32'), [4, 9, 13]), ), 0)
call_3165 = relay.TupleGetItem(func_1642_call(relay.reshape(var_3164.astype('float32'), [4, 9, 13]), relay.reshape(var_3164.astype('float32'), [4, 9, 13]), ), 0)
output = relay.Tuple([call_3157,call_3163,var_3164,])
output2 = relay.Tuple([call_3158,call_3165,var_3164,])
func_3179 = relay.Function([var_3164,], output)
mod['func_3179'] = func_3179
mod = relay.transform.InferType()(mod)
var_3180 = relay.var("var_3180", dtype = "float32", shape = (468,))#candidate|3180|(468,)|var|float32
output = func_3179(var_3180)
func_3181 = relay.Function([var_3180], output)
mutated_mod['func_3181'] = func_3181
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3196 = relay.var("var_3196", dtype = "float32", shape = ())#candidate|3196|()|var|float32
var_3197 = relay.var("var_3197", dtype = "float32", shape = (8, 1, 4))#candidate|3197|(8, 1, 4)|var|float32
bop_3198 = relay.floor_mod(var_3196.astype('float32'), var_3197.astype('float32')) # shape=(8, 1, 4)
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_3213 = relay.TupleGetItem(func_377_call(), 1)
call_3214 = relay.TupleGetItem(func_379_call(), 1)
func_1394_call = mod.get_global_var('func_1394')
func_1397_call = mutated_mod.get_global_var('func_1397')
const_3217 = relay.const([-2.418589,7.090883,-4.139969,-2.366089,-4.891076,8.011379,6.558519,9.356470,9.834821,-1.549729,5.197455,-8.666313,6.194385,-3.573206,5.787287,-4.665313,6.442977,7.508109,-8.723057,-7.757829,9.170456,-9.672188,-0.452346,-6.067376,8.029781,5.231574,2.491274,8.803992,4.697737,-1.377329,5.106776,-2.138321,-3.897420,-6.651812,-6.428261,6.579434,-4.649106,-3.786127,-1.137241,-5.615296,8.104012,-4.104410,-3.268478,7.016762,4.506240,-9.926476,-1.663104,-6.327045,-0.226210,-3.372822,5.993522,-7.731026,6.543205,-0.291562,8.553667,6.535681,-1.577727,3.748822,-2.778146,-1.125381,-2.309180,-6.298160,7.698012,8.966660,5.891200,-3.602975,-5.982396,-3.810799,3.872958,4.916147,-4.745813,5.101333,-7.689313,3.914364,7.871007,-2.920018,-7.690782,0.241372,2.359761,9.966841,-3.668155,4.885465,-7.014777,-7.429844,-3.563209,-1.749716,-6.843078,9.275524,-8.385165,1.106677,-5.816031,-4.167263,-4.740156,7.851282,-2.221811,-1.584200], dtype = "float32")#candidate|3217|(96,)|const|float32
call_3216 = func_1394_call(relay.reshape(const_3217.astype('float32'), [8, 12]))
call_3218 = func_1394_call(relay.reshape(const_3217.astype('float32'), [8, 12]))
output = relay.Tuple([bop_3198,call_3213,call_3216,const_3217,])
output2 = relay.Tuple([bop_3198,call_3214,call_3218,const_3217,])
func_3231 = relay.Function([var_3196,var_3197,], output)
mod['func_3231'] = func_3231
mod = relay.transform.InferType()(mod)
mutated_mod['func_3231'] = func_3231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3231_call = mutated_mod.get_global_var('func_3231')
var_3233 = relay.var("var_3233", dtype = "float32", shape = ())#candidate|3233|()|var|float32
var_3234 = relay.var("var_3234", dtype = "float32", shape = (8, 1, 4))#candidate|3234|(8, 1, 4)|var|float32
call_3232 = func_3231_call(var_3233,var_3234,)
output = call_3232
func_3235 = relay.Function([var_3233,var_3234,], output)
mutated_mod['func_3235'] = func_3235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_3245 = func_2526_call()
call_3246 = func_2526_call()
output = call_3245
output2 = call_3246
func_3259 = relay.Function([], output)
mod['func_3259'] = func_3259
mod = relay.transform.InferType()(mod)
mutated_mod['func_3259'] = func_3259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3259_call = mutated_mod.get_global_var('func_3259')
call_3260 = func_3259_call()
output = call_3260
func_3261 = relay.Function([], output)
mutated_mod['func_3261'] = func_3261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_3269 = relay.TupleGetItem(func_273_call(), 1)
call_3270 = relay.TupleGetItem(func_275_call(), 1)
output = call_3269
output2 = call_3270
func_3271 = relay.Function([], output)
mod['func_3271'] = func_3271
mod = relay.transform.InferType()(mod)
mutated_mod['func_3271'] = func_3271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3271_call = mutated_mod.get_global_var('func_3271')
call_3272 = func_3271_call()
output = call_3272
func_3273 = relay.Function([], output)
mutated_mod['func_3273'] = func_3273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_976_call = mod.get_global_var('func_976')
func_977_call = mutated_mod.get_global_var('func_977')
call_3312 = relay.TupleGetItem(func_976_call(), 2)
call_3313 = relay.TupleGetItem(func_977_call(), 2)
output = relay.Tuple([call_3312,])
output2 = relay.Tuple([call_3313,])
func_3323 = relay.Function([], output)
mod['func_3323'] = func_3323
mod = relay.transform.InferType()(mod)
output = func_3323()
func_3324 = relay.Function([], output)
mutated_mod['func_3324'] = func_3324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1987_call = mod.get_global_var('func_1987')
func_1989_call = mutated_mod.get_global_var('func_1989')
call_3384 = relay.TupleGetItem(func_1987_call(), 0)
call_3385 = relay.TupleGetItem(func_1989_call(), 0)
output = relay.Tuple([call_3384,])
output2 = relay.Tuple([call_3385,])
func_3416 = relay.Function([], output)
mod['func_3416'] = func_3416
mod = relay.transform.InferType()(mod)
mutated_mod['func_3416'] = func_3416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3416_call = mutated_mod.get_global_var('func_3416')
call_3417 = func_3416_call()
output = call_3417
func_3418 = relay.Function([], output)
mutated_mod['func_3418'] = func_3418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2394_call = mod.get_global_var('func_2394')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_3445 = func_2394_call()
call_3446 = func_2394_call()
func_3416_call = mod.get_global_var('func_3416')
func_3418_call = mutated_mod.get_global_var('func_3418')
call_3450 = relay.TupleGetItem(func_3416_call(), 0)
call_3451 = relay.TupleGetItem(func_3418_call(), 0)
output = relay.Tuple([call_3445,call_3450,])
output2 = relay.Tuple([call_3446,call_3451,])
func_3455 = relay.Function([], output)
mod['func_3455'] = func_3455
mod = relay.transform.InferType()(mod)
mutated_mod['func_3455'] = func_3455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3455_call = mutated_mod.get_global_var('func_3455')
call_3456 = func_3455_call()
output = call_3456
func_3457 = relay.Function([], output)
mutated_mod['func_3457'] = func_3457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1428_call = mod.get_global_var('func_1428')
func_1429_call = mutated_mod.get_global_var('func_1429')
call_3467 = relay.TupleGetItem(func_1428_call(), 0)
call_3468 = relay.TupleGetItem(func_1429_call(), 0)
output = relay.Tuple([call_3467,])
output2 = relay.Tuple([call_3468,])
func_3499 = relay.Function([], output)
mod['func_3499'] = func_3499
mod = relay.transform.InferType()(mod)
output = func_3499()
func_3500 = relay.Function([], output)
mutated_mod['func_3500'] = func_3500
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3522 = relay.var("var_3522", dtype = "float32", shape = (7, 7, 1))#candidate|3522|(7, 7, 1)|var|float32
uop_3523 = relay.acosh(var_3522.astype('float32')) # shape=(7, 7, 1)
output = relay.Tuple([uop_3523,])
output2 = relay.Tuple([uop_3523,])
func_3528 = relay.Function([var_3522,], output)
mod['func_3528'] = func_3528
mod = relay.transform.InferType()(mod)
mutated_mod['func_3528'] = func_3528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3529 = relay.var("var_3529", dtype = "float32", shape = (7, 7, 1))#candidate|3529|(7, 7, 1)|var|float32
func_3528_call = mutated_mod.get_global_var('func_3528')
call_3530 = func_3528_call(var_3529)
output = call_3530
func_3531 = relay.Function([var_3529], output)
mutated_mod['func_3531'] = func_3531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_3559 = relay.TupleGetItem(func_2220_call(), 0)
call_3560 = relay.TupleGetItem(func_2222_call(), 0)
output = relay.Tuple([call_3559,])
output2 = relay.Tuple([call_3560,])
func_3579 = relay.Function([], output)
mod['func_3579'] = func_3579
mod = relay.transform.InferType()(mod)
output = func_3579()
func_3580 = relay.Function([], output)
mutated_mod['func_3580'] = func_3580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_3581 = relay.TupleGetItem(func_329_call(), 1)
call_3582 = relay.TupleGetItem(func_330_call(), 1)
output = relay.Tuple([call_3581,])
output2 = relay.Tuple([call_3582,])
func_3583 = relay.Function([], output)
mod['func_3583'] = func_3583
mod = relay.transform.InferType()(mod)
output = func_3583()
func_3584 = relay.Function([], output)
mutated_mod['func_3584'] = func_3584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_740_call = mod.get_global_var('func_740')
func_742_call = mutated_mod.get_global_var('func_742')
call_3919 = relay.TupleGetItem(func_740_call(), 1)
call_3920 = relay.TupleGetItem(func_742_call(), 1)
output = relay.Tuple([call_3919,])
output2 = relay.Tuple([call_3920,])
func_3927 = relay.Function([], output)
mod['func_3927'] = func_3927
mod = relay.transform.InferType()(mod)
output = func_3927()
func_3928 = relay.Function([], output)
mutated_mod['func_3928'] = func_3928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2528_call = mutated_mod.get_global_var('func_2528')
call_3993 = func_2526_call()
call_3994 = func_2526_call()
output = relay.Tuple([call_3993,])
output2 = relay.Tuple([call_3994,])
func_4009 = relay.Function([], output)
mod['func_4009'] = func_4009
mod = relay.transform.InferType()(mod)
mutated_mod['func_4009'] = func_4009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4009_call = mutated_mod.get_global_var('func_4009')
call_4010 = func_4009_call()
output = call_4010
func_4011 = relay.Function([], output)
mutated_mod['func_4011'] = func_4011
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4059 = relay.const([[[8.955590,-4.076465,-4.821302,9.018327,-5.537279,4.460451,2.396640,8.108537,0.585113,-6.828762,0.347159,0.090236,-4.900963,3.302810,-1.704768],[7.215259,1.018460,-5.651846,-6.789836,-7.027606,-0.560288,-6.610352,1.633755,-1.254480,7.790451,-4.202722,2.823356,0.639666,-2.901145,8.096904],[4.997316,-6.772330,-2.176053,8.689965,5.479916,2.570928,4.067286,2.321131,7.089273,-6.752458,-1.567190,4.959579,-9.962324,7.015012,-6.313235],[7.271255,0.782871,-9.104179,-5.454451,-1.647159,-1.943684,7.090378,1.294976,-6.776586,-6.560367,5.710768,-9.297932,-5.231850,-5.852552,3.822636],[-2.594350,-3.016001,3.230024,5.925241,-4.073587,7.873255,-3.278439,7.693406,9.661501,-5.084007,-4.361243,-6.663859,6.335026,9.978580,-8.633339],[-9.396470,7.800613,-9.865365,0.837875,2.786913,6.782765,-1.630134,4.087050,0.725068,-0.180449,1.425921,8.945204,2.290815,-4.491086,-5.289775],[8.711597,-3.384522,-4.302861,3.189356,-6.111435,6.034798,4.556123,1.055335,4.335497,4.637754,4.605643,-4.748054,-8.571798,0.562371,-4.537146],[4.208866,-7.407117,6.657965,-4.153410,-3.574505,0.364642,-8.583613,-9.995484,4.472193,-2.438825,4.047678,6.269039,7.057739,8.747340,9.706748],[-7.715913,2.876280,-6.042312,0.883360,-8.371685,3.762870,-0.073633,-8.854306,-3.036635,-3.743191,9.648514,-2.252021,-2.803588,-0.329989,-6.010838],[2.938603,8.290497,6.281344,5.491257,-8.836495,-8.894243,7.000743,-5.185524,2.952797,-8.172362,1.017753,1.076344,-0.486584,6.593777,4.241503],[-6.589010,6.212388,-7.247623,3.022539,1.078768,0.500769,-9.819285,-1.302458,-2.783805,0.063302,-4.661363,-6.682909,-2.533764,2.930898,-1.256701],[6.673711,9.932872,-7.871635,7.736173,-3.347387,9.147650,-3.646100,-0.718182,-1.428171,9.398920,9.187529,5.265831,5.065635,3.937394,4.548356],[-7.534870,-3.894577,5.345048,6.186643,9.880844,-2.673764,2.367765,-8.730331,5.585025,-0.482922,-3.460626,-8.694649,-8.668607,2.462861,-0.432823],[9.023558,8.928305,9.843450,-6.199598,4.006563,-2.252254,-2.902464,-2.451935,9.819835,-7.726187,-8.558862,-2.192496,-6.526093,5.054480,-1.347491],[-4.891209,-4.634800,2.159625,6.033724,-4.364928,4.225911,-2.422229,-2.253913,-4.752235,-9.586394,3.285779,0.030764,-4.782574,-8.959035,8.629622]],[[5.560026,-5.258200,8.720662,7.120877,7.402923,7.191981,-0.999610,3.847673,6.173219,4.859372,-3.586374,-0.173429,-3.945523,7.518763,-0.573970],[2.799980,-1.086529,9.842158,8.087457,-9.124732,-7.772300,-8.554130,3.990316,3.008650,9.929347,8.518267,-0.440479,-5.049213,-7.596681,5.167443],[-9.743834,-6.209433,5.932956,8.595323,8.859219,9.154043,4.914509,-7.608564,4.008799,9.043899,-6.540626,-8.200345,7.850250,4.735652,-2.888959],[-7.863752,1.782464,-2.260328,1.561859,-2.597904,9.941057,-2.922375,3.929252,-0.656362,4.238206,9.293781,-5.518904,-2.798120,-4.398500,3.670190],[-6.442631,-5.406062,-5.289577,-1.787379,-1.676651,-2.706782,5.360769,-6.231233,-1.477541,8.156645,8.085099,7.913458,5.879411,4.196652,-3.011453],[-1.815105,-2.352037,-0.686464,2.578101,-3.777421,8.022203,-2.651533,-7.081800,8.531627,9.326191,-7.206147,-3.059098,-8.808280,3.927308,3.402246],[-1.360150,-2.944733,-4.757865,4.439756,-6.833983,7.702081,7.616577,-9.293636,6.639769,-9.325208,-4.947582,5.467389,-4.931419,-5.886644,9.408123],[3.383259,-6.206374,-0.220114,4.248984,-6.651815,-5.519822,1.346114,6.815690,6.791851,-3.509480,3.359577,-9.667617,1.332863,-5.853629,-1.553110],[4.349307,8.624403,7.711081,1.486256,-7.176705,-3.413510,7.115823,-8.475342,8.535016,2.471072,4.956704,1.753752,5.125393,-5.471452,-9.813183],[8.719982,3.896634,2.788626,7.451742,6.580796,6.004661,-2.085384,5.959105,0.683476,-9.249692,-1.094304,-0.506142,5.161703,-4.959205,5.372870],[-7.066974,0.111978,-4.034079,-4.392279,6.464988,3.202869,-5.055346,0.419356,-7.490286,-7.636591,-1.083314,-9.275094,-2.262680,-8.771578,9.216440],[-4.146495,5.881400,6.585753,-7.332697,3.511639,4.444774,-3.856406,-7.409934,-2.465011,8.603215,9.841381,5.212764,-0.891857,1.463706,0.487967],[-5.514912,-0.371479,9.828778,0.056747,8.937636,3.309146,4.231471,-8.594962,1.197157,-9.145013,-9.950438,-9.589232,0.682225,7.340507,-1.256030],[-3.141854,-1.088028,-1.554017,-9.700327,-9.686334,-2.957067,0.874728,0.421505,0.547418,-6.510638,7.088676,0.822537,-1.625453,-9.105736,0.927355],[-9.836174,-7.324196,-9.918994,-4.305730,-2.469763,-7.969739,-9.089140,2.898501,-4.300147,5.634998,-2.742688,0.454958,-0.630642,4.744619,9.524543]],[[9.346635,-6.861470,6.678360,-4.385730,0.236004,-1.929494,4.814586,8.929565,-0.433588,5.436870,-2.076649,2.201811,0.732053,-9.926379,-6.128529],[3.378673,0.335759,7.598598,-9.378174,0.999459,4.513048,-8.487080,-4.084629,7.042534,4.960406,-0.481820,-2.801319,7.425601,-0.286215,-2.607820],[7.297396,-4.816933,5.865316,8.934816,-1.719130,-7.908570,-8.422674,-7.871944,-1.589474,-6.809674,2.070602,-4.599370,-5.591960,9.772405,4.226512],[2.766559,-3.834301,5.418467,-4.173129,0.269982,7.601238,-6.479967,-5.947427,6.397697,-4.795673,-9.286845,-6.870009,3.195360,-9.941496,6.796746],[3.219947,0.971680,0.442919,9.495701,7.906415,-9.508657,-2.419536,1.911553,3.193556,-1.998331,-2.138482,2.782194,5.456756,8.788824,-0.959424],[5.820801,0.574892,9.926380,6.328801,-9.068471,7.975485,-4.142271,5.172698,7.150947,-7.290539,-9.799254,-1.179436,7.531581,4.379682,-8.832738],[-8.928010,0.258741,-4.208774,-9.615539,4.071732,-6.059001,8.268725,1.637935,-8.519809,2.699736,-1.240957,5.298989,-0.861211,-8.464130,6.549933],[3.039170,-0.108892,-9.654289,6.248452,-7.656222,8.735991,8.092207,5.008327,-5.657505,6.195808,-4.799415,7.082158,8.049892,8.914631,1.074815],[-3.885147,-1.374920,3.188070,7.157355,1.878022,-5.146256,-8.357477,1.489023,-3.238362,-2.265312,6.794878,4.165683,-5.440370,-6.691432,-2.995015],[5.943750,-2.362050,8.451434,-8.566827,-0.798316,-9.928227,-3.148710,7.341874,7.388300,3.112956,5.661659,-7.460733,-4.040969,1.251446,-7.297621],[-6.543104,-3.010619,3.530099,8.155909,-8.789068,7.231027,-6.587781,-6.311991,9.519752,5.537492,4.184715,-1.927806,0.611578,-0.412979,9.420583],[-6.996433,-7.123206,6.693143,-8.625907,3.758409,-4.285466,5.238429,5.322029,-5.576888,0.653039,6.532901,9.439219,2.061277,-9.402150,9.264949],[-5.107389,-7.675243,9.639627,7.969012,-9.852268,-4.184785,9.797036,5.029990,5.453902,-1.843662,2.931105,3.674456,3.305769,5.470091,7.760193],[8.511630,-6.378096,-8.061491,9.367242,3.817494,0.213325,7.313763,1.222718,1.742863,-2.290595,-4.085753,1.074163,-0.170256,-8.279497,4.243910],[7.696881,5.348340,-2.845492,9.209740,2.922421,9.348167,-7.759035,-2.060079,8.936593,4.064523,7.960053,9.872739,9.906334,6.846820,0.868379]],[[9.754226,6.046449,-7.098610,3.968930,-2.343847,-3.007617,3.007169,-4.484892,-6.849633,7.360697,6.114020,5.053706,5.336337,3.933104,-9.513776],[2.163220,5.411107,9.494117,-4.448387,0.083918,1.699956,-1.376260,-5.457316,-8.495763,-9.878838,-2.673062,-8.063813,-6.319901,4.880050,-9.425841],[-5.355165,3.034126,7.327272,7.317729,4.931089,-6.454410,-3.246960,1.807227,5.308463,-2.458477,9.980944,6.143731,-3.581642,-7.729594,6.711614],[-3.032240,-9.658245,2.950098,-2.923328,-6.372520,3.227509,-1.252951,6.460712,2.819474,-9.369157,1.782741,-8.326338,3.995133,-3.336927,-1.902279],[4.280018,-3.599338,3.158534,1.285883,-3.227668,3.127966,-5.231723,-0.069912,-0.936963,-8.175570,6.524387,-5.449708,-3.751357,-4.826227,1.714609],[1.516651,2.329840,9.547755,0.799397,-8.305533,-5.202125,-4.292235,-4.270750,-9.481012,-2.407567,9.790606,-0.166652,1.200278,5.183521,-7.694553],[4.811102,8.362177,5.314096,3.696349,6.521595,-9.371020,1.441415,-8.829251,9.380443,-4.946979,2.513373,9.486429,-2.477294,5.102863,3.924250],[-6.913608,9.815540,6.355361,-3.248121,6.597416,1.640685,7.265766,-4.782235,-0.707239,8.786806,8.029439,-4.769191,-7.151522,-8.682520,-6.249341],[6.235773,-9.566346,6.313254,6.829829,-7.095099,6.403426,0.586133,-1.899524,0.416346,5.131878,-8.136563,9.948884,-6.303434,0.287063,9.176931],[-5.385683,-7.546255,9.621150,-1.535327,-2.446557,-3.827191,-1.862694,-2.555398,1.800450,8.022601,-3.197089,-5.827807,-3.339456,-2.785146,9.483540],[-8.760825,-2.149092,-2.028550,-7.126041,6.810540,2.434043,-4.736093,8.800397,-3.855650,-5.396979,3.748330,7.007211,5.355937,-1.797098,1.413445],[0.911594,0.381492,8.573567,-9.400526,9.705568,-2.620548,4.697520,-6.755638,1.281474,2.530693,7.003586,5.458557,-4.769125,-1.902529,-4.029817],[-6.261401,6.762496,4.500459,4.176170,-7.685952,4.096246,1.333196,-1.953152,0.955905,7.169037,2.297977,-5.281195,6.195388,1.426404,7.869093],[-5.402613,-1.522575,-5.224837,-6.412309,9.314762,-0.148671,6.408498,6.422894,3.612648,5.768256,7.421985,0.314766,8.619083,2.547479,9.476254],[-7.324662,-6.702256,3.493415,4.096342,3.877992,0.362756,5.058307,3.323075,-0.290470,-3.037850,1.424165,-0.147746,9.070271,-0.868586,9.959633]],[[1.943905,0.876014,-9.888132,-7.546260,-1.742181,-4.315616,7.374651,-9.631062,-5.244224,-6.856573,-8.677387,-9.874340,-6.676795,0.162716,-3.826511],[-4.495055,-0.076324,-3.076399,6.260664,-1.331490,-7.551656,9.279248,4.371942,-6.481748,-2.242835,-6.581152,8.520931,1.393924,-4.589025,-2.089021],[9.889792,-0.805971,-4.044034,-6.063488,-7.980338,7.535233,9.910871,-5.273826,-1.810721,-7.610205,5.680164,1.394612,-1.098318,5.027403,0.425965],[2.808159,-6.277540,1.837815,-4.217395,-0.071316,-3.128970,7.367503,-6.058907,-1.619226,1.935218,3.096913,0.419686,5.404863,-3.895582,-8.296752],[-6.077288,-3.223758,-8.494327,9.536809,-3.527680,3.261055,0.427564,-0.978547,-0.910713,-0.819127,-6.233645,0.562750,-5.396959,1.359583,3.111389],[1.500822,3.938567,-7.900002,3.066643,8.944257,-4.929744,-6.980596,6.318721,9.424905,-8.691932,7.493278,-0.533526,-1.919133,6.211016,0.877406],[-4.116424,-5.620945,-3.361246,1.289349,-8.155534,5.712522,1.452370,-7.549970,3.646673,-7.549024,3.102560,-1.634444,-0.724057,5.367404,-4.139745],[-5.373975,8.884293,-8.011166,-7.871437,1.614275,-8.516405,5.820996,-6.914055,7.292252,7.965933,6.548211,9.273041,-9.318349,7.946054,-0.206410],[-2.017275,-7.850354,6.564236,-1.057831,-8.576135,2.999776,-0.752385,-1.262261,-6.083817,-2.967301,7.053975,1.302757,8.662347,3.828502,4.973280],[-3.031576,-1.370289,7.104094,-9.342240,1.798106,0.231401,5.591727,8.690858,-4.986015,0.960369,-4.162511,6.913103,-1.459183,3.685993,9.451381],[1.401250,5.549481,-3.002424,5.472259,-5.228943,4.623151,4.509410,6.750116,-8.678124,1.314486,3.602198,-0.839183,6.876073,8.927916,-0.296265],[6.931028,3.851138,-2.955884,8.705140,-8.684513,-6.107362,5.375939,-2.297921,3.883830,-0.902725,6.101760,-3.906849,-1.995584,-1.868793,-4.609494],[-7.955469,-1.115922,-0.723303,6.486736,-5.057216,2.908721,0.786082,5.952118,-7.814143,-9.489557,8.194718,-4.539903,-6.826763,9.190837,-8.464360],[1.574773,3.491046,-5.700968,-6.395580,7.817501,3.664532,-0.232916,9.119860,4.010868,-2.239041,-9.489682,4.068143,9.586769,-0.396035,-4.933958],[-5.616398,9.611428,7.200369,-3.081634,-5.253226,-2.520261,-0.164727,-3.440852,-6.346692,9.534324,-7.780333,-7.854322,-7.108522,4.899060,-0.590134]],[[-0.995089,7.765438,-3.407499,6.477390,9.826001,-9.352355,-7.362454,-2.657424,-8.085564,-8.574820,2.062390,-2.897567,-2.984104,1.602256,6.163531],[7.939766,-5.076832,2.313800,7.103841,7.577279,-4.468296,-2.997643,1.035688,-0.116155,-0.261960,6.583998,2.226320,6.493394,6.032654,3.888816],[9.781632,-1.278259,0.831182,-9.035352,-3.991377,8.706421,-7.810714,9.924985,-0.122825,6.672914,-7.291605,-7.275322,-5.540148,2.597092,-9.628572],[-5.169013,2.555129,-1.841741,2.214548,4.423935,-1.636152,-4.458013,7.843127,-5.925735,0.349667,-9.918271,5.177168,2.915012,-2.950280,9.792706],[3.647940,-4.334308,-7.393977,-9.478739,-6.512410,0.917404,-5.090915,7.329503,-5.335009,-8.977273,2.194543,4.170791,0.508200,6.814465,-9.882333],[8.474297,-8.586170,-4.388957,-1.838223,-5.913700,5.859020,7.062583,-3.249291,4.322106,0.168216,-9.277162,-1.663284,2.115158,3.475817,0.053743],[3.036375,2.025719,9.680600,-9.568348,-9.625458,-4.448679,-5.071608,-5.691064,-8.886805,3.291754,2.402896,-7.503941,-8.510641,9.711229,-3.427059],[8.507131,3.809132,-5.141464,-9.280801,-1.105149,9.931690,-0.178693,2.286750,-9.874339,-8.123176,1.294550,-1.362536,2.521192,5.077194,-2.608465],[-6.521482,8.654543,-5.157295,-0.795628,-3.847228,-4.892219,4.608327,0.761784,1.394630,-6.086777,-1.985490,6.893657,2.293812,1.540141,8.899766],[5.840244,2.245375,-4.518531,-7.013259,-0.577858,1.057917,-5.713565,-9.972198,4.785869,-2.362067,8.180144,6.403546,3.359415,-0.557474,2.726621],[-0.373996,1.740344,5.215534,5.069659,-9.604976,-1.172865,-9.335888,-8.842017,9.268049,-7.086949,2.746716,-2.366640,-2.107067,1.505166,-0.808049],[2.667629,1.784619,-5.938684,-7.229856,-7.871131,7.367456,-3.125920,-9.997029,-8.961001,5.321060,9.656296,7.775770,6.898522,7.004785,-7.613111],[-6.706950,-7.002852,-1.451604,-9.905185,-0.537744,7.442765,-0.250264,-9.190144,-4.632492,-2.395196,2.325790,-9.849462,3.744293,9.514571,-7.677799],[-6.369149,8.986219,9.106801,0.545728,-7.152071,-6.842471,4.286418,1.185478,4.494611,8.747143,4.239826,8.542272,5.217071,-4.935857,8.470088],[-3.658601,8.347656,-8.794985,1.243333,-7.091038,-8.076062,2.631542,9.704869,9.752331,-0.656735,-8.846166,0.963702,7.709406,-8.959027,0.439030]],[[-8.604170,9.428894,3.055067,-9.000578,5.645503,-8.811625,-9.846905,-2.088269,7.540946,-0.350650,-6.847257,2.689216,5.992672,-0.277835,-2.932109],[7.051272,9.554088,-8.995356,3.655740,3.444790,-0.794718,-7.372497,1.692761,-7.641731,-6.674281,-8.872647,-7.173668,-7.928504,-6.353873,7.698673],[5.029946,7.771642,-0.224336,7.703921,4.330509,-4.354389,6.790441,-6.785283,4.983154,2.896405,6.622264,-9.343177,1.286887,3.625318,2.725858],[3.957706,-9.081708,3.049453,-9.817003,-0.231147,0.457009,4.018666,7.766853,6.547006,1.438522,-8.155307,-6.731880,-9.794018,5.322758,8.649374],[-7.247021,7.676137,-5.156974,2.773851,-2.097702,-1.315352,2.734874,-6.086829,3.488529,9.934127,-4.364805,8.059792,9.410071,-1.158087,-9.162383],[7.565489,-6.007416,0.180269,-3.190265,-7.213806,-6.370053,-2.983779,-8.537269,-3.860083,1.612350,-0.177618,0.559815,-6.140906,1.791418,8.596791],[7.165306,3.502788,-3.326629,-2.641603,9.498303,0.987398,6.983145,6.099236,-2.029821,3.463370,-8.336597,8.496646,0.695312,-1.584462,-3.031657],[-1.880775,-5.345447,-0.410124,-1.259549,2.147535,6.936015,1.829645,4.550698,-5.595509,-7.655867,2.391558,-8.006092,-6.235067,-6.599882,-6.196446],[4.364994,-2.854394,-7.057469,-6.254067,4.153642,6.975623,-5.272636,1.301371,1.671302,8.984805,0.099798,-2.612013,2.892045,-5.553843,6.968914],[-6.217371,5.133058,1.404853,7.868085,5.404633,0.080967,3.169332,7.268813,9.265680,6.725566,2.768054,4.895499,-7.635043,-7.912032,7.950205],[8.151569,-9.238433,-7.020917,9.625459,9.245643,2.719642,9.143772,-5.008020,8.094520,8.542071,-1.848669,-0.268529,1.123657,-2.842241,3.848147],[8.911082,-8.323985,5.390487,2.940895,-8.289538,9.825107,-5.487054,5.316075,-7.637358,-2.155052,6.609343,-7.683800,8.527396,-3.726317,8.948087],[6.699216,-1.384187,5.169303,-4.785433,-0.519100,3.372547,-0.231754,-2.051890,6.562348,8.016631,5.298940,-2.028963,-9.148456,8.936702,-6.989936],[-8.726445,2.801392,3.868896,-4.270080,-9.122760,-4.077251,6.781767,8.797460,-0.141501,-2.234489,-9.770754,-3.796229,0.574503,-7.363662,4.356033],[1.476563,-7.690572,0.738604,3.671783,-8.644911,-1.773814,-9.804921,4.900961,-5.909941,-3.815528,9.865709,-3.677937,3.673593,-7.771278,-2.506738]],[[-8.219197,0.776887,-8.068744,-2.085134,2.894331,7.284495,-9.260929,0.398674,3.223729,9.364583,-9.701543,6.908654,4.272292,-4.877707,-3.851204],[2.499279,-9.818501,-8.171608,8.829270,6.399520,7.541756,4.405252,-7.102475,4.189355,-7.601218,9.542939,-0.502609,5.372925,3.607146,0.787374],[-0.989431,0.544568,-4.744908,4.120388,-2.474309,-3.467993,-6.534537,1.380943,-6.412630,-8.432841,-9.105407,3.942249,-3.184695,-3.755414,-9.955735],[-9.627072,-6.647127,5.571869,1.120038,2.735637,2.567839,1.824034,0.620124,-2.005780,7.402542,-6.553996,-6.569148,-1.218339,-2.466083,1.455616],[9.480305,2.422214,4.726295,-5.815710,9.324600,-4.519290,3.424484,-3.014326,4.926154,-7.473114,-3.927992,-8.756491,-1.254279,4.385282,2.809203],[3.220605,-4.091100,-5.696136,5.365171,-7.283469,-2.063850,-3.919746,-5.929296,-6.755666,6.462309,2.735831,1.379748,6.480600,-9.242151,-7.404517],[6.366020,-2.964863,-6.862378,0.056355,4.944795,4.779640,-5.977053,8.733557,-6.668617,-0.981704,-1.397799,3.176725,1.157307,8.620661,-5.331020],[4.451937,0.878754,6.220471,9.624426,-5.901247,6.833181,-6.694469,5.260940,-4.027744,-9.560989,9.347812,-1.139759,-2.729878,6.517256,-4.785296],[-6.365277,5.524812,2.231421,6.974099,0.065934,-3.707190,3.138861,6.125160,-7.045071,3.114185,-5.032799,-7.127046,8.975739,1.279220,-8.660616],[-6.707005,1.447272,9.455158,5.653142,3.661437,-3.855348,5.093375,0.418816,-3.778775,-6.586310,-0.927032,-3.546017,-7.437096,9.489775,6.222464],[7.113939,-2.567115,2.335527,4.719213,3.443951,-1.137696,-1.103456,5.463520,-8.940036,-0.775839,3.883521,4.001099,7.112154,-6.467075,6.518353],[-2.827969,7.748776,-5.736013,-4.462576,7.594639,-7.665300,0.975104,7.074584,-8.683713,-5.276189,6.000754,7.814285,-7.918111,-4.322557,-0.110694],[-8.639127,-6.669699,8.808478,-1.449928,-1.987584,6.760488,8.748954,-0.549339,-9.863197,-2.634739,8.213256,-8.004737,5.198079,8.114396,5.693506],[2.787725,-4.658545,-8.497396,-5.381325,-7.081487,-2.060931,-7.106748,-3.976896,1.410715,1.369517,-3.314183,8.236481,-0.400315,0.500808,-1.325878],[8.905896,-8.344016,1.248758,7.348966,1.814388,-3.056106,-4.471746,-1.012964,3.498259,2.620849,2.943740,0.256917,-5.541428,2.308191,6.423808]],[[3.031224,-6.789259,3.574610,-2.304515,4.708847,-0.247438,0.590479,-8.935533,5.543402,0.138717,5.444540,-8.032751,2.593832,-0.952216,-0.101711],[-6.337577,-8.032648,1.263764,-0.779424,-3.707571,-2.578342,-7.111861,8.489058,4.853346,-0.633993,3.281832,8.420629,7.266889,1.246696,-5.074542],[1.557483,1.797576,3.793379,7.967163,-3.492185,1.347453,-3.832716,-4.559316,9.829123,5.783610,0.294081,5.534116,-8.661782,1.600316,-5.118678],[-6.733143,1.710969,2.987864,-6.238635,-7.528118,-9.760181,6.770434,8.482838,8.872779,0.701954,1.278661,2.768464,-4.273735,0.731902,0.363015],[1.265508,6.045949,3.806548,3.610561,-8.792592,-3.997649,4.017576,3.733265,-8.739018,4.997238,3.832957,-2.319748,7.086388,9.084608,-7.741283],[-7.042498,-0.691384,-8.380939,-1.049637,9.391035,-4.848447,-2.675511,-9.803708,-4.352956,-4.070106,-9.015796,-2.218860,-9.974790,9.466967,-1.547528],[3.876847,7.676001,2.775828,5.938157,6.458876,-0.868700,0.395732,-4.201116,-0.317513,-7.373452,-6.668168,9.724607,9.787459,0.959501,1.434163],[-9.742440,-1.897341,-0.968892,-7.179304,-8.642552,-3.995809,1.677705,5.154632,1.685376,-9.032781,-9.344515,4.265198,-7.090537,8.336793,4.804258],[3.482323,5.462282,-0.634647,3.031319,-7.272463,-9.677942,-3.688238,-6.557353,8.475968,-2.882829,1.140414,3.785809,-6.363688,4.096925,6.913391],[-9.447189,-0.408711,-6.323060,6.225648,2.267196,1.436817,-4.517825,2.370503,4.358993,1.879296,7.065483,-1.217221,0.755609,-7.410188,8.277336],[9.526401,-3.149651,3.994440,-0.257572,2.678755,-0.730929,-7.525463,-4.827429,2.161688,-0.380961,7.808606,0.925141,-2.261409,-6.076133,7.960381],[-5.359656,3.930347,9.071641,-7.976847,0.452990,2.442035,-5.388354,9.031926,-0.061495,2.128403,5.458933,-5.381608,-4.244021,8.821470,6.613200],[-4.565733,9.018524,-7.579400,0.135097,7.924044,-5.079198,-9.865501,-5.556116,-1.072140,5.826782,5.706095,-1.637195,1.749883,8.311416,-5.808800],[-8.505358,-8.479895,-1.935801,-8.183215,1.065531,1.290500,-0.818751,0.960743,6.885489,2.051122,5.029189,6.202004,-2.921160,-7.883636,7.693121],[-5.886049,-6.824034,3.809815,-8.257263,-5.809921,3.590555,4.017127,6.617985,-8.970321,-3.176959,2.248089,6.079619,-5.049206,-8.213879,5.279445]],[[8.109918,9.477224,-9.234300,-5.504192,-5.139595,7.429524,-6.630102,2.406366,3.674612,-7.472609,-5.351161,5.817332,-2.325361,7.613378,-0.755297],[-5.948936,3.111860,7.217183,3.420932,-6.591529,-8.532937,9.408791,-4.153056,1.378224,5.352705,-7.538915,6.158917,5.764435,8.814643,-4.538270],[4.241519,7.024872,-5.992781,-8.114596,-1.108819,5.563100,-7.988633,-8.523253,-0.317656,-0.655214,1.974290,4.848162,-6.488772,0.619747,8.709817],[-7.609588,-8.516316,6.965416,-7.010795,-4.284188,-7.793162,-9.936518,2.611903,-5.011020,-2.445451,3.455002,7.405227,-5.097715,0.002575,3.440149],[-6.485928,5.019556,4.727772,9.076043,-2.252772,-0.728458,-2.448507,-6.032951,1.784400,9.863744,9.421645,-7.936722,0.280975,4.280193,-2.829471],[8.711040,-1.342899,8.094193,-2.808311,6.157864,7.717033,1.207713,-5.131717,0.396583,-7.041988,6.829577,4.347908,-9.169617,9.293461,0.904639],[-3.280772,-7.706814,2.702976,-8.244237,-8.928109,-2.068644,-8.829776,5.724596,9.068843,-1.606995,7.482368,-8.405910,5.060178,8.464127,-8.103444],[-5.518815,-4.274517,7.986512,0.427669,6.721007,7.791581,9.213398,7.702641,9.993372,4.249308,6.115476,5.944363,8.079531,-2.476084,7.283260],[7.292269,-2.497665,-8.784066,4.783895,6.786520,-2.255522,-7.915187,-5.840312,-0.774321,2.251202,-5.885937,5.153732,-0.787542,-0.211559,7.597141],[8.538979,-5.538807,-6.363247,8.241441,-8.133297,-2.698251,3.789897,-6.534034,9.493030,8.646284,-0.734839,2.034892,-6.604968,-1.394049,-4.467737],[-4.414474,-2.649090,2.874890,-2.675377,-9.058445,-1.637087,0.726679,3.356008,4.815971,-7.064443,4.759486,-1.845706,-3.312976,-4.685293,-2.200328],[0.942836,-8.196662,8.393343,-9.121358,-5.808692,-1.411702,-8.697395,2.144900,9.784259,-1.202927,5.911453,-4.642513,-2.701195,-9.411333,0.688816],[3.773510,-5.161899,-1.512712,-7.719693,7.525205,5.316649,4.406365,1.075331,2.947850,0.496325,-3.136376,-2.759997,4.728644,-1.011781,9.226745],[-5.622904,-0.922724,2.418782,-1.211621,2.915814,-8.634118,9.792792,-9.941143,-1.539249,2.870045,5.427353,3.262706,-6.772026,-2.764428,-3.758352],[-3.284181,0.944471,6.633221,1.470514,-0.358496,4.568287,2.424443,-7.429057,5.180425,4.464728,-6.311169,7.487642,-6.979847,-2.950147,-6.354220]],[[0.631525,7.064249,0.549918,4.970231,-0.687653,9.508526,-4.422632,-0.269303,0.039652,-8.393837,-7.568588,7.639376,-3.458307,5.850731,6.432269],[3.403676,-2.766627,3.165724,-9.636851,-7.630668,-0.863340,-0.645330,-8.540410,4.238958,6.914953,2.578226,-9.664574,7.052327,-8.625239,-2.801319],[-0.096129,-3.768298,-1.237182,-4.314131,-9.011776,-6.043906,-4.830449,-2.068790,2.816828,-6.688140,2.601223,5.705778,6.031089,-0.524594,9.836860],[1.147962,-4.269680,0.326766,3.793147,2.893809,-8.471945,-5.208546,8.289797,-0.448043,-1.000830,2.461912,-8.325631,1.133068,4.239921,0.728533],[-5.938141,-9.086469,5.826908,-4.062120,8.703737,-0.736662,6.597781,-6.755926,6.454489,1.010418,-7.414327,8.445203,8.347423,-3.003363,-9.038919],[-9.787486,-2.121242,-5.485365,-0.672572,-1.002419,-3.568599,7.635726,6.330449,-6.651659,-1.673688,-9.144054,-0.431265,0.375502,-9.622308,-9.973424],[-4.773155,-3.618479,0.268742,-9.735745,0.813215,2.115619,8.885228,2.073264,2.861057,-7.208916,3.822036,-5.069346,-3.139577,-9.928905,0.300595],[-1.585549,1.824268,-8.345414,5.336673,-3.929591,8.852265,-2.550677,-0.773241,7.141934,-3.635824,-2.242421,-2.351658,4.122486,-7.314121,5.916252],[5.351947,5.235470,-8.592115,5.070796,-2.864470,-3.753595,-7.603280,0.741263,-8.210346,-0.085267,-1.601841,5.951995,8.234091,1.052978,-3.418633],[7.819268,-3.578888,-5.700494,-8.953032,-6.811335,7.952901,-1.638383,-8.210982,-3.964966,-6.354613,0.187132,2.538485,3.584154,4.940249,1.563173],[1.396466,5.516284,6.323236,4.626354,-9.329417,1.708384,-6.061040,3.514411,6.601313,-0.484599,-9.821404,-4.682514,-7.516924,-2.018177,-7.746685],[7.892339,-4.317444,-5.566198,-5.264542,8.491063,8.323309,-7.268766,-8.929247,-1.267611,6.189252,7.026363,-8.431597,-2.083755,3.823954,0.635843],[-4.506470,6.532765,8.848400,-2.118231,8.411067,-5.791622,-6.865247,2.912988,-6.716745,-0.909376,-8.071038,1.248065,7.837966,0.642021,-1.041593],[0.192104,2.026102,0.977862,-8.855160,-1.908540,7.070188,-3.787602,4.891524,-7.435495,-9.309984,1.734191,-2.321519,4.230756,-4.606326,-4.423241],[2.392356,9.840704,6.125168,-2.708994,2.581821,7.314077,0.171500,-9.218020,5.309398,2.205108,-4.464643,-8.214494,2.992973,-8.857751,-3.893514]],[[4.619085,-2.750608,-4.876777,3.056811,6.692368,9.097811,-6.529532,3.694227,4.021403,0.719524,-6.468221,-1.780154,0.133448,-8.121735,2.741214],[-3.024008,2.569780,-5.902599,-4.514774,-8.279221,-4.211026,3.598318,-5.261880,4.733361,7.990004,-8.411984,-9.825033,3.965763,6.925229,-5.170055],[-7.546256,6.553386,4.832681,-3.545143,8.671795,-2.494736,-4.017547,-7.914641,-1.855960,5.369738,1.773197,9.123114,-1.839213,1.350310,-9.466769],[-6.408836,-0.778114,-9.353707,8.770754,-7.876366,5.536524,-2.083572,-8.501023,0.851876,5.944343,-5.104865,-6.848703,-5.321215,-1.563696,-4.455398],[2.966730,-9.960943,-5.101370,-4.521739,1.341112,6.549704,5.889730,-2.023280,-0.527618,-9.157957,-9.983510,-3.632108,-7.293054,9.623020,-6.600678],[8.752780,0.075265,-7.933019,5.616698,2.257237,7.862891,8.875581,8.166076,-0.395417,9.098933,3.165708,2.144105,7.301719,-3.131968,1.527489],[-3.853214,2.689029,-3.629283,-9.702851,-1.105729,-9.325605,-2.135170,-6.233169,0.357232,2.823470,8.440893,9.282259,4.435580,-9.535568,0.887883],[-9.405337,-6.067117,3.966554,8.576516,-9.015857,-0.444079,3.184050,2.588360,-1.055676,-5.516883,5.754461,-7.394650,4.253519,4.683722,9.060152],[8.903349,3.284921,0.646836,-3.665450,-7.827728,-7.185717,9.442629,0.674484,3.380704,4.720001,3.068656,8.175325,4.562124,4.291163,-4.668606],[-4.393679,9.815560,-7.418403,-3.585084,8.196622,0.737589,7.897858,-5.175461,3.668118,-0.318196,5.405876,-1.839104,7.753071,9.811856,-5.261628],[-8.966962,2.755204,-4.976982,-4.811554,-7.339082,0.525684,-3.703687,-8.701186,3.168225,-6.685008,8.845544,-8.143635,3.534066,1.773600,-4.460954],[-7.686329,-8.405983,-7.462240,5.372875,-5.618335,2.122623,-5.692754,-7.432676,-7.900454,-3.970125,-0.513665,-9.926144,5.643229,-3.292709,4.349522],[3.320049,0.628236,3.475007,-1.288968,4.809647,3.651208,0.913374,-9.563866,-0.295425,7.653993,7.320106,-5.714168,-8.330278,6.685306,5.525738],[-9.306590,8.273830,-1.760011,6.413893,3.617066,9.926997,3.757275,-6.923626,8.631099,-0.099177,-2.342168,-2.870819,-3.567420,-1.259999,3.517217],[-9.015513,-0.475398,-7.227672,-7.608266,-8.072926,-9.549912,-3.342934,-1.557748,7.608416,-0.612990,-9.417370,2.947104,8.639046,-5.016490,-6.122741]],[[9.591882,1.215269,-5.074680,2.842497,4.071329,-4.221641,0.180319,-1.347645,-9.255159,6.155594,2.997657,7.049117,-0.887605,-0.441560,-3.634406],[3.986394,1.159601,-9.798274,-6.459464,7.705705,3.451466,6.509330,-5.861234,-5.383934,2.476713,9.852537,9.287643,0.228203,-7.679861,-9.138149],[-0.158230,-3.919150,-1.474760,0.112867,-1.449338,1.874131,7.734937,9.575802,-8.016201,-3.286587,3.006984,-4.774229,-1.165780,6.502656,-9.406659],[1.048485,3.684351,-4.461825,-1.896006,-1.492703,-6.660149,-3.998349,-6.870972,-2.618343,0.636553,-3.630456,-7.593341,-1.151705,-1.815767,4.124232],[4.885667,-0.664337,3.695793,8.058841,-4.830932,-2.085488,3.974619,-0.925673,-0.290467,-5.109479,9.640083,9.192740,6.418737,-6.594597,3.721742],[-2.886081,6.510619,5.833098,-0.318042,-1.752065,-2.885158,9.502439,-7.197463,0.394629,-0.926871,-1.856555,-1.332438,-6.442993,3.150162,2.517435],[-4.243717,-5.354706,-3.367775,-8.358446,-3.157492,-9.695324,-0.147666,-7.374199,0.310519,4.899686,9.666918,-9.898042,0.964795,0.857098,3.820322],[8.111031,2.030276,1.231135,9.737320,-7.807535,8.828605,-4.837551,-7.115276,-2.692116,-3.692435,-7.499015,0.712817,1.598354,4.436361,-9.282556],[-4.914040,-0.955920,7.039576,8.773807,-9.657698,-2.756510,-6.627947,8.894172,5.977379,8.417315,2.197898,6.571806,-0.345243,-4.161691,9.903310],[-0.314484,-7.853631,0.115925,2.236660,6.691404,-5.043433,4.654276,-6.333728,-3.515931,-2.626693,-0.646939,8.656783,-2.544112,-2.075590,0.806068],[9.984819,5.527945,-1.599919,4.931836,-9.500426,8.929528,-7.805843,0.369866,2.929582,-2.079539,8.691796,-1.932130,-2.412942,-1.952277,5.716806],[2.707966,-7.960334,-4.987204,2.397932,-1.560640,-8.293586,5.005225,-5.775028,-7.150724,-0.939702,3.852952,5.756871,-7.168738,-0.883862,-2.930273],[-8.690928,4.558231,9.870379,4.923733,5.428826,-9.577392,-9.784752,6.976248,-9.225553,-0.242620,-5.819537,0.363462,2.825007,-2.495641,-7.351339],[8.898737,-9.360050,9.341703,2.500608,-0.471860,-6.478869,-7.650734,-1.404088,4.303233,5.612129,0.040125,2.436922,5.354961,-9.996400,2.511470],[3.027275,1.323226,3.565542,3.781510,-1.277784,4.720015,-7.566013,0.567189,6.732564,2.010409,-3.007536,8.452366,2.332814,6.126813,-8.105826]],[[8.485622,3.331026,7.865207,3.673754,5.481179,-6.257336,9.344861,8.087643,-2.551843,4.500472,3.216882,-0.483761,-7.491455,-7.970351,-2.025035],[-4.247559,-3.180035,-9.231665,-2.723237,-7.676022,1.412928,-1.128339,7.320139,2.101835,8.965719,8.174388,0.336028,9.172849,-5.857726,5.018832],[-0.482126,-4.216166,3.473557,-2.348259,-5.245920,-8.176487,8.502362,-8.719283,-9.018506,-5.973963,7.373880,-0.924997,-0.202150,-4.597903,4.701498],[3.234383,5.429623,-3.237611,-5.745546,-4.688053,3.536787,4.114152,6.333397,3.208676,4.357620,0.805457,-4.909238,8.766028,6.266987,1.229184],[6.945833,-8.168522,-5.629704,-1.288209,9.973030,7.121118,8.775068,-7.036873,1.077475,-9.043905,7.018915,8.999912,3.959340,-9.231358,-0.556648],[-4.743193,-0.026122,-8.402698,1.628840,-5.237967,1.596300,-0.867504,-4.404893,7.229226,-1.909035,-7.726956,-1.510607,5.343984,0.974200,-7.161957],[9.114214,0.016158,-7.274409,-0.946078,-4.077836,-5.243945,0.237776,-3.041792,2.281326,2.673423,7.973855,-9.201949,1.377667,-7.425744,0.355153],[-0.654583,9.218812,1.143915,9.695862,0.522844,-3.354307,2.757274,-8.972427,6.955116,4.590836,-9.315777,-8.020069,-4.108931,-7.057198,-8.212720],[-7.726368,0.026093,4.096555,7.028946,-8.701285,-5.619593,-3.665968,-4.500558,-2.136791,9.281669,-7.674642,-2.931790,-4.411552,-0.867207,0.195568],[-6.398896,7.868809,6.483502,-6.376014,1.664213,-4.660987,3.810276,0.506120,3.217651,7.247860,-3.842226,-6.450149,2.540366,9.549604,-6.157184],[-1.373141,-6.558446,-4.750931,-7.381168,-8.723968,9.743737,-6.062478,-3.337725,7.089518,2.606846,-8.300980,-5.874378,-7.947785,8.637348,-4.072885],[0.838592,-4.350329,-1.703676,6.559142,-8.328295,8.364514,-4.544841,-2.401290,1.098720,8.183586,9.701396,-1.097882,-2.303505,8.845157,1.903916],[1.359747,-0.906891,-5.511090,-2.568553,-4.263112,-2.220123,8.902004,1.189032,1.473702,5.991313,9.938681,-1.852678,-6.872632,-0.427719,-2.040194],[2.197029,-9.205560,4.431635,0.153934,1.891342,-6.519869,3.808904,-9.894251,-6.778367,9.593791,-1.103471,-4.478337,9.344738,-7.347947,-8.379986],[0.250357,-1.351083,7.917945,-1.823381,-8.325389,-9.085889,9.196148,-4.166807,-1.291661,9.445298,-4.760046,-9.139018,-5.783716,8.146173,-2.582442]],[[4.134684,-8.900229,9.577267,-9.058098,-1.075777,5.998432,4.992577,-4.713118,6.054163,-0.576819,-7.533385,-4.732806,8.145356,-3.615041,2.512890],[-9.672255,-9.795954,3.180798,6.879815,-4.500743,-4.383897,-5.416803,-5.920717,5.449872,-2.871616,9.932798,-8.495445,7.234715,-5.811464,-2.121332],[-2.549773,4.566315,8.734073,3.863483,-8.890817,-2.140712,7.917551,-4.043089,3.715653,7.384037,-7.549752,7.056912,2.936729,-3.285394,-2.317823],[8.339621,-1.075980,-8.938489,2.027044,-3.818949,4.501777,-4.343750,3.269479,-8.458887,-2.150937,-8.097622,-6.035523,1.379519,3.051618,-4.113508],[0.771759,-4.388733,-8.044768,3.745942,-6.958785,6.690202,3.461775,7.934896,-6.796751,4.251585,2.000845,8.383300,9.236212,0.001259,4.033135],[3.633533,-0.216374,-0.956937,-2.338897,-2.879397,8.000879,-2.633163,-2.278356,5.862141,7.851094,8.260024,9.960645,7.269877,-9.915768,4.013254],[-2.882885,-1.583731,-8.118771,6.892058,-7.013698,-4.204596,5.887164,-2.797352,-6.081443,-9.403234,9.769994,-7.007802,0.045304,1.366443,3.690520],[9.829856,0.696596,-5.355640,-4.740863,-9.528327,5.739807,-1.622521,4.368435,-8.166899,-4.495044,-9.128660,0.559453,-3.251473,-1.023650,-4.862011],[-6.844287,3.360047,5.323452,-5.563504,0.951006,-1.152405,2.264064,4.612729,-7.997575,-1.124186,-7.338422,-1.252761,9.821093,-4.167772,-9.314522],[1.919657,-6.491672,7.105948,-1.096771,5.192771,-8.301852,4.832448,-1.803047,6.609290,-0.220436,-1.880103,-2.993936,-5.636643,5.663978,3.327089],[2.209219,0.794628,3.145557,7.713940,-1.940278,9.968011,3.005897,-7.549325,4.647129,-4.524528,8.310689,-7.574263,5.943114,6.447496,-7.358910],[-5.992704,-8.741984,3.534022,-6.659992,2.850623,-4.269172,-0.562304,9.832723,6.392861,-5.593390,2.457707,-1.292841,0.335791,-1.645572,4.564686],[6.431649,3.829193,2.934735,5.918302,6.694009,-5.566537,5.800671,0.400786,3.260783,5.789024,-4.660979,9.715367,-3.430309,-1.819168,1.560919],[9.656518,-0.474756,-4.288018,-9.346622,4.360564,1.158151,6.648346,-6.187000,9.467990,7.040622,5.790986,7.667306,6.997191,8.948409,2.535625],[8.593913,6.863312,0.941000,7.133197,7.883764,0.226742,-0.369592,0.753217,-8.578117,-7.242611,5.698559,1.380260,-6.665118,9.862545,2.423170]]], dtype = "float32")#candidate|4059|(15, 15, 15)|const|float32
uop_4060 = relay.acosh(const_4059.astype('float32')) # shape=(15, 15, 15)
func_1080_call = mod.get_global_var('func_1080')
func_1082_call = mutated_mod.get_global_var('func_1082')
var_4076 = relay.var("var_4076", dtype = "int8", shape = (168,))#candidate|4076|(168,)|var|int8
call_4075 = relay.TupleGetItem(func_1080_call(relay.reshape(var_4076.astype('int8'), [8, 7, 3])), 2)
call_4077 = relay.TupleGetItem(func_1082_call(relay.reshape(var_4076.astype('int8'), [8, 7, 3])), 2)
output = relay.Tuple([uop_4060,call_4075,var_4076,])
output2 = relay.Tuple([uop_4060,call_4077,var_4076,])
func_4079 = relay.Function([var_4076,], output)
mod['func_4079'] = func_4079
mod = relay.transform.InferType()(mod)
mutated_mod['func_4079'] = func_4079
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4080 = relay.var("var_4080", dtype = "int8", shape = (168,))#candidate|4080|(168,)|var|int8
func_4079_call = mutated_mod.get_global_var('func_4079')
call_4081 = func_4079_call(var_4080)
output = call_4081
func_4082 = relay.Function([var_4080], output)
mutated_mod['func_4082'] = func_4082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4103 = relay.var("var_4103", dtype = "float64", shape = (5, 2, 6))#candidate|4103|(5, 2, 6)|var|float64
uop_4104 = relay.rsqrt(var_4103.astype('float64')) # shape=(5, 2, 6)
output = relay.Tuple([uop_4104,])
output2 = relay.Tuple([uop_4104,])
func_4107 = relay.Function([var_4103,], output)
mod['func_4107'] = func_4107
mod = relay.transform.InferType()(mod)
mutated_mod['func_4107'] = func_4107
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4108 = relay.var("var_4108", dtype = "float64", shape = (5, 2, 6))#candidate|4108|(5, 2, 6)|var|float64
func_4107_call = mutated_mod.get_global_var('func_4107')
call_4109 = func_4107_call(var_4108)
output = call_4109
func_4110 = relay.Function([var_4108], output)
mutated_mod['func_4110'] = func_4110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_4127 = relay.TupleGetItem(func_329_call(), 1)
call_4128 = relay.TupleGetItem(func_330_call(), 1)
output = relay.Tuple([call_4127,])
output2 = relay.Tuple([call_4128,])
func_4129 = relay.Function([], output)
mod['func_4129'] = func_4129
mod = relay.transform.InferType()(mod)
mutated_mod['func_4129'] = func_4129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4129_call = mutated_mod.get_global_var('func_4129')
call_4130 = func_4129_call()
output = call_4130
func_4131 = relay.Function([], output)
mutated_mod['func_4131'] = func_4131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_4196 = relay.TupleGetItem(func_776_call(), 0)
call_4197 = relay.TupleGetItem(func_778_call(), 0)
output = call_4196
output2 = call_4197
func_4215 = relay.Function([], output)
mod['func_4215'] = func_4215
mod = relay.transform.InferType()(mod)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4215_call = mutated_mod.get_global_var('func_4215')
call_4216 = func_4215_call()
output = call_4216
func_4217 = relay.Function([], output)
mutated_mod['func_4217'] = func_4217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4215_call = mod.get_global_var('func_4215')
func_4217_call = mutated_mod.get_global_var('func_4217')
call_4220 = func_4215_call()
call_4221 = func_4215_call()
var_4222 = relay.var("var_4222", dtype = "int32", shape = (8, 7, 3))#candidate|4222|(8, 7, 3)|var|int32
bop_4223 = relay.multiply(call_4220.astype('int64'), relay.reshape(var_4222.astype('int64'), relay.shape_of(call_4220))) # shape=(8, 7, 3)
bop_4226 = relay.multiply(call_4221.astype('int64'), relay.reshape(var_4222.astype('int64'), relay.shape_of(call_4221))) # shape=(8, 7, 3)
func_2441_call = mod.get_global_var('func_2441')
func_2443_call = mutated_mod.get_global_var('func_2443')
call_4253 = func_2441_call()
call_4254 = func_2441_call()
output = relay.Tuple([bop_4223,call_4253,])
output2 = relay.Tuple([bop_4226,call_4254,])
func_4260 = relay.Function([var_4222,], output)
mod['func_4260'] = func_4260
mod = relay.transform.InferType()(mod)
var_4261 = relay.var("var_4261", dtype = "int32", shape = (8, 7, 3))#candidate|4261|(8, 7, 3)|var|int32
output = func_4260(var_4261)
func_4262 = relay.Function([var_4261], output)
mutated_mod['func_4262'] = func_4262
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4268 = relay.var("var_4268", dtype = "float32", shape = (4, 7, 2))#candidate|4268|(4, 7, 2)|var|float32
uop_4269 = relay.atanh(var_4268.astype('float32')) # shape=(4, 7, 2)
func_3499_call = mod.get_global_var('func_3499')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_4273 = relay.TupleGetItem(func_3499_call(), 0)
call_4274 = relay.TupleGetItem(func_3500_call(), 0)
output = relay.Tuple([uop_4269,call_4273,])
output2 = relay.Tuple([uop_4269,call_4274,])
func_4280 = relay.Function([var_4268,], output)
mod['func_4280'] = func_4280
mod = relay.transform.InferType()(mod)
var_4281 = relay.var("var_4281", dtype = "float32", shape = (4, 7, 2))#candidate|4281|(4, 7, 2)|var|float32
output = func_4280(var_4281)
func_4282 = relay.Function([var_4281], output)
mutated_mod['func_4282'] = func_4282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1244_call = mod.get_global_var('func_1244')
func_1245_call = mutated_mod.get_global_var('func_1245')
call_4421 = relay.TupleGetItem(func_1244_call(), 0)
call_4422 = relay.TupleGetItem(func_1245_call(), 0)
output = call_4421
output2 = call_4422
func_4457 = relay.Function([], output)
mod['func_4457'] = func_4457
mod = relay.transform.InferType()(mod)
mutated_mod['func_4457'] = func_4457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mutated_mod.get_global_var('func_4457')
call_4458 = func_4457_call()
output = call_4458
func_4459 = relay.Function([], output)
mutated_mod['func_4459'] = func_4459
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4496 = relay.var("var_4496", dtype = "int16", shape = ())#candidate|4496|()|var|int16
var_4497 = relay.var("var_4497", dtype = "int16", shape = (14, 2, 11))#candidate|4497|(14, 2, 11)|var|int16
bop_4498 = relay.equal(var_4496.astype('bool'), var_4497.astype('bool')) # shape=(14, 2, 11)
func_4457_call = mod.get_global_var('func_4457')
func_4459_call = mutated_mod.get_global_var('func_4459')
call_4505 = func_4457_call()
call_4506 = func_4457_call()
uop_4510 = relay.atanh(call_4505.astype('float32')) # shape=(8, 7, 3)
uop_4512 = relay.atanh(call_4506.astype('float32')) # shape=(8, 7, 3)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
const_4521 = relay.const([[7.402795],[6.829633],[-3.416642],[-1.959735],[4.606038],[-8.623506],[-2.361194],[1.368145],[3.564584],[-7.150026],[9.169255],[1.665535],[-5.669338],[-5.492549],[-5.273547],[6.426353],[5.576154],[1.515786],[-7.561916],[-0.366752],[0.376210],[7.736148],[-7.049254],[-0.587528],[9.459605],[-5.469637],[4.990236],[-5.292781],[-9.744583],[-4.286602],[2.972953],[-7.232758],[-2.022680],[-8.362928],[6.207088],[-8.797664],[-6.071814],[5.698041],[8.599931],[-0.871175],[-5.362411],[4.149045],[-2.025540],[5.094359],[3.025120],[2.034818],[0.071967],[2.533867],[4.827526],[-2.251009],[-0.460298],[4.345319],[-8.406929],[4.783524],[-9.845734],[8.667884],[8.072839],[-2.831455],[-6.220729],[-8.705712],[-6.785849],[-8.283714],[-7.554570],[9.866568],[-5.777617],[-0.914394],[9.156682],[5.252485],[-9.146841],[9.134185],[-7.375088],[9.767263],[2.420952],[7.824240],[7.758511],[8.785288],[8.682175],[8.652844],[2.249887],[7.631966],[9.155737],[0.552189],[9.156459],[-7.635800],[2.246829],[-2.264410],[-0.883306],[2.094932],[-5.643747],[4.183393],[5.924407],[5.024374],[9.043360],[-0.647878],[7.690760],[-6.424930],[9.067828],[6.050963],[-9.593163],[5.768487],[5.255640],[3.131567],[6.503343],[-0.869766],[7.309227],[-7.204620],[-3.374588],[7.317980],[-9.071611],[9.413132],[7.417338],[-5.161762],[2.465735],[3.792586],[-4.426797],[0.440973],[-1.535286],[8.902791],[-8.697732],[5.154330],[-2.208021],[-8.281308],[5.738985],[-1.272192],[2.631948],[-3.468189],[7.436978],[6.092635],[-4.359913],[-1.886644],[0.733752],[9.909221],[-8.769210],[-6.517451],[-0.082089],[-6.666854],[9.577330],[6.327394],[-3.262675],[-1.483041],[0.115193],[-9.650263],[-1.688533],[6.778665],[-9.069263],[2.830401],[-8.318285],[2.451458],[6.791184],[4.266140],[-7.071445],[-3.602629],[-9.879985],[-8.716793],[5.472441],[-3.109966],[3.993849],[8.549549],[-3.249785],[5.211561],[-4.890473],[3.527040],[0.011091],[1.816847],[-3.354108],[-8.752675],[-3.086478],[-9.434183],[-2.985296],[1.806694],[8.448884],[6.478361],[-0.797901],[-9.781987],[3.606332],[9.225640],[-3.155975],[-5.352083],[-7.736521],[1.742488],[-7.015014],[6.228154],[-7.304533],[7.155605],[-1.429767],[1.764642],[-3.777607],[8.131850],[6.487689],[-6.313455],[4.254044],[8.002761],[-6.260358],[8.912618],[9.233618],[9.529160],[-4.547196],[7.315437],[-4.512095],[8.126130],[8.664892],[-1.124288],[6.320496],[9.211947],[-9.222323],[-8.735195],[0.913309],[4.641683],[8.254074],[-5.128905],[9.622392],[4.876017],[-4.425085],[7.601904],[9.639274],[-2.926648],[8.399933],[0.912996],[-8.794839],[9.866697],[-6.615992],[-9.011413],[4.039509],[4.008652],[-3.245168],[-6.457830],[7.950343],[1.099203],[-5.138294],[-8.558763],[4.807609],[-1.325762],[7.818965],[-3.952269],[-1.637886],[-4.688571],[5.476209],[2.662284],[9.698997],[5.631361],[-0.646216],[2.108796],[8.746301],[-9.385230],[4.693834],[-8.792848],[9.166874],[1.538529],[-7.539939],[-1.275345],[-3.585381],[7.438506],[1.254005],[-4.569009],[1.637071],[-2.282668],[3.285902],[9.003102],[-4.610822],[-7.002519],[-3.088096],[-2.545162],[-0.158238],[-7.401438],[6.817386],[6.398997],[-1.946716],[9.114935],[9.568237],[-8.245220],[-5.594781],[8.721464],[-3.956966],[-7.536257],[-2.007398],[2.922449],[1.429039],[-8.217958],[2.656292],[-3.940555],[9.811476],[-3.258498],[-7.379161],[7.675482],[-5.816512],[-3.846558],[-6.333739],[-7.662243],[-6.575206],[3.839853],[-2.276212],[1.332627],[-0.441787],[3.417156],[9.444743],[4.075565],[1.074607],[-4.389908],[6.844445],[-7.527332],[3.826239],[-0.371656],[-0.890097],[-3.142740],[-2.934644],[7.162406],[-3.276692],[-4.473919],[-0.076438],[2.506322],[-6.617287],[-5.729130],[-1.056157],[4.599229],[-7.760966],[1.160652],[0.505368],[7.946744],[0.869077],[-8.244531],[4.545137],[-3.433277],[7.998672],[-9.752379],[-4.866058],[1.151320],[-7.063807],[-8.416147],[-7.634256],[1.474152],[9.195393],[-1.509654],[-7.104606],[-9.710037],[7.691605],[2.937220],[-0.783453],[5.387026],[6.051813],[3.988399],[2.341021],[-6.439454],[-7.684581],[-6.830371],[-0.469239],[5.812448],[8.634578],[-4.432352],[5.815309],[1.321185],[-3.760505],[1.489975],[-6.406189],[-2.919864],[5.733297],[5.084724],[-7.539517],[-0.169507],[-2.674725],[4.522005],[-7.038089],[0.018407],[-3.441994],[-8.662890],[-4.324240],[-8.170194],[-0.163556],[-6.061440],[-6.076700],[-8.683627],[-3.340328],[-1.116156],[6.176890],[-5.492933],[-9.362209],[7.510641],[-4.269874],[-4.961914],[-7.869210],[7.830303],[-4.038619],[1.827638],[9.792259],[8.503476],[-0.380809],[5.440379],[7.653898],[0.045414],[1.612822],[-8.293571],[0.670131],[-9.944432],[-9.277995],[-2.047285],[0.372944],[-7.728925],[-3.613859],[8.909350],[7.075483],[5.010162],[-4.790785],[-8.402062],[6.104371],[0.779633],[6.384976],[-2.269512],[7.549185],[7.068490],[4.240407],[-7.278281],[1.092388],[-5.777915],[9.669083],[3.199866],[-3.188205],[-1.029368],[-9.008764],[-4.969882],[4.430889],[-1.362042],[7.941239],[2.720092],[7.992129],[6.977188],[2.820921],[-7.973957],[-1.516134],[-1.962694],[-4.816901],[-3.052004],[-5.110953],[9.783612],[8.045514],[-3.587302],[0.288676],[-8.258748],[5.424747],[3.475008],[-4.185735],[1.395916],[7.646729],[-7.434467],[-7.605855],[8.551805],[-0.237230],[8.609373],[-9.905894],[9.797458],[-0.075452],[-0.364972],[-4.854488],[6.557392],[2.340505],[2.334937],[0.544650],[5.176977],[-4.253885],[-5.194878],[-2.526708],[9.470669],[5.586196],[0.770409],[8.387085],[3.979477],[6.754424],[-3.163600],[-5.194865],[0.424037],[-7.506653],[0.378631],[-9.823488],[-1.202830],[-0.228246],[1.445427],[-9.847574],[-3.220623],[-5.405785],[-3.873649],[-9.709095],[4.337536],[7.237380],[-1.904545],[1.694249],[8.847756],[-3.155948],[7.100906],[3.096448],[8.250677],[-8.058612],[-8.346757],[5.223108],[-5.910440],[3.264295],[7.050185],[3.240413],[7.665525],[-8.276701],[-7.424515],[3.304876],[-3.281729],[7.302177],[-1.437019],[1.458584],[-3.833159],[4.274942],[5.918746],[7.870837],[-4.845645],[-0.849182],[2.994429],[-1.902815],[-2.289403],[-7.013110],[4.020511],[2.423825],[9.282115],[2.904580],[7.084060],[7.686815],[8.117765]], dtype = "float32")#candidate|4521|(520, 1)|const|float32
call_4520 = func_1690_call(relay.reshape(const_4521.astype('float32'), [10, 4, 13]))
call_4522 = func_1690_call(relay.reshape(const_4521.astype('float32'), [10, 4, 13]))
output = relay.Tuple([bop_4498,uop_4510,call_4520,const_4521,])
output2 = relay.Tuple([bop_4498,uop_4512,call_4522,const_4521,])
func_4523 = relay.Function([var_4496,var_4497,], output)
mod['func_4523'] = func_4523
mod = relay.transform.InferType()(mod)
mutated_mod['func_4523'] = func_4523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4523_call = mutated_mod.get_global_var('func_4523')
var_4525 = relay.var("var_4525", dtype = "int16", shape = ())#candidate|4525|()|var|int16
var_4526 = relay.var("var_4526", dtype = "int16", shape = (14, 2, 11))#candidate|4526|(14, 2, 11)|var|int16
call_4524 = func_4523_call(var_4525,var_4526,)
output = call_4524
func_4527 = relay.Function([var_4525,var_4526,], output)
mutated_mod['func_4527'] = func_4527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_505_call = mod.get_global_var('func_505')
func_507_call = mutated_mod.get_global_var('func_507')
call_4568 = relay.TupleGetItem(func_505_call(), 0)
call_4569 = relay.TupleGetItem(func_507_call(), 0)
output = relay.Tuple([call_4568,])
output2 = relay.Tuple([call_4569,])
func_4570 = relay.Function([], output)
mod['func_4570'] = func_4570
mod = relay.transform.InferType()(mod)
output = func_4570()
func_4571 = relay.Function([], output)
mutated_mod['func_4571'] = func_4571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4459_call = mutated_mod.get_global_var('func_4459')
call_4575 = func_4457_call()
call_4576 = func_4457_call()
output = call_4575
output2 = call_4576
func_4579 = relay.Function([], output)
mod['func_4579'] = func_4579
mod = relay.transform.InferType()(mod)
output = func_4579()
func_4580 = relay.Function([], output)
mutated_mod['func_4580'] = func_4580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1428_call = mod.get_global_var('func_1428')
func_1429_call = mutated_mod.get_global_var('func_1429')
call_4587 = relay.TupleGetItem(func_1428_call(), 0)
call_4588 = relay.TupleGetItem(func_1429_call(), 0)
func_2441_call = mod.get_global_var('func_2441')
func_2443_call = mutated_mod.get_global_var('func_2443')
call_4589 = func_2441_call()
call_4590 = func_2441_call()
output = relay.Tuple([call_4587,call_4589,])
output2 = relay.Tuple([call_4588,call_4590,])
func_4611 = relay.Function([], output)
mod['func_4611'] = func_4611
mod = relay.transform.InferType()(mod)
output = func_4611()
func_4612 = relay.Function([], output)
mutated_mod['func_4612'] = func_4612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_869_call = mod.get_global_var('func_869')
func_871_call = mutated_mod.get_global_var('func_871')
call_4619 = relay.TupleGetItem(func_869_call(), 1)
call_4620 = relay.TupleGetItem(func_871_call(), 1)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_4623 = relay.TupleGetItem(func_2385_call(), 1)
call_4624 = relay.TupleGetItem(func_2387_call(), 1)
output = relay.Tuple([call_4619,call_4623,])
output2 = relay.Tuple([call_4620,call_4624,])
func_4628 = relay.Function([], output)
mod['func_4628'] = func_4628
mod = relay.transform.InferType()(mod)
mutated_mod['func_4628'] = func_4628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mutated_mod.get_global_var('func_4628')
call_4629 = func_4628_call()
output = call_4629
func_4630 = relay.Function([], output)
mutated_mod['func_4630'] = func_4630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2631_call = mod.get_global_var('func_2631')
func_2633_call = mutated_mod.get_global_var('func_2633')
call_4644 = relay.TupleGetItem(func_2631_call(), 0)
call_4645 = relay.TupleGetItem(func_2633_call(), 0)
output = call_4644
output2 = call_4645
func_4655 = relay.Function([], output)
mod['func_4655'] = func_4655
mod = relay.transform.InferType()(mod)
output = func_4655()
func_4656 = relay.Function([], output)
mutated_mod['func_4656'] = func_4656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4672 = relay.var("var_4672", dtype = "int8", shape = (2, 11, 9))#candidate|4672|(2, 11, 9)|var|int8
var_4673 = relay.var("var_4673", dtype = "int8", shape = (2, 11, 9))#candidate|4673|(2, 11, 9)|var|int8
bop_4674 = relay.equal(var_4672.astype('bool'), relay.reshape(var_4673.astype('bool'), relay.shape_of(var_4672))) # shape=(2, 11, 9)
output = bop_4674
output2 = bop_4674
func_4698 = relay.Function([var_4672,var_4673,], output)
mod['func_4698'] = func_4698
mod = relay.transform.InferType()(mod)
mutated_mod['func_4698'] = func_4698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4698_call = mutated_mod.get_global_var('func_4698')
var_4700 = relay.var("var_4700", dtype = "int8", shape = (2, 11, 9))#candidate|4700|(2, 11, 9)|var|int8
var_4701 = relay.var("var_4701", dtype = "int8", shape = (2, 11, 9))#candidate|4701|(2, 11, 9)|var|int8
call_4699 = func_4698_call(var_4700,var_4701,)
output = call_4699
func_4702 = relay.Function([var_4700,var_4701,], output)
mutated_mod['func_4702'] = func_4702
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4719 = relay.const([[[-9.878986,-4.140355,1.573418,-3.086148,-8.200124,-5.767699,-5.205543,5.570778,3.742352,1.094242,2.543567,5.007974,-9.754304,7.881941,-5.403418,-2.772418],[3.710046,3.731424,8.072760,3.535595,9.542647,0.175459,-5.819841,5.714976,3.160756,1.981932,-2.066493,-2.941755,-4.126776,8.818247,-6.624669,6.371933],[-0.324374,-3.801287,-4.911658,-1.138442,-2.754348,0.978882,-7.841344,-4.442127,0.854344,1.129564,-2.931761,-3.424992,2.513256,5.530595,4.660803,9.938990],[-3.444961,-5.265302,-0.018166,-2.311540,-4.392021,8.600298,-7.877259,-4.210669,-7.737757,-4.069368,4.264013,8.209887,-0.341947,1.995312,3.557090,-6.258417],[-6.543134,-8.347723,5.463150,5.738197,6.840002,-8.482108,6.619163,4.307275,-5.598866,-0.398301,4.089416,7.846373,3.540147,5.930195,8.595231,-1.008351]],[[-9.701994,-9.615776,3.597169,2.057862,8.454311,-1.606315,6.142521,-4.185961,1.469471,4.942765,-9.211277,4.127886,1.194901,-1.895565,-1.326444,8.492694],[6.489985,-9.496515,1.340811,5.628317,9.623464,8.102786,-2.012266,5.226045,7.042254,-4.248512,1.357279,3.916798,-7.394847,6.547413,-8.855725,-7.303521],[8.334468,-6.436221,-2.638517,9.196252,1.960267,-2.765934,-7.893501,-0.374377,0.294132,7.481374,-9.139401,8.093813,-5.928156,8.259870,5.426932,-5.174171],[-0.826702,-2.829049,3.958854,-9.028463,-4.976374,-8.688489,-4.228837,-8.817528,4.422014,-1.508347,-1.591176,-0.643459,2.016918,8.377442,9.352253,4.073160],[-8.001859,0.551542,3.290511,4.522933,-7.242775,-8.193836,-7.180470,-3.270646,-8.673052,6.090632,6.059711,1.075728,0.757305,5.848530,-9.261049,-7.253753]],[[-8.059472,-8.401270,2.280939,-4.112553,0.526718,4.905824,5.125874,2.227955,-0.826679,3.538195,6.637812,-9.089257,5.456667,4.408278,-1.923139,3.863057],[1.857061,-8.073980,6.448837,4.767150,6.464606,-0.238949,-2.253021,-5.744706,-5.902811,-9.615484,-8.631266,-8.666235,4.652913,-0.192211,5.537260,-2.616587],[3.341452,5.719339,9.297339,-9.829008,9.966388,-6.635650,-0.636007,9.373657,-5.417089,-7.089213,-1.558482,-9.981208,8.426500,-4.765983,-2.970827,1.013278],[3.541619,-9.486134,0.532684,-3.014881,5.980199,4.939603,6.226369,-9.282002,-6.993721,8.322832,5.955795,-5.642099,-5.674699,9.458806,-2.399680,-4.135820],[-4.458915,-0.023151,9.597866,-2.060286,7.878193,9.744261,-4.844066,-1.736097,-0.566424,-2.289171,-9.343311,-5.376303,0.875618,0.297426,7.679831,5.448591]],[[6.228550,6.901313,-6.417047,0.887808,9.023066,7.416772,1.039362,0.111987,0.080362,4.514588,-2.033361,-9.376402,-6.308442,8.135552,4.491095,5.398623],[0.983399,-0.848658,-2.615855,3.801959,-2.663146,-8.340997,9.431647,7.020431,8.968481,-1.294571,7.122365,7.196406,-8.874609,1.493697,9.383268,-6.787201],[1.983219,1.899299,7.836333,-6.350972,4.801880,7.237235,-0.167194,8.823716,1.378161,8.635647,-1.524986,-8.285549,-4.628469,-5.725860,-9.109848,-3.443110],[2.511511,-4.279916,-8.330426,-6.715414,5.558841,-6.456547,9.546146,8.521504,8.908776,1.580323,5.439715,1.484669,3.766715,3.026627,-6.158735,1.350944],[7.253867,-8.288104,-3.046706,8.063537,-9.686449,8.746728,4.420279,5.400606,-8.065067,-8.862457,-0.703423,3.741237,-6.217898,-4.004583,-8.161880,-2.757850]],[[7.371628,6.168694,-3.281640,5.405802,0.307065,-8.852535,6.986782,7.105905,-2.845074,7.503519,9.453462,-7.066400,9.910793,7.059603,-0.414697,-7.710995],[-9.877935,-7.429291,-7.825633,-5.931369,-7.652202,5.117812,-3.345586,1.403890,-2.930946,7.140808,0.662182,1.786523,-4.927845,-3.258140,3.589237,-9.761457],[6.890381,-1.421085,-3.033191,6.841413,6.041407,-6.508398,8.360998,-6.755467,-5.091840,-0.612177,7.116286,8.950705,-9.389037,-2.041541,-3.880467,0.034655],[3.469715,6.134285,-8.842115,8.349326,5.627390,7.721638,9.774480,6.790159,-1.993573,-4.678010,5.563418,9.759286,6.606370,1.359412,8.099066,1.760288],[-6.494728,-6.800179,9.334542,-7.274679,-8.315206,-2.292484,1.220850,3.458558,5.967752,7.231330,9.160652,-6.469453,0.222720,-6.724157,-3.365629,1.440133]],[[5.343549,-9.936036,4.062577,8.305266,-5.152336,-1.880630,8.719302,1.107752,6.688975,-3.554532,-0.165025,0.995683,-9.965424,-1.365762,-9.362883,-9.830596],[3.951815,-9.860154,2.023231,-8.580144,4.971618,-8.465781,7.097576,5.274545,-9.253563,7.698711,-5.936944,-2.065248,9.221729,-8.316286,2.932859,2.074459],[4.264306,3.915208,0.509207,-7.958387,-9.001779,-5.572737,5.145096,-6.342169,0.303366,-6.532720,8.419611,-8.446249,4.019224,-6.945218,6.802040,5.078240],[1.222429,-6.475847,7.769852,-8.099282,2.853510,4.230422,-4.496547,-0.740532,4.120460,-1.430906,-5.579051,3.129609,8.321507,-4.340259,2.550211,0.806777],[-8.438494,-4.082984,-2.100457,-2.135355,5.982729,-6.213799,8.205824,2.564049,1.754826,3.378945,-3.188505,5.758278,-3.775341,1.340031,-6.520884,4.796942]],[[-3.622610,-8.269851,-5.700734,-9.954246,-3.254394,3.501947,3.885888,-3.056691,-7.301729,-6.758255,1.641885,-8.957023,1.135497,2.668992,-6.565159,2.500251],[-9.401215,-5.467222,-6.253702,-2.852039,3.013547,-7.163206,-7.856961,-7.247502,0.957192,-1.361845,-0.168540,-0.223450,-3.859411,0.009387,-9.434800,3.462480],[-5.968585,6.214994,-0.974959,1.213568,-3.054692,-4.539330,7.705848,1.438973,-1.497339,5.966301,8.560683,-0.405158,1.555487,-6.992991,-5.529178,0.798843],[7.072776,9.885501,-7.157706,-1.573948,2.668895,-4.267435,5.853933,4.712144,4.868970,-6.620289,-8.434483,-3.146057,8.203493,-7.303425,-5.230353,-9.924946],[-8.959772,8.973509,6.302654,4.352832,-7.668875,9.578909,-7.611340,7.436816,3.766342,-6.164852,7.686854,3.160461,9.463339,-3.781203,4.809735,-6.841571]],[[3.463816,9.073196,3.704830,3.935608,-2.991060,9.769212,7.367447,-8.241557,-6.516529,-8.531433,4.877379,-5.714546,3.782877,-0.133287,-7.540524,0.128562],[-7.038708,-1.944140,9.236552,5.663612,-7.321018,-3.252298,-0.662786,-3.185250,6.442693,-2.402910,-1.181411,-9.988147,7.932369,7.224846,5.632490,1.791003],[5.485630,5.403958,8.984226,-9.154545,3.706998,2.252377,8.051723,-2.869274,7.551977,0.468826,-9.271991,0.558841,-5.481350,8.378649,0.384888,0.520727],[-3.842610,-1.116043,8.897936,6.628383,6.787252,-4.562993,-1.675864,-6.323583,4.156942,9.012835,3.619123,-7.375225,5.794108,1.375950,-8.481127,6.327102],[9.178249,4.335485,-3.907906,4.340978,7.574182,-7.351800,-6.060406,9.867832,-9.871560,2.919057,-3.200708,0.961729,8.344813,-4.290905,9.892982,-6.796116]],[[1.864120,-2.710439,-9.621339,-3.845260,4.624827,7.144467,6.379147,-1.317433,-3.243556,1.251978,6.643134,-8.624907,5.723459,-2.329491,2.567448,5.436540],[-8.622137,-5.331415,3.086811,1.432538,-6.738132,-7.385664,2.247454,9.558307,3.963470,-1.910087,-1.782967,5.140891,-5.399664,-0.499879,0.739695,-9.766834],[3.054528,-3.946165,6.260060,-4.516986,0.643903,3.128792,7.463074,-6.701494,2.701783,0.663241,1.490643,0.217376,-3.897489,1.323805,5.564180,-0.204156],[8.084358,5.902511,-9.010455,-3.054011,0.297259,-8.480826,-3.272469,8.112037,-3.859493,4.631932,0.907880,9.755030,6.761721,6.155743,-0.905694,7.076954],[7.728291,4.055329,-6.269944,8.943234,5.061075,-8.092151,-2.305337,-7.504621,-9.845189,-2.730277,-7.671388,-4.065899,9.945374,9.624504,5.038321,8.894838]]], dtype = "float32")#candidate|4719|(9, 5, 16)|const|float32
var_4720 = relay.var("var_4720", dtype = "float32", shape = (9, 5, 16))#candidate|4720|(9, 5, 16)|var|float32
bop_4721 = relay.less_equal(const_4719.astype('bool'), relay.reshape(var_4720.astype('bool'), relay.shape_of(const_4719))) # shape=(9, 5, 16)
output = relay.Tuple([bop_4721,])
output2 = relay.Tuple([bop_4721,])
func_4726 = relay.Function([var_4720,], output)
mod['func_4726'] = func_4726
mod = relay.transform.InferType()(mod)
var_4727 = relay.var("var_4727", dtype = "float32", shape = (9, 5, 16))#candidate|4727|(9, 5, 16)|var|float32
output = func_4726(var_4727)
func_4728 = relay.Function([var_4727], output)
mutated_mod['func_4728'] = func_4728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_4745 = relay.TupleGetItem(func_2513_call(), 1)
call_4746 = relay.TupleGetItem(func_2515_call(), 1)
func_3131_call = mod.get_global_var('func_3131')
func_3134_call = mutated_mod.get_global_var('func_3134')
const_4759 = relay.const([5.456240,3.509801,0.269036,5.025967,9.598969,-1.806284,4.086207,0.752462,1.767054,0.243915,1.608979,-4.283249,-0.640390,4.200259,9.753793,-1.358673,-4.301819,2.511961,-3.839519,-1.528365,1.746788,4.591061,0.449172,3.375729,8.309740,2.275902,2.814535,5.617251,-7.511748,9.861192,-2.769973,6.589148,8.686125,-8.508771,4.982257,0.246468,-7.332246,8.606630,2.360182,-6.008081,-0.652273,-7.492601,-5.020506,9.555318,-2.653286,-6.672895,-6.139984,6.196805,-2.681689,2.934361,-4.958024,5.707514,3.760744,-7.016323,0.970897,3.118983,-9.370837,7.263011,-8.082742,-9.297065,8.434546,2.050296,-0.911983,8.144238,-6.047882,-1.944261,-4.161959,2.289460,-0.060676,-7.403634,7.663839,1.893298,2.979171,-5.550717,4.347039,-6.493072,7.594981,-2.133962,-0.731163,-6.555276,-0.960800,-7.648270,-5.855790,-1.513681,2.780271,-8.572605,7.185987,1.375259,-8.827210,-4.196676,-7.280244,-2.585497,-4.465819,6.858423,0.770504,6.939014,-0.776361,-0.241157,-6.144229,4.113286,1.191233,-7.545179,-7.654492,-1.315213,6.917469,-3.299094,6.510593,6.705895,-9.857186,1.191524,-5.829228,2.347963,-3.583412,-6.403013,3.445168,-9.065384,5.929010,6.061339,-6.800495,4.890050,-5.813947,5.100164,-3.291796,8.898200,9.646668,-5.357194,4.666768,-7.491912,2.252581,-8.766272,7.006467,-4.176317,5.406881,-1.111327,3.976612,4.677046,7.314213,0.634502,9.406087,-9.584746,3.366425,3.911783,5.371117,-0.453003,-0.050979,3.250865,-4.485220,-3.497929,4.139777,8.914046,-5.279849,-9.612198,-7.189783,-1.539111,-7.211130,-9.185106,5.741313,-0.946939,-0.183283,-3.235268,-8.045695,-0.199147,5.663878,-0.127521,6.338912,2.034861,9.885029,7.806221,4.003065,7.066301,3.694010,-2.597894,2.408481,4.450759,5.412331,-0.220337,1.899888,-1.659173,-1.264016,7.303154,3.108248,4.839171,-0.840804,-2.189190,-1.919761,7.468262,4.502786,0.343078,-1.922616,-8.257963,-0.470265,6.595951,0.402446,-9.467172,5.937277,3.687174,-4.248584,1.779195,-8.535369,-4.725988,4.583720,-2.095242,5.346276,-5.995920,-0.948451,-9.119751,5.481127,-4.075248,4.085081,-2.703713,-1.852843,5.490406,3.780168,4.521117,-2.096843,-5.816690,3.671833,4.220095,-7.387199,-7.564760,-6.166958,5.656159,9.004268,2.918596,-4.594905,1.997852,4.109270,8.314865,9.291712,-2.125619,2.450633,6.255588,8.605484,5.736267,-0.842927,-1.399664,-8.141774,1.305631,3.879773,2.372737,-9.058759,-0.948310,3.549594,-6.910181,-2.136469,8.866808,-9.258075,-4.562116,0.231291,8.213092,-7.922746,-9.022863,-9.576340,-5.739168,-5.788360,6.267778,-9.497937,4.186145,-5.746270,-5.236741,-8.666700,-7.492137,-9.776179,0.021352,-5.057725,-2.863763,-8.532962,-8.508500,-6.216542,1.482775,-9.157486,3.080963,-4.394877,-5.992812,9.009818,-4.974589,-8.943684,-8.032353,0.028419,-2.907025,-2.102966,-1.319290,-7.357608,1.645423,7.873212,3.277631,-6.855479,-1.042323,9.558488,7.727292,6.160281,6.984744,-4.098920,1.364816,2.157257,8.053609,-0.202061,-0.449071,-0.655929,1.966392,-8.422496,2.987276,0.703125,-0.111977,9.989830,1.831636,8.393281,-6.265265,-9.935747,4.782419,-6.820210,-4.533790,0.011850,4.912729,-4.030826,2.589046,0.572157,9.878619,1.010966,-9.015403,5.376253,0.126494,-3.541433,-1.118215,1.860761,-6.910697,7.628742,-7.200407,2.880323,-9.123873,-1.153626,6.472551,9.916662,6.831112,-9.985308,6.425650,8.857463,-0.873758,-9.277725,5.157569,-2.072295,5.610320,-5.139160,-7.288967,3.139989,7.731482,5.740249,-9.327885,-3.143430,2.277326,4.966624,-1.483805,1.639270,-7.921760,-3.097734,-6.937074,3.423338,-7.565575,8.596329,5.515268,4.717402,6.605112,5.946265,7.531732,0.772997,-0.839059,7.340936,4.905701,9.707271,5.361129,7.230640,6.684415,9.184183,-4.902436,-0.744961,-2.419329,8.103005,-8.471363,5.432520,-8.161569,-8.785105,4.075650,4.741565,9.931763,-2.109588,-3.923157,-5.004218,-0.492004,5.508616,-8.986728,-6.798768,-2.219216,-6.738504,2.434296,-5.696214,-5.715171,-7.782671,7.920190,0.572025,3.913292,6.490739,1.015861,5.203189,4.551657,9.396548,-8.891290,-6.578078,5.383130,-1.747337,-9.164049,-4.185903,2.097640,-9.305447,-5.453641,6.654168,0.787367,-9.760988,-0.135264,-0.850686,-6.036413,-3.251662,-6.239420,9.873429,8.408851,-4.486909,2.338636,4.786373,9.503430,8.840159,8.519169,2.343981,9.990239,7.961978,3.080644,8.760046,4.007283,2.687624,4.600165,5.958815,-6.162525,-8.088589,-7.857253,-1.520474,-7.389348,-9.185084,3.843131,-8.858692,2.849148,-6.064702,-3.929847,-8.437380,4.824446,8.556773,9.668354,-6.712743,-9.335652,2.713703,-9.815036,-8.421095,2.497876,-6.459815,7.758550,5.336662,-3.571842,1.398670,0.568013,8.801650,5.936807,6.448428,9.508557,-6.389397,8.172716,5.719192,-6.088144,-6.982599,-3.820554,-5.809137,5.267765,-9.275498,5.141850,-5.554352,2.523544,-5.432053,-5.391103,5.383516,6.612446,3.250423,0.685335,-8.999754,9.974023,9.388417,3.930104,9.987800,2.171266,-6.761619,2.915072,-8.454475,-2.623574,-3.278139,-2.302448,2.794403,3.829773,-3.143675,1.671362,-6.718900,5.498373,-3.418888,0.003691,-9.930464,3.140757,-4.034098,4.803837,1.959952,5.904695,8.126744,-3.145873,2.879885,0.394608,-0.718200,-4.465116,0.933638,4.239981,-4.304937,6.695203,6.390473,2.984772,-0.440207,-5.239483,2.719513,6.252892,-2.306363,0.002095,9.331192,5.363287,0.094753,4.527673,-3.604632,-5.186366,1.704698,7.423477,-9.731760,-3.546005,3.462545,-6.223006,-3.594414,6.664056,0.858151,-9.501591,-3.048489,3.127398,3.508740,-5.361345,5.102930,-5.252609,5.165656,1.070381,2.124112,-9.028284,7.340401,6.022125,-5.203911,-1.337712,4.841848,-2.489472,-3.859305,9.577073,-3.991900,0.577395,-6.432610,5.656618,5.834047,8.590621,-9.702205,-6.204053,-0.826800,-6.125941,-0.480793,4.837342,7.361314,8.986987,7.432262,-4.234271,3.068413,3.644180,0.786732,2.217653,6.127873,1.019444,-3.008660,5.833638,4.621979,6.870505,-7.022313,4.428422,-3.108695,-9.599821,4.169643,-7.604834,-7.556684,-1.201932,-3.375850,4.946221,-5.053818,9.945501,-7.864401,-3.384879,-3.018944,0.635025,-5.089854,8.738286,-0.692414,-7.837101,-0.266500,-2.138232,-3.873909,-4.486049,-3.761479,-7.835780,8.241747,3.553058,9.410024,6.358023,8.922404,-9.267222,-5.709304,-4.320857,7.328322,-7.788044,7.196633,7.620114,-5.557924,-6.072588,7.966271,1.599407,7.621252,-3.981309,-9.105101,-3.749463,-9.247819,9.558506,-5.034025,2.212872,-0.190468,5.456206,-8.867050,9.145028,4.742208,4.329066,2.798302,2.142435,3.864298,3.050379,8.304902,3.475956,-2.921867,-2.989712,5.183504,0.603452,-5.377104,4.586667,2.428475,7.300310,3.104999,8.718463,8.520681,3.954698,-0.391751,4.827811,-3.383663,6.069588,0.031064,-8.712218,-1.961151,1.708324,-8.741569,7.561571,7.150862,-1.763072,-9.775706,5.089141,-9.329850,-7.040413,5.289429,1.058200,3.598952,7.637451,-0.691027,7.213536,0.751558,1.505862,0.591944,3.976813,8.334494,8.879949,6.301377,-5.341087,0.070602,-4.270368,-0.393585,1.828614,-6.884624,-3.173226,-5.098600,8.620503,-9.659306,0.931915,-7.363069,5.221331,8.922448,2.232489,4.017959,-7.128526,-7.896463,-4.728840,-0.495949,-9.967598,-8.280676,-3.730918,-3.226575,-7.614053,-2.860804,0.266111,-0.249301,5.783108,5.333484,-1.767549,-5.454466,-0.165454,5.570949,3.310238,-3.826533,-3.846680,-2.968008,5.398266,3.040438,-9.074335,2.271502,-8.707851,-6.011671,7.161813,-7.968639,-0.128740,2.111059,3.087804,7.199409,-0.800911,0.669083,-7.372988,7.590488,-7.631280,6.217788,2.531011,-9.679481,-9.306665,0.448038,4.069404,7.968344,-7.673793,-4.003217,4.515896,-4.779035,5.211081,9.322548,3.469894,5.162274,5.682962,-5.255743,7.315898,-7.869554,7.029863,-1.950841,7.623663,8.246742,-3.062946,9.946200,9.612279,0.257187,2.216457,8.671152,-4.511619,8.207577,2.611820,-1.656359,-6.191483,1.655501,-3.062814,-7.413474,0.070114,7.346040,7.824042,-1.436566,-4.873389,8.096648,-0.437723,-8.959810,6.216047,-3.669179,-1.272744,-4.825897,0.866377,-0.547517,9.043356,7.082422,-6.665640,-3.774714,0.815509,6.107342,-8.282591,-4.366322,7.708689,7.572726,-1.158800,9.265393,-8.636475,3.368562,7.505497,5.910262,7.891423,-3.199119,3.558584,7.903092,9.455183,-8.937866,-2.453482,-8.910010,-5.986464,-0.783657,9.141035,0.240770,3.824748,2.037050,-2.388306,7.359027,0.283993,-1.992836,-5.005264,1.088792,-0.846376,-9.809114,-7.236378,-3.718480,-3.435524,4.072216,-0.131762,-3.784301,-9.079672,1.986518,-9.370835,-6.441173,-6.703014,3.530836,-9.425817,-2.208742,-7.065772,1.142368,6.327046,4.832380,4.977565,2.992790,3.557548,3.138592,7.183527,3.109134,-0.047957,2.433079,-0.319887,1.810200,0.340367,3.216673,-4.969846,8.044136,-5.264416,-1.495004,8.881389,9.946481,9.817322,-8.093458,1.008308,-5.832059,3.165992,-1.941358,-2.779504,6.714591,6.017063,-4.018999,1.140354,6.385277,-0.382259,7.767267,1.423180,7.456807,-3.528337,2.484256,4.751970,9.104329,1.988290,-6.634379,3.842959,-9.710528,-2.904550,0.227904,-7.420202,4.458091,-9.439961,-9.898308,3.023258,-8.292993,-9.410499,-1.278996,1.730942,-8.697207,2.478728,3.322506,-1.407565,-3.497725,-9.487009,0.813346,-6.245337,3.569358,5.714018,5.962785,7.686173,-7.795715,5.534070,7.909637,-7.947497,-4.902220,-3.760508,4.432887,6.054965,1.158925,8.496949,-7.919274,4.221844,-0.088554,3.020271,-1.910557,9.463162,-1.080882,5.013101,4.305511,-3.247413,9.236608,6.358848,4.463331,-2.019058,-8.521748,8.281084,-0.007602,2.365047,-0.794372,-9.671786,6.782170,1.948981,-8.319315,-5.878023,2.555291,4.873247,9.708338,9.826080,5.148318,-1.816782,7.276423,-9.681400,-5.080025,-3.490210,4.676495,4.897513,-1.336948,-4.491313,4.866224,-3.398898,4.603582,-0.102872,9.947752,-1.504135,9.914920,-5.860891,-5.031380,-6.035240,-0.887355,3.416066,4.770526,5.057958,-4.081457,9.467278,-8.358689,-9.725707,1.062863,-8.239290,-4.755279,-7.828291,9.431400,-8.005648,6.457219,3.071562,4.730938,6.032644,3.726415,-8.970337,4.603996,-5.838995,8.861425,9.407108,5.206668,5.179723,-0.379643,7.157313,8.771793,-3.488804,3.710892,-7.798779,-1.293329,1.804716,-7.709195,1.490131,3.354685,7.436669,-4.443404,-8.756330,5.124731,0.799835,6.803034,5.958844,-2.798951,7.152160,0.352607,-1.180743,-6.706693,-8.749307,7.827353,-7.419483,5.625788,-2.609307,-8.649993,9.454088,-4.655863,-0.811950,3.922052,-0.399028,8.463485,7.945619,-2.922663,-0.201239,-3.648018,3.470568,2.943344,-3.589663,-7.652859,-1.613680,2.588104,-9.315592,6.270210,8.101759,-2.599713,-9.946339,-2.852884,7.516177,-7.496681,3.558392,-1.108941,-7.255105,-4.747506,-2.834228,0.443048,4.707165,-7.656849,0.609315,-9.645980,-2.305426,-6.338372,-8.118248,0.099417,2.542870,-7.878867,-0.752440,-4.893615,-0.370050,6.573945,6.709716], dtype = "float64")#candidate|4759|(1080,)|const|float64
call_4758 = relay.TupleGetItem(func_3131_call(relay.reshape(const_4759.astype('float64'), [12, 6, 15])), 1)
call_4760 = relay.TupleGetItem(func_3134_call(relay.reshape(const_4759.astype('float64'), [12, 6, 15])), 1)
output = relay.Tuple([call_4745,call_4758,const_4759,])
output2 = relay.Tuple([call_4746,call_4760,const_4759,])
func_4761 = relay.Function([], output)
mod['func_4761'] = func_4761
mod = relay.transform.InferType()(mod)
output = func_4761()
func_4762 = relay.Function([], output)
mutated_mod['func_4762'] = func_4762
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4815 = relay.const([[[0.243701,-9.708729,1.232759,1.339014,5.618837,0.564477,2.877325,2.233335,-7.331156,2.445627,8.389988],[-9.966174,-1.049213,-5.352536,-0.342070,3.213276,-4.925366,4.973809,-6.062683,9.928556,2.808983,-7.430378],[3.373041,-6.158303,3.281883,-0.548066,1.758755,1.795878,-1.299863,-3.378561,-3.836065,-7.523372,9.717674],[-4.771983,-5.843278,3.566784,1.222777,-6.504319,6.301759,-9.438234,-5.456075,-3.082790,-5.311057,-8.683282],[0.084046,3.754553,-2.327742,1.426688,6.655196,9.909939,5.829355,7.773080,-3.806620,7.242659,-0.343112],[-8.746218,-5.446812,9.698494,3.153804,6.204698,-2.750284,-2.280513,-9.619073,-8.248292,8.585844,6.441737],[-4.125938,9.289473,2.045536,8.995336,9.739921,-2.899643,-2.538242,-4.438194,9.632735,-1.402910,-3.259954]],[[-7.962854,-3.108346,-7.722071,9.768660,-4.884391,-8.442823,-9.918900,-1.069101,4.083222,-0.785160,0.625194],[7.601290,-6.340528,1.339183,-8.233602,0.566936,-6.774919,9.350369,7.347555,3.170289,4.606592,-4.491720],[9.476671,2.963731,-0.382501,-3.418216,-5.563228,2.011347,2.559434,8.111901,-4.722383,-8.743158,6.145389],[7.605217,-9.538387,-2.963604,-6.213893,-1.206862,-6.295738,-2.107165,8.287338,-2.700667,8.382096,-7.763535],[4.936174,-2.547728,-5.353045,-7.268676,5.779643,-0.692393,-7.131960,0.765385,3.701348,-3.689830,1.907870],[-6.360651,-5.292876,-4.002875,-6.499427,-2.586126,-4.693503,9.480201,1.932093,-0.300268,2.910606,2.515523],[-8.953049,-9.262686,-5.828999,4.408403,-0.925451,-6.454742,-9.517266,-1.216359,0.574141,-5.870940,3.062152]],[[-1.577375,-4.768989,3.126987,4.726510,5.200870,3.974284,-1.935024,7.264152,5.986455,2.433317,-9.831815],[-7.030354,0.658807,5.426702,-2.928084,5.931151,0.591145,8.616891,-4.397608,8.581173,-3.044081,0.633772],[-9.136151,-3.227180,-3.382232,2.201988,-7.382422,1.388702,0.859000,2.616563,-5.078849,-4.697316,-3.277368],[-6.707464,5.943836,3.724543,9.211215,-9.262717,8.477553,7.144983,-4.877947,-0.263826,5.039904,-1.149447],[-7.583633,-3.861678,7.685581,-0.166365,-1.337861,-0.771351,8.842422,-0.694726,-8.103245,-1.342121,9.359689],[-4.370699,5.700795,-2.155302,-2.301400,2.218594,4.541116,6.027742,4.570708,-3.508320,4.597809,3.398868],[-3.955057,0.566689,-3.830143,-0.852847,8.296889,9.704627,5.874947,7.411475,8.981335,-5.827263,-6.317034]]], dtype = "float32")#candidate|4815|(3, 7, 11)|const|float32
var_4816 = relay.var("var_4816", dtype = "float32", shape = (3, 7, 11))#candidate|4816|(3, 7, 11)|var|float32
bop_4817 = relay.floor_divide(const_4815.astype('float32'), relay.reshape(var_4816.astype('float32'), relay.shape_of(const_4815))) # shape=(3, 7, 11)
output = bop_4817
output2 = bop_4817
func_4834 = relay.Function([var_4816,], output)
mod['func_4834'] = func_4834
mod = relay.transform.InferType()(mod)
mutated_mod['func_4834'] = func_4834
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4835 = relay.var("var_4835", dtype = "float32", shape = (3, 7, 11))#candidate|4835|(3, 7, 11)|var|float32
func_4834_call = mutated_mod.get_global_var('func_4834')
call_4836 = func_4834_call(var_4835)
output = call_4836
func_4837 = relay.Function([var_4835], output)
mutated_mod['func_4837'] = func_4837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1504_call = mod.get_global_var('func_1504')
func_1506_call = mutated_mod.get_global_var('func_1506')
call_4886 = relay.TupleGetItem(func_1504_call(), 2)
call_4887 = relay.TupleGetItem(func_1506_call(), 2)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_4904 = func_1620_call()
call_4905 = func_1620_call()
output = relay.Tuple([call_4886,call_4904,])
output2 = relay.Tuple([call_4887,call_4905,])
func_4929 = relay.Function([], output)
mod['func_4929'] = func_4929
mod = relay.transform.InferType()(mod)
output = func_4929()
func_4930 = relay.Function([], output)
mutated_mod['func_4930'] = func_4930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_4958 = relay.TupleGetItem(func_273_call(), 0)
call_4959 = relay.TupleGetItem(func_275_call(), 0)
output = relay.Tuple([call_4958,])
output2 = relay.Tuple([call_4959,])
func_4969 = relay.Function([], output)
mod['func_4969'] = func_4969
mod = relay.transform.InferType()(mod)
output = func_4969()
func_4970 = relay.Function([], output)
mutated_mod['func_4970'] = func_4970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1570_call = mod.get_global_var('func_1570')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_4985 = relay.TupleGetItem(func_1570_call(), 0)
call_4986 = relay.TupleGetItem(func_1571_call(), 0)
func_1394_call = mod.get_global_var('func_1394')
func_1397_call = mutated_mod.get_global_var('func_1397')
const_5009 = relay.const([[-7.964943,-5.486791,-0.998807,0.286713,9.231272,5.745597,9.381678,-3.728154,2.879871,7.452029,-7.783707,-8.771593,1.116673,8.778350,3.913889,3.023663,5.711407,-6.632801,-7.385143,4.770725,-3.535739,-4.926881,-9.735381,-3.018158],[-2.115491,0.168110,-9.277764,-0.622726,5.302934,4.726597,4.181998,4.045111,3.663186,-5.863638,4.683222,4.487056,-9.391435,5.610008,-0.166664,-3.175973,-0.690839,6.643280,4.281413,-7.033742,2.050369,-7.137396,-2.813884,-8.297707],[6.151409,9.586368,-6.924249,-8.209795,8.737226,-7.192199,0.780198,-6.302547,-0.261270,-2.310289,5.285939,8.146651,0.880964,2.762281,0.753836,5.073586,-2.957157,4.486856,1.632953,8.702283,-7.593148,-3.266240,-2.932718,3.171656],[-7.175793,9.738113,-1.517627,-8.459626,-5.940404,9.602805,0.924786,-1.291830,2.639606,7.637906,1.621528,4.317884,-5.105517,8.806684,1.309744,5.539146,-9.115598,3.117841,2.646584,-7.125364,-3.018818,5.726025,-7.456306,6.937890]], dtype = "float32")#candidate|5009|(4, 24)|const|float32
call_5008 = func_1394_call(relay.reshape(const_5009.astype('float32'), [8, 12]))
call_5010 = func_1394_call(relay.reshape(const_5009.astype('float32'), [8, 12]))
output = relay.Tuple([call_4985,call_5008,const_5009,])
output2 = relay.Tuple([call_4986,call_5010,const_5009,])
func_5017 = relay.Function([], output)
mod['func_5017'] = func_5017
mod = relay.transform.InferType()(mod)
mutated_mod['func_5017'] = func_5017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5017_call = mutated_mod.get_global_var('func_5017')
call_5018 = func_5017_call()
output = call_5018
func_5019 = relay.Function([], output)
mutated_mod['func_5019'] = func_5019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_5022 = relay.TupleGetItem(func_329_call(), 0)
call_5023 = relay.TupleGetItem(func_330_call(), 0)
output = relay.Tuple([call_5022,])
output2 = relay.Tuple([call_5023,])
func_5030 = relay.Function([], output)
mod['func_5030'] = func_5030
mod = relay.transform.InferType()(mod)
output = func_5030()
func_5031 = relay.Function([], output)
mutated_mod['func_5031'] = func_5031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2231_call = mod.get_global_var('func_2231')
func_2232_call = mutated_mod.get_global_var('func_2232')
call_5043 = func_2231_call()
call_5044 = func_2231_call()
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_5055 = relay.TupleGetItem(func_776_call(), 0)
call_5056 = relay.TupleGetItem(func_778_call(), 0)
output = relay.Tuple([call_5043,call_5055,])
output2 = relay.Tuple([call_5044,call_5056,])
func_5064 = relay.Function([], output)
mod['func_5064'] = func_5064
mod = relay.transform.InferType()(mod)
output = func_5064()
func_5065 = relay.Function([], output)
mutated_mod['func_5065'] = func_5065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_329_call = mod.get_global_var('func_329')
func_330_call = mutated_mod.get_global_var('func_330')
call_5074 = relay.TupleGetItem(func_329_call(), 0)
call_5075 = relay.TupleGetItem(func_330_call(), 0)
func_2732_call = mod.get_global_var('func_2732')
func_2733_call = mutated_mod.get_global_var('func_2733')
call_5096 = relay.TupleGetItem(func_2732_call(), 0)
call_5097 = relay.TupleGetItem(func_2733_call(), 0)
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_5099 = relay.TupleGetItem(func_377_call(), 2)
call_5100 = relay.TupleGetItem(func_379_call(), 2)
output = relay.Tuple([call_5074,call_5096,call_5099,])
output2 = relay.Tuple([call_5075,call_5097,call_5100,])
func_5109 = relay.Function([], output)
mod['func_5109'] = func_5109
mod = relay.transform.InferType()(mod)
output = func_5109()
func_5110 = relay.Function([], output)
mutated_mod['func_5110'] = func_5110
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5183 = relay.var("var_5183", dtype = "float32", shape = (10, 10, 7))#candidate|5183|(10, 10, 7)|var|float32
uop_5184 = relay.acosh(var_5183.astype('float32')) # shape=(10, 10, 7)
uop_5193 = relay.atan(var_5183.astype('float32')) # shape=(10, 10, 7)
func_3179_call = mod.get_global_var('func_3179')
func_3181_call = mutated_mod.get_global_var('func_3181')
var_5196 = relay.var("var_5196", dtype = "float32", shape = (468,))#candidate|5196|(468,)|var|float32
call_5195 = relay.TupleGetItem(func_3179_call(relay.reshape(var_5196.astype('float32'), [468,])), 1)
call_5197 = relay.TupleGetItem(func_3181_call(relay.reshape(var_5196.astype('float32'), [468,])), 1)
output = relay.Tuple([uop_5184,uop_5193,call_5195,var_5196,])
output2 = relay.Tuple([uop_5184,uop_5193,call_5197,var_5196,])
func_5204 = relay.Function([var_5183,var_5196,], output)
mod['func_5204'] = func_5204
mod = relay.transform.InferType()(mod)
mutated_mod['func_5204'] = func_5204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5204_call = mutated_mod.get_global_var('func_5204')
var_5206 = relay.var("var_5206", dtype = "float32", shape = (10, 10, 7))#candidate|5206|(10, 10, 7)|var|float32
var_5207 = relay.var("var_5207", dtype = "float32", shape = (468,))#candidate|5207|(468,)|var|float32
call_5205 = func_5204_call(var_5206,var_5207,)
output = call_5205
func_5208 = relay.Function([var_5206,var_5207,], output)
mutated_mod['func_5208'] = func_5208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1244_call = mod.get_global_var('func_1244')
func_1245_call = mutated_mod.get_global_var('func_1245')
call_5212 = relay.TupleGetItem(func_1244_call(), 1)
call_5213 = relay.TupleGetItem(func_1245_call(), 1)
func_740_call = mod.get_global_var('func_740')
func_742_call = mutated_mod.get_global_var('func_742')
call_5233 = relay.TupleGetItem(func_740_call(), 0)
call_5234 = relay.TupleGetItem(func_742_call(), 0)
func_995_call = mod.get_global_var('func_995')
func_997_call = mutated_mod.get_global_var('func_997')
call_5245 = relay.TupleGetItem(func_995_call(relay.reshape(call_5233.astype('int32'), [8, 7, 3])), 0)
call_5246 = relay.TupleGetItem(func_997_call(relay.reshape(call_5233.astype('int32'), [8, 7, 3])), 0)
func_4761_call = mod.get_global_var('func_4761')
func_4762_call = mutated_mod.get_global_var('func_4762')
call_5257 = relay.TupleGetItem(func_4761_call(), 0)
call_5258 = relay.TupleGetItem(func_4762_call(), 0)
func_2876_call = mod.get_global_var('func_2876')
func_2877_call = mutated_mod.get_global_var('func_2877')
call_5263 = relay.TupleGetItem(func_2876_call(), 0)
call_5264 = relay.TupleGetItem(func_2877_call(), 0)
output = relay.Tuple([call_5212,call_5233,call_5245,call_5257,call_5263,])
output2 = relay.Tuple([call_5213,call_5234,call_5246,call_5258,call_5264,])
func_5276 = relay.Function([], output)
mod['func_5276'] = func_5276
mod = relay.transform.InferType()(mod)
output = func_5276()
func_5277 = relay.Function([], output)
mutated_mod['func_5277'] = func_5277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2394_call = mod.get_global_var('func_2394')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_5280 = func_2394_call()
call_5281 = func_2394_call()
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_5322 = relay.TupleGetItem(func_2513_call(), 0)
call_5323 = relay.TupleGetItem(func_2515_call(), 0)
func_1329_call = mod.get_global_var('func_1329')
func_1332_call = mutated_mod.get_global_var('func_1332')
var_5332 = relay.var("var_5332", dtype = "uint32", shape = ())#candidate|5332|()|var|uint32
call_5331 = relay.TupleGetItem(func_1329_call(relay.reshape(var_5332.astype('uint32'), [])), 0)
call_5333 = relay.TupleGetItem(func_1332_call(relay.reshape(var_5332.astype('uint32'), [])), 0)
output = relay.Tuple([call_5280,call_5322,call_5331,var_5332,])
output2 = relay.Tuple([call_5281,call_5323,call_5333,var_5332,])
func_5334 = relay.Function([var_5332,], output)
mod['func_5334'] = func_5334
mod = relay.transform.InferType()(mod)
mutated_mod['func_5334'] = func_5334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5335 = relay.var("var_5335", dtype = "uint32", shape = ())#candidate|5335|()|var|uint32
func_5334_call = mutated_mod.get_global_var('func_5334')
call_5336 = func_5334_call(var_5335)
output = call_5336
func_5337 = relay.Function([var_5335], output)
mutated_mod['func_5337'] = func_5337
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5368 = relay.var("var_5368", dtype = "uint8", shape = (10, 6, 6))#candidate|5368|(10, 6, 6)|var|uint8
var_5369 = relay.var("var_5369", dtype = "uint8", shape = (10, 6, 6))#candidate|5369|(10, 6, 6)|var|uint8
bop_5370 = relay.equal(var_5368.astype('bool'), relay.reshape(var_5369.astype('bool'), relay.shape_of(var_5368))) # shape=(10, 6, 6)
uop_5381 = relay.erf(var_5369.astype('float64')) # shape=(10, 6, 6)
uop_5386 = relay.log(var_5369.astype('float32')) # shape=(10, 6, 6)
uop_5388 = relay.sinh(bop_5370.astype('float32')) # shape=(10, 6, 6)
func_869_call = mod.get_global_var('func_869')
func_871_call = mutated_mod.get_global_var('func_871')
call_5391 = relay.TupleGetItem(func_869_call(), 2)
call_5392 = relay.TupleGetItem(func_871_call(), 2)
func_4579_call = mod.get_global_var('func_4579')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_5399 = func_4579_call()
call_5400 = func_4579_call()
func_4655_call = mod.get_global_var('func_4655')
func_4656_call = mutated_mod.get_global_var('func_4656')
call_5402 = func_4655_call()
call_5403 = func_4655_call()
uop_5408 = relay.asinh(uop_5381.astype('float64')) # shape=(10, 6, 6)
func_2999_call = mod.get_global_var('func_2999')
func_3001_call = mutated_mod.get_global_var('func_3001')
const_5414 = relay.const([[0.510570,-6.240294],[5.428308,9.948971],[7.402921,0.268918],[7.389028,-2.173242],[8.283748,-1.502327],[6.393194,4.866812],[-7.382231,2.903019],[-0.074560,-2.307823],[-2.481926,-2.289428],[9.110039,9.320531],[4.895375,-0.078740],[0.689061,-8.024094],[-5.700102,7.650409],[-6.353484,8.441072],[2.129515,3.634357],[3.437374,-2.378712],[-8.930629,2.344936],[-1.282811,3.903997],[2.293060,2.132818],[-6.332937,5.500948],[-6.602119,7.276732],[7.081619,9.479332],[6.837874,0.927730],[0.406182,4.589021],[-9.284700,0.302707],[8.164885,-2.431032],[-6.804967,3.302717],[0.746681,0.977804],[0.750670,-8.027103],[3.850511,-8.716278],[2.403113,-0.410424],[9.274629,-4.065095],[-8.752366,-6.805302],[-2.615274,8.449313],[-0.732761,-5.788496],[8.028248,0.539544],[-1.183055,-8.375744],[-0.266959,-4.648670],[-7.210652,-8.917671],[-1.479639,3.356034],[-3.646156,-7.656756],[8.480896,5.366825],[-5.606849,0.882682],[4.099976,7.926611],[6.641616,8.920759],[-5.281571,9.346883],[-8.891761,-0.585255],[-8.692086,-3.935523],[4.960749,-5.195556],[-4.947454,3.034115],[8.380066,-5.156539],[6.933124,-5.817174],[4.793254,-6.458449],[5.999032,-8.441530],[0.121586,4.287071],[5.157405,-2.502477],[-7.050708,6.162210],[-4.280491,-6.620423],[2.773552,-2.519689],[-1.953219,4.352737],[0.460896,6.283377],[3.633717,-6.365700],[-6.540906,7.078540],[8.130381,-8.236894],[-9.051496,-4.202798],[-5.196122,-2.084650],[-2.456548,9.719775],[2.648931,-0.781565],[-1.171114,1.021716],[-3.491283,1.948918],[5.574070,-5.796562],[-5.876159,2.401784],[-5.161863,-9.530751],[-3.926808,-5.795031],[3.711517,5.244146],[6.354682,5.103285],[4.062204,8.914345],[4.617333,-5.063669],[6.828624,7.189959],[7.917488,-1.446045],[2.979531,0.474095],[3.884187,-6.685288],[6.460368,5.109799],[8.357404,-2.819957],[-5.366396,-6.756553],[-8.235681,-1.978271],[2.271788,-7.347258],[-3.200766,-4.016985],[2.418520,5.740471],[-0.271898,7.196251],[0.062426,-4.525094],[-8.069920,8.962991],[-7.427953,-9.473895],[-7.380186,9.966131],[-0.671942,3.157145],[-6.776212,-0.064420],[7.528436,7.218767],[0.248991,0.176132],[5.178536,-2.826174],[-4.732491,-3.295291],[6.222376,-7.195600],[-7.747621,-1.760479],[3.621700,4.955200],[8.439401,3.008114],[-4.215277,-6.094272],[3.389907,-8.869967],[9.936719,-8.339145],[9.898255,4.317684],[1.237591,-3.171491],[7.527159,2.500353],[-3.244017,-8.213825],[-1.665213,-8.508769],[-1.803808,3.702512],[-0.993283,0.510198],[-8.839592,-1.264334],[-8.089349,-4.495831],[7.185244,9.928875],[6.302557,1.342413],[-1.686465,-2.359084],[1.408533,5.327364],[6.191822,1.087821],[-8.235245,-7.385385],[2.158521,-1.599793],[-5.532885,6.960646],[-8.299800,-0.354871],[8.611185,8.449521],[7.900320,9.322880],[5.985297,7.114629],[8.631675,-1.218950],[4.242325,-7.029167],[3.901563,-6.257184],[5.439543,3.391111],[5.998229,-2.500880],[1.685985,-9.825821],[7.768816,2.035451],[-4.920434,1.940218],[-0.009881,3.680334],[-0.997618,-5.840914],[0.691407,8.740394],[-5.705104,-0.188427],[-7.673244,0.381116],[-9.940014,9.827766],[3.416507,-1.040359],[9.095439,6.286194],[-4.035496,6.350428],[-0.359289,-1.145527],[-0.584304,-2.058560],[5.869727,-5.786057],[2.871444,0.440683],[6.719828,6.859844],[-3.468092,-4.975813],[-8.670144,0.371361],[4.945603,1.620476],[-4.219430,2.897335],[-2.744969,5.173654],[-1.091281,5.984330],[5.903110,4.758044],[8.211943,6.329518],[0.619543,2.014363],[9.525081,-5.681240],[3.260447,-7.822580],[6.617478,5.096239],[-2.012094,3.425107],[-9.234631,-6.123647],[-3.392696,9.973571],[7.739862,0.497270],[-5.449163,-0.608509],[2.657607,-3.946864],[-8.012697,-1.270686],[-5.174060,9.323027],[-9.565315,1.816153],[-6.955034,6.818150],[-2.716350,-2.803865],[9.894358,-6.787653],[3.519488,-0.152391],[4.013849,9.112767],[7.206298,6.368679],[0.036869,-7.093853],[-9.409809,2.050638],[-0.276372,2.877861],[3.334236,-6.242744],[9.573517,-7.264171],[9.328300,0.406178],[-0.400186,-1.632502],[-8.515036,1.757976],[2.267597,1.410381],[-4.788973,-5.650712],[2.677561,2.058873],[6.421850,-6.835729],[-6.351036,8.580551],[7.334342,-5.763661],[-8.024119,2.131816],[-4.955460,-3.689976],[3.432361,7.921527],[-0.844191,-6.912052],[9.291766,-3.907465],[4.793004,5.708324],[-1.787136,0.183967],[2.169656,5.320954],[-8.120774,-0.576986],[8.647146,-3.209982],[7.668050,-2.543938],[6.526616,6.727149],[-8.233304,-6.795231],[-3.938927,9.363812],[-7.868009,-1.994158],[-0.160993,8.183239],[3.032912,-9.803621],[5.291069,5.572748],[-6.409367,-6.068204],[-3.335809,3.256033],[-5.285974,-8.391637],[3.141906,2.358882],[-4.609680,-4.418937],[9.461844,6.054002],[1.150012,8.455261],[9.224619,3.180253],[3.699216,2.025816],[-7.755997,-2.085545],[-1.707546,6.563032],[4.474906,-3.767268],[4.063775,-6.502934],[-6.040156,7.637872],[3.556219,-0.493619],[8.479640,3.557542],[-9.530177,-5.443927],[8.270421,1.511625],[1.071036,6.949293],[5.254093,-6.521566],[-3.071735,8.865751],[-9.375965,0.805150],[4.353813,-0.418223],[3.168677,0.917549],[8.362833,-6.370709],[9.334258,-9.416274],[7.618697,1.683738],[4.345399,9.082358],[-3.038877,5.387514],[8.335852,2.519356],[-0.008992,5.637353],[6.041988,6.077760],[-8.650633,8.345445],[0.332555,-4.654217],[6.436563,7.268684],[7.669513,5.717741],[0.624972,-3.968770],[9.456183,-2.456490],[-7.581599,3.670842],[-6.094738,-7.421340],[0.050830,-0.255681],[3.763969,1.125551],[-2.734602,-8.945124],[8.341932,-2.663678],[-8.643511,7.100238],[-1.488209,9.453244],[9.094942,-0.474724],[-4.513724,-4.558494],[-9.233723,-3.049633],[3.820346,-3.055997],[7.630905,8.361775]], dtype = "float32")#candidate|5414|(260, 2)|const|float32
call_5413 = relay.TupleGetItem(func_2999_call(relay.reshape(const_5414.astype('float32'), [520,])), 3)
call_5415 = relay.TupleGetItem(func_3001_call(relay.reshape(const_5414.astype('float32'), [520,])), 3)
output = relay.Tuple([uop_5386,uop_5388,call_5391,call_5399,call_5402,uop_5408,call_5413,const_5414,])
output2 = relay.Tuple([uop_5386,uop_5388,call_5392,call_5400,call_5403,uop_5408,call_5415,const_5414,])
func_5417 = relay.Function([var_5368,var_5369,], output)
mod['func_5417'] = func_5417
mod = relay.transform.InferType()(mod)
var_5418 = relay.var("var_5418", dtype = "uint8", shape = (10, 6, 6))#candidate|5418|(10, 6, 6)|var|uint8
var_5419 = relay.var("var_5419", dtype = "uint8", shape = (10, 6, 6))#candidate|5419|(10, 6, 6)|var|uint8
output = func_5417(var_5418,var_5419,)
func_5420 = relay.Function([var_5418,var_5419,], output)
mutated_mod['func_5420'] = func_5420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5030_call = mod.get_global_var('func_5030')
func_5031_call = mutated_mod.get_global_var('func_5031')
call_5425 = relay.TupleGetItem(func_5030_call(), 0)
call_5426 = relay.TupleGetItem(func_5031_call(), 0)
output = call_5425
output2 = call_5426
func_5427 = relay.Function([], output)
mod['func_5427'] = func_5427
mod = relay.transform.InferType()(mod)
output = func_5427()
func_5428 = relay.Function([], output)
mutated_mod['func_5428'] = func_5428
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5442 = relay.const([[[10],[-2],[-4],[-5]],[[-9],[10],[10],[-6]]], dtype = "uint8")#candidate|5442|(2, 4, 1)|const|uint8
var_5443 = relay.var("var_5443", dtype = "uint8", shape = (2, 4, 1))#candidate|5443|(2, 4, 1)|var|uint8
bop_5444 = relay.bitwise_xor(const_5442.astype('uint8'), relay.reshape(var_5443.astype('uint8'), relay.shape_of(const_5442))) # shape=(2, 4, 1)
output = bop_5444
output2 = bop_5444
func_5454 = relay.Function([var_5443,], output)
mod['func_5454'] = func_5454
mod = relay.transform.InferType()(mod)
mutated_mod['func_5454'] = func_5454
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5455 = relay.var("var_5455", dtype = "uint8", shape = (2, 4, 1))#candidate|5455|(2, 4, 1)|var|uint8
func_5454_call = mutated_mod.get_global_var('func_5454')
call_5456 = func_5454_call(var_5455)
output = call_5456
func_5457 = relay.Function([var_5455], output)
mutated_mod['func_5457'] = func_5457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_5471 = relay.TupleGetItem(func_776_call(), 0)
call_5472 = relay.TupleGetItem(func_778_call(), 0)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_5483 = func_1620_call()
call_5484 = func_1620_call()
output = relay.Tuple([call_5471,call_5483,])
output2 = relay.Tuple([call_5472,call_5484,])
func_5501 = relay.Function([], output)
mod['func_5501'] = func_5501
mod = relay.transform.InferType()(mod)
output = func_5501()
func_5502 = relay.Function([], output)
mutated_mod['func_5502'] = func_5502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3416_call = mod.get_global_var('func_3416')
func_3418_call = mutated_mod.get_global_var('func_3418')
call_5509 = relay.TupleGetItem(func_3416_call(), 0)
call_5510 = relay.TupleGetItem(func_3418_call(), 0)
func_3259_call = mod.get_global_var('func_3259')
func_3261_call = mutated_mod.get_global_var('func_3261')
call_5528 = func_3259_call()
call_5529 = func_3259_call()
bop_5530 = relay.subtract(call_5528.astype('uint8'), relay.reshape(call_5509.astype('uint8'), relay.shape_of(call_5528))) # shape=(8, 7, 3)
bop_5533 = relay.subtract(call_5529.astype('uint8'), relay.reshape(call_5510.astype('uint8'), relay.shape_of(call_5529))) # shape=(8, 7, 3)
output = bop_5530
output2 = bop_5533
func_5542 = relay.Function([], output)
mod['func_5542'] = func_5542
mod = relay.transform.InferType()(mod)
output = func_5542()
func_5543 = relay.Function([], output)
mutated_mod['func_5543'] = func_5543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5030_call = mod.get_global_var('func_5030')
func_5031_call = mutated_mod.get_global_var('func_5031')
call_5547 = relay.TupleGetItem(func_5030_call(), 0)
call_5548 = relay.TupleGetItem(func_5031_call(), 0)
func_3271_call = mod.get_global_var('func_3271')
func_3273_call = mutated_mod.get_global_var('func_3273')
call_5571 = func_3271_call()
call_5572 = func_3271_call()
output = relay.Tuple([call_5547,call_5571,])
output2 = relay.Tuple([call_5548,call_5572,])
func_5573 = relay.Function([], output)
mod['func_5573'] = func_5573
mod = relay.transform.InferType()(mod)
output = func_5573()
func_5574 = relay.Function([], output)
mutated_mod['func_5574'] = func_5574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4630_call = mutated_mod.get_global_var('func_4630')
call_5578 = relay.TupleGetItem(func_4628_call(), 0)
call_5579 = relay.TupleGetItem(func_4630_call(), 0)
output = call_5578
output2 = call_5579
func_5581 = relay.Function([], output)
mod['func_5581'] = func_5581
mod = relay.transform.InferType()(mod)
mutated_mod['func_5581'] = func_5581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5581_call = mutated_mod.get_global_var('func_5581')
call_5582 = func_5581_call()
output = call_5582
func_5583 = relay.Function([], output)
mutated_mod['func_5583'] = func_5583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3499_call = mod.get_global_var('func_3499')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_5653 = relay.TupleGetItem(func_3499_call(), 0)
call_5654 = relay.TupleGetItem(func_3500_call(), 0)
output = call_5653
output2 = call_5654
func_5657 = relay.Function([], output)
mod['func_5657'] = func_5657
mod = relay.transform.InferType()(mod)
output = func_5657()
func_5658 = relay.Function([], output)
mutated_mod['func_5658'] = func_5658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2876_call = mod.get_global_var('func_2876')
func_2877_call = mutated_mod.get_global_var('func_2877')
call_5662 = relay.TupleGetItem(func_2876_call(), 0)
call_5663 = relay.TupleGetItem(func_2877_call(), 0)
func_5030_call = mod.get_global_var('func_5030')
func_5031_call = mutated_mod.get_global_var('func_5031')
call_5707 = relay.TupleGetItem(func_5030_call(), 0)
call_5708 = relay.TupleGetItem(func_5031_call(), 0)
func_3499_call = mod.get_global_var('func_3499')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_5720 = relay.TupleGetItem(func_3499_call(), 0)
call_5721 = relay.TupleGetItem(func_3500_call(), 0)
func_1394_call = mod.get_global_var('func_1394')
func_1397_call = mutated_mod.get_global_var('func_1397')
var_5725 = relay.var("var_5725", dtype = "float32", shape = (96,))#candidate|5725|(96,)|var|float32
call_5724 = func_1394_call(relay.reshape(var_5725.astype('float32'), [8, 12]))
call_5726 = func_1394_call(relay.reshape(var_5725.astype('float32'), [8, 12]))
output = relay.Tuple([call_5662,call_5707,call_5720,call_5724,var_5725,])
output2 = relay.Tuple([call_5663,call_5708,call_5721,call_5726,var_5725,])
func_5730 = relay.Function([var_5725,], output)
mod['func_5730'] = func_5730
mod = relay.transform.InferType()(mod)
mutated_mod['func_5730'] = func_5730
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5731 = relay.var("var_5731", dtype = "float32", shape = (96,))#candidate|5731|(96,)|var|float32
func_5730_call = mutated_mod.get_global_var('func_5730')
call_5732 = func_5730_call(var_5731)
output = call_5732
func_5733 = relay.Function([var_5731], output)
mutated_mod['func_5733'] = func_5733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3416_call = mod.get_global_var('func_3416')
func_3418_call = mutated_mod.get_global_var('func_3418')
call_5738 = relay.TupleGetItem(func_3416_call(), 0)
call_5739 = relay.TupleGetItem(func_3418_call(), 0)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_5759 = relay.TupleGetItem(func_2385_call(), 0)
call_5760 = relay.TupleGetItem(func_2387_call(), 0)
func_5109_call = mod.get_global_var('func_5109')
func_5110_call = mutated_mod.get_global_var('func_5110')
call_5762 = relay.TupleGetItem(func_5109_call(), 0)
call_5763 = relay.TupleGetItem(func_5110_call(), 0)
output = relay.Tuple([call_5738,call_5759,call_5762,])
output2 = relay.Tuple([call_5739,call_5760,call_5763,])
func_5771 = relay.Function([], output)
mod['func_5771'] = func_5771
mod = relay.transform.InferType()(mod)
mutated_mod['func_5771'] = func_5771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5771_call = mutated_mod.get_global_var('func_5771')
call_5772 = func_5771_call()
output = call_5772
func_5773 = relay.Function([], output)
mutated_mod['func_5773'] = func_5773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2876_call = mod.get_global_var('func_2876')
func_2877_call = mutated_mod.get_global_var('func_2877')
call_5782 = relay.TupleGetItem(func_2876_call(), 0)
call_5783 = relay.TupleGetItem(func_2877_call(), 0)
output = relay.Tuple([call_5782,])
output2 = relay.Tuple([call_5783,])
func_5787 = relay.Function([], output)
mod['func_5787'] = func_5787
mod = relay.transform.InferType()(mod)
output = func_5787()
func_5788 = relay.Function([], output)
mutated_mod['func_5788'] = func_5788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4570_call = mod.get_global_var('func_4570')
func_4571_call = mutated_mod.get_global_var('func_4571')
call_5802 = relay.TupleGetItem(func_4570_call(), 0)
call_5803 = relay.TupleGetItem(func_4571_call(), 0)
func_5109_call = mod.get_global_var('func_5109')
func_5110_call = mutated_mod.get_global_var('func_5110')
call_5819 = relay.TupleGetItem(func_5109_call(), 0)
call_5820 = relay.TupleGetItem(func_5110_call(), 0)
func_2394_call = mod.get_global_var('func_2394')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_5823 = func_2394_call()
call_5824 = func_2394_call()
output = relay.Tuple([call_5802,call_5819,call_5823,])
output2 = relay.Tuple([call_5803,call_5820,call_5824,])
func_5838 = relay.Function([], output)
mod['func_5838'] = func_5838
mod = relay.transform.InferType()(mod)
output = func_5838()
func_5839 = relay.Function([], output)
mutated_mod['func_5839'] = func_5839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5017_call = mod.get_global_var('func_5017')
func_5019_call = mutated_mod.get_global_var('func_5019')
call_5883 = relay.TupleGetItem(func_5017_call(), 1)
call_5884 = relay.TupleGetItem(func_5019_call(), 1)
func_5064_call = mod.get_global_var('func_5064')
func_5065_call = mutated_mod.get_global_var('func_5065')
call_5899 = relay.TupleGetItem(func_5064_call(), 0)
call_5900 = relay.TupleGetItem(func_5065_call(), 0)
func_1781_call = mod.get_global_var('func_1781')
func_1783_call = mutated_mod.get_global_var('func_1783')
call_5911 = func_1781_call()
call_5912 = func_1781_call()
output = relay.Tuple([call_5883,call_5899,call_5911,])
output2 = relay.Tuple([call_5884,call_5900,call_5912,])
func_5914 = relay.Function([], output)
mod['func_5914'] = func_5914
mod = relay.transform.InferType()(mod)
mutated_mod['func_5914'] = func_5914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5914_call = mutated_mod.get_global_var('func_5914')
call_5915 = func_5914_call()
output = call_5915
func_5916 = relay.Function([], output)
mutated_mod['func_5916'] = func_5916
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5949 = relay.var("var_5949", dtype = "int8", shape = (16, 11, 1))#candidate|5949|(16, 11, 1)|var|int8
const_5950 = relay.const([[[1,10],[10,1],[8,4],[1,-2],[-3,8],[-7,3],[-3,5],[-1,1],[10,6],[-7,-7],[8,-4]],[[-1,8],[7,3],[4,1],[6,7],[-3,-1],[-8,-1],[1,-9],[-9,-10],[7,2],[1,9],[1,5]],[[8,-7],[10,3],[3,4],[-2,-5],[-4,-1],[2,-5],[1,2],[-6,1],[9,-6],[-6,-9],[-3,-4]],[[-6,5],[-3,-10],[-2,-2],[1,-6],[1,4],[7,-8],[-8,-1],[2,5],[-4,5],[-9,-4],[10,-7]],[[-8,-9],[-2,8],[2,2],[5,-1],[9,-4],[-6,-10],[-3,-9],[8,5],[9,-4],[8,10],[-10,-10]],[[-8,-3],[-4,-1],[5,9],[-4,3],[2,-10],[6,4],[8,4],[8,4],[-4,6],[1,10],[7,-5]],[[8,4],[8,3],[-10,5],[-2,-5],[-2,10],[-5,4],[2,-3],[5,-3],[-6,7],[3,-5],[8,2]],[[-1,-2],[-7,1],[-9,-9],[2,3],[9,-4],[-4,-6],[-10,1],[-3,10],[9,10],[-8,-7],[7,9]],[[7,-9],[-7,9],[4,8],[8,-4],[2,6],[-9,9],[-7,-4],[2,6],[-5,-4],[-7,-6],[10,-7]],[[-5,7],[6,-3],[10,-2],[-8,-9],[-8,-10],[9,-9],[-6,-1],[1,5],[10,7],[5,-3],[-10,2]],[[-9,-8],[8,-4],[-1,7],[-8,-6],[-6,-6],[2,4],[-1,-4],[2,-1],[-7,-2],[7,3],[-8,7]],[[-7,-4],[-5,1],[4,-9],[-4,10],[-9,1],[-9,2],[-8,6],[-5,2],[10,-7],[8,4],[-5,1]],[[-6,-7],[1,4],[10,8],[2,6],[6,9],[5,1],[-6,-9],[8,10],[2,-8],[5,3],[-7,-5]],[[-4,6],[10,6],[-3,-3],[3,-2],[2,2],[9,-7],[1,2],[-10,7],[-8,3],[-10,5],[9,-6]],[[10,3],[10,-7],[5,-5],[-3,-6],[-4,8],[10,1],[-2,5],[4,4],[-9,-7],[-2,8],[-8,6]],[[10,6],[-7,-7],[8,6],[6,-3],[-5,6],[4,1],[-8,3],[-1,-9],[3,4],[-2,8],[1,-1]]], dtype = "int8")#candidate|5950|(16, 11, 2)|const|int8
bop_5951 = relay.less_equal(var_5949.astype('bool'), const_5950.astype('bool')) # shape=(16, 11, 2)
output = bop_5951
output2 = bop_5951
func_5954 = relay.Function([var_5949,], output)
mod['func_5954'] = func_5954
mod = relay.transform.InferType()(mod)
mutated_mod['func_5954'] = func_5954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5955 = relay.var("var_5955", dtype = "int8", shape = (16, 11, 1))#candidate|5955|(16, 11, 1)|var|int8
func_5954_call = mutated_mod.get_global_var('func_5954')
call_5956 = func_5954_call(var_5955)
output = call_5956
func_5957 = relay.Function([var_5955], output)
mutated_mod['func_5957'] = func_5957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1244_call = mod.get_global_var('func_1244')
func_1245_call = mutated_mod.get_global_var('func_1245')
call_5971 = relay.TupleGetItem(func_1244_call(), 0)
call_5972 = relay.TupleGetItem(func_1245_call(), 0)
output = relay.Tuple([call_5971,])
output2 = relay.Tuple([call_5972,])
func_5990 = relay.Function([], output)
mod['func_5990'] = func_5990
mod = relay.transform.InferType()(mod)
mutated_mod['func_5990'] = func_5990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5990_call = mutated_mod.get_global_var('func_5990')
call_5991 = func_5990_call()
output = call_5991
func_5992 = relay.Function([], output)
mutated_mod['func_5992'] = func_5992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4628_call = mod.get_global_var('func_4628')
func_4630_call = mutated_mod.get_global_var('func_4630')
call_6043 = relay.TupleGetItem(func_4628_call(), 1)
call_6044 = relay.TupleGetItem(func_4630_call(), 1)
func_4698_call = mod.get_global_var('func_4698')
func_4702_call = mutated_mod.get_global_var('func_4702')
var_6048 = relay.var("var_6048", dtype = "int8", shape = (198,))#candidate|6048|(198,)|var|int8
call_6047 = func_4698_call(relay.reshape(var_6048.astype('int8'), [2, 11, 9]), relay.reshape(var_6048.astype('int8'), [2, 11, 9]), )
call_6049 = func_4698_call(relay.reshape(var_6048.astype('int8'), [2, 11, 9]), relay.reshape(var_6048.astype('int8'), [2, 11, 9]), )
func_3323_call = mod.get_global_var('func_3323')
func_3324_call = mutated_mod.get_global_var('func_3324')
call_6059 = relay.TupleGetItem(func_3323_call(), 0)
call_6060 = relay.TupleGetItem(func_3324_call(), 0)
output = relay.Tuple([call_6043,call_6047,var_6048,call_6059,])
output2 = relay.Tuple([call_6044,call_6049,var_6048,call_6060,])
func_6071 = relay.Function([var_6048,], output)
mod['func_6071'] = func_6071
mod = relay.transform.InferType()(mod)
mutated_mod['func_6071'] = func_6071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6072 = relay.var("var_6072", dtype = "int8", shape = (198,))#candidate|6072|(198,)|var|int8
func_6071_call = mutated_mod.get_global_var('func_6071')
call_6073 = func_6071_call(var_6072)
output = call_6073
func_6074 = relay.Function([var_6072], output)
mutated_mod['func_6074'] = func_6074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_6106 = relay.TupleGetItem(func_377_call(), 3)
call_6107 = relay.TupleGetItem(func_379_call(), 3)
output = call_6106
output2 = call_6107
func_6114 = relay.Function([], output)
mod['func_6114'] = func_6114
mod = relay.transform.InferType()(mod)
mutated_mod['func_6114'] = func_6114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6114_call = mutated_mod.get_global_var('func_6114')
call_6115 = func_6114_call()
output = call_6115
func_6116 = relay.Function([], output)
mutated_mod['func_6116'] = func_6116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_6157 = relay.TupleGetItem(func_776_call(), 0)
call_6158 = relay.TupleGetItem(func_778_call(), 0)
func_6114_call = mod.get_global_var('func_6114')
func_6116_call = mutated_mod.get_global_var('func_6116')
call_6165 = func_6114_call()
call_6166 = func_6114_call()
func_4280_call = mod.get_global_var('func_4280')
func_4282_call = mutated_mod.get_global_var('func_4282')
var_6170 = relay.var("var_6170", dtype = "float32", shape = (56,))#candidate|6170|(56,)|var|float32
call_6169 = relay.TupleGetItem(func_4280_call(relay.reshape(var_6170.astype('float32'), [4, 7, 2])), 0)
call_6171 = relay.TupleGetItem(func_4282_call(relay.reshape(var_6170.astype('float32'), [4, 7, 2])), 0)
var_6174 = relay.var("var_6174", dtype = "float32", shape = (4, 7, 2))#candidate|6174|(4, 7, 2)|var|float32
bop_6175 = relay.left_shift(call_6169.astype('uint32'), relay.reshape(var_6174.astype('uint32'), relay.shape_of(call_6169))) # shape=(4, 7, 2)
bop_6178 = relay.left_shift(call_6171.astype('uint32'), relay.reshape(var_6174.astype('uint32'), relay.shape_of(call_6171))) # shape=(4, 7, 2)
output = relay.Tuple([call_6157,call_6165,var_6170,bop_6175,])
output2 = relay.Tuple([call_6158,call_6166,var_6170,bop_6178,])
func_6188 = relay.Function([var_6170,var_6174,], output)
mod['func_6188'] = func_6188
mod = relay.transform.InferType()(mod)
mutated_mod['func_6188'] = func_6188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6188_call = mutated_mod.get_global_var('func_6188')
var_6190 = relay.var("var_6190", dtype = "float32", shape = (56,))#candidate|6190|(56,)|var|float32
var_6191 = relay.var("var_6191", dtype = "float32", shape = (4, 7, 2))#candidate|6191|(4, 7, 2)|var|float32
call_6189 = func_6188_call(var_6190,var_6191,)
output = call_6189
func_6192 = relay.Function([var_6190,var_6191,], output)
mutated_mod['func_6192'] = func_6192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2876_call = mod.get_global_var('func_2876')
func_2877_call = mutated_mod.get_global_var('func_2877')
call_6199 = relay.TupleGetItem(func_2876_call(), 0)
call_6200 = relay.TupleGetItem(func_2877_call(), 0)
func_449_call = mod.get_global_var('func_449')
func_450_call = mutated_mod.get_global_var('func_450')
call_6221 = func_449_call()
call_6222 = func_449_call()
output = relay.Tuple([call_6199,call_6221,])
output2 = relay.Tuple([call_6200,call_6222,])
func_6249 = relay.Function([], output)
mod['func_6249'] = func_6249
mod = relay.transform.InferType()(mod)
mutated_mod['func_6249'] = func_6249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6249_call = mutated_mod.get_global_var('func_6249')
call_6250 = func_6249_call()
output = call_6250
func_6251 = relay.Function([], output)
mutated_mod['func_6251'] = func_6251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5657_call = mod.get_global_var('func_5657')
func_5658_call = mutated_mod.get_global_var('func_5658')
call_6265 = func_5657_call()
call_6266 = func_5657_call()
func_5109_call = mod.get_global_var('func_5109')
func_5110_call = mutated_mod.get_global_var('func_5110')
call_6296 = relay.TupleGetItem(func_5109_call(), 1)
call_6297 = relay.TupleGetItem(func_5110_call(), 1)
output = relay.Tuple([call_6265,call_6296,])
output2 = relay.Tuple([call_6266,call_6297,])
func_6319 = relay.Function([], output)
mod['func_6319'] = func_6319
mod = relay.transform.InferType()(mod)
mutated_mod['func_6319'] = func_6319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mutated_mod.get_global_var('func_6319')
call_6320 = func_6319_call()
output = call_6320
func_6321 = relay.Function([], output)
mutated_mod['func_6321'] = func_6321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3499_call = mod.get_global_var('func_3499')
func_3500_call = mutated_mod.get_global_var('func_3500')
call_6336 = relay.TupleGetItem(func_3499_call(), 0)
call_6337 = relay.TupleGetItem(func_3500_call(), 0)
func_5838_call = mod.get_global_var('func_5838')
func_5839_call = mutated_mod.get_global_var('func_5839')
call_6357 = relay.TupleGetItem(func_5838_call(), 2)
call_6358 = relay.TupleGetItem(func_5839_call(), 2)
output = relay.Tuple([call_6336,call_6357,])
output2 = relay.Tuple([call_6337,call_6358,])
func_6365 = relay.Function([], output)
mod['func_6365'] = func_6365
mod = relay.transform.InferType()(mod)
mutated_mod['func_6365'] = func_6365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6365_call = mutated_mod.get_global_var('func_6365')
call_6366 = func_6365_call()
output = call_6366
func_6367 = relay.Function([], output)
mutated_mod['func_6367'] = func_6367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2911_call = mod.get_global_var('func_2911')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_6449 = relay.TupleGetItem(func_2911_call(), 0)
call_6450 = relay.TupleGetItem(func_2913_call(), 0)
func_3131_call = mod.get_global_var('func_3131')
func_3134_call = mutated_mod.get_global_var('func_3134')
var_6472 = relay.var("var_6472", dtype = "float64", shape = (1080,))#candidate|6472|(1080,)|var|float64
call_6471 = relay.TupleGetItem(func_3131_call(relay.reshape(var_6472.astype('float64'), [12, 6, 15])), 0)
call_6473 = relay.TupleGetItem(func_3134_call(relay.reshape(var_6472.astype('float64'), [12, 6, 15])), 0)
bop_6486 = relay.bitwise_xor(call_6471.astype('int32'), relay.reshape(var_6472.astype('int32'), relay.shape_of(call_6471))) # shape=(12, 6, 15)
bop_6489 = relay.bitwise_xor(call_6473.astype('int32'), relay.reshape(var_6472.astype('int32'), relay.shape_of(call_6473))) # shape=(12, 6, 15)
output = relay.Tuple([call_6449,bop_6486,])
output2 = relay.Tuple([call_6450,bop_6489,])
func_6490 = relay.Function([var_6472,], output)
mod['func_6490'] = func_6490
mod = relay.transform.InferType()(mod)
mutated_mod['func_6490'] = func_6490
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6491 = relay.var("var_6491", dtype = "float64", shape = (1080,))#candidate|6491|(1080,)|var|float64
func_6490_call = mutated_mod.get_global_var('func_6490')
call_6492 = func_6490_call(var_6491)
output = call_6492
func_6493 = relay.Function([var_6491], output)
mutated_mod['func_6493'] = func_6493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_6502 = func_2072_call()
call_6503 = func_2072_call()
func_4628_call = mod.get_global_var('func_4628')
func_4630_call = mutated_mod.get_global_var('func_4630')
call_6510 = relay.TupleGetItem(func_4628_call(), 0)
call_6511 = relay.TupleGetItem(func_4630_call(), 0)
func_5787_call = mod.get_global_var('func_5787')
func_5788_call = mutated_mod.get_global_var('func_5788')
call_6514 = relay.TupleGetItem(func_5787_call(), 0)
call_6515 = relay.TupleGetItem(func_5788_call(), 0)
func_5064_call = mod.get_global_var('func_5064')
func_5065_call = mutated_mod.get_global_var('func_5065')
call_6516 = relay.TupleGetItem(func_5064_call(), 0)
call_6517 = relay.TupleGetItem(func_5065_call(), 0)
output = relay.Tuple([call_6502,call_6510,call_6514,call_6516,])
output2 = relay.Tuple([call_6503,call_6511,call_6515,call_6517,])
func_6527 = relay.Function([], output)
mod['func_6527'] = func_6527
mod = relay.transform.InferType()(mod)
output = func_6527()
func_6528 = relay.Function([], output)
mutated_mod['func_6528'] = func_6528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6545 = relay.var("var_6545", dtype = "int16", shape = (7, 14, 12))#candidate|6545|(7, 14, 12)|var|int16
const_6546 = relay.const([[[5,6,9,9,9,10,-1,-9,5,-6,-6,-2],[5,-1,-8,-10,3,4,-5,-10,10,10,8,-2],[-1,-5,-3,7,4,-8,3,9,4,-9,-6,-5],[10,10,5,10,10,2,-4,-3,5,3,9,-5],[5,6,-5,-10,4,-5,-3,2,2,-9,1,5],[3,-5,9,-7,-7,8,4,9,9,5,-8,-5],[1,9,6,-9,3,3,-5,8,5,-4,-5,7],[6,6,-8,-6,-7,-10,-8,-3,-4,-5,-9,1],[-9,3,1,-8,1,-2,-6,-8,5,5,-9,-6],[-5,2,-4,-7,1,8,9,8,1,9,-10,2],[6,-9,-6,-10,6,4,-6,-6,1,8,2,-10],[-7,2,-7,-3,2,10,8,8,1,-5,-2,-5],[-7,-3,-10,-3,3,6,-2,2,4,-3,-1,8],[4,8,-6,-1,7,-3,-10,-8,4,10,5,-1]],[[2,-1,6,5,-5,-9,8,-4,-5,-6,5,-7],[-9,8,-7,-5,4,3,7,1,-3,-3,-10,9],[-5,-10,10,1,4,-3,8,-3,-6,-2,6,-5],[2,1,-4,-9,7,9,-9,-7,8,6,-10,8],[-5,10,-4,10,4,9,-4,-9,10,-8,-8,1],[-5,-2,6,-2,10,4,-1,-1,-8,5,9,-6],[-1,7,9,5,-7,-2,1,-5,8,-7,6,3],[8,-7,-1,-7,7,-4,-2,-4,-10,-3,10,1],[7,-6,6,8,-9,-1,10,-7,-2,7,9,-4],[-8,9,-4,6,8,6,-3,-6,-1,-5,4,8],[-2,-9,-6,10,-9,2,9,9,-3,-9,-1,-1],[1,3,-9,-1,-8,1,-5,-10,2,-10,-1,8],[5,-2,-2,9,10,-3,5,-9,-4,8,1,-6],[9,4,6,-4,1,7,9,-9,8,-8,-5,7]],[[-7,-1,-3,3,-4,4,3,8,5,7,9,-5],[-9,-3,1,-6,-7,9,3,-5,-3,6,6,7],[-7,-5,2,7,-2,4,2,-2,-6,-2,4,-7],[-4,-2,6,4,-4,2,-9,-5,-1,6,10,4],[-10,-8,-4,1,9,10,1,-9,-3,2,1,-4],[-10,-8,8,-8,-8,3,1,-10,5,4,-4,-4],[-5,10,6,10,4,-4,-10,3,9,8,9,-10],[9,-2,-10,-1,-3,-1,-3,-4,-9,-1,3,6],[9,-1,3,-5,-9,5,-5,4,-7,8,-8,-9],[1,5,-4,-5,7,3,1,-2,7,10,6,-4],[9,-3,4,-3,1,-10,-10,-10,-3,5,-3,6],[6,3,-10,-5,1,-5,9,4,7,-5,-9,4],[-7,9,7,1,-1,-5,3,1,7,1,-5,6],[-6,-1,-7,10,5,6,-5,7,-1,-9,2,8]],[[-6,-5,-1,5,3,6,-2,-8,6,-10,10,8],[-10,8,7,-3,-5,3,1,-5,3,-6,10,3],[7,8,1,-1,-3,2,2,-2,-6,-5,3,1],[3,-3,1,-8,7,6,-4,-8,-3,-8,8,4],[-4,-8,10,5,9,6,-3,-10,10,10,-2,-10],[1,-4,7,2,8,8,-1,1,10,10,2,6],[6,6,4,-7,-6,-3,-10,4,-5,7,-7,6],[6,3,-7,-9,-4,-5,3,-3,-4,3,9,3],[10,-2,10,6,-7,3,-9,1,7,2,-7,-2],[1,-8,-1,-8,2,-9,9,6,6,2,-2,-9],[-6,-3,-7,-7,-8,-1,-5,-1,-9,7,10,6],[3,-1,8,5,10,8,-3,-8,-9,10,-9,10],[5,-8,1,1,9,-8,-10,2,3,9,-6,-4],[9,-10,9,8,5,9,1,9,-9,-8,4,-1]],[[1,-10,1,1,-2,-8,-9,4,-6,2,-10,7],[2,10,-5,-2,3,3,-7,-3,5,9,10,2],[4,-3,-4,6,6,-1,-7,9,-4,3,9,2],[7,-2,5,-5,5,-5,-6,7,7,7,1,-3],[10,-8,-1,-5,-2,-7,8,-5,-10,5,1,10],[-2,-1,4,-9,7,-3,8,9,2,6,-8,4],[3,-3,-3,-2,1,1,-7,-10,-8,5,1,-5],[-9,-5,-3,-6,10,1,-4,2,6,1,-4,8],[-3,9,6,-7,6,-4,10,-5,1,8,7,-3],[1,-6,6,-8,-6,5,10,9,-3,-5,4,5],[-4,-3,3,5,1,-1,-5,7,6,3,1,2],[-4,-9,6,6,-9,2,4,-7,9,3,9,-3],[-10,-8,8,-7,6,-5,-1,2,-9,-3,-2,-1],[2,-4,1,-3,4,4,-3,8,-8,-4,3,3]],[[10,8,-8,-2,-10,1,-4,4,8,-3,10,2],[4,9,10,9,9,4,6,-10,-4,10,5,-7],[-2,6,2,10,-2,3,-4,-3,-2,2,7,-6],[3,9,10,3,-8,3,-4,8,-5,-9,-5,-2],[3,7,-6,-1,9,-8,-7,2,-9,7,-10,-1],[-6,-4,5,10,-9,-8,-9,5,8,-8,6,10],[5,-9,2,1,-10,-9,-8,5,-5,2,1,-2],[3,-3,10,-2,-1,-3,3,-1,7,-10,-10,-2],[-7,8,4,-6,-2,3,4,-8,-10,-8,-2,-6],[2,6,10,-6,4,4,6,4,10,-9,-5,-1],[-9,-8,9,-2,7,-2,5,3,-2,5,8,5],[9,4,2,-8,4,3,-9,4,-2,2,-2,5],[1,-1,1,9,-1,-3,8,-5,-9,-6,1,4],[-4,-1,3,-2,7,-5,1,-8,9,-7,-5,1]],[[-9,4,-7,-5,7,9,3,-6,5,1,-7,10],[2,-5,8,-3,-5,8,5,4,9,-2,5,5],[9,-7,6,-4,-5,-9,7,9,-9,5,-2,8],[2,-6,-9,-6,6,9,-3,2,4,-10,-3,4],[-5,10,7,9,-9,6,-5,-8,-8,-4,-10,8],[8,-6,6,-5,-8,-10,-2,-4,-5,10,-5,-10],[-5,-3,-3,-10,6,1,5,-2,-10,10,1,-4],[-4,-6,-3,1,5,5,-4,6,-9,1,3,-9],[-8,-7,-10,-7,3,5,-2,-4,-10,-2,3,4],[6,-8,-1,-4,-3,-9,-1,-1,-10,2,3,-10],[6,9,1,-1,-1,8,5,10,-4,-1,5,-1],[8,-6,1,8,-7,5,2,-5,-7,4,6,10],[-3,6,4,-3,-3,7,-5,9,2,2,-4,-7],[-1,-2,7,6,4,-7,1,3,1,6,-3,-7]]], dtype = "int16")#candidate|6546|(7, 14, 12)|const|int16
bop_6547 = relay.bitwise_xor(var_6545.astype('int16'), relay.reshape(const_6546.astype('int16'), relay.shape_of(var_6545))) # shape=(7, 14, 12)
bop_6551 = relay.minimum(const_6546.astype('uint16'), relay.reshape(var_6545.astype('uint16'), relay.shape_of(const_6546))) # shape=(7, 14, 12)
bop_6555 = relay.not_equal(bop_6551.astype('bool'), relay.reshape(var_6545.astype('bool'), relay.shape_of(bop_6551))) # shape=(7, 14, 12)
output = relay.Tuple([bop_6547,bop_6555,])
output2 = relay.Tuple([bop_6547,bop_6555,])
func_6563 = relay.Function([var_6545,], output)
mod['func_6563'] = func_6563
mod = relay.transform.InferType()(mod)
var_6564 = relay.var("var_6564", dtype = "int16", shape = (7, 14, 12))#candidate|6564|(7, 14, 12)|var|int16
output = func_6563(var_6564)
func_6565 = relay.Function([var_6564], output)
mutated_mod['func_6565'] = func_6565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6567 = relay.var("var_6567", dtype = "float64", shape = (2, 11, 14))#candidate|6567|(2, 11, 14)|var|float64
uop_6568 = relay.log2(var_6567.astype('float64')) # shape=(2, 11, 14)
uop_6574 = relay.acosh(var_6567.astype('float32')) # shape=(2, 11, 14)
uop_6593 = relay.log10(uop_6568.astype('float64')) # shape=(2, 11, 14)
var_6602 = relay.var("var_6602", dtype = "float32", shape = (2, 11, 14))#candidate|6602|(2, 11, 14)|var|float32
bop_6603 = relay.logical_xor(uop_6574.astype('uint64'), relay.reshape(var_6602.astype('uint64'), relay.shape_of(uop_6574))) # shape=(2, 11, 14)
func_5501_call = mod.get_global_var('func_5501')
func_5502_call = mutated_mod.get_global_var('func_5502')
call_6607 = relay.TupleGetItem(func_5501_call(), 1)
call_6608 = relay.TupleGetItem(func_5502_call(), 1)
func_4129_call = mod.get_global_var('func_4129')
func_4131_call = mutated_mod.get_global_var('func_4131')
call_6609 = relay.TupleGetItem(func_4129_call(), 0)
call_6610 = relay.TupleGetItem(func_4131_call(), 0)
func_5542_call = mod.get_global_var('func_5542')
func_5543_call = mutated_mod.get_global_var('func_5543')
call_6617 = func_5542_call()
call_6618 = func_5542_call()
output = relay.Tuple([uop_6593,bop_6603,call_6607,call_6609,call_6617,])
output2 = relay.Tuple([uop_6593,bop_6603,call_6608,call_6610,call_6618,])
func_6619 = relay.Function([var_6567,var_6602,], output)
mod['func_6619'] = func_6619
mod = relay.transform.InferType()(mod)
mutated_mod['func_6619'] = func_6619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6619_call = mutated_mod.get_global_var('func_6619')
var_6621 = relay.var("var_6621", dtype = "float64", shape = (2, 11, 14))#candidate|6621|(2, 11, 14)|var|float64
var_6622 = relay.var("var_6622", dtype = "float32", shape = (2, 11, 14))#candidate|6622|(2, 11, 14)|var|float32
call_6620 = func_6619_call(var_6621,var_6622,)
output = call_6620
func_6623 = relay.Function([var_6621,var_6622,], output)
mutated_mod['func_6623'] = func_6623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5501_call = mod.get_global_var('func_5501')
func_5502_call = mutated_mod.get_global_var('func_5502')
call_6644 = relay.TupleGetItem(func_5501_call(), 0)
call_6645 = relay.TupleGetItem(func_5502_call(), 0)
func_1080_call = mod.get_global_var('func_1080')
func_1082_call = mutated_mod.get_global_var('func_1082')
call_6656 = relay.TupleGetItem(func_1080_call(relay.reshape(call_6644.astype('int8'), [8, 7, 3])), 0)
call_6657 = relay.TupleGetItem(func_1082_call(relay.reshape(call_6644.astype('int8'), [8, 7, 3])), 0)
func_2999_call = mod.get_global_var('func_2999')
func_3001_call = mutated_mod.get_global_var('func_3001')
const_6667 = relay.const([-5.012322,-6.974327,-2.683783,3.853202,4.155284,5.158049,7.877126,7.839640,8.639004,3.825381,-0.860865,8.337826,-7.811388,-1.425334,6.467685,0.656151,1.460271,8.120686,2.316251,7.682565,3.621572,-9.972951,-8.436574,1.649274,6.003495,4.183136,5.614024,-4.702628,4.269016,3.255426,-7.390160,-8.936509,-3.020617,2.321036,-6.881951,-4.408332,-7.851768,-7.395106,-8.650487,-2.284543,-6.114676,-8.220197,-3.902293,8.727946,4.637067,-7.895538,2.050141,8.799203,-0.242775,-1.347378,-5.896635,-9.466982,7.460233,0.784153,-3.164232,-8.423246,9.749871,-1.171918,7.246089,6.088298,-1.347890,2.989320,2.384309,5.156192,5.593556,-4.068099,-2.202377,-3.538009,-9.652054,-3.738766,7.395148,8.927888,9.427978,-9.251520,-7.898107,4.299993,-9.785117,-6.374324,-0.244993,1.006374,6.413202,4.703715,4.947857,-7.285439,5.564461,-4.557067,2.658066,-5.277463,-3.848633,9.822239,-0.357028,1.280541,7.163294,-2.632805,-1.928875,-9.752350,-2.347585,6.528641,9.984765,6.397686,-5.123743,-3.674811,9.780835,-5.132604,3.611196,-4.842398,2.839947,-6.460599,-3.147344,-3.690775,6.194893,-8.036289,-0.944715,9.378220,4.194646,-3.892450,-0.344263,5.096015,7.920169,3.357700,-0.823735,3.471040,-2.452592,-6.031505,-2.642044,5.756163,3.864012,3.217351,3.851952,-5.782687,5.700694,5.638863,2.326035,-9.293665,-6.335280,9.350695,4.558929,-4.500380,1.095696,-3.182891,0.625188,8.589620,-1.724179,-1.526291,5.781663,-4.070418,-8.574333,-1.131775,8.468921,-9.722381,1.824445,-0.776005,-3.710709,-4.881722,8.051292,-8.469250,-8.063194,-4.528393,-2.525484,-3.376703,4.364268,3.544465,-8.999866,4.824804,-8.662210,-6.590123,8.179824,-4.591583,8.066181,5.565635,-2.315495,-1.876231,9.201512,7.419309,9.183428,4.534195,-6.966255,-2.590134,4.289435,-0.858793,-9.071358,3.500375,6.529065,5.864312,-5.719880,-3.594364,-9.837353,2.880558,1.154004,-7.630634,-4.578129,3.522086,-2.293891,-8.063295,6.852628,0.101026,0.385106,1.542067,-9.791726,0.946985,-1.039952,8.402611,-7.939847,-1.145342,4.324535,3.967441,7.966719,4.433361,-2.602333,2.868149,-0.254220,6.152069,0.027069,6.937682,-8.828861,-9.554559,-9.655679,9.201371,-2.223699,-4.328305,-5.078493,5.344782,-1.347107,8.215402,-6.899820,-2.729228,9.138527,-5.658651,-8.115339,4.555633,4.475760,1.393080,0.987022,-5.030506,3.471759,-6.374480,-3.158575,6.004823,-5.953334,-8.795573,2.121499,9.954712,-8.191656,4.363268,1.960275,6.076276,-7.305450,-4.623610,-7.783886,8.521163,9.230169,7.133401,9.555296,-3.361628,-3.615740,4.793499,8.040661,-0.971712,-0.535652,3.394996,-4.049403,-0.640120,8.440808,3.396992,-8.043567,8.302213,-5.294791,9.860493,8.002100,3.065812,-0.549491,6.622770,2.038666,-0.755833,8.683413,-9.053537,-1.031597,-3.211867,9.298077,6.691736,-6.314692,-3.541032,-4.509201,1.644652,5.975378,8.764989,8.832557,-5.864235,-6.617403,-0.850413,-9.876513,-9.283221,-3.188177,-9.046993,-1.494305,1.742353,2.639821,8.579774,1.532197,9.962558,5.580299,5.582494,-7.773112,6.452266,-1.650735,-8.014918,-5.508964,2.626991,-4.618958,1.830234,-5.872027,6.466216,-0.143668,8.305049,9.020128,-0.823741,2.250861,4.127980,9.959454,-3.256761,3.544406,-2.346608,2.615230,-3.288363,-5.270885,-9.574810,-7.129687,-1.825649,-3.108920,-1.702432,-5.220055,-0.812921,-4.779419,8.776818,5.316743,6.077400,5.349298,-0.665616,-6.060178,-8.663372,-5.897291,1.404956,-6.470176,5.331366,1.854377,8.477616,1.811003,9.868096,2.109573,7.409933,-2.602496,5.654218,7.367293,9.287155,-0.233314,-6.827787,-3.337075,2.985366,1.766154,-8.241133,8.297024,-4.493103,4.323735,-7.974178,6.339938,6.897810,6.151869,8.113651,2.813162,-9.895936,-2.914618,-5.332775,-9.585310,0.923907,0.406026,-7.088922,7.454312,1.935591,-7.242658,-9.759103,7.807387,9.374581,-6.136777,2.427010,4.832209,-3.104022,-8.547882,5.513698,-8.284980,-1.021850,-4.994488,-9.022906,-0.877484,-8.717437,-6.458572,-4.913332,4.022041,-7.809664,-4.817450,2.215583,1.533373,7.223276,-2.195076,-9.312204,2.070734,-5.843447,0.638871,-4.452330,-3.429983,-1.591137,2.840756,5.907403,-7.858384,-7.566127,6.014584,9.528299,8.125649,6.220203,9.867213,9.520464,-4.961727,-4.778205,-6.680814,3.832370,1.613161,6.966667,-5.993377,9.916343,-9.423244,2.565134,3.994576,-3.048561,7.327688,6.960888,0.545293,-3.839662,-5.025951,1.815735,8.722376,-5.267873,-2.213624,4.543215,-6.655934,-3.339417,-8.869641,-1.874415,-1.260409,6.324337,-1.234478,-1.710610,6.589908,-3.458379,1.714328,-6.138346,-1.853610,9.512088,5.354021,-0.210761,-2.811169,-9.499200,-9.051912,-1.832666,-2.247416,6.275950,-6.080255,-7.787517,-5.862167,-1.502204,7.110352,-3.161708,6.877430,-1.391005,-7.446116,-9.866289,8.499219,1.640517,3.492315,-0.777822,9.572712,0.178022,1.042235,6.934398,-1.059735,1.386893,9.073396,2.286471,-3.557817,9.746337,-9.566592,2.269085,-5.921665,-9.588569,-9.640485,6.547231,-4.495239,-0.416802,7.576335,0.824424,4.711178,1.541890,-3.857648,0.495962,-9.591278,4.917934,-2.178280,1.601953,8.914543,-6.087981,-0.653714,-2.373407,-3.535217,1.257697,-4.366970,7.731458,4.114989,-6.215864,-2.315499,-2.128099,-6.958168,1.882721], dtype = "float32")#candidate|6667|(520,)|const|float32
call_6666 = relay.TupleGetItem(func_2999_call(relay.reshape(const_6667.astype('float32'), [520,])), 2)
call_6668 = relay.TupleGetItem(func_3001_call(relay.reshape(const_6667.astype('float32'), [520,])), 2)
func_1080_call = mod.get_global_var('func_1080')
func_1082_call = mutated_mod.get_global_var('func_1082')
call_6677 = relay.TupleGetItem(func_1080_call(relay.reshape(call_6644.astype('int8'), [8, 7, 3])), 3)
call_6678 = relay.TupleGetItem(func_1082_call(relay.reshape(call_6644.astype('int8'), [8, 7, 3])), 3)
func_1987_call = mod.get_global_var('func_1987')
func_1989_call = mutated_mod.get_global_var('func_1989')
call_6689 = relay.TupleGetItem(func_1987_call(), 0)
call_6690 = relay.TupleGetItem(func_1989_call(), 0)
output = relay.Tuple([call_6644,call_6656,call_6666,const_6667,call_6677,call_6689,])
output2 = relay.Tuple([call_6645,call_6657,call_6668,const_6667,call_6678,call_6690,])
func_6692 = relay.Function([], output)
mod['func_6692'] = func_6692
mod = relay.transform.InferType()(mod)
mutated_mod['func_6692'] = func_6692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6692_call = mutated_mod.get_global_var('func_6692')
call_6693 = func_6692_call()
output = call_6693
func_6694 = relay.Function([], output)
mutated_mod['func_6694'] = func_6694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6709 = relay.var("var_6709", dtype = "float32", shape = ())#candidate|6709|()|var|float32
var_6710 = relay.var("var_6710", dtype = "float32", shape = (2, 13, 7))#candidate|6710|(2, 13, 7)|var|float32
bop_6711 = relay.floor_divide(var_6709.astype('float32'), var_6710.astype('float32')) # shape=(2, 13, 7)
uop_6716 = relay.asinh(var_6710.astype('float32')) # shape=(2, 13, 7)
var_6719 = relay.var("var_6719", dtype = "float32", shape = (2, 13, 7))#candidate|6719|(2, 13, 7)|var|float32
bop_6720 = relay.not_equal(uop_6716.astype('bool'), relay.reshape(var_6719.astype('bool'), relay.shape_of(uop_6716))) # shape=(2, 13, 7)
uop_6724 = relay.cos(var_6719.astype('float32')) # shape=(2, 13, 7)
func_6249_call = mod.get_global_var('func_6249')
func_6251_call = mutated_mod.get_global_var('func_6251')
call_6726 = relay.TupleGetItem(func_6249_call(), 1)
call_6727 = relay.TupleGetItem(func_6251_call(), 1)
const_6728 = relay.const([[[-7.074093,5.711468,3.397033,-4.592504,6.598449,-8.275201,-6.696551],[5.965271,-2.410293,6.721784,-2.465362,9.547819,-2.342738,4.521006],[-0.288901,-5.055989,-4.547113,5.227256,1.080056,-8.890453,-7.009579],[-2.467144,1.998538,-9.689210,7.289826,0.607347,8.882029,-7.691770],[2.445128,-6.006796,-8.606962,6.468818,-8.031736,6.157114,-3.910396],[-6.312497,-7.043599,6.419386,-2.046490,-1.522137,9.122614,7.886911],[-5.997031,9.904872,7.670325,8.739381,-8.710435,7.778020,7.769734],[-7.832613,-6.400511,-2.013444,0.617607,-5.974452,7.306461,1.293799],[0.989338,5.196232,1.214848,6.353268,9.420485,-1.849849,2.539846],[-2.934011,-0.355802,6.182589,-4.641970,-0.452292,1.709698,1.352678],[8.708432,-4.435737,-1.248836,-5.829641,-4.026694,-2.222076,-6.462687],[7.272850,-8.393870,-8.083258,-6.723797,-7.609215,4.887061,-5.608136],[5.486748,4.207024,-5.680911,6.011733,2.529434,-3.830657,-4.062697]],[[6.571183,-9.531465,-4.804992,5.876732,1.409071,-3.727840,-0.370904],[-5.396912,2.608960,-4.335439,-3.215512,-4.940515,0.559248,1.479484],[1.763627,8.353039,-2.187883,5.525435,-9.690540,1.530389,-1.285718],[9.973046,5.089357,2.678673,-0.458794,9.841738,-4.318114,-4.998928],[-5.932049,-9.915181,8.233432,-1.590073,1.984032,5.692403,-7.287659],[4.111244,-0.917525,3.723177,1.621917,-3.912604,2.726861,-4.751385],[1.265247,9.496053,3.995318,0.257496,7.924390,-3.136684,3.433877],[2.717194,9.751923,-4.116592,1.496027,3.039743,-9.063139,-4.898553],[-2.769663,-3.277792,-2.605602,6.385365,8.316468,-5.511628,-0.275761],[6.963514,-8.828724,-5.846064,1.037557,-2.906506,-4.740555,0.364716],[2.513681,-7.707190,5.733970,-9.634966,3.436960,1.747767,-0.475869],[9.595534,-0.272330,6.281002,3.459250,-0.674004,-8.960787,-6.575688],[2.648039,-1.710511,1.999995,-3.309718,1.662234,-1.099042,-8.395497]]], dtype = "float32")#candidate|6728|(2, 13, 7)|const|float32
bop_6729 = relay.bitwise_xor(uop_6724.astype('uint16'), relay.reshape(const_6728.astype('uint16'), relay.shape_of(uop_6724))) # shape=(2, 13, 7)
output = relay.Tuple([bop_6711,bop_6720,call_6726,bop_6729,])
output2 = relay.Tuple([bop_6711,bop_6720,call_6727,bop_6729,])
func_6732 = relay.Function([var_6709,var_6710,var_6719,], output)
mod['func_6732'] = func_6732
mod = relay.transform.InferType()(mod)
mutated_mod['func_6732'] = func_6732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6732_call = mutated_mod.get_global_var('func_6732')
var_6734 = relay.var("var_6734", dtype = "float32", shape = ())#candidate|6734|()|var|float32
var_6735 = relay.var("var_6735", dtype = "float32", shape = (2, 13, 7))#candidate|6735|(2, 13, 7)|var|float32
var_6736 = relay.var("var_6736", dtype = "float32", shape = (2, 13, 7))#candidate|6736|(2, 13, 7)|var|float32
call_6733 = func_6732_call(var_6734,var_6735,var_6736,)
output = call_6733
func_6737 = relay.Function([var_6734,var_6735,var_6736,], output)
mutated_mod['func_6737'] = func_6737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5787_call = mod.get_global_var('func_5787')
func_5788_call = mutated_mod.get_global_var('func_5788')
call_6771 = relay.TupleGetItem(func_5787_call(), 0)
call_6772 = relay.TupleGetItem(func_5788_call(), 0)
func_4129_call = mod.get_global_var('func_4129')
func_4131_call = mutated_mod.get_global_var('func_4131')
call_6785 = relay.TupleGetItem(func_4129_call(), 0)
call_6786 = relay.TupleGetItem(func_4131_call(), 0)
output = relay.Tuple([call_6771,call_6785,])
output2 = relay.Tuple([call_6772,call_6786,])
func_6803 = relay.Function([], output)
mod['func_6803'] = func_6803
mod = relay.transform.InferType()(mod)
mutated_mod['func_6803'] = func_6803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6803_call = mutated_mod.get_global_var('func_6803')
call_6804 = func_6803_call()
output = call_6804
func_6805 = relay.Function([], output)
mutated_mod['func_6805'] = func_6805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5990_call = mod.get_global_var('func_5990')
func_5992_call = mutated_mod.get_global_var('func_5992')
call_6839 = relay.TupleGetItem(func_5990_call(), 0)
call_6840 = relay.TupleGetItem(func_5992_call(), 0)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_6867 = relay.TupleGetItem(func_273_call(), 0)
call_6868 = relay.TupleGetItem(func_275_call(), 0)
func_6732_call = mod.get_global_var('func_6732')
func_6737_call = mutated_mod.get_global_var('func_6737')
const_6873 = relay.const(-9.455948, dtype = "float32")#candidate|6873|()|const|float32
var_6874 = relay.var("var_6874", dtype = "float32", shape = (26, 7))#candidate|6874|(26, 7)|var|float32
call_6872 = relay.TupleGetItem(func_6732_call(relay.reshape(const_6873.astype('float32'), []), relay.reshape(var_6874.astype('float32'), [2, 13, 7]), relay.reshape(var_6874.astype('float32'), [2, 13, 7]), ), 0)
call_6875 = relay.TupleGetItem(func_6737_call(relay.reshape(const_6873.astype('float32'), []), relay.reshape(var_6874.astype('float32'), [2, 13, 7]), relay.reshape(var_6874.astype('float32'), [2, 13, 7]), ), 0)
func_6249_call = mod.get_global_var('func_6249')
func_6251_call = mutated_mod.get_global_var('func_6251')
call_6887 = relay.TupleGetItem(func_6249_call(), 1)
call_6888 = relay.TupleGetItem(func_6251_call(), 1)
output = relay.Tuple([call_6839,call_6867,call_6872,const_6873,var_6874,call_6887,])
output2 = relay.Tuple([call_6840,call_6868,call_6875,const_6873,var_6874,call_6888,])
func_6903 = relay.Function([var_6874,], output)
mod['func_6903'] = func_6903
mod = relay.transform.InferType()(mod)
mutated_mod['func_6903'] = func_6903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6904 = relay.var("var_6904", dtype = "float32", shape = (26, 7))#candidate|6904|(26, 7)|var|float32
func_6903_call = mutated_mod.get_global_var('func_6903')
call_6905 = func_6903_call(var_6904)
output = call_6905
func_6906 = relay.Function([var_6904], output)
mutated_mod['func_6906'] = func_6906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2231_call = mod.get_global_var('func_2231')
func_2232_call = mutated_mod.get_global_var('func_2232')
call_6928 = func_2231_call()
call_6929 = func_2231_call()
output = relay.Tuple([call_6928,])
output2 = relay.Tuple([call_6929,])
func_6938 = relay.Function([], output)
mod['func_6938'] = func_6938
mod = relay.transform.InferType()(mod)
mutated_mod['func_6938'] = func_6938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6938_call = mutated_mod.get_global_var('func_6938')
call_6939 = func_6938_call()
output = call_6939
func_6940 = relay.Function([], output)
mutated_mod['func_6940'] = func_6940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5581_call = mod.get_global_var('func_5581')
func_5583_call = mutated_mod.get_global_var('func_5583')
call_6950 = func_5581_call()
call_6951 = func_5581_call()
output = relay.Tuple([call_6950,])
output2 = relay.Tuple([call_6951,])
func_6957 = relay.Function([], output)
mod['func_6957'] = func_6957
mod = relay.transform.InferType()(mod)
mutated_mod['func_6957'] = func_6957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6957_call = mutated_mod.get_global_var('func_6957')
call_6958 = func_6957_call()
output = call_6958
func_6959 = relay.Function([], output)
mutated_mod['func_6959'] = func_6959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mod.get_global_var('func_4611')
func_4612_call = mutated_mod.get_global_var('func_4612')
call_6965 = relay.TupleGetItem(func_4611_call(), 1)
call_6966 = relay.TupleGetItem(func_4612_call(), 1)
func_1189_call = mod.get_global_var('func_1189')
func_1192_call = mutated_mod.get_global_var('func_1192')
var_6985 = relay.var("var_6985", dtype = "uint32", shape = ())#candidate|6985|()|var|uint32
var_6986 = relay.var("var_6986", dtype = "uint32", shape = (360,))#candidate|6986|(360,)|var|uint32
call_6984 = relay.TupleGetItem(func_1189_call(relay.reshape(var_6985.astype('uint32'), []), relay.reshape(var_6986.astype('uint32'), [12, 3, 10]), ), 1)
call_6987 = relay.TupleGetItem(func_1192_call(relay.reshape(var_6985.astype('uint32'), []), relay.reshape(var_6986.astype('uint32'), [12, 3, 10]), ), 1)
func_4698_call = mod.get_global_var('func_4698')
func_4702_call = mutated_mod.get_global_var('func_4702')
const_7018 = relay.const([8,6,8,8,-4,8,-1,-1,-8,-2,-5,-8,4,-5,-5,-4,6,-7,-3,8,-5,3,1,8,3,4,-5,-4,-2,-9,1,2,-3,-2,3,4,-6,5,10,-5,-3,2,3,9,7,4,3,-7,-4,-5,-9,-8,7,-2,-7,2,8,-8,-4,-8,-6,8,8,-8,-6,-3,3,10,3,6,1,-9,-4,9,7,6,10,5,-3,10,7,4,3,9,-8,-9,5,-7,7,6,5,-9,9,-3,-10,-2,6,-8,-2,8,-4,-10,-5,9,-4,7,-6,-4,-4,-9,-10,3,7,-7,-8,10,2,-2,-6,10,-5,-1,7,8,-4,8,-6,-2,-2,-3,-5,-4,-2,5,-7,-1,-6,-3,-2,6,8,10,7,-8,-2,-1,5,-6,-2,-8,-8,1,-3,-8,-7,-9,-10,-10,2,6,-10,-2,10,5,-9,-3,2,-10,2,10,-2,-4,-9,-9,-2,-8,10,9,-6,-4,-5,-1,-4,-4,10,-4,2,-5,2,-3,-7,-7,10,6,10,2,-8,-4], dtype = "int8")#candidate|7018|(198,)|const|int8
call_7017 = func_4698_call(relay.reshape(const_7018.astype('int8'), [2, 11, 9]), relay.reshape(const_7018.astype('int8'), [2, 11, 9]), )
call_7019 = func_4698_call(relay.reshape(const_7018.astype('int8'), [2, 11, 9]), relay.reshape(const_7018.astype('int8'), [2, 11, 9]), )
func_5581_call = mod.get_global_var('func_5581')
func_5583_call = mutated_mod.get_global_var('func_5583')
call_7024 = func_5581_call()
call_7025 = func_5581_call()
output = relay.Tuple([call_6965,call_6984,var_6985,var_6986,call_7017,const_7018,call_7024,])
output2 = relay.Tuple([call_6966,call_6987,var_6985,var_6986,call_7019,const_7018,call_7025,])
func_7038 = relay.Function([var_6985,var_6986,], output)
mod['func_7038'] = func_7038
mod = relay.transform.InferType()(mod)
var_7039 = relay.var("var_7039", dtype = "uint32", shape = ())#candidate|7039|()|var|uint32
var_7040 = relay.var("var_7040", dtype = "uint32", shape = (360,))#candidate|7040|(360,)|var|uint32
output = func_7038(var_7039,var_7040,)
func_7041 = relay.Function([var_7039,var_7040,], output)
mutated_mod['func_7041'] = func_7041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7085 = relay.var("var_7085", dtype = "float32", shape = (11, 12, 16))#candidate|7085|(11, 12, 16)|var|float32
uop_7086 = relay.asinh(var_7085.astype('float32')) # shape=(11, 12, 16)
uop_7093 = relay.erf(uop_7086.astype('float64')) # shape=(11, 12, 16)
uop_7106 = relay.exp(uop_7093.astype('float32')) # shape=(11, 12, 16)
uop_7110 = relay.sinh(uop_7106.astype('float32')) # shape=(11, 12, 16)
bop_7112 = relay.power(uop_7110.astype('float64'), relay.reshape(uop_7093.astype('float64'), relay.shape_of(uop_7110))) # shape=(11, 12, 16)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_7118 = relay.TupleGetItem(func_2220_call(), 0)
call_7119 = relay.TupleGetItem(func_2222_call(), 0)
func_1080_call = mod.get_global_var('func_1080')
func_1082_call = mutated_mod.get_global_var('func_1082')
call_7120 = relay.TupleGetItem(func_1080_call(relay.reshape(call_7118.astype('int8'), [8, 7, 3])), 3)
call_7121 = relay.TupleGetItem(func_1082_call(relay.reshape(call_7118.astype('int8'), [8, 7, 3])), 3)
func_3583_call = mod.get_global_var('func_3583')
func_3584_call = mutated_mod.get_global_var('func_3584')
call_7123 = relay.TupleGetItem(func_3583_call(), 0)
call_7124 = relay.TupleGetItem(func_3584_call(), 0)
bop_7138 = relay.bitwise_xor(uop_7110.astype('uint16'), relay.reshape(uop_7093.astype('uint16'), relay.shape_of(uop_7110))) # shape=(11, 12, 16)
func_3579_call = mod.get_global_var('func_3579')
func_3580_call = mutated_mod.get_global_var('func_3580')
call_7142 = relay.TupleGetItem(func_3579_call(), 0)
call_7143 = relay.TupleGetItem(func_3580_call(), 0)
func_5771_call = mod.get_global_var('func_5771')
func_5773_call = mutated_mod.get_global_var('func_5773')
call_7150 = relay.TupleGetItem(func_5771_call(), 1)
call_7151 = relay.TupleGetItem(func_5773_call(), 1)
bop_7152 = relay.bitwise_or(uop_7106.astype('int32'), relay.reshape(uop_7093.astype('int32'), relay.shape_of(uop_7106))) # shape=(11, 12, 16)
output = relay.Tuple([bop_7112,call_7118,call_7120,call_7123,bop_7138,call_7142,call_7150,bop_7152,])
output2 = relay.Tuple([bop_7112,call_7119,call_7121,call_7124,bop_7138,call_7143,call_7151,bop_7152,])
func_7156 = relay.Function([var_7085,], output)
mod['func_7156'] = func_7156
mod = relay.transform.InferType()(mod)
var_7157 = relay.var("var_7157", dtype = "float32", shape = (11, 12, 16))#candidate|7157|(11, 12, 16)|var|float32
output = func_7156(var_7157)
func_7158 = relay.Function([var_7157], output)
mutated_mod['func_7158'] = func_7158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7200 = relay.var("var_7200", dtype = "float32", shape = (6, 16, 1))#candidate|7200|(6, 16, 1)|var|float32
uop_7201 = relay.erf(var_7200.astype('float32')) # shape=(6, 16, 1)
output = uop_7201
output2 = uop_7201
func_7203 = relay.Function([var_7200,], output)
mod['func_7203'] = func_7203
mod = relay.transform.InferType()(mod)
var_7204 = relay.var("var_7204", dtype = "float32", shape = (6, 16, 1))#candidate|7204|(6, 16, 1)|var|float32
output = func_7203(var_7204)
func_7205 = relay.Function([var_7204], output)
mutated_mod['func_7205'] = func_7205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4929_call = mod.get_global_var('func_4929')
func_4930_call = mutated_mod.get_global_var('func_4930')
call_7239 = relay.TupleGetItem(func_4929_call(), 0)
call_7240 = relay.TupleGetItem(func_4930_call(), 0)
func_5542_call = mod.get_global_var('func_5542')
func_5543_call = mutated_mod.get_global_var('func_5543')
call_7242 = func_5542_call()
call_7243 = func_5542_call()
output = relay.Tuple([call_7239,call_7242,])
output2 = relay.Tuple([call_7240,call_7243,])
func_7245 = relay.Function([], output)
mod['func_7245'] = func_7245
mod = relay.transform.InferType()(mod)
output = func_7245()
func_7246 = relay.Function([], output)
mutated_mod['func_7246'] = func_7246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4969_call = mod.get_global_var('func_4969')
func_4970_call = mutated_mod.get_global_var('func_4970')
call_7300 = relay.TupleGetItem(func_4969_call(), 0)
call_7301 = relay.TupleGetItem(func_4970_call(), 0)
output = call_7300
output2 = call_7301
func_7302 = relay.Function([], output)
mod['func_7302'] = func_7302
mod = relay.transform.InferType()(mod)
output = func_7302()
func_7303 = relay.Function([], output)
mutated_mod['func_7303'] = func_7303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_7311 = relay.TupleGetItem(func_776_call(), 0)
call_7312 = relay.TupleGetItem(func_778_call(), 0)
func_6188_call = mod.get_global_var('func_6188')
func_6192_call = mutated_mod.get_global_var('func_6192')
const_7348 = relay.const([[3.492448,-9.164056,0.267319,7.110571,7.796273,-2.792961,-7.323612,-3.557739,-5.549848,1.641696,4.175675,5.951102,-3.089911,-0.370521,6.286788,-9.330952,-4.295686,-4.399315,3.642371,-5.345138,-2.998541,5.142009,4.807302,6.378406,5.311673,-0.533412,9.526637,-8.786989,8.305309,-6.748000,4.804432,4.058254,9.903557,-4.907028,-8.555492,-4.542334,8.237226,3.819839,3.708278,-7.121126,8.461146,3.921921,-8.519307,-4.214265,-7.527407,0.648868,9.240814,-3.016123,-3.561290,-5.609946,1.863378,0.835304,-6.208096,-4.034197,4.184457,-7.747612]], dtype = "float32")#candidate|7348|(1, 56)|const|float32
call_7347 = relay.TupleGetItem(func_6188_call(relay.reshape(const_7348.astype('float32'), [56,]), relay.reshape(const_7348.astype('float32'), [4, 7, 2]), ), 3)
call_7349 = relay.TupleGetItem(func_6192_call(relay.reshape(const_7348.astype('float32'), [56,]), relay.reshape(const_7348.astype('float32'), [4, 7, 2]), ), 3)
uop_7350 = relay.asin(call_7347.astype('float32')) # shape=(4, 7, 2)
uop_7352 = relay.asin(call_7349.astype('float32')) # shape=(4, 7, 2)
output = relay.Tuple([call_7311,const_7348,uop_7350,])
output2 = relay.Tuple([call_7312,const_7348,uop_7352,])
func_7361 = relay.Function([], output)
mod['func_7361'] = func_7361
mod = relay.transform.InferType()(mod)
output = func_7361()
func_7362 = relay.Function([], output)
mutated_mod['func_7362'] = func_7362
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7370 = relay.const([[[-4,8,-4,-7,-5,-5,3,9,-1,7,-7,-3,-6,-9],[-4,10,6,5,-10,-8,-3,1,4,8,-9,1,-6,6],[-7,10,-6,9,-8,-3,-1,3,-5,9,-4,-5,4,2],[10,3,-7,-1,5,6,-8,-4,-9,2,3,5,10,2],[-6,3,4,-7,1,3,-2,9,-7,9,-10,-2,-4,-10],[-9,-8,9,-4,7,4,-9,-4,-6,-3,6,9,-4,-10],[-9,3,-3,4,-2,4,10,-7,-3,-2,-6,1,6,9],[-2,10,-9,1,6,3,4,7,-3,2,7,-6,8,6],[-9,6,2,-3,9,-3,1,-2,3,-8,-4,-4,-6,-6],[8,-10,5,-8,-2,-9,7,5,-10,-3,-4,1,5,1],[-8,8,6,-2,-6,1,-1,10,-4,8,-9,9,3,-5],[7,-2,4,-8,-9,-3,-1,6,5,-4,8,3,2,-5],[1,-5,-6,1,6,2,2,-4,-10,-8,4,-1,3,-4],[-3,-2,-8,3,4,4,5,-7,1,-3,2,3,-5,-10],[8,3,-2,-8,-2,4,4,5,-4,-10,4,6,-5,1]],[[7,10,5,9,-10,8,9,-9,-2,4,-7,-2,8,-4],[-1,4,-8,3,8,3,-10,-2,-4,2,7,3,8,4],[5,10,-5,-4,-9,-8,-9,-6,1,8,1,3,-3,4],[4,-9,8,-5,-4,-7,5,9,-6,5,-3,5,10,-3],[-6,8,5,-9,9,-9,4,-5,3,7,8,-9,4,6],[3,8,-8,-9,6,-7,3,-7,4,-8,-5,-6,-4,4],[8,1,-1,3,7,-2,2,-9,7,-2,9,10,4,7],[-1,-5,4,2,-6,5,-7,-8,10,1,-5,-10,2,8],[-8,-3,7,7,7,7,2,-9,-2,-7,-6,10,3,6],[2,3,-1,8,-8,1,6,-9,1,9,-6,-6,5,6],[7,-5,-7,10,7,-8,-5,-8,-7,9,-6,-1,-3,9],[-2,7,-8,-8,-1,3,-6,-10,-9,10,-7,4,-5,10],[-2,7,-3,-1,7,5,8,5,-8,3,-5,-3,-1,-10],[2,6,10,-5,-10,-5,8,4,-8,9,3,-3,-6,3],[-3,-8,2,8,9,-6,-2,3,-8,5,5,-2,-6,9]],[[3,-3,-4,1,5,9,-3,-1,5,-2,-3,9,-2,8],[-9,-2,-10,9,6,-1,9,4,-6,-4,1,4,-4,-3],[5,6,2,-6,-3,-6,7,9,-9,6,8,-6,8,4],[-2,-10,-10,-5,-4,-5,-8,-5,8,8,5,-5,-6,1],[-1,-7,1,4,-4,6,-9,-5,1,1,2,-9,5,-1],[2,-6,4,-8,3,-8,8,-2,-2,4,-7,-5,8,7],[5,-6,-9,-4,6,-9,3,-5,-9,9,-6,-7,10,3],[5,1,9,8,2,2,-3,8,-6,6,1,-1,8,9],[1,8,-5,5,-8,3,-7,9,-6,6,9,-9,9,5],[-9,7,-10,3,6,9,-3,4,-7,-1,-8,-5,1,5],[-6,-9,-9,-3,1,-6,6,-1,-10,-10,-7,-2,-8,-2],[-2,8,1,3,4,-3,-3,-4,-4,7,-1,3,-6,5],[-3,-4,5,-5,9,-10,-5,2,10,7,2,-10,-1,-2],[-7,2,3,-6,-7,-9,-10,-3,-10,3,2,5,-1,8],[-7,10,7,-5,7,-1,4,-3,8,7,3,-9,-9,-9]],[[-9,-4,-9,-2,6,9,9,-10,-1,-7,-10,-7,4,8],[-10,4,5,-8,2,-3,5,2,3,9,4,2,-8,-7],[-7,-8,1,8,1,2,-4,-2,8,-5,7,-6,-7,6],[-9,2,9,3,-3,6,7,-9,-5,-9,8,-6,9,-7],[2,4,8,7,7,7,-1,5,-3,8,-7,10,3,10],[8,8,1,-1,-7,6,8,-5,-6,-8,5,4,-3,9],[10,7,7,8,-9,-6,-7,2,6,6,-8,-1,-8,-6],[9,8,5,9,-5,9,-6,-2,-9,-8,-2,7,7,-4],[2,10,7,3,7,5,1,-6,9,9,2,1,2,-3],[-5,-5,-9,8,-5,10,-5,4,9,2,-7,5,8,1],[-5,8,3,7,-10,-10,8,-7,-6,-10,10,-2,2,-6],[5,-8,-4,-10,-2,1,-4,7,2,6,6,5,-7,-4],[-4,9,10,10,6,10,-9,-9,3,-4,1,-5,5,4],[-6,-10,1,-2,7,-4,3,10,-9,4,7,9,9,7],[-3,-7,1,1,-7,4,4,8,4,-1,10,-4,-5,-5]],[[6,-2,2,2,-9,7,6,1,-1,-9,-10,9,8,-7],[6,-1,5,-5,-3,2,8,7,3,5,-10,9,9,-9],[1,1,-9,2,-6,-3,-2,2,-6,-5,8,3,8,-7],[1,-3,-4,-2,7,-1,10,3,-10,-3,5,-7,10,2],[-5,-5,8,9,-4,-7,4,5,1,-8,-2,-9,-9,-1],[-6,10,-3,8,-5,-3,9,-10,-9,8,3,-3,7,4],[-8,-8,10,-8,3,4,4,-6,9,-7,-1,10,-5,2],[5,-9,-3,-7,-4,-5,10,4,-7,8,-8,-4,-4,-4],[-7,10,-4,-5,7,-9,-9,-10,4,-7,-6,-6,-2,5],[7,6,8,8,-4,-9,6,-3,-10,8,-7,-4,-9,-9],[-3,8,6,3,-9,-5,3,7,-2,6,1,8,8,3],[4,-10,-6,4,2,5,-8,8,6,3,-4,-2,3,-5],[1,8,-9,10,-7,-7,-4,4,-5,-5,6,9,-7,6],[-10,-2,-10,4,-9,7,3,-6,-8,-8,1,-4,-1,8],[5,-9,9,-5,2,-10,-8,-6,1,-7,-2,-2,10,3]],[[-2,-1,-7,3,4,6,-9,-6,3,9,5,5,-1,-4],[4,4,8,-2,-10,10,-4,9,-3,2,8,-2,-5,2],[-3,-1,-2,2,2,5,-10,5,1,7,8,10,1,9],[-8,-6,-5,-9,-1,7,6,7,-6,9,-6,-1,-8,-2],[-4,6,2,-4,-6,4,-3,-1,2,6,10,-5,-4,5],[-1,2,8,9,8,6,4,1,2,8,-10,4,-2,8],[-7,-9,-10,6,-6,7,-6,-8,-5,-10,3,-3,-2,2],[-5,-9,5,-3,-8,-2,-3,8,2,-4,9,5,3,4],[2,9,-8,2,-8,-8,-5,1,-9,-1,-9,9,-8,9],[-2,-7,8,-4,6,-10,2,-3,10,8,4,-10,2,-2],[-4,10,-1,2,4,-8,3,-7,7,3,3,-7,-1,-2],[8,3,-5,10,1,7,-10,-4,-2,8,-10,-9,6,-1],[-2,-8,-9,2,6,-1,-4,10,3,6,6,9,9,-10],[3,-10,6,-5,10,10,9,-3,-2,-8,-9,-4,-8,-3],[-10,-2,4,-8,-3,-7,10,1,1,-4,-8,-1,7,-2]],[[-8,-4,7,3,-1,2,-6,6,-6,-9,2,-1,-8,-7],[-8,1,-3,-6,2,-2,2,4,-10,-6,-9,3,-8,10],[-7,-10,6,-10,-6,-1,-6,1,4,-8,8,-3,8,-8],[2,-2,-7,-3,4,5,-2,8,7,5,-5,-8,-6,-3],[6,-1,-1,7,-7,-4,6,1,-4,-3,8,-6,3,-9],[-4,-5,4,-1,1,7,-8,1,10,9,2,-7,-4,-7],[-7,-7,-9,-5,10,-1,4,3,1,-6,-7,-5,9,-3],[-4,-1,9,6,-2,-4,-7,-7,3,2,3,4,-3,3],[10,-6,-8,-7,-6,-6,4,-5,5,1,-10,-3,-1,7],[6,7,-5,10,1,-2,-10,7,6,-6,-4,10,-2,-8],[-10,8,-4,9,1,5,-9,-8,5,5,-1,-4,-10,8],[-7,-6,3,10,2,-9,3,4,10,10,-1,-9,-8,7],[7,-1,-4,-9,4,8,-1,8,10,-5,-5,-10,-2,9],[1,-9,1,-3,8,6,3,7,-1,-9,6,-3,-9,-9],[1,-10,-4,-1,8,2,7,-5,1,4,6,3,7,4]]], dtype = "uint8")#candidate|7370|(7, 15, 14)|const|uint8
const_7371 = relay.const([[[-3,3,-7,-6,-6,-3,5,9,-1,5,-3,8,-10,-6],[-4,-8,10,-8,-6,-4,-7,5,5,5,2,10,6,1],[-9,-7,-8,9,-6,-6,1,9,7,9,8,7,-4,3],[-5,10,-3,-6,-1,10,-3,-4,-6,-4,6,4,9,-4],[-10,-5,-3,-10,1,9,2,1,-6,2,7,7,-9,-7],[-4,-3,10,-1,2,-1,-7,7,10,5,-5,1,10,5],[-1,-2,-3,-1,-1,-8,-4,-10,-9,-10,-6,-6,9,5],[5,3,-4,3,7,2,6,3,-9,1,-9,-5,-4,-10],[-8,4,-4,-9,1,-6,6,8,-8,-2,-5,4,-3,-3],[-10,2,5,-1,-7,7,-4,8,-3,-2,1,-7,-8,-4],[-10,10,9,9,-1,7,3,-6,9,5,-2,10,-4,2],[7,-2,5,6,7,-2,-8,-4,2,-5,6,10,10,3],[-8,5,3,2,-1,-5,-6,7,-3,4,-3,-4,-1,-6],[8,-5,6,-4,9,-8,8,1,8,9,-8,-7,-2,-7],[9,3,5,-6,8,-10,7,7,1,1,-5,5,1,-2]],[[4,5,-7,3,-6,10,8,-1,10,-2,6,-2,-4,-4],[-10,-8,-8,-10,-3,6,1,-3,8,7,4,8,-3,-10],[-9,1,-3,-4,4,-7,-8,-6,8,9,5,-1,7,10],[-4,-6,7,2,8,10,-1,-9,-7,-9,4,1,6,-10],[-5,-3,-1,2,6,-5,-2,-6,-9,6,-10,10,-5,-5],[5,3,4,-9,-5,-10,-4,5,9,3,-8,3,-1,4],[-6,-6,2,2,-7,10,9,3,6,-1,1,2,-10,7],[-10,9,8,8,7,10,9,4,-2,3,-6,5,-8,-7],[2,2,-5,-7,-6,-6,2,-7,-6,1,9,-7,10,-2],[-7,-7,-3,10,-1,2,1,-2,-4,6,-9,7,2,-3],[-6,-1,4,-1,-8,-6,9,8,-7,-2,9,-10,-6,-6],[-3,-3,2,1,3,-4,4,-1,1,2,10,-1,-2,7],[10,-8,-2,3,4,-1,-7,-7,-6,-3,-8,5,8,4],[8,2,5,-4,-3,-1,10,-4,-9,-9,1,-2,-8,-4],[-6,8,2,-4,10,-3,5,-1,-8,-4,-8,-3,-5,-8]],[[5,-9,2,5,-7,-2,6,-1,-1,-8,9,-7,-4,-8],[7,-4,-9,1,10,7,6,-8,5,5,-2,-7,4,-8],[6,9,-1,4,-6,1,-5,-5,8,-3,-3,-10,-3,5],[-3,-8,-8,-10,2,7,3,3,-6,6,4,-8,-2,-3],[5,4,1,-7,-1,-8,-5,8,-4,-3,-3,-4,-2,5],[1,7,-6,-4,-3,9,-1,6,3,3,6,8,7,-6],[6,-3,9,-3,-2,-5,-1,10,1,-8,-9,2,7,5],[-3,4,-4,6,-10,-10,9,7,10,-2,3,-3,-10,-8],[-4,2,-5,9,-7,5,-8,-8,-2,7,-4,1,10,8],[9,-9,-10,-2,-9,-6,-6,4,8,10,-8,-10,-7,-10],[2,-7,3,-6,6,9,7,-4,6,8,1,-2,5,1],[-10,9,8,-5,-9,-5,-8,-10,10,9,-1,8,5,3],[1,-3,5,-6,-5,6,-3,9,-5,-6,5,1,-2,-10],[-2,-8,6,-5,-1,-6,2,-10,-2,6,-2,-6,-6,4],[7,-7,-8,-1,6,7,-9,-4,4,-5,7,-8,4,5]],[[-1,9,7,-9,1,-1,-8,-6,3,7,8,-6,5,-3],[7,8,8,-8,-3,10,-8,3,-1,-2,-1,-4,3,1],[5,5,-1,-4,10,4,10,7,6,4,1,4,7,8],[-7,9,4,-7,-9,-5,-2,2,6,-10,1,2,1,3],[-3,9,-1,-3,2,-1,-1,-10,7,5,-3,-6,8,-8],[3,9,4,7,6,-2,1,1,-10,-7,5,10,6,4],[-5,4,-6,3,1,-7,1,-7,-5,-6,-3,3,4,8],[1,-7,6,4,6,-4,-9,-6,-4,-3,-3,-5,-2,4],[2,-10,-6,9,10,-4,1,3,-10,-10,-4,-3,-2,5],[5,-3,-3,-3,-10,1,-6,-6,4,8,-10,8,1,-5],[8,-8,1,-3,2,3,8,4,8,2,-9,6,7,7],[3,-1,-2,-5,10,-7,-2,6,4,-4,10,-6,6,-10],[6,-1,9,-10,-10,-4,-3,-5,-3,6,1,-2,6,9],[2,5,9,6,9,-1,-3,1,9,-2,5,10,10,6],[-1,-9,6,-2,-1,5,6,-1,4,-8,6,-5,-10,8]],[[8,5,8,-4,-8,-1,5,-9,3,-2,1,-2,-10,9],[-2,9,10,-1,5,-5,4,-2,-2,-1,-2,-4,5,-10],[-4,6,-6,8,-6,-4,-6,6,5,-10,10,3,-6,-4],[4,-7,-3,-4,7,-6,-1,-8,1,9,-9,-2,10,-10],[4,-9,-8,-7,-1,-1,-3,5,-1,-2,-4,-8,-10,1],[-8,8,5,-10,-4,-3,8,-5,-2,6,1,6,1,-8],[8,2,-2,-8,8,9,5,-8,7,3,-4,-5,-8,-2],[-6,-9,4,10,2,3,6,-1,-4,-5,4,2,-8,5],[-7,5,1,-8,5,-3,6,4,-7,-4,-6,6,6,8],[-5,9,3,-7,-8,-9,7,-10,7,-6,9,-9,-10,4],[3,1,6,1,-4,4,-7,4,5,6,8,-10,3,-3],[-4,-8,-9,-6,9,-4,8,-6,1,9,-4,1,9,8],[-1,-7,-7,4,6,-1,-9,-9,-3,4,-4,1,9,7],[-3,2,-5,-1,-5,-10,-6,5,8,-2,8,-6,-8,8],[8,5,-2,7,7,-2,2,-3,-5,-4,4,-3,-10,5]],[[-7,-5,-2,-8,1,-4,3,1,9,4,4,-6,-3,-3],[9,1,4,-1,-10,1,-4,10,-10,-5,-6,-3,-6,-1],[10,-4,-1,-7,2,-1,6,-6,4,10,-8,1,3,-6],[-2,9,-8,-3,7,6,-7,-6,7,-5,-7,-5,9,8],[-1,-2,1,9,6,10,1,5,-1,2,2,-10,-2,5],[-2,-3,9,-8,-7,-10,8,-6,-6,-8,3,-6,5,5],[3,-9,5,8,5,4,4,5,-8,2,4,-2,9,-4],[-7,4,-1,3,-2,1,10,9,1,-9,-7,-4,2,-9],[-7,-7,-6,-2,-1,4,-9,-1,2,4,-8,-4,-3,-7],[6,6,-3,-6,4,-7,-7,8,-5,5,-1,-1,-2,-5],[3,10,1,3,-8,2,-8,-7,-9,-1,6,-2,-4,7],[7,-1,-3,10,-6,10,1,-8,-1,4,-1,-4,10,3],[8,10,-1,6,1,-10,8,-4,1,7,-8,2,7,-6],[4,3,-1,-7,-1,6,10,10,5,-4,6,8,4,5],[8,8,-3,5,-3,6,-7,7,-10,5,9,-10,1,-8]],[[10,6,-7,9,7,-3,6,4,4,3,6,-9,-7,1],[9,-3,-5,4,-5,-1,8,-1,-5,-10,-6,-3,10,7],[-1,5,8,-8,9,4,-6,6,-8,8,4,2,-10,-2],[7,6,-8,9,-1,8,8,3,6,5,10,7,1,4],[4,-10,7,-10,-10,-10,5,-10,1,-6,5,-1,3,1],[-5,5,-10,2,-4,-2,-5,-3,2,3,7,2,-1,8],[-9,7,-3,7,9,3,-4,-6,-7,1,-4,-7,-6,-6],[-10,-10,-3,-6,1,-2,-3,-4,9,-7,-2,-10,-3,-9],[3,-5,-10,-5,3,-9,-3,7,-7,-4,-2,3,-9,10],[9,2,-5,-7,1,-7,-3,9,9,-3,-6,3,8,-1],[10,-1,-3,10,-10,-2,-1,5,5,-2,-9,-9,2,2],[9,-8,-7,5,-4,9,-6,-6,7,-2,7,-7,9,-9],[9,2,5,6,-1,-3,7,-10,10,-9,9,-1,7,3],[7,8,5,3,-10,-3,9,-5,-5,-9,-4,6,-2,-2],[-9,5,-8,2,-3,-3,-6,-5,2,1,-6,6,3,-3]]], dtype = "uint8")#candidate|7371|(7, 15, 14)|const|uint8
bop_7372 = relay.logical_xor(const_7370.astype('uint8'), relay.reshape(const_7371.astype('uint8'), relay.shape_of(const_7370))) # shape=(7, 15, 14)
func_1189_call = mod.get_global_var('func_1189')
func_1192_call = mutated_mod.get_global_var('func_1192')
var_7382 = relay.var("var_7382", dtype = "uint32", shape = ())#candidate|7382|()|var|uint32
var_7383 = relay.var("var_7383", dtype = "uint32", shape = (180, 2))#candidate|7383|(180, 2)|var|uint32
call_7381 = relay.TupleGetItem(func_1189_call(relay.reshape(var_7382.astype('uint32'), []), relay.reshape(var_7383.astype('uint32'), [12, 3, 10]), ), 1)
call_7384 = relay.TupleGetItem(func_1192_call(relay.reshape(var_7382.astype('uint32'), []), relay.reshape(var_7383.astype('uint32'), [12, 3, 10]), ), 1)
func_5276_call = mod.get_global_var('func_5276')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_7385 = relay.TupleGetItem(func_5276_call(), 4)
call_7386 = relay.TupleGetItem(func_5277_call(), 4)
output = relay.Tuple([bop_7372,call_7381,var_7382,var_7383,call_7385,])
output2 = relay.Tuple([bop_7372,call_7384,var_7382,var_7383,call_7386,])
func_7388 = relay.Function([var_7382,var_7383,], output)
mod['func_7388'] = func_7388
mod = relay.transform.InferType()(mod)
var_7389 = relay.var("var_7389", dtype = "uint32", shape = ())#candidate|7389|()|var|uint32
var_7390 = relay.var("var_7390", dtype = "uint32", shape = (180, 2))#candidate|7390|(180, 2)|var|uint32
output = func_7388(var_7389,var_7390,)
func_7391 = relay.Function([var_7389,var_7390,], output)
mutated_mod['func_7391'] = func_7391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3416_call = mod.get_global_var('func_3416')
func_3418_call = mutated_mod.get_global_var('func_3418')
call_7413 = relay.TupleGetItem(func_3416_call(), 0)
call_7414 = relay.TupleGetItem(func_3418_call(), 0)
output = call_7413
output2 = call_7414
func_7422 = relay.Function([], output)
mod['func_7422'] = func_7422
mod = relay.transform.InferType()(mod)
output = func_7422()
func_7423 = relay.Function([], output)
mutated_mod['func_7423'] = func_7423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5771_call = mod.get_global_var('func_5771')
func_5773_call = mutated_mod.get_global_var('func_5773')
call_7456 = relay.TupleGetItem(func_5771_call(), 1)
call_7457 = relay.TupleGetItem(func_5773_call(), 1)
func_4579_call = mod.get_global_var('func_4579')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_7470 = func_4579_call()
call_7471 = func_4579_call()
output = relay.Tuple([call_7456,call_7470,])
output2 = relay.Tuple([call_7457,call_7471,])
func_7474 = relay.Function([], output)
mod['func_7474'] = func_7474
mod = relay.transform.InferType()(mod)
output = func_7474()
func_7475 = relay.Function([], output)
mutated_mod['func_7475'] = func_7475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4570_call = mod.get_global_var('func_4570')
func_4571_call = mutated_mod.get_global_var('func_4571')
call_7536 = relay.TupleGetItem(func_4570_call(), 0)
call_7537 = relay.TupleGetItem(func_4571_call(), 0)
func_6903_call = mod.get_global_var('func_6903')
func_6906_call = mutated_mod.get_global_var('func_6906')
const_7540 = relay.const([9.771222,-6.080910,-6.407749,-4.717654,1.470951,-4.463317,9.354915,-3.640869,-4.603345,2.309849,-2.969295,-1.777797,-9.306766,4.500224,-7.715275,-7.722727,-2.695834,7.318052,-7.164063,4.861769,6.521713,6.415266,-4.743614,-1.883476,-4.114400,-9.757288,-1.302541,-1.552067,2.986260,-4.774089,7.179561,3.479076,0.171772,-8.391358,8.143764,3.659998,-8.355217,4.435342,-3.780367,1.152625,6.858707,-5.181392,-6.175830,-7.901537,-9.195262,4.858109,9.122849,-2.866890,-2.816811,-4.544656,-9.224664,-3.318374,-4.102038,-0.521635,7.885523,1.529637,3.579057,-1.286297,3.971484,6.913598,-2.702797,8.421285,-6.689147,-7.944656,4.595664,-2.846184,9.495169,-3.192954,-4.587906,-0.277794,-6.687691,-1.711543,9.024979,-5.763723,-1.881451,2.085309,-1.878720,-9.515594,-8.630663,8.224012,-6.841226,2.699155,-3.468382,0.584851,-1.359613,3.918919,-7.781439,-3.988534,-0.861313,-9.697791,6.320975,8.215257,-9.761442,-0.543670,0.325885,-9.318886,4.962476,2.176318,1.927068,-2.407590,-4.186787,3.221191,3.078262,8.895496,-5.379874,-6.685382,1.350183,4.871855,-2.072024,-3.703402,-1.536567,5.494582,-2.657756,8.593309,9.835913,-1.635892,8.623617,-8.119882,1.977993,9.639360,6.770038,3.382434,4.560328,0.467222,-2.937489,9.851998,-7.849309,-2.212409,6.319898,5.012596,8.607316,1.430234,1.443645,-6.552620,3.493292,-4.310604,6.255421,8.280591,-4.418163,-5.077602,-9.213750,2.770549,-4.866486,0.121852,-0.494096,4.411504,-9.361447,-1.296047,-4.050169,8.227211,-4.142543,8.756900,7.817741,0.908430,2.141979,3.944312,6.538780,-7.632697,-9.456482,-5.209675,-2.055624,9.703391,-6.619292,-2.500210,-9.321541,-4.305437,0.457689,-0.259419,-1.985614,8.511200,-9.780291,2.303962,1.434164,9.518810,5.599603,-1.383584,4.583423,8.008502,-3.989941,6.382567,2.952897,3.794312], dtype = "float32")#candidate|7540|(182,)|const|float32
call_7539 = relay.TupleGetItem(func_6903_call(relay.reshape(const_7540.astype('float32'), [26, 7])), 3)
call_7541 = relay.TupleGetItem(func_6906_call(relay.reshape(const_7540.astype('float32'), [26, 7])), 3)
func_5581_call = mod.get_global_var('func_5581')
func_5583_call = mutated_mod.get_global_var('func_5583')
call_7542 = func_5581_call()
call_7543 = func_5581_call()
func_995_call = mod.get_global_var('func_995')
func_997_call = mutated_mod.get_global_var('func_997')
call_7547 = relay.TupleGetItem(func_995_call(relay.reshape(call_7542.astype('int32'), [8, 7, 3])), 0)
call_7548 = relay.TupleGetItem(func_997_call(relay.reshape(call_7542.astype('int32'), [8, 7, 3])), 0)
output = relay.Tuple([call_7536,call_7539,const_7540,call_7542,call_7547,])
output2 = relay.Tuple([call_7537,call_7541,const_7540,call_7543,call_7548,])
func_7550 = relay.Function([], output)
mod['func_7550'] = func_7550
mod = relay.transform.InferType()(mod)
mutated_mod['func_7550'] = func_7550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7550_call = mutated_mod.get_global_var('func_7550')
call_7551 = func_7550_call()
output = call_7551
func_7552 = relay.Function([], output)
mutated_mod['func_7552'] = func_7552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7556 = relay.var("var_7556", dtype = "uint8", shape = (7, 16, 15))#candidate|7556|(7, 16, 15)|var|uint8
var_7557 = relay.var("var_7557", dtype = "uint8", shape = (7, 16, 15))#candidate|7557|(7, 16, 15)|var|uint8
bop_7558 = relay.bitwise_xor(var_7556.astype('uint8'), relay.reshape(var_7557.astype('uint8'), relay.shape_of(var_7556))) # shape=(7, 16, 15)
output = bop_7558
output2 = bop_7558
func_7564 = relay.Function([var_7556,var_7557,], output)
mod['func_7564'] = func_7564
mod = relay.transform.InferType()(mod)
mutated_mod['func_7564'] = func_7564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7564_call = mutated_mod.get_global_var('func_7564')
var_7566 = relay.var("var_7566", dtype = "uint8", shape = (7, 16, 15))#candidate|7566|(7, 16, 15)|var|uint8
var_7567 = relay.var("var_7567", dtype = "uint8", shape = (7, 16, 15))#candidate|7567|(7, 16, 15)|var|uint8
call_7565 = func_7564_call(var_7566,var_7567,)
output = call_7565
func_7568 = relay.Function([var_7566,var_7567,], output)
mutated_mod['func_7568'] = func_7568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2231_call = mod.get_global_var('func_2231')
func_2232_call = mutated_mod.get_global_var('func_2232')
call_7578 = func_2231_call()
call_7579 = func_2231_call()
func_5454_call = mod.get_global_var('func_5454')
func_5457_call = mutated_mod.get_global_var('func_5457')
const_7590 = relay.const([[-6,1,-10,-5,4,8,-7,10]], dtype = "uint8")#candidate|7590|(1, 8)|const|uint8
call_7589 = func_5454_call(relay.reshape(const_7590.astype('uint8'), [2, 4, 1]))
call_7591 = func_5454_call(relay.reshape(const_7590.astype('uint8'), [2, 4, 1]))
bop_7592 = relay.minimum(call_7589.astype('int16'), relay.reshape(const_7590.astype('int16'), relay.shape_of(call_7589))) # shape=(2, 4, 1)
bop_7595 = relay.minimum(call_7591.astype('int16'), relay.reshape(const_7590.astype('int16'), relay.shape_of(call_7591))) # shape=(2, 4, 1)
output = relay.Tuple([call_7578,bop_7592,])
output2 = relay.Tuple([call_7579,bop_7595,])
func_7604 = relay.Function([], output)
mod['func_7604'] = func_7604
mod = relay.transform.InferType()(mod)
output = func_7604()
func_7605 = relay.Function([], output)
mutated_mod['func_7605'] = func_7605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_505_call = mod.get_global_var('func_505')
func_507_call = mutated_mod.get_global_var('func_507')
call_7612 = relay.TupleGetItem(func_505_call(), 0)
call_7613 = relay.TupleGetItem(func_507_call(), 0)
output = call_7612
output2 = call_7613
func_7626 = relay.Function([], output)
mod['func_7626'] = func_7626
mod = relay.transform.InferType()(mod)
output = func_7626()
func_7627 = relay.Function([], output)
mutated_mod['func_7627'] = func_7627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7676 = relay.var("var_7676", dtype = "float32", shape = (11, 13, 8))#candidate|7676|(11, 13, 8)|var|float32
var_7677 = relay.var("var_7677", dtype = "float32", shape = (11, 13, 8))#candidate|7677|(11, 13, 8)|var|float32
bop_7678 = relay.mod(var_7676.astype('float32'), relay.reshape(var_7677.astype('float32'), relay.shape_of(var_7676))) # shape=(11, 13, 8)
uop_7693 = relay.exp(var_7676.astype('float32')) # shape=(11, 13, 8)
output = relay.Tuple([bop_7678,uop_7693,])
output2 = relay.Tuple([bop_7678,uop_7693,])
func_7707 = relay.Function([var_7676,var_7677,], output)
mod['func_7707'] = func_7707
mod = relay.transform.InferType()(mod)
var_7708 = relay.var("var_7708", dtype = "float32", shape = (11, 13, 8))#candidate|7708|(11, 13, 8)|var|float32
var_7709 = relay.var("var_7709", dtype = "float32", shape = (11, 13, 8))#candidate|7709|(11, 13, 8)|var|float32
output = func_7707(var_7708,var_7709,)
func_7710 = relay.Function([var_7708,var_7709,], output)
mutated_mod['func_7710'] = func_7710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5064_call = mod.get_global_var('func_5064')
func_5065_call = mutated_mod.get_global_var('func_5065')
call_7723 = relay.TupleGetItem(func_5064_call(), 1)
call_7724 = relay.TupleGetItem(func_5065_call(), 1)
output = relay.Tuple([call_7723,])
output2 = relay.Tuple([call_7724,])
func_7733 = relay.Function([], output)
mod['func_7733'] = func_7733
mod = relay.transform.InferType()(mod)
mutated_mod['func_7733'] = func_7733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7733_call = mutated_mod.get_global_var('func_7733')
call_7734 = func_7733_call()
output = call_7734
func_7735 = relay.Function([], output)
mutated_mod['func_7735'] = func_7735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_7736 = relay.TupleGetItem(func_377_call(), 3)
call_7737 = relay.TupleGetItem(func_379_call(), 3)
func_4628_call = mod.get_global_var('func_4628')
func_4630_call = mutated_mod.get_global_var('func_4630')
call_7753 = relay.TupleGetItem(func_4628_call(), 0)
call_7754 = relay.TupleGetItem(func_4630_call(), 0)
func_1690_call = mod.get_global_var('func_1690')
func_1692_call = mutated_mod.get_global_var('func_1692')
var_7767 = relay.var("var_7767", dtype = "float32", shape = (520,))#candidate|7767|(520,)|var|float32
call_7766 = func_1690_call(relay.reshape(var_7767.astype('float32'), [10, 4, 13]))
call_7768 = func_1690_call(relay.reshape(var_7767.astype('float32'), [10, 4, 13]))
func_6365_call = mod.get_global_var('func_6365')
func_6367_call = mutated_mod.get_global_var('func_6367')
call_7783 = relay.TupleGetItem(func_6365_call(), 0)
call_7784 = relay.TupleGetItem(func_6367_call(), 0)
output = relay.Tuple([call_7736,call_7753,call_7766,var_7767,call_7783,])
output2 = relay.Tuple([call_7737,call_7754,call_7768,var_7767,call_7784,])
func_7787 = relay.Function([var_7767,], output)
mod['func_7787'] = func_7787
mod = relay.transform.InferType()(mod)
mutated_mod['func_7787'] = func_7787
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7788 = relay.var("var_7788", dtype = "float32", shape = (520,))#candidate|7788|(520,)|var|float32
func_7787_call = mutated_mod.get_global_var('func_7787')
call_7789 = func_7787_call(var_7788)
output = call_7789
func_7790 = relay.Function([var_7788], output)
mutated_mod['func_7790'] = func_7790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4570_call = mod.get_global_var('func_4570')
func_4571_call = mutated_mod.get_global_var('func_4571')
call_7818 = relay.TupleGetItem(func_4570_call(), 0)
call_7819 = relay.TupleGetItem(func_4571_call(), 0)
output = relay.Tuple([call_7818,])
output2 = relay.Tuple([call_7819,])
func_7820 = relay.Function([], output)
mod['func_7820'] = func_7820
mod = relay.transform.InferType()(mod)
output = func_7820()
func_7821 = relay.Function([], output)
mutated_mod['func_7821'] = func_7821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3021_call = mod.get_global_var('func_3021')
func_3022_call = mutated_mod.get_global_var('func_3022')
call_7834 = relay.TupleGetItem(func_3021_call(), 1)
call_7835 = relay.TupleGetItem(func_3022_call(), 1)
output = call_7834
output2 = call_7835
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
func_2786_call = mod.get_global_var('func_2786')
func_2787_call = mutated_mod.get_global_var('func_2787')
call_7844 = relay.TupleGetItem(func_2786_call(), 2)
call_7845 = relay.TupleGetItem(func_2787_call(), 2)
func_2999_call = mod.get_global_var('func_2999')
func_3001_call = mutated_mod.get_global_var('func_3001')
const_7860 = relay.const([7.739189,1.826426,7.750999,7.927119,-8.393225,6.221753,-3.058504,-3.999901,4.973275,6.149026,4.054048,-0.103052,8.486545,1.875514,-6.201476,-2.817703,3.541590,-9.777180,-1.534133,4.277741,-4.980613,1.364780,-6.300696,6.011101,-5.855326,-5.781546,-8.886513,1.266563,2.616449,-0.142552,-9.592927,9.067959,-5.765502,6.621321,-7.310021,8.519977,3.675508,1.051080,-7.051066,6.239425,7.209713,-5.425175,-0.905327,-2.232799,0.563939,3.804175,4.674959,4.408367,-7.345562,-9.995428,8.219158,9.465664,9.384280,-4.481255,9.293155,-5.292813,8.566541,-2.964610,-7.220885,-8.130736,7.338415,2.809131,-6.959140,2.590750,6.350801,4.629922,7.482952,-5.769686,3.914551,4.509555,-8.145398,-9.802021,-8.242270,-4.014400,8.279411,-9.150128,-5.138045,1.045991,7.481749,-9.551932,8.068356,2.389006,-2.205639,1.579540,4.064393,4.063443,-6.082545,4.324558,-0.428452,9.964174,-5.745898,4.520719,6.071825,-0.125439,2.477980,-3.240752,-0.048626,7.453522,7.487471,3.795358,6.383058,-8.325142,-5.222066,1.012691,3.408785,-9.873247,-3.810049,1.099743,-4.850082,-4.560365,-6.942724,-1.597899,6.732765,4.551979,-5.576374,0.890856,0.377162,9.621144,7.368249,4.504463,5.724631,0.865335,1.710686,-8.560010,-2.810816,7.443826,2.293815,9.867751,1.408348,1.986452,8.413864,-3.338198,-3.417797,-2.129720,-2.294454,2.450723,6.806186,4.483241,3.721381,4.175391,1.172376,-8.609777,-2.598174,5.248604,-8.285417,-4.989298,0.567415,3.532857,-8.944796,6.597883,3.889830,4.927299,8.610694,5.571741,-0.845311,-6.509101,7.994166,-5.327860,7.100166,2.922595,-2.930818,3.420977,-6.794116,9.585230,7.635403,9.437721,4.863377,6.345260,-2.601083,8.845126,3.796141,-1.754360,-8.352862,7.386084,-9.734728,-3.458306,-6.391561,-1.587237,-4.347884,4.831644,-9.383796,-3.032705,2.892771,9.579258,-6.636752,-0.036581,-5.027271,-2.592948,0.256452,-3.210740,-3.004262,-6.259555,1.810303,-4.258285,1.707245,8.929917,-9.314608,7.776919,9.178672,6.061106,-1.522520,-4.110431,-4.457167,7.766912,-1.390688,1.628990,-1.975242,7.175170,-4.460048,2.043877,7.028879,-3.942285,-2.987654,-5.345375,-2.413215,0.098593,2.130750,6.329424,-7.898538,-1.311040,4.469001,-3.081352,4.363421,9.501933,0.260207,2.745782,4.683330,-2.176361,-1.647953,7.232642,0.165875,6.182351,-7.116685,-0.612727,9.050164,8.885663,3.923704,6.466203,2.841460,-6.283537,5.964829,-1.256057,4.112730,9.656427,8.362535,-6.113692,9.080651,9.849337,6.824052,1.437720,-8.958442,2.153793,-8.275477,3.612309,2.266597,-4.406620,8.709431,0.538971,9.921570,-9.984969,7.458032,5.717758,-2.971570,0.365190,8.868947,4.111471,8.927227,8.677805,2.425096,-9.746718,-3.044510,9.367424,3.377128,4.880486,7.265953,0.813915,-4.479837,-8.467782,8.766938,-9.088648,-7.686556,8.787751,-4.177235,6.019057,7.296467,-0.237722,-7.295360,3.564282,-8.567415,-1.300493,0.632109,4.399365,8.399015,-8.251515,5.855583,1.390785,-7.867464,5.230394,6.580066,-3.878456,-3.110620,-4.821978,6.666872,-6.991519,-6.044710,8.641394,-5.943216,-8.750203,-4.760575,9.188958,2.294558,1.896337,9.535186,8.297737,0.475595,1.231167,-5.651944,-1.488646,0.502532,-4.238381,-6.085462,0.596660,-5.330412,-3.303605,0.144039,-3.734374,-5.756427,-7.332226,-2.443244,-0.738884,-4.043351,-7.292135,5.369405,-1.598374,3.295806,6.633484,-1.614443,0.120185,-5.411595,-1.745415,5.435337,-2.878609,-5.761411,5.838763,-4.095845,1.217541,0.479013,-7.583845,-8.303276,0.355461,2.253084,7.161202,-7.385489,-1.239392,-2.894708,-8.931591,5.347795,1.943132,7.321969,-3.360177,-7.623919,-1.693005,8.390266,9.151330,4.747774,-9.342189,0.054935,8.872238,-3.681965,-0.594702,-9.143365,-6.287799,1.197597,8.671597,-0.164881,6.861536,3.475113,-4.613128,-7.269068,7.463487,-1.669347,-5.612469,5.079157,9.090484,1.104626,1.826040,-3.828920,5.616039,4.669616,7.571578,-4.623128,5.885697,-7.538920,4.965461,1.152527,6.027119,-9.939632,6.415675,4.581523,8.235310,-8.652697,-7.120070,-8.109501,-9.499391,-0.506211,8.055559,-9.310218,7.760470,-5.914716,5.981791,1.842896,6.376569,-1.134242,9.058994,-9.851071,-3.656579,8.072144,1.446228,-4.291065,-5.934682,7.878596,-2.481415,-4.317425,5.725118,-9.857810,-8.297177,1.639363,5.389884,-2.158548,5.204329,9.315912,2.831932,-2.823905,-0.831048,-3.509157,7.685363,-8.828971,-7.390172,3.910003,7.494604,-5.016325,8.448566,3.894035,-3.696372,-5.807129,-7.218447,7.325644,-2.495676,4.974605,3.743907,7.104098,9.114093,-5.064016,-2.092811,6.662771,9.000249,8.214386,2.895025,2.435416,-3.837359,4.050990,8.702228,-4.582125,-5.913355,-6.791946,-2.358573,0.687465,2.120631,7.863046,7.325858,5.133084,-5.622453,-1.789989,4.206437,5.220744,1.562251,9.155697,-0.875965,-0.482385,5.321448,-3.359114,0.071515,1.091113,7.695081,-4.149542,-8.615353,5.825286,3.849943,-1.459395,7.639058,-5.898026,5.794762,8.110773,-0.004242,-3.811315,-5.577906,9.957300,-1.349202,-2.085424,8.896537,7.670446,-3.585071,-9.696978,-9.194598,-5.480466,5.830258,-3.176190,-2.706331,-7.457540,6.129336,-3.141813,9.631613,1.509542,7.864200,1.555571,9.225524,-0.525448,6.887204,9.365631,5.729973], dtype = "float32")#candidate|7860|(520,)|const|float32
call_7859 = relay.TupleGetItem(func_2999_call(relay.reshape(const_7860.astype('float32'), [520,])), 1)
call_7861 = relay.TupleGetItem(func_3001_call(relay.reshape(const_7860.astype('float32'), [520,])), 1)
output = relay.Tuple([call_7844,call_7859,const_7860,])
output2 = relay.Tuple([call_7845,call_7861,const_7860,])
func_7864 = relay.Function([], output)
mod['func_7864'] = func_7864
mod = relay.transform.InferType()(mod)
output = func_7864()
func_7865 = relay.Function([], output)
mutated_mod['func_7865'] = func_7865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_7897 = relay.TupleGetItem(func_776_call(), 0)
call_7898 = relay.TupleGetItem(func_778_call(), 0)
func_2732_call = mod.get_global_var('func_2732')
func_2733_call = mutated_mod.get_global_var('func_2733')
call_7899 = relay.TupleGetItem(func_2732_call(), 0)
call_7900 = relay.TupleGetItem(func_2733_call(), 0)
func_385_call = mod.get_global_var('func_385')
func_387_call = mutated_mod.get_global_var('func_387')
var_7904 = relay.var("var_7904", dtype = "float32", shape = (616,))#candidate|7904|(616,)|var|float32
call_7903 = relay.TupleGetItem(func_385_call(relay.reshape(var_7904.astype('float32'), [8, 11, 7])), 0)
call_7905 = relay.TupleGetItem(func_387_call(relay.reshape(var_7904.astype('float32'), [8, 11, 7])), 0)
output = relay.Tuple([call_7897,call_7899,call_7903,var_7904,])
output2 = relay.Tuple([call_7898,call_7900,call_7905,var_7904,])
func_7910 = relay.Function([var_7904,], output)
mod['func_7910'] = func_7910
mod = relay.transform.InferType()(mod)
var_7911 = relay.var("var_7911", dtype = "float32", shape = (616,))#candidate|7911|(616,)|var|float32
output = func_7910(var_7911)
func_7912 = relay.Function([var_7911], output)
mutated_mod['func_7912'] = func_7912
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7930 = relay.var("var_7930", dtype = "float32", shape = (11, 11, 3))#candidate|7930|(11, 11, 3)|var|float32
uop_7931 = relay.sigmoid(var_7930.astype('float32')) # shape=(11, 11, 3)
func_4457_call = mod.get_global_var('func_4457')
func_4459_call = mutated_mod.get_global_var('func_4459')
call_7938 = func_4457_call()
call_7939 = func_4457_call()
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_7957 = func_2072_call()
call_7958 = func_2072_call()
output = relay.Tuple([uop_7931,call_7938,call_7957,])
output2 = relay.Tuple([uop_7931,call_7939,call_7958,])
func_7959 = relay.Function([var_7930,], output)
mod['func_7959'] = func_7959
mod = relay.transform.InferType()(mod)
mutated_mod['func_7959'] = func_7959
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7960 = relay.var("var_7960", dtype = "float32", shape = (11, 11, 3))#candidate|7960|(11, 11, 3)|var|float32
func_7959_call = mutated_mod.get_global_var('func_7959')
call_7961 = func_7959_call(var_7960)
output = call_7961
func_7962 = relay.Function([var_7960], output)
mutated_mod['func_7962'] = func_7962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4761_call = mod.get_global_var('func_4761')
func_4762_call = mutated_mod.get_global_var('func_4762')
call_7970 = relay.TupleGetItem(func_4761_call(), 1)
call_7971 = relay.TupleGetItem(func_4762_call(), 1)
output = relay.Tuple([call_7970,])
output2 = relay.Tuple([call_7971,])
func_7972 = relay.Function([], output)
mod['func_7972'] = func_7972
mod = relay.transform.InferType()(mod)
output = func_7972()
func_7973 = relay.Function([], output)
mutated_mod['func_7973'] = func_7973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1956_call = mod.get_global_var('func_1956')
func_1957_call = mutated_mod.get_global_var('func_1957')
call_7996 = relay.TupleGetItem(func_1956_call(), 0)
call_7997 = relay.TupleGetItem(func_1957_call(), 0)
func_3927_call = mod.get_global_var('func_3927')
func_3928_call = mutated_mod.get_global_var('func_3928')
call_8022 = relay.TupleGetItem(func_3927_call(), 0)
call_8023 = relay.TupleGetItem(func_3928_call(), 0)
output = relay.Tuple([call_7996,call_8022,])
output2 = relay.Tuple([call_7997,call_8023,])
func_8041 = relay.Function([], output)
mod['func_8041'] = func_8041
mod = relay.transform.InferType()(mod)
output = func_8041()
func_8042 = relay.Function([], output)
mutated_mod['func_8042'] = func_8042
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8078 = relay.var("var_8078", dtype = "int64", shape = ())#candidate|8078|()|var|int64
const_8079 = relay.const([[[10,-8,-6,-8,-8,-4,7,4,-4,5,-9,5,10,1],[-5,-9,-3,-9,-7,-7,5,-9,3,-2,-6,-3,7,-7],[9,6,-2,-10,-4,-4,-8,-6,-4,7,-8,-4,-5,3],[5,8,7,8,9,-4,9,-1,-1,-9,-4,2,-5,-8],[1,4,-1,-10,6,-8,9,7,-2,-6,7,-7,2,-3],[-6,-9,4,5,-6,4,6,-7,5,-3,-2,1,-4,8],[-10,7,6,4,-1,-3,-5,-9,10,6,-7,4,9,9],[-6,1,10,3,-6,-5,-8,-2,-7,2,6,-3,-8,-4],[-2,10,2,5,9,-9,7,-10,2,7,-4,7,6,6],[-6,-1,-3,-8,10,6,-3,4,9,-6,7,-10,-2,-2],[-6,-2,-9,3,-4,7,-6,5,10,-1,3,-9,1,-3],[8,-1,6,-9,8,6,-2,-8,-8,10,-10,6,-10,-6],[-6,-4,-6,9,10,-6,-9,-2,5,-1,-1,-2,4,6],[5,-5,-3,-3,5,1,-9,6,9,-1,10,-7,5,-3],[7,2,-1,3,7,-3,10,-8,10,7,3,-4,-1,3]],[[-10,2,-8,-1,1,-5,10,1,-3,-8,-4,-2,4,2],[-7,-1,3,-6,8,-10,-3,-9,4,-4,-10,9,9,3],[-7,1,3,-3,-5,-7,-8,4,-3,-4,-3,-3,-1,7],[4,-5,6,-5,10,-5,-6,-10,1,-4,4,-3,-4,-10],[-1,-7,8,5,2,2,7,6,2,-6,7,1,-7,10],[3,8,-10,8,-9,-1,3,2,3,-1,-4,-7,-10,4],[-3,1,-8,-1,-6,-6,9,7,-3,2,-6,8,-2,1],[-5,9,1,5,1,-8,4,5,1,5,-10,9,-10,4],[-4,-3,-1,-9,4,-4,2,5,7,-9,-1,-2,1,-7],[-8,2,7,5,10,10,9,-1,7,-7,8,-3,-10,10],[-8,-2,-9,10,-10,3,8,5,9,-10,-4,1,3,-10],[10,-6,-8,-7,-3,-2,4,4,-3,1,5,-10,-8,-8],[6,-6,8,5,10,-5,-8,5,-4,-4,-6,-9,-6,-9],[-10,7,-4,2,-5,-2,-10,-6,-3,10,10,4,-1,-10],[-2,3,-5,-9,3,5,-2,-3,-1,1,-1,-1,7,10]],[[8,6,8,-5,-8,-6,-8,1,7,2,-4,-3,-6,-8],[10,2,8,10,-5,-1,-9,-6,-7,9,-10,3,4,10],[8,2,8,6,1,-3,2,9,-10,-2,-1,-10,-2,6],[-7,-7,-4,3,-4,-7,-8,9,-4,-1,5,-9,4,9],[10,-5,10,4,-2,6,-7,-9,3,4,10,2,-1,-4],[-2,-3,10,1,-8,6,1,6,-4,4,-6,-5,-6,-2],[9,3,10,-4,-2,10,8,-1,-7,9,-3,9,3,-6],[2,-5,-5,-2,4,5,1,-7,-3,-9,5,-2,-1,8],[8,1,1,10,-6,-10,10,-6,3,9,-2,-6,6,-5],[-2,9,4,-9,7,8,-6,6,4,-5,7,-2,-4,-4],[-8,-5,2,10,5,-1,-1,-8,9,-10,-9,-9,3,-3],[-8,7,-8,6,-8,5,8,-6,7,5,-1,7,4,-4],[5,-5,-6,1,-7,-5,-5,-8,6,-3,1,7,5,-10],[9,-5,3,1,2,-5,-1,6,1,-1,10,-2,-2,-1],[-4,-5,6,1,-9,9,4,-10,6,-1,10,8,7,-10]],[[-10,5,5,10,1,-1,4,2,5,1,10,8,7,1],[-5,-3,6,-10,-10,-2,-2,9,-2,1,7,-1,-5,6],[-7,6,-1,-7,-6,8,7,-7,3,-2,9,6,-7,-2],[6,-6,6,-4,-10,-4,10,-4,-1,8,7,3,-5,-3],[-4,7,-4,2,7,-6,7,-5,1,-3,-10,-8,-1,6],[-10,10,-5,-5,-10,-8,-10,-3,-4,3,-10,10,9,1],[-1,-8,6,-6,-5,-10,7,-1,10,-4,-6,2,5,-8],[-1,6,5,-2,2,-2,8,-1,9,2,7,6,2,9],[-1,2,5,-4,2,9,-6,10,-4,1,-4,-5,-8,6],[2,-9,-2,4,1,-6,-6,8,10,5,10,9,8,4],[-8,8,-8,2,-8,-7,-4,1,-10,1,-6,7,-4,-9],[-2,-8,5,-10,-1,-3,7,-7,3,-3,6,6,-2,-9],[9,9,-2,4,3,10,-6,-4,-1,6,-2,10,2,-1],[8,1,9,-1,-6,-8,-8,-6,9,7,-4,7,-3,3],[2,-2,-5,10,-2,5,-5,-1,-9,-9,-7,-10,9,-5]],[[6,-8,4,-1,-4,1,1,5,8,10,3,8,6,-10],[-7,9,-5,-2,-8,5,3,7,-3,3,-10,-9,-4,2],[-4,7,9,5,-3,-10,9,5,5,-7,4,-10,-2,-7],[7,-6,-2,-2,-9,3,-3,4,-2,3,1,-8,9,9],[-8,-10,6,5,9,8,-6,1,-8,9,-4,-9,-4,9],[-6,9,-9,-10,4,-2,5,-2,-3,-10,10,10,4,8],[-6,-3,9,6,-10,-2,2,-1,4,-7,8,5,-9,-1],[-4,-2,8,-1,-9,5,-1,-6,-9,-9,-10,-9,6,-6],[8,-7,-8,3,6,3,8,5,-4,-4,7,7,2,8],[1,2,-3,4,-7,7,8,1,9,7,8,-8,5,-4],[3,-4,8,-6,4,-2,4,6,-1,-9,-2,6,8,-5],[-1,-9,-1,-3,-8,9,8,4,-1,5,9,6,2,3],[8,-4,-7,5,7,-6,-6,8,-8,-7,5,3,-8,7],[-1,-2,8,-7,-3,4,2,-5,-9,-2,7,6,-1,-8],[-7,1,-5,6,2,-2,-8,5,10,-8,-2,4,2,-3]],[[-8,-4,-6,-5,-1,-6,-6,8,-7,-4,2,4,4,5],[-7,-9,-9,-1,9,8,9,-4,4,-9,-4,6,8,-10],[-9,8,-5,-2,-3,9,-1,3,1,-4,-9,6,7,9],[-3,10,8,-9,-7,7,-5,2,-3,3,2,9,-2,7],[8,-5,-7,-4,-2,-5,-3,9,-9,4,-7,8,-6,-3],[3,-8,-3,1,-9,-2,7,2,-2,-7,-3,4,8,1],[8,-2,1,-9,4,-4,-6,-6,8,2,10,-2,2,4],[6,6,7,-5,10,3,-6,9,-7,-5,-2,4,8,-6],[10,2,3,-1,8,9,10,3,2,5,8,4,-9,-3],[-4,7,7,1,-7,-2,-6,2,6,-1,-9,6,8,-9],[-10,-2,-1,10,8,10,4,10,-5,-8,-10,-7,-5,8],[5,-10,10,-9,1,-1,-3,-4,-2,-8,7,-8,-5,7],[2,-7,3,-3,-9,5,4,-1,-6,-3,-9,7,-9,4],[2,7,-7,2,-10,-4,-9,-1,5,-1,6,9,-7,3],[1,-1,9,8,2,5,-7,3,9,3,5,-3,10,-6]],[[8,2,-9,4,-10,-3,4,-6,-10,-1,2,-1,7,-8],[5,3,-5,5,-7,1,1,2,5,-10,-9,-2,-4,8],[8,-8,1,-8,-6,2,2,-5,-1,-10,-6,-9,-1,6],[5,-9,-1,8,10,-10,-1,-4,-8,-5,7,-3,-8,-8],[7,-6,-7,7,-6,7,3,4,2,6,-8,-8,8,8],[8,-7,-7,9,-2,9,3,3,5,-1,-5,8,-10,8],[8,6,-9,10,9,-9,6,-6,6,-7,7,2,5,-7],[6,4,1,-1,6,8,1,-4,-7,-7,2,-8,2,-2],[9,1,-7,9,-7,-10,-10,-8,-8,-9,5,-2,8,7],[-9,6,-8,-3,-3,3,-1,-5,-3,-3,5,8,7,-8],[-1,6,2,9,-2,7,5,7,2,8,-3,6,4,-8],[5,10,1,-7,-2,4,-9,9,-10,-9,-8,-8,9,-9],[-10,-7,-2,-3,5,-7,8,-8,2,-2,-4,7,-9,3],[8,2,8,5,6,-5,9,7,5,4,-5,-2,-7,-10],[-3,-4,-4,1,6,6,-3,5,4,9,7,9,-8,-2]],[[-9,1,5,2,-4,3,-10,-3,9,7,10,-5,9,-1],[-2,-4,-5,-4,2,2,-1,-5,-4,-4,-6,8,-6,5],[4,2,6,10,1,-2,10,-9,8,1,-6,-7,-7,10],[-10,9,-8,-4,7,10,6,2,-5,-6,-9,-7,4,-7],[10,4,-10,-6,4,-7,-1,-8,8,-4,3,9,9,-4],[1,3,9,-3,-10,1,8,4,6,6,-4,-8,10,-6],[5,-1,-3,10,-2,3,2,6,4,9,2,4,8,2],[9,-9,9,-1,-4,4,-3,-10,3,-5,3,-4,1,-10],[2,-7,9,-7,5,1,-8,7,-2,-6,-2,1,-7,10],[-5,-5,2,9,-7,10,-4,-3,-5,-4,9,3,3,5],[-1,9,7,4,-7,1,-9,8,-3,8,1,-7,3,10],[-6,-9,-1,-2,2,8,-8,3,-1,1,-10,-5,2,-3],[-4,3,9,-4,10,-9,-1,-2,-5,6,-6,3,5,-8],[10,4,-6,3,-10,-6,-4,-3,-1,3,9,-3,6,2],[-5,-10,4,10,-10,-5,-1,-1,5,1,-8,-3,6,4]]], dtype = "int64")#candidate|8079|(8, 15, 14)|const|int64
bop_8080 = relay.greater(var_8078.astype('bool'), const_8079.astype('bool')) # shape=(8, 15, 14)
output = relay.Tuple([bop_8080,])
output2 = relay.Tuple([bop_8080,])
func_8089 = relay.Function([var_8078,], output)
mod['func_8089'] = func_8089
mod = relay.transform.InferType()(mod)
mutated_mod['func_8089'] = func_8089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8090 = relay.var("var_8090", dtype = "int64", shape = ())#candidate|8090|()|var|int64
func_8089_call = mutated_mod.get_global_var('func_8089')
call_8091 = func_8089_call(var_8090)
output = call_8091
func_8092 = relay.Function([var_8090], output)
mutated_mod['func_8092'] = func_8092
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8101 = relay.var("var_8101", dtype = "int16", shape = (9, 2, 10))#candidate|8101|(9, 2, 10)|var|int16
var_8102 = relay.var("var_8102", dtype = "int16", shape = (9, 2, 10))#candidate|8102|(9, 2, 10)|var|int16
bop_8103 = relay.maximum(var_8101.astype('int16'), relay.reshape(var_8102.astype('int16'), relay.shape_of(var_8101))) # shape=(9, 2, 10)
output = bop_8103
output2 = bop_8103
func_8109 = relay.Function([var_8101,var_8102,], output)
mod['func_8109'] = func_8109
mod = relay.transform.InferType()(mod)
mutated_mod['func_8109'] = func_8109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8109_call = mutated_mod.get_global_var('func_8109')
var_8111 = relay.var("var_8111", dtype = "int16", shape = (9, 2, 10))#candidate|8111|(9, 2, 10)|var|int16
var_8112 = relay.var("var_8112", dtype = "int16", shape = (9, 2, 10))#candidate|8112|(9, 2, 10)|var|int16
call_8110 = func_8109_call(var_8111,var_8112,)
output = call_8110
func_8113 = relay.Function([var_8111,var_8112,], output)
mutated_mod['func_8113'] = func_8113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_8170 = relay.TupleGetItem(func_377_call(), 1)
call_8171 = relay.TupleGetItem(func_379_call(), 1)
output = call_8170
output2 = call_8171
func_8202 = relay.Function([], output)
mod['func_8202'] = func_8202
mod = relay.transform.InferType()(mod)
output = func_8202()
func_8203 = relay.Function([], output)
mutated_mod['func_8203'] = func_8203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3583_call = mod.get_global_var('func_3583')
func_3584_call = mutated_mod.get_global_var('func_3584')
call_8243 = relay.TupleGetItem(func_3583_call(), 0)
call_8244 = relay.TupleGetItem(func_3584_call(), 0)
func_740_call = mod.get_global_var('func_740')
func_742_call = mutated_mod.get_global_var('func_742')
call_8246 = relay.TupleGetItem(func_740_call(), 1)
call_8247 = relay.TupleGetItem(func_742_call(), 1)
func_8041_call = mod.get_global_var('func_8041')
func_8042_call = mutated_mod.get_global_var('func_8042')
call_8251 = relay.TupleGetItem(func_8041_call(), 0)
call_8252 = relay.TupleGetItem(func_8042_call(), 0)
func_7838_call = mod.get_global_var('func_7838')
func_7840_call = mutated_mod.get_global_var('func_7840')
call_8306 = func_7838_call()
call_8307 = func_7838_call()
output = relay.Tuple([call_8243,call_8246,call_8251,call_8306,])
output2 = relay.Tuple([call_8244,call_8247,call_8252,call_8307,])
func_8326 = relay.Function([], output)
mod['func_8326'] = func_8326
mod = relay.transform.InferType()(mod)
output = func_8326()
func_8327 = relay.Function([], output)
mutated_mod['func_8327'] = func_8327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2704_call = mod.get_global_var('func_2704')
func_2706_call = mutated_mod.get_global_var('func_2706')
call_8354 = func_2704_call()
call_8355 = func_2704_call()
output = call_8354
output2 = call_8355
func_8378 = relay.Function([], output)
mod['func_8378'] = func_8378
mod = relay.transform.InferType()(mod)
mutated_mod['func_8378'] = func_8378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8378_call = mutated_mod.get_global_var('func_8378')
call_8379 = func_8378_call()
output = call_8379
func_8380 = relay.Function([], output)
mutated_mod['func_8380'] = func_8380
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8413 = relay.var("var_8413", dtype = "float32", shape = (13, 12, 6))#candidate|8413|(13, 12, 6)|var|float32
var_8414 = relay.var("var_8414", dtype = "float32", shape = (13, 12, 6))#candidate|8414|(13, 12, 6)|var|float32
bop_8415 = relay.subtract(var_8413.astype('float32'), relay.reshape(var_8414.astype('float32'), relay.shape_of(var_8413))) # shape=(13, 12, 6)
func_4280_call = mod.get_global_var('func_4280')
func_4282_call = mutated_mod.get_global_var('func_4282')
var_8444 = relay.var("var_8444", dtype = "float32", shape = (2, 28))#candidate|8444|(2, 28)|var|float32
call_8443 = relay.TupleGetItem(func_4280_call(relay.reshape(var_8444.astype('float32'), [4, 7, 2])), 1)
call_8445 = relay.TupleGetItem(func_4282_call(relay.reshape(var_8444.astype('float32'), [4, 7, 2])), 1)
uop_8452 = relay.tan(var_8413.astype('float32')) # shape=(13, 12, 6)
output = relay.Tuple([bop_8415,call_8443,var_8444,uop_8452,])
output2 = relay.Tuple([bop_8415,call_8445,var_8444,uop_8452,])
func_8462 = relay.Function([var_8413,var_8414,var_8444,], output)
mod['func_8462'] = func_8462
mod = relay.transform.InferType()(mod)
var_8463 = relay.var("var_8463", dtype = "float32", shape = (13, 12, 6))#candidate|8463|(13, 12, 6)|var|float32
var_8464 = relay.var("var_8464", dtype = "float32", shape = (13, 12, 6))#candidate|8464|(13, 12, 6)|var|float32
var_8465 = relay.var("var_8465", dtype = "float32", shape = (2, 28))#candidate|8465|(2, 28)|var|float32
output = func_8462(var_8463,var_8464,var_8465,)
func_8466 = relay.Function([var_8463,var_8464,var_8465,], output)
mutated_mod['func_8466'] = func_8466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2513_call = mod.get_global_var('func_2513')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_8504 = relay.TupleGetItem(func_2513_call(), 1)
call_8505 = relay.TupleGetItem(func_2515_call(), 1)
func_5204_call = mod.get_global_var('func_5204')
func_5208_call = mutated_mod.get_global_var('func_5208')
const_8515 = relay.const([[6.858656,-0.981373,0.612510,-5.403065,2.225787,8.203036,0.476560,8.641760,5.462979,4.211412,6.229908,-3.324277,-7.890863,4.650014,-4.327012,-2.273807,1.575201,-5.380889,-8.748428,1.546314,7.303176,-0.657709,9.226179,9.544206,-7.742803,-1.730219,8.845558,-4.766939,-5.916616,-9.144878,-8.037725,-8.387242,3.993614,2.951187,0.668262,0.493774,6.367644,-4.427376,3.875708,-2.551583,-5.078658,7.329733,6.322168,4.978068,-8.237910,-3.906352,-8.067026,-8.173414,0.578795,8.013216,-5.082642,3.825459,-6.261170,-4.251222,0.253473,3.121894,6.841004,7.135440,-3.122389,-6.746320,-6.359283,-2.265109,1.522508,-9.370500,-0.548667,-5.349269,-2.663766,-4.055388,0.050154,-3.730338,8.139514,-2.751228,7.478938,2.261562,-5.463653,-6.136863,-9.517522,5.209292,1.859951,-9.098029,-7.711825,-8.822862,-8.580420,0.407571,-7.042926,3.219030,-5.062093,-6.765395,0.464324,8.579076,-1.370961,6.045708,-4.344738,-6.923682,-7.113158,5.331297,2.263862,-3.760969,5.455050,2.966137,1.634194,5.292917,-8.972479,8.265110,-8.697965,7.427088,-6.693042,7.562524,-9.575620,-5.989523,1.338611,8.081779,-5.102147,-0.448651,0.702301,3.413690,-6.970512,-5.624710,-4.884363,9.692260,4.825048,6.045975,2.951358,-1.525982,2.786409,-7.331334,9.049355,6.437826,8.647940,3.708366,-9.101210,-0.703329,9.217024,9.573026,-2.369708,-3.207714,-7.661097,-2.238193,7.900715,9.318147,3.785754,3.362324,6.289943,-3.604129,-6.657388,6.055776,-5.678523,-0.960865,6.422217,-9.021759,-6.380269,6.087826,-3.436197,-8.739781,-7.075493,-5.535943,6.303224,-4.767215,9.400495,-9.188942,-9.912604,-6.008981,0.864244,8.527247,-4.261585,-1.476600,-0.232540,6.061226,6.745683,-1.687614,7.203799,-6.954888,-6.486223,7.346787,3.736097,-8.218786,-4.901486,3.332677,9.411596,-2.553167,-3.800979,-2.511296,-4.654084,4.482302,9.648577,7.175179,9.202692,1.718466,9.319162,7.897758,-2.590825,-2.731486,-2.746410,-6.855866,-1.944395,0.284317,-0.009964,-5.072929,-9.243570,-6.979204,5.065389,-7.223769,5.105852,5.848359,9.414822,-3.269741,-6.500666,-8.838600,-2.895072,-6.473607,1.628913,9.557803,9.772433,-6.372317,8.976902,9.702784,-3.932484,1.071584,2.884176,-6.189625,1.103066,4.298731,-3.172045,-7.243485,-7.826348,4.709615,0.967752,6.765658,-3.977443,-4.812537,5.180779,1.662891,3.902011,1.227826,5.376433,5.083264,-6.849159,-5.202160,-8.312488,7.141271,8.087868,-1.260798,5.018500,6.730500,0.623643,-9.925170,8.050689,8.659943,-3.601595,7.674835,-9.750153,8.895647,1.223259,2.206710,-2.987067,6.255266,-4.277721,-4.701586,9.986298,8.964763,3.684352,0.366338,5.219097,-4.129779,-1.232927,1.506890,-3.132960,6.427149,-3.992301,-1.986888,-5.954822,-9.099425,7.124102,-0.923511,-4.665863,-7.583011,7.981759,-6.969316,-9.963879,8.533641,8.717437,8.129110,9.586888,5.756765,-1.955980,-9.756252,6.484074,4.749581,-7.056206,-2.074687,4.899443,-8.216069,-1.786810,-1.737022,9.949778,4.370786,-0.247591,3.955201,-7.005691,-9.557709,-4.193674,6.374093,1.123761,-0.028402,-4.332693,7.659861,6.107316,8.525376,-1.466374,-0.794108,1.398804,-3.463939,8.949219,4.236840,8.968125,-5.661816,-8.845719,1.438952,-7.531410,5.305652,-5.094970,-1.656798,9.570538,-1.044406,2.793698,9.658213,-4.615285,8.466211,0.722133,0.925557,-6.883091,-3.710165,3.753253,-0.815245,-1.207885,6.762034,-8.362986,-5.733371,2.096603,-0.568807,-6.759088,8.378260,2.953585,-1.131538,5.755509,3.495582,9.836846,-4.599413,-9.958426,-4.099901,6.049783,0.015890,9.404298,4.133620,-0.461044,-7.595741,4.325530,-8.044819,-2.390287,-4.516129,-2.758858,2.608243,7.446803,6.128189,-9.770466,-2.810681,0.538032,-5.088160,-1.569264,5.036742,2.358235,9.200116,6.343174,0.252376,-8.539359,8.943104,-7.794149,-5.580423,-9.638012,5.717847,6.557945,-8.547508,2.645947,8.269081,-1.159714,9.228714,-8.627531,3.760825,-9.374228,3.223615,-6.147150,5.627354,8.036288,-5.599954,7.595769,4.560901,-5.994767,7.742069,-0.339069,8.091514,7.467008,-7.327333,8.780281,4.214280,-2.366345,-9.912031,6.946808,1.086145,4.488587,8.946605,0.043667,7.581962,-3.867606,-1.895874,7.347130,-0.744272,-9.988066,0.949204,-7.617088,6.359428,5.218719,3.020364,2.110507,-8.009227,-3.582191,-7.846198,-2.869510,7.494971,-7.538008,7.346868,2.800725,7.019072,-3.364076,5.509186,9.313172,5.689993,-0.799252,-9.908816,-2.418846,-3.487088,-0.143077,-9.862064,-9.800339,4.486766,1.504080,3.465216,-4.363389,-8.035368,9.824868,7.005154,-0.058373,4.914520,6.152898,6.440943,-7.403700,2.541463,-0.886460,7.537614,4.826475,4.818916,6.351945,-9.357327,9.249018,-9.370580,-8.715580,-8.712671,9.168015,-5.498458,7.851804,-0.523313,5.559002,-5.045375,2.106376,7.347480,-8.175543,-3.886580,9.634271,-3.044845,5.957691,9.126435,-2.337970,7.772682,5.539391,3.608769,2.344570,3.672945,9.522155,-1.130071,5.377440,3.928767,-2.709765,-8.781476,-0.228507,2.446401,3.388189,-1.411721,-8.749784,2.838099,8.933741,-8.129803,-8.432021,8.636572,8.244596,2.506796,7.331582,-7.141704,-8.887999,6.257351,0.057615,-1.908462,1.731380,6.270088,-8.008650,-8.082969,6.369389,-7.549993,-3.459722,2.735382,7.420537,-5.346884,1.964509,5.183905,9.852068,4.235711,4.544540,-6.617758,-1.062443,-1.341362,-5.071253,-9.914517,1.392452,-0.856510,-5.419075,5.150179,-4.108741,7.474639,-3.321189,4.329660,1.933036,0.135144,-2.373143,-3.732856,0.742445,-3.275620,7.170865,3.329133,8.575843,-3.040020,2.114369,-2.249746,3.493480,0.860885,-9.550588,-2.828189,8.346895,-2.663456,8.572896,-1.416001,5.516932,-8.601807,1.347165,6.414928,3.388254,0.697158,0.616577,-2.001254,5.200960,-7.442289,-5.970980,6.203728,-2.520534,-6.438767,-5.252152,-8.314129,0.230664,-2.724588,-5.229332,2.374028,3.875710,-4.589761,-8.713268,-0.768540,8.233358,6.418537,7.695216,8.032930,-8.507378,0.898543,4.982388,-0.001136,-4.577818,3.992819,-9.032281,3.735854,3.323674,-7.202150,-8.816892,4.158606,-8.593542,-1.058814,-2.387644,8.444747,9.116173,6.156534,8.481154,7.849462,7.976218,-4.237940,7.546980,4.140541,-1.899784,5.455312,-8.807531,-3.122644,7.803977,-1.558867,-7.608783,6.652134,-9.336209,-8.738806,-5.168725,-8.180185,0.120265,-6.402587,-6.841295,3.466005,2.198540,1.299877,-6.804388,-8.064339,-8.451700,9.307620,1.280459,-7.269218,0.221573,0.390298,-5.059262,9.541946,-8.100739,0.022457,-5.110893,2.052284,0.602138,1.087818,-3.429094,3.211901,2.334479,-0.455963,3.169060,-9.934736,1.930951,8.666142,7.294457,1.910724,-8.962281,-3.412945,-6.884734,-9.101599,4.731235,1.987047,-6.131372,-3.672501,7.187930,-1.782716,-7.926621,8.716608,-9.751056,7.396350,-4.327976,8.229149,0.633054,0.953963,-9.958899,6.696348,5.619104,2.243628,-3.424003,7.471614,-0.942799,-0.198295,8.052831,0.339715,-4.356854,8.177828,9.401982,7.102863,6.148310,-9.704690,4.075192,6.907889,-4.734380,-3.248325,-1.714010,-2.626125,4.650081,9.604623,7.038762,-4.441863,-1.383337,-4.083450]], dtype = "float32")#candidate|8515|(1, 700)|const|float32
var_8516 = relay.var("var_8516", dtype = "float32", shape = (78, 6))#candidate|8516|(78, 6)|var|float32
call_8514 = relay.TupleGetItem(func_5204_call(relay.reshape(const_8515.astype('float32'), [10, 10, 7]), relay.reshape(var_8516.astype('float32'), [468,]), ), 0)
call_8517 = relay.TupleGetItem(func_5208_call(relay.reshape(const_8515.astype('float32'), [10, 10, 7]), relay.reshape(var_8516.astype('float32'), [468,]), ), 0)
output = relay.Tuple([call_8504,call_8514,const_8515,var_8516,])
output2 = relay.Tuple([call_8505,call_8517,const_8515,var_8516,])
func_8527 = relay.Function([var_8516,], output)
mod['func_8527'] = func_8527
mod = relay.transform.InferType()(mod)
var_8528 = relay.var("var_8528", dtype = "float32", shape = (78, 6))#candidate|8528|(78, 6)|var|float32
output = func_8527(var_8528)
func_8529 = relay.Function([var_8528], output)
mutated_mod['func_8529'] = func_8529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_8542 = func_1620_call()
call_8543 = func_1620_call()
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_8555 = relay.TupleGetItem(func_2385_call(), 1)
call_8556 = relay.TupleGetItem(func_2387_call(), 1)
output = relay.Tuple([call_8542,call_8555,])
output2 = relay.Tuple([call_8543,call_8556,])
func_8571 = relay.Function([], output)
mod['func_8571'] = func_8571
mod = relay.transform.InferType()(mod)
output = func_8571()
func_8572 = relay.Function([], output)
mutated_mod['func_8572'] = func_8572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5064_call = mod.get_global_var('func_5064')
func_5065_call = mutated_mod.get_global_var('func_5065')
call_8674 = relay.TupleGetItem(func_5064_call(), 0)
call_8675 = relay.TupleGetItem(func_5065_call(), 0)
func_2441_call = mod.get_global_var('func_2441')
func_2443_call = mutated_mod.get_global_var('func_2443')
call_8687 = func_2441_call()
call_8688 = func_2441_call()
func_3231_call = mod.get_global_var('func_3231')
func_3235_call = mutated_mod.get_global_var('func_3235')
const_8699 = relay.const(-3.681716, dtype = "float32")#candidate|8699|()|const|float32
var_8700 = relay.var("var_8700", dtype = "float32", shape = (16, 2))#candidate|8700|(16, 2)|var|float32
call_8698 = relay.TupleGetItem(func_3231_call(relay.reshape(const_8699.astype('float32'), []), relay.reshape(var_8700.astype('float32'), [8, 1, 4]), ), 2)
call_8701 = relay.TupleGetItem(func_3235_call(relay.reshape(const_8699.astype('float32'), []), relay.reshape(var_8700.astype('float32'), [8, 1, 4]), ), 2)
output = relay.Tuple([call_8674,call_8687,call_8698,const_8699,var_8700,])
output2 = relay.Tuple([call_8675,call_8688,call_8701,const_8699,var_8700,])
func_8715 = relay.Function([var_8700,], output)
mod['func_8715'] = func_8715
mod = relay.transform.InferType()(mod)
var_8716 = relay.var("var_8716", dtype = "float32", shape = (16, 2))#candidate|8716|(16, 2)|var|float32
output = func_8715(var_8716)
func_8717 = relay.Function([var_8716], output)
mutated_mod['func_8717'] = func_8717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7245_call = mod.get_global_var('func_7245')
func_7246_call = mutated_mod.get_global_var('func_7246')
call_8728 = relay.TupleGetItem(func_7245_call(), 1)
call_8729 = relay.TupleGetItem(func_7246_call(), 1)
output = call_8728
output2 = call_8729
func_8739 = relay.Function([], output)
mod['func_8739'] = func_8739
mod = relay.transform.InferType()(mod)
output = func_8739()
func_8740 = relay.Function([], output)
mutated_mod['func_8740'] = func_8740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8326_call = mod.get_global_var('func_8326')
func_8327_call = mutated_mod.get_global_var('func_8327')
call_8754 = relay.TupleGetItem(func_8326_call(), 0)
call_8755 = relay.TupleGetItem(func_8327_call(), 0)
func_4009_call = mod.get_global_var('func_4009')
func_4011_call = mutated_mod.get_global_var('func_4011')
call_8771 = relay.TupleGetItem(func_4009_call(), 0)
call_8772 = relay.TupleGetItem(func_4011_call(), 0)
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_8801 = relay.TupleGetItem(func_377_call(), 1)
call_8802 = relay.TupleGetItem(func_379_call(), 1)
func_8109_call = mod.get_global_var('func_8109')
func_8113_call = mutated_mod.get_global_var('func_8113')
var_8806 = relay.var("var_8806", dtype = "int16", shape = (180,))#candidate|8806|(180,)|var|int16
call_8805 = func_8109_call(relay.reshape(var_8806.astype('int16'), [9, 2, 10]), relay.reshape(var_8806.astype('int16'), [9, 2, 10]), )
call_8807 = func_8109_call(relay.reshape(var_8806.astype('int16'), [9, 2, 10]), relay.reshape(var_8806.astype('int16'), [9, 2, 10]), )
uop_8810 = relay.asinh(call_8805.astype('float32')) # shape=(9, 2, 10)
uop_8812 = relay.asinh(call_8807.astype('float32')) # shape=(9, 2, 10)
bop_8823 = relay.bitwise_xor(uop_8810.astype('uint64'), relay.reshape(call_8805.astype('uint64'), relay.shape_of(uop_8810))) # shape=(9, 2, 10)
bop_8826 = relay.bitwise_xor(uop_8812.astype('uint64'), relay.reshape(call_8807.astype('uint64'), relay.shape_of(uop_8812))) # shape=(9, 2, 10)
output = relay.Tuple([call_8754,call_8771,call_8801,var_8806,bop_8823,])
output2 = relay.Tuple([call_8755,call_8772,call_8802,var_8806,bop_8826,])
func_8827 = relay.Function([var_8806,], output)
mod['func_8827'] = func_8827
mod = relay.transform.InferType()(mod)
mutated_mod['func_8827'] = func_8827
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8828 = relay.var("var_8828", dtype = "int16", shape = (180,))#candidate|8828|(180,)|var|int16
func_8827_call = mutated_mod.get_global_var('func_8827')
call_8829 = func_8827_call(var_8828)
output = call_8829
func_8830 = relay.Function([var_8828], output)
mutated_mod['func_8830'] = func_8830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1987_call = mod.get_global_var('func_1987')
func_1989_call = mutated_mod.get_global_var('func_1989')
call_8850 = relay.TupleGetItem(func_1987_call(), 0)
call_8851 = relay.TupleGetItem(func_1989_call(), 0)
output = call_8850
output2 = call_8851
func_8855 = relay.Function([], output)
mod['func_8855'] = func_8855
mod = relay.transform.InferType()(mod)
mutated_mod['func_8855'] = func_8855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8855_call = mutated_mod.get_global_var('func_8855')
call_8856 = func_8855_call()
output = call_8856
func_8857 = relay.Function([], output)
mutated_mod['func_8857'] = func_8857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5914_call = mod.get_global_var('func_5914')
func_5916_call = mutated_mod.get_global_var('func_5916')
call_8987 = relay.TupleGetItem(func_5914_call(), 2)
call_8988 = relay.TupleGetItem(func_5916_call(), 2)
func_4579_call = mod.get_global_var('func_4579')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_8993 = func_4579_call()
call_8994 = func_4579_call()
output = relay.Tuple([call_8987,call_8993,])
output2 = relay.Tuple([call_8988,call_8994,])
func_9015 = relay.Function([], output)
mod['func_9015'] = func_9015
mod = relay.transform.InferType()(mod)
mutated_mod['func_9015'] = func_9015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9015_call = mutated_mod.get_global_var('func_9015')
call_9016 = func_9015_call()
output = call_9016
func_9017 = relay.Function([], output)
mutated_mod['func_9017'] = func_9017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1570_call = mod.get_global_var('func_1570')
func_1571_call = mutated_mod.get_global_var('func_1571')
call_9048 = relay.TupleGetItem(func_1570_call(), 0)
call_9049 = relay.TupleGetItem(func_1571_call(), 0)
output = relay.Tuple([call_9048,])
output2 = relay.Tuple([call_9049,])
func_9062 = relay.Function([], output)
mod['func_9062'] = func_9062
mod = relay.transform.InferType()(mod)
mutated_mod['func_9062'] = func_9062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9062_call = mutated_mod.get_global_var('func_9062')
call_9063 = func_9062_call()
output = call_9063
func_9064 = relay.Function([], output)
mutated_mod['func_9064'] = func_9064
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9070 = relay.const([[[3,-8,4,1,-10,-10],[-9,-3,7,-7,6,-6],[-7,5,-4,-8,2,10],[-7,3,-6,-8,8,-9],[3,-6,8,-9,4,3],[-3,-7,-8,9,1,-3],[-7,-1,-4,9,-6,8],[7,-1,1,1,4,7],[8,-9,1,6,-3,-2],[7,4,-6,-1,10,-6],[-5,-5,6,3,9,4]],[[4,-8,7,5,1,9],[-4,2,2,4,-4,8],[-10,-7,5,-9,-1,7],[8,2,-3,-9,-3,10],[-9,-3,-5,5,4,-4],[-3,-9,3,10,7,-1],[5,9,2,-3,4,-4],[-9,-4,-2,3,5,-2],[7,8,-6,-6,2,6],[5,-5,-5,9,9,-8],[-4,-8,10,-7,-2,3]],[[-5,-8,4,-1,3,-9],[-6,-2,-4,7,1,6],[7,-10,-10,8,2,2],[-10,-7,10,1,6,10],[6,-7,5,10,-9,-5],[-1,-4,-9,-9,1,1],[-1,7,10,5,-5,4],[-8,-5,3,5,3,7],[6,-10,-9,8,5,-7],[-3,2,-5,-1,9,9],[6,-7,3,-2,9,8]],[[4,10,-3,6,-9,5],[7,8,-4,9,3,2],[8,-5,-5,-7,-10,10],[-3,-1,-9,6,-4,1],[3,1,-3,-2,-4,-10],[-3,-2,3,6,10,-6],[-6,4,-1,10,-4,10],[2,10,2,-9,-6,-7],[2,-5,-1,-3,5,6],[2,-10,7,-4,5,-6],[-4,1,5,1,1,10]],[[-8,10,-8,-1,-4,-7],[-4,-3,4,7,4,10],[-6,-7,-8,3,-7,3],[-1,6,-5,10,1,-10],[3,-3,-5,-6,-5,-10],[-9,-2,5,-2,8,-4],[10,-4,-7,5,2,-7],[-2,-8,8,-3,10,-3],[-1,-3,-2,5,3,2],[4,10,-9,2,1,-10],[7,-8,-1,4,-6,10]],[[-6,-2,4,10,5,-5],[8,6,7,-10,1,1],[-1,-3,-2,6,10,6],[4,-6,-6,1,-10,5],[5,4,-5,10,-10,2],[-8,9,-8,3,-2,1],[2,2,-1,9,-2,3],[-8,3,6,9,6,3],[2,6,-7,-2,8,-10],[2,-6,4,4,-2,9],[2,3,7,-4,6,-5]],[[-8,1,-2,7,-4,-2],[10,-10,5,-10,1,-7],[-1,-7,10,1,8,5],[5,-8,3,-7,8,-5],[1,9,1,8,6,1],[7,5,-4,-9,-10,-9],[-9,-6,-4,-9,8,-6],[-6,1,10,-8,-3,-6],[3,7,-4,-6,1,-1],[5,-1,-10,2,-1,-7],[-4,-10,10,-6,-3,6]],[[-7,4,8,-6,-7,-6],[4,-4,2,8,8,4],[5,-1,-1,10,1,10],[9,-2,5,-7,7,-5],[-3,-4,-10,9,8,-8],[4,9,-1,-5,-6,-1],[5,9,-9,3,-7,3],[7,5,-1,-4,-10,-2],[-3,3,4,-10,2,-2],[-4,-3,4,-10,-9,4],[-7,-6,-3,-8,-3,-6]],[[5,-7,5,-5,6,2],[7,9,-7,5,5,-9],[-10,-7,-7,2,-10,8],[8,-6,3,-4,-2,-6],[8,-2,-5,-1,9,-9],[-10,-10,-8,8,4,-2],[-4,7,9,-6,9,10],[-9,10,-1,-6,-8,3],[-7,-5,5,-7,-4,-6],[2,-10,7,6,2,-8],[4,4,-2,-1,-8,-7]],[[-4,1,-9,-10,6,-1],[-1,3,-2,8,4,-10],[-1,-5,-5,-1,7,6],[-8,6,-8,10,-5,-7],[-1,4,9,4,-5,8],[-1,1,-10,5,-7,3],[-9,7,6,-2,-8,-4],[10,-6,5,9,2,4],[-10,1,10,-1,9,-3],[-1,-3,1,8,5,10],[-8,6,8,-6,-10,4]],[[-5,9,4,-10,-8,7],[-10,3,-9,-5,-10,8],[2,-8,3,2,-10,3],[-4,-10,5,2,-2,-1],[7,-7,9,-9,-1,5],[1,-3,8,-5,-8,7],[-4,-9,5,7,-5,1],[2,-7,6,-9,9,8],[-10,4,-1,9,1,4],[-7,-9,5,-8,-1,2],[-9,6,4,9,-8,10]]], dtype = "uint16")#candidate|9070|(11, 11, 6)|const|uint16
const_9071 = relay.const([[[10,5,8,5,-2,-6],[8,7,4,1,-2,9],[10,-6,-2,-6,10,10],[-5,-8,6,2,-5,7],[-4,3,1,-3,2,3],[2,-6,3,10,5,-5],[-9,-4,-5,-2,-9,2],[7,-1,3,-4,-5,9],[8,-8,-5,-1,-1,9],[-6,-4,7,5,3,4],[-9,-3,9,-2,1,-10]],[[-4,-3,6,10,6,-8],[-2,-9,-10,1,3,6],[7,-9,-10,7,9,-9],[-5,-8,-3,-5,3,9],[9,5,-5,-2,-10,1],[9,4,-1,5,-1,8],[-3,-8,7,2,-7,-5],[-9,-5,1,9,-7,10],[-3,3,-9,-8,3,9],[-3,-5,-7,3,1,-4],[-5,2,3,9,6,10]],[[4,-8,-3,-7,7,9],[6,9,-9,10,8,-7],[6,7,-9,-7,-6,-7],[1,7,10,1,7,5],[-5,-3,1,-3,5,8],[10,6,10,7,9,-9],[-4,-7,4,-9,9,1],[-2,-6,8,-3,-9,6],[-2,3,1,-2,-6,-5],[3,9,-8,1,-9,-8],[-2,5,10,3,6,-3]],[[1,9,-4,-6,-8,8],[-7,5,9,3,4,1],[9,6,-1,10,4,-7],[-4,7,10,-6,-8,3],[6,-7,1,-6,3,8],[1,-5,-9,-7,-9,-5],[-2,6,-3,5,2,-2],[9,7,-10,-7,-5,7],[-7,9,7,-5,-6,-8],[9,-10,5,-7,-10,10],[1,10,-10,-10,-1,2]],[[-2,6,-9,8,-8,-10],[10,1,4,-1,-7,-1],[-8,-5,-9,-7,-6,-8],[9,-5,-4,-4,-4,8],[4,-3,8,9,4,-7],[3,-1,-8,3,6,-8],[5,-7,-7,-7,2,-2],[-5,-10,-5,9,8,-6],[-10,6,9,8,-6,-2],[-10,3,-10,-4,-8,-3],[9,2,3,-8,8,-1]],[[-7,-10,-4,7,-3,5],[5,-10,2,-5,-7,-2],[6,-5,3,-1,5,-5],[-6,-2,-3,6,-4,1],[4,-1,-5,-1,-1,3],[-4,-4,8,9,-4,-6],[-6,2,-3,-8,-1,7],[-1,4,7,-6,6,2],[-1,-9,-10,1,9,7],[-6,-8,3,-2,-4,-8],[8,1,-6,-7,4,4]],[[-2,1,8,-5,3,3],[9,-2,-6,5,4,7],[1,-9,-1,-8,-7,6],[6,-2,-5,5,-2,8],[-9,1,10,-5,1,5],[-8,5,-1,3,-10,-4],[-1,10,10,-1,-2,-4],[10,3,-5,5,1,-1],[9,-10,10,-8,5,-4],[8,5,10,2,1,3],[-4,-1,6,-9,-7,-8]],[[3,10,3,-4,-1,-1],[-10,-1,8,9,2,-1],[4,-7,-9,10,10,1],[-5,-6,-5,7,10,8],[-4,4,-7,-8,4,-1],[-2,-6,-4,8,3,-4],[-1,-6,1,-8,1,2],[-6,-6,-4,3,2,10],[6,5,-2,-2,2,-3],[-3,7,-3,-9,-7,-9],[-4,9,-2,1,-7,-1]],[[-7,-3,10,1,4,-5],[-7,6,-1,-9,7,-2],[8,-9,2,-5,3,-6],[-3,8,7,6,10,-1],[9,6,9,5,1,-4],[5,10,7,-3,-6,-10],[4,8,8,-5,-7,-2],[-8,4,2,2,7,-7],[9,7,-1,-8,-2,1],[6,-6,-6,1,-7,5],[5,7,9,-8,-4,-6]],[[1,9,2,3,5,-3],[10,-9,1,4,-1,-7],[7,-1,-10,7,4,-5],[6,-6,-9,-6,-5,4],[8,1,3,10,-5,10],[-1,-9,4,1,3,-3],[-6,-1,-3,-6,-5,10],[7,7,-2,-9,5,-6],[-3,-9,4,-1,4,-1],[9,7,6,-1,7,7],[6,-10,4,-9,5,-5]],[[3,-9,-10,-1,-10,4],[-8,-1,4,4,-3,-10],[-2,-6,-9,4,-9,-7],[5,-1,-8,1,9,-3],[-1,4,1,5,-2,-10],[3,3,1,4,-9,1],[7,5,5,2,5,1],[9,1,6,4,-9,1],[8,6,-8,7,6,-5],[2,-8,-3,-2,3,-4],[7,8,5,-6,7,-2]]], dtype = "uint16")#candidate|9071|(11, 11, 6)|const|uint16
bop_9072 = relay.bitwise_or(const_9070.astype('uint16'), relay.reshape(const_9071.astype('uint16'), relay.shape_of(const_9070))) # shape=(11, 11, 6)
func_5017_call = mod.get_global_var('func_5017')
func_5019_call = mutated_mod.get_global_var('func_5019')
call_9075 = relay.TupleGetItem(func_5017_call(), 1)
call_9076 = relay.TupleGetItem(func_5019_call(), 1)
output = relay.Tuple([bop_9072,call_9075,])
output2 = relay.Tuple([bop_9072,call_9076,])
func_9079 = relay.Function([], output)
mod['func_9079'] = func_9079
mod = relay.transform.InferType()(mod)
output = func_9079()
func_9080 = relay.Function([], output)
mutated_mod['func_9080'] = func_9080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_9173 = relay.TupleGetItem(func_776_call(), 0)
call_9174 = relay.TupleGetItem(func_778_call(), 0)
func_2732_call = mod.get_global_var('func_2732')
func_2733_call = mutated_mod.get_global_var('func_2733')
call_9191 = relay.TupleGetItem(func_2732_call(), 0)
call_9192 = relay.TupleGetItem(func_2733_call(), 0)
func_273_call = mod.get_global_var('func_273')
func_275_call = mutated_mod.get_global_var('func_275')
call_9218 = relay.TupleGetItem(func_273_call(), 1)
call_9219 = relay.TupleGetItem(func_275_call(), 1)
func_4698_call = mod.get_global_var('func_4698')
func_4702_call = mutated_mod.get_global_var('func_4702')
var_9224 = relay.var("var_9224", dtype = "int8", shape = (198,))#candidate|9224|(198,)|var|int8
call_9223 = func_4698_call(relay.reshape(var_9224.astype('int8'), [2, 11, 9]), relay.reshape(var_9224.astype('int8'), [2, 11, 9]), )
call_9225 = func_4698_call(relay.reshape(var_9224.astype('int8'), [2, 11, 9]), relay.reshape(var_9224.astype('int8'), [2, 11, 9]), )
uop_9231 = relay.acos(call_9223.astype('float32')) # shape=(2, 11, 9)
uop_9233 = relay.acos(call_9225.astype('float32')) # shape=(2, 11, 9)
func_7733_call = mod.get_global_var('func_7733')
func_7735_call = mutated_mod.get_global_var('func_7735')
call_9236 = relay.TupleGetItem(func_7733_call(), 0)
call_9237 = relay.TupleGetItem(func_7735_call(), 0)
output = relay.Tuple([call_9173,call_9191,call_9218,var_9224,uop_9231,call_9236,])
output2 = relay.Tuple([call_9174,call_9192,call_9219,var_9224,uop_9233,call_9237,])
func_9241 = relay.Function([var_9224,], output)
mod['func_9241'] = func_9241
mod = relay.transform.InferType()(mod)
mutated_mod['func_9241'] = func_9241
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9242 = relay.var("var_9242", dtype = "int8", shape = (198,))#candidate|9242|(198,)|var|int8
func_9241_call = mutated_mod.get_global_var('func_9241')
call_9243 = func_9241_call(var_9242)
output = call_9243
func_9244 = relay.Function([var_9242], output)
mutated_mod['func_9244'] = func_9244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4009_call = mod.get_global_var('func_4009')
func_4011_call = mutated_mod.get_global_var('func_4011')
call_9277 = relay.TupleGetItem(func_4009_call(), 0)
call_9278 = relay.TupleGetItem(func_4011_call(), 0)
func_7302_call = mod.get_global_var('func_7302')
func_7303_call = mutated_mod.get_global_var('func_7303')
call_9289 = func_7302_call()
call_9290 = func_7302_call()
func_377_call = mod.get_global_var('func_377')
func_379_call = mutated_mod.get_global_var('func_379')
call_9291 = relay.TupleGetItem(func_377_call(), 1)
call_9292 = relay.TupleGetItem(func_379_call(), 1)
uop_9297 = relay.log(call_9291.astype('float32')) # shape=(8, 7, 3)
uop_9299 = relay.log(call_9292.astype('float32')) # shape=(8, 7, 3)
func_4579_call = mod.get_global_var('func_4579')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_9303 = func_4579_call()
call_9304 = func_4579_call()
func_7550_call = mod.get_global_var('func_7550')
func_7552_call = mutated_mod.get_global_var('func_7552')
call_9308 = relay.TupleGetItem(func_7550_call(), 0)
call_9309 = relay.TupleGetItem(func_7552_call(), 0)
func_6692_call = mod.get_global_var('func_6692')
func_6694_call = mutated_mod.get_global_var('func_6694')
call_9317 = relay.TupleGetItem(func_6692_call(), 3)
call_9318 = relay.TupleGetItem(func_6694_call(), 3)
func_7820_call = mod.get_global_var('func_7820')
func_7821_call = mutated_mod.get_global_var('func_7821')
call_9322 = relay.TupleGetItem(func_7820_call(), 0)
call_9323 = relay.TupleGetItem(func_7821_call(), 0)
func_7910_call = mod.get_global_var('func_7910')
func_7912_call = mutated_mod.get_global_var('func_7912')
const_9326 = relay.const([[-0.084447,8.118668],[6.637700,-0.834451],[9.404074,6.412630],[-1.328382,2.624226],[-2.570598,8.792222],[5.719748,-8.647542],[6.388302,-5.763507],[-0.108385,-7.634173],[7.948426,3.014266],[5.069940,1.205973],[-8.188151,-9.036847],[-1.724740,8.666836],[0.403419,-3.422081],[8.691001,9.169715],[-6.861862,-9.697262],[9.921236,1.915696],[9.685898,7.730813],[4.679741,7.086785],[-1.723214,-3.491571],[-7.481622,6.970865],[-0.395057,-0.190403],[-8.735282,-7.627569],[4.743901,7.422061],[6.443994,6.234584],[-0.267089,6.485380],[6.611610,3.865562],[2.285587,4.572682],[4.638720,9.693945],[-7.574843,9.466801],[9.549786,8.343865],[6.845133,-8.150210],[6.739478,3.407898],[-3.218196,0.869654],[7.162596,5.609226],[-9.706269,-1.602313],[5.659961,-1.307295],[4.542132,-1.182265],[7.282193,5.741124],[9.000289,-0.110129],[-1.186796,-7.374206],[-5.820037,-6.848833],[-9.230968,-7.568830],[-3.007529,5.267660],[3.319192,5.535783],[7.423757,7.288590],[8.525073,9.043916],[-1.488427,-4.410145],[8.697313,-1.467325],[-8.635908,-1.773205],[-3.176442,-2.268508],[7.140106,1.998212],[8.162788,-7.199958],[-7.179661,3.407374],[-4.991730,-3.958930],[-3.319830,0.576573],[8.958643,-5.473358],[7.502709,8.698523],[7.930382,-0.223872],[1.360930,8.374426],[7.338009,3.700172],[-2.015584,7.455938],[-4.328196,0.560240],[-0.633832,-9.181472],[-8.459935,-9.189987],[0.057477,-3.176721],[9.348911,-4.091866],[-4.943012,5.050762],[8.567603,1.274666],[3.631096,-8.009888],[5.173688,7.323054],[3.955491,9.197814],[-6.554026,4.480849],[4.033672,-2.159747],[-2.544817,5.829191],[1.931795,-9.046532],[-5.453956,-2.723892],[1.777404,5.485367],[-8.152330,-9.950463],[-1.500219,-2.739943],[1.345511,8.970283],[0.406929,1.619700],[-9.361589,-3.303401],[9.122534,-1.900931],[-9.794519,-2.733727],[7.991150,-2.346243],[-1.165324,1.048571],[3.777815,1.350933],[8.464709,1.848616],[-3.333929,8.030512],[-1.323633,-5.873884],[-3.139374,7.833935],[6.021944,-6.651504],[7.576991,1.088713],[-8.042199,-4.930628],[-2.756776,-0.773823],[-6.729657,-6.275729],[7.717179,6.211126],[2.077080,7.348042],[-3.966614,-7.949483],[-5.025129,2.987788],[-9.062566,8.019634],[1.834461,-7.711059],[6.159044,-3.599150],[-6.377708,8.735794],[-3.809930,8.812200],[-4.333500,7.096283],[5.183137,9.599250],[6.474398,8.343856],[4.487028,-6.231466],[7.645222,-9.897588],[4.030508,-0.122736],[7.179894,8.875869],[4.230386,2.844343],[-1.947635,-9.739172],[-9.815786,6.430990],[-2.486884,2.485229],[-1.545245,5.395784],[-1.394897,-1.647295],[-1.712587,-0.758451],[-9.665669,8.119497],[-8.148849,-9.953690],[7.021337,2.062675],[-7.095190,7.527569],[1.743823,-9.567420],[-8.591303,4.210078],[3.428980,4.442939],[8.278375,0.886551],[4.433229,4.194126],[1.375893,-0.790761],[-7.122337,-7.925304],[1.462031,-3.904798],[1.651582,-9.397436],[-4.048804,-5.614235],[1.551031,5.517547],[4.296875,2.705855],[2.035394,6.043602],[-2.645614,9.490430],[1.496198,9.206082],[-6.850543,3.556477],[-1.480102,5.850945],[-0.983617,-6.494948],[8.648252,-1.265668],[-5.770989,-4.666393],[-9.310382,-8.249034],[6.732766,9.759847],[4.826498,7.720030],[-2.092673,7.272428],[-6.681783,2.854130],[2.431273,0.256210],[7.333050,4.149918],[7.061426,0.486543],[8.218575,-1.758303],[-9.753806,9.679748],[-1.060179,4.215715],[-4.789775,5.970982],[4.173497,1.982306],[-9.433327,-5.868284],[-2.154101,3.714273],[0.366100,2.032333],[-7.640365,0.314338],[8.693152,-7.164933],[-7.214925,0.012127],[0.385207,3.111597],[0.361388,1.564991],[8.716720,-5.986715],[9.722223,2.398163],[-1.783934,-0.822446],[-7.922716,1.714676],[-7.036123,6.794842],[7.187262,8.986975],[3.663567,-0.958711],[1.904600,-1.606192],[2.825375,-8.804399],[-7.071897,9.347385],[-2.813729,4.690985],[2.011569,5.665451],[6.157405,-5.859633],[2.014037,7.954877],[1.824676,0.818538],[3.298722,4.501484],[-8.077332,1.744935],[-0.999880,-1.053530],[-7.333127,5.445926],[-9.021888,-3.964542],[-8.026136,1.367640],[-3.266575,-7.101692],[-4.592365,0.511352],[-9.124863,-4.471311],[-7.643089,2.318256],[-5.359278,-6.042254],[-8.819900,-7.761653],[-4.142941,-3.556172],[-7.271014,-9.432689],[-3.052984,-8.763261],[-7.108130,-4.262021],[-5.166282,-3.195009],[-0.099365,9.862528],[9.272557,-0.462206],[-2.017409,-8.649523],[6.685841,2.739275],[-1.327473,-9.554369],[-8.118851,6.254626],[-0.023055,4.558024],[-6.804449,-1.164430],[-8.659482,2.485183],[4.263228,1.030373],[3.122074,-3.788437],[-3.023265,-3.476727],[1.334305,9.193771],[8.529882,-3.427727],[-5.106566,-9.188526],[7.296238,7.788485],[9.990391,7.009413],[-2.109973,-5.885532],[6.304802,-5.277686],[-8.626032,-7.479731],[-6.052881,4.790935],[4.764584,3.350853],[-9.017748,-1.113403],[-4.624611,6.971626],[8.583905,-9.318173],[7.227427,7.299024],[2.245531,-7.342862],[-6.355499,3.705984],[-6.272681,-1.130033],[6.552790,7.283476],[0.160794,3.804345],[4.149159,4.889031],[-1.304529,4.368990],[-8.621224,-2.487113],[-1.158657,9.836755],[8.350412,1.460947],[-1.908737,3.830267],[-3.354683,5.591311],[3.798480,1.889643],[2.179788,3.082512],[4.842722,9.000717],[8.066173,4.499439],[-5.992050,-5.325778],[-5.473231,1.290523],[6.684156,-8.038364],[2.491221,2.569250],[-7.420023,5.926148],[-7.368270,2.848717],[8.020246,4.712244],[-7.219921,0.407618],[-5.121358,8.760164],[5.600221,9.622298],[8.051651,-3.768444],[8.668672,4.707700],[3.980417,4.091666],[7.740653,9.559148],[4.109994,2.024171],[8.330480,-8.410676],[-4.909686,-4.938230],[-8.289501,-0.504286],[8.397113,-9.737676],[1.248007,7.713156],[-4.385587,-3.574806],[4.315290,0.740340],[-1.140721,9.476751],[6.628446,4.606786],[5.234825,2.843663],[7.270830,5.577601],[1.612644,0.771166],[-8.643492,6.022668],[2.309769,-6.294886],[0.380739,6.503759],[3.505513,7.402542],[-5.873532,-8.616397],[0.160275,0.710882],[-3.774459,2.477835],[-8.649669,-6.097573],[2.070411,-0.477870],[9.019537,-0.837084],[-8.605455,-8.340606],[-5.589375,-6.832442],[7.039744,-3.115139],[-0.388944,7.918084],[-3.156466,-5.646652],[-8.119534,8.905444],[-1.479726,-8.170723],[6.673025,-8.301849],[2.837818,7.523453],[4.796316,-5.828826],[-5.335123,9.980455],[1.873417,1.381795],[2.002593,-1.347579],[-3.381866,-7.682785],[7.908423,-2.745802],[5.761447,-8.912240],[-1.776685,-0.787344],[2.546097,-8.774601],[1.525466,5.383659],[-0.877898,-5.296238],[-6.878385,0.559317],[4.143801,-8.858629],[3.843677,0.254408],[2.358102,7.623051],[1.976790,3.448522],[-6.025974,-7.623887],[6.109919,-5.210252],[7.050320,-5.841567],[-1.175774,-9.740296],[9.419162,-2.083979],[-2.366215,8.455765],[-3.210440,9.753940],[-8.960928,-8.292285]], dtype = "float32")#candidate|9326|(308, 2)|const|float32
call_9325 = relay.TupleGetItem(func_7910_call(relay.reshape(const_9326.astype('float32'), [616,])), 3)
call_9327 = relay.TupleGetItem(func_7912_call(relay.reshape(const_9326.astype('float32'), [616,])), 3)
output = relay.Tuple([call_9277,call_9289,uop_9297,call_9303,call_9308,call_9317,call_9322,call_9325,const_9326,])
output2 = relay.Tuple([call_9278,call_9290,uop_9299,call_9304,call_9309,call_9318,call_9323,call_9327,const_9326,])
func_9331 = relay.Function([], output)
mod['func_9331'] = func_9331
mod = relay.transform.InferType()(mod)
mutated_mod['func_9331'] = func_9331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9331_call = mutated_mod.get_global_var('func_9331')
call_9332 = func_9331_call()
output = call_9332
func_9333 = relay.Function([], output)
mutated_mod['func_9333'] = func_9333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9366 = relay.var("var_9366", dtype = "uint16", shape = ())#candidate|9366|()|var|uint16
var_9367 = relay.var("var_9367", dtype = "uint16", shape = (5, 1, 9))#candidate|9367|(5, 1, 9)|var|uint16
bop_9368 = relay.bitwise_xor(var_9366.astype('uint16'), var_9367.astype('uint16')) # shape=(5, 1, 9)
uop_9389 = relay.sinh(var_9367.astype('float32')) # shape=(5, 1, 9)
func_4280_call = mod.get_global_var('func_4280')
func_4282_call = mutated_mod.get_global_var('func_4282')
const_9392 = relay.const([[3.556273,0.857811,-1.386317,-8.998044,-6.633558,1.242228,3.502851,-9.650407,-2.874571,8.726342,9.559227,1.231256,7.681489,-2.181224,-9.626282,8.000376,5.214474,-6.762852,0.555080,9.659027,9.127105,-9.510262,9.799263,-6.809863,9.952669,1.690626,9.668917,3.170949,9.059540,1.947296,8.946957,6.210619,0.492691,-1.678512,-3.970195,-2.635725,-9.128360,-7.301730,-1.994897,5.450948,-8.785832,-3.523195,-5.640793,1.572767,8.725891,8.056966,9.693067,6.023250,4.072131,8.902265,8.303299,8.974812,-6.764797,-1.546501,-2.903701,1.209487]], dtype = "float32")#candidate|9392|(1, 56)|const|float32
call_9391 = relay.TupleGetItem(func_4280_call(relay.reshape(const_9392.astype('float32'), [4, 7, 2])), 0)
call_9393 = relay.TupleGetItem(func_4282_call(relay.reshape(const_9392.astype('float32'), [4, 7, 2])), 0)
func_2786_call = mod.get_global_var('func_2786')
func_2787_call = mutated_mod.get_global_var('func_2787')
call_9395 = relay.TupleGetItem(func_2786_call(), 2)
call_9396 = relay.TupleGetItem(func_2787_call(), 2)
uop_9405 = relay.tan(uop_9389.astype('float32')) # shape=(5, 1, 9)
func_621_call = mod.get_global_var('func_621')
func_622_call = mutated_mod.get_global_var('func_622')
call_9414 = relay.TupleGetItem(func_621_call(), 1)
call_9415 = relay.TupleGetItem(func_622_call(), 1)
func_4280_call = mod.get_global_var('func_4280')
func_4282_call = mutated_mod.get_global_var('func_4282')
call_9419 = relay.TupleGetItem(func_4280_call(relay.reshape(call_9391.astype('float32'), [4, 7, 2])), 1)
call_9420 = relay.TupleGetItem(func_4282_call(relay.reshape(call_9391.astype('float32'), [4, 7, 2])), 1)
func_4570_call = mod.get_global_var('func_4570')
func_4571_call = mutated_mod.get_global_var('func_4571')
call_9426 = relay.TupleGetItem(func_4570_call(), 0)
call_9427 = relay.TupleGetItem(func_4571_call(), 0)
bop_9435 = relay.logical_and(uop_9405.astype('bool'), relay.reshape(bop_9368.astype('bool'), relay.shape_of(uop_9405))) # shape=(5, 1, 9)
output = relay.Tuple([call_9391,const_9392,call_9395,call_9414,call_9419,call_9426,bop_9435,])
output2 = relay.Tuple([call_9393,const_9392,call_9396,call_9415,call_9420,call_9427,bop_9435,])
func_9441 = relay.Function([var_9366,var_9367,], output)
mod['func_9441'] = func_9441
mod = relay.transform.InferType()(mod)
mutated_mod['func_9441'] = func_9441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9441_call = mutated_mod.get_global_var('func_9441')
var_9443 = relay.var("var_9443", dtype = "uint16", shape = ())#candidate|9443|()|var|uint16
var_9444 = relay.var("var_9444", dtype = "uint16", shape = (5, 1, 9))#candidate|9444|(5, 1, 9)|var|uint16
call_9442 = func_9441_call(var_9443,var_9444,)
output = call_9442
func_9445 = relay.Function([var_9443,var_9444,], output)
mutated_mod['func_9445'] = func_9445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2074_call = mutated_mod.get_global_var('func_2074')
call_9450 = func_2072_call()
call_9451 = func_2072_call()
func_5030_call = mod.get_global_var('func_5030')
func_5031_call = mutated_mod.get_global_var('func_5031')
call_9467 = relay.TupleGetItem(func_5030_call(), 0)
call_9468 = relay.TupleGetItem(func_5031_call(), 0)
func_3579_call = mod.get_global_var('func_3579')
func_3580_call = mutated_mod.get_global_var('func_3580')
call_9480 = relay.TupleGetItem(func_3579_call(), 0)
call_9481 = relay.TupleGetItem(func_3580_call(), 0)
output = relay.Tuple([call_9450,call_9467,call_9480,])
output2 = relay.Tuple([call_9451,call_9468,call_9481,])
func_9496 = relay.Function([], output)
mod['func_9496'] = func_9496
mod = relay.transform.InferType()(mod)
output = func_9496()
func_9497 = relay.Function([], output)
mutated_mod['func_9497'] = func_9497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_621_call = mod.get_global_var('func_621')
func_622_call = mutated_mod.get_global_var('func_622')
call_9527 = relay.TupleGetItem(func_621_call(), 1)
call_9528 = relay.TupleGetItem(func_622_call(), 1)
func_8739_call = mod.get_global_var('func_8739')
func_8740_call = mutated_mod.get_global_var('func_8740')
call_9564 = func_8739_call()
call_9565 = func_8739_call()
func_4969_call = mod.get_global_var('func_4969')
func_4970_call = mutated_mod.get_global_var('func_4970')
call_9567 = relay.TupleGetItem(func_4969_call(), 0)
call_9568 = relay.TupleGetItem(func_4970_call(), 0)
func_5334_call = mod.get_global_var('func_5334')
func_5337_call = mutated_mod.get_global_var('func_5337')
const_9576 = relay.const(3, dtype = "uint32")#candidate|9576|()|const|uint32
call_9575 = relay.TupleGetItem(func_5334_call(relay.reshape(const_9576.astype('uint32'), [])), 2)
call_9577 = relay.TupleGetItem(func_5337_call(relay.reshape(const_9576.astype('uint32'), [])), 2)
output = relay.Tuple([call_9527,call_9564,call_9567,call_9575,const_9576,])
output2 = relay.Tuple([call_9528,call_9565,call_9568,call_9577,const_9576,])
func_9588 = relay.Function([], output)
mod['func_9588'] = func_9588
mod = relay.transform.InferType()(mod)
mutated_mod['func_9588'] = func_9588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9588_call = mutated_mod.get_global_var('func_9588')
call_9589 = func_9588_call()
output = call_9589
func_9590 = relay.Function([], output)
mutated_mod['func_9590'] = func_9590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8855_call = mod.get_global_var('func_8855')
func_8857_call = mutated_mod.get_global_var('func_8857')
call_9612 = func_8855_call()
call_9613 = func_8855_call()
output = relay.Tuple([call_9612,])
output2 = relay.Tuple([call_9613,])
func_9615 = relay.Function([], output)
mod['func_9615'] = func_9615
mod = relay.transform.InferType()(mod)
mutated_mod['func_9615'] = func_9615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9615_call = mutated_mod.get_global_var('func_9615')
call_9616 = func_9615_call()
output = call_9616
func_9617 = relay.Function([], output)
mutated_mod['func_9617'] = func_9617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_776_call = mod.get_global_var('func_776')
func_778_call = mutated_mod.get_global_var('func_778')
call_9618 = relay.TupleGetItem(func_776_call(), 0)
call_9619 = relay.TupleGetItem(func_778_call(), 0)
output = relay.Tuple([call_9618,])
output2 = relay.Tuple([call_9619,])
func_9643 = relay.Function([], output)
mod['func_9643'] = func_9643
mod = relay.transform.InferType()(mod)
mutated_mod['func_9643'] = func_9643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9643_call = mutated_mod.get_global_var('func_9643')
call_9644 = func_9643_call()
output = call_9644
func_9645 = relay.Function([], output)
mutated_mod['func_9645'] = func_9645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4570_call = mod.get_global_var('func_4570')
func_4571_call = mutated_mod.get_global_var('func_4571')
call_9666 = relay.TupleGetItem(func_4570_call(), 0)
call_9667 = relay.TupleGetItem(func_4571_call(), 0)
output = relay.Tuple([call_9666,])
output2 = relay.Tuple([call_9667,])
func_9668 = relay.Function([], output)
mod['func_9668'] = func_9668
mod = relay.transform.InferType()(mod)
mutated_mod['func_9668'] = func_9668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9668_call = mutated_mod.get_global_var('func_9668')
call_9669 = func_9668_call()
output = call_9669
func_9670 = relay.Function([], output)
mutated_mod['func_9670'] = func_9670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8041_call = mod.get_global_var('func_8041')
func_8042_call = mutated_mod.get_global_var('func_8042')
call_9702 = relay.TupleGetItem(func_8041_call(), 1)
call_9703 = relay.TupleGetItem(func_8042_call(), 1)
output = relay.Tuple([call_9702,])
output2 = relay.Tuple([call_9703,])
func_9713 = relay.Function([], output)
mod['func_9713'] = func_9713
mod = relay.transform.InferType()(mod)
mutated_mod['func_9713'] = func_9713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9713_call = mutated_mod.get_global_var('func_9713')
call_9714 = func_9713_call()
output = call_9714
func_9715 = relay.Function([], output)
mutated_mod['func_9715'] = func_9715
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9716 = relay.const([[[-7.514608,-2.361381,3.833172],[-2.369301,9.953038,-8.889920],[-8.183426,-0.770974,1.006893],[5.527133,-2.487585,-4.974895],[-0.464513,-8.370180,7.716321]],[[4.162815,8.339678,-2.145052],[-8.650999,-9.161035,-8.556566],[1.506765,7.953993,-8.117979],[7.343790,-8.652259,8.160122],[-6.890961,-3.150114,0.115384]],[[6.151921,5.374879,-3.390872],[6.785788,-2.077178,-3.871946],[-8.072637,-5.525921,5.875244],[-5.652242,-8.499204,-3.374456],[-0.563093,1.044987,1.191830]],[[-9.918586,9.640200,-5.786035],[4.481967,0.769266,2.169793],[-3.987505,7.043934,6.386381],[4.083213,-9.260132,-9.851411],[1.442991,1.851575,7.303535]],[[-9.741448,6.268552,1.676616],[2.022251,5.296131,-8.222427],[0.843809,6.231256,4.270880],[9.523568,-3.050547,-7.820307],[0.812258,2.477085,-3.406719]],[[9.265775,-3.798714,1.434964],[-3.959824,5.082405,9.283604],[-7.935345,-0.672893,6.521410],[-6.414180,6.990414,-2.442275],[6.421162,8.214754,4.882405]],[[4.755081,-7.829698,8.554331],[6.913607,9.132878,-7.011104],[1.536554,4.792800,-1.911905],[8.262148,4.206639,0.236429],[9.768870,8.427811,-2.061592]],[[-7.427332,-4.751918,0.946249],[-0.373545,0.357753,1.670516],[-4.791225,1.427041,8.696381],[1.952432,-8.427589,7.228599],[-8.250201,6.387455,3.336243]]], dtype = "float32")#candidate|9716|(8, 5, 3)|const|float32
var_9717 = relay.var("var_9717", dtype = "float32", shape = (8, 5, 3))#candidate|9717|(8, 5, 3)|var|float32
bop_9718 = relay.subtract(const_9716.astype('float32'), relay.reshape(var_9717.astype('float32'), relay.shape_of(const_9716))) # shape=(8, 5, 3)
output = bop_9718
output2 = bop_9718
F = relay.Function([var_9717,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9717,], output2)
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
