import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_208 = relay.var("var_208", dtype = "float64", shape = (10, 7, 11))#candidate|208|(10, 7, 11)|var|float64
var_209 = relay.var("var_209", dtype = "float64", shape = (10, 7, 11))#candidate|209|(10, 7, 11)|var|float64
bop_210 = relay.power(var_208.astype('float64'), relay.reshape(var_209.astype('float64'), relay.shape_of(var_208))) # shape=(10, 7, 11)
output = relay.Tuple([bop_210,])
output2 = relay.Tuple([bop_210,])
func_219 = relay.Function([var_208,var_209,], output)
mod['func_219'] = func_219
mod = relay.transform.InferType()(mod)
var_220 = relay.var("var_220", dtype = "float64", shape = (10, 7, 11))#candidate|220|(10, 7, 11)|var|float64
var_221 = relay.var("var_221", dtype = "float64", shape = (10, 7, 11))#candidate|221|(10, 7, 11)|var|float64
output = func_219(var_220,var_221,)
func_222 = relay.Function([var_220,var_221,], output)
mutated_mod['func_222'] = func_222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_229 = relay.var("var_229", dtype = "int64", shape = ())#candidate|229|()|var|int64
const_230 = relay.const([[[-1,-1],[2,3],[6,-6],[-5,-3],[5,1],[-3,-7],[8,-7],[-8,6],[4,2],[1,-2],[3,2],[-4,6]],[[-4,-7],[-6,5],[4,10],[-9,-1],[6,-8],[1,3],[-6,3],[-9,-3],[-7,-2],[-7,-9],[-9,2],[7,-10]],[[9,9],[-8,7],[9,-5],[-2,-3],[-3,4],[-4,-8],[3,-10],[5,5],[-7,-7],[9,8],[3,-6],[6,-4]],[[4,6],[2,-10],[5,-9],[-7,-6],[1,9],[7,-9],[3,-5],[-5,-7],[-8,7],[-8,-7],[7,5],[10,-10]],[[5,2],[9,2],[5,2],[-6,-10],[-9,-4],[-4,-1],[-7,-4],[-6,-8],[4,-4],[-1,6],[4,7],[4,-6]],[[-2,1],[1,8],[-6,3],[-7,-6],[-10,7],[-7,-9],[-8,2],[-2,6],[-9,4],[10,-6],[-4,-10],[-1,-5]],[[7,4],[2,4],[10,3],[-6,-5],[-7,5],[-1,-4],[1,6],[-10,-6],[-1,-2],[4,5],[4,5],[7,5]],[[9,1],[-10,-4],[1,-4],[3,10],[10,8],[-10,7],[1,3],[2,-1],[-7,-4],[9,9],[-10,-1],[-3,-6]],[[2,9],[7,5],[-8,5],[8,4],[10,4],[5,-9],[8,-7],[-2,-6],[-9,8],[10,3],[4,1],[-5,7]],[[2,7],[7,-2],[8,6],[4,-6],[-6,8],[-8,6],[-10,3],[-2,5],[4,-1],[9,-5],[-5,-9],[-4,2]],[[1,-8],[3,-2],[2,10],[-8,8],[-6,4],[-6,-2],[-2,2],[8,-8],[5,8],[1,-1],[-5,-7],[-6,8]],[[5,7],[1,-4],[2,10],[9,-9],[-3,2],[-6,7],[6,8],[-8,-5],[-8,-6],[-4,3],[6,8],[-1,-10]],[[3,-10],[-7,-2],[-10,6],[-7,-3],[-3,-4],[-1,3],[-2,3],[-7,10],[6,-10],[-7,-7],[-5,7],[4,-6]],[[10,4],[-9,-9],[7,4],[6,5],[-2,-5],[9,5],[5,-5],[1,5],[-1,5],[7,1],[-5,-9],[7,-2]],[[-9,9],[1,2],[-6,-6],[-8,2],[-2,-1],[10,-3],[7,7],[4,-4],[-8,-10],[8,4],[9,-3],[-1,-10]],[[4,1],[3,1],[6,5],[-9,4],[1,4],[-8,-3],[8,-5],[3,-3],[-5,10],[-10,10],[-1,9],[-2,-7]]], dtype = "int64")#candidate|230|(16, 12, 2)|const|int64
bop_231 = relay.less_equal(var_229.astype('bool'), const_230.astype('bool')) # shape=(16, 12, 2)
bop_260 = relay.left_shift(var_229.astype('int32'), bop_231.astype('int32')) # shape=(16, 12, 2)
output = bop_260
output2 = bop_260
func_268 = relay.Function([var_229,], output)
mod['func_268'] = func_268
mod = relay.transform.InferType()(mod)
mutated_mod['func_268'] = func_268
mutated_mod = relay.transform.InferType()(mutated_mod)
var_269 = relay.var("var_269", dtype = "int64", shape = ())#candidate|269|()|var|int64
func_268_call = mutated_mod.get_global_var('func_268')
call_270 = func_268_call(var_269)
output = call_270
func_271 = relay.Function([var_269], output)
mutated_mod['func_271'] = func_271
mutated_mod = relay.transform.InferType()(mutated_mod)
const_278 = relay.const([[[-1.040883,-9.381473],[-6.734378,9.468110],[8.642105,-2.763518],[-1.902920,6.517225],[7.270195,-5.669825],[2.687153,-8.980146],[8.233895,-1.784790],[0.260988,9.031749],[-5.227519,-9.170478],[4.080066,-9.065437],[-8.026717,-6.443777],[5.510882,-0.552188],[7.134079,2.202167]],[[6.635528,-8.648649],[7.295506,-8.400035],[-5.088559,-8.403969],[-9.057027,6.806333],[-7.035231,-9.362834],[1.703746,4.204098],[-3.185138,2.087395],[0.444328,-9.007817],[-7.815471,7.693370],[-3.113681,-4.850562],[9.617635,7.083216],[7.282024,0.865376],[3.192623,-9.775850]],[[-0.686208,4.065042],[2.144362,4.070053],[6.711407,4.070189],[-5.124453,8.625241],[0.356349,0.600772],[-1.502783,-6.689264],[-7.775078,0.778848],[6.496326,-7.894550],[-5.284921,-6.862422],[-0.051891,-8.929163],[3.699860,6.697643],[-9.425463,-8.222413],[-6.360948,-8.048957]]], dtype = "float32")#candidate|278|(3, 13, 2)|const|float32
uop_279 = relay.atanh(const_278.astype('float32')) # shape=(3, 13, 2)
output = relay.Tuple([uop_279,])
output2 = relay.Tuple([uop_279,])
func_281 = relay.Function([], output)
mod['func_281'] = func_281
mod = relay.transform.InferType()(mod)
mutated_mod['func_281'] = func_281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mutated_mod.get_global_var('func_281')
call_282 = func_281_call()
output = call_282
func_283 = relay.Function([], output)
mutated_mod['func_283'] = func_283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_337 = relay.TupleGetItem(func_281_call(), 0)
call_338 = relay.TupleGetItem(func_283_call(), 0)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_341 = relay.TupleGetItem(func_281_call(), 0)
call_342 = relay.TupleGetItem(func_283_call(), 0)
output = relay.Tuple([call_337,call_341,])
output2 = relay.Tuple([call_338,call_342,])
func_353 = relay.Function([], output)
mod['func_353'] = func_353
mod = relay.transform.InferType()(mod)
mutated_mod['func_353'] = func_353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mutated_mod.get_global_var('func_353')
call_354 = func_353_call()
output = call_354
func_355 = relay.Function([], output)
mutated_mod['func_355'] = func_355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_396 = relay.TupleGetItem(func_281_call(), 0)
call_397 = relay.TupleGetItem(func_283_call(), 0)
output = call_396
output2 = call_397
func_407 = relay.Function([], output)
mod['func_407'] = func_407
mod = relay.transform.InferType()(mod)
mutated_mod['func_407'] = func_407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mutated_mod.get_global_var('func_407')
call_408 = func_407_call()
output = call_408
func_409 = relay.Function([], output)
mutated_mod['func_409'] = func_409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_410 = relay.TupleGetItem(func_353_call(), 1)
call_411 = relay.TupleGetItem(func_355_call(), 1)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_417 = relay.TupleGetItem(func_281_call(), 0)
call_418 = relay.TupleGetItem(func_283_call(), 0)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_421 = relay.TupleGetItem(func_353_call(), 0)
call_422 = relay.TupleGetItem(func_355_call(), 0)
output = relay.Tuple([call_410,call_417,call_421,])
output2 = relay.Tuple([call_411,call_418,call_422,])
func_423 = relay.Function([], output)
mod['func_423'] = func_423
mod = relay.transform.InferType()(mod)
output = func_423()
func_424 = relay.Function([], output)
mutated_mod['func_424'] = func_424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_447 = func_407_call()
call_448 = func_407_call()
output = call_447
output2 = call_448
func_458 = relay.Function([], output)
mod['func_458'] = func_458
mod = relay.transform.InferType()(mod)
mutated_mod['func_458'] = func_458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mutated_mod.get_global_var('func_458')
call_459 = func_458_call()
output = call_459
func_460 = relay.Function([], output)
mutated_mod['func_460'] = func_460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_474 = relay.TupleGetItem(func_353_call(), 1)
call_475 = relay.TupleGetItem(func_355_call(), 1)
const_482 = relay.const([[[-3.745434,4.533924],[7.662985,3.333385],[-1.486143,-2.607683],[5.489183,-7.295718],[7.215324,-6.436608],[6.904243,-8.530310],[-0.240290,6.696533],[3.847039,0.902213],[-1.261716,5.269377],[8.370738,-6.545885],[-4.983134,-6.353572],[9.450905,2.108184],[-1.926795,-1.462026]],[[9.767258,-5.134898],[2.997765,7.647983],[8.253587,-2.787077],[2.687093,4.965554],[9.493552,8.566404],[-2.034551,0.941836],[-9.203222,-5.335844],[-3.854996,-0.401281],[9.632374,4.684380],[-8.655501,8.652721],[9.284589,7.409857],[1.383700,7.590617],[0.439175,7.406742]],[[9.678007,2.973703],[6.734626,-9.909877],[2.566303,8.250201],[-5.246821,4.377654],[5.668932,-9.602063],[-9.410092,-8.851450],[-4.331080,-4.441327],[-8.460117,2.659385],[-4.506920,1.246535],[5.228593,1.176645],[-6.229600,2.567440],[7.734161,-6.609473],[-7.767757,1.609286]]], dtype = "float32")#candidate|482|(3, 13, 2)|const|float32
bop_483 = relay.add(call_474.astype('int64'), relay.reshape(const_482.astype('int64'), relay.shape_of(call_474))) # shape=(3, 13, 2)
bop_486 = relay.add(call_475.astype('int64'), relay.reshape(const_482.astype('int64'), relay.shape_of(call_475))) # shape=(3, 13, 2)
output = relay.Tuple([bop_483,])
output2 = relay.Tuple([bop_486,])
func_489 = relay.Function([], output)
mod['func_489'] = func_489
mod = relay.transform.InferType()(mod)
mutated_mod['func_489'] = func_489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_489_call = mutated_mod.get_global_var('func_489')
call_490 = func_489_call()
output = call_490
func_491 = relay.Function([], output)
mutated_mod['func_491'] = func_491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_492 = func_407_call()
call_493 = func_407_call()
var_495 = relay.var("var_495", dtype = "float32", shape = (3, 13, 2))#candidate|495|(3, 13, 2)|var|float32
bop_496 = relay.greater(call_492.astype('bool'), relay.reshape(var_495.astype('bool'), relay.shape_of(call_492))) # shape=(3, 13, 2)
bop_499 = relay.greater(call_493.astype('bool'), relay.reshape(var_495.astype('bool'), relay.shape_of(call_493))) # shape=(3, 13, 2)
var_515 = relay.var("var_515", dtype = "float32", shape = (3, 13, 2))#candidate|515|(3, 13, 2)|var|float32
bop_516 = relay.less_equal(var_495.astype('bool'), relay.reshape(var_515.astype('bool'), relay.shape_of(var_495))) # shape=(3, 13, 2)
bop_519 = relay.minimum(var_495.astype('float32'), relay.reshape(var_515.astype('float32'), relay.shape_of(var_495))) # shape=(3, 13, 2)
output = relay.Tuple([bop_496,bop_516,bop_519,])
output2 = relay.Tuple([bop_499,bop_516,bop_519,])
func_523 = relay.Function([var_495,var_515,], output)
mod['func_523'] = func_523
mod = relay.transform.InferType()(mod)
mutated_mod['func_523'] = func_523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_523_call = mutated_mod.get_global_var('func_523')
var_525 = relay.var("var_525", dtype = "float32", shape = (3, 13, 2))#candidate|525|(3, 13, 2)|var|float32
var_526 = relay.var("var_526", dtype = "float32", shape = (3, 13, 2))#candidate|526|(3, 13, 2)|var|float32
call_524 = func_523_call(var_525,var_526,)
output = call_524
func_527 = relay.Function([var_525,var_526,], output)
mutated_mod['func_527'] = func_527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_529 = relay.var("var_529", dtype = "float32", shape = (14, 2, 15))#candidate|529|(14, 2, 15)|var|float32
uop_530 = relay.sigmoid(var_529.astype('float32')) # shape=(14, 2, 15)
func_523_call = mod.get_global_var('func_523')
func_527_call = mutated_mod.get_global_var('func_527')
var_564 = relay.var("var_564", dtype = "float32", shape = (78,))#candidate|564|(78,)|var|float32
call_563 = relay.TupleGetItem(func_523_call(relay.reshape(var_564.astype('float32'), [3, 13, 2]), relay.reshape(var_564.astype('float32'), [3, 13, 2]), ), 0)
call_565 = relay.TupleGetItem(func_527_call(relay.reshape(var_564.astype('float32'), [3, 13, 2]), relay.reshape(var_564.astype('float32'), [3, 13, 2]), ), 0)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_572 = relay.TupleGetItem(func_353_call(), 1)
call_573 = relay.TupleGetItem(func_355_call(), 1)
output = relay.Tuple([uop_530,call_563,var_564,call_572,])
output2 = relay.Tuple([uop_530,call_565,var_564,call_573,])
func_585 = relay.Function([var_529,var_564,], output)
mod['func_585'] = func_585
mod = relay.transform.InferType()(mod)
mutated_mod['func_585'] = func_585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mutated_mod.get_global_var('func_585')
var_587 = relay.var("var_587", dtype = "float32", shape = (14, 2, 15))#candidate|587|(14, 2, 15)|var|float32
var_588 = relay.var("var_588", dtype = "float32", shape = (78,))#candidate|588|(78,)|var|float32
call_586 = func_585_call(var_587,var_588,)
output = call_586
func_589 = relay.Function([var_587,var_588,], output)
mutated_mod['func_589'] = func_589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_489_call = mod.get_global_var('func_489')
func_491_call = mutated_mod.get_global_var('func_491')
call_620 = relay.TupleGetItem(func_489_call(), 0)
call_621 = relay.TupleGetItem(func_491_call(), 0)
uop_638 = relay.sigmoid(call_620.astype('float64')) # shape=(3, 13, 2)
uop_640 = relay.sigmoid(call_621.astype('float64')) # shape=(3, 13, 2)
output = uop_638
output2 = uop_640
func_648 = relay.Function([], output)
mod['func_648'] = func_648
mod = relay.transform.InferType()(mod)
mutated_mod['func_648'] = func_648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_648_call = mutated_mod.get_global_var('func_648')
call_649 = func_648_call()
output = call_649
func_650 = relay.Function([], output)
mutated_mod['func_650'] = func_650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_675 = func_458_call()
call_676 = func_458_call()
func_268_call = mod.get_global_var('func_268')
func_271_call = mutated_mod.get_global_var('func_271')
var_691 = relay.var("var_691", dtype = "int64", shape = ())#candidate|691|()|var|int64
call_690 = func_268_call(relay.reshape(var_691.astype('int64'), []))
call_692 = func_268_call(relay.reshape(var_691.astype('int64'), []))
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_697 = relay.TupleGetItem(func_281_call(), 0)
call_698 = relay.TupleGetItem(func_283_call(), 0)
output = relay.Tuple([call_675,call_690,var_691,call_697,])
output2 = relay.Tuple([call_676,call_692,var_691,call_698,])
func_699 = relay.Function([var_691,], output)
mod['func_699'] = func_699
mod = relay.transform.InferType()(mod)
var_700 = relay.var("var_700", dtype = "int64", shape = ())#candidate|700|()|var|int64
output = func_699(var_700)
func_701 = relay.Function([var_700], output)
mutated_mod['func_701'] = func_701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_489_call = mod.get_global_var('func_489')
func_491_call = mutated_mod.get_global_var('func_491')
call_738 = relay.TupleGetItem(func_489_call(), 0)
call_739 = relay.TupleGetItem(func_491_call(), 0)
output = relay.Tuple([call_738,])
output2 = relay.Tuple([call_739,])
func_757 = relay.Function([], output)
mod['func_757'] = func_757
mod = relay.transform.InferType()(mod)
output = func_757()
func_758 = relay.Function([], output)
mutated_mod['func_758'] = func_758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_648_call = mod.get_global_var('func_648')
func_650_call = mutated_mod.get_global_var('func_650')
call_784 = func_648_call()
call_785 = func_648_call()
output = call_784
output2 = call_785
func_810 = relay.Function([], output)
mod['func_810'] = func_810
mod = relay.transform.InferType()(mod)
mutated_mod['func_810'] = func_810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_810_call = mutated_mod.get_global_var('func_810')
call_811 = func_810_call()
output = call_811
func_812 = relay.Function([], output)
mutated_mod['func_812'] = func_812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_816 = relay.TupleGetItem(func_353_call(), 0)
call_817 = relay.TupleGetItem(func_355_call(), 0)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_820 = func_458_call()
call_821 = func_458_call()
uop_822 = relay.log10(call_816.astype('float32')) # shape=(3, 13, 2)
uop_824 = relay.log10(call_817.astype('float32')) # shape=(3, 13, 2)
output = relay.Tuple([call_820,uop_822,])
output2 = relay.Tuple([call_821,uop_824,])
func_831 = relay.Function([], output)
mod['func_831'] = func_831
mod = relay.transform.InferType()(mod)
mutated_mod['func_831'] = func_831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_831_call = mutated_mod.get_global_var('func_831')
call_832 = func_831_call()
output = call_832
func_833 = relay.Function([], output)
mutated_mod['func_833'] = func_833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_836 = relay.TupleGetItem(func_281_call(), 0)
call_837 = relay.TupleGetItem(func_283_call(), 0)
var_838 = relay.var("var_838", dtype = "float32", shape = (3, 13, 2))#candidate|838|(3, 13, 2)|var|float32
bop_839 = relay.floor_mod(call_836.astype('float64'), relay.reshape(var_838.astype('float64'), relay.shape_of(call_836))) # shape=(3, 13, 2)
bop_842 = relay.floor_mod(call_837.astype('float64'), relay.reshape(var_838.astype('float64'), relay.shape_of(call_837))) # shape=(3, 13, 2)
uop_843 = relay.erf(bop_839.astype('float32')) # shape=(3, 13, 2)
uop_845 = relay.erf(bop_842.astype('float32')) # shape=(3, 13, 2)
output = relay.Tuple([uop_843,])
output2 = relay.Tuple([uop_845,])
func_853 = relay.Function([var_838,], output)
mod['func_853'] = func_853
mod = relay.transform.InferType()(mod)
mutated_mod['func_853'] = func_853
mutated_mod = relay.transform.InferType()(mutated_mod)
var_854 = relay.var("var_854", dtype = "float32", shape = (3, 13, 2))#candidate|854|(3, 13, 2)|var|float32
func_853_call = mutated_mod.get_global_var('func_853')
call_855 = func_853_call(var_854)
output = call_855
func_856 = relay.Function([var_854], output)
mutated_mod['func_856'] = func_856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_871 = func_458_call()
call_872 = func_458_call()
uop_874 = relay.rsqrt(call_871.astype('float64')) # shape=(3, 13, 2)
uop_876 = relay.rsqrt(call_872.astype('float64')) # shape=(3, 13, 2)
bop_878 = relay.bitwise_or(uop_874.astype('uint8'), relay.reshape(call_871.astype('uint8'), relay.shape_of(uop_874))) # shape=(3, 13, 2)
bop_881 = relay.bitwise_or(uop_876.astype('uint8'), relay.reshape(call_872.astype('uint8'), relay.shape_of(uop_876))) # shape=(3, 13, 2)
bop_884 = relay.equal(bop_878.astype('bool'), relay.reshape(uop_874.astype('bool'), relay.shape_of(bop_878))) # shape=(3, 13, 2)
bop_887 = relay.equal(bop_881.astype('bool'), relay.reshape(uop_876.astype('bool'), relay.shape_of(bop_881))) # shape=(3, 13, 2)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_895 = relay.TupleGetItem(func_353_call(), 1)
call_896 = relay.TupleGetItem(func_355_call(), 1)
func_699_call = mod.get_global_var('func_699')
func_701_call = mutated_mod.get_global_var('func_701')
const_900 = relay.const(-2, dtype = "int64")#candidate|900|()|const|int64
call_899 = relay.TupleGetItem(func_699_call(relay.reshape(const_900.astype('int64'), [])), 0)
call_901 = relay.TupleGetItem(func_701_call(relay.reshape(const_900.astype('int64'), [])), 0)
bop_909 = relay.logical_or(bop_884.astype('bool'), relay.reshape(call_899.astype('bool'), relay.shape_of(bop_884))) # shape=(3, 13, 2)
bop_912 = relay.logical_or(bop_887.astype('bool'), relay.reshape(call_901.astype('bool'), relay.shape_of(bop_887))) # shape=(3, 13, 2)
uop_922 = relay.exp(uop_874.astype('float32')) # shape=(3, 13, 2)
uop_924 = relay.exp(uop_876.astype('float32')) # shape=(3, 13, 2)
func_523_call = mod.get_global_var('func_523')
func_527_call = mutated_mod.get_global_var('func_527')
call_936 = relay.TupleGetItem(func_523_call(relay.reshape(bop_884.astype('float32'), [3, 13, 2]), relay.reshape(call_895.astype('float32'), [3, 13, 2]), ), 1)
call_937 = relay.TupleGetItem(func_527_call(relay.reshape(bop_884.astype('float32'), [3, 13, 2]), relay.reshape(call_895.astype('float32'), [3, 13, 2]), ), 1)
func_219_call = mod.get_global_var('func_219')
func_222_call = mutated_mod.get_global_var('func_222')
const_949 = relay.const([[-6.591923,-8.384531,0.577054,-8.263866,7.428835,7.315944,-9.068160,-6.105768,-8.232174,-0.337986,-1.479999,-3.372631,3.440064,-3.037325,6.354801,-5.857252,1.550567,9.421720,-1.933244,9.225891,-7.843008,-2.126996,6.626305,7.144315,-3.676826,8.778999,4.631844,-4.291985,6.763837,6.669530,5.913073,-1.984308,-6.423682,7.441267,6.504054,-9.683124,-3.812651,-8.766541,0.402721,0.548291,0.919654,9.928240,1.308116,8.300532,-2.703359,7.242597,-4.873917,-4.266485,9.058092,6.606354,-5.598661,-2.043240,6.878726,6.911214,1.206709,-3.480915,8.412634,3.158978,-4.527709,-1.985173,6.548089,-1.637774,7.668840,-7.035983,5.564725,-9.846513,4.886445,-4.131873,4.039974,-7.917774,-6.473300,-9.950400,-9.915500,-4.342041,-2.928968,5.006586,-9.318920,-2.281341,3.748311,8.985879,-1.919004,-7.924047,-9.299989,-7.784748,-5.357668,-1.298251,-6.286480,2.505502,2.754933,4.192289,-3.155878,9.712975,-2.311341,-5.681849,7.910289,-8.776041,0.042696,8.157547,1.934747,-2.222331,-1.453752,4.812115,7.425938,4.838256,-3.864802,-1.816190,-8.773333,-8.680733,4.228499,-3.054017,-2.014277,6.346876,6.824104,1.880105,-1.215748,7.536632,8.154784,0.800083,4.724343,3.034041,8.963516,-1.326326,7.621964,4.782268,3.013097,0.345553,-9.421581,-9.275048,-5.061906,2.404802,8.381730,5.507505,6.692158,2.507505,-9.643589,-5.285964,-3.668544,1.559845,8.418362,1.920145,-8.737628,-9.948720,9.882188,-2.710045,0.016744,-1.747204,-7.185702,5.674820,9.539366,-1.784722,3.156956,9.556612,5.582961,1.244822,0.617875,-0.443790,-9.464520,5.769900,0.862286,0.724948,1.668944,5.930162,1.995327,1.280879,5.912920,-6.041242,-7.736973,-9.687307,-5.549622,4.769644,-6.138704,8.354165,-2.152491,-8.049629,5.403474,-0.883707,-9.633420,-2.124156,-2.777489,-5.029541,-8.168962,-8.602529,-3.557077,-5.000131,6.257395,5.610296,6.689425,-0.071478,9.780113,5.096804,-1.126246,3.991600,4.050760,-7.990108,7.650298,2.601903,-5.561914,-1.640568,0.933197,9.941718,-0.689376,-9.536905,-4.494567,-2.871025,-3.538090,-9.848840,3.659558,2.524847,6.418526,5.824848,-2.523185,-8.999107,-7.085732,5.275482,-1.683826,-9.036446,6.953723,-4.314199,3.988929,7.125633,9.630404,-6.943635,8.625748,2.377326,-8.613973,1.264491,-9.807527,4.357290,6.257250,-2.156701,7.176969,-2.198029,1.606384,-6.063844,7.429284,-8.224974,0.409635,-1.953560,-8.147828,-7.190917,-2.845186,4.197858,3.311535,3.831270,-2.776272,-2.352631,8.188812,-5.197000,-9.779711,1.532753,3.614396,-8.089003,8.818456,0.686613,-0.604028,-7.608933,-5.238669,7.287617,-6.287316,-4.686186,-0.797405,-0.952222,6.349034,7.745463,-2.377937,-8.552262,-9.750960,-8.041346,7.715364,-7.894402,7.743815,-7.220245,-0.100504,-9.155933,-9.208760,5.295852,6.424852,-8.167928,8.331469,-6.647908,4.079210,4.320181,7.725911,0.398725,6.394904,8.098406,-3.239060,-5.727109,6.654687,2.120070,9.576464,1.520576,-5.135723,-6.261219,6.520046,9.659168,9.568214,-1.649182,5.797466,0.219113,4.815339,9.963720,-7.530266,9.339059,-6.265374,0.781865,1.174108,2.698055,3.187308,6.272066,-3.659712,8.627107,2.269920,6.069762,4.456742,-8.315592,3.707928,-0.149127,5.739347,1.925010,-6.926939,-8.175824,2.256666,9.237131,3.304024,5.708490,-9.143358,4.480402,2.543584,-3.457916,0.660844,2.076089,-9.570264,-8.105033,4.520111,-4.338693,-1.458914,-3.256011,-5.758312,-7.148165,-1.579631,8.729105,-0.606388,6.885920,7.302147,-2.174352,-2.514452,1.950549,9.426893,-9.459061,-5.360401,-9.393043,8.427657,-4.039424,3.699108,1.690634,6.469867,-7.125549,2.521594,3.938765,2.718428,1.379252,5.456608,-0.823650,-7.855305,-0.246581,8.514897,-9.078035,6.111225,-3.094974,1.231483,-1.220858,3.834338,0.704803,-7.535255,3.077880,-8.408189,1.963313,-5.962242,0.710286,3.152334,0.921929,-7.587686,5.652041,-4.964641,-7.169476,-1.577575,-5.839258,8.459705,-2.382156,-2.658607,8.803545,8.611359,9.791320,3.985510,-5.818057,-9.072787,7.178402,5.323454,-7.620500,0.582652,-1.724554,9.382836,7.746653,-5.504452,9.753661,0.675184,9.283592,0.678355,-8.811799,2.778861,5.334144,-4.592961,5.989590,-6.227929,-0.383975,-6.487554,6.016747,8.329507,5.013641,-6.417922,9.982775,2.992123,-0.299034,0.493325,7.408598,-8.203333,-0.681434,-8.586235,-0.384070,5.074547,-3.079263,9.251241,3.289035,-4.577703,-2.725701,4.036294,-6.335260,7.319363,-2.112127,-6.413779,0.833812,-8.567940,0.090060,0.658827,2.434153,-7.993759,4.513958,6.158972,4.368755,2.755652,7.253718,9.517496,6.506599,-4.847404,4.512318,-6.748253,3.204172,-5.439282,5.939044,5.837121,-9.988518,-0.290098,4.545793,-6.965587,4.698111,8.067804,3.388516,-3.452612,6.649095,-4.908200,0.951511,7.186602,6.087593,-9.387202,-8.174830,-1.662511,6.877688,-8.393315,-0.634700,2.113919,-4.103498,-6.309355,2.828437,-6.778868,-9.572867,2.639711,6.523325,-6.147964,-4.525073,3.742972,-9.985958,2.548944,-0.116808,0.640852,5.735773,-7.674978,3.206897,6.231285,-8.927087,9.034356,-3.095685,-9.172861,3.440977,-1.594569,8.866581,-0.629097,1.419137,-0.029253,9.000017,8.373621,-6.016470,-8.845124,-9.824345,0.714640,-3.102418,2.831721,3.455407,-1.489007,0.939639,0.025379,8.130203,-6.534769,7.187266,-3.670498,-3.944500,3.138985,-0.966454,-4.277536,6.105379,9.917293,-0.018858,-2.292953,-0.893792,8.654077,-0.187263,5.248608,-3.262762,-0.569541,-1.522479,1.712380,-7.828646,4.173404,-4.840381,-6.720754,9.174840,7.957919,-3.660433,-3.547370,2.639739,-1.899874,-2.056084,4.676596,-0.729975,-1.444977,-7.588129,9.854271,1.873791,7.501392,7.411397,6.381203,8.617341,-3.504414,2.751706,6.844952,-4.326253,-7.165366,0.848477,-0.242724,9.992243,-9.936304,-9.181095,2.343709,-8.245991,4.882359,-8.274251,6.843977,-7.056047,0.901075,-2.375216,-5.849242,5.394866,5.074140,-8.944928,-8.675089,-9.698584,9.602355,-0.303912,-4.587972,-2.512463,-2.070692,3.476867,-3.273158,-9.654977,1.274007,-7.464446,2.841384,-9.842350,-2.487894,-6.157070,-7.914978,0.861613,2.638607,-7.360871,8.100566,-7.067447,4.378865,0.350475,3.074238,-4.538456,-1.755184,-6.054920,-4.244651,-2.628878,6.752952,2.006793,6.577384,2.494763,-6.792290,1.322028,-2.472777,-0.476259,4.809137,-1.567834,9.930910,0.612979,3.156272,0.291288,-5.325696,4.663210,1.940334,8.532663,2.786539,4.434411,4.450377,6.622595,-9.805042,9.549614,3.849805,-7.896236,-8.802040,-7.477144,4.191394,2.106653,9.888740,1.446938,0.108240,-4.915381,-5.620027,6.477373,-4.706866,3.128316,-4.981752,-8.622888,-1.372795,-3.177577,-8.566135,9.540208,-7.405778,8.812823,8.744236,-4.143760,2.102507,7.037309,0.724265,0.017062,-3.680791,-2.676813,-5.453168,-8.549325,-2.183126,3.797850,-8.064806,-7.145549,-9.274176,-9.235232,6.547454,-3.897861,3.425409,-6.309670,-0.159117,-0.382117,-2.396551,3.680146,9.812922,-9.492011,-7.228776,-7.043733,-6.290255,-6.197716,-5.045704,-6.159873,1.714749,2.853329,-2.355089,7.301855,5.905439,8.050658,5.765634,-9.616697,7.299834,-2.283144,9.989797,-8.065109,2.324835,-1.896825,0.749959,0.998071,6.851551,-9.295830,-1.624588,9.505606,8.465296,-1.485072,6.329610,-9.042940,3.772658,3.953139,3.913757,-2.212392,-4.948264,5.783095,6.444198,-7.682795,1.358378,-6.144081,0.624678,1.016461,6.443926,1.435725,6.472344,1.151854,-6.156637,7.242813,-4.156929,-9.211005,-0.783383,-7.081780,8.568501,-3.213720,5.602782,-0.290145,-9.309357,-0.754623,5.409265,1.475335,6.084275,8.032385,4.268962,1.038391,-1.313719,-1.057224,6.479536,-5.489192,8.908582,3.382720,-0.065319,1.519462,-1.579839,-9.209376,0.246006,-6.817849,-7.484243,-0.432616,-9.214416,5.788586,-6.080919,7.874968,-1.435824,-3.582519]], dtype = "float64")#candidate|949|(1, 770)|const|float64
call_948 = relay.TupleGetItem(func_219_call(relay.reshape(const_949.astype('float64'), [10, 7, 11]), relay.reshape(const_949.astype('float64'), [10, 7, 11]), ), 0)
call_950 = relay.TupleGetItem(func_222_call(relay.reshape(const_949.astype('float64'), [10, 7, 11]), relay.reshape(const_949.astype('float64'), [10, 7, 11]), ), 0)
func_699_call = mod.get_global_var('func_699')
func_701_call = mutated_mod.get_global_var('func_701')
call_957 = relay.TupleGetItem(func_699_call(relay.reshape(const_900.astype('int64'), [])), 3)
call_958 = relay.TupleGetItem(func_701_call(relay.reshape(const_900.astype('int64'), [])), 3)
bop_959 = relay.minimum(const_949.astype('int8'), const_900.astype('int8')) # shape=(1, 770)
func_853_call = mod.get_global_var('func_853')
func_856_call = mutated_mod.get_global_var('func_856')
call_964 = relay.TupleGetItem(func_853_call(relay.reshape(bop_878.astype('float32'), [3, 13, 2])), 0)
call_965 = relay.TupleGetItem(func_856_call(relay.reshape(bop_878.astype('float32'), [3, 13, 2])), 0)
func_831_call = mod.get_global_var('func_831')
func_833_call = mutated_mod.get_global_var('func_833')
call_966 = relay.TupleGetItem(func_831_call(), 0)
call_967 = relay.TupleGetItem(func_833_call(), 0)
func_853_call = mod.get_global_var('func_853')
func_856_call = mutated_mod.get_global_var('func_856')
call_980 = relay.TupleGetItem(func_853_call(relay.reshape(bop_909.astype('float32'), [3, 13, 2])), 0)
call_981 = relay.TupleGetItem(func_856_call(relay.reshape(bop_909.astype('float32'), [3, 13, 2])), 0)
output = relay.Tuple([call_895,bop_909,uop_922,call_936,call_948,call_957,bop_959,call_964,call_966,call_980,])
output2 = relay.Tuple([call_896,bop_912,uop_924,call_937,call_950,call_958,bop_959,call_965,call_967,call_981,])
func_989 = relay.Function([], output)
mod['func_989'] = func_989
mod = relay.transform.InferType()(mod)
output = func_989()
func_990 = relay.Function([], output)
mutated_mod['func_990'] = func_990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_810_call = mod.get_global_var('func_810')
func_812_call = mutated_mod.get_global_var('func_812')
call_1041 = func_810_call()
call_1042 = func_810_call()
func_523_call = mod.get_global_var('func_523')
func_527_call = mutated_mod.get_global_var('func_527')
call_1056 = relay.TupleGetItem(func_523_call(relay.reshape(call_1041.astype('float32'), [3, 13, 2]), relay.reshape(call_1041.astype('float32'), [3, 13, 2]), ), 1)
call_1057 = relay.TupleGetItem(func_527_call(relay.reshape(call_1041.astype('float32'), [3, 13, 2]), relay.reshape(call_1041.astype('float32'), [3, 13, 2]), ), 1)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_1058 = func_458_call()
call_1059 = func_458_call()
uop_1073 = relay.sin(call_1041.astype('float32')) # shape=(3, 13, 2)
uop_1075 = relay.sin(call_1042.astype('float32')) # shape=(3, 13, 2)
output = relay.Tuple([call_1056,call_1058,uop_1073,])
output2 = relay.Tuple([call_1057,call_1059,uop_1075,])
func_1076 = relay.Function([], output)
mod['func_1076'] = func_1076
mod = relay.transform.InferType()(mod)
output = func_1076()
func_1077 = relay.Function([], output)
mutated_mod['func_1077'] = func_1077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1076_call = mod.get_global_var('func_1076')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_1090 = relay.TupleGetItem(func_1076_call(), 2)
call_1091 = relay.TupleGetItem(func_1077_call(), 2)
func_853_call = mod.get_global_var('func_853')
func_856_call = mutated_mod.get_global_var('func_856')
call_1094 = relay.TupleGetItem(func_853_call(relay.reshape(call_1090.astype('float32'), [3, 13, 2])), 0)
call_1095 = relay.TupleGetItem(func_856_call(relay.reshape(call_1090.astype('float32'), [3, 13, 2])), 0)
output = relay.Tuple([call_1090,call_1094,])
output2 = relay.Tuple([call_1091,call_1095,])
func_1108 = relay.Function([], output)
mod['func_1108'] = func_1108
mod = relay.transform.InferType()(mod)
output = func_1108()
func_1109 = relay.Function([], output)
mutated_mod['func_1109'] = func_1109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_1165 = func_407_call()
call_1166 = func_407_call()
func_699_call = mod.get_global_var('func_699')
func_701_call = mutated_mod.get_global_var('func_701')
var_1176 = relay.var("var_1176", dtype = "int64", shape = ())#candidate|1176|()|var|int64
call_1175 = relay.TupleGetItem(func_699_call(relay.reshape(var_1176.astype('int64'), [])), 0)
call_1177 = relay.TupleGetItem(func_701_call(relay.reshape(var_1176.astype('int64'), [])), 0)
func_219_call = mod.get_global_var('func_219')
func_222_call = mutated_mod.get_global_var('func_222')
var_1179 = relay.var("var_1179", dtype = "float64", shape = (1, 770))#candidate|1179|(1, 770)|var|float64
call_1178 = relay.TupleGetItem(func_219_call(relay.reshape(var_1179.astype('float64'), [10, 7, 11]), relay.reshape(var_1179.astype('float64'), [10, 7, 11]), ), 0)
call_1180 = relay.TupleGetItem(func_222_call(relay.reshape(var_1179.astype('float64'), [10, 7, 11]), relay.reshape(var_1179.astype('float64'), [10, 7, 11]), ), 0)
func_831_call = mod.get_global_var('func_831')
func_833_call = mutated_mod.get_global_var('func_833')
call_1181 = relay.TupleGetItem(func_831_call(), 0)
call_1182 = relay.TupleGetItem(func_833_call(), 0)
func_523_call = mod.get_global_var('func_523')
func_527_call = mutated_mod.get_global_var('func_527')
call_1198 = relay.TupleGetItem(func_523_call(relay.reshape(call_1181.astype('float32'), [3, 13, 2]), relay.reshape(call_1175.astype('float32'), [3, 13, 2]), ), 1)
call_1199 = relay.TupleGetItem(func_527_call(relay.reshape(call_1181.astype('float32'), [3, 13, 2]), relay.reshape(call_1175.astype('float32'), [3, 13, 2]), ), 1)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_1201 = relay.TupleGetItem(func_281_call(), 0)
call_1202 = relay.TupleGetItem(func_283_call(), 0)
var_1233 = relay.var("var_1233", dtype = "float64", shape = (15, 770))#candidate|1233|(15, 770)|var|float64
bop_1234 = relay.multiply(var_1179.astype('int64'), var_1233.astype('int64')) # shape=(15, 770)
func_1108_call = mod.get_global_var('func_1108')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_1254 = relay.TupleGetItem(func_1108_call(), 0)
call_1255 = relay.TupleGetItem(func_1109_call(), 0)
func_219_call = mod.get_global_var('func_219')
func_222_call = mutated_mod.get_global_var('func_222')
call_1259 = relay.TupleGetItem(func_219_call(relay.reshape(var_1179.astype('float64'), [10, 7, 11]), relay.reshape(call_1178.astype('float64'), [10, 7, 11]), ), 0)
call_1260 = relay.TupleGetItem(func_222_call(relay.reshape(var_1179.astype('float64'), [10, 7, 11]), relay.reshape(call_1178.astype('float64'), [10, 7, 11]), ), 0)
bop_1269 = relay.divide(var_1176.astype('float64'), bop_1234.astype('float64')) # shape=(15, 770)
func_810_call = mod.get_global_var('func_810')
func_812_call = mutated_mod.get_global_var('func_812')
call_1272 = func_810_call()
call_1273 = func_810_call()
output = relay.Tuple([call_1165,call_1175,call_1178,call_1181,call_1198,call_1201,call_1254,call_1259,bop_1269,call_1272,])
output2 = relay.Tuple([call_1166,call_1177,call_1180,call_1182,call_1199,call_1202,call_1255,call_1260,bop_1269,call_1273,])
func_1278 = relay.Function([var_1176,var_1179,var_1233,], output)
mod['func_1278'] = func_1278
mod = relay.transform.InferType()(mod)
var_1279 = relay.var("var_1279", dtype = "int64", shape = ())#candidate|1279|()|var|int64
var_1280 = relay.var("var_1280", dtype = "float64", shape = (1, 770))#candidate|1280|(1, 770)|var|float64
var_1281 = relay.var("var_1281", dtype = "float64", shape = (15, 770))#candidate|1281|(15, 770)|var|float64
output = func_1278(var_1279,var_1280,var_1281,)
func_1282 = relay.Function([var_1279,var_1280,var_1281,], output)
mutated_mod['func_1282'] = func_1282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1076_call = mod.get_global_var('func_1076')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_1298 = relay.TupleGetItem(func_1076_call(), 2)
call_1299 = relay.TupleGetItem(func_1077_call(), 2)
output = relay.Tuple([call_1298,])
output2 = relay.Tuple([call_1299,])
func_1304 = relay.Function([], output)
mod['func_1304'] = func_1304
mod = relay.transform.InferType()(mod)
mutated_mod['func_1304'] = func_1304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1304_call = mutated_mod.get_global_var('func_1304')
call_1305 = func_1304_call()
output = call_1305
func_1306 = relay.Function([], output)
mutated_mod['func_1306'] = func_1306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1108_call = mod.get_global_var('func_1108')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_1389 = relay.TupleGetItem(func_1108_call(), 0)
call_1390 = relay.TupleGetItem(func_1109_call(), 0)
output = relay.Tuple([call_1389,])
output2 = relay.Tuple([call_1390,])
func_1393 = relay.Function([], output)
mod['func_1393'] = func_1393
mod = relay.transform.InferType()(mod)
output = func_1393()
func_1394 = relay.Function([], output)
mutated_mod['func_1394'] = func_1394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_810_call = mod.get_global_var('func_810')
func_812_call = mutated_mod.get_global_var('func_812')
call_1454 = func_810_call()
call_1455 = func_810_call()
func_810_call = mod.get_global_var('func_810')
func_812_call = mutated_mod.get_global_var('func_812')
call_1508 = func_810_call()
call_1509 = func_810_call()
output = relay.Tuple([call_1454,call_1508,])
output2 = relay.Tuple([call_1455,call_1509,])
func_1514 = relay.Function([], output)
mod['func_1514'] = func_1514
mod = relay.transform.InferType()(mod)
output = func_1514()
func_1515 = relay.Function([], output)
mutated_mod['func_1515'] = func_1515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1076_call = mod.get_global_var('func_1076')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_1596 = relay.TupleGetItem(func_1076_call(), 2)
call_1597 = relay.TupleGetItem(func_1077_call(), 2)
func_268_call = mod.get_global_var('func_268')
func_271_call = mutated_mod.get_global_var('func_271')
var_1627 = relay.var("var_1627", dtype = "int64", shape = ())#candidate|1627|()|var|int64
call_1626 = func_268_call(relay.reshape(var_1627.astype('int64'), []))
call_1628 = func_268_call(relay.reshape(var_1627.astype('int64'), []))
output = relay.Tuple([call_1596,call_1626,var_1627,])
output2 = relay.Tuple([call_1597,call_1628,var_1627,])
func_1631 = relay.Function([var_1627,], output)
mod['func_1631'] = func_1631
mod = relay.transform.InferType()(mod)
mutated_mod['func_1631'] = func_1631
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1632 = relay.var("var_1632", dtype = "int64", shape = ())#candidate|1632|()|var|int64
func_1631_call = mutated_mod.get_global_var('func_1631')
call_1633 = func_1631_call(var_1632)
output = call_1633
func_1634 = relay.Function([var_1632], output)
mutated_mod['func_1634'] = func_1634
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1648 = relay.var("var_1648", dtype = "uint16", shape = (12, 12, 14))#candidate|1648|(12, 12, 14)|var|uint16
var_1649 = relay.var("var_1649", dtype = "uint16", shape = (12, 12, 14))#candidate|1649|(12, 12, 14)|var|uint16
bop_1650 = relay.greater(var_1648.astype('bool'), relay.reshape(var_1649.astype('bool'), relay.shape_of(var_1648))) # shape=(12, 12, 14)
output = bop_1650
output2 = bop_1650
func_1653 = relay.Function([var_1648,var_1649,], output)
mod['func_1653'] = func_1653
mod = relay.transform.InferType()(mod)
mutated_mod['func_1653'] = func_1653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mutated_mod.get_global_var('func_1653')
var_1655 = relay.var("var_1655", dtype = "uint16", shape = (12, 12, 14))#candidate|1655|(12, 12, 14)|var|uint16
var_1656 = relay.var("var_1656", dtype = "uint16", shape = (12, 12, 14))#candidate|1656|(12, 12, 14)|var|uint16
call_1654 = func_1653_call(var_1655,var_1656,)
output = call_1654
func_1657 = relay.Function([var_1655,var_1656,], output)
mutated_mod['func_1657'] = func_1657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1662 = relay.var("var_1662", dtype = "int64", shape = (6, 4, 4))#candidate|1662|(6, 4, 4)|var|int64
var_1663 = relay.var("var_1663", dtype = "int64", shape = (6, 4, 4))#candidate|1663|(6, 4, 4)|var|int64
bop_1664 = relay.bitwise_or(var_1662.astype('int64'), relay.reshape(var_1663.astype('int64'), relay.shape_of(var_1662))) # shape=(6, 4, 4)
uop_1674 = relay.cosh(var_1662.astype('float64')) # shape=(6, 4, 4)
output = relay.Tuple([bop_1664,uop_1674,])
output2 = relay.Tuple([bop_1664,uop_1674,])
func_1677 = relay.Function([var_1662,var_1663,], output)
mod['func_1677'] = func_1677
mod = relay.transform.InferType()(mod)
mutated_mod['func_1677'] = func_1677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1677_call = mutated_mod.get_global_var('func_1677')
var_1679 = relay.var("var_1679", dtype = "int64", shape = (6, 4, 4))#candidate|1679|(6, 4, 4)|var|int64
var_1680 = relay.var("var_1680", dtype = "int64", shape = (6, 4, 4))#candidate|1680|(6, 4, 4)|var|int64
call_1678 = func_1677_call(var_1679,var_1680,)
output = call_1678
func_1681 = relay.Function([var_1679,var_1680,], output)
mutated_mod['func_1681'] = func_1681
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1688 = relay.const([[[1,-10,5,10,-8,-3,-9,4,4,7,1],[-1,-5,3,-9,6,10,3,-9,-3,7,-10],[9,-2,5,1,5,-4,10,-10,10,1,9],[-5,8,-7,-4,-3,1,7,5,4,1,-10],[-5,-2,-4,5,6,2,-10,10,8,-10,-9],[8,5,5,2,-7,-4,2,-1,-3,-10,2],[6,5,-7,4,2,-3,-6,2,-4,6,7],[7,-6,-8,7,-8,4,-8,8,1,6,6],[-2,1,-7,-3,-5,-6,-3,9,4,3,-9],[-1,5,-9,-5,4,-3,-3,-1,9,-9,9],[7,1,3,1,7,3,5,-2,6,10,-2],[-2,-9,1,5,-1,-7,-6,-10,-6,-1,8],[8,-8,7,-6,9,4,-6,-8,-4,-3,-1],[3,8,-8,-6,-4,-8,1,-8,-6,2,7],[-4,10,1,-9,6,6,9,10,-2,-2,-9],[-8,9,-6,-4,10,7,6,-7,4,6,5]],[[4,1,-2,-6,5,9,-8,6,7,9,-7],[-4,1,6,-8,3,8,7,8,-2,7,-8],[6,8,9,1,-4,10,5,-3,1,-4,-1],[-1,-6,5,-6,-10,-8,-10,-6,4,-8,-5],[4,-5,-5,4,-3,6,-9,5,-3,-10,5],[-9,10,3,10,10,-8,-9,-5,-9,-7,8],[-4,-1,-9,-2,-8,-7,6,8,-10,2,-3],[-10,-3,5,-2,5,-5,6,5,10,7,-6],[7,-1,-10,6,-3,10,-5,-3,7,4,-4],[7,6,-5,-5,8,-4,-1,-1,6,5,-7],[2,-5,9,4,-10,5,8,-9,-2,7,5],[8,6,9,3,-10,-5,5,-6,9,10,2],[-3,-3,9,1,-9,-1,5,6,5,5,5],[-5,-1,-7,-10,10,-1,10,-2,-5,10,-6],[7,4,-10,-3,9,5,4,-10,2,-8,1],[-2,-9,-4,4,-5,-1,-4,-6,-3,-7,-4]],[[2,-7,-3,5,3,9,-6,-10,-4,-5,3],[-4,-6,-5,-7,6,-4,4,-10,-5,8,-6],[8,7,2,-7,-1,4,-9,-2,2,8,1],[-5,-10,-3,-6,-3,6,6,-1,-2,3,-10],[7,-3,-10,-6,2,1,4,2,-4,6,-4],[7,-7,-10,5,5,1,-2,10,3,1,-7],[1,-7,-2,-6,-5,-6,4,-5,5,2,9],[-9,3,-2,-10,-9,8,-6,7,9,-7,-6],[-10,-9,-10,-2,-6,-9,-5,-3,-2,5,-6],[-10,-3,7,-5,-10,-4,9,3,-5,4,-9],[-5,-5,-5,-6,-1,6,-7,-3,-5,-9,-5],[3,2,6,1,9,6,-2,-4,1,-7,9],[-7,-8,9,-1,8,10,-1,-7,10,8,-10],[6,-1,9,-4,-3,3,5,-1,-6,-4,10],[-3,-8,3,-10,8,-4,4,8,4,-1,5],[10,-6,-6,5,6,2,-10,9,7,7,-8]],[[-7,-1,10,-7,-9,4,5,8,5,-5,-7],[6,-6,-7,6,-4,-2,3,6,-10,9,4],[1,2,-5,6,4,2,-5,-5,-4,4,-5],[-9,-7,7,10,-9,-5,-10,-8,4,10,-5],[5,-6,8,-7,4,-5,-5,-8,6,-10,8],[3,8,-1,-3,1,-6,-9,4,-9,-1,3],[7,-3,-9,-5,-2,-5,6,-7,2,-9,5],[-3,1,1,-6,-8,-8,-5,-1,-5,9,-3],[8,3,8,-8,-9,3,-3,-2,9,-2,-10],[-3,9,5,-10,10,8,7,5,-8,6,-6],[4,-8,7,-9,6,1,-1,-3,5,-10,9],[7,-5,-10,-4,2,4,2,-1,-2,4,4],[8,-8,-3,5,6,-7,7,-3,-4,1,-6],[-1,6,4,5,-5,5,7,2,9,-2,-2],[-4,1,2,7,-7,-5,-4,-2,8,3,3],[-1,-1,-6,7,-3,-2,10,-8,-4,-9,-7]],[[9,-3,7,10,5,-6,10,-9,-9,-9,-9],[-7,-9,-2,-7,1,-6,-2,-10,4,4,2],[-3,2,-5,5,1,1,-2,-8,1,6,4],[2,-10,9,-10,7,-4,-7,9,7,3,-10],[2,-3,-7,-10,-9,-7,9,-3,9,-2,1],[5,3,-2,1,-1,-1,-4,7,3,6,-3],[8,-4,9,1,7,-2,10,-7,9,4,4],[10,1,7,3,-2,7,-7,4,-8,6,9],[7,6,4,6,5,-1,-9,-6,8,3,-6],[4,8,8,4,-9,1,-5,-3,-5,8,7],[-4,-2,-10,10,3,5,5,-5,-9,10,-8],[-7,7,-9,7,4,10,-4,9,8,7,5],[-5,1,-5,-5,5,3,-5,-6,-10,-4,6],[-3,-1,7,2,-9,2,-2,2,-9,-1,-10],[-7,-9,-9,-7,8,-8,-9,-6,-8,-10,7],[-9,-1,-8,1,1,4,-6,2,6,3,10]],[[2,7,-10,-2,10,8,8,-6,-1,10,8],[8,9,-9,-9,-8,-4,1,-1,3,-2,3],[-6,-2,7,-2,-6,-4,-4,9,1,-4,-2],[8,-8,5,3,-2,8,-8,6,1,-2,-8],[7,2,7,-2,3,-2,-3,4,4,7,-10],[8,-4,-9,-5,5,-8,-7,-4,-2,9,9],[1,-7,9,-9,-8,-6,-8,-9,6,3,10],[7,-1,1,4,-1,3,-10,-4,1,7,-6],[-6,10,-10,4,-4,-4,-1,-4,-4,2,5],[-10,-2,-2,-2,-6,3,8,8,3,-4,-7],[-1,2,6,-5,-7,-9,-7,7,-9,-8,8],[6,-10,8,-8,-1,-5,-6,-8,-3,5,-3],[5,6,5,-6,1,-9,-3,-7,3,7,4],[3,4,6,-8,-6,8,-4,-5,6,-4,-7],[3,5,-5,-7,8,10,6,3,-2,6,10],[-5,-2,-1,7,3,-3,7,3,-6,4,4]],[[9,-3,-6,-4,-8,-1,9,7,9,5,10],[-1,-6,5,2,-7,7,-3,6,1,-6,6],[-4,9,-5,-9,-6,10,-7,9,2,-10,5],[-2,-1,-9,-5,2,10,-7,6,1,-4,2],[-6,1,-9,7,-4,-9,1,-4,2,8,-7],[-6,10,-7,-8,6,-1,2,-7,6,-5,8],[2,4,8,-6,6,-2,-9,1,-9,3,-5],[2,1,3,4,4,3,-9,-10,10,7,2],[-10,-5,-1,8,3,-8,-9,-4,2,10,6],[10,6,-3,9,-1,8,5,6,7,-5,-4],[6,7,6,5,9,-9,3,-8,-7,1,-6],[-9,4,-10,9,-3,-3,-2,8,-2,-3,1],[-5,10,9,1,2,8,4,-4,1,9,-8],[3,-10,-4,-8,-3,-6,-6,8,2,5,-7],[5,3,9,-2,-5,-4,3,-10,-2,3,7],[5,-7,7,-5,3,6,-10,10,-1,-8,-9]],[[-2,2,-3,-4,-8,-6,-5,9,7,-2,9],[-7,5,-3,-4,5,-3,-2,4,7,-4,-7],[5,-3,-9,5,-6,-9,2,-5,4,4,7],[-4,-1,-2,-1,8,-8,-8,5,-7,6,3],[7,4,-5,1,-4,2,-5,2,5,3,8],[-10,-5,-3,2,6,-1,-1,1,-8,-6,-10],[-5,6,-2,-3,10,-5,-2,-3,6,4,-4],[-6,8,7,4,-6,10,9,2,-6,7,7],[-10,4,4,3,-4,10,-3,-5,-4,8,-4],[10,10,10,5,-9,-10,3,10,1,-7,3],[7,8,2,9,-2,-3,5,2,-1,-9,3],[-4,-9,4,-7,7,8,9,-1,5,9,10],[1,6,-2,-2,6,-5,-2,-1,9,-5,3],[-6,-2,2,10,5,-1,-1,5,-7,1,8],[-2,-4,-6,5,-3,-4,3,-6,7,2,2],[10,-1,2,8,7,8,-8,-10,-2,5,8]],[[3,10,-5,7,-10,-9,-3,-10,1,-2,9],[-3,-4,-4,4,-10,5,-4,-2,2,-9,2],[-1,4,2,-3,5,-1,-3,-1,-6,2,1],[-4,9,7,-6,-10,1,-1,10,-3,-9,8],[-9,9,-10,-7,-8,-3,8,7,-9,2,-4],[3,8,1,-2,1,7,-9,10,-5,-8,9],[10,-1,-6,-1,8,4,-1,5,-3,-9,6],[-5,-5,-9,1,-8,-6,2,-1,-10,-8,-5],[9,-4,-6,-1,10,-1,8,-7,-7,-4,3],[-5,-8,3,1,-6,-6,3,5,4,-1,10],[4,10,4,6,-9,-4,-8,-4,-5,-7,1],[2,-5,-1,3,6,1,-3,-2,-4,10,8],[5,4,2,-10,3,-7,2,5,-9,5,8],[7,-6,1,-1,3,10,-7,-3,5,10,-4],[-10,-10,-1,3,4,1,2,-8,-10,-10,-2],[-5,3,1,-4,8,6,-4,-4,8,8,-7]],[[-1,5,8,6,-4,3,2,3,-8,1,8],[1,-4,-7,10,7,1,-5,-9,6,-3,-3],[4,-3,4,8,-1,3,10,2,-5,1,10],[4,-8,-3,1,8,-1,-10,6,6,-7,-7],[-8,-8,5,-9,-5,4,-5,-6,2,-2,6],[-7,-9,2,-3,-4,-7,6,-2,-4,-9,-2],[-5,1,-2,-2,6,-3,-6,5,-5,4,3],[-1,-6,4,5,-2,-6,-10,7,-7,5,1],[6,-3,-7,10,-7,-7,-7,-2,8,-3,-6],[-3,8,9,-9,-7,8,-3,-8,-7,3,10],[4,2,-6,6,-9,7,8,-1,8,-1,9],[-1,8,-2,1,-3,-5,-5,-2,-5,10,6],[-9,3,6,-4,-2,10,3,5,7,7,4],[5,4,5,-3,2,-10,9,-10,1,-8,-4],[-4,-4,-8,4,-6,-6,-8,-6,5,-5,4],[-1,7,-8,2,7,-2,6,4,10,1,-4]],[[-10,-2,-8,-10,-8,-9,-2,9,1,-9,-7],[-1,-8,-2,-10,8,9,-4,6,1,4,1],[7,9,8,-10,-6,-7,-5,-1,-7,4,-8],[3,4,-8,-4,-4,10,10,5,2,-3,8],[-10,-3,-10,3,7,4,9,-10,2,5,-1],[-8,5,10,9,-3,6,5,5,6,5,-3],[-3,-9,-7,6,9,4,6,-1,-1,3,2],[-7,-8,-1,2,-7,-5,9,3,1,9,-8],[-1,-9,7,4,-4,8,-4,4,3,3,10],[-1,9,-6,9,-3,-7,5,-8,3,1,-1],[2,-3,9,-2,-7,-1,-7,5,3,8,-4],[-1,-5,-4,8,9,3,5,-7,-8,-2,-3],[5,6,-9,7,-1,-6,7,-3,7,6,-4],[-9,-10,7,7,-2,9,-2,4,2,10,-4],[-9,-1,-8,6,10,7,4,1,-4,-6,10],[-3,-9,-4,4,5,4,10,5,-6,-3,4]],[[-6,1,-5,-7,4,1,-5,-2,2,4,7],[8,2,-8,10,4,-6,-8,-9,6,-4,-7],[-2,10,8,10,10,9,5,-8,-9,10,5],[-6,4,-10,-3,-1,-7,10,7,-3,9,8],[1,-10,-8,8,2,-8,8,-7,4,-7,-1],[6,-7,4,3,4,9,4,6,-9,-6,5],[4,6,-9,6,-7,9,-3,2,6,10,9],[1,6,2,-8,9,-8,-7,-7,9,9,-10],[1,-8,9,10,-2,3,-2,1,1,-1,6],[-8,-3,8,6,-6,-3,4,2,8,-9,-1],[6,-1,3,-8,10,-1,4,6,-1,-9,-7],[-4,8,-3,3,-8,-10,-7,-8,4,-10,2],[-6,6,-3,10,7,-8,-8,-4,5,-9,10],[7,-1,-8,8,5,-10,-1,-5,2,-7,-8],[1,5,3,-10,1,1,-10,1,10,-2,-6],[-5,6,-2,10,-7,2,-5,-7,6,-4,-10]],[[-7,-10,10,9,-5,-6,6,5,7,-4,-5],[4,6,3,-8,-4,-5,-3,-6,-10,1,-3],[3,-2,9,1,-5,-9,-6,10,-5,-2,9],[-5,2,-8,-1,-9,-9,9,4,-4,-9,-1],[5,-1,-6,-1,10,1,-3,-4,-8,-1,3],[4,3,8,3,7,3,-6,-2,-5,5,4],[-3,-2,-1,-9,-6,2,5,9,1,3,5],[2,-8,-2,3,1,-6,10,-8,2,3,1],[-5,-3,-8,8,-8,5,-7,1,2,-7,-4],[6,3,-4,-3,4,7,2,-6,3,1,1],[2,10,-5,4,2,-1,-9,3,2,-10,7],[-6,-4,-8,-6,7,-5,4,3,-9,-10,-2],[-5,-3,-6,-8,6,-7,-3,-7,8,-7,-10],[10,10,8,10,-9,7,-6,6,6,-7,2],[10,9,3,8,8,7,-9,-6,-5,8,8],[6,5,5,7,-4,-9,2,10,7,9,-3]],[[-1,1,-7,-9,-2,-8,7,1,-3,8,7],[-7,-1,4,-10,-10,10,-6,-10,-2,10,-9],[7,8,4,-3,-7,9,-5,-1,4,6,3],[-10,9,-7,-4,-5,-6,-1,10,-5,-6,-8],[-9,-8,10,-8,-9,8,-10,4,-1,7,3],[-2,-3,1,-1,-10,8,3,5,-3,-10,10],[-7,-8,-5,-8,2,-1,-4,6,-1,-6,-6],[7,2,6,10,-4,2,5,-6,6,-10,-4],[-9,-10,9,-9,4,-6,5,-8,10,2,-3],[-9,-8,8,-4,-4,5,5,-9,8,-2,2],[10,2,4,-10,-1,-8,4,8,-10,-2,6],[10,-2,1,-7,-1,2,5,-9,5,-3,-8],[-10,-6,-9,-5,6,2,-6,-1,-3,7,8],[-3,6,7,-10,-8,-1,1,5,-9,-3,-8],[-2,-9,-5,-2,8,-10,-3,4,1,-6,-8],[-4,-4,3,-4,6,2,-10,-4,10,8,-6]],[[6,-6,4,9,8,-5,8,2,1,-7,5],[-9,-10,3,-8,8,-1,-9,8,-8,-3,1],[-3,5,-2,6,-8,8,-6,5,-2,-8,-9],[9,-8,6,-10,-5,1,-6,2,2,-8,9],[5,-8,9,9,4,7,-5,-3,9,7,-8],[5,-4,10,-9,-6,3,1,-9,-1,-10,-6],[1,-9,9,-2,-8,7,-6,-6,7,9,-5],[3,-3,-10,5,8,-5,-8,-5,-1,9,-7],[-6,10,-4,-5,-1,6,5,9,-9,-7,3],[9,10,-3,8,4,2,9,-6,8,5,3],[7,1,8,2,-5,-1,1,-6,3,-4,5],[-2,10,-8,3,6,-1,10,6,3,5,6],[8,-6,1,6,7,-7,-10,-1,-6,3,-5],[9,4,-1,-5,-6,1,4,4,-10,-9,-8],[-5,10,-8,-1,5,-2,-3,8,4,-3,-8],[8,6,-2,6,2,1,-3,6,-1,7,9]]], dtype = "uint16")#candidate|1688|(15, 16, 11)|const|uint16
var_1689 = relay.var("var_1689", dtype = "uint16", shape = (15, 16, 11))#candidate|1689|(15, 16, 11)|var|uint16
bop_1690 = relay.subtract(const_1688.astype('uint16'), relay.reshape(var_1689.astype('uint16'), relay.shape_of(const_1688))) # shape=(15, 16, 11)
output = bop_1690
output2 = bop_1690
func_1707 = relay.Function([var_1689,], output)
mod['func_1707'] = func_1707
mod = relay.transform.InferType()(mod)
var_1708 = relay.var("var_1708", dtype = "uint16", shape = (15, 16, 11))#candidate|1708|(15, 16, 11)|var|uint16
output = func_1707(var_1708)
func_1709 = relay.Function([var_1708], output)
mutated_mod['func_1709'] = func_1709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_757_call = mod.get_global_var('func_757')
func_758_call = mutated_mod.get_global_var('func_758')
call_1765 = relay.TupleGetItem(func_757_call(), 0)
call_1766 = relay.TupleGetItem(func_758_call(), 0)
var_1775 = relay.var("var_1775", dtype = "int64", shape = (3, 13, 2))#candidate|1775|(3, 13, 2)|var|int64
bop_1776 = relay.less(call_1765.astype('bool'), relay.reshape(var_1775.astype('bool'), relay.shape_of(call_1765))) # shape=(3, 13, 2)
bop_1779 = relay.less(call_1766.astype('bool'), relay.reshape(var_1775.astype('bool'), relay.shape_of(call_1766))) # shape=(3, 13, 2)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_1784 = relay.TupleGetItem(func_1393_call(), 0)
call_1785 = relay.TupleGetItem(func_1394_call(), 0)
func_1677_call = mod.get_global_var('func_1677')
func_1681_call = mutated_mod.get_global_var('func_1681')
var_1799 = relay.var("var_1799", dtype = "int64", shape = (1, 96))#candidate|1799|(1, 96)|var|int64
call_1798 = relay.TupleGetItem(func_1677_call(relay.reshape(var_1799.astype('int64'), [6, 4, 4]), relay.reshape(var_1799.astype('int64'), [6, 4, 4]), ), 1)
call_1800 = relay.TupleGetItem(func_1681_call(relay.reshape(var_1799.astype('int64'), [6, 4, 4]), relay.reshape(var_1799.astype('int64'), [6, 4, 4]), ), 1)
output = relay.Tuple([bop_1776,call_1784,call_1798,var_1799,])
output2 = relay.Tuple([bop_1779,call_1785,call_1800,var_1799,])
func_1815 = relay.Function([var_1775,var_1799,], output)
mod['func_1815'] = func_1815
mod = relay.transform.InferType()(mod)
var_1816 = relay.var("var_1816", dtype = "int64", shape = (3, 13, 2))#candidate|1816|(3, 13, 2)|var|int64
var_1817 = relay.var("var_1817", dtype = "int64", shape = (1, 96))#candidate|1817|(1, 96)|var|int64
output = func_1815(var_1816,var_1817,)
func_1818 = relay.Function([var_1816,var_1817,], output)
mutated_mod['func_1818'] = func_1818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_1868 = func_407_call()
call_1869 = func_407_call()
uop_1876 = relay.log(call_1868.astype('float64')) # shape=(3, 13, 2)
uop_1878 = relay.log(call_1869.astype('float64')) # shape=(3, 13, 2)
output = relay.Tuple([uop_1876,])
output2 = relay.Tuple([uop_1878,])
func_1886 = relay.Function([], output)
mod['func_1886'] = func_1886
mod = relay.transform.InferType()(mod)
mutated_mod['func_1886'] = func_1886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1886_call = mutated_mod.get_global_var('func_1886')
call_1887 = func_1886_call()
output = call_1887
func_1888 = relay.Function([], output)
mutated_mod['func_1888'] = func_1888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_1901 = func_407_call()
call_1902 = func_407_call()
output = call_1901
output2 = call_1902
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
const_1932 = relay.const([[[True,True,False,False,False,False],[False,False,True,True,True,False]],[[False,True,True,True,False,False],[True,False,True,False,False,True]],[[True,False,False,False,True,False],[True,True,True,True,True,True]],[[False,True,True,True,False,True],[False,False,False,True,True,False]],[[False,False,True,True,True,True],[False,False,True,True,False,False]],[[True,True,True,False,True,False],[True,True,True,False,False,True]],[[True,False,True,False,False,False],[False,False,True,True,True,False]],[[False,False,False,True,True,False],[False,False,False,True,False,True]]], dtype = "bool")#candidate|1932|(8, 2, 6)|const|bool
var_1933 = relay.var("var_1933", dtype = "bool", shape = (8, 2, 6))#candidate|1933|(8, 2, 6)|var|bool
bop_1934 = relay.logical_or(const_1932.astype('bool'), relay.reshape(var_1933.astype('bool'), relay.shape_of(const_1932))) # shape=(8, 2, 6)
output = bop_1934
output2 = bop_1934
func_1971 = relay.Function([var_1933,], output)
mod['func_1971'] = func_1971
mod = relay.transform.InferType()(mod)
var_1972 = relay.var("var_1972", dtype = "bool", shape = (8, 2, 6))#candidate|1972|(8, 2, 6)|var|bool
output = func_1971(var_1972)
func_1973 = relay.Function([var_1972], output)
mutated_mod['func_1973'] = func_1973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_1994 = relay.TupleGetItem(func_281_call(), 0)
call_1995 = relay.TupleGetItem(func_283_call(), 0)
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
const_2001 = relay.const([[-7,-10,1,5,10,-9,1,9,-4,-3,-8,9,7,-5,-9,3,10,-4,-5,-5,6,-4,-3,-7,3,1,1,1,-7,-10,5,-4,-7,8,-1,9,-8,-4,-5,-8,-5,10,-9,5,-9,-4,-8,-3,-1,7,5,-9,8,-6,8,-3,-2,-6,-6,-9,-6,1,-3,9,5,-8,-9,-7,-2,-1,-6,-3,7,-1,10,10,-5,2,-3,-4,4,-1,10,-1,1,-5,6,7,-7,8,10,-5,-7,5,-7,-10,-2,5,9,6,-10,6,7,1,4,1,-5,1,5,-4,6,3,-5,9,4,5,-4,-2,-6,5,10,6,-4,9,-4,2,-7,7,1,5,1,3,-10,-8,-8,8,1,-7,-2,6,7,5,3,5],[10,-1,-1,8,-1,-10,1,9,4,1,-2,2,-5,3,-1,-1,-10,1,1,5,-8,-1,2,3,7,4,10,-1,4,-4,4,-5,-10,-8,-10,2,-7,-6,-6,7,-4,-5,6,1,9,7,3,-10,10,3,-10,-7,10,7,4,-1,4,3,9,-2,-1,4,10,-6,-1,-2,6,9,3,-3,-10,5,8,6,4,-8,6,9,-5,8,-6,10,-2,-1,4,3,-8,-8,8,8,9,-1,7,2,-6,9,-3,-3,7,-1,8,3,-4,-6,2,-8,-9,7,-8,-9,9,4,6,-6,-3,-2,-3,-9,-5,-1,1,9,8,-6,-4,1,-3,-5,4,10,10,-10,-6,-10,-6,-9,2,-8,5,-9,9,2,6,-10],[9,-2,3,-2,3,-1,6,-7,-9,1,9,5,-1,-1,-4,-9,-5,2,3,9,9,-4,-2,-3,5,9,7,3,8,-7,7,5,-7,9,4,-7,-8,8,-1,4,-7,2,-4,-2,-9,5,4,-5,9,-2,-2,6,9,9,-6,-8,6,7,-2,-2,-9,-6,-9,6,5,-2,7,6,-1,10,9,-2,-7,-3,-9,2,4,-1,-9,10,4,-10,10,-1,-10,-10,-8,-4,-1,-5,-3,-8,-5,9,-5,9,-1,-2,-6,3,3,-6,4,-5,-6,5,7,4,4,9,2,-9,-8,5,-6,-9,2,10,-5,10,5,-9,-9,-6,6,-2,-3,3,-4,5,-7,-8,2,-4,3,6,-9,10,-8,3,-4,-6,8,10],[10,-3,-2,7,-9,10,-4,9,1,-3,10,7,-1,-2,-2,2,-8,8,-7,5,-5,9,-1,-3,2,3,10,-7,-1,-1,-1,-5,-9,10,-8,-4,-10,-10,-5,-1,-9,-8,-4,-1,4,-10,-6,-6,5,-2,1,-4,3,9,-9,3,-7,-4,-6,8,8,4,10,-8,8,-10,10,-9,9,8,-2,-3,-6,4,3,-3,-9,-2,9,-7,-4,5,10,6,5,5,-9,-8,7,-8,-3,1,7,4,5,-4,-8,-4,4,8,-8,-5,-5,-1,-5,3,9,2,7,-4,9,3,7,-6,1,-8,-10,5,8,-6,-6,-4,10,3,-4,-2,-4,-10,4,2,1,4,5,-5,-9,9,-1,-10,-1,-10,1,7,7,-8],[5,-8,-2,-8,-4,-3,5,8,-4,-8,-5,-9,-10,-4,6,-10,4,5,-2,4,-7,9,-8,9,7,-9,6,9,-6,1,-6,1,8,-7,-3,6,-9,-4,-4,-1,10,3,9,10,-4,-7,3,-10,8,-3,8,10,6,4,-7,-1,6,1,-8,5,3,4,-2,6,2,8,9,-9,2,-3,10,-3,1,-6,-6,-3,-2,2,-3,-1,-6,-7,9,-7,1,9,7,-10,6,9,4,9,-1,8,-9,-1,2,-9,-5,-3,10,8,1,-8,-1,-1,1,10,2,5,1,-8,5,-5,8,7,-7,7,-10,-9,4,-5,-1,-8,-5,4,-9,8,-10,4,-10,-5,-5,-4,-1,-5,2,-1,-5,6,2,-7,-2,4],[-7,-9,-1,-3,-1,9,-2,7,4,-7,-9,-10,-2,-1,-1,6,5,-6,-4,-1,6,6,-6,-3,3,9,4,-2,-8,3,-5,-9,8,7,2,4,-9,7,-5,4,-2,-1,-6,-5,3,-4,-8,-1,6,-8,-7,10,5,1,-10,10,-10,2,-2,-10,6,-5,5,-3,-5,3,3,8,-1,-10,4,6,-10,9,5,9,3,8,-10,-1,1,-7,-7,6,1,-10,-5,8,5,7,9,3,-10,10,-3,-4,-6,3,-3,-1,5,9,10,-3,-7,6,6,7,-2,7,1,4,-2,1,5,2,-5,-8,-10,-9,3,2,5,-7,-8,4,6,7,4,5,-9,-9,-8,9,-10,-5,-6,-6,8,-9,10,8,-1,3],[-2,-5,5,-5,-1,-1,5,-7,4,-3,7,-1,-5,-2,-3,-4,-5,-7,-2,-5,9,5,-3,6,-4,-2,-10,9,-3,4,9,-2,-4,7,1,9,10,-5,-6,2,9,4,-8,-7,-5,-6,8,1,7,9,1,-10,-4,6,8,-2,6,6,-9,7,-3,-8,-3,4,8,7,-3,-2,4,5,-8,8,-2,-9,9,-5,-1,5,4,3,5,1,9,-3,3,-4,6,6,6,9,3,10,-6,9,4,-2,-4,-7,8,5,-9,-4,-10,-4,-8,-2,6,-9,6,-4,10,1,1,-4,-9,2,-9,-4,-7,-5,-3,7,8,-4,4,7,8,-5,-8,-9,9,7,-6,-6,9,-9,6,-4,4,1,7,-9,5,-3],[-4,-10,-4,2,7,-4,-7,1,-10,2,-2,-1,8,-6,-5,-6,3,-3,-2,-8,3,5,6,-5,-8,2,9,-3,-5,-2,9,-1,-3,-1,9,3,-3,4,-2,-8,8,-2,-5,-4,3,-1,3,7,6,2,-9,-1,-1,6,4,6,5,-8,5,1,7,10,-3,5,-7,9,2,-2,5,-8,1,-2,4,-7,2,-8,-1,7,7,7,9,-2,6,-3,2,-3,-7,-1,4,1,7,5,8,-2,-5,9,-5,-6,6,5,3,3,2,1,2,-4,-1,-7,-2,-4,-9,5,-5,-6,-2,-1,8,5,7,-8,9,-10,-2,9,-7,2,-7,2,10,5,1,-7,9,1,-1,7,-10,2,3,7,-6,7,-8,5],[9,9,7,10,-9,4,-1,-4,7,2,-9,9,8,1,5,3,8,-5,-8,-3,-8,-1,-9,10,10,5,3,-7,9,8,-5,-9,2,10,-9,-1,1,5,-4,5,9,5,3,2,1,-6,-10,9,-9,4,-3,6,-4,5,8,-5,-9,8,4,2,1,-2,-2,-2,2,-8,10,1,7,-5,-6,-1,-1,-7,-10,-10,8,9,-3,-1,-1,-1,5,7,8,6,-2,-10,-7,-10,7,-5,4,-3,8,-3,4,-10,-8,10,8,-1,-4,-7,-10,-9,9,-2,-9,1,10,8,7,-1,-4,-2,-9,-7,6,6,-3,4,9,4,-2,9,8,-6,-5,2,9,4,-7,-1,-6,-2,3,10,4,2,-10,10,8,5],[-6,-3,-10,-3,1,-1,-2,-6,1,-7,-2,2,9,2,-1,-1,1,-10,-4,-8,-8,1,-2,-6,-5,-7,-3,-10,5,2,-8,-1,-10,10,5,-8,-8,6,8,-2,-9,3,-2,-6,7,-2,-4,4,5,7,-1,-4,6,9,-4,-10,-4,6,-5,2,2,-7,-7,8,4,-4,10,3,10,1,-7,-10,1,-6,6,-10,-3,5,-7,-4,8,-5,-7,-4,4,-4,4,1,-8,6,6,4,-5,9,-2,5,2,8,-10,-10,-8,5,-8,1,-3,2,3,9,5,-1,5,-6,-6,8,-7,-10,3,-8,2,-7,-6,-6,-4,-8,7,7,5,-8,-8,-9,-5,1,-8,6,-10,-7,-1,5,10,-6,5,8,7,-3],[4,-9,4,-4,-8,-2,-5,-5,4,4,5,2,3,10,-5,4,-8,8,-2,-4,-5,1,7,-6,7,-4,2,-10,5,-5,-6,10,10,6,2,-2,-6,7,-10,4,-7,-8,4,1,10,2,3,-10,1,6,-5,10,-3,5,-2,-9,-7,5,6,3,-4,-4,6,-1,-9,8,-5,-7,5,-2,-3,7,7,-5,2,9,-2,2,-6,-5,-9,-10,1,-3,-1,7,-5,6,-8,6,-9,-3,-7,-9,7,-7,6,1,7,8,-10,-2,9,8,10,-7,-9,10,-7,-9,10,1,5,5,-7,-8,8,-1,-1,-4,10,-8,4,-5,6,5,9,-3,-9,6,1,-10,-5,4,7,7,-1,-8,-4,8,-6,5,1,2],[6,6,2,-4,7,5,8,-5,8,6,6,-1,8,-10,5,9,-9,-9,-2,-2,-3,-5,10,3,-3,9,4,-4,9,1,5,7,4,-7,-1,5,7,-8,-10,-4,-2,2,4,-8,1,6,9,2,-9,2,-9,5,-7,-10,4,9,8,1,9,-4,7,6,3,-1,-8,-4,10,-2,4,5,7,-3,-9,-4,4,-9,-10,-8,5,-7,2,2,3,-10,-8,-7,3,8,6,2,-2,2,-8,-4,2,7,-7,8,5,-8,-7,7,-5,-1,7,-1,-4,10,5,-6,9,1,-4,-5,10,-3,-8,-6,3,2,-1,-8,5,-9,-6,-5,10,-1,8,-5,-9,3,9,10,7,2,2,6,-2,6,-2,2,-9,-8],[9,5,-4,-5,8,-4,7,4,8,7,-7,-7,-7,2,-10,-3,6,6,6,2,9,10,2,5,6,-3,8,3,-8,1,7,-8,-4,4,10,-4,4,4,8,9,5,8,-1,-7,7,-9,-4,9,3,-7,-3,-3,7,-4,-9,10,4,-7,8,-4,-4,9,-9,-5,4,-7,-3,2,10,-6,9,-2,3,-8,5,-5,-4,-6,-3,-7,-1,1,-7,-7,-1,5,-8,-4,8,5,3,-4,-4,-2,-1,5,-5,9,1,8,-6,5,2,8,-3,-7,3,-5,-2,-6,-6,-7,9,-3,-2,6,6,4,3,1,-7,2,10,6,4,8,-5,9,1,-6,-4,10,4,-9,-10,-2,-9,-4,2,2,6,-6,-5,6],[-8,10,7,-2,-8,7,-1,2,3,-10,9,-3,-2,-7,3,-6,8,-4,7,-5,7,10,10,10,9,-10,-2,5,-1,4,8,6,-5,2,-6,-5,-8,3,-9,3,4,6,6,1,-6,1,4,-1,-8,9,9,-9,10,-6,8,7,-3,-8,-6,6,6,5,7,-9,10,-10,-3,-7,2,2,-5,2,3,6,-2,1,-10,-8,-4,-3,-6,-3,-4,1,-6,-8,3,-8,3,-6,-6,1,-7,4,-7,-8,-10,1,3,-1,-7,1,-2,-6,3,-8,-1,5,-9,9,-6,8,-10,-1,10,-2,-5,-7,-2,-10,5,3,8,-5,-7,-4,3,-8,-10,4,2,-9,10,4,8,-6,1,-10,9,7,-10,-8,2,4]], dtype = "uint16")#candidate|2001|(14, 144)|const|uint16
call_2000 = func_1653_call(relay.reshape(const_2001.astype('uint16'), [12, 12, 14]), relay.reshape(const_2001.astype('uint16'), [12, 12, 14]), )
call_2002 = func_1653_call(relay.reshape(const_2001.astype('uint16'), [12, 12, 14]), relay.reshape(const_2001.astype('uint16'), [12, 12, 14]), )
output = relay.Tuple([call_1994,call_2000,const_2001,])
output2 = relay.Tuple([call_1995,call_2002,const_2001,])
func_2003 = relay.Function([], output)
mod['func_2003'] = func_2003
mod = relay.transform.InferType()(mod)
mutated_mod['func_2003'] = func_2003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2003_call = mutated_mod.get_global_var('func_2003')
call_2004 = func_2003_call()
output = call_2004
func_2005 = relay.Function([], output)
mutated_mod['func_2005'] = func_2005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_2049 = relay.TupleGetItem(func_281_call(), 0)
call_2050 = relay.TupleGetItem(func_283_call(), 0)
uop_2066 = relay.sinh(call_2049.astype('float32')) # shape=(3, 13, 2)
uop_2068 = relay.sinh(call_2050.astype('float32')) # shape=(3, 13, 2)
func_648_call = mod.get_global_var('func_648')
func_650_call = mutated_mod.get_global_var('func_650')
call_2069 = func_648_call()
call_2070 = func_648_call()
bop_2072 = relay.power(uop_2066.astype('float64'), relay.reshape(call_2069.astype('float64'), relay.shape_of(uop_2066))) # shape=(3, 13, 2)
bop_2075 = relay.power(uop_2068.astype('float64'), relay.reshape(call_2070.astype('float64'), relay.shape_of(uop_2068))) # shape=(3, 13, 2)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_2078 = func_407_call()
call_2079 = func_407_call()
func_2003_call = mod.get_global_var('func_2003')
func_2005_call = mutated_mod.get_global_var('func_2005')
call_2081 = relay.TupleGetItem(func_2003_call(), 1)
call_2082 = relay.TupleGetItem(func_2005_call(), 1)
output = relay.Tuple([bop_2072,call_2078,call_2081,])
output2 = relay.Tuple([bop_2075,call_2079,call_2082,])
func_2083 = relay.Function([], output)
mod['func_2083'] = func_2083
mod = relay.transform.InferType()(mod)
mutated_mod['func_2083'] = func_2083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2083_call = mutated_mod.get_global_var('func_2083')
call_2084 = func_2083_call()
output = call_2084
func_2085 = relay.Function([], output)
mutated_mod['func_2085'] = func_2085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_2089 = relay.TupleGetItem(func_281_call(), 0)
call_2090 = relay.TupleGetItem(func_283_call(), 0)
output = call_2089
output2 = call_2090
func_2097 = relay.Function([], output)
mod['func_2097'] = func_2097
mod = relay.transform.InferType()(mod)
output = func_2097()
func_2098 = relay.Function([], output)
mutated_mod['func_2098'] = func_2098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_2099 = func_407_call()
call_2100 = func_407_call()
const_2147 = relay.const([[[-1.817005,-8.744400],[-6.422125,5.106821],[-6.960724,3.467487],[-3.893964,0.799838],[-7.936131,-4.740075],[-7.078044,5.563431],[-0.530546,-3.736775],[2.807869,2.645788],[0.388674,1.153049],[-5.822924,7.994307],[1.742984,-0.334540],[-0.591055,6.180345],[-5.446539,9.662232]],[[-6.251341,3.931454],[-3.763151,-0.782107],[0.435697,2.912605],[7.875998,8.816368],[4.535836,1.617933],[3.641332,-0.620217],[5.298248,-0.757498],[4.899830,6.145282],[-0.677962,3.501087],[-5.756947,-8.193153],[1.798157,-6.036326],[-1.519648,-2.657258],[8.888032,1.241127]],[[-4.282214,-2.628954],[2.985800,0.285615],[-6.023702,-3.543591],[-2.664388,9.232683],[-6.162539,-7.164260],[5.776391,-2.752520],[-7.393613,4.979929],[-0.489850,-7.457490],[-8.574798,7.312507],[9.561009,9.997792],[5.273439,0.243202],[3.365903,-9.363930],[-4.137512,7.670527]]], dtype = "float32")#candidate|2147|(3, 13, 2)|const|float32
bop_2148 = relay.maximum(call_2099.astype('uint8'), relay.reshape(const_2147.astype('uint8'), relay.shape_of(call_2099))) # shape=(3, 13, 2)
bop_2151 = relay.maximum(call_2100.astype('uint8'), relay.reshape(const_2147.astype('uint8'), relay.shape_of(call_2100))) # shape=(3, 13, 2)
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
const_2153 = relay.const([-2,-4,4,-1,8,-9,10,-5,1,2,-5,-3,10,3,9,-6,1,-10,-5,3,10,-6,-2,-9,-9,6,-6,5,8,9,-1,10,4,-8,3,-10,3,-3,1,9,-7,-3,5,10,-5,-1,-3,-10,-1,3,8,-6,3,6,-3,3,-2,-2,4,2,-10,-8,4,-9,-4,10,8,-5,-7,-7,7,-10,-4,-8,6,-8,5,-9,-3,5,-1,-1,10,1,6,8,8,2,2,-10,2,-5,3,-5,2,-6,-2,3,-3,-1,-4,2,-7,-4,4,7,2,-2,-8,1,-4,3,6,-2,-2,-7,2,-8,4,7,-6,6,10,2,5,-6,-2,9,-4,-6,1,-3,-3,-1,-5,-4,7,-8,10,-3,-5,5,9,-7,4,9,5,10,7,4,2,-2,10,5,1,-4,-8,-6,-3,-10,-4,-4,-3,6,6,1,-10,6,-2,-9,-1,-9,-3,6,8,3,-4,-3,-1,-6,-1,-6,9,-10,-5,4,-1,6,10,10,-7,1,1,-8,-7,9,3,-10,7,5,-6,-9,4,10,7,-3,2,6,2,-6,-2,8,2,10,-7,-3,-4,1,-10,-1,1,-1,-9,-8,3,-1,-1,-2,4,-2,5,-3,2,6,-5,8,2,-10,-8,-4,-2,-8,2,4,10,-9,5,-5,-6,-6,-7,-8,6,9,-6,-5,-6,9,-2,5,1,8,-6,1,-3,4,3,-8,9,3,10,4,-10,5,-6,-4,4,2,-7,1,-4,-2,8,8,-9,5,-8,7,-1,-7,-3,-3,3,7,2,9,-5,-5,-1,2,-1,-9,-5,-6,-9,3,-4,-2,-4,8,-9,2,-8,-8,-9,10,9,-10,8,-1,6,10,2,6,1,4,3,-7,-4,-1,-7,-2,2,9,7,-6,5,3,-10,-3,-5,4,-2,8,-3,-8,1,7,3,5,7,3,9,-7,-8,-3,-7,10,5,-5,10,1,3,-7,5,6,-3,-3,-6,-3,-1,7,3,-7,-9,7,8,-1,5,9,1,-1,6,-1,4,-9,10,5,5,-2,-6,4,-8,-7,6,-4,-3,3,8,-4,-8,9,8,3,-8,10,5,-8,-10,5,-10,2,3,3,-7,-4,-9,-5,7,-4,5,8,7,-1,2,-2,-7,8,-10,-3,-7,4,-2,-6,-8,-3,-2,3,9,-6,-1,5,-3,-2,-3,1,-2,9,5,2,-4,6,-5,7,2,5,4,-5,-3,9,2,8,-7,9,-10,5,5,10,-2,-4,-10,10,-10,-10,-2,1,-3,7,5,1,-6,-9,-8,2,8,4,6,-4,9,-1,7,4,-10,7,6,1,4,4,3,-4,2,2,4,-8,4,-5,-1,10,-9,-9,6,-6,3,4,5,-8,-8,7,-8,6,-6,10,9,1,8,-10,1,3,-7,2,7,-9,10,-8,2,-10,-6,-6,-2,-10,8,-3,7,2,6,-5,4,9,-9,4,-4,8,9,-2,10,3,1,6,3,3,-4,4,10,3,2,-1,-4,-4,-2,5,-8,9,-4,9,-4,7,-1,-5,-6,-10,-6,5,-1,-4,-7,6,-5,7,9,9,10,-1,-8,-2,5,-1,5,10,4,9,-2,7,10,-9,9,4,3,-10,4,-3,6,-9,-1,8,-4,9,4,5,9,4,-1,9,8,7,3,-10,-6,-1,1,-2,-8,10,6,-7,1,-5,2,8,-3,-1,-5,-7,-3,7,10,8,2,-2,-5,-3,10,1,-2,-1,4,-3,-6,-9,1,-2,7,10,8,-8,-3,-1,1,-7,1,-7,-2,5,3,7,-1,-6,9,-8,2,-3,-8,-7,4,-1,-4,1,1,3,9,-9,-1,9,-2,8,-4,8,3,1,3,-4,2,-2,1,-8,-5,1,1,5,-8,1,4,-3,7,8,-8,7,-10,-3,-4,1,8,-7,-1,-4,7,-10,7,10,9,-5,2,9,1,-3,2,4,6,-9,-4,-6,10,-4,9,-10,3,7,7,7,9,3,-6,1,10,10,5,-5,-2,-2,2,-1,-9,-10,6,6,-9,-7,8,8,-8,-2,-6,7,-7,-3,3,5,4,-2,-3,8,-9,-7,-2,5,-5,2,7,3,10,-4,-10,9,-2,-8,9,-7,2,-3,8,6,-8,-9,10,8,8,7,1,-5,6,10,-7,2,-10,6,5,-5,10,10,6,4,-2,-5,6,7,-1,-7,-3,-8,6,-3,5,5,-2,9,-3,-3,3,-9,5,-3,5,5,-9,-3,8,-5,3,-10,5,2,-2,4,-10,6,-10,-2,-9,3,1,-4,-1,3,10,-9,-3,-6,6,10,-4,-3,-7,9,5,5,-9,6,9,6,-5,8,-5,-4,-4,-9,3,3,9,6,-8,-2,2,-7,-7,4,-7,9,7,-3,8,-1,5,10,10,10,9,-4,-7,-1,3,8,10,-4,-1,-9,-10,-1,-8,1,-9,5,10,-8,-10,5,6,5,-1,2,7,-4,-4,2,-9,10,-3,-5,-2,-3,-4,8,-2,-6,4,-8,1,-10,8,-9,-6,-5,3,3,3,-10,4,6,2,10,2,-1,-9,-8,-2,4,-5,8,-10,-3,-4,-1,2,-4,-1,-2,-2,4,3,-8,10,-4,4,-2,2,-9,-10,-5,-10,-9,-5,2,6,-9,-1,-6,3,-5,-4,1,-4,-2,-3,-9,8,-1,-10,8,-2,-7,-6,-3,6,5,-5,-6,7,3,5,-10,-9,3,8,7,10,3,8,-4,6,-4,4,-9,-8,-10,6,5,4,7,9,4,-10,5,4,4,-9,-2,10,5,-8,10,-8,9,3,4,2,3,-6,1,8,-2,4,9,7,-2,10,7,7,9,-4,1,-2,9,3,-10,5,-7,5,-5,-3,-7,10,-10,-2,6,4,5,4,-4,3,-9,5,9,5,4,2,-10,5,-9,8,6,-5,-8,4,7,5,6,-1,9,1,-3,-5,5,-2,9,-2,-4,6,5,5,7,-7,9,10,-5,3,5,-10,10,-5,-5,-5,-3,2,-1,1,6,-3,-9,5,5,1,-8,10,-6,-10,-3,2,8,-5,3,-8,-5,6,-5,7,10,2,2,7,-9,7,-2,8,-4,-10,9,6,1,10,-2,8,7,-2,-1,5,8,2,2,1,-10,-3,-10,-5,-10,9,-1,5,-8,-9,8,9,-7,-5,10,6,-8,9,7,-1,10,-10,8,1,6,2,-5,9,3,-2,9,-1,9,5,7,-5,-5,-7,2,-6,7,2,1,3,-5,-7,5,1,9,1,1,2,-1,-6,7,1,2,-6,-5,8,-8,-4,2,-8,-1,-8,3,6,-7,6,6,9,-3,4,-8,9,7,8,1,2,-4,-4,-10,-10,-5,-2,6,-1,-8,8,-7,-9,-10,-6,4,-3,-10,-5,9,9,4,7,5,-8,4,9,4,-8,9,-7,5,1,-7,8,-4,2,-2,-7,-8,2,-2,5,-10,-10,8,4,-7,1,-3,-2,7,4,-2,6,5,-1,-8,-3,-1,9,-10,5,10,-1,-4,-10,6,8,-5,5,-2,-7,5,9,2,-5,3,-10,-3,-5,-4,6,9,6,-8,-3,9,1,9,10,-1,6,3,6,6,3,-6,-2,2,-10,10,3,5,-5,-5,8,10,-10,9,-8,-9,7,-7,2,-6,4,-6,-7,-2,-5,-7,-2,8,-9,10,-2,-6,6,-9,-7,-3,-10,7,-1,-2,-5,-1,6,-9,-6,2,-7,8,-4,-4,-1,9,5,1,-4,-2,1,-3,5,-4,2,1,-4,5,-8,-8,-3,10,-2,3,5,-4,1,5,-3,6,-5,-5,6,9,-10,-2,-4,2,-5,-4,2,-7,9,-10,-3,6,-5,-8,-2,4,-4,4,1,5,-2,-6,-1,9,7,10,8,-9,-8,4,6,3,-6,-9,4,-3,-5,1,4,-5,3,-2,-1,6,9,-9,-7,4,-1,8,-7,2,-10,7,6,6,7,-10,10,-8,-5,-4,1,-6,9,8,7,-9,2,2,9,-7,7,-5,-5,-7,-1,-3,-7,5,-6,-3,10,3,-7,3,-4,-2,-10,-9,-1,-5,7,5,10,-1,2,1,-7,7,1,10,10,10,1,5,8,-4,-10,9,2,6,8,-7,6,-9,-4,4,-10,-6,-4,5,-2,4,-10,2,7,-6,-9,-9,7,-10,6,-6,6,9,2,-1,3,-6,10,-6,8,-3,-5,10,10,-6,5,5,4,3,-6,-2,-10,3,-8,1,3,3,-8,-3,-6,-7,10,2,5,-2,10,1,6,-3,5,2,-8,7,9,-4,-8,6,2,2,5,-8,1,6,5,2,1,-9,9,5,-5,-5,-10,1,-8,7,8,-8,-5,4,4,-10,-10,-6,-5,8,-1,-3,3,3,6,5,-7,10,-9,-4,2,10,2,-10,-8,-9,1,-10,-5,-6,-4,4,5,-5,-10,-9,-2,-4,-8,3,5,5,-5,10,9,-10,8,6,6,10,-8,-8,-10,7,7,4,-2,-7,7,7,-7,10,-9,-1,-8,2,-1,-8,-3,1,-5,-3,5,5,1,-7,-9,4,-5,-6,7,1,-10,-1,6,-6,-6,-9,1,2,-6,-10,7,-2,10,-5,5,5,9,-10,-7,-5,3,5,-7,-6,7,7,-2,6,6,1,1,9,-1,2,-3,-2,-2,2,3,4,6,5,10,-3,5,10,-9,4,5,-7,-7,-7,-5,2,-9,-9,-8,6,-6,-8,1,6,6,10,-8,-2,-8,-5,9,3,4,6,4,1,1,10,-7,3,-8,7,-2,2,1,4,-7,-2,9,-2,-10,-3,-4,2,-3,9,8,9,8,-1,-3,8,2,-10,8,3,6,-8,3,6,-4,7,-2,3,10,-8,9,-2,6,3,3,-1,-4,-3,-8,4,5,-8,-10,6,7,2,10,8,-3,9,8,6,8,10,-8,9,-6,2,-8,-5,-4,10,8,-1,10,8,1,-10,3,4,2,9,-10,3,1,2,4,1,-1,-4,4,7,-6,-4,-4,-4,-2,8,4,-2,9,2,8,-5,6,8,-1,-5,1,-8,8,3,5,-5,-3,3,3,-5,-9,-9,-2,-6,3,2,1,-9,3,2,-5,6,6,-2,-5,9,9,-8,7,4,5,6,-7,6,8,8,7,-3,-3,1,2,-9,-9,2,1,10,3,4,10,1,-10,-3,-3,9,9,-4,-1,2,2,-8,1,10,3,-5,4,10,5,2,-2,-3,-2,-4,10,2,1,6,7,7,8,2,-9,7,-8,1,-1,-10,1,-5,-9,2,7,1,2,4,1,-3,8,4,10,-7,10,-5,1,-2,4,-2,2,5,-3,-5,4,-7,-1,-10,8,3,5,9,-5,-8,-4,2,-4,-3,5,-3,7,3,3,-8,-3,1,8,-3,10,4,4,2,-10,-6,5,7,-3,10,6,-9,1,-4,-7,-2,10,2,9,-3,1,7,1,7,-4,8,-7,6,6,-8,1,-1,-5,7,1,6,-7,9,7,-10,5,9,-6,1,-7,6,-9,8,-1,2,5,5,1,10,2,-8,-1,-8,-4,-10,7,10,2,-4,5,7,3,1,-10,3,2,-8,10,9,-6,-6,2,1,-6,-9,10,-10,-9,-1,4,10,7,9,5,-3,7,-8,-9,-5,5,-7,-1,9,8,1,-4,-7,1,10,4,-1,-7,1,9,1,1,8,-5,-6,-7,-6,-9,3,1,-10,-9,7,9,9,6,-1,-8,-3,-5,5,-5,4,5,6,3,2,-8,-7,9,-4,-6,5,3,6,-4,-2,3,5,-3,6,8,7,7,2,10,2,-2,-1,-5,-4,9,10,-2,-1,-7,-1,5,10,2,1,-9,-7,1,7,-4,-7,-7,-6,-1,5,6,-4,6,6,-7,1,9,8,-7,-8,-7,5,-1,4,7,-1,-7,-5,-8,-2,-5,10,10,-6,4,-7,6,-7,-10,8,-10,2,3,-10,-8,5,-3,7,-6,10,6,2,-7,10,10,7,-6,-9,6,-1,2,-8,-2,10,-10,7,6,-10,8,2,-8,10,-10,5,8,2,2,5,-7,-2,-5,-4,6,-6,4,2,9,-7,1,-6,-8,9,8,-5,-8,1,4,4,7,-8,-8,-4,4,-7,-5,-4,-1,4,4,2,6,3,9,4,7,-9,-2,-3,6,9,-3,6,-5,-3,10,1,1,8,3,-5,1,5,-9,-8,-10,-8,-2,-7,5,-6,-7,2,2,7,-9,-8,-10,-4,3,6,10,4,-10,-7,-3,1,1,-10,-3,-10,3,5,-1,2,10,7,4,2,-4,-1,3,9,-7,-8,-5,-5,8,-2,8,5,2,9,-5,9,9,6,-4,-7,3,-1,6,9,-7,-7,2,4,3,-1,-4,8,10,5,-9,5,8,2,-4,-9,1,8,7,-9,-7,9,-1,-5,2,-7,10,3,-9,-3,-6,-8,8,10,9,-8,-10,-8,-5,-3,10,-6,-1,-2,5,-7,-10,10,10,5,-1,-6,9,3,-6,1,-6,8,-7,10,-6,7,-2,5,-8,1,-3,-2,2,8,-10,4,5,3,-4,8,-2,7,-1,-7,-3,8,-7,8,-6,7,-5,-1,-5,-2,9,-1,4,-6,10,-4,2,-9,-4,10,5,-5,-10,-1,-3,6,-5,-7,-4,-4,8,9,1,1,-7,7,-8,-2,-1,3,-6,-9,5,7,-1,-6,-10,1,5,9,2,-3,10,-1,6,8,5,2,5,1,-2,-5,2,-4,-7,-8,-10,-1,6,-1,6,-6,-7,10,10,8,-8,6,10,-8,4,-7,-7,-3,2,7,3,10,-2,2,2,3,6,2,9,2,-8,-8,-9,9,-6,9,10,9,-10,3,4,3,-7,-3,-7,-10,6,-9,10,6,6,5,-5,-7,9,8,-8,-3,-6,-9,-3,-7,10,6,5,6,-9,7,-9,-10,4,2,-7,-5,3,-5,5,-7,-7,5,-7,3,-3,-2,5,-1,-10,-9,9,-1,7,9,7,9,3,7,-4,-7,-3,9,1,-6,-2,9], dtype = "uint16")#candidate|2153|(2640,)|const|uint16
call_2152 = func_1707_call(relay.reshape(const_2153.astype('uint16'), [15, 16, 11]))
call_2154 = func_1707_call(relay.reshape(const_2153.astype('uint16'), [15, 16, 11]))
func_1304_call = mod.get_global_var('func_1304')
func_1306_call = mutated_mod.get_global_var('func_1306')
call_2155 = relay.TupleGetItem(func_1304_call(), 0)
call_2156 = relay.TupleGetItem(func_1306_call(), 0)
uop_2183 = relay.sinh(const_2153.astype('float64')) # shape=(2640,)
func_1677_call = mod.get_global_var('func_1677')
func_1681_call = mutated_mod.get_global_var('func_1681')
const_2201 = relay.const([9,-6,-10,7,-9,5,-10,8,10,6,-9,-4,3,-5,4,-8,5,1,-3,5,-7,-7,-3,-7,-5,3,-3,2,4,1,-5,-3,3,6,-2,9,-1,-6,-1,7,7,9,9,-8,-9,3,7,6,7,5,-3,1,-3,10,2,-2,-9,9,-4,-3,5,9,-1,2,-7,9,3,3,9,-2,3,9,6,-10,-6,-5,8,-5,-1,8,5,-7,9,8,7,8,3,2,5,10,-4,4,-9,2,5,-9], dtype = "int64")#candidate|2201|(96,)|const|int64
call_2200 = relay.TupleGetItem(func_1677_call(relay.reshape(const_2201.astype('int64'), [6, 4, 4]), relay.reshape(const_2201.astype('int64'), [6, 4, 4]), ), 1)
call_2202 = relay.TupleGetItem(func_1681_call(relay.reshape(const_2201.astype('int64'), [6, 4, 4]), relay.reshape(const_2201.astype('int64'), [6, 4, 4]), ), 1)
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
var_2213 = relay.var("var_2213", dtype = "uint16", shape = (2016,))#candidate|2213|(2016,)|var|uint16
call_2212 = func_1653_call(relay.reshape(var_2213.astype('uint16'), [12, 12, 14]), relay.reshape(var_2213.astype('uint16'), [12, 12, 14]), )
call_2214 = func_1653_call(relay.reshape(var_2213.astype('uint16'), [12, 12, 14]), relay.reshape(var_2213.astype('uint16'), [12, 12, 14]), )
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_2219 = relay.TupleGetItem(func_281_call(), 0)
call_2220 = relay.TupleGetItem(func_283_call(), 0)
bop_2222 = relay.divide(bop_2148.astype('float32'), relay.reshape(call_2219.astype('float32'), relay.shape_of(bop_2148))) # shape=(3, 13, 2)
bop_2225 = relay.divide(bop_2151.astype('float32'), relay.reshape(call_2220.astype('float32'), relay.shape_of(bop_2151))) # shape=(3, 13, 2)
var_2232 = relay.var("var_2232", dtype = "bool", shape = (12, 12, 14))#candidate|2232|(12, 12, 14)|var|bool
bop_2233 = relay.mod(call_2212.astype('float64'), relay.reshape(var_2232.astype('float64'), relay.shape_of(call_2212))) # shape=(12, 12, 14)
bop_2236 = relay.mod(call_2214.astype('float64'), relay.reshape(var_2232.astype('float64'), relay.shape_of(call_2214))) # shape=(12, 12, 14)
func_1108_call = mod.get_global_var('func_1108')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_2250 = relay.TupleGetItem(func_1108_call(), 0)
call_2251 = relay.TupleGetItem(func_1109_call(), 0)
output = relay.Tuple([call_2152,call_2155,uop_2183,call_2200,const_2201,var_2213,bop_2222,bop_2233,call_2250,])
output2 = relay.Tuple([call_2154,call_2156,uop_2183,call_2202,const_2201,var_2213,bop_2225,bop_2236,call_2251,])
func_2256 = relay.Function([var_2213,var_2232,], output)
mod['func_2256'] = func_2256
mod = relay.transform.InferType()(mod)
mutated_mod['func_2256'] = func_2256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2256_call = mutated_mod.get_global_var('func_2256')
var_2258 = relay.var("var_2258", dtype = "uint16", shape = (2016,))#candidate|2258|(2016,)|var|uint16
var_2259 = relay.var("var_2259", dtype = "bool", shape = (12, 12, 14))#candidate|2259|(12, 12, 14)|var|bool
call_2257 = func_2256_call(var_2258,var_2259,)
output = call_2257
func_2260 = relay.Function([var_2258,var_2259,], output)
mutated_mod['func_2260'] = func_2260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_2270 = func_458_call()
call_2271 = func_458_call()
uop_2280 = relay.cos(call_2270.astype('float32')) # shape=(3, 13, 2)
uop_2282 = relay.cos(call_2271.astype('float32')) # shape=(3, 13, 2)
output = uop_2280
output2 = uop_2282
func_2284 = relay.Function([], output)
mod['func_2284'] = func_2284
mod = relay.transform.InferType()(mod)
output = func_2284()
func_2285 = relay.Function([], output)
mutated_mod['func_2285'] = func_2285
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2293 = relay.const([[[-2.340938,-5.156095,-8.282686,-4.690534,2.117996,2.879829,-6.845348,6.167203]],[[-7.486946,7.869356,-2.692737,8.803624,9.921442,5.578773,-7.017905,5.703435]],[[-8.323498,7.558011,-5.655726,-4.614436,1.137995,0.119242,5.072673,-7.737321]],[[1.013468,4.951014,9.262960,5.037843,-9.206855,-1.429006,9.816152,7.368293]],[[7.707123,-1.053202,1.645835,1.649081,-8.838142,-7.160839,7.871651,-0.654961]],[[-0.351204,-0.176684,-1.792800,-6.919563,-3.495537,7.017813,-6.811637,9.720196]],[[5.318929,-6.718202,6.935121,4.919290,-1.808218,2.255750,9.338535,-1.055368]],[[8.790112,5.937379,-1.916424,-7.738635,1.634145,-6.023498,4.596751,6.156580]],[[3.599582,5.515433,-4.435725,-5.333958,-0.372011,-9.659505,3.396871,3.507265]],[[-9.508719,-0.472348,-3.702840,7.830456,0.464742,0.728242,-9.117970,1.710421]],[[-4.770064,-3.506084,-2.642985,5.863089,-9.513921,-5.644429,-2.288790,-4.598977]]], dtype = "float64")#candidate|2293|(11, 1, 8)|const|float64
uop_2294 = relay.asin(const_2293.astype('float64')) # shape=(11, 1, 8)
output = relay.Tuple([uop_2294,])
output2 = relay.Tuple([uop_2294,])
func_2334 = relay.Function([], output)
mod['func_2334'] = func_2334
mod = relay.transform.InferType()(mod)
mutated_mod['func_2334'] = func_2334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2334_call = mutated_mod.get_global_var('func_2334')
call_2335 = func_2334_call()
output = call_2335
func_2336 = relay.Function([], output)
mutated_mod['func_2336'] = func_2336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2284_call = mod.get_global_var('func_2284')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_2352 = func_2284_call()
call_2353 = func_2284_call()
func_989_call = mod.get_global_var('func_989')
func_990_call = mutated_mod.get_global_var('func_990')
call_2361 = relay.TupleGetItem(func_989_call(), 2)
call_2362 = relay.TupleGetItem(func_990_call(), 2)
output = relay.Tuple([call_2352,call_2361,])
output2 = relay.Tuple([call_2353,call_2362,])
func_2364 = relay.Function([], output)
mod['func_2364'] = func_2364
mod = relay.transform.InferType()(mod)
mutated_mod['func_2364'] = func_2364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mutated_mod.get_global_var('func_2364')
call_2365 = func_2364_call()
output = call_2365
func_2366 = relay.Function([], output)
mutated_mod['func_2366'] = func_2366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_810_call = mod.get_global_var('func_810')
func_812_call = mutated_mod.get_global_var('func_812')
call_2418 = func_810_call()
call_2419 = func_810_call()
func_1653_call = mod.get_global_var('func_1653')
func_1657_call = mutated_mod.get_global_var('func_1657')
const_2430 = relay.const([[3,-5,1,-4,1,1,-8,-5,7,-3,-3,3,6,2,3,8,3,-8,5,3,1,-7,-4,9,-10,-4,-7,8,10,-7,-8,-2,10,7,-1,-5,-4,-3,-5,-10,7,8,10,-7,6,5,1,-6,9,-10,4,3,6,-6,10,-7,-9,1,3,-10,-4,-4,6,9,5,-4,-3,-9,-4,-3,1,1],[5,9,-2,8,8,4,-3,-7,-2,-9,9,5,3,2,-8,-5,-7,-2,5,-6,1,5,10,-10,5,9,-7,9,-2,7,-4,-4,9,9,-3,7,4,8,5,6,7,-4,-10,6,4,4,6,-8,-2,-10,-3,-1,-10,10,-8,7,-2,2,6,7,-3,-9,-7,-5,5,7,2,-2,8,-2,-8,4],[2,5,-5,-1,1,9,-8,-10,10,10,7,6,5,4,9,-5,-3,10,-3,6,10,6,10,10,3,-1,3,8,7,1,-9,8,9,9,10,7,-1,-7,-9,8,-8,-6,8,9,5,3,8,-5,-1,10,10,-3,-2,-9,-1,7,-7,10,-7,5,1,-8,-1,-8,7,-6,-5,7,1,-10,-2,10],[10,-9,1,10,1,-2,5,5,-8,-9,9,-4,-2,3,-1,-7,6,-9,9,-10,-9,5,2,6,-2,-7,-2,3,3,-10,-10,-7,-5,3,6,-6,-6,1,-10,10,-3,-3,5,-1,-4,5,9,8,8,6,5,-1,3,-10,8,-7,6,7,7,-4,-8,3,-10,-1,-4,-4,-9,3,6,6,-3,6],[2,3,-3,10,-5,-9,6,7,7,3,6,-1,-7,-8,-10,2,-10,-3,1,4,-6,4,5,6,-1,-1,2,1,10,4,8,4,-10,-10,-10,-10,9,10,3,9,4,-3,3,10,7,-3,-9,-2,-6,3,-9,4,-4,4,-2,-3,3,3,-4,-7,-6,-6,9,-3,2,-1,-8,9,-9,1,-5,8],[-2,4,-5,-9,-3,-5,4,-7,5,-7,1,4,8,3,-10,3,-3,10,-10,-8,-5,-7,-10,-7,-2,-7,2,-5,7,-6,-9,8,6,10,8,-2,1,-4,-6,8,-9,1,6,-2,3,9,4,6,7,7,3,10,9,-7,-7,10,-1,5,-6,10,4,-3,-9,10,4,3,5,3,7,6,6,10],[-9,-7,-4,4,8,-10,-6,-5,8,-6,-1,-6,1,-4,1,6,-1,-3,-10,4,-6,-5,5,-1,-7,-5,-7,9,-6,-7,-7,5,6,4,8,-3,4,-5,5,-1,4,-3,8,1,4,-9,10,10,3,-9,-4,5,10,7,7,-10,-2,4,-4,4,-2,1,-6,-8,-9,-1,-1,10,-8,9,-3,-8],[1,-6,8,4,-10,4,10,-8,8,9,-8,1,6,-1,8,-5,-3,5,-1,-1,-6,9,-6,-4,-6,4,-3,-10,-2,7,2,10,-5,5,3,-6,-3,-6,2,1,-2,4,9,-4,4,-2,7,10,-4,5,2,-10,-6,4,-8,-8,2,-8,5,-4,5,-5,-6,4,1,1,1,-10,10,7,-9,-8],[6,-1,-10,-9,-9,-9,9,-8,3,4,1,-2,-8,-8,-3,-7,4,9,-3,9,1,10,1,8,7,9,8,10,-10,2,-7,-2,10,-5,8,-6,3,-8,-4,-10,10,9,-3,-3,-9,6,-7,7,10,10,-7,8,2,6,-4,-7,6,-4,6,1,4,9,6,7,-7,3,-3,4,6,-1,6,7],[-5,2,8,-7,3,-4,-4,-6,-7,-7,-1,-6,-2,-9,7,2,-5,-3,10,-5,-8,3,-9,-4,-9,7,-5,6,1,6,1,10,-4,9,5,-6,-3,6,9,10,-3,5,1,-5,-9,2,3,-6,-7,3,-10,-8,10,-7,-5,5,6,-8,-5,9,8,-4,5,9,6,5,-1,-3,8,1,8,3],[-8,-1,6,7,-1,-6,-10,10,7,3,8,-10,-5,10,-7,-7,6,7,8,-5,-4,7,5,9,-3,-1,-8,9,-4,-7,4,7,2,9,8,8,6,-8,-3,5,9,8,9,-1,6,3,3,-9,3,-2,-5,-7,-8,-4,-9,-6,6,-8,-9,7,10,-7,-1,-6,6,9,2,2,8,8,8,-10],[8,-1,-8,4,10,10,10,8,-6,7,3,-8,7,10,10,10,-9,-6,-1,4,-4,3,-10,1,-7,6,10,-1,-7,-2,1,6,-5,7,-3,-7,5,10,-10,1,-9,-7,8,6,7,6,-4,-9,5,4,5,4,3,5,-4,1,5,4,6,-1,-10,2,-9,2,5,1,-9,-1,-8,-8,-5,8],[8,3,2,6,1,5,-7,6,-6,3,2,10,10,-2,6,3,2,6,10,-5,8,-2,8,6,-7,-9,-2,-10,-6,7,4,4,6,7,3,-6,3,-7,-10,-5,3,9,-5,-8,-3,1,-5,-1,-8,-6,2,2,-3,-6,-6,-1,7,4,9,10,-9,9,-9,-6,9,-6,7,6,-10,5,3,3],[-8,-1,1,8,6,5,-8,-10,6,-9,7,4,-8,-1,5,-3,3,1,-9,7,6,1,-4,2,9,2,5,-1,-5,5,8,-4,-4,-6,-3,8,-4,5,10,-9,-9,4,7,8,-8,3,-3,-9,-3,9,8,7,-6,2,-2,-4,-2,-8,4,2,-10,-9,3,9,-5,-1,-8,6,3,-10,9,-9],[-4,3,-2,1,-1,5,10,-9,6,7,8,-8,1,9,3,2,-4,5,-1,8,-9,-5,8,-2,-4,8,10,5,5,-1,2,6,-10,2,9,3,-2,5,-2,4,-5,8,-10,9,8,4,5,6,2,9,5,-9,2,-6,-10,2,7,-5,4,-2,3,-2,7,6,-5,3,6,-8,-6,3,-9,3],[7,-2,-1,-5,4,3,-7,-3,1,-4,-5,-5,9,9,3,3,-10,-2,1,5,5,7,4,-6,-5,2,-5,3,5,3,3,-9,-2,6,-6,-1,9,-5,-9,10,1,7,8,-1,1,-10,-9,1,-10,9,10,-9,9,1,-2,3,2,-9,-8,-3,4,7,-2,7,5,-8,-5,3,-10,1,7,7],[-1,-2,-9,-10,-8,-6,-5,-2,8,-7,-8,6,-9,4,-8,7,-9,10,2,9,-7,10,-10,4,4,-3,-4,-2,8,8,5,5,4,2,-5,6,7,-6,8,-9,3,-5,-2,1,1,6,-5,-3,-8,5,-7,-9,-6,-3,7,9,3,1,10,-7,-1,10,6,5,8,9,-10,10,-5,2,-7,4],[-6,-7,-4,9,7,-1,3,-7,7,-6,6,5,-1,3,-10,7,-1,4,9,1,5,1,10,-10,-5,4,-4,-3,7,-2,3,3,-6,-9,10,-2,-4,4,-10,8,1,-9,2,2,5,6,-7,-2,-6,7,1,-3,-2,-8,1,10,-10,1,-10,-9,8,3,-4,8,5,10,-7,-10,1,-1,-4,6],[-1,-5,-9,6,-10,3,-3,8,6,-6,2,-10,-4,5,6,-1,8,6,10,5,10,-6,6,-2,3,-3,-4,7,-8,7,4,8,3,9,5,-5,-1,9,6,-10,-1,-1,-10,4,-1,-1,-8,8,5,7,1,-7,3,-10,9,-8,-4,5,9,1,10,-6,-3,2,-4,-9,2,-7,-4,-4,6,-3],[-2,6,8,3,1,8,6,3,-10,-4,10,7,-8,-9,2,-9,-8,6,-2,4,8,7,-2,3,5,-4,9,-1,2,-5,9,1,-9,-5,-5,4,1,-1,-4,-6,-2,-3,4,1,-3,-10,-10,-4,-7,-10,8,-10,-9,-3,-5,-3,-3,-9,-2,1,-7,-2,2,-6,2,3,-3,-8,-2,-7,-2,-6],[-7,-10,-5,6,3,-9,-3,2,-10,-5,8,5,-6,8,1,5,-9,8,-7,6,-6,3,-9,-5,1,-3,-5,10,-1,1,2,-1,-10,-7,-7,5,7,3,4,-6,-9,-4,7,10,-2,-9,7,-7,3,4,-6,-3,10,10,3,-8,7,9,-6,4,-9,4,5,5,-3,7,-9,-2,-6,2,2,-4],[-4,5,-3,9,1,10,-3,3,-3,7,1,-2,4,6,5,-5,2,-10,8,-9,-3,3,3,3,-6,-9,-10,6,6,-1,2,10,7,-3,9,2,-8,-9,-2,-8,-3,-9,-9,-8,-7,-5,-7,6,-7,7,-8,10,-5,-8,3,7,-2,-2,1,3,-9,8,-5,9,1,8,6,-7,8,10,-3,9],[7,-6,1,6,-10,-7,-9,5,-4,-3,-10,3,-8,-9,-4,-6,-8,-7,2,1,10,-6,-4,-2,3,-9,8,3,7,-6,-8,1,-5,-9,4,10,7,6,9,10,-5,-7,2,-8,-1,9,-9,7,9,-2,5,-8,9,2,3,-2,-2,1,8,-1,6,-8,10,-10,1,-3,-5,9,-8,4,4,10],[-2,7,10,8,-10,10,4,-3,1,3,9,-2,4,8,1,-1,-7,-4,8,3,-10,2,-3,1,10,-4,6,8,3,6,-4,-8,9,9,5,7,-5,1,1,5,-6,2,4,-3,-4,10,8,-8,-1,-4,9,4,-10,5,9,-5,-7,-8,-7,-10,2,10,10,-8,-4,-7,-6,10,-6,-9,3,1],[-1,2,1,-8,2,4,-5,-2,5,-6,10,6,9,2,-9,3,-3,-7,-7,-7,4,-10,6,-10,1,1,-1,7,4,5,2,3,-3,10,-5,10,10,8,3,-8,-5,-4,-8,8,10,-5,-1,8,7,5,-6,-1,4,4,-7,-2,1,-9,-8,-3,10,3,-4,-5,-8,5,5,2,-7,-9,-9,7],[8,9,4,-6,-9,6,-9,-8,-1,-3,-1,8,-1,2,-5,-10,-6,-8,-2,-5,-3,-6,-3,-9,5,3,-7,4,7,8,5,-4,8,1,8,8,-8,4,-9,10,-7,2,5,3,-1,3,-10,7,10,-5,6,2,10,-7,-2,-4,9,4,1,-5,10,-6,-4,-6,3,-3,-9,-2,2,9,-6,3],[-9,9,-4,-10,-2,-5,-1,1,4,-2,-10,3,2,5,5,3,-5,-3,9,-5,10,-9,1,-7,-5,-2,-1,-8,9,3,1,7,10,-7,3,-4,-2,-6,-1,9,-1,-1,-6,-7,2,8,-8,1,4,9,-2,2,3,6,-4,2,-6,10,-3,6,9,-9,8,4,-2,3,5,-9,-5,6,1,-5],[-2,10,1,9,7,-6,-1,-1,3,-8,-9,-9,-3,-4,-3,-3,3,10,-7,-6,10,3,2,6,-6,-2,-1,-9,-5,1,1,3,-5,-8,4,9,7,3,6,3,-4,-8,7,3,10,2,-8,-5,-7,-7,8,5,8,5,9,-7,-4,-10,-2,-4,5,-4,-10,5,-2,10,-8,5,3,3,7,-3]], dtype = "uint16")#candidate|2430|(28, 72)|const|uint16
call_2429 = func_1653_call(relay.reshape(const_2430.astype('uint16'), [12, 12, 14]), relay.reshape(const_2430.astype('uint16'), [12, 12, 14]), )
call_2431 = func_1653_call(relay.reshape(const_2430.astype('uint16'), [12, 12, 14]), relay.reshape(const_2430.astype('uint16'), [12, 12, 14]), )
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
var_2434 = relay.var("var_2434", dtype = "uint16", shape = (2640,))#candidate|2434|(2640,)|var|uint16
call_2433 = func_1707_call(relay.reshape(var_2434.astype('uint16'), [15, 16, 11]))
call_2435 = func_1707_call(relay.reshape(var_2434.astype('uint16'), [15, 16, 11]))
var_2436 = relay.var("var_2436", dtype = "uint16", shape = (15, 16, 11))#candidate|2436|(15, 16, 11)|var|uint16
bop_2437 = relay.bitwise_xor(call_2433.astype('uint32'), relay.reshape(var_2436.astype('uint32'), relay.shape_of(call_2433))) # shape=(15, 16, 11)
bop_2440 = relay.bitwise_xor(call_2435.astype('uint32'), relay.reshape(var_2436.astype('uint32'), relay.shape_of(call_2435))) # shape=(15, 16, 11)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_2448 = func_458_call()
call_2449 = func_458_call()
func_1677_call = mod.get_global_var('func_1677')
func_1681_call = mutated_mod.get_global_var('func_1681')
const_2453 = relay.const([3,8,2,1,-5,9,9,8,-7,-2,-4,7,-7,-2,6,1,-9,-1,8,6,-2,-3,2,-2,-2,7,1,9,6,-10,-9,4,-9,8,6,-5,6,9,9,7,6,-5,-10,8,6,-8,8,-10,8,-6,-9,-5,9,4,-5,-7,-9,-1,-7,-4,-4,7,-6,-9,-4,-1,8,-9,-9,-2,6,-7,-4,-3,-5,5,9,3,8,10,-9,-6,-6,-1,-7,-9,-6,9,5,2,-7,3,-8,1,-8,-1], dtype = "int64")#candidate|2453|(96,)|const|int64
call_2452 = relay.TupleGetItem(func_1677_call(relay.reshape(const_2453.astype('int64'), [6, 4, 4]), relay.reshape(const_2453.astype('int64'), [6, 4, 4]), ), 0)
call_2454 = relay.TupleGetItem(func_1681_call(relay.reshape(const_2453.astype('int64'), [6, 4, 4]), relay.reshape(const_2453.astype('int64'), [6, 4, 4]), ), 0)
output = relay.Tuple([call_2418,call_2429,const_2430,var_2434,bop_2437,call_2448,call_2452,const_2453,])
output2 = relay.Tuple([call_2419,call_2431,const_2430,var_2434,bop_2440,call_2449,call_2454,const_2453,])
func_2463 = relay.Function([var_2434,var_2436,], output)
mod['func_2463'] = func_2463
mod = relay.transform.InferType()(mod)
mutated_mod['func_2463'] = func_2463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2463_call = mutated_mod.get_global_var('func_2463')
var_2465 = relay.var("var_2465", dtype = "uint16", shape = (2640,))#candidate|2465|(2640,)|var|uint16
var_2466 = relay.var("var_2466", dtype = "uint16", shape = (15, 16, 11))#candidate|2466|(15, 16, 11)|var|uint16
call_2464 = func_2463_call(var_2465,var_2466,)
output = call_2464
func_2467 = relay.Function([var_2465,var_2466,], output)
mutated_mod['func_2467'] = func_2467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mod.get_global_var('func_989')
func_990_call = mutated_mod.get_global_var('func_990')
call_2483 = relay.TupleGetItem(func_989_call(), 0)
call_2484 = relay.TupleGetItem(func_990_call(), 0)
uop_2489 = relay.asin(call_2483.astype('float64')) # shape=(3, 13, 2)
uop_2491 = relay.asin(call_2484.astype('float64')) # shape=(3, 13, 2)
output = relay.Tuple([uop_2489,])
output2 = relay.Tuple([uop_2491,])
func_2494 = relay.Function([], output)
mod['func_2494'] = func_2494
mod = relay.transform.InferType()(mod)
mutated_mod['func_2494'] = func_2494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mutated_mod.get_global_var('func_2494')
call_2495 = func_2494_call()
output = call_2495
func_2496 = relay.Function([], output)
mutated_mod['func_2496'] = func_2496
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2508 = relay.const([[[-7,-10,-10,5,-7,9,4,6]],[[8,-6,-1,-4,-1,-7,4,-10]],[[-2,6,-9,-5,1,10,9,-1]],[[-9,2,9,-2,4,-7,-5,-3]],[[-9,-9,9,-7,-10,-8,-7,6]],[[6,-8,5,-5,9,9,-3,1]],[[1,-10,-3,-3,-4,-2,1,-6]],[[7,4,-4,-4,3,9,8,-5]],[[1,1,2,7,-6,8,-6,-4]]], dtype = "int8")#candidate|2508|(9, 1, 8)|const|int8
var_2509 = relay.var("var_2509", dtype = "int8", shape = (9, 2, 8))#candidate|2509|(9, 2, 8)|var|int8
bop_2510 = relay.bitwise_or(const_2508.astype('int8'), var_2509.astype('int8')) # shape=(9, 2, 8)
output = relay.Tuple([bop_2510,])
output2 = relay.Tuple([bop_2510,])
func_2529 = relay.Function([var_2509,], output)
mod['func_2529'] = func_2529
mod = relay.transform.InferType()(mod)
mutated_mod['func_2529'] = func_2529
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2530 = relay.var("var_2530", dtype = "int8", shape = (9, 2, 8))#candidate|2530|(9, 2, 8)|var|int8
func_2529_call = mutated_mod.get_global_var('func_2529')
call_2531 = func_2529_call(var_2530)
output = call_2531
func_2532 = relay.Function([var_2530], output)
mutated_mod['func_2532'] = func_2532
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2540 = relay.var("var_2540", dtype = "float64", shape = (7, 11, 9))#candidate|2540|(7, 11, 9)|var|float64
uop_2541 = relay.log10(var_2540.astype('float64')) # shape=(7, 11, 9)
output = uop_2541
output2 = uop_2541
func_2547 = relay.Function([var_2540,], output)
mod['func_2547'] = func_2547
mod = relay.transform.InferType()(mod)
mutated_mod['func_2547'] = func_2547
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2548 = relay.var("var_2548", dtype = "float64", shape = (7, 11, 9))#candidate|2548|(7, 11, 9)|var|float64
func_2547_call = mutated_mod.get_global_var('func_2547')
call_2549 = func_2547_call(var_2548)
output = call_2549
func_2550 = relay.Function([var_2548], output)
mutated_mod['func_2550'] = func_2550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2083_call = mod.get_global_var('func_2083')
func_2085_call = mutated_mod.get_global_var('func_2085')
call_2554 = relay.TupleGetItem(func_2083_call(), 0)
call_2555 = relay.TupleGetItem(func_2085_call(), 0)
output = relay.Tuple([call_2554,])
output2 = relay.Tuple([call_2555,])
func_2558 = relay.Function([], output)
mod['func_2558'] = func_2558
mod = relay.transform.InferType()(mod)
mutated_mod['func_2558'] = func_2558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2558_call = mutated_mod.get_global_var('func_2558')
call_2559 = func_2558_call()
output = call_2559
func_2560 = relay.Function([], output)
mutated_mod['func_2560'] = func_2560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2334_call = mod.get_global_var('func_2334')
func_2336_call = mutated_mod.get_global_var('func_2336')
call_2617 = relay.TupleGetItem(func_2334_call(), 0)
call_2618 = relay.TupleGetItem(func_2336_call(), 0)
output = call_2617
output2 = call_2618
func_2625 = relay.Function([], output)
mod['func_2625'] = func_2625
mod = relay.transform.InferType()(mod)
output = func_2625()
func_2626 = relay.Function([], output)
mutated_mod['func_2626'] = func_2626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_2635 = relay.TupleGetItem(func_2364_call(), 1)
call_2636 = relay.TupleGetItem(func_2366_call(), 1)
func_810_call = mod.get_global_var('func_810')
func_812_call = mutated_mod.get_global_var('func_812')
call_2642 = func_810_call()
call_2643 = func_810_call()
output = relay.Tuple([call_2635,call_2642,])
output2 = relay.Tuple([call_2636,call_2643,])
func_2660 = relay.Function([], output)
mod['func_2660'] = func_2660
mod = relay.transform.InferType()(mod)
mutated_mod['func_2660'] = func_2660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2660_call = mutated_mod.get_global_var('func_2660')
call_2661 = func_2660_call()
output = call_2661
func_2662 = relay.Function([], output)
mutated_mod['func_2662'] = func_2662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_423_call = mod.get_global_var('func_423')
func_424_call = mutated_mod.get_global_var('func_424')
call_2751 = relay.TupleGetItem(func_423_call(), 2)
call_2752 = relay.TupleGetItem(func_424_call(), 2)
func_2558_call = mod.get_global_var('func_2558')
func_2560_call = mutated_mod.get_global_var('func_2560')
call_2755 = relay.TupleGetItem(func_2558_call(), 0)
call_2756 = relay.TupleGetItem(func_2560_call(), 0)
func_1915_call = mod.get_global_var('func_1915')
func_1917_call = mutated_mod.get_global_var('func_1917')
call_2761 = func_1915_call()
call_2762 = func_1915_call()
output = relay.Tuple([call_2751,call_2755,call_2761,])
output2 = relay.Tuple([call_2752,call_2756,call_2762,])
func_2774 = relay.Function([], output)
mod['func_2774'] = func_2774
mod = relay.transform.InferType()(mod)
output = func_2774()
func_2775 = relay.Function([], output)
mutated_mod['func_2775'] = func_2775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_2778 = relay.TupleGetItem(func_353_call(), 1)
call_2779 = relay.TupleGetItem(func_355_call(), 1)
output = relay.Tuple([call_2778,])
output2 = relay.Tuple([call_2779,])
func_2782 = relay.Function([], output)
mod['func_2782'] = func_2782
mod = relay.transform.InferType()(mod)
output = func_2782()
func_2783 = relay.Function([], output)
mutated_mod['func_2783'] = func_2783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_2850 = func_2625_call()
call_2851 = func_2625_call()
uop_2861 = relay.log(call_2850.astype('float32')) # shape=(11, 1, 8)
uop_2863 = relay.log(call_2851.astype('float32')) # shape=(11, 1, 8)
uop_2864 = relay.tan(call_2850.astype('float32')) # shape=(11, 1, 8)
uop_2866 = relay.tan(call_2851.astype('float32')) # shape=(11, 1, 8)
uop_2869 = relay.sigmoid(uop_2864.astype('float64')) # shape=(11, 1, 8)
uop_2871 = relay.sigmoid(uop_2866.astype('float64')) # shape=(11, 1, 8)
output = relay.Tuple([uop_2861,uop_2869,])
output2 = relay.Tuple([uop_2863,uop_2871,])
func_2877 = relay.Function([], output)
mod['func_2877'] = func_2877
mod = relay.transform.InferType()(mod)
output = func_2877()
func_2878 = relay.Function([], output)
mutated_mod['func_2878'] = func_2878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_2882 = relay.TupleGetItem(func_1393_call(), 0)
call_2883 = relay.TupleGetItem(func_1394_call(), 0)
func_2463_call = mod.get_global_var('func_2463')
func_2467_call = mutated_mod.get_global_var('func_2467')
var_2896 = relay.var("var_2896", dtype = "uint16", shape = (2640,))#candidate|2896|(2640,)|var|uint16
call_2895 = relay.TupleGetItem(func_2463_call(relay.reshape(var_2896.astype('uint16'), [2640,]), relay.reshape(var_2896.astype('uint16'), [15, 16, 11]), ), 1)
call_2897 = relay.TupleGetItem(func_2467_call(relay.reshape(var_2896.astype('uint16'), [2640,]), relay.reshape(var_2896.astype('uint16'), [15, 16, 11]), ), 1)
uop_2937 = relay.acosh(call_2895.astype('float32')) # shape=(12, 12, 14)
uop_2939 = relay.acosh(call_2897.astype('float32')) # shape=(12, 12, 14)
uop_2949 = relay.erf(uop_2937.astype('float64')) # shape=(12, 12, 14)
uop_2951 = relay.erf(uop_2939.astype('float64')) # shape=(12, 12, 14)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_2960 = relay.TupleGetItem(func_1886_call(), 0)
call_2961 = relay.TupleGetItem(func_1888_call(), 0)
output = relay.Tuple([call_2882,var_2896,uop_2949,call_2960,])
output2 = relay.Tuple([call_2883,var_2896,uop_2951,call_2961,])
func_2965 = relay.Function([var_2896,], output)
mod['func_2965'] = func_2965
mod = relay.transform.InferType()(mod)
var_2966 = relay.var("var_2966", dtype = "uint16", shape = (2640,))#candidate|2966|(2640,)|var|uint16
output = func_2965(var_2966)
func_2967 = relay.Function([var_2966], output)
mutated_mod['func_2967'] = func_2967
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3050 = relay.var("var_3050", dtype = "uint8", shape = (6, 14, 2))#candidate|3050|(6, 14, 2)|var|uint8
var_3051 = relay.var("var_3051", dtype = "uint8", shape = (6, 14, 2))#candidate|3051|(6, 14, 2)|var|uint8
bop_3052 = relay.not_equal(var_3050.astype('bool'), relay.reshape(var_3051.astype('bool'), relay.shape_of(var_3050))) # shape=(6, 14, 2)
output = bop_3052
output2 = bop_3052
func_3078 = relay.Function([var_3050,var_3051,], output)
mod['func_3078'] = func_3078
mod = relay.transform.InferType()(mod)
var_3079 = relay.var("var_3079", dtype = "uint8", shape = (6, 14, 2))#candidate|3079|(6, 14, 2)|var|uint8
var_3080 = relay.var("var_3080", dtype = "uint8", shape = (6, 14, 2))#candidate|3080|(6, 14, 2)|var|uint8
output = func_3078(var_3079,var_3080,)
func_3081 = relay.Function([var_3079,var_3080,], output)
mutated_mod['func_3081'] = func_3081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2774_call = mod.get_global_var('func_2774')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_3083 = relay.TupleGetItem(func_2774_call(), 2)
call_3084 = relay.TupleGetItem(func_2775_call(), 2)
func_2284_call = mod.get_global_var('func_2284')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_3085 = func_2284_call()
call_3086 = func_2284_call()
output = relay.Tuple([call_3083,call_3085,])
output2 = relay.Tuple([call_3084,call_3086,])
func_3096 = relay.Function([], output)
mod['func_3096'] = func_3096
mod = relay.transform.InferType()(mod)
mutated_mod['func_3096'] = func_3096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3096_call = mutated_mod.get_global_var('func_3096')
call_3097 = func_3096_call()
output = call_3097
func_3098 = relay.Function([], output)
mutated_mod['func_3098'] = func_3098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_3143 = relay.TupleGetItem(func_353_call(), 1)
call_3144 = relay.TupleGetItem(func_355_call(), 1)
func_1815_call = mod.get_global_var('func_1815')
func_1818_call = mutated_mod.get_global_var('func_1818')
var_3165 = relay.var("var_3165", dtype = "int64", shape = (96,))#candidate|3165|(96,)|var|int64
call_3164 = relay.TupleGetItem(func_1815_call(relay.reshape(call_3143.astype('int64'), [3, 13, 2]), relay.reshape(var_3165.astype('int64'), [1, 96]), ), 0)
call_3166 = relay.TupleGetItem(func_1818_call(relay.reshape(call_3143.astype('int64'), [3, 13, 2]), relay.reshape(var_3165.astype('int64'), [1, 96]), ), 0)
func_1971_call = mod.get_global_var('func_1971')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_3175 = func_1971_call(relay.reshape(var_3165.astype('bool'), [8, 2, 6]))
call_3176 = func_1971_call(relay.reshape(var_3165.astype('bool'), [8, 2, 6]))
output = relay.Tuple([call_3143,call_3164,var_3165,call_3175,])
output2 = relay.Tuple([call_3144,call_3166,var_3165,call_3176,])
func_3179 = relay.Function([var_3165,], output)
mod['func_3179'] = func_3179
mod = relay.transform.InferType()(mod)
mutated_mod['func_3179'] = func_3179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3180 = relay.var("var_3180", dtype = "int64", shape = (96,))#candidate|3180|(96,)|var|int64
func_3179_call = mutated_mod.get_global_var('func_3179')
call_3181 = func_3179_call(var_3180)
output = call_3181
func_3182 = relay.Function([var_3180], output)
mutated_mod['func_3182'] = func_3182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_810_call = mod.get_global_var('func_810')
func_812_call = mutated_mod.get_global_var('func_812')
call_3273 = func_810_call()
call_3274 = func_810_call()
func_2558_call = mod.get_global_var('func_2558')
func_2560_call = mutated_mod.get_global_var('func_2560')
call_3297 = relay.TupleGetItem(func_2558_call(), 0)
call_3298 = relay.TupleGetItem(func_2560_call(), 0)
output = relay.Tuple([call_3273,call_3297,])
output2 = relay.Tuple([call_3274,call_3298,])
func_3305 = relay.Function([], output)
mod['func_3305'] = func_3305
mod = relay.transform.InferType()(mod)
mutated_mod['func_3305'] = func_3305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3305_call = mutated_mod.get_global_var('func_3305')
call_3306 = func_3305_call()
output = call_3306
func_3307 = relay.Function([], output)
mutated_mod['func_3307'] = func_3307
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3325 = relay.var("var_3325", dtype = "float64", shape = (7, 15, 13))#candidate|3325|(7, 15, 13)|var|float64
uop_3326 = relay.sin(var_3325.astype('float64')) # shape=(7, 15, 13)
bop_3340 = relay.floor_divide(uop_3326.astype('float32'), relay.reshape(var_3325.astype('float32'), relay.shape_of(uop_3326))) # shape=(7, 15, 13)
func_699_call = mod.get_global_var('func_699')
func_701_call = mutated_mod.get_global_var('func_701')
var_3345 = relay.var("var_3345", dtype = "int64", shape = ())#candidate|3345|()|var|int64
call_3344 = relay.TupleGetItem(func_699_call(relay.reshape(var_3345.astype('int64'), [])), 1)
call_3346 = relay.TupleGetItem(func_701_call(relay.reshape(var_3345.astype('int64'), [])), 1)
bop_3354 = relay.mod(bop_3340.astype('float64'), relay.reshape(var_3325.astype('float64'), relay.shape_of(bop_3340))) # shape=(7, 15, 13)
func_2083_call = mod.get_global_var('func_2083')
func_2085_call = mutated_mod.get_global_var('func_2085')
call_3367 = relay.TupleGetItem(func_2083_call(), 1)
call_3368 = relay.TupleGetItem(func_2085_call(), 1)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_3379 = relay.TupleGetItem(func_281_call(), 0)
call_3380 = relay.TupleGetItem(func_283_call(), 0)
func_2003_call = mod.get_global_var('func_2003')
func_2005_call = mutated_mod.get_global_var('func_2005')
call_3381 = relay.TupleGetItem(func_2003_call(), 0)
call_3382 = relay.TupleGetItem(func_2005_call(), 0)
func_219_call = mod.get_global_var('func_219')
func_222_call = mutated_mod.get_global_var('func_222')
var_3385 = relay.var("var_3385", dtype = "float64", shape = (770,))#candidate|3385|(770,)|var|float64
call_3384 = relay.TupleGetItem(func_219_call(relay.reshape(var_3385.astype('float64'), [10, 7, 11]), relay.reshape(var_3385.astype('float64'), [10, 7, 11]), ), 0)
call_3386 = relay.TupleGetItem(func_222_call(relay.reshape(var_3385.astype('float64'), [10, 7, 11]), relay.reshape(var_3385.astype('float64'), [10, 7, 11]), ), 0)
func_2463_call = mod.get_global_var('func_2463')
func_2467_call = mutated_mod.get_global_var('func_2467')
var_3391 = relay.var("var_3391", dtype = "uint16", shape = (2640,))#candidate|3391|(2640,)|var|uint16
call_3390 = relay.TupleGetItem(func_2463_call(relay.reshape(var_3391.astype('uint16'), [2640,]), relay.reshape(var_3391.astype('uint16'), [15, 16, 11]), ), 5)
call_3392 = relay.TupleGetItem(func_2467_call(relay.reshape(var_3391.astype('uint16'), [2640,]), relay.reshape(var_3391.astype('uint16'), [15, 16, 11]), ), 5)
func_3179_call = mod.get_global_var('func_3179')
func_3182_call = mutated_mod.get_global_var('func_3182')
var_3395 = relay.var("var_3395", dtype = "int64", shape = (96,))#candidate|3395|(96,)|var|int64
call_3394 = relay.TupleGetItem(func_3179_call(relay.reshape(var_3395.astype('int64'), [96,])), 3)
call_3396 = relay.TupleGetItem(func_3182_call(relay.reshape(var_3395.astype('int64'), [96,])), 3)
output = relay.Tuple([call_3344,var_3345,bop_3354,call_3367,call_3379,call_3381,call_3384,var_3385,call_3390,var_3391,call_3394,var_3395,])
output2 = relay.Tuple([call_3346,var_3345,bop_3354,call_3368,call_3380,call_3382,call_3386,var_3385,call_3392,var_3391,call_3396,var_3395,])
func_3398 = relay.Function([var_3325,var_3345,var_3385,var_3391,var_3395,], output)
mod['func_3398'] = func_3398
mod = relay.transform.InferType()(mod)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3398_call = mutated_mod.get_global_var('func_3398')
var_3400 = relay.var("var_3400", dtype = "float64", shape = (7, 15, 13))#candidate|3400|(7, 15, 13)|var|float64
var_3401 = relay.var("var_3401", dtype = "int64", shape = ())#candidate|3401|()|var|int64
var_3402 = relay.var("var_3402", dtype = "float64", shape = (770,))#candidate|3402|(770,)|var|float64
var_3403 = relay.var("var_3403", dtype = "uint16", shape = (2640,))#candidate|3403|(2640,)|var|uint16
var_3404 = relay.var("var_3404", dtype = "int64", shape = (96,))#candidate|3404|(96,)|var|int64
call_3399 = func_3398_call(var_3400,var_3401,var_3402,var_3403,var_3404,)
output = call_3399
func_3405 = relay.Function([var_3400,var_3401,var_3402,var_3403,var_3404,], output)
mutated_mod['func_3405'] = func_3405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_423_call = mod.get_global_var('func_423')
func_424_call = mutated_mod.get_global_var('func_424')
call_3452 = relay.TupleGetItem(func_423_call(), 1)
call_3453 = relay.TupleGetItem(func_424_call(), 1)
output = call_3452
output2 = call_3453
func_3468 = relay.Function([], output)
mod['func_3468'] = func_3468
mod = relay.transform.InferType()(mod)
output = func_3468()
func_3469 = relay.Function([], output)
mutated_mod['func_3469'] = func_3469
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3493 = relay.var("var_3493", dtype = "bool", shape = ())#candidate|3493|()|var|bool
var_3494 = relay.var("var_3494", dtype = "bool", shape = (12, 9, 15))#candidate|3494|(12, 9, 15)|var|bool
bop_3495 = relay.logical_and(var_3493.astype('bool'), var_3494.astype('bool')) # shape=(12, 9, 15)
var_3517 = relay.var("var_3517", dtype = "bool", shape = (12, 9, 15))#candidate|3517|(12, 9, 15)|var|bool
bop_3518 = relay.maximum(bop_3495.astype('uint16'), relay.reshape(var_3517.astype('uint16'), relay.shape_of(bop_3495))) # shape=(12, 9, 15)
uop_3523 = relay.erf(var_3494.astype('float32')) # shape=(12, 9, 15)
var_3546 = relay.var("var_3546", dtype = "float32", shape = (12, 9, 15))#candidate|3546|(12, 9, 15)|var|float32
bop_3547 = relay.power(uop_3523.astype('float64'), relay.reshape(var_3546.astype('float64'), relay.shape_of(uop_3523))) # shape=(12, 9, 15)
func_989_call = mod.get_global_var('func_989')
func_990_call = mutated_mod.get_global_var('func_990')
call_3551 = relay.TupleGetItem(func_989_call(), 0)
call_3552 = relay.TupleGetItem(func_990_call(), 0)
uop_3554 = relay.asin(bop_3547.astype('float64')) # shape=(12, 9, 15)
uop_3556 = relay.atan(uop_3554.astype('float64')) # shape=(12, 9, 15)
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
const_3559 = relay.const([8,-4,-1,5,-2,-7,10,6,-3,1,3,-2,-1,8,8,-8,3,9,6,2,-2,-4,-7,4,-9,6,5,8,-9,-1,-6,-3,2,4,7,5,3,4,10,-3,-4,-8,-7,4,-5,-10,5,-9,-7,-4,9,6,1,-3,9,-7,-3,2,5,5,-5,10,-10,5,-4,-2,10,-2,-9,1,10,-2,5,2,-4,-10,2,6,-1,-1,-4,5,-2,-5,3,-10,-6,-8,10,2,7,-2,-4,-4,3,-9,8,-1,2,-1,1,-1,-8,7,1,2,3,-10,2,9,7,2,-3,-6,-8,3,-10,8,3,4,7,1,-9,5,3,9,-4,-7,-4,4,-10,3,9,-8,9,6,7,5,10,-9,8,5,1,-10,3,-8,1,2,5,4,-1,1,10,6,-8,3,7,9,-9,2,3,6,-3,3,8,5,8,7,-4,9,2,-9,1,-4,6,-2,-7,-10,7,-2,9,-4,3,-6,-6,10,-7,6,6,-6,-7,-9,9,9,-1,10,-6,8,6,8,-8,-10,7,3,-8,-4,-1,3,2,-5,1,-6,8,10,-9,5,-7,4,-3,-7,-8,-9,-8,9,4,-5,-7,-6,5,8,4,-1,2,-7,2,7,-7,-9,1,-4,-1,-10,10,-5,1,6,1,-6,-3,-8,-7,7,3,8,5,7,-3,-6,4,-7,-9,8,-2,-10,7,2,-3,7,-6,-8,-1,8,-5,-6,-8,-3,7,4,8,-6,2,-7,6,10,1,2,-4,-5,-5,-7,-7,9,-4,3,6,4,-7,10,-7,5,8,-1,8,-3,-10,-5,3,-8,4,6,3,6,3,5,-6,-9,8,9,7,-8,-4,-1,-4,1,-2,-9,-9,7,3,-3,10,5,1,3,-8,4,-3,-9,3,6,9,2,-10,-1,1,-4,-5,1,7,-3,-7,8,-1,9,-7,3,10,-5,6,-7,-9,10,-2,-9,6,-5,-10,-5,8,-6,8,-4,-7,-3,6,-2,1,-8,-4,3,10,5,10,10,5,-4,9,3,6,3,-6,-6,8,9,2,3,9,-1,-1,9,-1,1,3,-6,-10,3,-3,-2,-5,-4,-2,-7,7,1,1,4,-5,1,-8,6,-7,5,-8,-2,7,-9,3,1,-6,-9,-4,-8,-9,4,-6,-7,-9,-3,-1,-1,-1,9,-8,5,5,-8,9,6,5,-5,-2,3,9,10,1,10,4,7,10,-4,7,3,-10,-4,-1,-5,5,4,-4,-4,10,6,-1,-5,-4,-7,-3,-7,-9,9,9,-3,-1,-8,5,-9,-6,-8,9,-10,-2,-4,-7,-9,1,8,-1,-4,-10,-9,-4,10,5,-7,-3,5,-5,-2,9,3,-1,-10,4,9,10,-10,6,4,-10,-4,-9,-10,-10,-9,6,-1,-2,3,8,-9,10,3,-1,-7,-10,-4,2,5,8,4,-5,5,7,5,-10,4,-4,-5,-3,-6,3,-6,-5,10,-7,1,9,-1,-4,4,1,-5,4,-1,-2,2,8,2,-10,-9,7,9,6,4,8,-3,3,-5,-7,6,3,5,-5,-7,1,2,-5,-4,4,-10,-4,-3,-8,4,7,5,7,3,8,8,5,-5,-10,-1,7,-7,4,-7,-10,-10,-2,-7,4,4,-10,-9,-2,-5,-5,9,10,2,7,6,4,-4,-8,9,1,-4,-4,3,-9,-10,-7,-8,-6,8,-4,1,-10,-6,4,-2,7,-3,1,8,-6,-8,-7,9,9,-7,4,10,-10,6,-2,-10,-6,-1,-1,-1,-9,-2,-3,2,-10,4,-6,2,3,-4,8,-5,9,3,6,6,1,6,9,-8,6,5,-10,-1,-2,-9,9,5,1,7,-2,-5,-3,8,8,2,-10,9,1,3,5,6,-8,-3,10,6,-6,-6,-3,-2,-10,6,-9,-2,-5,6,8,7,2,3,-1,-6,4,-6,6,-8,10,6,1,2,4,-5,9,-6,-1,4,2,8,2,2,4,4,-8,-5,-10,-4,-4,-7,-10,-3,4,4,9,-3,-10,1,-7,-7,-9,3,-1,4,-5,-8,5,-7,-1,6,-6,5,4,-9,-2,7,1,1,-6,-7,7,5,9,3,-2,1,10,4,-1,6,-9,5,2,2,-2,-8,-8,-2,-2,6,6,3,-3,-9,-10,-8,-7,-9,-10,8,3,2,6,8,-1,-5,4,-2,-5,-3,-5,3,3,-2,6,6,5,-1,-4,-8,-5,-1,-10,-8,-3,1,-2,-1,-8,-10,2,-4,-4,7,-3,-2,-9,-9,-5,6,-8,7,1,6,10,4,2,8,-2,-1,-9,5,-5,8,1,-1,9,8,-5,-9,-8,6,10,5,8,-7,10,-6,6,8,-6,-4,-6,-4,7,-7,-6,-7,6,8,-10,2,9,-7,-2,2,-6,4,1,5,1,2,-3,-4,1,-3,-9,2,-3,-2,-6,2,3,3,3,-9,-10,-4,10,-3,1,3,-1,7,6,10,4,-3,7,10,-4,8,1,-6,-1,-3,5,4,3,-1,-3,-8,-2,-5,-6,2,-3,3,-2,7,10,-8,8,-4,-5,7,-7,-4,-7,-1,-5,5,3,4,-1,-1,-2,7,-10,8,-7,3,1,2,-8,3,5,-1,-7,6,-7,8,-5,-7,5,2,10,5,-3,-1,7,-4,9,-1,-2,2,-5,9,7,-6,-1,4,4,-7,4,7,10,-6,-9,-5,7,2,-10,-1,-7,9,7,-3,3,-7,-6,2,6,-4,6,-5,9,-4,-8,-5,-2,-5,8,-10,-6,9,1,-9,-9,1,-2,-8,-6,7,-7,-9,7,-10,1,-5,6,10,-5,-6,2,2,8,3,4,7,4,-2,1,-5,3,1,6,-9,-2,7,-4,6,-1,-5,-10,-8,-10,5,-2,4,-2,7,6,-1,10,-10,9,8,8,-6,-6,5,3,-7,-2,-2,-4,4,-4,-8,-5,3,-8,-5,-2,5,3,6,-9,3,-2,6,6,7,7,6,-8,9,10,2,-4,2,4,5,8,5,-3,-9,-2,-8,-4,4,-5,-7,6,-7,-6,-8,-4,4,-1,4,-1,-2,9,-6,6,6,3,-6,-3,-9,-1,-9,-10,-7,-3,4,5,-9,-9,7,6,-9,-7,10,-8,-6,10,4,-8,10,5,5,3,2,10,-7,3,7,-1,-9,-10,7,-2,-7,-3,2,-4,-6,5,-6,9,3,-9,3,9,-8,9,-6,-6,1,-1,-7,-2,-1,3,1,-3,6,-5,2,1,3,-5,8,4,-3,4,2,-5,4,10,-1,-10,-5,-4,-10,-6,4,4,5,3,2,9,5,7,-3,-5,-10,-9,-9,-1,-7,-4,2,-3,5,-4,5,-1,7,-10,-4,5,7,10,-7,8,10,7,9,9,-9,-1,8,5,-1,-6,-9,9,-4,-3,-10,9,3,3,9,8,-7,-2,-2,-10,1,7,8,-5,5,-5,9,8,-3,5,-5,10,3,-4,-9,9,-10,-10,-4,-1,3,7,-4,-5,8,-9,-5,4,8,-5,2,-7,-10,-3,1,5,-3,-7,5,-4,-2,-5,-1,-4,-7,-8,-3,-5,3,9,-3,-8,-5,3,-7,-5,1,3,-9,5,-6,-8,1,3,-3,-7,-7,3,10,-3,7,5,8,-4,-6,6,3,10,9,-7,8,-9,9,-6,-1,7,7,-6,9,-5,-10,-7,-4,8,-2,6,-8,-2,6,-7,7,5,-3,2,-2,7,7,-6,10,-4,8,2,-4,3,4,-7,2,-6,2,7,4,-5,-5,-2,4,7,6,7,4,10,-10,9,-8,8,-5,-3,8,-8,10,10,-5,-5,6,3,-2,10,-1,-3,-5,10,-6,9,-2,9,-6,-5,7,6,-9,-5,-3,2,-5,-2,8,2,-4,9,7,-7,6,6,9,9,10,-1,-1,6,10,8,-1,-1,1,-10,-8,1,-8,-9,10,6,-4,-4,2,4,-9,9,5,4,1,-6,2,7,6,-6,-6,8,-1,-8,2,4,-6,-3,4,9,-3,8,-2,-5,1,-7,-6,-8,5,10,7,3,7,-4,-5,-8,-6,4,-1,8,-10,10,8,-5,-3,-4,-6,-4,3,6,1,-6,2,6,-9,-5,7,-7,3,-10,4,7,-1,5,-10,-1,6,-9,7,2,-10,-7,10,6,3,-10,-9,10,-9,-3,-7,2,-4,-2,6,9,10,-7,-7,4,8,-10,2,-9,5,9,-6,7,-2,1,2,-8,-5,3,-9,-3,-2,5,2,-4,-4,1,6,10,-7,-7,-2,-9,1,10,-8,6,5,-5,-3,-6,-2,9,-4,-7,3,-8,-1,1,-1,-4,3,1,1,-8,5,-3,10,-6,-2,-3,-6,-9,10,-1,-2,-9,4,4,-6,-2,-6,-7,-1,-9,5,-10,-5,-2,-1,-5,9,-8,4,2,4,-8,-1,5,9,4,7,8,3,6,-4,-6,3,-8,6,6,4,-10,-10,-6,2,2,6,-1,2,4,8,-9,-4,9,-6,1,8,4,10,-6,2,2,-10,8,10,-5,1,-1,-10,-6,7,4,-3,-3,10,5,-9,-3,-10,10,2,10,1,8,-4,-8,6,-8,2,-3,-1,8,5,-1,-10,-7,-6,6,8,9,-10,7,-8,-6,6,-5,-8,-9,2,-8,-10,-5,-1,6,-6,-5,1,-4,-5,-1,8,8,-7,-8,6,3,2,4,8,-5,4,-1,-10,-4,-3,-7,-1,8,-3,-8,2,-7,-7,8,-3,-10,-10,2,7,-8,2,-3,2,10,-6,6,-10,-2,6,-4,10,-5,-6,4,-4,-6,-8,9,10,5,10,6,6,6,-8,2,6,-2,-6,-8,9,-7,2,-8,7,-10,7,-4,-4,9,-3,-1,10,-3,-10,-7,6,-9,-1,-1,-2,-5,9,-4,-2,-6,-3,5,-2,2,-1,4,-4,-6,-10,3,-9,1,-8,10,7,6,-7,-7,-1,-3,-5,-10,10,4,-2,-1,3,-9,-6,-2,9,7,1,4,-1,4,4,7,-7,-3,7,-2,-6,3,1,9,5,5,7,10,8,6,-8,-7,3,6,6,4,8,-7,5,1,9,-10,5,6,3,-5,-4,-8,4,1,-3,-3,-2,-1,4,9,-8,-2,6,-6,10,2,6,3,5,10,-8,-8,-3,7,1,-1,-2,1,10,9,-9,-4,-2,-4,10,4,9,8,2,-9,9,1,-2,-1,8,-2,10,5,-2,6,5,2,3,3,-5,-8,2,-8,-10,9,-7,-8,-7,-7,-1,3,-7,9,-6,7,7,-8,5,-5,4,-6,7,8,-6,-4,-1,3,3,8,-6,-3,-10,-4,-6,1,-5,1,-10,5,-5,3,8,-4,1,10,-8,-2,3,-5,-5,9,5,1,10,-3,4,2,5,-3,-9,4,8,-8,-10,-2,-1,-6,-2,4,-2,6,5,10,-6,-6,7,-2,4,8,5,2,10,2,4,3,-5,5,-6,1,9,-7,-7,-1,-1,6,8,1,5,-9,1,8,10,-9,-8,10,-8,-4,-10,-6,6,6,-2,-2,-2,10,5,-1,-1,5,3,-7,-6,7,-7,-4,7,-7,-7,-9,-1,2,5,5,6,-7,7,1,6,7,1,6,-3,8,-3,-1,-4,-4,-8,8,9,4,-1,9,-3,1,-10,-1,-2,-5,5,-1,8,-1,2,-2,-3,9,3,1,4,1,3,-7,2,1,-7,-10,6,3,9,1,4,-7,-7,7,4,-5,10,1,-5,1,5,-9,3,2,-7,-5,4,10,-4,-3,4,5,-10,-10,-1,7,4,-8,5,-8,-5,-5,-9,-8,-3,1,-9,-3,-3,3,6,9,-7,-7,-6,-7,2,-8,9,3,-9,1,-1,8,-9,-7,3,5,2,4,-6,9,-3,8,6,-5,-6,-4,3,2,-3,7,4,7,3,-5,2,-7,-4,-8,6,5,10,-10,1,4,-10,3,-4,-1,-2,6,-2,-1,-9,7,2,9,1,-6,-1,10,1,5,-4,2,5,-1,10,3,1,-7,2,-7,-5,-7,1,-10,-3,-10,3,4,-10,5,7,1,6,2,-4,-10,2,-5,-7,7,-10,-8,9,-1,6,-10,1,-2,-9,-6,-5,-2,-6,-10,-2,2,6,-6,-1,-3,-10,2,4,10,-10,6,3,-2,5,-1,-1,-10,4,-3,1,-3,-10,-6,-9,-10,3,8,-2,-6,-4,-5,-1,-3,8,-9,1,2,7,8,4,-8,-1,-4,7,-3,6,-6,-10,-1,7,9,-4,-1,-1,-8,4,4,2,-2,10,10,1,3,6,-2,-8,1,4,-2,9,-1,-5,10,-5,-6,6,-2,-1,10,1,-10,-1,-10,1,9,5,4,-5,7,7,-6,9,-1,3,8,3,4,9,8,-9,1,-9,3,-9,7,-6,-10,10,-7,-5,8,3,2,5,3,1,5,-8,5,1,-5,4,1,-1,7,-3,3,-7,9,7,6,-7,7,1,7,3,-8,9,10,-8,-5,-4,-9,3,2,2,-7,1,6,-5,6,5,6,-3,-6,-5,-4,-1,-9,2,6,1,5,-9,-4,4,-4,-3,-4,7,9,-3,3,7,10,-5,-3,10,-6,9,-3,1,-3,-8,-3,9,8,-5,5,3,1,-2,4,-2,-2,4,7,3,-10,-9,5,-4,-1,4,-1,1,-6,-8,-8,-3,-3,-6,-2,10,-9,6,-8,-8,1,5,2,-6,1,-1,4,7,-10,-8,3,6,-9,-7,3,6,-9,6,6,-10,-5,6,-4,7,-8,-8,-4,-5,9,2,9,-7,-6,2,6,9,-4,3,9,-3,6,10,-10,-5,-8,4,-2,10,6,9,5,-7,4,8,-9,-2,6,5,6,-4,6,4,1,-7,5,10,6,8,5,-3,8,-9,7,8,-5,-10,2,-10,-5,9,5,-9,-7,2,2,6,3,4,-9,-7,-7,-7,10,-4,-6,-6,-4,-3,1,-3,-3,3,-6,7,-1,2,-1,9,-6,-8,-5,5,-7,-10,-6,-3,6,4,-5,9,-7,-4,-10,10,5,10,2,1,4,10,-6,8,9,4,-6,9,-4,2], dtype = "uint16")#candidate|3559|(2640,)|const|uint16
call_3558 = func_1707_call(relay.reshape(const_3559.astype('uint16'), [15, 16, 11]))
call_3560 = func_1707_call(relay.reshape(const_3559.astype('uint16'), [15, 16, 11]))
uop_3561 = relay.asinh(uop_3556.astype('float64')) # shape=(12, 9, 15)
bop_3563 = relay.greater(uop_3561.astype('bool'), relay.reshape(bop_3495.astype('bool'), relay.shape_of(uop_3561))) # shape=(12, 9, 15)
output = relay.Tuple([bop_3518,call_3551,call_3558,const_3559,bop_3563,])
output2 = relay.Tuple([bop_3518,call_3552,call_3560,const_3559,bop_3563,])
func_3571 = relay.Function([var_3493,var_3494,var_3517,var_3546,], output)
mod['func_3571'] = func_3571
mod = relay.transform.InferType()(mod)
var_3572 = relay.var("var_3572", dtype = "bool", shape = ())#candidate|3572|()|var|bool
var_3573 = relay.var("var_3573", dtype = "bool", shape = (12, 9, 15))#candidate|3573|(12, 9, 15)|var|bool
var_3574 = relay.var("var_3574", dtype = "bool", shape = (12, 9, 15))#candidate|3574|(12, 9, 15)|var|bool
var_3575 = relay.var("var_3575", dtype = "float32", shape = (12, 9, 15))#candidate|3575|(12, 9, 15)|var|float32
output = func_3571(var_3572,var_3573,var_3574,var_3575,)
func_3576 = relay.Function([var_3572,var_3573,var_3574,var_3575,], output)
mutated_mod['func_3576'] = func_3576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_3619 = relay.TupleGetItem(func_353_call(), 1)
call_3620 = relay.TupleGetItem(func_355_call(), 1)
var_3625 = relay.var("var_3625", dtype = "float32", shape = (3, 13, 2))#candidate|3625|(3, 13, 2)|var|float32
bop_3626 = relay.left_shift(call_3619.astype('int64'), relay.reshape(var_3625.astype('int64'), relay.shape_of(call_3619))) # shape=(3, 13, 2)
bop_3629 = relay.left_shift(call_3620.astype('int64'), relay.reshape(var_3625.astype('int64'), relay.shape_of(call_3620))) # shape=(3, 13, 2)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_3643 = func_2625_call()
call_3644 = func_2625_call()
func_2334_call = mod.get_global_var('func_2334')
func_2336_call = mutated_mod.get_global_var('func_2336')
call_3645 = relay.TupleGetItem(func_2334_call(), 0)
call_3646 = relay.TupleGetItem(func_2336_call(), 0)
uop_3647 = relay.tan(var_3625.astype('float32')) # shape=(3, 13, 2)
func_3398_call = mod.get_global_var('func_3398')
func_3405_call = mutated_mod.get_global_var('func_3405')
const_3655 = relay.const([-8.888120,-8.743878,0.364960,-4.209545,2.739385,-4.104377,-7.627571,-4.506779,5.759541,-5.058393,4.766992,6.301512,1.854588,-3.686062,-5.883292,9.845248,4.555937,-4.651127,-8.410836,-0.515271,-9.778188,9.977320,-3.075144,-9.919859,8.156092,2.681519,0.863000,6.903628,-6.116272,4.653588,0.038090,2.471806,1.828745,-8.317570,-8.355389,3.309689,6.896917,-7.416699,-3.534329,-1.932366,7.767586,9.952532,-5.572462,4.053487,-2.056230,5.492856,-2.694293,-7.665627,6.520573,4.326062,2.499078,-2.386280,6.996601,-4.801250,5.606331,-6.590799,-9.570595,6.408935,-7.424904,0.141997,-7.090843,-0.607260,8.190782,-5.789416,6.387596,9.622156,-1.994182,-8.147399,-7.483242,-3.683793,7.238532,-4.069689,-3.482872,-6.808507,3.581192,1.687126,6.188039,-9.104504,-8.769560,3.916645,-9.533812,-8.790280,-3.807049,-5.873903,0.400663,-9.850754,9.830905,7.208767,8.750413,-5.751631,3.057684,-1.704506,-1.246449,-2.288300,9.667175,-1.739976,-8.429060,-5.463745,2.662330,2.985192,1.849268,9.016578,-4.828232,-4.346375,7.944685,-6.264341,-8.519569,3.808759,0.494575,3.303090,2.300285,-5.082192,-6.788911,-2.488554,-1.303351,7.286380,7.292887,-2.452200,7.950230,1.829319,-6.197057,7.344874,-2.143781,5.210311,-8.743603,-7.876655,-9.943680,2.785615,-4.407979,6.747113,3.944757,-4.272228,3.644447,0.471342,-1.134811,2.202904,-1.838572,0.172900,1.870384,9.608838,-5.093038,3.084021,-5.885620,0.745669,-2.691977,2.597227,5.605735,0.008914,7.680734,6.748073,4.571401,-0.541288,-9.481692,8.173009,-0.186280,0.690588,-8.738872,5.260063,-4.282860,1.266370,6.156537,-5.644759,9.463010,-5.800912,-3.888306,-9.883195,-5.808982,-8.948793,-7.897838,7.136268,-5.578729,7.666196,6.218645,5.945130,-0.775963,0.755672,-3.224052,-8.896361,9.565963,-2.789483,5.295271,1.239413,2.513404,-4.756430,4.765196,-2.379355,-2.019455,0.011723,-0.471883,5.076742,3.464574,9.630941,8.292434,6.340758,-7.414114,-8.945073,-1.049850,4.979153,4.571728,-8.897032,7.819603,-6.202957,-7.830090,-3.553200,4.296716,4.960582,-4.600703,-0.812534,2.960852,-8.252869,8.245540,7.880184,-8.051474,5.612731,-1.875667,8.616701,-2.967810,3.609341,8.681699,1.286112,-1.291242,5.449168,8.279672,-0.927946,-7.150017,-1.330198,3.797169,6.258211,2.315197,-7.506473,-0.801617,2.942965,1.378269,-3.665223,-3.950311,2.439860,-1.842307,3.744575,-4.457677,-4.025095,-1.489130,-1.581351,-0.644372,-4.874509,-9.043630,3.147876,-8.193580,7.327430,-2.016422,-7.836928,-4.449411,4.335907,-7.466054,-7.732247,-2.302850,3.285872,-7.530852,-6.974585,-2.206050,-7.339675,2.287367,6.363735,-1.431219,-5.307057,-3.518010,-6.515765,-5.724476,-9.116932,-8.654867,-1.522628,5.367490,-5.480855,5.105350,8.340736,6.462764,2.319078,9.490904,-1.469502,7.498563,-1.138075,4.469799,-7.623447,-5.308176,-6.826949,-4.238153,5.642606,6.956564,1.428739,7.182506,-4.200782,-4.543433,8.552164,-7.648787,4.346407,-0.394133,-9.900543,-4.014323,-4.642133,2.533128,-2.016957,6.738744,8.106646,5.413917,6.603204,4.065891,1.982427,0.679679,-8.015407,-6.287458,-4.978025,0.827513,-1.916314,0.889799,4.181158,7.137482,-6.878388,6.204009,4.440042,-1.648749,8.936036,-3.297296,1.878783,-2.158419,-5.062321,-3.571129,7.895917,7.691374,2.071802,-2.340561,8.223755,-3.092709,-7.809787,1.163083,-7.271878,0.867510,-0.448029,-8.854647,2.159859,2.208640,2.625446,-8.555468,5.016307,-8.639091,3.955247,2.581677,6.087783,-2.283597,-4.320998,6.069834,-9.746970,-2.663240,3.970365,-2.922576,6.634711,-5.727624,1.964438,-8.703285,-6.427392,-8.410931,5.576867,-7.653674,5.017944,5.119481,-6.725573,7.333768,5.548261,3.899859,-5.517887,8.569299,5.141458,4.479724,4.851178,-5.158303,-5.482922,4.785447,-5.423746,-1.353329,-9.429923,4.519168,5.987600,1.359685,8.990448,4.064190,9.290119,7.702489,-6.952663,5.703785,-2.176004,9.839764,-1.895633,8.144974,-5.403257,6.270403,2.992039,0.795166,6.822129,7.508579,-3.980448,-0.757753,4.754163,-1.284217,-9.057717,1.251938,1.794555,-4.748288,8.646007,1.830615,5.630407,1.466399,9.868819,8.063229,8.173407,9.474391,1.760086,7.709504,-8.512446,-4.509380,-5.063308,4.193158,-5.521073,2.664984,8.545213,1.792452,2.454722,4.767773,-3.584047,4.885342,0.775074,3.422807,1.506157,-3.478243,-1.503643,-4.517022,-1.951931,5.752419,9.879000,0.740406,3.791316,-7.539689,2.014159,8.304472,-4.922541,7.661750,-7.228528,3.808705,-7.066568,3.114658,-9.332884,0.957419,8.725074,-4.086072,8.991855,-2.906098,-3.903306,-3.786065,-6.560093,7.985213,-8.122432,1.284431,0.774416,-1.713207,-0.243500,4.875726,-1.182893,0.004454,8.626887,-9.831822,4.632690,4.017989,0.752860,8.049741,6.327349,4.266361,-0.185491,-7.892004,2.376676,4.989100,-2.819516,-1.698510,9.232975,3.666786,2.067539,5.299862,-5.591818,1.986381,-8.995378,2.447822,8.820818,-8.065532,3.699991,-4.065855,4.847637,-1.685250,-6.410223,-0.751470,1.218628,-4.207235,-8.857623,9.741753,-3.186421,-4.318000,-5.363431,-0.566702,-5.066620,3.770720,-0.984232,-2.418551,5.007042,5.356888,-3.455289,5.039835,1.099275,-3.608114,4.160784,-2.193879,-0.292189,2.974183,7.594287,5.561371,-2.440972,3.052424,-9.898309,-0.705825,4.055663,2.248766,-7.120750,0.747240,-6.024517,3.120934,2.358662,6.897581,-5.361173,-0.132350,-4.242880,-9.659302,-0.959672,1.174143,7.585999,-3.151444,-4.762659,-3.330638,-0.216592,-5.786792,-6.094320,4.187639,-9.190995,5.556754,3.879600,-7.673020,2.607034,-1.622819,-5.652477,-0.845424,3.670322,-9.430845,-4.914939,-0.862963,-4.693358,2.445692,-4.674304,3.124291,9.540128,-9.228473,-7.405874,8.807454,9.325174,-5.374904,2.683627,4.272053,6.520287,-6.470669,9.014703,1.865470,-8.490358,-2.094511,0.640399,6.355060,-0.128137,8.506410,-5.725294,0.530817,-1.231610,4.080910,-8.798425,-3.699820,4.835622,-3.666879,-0.153014,-9.837750,-5.739683,2.128858,-6.636922,2.014452,-2.214519,-6.520223,3.527594,-0.121156,3.359407,9.781419,1.551577,6.825050,6.870093,7.896092,2.765253,-6.514349,-4.435923,2.741791,-3.959272,7.461605,8.373366,4.324665,9.985403,-3.151695,3.431710,6.168810,-1.740211,9.094809,-4.582638,0.600268,4.377760,2.163290,0.100631,-0.176276,1.731206,7.957854,3.986459,1.678232,-1.341041,6.811672,-7.927244,-7.073922,-7.462942,-7.955670,-1.116704,-5.154722,5.215703,4.439821,3.440845,-3.933355,-0.417559,0.006152,-7.904652,-7.650613,7.002780,-8.150568,-7.023203,-4.727327,8.622114,2.209655,-6.061611,8.242840,-0.231370,-6.055903,-2.728412,-1.272333,-1.249385,6.215555,5.197841,-1.410292,6.657350,-4.899309,5.166332,-7.471299,1.763961,2.644861,-0.647674,7.475332,2.824731,-1.156209,-0.413270,-6.595688,-2.660383,6.153329,-7.810129,-3.119132,-0.179643,9.955073,9.772159,-6.465925,-9.547992,-2.375357,-6.264371,4.815101,-4.004250,-2.177514,-7.523486,0.173258,-3.516885,-1.169468,-8.897436,-8.383646,4.019749,2.088211,-3.390073,2.785794,1.614947,7.123442,5.520274,3.428105,-9.040790,-0.517818,7.192336,7.147755,-7.167819,-6.532078,3.044571,-5.919402,-5.897010,5.603593,7.776718,3.995729,7.510211,6.083152,6.271665,-4.023926,-2.304159,4.917602,-1.610956,1.058477,-7.011669,-2.528163,-6.159719,8.637466,-3.323216,6.040631,3.083873,-5.153788,1.551929,-3.472064,-0.755435,-4.289953,0.026268,-1.318477,5.828206,7.641612,6.555634,8.355686,-6.840038,3.441325,3.667893,-9.138141,4.334063,0.377694,-9.408416,-4.400136,-2.033038,0.922619,-6.011612,-4.103163,3.714115,9.046399,1.559142,7.807309,6.010360,-4.128023,8.225266,-4.074751,2.344987,-6.754827,0.100594,-6.829066,0.539625,9.995185,-8.501714,6.065884,5.941688,-0.915800,9.938407,-6.582158,-5.921516,-9.610905,-3.257884,1.431588,-3.168364,6.137251,-4.402350,-1.189234,-4.251227,2.902236,9.106284,-4.889029,5.654269,6.212888,-3.054106,-8.002903,-6.454798,6.599728,8.355149,-0.044288,-5.470625,7.664344,2.653870,-1.301488,3.897756,-1.012817,2.178749,-1.505094,-0.906661,7.098401,2.507136,4.648884,-0.820228,-8.732019,0.341736,-9.747266,7.160363,-0.145575,7.402082,-4.930563,-7.960460,1.371780,9.269017,9.267662,4.251694,8.254716,-2.690857,-0.658848,6.190838,-4.166622,8.167542,-1.008884,-3.716312,2.477287,7.643734,-7.055001,0.226857,0.806317,5.083497,-8.728727,-3.166005,-4.650286,-8.412149,3.956318,1.845877,8.218882,-1.137494,3.587657,-2.438477,-2.243401,-2.102336,-6.847693,-1.997291,4.312273,-6.714803,-2.200910,5.127384,0.019653,5.966626,0.129539,-1.815608,3.935473,-6.722861,8.210915,-5.028513,-5.190164,-3.777780,-5.112636,2.544589,3.155797,7.266568,-5.342230,-0.779730,-2.086805,-7.362702,-7.309685,-5.764793,-0.316079,6.609304,-6.530926,0.147540,-7.408936,9.108920,7.956029,-4.334609,-3.091064,-0.040033,-0.087492,-8.230827,0.911334,-6.123382,8.784528,4.758539,3.431013,8.534495,-3.341353,5.294436,-0.523921,0.148179,3.388040,-9.998144,5.717350,-1.723251,4.253121,4.599060,6.097302,3.688673,-2.646631,-9.046108,1.612694,0.573709,4.961821,-4.998463,1.135141,9.135845,-1.929791,-0.697421,-3.835669,3.706279,7.753205,-8.247866,2.960113,3.871382,7.283081,1.081694,9.599407,-5.381022,4.177910,2.987134,0.548115,9.710842,-5.981202,8.392324,-8.574445,3.513567,6.596519,3.770200,8.834020,8.183706,-5.548802,3.798793,8.509259,-7.964876,-7.396830,-0.439815,-7.672658,7.546581,0.814643,-3.124546,-3.419258,-3.330687,9.321592,-0.838161,-3.072481,2.830140,-0.067909,2.382607,7.822357,2.637658,0.141632,4.506276,6.480912,-9.286752,5.646974,8.117957,-0.320391,-4.243540,8.228500,-9.019218,-1.645708,-4.413872,-2.303244,-9.250927,-7.585821,-8.568332,1.859450,6.154086,-7.882163,-3.268435,-9.168482,2.995813,3.034055,8.519358,-0.662019,-1.835583,8.374543,-3.680697,-4.811292,2.003794,-8.130423,-4.892539,4.068976,-6.480739,-1.726994,-1.331902,-8.285775,6.163545,6.147229,-5.769966,2.904850,-8.746823,-9.014426,-6.519651,6.512613,7.144682,9.835790,-1.650492,8.498889,1.484829,8.754964,5.473080,8.050815,4.831096,1.017693,6.627681,-2.846300,0.805930,-8.946019,-9.041307,-4.496357,9.948137,7.896486,-7.811915,-4.355403,-7.859326,2.770694,-0.963112,2.349047,8.702199,5.975716,6.934768,-1.378294,-7.885846,-8.218407,9.218165,-7.412873,4.288739,-5.567945,7.369982,9.894137,-0.211655,4.012258,5.289584,-2.546190,1.393699,7.571776,2.838773,2.044275,-7.493296,-4.289421,-5.860405,-8.762709,4.839024,-0.956850,-1.737560,-9.810561,-7.279873,9.727279,-3.265161,4.949753,3.215032,-1.069500,-1.249208,5.098666,-9.638464,-5.146382,-3.837409,-0.358655,7.807218,-1.531253,-3.159131,-1.315219,-3.598301,-0.547206,1.146729,-4.876965,1.473098,-2.836521,4.184628,-4.296777,4.237914,-1.506630,-0.159081,8.581533,0.145934,7.516501,2.176672,9.316833,5.284938,-3.527433,2.403075,9.578571,-4.110757,-5.553158,0.870589,4.917011,-1.172874,5.749837,-6.087923,-0.460642,-5.118658,2.792654,-6.707857,-8.405288,-7.282182,-0.685437,1.682139,-0.847552,2.874744,8.797886,-7.767455,-5.526001,8.302319,7.984021,-3.984857,5.156194,8.684020,-6.563407,4.848849,6.791062,-0.694759,2.982317,2.510278,6.471472,5.337178,-2.251697,8.433203,-4.021054,-6.661216,-0.156119,7.871368,9.666244,-9.528441,-6.703915,-4.642579,9.749418,-6.717159,7.662403,5.522141,-3.585026,9.499628,-4.903485,3.853377,3.976842,-7.528293,3.637698,-1.739714,-2.558471,-7.261978,-5.398304,-7.372397,8.481026,5.775636,-7.345809,5.614670,0.545677,5.018093,6.303741,-9.892567,-5.463007,-3.974196,-2.080716,3.318460,0.449376,-6.358337,-3.894414,-6.735701,7.439340,-6.172034,-9.896591,-3.499935,9.927326,7.456355,2.513376,3.857628,-6.048189,2.343860,-4.232867,6.505680,-5.829355,-1.617897,-7.996948,2.673608,-2.689160,2.200539,9.249965,-7.477779,-1.117580,-4.420826,3.684996,3.220712,7.121196,-3.228108,2.365746,-8.106559,9.251461,5.379005,6.444125,5.176119,-0.564807,-7.424864,7.950899,-6.968362,-0.370012,8.848437,1.363402,4.516485,1.701777,-6.110168,2.673131,-1.653001,3.076431,-8.867756,-7.387196,-1.154087,-6.474063,4.498761,5.415667,2.842531,-0.807009,6.498312,-2.646325,-2.170118,9.308458,-2.606820,3.545642,6.569380,-8.787361,1.662421,-5.350379,-7.196688,-2.551075,-6.780758,8.526853,2.924983,-2.544480,8.383949,3.558889,-3.627662,1.548152,3.497223,4.119115,4.431932,-6.522298,3.070783,4.229139,-9.161587,3.379134,3.432108,-8.530089,-2.669078,-1.653269,9.093556,9.363924,-7.267376,9.735745,-6.469108,-8.814000,-5.511058,-1.626861,2.654688,7.034418,-1.816855,-1.427188,-1.394665,-5.977553,9.922826,-0.808178,0.772465,-6.479916,-3.729163,5.531779,5.134143,7.883760,3.941555,2.531353,0.306415,-3.090062,2.678120,9.221781,2.337305,-9.451663,-7.182833,-7.889314,-3.782772,4.747166,-0.012340,6.661424,1.548258,6.050076,4.234156,4.844722,-3.743986,-9.735076,1.164747,7.864607,5.213947,0.280798,-5.508543,5.998247,9.910459,-5.462841,-6.821554,0.341552,-6.387359,-4.899675,4.431367,-2.322906,1.010129,9.154630,-9.135641,7.932893,-1.165050,-4.919940,-1.026411,4.815183,-2.973748,0.106734,-2.571931,-6.098321,-7.869583,-2.656149,6.457354,6.862838,6.798408,3.248195,3.897055,9.244798,2.344962,-9.536391,-6.244879,5.639596,9.772474,4.012329,6.264578,-9.052215,-2.560282,2.562497,6.708312,-4.332932,0.409242,2.916855,-6.201075,-5.649573,-4.559842,-8.045893,3.204670,9.222294,-0.018185,-6.102457,8.145104,9.614517,6.114125,5.026832,5.976929,5.644697,8.733102,4.914378,4.491997,1.611537,2.232382,-2.108826,-5.204148,9.236180,-5.861198,-6.572848,0.932729,7.345017,6.901468,8.332750,-8.504998,0.497909,4.742000,-1.478551,3.459265,-1.940662], dtype = "float64")#candidate|3655|(1365,)|const|float64
const_3656 = relay.const(9, dtype = "int64")#candidate|3656|()|const|int64
var_3657 = relay.var("var_3657", dtype = "float64", shape = (770,))#candidate|3657|(770,)|var|float64
const_3658 = relay.const([10,-1,-1,6,-2,-4,-7,-2,10,-1,-5,6,-4,-1,1,-8,-7,3,9,-1,10,-4,2,7,-3,-8,-7,4,-9,-6,8,-3,-2,2,-6,2,8,2,2,-3,10,-5,-6,-10,3,-7,-7,5,-9,-1,-2,2,9,-10,-7,-7,-8,6,1,-1,2,-5,-10,-10,-9,-7,-4,-9,-5,3,5,9,-4,9,10,10,-8,3,-7,-1,6,5,7,2,-6,3,6,-7,6,-6,4,10,-2,3,8,6,-2,-1,-7,-10,-7,-6,-5,-5,-9,-9,8,-8,-2,10,5,-1,8,-5,-6,-10,9,10,-1,7,6,2,5,4,10,-7,-9,1,4,-2,4,5,-10,-9,8,8,4,-7,1,-6,5,-8,-4,4,9,-8,10,6,8,10,3,-1,-9,8,10,-2,9,-3,-3,1,-5,-4,-4,-6,8,-2,3,10,4,3,-3,-2,7,7,2,-3,-9,-3,-9,-9,4,-10,5,-8,-9,4,6,-4,1,4,-1,10,5,-7,4,-1,-7,3,2,-2,2,3,-4,-10,10,6,-4,3,2,4,-6,-4,8,7,-9,-1,7,-9,-10,-5,5,-2,-10,8,5,-7,1,-5,9,10,-1,8,-2,-10,-6,-3,-6,9,9,7,-1,6,6,-10,-3,4,1,3,-9,-6,-8,7,3,10,-5,-8,1,-8,-5,-3,-1,2,7,5,-10,2,-9,2,4,6,6,6,7,-6,6,-1,-4,-9,2,-8,5,10,8,-8,3,2,7,7,-3,6,-2,-8,-4,9,1,8,-1,3,-8,10,2,-1,9,3,-4,-3,8,3,8,-7,3,-8,4,4,10,-5,5,3,7,9,-7,-6,-4,8,-4,1,-2,4,10,-8,-1,5,1,3,4,-7,-2,5,-3,8,-7,7,-9,5,-10,-10,-8,-8,-2,4,2,-6,-4,2,3,-7,8,4,-6,7,-2,6,9,-6,6,7,-1,2,-4,-3,4,-1,-3,-10,-4,6,1,5,-5,-2,-2,8,-2,1,5,-4,3,1,-2,6,7,1,3,1,10,-10,10,8,-6,-9,2,-10,-1,-2,4,-9,9,3,8,1,-7,10,6,-1,-6,7,-6,-10,10,1,9,8,-2,3,5,7,4,-1,-5,7,3,-7,1,-5,1,-6,6,2,5,7,9,3,-1,-8,-7,6,-8,-10,-2,1,-2,6,1,7,3,-7,10,-8,4,-5,-2,2,4,1,8,-1,-9,2,5,7,5,-2,1,4,-5,-8,-10,7,4,-3,-9,5,-1,9,8,6,9,-8,8,-8,1,-2,-6,-6,-6,-3,3,-7,6,-4,4,-8,8,5,-6,-10,7,-9,-10,3,3,-3,5,3,-7,-6,7,-4,-7,-2,2,-1,4,3,-4,2,-2,6,-4,-9,-7,2,6,-10,6,6,-6,8,7,-5,-8,8,1,-9,4,8,2,7,7,-1,-3,-3,-5,10,2,3,-2,4,-7,-10,1,-4,9,9,3,1,8,-5,-6,-5,4,-10,8,-2,7,8,2,-8,-5,9,8,4,-5,-9,5,9,1,-6,3,6,1,-7,7,-2,-6,-2,10,-2,-4,3,-6,-1,-2,-8,6,-7,9,8,3,8,-2,6,6,-6,-1,-2,-1,-8,3,-2,-1,5,-6,7,4,1,-8,7,-6,-4,4,-6,2,-10,1,3,-2,3,3,5,5,-5,-2,-7,-7,-7,-9,-6,8,-6,-9,-10,-9,-6,3,4,-9,1,5,-2,-8,-5,-2,10,8,-7,-8,5,4,-2,5,6,-8,7,-4,-6,-8,1,-2,7,8,-9,5,-4,7,5,-5,-8,-8,4,4,6,3,-1,8,-6,-4,-3,-9,7,6,-10,2,3,2,4,1,9,7,8,-8,2,-1,8,-5,-8,6,3,5,-8,5,-5,1,-8,-4,4,5,3,-2,-8,5,-7,3,10,5,-2,-1,-7,-3,-3,-3,8,-2,4,1,2,-7,10,8,-5,-8,-5,6,-3,7,5,-2,8,3,9,-5,1,-9,-9,8,2,-4,7,9,8,-8,3,-5,6,-4,-1,6,-8,-10,-6,4,-6,-6,-8,-7,-8,1,-6,4,-6,9,-7,9,3,-6,-10,6,-9,-1,5,3,-4,9,-1,-4,-3,-4,9,8,5,-9,-6,-10,-7,-10,-2,8,-7,6,9,-5,-10,-3,-2,-10,-6,-1,4,-5,-6,-3,-8,-2,7,-3,7,-7,6,-7,10,5,-6,8,8,1,8,10,-5,1,2,6,-1,-6,4,5,-1,-2,5,-9,3,4,-3,9,9,-2,3,10,-3,-1,10,-3,-4,-9,6,1,7,-3,4,-10,2,-3,10,-1,10,1,7,2,-2,-2,1,8,-3,-8,-10,9,2,7,5,-6,9,6,5,1,1,4,9,7,2,8,-6,4,-10,2,10,-2,-7,-6,6,-10,1,6,5,-3,-1,-10,1,-6,6,6,-6,-6,-7,-5,-2,-8,8,-4,-9,1,1,8,-5,2,-4,7,9,3,8,8,3,-2,2,-6,-6,-1,-8,8,7,5,10,-1,7,-2,-4,-2,8,1,-3,-1,6,5,-2,9,3,-1,10,-2,10,10,6,-2,-8,-4,-2,10,-6,-3,-10,-10,-10,5,-4,7,-3,-9,-10,3,6,9,-10,-5,5,-7,-2,-7,-9,-2,-1,9,5,3,9,-3,5,2,-10,4,-6,-10,9,3,-2,-10,-4,-7,7,2,7,-10,7,8,8,5,-4,-2,-4,8,10,7,9,2,-5,1,-10,-4,2,8,-5,-3,10,9,-2,8,-9,5,10,-3,2,8,-6,10,-8,7,1,-2,7,5,-10,-1,-9,-6,-4,7,-6,9,-9,9,7,-1,-6,-1,4,-2,10,-3,2,9,10,-3,3,8,2,9,3,-2,-3,-4,9,-1,-1,-8,-4,10,-5,2,-8,-9,-2,-4,8,-6,8,-8,-7,-6,1,-3,2,-3,-10,-4,9,-9,-4,6,8,3,-3,5,-9,-10,6,7,7,-7,-7,5,6,7,-8,4,-6,-6,-9,8,-3,-8,2,-8,-5,7,-8,10,-8,-6,9,-4,6,-3,-10,-2,-9,-1,6,-3,-4,5,-3,-8,1,9,3,-4,-5,5,-7,-8,7,-9,-1,-4,-3,9,-5,8,8,-7,-1,1,5,3,2,8,3,10,10,-10,-6,-8,3,-8,-3,3,3,2,-9,2,8,-9,-9,-4,-5,-1,-3,-4,7,1,-5,6,8,8,4,-7,9,-3,6,-7,-6,-4,9,7,-9,8,3,-2,5,-8,-1,3,-2,-10,6,1,-8,-10,2,5,-6,-5,-10,-9,10,-3,-2,-3,-3,-3,2,2,9,-7,1,-4,8,5,-8,-10,-2,9,9,8,-5,-10,3,7,4,-4,-7,-4,-10,2,5,-4,6,1,-5,5,10,-9,7,-6,9,8,10,2,10,6,9,-4,-5,-10,6,4,-1,8,8,-1,-3,4,10,3,-3,7,3,7,-10,10,-4,-9,-5,5,10,10,-4,9,2,3,-5,7,6,5,3,-10,-10,-2,-8,8,-4,3,5,-1,8,-10,6,2,-3,8,4,1,-8,1,-3,-6,-9,4,-5,-1,-10,-7,-10,10,7,7,5,7,4,-1,-7,3,-8,-2,-1,7,5,10,4,-9,8,-2,8,6,7,7,6,2,7,8,-8,-9,-10,8,-9,-3,-5,-9,6,2,-5,-7,-1,5,-6,7,-10,7,-7,2,-4,-2,1,9,-9,9,2,-4,-9,-2,-4,7,5,-3,-10,8,-9,-10,-2,-8,-2,4,4,-10,9,-6,-10,6,-8,8,4,-2,8,3,-5,-2,9,2,6,-6,5,-7,-6,10,1,-4,6,8,-1,6,4,-2,4,4,-7,4,-2,-7,-3,4,7,-9,-7,-8,7,-4,-2,2,2,5,-8,-1,1,1,-5,7,5,6,10,10,-8,6,3,-3,6,4,10,-4,-5,4,-10,-3,-5,-8,-3,-4,-5,8,-10,2,-2,10,6,-2,1,-1,4,-7,-3,8,7,4,2,-1,4,8,4,5,-4,-10,-2,5,5,7,-8,3,-4,-7,-10,9,-4,9,7,-7,-10,7,6,-7,5,-10,-10,-8,1,-3,6,6,-10,-9,8,1,10,1,9,8,4,7,-2,-10,-2,5,-6,-9,3,-7,-3,10,-6,1,9,-7,7,10,-9,-4,5,1,8,2,-10,-6,-7,6,7,9,7,2,-2,-5,3,3,9,-1,-8,10,-4,-10,-3,6,-4,-6,3,-6,10,-9,1,1,8,4,-7,-3,-3,1,9,-3,-4,-5,9,-3,1,10,-4,9,-4,-7,1,1,-10,7,-2,4,1,3,9,7,-6,3,7,-1,8,4,-5,-1,-9,-8,-1,7,2,-2,-3,-2,-5,10,-6,6,8,-3,-5,2,5,5,2,9,-1,4,1,5,-10,9,6,2,-5,9,-9,6,-10,-3,-2,-6,-3,-8,-8,-10,8,6,9,1,3,6,2,-10,-2,7,-5,-6,5,3,-7,-4,6,-2,-2,-9,-3,-8,4,9,1,9,-1,4,-8,-1,-2,3,-9,-1,8,-5,-4,7,-3,3,2,-9,8,9,10,5,7,8,-1,-4,-10,9,1,1,2,-7,-9,-5,10,4,-4,-10,5,6,10,4,-8,-3,10,-3,9,7,4,4,8,4,5,2,3,-7,-7,-2,-7,-3,8,-9,6,4,8,6,7,7,-5,3,8,-2,2,-9,6,6,-10,10,1,-9,-3,4,-4,-4,-9,-8,9,-1,1,-10,3,-2,10,-10,7,9,-4,-2,1,9,4,-6,-7,-4,8,7,9,-4,-1,-10,-6,10,4,-10,9,7,-9,4,10,6,1,9,3,9,-2,4,-1,-7,6,10,-7,9,-9,-1,1,7,1,4,-1,-9,5,10,8,9,-3,9,5,7,1,3,5,5,-5,-9,-3,9,10,2,-7,1,-1,1,8,-9,5,-2,1,-4,6,5,2,7,-3,9,1,1,10,-7,-1,-9,8,7,-9,-6,-6,6,6,9,2,1,-8,5,-4,8,1,-2,-7,10,9,4,-8,-3,-4,4,-8,9,-7,4,9,7,-7,2,-7,3,10,-3,-8,5,-9,-7,-5,-5,-1,6,-10,3,-3,5,-9,7,-6,10,-9,3,5,4,-6,-4,7,8,-4,-7,8,-8,10,6,6,-9,2,-2,2,9,-7,7,-7,-3,8,8,6,10,-1,-4,-4,-3,-5,-5,3,6,-1,5,-8,8,2,1,-4,-4,7,4,-10,-10,-2,-1,9,4,-2,7,-9,7,1,-7,-7,7,-10,-7,-8,3,-2,-2,4,2,-6,8,-3,5,1,6,5,-3,-6,3,-9,-3,-5,-1,-2,-6,1,-2,-7,8,-10,-7,10,10,-2,2,-3,2,10,6,-8,2,6,-6,2,-10,-8,7,-7,-6,2,-10,-2,3,-8,6,1,7,-2,2,-9,-6,9,7,-10,7,-10,9,3,-4,10,9,9,-3,-1,5,-7,-6,-4,-6,-7,-8,-4,-1,-10,-8,-6,-6,-2,-6,-3,-2,-9,9,-3,-10,10,9,7,-8,4,9,-10,-5,-3,-5,1,7,6,-5,-10,9,-5,3,8,-10,7,4,-6,2,-1,8,-2,4,-2,7,6,-4,-6,-4,6,9,-7,3,-6,-5,-1,1,-9,-3,5,-2,8,3,-3,-10,-3,4,-4,1,1,-6,-10,-6,-3,-9,9,-1,-9,10,-1,1,-9,-2,-10,-2,-1,-3,-5,-2,-8,-7,4,5,-2,3,5,-5,-9,-9,2,-1,-10,-7,-3,-3,10,9,10,5,-9,5,-4,-2,1,-1,-1,-7,-7,7,-1,-3,4,5,6,-8,-10,-10,-5,-7,-4,-9,-3,7,1,1,6,-5,6,4,9,8,5,6,-2,6,5,4,-2,-9,-7,-6,-6,3,10,5,-7,1,-3,-2,1,-3,-3,-6,10,-9,6,9,-6,-6,-8,-8,-4,-9,-5,3,10,4,-5,-2,6,1,9,-3,-10,3,-10,7,7,2,-8,2,5,3,6,6,-7,1,-6,-10,5,-8,-4,10,10,5,-1,8,-3,-7,-4,-9,9,-6,-8,1,10,8,-4,-5,-2,-4,9,8,-3,-1,5,8,1,7,10,5,-7,4,-3,8,1,-8,-4,-10,-9,-3,-2,8,-5,-5,7,5,-4,5,-7,-5,-5,-7,-9,-7,10,5,-3,5,10,-4,-1,10,9,-3,10,-5,10,5,10,10,-4,-4,-7,-8,1,5,3,9,5,-10,-9,10,-8,-1,-9,-10,5,3,-5,1,2,-9,-3,9,-10,3,-4,1,1,10,-2,-4,-4,-8,-5,6,9,4,-2,10,-2,1,7,7,5,-8,8,5,9,3,-4,-3,2,5,-2,6,-9,9,-1,5,-2,5,7,3,3,9,-3,-10,-2,1,-1,8,-5,7,-1,-4,-7,4,6,9,-3,7,-3,-1,4,-8,10,-7,1,3,-8,9,-5,-9,-2,10,-7,9,8,2,3,-6,-6,-8,-7,-10,-7,10,4,4,-6,-9,-5,-10,10,2,-3,-8,1,3,8,-3,-4,8,-10,2,-7,8,1,3,-1,-7,-5,-1,-3,-4,-10,4,8,10,4,-6,4,3,2,-7,2,5,-10,-2,3,-2,3,-6,9,10,9,4,-10,9,2,-2,1,-10,6,-6,9,1,-7,4,-3,9,10,5,2,-1,9,9,-3,-3,-4,-7,8,-7,-2,-10,3,9,7,-5,-6,-5,2,-7,6,5,10,3,9,-2,8,10,-5,9,10,1,10,1,2,10,-7,-6,-8,-6,10,2,1,-1,8,10,-4,6,-9,-10,6,-6,5,-1,-2,2,4,-2,-3,-5,3,-10,8,-2,4,7,10,-2,-7,9,-9,-3,-4,-10,-8,-9,10,-7,-5,3,-1,-7,4,-7,2,2,9,-4,10,10,-9,-8,-6,5,-6,-1,1,-9,7,5,3,3,-5,-5,-1,3,-3,8,8,3,6], dtype = "uint16")#candidate|3658|(2640,)|const|uint16
var_3659 = relay.var("var_3659", dtype = "int64", shape = (48, 2))#candidate|3659|(48, 2)|var|int64
call_3654 = relay.TupleGetItem(func_3398_call(relay.reshape(const_3655.astype('float64'), [7, 15, 13]), relay.reshape(const_3656.astype('int64'), []), relay.reshape(var_3657.astype('float64'), [770,]), relay.reshape(const_3658.astype('uint16'), [2640,]), relay.reshape(var_3659.astype('int64'), [96,]), ), 11)
call_3660 = relay.TupleGetItem(func_3405_call(relay.reshape(const_3655.astype('float64'), [7, 15, 13]), relay.reshape(const_3656.astype('int64'), []), relay.reshape(var_3657.astype('float64'), [770,]), relay.reshape(const_3658.astype('uint16'), [2640,]), relay.reshape(var_3659.astype('int64'), [96,]), ), 11)
var_3670 = relay.var("var_3670", dtype = "float32", shape = (3, 13, 2))#candidate|3670|(3, 13, 2)|var|float32
bop_3671 = relay.mod(uop_3647.astype('float32'), relay.reshape(var_3670.astype('float32'), relay.shape_of(uop_3647))) # shape=(3, 13, 2)
output = relay.Tuple([bop_3626,call_3643,call_3645,call_3654,const_3655,const_3656,var_3657,const_3658,var_3659,bop_3671,])
output2 = relay.Tuple([bop_3629,call_3644,call_3646,call_3660,const_3655,const_3656,var_3657,const_3658,var_3659,bop_3671,])
func_3683 = relay.Function([var_3625,var_3657,var_3659,var_3670,], output)
mod['func_3683'] = func_3683
mod = relay.transform.InferType()(mod)
mutated_mod['func_3683'] = func_3683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3683_call = mutated_mod.get_global_var('func_3683')
var_3685 = relay.var("var_3685", dtype = "float32", shape = (3, 13, 2))#candidate|3685|(3, 13, 2)|var|float32
var_3686 = relay.var("var_3686", dtype = "float64", shape = (770,))#candidate|3686|(770,)|var|float64
var_3687 = relay.var("var_3687", dtype = "int64", shape = (48, 2))#candidate|3687|(48, 2)|var|int64
var_3688 = relay.var("var_3688", dtype = "float32", shape = (3, 13, 2))#candidate|3688|(3, 13, 2)|var|float32
call_3684 = func_3683_call(var_3685,var_3686,var_3687,var_3688,)
output = call_3684
func_3689 = relay.Function([var_3685,var_3686,var_3687,var_3688,], output)
mutated_mod['func_3689'] = func_3689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3096_call = mod.get_global_var('func_3096')
func_3098_call = mutated_mod.get_global_var('func_3098')
call_3718 = relay.TupleGetItem(func_3096_call(), 0)
call_3719 = relay.TupleGetItem(func_3098_call(), 0)
var_3728 = relay.var("var_3728", dtype = "float32", shape = (3, 13, 2))#candidate|3728|(3, 13, 2)|var|float32
bop_3729 = relay.bitwise_xor(call_3718.astype('uint16'), relay.reshape(var_3728.astype('uint16'), relay.shape_of(call_3718))) # shape=(3, 13, 2)
bop_3732 = relay.bitwise_xor(call_3719.astype('uint16'), relay.reshape(var_3728.astype('uint16'), relay.shape_of(call_3719))) # shape=(3, 13, 2)
func_2284_call = mod.get_global_var('func_2284')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_3733 = func_2284_call()
call_3734 = func_2284_call()
func_2463_call = mod.get_global_var('func_2463')
func_2467_call = mutated_mod.get_global_var('func_2467')
var_3744 = relay.var("var_3744", dtype = "uint16", shape = (2640,))#candidate|3744|(2640,)|var|uint16
call_3743 = relay.TupleGetItem(func_2463_call(relay.reshape(var_3744.astype('uint16'), [2640,]), relay.reshape(var_3744.astype('uint16'), [15, 16, 11]), ), 3)
call_3745 = relay.TupleGetItem(func_2467_call(relay.reshape(var_3744.astype('uint16'), [2640,]), relay.reshape(var_3744.astype('uint16'), [15, 16, 11]), ), 3)
output = relay.Tuple([bop_3729,call_3733,call_3743,var_3744,])
output2 = relay.Tuple([bop_3732,call_3734,call_3745,var_3744,])
func_3747 = relay.Function([var_3728,var_3744,], output)
mod['func_3747'] = func_3747
mod = relay.transform.InferType()(mod)
var_3748 = relay.var("var_3748", dtype = "float32", shape = (3, 13, 2))#candidate|3748|(3, 13, 2)|var|float32
var_3749 = relay.var("var_3749", dtype = "uint16", shape = (2640,))#candidate|3749|(2640,)|var|uint16
output = func_3747(var_3748,var_3749,)
func_3750 = relay.Function([var_3748,var_3749,], output)
mutated_mod['func_3750'] = func_3750
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3752 = relay.var("var_3752", dtype = "int8", shape = ())#candidate|3752|()|var|int8
const_3753 = relay.const([[[10,1,3,-8,7,-5,1,-7],[8,7,4,6,5,4,4,3],[-1,5,8,-8,1,5,-1,2],[2,7,-7,-7,-9,-8,-2,10],[-7,-7,8,-9,-9,5,-7,-7],[-6,4,7,8,2,-2,10,10],[-7,-4,2,-6,-10,-1,7,7],[-4,9,-2,-9,4,1,-3,3],[7,5,-3,-4,-1,1,5,-1],[8,-2,8,7,5,8,-10,-8],[-8,-8,-3,5,7,3,-5,3],[-6,-6,-8,-6,4,9,-5,-10],[-1,6,-3,9,9,6,-8,-9]],[[-3,9,-9,-4,-9,6,-1,6],[7,5,3,1,-6,5,-5,-8],[-9,-2,10,-3,9,2,8,-2],[-10,-6,-1,-4,-6,-10,-3,-1],[-5,-5,9,5,-9,-7,-3,-5],[-4,-5,-10,1,-7,-8,1,-5],[2,-3,-9,-8,3,9,-4,10],[-5,-2,-3,-2,-8,-3,10,5],[-9,5,-7,6,10,-8,10,-4],[-5,10,1,-10,-10,10,-10,-4],[-5,7,-3,2,10,10,9,3],[-10,2,2,-2,5,-4,7,4],[-8,2,5,9,-3,3,2,-6]],[[8,-6,9,5,-10,-1,-9,-8],[7,10,-5,7,-9,10,8,-4],[3,7,7,-8,-10,-3,3,6],[1,-1,-7,4,9,-7,-1,3],[10,10,1,2,4,-2,5,6],[-6,-2,-5,8,2,1,6,-9],[-4,-4,6,10,-1,6,8,4],[1,6,-4,-10,-10,2,-6,4],[2,9,-2,-8,9,1,-8,-3],[2,-4,4,3,-8,-3,5,-4],[-3,-5,-2,-10,-8,8,5,-4],[-1,-3,6,-2,-10,9,-2,2],[-8,2,1,8,-4,-5,10,-6]],[[-10,9,-7,-10,-7,2,-2,7],[-3,-7,-3,-4,-5,-6,8,9],[2,-4,10,6,1,-9,2,2],[-4,-2,7,-6,4,-9,-5,-10],[6,-6,8,-4,-9,3,-8,9],[-5,1,-8,6,8,-4,-4,9],[-8,6,8,6,-2,9,5,2],[-10,4,7,-1,3,-7,10,9],[-1,-6,5,-6,-3,5,-4,6],[9,3,-9,-10,-10,1,2,-1],[-5,4,1,4,-5,-9,-5,3],[6,9,-10,8,-9,1,-9,6],[1,1,-10,-3,-8,-1,9,7]],[[10,1,-9,2,-9,9,7,-3],[7,-10,1,-9,-8,-1,4,4],[-8,-8,7,-6,6,6,5,4],[5,7,7,-6,8,-4,7,-10],[3,5,9,6,-9,9,-4,-3],[6,5,-8,10,8,8,-2,-4],[4,6,-9,9,7,-1,2,9],[4,1,5,-7,5,-10,-2,1],[2,-1,10,-10,-9,-9,4,9],[4,-1,-3,-1,2,5,-8,1],[-4,2,4,4,-4,4,-2,8],[-3,2,5,-4,9,-2,6,6],[8,7,-1,-5,3,-4,2,-1]],[[-1,1,-10,-5,-6,5,-2,5],[10,-2,-2,-9,6,-2,-3,3],[5,10,-1,-2,1,1,10,-3],[-6,5,-2,5,-6,-6,9,5],[-5,7,9,3,1,-5,-9,-3],[-3,-5,3,-5,-6,-1,4,8],[10,-5,9,1,3,-10,4,7],[4,-4,-1,-7,2,3,2,5],[-9,1,2,5,-7,8,-8,1],[-9,8,-4,9,3,-1,-5,8],[-9,-1,2,6,3,-3,3,3],[-8,3,8,-7,-6,-7,-7,7],[4,8,-6,-7,10,-9,5,4]],[[5,-5,-1,-3,3,10,-4,7],[-4,8,-9,8,7,2,-9,5],[-4,-8,-3,2,2,-7,8,6],[10,4,1,9,-1,-1,-9,-6],[-7,8,5,7,1,-4,9,-4],[6,-10,-2,-6,-2,-5,1,4],[8,-9,1,2,1,4,8,1],[-8,2,8,4,2,10,5,-3],[-3,7,8,9,-7,-9,1,-10],[1,-8,7,10,3,5,2,-10],[10,-1,7,10,-3,9,-9,10],[9,8,9,-7,7,-10,-10,6],[-6,-10,8,-6,-9,4,4,-9]],[[-3,-8,6,-5,-7,-2,3,-1],[-4,3,1,5,-6,1,3,2],[-8,8,-8,-6,8,-6,-5,-2],[-7,3,6,-9,6,-4,-1,-5],[-9,-2,-6,3,-8,4,5,-4],[-3,-10,6,-5,1,-1,6,-1],[1,-3,4,10,5,5,2,-2],[-6,-5,-2,-5,10,5,-4,-10],[-2,3,-8,-9,-8,5,-4,6],[9,-2,-4,8,-5,-9,-1,-5],[3,-10,10,6,-4,10,9,-7],[1,-3,-8,-8,-4,-3,9,10],[3,-5,-9,-3,-3,10,10,2]],[[7,-6,-4,8,-3,-3,-9,6],[-4,7,1,8,-4,6,6,-5],[3,7,-6,-5,8,-5,4,-8],[-2,2,6,9,-10,4,-5,10],[2,5,-4,9,2,-8,-5,3],[-1,1,6,-5,-7,4,-10,7],[-2,10,-5,-8,4,3,2,7],[2,-9,9,7,-7,-7,-3,-8],[9,3,-6,-2,6,-10,-3,2],[-6,-6,-6,-1,3,-9,2,-3],[5,4,-6,-4,4,-3,-10,2],[5,-10,-10,6,-7,-10,-4,8],[1,-1,-10,1,8,1,-8,-5]],[[-9,-6,4,-2,8,-9,-7,10],[-3,-4,5,-9,9,2,-10,-2],[9,-10,1,5,-4,-2,3,10],[4,-9,9,-5,-7,-10,3,8],[10,-7,9,-2,8,5,-7,-7],[9,3,3,8,4,-7,-10,9],[2,-2,-7,4,-8,7,4,-6],[8,-10,-7,1,6,8,-10,7],[2,2,2,5,5,-5,5,-9],[-3,6,-7,1,4,3,-6,-5],[-10,6,-3,1,-4,-4,-10,-2],[1,-2,4,6,-5,-1,7,-7],[-4,-8,7,-2,10,8,10,2]],[[9,-2,9,10,-4,5,8,10],[-9,9,-10,7,-9,-9,-6,-10],[4,9,-7,9,1,-5,-10,-2],[-3,-4,-2,-2,-7,-9,1,9],[9,-1,8,-10,-6,9,9,-4],[4,5,1,6,10,3,5,9],[2,2,3,-1,8,6,3,10],[-10,-3,6,-10,-5,10,-7,-5],[2,-10,-1,6,3,9,-2,3],[-5,2,6,-10,7,2,-10,6],[4,8,9,7,4,7,-6,-5],[-9,-4,2,-7,-5,-4,3,6],[-8,-5,8,8,-7,-5,9,5]],[[10,-2,-3,-1,5,-3,7,-8],[-6,1,-4,-4,-8,-5,3,-5],[-7,-7,-6,-1,4,-1,-3,-8],[-1,-3,-10,5,9,2,-10,-7],[6,9,10,2,4,-7,-4,6],[-3,-10,7,10,-7,-8,-1,-4],[-6,-6,-3,-4,-4,3,-7,-5],[9,3,3,2,6,-5,-4,4],[1,8,-10,10,5,-4,-4,5],[4,-9,-1,-7,10,6,2,-6],[9,9,-8,5,-4,-8,-8,2],[-10,9,2,10,9,-8,5,-3],[7,4,-1,-1,-8,3,-9,-7]]], dtype = "int8")#candidate|3753|(12, 13, 8)|const|int8
bop_3754 = relay.equal(var_3752.astype('bool'), const_3753.astype('bool')) # shape=(12, 13, 8)
func_523_call = mod.get_global_var('func_523')
func_527_call = mutated_mod.get_global_var('func_527')
const_3760 = relay.const([0.097366,8.399427,1.788190,7.273075,4.287391,-4.876462,8.790388,2.180694,3.860035,-5.622683,2.508569,3.966599,-4.156384,5.964192,-6.977233,1.760109,-2.038336,-5.877893,9.388812,-4.825342,0.286393,-3.411341,-2.173757,7.213214,0.828396,-9.488620,9.625146,0.835598,1.096737,4.212835,-5.310434,3.002591,4.913467,-3.805725,8.046501,-9.131130,-6.824078,7.724177,-3.837630,-1.024168,-5.030884,-9.581978,2.442083,1.584984,-0.194344,-4.685491,-7.631224,8.556630,7.791216,-6.251119,-3.132610,9.859752,9.866378,-7.091888,-9.165582,0.311717,0.805468,-1.083764,-6.349063,7.442513,-8.149021,8.097667,-9.462662,-7.805723,7.036573,-2.199226,0.089324,-1.614445,8.144653,-3.693608,2.063729,-1.999317,-2.847558,3.871116,2.384507,0.381444,-4.343680,-6.429239], dtype = "float32")#candidate|3760|(78,)|const|float32
call_3759 = relay.TupleGetItem(func_523_call(relay.reshape(const_3760.astype('float32'), [3, 13, 2]), relay.reshape(const_3760.astype('float32'), [3, 13, 2]), ), 1)
call_3761 = relay.TupleGetItem(func_527_call(relay.reshape(const_3760.astype('float32'), [3, 13, 2]), relay.reshape(const_3760.astype('float32'), [3, 13, 2]), ), 1)
uop_3762 = relay.atan(call_3759.astype('float64')) # shape=(3, 13, 2)
uop_3764 = relay.atan(call_3761.astype('float64')) # shape=(3, 13, 2)
output = relay.Tuple([bop_3754,const_3760,uop_3762,])
output2 = relay.Tuple([bop_3754,const_3760,uop_3764,])
func_3769 = relay.Function([var_3752,], output)
mod['func_3769'] = func_3769
mod = relay.transform.InferType()(mod)
var_3770 = relay.var("var_3770", dtype = "int8", shape = ())#candidate|3770|()|var|int8
output = func_3769(var_3770)
func_3771 = relay.Function([var_3770], output)
mutated_mod['func_3771'] = func_3771
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3886 = relay.var("var_3886", dtype = "bool", shape = ())#candidate|3886|()|var|bool
var_3887 = relay.var("var_3887", dtype = "bool", shape = (7, 12, 8))#candidate|3887|(7, 12, 8)|var|bool
bop_3888 = relay.logical_and(var_3886.astype('bool'), var_3887.astype('bool')) # shape=(7, 12, 8)
bop_3910 = relay.power(bop_3888.astype('float32'), var_3886.astype('float32')) # shape=(7, 12, 8)
func_1076_call = mod.get_global_var('func_1076')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_3916 = relay.TupleGetItem(func_1076_call(), 1)
call_3917 = relay.TupleGetItem(func_1077_call(), 1)
output = relay.Tuple([bop_3910,call_3916,])
output2 = relay.Tuple([bop_3910,call_3917,])
func_3926 = relay.Function([var_3886,var_3887,], output)
mod['func_3926'] = func_3926
mod = relay.transform.InferType()(mod)
mutated_mod['func_3926'] = func_3926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3926_call = mutated_mod.get_global_var('func_3926')
var_3928 = relay.var("var_3928", dtype = "bool", shape = ())#candidate|3928|()|var|bool
var_3929 = relay.var("var_3929", dtype = "bool", shape = (7, 12, 8))#candidate|3929|(7, 12, 8)|var|bool
call_3927 = func_3926_call(var_3928,var_3929,)
output = call_3927
func_3930 = relay.Function([var_3928,var_3929,], output)
mutated_mod['func_3930'] = func_3930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_831_call = mod.get_global_var('func_831')
func_833_call = mutated_mod.get_global_var('func_833')
call_3976 = relay.TupleGetItem(func_831_call(), 1)
call_3977 = relay.TupleGetItem(func_833_call(), 1)
uop_3994 = relay.cosh(call_3976.astype('float64')) # shape=(3, 13, 2)
uop_3996 = relay.cosh(call_3977.astype('float64')) # shape=(3, 13, 2)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_3997 = relay.TupleGetItem(func_2494_call(), 0)
call_3998 = relay.TupleGetItem(func_2496_call(), 0)
output = relay.Tuple([uop_3994,call_3997,])
output2 = relay.Tuple([uop_3996,call_3998,])
func_4005 = relay.Function([], output)
mod['func_4005'] = func_4005
mod = relay.transform.InferType()(mod)
mutated_mod['func_4005'] = func_4005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4005_call = mutated_mod.get_global_var('func_4005')
call_4006 = func_4005_call()
output = call_4006
func_4007 = relay.Function([], output)
mutated_mod['func_4007'] = func_4007
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4017 = relay.var("var_4017", dtype = "float64", shape = (4, 3, 16))#candidate|4017|(4, 3, 16)|var|float64
uop_4018 = relay.atan(var_4017.astype('float64')) # shape=(4, 3, 16)
func_2284_call = mod.get_global_var('func_2284')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_4023 = func_2284_call()
call_4024 = func_2284_call()
func_489_call = mod.get_global_var('func_489')
func_491_call = mutated_mod.get_global_var('func_491')
call_4039 = relay.TupleGetItem(func_489_call(), 0)
call_4040 = relay.TupleGetItem(func_491_call(), 0)
bop_4055 = relay.subtract(var_4017.astype('uint32'), relay.reshape(uop_4018.astype('uint32'), relay.shape_of(var_4017))) # shape=(4, 3, 16)
uop_4058 = relay.exp(bop_4055.astype('float32')) # shape=(4, 3, 16)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_4062 = func_407_call()
call_4063 = func_407_call()
output = relay.Tuple([call_4023,call_4039,uop_4058,call_4062,])
output2 = relay.Tuple([call_4024,call_4040,uop_4058,call_4063,])
func_4067 = relay.Function([var_4017,], output)
mod['func_4067'] = func_4067
mod = relay.transform.InferType()(mod)
var_4068 = relay.var("var_4068", dtype = "float64", shape = (4, 3, 16))#candidate|4068|(4, 3, 16)|var|float64
output = func_4067(var_4068)
func_4069 = relay.Function([var_4068], output)
mutated_mod['func_4069'] = func_4069
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4122 = relay.const(4, dtype = "uint8")#candidate|4122|()|const|uint8
var_4123 = relay.var("var_4123", dtype = "uint8", shape = (7, 13, 15))#candidate|4123|(7, 13, 15)|var|uint8
bop_4124 = relay.greater_equal(const_4122.astype('bool'), var_4123.astype('bool')) # shape=(7, 13, 15)
output = relay.Tuple([bop_4124,])
output2 = relay.Tuple([bop_4124,])
func_4128 = relay.Function([var_4123,], output)
mod['func_4128'] = func_4128
mod = relay.transform.InferType()(mod)
var_4129 = relay.var("var_4129", dtype = "uint8", shape = (7, 13, 15))#candidate|4129|(7, 13, 15)|var|uint8
output = func_4128(var_4129)
func_4130 = relay.Function([var_4129], output)
mutated_mod['func_4130'] = func_4130
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4135 = relay.var("var_4135", dtype = "float64", shape = (6, 4, 5))#candidate|4135|(6, 4, 5)|var|float64
uop_4136 = relay.acosh(var_4135.astype('float64')) # shape=(6, 4, 5)
func_699_call = mod.get_global_var('func_699')
func_701_call = mutated_mod.get_global_var('func_701')
var_4140 = relay.var("var_4140", dtype = "int64", shape = ())#candidate|4140|()|var|int64
call_4139 = relay.TupleGetItem(func_699_call(relay.reshape(var_4140.astype('int64'), [])), 3)
call_4141 = relay.TupleGetItem(func_701_call(relay.reshape(var_4140.astype('int64'), [])), 3)
func_1108_call = mod.get_global_var('func_1108')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_4142 = relay.TupleGetItem(func_1108_call(), 1)
call_4143 = relay.TupleGetItem(func_1109_call(), 1)
func_2774_call = mod.get_global_var('func_2774')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_4144 = relay.TupleGetItem(func_2774_call(), 1)
call_4145 = relay.TupleGetItem(func_2775_call(), 1)
output = relay.Tuple([uop_4136,call_4139,var_4140,call_4142,call_4144,])
output2 = relay.Tuple([uop_4136,call_4141,var_4140,call_4143,call_4145,])
func_4163 = relay.Function([var_4135,var_4140,], output)
mod['func_4163'] = func_4163
mod = relay.transform.InferType()(mod)
var_4164 = relay.var("var_4164", dtype = "float64", shape = (6, 4, 5))#candidate|4164|(6, 4, 5)|var|float64
var_4165 = relay.var("var_4165", dtype = "int64", shape = ())#candidate|4165|()|var|int64
output = func_4163(var_4164,var_4165,)
func_4166 = relay.Function([var_4164,var_4165,], output)
mutated_mod['func_4166'] = func_4166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_831_call = mod.get_global_var('func_831')
func_833_call = mutated_mod.get_global_var('func_833')
call_4202 = relay.TupleGetItem(func_831_call(), 0)
call_4203 = relay.TupleGetItem(func_833_call(), 0)
var_4206 = relay.var("var_4206", dtype = "float32", shape = (3, 13, 2))#candidate|4206|(3, 13, 2)|var|float32
bop_4207 = relay.greater_equal(call_4202.astype('bool'), relay.reshape(var_4206.astype('bool'), relay.shape_of(call_4202))) # shape=(3, 13, 2)
bop_4210 = relay.greater_equal(call_4203.astype('bool'), relay.reshape(var_4206.astype('bool'), relay.shape_of(call_4203))) # shape=(3, 13, 2)
func_2547_call = mod.get_global_var('func_2547')
func_2550_call = mutated_mod.get_global_var('func_2550')
const_4212 = relay.const([5.123929,2.800328,8.522525,4.465534,-1.116613,6.672281,-5.218963,4.853407,-3.288133,-4.448432,7.324211,7.240162,-8.728417,-2.406257,-7.459971,-4.373320,-0.707582,-3.436026,-2.140266,-9.227902,5.109764,-5.836654,7.518741,8.069001,7.196650,7.001030,2.194885,0.017933,-9.870545,7.473845,-7.372507,0.758544,2.929421,6.684194,9.498433,-6.909744,0.814992,-7.519370,-7.506557,-8.219106,5.910954,-7.277288,-2.643708,-4.151224,1.746283,2.605036,4.337815,-5.639401,-5.179264,-7.635249,7.938983,-0.322402,-0.807920,8.777166,0.512135,-3.803810,-6.591386,8.099768,-2.670027,8.645799,-8.996291,5.781822,6.185883,-8.007683,2.397646,1.917151,-7.747875,8.491288,2.709531,0.035315,-5.168377,1.883236,4.588953,-7.015148,9.591744,5.321796,-9.300762,2.344059,8.867402,-3.004050,2.697863,8.664152,4.320540,-2.523746,-9.022811,9.435527,5.470538,4.267369,-3.457486,-5.438550,7.719733,5.354250,-1.315046,-6.364597,-1.658297,7.012446,-5.215964,2.123586,2.601105,-7.669932,-6.126232,3.994626,7.246872,-4.895745,-2.029590,7.795243,-2.738755,1.917468,6.024388,-8.236289,-6.661802,9.576293,0.305533,4.032685,-5.194762,-3.955946,9.231773,-4.311266,-1.987395,-2.101448,5.598814,-1.216208,-6.139669,2.985365,0.570217,-5.216197,0.895598,3.238530,-3.814596,5.371726,-7.765827,8.574356,5.184796,-5.039673,-6.713037,-7.773150,-2.971023,-8.132741,1.110856,3.551899,6.206113,-1.930287,3.715242,7.716960,-8.347192,5.889514,-0.499612,0.889595,-6.429582,8.017883,-7.088718,6.557984,9.621087,-8.421747,6.719881,1.246739,2.357916,3.250262,2.903134,-6.238732,7.975839,4.718897,1.454681,-5.108825,-7.303803,-6.039055,5.559002,-4.797070,0.363764,8.191322,-1.904469,-6.702617,4.928123,-7.956861,-9.162802,-2.734550,-9.336104,-6.125579,-4.023936,-3.808704,-2.997363,-5.904903,-1.046947,-8.507856,2.990866,-6.626125,0.674632,5.771124,-2.226049,7.768315,-2.596817,-1.512215,9.919010,-5.269573,8.867042,5.592625,-1.216027,-0.436199,-9.280558,-2.263063,-4.759357,2.629819,3.374157,-4.214414,-0.735124,6.280753,-3.363781,-5.728925,-4.994146,2.607849,1.775324,4.845822,-2.174370,-8.726472,8.842836,-3.081261,1.806973,4.148907,-9.630883,-9.631355,8.893410,-9.880009,1.247572,-0.426390,4.651386,-2.857044,-8.603086,-7.183963,9.541737,9.995784,-3.869326,-6.252107,8.614317,-0.372256,-5.276336,-0.074202,-1.287132,1.667484,5.291334,4.951085,5.951442,0.610565,-1.656969,1.356570,-3.496380,-0.472109,-2.171152,-8.815275,-6.850541,-7.850629,6.356840,-5.452020,2.005968,-3.003706,9.705515,5.462660,2.297326,-5.310136,1.379189,5.207298,-5.816912,-2.753723,-3.011249,-5.057149,5.976172,3.399427,-6.224789,6.121385,0.982837,-5.184880,8.061814,-5.318170,8.530306,-7.271008,-9.505485,-0.207766,4.062379,3.013781,-6.563488,-6.730714,-6.100721,-6.751479,-3.873341,-5.185115,6.094442,-6.046853,6.525866,1.906510,-6.507084,6.934640,4.450778,9.562337,-3.571146,4.108533,6.002461,-3.760173,4.218125,-1.464154,-5.986131,-3.913192,7.963040,5.964791,6.985543,1.464464,-5.560372,-1.701273,6.728753,4.462149,-2.897954,-6.433826,-9.734184,-8.350108,8.843642,6.734509,3.559335,-7.701816,3.330743,7.964248,-6.081187,-5.280947,4.247167,2.087820,-8.965446,-8.533626,3.739185,-9.884103,-4.406189,8.099727,1.869752,1.834179,-2.420055,-0.865859,2.897378,-8.551661,-5.565758,3.214340,0.786413,-7.830940,3.819235,1.622868,3.638766,-3.203775,-5.151779,-5.928436,6.060803,-1.877097,7.634898,8.452575,5.180075,-4.930519,-3.357907,1.553007,-4.513714,2.574954,2.969525,-1.282205,0.414292,-6.392725,0.387803,5.266255,-7.650522,-2.161063,-0.777596,5.474648,-6.544257,-8.786895,9.397166,-1.631728,6.308451,6.469818,-9.128915,-8.387413,-7.552244,9.234358,8.939087,-4.433038,2.917059,7.937964,-6.947902,8.616294,-5.216512,2.395310,2.915804,-5.114720,-9.630746,3.451763,0.284575,-3.979524,-0.767310,2.341878,-9.157607,-4.939606,0.174088,-7.012244,-1.176507,-6.787694,9.550060,-0.021971,4.417246,8.777672,-2.197834,1.654620,-8.276024,3.517909,5.508107,-7.337401,3.297862,8.859323,-0.307498,-3.681524,6.717450,-3.044449,4.059489,-5.389746,1.654748,-2.477630,-2.562681,7.023388,9.905627,-7.820879,-5.968400,-7.375009,4.425249,-7.446335,3.034147,-9.338990,9.667917,5.077042,9.566377,8.387405,-9.903707,-0.774644,3.103395,7.559495,-7.821900,-7.946360,8.845853,-8.898309,-1.647115,-8.144432,-9.607167,0.933854,3.127057,-1.666025,-8.412496,5.770683,2.094088,2.148473,-8.351744,8.333565,-9.955839,5.479704,-5.030185,-6.052606,-8.914294,8.888244,8.523375,-6.642183,3.342965,7.030759,-0.460741,-1.672532,-3.591200,9.140262,5.403541,-7.141759,-1.493377,4.088063,4.166337,9.402259,-5.899883,-1.369993,8.260328,7.021028,7.323473,-3.562872,8.397278,5.699108,9.321211,-6.669741,4.867690,-6.988839,-5.424693,4.265357,-2.854677,7.443309,4.504681,-9.576105,-6.118634,3.750376,6.330278,-9.699063,9.378279,-5.719350,-2.302134,7.894001,3.070077,9.700081,2.728248,-2.420424,2.658398,-9.616011,1.545396,-3.203275,-2.684141,-7.135567,6.497660,7.639333,-9.470894,3.632472,-5.067645,1.337592,8.071106,-1.722644,1.732827,-2.429779,-1.671845,1.118996,3.844050,-3.086776,0.663270,0.682892,4.767408,0.850942,6.093093,-5.460084,3.806294,6.884150,-6.860855,7.502737,-5.214384,-9.573106,0.463286,4.468134,0.623532,-4.311946,-5.735629,-4.230941,-7.218416,0.260593,-7.521522,-7.245954,9.523609,-5.556648,0.851030,6.033896,3.442512,-6.089008,8.094594,-8.741693,4.635502,-5.360403,-4.033817,6.076402,-8.950864,-2.157972,-0.231464,4.208812,4.854268,1.385708,5.988747,-1.985411,5.238577,8.883700,-3.012514,6.362773,9.644746,4.100330,-5.406011,-7.686376,-3.645524,-3.968529,6.559220,-8.499235,3.140203,9.572183,2.159062,-4.460150,5.792046,8.292325,0.565077,7.866003,-4.036805,-5.825246,-8.734713,-6.960058,-9.903871,9.925622,-5.401558,-9.015258,-2.609400,-4.327271,2.030394,-9.335913,0.665556,4.592221,-2.342433,7.837748,2.496848,-9.148683,-2.520537,-6.564123,0.247713,4.584433,-6.697477,4.209127,9.931498,-8.920118,-8.491709,7.244089,-0.728658,-2.393733,-8.593489,-6.761893,-4.128858,9.524038,6.752159,3.029937,4.478903,-9.891372,-2.408464,-0.389255,7.722944,-9.023579,9.861468,0.771096,-0.235650,5.252416,9.195240,8.860118,-1.702160,1.070823,-3.018517,-1.217273,7.082622,1.038830,-1.739692,6.078560,-9.168501,-6.472409,-6.675461,-8.026385,3.491674,7.294321,9.016862,-2.248203,8.588586,1.430969,-1.364284,9.535872,-1.959157,6.674575,2.472219,-7.727155,9.138192,1.455053,4.698692,-5.222446,7.617360,2.957342,-7.884506,-9.445596,8.441188,-3.415328,5.154734,7.109315,-6.520414,9.570474,-4.835649,-7.017736,-6.801258,6.377527,8.441444,-2.145579,9.735428,1.689220,-6.880049,5.740834,6.059296,9.259058,6.213000,-1.738812,-4.797167,9.935543,3.623778,-3.987640,-3.681855,5.727452,1.885716,-8.879992,-6.021956,9.446633,-1.367543], dtype = "float64")#candidate|4212|(693,)|const|float64
call_4211 = func_2547_call(relay.reshape(const_4212.astype('float64'), [7, 11, 9]))
call_4213 = func_2547_call(relay.reshape(const_4212.astype('float64'), [7, 11, 9]))
output = relay.Tuple([bop_4207,call_4211,const_4212,])
output2 = relay.Tuple([bop_4210,call_4213,const_4212,])
func_4241 = relay.Function([var_4206,], output)
mod['func_4241'] = func_4241
mod = relay.transform.InferType()(mod)
mutated_mod['func_4241'] = func_4241
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4242 = relay.var("var_4242", dtype = "float32", shape = (3, 13, 2))#candidate|4242|(3, 13, 2)|var|float32
func_4241_call = mutated_mod.get_global_var('func_4241')
call_4243 = func_4241_call(var_4242)
output = call_4243
func_4244 = relay.Function([var_4242], output)
mutated_mod['func_4244'] = func_4244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3305_call = mod.get_global_var('func_3305')
func_3307_call = mutated_mod.get_global_var('func_3307')
call_4310 = relay.TupleGetItem(func_3305_call(), 1)
call_4311 = relay.TupleGetItem(func_3307_call(), 1)
func_2529_call = mod.get_global_var('func_2529')
func_2532_call = mutated_mod.get_global_var('func_2532')
const_4319 = relay.const([-10,5,-3,-9,-1,-2,-10,10,7,8,-9,-6,6,7,7,-5,10,4,-10,6,9,2,10,-5,-5,-2,1,9,6,-7,1,2,10,7,-9,3,-10,-7,6,9,8,8,-1,-5,10,-2,3,-4,-7,5,1,6,-3,-4,-9,-10,6,4,-2,4,2,5,-7,-8,-8,-4,1,4,7,2,-3,-2,-10,-6,-9,4,-6,7,-8,2,8,-6,-8,-4,8,-10,10,-10,8,1,-6,-9,6,10,2,9,-7,-10,5,9,-2,4,9,-2,-2,6,-2,4,2,-1,3,-4,-6,7,-10,5,-3,6,7,-3,-5,-8,-4,4,-4,10,-6,10,-1,-5,3,-7,-1,2,-2,-8,4,5,-6,-5,3,-10,2,-3], dtype = "int8")#candidate|4319|(144,)|const|int8
call_4318 = relay.TupleGetItem(func_2529_call(relay.reshape(const_4319.astype('int8'), [9, 2, 8])), 0)
call_4320 = relay.TupleGetItem(func_2532_call(relay.reshape(const_4319.astype('int8'), [9, 2, 8])), 0)
func_3747_call = mod.get_global_var('func_3747')
func_3750_call = mutated_mod.get_global_var('func_3750')
const_4340 = relay.const([7,1,-1,9,7,-5,-1,1,8,6,-5,6,4,10,-2,-5,6,6,-1,1,4,3,3,-1,-5,-8,10,2,6,1,6,-7,-3,2,-8,4,-1,7,-2,-4,-7,-5,-10,2,-6,-4,-8,5,-5,-7,-1,7,9,-5,4,8,-4,10,-8,10,3,8,-6,-5,9,-4,-5,2,4,-7,-7,-10,7,-6,10,1,-1,-7,2,-8,3,3,2,6,-3,6,7,4,4,1,6,-9,2,2,7,-9,3,-10,7,2,-8,-1,-2,1,5,-4,-7,-5,-9,7,8,-6,-7,-5,10,-6,6,5,2,-8,9,7,-4,-5,1,9,-7,10,1,8,-3,-2,-2,8,3,3,5,8,-2,2,-4,-5,-8,-2,-10,-2,5,-1,1,10,-5,-5,-3,-2,3,-10,-9,-7,10,5,2,-3,9,3,-5,-3,-6,-3,-9,-3,10,-1,-8,3,-10,8,-6,-8,-4,5,3,-10,-6,7,-7,-2,-8,6,-3,-4,9,-4,10,10,-2,5,-4,-6,7,10,8,3,-4,1,-9,-10,-6,3,-6,-2,-7,8,2,-4,9,-3,5,-2,4,-6,-8,-1,-1,-10,5,-9,-1,-6,1,1,5,7,-9,-10,-2,-6,-5,5,-9,-6,9,9,-10,-2,-6,-9,7,10,4,-9,-10,-7,1,-2,-6,-5,2,4,10,3,9,6,9,-1,7,1,4,2,-7,6,-3,-8,-6,6,-10,-1,-4,-6,4,-8,-9,8,-5,9,-7,5,9,-4,6,2,-1,-7,-1,-8,10,5,4,-5,8,-1,10,-2,9,-3,-7,3,7,5,-2,-2,-8,4,-4,1,2,4,9,-10,-5,-5,9,10,-7,5,-7,-4,5,9,6,1,3,9,-3,-10,3,1,-1,-9,6,-10,10,-10,-1,-4,10,-4,-1,2,-5,2,-8,-1,4,9,-1,-2,4,-5,10,1,-3,2,-1,7,9,-5,2,5,-5,5,5,8,1,4,3,1,4,9,10,-1,-5,5,2,7,-6,3,2,-1,-5,6,4,-3,3,-4,-9,-1,5,4,-3,5,3,-1,1,10,8,-5,3,1,-1,-8,-3,-5,-4,6,-9,-9,10,9,-1,-9,-5,3,4,4,2,4,-3,-4,7,4,-10,10,10,-3,-10,-4,-9,-3,-3,-6,10,-8,10,-8,3,-5,-3,-5,6,-8,2,-1,8,-2,10,-6,10,1,-8,-9,1,6,-10,-10,8,-5,1,1,-10,2,3,-8,2,4,-10,-2,8,-6,-8,-7,4,9,9,-7,-3,7,-5,-10,6,-8,5,-7,6,3,8,2,-1,-9,1,9,3,1,-1,-6,2,-3,-3,-2,-2,5,-5,5,-6,-8,10,-2,-3,2,3,-3,1,-6,4,5,2,-9,-5,-5,-7,-9,-2,10,5,9,2,-4,6,9,-7,10,-4,-8,-1,3,8,7,-4,-5,-10,6,-4,7,8,2,2,-5,-10,7,-8,1,2,-5,-6,-5,5,-8,-2,9,-3,-5,4,3,-5,-5,-1,-10,-4,-9,-7,7,-6,1,4,-7,-2,3,-6,-1,-5,5,-3,-8,10,-9,2,9,3,-5,1,-3,8,-10,-10,-5,-9,2,-5,-1,10,4,-6,-9,4,-5,7,7,-3,10,-9,-10,-7,-10,-3,-9,-3,-4,-5,-9,8,-1,3,2,6,9,9,4,2,-10,9,9,-2,2,-5,-6,6,-9,9,4,5,1,-3,-4,2,-1,1,2,2,-3,-6,1,8,10,-3,-3,10,-6,2,9,2,-5,-1,-8,-3,-1,2,9,-5,-7,5,-9,-7,-7,5,-3,7,1,6,-2,-2,6,-8,4,-7,-4,-5,7,-9,1,2,2,1,-1,7,-6,8,-3,-8,-2,1,7,-10,-8,-9,-7,-10,-2,4,-7,-7,-10,-6,3,-1,9,10,10,10,-3,4,10,8,-6,-7,3,-8,9,5,8,-7,-2,2,-1,7,-1,-5,-6,5,5,-4,6,-1,-4,6,-6,8,4,-9,4,8,-8,6,-5,-3,5,-1,1,-7,-10,-8,8,4,8,6,9,5,8,-9,-6,-5,4,-3,10,10,3,-8,-6,4,6,-3,-5,-2,4,7,-8,1,10,6,4,-2,6,7,-4,3,10,-5,-6,7,8,10,-8,-7,6,10,9,-6,-6,6,-5,-10,-5,-9,1,1,-2,5,-1,-10,-6,-7,-6,2,6,-2,7,6,-6,-4,-3,-6,5,6,-6,3,9,-10,2,9,-2,-9,-2,2,9,4,-1,6,-2,2,-1,9,-6,6,-3,-6,-7,-3,-7,8,-10,-8,1,-9,-8,-10,-9,-8,-9,10,1,-4,-8,-9,1,3,-8,-6,-6,-1,-7,3,1,10,-8,-10,6,-7,-3,3,2,7,8,-8,-8,3,1,3,7,-9,-4,4,-7,6,9,-3,-5,2,6,2,-10,-1,-8,2,10,4,2,-3,1,10,9,3,-6,9,-7,-7,-3,8,5,-1,-1,8,-3,4,-10,-5,10,5,3,7,3,6,4,-1,4,-1,-7,2,-10,5,3,-1,8,-8,-9,8,8,-10,-10,1,-3,10,-3,-9,9,7,3,-4,3,9,-6,4,5,-8,6,-8,4,-8,-10,-2,-10,2,6,-4,9,-10,4,-3,-1,1,-2,6,-7,-5,-1,8,9,-7,-8,-3,-4,-4,-1,5,-9,9,5,9,10,-1,-4,-4,-10,7,2,7,-7,4,7,9,-8,-9,-4,7,2,-4,-8,9,-9,-6,-8,-7,-3,10,10,7,-8,1,3,-5,-7,-5,-9,-2,1,-9,10,-2,5,-4,3,-5,8,-4,-5,9,-8,-8,7,5,-8,8,8,-1,-4,-10,-4,10,10,-4,1,-8,6,-7,-5,-4,7,-9,2,10,4,-2,4,2,-6,-10,8,9,5,8,8,-3,1,-10,3,-10,-9,-7,6,8,4,10,-7,7,-3,-3,6,-6,1,4,5,3,6,-6,7,-4,-1,6,-1,3,9,-7,-6,-4,8,-3,1,6,5,-2,5,5,10,7,6,7,7,-10,8,10,-1,-8,8,-2,5,5,-9,5,4,3,1,-3,8,1,-7,-2,3,-5,-6,-4,-10,-9,1,-10,-6,-3,7,-5,-1,-8,7,-9,2,1,-10,8,-6,-10,-5,-2,-7,9,-2,6,-9,2,-6,8,6,7,6,7,-6,-9,-1,-1,-5,-10,-5,2,3,-1,6,9,9,-7,3,9,3,10,8,-2,-4,-3,9,4,-7,10,-4,-5,-7,10,-10,-1,6,9,-7,-10,-3,9,-6,5,9,9,6,-8,10,-5,6,5,9,7,-3,4,-10,2,-7,-3,4,-10,10,5,6,10,6,-4,-9,9,-10,10,10,-9,-8,-3,-4,5,1,-4,2,8,1,-2,-5,-4,8,8,-7,4,7,8,-2,-7,-4,1,9,3,3,2,-10,4,2,7,7,5,-1,-9,-7,-8,-1,9,10,2,1,1,2,-1,-7,4,-8,-10,-3,1,-9,-2,-10,10,5,1,-8,7,-10,-4,5,-1,-8,-3,1,-10,-7,-1,-5,6,5,-6,-2,2,-3,6,-6,-2,-9,-5,3,3,10,-6,6,-7,-1,-5,7,-4,-6,8,-9,-8,7,1,9,-1,-9,-5,1,6,-6,5,-8,4,1,-8,2,3,9,3,-9,8,1,2,7,4,-9,-7,-7,-3,-2,-3,6,6,-7,5,3,-3,-9,6,3,9,8,10,-6,-6,-3,5,-2,-7,1,-6,-7,9,-3,2,-5,-1,7,-8,4,3,10,1,10,2,1,-6,-6,4,9,9,-9,7,-2,10,7,-7,1,1,-7,-5,-1,-7,-5,6,9,10,-6,3,-1,3,-6,7,8,3,10,-4,-6,-8,3,6,9,-1,2,10,7,-3,4,4,-9,7,-2,10,3,-2,-2,-10,4,-4,5,4,-9,-7,-7,7,8,5,5,10,1,-4,-10,-4,6,-5,-5,-3,3,9,10,6,-10,-8,6,4,-9,2,3,-6,-3,-9,9,3,1,4,10,9,-2,-8,4,8,10,-3,-6,-3,-9,7,6,1,-6,1,6,-5,-7,-7,-4,-6,-4,9,-9,9,7,-5,-10,2,-1,9,5,4,-8,2,-7,-8,7,-1,10,-4,9,-3,8,-4,-10,-6,8,6,-2,-10,7,2,-5,-2,-4,-5,-8,2,4,4,-9,-9,-10,-7,-3,3,-4,6,9,-6,4,8,10,7,5,9,2,3,3,4,6,10,4,9,5,6,7,-1,-3,-2,-2,2,-9,3,6,9,-7,-4,-6,4,-10,-1,4,5,-2,6,6,-7,-5,-6,-10,-5,-6,9,1,5,6,10,10,5,-4,8,-9,4,5,-6,-9,-5,-9,-8,2,6,9,-5,-3,5,-3,7,7,-7,3,1,-6,6,-3,-8,8,-10,-1,-10,-7,-2,-7,2,10,8,5,-5,6,-6,6,5,-7,-4,1,-3,-6,-9,-3,9,-4,-7,6,8,3,-4,-8,-4,-1,-5,2,-3,2,3,4,-7,9,-7,-5,-9,-1,-9,2,-5,-4,7,8,-6,1,6,-1,6,-8,-7,10,-3,-10,1,8,5,8,-7,2,-9,-1,8,7,-4,-9,-7,-10,1,5,-2,-7,2,-10,2,-10,-5,-3,7,-9,6,-3,-8,-5,2,8,-10,2,-8,3,-4,-10,-6,-2,-4,3,10,3,8,4,6,6,8,-10,-4,-8,-5,-7,-1,3,1,-3,3,-8,4,3,-5,5,-10,-10,7,-3,6,5,-1,3,6,5,-4,2,-5,7,7,3,-9,2,-3,-10,6,-8,-6,3,9,-3,10,-2,-2,7,2,-9,-7,1,-7,-10,-8,4,-1,6,-4,2,6,-1,4,-10,-9,9,9,5,3,-10,6,-5,-10,7,-3,10,-5,-10,8,-5,-8,-3,6,-4,7,-2,-10,10,-1,6,5,3,-6,7,2,2,-8,-8,7,5,-8,7,-5,7,-1,8,-8,4,-4,7,4,-8,6,-7,10,5,1,5,8,-10,5,-4,8,9,10,-10,7,7,5,-6,-9,2,-2,4,1,8,-3,-10,-10,-5,-5,5,4,-5,9,2,2,-6,3,4,-5,9,-3,-8,-8,-5,7,-4,3,8,1,-10,5,7,5,1,4,-5,-9,-1,-6,-1,-6,4,6,-3,-3,8,-8,-8,-6,2,-9,6,2,8,-4,2,3,1,-7,6,5,2,1,-8,-8,-7,-9,-6,2,10,-10,8,-8,7,-3,-7,-9,4,8,-8,-2,1,10,4,-1,8,7,-7,4,2,6,-8,10,-6,-3,5,9,-7,-5,-1,-5,8,-4,7,-10,5,-10,-3,-4,9,3,-1,9,-1,8,9,-10,5,3,-2,-3,-8,-2,3,8,-3,5,-3,-3,9,4,-5,6,-8,4,-9,-9,-9,-6,6,6,6,5,-8,-2,2,-6,10,-10,8,-8,-10,5,-7,6,6,-5,5,-2,2,9,-9,2,-4,10,6,-10,7,8,8,-9,5,-7,-6,1,-2,-2,5,2,6,-3,2,-1,-9,-2,4,-1,7,-9,-8,9,-3,3,-4,-9,-9,-7,6,-9,-10,1,-4,4,2,-2,-6,-10,-1,10,10,-10,-2,7,6,2,-8,-9,-7,2,6,2,7,2,-7,-5,-2,3,3,-9,-7,-2,-5,-5,-4,4,3,2,1,7,-6,4,-1,-1,10,-1,2,2,-6,2,6,-10,5,8,-5,4,1,-1,-7,-5,4,-4,3,6,2,9,-7,8,10,5,-3,9,7,4,-6,-2,7,9,-9,9,-4,-1,9,10,-5,7,6,-2,9,8,7,6,-6,-3,-9,-8,3,3,-9,3,9,-4,9,-9,-3,2,7,-3,-2,-7,3,3,5,9,-8,-7,-6,10,-6,4,6,-9,-5,-7,1,5,1,9,1,-9,-4,-5,-9,6,6,3,7,6,-4,-6,-10,10,-8,-9,-9,-9,7,5,-1,-1,2,-8,8,8,10,9,-6,3,-10,-6,-1,3,-1,7,-9,6,4,10,-9,-6,-4,-10,5,-8,-4,-5,-9,6,-7,1,-1,7,4,-7,-8,3,9,-6,-5,-1,-9,7,-3,10,-7,-5,-2,4,-2,9,6,-5,5,9,-6,-2,-7,2,3,-9,5,-7,-8,10,-3,-3,-3,4,-8,8,5,8,9,1,4,-10,-8,5,-9,-8,-6,-1,-9,-6,8,-10,6,-5,10,6,-8,2,-7,-1,-3,-1,2,-9,7,-8,1,-7,8,3,8,3,-8,-3,3,1,5,-7,4,-9,-3,-7,7,-3,-6,4,-6,1,3,6,7,3,1,-2,8,-7,8,-5,-8,1,-5,-7,5,4,1,3,-9,-4,6,5,-9,5,6,4,10,-7,4,7,-3,5,-1,4,5,-2,7,-5,2,4,1,4,-5,8,5,7,6,-2,2,-1,-7,10,-10,8,4,-2,10,-6,-4,-2,-10,7,-3,-7,4,-2,10,-2,-6,2,4,4,-9,9,-7,-4,-2,-6,-7,-1,-10,-3,4,3,-8,1,1,6,-8,-5,5,-3,-8,1,-2,8,5,4,-7,-3,-4,-8,2,4,6,6,-7,-8,7,-10,-4,-5,-10,-10,8,5,-8,6,5,-9,-9,2,-5,3,-10,5,3,-2,-8,1,6,5,-9,3,3,2,-10,-10,-5,-8,-5,-10,10,-3,-8,4,2,-9,2,-4,-5,-5,-3,1,7,4,2,-2,9,3,-4,1,-6,-9,-2,1,9,4,2,-9,-5,-3,-10,1,4,7,1,-6,-10,-7,-5,-2,6,-8,3,9,2,-9,9,-4,-4,-9,-10,-3,-9,3,-9,-10,-2,7,-6,7,8,-10,6,10,-4,-6,-5,5,1,7,2,7,6,3,-10,-9,6,7,-5,1,-5,6,-10,-3,-8,1,8,5,-3,7,9,-6,-9,-7,10,-8,7,-5,4,7,8,3,9,-1,6,-10,6,-10,-8,1,-4,-1,2,7,-3,9,6,9,-10,10,10,3,-3], dtype = "uint16")#candidate|4340|(2640,)|const|uint16
call_4339 = relay.TupleGetItem(func_3747_call(relay.reshape(call_4310.astype('float32'), [3, 13, 2]), relay.reshape(const_4340.astype('uint16'), [2640,]), ), 1)
call_4341 = relay.TupleGetItem(func_3750_call(relay.reshape(call_4310.astype('float32'), [3, 13, 2]), relay.reshape(const_4340.astype('uint16'), [2640,]), ), 1)
output = relay.Tuple([call_4310,call_4318,const_4319,call_4339,const_4340,])
output2 = relay.Tuple([call_4311,call_4320,const_4319,call_4341,const_4340,])
func_4359 = relay.Function([], output)
mod['func_4359'] = func_4359
mod = relay.transform.InferType()(mod)
mutated_mod['func_4359'] = func_4359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4359_call = mutated_mod.get_global_var('func_4359')
call_4360 = func_4359_call()
output = call_4360
func_4361 = relay.Function([], output)
mutated_mod['func_4361'] = func_4361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3096_call = mod.get_global_var('func_3096')
func_3098_call = mutated_mod.get_global_var('func_3098')
call_4376 = relay.TupleGetItem(func_3096_call(), 1)
call_4377 = relay.TupleGetItem(func_3098_call(), 1)
output = relay.Tuple([call_4376,])
output2 = relay.Tuple([call_4377,])
func_4474 = relay.Function([], output)
mod['func_4474'] = func_4474
mod = relay.transform.InferType()(mod)
output = func_4474()
func_4475 = relay.Function([], output)
mutated_mod['func_4475'] = func_4475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1076_call = mod.get_global_var('func_1076')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_4529 = relay.TupleGetItem(func_1076_call(), 2)
call_4530 = relay.TupleGetItem(func_1077_call(), 2)
output = relay.Tuple([call_4529,])
output2 = relay.Tuple([call_4530,])
func_4533 = relay.Function([], output)
mod['func_4533'] = func_4533
mod = relay.transform.InferType()(mod)
output = func_4533()
func_4534 = relay.Function([], output)
mutated_mod['func_4534'] = func_4534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_4558 = relay.TupleGetItem(func_1886_call(), 0)
call_4559 = relay.TupleGetItem(func_1888_call(), 0)
func_3305_call = mod.get_global_var('func_3305')
func_3307_call = mutated_mod.get_global_var('func_3307')
call_4563 = relay.TupleGetItem(func_3305_call(), 0)
call_4564 = relay.TupleGetItem(func_3307_call(), 0)
output = relay.Tuple([call_4558,call_4563,])
output2 = relay.Tuple([call_4559,call_4564,])
func_4573 = relay.Function([], output)
mod['func_4573'] = func_4573
mod = relay.transform.InferType()(mod)
output = func_4573()
func_4574 = relay.Function([], output)
mutated_mod['func_4574'] = func_4574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_4582 = func_458_call()
call_4583 = func_458_call()
func_1278_call = mod.get_global_var('func_1278')
func_1282_call = mutated_mod.get_global_var('func_1282')
var_4592 = relay.var("var_4592", dtype = "int64", shape = ())#candidate|4592|()|var|int64
var_4593 = relay.var("var_4593", dtype = "float64", shape = (7, 110))#candidate|4593|(7, 110)|var|float64
const_4594 = relay.const([5.632464,6.036291,1.906372,-9.121259,-1.878694,6.598617,-1.722933,6.715230,9.587080,-3.565337,-4.744047,-6.416305,0.671306,2.502394,-9.684060,-1.532606,-6.587131,-7.071953,-1.915687,-6.116104,8.462948,7.523799,-3.353764,-3.629313,7.608755,8.971698,-7.096729,-8.827997,8.092514,-9.577482,7.524202,-1.763507,-3.211059,1.064272,7.541456,1.447092,1.558609,8.321448,-3.616804,3.680663,-7.511856,9.689287,-0.715325,-7.349179,-9.921645,6.250162,2.525552,3.400152,-5.409755,8.807096,-7.905976,5.157240,2.478702,-5.610613,-8.005925,7.099025,-5.697839,2.101209,6.271058,0.005174,-8.429538,5.001184,-1.044381,4.413288,1.346022,-7.614791,-7.208336,3.204785,-6.336068,9.527337,7.109724,8.837521,8.457888,-4.992426,-2.076482,-8.269265,-4.948315,0.814194,5.126802,5.337978,0.660030,-2.793333,2.511275,5.271756,8.122942,6.830719,-9.349605,5.673349,8.844904,-1.978129,7.206949,4.657201,-4.749724,-1.400266,8.042789,-6.777336,9.099327,-9.639641,-0.999231,2.418462,-5.984480,-1.216088,5.824153,2.285609,6.980971,3.325452,-3.624528,-3.210415,8.087604,-8.614504,-3.338184,6.060418,-4.631272,1.609360,1.741689,-1.897093,4.007204,-0.135775,-3.000208,7.723833,8.514212,-1.517391,3.252875,-3.698996,5.630421,-5.226114,4.164819,-4.235957,6.558023,-2.339344,-7.328687,8.756462,8.003732,-2.015816,3.460136,7.011055,-7.107477,-2.463029,-4.117048,-1.656507,-1.492358,-7.096863,-6.590004,5.366883,-7.538825,7.001645,-1.430973,-3.174363,-6.097363,-2.558297,-1.632572,7.326057,4.520359,9.575252,-1.238981,-1.830813,-9.741380,1.464831,5.884825,-7.880153,-5.923177,-3.511766,-0.532390,4.750927,2.273878,-9.054492,6.802440,6.887638,-9.433222,9.074645,-9.664860,5.570428,-9.104849,-5.404299,2.055793,6.471757,-7.203552,-3.397654,-8.776675,2.299548,3.407343,2.672908,6.200732,-5.366209,4.905925,6.906363,5.214958,-7.802536,5.635508,1.075848,-6.476887,-8.956782,-5.355823,8.318178,-0.829402,-2.563333,5.876871,0.578231,-5.060145,-2.057601,6.410226,-3.566588,-7.170155,-1.321981,8.934534,-3.568611,-7.335017,-4.590966,4.204660,2.512183,-4.162709,-6.630315,6.854130,8.747691,7.174745,-2.489157,0.389937,2.568962,5.354698,6.188771,9.235375,-2.707308,-4.585153,-0.863770,6.603108,-9.573807,5.632360,2.243004,-4.867841,2.803943,-1.343890,-1.306858,-9.109830,2.515149,0.245454,-0.033917,-0.860728,-1.985904,9.555923,-9.134597,-3.417733,-4.445009,3.222856,-1.656093,-1.703503,4.115073,5.077134,-5.885035,3.521573,-1.409433,-5.691217,8.276726,8.391806,-0.958100,-6.345052,5.831756,9.244520,2.157722,6.899612,-2.625077,6.943441,-0.930621,7.048897,-0.428635,-8.445481,0.411827,1.816281,6.216799,-0.290000,0.396128,8.558173,7.115743,-6.041983,3.690121,-1.207209,-2.462486,-0.155700,8.383658,4.736845,-5.079411,-4.133029,5.481382,1.927832,-0.657139,-4.156080,-1.384158,9.299408,-7.401538,-1.474752,2.325060,2.559666,-2.549136,6.160017,4.338563,9.881843,-4.889727,8.815787,3.325128,9.939430,-1.243155,6.630975,4.284176,-8.222457,5.227827,7.107548,8.479726,-6.535461,-3.233016,7.559460,-7.614371,-5.221514,-6.834754,-9.242091,-5.163116,-2.831702,4.160247,9.002615,-2.734981,-7.809820,2.715333,-1.922739,-2.676382,-8.052224,-5.931376,-4.334090,9.950996,-4.252496,-6.917156,3.704918,-3.036550,5.379374,-3.681607,-2.087665,-8.269595,-0.872785,-0.889530,6.263136,6.587508,-4.468650,0.162065,-8.292269,2.566672,8.714026,-4.355144,-8.767230,-8.037322,-3.354148,-5.118849,4.446278,-5.869024,-4.830804,-4.993171,5.039091,-5.123652,-3.873059,0.541980,-5.270245,6.636180,-3.410785,-5.786739,-4.754252,3.605738,0.450812,1.697487,-1.808446,-8.611718,-6.910963,-5.876024,-7.013195,9.653484,3.563790,-2.007880,8.011947,5.851836,1.894906,-5.920409,-9.171812,-6.329060,-5.401736,-5.803800,3.194089,2.029616,9.196521,-0.817948,-1.319756,-2.258034,-4.545402,9.266916,-4.734051,6.369393,5.890053,8.246872,0.806766,5.268361,2.325189,2.007361,1.207613,2.967245,-9.402809,-6.907455,6.966206,-6.348040,1.194980,-1.365061,-1.483021,8.683634,2.595848,3.271825,2.606721,-7.139232,-9.718012,1.493539,2.486324,9.834705,-6.004670,-8.779993,-1.897342,3.938976,1.322316,-2.357178,-3.309803,5.539670,-8.426939,-8.354760,5.474264,1.116852,-9.723575,0.471984,0.215283,-7.996216,2.197593,1.153562,9.765472,3.382837,-9.450408,7.889325,-1.165780,2.109109,7.120975,-7.119789,-1.712111,7.874169,-7.030338,-9.826965,2.017506,-0.013839,-1.280727,-4.854342,-6.721634,-2.675578,4.536252,3.114984,-6.675606,0.415128,2.260473,-4.624797,6.707745,-3.686759,1.260932,1.107656,6.821710,1.814221,2.597213,-8.889070,3.539459,3.997451,-8.769326,-1.127515,6.558942,-9.107675,9.460010,-1.520325,-0.385192,5.547544,-4.437234,-7.217283,-2.847275,2.899191,-7.335347,2.210847,-3.464009,-5.842351,-2.006763,5.222764,-1.521108,-4.963042,-2.737091,-8.640496,2.935584,-5.907458,-4.358755,-4.583098,-6.238305,9.308786,4.397954,8.140570,4.983851,-9.614880,-7.613990,5.650278,3.116863,1.332974,-8.488911,7.517731,6.941037,5.851421,-7.158608,-8.914993,5.892674,9.083953,-5.613758,-9.141543,9.807062,7.992558,-7.611998,-9.765539,-3.953239,-7.703801,-5.291277,0.997904,9.448202,7.939951,-6.577337,1.258321,9.094821,-5.404832,9.305007,2.716157,5.232568,-9.390240,3.351368,6.790015,-1.693982,8.651680,0.049219,-5.757408,5.962847,4.338232,7.261781,-9.725032,6.904431,7.422900,8.954754,7.386772,6.186490,8.372561,2.152923,8.881801,-6.276547,-2.132856,0.537161,-3.032188,-1.990948,-5.913379,-6.144880,2.328981,7.842720,-9.578556,0.261615,7.260217,-2.224163,-2.203520,2.159199,9.742108,-5.838448,-5.105457,7.041848,-2.281353,-7.132338,8.843342,1.103492,-5.541622,2.269535,-3.204397,3.762605,-1.849045,-1.060337,6.560419,-8.771989,7.242396,-2.914622,-7.137801,-7.457278,5.453773,6.846470,-8.774482,7.263288,9.485794,4.532712,-2.840667,1.571923,-0.586473,4.626653,2.196799,6.653000,-4.171783,-3.066874,7.865150,5.194965,4.901043,8.424563,-8.811876,0.499367,-0.482075,4.230671,8.486478,3.979675,-1.357337,1.730329,-9.614320,-3.260685,-9.195534,9.940406,4.298529,-4.272138,1.785253,-4.360694,1.221730,8.838562,2.282766,-2.349112,9.694546,-9.364320,-0.129658,7.381608,-5.088981,7.047058,8.979219,-9.870122,6.339023,6.244734,1.805754,-7.040992,6.488485,-7.097889,-2.573743,7.648972,-9.414535,5.647198,6.046747,1.239618,-5.868113,-0.991034,1.013694,0.283561,-9.319008,5.552890,-9.706249,-1.297764,9.168926,-0.280257,4.476519,2.550463,-3.074520,-7.908657,8.304705,3.201605,-1.641431,1.932492,3.047295,-3.043066,-7.417392,8.570260,-8.284282,-1.553322,-3.807037,1.907669,0.359926,1.614780,-9.457793,0.532350,5.488938,4.095004,1.944402,5.077487,6.206184,-0.432866,5.414882,8.844587,0.262338,9.280363,-9.793797,7.172091,5.782420,5.410932,-9.127484,7.852261,-6.557489,0.647498,-0.265455,-0.715829,-7.986341,5.830119,-7.988911,5.146423,-2.191374,7.580994,-3.435836,-2.543246,4.892493,8.748104,3.826990,1.471846,0.648456,0.137652,1.756099,-8.437406,-7.778541,2.375670,-4.777964,-3.375165,4.563530,8.782181,-1.943448,6.421326,-6.774221,6.777846,2.368395,0.231749,5.552293,-6.010765,-0.556700,-2.257130,-1.438187,7.049451,2.632806,-5.769294,0.524125,-2.997182,8.566454,6.969884,-5.866323,0.151202,7.799878,-5.077725,1.000437,3.853585,0.837732,-3.718306,0.961445,-3.975305,9.300278,6.471458,9.632891,-3.431004,5.255345,-1.016415,-4.332430,6.467081,-2.682986,-5.822160,1.505934,0.364024,-3.040626,-7.588989,3.032847,-7.704140,6.491800,3.802930,4.152481,-9.365379,7.046896,-1.188400,-0.125842,8.680923,3.062475,7.299817,4.668977,-5.501489,-4.474247,5.050676,5.588084,6.386030,8.243014,3.574132,-6.560363,9.950169,-7.092118,-4.622297,4.196249,3.403772,9.672113,7.456014,7.335269,-0.238632,7.753223,1.380690,1.107041,2.188903,6.565158,1.606090,-1.319592,2.314307,-9.073575,-2.058886,0.047029,2.076806,-4.585567,2.005620,-0.333148,6.805102,1.918145,-3.670456,5.706492,5.601140,9.736668,0.044516,1.560601,-1.088478,-1.578955,-8.807901,2.127076,-7.374924,-4.590385,2.976864,-4.813139,-4.745669,-8.771569,-0.901591,1.235676,-7.725398,8.270634,-1.070724,2.400323,-4.038932,2.050375,1.315800,-1.373096,-6.064589,-3.924201,8.278131,3.855380,-9.103899,9.742892,8.699494,3.087953,9.979867,5.400681,7.950508,-0.190096,-2.703045,-5.384001,-6.838813,-7.891940,-0.908214,5.815304,0.330100,0.317952,-2.106629,-1.993966,4.608427,4.510276,-0.895553,4.855802,5.920352,-8.297519,2.617448,-3.957331,6.090966,3.216803,9.277512,-5.942056,5.787977,-2.455942,-5.898886,3.648296,-6.374551,-3.939486,-3.525528,7.644540,0.917047,3.023763,-6.192008,8.863287,-3.615244,1.750566,3.190089,-4.380461,-0.037039,-6.274238,-5.339183,-0.091991,-0.348474,0.244386,-7.182620,1.347001,-3.190741,6.901108,-2.995946,8.644172,5.038864,-8.722342,-3.178156,5.264180,5.110713,9.498631,1.310403,7.376433,-3.408586,-9.037304,2.285692,-9.033324,9.981055,-6.641643,-2.558825,-8.589045,1.242964,-9.773440,-9.277085,-2.998325,1.456908,2.278553,0.714367,9.434303,3.645833,4.563772,1.478033,6.956682,4.156851,-7.155618,2.269893,9.192056,8.484022,-6.063211,9.852549,0.702306,-2.812732,9.315902,5.922381,4.765004,8.151957,9.144392,-0.240408,6.681338,9.261023,-8.944244,-3.729129,4.562863,8.013314,2.019022,-0.801543,-0.394656,3.255356,-2.084194,-2.139462,-9.130610,-7.416912,-3.489971,-3.229898,-4.444894,9.709279,-4.286630,-0.476995,1.942660,3.517053,-7.402455,1.556130,-3.470305,3.559066,-2.109760,-4.559034,0.284012,-2.941001,8.774326,8.872748,-6.172537,-1.657194,-4.016859,-3.787335,9.811821,1.581019,8.478240,-7.436549,6.642216,6.934315,3.854881,-0.847688,-8.070691,-6.607523,2.850495,-1.745067,-5.416323,-7.628144,0.175622,-2.127509,-0.415752,5.699032,-7.993392,6.237110,3.595594,5.449970,-1.839421,2.782471,3.021655,9.237653,6.026754,-0.196628,-7.503411,-7.439543,-7.554885,-6.376668,-4.762767,-2.703082,8.901436,6.486531,-5.606559,7.681455,-3.921234,-2.196072,-9.706459,1.051414,1.717710,6.050139,-6.066628,3.363730,-0.300658,-2.290762,3.444395,-8.558996,-0.276305,8.607922,-3.250162,-0.973867,9.539495,-6.958185,-0.387516,1.220044,-3.921640,9.067642,8.249936,4.754206,4.158694,-4.623688,-2.630391,7.089457,-9.814827,-0.157425,-7.780374,-4.224414,7.381036,4.944249,-7.894574,6.566909,-6.236970,6.722174,0.708524,7.909175,-5.859650,-5.821387,-7.164786,-0.731876,-4.618087,-3.455527,1.362922,2.512951,5.765170,-6.861737,6.343188,-2.544692,-4.030658,5.437849,-3.782025,-0.039545,3.334716,-1.776790,8.807627,-5.933061,1.487774,-9.603413,1.094316,7.059220,-8.828406,-4.407629,5.719877,5.646864,1.114122,0.395134,-4.224661,-3.392130,-5.155964,7.054859,4.040755,-7.519149,-4.899716,4.566775,-9.996739,0.148428,-2.910081,-1.506120,-8.080355,-3.580178,0.893554,-4.207420,7.962317,4.451028,7.539138,3.637212,-8.149953,4.375912,-5.896694,6.528637,7.052527,-6.419543,-5.007032,7.277038,-3.662842,-0.058978,2.750987,6.595913,-8.284149,4.737158,-3.050392,-4.252704,-7.950348,3.963631,7.046573,5.769054,5.480681,-0.656697,-4.242469,4.535826,0.491125,-4.477022,-2.852826,-4.481889,-1.076954,-4.276760,-0.192477,-0.328317,-9.205312,-2.382103,-7.072549,-2.224877,3.085899,0.710675,-4.152772,-5.685957,7.847280,-4.150692,6.665543,-2.420872,-7.832371,-0.859652,3.991901,3.127654,-5.536519,5.783319,6.903634,4.202167,5.834883,2.628929,5.711185,3.907556,-1.910963,-5.267660,-8.593001,-7.298050,0.782996,-6.794835,7.039747,-8.329685,6.125302,-8.331446,9.221411,3.446391,-5.748601,-5.203229,-4.953262,-6.931792,3.556159,-7.488714,6.045040,1.950574,2.737036,-0.614920,6.425949,2.210797,-0.845937,-3.412782,1.487873,-7.156242,-4.189297,4.944973,2.445916,9.852062,-2.902254,-1.511614,-1.025389,-1.205233,4.656093,-9.087618,5.753910,4.845689,5.923277,1.937189,2.634164,6.932404,-5.818199,0.389663,-3.532038,-6.380968,-2.007501,9.738168,-9.595396,7.462887,-1.136722,8.291336,4.894175,9.058956,-4.675028,6.245726,9.870889,1.684867,4.071979,7.145399,1.056493,-4.292453,-1.214044,1.202157,1.864417,8.702380,-8.984102,6.121436,0.747816,3.690365,1.154922,-9.117166,5.106403,-2.664940,-5.671751,-6.880803,0.493505,4.029828,-6.557208,4.923811,4.572254,5.286435,9.165728,7.605887,-1.519473,-4.345361,8.409400,-9.484781,-1.664594,8.418709,-7.807418,-0.571126,-0.878432,7.689481,-2.970455,-7.140259,7.035229,-6.327515,-7.940912,-3.049184,-0.516386,-7.062114,2.869853,-5.499273,7.223074,-5.672762,0.902932,-0.573096,-9.798878,4.071607,-5.397001,4.058190,9.095607,-4.511930,0.874878,-6.243534,1.444669,-2.595605,0.709238,-4.547234,-2.900357,-3.768749,6.235428,-3.802914,0.168741,5.802411,4.184946,3.649391,-7.650574,0.781889,-9.479303,8.838007,-5.637632,-2.165776,-6.964858,4.894792,7.799536,-0.448237,-4.050478,7.458384,-3.020472,6.592746,4.629340,4.298594,-0.646566,7.795182,-9.483845,-4.572736,-7.926687,2.426188,9.547278,-6.856647,-0.709837,5.880444,5.662986,-5.742401,8.741152,5.709146,5.798386,-3.714821,5.158698,-8.102137,-5.134287,4.038477,-9.465151,6.422967,1.923520,-1.982465,1.366049,-5.981024,-1.511182,-0.451592,-9.952175,-9.829406,-4.612605,7.378301,0.503336,-9.603684,-1.112988,-9.703435,-3.715967,-2.055390,5.376730,3.236461,-8.897611,4.444941,6.720193,3.005087,-9.458329,5.777976,-2.284110,-5.441455,-2.899199,-7.999064,-3.866260,6.913458,-6.286868,-6.266901,6.845878,-0.213179,6.972392,-4.161057,-5.244700,-2.990530,-1.167358,3.938738,-2.293443,-9.145242,-7.892483,0.306527,2.536708,4.762309,-0.209590,-7.134934,-2.113303,-1.220349,-6.494535,-4.241402,-8.893274,8.722550,-3.221245,3.940426,2.003227,0.925993,-5.635681,-7.916821,-5.933759,-9.979718,-2.492482,-0.308598,2.845431,-5.462791,9.519439,-7.224656,-2.243321,-4.301355,3.798661,4.776849,7.842122,-7.607887,-5.884014,-1.668280,5.733279,4.957128,4.492379,-4.795504,-6.193185,-8.418291,4.012490,3.130274,8.049764,-4.559873,-7.378749,1.496324,-8.399594,5.484385,-2.608854,8.973544,-7.054071,1.473891,-6.110853,3.985248,6.058230,3.871402,-4.492944,-3.321189,-4.678537,-7.230790,-3.547959,8.698536,-5.167141,3.333770,-8.438928,-7.754967,-0.076063,-9.762005,3.515027,4.495151,5.217129,4.953897,-1.224699,7.991047,-1.133986,5.953167,0.628924,6.390631,1.632490,4.601793,-9.822486,7.509396,8.087517,1.348765,9.412597,2.242885,6.023958,-6.718494,-6.384858,6.192052,-7.978519,-4.770466,8.492945,5.566006,-3.326686,-0.264745,-6.794765,0.762704,3.634201,-1.195991,-0.199178,4.335747,-8.309388,3.451417,-3.929092,5.827313,3.801089,-7.577274,9.994767,5.430640,-9.356064,-9.328465,0.565503,1.770143,3.636359,6.047851,7.412833,1.248488,3.914469,7.224869,8.013474,-0.300634,-2.623426,1.437645,-1.044449,4.065938,-6.294793,1.391929,-6.137774,-5.202804,-3.531102,4.399826,5.549891,3.365087,0.163852,-3.078729,8.198102,5.278576,7.607194,7.351241,9.592341,5.619151,4.321342,-5.130128,3.783967,6.818150,-4.312970,7.159760,7.057975,-4.433452,8.654598,-8.785360,6.946344,-5.145535,-7.447112,-7.603794,0.315346,-9.197590,-1.940508,-6.857607,1.015501,9.841524,-3.692282,6.222635,0.374616,-9.105770,-2.167806,4.810390,-4.532895,5.418732,-6.694235,-4.312613,4.691944,-6.312034,6.224552,0.691124,-9.504201,9.836493,6.919892,-2.382904,-6.693152,-2.137661,8.838217,0.934624,1.993290,3.800703,-6.368255,7.183825,-7.993608,-6.000150,-5.008412,-2.510798,-5.198270,0.501382,3.915731,9.594087,-1.035661,-6.823575,8.004243,9.424341,-3.162028,-4.282469,1.107529,-4.023734,0.084118,1.296977,-1.809065,-3.759312,5.620045,3.540898,-4.617599,6.554775,-2.848248,-3.486106,3.043844,-0.912623,-8.861058,-3.641951,2.020670,9.117342,4.724342,-9.062037,4.984659,5.251062,8.562878,5.927850,2.898384,-6.322444,-0.934693,2.686815,7.380396,-5.614608,6.569938,0.657561,1.901299,3.597588,1.894199,9.072297,4.993039,-5.073503,3.869717,-4.087702,-5.850543,-8.466043,2.321272,-9.200941,1.787927,6.685778,1.148610,8.369294,1.697955,-4.180337,4.787333,4.426087,-2.881449,5.664653,7.181985,-2.099130,-4.201361,1.377144,-6.939814,-3.495994,-1.983955,-5.703425,-8.974658,-7.705607,8.075289,6.024625,-9.439457,4.497281,-9.801018,-1.255013,-0.990666,1.003197,3.607849,-2.413898,-7.720225,-4.060996,-3.412444,-0.332440,-7.209207,2.521045,0.473658,-1.908406,1.418659,-2.371811,-1.312614,-9.119285,7.947776,-0.336038,-2.205276,2.329702,2.334348,6.273649,-4.653496,8.925658,-6.773316,-6.921914,7.157662,-8.882666,-7.598540,-9.891392,3.008230,9.752275,-7.535559,-1.894758,0.843671,7.888743,2.332854,-5.546346,-0.274671,-9.725538,-6.456609,5.980681,-1.436631,5.104646,-3.383243,6.926801,-1.366927,1.040083,-0.575655,4.572584,5.024467,1.510749,6.704373,-3.346871,5.971955,-7.871737,-2.113580,6.209887,4.118756,8.482420,-3.739997,-8.759528,-9.734614,3.196304,3.646892,-8.600943,3.621632,9.713925,4.077280,-5.330317,-2.124265,9.120476,-8.682724,2.213905,9.015657,-6.677280,-8.568620,-5.560830,-4.474123,5.184294,-0.721575,-2.404238,7.706615,-0.051342,8.918586,9.887902,5.702577,-1.336527,4.292328,-7.363645,0.971360,-7.278974,9.775841,-7.029546,-5.510589,5.353634,5.364190,-2.341962,3.062786,9.336172,-5.674192,-4.980311,6.584465,4.607427,0.965399,2.723150,-3.138573,-9.864147,-7.588284,3.558822,-7.432544,0.461515,-0.247417,4.915896,-9.836068,5.885543,1.684919,1.017269,-6.609961,-3.272668,-3.354596,-2.684416,9.433880,-4.182912,1.920941,3.469857,-5.468227,2.280006,-6.227783,-5.151150,-7.360338,5.276495,5.011288,-4.598832,-2.150955,0.704266,9.037771,8.872269,-6.863990,-9.125937,-9.162788,-4.675132,0.316982,8.175730,-4.811342,-9.175810,2.528096,-4.472569,-2.361343,4.319473,9.361637,1.373521,-0.712694,-3.982628,-4.910306,6.349117,-3.617843,2.953929,6.968939,7.325582,-5.458957,-4.636955,-9.881595,4.427973,-0.512044,6.970152,5.128456,-5.526250,3.429024,9.628148,1.938825,-4.052113,-7.099988,7.544059,1.046529,4.282355,4.911119,3.957312,-1.174374,-2.197764,4.721290,8.758861,3.907575,6.650811,-1.192556,-7.434900,4.797196,1.134014,4.992307,4.938674,7.111863,-8.518059,4.956460,-0.242736,-0.197700,-7.505770,-7.978486,6.632248,5.302460,6.888191,8.367286,5.869247,-1.941896,-3.974138,-1.721051,-2.140477,-7.566348,-7.758234,4.304102,4.828054,9.545043,5.106570,6.425537,1.940151,4.259724,-0.988297,0.693635,1.427773,-7.903077,7.792856,-5.854814,9.171404,-4.127087,-6.741469,-6.390728,-6.464988,6.227073,-1.817754,-2.197174,6.293993,-9.907875,-7.276929,6.775662,6.550095,9.903086,-5.011503,2.052972,-0.759519,8.986014,5.864678,-1.024300,-9.835542,7.331005,8.833816,-3.839465,-4.666343,-1.824692,-4.070557,-1.120001,-3.468347,-8.666037,1.795870,-4.748131,-1.482781,-5.154202,4.911491,0.268006,-6.430970,-4.648249,-0.548447,-2.358291,4.737844,9.889716,3.214843,-5.182803,8.247997,-3.331611,-1.074215,-3.474607,8.045160,-6.420234,1.791644,-0.185453,-9.954140,8.229794,2.604004,3.056798,1.481039,4.509753,5.499525,-6.958501,-2.838760,2.998312,5.394340,8.128867,8.930241,0.641253,6.779758,-4.728724,2.262522,-3.109280,-0.645901,7.726812,-1.823764,-0.500186,-6.624034,-1.782185,0.391789,0.644398,3.521967,9.075144,-4.258725,-5.303283,-4.814597,-9.926226,-2.315179,7.231696,-8.487734,-2.221038,0.106655,-8.278415,9.969688,-4.747688,9.818574,3.165472,5.526290,0.989086,-7.671537,1.963260,-7.130972,-0.502587,1.622270,2.816537,-7.000833,-3.799005,-1.671458,-6.630663,-7.347747,9.170184,-7.480638,-9.985896,8.617613,-9.489908,5.175801,5.801829,6.174411,2.175136,7.312597,-0.149389,-6.450662,0.893908,-2.103137,9.133168,-8.037730,-5.231241,0.939331,-2.176826,-6.368667,-0.675336,7.590891,7.011213,7.383465,4.471109,-0.387466,4.185054,-4.248357,9.860776,-8.475439,0.460364,5.754000,4.361720,8.377093,-3.689318,-3.216187,8.442163,-0.453750,-9.172400,7.054824,-9.104457,-9.687344,1.479976,-3.435084,1.229047,3.919609,8.082945,-5.088678,8.342507,2.397691,2.913874,9.012158,6.193027,4.731694,3.461206,6.322707,-0.398636,3.659947,-3.778931,6.788075,-1.814126,5.207867,3.970735,6.826404,8.174078,-1.793714,-2.885709,0.485392,7.061391,-3.912054,-3.485816,-6.134308,6.083449,-2.139468,1.954220,6.876811,-8.651474,-6.878760,-6.336948,-6.547558,-4.809975,-1.089752,-4.850748,-4.524930,-8.705928,4.595501,-9.659955,-4.468551,7.437355,0.567038,-6.482307,1.856300,4.247308,-1.402513,8.518752,7.552709,-6.732583,-8.784439,-0.412860,-2.362941,6.631138,3.269589,-7.327923,2.321732,-0.431692,-3.802078,7.249326,5.389214,6.432416,-9.173718,-2.905361,-5.386345,8.230091,-7.931429,0.110837,7.629320,-7.165845,-1.385292,-7.100663,-6.033430,7.458645,0.806029,-1.870919,3.276628,-7.660505,-2.330707,-2.730170,5.441571,-0.685745,3.970666,5.469881,-5.883326,7.542463,-3.274461,3.644913,-4.492318,5.835279,9.209658,-4.611390,-9.959986,0.641831,4.701039,2.770458,0.508893,-4.291823,-7.217352,0.497481,8.360602,9.124721,-0.584243,6.100376,1.918489,-4.584830,-5.369642,-5.002213,-8.842615,-7.431829,7.390294,-4.069457,7.344139,0.992199,-9.671944,-6.015571,1.041388,6.250627,-5.317898,-2.490297,-1.091495,5.043920,9.378914,1.914817,8.849709,5.009763,9.520553,2.470238,1.229567,-1.209145,-8.967918,6.806885,8.450028,6.478075,6.327459,8.042341,8.563207,9.474571,-6.569958,-5.636435,-6.295803,-7.512691,5.294959,-3.092597,-5.315130,6.956112,6.725666,-1.292800,5.095231,7.329191,7.576706,-9.810068,6.277135,1.010635,-5.202219,1.054654,-3.579202,1.157368,8.486804,-1.098435,-1.696011,-0.588736,-0.212301,-6.333074,8.013926,9.771290,1.924698,0.736570,7.775837,-5.304859,-0.139511,-3.516457,-2.504308,-5.254614,6.017286,7.946748,-6.015181,0.820296,9.743955,3.584038,1.839314,7.951149,-9.081348,6.454980,-7.444337,-9.651003,3.234656,2.303100,-9.468866,-4.213936,-5.543331,8.982450,0.373899,4.664709,1.671116,4.147539,2.556761,2.787788,7.458638,6.336474,-3.577101,-0.124752,-3.925060,2.119150,-5.084922,-8.341516,-9.033510,4.953295,1.272289,-4.735046,7.395821,8.559911,-2.948099,6.333553,-6.113956,8.340779,-5.929285,-1.603207,9.454412,4.004437,2.456572,-4.952567,0.230071,-2.362273,3.751434,9.875487,-1.527965,1.769163,2.898234,5.755296,-0.808360,6.398082,-2.609340,1.541212,2.490917,9.338502,0.694521,-9.237974,-0.539329,7.398373,1.655104,-7.098388,7.245256,9.955244,-4.352932,-6.871411,6.214245,4.616789,-4.758096,-8.648392,3.332717,-7.976319,6.626622,-1.932132,3.807043,5.334138,-3.443944,5.287190,-1.734727,0.306009,2.062372,9.056447,3.731100,-7.210439,1.885118,2.266148,5.819560,6.247902,4.013460,-0.547085,8.463340,3.412402,8.202569,-6.753322,0.272411,1.577629,2.849608,-9.981701,2.301061,-8.826710,9.316886,-3.253124,-3.631675,5.113674,9.876409,-1.662695,-5.616524,-9.933714,-8.977329,1.992728,-9.182327,-0.609613,3.083700,-3.439346,-7.949058,8.553100,7.652809,-3.898814,-3.757727,5.029866,6.065639,-9.276214,5.132747,7.571706,7.128963,-3.048498,8.695637,-9.827117,0.354008,-5.359536,9.673947,3.548150,3.316596,-5.273584,8.857420,3.856223,-5.058069,-7.567061,-1.581352,8.284094,-8.828157,-6.659069,7.010654,-6.248499,9.639136,-9.439002,5.428169,6.630434,5.281460,-9.197771,2.070665,7.009693,9.946638,-5.605419,3.689671,-9.923703,8.073332,-2.480334,2.345583,4.764424,1.113250,9.302083,4.041932,4.326352,4.475514,6.432051,4.773870,-9.012950,5.874466,-2.605337,-9.726381,-4.052916,4.060570,-1.254286,-9.168619,-6.963961,4.309149,-5.633249,-8.537558,7.050502,0.422066,6.555320,8.079894,8.070551,-4.536621,-1.218773,-8.080662,-9.799534,0.549192,-6.240715,-1.540957,1.355480,9.063607,-9.623950,0.713470,7.434428,-9.084229,1.297036,-9.548568,-9.213198,-6.203173,0.775311,-8.352140,3.277383,9.151034,1.642141,-4.559903,5.747925,-8.088438,5.395138,-2.754122,-1.384566,1.079469,-7.846493,-5.815902,-3.564835,7.053010,-8.718350,2.865888,2.601762,6.964092,-8.595183,0.998976,3.123073,0.694157,2.064671,0.068760,4.022622,9.398754,-4.326903,-0.610036,9.381253,4.137126,5.440469,1.443312,7.652118,9.499346,-3.358078,6.500614,-2.341506,-6.730514,-3.269614,9.916465,6.358507,-6.933477,1.973794,-9.992559,-4.506234,-0.365656,8.417332,2.138795,-9.114666,-9.646223,9.593451,7.803578,9.432089,-6.972858,3.010969,6.167536,-7.336323,3.102943,-5.180212,-6.417974,7.575833,2.353704,-4.644447,1.687943,1.384710,0.546704,4.491173,2.490446,1.026030,3.910107,3.796243,0.347880,-2.609645,5.128609,-9.337504,5.426471,-4.734103,-8.712413,8.034439,-4.442172,-8.358876,-9.508884,-4.966897,-6.391536,9.305622,-4.040472,-0.403395,-0.378520,-5.467509,9.677666,-6.138914,-2.705813,1.942103,0.103692,-6.170880,-7.484387,-6.589103,0.667848,-2.754793,-2.653469,5.670335,-8.314420,-8.492748,-1.265415,8.870751,5.844812,-7.297494,-5.743297,0.310493,5.390727,0.283406,-3.694704,-7.527201,-9.633133,9.743989,-2.241504,-7.970799,-5.467866,0.146966,0.722137,-7.414485,-1.903473,1.568026,9.914858,6.295659,-9.676151,-3.548484,-2.736494,-0.818341,8.083770,2.815541,-5.247992,-6.415258,-4.334355,8.885886,-9.632561,-2.954929,2.358156,-2.955175,-0.398463,9.507837,-2.736731,8.083967,-3.886442,-4.059485,2.559252,4.199783,8.599258,-9.214504,8.549686,9.359431,-2.288743,7.046211,7.468791,-9.312148,4.946593,5.014875,5.255043,-2.007831,-1.347564,5.596186,-7.828376,-0.460046,-5.112228,5.077057,-2.878271,-6.103468,-9.179741,-5.404869,4.655721,-8.422615,-1.955634,-3.133343,-2.584436,0.906055,3.023820,2.468808,9.464005,1.943820,-4.396400,-9.333560,-6.744513,5.971383,-4.295626,-7.109163,-5.596642,-3.576364,-6.104024,-9.219553,1.303776,-5.014185,-4.394836,-3.804094,3.547253,-2.290609,-1.023857,-0.923444,5.395867,3.024391,-9.696605,5.705013,-2.184413,3.021663,-8.122473,-1.606881,-7.189295,3.702769,-6.240947,-1.059312,6.743495,0.322137,4.967116,-6.505403,-2.418221,-1.354787,-6.655455,7.189269,9.505563,9.976579,2.729129,7.684135,-8.396013,-4.830915,-7.117072,-5.405267,5.226441,4.003723,-7.339232,3.579740,-6.759957,0.574426,8.589953,9.289232,6.526064,7.741420,-2.355681,-1.719391,1.954154,9.622207,-3.467189,3.507191,-8.771544,-6.126766,7.213403,3.343294,-2.956776,-4.696469,5.869798,-7.211346,-9.958116,4.820579,1.573664,-7.293203,2.394185,-1.265490,3.091067,7.114854,2.372126,-9.749996,-3.839684,-7.535794,-4.320474,-4.817346,-8.246703,4.102328,-1.581945,-9.558506,-9.544457,-1.042238,-3.968665,3.474469,2.565221,9.587125,3.534445,6.453885,7.170138,-8.143742,-6.679956,-5.755535,3.886935,8.677355,-4.221242,2.862105,-8.066115,-4.142464,4.561856,7.682232,1.527170,2.479701,-9.893547,-0.393416,-1.959253,-1.313885,4.662730,3.989302,-8.880519,0.261517,-3.649824,4.783093,-1.164941,-6.148493,-4.796734,-2.672459,-6.580690,-5.400475,-8.043696,4.866288,3.527701,8.143192,-7.484556,3.809753,-8.848099,7.215227,-4.356585,9.009793,1.809949,-3.743962,9.884808,2.682581,-7.952820,9.775738,-1.611171,3.297974,-1.201384,-0.343006,4.572239,0.714014,-9.007198,7.503213,3.855812,-3.744762,-8.191752,-1.189048,3.211951,8.533440,5.772882,7.699814,5.745258,3.727893,7.020041,-0.707041,-1.345108,-8.885433,2.104051,2.653079,7.099287,0.742070,-8.567084,1.874838,2.053027,1.606753,7.359953,-3.152645,8.310737,-9.490134,8.103416,3.345770,-1.205893,6.713748,7.186631,2.921848,-7.428371,-4.317273,-0.439541,-6.594716,3.082393,8.524327,-0.584812,6.434015,2.261737,1.649633,0.521644,-6.762765,-1.594315,4.163556,-2.214464,-8.499940,7.104187,1.873267,6.058118,4.485314,2.951541,6.805974,-1.390521,5.249288,5.780189,-1.934912,-0.641163,-6.414829,-9.670936,-5.400823,-6.461348,7.102574,-8.844265,-6.392014,9.661583,-5.980148,-0.692513,-4.388952,-3.266090,-1.019841,-7.895001,-3.025616,-6.802084,-7.641667,-1.055250,1.597803,4.241602,-6.226822,-8.031680,7.862801,-9.184902,-3.673675,-2.261074,6.877891,3.987446,-9.254364,0.795248,-1.879821,6.393188,-6.041137,5.812982,2.342875,6.507591,-5.717425,-6.608189,8.282480,4.125218,9.726261,-5.504509,9.502322,-3.349798,-3.605245,-6.007044,9.400312,8.443952,-5.306802,-3.545107,1.636094,0.995820,0.844895,-5.883197,5.959339,-3.646731,2.709597,7.574216,-4.370455,-8.197080,1.069901,6.108470,-8.938207,8.293556,-7.444954,-8.788847,4.436276,8.030505,0.567929,2.314668,-9.801738,9.623745,-8.426870,-6.304202,7.529376,8.569028,8.016022,8.601218,8.607133,-0.472666,-0.583947,-5.849677,1.446413,-2.386754,1.112298,6.960916,-6.344889,3.199678,5.411561,6.293452,-7.905546,-5.614354,-8.646898,7.706666,-9.594522,9.281951,5.250668,-7.893824,5.271705,8.091622,-5.374564,-2.804566,-7.047769,3.778281,3.447957,-7.679545,-3.066971,-1.951139,-6.220476,-8.311175,3.700969,-6.493752,5.236033,1.436411,1.999704,6.269436,6.938139,-1.302536,5.526038,-2.673972,6.895962,-2.371484,2.717336,-8.679078,2.327856,-1.653943,-4.166202,7.596390,4.073188,-5.337737,6.412272,-5.766051,-6.985868,-5.288771,-5.706362,-3.325756,3.307808,0.303116,8.701421,8.622613,1.981465,-1.087895,-4.018703,8.272364,-7.929015,-2.443628,-1.121692,2.062710,-7.047631,-8.008818,-6.800509,-6.449659,-3.063523,-5.837924,9.635669,-1.804696,9.998460,-7.967689,-7.525011,1.606780,7.182383,-0.486607,-6.831415,-4.842291,-2.157771,3.252278,-2.389386,-2.463996,-7.635559,-6.084541,-7.448557,-5.531700,0.484282,0.055626,-2.056218,0.006084,3.670685,7.320286,1.500578,-5.095038,2.502344,-9.983077,2.873738,-8.763427,7.878252,9.660306,0.466642,0.826384,-0.788918,-8.932809,6.165680,-3.419622,1.268691,-9.776609,-9.066645,-2.540823,-5.072859,7.057412,-3.508595,4.982378,-7.410445,7.058178,-4.266018,7.860839,-5.925880,-0.507107,0.491794,-3.226738,-6.164417,4.890007,7.530080,-1.926998,-6.782541,0.639093,6.781791,-4.985931,9.099325,3.857881,-4.870029,-7.342205,-9.742044,-7.075262,2.570793,8.726763,5.344313,-2.978415,-3.557428,-5.310202,-5.177699,3.941871,5.263494,-1.177574,-0.765069,-1.796604,-2.504683,7.775779,6.733107,-9.899298,-7.279308,0.805010,-0.970880,-4.439935,-8.936379,6.624844,-4.904839,8.974959,-3.253406,-8.917531,8.176388,4.525897,2.476349,9.419662,-1.844322,2.482307,3.538400,-5.088935,8.652005,-8.882304,6.407629,-2.164494,7.938096,5.315797,4.713064,-2.658042,6.674052,-8.448892,-9.028375,6.513678,1.402512,6.115210,0.429604,-6.951871,-8.559187,5.051562,-6.136142,8.916227,4.904487,2.462829,-1.699027,4.373959,3.580791,-8.756169,3.068957,-6.380395,-6.211256,8.728688,8.169402,-9.538779,2.024441,-4.215675,-7.532117,8.928691,-0.437797,-9.765984,-7.163251,-3.256117,-8.422895,3.678066,4.560367,-9.355065,1.311900,1.222345,-8.800141,-0.351200,2.676547,5.825746,-0.271964,3.328324,-5.494181,9.718986,-0.166370,-4.235405,-1.145202,-8.809936,-2.241062,6.822076,9.614496,-6.375400,5.298909,9.023851,5.065659,-3.011531,0.712762,5.551287,6.761405,-9.362764,-6.648334,-7.797676,-5.819252,-3.586143,-0.683940,-8.503642,9.516891,8.519813,9.027276,9.352954,4.839748,-9.441722,-6.515054,-8.949665,-4.453730,9.166267,-5.813724,5.410082,-7.076771,7.312101,1.908792,-8.496332,-1.680232,0.165235,-9.867051,9.596469,-4.171086,-9.845883,7.725533,1.232046,7.541891,-3.598153,-6.805317,-5.934730,-9.788623,3.269936,5.109477,-5.666477,4.150950,9.703010,-7.158543,-6.785774,-3.595937,4.530382,5.590267,1.837519,7.013881,-0.741928,4.276010,0.876429,-2.492236,-3.119735,-3.743794,-9.361730,-9.808280,-3.880790,-9.564091,-0.415006,6.678317,-8.017963,-0.213519,-2.221088,8.887612,4.549095,5.058577,-6.797297,-1.062166,-9.316697,7.068267,-4.785409,-1.948983,0.369769,5.737024,-5.805741,4.900491,-8.464559,-2.401599,-3.543006,6.314870,0.315982,-2.818149,1.988663,-6.141169,2.395168,-6.267648,8.408503,-5.515381,9.898162,-0.065657,3.770615,-7.742585,2.856277,-1.034413,-1.805162,-6.068813,-6.500250,-5.706884,9.702925,7.720435,-1.262261,-5.653834,1.360992,-2.012556,3.038540,-2.209757,4.461127,-9.626937,9.825701,-8.686103,-9.209035,4.864246,1.686246,-2.954713,-5.254599,3.204229,3.090735,9.372724,2.073418,2.862180,-8.428611,3.685511,-0.620520,5.146564,-2.721648,-8.112180,-3.397385,0.125641,1.603548,-6.706249,-7.351204,-5.864013,8.762440,-9.662337,-6.157724,9.004221,1.016564,-2.549140,-0.795801,8.152307,0.462417,-5.178996,-8.089548,3.349484,5.723288,4.308808,3.862677,-9.568388,3.541311,6.774640,-8.393195,3.193414,9.257221,-0.498226,9.105678,-3.442239,7.528641,-7.954530,0.889161,9.268162,6.055654,-4.367883,-7.908261,6.192911,9.352399,3.026037,-0.200248,9.031195,-0.150293,9.720457,5.487422,-1.987454,-6.034671,-8.318647,-4.014690,6.807669,3.100760,4.730428,-3.392840,0.674050,2.821303,2.865574,5.476975,-7.337869,-2.421827,9.736360,3.062349,-8.874883,-1.953842,9.610569,-6.881917,-6.607064,-5.771188,-3.142280,3.315775,-9.688033,-7.463006,-9.340823,-9.809289,-9.129856,-5.911227,5.749266,5.095532,-0.610045,-2.292217,6.870862,-4.909388,-9.011907,8.272082,6.632891,8.692904,8.333502,9.406150,3.986432,-0.435911,0.353350,-8.778367,5.604880,-2.582069,0.485382,7.371042,-9.820330,2.989692,0.873305,2.501800,4.133931,-0.800420,-0.956386,-2.657697,-3.171871,9.862711,4.163880,-9.734417,-1.383782,-7.065049,1.124336,-3.744766,1.729603,0.752230,-2.503373,4.287014,1.288982,-0.285230,-0.694213,7.248249,-5.925746,-7.877652,-7.916141,-4.566358,7.456110,7.784162,-6.131178,-3.832600,7.451326,-8.964747,-7.085355,2.118102,-5.396336,-1.297679,-0.459571,9.450399,-9.985581,-9.638783,-9.833651,7.489724,-8.928025,-9.072203,-4.865422,-9.180601,-4.430334,4.734153,3.704370,-9.150044,5.918765,-9.371895,2.712694,-3.824157,7.403376,-6.841307,5.217042,6.894532,-3.076143,-3.469598,1.881909,-5.726113,-1.226441,-1.366395,-8.266805,5.260629,0.615504,8.723620,3.513131,1.039051,5.664747,-8.125085,4.545747,-0.841965,0.449711,8.611715,3.472819,2.581505,2.848816,2.371885,-8.552239,5.519016,-5.100918,-0.722022,-1.183297,-3.923785,-4.228476,-6.166582,8.059857,0.756260,-9.599422,7.541231,0.172706,3.512238,-2.391236,-6.347861,5.066206,3.117163,5.598844,1.367278,3.471635,1.052958,-4.641723,4.248994,-5.290308,-9.380467,3.786033,-3.458019,-4.928797,-3.173648,1.537537,-2.287278,-7.904757,-6.840622,3.515185,-1.049234,-7.167106,-8.789879,3.101024,-7.687388,4.567240,-0.697903,-2.055992,2.319349,-4.805220,9.560607,-1.104802,-3.763321,4.056816,-0.379056,-6.550043,4.450457,-9.656625,7.029509,-2.671289,8.823462,5.063294,-3.108098,7.182704,-3.208946,5.036543,6.452493,0.825498,0.715652,-7.040978,-5.879393,-6.764462,1.794293,4.091882,-6.182541,-2.845215,9.445622,-4.295146,8.157448,8.234552,6.414933,-1.332514,2.585302,8.443606,-8.384943,-2.920141,-5.462955,8.081296,-6.676326,7.517011,-7.710900,-2.711673,9.793312,9.260489,-4.101545,-3.878773,-9.717728,-0.446084,4.447498,-8.491129,-5.308923,-9.858822,5.621227,-3.176520,-7.587843,-9.947419,-5.655759,2.112791,0.144381,-4.990397,5.297984,-4.783297,6.031383,5.593683,-4.087131,8.631682,0.552939,5.191570,8.172023,-9.652966,2.286475,-1.729208,4.348043,8.450010,-9.245823,6.830396,9.258730,9.295624,-6.873979,9.693881,-3.926202,0.772379,-1.127507,-7.808309,3.739939,6.656966,-4.412752,-0.323081,7.453908,-2.902956,2.289175,-7.422657,6.537056,-7.651307,-4.816012,-5.710834,-2.706252,-9.800926,5.626758,-8.185567,3.869542,3.741722,5.218072,-4.105149,-2.162431,-1.957262,-2.776891,-7.684420,6.749828,3.258617,-4.063171,-1.461048,-4.401975,7.312392,-1.386084,-4.544888,8.298106,5.840672,7.577452,-4.769867,-9.578836,3.922460,2.805790,7.751342,-5.288267,-9.373498,-0.763752,2.149133,-0.940623,-0.198275,-7.698930,-1.569513,8.535794,-0.327776,1.948821,-6.774856,-6.482541,-4.173442,1.829401,-6.008062,9.401738,-8.272503,6.844366,-7.226669,-5.903591,-1.482161,9.704567,-8.566309,-6.304123,1.482097,1.712872,-3.347973,6.304783,6.592417,-7.005535,8.510241,4.580541,5.173771,3.993498,-8.208408,4.204940,2.962411,8.097619,5.044387,-8.538929,-9.453143,-4.723826,0.025160,7.995822,-7.407686,-5.097538,4.146913,8.050756,2.571541,-4.410627,-1.259773,-4.828901,-6.143435,5.218934,-7.889128,-9.263477,-5.203815,5.825964,1.397907,-3.715574,-6.539391,7.630206,-8.358170,-2.092740,8.166952,8.144143,-2.450233,5.852556,-6.663703,-3.732264,7.187316,1.315884,0.070999,8.940288,1.795745,-4.714364,7.450714,-7.025975,-7.350688,2.799193,7.405302,7.919419,-6.343204,1.179945,-0.068900,0.364665,-3.999872,2.950997,6.307977,-8.287696,-8.365253,-1.710516,-8.928687,-6.203829,-3.437148,3.375886,-2.485240,5.253205,4.198618,1.976686,0.449959,5.376243,2.875131,9.289264,-0.818363,-2.942674,5.953100,-1.439246,5.896668,-7.497827,-7.381616,7.153233,6.017312,7.585667,1.100697,-7.035757,-7.346658,4.655023,-4.313262,-0.177006,-1.166761,2.985594,-4.264296,-8.034081,-2.750477,0.236175,-9.807485,-2.472318,7.877263,-9.439780,-6.420854,4.445302,2.101826,5.444646,-5.100649,-6.820972,-1.198093,-7.077636,2.678697,-0.590036,9.420223,-1.071886,-9.044634,2.172367,-5.089015,1.394751,-3.185694,9.789040,5.200883,6.132608,2.175541,-2.073270,-4.305081,-3.082413,4.361470,7.711440,-0.230874,-7.531552,-1.555799,-5.154755,-6.065771,-7.162098,7.376631,-4.338688,-5.628191,-0.462362,4.781360,8.957229,6.000184,1.609978,-5.425552,0.288564,-1.729168,0.107905,-1.277659,3.800021,1.076045,7.831994,-2.256603,8.530181,-4.341824,-3.233358,0.580106,7.602777,7.730142,7.794775,5.261877,-9.516585,0.493771,8.747449,4.279792,-5.689662,-0.905249,2.966578,5.676472,4.308897,-7.432977,4.960000,7.770074,-4.730597,7.013375,-0.965659,6.055816,-7.473589,-5.039311,-4.353431,-7.486219,9.113994,-5.792608,3.539123,0.176680,4.935535,-1.207471,3.714769,4.665427,-3.568385,-8.841368,-2.783582,6.347284,-2.639389,-4.308977,-7.008386,0.988656,9.383037,-8.434162,2.025773,5.682880,-5.789219,3.062119,5.998891,6.981315,6.929195,-9.546173,9.015698,-7.835497,0.027239,-0.975794,2.977704,4.031959,-5.728946,-5.781693,-9.544183,-9.731888,7.897545,-8.790297,4.586791,5.163570,2.974014,-3.886609,7.522878,-9.616093,1.388886,-6.533925,-2.093769,9.104701,-1.209151,-1.251793,4.812433,4.440775,-7.280670,2.553366,2.976493,-9.936530,-6.925310,-6.347829,4.056694,-7.926690,1.359498,-2.386965,7.538629,-3.930057,5.896872,-5.005006,-8.068690,7.743967,1.924010,-9.787017,3.599710,-3.822752,2.447983,-7.906220,8.068850,3.324453,6.352925,8.011683,2.314950,-6.964050,-6.511823,4.238791,-1.241928,-0.029073,7.708007,0.644276,6.204089,-5.539986,-9.322185,-0.173447,5.993692,-0.244490,5.968327,9.042068,-4.266624,2.700920,-9.286025,0.360154,6.583190,8.049273,-3.871500,-1.200851,-7.628949,-2.618153,8.667757,-4.497352,-4.047646,2.494455,-1.953025,-8.663767,0.771384,-9.624422,-1.279963,-2.102463,0.483609,-5.616239,-9.573213,7.228915,7.219140,9.476542,-2.901912,1.517432,5.172857,-1.298830,-4.852866,-3.325050,-1.192014,6.670271,-5.626471,9.394272,4.922575,9.255907,-6.346884,-9.067052,-1.152606,-6.849078,-0.007330,3.755951,-7.134866,8.937910,-2.569735,-4.557380,-8.070808,2.697126,-2.503410,-7.236198,-4.261245,2.248316,7.272670,-4.201504,-4.412380,-7.009752,-5.542066,-0.797004,-2.450891,1.242788,5.954779,9.320535,-1.815942,-6.114539,4.655638,-1.964501,-7.430066,-7.408150,-6.743330,3.667665,8.115973,1.389599,8.378829,2.124071,6.991209,-5.905529,-8.775915,2.056623,-8.398270,8.911629,-9.009321,7.955276,-5.123345,-9.919737,-2.923363,2.760033,-3.886538,2.057371,-8.440822,7.036334,-6.133822,-2.861576,9.247645,0.805163,7.617894,-1.086053,-6.840535,-0.977437,1.135470,6.025125,-4.248749,-0.296797,0.718236,-0.556872,-7.174776,-1.307439,6.349777,3.788359,-0.412539,-8.286274,-5.061927,3.444589,-4.198831,9.559497,7.399657,3.813773,3.309984,-6.768843,8.560439,-1.738142,-5.105338,-6.212983,3.276634,-5.785747,-0.232787,6.195683,1.522186,-1.282398,-3.074252,-8.822552,-2.949303,4.217505,5.935286,5.406515,-7.101323,-4.556364,-4.148929,-1.792035,-0.066993,0.839973,8.265809,7.378259,8.333020,-5.092372,8.927554,0.450265,-5.893927,8.102467,-8.243172,-6.289873,-2.234454,8.463158,-1.055670,-5.534850,4.185513,0.947436,-8.307810,1.054153,-7.518516,7.955680,-7.801826,-8.191954,4.259311,-0.860161,-9.572007,-3.991014,9.772433,5.685738,3.538663,8.234229,0.993404,4.713437,9.706156,0.040195,-2.726164,-4.530853,-2.675370,0.746208,-2.976341,4.468810,8.113897,-1.877209,-5.247437,-5.374326,6.147411,-8.782031,-2.133308,9.722213,-8.065485,-9.264580,8.177929,-3.491618,0.274922,-8.037875,0.137443,-7.439804,0.777057,-5.158803,-7.233812,-9.550310,-1.089213,-2.856684,-2.290340,-6.238413,-9.898737,-1.332277,8.857267,1.293118,-4.417675,2.960140,-7.038725,-7.976120,-4.996995,4.421188,3.383205,-0.616651,-3.426879,5.584461,-3.086270,2.280625,-9.244959,3.971773,-2.620179,-8.424999,-7.322447,6.012982,5.103787,-7.453976,-9.018271,-2.098418,8.445805,8.180385,5.055786,8.193200,-0.027266,-0.069394,-4.172906,2.885289,4.226182,7.331427,2.674729,-3.936685,9.982725,-7.984255,-3.235551,5.125838,4.894551,9.790338,5.086550,5.703729,1.791137,-7.489565,4.862695,1.404250,5.635860,-9.297419,8.513973,7.867021,4.348021,-6.147967,-0.754057,-3.038702,-1.697859,-3.521553,-0.908983,3.881231,-7.289451,0.916289,3.784907,-7.021735,9.812249,1.789884,1.991321,7.458133,-3.478534,-6.289060,-6.715687,0.702933,-6.886575,-3.689018,9.387115,-5.199411,-4.871252,2.740425,-3.396610,-1.271172,-5.637653,-2.366588,0.814375,-4.029940,3.154705,-7.391443,5.413133,-2.039978,-9.084788,-9.743445,9.511055,4.273871,-2.252700,9.913928,-1.901769,7.222242,-5.888103,-9.658040,1.196690,0.363048,9.932801,-6.118523,5.249443,-0.487401,-8.300712,0.373276,9.380597,4.757532,0.100761,5.575921,-5.097186,-3.493577,-7.854936,-7.398931,-7.962172,7.417878,-6.363266,-3.336939,-7.846597,4.315022,-4.188022,-9.228368,4.659964,7.273404,9.107535,-0.049311,3.512312,-9.263035,9.198587,-8.500355,-1.106619,5.398471,3.383413,4.275898,-3.736183,-3.456477,6.790873,-2.436077,-9.148328,-3.316905,-3.489024,-8.126742,1.061163,-3.725320,4.528071,-6.735190,-0.565853,-0.299039,-8.188893,6.873620,-6.392774,1.931918,2.782551,-1.481647,2.262267,6.305047,1.348333,-8.516585,-4.869133,4.703944,5.210465,2.883550,5.687208,6.670615,1.676761,-5.447647,0.777031,-2.733180,-1.261672,-5.150444,0.448938,5.974849,3.863912,3.397332,-4.020022,-4.160884,8.579761,2.605726,0.527534,-5.475915,-3.436368,9.015824,-2.267816,-4.734109,-9.355093,-5.715087,-4.984319,9.426381,4.870063,3.193717,1.678630,2.250710,0.907778,-8.912744,-0.044806,-3.937519,0.900934,-8.631325,2.192017,-0.975820,3.750545,8.062985,7.535121,-8.628304,4.141069,-8.261825,5.959493,1.178855,0.199937,1.572297,-7.023651,-2.939971,2.276356,4.691586,2.640053,6.792729,4.443791,-5.195128,6.409434,9.202253,-2.456925,6.618080,-1.768877,-0.410794,-0.752727,0.073254,4.924811,1.764710,-1.714424,0.925557,-4.430614,-4.836239,6.046648,-2.404981,2.375917,-9.255423,-7.059908,8.705917,-8.003962,-6.939220,-8.930922,-6.989707,5.916566,-4.439282,-1.302644,3.302798,-3.842278,-1.104065,-7.295817,-4.166560,1.719244,8.947609,9.495754,-9.599660,-1.360657,-0.536140,-8.778363,4.104050,-1.092367,6.673764,6.464315,-2.095359,-5.851274,-2.817656,8.200049,6.980803,8.185798,-8.285345,8.752572,-6.431995,0.761911,-5.660037,3.910838,0.296257,-2.846586,1.261953,6.301178,0.883905,-3.187671,-8.812130,7.559682,-7.698628,-6.638556,5.844246,5.952737,-2.167738,-6.330523,-8.309808,-6.318132,-3.479702,-9.563800,-2.345393,3.870410,-9.160381,8.657550,4.859668,-0.983079,5.600305,4.756400,-3.574531,1.021010,1.228091,-3.777055,2.361361,-8.954980,1.354409,5.328642,-5.691436,4.147267,4.490124,-8.695797,2.419710,-1.517802,2.139801,1.749872,9.951830,-1.847459,4.197306,-4.720382,0.825552,-3.884380,-4.333410,8.509812,-1.148309,4.241549,5.167957,-9.147146,-1.523756,-1.759010,-8.252345,2.268633,-6.675273,7.613797,-9.913998,-0.158952,-5.177905,-4.407691,7.481739,2.607483,8.989558,6.493175,-6.031579,5.687904,-3.547637,4.690375,-0.993450,-9.220888,-2.638365,-3.713046,-7.780770,7.963744,6.488105,9.286007,6.342026,-7.576613,7.460621,2.905417,7.293752,-9.542089,-5.627564,9.092885,-1.460824,3.380915,0.627403,-9.019018,0.296724,-4.240177,7.187497,3.064046,-8.049835,3.877162,1.418184,-6.452510,-7.727688,-5.687617,-5.232913,0.757464,-9.428576,4.507746,-2.124003,3.042167,7.793023,-2.545811,2.088975,5.650579,0.791418,1.646703,-9.509787,5.087012,-3.026544,9.771551,0.790934,5.088296,-1.720113,7.026857,-1.283079,-2.455392,-0.704455,4.561334,-6.437709,-3.965276,0.606576,-6.965355,8.563447,-8.768630,6.520277,-8.604371,-9.711780,-9.240647,-8.838131,8.004650,-7.852963,5.903556,-1.411450,-5.551412,5.581222,-6.067015,-5.160785,-0.764919,8.330962,0.880468,9.720052,1.358803,-7.006988,-4.250744,-5.916526,8.543195,0.340631,9.524610,7.938771,-6.713054,-3.188239,-3.656147,6.299952,-9.120859,4.859220,1.165175,2.372419,6.738673,1.621547,4.224388,5.204541,-0.941705,7.346714,8.233198,-3.323928,2.874614,-6.120261,4.918690,8.729564,-8.719039,-0.301222,6.124862,0.723896,0.060114,-0.970895,-3.306710,0.668793,-6.372264,-0.817281,-1.224273,3.354952,-2.776681,4.378941,6.239542,8.849139,0.090204,3.123724,-7.640844,9.874131,3.679045,-1.416023,-9.164305,9.879762,-3.067556,-2.530292,-8.366572,-0.925470,1.386437,-8.245410,-7.919954,9.257022,5.516851,-7.369580,5.540371,8.328543,5.998857,-0.013250,-8.229556,-2.587549,1.421259,2.482245,-4.099392,-3.824700,3.580926,-3.301978,7.109970,0.963119,9.920636,-6.498001,-2.613996,6.518109,3.819635,3.743566,5.316675,-4.043853,-5.437954,-0.178355,6.057119,-1.162707,-4.108352,2.366103,-0.799201,-0.935205,-3.118715,-2.885359,8.908307,5.537367,1.979838,-0.727918,-2.819945,-3.374160,-4.957974,-0.025491,1.335629,-8.505189,0.295665,1.962046,-7.611664,7.671275,-1.328260,9.614082,-2.427573,-0.549404,7.053836,-4.349119,2.047504,-8.984384,-4.380636,-8.325065,-0.055342,5.997129,-9.349860,6.266275,-7.137213,4.782424,6.649529,-4.233808,2.903253,9.649002,4.885820,7.147021,-3.757321,-3.074133,-4.255337,4.894668,2.187851,-4.259544,3.090344,6.866129,5.000918,1.740114,5.640559,-6.432284,-2.005833,-9.293200,0.154098,3.018321,2.566185,-4.922148,-1.606199,-3.848372,-1.085210,6.729781,2.056578,-7.115964,5.244186,2.618734,7.127106,-5.614078,8.824945,-7.276446,-2.956368,2.168754,4.635153,2.934847,1.558348,-0.099582,-2.099514,5.746609,-4.860392,-4.927155,4.385476,-0.640628,1.248049,4.398324,1.655833,-4.401226,4.600536,-1.586505,4.970184,-2.000429,0.950658,4.560336,-6.968664,5.584394,-7.172424,-5.785226,9.596123,-9.741493,0.934929,-6.950473,1.613384,-0.690558,-0.730287,-0.256644,-6.870298,-6.692823,2.530971,-8.018832,-9.655243,-7.239300,2.139960,7.157529,0.886247,-0.949007,9.337729,-9.514651,3.252422,0.416475,5.920517,9.645141,-7.395130,9.273524,4.015288,4.121457,-6.196691,-8.926448,-3.075674,-5.728744,-0.434922,2.142005,6.713313,-5.556216,-6.077334,-1.069448,6.014447,-0.859977,1.737602,7.794259,0.797316,1.374060,-6.222911,5.305136,0.973388,2.477431,-4.765638,9.097018,-7.419207,-8.415966,7.496824,-4.029691,4.479998,-5.558168,-1.879938,1.009886,-4.951631,4.970936,9.712589,6.772495,4.254938,-9.055573,4.293073,8.980630,9.191261,2.113556,2.339304,-0.249752,-9.173350,9.014852,-7.619940,-7.857131,1.351286,-8.931826,-5.660110,4.979553,-3.986432,-1.446400,8.927563,9.236057,5.903889,4.575075,-2.684076,2.404475,-7.943089,0.170495,-7.092433,0.162311,-9.690870,-8.326264,-7.265478,-6.368870,2.338355,-4.600962,-0.562742,1.252674,-1.133415,-6.216589,-2.648074,9.986616,6.350358,-7.080727,-6.794162,0.854023,3.634590,-8.228027,-2.408797,-5.400464,1.898592,-2.556051,-8.245219,2.251129,3.788469,4.440985,-1.297127,-4.714539,8.296056,6.081254,9.141908,-0.288728,-7.637935,-0.026459,9.451441,-7.291071,7.102287,6.024370,-2.238291,8.168112,-2.289081,-6.690464,6.225879,-4.082401,1.807016,0.612548,8.125392,4.477467,-1.272326,-9.152130,-4.777485,-1.315167,9.031572,4.934566,-5.828115,9.841295,9.228511,4.068486,6.449992,1.077032,6.097740,5.813363,0.510602,-2.436414,-6.236840,7.627108,9.256273,-3.938271,1.911991,2.556750,-1.964165,0.311226,-4.819513,7.383118,-5.797815,-2.402930,2.053579,-1.920733,-6.638103,-3.647710,2.757406,5.065633,1.688783,-1.603045,8.754829,-0.115577,-1.988613,9.405463,1.775946,-1.228619,9.968062,5.407658,-8.078330,8.742925,0.751045,8.999146,-1.815789,0.667002,3.604955,-6.073781,7.628076,-3.189451,-6.787167,-5.969779,-0.454816,-6.144211,0.260862,-8.346412,2.228007,-2.444469,2.503545,-2.503237,-0.506599,6.691902,4.520338,-1.117440,8.047860,-5.577296,-5.501294,7.437495,-7.838588,5.325313,3.723752,6.992896,8.993115,0.615450,-6.169291,-3.681337,-8.651574,-2.378104,-9.184884,-3.631932,2.457857,7.744839,-6.449968,3.877557,-8.588309,-1.784223,-0.334997,4.086385,-8.493450,1.877523,-9.502649,7.035592,5.900785,-4.255117,8.447409,8.365952,1.633947,-4.748851,6.081925,-1.712674,-1.084763,-1.023611,5.358706,3.152657,-2.636851,-5.053897,-0.329788,0.955826,8.276316,2.884653,9.751615,9.590700,-3.289355,-3.090288,8.871037,0.552394,4.008625,4.678785,9.697547,-6.584325,4.293847,-0.136478,2.174363,4.338723,9.187920,3.399515,-2.185444,-1.719179,-8.709504,-1.747087,2.787685,-3.015275,7.276469,2.007940,-2.822567,4.429564,-3.576744,0.852153,9.514165,-4.130234,-2.517845,6.855413,9.134167,2.382936,-4.707977,0.756416,7.164765,2.673698,3.400817,-1.737275,-9.247232,3.712063,9.816836,-9.913281,-6.897764,-2.245236,-9.206402,8.999997,8.850656,-5.961132,-3.672590,3.798433,5.423116,3.077385,-9.924408,-9.763540,3.797269,7.771205,-0.592806,5.299550,0.806926,9.354140,-6.835864,7.355613,2.611513,1.817511,3.366999,-7.996738,0.986169,-1.155623,6.258310,3.251282,-0.639341,0.248462,-1.322958,2.252103,-5.630907,-2.522811,9.455405,-2.625703,6.708679,2.375661,8.384670,3.607471,5.093632,-5.313917,-3.273119,9.836413,-2.572305,0.215965,0.228060,-7.822928,-0.185678,-8.576735,-8.733372,-3.021279,6.554877,4.555162,8.572312,2.166137,-0.258141,7.734639,6.149846,1.908814,-9.285827,9.827390,-7.631136,5.153644,-6.697520,-9.672138,5.643061,-2.741622,-0.962336,1.845849,-1.508155,-4.900532,-5.529836,3.310743,-9.899142,3.591903,9.437857,4.505357,8.944612,-0.764300,-5.463968,-0.615808,-0.758072,-1.372770,-9.503917,-5.290240,3.442005,5.238177,0.119334,5.090662,-0.105983,-3.933449,7.755562,9.699627,-1.932212,-3.582233,-5.993349,-7.214682,3.212323,-6.843232,-9.856817,-4.573126,2.933892,1.467012,-6.075588,2.084661,-8.196509,5.370885,2.402728,-9.314528,-0.631604,-9.182692,7.247408,4.158356,-8.457402,9.575381,7.046884,-7.042521,8.356067,3.216218,-5.562186,-9.870509,-3.322712,2.072881,-10.000000,6.780466,-4.007313,-6.514628,1.022940,8.515413,8.540293,-4.631580,-9.795590,7.650280,9.055038,-4.122783,6.306031,-4.368259,-0.898897,1.501173,3.296995,7.318316,5.469958,5.488312,-7.689652,-0.490065,6.932581,-5.187228,5.570152,-7.448792,-3.570315,-4.290337,3.200370,6.811208,-1.496204,9.186295,2.834940,-7.154936,-3.248937,0.446646,-7.768647,-1.988189,2.992545,4.008986,-8.988118,8.183349,-2.357160,1.373287,-8.120215,0.291712,5.659825,-2.224958,-8.265549,1.050601,-8.839979,7.979282,-1.939510,1.824521,-6.422230,-5.569179,-3.644352,2.436224,-0.760587,-6.956744,3.449276,6.780949,-6.055826,0.889137,-3.458538,7.617182,-5.380533,9.234646,-1.356591,-7.879424,-6.030354,-0.189163,-2.031948,6.996324,-8.271975,4.431793,-4.932999,-1.469708,-1.410847,5.583222,5.176771,5.139370,1.760651,-2.931173,3.614876,-9.608681,-1.264321,-0.419794,-8.475055,4.890203,-2.330583,-9.135782,0.652598,5.609976,-1.995386,7.043509,-0.891300,2.334014,8.703153,4.649175,-9.296902,-8.387820,-9.038081,6.847846,7.986313,1.094459,0.321151,-0.142694,1.827432,-4.379713,-6.504994,4.911449,4.653398,-0.346683,-9.873622,4.347337,2.993183,3.792171,7.404762,-5.061356,0.252961,-4.872844,5.417080,-2.728751,-1.137513,-9.909372,-4.169163,8.680197,1.281941,-1.441374,-9.510295,-4.789923,-7.302616,8.785618,4.120702,-5.367984,-9.931193,0.930736,2.950720,-5.067402,5.111582,-2.066359,-2.307435,5.376465,6.126543,1.548594,1.218854,8.659630,-6.640927,2.741980,-5.654969,-6.274411,-9.856794,-7.086153,9.430559,-2.030809,7.100880,-8.260554,-9.500805,9.178924,-9.548928,8.053725,2.344414,2.820396,-0.394057,9.311655,-9.627339,9.870131,4.512304,-5.077424,-1.851471,5.162732,2.381626,8.570093,0.561382,7.549024,5.859788,-1.368436,4.656844,-5.799609,-7.907380,-0.567877,-4.230063,-3.143252,5.445592,-1.490187,6.174400,5.833681,-7.760450,-3.964194,-2.113328,7.404576,4.215487,-0.252121,7.958140,-3.444708,-9.097822,-6.718172,-5.065522,-9.906859,9.121081,4.384655,7.079037,7.150693,5.403882,7.483728,2.918760,2.376491,-2.840981,0.924091,5.714802,-5.824364,-2.515868,-8.366713,5.296512,-6.654006,7.351279,9.371781,-5.186524,-6.344642,-5.393645,1.326785,-5.029689,-8.983941,-4.290078,-2.201326,4.781329,2.779598,6.747101,-7.985238,9.124963,0.928399,-0.253035,1.432298,7.066120,-6.385613,7.108389,9.234980,3.730950,2.373690,3.947631,0.997534,-1.374718,-8.258501,-7.617816,-9.518413,5.398364,-7.455942,-8.549149,5.377178,-6.867148,2.038219,8.370149,0.133584,7.435788,0.559266,9.422195,8.501559,4.382427,2.738265,2.092845,5.034271,-8.261085,-0.764552,4.799538,-1.326663,-0.283182,-4.789106,1.865503,-8.685085,-1.110847,0.263813,-2.967778,2.997994,3.041078,9.464364,-3.417888,9.261441,-5.092277,2.017742,7.757954,7.123613,5.836206,-8.718162,-5.673996,6.111221,-7.393403,-0.149748,-2.581546,-4.114828,-0.789193,-2.776653,0.102238,8.450902,7.826016,8.673047,0.915669,-3.482035,-9.830148,3.423554,5.604616,7.751537,9.641395,-3.022628,1.221311,9.473099,-9.471768,-2.744298,-9.794401,-3.963170,-8.812976,-1.708881,-8.034074,2.056638,5.818228,8.470863,0.308571,-5.232276,-2.548400,-2.630428,-6.702428,-7.464706,0.121104,-2.974636,-3.281604,-4.484634,-9.398876,-4.015155,7.924100,-0.297223,-6.083306,-6.374234,-3.817645,8.707448,3.625222,8.266105,0.115154,6.113321,-0.238232,-2.201352,-9.085200,-8.992867,-7.033747,6.324108,-6.847496,-2.032253,-7.253164,-4.648489,-3.003318,1.147614,-9.461794,7.024399,-5.102680,-6.577558,-3.744717,-9.659921,9.933034,4.186728,4.639738,-1.943724,-7.996399,8.023994,8.077531,-1.654546,9.732629,5.273020,-5.052533,1.637253,8.295314,6.978565,3.798154,-0.752075,-0.429347,-1.826606,9.843499,6.373231,5.597355,-3.790527,5.510135,-1.644866,-6.657498,-9.740624,-7.222274,-4.272931,7.415913,8.292961,1.404198,-9.391965,-4.969677,1.566188,1.222698,6.906426,9.631155,2.970082,-2.364830,0.606725,7.718498,4.151648,-2.072217,-8.442838,-6.139520,-9.920171,8.706447,6.378516,0.003862,9.371232,-0.797724,1.959113,-5.617779,-9.215683,4.633906,-4.987521,5.225448,-9.747445,0.084277,9.453514,3.048598,3.269764,-9.823667,-5.773782,0.566403,-8.619828,-9.036518,-6.242208,-6.898255,-9.366101,-3.398647,4.033273,-3.905110,7.742862,-2.852506,4.427788,-6.450035,-0.621258,-6.154819,-7.391054,4.066292,8.982092,9.162842,-8.523499,-2.812289,6.953894,8.364361,-9.284849,-7.878418,4.544851,-3.926321,-1.911060,6.734779,-5.477543,9.966244,-6.719497,2.993574,1.749608,9.212668,0.095507,-3.552996,-7.385340,5.856851,5.740666,8.356858,-9.106964,-0.979972,-3.337978,2.072112,3.283711,-1.917709,7.967028,0.291982,-3.670592,7.884439,-5.622901,-9.005781,4.947299,2.378819,8.715368,-9.863468,-4.338537,8.469226,-8.364992,9.269600,9.986051,9.400702,-8.323859,9.760315,0.993181,-4.707493,-0.506810,8.502375,-4.940518,6.419711,5.465953,9.133586,-1.685394,-1.211064,9.456564,-2.141915,9.691239,-2.330477,-5.466156,-9.197022,-0.823723,0.099212,7.143542,-8.087494,3.207027,-8.066122,2.272683,-9.957555,-6.763935,9.525031,9.774668,-1.479068,2.537839,-3.140142,1.452634,-8.939909,3.334487,-5.512259,-8.758983,-9.391804,-8.066630,-5.509169,-4.044549,5.396533,0.706835,-6.151336,-8.049567,-4.335328,8.219508,8.622878,9.801217,-6.161332,4.659497,-1.221494,-0.861571,0.653457,9.205399,-6.970693,8.599638,-9.832899,-2.867456,5.018243,6.183992,5.977104,-7.561903,1.932228,-4.327754,-8.844259,3.232550,0.546240,4.315848,-0.508399,-3.542468,-4.188635,8.445563,-9.508847,4.879784,-5.845401,6.516550,-0.112819,8.543610,-9.352106,5.455878,9.859977,4.435635,-7.578414,-9.476317,3.665965,-2.809891,-6.624775,-4.725847,4.551133,-6.270212,-2.296387,0.962734,8.734452,4.028613,-1.579963,-7.084816,8.653688,-7.647537,-5.511933,-6.355622,9.602054,5.224326,-6.004756,5.225924,0.234216,-2.870562,3.962617,-6.089393,-4.798676,-9.146260,9.785108,-0.760894,-5.489483,-3.215226,4.400418,-6.421027,9.127469,-2.789312,2.985167,-8.214764,5.198499,3.219680,-1.821578,1.981580,9.422027,-7.707609,-3.714019,9.623317,9.971003,1.204109,-4.336672,-1.066726,5.987025,-7.796209,-6.099983,-4.754622,1.118949,-9.533785,0.882695,-5.161873,-1.514392,0.940355,6.072423,7.076498,0.346007,-6.808476,4.490535,9.370644,4.303163,7.056806,-3.233682,-1.104674,9.266869,-4.951413,-2.482771,6.077608,8.826507,-0.855815,8.090060,9.285167,-3.453953,6.676473,-7.085144,6.168553,-4.997530,0.030980,-2.274463,-2.674979,6.934860,-1.969119,6.560503,-0.884064,1.853963,6.535596,-3.231740,6.925665,-2.419975,-9.201029,4.829642,6.097489,0.113074,1.392540,-6.521442,5.940286,-0.013568,5.130431,-5.702427,-3.229181,-7.093060,-5.605013,-0.610219,-9.370249,-4.033516,-1.376892,-1.663941,2.261961,-0.858785,0.747011,-8.244188,-2.560799,-7.484322,-1.576227,1.361225,-4.280176,9.869288,7.826513,-4.571333,-5.305384,-0.857897,5.901011,-2.614777,-4.108287,2.112917,8.591233,5.566839,-1.701155,-7.895379,-2.773565,6.519405,1.273294,6.904905,-9.329974,-7.628972,9.579978,5.452271,4.928520,6.246824,8.358357,6.789797,0.168470,-1.257152,2.948388,-4.039518,6.701282,-2.381798,-9.366789,3.598591,-0.526471,-0.971572,-6.076774,-3.384293,3.614432,-8.525078,-1.832523,-7.194613,-2.883263,9.040472,8.558653,5.791110,4.581534,3.713664,0.816179,-5.826838,1.254130,0.149475,2.462124,0.777837,-7.832702,4.660888,-6.425275,-4.519462,-6.759398,-0.720989,9.309365,-0.299812,4.768766,3.038879,-3.439470,-5.350948,-3.925300,-5.819487,0.120039,-9.073306,7.912274,-7.686951,7.914487,-3.779958,-8.524154,0.728510,-8.333201,-6.033161,-3.264513,-3.496671,-8.484319,-7.046997,3.842727,-5.812857,-3.986052,-9.977089,-4.562915,1.732400,8.807787,1.712515,-3.195751,4.469999,8.853136,7.696770,5.989194,-4.002317,-2.613997,-4.244455,8.222321,7.733221,-7.433034,9.462132,-9.307094,-9.357229,-2.284595,-5.195524,2.876775,4.648292,0.452649,-0.978634,1.268496,-5.178248,0.011467,6.350818,0.656982,-1.469871,-2.568620,-6.390419,5.917765,-3.744203,6.619870,-4.905465,-8.437563,2.937891,-7.728362,8.896786,-6.037952,-8.588304,-6.464527,7.184563,-9.257236,2.654213,5.195092,1.284479,4.089998,8.944703,-3.364165,7.669806,5.122776,9.507444,-1.300086,2.143793,-6.405223,-6.861883,9.878062,0.332041,2.796128,-1.858229,-2.851750,1.419958,6.287329,-9.475960,7.773220,4.104981,-0.893418,-9.315957,7.916973,-1.796090,4.899948,-4.415357,-0.310951,-0.788441,1.107728,-8.072313,2.128256,0.779250,-1.410387,-4.288448,8.816474,6.369508,-8.290952,-1.566915,5.155777,-9.130386,5.836921,-3.383330,-3.551817,2.871779,8.494541,9.860796,-8.173522,-1.680012,0.460924,-3.229101,-8.521685,-4.085189,3.632185,-9.239501,8.248497,-1.975470,8.412826,-8.950338,0.853041,9.670921,-8.507904,1.396580,6.441625,8.787735,8.974173,3.785716,5.131449,-7.761435,-7.986851,-5.018695,1.866920,-7.952126,3.582679,-6.518631,3.021824,9.768832,4.392725,-8.622820,-4.184871,2.147740,9.084213,5.572830,-2.385100,8.642874,-3.130578,9.502718,-1.801660,6.737735,-7.486922,1.075395,9.072067,1.816225,1.203715,-7.898623,-9.545008,8.565037,-6.267864,-9.801292,9.727412,-2.789036,3.812571,7.609447,7.423040,0.391843,0.860931,0.876193,-6.076666,5.506525,-4.910660,7.043498,5.622586,-1.098724,-0.271088,-8.758686,1.880432,2.618970,-6.369912,-2.793408,5.608815,-1.702691,-7.139625,-1.495691,-7.757609,1.118082,8.655873,8.821662,4.453800,-6.075890,0.547488,8.897513,8.836128,6.879374,-2.894742,-9.301824,-7.224494,-4.678645,-2.522423,0.881276,-6.116007,-4.876899,9.180686,-6.242255,5.982954,-6.782017,1.465856,2.062693,2.638625,9.376028,1.450055,7.322944,-0.163378,-7.684874,-9.942508,7.958449,-0.546051,-2.119588,-5.953449,1.894480,-4.604868,-0.375688,7.048571,-0.733528,-3.697647,-5.313977,4.303878,5.439300,4.222866,0.698676,1.313642,-3.713449,-9.615296,-0.154019,0.850044,-4.326949,3.879975,-0.371970,9.496779,6.132120,-5.169892,4.485290,-8.883449,8.754903,-1.198120,2.375419,3.308656,-4.704986,2.920370,-8.006419,-2.866547,-5.391342,9.656348,-4.210339,8.473507,3.732134,-6.327832,-9.215008,3.784030,-7.658963,-5.227964,-4.424563,-5.138318,6.801523,4.745829,-4.120315,-0.300876,5.731094,3.496313,-2.415978,-9.304959,-8.534120,-7.420992,9.277921,-6.190807,-6.796524,7.786803,2.748596,7.123309,0.915153,-5.063455,-9.706390,-4.073488,2.829303,6.923621,5.248851,4.039130,-4.607111,-1.096114,2.510054,-7.033267,0.274689,-3.450599,4.915817,3.074610,-9.076329,-5.051010,-0.214919,0.846615,8.096557,-2.523818,-0.570594,-6.552939,0.851669,-1.088961,-8.574780,-9.561335,-9.812219,-0.309560,-0.257531,4.371365,9.530401,2.829952,-7.731179,9.126485,-4.697113,-6.519665,8.791837,6.294086,5.666954,-9.119901,-5.665704,3.741822,0.130253,-3.831013,1.889850,2.950800,-7.176929,2.830417,6.832925,-7.327758,-2.315351,-6.194008,1.410345,-1.532283,4.495832,-6.048833,-0.067063,-9.955915,6.010657,7.607149,-3.417433,-2.429834,-9.557586,-6.957941,-8.550862,8.912422,2.308147,3.813013,4.805089,-6.841644,-8.094265,1.270980,-7.904132,-6.026046,-4.615888,1.869895,-9.503740,4.445856,4.062032,-8.146381,-4.905544,-2.095348,0.130021,1.332324,7.310855,6.847872,-5.500107,-7.145549,0.207457,1.440342,5.682533,-7.606554,-4.905917,-7.734806,3.687197,1.511646,-9.089678,-3.316396,3.252380,-5.921745,1.335497,-7.247099,-2.961156,-6.718975,-6.249785,-9.071494,-9.199863,3.003569,-3.081035,-8.058994,8.514126,-8.013702,0.812082,8.494025,-7.332152,-0.275827,-6.449701,4.737962,9.903593,-5.687241,1.612230,9.749341,8.537433,-7.044280,-0.495384,-4.889467,4.258925,5.859595,0.705461,9.461959,3.297967,8.633464,5.496697,-2.280479,-4.308081,-1.689368,8.131820,-3.554534,-6.823013,4.721699,5.110367,-6.221344,-1.806645,-4.241204,2.071528,1.880165,8.915516,-2.450875,3.597237,7.421031,4.581133,-6.087684,-1.114103,4.850844,2.793912,8.516135,-4.569840,4.002129,-1.430818,-7.173155,-1.926387,-9.907257,-4.468637,-8.424545,5.697609,-5.306615,0.339153,-8.970286,5.654574,-3.447710,-1.946972,1.493796,-7.355976,3.757895,-5.265363,-9.696068,2.189714,-0.384880,9.197926,5.483005,3.493035,9.730561,-9.717258,-0.981516,5.085140,3.156012,-2.314546,7.536671,7.876807,3.032971,-6.968344,-1.322038,-9.527968,-1.067402,7.860276,9.462840,1.292311,6.082330,-1.857061,8.750622,9.818727,5.885999,8.177994,-3.730550,8.213184,6.001237,6.791474,1.992097,-7.958616,6.719384,9.020752,-9.116095,5.780039,3.688519,1.508820,0.838940,0.172057,1.137449,1.861665,6.153680,2.580185,7.017358,6.214217,6.779454,-9.621246,8.324169,4.479114,-6.709548,-5.868271,-4.190310,-6.154023,-0.074826,-2.189931,-6.765848,9.373384,-9.156284,-6.187946,4.727914,-0.451715,-7.337240,6.891696,-8.572675,6.413397,2.036973,-4.620227,-3.595701,1.666390,-5.139952,-5.919268,-9.889864,2.564387,-2.913129,-6.685735,9.389606,-0.150505,1.481000,9.462961,-4.940238,-8.094282,-6.722895,1.682153,4.286757,6.972060,-9.327481,-1.209027,1.853209,6.889517,-4.079078,4.014947,-7.019562,1.314916,3.746244,-1.329507,8.862343,5.396676,5.137793,-4.257904,-8.062581,3.124278,2.035051,9.278729,5.008597,7.558592,-5.165274,3.574192,-5.800666,-6.340758,5.059160,-7.928943,7.537050,5.646224,-9.686831,2.607284,9.039572,-4.070608,-3.291706,-8.718932,-5.265143,2.495186,-1.998690,-9.922847,1.954422,9.903070,7.040812,-0.472951,7.539848,7.439094,5.657163,-0.380172,6.059934,-0.383556,-0.009538,1.849505,-0.252037,0.547367,8.422714,7.250656,-6.979972,-2.378907,-8.831282,-3.384604,-5.921530,-7.878418,-9.269594,-7.347299,1.972866,-7.840191,7.551232,-8.791100,-1.692344,9.134324,2.768471,8.530330,3.403101,0.932028,-1.117784,2.723197,-9.794729,-2.121907,1.757675,-8.969766,9.690548,-8.493839,5.781516,-0.894086,4.247574,1.611902,4.601072,-1.980607,-4.890019,-6.309950,-8.356390,1.721077,0.051096,4.974202,8.500926,3.229934,-9.253186,3.656794,6.862275,-4.015020,2.892282,7.014937,-3.379700,9.338054,-0.780771,2.416023,-4.665805,3.827488,-7.968187,-8.081486,-1.605696,2.860472,5.813235,-2.365577,-2.325290,4.978080,4.455340,-8.264318,6.347672,-0.325889,-5.105294,-9.263493,5.131720,-1.647546,-1.835693,0.347534,3.638965,-6.218024,3.583559,0.561423,6.875217,-8.232119,3.868044,-8.190848,-3.767345,-9.077004,-9.515216,8.103420,-5.288207,2.360258,-0.076565,-4.232184,5.844428,0.167336,1.248587,1.773899,0.134987,3.808366,-8.201992,5.957793,5.968678,8.912130,-4.337166,8.518122,4.875293,-1.636668,8.600984,8.112955,4.295576,9.453935,3.122517,9.401491,-3.061390,6.720544,-0.634881,-5.875806,5.311973,2.231686,-1.876621,-0.045383,3.317871,-7.508477,5.285985,-1.621443,-6.423259,-9.060848,-4.089086,-6.605619,-5.325190,6.221422,7.850804,-9.247021,-2.310372,-3.900028,-3.408603,-2.837671,9.566191,-3.523591,-4.787486,0.782830,2.252289,-1.686435,1.484263,-1.131671,-2.969171,-5.398751,1.767721,-7.874252,-0.106635,6.362479,-7.178361,8.177489,-0.952674,-9.011601,-0.805064,1.885348,4.962776,3.996574,-6.381879,1.897295,5.211835,-9.566082,-9.070564,-7.013786,-2.530630,-5.365680,5.154446,-9.907506,4.513193,-9.034699,5.798156,0.197879,6.463838,4.104570,0.853840,9.026200,3.758809,7.165604,-4.445890,-9.931188,9.473783,8.714611,-9.085774,-2.648534,6.060845,1.283561,-2.103156,0.606527,3.545347,-2.264714,9.950490,-4.261765,0.895114,6.321643,8.282913,-4.395278,-6.858823,-2.350654,-5.762668,-9.500331,2.613809,-2.522977,2.851396,-2.153900,-5.830029,8.994595,-4.593283,-5.188797,4.508138,1.304366,-5.932861,-6.380738,-2.902935,9.153586,4.007941,-3.513017,-1.611147,7.346967,-9.516372,-8.474724,-7.610119,2.889471,7.195323,-6.536999,7.133388,-5.747527,-7.286282,-7.329083,3.064992,9.927016,9.080271,6.938153,-8.738210,7.148503,-9.432611,1.597079,8.175604,1.912942,6.684856,-1.933828,-8.376280,-4.934303,3.082734,7.013021,-5.069909,5.513859,-0.622986,1.641948,8.539083,0.291970,2.757243,-9.151700,0.567921,2.836067,-7.387255,3.753348,-0.870313,4.061689,-8.401265,-4.900487,2.101692,5.284112,0.961198,-0.565612,6.205994,-0.226390,-4.018690,-3.442106,8.468399,-2.722582,5.379637,-9.005502,7.691917,1.946296,-1.819723,6.545070,3.042745,3.039708,6.653513,-1.932043,0.961876,1.058515,6.494797,-4.485374,-8.133253,-6.339190,-4.772613,6.366171,-4.649886,-7.346246,2.088541,-8.324393,-8.507050,0.211998,3.640165,-9.127222,-9.380873,7.466988,2.804098,-6.455150,-5.840116,8.080647,7.100703,0.579331,2.861637,-6.302106,1.651374,-4.458624,-7.252322,8.854616,0.630558,7.110669,-5.101946,8.286197,-0.970968,4.158178,6.923749,6.143809,6.937427,-3.874827,-8.853428,0.173665,-6.469678,5.181412,6.286454,-8.406583,6.879816,5.276352,-3.999422,1.605691,-3.716020,-5.176656,-7.648108,6.165427,-5.147998,-0.905776,-0.864916,-2.761557,3.094544,-9.412213,-1.185768,5.247528,-7.813358,2.853936,-2.026810,6.140089,3.052038,-9.156727,3.074757,-9.859409,8.495101,9.672893,-6.890285,-0.525008,3.430650,3.803866,-0.091041,5.170721,5.437926,2.111511,-4.726487,-3.838265,-4.095874,1.396495,-8.482210,6.447540,-4.217824,-8.976716,-2.636104,6.741750,5.840514,-4.807612,3.392174,-3.992268,-7.818449,-1.309263,-2.105949,4.476807,7.461492,-3.939728,-0.340716,-2.151139,-8.355954,7.837845,6.338071,4.515158,7.473344,-4.326898,2.046629,1.486483,6.806857,-8.977555,3.566926,-1.939427,-0.526505,-7.516914,9.929040,-1.955692,0.116935,-3.637040,-8.396744,9.698836,6.469746,-3.765164,-1.925677,4.015935,-9.535738,8.455659,3.009551,-8.705756,6.490295,-9.146903,5.527668,-8.025987,-1.165150,-8.144849,-9.531075,2.053210,6.009497,5.079563,0.401275,4.196032,-4.816293,2.627201,4.619686,-7.494236,1.160995,4.921002,5.542202,3.716102,-7.620195,-6.624302,-0.666110,7.560499,0.413260,3.046278,0.221191,-4.219206,-0.193641,9.725747,-3.657154,-3.895972,-1.741504,-9.507611,6.755289,1.320678,6.249076,4.976463,0.396992,-9.157746,8.921813,-1.419169,-4.473872,-3.214718,-6.333885,-8.290724,2.488294,-5.457409,-6.378220,6.041303,4.184950,-9.662466,-8.410630,-9.212756,-7.420728,6.412786,-0.070293,-2.328526,-1.976889,5.307410,-7.398463,3.418201,-2.155683,6.415501,1.948020,7.207244,3.073869,3.916337,2.154486,-2.037470,-5.734390,5.083247,1.615657,-1.625818,-8.002807,-9.490944,9.085405,7.320748,-4.143853,5.826248,0.501714,-1.334551,-3.509892,9.924190,9.098551,0.211264,4.351747,-4.931149,-0.373013,-9.899836,8.536687,7.544624,4.205032,-5.337505,2.648617,8.068794,-3.454668,7.437537,6.714177,-7.630549,-4.682995,9.373494,-8.677502,-8.759389,-2.201928,-4.345632,-2.814118,-4.797764,-8.879983,9.065625,-0.999515,-4.518077,-5.464081,3.773682,-8.388653,-8.821727,0.823227,-8.182308,6.395281,-1.310132,-1.760628,4.463030,-9.706676,-2.705484,2.602017,-0.909998,-5.067985,-7.990204,3.979815,-3.257607,-5.820121,-4.843585,-7.927416,0.768396,-6.885003,4.529619,-8.825893,4.811392,0.750853,4.812691,4.997758,-5.594865,7.271333,-0.975183,2.281604,-0.607543,5.694599,0.470404,-2.190434,1.411307,6.571624,8.764151,-9.024338,-0.313113,-2.566536,-3.685626,-4.762683,7.685471,9.436411,-1.533690,-7.688209,-2.360883,5.741937,-7.331668,6.950262,-1.725111,-3.443187,-9.124178,-2.482675,-1.906487,6.308555,-4.488893,-2.500122,5.312781,5.235977,-0.764444,-8.941391,0.136010,-0.670865,0.953955,-4.386863,-1.607002,3.328799,5.037486,-7.871801,-7.371320,-7.275800,4.977926,-0.001359,-3.939799,-9.178761,-7.103541,-2.564181,-6.524617,2.667240,-1.674352,-3.434307,-8.434741,0.392151,5.948992,-2.919181,1.550593,6.182859,4.472734,4.907468,1.501245,-7.619829,0.363765,-4.792773,5.892079,2.803166,3.111484,7.684047,-3.519300,3.714047,-7.813605,9.151684,-5.052904,-6.017232,2.055913,5.938974,8.197470,-9.510151,-6.846206,-8.146189,-7.207707,6.508668,4.243168,0.468618,-6.500203,-6.114982,-4.175977,-3.347805,-9.821819,-1.123675,3.352106,-3.622836,1.825367,6.365221,1.715990,-9.402828,9.777565,5.587846,-1.449618,-0.365489,9.906135,3.623413,8.489416,-1.317996,-3.040717,7.834408,1.447025,-5.486724,-9.840029,-6.083862,4.036346,9.800649,1.662590,-7.389414,3.402193,-1.392643,3.285529,5.194766,9.667025,-6.742765,-7.238040,6.898622,9.422319,3.060297,0.176691,-7.824600,-1.528602,-5.041585,-9.786551,6.669419,7.769320,1.550134,1.822255,7.534606,-9.943420,-9.217093,7.279812,-5.352054,3.007892,-9.110753,-5.848156,8.589263,-9.129319,-8.548627,-0.300104,0.667899,7.611404,-9.304556,7.487368,8.130110,4.921301,-1.968808,-2.277889,-7.224375,-0.157199,-9.584440,7.981985,2.266204,8.972657,-0.389825,9.393791,-9.563868,-4.890566,4.872388,-3.035471,-2.098391,-2.088722,5.051704,8.690154,-5.752329,-1.444365,-4.780824,4.690598,-2.393914,0.229870,-2.135103,-2.219564,1.766018,-6.728912,-1.929201,-3.449373,-7.216629,3.191878,1.370992,4.184570,5.086897,-8.581296,2.460722,5.561514,0.767812,9.050450,-5.904034,-9.334099,-5.523747,-4.537025,9.219993,1.062717,-1.472396,6.512047,-1.143153,9.816321,7.918828,2.685694,6.473157,-3.602539,-0.108261,3.116062,7.546208,-7.832229,-8.439013,-1.766412,7.788539,1.137208,-3.519911,1.269836,-8.136304,-2.376801,2.083195,-1.251566,6.081957,8.188420,-7.094544,-1.480851,-9.622518,-8.607604,7.052362,-2.943844,-9.651155,-9.544867,6.170326,8.271664,2.800437,7.862023,-1.899411,5.894368,-6.465246,7.956966,1.240630,-4.644840,-6.294652,-9.775888,2.778843,5.622766,2.115906,-7.577288,1.925472,-7.126185,-2.085792,7.161245,5.777118,-4.367852,4.591000,6.055544,8.835013,-4.833032,-7.744196,5.471355,-9.434148,9.437744,2.622806,-8.750466,-1.723716,6.773301,-4.735362,3.396277,4.775392,9.434743,7.399821,-4.459204,-0.841659,-5.851843,9.060247,-0.080772,-7.000704,5.094109,0.121244,9.875579,-0.740257,-1.828159,9.874501,6.044808,6.733327,-6.914500,6.345710,2.077342,6.041742,-6.323704,-5.029815,-1.522539,-8.538408,-0.677774,1.687523,0.717968,-2.399492,-4.775859,3.679461,-2.250950,-6.550284,1.424440,5.143648,7.658147,9.262494,-6.834732,-0.930365,-0.274200,-9.447817,7.188517,-7.022866,-8.876041,-0.780340,1.247050,-0.236555,9.021979,-5.023304,-9.689225,8.525544,-9.533669,8.064845,-0.425432,-1.021435,-4.591618,6.629157,-9.917034,8.188636,-9.031679,-6.372309,8.709436,-0.667805,0.012754,-8.188623,-7.900168,-7.586658,-8.841717,0.274796,7.781749,2.138338,4.297671,9.162287,7.807770,-5.729321,7.395952,1.094734,8.246600,5.758866,-0.043533,-1.251384,6.309641,5.419942,-0.297080,2.477255,-8.583819,7.998841,5.554442,-9.875919,4.339148,9.248049,7.367850,-9.074908,-6.601139,3.914675,7.354465,6.287140,-8.383435,-2.126420,-3.732986,2.116738,-0.567274,-7.611362,0.900438,-0.236722,5.747460,7.009047,-7.771357,1.242031,6.564262,4.292526,-5.700818,-6.531997,-7.054401,9.578226,-1.620710,7.832940,1.231707,-2.904707,-6.158878,-8.140953,-5.523140,-1.032153,8.191324,7.000883,6.555770,3.286986,-6.376987,-1.001235,-6.607488,2.534767,-4.942531,6.910497,-9.603950,3.632297,6.165059,-9.222749,6.714894,-6.273311,-4.111091,-9.911512,7.995098,3.408271,2.636756,-1.943913,2.878310,-5.451850,-4.445632,3.558746,3.518372,-3.104520,-7.417300,3.198485,6.113366,-5.938924,8.896860,5.459888,-2.195889,-3.005676,3.898917,1.246360,-4.352899,-0.492828,-8.137711,3.869855,-6.067410,-5.410778,-5.387086,4.833220,9.709034,0.751734,-0.043201,8.247776,6.443894,-0.595500,-6.280555,9.158604,1.712918,-0.167248,-7.060434,1.704139,7.102685,0.428725,2.152810,9.916240,4.059445,-3.960763,-0.695013,-8.566749,5.717247,-9.782453,6.069658,9.962300,1.302880,-8.631753,7.610493,0.949357,1.367741,0.187487,7.107332,5.649102,8.336802,-9.754423,-0.672601,-4.016269,6.377917,9.148587,-0.396875,0.177722,-1.308850,2.629951,6.693702,-7.803443,-8.399740,-0.748480,8.495757,-3.406495,7.374023,-1.947230,3.771020,4.074787,8.963825,8.958133,0.245059,0.949674,-2.233469,-2.188003,6.817455,-2.674210,-4.615549,5.330194,7.540094,-2.480531,-6.759935,-5.621421,5.508256,-1.021829,-7.909543,9.978677,-2.578476,-1.980333,2.578645,2.602632,8.512937,-1.395838,-7.253171,8.379758,9.279197,-0.413645,-7.442854,-1.076141,-3.070441,-9.374188,-6.587366,8.584257,2.929914,-4.102835,-9.730385,1.028342,2.473791,7.069831,-1.680580,3.256418,-2.447845,3.261184,-8.980036,9.887847,6.563439,-7.617881,5.119892,-9.772790,1.207329,5.948553,-0.694774,6.155997,9.379942,9.814988,-2.851559,3.195031,-9.954750,9.856871,-8.976079,-1.746818,2.624802,-1.205828,-8.959294,1.800674,4.323063,4.402340,7.371237,5.225873,6.469160,-6.650291,-4.620716,-8.746991,5.277124,9.077679,-7.282248,4.373223,-1.731040,-7.556604,-6.761689,-3.283051,7.595657,-2.264134,0.888661,3.513574,-8.099704,-0.209635,9.119142,-4.825687,-7.940622,9.162457,8.330043,-3.426470,-2.521061,-0.104915,-4.003800,-7.409688,-5.366020,1.356186,-1.231172,-1.548743,-0.944874,3.200695,4.507947,-5.621100,-4.457481,1.165387,-6.900567,5.204848,-0.616188,-3.180643,8.733133,-4.106204,7.481408,5.338514,-9.949467,-0.719617,-6.446385,9.617808,9.434975,5.125957,5.077680,0.504821,9.590253,-6.194711,-0.872048,-9.584586,8.969913,4.578401,-6.429787,-7.989104,-3.452949,-8.781934,7.412566,1.480948,6.278923,-7.795718,4.585042,0.216509,-3.451822,-4.127452,-5.216419,-3.486505,-4.542212,-0.124835,-6.289306,3.425654,4.435035,1.432689,8.688303,-2.516720,-3.407376,7.966471,-9.294566,-6.837288,-3.815914,-9.339949,8.060399,-8.238615,-0.587467,2.209855,-4.822647,-9.826194,-9.683076,-5.063148,-8.511154,-8.043100,4.697405,-4.379482,-4.517674,-9.540136,3.340352,5.194322,-5.435965,-8.200122,-0.061230,3.104925,8.766594,5.889934,-0.099035,0.259077,-4.128200,8.950811,-1.549512,4.434968,-3.151345,4.012268,-8.271342,-2.157544,5.055792,-8.700210,-8.617576,-8.488883,6.151809,0.692384,4.092114,-7.788788,0.487259,6.644488,7.341282,-5.985149,-2.864183,6.579042,3.075650,5.349446,1.875664,-2.208610,-0.607542,4.797244,-1.368090,8.287736,1.933433,8.198423,0.563153,-3.321471,-0.883055,-7.237250,0.452056,4.670629,8.271095,5.344748,-6.565639,9.464119,-8.948683,-4.891367,9.406892,-9.671830,3.079669,2.995537,-2.681106,2.062722,0.592976,3.228704,-3.361065,5.177614,-4.786553,-4.846062,-8.728275,6.589154,-6.481369,-2.424023,8.289225,-5.647840,-6.966161,3.564381,-7.563345,6.454134,-4.118903,-2.068416,-5.597128,-9.130582,-1.144776,3.441318,-6.009301,5.466667,3.856361,9.666536,-9.006337,2.381907,4.335829,7.559544,-1.833472,2.926921,5.439072,7.622257,1.634998,-6.236681,-4.157250,2.017108,-1.796799,1.959723,-9.490147,-2.464331,-4.557321,7.831872,-9.232194,1.470833,-1.656337,3.754022,-4.268948,2.608898,7.533498,2.645358,3.778389,-8.535561,3.720167,7.802614,-9.499573,-0.533285,-8.730534,1.587382,-4.201426,4.899922,1.042045,1.106513,7.048405,-9.714190,-3.780385,-9.902839,-3.043992,-1.138386,-0.771586,7.920743,9.957180,7.874427,9.719139,2.231140,-5.460177,-3.366069,8.023905,8.438356,-2.203770,3.030409,-5.743129,0.059929,2.982366,-4.579369,7.404976,-2.037190,-0.469343,-6.375925,-6.280357,9.273279,-8.959872,2.441907,2.803202,-6.874071,-2.008695,5.241826,0.815697,7.454798,-4.096298,-3.273482,9.288383,-2.320469,3.497951,9.122087,-8.743463,-9.336223,8.141962,2.208419,-6.206968,-2.061024,0.466371,1.148421,-6.183989,7.760459,3.444017,5.797160,2.078539,-0.759835,-2.452266,-8.605153,-0.906468,-0.566739,-1.954215,4.245089,1.194539,2.434579,2.188596,-8.997086,2.090120,-7.534018,7.160414,5.955823,3.075292,3.355428,-3.278188,4.466389,-4.170429,-0.041057,0.849815,-5.670541,5.923277,6.354950,-8.177632,0.688154,-7.354544,-4.973993,6.148827,-2.935057,8.414028,-5.071592,7.248791,0.402300,1.394986,6.848960,7.028847,-6.092448,2.177590,0.896921,8.136997,-6.799386,-5.829455,4.041564,-9.106974,-5.674043,-1.267150,2.484224,-0.370547,1.669562,-8.080948,-8.222954,-0.654067,0.517990,8.553051,-7.450556,3.682293,-1.425951,7.279117,7.886804,3.785604,-8.538344,-7.310215,1.153702,-0.637972,0.518027,4.344034,-6.981450,-9.074105,-4.503750,-2.527897,-1.311488,9.014480,7.694645,-9.948963,-7.941086,-2.251494,6.376708,7.468652,-8.158573,-8.769609,-8.260814,7.710025,7.645521,-6.036869,7.903350,-0.736085,-5.810484,-8.325372,6.702560,-5.955931,-7.706870,-5.880866,-3.675931,5.407750,6.780721,-3.916516,4.093623,-6.801351,7.931166,-1.890955,0.366597,-8.417877,-2.273159,2.332439,1.853566,-8.533662,-6.844052,-7.525795,-0.144100,1.304554,1.137142,7.281834,-5.703020,6.643072,8.063663,-9.759410,5.851355,-8.848307,-7.371656,8.261736,-4.686667,4.313537,-6.775016,0.050260,9.707161,-8.664858,-6.997573,-0.297957,4.404781,-5.667826,5.497220,5.062828,7.967785,3.113754,2.787881,4.837162,-0.987098,-9.059461,-7.156935,3.116583,4.764082,-2.354493,9.621627,-2.098936,2.083263,6.597308,1.618892,0.425843,5.890172,-2.034177,7.686935,-3.611374,6.041249,-1.609898,-1.779697,4.362705,8.057621,1.049372,-4.298468,2.795534,-8.471368,3.797596,7.169338,-1.596270,0.481582,1.075057,-7.086982,-4.542021,-8.905456,-1.670185,-2.459017,-6.678994,5.766719,-1.848253,4.884679,6.051817,0.616979,-3.259751,4.875544,1.680768,8.696743,6.930392,-2.722542,3.252892,-1.313044,3.688847,-1.666148,-6.583423,1.119423,2.942388,-7.618460,-9.655046,6.417623,-6.552645,1.217928,1.875183,-9.539095,-5.649419,-4.687910,-2.868769,5.805852,1.575776,4.248387,-2.362895,6.506087,-4.086738,-5.929821,9.631012,3.201331,8.419712,2.257002,9.894782,7.350113,-8.196068,-7.811309,6.538059,-9.065958,8.526699,-6.858915,-5.200272,6.017852,-6.522910,6.055469,-8.772667,7.748455,2.948790,-0.934704,9.960578,-3.328427,-6.191949,-8.836133,0.723115,-3.030406,-4.864195,-3.279990,-2.027805,7.584200,3.007150,-9.199281,0.397653,6.209140,-5.179777,-3.978999,-9.247437,6.026515,5.047923,-5.535051,-4.485341,4.682751,9.689019,5.636909,8.855000,-1.842043,2.362124,-8.041721,3.105054,9.702199,-7.260757,6.540487,5.728270,9.726412,-0.874683,4.167768,-0.319330,7.986114,-8.783036,-9.858779,-6.653880,-0.415737,1.588795,-4.179379,7.050657,0.993276,5.361924,-8.397516,0.775001,7.089582,6.586913,6.619344,7.551856,2.315274,8.290846,-6.971680,6.140661,-5.261811,3.661012,5.945277,-4.256134,-1.090669,9.972495,-5.016183,-5.434744,-3.060535,-2.116701,-5.140389,-2.180982,8.557625,4.083968,4.522516,1.844933,8.091989,9.731772,9.723343,4.591258,0.150954,-7.195632,-9.131866,-7.993789,-7.035811,-7.880498,-5.233913,-5.509447,-6.394095,3.713627,-3.944354,8.075641,-7.425636,-7.332383,3.646924,1.717214,-4.527924,-2.080114,9.170916,4.051042,-6.845585,-3.820876,5.640883,-1.661413,-1.972928,4.655965,-7.119181,-6.007071,3.037187,-3.654483,8.727540,-0.822346,6.843674,-6.816442,1.621889,-5.606490,4.015265,-1.767645,-1.486376,-7.377549,6.023423,2.429353,0.092335,-8.290215,2.479394,5.607437,-5.443409,-5.417033,-7.328979,-2.249702,4.259663,6.809887,7.420086,3.527528,1.388785,-4.232247,3.294905,-0.396331,-2.970550,-0.719276,-5.518683,-0.098932,0.834777,-8.237954,5.278773,6.479621,-9.117863,8.492475,-7.319329,2.670128,-7.149103,-2.023626,6.996412,-3.287413,4.331859,2.445404,-3.156110,2.399780,6.156062,-1.946415,-8.402493,7.729264,-5.514820,2.399095,5.271728,-4.825763,-8.478579,9.927611,-4.332097,4.631264,-1.610227,6.109427,-8.844532,-0.030693,-2.211436,-8.245605,-7.206291,1.624536,-8.184813,-1.376011,7.805853,-1.164387,8.180759,-0.792323,0.997717,-5.676610,-3.894019,8.208152,-9.634300,-2.670918,-0.019614,3.954303,-0.811210,5.799015,4.503946,-9.071391,8.023658,3.156644,8.153815,-2.594376,7.979051,-2.451902,-5.807822,1.210866,-8.880658,7.085664,-3.530173,4.003399,-7.588223,-3.339705,-2.258769,-6.435088,8.370892,5.418939,2.875708,3.668742,-2.792484,7.093065,3.968883,4.583147,-5.872843,-7.477005,5.154015,-6.093589,7.103457,-8.852220,1.885851,1.419597,-0.928987,6.782261,-7.679821,-0.644619,8.432441,3.237907,-4.822857,-2.178392,8.308317,-3.263752,-0.886890,-3.299441,5.002876,-8.872340,-8.571182,6.418661,-8.909181,-7.491117,6.904706,9.480292,-4.754008,-9.798723,8.793248,-2.877669,2.468594,5.108018,7.864399,7.223605,-5.998336,7.256328,3.811477,3.041311,-8.483938,-1.210829,5.796269,-6.630760,-1.794322,-5.145343,4.301057,2.781254,4.642520,-4.069034,-3.675011,5.203484,2.658838,0.945497,1.941206,-4.994838,6.360604,-7.470190,-3.462380,-8.259079,6.174523,-4.382066,5.397099,6.914902,2.967532,6.284597,-6.968610,-1.593035,-3.563571,-4.927629,7.247396,9.763910,-6.408003,2.758319,-0.369116,0.131667,-6.919474,-2.563195,2.838649,3.645788,4.345881,7.982615,3.573889,-1.693702,0.751149,-3.605756,7.299471,8.270322,6.081561,0.446198,4.265209,1.035595,-0.908655,7.450316,3.348657,-2.481978,-9.411444,-1.530843,-1.291756,0.800729,-5.229512,-7.631246,2.744364,7.816982,-5.661313,-5.353842,0.630642,8.668867,3.457754,-9.358974,3.672640,3.013982,-7.791291,-8.046086,-2.913570,-2.049519,4.320730,0.304043,6.013744,0.899749,5.185344,4.136751,4.564286,-6.521972,0.449680,2.245638,-5.642954,-7.312407,1.858239,5.606935,-5.940253,-1.809100,-9.116230,-4.404506,-8.288442,7.182397,7.714208,-0.056634,8.071803,5.672775,7.257024,-7.245700,-4.629056,-2.428077,8.589553,6.381964,-8.721943,7.452001,2.648211,-6.596191,0.618564,7.639121,-5.183763,1.165400,6.493977,-1.377952,2.660440,-7.625758,-8.577225,8.908390,-6.643372,3.734900,-0.642965,0.113529,9.475620,2.215886,5.842618,0.584877,4.369251,6.754498,-9.689594,3.689715,-5.724310,9.036898,5.394034,-0.844521,3.191946,-9.336411,-0.145679,-2.868228,3.487755,-4.475446,-5.379865,-8.122305,-9.098729,-0.084961,0.647322,5.508238,5.414490,-8.205456,7.017280,-2.442168,7.876976,0.125306,-1.318526,8.174741,8.001624,-1.255667,5.826776,8.710421,8.907268,-0.269372,-6.979354,-3.343289,-5.338892,-8.832087,-6.066511,3.368280,9.261538,2.005742,-3.262836,3.121448,0.654192,1.733956,-0.275220,-6.661907,3.252682,-1.196904,-9.041706,6.685345,-4.416078,2.807788,4.667236,-5.275441,0.987954,-0.180458,-9.396571,5.458169,-2.255803,-6.742972,-9.918608,-9.506245,-1.491757,9.098132,3.031641,3.933009,-5.862892,-7.504272,6.889705,-8.231651,9.559558,-2.446479,-4.800122,7.798860,3.837399,7.477635,-9.497943,7.555999,-5.785072,-3.816818,2.764455,7.735666,-5.998905,3.808016,-3.449825,-3.567714,3.193357,0.027435,-9.737367,-3.873620,2.100868,6.364688,6.997425,-8.460968,0.807850,1.673317,-3.609115,-7.109412,1.148232,1.740705,5.215094,6.146632,-9.028399,-8.057528,2.082088,-1.743671,-2.053730,-1.851890,-9.166397,-2.230799,1.281147,9.385694,-4.528963,-5.983790,3.344579,-2.626977,2.784169,2.382702,-3.861687,7.806088,-1.537759,-7.018960,4.064592,-8.938173,4.411891,-5.647083,7.882877,8.399307,8.436849,3.513789,4.797924,-8.247304,3.064789,-7.710913,4.369205,4.017310,-2.084467,0.248707,-7.392706,3.613180,-4.499755,1.942676,6.052327,7.638933,-7.832680,-6.163365,-6.697414,1.207588,-0.068009,-1.241047,0.916499,-1.665597,8.474579,2.873508,3.118375,-6.081270,-0.429576,0.077389,-4.834587,4.078742,3.496680,-3.579603,-4.828833,0.416403,6.703504,-2.345139,3.814798,-6.628636,-2.089557,3.846700,5.603540,1.186760,1.335079,8.292882,-4.449499,-4.236269,-4.883864,0.415072,-4.265149,-5.569712,-6.523486,-1.985039,9.109737,4.099912,4.270271,7.277300,-2.839957,-3.252209,-5.789243,8.891375,-1.066994,-1.419904,-0.001686,1.241879,8.941715,-0.590654,2.188536,4.648865,-3.947555,-4.725627,9.454020,-3.348231,8.216457,4.446263,-1.585625,-3.475738,5.388938,-3.863263,-0.751827,-4.311898,5.474283,-7.459383,-2.191999,9.698606,-6.423385,-5.219705,4.228509,0.531922,4.692160,-1.699715,5.497539,5.343894,-8.268804,-3.146219,0.629408,-7.943075,5.421158,8.862148,-2.512661,-4.801116,0.891634,6.883942,7.169554,0.578864,3.170499,3.201943,-7.698683,2.228871,-9.837008,1.045655,5.582543,-7.728399,-8.860441,-9.528584,-5.678452,2.256985,1.540526,-7.296236,4.439624,6.055609,-3.312306,1.490514,5.076978,9.871401,-3.096251,-7.234078,-3.443823,6.100963,-7.099015,8.019365,-9.478979,-6.069364,8.116614,0.345176,-6.784620,-9.717929,8.654150,5.048327,-9.062368,-9.468116,-7.191115,-5.078709,2.432766,0.377416,9.221610,-6.897126,-9.603580,6.700270,9.778048,-5.858466,-0.789724,-5.918123,4.982944,-9.274577,-8.808085,-7.651807,5.881917,4.398157,-7.195924,4.220673,-7.212072,-2.346146,-8.365478,-2.967201,-8.247830,-7.569880,3.862537,-8.453327,-0.828582,9.028840,3.228944,0.431738,-6.405749,7.270925,-0.199707,3.177427,-3.055321,1.452374,0.842791,-4.028469,-7.921486,-3.303190,-4.316177,-4.833082,-4.236453,7.884344,-6.119971,-7.264528,-4.221881,8.703166,-9.358824,4.808479,-9.538989,-0.365441,-0.333031,7.380716,1.522171,8.181088,-1.726848,-0.855318,8.233403,-4.234219,1.040786,-0.706075,-8.126975,-3.222545,-9.619657,7.591878,-9.339699,1.341791,9.994122,2.061914,-8.667043,-8.983246,8.670994,2.741303,-9.903650,-0.172802,2.930148,7.956246,-3.504997,-5.211403,6.270039,-0.034683,0.674149,6.651139,-8.456166,7.219051,0.277421,-6.897391,8.053707,3.141364,5.966105,9.544212,-1.519404,7.543279,-7.950674,-6.792501,3.901346,9.952110,-9.998402,4.085190,8.623625,6.497781,-2.560185,1.595569,-2.577667,-5.533174,-4.579652,-7.301000,-6.418128,-7.723720,8.251010,3.801226,6.305296,-8.417698,9.860316,-9.632479,-9.550783,4.396402,4.624947,-2.673294,0.254280,-2.802301,-1.163190,-1.061773,-1.673083,8.973050,7.269362,-2.247225,2.043881,-4.720684,6.319716,-7.157315,4.069164,-1.036565,-9.035705,-8.719652,0.765689,-6.423735,8.600785,9.017443,2.123543,5.688136,5.199084,5.647297,-6.267910,0.867534,-8.223570,-0.784693,9.460974,5.237965,1.427304,2.192451,-4.154106,3.412487,-4.567649,2.223045,5.358426,3.532633,-7.265592,-1.764561,-9.626288,-7.402248,3.601862,-9.532110,-9.846495,-0.918382,7.934822,-7.211783,8.066818,7.010811,-9.355808,5.354800,-5.111479,-7.287796,1.069647,1.538963,-9.270888,2.196538,-1.450588,-1.757767,7.478176,2.573037,-1.169604,-4.415455,6.492318,-9.870692,-4.651333,7.600122,-2.651009,1.713830,-8.286908,9.947296,4.000435,-4.964651,8.323102,-3.175349,-5.632032,4.451358,9.179803,-6.285595,-5.060631,3.406463,0.066380,9.579779,-9.785433,3.987854,4.407853,-5.094265,8.961021,2.818716,0.285351,8.694955,6.553970,1.555138,-9.756724,6.740759,-2.881851,8.523362,3.345466,2.237538,-3.399270,1.093229,8.452442,-8.477614,-2.235103,5.371108,3.014068,9.202763,-0.126370,1.344218,8.321997,1.416787,1.748727,4.923109,2.256808,6.530614,1.598065,4.161223,-3.180864,-0.721679,5.249064,-8.390603,-0.390043,2.345302,-1.821993,-6.007317,0.548540,0.984386,-8.479838,-5.897438,1.111731,0.680302,-3.787238,-1.511851,-2.064395,6.434019,-7.130272,-9.039443,-3.442925,0.650656,0.158152,-6.435897,5.344647,3.996131,-1.156654,9.093373,2.597330,-4.993049,-4.535766,-6.115238,2.466429,-9.377371,-7.377796,7.382874,6.217355,4.119116,-6.459139,7.728126,-2.364535,7.572949,-0.988905,-9.103778,-7.628439,4.523073,0.314279,9.826050,-9.995939,3.977047,5.543544,8.495271,7.224590,4.273857,-4.275941,-6.809924,3.655782,1.316467,-3.840162,-6.774933,-7.609850,1.140400,3.922780,8.101957,2.389976,-5.645873,2.512343,5.780527,5.656416,-8.961229,9.572592,-6.857762,-4.924793,6.295502,6.198643,0.515413,8.044979,-1.865702,-5.589267,-9.548672,-9.870994,-5.898139,-3.427462,-7.323921,-3.107713,5.574570,3.097705,-7.805419,2.848927,8.196785,2.242960,3.689589,5.031041,-9.400957,7.387867,9.363121,9.614103,2.840016,7.898445,4.087894,-4.425045,-0.874793,-5.169083,1.403341,-1.097876,0.471648,-9.209097,-6.431027,-0.200044,2.084080,-4.483780,9.203698,-1.286902,0.762378,-2.335181,7.160142,-6.038486,9.847874,-8.188117,-2.497692,9.856054,6.363390,-0.190865,7.952857,-8.258544,-9.689597,-1.377680,-5.500524,-9.763064,-3.022577,8.964404,5.342253,6.286784,-5.413177,-4.907321,-8.311576,-7.736079,8.063715,-3.356560,5.018183,0.447992,7.556173,6.037333,-7.885529,6.594815,7.295760,-7.403467,-0.139060,4.204875,7.925433,-7.245006,3.577046,7.381283,6.731043,2.432159,-4.756339,7.930910,-9.646411,-8.545953,-9.639697,-0.985454,-6.011639,1.146867,-8.661449,4.914705,-9.940217,-3.251652,8.951692,-8.311020,2.270339,5.416713,-7.369570,0.007541,-6.291034,7.775422,7.306759,-9.168537,-7.327016,8.520467,-6.634763,-9.899908,-3.671628,-2.357792,2.153593,-7.943899,-8.818992,-8.892706,-0.558509,-6.120356,2.496057,-9.645556,0.942562,-4.602362,-5.984562,-4.132973,4.707257,6.419420,7.826092,1.767659,-2.981362,1.368689,5.212655,4.493375,2.975147,-2.758486,7.237684,-1.852446,6.068160,-7.505745,-4.064906,-5.636753,0.615835,9.576599,4.258221,6.880713,-2.246255,8.930648,4.417526,-2.763992,-9.619713,0.208558,4.383613,-8.430229,5.722682,-7.252627,9.846156,8.858876,-8.653313,-7.954686,7.806902,7.769040,-7.525682,7.625106,3.204423,9.917498,3.044899,9.948289,-6.590732,1.029647,-7.113751,0.416180,5.552229,-7.367303,5.433739,2.808203,1.496887,-5.308045,2.764597,0.022336,0.956639,-0.994173,5.089718,1.781951,5.579919,6.161722,-0.491610,-7.271702,4.227305,9.967657,1.395085,7.611469,1.917995,-1.070046,-4.365239,7.575517,-7.654566,-8.400093,5.240885,0.333230,-6.804994,-6.889458,1.643376,-2.163077,-6.543527,9.524799,1.732519,-1.966149,3.193817,8.801880,-8.718951,3.902329,5.455656,-4.632442,-6.640975,3.022163,7.429371,3.695760,-8.049237,0.762477,-6.261171,-9.842182,-0.015936,-9.409536,-5.568526,7.920428,3.903002,0.479619,-9.954370,9.769162,-7.346872,0.837120,9.016148,-7.426766,4.902100,-4.385807,6.808687,1.855735,3.121852,6.743975,2.015113,-6.596811,3.605525,3.019408,0.317688,-3.631132,-1.108975,8.428527,6.724570,8.712077,-4.285435,-8.027631,9.125958,3.683665,6.654814,-6.589922,9.095690,8.816025,-2.731344,-6.870261,-5.410291,8.982818,-4.428793,-0.249465,0.934041,-0.715167,8.941870,0.296895,-7.638423,1.815400,5.208052,5.970070,-5.327854,5.108233,6.064675,-8.997327,2.703734,-0.599927,8.555579,6.450550,9.877902,-0.282016,-9.747164,9.716784,-0.790446,-6.155110,-7.710493,-1.253721,3.344664,2.036112,9.584207,-1.392193,-8.218337,-9.886682,9.106633,-1.397429,-0.733137,9.441783,-6.267169,6.486789,3.119683,-9.391401,6.375826,-6.346379,-9.438173,-7.507015,0.441372,-6.910555,0.903071,2.791297,-4.244897,8.166272,-6.618291,4.553500,9.870842,3.389805,3.383860,-8.423351,-5.685097,9.833064,3.283808,-6.359220,-0.630752,-2.363819,-2.487406,-0.827602,6.639616,4.388577,-0.085288,-3.310897,8.276942,-4.354146,0.584408,-6.582326,6.952939,-5.296013,2.046491,5.300526,-9.793607,5.731725,-7.626922,8.199132,-6.185650,8.121452,-3.214219,-4.786069,-2.851877,-4.021901,-7.133469,3.567612,-4.931175,-7.225582,8.670400,3.395402,5.256572,-5.097908,-8.844124,9.522571,-2.442658,7.058173,-0.446511,-1.431645,-5.317152,-6.875526,3.494847,-1.316755,4.511689,4.241962,-1.634416,-3.613408,-8.630209,2.896341,3.106964,6.297997,-0.543901,-2.549314,-2.663274,3.357335,9.367503,3.003196,9.347018,-6.874481,-9.753648,1.549448,-8.899538,-9.300402,-2.156493,6.787551,-8.523260,5.807600,9.687112,4.741361,4.680332,-4.579465,-5.106325,3.882000,8.636648,9.565988,-9.208647,-9.671508,-2.088635,4.479718,1.439357,-6.974190,7.176446,-1.486891,2.563799,-6.481683,-6.903165,7.287577,3.794498,-3.383213,-4.516304,-0.181004,1.554183,8.379491,-1.829021,-1.710669,2.021205,7.801314,8.455493,9.496632,-1.183362,7.145413,-6.286232,3.159108,4.293786,-2.729626,3.801872,-2.914331,-7.225787,7.423004,-0.354633,-6.627702,-5.755962,-1.965053,4.005583,4.152476,-1.219289,-8.788065,0.599881,-7.570845,8.099120,8.070203,7.257240,7.184410,2.592676,-5.809361,7.429729,-7.337757,5.960102,9.406268,-7.012467,-0.170124,5.683084,-7.127483,-9.422995,1.395303,1.881189,2.680567,8.247793,-3.679366,9.187018,-9.539619,9.967120,-7.401347,-4.298534,0.060492,-5.390013,7.589283,-4.343113,8.507810,-7.334883,5.264570,6.228169,-8.906387,7.476297,6.119509,-3.348211,2.183911,-9.621505,-7.783371,3.820632,-0.594020,8.752805,8.216878,8.985383,-2.238618,-9.618898,5.569283,-8.021895,-8.006240,7.162319,-8.610342,0.784166,0.563335,-2.599527,-6.410893,-0.240161,4.898365,-9.157873,3.263906,0.826142,5.373330,4.576844,4.154794,1.350069,-3.219191,-9.811597,-1.810325,-4.153511,4.794976,4.948163,2.278552,-3.460192,5.160880,1.099322,-8.062862,-2.380519,-8.528293,9.795241,-6.744591,3.346385,3.780876,9.259455,-1.297595,5.155651,-5.390622,2.545441,-7.025731,4.014424,5.389574,5.497587,1.309989,0.314007,0.913906,-8.924555,1.583443,-1.813873,9.206526,-2.010080,-6.097982,8.554929,-6.146498,-9.245805,8.448771,-9.871511,-2.760423,-2.211016,-9.751932,-1.954391,-8.774196,3.422322,-3.066635,-5.849187,4.425653,9.161308,6.070526,7.970676,-2.935500,-5.512241,7.156088,-0.090968,-3.064956,6.926066,-9.246575,6.492875,-1.313289,7.117475,-2.792238,-4.918166,-9.717063,2.627430,1.946837,-6.409455,-8.650567,6.471288,6.628351,-9.458092,-5.743246,-8.106535,8.083604,-6.959664,-4.865954,-7.654519,9.989995,3.037849,1.329582,6.103395,5.523819,-1.207993,7.082956,8.471096,9.549597,-1.257595,4.138759,-3.929627,-6.308340,3.020484,-7.424530,-9.279920,-3.061518,-5.787239,-6.916013,-6.598562,9.470929,-7.251980,-4.565541,9.301865,1.860855,-2.178189,9.746853,8.693540,0.165448,-7.471269,-2.564959,7.138658,-2.141767,-6.340271,-5.702908,-4.276293,8.517007,-6.721880,-8.594214,3.568321,9.801992,8.308368,6.156201,4.984599,3.142705,-9.711260,-7.703813,-2.267249,7.678056,8.067131,-4.348146,4.366490,-3.535883,7.814122,-6.578443,-1.786289,-1.641721,-3.287843,-1.944613,-0.925115,5.489092,-4.606729,7.442957,6.406693,6.273647,-2.577224,-8.525462,-2.466001,2.263545,-3.386422,-9.459807,2.533613,-3.035667,-7.893310,6.703703,-7.415805,-6.529485,-6.764163,5.610693,-1.283367,8.588437,-2.600492,4.697585,-2.434957,0.434008,-9.665047,-7.258065,-0.224219,4.181194,8.471603,-2.538096,9.420804,-4.405560,-4.266479,0.194394,2.289737,9.875253,6.438556,-1.231075,7.666986,-5.880208,5.926892,7.630186,2.658099,3.257461,-8.799705,-2.239215,-9.948601,9.738201,-1.397744,9.823021,4.097148,-1.473515,0.336012,7.078648,-6.168430,-6.540543,-7.807330,7.863020,-4.051548,-8.658213,-3.886133,2.648671,-8.989350,2.180336,5.130014,-9.594535,8.277305,9.314570,5.867347,8.325174,-2.694708,8.446234,-9.328846,-7.761519,5.931524,3.006907,1.440015,-7.756130,2.611581,7.597184,1.266533,-0.708464,-9.408319,5.791996,-9.547210,3.004518,2.963579,3.146538,3.152379,-6.963165,-7.524872,7.659296,-1.179176,9.572410,1.856061,4.550656,-8.068822,-0.297274,9.745151,-7.632983,-1.836819,8.017696,4.165747,5.485869,-1.061244,8.115392,1.952112,7.359291,9.469410,-9.553750,0.012518,1.965888,1.689875,-4.841452,9.074370,-2.953592,-7.815318,8.479529,-7.547943,-4.213515,0.835699,1.222827,-1.253369,-4.612770,-3.819935,0.671438,-2.775225,5.993029,-2.191506,3.882443,4.140002,0.785750,7.889787,1.521820,-2.380784,-5.680103,4.878632,-7.590955,-5.577043,4.719614,5.326204,-2.121574,8.681501,5.721245,6.817602,-4.076140,-1.359805,-6.908264,-3.987924,0.712356,-0.580446,-6.059797,-0.811704,8.955369,-5.534889,9.193662,5.058020,5.885791,7.672529,-8.907323,3.538909,7.385282,6.319209,1.123482,3.905561,-0.532791,3.733089,-8.605731,8.932259,-8.876809,-4.950252,-9.518822,-0.294685,9.549206,-4.973692,-7.320125,-4.166722,-7.295455,-0.885665,7.101918,-6.071065,9.834697,7.907182,0.416384,8.944400,-1.651300,4.427649,-1.580372,-7.322771,-8.067225,1.989602,3.660419,-8.166994,2.740869,0.081438,8.384111,-2.019145,1.038112,-0.553496,6.445217,1.269193,2.993528,-4.123158,-7.794288,0.262178,0.121883,2.380204,-7.688547,-9.923231,-2.183930,0.212787,-9.324568,-8.585531,3.741549,-2.306997,8.989746,-0.091847,5.408204,-4.777183,8.827846,-6.916579,-8.315188,5.557105,3.768544,9.202330,-5.673537,8.985697,-6.422684,-0.495028,-6.195226,-8.884570,-6.560203,1.105841,8.355696,2.389261,8.929154,-7.720687,-2.850981,6.761565,5.845457,6.240799,8.042257,-1.029065,2.752299,4.188119,-7.053521,2.695391,-5.045233,-3.041520,-7.789595,-1.538951,4.982655,3.803275,3.205122,2.115182,7.256292,-8.709608,-5.729793,0.045605,4.465379,7.145763,-2.425811,8.660399,8.997386,5.492733,4.662818,-1.703951,-6.528851,-5.723696,-3.689594,-1.351141,4.749920,-0.340121,-1.093010,5.647660,-8.345185,5.376204,5.061478,6.145709,-3.243972,-1.097477,-8.781762,-2.885781,-2.131190,-8.550873,-9.684101,6.239102,7.425464,1.601255,7.326009,-8.896903,-1.510802,-9.261102,-3.764336,-2.241775,-1.323664,-2.938356,6.460246,3.956999,-8.120363,-2.668124,7.698206,-5.854396,8.318309,-7.304414,-8.286904,-2.585752,-7.634769,-0.631927,-3.762725,1.775441,6.920675,-1.902836,-5.419827,-6.566300,2.342047,1.267304,-8.928756,-9.493919,-1.722353,-7.876755,9.994975,0.494997,-3.909297,-7.256683,-7.872802,8.282966,5.405284,5.887895,-2.109336,-7.079551,-2.223347,-2.726749,5.054717,1.308189,1.813101,-1.466692,-0.216943,-2.046395,0.219426,-7.272367,-4.907150,6.687804,6.265677,0.307590,6.543287,7.553845,1.111316,-4.981826,-2.267211,-1.659422,-0.302899,-4.724814,-9.786245,3.369547,6.920937,-9.237282,8.692217,-2.244284,-9.192147,-7.325197,5.124109,9.095231,7.122142,-3.488988,8.301191,6.598243,2.422768,1.033474,-6.108530,-1.762818,-5.393772,4.440166,-1.540134,-0.952419,4.150400,-1.728467,-7.404169,-9.035822,-9.329896,-2.159204,8.915095,1.203091,9.023276,8.426632,5.839146,-9.395886,-4.545519,9.488298,9.183655,6.827613,4.436714,8.566299,7.301314,6.890634,-2.987968,-2.016021,-0.090224,6.490899,-1.501504,9.831415,-6.118720,8.018679,-4.388031,7.215897,-0.213673,-8.671327,9.003900,1.105966,6.550771,-5.217989,-1.473677,-3.713846,-9.710588,4.723903,-8.465162,-0.470591,-2.687986,7.294988,-2.195267,-4.250405,9.858715,-2.446187,-1.191200,4.058226,9.532665,-7.244884,-4.824525,-6.292340,-9.610528,8.884991,-3.838523,5.654217,1.224387,3.161737,4.975352,-9.913850,7.582252,6.063440,8.342701,7.031766,-2.914438,-7.434724,-2.141356,4.088821,-9.177149,3.769683,-2.365780,4.893416,9.596472,-8.090399,-3.591272,8.349984,6.828983,-8.599614,-8.665529,6.338087,5.207293,7.459038,-8.159255,-8.233182,-5.383568,-2.810787,-2.824748,-8.696610,-8.116064,-0.110115,-1.743683,-6.827267,1.806402,-6.284721,3.515162,-8.531576,2.251138,-9.722813,6.132760,6.819893,8.879196,-5.220864,5.713218,2.241216,7.759769,8.153449,-6.582827,-7.504735,-0.708224,2.169962,-5.259354,-8.511361,9.788573,-6.860831,6.972434,-5.240005,4.179979,-7.308983,-8.455549,-9.277074,8.648651,7.899932,-9.028174,9.976041,-6.480606,-1.172047,4.385109,-1.420401,7.814456,0.991808,-9.402199,2.579352,-5.030066,4.652297,-4.709513,7.057761,3.314149,3.472779,-5.829755,-1.014742,8.673714,1.681719,7.611535,0.503374,-5.184294,9.950162,7.850141,-6.980714,-3.708364,-2.758048,-8.192082,-8.102609,-7.836581,8.902936,6.570430,2.184018,-0.252584,5.280134,-0.631628,-9.198722,4.516715,-1.814969,3.970907,-9.567138,-0.018667,-1.987996,-7.500005,-3.520696,-9.328074,7.885818,3.387154,-4.096351,-2.877523,8.469027,-6.985692,0.206915,5.239394,-0.601123,7.333658,-1.487776,0.963201,-1.056950,1.208706,-5.621165,-9.291307,3.021681,-2.862036,1.406639,1.588381,-0.349939,-9.042660,1.178615,5.838018,-4.636176,9.654299,-7.024102,3.062921,-6.684720,9.869154,-7.721997,5.674051,0.361454,3.075464,-6.144789,5.018393,9.511311,-3.412820,2.916959,-0.596693,-4.709477,-5.017986,9.882433,2.789762,-2.143777,-1.842371,-6.915417,1.801479,-9.573579,-8.249517,3.180633,5.261280,-1.974008,-5.932520,7.496483,7.403475,-4.806875,-8.054823,-1.283557,1.409866,-7.114601,7.987329,1.015690,-9.499948,-8.099192,-8.890956,-2.658647,-1.715285,-0.186572,-7.395995,0.980871,7.870575,9.037787,8.494562,-8.430252,-9.079969,0.725104,5.144979,-6.206558,-7.749274,5.664927,1.446079,-8.585998,-4.889720,-4.148608,-9.617295,-2.101652,8.203576,4.706224,0.710696,5.310925,-1.247405,-9.779443,-8.361122,0.351385,0.314225,0.318026,-8.251483,-5.769809,-4.590963,4.359879,-3.197775,5.275341,8.440277,5.837683,-0.820040,-3.444195,0.466032,-6.349352,-8.709802,-1.428695,-4.542183,-0.115693,0.380498,9.450283,4.291829,-3.888530,8.155896,4.808491,-1.312052,3.035879,8.214126,5.062954,-6.265326,-7.231067,6.568839,-2.117041,1.370752,-1.425799,1.078617,-5.023913,-5.814382,5.281678,-7.239493,-0.464857,2.152238,1.515601,9.384355,9.157538,9.347017,-5.516403,-5.312533,-7.529612,6.420738,-0.696993,4.793774,0.768007,8.610164,8.072100,4.461973,-0.282597,2.205801,-6.978669,-9.973862,1.245902,4.488462,-6.650874,-6.763455,2.780632,1.787162,6.948523,9.191278,-2.029691,3.991481,-9.614509,8.327539,8.435839,9.443700,9.810843,7.114426,4.005214,5.647545,-8.502821,-9.796799,0.405994,8.421058,-9.624976,-9.688170,6.825537,-5.293300,-9.030988,-6.554027,4.236213,6.030416,5.702670,9.080086,-4.983464,-2.307134,-3.689219,-7.273871,-4.273552,-5.008801,-7.218647,0.516174,-3.996152,-1.424842,3.355434,-3.124780,-0.533371,5.439884,-7.405557,-1.826535,3.688986,6.240815,7.066580,-2.272960,9.086593,9.599440,8.649654,4.711990,-3.317996,-7.554243,-7.729624,-1.954517,3.800473,-8.057262,-8.941278,-0.576081,0.257599,-7.362404,6.091350,-5.170228,0.912605,6.008131,-3.867231,1.623403,-6.131700,-4.047174,-6.026603,6.500490,1.228062,-9.879886,-4.992686,5.506082,-8.578957,-6.055103,-0.356315,4.601882,-1.126539,-8.910708,4.121998,-7.060522,-4.806814,5.565365,4.604635,-0.953289,-3.925819,0.350643,4.687836,1.007594,-1.284808,6.544199,-9.045859,-4.852192,2.520120,-1.348570,-7.462449,-4.971248,6.629731,-8.910650,-7.476407,4.797905,1.789240,3.396129,-8.838825,-1.348709,6.056867,4.590409,-6.850753,-4.482183,7.587801,9.678669,3.251496,-0.117322,2.701344,-3.023581,1.768781,-2.877850,-5.439751,7.109009,-9.649108,4.031976,6.493128,-6.624086,-7.442054,-9.432005,8.793261,-2.050296,6.414292,7.472404,2.164630,0.320165,-4.125020,3.321666,8.891684,5.464050,-4.650124,3.900152,3.042835,-7.696067,5.371866,4.808825,-3.143212,0.386438,-2.307384,-5.307397,-0.721777,-7.172620,3.024879,9.836493,-7.425918,6.297434,3.064086,9.209553,-3.936478,6.526709,-3.667402,-9.211991,-7.083254,-7.756820,-2.416260,-4.950987,-2.385092,5.851376,-4.529900,0.609619,8.395665,9.164605,9.970904,-9.055898,-5.728228,6.920109,-2.420509,6.696105,-3.652413,-6.831478,-4.927142,1.039517,8.527081,8.366266,-3.496058,8.304995,1.958754,-1.447043,3.617060,-7.436341,-8.183674,-9.405418,2.669803,5.597006,0.649832,-2.945549,-0.754536,6.046602,5.443919,0.492755,5.673425,7.227764,-4.800213,7.524502,-3.916882,0.997212,-6.192523,-2.684487,-9.505037,2.099467,2.632487,3.132812,2.395669,6.401505,6.523972,-9.758935,8.469142,5.300074,-3.068390,3.494811,-3.983927,8.986069,-9.795471,-3.638738,-4.527650,7.930474,-2.128946,4.868241,2.412196,-7.881045,-2.312455,3.884836,-3.854496,3.974706,9.499625,-2.987458,9.907108,-0.826409,0.345057,-2.892970,-5.163633,3.944102,0.847879,1.051831,9.484546,7.922452,-8.473154,-8.363494,-5.207839,6.690845,-8.572125,3.936090,-0.657780,-1.789858,6.257209,5.620344,-8.848339,-2.256700,9.701235,-6.028196,6.084357,-8.366656,-4.067579,-4.075509,-1.861856,-3.054772,3.527781,8.594134,-1.028101,3.490406,-1.765110,7.199176,4.673645,-0.434810,7.414642,-7.154073,0.099879,3.371397,7.116467,-4.500228,5.154380,-5.819849,-7.423128,-2.663327,7.894794,-6.124190,-9.699656,-4.733724,3.180952,4.499242,8.286271,1.591084,-2.880962,-0.199252,6.678652,-7.456790,-4.902168,3.844826,-3.451487,5.899488,-8.035341,7.828218,8.489320,-8.047497,0.591699,-5.339722,2.484832,7.882605,-8.710870,8.130713,-6.671124,-3.509793,2.848530,2.868317,-9.775171,4.589517,2.478370,8.875690,8.149033,7.957093,8.496665,6.246146,-7.070380,8.422878,0.730301,-9.996368,-8.089773,-0.896494,-9.698721,0.004688,-9.610098,7.745596,0.817732,-1.996861,4.189782,7.142050,8.860098,1.264353,3.619418,-3.790740,-5.400309,-5.592557,-7.634774,-6.300086,7.522947,0.009325,-0.918074,9.009150,9.072816,-0.020340,9.709621,-4.764122,9.654397,-0.079405,-2.694697,6.403136,7.015163,0.369365,-6.969375,9.438818,8.086874,6.507646,9.355397,3.064407,-8.809317,0.303668,-7.231234,0.308345,-6.684481,-8.709312,-0.393571,6.218392,-1.912102,4.702397,-1.143897,-4.176680,9.084404,4.143073,-2.818018,-6.188539,5.883839,-8.169067,3.369843,9.581032,-8.368521,-9.375118,6.000169,-1.607998,-7.333098,-4.605044,-9.223166,-7.585069,-8.371003,0.299630,-2.964625,3.523185,5.910270,7.526554,1.576682,-5.171667,8.062815,4.943450,-8.898878,-4.311583,3.828964,9.455612,9.883926,-1.078362,-4.066424,-1.204372,2.890802,-2.317465,9.271638,9.985746,-9.054153,-2.635398,-5.557678,-2.735070,-4.630599,2.459484,4.800179,9.384707,-8.734350,-8.762062,7.674360,1.309863,-3.526685,-2.728954,-5.851806,0.019627,8.779932,-0.939601,6.846028,6.948875,5.792457,8.445577,7.085661,5.488283,-6.433573,-4.862412,-0.095730,-5.690263,8.439365,-6.421884,-4.009244,-9.221372,-1.069969,7.772981,4.334583,9.830912,5.528676,5.720118,7.474143,-8.663759,-1.521378,-4.030023,9.168025,-9.692730,4.964191,-4.527080,-2.665707,0.864808,7.415385,-2.029832,2.719523,3.557651,-1.930789,-8.562693,2.121447,-6.776200,8.449509,-4.194719,6.619407,-4.271925,3.480981,5.206152,2.744346,-2.310827,3.429102,-9.144218,-5.386346,-6.960994,-1.205912,8.114291,2.399841,-7.955967,-9.412206,5.885774,6.143694,-6.592717,-3.573416,-2.192426,-0.007773,-1.968827,7.159677,0.037791,-3.667926,-1.668882,-7.278759,-5.903455,5.785328,-0.285475,7.931150,-9.887772,1.184867,-6.844800,-1.818395,-6.597131,4.586533,-3.092332,6.275600,7.151774,0.546724,-5.021069,0.753718,-8.453284,2.326433,-3.580849,-2.253936,7.175727,9.667707,-2.784602,-1.546156,-5.439640,4.093903,-6.233502,-5.538591,9.119452,-0.532484,0.685541,-8.534423,-1.379452,7.816568,4.598297,7.245283,9.472957,-7.161499,-9.354235,-0.074554,-6.060161,-2.140290,-7.695943,-6.001097,-4.661272,-7.384897,-5.261578,6.469207,-4.629402,9.292194,0.559159,2.486006,0.281771,-5.033349,-2.759000,3.029587,-4.969859,-7.748011,-8.506872,-5.612998,3.663989,1.490396,-1.421183,-7.257860,3.572661,-7.063225,1.062298,1.836193,3.803218,-5.055910,3.916644,-6.622339,9.122668,-1.183817,-6.827311,8.688650,7.581291,4.946677,6.531026,2.467010,-0.576669,5.851077,5.141030,-0.338896,-2.172642,-3.805883,-1.991282,-8.040390,3.922189,-7.383231,4.019895,2.327304,-8.624240,-2.373591,2.213098,-3.694311,5.896952,8.076933,-8.302244,5.833186,-6.234988,-6.933753,0.591364,9.570596,-4.600730,-8.400898,9.325443,-7.112808,-4.475976,3.775491,-0.884804,5.568730,-6.911078,-4.215171,6.003602,4.784500,-4.847873,-1.733677,-6.411982,-7.429707,0.134777,7.408460,1.822995,-5.615079,-4.548850,8.442881,0.468438,8.558755,1.027591,2.601249,6.658480,-9.346560,-1.951187,6.152228,-9.149529,3.107921,-2.389272,-8.816830,4.038444,-8.040906,6.219745,-4.944256,-1.515407,-8.678182,-5.560155,-9.367933,-0.858674,1.361239,-5.458057,-7.248257,-1.807500,-2.121286,-7.573487,-3.680547,-2.709121,7.045688,-4.973431,-4.866372,1.203897,-4.600519,-3.139673,-3.517410,-5.984913,-9.317854,-2.517942,5.355574,-2.342958,-5.861569,9.165727,-2.157496,6.044357,1.654101,-1.517561,-1.434539,-2.717220,2.146172,-2.774679,2.322427,3.535279,5.963675,-4.159889,-1.306559,-4.592859,0.003444,-5.235714,5.488294,-3.447690,4.475133,9.861021,-5.693989,7.800254,-8.659131,6.048367,-9.488331,7.257452,5.139901,-2.163587,6.960621,-2.840926,-3.346160,-4.126961,-2.486586,-1.208956,7.372727,9.311453,2.092190,7.851156,-1.478600,-5.716663,5.914428,-7.142740,2.307150,9.188374,-3.474211,-9.831228,-6.897047,-7.832716,8.650372,-2.534003,-4.242033,-3.651997,-7.705689,-9.032906,9.681567,7.975178,-3.723557,7.554426,5.356177,-7.346719,-3.515448,-2.265839,-2.492008,7.238717,-0.108881,-0.981530,3.302243,-4.255102,7.518250,0.526107,3.372447,0.199585,-3.673051,-9.780384,2.590297,7.407971,0.189236,-4.303558,8.436275,5.380754,-7.150300,-8.722246,-4.277825,1.810434,6.799047,-6.798266,-1.914981,4.942399,-6.158603,-4.364701,-3.924328,5.133834,7.774679,5.047935,4.932964,-3.836231,4.505209,-4.438359,-3.556972,5.812090,-7.903262,-7.689666,4.543412,8.328074,3.467685,-4.278711,-3.016689,8.477703,1.460884,-6.069101,1.315987,-1.568868,6.079448,1.505079,9.481401,-4.435517,-9.056496,-4.596406,-0.773160,-9.928047,0.754748,1.677172,-0.945638,2.287157,-8.069233,7.370590,5.421879,-8.415825,-9.367944,-3.314100,-4.694260,9.005979,8.929355,-0.275187,0.145814,-2.326704,0.279197,-3.195653,-8.840047,-5.012635,5.419472,3.503920,8.650525,-0.951928,5.922089,8.309181,1.085081,-0.473816,-0.625908,-6.015527,3.020478,-9.495751,-7.985860,7.302115,4.048219,6.455789,9.212933,5.025562,-8.373458,-2.297927,-9.966262,5.049015,-1.914481,-3.643323,7.309229,-2.942057,8.458965,0.924565,-4.300384,8.134501,-1.050641,-1.021901,6.051032,1.249416,0.989257,0.159449,7.303938,6.862090,-2.221849,6.941080,-8.985977,9.445409,-0.640869,-9.960442,2.815899,-3.610069,-3.188361,8.586987,-5.982714,-6.122141,-7.257116,6.904147,-0.740456,2.405565,1.037812,-8.608844,-9.143410,1.291650,0.058759,9.313370,7.803082,-8.378652,7.647764,8.156967,-7.366367,4.110829,5.570648,3.140589,-9.314956,9.116536,7.193562,6.573412,0.559030,-5.757020,-2.886141,8.573256,-3.538231,-8.879627,2.829957,9.829269,7.889105,-1.094740,-9.947762,-8.591276,-6.886954,-3.512040,-0.665970,0.801067,-7.642499,-7.507123,-1.062879,0.964264,6.812412,-2.572891,4.823822,4.896223,-7.344593,-0.013285,4.281976,5.584083,-7.829251,2.128719,-1.476537,-9.224975,-5.380555,1.199253,-1.375457,0.553800,-2.955425,-5.268460,-9.414897,-8.768805,4.067813,7.871131,-1.458437,-3.241245,-6.814238,3.607599,-8.173762,8.238635,-2.246167,9.811077,3.339423,-6.474855,-0.641124,-8.517085,-9.256712,-3.032678,7.723617,-9.198292,-7.695663,-1.225321,-6.177375,3.501551,9.884819,-8.419052,-9.319231,-3.709549,-6.700151,3.518395,7.795227,0.971006,5.363402,4.477196,5.831218,-0.806022,-0.359871,-9.286605,-7.680926,9.919625,0.849582,9.091675,-2.234579,7.184103,-8.309817,2.696342,-4.737404,-1.370646,-1.430259,-5.720267,4.796329,-5.997584,1.400971,5.577412,-7.620812,5.580865,-4.515752,7.635719,-4.287842,9.116254,-6.126918,-1.301587,-5.132160,-0.244010,-3.977807,-8.797595,7.928017,4.185728,-8.756408,-8.487198,-5.947554,-6.225223,-1.521455,2.691916,-3.209178,9.865640,0.095625,-8.398809,-7.723621,9.505607,8.082173,9.301175,-0.357242,-4.681015,1.505636,8.389910,-0.203366,-0.843166,-5.995729,-0.985590,-5.508792,1.416866,0.374172,9.232006,-9.872891,8.731813,5.258513,-9.276760,3.311531,-0.278282,7.187202,-2.718341,3.763626,-8.939791,-5.953266,-6.424252,-6.894711,5.911194,9.504881,-9.995611,4.074753,-9.317931,-7.531237,-6.788441,5.896083,-9.837636,-0.444154,-7.689011,1.175416,3.083739,2.223917,-6.477891,3.335252,-5.237161,2.112845,-4.539597,-4.999788,7.641684,2.577770,-9.091261,-4.281594,0.592001,-5.334476,-0.614626,-0.209521,5.680150,5.012343,-9.020664,3.267199,-2.719910,5.558264,1.842660,6.138580,-0.942580,-7.224706,4.771043,8.857265,-7.682352,-1.223615,3.930609,-5.780760,7.402217,-1.174428,8.547792,-7.358688,-5.150174,-7.417563,0.631597,-6.696704,5.396330,-4.672327,6.314060,5.225541,5.223335,-2.360584,8.271990,-6.339939,3.580704,-5.159348,-6.265653,-5.551229,-9.491455,2.103570,-2.046470,1.192811,-7.059401,-2.784901,5.600790,4.768754,6.347195,1.131132,8.383744,5.133215,-1.848428,8.921419,-5.597239,-7.434954,-5.264804,-6.041502,5.510325,-8.943067,-5.949531,-7.564799,5.570178,-8.412619,5.649268,9.944214,8.454522,2.203127,-9.359059,1.059030,-8.609172,3.431661,9.883790,7.045014,7.614024,-8.755097,-6.577867,3.960971,4.449965,2.054806,4.929675,5.765914,4.632965,-9.606599,5.639211,9.671202,7.161264,-9.424935,-3.140685,-2.828324,-0.550261,0.058817,3.604932,-4.735746,9.514593,2.317966,-2.938325,2.470768,-9.613604], dtype = "float64")#candidate|4594|(11550,)|const|float64
call_4591 = relay.TupleGetItem(func_1278_call(relay.reshape(var_4592.astype('int64'), []), relay.reshape(var_4593.astype('float64'), [1, 770]), relay.reshape(const_4594.astype('float64'), [15, 770]), ), 9)
call_4595 = relay.TupleGetItem(func_1282_call(relay.reshape(var_4592.astype('int64'), []), relay.reshape(var_4593.astype('float64'), [1, 770]), relay.reshape(const_4594.astype('float64'), [15, 770]), ), 9)
output = relay.Tuple([call_4582,call_4591,var_4592,var_4593,const_4594,])
output2 = relay.Tuple([call_4583,call_4595,var_4592,var_4593,const_4594,])
func_4604 = relay.Function([var_4592,var_4593,], output)
mod['func_4604'] = func_4604
mod = relay.transform.InferType()(mod)
mutated_mod['func_4604'] = func_4604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4604_call = mutated_mod.get_global_var('func_4604')
var_4606 = relay.var("var_4606", dtype = "int64", shape = ())#candidate|4606|()|var|int64
var_4607 = relay.var("var_4607", dtype = "float64", shape = (7, 110))#candidate|4607|(7, 110)|var|float64
call_4605 = func_4604_call(var_4606,var_4607,)
output = call_4605
func_4608 = relay.Function([var_4606,var_4607,], output)
mutated_mod['func_4608'] = func_4608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4474_call = mod.get_global_var('func_4474')
func_4475_call = mutated_mod.get_global_var('func_4475')
call_4622 = relay.TupleGetItem(func_4474_call(), 0)
call_4623 = relay.TupleGetItem(func_4475_call(), 0)
func_4005_call = mod.get_global_var('func_4005')
func_4007_call = mutated_mod.get_global_var('func_4007')
call_4625 = relay.TupleGetItem(func_4005_call(), 1)
call_4626 = relay.TupleGetItem(func_4007_call(), 1)
output = relay.Tuple([call_4622,call_4625,])
output2 = relay.Tuple([call_4623,call_4626,])
func_4630 = relay.Function([], output)
mod['func_4630'] = func_4630
mod = relay.transform.InferType()(mod)
output = func_4630()
func_4631 = relay.Function([], output)
mutated_mod['func_4631'] = func_4631
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4667 = relay.var("var_4667", dtype = "float64", shape = (8, 2, 11))#candidate|4667|(8, 2, 11)|var|float64
uop_4668 = relay.erf(var_4667.astype('float64')) # shape=(8, 2, 11)
func_1815_call = mod.get_global_var('func_1815')
func_1818_call = mutated_mod.get_global_var('func_1818')
var_4674 = relay.var("var_4674", dtype = "int64", shape = (78,))#candidate|4674|(78,)|var|int64
var_4675 = relay.var("var_4675", dtype = "int64", shape = (96,))#candidate|4675|(96,)|var|int64
call_4673 = relay.TupleGetItem(func_1815_call(relay.reshape(var_4674.astype('int64'), [3, 13, 2]), relay.reshape(var_4675.astype('int64'), [1, 96]), ), 0)
call_4676 = relay.TupleGetItem(func_1818_call(relay.reshape(var_4674.astype('int64'), [3, 13, 2]), relay.reshape(var_4675.astype('int64'), [1, 96]), ), 0)
bop_4688 = relay.maximum(uop_4668.astype('uint16'), relay.reshape(var_4667.astype('uint16'), relay.shape_of(uop_4668))) # shape=(8, 2, 11)
output = relay.Tuple([call_4673,var_4674,var_4675,bop_4688,])
output2 = relay.Tuple([call_4676,var_4674,var_4675,bop_4688,])
func_4709 = relay.Function([var_4667,var_4674,var_4675,], output)
mod['func_4709'] = func_4709
mod = relay.transform.InferType()(mod)
var_4710 = relay.var("var_4710", dtype = "float64", shape = (8, 2, 11))#candidate|4710|(8, 2, 11)|var|float64
var_4711 = relay.var("var_4711", dtype = "int64", shape = (78,))#candidate|4711|(78,)|var|int64
var_4712 = relay.var("var_4712", dtype = "int64", shape = (96,))#candidate|4712|(96,)|var|int64
output = func_4709(var_4710,var_4711,var_4712,)
func_4713 = relay.Function([var_4710,var_4711,var_4712,], output)
mutated_mod['func_4713'] = func_4713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2097_call = mod.get_global_var('func_2097')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_4743 = func_2097_call()
call_4744 = func_2097_call()
func_3398_call = mod.get_global_var('func_3398')
func_3405_call = mutated_mod.get_global_var('func_3405')
const_4763 = relay.const([5.511781,9.217010,-9.439434,-1.552960,-1.290896,-3.891618,4.812164,9.679866,-9.897391,-8.358190,3.954125,4.881752,-9.748616,-2.177681,-4.934213,5.957457,-8.009455,1.190118,-5.687504,-9.046926,9.012311,-9.175177,-1.632859,-3.959879,-3.225741,4.090693,-8.469857,-7.401886,5.763261,-3.383928,-4.069150,9.928114,6.387490,7.825982,-0.162878,-7.837493,-2.643696,-6.441786,1.883869,5.339575,-9.335979,1.439930,-9.219721,1.115520,-8.398343,2.586669,7.707869,3.017269,1.373860,7.138967,3.206462,-5.811115,-1.386789,-0.017005,7.440132,6.563793,-3.736281,-2.111854,-8.233946,-0.177081,6.179039,-1.842948,7.896141,4.690049,-8.844130,-5.204684,2.962537,-9.801124,-6.877430,1.672606,-9.201403,3.516738,7.303845,3.431127,9.260599,-2.030440,9.136412,0.684718,-7.315949,-0.755483,1.246141,-1.197634,3.030374,-7.820571,2.546027,7.523117,9.920439,8.708426,-4.464339,-2.043111,-6.806139,-8.961322,2.316617,-7.722307,5.695037,9.942040,-3.945612,4.272043,-7.896537,4.215286,3.745784,8.797239,5.509409,8.406334,-5.902154,4.714097,-3.673432,-5.469038,4.221998,3.100114,2.478357,-1.442131,0.339937,1.900281,7.721323,6.194885,6.423727,5.143090,7.080132,-2.153446,2.532596,1.847533,-4.567939,2.329108,-9.767112,-6.869280,8.973055,3.018754,-5.879765,-2.704926,3.230387,-5.002966,1.333429,5.826499,-0.254425,-9.076237,3.465053,4.554142,7.099813,-6.949488,9.156954,-0.776901,0.719075,6.439715,-7.244075,8.573118,-9.800278,0.893468,-1.041515,-5.147342,-6.626311,-9.829108,-8.157016,0.933703,-4.463903,-3.209332,-1.062184,3.836753,-5.808248,2.319785,-1.518149,5.312040,-9.785710,-7.670777,5.003157,8.786735,0.141146,-7.296167,2.367355,-3.031168,8.480152,-4.543044,0.199236,0.093011,-9.236886,-1.017160,4.635543,9.977565,-9.093468,-6.122484,0.565188,-2.413937,5.220307,-9.138596,-7.083091,6.575768,5.520780,-4.593309,4.254384,5.616194,-8.874252,-3.436439,0.745667,-7.464942,-7.570862,2.465635,-0.016775,-6.363054,-7.175459,8.523020,3.385999,-0.107113,-4.281136,8.120395,-8.592337,2.933859,4.481992,4.597126,-0.651830,-8.870138,-5.585223,-4.546972,7.902437,1.331156,1.292474,6.763540,6.473671,-6.910252,-3.856253,3.641063,-7.359728,1.696850,-0.391175,-1.607956,-5.127100,6.157628,-8.459740,-5.124229,3.122735,-8.224235,-8.915455,3.808497,3.150598,7.972450,-0.240563,9.160416,8.517057,-7.416378,3.499590,-3.323586,0.210865,-1.339340,1.897790,-0.102419,-0.074297,-1.503069,-1.478930,-8.946485,9.471006,5.345658,-5.635658,-9.113230,8.614627,-6.235542,3.969442,7.023493,-0.371199,-4.656909,-2.886652,-7.530009,6.314176,7.899151,5.641396,-3.194165,3.816138,-2.070374,-2.279203,0.352454,3.825974,-3.599444,8.098555,8.896363,5.718802,3.113787,-8.921334,9.874532,-8.138865,9.435622,-0.591188,-2.572255,8.932730,-8.094308,0.502481,-2.801410,4.428925,4.169467,-7.321593,-2.443159,8.215814,5.517437,-0.154982,5.410656,4.158724,-8.970491,-6.109859,4.927047,9.463813,8.437421,3.857452,3.968420,-5.065833,9.294722,9.600189,6.547089,-8.796857,5.494718,5.555777,3.366053,7.966156,-3.872685,5.529511,-1.125375,8.833452,7.338294,7.277048,4.267915,-2.492782,-6.563130,9.470210,-4.962886,-3.502209,-5.214046,-3.799027,-0.592206,5.977316,-6.864912,-9.998894,2.052447,-5.974993,-0.237672,0.342358,-6.761756,8.627748,0.734790,-6.953557,-0.104269,5.109500,-5.182110,-3.577015,-0.386980,1.790009,-1.096484,6.389252,-0.385045,3.202891,9.983418,-7.486717,-8.184351,-0.742376,-0.245045,7.042630,3.088973,9.084494,-4.134809,-4.019383,3.784005,2.967001,4.963792,9.069905,2.438367,-1.434751,5.454622,-7.087707,-7.118174,-8.466014,6.746667,1.627781,-1.659609,-7.372376,8.819587,1.971538,-9.628427,-7.518021,9.274516,0.010302,-4.162157,9.716313,3.897597,3.716011,-0.174650,-5.868469,3.315160,-5.800966,1.308023,2.438454,3.079324,7.112379,7.388915,0.733678,-9.526124,0.519172,2.668007,-6.479829,-0.936103,-0.834478,4.297823,-7.804517,5.091200,8.333983,3.364803,4.965652,3.081322,5.121950,-6.664588,-6.082968,8.957918,-4.104686,-3.004773,2.113531,-5.175253,-3.878641,3.512440,3.554611,4.749979,1.891351,7.424326,-6.205807,3.305761,2.793484,-6.779257,-4.789214,-3.459104,-1.713255,-5.525034,7.069549,-1.853294,-6.229460,8.370950,-9.247510,-6.994843,0.846698,-5.286897,2.487185,1.868922,1.807216,-0.569789,-8.467581,-8.293618,9.549395,-2.413159,-3.257604,-6.695079,-5.410082,-1.308155,9.352861,-4.204345,-8.122905,-6.260421,5.455989,-9.952925,2.757356,-8.374091,1.179583,2.740154,1.435592,-4.843079,-6.246475,4.218600,-7.135548,1.766717,-4.676586,-4.227542,-7.816747,-2.491970,5.202726,-8.751155,1.835516,-1.137169,-3.170365,-0.383191,6.118742,7.097567,3.978003,4.580621,-9.930616,1.092501,-4.243119,5.071001,-7.839429,-5.535743,-8.444176,6.323636,-0.917774,4.631103,8.925458,-5.328356,-6.961833,-7.022193,-3.677375,6.260617,-2.736504,-9.397613,-1.557080,1.895284,3.388064,-8.416867,-1.149740,-3.323756,4.195899,8.910051,4.187569,-8.744119,3.425757,9.640340,-3.411248,-1.808428,-7.712168,2.360068,-4.209454,6.317365,5.728238,-4.235439,9.288052,-4.098965,-0.374802,2.367167,2.900912,0.844592,-5.573527,8.781019,0.544967,4.194358,-3.039489,-8.591830,1.092298,-2.350052,-7.091314,1.248515,1.683184,-3.052045,4.053531,4.788597,9.573890,-9.310142,-5.623598,-0.236420,1.665248,6.564130,1.439850,0.509677,2.118190,0.983628,-6.156151,-4.703684,-2.216283,6.261666,-9.130628,-1.139393,0.871704,-9.432379,-8.547978,8.260816,-8.380703,9.973607,-8.145637,3.822084,0.494851,3.144087,3.759378,6.666389,2.464678,4.655201,-9.563978,1.734534,-9.681956,9.441905,9.577891,8.686433,3.518561,6.478664,0.176584,6.039592,3.872043,-1.704989,-8.288843,-3.698093,-2.622213,-1.514733,1.172207,-5.830486,4.205783,8.359751,-7.658990,-9.782059,3.581908,1.146219,-2.056909,1.969649,-8.731403,-1.495964,-8.380196,-3.961230,8.048828,7.967618,-5.812245,-3.992042,4.792620,-3.124421,-9.511798,1.954514,-0.563084,-7.274083,9.354344,-1.856175,9.271168,7.920369,2.733877,-1.046692,-2.012684,-5.104350,3.866953,-7.203038,-3.106177,-6.348420,3.765223,-4.310903,7.064103,5.808434,8.155817,-7.199658,-8.100580,-1.663118,5.073275,-9.030468,-8.918080,-5.755804,-6.080629,-7.332843,-2.268541,6.262970,-5.663222,9.109190,4.356118,-3.759759,4.179880,6.737915,-7.870671,7.532014,0.198165,1.751440,-5.665483,3.792208,-4.146446,9.749315,7.335825,5.430867,9.757108,8.397241,6.814163,4.721290,-4.217109,-2.257377,-1.488064,-0.402595,-6.905147,3.301206,5.259232,4.370212,-5.539906,-5.314977,5.694645,8.830835,0.933532,5.598896,-1.130965,5.251769,-4.583627,-8.789990,7.243899,-0.083887,-2.504689,2.472389,-3.925171,-9.519043,5.353470,-1.179254,-3.862590,9.993642,-1.116414,-6.816156,1.809336,3.705732,2.912446,-2.459452,-9.756932,-9.142845,-4.532735,5.703033,-7.775826,8.503765,-7.918300,2.679862,1.020936,-3.070611,4.300813,6.498835,-5.273970,-2.139999,-9.030622,3.062655,5.885771,5.802767,0.649288,6.448383,-3.817832,0.280328,-2.684933,4.556966,-9.747687,-8.571728,-1.063325,-6.059761,-3.191783,0.300107,-1.506162,-4.465607,-3.646575,2.440110,-5.217026,-1.303615,-8.390653,5.656383,-9.935319,-9.202868,6.874486,-6.800108,-4.328584,-6.170069,-9.892534,2.043926,-0.628739,-5.388003,-7.296887,-6.264051,-7.050298,4.676699,3.864343,-5.699156,-0.039676,-7.594782,4.391522,2.124639,4.347995,-3.533303,9.704203,-0.697629,6.034360,6.008132,9.388575,-8.692464,-8.893193,-1.811606,4.486109,5.810691,6.027889,1.884454,-1.034073,6.495880,-1.853880,0.062852,8.070183,-1.141064,6.617433,-1.783892,0.499939,-4.974022,6.152421,8.385976,2.302617,-8.537078,-7.955983,7.417479,-6.190680,5.139265,2.196423,7.301686,-2.961359,4.857345,3.353841,-6.539752,1.369597,-2.411699,3.161327,4.269090,-0.886572,-0.678393,0.074839,3.925866,-4.589085,-0.549486,-0.226658,-0.386789,0.037572,-8.480446,-7.499255,-3.624944,8.243926,-5.284438,-3.282959,-3.559554,8.118903,-8.002582,-1.716310,-3.629956,-3.135070,-3.582641,-0.660027,6.229831,0.127617,-8.990589,0.582879,1.138498,2.942841,2.943640,7.652771,-2.761410,-2.740773,1.047333,3.457883,2.098302,-0.431662,-6.765594,3.306139,6.978796,9.057568,-2.795139,-0.293670,8.482108,4.352599,3.316379,-3.985806,0.091261,-5.309187,-5.132812,-3.006329,0.622532,5.713693,-0.953043,-1.017478,0.918737,7.840829,-3.839259,2.397787,-1.289153,-9.316993,3.341133,2.431305,-0.173356,9.528347,7.520256,-8.047772,0.845223,-7.975285,-5.344891,9.954598,-2.798919,7.199647,-0.112979,1.191950,8.240723,-2.639275,-7.206181,7.935797,-5.694806,1.421638,7.520258,-3.282485,-4.836566,-1.296417,6.187078,-2.461212,-2.722664,-7.081213,6.187337,1.275615,-3.827611,0.770893,-4.104718,4.297531,-5.675504,-3.416488,-5.634048,-3.045094,-8.807484,-5.309143,-4.013153,5.954304,-6.085487,8.016199,9.998374,1.645045,-5.933294,2.179905,9.287426,3.603639,7.780819,4.704758,1.998719,-3.583321,-2.787550,4.920247,-1.524434,-3.837091,4.722273,-3.572766,-7.938599,-8.933056,-1.218338,6.706786,-8.499974,0.286757,4.867748,2.064099,-8.217785,-2.202886,-2.818637,6.471293,-3.987423,-1.611007,5.163784,5.715302,-1.077406,3.086954,4.122697,-0.098184,1.558013,7.832368,2.649079,2.996030,1.344012,-5.319575,-2.832749,-7.004596,3.348770,-7.207386,4.416130,1.848062,8.028163,-6.455080,1.286453,-6.975606,5.675783,5.269298,-6.328603,-5.808179,-1.463765,-1.782710,2.871010,-0.201170,2.531622,3.943487,-7.356401,-7.652790,3.643892,-3.545219,2.601442,-6.755114,-6.951600,9.064960,-2.984327,-3.847610,4.768522,6.549628,8.613667,6.888032,-1.599249,2.733045,5.895374,-1.105630,7.556563,-6.519251,7.705533,1.727386,-7.440089,0.773940,-4.676088,-8.642585,-7.655780,-8.481364,0.503778,-8.637138,8.052431,-9.552167,2.065537,4.436169,3.719873,1.461701,-0.288373,-7.952522,-9.358223,-1.966267,-6.579939,-5.771880,-4.092143,-2.405710,-4.941620,-5.635407,2.023632,1.945634,6.760909,0.421458,-0.488379,-3.188024,4.097988,9.188586,-1.274165,-8.496982,-9.058589,4.619889,-5.048384,-0.041288,-7.437425,-1.908970,5.897099,-4.630682,-9.562266,7.179023,-4.488120,-1.350048,8.917655,3.778622,4.621408,-7.807255,-8.098470,-5.165145,0.159274,-9.861936,6.206731,7.408192,-9.434536,-2.138392,7.594953,7.171902,0.015708,3.159905,6.223810,-7.128403,4.990530,8.648640,-8.001594,-4.906082,-6.852136,9.923519,9.687743,6.987496,-0.933532,-9.464840,3.569644,0.580201,7.527477,5.502888,-0.331506,4.669628,-1.815525,1.516592,8.704975,8.644371,-2.689439,7.949044,8.593294,5.263812,-5.792063,-4.447384,7.152526,-3.974335,-3.924451,-9.810025,3.447880,-5.452055,-6.492348,-6.436141,9.897393,7.480951,-8.413068,3.556798,9.262180,6.196166,0.712856,-7.215813,-8.316916,2.607099,-0.949735,5.304494,-1.467460,-0.007459,4.071755,-4.634713,-7.600130,8.879368,-9.375630,-5.801216,3.053481,-8.626527,3.961004,-8.240612,7.784826,1.324275,8.596395,-5.548149,-3.878718,-3.084729,3.834833,4.987922,-6.412411,3.742999,3.926159,1.283836,8.023936,3.434401,-7.927229,-8.024681,-7.426637,9.391280,-2.811457,7.614781,-8.972185,7.402890,-5.704888,7.784277,9.098521,4.294000,0.144623,4.854083,-4.289230,9.919139,-8.559391,2.237168,0.309596,-9.667422,-7.662251,4.088832,9.089175,-1.188500,0.795760,0.269663,-7.091241,1.750463,4.864080,5.426971,-6.670564,-4.471245,-4.185449,0.770402,-1.751226,-5.624753,2.729847,-4.080333,-4.960910,-7.009194,-0.837188,-2.139649,-0.783866,-6.720848,-6.712559,-4.299039,0.104028,-7.321012,-4.806888,8.881047,6.644491,5.607001,1.891348,-9.527679,-1.296603,6.627954,-9.661425,-0.797131,-9.208589,-2.734389,-9.681672,5.626221,8.275268,6.128110,6.182165,-6.105567,-7.973483,9.549022,6.811100,1.411579,-3.660633,7.781140,-1.461953,8.585347,-3.642631,-5.084478,-2.305181,-8.365808,6.683866,9.373578,6.116870,8.829894,9.979968,0.224198,-7.450757,1.530582,-1.421545,7.347951,-1.684182,3.309245,-1.481717,7.547056,5.220035,-4.675502,4.825338,4.484285,-1.310438,3.822451,8.343223,-5.408585,8.764274,-2.443906,-4.707977,3.891935,-7.970860,-1.913595,-2.662169,-2.950246,9.306800,-8.014256,-9.992316,8.275193,-2.425093,6.631895,-9.900890,-2.256390,9.666453,4.138832,-8.627363,-2.790019,4.572908,-8.555832,-1.908912,9.708843,6.881668,-7.158264,7.787853,-7.121035,-8.320792,2.023954,-9.904632,5.843328,-5.677008,4.426419,1.123918,1.436535,-9.836569,-1.497501,-7.671757,3.892090,5.582179,-9.642064,9.036850,-4.208769,-5.411892,-2.815834,4.457269,-5.636802,-6.543251,2.048901,9.736493,-4.904393,-4.307460,-5.563507,-4.803561,-7.264337,8.567028,-0.528664,-6.124096,4.258322,-5.790210,7.770502,3.131345,8.230460,0.796523,2.555957,-7.347207,1.839197,-4.941786,3.209369,7.066037,-6.921795,-0.900224,9.958505,9.020606,2.778768,9.770899,-3.098748,-5.910678,-4.417502,-5.566040,-4.647063,-0.077771,0.934871,1.052199,5.907027,-7.720078,-4.682378,6.550434,8.350502,-4.866816,-6.995986,3.838313,-1.322104,2.137051,-2.980372,-2.200195,-6.496396,-4.929767,2.216246,-6.680133,-7.247324,-0.497269,-2.104873,-0.582994,-0.068192,-6.342145,-4.564293,8.693022,-3.438622,-5.502021,-3.797822,9.353679,6.267428,-0.656413,-4.651216,5.208310,-0.816912,6.191224,2.170327,-1.008676,-4.738757,0.142679,5.834849,5.093662,4.036760,-6.838462,-3.087675,-6.621789,5.117974,-2.668805,9.949007,-2.773508,8.493137,-2.452782,4.710758,-7.194045,-9.729168,5.450386,6.527538,7.285899,-6.142105,-2.467265,9.793294,-0.157946,-1.486888,-3.792274,-5.631605,0.847603,-7.448784,4.248883,-2.509519,1.704897,9.354548,-6.448343,5.311823], dtype = "float64")#candidate|4763|(1365,)|const|float64
const_4764 = relay.const(-3, dtype = "int64")#candidate|4764|()|const|int64
var_4765 = relay.var("var_4765", dtype = "float64", shape = (770,))#candidate|4765|(770,)|var|float64
const_4766 = relay.const([[-5,7,5,1,-2,5,5,2,-2,1,-2,-7,3,3,3,-5,6,-6,-9,-6,-9,-6,6,-2,-3,-6,-4,-8,-2,10,-8,4,6,-4,8,-7,-1,-1,1,5,-6,8,8,8,-9,-5,-3,9,-10,6,3,5,6,-2,9,2,-10,7,10,-8,-2,-4,-6,6,-7,2,-6,7,2,1,-9,-7,5,9,-9,-4,3,-8,2,3,-4,3,-3,-2,-2,-6,-7,-1,9,10,10,9,-2,2,-8,-5,-1,2,9,-1,-6,1,2,-8,6,10,-1,-9,5,7,6,8,8,-3,4,9,3,-5,-4,7,-2,7,-6,-6,-8,6,3,-3,-2,2,-10,-7,-1,-7,7,6,-3,-3,-1,-9,2,-5,7,-9,-4,-6,10,-7,-8,-7,-10,-8,-5,-1,-10,7,8,-6,-10,6,6,10,7,-6,-4,4,5,7,3,-8,10,4,7,-3,-6,1,-2,7,-8,6,7,8,-2,-4,4,-7,-7,-4,-2,1,5,2,-3,-7,-4,-5,-3,-3,-9,-9,8,9,6,2,-10,9,-5,5,10,2,-4,-6,-1,3,5,3,9,-1,-5,4,5,3,4,1,9,-1,10,4,-6,9,1,7,6,-5,-2,-10,-4,-9,10,-4,3,4,3,-3,4,-2,-6,5,8,6,-8,-9,9,1,-7,-10,2,-4,-1,2,10,10,-5,-9,4,-3,4,-5,9,4,-4,-8,8,9,-8,-5,-7,4,10,4,-1,-8,-8,-9,10,-5,-10,1,5,-7,3,9,7,-1,-9,2,-2,6,-5,9,10,10,-8,-8,-2,-6,-7,4,-10,-2,10,8,6,3,1,-7,-5,3,-9,-6,7,6,9,-9,-7,-8,7,-2,-2,-4,-7,5,1,7,10,3,-5,3,-10,-5,-3,5,-10,3,-10,-6,10,-10,9,1,1,9,2,2,-4,9,9,-7,9,-3,-7,-9,-10,5,6,-3,9,-3,-5,3,3,9,5,2,-4,-6,-6,7,2,9,8,-5,3,-8,-6,-10,-10,-10,4,9,-1,-10,-10,4,9,-9,5,-3,-3,-7,-9,-7,-5,-6,-1,9,-9,-10,6,-10,9,-1,5,-3,7,9,-8,-7,-5,3,7,9,-1,-7,-3,1,8,4,-7,4,-8,8,-1,-10,7,2,7,9,10,-4,-3,-5,-6,4,8,5,-1,4,1,8,-1,-9,-2,6,-6,-7,7,10,10,7,2,-6,9,4,-5,-6,-5,-5,-7,10,-3,-2,8,-4,-8,8,4,-2,5,-3,-10,-5,5,-3,10,8,2,-6,2,9,-10,9,-3,9,8,-8,-10,-5,-4,-9,-4,10,7,-6,-5,-10,-4,-10,-1,-6,-10,9,-9,7,5,-10,5,4,-7,4,5,-6,4,-7,7,-3,-8,-7,9,10,1,4,1,7,-8,9,-6,2,3,2,3,-6,-10,-7,4,2,1,-1,-3,8,1,7,-4,-5,10,-6,-7,-5,-3,5,-4,-5,4,-5,6,2,-3,-5,10,4,9,5,2,2,-2,5,5,-9,5,8,9,9,7,-9,-5,-8,-2,-10,-1,-10,-9,-1,4,-3,-5,-10,-9,8,-4,4,9,4,5,4,6,10,-6,10,-2,10,-2,-2,1,8,9,5,-5,7,-4,-3,4,8,6,-1,10,4,2,-6,9,10,-7,-4,-5,10,2,2,9,-8,-9,-1,-8,3,-4,5,-3,9,-2,-10,-4,8,4,-3,-1,9,-8,9,7,8,-10,-5,7,-1,-7,-6,1,-6,-6,-9,-10,7,9,3,-7,-9,1,-8,-6,-7,-9,-5,-7,-9,-1,-1,9,6,1,5,-10,3,-6,10,-1,6,-10,-2,3,-1,2,-3,8,-8,-9,-9,7,10,4,-7,9,-4,-6,5,10,4,-7,-2,6,-8,-2,4,10,3,6,-10,7,3,2,3,-5,3,-3,1,-4,-4,7,-6,-4,2,10,4,-5,1,6,-1,-2,-4,-9,2,-3,10,4,6,6,5,-1,-5,7,-6,-1,-3,1,-6,10,4,4,-3,3,-4,9,-6,2,7,-9,-2,9,-3,-1,-1,-9,-4,2,-1,9,3,-7,-8,-10,8,-7,-10,-4,-7,4,-7,4,7,-1,8,-2,-9,9,7,2,1,-6,6,-5,-6,-2,3,-6,-1,-9,-8,1,1,3,-1,3,-4,2,8,4,10,9,-1,4,-2,4,-3,9,7,1,-9,-2,5,3,-5,9,3,9,-3,-8,7,6,9,5,7,7,-2,9,5,3,8,-3,10,-7,-6,-9,-8,-2,-10,6,5,-5,2,-6,-7,7,3,-8,-4,7,1,1,-2,-8,-2,-2,-10,5,3,1,4,-7,7,-1,2,1,5,5,-6,10,9,-6,10,-1,7,-5,9,8,-9,9,9,7,3,-3,-6,9,-8,-6,-10,-3,10,-8,4,-7,6,-6,-7,1,8,-10,-1,-2,6,7,-7,-5,-10,6,-8,9,-10,-9,10,6,5,2,5,-3,4,-8,-2,-7,-5,-6,-5,-7,10,1,-5,9,3,6,-7,-10,10,-3,-3,5,-3,-3,6,5,-5,7,5,1,-9,-5,-7,9,-3,2,-3,5,7,-6,5,10,-10,-1,-5,3,9,-10,1,8,10,-1,6,-10,-2,-6,10,9,3,6,-2,9,7,10,9,-3,7,-3,-7,-5,-9,-8,-7,10,-6,-9,3,10,9,9,9,8,-3,-10,-6,-9,-8,-4,3,6,-8,6,2,5,-7,1,4,3,-2,8,-7,-5,-4,-9,-2,-6,9,6,-7,5,3,9,5,7,-4,7,3,-8,10,-4,4,5,-2,-7,1,-3,7,-4,-4,4,-5,1,5,-5,-9,-9,10,8,-4,1,8,2,5,-10,6,-9,6,-8,-3,6,-3,7,-9,-5,2,10,1,-5,-7,-7,10,-5,10,-7,-6,7,8,-3,10,9,6,-2,-1,-5,-4,3,-2,2,10,7,2,5,7,-4,8,7,-3,2,7,-4,4,7,-6,10,-8,-1,-10,-8,-4,1,8,-5,10,6,-7,-8,-8,8,6,9,4,2,-8,-10,5,-4,3,5,-1,1,-3,-10,6,6,-6,5,7,-6,8,-7,1,-9,5,10,-6,3,-1,-4,-10,10,7,8,1,-9,3,-5,9,1,-7,-9,1,6,-4,-1,-1,10,4,-2,-5,-7,6,5,5,1,-8,-7,-4,-2,-3,3,-2,10,5,3,2,8,-4,-7,-8,1,9,-4,-2,1,9,-9,-9,9,2,3,3,-4,-4,-6,-9,8,-8,3,9,7,-10,-1,7,2,-3,5,-6,-3,-2,-3,-5,-3,3,2,1,-2,-6,-1,-2,-4,8,10,-8,4,-1,3,8,-10,-1,3,-4,3,5,-4,-7,-1,-8,10,-2,-8,-3,-1,-6,-2,-3,-8,-9,6,-7,2,-1,-10,3,-4,8,8,-4,2,9,-8,-10,-9,9,4,8,-1,-8,7,-3,-6,5,-2,-4,1,-10,-8,-5,-9,4,4,9],[10,-4,-1,-8,-8,3,-1,4,-2,1,5,7,-2,-7,-3,-10,6,-10,5,-1,10,-2,-5,-3,3,9,9,1,-6,-8,7,-4,5,7,3,-2,-4,-5,3,5,9,-3,9,2,4,-8,1,3,9,8,8,6,4,-2,-9,-2,-1,9,-3,-9,2,-10,-1,-8,3,-4,-6,2,2,-9,-10,-9,10,-5,8,1,-3,-2,-6,-7,-8,7,-3,-6,-4,6,-5,-7,5,-7,-5,-5,-1,-3,9,3,2,3,-2,10,3,-2,-1,3,-10,-10,-1,3,2,-9,9,10,6,7,-10,4,1,2,-2,9,-9,8,4,2,-1,-10,-6,10,-2,8,1,7,-7,-5,6,-2,5,-5,-3,-6,1,-3,-6,7,-9,2,-8,-6,-8,3,-7,8,-4,2,1,10,-3,7,5,7,-10,7,-8,10,-6,-1,-7,-6,4,-6,5,7,8,-9,-7,-10,7,-4,10,2,-6,-10,4,3,3,2,-5,10,-2,-8,-7,-7,-6,9,4,4,6,4,10,-7,7,3,-8,-7,1,-9,-4,1,7,5,-3,5,3,-9,-7,5,6,7,-10,4,2,8,-2,-7,10,2,1,5,7,6,-10,9,1,-2,2,2,1,-9,2,-2,8,-8,-1,4,4,-1,4,-2,6,8,10,-2,-2,4,7,-8,9,-7,-6,-6,2,7,-7,-3,-1,-3,-10,1,-7,10,10,10,-2,8,9,-10,-1,-9,6,-3,2,9,10,8,5,-3,5,-4,2,5,-8,-2,-4,9,-4,10,-8,-2,8,-8,-9,10,6,-1,8,10,2,4,5,-9,-4,9,-7,4,2,-8,3,-4,-4,7,-10,-7,-9,2,2,4,-10,10,3,-1,-8,-7,1,-9,-6,-6,-3,9,-3,5,2,-3,-2,8,-9,-2,1,7,1,-8,2,3,8,7,-3,-7,2,7,-5,1,7,-10,-7,10,-4,-4,2,-4,-1,4,-3,-1,2,-1,5,2,9,10,-2,-3,1,-3,-5,5,-7,-10,-9,7,10,-10,-2,-7,-8,-7,1,7,7,5,8,-10,9,7,-2,1,4,7,8,7,4,6,-3,-5,4,2,2,-9,1,-2,2,-5,7,-10,-7,-2,-2,6,3,4,3,-1,8,-7,8,4,-5,6,-10,-8,7,7,8,3,-5,1,4,5,4,3,-3,3,5,-9,-8,-3,7,-2,-5,8,-3,10,-3,-9,6,8,-10,-7,-10,1,3,3,-6,-5,-2,-1,-2,-2,5,-1,-7,2,9,4,6,-7,1,-7,9,-8,-4,7,1,2,-3,10,-9,-9,2,8,-9,6,-9,7,-4,-10,-3,8,-6,-1,-3,-1,3,-3,-3,2,-7,2,-1,5,-3,8,2,1,6,1,2,2,-1,-8,-7,6,1,2,-8,-9,-2,8,-3,-3,10,-8,5,-8,6,-1,-8,-7,-5,-1,5,-6,9,10,3,-2,-9,-7,-2,-1,3,-1,8,-10,-8,8,2,-10,-7,4,-6,-5,5,-1,1,7,-3,4,8,-6,6,-10,7,-1,10,4,-10,-3,3,5,-6,-7,-1,-2,-5,-7,-4,1,-7,-4,10,7,9,6,-3,-5,3,10,2,-5,4,-10,-9,10,5,-4,-3,6,8,3,5,2,1,2,-8,2,8,-10,3,2,-7,-5,-5,4,3,9,-9,-5,-5,-6,5,4,-10,-10,-8,2,-7,8,8,-9,1,-10,-9,9,-4,-8,2,10,-10,-4,-3,4,3,-5,-3,-3,-2,-3,10,8,10,2,-10,4,5,8,4,7,5,-2,6,-5,10,1,3,-5,5,-2,2,-5,-4,4,-9,9,4,-4,-7,-9,6,-1,7,-1,5,-5,9,-5,-7,5,1,9,5,6,-2,-1,2,9,-9,-2,-4,-3,-1,10,-7,-1,8,6,5,7,6,6,-1,-9,-7,-5,10,-6,4,8,-10,4,10,1,-1,-3,-8,4,5,-8,-6,3,-10,-6,4,10,4,-2,-1,2,-1,8,3,9,-5,2,1,-9,4,-7,-1,2,8,-10,9,2,6,-1,2,-10,-8,-10,10,10,-5,4,-6,9,-2,-5,-2,1,7,-10,-2,5,3,-9,-3,6,-7,-3,-9,-9,5,2,-10,-7,4,3,-8,-8,-4,-3,-5,6,-1,7,1,-1,-9,-4,-5,-6,-10,7,-7,-8,-1,7,-4,-1,2,-7,5,1,-10,-3,-8,5,5,-6,8,-3,-9,-8,5,-7,7,-2,-1,-6,-10,7,-7,-7,-6,-7,9,5,4,10,-3,6,3,4,-3,-5,9,-2,-6,-1,2,-7,1,10,7,3,-8,-2,1,5,6,8,3,4,-8,2,-6,-2,4,2,-1,3,-6,-10,-1,-2,6,4,9,-1,-6,9,-3,-1,-3,8,8,5,8,-10,10,-8,1,10,-4,10,-5,4,-2,-4,-7,-10,6,10,9,-3,-1,9,-4,5,1,10,4,3,10,-10,-2,4,4,-1,4,-5,-4,-9,3,-8,9,2,1,-9,5,-10,2,4,-7,-10,-1,-6,-7,-5,10,9,-9,-3,6,-1,-3,-7,-4,10,8,-10,5,3,-2,-6,-10,-2,-4,9,-8,1,1,8,-1,-5,-10,-5,3,-7,-4,5,-8,3,1,1,4,3,-2,-9,1,9,10,-4,-1,6,-6,1,10,-5,6,2,-2,5,8,-6,-9,8,-2,-10,7,-8,9,-6,-3,-9,1,-1,8,6,2,-5,-10,8,-9,-4,-4,-9,4,-1,-8,-10,-4,1,-8,10,-10,9,-1,-1,3,5,10,2,9,10,4,6,10,-9,-4,-6,-3,-4,2,-5,1,-4,-5,-4,10,2,4,1,3,4,-9,2,7,-8,-1,6,4,4,8,4,4,1,3,-3,4,-4,10,-8,-1,-4,1,8,-9,3,-10,5,-2,-1,-2,3,-4,2,-4,8,9,2,3,-5,10,-2,-6,6,7,5,4,7,7,-3,-2,-6,5,2,8,4,9,10,-5,5,6,3,-10,-9,2,5,2,-6,1,-9,-7,-7,-7,2,-5,-5,-9,-10,-9,-3,10,-4,1,-1,9,-1,3,5,-9,3,3,3,-4,-10,-4,5,-1,8,10,6,9,10,-7,1,1,10,-2,8,7,-1,1,5,-7,-3,2,8,7,5,-2,-2,2,1,-6,-4,-8,-4,-2,-10,3,6,3,1,4,5,-4,-3,8,4,4,5,-2,-1,-1,3,-4,-1,5,-6,10,6,-6,-2,-10,8,-4,-6,-3,3,5,10,-7,6,-3,-2,4,6,-5,-6,-7,-1,-7,-9,1,6,10,-9,7,10,10,2,9,5,8,-1,6,-6,-6,-5,9,-6,7,7,-1,-3,-10,-4,-5,-5,10,8,7,-1,10,-3,-9,-9,4,-2,6,5,-2,-9,10,10,9,8,-5,-10,-6,6,-1,4,5,-10,3,9,6,2,1,8,1,7,-6,1,-9,9,-3,5,1,9,3,-9,5,5,-5,-5,8,4]], dtype = "uint16")#candidate|4766|(2, 1320)|const|uint16
var_4767 = relay.var("var_4767", dtype = "int64", shape = (1, 96))#candidate|4767|(1, 96)|var|int64
call_4762 = relay.TupleGetItem(func_3398_call(relay.reshape(const_4763.astype('float64'), [7, 15, 13]), relay.reshape(const_4764.astype('int64'), []), relay.reshape(var_4765.astype('float64'), [770,]), relay.reshape(const_4766.astype('uint16'), [2640,]), relay.reshape(var_4767.astype('int64'), [96,]), ), 5)
call_4768 = relay.TupleGetItem(func_3405_call(relay.reshape(const_4763.astype('float64'), [7, 15, 13]), relay.reshape(const_4764.astype('int64'), []), relay.reshape(var_4765.astype('float64'), [770,]), relay.reshape(const_4766.astype('uint16'), [2640,]), relay.reshape(var_4767.astype('int64'), [96,]), ), 5)
func_3571_call = mod.get_global_var('func_3571')
func_3576_call = mutated_mod.get_global_var('func_3576')
var_4771 = relay.var("var_4771", dtype = "bool", shape = (1620,))#candidate|4771|(1620,)|var|bool
call_4770 = relay.TupleGetItem(func_3571_call(relay.reshape(const_4764.astype('bool'), []), relay.reshape(var_4771.astype('bool'), [12, 9, 15]), relay.reshape(var_4771.astype('bool'), [12, 9, 15]), relay.reshape(var_4771.astype('float32'), [12, 9, 15]), ), 2)
call_4772 = relay.TupleGetItem(func_3576_call(relay.reshape(const_4764.astype('bool'), []), relay.reshape(var_4771.astype('bool'), [12, 9, 15]), relay.reshape(var_4771.astype('bool'), [12, 9, 15]), relay.reshape(var_4771.astype('float32'), [12, 9, 15]), ), 2)
output = relay.Tuple([call_4743,call_4762,const_4763,const_4764,var_4765,const_4766,var_4767,call_4770,var_4771,])
output2 = relay.Tuple([call_4744,call_4768,const_4763,const_4764,var_4765,const_4766,var_4767,call_4772,var_4771,])
func_4786 = relay.Function([var_4765,var_4767,var_4771,], output)
mod['func_4786'] = func_4786
mod = relay.transform.InferType()(mod)
var_4787 = relay.var("var_4787", dtype = "float64", shape = (770,))#candidate|4787|(770,)|var|float64
var_4788 = relay.var("var_4788", dtype = "int64", shape = (1, 96))#candidate|4788|(1, 96)|var|int64
var_4789 = relay.var("var_4789", dtype = "bool", shape = (1620,))#candidate|4789|(1620,)|var|bool
output = func_4786(var_4787,var_4788,var_4789,)
func_4790 = relay.Function([var_4787,var_4788,var_4789,], output)
mutated_mod['func_4790'] = func_4790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1304_call = mod.get_global_var('func_1304')
func_1306_call = mutated_mod.get_global_var('func_1306')
call_4808 = relay.TupleGetItem(func_1304_call(), 0)
call_4809 = relay.TupleGetItem(func_1306_call(), 0)
output = relay.Tuple([call_4808,])
output2 = relay.Tuple([call_4809,])
func_4824 = relay.Function([], output)
mod['func_4824'] = func_4824
mod = relay.transform.InferType()(mod)
mutated_mod['func_4824'] = func_4824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4824_call = mutated_mod.get_global_var('func_4824')
call_4825 = func_4824_call()
output = call_4825
func_4826 = relay.Function([], output)
mutated_mod['func_4826'] = func_4826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2558_call = mod.get_global_var('func_2558')
func_2560_call = mutated_mod.get_global_var('func_2560')
call_4834 = relay.TupleGetItem(func_2558_call(), 0)
call_4835 = relay.TupleGetItem(func_2560_call(), 0)
output = call_4834
output2 = call_4835
func_4858 = relay.Function([], output)
mod['func_4858'] = func_4858
mod = relay.transform.InferType()(mod)
output = func_4858()
func_4859 = relay.Function([], output)
mutated_mod['func_4859'] = func_4859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_810_call = mod.get_global_var('func_810')
func_812_call = mutated_mod.get_global_var('func_812')
call_4902 = func_810_call()
call_4903 = func_810_call()
output = call_4902
output2 = call_4903
func_4907 = relay.Function([], output)
mod['func_4907'] = func_4907
mod = relay.transform.InferType()(mod)
output = func_4907()
func_4908 = relay.Function([], output)
mutated_mod['func_4908'] = func_4908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2003_call = mod.get_global_var('func_2003')
func_2005_call = mutated_mod.get_global_var('func_2005')
call_4922 = relay.TupleGetItem(func_2003_call(), 0)
call_4923 = relay.TupleGetItem(func_2005_call(), 0)
func_3398_call = mod.get_global_var('func_3398')
func_3405_call = mutated_mod.get_global_var('func_3405')
var_4925 = relay.var("var_4925", dtype = "float64", shape = (1365,))#candidate|4925|(1365,)|var|float64
var_4926 = relay.var("var_4926", dtype = "int64", shape = ())#candidate|4926|()|var|int64
var_4927 = relay.var("var_4927", dtype = "float64", shape = (770,))#candidate|4927|(770,)|var|float64
const_4928 = relay.const([2,-10,-7,-10,1,-10,-4,-3,-9,10,-6,-10,2,8,-7,-2,6,-9,10,-2,1,6,-2,-10,1,9,-1,-8,1,8,3,-9,3,-10,9,-6,5,6,10,10,-5,9,-10,-8,-7,8,-8,8,7,6,1,-8,3,4,7,-7,3,-10,-6,-3,-7,-10,-10,-8,-6,4,-6,4,4,5,1,6,7,-8,-4,-6,4,8,4,-10,10,-8,6,-8,-1,2,4,-8,3,3,-9,-10,5,-6,4,1,-1,2,2,-8,4,7,-9,6,2,-1,10,-3,-9,-6,-4,9,-6,3,-3,-3,2,-5,-6,4,2,-9,9,9,-1,-3,2,10,-4,-5,5,-6,-7,-7,1,3,7,8,-3,5,2,7,-7,9,2,-10,2,-4,-4,4,-10,-1,-6,-4,5,-3,7,-10,-10,8,5,-9,-4,5,-3,5,5,-2,-2,2,-8,-4,-6,1,-3,8,-7,-4,9,8,8,7,9,6,8,9,-2,10,5,-2,10,-6,-8,-5,10,10,9,3,7,-9,5,10,1,5,-1,6,-8,6,3,-4,-9,2,2,-7,-5,3,-6,-9,-4,5,-3,7,-3,1,8,-8,-2,6,6,-2,-2,2,9,-5,8,-10,-10,6,10,9,3,-5,-10,8,4,8,6,-4,-1,-1,10,10,6,5,-3,6,-4,8,3,1,-7,-5,-8,1,-9,-10,2,9,8,-6,10,7,-2,-7,3,4,8,-5,8,8,6,6,-10,6,1,-10,-3,-5,2,-1,4,6,-5,-8,7,-2,-6,1,-5,7,-8,-1,2,7,9,-2,3,3,-9,1,-1,-8,-3,-4,-5,-8,-5,-3,2,2,8,-4,-2,-9,2,-6,4,9,-1,6,3,9,1,-7,-4,6,-5,-2,-1,-7,-2,-5,6,-2,6,-5,9,9,7,-5,-8,-4,-3,-9,7,7,-10,-4,6,-5,3,3,3,-4,-9,3,1,-10,4,-1,7,2,10,-8,-3,1,3,10,8,-8,4,-6,-1,-1,6,-9,8,2,9,-8,-3,8,5,-3,5,-3,7,4,-4,4,-7,-2,-6,4,-6,-8,3,4,8,-4,1,2,5,-5,-10,-8,3,3,8,-7,-2,-3,2,7,-7,3,-8,-3,10,1,-6,-9,1,-10,-9,-3,-3,8,-6,-5,3,8,-10,4,8,10,-6,-6,-10,8,-5,-10,9,-4,-10,9,-7,-7,-9,-7,-8,-2,-7,-3,-5,4,-6,-6,2,-2,-9,8,-8,-2,-7,6,7,2,-6,-9,-10,3,-9,10,1,4,3,-5,-6,-7,-8,-10,1,-9,9,-10,-2,4,3,3,-6,-1,8,7,5,-8,-9,5,2,-8,1,1,-10,7,9,-7,-4,1,6,-7,-3,1,-3,1,2,8,7,9,4,-3,3,-5,8,-10,-5,-5,-1,-2,7,-2,3,4,-9,9,8,-6,4,1,-9,-8,9,-5,-2,-7,-10,-7,8,5,4,-3,-8,5,-2,3,7,-8,-5,-9,9,5,4,2,-3,3,1,-2,-7,-10,-3,-2,2,-9,2,3,1,-1,-10,-10,10,-2,1,1,-9,9,-1,2,-3,-10,8,-8,-1,-5,4,4,1,6,-10,-10,-5,2,-9,1,7,1,-5,4,10,7,-7,7,-6,7,-9,4,-5,-1,-3,10,-4,-3,8,4,-7,1,1,1,2,-3,7,6,-6,-8,-1,-6,9,-5,7,6,-10,9,4,9,9,8,9,-10,3,3,8,1,9,4,-7,1,7,1,1,7,1,-8,1,7,-7,10,-10,-3,-10,8,-7,-7,10,-6,-7,2,10,10,7,-7,-8,2,-9,10,1,-7,6,3,-1,6,3,5,8,-7,5,-1,-1,2,7,-1,9,-9,3,10,2,-1,-5,-10,-4,-10,-1,1,-6,-3,-4,-3,2,7,-3,-7,-6,-2,7,-4,1,7,8,5,10,7,2,-8,-2,-8,-5,-10,7,9,-7,2,-10,-1,8,2,-4,5,-9,-10,9,5,-7,2,10,6,8,-5,-1,-7,-2,1,8,-4,9,9,4,-2,3,-4,7,10,2,-4,-2,5,9,-2,2,-7,9,-8,2,-5,4,-9,1,-8,7,-9,-4,2,8,2,7,-10,-7,-1,-8,5,-8,-5,-6,-4,-7,-1,-5,4,-7,5,10,-2,6,6,-2,10,-9,-8,9,9,7,9,-3,7,-1,-5,2,8,5,-5,-6,6,1,-10,8,-8,-9,6,10,-5,-10,4,10,-9,7,-3,-1,10,-2,4,-2,-4,-9,-5,6,4,10,5,3,8,-9,4,-7,2,7,-1,10,1,6,2,8,7,5,10,7,7,9,10,8,-7,-9,7,4,9,-6,1,7,1,-1,10,-1,7,-10,5,-8,6,-1,-7,1,-2,-6,-8,-2,-7,-2,-2,-5,4,-4,5,1,9,4,-4,1,3,-2,4,-2,8,9,-8,9,-2,-10,4,10,-3,9,-1,-7,2,5,-5,7,2,3,10,1,4,-1,-5,4,-5,-7,-5,-1,6,-3,5,-6,5,7,1,9,9,6,1,2,-2,4,-5,-6,-3,4,6,4,-9,-9,7,10,10,-10,5,-10,-10,6,-1,6,9,3,10,-9,6,-3,-7,-1,-8,-1,2,2,6,-7,10,5,3,-7,5,4,-5,6,-2,3,7,-3,-5,-1,4,-10,-1,-4,-10,9,-8,-7,-2,6,-10,-3,3,6,-2,-1,-2,1,-5,-8,-5,-2,-10,5,-2,3,2,-10,4,4,-10,-2,-5,6,5,5,-8,4,-6,7,4,1,-8,2,5,-7,3,7,-2,10,-6,-1,1,-10,6,6,-1,-5,-8,-10,5,9,-9,-7,-1,2,1,-2,9,-1,1,-3,4,1,5,8,1,1,6,-4,-5,4,8,-10,8,-1,9,-1,-4,-7,-6,-10,-2,10,8,-5,-10,1,-5,-6,2,-1,-3,-4,-7,-5,-7,3,-7,9,8,-8,-5,8,-2,2,-4,-5,-7,4,-1,10,-6,-9,-9,8,-2,-8,7,-8,2,1,3,5,-4,-6,1,-4,1,10,10,7,-6,3,-1,-2,-9,1,10,5,-8,-10,-9,6,8,1,-7,3,3,7,-5,9,4,9,9,-8,5,5,-4,5,10,1,-4,1,8,-5,6,8,-7,4,1,2,1,9,2,-9,-9,10,-3,-5,8,8,6,-6,5,7,-3,9,8,-1,-1,3,-9,5,5,-6,10,10,10,-8,-5,10,-6,4,-8,-4,-5,10,3,7,7,-2,-7,-2,-8,1,-5,-3,-9,-5,-2,-5,10,-1,3,3,-3,-7,-7,7,-1,-1,9,-9,3,-5,-7,-3,8,-9,4,-8,-7,5,-6,-1,3,3,-10,-10,8,-9,6,1,-8,4,2,-8,7,-5,8,-9,-10,10,-7,-4,-6,10,-4,7,-3,3,2,-4,-7,-3,-5,-3,-9,6,5,-2,2,4,-5,10,-1,3,6,-6,6,-7,4,-9,-3,8,6,9,-4,-6,6,-6,2,-2,-7,-3,-8,8,-10,-6,2,1,5,-6,4,7,9,-5,-3,1,-7,-6,5,-8,1,-8,-1,-2,8,7,-1,10,-10,-3,3,-6,8,-5,6,-8,1,-1,-2,1,1,3,-4,4,-9,-10,10,-5,8,3,-5,-2,-4,1,5,7,-1,10,3,-3,10,7,9,-10,1,-4,4,-5,8,4,9,1,-4,-7,-6,1,4,-8,7,-4,3,5,2,6,7,3,-3,-5,-7,6,-3,-1,-5,1,-9,2,-1,-1,-8,-4,7,8,4,-9,-6,-4,5,7,6,-4,3,9,3,-8,7,4,9,-3,7,-4,10,3,5,5,-8,-6,-7,4,5,10,3,-5,8,-7,-2,10,-1,9,-3,-7,5,1,-10,-1,6,-8,-5,-3,-1,-8,3,8,2,-2,-2,-5,4,-9,10,9,1,-7,10,-9,-2,5,6,-1,-9,-3,-2,9,6,-10,10,-4,-7,-7,-3,-8,-5,8,6,-10,-2,7,-5,2,4,10,3,5,5,9,-8,10,-1,5,-10,4,9,-10,10,6,3,-10,-9,8,-6,-1,5,-8,-4,6,7,9,-3,-2,10,9,-3,-2,1,-6,9,1,-3,-10,1,4,-8,-6,2,6,-6,-7,-1,9,9,10,7,1,2,8,9,-3,-4,2,7,-8,-2,-1,-4,-8,8,-10,-1,4,2,9,1,-8,1,1,-7,-10,-3,-3,-3,-9,-9,5,-10,5,10,-1,4,-8,-1,-2,9,9,-4,1,3,8,1,-4,-4,-2,3,-7,-5,1,-5,8,6,8,-10,-9,10,-7,-3,-1,9,3,-7,8,-7,-1,5,-6,7,-3,2,-1,1,3,-10,3,8,-5,6,8,-4,6,8,-10,-8,1,-7,4,4,-2,-4,8,-10,-8,6,-2,4,-10,1,-7,-7,9,-5,-1,-10,5,-7,7,-6,4,10,-2,3,7,6,-5,4,-6,-8,-8,-2,-4,8,6,4,-5,7,9,1,-6,-1,9,-4,4,2,2,-7,-2,-6,6,-2,4,-8,1,-10,6,7,-7,-10,5,-3,5,3,-4,10,1,-10,-1,-10,10,7,-1,3,7,7,7,-9,1,-2,1,6,3,-6,6,5,8,-4,-8,5,2,7,5,2,10,-2,7,4,5,4,-8,9,-3,-2,-4,8,10,-5,-5,-2,2,-5,-1,-1,-9,-10,-6,-2,6,1,3,-3,-7,10,7,7,4,-10,-1,5,-8,8,6,10,-5,1,10,-3,-2,1,2,1,-7,5,4,9,-5,-3,-10,2,-5,5,6,-4,-8,-10,-2,10,-3,-9,-3,6,-9,10,3,-5,4,6,6,10,7,-8,-2,10,1,2,-10,-5,-9,-8,-4,3,-1,-10,2,-4,-2,10,9,1,7,-6,-4,-8,4,7,9,10,2,-8,9,-3,-2,-7,1,3,-1,-9,-9,-8,-2,-3,-7,-10,2,-1,-2,4,-9,7,8,2,-8,-4,5,-10,-5,8,7,-10,8,1,-8,-3,7,9,-9,-5,-9,4,1,2,8,-9,-10,7,8,7,3,5,10,-5,2,-6,9,6,3,-7,10,7,2,-5,1,8,-1,-4,-4,10,1,8,5,1,2,10,-3,-1,2,-7,7,9,-8,-1,-3,10,-8,-5,2,10,3,7,8,1,3,2,-3,10,-3,-6,3,-10,4,-3,-3,-2,4,4,-7,-1,-5,2,4,-1,-4,-5,5,-7,3,7,2,4,-9,7,5,8,-1,-10,-6,-1,-2,-9,-4,-5,-6,-2,-2,-6,7,8,-1,4,9,-6,6,5,-6,4,1,-8,2,5,8,-6,5,7,-2,-8,4,4,-3,-8,3,10,1,-9,8,10,7,1,2,8,10,5,-9,-5,-7,-1,7,2,-7,-3,-9,1,9,-8,1,-4,-9,6,-7,-10,6,-5,-1,8,-2,-3,4,-6,7,3,-9,10,8,-6,6,9,5,2,-3,-6,-1,-5,-4,-9,5,8,1,-2,3,-5,-5,-9,-10,-8,1,-9,2,1,-5,6,2,-5,-3,1,-6,5,1,-2,4,4,-6,2,-7,6,3,3,8,-6,5,-7,6,-2,7,-9,-6,10,8,-9,-7,8,-7,-3,10,-5,9,-8,7,3,8,5,-7,-5,9,1,-7,3,-1,-8,-8,-8,9,3,9,-8,-1,10,-9,2,-7,3,-3,9,-3,-5,-3,7,2,-8,9,8,10,-8,3,9,5,5,6,-10,-2,-1,1,-7,-9,5,-2,8,3,2,-5,5,3,-8,5,-10,-4,-1,1,9,4,10,7,7,3,3,10,-10,9,4,7,-10,-4,-7,1,-5,-9,9,2,-5,5,6,7,8,5,1,-7,4,-2,-6,-6,7,7,-3,-2,-7,6,2,-9,-1,-6,6,-3,-5,-3,9,-4,-7,2,2,-6,-1,-2,8,-7,8,3,-5,6,1,-10,9,7,-7,-5,5,9,6,10,5,-4,1,6,-4,-5,-4,-7,1,8,-7,10,-6,7,-10,-5,6,-7,9,-2,-8,1,-4,-4,6,-6,6,-2,-4,-4,8,9,-3,1,-10,6,-10,1,-7,2,10,6,-3,-8,-9,-1,-6,-1,7,-2,2,6,-6,9,-5,-7,-10,-8,-3,-8,-3,-7,9,9,-9,4,10,7,-8,-1,7,5,3,10,4,-6,9,9,3,-6,10,6,-2,5,-9,-3,6,-4,5,-3,-4,-9,6,2,5,-2,8,4,10,7,8,6,2,-1,7,-8,-6,-3,7,2,1,-7,-3,-6,2,4,7,-2,-1,-8,10,9,-4,-6,6,-3,3,6,4,-9,-9,-6,3,5,-4,4,8,-10,6,3,6,-10,9,5,10,-10,8,-5,-6,7,-1,4,4,4,-9,-1,3,6,-7,-5,-6,8,-1,-5,3,-4,4,-6,1,-10,6,-7,-5,1,3,-1,-1,1,1,-8,1,-9,-2,-7,4,3,-1,9,3,-7,7,3,6,1,-3,2,-3,-9,7,-7,-3,10,-1,7,-2,10,2,-9,-9,-6,1,4,-8,-8,1,5,-6,-8,-8,2,-1,9,-4,-2,1,5,5,-6,2,-7,9,-7,-8,3,9,-4,-6,4,3,4,5,8,9,-2,-9,-6,-10,5,-7,2,4,6,2,1,-7,1,-4,-1,-4,6,3,-2,-2,-1,-5,-4,-10,8,-2,9,-4,1,-9,3,-7,-7,-10,3,5,-2,8,9,8,-2,-6,10,-9,-2,-5,-4,-5,-5,9,8,4,6,7,2,5,-6,2,3,-8,4,1,8,-8,-2,2,4,-1,10,8,-1,-3,-3,4,-10,2,-6,1,-10,6,7,1,4,4,8,-5,4,-10,6,-5,-6,8,10,5,-8,10,-9,-1,-3,-8,-6,3,-2,8,-7,-4,-8,5,2,7,-1,7,8,-4,2,3,6,9,9,5,10,8,-2,7,-3,5,-1,-3,-2,-1,10,4,2,-3,1,-8,9,-3,1,8], dtype = "uint16")#candidate|4928|(2640,)|const|uint16
var_4929 = relay.var("var_4929", dtype = "int64", shape = (96,))#candidate|4929|(96,)|var|int64
call_4924 = relay.TupleGetItem(func_3398_call(relay.reshape(var_4925.astype('float64'), [7, 15, 13]), relay.reshape(var_4926.astype('int64'), []), relay.reshape(var_4927.astype('float64'), [770,]), relay.reshape(const_4928.astype('uint16'), [2640,]), relay.reshape(var_4929.astype('int64'), [96,]), ), 8)
call_4930 = relay.TupleGetItem(func_3405_call(relay.reshape(var_4925.astype('float64'), [7, 15, 13]), relay.reshape(var_4926.astype('int64'), []), relay.reshape(var_4927.astype('float64'), [770,]), relay.reshape(const_4928.astype('uint16'), [2640,]), relay.reshape(var_4929.astype('int64'), [96,]), ), 8)
output = relay.Tuple([call_4922,call_4924,var_4925,var_4926,var_4927,const_4928,var_4929,])
output2 = relay.Tuple([call_4923,call_4930,var_4925,var_4926,var_4927,const_4928,var_4929,])
func_4942 = relay.Function([var_4925,var_4926,var_4927,var_4929,], output)
mod['func_4942'] = func_4942
mod = relay.transform.InferType()(mod)
mutated_mod['func_4942'] = func_4942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4942_call = mutated_mod.get_global_var('func_4942')
var_4944 = relay.var("var_4944", dtype = "float64", shape = (1365,))#candidate|4944|(1365,)|var|float64
var_4945 = relay.var("var_4945", dtype = "int64", shape = ())#candidate|4945|()|var|int64
var_4946 = relay.var("var_4946", dtype = "float64", shape = (770,))#candidate|4946|(770,)|var|float64
var_4947 = relay.var("var_4947", dtype = "int64", shape = (96,))#candidate|4947|(96,)|var|int64
call_4943 = func_4942_call(var_4944,var_4945,var_4946,var_4947,)
output = call_4943
func_4948 = relay.Function([var_4944,var_4945,var_4946,var_4947,], output)
mutated_mod['func_4948'] = func_4948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_4963 = relay.TupleGetItem(func_2364_call(), 0)
call_4964 = relay.TupleGetItem(func_2366_call(), 0)
output = relay.Tuple([call_4963,])
output2 = relay.Tuple([call_4964,])
func_4971 = relay.Function([], output)
mod['func_4971'] = func_4971
mod = relay.transform.InferType()(mod)
output = func_4971()
func_4972 = relay.Function([], output)
mutated_mod['func_4972'] = func_4972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_4986 = relay.TupleGetItem(func_1886_call(), 0)
call_4987 = relay.TupleGetItem(func_1888_call(), 0)
func_2097_call = mod.get_global_var('func_2097')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_5026 = func_2097_call()
call_5027 = func_2097_call()
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_5028 = relay.TupleGetItem(func_1393_call(), 0)
call_5029 = relay.TupleGetItem(func_1394_call(), 0)
output = relay.Tuple([call_4986,call_5026,call_5028,])
output2 = relay.Tuple([call_4987,call_5027,call_5029,])
func_5035 = relay.Function([], output)
mod['func_5035'] = func_5035
mod = relay.transform.InferType()(mod)
output = func_5035()
func_5036 = relay.Function([], output)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_831_call = mod.get_global_var('func_831')
func_833_call = mutated_mod.get_global_var('func_833')
call_5050 = relay.TupleGetItem(func_831_call(), 0)
call_5051 = relay.TupleGetItem(func_833_call(), 0)
output = relay.Tuple([call_5050,])
output2 = relay.Tuple([call_5051,])
func_5090 = relay.Function([], output)
mod['func_5090'] = func_5090
mod = relay.transform.InferType()(mod)
output = func_5090()
func_5091 = relay.Function([], output)
mutated_mod['func_5091'] = func_5091
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5114 = relay.var("var_5114", dtype = "float32", shape = (12, 9, 4))#candidate|5114|(12, 9, 4)|var|float32
var_5115 = relay.var("var_5115", dtype = "float32", shape = (12, 9, 4))#candidate|5115|(12, 9, 4)|var|float32
bop_5116 = relay.divide(var_5114.astype('float32'), relay.reshape(var_5115.astype('float32'), relay.shape_of(var_5114))) # shape=(12, 9, 4)
output = bop_5116
output2 = bop_5116
func_5129 = relay.Function([var_5114,var_5115,], output)
mod['func_5129'] = func_5129
mod = relay.transform.InferType()(mod)
var_5130 = relay.var("var_5130", dtype = "float32", shape = (12, 9, 4))#candidate|5130|(12, 9, 4)|var|float32
var_5131 = relay.var("var_5131", dtype = "float32", shape = (12, 9, 4))#candidate|5131|(12, 9, 4)|var|float32
output = func_5129(var_5130,var_5131,)
func_5132 = relay.Function([var_5130,var_5131,], output)
mutated_mod['func_5132'] = func_5132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_5202 = relay.TupleGetItem(func_1393_call(), 0)
call_5203 = relay.TupleGetItem(func_1394_call(), 0)
output = relay.Tuple([call_5202,])
output2 = relay.Tuple([call_5203,])
func_5204 = relay.Function([], output)
mod['func_5204'] = func_5204
mod = relay.transform.InferType()(mod)
output = func_5204()
func_5205 = relay.Function([], output)
mutated_mod['func_5205'] = func_5205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_5222 = relay.TupleGetItem(func_2494_call(), 0)
call_5223 = relay.TupleGetItem(func_2496_call(), 0)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_5244 = relay.TupleGetItem(func_281_call(), 0)
call_5245 = relay.TupleGetItem(func_283_call(), 0)
output = relay.Tuple([call_5222,call_5244,])
output2 = relay.Tuple([call_5223,call_5245,])
func_5253 = relay.Function([], output)
mod['func_5253'] = func_5253
mod = relay.transform.InferType()(mod)
output = func_5253()
func_5254 = relay.Function([], output)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_5295 = relay.TupleGetItem(func_1393_call(), 0)
call_5296 = relay.TupleGetItem(func_1394_call(), 0)
func_2558_call = mod.get_global_var('func_2558')
func_2560_call = mutated_mod.get_global_var('func_2560')
call_5297 = relay.TupleGetItem(func_2558_call(), 0)
call_5298 = relay.TupleGetItem(func_2560_call(), 0)
func_5090_call = mod.get_global_var('func_5090')
func_5091_call = mutated_mod.get_global_var('func_5091')
call_5312 = relay.TupleGetItem(func_5090_call(), 0)
call_5313 = relay.TupleGetItem(func_5091_call(), 0)
output = relay.Tuple([call_5295,call_5297,call_5312,])
output2 = relay.Tuple([call_5296,call_5298,call_5313,])
func_5324 = relay.Function([], output)
mod['func_5324'] = func_5324
mod = relay.transform.InferType()(mod)
mutated_mod['func_5324'] = func_5324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5324_call = mutated_mod.get_global_var('func_5324')
call_5325 = func_5324_call()
output = call_5325
func_5326 = relay.Function([], output)
mutated_mod['func_5326'] = func_5326
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5327 = relay.var("var_5327", dtype = "int16", shape = (6, 2, 9))#candidate|5327|(6, 2, 9)|var|int16
var_5328 = relay.var("var_5328", dtype = "int16", shape = (6, 2, 9))#candidate|5328|(6, 2, 9)|var|int16
bop_5329 = relay.equal(var_5327.astype('bool'), relay.reshape(var_5328.astype('bool'), relay.shape_of(var_5327))) # shape=(6, 2, 9)
output = bop_5329
output2 = bop_5329
func_5333 = relay.Function([var_5327,var_5328,], output)
mod['func_5333'] = func_5333
mod = relay.transform.InferType()(mod)
var_5334 = relay.var("var_5334", dtype = "int16", shape = (6, 2, 9))#candidate|5334|(6, 2, 9)|var|int16
var_5335 = relay.var("var_5335", dtype = "int16", shape = (6, 2, 9))#candidate|5335|(6, 2, 9)|var|int16
output = func_5333(var_5334,var_5335,)
func_5336 = relay.Function([var_5334,var_5335,], output)
mutated_mod['func_5336'] = func_5336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3305_call = mod.get_global_var('func_3305')
func_3307_call = mutated_mod.get_global_var('func_3307')
call_5405 = relay.TupleGetItem(func_3305_call(), 1)
call_5406 = relay.TupleGetItem(func_3307_call(), 1)
var_5411 = relay.var("var_5411", dtype = "float64", shape = (3, 13, 2))#candidate|5411|(3, 13, 2)|var|float64
bop_5412 = relay.logical_and(call_5405.astype('bool'), relay.reshape(var_5411.astype('bool'), relay.shape_of(call_5405))) # shape=(3, 13, 2)
bop_5415 = relay.logical_and(call_5406.astype('bool'), relay.reshape(var_5411.astype('bool'), relay.shape_of(call_5406))) # shape=(3, 13, 2)
output = relay.Tuple([bop_5412,])
output2 = relay.Tuple([bop_5415,])
func_5418 = relay.Function([var_5411,], output)
mod['func_5418'] = func_5418
mod = relay.transform.InferType()(mod)
var_5419 = relay.var("var_5419", dtype = "float64", shape = (3, 13, 2))#candidate|5419|(3, 13, 2)|var|float64
output = func_5418(var_5419)
func_5420 = relay.Function([var_5419], output)
mutated_mod['func_5420'] = func_5420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2334_call = mod.get_global_var('func_2334')
func_2336_call = mutated_mod.get_global_var('func_2336')
call_5437 = relay.TupleGetItem(func_2334_call(), 0)
call_5438 = relay.TupleGetItem(func_2336_call(), 0)
var_5439 = relay.var("var_5439", dtype = "float64", shape = (11, 12, 8))#candidate|5439|(11, 12, 8)|var|float64
bop_5440 = relay.bitwise_and(call_5437.astype('int64'), var_5439.astype('int64')) # shape=(11, 12, 8)
bop_5443 = relay.bitwise_and(call_5438.astype('int64'), var_5439.astype('int64')) # shape=(11, 12, 8)
output = bop_5440
output2 = bop_5443
func_5453 = relay.Function([var_5439,], output)
mod['func_5453'] = func_5453
mod = relay.transform.InferType()(mod)
var_5454 = relay.var("var_5454", dtype = "float64", shape = (11, 12, 8))#candidate|5454|(11, 12, 8)|var|float64
output = func_5453(var_5454)
func_5455 = relay.Function([var_5454], output)
mutated_mod['func_5455'] = func_5455
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5457 = relay.var("var_5457", dtype = "float32", shape = (16, 9, 16))#candidate|5457|(16, 9, 16)|var|float32
uop_5458 = relay.asin(var_5457.astype('float32')) # shape=(16, 9, 16)
bop_5463 = relay.equal(uop_5458.astype('bool'), relay.reshape(var_5457.astype('bool'), relay.shape_of(uop_5458))) # shape=(16, 9, 16)
output = relay.Tuple([bop_5463,])
output2 = relay.Tuple([bop_5463,])
func_5475 = relay.Function([var_5457,], output)
mod['func_5475'] = func_5475
mod = relay.transform.InferType()(mod)
mutated_mod['func_5475'] = func_5475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5476 = relay.var("var_5476", dtype = "float32", shape = (16, 9, 16))#candidate|5476|(16, 9, 16)|var|float32
func_5475_call = mutated_mod.get_global_var('func_5475')
call_5477 = func_5475_call(var_5476)
output = call_5477
func_5478 = relay.Function([var_5476], output)
mutated_mod['func_5478'] = func_5478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2334_call = mod.get_global_var('func_2334')
func_2336_call = mutated_mod.get_global_var('func_2336')
call_5540 = relay.TupleGetItem(func_2334_call(), 0)
call_5541 = relay.TupleGetItem(func_2336_call(), 0)
func_4533_call = mod.get_global_var('func_4533')
func_4534_call = mutated_mod.get_global_var('func_4534')
call_5555 = relay.TupleGetItem(func_4533_call(), 0)
call_5556 = relay.TupleGetItem(func_4534_call(), 0)
output = relay.Tuple([call_5540,call_5555,])
output2 = relay.Tuple([call_5541,call_5556,])
func_5558 = relay.Function([], output)
mod['func_5558'] = func_5558
mod = relay.transform.InferType()(mod)
output = func_5558()
func_5559 = relay.Function([], output)
mutated_mod['func_5559'] = func_5559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_5562 = relay.TupleGetItem(func_1393_call(), 0)
call_5563 = relay.TupleGetItem(func_1394_call(), 0)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_5570 = relay.TupleGetItem(func_353_call(), 1)
call_5571 = relay.TupleGetItem(func_355_call(), 1)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_5581 = relay.TupleGetItem(func_353_call(), 1)
call_5582 = relay.TupleGetItem(func_355_call(), 1)
output = relay.Tuple([call_5562,call_5570,call_5581,])
output2 = relay.Tuple([call_5563,call_5571,call_5582,])
func_5592 = relay.Function([], output)
mod['func_5592'] = func_5592
mod = relay.transform.InferType()(mod)
output = func_5592()
func_5593 = relay.Function([], output)
mutated_mod['func_5593'] = func_5593
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5644 = relay.var("var_5644", dtype = "float64", shape = (15, 16, 5))#candidate|5644|(15, 16, 5)|var|float64
var_5645 = relay.var("var_5645", dtype = "float64", shape = (15, 16, 5))#candidate|5645|(15, 16, 5)|var|float64
bop_5646 = relay.less(var_5644.astype('bool'), relay.reshape(var_5645.astype('bool'), relay.shape_of(var_5644))) # shape=(15, 16, 5)
output = bop_5646
output2 = bop_5646
func_5654 = relay.Function([var_5644,var_5645,], output)
mod['func_5654'] = func_5654
mod = relay.transform.InferType()(mod)
mutated_mod['func_5654'] = func_5654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5654_call = mutated_mod.get_global_var('func_5654')
var_5656 = relay.var("var_5656", dtype = "float64", shape = (15, 16, 5))#candidate|5656|(15, 16, 5)|var|float64
var_5657 = relay.var("var_5657", dtype = "float64", shape = (15, 16, 5))#candidate|5657|(15, 16, 5)|var|float64
call_5655 = func_5654_call(var_5656,var_5657,)
output = call_5655
func_5658 = relay.Function([var_5656,var_5657,], output)
mutated_mod['func_5658'] = func_5658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_281_call = mod.get_global_var('func_281')
func_283_call = mutated_mod.get_global_var('func_283')
call_5677 = relay.TupleGetItem(func_281_call(), 0)
call_5678 = relay.TupleGetItem(func_283_call(), 0)
func_2334_call = mod.get_global_var('func_2334')
func_2336_call = mutated_mod.get_global_var('func_2336')
call_5695 = relay.TupleGetItem(func_2334_call(), 0)
call_5696 = relay.TupleGetItem(func_2336_call(), 0)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_5699 = relay.TupleGetItem(func_1886_call(), 0)
call_5700 = relay.TupleGetItem(func_1888_call(), 0)
func_853_call = mod.get_global_var('func_853')
func_856_call = mutated_mod.get_global_var('func_856')
call_5703 = relay.TupleGetItem(func_853_call(relay.reshape(call_5677.astype('float32'), [3, 13, 2])), 0)
call_5704 = relay.TupleGetItem(func_856_call(relay.reshape(call_5677.astype('float32'), [3, 13, 2])), 0)
func_2097_call = mod.get_global_var('func_2097')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_5705 = func_2097_call()
call_5706 = func_2097_call()
output = relay.Tuple([call_5677,call_5695,call_5699,call_5703,call_5705,])
output2 = relay.Tuple([call_5678,call_5696,call_5700,call_5704,call_5706,])
func_5726 = relay.Function([], output)
mod['func_5726'] = func_5726
mod = relay.transform.InferType()(mod)
mutated_mod['func_5726'] = func_5726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5726_call = mutated_mod.get_global_var('func_5726')
call_5727 = func_5726_call()
output = call_5727
func_5728 = relay.Function([], output)
mutated_mod['func_5728'] = func_5728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3096_call = mod.get_global_var('func_3096')
func_3098_call = mutated_mod.get_global_var('func_3098')
call_5736 = relay.TupleGetItem(func_3096_call(), 1)
call_5737 = relay.TupleGetItem(func_3098_call(), 1)
func_489_call = mod.get_global_var('func_489')
func_491_call = mutated_mod.get_global_var('func_491')
call_5744 = relay.TupleGetItem(func_489_call(), 0)
call_5745 = relay.TupleGetItem(func_491_call(), 0)
func_4474_call = mod.get_global_var('func_4474')
func_4475_call = mutated_mod.get_global_var('func_4475')
call_5746 = relay.TupleGetItem(func_4474_call(), 0)
call_5747 = relay.TupleGetItem(func_4475_call(), 0)
output = relay.Tuple([call_5736,call_5744,call_5746,])
output2 = relay.Tuple([call_5737,call_5745,call_5747,])
func_5759 = relay.Function([], output)
mod['func_5759'] = func_5759
mod = relay.transform.InferType()(mod)
output = func_5759()
func_5760 = relay.Function([], output)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3096_call = mod.get_global_var('func_3096')
func_3098_call = mutated_mod.get_global_var('func_3098')
call_5807 = relay.TupleGetItem(func_3096_call(), 1)
call_5808 = relay.TupleGetItem(func_3098_call(), 1)
func_2003_call = mod.get_global_var('func_2003')
func_2005_call = mutated_mod.get_global_var('func_2005')
call_5809 = relay.TupleGetItem(func_2003_call(), 2)
call_5810 = relay.TupleGetItem(func_2005_call(), 2)
uop_5838 = relay.asin(call_5809.astype('float32')) # shape=(14, 144)
uop_5840 = relay.asin(call_5810.astype('float32')) # shape=(14, 144)
bop_5848 = relay.subtract(uop_5838.astype('uint64'), relay.reshape(call_5809.astype('uint64'), relay.shape_of(uop_5838))) # shape=(14, 144)
bop_5851 = relay.subtract(uop_5840.astype('uint64'), relay.reshape(call_5810.astype('uint64'), relay.shape_of(uop_5840))) # shape=(14, 144)
uop_5852 = relay.atan(uop_5838.astype('float64')) # shape=(14, 144)
uop_5854 = relay.atan(uop_5840.astype('float64')) # shape=(14, 144)
func_523_call = mod.get_global_var('func_523')
func_527_call = mutated_mod.get_global_var('func_527')
call_5864 = relay.TupleGetItem(func_523_call(relay.reshape(call_5807.astype('float32'), [3, 13, 2]), relay.reshape(call_5807.astype('float32'), [3, 13, 2]), ), 2)
call_5865 = relay.TupleGetItem(func_527_call(relay.reshape(call_5807.astype('float32'), [3, 13, 2]), relay.reshape(call_5807.astype('float32'), [3, 13, 2]), ), 2)
uop_5876 = relay.sigmoid(bop_5848.astype('float32')) # shape=(14, 144)
uop_5878 = relay.sigmoid(bop_5851.astype('float32')) # shape=(14, 144)
func_219_call = mod.get_global_var('func_219')
func_222_call = mutated_mod.get_global_var('func_222')
var_5880 = relay.var("var_5880", dtype = "float64", shape = (770,))#candidate|5880|(770,)|var|float64
call_5879 = relay.TupleGetItem(func_219_call(relay.reshape(var_5880.astype('float64'), [10, 7, 11]), relay.reshape(var_5880.astype('float64'), [10, 7, 11]), ), 0)
call_5881 = relay.TupleGetItem(func_222_call(relay.reshape(var_5880.astype('float64'), [10, 7, 11]), relay.reshape(var_5880.astype('float64'), [10, 7, 11]), ), 0)
output = relay.Tuple([call_5807,uop_5852,call_5864,uop_5876,call_5879,var_5880,])
output2 = relay.Tuple([call_5808,uop_5854,call_5865,uop_5878,call_5881,var_5880,])
func_5882 = relay.Function([var_5880,], output)
mod['func_5882'] = func_5882
mod = relay.transform.InferType()(mod)
mutated_mod['func_5882'] = func_5882
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5883 = relay.var("var_5883", dtype = "float64", shape = (770,))#candidate|5883|(770,)|var|float64
func_5882_call = mutated_mod.get_global_var('func_5882')
call_5884 = func_5882_call(var_5883)
output = call_5884
func_5885 = relay.Function([var_5883], output)
mutated_mod['func_5885'] = func_5885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2774_call = mod.get_global_var('func_2774')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_5923 = relay.TupleGetItem(func_2774_call(), 0)
call_5924 = relay.TupleGetItem(func_2775_call(), 0)
func_4858_call = mod.get_global_var('func_4858')
func_4859_call = mutated_mod.get_global_var('func_4859')
call_5930 = func_4858_call()
call_5931 = func_4858_call()
func_4533_call = mod.get_global_var('func_4533')
func_4534_call = mutated_mod.get_global_var('func_4534')
call_5953 = relay.TupleGetItem(func_4533_call(), 0)
call_5954 = relay.TupleGetItem(func_4534_call(), 0)
func_1278_call = mod.get_global_var('func_1278')
func_1282_call = mutated_mod.get_global_var('func_1282')
var_5967 = relay.var("var_5967", dtype = "int64", shape = ())#candidate|5967|()|var|int64
const_5968 = relay.const([-7.750018,2.400868,-7.790415,-1.508164,7.251168,-0.364150,-1.778291,2.631241,7.541799,3.501850,-6.299491,-5.324935,-8.729677,-9.890580,-1.838308,-9.573175,-0.143046,9.771650,-3.147818,4.222080,-7.268458,-1.927075,3.912085,0.532819,9.202604,-8.031438,-4.961907,-0.696006,8.745083,-5.268302,1.006071,9.530929,-7.505033,-8.385501,-4.456149,-7.577234,-1.080858,6.095027,-9.924741,-0.053941,-3.781860,5.581050,5.123946,4.885268,9.116080,-0.287989,-3.647211,-5.778882,-9.252763,9.445644,-4.628448,1.712976,1.412867,-3.960564,7.095239,6.728506,5.547734,-1.343229,-3.245871,-4.244771,9.551849,-5.228945,-4.633152,2.730667,-0.400143,9.022903,-5.948969,6.130546,-2.496199,-9.054555,-5.469186,3.560132,-1.161091,-3.393893,4.296171,-8.280856,7.314493,-3.609331,-0.886720,-0.573743,-6.807707,9.207613,-4.174037,-4.722714,5.856817,-1.689084,-5.096321,7.133237,1.593758,-0.227341,-7.003934,7.598230,3.626024,2.548400,8.699129,-8.378585,-6.356845,8.243572,-0.500170,3.549525,-6.503027,7.881607,0.243636,7.460422,-9.355050,4.086783,7.962888,-6.832053,-4.535093,-5.016648,0.898934,4.435515,-4.101670,-0.147951,6.592569,-4.560238,1.486243,-7.886057,0.306161,6.933791,1.192631,-4.875251,-3.414247,-6.934812,1.631237,-0.239017,2.215169,-0.066533,-7.812721,9.215825,-6.213980,2.969810,8.545684,-0.489145,-9.278221,7.453604,-3.231063,-5.007983,-5.341472,7.087135,5.112182,3.663694,6.586037,-6.417118,-4.921286,6.813156,-6.221486,4.597338,1.879502,-4.412787,4.998546,1.910747,9.208860,-3.860653,-3.556389,2.787202,-0.563643,4.136641,-8.604450,0.823650,9.481405,4.891264,-0.066772,4.384909,-5.950997,4.703566,7.995719,0.186319,-1.591327,7.180048,2.231501,-2.578151,6.458758,-8.263592,8.039870,-8.411241,-2.214950,-6.545654,-5.100824,-5.574686,3.242824,1.427686,5.740793,-7.146535,-4.862891,-5.218623,-1.044239,6.497701,-1.559895,-7.689110,-6.742225,-2.645440,-9.762051,4.499541,5.807299,-8.357498,0.985955,3.033281,-5.693349,-8.839319,4.769343,6.590902,4.819135,5.940101,-4.718536,7.404677,4.172722,9.142803,4.831799,-6.411544,8.053858,6.313058,-7.953265,1.616203,-4.973978,-4.985194,-1.942142,-6.535659,-6.668387,-7.463431,4.032543,4.632727,1.861406,-5.467995,3.875355,9.061124,2.454007,8.158486,-3.048919,0.928046,-0.563273,-8.874221,5.692113,-0.165865,4.901424,-5.380439,1.313948,4.915605,-9.563682,0.345596,-6.388486,-3.572005,9.727922,-6.667821,-7.324967,5.510251,9.873615,-0.363279,-0.542617,-6.682714,4.003947,-4.368136,5.179189,4.424466,0.102347,0.293969,-7.661729,-8.748718,-2.833455,0.882136,-7.507834,5.255755,-1.562898,-2.360206,1.666937,-9.426661,5.261749,7.127714,-6.775443,-0.940011,3.509210,-4.644031,-8.582144,3.068141,0.481832,9.697025,4.951773,3.410076,-3.569636,-3.764458,-3.420219,-9.677114,0.847818,-7.524008,6.612489,-2.610536,1.728506,-9.715265,7.675362,-2.936916,-8.988801,-3.887156,-1.932293,1.849489,2.543135,-3.736573,6.233996,9.306058,-7.110016,-3.934424,-7.516634,-1.009545,8.513990,0.871930,2.166833,3.365972,-3.703914,7.769245,8.024713,5.927841,0.975590,8.257342,3.739745,7.519838,-0.737194,6.426628,-2.757512,-9.795548,-9.495155,-4.795188,3.203669,1.951153,6.210767,2.337278,2.360323,1.387635,-6.235299,3.112496,6.700287,-3.362567,6.537426,6.045654,3.642914,0.472482,7.404503,7.082457,-6.181853,-0.185316,-0.178460,-7.160522,4.709517,-0.602377,-0.666901,7.129338,-1.435550,-5.567591,0.061438,-8.868001,2.138980,-1.709372,0.574516,-3.838038,-9.189516,-7.750440,-0.621760,-8.123951,-4.691063,6.130421,0.329760,1.113732,-7.071447,0.060700,3.899848,5.094422,1.395522,3.042674,3.712495,-1.410457,1.356612,-0.132538,-8.076471,8.310599,5.467105,8.277731,7.989657,4.818517,-8.445143,2.474085,-1.363276,0.735972,-3.356734,-4.419231,-0.693763,2.207302,8.220553,7.049650,-4.531823,6.622297,9.353322,-0.139902,9.912576,4.147325,-9.401731,2.045242,3.082080,9.321121,0.932244,4.887938,-7.708771,4.504045,5.228150,0.257132,1.593105,1.923684,-4.086201,2.672238,7.739205,1.236862,2.338151,-8.062271,7.108537,-7.004624,-9.849899,-0.291011,-3.215975,-5.964319,-2.088872,-4.868257,-2.855836,6.662872,0.084375,-1.105621,8.836238,6.087846,-8.844446,7.640132,0.941433,8.197505,6.881299,-9.052538,4.243173,0.850639,0.726865,-9.835185,-7.160160,-8.588051,-2.670252,-5.764941,-3.537828,1.853100,-4.260706,1.070759,-3.370722,0.812253,-7.377574,-9.540962,-1.609471,-7.458800,6.374134,-2.102946,-8.756925,4.091800,0.528576,-2.479626,6.349157,7.176257,-2.206868,5.990144,8.760698,-0.434605,4.207524,9.223070,9.140284,9.573078,-0.562891,-0.540385,-7.428403,-7.176826,6.697146,1.235473,-4.240953,-1.499681,5.993559,0.348602,-8.379153,6.620221,-8.887208,-0.711126,-6.961873,-5.801004,5.778535,4.979472,6.397489,7.899632,-0.219104,8.436140,5.126110,2.360143,-3.070391,1.935926,-1.294066,-0.860843,-8.094426,-3.344425,-4.004216,6.433247,4.144204,2.537565,-5.021711,-2.064070,0.569698,1.464954,4.848752,-9.795693,-1.971761,0.572116,-8.679151,7.659172,-9.907615,4.167313,5.986306,-4.268816,1.374553,8.569032,-2.997958,-4.951910,7.378498,5.462109,-6.439115,-0.177847,0.397555,0.921381,1.527204,-8.452759,5.725630,-1.689101,2.974280,1.539857,-5.639012,-5.656214,-0.711750,8.600300,7.443464,2.916346,-3.814569,-9.513899,2.089635,5.353034,-9.803073,-5.861846,8.422876,-9.819209,3.980374,6.203765,-8.956787,-1.736134,-7.301625,6.989949,-1.780698,6.263644,-7.847049,2.525113,5.172009,3.971657,-2.520135,0.304836,-2.791590,-3.090507,-9.097138,-1.269892,-7.543999,7.175421,-5.124494,-4.933829,1.449219,4.256985,9.782812,1.413303,8.618547,-8.435299,-6.356715,7.159718,-8.577053,-1.497970,5.393302,0.910447,-4.676590,-3.762940,9.523620,9.635022,-6.472947,9.392895,6.351748,-5.867123,1.485183,7.996471,8.419797,-9.419918,-7.175469,-6.827500,6.912152,7.250071,-7.862816,-5.166116,-1.732900,4.488889,-6.674600,-0.707754,9.848606,-6.276842,-5.662623,7.705359,-3.510762,2.894873,-8.430718,-6.011224,6.119502,7.863934,1.637728,-3.626031,-4.879841,-3.342552,-0.316112,-7.980194,-9.929014,-4.436636,-9.791808,-7.235851,7.543935,-3.381459,8.212479,-8.685654,-2.918907,-3.454829,6.991273,-7.304310,-3.286333,3.647471,2.913731,2.708235,-6.348819,-6.084339,2.362291,-3.521404,-0.419626,-3.438046,8.549207,9.491656,1.130932,-3.738300,-8.901684,-1.498926,1.617832,9.122331,3.247673,-5.175394,-9.607166,0.383045,9.192852,-2.914201,-5.440298,0.747754,1.465565,8.375702,8.364355,-8.063075,-4.872836,-5.465917,-0.268945,6.054522,-9.133395,7.023911,-2.583844,-2.223185,-5.682609,-9.828152,-1.813508,2.391318,-1.900781,-5.357290,-9.542423,0.595061,8.525842,-6.782182,5.969899,2.473497,-4.877234,-0.866096,3.410007,-8.689666,9.624016,-4.577266,2.714680,-1.661336,1.812854,3.707445,6.058066,-0.100556,-6.004693,-3.081205,-6.262242,-6.033555,-2.801288,-1.140092,5.912341,-4.257538,1.399733,-8.065924,-1.468321,-6.328900,3.382568,1.495112,-2.517187,3.727280,-6.522259,-2.041101,-5.921238,7.592824,9.237568,-6.254645,2.847834,3.374010,-5.182621,3.394291,-0.475164,-6.414226,7.761936,-5.347413,2.658602,-9.130506,7.392341,9.017663,9.284656,4.329362,-8.059858,-7.233438,-4.925419,-1.997666,5.545328,7.220938,6.193506,-8.849631,9.073741,-4.130462,-1.284475,-9.309803,4.959556,0.442407,6.261161,7.546813,3.468750,6.899066,0.818844,-5.138947,0.352408,4.847651,5.283647,4.631458,-4.345647,6.466918,-3.694471,9.630744,2.508169,2.399001,1.738570,-2.462847,-8.769936,-0.052581,1.629310,-0.817330,-7.862052,2.020048,5.167289,-3.229866,-8.337462,9.187639,6.352280,-2.357806,7.939563,1.169054], dtype = "float64")#candidate|5968|(770,)|const|float64
var_5969 = relay.var("var_5969", dtype = "float64", shape = (11550,))#candidate|5969|(11550,)|var|float64
call_5966 = relay.TupleGetItem(func_1278_call(relay.reshape(var_5967.astype('int64'), []), relay.reshape(const_5968.astype('float64'), [1, 770]), relay.reshape(var_5969.astype('float64'), [15, 770]), ), 7)
call_5970 = relay.TupleGetItem(func_1282_call(relay.reshape(var_5967.astype('int64'), []), relay.reshape(const_5968.astype('float64'), [1, 770]), relay.reshape(var_5969.astype('float64'), [15, 770]), ), 7)
output = relay.Tuple([call_5923,call_5930,call_5953,call_5966,var_5967,const_5968,var_5969,])
output2 = relay.Tuple([call_5924,call_5931,call_5954,call_5970,var_5967,const_5968,var_5969,])
func_5974 = relay.Function([var_5967,var_5969,], output)
mod['func_5974'] = func_5974
mod = relay.transform.InferType()(mod)
mutated_mod['func_5974'] = func_5974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5974_call = mutated_mod.get_global_var('func_5974')
var_5976 = relay.var("var_5976", dtype = "int64", shape = ())#candidate|5976|()|var|int64
var_5977 = relay.var("var_5977", dtype = "float64", shape = (11550,))#candidate|5977|(11550,)|var|float64
call_5975 = func_5974_call(var_5976,var_5977,)
output = call_5975
func_5978 = relay.Function([var_5976,var_5977,], output)
mutated_mod['func_5978'] = func_5978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_831_call = mod.get_global_var('func_831')
func_833_call = mutated_mod.get_global_var('func_833')
call_5997 = relay.TupleGetItem(func_831_call(), 1)
call_5998 = relay.TupleGetItem(func_833_call(), 1)
func_523_call = mod.get_global_var('func_523')
func_527_call = mutated_mod.get_global_var('func_527')
call_6008 = relay.TupleGetItem(func_523_call(relay.reshape(call_5997.astype('float32'), [3, 13, 2]), relay.reshape(call_5997.astype('float32'), [3, 13, 2]), ), 1)
call_6009 = relay.TupleGetItem(func_527_call(relay.reshape(call_5997.astype('float32'), [3, 13, 2]), relay.reshape(call_5997.astype('float32'), [3, 13, 2]), ), 1)
output = relay.Tuple([call_5997,call_6008,])
output2 = relay.Tuple([call_5998,call_6009,])
func_6015 = relay.Function([], output)
mod['func_6015'] = func_6015
mod = relay.transform.InferType()(mod)
mutated_mod['func_6015'] = func_6015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6015_call = mutated_mod.get_global_var('func_6015')
call_6016 = func_6015_call()
output = call_6016
func_6017 = relay.Function([], output)
mutated_mod['func_6017'] = func_6017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_648_call = mod.get_global_var('func_648')
func_650_call = mutated_mod.get_global_var('func_650')
call_6047 = func_648_call()
call_6048 = func_648_call()
func_5204_call = mod.get_global_var('func_5204')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_6066 = relay.TupleGetItem(func_5204_call(), 0)
call_6067 = relay.TupleGetItem(func_5205_call(), 0)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_6094 = func_3468_call()
call_6095 = func_3468_call()
output = relay.Tuple([call_6047,call_6066,call_6094,])
output2 = relay.Tuple([call_6048,call_6067,call_6095,])
func_6116 = relay.Function([], output)
mod['func_6116'] = func_6116
mod = relay.transform.InferType()(mod)
mutated_mod['func_6116'] = func_6116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6116_call = mutated_mod.get_global_var('func_6116')
call_6117 = func_6116_call()
output = call_6117
func_6118 = relay.Function([], output)
mutated_mod['func_6118'] = func_6118
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6152 = relay.var("var_6152", dtype = "int16", shape = (8, 4, 8))#candidate|6152|(8, 4, 8)|var|int16
var_6153 = relay.var("var_6153", dtype = "int16", shape = (8, 4, 8))#candidate|6153|(8, 4, 8)|var|int16
bop_6154 = relay.less_equal(var_6152.astype('bool'), relay.reshape(var_6153.astype('bool'), relay.shape_of(var_6152))) # shape=(8, 4, 8)
func_4241_call = mod.get_global_var('func_4241')
func_4244_call = mutated_mod.get_global_var('func_4244')
var_6170 = relay.var("var_6170", dtype = "float32", shape = (78,))#candidate|6170|(78,)|var|float32
call_6169 = relay.TupleGetItem(func_4241_call(relay.reshape(var_6170.astype('float32'), [3, 13, 2])), 1)
call_6171 = relay.TupleGetItem(func_4244_call(relay.reshape(var_6170.astype('float32'), [3, 13, 2])), 1)
output = relay.Tuple([bop_6154,call_6169,var_6170,])
output2 = relay.Tuple([bop_6154,call_6171,var_6170,])
func_6173 = relay.Function([var_6152,var_6153,var_6170,], output)
mod['func_6173'] = func_6173
mod = relay.transform.InferType()(mod)
mutated_mod['func_6173'] = func_6173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6173_call = mutated_mod.get_global_var('func_6173')
var_6175 = relay.var("var_6175", dtype = "int16", shape = (8, 4, 8))#candidate|6175|(8, 4, 8)|var|int16
var_6176 = relay.var("var_6176", dtype = "int16", shape = (8, 4, 8))#candidate|6176|(8, 4, 8)|var|int16
var_6177 = relay.var("var_6177", dtype = "float32", shape = (78,))#candidate|6177|(78,)|var|float32
call_6174 = func_6173_call(var_6175,var_6176,var_6177,)
output = call_6174
func_6178 = relay.Function([var_6175,var_6176,var_6177,], output)
mutated_mod['func_6178'] = func_6178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2660_call = mod.get_global_var('func_2660')
func_2662_call = mutated_mod.get_global_var('func_2662')
call_6193 = relay.TupleGetItem(func_2660_call(), 1)
call_6194 = relay.TupleGetItem(func_2662_call(), 1)
output = call_6193
output2 = call_6194
func_6212 = relay.Function([], output)
mod['func_6212'] = func_6212
mod = relay.transform.InferType()(mod)
output = func_6212()
func_6213 = relay.Function([], output)
mutated_mod['func_6213'] = func_6213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2774_call = mod.get_global_var('func_2774')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_6227 = relay.TupleGetItem(func_2774_call(), 2)
call_6228 = relay.TupleGetItem(func_2775_call(), 2)
output = call_6227
output2 = call_6228
func_6230 = relay.Function([], output)
mod['func_6230'] = func_6230
mod = relay.transform.InferType()(mod)
output = func_6230()
func_6231 = relay.Function([], output)
mutated_mod['func_6231'] = func_6231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_6234 = func_458_call()
call_6235 = func_458_call()
output = relay.Tuple([call_6234,])
output2 = relay.Tuple([call_6235,])
func_6258 = relay.Function([], output)
mod['func_6258'] = func_6258
mod = relay.transform.InferType()(mod)
mutated_mod['func_6258'] = func_6258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6258_call = mutated_mod.get_global_var('func_6258')
call_6259 = func_6258_call()
output = call_6259
func_6260 = relay.Function([], output)
mutated_mod['func_6260'] = func_6260
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6266 = relay.var("var_6266", dtype = "int16", shape = ())#candidate|6266|()|var|int16
var_6267 = relay.var("var_6267", dtype = "int16", shape = (14, 9, 11))#candidate|6267|(14, 9, 11)|var|int16
bop_6268 = relay.multiply(var_6266.astype('int16'), var_6267.astype('int16')) # shape=(14, 9, 11)
output = relay.Tuple([bop_6268,])
output2 = relay.Tuple([bop_6268,])
func_6271 = relay.Function([var_6266,var_6267,], output)
mod['func_6271'] = func_6271
mod = relay.transform.InferType()(mod)
mutated_mod['func_6271'] = func_6271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6271_call = mutated_mod.get_global_var('func_6271')
var_6273 = relay.var("var_6273", dtype = "int16", shape = ())#candidate|6273|()|var|int16
var_6274 = relay.var("var_6274", dtype = "int16", shape = (14, 9, 11))#candidate|6274|(14, 9, 11)|var|int16
call_6272 = func_6271_call(var_6273,var_6274,)
output = call_6272
func_6275 = relay.Function([var_6273,var_6274,], output)
mutated_mod['func_6275'] = func_6275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4359_call = mod.get_global_var('func_4359')
func_4361_call = mutated_mod.get_global_var('func_4361')
call_6289 = relay.TupleGetItem(func_4359_call(), 4)
call_6290 = relay.TupleGetItem(func_4361_call(), 4)
output = call_6289
output2 = call_6290
func_6291 = relay.Function([], output)
mod['func_6291'] = func_6291
mod = relay.transform.InferType()(mod)
output = func_6291()
func_6292 = relay.Function([], output)
mutated_mod['func_6292'] = func_6292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2083_call = mod.get_global_var('func_2083')
func_2085_call = mutated_mod.get_global_var('func_2085')
call_6316 = relay.TupleGetItem(func_2083_call(), 1)
call_6317 = relay.TupleGetItem(func_2085_call(), 1)
func_4163_call = mod.get_global_var('func_4163')
func_4166_call = mutated_mod.get_global_var('func_4166')
var_6353 = relay.var("var_6353", dtype = "float64", shape = (3, 40))#candidate|6353|(3, 40)|var|float64
const_6354 = relay.const(-2, dtype = "int64")#candidate|6354|()|const|int64
call_6352 = relay.TupleGetItem(func_4163_call(relay.reshape(var_6353.astype('float64'), [6, 4, 5]), relay.reshape(const_6354.astype('int64'), []), ), 4)
call_6355 = relay.TupleGetItem(func_4166_call(relay.reshape(var_6353.astype('float64'), [6, 4, 5]), relay.reshape(const_6354.astype('int64'), []), ), 4)
output = relay.Tuple([call_6316,call_6352,var_6353,const_6354,])
output2 = relay.Tuple([call_6317,call_6355,var_6353,const_6354,])
func_6356 = relay.Function([var_6353,], output)
mod['func_6356'] = func_6356
mod = relay.transform.InferType()(mod)
var_6357 = relay.var("var_6357", dtype = "float64", shape = (3, 40))#candidate|6357|(3, 40)|var|float64
output = func_6356(var_6357)
func_6358 = relay.Function([var_6357], output)
mutated_mod['func_6358'] = func_6358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_6373 = relay.TupleGetItem(func_1886_call(), 0)
call_6374 = relay.TupleGetItem(func_1888_call(), 0)
uop_6389 = relay.acos(call_6373.astype('float64')) # shape=(3, 13, 2)
uop_6391 = relay.acos(call_6374.astype('float64')) # shape=(3, 13, 2)
func_4709_call = mod.get_global_var('func_4709')
func_4713_call = mutated_mod.get_global_var('func_4713')
const_6395 = relay.const([7.833887,5.562397,-4.642452,5.112583,-8.700664,-6.182867,-5.769257,-0.508672,-3.491031,6.202508,-2.701451,-5.089682,1.460617,-6.857417,4.767777,-5.952200,1.587249,1.215663,4.944937,-6.306100,9.131594,-8.833656,7.718743,4.007768,-5.187024,-1.511920,-8.774556,-8.516216,-4.659582,-8.828490,-6.781048,-0.720612,-9.420754,-5.611862,-4.572016,5.056243,7.579065,4.353397,5.885815,7.014232,-3.829449,-1.617017,-6.231548,-0.283435,3.802017,-6.706810,-1.639399,5.170896,3.177346,-1.405154,-3.368303,7.273090,5.108024,-1.710743,1.135634,9.521299,-6.942405,-6.600275,-6.025549,6.286308,-0.675650,1.823286,7.797666,0.984872,-1.932570,-4.041173,-6.595823,6.753879,3.724453,-3.711086,5.972347,-4.841178,2.475089,-7.389235,3.041910,4.482780,-1.321867,-9.266037,-4.899007,-1.872837,-3.989536,5.480344,-7.669030,-0.374861,4.516039,-8.150144,-7.691625,-5.996517,-9.366929,3.803199,-8.270282,0.744189,-8.499205,-8.940607,6.041036,4.704470,-6.663834,-1.120726,6.987573,-1.364848,5.758993,0.163176,1.946961,4.839312,1.440030,5.750888,-4.846971,-7.272945,4.071646,1.680341,2.011247,-9.283654,4.613793,-8.581307,8.940258,5.796136,7.217421,8.100675,-0.647778,-3.965354,6.708208,-9.358400,-8.756112,-9.396388,3.990417,4.133578,4.363008,-1.880937,-7.260205,7.742181,9.090504,2.235493,-9.440268,2.323892,8.486004,-0.570063,-6.923107,-3.382650,0.672272,-3.234597,-4.997581,3.961601,3.251896,4.335775,-2.029518,0.529377,5.091326,-8.252066,1.494925,9.508263,-6.162270,-7.895487,-3.139421,1.474682,1.011380,-4.503533,5.820431,3.541645,-0.296681,0.191029,-6.514833,-8.351166,6.645681,0.961824,0.333294,1.155862,-4.396464,-8.375325,8.110173,-6.918191,8.684551,-1.785542,-8.087850,0.006838,-1.850071,4.935519], dtype = "float64")#candidate|6395|(176,)|const|float64
const_6396 = relay.const([[3,-9,4,-3,-4,6,-2,-1,-7,5,9,-8,-7,8,2,-6,-4,1,3,-10,-1,-2,-3,7,7,3,9,10,4,5,5,-4,-6,-10,-8,-7,-7,3,1,2,-3,5,-6,5,-4,9,-4,10],[-5,1,1,4,9,9,-9,-10,-8,2,10,6,-8,5,8,-1,4,-8,-2,-2,-4,-2,2,3,7,-5,-3,-10,8,2,-1,-8,-7,-9,-3,-1,-1,-9,-5,4,10,-8,2,5,-5,3,3,10]], dtype = "int64")#candidate|6396|(2, 48)|const|int64
call_6394 = relay.TupleGetItem(func_4709_call(relay.reshape(const_6395.astype('float64'), [8, 2, 11]), relay.reshape(call_6373.astype('int64'), [78,]), relay.reshape(const_6396.astype('int64'), [96,]), ), 0)
call_6397 = relay.TupleGetItem(func_4713_call(relay.reshape(const_6395.astype('float64'), [8, 2, 11]), relay.reshape(call_6373.astype('int64'), [78,]), relay.reshape(const_6396.astype('int64'), [96,]), ), 0)
func_6212_call = mod.get_global_var('func_6212')
func_6213_call = mutated_mod.get_global_var('func_6213')
call_6406 = func_6212_call()
call_6407 = func_6212_call()
output = relay.Tuple([uop_6389,call_6394,const_6395,const_6396,call_6406,])
output2 = relay.Tuple([uop_6391,call_6397,const_6395,const_6396,call_6407,])
func_6408 = relay.Function([], output)
mod['func_6408'] = func_6408
mod = relay.transform.InferType()(mod)
mutated_mod['func_6408'] = func_6408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6408_call = mutated_mod.get_global_var('func_6408')
call_6409 = func_6408_call()
output = call_6409
func_6410 = relay.Function([], output)
mutated_mod['func_6410'] = func_6410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_6536 = relay.TupleGetItem(func_1886_call(), 0)
call_6537 = relay.TupleGetItem(func_1888_call(), 0)
output = relay.Tuple([call_6536,])
output2 = relay.Tuple([call_6537,])
func_6542 = relay.Function([], output)
mod['func_6542'] = func_6542
mod = relay.transform.InferType()(mod)
mutated_mod['func_6542'] = func_6542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6542_call = mutated_mod.get_global_var('func_6542')
call_6543 = func_6542_call()
output = call_6543
func_6544 = relay.Function([], output)
mutated_mod['func_6544'] = func_6544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2774_call = mod.get_global_var('func_2774')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_6577 = relay.TupleGetItem(func_2774_call(), 1)
call_6578 = relay.TupleGetItem(func_2775_call(), 1)
output = call_6577
output2 = call_6578
func_6579 = relay.Function([], output)
mod['func_6579'] = func_6579
mod = relay.transform.InferType()(mod)
mutated_mod['func_6579'] = func_6579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6579_call = mutated_mod.get_global_var('func_6579')
call_6580 = func_6579_call()
output = call_6580
func_6581 = relay.Function([], output)
mutated_mod['func_6581'] = func_6581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_6587 = func_3468_call()
call_6588 = func_3468_call()
output = call_6587
output2 = call_6588
func_6609 = relay.Function([], output)
mod['func_6609'] = func_6609
mod = relay.transform.InferType()(mod)
mutated_mod['func_6609'] = func_6609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6609_call = mutated_mod.get_global_var('func_6609')
call_6610 = func_6609_call()
output = call_6610
func_6611 = relay.Function([], output)
mutated_mod['func_6611'] = func_6611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1514_call = mod.get_global_var('func_1514')
func_1515_call = mutated_mod.get_global_var('func_1515')
call_6661 = relay.TupleGetItem(func_1514_call(), 1)
call_6662 = relay.TupleGetItem(func_1515_call(), 1)
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
const_6711 = relay.const([-1,10,7,-1,3,8,-4,-4,7,8,9,6,-4,1,10,2,8,-3,-1,-9,2,-6,6,-3,-5,-6,4,-4,5,-6,-3,6,2,6,8,6,5,-8,-3,6,1,6,-4,-4,4,-5,10,-8,-1,-6,2,-8,-7,7,-7,-9,7,-4,6,1,9,8,-7,2,1,-6,-3,9,3,1,1,10,5,-10,-3,-10,-8,2,5,3,3,8,-6,-7,4,-2,-7,-4,6,3,8,-10,4,-2,-7,4,4,7,10,2,-9,9,-7,-8,1,-2,7,-5,-5,9,-10,1,4,8,1,7,4,-6,1,4,7,10,10,-4,-10,7,5,-8,6,-4,5,9,-7,10,10,1,10,1,5,-4,-8,7,-9,-2,-10,-1,8,-4,-6,-5,8,4,-7,5,10,-7,10,-2,8,3,-2,2,-4,-5,1,-7,-5,-7,5,4,-1,6,6,10,5,3,8,7,4,-4,-1,-3,9,-1,-4,-2,8,8,-7,10,-2,9,-10,1,8,10,6,8,-5,-2,3,-4,3,7,-10,1,-1,9,-7,-7,8,4,1,9,-10,5,-4,-4,-8,-6,7,-10,10,-2,-2,1,4,-1,-7,1,1,1,-4,2,-6,-10,-8,5,-2,4,-4,1,10,5,4,5,1,-1,-10,6,-5,-3,1,-10,3,-4,-1,-6,-8,-10,-6,-8,-2,-3,5,-2,-10,-1,3,1,-7,6,1,-1,-3,-1,-8,6,-9,-4,-10,3,3,8,-7,-3,-5,4,-1,3,8,10,5,9,7,-6,-2,-7,-3,1,6,-6,-3,5,7,-7,-3,2,5,10,5,-10,-5,1,2,7,8,-6,-6,-4,-10,10,7,3,-3,5,9,8,10,1,3,-9,3,-1,-8,-2,7,-4,-3,-8,10,-8,-9,-4,-6,-3,2,8,-9,4,8,-8,5,-1,8,7,-5,8,9,-4,-4,-2,1,4,2,9,-2,-5,10,-7,5,6,-9,5,6,-3,-6,-9,-6,9,8,8,-7,-9,6,5,2,-3,-8,6,-8,4,-3,-3,3,9,-3,3,7,-7,10,6,3,-10,8,3,-7,9,10,-1,5,-4,4,-8,-9,-5,5,10,3,-9,6,-8,-10,4,-1,1,-4,6,-4,10,9,4,-9,4,-4,4,6,4,-8,-4,-1,7,-3,5,7,-3,-1,10,3,1,-8,9,6,10,10,-5,10,-8,2,10,-9,4,4,-7,10,6,4,2,9,-5,7,-1,9,9,3,1,-6,1,10,9,-7,-8,10,-10,-3,7,-5,6,-8,-5,6,-4,-2,-2,-2,-4,6,9,-3,7,5,7,-2,6,-2,10,9,-2,-8,5,7,-8,-1,-3,9,-2,3,6,6,3,5,8,1,8,6,9,3,8,-8,8,-8,2,4,5,2,-10,5,-4,7,6,-5,7,-6,-2,6,2,2,5,3,-8,2,-5,-5,5,-3,7,10,10,1,-10,1,2,7,-1,-1,-9,-8,-2,-5,7,10,10,10,-5,1,9,-9,-7,-10,7,9,2,2,10,-3,-7,-1,-4,-8,-3,8,1,4,-2,-8,4,6,-7,-2,-8,-4,-1,-4,9,7,1,5,-1,-3,1,-5,-1,3,-9,-4,3,4,6,-8,-9,6,-10,-5,-10,-5,10,-8,-1,8,7,9,-4,3,-10,-5,-5,1,2,6,2,4,1,4,2,-2,-8,10,-1,-1,3,-9,7,-6,6,2,3,-4,8,6,10,1,-6,-9,4,-9,-6,-5,-10,3,-3,6,8,2,-7,-8,-4,-4,-9,-1,-1,-8,-9,-1,4,-5,-6,4,-2,-2,5,-4,10,-3,-9,2,3,8,-6,8,-10,6,-5,-3,-9,4,6,4,7,7,-10,-7,-10,4,5,-6,7,2,4,-9,-2,-6,-2,-6,-8,5,1,-10,1,9,-9,1,-6,-8,-10,-5,1,-5,-2,9,4,-9,-10,-8,-4,-4,-9,-9,-10,7,-5,4,-4,8,-10,7,5,-8,4,3,-2,-2,-4,8,-9,3,7,-1,-4,8,-8,-7,8,5,1,1,8,6,4,3,-9,9,-4,7,-9,-4,-10,9,8,2,-3,5,-8,-3,-3,6,-5,-7,5,-10,1,-1,-7,-8,4,4,-3,-1,8,-3,-2,-4,-6,-9,7,5,-3,6,9,-5,-4,-4,-8,9,-1,-8,3,-2,-2,-10,-10,8,5,7,8,7,-1,-10,-6,-6,1,-1,-5,-5,-6,8,2,-3,-10,1,2,-1,-10,3,-1,-4,2,-9,10,4,9,-4,-9,-9,9,10,-9,4,3,-5,6,-7,7,-5,-9,5,-2,10,7,-2,-7,-8,3,-6,-1,3,2,-8,-5,10,-2,4,5,7,1,-10,4,-7,-2,-5,5,2,7,10,1,-8,4,-8,5,-1,-9,-9,1,-9,-10,-5,4,2,-5,5,-2,-10,-6,3,8,-10,-7,9,6,10,-4,-10,-2,10,-7,-5,8,5,-8,5,-4,-2,-5,-8,8,-6,-5,-1,-1,6,5,-6,9,-7,8,10,9,3,-2,5,-1,4,-7,2,-5,-3,10,-5,9,-5,-6,-10,-8,6,-8,-1,2,-6,10,5,8,8,-9,8,-7,-6,-9,-7,-3,-8,6,1,-5,-6,-5,-10,1,3,-3,8,4,-6,-4,2,7,-8,9,10,-6,-1,-7,6,-1,6,7,-7,-7,6,5,9,-9,-5,-10,-4,-1,-7,-8,-4,1,-4,-3,-1,-3,4,-6,9,3,4,1,8,-5,-8,-10,-1,-2,1,-7,8,1,9,4,-5,-4,-10,8,-6,-5,-5,7,-7,-2,-6,1,10,-5,-9,9,-8,4,-9,-6,-7,-9,7,10,-7,-2,-3,7,7,4,-1,-2,7,4,8,3,2,-10,10,-7,-4,9,4,-3,-8,-6,10,-7,-4,7,3,-7,-3,-6,-7,-9,-1,-10,-2,5,8,8,-9,-8,-8,-7,4,5,-1,10,5,-10,-6,5,-3,-10,4,-10,-5,-8,-3,3,8,-7,-1,8,-6,6,1,4,2,5,-3,8,3,-10,-8,-6,-1,7,9,9,6,-9,-7,-2,-6,4,4,-7,8,7,-10,-4,7,-2,7,-4,-9,3,-8,6,4,5,-3,-8,2,1,-8,1,-6,-4,4,-9,2,10,9,-2,-5,-2,1,-9,7,3,7,-3,-8,-8,-4,7,1,4,1,-2,4,5,3,-6,-6,-6,-4,-5,-5,-5,2,-4,9,-2,5,7,5,5,-5,-10,4,1,-6,-10,-1,-1,9,7,-5,-6,-10,-2,-4,7,-1,-10,5,-3,-10,-4,-8,-6,-2,2,-10,10,3,7,2,-5,-10,-6,-6,6,1,-9,-6,-5,7,-8,8,-9,3,-6,-9,-5,-8,6,9,-2,-3,-9,-5,7,-4,1,4,-2,-7,9,-3,-6,7,-5,-3,7,9,5,10,7,9,-5,7,10,-8,-9,7,-10,-9,-1,1,8,-3,5,7,5,-10,-8,8,3,1,6,9,-10,-2,-1,-8,4,-4,-5,9,-6,2,7,2,-7,2,-10,-1,1,1,8,-3,-3,9,7,-9,8,4,1,-5,-10,-4,-2,-1,8,-5,3,7,4,-3,-8,3,-2,-3,-7,-3,-9,-7,10,4,-2,-4,-6,1,9,-4,-6,2,5,5,6,-1,5,-4,8,2,-6,4,-7,5,-1,-2,-5,9,2,4,-1,2,2,10,-3,-1,1,2,-2,-6,3,2,-4,8,2,-5,4,7,-1,-10,-1,5,6,-10,2,1,-5,3,-1,-7,-10,6,-8,-2,1,-5,-2,-4,8,5,9,-5,-9,4,-7,3,-3,-3,-3,4,-8,-8,-1,-9,6,9,9,10,2,8,-6,9,1,4,7,-9,9,5,10,7,7,-1,-1,6,6,-3,4,-4,3,10,8,-7,9,-6,-6,-4,10,3,8,-3,3,7,-9,4,-2,2,-4,-6,-10,9,-5,1,10,-7,3,-3,7,6,4,7,-4,6,7,8,-4,5,2,7,2,-2,-5,3,-6,9,1,-6,5,1,-5,9,-8,1,10,3,3,7,2,-9,1,8,3,6,-7,-8,-6,2,-1,3,2,-5,3,2,-4,-4,8,-6,6,-7,-9,-5,-3,-8,-3,-8,-8,9,-5,-5,-9,-3,-10,8,-2,-1,1,7,-5,10,7,3,1,5,1,6,-10,9,-9,-8,-3,4,-4,-1,8,-7,1,10,-1,9,-6,4,-3,8,3,5,-2,1,1,-7,5,-4,5,10,9,-10,6,3,-10,-5,6,8,-8,5,2,10,5,6,8,-8,9,3,3,-7,8,5,-2,3,-3,-1,8,6,5,-5,-10,-9,-10,-4,-8,-7,5,-10,6,-8,2,8,3,5,-8,1,1,8,-2,-6,5,5,-7,6,-10,6,6,-2,-10,6,-7,-7,-9,-2,7,-9,3,-4,-3,-6,7,-3,-6,1,-1,-5,6,-9,-4,5,-8,6,2,-4,10,-6,-1,-9,5,4,-9,-4,-10,-9,3,8,10,-5,-3,5,-8,-2,1,10,3,2,5,-8,-9,9,-3,-3,10,5,-6,9,-3,-5,-2,2,8,-9,10,-8,-4,-10,6,10,-1,1,5,-1,9,-5,-10,-8,9,-1,-5,-7,-10,8,8,1,-4,7,2,-10,-4,6,9,2,1,8,-6,9,-2,1,-6,1,7,-9,-8,2,3,-5,1,-2,-3,-10,-7,-5,5,-3,8,-9,4,4,7,1,3,2,-5,6,-7,7,5,-7,7,1,3,-10,10,-8,-1,8,-7,8,7,10,-2,1,10,-10,-5,-6,-3,-7,2,3,-4,-5,-3,5,-7,-5,-3,-6,4,3,9,10,-6,6,-10,-1,-1,-9,9,4,8,-5,-8,5,-9,1,-6,9,-6,1,-5,2,9,10,-5,6,-6,4,3,5,-6,9,5,-7,4,-9,-10,-7,-2,7,-3,-1,-3,4,4,8,-8,-5,3,-6,-10,8,-5,9,1,-5,8,-7,10,-6,3,-6,9,3,-1,-10,3,-1,10,6,-5,-10,-10,3,-10,-6,-3,5,-4,-3,-9,-8,-1,-1,-8,-6,1,-3,3,-10,-4,-8,-1,-8,-1,-9,-6,-3,3,-9,2,-3,1,3,-3,1,-1,4,-1,-4,3,-3,10,5,-9,-6,10,-3,5,-9,8,6,6,-3,2,9,3,-4,7,6,-6,4,-2,-8,-2,-7,-6,2,-3,-1,4,-2,-2,-10,8,5,-8,9,-8,9,6,2,9,6,-1,-6,-8,2,5,-1,7,6,-6,7,1,-4,2,-1,-2,-2,7,-5,-8,-7,8,7,-3,-3,7,-5,-10,7,4,2,8,-6,3,10,-10,-6,4,-6,-6,9,2,4,-2,-3,-1,-2,-8,2,4,5,-10,4,4,-4,-2,-4,5,-8,8,-3,6,-6,6,8,-1,-5,3,4,1,10,10,-10,1,-2,-9,8,2,2,5,7,-4,-6,2,-8,9,-8,9,4,6,-1,-10,-2,4,-10,5,-6,2,10,3,8,-4,-10,4,7,9,7,-8,4,3,2,3,-1,-9,10,-10,1,-5,-9,5,9,5,-3,-6,-4,3,9,3,1,-2,3,9,8,-6,-1,4,-5,9,-1,-5,4,-2,-3,4,6,-7,9,-4,8,-3,-1,2,-5,3,3,-10,7,-1,-6,6,-2,4,9,-8,8,-7,-10,6,-9,3,1,1,7,10,-7,-7,1,2,-9,-8,-6,7,-5,3,-4,-10,-2,-4,-2,-2,3,2,1,6,6,9,1,8,-1,-4,7,-1,-4,6,9,9,-7,8,2,-10,-9,8,4,-10,7,9,5,-5,-5,6,-10,6,3,7,-9,4,3,10,2,-2,3,4,-3,6,1,4,5,1,5,3,-3,1,-3,-5,2,-3,-3,10,8,-6,10,-2,-9,2,1,7,6,-1,-3,-5,8,-8,7,-8,8,5,5,10,10,-9,9,4,8,-6,6,5,-9,6,3,-2,10,-8,5,-1,1,-4,8,8,5,-6,-3,-4,4,-10,-4,7,-8,-10,-2,-5,-3,-5,-9,6,7,5,-2,4,-9,-2,-5,-8,3,-5,1,8,-1,4,8,-3,1,-6,-7,9,-5,8,10,-2,-3,6,8,-7,-8,10,10,-10,-3,6,-7,5,-5,-1,-8,8,1,-5,-9,-10,3,5,-5,-6,1,8,8,9,6,-10,10,-8,-1,10,5,-9,9,-4,8,3,-6,9,-6,-1,6,-9,-1,-9,-9,-4,-8,5,-8,-4,-2,8,-7,4,-3,8,-8,6,-3,4,4,8,-5,-1,-5,9,-9,-7,-4,-4,8,6,10,-9,-9,-6,-5,6,1,-2,2,4,-10,10,4,1,-5,-9,-3,9,-3,6,9,-7,9,7,-1,-3,-1,-5,8,-8,2,-9,8,-6,2,9,4,-4,-5,6,-1,7,3,-9,-5,-7,6,4,3,5,4,9,-1,-2,-3,2,-7,-7,8,-5,-5,-4,10,5,9,-1,5,10,-2,-2,-1,8,-1,2,3,4,10,8,-5,-3,4,-5,3,-5,-8,-9,-1,-8,-4,-2,8,6,4,-9,-7,-1,-8,10,-2,6,3,-10,4,7,-8,8,6,5,-8,-7,7,-7,-6,8,-3,-9,-2,1,7,-6,8,1,8,4,-10,-2,-10,-4,8,-4,6,7,2,-4,7,-2,-3,-9,-10,-6,5,-9,-7,-1,5,-5,-9,-9,-2,10,4,-2,-6,8,5,6,2,-5,8,-3,3,4,-2,-3,-9,-2,4,1,-7,5,5,-10,-7,-7,10,8,9,7,6,-4,4,9,1,9,-9,10,6,-2,-4,7,-8,-9,-8,8,6,-10,-9,-10,7,6,4,1,-5,-4,-1,-7,8,7,4,-10,9,-3,-9,7,-10,3,1,5,-6,-9,2,5,3,5,-7,-8,-7,5,3,1,8,-7,-7,-9,1,-1,5,2,9,-5,-4,-5,5,-4,-3,-2,-8,-10,-1,-9,6,-5,7,-8,5,-3,10,10,7,4], dtype = "uint16")#candidate|6711|(2640,)|const|uint16
call_6710 = func_1707_call(relay.reshape(const_6711.astype('uint16'), [15, 16, 11]))
call_6712 = func_1707_call(relay.reshape(const_6711.astype('uint16'), [15, 16, 11]))
output = relay.Tuple([call_6661,call_6710,const_6711,])
output2 = relay.Tuple([call_6662,call_6712,const_6711,])
func_6718 = relay.Function([], output)
mod['func_6718'] = func_6718
mod = relay.transform.InferType()(mod)
mutated_mod['func_6718'] = func_6718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6718_call = mutated_mod.get_global_var('func_6718')
call_6719 = func_6718_call()
output = call_6719
func_6720 = relay.Function([], output)
mutated_mod['func_6720'] = func_6720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2774_call = mod.get_global_var('func_2774')
func_2775_call = mutated_mod.get_global_var('func_2775')
call_6723 = relay.TupleGetItem(func_2774_call(), 2)
call_6724 = relay.TupleGetItem(func_2775_call(), 2)
func_1278_call = mod.get_global_var('func_1278')
func_1282_call = mutated_mod.get_global_var('func_1282')
var_6731 = relay.var("var_6731", dtype = "int64", shape = ())#candidate|6731|()|var|int64
const_6732 = relay.const([[-2.938183,7.108889,9.278756,0.465045,-8.773475,3.920336,-1.867627,-2.640845,7.493736,-4.606265,-5.591584,0.517007,-1.916937,5.585873,8.375774,-1.335393,-1.862477,8.851366,4.553343,1.669767,1.097114,-2.789208,-6.593243,-0.932430,1.019172,3.881419,-3.044551,6.138564,-2.125867,0.266116,-8.308541,4.250650,8.093238,0.802622,7.273502,-6.314177,9.200609,-2.495794,6.243459,8.071316,2.283914,5.898067,5.129238,8.286971,1.502384,0.227254,-7.886386,-9.213153,-5.806025,-7.346200,-0.401848,-6.090102,-7.966463,7.966089,6.765514,-4.595146,-3.052422,-6.059813,-3.583868,2.344774,-3.896513,-3.200700,0.776374,5.342049,-2.890982,2.452683,-4.575159,-5.981135,2.219894,4.024536,-0.955214,4.784472,0.672424,1.886298,0.400029,9.907229,8.956824,-3.172374,-6.143408,-4.992288,-9.548372,8.155470,-8.431864,2.385217,0.671101,-6.757465,-6.407276,-1.586703,-2.683504,-5.425820,-8.585210,6.769124,6.085759,-9.796426,8.423664,-4.241320,0.930963,3.913511,3.997801,0.332189,9.797383,-3.396910,5.884813,1.423543,-8.038862,-6.512634,9.901366,9.368603,0.285197,-4.234291,-7.212119,-7.326668,-2.650592,8.328020,-3.989454,-2.497977,8.447328,-6.465450,-4.887815,-2.766740,6.646259,8.279212,-0.575384,6.064292,8.277411,8.154595,-3.782989,5.304432,8.194627,-2.083235,4.919693,7.721258,9.508019,2.056092,3.240830,6.026382,-1.747164,1.268970,2.260418,1.187559,-9.406855,-6.373353,-1.899575,4.421155,9.087071,-5.259437,-0.816413,4.984900,3.541603,8.348747,-1.349312,2.696807,-7.097813,3.009066,2.676474,-4.582858,5.702052,-3.117287,-0.899550,3.740279,7.917705,-9.589466,0.367275,1.415424,-0.907698,6.932810,0.981910,-9.447909,7.583898,0.362630,-7.070165,-6.652218,9.511537,0.280233,-8.248370,8.805503,-3.108307,-8.942017,8.750859,-2.121842,-5.521861,-1.617716,-4.313470,9.732602,-6.114464,-8.682904,-4.456180,4.211142,4.760852,0.657268,4.174353,0.806213,-3.527264,-1.656820,-0.617979,-5.072721,-8.051466,-0.417602,9.654448,6.624861,3.933336,-9.026125,-0.236685,7.912998,-1.519665,-0.971761,3.263241,-5.786571,3.081493,0.766934,9.913539,-9.004113,-1.760148,6.673429,1.655939,3.210757,-3.594340,-4.011518,0.031313,8.767848,7.457271,-1.444551,3.743504,-2.354039,1.865885,-7.471760,2.723644,-3.197560,-9.462929,3.930697,-0.029429,-9.398441,-4.684445,-7.488542,-5.072224,-4.452529,8.114548,-0.651712,2.108415,5.547179,-9.441101,6.416637,-6.774781,9.485153,6.968714,-1.580588,1.670018,7.234905,-9.462900,-7.961934,3.987296,-6.593902,8.789734,7.839236,0.413393,2.401049,9.030798,-1.740757,-9.210902,-5.196912,-5.327385,-2.057811,4.025377,-5.151032,2.877726,-8.036277,3.004051,5.569156,6.826384,4.683538,3.202101,-1.899636,0.162311,-5.654535,-6.623075,-6.599651,-3.859500,-9.874687,-2.209094,4.353910,3.014783,-8.410375,-1.251242,2.954350,-7.651237,-4.102999,3.485562,-5.439051,8.803220,2.270176,7.618060,6.109800,-0.934597,6.949569,-4.083984,-3.658288,-1.438102,-6.397995,-7.504917,-8.014678,-9.668256,-7.358227,9.221423,-6.302342,3.493920,-0.105660,0.804430,-9.672444,-1.459290,-2.685294,-2.275060,-5.324331,0.621233,1.419929,4.903981,6.737461,8.836137,4.307568,-0.768061,3.169895,2.618710,0.741104,9.488450,-1.206941,0.422255,-4.022601,7.359917,6.135326,1.649214,-3.073442,-8.159892,-5.998307,4.780165,1.148738,-9.406185,-1.583175,-7.140289,-3.818148,3.643556,7.315559,-9.598570,1.218720,0.320758,-1.221792,2.345416,7.386073,-0.322245,2.898563,0.513248,-2.370001,-3.478742,-5.413339,-3.497980,-8.220796,1.282917,-7.196143,-6.029724,-1.277758,-3.500447,-7.964005,9.483792,-4.244653,-8.383635,-1.805482,-3.772938,5.457462,6.652264,1.666786,-2.516196,9.629944,-6.590920,7.548251,7.378889,-0.175611,7.243685,-3.679952,-7.052503,-2.509822,-5.324949,-5.928340,5.050606,2.692627,0.861799,-2.497077,7.745085,-7.485856,-6.450268,-6.157164,2.994583,2.556116,9.564610,3.864288,-0.323804,-7.280161,-7.699626,7.699881,-0.945832,-8.899318,-3.491253,-0.917947,6.944896,3.429413,-5.951317,0.103094,-3.137020,-1.361080,-6.240760,4.000594,-6.791399,-1.257058,-4.693333,-0.575464,-5.693656,1.246772,-0.718321,-2.655789,-6.612274,0.792480,2.703067,-9.151451,0.862658,-6.639131,-4.488848,3.834553,9.862547,-5.977415,2.417330,1.486701,5.470491,-5.585371,-5.947876,0.284380,-4.370585,4.409118,-1.001999,1.949861,3.097648,8.490916,6.397463,-6.034410,-0.227759,1.952216,2.534137,-6.525545,5.931529,-4.569768,5.230494,-4.806875,-4.245300,-3.013510,2.333778,0.716353,2.382434,-2.034676,5.775907,5.851466,5.181700,0.930270,2.753398,-3.478619,0.715768,-2.698908,-2.982020,-8.473369,4.622015,0.133422,9.729794,4.360513,-9.849435,1.339818,-3.465044,4.763003,8.749689,-2.026948,-8.943865,3.981973,-0.688806,6.330170,-7.464912,2.379281,-3.059004,-6.989016,3.394487,-1.633309,-1.109813,4.758466,-1.573659,-9.186388,-6.954620,6.937475,6.369931,-6.190313,-6.833907,2.895405,2.380239,-7.313015,8.661635,8.299694,-1.499994,-3.336439,-5.054957,3.509236,1.519368,-8.837371,3.429999,-3.703909,2.390633,-7.419213,-3.557108,-0.037001,-4.306025,5.047312,-3.267023,6.557319,-4.740253,0.245550,2.318990,-0.113020,-6.789036,-8.277604,-5.399369,9.007401,0.771170,0.816697,0.270470,-3.470680,3.859617,4.621710,-7.579524,-8.189283,9.971645,2.567409,2.861324,6.176729,8.397757,2.815398,-6.401299,3.620361,-6.074492,-7.863724,-4.421981,4.183795,-2.747562,5.275423,5.330700,-4.740288,7.201187,-8.966643,5.574175,7.760425,2.670679,-0.284056,1.807996,-1.606381,-9.283542,7.433498,9.374546,-2.362614,5.974596,-3.971422,-8.355859,5.336462,2.017717,-9.910620,2.773999,1.945810,-9.819683,5.035412,0.127187,4.808658,-5.227966,-3.214949,2.329516,5.033365,8.882053,-6.297951,-6.523487,6.813587,3.506127,-1.958558,3.402441,3.607499,9.896421,1.519319,-6.610711,1.017417,1.776031,-0.274174,-8.467284,-1.093234,-6.822450,3.025242,-2.313525,-5.203564,-1.468847,9.829597,-0.808398,7.514131,5.440763,-5.141193,9.777931,-4.445975,8.055488,-4.277809,-8.675375,0.087775,6.821997,-7.439143,-7.589616,8.330112,1.099433,-7.223766,7.202447,-7.738338,9.934036,2.070212,-4.710570,8.994397,-6.825077,6.996863,-5.372755,4.472249,-5.496327,-0.406004,-6.703965,5.880147,-5.180003,0.405413,-1.879650,-8.865838,-1.092993,-2.147939,8.106538,6.523311,7.332531,-0.022586,1.969351,9.935550,9.794366,-5.964230,7.073671,-0.742354,-9.640038,-2.541194,2.862782,-5.356840,-3.208767,-3.106057,-5.260874,6.331459,-7.059156,-1.002562,-4.164110,5.043845,6.539318,2.697470,-4.528060,-4.285008,-4.119439,7.690627,3.822240,3.404027,-6.386379,9.202741,0.763054,7.969825,-5.474183,-9.354429,4.209366,6.180560,1.798229,-1.760940,-1.977018,-5.483802,4.986769,-8.462507,8.555031,-0.978901,9.917177,3.515042,-3.888943,-4.455304,-4.423419,0.116730,7.081895,-0.154485,-3.275776,-0.641318,8.306940,7.737719,-9.634017,0.486421,5.468604,2.342719,4.390306,-8.960520,0.123969,-2.326450,4.462141,-1.162404,-3.398499,2.621577,3.691120,1.895644,6.433653,1.333649,-3.595168,3.614718,-3.473806,-6.178822,0.286506,6.427807,-8.759455,-2.849755,-9.385816,-0.136320,0.040665,7.078514,7.107909,4.257618,2.660557,-6.384891,7.282223,7.764042,-2.350904,0.166463,-1.078291,3.074411,8.453719,-1.112430,-7.080166,-5.414795,9.474072,-1.860178,1.907440,9.745582,-6.089156,-2.988594,4.290615,6.948478,-3.137211,-3.074616,8.878971,1.001471,0.501836,-4.309183,-8.362398,-7.977366,-4.505337,-1.935396,-3.624023,-6.844799,4.923914,1.604770,6.336580,-0.133542,3.716706,-7.883775,-0.797042,5.799014,-2.740471,1.098145,9.215893,-1.179542,-1.102488,7.155917,-2.941314,4.401056,-4.816222,-4.860824]], dtype = "float64")#candidate|6732|(1, 770)|const|float64
const_6733 = relay.const([7.153146,-2.822608,2.780990,-2.771856,4.099965,-1.834275,0.916855,9.892320,5.381509,-1.756289,-1.340631,1.026152,-5.718593,-1.374812,0.781417,3.002719,-9.970977,-7.375251,6.887320,3.687853,2.697379,2.158194,-7.238900,-7.271701,1.819281,4.003978,0.127187,9.562462,-3.875975,5.341105,5.866522,7.297202,-9.723893,-4.455256,-1.578927,9.978992,3.119051,-6.686092,3.410649,-9.777126,5.586033,-5.151797,-6.906238,3.261362,-3.817812,-6.770446,9.317522,8.112412,-7.324255,9.475778,9.361157,-9.417315,-2.999477,-0.012014,0.087922,-4.470063,-8.554876,2.386206,-0.998500,4.740837,-5.867641,9.969505,4.204632,8.679279,-2.531667,-6.127488,9.156250,-1.897056,5.785734,4.311269,4.655406,-2.275774,4.238296,0.085361,-8.669699,-7.326611,-0.158499,-7.165108,-0.707436,3.471309,-6.564953,-8.647224,-3.802740,4.209089,6.043751,8.690342,6.045450,-8.155404,2.036420,-8.437483,-1.506456,-9.324395,-8.937854,4.085981,7.971092,1.732510,-6.904517,6.055235,0.150121,5.810453,-7.299254,0.765628,-3.810857,-0.337889,3.769544,1.161151,4.893597,2.382263,-8.632439,-4.981328,7.836037,7.295490,6.822892,4.661398,-4.395052,2.886088,7.558870,-9.002972,-4.131555,5.046140,2.184750,8.841451,0.325239,2.156359,5.456732,5.504751,9.963583,3.077870,6.988855,1.732179,8.635392,-6.220566,-1.374706,-8.491995,2.812114,-9.949028,-3.603786,9.296728,-7.880931,7.802820,-7.853521,3.302762,7.189849,-7.709002,3.209991,-1.075856,-4.148178,7.900338,7.985937,1.554186,4.985985,-1.196801,-2.404809,9.417488,-6.495773,-5.276236,7.712566,-4.779781,-0.294372,-4.359602,6.627811,-0.979840,6.195927,-5.527491,7.635962,-3.138198,9.180375,-1.575384,-0.797765,0.470583,-2.224369,-0.144761,3.369678,6.712774,3.215023,3.352387,-8.286870,7.899092,9.844071,9.250561,4.480874,8.518922,-6.716017,-4.085228,-8.663059,0.405644,-0.313868,-9.376448,-9.349574,6.822723,1.096365,-6.636211,3.117655,-2.533229,3.245422,4.845198,1.583156,-2.171937,8.099218,-6.037088,-4.415407,-6.104143,0.957668,-4.843910,-2.188030,-5.427349,-0.327728,-9.242954,-2.087080,-7.637330,-4.364901,-3.818348,-2.239314,8.005268,-0.718850,5.038060,7.261350,6.718539,0.075105,-9.561768,5.718266,6.537187,-3.255487,5.298930,-1.156774,-1.773133,-2.075023,-2.542372,8.968307,-1.384172,-0.378805,-8.251522,3.828945,-6.936952,1.971783,5.328827,5.383919,-9.616687,-8.673540,-0.553272,9.026310,2.986895,-3.464023,8.118486,7.770877,8.214470,0.121971,1.055845,5.125410,2.310882,-8.500773,3.529255,-0.661573,0.276633,-0.695137,4.020417,9.379807,3.001842,9.969828,2.336119,-2.395824,-3.789603,1.162378,-7.453333,7.704019,0.544027,-4.940336,-6.863795,3.829671,5.486008,6.319987,5.258585,1.855658,-5.696048,3.745825,5.010237,-3.650717,-4.605099,6.034456,-2.387698,-2.330534,3.554793,5.896134,2.381916,9.471426,-9.085522,-6.447458,8.853092,-4.522539,-3.331197,-4.604811,9.031948,1.164801,-3.770379,-1.387747,1.660315,-4.464764,-3.996440,-3.510613,-7.101401,-0.157018,2.532001,9.394555,7.573563,-5.609000,6.964039,7.253245,-1.423148,-0.145257,-7.845025,2.341650,-2.710384,-0.248670,9.028394,-9.166676,-1.315087,-6.242656,2.623294,7.577566,9.650214,-3.805134,-4.028012,8.827257,-0.964965,1.114051,7.448759,4.877309,-7.629994,-8.580254,-9.874634,-8.263065,4.054664,-3.090899,-8.457624,2.730513,-1.496840,-5.601977,-4.586344,5.845729,-1.280808,8.090643,7.466831,6.386375,-8.599472,-1.948917,-1.226212,0.795135,2.798893,8.690789,2.924307,-9.937924,-9.165152,-2.337157,-9.707582,-0.187918,-9.153794,-1.204503,-4.153862,-4.245008,6.644261,2.287595,1.636340,-7.875663,1.769583,-7.112471,-4.777149,-4.397399,0.605352,4.625312,-6.729244,-0.380939,9.617602,-3.736228,-4.734472,-6.984172,1.390879,-7.148667,8.358999,-8.465465,-4.982988,4.985574,0.481284,4.810649,2.801043,-6.621712,-4.851795,-8.651607,-7.381324,1.370482,8.436570,-7.887996,-2.929075,2.116252,7.060005,-3.177191,-5.679662,9.717894,3.676856,8.188384,8.669646,-0.793025,-3.036551,-2.311836,4.851936,-1.595672,1.432980,-9.576664,4.612560,4.279521,2.024926,-0.295822,-8.290541,3.752824,-9.627722,-8.425058,-2.319021,-1.610634,4.763511,9.823097,-6.509798,-7.595397,5.001938,7.156328,-2.216604,6.897610,-4.607700,-6.088380,0.860871,-9.198620,-4.460897,-4.350242,3.922351,5.707594,2.895904,-2.376535,-3.469962,7.852232,3.934180,-5.099953,-8.895476,8.739364,6.768471,7.538491,3.460540,6.906172,-9.969518,-8.152202,-4.687569,-1.458354,2.966008,9.489966,7.572550,2.576007,-8.150573,4.256610,8.848803,9.344066,-0.719854,-1.361715,8.570785,4.575012,4.810935,7.682907,2.897100,2.517281,-1.337394,4.406527,9.374904,-0.829199,-2.659273,-8.554339,-9.927591,4.609261,-2.110367,-7.625351,8.360986,2.732735,-6.120931,-6.950840,5.794447,-6.185792,-8.735535,5.135069,-6.855590,6.572250,2.385722,-4.362924,-7.859717,-4.435131,4.673075,-1.149462,-1.218840,5.574711,-2.943201,9.414044,1.862738,-8.541102,6.465707,-8.493780,7.237471,-5.687280,6.310446,0.468984,-4.784773,6.317544,-9.888905,-5.346829,0.684920,7.691148,8.320305,2.100730,-1.546791,5.524037,-2.243330,4.329094,2.655843,-5.816852,5.269728,-7.692531,-4.284346,4.008687,6.559430,0.317758,-2.953495,2.413243,6.428556,-2.224468,-5.528483,8.974552,1.059512,-3.299178,4.695095,-4.108638,-3.389894,-0.987084,-3.622307,-4.482584,-3.993106,-8.525041,-0.751829,-8.927164,1.060023,-9.921988,-4.120845,-9.674860,-4.609231,6.673371,8.718941,-8.386474,-9.055287,-1.069666,6.300290,4.582563,0.565036,-6.495709,8.412871,8.764206,9.969878,-8.193949,-9.840642,-4.185309,8.342010,-7.371815,5.421266,5.355085,5.807126,-1.135044,-6.234808,-2.004533,7.910815,5.308491,-2.339833,5.083261,-2.151599,7.439874,-5.146384,-9.374874,8.710027,3.493257,9.311819,8.306070,-4.658156,2.251139,0.220374,-8.840291,-1.421576,5.869718,5.498253,2.381558,-1.124560,-5.173455,-2.945771,-4.589089,7.683458,-5.717341,-1.934740,3.485464,7.031269,3.721528,0.055493,2.810431,-2.645676,-2.204797,-1.722603,4.696814,-4.721970,1.681232,-5.278040,0.954697,5.216499,4.152185,8.934733,7.488235,2.144719,2.335536,-0.613889,0.080850,1.450295,-1.323557,7.930340,-0.631033,1.169579,-8.872380,1.952263,9.267812,5.115064,8.857482,-6.694206,5.727376,1.826922,-1.979833,5.923940,-8.155554,2.250363,-1.510568,2.101802,-5.254007,9.521356,-0.368779,-2.376622,4.715994,-0.877438,-6.369313,0.169576,1.965753,-4.235416,6.860016,0.645615,-2.070333,-3.212895,7.356652,5.651516,1.981376,-2.502737,-6.670449,7.874080,-1.739468,-3.062287,-4.211011,-9.384221,-9.880218,4.788937,-6.161499,-2.484980,9.036255,-2.877920,-4.149814,5.652135,-8.816048,7.668788,-6.475413,-0.039342,5.101621,-6.645671,1.418617,2.875340,5.973559,7.745904,7.027207,0.701457,-3.930040,9.448739,1.677559,-2.542163,-6.566342,-0.569465,3.997911,1.261088,2.993882,-4.883945,-4.820130,4.298583,5.302734,2.000985,-3.305594,2.864206,-1.125135,2.058134,6.793195,5.254825,8.594420,3.601136,0.838368,8.968519,-0.526901,6.046001,3.683194,-4.222515,1.962589,2.732916,-3.200573,-8.195448,2.082752,6.421336,-2.474423,-2.034411,-2.387145,-0.332615,-0.284768,7.285255,2.968827,4.232393,5.336437,8.361250,-5.811317,-2.409177,-3.384774,3.679811,-1.784332,-2.504834,-9.631002,-4.372437,-0.023410,-3.783459,1.266667,3.783159,-8.645911,9.528968,5.589768,-6.776730,-2.191645,-7.223616,4.968823,-4.984792,-9.521069,-1.646719,-3.162865,-3.307827,3.894056,4.913130,-3.135318,-9.993326,-4.422398,-4.489808,-0.761340,7.442513,8.794909,1.906346,5.572663,-9.660182,1.856874,-7.529680,2.468188,-4.576297,5.878760,8.842963,9.167918,-7.518259,-7.656649,5.770382,8.036775,0.298894,-2.955784,-5.787473,-8.164405,-4.468912,1.692144,7.539638,2.021917,-4.602647,-0.457424,-5.692397,4.854248,3.102142,2.270795,-9.946281,9.398239,4.013682,4.248851,2.177097,-2.620030,0.185893,4.633744,-1.396752,-8.899243,9.319187,1.622870,-7.185283,5.385881,-4.000062,-9.932952,3.663530,-1.188207,-6.190487,-5.873720,7.502181,8.954831,1.809125,-6.099337,1.003630,-3.513930,8.810994,-1.369065,-8.516361,8.735607,-1.618313,2.040701,6.071125,-7.938727,0.456619,0.472863,9.821159,6.934585,6.890536,-2.720914,5.610560,-6.905750,-8.444245,-0.012630,-4.663928,2.553606,-1.075084,-2.308487,-6.844625,5.922341,-2.435904,0.866783,5.233136,-2.157273,-9.847508,6.069597,4.247923,-6.195108,-0.978240,-9.588366,-8.535287,0.334387,-2.588146,-3.393306,-0.971957,4.404455,-8.728973,-8.686159,3.361406,4.223377,8.575118,0.956805,-6.115797,6.953725,6.312003,2.739127,0.181723,-7.352028,-2.031974,1.799292,-2.192583,2.185668,5.782284,-0.110400,-9.383333,-6.726590,-9.360993,-9.560965,7.311277,4.451666,8.266838,-0.405977,1.417102,8.672362,4.064153,-8.196360,1.517111,-1.773746,3.240678,8.711668,-1.483870,3.422580,-1.171768,4.141040,5.517299,-5.470158,4.426004,-9.101046,8.391356,1.591651,-0.594245,-5.958062,0.011985,-4.577430,9.190747,9.745271,3.404410,-9.582347,-5.556101,1.206701,-4.352275,6.277000,-5.064029,-3.504242,2.795198,-8.895565,6.555820,7.981727,0.596529,0.224524,5.246940,7.755043,6.109630,-3.130076,9.195273,-9.888469,3.653608,-2.330238,1.817446,1.542381,-9.368440,-0.534431,-7.066411,-7.265714,8.392577,-6.018256,-5.777793,0.651119,1.620044,-5.066093,9.826900,-6.092545,-6.407645,-7.577766,3.707146,-4.541718,4.359794,6.073134,-9.284755,1.738634,6.458206,-4.207463,7.881385,-2.561516,-8.527915,-1.688424,0.582305,-5.117285,9.433629,0.399404,3.577996,-4.424126,-9.975910,-7.156425,0.933432,-5.480601,-6.481062,8.469259,-8.798814,-7.744410,-1.456380,-2.925154,-2.867771,4.209173,3.627704,-4.264420,-4.491383,3.524618,1.277614,7.317118,6.776020,4.452915,-3.443451,-7.827868,-6.108862,5.192868,9.576837,-2.426071,5.473841,1.782847,-6.504077,5.005507,-3.269771,3.784653,-3.448398,-2.447734,-5.008784,9.864300,-9.258408,1.680301,1.992628,0.692253,-8.871816,-1.699413,6.055377,-8.892375,3.697069,-0.843175,-3.328344,3.112044,-5.110066,1.856863,-9.829988,-6.205938,-8.728444,9.737695,-6.289741,-4.614369,3.649190,-5.967226,-9.156677,-5.743122,-9.114690,1.131881,7.509684,-5.434831,-2.009292,-8.499432,-5.161882,-7.934439,6.583857,-2.827838,-2.099850,-7.022800,5.801373,7.029976,-4.172353,-8.481712,-9.197198,8.576587,-2.491800,-2.899460,2.557575,9.129028,9.530346,-1.278589,-9.390537,-3.958359,8.980819,-6.007442,-6.959572,-5.597987,9.288885,1.388826,-6.522422,9.866690,-7.832383,-1.002008,6.819741,-7.612636,8.677865,2.097040,3.713799,-2.985738,-4.688297,-4.306614,-6.484637,9.667131,9.603045,-4.110591,-1.167373,-0.773717,0.632719,-8.512236,8.582005,4.763671,-8.286750,-4.923049,-3.923447,-8.207497,4.572256,6.706292,-0.574429,2.024875,-3.499678,9.765937,-5.715140,8.727334,-8.438196,-9.444303,-9.238644,-5.523146,-4.773333,8.459247,-2.386787,9.302950,-3.827753,2.609698,-2.623798,-2.637556,-5.811948,5.827621,6.856057,-1.939781,-7.108055,2.204474,-3.959984,0.994152,-2.074535,-7.085078,0.234252,-7.654690,-5.004688,-9.591351,5.253890,3.512195,-1.866486,-9.466282,-1.385439,-6.404569,9.610689,1.105873,1.400089,-4.393774,2.693809,-5.724856,-1.122412,-4.458784,6.052236,8.584804,0.533135,-8.692854,5.151812,-6.238137,-7.069159,0.268841,-9.717670,2.663800,0.624612,-9.650673,-3.012554,9.605417,6.055855,-0.401681,-8.126486,4.790993,-8.003089,-3.258517,-5.204658,3.025551,9.793782,-4.275641,-3.249430,2.788819,3.715390,-0.734423,3.309917,0.118409,-8.927523,6.836359,1.319877,-9.878486,-2.125073,-4.826591,7.643064,1.395093,-5.724340,7.380077,-1.764694,-5.886311,-9.245871,8.593557,6.990795,-6.442736,-7.341844,-0.545290,2.223968,-1.889164,9.192728,-9.518087,-4.909790,2.360499,-8.020979,1.648978,-7.667655,-0.762844,2.240492,-5.283780,-2.403887,-8.295469,-1.168892,7.858879,8.766051,4.726986,-6.330182,-9.539188,-8.138846,4.727954,-5.679476,0.859234,-0.591978,2.305455,9.303251,-8.093832,-4.732905,6.089604,-5.520473,-4.035222,-0.627815,-4.479563,-2.525535,6.895090,6.418059,6.924859,-1.341312,-5.604357,-6.254494,-0.198402,6.467871,-7.859299,6.115828,-8.883780,-1.926679,6.517352,-4.601255,7.907679,-9.912057,0.256808,8.571393,3.406020,5.044790,-5.188533,5.757973,-0.964821,-2.694124,0.251621,-1.691167,0.343029,-3.751763,7.004714,-3.812930,0.566131,3.454919,-7.155536,9.202321,-6.263633,6.229602,6.022445,2.047617,3.641081,-3.235924,7.818975,-3.766206,5.363443,-2.515950,-5.193048,3.544534,8.597159,-0.021186,1.405086,-3.298933,8.096384,-0.435535,-8.168043,-0.991315,2.184835,-3.008071,9.561148,4.512059,-7.944184,0.184326,2.186221,-7.769145,3.880946,-5.631501,7.689414,6.798959,0.136628,1.597696,8.576523,6.520221,-6.484592,-4.805389,0.047139,-2.724526,2.123153,-3.632429,-6.599543,6.564106,2.463225,-4.056322,-3.294179,2.598179,5.397854,-8.214129,-5.454761,-4.973956,8.585660,-9.504846,-6.042426,-9.252120,-8.467153,-8.361725,-2.710005,1.284594,-5.132807,-2.418619,9.023223,-3.538104,-5.060540,3.590683,-2.415539,8.322058,-6.735792,-7.627375,-2.589511,-2.335181,2.142614,5.053003,8.739853,-2.624384,-6.281357,-7.078804,-5.022458,-8.035608,6.139338,-1.006201,4.295283,-8.083336,9.816828,0.382156,6.467339,1.663950,-8.652555,-4.630885,6.085031,5.895690,6.933346,8.637896,-7.093933,-6.159475,9.817187,-5.625786,-6.398778,6.752203,7.247101,2.938543,-9.193005,-4.070148,7.271564,-1.348812,3.360713,-4.452661,-0.876166,-2.526041,-1.491032,-3.207850,0.993921,-7.460138,3.813869,-1.708650,-6.268572,-5.511199,-8.264553,-6.799367,9.578714,-2.917028,-3.311815,-8.130996,-0.678017,-8.431633,0.704017,-0.725056,0.630860,9.531274,-2.879328,0.192983,4.366318,-4.677199,-6.557977,-9.618876,0.384172,-4.318107,8.277886,-1.656264,-1.102114,-7.787849,-9.316807,-0.296728,-9.140574,-0.721044,5.460287,4.191753,6.834508,-6.891487,-6.312041,-4.047794,1.342013,-1.559996,1.152838,-6.278648,6.205150,0.213644,-0.430815,8.878471,6.536269,5.660456,0.276006,-5.088816,-5.403252,0.250745,9.345716,7.652096,-3.074699,9.378795,-2.463173,5.281584,6.346428,4.128395,7.334674,-0.205589,2.895309,7.587495,-4.773551,9.512863,2.692628,-3.003463,-2.793647,4.715634,7.148855,-3.997412,7.318272,3.670187,8.541927,-0.722043,7.903532,2.089065,-9.135056,3.608720,-4.736964,-2.610866,7.145535,-2.538236,-9.932264,4.107616,3.812463,0.746399,9.205699,8.182469,-4.714986,0.911102,-3.534960,-0.794193,-2.426066,7.898755,-8.257257,-5.204062,-7.554929,-8.397496,-8.638062,-1.166867,9.114967,-7.169898,-5.891751,7.867262,7.409573,-3.242967,-3.571207,3.068371,1.298337,2.520803,-4.768617,0.467381,3.217051,6.354405,0.350867,6.937573,2.350646,-3.277651,1.377051,-9.990756,-8.673139,-3.007171,2.960563,8.897212,-3.742777,0.105196,-9.612322,-8.248174,-9.308233,-1.161642,9.237337,-7.265218,8.724922,5.925514,5.385094,-4.576786,-0.784437,-8.107077,-7.982038,-6.763343,-3.740169,5.005140,2.499854,-4.731290,8.122848,4.619400,-7.597320,5.980810,-4.884352,-3.252888,4.093464,-5.333823,1.608016,5.837277,-2.279764,6.157190,8.774630,-4.809068,-8.699935,-1.417975,3.695178,-8.133177,-1.152540,2.658840,-9.542745,-3.642208,-0.316646,-5.326032,8.138418,2.313365,7.978929,-8.886803,1.987382,1.658321,-3.078682,1.741015,-7.200833,2.943880,-8.516955,4.281327,8.727739,-5.327614,-9.417744,9.234131,-4.953253,-9.373002,5.615866,1.844109,9.143665,-1.020625,-2.733466,4.904588,-0.050977,0.967508,9.745513,6.501842,-6.598199,5.711820,-4.898488,-7.877065,6.053481,1.012713,-5.690256,-0.242246,2.349058,0.790471,-0.971042,-6.396737,8.254762,2.193465,0.375529,4.885845,-7.143534,-2.307506,-5.442738,-2.187966,5.118730,-1.239212,-9.938218,3.230401,-2.489758,2.435518,1.854018,5.226905,-2.166636,-6.966041,7.241104,0.797101,-0.808329,5.654776,4.208252,-9.410554,5.005905,-5.978995,3.802770,4.396407,-1.866200,5.894765,9.233461,-4.823468,8.981868,4.040403,4.468695,1.890789,-2.091276,-3.252257,-9.585897,5.993136,2.311021,7.581689,6.624392,-4.228705,9.031666,-6.003171,-3.859732,-0.859948,0.820431,6.510355,7.958321,-6.532908,1.014006,1.821322,2.569983,2.936608,-4.029575,-9.760586,0.131045,6.968693,-7.078855,9.835990,-6.230399,-8.745222,8.612590,-6.274922,-9.135195,6.709949,4.561307,4.969388,7.679623,-8.417096,5.428844,2.295675,2.251887,-9.255224,-3.288232,1.603808,0.905882,-0.231328,9.255130,6.539908,8.013623,1.570780,3.445621,-3.544791,2.773247,-2.955784,9.814337,8.633085,-1.249723,-9.120599,-6.278943,-1.599351,9.029394,-2.789426,3.316168,6.189025,-3.139103,-1.739305,3.351252,-3.710555,1.135337,-8.743885,3.368133,0.982745,3.682155,-3.806398,4.959484,3.362733,-0.084854,4.373812,-0.576851,-7.905296,9.698712,-2.948350,9.229824,7.621678,-9.974947,7.639158,-3.312707,5.118556,-9.903082,5.463051,-7.513866,9.147558,-7.144782,0.052339,0.087528,-2.729647,-7.453380,7.697327,6.654917,-2.890595,-6.115137,1.335335,-5.433635,-6.093034,5.987219,7.094152,6.134325,-2.431756,0.865025,-9.941496,1.556637,-3.759838,7.821711,-1.307046,-9.821456,-6.817315,-8.591369,6.899290,4.724074,-9.730364,4.736064,-0.390728,-5.080393,9.160217,-9.374189,-4.166507,-3.703782,9.533216,-0.990770,-2.630639,-9.336175,-6.695353,5.031278,-3.159532,7.186789,3.538389,-4.301614,6.311132,-9.535668,-3.444883,-0.580850,-7.556035,3.007384,2.239382,4.366256,5.358248,-1.800480,1.987032,9.992151,-3.837995,-1.037671,-7.198634,-4.264795,4.963283,-3.867201,1.870379,-2.399297,5.592643,-3.807519,9.346244,-7.061439,3.548774,-6.830176,-6.943673,-1.967986,8.631937,-3.433855,7.022616,9.458802,7.866953,5.885576,8.450451,6.146229,4.941190,9.061957,2.042635,2.036576,-5.359205,0.147038,-3.332007,-5.736453,-4.242694,7.613438,7.775831,-4.549259,-7.585337,0.947649,3.213382,-0.337279,-4.772256,-6.006414,1.068232,0.377717,2.861872,5.790917,-1.808311,0.409674,-6.350439,1.265716,-9.666709,7.758438,8.345764,-3.805279,6.687943,5.771446,-4.230699,0.984154,-2.657044,5.912953,-8.503585,5.001154,-0.996847,5.351519,3.263561,-0.739077,7.240886,-8.003249,3.444610,5.339466,7.000435,-2.365810,-5.720115,0.396527,-1.588067,0.846991,5.084117,-3.085173,8.831195,7.883130,-5.502560,-5.794003,2.253813,-7.880468,0.353145,5.080092,-3.941114,-6.801267,2.697367,3.393525,3.449739,-0.095811,4.279149,-7.276980,9.623250,7.692357,-7.973365,1.760022,-1.972444,-8.613907,8.468133,-7.674463,5.074087,4.734441,2.195192,7.111132,0.729277,7.056826,-9.138790,7.047032,7.810711,5.047507,8.658704,6.296121,-4.862903,9.307007,7.554682,0.033273,9.246650,-0.493270,-1.569174,4.099318,9.416255,-8.493267,-0.627867,4.159969,2.645922,6.221387,4.476719,-2.493247,-6.642946,-0.965045,-9.045738,3.127599,-9.834501,-9.742487,8.854654,-0.024740,-1.330743,-4.109921,-8.845365,6.682867,-3.548055,-0.300099,3.251270,8.263250,5.139552,-4.722942,7.894436,9.208438,4.411922,-6.025836,2.683409,3.080446,-3.977646,-3.438065,-9.428419,-1.857190,0.241690,-0.526818,4.382350,-9.808653,7.926785,-5.410930,-0.556339,-5.430237,5.710564,-7.528433,8.770519,5.566473,1.171504,2.359692,2.470139,-1.111823,-9.646886,9.170095,-7.308047,-1.087251,-3.376938,9.118899,-0.933643,-8.228123,-2.704345,-0.332123,4.208091,2.477149,-6.937121,-7.158165,-5.143637,-1.091080,9.587159,0.512426,7.991564,-5.152595,-0.157774,1.634320,6.677136,8.586648,-9.941658,-1.180646,4.314756,3.439564,-9.506833,4.518983,-2.550839,3.063972,1.385356,-2.778029,4.214841,8.953784,-8.951300,-7.096437,-3.844212,6.735756,-2.203052,-0.740186,-2.432632,5.023600,5.846237,2.834565,-7.697212,-5.995792,2.850621,-4.687504,3.018334,0.099595,-8.512551,9.546735,9.744519,-2.903176,-3.392413,5.265930,-6.806576,2.410012,9.885310,2.443975,-3.396802,5.950886,-8.359630,-1.794885,6.554261,6.283822,2.089044,5.298596,-3.839971,-2.845920,-9.045209,2.528587,-7.499304,4.020929,5.101477,8.082048,-1.499257,-4.291897,6.936417,-2.385394,-9.004059,-8.454923,-0.893454,-5.435680,8.566228,-9.343214,-0.848348,-6.327015,-1.269418,-6.608956,4.488004,7.325220,-7.239013,-9.733970,-5.024282,1.937225,4.539380,0.047122,0.323008,-7.295617,-1.188301,-1.163186,-4.294147,-8.482735,-5.839166,-2.351371,-1.550002,8.443942,8.847054,-9.183604,-2.322375,-0.477974,-4.344368,-3.653721,4.751373,-8.181447,9.955527,-4.551661,-9.518478,-2.966406,4.723311,-4.678898,7.881666,3.234394,0.610400,-2.136853,8.976152,0.517493,-2.347654,1.828119,-6.393274,-5.349553,-2.022557,2.116552,6.648682,-7.277188,1.029876,-7.542279,-9.055399,8.888670,-5.851279,-7.251307,9.716604,4.582252,9.459504,2.834559,-2.411552,4.388751,3.169854,5.398289,-2.517067,4.714060,-6.512464,-0.779773,3.936518,7.533225,-6.280597,0.021969,1.337222,9.337910,6.569110,1.824053,-3.789972,8.035974,1.809363,-4.018918,-1.904947,7.458409,-1.506287,3.809541,-2.496656,7.310049,-4.034580,-4.842575,7.898639,-9.379763,-3.167258,-4.876615,-0.153387,-0.542036,1.393796,-3.786733,6.187688,-9.929013,6.278879,2.194228,-3.323923,-4.998521,-7.201035,4.530650,3.108524,-4.098476,5.740263,-4.159713,-3.935149,9.822642,-2.403710,1.289658,-4.485073,4.865227,-8.197337,7.680825,9.416866,0.150718,-5.883621,5.721877,3.566892,0.805541,-3.876226,-2.317674,1.253663,-9.129431,7.575807,8.132979,-8.362552,-4.067631,5.758758,3.247270,5.722996,-2.523351,1.804582,3.637559,-4.221872,5.054654,3.450919,2.777313,-5.384413,-0.168621,-6.384987,2.599212,-5.826508,3.262430,6.822054,-0.217924,9.731008,-5.576063,-4.095607,0.132617,-1.606715,9.235708,0.354520,-4.927063,9.889032,8.089702,-9.328894,-0.614044,-5.236752,5.560014,-1.460825,5.613055,-6.662961,9.316702,2.074948,8.371165,9.877111,5.461401,-5.187869,-0.482260,-5.647842,2.194620,-3.197459,2.493163,7.788636,-5.953653,-4.364650,8.720527,4.592696,3.254654,-7.310202,9.485019,-7.125150,-8.898410,-1.108197,-5.043494,-0.731176,-1.427609,8.691479,-4.237518,-1.910541,-5.783065,-3.938626,0.069466,-4.753505,-5.483147,-1.019584,8.502724,1.882556,3.610311,-0.054628,-6.676612,9.654883,-0.170115,9.060180,9.785552,6.054169,-0.356110,9.482194,-0.197108,6.105069,-8.953485,-7.243063,-6.519628,6.606619,2.061273,2.332984,1.242734,-4.236867,1.501203,-3.950996,4.642044,-3.032218,4.439966,-9.580038,-1.061043,-7.082647,1.594919,-8.560212,-6.716228,8.862386,9.144401,-7.582919,9.164858,-4.156101,-8.095059,5.878335,7.137289,0.087022,2.210078,-7.484109,0.246604,6.671764,0.117014,-8.239424,0.517642,0.826158,-1.255747,2.201067,4.821061,-4.546634,-4.553233,7.176973,-9.368618,-3.591830,-6.933809,2.363995,-4.164658,-9.443137,-6.339427,1.918799,-7.147129,-3.978710,-6.999748,-1.441880,-8.143160,6.593729,-9.929123,-7.466524,-6.167504,4.096283,9.013706,-0.373960,8.191825,3.864550,-8.380310,2.597318,4.775585,3.233703,-9.749526,5.765548,4.562836,5.113807,-7.144697,-4.474417,9.453260,7.474402,-1.233576,-3.879948,4.133220,5.868213,-8.763223,-1.797494,-5.812648,-0.767746,-2.664731,5.550530,-9.991206,7.372008,-4.408139,1.495017,3.332210,-0.349371,4.456444,8.284896,-1.673422,-4.935114,-2.284344,5.908673,-6.666952,1.590313,8.982673,-5.776283,9.908256,-2.138106,5.182685,7.332511,6.755900,-4.001462,-8.256311,7.916994,-5.389780,-3.772023,-1.585219,-0.488182,3.678271,3.809240,-5.198288,-1.815497,-4.234122,-9.913418,9.543813,-8.625665,9.801666,8.229583,8.551655,2.920123,-3.843336,-9.523212,1.022639,8.240439,-0.256334,8.766202,6.598437,-6.871963,5.930915,0.227464,3.571910,6.615942,8.076023,-2.854305,9.232807,-0.497912,8.803828,-1.743381,3.066238,7.963665,4.664521,7.038211,5.405574,-5.438563,-0.120071,5.388987,4.976258,-9.885058,2.157338,2.613214,-4.213606,-3.313103,-0.009460,-4.572595,-5.173304,7.328016,5.222236,-9.924726,6.935620,4.848812,8.867440,0.966853,1.766396,7.298478,-3.187658,0.899001,-7.582448,9.395813,-1.122138,8.514249,6.327327,-2.377101,3.388012,8.316773,0.010417,-1.575967,4.293784,-3.690716,7.706411,5.956803,-9.928448,0.985705,-0.700875,-2.967736,-0.639156,-0.211201,-0.001045,-3.631072,6.561224,-2.279660,-3.115096,9.658170,-3.357347,-1.067556,7.156315,-4.053659,-9.746477,5.347462,-1.944591,-5.671716,2.797692,-0.044095,5.632511,5.364583,2.456500,-9.229070,-0.428499,8.465898,6.056789,-1.926315,-5.637884,-3.499092,-8.151653,3.261841,7.741383,-4.670532,-5.372372,2.208216,8.852857,7.899685,-8.691328,9.957872,5.005238,-2.956708,-0.370115,-1.543212,2.399314,-2.457764,-1.335887,-6.994505,6.166190,-5.818153,8.787625,0.915936,-2.892641,0.936896,-9.080836,1.000737,-5.404220,-9.452679,-1.574647,8.536825,-4.494013,-7.054742,4.717177,-1.705297,5.125552,2.920949,-9.008091,0.367415,0.304197,-8.366161,8.755955,5.358570,6.377301,7.622349,-9.165985,7.767203,-1.922193,1.930429,-1.866519,-7.313841,-3.571701,-5.402810,-4.103158,5.961352,5.467643,-7.424578,6.689464,-4.516962,3.285871,8.839205,-8.080543,-6.017964,-9.548913,-6.706487,-2.002685,-4.755018,-1.753307,3.373155,-5.368989,-2.962844,-0.665908,1.184774,7.706677,-5.267818,5.832445,-4.751103,-6.946013,-9.753526,9.438136,4.184516,2.055505,-0.837028,9.876361,-0.177490,0.196188,9.455284,3.933491,4.783859,-9.891981,-7.124379,9.367668,3.381736,2.585045,-2.885884,-4.380949,-6.994600,8.838542,-2.804616,4.089433,9.566342,3.758304,-4.591231,8.977144,0.762134,-1.614821,2.351321,7.467783,6.213883,-9.949198,5.985197,-5.241473,-1.825961,-8.865194,-6.793760,3.887079,-2.142955,-1.851112,-9.776158,5.721654,6.820100,7.594180,0.570177,5.133652,5.376987,9.895785,-5.613662,6.051930,7.840489,8.844985,5.398583,5.063698,-3.307187,-0.641881,3.852655,-6.673749,4.364481,6.642115,-1.872491,-1.032425,-1.946270,-9.256744,2.150786,6.693994,-7.107185,-5.692270,-0.482157,1.095798,6.428272,3.465639,5.380531,7.564297,2.664930,-5.395236,2.854845,1.156635,-3.709324,-6.550076,9.523838,-1.265170,6.774692,9.955134,3.221632,-4.578172,8.694168,9.943134,3.047729,6.698033,-4.674842,8.624355,-1.548067,9.224632,-9.251062,-0.241634,-7.460052,8.211528,2.893767,8.286029,-1.357720,9.274385,0.249156,-2.284661,6.557867,1.833702,3.371759,8.022721,8.116300,-1.541850,3.161985,-2.134400,-7.594663,7.655740,-3.873993,-6.956496,-1.281074,-3.491401,-9.228977,-5.534801,4.443317,2.175043,-5.523589,-6.153655,-5.899364,-2.033261,-5.050626,0.920948,-0.237812,-4.054239,0.001719,6.268568,1.954147,0.534304,3.223816,9.532883,8.639043,8.709877,-5.674694,1.734381,2.773930,-3.851665,-6.237282,-8.472858,-4.696067,-0.959749,0.628726,9.279345,2.575890,-0.947865,-1.814194,5.031391,3.672514,-4.663576,8.231494,-2.441645,9.413504,-6.372677,-0.582334,-8.199869,6.585648,-7.364029,1.035759,0.480012,-8.109788,5.709509,-7.461571,-4.220797,4.691683,0.434932,-0.475918,4.808668,-3.139902,-9.319248,-5.975802,5.227367,2.887891,-3.024244,2.671643,2.431499,-2.514687,-8.192429,-8.110065,-3.492974,8.466504,-6.421390,4.462671,4.172489,5.636097,-1.913370,7.652046,9.876683,4.114688,8.687336,-0.258226,-3.626437,9.750948,7.621189,1.543626,5.345634,2.497911,-7.174344,-5.957705,-8.999561,3.618280,3.042291,-0.050066,6.340034,4.676944,-4.717435,-6.015108,-9.727566,3.520467,1.491808,0.931708,-7.158133,-1.162845,8.986011,-3.771740,-5.611681,-8.839201,-6.898834,-6.267686,-7.643418,-8.768013,1.707181,3.171566,-4.251815,5.281566,2.798317,2.891582,1.346615,-6.000004,-0.230753,-7.994492,0.767275,-1.578438,9.390670,6.562307,-8.461153,-6.897958,-5.462282,0.111274,2.278307,-1.628730,9.034953,-8.845322,0.219030,8.160320,1.146586,-9.953977,-1.701022,4.928481,-1.682385,9.400145,-4.442407,-9.488418,8.782369,-9.587748,4.971830,7.665840,-8.978673,7.108254,6.019694,4.343622,3.035264,3.288592,-2.618798,9.623628,9.149206,-2.599270,7.389591,7.925467,-1.133058,4.542691,-1.963680,0.294792,-5.092628,9.464038,9.087009,-7.768194,-3.315101,7.125386,-3.752749,7.192894,2.712825,-6.456817,0.958026,-1.928112,6.077617,2.969322,-7.510422,-3.957923,4.466602,-5.424059,-0.988469,3.545625,-6.482791,7.600250,-3.135580,0.669405,-0.363642,-7.530935,3.249355,-3.817291,-8.436208,-5.083068,-3.611557,6.747883,-0.630118,-0.511521,-7.845576,-7.841303,-9.517862,-8.361140,-6.548186,9.175357,7.826888,-1.245989,-2.271440,4.164136,-5.553610,4.404469,-9.276982,2.720971,4.643950,8.231834,7.885970,-5.154674,1.560332,-8.504763,-5.207579,9.240763,6.000463,-5.757823,-0.156310,-0.690467,-8.407358,2.991609,-9.704479,9.482353,-1.333492,-0.266883,-6.432610,-4.894099,5.050540,-9.582917,-5.311011,2.262166,6.854341,6.047136,9.872621,0.138084,7.180469,-1.597785,0.400488,4.638732,-0.817280,6.713979,7.023794,-2.701042,1.297356,-4.263199,-2.748438,3.984805,-8.959178,7.926435,9.356333,8.522779,2.375241,-0.889524,8.834566,4.193941,9.470644,0.330710,-6.702446,6.493745,-5.567553,9.588191,3.328654,-1.256479,1.519972,0.222835,-2.497597,4.299385,-9.238146,-2.258203,-4.216914,4.540362,2.228614,-3.450143,6.677167,8.921820,3.190345,-5.804202,6.466960,-4.558102,5.597897,1.567144,-9.323349,1.807545,9.541020,2.088456,0.957185,6.361615,5.260225,-9.373853,-8.524044,-5.278270,-2.164627,-5.437316,5.229503,-3.820895,6.945708,8.694275,6.654761,-8.453357,-5.238728,-3.616929,1.343042,-3.166195,1.831892,5.990674,-7.732940,6.119190,-4.884280,2.261917,5.829337,-0.661530,1.622951,-4.788072,0.833196,3.987581,-0.546199,1.035967,-3.930880,-8.123720,6.167707,5.836776,1.609300,-0.269804,-8.777063,-2.937641,-2.764349,-5.115618,-4.766311,-1.591703,-9.427724,2.779512,9.922822,-1.485345,8.139968,4.337969,-3.682501,-3.793884,4.628343,6.731016,-8.667789,6.176682,7.341087,3.319147,7.778927,2.278354,0.261353,-6.604781,6.318840,-0.680457,-1.476440,8.830835,-9.836705,-1.958927,9.483948,-8.188632,3.607673,-1.792854,4.454033,-1.380115,4.194678,-4.036270,3.728459,8.537841,0.389633,5.823331,8.280379,-5.080616,-4.878327,9.781873,9.172712,-5.942092,-4.504181,0.131436,-7.826797,-6.191981,8.648732,-0.806983,8.615696,1.821700,-8.440050,-3.851931,-8.935840,2.879181,-3.895264,-3.955961,-8.482366,-8.127625,3.044376,1.216296,-7.331911,6.692931,-2.983288,-8.770676,5.675472,8.240353,-4.109944,9.112102,-0.230978,4.642621,6.481917,-1.680676,-6.050099,-8.723732,-9.168512,8.513219,5.580491,-4.697357,7.723605,-8.092974,3.545204,-7.752443,8.434749,-9.354862,-5.804501,-9.074410,4.143804,-8.047665,-3.872480,7.664436,-0.654342,9.258008,8.657744,2.160075,-6.723873,1.519413,6.018260,7.836599,7.847268,6.257396,3.534591,3.328266,-6.957447,9.509355,8.223896,-9.821804,8.105826,5.378930,1.015302,8.407535,-8.565549,2.714458,-5.421143,1.131158,-0.883299,-7.618022,-1.423665,-7.997633,4.127168,0.740077,-8.825407,-6.757195,9.823521,-7.144940,-8.626013,-4.338558,-3.548481,4.915127,-4.511523,-8.269173,7.775480,1.283190,0.029108,-3.816294,7.771318,6.928807,8.703480,4.675107,4.988037,-9.129706,-2.457706,4.561764,-6.783867,1.355940,6.525932,-7.663321,-6.600145,-0.064728,5.620924,-3.359525,9.532882,3.363918,0.482940,3.998608,-9.026215,7.503200,5.582697,-9.941364,0.048087,-0.056641,3.318967,5.463208,-5.507353,9.437230,-8.003170,-9.809224,5.860031,8.643677,0.754822,-0.106597,-2.680183,-2.686228,-5.423753,5.195948,-9.761176,-8.058538,-0.011139,-6.204635,4.554965,7.350133,3.587768,5.216401,7.669979,-1.660036,-3.285319,-3.224853,-9.201384,-4.476664,2.223672,-9.691849,0.903789,-9.327586,-3.808971,0.041710,-0.248981,0.233237,-1.474091,3.941268,5.508951,-4.704242,-4.166228,-8.527709,1.302311,9.593915,8.273750,4.238234,-9.754413,-1.451720,-4.395712,-2.323454,-9.907158,-6.754603,1.232914,-6.026038,0.202838,-5.767759,-7.441439,-8.358610,6.442209,-0.811072,4.137642,1.749316,4.272215,-5.040030,8.792730,8.737127,4.060762,7.811610,4.067762,1.339959,-8.177609,-0.765044,0.177479,8.310352,-6.419012,2.277808,3.691877,8.231083,-7.480565,-4.698596,-0.594135,-3.660508,7.896361,-5.111033,4.937969,-5.534046,4.052083,-1.533160,3.272545,3.139433,-9.803580,-3.013438,-4.763469,-4.608819,0.926920,-5.278327,-9.201290,8.552000,-1.968881,-7.356168,-1.641475,-4.510188,5.327132,-5.872683,-5.314755,-3.298963,-2.950143,-7.452636,-2.877980,1.270485,2.112151,-1.392081,-8.932843,2.121330,8.987059,2.831221,-0.730649,-7.252057,-5.751734,4.549644,-2.890167,1.429089,-4.361179,0.047472,4.056876,-2.091328,2.264673,-3.000876,6.801254,-8.786005,-5.267428,-1.466282,3.531180,-0.769940,1.553835,-7.510157,-4.515982,-3.112248,0.403322,2.526675,-6.316266,1.326253,-1.323270,-8.153975,-8.577595,4.289010,-5.485336,4.267920,-7.412075,1.409205,9.607456,4.739720,-2.862835,-4.458616,-0.329573,-2.395286,-3.326073,-6.736373,4.004188,-4.106962,7.389797,-2.145149,5.438740,-3.283239,-8.771646,6.269679,1.137841,7.075625,-9.288079,-3.438422,5.271574,8.635014,-5.564624,4.045039,-8.716765,5.313005,5.315311,7.004562,-9.441668,-9.677230,-9.774048,-6.212418,-9.655053,3.256881,-1.045634,2.703500,-8.756292,5.822415,-2.204583,-7.102960,-6.212949,0.379325,-8.477516,-1.195370,-3.942824,7.770702,-8.864073,-9.383352,1.583266,1.920762,6.492374,2.804154,5.298114,0.844245,3.926614,8.962244,3.008089,9.343453,2.506757,-9.886331,-5.147509,-3.401242,-3.211121,-7.786470,-8.507361,1.492272,-1.057548,0.120720,4.624116,-8.093507,4.414180,-7.677490,-4.838762,-2.432037,8.973549,0.270729,-4.302323,-1.344361,-5.254258,-6.349480,-0.355353,7.784692,-6.242306,-9.481749,8.184339,7.510086,-5.735099,4.881155,0.248009,0.060747,3.642607,1.488291,-7.610927,-1.641636,-5.724651,-9.353315,-3.306817,8.012993,-7.501634,-0.845244,-5.081015,-3.193880,5.372360,0.109080,6.482850,4.475404,8.377580,-2.408027,-4.951722,5.866851,0.771980,2.649131,9.429291,9.902827,-1.635486,2.728522,2.780382,-7.118254,8.280711,9.238646,-6.518504,8.928231,8.348708,5.117597,-1.757177,-8.359421,-6.021113,9.225660,9.317296,-6.757372,-3.978119,-6.800887,8.465054,-1.250670,4.216311,-3.530327,-7.647581,7.175718,9.674391,5.019081,8.322474,-8.552220,7.207962,3.337960,-5.230576,3.541842,2.590136,-6.054415,-9.193194,-1.520359,-0.026031,0.057145,-6.956622,8.786579,8.927252,-2.398131,-4.706061,7.337173,-3.823969,-4.526420,-0.804101,-9.409739,-7.873648,-9.016845,7.046990,-0.201684,1.535300,7.977601,-1.554634,-6.723625,6.468745,8.445389,2.237178,-6.845787,2.123133,-2.226886,-0.786408,-6.026934,3.232749,6.059554,8.835750,-8.769300,7.151072,-4.230275,-7.352965,3.574094,8.982830,-3.837788,3.197604,0.983721,0.171344,-6.520622,-8.040140,-5.535633,-0.256625,-4.432489,6.020906,-3.523296,-3.302937,6.244650,9.075724,7.502707,7.607304,3.125150,-4.628848,3.474133,-0.174122,4.873979,-9.286695,-2.823270,8.824052,-1.419215,-2.898804,1.434460,-4.820179,0.114663,5.705041,-3.605085,-4.145024,-6.420656,-2.132638,7.734161,9.133535,6.472086,-6.594301,-2.570013,6.203158,8.929389,-9.997270,-5.010485,3.764477,-8.780613,-6.884102,2.346663,1.274213,9.770420,3.552695,-0.147300,1.465411,9.344130,-4.803048,8.105587,-0.407702,6.536047,1.039695,0.435446,0.026439,-1.437090,2.519055,9.445448,9.981175,-6.164495,1.742684,9.619414,2.881231,-1.103861,2.042155,7.094531,-8.098533,-7.055486,-3.690027,-9.630145,9.974360,-7.520993,-5.710624,8.121199,-6.013934,4.901078,3.900329,6.305366,6.947764,-2.945739,5.000115,-7.664942,-4.993300,-9.015101,8.512922,-3.171404,6.549040,4.160492,-1.939215,8.384269,-2.753837,-3.721830,6.524056,-9.408023,-3.860861,0.341996,-1.368827,3.781410,-2.919311,-9.167068,3.411146,1.258180,5.318062,-7.244873,1.680042,-1.237328,-3.793871,4.093872,-8.422967,-3.776596,-5.740001,3.566269,-8.833725,0.928712,-0.656248,-6.277930,6.774803,-9.965743,-7.676290,-0.722067,-1.704627,8.408101,-5.770647,-2.872101,7.479210,7.372953,2.420571,-3.221412,5.728603,-5.842030,5.808528,1.485327,-7.923726,2.733396,1.431329,4.144155,1.562057,-3.678004,0.164349,-2.559291,-2.070504,6.888099,-3.536508,5.863054,7.076357,0.691723,-3.004258,3.703085,-0.144471,8.708316,8.196607,1.420411,7.527921,-0.772430,3.086905,6.998877,-0.878638,1.057081,4.925296,-9.463874,-9.016547,5.129081,3.832445,-6.874273,-7.009660,8.538191,-9.336806,-8.684485,-5.000390,-8.071914,7.685637,2.790474,-4.102186,7.182986,5.173097,6.571150,9.442624,-9.702133,3.154405,5.707986,-2.274138,4.600203,8.212961,4.260829,-6.017691,2.101967,1.599888,9.964340,5.667187,9.266077,3.728356,9.640635,-6.145706,5.638399,-9.844234,2.930987,8.692161,3.069033,-5.573917,-7.946412,-3.287173,-3.229906,8.127733,-2.682475,-8.402874,9.316008,-4.069664,7.469226,8.423053,-8.806182,6.280203,-3.703575,9.937113,4.076929,-8.463826,-9.870367,-9.381584,3.826159,9.573678,-0.067058,7.972773,0.112674,-2.659247,-9.513581,6.176994,2.285811,-2.838017,9.020301,6.805894,5.223227,-8.327633,6.266982,0.825180,-6.344890,-3.284325,-8.965865,2.394448,6.708648,-8.099675,2.503305,-1.427728,-6.030502,-5.699125,-6.211843,2.451830,-6.806308,-4.452702,-7.090077,-5.576250,-9.234517,0.285105,-7.526496,-2.641143,3.857807,-6.282366,-8.687398,4.541997,8.577628,-0.694418,-2.877785,-5.718823,8.412531,-0.422968,-3.311248,0.492057,8.787694,0.459599,1.252572,0.288300,4.837652,1.494038,-7.992130,-4.686251,-3.639371,-2.411163,-3.749149,8.675175,7.506531,5.182600,-9.613100,-0.792234,-1.086094,-0.020878,2.834889,-4.944181,4.527462,-4.649638,-7.937550,5.396822,6.784967,9.892679,-9.012493,5.800951,-4.394091,9.941362,4.219650,-1.879900,-8.441253,9.119384,-6.698621,-1.123697,1.118523,-1.161049,5.805864,6.316969,7.256934,0.078598,7.629103,7.908934,0.058189,8.974740,-8.723981,-1.580291,-7.656575,-7.163705,7.074087,-1.534529,2.445627,9.585237,-0.620487,7.312632,6.831696,-8.389746,2.786712,8.056851,-5.733133,-6.575496,-1.448336,3.867292,-6.083525,-0.868621,-1.934988,4.891457,4.365655,7.757520,7.085982,6.076589,0.685871,1.329915,6.196685,4.027102,8.322265,-1.700755,7.885529,-0.189695,8.925993,1.753662,7.194220,1.560234,0.142322,9.898446,7.314428,-7.651996,-4.285038,0.041596,-6.147465,3.329266,-0.716025,3.400530,-0.745111,-1.373057,-7.707812,9.847725,-1.782178,-7.519285,2.459557,-3.155550,-0.345642,8.111967,-7.341173,-0.615290,-7.245672,9.101224,8.256787,-9.372562,-7.450175,1.203647,-6.479244,4.298092,1.050262,6.539826,9.421302,1.272147,-5.305472,-8.108020,-8.214270,9.854850,-4.058599,3.560247,2.457662,8.032303,-2.362064,5.738876,-3.314246,7.339008,-1.658077,-4.882249,-9.403661,-0.244126,3.443843,-2.014115,1.073396,-7.078256,-6.010600,-9.985064,2.199672,4.473167,-5.350694,-8.726437,6.831784,4.551339,-5.075299,4.476131,8.986259,1.930746,-9.095716,-3.515963,9.683613,-7.397870,7.560369,-5.476562,-0.328023,-3.340971,-1.271418,2.403951,6.820936,2.490877,1.062360,-7.433834,-2.136270,3.296351,2.982765,9.646240,-2.564995,-9.468688,-0.966535,-5.712529,3.701103,8.728162,6.761424,8.914169,3.330410,7.357376,-3.827209,-6.913226,1.511656,1.490067,7.370386,-8.993042,-3.607481,1.384083,7.675429,-4.132471,7.083474,-2.853970,-2.400755,0.067459,-4.674731,-5.035102,-3.556639,-9.161040,-2.102573,0.905752,-6.699852,1.702641,-8.039632,6.798167,-2.469399,-2.409859,7.680392,5.083441,0.978835,-5.966654,9.935903,-9.379369,1.308527,4.665176,-0.295223,4.413826,-2.220499,-7.967788,-3.728969,-9.669256,7.538286,-0.200846,4.024822,-2.403931,-1.207153,4.366592,-7.562513,9.942013,-8.680799,5.256058,3.203861,3.802117,-0.733707,6.603062,4.136224,3.759218,-7.864730,5.685557,5.080711,-8.297365,-0.857661,2.940668,3.319991,-6.679799,-9.824836,4.133656,7.909014,2.263703,-4.380859,-6.837356,9.701369,-7.032902,3.054921,3.078098,9.184179,-1.866860,4.335672,-3.561613,-3.267687,-7.207285,7.530147,5.165128,-7.485816,-8.267120,0.560987,-7.416068,-6.127020,-7.883108,4.218443,5.583348,-5.940903,-4.621812,3.229782,-2.147068,-7.402191,-2.642350,-2.201073,-7.557128,6.927600,0.582426,7.403420,1.680904,-0.030974,9.494879,5.070566,1.724157,-0.436712,-5.278942,-4.817430,6.667153,4.637976,-2.759840,4.693372,3.929823,8.231376,2.728213,-3.629403,5.833439,5.226023,-8.299441,1.357030,-2.015454,-2.607798,1.697471,7.372654,1.348741,2.079455,0.481102,-3.064042,7.159052,6.101353,-5.004724,2.121695,2.502002,-4.608298,3.175403,1.064349,7.142688,-4.517636,-0.646634,9.588217,1.442061,-8.886752,-3.537204,8.737748,-5.083853,-5.850914,-3.459830,-4.523064,-4.798279,-5.210549,-6.406842,5.987979,7.378285,4.214427,-2.472301,3.144353,0.827416,-9.705722,-8.012134,7.660310,-5.232798,5.418043,3.311192,-0.331080,-9.120235,2.320413,-6.385177,-8.174522,4.365782,-7.715124,-4.637524,2.484002,2.490354,9.587177,0.023458,-8.172089,7.002764,-0.233638,-2.606135,-4.358878,7.244904,4.870557,6.087704,4.942338,7.484851,-6.310484,6.073427,0.175512,2.239018,-5.632213,4.609387,-6.695023,-3.404644,2.714562,-6.972970,7.620837,-3.740376,4.376454,-8.781611,-4.862131,-1.932538,-7.019884,-1.534662,-5.483760,-0.858269,-3.597109,-1.999395,-6.181742,2.595970,3.598187,-9.957167,-1.246860,3.751565,-2.592357,-5.612899,-8.223735,4.185140,0.137532,-1.198157,9.671589,-7.991562,7.221372,-3.567527,-3.097183,6.813900,5.380939,-5.777287,-5.721748,-6.621948,-0.031820,8.549466,1.620827,7.613252,-8.062189,3.004692,-9.414901,7.669940,-6.318686,-8.477611,-0.069529,-2.388565,8.264997,9.320832,-1.029575,-6.167757,-1.264563,0.573354,-3.026495,-1.317066,3.902669,-4.923754,-2.320616,6.230353,7.361556,8.593085,6.821951,-8.425030,-3.716045,4.908201,4.288174,1.818047,9.862663,0.740937,2.108193,1.336629,2.569584,6.075787,2.285325,-4.360573,-0.347528,-7.250020,9.689157,-2.285859,-4.522215,3.594224,5.377656,-7.535766,1.381877,-1.669794,2.460493,2.583250,4.841760,-1.822657,7.616327,4.889237,-8.556191,-0.591759,-3.231788,-6.007128,-3.218475,-0.551843,-9.944341,-1.749166,6.207475,1.470267,-5.426696,6.724703,6.870995,0.491525,0.332418,-2.547193,-5.565032,5.994252,1.974321,-0.642877,3.887967,0.166832,3.636824,-1.659627,-1.732168,0.472954,-0.876547,-9.835636,2.309348,9.259421,-3.124917,-7.172250,-0.565741,-6.811153,5.850349,0.331562,3.485024,7.648043,-0.617151,9.789624,4.118074,-3.920278,-7.584114,5.897178,-2.684660,-6.128205,-6.897778,5.173704,-7.388651,-4.682644,-9.996342,0.672464,-7.276162,-1.977897,-4.406774,2.508703,5.165657,3.711033,-2.444958,4.905912,5.179193,8.479939,-6.956515,-3.910503,-4.663769,5.173808,-2.516430,2.730293,3.824330,-1.094284,7.296211,2.658850,4.857675,-5.072320,8.108204,-2.741838,5.624249,-5.639611,-7.237029,1.299380,7.039950,-7.710433,1.144727,-4.770359,9.017811,-0.972583,-1.958258,1.036069,-8.937098,3.601395,6.110843,6.297216,6.731114,5.128255,-8.751558,5.491579,1.605940,-5.028136,1.333981,0.875137,4.781417,7.709407,2.357743,3.521235,6.821601,4.473057,-1.785716,5.237376,-3.961043,1.978057,2.459591,-2.098478,-2.419949,9.946867,6.740518,6.734782,-1.073494,-5.673320,7.804055,-5.677128,-5.531013,-4.500010,-6.206048,-3.129407,-3.163730,7.534644,-8.721911,-1.103542,-1.454251,-5.910458,-7.415187,-8.612844,3.829262,-2.834346,-0.635245,7.229916,-1.263991,0.521760,8.169040,7.467770,-0.225270,-8.910495,-2.267266,9.521240,-4.602579,-5.005819,4.745210,-7.381854,2.187493,-9.961307,8.058932,-1.575600,4.929156,-5.123448,1.007312,-0.552760,-8.703336,4.982113,0.439113,-5.095688,-2.130325,-6.510899,7.304230,-6.452935,5.549597,1.319236,-9.939047,-3.670621,9.707729,2.894065,-1.578862,-6.815788,-8.701883,6.009834,8.838551,9.290611,-5.361322,4.814108,-6.908812,-7.062271,-2.405860,-5.488140,1.603573,-6.886854,7.275359,6.747010,5.901234,2.716693,6.443314,8.902723,-3.326557,9.165528,-5.775251,-7.859279,-1.940438,-6.197949,-2.875738,-2.705913,3.629467,6.759799,-8.603442,-3.108708,-9.822269,7.981018,-0.653650,-4.581869,7.922445,2.162232,5.958135,9.738724,-2.539702,-5.691901,-1.784192,-1.315780,-7.197083,6.344322,3.476044,-1.952576,6.004927,6.286354,4.516989,-8.154875,7.847577,-8.663378,3.740960,1.296235,-9.138333,4.769787,-8.260890,-3.577270,0.913127,0.482803,-4.682044,-7.980754,6.151668,3.528790,-6.342294,4.299742,-4.436511,-7.514577,6.250903,1.449432,0.102040,1.183892,1.223900,-2.501037,2.474549,1.277231,-8.357861,9.761838,0.957431,-3.217626,-0.572899,-6.373335,0.103933,-7.735321,-7.436508,-2.649029,-2.933093,5.126788,-4.195346,-0.310531,2.085988,7.458636,-5.322365,3.167891,0.586641,0.378297,7.644703,-3.783285,-8.512683,-0.147659,4.550204,-2.409015,-5.941239,4.426627,-4.196728,-1.768341,9.743251,6.413907,-4.277480,4.047678,-2.586508,2.359889,-9.491991,-5.300153,-9.194492,9.181487,-9.868531,-7.201859,0.252363,8.788573,7.537914,7.119833,4.642214,-6.663870,1.144176,8.316932,-1.005893,-0.082466,3.479409,1.204714,0.252387,3.661160,2.466398,-0.791913,4.510553,-6.538432,3.281684,0.140723,-8.555331,-5.604061,9.180632,8.393884,-8.838215,1.973145,-4.642362,8.427765,6.619920,0.358446,-5.097425,-9.516816,5.442634,5.413321,-3.759522,5.316755,-4.737910,3.214315,-0.627331,-2.693494,-2.653817,-4.134529,-3.615905,-3.675035,-5.894213,-4.414124,3.800873,-0.175972,7.058116,4.747333,-6.407527,-5.685339,-5.518652,-7.922676,-4.752856,2.375092,-7.739809,-0.782678,6.475058,2.893523,-0.967742,9.645364,-3.746898,4.249925,5.708216,0.791950,2.788843,-7.116061,5.952366,-2.690483,7.274688,-3.237567,1.523074,5.591946,8.904466,-6.678964,-7.869173,4.740136,1.687013,6.307599,2.998244,-7.534882,-0.340915,-5.613057,-3.012416,-8.531960,-0.928356,1.613246,0.297829,3.700114,4.815440,-5.876515,8.855534,-2.873194,-1.684203,1.139539,4.417577,3.050351,-6.937345,7.428546,-5.852954,5.430796,2.080942,4.562254,7.502595,0.817165,-2.330073,-5.058396,-3.914607,0.585010,-5.940049,-4.586475,-0.755898,-0.879367,-1.680323,1.976247,6.105158,2.367585,-0.030711,1.046767,3.216938,-1.950097,-8.628690,9.365955,-7.328985,-0.872746,5.924556,-0.941631,-3.698000,4.655340,-8.179603,1.892930,8.448761,-7.791204,4.962945,1.764866,9.977730,3.168494,-0.778969,-4.786657,3.508773,-9.780070,7.638176,-7.132901,3.133780,-8.402210,3.839224,3.996125,4.880487,-3.037098,4.329447,3.984056,8.999966,-0.017726,-4.450486,-8.878315,2.395041,-2.476643,2.027984,-8.397540,-2.173427,0.014126,4.434628,-1.417566,-9.063803,1.816026,-2.081277,-2.954567,3.233258,-1.491496,6.251680,0.655196,5.683012,-1.262703,0.490216,3.137670,5.145708,0.062594,9.115010,1.310746,-6.005831,2.029582,-8.461692,-8.123962,-5.134834,6.137370,-7.164368,8.015618,-4.533472,-3.137185,-8.637818,-9.227775,-7.422977,-6.082650,4.917994,-6.477872,8.875376,9.440721,3.406003,1.900032,-8.549294,-4.650812,-0.680373,-9.685681,4.614920,-7.918021,-5.234016,6.747137,-5.998293,-7.501302,-2.743030,9.161186,-4.731161,7.885749,-4.254747,8.174392,7.650489,1.709000,3.166756,-9.418605,8.981457,5.214620,5.204649,-8.717253,-8.087533,-7.969379,6.000121,-3.104952,-3.207558,-3.299915,7.706647,2.024372,8.007999,-7.363927,-7.793299,5.054262,4.163515,6.387915,7.450058,-1.183674,-6.080175,-2.300164,-7.027471,9.581244,-4.349492,5.822837,2.805118,-7.374213,-8.780916,-2.419530,-0.384231,-3.101747,-4.866156,-3.788570,3.145293,0.077659,9.228512,-7.761974,2.264008,-5.428672,0.920948,4.049961,-2.977168,5.656703,-9.452026,5.323107,2.538770,-1.488306,8.639921,0.281580,3.876554,-8.145737,1.944245,-2.025020,-8.281273,-1.847259,-8.232371,7.191549,-0.357035,1.952652,-5.599047,6.077523,-1.367336,8.892911,-0.126266,9.887623,1.789597,0.411048,-3.019276,6.555605,-6.330615,-3.929487,5.744024,-5.793556,-7.112817,-4.058717,-0.691014,-5.603460,9.380644,2.768122,-4.354964,3.832265,-2.641103,-1.652585,-7.254539,-7.753670,-0.326950,-5.461632,-4.517811,2.349970,-8.727876,2.701410,4.691395,-7.947095,6.614732,-8.760687,-7.331457,1.794902,-3.810258,4.485648,-2.575500,-5.254480,-7.806383,-5.291011,9.287209,0.615942,-5.945603,-7.031563,-4.290308,-6.928087,-6.880901,4.700819,1.581418,-3.128734,2.724889,-7.321143,0.762147,-4.946349,6.620139,-4.864958,-0.295489,3.736981,-6.571978,-8.241350,-0.813625,-0.298899,1.850841,7.586317,-9.843980,3.003101,1.319089,7.131545,-0.058049,-4.225115,9.940984,-3.212432,-2.436112,-5.545068,2.665929,1.813920,8.770515,3.303403,2.826107,5.940666,-3.149671,8.761397,0.051112,-1.548474,-2.590169,3.907938,6.471880,0.403613,2.197018,-0.146860,-0.372248,-6.191598,6.301051,4.487845,-4.884164,-5.539459,9.837028,-2.724815,2.476987,-3.582670,2.269224,2.280875,7.686772,-8.086227,-5.180679,1.411188,-9.830680,-7.923842,4.404695,2.541372,1.271298,-8.047532,5.197947,0.790533,9.311699,9.666058,2.140624,8.715267,9.723452,-2.816033,-4.792936,0.433515,7.562519,-6.025077,5.115898,3.805487,-6.234707,1.728176,-0.769405,-5.543101,-7.549524,8.543310,-4.856271,-5.425135,-2.600397,2.252912,-6.806151,-3.036194,-8.940367,3.303235,-3.676114,-9.393834,-8.800741,-6.533425,-1.943081,8.384974,-4.631364,5.141195,3.071114,4.285629,-6.405189,5.713345,6.931847,-1.291196,-9.283946,1.316959,-6.933579,7.125527,1.806370,-5.756889,-7.117524,-8.710223,-3.769245,4.904226,5.886904,4.281545,7.269199,-1.752959,-0.752722,7.385983,-2.482411,7.478008,-5.935881,-0.269776,0.588341,-2.550382,-0.716331,-2.700868,-8.476665,-7.106468,-6.932658,9.729332,-5.876521,-7.667064,-5.653468,-5.686388,-8.977592,-0.822261,-9.799142,-7.482858,4.213155,-6.659017,6.497902,-2.526885,-1.880353,3.828979,-5.680106,0.550710,8.203437,-8.737187,1.525890,-9.650401,-2.803902,-3.875139,4.973565,-2.280890,2.606262,-2.453300,-6.240647,-4.699778,-6.417136,1.077985,-4.537185,1.242957,3.398421,-5.513735,-1.843923,-2.116582,6.020470,-3.587024,-3.068357,4.433889,3.829646,-8.111548,-3.650797,-5.533624,7.650233,1.211491,-8.833831,9.059731,-8.425010,-9.614469,-0.441447,-4.473803,-4.979052,7.195056,3.585815,-8.304998,-5.474395,-2.615175,-7.335062,9.419781,0.661593,0.330095,-1.184629,5.586903,-4.537798,7.439377,-3.486263,-9.062885,-8.260745,2.441672,-8.352791,-5.487773,5.693240,2.542508,-4.551458,9.069704,-4.072814,9.509381,7.548132,4.244791,7.182062,-7.110927,-5.802310,-6.383604,-1.586630,8.100620,3.743634,-2.056312,-2.231331,-4.167105,-3.458941,-5.796780,8.719677,8.267114,-7.074155,-3.537184,-1.289734,-7.139413,-2.703428,1.735189,-8.395429,1.278616,5.322649,-2.262064,-7.455907,-9.929156,-9.503773,3.717306,-7.383933,-3.613905,5.017901,-5.376235,-0.608528,4.753058,5.774890,4.205877,1.964099,-3.502535,-2.845442,-8.188642,8.564253,-4.874618,-3.511141,8.182788,-6.951841,8.806562,9.824094,6.683614,-8.985234,-1.892617,-5.204859,-2.332910,-0.874499,-1.930546,0.955246,8.063879,7.061956,5.021047,8.467998,-9.149265,-6.063432,-9.957675,-3.919766,9.757819,-6.034273,-8.055839,-9.802308,-6.783058,7.566090,4.531561,8.527276,-5.602524,-4.989165,-3.428177,-6.294030,-3.583078,1.812697,-0.432908,-7.680140,-0.815716,8.309155,6.229117,7.494712,2.885585,-3.052577,-5.518135,3.035060,-1.640010,-1.009353,-1.642736,-3.834849,4.086035,7.583402,1.033539,-5.808070,-7.323292,-6.918835,9.348468,8.032094,6.707711,4.149086,8.677183,-5.246988,9.469343,1.514246,0.744857,-3.244419,1.196176,0.588466,5.598227,-4.273956,1.321851,-4.111943,9.140838,6.154975,9.554086,-0.712847,-5.499687,4.569182,3.203315,9.785758,-1.049469,7.286727,6.038464,-1.098037,-7.415986,-9.104768,9.296614,-4.919832,-6.282827,5.230848,0.722933,-0.286045,-3.359293,0.820592,-5.431018,0.971792,-2.679580,-8.532979,6.857814,-4.769600,-9.405288,3.066463,8.815433,-9.213860,-5.267645,-7.056102,5.199695,7.865803,-8.221560,7.238191,8.379768,2.794712,5.801988,3.275685,-0.741822,0.858505,-5.925311,-4.892737,-8.374044,4.160174,2.130972,-2.676248,-8.850602,-8.018552,-8.946435,-0.508868,-6.772657,2.167086,4.012806,-0.117760,0.922999,-1.036639,9.964300,3.251904,0.161270,-3.433526,-3.068509,5.162328,-9.929798,3.136532,4.223942,-1.225177,7.902721,-2.418084,-1.033133,-2.370065,-8.178139,0.787634,-1.317695,7.030657,2.038465,-7.240988,8.665890,-5.558068,8.420931,-6.079791,3.965075,4.792676,0.172032,-0.487973,-3.797078,9.147244,7.989866,-6.886728,4.111076,-1.741052,2.920612,8.545270,-4.063231,-1.820086,5.389238,2.882002,3.885675,-5.710589,-9.161361,-3.082679,3.483570,3.767494,-9.542776,-2.220192,6.185866,-7.057593,6.759383,5.618847,-0.877350,-5.499208,8.951781,-0.500988,-4.774892,7.080771,9.031397,7.333104,8.349013,-1.585817,5.283793,3.220292,5.205064,4.904522,1.163866,-2.730514,0.085946,-5.812390,-9.917177,4.151339,0.850760,1.998580,2.963393,0.429773,8.888249,-7.137939,0.229739,-3.110499,-9.951015,1.403176,-4.006773,5.560246,-9.300424,-8.655367,-2.914826,8.329121,-8.948012,9.024835,-7.934214,-1.608087,-0.006118,-0.520542,4.864025,-0.691821,-3.234259,8.697853,6.337701,-9.168157,-5.408373,5.739023,6.067209,-5.256212,7.311157,6.622858,5.024219,-9.401232,-7.794369,7.688416,7.312418,6.919726,6.379284,-6.373975,3.256884,7.746773,-3.708979,7.596091,4.863155,9.022255,3.974048,-3.050477,1.023592,-7.616671,6.186863,1.232774,6.557429,1.392629,1.622306,5.899393,-5.568024,5.907163,7.343780,-8.232982,-0.473427,-8.089684,-7.427332,-9.774638,2.296943,-1.587231,-3.175466,0.053116,-0.319968,0.378587,-6.333244,6.447486,1.240990,1.773534,3.760088,9.321699,-2.941051,7.033717,3.887374,-1.633223,-0.902818,9.445963,-0.742119,-6.912686,9.979047,-6.667038,-7.881245,3.793512,-2.324084,9.207319,-7.668837,-9.005901,-2.426157,-0.159093,1.771755,-9.437632,0.391834,3.707123,-6.414906,-8.663443,3.168186,7.195772,-7.938958,4.907786,-5.793550,-8.267860,5.835092,0.342654,-3.954688,2.051699,-1.905361,1.563431,-9.935723,9.178601,-4.951316,-8.193744,-7.575850,-4.715257,-0.480240,-5.216554,-9.214510,-9.594003,2.962413,7.373486,5.079235,6.073902,-2.811845,0.387916,1.121091,2.528754,-4.085229,0.896899,1.432062,-9.946639,0.313485,-6.157230,7.307537,-3.573662,-6.650396,9.632894,-9.577011,0.187137,4.095978,3.686233,9.607559,8.762574,1.117436,9.715533,-1.945443,-6.376318,-3.843053,0.364585,3.628248,-3.939213,0.291231,8.404933,-8.685288,-5.470753,4.018884,6.522823,-9.308279,5.364091,1.194125,-4.313600,-7.321144,-9.479402,-0.365607,-7.168546,0.795402,7.175833,-4.659727,-2.434069,-2.260329,6.171265,9.086218,-3.983374,4.199750,5.055196,-7.127693,-3.735928,-9.067869,0.880324,-2.665165,6.709215,-5.045989,-7.136925,6.227116,-7.634317,7.294659,-6.658335,-6.344254,-6.411190,-0.622765,-4.145237,7.013051,3.198176,0.670491,-7.106034,-2.146157,3.013935,3.907001,-3.276023,8.720084,-3.478877,-9.285291,2.548106,0.652982,-8.432767,6.067783,8.100253,2.447227,-9.611768,1.672190,-4.058653,-1.058704,9.608649,1.441478,9.832546,-5.538733,3.075958,-5.479188,9.629716,-1.773990,9.338337,-4.263381,-5.295134,0.671191,7.808906,-8.156522,-3.069010,3.689459,-0.800739,8.740908,3.332916,4.651551,-9.715430,2.202011,4.329513,7.525747,0.765306,5.432621,1.131647,2.144001,-2.203720,-0.026100,-7.662742,-4.175243,-6.098377,-7.930350,0.224404,-5.586114,9.809577,5.850596,2.315813,1.932136,-2.477157,9.131830,5.646516,-6.436145,-5.951034,6.842775,3.722039,9.933158,4.687999,4.132081,4.870914,2.956117,-6.194722,2.448347,7.193989,-7.486768,-9.384465,-8.259623,-2.144426,1.013716,2.241893,-9.460386,-0.802459,3.043551,2.292024,-1.754073,-2.112092,-5.697238,-4.408097,8.461708,-2.103850,3.093520,0.433251,2.868540,0.444717,-8.688775,4.180644,3.694068,-1.370017,7.580724,4.966842,-8.135890,2.132182,-4.523302,-5.992570,-0.703171,-5.104629,4.623358,3.012717,2.686055,0.300417,7.948369,-7.637142,-6.970264,1.757223,5.408706,5.028670,0.638581,-6.906016,-7.969638,3.164618,1.509311,2.331818,9.091144,3.465655,0.826356,-4.376992,9.009926,2.558100,5.724927,-6.979845,8.328444,-5.270826,-1.537440,1.804832,1.974498,9.517454,-3.087694,-6.134693,6.064313,-6.628111,-8.207871,-1.844874,-1.760824,-2.042066,-2.395467,-6.721397,-4.208044,-6.702595,2.742963,-8.199613,-1.515851,1.345695,-5.289299,-3.248217,-0.186052,-6.516738,3.745398,-1.079607,-9.882634,2.049250,9.648818,-5.598720,-0.894459,0.292898,-4.219934,4.089960,9.943446,3.884636,-0.927028,-6.458435,3.111947,9.986257,5.859690,-1.594107,-9.991433,-5.885400,7.933166,-9.253497,-1.276392,3.569658,5.517453,2.155486,2.387842,-1.784359,8.885943,-9.055201,4.360789,2.647862,-2.718936,-3.526607,-7.483138,-3.316765,2.233207,7.453018,-7.156507,7.625906,7.911723,7.237478,0.694600,-6.227715,-8.411318,9.138202,0.038670,-1.203757,-8.625054,-4.686934,7.974341,-5.580847,8.394824,-2.159034,-0.822409,5.050581,8.333423,3.995537,-5.159589,9.830132,-7.249997,-7.990168,4.505818,6.417996,4.419700,-0.870374,9.372388,-8.277662,7.778385,-6.280269,-6.142963,5.140010,-9.276028,-2.461930,3.637411,6.938889,4.023970,0.121808,-2.969719,-2.690983,-7.105728,6.857402,-4.646455,8.154387,-7.185603,7.983147,5.976693,-8.521339,8.274433,6.114434,-8.880680,2.839581,-0.273834,9.354217,6.079585,0.557757,-3.628756,4.786787,-0.761886,-3.273601,5.688579,7.490211,8.460357,-7.642705,-4.255024,7.571240,6.014513,-8.524377,8.662421,-8.473112,-1.301329,-3.875314,-8.221553,5.851606,-0.919049,-2.434045,3.004003,4.722297,9.462068,-2.025943,9.003868,5.784517,-4.432000,-7.756403,7.934948,-5.492596,-6.694089,-2.875521,7.316145,0.751101,-8.173547,4.428888,1.196772,-6.617651,-6.042659,2.338889,-7.071718,-5.950987,-5.276150,-3.872919,-0.778059,5.524848,4.348524,6.333691,1.700113,2.861143,-5.853601,-5.425914,4.635222,7.122270,5.309274,1.274054,8.683664,-1.507273,-9.246825,1.047890,7.332240,-9.199761,-5.038521,0.595086,-1.657543,9.413008,8.170175,9.653309,-0.727632,3.319442,5.755509,7.328663,-8.522381,-7.182834,-7.074911,3.090864,6.785511,6.617306,-4.673069,9.156299,1.867455,5.607314,-7.778195,7.665658,5.671411,-8.490808,3.363992,2.383777,4.103015,-4.452138,3.828976,-8.564172,2.582425,3.778946,-8.411947,2.449033,7.357056,5.893190,6.901030,2.970018,4.582412,6.435774,0.956017,-9.285376,-5.569246,5.057095,7.614089,-7.197878,2.188923,-2.831144,9.699987,1.499351,-3.153811,-8.221954,0.345605,6.685602,-6.475585,0.331396,1.891104,-2.477348,-4.362541,-1.014578,4.956804,4.837366,-9.215745,6.959722,9.199127,-8.369834,1.986324,4.359601,-9.293746,8.337520,0.266105,6.039026,-5.142370,-3.990832,0.077889,-2.450423,-7.999693,1.189174,0.463587,-8.258976,2.597424,2.254250,3.328759,2.191277,9.440708,-0.337838,7.533982,5.334885,-6.499892,-7.697566,-4.314813,-0.200130,-4.278061,4.719091,-5.167630,-9.980881,9.973297,-6.390164,-1.280422,-3.603298,-1.166075,-0.462922,-7.601473,-1.851882,-9.347387,-9.806249,1.195430,7.517829,-8.969254,-6.907817,-9.998958,-3.659864,-8.906176,-9.740749,-7.670823,-9.062104,-6.677810,-8.660523,-0.390088,8.932151,-6.841424,-9.657516,-3.978945,9.337408,-8.958669,-6.875982,1.115786,-2.786086,5.721485,-5.013961,-8.826804,1.340409,-0.603778,2.086767,-7.060326,6.630876,3.306443,-2.807491,2.549190,-2.513572,3.247216,-7.486016,-1.981531,-7.232126,7.552462,1.556572,7.674747,-3.641944,9.348822,3.798601,-6.510263,-5.965255,-8.124826,-4.641488,-1.276557,3.648442,9.381746,-4.318033,9.519478,8.989163,-4.875297,-6.035996,5.809230,8.936257,-9.589473,-1.116555,7.959713,-4.957904,-6.292686,0.654798,-2.202199,-8.252366,-9.058465,1.583176,-2.221096,-5.114912,4.626828,-1.018796,-4.548261,5.163402,-2.230535,2.972899,-2.898999,9.545802,-8.529139,-0.578103,-4.978751,-8.880230,1.747826,-0.911573,1.310092,-1.052477,4.181184,3.246287,-6.430389,-2.908113,1.193475,-4.121391,-8.965039,-7.374255,-8.364439,3.032929,8.020578,5.933954,0.132821,-1.614885,2.806483,5.476956,-7.291239,-8.751297,-1.954504,7.618548,-3.221564,1.814987,-4.196733,-5.496545,-4.694265,4.248838,9.033581,2.468960,-8.847717,3.566838,-5.362855,-4.099923,-9.901169,-5.844928,0.587358,-5.585909,2.672912,-3.910647,8.633255,1.810452,-6.356086,4.142350,9.380814,-7.901831,3.536286,6.099486,4.031355,-3.519552,-7.739053,-3.902698,-9.812739,-9.751907,-5.945879,3.214400,4.364064,-0.605601,0.689376,8.635854,-7.461683,-6.570393,-9.951230,8.436646,8.367831,0.164117,-0.796040,-9.989534,-5.825910,0.375246,8.530511,-4.878813,2.883270,8.787542,-8.043610,0.355932,-1.139561,-7.014231,-1.700515,-8.148813,6.413808,8.989451,0.254279,9.535745,-7.093235,5.884582,0.617083,-4.030743,-4.916671,-6.915346,3.357377,6.310751,3.779242,-1.320937,2.982381,-2.416252,-0.210287,6.978553,2.010633,1.043727,9.695997,7.502796,-0.441507,5.926201,4.997664,7.588016,7.737313,2.381581,3.643063,-5.121332,-9.885275,7.117077,6.565852,9.961301,9.728659,-4.772009,4.359022,-7.760300,-1.491566,-3.594140,2.255562,-4.841083,-3.436003,1.902435,1.616102,-0.793998,-0.728495,-0.990646,-0.692206,-5.169434,-9.402281,-5.452593,6.228693,4.419247,-3.477470,6.592787,5.936589,8.911766,0.548610,7.370000,-9.656818,3.004501,-9.458526,-7.069716,7.223585,-2.766372,-1.101853,3.947450,4.537002,9.336415,-4.346595,6.696738,-4.226025,2.742975,-1.864882,-1.332572,-0.725688,8.950487,4.971861,-4.813578,0.933819,-8.946881,5.318241,2.439312,-4.012818,1.883819,4.201635,-9.980725,1.607973,-6.301914,3.883678,-5.168713,-4.455479,-2.131164,-9.757555,-2.762481,3.346396,9.375949,-3.801513,-2.818316,5.960687,0.205094,-8.440536,-0.474021,6.306753,1.836035,9.886823,-9.744938,-1.724432,2.588230,9.722425,-3.466732,-7.895372,-4.010903,-9.642303,0.444346,-8.602359,-0.288843,-9.486698,-8.595260,0.739605,-4.478663,7.443565,-2.051142,9.073696,-9.876538,9.188348,-1.944194,-7.971489,-0.218226,3.189973,-1.553666,-5.587806,-0.622923,2.113243,-2.357661,0.076554,0.365122,-9.416069,-7.911420,5.720986,-0.713600,3.566553,-5.645100,6.284409,-0.364769,-2.803583,-3.231614,1.572557,-3.102086,4.224535,-9.396652,1.404244,-3.722658,2.582347,-7.425738,3.967010,-4.331694,2.890249,7.460536,9.287977,3.828368,-7.610748,6.751198,-3.255991,6.486896,-6.744762,-0.759316,7.627881,7.656409,0.410628,-8.791182,2.977526,7.745743,8.822429,7.761237,-4.802733,0.742744,5.849334,0.688888,-3.105151,2.129687,-2.872338,-1.846526,-7.365831,-9.697958,9.433334,6.508848,5.887836,0.424080,5.325558,-7.086334,5.538233,-0.528609,-7.324295,5.182722,-0.290365,1.604043,-9.482652,2.657005,-2.649519,8.306207,-2.544957,-4.844797,6.067083,-3.533608,-1.963577,4.550686,-3.066978,-4.699134,4.730126,1.083405,6.811623,-9.534209,8.732247,-6.369313,6.514474,9.622313,-4.373551,-4.421230,-2.625359,-6.970864,1.643347,-7.980132,-5.367217,-2.331941,-5.979433,2.115104,-9.188731,-1.359251,8.761347,9.566644,-7.251354,-3.239097,-5.436872,-2.618230,-8.336143,-6.560797,-1.235434,2.093703,4.883473,-8.835870,-0.517770,5.853821,3.461458,-6.878134,4.732419,-3.066783,-5.049997,-4.699809,5.506273,6.893622,-6.597993,9.049267,3.122098,0.665942,-7.011817,-2.634287,7.384780,3.439244,0.298027,-1.009371,-1.913305,-2.699096,2.808802,9.926119,-3.811120,-5.564610,-7.380776,6.722064,9.255973,8.718742,6.241641,-6.697150,3.110346,8.089424,8.156178,7.392545,-9.567263,-4.325435,5.986141,-9.243829,6.245278,-3.161560,-5.237931,1.335648,-6.083126,2.404345,-7.437504,-1.577183,-2.422197,7.422091,2.281220,6.207546,-8.780227,-4.750128,9.991236,8.544787,9.690753,9.905945,-0.568833,3.171509,3.812312,-1.902586,-1.552761,5.550560,-0.425719,-3.767602,-8.429323,-7.768859,-1.002573,-6.738071,8.249276,-0.490761,9.895282,5.180949,-1.036044,-6.465756,2.902713,1.243507,4.538748,-0.529093,9.492240,-8.186427,-4.760399,7.024718,1.551589,1.511019,7.355272,7.996254,3.669784,-2.926030,-7.903354,1.853560,1.505716,6.911246,6.596244,7.256560,6.362059,-7.091684,-0.201953,-8.156133,3.594926,-3.634505,3.469528,2.237943,-9.339565,-0.194988,-4.099794,4.783202,-7.897890,3.033937,-8.500172,3.284675,-2.433933,-0.060748,8.847739,-0.006458,-2.902033,5.607426,-5.502464,-0.921301,9.230281,8.314430,-2.234519,3.801158,-0.129138,-5.450513,7.794327,-9.962155,-9.554182,-1.670099,4.856482,-5.287955,-5.776133,0.306550,6.307723,0.503497,-1.275309,-8.282453,4.639504,8.320827,-2.051176,3.333900,5.317440,6.936678,-7.743880,0.355681,-2.766139,6.368206,-8.809351,-4.844831,-8.715305,-1.769982,-6.853354,4.928618,-6.363190,8.057875,-4.471273,5.670351,-1.264566,3.657978,-1.434161,-5.951312,0.765763,9.107530,-5.096277,9.481800,-8.865826,6.046453,-7.627814,-1.240499,-2.745846,-5.380463,-6.065570,-6.447129,-2.265215,2.821370,9.991358,-2.466835,3.972456,-5.009178,5.107036,-9.207101,5.093806,-5.849456,-4.078156,-4.853182,8.651120,-2.811012,-0.632113,-8.701350,-6.121960,-7.039890,-1.774284,-8.736895,-0.880476,1.852022,-6.240485,7.199052,-3.377241,-2.377593,6.055273,0.810271,1.987307,-4.996223,-1.550445,-1.258641,1.508681,-8.524625,3.397725,6.097235,3.158735,5.333680,9.868512,1.880864,3.583449,-7.604225,1.806641,8.673566,6.203298,-9.047466,-1.663310,1.325997,3.186413,3.218124,-9.750962,1.595606,-0.360825,-1.646693,4.415429,3.934518,1.400929,3.625901,9.045615,1.611704,9.067359,-0.520532,-6.211599,0.871667,-7.515343,5.113995,1.965892,-4.370593,5.453007,6.488174,5.398935,7.145960,9.096348,0.872314,0.504570,7.503165,-9.606635,4.513780,2.026205,9.848004,4.464701,8.311270,6.690324,-0.048031,-2.692076,3.769088,-1.614802,-3.734351,-0.507347,-7.635967,-3.440523,-9.279298,-2.083709,2.820890,-3.786377,8.303702,1.281200,-0.376226,-0.548667,-1.763405,9.121630,-9.881075,-5.726485,1.915677,-7.987986,0.378475,3.407815,-6.979974,4.870263,-3.016960,-0.764195,7.567885,-2.051123,-5.920018,9.701144,1.487363,-4.363926,-7.686105,-3.734684,3.902516,-6.653006,0.844620,-6.714510,8.045461,2.808373,2.513279,1.838925,-5.738508,1.753671,-9.749259,4.518334,0.644652,-0.061343,-8.135363,0.237376,5.254256,-9.483211,0.584004,-8.887904,-8.920246,-0.731292,5.713326,6.735676,6.338370,-7.156684,3.721329,0.325067,-4.155366,-9.601998,-4.397332,-0.735328,9.374390,-4.095650,-1.570464,2.070154,8.412632,-6.046674,5.318820,-3.905836,-5.672583,3.380378,-3.431625,-5.037609,-6.858382,4.875155,-5.001784,-1.006722,5.597702,5.154538,-2.155742,-3.688516,-1.406878,-8.053224,-3.632077,8.249475,-1.465965,-0.691323,8.716980,1.415108,-6.849896,7.262344,-0.921668,-1.813965,-5.105473,3.426973,7.304723,-8.058959,5.464485,7.278086,8.098820,-6.378255,6.684836,-2.671158,-7.118230,-9.684229,2.973058,2.527875,-6.240310,1.905023,4.042935,8.569568,-3.377692,9.223896,-3.849441,-4.757799,8.173568,4.192701,3.535156,0.587480,6.471477,-1.329727,7.292610,0.201811,-1.523324,8.586605,3.629697,-4.731594,-2.767360,3.424946,-7.818247,6.149200,3.716229,2.246696,-5.582163,-3.833778,-0.152836,-0.575237,-5.788462,2.463131,-1.634930,0.756640,0.277495,-5.059042,7.246606,7.667037,2.693565,3.218136,7.802779,7.661559,0.343900,-6.851928,6.346764,-8.514836,-0.056944,-5.164045,-1.544107,-5.380759,0.837271,3.333854,8.565765,-4.329222,0.636564,2.254574,-1.590589,1.801729,-7.043232,-1.146774,-6.281058,5.628002,-3.137789,-6.408313,2.260020,4.435184,5.003663,6.537456,0.749677,6.976092,1.081852,0.262540,2.098347,-8.477000,-4.718397,9.486152,8.818558,9.440350,-9.883036,-2.482632,7.066742,-4.655727,-8.542441,9.865026,-3.456935,0.416471,7.966346,6.026101,3.982737,-8.184932,-7.839901,-3.673499,-9.976088,-2.542513,2.269265,7.511258,-6.697306,3.805106,1.949857,-4.460796,6.548413,-7.853874,-0.131840,-7.249570,4.302842,-2.151132,-7.138426,5.193825,-1.668876,-4.141852,-4.982533,-8.929653,8.344809,4.211887,-4.485249,-7.519031,3.776950,-7.824680,3.188791,3.160047,5.784621,-9.234593,3.670648,8.952333,8.668004,4.085952,4.137401,-7.683111,-6.691525,5.209004,6.721526,-4.216365,-2.460342,2.908578,5.305441,-9.840709,-5.411742,1.830027,-9.793194,1.450319,-5.526201,8.380152,1.522965,-6.122707,-8.028557,-0.576415,-6.438959,-9.188874,-4.198754,-0.529624,4.078508,-7.723332,8.760900,5.084331,-7.353014,-7.741307,6.167431,-0.442894,5.110440,-0.123035,6.791386,-4.490999,-7.908586,-5.582258,-0.239720,-2.792617,-3.993459,2.239657,-9.893640,4.707751,0.959179,2.308997,-4.417006,8.196802,7.980709,4.551597,4.373979,-6.160163,-5.907156,-7.697200,6.034881,-7.017156,7.916219,3.340894,-1.197744,6.196105,-7.149216,3.920125,-7.755974,8.278397,-8.910758,-5.902585,-4.256048,1.405732,-1.544086,4.795159,1.920489,8.134023,7.170005,-0.939156,3.904374,8.945589,8.909377,-2.658908,-1.079847,9.731815,-5.298093,-0.013584,-6.949446,-6.201089,7.798890,-7.466123,0.519027,8.535223,-2.239429,1.537945,1.349391,-7.698289,1.175840,0.321569,-8.143385,-1.826380,-1.297759,9.027000,0.071961,3.930048,3.979402,3.659506,7.691341,3.626441,-3.592566,-4.780753,6.987648,-3.605932,8.961979,-7.119703,-8.109487,4.222349,5.372620,4.143215,-2.043621,9.063354,-4.554191,-1.315713,-9.492536,-4.169555,-8.340028,-4.166361,8.893167,-0.236907,-6.551369,-0.887038,-0.588941,-7.278585,-5.204948,-5.198422,-9.992733,-0.141080,-8.630341,9.885921,-1.914306,9.052447,-0.781227,-2.907353,7.797097,-3.533197,-7.246692,-1.421331,-3.765290,-7.177754,4.939505,8.956325,8.306038,-5.823373,1.933992,-9.109715,3.033298,-2.419564,8.164829,3.353387,-9.477599,3.873822,-3.146172,4.309317,-7.165527,8.697312,-8.609678,6.516349,-5.587938,3.500055,6.569902,7.899441,6.966606,-7.770112,1.538112,0.352841,-7.652818,-0.327787,6.108034,9.497858,4.241749,6.092998,-6.964629,1.711074,-7.917127,-9.859849,-5.901659,3.134785,6.197706,5.981378,0.533327,-6.971895,7.602142,8.225585,-6.439789,-9.706135,6.175133,8.955005,-6.632891,6.382746,7.730648,9.764660,3.038739,-8.629898,-6.808160,1.586255,-5.968200,6.212251,-6.945924,-6.574910,-7.723547,9.036871,-9.958267,8.020182,1.310646,-4.942611,-5.599829,3.111920,-0.271267,-1.071454,1.960233,-5.742441,-7.653986,9.348108,-4.057056,0.642141,-5.543316,2.187961,-5.324261,1.590238,1.312895,-9.521298,5.739560,1.743909,8.584594,9.143930,-4.970567,4.596616,2.412942,2.675530,-6.073934,-4.982715,5.894138,-7.058921,-4.314183,-8.555384,3.646605,1.332103,-2.164063,-5.903770,7.779680,-3.141046,5.212883,-4.119147,-5.407997,0.088625,-0.377240,9.347548,9.295290,3.335436,4.188364,9.211643,2.210676,-4.118217,0.721812,6.333625,-2.325008,-4.951871,8.088933,-2.660095,5.943961,6.783078,-4.959058,4.558008,-1.683750,5.260134,-2.932162,-6.988715,-1.103493,3.780965,0.335506,-7.062790,-7.993413,3.532597,3.651854,7.025698,5.365179,-7.899831,1.998123,9.657922,8.052791,-7.637095,4.264828,1.199845,2.482283,-3.738468,0.337179,-1.922306,3.034834,-7.199942,5.814523,5.405556,-8.036409,-6.123818,-7.937238,2.769991,3.806398,6.684411,-8.486573,-8.208710,-4.794653,-9.119829,4.928840,4.223735,-1.701241,0.396108,-6.631845,1.414335,-4.526157,-3.823745,3.805937,-1.051015,8.371254,-4.872144,-5.541479,6.837748,2.342750,6.473657,-4.363419,9.566692,-8.416208,1.485329,-4.079986,2.102461,-8.446250,8.629064,1.167100,-9.385609,7.667335,-1.202502,3.012422,-7.291077,1.228531,7.622681,9.016239,-6.719662,9.646608,-7.821882,-2.731297,9.789621,5.806954,7.409872,-0.260877,-4.860245,-9.923647,-6.537518,-0.834377,-2.505241,-0.700185,-6.921246,-0.231370,8.838051,-1.731594,2.108841,7.427696,5.410775,9.064395,7.207426,8.614677,-1.529476,-8.915497,2.583302,1.579715,-4.669199,-7.590357,4.563940,5.645838,-9.727923,-1.664105,2.514639,-0.101640,1.498953,5.562861,-4.914603,-1.786635,-9.034154,8.718033,3.296811,1.360392,-5.317633,-8.425689,-1.013715,-1.652290,1.090533,0.487922,-8.454851,-6.590193,9.406299,-1.464784,-3.682180,-7.461092,4.069175,-1.128636,2.413125,-4.360295,1.650922,8.371832,-0.242467,4.483123,0.152121,-8.285555,-3.437396,1.165991,-8.981207,1.480664,-8.899000,3.124339,2.028766,-0.085840,5.122446,-0.208058,-9.373378,6.281552,9.434950,-7.862193,3.951784,-0.446037,5.398391,4.503683,5.259209,-5.366258,9.174447,5.411995,-9.576828,9.269061,-5.530721,-9.422639,7.618705,-4.844927,-6.449640,8.682603,9.625278,-4.494039,9.117117,1.404954,-5.698417,-1.179701,8.952246,2.565815,-3.935839,-2.832084,-4.339580,0.342108,-1.425052,3.318274,-1.353734,-1.401132,-4.061893,4.629178,-2.868770,3.075800,-2.552249,-0.993775,8.386006,4.149561,-8.675057,0.922672,8.935871,9.456482,-0.527294,-5.657926,9.946300,-3.721002,2.882755,-1.019382,-4.457811,9.676454,7.020223,5.457862,1.492813,-6.510387,-4.267786,-3.381816,-1.357290,6.897604,-2.711376,-3.183131,-9.791260,-2.833565,-5.730366,1.003150,-0.485832,5.071085,6.257359,-2.468313,-3.305059,-2.290896,-6.676976,-9.772032,-6.545452,9.858122,4.688871,7.386281,9.428977,-5.964523,-2.005684,-3.690819,-5.333411,-3.013087,-3.891144,-0.940943,-2.551909,2.894530,6.056855,0.383676,8.508957,3.969112,-8.442332,-2.231328,-8.501763,5.103242,9.180970,7.446155,-3.474379,9.118366,-1.195836,7.769072,-7.208019,-7.499034,-3.071494,-2.213597,-0.641542,-4.317884,-5.714167,-1.264298,5.496728,6.612256,-0.487103,-8.892547,-1.776761,2.709565,0.151966,8.715435,-5.972593,-3.333022,-6.665095,-1.007213,-5.836740,8.382791,-4.151357,8.298854,-4.585488,-8.481051,2.346813,4.209964,-6.374971,-1.178220,5.352084,6.718304,7.109380,-7.014402,-4.195032,6.124515,9.386068,0.834583,-9.288859,-2.343547,0.338752,0.185001,1.381624,3.719958,-0.429610,-3.891991,4.992599,5.494441,8.185142,-3.290877,-8.401483,-5.198698,9.937454,9.339014,-5.016576,-5.154070,-3.271732,-6.116934,-5.172953,2.899298,8.718907,-3.205870,-2.954698,-4.541956,8.122052,6.231537,-4.773283,4.143645,-1.715957,5.148054,-8.780137,-4.421623,-5.085857,3.301322,-3.396801,9.112543,-7.411075,5.244471,8.091679,-4.855181,-3.452259,-3.042564,2.110756,-6.960389,5.244339,-9.684412,0.437531,-4.640743,5.018537,-7.779987,7.850004,3.734781,8.198810,-1.079235,-4.558768,2.792711,-5.882602,2.887695,-1.071095,1.193287,-0.020143,3.389872,1.504077,7.701142,5.259036,-9.044758,1.661706,-8.827805,-8.391698,9.786377,2.484550,-7.486839,-3.327164,1.364774,8.681899,-3.689174,-3.405094,-7.691066,-4.789584,-4.028601,7.520610,-8.714214,9.469097,-5.834029,8.838613,-1.754327,-4.982500,-4.502432,1.900190,6.109395,7.158382,-4.928027,-6.574964,4.039396,-6.204017,-5.069346,-1.878344,-3.366508,-6.526142,-2.678361,-1.837752,-1.961902,1.505197,5.464263,7.668207,3.137589,3.966603,-7.292154,-5.541918,-9.852344,-9.842410,2.174130,1.441647,-2.909602,-2.341313,4.114529,2.533392,6.826987,-6.876182,0.501938,-8.605319,-4.708423,-4.778751,7.097670,-1.534001,9.110420,-0.467191,-3.733620,-2.838086,4.838285,5.040692,5.106773,8.541689,4.330529,-3.660036,3.752698,4.768706,-5.400954,-1.492402,4.638030,2.199565,4.717388,9.896229,3.233762,-4.582915,-5.420417,0.868606,8.441151,-3.022940,-5.921588,6.700245,7.012327,-4.961127,2.877826,0.176197,7.924518,3.270736,7.096155,-0.199823,8.846614,4.961742,-0.817367,3.019437,6.199343,-6.791634,-3.470075,4.225532,5.597166,5.060235,1.768471,9.588398,7.056671,2.920642,1.632913,7.173581,8.958303,-9.673620,5.797871,7.133540,0.587061,9.689088,2.554535,-3.541562,-7.644184,6.962507,-6.936942,-3.937496,-5.353848,-5.978077,-6.820244,-3.703446,4.029268,4.609357,-0.096302,1.117908,0.520588,-0.362057,-7.545126,4.812181,-2.614950,-1.169696,4.366447,5.256250,-8.113607,5.719879,7.670931,-4.907620,-0.341835,-7.945450,-7.338192,-4.631436,-2.073194,2.618424,6.085772,1.023636,1.863076,1.104149,-8.910144,-7.915281,-1.155954,7.348264,2.375914,-2.287921,-1.496058,6.954602,1.743768,-4.616393,-3.636079,-2.090831,-1.952090,3.020159,0.849809,-2.301648,1.520352,-0.549177,-0.656358,-3.941716,-3.689003,1.473864,4.609527,1.250914,-1.896626,-4.428025,8.103828,3.679462,-6.684889,-8.278110,3.312535,7.598378,1.723902,-3.286207,-7.058611,-3.982304,-2.490031,4.559398,-3.284117,-4.950960,-4.608550,8.319679,2.070718,2.299046,8.870030,2.625640,-3.187412,-9.119846,-0.188311,5.261857,6.611535,1.295789,2.488428,7.949560,-4.889260,-7.121096,-8.228493,-0.082894,-1.910425,8.597998,2.033201,-7.077685,4.540483,-7.936460,-3.273357,-5.155717,8.618904,1.759203,-9.982284,-3.746883,-7.161771,3.586301,-0.558264,-3.538642,5.916457,-1.630788,-6.987222,-2.417961,3.768462,2.123875,-1.687712,3.510351,-6.757965,-0.186228,5.659503,7.606298,-6.246502,-2.399621,-9.297255,2.453275,-9.039573,0.381327,7.057951,3.597120,-0.378684,-3.444748,-9.521541,-0.477167,-7.614173,-5.637168,3.683855,5.986722,-0.736106,-2.480965,-0.844245,1.227466,3.158125,7.014246,-8.577421,-8.393900,6.319905,-3.078212,-1.313049,-9.638771,5.858112,3.767946,-0.126768,-5.072329,-1.239227,-3.129669,7.823129,-5.532304,-3.650250,8.709731,-7.665122,2.493021,-9.689245,1.442372,-8.501775,8.130132,-6.360457,-1.665051,9.193942,-7.776358,7.886557,-3.145806,-3.098458,9.448096,-2.829094,0.475190,-9.554196,-2.411273,-1.130838,-7.256420,-8.100158,7.308714,-9.467837,1.249222,-4.711685,9.807654,-8.741614,-5.897810,-2.625715,5.345722,-5.494371,9.286536,6.412751,6.354496,-1.423995,-2.536346,4.091777,0.282945,9.966765,0.771008,-5.337024,5.806932,-0.379629,2.248186,-1.999483,2.847921,-9.959715,7.840558,4.815397,0.486646,-0.345733,-4.256634,7.070194,8.770866,-8.368073,1.397061,-9.071207,-7.759472,-7.002300,8.477624,-1.088300,-9.530425,-2.952090,6.477805,-4.202968,0.593993,-0.065057,3.684341,5.660260,1.985876,8.173583,4.235768,9.133133,4.740745,7.342393,-7.836175,3.763706,-5.550588,1.829151,5.013961,9.095855,-7.611327,-8.207296,8.703830,5.124566,-2.242991,9.721846,-4.493413,9.368625,3.281953,-6.772010,-4.489194,-2.481064,1.901702,-9.550116,3.194409,9.193699,-0.624510,2.967473,-7.011107,-7.161687,-7.167309,-1.052531,-6.937553,-0.275647,-5.627782,-4.500743,-8.255284,-7.186113,-5.886133,9.370749,-7.240251,8.321586,-6.885100,-0.359758,8.525306,2.870926,3.120606,-6.825088,3.668961,1.675156,-6.158241,0.786126,-7.281526,-9.334340,-1.130654,-1.716603,4.414220,6.509964,1.927352,-2.576037,-2.961872,-3.647784,9.557313,-4.718637,3.740319,-0.672353,7.891740,-3.474134,0.152997,-1.718849,-9.070497,-6.638106,-3.967982,-1.820255,-3.465147,8.784873,-7.639644,-2.278195,-0.603944,0.549967,-8.003531,5.691669,7.200701,4.562941,9.898075,-5.719974,-9.626330,8.355955,6.747266,-0.482245,-8.765648,-0.954416,9.633077,-9.516257,9.991757,5.800019,2.620941,9.630821,2.713642,-7.990710,-3.892758,-5.519090,8.459416,-0.847094,4.732717,-3.163249,-9.028913,2.581396,5.921894,9.716838,7.043807,-6.933990,-6.718358,7.731515,-6.948292,-2.583383,-3.767750,-0.881805,-2.674363,-4.582251,2.595330,5.439455,-2.424187,-4.402142,-5.422558,-3.667261,-8.326856,-6.649113,0.904537,-9.532730,5.449989,-8.326985,-7.657032,-8.138152,2.154982,-2.283676,7.697549,-8.094192,-2.516749,-7.778265,9.615878,-8.333122,1.582945,-6.967505,-3.883994,8.106487,5.025638,-4.943131,-2.393386,-5.376649,4.456349,-3.958683,-1.289746,-8.222290,2.416489,6.617049,-2.210358,4.837578,-9.576795,-9.212316,-3.197554,5.028900,2.171247,0.156108,-7.244924,-4.217212,1.427750,-5.925413,9.718846,-9.377460,8.671761,4.980145,-8.591087,-8.775930,-1.621788,2.940613,-6.723342,-3.355142,-8.396839,4.160752,5.309093,3.180134,-3.524425,-6.360194,-8.637649,2.018142,-4.854833,5.512594,7.097625,-3.061764,-6.777004,-0.493961,-2.307658,9.939707,4.726067,7.208243,-5.752627,4.692566,-9.911292,-8.589978,-5.084347,2.665208,7.223285,8.593300,-6.558761,-3.670897,-5.299765,6.898915,-8.471435,8.696014,7.484281,-5.830730,5.475380,-8.113547,-2.110920,2.755122,-9.484346,7.680971,8.618247,-4.722631,-3.374987,0.352889,-5.618999,7.833409,9.944507,-7.697892,2.087543,-3.188667,-1.009709,8.761741,9.852905,5.365455,5.104124,1.760046,-7.285442,-9.562844,6.377995,7.193678,-7.520479,-2.840431,8.781447,-4.332937,6.035480,-4.564039,3.783641,-4.570388,-4.139452,8.097664,1.036637,-1.520994,-1.198181,-9.748165,-5.236835,1.897447,8.030498,-1.732002,-0.740792,8.055062,5.714532,3.361336,8.548049,-3.465063,-3.950590,4.311607,-2.976228,4.988659,-1.850969,-4.655752,5.631346,2.531961,5.620502,1.042951,-9.844356,-8.461052,-1.116229,0.013296,6.940127,5.378112,6.700796,9.083314,0.439241,-1.379330,3.315318,-6.934700,9.326932,7.385487,-1.400905,-8.961584,4.504918,-6.248855,0.060765,-8.718065,2.489323,-1.233619,-4.866387,6.098675,-5.053086,-2.586197,-2.474918,-8.023531,-9.012222,9.648195,-0.385770,-2.176071,-7.074871,-7.649893,-6.043704,-7.369486,-4.071874,-9.975038,3.756008,-6.456331,2.454942,6.285720,-6.401661,4.686825,6.615912,3.815160,6.057148,0.933671,-3.467561,8.364346,-0.392322,0.087950,-0.891700,-4.086984,7.994517,2.295660,7.394467,-0.896761,-3.632657,-5.983907,-0.035890,6.322828,8.130683,0.188849,-4.698475,-6.006404,4.628844,-8.498145,8.133152,9.040179,4.512300,-9.757207,9.483242,-3.642462,-3.920789,5.850684,-9.908178,-5.338823,8.676639,-2.130427,-8.842616,2.026742,-0.374758,3.968193,-2.832468,-7.176305,1.597503,-6.375474,8.213491,-4.522266,3.373740,4.824931,7.818680,-4.495050,6.786639,-6.598058,3.963915,6.373236,3.626177,-5.129052,6.213859,-2.373699,9.150647,2.201184,0.528922,-4.076004,4.647701,2.186527,-4.112512,-9.822007,-6.638590,3.969309,-5.032738,6.644315,-7.498053,2.308097,-5.232574,-2.964839,-0.051822,-1.743252,-9.979567,-5.629442,-0.597269,-4.328735,8.008316,2.667052,0.800838,-7.505295,3.849828,-0.559245,9.044410,-3.888237,5.994728,9.862809,-7.327950,2.412901,-4.299780,8.820839,4.281883,8.298680,-9.743300,-3.613398,-1.289980,0.493467,-1.506661,8.273371,3.747279,9.761428,-6.673086,-6.602492,2.481986,9.947037,3.940064,-5.435851,-1.085747,-7.139360,-5.625263,8.826082,5.197171,9.787787,-8.551438,0.507218,-3.078069,-7.795607,8.478540,1.742210,-7.361441,-8.782937,1.581700,6.964317,1.205624,-5.567323,-9.469006,-1.336283,-5.850921,-4.349387,-9.091000,-4.984742,-3.940209,4.618706,8.145694,-6.161772,-4.002634,-0.025254,-8.604903,2.601263,1.550467,1.233934,6.239831,4.699531,8.176764,-8.870099,3.196339,-1.889592,1.157905,6.198667,9.097916,4.928672,-8.115739,0.555000,7.632229,-1.797475,8.931295,-7.274298,9.735819,-7.237257,4.590490,-4.340493,-1.645857,9.990721,8.015365,-6.645368,-5.325465,-6.939157,6.526828,7.180190,-2.562587,5.494272,-6.235541,7.997448,1.691608,-2.239469,-3.662234,4.853808,-6.785109,5.809054,0.510793,-9.624583,4.317076,9.903427,-0.072420,0.603971,-1.500695,-3.448379,-4.210730,4.098552,-6.760920,2.064053,-3.346397,0.494915,3.923877,-4.285092,-1.422555,-2.815193,1.139051,9.926222,4.645452,7.193765,5.699005,-8.049477,9.374297,-7.089561,5.626247,-6.471716,-0.898514,-4.233592,-6.750108,1.879398,5.831567,-5.209826,1.806122,5.552108,-3.806817,-5.408549,-0.246475,-1.375685,-1.901089,0.479937,-2.415008,-9.453880,3.859362,-9.568626,8.875811,0.232262,8.713297,-9.031339,7.187721,1.060137,-5.283302,6.704343,-1.530856,-1.692184,-3.317532,4.109309,2.707190,-0.144956,-1.568114,3.416609,-1.933290,0.022126,-7.043530,-2.787381,7.414000,-8.693848,8.695326,-8.692160,5.785740,4.429969,2.719647,-5.625341,-5.414151,2.831634,5.768062,-4.002861,8.690698,3.824560,1.962911,5.219360,-8.000791,-9.915796,-2.945142,6.874624,9.746324,2.489332,5.816709,-2.519891,-7.428063,3.963449,-6.510481,2.373274,7.175759,7.456865,-8.521472,1.968082,-7.118676,5.915304,-2.329768,-7.986241,0.663237,-3.450836,7.797921,-2.205910,6.609236,7.266647,5.088287,3.546878,-1.238664,-2.804709,-2.558264,2.924652,8.746168,2.050036,6.178174,-1.282157,0.570643,-4.411139,2.398180,9.919292,-8.550662,-7.367495,9.485459,-7.296350,-9.265279,1.605822,-8.067099,-5.832715,3.403940,5.366302,5.549444,2.553537,5.367092,-2.079481,-4.346993,8.111448,-3.215900,-9.458023,7.286820,1.821915,1.096762,-4.606114,2.247709,-8.360953,-3.156647,-2.988352,1.755495,7.609664,2.199484,9.040169,1.271973,-0.072654,-5.093008,6.082304,8.054213,2.575616,0.087475,-3.676508,-0.704943,7.143380,-2.636143,5.648613,4.489666,-5.432353,-6.614843,-6.311010,-6.021030,2.892279,-6.567033,6.776210,-1.962939,-5.372783,-9.790295,-0.097472,8.338607,-5.432249,0.376825,5.175273,-2.942693,6.067989,4.966906,-4.794757,-6.833558,-5.588085,-5.046190,-1.866592,3.278952,0.754481,1.294498,-4.065455,8.327357,8.876305,-1.973382,-5.329347,-8.678713,9.708141,6.877764,-8.230009,-9.853945,-3.091962,-7.194175,5.986087,-3.139888,6.962349,-4.888333,-0.147377,-1.527593,2.556801,1.654531,0.213617,5.684811,3.400656,-2.479938,3.528257,0.884490,-4.255426,-3.877297,0.076318,-5.759356,7.414857,-4.813395,-5.070317,6.776681,-2.870503,2.788109,-8.223226,-1.318179,-7.063405,8.007586,7.937120,4.369107,-4.883759,0.901447,-9.779735,9.164816,0.373487,-2.747956,-9.157973,9.356311,-8.816389,4.201101,2.124261,-0.808644,-0.556042,3.084791,-3.123009,8.325755,7.153676,-4.942551,-9.158053,2.136808,-2.827015,-6.886725,7.358454,0.774034,-0.088977,-7.873325,-0.178875,1.019511,6.474522,1.552958,-4.277584,-0.484857,7.422367,3.127044,-6.650966,9.873392,-8.458235,-2.093026,4.832950,5.616257,-5.527047,-1.098818,8.771768,7.430332,-4.971687,-5.030243,-9.213642,-1.167328,-7.529932,9.550555,-5.624368,5.452981,-1.673592,-1.695294,2.772488,-9.385341,-1.250786,-6.387522,-9.990743,-7.820039,-5.950456,8.827917,5.033646,3.632277,-0.560650,3.888910,1.858047,9.226524,-1.623656,-3.214198,-9.182233,6.662963,7.178222,-3.726699,0.235310,-0.864599,5.554841,-6.085454,-3.549059,-0.281056,4.638991,4.700574,-9.612916,-2.725471,7.045794,-5.200045,3.616445,-5.141977,-1.004550,6.976610,3.043666,6.783586,0.148387,6.244085,1.033562,-6.967611,9.097090,-5.369215,9.486651,-7.168842,7.049200,-3.387676,-8.245325,3.485241,3.357403,5.829058,-4.247274,5.998356,-5.835740,2.838832,6.476241,-0.375105,-5.817780,-7.590212,-8.874390,-4.741087,-2.537946,-2.661310,6.190289,5.944764,-3.575303,5.422281,1.086475,5.431217,3.128090,-2.103293,-7.604410,-2.900902,6.871519,-5.707179,4.193064,1.607177,6.970860,5.559883,2.191354,8.800597,1.676041,-8.109167,-0.531976,-9.926670,3.061552,-2.598710,-5.814940,-2.697373,6.745205,9.873837,1.829116,-1.856932,-3.465917,9.948244,-1.601028,-5.013934,4.797023,2.690445,-6.392691,4.853058,-5.747541,5.411785,-7.544344,-2.887572,2.371271,6.583870,-0.136945,5.998126,0.843637,-6.775946,-7.524091,8.346527,6.697577,0.979122,-4.945533,9.639644,-3.665291,7.645757,-2.772711,-7.620720,9.689926,-9.007669,-9.726094,3.687456,-8.453738,6.969409,-5.078649,-6.494172,5.359898,0.699432,2.294059,-5.161643,1.702095,-4.492054,3.044484,2.188548,-8.399623,-5.298047,-2.870697,-4.561377,0.831729,3.315402,-1.627305,-3.828035,2.197868,-5.789706,-4.186078,-2.626628,-5.455748,-9.853961,2.128154,2.731239,2.381927,-4.656067,7.524988,4.626701,3.515442,-9.405314,-6.860052,5.027635,-7.976937,-6.830603,8.426916,-6.123984,-2.275071,2.129512,8.981296,5.028612,7.157449,-6.003366,0.190414,7.854692,-8.235550,-3.939629,-2.683728,-0.418791,6.899131,-7.565874,8.068633,0.953384,8.552170,0.401963,7.738154,2.947360,7.627729,5.299379,1.936336,3.865298,-4.759476,8.953767,9.303532,6.039071,-9.861886,7.970584,-2.137941,0.729161,-0.140789,-9.388782,-7.974897,-3.511494,5.834278,-0.208298,-6.023694,-0.260189,5.397844,-2.457427,6.664779,-7.484933,0.561938,0.824069,-6.890983,4.032873,-1.024797,-0.185901,4.301849,-0.833105,-6.699970,-2.742583,-9.441229,2.181375,-9.368925,-3.835399,5.684239,6.852208,3.326376,-3.554117,-1.313191,-5.199787,-6.464225,6.083540,6.086418,-0.028675,-3.774621,-6.448867,-7.874341,-9.367944,2.731463,-3.226591,1.493799,3.490806,9.567566,-5.256035,2.155129,-4.123098,0.935277,-6.030793,0.226484,-3.229001,9.357368,-8.241135,-4.618575,-9.187668,5.743876,-6.932982,-8.646675,7.207610,-3.953832,9.546005,-7.557001,7.190917,9.896872,-0.365226,-8.157147,-0.532300,-6.365169,6.978273,-5.046992,-2.382329,8.208280,-9.487501,8.645565,0.927373,-6.696956,1.539542,-2.697743,-7.204809,-9.836960,-9.001575,-0.395985,-0.135559,1.220301,9.784067,4.159385,6.046496,9.084548,6.376574,-6.389727,-0.524156,7.615294,7.769923,-5.949439,-2.375585,8.535177,9.861401,9.428751,-0.419451,-7.255801,-3.935271,2.313193,-3.576959,-5.227315,0.796641,-9.478623,0.240908,-2.802324,0.047074,-4.630550,1.071664,-6.407565,8.967982,0.998360,-1.101747,-4.795506,1.985752,-7.318346,-9.319502,2.839777,5.249249,6.655843,-9.098773,-1.406100,-1.127136,2.235159,-3.336191,-4.539450,8.569327,3.277455,1.694081,3.884543,1.949351,-5.116148,-0.413931,-6.724923,7.884114,-3.927202,0.298151,7.362758,2.266073,1.797359,-8.548865,-5.921990,2.980471,9.107315,4.875034,-3.090462,1.952942,-0.769330,-0.675624,2.586633,-8.352418,1.147697,-0.358925,8.711771,7.875132,2.280132,-3.489895,-8.361808,8.720423,9.374447,-8.217502,-6.108320,-2.526386,8.185640,4.870345,8.319066,-2.078504,7.987537,1.048482,-6.329334,5.569674,6.867940,2.136439,-2.933455,6.076842,2.525165,7.070929,1.157281,-0.698606,-0.909217,-2.420509,9.192342,0.447883,9.885583,5.510904,2.994186,-9.759249,9.050276,-5.138471,-3.521122,2.238796,7.067328,2.707706,-2.562729,6.190194,4.187633,-5.615871,-9.896847,3.224769,9.555831,-8.060925,-5.358962,6.721614,-9.262564,5.120479,1.181418,9.158330,0.795493,-2.224212,-1.991594,-3.308732,2.561938,9.545909,-7.690151,5.731421,8.162292,7.943349,-8.828127,9.498782,-3.016156,-3.182392,4.740831,2.423780,-0.625985,7.449198,7.527687,3.929665,-9.725676,2.024631,9.559182,-1.830561,-8.732300,-5.738617,-4.125398,3.911403,-0.740982,3.144311,8.327630,-7.712754,-8.389277,4.284691,-7.346626,-3.745637,9.252496,1.822290,-3.503362,0.497415,5.705400,-0.659445,-8.182380,8.372209,6.304219,-5.853024,9.965506,-0.269324,-7.144039,6.583004,-3.059318,-2.450571,3.118617,6.302709,7.221971,-9.854912,-0.936725,8.403181,2.272009,-8.640184,0.007941,5.084465,5.031974,-8.605145,4.770402,-0.449786,0.813001,1.809779,1.133861,-2.054778,-0.898454,4.902956,8.641404,5.261906,3.786823,8.754831,-6.386104,6.040850,6.585571,-8.408351,-8.449059,-9.894770,4.690584,-0.453554,-6.469640,6.493066,-3.488660,-6.214558,0.595555,-8.626268,7.742463,3.313407,-6.094856,0.369882,-1.934804,3.440393,9.947635,-4.574583,7.569319,5.436456,-9.481396,-8.157735,5.199877,-2.431352,-9.692146,-3.374272,4.159803,-5.194135,-7.852763,3.031368,0.084791,3.274858,-2.906817,7.562043,8.271476,-2.379969,6.509377,-0.719063,2.910321,-4.325564,4.920387,8.808999,-7.334016,-8.249673,6.237672,-9.923879,-5.108390,1.047800,8.162497,6.231078,2.751490,-4.694754,-7.315405,-8.536296,-6.395091,-2.165267,3.742135,-5.361748,5.328086,-7.244124,-9.693218,2.056512,6.575125,9.585727,8.912009,4.863509,-8.491903,5.699240,-9.400452,-9.780335,-7.510490,-3.608556,-3.833519,-0.777891,3.400327,9.891475,1.518789,3.006729,2.431130,5.923370,2.969566,-4.396405,6.107578,-8.634430,3.543883,-5.402350,7.741999,6.104094,3.088684,5.100507,-9.288043,-2.751966,3.257852,-3.218097,-2.729693,9.629908,-8.845957,-6.800525,-4.279664,7.149944,6.172740,7.193286,-6.727759,5.230325,-5.452897,2.746937,9.419033,-1.984056,0.281519,1.796098,6.966421,4.809705,-1.321194,9.351434,-6.867418,-2.025832,-0.126383,4.972643,-0.591947,-8.806342,5.838393,-6.128756,6.366434,-6.858166,1.059218,-9.945691,-0.308911,3.954668,4.518230,1.214114,6.910789,-9.999299,-6.158909,2.046564,-3.253049,4.085678,6.960484,-4.640437,6.894662,6.537960,-3.557180,0.560779,1.358615,-3.448644,5.234012,-7.464099,0.772368,-1.405316,-7.221478,0.176983,9.036621,3.288728,-9.355706,9.921844,-8.922235,-1.862130,-5.226665,7.722726,-4.861728,7.078032,-3.532710,5.350706,-2.550489,8.494322,4.239571,4.754613,7.578553,3.254663,-0.791273,2.394083,7.935259,9.304849,9.971535,7.368302,-2.825394,7.528320,-6.308247,7.643621,-0.642959,-4.989903,1.566653,-3.909791,-7.516729,-4.670343,-1.653006,7.405632,9.995028,-5.982326,8.671919,2.200567,-0.350806,-1.558252,4.993775,1.798449,-9.564449,6.980983,6.084496,3.706801,8.291859,-5.593389,9.392878,3.540768,-0.074677,-7.753707,9.180277,-5.587043,-2.627571,-9.545511,-7.395816,-7.474380,6.347927,-8.414655,4.333565,-5.271949,6.577634,2.360491,-2.665793,6.809934,-1.856760,8.990818,3.608001,3.620580,-3.074039,9.682002,3.319283,-3.210937,0.683570,2.012839,-4.201066,8.733784,-6.501877,-4.178491,9.855750,7.947205,4.583591,4.448888,-0.974706,5.431796,9.827626,0.833377,-0.114266,4.848340,-5.570593,-2.682698,7.409756,-5.665365,-3.254799,-3.772241,7.506811,0.560285,-9.653784,0.005144,3.582662,-8.935793,-4.844783,5.687140,7.825391,-8.486056,1.082134,-3.289505,9.702835,-1.997895,3.518603,3.937458,2.784363,-1.094235,-1.905193,-4.252595,-5.715809,-0.955290,6.253147,7.515621,-0.606478,-5.541136,-1.944484,-2.774427,-7.852348,-8.768430,-9.244702,-0.905596,-5.059818,3.716611,-9.269744,6.055259,-2.883696,0.120736,0.227144,-4.673404,3.716755,-8.873183,2.070688,2.129054,9.208118,-6.799230,7.043821,0.985463,6.125348,-9.192610,8.542640,-7.765990,8.358360,4.907047,-7.852733,2.841332,-5.014602,4.888653,-5.208317,7.382736,-6.465940,9.349805,-6.446078,-9.423046,-8.986616,-9.567044,-5.007525,2.512906,-9.317935,-2.152857,8.790126,-0.877607,8.550919,2.997846,-8.264212,-9.750683,-7.462333,1.117556,-9.401605,-0.496149,-6.055148,-4.049908,1.772552,9.694364,-4.893355,-6.965241,7.725726,-3.594976,0.534868,-5.078276,-2.677332,-5.897954,0.225094,-2.714181,7.610160,-8.755631,6.506721,-9.745289,-7.200620,-0.130160,-4.974893,-7.931924,-6.770146,-8.278190,7.550992,7.433511,3.807443,-3.578065,6.609826,4.835540,-7.578379,6.479234,-5.282886,-4.332397,1.824394,-1.915961,-0.961536,7.724069,8.757901,-7.442628,-3.220161,-2.714904,8.479890,-0.792081,8.774563,-6.868819,2.523598,5.744923,8.574269,8.591065,4.403895,-8.851583,-6.055664,-3.525982,-4.796513,-1.545621,-6.374920,-2.985948,-8.285501,1.275758,-9.163843,1.238243,6.457142,-6.626345,-8.741847,1.703373,0.548712,0.914151,5.849107,0.725999,-6.795902,-8.322590,-6.331763,7.060966,-5.151837,8.295573,-5.743329,-4.742825,7.485685,-0.475593,-2.150415,7.276212,-9.683022,-8.081852,-8.041034,5.866909,4.652931,-3.704391,-1.895821,-0.011492,-4.432062,-5.097576,-3.129925,-4.199364,6.631756,-5.103810,-6.474079,7.693903,-6.872471,-9.994155,9.567202,-6.014548,5.945069,-1.924532,-8.249148,-7.689757,-2.781070,8.380164,-0.591102,6.611609,-7.325446,3.381038,0.850064,9.592384,-8.024181,9.231877,7.365840,8.755545,-6.977153,5.848320,-7.374081,2.621725,-3.512214,-3.493172,-4.932785,-4.875321,3.925095,7.868910,-7.262543,-1.600004,-7.451337,-6.500958,8.745998,-1.672400,0.203305,-2.053261,-1.931697,6.820890,-6.595043,4.414660,4.054092,-1.163580,4.585691,0.643316,-2.327281,1.445377,4.635725,5.677980,5.686586,-7.053091,8.959615,-0.175081,-6.783910,-9.926975,4.538460,4.528516,2.052991,7.625573,8.846451,-9.369104,1.569413,-2.015942,5.637349,5.368193,-6.827295,0.883965,7.807888,4.163650,5.373371,-4.385495,9.159833,6.337520,1.828539,5.050551,-3.783400,2.485693,4.426792,-7.560358,2.722175,8.618289,-0.776177,0.940691,2.416531,7.531238,-2.234411,7.037857,-6.124655,-5.127434,-7.873327,-8.608763,2.782841,-3.770766,-5.267626,2.277477,-9.479246,0.862191,7.635565,-0.435042,6.399592,-5.359498,-7.395383,6.523976,-2.996813,-5.563192,0.816093,3.871607,-0.489863,-2.939700,7.538998,-2.818148,-2.506486,-1.159066,-5.365631,-1.658602,-6.121406,2.124421,6.288644,5.919291,-2.003303,-0.957365,1.500189,-3.476004,5.056394,-8.578198,-5.899153,-7.548878,-8.241935,5.756197,-8.626043,-1.509930,-6.277155,3.342939,-8.358530,1.304767,-3.579505,-1.658595,-3.709865,-4.132012,0.895774,-1.685240,0.767421,8.072680,8.301338,6.380608,-1.551948,-1.359957,2.510418,-8.355940,5.923196,6.184320,3.296854,6.643190,-6.781625,1.822921,-8.699912,-2.014759,8.318770,0.685330,-7.792915,-3.519560,-5.298423,5.789422,-6.345796,1.337678,3.409493,3.148576,-6.256012,-0.438926,-9.570620,1.693828,9.484531,3.026347,0.020500,7.929376,7.449557,-6.233381,2.406299,5.369827,-8.351971,3.952876,0.321955,-4.817671,4.098995,9.400247,1.837959,-4.896428,-5.733436,6.752768,-0.966484,7.434356,-3.930671,4.267137,2.811719,1.335805,5.784189,2.328590,7.490152,-9.212556,0.482683,8.204636,-1.143909,8.411817,9.033078,-0.499451,-2.826058,9.790043,-3.571808,-2.481682,6.414034,8.752711,-7.379878,-0.322263,-3.538903,-2.673030,-3.156841,-8.357509,2.684334,5.094451,-7.020872,-1.064465,8.357729,5.210199,-3.562517,4.065692,7.989991,-2.829829,4.524444,-5.528276,3.443931,1.341635,-9.179922,6.412605,-5.300603,-7.908098,-5.919306,6.024889,-8.872278,1.408482,-0.735776,-0.501578,8.271431,2.623339,6.847139,5.558641,-7.526245,-1.556636,-5.488177,-5.381488,-2.720565,-6.750305,6.775566,-8.283797,-4.575981,-6.377295,-3.159908,3.511936,2.506571,7.321669,-9.557946,5.287094,2.631086,9.910722,6.783403,-8.271104,-2.875496,6.028947,-8.292603,2.797683,0.569999,6.374883,-8.750012,-0.733131,7.993724,2.791305,-9.415657,-8.029455,-3.717585,7.044156,6.479706,-0.469045,-2.278339,5.219990,5.480094,-8.296100,-0.334750,9.488839,-1.888631,-2.058218,6.568577,8.849159,9.263329,4.005396,9.665227,2.477280,7.657213,-6.035017,5.899247,-4.341741,-3.515812,-7.067471,4.903333,2.183487,4.017214,0.074455,5.370757,-0.243828,3.892420,3.789657,-4.158924,4.438467,-9.132479,-5.881431,-9.030110,-7.053503,2.120306,8.509721,-0.673570,-8.912213,6.279475,-3.497261,-4.955877,6.680578,4.065759,-2.638224,8.866313,2.990324,8.662179,-5.534930,-3.204047,-6.842382,6.492856,-4.987205,-3.921853,4.045527,1.624766,9.887417,-4.432690,1.813702,8.909910,8.744023,7.256384,-4.445822,-3.950231,-9.486716,1.244042,-3.726386,0.675046,8.969895,2.886814,8.675167,-6.794810,-8.006479,7.143075,-1.895847,1.473618,0.977142,-9.433181,9.607827,-6.308043,-8.113798,-8.186627,-8.755549,8.066126,-1.487917,-5.151921,2.802229,-3.972659,5.778620,1.268981,-0.002524,-0.776463,-2.188109,9.743770,1.290324,6.362706,3.831782,1.038020,0.165368,0.359892,1.908928,1.064252,4.301114,6.032359,8.881979,-1.566471,6.303282,-7.895629,-2.095012,-7.164287,1.478734,8.799101,7.456753,2.254881,9.805584,-2.720984,-0.589837,-9.579334,7.329626,2.998759,-3.357957,-7.641117,-1.139419,7.574706,-7.865754,-7.270579,-3.450200,2.133147,-4.262153,-1.292981,4.166104,7.347695,9.281543,5.296790,3.917471,9.434385,2.665536,7.357477,-9.496227,-2.983594,-2.747488,0.631271,-2.561769,2.343416,5.836880,-0.053471,-5.237236,-9.582498,2.932422,6.676543,-9.300380,3.163310,-2.885648,4.993067,1.171306,-7.697320,3.685398,-7.185989,-8.788166,-8.734241,-7.571649,-6.183180,-3.342116,-5.701119,4.755064,-5.941634,-7.839419,1.632357,7.671684,-9.579741,-4.530742,-0.993855,-4.534071,1.900615,-1.567489,-6.766742,-6.865991,-0.114275,5.056430,8.224680,-5.694645,2.307494,4.706523,6.763288,7.062874,4.463465,-5.806275,1.616636,0.165191,3.890567,8.682867,-8.247017,6.570374,-0.922868,3.558226,2.428882,-8.783489,-0.825958,5.977150,-2.344090,3.482714,-4.768464,0.322942,-7.124401,-3.273140,4.692994,7.314406,6.385810,-9.434513,-6.026270,4.314915,5.215593,-0.732497,1.963343,2.237953,-5.834100,-5.853422,1.170919,8.309216,-5.385247,4.389350,9.028011,5.321105,2.183621,-0.848521,5.990517,3.183562,2.044948,-7.673379,7.158107,-4.926697,7.122824,-2.663205,3.121893,-0.700900,5.211921,1.076818,8.031840,-7.058702,-2.254685,-2.044393,-2.025378,-0.429162,0.491690,6.112475,-7.025603,-6.018168,-7.718659,-5.029959,-8.121227,6.777504,2.285608,-5.271514,3.143932,5.742326,-0.970775,5.173647,-1.900058,-4.981899,-2.349900,-4.860112,-5.744803,-0.415277,-4.877937,-0.249184,-0.812921,-4.978868,-3.002500,-2.241395,8.844171,7.485914,5.850107,8.748611,-4.705763,0.622236,7.211891,0.716695,-3.168020,-8.761906,2.401302,-0.629279,-4.691058,0.765292,6.047048,-5.761799,8.557806,-7.079242,-9.820437,-5.465515,-2.931383,6.228438,-2.544698,5.273068,2.744220,3.651201,-4.623979,-0.183844,-9.835246,6.353010,1.703672,0.535696,4.231625,2.346659,4.734936,-7.318762,1.083828,5.934895,-6.710249,-8.478881,-6.389351,-7.727121,8.836642,1.363477,-0.920496,-4.743448,-2.287188,1.856747,9.030186,5.771113,-6.863195,-6.979404,2.561431,8.056530,-9.345079,1.131098,5.476549,1.344269,-0.527059,5.581913,4.813944,-6.101588,8.786687,4.371150,-5.222194,3.014897,-5.230441,-8.262342,8.018639,-5.635879,-7.202351,-2.674207,3.683170,-6.235878,-7.618013,7.964384,3.111624,9.111017,7.423009,-5.552128,8.384350,-2.192748,0.128240,3.344339,5.374303,7.601817,-2.345073,9.808508,1.484961,0.497658,8.109488,-6.892401,4.798088,0.293609,-9.457186,-8.297700,4.157313,-5.456851,-4.123623,2.960447,4.077008,5.013859,-9.574107,5.619149,-3.402730,5.134903,1.427809,6.090961,1.689249,8.207805,-0.837215,7.070072,1.580327,-8.609019,-9.934647,6.843706,-5.854915,4.906683,7.964975,5.489546,6.524764,-3.094280,-6.653273,7.636626,-2.504116,5.847205,4.740247,9.082821,-1.602098,-8.325362,2.488477,-3.705180,-3.131023,5.893907,2.173958,9.668165,3.164340,3.592596,9.411225,-0.300351,-8.003082,-4.311681,-3.167226,-1.024136,-7.361318,6.515246,-1.944990,9.125713,0.629406,-3.581322,4.632935,-7.498061,2.997969,-1.285058,-2.083013,9.169374,2.020524,-2.979083,8.970476,-3.315432,9.076017,3.421173,-0.484376,-1.344907,1.187331,-4.324435,4.076519,-8.571882,-3.864329,5.009932,6.170016,7.402475,6.812799,-0.760891,-1.624718,-4.208259,1.867957,3.047415,-6.248663,3.997536,1.093402,7.476158,-8.747164,5.689379,-6.150313,-5.156119,5.598141,-3.933655,1.027403,4.111159,-3.439680,-8.914143,-5.546319,9.804966,8.118966,-4.274960,-2.311199,5.511361,8.554468,2.663511,-1.446477,8.063637,-9.077757,-3.126214,0.323593,9.788524,1.082300,9.014668,-6.089889,-4.256292,2.979287,-9.212954,-4.720780,0.255426,-9.434894,-3.404126,-6.739458,3.754340,7.294802,-3.377514,1.164567,-9.668737,0.124507,-9.785449,-9.282305,-6.636589,-5.643014,7.519432,-9.896749,-9.144129,-7.264396,1.466901,4.300557,1.921293,-8.818107,3.709381,1.498897,-8.666195,3.756567,-7.015012,-6.023368,9.800684,7.963931,0.343044,0.373793,5.317587,-2.167347,-8.055274,1.412888,2.984717,-2.994070,5.053540,-1.326698,-2.765535,9.100168,-8.678792,8.632164,-4.255330,-1.913318,2.740260,1.453737,7.649558,1.203206,3.889659,7.656625,1.543919,4.845209,-4.827740,-0.076147,9.218033,7.125443,7.945628,-3.942882,-7.567460,-8.394275,-4.502523,-0.282231,0.678064,-6.663990,-1.117775,8.601977,7.424768,-2.392962,8.500145,-2.451926,-1.331085,-4.520138,7.500937,0.380125,1.256436,0.737648,-9.235868,-6.766256,6.762455,-5.419915,-2.077603,1.721097,4.865025,4.507234,6.949279,4.707120,-9.062013,5.591056,-9.491323,9.979874,-1.833947,-7.850903,-4.003164,6.665344,8.021426,6.262586,2.032645,4.740058,-7.039383,5.933306,-9.250021,-0.270075,-0.582838,-2.611342,-5.446538,7.043417,-1.756765,6.248943,-1.763709,8.805953,9.989653,4.571589,8.244045,0.019616,-0.668301,9.142447,5.643172,8.751359,-0.034366,6.388304,2.224889,6.689296,-1.686191,-2.043391,8.344489,-4.137043,-9.670265,-1.131039,-4.877218,0.931052,-8.887662,7.018291,-8.749330,-8.160974,3.738199,-7.319065,-3.253594,-1.417919,-8.359070,3.342123,-0.690336,-5.146715,9.323134,3.648929,-5.511223,-0.056176,0.032501,2.884636,-5.531513,-4.506527,8.071783,-3.631016,8.604610,-8.213010,7.624180,7.566275,6.853845,-1.600511,-0.531684,-4.379306,2.833775,-0.342298,-6.862054,-8.777088,2.999437,-3.538790,8.129685,-4.073144,-7.945267,6.892428,-4.007507,5.417091,-6.684356,-5.538329,7.914022,-9.708258,-8.957259,-5.607139,-3.701703,1.151867,1.441559,-8.614806,7.262642,1.165741,0.778098,2.596864,-8.929607,1.083808,5.097776,9.889686,-5.946163,9.495681,-4.403645,7.714326,-1.164370,-2.309065,5.004953,8.355655,6.383333,-1.627977,6.554284,-5.754737,-8.204874,-1.006418,-2.623078,2.205979,0.172338,4.083566,-5.174061,-2.862191,3.671436,-0.503486,2.551762,2.744284,1.939018,4.107266,-1.034499,-5.334885,5.174103,-1.634441,-2.602272,-0.748147,-0.069645,-2.129253,3.173356,0.098561,0.999699,2.257749,8.211169,-8.407239,-8.857398,9.437885,9.241145,5.553214,5.443007,-2.506676,3.161210,2.429882,-4.665195,-0.354748,7.927069,5.252869,-7.142844,4.366145,0.429597,-0.874212,-1.064378,-8.760350,1.457974,-5.128571,9.129602,-9.561867,-3.749963,-9.855569,9.340220,-3.672316,3.058872,-0.477717,-0.046357,8.445020,7.453574,9.909141,-1.398542,8.013377,3.063567,-3.483068,6.602414,-7.758931,-0.374993,-3.867408,9.728349,-8.267815,-5.144101,-2.707969,5.127961,7.816515,2.970847,-2.741974,-0.152483,0.189560,9.168407,6.180133,3.207035,-5.431658,-6.354943,0.120453,7.817043,-4.447512,-1.710304,-2.277131,7.836667,-1.768233,-9.545479,-8.830248,4.628386,9.467201,9.738160,5.479558,-2.742630,-3.774398,-2.943602,-0.046134,-4.887224,-9.871937,-8.205912,-4.042056,-5.338863,-8.999456,4.844840,4.145048,4.922061,6.325526,8.007345,3.643475,4.098504,6.101416,1.541931,7.421357,-6.441572,1.294374,2.228382,-5.039309,-2.259499,-3.961820,1.241606,-2.933398,-3.590407,6.318483,-8.368922,6.411366,5.704025,-5.052555,3.886374,-8.494363,9.186507,-6.925075,0.444540,-0.857952,6.530108,5.165138,-3.689667,3.024238,8.870983,1.629519,7.927348,7.659039,3.425375,-4.065729,-0.845983,-7.865943,-9.459258,-4.032822,-6.703249,3.851668,8.751651,-7.327389,1.124926,5.611588,9.606795,-2.126105,2.956529,5.987269,3.824823,7.164198,-9.963601,4.415089,-6.514595,-0.690908,-4.819984,2.235751,-3.942550,-3.701292,7.365261,-3.268023,-8.436966,-6.503667,9.969287,-6.879834,6.307615,-7.204402,8.948322,-2.331424,4.935542,-6.173998,-7.556423,2.397281,-2.274932,-1.301649,6.412821,-2.877487,-5.891760,-3.170263,-4.751456,-5.660653,-9.528530,7.140895,5.788532,-3.860621,-6.754350,-0.027662,-9.758126,7.033202,2.314783,-4.398277,-8.624403,-8.484266,8.743456,-7.687841,9.707912,6.940888,4.152310,-0.773804,-1.193553,6.463156,2.531073,-3.209656,-4.147043,-8.380663,0.709688,-5.788335,4.710317,-5.056225,4.930047,-1.070374,-1.097247,9.311688,-6.115613,-0.333387,-5.965707,5.378192,2.196779,3.551672,0.198473,-7.105951,-0.841321,0.618757,4.115664,5.620133,-3.552245,-4.728031,9.728453,2.191075,6.830340,8.962707,7.653802,9.696965,-5.992663,-2.402349,3.659580,-4.645910,-0.371659,4.468960,-9.050799,-2.543043,0.053632,9.706226,-9.861548,-2.840959,-1.759724,1.494734,0.999715,-6.087205,1.754698,4.320900,6.468370,2.486517,7.867235,-7.434670,5.028733,4.938221,6.630735,8.367498,2.192889,4.547568,5.725839,4.216910,4.339545,-7.882487,6.994316,3.081272,-3.338918,-4.597271,-2.477084,9.529369,0.790874,-4.657976,7.182528,0.452913,1.630603,-2.821892,4.247142,0.305677,9.124132,-4.255805,-7.376446,-2.055240,-5.382340,-8.198813,7.963739,-9.962795,-7.250225,3.710622,-6.123591,-5.758473,7.691963,7.106345,1.242390,7.043915,-3.910204,8.251673,-1.464771,7.589738,-5.280377,6.437166,1.809710,-0.936102,-1.498235,0.807504,-6.313085,-2.539781,-6.833338,9.811724,7.108994,6.204526,-6.596343,-4.185195,-9.049808,0.221456,5.945417,-2.655745,-2.808457,2.514704,-9.923900,3.956234,-9.239579,-7.602141,3.497256,-8.560578,-0.351795,9.864198,-4.281167,2.101906,5.139449,7.058316,7.387813,-4.040622,0.639653,-7.838014,-2.475603,-9.688105,-6.747486,-3.300268,-6.113110,-0.900586,-0.847905,6.178698,7.112000,4.309433,9.506553,7.066910,-1.004408,-4.721329,0.977104,8.198197,6.759655,9.884917,-1.324616,5.514399,-2.628346,8.366371,4.666635,-6.074189,-0.995661,-3.120740,-9.544387,-6.381603,7.513238,-0.090953,-2.350720,-4.436965,-5.669336,0.969717,7.077874,9.667492,-4.626058,-0.462414,-3.660982,-5.554791,-2.392345,-9.288009,-3.285119,4.189806,-5.500985,7.945177,1.999456,-7.486897,0.143047,-9.394606,-2.341321,-8.606067,0.197361,2.487866,4.624523,-2.257909,-6.101690,9.448295,7.124190,-5.903469,-2.337236,-8.345390,5.569072,0.067206,-1.523838,-1.317106,-9.709335,3.056785,2.082370,0.306759,-4.581342,9.316650,-3.540567,-8.054429,4.297311,7.812823,-8.657187,-5.351026,-8.986248,-1.641822,2.831207,-2.358823,8.700500,9.463273,-7.663903,-8.429977,-1.855836,1.615885,-2.254483,0.033023,-7.973767,9.770904,-0.506408,-0.489704,-7.409352,-5.870037,1.281666,5.946388,-6.638479,-2.981330,5.096224,-5.572792,-6.695534,-1.544598,1.148800,-3.787289,6.654667,-7.983491,7.801549,-1.154226,4.346862,-8.453819,1.123117,7.086974,-1.129178,-9.873713,-5.858308,-7.736848,-7.241339,1.762146,-8.581166,2.642219,-2.070659,1.758678,2.682372,2.195873,-4.254859,1.489809,7.624709,-7.161083,-6.841674,2.924257,1.358195,6.171129,-0.100798,2.114978,9.507801,-1.960332,-7.732211,7.364845,-4.245500,-5.005038,-8.911013,-2.727485,-1.506777,-4.550461,-3.929248,-0.294319,8.178173,7.734789,-6.973318,-4.039079,-2.030071,2.251628,-9.405993,-6.660690,8.745551,-7.364943,-2.645358,0.990635,4.472324,-7.265121,6.271230,3.749696,-7.172674,1.447380,7.055481,-2.503822,-7.751447,-5.782608,2.611826,2.459004,1.065164,-9.936776,7.642424,-8.930971,7.292708,-7.684864,0.737427,4.206742,-4.752242,8.946868,-9.797007,9.024801,9.327487,-1.511181,-1.784196,-0.821303,4.455624,-4.681777,-0.776272,4.106170,7.325865,5.260450,6.753735,-4.769364,3.040500,6.940062,-1.406439,-3.210828,-3.714236,-7.112652,5.804183,-0.452490,6.868528,4.726081,7.578982,-4.531921,-0.147739,-1.863575,-1.170185,4.377289,-0.222106,-2.545572,-8.107745,-4.743738,2.514403,3.283735,2.771920,3.792972,-3.550436,6.523133,7.346223,-0.080673,9.009765,3.735686,-1.345296,2.979074,4.884394,8.989350,-3.601663,-0.359042,-3.562527,-5.812080,7.425165,-3.505596,-8.265247,0.058625,2.177450,2.277233,-3.660933,2.503957,-8.629750,0.928449,-1.608354,8.875177,4.308188,-8.133047,8.860341,5.232141,-6.193160,0.678333,2.210819,-3.237131,-8.273753,3.556294,-0.842296,4.782360,8.386292,-1.889768,0.176767,4.541249,9.949829,-1.042943,-9.999024,7.064175,-6.021668,-2.666430,9.381883,-6.993774,-5.039053,0.926576,-2.587564,6.525962,2.373787,2.875785,1.152952,7.869326,-2.073988,-3.102546,-5.833562,6.653828,-6.279399,-8.188124,-6.847935,8.824607,5.398462,4.453847,-2.343332,3.877281,-1.307265,-7.740568,4.865898,-7.936119,-3.325328,9.625417,-0.745559,9.964115,-5.922201,0.952516,-5.369882,1.603280,1.308776,-4.374675,-5.668721,5.938899,-6.513594,-3.867619,-8.418866,-5.716457,8.573512,1.967498,-1.432742,-5.656315,-4.555018,-5.881442,8.196808,-0.557666,-7.960255,-6.577088,4.049862,-8.230779,7.100927,9.128479,3.873429,-7.197028,0.948147,1.301631,-2.036351,-4.208623,9.322599,-7.312265,2.458255,5.934946,6.205537,-5.204676,9.114705,-6.766969,3.651472,-8.735345,9.565622,-4.057837,-8.694223,4.859690,8.534003,-0.581222,-3.679188,4.002213,8.849646,8.103527,-6.186501,8.311059,-9.055662,7.965549,-0.845612,4.365680,-6.123091,-0.338767,5.134873,-9.985419,-0.075669,1.796664,2.514527,-1.344381,5.973875,0.797814,6.969422,6.771075,-6.500032,0.713564,1.205250,4.879411,-3.447240,-4.433102,1.406936,2.476717,3.060796,-2.844851,8.161820,-4.069352,-1.623781,3.325243,-8.042150,-8.458337,2.302609,3.172394,-6.122970,-0.746642,1.044472,-8.330804,1.594574,-6.193957,-9.308295,4.239586,6.429362,-7.817798,4.838281,8.149600,-7.901514,7.644694,8.888429,-6.663921,0.045801,5.237812,-8.071236,8.002086,6.861106,-4.883311,-1.960494,1.600786,7.192134,8.218827,1.663712,3.528858,-0.327598,8.743484,1.304240,1.180710,2.107051,3.977831,-2.596335,2.720145,-2.665229,7.630670,-7.888535,-2.264299,-1.697097,-5.558121,-4.763709,-8.445491,-7.516183,7.975164,5.461003,-9.034196,5.288955,-3.624018,-4.613435,7.087854,-8.559384,1.227364,7.326830,-3.863138,-1.116354,-9.742905,-5.210462,2.203942,-7.685500,1.149036,-4.798334,-3.581004,1.614804,8.639742,7.543121,0.334080,-2.947135,-6.284873,-2.117428,9.399374,3.294967,-9.951132,-1.126488,2.121770,-1.989264,8.282281,-9.053317,-3.297196,-3.967235,-3.518128,-8.592681,7.236133,-8.593049,-3.530717,3.431995,8.603157,0.252160,-7.407801,-6.755138,7.678346,-3.442414,0.809968,-2.096327,5.940925,6.153720,-0.888613,7.006350,-3.096267,1.467162,-5.231957,8.712456,-3.316483,6.147348,-6.150059,-2.720291,-7.994575,-9.006308,3.886105,5.489196,-5.715068,-3.044459,-5.850016,-5.630397,-0.202011,-3.929435,-9.386610,-1.595151,-9.293379,-9.004608,9.230245,-6.399071,6.849221,7.327508,-1.856699,4.611945,-8.444019,8.855599,4.668141,5.431411,-0.727750,6.996675,4.276104,3.595307,6.984176,0.607692,-4.154207,6.616508,-4.845210,-7.985412,4.715278,3.831526,-4.422097,2.806375,7.178919,3.258141,-2.102534,-6.719935,-9.349203,2.580434,9.956190,2.559896,9.019851,-5.123217,7.847247,-1.547879,-4.236310,-7.316361,-2.681155,1.183412,6.311111,6.677001,0.313726,2.460734,9.603079,3.777444,6.707965,-9.583281,0.391356,7.174751,-6.052278,-8.824890,8.053755,0.996515,-8.454634,5.167110,7.683383,7.101440,9.286356,-2.897097,4.737186,1.928658,-8.625109,7.694013,-5.069934,4.454650,-1.237176,-7.155573,-7.896988,-8.190749,-7.563652,-0.837232,-5.626740,-5.275310,2.607254,3.334380,-4.723437,3.598330,-9.294309,7.327898,0.806091,6.985482,-8.499662,-5.982895,7.288347,0.686094,-4.430816,6.575788,6.598639,-9.583635,0.600217,1.363228,0.712937,-7.658383,-7.371987,-6.766076,-0.302775,2.572229,1.360882,-4.975567,-4.578719,-0.066325,3.995603,-2.682819,9.583297,5.826003,-7.003438,2.015089,-3.891839,8.075823,3.798038,-2.226641,-1.985153,-6.936278,6.590230,-3.268392,-8.498046,2.067719,7.457069,-6.164126,-0.592017,1.566332,-2.179179,-1.406156,-5.567533,6.603325,-3.906512,-4.043991,-6.992898,-1.275329,0.882575,5.522880,-9.313274,0.311803,-5.987424,-8.266428,-7.817535,0.486646,-9.309166,8.744052,-2.767487,-1.518167,-4.042663,7.437311,6.730269,6.489549,-2.254856,-5.244542,7.888985,-2.843998,1.719929,-8.294769,-0.501622,1.849299,-2.596075,-2.663756,3.469195,4.530071,4.195560,-4.308700,-5.378061,0.168125,8.199730,1.100530,2.457235,-5.577598,4.654249,-5.720452,3.707495,-6.803385,-5.192396,-0.058998,-6.826105,-2.328167,-7.282670,-8.121848,-0.777675,0.338535,-1.606398,-9.313095,3.074710,-3.974342,9.821080,-9.223093,-2.508819,-2.220438,5.749697,3.809532,-5.132338,9.539336,-3.284144,-8.291100,4.740930,-9.367652,-2.913938,-3.300792,-5.984393,-4.792071,0.352495,-2.095512,-7.237187,0.547020,2.421486,8.231742,-5.617487,-1.716579,-3.275670,8.474518,-2.248898,7.062692,-7.042460,-3.547477,6.631657,-4.732364,-4.887196,-7.484044,-2.995474,-0.279405,-6.414317,9.035542,8.016702,-1.712034,-9.353085,7.782729,0.663713,-7.953530,-6.959301,-2.766733,3.343383,1.205032,1.624844,-8.835049,1.551394,8.600254,-6.391720,-0.826857,-9.724440,-6.195606,-4.559679,-3.429845,-2.059300,2.767859,9.552864,-6.819158,-0.464648,-4.807223,-9.740134,4.125016,-3.832760,1.253395,-7.458905,-0.426733,-3.544915,6.796576,-7.234286,4.018356,-1.444132,-4.657094,-9.374361,5.219152,-3.472940], dtype = "float64")#candidate|6733|(11550,)|const|float64
call_6730 = relay.TupleGetItem(func_1278_call(relay.reshape(var_6731.astype('int64'), []), relay.reshape(const_6732.astype('float64'), [1, 770]), relay.reshape(const_6733.astype('float64'), [15, 770]), ), 4)
call_6734 = relay.TupleGetItem(func_1282_call(relay.reshape(var_6731.astype('int64'), []), relay.reshape(const_6732.astype('float64'), [1, 770]), relay.reshape(const_6733.astype('float64'), [15, 770]), ), 4)
func_6212_call = mod.get_global_var('func_6212')
func_6213_call = mutated_mod.get_global_var('func_6213')
call_6755 = func_6212_call()
call_6756 = func_6212_call()
output = relay.Tuple([call_6723,call_6730,var_6731,const_6732,const_6733,call_6755,])
output2 = relay.Tuple([call_6724,call_6734,var_6731,const_6732,const_6733,call_6756,])
func_6760 = relay.Function([var_6731,], output)
mod['func_6760'] = func_6760
mod = relay.transform.InferType()(mod)
var_6761 = relay.var("var_6761", dtype = "int64", shape = ())#candidate|6761|()|var|int64
output = func_6760(var_6761)
func_6762 = relay.Function([var_6761], output)
mutated_mod['func_6762'] = func_6762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1915_call = mod.get_global_var('func_1915')
func_1917_call = mutated_mod.get_global_var('func_1917')
call_6782 = func_1915_call()
call_6783 = func_1915_call()
output = relay.Tuple([call_6782,])
output2 = relay.Tuple([call_6783,])
func_6788 = relay.Function([], output)
mod['func_6788'] = func_6788
mod = relay.transform.InferType()(mod)
output = func_6788()
func_6789 = relay.Function([], output)
mutated_mod['func_6789'] = func_6789
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6876 = relay.var("var_6876", dtype = "float32", shape = (4, 9, 6))#candidate|6876|(4, 9, 6)|var|float32
uop_6877 = relay.erf(var_6876.astype('float32')) # shape=(4, 9, 6)
output = relay.Tuple([uop_6877,])
output2 = relay.Tuple([uop_6877,])
func_6881 = relay.Function([var_6876,], output)
mod['func_6881'] = func_6881
mod = relay.transform.InferType()(mod)
var_6882 = relay.var("var_6882", dtype = "float32", shape = (4, 9, 6))#candidate|6882|(4, 9, 6)|var|float32
output = func_6881(var_6882)
func_6883 = relay.Function([var_6882], output)
mutated_mod['func_6883'] = func_6883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_6925 = relay.TupleGetItem(func_2364_call(), 1)
call_6926 = relay.TupleGetItem(func_2366_call(), 1)
output = call_6925
output2 = call_6926
func_6975 = relay.Function([], output)
mod['func_6975'] = func_6975
mod = relay.transform.InferType()(mod)
mutated_mod['func_6975'] = func_6975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6975_call = mutated_mod.get_global_var('func_6975')
call_6976 = func_6975_call()
output = call_6976
func_6977 = relay.Function([], output)
mutated_mod['func_6977'] = func_6977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2083_call = mod.get_global_var('func_2083')
func_2085_call = mutated_mod.get_global_var('func_2085')
call_7179 = relay.TupleGetItem(func_2083_call(), 0)
call_7180 = relay.TupleGetItem(func_2085_call(), 0)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_7190 = func_2625_call()
call_7191 = func_2625_call()
output = relay.Tuple([call_7179,call_7190,])
output2 = relay.Tuple([call_7180,call_7191,])
func_7199 = relay.Function([], output)
mod['func_7199'] = func_7199
mod = relay.transform.InferType()(mod)
output = func_7199()
func_7200 = relay.Function([], output)
mutated_mod['func_7200'] = func_7200
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7217 = relay.var("var_7217", dtype = "float64", shape = (3, 16, 3))#candidate|7217|(3, 16, 3)|var|float64
uop_7218 = relay.cos(var_7217.astype('float64')) # shape=(3, 16, 3)
func_1108_call = mod.get_global_var('func_1108')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_7251 = relay.TupleGetItem(func_1108_call(), 1)
call_7252 = relay.TupleGetItem(func_1109_call(), 1)
output = relay.Tuple([uop_7218,call_7251,])
output2 = relay.Tuple([uop_7218,call_7252,])
func_7269 = relay.Function([var_7217,], output)
mod['func_7269'] = func_7269
mod = relay.transform.InferType()(mod)
var_7270 = relay.var("var_7270", dtype = "float64", shape = (3, 16, 3))#candidate|7270|(3, 16, 3)|var|float64
output = func_7269(var_7270)
func_7271 = relay.Function([var_7270], output)
mutated_mod['func_7271'] = func_7271
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7314 = relay.var("var_7314", dtype = "int32", shape = (13, 6, 14))#candidate|7314|(13, 6, 14)|var|int32
const_7315 = relay.const([[[8,2,6,6,-3,8,-10,-10,1,-3,-7,1,-3,-3],[3,2,-5,7,-6,-1,-9,-2,-3,-1,10,5,-4,-7],[7,-10,3,-6,-6,10,-5,-1,-9,5,-3,6,10,-3],[10,-3,-9,-9,-7,-9,-7,-5,9,7,8,1,10,-5],[1,-5,5,9,-3,6,-3,-2,-3,3,2,-9,-3,2],[-10,-4,-4,-3,8,-4,-10,10,-5,-6,-1,2,8,-6]],[[4,6,4,6,-8,-8,8,-7,2,4,2,-8,8,6],[1,-8,-9,-8,4,-2,2,-9,2,1,-7,-3,-4,2],[9,9,-2,-5,-3,4,7,-10,-6,9,6,3,-4,4],[7,1,6,6,-7,8,7,7,-2,5,5,7,6,7],[-6,10,-7,-1,-1,2,9,-9,-6,10,-3,-5,1,-2],[-1,6,1,3,9,4,1,9,6,8,-6,7,5,10]],[[3,2,-4,-5,6,-7,-2,-6,-7,-6,-7,-4,-5,4],[4,-6,5,-2,6,-6,-5,-9,3,1,4,-10,2,-4],[8,6,2,-8,-10,8,8,-8,6,-2,-5,-7,-2,10],[5,-2,-1,-3,-10,10,3,-4,1,-6,1,5,2,-7],[-3,10,-2,-8,-1,-6,6,-9,-5,2,6,4,-7,-5],[5,5,10,5,-8,-5,-6,9,8,-2,10,-10,3,4]],[[-6,-1,3,-8,-5,-5,8,1,-10,7,-8,-10,5,5],[-5,-8,-9,2,8,7,5,-6,9,-8,-10,6,5,8],[-9,8,3,-4,8,6,-10,-9,4,-9,-7,-1,-3,6],[-6,-8,9,-8,-3,-7,-10,6,8,4,-5,3,9,8],[5,-2,10,6,7,10,-8,-2,1,-10,-7,9,9,-3],[-9,2,7,-7,-5,4,8,-3,-2,9,-3,2,-5,-2]],[[-6,3,-6,-1,1,7,10,-8,-7,7,6,-5,-4,10],[2,4,-5,-3,-5,3,10,-2,5,-1,10,2,-3,-6],[-5,-8,8,-5,2,5,4,-3,-10,-7,4,-7,-7,4],[-7,-8,-7,-1,2,-8,-8,2,-1,-6,-2,7,-2,-2],[-5,-8,-7,9,5,-10,10,1,-3,7,10,6,-8,-7],[9,-9,8,-9,6,-2,7,-9,-2,-4,5,-8,7,-8]],[[10,5,-7,-4,-2,9,-10,-10,-2,6,1,-8,1,3],[1,3,7,9,-10,8,-7,-1,-9,-7,-2,-7,-3,9],[-1,4,-6,-3,2,-8,6,-6,4,-1,-10,7,1,5],[9,10,8,1,-10,8,6,-6,-1,-9,-2,9,-1,4],[-8,-8,2,-6,1,-6,-2,2,-10,2,3,-6,2,-8],[2,6,10,-9,-1,5,-2,2,-7,4,3,7,-9,-2]],[[8,5,2,10,-3,-6,-3,6,-4,-9,-3,8,-1,1],[-8,1,2,6,5,-8,4,-5,-7,-2,1,3,4,-1],[6,3,6,-10,9,-2,1,-5,4,-1,2,3,3,-9],[-7,2,-2,-7,-10,-7,-2,-3,1,-7,-9,5,2,-9],[3,-3,-6,-2,-1,-7,6,10,-4,-1,5,7,6,9],[1,-2,4,5,-2,10,-5,-6,10,-9,3,7,-7,3]],[[-10,1,8,6,-1,-4,9,8,-1,-7,2,-7,-5,2],[3,-7,-6,4,2,-10,2,-7,7,5,10,1,9,5],[-6,-5,-2,2,1,-6,8,7,7,1,9,-4,-1,9],[6,-3,2,-9,-2,-4,7,-7,5,6,-8,-8,4,-6],[-8,4,-10,4,5,-8,-4,-10,-4,7,1,-1,-10,-5],[-10,1,5,-2,2,-9,-1,6,1,10,10,-5,1,-9]],[[-3,-9,-3,-3,-8,5,4,9,-5,3,-8,3,2,-1],[4,-6,-4,1,7,-8,-10,-7,1,10,-10,3,-7,7],[4,4,10,4,7,1,-1,9,6,-8,9,-4,-2,-6],[-3,2,-3,-7,6,-6,1,7,8,5,-9,2,10,8],[3,5,-10,-7,-3,7,8,-2,-1,-10,4,-5,-10,-4],[3,6,-7,3,-8,-4,5,-10,-5,1,-1,6,-8,-8]],[[-8,-1,-4,6,-8,1,-7,6,-6,-4,-7,6,-10,3],[3,-8,-4,1,-6,9,6,-9,-7,-7,-9,2,10,6],[-10,7,10,6,4,2,-4,3,3,5,7,2,4,6],[4,3,-2,-9,6,6,3,-2,-1,1,9,5,-9,-3],[-3,-9,10,-2,2,5,-9,8,3,2,-6,-7,8,-2],[8,-10,-4,-7,10,-9,3,10,6,-5,-1,2,-10,2]],[[-10,-5,-2,1,-5,-2,-8,-9,4,-4,-1,-9,7,-10],[2,-5,8,3,4,-6,2,5,-9,-4,4,-3,-8,7],[-6,2,-9,-10,-6,7,-7,-10,10,-1,-10,2,-3,-10],[9,-6,-2,-1,-7,10,-6,-3,1,-3,9,-2,7,2],[8,10,-9,2,-7,4,6,7,-2,-6,-4,-6,1,9],[-1,-9,-2,8,-7,5,-5,-10,-3,-4,7,-8,7,1]],[[1,7,2,-2,-4,8,-1,7,-1,9,-4,-1,-1,10],[-4,-7,5,-6,7,-3,-8,-4,5,-9,10,2,-8,-5],[-3,-8,-9,9,-6,-1,5,-8,9,6,-7,10,-10,1],[7,-1,-2,5,-4,5,3,7,-2,-1,-6,4,-1,-1],[9,10,-10,4,10,5,-6,-5,6,7,6,-6,-6,-6],[-5,9,-2,9,2,6,-5,-7,1,9,4,5,3,-2]],[[4,-5,6,-4,-5,-10,6,-8,-7,1,-6,5,-6,8],[4,8,8,6,9,2,-2,-10,10,-1,-2,-5,3,-8],[10,10,-6,1,-4,-7,6,-7,-6,7,5,-3,10,-7],[7,4,3,-1,-2,2,9,1,3,-4,-6,-2,-8,-10],[-2,5,-4,7,3,-6,-2,3,8,-7,-1,-9,-1,-8],[8,1,-6,-9,3,8,8,3,10,1,9,10,-8,-6]]], dtype = "int32")#candidate|7315|(13, 6, 14)|const|int32
bop_7316 = relay.maximum(var_7314.astype('int32'), relay.reshape(const_7315.astype('int32'), relay.shape_of(var_7314))) # shape=(13, 6, 14)
output = bop_7316
output2 = bop_7316
func_7334 = relay.Function([var_7314,], output)
mod['func_7334'] = func_7334
mod = relay.transform.InferType()(mod)
mutated_mod['func_7334'] = func_7334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7335 = relay.var("var_7335", dtype = "int32", shape = (13, 6, 14))#candidate|7335|(13, 6, 14)|var|int32
func_7334_call = mutated_mod.get_global_var('func_7334')
call_7336 = func_7334_call(var_7335)
output = call_7336
func_7337 = relay.Function([var_7335], output)
mutated_mod['func_7337'] = func_7337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5035_call = mod.get_global_var('func_5035')
func_5036_call = mutated_mod.get_global_var('func_5036')
call_7378 = relay.TupleGetItem(func_5035_call(), 1)
call_7379 = relay.TupleGetItem(func_5036_call(), 1)
output = relay.Tuple([call_7378,])
output2 = relay.Tuple([call_7379,])
func_7388 = relay.Function([], output)
mod['func_7388'] = func_7388
mod = relay.transform.InferType()(mod)
mutated_mod['func_7388'] = func_7388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7388_call = mutated_mod.get_global_var('func_7388')
call_7389 = func_7388_call()
output = call_7389
func_7390 = relay.Function([], output)
mutated_mod['func_7390'] = func_7390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1108_call = mod.get_global_var('func_1108')
func_1109_call = mutated_mod.get_global_var('func_1109')
call_7470 = relay.TupleGetItem(func_1108_call(), 0)
call_7471 = relay.TupleGetItem(func_1109_call(), 0)
output = relay.Tuple([call_7470,])
output2 = relay.Tuple([call_7471,])
func_7476 = relay.Function([], output)
mod['func_7476'] = func_7476
mod = relay.transform.InferType()(mod)
mutated_mod['func_7476'] = func_7476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7476_call = mutated_mod.get_global_var('func_7476')
call_7477 = func_7476_call()
output = call_7477
func_7478 = relay.Function([], output)
mutated_mod['func_7478'] = func_7478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_355_call = mutated_mod.get_global_var('func_355')
call_7482 = relay.TupleGetItem(func_353_call(), 0)
call_7483 = relay.TupleGetItem(func_355_call(), 0)
func_989_call = mod.get_global_var('func_989')
func_990_call = mutated_mod.get_global_var('func_990')
call_7489 = relay.TupleGetItem(func_989_call(), 1)
call_7490 = relay.TupleGetItem(func_990_call(), 1)
output = relay.Tuple([call_7482,call_7489,])
output2 = relay.Tuple([call_7483,call_7490,])
func_7533 = relay.Function([], output)
mod['func_7533'] = func_7533
mod = relay.transform.InferType()(mod)
mutated_mod['func_7533'] = func_7533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7533_call = mutated_mod.get_global_var('func_7533')
call_7534 = func_7533_call()
output = call_7534
func_7535 = relay.Function([], output)
mutated_mod['func_7535'] = func_7535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2660_call = mod.get_global_var('func_2660')
func_2662_call = mutated_mod.get_global_var('func_2662')
call_7595 = relay.TupleGetItem(func_2660_call(), 1)
call_7596 = relay.TupleGetItem(func_2662_call(), 1)
output = relay.Tuple([call_7595,])
output2 = relay.Tuple([call_7596,])
func_7610 = relay.Function([], output)
mod['func_7610'] = func_7610
mod = relay.transform.InferType()(mod)
output = func_7610()
func_7611 = relay.Function([], output)
mutated_mod['func_7611'] = func_7611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_7659 = func_407_call()
call_7660 = func_407_call()
func_3305_call = mod.get_global_var('func_3305')
func_3307_call = mutated_mod.get_global_var('func_3307')
call_7696 = relay.TupleGetItem(func_3305_call(), 0)
call_7697 = relay.TupleGetItem(func_3307_call(), 0)
func_4858_call = mod.get_global_var('func_4858')
func_4859_call = mutated_mod.get_global_var('func_4859')
call_7698 = func_4858_call()
call_7699 = func_4858_call()
output = relay.Tuple([call_7659,call_7696,call_7698,])
output2 = relay.Tuple([call_7660,call_7697,call_7699,])
func_7708 = relay.Function([], output)
mod['func_7708'] = func_7708
mod = relay.transform.InferType()(mod)
output = func_7708()
func_7709 = relay.Function([], output)
mutated_mod['func_7709'] = func_7709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_7720 = func_458_call()
call_7721 = func_458_call()
func_3398_call = mod.get_global_var('func_3398')
func_3405_call = mutated_mod.get_global_var('func_3405')
var_7734 = relay.var("var_7734", dtype = "float64", shape = (1365,))#candidate|7734|(1365,)|var|float64
var_7735 = relay.var("var_7735", dtype = "int64", shape = ())#candidate|7735|()|var|int64
const_7736 = relay.const([-0.542372,1.355146,-8.701724,2.119117,-2.009470,-9.096188,5.499103,7.517064,8.888551,8.468231,-2.487389,5.255870,-6.164015,-6.084542,8.081762,-6.038496,1.294650,-3.162532,2.671884,1.706914,7.111560,5.138771,-4.619284,-7.198181,-7.241213,-8.494832,-7.224920,-6.339743,8.129860,-4.412476,-6.090884,-7.672806,-7.441359,5.669698,3.147627,9.222778,-4.649175,2.984585,4.162643,2.663395,3.168180,-4.586769,7.920009,3.120470,1.714485,3.104271,-8.498972,8.205487,6.897902,-8.209725,-0.015941,2.596298,-2.033237,4.555412,-6.855773,8.223315,-7.000028,9.659125,-8.980719,9.248379,-3.726529,9.180050,-1.117801,1.777757,-2.090130,-7.218229,3.912654,8.998309,-5.599804,4.685828,1.577753,5.738428,-7.099085,9.247881,3.700349,5.209907,-3.624414,-2.022865,0.423116,-8.379505,3.361637,-5.409889,-4.977041,-4.009678,5.927369,5.393641,-0.027907,-3.461821,-0.992472,-7.705141,-7.731407,4.008627,-7.994108,-1.101993,-0.057863,8.861609,7.921718,-0.325641,-1.330884,3.158465,5.605636,-5.580081,4.751239,-0.821149,3.405355,7.127347,-7.966987,-4.983745,-3.860429,3.123064,9.699905,-1.450066,-7.168863,-2.366091,9.839652,-6.887891,-5.035994,-7.199888,-7.993755,1.713795,5.389660,5.800286,-6.032992,1.328526,-4.832774,5.159268,8.535488,2.899240,-7.966848,-5.461048,1.518267,-4.497413,-0.710796,4.842163,-0.375570,-3.168699,9.849099,1.042256,4.137572,-1.963441,9.649026,5.220953,9.198595,0.208426,-8.876246,9.725241,-4.733753,5.118712,-9.474397,7.209248,-8.356650,3.829307,-9.492036,2.599395,1.210721,2.913041,2.005204,1.746260,1.708509,-2.776578,8.905332,1.745281,-4.701585,-2.730114,6.408983,3.256899,1.181115,9.470232,8.363796,5.864589,-7.213547,-8.090441,6.196088,-4.573092,-9.390916,-2.693958,-5.606583,6.323730,-1.963418,-8.757032,-9.105883,1.454424,-4.960693,7.546093,8.760379,-2.257787,3.760513,5.820419,-7.054673,-1.236465,3.300878,-5.569940,-8.923308,-4.448790,6.937776,0.460833,-3.431618,5.273354,2.715917,-8.615037,3.329472,9.772879,2.428362,0.827680,-6.235712,-8.976703,-0.419979,-3.129338,6.789186,-6.585510,5.482038,-8.653380,-0.524514,-0.876390,-8.513974,4.281212,7.584597,-3.981426,2.847098,-3.885922,6.126394,4.771433,-3.028611,7.525325,-9.751304,-4.771870,2.274791,7.005672,6.409002,0.429360,8.394669,5.055610,5.931440,4.954110,-3.106127,6.119000,8.579974,1.360466,-3.114159,4.119227,-6.456838,-0.365253,-8.339749,-0.428655,6.658675,1.589970,-1.822987,0.955749,-8.534504,-5.521457,-5.229648,0.174924,2.619744,7.034723,6.183314,-6.006646,1.518240,3.519472,1.556779,9.584855,7.569968,5.494662,4.315657,-3.100148,5.434127,-4.364037,-7.247605,1.202871,9.292118,9.622993,5.041545,-1.533648,-9.793858,-6.560911,3.409283,-1.814331,-7.442105,-3.869277,-5.215585,-8.772959,-1.893522,2.605543,-7.719906,-9.757853,-2.852146,-0.422509,3.948426,-2.989951,-0.443449,9.835771,-8.492375,-6.239791,4.851224,-1.258436,8.137911,-0.632076,-8.463780,-5.270565,-8.456247,-6.789735,-4.255630,4.959682,3.915549,1.156402,-6.068081,-3.548237,-8.183381,-9.151754,4.367212,1.229022,2.082159,-7.813544,-7.560168,-8.707908,4.490767,2.237103,3.076355,-2.277564,-7.491237,-5.964577,-4.628552,2.720188,5.534989,9.556497,-3.096304,-7.535454,-0.333713,2.847480,7.298482,0.449033,-8.019090,9.766373,7.515199,0.192660,1.484961,2.399048,-2.596369,8.591861,-1.463255,-2.580201,8.867367,-0.747108,-0.002930,-7.396238,9.144318,-1.148863,-6.337407,4.023179,7.466758,4.628911,-8.010150,2.790477,6.049730,-0.718568,5.833932,2.322200,4.402257,-6.254323,0.252849,-7.247199,-9.616446,0.922681,-8.313136,1.174822,6.668606,-0.916484,6.616434,-3.619528,-7.261711,-0.116073,6.407924,4.957735,4.062014,-5.593957,-1.849766,1.301540,-9.999761,-4.183620,3.899658,-6.787526,-9.447728,-8.587781,-4.140604,6.012640,3.134651,-1.679961,6.510182,-2.870041,7.999463,4.392512,6.216862,3.016048,4.496343,-3.412184,6.867551,1.414669,1.908364,4.601335,-7.567378,3.685610,-3.865682,9.500546,1.130684,-5.457936,-5.171234,-3.658798,-0.579493,9.101805,0.712042,-0.729674,6.253706,5.661921,3.252791,-0.412011,6.705556,6.538097,-4.180782,9.297194,-3.701311,-9.432627,5.474977,-2.735097,-9.000281,-9.391422,2.822538,-5.257558,-9.535192,-7.561968,-9.909945,-2.053804,-7.029913,1.671095,-3.128027,-1.695237,-8.463269,6.838932,9.917879,2.246343,-0.866778,-4.367765,-7.542045,-6.556582,-5.420592,-7.294834,9.484206,-9.128585,0.350631,-7.069511,-0.716256,-7.014235,-6.076596,-7.748830,-3.961935,5.986037,7.718913,-1.417516,6.354426,3.554769,2.332718,-1.412553,-9.563119,-5.823246,3.418957,2.580146,1.959932,-1.479715,4.240881,-7.416865,1.583714,-0.234072,3.206407,-8.134419,2.182839,-8.108802,-7.105892,-2.959590,8.812784,-3.371579,5.112166,-3.258142,0.851225,-6.077428,6.380302,-4.054814,7.160969,-8.571686,-9.541538,1.675950,-0.044052,-5.954265,-2.704241,2.977450,-6.493989,-8.390685,8.012988,-3.407549,-2.390490,7.512759,2.457768,-3.493893,7.501883,2.709374,2.439425,9.611920,-8.689321,-2.728122,-5.372169,-7.851645,9.411185,9.391662,3.904610,-9.474398,-5.912138,-0.044869,6.766062,-0.145914,7.655109,-1.918160,-8.213205,-7.078305,-2.133861,-2.613670,-3.958069,9.669963,5.137941,-4.702331,-9.933578,-8.043916,-7.400174,0.378825,5.865513,-7.748101,8.663149,-7.925435,1.519740,3.239838,6.789043,-4.695754,-8.881982,-7.242004,-4.474596,4.109243,9.895081,-9.828871,-0.048263,6.932491,5.005205,-1.337855,2.627615,9.606381,1.546237,-3.357103,-4.270227,-2.669677,-0.246529,-8.697750,8.263325,0.011417,-0.789171,-5.796720,6.566327,-9.696885,-3.901462,-1.428486,9.400408,-4.978332,-7.677693,-9.389647,0.549093,5.688864,6.662202,7.859352,1.812117,4.521553,-0.956137,-3.952688,1.128276,-4.885462,3.942215,5.499490,-2.892647,7.723598,-3.707931,4.508978,-5.478298,0.012780,5.683645,-3.050308,-2.667735,-0.139403,-8.397225,-6.001758,7.628984,5.764286,1.710980,-2.797583,-9.017095,-0.425242,2.259458,-0.176120,3.507524,2.775272,-1.370593,5.869735,3.438119,0.135157,4.310107,9.615561,0.770645,9.881512,-1.386280,-0.870325,-8.804449,5.498357,2.304850,1.780213,-8.072876,4.062470,5.758381,3.897883,-0.890167,-6.764166,-5.899260,-4.327802,-7.040985,8.295728,8.585081,9.468073,-2.199224,3.722892,-4.874761,-3.444507,9.549338,-1.971546,8.904156,5.775936,-7.774740,2.417974,-4.546861,-3.782951,0.551823,8.886106,-7.454006,-8.668704,3.339169,-6.754148,1.719578,-0.496150,-2.142632,2.011342,-9.147752,4.140008,-0.470861,-0.957037,-7.683588,9.552297,-7.366771,9.956031,1.683627,8.432560,8.954653,-8.655507,4.366322,-2.747554,6.154538,7.888567,-6.498233,6.227602,3.625157,7.955281,-0.301598,8.663284,7.963285,4.204114,6.869826,-8.468895,-6.483944,2.896342,4.011816,8.387296,2.954525,6.583410,5.839403,-2.055920,-6.593728,2.052856,-0.228347,8.101393,3.899778,-0.169551,6.472603,0.645501,0.660364,4.574181,-7.648605,-2.276686,3.311263,-8.823586,-4.725252,3.694117,-8.086321,5.668826,-0.860410,2.611850,-9.819020,-4.119155,-3.937520,4.668454,-6.569300,-3.872354,-8.395034,-3.656988,-9.365641,-3.444529,7.736714,6.632058,-3.327400,-8.109685,1.471051,-9.375044,2.315008,-0.873011,8.657904,3.198210,-5.439622,-4.731890,-9.473733,6.018887,2.289744,2.109434,5.044363,2.400566,-8.807475,-2.443235,3.785162,1.628348,1.109079,-7.943485,7.188599,-4.313877,5.935084,-5.050087,9.320456,7.462317,-2.151467,3.283244,1.843193,0.444145,-3.535561,-1.404860,4.239753,-8.059437,4.989906,3.427189,0.158942,-6.195044,-6.881809,-2.547249,-9.140320,9.141524,8.280407,1.149164,9.690320,-2.433301,-7.280131,0.512178,-3.827935,9.710173,-8.831743,-6.970677], dtype = "float64")#candidate|7736|(770,)|const|float64
var_7737 = relay.var("var_7737", dtype = "uint16", shape = (2640, 1))#candidate|7737|(2640, 1)|var|uint16
const_7738 = relay.const([[5,3,4,-6,-9,9,4,-7,5,-3,-5,-4,-9,-3,6,-4,9,-8,-9,-1,5,-2,-7,1,2,-3,-10,9,9,-2,-7,8,4,-8,-10,1,-1,6,3,-10,-1,1,7,-3,-4,-1,-1,-7],[-7,-10,-6,-6,-6,-4,2,-6,-4,6,-9,-10,-6,-5,2,-6,9,-9,8,3,-8,7,-1,-2,-9,8,9,-4,1,-2,3,3,3,-10,-7,-7,10,-6,-6,-5,7,7,-1,1,-2,4,-2,-1]], dtype = "int64")#candidate|7738|(2, 48)|const|int64
call_7733 = relay.TupleGetItem(func_3398_call(relay.reshape(var_7734.astype('float64'), [7, 15, 13]), relay.reshape(var_7735.astype('int64'), []), relay.reshape(const_7736.astype('float64'), [770,]), relay.reshape(var_7737.astype('uint16'), [2640,]), relay.reshape(const_7738.astype('int64'), [96,]), ), 7)
call_7739 = relay.TupleGetItem(func_3405_call(relay.reshape(var_7734.astype('float64'), [7, 15, 13]), relay.reshape(var_7735.astype('int64'), []), relay.reshape(const_7736.astype('float64'), [770,]), relay.reshape(var_7737.astype('uint16'), [2640,]), relay.reshape(const_7738.astype('int64'), [96,]), ), 7)
output = relay.Tuple([call_7720,call_7733,var_7734,var_7735,const_7736,var_7737,const_7738,])
output2 = relay.Tuple([call_7721,call_7739,var_7734,var_7735,const_7736,var_7737,const_7738,])
func_7748 = relay.Function([var_7734,var_7735,var_7737,], output)
mod['func_7748'] = func_7748
mod = relay.transform.InferType()(mod)
mutated_mod['func_7748'] = func_7748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7748_call = mutated_mod.get_global_var('func_7748')
var_7750 = relay.var("var_7750", dtype = "float64", shape = (1365,))#candidate|7750|(1365,)|var|float64
var_7751 = relay.var("var_7751", dtype = "int64", shape = ())#candidate|7751|()|var|int64
var_7752 = relay.var("var_7752", dtype = "uint16", shape = (2640, 1))#candidate|7752|(2640, 1)|var|uint16
call_7749 = func_7748_call(var_7750,var_7751,var_7752,)
output = call_7749
func_7753 = relay.Function([var_7750,var_7751,var_7752,], output)
mutated_mod['func_7753'] = func_7753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_7861 = func_458_call()
call_7862 = func_458_call()
output = call_7861
output2 = call_7862
func_7876 = relay.Function([], output)
mod['func_7876'] = func_7876
mod = relay.transform.InferType()(mod)
output = func_7876()
func_7877 = relay.Function([], output)
mutated_mod['func_7877'] = func_7877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2284_call = mod.get_global_var('func_2284')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_7964 = func_2284_call()
call_7965 = func_2284_call()
output = relay.Tuple([call_7964,])
output2 = relay.Tuple([call_7965,])
func_7966 = relay.Function([], output)
mod['func_7966'] = func_7966
mod = relay.transform.InferType()(mod)
output = func_7966()
func_7967 = relay.Function([], output)
mutated_mod['func_7967'] = func_7967
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8137 = relay.var("var_8137", dtype = "float64", shape = (10, 7, 6))#candidate|8137|(10, 7, 6)|var|float64
uop_8138 = relay.atanh(var_8137.astype('float64')) # shape=(10, 7, 6)
bop_8151 = relay.greater_equal(uop_8138.astype('bool'), relay.reshape(var_8137.astype('bool'), relay.shape_of(uop_8138))) # shape=(10, 7, 6)
uop_8173 = relay.tan(var_8137.astype('float64')) # shape=(10, 7, 6)
func_5204_call = mod.get_global_var('func_5204')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_8183 = relay.TupleGetItem(func_5204_call(), 0)
call_8184 = relay.TupleGetItem(func_5205_call(), 0)
uop_8189 = relay.cos(uop_8138.astype('float32')) # shape=(10, 7, 6)
func_2625_call = mod.get_global_var('func_2625')
func_2626_call = mutated_mod.get_global_var('func_2626')
call_8191 = func_2625_call()
call_8192 = func_2625_call()
uop_8203 = relay.log10(uop_8189.astype('float32')) # shape=(10, 7, 6)
uop_8206 = relay.sigmoid(uop_8189.astype('float32')) # shape=(10, 7, 6)
output = relay.Tuple([bop_8151,uop_8173,call_8183,call_8191,uop_8203,uop_8206,])
output2 = relay.Tuple([bop_8151,uop_8173,call_8184,call_8192,uop_8203,uop_8206,])
func_8209 = relay.Function([var_8137,], output)
mod['func_8209'] = func_8209
mod = relay.transform.InferType()(mod)
mutated_mod['func_8209'] = func_8209
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8210 = relay.var("var_8210", dtype = "float64", shape = (10, 7, 6))#candidate|8210|(10, 7, 6)|var|float64
func_8209_call = mutated_mod.get_global_var('func_8209')
call_8211 = func_8209_call(var_8210)
output = call_8211
func_8212 = relay.Function([var_8210], output)
mutated_mod['func_8212'] = func_8212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6015_call = mod.get_global_var('func_6015')
func_6017_call = mutated_mod.get_global_var('func_6017')
call_8294 = relay.TupleGetItem(func_6015_call(), 0)
call_8295 = relay.TupleGetItem(func_6017_call(), 0)
output = relay.Tuple([call_8294,])
output2 = relay.Tuple([call_8295,])
func_8309 = relay.Function([], output)
mod['func_8309'] = func_8309
mod = relay.transform.InferType()(mod)
output = func_8309()
func_8310 = relay.Function([], output)
mutated_mod['func_8310'] = func_8310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7966_call = mod.get_global_var('func_7966')
func_7967_call = mutated_mod.get_global_var('func_7967')
call_8346 = relay.TupleGetItem(func_7966_call(), 0)
call_8347 = relay.TupleGetItem(func_7967_call(), 0)
output = relay.Tuple([call_8346,])
output2 = relay.Tuple([call_8347,])
func_8350 = relay.Function([], output)
mod['func_8350'] = func_8350
mod = relay.transform.InferType()(mod)
output = func_8350()
func_8351 = relay.Function([], output)
mutated_mod['func_8351'] = func_8351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2558_call = mod.get_global_var('func_2558')
func_2560_call = mutated_mod.get_global_var('func_2560')
call_8388 = relay.TupleGetItem(func_2558_call(), 0)
call_8389 = relay.TupleGetItem(func_2560_call(), 0)
func_219_call = mod.get_global_var('func_219')
func_222_call = mutated_mod.get_global_var('func_222')
const_8459 = relay.const([-3.712637,-1.188326,3.584062,-3.124806,-2.766865,-4.188363,7.325573,-7.303960,-5.979265,-5.662040,5.969176,-9.407392,-5.599664,-7.508141,-8.846213,4.469740,-3.719638,-5.575716,3.046144,-7.964952,9.044906,-0.566429,3.735661,-4.018948,-2.392909,8.224309,-4.931241,6.589576,3.722184,1.073415,-7.446264,-9.164963,-6.627698,-3.143414,0.237385,1.233079,9.794421,6.629009,-8.575022,-6.724718,3.167286,-4.426184,-9.468134,-7.730645,-0.009822,5.701973,5.255901,9.883019,-7.016041,6.812175,-2.024147,1.899504,-3.301352,5.005992,-5.989136,0.676890,3.325099,-9.765906,1.929006,3.098654,-0.900023,-8.769718,-9.647183,3.811585,6.904214,-4.533873,-7.646437,-0.100557,-7.541480,5.102642,6.269523,-1.863200,9.598841,-7.188383,-3.570537,-8.497920,5.180048,-1.540294,-2.418685,-5.964589,-1.009820,-7.459290,-4.280255,8.619600,-1.959752,-0.394880,7.621896,-0.918189,1.790038,3.958103,-9.253667,-4.212784,-8.467973,3.843325,-0.146900,-8.111706,-3.511486,5.793190,2.491437,7.163707,-1.162502,-8.941860,8.856593,-8.180533,3.686977,-1.660903,5.892831,1.381667,6.310044,-2.947751,0.508219,-2.410183,5.244283,-8.388833,-6.245767,-8.048917,8.598695,-8.887309,2.435260,0.471744,-6.892361,-6.120497,-2.197422,8.241859,-6.372771,-4.217380,-0.618114,4.351029,-5.160915,6.727002,-8.722635,9.714432,-1.918181,-2.713019,-8.066791,-5.251265,7.182010,-8.721421,5.916120,7.292105,-7.496315,8.509719,-8.457902,-4.964070,-9.603614,5.036846,-1.643418,2.078847,-0.519160,-7.816782,3.609817,9.696431,-3.753289,1.548821,1.270340,7.966058,-0.590120,-0.737765,-7.810886,8.377929,-4.417324,0.859157,-5.963757,3.283984,-1.758933,2.600487,3.918287,-6.651744,2.282930,1.839422,-7.003167,-4.800181,5.239062,2.981138,1.780913,-0.206777,7.918572,-2.490201,-4.173089,-7.242390,-8.975937,8.085714,-6.133649,2.227314,1.136822,-2.096270,6.252287,-1.414065,4.684938,-1.199604,-1.533302,7.686861,-5.044690,0.369067,2.094361,9.693408,-1.812434,4.660290,-4.175406,-5.603619,0.838337,3.652129,4.325081,9.197885,0.458245,8.064779,6.329350,1.111861,4.210657,-3.328915,-0.359487,-2.324356,-3.381651,4.158101,-9.428972,-8.104720,-9.543169,-4.259893,0.305781,2.710520,-4.946547,8.766922,4.823658,9.412820,0.080894,3.416720,-1.595815,-9.681094,-7.614610,2.442440,5.075753,-2.203485,-6.644338,2.540025,6.476534,-3.468339,-7.144290,5.179679,9.163995,-0.043666,-3.370020,-2.058534,4.088989,-3.025532,6.778011,-5.990333,4.185658,-7.547739,0.268025,-1.516494,-1.650234,-1.161840,-5.433090,-4.904633,7.754906,-0.341541,7.977709,-2.953958,-3.217187,-2.237760,-6.132180,-8.228379,6.259746,9.625171,7.779823,1.650617,4.021860,-8.989324,2.365817,4.206962,8.264343,3.671726,-5.458752,0.617649,-2.057535,-8.223689,-9.947692,-0.941084,-5.909255,-8.308267,5.165715,5.135020,-1.422618,-8.238236,6.551863,-9.941400,-3.638386,6.041762,9.468430,7.889819,-7.173051,-6.952146,-9.547124,-7.037162,1.445898,-1.487909,0.836806,2.529565,7.630851,5.143697,1.158614,7.544821,0.081746,-8.503588,5.224009,-9.199830,-3.508554,-9.500058,-0.648559,2.669661,-4.279564,-0.367176,3.747533,7.347424,-0.051554,8.570237,-4.424829,5.563423,6.380002,-3.535475,4.047481,-7.744449,7.897509,-4.732972,-8.040819,5.999396,-7.994711,-5.007734,2.044569,-1.220423,-9.955532,4.770055,0.963425,0.672979,0.645173,2.608108,-6.333688,-4.019684,8.743651,4.874360,-6.274882,-4.447273,4.660992,-0.099436,-5.291682,-0.436684,8.240373,3.238728,-3.195078,4.934610,-6.825920,-5.227744,5.966018,-4.061149,5.261404,-9.433548,6.138110,-2.369148,6.483843,5.156585,-7.356584,-5.212646,-5.483025,-2.412465,-4.332904,-3.864691,-7.824555,-2.971786,5.540338,-7.934796,-8.437643,-8.119983,1.167617,-3.242214,5.713371,-1.661894,7.915355,0.809883,-3.057582,-2.558099,-1.192961,3.085743,9.231627,-6.745074,3.356526,-2.221166,6.346673,0.977332,7.688305,4.384916,4.185590,-9.185481,-5.677684,-8.497404,5.297847,-1.864406,7.502952,6.024535,7.941744,8.586450,-2.196025,-2.561718,-4.474061,8.844503,-5.796843,7.710341,-0.736039,-3.136768,1.144815,-9.713235,-2.787586,-8.722734,-8.546202,-3.058906,5.040423,-7.881433,2.673797,7.411769,-7.018267,-9.990355,1.825131,0.604419,7.762893,5.169013,-3.786645,-8.162663,-1.713684,4.626062,-8.556143,-6.452848,6.123648,9.520111,9.749564,8.615432,1.548941,-0.519215,8.680990,0.457539,-7.979204,4.419195,-9.949154,5.153244,3.574162,3.154593,-6.241187,0.860297,2.456871,9.479763,-5.054214,-5.025896,-3.856598,-3.858887,-7.416946,-7.726906,-0.754472,-0.037989,6.596896,2.048809,-1.133690,-1.940895,-4.343612,-2.858732,0.553702,6.676894,-2.626541,0.569915,-9.921878,-9.692976,4.228412,1.230054,7.161777,-7.347506,3.340705,7.140538,7.457294,8.438823,4.753380,2.644736,2.350035,-7.011293,-7.466556,-2.252307,-4.951630,-4.077126,9.946482,6.795905,3.167717,-3.932088,-8.232764,-1.664887,0.553615,7.528171,4.773178,4.091953,3.325771,6.029742,-0.262726,6.363082,-8.171530,-0.161828,8.444895,-5.345838,-0.577508,-6.809577,-8.231836,-6.749921,-5.546815,0.824274,-0.131091,-5.249761,-0.567018,0.982656,7.140873,3.278511,-9.843600,6.846470,-6.255623,-6.112396,-2.445223,7.235565,0.645451,5.179214,5.580279,-7.812741,3.148470,-7.535882,-0.691558,-2.714940,-3.112565,3.056603,-0.820345,-5.787914,4.810246,2.709115,6.808686,-6.849503,-1.906530,-9.248816,-7.263155,9.711149,3.398555,-6.011693,6.692220,3.732704,-2.815047,1.571270,-6.223637,5.571342,-2.100699,6.479001,4.404160,8.744331,5.600738,-2.978673,-6.937984,-6.666875,2.874904,4.036497,6.810206,-7.293243,2.691101,-4.237257,0.267488,9.249392,-0.383781,-0.150363,4.850227,0.982310,2.713526,-1.725964,1.150021,-2.565682,5.857835,-3.762989,-6.539964,0.213514,-9.598608,7.915854,6.304819,4.759182,-4.296338,-9.416310,4.584304,-7.189303,4.566508,-9.408185,7.161419,2.583894,-5.595824,-6.421220,-1.521558,8.252588,3.563457,-2.148930,7.560134,2.636686,2.392576,3.425405,5.220561,-9.406064,6.652225,-8.909823,0.923684,0.508845,4.351547,-6.285465,4.722302,-7.443485,0.183559,-9.075270,-5.583455,-7.347741,5.686140,8.684473,4.687303,5.597775,-0.629947,-3.706382,7.556981,-6.502806,7.047563,-9.738247,-8.296294,1.336887,4.756303,-0.123979,4.258115,-5.173987,2.431630,-7.424977,6.137479,9.489231,8.359169,7.794038,8.665782,7.633539,-0.395337,-1.145467,-8.461763,-0.496296,5.238884,1.398195,9.164023,3.599646,6.486474,-9.993165,2.632540,7.424867,4.437155,1.006485,-6.329626,2.936594,-3.995236,6.512049,0.941983,-3.097539,-9.668855,-9.715327,7.450483,-8.157823,7.667930,5.194843,-2.049299,1.350303,1.548598,9.945133,7.767094,4.911558,-7.811624,-7.264042,-4.157334,-1.656111,-7.513294,6.555520,-3.394503,2.852693,-3.225022,-2.123735,2.727495,-5.391654,-2.153702,-5.947464,-5.077026,2.553829,-7.511089,-3.267047,-0.995400,6.337280,2.927788,6.091611,0.022687,0.452147,2.229784,-7.526861,5.160916,-1.644073,-6.304224,3.799677,-6.408714,3.756823,-4.587619,8.984982,-4.462525,-8.372467,4.794748,6.531464,-2.343931,-3.093493,-0.742435,-0.472560,2.210327,4.453584,0.962844,-8.269958,8.786639,-1.802407,-1.237066,4.035592,-0.905484,-8.604203,3.618489,-9.670654,0.710599,2.037305,-1.760682,1.890773,-7.299075,6.131897,-7.463407,8.842209,-0.306844,6.872177,-1.570068,6.668336,-2.579338,-6.492791,-8.954001,0.796628,-4.630488,0.242314,-4.340973,-5.107180,-8.100149,-5.298801,-2.161553,-5.480485,5.695454,8.440252,-5.527487,6.098084,-2.438405,-4.969767,-7.350856,-1.827303,4.473943,0.492572,8.982169,-7.404872,-2.720931,-4.966015,0.173557,5.208863,-7.394473,-3.067020,8.024710,-5.768439,6.027716,-1.895055,-0.666164,-0.202841], dtype = "float64")#candidate|8459|(770,)|const|float64
call_8458 = relay.TupleGetItem(func_219_call(relay.reshape(const_8459.astype('float64'), [10, 7, 11]), relay.reshape(const_8459.astype('float64'), [10, 7, 11]), ), 0)
call_8460 = relay.TupleGetItem(func_222_call(relay.reshape(const_8459.astype('float64'), [10, 7, 11]), relay.reshape(const_8459.astype('float64'), [10, 7, 11]), ), 0)
func_6015_call = mod.get_global_var('func_6015')
func_6017_call = mutated_mod.get_global_var('func_6017')
call_8463 = relay.TupleGetItem(func_6015_call(), 0)
call_8464 = relay.TupleGetItem(func_6017_call(), 0)
func_4241_call = mod.get_global_var('func_4241')
func_4244_call = mutated_mod.get_global_var('func_4244')
call_8470 = relay.TupleGetItem(func_4241_call(relay.reshape(call_8463.astype('float32'), [3, 13, 2])), 2)
call_8471 = relay.TupleGetItem(func_4244_call(relay.reshape(call_8463.astype('float32'), [3, 13, 2])), 2)
bop_8483 = relay.add(call_8458.astype('float64'), relay.reshape(const_8459.astype('float64'), relay.shape_of(call_8458))) # shape=(10, 7, 11)
bop_8486 = relay.add(call_8460.astype('float64'), relay.reshape(const_8459.astype('float64'), relay.shape_of(call_8460))) # shape=(10, 7, 11)
output = relay.Tuple([call_8388,call_8463,call_8470,bop_8483,])
output2 = relay.Tuple([call_8389,call_8464,call_8471,bop_8486,])
func_8491 = relay.Function([], output)
mod['func_8491'] = func_8491
mod = relay.transform.InferType()(mod)
output = func_8491()
func_8492 = relay.Function([], output)
mutated_mod['func_8492'] = func_8492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_8506 = func_458_call()
call_8507 = func_458_call()
output = call_8506
output2 = call_8507
func_8544 = relay.Function([], output)
mod['func_8544'] = func_8544
mod = relay.transform.InferType()(mod)
mutated_mod['func_8544'] = func_8544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8544_call = mutated_mod.get_global_var('func_8544')
call_8545 = func_8544_call()
output = call_8545
func_8546 = relay.Function([], output)
mutated_mod['func_8546'] = func_8546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mod.get_global_var('func_458')
func_460_call = mutated_mod.get_global_var('func_460')
call_8572 = func_458_call()
call_8573 = func_458_call()
func_699_call = mod.get_global_var('func_699')
func_701_call = mutated_mod.get_global_var('func_701')
const_8592 = relay.const(-7, dtype = "int64")#candidate|8592|()|const|int64
call_8591 = relay.TupleGetItem(func_699_call(relay.reshape(const_8592.astype('int64'), [])), 0)
call_8593 = relay.TupleGetItem(func_701_call(relay.reshape(const_8592.astype('int64'), [])), 0)
output = relay.Tuple([call_8572,call_8591,const_8592,])
output2 = relay.Tuple([call_8573,call_8593,const_8592,])
func_8604 = relay.Function([], output)
mod['func_8604'] = func_8604
mod = relay.transform.InferType()(mod)
mutated_mod['func_8604'] = func_8604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8604_call = mutated_mod.get_global_var('func_8604')
call_8605 = func_8604_call()
output = call_8605
func_8606 = relay.Function([], output)
mutated_mod['func_8606'] = func_8606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4533_call = mod.get_global_var('func_4533')
func_4534_call = mutated_mod.get_global_var('func_4534')
call_8704 = relay.TupleGetItem(func_4533_call(), 0)
call_8705 = relay.TupleGetItem(func_4534_call(), 0)
output = relay.Tuple([call_8704,])
output2 = relay.Tuple([call_8705,])
func_8718 = relay.Function([], output)
mod['func_8718'] = func_8718
mod = relay.transform.InferType()(mod)
mutated_mod['func_8718'] = func_8718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8718_call = mutated_mod.get_global_var('func_8718')
call_8719 = func_8718_call()
output = call_8719
func_8720 = relay.Function([], output)
mutated_mod['func_8720'] = func_8720
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8847 = relay.var("var_8847", dtype = "float32", shape = (3, 16, 10))#candidate|8847|(3, 16, 10)|var|float32
uop_8848 = relay.acos(var_8847.astype('float32')) # shape=(3, 16, 10)
output = uop_8848
output2 = uop_8848
F = relay.Function([var_8847,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8847,], output2)
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
