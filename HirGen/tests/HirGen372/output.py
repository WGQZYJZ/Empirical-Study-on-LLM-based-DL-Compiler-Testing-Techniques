import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_201 = relay.const([[[5.997102],[7.502273]],[[-6.034609],[1.807373]],[[-3.614950],[1.429258]],[[-6.659972],[-9.500453]],[[4.139578],[7.034395]],[[-6.673233],[-8.885316]]], dtype = "float32")#candidate|201|(6, 2, 1)|const|float32
uop_202 = relay.log2(const_201.astype('float32')) # shape=(6, 2, 1)
uop_227 = relay.cosh(const_201.astype('float32')) # shape=(6, 2, 1)
output = relay.Tuple([uop_202,uop_227,])
output2 = relay.Tuple([uop_202,uop_227,])
func_237 = relay.Function([], output)
mod['func_237'] = func_237
mod = relay.transform.InferType()(mod)
mutated_mod['func_237'] = func_237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_237_call = mutated_mod.get_global_var('func_237')
call_238 = func_237_call()
output = call_238
func_239 = relay.Function([], output)
mutated_mod['func_239'] = func_239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_237_call = mod.get_global_var('func_237')
func_239_call = mutated_mod.get_global_var('func_239')
call_317 = relay.TupleGetItem(func_237_call(), 1)
call_318 = relay.TupleGetItem(func_239_call(), 1)
func_237_call = mod.get_global_var('func_237')
func_239_call = mutated_mod.get_global_var('func_239')
call_331 = relay.TupleGetItem(func_237_call(), 0)
call_332 = relay.TupleGetItem(func_239_call(), 0)
uop_336 = relay.atan(call_317.astype('float64')) # shape=(6, 2, 1)
uop_338 = relay.atan(call_318.astype('float64')) # shape=(6, 2, 1)
func_237_call = mod.get_global_var('func_237')
func_239_call = mutated_mod.get_global_var('func_239')
call_339 = relay.TupleGetItem(func_237_call(), 1)
call_340 = relay.TupleGetItem(func_239_call(), 1)
output = relay.Tuple([call_331,uop_336,call_339,])
output2 = relay.Tuple([call_332,uop_338,call_340,])
func_341 = relay.Function([], output)
mod['func_341'] = func_341
mod = relay.transform.InferType()(mod)
output = func_341()
func_342 = relay.Function([], output)
mutated_mod['func_342'] = func_342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_237_call = mod.get_global_var('func_237')
func_239_call = mutated_mod.get_global_var('func_239')
call_413 = relay.TupleGetItem(func_237_call(), 1)
call_414 = relay.TupleGetItem(func_239_call(), 1)
func_341_call = mod.get_global_var('func_341')
func_342_call = mutated_mod.get_global_var('func_342')
call_420 = relay.TupleGetItem(func_341_call(), 0)
call_421 = relay.TupleGetItem(func_342_call(), 0)
uop_431 = relay.sin(call_420.astype('float64')) # shape=(6, 2, 1)
uop_433 = relay.sin(call_421.astype('float64')) # shape=(6, 2, 1)
bop_435 = relay.greater_equal(uop_431.astype('bool'), relay.reshape(call_420.astype('bool'), relay.shape_of(uop_431))) # shape=(6, 2, 1)
bop_438 = relay.greater_equal(uop_433.astype('bool'), relay.reshape(call_421.astype('bool'), relay.shape_of(uop_433))) # shape=(6, 2, 1)
output = relay.Tuple([call_413,bop_435,])
output2 = relay.Tuple([call_414,bop_438,])
func_448 = relay.Function([], output)
mod['func_448'] = func_448
mod = relay.transform.InferType()(mod)
mutated_mod['func_448'] = func_448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mutated_mod.get_global_var('func_448')
call_449 = func_448_call()
output = call_449
func_450 = relay.Function([], output)
mutated_mod['func_450'] = func_450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_341_call = mod.get_global_var('func_341')
func_342_call = mutated_mod.get_global_var('func_342')
call_454 = relay.TupleGetItem(func_341_call(), 1)
call_455 = relay.TupleGetItem(func_342_call(), 1)
output = call_454
output2 = call_455
func_465 = relay.Function([], output)
mod['func_465'] = func_465
mod = relay.transform.InferType()(mod)
mutated_mod['func_465'] = func_465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mutated_mod.get_global_var('func_465')
call_466 = func_465_call()
output = call_466
func_467 = relay.Function([], output)
mutated_mod['func_467'] = func_467
mutated_mod = relay.transform.InferType()(mutated_mod)
var_505 = relay.var("var_505", dtype = "float32", shape = (13, 4, 7))#candidate|505|(13, 4, 7)|var|float32
uop_506 = relay.sinh(var_505.astype('float32')) # shape=(13, 4, 7)
uop_508 = relay.sin(var_505.astype('float32')) # shape=(13, 4, 7)
output = relay.Tuple([uop_506,uop_508,])
output2 = relay.Tuple([uop_506,uop_508,])
func_525 = relay.Function([var_505,], output)
mod['func_525'] = func_525
mod = relay.transform.InferType()(mod)
mutated_mod['func_525'] = func_525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_526 = relay.var("var_526", dtype = "float32", shape = (13, 4, 7))#candidate|526|(13, 4, 7)|var|float32
func_525_call = mutated_mod.get_global_var('func_525')
call_527 = func_525_call(var_526)
output = call_527
func_528 = relay.Function([var_526], output)
mutated_mod['func_528'] = func_528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_530 = relay.var("var_530", dtype = "float64", shape = ())#candidate|530|()|var|float64
var_531 = relay.var("var_531", dtype = "float64", shape = (3, 2, 15))#candidate|531|(3, 2, 15)|var|float64
bop_532 = relay.equal(var_530.astype('bool'), var_531.astype('bool')) # shape=(3, 2, 15)
output = bop_532
output2 = bop_532
func_535 = relay.Function([var_530,var_531,], output)
mod['func_535'] = func_535
mod = relay.transform.InferType()(mod)
var_536 = relay.var("var_536", dtype = "float64", shape = ())#candidate|536|()|var|float64
var_537 = relay.var("var_537", dtype = "float64", shape = (3, 2, 15))#candidate|537|(3, 2, 15)|var|float64
output = func_535(var_536,var_537,)
func_538 = relay.Function([var_536,var_537,], output)
mutated_mod['func_538'] = func_538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_341_call = mod.get_global_var('func_341')
func_342_call = mutated_mod.get_global_var('func_342')
call_540 = relay.TupleGetItem(func_341_call(), 2)
call_541 = relay.TupleGetItem(func_342_call(), 2)
const_547 = relay.const([[[5.019566],[-9.489592]],[[3.185784],[-7.954815]],[[7.323197],[8.897719]],[[-4.141701],[-7.211395]],[[-0.672302],[-9.231157]],[[-6.793905],[2.883847]]], dtype = "float32")#candidate|547|(6, 2, 1)|const|float32
bop_548 = relay.logical_xor(call_540.astype('uint8'), relay.reshape(const_547.astype('uint8'), relay.shape_of(call_540))) # shape=(6, 2, 1)
bop_551 = relay.logical_xor(call_541.astype('uint8'), relay.reshape(const_547.astype('uint8'), relay.shape_of(call_541))) # shape=(6, 2, 1)
bop_557 = relay.not_equal(bop_548.astype('bool'), relay.reshape(const_547.astype('bool'), relay.shape_of(bop_548))) # shape=(6, 2, 1)
bop_560 = relay.not_equal(bop_551.astype('bool'), relay.reshape(const_547.astype('bool'), relay.shape_of(bop_551))) # shape=(6, 2, 1)
output = bop_557
output2 = bop_560
func_566 = relay.Function([], output)
mod['func_566'] = func_566
mod = relay.transform.InferType()(mod)
mutated_mod['func_566'] = func_566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mutated_mod.get_global_var('func_566')
call_567 = func_566_call()
output = call_567
func_568 = relay.Function([], output)
mutated_mod['func_568'] = func_568
mutated_mod = relay.transform.InferType()(mutated_mod)
var_614 = relay.var("var_614", dtype = "uint8", shape = (6, 3, 1))#candidate|614|(6, 3, 1)|var|uint8
var_615 = relay.var("var_615", dtype = "uint8", shape = (6, 3, 6))#candidate|615|(6, 3, 6)|var|uint8
bop_616 = relay.bitwise_or(var_614.astype('uint8'), var_615.astype('uint8')) # shape=(6, 3, 6)
uop_619 = relay.sin(bop_616.astype('float32')) # shape=(6, 3, 6)
output = uop_619
output2 = uop_619
func_623 = relay.Function([var_614,var_615,], output)
mod['func_623'] = func_623
mod = relay.transform.InferType()(mod)
var_624 = relay.var("var_624", dtype = "uint8", shape = (6, 3, 1))#candidate|624|(6, 3, 1)|var|uint8
var_625 = relay.var("var_625", dtype = "uint8", shape = (6, 3, 6))#candidate|625|(6, 3, 6)|var|uint8
output = func_623(var_624,var_625,)
func_626 = relay.Function([var_624,var_625,], output)
mutated_mod['func_626'] = func_626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_341_call = mod.get_global_var('func_341')
func_342_call = mutated_mod.get_global_var('func_342')
call_651 = relay.TupleGetItem(func_341_call(), 0)
call_652 = relay.TupleGetItem(func_342_call(), 0)
func_341_call = mod.get_global_var('func_341')
func_342_call = mutated_mod.get_global_var('func_342')
call_669 = relay.TupleGetItem(func_341_call(), 2)
call_670 = relay.TupleGetItem(func_342_call(), 2)
output = relay.Tuple([call_651,call_669,])
output2 = relay.Tuple([call_652,call_670,])
func_691 = relay.Function([], output)
mod['func_691'] = func_691
mod = relay.transform.InferType()(mod)
mutated_mod['func_691'] = func_691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_691_call = mutated_mod.get_global_var('func_691')
call_692 = func_691_call()
output = call_692
func_693 = relay.Function([], output)
mutated_mod['func_693'] = func_693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_711 = relay.TupleGetItem(func_448_call(), 0)
call_712 = relay.TupleGetItem(func_450_call(), 0)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_718 = func_465_call()
call_719 = func_465_call()
output = relay.Tuple([call_711,call_718,])
output2 = relay.Tuple([call_712,call_719,])
func_723 = relay.Function([], output)
mod['func_723'] = func_723
mod = relay.transform.InferType()(mod)
output = func_723()
func_724 = relay.Function([], output)
mutated_mod['func_724'] = func_724
mutated_mod = relay.transform.InferType()(mutated_mod)
var_790 = relay.var("var_790", dtype = "float64", shape = (12, 11, 3))#candidate|790|(12, 11, 3)|var|float64
uop_791 = relay.cosh(var_790.astype('float64')) # shape=(12, 11, 3)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_799 = relay.TupleGetItem(func_448_call(), 1)
call_800 = relay.TupleGetItem(func_450_call(), 1)
func_566_call = mod.get_global_var('func_566')
func_568_call = mutated_mod.get_global_var('func_568')
call_804 = func_566_call()
call_805 = func_566_call()
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_811 = relay.TupleGetItem(func_448_call(), 0)
call_812 = relay.TupleGetItem(func_450_call(), 0)
bop_826 = relay.power(call_804.astype('float64'), relay.reshape(call_811.astype('float64'), relay.shape_of(call_804))) # shape=(6, 2, 1)
bop_829 = relay.power(call_805.astype('float64'), relay.reshape(call_812.astype('float64'), relay.shape_of(call_805))) # shape=(6, 2, 1)
func_623_call = mod.get_global_var('func_623')
func_626_call = mutated_mod.get_global_var('func_626')
var_865 = relay.var("var_865", dtype = "uint8", shape = (6, 3))#candidate|865|(6, 3)|var|uint8
var_866 = relay.var("var_866", dtype = "uint8", shape = (108,))#candidate|866|(108,)|var|uint8
call_864 = func_623_call(relay.reshape(var_865.astype('uint8'), [6, 3, 1]), relay.reshape(var_866.astype('uint8'), [6, 3, 6]), )
call_867 = func_623_call(relay.reshape(var_865.astype('uint8'), [6, 3, 1]), relay.reshape(var_866.astype('uint8'), [6, 3, 6]), )
output = relay.Tuple([uop_791,call_799,bop_826,call_864,var_865,var_866,])
output2 = relay.Tuple([uop_791,call_800,bop_829,call_867,var_865,var_866,])
func_891 = relay.Function([var_790,var_865,var_866,], output)
mod['func_891'] = func_891
mod = relay.transform.InferType()(mod)
mutated_mod['func_891'] = func_891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_891_call = mutated_mod.get_global_var('func_891')
var_893 = relay.var("var_893", dtype = "float64", shape = (12, 11, 3))#candidate|893|(12, 11, 3)|var|float64
var_894 = relay.var("var_894", dtype = "uint8", shape = (6, 3))#candidate|894|(6, 3)|var|uint8
var_895 = relay.var("var_895", dtype = "uint8", shape = (108,))#candidate|895|(108,)|var|uint8
call_892 = func_891_call(var_893,var_894,var_895,)
output = call_892
func_896 = relay.Function([var_893,var_894,var_895,], output)
mutated_mod['func_896'] = func_896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_939 = func_465_call()
call_940 = func_465_call()
output = call_939
output2 = call_940
func_941 = relay.Function([], output)
mod['func_941'] = func_941
mod = relay.transform.InferType()(mod)
mutated_mod['func_941'] = func_941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mutated_mod.get_global_var('func_941')
call_942 = func_941_call()
output = call_942
func_943 = relay.Function([], output)
mutated_mod['func_943'] = func_943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_959 = func_465_call()
call_960 = func_465_call()
output = call_959
output2 = call_960
func_964 = relay.Function([], output)
mod['func_964'] = func_964
mod = relay.transform.InferType()(mod)
output = func_964()
func_965 = relay.Function([], output)
mutated_mod['func_965'] = func_965
mutated_mod = relay.transform.InferType()(mutated_mod)
var_976 = relay.var("var_976", dtype = "uint32", shape = (1, 13, 8))#candidate|976|(1, 13, 8)|var|uint32
const_977 = relay.const([[[1,-3,-4,-4,2,10,-7,-8],[-3,-8,4,6,-9,-4,9,4],[-7,-6,-10,4,8,-5,-4,-8],[3,9,6,-5,-2,-1,-2,-1],[-2,10,9,3,-7,-4,3,-1],[-10,4,-6,2,-2,1,5,-1],[-10,8,8,-7,-10,-7,7,-9],[-6,2,4,2,-6,-7,6,10],[2,5,9,-4,-7,4,-9,-10],[8,9,-5,-7,5,-1,-6,6],[7,8,7,7,-5,7,-5,-10],[-8,-6,-1,1,-9,-6,-3,4],[4,-8,-6,-5,9,4,9,-9]],[[-3,10,-10,-10,5,-3,-8,10],[1,-5,4,-7,-3,7,4,-1],[-2,3,-3,-8,-8,-7,-2,-10],[-5,-7,6,4,-4,3,8,7],[4,2,4,6,-3,-2,-9,7],[7,5,-7,-3,1,-8,-2,10],[8,3,-2,-8,1,-1,10,4],[-1,1,9,8,3,-10,-3,-1],[4,5,-3,2,-10,-4,-10,-10],[-7,-8,8,-6,-2,-4,-9,-7],[8,-9,-4,-7,-4,7,-9,-5],[-1,-5,-9,-7,-7,7,7,9],[6,8,-10,6,-10,-8,-1,7]],[[7,8,3,8,-10,8,-7,-5],[-6,4,-10,10,1,-8,4,-4],[-7,9,-10,10,10,-5,6,1],[-3,-7,-5,-4,6,1,-9,-1],[7,-8,6,5,7,-4,-2,-4],[2,-1,-8,-3,8,4,-9,4],[6,-3,2,-8,-9,-10,7,-9],[5,4,-4,-8,3,10,9,-9],[7,-7,9,-8,8,-3,-3,-4],[2,-4,6,-1,-5,2,6,-3],[3,-4,5,-3,3,10,10,-6],[1,-1,3,-6,4,6,-9,-4],[9,7,9,9,-7,10,10,-2]],[[-6,-7,-6,9,3,9,-2,-6],[-9,7,2,2,2,7,-7,-4],[-1,-4,-4,-6,-8,-10,-5,3],[7,4,5,-9,9,10,4,-3],[-5,-1,-1,7,-1,2,-3,-10],[7,10,-3,1,-4,9,5,4],[-8,10,-3,9,-3,-9,-7,5],[-4,-6,-5,-8,7,10,9,3],[-10,-7,9,-4,-8,-7,4,7],[-10,-5,-9,5,-2,10,-6,1],[6,-8,5,-7,6,7,7,-8],[-8,-1,5,7,-10,1,9,-3],[-3,2,-2,-10,-5,8,3,-9]],[[8,10,-8,5,3,6,-9,9],[-10,1,-9,4,-9,6,-10,-3],[-8,4,-9,6,6,-3,4,8],[-2,8,9,7,-6,-10,-1,5],[-5,7,-9,-3,8,-1,-8,6],[5,5,-8,1,-7,-2,-3,10],[-7,9,4,2,-10,4,-1,9],[-6,1,-7,10,3,-4,9,4],[1,-4,7,-6,-9,4,1,-6],[-8,-3,-9,-10,-4,-1,-6,-1],[-6,3,10,-10,-2,-1,-8,1],[5,-2,6,-9,4,-3,2,-1],[-8,-4,6,9,8,10,-8,5]],[[-5,-10,-9,-1,-8,7,-10,-10],[5,-7,10,8,8,8,-8,-1],[-8,-2,-9,-1,-9,7,-7,8],[-3,-10,2,2,5,-10,-1,-6],[10,-7,2,6,-4,-1,-9,2],[3,-4,-9,7,-6,-7,-7,-9],[10,8,4,3,6,-1,-10,-7],[-3,8,-9,8,-3,6,7,-7],[-1,-8,6,3,3,6,-4,-6],[6,-1,-2,-2,-3,3,4,-6],[2,8,-3,-9,-4,10,8,9],[4,10,-8,-9,1,-10,1,-9],[-9,-10,-7,-9,-5,-1,8,10]],[[-9,-8,-3,9,-8,-8,-6,-1],[-4,-9,3,4,-8,-5,-6,-8],[3,5,10,9,-6,8,-4,8],[1,10,5,4,-2,10,1,-4],[-2,2,4,4,8,1,1,1],[7,8,7,5,-10,-7,3,-7],[4,-8,9,-8,6,-1,1,10],[3,-1,-1,-10,-3,2,-2,-10],[-8,-5,-4,6,-4,-6,-8,4],[6,2,4,-8,2,-3,-1,-1],[5,10,8,-7,4,9,10,5],[-9,-3,2,-1,3,9,7,7],[-7,-9,-4,7,-10,1,-10,-5]],[[-5,5,10,-10,-8,-9,10,-8],[2,1,-6,3,7,-7,2,7],[10,3,-5,-7,3,-9,1,-9],[5,-8,-2,-8,-6,-5,4,-4],[-3,-8,-1,3,-10,-6,-2,-3],[-8,-9,-3,9,-9,-8,6,9],[10,-2,-4,-4,9,-5,-6,9],[9,-4,4,-10,8,8,-1,-5],[-6,-1,-4,-5,4,6,-6,5],[5,-6,1,-4,7,4,8,-8],[-8,7,3,-7,-1,8,-9,3],[-10,-3,-8,-1,8,2,7,-2],[-8,-7,10,7,-4,-1,7,7]],[[4,2,6,6,1,9,7,-10],[-10,-3,10,4,-4,-9,8,10],[-5,-3,-6,-4,-8,-2,4,-7],[1,-9,-1,-7,7,-5,1,8],[-8,8,1,-8,4,-3,3,7],[9,7,8,-4,-9,1,-6,7],[-1,5,-6,10,-4,10,-2,-1],[2,10,1,6,-6,-1,5,6],[2,7,-6,-8,1,-8,-7,-3],[-9,1,-8,-4,-4,-7,-3,-5],[6,-3,-1,5,-2,-5,3,10],[-3,-4,7,-7,10,-10,-1,-10],[-8,-1,3,-3,8,4,7,3]],[[-6,-5,2,-4,8,-7,-8,5],[-9,5,4,-9,-5,4,-8,4],[-4,6,2,10,3,-8,4,7],[2,7,9,8,8,7,-1,-9],[1,2,-5,-3,2,1,5,-1],[-1,10,-4,-5,-2,-8,5,-9],[1,10,-8,4,4,-5,-5,-3],[7,-6,4,3,6,-1,9,7],[-3,-5,2,10,5,5,6,-6],[-1,-3,-4,3,10,-10,3,-8],[-8,9,2,-6,-7,-9,-8,5],[7,-6,-8,10,-2,6,10,4],[-7,-8,4,-8,-6,5,1,-5]]], dtype = "uint32")#candidate|977|(10, 13, 8)|const|uint32
bop_978 = relay.bitwise_or(var_976.astype('uint32'), const_977.astype('uint32')) # shape=(10, 13, 8)
output = bop_978
output2 = bop_978
func_984 = relay.Function([var_976,], output)
mod['func_984'] = func_984
mod = relay.transform.InferType()(mod)
mutated_mod['func_984'] = func_984
mutated_mod = relay.transform.InferType()(mutated_mod)
var_985 = relay.var("var_985", dtype = "uint32", shape = (1, 13, 8))#candidate|985|(1, 13, 8)|var|uint32
func_984_call = mutated_mod.get_global_var('func_984')
call_986 = func_984_call(var_985)
output = call_986
func_987 = relay.Function([var_985], output)
mutated_mod['func_987'] = func_987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
call_991 = func_941_call()
call_992 = func_941_call()
output = call_991
output2 = call_992
func_995 = relay.Function([], output)
mod['func_995'] = func_995
mod = relay.transform.InferType()(mod)
output = func_995()
func_996 = relay.Function([], output)
mutated_mod['func_996'] = func_996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_1011 = relay.TupleGetItem(func_448_call(), 1)
call_1012 = relay.TupleGetItem(func_450_call(), 1)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_1017 = func_465_call()
call_1018 = func_465_call()
func_535_call = mod.get_global_var('func_535')
func_538_call = mutated_mod.get_global_var('func_538')
var_1025 = relay.var("var_1025", dtype = "float64", shape = ())#candidate|1025|()|var|float64
var_1026 = relay.var("var_1026", dtype = "float64", shape = (90,))#candidate|1026|(90,)|var|float64
call_1024 = func_535_call(relay.reshape(var_1025.astype('float64'), []), relay.reshape(var_1026.astype('float64'), [3, 2, 15]), )
call_1027 = func_535_call(relay.reshape(var_1025.astype('float64'), []), relay.reshape(var_1026.astype('float64'), [3, 2, 15]), )
func_723_call = mod.get_global_var('func_723')
func_724_call = mutated_mod.get_global_var('func_724')
call_1029 = relay.TupleGetItem(func_723_call(), 1)
call_1030 = relay.TupleGetItem(func_724_call(), 1)
var_1032 = relay.var("var_1032", dtype = "float64", shape = (6, 2, 10))#candidate|1032|(6, 2, 10)|var|float64
bop_1033 = relay.bitwise_or(call_1017.astype('uint32'), var_1032.astype('uint32')) # shape=(6, 2, 10)
bop_1036 = relay.bitwise_or(call_1018.astype('uint32'), var_1032.astype('uint32')) # shape=(6, 2, 10)
output = relay.Tuple([call_1011,call_1024,var_1025,var_1026,call_1029,bop_1033,])
output2 = relay.Tuple([call_1012,call_1027,var_1025,var_1026,call_1030,bop_1036,])
func_1039 = relay.Function([var_1025,var_1026,var_1032,], output)
mod['func_1039'] = func_1039
mod = relay.transform.InferType()(mod)
var_1040 = relay.var("var_1040", dtype = "float64", shape = ())#candidate|1040|()|var|float64
var_1041 = relay.var("var_1041", dtype = "float64", shape = (90,))#candidate|1041|(90,)|var|float64
var_1042 = relay.var("var_1042", dtype = "float64", shape = (6, 2, 10))#candidate|1042|(6, 2, 10)|var|float64
output = func_1039(var_1040,var_1041,var_1042,)
func_1043 = relay.Function([var_1040,var_1041,var_1042,], output)
mutated_mod['func_1043'] = func_1043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_691_call = mod.get_global_var('func_691')
func_693_call = mutated_mod.get_global_var('func_693')
call_1067 = relay.TupleGetItem(func_691_call(), 1)
call_1068 = relay.TupleGetItem(func_693_call(), 1)
output = call_1067
output2 = call_1068
func_1084 = relay.Function([], output)
mod['func_1084'] = func_1084
mod = relay.transform.InferType()(mod)
output = func_1084()
func_1085 = relay.Function([], output)
mutated_mod['func_1085'] = func_1085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_1124 = func_995_call()
call_1125 = func_995_call()
output = relay.Tuple([call_1124,])
output2 = relay.Tuple([call_1125,])
func_1139 = relay.Function([], output)
mod['func_1139'] = func_1139
mod = relay.transform.InferType()(mod)
mutated_mod['func_1139'] = func_1139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1139_call = mutated_mod.get_global_var('func_1139')
call_1140 = func_1139_call()
output = call_1140
func_1141 = relay.Function([], output)
mutated_mod['func_1141'] = func_1141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1139_call = mod.get_global_var('func_1139')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1148 = relay.TupleGetItem(func_1139_call(), 0)
call_1149 = relay.TupleGetItem(func_1141_call(), 0)
func_691_call = mod.get_global_var('func_691')
func_693_call = mutated_mod.get_global_var('func_693')
call_1162 = relay.TupleGetItem(func_691_call(), 0)
call_1163 = relay.TupleGetItem(func_693_call(), 0)
uop_1174 = relay.asin(call_1148.astype('float32')) # shape=(6, 2, 1)
uop_1176 = relay.asin(call_1149.astype('float32')) # shape=(6, 2, 1)
func_984_call = mod.get_global_var('func_984')
func_987_call = mutated_mod.get_global_var('func_987')
const_1184 = relay.const([[7,6,6,6,7,5,9,-5,3,9,-10,5,-8,5,-2,-2,2,9,-9,1,-5,9,6,-8,-7,9,5,1,4,-9,-10,7,8,1,-1,5,-1,-9,2,7,4,5,10,7,9,-2,7,-4,-5,2,9,9],[-4,10,6,3,3,-3,3,9,-4,-4,10,5,3,9,-5,-6,9,-2,3,-6,3,-9,7,-8,-7,-3,-10,-2,4,-7,-2,-7,-8,5,-4,8,-10,4,5,10,6,-10,-2,9,6,6,-10,-8,-1,2,5,3]], dtype = "uint32")#candidate|1184|(2, 52)|const|uint32
call_1183 = func_984_call(relay.reshape(const_1184.astype('uint32'), [1, 13, 8]))
call_1185 = func_984_call(relay.reshape(const_1184.astype('uint32'), [1, 13, 8]))
output = relay.Tuple([call_1162,uop_1174,call_1183,const_1184,])
output2 = relay.Tuple([call_1163,uop_1176,call_1185,const_1184,])
func_1186 = relay.Function([], output)
mod['func_1186'] = func_1186
mod = relay.transform.InferType()(mod)
output = func_1186()
func_1187 = relay.Function([], output)
mutated_mod['func_1187'] = func_1187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
call_1219 = func_941_call()
call_1220 = func_941_call()
output = call_1219
output2 = call_1220
func_1226 = relay.Function([], output)
mod['func_1226'] = func_1226
mod = relay.transform.InferType()(mod)
output = func_1226()
func_1227 = relay.Function([], output)
mutated_mod['func_1227'] = func_1227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mod.get_global_var('func_566')
func_568_call = mutated_mod.get_global_var('func_568')
call_1254 = func_566_call()
call_1255 = func_566_call()
func_1139_call = mod.get_global_var('func_1139')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1256 = relay.TupleGetItem(func_1139_call(), 0)
call_1257 = relay.TupleGetItem(func_1141_call(), 0)
output = relay.Tuple([call_1254,call_1256,])
output2 = relay.Tuple([call_1255,call_1257,])
func_1275 = relay.Function([], output)
mod['func_1275'] = func_1275
mod = relay.transform.InferType()(mod)
output = func_1275()
func_1276 = relay.Function([], output)
mutated_mod['func_1276'] = func_1276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_1301 = func_465_call()
call_1302 = func_465_call()
func_1275_call = mod.get_global_var('func_1275')
func_1276_call = mutated_mod.get_global_var('func_1276')
call_1305 = relay.TupleGetItem(func_1275_call(), 0)
call_1306 = relay.TupleGetItem(func_1276_call(), 0)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_1313 = func_995_call()
call_1314 = func_995_call()
output = relay.Tuple([call_1301,call_1305,call_1313,])
output2 = relay.Tuple([call_1302,call_1306,call_1314,])
func_1330 = relay.Function([], output)
mod['func_1330'] = func_1330
mod = relay.transform.InferType()(mod)
output = func_1330()
func_1331 = relay.Function([], output)
mutated_mod['func_1331'] = func_1331
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1337 = relay.const([[[7.389196],[-7.005580],[-4.053107],[5.422208]],[[-9.528174],[2.406092],[4.018465],[-7.365422]],[[0.637914],[1.661755],[3.240201],[1.403539]],[[1.441523],[4.736371],[-5.129171],[-2.463290]],[[-6.658293],[6.300266],[-1.151402],[-5.507279]],[[1.294601],[2.715647],[7.557331],[-4.318501]],[[-4.360063],[-8.441985],[1.324503],[-2.756846]],[[6.314866],[1.920839],[-9.436046],[8.842865]],[[-9.305876],[8.327059],[-3.139960],[-5.788061]],[[4.488058],[-1.861945],[4.378589],[3.041292]],[[-2.410425],[-3.389391],[1.242012],[-9.394038]]], dtype = "float32")#candidate|1337|(11, 4, 1)|const|float32
var_1338 = relay.var("var_1338", dtype = "float32", shape = (11, 4, 12))#candidate|1338|(11, 4, 12)|var|float32
bop_1339 = relay.floor_mod(const_1337.astype('float32'), var_1338.astype('float32')) # shape=(11, 4, 12)
output = relay.Tuple([bop_1339,])
output2 = relay.Tuple([bop_1339,])
func_1345 = relay.Function([var_1338,], output)
mod['func_1345'] = func_1345
mod = relay.transform.InferType()(mod)
var_1346 = relay.var("var_1346", dtype = "float32", shape = (11, 4, 12))#candidate|1346|(11, 4, 12)|var|float32
output = func_1345(var_1346)
func_1347 = relay.Function([var_1346], output)
mutated_mod['func_1347'] = func_1347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_1370 = relay.TupleGetItem(func_1186_call(), 2)
call_1371 = relay.TupleGetItem(func_1187_call(), 2)
func_891_call = mod.get_global_var('func_891')
func_896_call = mutated_mod.get_global_var('func_896')
var_1373 = relay.var("var_1373", dtype = "float64", shape = (396,))#candidate|1373|(396,)|var|float64
var_1374 = relay.var("var_1374", dtype = "uint8", shape = (18,))#candidate|1374|(18,)|var|uint8
var_1375 = relay.var("var_1375", dtype = "uint8", shape = (108,))#candidate|1375|(108,)|var|uint8
call_1372 = relay.TupleGetItem(func_891_call(relay.reshape(var_1373.astype('float64'), [12, 11, 3]), relay.reshape(var_1374.astype('uint8'), [6, 3]), relay.reshape(var_1375.astype('uint8'), [108,]), ), 1)
call_1376 = relay.TupleGetItem(func_896_call(relay.reshape(var_1373.astype('float64'), [12, 11, 3]), relay.reshape(var_1374.astype('uint8'), [6, 3]), relay.reshape(var_1375.astype('uint8'), [108,]), ), 1)
output = relay.Tuple([call_1370,call_1372,var_1373,var_1374,var_1375,])
output2 = relay.Tuple([call_1371,call_1376,var_1373,var_1374,var_1375,])
func_1388 = relay.Function([var_1373,var_1374,var_1375,], output)
mod['func_1388'] = func_1388
mod = relay.transform.InferType()(mod)
var_1389 = relay.var("var_1389", dtype = "float64", shape = (396,))#candidate|1389|(396,)|var|float64
var_1390 = relay.var("var_1390", dtype = "uint8", shape = (18,))#candidate|1390|(18,)|var|uint8
var_1391 = relay.var("var_1391", dtype = "uint8", shape = (108,))#candidate|1391|(108,)|var|uint8
output = func_1388(var_1389,var_1390,var_1391,)
func_1392 = relay.Function([var_1389,var_1390,var_1391,], output)
mutated_mod['func_1392'] = func_1392
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1409 = relay.const([[[2.335843,0.129873,0.793951,2.194344,-3.907439,-6.878511],[-9.319570,7.763888,2.116259,7.965847,-6.220979,9.724224],[7.002475,6.114338,1.765151,-5.589029,3.345350,-3.180883],[4.115790,-8.622649,-3.981607,1.259145,9.310173,9.199512],[0.022289,-2.098731,2.853210,-2.434488,-0.770576,-2.176422],[9.980001,-3.368285,-5.585373,3.212840,7.554844,5.446210],[-9.361634,-3.817582,8.161839,-6.270896,4.221210,-3.549198],[-6.091484,2.052389,-9.971687,-3.957631,-5.823018,3.588953],[-7.431175,5.391845,-4.091622,9.444117,8.402439,-1.689729],[9.575939,2.515379,1.675113,0.200867,2.355518,-7.707917],[-7.373619,2.902763,-8.171541,6.701444,7.741274,-3.959980]],[[7.390333,-0.909671,8.487242,-7.223611,4.680820,2.689047],[9.271771,-7.083970,-4.171404,1.705066,-8.362184,3.298613],[0.448135,5.722792,4.532622,-9.124439,5.943651,-5.393188],[6.815473,3.128329,-8.618807,-2.261833,-3.728945,-3.255358],[7.591985,1.538022,-6.383182,-4.518902,-7.439126,-3.683926],[6.167602,-9.873882,5.615323,-8.533308,7.866316,5.749505],[-3.055448,-3.610457,5.297010,6.031351,-3.739289,-0.647362],[-8.150168,-8.159096,-4.589668,-3.048246,2.222566,-5.054399],[6.732241,3.970990,-2.545556,7.996060,-4.535617,9.207890],[-3.344753,5.064630,-4.629787,-3.908501,-5.662041,1.581408],[2.668406,5.604356,-0.362605,-6.577431,-0.988422,4.139485]],[[-9.071821,1.706556,-8.658155,-7.961164,-7.909664,1.043146],[8.830716,5.700540,-6.935394,-2.819321,-3.759150,-6.684352],[7.459339,5.540411,-2.296905,3.652620,9.862553,-7.610510],[1.993531,-0.665800,-9.220488,-7.250381,2.088567,6.214655],[-1.007778,-1.334687,2.983418,-2.076601,2.161386,-3.105885],[-2.330736,-0.379384,0.646528,7.970147,-5.184428,-2.602604],[9.440924,-6.964759,-1.907356,-2.340165,-4.254558,5.925807],[2.251409,-6.202311,0.129838,-9.487432,-4.371019,9.522261],[4.329169,0.547868,2.670451,-6.749814,-7.132645,4.922814],[8.365550,-1.594570,-8.664306,3.270122,8.685112,-8.781515],[1.092507,-7.276766,-2.294535,8.938362,-2.875295,5.542159]],[[-0.716756,-6.896232,-6.371765,7.586811,2.497810,7.578375],[1.127547,7.830090,1.483410,-0.409152,-0.180645,-8.049221],[-3.068693,4.852733,-6.243388,-4.308442,-6.161720,-1.452210],[0.739185,-3.491778,7.194964,-6.608217,6.394807,8.435355],[-4.626045,2.197112,-8.549044,1.177344,6.330929,7.900149],[5.606694,-2.763162,-3.777788,-4.971022,-7.718687,-0.296640],[6.845227,-6.282802,-9.250755,0.642681,4.419055,9.029300],[-5.887812,4.778067,1.786222,-1.521543,-7.853399,6.257479],[1.238233,-4.412517,-4.951037,2.004078,-1.626751,-7.790653],[4.009970,2.617359,-1.883025,-9.029403,2.441742,-5.587936],[-7.030837,9.576394,2.425699,9.030448,-1.580881,-6.414734]],[[-6.799455,-8.487275,-7.769913,7.534907,-3.503650,-4.546699],[7.070883,-4.823703,-8.980110,-8.969081,0.347652,-5.102772],[-4.563491,5.561123,2.759353,0.558538,6.686801,-6.096313],[6.504885,2.242191,-6.007363,-5.137283,-8.930121,-3.771591],[-4.034546,3.858640,-2.741759,-2.030353,8.247174,-0.997147],[-9.723167,-0.665529,2.617367,8.140221,-4.529876,5.448250],[-2.613464,-4.222042,-6.865513,-7.929762,9.158717,-5.837697],[2.115689,-2.160308,-6.860607,2.401834,3.665913,-1.206070],[2.515128,6.106717,-4.312852,-3.970497,-2.210132,0.518216],[-3.646636,4.929209,0.247649,9.904131,6.262877,2.734156],[-6.665479,-6.354817,-3.968681,3.504213,-9.359913,0.399640]],[[6.145574,6.911657,-3.100099,-7.100133,-0.788155,2.018603],[6.436922,-1.689086,-1.459598,-0.455260,2.059301,-6.409496],[5.167373,3.340765,-3.402444,-0.079441,-6.179878,-1.741024],[-2.017500,2.079633,-3.454551,-1.741707,-6.786643,-1.025995],[-6.296189,9.401920,0.252286,4.945482,8.710427,-7.924763],[4.851361,5.183785,2.440926,-2.548711,-3.118083,-7.045765],[-2.657535,-2.879535,-9.046922,-6.793570,4.911417,-7.298070],[4.911626,8.178996,-7.555714,4.382814,-6.461217,5.665984],[-4.497059,3.115331,-7.757971,6.800460,-9.441679,7.359321],[3.303917,1.995808,1.626177,2.883978,9.469533,-1.080202],[4.603345,9.882096,-6.128087,0.772327,6.934838,-5.377029]],[[-6.054859,-6.755833,5.144893,9.855259,5.217873,-9.743863],[-2.255196,-8.842419,-0.673819,1.137408,-2.662878,-8.390024],[-0.792106,8.925028,-7.648963,2.268597,6.003534,-8.155475],[9.128422,8.946339,-9.123873,6.185275,-1.199388,0.774447],[-5.219065,-6.231733,4.198814,-0.120532,-2.756204,2.465304],[6.655028,0.580164,7.911993,4.965176,-2.254873,8.892911],[-0.823855,6.976773,-9.012535,-1.835151,-0.839755,8.146846],[1.414994,2.938347,1.690604,-0.253473,9.943706,-1.711503],[9.489026,4.879898,-0.934017,5.288905,9.988434,8.388508],[8.462541,9.909830,-6.579484,0.294568,-5.861353,5.813537],[-0.227455,-5.021781,-8.774556,-3.607601,-6.315692,9.021548]],[[-8.157262,-2.921970,3.837499,-0.111500,8.540332,-1.142404],[-1.457319,8.197429,-0.801145,1.455010,-8.017691,-4.336991],[-9.001672,6.207471,-5.174878,1.585372,6.378187,1.975488],[-2.186437,8.894715,2.320802,0.859083,5.299967,-1.657069],[-4.862042,-4.968611,4.309551,7.895189,6.030057,-4.149320],[4.733217,7.343829,7.484111,8.443394,-6.114418,2.111343],[2.354089,1.567488,6.998941,-7.039400,3.414377,6.236043],[-3.073341,-4.265104,6.416810,5.194567,4.384267,4.465473],[9.470196,-9.537419,5.672852,6.553728,-6.376579,5.115614],[-1.423140,3.673518,6.277062,-1.779682,5.634858,6.724057],[-2.834047,8.675165,3.158899,-7.952875,-1.488001,-8.568250]],[[4.903240,-3.877228,3.647517,9.531138,1.481545,3.488583],[2.095682,-3.938437,5.982846,6.166212,0.767908,9.574104],[3.354990,0.067423,-7.388845,3.060387,-1.027083,1.187532],[-3.643901,2.011370,-3.855826,-5.032537,8.386146,-8.664198],[-4.912964,-9.476849,5.707873,4.299506,8.793669,-7.613633],[-7.206742,6.736601,4.625324,-0.678159,-3.077676,1.724113],[2.272561,-2.978491,3.368873,5.832796,9.567434,4.589321],[3.471969,7.263545,8.425127,-4.352960,-8.175719,-2.895051],[-7.506885,6.960282,3.073332,1.320946,-4.892722,0.381929],[0.740989,8.851158,-5.401650,6.536478,8.078909,-5.308816],[-9.038772,1.305884,9.343057,-5.754784,-1.090798,-2.757300]],[[-2.105740,-8.051930,4.731787,-0.921504,-8.014161,1.669204],[-7.006726,-8.453206,-6.118096,7.648078,2.059687,1.392996],[-5.235561,6.250445,9.987817,-2.541374,2.287224,-7.239001],[-1.821596,9.186807,-0.808021,3.307332,5.591638,0.570496],[3.382371,-3.685184,3.844454,8.453786,8.200205,-3.840198],[-2.843733,4.841072,-1.617958,-7.392867,-3.625738,3.791590],[2.021365,-0.081396,7.305802,-6.260146,-0.657702,8.222246],[-6.055489,6.965790,0.888335,-2.918899,2.500434,-1.882709],[0.822069,-3.802533,-5.612817,-7.125268,5.945233,1.965110],[-1.425339,7.190499,-3.181248,-6.478412,4.942850,5.140026],[-3.625037,-0.972274,3.676590,0.297940,2.000142,-3.534693]],[[2.723738,5.680476,5.706544,5.217491,-4.838361,-2.707257],[-0.920429,7.018546,0.147770,-3.054840,-8.864517,6.135848],[3.256437,-5.414050,-7.117835,2.651116,-4.303269,-4.613799],[5.193926,2.024250,-8.156686,-0.624614,1.239332,-4.486678],[-2.698874,-9.626551,2.553197,-3.421043,-9.971720,-2.154771],[-0.729055,-0.133595,-9.440825,-3.683025,2.001207,-8.157462],[-6.083346,-3.251942,-1.466840,-6.082366,2.531875,-3.145435],[-9.727948,-4.384231,5.943169,1.623198,-0.511237,-9.968855],[5.988850,-4.222504,9.402570,-3.451135,5.558858,3.295724],[-9.305598,4.783526,-4.675745,-2.247952,-1.503230,2.640683],[7.376258,1.518269,-9.880426,2.925867,4.565177,-9.950319]],[[-1.703147,-8.738846,2.957991,1.903795,5.294531,-3.539707],[-3.298307,-9.784408,0.063470,2.131443,-1.074899,-6.754847],[-6.347985,-8.295166,1.270796,-2.359856,-1.976183,0.286924],[-2.428390,9.009679,2.857743,8.175244,-3.195670,0.866369],[3.336840,7.355041,3.238849,2.990243,1.676994,6.020522],[-8.786703,-7.327491,-8.834497,5.924753,-2.650249,-7.044002],[-1.177499,-0.441089,1.604500,-2.630099,-9.929442,6.345372],[1.702182,0.001510,-0.895494,8.376417,7.580559,4.644556],[4.484913,-6.418772,0.249158,-6.601028,0.133845,3.662075],[-0.683343,9.767740,7.218083,-7.866407,5.819294,4.742509],[5.377713,5.283036,-8.974517,-4.629309,2.878768,7.798441]],[[-4.766615,-7.475571,-2.976426,-5.326842,9.171148,8.001161],[-3.233303,9.940115,-2.141151,-8.922791,2.449781,-1.442049],[-5.777847,0.849964,5.799268,7.430908,-4.185390,4.991615],[6.445087,9.571974,-3.388665,8.646316,1.999679,-8.093664],[6.156247,3.651695,-3.443961,-9.815280,-9.507200,-5.517749],[-2.530165,3.192472,1.857821,-6.794283,4.006982,7.346816],[-7.949344,-4.374551,3.958324,5.467998,3.547652,5.932318],[-3.740242,7.256603,-1.428682,6.485752,6.595678,6.677484],[7.358965,9.900032,-2.699174,-0.365727,4.683206,-3.625850],[-3.050662,1.624977,-1.063676,1.253747,-3.291501,7.653339],[5.977971,7.826243,-0.512878,2.055779,-7.840556,-5.969982]],[[-5.876004,-9.328808,1.978738,-7.347866,-1.144006,-9.597306],[4.144923,-0.873353,-7.640759,-7.222070,-1.873959,-4.233018],[-8.405913,-2.638412,-7.032104,4.037320,-0.029136,-5.883966],[-0.866937,6.384634,-1.918492,1.165977,6.174855,8.036695],[-9.294664,0.829058,1.988552,8.365312,-9.589312,5.452517],[-0.210324,1.727123,-3.601220,-8.634658,-7.175787,9.478287],[7.785645,-3.337735,-2.546546,-6.667562,9.392177,4.946050],[7.031716,1.641934,9.453743,-0.484121,5.650873,-4.425644],[8.093472,8.481503,-9.860068,-9.453324,8.292623,-2.561185],[-6.643878,-0.370332,4.144818,1.323266,-7.697204,-7.115118],[0.048655,1.821014,-6.741984,-2.086671,5.838236,8.145449]]], dtype = "float64")#candidate|1409|(14, 11, 6)|const|float64
uop_1410 = relay.sinh(const_1409.astype('float64')) # shape=(14, 11, 6)
output = uop_1410
output2 = uop_1410
func_1415 = relay.Function([], output)
mod['func_1415'] = func_1415
mod = relay.transform.InferType()(mod)
output = func_1415()
func_1416 = relay.Function([], output)
mutated_mod['func_1416'] = func_1416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1226_call = mod.get_global_var('func_1226')
func_1227_call = mutated_mod.get_global_var('func_1227')
call_1472 = func_1226_call()
call_1473 = func_1226_call()
func_341_call = mod.get_global_var('func_341')
func_342_call = mutated_mod.get_global_var('func_342')
call_1486 = relay.TupleGetItem(func_341_call(), 2)
call_1487 = relay.TupleGetItem(func_342_call(), 2)
bop_1506 = relay.mod(call_1472.astype('float32'), relay.reshape(call_1486.astype('float32'), relay.shape_of(call_1472))) # shape=(6, 2, 1)
bop_1509 = relay.mod(call_1473.astype('float32'), relay.reshape(call_1487.astype('float32'), relay.shape_of(call_1473))) # shape=(6, 2, 1)
output = bop_1506
output2 = bop_1509
func_1527 = relay.Function([], output)
mod['func_1527'] = func_1527
mod = relay.transform.InferType()(mod)
mutated_mod['func_1527'] = func_1527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1527_call = mutated_mod.get_global_var('func_1527')
call_1528 = func_1527_call()
output = call_1528
func_1529 = relay.Function([], output)
mutated_mod['func_1529'] = func_1529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_1580 = relay.TupleGetItem(func_448_call(), 0)
call_1581 = relay.TupleGetItem(func_450_call(), 0)
output = relay.Tuple([call_1580,])
output2 = relay.Tuple([call_1581,])
func_1582 = relay.Function([], output)
mod['func_1582'] = func_1582
mod = relay.transform.InferType()(mod)
output = func_1582()
func_1583 = relay.Function([], output)
mutated_mod['func_1583'] = func_1583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
call_1590 = func_1527_call()
call_1591 = func_1527_call()
func_1275_call = mod.get_global_var('func_1275')
func_1276_call = mutated_mod.get_global_var('func_1276')
call_1592 = relay.TupleGetItem(func_1275_call(), 0)
call_1593 = relay.TupleGetItem(func_1276_call(), 0)
uop_1596 = relay.exp(call_1592.astype('float64')) # shape=(6, 2, 1)
uop_1598 = relay.exp(call_1593.astype('float64')) # shape=(6, 2, 1)
func_535_call = mod.get_global_var('func_535')
func_538_call = mutated_mod.get_global_var('func_538')
var_1602 = relay.var("var_1602", dtype = "float64", shape = ())#candidate|1602|()|var|float64
const_1603 = relay.const([2.920309,-0.274839,6.429329,7.969983,0.474382,3.653007,5.291330,9.508950,2.976089,-8.738931,-7.811213,-9.917820,-4.765084,3.418945,8.438479,-8.919371,1.776521,-7.100976,-4.477733,4.060766,1.924303,3.283066,7.701113,3.762913,1.411117,8.582571,4.302264,2.993678,2.757849,-9.454511,0.917154,3.572641,9.928457,-2.058284,4.877257,9.969518,-5.990447,-9.821609,-5.760048,-2.985835,8.240234,4.306084,-8.433190,-9.513979,5.543429,-3.705805,-7.164942,-8.031059,8.466716,6.359074,-3.001704,6.965336,-7.428757,-7.492101,-9.282644,-6.293630,8.347888,-3.397800,-9.957003,0.485260,8.945396,7.273994,8.231700,3.494426,-4.148699,-2.411220,-1.191750,4.045675,9.145990,7.781851,-6.381824,2.218133,6.583404,7.224368,-2.803147,3.724517,-0.321903,3.687975,-8.093108,0.837734,-5.945572,-7.361471,6.404298,7.527822,2.055280,-6.103770,-4.378778,7.657941,-5.990643,-0.053444], dtype = "float64")#candidate|1603|(90,)|const|float64
call_1601 = func_535_call(relay.reshape(var_1602.astype('float64'), []), relay.reshape(const_1603.astype('float64'), [3, 2, 15]), )
call_1604 = func_535_call(relay.reshape(var_1602.astype('float64'), []), relay.reshape(const_1603.astype('float64'), [3, 2, 15]), )
var_1605 = relay.var("var_1605", dtype = "float64", shape = (6, 2, 1))#candidate|1605|(6, 2, 1)|var|float64
bop_1606 = relay.less_equal(uop_1596.astype('bool'), relay.reshape(var_1605.astype('bool'), relay.shape_of(uop_1596))) # shape=(6, 2, 1)
bop_1609 = relay.less_equal(uop_1598.astype('bool'), relay.reshape(var_1605.astype('bool'), relay.shape_of(uop_1598))) # shape=(6, 2, 1)
output = relay.Tuple([call_1590,call_1601,var_1602,const_1603,bop_1606,])
output2 = relay.Tuple([call_1591,call_1604,var_1602,const_1603,bop_1609,])
func_1616 = relay.Function([var_1602,var_1605,], output)
mod['func_1616'] = func_1616
mod = relay.transform.InferType()(mod)
mutated_mod['func_1616'] = func_1616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1616_call = mutated_mod.get_global_var('func_1616')
var_1618 = relay.var("var_1618", dtype = "float64", shape = ())#candidate|1618|()|var|float64
var_1619 = relay.var("var_1619", dtype = "float64", shape = (6, 2, 1))#candidate|1619|(6, 2, 1)|var|float64
call_1617 = func_1616_call(var_1618,var_1619,)
output = call_1617
func_1620 = relay.Function([var_1618,var_1619,], output)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_1650 = relay.TupleGetItem(func_448_call(), 1)
call_1651 = relay.TupleGetItem(func_450_call(), 1)
output = call_1650
output2 = call_1651
func_1654 = relay.Function([], output)
mod['func_1654'] = func_1654
mod = relay.transform.InferType()(mod)
output = func_1654()
func_1655 = relay.Function([], output)
mutated_mod['func_1655'] = func_1655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_1698 = func_1084_call()
call_1699 = func_1084_call()
output = relay.Tuple([call_1698,])
output2 = relay.Tuple([call_1699,])
func_1700 = relay.Function([], output)
mod['func_1700'] = func_1700
mod = relay.transform.InferType()(mod)
output = func_1700()
func_1701 = relay.Function([], output)
mutated_mod['func_1701'] = func_1701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_1711 = func_1084_call()
call_1712 = func_1084_call()
func_1139_call = mod.get_global_var('func_1139')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1718 = relay.TupleGetItem(func_1139_call(), 0)
call_1719 = relay.TupleGetItem(func_1141_call(), 0)
bop_1728 = relay.add(call_1711.astype('int8'), relay.reshape(call_1718.astype('int8'), relay.shape_of(call_1711))) # shape=(6, 2, 1)
bop_1731 = relay.add(call_1712.astype('int8'), relay.reshape(call_1719.astype('int8'), relay.shape_of(call_1712))) # shape=(6, 2, 1)
func_964_call = mod.get_global_var('func_964')
func_965_call = mutated_mod.get_global_var('func_965')
call_1736 = func_964_call()
call_1737 = func_964_call()
bop_1738 = relay.greater(call_1718.astype('bool'), relay.reshape(bop_1728.astype('bool'), relay.shape_of(call_1718))) # shape=(6, 2, 1)
bop_1741 = relay.greater(call_1719.astype('bool'), relay.reshape(bop_1731.astype('bool'), relay.shape_of(call_1719))) # shape=(6, 2, 1)
uop_1747 = relay.acosh(bop_1738.astype('float64')) # shape=(6, 2, 1)
uop_1749 = relay.acosh(bop_1741.astype('float64')) # shape=(6, 2, 1)
output = relay.Tuple([call_1736,uop_1747,])
output2 = relay.Tuple([call_1737,uop_1749,])
func_1751 = relay.Function([], output)
mod['func_1751'] = func_1751
mod = relay.transform.InferType()(mod)
mutated_mod['func_1751'] = func_1751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1751_call = mutated_mod.get_global_var('func_1751')
call_1752 = func_1751_call()
output = call_1752
func_1753 = relay.Function([], output)
mutated_mod['func_1753'] = func_1753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_1788 = relay.TupleGetItem(func_448_call(), 1)
call_1789 = relay.TupleGetItem(func_450_call(), 1)
output = call_1788
output2 = call_1789
func_1793 = relay.Function([], output)
mod['func_1793'] = func_1793
mod = relay.transform.InferType()(mod)
output = func_1793()
func_1794 = relay.Function([], output)
mutated_mod['func_1794'] = func_1794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_1836 = func_995_call()
call_1837 = func_995_call()
var_1844 = relay.var("var_1844", dtype = "float64", shape = (6, 2, 4))#candidate|1844|(6, 2, 4)|var|float64
bop_1845 = relay.logical_and(call_1836.astype('bool'), var_1844.astype('bool')) # shape=(6, 2, 4)
bop_1848 = relay.logical_and(call_1837.astype('bool'), var_1844.astype('bool')) # shape=(6, 2, 4)
bop_1868 = relay.power(call_1836.astype('float64'), bop_1845.astype('float64')) # shape=(6, 2, 4)
bop_1871 = relay.power(call_1837.astype('float64'), bop_1848.astype('float64')) # shape=(6, 2, 4)
func_691_call = mod.get_global_var('func_691')
func_693_call = mutated_mod.get_global_var('func_693')
call_1873 = relay.TupleGetItem(func_691_call(), 1)
call_1874 = relay.TupleGetItem(func_693_call(), 1)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
call_1881 = func_1527_call()
call_1882 = func_1527_call()
output = relay.Tuple([bop_1868,call_1873,call_1881,])
output2 = relay.Tuple([bop_1871,call_1874,call_1882,])
func_1883 = relay.Function([var_1844,], output)
mod['func_1883'] = func_1883
mod = relay.transform.InferType()(mod)
var_1884 = relay.var("var_1884", dtype = "float64", shape = (6, 2, 4))#candidate|1884|(6, 2, 4)|var|float64
output = func_1883(var_1884)
func_1885 = relay.Function([var_1884], output)
mutated_mod['func_1885'] = func_1885
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1907 = relay.const([[[-3.298918,-1.712838,8.868130,-5.575079,-6.287955,-2.166719,0.314364,-8.973284],[-3.291494,6.489020,-7.298888,-8.759554,7.942664,-8.830138,1.890318,8.244577],[-5.758821,-2.592067,-5.211539,-8.572455,9.680630,1.248829,-7.679490,-0.152345],[0.711337,-1.494635,-2.824149,0.774064,-0.948516,0.832482,-1.899581,2.834103],[-4.555362,-1.796187,-2.734642,0.540195,0.405920,-2.037790,-2.098457,8.549561],[-1.597977,0.178154,-2.882403,-5.818470,1.103663,-8.923870,-8.046411,-5.694953],[4.824028,-1.989173,3.266931,-0.194047,-9.985765,1.324229,1.129894,-8.482658],[-9.397884,-3.979136,8.461855,-7.502871,9.211571,-8.692722,-4.605361,-5.479069],[7.313359,-8.438681,5.818899,-6.964251,0.433649,-7.970614,-9.220631,4.640445],[6.198862,7.479561,-7.889972,9.660686,-6.424298,-8.690086,-6.745399,-2.482119],[7.559493,-9.541608,7.240779,-9.946784,-4.209401,-7.032539,-3.920167,-9.206229],[4.930424,-6.103860,1.786270,2.927003,9.393682,-5.916949,0.005612,9.444252],[5.897339,5.722873,-9.845757,-0.822126,-0.737527,0.363604,-7.047687,-2.859681],[8.963646,3.773852,-9.466623,-4.795528,-5.291135,1.178992,-2.337685,-7.996631],[6.242860,-8.816960,-2.986141,-9.683389,0.783381,5.039102,2.072020,-0.757440]],[[-9.556735,6.415673,-9.417277,-2.421991,7.960427,-0.834732,-6.219119,6.466279],[-3.001030,-0.909159,-7.843570,-3.612108,-8.624263,2.053324,0.948030,7.369054],[-1.716778,9.698559,-3.086077,2.380186,6.508979,2.580688,7.606645,7.648032],[9.350229,-3.705458,1.407029,2.215496,-1.496499,5.756606,-2.658312,2.552156],[-8.189207,-3.215495,-1.067632,-8.921655,2.702603,3.753040,-1.266190,4.070327],[-4.462543,-2.935701,-9.081865,-3.161473,-3.457695,-9.054891,-5.390020,1.675281],[-1.377891,7.193951,-5.169947,4.945257,-3.696605,-6.422528,9.053881,-0.915992],[9.994163,0.316119,-1.897287,-9.226352,-8.231463,-6.956840,-2.861870,5.716424],[1.789715,1.203937,-8.371501,6.996481,8.870314,3.434114,8.852084,7.947628],[-9.829974,-9.010700,-0.473950,-5.595170,-2.631914,8.988083,-4.154082,3.823246],[4.884752,5.341817,4.859114,-0.444360,-4.144679,-7.320227,7.231729,-2.269929],[-9.070406,6.858902,8.488648,3.201866,-3.675081,-8.645090,5.291599,-3.581958],[-9.327155,-3.856658,-0.760592,0.617313,4.866400,5.188174,0.508841,-3.164534],[-8.493130,-8.965473,6.357309,7.139327,-8.089363,6.774513,-7.375340,-7.514012],[4.543788,-2.104379,-4.758366,9.715138,7.823095,-2.608975,-5.188212,9.592078]],[[-1.967027,9.736597,1.122997,2.454103,-2.234216,-3.293723,-7.436017,-1.538354],[7.197396,-6.430659,-5.772514,1.038748,-5.242316,-5.817929,1.636274,5.952490],[0.440640,2.928069,-0.263444,-6.513610,5.125751,1.532873,3.203967,-9.581772],[-9.004765,-5.662916,-3.184280,6.914239,-4.592574,1.060960,1.556369,8.550068],[9.546931,0.955488,-5.463744,1.539298,-9.881460,0.449860,-9.534651,3.236093],[-9.822668,3.863010,5.728580,3.202530,-0.338976,1.299300,-1.580117,-9.672733],[-1.725704,6.930697,9.086787,-6.187183,3.124652,3.538536,9.198204,-6.042280],[5.734064,-9.283342,-1.113764,-5.740723,2.975808,-1.816630,-2.175062,1.579406],[6.841489,4.568337,0.555379,-0.295293,-4.523342,-3.556358,-5.642824,9.191772],[-4.848482,8.606270,-9.694363,6.716020,8.840233,1.473874,-4.291305,-3.776337],[0.153005,-8.809310,-7.712188,6.778021,1.386769,-7.367703,-1.247446,0.489783],[-0.922593,-4.309704,-8.701957,-7.291444,4.125757,6.181381,-5.327278,8.297405],[-3.698927,4.011435,9.445369,8.566721,-7.196996,-7.029451,8.605587,-3.259813],[-0.594886,-1.365839,-8.643936,3.643205,-0.224863,-3.045775,-4.680606,-6.999352],[2.357713,7.647848,-6.298522,4.456863,6.446319,-1.372942,7.235807,-3.074880]],[[1.632635,-3.345259,1.365202,9.230010,0.830413,-0.527909,-9.801781,-0.708394],[-1.888528,-2.268413,-2.551189,-7.032704,9.936328,-8.841171,6.660644,2.430799],[-7.855504,-4.172344,0.776332,6.208272,3.790933,-7.788379,3.514847,-9.676234],[4.770867,-5.869553,-0.365286,1.791674,3.784675,0.201820,-3.571909,1.239870],[-1.150967,-3.181347,-6.416985,-7.337683,7.748977,3.823960,9.312308,4.572899],[-7.965465,-2.480612,-9.085536,-9.406278,-7.895127,-0.627924,-4.853928,4.592069],[7.567765,-7.695993,6.784726,-7.380909,-1.641281,5.962052,3.353629,-7.653980],[3.659205,-7.082033,-8.135561,3.770525,-0.633081,0.438841,-5.488184,-6.644190],[-7.307498,0.353234,5.187950,-7.158778,2.405742,-7.752195,-1.554671,-5.260330],[2.828003,3.387888,1.699657,-7.562649,-0.785299,1.166535,-5.847344,5.195617],[-0.063470,8.257880,-0.288707,9.388431,3.084167,-3.367948,-5.622394,6.222653],[4.617362,5.414496,-6.555310,6.384071,5.545912,1.444050,-2.047545,-3.750332],[5.436702,-9.064417,-7.762605,1.725952,5.750252,2.498100,-5.487333,-4.822313],[-1.278436,-6.715320,0.072195,8.790009,-9.690865,9.163771,4.786116,-6.555366],[9.719516,-9.061751,-3.334623,3.312569,8.497848,-1.808102,-1.930525,-9.271584]],[[-4.603707,0.883515,-5.446618,6.497562,2.520101,5.608886,-6.512797,8.834189],[-3.211096,8.114773,6.582688,9.694403,-8.816890,-3.035682,-4.991168,8.080841],[6.439371,-4.890298,8.947677,9.136454,-3.543683,-2.956010,-1.709626,-6.857857],[9.698716,6.978801,5.732773,-9.646976,-0.506423,-6.960617,3.470754,-4.786054],[-6.798849,-8.249100,-5.095709,-4.375937,-2.586170,5.553111,-4.005873,7.849252],[-0.829873,-5.987760,5.364423,4.281507,4.901316,-4.032945,8.432861,0.101441],[-3.238512,5.775828,2.015167,1.929132,-0.925609,-4.054581,7.530501,0.846107],[6.458823,5.827627,-7.271866,-0.511175,-6.007395,-0.307034,8.809535,7.646447],[2.939297,-8.998840,-8.584017,-1.645950,0.654045,2.162061,-6.183730,-0.463424],[-6.193152,3.527362,-5.835736,-5.776122,-6.304954,-6.844991,-8.685846,1.850615],[-4.575776,0.799985,-9.139524,-7.037006,-8.823022,-6.729933,-1.711944,-2.199827],[-4.786315,5.421667,-1.781014,0.826385,-4.830892,-7.465900,7.843167,-2.687973],[-6.919028,-4.130642,1.131145,-3.058026,-2.659995,-4.193006,5.069018,8.790267],[-6.429550,-9.916499,-4.638613,-4.603880,7.212132,8.082527,-4.852666,-6.274314],[1.025344,0.431995,1.047737,4.337919,-3.263702,-5.042676,-4.626499,5.793947]],[[-3.442119,6.086376,5.055625,6.803385,9.147918,2.123527,-1.116335,-4.595965],[-0.973107,-8.930115,9.352254,5.068680,-7.785232,0.776588,8.228590,1.638305],[-7.674015,-6.966199,-5.164841,-3.698118,1.589479,-4.276778,0.410016,6.887038],[-6.172616,-4.981701,0.231915,-0.801455,4.000170,6.133688,-9.255700,7.602414],[8.484521,7.032193,9.672377,5.186597,8.404244,3.349737,-2.721017,2.221646],[-8.576398,-7.623118,3.130620,0.957882,-7.254726,-5.526022,-6.417726,1.150836],[6.796312,2.008691,-1.166804,6.279288,-1.671548,9.808889,-8.554809,-0.285330],[-2.607789,-8.592561,0.642198,-4.637243,-9.702280,-6.059855,-0.785319,0.574824],[-3.634374,4.254616,6.780753,7.970176,5.122657,2.179169,0.349264,-5.577479],[-5.174058,0.700448,6.553428,-8.894798,-2.810495,-9.728262,-3.039425,3.610927],[-9.923141,-6.523554,4.277717,-0.441723,-9.397214,-1.985344,0.013280,5.530721],[-4.493733,9.051208,-1.457853,4.812863,-2.472293,-9.215353,9.828800,-9.105643],[-9.830952,-5.769867,-0.746320,-4.136790,-3.807585,-3.663856,5.126584,4.466969],[-3.134768,2.724215,-7.545079,-3.537556,-1.213690,-2.144046,-9.585042,-2.299129],[7.931996,-2.953896,2.596490,-6.937390,-6.429999,5.086138,-4.368025,7.828979]],[[8.733320,1.370400,7.227938,-7.812798,-5.933680,-0.190524,8.356710,2.452988],[8.795948,-5.314006,-0.549764,-4.361111,2.323083,6.886991,-6.897003,6.696188],[6.302008,-9.961068,-5.617449,8.527779,1.443913,4.422810,-6.517627,4.457347],[-6.835657,-9.750782,-4.335315,8.836032,-0.369380,6.501206,8.613398,-3.924326],[7.792667,-5.460981,1.848501,1.685108,0.157676,-6.658245,1.056741,2.694697],[5.129057,6.989673,-2.707495,-5.588220,0.179374,8.050592,-2.622199,4.215872],[-6.796594,2.304201,0.129857,-2.734914,9.653526,-7.285140,-3.551895,-6.832889],[9.161006,3.431256,8.066845,-0.528344,6.291722,9.874031,8.040396,-7.551516],[-1.964793,-5.422928,-3.181643,-7.671437,5.913207,-5.221075,-3.440401,1.436039],[-9.933795,2.148729,-1.074618,-3.574393,-5.722607,2.790424,6.489542,3.404881],[1.465769,9.992049,9.105585,2.805697,5.658344,-4.283965,7.526746,3.953267],[9.642238,8.705979,8.503534,2.757921,8.826775,9.524601,-4.144628,7.855485],[-2.986219,7.289661,-1.235674,-4.123301,5.029650,-4.164333,3.173895,-4.095836],[-9.670146,-7.955502,-6.072734,7.194208,2.639485,-7.963901,-1.791962,0.929040],[-8.295382,-0.739883,-7.462541,-4.797594,7.849665,-5.533342,2.880341,3.628077]],[[-0.611584,8.105050,-8.410480,-0.373050,8.505143,4.216690,-4.290055,3.456298],[-2.360348,-1.421045,-9.370197,-3.503657,9.678284,-7.409319,0.646925,-3.165401],[-1.449806,-4.210352,2.107910,-5.588056,4.814553,-1.437841,-8.341168,9.955889],[6.959422,6.600751,-8.117773,6.490409,-0.449422,-7.374313,-4.282912,8.858665],[-2.433297,4.788115,0.882844,5.321427,4.016600,-0.700282,0.597995,-5.865383],[3.525214,-2.739122,3.090693,5.885214,-8.786623,-6.185214,0.856990,4.511617],[7.704594,0.233730,-7.725441,-1.404892,-0.752902,2.472808,-6.895148,-3.644328],[-1.609859,0.088815,-4.856168,0.343714,3.655567,7.300407,-5.361472,-6.941983],[0.768571,-7.451300,-5.110251,-7.972007,3.914105,-2.896946,2.872310,-7.973377],[-0.221393,-7.577609,-9.389394,4.492552,1.904866,-3.239320,8.029870,8.090069],[-3.610301,-1.046882,-9.638879,9.135504,-3.792268,4.172729,-5.027346,4.237719],[-7.269105,-0.185505,-1.936652,-0.674778,-9.490257,1.935678,4.945699,5.598900],[-7.344322,4.840216,-2.331990,-8.000219,-2.446800,-2.012461,2.301348,3.880523],[5.736151,4.411955,9.936314,2.728965,-0.964261,0.364162,-0.734939,-2.684603],[-4.434221,9.212491,-5.697007,-7.952452,-6.014598,-1.633350,-9.449834,2.592875]],[[1.771363,5.172118,-3.175939,-6.961107,0.688794,-2.829983,-2.469828,-5.861665],[-0.905642,3.038268,-7.868656,-9.081892,0.002981,-5.137276,-1.186925,0.389717],[-8.186474,1.727558,-4.294057,-0.538258,5.177570,8.129717,6.638940,6.332449],[4.390736,-7.278647,-5.278809,-1.465811,3.013332,1.499487,-8.206750,3.645268],[-8.705530,3.997766,0.544169,-2.878115,0.686308,-1.989188,-5.666521,-9.545398],[8.869380,5.004650,3.208486,5.503366,-9.490434,8.582711,8.786519,-2.282605],[8.135866,-9.804647,3.610149,6.926271,-8.905682,1.198558,1.948231,6.053339],[-8.469011,-1.034971,-5.293090,6.583628,0.114475,-9.910377,6.414293,-1.879128],[-7.200466,9.340960,3.486239,-6.557260,8.293370,-1.523184,-8.446657,6.174820],[-2.920784,-1.158902,4.752030,-0.716624,-8.769374,7.786794,9.497935,-4.879804],[9.976098,6.357405,1.718656,-0.183139,0.341528,7.753971,-4.926154,-9.164261],[0.694000,-8.235623,-0.855358,9.382106,0.298947,7.650363,-3.356503,-8.510791],[6.552980,-1.412133,-4.292138,0.802320,-6.154549,4.999297,3.829294,5.712656],[-5.549609,1.728173,-0.221407,-6.776748,-3.937806,-7.882234,4.594998,-2.356290],[-1.215885,0.040302,4.114823,-8.242227,-4.686649,8.586190,-0.138771,-3.041361]],[[-5.574777,1.015499,-2.793798,-3.528598,1.628526,4.690953,8.627102,-5.515478],[-4.639635,-2.862002,-7.448911,6.744470,-9.500119,3.456556,-4.041981,-4.838961],[4.430238,7.587943,3.747863,-1.337198,8.940776,1.031239,2.638050,-2.482475],[-7.078407,-9.602724,-9.129644,8.640930,-4.916047,2.855393,-8.339693,3.382053],[6.112926,8.618374,-8.434002,-8.706204,0.308801,-7.302912,8.805417,-7.878187],[-0.324443,-3.411636,6.625228,0.208329,-1.515277,-6.504498,-4.023687,7.438414],[-7.045816,-9.581424,-2.059362,-3.963460,2.011685,4.784066,-3.917712,-1.051263],[-9.085449,1.776708,-7.392853,6.080538,3.463435,1.913296,6.089977,2.504013],[5.977738,-9.496766,-8.161913,4.122881,0.969326,-6.561739,-8.780087,-1.983455],[-2.708757,-4.578050,4.892235,2.664409,2.164680,-3.301008,8.061999,3.642703],[-0.801230,2.531709,-2.967705,-0.370027,8.700783,0.538974,1.898388,-5.550853],[9.657797,-5.659018,-7.323515,0.564041,-6.810180,-3.341525,-6.525638,-0.444859],[0.941568,6.761243,-2.707973,3.769081,1.538526,8.736718,7.051140,-8.295123],[3.835009,7.608246,-6.055114,5.259833,-5.618446,8.385964,0.047380,6.557106],[8.213937,6.330954,-2.448481,6.470382,8.090666,-5.710558,-7.172837,-0.970962]],[[8.755626,8.958478,-9.717349,-1.458630,-8.754488,0.356246,5.105783,-5.039204],[-9.608392,-6.793345,-8.669728,-6.770347,8.449388,-9.122723,6.695944,4.213866],[-3.281443,-2.344595,7.108116,-7.610437,-2.341131,-0.332686,-9.326101,-1.517711],[-7.513343,-8.085925,-2.386978,-8.183093,4.702947,8.207253,2.694397,-5.117070],[6.575163,8.678791,7.504223,-4.475299,2.978706,-9.235007,1.356107,-7.476603],[6.128719,0.434307,9.153296,4.938952,-7.386795,1.107712,1.027322,-8.886998],[2.509875,-3.785451,6.812888,-0.580181,9.235797,-5.439002,-4.242019,-2.956033],[0.961029,5.723094,7.636909,-7.683984,-8.902567,-1.015899,8.261140,-4.937966],[-0.190387,4.834057,-5.014013,-1.082313,-4.471088,-8.187343,-8.056129,9.728526],[-8.181678,-0.336522,9.245765,-3.797772,1.912745,-9.726798,3.151545,1.425980],[5.050574,8.643616,-1.536970,1.847861,-6.180387,2.956573,-9.269750,0.129084],[-7.066267,-4.967184,-0.928398,7.922520,7.795275,-3.921221,-7.453090,-8.684752],[-5.127582,7.679597,-2.873246,-1.252304,3.435903,1.403224,-4.779934,-3.615572],[-9.085343,-6.297968,6.101661,-0.176582,8.406992,4.616545,-0.027438,1.535494],[1.544534,-5.228035,1.043133,7.086320,-6.379319,-0.231362,4.575215,3.668981]],[[-9.222324,-2.450147,6.405376,-9.025696,3.492606,3.104123,-2.543077,-1.449668],[9.637939,7.800078,0.672358,9.069776,4.035917,-1.896233,1.853682,-3.119091],[-9.416893,9.335987,-7.577383,-6.539871,-5.983179,9.728888,2.916007,-2.131815],[-2.377525,6.243117,-0.298504,-9.739682,1.506427,-8.545373,-6.482803,-4.923941],[1.044515,9.415880,2.845771,7.034102,9.350436,-2.495482,7.721523,4.809624],[-2.916898,1.071383,-5.848312,-6.928188,9.941128,-0.106521,-2.707078,-5.558531],[-5.919437,5.861797,8.239131,0.184498,9.676812,8.977405,5.680349,1.319964],[-6.618418,-4.681294,-2.528092,-7.315855,-0.660010,5.469572,9.674689,-0.781980],[6.892992,7.465248,4.615743,6.827907,4.798279,4.240586,-1.997464,-5.285413],[4.927327,5.368156,-3.710332,5.478353,-7.020745,0.496829,-9.707495,1.862631],[1.332502,8.005095,-8.925617,1.941845,5.646805,-9.759434,4.194600,-7.429081],[5.764058,-8.004815,1.158497,-5.543896,6.354547,4.809709,-6.082744,7.595386],[-5.613427,-2.070150,-6.211527,-7.685301,-1.533380,9.298164,0.147703,-6.110032],[2.300057,-9.142506,7.054811,-1.254928,-0.583471,-9.265924,-2.287729,-6.096398],[-7.276146,1.993274,2.820346,0.942390,-8.144015,8.049106,-0.628461,1.070688]],[[2.827734,5.173479,-0.399937,6.027429,3.833785,7.304118,3.281380,-8.324120],[-6.125571,-7.736887,7.461611,4.183617,-4.754187,-6.438974,2.927246,-0.367967],[3.033229,2.370773,8.567977,7.608244,-1.741601,7.668729,-0.641508,-0.115829],[4.259155,-8.002084,-5.930472,2.639912,2.441634,7.306194,4.706606,0.048429],[4.948351,-2.646450,9.930622,-5.858076,5.506161,4.886574,7.945252,-7.819500],[3.515748,-2.706826,5.313202,-4.779336,8.309264,4.936923,-2.313688,8.913448],[3.429570,-9.018708,2.489457,-4.283826,-9.863339,6.702110,5.412132,9.672961],[-1.343849,-6.521427,1.016158,-1.751446,1.453219,5.182094,-1.915166,5.672606],[-6.322518,-5.588813,-6.371036,-6.948598,9.424519,8.986069,-9.918944,5.452238],[-0.024481,-1.437615,-0.578281,-1.645160,-1.430158,8.409246,-5.876898,-6.549870],[2.514041,6.704403,6.691006,-9.723043,0.524461,-9.495503,-4.978162,-7.500440],[8.461701,-1.953632,-9.423866,4.481564,-1.822724,2.799642,-3.970056,-7.938372],[4.372685,6.410478,7.499106,0.993670,9.012331,-5.527223,0.470778,-0.867114],[8.756664,-8.550447,9.722926,-6.521299,8.669382,4.756948,4.159419,0.120065],[1.116135,-9.356097,-5.761325,0.690393,2.871019,-8.440987,-0.292724,2.752537]]], dtype = "float64")#candidate|1907|(13, 15, 8)|const|float64
uop_1908 = relay.sqrt(const_1907.astype('float64')) # shape=(13, 15, 8)
output = relay.Tuple([uop_1908,])
output2 = relay.Tuple([uop_1908,])
func_1924 = relay.Function([], output)
mod['func_1924'] = func_1924
mod = relay.transform.InferType()(mod)
output = func_1924()
func_1925 = relay.Function([], output)
mutated_mod['func_1925'] = func_1925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1924_call = mod.get_global_var('func_1924')
func_1925_call = mutated_mod.get_global_var('func_1925')
call_1949 = relay.TupleGetItem(func_1924_call(), 0)
call_1950 = relay.TupleGetItem(func_1925_call(), 0)
var_1958 = relay.var("var_1958", dtype = "float64", shape = (13, 15, 8))#candidate|1958|(13, 15, 8)|var|float64
bop_1959 = relay.left_shift(call_1949.astype('int8'), relay.reshape(var_1958.astype('int8'), relay.shape_of(call_1949))) # shape=(13, 15, 8)
bop_1962 = relay.left_shift(call_1950.astype('int8'), relay.reshape(var_1958.astype('int8'), relay.shape_of(call_1950))) # shape=(13, 15, 8)
output = bop_1959
output2 = bop_1962
func_1970 = relay.Function([var_1958,], output)
mod['func_1970'] = func_1970
mod = relay.transform.InferType()(mod)
mutated_mod['func_1970'] = func_1970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1971 = relay.var("var_1971", dtype = "float64", shape = (13, 15, 8))#candidate|1971|(13, 15, 8)|var|float64
func_1970_call = mutated_mod.get_global_var('func_1970')
call_1972 = func_1970_call(var_1971)
output = call_1972
func_1973 = relay.Function([var_1971], output)
mutated_mod['func_1973'] = func_1973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1139_call = mod.get_global_var('func_1139')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1979 = relay.TupleGetItem(func_1139_call(), 0)
call_1980 = relay.TupleGetItem(func_1141_call(), 0)
output = relay.Tuple([call_1979,])
output2 = relay.Tuple([call_1980,])
func_1986 = relay.Function([], output)
mod['func_1986'] = func_1986
mod = relay.transform.InferType()(mod)
mutated_mod['func_1986'] = func_1986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1986_call = mutated_mod.get_global_var('func_1986')
call_1987 = func_1986_call()
output = call_1987
func_1988 = relay.Function([], output)
mutated_mod['func_1988'] = func_1988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mod.get_global_var('func_1330')
func_1331_call = mutated_mod.get_global_var('func_1331')
call_2011 = relay.TupleGetItem(func_1330_call(), 1)
call_2012 = relay.TupleGetItem(func_1331_call(), 1)
output = relay.Tuple([call_2011,])
output2 = relay.Tuple([call_2012,])
func_2019 = relay.Function([], output)
mod['func_2019'] = func_2019
mod = relay.transform.InferType()(mod)
mutated_mod['func_2019'] = func_2019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2020 = func_2019_call()
output = call_2020
func_2021 = relay.Function([], output)
mutated_mod['func_2021'] = func_2021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_237_call = mod.get_global_var('func_237')
func_239_call = mutated_mod.get_global_var('func_239')
call_2022 = relay.TupleGetItem(func_237_call(), 1)
call_2023 = relay.TupleGetItem(func_239_call(), 1)
output = relay.Tuple([call_2022,])
output2 = relay.Tuple([call_2023,])
func_2042 = relay.Function([], output)
mod['func_2042'] = func_2042
mod = relay.transform.InferType()(mod)
mutated_mod['func_2042'] = func_2042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mutated_mod.get_global_var('func_2042')
call_2043 = func_2042_call()
output = call_2043
func_2044 = relay.Function([], output)
mutated_mod['func_2044'] = func_2044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_2048 = func_995_call()
call_2049 = func_995_call()
func_1654_call = mod.get_global_var('func_1654')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_2051 = func_1654_call()
call_2052 = func_1654_call()
var_2056 = relay.var("var_2056", dtype = "bool", shape = (6, 2, 15))#candidate|2056|(6, 2, 15)|var|bool
bop_2057 = relay.power(call_2051.astype('float32'), var_2056.astype('float32')) # shape=(6, 2, 15)
bop_2060 = relay.power(call_2052.astype('float32'), var_2056.astype('float32')) # shape=(6, 2, 15)
output = relay.Tuple([call_2048,bop_2057,])
output2 = relay.Tuple([call_2049,bop_2060,])
func_2066 = relay.Function([var_2056,], output)
mod['func_2066'] = func_2066
mod = relay.transform.InferType()(mod)
var_2067 = relay.var("var_2067", dtype = "bool", shape = (6, 2, 15))#candidate|2067|(6, 2, 15)|var|bool
output = func_2066(var_2067)
func_2068 = relay.Function([var_2067], output)
mutated_mod['func_2068'] = func_2068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1924_call = mod.get_global_var('func_1924')
func_1925_call = mutated_mod.get_global_var('func_1925')
call_2114 = relay.TupleGetItem(func_1924_call(), 0)
call_2115 = relay.TupleGetItem(func_1925_call(), 0)
output = call_2114
output2 = call_2115
func_2121 = relay.Function([], output)
mod['func_2121'] = func_2121
mod = relay.transform.InferType()(mod)
output = func_2121()
func_2122 = relay.Function([], output)
mutated_mod['func_2122'] = func_2122
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2143 = relay.var("var_2143", dtype = "float32", shape = (4, 2, 15))#candidate|2143|(4, 2, 15)|var|float32
uop_2144 = relay.atanh(var_2143.astype('float32')) # shape=(4, 2, 15)
output = relay.Tuple([uop_2144,])
output2 = relay.Tuple([uop_2144,])
func_2161 = relay.Function([var_2143,], output)
mod['func_2161'] = func_2161
mod = relay.transform.InferType()(mod)
mutated_mod['func_2161'] = func_2161
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2162 = relay.var("var_2162", dtype = "float32", shape = (4, 2, 15))#candidate|2162|(4, 2, 15)|var|float32
func_2161_call = mutated_mod.get_global_var('func_2161')
call_2163 = func_2161_call(var_2162)
output = call_2163
func_2164 = relay.Function([var_2162], output)
mutated_mod['func_2164'] = func_2164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2166 = relay.var("var_2166", dtype = "uint32", shape = (14, 3, 1))#candidate|2166|(14, 3, 1)|var|uint32
var_2167 = relay.var("var_2167", dtype = "uint32", shape = (14, 3, 5))#candidate|2167|(14, 3, 5)|var|uint32
bop_2168 = relay.greater_equal(var_2166.astype('bool'), var_2167.astype('bool')) # shape=(14, 3, 5)
func_623_call = mod.get_global_var('func_623')
func_626_call = mutated_mod.get_global_var('func_626')
const_2173 = relay.const([[-2,7,2,-2,-10,-5],[-1,7,7,-2,-5,-2],[-6,2,6,-2,10,10]], dtype = "uint8")#candidate|2173|(3, 6)|const|uint8
const_2174 = relay.const([4,-4,-6,-3,-6,9,1,-2,-8,3,4,-9,-6,8,-3,-9,-8,-8,-7,-7,1,8,9,-7,8,-6,-1,-9,-6,-4,-5,7,-5,10,-6,-2,3,9,10,9,-7,-2,-4,5,7,-10,-4,10,2,9,6,-2,-3,-1,8,3,-6,4,-6,-1,-10,-9,-8,2,-8,-5,-4,1,10,10,-3,3,-8,9,-6,8,1,-10,4,-6,-5,-7,10,6,-2,-9,-9,-4,9,-2,-6,-1,-8,8,5,6,-7,-8,-1,-10,-1,9,1,-9,-1,-3,1,-5], dtype = "uint8")#candidate|2174|(108,)|const|uint8
call_2172 = func_623_call(relay.reshape(const_2173.astype('uint8'), [6, 3, 1]), relay.reshape(const_2174.astype('uint8'), [6, 3, 6]), )
call_2175 = func_623_call(relay.reshape(const_2173.astype('uint8'), [6, 3, 1]), relay.reshape(const_2174.astype('uint8'), [6, 3, 6]), )
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2182 = relay.TupleGetItem(func_2042_call(), 0)
call_2183 = relay.TupleGetItem(func_2044_call(), 0)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_2186 = func_995_call()
call_2187 = func_995_call()
bop_2189 = relay.greater(call_2186.astype('bool'), const_2174.astype('bool')) # shape=(6, 2, 108)
bop_2192 = relay.greater(call_2187.astype('bool'), const_2174.astype('bool')) # shape=(6, 2, 108)
const_2193 = relay.const([[[6,8,7,7,1],[9,5,-3,-3,-2],[5,10,4,-8,-6]],[[10,-3,7,6,-1],[7,9,7,-3,-3],[3,8,9,-1,-6]],[[-8,-8,-5,-8,-10],[-9,10,10,-2,-8],[-9,-2,-4,-8,-8]],[[9,-1,4,1,-8],[-4,9,7,-9,-4],[5,-8,2,-9,-5]],[[7,10,1,5,-9],[-7,9,7,5,6],[-3,-7,-9,-2,-1]],[[5,3,7,1,-9],[4,5,2,-9,8],[-8,-8,1,-6,-4]],[[-4,-5,6,2,-4],[10,-7,-1,-7,-5],[8,3,8,1,-10]],[[1,6,10,7,-9],[-3,9,4,-6,-2],[3,6,-6,-3,-10]],[[-4,7,-6,1,-9],[4,-9,-1,-5,-3],[9,7,-5,10,9]],[[-3,1,-2,8,-10],[-2,-8,-1,6,-7],[-3,7,2,2,-10]],[[-3,4,2,1,-9],[-7,-9,-4,6,-6],[-8,-9,-8,7,-2]],[[3,-7,-9,4,8],[-5,4,10,4,-7],[8,9,2,-6,-9]],[[3,4,-10,-10,-7],[8,3,-3,2,-8],[-10,-8,-2,8,7]],[[-8,9,2,-7,6],[1,5,7,-5,-7],[-10,9,-6,8,1]]], dtype = "uint32")#candidate|2193|(14, 3, 5)|const|uint32
bop_2194 = relay.minimum(var_2167.astype('uint32'), relay.reshape(const_2193.astype('uint32'), relay.shape_of(var_2167))) # shape=(14, 3, 5)
output = relay.Tuple([bop_2168,call_2172,const_2173,call_2182,bop_2189,bop_2194,])
output2 = relay.Tuple([bop_2168,call_2175,const_2173,call_2183,bop_2192,bop_2194,])
func_2203 = relay.Function([var_2166,var_2167,], output)
mod['func_2203'] = func_2203
mod = relay.transform.InferType()(mod)
var_2204 = relay.var("var_2204", dtype = "uint32", shape = (14, 3, 1))#candidate|2204|(14, 3, 1)|var|uint32
var_2205 = relay.var("var_2205", dtype = "uint32", shape = (14, 3, 5))#candidate|2205|(14, 3, 5)|var|uint32
output = func_2203(var_2204,var_2205,)
func_2206 = relay.Function([var_2204,var_2205,], output)
mutated_mod['func_2206'] = func_2206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1139_call = mod.get_global_var('func_1139')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_2208 = relay.TupleGetItem(func_1139_call(), 0)
call_2209 = relay.TupleGetItem(func_1141_call(), 0)
func_964_call = mod.get_global_var('func_964')
func_965_call = mutated_mod.get_global_var('func_965')
call_2214 = func_964_call()
call_2215 = func_964_call()
output = relay.Tuple([call_2208,call_2214,])
output2 = relay.Tuple([call_2209,call_2215,])
func_2223 = relay.Function([], output)
mod['func_2223'] = func_2223
mod = relay.transform.InferType()(mod)
mutated_mod['func_2223'] = func_2223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2223_call = mutated_mod.get_global_var('func_2223')
call_2224 = func_2223_call()
output = call_2224
func_2225 = relay.Function([], output)
mutated_mod['func_2225'] = func_2225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_341_call = mod.get_global_var('func_341')
func_342_call = mutated_mod.get_global_var('func_342')
call_2282 = relay.TupleGetItem(func_341_call(), 2)
call_2283 = relay.TupleGetItem(func_342_call(), 2)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_2287 = func_995_call()
call_2288 = func_995_call()
func_1924_call = mod.get_global_var('func_1924')
func_1925_call = mutated_mod.get_global_var('func_1925')
call_2294 = relay.TupleGetItem(func_1924_call(), 0)
call_2295 = relay.TupleGetItem(func_1925_call(), 0)
func_1751_call = mod.get_global_var('func_1751')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_2307 = relay.TupleGetItem(func_1751_call(), 0)
call_2308 = relay.TupleGetItem(func_1753_call(), 0)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
const_2310 = relay.const([-6.564330,1.539398,1.730717,-2.030808,-1.016756,-4.704656,-2.556465,0.708851,2.928835,7.716848,-7.306116,-7.408930,7.897858,-1.041292,-4.724916,-4.009780,8.300688,-4.184227,4.146640,-6.357373,1.321644,5.505285,-2.671943,9.929773,1.600231,-1.432443,-2.522656,5.908394,5.772167,-9.404426,0.589906,-5.384032,0.024550,1.019413,8.945140,-2.684655,2.987297,6.757593,7.863271,8.446753,5.329951,-9.849491,-3.612810,5.224040,1.264487,9.684577,-4.130070,5.018980], dtype = "float64")#candidate|2310|(48,)|const|float64
call_2309 = relay.TupleGetItem(func_1883_call(relay.reshape(const_2310.astype('float64'), [6, 2, 4])), 2)
call_2311 = relay.TupleGetItem(func_1885_call(relay.reshape(const_2310.astype('float64'), [6, 2, 4])), 2)
func_535_call = mod.get_global_var('func_535')
func_538_call = mutated_mod.get_global_var('func_538')
const_2320 = relay.const(-5.270177, dtype = "float64")#candidate|2320|()|const|float64
var_2321 = relay.var("var_2321", dtype = "float64", shape = (90,))#candidate|2321|(90,)|var|float64
call_2319 = func_535_call(relay.reshape(const_2320.astype('float64'), []), relay.reshape(var_2321.astype('float64'), [3, 2, 15]), )
call_2322 = func_535_call(relay.reshape(const_2320.astype('float64'), []), relay.reshape(var_2321.astype('float64'), [3, 2, 15]), )
output = relay.Tuple([call_2282,call_2287,call_2294,call_2307,call_2309,const_2310,call_2319,const_2320,var_2321,])
output2 = relay.Tuple([call_2283,call_2288,call_2295,call_2308,call_2311,const_2310,call_2322,const_2320,var_2321,])
func_2326 = relay.Function([var_2321,], output)
mod['func_2326'] = func_2326
mod = relay.transform.InferType()(mod)
var_2327 = relay.var("var_2327", dtype = "float64", shape = (90,))#candidate|2327|(90,)|var|float64
output = func_2326(var_2327)
func_2328 = relay.Function([var_2327], output)
mutated_mod['func_2328'] = func_2328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mod.get_global_var('func_566')
func_568_call = mutated_mod.get_global_var('func_568')
call_2333 = func_566_call()
call_2334 = func_566_call()
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2344 = relay.TupleGetItem(func_2042_call(), 0)
call_2345 = relay.TupleGetItem(func_2044_call(), 0)
bop_2353 = relay.bitwise_or(call_2344.astype('int16'), relay.reshape(call_2333.astype('int16'), relay.shape_of(call_2344))) # shape=(6, 2, 1)
bop_2356 = relay.bitwise_or(call_2345.astype('int16'), relay.reshape(call_2334.astype('int16'), relay.shape_of(call_2345))) # shape=(6, 2, 1)
output = bop_2353
output2 = bop_2356
func_2361 = relay.Function([], output)
mod['func_2361'] = func_2361
mod = relay.transform.InferType()(mod)
mutated_mod['func_2361'] = func_2361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2361_call = mutated_mod.get_global_var('func_2361')
call_2362 = func_2361_call()
output = call_2362
func_2363 = relay.Function([], output)
mutated_mod['func_2363'] = func_2363
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2390 = relay.const([[[-3,-7,7,-2],[-9,-7,-3,-4],[-7,-8,-10,4],[5,-6,10,-2],[-6,-9,-4,-8],[-3,5,-9,1],[-6,6,9,1],[-1,-5,-6,8],[-6,6,8,-3],[2,-9,7,-6],[8,-6,-2,-2],[-5,-6,6,4],[8,1,6,7],[10,-7,-5,-7],[-7,-9,-1,1],[-10,6,10,-7]],[[9,-4,-10,3],[8,-6,-4,-3],[7,9,-5,-3],[-5,10,-8,-4],[4,2,-1,-3],[-4,10,-1,1],[7,5,8,6],[6,1,-4,1],[-4,-2,-7,-2],[4,-10,-6,-1],[1,-6,4,4],[-9,-4,-1,1],[-9,8,7,-6],[5,4,-9,6],[-2,10,-4,6],[1,-4,-8,-8]],[[7,-10,10,-3],[-5,8,-3,5],[7,-1,-2,-2],[-10,7,-3,-2],[5,-5,1,-1],[7,10,4,-5],[-3,-9,3,9],[-10,-1,5,5],[7,-4,10,-5],[-3,-8,2,-7],[10,-9,-9,-8],[7,4,-3,10],[1,-10,-9,9],[-10,8,-2,7],[1,9,-4,-9],[-4,-1,-1,9]],[[-6,2,-4,7],[10,7,2,-6],[-10,3,1,5],[6,-6,-10,9],[-4,1,-4,5],[6,7,-8,1],[9,-3,5,-8],[7,-7,9,-5],[9,-2,-4,8],[-8,8,-2,-5],[-10,-3,-8,7],[7,4,-2,-10],[5,-5,-8,9],[-1,-4,-5,-4],[-9,3,10,-5],[-5,-2,6,-9]],[[1,-9,8,6],[6,-2,1,7],[3,-7,9,-9],[-1,-1,-10,-7],[6,-3,-6,6],[1,3,4,-3],[-10,-1,2,-1],[-10,9,3,-2],[-4,5,-5,1],[9,-9,-6,1],[3,-2,9,-10],[-8,-10,5,-1],[-8,-8,-7,9],[5,-8,-10,-4],[8,-10,1,-7],[-8,-1,-8,3]],[[-9,9,10,-10],[5,3,-7,-2],[4,4,-3,6],[8,6,8,-4],[-10,2,10,-4],[-10,-4,-5,1],[-8,7,-8,3],[-10,3,-8,-4],[-1,-8,-8,8],[3,-6,8,-10],[-4,10,-1,7],[-3,9,9,-10],[2,1,-4,2],[1,-6,7,5],[-4,-3,-9,-4],[3,4,1,-2]],[[3,4,2,-5],[-4,-10,-6,2],[10,-2,-10,-1],[-4,-6,-8,7],[-2,1,9,-7],[-4,3,1,-9],[-5,-2,-9,-7],[-6,7,3,-7],[7,9,3,-8],[-2,-8,-10,-6],[8,-9,8,10],[-1,10,-1,9],[7,3,-3,-9],[-3,7,-4,6],[8,-8,3,2],[3,8,-1,1]],[[4,-9,4,-1],[5,-8,-1,-2],[2,-7,8,-1],[-3,6,-7,-5],[-10,9,2,-10],[-9,7,-3,-1],[9,-1,9,-9],[-2,-8,9,-1],[8,2,1,-9],[10,-4,-5,9],[-5,10,-4,-6],[-1,5,-10,2],[6,7,7,10],[2,-2,9,2],[4,7,10,-4],[8,4,6,5]],[[9,9,-10,3],[5,10,9,-7],[3,-10,-7,-7],[-4,4,-8,-1],[-3,-4,1,4],[5,9,7,6],[2,-6,-2,4],[3,-7,-7,9],[-9,10,8,-8],[-1,6,5,-7],[-8,3,-5,8],[-5,10,-3,9],[-9,4,6,-2],[-10,-2,-10,1],[-3,10,1,7],[-2,9,5,7]],[[-8,5,4,-8],[6,7,-10,-6],[5,2,-5,-4],[-5,10,1,-6],[-10,-3,-8,9],[3,-2,6,-8],[5,7,-9,4],[-3,8,4,3],[4,-10,-6,-8],[5,-4,7,2],[-3,1,9,8],[2,6,-9,-1],[4,9,10,-9],[-7,-8,6,-8],[10,-3,-5,-2],[8,-2,-6,3]],[[-4,-2,-10,-1],[-5,-3,10,1],[1,8,-6,10],[10,-2,2,-8],[8,3,10,-6],[3,-7,-1,3],[-2,-5,-3,4],[-4,2,2,4],[-10,9,-1,5],[4,-4,-10,-4],[-10,-1,-1,-6],[1,-5,-8,6],[-6,-7,10,10],[4,7,-3,-6],[-10,-5,4,-8],[-9,-2,1,-2]],[[3,-3,-1,-8],[-9,1,-8,4],[-6,6,10,6],[6,6,-8,-4],[10,-5,-2,-10],[-8,2,9,-3],[-5,-6,-3,-6],[-2,6,-3,-10],[-8,5,-8,1],[-3,-3,7,7],[4,-8,-8,8],[7,10,4,2],[-7,-10,-10,-2],[-3,7,-2,3],[10,5,-6,-9],[-6,-2,1,10]],[[10,2,2,5],[10,5,-8,7],[10,7,-4,-8],[5,9,-5,-3],[-1,-5,10,8],[1,3,-4,7],[-2,-9,-9,7],[10,-10,-8,-7],[8,4,1,-10],[-5,-2,-3,2],[-3,2,-1,-8],[8,5,-10,5],[-4,6,10,6],[8,6,-8,7],[-3,-3,-9,-7],[-10,-2,-3,-8]],[[3,2,1,1],[-7,9,7,-7],[4,-5,3,-1],[-4,-3,8,-6],[7,-8,-8,-8],[-6,-10,-2,3],[7,10,-2,4],[1,-3,-9,4],[6,6,1,-9],[-2,9,-6,-1],[-2,4,1,-10],[-5,5,-1,-2],[1,1,6,8],[-6,2,-1,4],[6,-7,-8,-3],[-9,9,-9,7]],[[10,3,-7,-4],[10,-5,-10,6],[9,-5,10,9],[8,9,8,-9],[-5,6,5,-5],[5,8,10,-3],[7,7,-8,9],[4,-5,-6,-3],[-1,3,9,3],[-7,-9,-4,6],[-2,9,1,8],[-5,-8,-1,2],[-1,8,-2,-4],[-1,-5,-7,4],[-6,-1,-2,2],[4,-10,2,7]],[[-6,3,-5,4],[10,-8,-2,8],[7,5,-6,9],[-7,-7,1,-2],[8,-5,-2,8],[10,-1,-2,10],[-6,-1,10,-6],[-8,-5,6,6],[-5,-8,1,1],[4,4,10,-5],[9,-3,-7,5],[10,4,9,10],[10,3,4,3],[-5,-5,-8,-3],[8,5,3,-1],[-2,-10,5,-9]]], dtype = "int16")#candidate|2390|(16, 16, 4)|const|int16
var_2391 = relay.var("var_2391", dtype = "int16", shape = (16, 16, 4))#candidate|2391|(16, 16, 4)|var|int16
bop_2392 = relay.right_shift(const_2390.astype('int16'), relay.reshape(var_2391.astype('int16'), relay.shape_of(const_2390))) # shape=(16, 16, 4)
uop_2395 = relay.atan(var_2391.astype('float64')) # shape=(16, 16, 4)
output = relay.Tuple([bop_2392,uop_2395,])
output2 = relay.Tuple([bop_2392,uop_2395,])
func_2397 = relay.Function([var_2391,], output)
mod['func_2397'] = func_2397
mod = relay.transform.InferType()(mod)
mutated_mod['func_2397'] = func_2397
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2398 = relay.var("var_2398", dtype = "int16", shape = (16, 16, 4))#candidate|2398|(16, 16, 4)|var|int16
func_2397_call = mutated_mod.get_global_var('func_2397')
call_2399 = func_2397_call(var_2398)
output = call_2399
func_2400 = relay.Function([var_2398], output)
mutated_mod['func_2400'] = func_2400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_2417 = func_995_call()
call_2418 = func_995_call()
output = relay.Tuple([call_2417,])
output2 = relay.Tuple([call_2418,])
func_2426 = relay.Function([], output)
mod['func_2426'] = func_2426
mod = relay.transform.InferType()(mod)
mutated_mod['func_2426'] = func_2426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2426_call = mutated_mod.get_global_var('func_2426')
call_2427 = func_2426_call()
output = call_2427
func_2428 = relay.Function([], output)
mutated_mod['func_2428'] = func_2428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
call_2438 = func_1527_call()
call_2439 = func_1527_call()
const_2444 = relay.const([[[-7.403677,6.899068,9.532972],[-6.582288,-6.787131,5.886498]],[[5.212301,-0.652060,-1.749398],[2.105605,-4.034040,-1.326047]],[[-9.871273,-7.697117,-0.484893],[-3.371302,9.536539,-8.739172]],[[-1.172196,9.477032,8.716898],[3.014725,-0.731794,4.480087]],[[3.196139,6.635626,-0.740185],[-5.067699,-5.019081,-7.492829]],[[-3.368893,8.357142,9.834849],[-6.973068,-6.309936,-8.249603]]], dtype = "float32")#candidate|2444|(6, 2, 3)|const|float32
bop_2445 = relay.less(call_2438.astype('bool'), const_2444.astype('bool')) # shape=(6, 2, 3)
bop_2448 = relay.less(call_2439.astype('bool'), const_2444.astype('bool')) # shape=(6, 2, 3)
bop_2457 = relay.subtract(const_2444.astype('int32'), call_2438.astype('int32')) # shape=(6, 2, 3)
bop_2460 = relay.subtract(const_2444.astype('int32'), call_2439.astype('int32')) # shape=(6, 2, 3)
bop_2466 = relay.greater_equal(call_2438.astype('bool'), bop_2445.astype('bool')) # shape=(6, 2, 3)
bop_2469 = relay.greater_equal(call_2439.astype('bool'), bop_2448.astype('bool')) # shape=(6, 2, 3)
bop_2470 = relay.bitwise_xor(bop_2466.astype('int64'), relay.reshape(bop_2445.astype('int64'), relay.shape_of(bop_2466))) # shape=(6, 2, 3)
bop_2473 = relay.bitwise_xor(bop_2469.astype('int64'), relay.reshape(bop_2448.astype('int64'), relay.shape_of(bop_2469))) # shape=(6, 2, 3)
output = relay.Tuple([bop_2457,bop_2470,])
output2 = relay.Tuple([bop_2460,bop_2473,])
func_2479 = relay.Function([], output)
mod['func_2479'] = func_2479
mod = relay.transform.InferType()(mod)
output = func_2479()
func_2480 = relay.Function([], output)
mutated_mod['func_2480'] = func_2480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2019_call = mod.get_global_var('func_2019')
func_2021_call = mutated_mod.get_global_var('func_2021')
call_2484 = relay.TupleGetItem(func_2019_call(), 0)
call_2485 = relay.TupleGetItem(func_2021_call(), 0)
var_2486 = relay.var("var_2486", dtype = "bool", shape = (6, 2, 12))#candidate|2486|(6, 2, 12)|var|bool
bop_2487 = relay.minimum(call_2484.astype('int64'), var_2486.astype('int64')) # shape=(6, 2, 12)
bop_2490 = relay.minimum(call_2485.astype('int64'), var_2486.astype('int64')) # shape=(6, 2, 12)
output = relay.Tuple([bop_2487,])
output2 = relay.Tuple([bop_2490,])
func_2491 = relay.Function([var_2486,], output)
mod['func_2491'] = func_2491
mod = relay.transform.InferType()(mod)
var_2492 = relay.var("var_2492", dtype = "bool", shape = (6, 2, 12))#candidate|2492|(6, 2, 12)|var|bool
output = func_2491(var_2492)
func_2493 = relay.Function([var_2492], output)
mutated_mod['func_2493'] = func_2493
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2508 = relay.var("var_2508", dtype = "float64", shape = (3, 15, 6))#candidate|2508|(3, 15, 6)|var|float64
uop_2509 = relay.log2(var_2508.astype('float64')) # shape=(3, 15, 6)
uop_2511 = relay.atan(uop_2509.astype('float32')) # shape=(3, 15, 6)
output = uop_2511
output2 = uop_2511
func_2515 = relay.Function([var_2508,], output)
mod['func_2515'] = func_2515
mod = relay.transform.InferType()(mod)
mutated_mod['func_2515'] = func_2515
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2516 = relay.var("var_2516", dtype = "float64", shape = (3, 15, 6))#candidate|2516|(3, 15, 6)|var|float64
func_2515_call = mutated_mod.get_global_var('func_2515')
call_2517 = func_2515_call(var_2516)
output = call_2517
func_2518 = relay.Function([var_2516], output)
mutated_mod['func_2518'] = func_2518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_2520 = func_995_call()
call_2521 = func_995_call()
func_2203_call = mod.get_global_var('func_2203')
func_2206_call = mutated_mod.get_global_var('func_2206')
var_2531 = relay.var("var_2531", dtype = "uint32", shape = (14, 3))#candidate|2531|(14, 3)|var|uint32
const_2532 = relay.const([[-10],[3],[-4],[3],[8],[-6],[7],[-9],[-5],[2],[8],[2],[7],[2],[5],[1],[3],[-7],[5],[-6],[7],[3],[6],[-7],[-9],[-8],[8],[-6],[10],[-7],[1],[10],[-3],[8],[-10],[-1],[8],[9],[6],[-6],[6],[9],[-4],[2],[-4],[-8],[-8],[9],[-9],[9],[3],[4],[-2],[7],[10],[2],[-7],[-3],[9],[-4],[-4],[-7],[3],[2],[-3],[1],[1],[-9],[-8],[-2],[10],[-6],[8],[-10],[5],[-9],[8],[-1],[-2],[-5],[6],[-10],[9],[9],[-6],[8],[6],[4],[3],[10],[-10],[7],[2],[1],[3],[-8],[-9],[-3],[10],[8],[4],[3],[-1],[-3],[-5],[-4],[-9],[-4],[-1],[5],[-2],[10],[-5],[-2],[6],[2],[-7],[9],[6],[-4],[-2],[-5],[-1],[1],[8],[5],[-3],[9],[-7],[-3],[-2],[-4],[-2],[7],[-2],[8],[-9],[-4],[5],[-2],[3],[1],[2],[4],[-3],[-4],[-3],[-4],[-1],[2],[1],[-5],[4],[3],[-5],[10],[-2],[-4],[1],[6],[6],[-8],[10],[4],[4],[5],[8],[8],[-1],[1],[5],[4],[2],[-4],[7],[-8],[-1],[1],[-10],[-3],[3],[-10],[7],[-2],[6],[-4],[5],[-8],[7],[10],[1],[-8],[6],[-4],[-8],[-1],[-4],[-3],[8],[9],[9],[6],[-1],[-2],[6],[4],[-2],[10],[6],[6]], dtype = "uint32")#candidate|2532|(210, 1)|const|uint32
call_2530 = relay.TupleGetItem(func_2203_call(relay.reshape(var_2531.astype('uint32'), [14, 3, 1]), relay.reshape(const_2532.astype('uint32'), [14, 3, 5]), ), 2)
call_2533 = relay.TupleGetItem(func_2206_call(relay.reshape(var_2531.astype('uint32'), [14, 3, 1]), relay.reshape(const_2532.astype('uint32'), [14, 3, 5]), ), 2)
output = relay.Tuple([call_2520,call_2530,var_2531,const_2532,])
output2 = relay.Tuple([call_2521,call_2533,var_2531,const_2532,])
func_2534 = relay.Function([var_2531,], output)
mod['func_2534'] = func_2534
mod = relay.transform.InferType()(mod)
var_2535 = relay.var("var_2535", dtype = "uint32", shape = (14, 3))#candidate|2535|(14, 3)|var|uint32
output = func_2534(var_2535)
func_2536 = relay.Function([var_2535], output)
mutated_mod['func_2536'] = func_2536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_2564 = func_465_call()
call_2565 = func_465_call()
output = call_2564
output2 = call_2565
func_2576 = relay.Function([], output)
mod['func_2576'] = func_2576
mod = relay.transform.InferType()(mod)
output = func_2576()
func_2577 = relay.Function([], output)
mutated_mod['func_2577'] = func_2577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2121_call = mod.get_global_var('func_2121')
func_2122_call = mutated_mod.get_global_var('func_2122')
call_2585 = func_2121_call()
call_2586 = func_2121_call()
func_1751_call = mod.get_global_var('func_1751')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_2587 = relay.TupleGetItem(func_1751_call(), 1)
call_2588 = relay.TupleGetItem(func_1753_call(), 1)
uop_2590 = relay.cos(call_2585.astype('float32')) # shape=(13, 15, 8)
uop_2592 = relay.cos(call_2586.astype('float32')) # shape=(13, 15, 8)
output = relay.Tuple([call_2587,uop_2590,])
output2 = relay.Tuple([call_2588,uop_2592,])
func_2596 = relay.Function([], output)
mod['func_2596'] = func_2596
mod = relay.transform.InferType()(mod)
mutated_mod['func_2596'] = func_2596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2596_call = mutated_mod.get_global_var('func_2596')
call_2597 = func_2596_call()
output = call_2597
func_2598 = relay.Function([], output)
mutated_mod['func_2598'] = func_2598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_2609 = relay.TupleGetItem(func_1186_call(), 3)
call_2610 = relay.TupleGetItem(func_1187_call(), 3)
var_2613 = relay.var("var_2613", dtype = "uint32", shape = (2, 52))#candidate|2613|(2, 52)|var|uint32
bop_2614 = relay.greater(call_2609.astype('bool'), relay.reshape(var_2613.astype('bool'), relay.shape_of(call_2609))) # shape=(2, 52)
bop_2617 = relay.greater(call_2610.astype('bool'), relay.reshape(var_2613.astype('bool'), relay.shape_of(call_2610))) # shape=(2, 52)
output = bop_2614
output2 = bop_2617
func_2625 = relay.Function([var_2613,], output)
mod['func_2625'] = func_2625
mod = relay.transform.InferType()(mod)
mutated_mod['func_2625'] = func_2625
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2626 = relay.var("var_2626", dtype = "uint32", shape = (2, 52))#candidate|2626|(2, 52)|var|uint32
func_2625_call = mutated_mod.get_global_var('func_2625')
call_2627 = func_2625_call(var_2626)
output = call_2627
func_2628 = relay.Function([var_2626], output)
mutated_mod['func_2628'] = func_2628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1582_call = mod.get_global_var('func_1582')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_2654 = relay.TupleGetItem(func_1582_call(), 0)
call_2655 = relay.TupleGetItem(func_1583_call(), 0)
func_2491_call = mod.get_global_var('func_2491')
func_2493_call = mutated_mod.get_global_var('func_2493')
var_2657 = relay.var("var_2657", dtype = "bool", shape = (144,))#candidate|2657|(144,)|var|bool
call_2656 = relay.TupleGetItem(func_2491_call(relay.reshape(var_2657.astype('bool'), [6, 2, 12])), 0)
call_2658 = relay.TupleGetItem(func_2493_call(relay.reshape(var_2657.astype('bool'), [6, 2, 12])), 0)
func_2361_call = mod.get_global_var('func_2361')
func_2363_call = mutated_mod.get_global_var('func_2363')
call_2665 = func_2361_call()
call_2666 = func_2361_call()
func_1345_call = mod.get_global_var('func_1345')
func_1347_call = mutated_mod.get_global_var('func_1347')
const_2683 = relay.const([3.608047,-2.643480,-0.966959,2.242859,-1.666177,4.826859,-1.775165,-2.311367,-0.093533,4.633339,-0.684003,6.689868,4.411147,-4.565549,6.970234,4.876273,7.900051,7.704131,-2.522114,-4.231017,-1.078244,-5.039371,-4.941741,-6.327219,-9.114259,2.843742,-2.416393,-2.815513,7.883000,-5.535231,-4.955305,7.550682,9.904463,-6.880464,2.219642,-5.963269,-9.976858,1.575196,9.318490,7.386745,1.723184,-2.399099,6.171382,2.398067,7.680038,-7.898672,5.497497,-8.707467,-2.628492,3.062381,3.785555,5.445761,-7.934268,-9.313912,-3.399034,7.196685,5.816775,-7.426054,-7.372930,6.557694,0.562740,-4.352091,9.760066,-4.443675,3.479371,-1.188663,2.572665,-3.147584,-9.400734,-7.215595,-0.046315,-2.041843,3.661423,-5.637020,5.849737,-4.586802,4.657232,5.297502,8.829133,-2.451030,8.058639,7.048336,4.047608,-6.365177,-7.623704,-2.796579,-5.762385,-9.486457,6.465033,-7.500596,-3.055269,-0.313582,3.455804,5.969910,1.242435,8.030917,-2.163562,1.104482,-8.382061,7.355744,-1.622479,1.050053,-9.081913,8.320081,-6.218260,-6.312817,-8.884327,9.959770,3.425358,-6.109283,-3.560620,3.367695,-8.622786,-6.086982,7.586189,4.192528,-6.742845,-9.675230,6.484731,-6.065540,6.752819,-8.194090,4.070719,9.607190,-2.180502,6.878965,3.867175,3.556707,-5.135785,-5.143701,6.610469,1.606939,-0.782965,4.810104,8.173908,-9.304803,-5.992513,-7.587129,-4.947992,-2.223160,5.255975,6.338568,1.004418,-2.115584,0.164003,7.728969,0.546374,-8.488388,-5.836662,2.519233,4.328526,7.466684,-6.729175,-7.647391,7.516429,-7.315168,-6.792207,-0.246593,-2.303227,1.018577,7.230064,3.223629,-1.930804,2.053796,8.456837,-3.210004,-0.174834,-5.327397,-4.685827,1.033488,-0.710938,-0.034079,0.906521,-2.976431,-4.781781,1.142065,-6.706182,-1.755091,-6.313688,3.339108,-5.676954,9.234281,0.739142,8.329652,-5.745103,-0.764271,-1.667174,9.990819,7.294405,-4.853129,-7.801039,1.427775,-1.420322,8.944104,8.106352,-8.646650,-7.608095,-7.461086,5.449405,5.289464,-6.730855,-2.965515,5.712299,0.523714,8.146036,-4.777385,5.805914,-5.798734,4.827491,1.146635,5.744594,-9.017530,3.706800,4.744782,-8.122967,-5.140013,-6.897411,-8.148305,-1.590717,-4.443299,2.011380,7.038078,2.083964,-5.991259,3.135085,1.141670,0.223405,1.540173,4.629761,0.581970,3.130121,-3.679110,3.646332,5.812451,-7.241072,5.533140,-9.346974,3.924939,4.381264,-1.371120,3.276772,2.751118,8.412403,4.655928,3.038977,2.396100,-7.441660,0.897609,-1.833746,9.216163,-9.701330,-9.781609,-6.962032,-4.684347,5.394327,-9.976581,3.231361,3.492819,-1.439735,1.380582,2.140585,1.498988,-9.654765,7.535553,9.299997,-7.292464,-1.850309,2.137231,-2.052913,-5.532873,-9.317809,-6.075341,-9.955342,3.051531,-4.392615,-8.496364,6.929680,7.182770,-4.359908,-5.909179,0.795715,-0.554591,8.448562,-6.850357,8.120774,7.147033,-0.962964,4.700961,5.573628,7.714616,7.542653,0.099425,1.366313,7.956259,-5.422716,-9.356322,-1.556075,6.189325,-6.029565,4.853214,-2.599871,1.901096,-8.076982,3.331762,7.606628,9.573985,-9.357224,4.511035,9.039848,-5.931381,-8.449228,6.362466,2.391861,-0.496966,2.504607,6.909348,-1.565323,-8.408508,-8.337215,-5.802520,-6.117363,-4.667279,8.627494,9.608156,-0.384821,-8.309639,-5.326802,6.482049,-7.141283,9.033595,9.022555,1.561127,4.804582,-9.729402,7.102084,-1.654974,-8.777104,-4.796261,-8.987696,-9.465658,6.242908,-1.116537,7.655195,1.990601,6.554836,8.657985,-8.690316,8.418194,-1.114824,2.831085,-1.788154,3.779577,-9.705861,-7.196723,6.422695,-0.747310,1.645852,-5.957168,-5.594213,-8.484455,-7.909034,4.759912,-4.216635,7.389041,-3.071525,-3.655109,-3.877691,-6.382040,-2.110931,2.689280,1.157428,-8.836670,-7.163016,1.991877,4.274140,8.596414,7.455183,-5.303866,1.634015,-8.881442,-3.948909,-6.059361,1.307089,2.944409,-0.897139,0.821598,-7.381715,-3.260088,6.767856,-8.927526,-3.442490,-7.455459,-2.777945,7.343015,-1.684961,6.313418,6.720823,8.685982,-6.063541,-8.281798,-0.015876,9.587822,3.325372,1.575742,5.969004,0.062778,2.152202,-5.321603,-3.790190,3.256571,7.775422,1.294005,0.702008,6.437537,-4.528715,-6.478241,-0.463894,8.537472,8.835646,-1.465643,-2.168521,-7.251884,5.065875,2.683067,2.937129,6.016507,-7.313075,8.680675,0.060168,1.494996,-9.343307,-4.158992,2.067906,-7.311251,4.511470,-3.063304,8.794753,0.616405,5.427448,-5.532134,-9.725177,1.697747,2.527080,-0.035304,-9.185390,-5.035043,0.862397,2.888493,-2.500027,5.989329,-3.912552,-6.431062,0.822541,-9.480052,-3.664110,9.459319,-2.035318,9.995983,8.192786,3.903891,-6.134482,-1.468022,-9.124815,-4.489797,6.597548,-8.759175,8.531863,8.201395,1.937774,2.443810,1.446550,-8.932821,-6.777583,7.426419,0.113309,0.011194,-2.752490,7.187915,5.069675,8.941056,8.032972,-1.686887,-5.224987,4.183018,3.721365,-7.376414,6.175518,7.669911,-9.241269,1.534073,8.787667,6.576883,-3.196230,-0.062157,1.772105,0.328131,-4.764317,0.583133,1.319362,-4.002993,-6.083621,0.818394,2.295926,7.767701,5.272013,2.931901,3.617318,-6.668635,5.766135,8.872110,7.422776,0.223891,-5.832063,-2.135815,-6.120914,-5.054634,4.726731,-7.636343,-3.700380,0.481623,8.756209,-8.808453,7.395214,-1.264288,-1.843455,6.831464,-0.329047,8.809470], dtype = "float32")#candidate|2683|(528,)|const|float32
call_2682 = relay.TupleGetItem(func_1345_call(relay.reshape(const_2683.astype('float32'), [11, 4, 12])), 0)
call_2684 = relay.TupleGetItem(func_1347_call(relay.reshape(const_2683.astype('float32'), [11, 4, 12])), 0)
func_1139_call = mod.get_global_var('func_1139')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_2687 = relay.TupleGetItem(func_1139_call(), 0)
call_2688 = relay.TupleGetItem(func_1141_call(), 0)
bop_2713 = relay.logical_and(call_2665.astype('bool'), var_2657.astype('bool')) # shape=(6, 2, 144)
bop_2716 = relay.logical_and(call_2666.astype('bool'), var_2657.astype('bool')) # shape=(6, 2, 144)
output = relay.Tuple([call_2654,call_2656,call_2682,const_2683,call_2687,bop_2713,])
output2 = relay.Tuple([call_2655,call_2658,call_2684,const_2683,call_2688,bop_2716,])
func_2726 = relay.Function([var_2657,], output)
mod['func_2726'] = func_2726
mod = relay.transform.InferType()(mod)
mutated_mod['func_2726'] = func_2726
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2727 = relay.var("var_2727", dtype = "bool", shape = (144,))#candidate|2727|(144,)|var|bool
func_2726_call = mutated_mod.get_global_var('func_2726')
call_2728 = func_2726_call(var_2727)
output = call_2728
func_2729 = relay.Function([var_2727], output)
mutated_mod['func_2729'] = func_2729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1700_call = mod.get_global_var('func_1700')
func_1701_call = mutated_mod.get_global_var('func_1701')
call_2745 = relay.TupleGetItem(func_1700_call(), 0)
call_2746 = relay.TupleGetItem(func_1701_call(), 0)
output = call_2745
output2 = call_2746
func_2751 = relay.Function([], output)
mod['func_2751'] = func_2751
mod = relay.transform.InferType()(mod)
output = func_2751()
func_2752 = relay.Function([], output)
mutated_mod['func_2752'] = func_2752
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2769 = relay.var("var_2769", dtype = "uint16", shape = (8, 5, 11))#candidate|2769|(8, 5, 11)|var|uint16
var_2770 = relay.var("var_2770", dtype = "uint16", shape = (8, 5, 11))#candidate|2770|(8, 5, 11)|var|uint16
bop_2771 = relay.multiply(var_2769.astype('uint16'), relay.reshape(var_2770.astype('uint16'), relay.shape_of(var_2769))) # shape=(8, 5, 11)
output = relay.Tuple([bop_2771,])
output2 = relay.Tuple([bop_2771,])
func_2778 = relay.Function([var_2769,var_2770,], output)
mod['func_2778'] = func_2778
mod = relay.transform.InferType()(mod)
var_2779 = relay.var("var_2779", dtype = "uint16", shape = (8, 5, 11))#candidate|2779|(8, 5, 11)|var|uint16
var_2780 = relay.var("var_2780", dtype = "uint16", shape = (8, 5, 11))#candidate|2780|(8, 5, 11)|var|uint16
output = func_2778(var_2779,var_2780,)
func_2781 = relay.Function([var_2779,var_2780,], output)
mutated_mod['func_2781'] = func_2781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mod.get_global_var('func_2751')
func_2752_call = mutated_mod.get_global_var('func_2752')
call_2823 = func_2751_call()
call_2824 = func_2751_call()
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_2834 = func_465_call()
call_2835 = func_465_call()
var_2837 = relay.var("var_2837", dtype = "float32", shape = (6, 2, 16))#candidate|2837|(6, 2, 16)|var|float32
bop_2838 = relay.less(call_2823.astype('bool'), var_2837.astype('bool')) # shape=(6, 2, 16)
bop_2841 = relay.less(call_2824.astype('bool'), var_2837.astype('bool')) # shape=(6, 2, 16)
uop_2846 = relay.cos(call_2823.astype('float64')) # shape=(6, 2, 1)
uop_2848 = relay.cos(call_2824.astype('float64')) # shape=(6, 2, 1)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
var_2851 = relay.var("var_2851", dtype = "float64", shape = (48,))#candidate|2851|(48,)|var|float64
call_2850 = relay.TupleGetItem(func_1883_call(relay.reshape(var_2851.astype('float64'), [6, 2, 4])), 0)
call_2852 = relay.TupleGetItem(func_1885_call(relay.reshape(var_2851.astype('float64'), [6, 2, 4])), 0)
func_2361_call = mod.get_global_var('func_2361')
func_2363_call = mutated_mod.get_global_var('func_2363')
call_2871 = func_2361_call()
call_2872 = func_2361_call()
func_2596_call = mod.get_global_var('func_2596')
func_2598_call = mutated_mod.get_global_var('func_2598')
call_2886 = relay.TupleGetItem(func_2596_call(), 1)
call_2887 = relay.TupleGetItem(func_2598_call(), 1)
func_535_call = mod.get_global_var('func_535')
func_538_call = mutated_mod.get_global_var('func_538')
var_2892 = relay.var("var_2892", dtype = "float64", shape = ())#candidate|2892|()|var|float64
const_2893 = relay.const([-6.610028,-8.032824,2.183797,-3.013501,-6.853594,-8.110981,1.479358,-7.214576,5.313992,-6.012759,3.718740,-7.158135,8.352661,5.252390,4.830255,9.981840,8.503448,-2.124505,-0.794730,-8.076702,1.519493,3.235853,2.645294,-4.558256,1.632408,-6.939482,-6.757451,-8.682633,9.103637,-7.385388,2.939672,0.186574,4.778425,-8.423889,-9.279075,-1.015158,8.132302,-5.453781,9.310438,5.615925,2.750040,2.250085,-0.781860,0.580900,4.431641,-0.872904,7.903295,2.856641,-5.327082,3.357932,9.743499,-1.034499,5.742603,0.670944,-4.359582,7.075003,-3.740833,8.760048,-0.806673,-5.993864,-0.545381,5.990589,-5.867047,-9.048162,-9.793957,5.521827,0.930853,-6.823754,-1.674762,-4.519513,-5.178322,-7.560827,-5.730872,0.270072,-7.462998,5.534480,5.451917,4.718593,9.822839,-3.646552,4.555413,4.847942,9.875190,4.095290,2.866714,-2.737220,5.311831,-7.446614,-5.829640,-3.589844], dtype = "float64")#candidate|2893|(90,)|const|float64
call_2891 = func_535_call(relay.reshape(var_2892.astype('float64'), []), relay.reshape(const_2893.astype('float64'), [3, 2, 15]), )
call_2894 = func_535_call(relay.reshape(var_2892.astype('float64'), []), relay.reshape(const_2893.astype('float64'), [3, 2, 15]), )
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_2896 = relay.TupleGetItem(func_448_call(), 1)
call_2897 = relay.TupleGetItem(func_450_call(), 1)
output = relay.Tuple([call_2834,bop_2838,uop_2846,call_2850,var_2851,call_2871,call_2886,call_2891,var_2892,const_2893,call_2896,])
output2 = relay.Tuple([call_2835,bop_2841,uop_2848,call_2852,var_2851,call_2872,call_2887,call_2894,var_2892,const_2893,call_2897,])
func_2907 = relay.Function([var_2837,var_2851,var_2892,], output)
mod['func_2907'] = func_2907
mod = relay.transform.InferType()(mod)
mutated_mod['func_2907'] = func_2907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2907_call = mutated_mod.get_global_var('func_2907')
var_2909 = relay.var("var_2909", dtype = "float32", shape = (6, 2, 16))#candidate|2909|(6, 2, 16)|var|float32
var_2910 = relay.var("var_2910", dtype = "float64", shape = (48,))#candidate|2910|(48,)|var|float64
var_2911 = relay.var("var_2911", dtype = "float64", shape = ())#candidate|2911|()|var|float64
call_2908 = func_2907_call(var_2909,var_2910,var_2911,)
output = call_2908
func_2912 = relay.Function([var_2909,var_2910,var_2911,], output)
mutated_mod['func_2912'] = func_2912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mod.get_global_var('func_1330')
func_1331_call = mutated_mod.get_global_var('func_1331')
call_2939 = relay.TupleGetItem(func_1330_call(), 0)
call_2940 = relay.TupleGetItem(func_1331_call(), 0)
uop_2941 = relay.sinh(call_2939.astype('float64')) # shape=(6, 2, 1)
uop_2943 = relay.sinh(call_2940.astype('float64')) # shape=(6, 2, 1)
bop_2959 = relay.logical_and(call_2939.astype('bool'), relay.reshape(uop_2941.astype('bool'), relay.shape_of(call_2939))) # shape=(6, 2, 1)
bop_2962 = relay.logical_and(call_2940.astype('bool'), relay.reshape(uop_2943.astype('bool'), relay.shape_of(call_2940))) # shape=(6, 2, 1)
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_2982 = relay.TupleGetItem(func_1186_call(), 0)
call_2983 = relay.TupleGetItem(func_1187_call(), 0)
output = relay.Tuple([bop_2959,call_2982,])
output2 = relay.Tuple([bop_2962,call_2983,])
func_2985 = relay.Function([], output)
mod['func_2985'] = func_2985
mod = relay.transform.InferType()(mod)
output = func_2985()
func_2986 = relay.Function([], output)
mutated_mod['func_2986'] = func_2986
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3006 = relay.var("var_3006", dtype = "float32", shape = (1, 14, 7))#candidate|3006|(1, 14, 7)|var|float32
uop_3007 = relay.exp(var_3006.astype('float32')) # shape=(1, 14, 7)
func_2361_call = mod.get_global_var('func_2361')
func_2363_call = mutated_mod.get_global_var('func_2363')
call_3015 = func_2361_call()
call_3016 = func_2361_call()
func_2479_call = mod.get_global_var('func_2479')
func_2480_call = mutated_mod.get_global_var('func_2480')
call_3019 = relay.TupleGetItem(func_2479_call(), 0)
call_3020 = relay.TupleGetItem(func_2480_call(), 0)
func_2397_call = mod.get_global_var('func_2397')
func_2400_call = mutated_mod.get_global_var('func_2400')
var_3022 = relay.var("var_3022", dtype = "int16", shape = (1024,))#candidate|3022|(1024,)|var|int16
call_3021 = relay.TupleGetItem(func_2397_call(relay.reshape(var_3022.astype('int16'), [16, 16, 4])), 0)
call_3023 = relay.TupleGetItem(func_2400_call(relay.reshape(var_3022.astype('int16'), [16, 16, 4])), 0)
bop_3024 = relay.multiply(uop_3007.astype('uint8'), relay.reshape(var_3006.astype('uint8'), relay.shape_of(uop_3007))) # shape=(1, 14, 7)
bop_3028 = relay.divide(var_3022.astype('float64'), call_3015.astype('float64')) # shape=(6, 2, 1024)
bop_3031 = relay.divide(var_3022.astype('float64'), call_3016.astype('float64')) # shape=(6, 2, 1024)
func_691_call = mod.get_global_var('func_691')
func_693_call = mutated_mod.get_global_var('func_693')
call_3038 = relay.TupleGetItem(func_691_call(), 0)
call_3039 = relay.TupleGetItem(func_693_call(), 0)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
var_3043 = relay.var("var_3043", dtype = "float64", shape = (90,))#candidate|3043|(90,)|var|float64
call_3042 = relay.TupleGetItem(func_2326_call(relay.reshape(var_3043.astype('float64'), [90,])), 8)
call_3044 = relay.TupleGetItem(func_2328_call(relay.reshape(var_3043.astype('float64'), [90,])), 8)
uop_3048 = relay.sigmoid(uop_3007.astype('float32')) # shape=(1, 14, 7)
output = relay.Tuple([call_3019,call_3021,bop_3024,bop_3028,call_3038,call_3042,var_3043,uop_3048,])
output2 = relay.Tuple([call_3020,call_3023,bop_3024,bop_3031,call_3039,call_3044,var_3043,uop_3048,])
func_3058 = relay.Function([var_3006,var_3022,var_3043,], output)
mod['func_3058'] = func_3058
mod = relay.transform.InferType()(mod)
var_3059 = relay.var("var_3059", dtype = "float32", shape = (1, 14, 7))#candidate|3059|(1, 14, 7)|var|float32
var_3060 = relay.var("var_3060", dtype = "int16", shape = (1024,))#candidate|3060|(1024,)|var|int16
var_3061 = relay.var("var_3061", dtype = "float64", shape = (90,))#candidate|3061|(90,)|var|float64
output = func_3058(var_3059,var_3060,var_3061,)
func_3062 = relay.Function([var_3059,var_3060,var_3061,], output)
mutated_mod['func_3062'] = func_3062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_3083 = func_995_call()
call_3084 = func_995_call()
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_3099 = relay.TupleGetItem(func_448_call(), 0)
call_3100 = relay.TupleGetItem(func_450_call(), 0)
output = relay.Tuple([call_3083,call_3099,])
output2 = relay.Tuple([call_3084,call_3100,])
func_3108 = relay.Function([], output)
mod['func_3108'] = func_3108
mod = relay.transform.InferType()(mod)
output = func_3108()
func_3109 = relay.Function([], output)
mutated_mod['func_3109'] = func_3109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3124 = relay.var("var_3124", dtype = "float32", shape = (6, 9, 15))#candidate|3124|(6, 9, 15)|var|float32
uop_3125 = relay.rsqrt(var_3124.astype('float32')) # shape=(6, 9, 15)
uop_3135 = relay.atan(uop_3125.astype('float64')) # shape=(6, 9, 15)
output = uop_3135
output2 = uop_3135
func_3139 = relay.Function([var_3124,], output)
mod['func_3139'] = func_3139
mod = relay.transform.InferType()(mod)
mutated_mod['func_3139'] = func_3139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3140 = relay.var("var_3140", dtype = "float32", shape = (6, 9, 15))#candidate|3140|(6, 9, 15)|var|float32
func_3139_call = mutated_mod.get_global_var('func_3139')
call_3141 = func_3139_call(var_3140)
output = call_3141
func_3142 = relay.Function([var_3140], output)
mutated_mod['func_3142'] = func_3142
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3177 = relay.var("var_3177", dtype = "uint8", shape = (12, 15, 9))#candidate|3177|(12, 15, 9)|var|uint8
const_3178 = relay.const([[[-10,1,3,7,9,8,-4,2,2],[-6,-6,-10,3,1,-3,-3,-7,4],[-10,-8,6,8,4,5,6,8,6],[-6,5,5,8,-10,2,3,-4,10],[-10,2,-2,9,10,10,5,-7,3],[-2,-1,6,-6,-5,1,-10,6,6],[-1,-6,4,7,1,-2,5,7,-8],[-9,-3,5,-2,6,1,7,-9,-2],[-8,2,2,-8,-10,3,8,-2,-8],[7,-6,-9,-5,8,1,4,-9,-1],[-2,10,-3,-2,6,-2,-3,-6,1],[5,-4,-9,2,-4,-2,4,3,-10],[8,7,-5,8,-1,-6,-4,8,3],[2,-1,-10,3,-8,9,-5,7,-1],[-5,10,-5,-6,-9,-6,-2,-2,7]],[[7,-4,-8,-3,10,-7,4,-9,-5],[5,3,8,8,10,-4,-10,10,-7],[8,1,4,6,9,-6,-10,-6,3],[-4,5,-1,-4,-1,4,3,2,8],[4,-3,1,-7,-10,-6,8,-6,-8],[1,5,-6,-10,10,5,-7,4,-5],[-1,6,5,4,3,-6,6,-1,-7],[-1,8,-10,-9,-5,9,8,10,1],[7,3,-5,1,4,4,10,2,-7],[2,-1,1,-5,-10,-4,-4,-8,2],[-4,7,-6,-3,6,-4,-10,-1,3],[1,-2,5,-3,6,6,5,1,-9],[-4,-3,8,5,4,-8,-7,-7,3],[-4,10,10,-10,-5,-8,7,-9,-4],[10,6,5,-2,-5,1,8,-8,9]],[[-6,4,9,-8,-6,9,-5,-9,-4],[6,-7,3,-1,-5,-1,7,-3,-9],[-3,-1,5,8,10,2,10,-9,1],[6,5,2,-6,-3,10,-3,2,-3],[-7,-8,8,2,10,-6,-3,4,6],[2,-5,-2,9,-9,1,-10,4,-7],[10,2,-9,2,1,-10,1,8,8],[-2,-5,-10,4,-7,7,-3,-1,8],[1,4,7,-10,7,-4,-8,-6,9],[1,5,4,-10,-3,-9,-5,-3,6],[-4,-8,-4,7,-9,7,8,-3,-6],[7,3,-8,-2,-5,-3,-5,-5,7],[-3,1,7,2,-6,8,-2,-9,-6],[-7,2,-3,5,2,-9,9,-5,-6],[10,8,2,7,3,-1,3,-7,-2]],[[-9,-6,-6,2,-7,-10,1,-10,6],[-5,8,-9,8,6,6,-4,4,-6],[5,8,4,4,7,-4,-5,-4,-8],[-1,4,10,5,2,5,10,5,3],[-7,5,-10,5,-10,8,3,-4,7],[6,9,-9,-8,-6,10,-4,-6,-1],[10,2,6,-9,9,7,-7,-8,-4],[3,-8,5,-8,-5,10,1,-1,-1],[4,9,3,-9,-10,9,6,6,-10],[-3,1,-5,3,4,-8,4,-7,5],[-6,10,-3,-10,2,-2,8,-3,5],[-10,5,-4,-9,4,1,5,6,-5],[-8,-8,2,3,7,-7,-7,3,-2],[-2,7,-8,7,-6,-3,-2,6,1],[3,-8,-3,5,3,-9,-4,10,9]],[[10,3,9,-6,9,4,-10,6,-7],[2,-7,9,3,-9,7,-1,3,2],[2,-4,10,10,5,9,-3,4,-7],[7,8,-3,3,-1,-7,-8,-1,-9],[10,-2,-3,5,-1,7,-3,1,2],[8,5,-10,4,-3,-10,-7,-10,-3],[9,1,10,1,-4,-7,-6,2,6],[-6,-1,5,-9,-2,-3,-4,-7,-4],[6,-10,-8,9,-4,5,-4,-10,10],[-6,10,-2,7,5,2,8,-7,-10],[-7,-8,9,-1,-4,8,6,7,-4],[-9,4,4,3,5,2,4,-4,2],[-6,6,4,8,-10,6,-3,-6,8],[4,-1,1,6,-7,-10,6,2,9],[-6,5,-1,1,-3,10,4,-5,3]],[[-2,-3,-9,-8,10,7,-7,6,2],[-3,9,7,-9,3,9,10,-7,10],[8,3,9,5,6,10,-9,10,-10],[9,-9,3,-10,-9,8,5,7,-1],[-1,-4,10,-4,8,-8,10,-8,-10],[6,6,9,5,9,5,10,-8,10],[10,-6,-7,-7,-10,5,-9,-1,6],[-8,-7,3,-7,-7,-7,3,-2,-6],[-1,-5,9,2,9,-3,-7,-6,-10],[-8,9,-3,4,-4,5,5,-10,-9],[-10,-6,-6,4,2,2,8,-8,-7],[3,-7,10,-6,7,7,6,-7,-8],[3,-10,3,-6,2,-10,-7,2,10],[5,1,4,8,-7,2,9,7,-10],[-1,-3,-2,-4,6,2,-10,-1,-9]],[[-10,5,-3,3,4,-3,-2,3,-7],[-6,2,7,-7,-3,9,-5,10,-8],[-1,-6,1,-1,4,-8,-7,-2,-8],[4,-9,6,-10,8,-3,4,-7,10],[2,3,-3,6,9,10,-10,-3,-1],[8,-1,1,3,9,8,8,-1,5],[-5,-4,3,-2,-8,4,5,1,8],[-10,-9,-1,-8,-6,-3,3,-6,-2],[10,-3,-8,-8,-9,-7,-10,8,-7],[6,-1,4,-5,-1,5,9,-5,6],[7,4,-2,3,-9,-3,3,2,2],[-7,5,8,-1,-5,-7,-10,4,10],[-5,2,-5,10,4,1,8,-5,-6],[-2,7,-3,-10,-1,-7,2,6,-7],[1,-1,9,-3,10,9,8,-2,1]],[[-3,8,-5,5,-8,3,1,3,9],[4,1,7,-9,-3,3,-8,-5,10],[-3,9,-5,-9,6,-8,5,6,-5],[6,-1,-9,-3,1,-5,-7,-6,-4],[-9,-7,4,-2,7,-5,-5,8,-7],[10,-6,-7,-4,3,-1,8,9,-8],[1,4,-10,-2,-9,8,-9,-8,-1],[-6,-9,4,-6,-1,8,-8,9,-6],[-2,-1,1,6,2,-5,-9,8,1],[-10,-4,2,10,10,-5,-6,7,5],[-1,-7,7,5,-2,5,-3,-2,6],[9,-5,5,7,4,-1,1,-4,-4],[-10,-8,-2,-8,10,3,4,-1,-3],[9,-10,-6,-4,4,5,8,8,2],[8,6,9,-5,-1,4,-5,-4,5]],[[-7,-6,6,2,9,-9,10,10,-7],[-5,-4,1,8,8,-2,-1,2,1],[-9,2,-2,10,10,8,-10,10,-9],[1,-6,9,-4,6,-8,-5,-9,-8],[8,3,-7,-5,-5,-3,7,-2,-3],[-10,3,-4,-2,-9,-6,2,-4,-3],[-7,10,-5,-4,6,-5,7,7,-1],[3,8,6,9,-9,2,-6,10,1],[-10,8,-1,7,8,7,3,-5,-2],[-6,-1,-5,-6,-4,-10,4,7,6],[-4,-5,-6,-4,-2,9,-1,6,9],[7,-6,-2,3,6,7,-8,-6,-5],[-5,1,-7,-3,7,-2,-5,-2,7],[7,3,2,7,2,4,8,-4,9],[1,-10,5,5,-1,1,4,-10,1]],[[-6,3,-4,3,6,-10,1,-1,10],[-2,-4,-3,-3,-2,3,-4,-4,8],[1,9,-1,4,-10,2,9,-6,-9],[9,-9,4,4,2,-2,-5,2,-10],[-3,-4,1,7,-1,4,-4,-1,-4],[7,-10,6,-9,-5,-5,3,-3,-4],[-2,4,-4,3,-1,-2,-9,5,-8],[-1,1,10,-3,5,2,10,-10,7],[-3,1,5,1,2,3,-6,-9,-10],[-5,3,-1,-1,9,3,5,-8,-2],[-10,7,8,4,-2,-2,-1,7,9],[9,9,3,-5,8,5,-6,-2,8],[3,-3,-6,-9,-2,-3,6,-4,1],[7,-4,-1,6,3,-2,-9,3,-2],[-6,6,-1,2,-2,-2,-2,10,5]],[[-4,-1,-2,-7,10,2,-1,-4,8],[-7,-3,-5,-9,-4,-4,2,-4,6],[-8,7,-7,9,-5,4,-8,-4,-7],[6,7,-8,-2,2,3,-2,-2,-8],[-5,-4,2,6,8,-3,-10,-4,-8],[9,-3,6,8,7,-6,-9,-6,3],[-3,-9,10,10,8,6,-6,-6,7],[-5,9,-5,8,7,-8,-1,-1,4],[2,-1,7,8,4,4,-7,6,-2],[-2,6,-6,10,-5,-8,2,2,2],[-1,-3,-2,8,-6,7,7,8,-9],[-10,-2,9,4,1,5,5,2,2],[-5,-7,-7,10,-2,-9,-3,-9,4],[8,-9,3,-2,1,8,-2,-8,-5],[3,-8,4,-5,8,3,-4,-9,-1]],[[9,3,-9,-7,-6,-2,-7,6,10],[-7,-8,-9,-7,3,-7,10,-8,-8],[-6,10,10,-2,-6,6,-8,-1,8],[-9,-4,-2,-5,-9,-7,-1,-3,-4],[-2,-10,5,-4,-9,-9,-4,3,-1],[1,9,-8,-6,-9,2,2,10,-4],[-9,5,-3,6,-5,7,6,-1,-9],[-9,-9,-4,4,5,-9,6,-7,-8],[7,10,-7,-5,7,5,-4,1,-5],[-4,-4,-2,8,-10,8,5,-6,-7],[-4,-3,10,-6,-4,-10,5,-9,-3],[-1,8,-5,-1,-2,-5,-9,5,9],[2,2,6,9,7,10,9,-2,5],[3,-8,-5,8,-2,-6,8,8,-5],[1,-6,10,-8,-9,7,-8,10,-7]]], dtype = "uint8")#candidate|3178|(12, 15, 9)|const|uint8
bop_3179 = relay.right_shift(var_3177.astype('uint8'), relay.reshape(const_3178.astype('uint8'), relay.shape_of(var_3177))) # shape=(12, 15, 9)
output = bop_3179
output2 = bop_3179
func_3184 = relay.Function([var_3177,], output)
mod['func_3184'] = func_3184
mod = relay.transform.InferType()(mod)
mutated_mod['func_3184'] = func_3184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3185 = relay.var("var_3185", dtype = "uint8", shape = (12, 15, 9))#candidate|3185|(12, 15, 9)|var|uint8
func_3184_call = mutated_mod.get_global_var('func_3184')
call_3186 = func_3184_call(var_3185)
output = call_3186
func_3187 = relay.Function([var_3185], output)
mutated_mod['func_3187'] = func_3187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_3203 = func_465_call()
call_3204 = func_465_call()
output = call_3203
output2 = call_3204
func_3206 = relay.Function([], output)
mod['func_3206'] = func_3206
mod = relay.transform.InferType()(mod)
mutated_mod['func_3206'] = func_3206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3206_call = mutated_mod.get_global_var('func_3206')
call_3207 = func_3206_call()
output = call_3207
func_3208 = relay.Function([], output)
mutated_mod['func_3208'] = func_3208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1275_call = mod.get_global_var('func_1275')
func_1276_call = mutated_mod.get_global_var('func_1276')
call_3209 = relay.TupleGetItem(func_1275_call(), 1)
call_3210 = relay.TupleGetItem(func_1276_call(), 1)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_3214 = func_1084_call()
call_3215 = func_1084_call()
func_1654_call = mod.get_global_var('func_1654')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_3233 = func_1654_call()
call_3234 = func_1654_call()
output = relay.Tuple([call_3209,call_3214,call_3233,])
output2 = relay.Tuple([call_3210,call_3215,call_3234,])
func_3248 = relay.Function([], output)
mod['func_3248'] = func_3248
mod = relay.transform.InferType()(mod)
mutated_mod['func_3248'] = func_3248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3248_call = mutated_mod.get_global_var('func_3248')
call_3249 = func_3248_call()
output = call_3249
func_3250 = relay.Function([], output)
mutated_mod['func_3250'] = func_3250
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3307 = relay.const([[[1.296513,8.353258,-9.953925],[2.965432,-4.327113,-1.930878],[5.241925,-1.231171,-5.293241]],[[5.894849,2.772442,8.979074],[-1.814320,9.824617,8.495254],[-7.737956,1.669149,9.903459]],[[-4.166203,7.784052,2.985537],[2.125730,1.707796,-1.578824],[-1.390587,4.376180,4.856237]],[[4.938584,-8.978179,-1.741310],[-6.370477,-8.444805,-5.950370],[2.796961,-3.172176,-6.175243]],[[-0.194542,-5.820601,7.944114],[3.521397,-6.891301,5.042551],[2.238788,8.980018,7.569147]],[[3.283506,-6.089424,-3.430460],[0.393981,8.677551,-4.225197],[8.931911,7.348616,4.885541]],[[4.889584,-3.517859,0.899067],[5.259128,1.015734,-4.755553],[-7.233068,-9.439839,0.997564]],[[-9.556481,-0.412152,7.178339],[6.944969,-7.775319,-3.187606],[1.486020,-0.932237,-4.405783]],[[-3.349465,1.661540,-8.677937],[-6.462145,3.182529,-9.255390],[8.863012,-7.815413,-0.467242]],[[8.859572,-5.111431,3.428808],[2.893491,-5.193206,-4.738671],[3.693459,2.478417,-8.038235]]], dtype = "float64")#candidate|3307|(10, 3, 3)|const|float64
uop_3308 = relay.cosh(const_3307.astype('float64')) # shape=(10, 3, 3)
uop_3329 = relay.erf(const_3307.astype('float64')) # shape=(10, 3, 3)
bop_3333 = relay.floor_mod(uop_3329.astype('float64'), relay.reshape(uop_3308.astype('float64'), relay.shape_of(uop_3329))) # shape=(10, 3, 3)
func_984_call = mod.get_global_var('func_984')
func_987_call = mutated_mod.get_global_var('func_987')
var_3337 = relay.var("var_3337", dtype = "uint32", shape = (104,))#candidate|3337|(104,)|var|uint32
call_3336 = func_984_call(relay.reshape(var_3337.astype('uint32'), [1, 13, 8]))
call_3338 = func_984_call(relay.reshape(var_3337.astype('uint32'), [1, 13, 8]))
var_3351 = relay.var("var_3351", dtype = "uint32", shape = (104,))#candidate|3351|(104,)|var|uint32
bop_3352 = relay.logical_or(var_3337.astype('bool'), relay.reshape(var_3351.astype('bool'), relay.shape_of(var_3337))) # shape=(104,)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_3370 = func_1084_call()
call_3371 = func_1084_call()
func_2361_call = mod.get_global_var('func_2361')
func_2363_call = mutated_mod.get_global_var('func_2363')
call_3373 = func_2361_call()
call_3374 = func_2361_call()
func_723_call = mod.get_global_var('func_723')
func_724_call = mutated_mod.get_global_var('func_724')
call_3375 = relay.TupleGetItem(func_723_call(), 0)
call_3376 = relay.TupleGetItem(func_724_call(), 0)
func_2361_call = mod.get_global_var('func_2361')
func_2363_call = mutated_mod.get_global_var('func_2363')
call_3389 = func_2361_call()
call_3390 = func_2361_call()
var_3411 = relay.var("var_3411", dtype = "float64", shape = (10, 3, 3))#candidate|3411|(10, 3, 3)|var|float64
bop_3412 = relay.subtract(uop_3329.astype('int32'), relay.reshape(var_3411.astype('int32'), relay.shape_of(uop_3329))) # shape=(10, 3, 3)
output = relay.Tuple([bop_3333,call_3336,bop_3352,call_3370,call_3373,call_3375,call_3389,bop_3412,])
output2 = relay.Tuple([bop_3333,call_3338,bop_3352,call_3371,call_3374,call_3376,call_3390,bop_3412,])
func_3422 = relay.Function([var_3337,var_3351,var_3411,], output)
mod['func_3422'] = func_3422
mod = relay.transform.InferType()(mod)
mutated_mod['func_3422'] = func_3422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3422_call = mutated_mod.get_global_var('func_3422')
var_3424 = relay.var("var_3424", dtype = "uint32", shape = (104,))#candidate|3424|(104,)|var|uint32
var_3425 = relay.var("var_3425", dtype = "uint32", shape = (104,))#candidate|3425|(104,)|var|uint32
var_3426 = relay.var("var_3426", dtype = "float64", shape = (10, 3, 3))#candidate|3426|(10, 3, 3)|var|float64
call_3423 = func_3422_call(var_3424,var_3425,var_3426,)
output = call_3423
func_3427 = relay.Function([var_3424,var_3425,var_3426,], output)
mutated_mod['func_3427'] = func_3427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1751_call = mod.get_global_var('func_1751')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_3453 = relay.TupleGetItem(func_1751_call(), 1)
call_3454 = relay.TupleGetItem(func_1753_call(), 1)
uop_3478 = relay.atanh(call_3453.astype('float64')) # shape=(6, 2, 1)
uop_3480 = relay.atanh(call_3454.astype('float64')) # shape=(6, 2, 1)
output = uop_3478
output2 = uop_3480
func_3484 = relay.Function([], output)
mod['func_3484'] = func_3484
mod = relay.transform.InferType()(mod)
output = func_3484()
func_3485 = relay.Function([], output)
mutated_mod['func_3485'] = func_3485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_3511 = func_1084_call()
call_3512 = func_1084_call()
output = call_3511
output2 = call_3512
func_3522 = relay.Function([], output)
mod['func_3522'] = func_3522
mod = relay.transform.InferType()(mod)
mutated_mod['func_3522'] = func_3522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3522_call = mutated_mod.get_global_var('func_3522')
call_3523 = func_3522_call()
output = call_3523
func_3524 = relay.Function([], output)
mutated_mod['func_3524'] = func_3524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3248_call = mod.get_global_var('func_3248')
func_3250_call = mutated_mod.get_global_var('func_3250')
call_3625 = relay.TupleGetItem(func_3248_call(), 1)
call_3626 = relay.TupleGetItem(func_3250_call(), 1)
func_2515_call = mod.get_global_var('func_2515')
func_2518_call = mutated_mod.get_global_var('func_2518')
var_3653 = relay.var("var_3653", dtype = "float64", shape = (270,))#candidate|3653|(270,)|var|float64
call_3652 = func_2515_call(relay.reshape(var_3653.astype('float64'), [3, 15, 6]))
call_3654 = func_2515_call(relay.reshape(var_3653.astype('float64'), [3, 15, 6]))
output = relay.Tuple([call_3625,call_3652,var_3653,])
output2 = relay.Tuple([call_3626,call_3654,var_3653,])
func_3655 = relay.Function([var_3653,], output)
mod['func_3655'] = func_3655
mod = relay.transform.InferType()(mod)
var_3656 = relay.var("var_3656", dtype = "float64", shape = (270,))#candidate|3656|(270,)|var|float64
output = func_3655(var_3656)
func_3657 = relay.Function([var_3656], output)
mutated_mod['func_3657'] = func_3657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1275_call = mod.get_global_var('func_1275')
func_1276_call = mutated_mod.get_global_var('func_1276')
call_3699 = relay.TupleGetItem(func_1275_call(), 0)
call_3700 = relay.TupleGetItem(func_1276_call(), 0)
func_2426_call = mod.get_global_var('func_2426')
func_2428_call = mutated_mod.get_global_var('func_2428')
call_3702 = relay.TupleGetItem(func_2426_call(), 0)
call_3703 = relay.TupleGetItem(func_2428_call(), 0)
func_1582_call = mod.get_global_var('func_1582')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_3706 = relay.TupleGetItem(func_1582_call(), 0)
call_3707 = relay.TupleGetItem(func_1583_call(), 0)
output = relay.Tuple([call_3699,call_3702,call_3706,])
output2 = relay.Tuple([call_3700,call_3703,call_3707,])
func_3708 = relay.Function([], output)
mod['func_3708'] = func_3708
mod = relay.transform.InferType()(mod)
output = func_3708()
func_3709 = relay.Function([], output)
mutated_mod['func_3709'] = func_3709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1654_call = mod.get_global_var('func_1654')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_3771 = func_1654_call()
call_3772 = func_1654_call()
var_3780 = relay.var("var_3780", dtype = "bool", shape = (6, 2, 3))#candidate|3780|(6, 2, 3)|var|bool
bop_3781 = relay.greater(call_3771.astype('bool'), var_3780.astype('bool')) # shape=(6, 2, 3)
bop_3784 = relay.greater(call_3772.astype('bool'), var_3780.astype('bool')) # shape=(6, 2, 3)
output = bop_3781
output2 = bop_3784
func_3793 = relay.Function([var_3780,], output)
mod['func_3793'] = func_3793
mod = relay.transform.InferType()(mod)
var_3794 = relay.var("var_3794", dtype = "bool", shape = (6, 2, 3))#candidate|3794|(6, 2, 3)|var|bool
output = func_3793(var_3794)
func_3795 = relay.Function([var_3794], output)
mutated_mod['func_3795'] = func_3795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3837 = relay.var("var_3837", dtype = "float32", shape = (14, 5, 4))#candidate|3837|(14, 5, 4)|var|float32
uop_3838 = relay.sqrt(var_3837.astype('float32')) # shape=(14, 5, 4)
func_1654_call = mod.get_global_var('func_1654')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_3840 = func_1654_call()
call_3841 = func_1654_call()
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
const_3844 = relay.const([4.939362,-6.232281,-8.591306,8.657028,6.282594,-4.958524,0.518777,-0.575511,-6.186445,7.187112,-2.199477,9.413534,-2.001002,8.297329,-2.615675,4.091806,4.718915,8.640706,5.565587,-1.862710,-5.776286,3.928717,7.541468,-0.844696,3.840621,7.462846,-0.108794,3.066125,-8.230852,-5.469644,1.030036,-4.833002,9.604799,-2.795939,-4.696826,-1.178249,7.870897,5.336327,1.511698,3.432529,8.087973,-6.535808,7.276327,-6.242372,-3.095882,-7.393161,-3.057437,-2.186460,0.381381,-7.977307,5.384389,-3.715514,-2.191739,1.524518,0.320872,-5.180064,4.380115,-0.235031,-7.598045,-2.402241,-8.137738,3.062727,-3.734089,-9.523735,-3.431913,7.082561,6.864961,7.497030,7.500983,-3.896489,5.179597,3.178527,5.489524,2.407876,-9.437714,4.902583,7.632231,0.435375,-4.454118,2.498128,-4.316868,4.452987,-1.889795,3.232990,2.561420,-1.962378,9.142201,-3.729007,4.553483,-4.127801], dtype = "float64")#candidate|3844|(90,)|const|float64
call_3843 = relay.TupleGetItem(func_2326_call(relay.reshape(const_3844.astype('float64'), [90,])), 1)
call_3845 = relay.TupleGetItem(func_2328_call(relay.reshape(const_3844.astype('float64'), [90,])), 1)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_3846 = func_465_call()
call_3847 = func_465_call()
output = relay.Tuple([uop_3838,call_3840,call_3843,const_3844,call_3846,])
output2 = relay.Tuple([uop_3838,call_3841,call_3845,const_3844,call_3847,])
func_3852 = relay.Function([var_3837,], output)
mod['func_3852'] = func_3852
mod = relay.transform.InferType()(mod)
var_3853 = relay.var("var_3853", dtype = "float32", shape = (14, 5, 4))#candidate|3853|(14, 5, 4)|var|float32
output = func_3852(var_3853)
func_3854 = relay.Function([var_3853], output)
mutated_mod['func_3854'] = func_3854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1582_call = mod.get_global_var('func_1582')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_3859 = relay.TupleGetItem(func_1582_call(), 0)
call_3860 = relay.TupleGetItem(func_1583_call(), 0)
func_2534_call = mod.get_global_var('func_2534')
func_2536_call = mutated_mod.get_global_var('func_2536')
var_3862 = relay.var("var_3862", dtype = "uint32", shape = (7, 6))#candidate|3862|(7, 6)|var|uint32
call_3861 = relay.TupleGetItem(func_2534_call(relay.reshape(var_3862.astype('uint32'), [14, 3])), 3)
call_3863 = relay.TupleGetItem(func_2536_call(relay.reshape(var_3862.astype('uint32'), [14, 3])), 3)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
const_3867 = relay.const([7.884079,-8.883004,6.318116,5.118852,0.865642,-3.274853,-0.022608,-7.762407,-2.070055,-6.577034,-6.788022,3.800906,7.352287,-1.505623,-6.244146,-0.579419,2.456859,3.978151,-1.124367,-2.049189,1.542035,-8.135298,-4.659991,-8.959893,7.501344,8.549063,9.129707,9.826579,0.589282,3.657901,-2.640478,0.170206,-1.550816,4.338047,9.157564,-7.204487,-1.762787,7.952552,-2.854755,2.010996,-4.507035,3.388979,-5.700168,-6.476767,4.796053,8.083344,9.348708,9.576707], dtype = "float64")#candidate|3867|(48,)|const|float64
call_3866 = relay.TupleGetItem(func_1883_call(relay.reshape(const_3867.astype('float64'), [6, 2, 4])), 2)
call_3868 = relay.TupleGetItem(func_1885_call(relay.reshape(const_3867.astype('float64'), [6, 2, 4])), 2)
uop_3871 = relay.atanh(call_3861.astype('float64')) # shape=(210, 1)
uop_3873 = relay.atanh(call_3863.astype('float64')) # shape=(210, 1)
var_3878 = relay.var("var_3878", dtype = "float64", shape = (210, 13))#candidate|3878|(210, 13)|var|float64
bop_3879 = relay.less_equal(uop_3871.astype('bool'), var_3878.astype('bool')) # shape=(210, 13)
bop_3882 = relay.less_equal(uop_3873.astype('bool'), var_3878.astype('bool')) # shape=(210, 13)
func_3184_call = mod.get_global_var('func_3184')
func_3187_call = mutated_mod.get_global_var('func_3187')
const_3885 = relay.const([6,-10,-1,-7,-9,-8,-7,9,2,-9,10,-5,-1,8,-4,4,8,-5,10,-7,-7,8,-1,-1,10,9,-1,2,5,-2,4,-7,9,3,-7,10,9,-7,4,5,-9,-3,-7,2,6,-10,-9,-5,10,2,2,1,-2,4,-8,8,-1,8,8,1,4,-6,-10,-3,-1,-8,-9,-4,9,6,7,3,-7,-10,-10,8,-2,-7,7,5,-9,1,-1,-10,5,8,-10,-1,-3,-9,-2,7,3,-8,-7,8,-5,-3,-6,-9,-9,-4,-9,3,6,2,-10,5,4,6,6,5,-3,-10,-3,9,-7,10,-9,-7,-8,-4,10,4,3,-5,-3,2,3,4,-2,-10,5,-8,-5,-1,6,1,-5,1,-4,6,-9,1,2,-7,-8,7,7,10,-10,4,8,-1,-2,-10,-1,4,-9,-9,10,-5,-5,4,8,5,-6,-4,-8,-7,9,7,-8,-9,3,7,-6,-4,7,-4,-5,-2,1,7,-1,8,-4,10,-3,8,-9,-3,-9,7,-6,-8,-1,4,-6,-9,-5,-9,-3,2,9,6,-7,2,-6,10,9,5,-10,-2,-7,-5,10,-1,2,1,-3,9,5,-6,2,5,5,1,-8,-4,-4,7,-1,-6,-2,-6,3,-7,-9,-9,10,-2,3,-2,4,6,-5,1,1,-2,-6,10,-6,-8,-1,-5,1,5,1,-5,-5,5,1,-9,5,5,-2,1,-1,2,-5,2,4,-10,-7,10,-3,6,-2,8,6,1,10,5,-2,-3,2,3,-5,1,-7,5,-9,-5,6,10,-1,-2,-6,2,2,5,3,3,10,-1,8,-6,-7,-8,8,-6,1,-8,3,-5,7,2,-7,-1,1,-5,-6,-4,3,7,-1,2,9,9,2,-10,5,3,8,-10,-4,6,5,4,-3,3,1,4,-5,-3,-8,-8,-4,-6,4,1,-10,-9,-8,-6,5,-3,-5,8,1,-7,-6,-3,-7,-5,4,1,3,-10,5,10,-7,6,-1,2,-10,10,-5,8,-1,-4,-9,10,5,4,7,-7,8,-4,2,8,4,-7,4,-2,-10,-9,-1,4,-8,5,-2,-10,8,7,10,3,7,7,-7,4,7,-10,-4,-4,1,-10,4,3,-3,-3,8,-9,5,-6,-4,4,6,2,8,-4,7,-4,-3,-10,-7,-9,8,10,3,10,6,9,-7,4,8,4,2,-4,-5,9,-9,9,-6,3,-4,-7,8,-6,8,10,-8,9,2,-4,8,-9,4,6,-6,9,3,-2,-1,-6,8,3,10,-7,5,-9,5,-4,5,-8,9,3,-3,-5,-5,5,4,-1,-2,-7,10,-2,4,-5,-5,2,-2,8,-9,-2,-1,-8,-7,-1,7,-5,-4,1,4,8,9,-3,-2,6,3,6,7,3,2,10,-2,6,4,5,-1,7,-1,-3,-1,-4,9,2,-5,9,-1,-9,-7,-10,-10,9,5,5,6,9,-7,4,3,3,3,7,2,-6,9,-10,-10,-4,4,-1,7,8,2,-1,1,5,5,-9,-6,-8,10,7,6,7,1,10,7,-4,-1,-6,-9,6,10,3,-10,-4,8,2,-3,3,6,-3,-1,-4,2,-3,-10,6,-4,-8,9,-9,-3,10,10,9,-7,1,-1,-8,-4,3,2,5,-8,2,-5,4,-2,4,-10,-1,9,-2,-6,1,-3,-3,-4,1,-1,9,6,6,10,1,4,6,4,4,-8,10,-9,-6,-1,-5,2,10,9,-7,7,10,1,-7,-4,5,-5,-5,1,-9,10,7,-8,-3,5,6,9,-5,4,5,10,1,-6,2,-2,10,-3,-8,-5,9,-1,2,-3,-8,7,-4,-3,4,3,-7,-5,9,-3,2,-5,8,8,-4,4,-7,-5,-8,7,-10,-8,-7,3,2,10,5,-4,1,-10,-4,-9,5,-3,-6,5,-5,10,-7,-10,10,2,7,-6,-2,5,1,7,2,9,4,-2,8,-1,-9,-3,-10,4,-2,8,-9,10,-1,-7,8,-10,1,-1,8,-5,4,-5,2,-4,10,-10,6,-10,-6,-1,5,7,7,-7,2,1,-10,2,6,8,-7,6,8,-2,4,-9,7,7,5,-9,7,-5,-8,1,-1,1,-7,5,6,-8,-3,1,6,-5,5,-10,-6,1,9,10,-1,2,-2,1,-4,-8,9,-8,9,-6,9,-7,8,-3,-8,-1,-5,-4,7,3,-6,2,-10,8,6,-4,-9,-2,-6,6,-7,2,-9,9,4,1,2,-5,4,4,9,-4,6,7,-2,-6,1,5,4,10,-5,-10,-2,1,-2,7,2,2,-9,10,6,-4,-5,9,-10,-9,-9,4,-6,9,-2,1,-8,-4,6,10,-3,8,-1,7,-5,-8,7,-6,-9,-3,1,-8,1,-8,9,6,2,10,-1,9,-5,-10,1,9,3,2,10,-5,-2,-5,-2,-3,-4,-2,-9,-1,-9,1,7,9,-4,3,1,-2,-2,-5,9,-1,-2,10,-5,8,-1,2,-10,9,-2,-5,-2,-9,5,1,4,9,-6,-7,-1,2,7,2,-5,-1,-3,3,5,-2,-5,-6,-4,7,3,8,3,6,4,-7,-10,9,5,1,-3,10,-3,-9,1,-6,1,8,3,-2,-3,7,7,7,7,2,10,-10,-8,1,-4,-4,10,-9,-6,-2,-1,-2,-7,10,6,6,4,10,-2,3,-7,-2,-9,-10,1,-3,10,-9,-6,-3,-3,-10,-2,10,1,-1,-10,-3,-4,-3,-4,-7,4,3,7,2,-4,6,3,1,9,2,7,-8,10,-7,-8,1,10,-1,10,6,6,-2,-2,-4,-7,10,-6,6,-10,2,-5,1,7,-4,-5,-2,4,1,9,9,-4,1,-7,-7,9,-6,-2,-2,9,7,6,-5,5,8,-3,-9,6,-8,6,4,3,-2,7,4,-7,9,10,8,10,-9,-3,-10,10,-3,-1,4,7,1,-9,1,5,3,-4,3,7,8,2,-8,-6,-1,-10,-5,2,-2,-10,-8,2,4,-2,-1,9,-6,7,-5,7,-2,-4,3,-10,8,-5,-8,-8,5,9,7,-5,-1,9,5,-4,4,-1,-4,1,4,-8,4,-7,8,-5,6,-9,2,6,7,-4,10,5,8,-5,3,7,1,-6,-1,-3,-1,-7,2,2,-3,-8,2,6,1,-4,-7,2,6,7,9,4,2,-4,-5,4,3,-3,-7,-6,-2,-5,-3,9,2,-7,-3,10,-4,-10,1,9,5,-8,10,-1,6,3,2,9,5,-5,-8,-6,1,3,9,5,-1,4,-1,-6,-2,8,-1,8,-4,-6,1,-7,5,4,10,-8,4,-6,9,-2,3,7,-9,-9,1,5,7,-4,-2,6,8,6,-8,-9,-4,-9,2,-10,4,-4,-7,7,-1,-6,-7,-6,8,9,2,-2,10,5,1,3,-9,10,-5,7,6,-10,8,2,-6,2,10,8,9,-3,1,6,4,5,5,-7,7,-5,-1,-3,-9,-7,-10,8,8,-2,9,8,-7,5,7,2,9,-9,4,7,6,2,-7,-7,-4,-6,8,6,-7,5,3,7,5,-2,5,-4,-5,9,9,-9,-5,-7,8,-8,6,-10,3,1,-1,-10,-6,9,3,5,4,-6,-8,-3,6,-3,7,1,1,7,-9,-2,3,6,9,-7,-7,1,-6,4,-6,-4,2,-2,-9,7,-5,-3,-10,4,2,4,6,5,-2,6,7,2,7,-2,-2,-4,-8,5,8,1,3,-7,1,-5,-2,2,2,9,-5,-8,10,3,-1,-9,-2,-6,4,-5,7,9,-10,-9,4,-4,8,7,5,7,-2,2,-7,-6,4,-9,1,2,-10,6,10,-6,-3,8,2,-4,4,-8,-6,5,6,-3,-1,-10,6,8,7,6,-4,10,10,2,-1,6,-5,-7,2,-1,5,-7,-7,-8,-8,6,7,-9,9,-2,4,-8,-8,1,5,6,-3,-10,7,-7,-2,-8,-9,9,-10,8,8,4,-1,7,-7,5,-5,2,-2,-8,4,-7,-3,-2,-7,9,-8,-3,-8,-4,-5,-6,-1,4,-1,-2,-8,-9,5,-4,-4,10,-5,-1,-5,-9,2,-1,-6,-10,7,2,-1,6,4,8,2,2,-1,10,5,-6,-5,-2,4,-7,-4,-6,-2,10,-2,-8,6,-4,10,-5,-3,6,10,10,9,-4,-8,7,3,-10,6,9,-5,-1,7,3,-6,2,6,7,9,6,2,-9,-1,-9,-6,-8,-3,7,-4,-4,9,6,7,-9,-7,-6,-10,-5,6,7,4,3,6,-1,-10,3,-10,5,2,-4,10,-9,6,1,-8,4], dtype = "uint8")#candidate|3885|(1620,)|const|uint8
call_3884 = func_3184_call(relay.reshape(const_3885.astype('uint8'), [12, 15, 9]))
call_3886 = func_3184_call(relay.reshape(const_3885.astype('uint8'), [12, 15, 9]))
output = relay.Tuple([call_3859,var_3862,call_3866,const_3867,bop_3879,call_3884,const_3885,])
output2 = relay.Tuple([call_3860,var_3862,call_3868,const_3867,bop_3882,call_3886,const_3885,])
func_3891 = relay.Function([var_3862,var_3878,], output)
mod['func_3891'] = func_3891
mod = relay.transform.InferType()(mod)
mutated_mod['func_3891'] = func_3891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3891_call = mutated_mod.get_global_var('func_3891')
var_3893 = relay.var("var_3893", dtype = "uint32", shape = (7, 6))#candidate|3893|(7, 6)|var|uint32
var_3894 = relay.var("var_3894", dtype = "float64", shape = (210, 13))#candidate|3894|(210, 13)|var|float64
call_3892 = func_3891_call(var_3893,var_3894,)
output = call_3892
func_3895 = relay.Function([var_3893,var_3894,], output)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_3902 = relay.TupleGetItem(func_2042_call(), 0)
call_3903 = relay.TupleGetItem(func_2044_call(), 0)
func_2778_call = mod.get_global_var('func_2778')
func_2781_call = mutated_mod.get_global_var('func_2781')
var_3907 = relay.var("var_3907", dtype = "uint16", shape = (220, 2))#candidate|3907|(220, 2)|var|uint16
call_3906 = relay.TupleGetItem(func_2778_call(relay.reshape(var_3907.astype('uint16'), [8, 5, 11]), relay.reshape(var_3907.astype('uint16'), [8, 5, 11]), ), 0)
call_3908 = relay.TupleGetItem(func_2781_call(relay.reshape(var_3907.astype('uint16'), [8, 5, 11]), relay.reshape(var_3907.astype('uint16'), [8, 5, 11]), ), 0)
func_2907_call = mod.get_global_var('func_2907')
func_2912_call = mutated_mod.get_global_var('func_2912')
const_3925 = relay.const([0.516629,5.424336,-7.536176,-4.977116,-0.721480,8.653847,-4.829891,-5.279853,9.410322,-7.331618,9.756019,-5.856297,-8.064399,-7.963284,-8.928737,4.465575,9.871078,-5.173269,-3.505132,7.943570,9.616183,-7.982115,5.786326,-9.574196,-0.662365,-2.373695,-6.270566,-5.850168,-7.867823,-9.088796,-2.735225,3.148484,7.639226,0.431323,-8.991985,-6.980496,0.411898,0.453504,7.700249,8.339869,-1.890784,-8.629637,9.078173,2.537041,6.693600,-8.640590,7.909187,6.131307,6.553557,-6.808424,-3.384264,-6.008346,7.350188,-7.583500,8.838207,7.207899,3.214530,-3.662248,-6.937209,1.994695,-0.469323,5.578505,6.028642,-6.275753,7.297060,-5.586613,6.295775,-4.251112,-3.763406,9.477953,-0.020646,3.715221,-1.027132,-0.467916,9.420913,-1.935906,-5.845816,1.039227,2.387535,-6.159938,2.565919,-9.536922,8.831059,5.716984,6.476972,2.657496,3.966958,-2.777391,9.298649,-0.531478,-3.934095,-3.548641,-9.692266,-7.123440,7.288328,5.759114,5.814014,5.627873,-2.965276,-1.648092,7.944627,6.137486,-5.969746,4.948349,7.655619,-2.257976,-2.228330,-0.944718,-7.270550,-6.583835,9.659532,-8.546914,0.029405,-7.360963,0.456310,-5.951518,-8.496387,2.654703,0.579846,-8.050880,1.489619,-8.852223,8.431614,-6.737741,3.279709,1.359166,-6.894581,4.153001,2.025339,9.659348,-9.463224,-1.270066,-4.592934,2.096135,-9.526549,-5.925076,-9.734448,2.331538,9.042064,1.722841,7.961705,9.868223,1.773962,3.935335,-5.883454,0.309816,-7.861704,-8.509189,3.963636,-2.287257,9.526336,7.274551,3.715813,-6.927986,7.879352,8.176426,-0.358367,-1.900614,6.559988,9.902262,6.799428,-2.041184,-1.739566,-7.376779,-3.603452,4.235681,9.065491,8.989856,0.180067,5.100682,-4.200819,9.665422,9.363872,-4.863651,-0.255665,6.705618,-9.796392,9.159643,-2.083224,-3.763302,3.509497,-8.052413,0.564917,6.278861,1.841385,8.792742,-8.108828,0.527989,-0.386668,-9.162775,4.866734,-1.254748], dtype = "float32")#candidate|3925|(192,)|const|float32
var_3926 = relay.var("var_3926", dtype = "float64", shape = (1, 48))#candidate|3926|(1, 48)|var|float64
const_3927 = relay.const(-5.667220, dtype = "float64")#candidate|3927|()|const|float64
call_3924 = relay.TupleGetItem(func_2907_call(relay.reshape(const_3925.astype('float32'), [6, 2, 16]), relay.reshape(var_3926.astype('float64'), [48,]), relay.reshape(const_3927.astype('float64'), []), ), 5)
call_3928 = relay.TupleGetItem(func_2912_call(relay.reshape(const_3925.astype('float32'), [6, 2, 16]), relay.reshape(var_3926.astype('float64'), [48,]), relay.reshape(const_3927.astype('float64'), []), ), 5)
func_3793_call = mod.get_global_var('func_3793')
func_3795_call = mutated_mod.get_global_var('func_3795')
const_3935 = relay.const([[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True]], dtype = "bool")#candidate|3935|(36, 1)|const|bool
call_3934 = func_3793_call(relay.reshape(const_3935.astype('bool'), [6, 2, 3]))
call_3936 = func_3793_call(relay.reshape(const_3935.astype('bool'), [6, 2, 3]))
func_1654_call = mod.get_global_var('func_1654')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_3949 = func_1654_call()
call_3950 = func_1654_call()
output = relay.Tuple([call_3902,call_3906,var_3907,call_3924,const_3925,var_3926,const_3927,call_3934,const_3935,call_3949,])
output2 = relay.Tuple([call_3903,call_3908,var_3907,call_3928,const_3925,var_3926,const_3927,call_3936,const_3935,call_3950,])
func_3956 = relay.Function([var_3907,var_3926,], output)
mod['func_3956'] = func_3956
mod = relay.transform.InferType()(mod)
mutated_mod['func_3956'] = func_3956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3956_call = mutated_mod.get_global_var('func_3956')
var_3958 = relay.var("var_3958", dtype = "uint16", shape = (220, 2))#candidate|3958|(220, 2)|var|uint16
var_3959 = relay.var("var_3959", dtype = "float64", shape = (1, 48))#candidate|3959|(1, 48)|var|float64
call_3957 = func_3956_call(var_3958,var_3959,)
output = call_3957
func_3960 = relay.Function([var_3958,var_3959,], output)
mutated_mod['func_3960'] = func_3960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_3972 = relay.TupleGetItem(func_1186_call(), 2)
call_3973 = relay.TupleGetItem(func_1187_call(), 2)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_3987 = func_995_call()
call_3988 = func_995_call()
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_4003 = func_1084_call()
call_4004 = func_1084_call()
func_2121_call = mod.get_global_var('func_2121')
func_2122_call = mutated_mod.get_global_var('func_2122')
call_4013 = func_2121_call()
call_4014 = func_2121_call()
bop_4017 = relay.left_shift(call_3987.astype('uint8'), relay.reshape(call_4003.astype('uint8'), relay.shape_of(call_3987))) # shape=(6, 2, 1)
bop_4020 = relay.left_shift(call_3988.astype('uint8'), relay.reshape(call_4004.astype('uint8'), relay.shape_of(call_3988))) # shape=(6, 2, 1)
func_3793_call = mod.get_global_var('func_3793')
func_3795_call = mutated_mod.get_global_var('func_3795')
var_4033 = relay.var("var_4033", dtype = "bool", shape = (36,))#candidate|4033|(36,)|var|bool
call_4032 = func_3793_call(relay.reshape(var_4033.astype('bool'), [6, 2, 3]))
call_4034 = func_3793_call(relay.reshape(var_4033.astype('bool'), [6, 2, 3]))
func_2625_call = mod.get_global_var('func_2625')
func_2628_call = mutated_mod.get_global_var('func_2628')
var_4037 = relay.var("var_4037", dtype = "uint32", shape = (104,))#candidate|4037|(104,)|var|uint32
call_4036 = func_2625_call(relay.reshape(var_4037.astype('uint32'), [2, 52]))
call_4038 = func_2625_call(relay.reshape(var_4037.astype('uint32'), [2, 52]))
func_1616_call = mod.get_global_var('func_1616')
func_1620_call = mutated_mod.get_global_var('func_1620')
const_4044 = relay.const(-2.427254, dtype = "float64")#candidate|4044|()|const|float64
call_4043 = relay.TupleGetItem(func_1616_call(relay.reshape(const_4044.astype('float64'), []), relay.reshape(call_3987.astype('float64'), [6, 2, 1]), ), 1)
call_4045 = relay.TupleGetItem(func_1620_call(relay.reshape(const_4044.astype('float64'), []), relay.reshape(call_3987.astype('float64'), [6, 2, 1]), ), 1)
func_2985_call = mod.get_global_var('func_2985')
func_2986_call = mutated_mod.get_global_var('func_2986')
call_4058 = relay.TupleGetItem(func_2985_call(), 1)
call_4059 = relay.TupleGetItem(func_2986_call(), 1)
func_623_call = mod.get_global_var('func_623')
func_626_call = mutated_mod.get_global_var('func_626')
const_4064 = relay.const([4,-7,-1,-8,2,3,-5,-4,-2,-8,7,-2,-3,6,-8,5,9,2], dtype = "uint8")#candidate|4064|(18,)|const|uint8
const_4065 = relay.const([-2,-4,-10,9,9,-9,10,5,10,-5,-3,3,6,8,-1,10,1,-8,6,6,-9,-10,-3,-1,2,1,-8,1,-6,5,9,1,-1,4,-8,-3,-7,6,-10,5,2,7,-2,-7,9,-8,-7,-2,-9,8,-7,4,3,-2,-8,5,4,-3,10,5,-2,-10,1,7,-8,-9,3,-7,-7,9,7,-7,-4,5,10,5,-4,-1,7,-7,3,10,-9,-4,5,2,-7,-2,1,7,9,5,7,8,-4,-10,1,4,-6,-8,2,-4,-3,2,-6,-7,-2,-8], dtype = "uint8")#candidate|4065|(108,)|const|uint8
call_4063 = func_623_call(relay.reshape(const_4064.astype('uint8'), [6, 3, 1]), relay.reshape(const_4065.astype('uint8'), [6, 3, 6]), )
call_4066 = func_623_call(relay.reshape(const_4064.astype('uint8'), [6, 3, 1]), relay.reshape(const_4065.astype('uint8'), [6, 3, 6]), )
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_4078 = func_995_call()
call_4079 = func_995_call()
func_3522_call = mod.get_global_var('func_3522')
func_3524_call = mutated_mod.get_global_var('func_3524')
call_4087 = func_3522_call()
call_4088 = func_3522_call()
output = relay.Tuple([call_3972,call_4013,bop_4017,call_4032,var_4033,call_4036,var_4037,call_4043,const_4044,call_4058,call_4063,const_4064,const_4065,call_4078,call_4087,])
output2 = relay.Tuple([call_3973,call_4014,bop_4020,call_4034,var_4033,call_4038,var_4037,call_4045,const_4044,call_4059,call_4066,const_4064,const_4065,call_4079,call_4088,])
func_4100 = relay.Function([var_4033,var_4037,], output)
mod['func_4100'] = func_4100
mod = relay.transform.InferType()(mod)
var_4101 = relay.var("var_4101", dtype = "bool", shape = (36,))#candidate|4101|(36,)|var|bool
var_4102 = relay.var("var_4102", dtype = "uint32", shape = (104,))#candidate|4102|(104,)|var|uint32
output = func_4100(var_4101,var_4102,)
func_4103 = relay.Function([var_4101,var_4102,], output)
mutated_mod['func_4103'] = func_4103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2985_call = mod.get_global_var('func_2985')
func_2986_call = mutated_mod.get_global_var('func_2986')
call_4131 = relay.TupleGetItem(func_2985_call(), 0)
call_4132 = relay.TupleGetItem(func_2986_call(), 0)
output = call_4131
output2 = call_4132
func_4148 = relay.Function([], output)
mod['func_4148'] = func_4148
mod = relay.transform.InferType()(mod)
mutated_mod['func_4148'] = func_4148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4148_call = mutated_mod.get_global_var('func_4148')
call_4149 = func_4148_call()
output = call_4149
func_4150 = relay.Function([], output)
mutated_mod['func_4150'] = func_4150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1415_call = mod.get_global_var('func_1415')
func_1416_call = mutated_mod.get_global_var('func_1416')
call_4159 = func_1415_call()
call_4160 = func_1415_call()
const_4167 = relay.const([[[-0.904390,4.550684,-8.924214,1.927764,7.833584,5.476192],[-3.983489,5.891264,8.869138,-5.240113,5.585981,4.661406],[9.228138,-8.103055,5.148943,9.598097,-8.586216,-5.282138],[-8.917113,-5.314390,5.477788,6.417389,6.824995,-2.340830],[2.873969,4.449717,2.472205,-9.974401,8.944648,7.953667],[-6.967515,-4.617854,-5.753487,7.947648,-6.492084,-9.273939],[5.995258,-4.755003,-5.533023,-5.081745,6.061369,7.258717],[-2.294196,5.022094,-3.291803,-8.475166,0.214185,9.602478],[2.584037,7.455164,-5.719285,3.925509,1.926681,-5.618869],[-4.745439,1.368865,3.544569,-4.679730,3.976066,2.779342],[9.344020,-8.399111,7.053764,-3.074336,3.046447,-3.548317]],[[0.478709,4.905245,5.038205,-3.854070,-1.054558,8.220539],[-9.456310,1.752271,-0.493206,7.460117,-7.633679,-0.348945],[-0.987880,-3.638269,-2.317909,6.949701,-6.466425,5.771008],[4.837032,-9.909208,4.473480,5.848800,8.991970,0.442131],[2.982662,5.145227,0.878959,3.289309,-3.577337,9.999498],[7.472776,-6.847298,0.584947,7.599754,-4.248314,2.254495],[-0.260530,3.931755,5.936942,0.245475,-1.322165,4.063538],[-8.082228,1.915681,-7.200356,-1.986675,2.661383,-5.821734],[-3.990828,7.653121,4.086510,-0.634106,6.304176,7.505750],[9.764010,-5.483669,-2.048643,5.947875,-5.350142,7.993195],[0.086186,-2.852020,0.803190,8.229149,3.963936,-8.650552]],[[6.381623,-9.616150,-8.769122,-5.791049,-7.404241,4.114513],[-1.547651,1.048182,2.805052,3.056910,-7.417669,-1.237204],[-6.529123,7.989469,-5.952185,-3.497372,6.598745,4.974933],[7.306799,1.902614,-5.588509,-7.337489,3.350000,7.963026],[-8.680747,4.487970,6.064381,-6.835497,1.578697,0.704941],[5.409958,-9.981672,-0.136792,2.973323,0.175551,0.140078],[6.133410,-4.902135,6.063453,-4.203491,-9.536894,0.191470],[0.095861,-2.551356,4.885428,-4.924896,5.877282,2.926272],[-3.358491,2.593033,7.654932,4.661249,-6.946475,1.482783],[-7.277295,-8.639036,2.610129,-9.899345,6.798974,-8.287931],[-5.325346,-4.832679,4.731607,6.531316,-6.084278,7.581930]],[[1.878333,-4.267728,-7.208743,1.819668,2.013345,1.224630],[9.561986,1.400629,-2.730207,-3.101854,6.613814,9.079767],[-6.712679,-8.280751,2.181829,5.132269,3.137384,2.977643],[7.022619,-6.448384,-9.253837,-8.011981,8.990387,-2.658479],[1.088988,-7.798157,5.244188,5.470248,-6.323299,-7.417471],[5.623575,-4.033807,-5.326831,-1.750613,-1.686442,-8.391827],[-1.788539,3.508176,4.736370,-0.732060,-3.947936,3.484232],[-2.910140,5.516724,-9.354405,-1.775474,6.110421,-7.500679],[-1.810659,-1.896840,8.699897,5.639527,7.506453,4.898578],[1.968077,2.019767,-0.245196,4.028680,5.628408,5.900682],[7.481483,7.578115,-7.321464,-1.371632,-1.924113,-4.056741]],[[3.676314,4.409183,-0.308818,5.212939,-4.755112,6.503396],[5.441255,9.619157,7.632028,9.013639,8.975266,-9.908706],[-2.137233,-2.253217,7.728496,9.920245,9.893654,7.689722],[9.207583,0.304262,3.651716,1.999102,6.436908,5.175698],[7.704409,4.083970,3.337059,9.938918,-0.684674,-4.359672],[-5.434508,6.801342,-9.224248,5.278453,4.785233,-3.002145],[7.653085,-3.872159,-5.597343,7.422141,-5.008066,-9.741670],[-1.345730,6.804850,-6.584320,-1.968513,7.459156,-6.878821],[-5.072953,-0.971488,-6.653480,-2.633354,-3.534764,-8.133752],[-4.660923,-3.911738,2.673123,-7.192031,-4.552001,-3.767967],[2.592160,6.338304,-2.487103,0.296457,3.789046,5.105104]],[[-8.003969,7.439820,-2.317330,4.244727,-7.016987,4.701119],[3.951076,8.482237,8.406521,-5.888708,1.334684,-3.947549],[9.421264,-5.035571,6.028296,-6.669637,-2.583323,-7.197685],[7.388409,0.482031,1.002028,9.036429,3.328601,3.135270],[5.306467,8.520654,3.203539,-3.257694,4.707309,-9.708243],[-0.915075,-4.812633,-6.125939,9.789956,8.412068,6.019545],[5.431737,9.814621,-0.423138,-5.651674,-1.330949,-7.353812],[5.790867,-5.997436,3.502893,5.314434,9.666092,-1.803446],[-4.461488,8.630212,4.487136,-4.103159,-6.213101,9.233783],[-8.341276,-2.534628,1.492222,8.322952,8.804293,-7.210930],[-1.511535,1.521843,0.615397,2.071542,7.735135,1.679977]],[[-3.626740,-1.734271,0.589307,8.866010,9.185254,-8.302996],[-8.310175,0.676780,8.048391,-2.620479,3.798380,0.866359],[-3.262368,-9.137483,-9.914932,-0.737673,3.960226,7.515600],[-5.915206,6.869751,-3.000242,-9.669762,2.938010,-1.635072],[2.028645,-5.010239,-9.858857,-0.101054,-4.391324,7.799037],[-6.873963,6.882660,-1.216130,2.763774,5.697187,-6.332146],[-3.941010,-1.059580,-9.698847,2.116283,-2.657907,-7.753550],[2.142565,1.357765,0.084861,-7.883181,-4.755393,4.117136],[-3.575260,0.676550,1.767868,9.793860,-0.133264,4.093600],[7.707423,8.154152,-5.008531,-6.864265,-1.502173,-3.621360],[-4.750265,7.746780,-8.979385,9.870410,5.008052,6.566963]],[[-3.771624,7.411332,-1.348858,5.074276,1.751277,4.923431],[-0.808297,4.928990,3.594957,-0.801746,7.152180,-8.446847],[8.496598,-8.124635,-3.006396,0.369814,5.059453,-3.581480],[-0.589675,8.781239,-0.253921,8.293902,-9.264260,5.030747],[-0.867570,-4.272119,7.618068,-7.784777,-5.871675,-7.364614],[-6.525601,-9.633324,-0.529696,3.316273,-2.206004,-2.157620],[-5.138995,-2.229047,-7.791084,-6.331382,9.031222,-5.935921],[-3.951133,5.696942,-1.066865,0.412802,-5.580739,-0.311486],[-7.780000,8.196841,-7.552481,7.024303,9.980981,8.693153],[0.647781,1.839095,-2.608055,-6.784096,-7.883349,-1.332422],[5.346543,9.960458,0.363218,-3.081257,9.988310,-8.154945]],[[2.172765,-4.262950,3.898741,-3.383820,-5.806818,-9.593375],[-0.200511,5.927785,-0.736681,8.009125,0.984137,1.392714],[-4.405415,0.900619,5.046274,9.691203,8.961513,-9.526224],[0.003526,-9.960374,-9.775162,6.514506,4.161766,5.943863],[-5.273022,1.258680,3.417064,-5.248171,-4.320994,0.133618],[6.564028,-2.387583,5.738243,-5.771588,7.559990,-9.798847],[8.177591,-7.323155,-3.859485,-5.965766,-0.200269,-0.584319],[4.806875,1.642566,-3.849737,9.574782,6.626180,7.394460],[-5.727111,-9.392563,-9.539260,9.571901,-3.081150,-4.658620],[4.090993,8.487831,-7.580625,6.449035,-5.283817,0.783237],[-0.236901,-8.411216,-9.591040,-3.452403,9.943307,-9.222590]],[[4.488777,7.511211,-9.990474,-7.082849,6.290259,0.394689],[2.054398,5.992790,-4.083955,8.242712,1.696060,-7.041880],[8.985116,6.986606,0.177512,-8.229027,8.314529,-5.273982],[8.914315,-2.930617,-0.927667,-1.014346,-5.198327,9.122460],[-3.639455,5.040255,4.465859,0.282943,-0.688575,5.818389],[-8.319152,-0.508544,-7.106852,0.156981,6.370640,-4.980520],[-2.442783,-9.923258,-4.480166,1.415507,-0.497537,-5.142747],[-5.886526,-7.548189,-6.408819,9.490182,0.277034,9.996226],[-7.558968,8.530791,-2.580675,-4.418339,-6.004465,7.590875],[-7.971060,0.800893,-6.343225,-6.541532,0.978443,1.818374],[3.687643,-0.836705,0.374125,-4.283760,3.414718,9.253784]],[[5.155961,-9.624936,-6.927702,-8.794921,-2.277117,3.000741],[4.084975,1.246633,-5.947870,7.818580,4.510040,-3.617318],[1.577231,4.417545,-9.441468,-6.943933,-5.449743,1.818672],[-4.303414,5.663012,4.880330,5.072596,1.000703,9.099721],[-8.029109,9.005658,1.792041,-8.190028,-0.290182,1.016545],[-5.303519,-2.386596,-0.793196,-7.328713,6.050911,4.866293],[-8.741611,1.597457,8.300787,-3.603439,6.188952,-4.745973],[3.992849,6.726567,-9.230929,2.521693,-7.740146,9.773497],[3.525802,-4.862667,7.828539,-8.106292,-6.695249,2.023128],[-7.761055,5.405262,0.961221,-4.890610,-0.190350,-7.143661],[-2.077603,-0.102156,5.138209,6.810347,6.581938,9.553159]],[[5.691310,-9.279522,-3.443304,-2.463169,4.298501,-4.847962],[1.821035,-6.588408,9.397996,-0.484110,-6.583271,-8.227791],[-3.955821,-7.614650,2.940889,-2.258602,2.307563,3.572446],[1.698393,3.661833,2.378091,3.354168,-6.276613,1.802409],[0.007028,-9.124429,-4.750335,7.716271,-1.485216,-5.382678],[-8.493032,5.521163,5.274940,6.814623,-1.190611,-2.323143],[-9.776564,-7.375726,4.029331,-6.241261,1.842082,-6.640551],[-7.271984,-7.023412,7.920140,-9.322023,2.447797,-2.196863],[-1.719635,9.053204,-1.613721,6.389239,-6.833336,1.891321],[0.279457,-4.786366,-7.716996,-1.467068,-3.347784,-8.666746],[0.464933,8.265698,-6.792718,0.043831,2.921272,0.948639]],[[-3.535757,7.707689,-7.557076,-8.388833,-0.465567,-0.822441],[9.015267,2.941613,0.595764,-5.884060,3.995347,8.415870],[1.938506,-0.940865,-2.915837,-2.380417,-9.033607,0.071805],[-6.904720,-0.465379,-8.066130,-2.508975,7.242250,7.000348],[4.654148,8.748871,-4.030601,-7.330660,-7.406443,-8.212368],[-5.056490,6.638651,-9.993016,9.328549,5.116910,-8.245542],[-3.559857,0.682594,-3.204221,-0.295546,-2.190146,-8.513394],[-4.490623,-7.816076,-4.418508,8.502956,7.136371,4.663054],[7.879998,3.792036,6.783503,-6.865376,-5.200167,9.466072],[0.156347,-7.219361,-0.839634,-6.292207,8.092168,3.467125],[2.837336,-5.321183,0.477514,1.400852,-8.702364,5.927886]],[[-3.635485,0.062976,-1.625270,7.885658,-6.801995,6.324011],[3.908884,2.086281,8.058501,-6.784854,-3.931030,5.729912],[-9.250317,-7.597788,9.762190,-2.658395,-4.607404,-0.326869],[0.539035,-3.637519,7.433267,-8.359618,8.247548,9.454935],[-7.685581,2.547617,-1.657002,-4.559011,0.087010,2.533434],[8.793116,-8.483595,9.221995,-1.598619,9.353505,-8.099353],[-0.353360,3.032599,8.940549,-5.407307,-3.008964,-1.714831],[7.630947,6.803355,6.405607,4.793776,5.551381,-6.887977],[4.751768,1.349243,7.698422,9.478086,-2.406850,4.645753],[-4.755941,2.793708,-7.163558,6.278995,-6.071884,-2.675076],[-9.804414,-6.559311,-2.776537,-6.963540,9.244427,-1.736034]]], dtype = "float64")#candidate|4167|(14, 11, 6)|const|float64
bop_4168 = relay.less(call_4159.astype('bool'), relay.reshape(const_4167.astype('bool'), relay.shape_of(call_4159))) # shape=(14, 11, 6)
bop_4171 = relay.less(call_4160.astype('bool'), relay.reshape(const_4167.astype('bool'), relay.shape_of(call_4160))) # shape=(14, 11, 6)
bop_4179 = relay.maximum(const_4167.astype('int8'), relay.reshape(call_4159.astype('int8'), relay.shape_of(const_4167))) # shape=(14, 11, 6)
bop_4182 = relay.maximum(const_4167.astype('int8'), relay.reshape(call_4160.astype('int8'), relay.shape_of(const_4167))) # shape=(14, 11, 6)
func_4148_call = mod.get_global_var('func_4148')
func_4150_call = mutated_mod.get_global_var('func_4150')
call_4183 = func_4148_call()
call_4184 = func_4148_call()
func_3484_call = mod.get_global_var('func_3484')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_4200 = func_3484_call()
call_4201 = func_3484_call()
output = relay.Tuple([bop_4168,bop_4179,call_4183,call_4200,])
output2 = relay.Tuple([bop_4171,bop_4182,call_4184,call_4201,])
func_4207 = relay.Function([], output)
mod['func_4207'] = func_4207
mod = relay.transform.InferType()(mod)
output = func_4207()
func_4208 = relay.Function([], output)
mutated_mod['func_4208'] = func_4208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4232 = relay.var("var_4232", dtype = "float64", shape = (15, 6, 15))#candidate|4232|(15, 6, 15)|var|float64
uop_4233 = relay.sqrt(var_4232.astype('float64')) # shape=(15, 6, 15)
func_3655_call = mod.get_global_var('func_3655')
func_3657_call = mutated_mod.get_global_var('func_3657')
var_4240 = relay.var("var_4240", dtype = "float64", shape = (270,))#candidate|4240|(270,)|var|float64
call_4239 = relay.TupleGetItem(func_3655_call(relay.reshape(var_4240.astype('float64'), [270,])), 1)
call_4241 = relay.TupleGetItem(func_3657_call(relay.reshape(var_4240.astype('float64'), [270,])), 1)
output = relay.Tuple([uop_4233,call_4239,var_4240,])
output2 = relay.Tuple([uop_4233,call_4241,var_4240,])
func_4242 = relay.Function([var_4232,var_4240,], output)
mod['func_4242'] = func_4242
mod = relay.transform.InferType()(mod)
var_4243 = relay.var("var_4243", dtype = "float64", shape = (15, 6, 15))#candidate|4243|(15, 6, 15)|var|float64
var_4244 = relay.var("var_4244", dtype = "float64", shape = (270,))#candidate|4244|(270,)|var|float64
output = func_4242(var_4243,var_4244,)
func_4245 = relay.Function([var_4243,var_4244,], output)
mutated_mod['func_4245'] = func_4245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4207_call = mod.get_global_var('func_4207')
func_4208_call = mutated_mod.get_global_var('func_4208')
call_4264 = relay.TupleGetItem(func_4207_call(), 1)
call_4265 = relay.TupleGetItem(func_4208_call(), 1)
output = call_4264
output2 = call_4265
func_4266 = relay.Function([], output)
mod['func_4266'] = func_4266
mod = relay.transform.InferType()(mod)
output = func_4266()
func_4267 = relay.Function([], output)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3248_call = mod.get_global_var('func_3248')
func_3250_call = mutated_mod.get_global_var('func_3250')
call_4353 = relay.TupleGetItem(func_3248_call(), 0)
call_4354 = relay.TupleGetItem(func_3250_call(), 0)
var_4368 = relay.var("var_4368", dtype = "float64", shape = (6, 2, 6))#candidate|4368|(6, 2, 6)|var|float64
bop_4369 = relay.add(call_4353.astype('int16'), var_4368.astype('int16')) # shape=(6, 2, 6)
bop_4372 = relay.add(call_4354.astype('int16'), var_4368.astype('int16')) # shape=(6, 2, 6)
var_4374 = relay.var("var_4374", dtype = "float64", shape = (6, 2, 15))#candidate|4374|(6, 2, 15)|var|float64
bop_4375 = relay.maximum(call_4353.astype('int16'), var_4374.astype('int16')) # shape=(6, 2, 15)
bop_4378 = relay.maximum(call_4354.astype('int16'), var_4374.astype('int16')) # shape=(6, 2, 15)
output = relay.Tuple([bop_4369,bop_4375,])
output2 = relay.Tuple([bop_4372,bop_4378,])
func_4380 = relay.Function([var_4368,var_4374,], output)
mod['func_4380'] = func_4380
mod = relay.transform.InferType()(mod)
var_4381 = relay.var("var_4381", dtype = "float64", shape = (6, 2, 6))#candidate|4381|(6, 2, 6)|var|float64
var_4382 = relay.var("var_4382", dtype = "float64", shape = (6, 2, 15))#candidate|4382|(6, 2, 15)|var|float64
output = func_4380(var_4381,var_4382,)
func_4383 = relay.Function([var_4381,var_4382,], output)
mutated_mod['func_4383'] = func_4383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_4395 = relay.TupleGetItem(func_2042_call(), 0)
call_4396 = relay.TupleGetItem(func_2044_call(), 0)
var_4405 = relay.var("var_4405", dtype = "float32", shape = (6, 2, 10))#candidate|4405|(6, 2, 10)|var|float32
bop_4406 = relay.equal(call_4395.astype('bool'), var_4405.astype('bool')) # shape=(6, 2, 10)
bop_4409 = relay.equal(call_4396.astype('bool'), var_4405.astype('bool')) # shape=(6, 2, 10)
func_2161_call = mod.get_global_var('func_2161')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_4424 = relay.TupleGetItem(func_2161_call(relay.reshape(bop_4406.astype('float32'), [4, 2, 15])), 0)
call_4425 = relay.TupleGetItem(func_2164_call(relay.reshape(bop_4406.astype('float32'), [4, 2, 15])), 0)
uop_4432 = relay.log2(var_4405.astype('float32')) # shape=(6, 2, 10)
output = relay.Tuple([bop_4406,call_4424,uop_4432,])
output2 = relay.Tuple([bop_4409,call_4425,uop_4432,])
func_4436 = relay.Function([var_4405,], output)
mod['func_4436'] = func_4436
mod = relay.transform.InferType()(mod)
mutated_mod['func_4436'] = func_4436
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4437 = relay.var("var_4437", dtype = "float32", shape = (6, 2, 10))#candidate|4437|(6, 2, 10)|var|float32
func_4436_call = mutated_mod.get_global_var('func_4436')
call_4438 = func_4436_call(var_4437)
output = call_4438
func_4439 = relay.Function([var_4437], output)
mutated_mod['func_4439'] = func_4439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_4495 = relay.TupleGetItem(func_448_call(), 0)
call_4496 = relay.TupleGetItem(func_450_call(), 0)
var_4514 = relay.var("var_4514", dtype = "float32", shape = (6, 2, 12))#candidate|4514|(6, 2, 12)|var|float32
bop_4515 = relay.left_shift(call_4495.astype('int64'), var_4514.astype('int64')) # shape=(6, 2, 12)
bop_4518 = relay.left_shift(call_4496.astype('int64'), var_4514.astype('int64')) # shape=(6, 2, 12)
uop_4529 = relay.log(var_4514.astype('float32')) # shape=(6, 2, 12)
func_984_call = mod.get_global_var('func_984')
func_987_call = mutated_mod.get_global_var('func_987')
var_4536 = relay.var("var_4536", dtype = "uint32", shape = (104,))#candidate|4536|(104,)|var|uint32
call_4535 = func_984_call(relay.reshape(var_4536.astype('uint32'), [1, 13, 8]))
call_4537 = func_984_call(relay.reshape(var_4536.astype('uint32'), [1, 13, 8]))
output = relay.Tuple([bop_4515,uop_4529,call_4535,var_4536,])
output2 = relay.Tuple([bop_4518,uop_4529,call_4537,var_4536,])
func_4545 = relay.Function([var_4514,var_4536,], output)
mod['func_4545'] = func_4545
mod = relay.transform.InferType()(mod)
mutated_mod['func_4545'] = func_4545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4545_call = mutated_mod.get_global_var('func_4545')
var_4547 = relay.var("var_4547", dtype = "float32", shape = (6, 2, 12))#candidate|4547|(6, 2, 12)|var|float32
var_4548 = relay.var("var_4548", dtype = "uint32", shape = (104,))#candidate|4548|(104,)|var|uint32
call_4546 = func_4545_call(var_4547,var_4548,)
output = call_4546
func_4549 = relay.Function([var_4547,var_4548,], output)
mutated_mod['func_4549'] = func_4549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mod.get_global_var('func_2751')
func_2752_call = mutated_mod.get_global_var('func_2752')
call_4595 = func_2751_call()
call_4596 = func_2751_call()
output = call_4595
output2 = call_4596
func_4600 = relay.Function([], output)
mod['func_4600'] = func_4600
mod = relay.transform.InferType()(mod)
mutated_mod['func_4600'] = func_4600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4600_call = mutated_mod.get_global_var('func_4600')
call_4601 = func_4600_call()
output = call_4601
func_4602 = relay.Function([], output)
mutated_mod['func_4602'] = func_4602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_691_call = mod.get_global_var('func_691')
func_693_call = mutated_mod.get_global_var('func_693')
call_4629 = relay.TupleGetItem(func_691_call(), 1)
call_4630 = relay.TupleGetItem(func_693_call(), 1)
output = call_4629
output2 = call_4630
func_4632 = relay.Function([], output)
mod['func_4632'] = func_4632
mod = relay.transform.InferType()(mod)
mutated_mod['func_4632'] = func_4632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4632_call = mutated_mod.get_global_var('func_4632')
call_4633 = func_4632_call()
output = call_4633
func_4634 = relay.Function([], output)
mutated_mod['func_4634'] = func_4634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4148_call = mod.get_global_var('func_4148')
func_4150_call = mutated_mod.get_global_var('func_4150')
call_4705 = func_4148_call()
call_4706 = func_4148_call()
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_4725 = func_465_call()
call_4726 = func_465_call()
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_4733 = func_1084_call()
call_4734 = func_1084_call()
func_2121_call = mod.get_global_var('func_2121')
func_2122_call = mutated_mod.get_global_var('func_2122')
call_4736 = func_2121_call()
call_4737 = func_2121_call()
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
const_4741 = relay.const([[True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True]], dtype = "bool")#candidate|4741|(1, 180)|const|bool
call_4740 = relay.TupleGetItem(func_2066_call(relay.reshape(const_4741.astype('bool'), [6, 2, 15])), 0)
call_4742 = relay.TupleGetItem(func_2068_call(relay.reshape(const_4741.astype('bool'), [6, 2, 15])), 0)
func_1654_call = mod.get_global_var('func_1654')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_4746 = func_1654_call()
call_4747 = func_1654_call()
output = relay.Tuple([call_4705,call_4725,call_4733,call_4736,call_4740,const_4741,call_4746,])
output2 = relay.Tuple([call_4706,call_4726,call_4734,call_4737,call_4742,const_4741,call_4747,])
func_4753 = relay.Function([], output)
mod['func_4753'] = func_4753
mod = relay.transform.InferType()(mod)
mutated_mod['func_4753'] = func_4753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4753_call = mutated_mod.get_global_var('func_4753')
call_4754 = func_4753_call()
output = call_4754
func_4755 = relay.Function([], output)
mutated_mod['func_4755'] = func_4755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2985_call = mod.get_global_var('func_2985')
func_2986_call = mutated_mod.get_global_var('func_2986')
call_4773 = relay.TupleGetItem(func_2985_call(), 1)
call_4774 = relay.TupleGetItem(func_2986_call(), 1)
var_4788 = relay.var("var_4788", dtype = "float32", shape = (6, 2, 1))#candidate|4788|(6, 2, 1)|var|float32
bop_4789 = relay.maximum(call_4773.astype('uint16'), relay.reshape(var_4788.astype('uint16'), relay.shape_of(call_4773))) # shape=(6, 2, 1)
bop_4792 = relay.maximum(call_4774.astype('uint16'), relay.reshape(var_4788.astype('uint16'), relay.shape_of(call_4774))) # shape=(6, 2, 1)
output = bop_4789
output2 = bop_4792
func_4795 = relay.Function([var_4788,], output)
mod['func_4795'] = func_4795
mod = relay.transform.InferType()(mod)
mutated_mod['func_4795'] = func_4795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4796 = relay.var("var_4796", dtype = "float32", shape = (6, 2, 1))#candidate|4796|(6, 2, 1)|var|float32
func_4795_call = mutated_mod.get_global_var('func_4795')
call_4797 = func_4795_call(var_4796)
output = call_4797
func_4798 = relay.Function([var_4796], output)
mutated_mod['func_4798'] = func_4798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2426_call = mod.get_global_var('func_2426')
func_2428_call = mutated_mod.get_global_var('func_2428')
call_4848 = relay.TupleGetItem(func_2426_call(), 0)
call_4849 = relay.TupleGetItem(func_2428_call(), 0)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_4880 = relay.TupleGetItem(func_2042_call(), 0)
call_4881 = relay.TupleGetItem(func_2044_call(), 0)
output = relay.Tuple([call_4848,call_4880,])
output2 = relay.Tuple([call_4849,call_4881,])
func_4896 = relay.Function([], output)
mod['func_4896'] = func_4896
mod = relay.transform.InferType()(mod)
output = func_4896()
func_4897 = relay.Function([], output)
mutated_mod['func_4897'] = func_4897
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4935 = relay.var("var_4935", dtype = "float64", shape = (9, 14, 12))#candidate|4935|(9, 14, 12)|var|float64
uop_4936 = relay.log10(var_4935.astype('float64')) # shape=(9, 14, 12)
output = uop_4936
output2 = uop_4936
func_4940 = relay.Function([var_4935,], output)
mod['func_4940'] = func_4940
mod = relay.transform.InferType()(mod)
mutated_mod['func_4940'] = func_4940
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4941 = relay.var("var_4941", dtype = "float64", shape = (9, 14, 12))#candidate|4941|(9, 14, 12)|var|float64
func_4940_call = mutated_mod.get_global_var('func_4940')
call_4942 = func_4940_call(var_4941)
output = call_4942
func_4943 = relay.Function([var_4941], output)
mutated_mod['func_4943'] = func_4943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1275_call = mod.get_global_var('func_1275')
func_1276_call = mutated_mod.get_global_var('func_1276')
call_4958 = relay.TupleGetItem(func_1275_call(), 1)
call_4959 = relay.TupleGetItem(func_1276_call(), 1)
uop_4976 = relay.log10(call_4958.astype('float32')) # shape=(6, 2, 1)
uop_4978 = relay.log10(call_4959.astype('float32')) # shape=(6, 2, 1)
func_4600_call = mod.get_global_var('func_4600')
func_4602_call = mutated_mod.get_global_var('func_4602')
call_4982 = func_4600_call()
call_4983 = func_4600_call()
bop_4989 = relay.floor_divide(uop_4976.astype('float32'), relay.reshape(call_4982.astype('float32'), relay.shape_of(uop_4976))) # shape=(6, 2, 1)
bop_4992 = relay.floor_divide(uop_4978.astype('float32'), relay.reshape(call_4983.astype('float32'), relay.shape_of(uop_4978))) # shape=(6, 2, 1)
output = bop_4989
output2 = bop_4992
func_4994 = relay.Function([], output)
mod['func_4994'] = func_4994
mod = relay.transform.InferType()(mod)
output = func_4994()
func_4995 = relay.Function([], output)
mutated_mod['func_4995'] = func_4995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_4998 = relay.TupleGetItem(func_1986_call(), 0)
call_4999 = relay.TupleGetItem(func_1988_call(), 0)
output = relay.Tuple([call_4998,])
output2 = relay.Tuple([call_4999,])
func_5009 = relay.Function([], output)
mod['func_5009'] = func_5009
mod = relay.transform.InferType()(mod)
output = func_5009()
func_5010 = relay.Function([], output)
mutated_mod['func_5010'] = func_5010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
call_5025 = func_941_call()
call_5026 = func_941_call()
output = relay.Tuple([call_5025,])
output2 = relay.Tuple([call_5026,])
func_5034 = relay.Function([], output)
mod['func_5034'] = func_5034
mod = relay.transform.InferType()(mod)
output = func_5034()
func_5035 = relay.Function([], output)
mutated_mod['func_5035'] = func_5035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3108_call = mod.get_global_var('func_3108')
func_3109_call = mutated_mod.get_global_var('func_3109')
call_5046 = relay.TupleGetItem(func_3108_call(), 0)
call_5047 = relay.TupleGetItem(func_3109_call(), 0)
func_623_call = mod.get_global_var('func_623')
func_626_call = mutated_mod.get_global_var('func_626')
var_5061 = relay.var("var_5061", dtype = "uint8", shape = (18,))#candidate|5061|(18,)|var|uint8
var_5062 = relay.var("var_5062", dtype = "uint8", shape = (54, 2))#candidate|5062|(54, 2)|var|uint8
call_5060 = func_623_call(relay.reshape(var_5061.astype('uint8'), [6, 3, 1]), relay.reshape(var_5062.astype('uint8'), [6, 3, 6]), )
call_5063 = func_623_call(relay.reshape(var_5061.astype('uint8'), [6, 3, 1]), relay.reshape(var_5062.astype('uint8'), [6, 3, 6]), )
output = relay.Tuple([call_5046,call_5060,var_5061,var_5062,])
output2 = relay.Tuple([call_5047,call_5063,var_5061,var_5062,])
func_5067 = relay.Function([var_5061,var_5062,], output)
mod['func_5067'] = func_5067
mod = relay.transform.InferType()(mod)
mutated_mod['func_5067'] = func_5067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5067_call = mutated_mod.get_global_var('func_5067')
var_5069 = relay.var("var_5069", dtype = "uint8", shape = (18,))#candidate|5069|(18,)|var|uint8
var_5070 = relay.var("var_5070", dtype = "uint8", shape = (54, 2))#candidate|5070|(54, 2)|var|uint8
call_5068 = func_5067_call(var_5069,var_5070,)
output = call_5068
func_5071 = relay.Function([var_5069,var_5070,], output)
mutated_mod['func_5071'] = func_5071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1226_call = mod.get_global_var('func_1226')
func_1227_call = mutated_mod.get_global_var('func_1227')
call_5103 = func_1226_call()
call_5104 = func_1226_call()
func_3522_call = mod.get_global_var('func_3522')
func_3524_call = mutated_mod.get_global_var('func_3524')
call_5123 = func_3522_call()
call_5124 = func_3522_call()
output = relay.Tuple([call_5103,call_5123,])
output2 = relay.Tuple([call_5104,call_5124,])
func_5134 = relay.Function([], output)
mod['func_5134'] = func_5134
mod = relay.transform.InferType()(mod)
mutated_mod['func_5134'] = func_5134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5134_call = mutated_mod.get_global_var('func_5134')
call_5135 = func_5134_call()
output = call_5135
func_5136 = relay.Function([], output)
mutated_mod['func_5136'] = func_5136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1415_call = mod.get_global_var('func_1415')
func_1416_call = mutated_mod.get_global_var('func_1416')
call_5182 = func_1415_call()
call_5183 = func_1415_call()
func_1654_call = mod.get_global_var('func_1654')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_5234 = func_1654_call()
call_5235 = func_1654_call()
func_984_call = mod.get_global_var('func_984')
func_987_call = mutated_mod.get_global_var('func_987')
const_5250 = relay.const([[6,-8,-7,1],[-2,-10,6,-6],[-10,2,1,-8],[5,3,-4,6],[4,6,-2,-3],[-9,1,-6,6],[10,-8,9,3],[9,-4,10,10],[-6,5,3,-2],[-3,-8,10,5],[-4,-10,-8,-7],[-6,10,2,1],[-8,6,6,-2],[3,-10,-5,-10],[9,-2,-2,5],[-3,-5,5,-5],[-4,-4,10,-1],[-7,-3,-7,1],[-4,4,3,5],[4,-1,6,2],[6,10,2,-9],[2,1,-9,-7],[5,-9,3,-6],[-4,6,4,7],[5,-8,-9,-8],[-10,-2,1,-2]], dtype = "uint32")#candidate|5250|(26, 4)|const|uint32
call_5249 = func_984_call(relay.reshape(const_5250.astype('uint32'), [1, 13, 8]))
call_5251 = func_984_call(relay.reshape(const_5250.astype('uint32'), [1, 13, 8]))
func_4896_call = mod.get_global_var('func_4896')
func_4897_call = mutated_mod.get_global_var('func_4897')
call_5259 = relay.TupleGetItem(func_4896_call(), 0)
call_5260 = relay.TupleGetItem(func_4897_call(), 0)
uop_5291 = relay.acosh(call_5249.astype('float32')) # shape=(10, 13, 8)
uop_5293 = relay.acosh(call_5251.astype('float32')) # shape=(10, 13, 8)
var_5304 = relay.var("var_5304", dtype = "uint32", shape = (10, 13, 8))#candidate|5304|(10, 13, 8)|var|uint32
bop_5305 = relay.bitwise_xor(call_5249.astype('uint64'), relay.reshape(var_5304.astype('uint64'), relay.shape_of(call_5249))) # shape=(10, 13, 8)
bop_5308 = relay.bitwise_xor(call_5251.astype('uint64'), relay.reshape(var_5304.astype('uint64'), relay.shape_of(call_5251))) # shape=(10, 13, 8)
func_4896_call = mod.get_global_var('func_4896')
func_4897_call = mutated_mod.get_global_var('func_4897')
call_5309 = relay.TupleGetItem(func_4896_call(), 0)
call_5310 = relay.TupleGetItem(func_4897_call(), 0)
bop_5330 = relay.right_shift(uop_5291.astype('uint64'), relay.reshape(var_5304.astype('uint64'), relay.shape_of(uop_5291))) # shape=(10, 13, 8)
bop_5333 = relay.right_shift(uop_5293.astype('uint64'), relay.reshape(var_5304.astype('uint64'), relay.shape_of(uop_5293))) # shape=(10, 13, 8)
func_4266_call = mod.get_global_var('func_4266')
func_4267_call = mutated_mod.get_global_var('func_4267')
call_5359 = func_4266_call()
call_5360 = func_4266_call()
output = relay.Tuple([call_5182,call_5234,const_5250,call_5259,bop_5305,call_5309,bop_5330,call_5359,])
output2 = relay.Tuple([call_5183,call_5235,const_5250,call_5260,bop_5308,call_5310,bop_5333,call_5360,])
func_5361 = relay.Function([var_5304,], output)
mod['func_5361'] = func_5361
mod = relay.transform.InferType()(mod)
mutated_mod['func_5361'] = func_5361
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5362 = relay.var("var_5362", dtype = "uint32", shape = (10, 13, 8))#candidate|5362|(10, 13, 8)|var|uint32
func_5361_call = mutated_mod.get_global_var('func_5361')
call_5363 = func_5361_call(var_5362)
output = call_5363
func_5364 = relay.Function([var_5362], output)
mutated_mod['func_5364'] = func_5364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5134_call = mod.get_global_var('func_5134')
func_5136_call = mutated_mod.get_global_var('func_5136')
call_5381 = relay.TupleGetItem(func_5134_call(), 0)
call_5382 = relay.TupleGetItem(func_5136_call(), 0)
output = call_5381
output2 = call_5382
func_5387 = relay.Function([], output)
mod['func_5387'] = func_5387
mod = relay.transform.InferType()(mod)
mutated_mod['func_5387'] = func_5387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5387_call = mutated_mod.get_global_var('func_5387')
call_5388 = func_5387_call()
output = call_5388
func_5389 = relay.Function([], output)
mutated_mod['func_5389'] = func_5389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4896_call = mod.get_global_var('func_4896')
func_4897_call = mutated_mod.get_global_var('func_4897')
call_5390 = relay.TupleGetItem(func_4896_call(), 1)
call_5391 = relay.TupleGetItem(func_4897_call(), 1)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
var_5411 = relay.var("var_5411", dtype = "float64", shape = (48,))#candidate|5411|(48,)|var|float64
call_5410 = relay.TupleGetItem(func_1883_call(relay.reshape(var_5411.astype('float64'), [6, 2, 4])), 2)
call_5412 = relay.TupleGetItem(func_1885_call(relay.reshape(var_5411.astype('float64'), [6, 2, 4])), 2)
func_3852_call = mod.get_global_var('func_3852')
func_3854_call = mutated_mod.get_global_var('func_3854')
const_5418 = relay.const([7.165919,-7.190008,9.263994,-4.190933,1.814289,-5.399840,-9.619080,-7.792166,9.672860,2.517940,-5.071416,9.377355,6.694734,-5.791917,5.574590,5.056689,-8.204497,6.624950,-0.394375,-5.328605,-3.946807,8.478709,-0.156880,4.945895,-1.119089,-4.309348,-2.329865,-3.318897,-4.965089,-3.788119,5.646501,-9.954854,6.333680,-4.729269,-3.469344,8.492122,8.474991,9.775447,3.239361,1.209598,9.251044,-3.684770,2.969755,-3.777109,9.896946,4.515827,-0.367306,9.952130,9.293459,2.587009,-2.953474,7.862598,9.069622,9.612139,8.368320,-3.270470,-7.511011,-8.192926,4.323944,9.343696,2.041342,-6.221137,4.711420,2.150527,0.389271,-5.988792,6.037994,7.036836,-3.015077,6.194130,5.086258,3.462200,-0.324289,9.168818,-4.202178,8.559053,6.522139,7.177896,6.997236,-1.352824,-0.306261,-5.517623,-4.315450,-6.768794,-9.720262,-7.735972,-6.072917,-6.579380,4.541073,-5.903868,-4.835432,5.164319,7.935823,-2.272907,0.533370,3.317878,4.124377,2.842060,9.725975,9.712347,-8.731159,7.026302,2.758455,5.037921,1.689723,-1.239511,4.020981,-7.956271,-8.697185,8.537306,3.267966,2.910772,-0.540041,-4.436176,9.004505,-7.793565,7.004270,-9.033491,6.383969,9.604845,1.727611,-8.507204,8.036040,-8.040398,-6.282951,3.897037,-9.083419,-6.036359,9.903924,7.212208,-4.499408,-9.640703,7.944784,-5.290523,6.236593,-4.894030,0.794703,7.356036,8.398514,8.907062,-7.796165,4.173326,1.871557,4.346870,-7.348451,1.552929,-6.770972,-5.013781,-9.943580,-5.527526,-8.517386,5.104147,-0.828091,-8.799188,-4.658593,4.832564,-0.733434,1.562358,-0.021745,-1.054947,3.295182,-4.914657,-6.696187,-6.315818,0.684542,-6.674156,7.041221,-8.137346,-1.773585,3.187799,-0.175467,6.922400,9.749578,-9.160082,-2.200280,-5.352078,1.710750,1.235582,1.250677,-1.544779,7.050471,-8.291048,-7.386173,-9.719262,2.611182,3.946441,-5.344752,-4.179684,-8.286403,9.076506,2.035748,-4.702467,-9.043464,-4.990017,2.234590,3.558954,1.438500,3.234821,-5.048917,7.620763,0.586248,3.754883,5.799108,7.079646,-0.200004,-5.804376,-7.877479,-3.884063,9.068867,-6.580536,-7.868570,0.117283,1.834025,0.687324,-5.314170,6.093962,-5.639859,5.100285,-9.655592,1.581337,9.244841,6.550158,-7.341989,0.714207,-1.714548,5.632271,4.313638,1.407455,0.468082,-0.809289,3.502888,-8.960067,-4.750151,4.681784,-5.990914,5.556001,2.442846,-4.050789,8.702337,2.410493,1.760015,-4.666969,9.487603,-6.899538,-5.066582,-6.564325,-1.616047,8.014592,-3.336488,-9.108594,0.044743,-1.432448,-9.025730,8.819859,-1.669384,6.153231,2.515362,-8.421451,1.253673,2.830156,8.676381,7.292195,-6.596745,-9.676709,-7.192224,-5.114272,6.908473,-9.701557,7.512072,1.008527,-0.697525,6.927811,-6.386655,-0.700808,-4.728490,4.868209,4.682631,-9.485542,-5.341684,-1.173189], dtype = "float32")#candidate|5418|(280,)|const|float32
call_5417 = relay.TupleGetItem(func_3852_call(relay.reshape(const_5418.astype('float32'), [14, 5, 4])), 0)
call_5419 = relay.TupleGetItem(func_3854_call(relay.reshape(const_5418.astype('float32'), [14, 5, 4])), 0)
bop_5425 = relay.bitwise_or(var_5411.astype('int64'), call_5390.astype('int64')) # shape=(6, 2, 48)
bop_5428 = relay.bitwise_or(var_5411.astype('int64'), call_5391.astype('int64')) # shape=(6, 2, 48)
output = relay.Tuple([call_5410,call_5417,const_5418,bop_5425,])
output2 = relay.Tuple([call_5412,call_5419,const_5418,bop_5428,])
func_5446 = relay.Function([var_5411,], output)
mod['func_5446'] = func_5446
mod = relay.transform.InferType()(mod)
mutated_mod['func_5446'] = func_5446
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5447 = relay.var("var_5447", dtype = "float64", shape = (48,))#candidate|5447|(48,)|var|float64
func_5446_call = mutated_mod.get_global_var('func_5446')
call_5448 = func_5446_call(var_5447)
output = call_5448
func_5449 = relay.Function([var_5447], output)
mutated_mod['func_5449'] = func_5449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_566_call = mod.get_global_var('func_566')
func_568_call = mutated_mod.get_global_var('func_568')
call_5468 = func_566_call()
call_5469 = func_566_call()
func_2397_call = mod.get_global_var('func_2397')
func_2400_call = mutated_mod.get_global_var('func_2400')
var_5485 = relay.var("var_5485", dtype = "int16", shape = (1024,))#candidate|5485|(1024,)|var|int16
call_5484 = relay.TupleGetItem(func_2397_call(relay.reshape(var_5485.astype('int16'), [16, 16, 4])), 0)
call_5486 = relay.TupleGetItem(func_2400_call(relay.reshape(var_5485.astype('int16'), [16, 16, 4])), 0)
output = relay.Tuple([call_5468,call_5484,var_5485,])
output2 = relay.Tuple([call_5469,call_5486,var_5485,])
func_5499 = relay.Function([var_5485,], output)
mod['func_5499'] = func_5499
mod = relay.transform.InferType()(mod)
mutated_mod['func_5499'] = func_5499
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5500 = relay.var("var_5500", dtype = "int16", shape = (1024,))#candidate|5500|(1024,)|var|int16
func_5499_call = mutated_mod.get_global_var('func_5499')
call_5501 = func_5499_call(var_5500)
output = call_5501
func_5502 = relay.Function([var_5500], output)
mutated_mod['func_5502'] = func_5502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2985_call = mod.get_global_var('func_2985')
func_2986_call = mutated_mod.get_global_var('func_2986')
call_5609 = relay.TupleGetItem(func_2985_call(), 0)
call_5610 = relay.TupleGetItem(func_2986_call(), 0)
output = relay.Tuple([call_5609,])
output2 = relay.Tuple([call_5610,])
func_5615 = relay.Function([], output)
mod['func_5615'] = func_5615
mod = relay.transform.InferType()(mod)
mutated_mod['func_5615'] = func_5615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mutated_mod.get_global_var('func_5615')
call_5616 = func_5615_call()
output = call_5616
func_5617 = relay.Function([], output)
mutated_mod['func_5617'] = func_5617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2361_call = mod.get_global_var('func_2361')
func_2363_call = mutated_mod.get_global_var('func_2363')
call_5652 = func_2361_call()
call_5653 = func_2361_call()
output = call_5652
output2 = call_5653
func_5667 = relay.Function([], output)
mod['func_5667'] = func_5667
mod = relay.transform.InferType()(mod)
output = func_5667()
func_5668 = relay.Function([], output)
mutated_mod['func_5668'] = func_5668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5134_call = mod.get_global_var('func_5134')
func_5136_call = mutated_mod.get_global_var('func_5136')
call_5719 = relay.TupleGetItem(func_5134_call(), 1)
call_5720 = relay.TupleGetItem(func_5136_call(), 1)
func_3206_call = mod.get_global_var('func_3206')
func_3208_call = mutated_mod.get_global_var('func_3208')
call_5725 = func_3206_call()
call_5726 = func_3206_call()
output = relay.Tuple([call_5719,call_5725,])
output2 = relay.Tuple([call_5720,call_5726,])
func_5734 = relay.Function([], output)
mod['func_5734'] = func_5734
mod = relay.transform.InferType()(mod)
output = func_5734()
func_5735 = relay.Function([], output)
mutated_mod['func_5735'] = func_5735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2361_call = mod.get_global_var('func_2361')
func_2363_call = mutated_mod.get_global_var('func_2363')
call_5740 = func_2361_call()
call_5741 = func_2361_call()
func_2515_call = mod.get_global_var('func_2515')
func_2518_call = mutated_mod.get_global_var('func_2518')
const_5760 = relay.const([4.317912,1.457831,8.149786,2.682162,-7.659780,5.649470,-0.132232,4.686498,-7.862234,-4.664908,5.453795,6.219029,-1.683441,-0.509515,-3.623269,-9.855662,-4.867282,3.767236,-7.416648,-5.656051,-3.502957,-2.128529,-0.453405,-2.175846,7.641661,8.024180,0.598002,-2.248359,-8.428149,1.941387,7.865858,4.577362,6.313216,6.499976,3.484823,-4.098821,7.620998,0.646583,-0.064003,-2.332491,-3.910596,-2.679652,4.575203,-6.670875,3.047330,-7.007843,1.760480,-8.327769,-6.960755,-6.998356,-5.419225,-3.450256,9.766889,3.160187,6.378609,-9.148312,2.251416,9.550850,6.935667,9.461591,9.169185,5.864787,3.230971,-9.316943,2.085398,7.476916,8.397081,-2.908157,7.676972,5.778683,5.448208,5.241951,-2.852841,6.728520,-9.907037,5.302899,3.389237,-6.281486,-9.814165,-3.509864,-8.514947,0.335779,8.150461,-1.067193,7.800746,-6.643215,4.333269,-0.711662,-4.740122,2.610936,-4.630523,5.756647,2.273635,-4.132079,-0.562981,-1.807398,-8.933984,-5.941435,0.030613,2.510662,-6.376570,3.701787,2.691446,-6.620079,-1.581593,-9.254326,-5.968321,-0.503839,9.323650,4.072853,7.196680,-2.752849,-1.014740,-9.875304,-8.774577,-9.805207,8.068124,-0.691319,1.554306,-3.830935,7.767277,-5.210394,-7.161151,7.285502,6.121687,7.010415,-6.698056,1.377825,4.107541,-1.400195,1.950575,-8.952095,5.343512,1.517689,7.797091,-6.831137,-2.667445,-2.064187,6.891500,-6.519378,3.787766,9.491319,-5.819195,-9.978680,-6.321801,9.601090,7.603664,-1.562324,-9.645985,-9.120746,-5.274521,-2.927774,3.823421,2.576301,9.236566,-0.069654,-0.789844,-7.007233,-3.406743,-7.974465,-6.616142,-8.238739,8.930615,-0.493564,-5.105033,-0.330032,6.966651,4.341966,2.120798,9.219630,-5.681163,0.986785,2.651131,2.112136,-3.439179,0.825621,3.293430,8.323434,-1.097600,6.468697,-5.291080,5.439161,-4.635288,-6.660699,-6.619183,-2.303726,0.626133,4.398243,-8.991118,-0.141544,-0.468467,5.936336,3.964467,-1.937938,-2.977554,-8.211535,0.436069,-4.739948,-8.117743,-3.785809,-8.373748,-5.857179,-9.479405,-4.078776,-2.627215,-2.327417,-8.726959,4.780504,-3.844752,-1.015569,8.183294,0.581735,-2.312422,-8.282455,-8.584391,7.372500,-2.162763,5.045291,7.133435,6.860213,-9.398005,-4.618397,6.112476,3.917343,-6.186219,-3.458293,-8.100748,-3.140962,6.249284,-6.178358,4.315994,-6.101613,5.692921,2.556023,7.503704,-6.612800,-5.070735,4.720253,-2.521909,1.181769,-8.331738,-7.885770,0.450858,6.447065,-6.037648,-9.204625,-4.405562,7.359709,-2.891991,-9.708312,0.749840,-8.320729,-8.198246,6.026592,-3.862852,9.808812,-2.252283,8.357550,-7.352454,-8.713343,-0.393098,6.786885,1.246693,-0.360715,9.698638,6.749462,-3.365777,-5.508626,3.827184,1.359171], dtype = "float64")#candidate|5760|(270,)|const|float64
call_5759 = func_2515_call(relay.reshape(const_5760.astype('float64'), [3, 15, 6]))
call_5761 = func_2515_call(relay.reshape(const_5760.astype('float64'), [3, 15, 6]))
uop_5800 = relay.asinh(call_5759.astype('float32')) # shape=(3, 15, 6)
uop_5802 = relay.asinh(call_5761.astype('float32')) # shape=(3, 15, 6)
output = relay.Tuple([call_5740,const_5760,uop_5800,])
output2 = relay.Tuple([call_5741,const_5760,uop_5802,])
func_5814 = relay.Function([], output)
mod['func_5814'] = func_5814
mod = relay.transform.InferType()(mod)
output = func_5814()
func_5815 = relay.Function([], output)
mutated_mod['func_5815'] = func_5815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2751_call = mod.get_global_var('func_2751')
func_2752_call = mutated_mod.get_global_var('func_2752')
call_5838 = func_2751_call()
call_5839 = func_2751_call()
func_1139_call = mod.get_global_var('func_1139')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_5843 = relay.TupleGetItem(func_1139_call(), 0)
call_5844 = relay.TupleGetItem(func_1141_call(), 0)
output = relay.Tuple([call_5838,call_5843,])
output2 = relay.Tuple([call_5839,call_5844,])
func_5847 = relay.Function([], output)
mod['func_5847'] = func_5847
mod = relay.transform.InferType()(mod)
mutated_mod['func_5847'] = func_5847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5847_call = mutated_mod.get_global_var('func_5847')
call_5848 = func_5847_call()
output = call_5848
func_5849 = relay.Function([], output)
mutated_mod['func_5849'] = func_5849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_5902 = relay.TupleGetItem(func_1986_call(), 0)
call_5903 = relay.TupleGetItem(func_1988_call(), 0)
output = call_5902
output2 = call_5903
func_5906 = relay.Function([], output)
mod['func_5906'] = func_5906
mod = relay.transform.InferType()(mod)
mutated_mod['func_5906'] = func_5906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5906_call = mutated_mod.get_global_var('func_5906')
call_5907 = func_5906_call()
output = call_5907
func_5908 = relay.Function([], output)
mutated_mod['func_5908'] = func_5908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4600_call = mod.get_global_var('func_4600')
func_4602_call = mutated_mod.get_global_var('func_4602')
call_5961 = func_4600_call()
call_5962 = func_4600_call()
func_237_call = mod.get_global_var('func_237')
func_239_call = mutated_mod.get_global_var('func_239')
call_5966 = relay.TupleGetItem(func_237_call(), 1)
call_5967 = relay.TupleGetItem(func_239_call(), 1)
output = relay.Tuple([call_5961,call_5966,])
output2 = relay.Tuple([call_5962,call_5967,])
func_5978 = relay.Function([], output)
mod['func_5978'] = func_5978
mod = relay.transform.InferType()(mod)
output = func_5978()
func_5979 = relay.Function([], output)
mutated_mod['func_5979'] = func_5979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3708_call = mod.get_global_var('func_3708')
func_3709_call = mutated_mod.get_global_var('func_3709')
call_5983 = relay.TupleGetItem(func_3708_call(), 2)
call_5984 = relay.TupleGetItem(func_3709_call(), 2)
output = call_5983
output2 = call_5984
func_5987 = relay.Function([], output)
mod['func_5987'] = func_5987
mod = relay.transform.InferType()(mod)
mutated_mod['func_5987'] = func_5987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5987_call = mutated_mod.get_global_var('func_5987')
call_5988 = func_5987_call()
output = call_5988
func_5989 = relay.Function([], output)
mutated_mod['func_5989'] = func_5989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_6012 = func_1084_call()
call_6013 = func_1084_call()
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
var_6022 = relay.var("var_6022", dtype = "bool", shape = (180,))#candidate|6022|(180,)|var|bool
call_6021 = relay.TupleGetItem(func_2066_call(relay.reshape(var_6022.astype('bool'), [6, 2, 15])), 0)
call_6023 = relay.TupleGetItem(func_2068_call(relay.reshape(var_6022.astype('bool'), [6, 2, 15])), 0)
bop_6024 = relay.logical_or(call_6021.astype('bool'), var_6022.astype('bool')) # shape=(6, 2, 180)
bop_6027 = relay.logical_or(call_6023.astype('bool'), var_6022.astype('bool')) # shape=(6, 2, 180)
bop_6034 = relay.left_shift(bop_6024.astype('uint32'), var_6022.astype('uint32')) # shape=(6, 2, 180)
bop_6037 = relay.left_shift(bop_6027.astype('uint32'), var_6022.astype('uint32')) # shape=(6, 2, 180)
bop_6038 = relay.not_equal(call_6012.astype('bool'), var_6022.astype('bool')) # shape=(6, 2, 180)
bop_6041 = relay.not_equal(call_6013.astype('bool'), var_6022.astype('bool')) # shape=(6, 2, 180)
func_525_call = mod.get_global_var('func_525')
func_528_call = mutated_mod.get_global_var('func_528')
var_6046 = relay.var("var_6046", dtype = "float32", shape = (364,))#candidate|6046|(364,)|var|float32
call_6045 = relay.TupleGetItem(func_525_call(relay.reshape(var_6046.astype('float32'), [13, 4, 7])), 0)
call_6047 = relay.TupleGetItem(func_528_call(relay.reshape(var_6046.astype('float32'), [13, 4, 7])), 0)
output = relay.Tuple([bop_6034,bop_6038,call_6045,var_6046,])
output2 = relay.Tuple([bop_6037,bop_6041,call_6047,var_6046,])
func_6063 = relay.Function([var_6022,var_6046,], output)
mod['func_6063'] = func_6063
mod = relay.transform.InferType()(mod)
mutated_mod['func_6063'] = func_6063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6063_call = mutated_mod.get_global_var('func_6063')
var_6065 = relay.var("var_6065", dtype = "bool", shape = (180,))#candidate|6065|(180,)|var|bool
var_6066 = relay.var("var_6066", dtype = "float32", shape = (364,))#candidate|6066|(364,)|var|float32
call_6064 = func_6063_call(var_6065,var_6066,)
output = call_6064
func_6067 = relay.Function([var_6065,var_6066,], output)
mutated_mod['func_6067'] = func_6067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
call_6080 = func_941_call()
call_6081 = func_941_call()
output = relay.Tuple([call_6080,])
output2 = relay.Tuple([call_6081,])
func_6082 = relay.Function([], output)
mod['func_6082'] = func_6082
mod = relay.transform.InferType()(mod)
output = func_6082()
func_6083 = relay.Function([], output)
mutated_mod['func_6083'] = func_6083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_6100 = relay.TupleGetItem(func_1186_call(), 0)
call_6101 = relay.TupleGetItem(func_1187_call(), 0)
func_984_call = mod.get_global_var('func_984')
func_987_call = mutated_mod.get_global_var('func_987')
const_6107 = relay.const([10,-3,-7,-7,-1,3,-5,-2,-3,-5,6,-1,1,-6,-1,-2,5,9,2,-3,7,6,10,-4,-2,7,3,9,-10,-2,2,-9,9,-2,-5,3,-10,7,-9,-3,8,-9,8,6,2,6,-3,-10,-4,-3,-7,5,5,9,1,-3,2,1,-7,-7,-8,-3,-9,-3,-5,-3,1,2,-8,-10,-3,-9,4,-2,-10,9,1,8,7,4,-8,-4,7,-4,7,5,6,4,5,-10,6,-4,3,8,1,-2,8,-7,2,-9,7,10,9,3], dtype = "uint32")#candidate|6107|(104,)|const|uint32
call_6106 = func_984_call(relay.reshape(const_6107.astype('uint32'), [1, 13, 8]))
call_6108 = func_984_call(relay.reshape(const_6107.astype('uint32'), [1, 13, 8]))
uop_6128 = relay.erf(call_6106.astype('float32')) # shape=(10, 13, 8)
uop_6130 = relay.erf(call_6108.astype('float32')) # shape=(10, 13, 8)
output = relay.Tuple([call_6100,const_6107,uop_6128,])
output2 = relay.Tuple([call_6101,const_6107,uop_6130,])
func_6135 = relay.Function([], output)
mod['func_6135'] = func_6135
mod = relay.transform.InferType()(mod)
mutated_mod['func_6135'] = func_6135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6135_call = mutated_mod.get_global_var('func_6135')
call_6136 = func_6135_call()
output = call_6136
func_6137 = relay.Function([], output)
mutated_mod['func_6137'] = func_6137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4994_call = mod.get_global_var('func_4994')
func_4995_call = mutated_mod.get_global_var('func_4995')
call_6164 = func_4994_call()
call_6165 = func_4994_call()
output = relay.Tuple([call_6164,])
output2 = relay.Tuple([call_6165,])
func_6170 = relay.Function([], output)
mod['func_6170'] = func_6170
mod = relay.transform.InferType()(mod)
mutated_mod['func_6170'] = func_6170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6170_call = mutated_mod.get_global_var('func_6170')
call_6171 = func_6170_call()
output = call_6171
func_6172 = relay.Function([], output)
mutated_mod['func_6172'] = func_6172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5906_call = mod.get_global_var('func_5906')
func_5908_call = mutated_mod.get_global_var('func_5908')
call_6275 = func_5906_call()
call_6276 = func_5906_call()
const_6278 = relay.const([[[-1.512685,-4.255323,7.920531,9.590061,-8.684230,4.908014,2.257922,-3.839631,-6.824938,3.549257,-2.730469,2.012813,-1.391576],[-9.476031,-2.523494,5.666165,6.990888,-9.738960,7.657374,-3.618226,-0.546148,9.254465,4.866046,-6.054035,1.487053,-7.944893]],[[8.209086,-7.506995,-8.666976,1.919354,-4.358091,3.343512,-1.683295,-4.102081,1.494362,-9.830739,-4.201536,4.029377,5.659683],[3.117556,-0.813721,-7.969481,1.073418,6.050064,7.161451,6.468396,-8.337221,-2.251115,-7.329552,-2.371641,0.270814,-8.620933]],[[0.552592,3.621918,1.378257,2.150427,-2.467464,8.462957,-6.711391,-6.776585,-7.378290,4.311473,-8.520945,6.485398,-1.950352],[4.522295,-9.467841,0.157602,1.203127,8.546068,7.290190,-6.431074,-1.623899,-8.155601,1.991887,4.731609,-5.226986,-4.731369]],[[-6.441979,2.174154,0.730130,-1.237743,-4.826118,0.908473,-2.388442,4.809738,-1.113823,2.808636,7.633231,4.881594,-0.477662],[-6.043072,-9.575164,-3.959881,9.716317,6.030171,-5.187966,-3.021905,-8.581106,-0.362235,-7.550943,-8.887885,-2.004827,-2.367368]],[[2.200915,-7.217561,-1.195257,-2.467631,1.053677,0.575946,9.867471,8.455594,-5.522877,-0.539855,-6.777474,1.685175,-1.114223],[9.874344,8.820549,0.276852,1.128477,4.789444,-0.088304,-8.564844,-2.241423,-4.505267,1.384719,0.692372,-3.405214,-8.245098]],[[-3.263732,5.137841,7.237705,0.524814,-1.633155,-7.123625,-9.788911,4.995202,7.660142,-8.238505,0.209941,8.441767,8.811327],[-9.564356,5.268392,-7.993368,-8.764573,-4.704062,-6.042293,8.836342,-4.146171,-0.269515,7.134164,-2.100322,-7.096411,-9.301744]]], dtype = "float64")#candidate|6278|(6, 2, 13)|const|float64
bop_6279 = relay.less(call_6275.astype('bool'), const_6278.astype('bool')) # shape=(6, 2, 13)
bop_6282 = relay.less(call_6276.astype('bool'), const_6278.astype('bool')) # shape=(6, 2, 13)
output = bop_6279
output2 = bop_6282
func_6287 = relay.Function([], output)
mod['func_6287'] = func_6287
mod = relay.transform.InferType()(mod)
output = func_6287()
func_6288 = relay.Function([], output)
mutated_mod['func_6288'] = func_6288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5387_call = mod.get_global_var('func_5387')
func_5389_call = mutated_mod.get_global_var('func_5389')
call_6311 = func_5387_call()
call_6312 = func_5387_call()
output = relay.Tuple([call_6311,])
output2 = relay.Tuple([call_6312,])
func_6318 = relay.Function([], output)
mod['func_6318'] = func_6318
mod = relay.transform.InferType()(mod)
mutated_mod['func_6318'] = func_6318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6318_call = mutated_mod.get_global_var('func_6318')
call_6319 = func_6318_call()
output = call_6319
func_6320 = relay.Function([], output)
mutated_mod['func_6320'] = func_6320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1793_call = mod.get_global_var('func_1793')
func_1794_call = mutated_mod.get_global_var('func_1794')
call_6355 = func_1793_call()
call_6356 = func_1793_call()
func_6287_call = mod.get_global_var('func_6287')
func_6288_call = mutated_mod.get_global_var('func_6288')
call_6367 = func_6287_call()
call_6368 = func_6287_call()
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
var_6370 = relay.var("var_6370", dtype = "float64", shape = (1, 90))#candidate|6370|(1, 90)|var|float64
call_6369 = relay.TupleGetItem(func_2326_call(relay.reshape(var_6370.astype('float64'), [90,])), 6)
call_6371 = relay.TupleGetItem(func_2328_call(relay.reshape(var_6370.astype('float64'), [90,])), 6)
output = relay.Tuple([call_6355,call_6367,call_6369,var_6370,])
output2 = relay.Tuple([call_6356,call_6368,call_6371,var_6370,])
func_6372 = relay.Function([var_6370,], output)
mod['func_6372'] = func_6372
mod = relay.transform.InferType()(mod)
mutated_mod['func_6372'] = func_6372
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6373 = relay.var("var_6373", dtype = "float64", shape = (1, 90))#candidate|6373|(1, 90)|var|float64
func_6372_call = mutated_mod.get_global_var('func_6372')
call_6374 = func_6372_call(var_6373)
output = call_6374
func_6375 = relay.Function([var_6373], output)
mutated_mod['func_6375'] = func_6375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4600_call = mod.get_global_var('func_4600')
func_4602_call = mutated_mod.get_global_var('func_4602')
call_6538 = func_4600_call()
call_6539 = func_4600_call()
output = relay.Tuple([call_6538,])
output2 = relay.Tuple([call_6539,])
func_6543 = relay.Function([], output)
mod['func_6543'] = func_6543
mod = relay.transform.InferType()(mod)
mutated_mod['func_6543'] = func_6543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6543_call = mutated_mod.get_global_var('func_6543')
call_6544 = func_6543_call()
output = call_6544
func_6545 = relay.Function([], output)
mutated_mod['func_6545'] = func_6545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2223_call = mod.get_global_var('func_2223')
func_2225_call = mutated_mod.get_global_var('func_2225')
call_6564 = relay.TupleGetItem(func_2223_call(), 1)
call_6565 = relay.TupleGetItem(func_2225_call(), 1)
func_3184_call = mod.get_global_var('func_3184')
func_3187_call = mutated_mod.get_global_var('func_3187')
var_6572 = relay.var("var_6572", dtype = "uint8", shape = (1620,))#candidate|6572|(1620,)|var|uint8
call_6571 = func_3184_call(relay.reshape(var_6572.astype('uint8'), [12, 15, 9]))
call_6573 = func_3184_call(relay.reshape(var_6572.astype('uint8'), [12, 15, 9]))
func_4994_call = mod.get_global_var('func_4994')
func_4995_call = mutated_mod.get_global_var('func_4995')
call_6574 = func_4994_call()
call_6575 = func_4994_call()
bop_6588 = relay.right_shift(call_6574.astype('int16'), relay.reshape(call_6564.astype('int16'), relay.shape_of(call_6574))) # shape=(6, 2, 1)
bop_6591 = relay.right_shift(call_6575.astype('int16'), relay.reshape(call_6565.astype('int16'), relay.shape_of(call_6575))) # shape=(6, 2, 1)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_6594 = relay.TupleGetItem(func_1986_call(), 0)
call_6595 = relay.TupleGetItem(func_1988_call(), 0)
func_4266_call = mod.get_global_var('func_4266')
func_4267_call = mutated_mod.get_global_var('func_4267')
call_6607 = func_4266_call()
call_6608 = func_4266_call()
var_6609 = relay.var("var_6609", dtype = "uint8", shape = (1620,))#candidate|6609|(1620,)|var|uint8
bop_6610 = relay.maximum(var_6572.astype('float32'), relay.reshape(var_6609.astype('float32'), relay.shape_of(var_6572))) # shape=(1620,)
uop_6620 = relay.cos(call_6571.astype('float64')) # shape=(12, 15, 9)
uop_6622 = relay.cos(call_6573.astype('float64')) # shape=(12, 15, 9)
func_984_call = mod.get_global_var('func_984')
func_987_call = mutated_mod.get_global_var('func_987')
const_6624 = relay.const([[-10],[-2],[8],[6],[10],[6],[3],[-1],[-4],[9],[-8],[-2],[5],[-9],[-7],[5],[-1],[6],[10],[-1],[-7],[4],[-4],[6],[-5],[8],[7],[6],[-5],[1],[6],[-9],[10],[8],[-9],[-4],[-6],[6],[-5],[-10],[7],[-6],[9],[6],[-6],[7],[-2],[1],[-4],[-4],[8],[7],[6],[3],[-6],[-4],[2],[-9],[3],[-6],[2],[-1],[10],[6],[8],[4],[8],[9],[-5],[-7],[-7],[7],[-4],[-2],[-2],[6],[-10],[8],[-8],[3],[-4],[2],[-8],[-8],[-5],[-7],[-10],[4],[1],[-1],[-4],[6],[-3],[-5],[9],[-4],[3],[-5],[-9],[8],[-9],[-8],[7],[3]], dtype = "uint32")#candidate|6624|(104, 1)|const|uint32
call_6623 = func_984_call(relay.reshape(const_6624.astype('uint32'), [1, 13, 8]))
call_6625 = func_984_call(relay.reshape(const_6624.astype('uint32'), [1, 13, 8]))
uop_6626 = relay.asinh(uop_6620.astype('float64')) # shape=(12, 15, 9)
uop_6628 = relay.asinh(uop_6622.astype('float64')) # shape=(12, 15, 9)
func_4795_call = mod.get_global_var('func_4795')
func_4798_call = mutated_mod.get_global_var('func_4798')
call_6632 = func_4795_call(relay.reshape(call_6564.astype('float32'), [6, 2, 1]))
call_6633 = func_4795_call(relay.reshape(call_6564.astype('float32'), [6, 2, 1]))
output = relay.Tuple([bop_6588,call_6594,call_6607,bop_6610,call_6623,const_6624,uop_6626,call_6632,])
output2 = relay.Tuple([bop_6591,call_6595,call_6608,bop_6610,call_6625,const_6624,uop_6628,call_6633,])
func_6636 = relay.Function([var_6572,var_6609,], output)
mod['func_6636'] = func_6636
mod = relay.transform.InferType()(mod)
mutated_mod['func_6636'] = func_6636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6636_call = mutated_mod.get_global_var('func_6636')
var_6638 = relay.var("var_6638", dtype = "uint8", shape = (1620,))#candidate|6638|(1620,)|var|uint8
var_6639 = relay.var("var_6639", dtype = "uint8", shape = (1620,))#candidate|6639|(1620,)|var|uint8
call_6637 = func_6636_call(var_6638,var_6639,)
output = call_6637
func_6640 = relay.Function([var_6638,var_6639,], output)
mutated_mod['func_6640'] = func_6640
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6657 = relay.var("var_6657", dtype = "int16", shape = (1, 4, 4))#candidate|6657|(1, 4, 4)|var|int16
const_6658 = relay.const([[[5,-6,-6,-1],[4,-8,9,1],[7,-6,-6,-2],[-8,1,5,1]],[[-5,-4,-9,-5],[-3,2,-3,9],[-10,-2,10,9],[-4,-3,2,-3]],[[-3,5,10,-7],[-2,-4,-1,5],[-10,8,-3,-7],[1,-10,-7,9]],[[7,-4,-5,1],[-7,10,-8,9],[-2,-7,8,-3],[-5,2,-5,-2]],[[5,1,-4,-5],[5,-8,10,10],[-6,8,2,-3],[-6,9,-3,4]],[[-4,8,-5,-10],[10,-5,7,6],[-4,-7,8,3],[4,5,-10,7]],[[-6,-3,-2,3],[-3,4,-6,1],[-7,-6,8,-8],[1,2,-4,7]],[[-6,1,5,9],[4,6,-6,-10],[7,7,-5,-2],[2,-6,-2,8]],[[-5,-5,-5,-8],[2,7,-3,2],[-2,9,-5,4],[4,-4,4,4]],[[3,2,8,4],[-6,-9,-1,10],[1,1,-2,-3],[-6,1,-1,9]]], dtype = "int16")#candidate|6658|(10, 4, 4)|const|int16
bop_6659 = relay.less(var_6657.astype('bool'), const_6658.astype('bool')) # shape=(10, 4, 4)
func_2066_call = mod.get_global_var('func_2066')
func_2068_call = mutated_mod.get_global_var('func_2068')
var_6673 = relay.var("var_6673", dtype = "bool", shape = (180,))#candidate|6673|(180,)|var|bool
call_6672 = relay.TupleGetItem(func_2066_call(relay.reshape(var_6673.astype('bool'), [6, 2, 15])), 0)
call_6674 = relay.TupleGetItem(func_2068_call(relay.reshape(var_6673.astype('bool'), [6, 2, 15])), 0)
func_5847_call = mod.get_global_var('func_5847')
func_5849_call = mutated_mod.get_global_var('func_5849')
call_6677 = relay.TupleGetItem(func_5847_call(), 1)
call_6678 = relay.TupleGetItem(func_5849_call(), 1)
func_3522_call = mod.get_global_var('func_3522')
func_3524_call = mutated_mod.get_global_var('func_3524')
call_6679 = func_3522_call()
call_6680 = func_3522_call()
output = relay.Tuple([bop_6659,call_6672,var_6673,call_6677,call_6679,])
output2 = relay.Tuple([bop_6659,call_6674,var_6673,call_6678,call_6680,])
func_6686 = relay.Function([var_6657,var_6673,], output)
mod['func_6686'] = func_6686
mod = relay.transform.InferType()(mod)
mutated_mod['func_6686'] = func_6686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6686_call = mutated_mod.get_global_var('func_6686')
var_6688 = relay.var("var_6688", dtype = "int16", shape = (1, 4, 4))#candidate|6688|(1, 4, 4)|var|int16
var_6689 = relay.var("var_6689", dtype = "bool", shape = (180,))#candidate|6689|(180,)|var|bool
call_6687 = func_6686_call(var_6688,var_6689,)
output = call_6687
func_6690 = relay.Function([var_6688,var_6689,], output)
mutated_mod['func_6690'] = func_6690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3522_call = mod.get_global_var('func_3522')
func_3524_call = mutated_mod.get_global_var('func_3524')
call_6769 = func_3522_call()
call_6770 = func_3522_call()
func_3139_call = mod.get_global_var('func_3139')
func_3142_call = mutated_mod.get_global_var('func_3142')
var_6790 = relay.var("var_6790", dtype = "float32", shape = (810,))#candidate|6790|(810,)|var|float32
call_6789 = func_3139_call(relay.reshape(var_6790.astype('float32'), [6, 9, 15]))
call_6791 = func_3139_call(relay.reshape(var_6790.astype('float32'), [6, 9, 15]))
output = relay.Tuple([call_6769,call_6789,var_6790,])
output2 = relay.Tuple([call_6770,call_6791,var_6790,])
func_6792 = relay.Function([var_6790,], output)
mod['func_6792'] = func_6792
mod = relay.transform.InferType()(mod)
var_6793 = relay.var("var_6793", dtype = "float32", shape = (810,))#candidate|6793|(810,)|var|float32
output = func_6792(var_6793)
func_6794 = relay.Function([var_6793], output)
mutated_mod['func_6794'] = func_6794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2426_call = mod.get_global_var('func_2426')
func_2428_call = mutated_mod.get_global_var('func_2428')
call_6802 = relay.TupleGetItem(func_2426_call(), 0)
call_6803 = relay.TupleGetItem(func_2428_call(), 0)
func_2751_call = mod.get_global_var('func_2751')
func_2752_call = mutated_mod.get_global_var('func_2752')
call_6814 = func_2751_call()
call_6815 = func_2751_call()
func_3422_call = mod.get_global_var('func_3422')
func_3427_call = mutated_mod.get_global_var('func_3427')
var_6821 = relay.var("var_6821", dtype = "uint32", shape = (2, 52))#candidate|6821|(2, 52)|var|uint32
const_6822 = relay.const([4.004687,4.831075,-1.475841,9.373007,-4.010161,-6.087806,-1.136663,-1.576965,5.742504,5.768120,-5.184470,1.211905,5.056948,5.471532,-3.647334,0.693406,-2.820233,-9.272081,-1.570976,6.444932,-8.692091,7.559439,1.584712,-6.589743,-8.237218,8.377409,2.144081,-5.148320,5.331093,0.970696,3.777049,-4.464607,-8.986869,-9.864393,-9.985131,2.442636,7.803197,-6.083385,-7.864722,-9.505425,-9.893288,6.061869,-7.759088,-0.316069,-6.636202,8.686750,-3.591172,0.520105,-8.821447,-1.477594,-7.902404,-7.764317,-8.008300,-8.383664,2.306109,8.028661,-4.866288,5.614654,-1.863157,4.649160,9.615513,-4.217025,-8.171240,-6.643493,0.454179,7.687799,5.019517,-8.186837,-4.833385,-2.338125,5.983524,1.167177,1.996344,-7.903134,-2.640124,-3.158428,-7.124122,-7.516818,-1.899880,-6.574694,8.117516,5.594604,1.190193,-7.527851,5.752808,0.246494,-6.610955,-2.360461,5.323693,3.032568], dtype = "float64")#candidate|6822|(90,)|const|float64
call_6820 = relay.TupleGetItem(func_3422_call(relay.reshape(var_6821.astype('uint32'), [104,]), relay.reshape(var_6821.astype('uint32'), [104,]), relay.reshape(const_6822.astype('float64'), [10, 3, 3]), ), 3)
call_6823 = relay.TupleGetItem(func_3427_call(relay.reshape(var_6821.astype('uint32'), [104,]), relay.reshape(var_6821.astype('uint32'), [104,]), relay.reshape(const_6822.astype('float64'), [10, 3, 3]), ), 3)
output = relay.Tuple([call_6802,call_6814,call_6820,var_6821,const_6822,])
output2 = relay.Tuple([call_6803,call_6815,call_6823,var_6821,const_6822,])
func_6824 = relay.Function([var_6821,], output)
mod['func_6824'] = func_6824
mod = relay.transform.InferType()(mod)
mutated_mod['func_6824'] = func_6824
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6825 = relay.var("var_6825", dtype = "uint32", shape = (2, 52))#candidate|6825|(2, 52)|var|uint32
func_6824_call = mutated_mod.get_global_var('func_6824')
call_6826 = func_6824_call(var_6825)
output = call_6826
func_6827 = relay.Function([var_6825], output)
mutated_mod['func_6827'] = func_6827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5906_call = mod.get_global_var('func_5906')
func_5908_call = mutated_mod.get_global_var('func_5908')
call_6834 = func_5906_call()
call_6835 = func_5906_call()
func_1654_call = mod.get_global_var('func_1654')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_6850 = func_1654_call()
call_6851 = func_1654_call()
func_964_call = mod.get_global_var('func_964')
func_965_call = mutated_mod.get_global_var('func_965')
call_6855 = func_964_call()
call_6856 = func_964_call()
func_3248_call = mod.get_global_var('func_3248')
func_3250_call = mutated_mod.get_global_var('func_3250')
call_6861 = relay.TupleGetItem(func_3248_call(), 0)
call_6862 = relay.TupleGetItem(func_3250_call(), 0)
bop_6883 = relay.floor_mod(call_6855.astype('float64'), relay.reshape(call_6834.astype('float64'), relay.shape_of(call_6855))) # shape=(6, 2, 1)
bop_6886 = relay.floor_mod(call_6856.astype('float64'), relay.reshape(call_6835.astype('float64'), relay.shape_of(call_6856))) # shape=(6, 2, 1)
func_995_call = mod.get_global_var('func_995')
func_996_call = mutated_mod.get_global_var('func_996')
call_6912 = func_995_call()
call_6913 = func_995_call()
func_4896_call = mod.get_global_var('func_4896')
func_4897_call = mutated_mod.get_global_var('func_4897')
call_6914 = relay.TupleGetItem(func_4896_call(), 1)
call_6915 = relay.TupleGetItem(func_4897_call(), 1)
func_5067_call = mod.get_global_var('func_5067')
func_5071_call = mutated_mod.get_global_var('func_5071')
var_6924 = relay.var("var_6924", dtype = "uint8", shape = (18,))#candidate|6924|(18,)|var|uint8
var_6925 = relay.var("var_6925", dtype = "uint8", shape = (108,))#candidate|6925|(108,)|var|uint8
call_6923 = relay.TupleGetItem(func_5067_call(relay.reshape(var_6924.astype('uint8'), [18,]), relay.reshape(var_6925.astype('uint8'), [54, 2]), ), 2)
call_6926 = relay.TupleGetItem(func_5071_call(relay.reshape(var_6924.astype('uint8'), [18,]), relay.reshape(var_6925.astype('uint8'), [54, 2]), ), 2)
func_1330_call = mod.get_global_var('func_1330')
func_1331_call = mutated_mod.get_global_var('func_1331')
call_6946 = relay.TupleGetItem(func_1330_call(), 2)
call_6947 = relay.TupleGetItem(func_1331_call(), 2)
bop_6949 = relay.minimum(call_6946.astype('int32'), relay.reshape(call_6914.astype('int32'), relay.shape_of(call_6946))) # shape=(6, 2, 1)
bop_6952 = relay.minimum(call_6947.astype('int32'), relay.reshape(call_6915.astype('int32'), relay.shape_of(call_6947))) # shape=(6, 2, 1)
output = relay.Tuple([call_6850,call_6861,bop_6883,call_6912,call_6923,var_6924,var_6925,bop_6949,])
output2 = relay.Tuple([call_6851,call_6862,bop_6886,call_6913,call_6926,var_6924,var_6925,bop_6952,])
F = relay.Function([var_6924,var_6925,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6924,var_6925,], output2)
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
